import socket
host = '120.124.135.96'
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
    print(f'recv: {indata.decode()}', end='\n\n')