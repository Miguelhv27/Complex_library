# Libreria de complejos

Los números complejos e imaginarios se emplean para resolver ecuaciones que no admiten soluciones en el conjunto de los números reales. Dado que su estructura difiere de la de los números tradicionales, las operaciones que se realizan con ellos presentan características y reglas particulares.

## Descripcion 

A lo largo de este proyecto se encuentran diferentes operaciones las cuales podemos hacer con numeros complejos. Las operaciones que estan definidas en este proyecto son suma, resta, multiplicacion, division, modulo, conjugado, conversion entre coordenadas polares y cartesianas, de igual manera se definio una conversion entre cartesianas y polares, la ultima funcion definida es la fase de un numero complejo.   

### Prerrequisitos

Para el uso adecuado de este proyecto hay que tener instalado un entorno en el cual se pueda usar python. 

### Instalación 

Inicialmente para instalar python, el primer paso es entrar en el navegador y entrar en la pagina oficial de python posteriormente tenemos que instalar la ultima version que hay disponible, y asi es como podemos tener acceso a python. 

## Pruebas y ejemplos de uso

Dentro de las funciones que estan definidas todas estan definidas por tuplas lo que indica que la primera parte de la tupla es la parte real del numero complejo y la segunda parte de la tupla es la parte imaginaria, por lo que para hacer cualquier operacion usando las funciones definidas, tenemos que escribir el numero complejo como una tupla.

### Ejemplo de suma de complejos

Para sumar dos numeros complejos los cuales son: 4 + 5i y 2 + 3i.

Primero los escribimos en tuplas lo cual nos daria el siguiente resultado: (4, 5) y (2, 3)

Una vez que ya tenemos escrito los numeros complejos en tuplas ahora lo que hacemos es llamar la funcion encargada de hacer la suma de dos numeros complejos la cual es:

```
sumcplx((4, 5), (2, 3))
```
El resultado de esa funcion es:

```
(6, 8)
```
Esto lo que nos indica es que el resultado de la suma de esos dos numeros complejos es: 6 + 8i

## Notas adicionales 

Tenemos que tener en cuenta que si usamos operaciones como la fase, conversion entre polares a cartesianas estas funciones solo nos piden un argumento, lo cual quiere decir que en esos casos tenemos que poner solo una tupla ya que la operacion no requiere dos numeros complejos para su correcto funcionamiento. 

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Miguel Ángel Hernández Vargas** 


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


