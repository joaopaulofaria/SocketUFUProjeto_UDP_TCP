from socket import *

def cifracesar(message):
    mensagem_criptografada = ""

    for char in message:
            mensagem_criptografada += chr(ord(char) + 3)

    return mensagem_criptografada

serverPort = 1216
serverSocket  = socket (AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print ("Servidor rodando e pronto para conexões: ")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    message = message.decode()
    mensagem_criptografada = cifracesar(message)
    serverSocket.sendto(mensagem_criptografada.encode(),clientAddress)

