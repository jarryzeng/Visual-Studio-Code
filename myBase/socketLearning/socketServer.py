import socket

host = input('input the public ip:')
port = input('input the monitor port:')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, int(port)))
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
            
        elif command == 'disconnect':
            print(f'client {str(addr)} {command}')
            conn.send(b'server is disconnect')
            conn.close()
            break

        elif command[:7] == 'request':
            print(f'recv: {command[8:]}')
            conn.send(f'{command[8:]}'.encode())

        else:
            print(command[:7])
            conn.send(b'unknow command')
            print('unknow command')
s.close()