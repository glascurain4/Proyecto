#Variables / Lista
datos = [0]*4

#Funciones
def evaluarcom(datos):
  return print("Los resultados serían los siguientes \n Valor de la propiedad:",datos[0], "\n Comisión:",(datos[0]*(datos[1]/100)))
  
def evaluarpub(datos):
  return print("Los resultados serían los siguientes \n Valor de la propiedad:", datos[0], "\n Comisión:",(datos[0]*(datos[1]/100)),"\n Inversión en publicidad:", datos[0]*datos[2], "\n Comisón neta:", (datos[0]*(datos[1]/100)-datos[0]*datos[2]), "\n Porcentaje de publicidad respecto a la comisión:", ((datos[0]*datos[2])/(datos[0]*(datos[1]/100))*100),"%")

#Logaritmo principal
def main():
  while True:
    datos[3] = str(input("¿Qué desea calcular? \n1. Comisión \n2. Comisión y Publicidad \n"))

    #Estructuras de decisión
    if datos[3] == "1":
      datos[0] = float(input("Precio de la propiedad a vender (en millones): \n"))*1000000
      datos[1] = float(input("Inserte el porcentaje de comisión (directa o compartida) en %: \n"))
      evaluarcom(datos)
      break
    elif datos[3] == "2":
      datos[0] = float(input("Precio de la propiedad a vender (en millones): \n"))*1000000
      datos[1] = float(input("Inserte el porcentaje de comisión (directa o compartida) en %: \n"))
      datos[2] = 0.0025
      evaluarpub(datos)
      break
    else:
      print("Respuesta invalida, intente de nuevo \n")

main()
