import socket                   # Import socket module
import os


port = 60000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.
host_ip = socket.gethostbyname(host)


print('[SERVER] Server is listening....')


while True:
    conn, addr = s.accept()  # Establish connection with client.
    print('[SERVER] Got connection from', addr)
    filename = conn.recv(1024).decode()
    conn.send('received filename'.encode())

    path = os.getcwd()
    path = path + f'\\files\\{host}'
    is_exist = os.path.exists(path)
    if not is_exist:
        print("[SERVER][NEW] New user detected!")
        os.makedirs(path)
        print(f'[SERVER][NEW] New directory created /{host}')

    files_in_directory = os.listdir(path)
    if f'{filename}' in files_in_directory:
        conn.send('file already exist in directory... replace-r, copy-c'.encode())
        x = conn.recv(1024).decode()
        if x == 'r':
            os.remove(f'files\\{host}\\{filename}')
        elif x == 'c':
            i = 1
            while True:
                if f'({i}) {filename}' in files_in_directory:
                    i = i + 1
                else:
                    filename = f'({i}) {filename}'
                    break

    else:
        conn.send('ok'.encode())

    with open(f'{path}\\{filename}', 'wb') as f:
        print(f'[SERVER] File "{filename}" has been opened')
        print(f'[SERVER] transferring data...')
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)
        conn.send('ok'.encode())
    print('[SERVER] File has been successfully uploaded')
    current_storage_on_disk = 0
    for file in files_in_directory:
        size_of_file = os.path.getsize(path + f'\\{file}')
        current_storage_on_disk = current_storage_on_disk + size_of_file
    current_storage_on_disk = current_storage_on_disk / 1000000

    print(f'[SERVER][STORAGE] Disk capacity: {round(current_storage_on_disk, 2)}mb of 500mb')
    # conn.send(f'[SERVER][STORAGE] Disk capacity: {round(current_storage_on_disk, 2)}mb of 500mb'.encode())
    conn.close()
    print('[SERVER] Connection closed')
    print('[SERVER] Server is listening....')


