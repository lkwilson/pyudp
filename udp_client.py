#!/usr/bin/env python3

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

message = b"your very important message"
server.sendto(message, ("192.168.1.255", 12345))
