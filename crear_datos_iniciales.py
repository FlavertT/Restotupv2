# Script para crear datos iniciales en RestoTup
from django.contrib.auth.models import User
from productos.models import CategoriaProducto, UnidadMedida, Producto
from personal.models import Empleado
from datetime import date

print("Creando categorías de productos...")
categorias = {
    'ingredientes': CategoriaProducto.objects.get_or_create(nombre='ingredientes')[0],
    'limpieza': CategoriaProducto.objects.get_or_create(nombre='limpieza')[0],
    'packaging': CategoriaProducto.objects.get_or_create(nombre='packaging')[0],
    'bebidas': CategoriaProducto.objects.get_or_create(nombre='bebidas')[0],
    'otros': CategoriaProducto.objects.get_or_create(nombre='otros')[0],
}
print(f"✓ Creadas {len(categorias)} categorías")

print("\nCreando unidades de medida...")
unidades = {
    'kg': UnidadMedida.objects.get_or_create(nombre='Kilogramos', abreviatura='kg')[0],
    'litros': UnidadMedida.objects.get_or_create(nombre='Litros', abreviatura='L')[0],
    'unidades': UnidadMedida.objects.get_or_create(nombre='Unidades', abreviatura='un')[0],
    'gramos': UnidadMedida.objects.get_or_create(nombre='Gramos', abreviatura='g')[0],
}
print(f"✓ Creadas {len(unidades)} unidades de medida")

print("\nCreando productos de ejemplo...")
productos_ejemplo = [
    {'nombre': 'Arroz', 'categoria': categorias['ingredientes'], 'unidad': unidades['kg'], 'stock': 50, 'minimo': 10, 'precio': 500},
    {'nombre': 'Pollo', 'categoria': categorias['ingredientes'], 'unidad': unidades['kg'], 'stock': 30, 'minimo': 5, 'precio': 800},
    {'nombre': 'Tomate', 'categoria': categorias['ingredientes'], 'unidad': unidades['kg'], 'stock': 20, 'minimo': 5, 'precio': 300},
    {'nombre': 'Aceite', 'categoria': categorias['ingredientes'], 'unidad': unidades['litros'], 'stock': 15, 'minimo': 3, 'precio': 1200},
    {'nombre': 'Sal', 'categoria': categorias['ingredientes'], 'unidad': unidades['kg'], 'stock': 10, 'minimo': 2, 'precio': 150},
    {'nombre': 'Detergente', 'categoria': categorias['limpieza'], 'unidad': unidades['litros'], 'stock': 8, 'minimo': 2, 'precio': 400},
    {'nombre': 'Envases plásticos', 'categoria': categorias['packaging'], 'unidad': unidades['unidades'], 'stock': 200, 'minimo': 50, 'precio': 50},
    {'nombre': 'Coca Cola', 'categoria': categorias['bebidas'], 'unidad': unidades['litros'], 'stock': 40, 'minimo': 10, 'precio': 600},
]

for p in productos_ejemplo:
    Producto.objects.get_or_create(
        nombre=p['nombre'],
        defaults={
            'categoria': p['categoria'],
            'unidad_medida': p['unidad'],
            'stock_actual': p['stock'],
            'stock_minimo': p['minimo'],
            'precio_unitario': p['precio']
        }
    )
print(f"✓ Creados {len(productos_ejemplo)} productos de ejemplo")

print("\nCreando empleados de ejemplo...")
empleados_ejemplo = [
    {'nombre': 'Juan', 'apellido': 'Pérez', 'rol': 'jefe', 'telefono': '1234567890', 'email': 'juan@restotup.com'},
    {'nombre': 'María', 'apellido': 'González', 'rol': 'encargado', 'telefono': '1234567891', 'email': 'maria@restotup.com'},
    {'nombre': 'Carlos', 'apellido': 'Rodríguez', 'rol': 'cocina', 'telefono': '1234567892', 'email': 'carlos@restotup.com'},
    {'nombre': 'Ana', 'apellido': 'Martínez', 'rol': 'mostrador', 'telefono': '1234567893', 'email': 'ana@restotup.com'},
]

for e in empleados_ejemplo:
    Empleado.objects.get_or_create(
        nombre=e['nombre'],
        apellido=e['apellido'],
        defaults={
            'rol': e['rol'],
            'telefono': e['telefono'],
            'email': e['email'],
            'fecha_ingreso': date.today()
        }
    )
print(f"✓ Creados {len(empleados_ejemplo)} empleados de ejemplo")

print("\n✅ Datos iniciales creados exitosamente!")
print("\nPuedes acceder al sistema con tu superusuario.")
print("Recuerda configurar las credenciales de Telegram en el archivo .env")
