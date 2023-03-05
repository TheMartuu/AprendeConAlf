#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
n= int(input("Inserte el primer número: "))
m= int(input("Inserte el segundo número: "))

cociente = n//m 
resto = n%m 

print(f'{n} dividido {m} da un cociente de {cociente} y un resto de {resto}')