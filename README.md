# CRM Shop – Inventario y facturación

Aplicación de escritorio en **Python** para que un pequeño comercio controle su inventario, registre ventas mediante facturas y consulte reportes gráficos de ventas. Interfaz gráfica con **Tkinter** y base de datos **MySQL**.

> **Estado:** proyecto de aprendizaje (2023). La aplicación principal está en la carpeta `Inventario/`; `proyecto/` e `informacion/` contienen versiones previas y pruebas de reportes.

## Funcionalidades

**Inventario**
- Registro de productos con categoría, cantidad, precio de compra y precio de venta.
- Tabla de productos que se actualiza tras cada operación.
- Cambio automático del estado del producto a **Agotado** cuando su cantidad llega a cero.

**Facturación**
- Creación de facturas con varios productos (detalle de factura).
- Validación de que la cantidad solicitada no supere la disponible.
- Cálculo automático del total de la factura.
- Descuento del inventario al confirmar la venta y opción de cancelar la factura.

**Reportes** (Matplotlib)
- Producto más vendido.
- Ventas por mes en gráfico de barras y de torta.

## Stack

- Python 3.11
- Tkinter (interfaz gráfica)
- MySQL con `mysql-connector-python`
- Matplotlib, Pandas y Seaborn (reportes)

## Estructura

```
Inventario/
├── vista_principal.py               # Punto de entrada: menú principal
├── ventana_productos.py             # Gestión de inventario
├── ventana_factura.py               # Creación de facturas
├── funciones_ventana_productos.py   # Lógica de productos
├── funciones_venta_factura.py       # Lógica de facturación
├── grafico_productos.py             # Reporte: producto más vendido
├── grafico_ventas.py                # Reporte: ventas por mes (barras)
├── grafico_ventas_pastel.py         # Reporte: ventas por mes (torta)
└── conexion_2.py                    # Conexión a MySQL
inventario.sql                       # Script de la base de datos
```

## Modelo de datos

| Tabla | Descripción |
|---|---|
| `producto` | nombre, categoría, precio de compra, precio de venta, cantidad, estado |
| `categoria` | categorías de productos |
| `facturas` | fecha, estado, total |
| `det_factura` | productos de cada factura: cantidad, precio de venta, total |

## Instalación

1. Crea una base de datos `inventario` en MySQL e importa `inventario.sql`.
2. Ajusta los datos de conexión en `Inventario/conexion_2.py` si tu usuario o contraseña de MySQL son distintos.
3. Instala las dependencias:
   ```bash
   pip install -r requiriments.txt
   ```
4. Ejecuta la aplicación:
   ```bash
   cd Inventario
   python vista_principal.py
   ```

## Lo que aprendí

- Diseñar una base de datos relacional con encabezado y detalle de factura.
- Conectar una interfaz gráfica de escritorio con MySQL.
- Generar reportes visuales a partir de consultas SQL.
- Trabajar con ramas y pull requests en Git (`feature/create-report`, `reportes`).

## Autor

**Eduardo Machacón** · [GitHub](https://github.com/Ed4ard6)
