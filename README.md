# Bienvenido a Talana Kombat!

Kombat es un programa escrito en **Python** que recibe una esntructura JSON y la interpreta como instrucciones de pelea entre 2 combatientes.
Actualmente, el programa se puede ejecutar vía consola y vía Web, con el framework Django.

Para instalar/ejecutar este programa, cuentas con 2 opciones:
1. Clonar/Bajar este repositorio GIT
2. Ejecutar el contenedor Docker

## Clonar el Repositorio
`Para realizar la acción detallada en esta sección, es necesario tener instalado el cliente de GIT`

Para clonar este repositorio, diríjase desde la consola (terminal) a la ruta local de su equipo en donde desea almacenar la aplicación.
Una vez en la ruta, ejecute el siguiente comando:

>git clone https://github.com/jmsarmientopalma/talana_kombat.git

Alternativamente, tiene la opción de bajar manualmente el código comprimido, desde el botón verde **Code** seleccionando la opción **Download Zip**. Con esto obtendrá el código en un archivo comprimido y sólo deberá descomprimirlo en la ubicación deseada.


### Ejecución por consola (Terminal)

Una vez que ya tenga el repositorio localmente, acceda al directorio raíz y ejecute el siguiente comando para iniciar el programa:

>python3 main.py

Esto iniciará la aplicación. Lea las instrucciones, siga los pasos y disfrute de la pelea :)

*Nota: En algunos equipos, la instrucción para ejecutar archivos .py puede cambiar desde python3 a solamente python.*

`Nota2: Para la correcta ejecución del programa utilizando esta opción de ejecución, debe tener instalado Python 3.9+`


### Ejecución en Web

Una vez que ya tenga el repositorio localmente, acceda al directorio raíz y ejecute el siguiente comando para iniciar el programa:

>python3 manage.py runserver

Este comando iniciará un servidor HTTP básico en la máquina local, en la URL http://localhost:8000 a la que deberá acceder desde su navegador.
El flujo de ejecución en Web es similar al de terminal.

## Obtener vía Docker
`Para realizar la acción detallada en esta sección, es necesario tener instalado el software Docker.`

Desde la consola, ejecutar el siguiente comando:

>docker pull jmsarmiento/talana-kombat

Una vez obtenida la imagen, levantar la ejecución con salida por consola (no *silent* o en background).

>docker run -ti jmsarmiento/talana-kombat

Para acceder al repositorio en Docker Hub, diríjase a la siguiente URL:

[Docker Hub TalanaKombat](https://hub.docker.com/r/jmsarmiento/talana-kombat)


`Atención: La versión de Docker aún no cuenta con la ejecución en modalidad Web.`


## Archivo JSON de pelea
La estructura JSON que la aplicación cargará, será tomada de archivos alojados en el directorio **json/**. Lo ideal es situar en dicha ruta el o los archivos antes de ejecutar la aplicación.
La aplicación tomará un máximo de 10 archivos de la ruta indicada, de los cuales usted deberá elegir uno para ejecutar el *plan de pelea*.

La estructura del archivo JSON debe ser la siguiente:

`{
    "player1":{
        "movimientos":["D","DSD","S","DSD","SD"],
        "golpes":["K","P","","K","P"]
    },
    "player2":{
        "movimientos":["SA","SA","SA","ASA","SA"],
        "golpes":["K","","K","P","P"]
    }
}`

*Con ambos métodos de instalación, van incluídos archivos JSON de prueba.*

`IMPORTANTE: En caso de presentar errores en la ejecución (comúnmente EOFError) de la imagen obtenida, esto suele deberse a problemas de formato en la codificación y/o charset de la virtualización de Docker. Si presenta este problema, agradecería informarme y obtener la aplicación por medio de GIT para su correcta ejecución.`

## Desarrollo y Testing
Este programa ha sido desarrollado con **Python 3.9.2** en un equipo Pixelbook con **ChromeOS v108**.
La imagen de Docker ha sido creada en **Kubuntu 22.04**. 



## Nota sobre Rendimiento vía Web

La ejecución vía Web implementa **Streams HTTP** de Python y SSE de HTML5 para lograr el efecto de *relato*. Los Streams de Python están diseñados para ejecuciones cortas y baja concurrencia, ya que *toman* un worker del servidor hasta que el request es cerrado. Esto quiere decir que al ejecutar múltiples instancias de la aplicación al mismo tiempo, el rendimiento podría verse reducido.
Al ser esta aplicación una demo y no estar pensada para su uso en ambientes productivos, no se dió prioridad a los detalles de eficiencia ni se consideró la implementación de otras modalidades, como Channels o Async Views.