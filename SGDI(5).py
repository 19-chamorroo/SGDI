"""
Cambiar las listas por diccionario [x]
Camabiar las funciones para que usen diccionarios [x]
Busqueda de diccionarios dentro de listas [x]
*Agregar el procesamiento de códigos de productos []


"""
opcion=0

lista_productos=[]
#+producto={"nombre":nombre,"cantidad":stock,"precio":precio, "codigo":codigo}



def contadordemayusculas(codigo):
    contador_mayusculas=0

# el for se va a ejecutar por cada uno de los caracteres dentro de la 
# variable/parametro "codigo".
# #en cada iteracion "letra" va a tener ek valor de un caracter dentro de "codigo". 
# por ejemplo: en la primera iteracion letra va a ser "3" si el codigo fuese Juan23"

    for letra in str(codigo):
        if letra.isupper():
            contador_mayusculas+=1
    return contador_mayusculas
def contadorDeNumeros(Codigo):
    contador_numeros=0
    for letra in str(Codigo):
        if letra.isnumeric():
            contador_numeros+=1
    return contadorDeNumeros

def validarcodigo(codigo):
    if contadordemayusculas(codigo)<2:
        print("El codigo debe tener al menos 2 mayusculas")
        return False
    elif contadordemayusculas(codigo)==0:
        return False
        print("el codigo debe tener al menos 1 numero")
    elif len(codigo)<5:
        print("el codigo debe tener almenos 5 caracteres")
        return False
    else:
        return False

def soliciarProducto():
    nombreProd= input("Ingrese el nombre del nuevo producto: ")
    
    while True:
        codigo=input("ingrese el codigo del nuevo producto")

        if validarcodigo(codigo)==True:
            print("Codigo ingresado correctamente")
            break
        else:
            print("Codigo incorrecto. ingreselo nuevamente")

    try:
        precioProd= int(input("Ingrese el precio del nuevo producto: "))
        stockProd= int(input("Ingrese el stock del nuevo producto: "))
        if precioProd<0 or stockProd<0:
            raise ValueError
        else:
            return [nombreProd,precioProd,stockProd]
            
    except ValueError:
        print("Debe ingresar valores númericos positivos")

def buscarProducto(nombre):

    for producto in lista_productos:
        if producto["nombre"].lower()==nombre.lower():
           return producto
    
    return None

def guardarProducto(nombre,precio,stock):

    if buscarProducto(nombre)==None:
        producto={
            "nombre":nombre,
            "cantidad":stock,
            "precio":precio}
        lista_productos.append(producto)
        print("Producto guardado con éxito")
    else:
        print("Ya existe un producto con ese nombre")

def actualizarProducto(nombre,nuevoStock,nuevoPrecio):
    productoBuscado= buscarProducto(nombre)
    if productoBuscado!=None:
        indice= lista_productos.index(productoBuscado)
        productoBuscado["cantidad"]=nuevoStock
        productoBuscado["precio"]=nuevoPrecio
        #actualizar el producto en la lista de productos
        lista_productos[indice]=productoBuscado
        print(f"el producto {nombre} fue actualizado correctamente")
    else:
        print("El producto que intenta actualizar no existe")

def mostrarInventarioCompleto():
    #deben iterar sobre la lista de productos
    #luego deben imprimir la información de cada producto
    if len(lista_productos)==0:
        print("No hay productos aún")
    else:
        for producto in lista_productos:
            print(f"Nombre: {producto["nombre"]} \t\t Precio: ${producto["precio"]} \t\t Stock: {producto["cantidad"]}")

def eliminarProducto(nombre):
    productoBuscado= buscarProducto(nombre)
    if productoBuscado!=None:
        lista_productos.remove(productoBuscado)
        print("Producto eliminado correctamente")
    else:
        print("No existe un producto con ese nombre")

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
            infoProducto=soliciatProducto()
            #[nombreProd,precioProd,stockProd]
            if infoProducto!=None:
                guardarProducto(infoProducto[0],
                                infoProducto[1],
                                infoProducto[2])
        


        case "2":
            nombre=input("Ingrese el nombre del producto a buscar: ")
            productoEncontrado=buscarProducto(nombre)
            if productoEncontrado!=None:
                print("-"*60)
                print(f"Nombre: {productoEncontrado["nombre"]} \t\t Precio: ${productoEncontrado["precio"]} \t\t Stock: {productoEncontrado["cantidad"]}")
                print("-"*60)

        case "3":
            infoProducto=soliciatProducto()
            #[nombreProd,precioProd,stockProd]
            if infoProducto!=None:
                actualizarProducto(nombre=infoProducto[0],nuevoStock=infoProducto[2],nuevoPrecio=infoProducto[1])

        case "4":
            mostrarInventarioCompleto()
        
        case "5":
            nombre=input("Ingrese el nombre del producto a eliminar: ")
            eliminarProducto(nombre)
        
        case "6":
            print("Saliendo...")
        
        case default:
            print("Opción no valida")
        