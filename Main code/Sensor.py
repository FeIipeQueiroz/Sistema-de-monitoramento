import socket
import time
import random

#Definição das variáveis do socket
ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 5001

#Tentativa de conexão no servidor
print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

#Recebe a mensagem do servidor
Response = ClientSocket.recv(1024)

#Define as variáveis de forma aleatória
TC = str(random.randint(36, 39))
FR = str(random.randint(9, 29))
OS = str(random.randint(90, 100))
PA = str(random.randint(71, 100))
FC = str(random.randint(51, 129))
    
#Opção para definir se o programa irá enviar dados automaticamente ou manualmente    
print("Deseja inserir os valores manualmente?")
x = input("(1) Sim e (2) Não ")
x = int(x)

#Loop principal do sensor
while True:

    #Passsa os valores para a variavel que será convertida em string e enviada ao servidor
    Var = TC+','+FR+','+OS+','+PA+','+FC
    ClientSocket.send(str.encode(Var))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))

    time.sleep(10)

    #Condição de conferência para o input dos dados
    if (x == 1):
        TC = input('Insira o valor da Temperatura corporal: ')
        FR = input('Insira o valor da Frequência respiratória: ')
        OS = input('Insira o valor da Oxigenação do sangue: ')
        PA = input('Insira o valor da Pressão arterial: ')
        FC = input('Insira o valor da Frequência cardíaca: ')
    else:
        TC = str(random.randint(36, 39))
        FR = str(random.randint(9, 29))
        OS = str(random.randint(90, 100))
        PA = str(random.randint(71, 100))
        FC = str(random.randint(51, 129))
        
ClientSocket.close()