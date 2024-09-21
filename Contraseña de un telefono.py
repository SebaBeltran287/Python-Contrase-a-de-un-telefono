import os
os.system("cls")
datos=[]
cantidadpacientes=0
print("---------------------------")
print("     INGRESO PACIENTE      ")
print("---------------------------")
rut=input("Rut: ")
nombre=input("Nombre: ")
while True:
    try:
        edad=int(input("Edad: "))
        break
    except:
        print("la edad debe ser numérica")
        x=input("presione una tecla para continuar...")
fila=[]
fila.append(rut)
fila.append(nombre)
fila.append(edad)
datos.append(fila)
cantidadpacientes+=1
