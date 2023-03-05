#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

horas = int(input("Introduzca la cantidad de horas trabajadas: "))
costo = float(input("Introduzca el costo por hora: "))

resultado = horas * costo

print(f'El pago correspondiente por {horas}hs. trabajadas es de ${resultado}.-')

