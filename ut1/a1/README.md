# Practica 1 creación de un dominio web en una maquina Ubuntu 20.04

## Configuración Nginx

### Paso 1: Configuramos nuestro dominio
* Para ello primero borraremos el archivo situado en /etc/nginx/sites-enabled/.
* sudo rm default.
* Luego mediante un editor de texto (nano,vi, ...) Creamos el archivo alua98c02009j.me situado en /etc/nginx/sites-available/alua98c02009j.me
![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a1/img/7creandopagina.png)
* Una vez hecho el punto anterior editamos el archivo he introducimos los parámetros de configuración.
 ![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a1/img/8creandopagina.png)
* hacemos un sudo Nginx -t para comprobar que todo anda bien.
![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a1/img/9creandopagina.png)
* Enlazamos el archivo con el comando de la imagen en sites-avaiable
![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a1/img/11creandopagina.png)
![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a1/img/10creandopagina.png)
* Recargamos el servicio.
* Debería funcionar.



## Pagina tirando
![]()
Comporbamos que la pagina conecta al dominio que hemos creado a travez de Nginx.
##
![]()
Imagen de la portada de nuestra web.

##
![]()
El lugar donde se supone que nos llevara los enlaces de las imágenes y titulos de las series.

##
![]()
Vemos que son enlaces dándole click derecho.

##
![]()
Un poco como hice mi html.

##
![]()
Lo que tenemos dentro de la carpeta series donde se encuentra nuestra página web.

##
![]()
Como queda finalmente la pagina web.
