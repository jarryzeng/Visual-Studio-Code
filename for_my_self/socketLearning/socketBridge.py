import socket
host = '0.0.0.0'
port = 7

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(5)

isBridgeOpen = True
isServerStart = False

print(f'server start at {host}:{port}')
print('wait for connection...')

while isBridgeOpen:
    conn, addr = s.accept()
    print(f'connected by {str(addr)}')
    while True:
        indata = conn.recv(1024)
        command = indata.decode()

        if command == 'stop':
            print('command: stop')
            conn.send(b'')
            conn.close()
            print('client closed connection.')
            break

        elif command == 'bridge stop':
            print('command: bridge stop')
            isBridgeOpen = False
            conn.send(b'')
            conn.close()
            print('client closed connection.')
            break

        elif command == 'start':
            if isServerStart:
                print('command: start')
                req.send(b'open the computer')
                res = req.recv(1024)
                conn.send(res)
            else:
                conn.send(b'server did not start')
                print('server did not start')

        elif command == 'server connect':
            print('command: server connect')
            if not isServerStart:
                isServerStart = True
                reqIp = '120.124.135.96'
                reqPort = 200
                try:
                    req = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    req.connect((reqIp, reqPort))
                    res = req.recv(1024)
                    conn.send(res)
                except Exception as exc:
                    conn.send(str(exc).encode())
                    print(exc)
            else:
                conn.send(b'server is already connected')
                print('server is already connected')

        elif command == 'server disconnect':
            print('command: server disconnect')
            if isServerStart:
                isServerStart = False
                req.send(b'disconnect')
                res = req.recv(1024)
                req.close()
                conn.send(res)
                print(res.decode())
            else:
                conn.send(b'server did not connect')
                print('server did not connect')

        elif command == 'server stop':
            print('command: server stop')
            if isServerStart:
                isServerStart = False
                req.send(b'stop')
                res = req.recv(1024)
                req.close()
                conn.send(res)
                print(res.decode())
            else:
                conn.send(b'server did not start')
                print('server did not start')

        else:
            conn.send(b'unknow command')
            print(f'unknow command: {command}')
s.close()
