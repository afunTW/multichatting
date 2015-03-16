# simpleRTP
implement reliable transprot protocol in python3

## step 1: simply transfer current time once from server to client (done)
* Blocking
* Single client
* Sending data once then close the connection
* Server can only send data and client can only receive data

## step 2: chat socket
* Non-blocking
* Multiple client
* Close connection until no more readable connection
* Both server and client can send/ receive data