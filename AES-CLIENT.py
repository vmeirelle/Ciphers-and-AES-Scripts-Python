import socket
import os
from Crypto.Cipher import AES

# Define key and initialization vector
key = b'sixteen byte key'
iv = b'InitializationVe'

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()

# Reserve a port for your service.
port = 12345

# Connect to the server
client_socket.connect((host, port))

# Get the message to be encrypted from the user
message = input("Enter the message: ").encode()

# Encrypt the message using AES algorithm
cipher = AES.new(key, AES.MODE_CFB, iv)
encrypted_message = cipher.encrypt(message)

# Send the encrypted message to the server
client_socket.send(encrypted_message)

# Close the connection
client_socket.close()
