# Basic Caesar Cipher Encryptor

Welcome to my cryptography learning sandbox! As a student aiming to become a bug bounty hunter and security expert, I know that understanding the absolute basics of data encryption is critical.

This project is a manual implementation of the classic Caesar Cipher. I built it without any complex libraries to force myself to understand how computer memory handles letters and numbers.

## What I Learned Building This

* **ASCII Mathematics:** I learned how every letter is secretly a number in the computer's memory. By using `ord()` to get the number, adding a shift value, and using `chr()` to turn it back into a letter, I applied basic mathematics directly to coding.
* **String Manipulation:** I practiced creating empty strings and safely adding new characters to them one by one using simple `for` loops.
* **Clean Logic:** I kept the variable names incredibly simple and readable so that anyone looking at the code can immediately understand the mathematical flow of the encryption.

## How to Run It

1. Ensure Python is installed on your system.
2. Open your terminal and run the script:
```bash
   python caesar_cipher.py
