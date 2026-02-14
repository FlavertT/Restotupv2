# RestoTup - Sistema de Gestión para Restaurante

Sistema completo de gestión para restaurante de viandas desarrollado con Django.

## Características

- 📦 **Gestión de Productos**: Control de stock con alertas automáticas
- 👥 **Gestión de Clientes**: Minoristas y empresas
- 📖 **Recetas**: Gestión de recetas con ingredientes y costos
- 👔 **Personal**: Gestión de empleados por roles
- 🛒 **Pedidos**: Sistema completo de pedidos con deducción automática de stock
- 📊 **Reportes**: Análisis mensual de productos más utilizados
- 📱 **Telegram**: Notificaciones automáticas de stock bajo

## Instalación

### 1. Crear entorno virtual

```bash
python -m venv venv
```

### 2. Activar entorno virtual

**Windows:**
```bash
.\venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Copia el archivo `.env.example` a `.env` y configura tus credenciales de Telegram:

```bash
copy .env.example .env
```

Edita `.env` y agrega:
- `TELEGRAM_BOT_TOKEN`: Token de tu bot (obtén uno con @BotFather)
- `TELEGRAM_CHAT_ID`: ID de tu chat (obtén uno con @userinfobot)

### 5. Ejecutar migraciones

```bash
python manage.py migrate
```

### 6. Crear superusuario

```bash
python manage.py createsuperuser
```

### 7. Crear datos iniciales (opcional)

```bash
python manage.py shell < crear_datos_iniciales.py
```

### 8. Ejecutar servidor

```bash
python manage.py runserver
```

Accede a: `http://localhost:8000`

## Uso

### Panel de Administración

Accede a `http://localhost:8000/admin` con tu superusuario para gestionar:
- Categorías de productos
- Unidades de medida
- Productos iniciales
- Empleados
- Clientes

### Dashboard Principal

El dashboard muestra:
- Pedidos del día
- Productos con stock bajo
- Total vendido
- Pedidos pendientes

### Flujo de Trabajo

1. **Configurar productos**: Agregar categorías, unidades y productos
2. **Crear recetas**: Definir recetas con sus ingredientes
3. **Registrar clientes**: Minoristas o empresas
4. **Crear pedidos**: Seleccionar cliente, agregar items (recetas)
5. **Completar pedido**: El stock se deduce automáticamente
6. **Ver reportes**: Analizar productos más utilizados por mes

### Notificaciones de Telegram

Cuando un producto alcanza el stock mínimo, recibirás una alerta automática en Telegram con:
- Nombre del producto
- Stock actual
- Stock mínimo
- Categoría

## Estructura del Proyecto

```
restotup/
├── clientes/          # App de gestión de clientes
├── productos/         # App de gestión de productos
├── recetas/           # App de gestión de recetas
├── personal/          # App de gestión de empleados
├── pedidos/           # App de gestión de pedidos
├── templates/         # Templates HTML
├── static/            # Archivos estáticos
├── restotup/          # Configuración del proyecto
└── manage.py          # Script de gestión de Django
```

## Tecnologías

- **Backend**: Django 4.2
- **Base de Datos**: SQLite (desarrollo)
- **Notificaciones**: python-telegram-bot
- **Frontend**: HTML, CSS (diseño moderno con gradientes)

## Soporte

Para problemas o preguntas, contacta al equipo de desarrollo.
