def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = shift % 26
            start = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr(start + (ord(char) - start + shift_amount) % 26)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(message, shift):
    decrypted_message = ""
    for char in message:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = shift % 26
            start = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr(start + (ord(char) - start - shift_amount) % 26)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

def main():
    print("Welcome to the Caesar Cipher program!")
    
    while True:
        choice = input("Would you like to (E)ncrypt or (D)ecrypt a message? (E/D): ").upper()
        if choice not in ['E', 'D']:
            print("Invalid choice. Please enter 'E' for encrypt or 'D' for decrypt.")
            continue
        
        message = input("Enter the message: ")
        shift = int(input("Enter the shift value (integer): "))
        
        if choice == 'E':
            result = encrypt(message, shift)
            print(f"Encrypted message: {result}")
        elif choice == 'D':
            result = decrypt(message, shift)
            print(f"Decrypted message: {result}")
        
        cont = input("Do you want to perform another operation? (Y/N): ").upper()
        if cont != 'Y':
            break

if __name__ == "__main__":
    main()
