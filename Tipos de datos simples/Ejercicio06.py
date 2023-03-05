# Escribir un programa que lea un entero positivo 'n' introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta 
# n La suma de los primeros enteros positivos puede ser calculada de la siguiente forma: suma = (n*(n+1))/2)

comprobar = True 
while comprobar: 
    n = int(input("Introduzca un número entero positivo: "))
    if n>0: 
        resultado = n*(n+1)/2
        print(f'El resultado es: {resultado}')
        comprobar = False
    else: 
        print('Número inválido, intente nuevamete. ')