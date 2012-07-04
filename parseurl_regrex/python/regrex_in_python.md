# Expresiones regulares.

## Introducción
* *Expresión regular*: Patrón que describe un cierto texto.
* En Python se utilizan a través del módulo `re`.
* Hacen distinción entre mayusculas y minúsculas.
* Para «capar» carácteres en los patrónes de búsqueda se utiliza el carácter "\"
 Ej: `\.` representa a un punto

## Opciones:
* `re.search(patron, cadena, flag)` # busca el patrón en toda la cadena. Si encuentra coincidencia devuelve el objeto `MatchObject`
* `re.match()` # busca coincidencia con el patrón en la cadena, *sólo* al principio.
* `re.compile()`  # Compilar la expresión regular. Para cuando se va a usar ese patrón más veces.
* `re.findall()` # devuelve una lista con las subcadenas que cumplieron el patrón.
* `re.finditer()` # devuelve un iterador con el que consultar uno a uno los distintos MatchObject
* `re.split()` # Devuelve las subcadenas que se obtienen al eliminar el patrón indicado. Si es la primera coincidencia, el primer valor de la lista es vacio:
```
>>> pato = re.compile("www\.[a-z0-9]+\.[a-z0-9]+/")
>>> pato
<_sre.SRE_Pattern object at 0x1923360>
>>> pato.split("www.sss.eeee/ssss/seeff.s")
['', 'ssss/seeff.s']
```
* `re.sub`: 

### Flag (Banderas)

re.IGNORECASE ## no hace distinción entre mayúsculas y minúsculas.
re.VERBOSE ## que hace que se ignoren los espacios y los comentarios en la cadena que representa la expresión regular.


## Reglas para crear los patrones:

* `.` => Cualquier carácter, solo uno.
Ejemplo: `...\.` # La cadena tiene 3 carácteres, seguidos por un punto.

* `patroa| patrónB` => # alternancia entre patrones.
* `(j|m|r)ana` => # Encerramos entre paréntesis la parte que puede cambiar en el patrón.
* `[jmr]ana` => igual.  ## Dentro de los [] no hay que capar los carácteres especiales.
* `^` => # negar una expresión.

### Indicar repeticiones de un carácter, de una clase [abc] o un subpatron (abc)

* `+`: El caracter de la izquierda del + se puede repetir n veces (como mínimo 1)
* `*`: Lo situado a la izquierda, se puede repetir cero o n veces.
* `?`: Lo situado a la izquierda, es opcional, o se encuentra una o cero veces.
* `{n}`: Lo situado a la izquierda se repite n veces

### Especificar de la posición donde se encuentra una cadena:

* `^`: inicio de la cadena
* `$`: fin de la cadena.

### Ejemplos: 

* `\A`: La cadena empieza
* `[0-9]`: Representa un caracter comprendido entre el 0-9
* `(hola, adios)`: Opciones de patrones.
* `.*`: Cualquier secuencia de caracteres.

### Secuencias predefinidad:

* `\d` : Un dígito. Equivale a [0-9]
* `\D` : Cualquier carácter que no sea un dígito. Equivale a [^0-9]
* `\w` : Cualquier caracter alfanumérico. Equivale a [a-zA-Z0-9_].
* `\W` : Cualquier carácter no alfanumérico. Equivale a [^a-zA-Z0-9_].
* `\s` : Cualquier carácter en blanco. Equivale a [ \t\n\r\f\v]
* `\S` : Cualquier carácter que no sea un espacio en blanco. Equivale a [^ \t\n\r\f\v]


## Valores que devuelve re.search(patron, string, flag):

* Sino lo encuentra, None
* Si encuentra coincidencia: devuelve un objeto MatchObject 

### Metodos útiles:

* group(): contiene la cadena encontrada a través del patron buscado.
* grouos(): Contiene todas las cadenas encontradas que cumplen el patrón buscado


## Enlaces de consulta:
* Python Regular Expression Testing Tool: http://www.pythonregex.com/
* http://docs.python.org/howto/regex.html
* http://mundogeek.net/archivos/2008/04/09/python-expresiones-regulares/

