# Calculadora de Publicidad y Comisiones Inmobiliarias

Este proyecto se centra en el desarrollo de una herramienta para calcular y comparar la inversión en publicidad con las ganancias generadas por comisiones en el sector inmobiliario. Surge de la necesidad práctica de tomar decisiones estratégicas sobre la inversión en publicidad para propiedades, optimizando el retorno de inversión.

## Funcionalidades Principales

1. **Cálculo de Comisiones**
   - Determina el total de ganancias por comisiones basado en un porcentaje especificado y el precio de venta de la propiedad.

2. **Cálculo de Inversión en Publicidad**
   - Estima el monto a invertir en publicidad como un porcentaje del precio de venta.

3. **Análisis Comparativo**
   - Calcula la ganancia neta restando la inversión en publicidad de las comisiones.
   - Determina la relación porcentual entre la inversión en publicidad y las ganancias por comisiones.

4. **Salidas Consolidadas**
   - Total de comisión esperada.
   - Total invertido en publicidad.
   - Ganancia neta.
   - Relación porcentual de inversión respecto a la comisión.

## Estructura del Proyecto

- `Proyecto.py`: Contiene la implementación del programa en Python basada en el pseudocódigo.
- `README.md`: Este archivo, que describe el propósito y las funcionalidades del proyecto.
- `Proyecto Demo.md`: Posiblemente una versión inicial o alternativa de la documentación.

## Pseudocódigo Implementado

### Entradas
- `precio`: Precio de venta de la propiedad.
- `pcom`: Porcentaje de comisión.
- `ppub`: Porcentaje de inversión en publicidad seleccionado.

### Proceso
1. Calcular el total de la comisión:
   ```python
   com = precio * pcom

