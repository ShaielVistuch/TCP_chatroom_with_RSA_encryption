import threading
import socket
import time
option=input('Choose an option:\n 1) Connect to a group chat\n 2) Create a new group chat\n 3) Disconnect\n')
n = 851
d = 659
if option == "1":
    alias = input('ENTER YOUR NAME: ')
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.2', 59000))
    identity = input('ENTER THE ID OF THE GROUP YOU WANT TO JOIN: ')
    password = input('ENTER THE PASSWORD: ')
    def client_receive():
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                if message == "alias?":
                    client.send(alias.encode('utf-8'))
                elif message == "enter group chat id:":
                    client.send(identity.encode('utf-8'))
                elif message == "password?":
                    client.send(password.encode('utf-8'))
                elif message == "option?":
                    client.send(option.encode('utf-8'))
                elif message == "disconnect":
                    print('Sorry, we are unable to connect you to the group chat')
                    client.close()
                else:
                    print(message)

            except:
                print('An error happened')
                client.close()
                break


    def client_send():
        while True:
            msg = input("")
            message = f'{alias}: {msg}'
            message_ascii = [ord(letters) for letters in message]
            end_of_messege = 127  # ascii of delete
            message_ascii.append(end_of_messege)
            encrypted_list = []
            for num in message_ascii:
                current_enc = (num ** d) % n
                encrypted_list.append(current_enc)
            for m in encrypted_list:
                time.sleep(0.1)
                client.send(str(m).encode('utf-8'))
                time.sleep(0.1)


    receive_thread = threading.Thread(target=client_receive)
    receive_thread.start()

    send_thread = threading.Thread(target=client_send)
    send_thread.start()

if option == "2":
    alias = input('ENTER YOUR NAME: ')
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.2', 59000))
    password = input('CHOOSE A PASSWORD FOR THE GROUP: ')
    identity='1'

    def client_receive():
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                if message == "alias?":
                    client.send(alias.encode('utf-8'))
                elif message == "password?":
                    client.send(password.encode('utf-8'))
                elif message == "enter group chat id:":
                    client.send(identity.encode('utf-8'))
                elif message == "option?":
                    client.send(option.encode('utf-8'))
                elif message == "disconnect":
                    print('Sorry, we are unable to connect you to the group chat')
                    client.close()
                elif message == "disconnect option":
                    print('Disconnecting . . . Bye!')
                    client.close()
                elif message == "wrong option":
                    print('You entered an invalid option. We are disconnecting you.')
                    client.close()
                    break
                else:
                    print(message)

            except:
                print('An error happened')
                client.close()
                break


    def client_send():
        while True:
            msg = input("")
            message = f'{alias}: {msg}'
            message_ascii = [ord(letters) for letters in message]
            end_of_messege = 127  # ascii of delete
            message_ascii.append(end_of_messege)
            encrypted_list = []
            for num in message_ascii:
                current_enc = (num ** d) % n
                encrypted_list.append(current_enc)
            for m in encrypted_list:
                time.sleep(0.1)
                client.send(str(m).encode('utf-8'))
                time.sleep(0.1)


    receive_thread = threading.Thread(target=client_receive)
    receive_thread.start()

    send_thread = threading.Thread(target=client_send)
    send_thread.start()