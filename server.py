from socket import *
import sys
#entrada: ./dcc023c2 -c <IP>:<PORT> <INPUT> <OUTPUT>


HOST = sys.argv[2]
PORT = int(sys.argv[3])

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
