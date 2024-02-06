# TCP_chatroom_with_RSA_encryption
For extra safety, I decided to expand further the project and add encryption. Messages are now encoded using RSA encryption. Clients use only the public key, while server has the private key.
Clients can:
1) Open a new group chat protected by a a password and group ID
2) Connect to an already opened group chat
3) Disconnect from the server
