#Variables / Lista / Matrices
datos = [0]*4
resultados = [["Precio propiedad:",0],["Comisión:",0]]
resultados2= [["Precio propiedad:",0], ["Comisión:",0], ["Valor publicidad:", 0], ["Comsión neta:",0], ["Relación publicidad/comisión:",0]]

#Funciones
def evaluarcom(datos):
  resultados[0][1]= datos[0]
  resultados[1][1]= datos[0]*(datos[1]/100)
  return print("Los resultados serían los siguientes \n", resultados[0], "\n", resultados[1])

def evaluarpub(datos):
  resultados2[0][1]= datos[0]
  resultados2[1][1]= datos[0]*(datos[1]/100)
  resultados2[2][1]= datos[0]*datos[2]
  resultados2[3][1]= (datos[0]*(datos[1]/100)-datos[0]*datos[2])
  resultados2[4][1]= (datos[0]*datos[2])/(datos[0]*(datos[1]/100))*100
  return print("Los resultados serían los siguientes: \n", resultados2[0], "\n", resultados2[1], "\n", resultados2[2], "\n ", resultados2[3], "\n ", resultados2[4], "%")

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