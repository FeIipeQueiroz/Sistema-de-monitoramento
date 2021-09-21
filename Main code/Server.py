import socket
import os
import string
from time import sleep
from _thread import *
from threading import Thread

#Definição das variáveis do socket
ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Host = 'localhost'
Port = 5001 

#Inicia o servidor
ServerSocket.bind((Host, Port))

print('Waiting for a Connection..')
ServerSocket.listen(5) 

Patients = []

#Definição da classe de paciente utilizada
class Patient:
    def __init__(self, id, name, TC, FR, OS, PA, FC):
        self.id = id
        self.name = name
        self.TC = TC
        self.FR = FR
        self.OS = OS
        self.PA = PA
        self.FC = FC
        self.i = 0
        self.state = False

    #Método que retorna as informações do paciente
    def check_info(self):
        return self.TC, self.FR, self.OS, self.PA, self.FC , self.status

    #Método que atualiza a informação do paciente
    def set_info(self, TC, FR, OS, PA, FC):
        self.TC = TC
        self.FR = FR
        self.OS = OS
        self.PA = PA
        self.FC = FC

    #Método que define a gravidade do paciente
    def check_status(self):
        i = 0
        if int(self.TC) > 38:
            i += 1
        if int(self.FR) > 15:
            i += 1
        if int(self.OS) < 92:
            i += 3
        if int(self.PA) < 100:
            i += 1
        if int(self.FC) > 100:
            i += 1
        if i >= 3:
            print(i)
            self.i = i
            self.state = True
            return i
        else:
            print(i)
            self.i = i
            self.state = False
            return i

    #Método de formatação de retorno dos dados do paciente
    def __repr__(self):
        ret = str(self.name) + str(self.TC) + str(self.FR) + str(self.OS) + str(self.FC) + str(self.state) + self.i + self.id
        return ret

#Método de recebimento de dados e retorno ao 
def Data_reciver(connection, i):
    connection.send(str.encode('Welcome to the Server'))
    patient = Patient(i, "Paciente " + str(i+1), 0, 0, 0, 0, 0)
    Patients.append(patient)
    while True:
        data = connection.recv(2048)
        tc,fr,os,pa,fc = data.decode('utf-8').split(",")
        patient.set_info(tc,fr,os,pa,fc)
        patient.check_status()
        print("ID:", patient.id)
        print("Temperatura corporal:", patient.TC)
        print("Frequência respiratória:", patient.FR)
        print("Oxigenação do sangue:", patient.OS)
        print("Pressão arterial:", patient.PA)
        print("Frequência cardíaca:", patient.FC)
        print("Estado Grave?", patient.state)
        reply = 'Server Says: ' + data.decode('utf-8') 
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()

#Método que inicia o loop principal da aplicação
def Socket_init():
    SensorCount = 0
    while True:
        Client, address = ServerSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        start_new_thread(Data_reciver, (Client, SensorCount))
        print('Thread Number: ' + str(SensorCount))
        SensorCount += 1 

Thread(target=Socket_init,args=()).start()