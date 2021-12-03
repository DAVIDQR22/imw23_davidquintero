# **UT1-A3: Trabajo con virtual hosts**

En esta actividad, vamos a configurar 4 sitios web (virtual hosts) en nuestro servidor web *nginx*.

## Sitio web 1

Para el primer sitio web lo primero quearemos sera crear la estructura de carpetas.

Crearemos un directorio *imw* dentro de la carpeta **webapps** y guardamos ahí la imagen.

![guarda](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a3/img/3sitioimw.png)

 Luego creamos el servidor editando el fichero */etc/nginx/sites-available/imw.aluXXXX.me* usando el comando **nano**.

 Creamos un index.html dentro de la carpeta */webapps/imw/* en el que pondremos la imagen para que se muestre correctamente.

 Ahora dentro de esta carpeta deberían estar la carpeta **img** y el **index.html**.

A continuación tenemos que enlazar el fichero que hemos creado para que esté disponible desde los **sites-enabled** como hemos hecho en las practicas anteriores.

Ahora, para comprobar que hemos realizado este apartado correctamnete, no tenemos que hacer más que abrir el navegador y buscar la URL "**imw.aluXXXX.me**". Si se ve el diagrama, hemos realizado este ejercicio con éxito.

![descarga imagen](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a3/img/2sitioimw.png)

>En caso de que no aparezca, ejecutar el comando "*sudo systemctl reload nginx*"

A continuación, vamos a hacer la segunda parte de este apartado, la cual consiste en mostrar una página con un enlace al Real decreto del título de Administración de Sistemas Informáticos en Red - MEC.

Primero nos dirigimos a la carpeta **webapps** y creamos la carpeta **mec**.

![carpetamec](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a3/img/3-3sitioimw.png)

Tras haberla creado, modificamos el archivo */etc/nginx/sites-available/imw.aluXXXX.me* para añadir la segunda parte de la dirección.

![locationmec](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a3/img/3-5sitioimw.png)

En la carpeta **mec** que creamos anteriormente, escribimos un fichero *index.html* usando el comando *nano* para añadir el enlace que nos lleve al archivo que pide el ejercicio.

![indexmec](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a3/img/3-4sitioimw.png)

Ejecutamos el comando sudo systemctl reload para reiniciar el servicio Nginx y se guarden los cambios.

Para comprobar que hemos finalizado este primer ejercicio, nos vamos a dirigir a la página *imw.aluXXXX.me/mec* haremos click sobre el único enlace que nos debe aparecer, y por último veremos el archivo del Real Decreto.

![pagina mec](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a3/img/2-2sitioimw.png)

## Sitio web 2

En este segundo ejercicio debemos Debe mostrar el listado de ficheros y directorios de /var/lib de nuestra máquina.

Primero crearemos el fichero */etc/nginx/sites-available/varlib.alua98c2009j.me* y escribimos lo siguiente:

![crearpagina](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a3/img/3-2sitiovarlib.png?raw=true)

>La línea "listen 9000;" es para que la página se pueda ver desde ese puerto.

Ahora crearemos la carpeta **varlib** en la carpeta **webapps**.

Enlazamos el fichero que creamos en el paso anterior desde */etc/nginx/sites-enabled* como hicimos en la practica anterior

Volvemos a recargar el servicio nginx para que se guarden los cabios con el comando "*sudo systemctl reload nginx*"

Comprobamos que la página *warlib.alua98c02009j.me:9000* enseña un index con un único enlace y que dentro de ese enlace, se pueden ver todos los ficheros de la carpeta.

![final1](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a3/img/3sitiovarlib.png?raw=true)

## Sitio web 3

En este ejercicio debemos mostrar una página web con el nombre de todo el alumnado de clase a través de la página *http://ssl.aluXXXX.me/students/* que crearemos a continuación.

Antes que nada, tenemos que crear el fichero que dará lugar al servidor en la carpeta */etc/nginx/sites-available/* al que llamaremos *ssl.aluXXXX.me*.

Creamos la carpeta **/webapps/students** y dentro de ella el **index.html** en el que pondremos la lista de todos los alumnos.

![carpetastudents](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a3/img/5sitiossl.png?raw=true)

Ahora vamos anlazar en la carpeta */etc/nginx/sites-enabled* como en los apartados anteriores.

Recargamos otra vez el servicio **nginx** si queremos comprobar que vamos bien encaminados.


A continuación, con estos dos comandos, crearemos una contraseña encriptada eligiendo una contraseña, en este caso "**2asir**" y una palabra clave par la encriptación "**2asir**". Luego ejecutaremos el segundo comando con un usuario a nuestra elección (**usuario1**) y poniendo la contraseña encriptada que nos ha dado el primer comando.

![contra](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a3/img/6sitiossl.png)

Tras haber hecho esto, para conseguir que la página nos pida el usuario y la contraseña, modificaremos el fichero */etc/nginx/sites-available/ssl.aluXXXX.me* añadiendo las siguientes líneas:

![completlocation](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a3/img/4sitiossl.png?raw=true)

A modo de comprobación buscaremos en el navegador la página **ssl.aluXXXX.me** y veremos que nos pide identificación.

![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a3/img/7sitiossl.png?raw=true)

Ahora vamos a restringir el acceso al archivo **.htpasswd**, que es donde se guardan las contraseñas.

Recargamos una vez más el servicio **nginx** para que los cambios se guarden y vemos que al dirigirnos a *ssl.aluXXXX.me/students/.htpasswd* nos manda a una página con un error, eso significa que hemos restringido el acceso a ese archivo correctamente.

![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a3/img/7-1sitiossl.png)

## Sitio web 4

Lo que nos pide este último ejrcicio es la  redirección cualquier petición del dominio http://redirect.aluXXXX.me al dominio http://target.aluXXXX.me.

Configuraremos los archivos y haremos sus respectivo enlaces, como hemos hecho en las practicas anteriores.

![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a3/img/8sitiosredirect.png?raw=true)

![image](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a3/img/10sitiostarget.png)

No olvidarnos de crear la carpetas.
![image](https://user-images.githubusercontent.com/71705577/144633494-f578a861-2a14-4a8a-b05d-b0d295de31fa.png)

Para target.alua98c02009j.me descargaremos el zip 'initializr-verekia-4.0.zip.' y lo estraemos en la carpeta de target.

![image](https://user-images.githubusercontent.com/71705577/144633690-038ed70d-24de-4d55-88a2-f853872da12d.png)

![image](https://user-images.githubusercontent.com/71705577/144633727-04b8f287-73b1-42db-b176-86dd62c5e9fc.png)



