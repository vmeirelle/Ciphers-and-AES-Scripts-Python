import numpy as np
from math import gcd

def encrypt(plaintext, key):
    # Converte o texto em uma matriz de números
    text_nums = [ord(c) - ord('a') for c in plaintext.lower() if c.isalpha()]
    while len(text_nums) % 2 != 0:
        text_nums.append(0)
    text_matrix = np.array(text_nums).reshape((-1, 2))
    # Calcula o determinante da chave e verifica se é invertível
    det = int(round(np.linalg.det(key)))
    if gcd(det, 26) != 1:
        raise ValueError("A chave não é invertível")
    # Criptografa a matriz de texto usando a chave
    ciphertext_matrix = np.dot(key, text_matrix.T).T % 26
    # Converte a matriz criptografada em uma string
    ciphertext = "".join([chr(c + ord('a')) for c in ciphertext_matrix.flatten()])
    return ciphertext

def decrypt(ciphertext, key):
    # Converte o texto criptografado em uma matriz de números
    text_nums = [ord(c) - ord('a') for c in ciphertext.lower() if c.isalpha()]
    text_matrix = np.array(text_nums).reshape((-1, 2))
    # Calcula o inverso multiplicativo do determinante da chave
    det_inv = pow(int(round(np.linalg.det(key))), -1, 26)
    if det_inv is None:
        raise ValueError("A chave não é invertível")
    # Calcula a matriz inversa da chave
    key_inv = np.array([[key[1,1], -key[0,1]], [-key[1,0], key[0,0]]]) * det_inv % 26
    # Descriptografa a matriz de texto usando a chave inversa
    plaintext_matrix = np.dot(key_inv, text_matrix.T).T % 26
    # Converte a matriz descriptografada em uma string
    plaintext = "".join([chr(c + ord('a')) for c in plaintext_matrix.flatten()])
    return plaintext

key = np.array([[7, 8], [11, 11]])
plaintext = "short example"
ciphertext = encrypt(plaintext, key)
print(ciphertext)
decrypted_plaintext = decrypt(ciphertext, key)
print(decrypted_plaintext) 
