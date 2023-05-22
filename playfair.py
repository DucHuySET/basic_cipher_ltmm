# Playfair Cipher Simulator

# Function to generate the Playfair cipher key table
def generate_key_table(key):
    key = key.upper().replace("J", "I")  # Convert to uppercase and replace J with I
    key = key + "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Append the remaining alphabets
    key = "".join(dict.fromkeys(key))  # Remove duplicate characters
    key_table = [list(key[i:i+5]) for i in range(0, 25, 5)]  # Create a 5x5 matrix
    return key_table

# Function to find the positions of two characters in the key table
def find_positions(key_table, char1, char2):
    pos1 = None
    pos2 = None
    for i in range(5):
        for j in range(5):
            if key_table[i][j] == char1:
                pos1 = (i, j)
            if key_table[i][j] == char2:
                pos2 = (i, j)
    return pos1, pos2

# Function to encrypt a plaintext using the Playfair cipher
def encrypt(plaintext, key):
    key_table = generate_key_table(key)
    plaintext = plaintext.upper().replace("J", "I")  # Convert to uppercase and replace J with I
    plaintext = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]  # Split plaintext into pairs of two characters
    ciphertext = ""
    for pair in plaintext:
        char1, char2 = pair[0], pair[1]
        pos1, pos2 = find_positions(key_table, char1, char2)
        if pos1[0] == pos2[0]:  # If the characters are in the same row
            ciphertext += key_table[pos1[0]][(pos1[1]+1)%5] + key_table[pos2[0]][(pos2[1]+1)%5]  # Shift to the right
        elif pos1[1] == pos2[1]:  # If the characters are in the same column
            ciphertext += key_table[(pos1[0]+1)%5][pos1[1]] + key_table[(pos2[0]+1)%5][pos2[1]]  # Shift downwards
        else:  # If the characters form a rectangle
            ciphertext += key_table[pos1[0]][pos2[1]] + key_table[pos2[0]][pos1[1]]  # Swap columns
    return ciphertext

# Function to decrypt a ciphertext using the Playfair cipher
def decrypt(ciphertext, key):
    key_table = generate_key_table(key)
    ciphertext = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]  # Split ciphertext into pairs of two characters
    plaintext = ""
    for pair in ciphertext:
        char1, char2 = pair[0], pair[1]
        pos1, pos2 = find_positions(key_table, char1, char2)
        if pos1[0] == pos2[0]:  # If the characters are in the same row
            plaintext += key_table[pos1[0]][(pos1[1]-1)%5] + key_table[pos2[0]][(pos2[1]-1)%5]  # Shift to the left
        elif pos1[1] == pos2[1]:  # If the characters are in the same
            plaintext