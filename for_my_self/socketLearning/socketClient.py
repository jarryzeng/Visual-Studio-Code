import socket
host = '10.147.20.138'
port = 7

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)
s.connect((host, port))

print('method:')
print('1.stop - disconnect to the bridge')
print('2.bridge stop - turn off the bridge')
print('3.bridge reboot - reboot birdge')
print('4.server connect - connect to server')
print('5.server disconnect - disconnect to server')
print('6.server stop - turn off the server')
print('7.server start - open tye server')
print('every request most waiting for 10 second')

while True:
    try:
        outdata = input('\ninput command:')
        s.send(outdata.encode())

        indata = s.recv(1024)
        if len(indata) == 0:
            s.close()
            print('server closed connection')
            break
        print(f'recv: {indata.decode()}')
    except TimeoutError as timeout:
        print('time out')
        print('please input again')
