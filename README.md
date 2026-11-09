# Café Aroma - Sistema de Gestión de Carta

Aplicación web desarrollada en **Django** para la gestión de la carta de productos de la cafetería de especialidad **Café Aroma**. El proyecto cuenta con un diseño minimalista y elegante en tonos tierra y dorado, cumpliendo con los estándares de integridad de datos, seguridad y operaciones CRUD completas.

---

## 🚀 Características Principales

- **Gestión de Catálogo (CRUD Completo):** Creación, lectura de detalles, actualización y eliminación de cafés desde la interfaz web.
- **Búsqueda y Filtros Avanzados:** Filtrado dinámico por categoría (tipo de café), búsqueda por nombre/código y ordenamiento por precio (ascendente y descendente).
- **Integridad de Datos:** 
  - Restricciones estrictas en modelos (`models.PROTECT`) para evitar la eliminación de tipos de café con productos asociados.
  - Validadores numéricos (`MinValueValidator(0)`) para asegurar que los precios y el stock nunca sean negativos.
- **Seguridad:** Protección contra falsificación de solicitudes entre sitios (`CSRF`) en todos los formularios y confirmación obligatoria previa a la eliminación de registros.
- **Contador de Visitas por Sesión:** Sistema integrado mediante `request.session` para llevar el conteo de visitas del usuario a la carta.
- **Diseño UI/UX Minimalista:** Interfaz optimizada con Tailwind CSS y tipografías editoriales (`Playfair Display` y `Plus Jakarta Sans`) inspiradas en una estética de alta gama.

---

## 🛠️ Tecnologías Utilizadas

- **Backend:** Python / Django (versión reciente compatible con views, forms y ORM).
- **Base de Datos:** SQLite (motor relacional por defecto).
- **Frontend:** HTML5, Tailwind CSS (vía CDN) y diseño responsivo.

---

# Guía de Instalación y Ejecución - Café Aroma

Este documento contiene el paso a paso detallado para configurar el entorno, aplicar migraciones, crear usuarios administrativos y ejecutar el proyecto **Café Aroma** en un entorno local.

---

## 📋 Requisitos Previos

Antes de comenzar, asegúrate de contar con lo siguiente en tu sistema:
- **Python 3.10** o superior instalado.
- **pip** (administrador de paquetes de Python).
- Un editor de código (ej. Visual Studio Code) o consola de comandos (PowerShell / Terminal).

---

## ⚙️ Paso a Paso: Configuración del Proyecto

### 1. Clonar o Ubicar el Proyecto
Abre la consola de comandos y navega hasta la carpeta raíz del proyecto (donde se encuentra el archivo `manage.py`):

```powershell
cd ruta/a/tu/proyecto/cafe_aroma
```

### 2. Crear y Activar un Entorno Virtual *(Recomendado)*
Para aislar las dependencias del proyecto, crea un entorno virtual:

- **En Windows:**
  ```powershell
  python -m venv venv
  .\venv\Scripts\activate
  ```

- **En macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Instalar Django
Asegúrate de tener instalado Django en el entorno activo:

```powershell
pip install django
```

---

## 🗄️ Base de Datos y Migraciones

### 4. Generar y Aplicar Migraciones
Ejecuta las migraciones necesarias para crear la estructura de la base de datos en SQLite (`db.sqlite3`), incluyendo las restricciones de validación y modelos (`Cafe` y `TipoCafe`):

```powershell
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear Superusuario para el Administrador *(Opcional)*
Para ingresar al panel de administración de Django (`/admin/`) y gestionar los registros directamente:

```powershell
python manage.py createsuperuser
```
*(Ingresa un usuario, correo y contraseña cuando la consola te lo pida).*

---

## 🚀 Ejecución del Servidor

### 6. Iniciar el Servidor de Desarrollo
Ejecuta el siguiente comando para poner en marcha la aplicación web:

```powershell
python manage.py runserver
```

Una vez ejecutado, verás en la consola una confirmación como esta:
```text
System check identified no issues (0 silenced).
November 09, 2026 - 17:57:00
Django version 5.0, using settings 'cafe_aroma.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

---

## 🌐 Accesos Web

- **Carta Pública (CRUD y Filtros):** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Panel de Administración:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🛠️ Comandos de Verificación Rápida

| Acción | Comando |
| :--- | :--- |
| **Comprobar errores en el proyecto** | `python manage.py check` |
| **Ejecutar pruebas unitarias** | `python manage.py test` |
| **Detener el servidor web** | Presionar `Ctrl + C` en la terminal |


---

# Estructura del Proyecto Café Aroma

A continuación se detalla la organización de los archivos y directorios del proyecto, junto con la descripción de la responsabilidad de cada componente.

## 📂 Árbol de Directorios

```text
cafe_aroma/
│
├── cafe_aroma/               # Configuración global del proyecto Django
│   ├── __init__.py
│   ├── settings.py           # Ajustes de BD, apps, staticfiles y sesiones
│   ├── urls.py               # Enrutador principal de URLs
│   ├── asgi.py               # Configuración para servidores ASGI
│   └── wsgi.py               # Configuración para servidores WSGI
│
├── carta/                    # Aplicación principal del catálogo de cafés
│   ├── migrations/           # Historial de migraciones de la base de datos
│   │   └── __init__.py
│   ├── static/               # Recursos estáticos de la aplicación
│   │   └── carta/
│   │       └── images/       # Imágenes locales (ej. speciality-coffee-768x512.jpg)
│   ├── templates/            # Plantillas HTML con diseño Tailwind y dorado
│   │   └── carta/
│   │       ├── lista_carta.html    # Vista principal (tabla, filtros, banner y contador)
│   │       ├── detalle_cafe.html   # Vista detallada de un producto
│   │       ├── crear_cafe.html     # Formulario de registro de nuevo café
│   │       ├── editar_cafe.html    # Formulario de edicion de datos
│   │       └── eliminar_cafe.html  # Pantalla de confirmación de borrado
│   ├── __init__.py
│   ├── admin.py              # Registro y personalización del Panel de Administración
│   ├── apps.py               # Configuración de la app 'carta'
│   ├── forms.py              # Formulario CafeForm basado en ModelForm
│   ├── models.py             # Modelos Cafe y TipoCafe con validadores (MinValueValidator)
│   ├── tests.py              # Módulo de pruebas unitarias
│   ├── urls.py               # Rutas de la aplicación 'carta'
│   └── views.py              # Lógica del CRUD, filtrado, búsqueda y manejo de sesiones
│
├── db.sqlite3                # Base de datos relacional SQLite
├── manage.py                 # Script ejecutable de comandos de Django
└── README.md                 # Documentación general del proyecto
```

---

## 📊 Tabla Explicativa de la Estructura

| Componente / Ruta | Tipo | Descripción y Función Principal |
| :--- | :---: | :--- |
| `cafe_aroma/settings.py` | Configuración | Registra las aplicaciones (`carta`), los archivos estáticos (`STATICFILES_DIRS`), el motor SQLite y la gestión de sesiones. |
| `cafe_aroma/urls.py` | Enrutamiento | Enlaza la ruta raíz del sitio con las URLs pertenecientes a la app `carta`. |
| `carta/models.py` | Modelo de Datos | Define las entidades `TipoCafe` y `Cafe` con restricciones `models.PROTECT` y `MinValueValidator(0)` en precio y stock. |
| `carta/forms.py` | Formulario | Modela la entrada de datos para `Cafe` a través de `ModelForm` e integra widgets personalizados para la fecha. |
| `carta/views.py` | Lógica / Control | Procesa las solicitudes HTTP: CRUD completo, filtrado por categorías, búsqueda por nombre, ordenamiento por precio y el contador de visitas vía `request.session`. |
| `carta/urls.py` | Enrutamiento | Define las rutas amigables para la lista (`/`), detalle (`/cafe/<id>/`), creación (`/cafe/nuevo/`), edición y eliminación. |
| `carta/templates/carta/` | Vistas HTML | Contiene la interfaz gráfica estilizada con Tailwind CSS, paleta café/dorado, etiquetas `{% csrf_token %}` y contador de visitas. |
| `carta/static/carta/images/` | Estáticos | Almacena los recursos gráficos locales del catálogo. |
| `db.sqlite3` | Base de Datos | Archivo donde se persisten las categorías, productos e información del sistema. |
