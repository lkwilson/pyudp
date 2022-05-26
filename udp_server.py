#!/usr/bin/env python3

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # UDP

# sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind(("192.168.1.255", 12345))
while True:
    data, addr = sock.recvfrom(1024)
    print(f"received message: {data.decode('utf-8')}")
