import json # Importa el módulo JSON para lectura y escritura de archivos JSON
import os # Importa el módulo OS para manejo de rutas y directorios
from producto import Producto  #Importa la clase Producto

class Inventario:
    def __init__(self):
        # Lista para almacenar los objetos Producto
        self.productos = []
        # Ruta del archivo donde se guarda el inventario
        self.archivo = os.path.join("data", "inventario.json")
        # Cargar inventario desde el archivo
        self.cargar_archivo()


    def agregar_producto(self, producto):
        # Agrega un producto a la lista de inventario
        self.productos.append(producto)

    def eliminar_producto(self, producto):
        # Elimina un producto de la lista de inventario
        self.productos.remove(producto)

    def modificar_producto(self, id, nombre=None, cantidad=None, precio=None): # Modifica los atributos de un producto identificado por su ID
        for prod in self.productos:
            if prod.id == id:
                if nombre:
                    prod.set_nombre(nombre)
                if cantidad is not None:
                    prod.set_cantidad(cantidad)
                if precio is not None:
                    prod.set_precio(precio)

    def mostrar_productos(self):
        # Devuelve una lista con la representación en string de cada producto
        return [str(prod) for prod in self.productos]

    def guardar_archivo(self):
        # Crear carpeta "data" si no existe
        os.makedirs("data", exist_ok=True)
         # Guardar inventario en formato JSON
        with open(self.archivo, "w") as f:
            json.dump([prod.__dict__ for prod in self.productos], f, indent=4)

    def cargar_archivo(self):
        try:
            with open(self.archivo, "r") as f:
                data = json.load(f)
                 # Crear objetos Producto desde los datos cargados
                self.productos = [Producto(**prod) for prod in data]
        except FileNotFoundError:
             # Si no existe el archivo, inicializar inventario vacío y crear archivo
            self.productos = []
            self.guardar_archivo()


