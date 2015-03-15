#!/usr/bin/python3

import socket
import time
#from tcpSocket import *

if __name__ == '__main__':
	"""
		As a client
		1. create socket(init)
		2. bind adddress
		3. connect to server
		4. send/ recv message
		5. shutdown
		6. close
	"""
	# get local machine host and port
	host = socket.gethostname();
	port = 9999;

	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
	print('Socket create.');
	serversocket.connect((host, port));
	print('Socket connect to host: ',host, ' port: ', port);

	# serversocket = tcpSocket();
	# serversocket.connect(host, port);

	tm = serversocket.recv(2048); # receive no more than 2048 bytes
	print('The time got from the server is %s', tm.decode('ascii'));

	serversocket.close();
	print('Socket close');