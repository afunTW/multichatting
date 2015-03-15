#!/usr/bin/python3

import time
import socket
#from tcpSocket import *

if __name__ == '__main__':
	"""
		As a server
		1. create socket(init)
		2. bind adddress
		3. listen on port
		4. send/ recv message
		5. shutdown
		6. close
	"""
	hopCount = 5;

	# get local machine host and port
	host = socket.gethostname();
	port = 9999;

	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
	print('Socket create.');
	serversocket.bind((host, port));
	print('Socket binding');
	serversocket.listen(hopCount);
	print('Socket listen: ', hopCount, ' hop')

	while True:
		clientsocket, address = serversocket.accept();
		print('Got a connection from ', str(address));

		currentTime = time.ctime(time.time()) + "\r\n";
		clientsocket.send(currentTime.encode('ascii'));
		clientsocket.close();
		print('Socket close');
		break;

	# serversocket = tcpSocket();
	# serversocket.bind(host, port);
	# serversocket.listen(5);

	# clientsocket, address = serversocket.sock.accept();	# return pair value (connection, addr)
	# print('Got a connection from %s', str(address))

	# while True:
	# 	currentTime = time.ctime(time.time()) + "\r\n";
	# 	clientsocket.mysend(currentTime.encode('ascii'));

	# 	time.sleep(1);	# Sleep 1 sec.