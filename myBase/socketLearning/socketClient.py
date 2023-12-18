import socket

host = input('input the ip:')
while len(host.split('.')) != 4: host = input('host ip is not set 4 of number like 192.168.1.1 \ninput the ip:')
port = int(input('input the port:'))
while port < 0 or port > 65535: port = input('port is not a allow value \nthe value had need to between 0 to 65535 \ninput the port:')

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
