#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
ahorros = float(input("Ingrese la cantidad ahorrada: "))
interes = 4/100

cantidad1 = ahorros * (1 + interes)
print("Balance tras el primer año:" + str(round(cantidad1, 2)))
cantidad2= cantidad1 * (1 + interes)
print("Balance tras el segundo año:" + str(round(cantidad2, 2)))
cantidad3 = cantidad2 * (1 + interes)
print("Balance tras el tercer año:" + str(round(cantidad3, 2)))