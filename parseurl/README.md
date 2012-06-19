Kata URL parse
==============

Se trata de parsear una URL. Para hacerlo bien iremos poco a poco y
siguiendo la progresión típica de los tests:
* Caso más simple _positivo_.
* Caso negativo.
* Caso concreto distinto.
* Más de un caso concreto.
* Casos _bordes_ o extremos.

El parseo consistirá en poder obtener de una url tipo
`http://www.site.com/something/index.html` tres valores:
* el **protocolo**: `http`
* el **host**: `www.site.com`
* el **path**: `something/index.html`

Empezaremos con el protocolo, pasando por los distintos tipos de
tests, luego el host y posteriormente el path. Y sólo implementaremos
aquello que nos haga falta para poder pasar los tests.

