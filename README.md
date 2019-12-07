# Proyecto de grado
## Prototipo funcional de una plataforma digital para aumentar la representatividad de los datos de percepciones de paz en la ciudad de Cali, en la zona norte del Cauca y sur del Valle del Cauca 

## Integrantes
- Sandra Niño
- Johnatan Garzón

## Backend

Para instalar el servidor backend desarrollado en Django se tiene que realizar lo siguiente:

1. Crear un ambiente virtual para el proyecto usando virtualenv:

```bash
sudo pip install virtualenv
```

Activar el ambiente virtual:

```bash
source myvenv/bin/activate
```

2. Luego de activar el ambiente virtual, se deben instalar las dependencias de python 3.6:
```bash
pip install -R requirements.txt
```

**Nota:** Para el modelo de analítica de datos se requiere instalar una dependencia extra que pertenece a spacy:
- opción 1:
 ```bash 
 spacy download es_core_news_sm
 ```
- opción 2: 

```bash
python -m spacy download es_core_news_sm
```

3. Crear la base de datos y el usuario a utilizar:

```SQL
CREATE DATABASE OPC_DB;
CREATE USER U_OPC WITH PASSWORD OPC_PASSWD;
ALTER ROLE U_OPC SET client_encoding TO 'utf8';
ALTER ROLE U_OPC SET default_transaction_isolation TO 'read committed';
ALTER ROLE U_OPC SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE OPC_DB TO U_OPC;
```

**Nota:** Para poder ejecutar las pruebas unitarias se necesita que el usuario, en este caso *U_OPC*, tenga permiso para crear una base de datos que es usada para realizar dichas pruebas:
```SQL
ALTER USER U_OPC CREATEDB;
```

4. Exportar las variables de entorno:
```bash
export OPC_USER=U_OPC
export OPC_PASS=OPC_PASSWD
export OPC_HOST=#.#.#.#
export DB_NAME=OPC_DB
```

5. Realizar las migraciones del modelo:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Correr los scripts en la base de datos postgresql, dichos scripts permitirán la creación de:
- Los conceptos de los tópicos que se obtuvo del modelo de análitica de datos.
- Generos
- Zonas
- Roles de usuario
- Titulo educativo más alto alcanzado
- Nivel alcanzado en el título educativo
- País
- Departamentos
- Municipios o Comunas
- Barrios o Veredas

**Nota:** Este script se encuentra en *scripts/newEnv1.sql*

7. Crear una persona proyectista, esto incluye crearlo como *user* y como *person*.

**Nota:** Un ejemplo de la creación del usuario mencionado en el paso 7. se encuentra en *scripts/newEnv1.1.sql*.


8. Crear una campaña asociada a la persona que se agregó en el paso anterior

**Nota:** Un ejemplo de este script se encuentra en *scripts/newEnv1.2.sql*




### Ejecutar la aplicación:

```bash
python manage.py runserver #.#.#.#:port
```
**Nota:** si se desea ver la documentación realizada en *OpenAPI*, la variable **debug** debe estar en **true**, en el archivo *opc/settings.py*.

## Frontend

Para instalar el servidor frontend desarrollado en Vue.js se tiene que realizar lo siguiente:

1. Ejecutar el siguiente comando:
```bash
npm install
```
### Ejecutar la aplicación
- Si se desea ejecutar el servidor de desarrollo puede ejecutar el siguiente comando:
```bash
npm run serve
```

**Nota:** Si se desea cambiar la ruta de conexión con el api, debe cambiar la variable **baseUrl** que se encuentra en el archivo *src/configaxios.js*

- Por otro lado, si se desea tener la versión de producción se realiza lo siguiente:
```bash
npm run build
```
Este comando crea una carpeta llamada dist, la cual es la que puede ser expuesta por un servidor como nginx.




