# Tutorial #1 : Docker

Este tutorial es inspirado del tutorial de [Alexander Ryabtsev](https://djangostars.com/blog/what-is-docker-and-how-to-use-it-with-python/). Introduce los conceptos de contenedores Docker para facilitar el despliegue de arquitecturas de software en producción más frecuentes y rápidos. 

 1. Introducción 
 2. Despliegar un primer contenedor Docker básico en práctica
 3. Crear sus propias imágenes con el archivo *Dockerfile*
 4. Combinar varias imágenes para construir software complejos con *Docker-compose*
 5. Preguntas
 6. Ejercicio

## 1. Introducción
### 1.1 ¿Qué es Docker y la integración por contenedores?

[Docker](https://www.docker.com/resources/what-container) corresponde a una herramienta de código abierto  que sirve para **empaquetar, transportar y ejecutar softwares** de distintos niveles de complejidad. Esta herramienta es un modelo de virtualización que se encarga de crear una capa de abstracción con el sistema operativo.

La idea principal de esta herramienta es crear contenedores portables para que las aplicaciones de software puedan ser ejecutadas en cualquier máquina que tenga Docker instalado, sin importar el sistema operativo que la máquina tenga instalado, **facilitando enormemente los despliegues de aplicaciones**.

Cuando se desarrolla una aplicación, se necesita proporcionar el código junto con todas las dependencias posibles como bibliotecas, el servidor web, bases de datos, etc. Es posible que se encuentre en una situación en la que la aplicación esté funcionando en su ordenador, pero que ni siquiera se inicie en el servidor de test o de producción.

Este desafío puede ser resuelto aislando la aplicación para que sea independiente del sistema.

### 1.2 ¿En qué se diferencia de la virtualización?

Tradicionalmente, se utilizaban [máquinas virtuales](https://es.wikipedia.org/wiki/M%C3%A1quina_virtual) para evitar este comportamiento inesperado. El principal problema de la VM es que un "sistema operativo adicional" en la parte superior del sistema operativo del host añade gigabytes de espacio al proyecto. La mayoría de las veces su servidor alojará varias máquinas virtuales que ocuparán aún más espacio. Y por cierto, por el momento, la mayoría de los proveedores de servidores basados en la nube le cobrarán por ese espacio extra. Otro inconveniente significativo de la VM es un arranque lento.

Docker elimina todo lo anterior simplemente compartiendo el kernel del SO a través de todos los contenedores que se ejecutan como procesos separados del sistema operativo del host.

![](vm-contenedores.png)

Docker no es la primera ni la única plataforma de contenedorización. Sin embargo, en la actualidad, Docker es el mayor y más poderoso actor del mercado.

**Nota Bene**: El Instituto de Informática dispone de un servidor físico, dividido en máquinas virtuales. Utilizaremos una de esta máquina virtual para despliegar nuestros de contenedores Docker.

### 1.3 ¿Por qué se necesita a Docker?

La lista corta de beneficios incluye:

- **Proceso de desarrollo más rápido**

No hay necesidad de instalar aplicaciones de terceros como MySQL, Redis, Elasticsearch en el sistema - puede ejecutarlo en contenedores.

- **Práctica encapsulación de aplicaciones**

Usted puede entregar su arquitectura de software en una sola pieza. Docker ofrece un formato de imagen unificado para distribuir sus aplicaciones a través de diferentes sistemas host y servicios cloud. Puede entregar su aplicación en una sola pieza con todas las dependencias requeridas (incluidas en una imagen) listas para ser ejecutadas.


- **El mismo comportamiento en la máquina local / desarrollo / servidores de producción**

Reduce a casi cero la probabilidad de error causado por diferentes versiones de sistemas operativos, dependencias del sistema, etc.

Con el enfoque correcto para construir imágenes Docker, su aplicación utilizará la misma imagen base con la misma versión del sistema operativo y las dependencias necesarias.

- **Monitoreo fácil y claro**

Docker provee una manera unificada de leer los logs de todos los contenedores en ejecución. No necesita recordar todas las rutas específicas donde su aplicación y sus dependencias almacenan los archivos de logs.

- **Fácil de escalar**

Por diseño, Docker le obliga a seguir sus principios básicos, como la configuración sobre variables de entorno, la comunicación sobre puertos TCP/UDP, etc. Y si ha hecho bien su aplicación, estará lista para ser escalada y facilmente despliegable en cualquier servidor.

### 1.4 Plataformas soportadas

La plataforma nativa de Docker es Linux, ya que se basa en las características proporcionadas por el núcleo de Linux. Sin embargo, todavía puede ejecutarlo en macOS y Windows. La única diferencia es que en macOS y Windows, Docker está encapsulado en una pequeña máquina virtual. Por el momento, Docker para macOS y Windows ha alcanzado un nivel significativo de usabilidad y se siente más como una aplicación nativa.

### 1.5 Instalación

Puede consultar las instrucciones de instalación de Docker [aquí](https://docs.docker.com/install/).
Si está ejecutando Docker en Linux, necesita ejecutar todos los siguientes comandos como root o añadir su usuario al grupo de dockers y volver a iniciar sesión:

```
sudo usermod -aG docker username
```

**Nota Bene:** reemplazar username por su nombre de usuario

### 1.6 Terminología

**Imagen** - Una descripción estática de la arquitectura de software que se quiere despliegar.

**Contenedor** - una instancia en ejecución que encapsula la arquitectura de software funcionando. Los contenedores siempre se crean a partir de imágenes. Un contenedor puede exponer puertos y volúmenes para interactuar con otros contenedores o con el mundo exterior. Los contenedores pueden ser fácilmente eliminados / removidos y recreados de nuevo en muy poco tiempo.

**Port (Puerto)** - un puerto TCP/UDP en su significado original. Corresponden a direcciones que sirven de punto de integración entre varios softwares. Los puertos pueden estar expuestos al mundo exterior (accesible desde el sistema operativo del host) o conectados a otros contenedores, es decir, accesibles sólo desde esos contenedores e invisibles para el mundo exterior. 

**Volumen** - puede ser descrito como una carpeta compartida dónde se almacenan los datos útiles. Los volúmenes se inicializan cuando se crea un contenedor. Los volúmenes están diseñados para datos persistentes, independientemente del ciclo de vida del contenedor.

**Docker Hub** - un servidor con interfaz web proporcionada por Docker Inc. Almacena muchas imágenes Docker con diferentes programas. Docker Hub es una fuente de imágenes "oficiales" de Docker realizadas por el equipo Docker o en cooperación con el fabricante original del software (no significa necesariamente que estas imágenes "originales" procedan de fabricantes oficiales de software). Las imágenes oficiales enumeran sus vulnerabilidades potenciales.

## 2. Despliegar un primer contenedor Docker básico en práctica

### Ejemplo 1: Hello World

Ejecutemos nuestro primer contenedor Docker:

```
docker run ubuntu /bin/echo 'Hello world' 
```

Salida de la consola:

```
Unable to find image 'ubuntu:latest' locally  
latest: Pulling from library/ubuntu  
6b98dfc16071: Pull complete  
4001a1209541: Pull complete  
6319fc68c576: Pull complete  
b24603670dc3: Pull complete  
97f170c87c6f: Pull complete  
Digest:sha256:5f4bdc3467537cbbe563e80db2c3ec95d548a9145d64453b06939c4592d67b6d  
Status: Downloaded newer image for ubuntu:latest  
Hello world  
```

- **docker run** es una orden para ejecutar un contenedor.
- **ubuntu** es la imagen que se ejecuta. Por ejemplo, la imagen del sistema operativo Ubuntu. Al especificar una imagen, el Docker busca primero la imagen en el host del Docker. Si la imagen no existe localmente, entonces la imagen se extrae del registro de imagen pública - Docker Hub.
- **/bin/echo 'Hello world'** es el comando que se ejecutará dentro de un nuevo contenedor. Este contenedor simplemente imprime "Hello world" y detiene la ejecución.

Creamos un shell interactivo dentro de un contenedor Docker:

```
docker run -i -t --rm ubuntu  
```

- **-t** crea un terminal dentro del contenedor
- **-i** le permite interactuar directamente con el terminal del contenedor
- El indicador **-rm** retira automáticamente el contenedor cuando el proceso sale. Por defecto, los contenedores no se eliminan. Este contenedor existe hasta que mantenemos la sesión shell y termina cuando salimos de la sesión (como una sesión SSH con un servidor remoto).

Veamos qué contenedores tenemos en este momento:

```
docker ps -a
```

Salida de la consola:

```
CONTAINER ID  IMAGE   COMMAND                 CREATED             STATUS                         PORTS  NAMES  
c006f1a02edf  ubuntu  "/bin/echo 'Hello ..."  About a minute ago  Exited (0) About a minute ago         gifted_nobel  
```

- **docker ps** es un comando para listar contenedores.
- **-a** muestra todos los contenedores (sin -a la bandera ps sólo mostrará los contenedores en ejecución).

Para eliminar todos los contenedores, podemos usar el siguiente comando:
```
docker rm -f $(docker ps -aq)  
```

- **docker rm** es el comando para remover el contenedor.
- **-f** (para rm) detiene el contenedor si está en marcha (es decir, borrar por la fuerza).
- **-q** (para ps) es imprimir sólo los IDs del contenedor.

### Ejemplo 2: Variables de entorno y volumenes

Posicionarse en la carpeta **examples** del tutorial.

Es hora de crear y ejecutar un contenedor más relevante, como [Nginx](https://es.wikipedia.org/wiki/Nginx). NGinx es un servidor web de código abierto muy utilizado.

Cambiar el directorio a ejamples/nginx:


```
docker run -d --name "test-nginx" -p 8080:80 -v $(pwd):/usr/share/nginx/html:ro nginx:latest  
```

**Advertencia**: Este comando parece bastante pesado, pero es sólo un ejemplo para explicar volúmenes y variables env. En el 99% de los casos de la vida real, no iniciará los contenedores Docker manualmente, sino que utilizará servicios de orquestación (ilustraremos el uso de Docker-Compose en el ejemplo 4).

Salida de la consola:

```
Unable to find image 'nginx:latest' locally  
latest: Pulling from library/nginx  
683abbb4ea60: Pull complete  
a470862432e2: Pull complete  
977375e58a31: Pull complete  
Digest: sha256:a65beb8c90a08b22a9ff6a219c2f363e16c477b6d610da28fe9cba37c2c3a2ac  
Status: Downloaded newer image for nginx:latest  
afa095a8b81960241ee92ecb9aa689f78d201cff2469895674cec2c2acdcc61c 
```

-  **-p** es un mapeo de los puertos HOST PORT:CONTAINER PORT.
-  **-v** es un mapeo de los volumenes HOST DIRECTORY:CONTAINER DIRECTORY.

Importante: el comando sólo acepta rutas absolutas. En nuestro ejemplo, hemos usado $(pwd) para establecer la ruta absoluta del directorio actual.
Ahora compruebe esta url - 127.0.0.1:8080 en su navegador web.

Podemos intentar cambiar /ejemplo/nginx/index.html (que está montado como un volumen en el directorio /usr/share/nginx/html dentro del contenedor) y actualizar la página.

Obtengamos la información sobre el contenedor **test-nginx*:

```
docker inspect test-nginx  
```
  Este comando muestra información de todo el sistema sobre la instalación del Docker. Esta información incluye la versión del núcleo, el número de contenedores e imágenes, los puertos expuestos, los volúmenes montados, etc.

## 3. Crear sus propias imágenes con el archivo *Dockerfile*

### 3.1 ¿Qué es el archivo *Dockerfile*?

Dockerfile es un archivo de textos que sirve para crear sus propias imágenes, y así configurar el funcionamiento de sus propios softwares.

### 3.2 Ejemplo: Escribir un Dockerfile

Para crear una imagen Docker, debe crear un archivo **Dockerfile**. Es un archivo de texto plano con instrucciones y argumentos. Aquí está la descripción de las instrucciones que vamos a usar en nuestro próximo ejemplo:

**FROM** - establece la imagen base
**RUN** - ejecuta ciertos comandos al momento de construir la imágen
**ENV** - define variables de entorno
**WORKDIR** - define directorio de trabajo
**VOLUME** - crea un punto de montaje para un volumen
**CMD** - ejecuta ciertos comandos al momento de despliegar un contenedor

Puede consultar la referencia de [Dockerfile](https://docs.docker.com/engine/reference/builder/) para obtener más detalles.

Vamos a crear una imagen que obtendrá el contenido del sitio web con el comando __curl__ y lo almacenará en un archivo de texto. Necesitamos pasar la URL del sitio web a través de la variable de entorno SITE_URL. El archivo resultante se colocará en un directorio, montado como un volumen.

Coloque el nombre de archivo Dockerfile en el directorio de ejemplos/curl con el siguiente contenido:

```
FROM ubuntu:latest  
RUN apt-get update   
    && apt-get install --no-install-recommends --no-install-suggests -y curl 
    && rm -rf /var/lib/apt/lists/*
ENV SITE_URL http://example.com/  
WORKDIR /data  
VOLUME /data  
CMD sh -c "curl -Lk $SITE_URL > /data/results"  
```

El archivo Dockerfile está listo. Es hora de construir la imagen real.

Vaya al directorio examples/curl y ejecute el siguiente comando para construir una imagen:

```
docker build . -t test-curl  
```

Salida del terminal:

```
Sending build context to Docker daemon  3.584kB  
Step 1/6 : FROM ubuntu:latest  
 ---> 113a43faa138
Step 2/6 : RUN apt-get update     && apt-get install --no-install-recommends --no-install-suggests -y curl     && rm -rf /var/lib/apt/lists/*  
 ---> Running in ccc047efe3c7
Get:1 http://archive.ubuntu.com/ubuntu bionic InRelease [242 kB]  
Get:2 http://security.ubuntu.com/ubuntu bionic-security InRelease [83.2 kB]  
...
Removing intermediate container ccc047efe3c7  
 ---> 8d10d8dd4e2d
Step 3/6 : ENV SITE_URL http://example.com/  
 ---> Running in 7688364ef33f
Removing intermediate container 7688364ef33f  
 ---> c71f04bdf39d
Step 4/6 : WORKDIR /data  
Removing intermediate container 96b1b6817779  
 ---> 1ee38cca19a5
Step 5/6 : VOLUME /data  
 ---> Running in ce2c3f68dbbb
Removing intermediate container ce2c3f68dbbb  
 ---> f499e78756be
Step 6/6 : CMD sh -c "curl -Lk $SITE_URL > /data/results"  
 ---> Running in 834589c1ac03
Removing intermediate container 834589c1ac03  
 ---> 4b79e12b5c1d
Successfully built 4b79e12b5c1d  
Successfully tagged test-curl:latest  

```

- **docker build** construye una nueva imagen localmente.
- **-t** establece la etiqueta de nombre en una imagen.

Ahora tenemos la nueva imagen, y podemos verla en la lista de imágenes existentes:

```
docker images  
```

Salida del terminal:

```
REPOSITORY  TAG     IMAGE ID      CREATED         SIZE  
test-curl   latest  5ebb2a65d771  37 minutes ago  180 MB  
nginx       latest  6b914bbcb89e  7 days ago      182 MB  
ubuntu      latest  0ef2e08ed3fa  8 days ago      130 MB  
```

Podemos crear y ejecutar el contenedor desde la imagen. Vamos a intentarlo con los parámetros por defecto:


```
docker run --rm -v $(pwd)/vol:/data/:rw test-curl  
```

Para ver los resultados en el archivo:

```
cat ./vol/results  
```

Probemos definiendo la variable de entorno, tomando un sitio real como ejemplo (por ejemplo Facebook.com):

```
docker run --rm -e SITE_URL=https://facebook.com/ -v $(pwd)/vol:/data/:rw test-curl   
```

Ver los resultados:

```
cat ./vol/results  
```

**Nota bene**: 


 - Para suprimir una imágen específica:

 ```
docker rmi -f [nombre o ID de la imágen]
```

 - Para suprimir todas las imágenes:

 ```
docker rmi $(docker images -qa)
```



## 4. Combinar varias imágenes para construir software complejos con *Docker-compose*

**Docker compose** - es un software CLI utilizada para conectar contenedores entre sí.

Puede instalar docker-composite vía pip:
```
pip install docker-compose  
```

### 4.1 Ejemplo 1: Aplicación Python y Redis (Sistema de gestión base de datos)

En este ejemplo, vamos a crear una aplicación web en Python (utilizando la librería Flask) y el SGBD Redis.

La aplicación Python simplemente va a contar cuántas veces un usuario se conecta a una página web y actualizará un contador en una base de datos Redis.

 #### Etapa 1: crear la aplicación Python

Crear una carpeta llamada *compose* y posicionarse a dentro. En  *compose*, crear una carpeta *app*. Esta carpeta almacenará los archivos útiles para nuestra aplicación.

En un archivo app.py, crear la aplicación Flask: 
```
import os

from flask import Flask
from redis import Redis


app = Flask(__name__)
redis = Redis(host=os.environ['REDIS_HOST'], port=os.environ['REDIS_PORT'])
bind_port = int(os.environ['BIND_PORT'])


@app.route('/')
def hello():
    redis.incr('hits')
    total_hits = redis.get('hits').decode()
    return f'Hello from Redis! I have been seen {total_hits} times.'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=bind_port)
```
**Nota bene**: Nuestra aplicación tiene dos dependencias. Depende de las librerias Flask y Redis.

Creamos un archivo txt listando las dependencias de nuestra applicación.

En *app/requirements.txt*:
```
flask==1.0.2
redis==2.10.6
```

#### Etapa 2: Crear una imágen de nuestra aplicación Python

En la carpeta *app*, crear un archivo Dockerfile.

```
FROM python:3.6.3

ENV BIND_PORT 5000
ENV REDIS_HOST localhost
ENV REDIS_PORT 6379

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY ./app.py /app.py

EXPOSE $BIND_PORT

CMD [ "python", "/app.py" ]
```

### Etapa 3: Componer un software con Docker-compose

En una nueva carpeta llamada *compose* , creamos una archivo de configuración llamado **docker-compose.yml**. Tiene el contenido siguiente:
```
version: '3.6'  
services:  
  app:
    build:
      context: ./app
    depends_on:
      - redis
    environment:
      - REDIS_HOST=redis
    ports:
      - "3001:5000"
  redis:
    image: redis:3.2-alpine
    volumes:
      - redis_data:/data
volumes:  
  redis_data:
```

Vayan a examples/compose y ejecute el siguiente comando:

```
docker-compose up  
```

El ejemplo actual incrementará la vista del contador en Redis. Abra la dirección 127.0.0.1:3001 en su navegador web y compruébelo.

Siempre deben dar nombres explícitos a sus volúmenes en docker-compose.yml (si la imagen tiene volúmenes). Esta sencilla regla les ahorrará un problema en el futuro cuando inspeccionen sus volúmenes.

```
version: '3.6'  
services:  
  ...
  redis:
    image: redis:3.2-alpine
    volumes:
      - redis_data:/data
volumes:  
  redis_data:
```

En este caso, redis_data será el nombre dentro del archivo docker-compose.yml.

Para ver los volúmenes, ejecuten:
  
```
docker volume ls 
```

Salida del terminal:

```
DRIVER              VOLUME NAME  
local               apptest_redis_data   
```

#### Sobre Redis...

Redes es un SGBD no relacional ("*No SQL"*) que permite almacenar datos en un formato "key --> value". 

`` docker ps`` : para ver el ID del contenedor Redis
`` docker exec -it [ID] redis-cli``: para ejecutar el cliente redis-cli en el contenedor de Redis

una vez conectado a Redis:

``keys *``: para listar todas las claves almacenedas
`` GET Hits`` : para leer el valor de la clave "Hits"
`` SET Hits 500`` : para escribir un nuevo valor en la clave "Hits"

## 5. Conclusión del tutorial

- Docker se ha convertido en una herramienta importante de desarrollo de software
- Se puede utilizar en todo tipo de proyectos independientemente de su tamaño y complejidad
- **La encapsulación de su código en contenedores Docker le ayudará a crear procesos de integración más rápidos y eficientes**
- No hay persistencia de datos en los contenedores
- Eviten configuraciones manuales dentro de los contenedores. Deberian añadir comandos en el archivo de configuración Dockerfile.
- Pueden utilizar el comando ``docker exec`` para ejecutar comandos puntualment en un contenedor activo.

## 6. Preguntas

Algunas preguntas para autoevaluar su comprensión del tutorial:

1. ¿Cuál es la diferencia entre una Imágen Docker y un Contenedor Docker?
2. ¿Cuál es la diferencia entre el archivo Dockerfile y el archivo Docker-compose.yml?
3. ¿Si utilizo un contenedor que contiene una Base de Datos (Redis, Mysql u otro), cómo y dónde se guardan los datos?
4. ¿Qué es un *port*? ¿Por qué algunas imágenes requieren hacer un *bind* entre distintos puertos?

## 7. Ejercicio

A partir de la aplicación Python desarrollada la semana pasada ("JamesBot"):
1. Dockerizar la aplicación para poder despliegar fácilmente en cualquer máquina con el comando **docker run**
2. Modificar la aplicación "JamesBot". El bot debe ir a búscar de manera aleaoria una frase en una base de datos (MySQL, MariaDB, Mongo u cualquier otro SGBD de su elección) y la escribirá en un canal Slack cada vez que ejecuten su aplicación. (Necesitarán utilizar el comando **docker-compose up** para ejecutar su aplicación)

