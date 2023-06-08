from Clase_carrera import Carrera
class Facultad:
    __codigo=0
    __name=""
    __direccion=""
    __localidad=""
    __telefono=""
    __Carreras=[]

    def __init__(self, codigo=0, nombre="", direccion="", localidad="", telefono="", lista=[]):
        self.__codigo=int(codigo)
        self.__name=nombre
        self.__direccion=direccion
        self.__localidad=localidad
        self.__telefono=telefono
        self.__Carreras=lista

    def str(self):
        return("{} {} {} {} {} {}".format(self.__codigo, self.__name, self.__direccion, self.__localidad, self.__telefono, self.__Carreras))

    def agregarcarrera(self, codc, nombre, fecha, duracion, titulo):
        crear=Carrera(codc, nombre, fecha, duracion, titulo)
        self.__Carreras.append(crear)
    
    def getcodigo(self):
        return self.__codigo
    
    def MostrarCarreras(self, cod):
        for i in range(len(self.__Carreras)):
            if cod == self.getcodigo():
                print(self.__Carreras)



    


