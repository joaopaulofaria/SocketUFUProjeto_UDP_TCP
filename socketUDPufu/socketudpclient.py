from socket import *

serverName = '10.0.99.150'
serverPort = 4443

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input("Digite sua senha para criptografia: ")

clientSocket.sendto(message.encode(), (serverName, serverPort))
mensagem_criptografada, serverAddress = clientSocket.recvfrom(2048)

print(mensagem_criptografada.decode())

clientSocket.close()

