import socket
host = '120.124.135.96'
port = 200

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(5)

isServerStart = True

print(f'server start at {host}:{port}')
print('wait for connection...')

while isServerStart:
    conn, addr = s.accept()
    conn.send(b'server is connect')
    print(f'connected by {str(addr)}')
    while True:
        indata = conn.recv(1024)
        command = indata.decode()
        
        if command == 'stop':
            print('client closed connection.')
            isServerStart = False
            conn.send(b'server is closed')
            conn.close()
            break

        elif command == 'open the computer':
            print(f'recv: {command}')
            outdata = 'computer is opened'
            conn.send(outdata.encode())
            
        elif command == 'disconnect':
            print(f'recv: {command}')
            conn.send(b'server is disconnect')
            conn.close()
            break

        else:
            print('unknow command')
s.close()