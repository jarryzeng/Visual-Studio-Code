import socket
import os

def start(conn, isServerStart):
    if isServerStart:
        print('server is opening')
        server.send(b'open the computer')
        res = server.recv(1024)
        conn.send(res)
    else:
        print('opening the server')
        conn.send(b'input the server mac')
        parame = conn.recv(1024)
        os.system(f'python wakeOnLan.py {parame}')
        conn.send(b'trying to opening the server')

def connect(conn):
    conn.send(b'input the destination server ip')
    serverIp = conn.recv(1024).decode()
    print(f'destination server ip {serverIp}')
    conn.send(b'input connect port')
    serverPort = conn.recv(1024).decode()
    print(f'destination server port {serverPort}')
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.settimeout(10)
        server.connect((serverIp, int(serverPort)))
        res = server.recv(1024)
        conn.send(res)
        return True, server
    except Exception as exc:
        conn.send(str(exc).encode())
        print(exc)

    return False, None

def disconnect(conn, server):
    server.send(b'disconnect')
    res = server.recv(1024)
    server.close()
    conn.send(res)
    print(res.decode())

def stop(conn, server):
    server.send(b'stop')
    res = server.recv(1024)
    server.close()
    conn.send(res)
    print(res.decode())

def send(conn, server, requset):
    print(f'send to sever: {requset}')
    try:
        server.send(f'requset {requset}'.encode())
        res = server.recv(1024)
        conn.send(res)
        print(f'server: {res.decode()}')
    except Exception as timeout:
        conn.send(str(timeout).encode())
        print(timeout)

def send2Client(conn, message):
    conn.send(message.encode())
    print(message)

host = input('input the public ip:')
port = input('input the monitor port:')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, int(port)))
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
        print(f'command: {command}')
        if command == 'stop' or command == 'bridge stop' or command == 'bridge reboot' or len(indata) == 0:
            if command != 'stop' and command != '': isBridgeOpen = False
            if command == 'bridge reboot': wantReboot = True
            conn.send(b'')
            conn.close()
            print(f'client {str(addr)} closed connection.')
            break
        
        elif 'server ' in command:
            '''
            if isServerStart:
                if 'start' in command: start(conn, isServerStart)
                elif 'stop' in command: stop(conn, server)
                elif 'disconnect' in command: disconnect(conn, server)
                elif 'connect' in command: send2Client(conn, 'server is already connected')
                elif 'send' in command:
                    requset = command[12:]
                    isServerStart = send(conn, server, requset)
                else: send2Client('unknow command')
            else:
                if 'start' in command: start(conn, isServerStart)
                elif 'connect' in command: isServerStart, server = connect(conn)
                elif 'disconnect' in command or 'stop' in command or 'send' in command: send2Client('server did not connect')
                else: send2Client('unknow command')

            '''
            if 'start\n' in command:
                start(conn, isServerStart)

            elif 'connect\n' in command:
                if not isServerStart:
                    isServerStart, server = connect(conn)
                else:
                    conn.send(b'server is already connected')
                    print('server is already connected')

            elif 'disconnect\n' in command:
                if isServerStart: 
                    isServerStart = False
                    disconnect(conn, server)
                else:
                    conn.send(b'server did not connect')
                    print('server did not connect')

            elif 'stop\n' in command:
                if isServerStart: 
                    isServerStart = False
                    stop(conn, server)
                else:
                    conn.send(b'server did not connect')
                    print('server did not connect')

            elif 'send ' in command:
                if isServerStart:
                    requset = command[12:]
                    send(conn, server, requset)
                else:
                    conn.send(b'server did not connect')
                    print('server did not connect')

        else:
            conn.send(b'unknow command')
            print('unknow command')
s.close()

if server != None: server.send(b'')

if wantReboot: os.system('bash rebootServer.sh')