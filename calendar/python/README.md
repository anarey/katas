# Diccionarios: 

* Conjunto no ordenado de pares clave: valor.
* Las claves han de ser únicas.

## Operaciones básicas:
* Crear un diccionario vacio: `dicVacio = {}` 
* Crear un diccionario con contenido: 

```
dias_laborables = {'lunes' : True,
                        'martes': True,
                        'miercoles': True}
```
* Añadir un elemento al diccionario: `dias_laborables['jueves'] = True`
**Nota**: Si la clave existe, sobreescribe el valor.

* Devolver la lista de claves de un diccionario: dias_laborables.keys() 

* Comprobar si existe una clave: `if 'Jueves' in dias_laborables:`
* Eliminar un elemento: ``
* Más información: [Diccionarios en Python](http://docs.python.org.ar/tutorial/datastructures.html#diccionarios)

# Excepciones. 

* Tratar una excepción:
```
   try:
        ## Código que puede provocar una excepción.
   except NombreExcepcion: ## Nombre de la/s excepciones a capturar/tratar
        ## Código a ejecutar si captura esa excepción.
    else: 
        ## Bloque opcional que se ejecuta en el caso de que no se lance ninguna excepción en el bloque try. 
    finally: 
        ## Codigo opcional que se lanza siempre hay lanzado o no excepciones. 
```

* Las excepciones que no se controlan dentro de un bloque de código try/except se propagan a un nivel superior que la procese o corta la ejecución del programa.

* Se pueden indicar todos los except que sean necesarios

* Ignorar una excepción que se produzca: 
```
try:
        ### Código
   except NombreExcepcion:
        pass
```

* Excepciones con argumentos. [TODO]

* Forzar a que se produzca una excepción expecífica: `raise` 
`raise NameError('Hola')`

* Crear nuestras propias excepciones: 
```
import re

class MyError(Exception):
    def __init__(self, value_exception):
        self.value_exception = value_exception
        
    def __str__(self):
        return self.value_exception
        
class NotProtocolFoundError(MyError):
    pass
    
class NotSiteFoundError(MyError):
    pass
```

## Manejar errores en tiempos de ejecución
```
>>> try:
...     esto_falla()
... except ZeroDivisionError as detail:
...     print 'Manejando error en tiempo de ejecucion:', detail

* Objetos con «métodos de limpieza»
with open("miarchivo.txt") as f:
    for linea in f:
        print linea
```
Cierra el archivo tanto si hubo un error como sino. Hay más objetos con estas funciones. TODO

# Calendario.

* Modulo `Calendar`. Mirar también `datatime` y `time`
* Tener en cuenta el día en el que empieza la semana.
* leap year = Año bisiesto.
* Día de la semana de una fecha concreta: `calendar.weekday(2012, 7, 6)`
Deuelve un 0-6 (Lunes-domingo)
* Calendario del año indicado: `calendar.prcal(2012)`
* Sumar x días a una fecha: 
```
one_day = datetime.timedelta(days=1)
day = day + one_day
```

# Sobre assert en Unittest:

* assertFalse(expr, msg=None) Test that expr is true (or false).

* assertIs(expr, True): Comprobar el tipo de datos.
