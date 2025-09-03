
def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            if mode == 'encrypt':
                result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            else:
                result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            result += char  
    return result



if __name__ == "__main__":
    print("=== Caesar Cipher Tool ===")
    message = input("Enter your message: ")
    shift_value = int(input("Enter shift value (number): "))
    choice = input("Encrypt or Decrypt (e/d): ").lower()

    if choice == 'e':
        output = caesar_cipher(message, shift_value, mode='encrypt')
        print("\nEncrypted Message:", output)
    elif choice == 'd':
        output = caesar_cipher(message, shift_value, mode='decrypt')
        print("\nDecrypted Message:", output)
    else:
        print("\nInvalid choice! Please select 'e' for encrypt or 'd' for decrypt.")
