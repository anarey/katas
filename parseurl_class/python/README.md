Kata URL parse using regrex
==========================

Descripción
-----------

Crear un parseador de URL aplicando conceptos de orientación a objetos.

El parseo consistirá en poder obtener de una url tipo `http://www.site.com/something/index.html` tres valores:
* el **protocolo**: `http`
* el **host**: `www.site.com`
* el **path**: `something/index.html`

Empezaremos con el protocolo, pasando por los distintos tipos de tests, luego el host y posteriormente el path.

Objetivo
--------

El objectivo de este ejercicio es aprender a trabajar con **orientación a objetos** en Python mientras practicamos **TDD**.

Metodología y cosas a recordar
------------------------------

Usaremos los test que ya tenemos del ejercicio anterior (`parseurl`). Comentaremos los tests, para ir descomentándolos e implementándo el código para pasarlos uno a uno.

En cuanto veamos que el código se complica mucho o hay código duplicado y tengamos _green_ en los tests, trataremos de refactorizar el código. Siempre ejecutando los tests en cada cambio y asegurándonos de que sigue _green_.

Para hacer un buen seguimiento, haremos un commit por cada cambio. Esto es, cuando descomentemos un test que falle (_red_), cuando creemos el código que hacer que pase el test (_green_) y cuando refactorizemos código o tests.

Recursos
--------

* Info sobre [cómo trabajar con expresiones regulares en Python](http://docs.python.org/howto/regex.html).
* Herramienta _online_ para [probar expresiones regulares en Python](http://www.pythonregex.com/).
