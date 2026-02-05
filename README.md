Python: Sistema de Gestión de Inventario "TechStore"

Contexto del Problema


La tienda "TechStore" necesita automatizar el control de su inventario. Actualmente guardan todo en un archivo JSON, pero necesitan una herramienta de consola que permita gestionar los productos sin errores de ejecución y asegurando que la información persistirá aunque se cierre el programa.



Requerimientos Funcionales


El programa debe presentar un menú interactivo con las siguientes opciones:

1️⃣	Cargar Inventario: Al iniciar, el programa debe leer un archivo llamado inventario.json. Si el archivo no existe, debe crear una lista vacía y notificar al usuario.



2️⃣ Agregar Producto: Debe solicitar: nombre, precio (flotante) y cantidad (entero).

Validación: El precio y la cantidad no pueden ser negativos.


3️⃣ Actualizar Stock: Buscar un producto por nombre y permitir modificar su cantidad.



4️⃣Mostrar Inventario: Listar todos los productos. Si el inventario está vacío, mostrar un mensaje informativo.



6️⃣Guardar y Salir: Escribir los datos actualizados en inventario.json y cerrar el programa.





Requerimientos Técnicos (Obligatorios)


Estructuras de Datos: Utilizar una lista de diccionarios para representar el inventario.
Manejo de Archivos: Uso estricto de la librería json con el manejador de contexto with.
Errores y Excepciones:
Implementar bloques try-except para capturar errores de tipo de dato (por ejemplo, si el usuario ingresa texto en lugar de un número en el precio).
Manejar la excepción FileNotFoundError al cargar el archivo.
Ciclos y Condiciones: Un ciclo principal para el menú y condicionales para la lógica de cada opción.