import socket
host = '192.168.1.104'
port = 7

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    outdata = input('please input message:')
    s.send(outdata.encode())

    indata = s.recv(1024)
    if len(indata) == 0:
        s.close()
        print('server closed connection')
        break
    print('recv: ' +  indata.decode())