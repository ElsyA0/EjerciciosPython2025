#          PROGRAMACIÓN PARA CIENCIA DE DATOS  
#                      ENTREGABLE 1
#         
#           Alumna: Elsy Rosario Morales Altamirano
#        Profesor: Gerardo Alexis Villavicencio Perez
#                      21/11/2025
#
#-------- EJERCICIO 1. Número par o impar.------------------
#Primero el codigo pide al usuario que ingrese un número entero
numero_entero = input("Ingrese un numero entero, y despues de ENTER ") 

# Se inicia una estructura de control if, si el modulo/resto de el número que el usuario ingreso 
# es 0 entnoces el numero es par, si no el numero es impar y 
# cualquier otro caso imprime el mensaje revisar.
if int(numero_entero) % 2 == 0: #int convierte el tipo de dato a un interger
    print(f"{numero_entero} es un numero par")
elif int(numero_entero) % 2 != 0:
    print(f"{numero_entero} es un numero impar")
else:
    print("Revisar")




#--------- EJERCICIO 2. Números naturales con ciclo while.-----------
# Primero el codigo pide al usuario que ingrese un número entero y positivo.
numero_entero_positivo = input("Ingrese un numero entero positivo y de ENTER ")

#Se creea una función que tiene una estrucutra de control y a su vez esta tiene un ciclo while
def ejercicio_dos(numero_entero_positivo):
    #validar que el numero sea entero y positivo.
    if int(numero_entero_positivo) <=0: #int convierte el tipo de dato a un interger
        print("Por favor ingrese un numero mayor a 0")
    else:
        print("Pensando")
    #Ciclo while
    #Este compara el número que el usuario ingreso contra la variable x de valor inicial 0
    #Mientras el número ingresado se menor o igual a la variable x
    # imprime la variable y luego esta suma +1.
        x = 1
        while x <= int(numero_entero_positivo):
            print(x)
            x+=1
ejercicio_dos(numero_entero_positivo)




#--------- EJERCICO 3. Calculo de descuento.-----------------------------
#Primero el codigo pide al usuario que ingrese el precio original del articulo y su porcentaje
precio_original = input("Ingrese el precio original del articulo y de ENTER ")
descuento = input("Ingrese el porcentaje de descuento sin el simbolo % y de ENTER ")
print("Calculando")

# Se crea una función en donde primero se convierte el porcentaje para poder trabajar con el matematicamente.
# ejemplo: convierte 20 a 0.20
def Calcular_descuento (precio_original, descuento):
    corvertir_descuento = float(descuento) / 100 #float convierte el tipo de dato a un float (números con decimales). 
    calculo_descuento = float(precio_original) * corvertir_descuento
    #Aqui se hace la opracion para obtener cuanto descuento tendria el articulo, para 
    #posteriormente restarle la cantidad al precio original 
    # y finalmente obtener lo que costaria el articulo ya con descuento.
    precio_Total = float(precio_original) - calculo_descuento

    print(f"El articulo quedaria a un precio de {precio_Total} pesos")
Calcular_descuento(precio_original, descuento)




#---------- EJERCICIO 4. Conteo de Pares e Impares.---------------------
#Se importa random para poder general lista de núemros aleatorios
import random

#Primero el codigo pide al usuario que ingrese la cantidad de números que quiere que se generen.
#Con ayuda de random se le pide que produzca numeros aleatorias dentro del rango: 0 hasta 1000
n = int(input("Ingrese cuantos números aleatorios quiere generar y de ENTER ")) #int convierte el tipo de dato a un interger.
lista_numeros = [random.randint(0,1000) for _ in range(n)]
print(f"La lista de números generada es: {lista_numeros}") #Imprime la lista que se genera.

def contando_pares_impares (lista_numeros):
    #Se creafunción que inicializa dos variables (par, impar) en 0 y luego se crea un ciclo for para poder determinar
    # si el numero es par o impar.
    par = 0
    impar = 0
    for numero in lista_numeros:
        #el ciclo compara el numero generado en la lista y si es par suma 1 a la variable "par"
        # en caso de que el numero sea impar entonces suma 1 a la variable "impar"
        # cualquier otro caso imprime "Revisar"
        #el ciclo termina cuando se acaban los numeros dentro de la lista generada e imprime la cantidad de numeros pares e impares que tenia la lista.
        if numero % 2 == 0:
            par+=1
        elif numero % 2 != 0:
            impar+=1
        else:
            print("revisar")
    print(f"En la lista hay {par} números pares y {impar} números impares")
contando_pares_impares(lista_numeros)



#---------- EJERCICIO 5. Seciencia de Fibonacci con recursión.-----------
#Primero el codigo pide al usuario que ingrese un número entero y positivo.
n = int(input("Ingrese un número positivo y de ENTER ")) #int convierte el tipo de dato a un interger

#Se crea una función en donde se construye una lista desde los casos base n=1 y n=2
#Cada llamda recursiva calcula el siguiente termino como la suma de los dos anteriores.
def Secuencia_Fibonacci (n):
    if n <= 0: #Validar que el número sea positivo.
        return[]
    elif n == 1:
        return[0]
    elif n == 2 :
        return[0, 1]
    else:
        secuencia = Secuencia_Fibonacci(n-1)
        siguiente = secuencia[-1] + secuencia[-2]
        secuencia.append(siguiente)
        return secuencia
#Finalmente se le inicializa la variable resultado para llamar a la funcion creada.
# Y se imprime la lista completa de los resltados. 
resultado = Secuencia_Fibonacci(n)
print(f"Los primeros {n} términos de la secuencia Fibonacci son: {resultado}")
