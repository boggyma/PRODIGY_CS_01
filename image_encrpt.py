from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    """Encrypts an image using a simple XOR operation with a key."""
    img = Image.open(image_path)
    img_array = np.array(img)
    
    # Generate the encryption key array
    key_array = np.full_like(img_array, key, dtype=np.uint8)
    
    # Encrypt the image by applying XOR operation
    encrypted_array = np.bitwise_xor(img_array, key_array)
    
    # Convert back to an image
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save('encrypted_image.png')
    print("Image encrypted and saved as 'encrypted_image.png'.")

def decrypt_image(encrypted_image_path, key):
    """Decrypts an image using a simple XOR operation with a key."""
    encrypted_img = Image.open(encrypted_image_path)
    encrypted_array = np.array(encrypted_img)
    
    # Generate the decryption key array
    key_array = np.full_like(encrypted_array, key, dtype=np.uint8)
    
    # Decrypt the image by applying XOR operation
    decrypted_array = np.bitwise_xor(encrypted_array, key_array)
    
    # Convert back to an image
    decrypted_img = Image.fromarray(decrypted_array)
    decrypted_img.save('decrypted_image.png')
    print("Image decrypted and saved as 'decrypted_image.png'.")

def main():
    action = input("Enter 'e' to encrypt or 'd' to decrypt: ").strip().lower()
    
    if action == 'e':
        image_path = input("Enter the path of the image to encrypt: ").strip()
        key = int(input("Enter a key (0-255): ").strip())
        encrypt_image(image_path, key)
    elif action == 'd':
        encrypted_image_path = input("Enter the path of the encrypted image to decrypt: ").strip()
        key = int(input("Enter the key used for encryption (0-255): ").strip())
        decrypt_image(encrypted_image_path, key)
    else:
        print("Invalid action. Please enter 'e' or 'd'.")

if __name__ == "__main__":
    main()
