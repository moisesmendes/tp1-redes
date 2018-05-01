from socket import *
import sys

HOST = "127.0.0.1"
PORT = 33121

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
# print ('Connection var: ') + str(conn)
# print ('Connected by addr: ') + str(addr)

maximum_bytes = 4096

while True:
	data = conn.recv(maximum_bytes) # recv using connection
	print (data)
	
	reply = input("Reply: ")
	conn.send(reply.encode())

conn.close()
