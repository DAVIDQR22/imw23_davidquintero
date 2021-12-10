# **UT1-A4: Sirviendo aplicaciones Php y Python**
En esta actividad nos dispondremos a configurar 2 sitios web (virtual hosts) en nuestro servidor web Nginx, con las siguiguientes características.

## Sitio web 1
Queremos que la URL de este sitio web sea `http://php.aluXXXX.me` y que en esa página se muestre la aplicación [demo_php.zip](https://github.com/sdelquin/claseando/blob/master/imw/UT1/assignments/assignment4/demo_php.zip).

Para empezar, crearemos en el directorio *webapps* la carpeta **php**.

![mkdirphp](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a4/images/1php.png)

Ahora, en `/etc/nginx/sites-available` crearemos el archivo que dará lugar a nuestro sitio web usando el camando **sudo nano php.aluXXXX.me**.

![sudonano](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a4/images/2php.png)

Y dentro escribiremos lo siguiente:

![nanophp](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a4/images/3php.png)

Guardamos el archivo y nos dirigimos a la carpeta **/etc/nginx/sites-enabled** para enlazar el archivo.

![sitesenabled](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a4/images/4php.png)

Volvemos a ir a la carpeta */webapps/php* y descargamos la demo nombrada al principio de la práctica: [demo_php.zip](https://github.com/sdelquin/claseando/blob/master/imw/UT1/assignments/assignment4/demo_php.zip).

La descomprimimos.
Comprobamos que se ha descomprimido correctamente y borramos el zip descargado.

![resultado1](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a4/images/5php.png)

Para comprobar el resultado de este primer sitio web, recargamos el servicio *Nginx* usando el comando `sudo reload Nginx` y deberemos dirigirnos a `php.aluXXXX.me`. Deberiamos ver esto:

![resultado1](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a4/images/6php.png)

## Sitio web 2

La URL de este segundo sitio web deberá ser `http://now.aluXXXX.me`

Al igual que al principio del siti web anterior, nos dirigiremos a la carpeta **webapps**
y dentro, crearemos otra llamada `now`.

![resultado1](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a4/images/7python.png)

Dentro de ella ejecutamos el comando **pipenv install**.

![pipenvins](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a4/images/8python.png)

A continuación, instalamos los paquetes `flask` y `pytz`.

![flask](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a4/images/9python.png)

![pytz](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a4/images/10python.png)

Ahora, en la misma carpeta en la que nos encontrsamos, creamos un fichero `main.py` e introducimos el siguiente código:

```bash
import datetime
import pytz
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    now = datetime.datetime.now(pytz.timezone("Atlantic/Canary"))
    return '''
    <h1>Testing Python over Nginx</h1>
    <h2>In Canary Islands...</h2>
    Today is: {today}
    <br>
    Now is: {now}
    '''.format(
        today=now.strftime('%d/%m/%Y'),
        now=now.strftime('%H:%Mh')
    )
```

![codigo](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a4/images/11python.png)

Para comprobar que lo hacho anteriormente funciona, ejecutaremos el siguiente comando:

![uwsgi](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a4/images/12python.png)

Ahora vamos a la carpeta `/etc/nginx/sites-available` y creamos el fichero que dará lugar al servidor **(sudo nano now.aluXXXX.me)**.

![nanoavail](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a4/images/13python.png)

Lo enlazamos en la carpeta `etc/nginx/sites-enabled`.

![enlace](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a4/images/14python.png)

Volvemos a ejecutar el comando *reload nginx* para que los cambios queden guardados.

![reload](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a4/images/15python.png)

Ahora vamos a crear un archivo de configuración del directorio **now** para el servicio `supervisor`.

![visuper](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a4/images/16python.png)

![visuper2](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a4/images/17python.png)

Reiniciamos el servicio *supervisor*:

![restartsuper](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a4/images/18python.png)

Luego, en la carpeta *now*, creamos un fichero que llamaremos **run.sh** en el que introduciremos lo siguiente:

![virun](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a4/images/19python.png)

![dentrovirun](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a4/images/20python.png)

Y le damos permisos de ejecución al fichero.

![chmod](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a4/images/21python.png)

Para comprobar los resultados finales, ejecutamos el comando `supervisorctl status` para asegurarnos de que está activo.

![statussuper](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a4/images/22python.png)


Podemos parar el servicio con `supervisorctl stop now`.

Por lo que la página, si intetamos acceder a la página, saldrá esto:

![resulstop](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a4/images/23python.png)

Y para finalizar, lo volvemos a iniciar (*supervisorctl restart now*).

![reinciamos](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a4/images/22-1python.png)

![result](https://github.com/DAVIDQR22/imw23_davidquintero/blob/main/ut1/a4/images/23-2python.png)
