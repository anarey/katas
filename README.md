Katas para TDD en Python
========================

Descripción:
------------
Ejercicios de programación para aprender y practicar TDD (Test Driven Development) con Python.

Cada directorio contiene un ejercio que iré realizando siguiendo la metodología TDD.

Metología a seguir:
-------------------

Se llevarán a cabo los ejercicios siguiendo el ciclo **red-green-refactor** de TDD, que se intentará reflejará cada estado en los commits.

Se empezará con los test siguiendo la siguiente secuencia de test:

* Caso más simple _positivo_.
* Caso negativo.
* Caso concreto distinto.
* Más de un caso concreto.
* Casos bordes o extremos.
* Casos raros.

Y se implementará sólo el código necesario para cada test, siguiendo los llamados «_baby-steps_».

Estructura de ejemplo:
----------------------

La estructura básica de un archivo de test en Python es la siguiente:

```python
import unittest

class test_something(unittest.TestCase):
   def test_something1(self):
       self.assertTrue(True)

if __name__ == '__main__':
   unittest.main()
```

Ejemplos de métodos que se pueden usar
-------------------------------------

* `assertEqual()`
* `assertNotEqual()`
* `assertTrue()`
* `assertFalse()`
* `assertRaises()`

Documentación de apoyo:
-----------------------

Aquí tienes más info sobre métodos 'assert' que puedes usar:
* http://docs.python.org/library/unittest.html#unittest.TestCase

Como ejecutar un test en Python:
--------------------------------
`$python -m unittest testNombre' [El nombre del archivo sin extensión]

Realizado por:
--------------

* [Ana Rey](https://github.com/anarey) 
* [Juanje Ojeda](https://github.com/juanje) 
