# Import necessary libraries
import string

# Define the alphabet
alphabet = string.ascii_uppercase

# Define the encryption function
def encrypt(plaintext, a, b):
    ciphertext = ""
    for char in plaintext:
        if char in alphabet:
            # Convert the character to uppercase
            char = char.upper()
            
            # Apply the affine encryption formula: E(x) = (ax + b) mod 26
            index = (a * alphabet.index(char) + b) % 26
            
            # Append the encrypted character to the ciphertext
            ciphertext += alphabet[index]
        else:
            # Append non-alphabetic characters as they are
            ciphertext += char
    return ciphertext

# Define the decryption function
def decrypt(ciphertext, a, b):
    plaintext = ""
    a_inverse = pow(a, -1, 26)  # Modular multiplicative inverse of a
    
    for char in ciphertext:
        if char in alphabet:
            # Convert the character to uppercase
            char = char.upper()
            
            # Apply the affine decryption formula: D(x) = a_inverse * (x - b) mod 26
            index = (a_inverse * (alphabet.index(char) - b)) % 26
            
            # Append the decrypted character to the plaintext
            plaintext += alphabet[index]
        else:
            # Append non-alphabetic characters as they are
            plaintext += char
    return plaintext

# Example usage
plaintext = "HELLO WORLD"
a = 5
b = 8

# Encryption
ciphertext = encrypt(plaintext, a, b)
print("Ciphertext:", ciphertext)

# Decryption
decrypted_text = decrypt(ciphertext, a, b)
print("Decrypted text:", decrypted_text)
