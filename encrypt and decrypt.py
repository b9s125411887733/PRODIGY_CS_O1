# Caesar Cipher Program in Python

def encrypt(text, shift):
    """Encrypt the text using Caesar Cipher"""
    encrypted_text = ""
    for char in text:
        # Encrypt uppercase letters
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        # Keep non-alphabetic characters unchanged
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(text, shift):
    """Decrypt the text using Caesar Cipher"""
    decrypted_text = ""
    for char in text:
        # Decrypt uppercase letters
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase letters
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        # Keep non-alphabetic characters unchanged
        else:
            decrypted_text += char
    return decrypted_text


def main():
    print("Caesar Cipher Program")

    # Ask for user input
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value (1-25): "))

    action = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()

    if action == 'e':
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    elif action == 'd':
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid action. Please choose 'e' to encrypt or 'd' to decrypt.")


if __name__ == "__main__":
    main()
