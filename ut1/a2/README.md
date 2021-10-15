#Segundo sitio web NMginx
## Configuración Nginx

### Paso 1: Configuramos nuestro dominio
* Para ello primero borraremos el archivo situado en /etc/nginx/sites-enabled/.
* sudo rm default.
* Luego mediante un editor de texto (nano,vi, ...) Creamos el archivo alua98c02009jV2.me situado en /etc/nginx/sites-available/alua98c02009jV2.me
* Una vez hecho el punto anterior editamos el archivo he introducimos los parámetros de configuración.
 ![]()
* hacemos un sudo Nginx -t para comprobar que todo anda bien.
![]()
* Enlazamos el archivo con el comando de la imagen en sites-avaiable
![]()
* Recargamos el servicio.
* Debería funcionar.
