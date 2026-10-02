from socket import *

def cifracesardescripto(sentence):
    mensagem_descripto = ''
    for char in sentence:
        mensagem_descripto += chr(ord(char) - 3)

    return mensagem_descripto

serverPort = 1216

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

print ('Servidor recebendo conexões')

while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    mensagem_descripto = cifracesardescripto(sentence)
    connectionSocket.send(mensagem_descripto.encode())
    connectionSocket.close()