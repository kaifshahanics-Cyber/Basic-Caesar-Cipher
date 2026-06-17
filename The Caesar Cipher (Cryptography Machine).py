# Project: Basic Caesar Cipher
# Made by: Muhammad Kaif Shahani
# Learning how basic cryptography and ASCII values work in Python.

def caesar_cipher():
    # getting message and shift key from the user
    plaintext = input("Enter the message to encrypt: ")
    offset = int(input("Enter the shift number: "))
    
    ciphertext = "" # empty box to store the final secret code
    
    # looping through every single letter
    for character in plaintext:
        code_point = ord(character) # converting letter to its ASCII number
        shifted_code = code_point + offset # adding the secret shift
        cipher_char = chr(shifted_code) # changing the number back to a new letter
        
        ciphertext += cipher_char # joining it to our final message
        
    return ciphertext

print("Encrypted result:", caesar_cipher())

