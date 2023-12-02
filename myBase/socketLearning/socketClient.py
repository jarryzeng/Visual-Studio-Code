import socket

host = input('input the destination ip:')
port = input('input the connect port:')

host = input('input the ip:')
while len(host.split('.')) != 4: host = input('host ip is not set 4 of number like 192.168.1.1 \ninput the ip:')
port = int(input('input the port:'))
while port < 0 or port > 65535: port = input('port is not a allow value \nthe value had need to between 0 to 65535 \ninput the port:')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)
s.connect((host, int(port)))

print('method:')
print('1.stop - disconnect to the bridge')
print('2.bridge stop - turn off the bridge')
print('3.bridge reboot - reboot birdge')
print('4.server connect - connect to server')
print('5.server disconnect - disconnect to server')
print('6.server stop - turn off the server')
print('7.server start - open tye server')
print('8.server send {command} - send command to server')
print('every request most waiting for 10 second')

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
