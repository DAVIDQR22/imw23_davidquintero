# Practica 1 creación de un dominio web en una maquina Ubuntu 20.04

## Configuración Nginx

### Paso 1: Configuramos nuestro dominio
* Para ello primero borraremos el archivo situado en /etc/nginx/sites-enabled/.
* sudo rm default.
* Luego mediante un editor de texto (nano,vi, ...) Creamos el archivo
alua98c02009j.me situado en /etc/nginx/sites-available/alua98c02009j.me
* Una vez hecho el punto anterior editamos el archivo he introducimos los parámetros de configuración.
* hacemos un sudo Nginx -t para comprobar que todo anda bien.
* Enlazamos el archivo con el comando de la imagen en sites-avaiable
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
