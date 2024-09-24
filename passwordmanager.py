import json, os
from random import randint

class SecretKeeper:
    def __init__(self, f='secrets.json'):
        self.f, self.s = f, self._l()

    def _l(self):
        return json.load(open(self.f)) if os.path.exists(self.f) else {}

    def _s(self):
        json.dump(self.s, open(self.f, 'w'))

    def a(self, k, u, p):
        self.s[k] = {'u': u, 'p': p}
        self._s()
        print(f"Entry for {k} added.")

    def g(self, k):
        return self.s.get(k)

    def r(self, k):
        if k in self.s:
            del self.s[k]
            self._s()
            print(f"Entry for {k} removed.")
        else:
            print(f"No entry found for {k}.")

def m():
    sk = SecretKeeper()
    while True:
        c = input("\n1. Add\n2. Get\n3. Remove\n4. Quit\nChoice: ")
        if c == '1':
            sk.a(input("Key: "), input("Username: "), input("Password: "))
        elif c == '2':
            r = sk.g(input("Key: "))
            print(f"Username: {r['u']}\nPassword: {r['p']}") if r else print("Not found.")
        elif c == '3':
            sk.r(input("Key: "))
        elif c == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    m()