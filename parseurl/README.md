Kata URL parse
==============

Descripción
-----------

Crear un parseador de URL.

El parseo consistirá en poder obtener de una url tipo `http://www.site.com/something/index.html` tres valores:
* el **protocolo**: `http`
* el **host**: `www.site.com`
* el **path**: `something/index.html`

Empezaremos con el protocolo, pasando por los distintos tipos de tests, luego el host y posteriormente el path.

Objetivo
--------

El objectivo de este ejercicio es aprender a trabajar con **las cadenas de texto** en Python mientras practicamos **TDD**.

Metodología y cosas a recordar
------------------------------

Hacer primero los tests y sólo implementar lo mínimo para ir pasando cada uno de los tests.

Para hacerlo bien iremos poco a poco y siguiendo la progresión típica de los tests:
* Caso más simple _positivo_.
* Caso negativo.
* Caso concreto distinto.
* Más de un caso concreto.
* Casos _bordes_ o extremos.

En cuanto veamos que el código o los tests se complican mucho o hay código duplicado y tengamos _green_ en los tests, trataremos de refactorizar los tests y el código. Siempre ejecutando los tests en cada cambio y asegurándonos de que sigue _green_.

Para hacer un buen seguimiento, haremos un commit por cada cambio. Esto es, cuando creemos un test que falle (_red_), cuando creemos el código que hacer que pase el test (_green_) y cuando refactorizemos código o tests.

