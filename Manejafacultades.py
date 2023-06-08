import csv
from Clase_facultad import Facultad

class manejador:
    __lista= []

    def __init__(self):
        self.__lista=[]

    def cargar(self):
        archivo=open("facultades.csv")
        reader=csv.reader(archivo, delimiter=",")
        cod=0
        
        for fila in reader:
            if int(fila[0]) == cod:
                # print(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5]) 
                # self.__lista[cod-1].
                Facultad.agregarcarrera(fila[1], fila[2], fila[3], fila[4], fila[5])
            else:
                facultad=Facultad(fila[0], fila[1], fila[2], fila[3], fila[4])
                self.__lista.append(facultad)
                cod = int(fila[0])

    def __str__(self):
        return("{}".format(self.__lista))
        
    def mostrar(self):
        for i in range(len(self.__lista)):
           print (self.__lista[i].getcodigo())
        

    def BuscarcodigoFac(self, cod):
        i=0
        Flag=False
        while i<len(self.__lista) and not Flag:
            if cod != self.__lista[i].getcodigo():
                Flag=True
            else:
                i+=1
        if Flag:
            Facultad.MostrarCarreras(i)