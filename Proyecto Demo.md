# Proyecto

El contexto consistiría en el uso de un vendedor de propiedades o acesor inmobilairio, que basado en el valor de venta de una propiedad pueda calcular la inversión apropiada para publicitar la propiedad, así como el valor de su comisión de lograr la venta y compararlos. Este ejemplo me es interesante ya que recientemente comencé a trabajar con ventas del sector inmobiliario y un compañero de mayor edad con experiencia me explicó de la relación de valores que existe a la hora de invertir en publicidad.

ALGORITMO>

ENTRADAS
precio = Precio de venta de la propiedad
pcom = Porcentaje de comisión
ppub = Porcentaje de inversión en publicidad seleccionado

PROCESO
com = Precio propiedad * Porcentaje comisión
pub = Precio propiedad * Porcentaje publicidad
dif = Total comisión - Total publicidad
rel = (Total publicidad / Total comisión )*100

SALIDAS
print(
com = Total de comisión
pub = Total de publicidad
dif = Ganancia neta (comisión - publicidad)
