#Pedir que se ingresen 3 numeros
numero1 = int(input("ingrese un numero: "))
numero2 = int(input("ingrese un segundo numero: "))
numero3 = int(input("ingrese un tercer numero: "))

print("")
print("")

#ingresar la opcion que se desea realizar. 
print("elija la opcion.")
print("Realizar la primera opcion")
print("Realizar la segunda opcion")
opcionnumero1= int(input())
opcionnumero2= int(input())
#ejecutar las funciones.
if(opcionnumero1==1):
    if(numero1>numero3):
        print("debido a que el primer numero ingresado es mayor que el tercero, se realizó la multiplicacion de los tres numeros.")
        print("su resultado es: ",numero1*numero2*numero3)
    if (numero1==numero2 & numero2==numero3):
        print("debido a que el valor de las 3 variables es igual se realiza la suma de de los tres.")
        print("su resultado es: ",numero1+numero2+numero3)
    if (numero2==0):
        print("debido a que el valor de la segunda variable es 0 se restara el mayor menos el menor")
        if(numero1>numero3):
            print("su resultado es: ",numero1-numero3)
        if (numero3>numero1):
            print("su resultado es: ", numero3-numero1)
if(opcionnumero2==2):

    print("el resultado al unir es: ",numero1,numero2,numero3)
    
