 # Webapp

## Instalación y configuración

1. Crear entorno virtual: virtualenv -p /usr/bin/python3 venv

2. Activar entorno virtual: source venv/bin/activate

3. Instalar Flask: pip install flask

4. Instalamos los modulos de requeriments.txt: pip install -r requirements.txt 

5. Instalamos wtforms: pip install wtforms

6. Instalamos mysqlclient: pip install mysqlclient

7. Instalamos dotenv: pip install python-dotenv

8. Iniciamos la aplicación: python app.py

NOTA: Usar en Python3 para que se pueda escribir la ñ. Si se usa en python2 al intentar insertar un usuario que contenga la letra ñ se produccirá 
      un error que se soluciona entrando a la base de datos y eliminando la ñ. Mientras no se haga ese cambio la aplicación no funcionará.


## Funcionamiento de la aplicación

Esta aplicacion sirve para crear, editar y borrar  usuarios FTP.

En la página principal se ve una tabla con todos los usuarios. Cada fila de la tabla equivale a un usuario, de ese usuario se  muestran los siguientes campos:
    
* Usuario: este campo muestra el nombre del usuario.
    
* Contraseña: en ese campo se muestra la contraseña del usuario hasheada
    
* Icono editar: pinchando en el se puede editar la contraseña del usuario.

* Icono borrar: pinchando en el se elimina al usuario.


En la parte inferior derecha de la tabla se ve un botón con el simbolo "+". Este botón se usa para añadir un usuario. Al pinchar en él se muestra un popup por pantalla con un formulario que pide los siguientes datos:
    
* Usuario: nombre del nuevo usuario (en  caso de introduccir un usuario ya existente cuando se presione en el botón enviar se mostrará un mensaje de usuario duplicado)
    
* Clave: contraseña que se le desea asignar al usuario que se está creando

* Repita la clave: en este campo se tiene que poner la misma contraseña que se ha puesto en el campo anterior.

* Botón reset: pinchando en este botón se limpiaran los datos introduccidos en el formulario.

* Botón Insertar: este botón crea el usuario (Solo se mostrará si el campo "Clave" y el campo "Repita la clave" tienen el mismo valor.)


Pinchando en el icono editar se muestra un popup con un formulario para editar la contraseña del usuario. El formulario tiene los siguientes campos:
   
* Clave: contraseña que se le desea asignar al usuario
   
* Repita la clave: n este campo se tiene que poner la misma contraseña que se ha puesto en el campo anterior.
   
* Botón reset: pinchando en este botón se limpiaran los datos introduccidos en el formulario.
   
* Botón Ejecutar: al pinchar en este botón se modifica la contraseña del usuario(Solo se mostrará si el campo "Clave" y el campo "Repita la clave" tienen el mismo valor.)