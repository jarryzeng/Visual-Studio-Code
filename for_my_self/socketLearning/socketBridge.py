import socket
host = '0.0.0.0'
port = 7

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(5)

isBridgeOpen = True
isServerStart = False

print('server start at %s:%s' % (host, port))
print('wait for connection...')

while isBridgeOpen:
    conn, addr = s.accept()
    print('connected by' + str(addr))
    while True:
        indata = conn.recv(1024)
        command = indata.decode()

        if command == 'stop':
            print('command: stop')
            conn.close()
            print('client closed connection.')
            break

        elif command == 'bridge stop':
            print('command: bridge stop')
            isBridgeOpen = False
            conn.close()
            print('client closed connection.')
            break

        elif command == 'start':
            if isServerStart:
                print('command: start')
                req.send('open the computer'.encode())
                res = req.recv(1024)
                conn.send(res)
            else:
                conn.send('server did not start'.encode())
                print('server did not start')

        elif command == 'server start':
            print('command: server start')
            if not isServerStart:
                isServerStart = True
                reqIp = '192.168.1.104'
                reqPort = 200
                req = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                req.connect((reqIp, reqPort))
                conn.send('server is start'.encode())
            else:
                conn.send('server is already start'.encode())
                print('server is already start')

        elif command == 'server stop':
            print('command: server stop')
            if isServerStart:
                isServerStart = False
                req.send('stop'.encode())
                req.close()
                conn.send('server is stop'.encode())
            else:
                conn.send('server did not start'.encode())
                print('server did not start')

        else:
            conn.send('unknow command'.encode())
            print('unknow command: ' + command)
s.close()