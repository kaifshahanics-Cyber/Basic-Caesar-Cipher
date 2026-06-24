# Project: Basic Caesar Cipher
# Made by: Muhammad Kaif Shahani
# Learning how basic cryptography works.

print("--- Secret Message Encryptor ---")
user_message = input("Type the message you want to hide: ")
shift_number = int(input("Enter a number to shift the letters (e.g., 3): "))

final_secret_message = ""

# loop through each letter in the user's message
for letter in user_message:
    # changing letter to its ascii math number
    ascii_number = ord(letter)
    
    # adding our shift key to the number
    new_number = ascii_number + shift_number
    
    # changing the new number back to a letter
    new_letter = chr(new_number)
    
    # adding it to our final text
    final_secret_message = final_secret_message + new_letter

print("\nHere is your encrypted result:")
print(final_secret_message)

