#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
dolls =  75
clown = 112 
cant_dolls = int(input("Ingrese la cantidad de muñecas: "))
cant_clowns = int(input("Ingrese la cantidad de payasos: "))

peso_dolls = dolls * cant_dolls
peso_clowns= clown * cant_clowns

peso_total = peso_clowns+peso_dolls

print(f'Se han vendido {cant_clowns} payasos y {cant_dolls} muñecas. El peso total del pedido es de {peso_total} grs. ')
