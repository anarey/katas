Kata Calendar
==============

Descripción
-----------

Calendario en el que consultar los días laborables y festivos.

Al final del ejercicio debemos tener alguna forma (función, método o lo que sea) obetener lo siguinte:
* Dado un día de la semana, ¿es laborable o no?
* Dado un día de un mes y un año, ¿es laborable o no?
* Dado un rango de días, decir qué días son laborable y qué días festivos.

La idea es tener una función o método que permita obtener esto último, pero lo iremos implementando en este orden.

**NOTA:** Entenderemos por día de laborable cualquier día de _lunes_ a _viernes_ y festivos, los _sábados_ y _domingos_. 

Objetivo
--------

El objectivo de este ejercicio es aprender a trabajar con las **fechas** en Python mientras practicamos **TDD**.

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

