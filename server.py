#!/usr/bin/python3

"""
	1. If the master socket is readable, the server would accept the new connection.
  2. If any of the client socket is readable, the server would read the message,
     and broadcast it back to all clients except the one who send the message.
"""

import sys
import select
import socket
# from tcpSocket import *

HOPCOUNT = 10;
SOCKET_LIST = [];			# [socket.socket], list of readable connection
RECV_BUFFER = 4096;
HOST = '';
PORT = 9009;

def broadcast(serversocket, sock, msg):
	# print('Broadcasting, msg: ', msg);
	for so in SOCKET_LIST:
		# send msg to peer only
		if so != serversocket and so != sock:
			try: so.send(msg);
			except Exception as e:
				# brocken socket connection
				so.close();
				if so in SOCKET_LIST: SOCKET_LIST.remove(so);

def chat_server():

	# serversocket = tcpSocket();
	# serversocket.bind(HOST, PORT);
	# serversocket.listen(HOPCOUNT);
	# SOCKET_LIST.append(serversocket.sock);	# Mark server socket is readable connection

	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
	print('Socket created.');
	serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);
	serversocket.bind((HOST, PORT));
	print('Chatting server started on port ', PORT);
	serversocket.listen(10);
	print('Socket listen: ', HOPCOUNT, ' hop');
	SOCKET_LIST.append(serversocket)

	while True:
		# Get the list sockets which are ready to be read thruogh select
		# 4th argument, time_out = 0: poll and never block
		ready_to_read, ready_to_write, in_error= select.select(SOCKET_LIST, [], [], 0);

		for sock in ready_to_read:
			# new connection request received
			if sock == serversocket:
				sockfd, address = serversocket.accept();
				SOCKET_LIST.append(sockfd);
				print('Client (%s, %s) connected'% address)
				broadcast(serversocket, sockfd, "[%s:%s] entered our chatting room\n" % address)

			# a message from client, not new connection
			else:
				# discard connection if there no more data
				try:
					data = recv(RECV_BUFFER);
					if data: broadcast(serversocket, sock, "\r["+ str(sock.getpeername())+ '] '+ data)
					else:
						if sock in SOCKET_LIST: SOCKET_LIST.remove(sock);
						broadcast(serversocket, sock, "Client (%s, %s) is offline\n" % address);
				except Exception as e:
					broadcast(serversocket, sock, "Client (%s, %s) is offline\n" % address);
					continue;
	serversocket.close();

if __name__ == '__main__':
	sys.exit(chat_server());