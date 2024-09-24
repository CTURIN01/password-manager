import sqlite3, hashlib, getpass, base64, os
from cryptography.fernet import Fernet

class AdvancedVault:
    def __init__(self, db='vault.db'):
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()
        self._create_table()
        self.mp = None
        self.key = None

    def _create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS vault
                          (id INTEGER PRIMARY KEY, service TEXT, username TEXT, password TEXT)''')
        self.conn.commit()

    def _derive_key(self, p, s=None):
        s = os.urandom(16) if s is None else s
        return hashlib.pbkdf2_hmac('sha256', p.encode(), s, 100000), s

    def setup_master(self):
        while True:
            p = getpass.getpass("Set master password: ")
            if p == getpass.getpass("Confirm master password: "):
                self.mp = p
                self.key, salt = self._derive_key(p)
                self.key = base64.urlsafe_b64encode(self.key)
                return salt
            print("Passwords don't match. Try again.")

    def unlock(self, s):
        p = getpass.getpass("Enter master password: ")
        key, _ = self._derive_key(p, s)
        self.key = base64.urlsafe_b64encode(key)
        return p == self.mp

    def add(self, service, username, password):
        if not self.key:
            print("Vault is locked.")
            return
        f = Fernet(self.key)
        encrypted = f.encrypt(password.encode()).decode()
        self.c.execute("INSERT INTO vault (service, username, password) VALUES (?, ?, ?)",
                       (service, username, encrypted))
        self.conn.commit()
        print(f"Entry for {service} added.")

    def get(self, service):
        if not self.key:
            print("Vault is locked.")
            return
        self.c.execute("SELECT username, password FROM vault WHERE service = ?", (service,))
        result = self.c.fetchone()
        if result:
            username, encrypted = result
            f = Fernet(self.key)
            password = f.decrypt(encrypted.encode()).decode()
            return username, password
        return None

    def remove(self, service):
        if not self.key:
            print("Vault is locked.")
            return
        self.c.execute("DELETE FROM vault WHERE service = ?", (service,))
        self.conn.commit()
        print(f"Entry for {service} removed." if self.c.rowcount else f"No entry found for {service}.")

    def close(self):
        self.conn.close()

def main():
    vault = AdvancedVault()
    salt = vault.setup_master()

    while True:
        if not vault.unlock(salt):
            print("Incorrect master password.")
            continue

        print("\n1. Add entry\n2. Get entry\n3. Remove entry\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            vault.add(input("Service: "), input("Username: "), getpass.getpass("Password: "))
        elif choice == '2':
            result = vault.get(input("Service: "))
            if result:
                print(f"Username: {result[0]}\nPassword: {result[1]}")
            else:
                print("Entry not found.")
        elif choice == '3':
            vault.remove(input("Service: "))
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

    vault.close()

if __name__ == "__main__":
    main()