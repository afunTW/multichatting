#!/usr/bin/python3

import sys
import select
import socket
# from tcpSocket import *

RECV_BUFFER = 4096

def chat_client():
	if len(sys.argv) < 3:
		print('usage: server.py, hostname, port')
		sys.exit();

	HOST = sys.argv[2];
	PORT = int(sys.argv[3]);

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
	s.settimeout(2);

	try: s.connect((HOST, PORT));
	except: print('Unable to connect');	sys.exit();

	print('Connected to remote host. You can start sending messages.');
	sys.stdout.write('[Me] '); sys.stdout.flush();

	while True:
		socketlist = [sys.stdin, s];

		# Get the list of sockets which are reachable
		ready_to_read, ready_to_write, in_error = select.select(socketlist, [], []);

		for sock in ready_to_read:
			if sock == s:
				# incoming data from remote server
				data = sock.recv(RECV_BUFFER).decode('utf-8');
				if not data: print('\nDisconnect from chat server'); sys.exit();
				else:
					#print data
					sys.stdout.write(str(data));
					sys.stdout.flush();
					print()

			else:
				# user enter the msg
				msg = sys.stdin.readline();
				s.send(bytes(msg, 'utf-8'));
				sys.stdout.flush();

if __name__ == '__main__':
	sys.exit(chat_client());