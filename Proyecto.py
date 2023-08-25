precio = float(input("Precio de la propiedad a vender (en millones):"))
pcom = float(input("Inserte el porcentaje de comisión (directa o compartida) en %:"))
ppub = 0.0025

com = (precio*1000000)*(pcom/100)
pub = (precio*1000000)*ppub
dif = com - pub
rel = (pub/com)*100

print("Los valores serían los siguientes: \n Valor propiedad:", precio*1000000, "\n Comisión:", com, "\n Pago por publicidad:", pub, "\n Comisión neta:", dif, "\n Porcentaje por publicidad respecto a la comisión:", rel,"%")