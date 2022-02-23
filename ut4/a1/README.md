<center>

# UT4-A1: Implantación de Wordpress


</center>

***David Quintero Reeve:***
***ASIR:*** 2º de Ciclo Superior de Administración de Sistemas Informáticos en Red.

### ÍNDICE

+ [Introducción](#id1)
+ [Objetivos](#id2)
+ [Material empleado](#id3)
+ [Desarrollo](#id4)
+ [Conclusiones](#id5)


#### ***Introducción***. <a name="id1"></a>

En esta practica aprenderemos a realizar una instalación en un dominio wordpress y a confifigurar este mismo .

#### ***Objetivos***. <a name="id2"></a>

-> Realizar la instalación de Wordpress en el dominio wordpress.aluXXXX.me.
-> Instalar y activar un tema gratuito.
-> Ajustar los permalinks a Día y Nombre.
-> Escribir un post con las estadísticas de uso de Wordpress vistas en clase y entrar a dicho post.

#### ***Material empleado***. <a name="id3"></a>

- Maquina virtual azure
- Maquina virtual Ubuntu 20.04

*Ambas maquinas tendrán sus tarjetas de redes con sus respectivas ip estáticas*

#### ***Desarrollo***. <a name="id4"></a>

## Implantación de Wordpress

![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut4/a1/images/0.PNG)

* Para empezar usaremos el intérprete de MySQL para acceder a una base de datos.
* Creamos una base de datos, un usuario y le asignamos privilegios.

![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut4/a1/images/1.PNG)

* Descargamos el código fuente de Wordpress desde su página web.
* Ahora descomprimimos el código y lo copiamos en /usr/share

![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut4/a1/images/2.PNG)

* Establecemos los permisos necesarios para que el usuario web www-data pueda usar estos ficheros.


### Editar ficheros de Configuración

![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut4/a1/images/4.PNG)

Para una configuración básica de WordPress debemos especificar lo siguiente:

- El nombre de la base de datos.
- El usuario.
- La contraseña.

### Acceso mediante Nginx

![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut4/a1/images/5.PNG)

* Supongamos que queremos acceder a nuestro Wordpress desde una url cualquiera. Para ello tendremos que crear un nuevo virtual host de la siguiente manera

![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut4/a1/images/6.PNG)

* Enlazamos la configuración para que el virtual host esté disponible:


![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut4/a1/images/7.PNG)

* Elegimos Español (O el idioma deseado).

![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut4/a1/images/8.PNG)

* Rellenamos los campos que nos piden y pulsamos Instalar Wordpress.

![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut4/a1/images/9.PNG)


![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut4/a1/images/10.PNG)

* Accedemos con nuestras credenciales.

![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut4/a1/images/11.PNG)

* Nos dirigimos a Ajustes, en el panel a la izquierda, y seleccionamos Enlaces permanentes.
* Seleccionamos Día y nombre y guardamos los cambios.

### Ajustes de permalinks

![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut4/a1/images/12.PNG)

* Ahora indicamos a Nginx que enlace estas URLs:

![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut4/a1/images/13.PNG)



![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut4/a1/images/14.PNG)

>Editamos el fichero anstes de esta parte de manera que las lienas que contengas "upload_max_filesize = 64"
"post_max_size = 64" y "max_execution_time = 300"<

* A continuación reiniciamos el servicio php-fpm. Además, deberemos añadir una líneaen el fichero de configuración de Nginx.

### Sitio web seguro

![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut4/a1/images/15.PNG)

* Instalamos snap core para poder trabajar con certbot

![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut4/a1/images/16.PNG)

* Nos aseguramos de que certbot pueda correr en nuestra máquina con este comando.

![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut4/a1/images/17.PNG)

* Elegimos el sitio web que queremos que sea seguro y seleccionamos las otras opciones a nuestro gusto.

![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut4/a1/images/18.PNG)

* Hacemos un renew para comprobar que todo esta correcto.


![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut4/a1/images/20.PNG)

* Comprobamos

#### ***Conclusiones***. <a name="id5"></a>

La práctica me resultó sencilla a la hora de configurar, me gusto poder instalar certbot por fin.
