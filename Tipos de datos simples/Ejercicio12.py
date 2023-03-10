#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

barras=3.49 
descuento = 60/100

ventas = int(input("Ingrese el número de barras de pan que no son del día: "))
precio_habitual = barras * ventas
print(f'El precio habitual por las barras es de {precio_habitual}')
precio_descontado = barras * (1 -descuento)*ventas
print('El descuento aplicado por una barra no fresca es de '+ str(descuento*100)+ "%")
print('El precio final con el descuento aplicado es de $' + str(round(precio_descontado,2)))