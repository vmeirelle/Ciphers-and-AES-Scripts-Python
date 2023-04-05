import socket
import os
from Crypto.Cipher import AES

# Define key and initialization vector
key = b'sixteen byte key'
iv = b'InitializationVe'

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()

# Reserve a port for your service.
port = 12345

# Bind the socket to a public host, and a well-known port
server_socket.bind((host, port))

# Listen to incoming connections
server_socket.listen(1)

# Accept incoming connections
conn, addr = server_socket.accept()
print('Connected by', addr)

# Receive the encrypted message from client
data = conn.recv(1024)
cipher = AES.new(key, AES.MODE_CFB, iv)
decrypted_data = cipher.decrypt(data)

print("Encrypted data: ", data)
print("Decrypted data: ", decrypted_data)

# Close the connection
conn.close()
