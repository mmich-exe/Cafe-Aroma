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

## ⚙️ Instrucciones de Instalación y Ejecución

Sigue estos pasos en tu terminal (PowerShell o bash) para poner el proyecto en marcha:

1. **Clonar o abrir la carpeta del proyecto** donde se encuentra el archivo `manage.py`.
2. **Activar tu entorno virtual** (si aplica):
   ```powershell
   # Ejemplo en Windows
   venv\Scripts\Activate


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
