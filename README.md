# Django CRUD Inventario - Deployment Guide

Este proyecto es una aplicación CRUD de inventario desarrollada con Django, preparada para despliegue en producción en Render.

## Estructura del Proyecto

- `inventario/` - Aplicación principal con modelos, vistas y templates
- `negocio/` - Configuración del proyecto Django
- `requirements.txt` - Dependencias del proyecto
- `build.sh` - Script de construcción para Render
- `render.yaml` - Configuración de despliegue para Render
- `Procfile` - Configuración alternativa de proceso

## Configuración para Producción

### Archivos Creados para Producción

1. **requirements.txt** - Dependencias necesarias incluyendo:
   - Django 4.2.3
   - psycopg2-binary (PostgreSQL)
   - gunicorn (servidor WSGI)
   - whitenoise (archivos estáticos)
   - python-decouple (variables de entorno)
   - dj-database-url (configuración de BD)

2. **settings_production.py** - Configuración específica para producción con:
   - Variables de entorno para configuración sensible
   - Configuración de PostgreSQL
   - Configuración de archivos estáticos con WhiteNoise
   - Configuraciones de seguridad

3. **build.sh** - Script que ejecuta Render para construir la aplicación

4. **.env.example** - Ejemplo de variables de entorno necesarias

## Despliegue en Render

### Opción 1: Usando render.yaml (Recomendado)

1. Conecta tu repositorio de GitHub a Render
2. Render detectará automáticamente el archivo `render.yaml`
3. Las variables de entorno se configurarán automáticamente

### Opción 2: Configuración Manual

1. **Crear Web Service en Render:**
   - Environment: Python 3
   - Build Command: `./build.sh`
   - Start Command: `gunicorn negocio.wsgi:application`

2. **Crear PostgreSQL Database:**
   - Crea una base de datos PostgreSQL en Render
   - Copia la URL de conexión

3. **Configurar Variables de Entorno:**
   ```
   DJANGO_SETTINGS_MODULE=negocio.settings_production
   DATABASE_URL=<tu-url-de-postgresql>
   SECRET_KEY=<genera-una-clave-secreta-segura>
   DEBUG=False
   ALLOWED_HOSTS=<tu-app>.onrender.com
   ```

### Variables de Entorno Requeridas

- `SECRET_KEY`: Clave secreta de Django (genera una nueva para producción)
- `DEBUG`: Debe ser `False` en producción
- `ALLOWED_HOSTS`: Dominio de tu aplicación en Render
- `DATABASE_URL`: URL de conexión a PostgreSQL
- `DJANGO_SETTINGS_MODULE`: `negocio.settings_production`

## Características de Producción Implementadas

✅ **Configuración de Base de Datos**: PostgreSQL para producción
✅ **Archivos Estáticos**: Configurados con WhiteNoise
✅ **Variables de Entorno**: Configuración segura con python-decouple
✅ **Servidor WSGI**: Gunicorn para servir la aplicación
✅ **Configuraciones de Seguridad**: Headers de seguridad habilitados
✅ **Logging**: Configuración de logs para producción
✅ **Build Script**: Automatización del proceso de despliegue

## Comandos Útiles

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar migraciones
python manage.py migrate

# Recopilar archivos estáticos
python manage.py collectstatic

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor de desarrollo
python manage.py runserver

# Ejecutar con configuración de producción localmente
DJANGO_SETTINGS_MODULE=negocio.settings_production python manage.py runserver
```

## Notas Importantes

1. **Nunca** commits tu archivo `.env` con credenciales reales
2. Genera una nueva `SECRET_KEY` para producción
3. Asegúrate de que `DEBUG=False` en producción
4. Configura correctamente `ALLOWED_HOSTS` con tu dominio de Render
5. La base de datos SQLite se usa solo para desarrollo

## Estructura de Archivos Estáticos

Los archivos estáticos se sirven usando WhiteNoise:
- `STATIC_URL = '/static/'`
- `STATIC_ROOT = 'staticfiles/'`

## Soporte

Si encuentras algún problema durante el despliegue, verifica:
1. Que todas las variables de entorno estén configuradas
2. Que la base de datos PostgreSQL esté conectada
3. Que el build script se ejecute sin errores
4. Los logs de la aplicación en el dashboard de Render
