
## Monitoreo de redes en Linux

Existen muchas herramientas de monitoreo de red hoy en día, donde algunas se gestionan con GUI (Graphic User Interface) y otras en CLI (Command Line Interface). Sin embargo, las herramientas usadas en este tutorial son gestionadas desde la terminal. 

## ss 
El comando **ss** muestra información sobre los sockets del sistema. Si no se dan argumentos muestra los sockets TCP que tienen una conexión establecida actualmente

    $ ss | less
    
   ![ss](https://geekstuff.org/wp-content/uploads/2019/02/ss-1024x537.png)

Para ver solo los sockets TCP que están en escucha usamos 

    $ ss -ltn

**Listar todas las conexiones UDP**

    $ ss -ua

- -u : lista conexiones UDP
- -a : listar tanto sockets "Conectados" y "Escuchando"

**Listar sockets TCP rapidamente**

    $ ss -nt
- -n : Evita que se resuelvan direcciones IP a nombre de host
- -t : Lista todos los sockets TCP

**Mostrar PID de proceso y nombre de sockets**

    $ ss -ltp
> Si el comando anterior lo ingresamos como root nos mostrará más información de los sockets.


**Mostrar solo sockets IPv4 o IPv6**

Para mostrar solo conexiones IPv4 podemos usar la opción `-4 `y para IPv6 `-6`

    $ ss -tl -4 
O

	$ ss -tl -6

**Estadisticas de sockets del sistema**

    $ ss -s 

**Filtrar un puerto específico**

    ss -anp | grep 22 



**Filtrar sockets por estado TCP**

Sintaxis

    $ ss [OPTIONS] [STATE-FILTER] [ADDRESS-FILTER]

**Mostrar conexiones TCP IPv4 en estado "Conectado"**

    $ ss -t4 state established

**Filtrar con operadores** 

    { dport | sport } { eq | neq | gt | ge | lt | le } [IP]:puerto

**Filtrar sockets con puertos mayores a 1024**

     $ ss dport gt :1024

 
## iftop
*iftop* es una **herramienta de monitorización de ancho de banda** basada en consola que funciona en tiempo real.
Iftop viene haciendo para el uso de la red lo que hace top para el uso de la CPU.

Para empezar a usar iftop primero debemos instalar sus dependencias *libpcap* y *libncurse*.


	   $ sudo apt update
	   $ sudo apt install libpcap0.8 libpcap0.8-dev libncurses5 libncurses5-dev

> Para algunas distribuciones como Fedora o Cent OS las dependencias son  libpcap libpcap-devel ncurses ncurses-devel

Luego pasamos a instalar iftop 

Debian :

    $ sudo apt install iftop

Arch:

    $ sudo pacman -S iftop 

   
   > Para iniciar iftop son necesarios privilegios de **root**
   
   Podemos iniciar iftop sin argumentos, lo que nos mostrará nuestra el ancho de banda de la interfaz de red por defecto. Personalmente prefiero indicar la interfaz en la cual voy a monitorear 

Primero para saber que interfaz usar podemos usar el comando ip 

    ip addr show 
    
    $ sudo iftop -i <interfaz> 

Para obtener todas las opciones solo basta con ingresar 

    $ sudo iftop -h 

Para mostrar los puertos involucrados podemos iniciar iftop de la forma 

    $ sudo iftop -Pi <interfaz>
   
  Para mostrar el tráfico en bytes 
  

    $ sudo iftop -i <interfaz> -B

Para observar el flujo de paquetes de entrada y de salida podemos hacerlo con la opción `-F`

    $ sudo iftop -F 192.168.1.0/24 -i <interfaz> 
   
   

