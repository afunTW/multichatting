#!/usr/bin/python3

"""
	1. Blocking(NOW) > Non-blocking
	2. Single thread(NOW) > Multiple thread
"""

import socket;

class tcpSocket:
	"""
		1. Initialize: Client sockets are normally only used for one exchange.
		2. Connection
	"""

	MSGLEN = 2048;

	def __init__(self, sock = None):
		if sock is None: self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
		else: self.sock = sock;
		print('Socket created.');

	def bind(self, host, port):
		self.sock.bind((host, port));
		print('Socket binding');

	def listen(self, hopCount):
		self.sock.listen(hopCount);
		print('Socket listen: ', hopCount, ' hop')

	def connect(self, host, port):
		self.sock.connect((host, port));
		print('Socket connected.');

	def accept(self):	# return pair value (connection, addr)
		self.sock.accept();
		print('Socket accept');
		print(self.sock.accept())

	def mysend(self, msg):
		total = 0;
		while total < MSGLEN:
			sent = self.sock.send(msg[total,]);
			if sent == 0: raise RuntimeError("socket connection broken");
			total += sent;
		print('Socket end of sending.');

	def myrecv(self): #if recv return 0 bytes, it means the connection is closed
		segment = [];
		bytes_recd = 0;
		while bytes_recd < MSGLEN:
			chunk = self.sock.recv(min(MSGLEN - bytes_recd, MSGLEN));
			if chunk == b'': raise RuntimeError("socket connection broken");
			segment.append(chunk);
			bytes_recd += len(chunk);
		print('Socket end of receiving');
		return b''.join(segment);