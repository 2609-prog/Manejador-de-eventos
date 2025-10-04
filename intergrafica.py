
import tkinter as tk # Importa Tkinter para la interfaz gráfica
from tkinter import messagebox, simpledialog
from inventario import Inventario # Importa la clase Inventario
from producto import Producto # Importa la clase Producto

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Inventario") # Establece el título de la ventana

        # Información del estudiante
        self.info_estudiante = "Nombre: Lisseth Puco\nCarrera: Ingeniería en Tecnologias de la Informacion\nParalelo: A"

        # Crear objeto Inventario y cargar datos desde archivo
        self.inventario = Inventario()
        self.inventario.cargar_archivo()
 
        # Mostrar el menú principal

        self.menu_principal()

    def menu_principal(self):
        self.limpiar_ventana()

        label_info = tk.Label(self.root, text=self.info_estudiante, font=("Arial", 14))
        label_info.pack(pady=10)

        btn_productos = tk.Button(self.root, text="Productos", width=20, command=self.abrir_productos)
        btn_productos.pack(pady=5)

        btn_salir = tk.Button(self.root, text="Salir", width=20, command=self.root.quit)
        btn_salir.pack(pady=5)

    def abrir_productos(self):
        self.limpiar_ventana() # Limpia ventana antes de mostrar opciones de productos

        label = tk.Label(self.root, text="Gestión de Productos", font=("Arial", 14))
        label.pack(pady=10)

        # Botones para cada acción sobre productos
        btn_agregar = tk.Button(self.root, text="Agregar Producto", width=20, command=self.agregar_producto)
        btn_agregar.pack(pady=5)

        btn_modificar = tk.Button(self.root, text="Modificar Producto", width=20, command=self.modificar_producto)
        btn_modificar.pack(pady=5)

        btn_eliminar = tk.Button(self.root, text="Eliminar Producto", width=20, command=self.eliminar_producto)
        btn_eliminar.pack(pady=5)

        btn_listar = tk.Button(self.root, text="Listar Productos", width=20, command=self.listar_productos)
        btn_listar.pack(pady=5)

        # Botón para volver al menú principal
        btn_volver = tk.Button(self.root, text="Volver", width=20, command=self.menu_principal)
        btn_volver.pack(pady=5)

    def agregar_producto(self):
         # Solicitar ID del producto
        id_producto = simpledialog.askstring("ID", "Ingrese ID del producto:")
        if not id_producto:
            return
        if id_producto in self.inventario.productos:
            messagebox.showerror("Error", "El ID ya existe.")
            return

        # Validar que el ID no exista
        nombre = simpledialog.askstring("Nombre", "Ingrese nombre del producto:")
        if not nombre:
            return

        try:
               # Solicitar cantidad y precio
            cantidad = int(simpledialog.askstring("Cantidad", "Ingrese cantidad:"))
            precio = float(simpledialog.askstring("Precio", "Ingrese precio:"))
        except (TypeError, ValueError):
            messagebox.showerror("Error", "Cantidad y precio deben ser números.")
            return
            
# Crear producto y agregarlo al inventario

        producto = Producto(id_producto, nombre, cantidad, precio)
        self.inventario.agregar_producto(producto)
        self.inventario.guardar_archivo()
        messagebox.showinfo("Éxito", "Producto agregado.")

    def modificar_producto(self):
         # Solicitar ID del producto a modificar
        id_producto = simpledialog.askstring("ID", "Ingrese ID del producto a modificar:")
        if not id_producto or id_producto not in self.inventario.productos:
            messagebox.showerror("Error", "Producto no encontrado.")
            return
 # Solicitar nuevos datos (permitiendo dejar vacío para no cambiar)
        nombre = simpledialog.askstring("Nombre", "Ingrese nuevo nombre (dejar vacío para no cambiar):")
        cantidad_str = simpledialog.askstring("Cantidad", "Ingrese nueva cantidad (dejar vacío para no cambiar):")
        precio_str = simpledialog.askstring("Precio", "Ingrese nuevo precio (dejar vacío para no cambiar):")

        cantidad = None
        precio = None

        if cantidad_str:
            try:
                cantidad = int(cantidad_str)
            except ValueError:
                messagebox.showerror("Error", "Cantidad debe ser un número.")
                return

        if precio_str:
            try:
                precio = float(precio_str)
            except ValueError:
                messagebox.showerror("Error", "Precio debe ser un número.")
                return
  # Modificar el producto en el inventario
        self.inventario.modificar_producto(id_producto, nombre if nombre else None, cantidad, precio)
        self.inventario.guardar_archivo("inventario.json")
        messagebox.showinfo("Éxito", "Producto modificado.")

    def eliminar_producto(self):
        id_producto = simpledialog.askstring("ID", "Ingrese ID del producto a eliminar:")
        if not id_producto or id_producto not in self.inventario.productos:
            messagebox.showerror("Error", "Producto no encontrado.")
            return
            
        # Eliminar producto del inventario

        self.inventario.eliminar_producto(id_producto)
        self.inventario.guardar_archivo("inventario.json")
        messagebox.showinfo("Éxito", "Producto eliminado.")

    def listar_productos(self):
        productos = self.inventario.mostrar_productos()
        if not productos:
            messagebox.showinfo("Productos", "No hay productos en el inventario.")
            return
  # Crear ventana para mostrar productos
        ventana_listar = tk.Toplevel(self.root)
        ventana_listar.title("Lista de Productos")

        text = tk.Text(ventana_listar, width=60, height=20)
        text.pack()
    # Insertar productos en la ventana
        for p in productos:
            text.insert(tk.END, p + "\n")

        text.config(state=tk.DISABLED) # Hacer texto no editable

    def limpiar_ventana(self):
        # Elimina todos los widgets de la ventana principal
        for widget in self.root.winfo_children():
            widget.destroy()


# Ejecutar la aplicación

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root) # Crear instancia de la aplicación
    root.mainloop() # Ejecutar bucle principal de Tkinter

