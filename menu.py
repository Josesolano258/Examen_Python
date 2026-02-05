import json

try:
    with open('inventario.json', 'r') as archivo:
        inventario = json.load(archivo)
except FileNotFoundError:
    inventario = []
    print("Archivo no encontrado, se creó uno nuevo")

    
def agregar_producto():
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad disponible: "))
        
        if precio < 0 or cantidad < 0:
            print("Error: El precio y la cantidad deben ser valores positivos.")
        else:
            
            producto = {
                'nombre' : nombre,
                'precio' : precio,
                'cantidad' : cantidad
            }
            
            inventario.append(producto)
            
def actualizar_stock():
        actualizar_stock = input("Ingrese el nombre del producto que desea modificar: ")
        encontrado = False
        for producto in inventario:
            if producto["nombre"] == actualizar_stock:
                producto_actualizado = int(input("Nuevo Stock: "))
                if producto_actualizado < 0:
                    print("Error")
                else:
                    producto["cantidad"] = producto_actualizado
                    print("Producto actualizado")
                    encontrado = True
                    break
                if not encontrado:
                    print("Producto no encontrado")
                    

def mostrar():
         if not inventario:
            print("No hay productos registrados")
         else:
            for producto in inventario:
                print("--- INVENTARIO ---")
                print(producto["nombre"])
                print(producto["precio"])
                print(producto["cantidad"])
                    
    
def guardar():
        with open('inventario.json', 'w') as archivo:
            json.dump(inventario, archivo, indent=4)
        


def menu_inventario ():
    while True:
        print("---- MENU ----")
        print("1.Agregar Producto")
        print("2.Actualizar stock")
        print("3.Mostrar inventario")
        print("4.Guardar y salir")
    

        opcion = input("Elige una opcion: ")
    
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            actualizar_stock()
        elif opcion == "3":
            mostrar()
        elif opcion == "4":
            guardar()
        elif opcion == "0":
            print("Saliendo del programa")
            break
        else:
            print("opcion invalida")    

menu_inventario()
    
