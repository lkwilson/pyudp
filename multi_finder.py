import socket
import struct

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007
bind_addr = '192.168.1.11'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_IP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
sock.bind((MCAST_GRP, MCAST_PORT))
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
  print(sock.recv(10240).decode('utf-8'))
