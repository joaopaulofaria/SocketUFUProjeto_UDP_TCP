from socket import *

serverName = '10.0.99.150'
serverPort = 1216

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

sentence = input ("Digite a mensagem a ser descriptografada: ")

clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print("Mensagem: ", modifiedSentence.decode())

clientSocket.close()
