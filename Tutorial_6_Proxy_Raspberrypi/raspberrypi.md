## Servidor Proxy Raspberry pi
En este tutorial te voy a mostrar como configurar un servidor proxy HTTP en tu raspberry pi usando [Privoxy](https://www.privoxy.org/). 
Privoxy es un proxy *web gratuito* y de *código abierto* sin almacenamiento en caché que puede filtrar y manipular los datos entrantes.

Para llevar a cabo nuestro servidor proxy necesitaremos ciertos requerimientos: 
- Raspberry pi 1, 2, 3 o 4  
- Tarjeta micro SD de almenos 16 GB con Raspbian instalado (*o al menos una distribución Debian*). 
- Fuente de alimentación
- Cable Ethernet o conexión Wifi (Raspberry 3 o 4).
- Configurar Raspberry pi con una [dirección IP estática](https://pimylifeup.com/raspberry-pi-static-ip-address/)
 
Este tutorial se llevará a cabo con [Raspbian Buster](https://largefiles.pimylifeup.com/raspbian/raspbian-desktop-lite/2020-05-27-raspios-buster-armhf.zip).
 
 **Instalación de Privoxy**
 1. Antes de instalar Privoxy en nuestra Raspberry pi necesitamos actualizar los paquetes de Raspbian
 `$ sudo apt update && sudo apt upgrade` 

2. Ahora podemos proceder a instalar Privoxy con el gestor de paquetes apt 
``$ sudo apt install privoxy ``

Luego de instalado *Privoxy* debemos configurar este para aceptar conexiones desde otros dispositivos locales. 

**Permitir conexiones desde dispositivos locales al servidor proxy**

Para poder aprovechar la funcionalidad de nuestro servidor proxy sería ideal aceptar conexiones locales desde *otros dispositivos*.
Por defecto, Privoxy está configurado para aceptar solo conexiones desde la computadora local (*there's no place like 127.0.0.1*). 

Para permitir conexiones externas debemos configurar su archivo de configuración

    $ sudo nano /etc/privoxy/config

Dentro de este archivo debemos encontrar un bloque de texto específico

    listen-address 127.0.0.1:8118  
    listen-address [::1]:8118
    
  Este bloque de texto nos dice que direcciones escuchará Privoxy, por lo que debemos reemplazar esto por algo que nos permita que cualquier dispositivo en la red local pueda conectarse al servidor proxy (*Debe tenerse en cuenta la seguridad de la red al realizar esto*). 
  
Debemos reemplazar el bloque de texto anterior con 
 

    listen-adress :8118
   Luego de esto guardamos nuestro archivo con `CTRL`+ `X` seguido de `Y ` y luego de `ENTER`.

Para que nuestros cambios surtan efecto en la Privoxy, debemos reiniciar el servicio 

    sudo systemctl restart privoxy


  Ahora para poder comprobar que nuetro servidor proxy está funcionando, es necesario configurar en su navegador preferido el proxy para que el tráfico pase a traves de este. 
  Dejaré links para agregar un servidor proxy en [Chrome](https://www.nettix.com.pe/documentacion/varios/como-configurar-un-proxy-en-mi-navegador-google-chromefirefoxinternet-explorer), [Firefox](https://support.mozilla.org/es/kb/ajustes-de-conexion-en-firefox) y [Safari](https://www.avast.com/es-es/c-how-to-set-up-a-proxy#:~:text=C%C3%B3mo%20se%20configura%20un%20servidor%20proxy%20en%20Safari,-Como%20sucede%20en&text=Haga%20clic%20en%20Safari%20en,clic%20en%20Cambiar%20ajustes...).
  
Cabe mencionar que la dirección IP  que debe agregarse en la configuración de proxy debe ser la dirección IP de su Raspberry y el puerto por defecto en el que Privoxy espera conexiones es `8118`.

Una vez terminada la configuración en su navegador para que apunte a nuestra Raspberry Pi, nos dirigiremos a  

    http://config.privoxy.org/

Si todo está funcionando correctamente podremos ver una página como esta 

![enter image description here](https://pi.lbbcdn.com/wp-content/uploads/2020/04/Raspberry-Pi-Proxy-Server-Successful-Connection.png)

Para una configuración personalizada del servidor proxy tales como bloqueador de anuncios, control de acceso y entre otros, revisar la [Documentación](https://www.privoxy.org/).
