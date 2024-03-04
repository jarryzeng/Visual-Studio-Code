import socket
import time

ip = input("input ip: ")
port = int(input("input port: "))

while True:
  time.sleep(5)
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.connect((ip, port))
  server.send(str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())).encode())
