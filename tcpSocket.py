#!/usr/bin/python3

import socket;

class tcpSocket:

	def __init__(self, sock = None):
		"""
			Create socket: AF_INET(IPv4); SOCK_STREAM(TCP);

			Set socket option:
				SO_REUSEADDR-
					Allows socket to bind to an address and port already in use.
					Also, if two sockets are bound to the same port the behavior is undefined
					as to which port will receive packets.
		"""
		if sock is None: self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
		else: self.sock = sock;
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);
		print('Socket created.');

	def bind(self, host, port):
		self.sock.bind((host, port));
		print('Socket binding');
		print('Chatting server started on port ', port);

	def listen(self, hopCount):
		self.sock.listen(hopCount);
		print('Socket listen: ', hopCount, ' hop')

	def connect(self, host, port):
		self.sock.connect((host, port));
		print('Socket connected.');