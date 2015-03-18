# Chat room
implement multiple client and non-blocking chat room

## step 1: simply transfer current time once from server to client (done)
* Blocking
* Single client
* Sending data once then close the connection
* Server can only send data and client can only receive data

## step 2: chat socket
* Non-blocking
* Multiple client
* Close connection until no more readable connection
* Server only handle broadcast and connection
> BUG: when another client try to connect to server, the first client will disconnect