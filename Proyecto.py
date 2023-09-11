#Variables
com = 0
pub = 0
dif = 0
rel= 0

#Funciones
def evaluarcom(precio, pcom, com):
    com = precio*(pcom/100) 
    return print("Los resultados serían los siguientes \n Valor de la propiedad:", precio, "\n Comisión:",com)
def evaluarpub(precio, pcom, ppub, com, pub, dif, rel):
    com = precio*(pcom/100)
    pub = precio*ppub    
    dif = com - pub
    rel = (pub/com)*100
    return print("Los resultados serían los siguientes \n Valor de la propiedad:", precio, "\n Comisión:",com,"\n Inversión en publicidad:", pub, "\n Comisón neta:", dif, "\n Porcentaje de publicidad respecto a la comisión:", rel,"%")

#Logaritmo principal
while True:
    accion = str(input("¿Qué desea calcular? \n1. Comisión \n2. Comisión y Publicidad \n"))

#Estructuras de decisión
    if accion == "1":
        precio = float(input("Precio de la propiedad a vender (en millones): \n"))*1000000
        pcom = float(input("Inserte el porcentaje de comisión (directa o compartida) en %: \n"))
        evaluarcom(precio, pcom, com)
        break
    elif accion == "2":
        precio = float(input("Precio de la propiedad a vender (en millones): \n"))*1000000
        pcom = float(input("Inserte el porcentaje de comisión (directa o compartida) en %: \n"))
        ppub = 0.0025
        evaluarpub(precio, pcom, ppub, com, pub, dif, rel)
        break
    else:
        print("Respuesta invalida, intente de nuevo \n")