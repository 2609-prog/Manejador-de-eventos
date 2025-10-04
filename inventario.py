import json
import os
from producto import Producto

class Inventario:
    def __init__(self):
        self.productos = []
        self.archivo = os.path.join("data", "inventario.json")
        self.cargar_archivo()


    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, producto):
        self.productos.remove(producto)

    def modificar_producto(self, id, nombre=None, cantidad=None, precio=None):
        for prod in self.productos:
            if prod.id == id:
                if nombre:
                    prod.set_nombre(nombre)
                if cantidad is not None:
                    prod.set_cantidad(cantidad)
                if precio is not None:
                    prod.set_precio(precio)

    def mostrar_productos(self):
        return [str(prod) for prod in self.productos]

    def guardar_archivo(self):
        os.makedirs("data", exist_ok=True)
        with open(self.archivo, "w") as f:
            json.dump([prod.__dict__ for prod in self.productos], f, indent=4)

    def cargar_archivo(self):
        try:
            with open(self.archivo, "r") as f:
                data = json.load(f)
                self.productos = [Producto(**prod) for prod in data]
        except FileNotFoundError:
            self.productos = []
            self.guardar_archivo()


