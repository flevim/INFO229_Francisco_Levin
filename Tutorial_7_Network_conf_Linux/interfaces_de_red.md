## Configuración de redes en Linux
Dentro de este pequeño tutorial intentaré explicar a grandes rasgos herramientas de red que generalmente vienen por defecto en gran variedad de distribuciones de **Linux**. Estas facilitan el proceso de *crear*, *administrar* y *modificar* las redes en las cuales nos podríamos ver involucrados. 

### Gestión de interfaces de red 
Una interfaz de red es la forma en que el kernel vincula el lado del software de la red con el lado del hardware. Podemos observar las interfaces de red de nuestro equipo usando *ifconfig*
 
	 $ ifconfig      
 
 Podemos ver una salida como esta

![ifconfig](https://linux-console.net/common-images/ifconfig-vs-ip-command-comparing-network-configuration/Ifconfig-Command.png)

La herramienta **ifconfig** nos permite configurar nuestras interfaces de red, si no tenemos ninguna interfaz de red configurada, los controladores de dispositivos del kernel y la red no sabrán cómo comunicarse entre sí. Ifconfig se ejecuta en el arranque y configura nuestras interfaces a través de archivos de configuración, pero también podemos modificarlos manualmente. La salida de ifconfig muestra el nombre de la interfaz en el lado izquierdo y el lado derecho muestra información detallada. Comúnmente podemos ver interfaces con nombres tales como 
- eth0 (*Primera tarjeta ethernet en el equipo*)
- wlan0 (*Interfaz inalámbrica*)
- lo (*loopback: cuando la transmisión de datos al host destino somos nosotros mismos*).
 
 **Cambiar estado de las interfaces de red** 

> Para realizar modificaciones en las interfaces de red es nesesario tener privilegios **root**. 
 
 Las interfaces de red pueden estar tanto activas como inactivas y como puedes adivinar, esto puede administrarse mediante el mismo comando *ifconfig* 
 - Desactivar una interfaz de red (eth0):  
 
		$ ifconfig eth0 down 

Luego de ingresar el comando podemos ver que si vemos nuestras interfaces de red con ifconfig eth0 ya no está. Sin embargo, no es que la interfaz se haya eliminado del sistema, sino que ha sido "apagada". Esto puede verificarse ingresando `ifconfig -a` 

- Activar una interfaz de red (eth0): 

Luego de apagar la interfaz de red *eth0* pasaremos a activarla nuevamente, ingresando 

	 $ ifconfig eth0 up 

- **Cambiar dirección IP o MAC de nuestra interfaz**
Para cambiar la dirección IP de nuestra interfaz basta con ingresar 
  
	`ifconfig <interfaz> <nueva-direccion-ip>`

Luego si hacemos `ifconfig` nos mostrará la interfaz con una nueva dirección IP. 

Para cambiar nuestra dirección MAC es necesario apagar la interfaz y luego cambiarla de la forma 
  

    $ ifconfig <interfaz> down 
    $ ifconfig <interfaz> ether <direccion-MAC>
    $ ifconfig <interfaz> up


> Según la documentación de linux (`man ifconfig`)  se recomienda cambiar de `ifconfig a ip link ya que ifconfig se encuentra a los días de hoy, *obsoleto*.

**Comando ip**
Como mencionamos anteriormente, ifconfig se encuentra obsoleto y para reemplazar este nos encontramos con el comando `ip` que a grandes rasgos tiene una sintaxis de la forma

    ip [OPTION] OBJECT {COMMAND | help}

Si ingresamos `ip help` obtenemos ayuda sobre sus opciones

![ip help](https://phoenixnap.com/kb/wp-content/uploads/2019/08/ip-command-options.png)

Donde los objetos comunmente usados son: 
- link (Capa de red)
- route (ruteo)
- address (similar a ifconfig)

**Mostrar interfaces de red**

Al igual que con ifconfig podemos mostrar las interfaces de red 

    $ ip addr show

 **Activar/Desactivar interfaces de red** 

Para *activar* una interfaz de red 

    $ ip link set eth0 up

Y para desactivarla 

    $ ip link set eth0 down

**Ver información de enrutamiento** 

    $ ip route show 

donde la salida nos muestra algo como esto

    default via 192.168.1.254 dev wlan0 src 192.168.1.29 metric 303 
    192.168.1.0/24 dev wlan0 proto dhcp scope link src 192.168.1.29 metric 303 

**Información de la capa de red de los dispositivos**

    $ ip link show

**Obtener estadísticas de las interfaces de red**
Información relacionada con paquetes transferidos, descartados y posibles errores se pueden obtener de 

    $ ip -s link

O tambien para ver una interfaz específica 

    $ ip -s link ls [interface]


### ethtool
El comando **_ethtool_** (paquete _ethtool_) se utiliza para consultar y modificar los parámetros de las interfaces de red ethernet.

Para conocer información del *hardware* de una interfaz de red específica 

    ethtool -i <interfaz>

Y la salida será algo como esto 

    
    driver: _e1000_  
    version: 7.3.21-k8-NAPI  
    firmware-version: N/A  
    bus-info: 0000:00:03.0 
    supports-statistics: yes  
    supports-test: yes  
    supports-eeprom-access: yes  
    supports-register-dump: yes  
    supports-priv-flags: no

Para obtener estadísticas del tráfico de la tarjeta de red 

    $ ethtool -S <interfaz>

Y la salida sería algo como esto

    NIC statistics:  
     rx_packets: 2072  
     tx_packets: 278  
     rx_bytes: 743240  
     tx_bytes: 24123  
     rx_broadcast: 913  
     tx_broadcast: 21  
     rx_multicast: 879  
     tx_multicast: 65  
     rx_errors: 0  
     tx_errors: 0  
     tx_dropped: 0  
     multicast: 879  
     collisions: 0  
     ...


