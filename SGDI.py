"""
Acciones del menú:

Agregar producto
Buscar producto
Actualizar cantidad/precio
Mostrar inventario completo
Eliminar producto
Salir
"""
opcion=0
nombreProductos=[]
precioProductos=[]
stockProductos=[]

def agregarProducto():
    nombreProd= input("Ingrese el nombre del nuevo producto: ")
    try:
        precioProd= int(input("Ingrese el precio del nuevo producto: "))
        stockProd= int(input("Ingrese el stock del nuevo producto: "))
        if precioProd<0 or stockProd<0:
            raise ValueError
        else:
            nombreProductos.append(nombreProd)
            precioProductos.append(precioProd)
            stockProductos.append(stockProd)
    except ValueError:
        print("Debe ingresar valores númericos positivos")

def buscarProducto(nombre):
    try:
        indice=nombreProductos.index(nombre)
        nombreProd=nombreProductos[indice]
        precioProd=precioProductos[indice]
        stockProd=stockProductos[indice]
        
        producto=[nombreProd,precioProd,stockProd]
        return producto

    except ValueError:
        print("No se encontró el producto")



while opcion!="6":
    print("**************Menu de gestión de inventario**************")
    print("1.- Agregar producto")
    print("2.- Buscar producto")
    print("3.- Actualizar cantidad/precio")
    print("4.- Mostrar inventario completo")
    print("5.- Eliminar producto")
    print("6.- Salir")

    opcion= input("Ingrese la opción que desea(1-6): ")

    match opcion:
        case "1":
            agregarProducto()
        case "2":
            nombre=input("Ingrese el nombre del producto a buscar: ")
            productoEncontrado=buscarProducto(nombre)
            if productoEncontrado!=None:
                print(f"Nombre: {productoEncontrado[0]} \t\t Precio: ${productoEncontrado[1]} \t\t Stock: {productoEncontrado[2]}")
            