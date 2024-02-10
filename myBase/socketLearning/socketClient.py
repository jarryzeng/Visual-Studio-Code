import socket

host = input("input ip: ")
port = input("input port: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)
s.connect((host, int(port)))

s.send(b'request command')
print(s.recv(1024).decode())

while True:
    try:
        outdata = input('\ninput: ')
        s.send(outdata.encode())

        indata = s.recv(1024)
        if len(indata) == 0:
            s.close()
            print('server closed connection')
            break
        print(indata.decode())
    except TimeoutError as timeout:
        print('time out')
        print('please input again')
