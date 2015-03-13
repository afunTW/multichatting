#!/usr/bin/python3

"""
	1. Blocking(NOW) > Non-blocking
	2. Single thread(NOW) > Multiple thread
"""

import socket;

class tcpSocket:
	"""
		1. Initialize
		2. Connection
	"""

	def __init__(this, sock = None):
		if sock is None: this.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
		else this.sock = sock;

	def connect(this, host, port):
		this.sock.connect((host, port));

	def send(this, msg):
		total = 0;
		while total < MSGLEN:
			sent = this.sock.send(msg[total,]);
			if sent == 0: raise RuntimeError("socket connection broken");
			total += sent;

	def rcv(this):
		segment = [];
		bytes_recd = 0;
		while bytes_recd < MSGLEN:
			chunk = this.sock.recv(min(MSGLEN - bytes_recd, 2048));
			if chunk == b'': raise RuntimeError("socket connection broken");
			segment.append(chunk);
			bytes_recd += len(chunk);
		return b''.join(segment);