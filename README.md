# FILE-INTEGRITY-CHECKER

**COMPANY**: CODTECH IT SOLUTIONS

**NAME**: PITTA MEGHANA

**INTERN ID**: CT12MLF

**DOMAIN**: CYBER SECURITY AND ETHICAL HACKING 

**BATCH DURATION**: FEBRUARY 5th, 2025 to MAY 5th, 2025

**MENTOR NAME**: NEELA SANTHOSH KUMAR

#Enter Description

from Crypto.Cipher import AES #type:ignore
from Crypto.Util.Padding import pad, unpad #type:ignore
from Crypto.Random import get_random_bytes #type:ignore
import os

# File Encryption
def encrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as f:
            plaintext = f.read()

        cipher = AES.new(key, AES.MODE_CBC)
        ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

        encrypted_file_path = file_path + ".enc"
        with open(encrypted_file_path, 'wb') as f:
            f.write(cipher.iv + ciphertext)

        print(f"File encrypted successfully: {encrypted_file_path}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error during encryption: {e}")
# File Decryption
def decrypt_file(encrypted_file_path, key):
    try:
        with open(encrypted_file_path, 'rb') as f:
            iv = f.read(16)  # First 16 bytes for IV
            ciphertext = f.read()  # Remaining bytes for ciphertext

        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

        decrypted_file_path = encrypted_file_path.replace(".enc", "_decrypted")
        with open(decrypted_file_path, 'wb') as f:
            f.write(plaintext)

        print(f"File decrypted successfully: {decrypted_file_path}")
    except FileNotFoundError:
        print(f"Error: Encrypted file '{encrypted_file_path}' not found.")
    except ValueError:
        print("Error: Incorrect decryption key or corrupted file.")
    except Exception as e:
        print(f"Error during decryption: {e}")
# Key Generation
def generate_key():
    return get_random_bytes(32)  # 256-bit key

# Main Menu
def main():
    print("Advanced Encryption Tool")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Generate a new encryption key")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        file_path = input("Enter the file path to encrypt: ")
        key_path = input("Enter the key file path: ")
        try:
            with open(key_path, 'rb') as f:
                key = f.read()
            encrypt_file(file_path, key)
        except FileNotFoundError:
            print(f"Error: Key file '{key_path}' not found.")
    elif choice == "2":
        encrypted_file_path = input("Enter the encrypted file path: ")
        key_path = input("Enter the key file path: ")
        try:
            with open(key_path, 'rb') as f:
              key = f.read()
            decrypt_file(encrypted_file_path, key)
        except FileNotFoundError:
            print(f"Error: Key file '{key_path}' not found.")
    elif choice == "3":
        key = generate_key()
        key_path = input("Enter the path to save the generated key: ")
        try:
            with open(key_path, 'wb') as f:
                f.write(key)
            print(f"Key generated and saved to: {key_path}")
        except Exception as e:
            print(f"Error saving key: {e}")
    else:
        print("Invalid choice. Exiting.")

if "_name__" == "_main_":
    main()
