import socket
import os
host = '0.0.0.0'
port = 7

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(5)

isBridgeOpen = True
isServerStart = False
wantReboot = False

print(f'server start at {host}:{port}')
print('wait for connection...')

while isBridgeOpen:
    conn, addr = s.accept()
    print(f'connected by {str(addr)}')
    while True:
        indata = conn.recv(1024)
        command = indata.decode()

        if command == 'stop' or command == 'bridge stop' or command == 'bridge reboot':
            print(f'command: {command}')
            if command != 'stop': isBridgeOpen = False
            if command == 'bridge reboot': wantReboot = True
            conn.send(b'')
            conn.close()
            print('client closed connection.')
            break

        elif command == 'server start':
            if isServerStart:
                print('command: server start')
                req.send(b'open the computer')
                res = req.recv(1024)
                conn.send(res)
            else:
                conn.send(b'input the server mac')
                parame = conn.recv(1024)
                os.system(f'python wakeOnLan.py {parame}')
                conn.send(b'try to opening the server input command later')
                print('opening the server')

        elif command == 'server connect':
            print('command: server connect')
            if not isServerStart:
                isServerStart = True
                conn.send(b'input destination server ip')
                reqIp = conn.recv(1024).decode()
                conn.send(b'input target port')
                reqPort = conn.recv(1024).decode()
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

if wantReboot: os.system('bash rebootServer.sh')