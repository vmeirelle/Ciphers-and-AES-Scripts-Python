def caesar_cipher(message, key, alphabet):
    encrypted_message = ""
    for char in message:
        if char in alphabet:
            char_index = alphabet.index(char)
            encrypted_index = (char_index + key) % len(alphabet)
            encrypted_message += alphabet[encrypted_index]
        else:
            encrypted_message += char
    return encrypted_message


def caesar_decipher(message, key, alphabet):
    key = -key
    decrypted_message = caesar_cipher(message, key, alphabet)
    return decrypted_message


alfabeto = ' abcdefghijklmnopqrstuvwxyz'
for i in range (26):
    print(caesar_decipher("cgrzm namfrzmnemzn unem namr fdnm namerzmnmv efdgpnamqrmgzmbdasveeva ny",i, alfabeto), '  Chave', i)