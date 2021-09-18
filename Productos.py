# PD: El pc que se vaya a usar debe tener sqlite3 para que funcione y la librería tkinter para python
# PD4: ********************** Hecho por Camilo Andrés Barragán Gómez ******************************
#pip install pyinstaller
#pyinstaller programa.py
#enviar bd con la tabla, muy importante que la tabla esté en el mismo archivo donde se ejecute el programa .exe o .py
#Después en la carpeta dist que se generó, abra el ejecutable
from tkinter import ttk #Importar el ttk
from tkinter import * #Importar todo de tkiner
import sqlite3 #Importar la base de datos
class Productos: #Crear el objeto productos
    #Definir ventana de la aplicación
    def __init__(self, window): #Define la inicialización de la ventana
        self.wind = window #Variable de la ventana de la aplicación
        self.wind.title("Productos") #Título de la ventana de la aplicación
        window.config(bg = "old lace") #Color de fondo
        #Cuadro de registro
        Frame=LabelFrame(self.wind,text = "Registre un nuevo producto", fg = "blue") #Label de mensaje para registrar productos
        Frame.grid(row = 0, column = 0, columnspan = 2, pady = 20) #row=Fila,columna=columna de texto, columspan= columna de relleno, pady=espacio entre elementos
        #Registrar productos
        #Ingresar el nombre del producto
        Label(Frame, text = "Nombre: ").grid(row = 1, column = 0) #Cuadro donde escribirán los nombre de los productos
        self.nombre=Entry(Frame) #Espacio donde escribe el nombre
        self.nombre.focus() #Lleva el cursos directamente a donde está el primer espacio que es el de nombre
        self.nombre.grid(row = 1, column = 1) #Lugar donde se ubicará el nombre a escribir
        #Ingresar el precio
        Label(Frame, text = "Precio: ").grid(row = 2, column = 0) #Cuadro donde escribirán los precios del producto
        self.precio=Entry(Frame) #Cuadro donde escriben los precios de los productos
        self.precio.grid(row = 2, column = 1) #Lugar donde se ubicará el precio a escribir
        #Botón para agregar a los productos
        ttk.Button(Frame, text = "Guardar producto y actualizar lista", command=self.AgregarProductos).grid(row = 21, columnspan = 2, sticky = W+E)#Ubicación del botón guardar el producto
        self.mensaje = Label(text = "", fg = "red") #Lugar donde se ubicará el espacio de los mensajes y el color
        self.mensaje.grid(row=2, column=0, columnspan=2, sticky=W+E) #Características del mensaje
        #Crear tabla
        self.tree = ttk.Treeview(height = 11 , columns =("#0")) #Tabla donde se verán los datos guardados, aquí se ve la creación
        self.tree.grid(row = 9, column = 0, columnspan = 2) #Ubicación de la tabla
        self.tree.heading("#0", text = "Nombre", anchor = W) #Ubicación de la columna nombre en la tabla
        self.tree.heading("#1", text = "Precio", anchor = W) #Ubicación de la columna precios en la tabla
        #Crear botón de editar y de eliminar
        ttk.Button(Frame, text = "Eliminar producto", command = self.EliminarProducto).grid(row = 22, column=0, columnspan=2, sticky= W+E) #Botón para eliminar productos
        ttk.Button(Frame, text = "Editar producto", command = self.EditarProductos).grid(row = 23, column=0, columnspan=2, sticky= W+E) #Botón para editar productos
        ttk.Button(Frame, text = "Actualizar lista", command = self.ActualizarLista).grid(row= 24, columnspan = 2, sticky = W+E) #Ubicación botón actualizar lista
        self.ObtenenerProductos() #"Actualiza" los datos de la tabla
        #Conectar base de datos
    DbName="Productos.db" #Nombre de la base de datos
    def RunQuests(self, quests, parameters=()): #Conexión de una función a la base de datos, propiedades, preguntas y parámetros si los hay
        with sqlite3.connect(self.DbName) as conn: #conecta la base de datos y la asigna un nombre corto de la acción
            Cursor = conn.cursor() #Muestra en qué posición de la base de datos está
            Result = Cursor.execute(quests, parameters) #Ejecuta cada pregunta del programa para guardarlo en la base de datos
            conn.commit() #Guardar las preguntas
        return Result #Regresa la información
    #Nueva función de obtener los datos
    def ObtenenerProductos(self): #Obtener los productos
        Records = self.tree.get_children() #Mostrar datos de la tabla
        for element in Records: #ciclo para limpiarla en caso de que tenga información
            self.tree.delete(element) #comando delete
        quests = "SELECT * FROM Productos ORDER BY nombre ASC" #Esto es de SQL para consultar los datos
        DbRows = self.RunQuests(quests) #hacer que las filas vayan aumentando atuomáticamente
        for row in DbRows: #Rellenar los datos
            self.tree.insert("", 0, text = row[1], values = row[2]) #Espacios para ingresar los nuevos datos
    def Validacion(self): #Definir función para validar que el usuario llene todos los espacios
        return len(self.nombre.get())!=0 and len(self.precio.get())!=0 #Validación de que los datos no estén vacíos, si es distinto de 0 significa que el usuario ha ingresado algo
    def AgregarProductos(self): #Definir función para que agregue los nuevos productos a la base de datos
        if self.Validacion(): #Ejecuta la función validación y si es true permite el guardado
            quests = "INSERT into Productos VALUES(NULL, ?, ?)" #Insetar productos en la DB
            parameters = (self.nombre.get(), self.precio.get()) #Parámetros a insertar
            self.RunQuests(quests, parameters) #Correr la base de datos
            self.mensaje["text"] = "El producto {} ha sido agregado".format(self.nombre.get()) #Mensaje de que sí agregó el producto
            self.nombre.delete(0,END) #Reinicia el espacio de nombre
            self.precio.delete(0,END) #Reinicia el espacio de precio
        else: #Acción por si no es verdadero
            self.mensaje["text"] = "Para ingresar datos debe llenar todos los campos" #Impresión de lo que sea falso
        self.ObtenenerProductos() #Muestra la información de productos
    def ActualizarLista(self): #Definir función para que agregue los nuevos productos a la base de datos
        if self.Validacion(): #Ejecuta la función validación y si es true permite el guardado
            quests = "INSERT into Productos VALUES(NULL, ?, ?)" #Lo coloco para que actualice la tabla
            parameters = (self.nombre.get(), self.precio.get()) #Lo coloco para que actualice la tabla
            self.RunQuests(quests, parameters) #Correr la base de datos
            self.mensaje["text"] = "El producto {} ha sido agregado".format(self.nombre.get()) #Mensaje de que sí agregó el producto
            self.nombre.delete(0,END) #Reinicia el espacio de nombre
            self.precio.delete(0,END) #Reinicia el espacio de precio
        else: #Acción por si no es verdadero
            self.mensaje["text"] = "" #Impresión de lo que sea falso
        self.ObtenenerProductos() #Muestra la información de productos
    def EliminarProducto(self): #Función para eliminar productos
        self.mensaje["text"] = "" #Reinicia el mensaje
        try:
            self.tree.item(self.tree.selection())["text"][0] #Intenta que si hay algo seleccionado deje que funcione el eliminar producto
        except IndexError as e:
            self.mensaje["text"] = "Por favor seleccione el producto que desea eliminar" #Mensaje por si no selecciona producto para borrar
            return #Regresa a valor de no tener algo seleccionado
        self.mensaje["text"] = "" #Reinicia el mensaje
        nombre = self.tree.item(self.tree.selection())["text"] #Le da el valor a nombre de lo que haya seleccionado
        quests = "DELETE FROM Productos WHERE nombre = ?" #Busca en la base de datos el producto con el parámetro de nombre
        self.RunQuests(quests, (nombre, )) #Elimina el producto que se encuentra en nombre
        self.mensaje["text"] = "El producto {} ha sido eliminado de la faz de la Tierra satisfactoriamente".format(nombre) #Mensaje de que borró el producto seleccionado
        self.ObtenenerProductos #Muestra los productos actualizados en la tabla
    def EditarProductos(self): #Define función editar productos
        self.mensaje["text"] = "" #Reinicia el mensaje
        try: #Intento
            self.tree.item(self.tree.selection())["text"][0] #Intenta que si hay algo seleccionado deje que funcione el eliminar producto
        except IndexError as e:
            self.mensaje["text"] = "Por favor seleccione el producto que desea editar" #Mensaje por si no selecciona producto para borrar
            return #Regresa a valor de no tener algo seleccionado
        nombre = self.tree.item(self.tree.selection())["text"] #Propiedad nombre que selecciona de la tabla
        OldPrecio = self.tree.item(self.tree.selection())["values"][0] #Propiedad de precio que selecciona de la tabla
        self.editwind = Toplevel() #Crea una ventana nueva
        self.editwind.tittle = "Editar producto" #Nombre de la ventana nueva
        #Antiguo nombre
        Label(self.editwind, text = "Antiguo nombre").grid(row = 0, column = 1) #Texto y ubicación para "Antiguo nombre"
        Entry(self.editwind, textvariable = StringVar(self.editwind, value = nombre), state = "readonly").grid(row = 0, column = 2) #Información que captura de la tabla con el read only
        #Nuevo nombre
        Label(self.editwind, text = "Nuevo nombre").grid(row = 1, column = 1) #Texto y ubicación para "Nuevo nombre"
        NuevoNombre = Entry(self.editwind) #Entrada de Nuevo nombre en la ventana de edición
        NuevoNombre.grid(row = 1, column = 2) #Posición de la entrada
        #Antiguo precio
        Label(self.editwind, text = "Antiguo precio").grid(row = 2, column = 1) #Texto y ubicación para "Antiguo precio"
        Entry(self.editwind, textvariable = StringVar(self.editwind, value= OldPrecio), state = "readonly").grid(row = 2, column = 2) #Información que captura de la tabla con el read only
        #Nuevo precio
        Label(self.editwind, text = "Nuevo precio").grid(row = 3, column = 1) #Texto y ubicación para "Nuevo precio"
        NuevoPrecio = Entry(self.editwind) #Entrada de nuevo precio en la ventana de edición
        NuevoPrecio.grid(row = 3, column = 2) #Posición de la entrada
        Button(self.editwind, text = "Actualizar datos", command = lambda: self.DatosGuardados(NuevoNombre.get(), nombre, NuevoPrecio.get(), OldPrecio)).grid(row = 6, column = 2, sticky = W) #Botón actualizar datos que captura los datos nuevos y los pasa a la tabala en las propiedades antiguas
    def DatosGuardados(self, NuevoNombre, nombre, NuevoPrecio, OldPrecio): #funció que va a editar los datos a editar
        quests = "UPDATE Productos SET nombre = ?, precio = ? WHERE nombre = ? AND precio = ?" #Órdenes que se le dan a la DB
        parameters = (NuevoNombre, NuevoPrecio, nombre, OldPrecio) #Parámetros que toma la DB
        self.RunQuests(quests, parameters) #Llama a la función runquests a hacer su trabajo tomando las propiedades anteriores
        self.editwind.destroy() #Cierra la ventana de editar productos
        self.mensaje["text"] = "El producto {} ha sido actualizado".format(nombre) #Muestra el mensaje de que se editó correctamente
        self.ObtenenerProductos #"Actualiza" la lista de la tabla
if __name__=='__main__': #Comprobar que funcione la aplicación, la ventana
            window=Tk()
            application=Productos(window)
            window.mainloop()