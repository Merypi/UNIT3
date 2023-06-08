import unittest

from Menu import menuOpciones
from Manejador import controlEmpleados


def test():
    listaempleados = controlEmpleados()
    listaempleados.cargarEmpleados()
    menu = menuOpciones()
    menu.opciones(listaempleados)


if __name__ == "__main__":
    test()