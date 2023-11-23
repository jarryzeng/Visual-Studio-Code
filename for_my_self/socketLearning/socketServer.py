import socket
host = '192.168.1.104'
port = 200

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(5)

print('server start at %s:%s' % (host, port))
print('wait for connection...')

while True:
    conn, addr = s.accept()
    print('connected by' + str(addr))
    while True:
        indata = conn.recv(1024)
        command = indata.decode()
        
        if len(indata) == 0 or command == 'stop':
            print('client closed connection.')
            conn.send('server is closed'.encode())
            conn.close()
            break

        if command == 'open the computer':
            print('recv: ' + command)
            outdata = 'computer is opened'
            conn.send(outdata.encode())
            
        else:
            print('unknow command')
s.close()