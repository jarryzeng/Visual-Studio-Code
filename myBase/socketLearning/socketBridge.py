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
        parame = conn.recv(1024).decode()
        systemRes = os.popen(f'python wakeOnLan.py {parame}').read()
        print(f"system response:\n")
        print(systemRes)
        conn.send(systemRes.encode())

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
    if command[1] == 'disconnect':conn.send(res)
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
        command = indata.decode().lower().split()
        if command[0] == 'stop' or command[0] == 'bridge' or command[0] == '':
            if isServerStart: isServerStart = disconnect(conn, server, command)
            if command[0] != 'stop' and command[0] != '': isBridgeOpen = False
            if command[1] == 'reboot': wantReboot = True
            conn.send(b'')
            conn.close()
            print(f'client {str(addr)} closed connection.')
            break
        
        elif command[0] == 'server':
            if command[1] == 'start': start(conn, isServerStart)
            elif isServerStart:
                if command[1] == 'connect': send2Client(conn, 'server is already connected')
                elif command[1] == 'send': send(conn, server, command[2])
                elif command[1] == 'stop': isServerStart = stop(conn, server)
                elif command[1] == 'disconnect': isServerStart = disconnect(conn, server, command)
                else: send2Client(conn, 'unknow command')
            else:
                if command[1] == 'connect': isServerStart, server = connect(conn)
                elif command[1] == 'disconnect' or command[1] == 'send' or command[1] == 'stop': send2Client(conn, 'server did not connect')
                else: send2Client(conn, 'unknow command')

        else:
            conn.send(b'unknow command')
            print('unknow command')

s.close()
if wantReboot: os.system('bash rebootServer.sh')