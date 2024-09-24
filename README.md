# Password Manager Project
This repository contains two versions of a password manager: a simple version and a more complex version. These projects demonstrate my journey in learning about password management and security concepts.

## Simple Password Manager (passwordmanager.py)
This was my first attempt at creating a password manager. It's a basic implementation focusing on core functionality.

## Features:
Uses JSON for data storage
Provides basic add, get, and remove operations
Simple command-line interface
No encryption (passwords stored in plain text)
Highlights:
Easy to understand and modify
Minimal dependencies (only uses Python's standard library)
Suitable for learning basic concepts of data storage and retrieval

## Advanced Password Manager (passwordmanagerv2.py)
This version represents an evolution of the original concept, incorporating more advanced features and security measures.

## Features:
Uses SQLite for data storage
Implements encryption using the Fernet symmetric encryption
Includes a master password for additional security
Provides add, get, and remove operations with encrypted storage
More robust command-line interface
## Highlights:
Increased security with encryption and master password
Uses a database for more efficient data management
Implements key derivation for enhanced security
More complex structure, demonstrating growth in programming skills
## Comparison
| Feature | Simple Version | Advanced Version | |---------|----------------|-------------------| | Storage | JSON file | SQLite database | | Encryption | None | Fernet symmetric encryption | | Master Password | No | Yes | | Dependencies | Standard library only | Requires 'cryptography' library | | Complexity | Low | Medium | | Security | Low (not for real use) | Moderate (still not for sensitive data) |

## Learning Outcomes
Through these projects, I've learned about:

Basic data storage and retrieval
Command-line interface design
Encryption concepts and implementation
Database usage in Python
Secure coding practices
The importance of user authentication in security applications
These projects demonstrate my progress in understanding both programming concepts and security principles in software development.