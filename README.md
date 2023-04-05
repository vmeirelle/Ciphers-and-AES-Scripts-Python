# Cipher Implementations in Python

## Ciphers

Implementations of three classical ciphers: the Caesar cipher, the Hill cipher, and the Vigenere cipher.

* CESAR Cipher: The Caesar cipher is a simple substitution cipher where each letter in the plaintext is shifted a certain number of positions down the alphabet. For example, with a shift of 3, A would be replaced by D, B would become E, and so on.

* HILL Cipher: The Hill cipher is a polygraphic substitution cipher that operates on blocks of letters. It uses matrix multiplication to encrypt and decrypt messages. The size of the matrix used determines the length of the block of letters being encrypted.

* VIGENERE Cipher: The Vigenere cipher is a polyalphabetic substitution cipher that uses a keyword to encrypt messages. Each letter of the keyword is used to shift the corresponding letter of the plaintext by a certain amount. The keyword is repeated as many times as necessary to cover the entire length of the plaintext. This makes it more difficult to break than simple substitution ciphers like the Caesar cipher.

## AES Client-Server

AES (Advanced Encryption Standard): AES is a symmetric block cipher used to encrypt electronic data. It is widely used to secure sensitive data, such as financial transactions, and is considered to be one of the most secure encryption algorithms available today. It operates on blocks of 128 bits and uses a key length of 128, 192, or 256 bits.

Python Client-Server Implementation of AES: There are several libraries available in Python for implementing AES, including the PyCrypto and cryptography libraries, in this case we are using Crypto.Cipher. This client-server implementation of AES involve a client sending plaintext to a server, which encrypts the plaintext using AES and sends the encrypted ciphertext back to the client. The client can then decrypt the ciphertext using the same AES key that was used by the server. This type of implementation can be useful for secure communication between two parties, such as a client and a server exchanging sensitive information.
