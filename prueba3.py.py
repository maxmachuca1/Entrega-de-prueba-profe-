import csv 
opc="" 
computador=0 
prestamo=0
nombre="" 
rut=""
documento=""
lista_prestamos=""
while True: 
    print('''Prestamo sala 021
          1-.Registrar prestamo
          2-.Registrar devolucion
          3-.Listar prestamos
          4)Terminar clase''')
    opc=int(input("Ingrese una opcion"))
    while opc.isnumeric()==True:
        opc.isnumeric()
        print("Opcion invalida. intentelo de nuevo")
        opc=int(input("Seleccione una opcion"))
        opc=int(opc)
    break

if opc==1:
    print("Ingrese datos de estudiante")
    nombre=input("Nombre:")
    if nombre.isalpha()==True:
        nombre.isalpha
    else:
        print("Vuelve a ingresar el nombre")
        nombre=input("Nombre: ")
        rut=input("Rut: ")
        print("Ingrese numero dedocumento")
        