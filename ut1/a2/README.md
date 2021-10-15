#Segundo sitio web NMginx
## Configuración Nginx

### Paso 1: Configuramos nuestro dominio
* Para ello primero borraremos el archivo situado en /etc/nginx/sites-enabled/.
* sudo rm default.
* Luego mediante un editor de texto (nano,vi, ...) Creamos el archivo alua98c02009jV2.me situado en /etc/nginx/sites-available/alua98c02009jV2.me
* Una vez hecho el punto anterior editamos el archivo he introducimos los parámetros de configuración.
 ![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a2/img/1configuracion.png)
* hacemos un sudo Nginx -t para comprobar que todo anda bien.
![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a2/img/2configuracion.png)
* Enlazamos el archivo con el comando de la imagen en sites-avaiable
![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a2/img/3configuracion.png)
* Recargamos el servicio.
* Debería funcionar.
![](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a2/img/4comprobacion.png)

