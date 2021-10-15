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
![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a1/img/1enlace.png)
Comporbamos que la pagina conecta al dominio que hemos creado a travez de Nginx.
##
![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a1/img/2portadas.png)
Imagen de la portada de nuestra web.

##

![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a1/img/3-2enlaces.png)
El lugar donde se supone que nos llevara los enlaces de las imágenes y titulos de las series.

##
![](![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a1/img/3enlaces.png))
Vemos que son enlaces dándole click derecho.

##
![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a1/img/4nano.png)
Un poco como hice mi html.

##
![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a1/img/5ubicatex.png)
Lo que tenemos dentro de la carpeta series donde se encuentra nuestra página web.

##
![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a1/img/6pagina.png)
Como queda finalmente la pagina web.
