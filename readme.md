# DOCUMENTACIÓN DEL PROYECTO – ANIMAL API

## 1. Nombre y descripción del proyecto

**Nombre: Animal API**

Animal API es un proyecto desarrollado en Python que permite administrar información de animales y usuarios. Por medio de esta API se pueden registrar, consultar, actualizar y eliminar datos.

Para su desarrollo se utilizaron FastAPI, SQLAlchemy y PostgreSQL, con la intención de trabajar con una base de datos alojada en Neon y realizar el despliegue mediante Render.

## 2. Objetivo de la API

El objetivo de Animal API es facilitar la administración de animales y usuarios mediante diferentes solicitudes HTTP.

La API permite realizar operaciones CRUD, consultar registros por su identificador y filtrar animales según su especie. También cuenta con validaciones para evitar algunos registros duplicados y datos incorrectos.

## 3. Descripción de los módulos desarrollados

El proyecto está dividido en varios módulos para mantener el código organizado:

- **main.py:** Es el archivo principal. Aquí se inicia FastAPI y se conectan las rutas de animales y usuarios.
- **routers:** Contiene las rutas y funciones que permiten realizar las operaciones CRUD.
- **models:** Define la estructura de las tablas de la base de datos.
- **schemas:** Se encarga de validar los datos que recibe y devuelve la API.
- **database:** Contiene la configuración necesaria para conectarse a la base de datos.
- **requirements.txt:** Contiene las librerías necesarias para ejecutar el proyecto.

## 4. Diagrama de arquitectura por capas

El proyecto está organizado por capas, de manera que cada una cumple una función específica.

**Organización del proyecto:**

```text
animales/
│
├── main.py
│
├── database/
│   └── conexion.py
│
├── models/
│   ├── animal.py
│   └── user.py
│
├── schemas/
│   ├── animal.py
│   └── user.py
│
├── routers/
│   ├── animales.py
│   └── usuarios.py
│
└── requirements.txt
```

**Diagrama de arquitectura:**

```text
       CLIENTE / SWAGGER
               |
               v
       CAPA DE PRESENTACIÓN
             main.py
               |
               v
        CAPA DE RUTAS
             routers
               |
          +----+----+
          |         |
          v         v
       schemas    models
       (Validación) (Estructura)
          |         |
          +----+----+
               |
               v
       CAPA DE CONEXIÓN
       database/conexion.py
               |
               v
          NEON / POSTGRESQL
```

## 5. Responsabilidad de cada capa

- **Presentación:** Permite iniciar la API y recibir solicitudes mediante FastAPI.
- **Rutas:** Procesa las solicitudes y ejecuta las operaciones de animales y usuarios.
- **Validación:** Comprueba que los datos enviados tengan el formato correcto.
- **Modelos:** Define cómo se organizan los datos dentro de las tablas.
- **Conexión:** Se encarga de establecer la comunicación con la base de datos.
- **Almacenamiento:** Guarda la información de los animales y usuarios en PostgreSQL.

## 6. Diagrama de las tablas de la base de datos

La base de datos cuenta con dos tablas principales: `animales` y `usuarios`.

```text
ANIMALES
-------------------
id (PK)
name
especie
raza
fecha_nacimiento
propietario


USUARIOS
-------------------
id (PK)
nombre
email (UNIQUE)
password
activo
```

Las dos tablas funcionan de manera independiente y no tienen una relación mediante claves foráneas.

## 7. Descripción de los campos de cada tabla

**Tabla animales**

- `id`: Identificador único del animal.
- `name`: Nombre del animal.
- `especie`: Especie a la que pertenece.
- `raza`: Raza del animal.
- `fecha_nacimiento`: Fecha de nacimiento.
- `propietario`: Nombre del propietario.

**Tabla usuarios**

- `id`: Identificador único del usuario.
- `nombre`: Nombre del usuario.
- `email`: Correo electrónico, debe ser único.
- `password`: Contraseña del usuario.
- `activo`: Indica si el usuario está activo o no.

## 8. Listado de endpoints implementados

La API cuenta con 11 endpoints que permiten administrar la información.

**Módulo de animales**

| Método | Endpoint | Función |
|---|---|---|
| GET | /animales | Consultar todos |
| GET | /animales/{animal_id} | Consultar por ID |
| GET | /animales/especie/{especie} | Filtrar por especie |
| POST | /animales | Registrar |
| PUT | /animales/{animal_id} | Actualizar |
| DELETE | /animales/{animal_id} | Eliminar |

**Módulo de usuarios**

| Método | Endpoint | Función |
|---|---|---|
| GET | /usuarios | Consultar todos |
| GET | /usuarios/{user_id} | Consultar por ID |
| POST | /usuarios | Registrar |
| PUT | /usuarios/{user_id} | Actualizar |
| DELETE | /usuarios/{user_id} | Eliminar |

## 9. Evidencias de pruebas en Swagger

Para comprobar el funcionamiento de la API se utiliza Swagger, una herramienta que permite probar los endpoints desde el navegador.

La documentación se puede consultar en:

`http://127.0.0.1:8000/docs`

Algunas pruebas que se deben realizar son:

- Consultar los animales registrados.
- Registrar un nuevo animal.
- Buscar un animal por su ID.
- Filtrar animales por especie.
- Actualizar y eliminar registros.
- Realizar las mismas operaciones con los usuarios.

**Evidencias:** Se deben agregar capturas de Swagger mostrando las solicitudes y sus respuestas.

## 10. Explicación de la conexión con Neon

Para almacenar la información se utiliza PostgreSQL mediante Neon, un servicio que permite tener una base de datos en la nube.

La conexión se realiza utilizando SQLAlchemy y Psycopg. En el archivo `database/conexion.py` se configura el motor de conexión y se utiliza la variable de entorno `DATABASE_URL` para obtener la dirección de la base de datos.

De esta manera, la API puede comunicarse con Neon para guardar, consultar, actualizar y eliminar información.

El proyecto también tiene SQLite como alternativa cuando no se encuentra configurada la variable de conexión.

## 11. Evidencia del despliegue en Render

Render es la plataforma utilizada para intentar publicar la API y permitir que pueda funcionar desde internet.

Para realizar el despliegue se conecta el repositorio de GitHub y se configuran los siguientes comandos:

**Build Command:**

```bash
pip install -r requirements.txt
```

**Start Command:**

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

En el registro de Render se observa que las dependencias se instalaron correctamente, pero apareció un error al importar el módulo `app`.

Por esta razón, todavía es necesario corregir ese problema para que el servicio pueda iniciar correctamente.

Se deben agregar capturas del despliegue y de la API funcionando cuando se solucione el error.

## 12. Enlace al repositorio GitHub

El código fuente del proyecto se encuentra en GitHub, donde se pueden consultar los archivos y las diferentes carpetas que lo componen.

**Enlace:** https://github.com/sam3246/animales

## Conclusión

Con este proyecto pude poner en práctica el desarrollo de API utilizando Python y FastAPI. También trabajé con operaciones CRUD, validación de datos, organización por capas y conexión con bases de datos.

Además, aprendí a utilizar herramientas como Swagger, Neon, GitHub y Render, que permiten probar, almacenar y publicar una aplicación.