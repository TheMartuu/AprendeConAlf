#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

comprobar = True 

while comprobar:
    peso = float(input("Indique su peso (en kgs.): "))
    altura  = float(input("Indique su altura (en mts.): "))
    if peso >0 and altura >0: 
        imc = round(peso/pow(altura,2),2)        
        print(f'El índice de masa corporal es de {imc}.')
        comprobar = False
    else: 
        print("Los valores son inválidos, intente nuevamente")