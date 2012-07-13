# Travis - CI

## Introducción:

* [Travis-ci](http://travis-ci.org/) es un servicio distribuido de Integración y generación continua.
* Permite conectar un repositorio de Github y probar el código desarrollado una vez publicado en el servidor.

* Este servicio dispone de distintor runtime con distinas configuraciones de librerías, lenguajes de programación y bases de datos de forma que podamos probar nuestro proyecto sobre distintas arquitecturas sin tener que tener todas ellas montadas por nosotros.

## Pasos para su configuración. 

* Autenticarse con la cuenta de github sobre Travis-ci.
* Indicar los repositorios sobre los que estemos interesados en el servicio de travis-ce través de la pagina de http://travis-ci.org/profile y configurar los parámetros sobre el token de la app (Normalmente viene configurado)

* Crear un fichero `.travis.yml` donde indicaremos las características del entorno del proyecto. **Nota:** Importante validar la correcta configuración del fichero, sino, coge los parámetros por defecto de Ruby

* Hacer un push del commit con el que has añadido el fichero .travis.yml sobre el proyecto para indicar a travis-ci que debe generar el proyecto.

## Enlaces
* [Primeros pasos con Travis-ci](http://about.travis-ci.org/es/docs/user/getting-started/)
