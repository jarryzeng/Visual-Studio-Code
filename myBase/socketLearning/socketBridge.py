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

def disconnect(conn, server, command):
    server.send(b'disconnect')
    res = server.recv(1024)
    server.close()
    if command[7:] == 'disconnect':conn.send(res)
    print(res.decode())
    return False

def stop(conn, server):
    server.send(b'stop')
    res = server.recv(1024)
    server.close()
    conn.send(res)
    print(res.decode())
    return False

def send(conn, server, requset):
    print(f'send to sever: {requset}')
    try:
        server.send(f'request {requset}'.encode())
        res = server.recv(1024)
        conn.send(res)
        print(f'server response: {res.decode()}')
    except Exception as timeout:
        conn.send(str(timeout).encode())
        print(timeout)

def send2Client(conn, message):
    conn.send(message.encode())
    print(message)

host = input('input the ip:')
while len(host.split('.')) != 4: host = input('host ip is not set 4 of number like 192.168.1.1 \ninput the ip:')
port = int(input('input the port:'))
while port < 0 or port > 65535: port = input('port is not a allow value \nthe value had need to between 0 to 65535 \ninput the port:')

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
        command = command.lower()
        print(f'command: {command}')
        if command == 'stop' or command == 'bridge stop' or command == 'bridge reboot' or command == '':
            if isServerStart: isServerStart = disconnect(conn, server, command)
            if command != 'stop' and command != '': isBridgeOpen = False
            if command == 'bridge reboot': wantReboot = True
            conn.send(b'')
            conn.close()
            print(f'client {str(addr)} closed connection.')
            break
        
        elif command[:6] == 'server':
            if command[7:] == 'start': start(conn, isServerStart)
            elif isServerStart:
                if command[7:] == 'connect': send2Client(conn, 'server is already connected')
                elif command[7:11] == 'send': send(conn, server, command[12:])
                elif command[7:] == 'stop': isServerStart = stop(conn, server)
                elif command[7:] == 'disconnect': isServerStart = disconnect(conn, server, command)
                else: send2Client(conn, 'unknow command')
            else:
                if command[7:] == 'connect': isServerStart, server = connect(conn)
                elif command[7:] == 'disconnect' or command[7:11] == 'send' or command[7:] == 'stop': send2Client(conn, 'server did not connect')
                else: send2Client(conn, 'unknow command')

        else:
            conn.send(b'unknow command')
            print('unknow command')

s.close()
if wantReboot: os.system('bash rebootServer.sh')