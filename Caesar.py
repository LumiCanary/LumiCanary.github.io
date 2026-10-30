def caesar_cipher(text: str, shift: int, mode: str = 'encrypt') -> str:
    """
    Encrypts or decrypts a text using the Caesar Cipher technique.
    
    :param text: The input string to process.
    :param shift: The number of positions to shift each letter.
    :param mode: 'encrypt' to shift forward, 'decrypt' to shift backward.
    :return: The processed ciphertext or plaintext string.
    """
    result = []
    
    # Adjust shift direction based on mode
    if mode.lower() == 'decrypt':
        shift = -shift
        
    # Normalize the shift value to stay within 0-25
    shift = shift % 26
    
    for char in text:
        if char.isalpha():
            # Determine ASCII base (65 for 'A', 97 for 'a')
            start = 65 if char.isupper() else 97
            # Shift the character and wrap around using modulo 26
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result.append(new_char)
        else:
            # Leave non-alphabet characters unchanged
            result.append(char)
            
    return "".join(result)


# --- Example Usage ---
if __name__ == "__main__":
    message = "Hello, World! 123"
    key = 4
    
    # Encrypt
    encrypted_msg = caesar_cipher(message, key, mode='encrypt')
    print(f"Original:  {message}")
    print(f"Encrypted: {encrypted_msg}")
    
    # Decrypt
    decrypted_msg = caesar_cipher(encrypted_msg, key, mode='decrypt')
    print(f"Decrypted: {decrypted_msg}")
