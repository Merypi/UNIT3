from Manejafacultades import manejador

if __name__=='__main__':
    man=manejador()
    man.cargar()
    man.mostrar()
    print("---Menu de opciones---")
    print("1:Mostrar carreras que se dicatan en una facultad")
    op=input("ingrese opción de menu:")

    while op !="0":
        if op=="1":
            cod=input("Ingresar codigo de facultad:")
            man.BuscarcodigoFac(cod)
        op=input("ingrese opción de menu:")
  