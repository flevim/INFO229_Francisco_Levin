## Pelican: Generador de sitios estáticos

[Pelican](https://blog.getpelican.com/) es un generador de sitios estáticos escrito en Python, esto quiere decir que el contenido de la página se genera antes de tiempo, a demanda de lo que se necesite. Esto de por sí tiene tanto ventajas como desventajas como desventajas, de las cuales, podemos decir algunas:

**Ventajas**
-  *Portabilidad*, funcionan en cualquier servidor.
-  Tiempos de acceso **mínimos**, tardan muy poco en cargarse.
- Máyor rapidez de desarrollo.

**Desventajas**
- Ausencia de interacción y dinamismo con el usuario. 
- Absoluta opacidad a los deseos o búsquedas del visitante a la página.

Como podemos ver, tanto las ventajas como desventajas son factores determinantes al momento de pensar si un sitio estático es lo que estamos buscando. Sin embargo, para blogs y páginas webs pequeñas los sitios estáticos son perfectos para nosotros. 
Ya que explicamos a grandes rasgos lo que vamos a construir, pasemos a la práctica. 

### Instalación 
>**Pelican** actualmente funciona mejor con	**3.6+**; las versiones anteriores de Python no son compatibles.


**Pelican** puede instalarse de varias maneras, pero la más sencilla es a traves de [pip](https://pip.pypa.io/en/stable/):

    python -m pip install pelican
O si vas a utilizar Markdown para generar el sitio:

    python -m pip install "pelican[markdown]"


Antes de iniciar se recomienda estar en un entorno virtual de Python donde manejar la versión y nuevas dependencias que se puedan requerir. También si se encuentra en Linux, el proceso de instalación de dependencias con pip no requerirá permisos **root**.

    virtualenv ~/pelicanenv
    source ~/pelicanenv/bin/activate

Al momento de salir del entorno virtual basta con ingresar 

    deactivate
   
 Ahora creamos el	**esqueleto** del proyecto

    pelican-quickstart
  
  Esto creará el proyecto en el directorio actual, por lo que si necesitamos crear el proyecto en un directorio especifico podemos ingresar
  

    pelican-quickstart  --path  /mi/directorio/deseado

Al ingresar `pelican-quickstart ` se harán una serie de preguntas acerca de la configuración nuestro sitio (*titulo, timezone, paginación, nombre desarrollador, etc*), por lo que esto queda a la desición de cada uno. 

La estructura del proyecto quedará de la forma

    yourproject/
    ├── content
    │   └── (pages)
    ├── output
    ├── tasks.py
    ├── Makefile
    ├── pelicanconf.py       # Main settings file
    └── publishconf.py       # Settings to use when ready to publish

Ahora procederemos a agregar **contenido** a nuestro sitio
 
 ### Agregar contenido 

**Artículos y páginas**
*Pelican* considera que los "artículos" son contenido cronológico, como publicaciones en un blog y, por lo tanto, están asociados con una fecha.

La idea detrás de las "páginas" es que generalmente no son de naturaleza temporal y se utilizan para contenido que no cambia con mucha frecuencia (por ejemplo, páginas "Acerca de" o "Contacto").

**Crear un artículo**

Procedemos a agregar nuestro primer contenido a la carpeta de nuestro proyecto
 `
~/projects/yourproject/content/first-content.md
` 

    Title: My First Review
    Date: 2010-12-03 10:20
    Category: Review
    Arquitectura de Software es una bella asignatura gracias por tanto.

**Generar sitio**
Ahora que guardamos el contenido de nuestro artículo debemos situarnos en el directorio raíz de nuestro proyecto y lo generamos 

    pelican content
Ahora, si observamos la carpeta `output/` de nuestro proyecto podemos ver que nuestro sitio se ha generado (*es posible que vea una advertencia relacionada con los feeds, pero eso es normal cuando se desarrolla localmente y puede ignorarse por ahora*)

Ahora que nuestro sitio se ha generado podemos apreciar la vista de este ejecutando un servidor web local en el directorio raíz de nuestro proyecto  

    pelican --listen 

Podrá obtener la vista del sitio navegando a [http://localhost:8000/](http://localhost:8000/)

  Para ver la documentación completa de *Pelican* te	recomiendo visitar [aquí](https://docs.getpelican.com/en/latest/index.html).

**Pelican** proporciona una interfaz de desarrollo muy sencilla para desarrollar sitios web estáticos a la velocidad de la luz (no en el vacío por supuesto), Y si se tiene experiencia en Python  te será muy facil incrementar tu productividad. Exito!
