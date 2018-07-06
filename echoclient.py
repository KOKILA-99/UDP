import socket
UDP_IP_ADDRESS = "10.1.24.119"
UDP_PORT_NO  = 6723
Message=("Hello server")
bytestosend= str.encode(Message)
clientSock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
clientSock.sendto(bytestosend,(UDP_IP_ADDRESS,UDP_PORT_NO))
msgfromserver= clientSock.recvfrom(1024)
print(msgfromserver)
