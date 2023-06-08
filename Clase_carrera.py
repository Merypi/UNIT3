class Carrera:
    __codigo=0
    __name=""
    __fecha_inicio=""
    __duracion=""
    __titulo=""

    def __init__(self,codigo=0, nombre="", direccion="", duracion="", telefono=""):
        self.__codigo=int(codigo)
        self.__name=nombre
        self.__direccion=direccion
        self.__duracion=duracion
        self.__telefono=telefono

    def __str__(self) -> str:
        return("{} {} {} {} {}".format( self.__codigo, self.__name, self.__direccion, self.__duracion, self.__telefono))


    

