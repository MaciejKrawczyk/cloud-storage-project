import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.

input("click any button to connect to the server...")


s.connect((host, port))

filename = 'BlenderGIS-master.zip'
s.send(filename.encode())
check = s.recv(1024)
print(check.decode())

x = s.recv(1024)
x = x.decode()
if x == 'file already exist in directory... replace-r, copy-c':
   y = input('file already exist in directory... replace-r, copy-c')
   s.send(y.encode())

f = open(filename, 'rb')
l = f.read(1024)
while l:
   s.send(l)
   # print(l)
   # print('Sent ', repr(l))
   l = f.read(1024)
f.close()
# s.recv(1024).decode()

print(f'File {filename} has been uploaded successfully')
# p = s.recv(1024).decode()
# print(p)
s.close()

# https://www.bogotobogo.com/python/python_network_programming_server_client_file_transfer.php
