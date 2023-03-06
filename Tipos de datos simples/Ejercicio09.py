#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
cantidad = float(input("Ingrese la cantidad de dinero a invertir: "))
años = int(input("Ingrese la cantidad de años en los que invertirá el dinero: "))
interes = float(input("Ingrese la tasa de interés anual: "))

capital_obtenido = round((cantidad * (interes/100+1) ** años),2)

print(f'El capital obtenido es de ${capital_obtenido}')