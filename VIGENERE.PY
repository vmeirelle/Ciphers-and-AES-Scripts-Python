def encrypt_vigenere(plaintext, key):
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].lower()) - ord('a')
            if char.isupper():
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            key_index += 1
        else:
            ciphertext += char
    return ciphertext


def decrypt_vigenere(ciphertext, key):
    plaintext = ""
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].lower()) - ord('a')
            if char.isupper():
                plaintext += chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            else:
                plaintext += chr((ord(char) - ord('a') - shift + 26) % 26 + ord('a'))
            key_index += 1
        else:
            plaintext += char
    return plaintext

plaintext = "shortexample"
key = "keywords"

# Encrypt the plaintext
ciphertext = encrypt_vigenere(plaintext, key)
print("Ciphertext:", ciphertext)

# Decrypt the ciphertext
decrypted_plaintext = decrypt_vigenere(ciphertext, key)
print("Decrypted plaintext:", decrypted_plaintext)
