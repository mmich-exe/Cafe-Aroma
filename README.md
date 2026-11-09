Markdown# Café Aroma - Sistema de Gestión de Carta

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
Aplicar las migraciones de la base de datos:PowerShellpython manage.py makemigrations
python manage.py migrate
Crear un superusuario (opcional para el panel de administración):PowerShellpython manage.py createsuperuser
Ejecutar el servidor de desarrollo:PowerShellpython manage.py runserver
Acceder a la aplicación:Vista Pública / Carta: http://127.0.0.1:8000/Panel de Administración: http://127.0.0.1:8000/admin/📋 Documentación de Pruebas y VerificaciónRequisito / CriterioEstadoMétodo de VerificaciónMigraciones sin errores✅Ejecución exitosa de python manage.py migrate.Registro asociado a un tipo✅Formulario web con selector dinámico de categoría mediante ForeignKey.CRUD Web Completo✅Operaciones operativas desde la interfaz para listar, ver detalle, editar y eliminar.Persistencia en SQLite✅Almacenamiento local mediante el ORM de Django en db.sqlite3.Seguridad CSRF✅Inclusión de {% csrf_token %} en todas las peticiones POST.Confirmación de Eliminación✅Pantalla de advertencia previa con método POST obligatorio.Contador de Visitas✅Implementación activa mediante request.session reflejada en la interfaz.📁 Estructura del ProyectoPlaintextcafe_aroma/
│
├── carta/                    # Aplicación principal
│   ├── migrations/           # Archivos de migración de la BD
│   ├── static/carta/images/  # Recursos visuales (imágenes estáticas)
│   ├── templates/carta/      # Plantillas HTML (lista, detalle, crear, editar, eliminar)
│   ├── forms.py              # Formularios basados en ModelForm
│   ├── models.py             # Definición de modelos (Cafe, TipoCafe) y validadores
│   └── views.py              # Lógica de negocio, vistas y control de sesiones
│
├── cafe_aroma/               # Configuración del proyecto Django
│   ├── settings.py           # Ajustes globales y configuración estática
│   ├── urls.py               # Enrutador principal
│   └── wsgi.py / asgi.py     # Interfaces de despliegue
│
└── manage.py                 # Utilidad de línea de comandos de Django
