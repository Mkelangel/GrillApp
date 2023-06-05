# Importar módulo tkinter para la interfaz gráfica
from tkinter import *
import sqlite3

#Definir 
ventana_inventario_abierta = False
ventana_inventario = None

ventana_personal_abierta = False
ventana_personal = None

ventana_registro_ventas_abierta = False
ventana_registro_ventas = None

ventana_facturas_abierta = False
ventana_facturas = None


# Funciones
def gestionar_inventario():

    global ventana_inventario_abierta, ventana_inventario

    # Verificar si la ventana de inventario ya está abierta
    if ventana_inventario is not None and ventana_inventario.winfo_exists():
        ventana_inventario.focus()
        return

    ventana_inventario = Toplevel(ventana)
    ventana_inventario.title("Gestión de Inventario")
    ventana_inventario.geometry("300x200")

    # Centrar la ventana en la pantalla
    ventana_inventario.update_idletasks()
    width = ventana_inventario.winfo_width()
    height = ventana_inventario.winfo_height()
    x = (ventana_inventario.winfo_screenwidth() // 2) - (width // 2)
    y = (ventana_inventario.winfo_screenheight() // 2) - (height // 2)
    ventana_inventario.geometry(f"{width}x{height}+{x}+{y}")

    # Hacer que la ventana sea inamovible
    ventana_inventario.resizable(False, False)

    # Conectar a la base de datos o crearla si no existe
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    # Crear la tabla de productos si no existe
    cursor.execute("CREATE TABLE IF NOT EXISTS Productos (id INTEGER PRIMARY KEY, nombre TEXT, precio REAL)")

    # Función para agregar un producto al inventario
    def agregar_producto():
        id_producto = entry_id.get()
        nombre_producto = entry_nombre.get()
        precio_producto = entry_precio.get()

        # Insertar el producto en la base de datos
        cursor.execute("INSERT INTO Productos VALUES (?, ?, ?)", (id_producto, nombre_producto, precio_producto))
        conexion.commit()

        # Limpiar los campos de entrada
        entry_id.delete(0, END)
        entry_nombre.delete(0, END)
        entry_precio.delete(0, END)

    # Función para mostrar los productos del inventario
    def mostrar_productos():
        # Obtener todos los productos de la base de datos
        cursor.execute("SELECT * FROM Productos")
        productos = cursor.fetchall()

        # Limpiar el área de visualización
        area_productos.delete("1.0", END)

        # Mostrar los productos en el área de visualización
        for producto in productos:
            area_productos.insert(END, f"ID: {producto[0]}\n")
            area_productos.insert(END, f"Nombre: {producto[1]}\n")
            area_productos.insert(END, f"Precio: {producto[2]}\n")
            area_productos.insert(END, "----------------------------\n")

    # Etiquetas y campos de entrada para agregar productos
    label_id = Label(ventana_inventario, text="ID:")
    label_id.pack()
    entry_id = Entry(ventana_inventario)
    entry_id.pack()

    label_nombre = Label(ventana_inventario, text="Nombre:")
    label_nombre.pack()
    entry_nombre = Entry(ventana_inventario)
    entry_nombre.pack()

    label_precio = Label(ventana_inventario, text="Precio:")
    label_precio.pack()
    entry_precio = Entry(ventana_inventario)
    entry_precio.pack()

    boton_agregar = Button(ventana_inventario, text="Agregar Producto", command=agregar_producto)
    boton_agregar.pack()

    # Área de visualización de productos
    area_productos = Text(ventana_inventario)
    area_productos.pack()

    boton_mostrar = Button(ventana_inventario, text="Mostrar Productos", command=mostrar_productos)
    boton_mostrar.pack()
def cerrar_ventana_inventario():
    global ventana_inventario

    # Cerrar la ventana si está definida
    if ventana_inventario is not None and ventana_inventario.winfo_exists():
        ventana_inventario.destroy()
        ventana_inventario = None


def gestionar_personal():
    ventana_personal = Toplevel(ventana)
    ventana_personal.title("Control de Personal")
    ventana_personal.geometry("300x200")

    # Centrar la ventana en la pantalla
    ventana_personal.update_idletasks()
    width = ventana_personal.winfo_width()
    height = ventana_personal.winfo_height()
    x = (ventana_personal.winfo_screenwidth() // 2) - (width // 2)
    y = (ventana_personal.winfo_screenheight() // 2) - (height // 2)
    ventana_personal.geometry(f"{width}x{height}+{x}+{y}")

    # Hacer que la ventana sea inamovible
    ventana_personal.resizable(False, False)

    # Conectar a la base de datos o crearla si no existe
    conexion = sqlite3.connect("personal.db")
    cursor = conexion.cursor()

    # Crear la tabla de personal si no existe
    cursor.execute("CREATE TABLE IF NOT EXISTS Personal (id INTEGER PRIMARY KEY, nombre TEXT, puesto TEXT, asistencia TEXT)")

    # Función para agregar una persona al control de personal
    def agregar_persona():
        id_persona = entry_id.get()
        nombre_persona = entry_nombre.get()
        puesto_persona = entry_puesto.get()
        asistencia_persona = entry_asistencia.get()

        # Insertar la persona en la base de datos
        cursor.execute("INSERT INTO Personal VALUES (?, ?, ?, ?)", (id_persona, nombre_persona, puesto_persona, asistencia_persona))
        conexion.commit()

        # Limpiar los campos de entrada
        entry_id.delete(0, END)
        entry_nombre.delete(0, END)
        entry_puesto.delete(0, END)
        entry_asistencia.delete(0, END)

    # Función para mostrar el personal
    def mostrar_personal():
        # Obtener todo el personal de la base de datos
        cursor.execute("SELECT * FROM Personal")
        personal = cursor.fetchall()

        # Limpiar el área de visualización
        area_personal.delete("1.0", END)

        # Mostrar el personal en el área de visualización
        for persona in personal:
            area_personal.insert(END, f"ID: {persona[0]}\n")
            area_personal.insert(END, f"Nombre: {persona[1]}\n")
            area_personal.insert(END, f"Puesto: {persona[2]}\n")
            area_personal.insert(END, f"Asistencia: {persona[3]}\n")
            area_personal.insert(END, "----------------------------\n")

    # Etiquetas y campos de entrada para agregar personas
    label_id = Label(ventana_personal, text="ID:")
    label_id.pack()
    entry_id = Entry(ventana_personal)
    entry_id.pack()

    label_nombre = Label(ventana_personal, text="Nombre:")
    label_nombre.pack()
    entry_nombre = Entry(ventana_personal)
    entry_nombre.pack()

    label_puesto = Label(ventana_personal, text="Puesto:")
    label_puesto.pack()
    entry_puesto = Entry(ventana_personal)
    entry_puesto.pack()

    label_asistencia = Label(ventana_personal, text="Asistencia:")
    label_asistencia.pack()
    entry_asistencia = Entry(ventana_personal)
    entry_asistencia.pack()

    boton_agregar = Button(ventana_personal, text="Agregar Persona", command=agregar_persona)
    boton_agregar.pack()

    # Área de visualización del personal
    area_personal = Text(ventana_personal)
    area_personal.pack()

    boton_mostrar = Button(ventana_personal, text="Mostrar Personal", command=mostrar_personal)
    boton_mostrar.pack()
def cerrar_ventana_personal():
    global ventana_personal_abierta, ventana_personal

    # Establecer la variable de control a False al cerrar la ventana
    ventana_personal_abierta = False

    # Cerrar la ventana si está definida
    if ventana_personal:
        ventana_personal.destroy()


def registrar_venta():
    # Crear la ventana de registro de ventas
    ventana_ventas = Toplevel(ventana)
    ventana_ventas.title("Registrar Ventas")
    ventana_ventas.geometry("300x200")

    # Centrar la ventana en la pantalla
    ventana_ventas.update_idletasks()
    width = ventana_ventas.winfo_width()
    height = ventana_ventas.winfo_height()
    x = (ventana_ventas.winfo_screenwidth() // 2) - (width // 2)
    y = (ventana_ventas.winfo_screenheight() // 2) - (height // 2)
    ventana_ventas.geometry(f"{width}x{height}+{x}+{y}")

    # Hacer que la ventana sea inamovible
    ventana_ventas.resizable(False, False)


    # Conectar a la base de datos o crearla si no existe
    conexion = sqlite3.connect("ventas.db")
    cursor = conexion.cursor()

    # Crear la tabla de ventas si no existe
    cursor.execute("CREATE TABLE IF NOT EXISTS Ventas (id INTEGER PRIMARY KEY, producto TEXT, cantidad INTEGER, precio REAL)")

    # Función para agregar una venta
    def agregar_venta():
        id_venta = entry_id.get()
        producto_venta = entry_producto.get()
        cantidad_venta = entry_cantidad.get()
        precio_venta = entry_precio.get()

        # Insertar la venta en la base de datos
        cursor.execute("INSERT INTO Ventas VALUES (?, ?, ?, ?)", (id_venta, producto_venta, cantidad_venta, precio_venta))
        conexion.commit()

        # Limpiar los campos de entrada
        entry_id.delete(0, END)
        entry_producto.delete(0, END)
        entry_cantidad.delete(0, END)
        entry_precio.delete(0, END)

    # Función para mostrar las ventas
    def mostrar_ventas():
        # Obtener todas las ventas de la base de datos
        cursor.execute("SELECT * FROM Ventas")
        ventas = cursor.fetchall()

        # Limpiar el área de visualización
        area_ventas.delete("1.0", END)

        # Mostrar las ventas en el área de visualización
        for venta in ventas:
            area_ventas.insert(END, f"ID: {venta[0]}\n")
            area_ventas.insert(END, f"Producto: {venta[1]}\n")
            area_ventas.insert(END, f"Cantidad: {venta[2]}\n")
            area_ventas.insert(END, f"Precio: {venta[3]}\n")
            area_ventas.insert(END, "----------------------------\n")

    # Etiquetas y campos de entrada para agregar ventas
    label_id = Label(ventana_ventas, text="ID:")
    label_id.pack()
    entry_id = Entry(ventana_ventas)
    entry_id.pack()

    label_producto = Label(ventana_ventas, text="Producto:")
    label_producto.pack()
    entry_producto = Entry(ventana_ventas)
    entry_producto.pack()

    label_cantidad = Label(ventana_ventas, text="Cantidad:")
    label_cantidad.pack()
    entry_cantidad = Entry(ventana_ventas)
    entry_cantidad.pack()

    label_precio = Label(ventana_ventas, text="Precio:")
    label_precio.pack()
    entry_precio = Entry(ventana_ventas)
    entry_precio.pack()

    boton_agregar = Button(ventana_ventas, text="Agregar Venta", command=agregar_venta)
    boton_agregar.pack()

    # Área de visualización de ventas
    area_ventas = Text(ventana_ventas)
    area_ventas.pack()

    boton_mostrar = Button(ventana_ventas, text="Mostrar Ventas", command=mostrar_ventas)
    boton_mostrar.pack()
def cerrar_ventana_registro_ventas():
    global ventana_registro_ventas_abierta, ventana_registro_ventas

    # Establecer la variable de control a False al cerrar la ventana
    ventana_registro_ventas_abierta = False

    # Cerrar la ventana si está definida
    if ventana_registro_ventas:
        ventana_registro_ventas.destroy()


def generar_facturas():

    global ventana_facturas_abierta, ventana_facturas # Declarar la variable como global

     # Verificar si la ventana de facturas ya está abierta
    if ventana_facturas is not None and ventana_facturas.winfo_exists():
        ventana_facturas.focus()
        return
    
    # Crear la ventana de generación de facturas
    ventana_facturas = Toplevel(ventana)
    ventana_facturas.title("Generar Facturas")

    # Obtener las dimensiones de la ventana secundaria
    ancho_ventana_facturas = 300
    alto_ventana_facturas = 400

    # Calcular las coordenadas para centrar la ventana secundaria
    x = int(ventana.winfo_x() + ventana.winfo_width() / 2 - ancho_ventana_facturas / 2)
    y = int(ventana.winfo_y() + ventana.winfo_height() / 2 - alto_ventana_facturas / 2)

    # Establecer la ubicación y las dimensiones de la ventana secundaria
    ventana_facturas.geometry(f"{ancho_ventana_facturas}x{alto_ventana_facturas}+{x}+{y}")

    # Desactivar el redimensionamiento de la ventana secundaria
    ventana_facturas.resizable(False, False)

    # Conectar a la base de datos o crearla si no existe
    conexion = sqlite3.connect("facturas.db")
    cursor = conexion.cursor()

    # Crear la tabla de facturas si no existe
    cursor.execute("CREATE TABLE IF NOT EXISTS Facturas (id INTEGER PRIMARY KEY, cliente TEXT, total REAL)")

    # Función para agregar una factura
    def agregar_factura():
        id_factura = entry_id.get()
        cliente_factura = entry_cliente.get()
        total_factura = entry_total.get()

        # Insertar la factura en la base de datos
        cursor.execute("INSERT INTO Facturas VALUES (?, ?, ?)", (id_factura, cliente_factura, total_factura))
        conexion.commit()

        # Limpiar los campos de entrada
        entry_id.delete(0, END)
        entry_cliente.delete(0, END)
        entry_total.delete(0, END)

    # Función para mostrar las facturas
    def mostrar_facturas():
        # Obtener todas las facturas de la base de datos
        cursor.execute("SELECT * FROM Facturas")
        facturas = cursor.fetchall()

        # Limpiar el área de visualización
        area_facturas.delete("1.0", END)

        # Mostrar las facturas en el área de visualización
        for factura in facturas:
            area_facturas.insert(END, f"ID: {factura[0]}\n")
            area_facturas.insert(END, f"Cliente: {factura[1]}\n")
            area_facturas.insert(END, f"Total: {factura[2]}\n")
            area_facturas.insert(END, "----------------------------\n")

    # Etiquetas y campos de entrada para agregar facturas
    label_id = Label(ventana_facturas, text="ID:")
    label_id.pack()
    entry_id = Entry(ventana_facturas)
    entry_id.pack()

    label_cliente = Label(ventana_facturas, text="Cliente:")
    label_cliente.pack()
    entry_cliente = Entry(ventana_facturas)
    entry_cliente.pack()

    label_total = Label(ventana_facturas, text="Total:")
    label_total.pack()
    entry_total = Entry(ventana_facturas)
    entry_total.pack()

    boton_agregar = Button(ventana_facturas, text="Agregar Factura", command=agregar_factura)
    boton_agregar.pack()

    # Área de visualización de facturas
    area_facturas = Text(ventana_facturas)
    area_facturas.pack()
    

    boton_mostrar = Button(ventana_facturas, text="Mostrar Facturas", command=mostrar_facturas)
    boton_mostrar.pack()

   # Función para cerrar la ventana de facturas
def cerrar_ventana_facturas():

    global ventana_facturas,ventana_facturas_abierta

    # Cerrar la ventana si está definida
    if ventana_facturas is not None and ventana_facturas.winfo_exists():
        ventana_facturas.destroy()
        ventana_facturas = None
  
    


# Crear la ventana principal
ventana = Tk()
ventana.title("Churrasquería")
ventana.geometry("300x400")

# Obtener la resolución de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# Calcular las coordenadas para centrar la ventana
x = int(ancho_pantalla/2 - 300/2)  # 300 es el ancho deseado de la ventana principal
y = int(alto_pantalla/2 - 400/2)  # 400 es el alto deseado de la ventana principal

# Ubicar la ventana principal en el centro de la pantalla
ventana.geometry(f"300x400+{x}+{y}")

# Botones para acceder a las diferentes funcionalidades
boton_inventario = Button(ventana, text="Gestionar Inventario", command=gestionar_inventario)
boton_inventario.pack(pady=20)

boton_personal = Button(ventana, text="Control de Personal", command=gestionar_personal)
boton_personal.pack(pady=20)

boton_venta = Button(ventana, text="Registrar Venta", command=registrar_venta)
boton_venta.pack(pady=20)

boton_facturas = Button(ventana, text="Generar Facturas", command=generar_facturas)
boton_facturas.pack(pady=20)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()