
# Tutorial #4 : Pruebas unitarias de código y _Test-Driven Development_

En informática, una **prueba unitaria** es una forma de comprobar el correcto funcionamiento de una porción de código.

Las pruebas unitarias deben ser:
- automatizables: *no requerir una intervención manual* (por ejemplo podrían realizarse al momento de desplegar una aplicación).
- completas: *deben ubrir la mayor cantidad de código.*
- repetibles o reutilizables: *No se deben crear pruebas que sólo puedan ser ejecutadas una sola vez.*
- independientes: *La ejecución de una prueba no debe afectar a la ejecución de otra.*

## 1. Introducción a la librería _PyTest_ para crear pruebas de código

Poder probar su código trae una amplia variedad de beneficios. En particular aumenta la **confianza** en el código desarrollo y permite evaluar su **fiabilidad**. La confianza/fiabilidad (_reliability_) es uno de los atributos de calidad / requisitos no funcionales al momento de construir un software.

En la primera parte de este tutorial, introducemos la libreria _PyTest_ (https://docs.pytest.org/en/stable/) que facilita el desarrollo de pruebas de software en Python.
```
pip install -U pytest
```
### 1.1 Ejemplos de pruebas básicas con PyTest

Creamos nuestra carpeta de trabajo:

    mkdir Tutorial_4_PyTest_TDD
    
El comando `pytest` ejecutará todos los tests que se encuentran en archivos **test_*.py** o ***_test.py** en la carpeta corrienta y sus sub-carpetas.

En la carpeta `ejemplo`, creamos el primer archivo de test siguiente **test_square.py**:

    import math
    
    def test_sqrt():
       num = 25
       assert math.sqrt(num) == 5
    
    def testsquare():
       num = 7
       assert 7*7 == 40
    
    def tes_equality():
       assert 10 == 11

El comando **assert** (en español "affirmar") consiste en afirmaciones que queremos probar. En este código queremos probar 3 afirmaciones. En este ejemplo, cada afirmación, o **assert**, está encapsulada en una función python.

Ejecutamos pytest:

    pytest -v

Observaciones:
- la función `test_sqrt` pasó con éxito
- la función `testsquare` falló
- la función `tes_equality` no pasó --> pytest ejecuta solo las funciones que empiezan por **test***

### 1.2 Ejecutar un conjunto de pruebas específicas

- **Por archivos**

Agreguemos un segundo archivo de pruebas llamado **test_compare.py**:

    def test_greater():
       num = 100
       assert num > 100
    
    def test_greater_equal():
       num = 100
       assert num >= 100
    
    def test_less():
       num = 100
       assert num < 200

El comando `pytest -v` ejecutará las funciones de pruebas de todos los archivos.
El comando `pytest test_compare.py -v`ejecutará solo las funcionalidades del archivo en parámetro.

**- Por palabra clave**

También existe la posibilidad de ejecutar un conjunto de pruebas a partir de un palabra clave. Por ejemplo el comando siguiente ejecutará todos los tests que contienen la palabra "great".

    pytest -k great -v

### 1.3 Ejecutar un código antes de probar los tests: *fixtures* (accesorios)

Las *fixtures* son funciones, que se ejecutarán antes de cada función de prueba a la que se aplique. En general, son funciones utilizadas para crear datos, instanciar variables o crear una conexión a una base de datos, que serán útiles para ejecutar pruebas.

En la carpeta "ejemplo", crear un archivo de test llamado: **test_div_by_3_6.py**

    import pytest
    
    @pytest.fixture
    def input_value():
       input = 39
       return input
    
    def test_divisible_by_3(input_value):
       assert input_value % 3 == 0
    
    def test_divisible_by_6(input_value):
       assert input_value % 6 == 0

### 1.4 Parametrizar los tests

La parametrización de una prueba se hace para ejecutar la prueba contra múltiples conjuntos de entradas. 

En **test_multiplication.py**:

    import pytest
    
    @pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
    def test_multiplication_11(num, output):
       assert 11*num == output

### 1.5 Ejecutar los tests en paralelo 

Por defecto, pytest ejecuta las pruebas en orden secuencial. En un escenario real, un conjunto de pruebas tendrá un número de archivos de prueba y cada archivo tendrá un montón de pruebas. Esto llevará a un gran tiempo de ejecución. Para superar esto, pytest nos proporciona una opción para ejecutar las pruebas en paralelo.

    pip install pytest-xdist

    pytest -n 3

### 1.6 Ejercicio 1: devolver el valor minimo de una lista de enteros

    mkdir ejercicio1

Queremos construir una función `get_min(values)` que recibe una lista de enteros como input y devuelve el valor mínimo como output.

1) Crear una función de prueba que permite afirmar que la función `get_min(values)` devuelve bien el valor mínimo.
2) Implementar la función que devuelve el valor mínimo de una lista de entero.

### 1.7 Ejercicio 2: Fibonacci

    mkdir ejercicio2


Queremos construir un función `fibonacci(n)` que devuelve cuál es el elemento de rango **n** en la serie de Fibonacci («empieza con 0 y 1, y cada término siguiente es la suma de los dos anteriores»).

Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, etc.

1) Crear una función que permite probar la función `fibonacci(n)`
2) Implementar la función `fibonacci(n)`

### 1.8 Ejercicio 3: Inversar una cadena de caracteres

    mkdir ejercicio3

Queremos construire una función inverse(string) que devuelve como output una cadena de caracteres escrito al revés ("hola" --> "aloh").

1) Crear una función que permite probar la función `fibonacci(n)`
2) Implementar la función `fibonacci(n)`

## 2. Test-Driven Development

El TDD (o desarrollo basado en pruebas) es una práctica simple de desarrollo de software que recomienda a un equipo de desarrolladores seguir tres pasos (**en este orden**) para crear software:

1.  Escribir una prueba que falla de una funcionalidad del software
2.  Escribir el código mínimo de la función para que la prueba pase
3.  Refactorizar el código según sea necesario

Este proceso iterativo se conoce comúnmente como el ciclo **Red-Green-Refactor**.

1.  Se escribe una prueba automatizada de cómo debería comportarse el nuevo código - **Rojo**
2.  Se escribe el código en la aplicación hasta que su prueba pase - **Verde**
3.  Se refactoriza el código para hacerlo más legible y eficiente. No hay necesidad de preocuparse de que la refactorización rompa la nueva función, sólo tiene que volver a ejecutar la prueba y asegurarse de que pasa. - **Refactor**

El desarrollo del código sigue volviendo en la etapa 1 (escribir una nueva prueba).

### 2.1 ¿Por qué?

El TDD permite responder a requisitos no funcionales:

1.  **Robustez**: TDD no elimina todos los errores, pero la probabilidad de encontrarlos es menor.
2.  **Evolutividad**: Al tener pruebas automatizadas para todas las funciones, los desarrolladores se sienten más seguros al desarrollar nuevas funciones. Se vuelve trivial probar todo el sistema para ver si los nuevos cambios rompen lo que existía antes.
3.  **Mantenibilidad**: Las pruebas requieren que modelamos las entradas y salidas de las funciones - TDD nos obliga a pensar en la API de cada modulo antes de empezar a codificar.
4.  **Documentation**: Las pruebas pueden ser usadas como documentación adicional. A medida que escribimos las entradas y salidas de una función, un desarrollador puede mirar la prueba y ver cómo la interfaz del código está destinada a ser utilizada.

### 2.2 Cobertura de código

La cobertura de código es una métrica que mide la cantidad de código fuente que está cubierto por sus pruebas. `pytest-cov` es un plugin de `pytest` que permite medir el nivel de cobertura de código.

> $pip install pytest-cov

La cobertura de código del 100% significa que todo el código que has escrito ha sido utilizado por alguna prueba. Una alta cobertura de código no significa que su aplicación no tenga errores. Es más que probable que el código no haya sido probado para todos los escenarios posibles.

### 2.3 Ejercicio 4: devolver un booleano que indica si un número es primo o no

Un número primo es un número superior a 1 y que solo se puede dividir por 1 o si mismo...

    mkdir ejercicio4

 - Escribir la prueba (rojo)

En test_primes.py:

    from primes import is_prime
    
    #Si introducimos 1, entonces no debe ser un número primo.
    def test_prime_number():
        assert is_prime(1) == False
 
 - Escribir el código mínimo (verde)
 
 En primes.py:

     def is_prime(num):
        if num == 1:
            return False

Probar el código:

    pytest --cov=.

- Refactorizar 

En primes.py:

    def is_prime(num):
        # Prime numbers must be greater than 1
        if num < 2:
            return False

- Escribir una nueva prueba (Rojo)

Sabemos que 29 debería ser un número primo.

En test_primes.py:

    def test_prime_number_2():
        assert is_prime(29)

- Actualizar el código:

En primes.py:

    import math
    
    def is_prime(num):
        # Prime numbers must be greater than 1
        if num < 2:
            return False
        #Prime numbers mu
        for n in range(2, math.floor(math.sqrt(num) + 1)):
            if num % n == 0:
                return False
        return True

- Escribir una nueva prueba:

En test_primes.py:

    def test_prime_other_number():
        assert is_prime(15) == False
        
### 2.4 Ejercicio 5: Calcular la suma de los números primos a partir de una lista de números

    cp -R ejercicio4 ejercicio5

Queremos implementar una función `sum_of_primes([])`que recibe como input una lista de números y devuelve la suma de los números primos.

1) Seguir un proceso de *Test-Driven Development* para desarrollar está función.
2) Desarollar al menos un test parametrizado.


## 3. Para prácticar TDD

Utilizando Python, PyTest y la metodología TDD, resolver los problemas de programación siguientes

    Números romanos: http://codingdojo.org/kata/RomanNumerals/
    Fizzbuzz: http://codingdojo.org/kata/FizzBuzz/
    Trading cards Kata: http://codingdojo.org/kata/TradingCardGame/
    Diamond Kata: http://codingdojo.org/kata/Diamond/


## 4. Tarea

1. A partir la correción N°2 del Bot Néstor, agregar pruebas unitarias a los distintos componentes de la arquitectura. ¿Qué ejemplos de pruebas proponen?

2. ¿Cómo se podría combinar las pruebas unitarias con Docker?


## 5. Próxima semana

Integraremos pruebas unitarias y seguiremos un desarrollo basado en pruebas para añadir nuevas funcionalidades a nuestra arquitectura de bot.

 


