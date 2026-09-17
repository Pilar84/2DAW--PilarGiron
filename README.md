# Steamlike

Proyecto de gestión de biblioteca de videojuegos con Django + React + PostgreSQL + Redis.

## Descripción

Steamlike permite:
- gestionar una biblioteca personal de videojuegos
- explorar un catálogo
- buscar títulos y consultar precios
- gestionar la cuenta del usuario
- tener una base preparada para desplegar una demo pública o una versión de proyecto final

## Stack

- Backend: Django 5
- Frontend: React + Vite
- Base de datos: PostgreSQL
- Cache: Redis
- Contenedores: Docker + Docker Compose

## Estructura principal

- `Desarrollo_Web_Servidor/Steamlike/` : proyecto principal
- `Desarrollo_Web_Servidor/Steamlike/Steamlike-frontend/` : frontend React
- `Desarrollo_Web_Servidor/Steamlike/steamlike_backend/` : backend Django

## Requisitos

- Docker Desktop
- Docker Compose
- Git
- Navegador web

## Arranque local

Desde la carpeta del proyecto:

```bash
docker compose up --build -d
```

Si es la primera vez, aplica migraciones:

```bash
docker compose exec web python manage.py migrate
```

Crea un superusuario si quieres acceder al admin:

```bash
docker compose exec web python manage.py createsuperuser
```

## URLs locales

- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- Admin Django: http://localhost:8000/admin/

## Variables de entorno

En el proyecto existe un archivo `.env` con la configuración local. Para un entorno de producción, no debes reutilizar esos valores tal cual.

Ejemplo de variables relevantes:

```env
POSTGRES_DB=app_db
POSTGRES_USER=admin
POSTGRES_PASSWORD=tu_password_segura
POSTGRES_HOST=db
POSTGRES_PORT=5432
REDIS_HOST=redis
REDIS_PORT=6379
DJANGO_SECRET_KEY=clave_muy_segura
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,tu-dominio.com
DJANGO_CORS_ALLOWED_ORIGINS=http://localhost:3000,https://tu-dominio.com
DJANGO_CSRF_TRUSTED_ORIGINS=http://localhost:3000,https://tu-dominio.com
```

## Comandos útiles

### Ver logs
```bash
docker compose logs -f
```

### Ejecutar migraciones
```bash
docker compose exec web python manage.py migrate
```

### Crear usuario admin
```bash
docker compose exec web python manage.py createsuperuser
```

### Entrar al contenedor del backend
```bash
docker compose exec web bash
```

### Ejecutar tests
```bash
docker compose exec web python manage.py test
```

## Despliegue en IONOS

Sí se puede desplegar, pero no como una versión completamente lista sin ajustes. Para una demo pública o proyecto final en IONOS necesitas:

1. un servidor Linux con Docker y Docker Compose
2. dominio o subdominio apuntando al servidor
3. HTTPS con certificado SSL
4. ajustar variables de entorno para producción
5. configurar `ALLOWED_HOSTS`, CORS y CSRF para tu dominio real
6. usar un backend en producción (no `runserver` de Django para exterior)

### Recomendación mínima

- dejar el frontend en un build estático servido por Nginx
- mantener Django detrás con Gunicorn o equivalente
- usar PostgreSQL y Redis gestionados o instalados en el servidor
- activar HTTPS y poner el dominio correcto en variables de entorno

### Ajustes obligatorios para producción

En `steamlike_backend/settings.py` tienes que revisar:

- `ALLOWED_HOSTS`
- `CORS_ALLOWED_ORIGINS`
- `CSRF_TRUSTED_ORIGINS`
- `SESSION_COOKIE_SECURE`
- `CSRF_COOKIE_SECURE`
- `SECRET_KEY`
- `DEBUG`

Esto es importante porque una app publicando en internet no puede seguir funcionando como si estuviera en localhost.

## ¿Se puede poner en producción ya?

### Sí, para una demo pública con dominio y HTTPS
Si configuras correctamente el servidor, el dominio y las variables de entorno, sí se puede dejar visible para redes sociales y pruebas.

### No, como “listo para producción final” sin más
Todavía no está del todo preparado para una puesta en producción de nivel profesional sin revisar seguridad, dominio, certificados y configuración de servicios.

## Recomendación final

Para mostrar el proyecto en redes sociales, lo ideal es:
- ponerlo en un servidor de IONOS con dominio
- habilitar HTTPS
- dejarlo funcionando con entorno seguro y limpio
- preparar una captura de pantalla y una demo breve

## Licencia

Proyecto académico y de desarrollo personal.

## Nota

Este README está pensado para que cualquier persona pueda arrancar el proyecto y entender rápidamente el flujo de trabajo local y de despliegue.
