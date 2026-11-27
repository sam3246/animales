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
| DELETE | /usuarios