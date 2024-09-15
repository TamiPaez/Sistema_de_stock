#~~~~~Importaciones~~~~~#
from tkinter import *
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from os import startfile
import sqlite3

#~~~~~Conexión a la base de datos~~~~~#
conexion=sqlite3.connect("Base_de_stock.db")

#~~~~~Creación y Configuración de la ventana~~~~~#
ventana=Tk()
ventana.state("zoomed")
ventana.geometry("900x700")
ventana.config(bg="#CFFFFA")
ventana.title("Sistema De Stock")
ventana.iconbitmap("Restaurante.ico")

#~~~~~Colores~~~~~#
colorFondo="#E3E3E3"
colorLetra="gray30"
colorStock="#FFD8ED"
colorClientes="#CFFFFA"
colorVentas="#C8FFC9"
colorServicios="#FEE3C6"

#~~~~~Frames~~~~~#
clientesFrame=Frame(bg=colorClientes)
stockFrame=Frame(bg=colorStock)
ingredientesFrame=Frame(stockFrame,bg=colorStock)
utensiliosFrame=Frame(stockFrame,bg=colorStock)
maquinariaFrame=Frame(stockFrame,bg=colorStock)

ventasFrame=Frame(bg=colorVentas)
comprasFrame=Frame(ventasFrame,bg=colorVentas)
carritoFrame=Frame(ventasFrame,bg=colorVentas)

serviciosFrame=Frame(bg=colorServicios)
tituloFrame=Frame(bg="ghost white")
tituloFrame.pack(fill=X)

#~~~~~Labels~~~~~#
tituloLabel=Label(tituloFrame,text="Sistema De Stock",bg="ghost white",fg="black",font=("Brush Script MT",24))
tituloLabel.pack()
clientesLabel=Label(clientesFrame,text="Listado de Clientes:",bg=colorClientes,font=("Calibri",14))
clientesLabel.pack()

#~~~~~Navegación~~~~~#
def borrarFrames():
    clientesFrame.pack_forget()
    stockFrame.pack_forget()
    ventasFrame.pack_forget()
    serviciosFrame.pack_forget()
def borrarFramesStock():
    ingredientesFrame.pack_forget()
    utensiliosFrame.pack_forget()
    maquinariaFrame.pack_forget()
def borrarFramesVentas():
    comprasFrame.pack_forget()
    carritoFrame.pack_forget()
    
def clientes():
    borrarFrames()
    clientesFrame.pack(fill=BOTH,expand=1)
def stock():
    borrarFrames()
    stockFrame.pack(fill=BOTH,expand=1)
def ventas():
    borrarFrames()
    ventasFrame.pack(fill=BOTH,expand=1)
def compras():
    borrarFramesVentas()
    comprasFrame.pack(fill=BOTH,expand=1)
def carrito():
    borrarFramesVentas()
    carritoFrame.pack(fill=BOTH,expand=1)
def servicios():
    borrarFrames()
    serviciosFrame.pack(fill=BOTH,expand=1)
def ingredientes():
    borrarFramesStock()
    ingredientesFrame.pack(fill=BOTH,expand=1)
def utensilios():
    borrarFramesStock()
    utensiliosFrame.pack(fill=BOTH,expand=1)
def maquinaria():
    borrarFramesStock()
    maquinariaFrame.pack(fill=BOTH,expand=1)

#~~~~~Botones Frame y Clientes~~~~~#
botonesFrame=Frame(bg=colorFondo)
botonesFrame.pack(fill=X)
botonClientes=Button(botonesFrame,text="Clientes",font=("Calibri",12),width=42,bg=colorFondo,fg=colorLetra,relief=FLAT,command=clientes)
botonClientes.pack(side=LEFT)

#~~~~~Botones Stock~~~~~#
botonStock=Button(botonesFrame,text="Stock",font=("Calibri",12),width=42,bg=colorFondo,fg=colorLetra,relief=FLAT,command=stock)
botonStock.pack(side=LEFT)
botonesStockFrame=Frame(stockFrame,bg=colorFondo)
botonesStockFrame.pack(side=LEFT,fill=Y,ipadx=6)
botonIngredientes=Button(botonesStockFrame,text="Ingredientes",font=("Calibri",12),width=14,heigh=3,bg=colorFondo,fg=colorLetra,relief=FLAT,command=ingredientes)
botonIngredientes.pack(fill=X)
botonUtensilios=Button(botonesStockFrame,text="Utensilios",font=("Calibri",12),width=14,heigh=3,bg=colorFondo,fg=colorLetra,relief=FLAT,command=utensilios)
botonUtensilios.pack(fill=X)
botonMaquinaria=Button(botonesStockFrame,text="Maquinaria",font=("Calibri",12),width=14,heigh=3,bg=colorFondo,fg=colorLetra,relief=FLAT,command=maquinaria)
botonMaquinaria.pack(fill=X)

#~~~~~Botones Ventas~~~~~#
botonVentas=Button(botonesFrame,text="Ventas",font=("Calibri",12),width=42,bg=colorFondo,fg=colorLetra,relief=FLAT,command=ventas)
botonVentas.pack(side=LEFT)
botonesVentasFrame=Frame(ventasFrame,bg=colorFondo)
botonesVentasFrame.pack(side=LEFT,fill=Y,ipadx=6)
botonCompras=Button(botonesVentasFrame,text="Ventas",font=("Calibri",12),width=14,heigh=3,bg=colorFondo,fg=colorLetra,relief=FLAT,command=compras)
botonCompras.pack(fill=X)
botonCarrito=Button(botonesVentasFrame,text="Carrito",font=("Calibri",12),width=14,heigh=3,bg=colorFondo,fg=colorLetra,relief=FLAT,command=carrito)
botonCarrito.pack(fill=X)

#~~~~~Botones Servicios#
botonServicios=Button(botonesFrame,text="Servicios",font=("Calibri",12),width=42,bg=colorFondo,fg=colorLetra,relief=FLAT,command=servicios)
botonServicios.pack(side=LEFT)

#~~~~~Frame Clientes~~~~~#
labelBuscarClientes=Label(clientesFrame,text="Buscar",bg=colorClientes,fg="black",font=("Calibri",12))
labelBuscarClientes.pack(anchor=W,padx=20,pady=(10,5))
entryBuscarClientes=Entry(clientesFrame,font=("Calibri",12))
entryBuscarClientes.pack(anchor=W,padx=20,pady=(10,5))

labelClientesId=Label(clientesFrame,text="Id",bg=colorClientes,fg="black",font=("Calibri",12))
labelClientesId.pack(anchor=W,padx=20,pady=(10,5))
entryClientesId=Entry(clientesFrame,font=("Calibri",12))
entryClientesId.pack(anchor=W,padx=20,pady=15)
entryClientesId.config(state="readonly")

labelClientesNombre=Label(clientesFrame,text="Nombre Completo",bg=colorClientes,fg="black",font=("Calibri",12))
labelClientesNombre.pack(anchor=W,padx=20,pady=(10,5))
entryClientesNombre=Entry(clientesFrame,font=("Calibri",12))
entryClientesNombre.pack(anchor=W,padx=20,pady=15)

labelClientesTelefono=Label(clientesFrame,text="Número Telefónico",bg=colorClientes,fg="black",font=("Calibri",12))
labelClientesTelefono.pack(anchor=W,padx=20,pady=(10,5))
entryClientesTelefono=Entry(clientesFrame,font=("Calibri",12))
entryClientesTelefono.pack(anchor=W,padx=20,pady=15)


#~~~~~Buscar Clientes~~~~~#
def buscarClientes():
    if(entryBuscarClientes.get()==""):
        messagebox.showwarning("Sistema","Ingrese algo que buscar")
    else:
        buscar=(entryBuscarClientes.get(),)
        tabla=conexion.cursor()
        tabla.execute("SELECT * FROM clientes WHERE Id=?",buscar)
        datos=tabla.fetchall()
        entryClientesId.config(state="normal")
        entryClientesId.delete(0,END)
        entryClientesNombre.delete(0,END)
        entryClientesTelefono.delete(0,END)
        if(len(datos)>0):
            botonGuardarClientes.config(state="disabled")
            botonModificarClientes.config(state="normal")
            botonEliminarClientes.config(state="normal")
            botonLimpiarClientes.config(state="normal")
            for dato in datos:
                Id=dato[0]
                nombre=dato[1]
                telefono=dato[2]
                entryClientesId.insert(END,Id)
                entryClientesNombre.insert(END,nombre)
                entryClientesTelefono.insert(END,telefono)
        else:
            messagebox.showwarning("Sistema","El cliente no existe")
        entryClientesId.config(state="readonly")
botonBuscarClientes=Button(clientesFrame,text="Buscar",font=("Calibri",14),bg=colorClientes,fg="black",command=buscarClientes)
botonBuscarClientes.pack(side=LEFT,pady=10,padx=20)

#~~~~~Guardar Clientes~~~~~#
def guardarClientes():
    nombre=entryClientesNombre.get()
    telefono=entryClientesTelefono.get()
    if(nombre!="" and telefono!=""):
        datos=(nombre,telefono)
        tabla=conexion.cursor()
        tabla.execute("INSERT INTO clientes(nombre,telefono)VALUES(?,?)",datos)
        conexion.commit()
        messagebox.showinfo("Sistema","Guardado con éxito!")
        limpiarClientes()
        listadoClientes()
    else:
        messagebox.showwarning("Sistema","Complete todos los campos!")
botonGuardarClientes=Button(clientesFrame,text="Guardar",font=("Calibri",14),bg=colorClientes,fg="black",command=guardarClientes)
botonGuardarClientes.pack(side=LEFT,pady=10,padx=20)
botonGuardarClientes.config(state="normal")

#~~~~~Modificar Clientes~~~~~#
def modificarClientes():
    Id=entryClientesId.get()
    nombre=entryClientesNombre.get()
    telefono=entryClientesTelefono.get()
    datos=(nombre,telefono,Id)
    tabla=conexion.cursor()
    tabla.execute("UPDATE clientes SET nombre=?,telefono=? WHERE Id=?",datos)
    conexion.commit()
    messagebox.showinfo("Sistema","Modificado con éxito!")
    limpiarClientes()
    listadoClientes()
    botonGuardarClientes.config(state="normal")
botonModificarClientes=Button(clientesFrame,text="Modificar",font=("Calibri",14),bg=colorClientes,fg="black",command=modificarClientes)
botonModificarClientes.pack(side=LEFT,pady=10,padx=20)
botonModificarClientes.config(state="disabled")

#~~~~~Eliminar Clientes~~~~~#
def eliminarClientes():
    Id=entryClientesId.get()
    datos=(Id,)
    tabla=conexion.cursor()
    tabla.execute("DELETE FROM clientes WHERE Id=?",datos)
    conexion.commit()
    messagebox.showinfo("Sistema","Eliminado con éxito!")
    limpiarClientes()
    listadoClientes()
    botonGuardarClientes.config(state="normal")
botonEliminarClientes=Button(clientesFrame,text="Eliminar",font=("Calibri",14),bg=colorClientes,fg="black",command=eliminarClientes)
botonEliminarClientes.pack(side=LEFT,pady=10,padx=20)
botonEliminarClientes.config(state="disabled")

#~~~~~Limpiar Clientes~~~~~#
def limpiarClientes():
    entryBuscarClientes.delete(0,END)
    entryClientesId.config(state="normal")
    entryClientesId.delete(0,END)
    entryClientesId.config(state="readonly")
    entryClientesNombre.delete(0,END)
    entryClientesTelefono.delete(0,END)
    botonGuardarClientes.config(state="normal")
    botonModificarClientes.config(state="disabled")
    botonEliminarClientes.config(state="disabled")
    botonLimpiarClientes.config(state="disabled")
botonLimpiarClientes=Button(clientesFrame,text="Limpiar",font=("Calibri",14),bg=colorClientes,fg="black",command=limpiarClientes)
botonLimpiarClientes.pack(side=LEFT,pady=10,padx=20)
botonLimpiarClientes.config(state="disabled")

#~~~~~Listado Clientes~~~~~#
def listadoClientes():
    tabla=conexion.cursor()
    tabla.execute("SELECT * FROM clientes ORDER BY Id")
    conexion.commit()
    datos=tabla.fetchall()
    listaClientes.delete(0,END)
    for dato in datos:
        articuloClientes="Id: "+str(dato[0])+" | Nombre: "+str(dato[1])+" | Teléfono: "+str(dato[2])
        listaClientes.insert(END,articuloClientes)
listaClientes=Listbox(clientesFrame,width=43,heigh=27,font=("Arial",12))
listaClientes.place(x=800,y=10)
botonListaClientes=Button(clientesFrame,text="Listado",font=("Calibri",14),bg=colorClientes,fg="black",command=listadoClientes())
botonListaClientes.pack(side=LEFT,pady=10,padx=120)

#~~~~~Frame Ingredientes~~~~~#
labelBuscarProducto=Label(ingredientesFrame,text="Buscar",bg=colorStock,fg="black",font=("Calibri",12))
labelBuscarProducto.pack(anchor=W,padx=20,pady=(10,5))
entryBuscarProducto=Entry(ingredientesFrame,font=("Calibri",12))
entryBuscarProducto.pack(anchor=W,padx=20,pady=(10,5))

labelIngredientesCodigo=Label(ingredientesFrame,text="Código",bg=colorStock,fg="black",font=("Calibri",12))
labelIngredientesCodigo.pack(anchor=W,padx=20,pady=(10,5))
entryIngredientesCodigo=Entry(ingredientesFrame,font=("Calibri",12))
entryIngredientesCodigo.pack(anchor=W,padx=20,pady=(10,5))
entryIngredientesCodigo.config(state="readonly")

labelIngredientesProducto=Label(ingredientesFrame,text="Producto",bg=colorStock,fg="black",font=("Calibri",12))
labelIngredientesProducto.pack(anchor=W,padx=20,pady=(10,5))
entryIngredientesProducto=Entry(ingredientesFrame,font=("Calibri",12))
entryIngredientesProducto.pack(anchor=W,padx=20,pady=(10,5))

labelIngredientesPrecio=Label(ingredientesFrame,text="Precio",bg=colorStock,fg="black",font=("Calibri",12))
labelIngredientesPrecio.pack(anchor=W,padx=20,pady=(10,5))
entryIngredientesPrecio=Entry(ingredientesFrame,font=("Calibri",12))
entryIngredientesPrecio.pack(anchor=W,padx=20,pady=(10,5))

labelIngredientesExistencias=Label(ingredientesFrame,text="Existencias",bg=colorStock,fg="black",font=("Calibri",12))
labelIngredientesExistencias.pack(anchor=W,padx=20,pady=(10,5))
entryIngredientesExistencias=Entry(ingredientesFrame,font=("Calibri",12))
entryIngredientesExistencias.pack(anchor=W,padx=20,pady=(10,5))

#~~~~~Buscar Producto~~~~~#
def buscarProducto():
    if(entryBuscarProducto.get()==""):
        messagebox.showwarning("Sistema","Ingrese algo que buscar")
    else:
        buscar=(entryBuscarProducto.get(),)
        tabla=conexion.cursor()
        tabla.execute("SELECT * FROM ingredientes WHERE codigo=?",buscar)
        datos=tabla.fetchall()
        entryIngredientesCodigo.config(state="normal")
        entryIngredientesCodigo.delete(0,END)
        entryIngredientesProducto.delete(0,END)
        entryIngredientesPrecio.delete(0,END)
        entryIngredientesExistencias.delete(0,END)
        if(len(datos)>0):
            botonGuardarProducto.config(state="disabled")
            botonModificarProducto.config(state="normal")
            botonEliminarProducto.config(state="normal")
            botonLimpiarProducto.config(state="normal")
            for dato in datos:
                codigo=dato[0]
                producto=dato[1]
                precio=dato[2]
                existencias=dato[3]
                entryIngredientesCodigo.insert(END,codigo)
                entryIngredientesProducto.insert(END,producto)
                entryIngredientesPrecio.insert(END,precio)
                entryIngredientesExistencias.insert(END,existencias)
        else:
            messagebox.showwarning("Sistema","El producto no existe")
        entryIngredientesCodigo.config(state="readonly")
botonBuscarProducto=Button(ingredientesFrame,text="Buscar",font=("Calibri",14),bg=colorStock,fg="black",command=buscarProducto)
botonBuscarProducto.pack(side=LEFT,pady=10,padx=20)

#~~~~~Guardar Producto~~~~~#
def guardarProducto():
    producto=entryIngredientesProducto.get()
    precio=entryIngredientesPrecio.get()
    existencias=entryIngredientesExistencias.get()
    if(producto!="" and precio!="" and existencias!=""):
        datos=(producto,precio,existencias)
        tabla=conexion.cursor()
        tabla.execute("INSERT INTO ingredientes(producto,precio,existencias)VALUES(?,?,?)",datos)
        conexion.commit()
        messagebox.showinfo("Sistema","Guardado con éxito!")
        limpiarProducto()
        listadoProducto()
    else:
        messagebox.showwarning("Sistema","Complete todos los campos!")
botonGuardarProducto=Button(ingredientesFrame,text="Guardar",font=("Calibri",14),bg=colorStock,fg="black",command=guardarProducto)
botonGuardarProducto.pack(side=LEFT,pady=10,padx=20)
botonGuardarProducto.config(state="normal")

#~~~~~Modificar Producto~~~~~#
def modificarProducto():
    codigo=entryIngredientesCodigo.get()
    producto=entryIngredientesProducto.get()
    precio=entryIngredientesPrecio.get()
    existencias=entryIngredientesExistencias.get()
    datos=(producto,precio,existencias,codigo)
    tabla=conexion.cursor()
    tabla.execute("UPDATE ingredientes SET producto=?,precio=?,existencias=? WHERE codigo=?",datos)
    conexion.commit()
    messagebox.showinfo("Sistema","Modificado con éxito!")
    limpiarProducto()
    listadoProducto()
    botonGuardarProducto.config(state="normal")
botonModificarProducto=Button(ingredientesFrame,text="Modificar",font=("Calibri",14),bg=colorStock,fg="black",command=modificarProducto)
botonModificarProducto.pack(side=LEFT,pady=10,padx=20)
botonModificarProducto.config(state="disabled")

#~~~~~Eliminar Producto~~~~~#
def eliminarProducto():
    codigo=entryIngredientesCodigo.get()
    datos=(codigo,)
    tabla=conexion.cursor()
    tabla.execute("DELETE FROM ingredientes WHERE codigo=?",datos)
    conexion.commit()
    messagebox.showinfo("Sistema","Eliminado con éxito!")
    limpiarProducto()
    listadoProducto()
    botonGuardarProducto.config(state="normal")
botonEliminarProducto=Button(ingredientesFrame,text="Eliminar",font=("Calibri",14),bg=colorStock,fg="black",command=eliminarProducto)
botonEliminarProducto.pack(side=LEFT,pady=10,padx=20)
botonEliminarProducto.config(state="disabled")

#~~~~~Limpiar Producto~~~~~#
def limpiarProducto():
    entryBuscarProducto.delete(0,END)
    entryIngredientesCodigo.config(state="normal")
    entryIngredientesCodigo.delete(0,END)
    entryIngredientesCodigo.config(state="readonly")
    entryIngredientesProducto.delete(0,END)
    entryIngredientesPrecio.delete(0,END)
    entryIngredientesExistencias.delete(0,END)
    botonGuardarProducto.config(state="normal")
    botonModificarProducto.config(state="disabled")
    botonEliminarProducto.config(state="disabled")
    botonLimpiarProducto.config(state="disabled")
botonLimpiarProducto=Button(ingredientesFrame,text="Limpiar",font=("Calibri",14),bg=colorStock,fg="black",command=limpiarProducto)
botonLimpiarProducto.pack(side=LEFT,pady=10,padx=20)
botonLimpiarProducto.config(state="disabled")

#~~~~~Listado Producto~~~~~#
def listadoProducto():
    tabla=conexion.cursor()
    tabla.execute("SELECT * FROM ingredientes ORDER BY codigo")
    conexion.commit()
    datos=tabla.fetchall()
    listaProducto.delete(0,END)
    for dato in datos:
        articuloProducto="Código: "+str(dato[0])+" | "+str(dato[1])+" $"+str(dato[2])+" | "+str(dato[3])
        listaProducto.insert(END,articuloProducto)
listaProducto=Listbox(ingredientesFrame,width=43,heigh=27,font=("Arial",12))
listaProducto.place(x=800,y=10)
botonListaProducto=Button(ingredientesFrame,text="Listado",font=("Calibri",14),bg=colorStock,fg="black",command=listadoProducto())
botonListaProducto.pack(side=LEFT,pady=10,padx=120)

#~~~~~Frame Utensilios~~~~~#
labelBuscarUtensilios=Label(utensiliosFrame,text="Buscar",bg=colorStock,fg="black",font=("Calibri",12))
labelBuscarUtensilios.pack(anchor=W,padx=20,pady=(10,5))
entryBuscarUtensilios=Entry(utensiliosFrame,font=("Calibri",12))
entryBuscarUtensilios.pack(anchor=W,padx=20,pady=(10,5))

labelUtensiliosCodigo=Label(utensiliosFrame,text="Código",bg=colorStock,fg="black",font=("Calibri",12))
labelUtensiliosCodigo.pack(anchor=W,padx=20,pady=(10,5))
entryUtensiliosCodigo=Entry(utensiliosFrame,font=("Calibri",12))
entryUtensiliosCodigo.pack(anchor=W,padx=20,pady=(10,5))
entryUtensiliosCodigo.config(state="readonly")

labelUtensiliosProducto=Label(utensiliosFrame,text="Producto",bg=colorStock,fg="black",font=("Calibri",12))
labelUtensiliosProducto.pack(anchor=W,padx=20,pady=(10,5))
entryUtensiliosProducto=Entry(utensiliosFrame,font=("Calibri",12))
entryUtensiliosProducto.pack(anchor=W,padx=20,pady=(10,5))

labelUtensiliosPrecio=Label(utensiliosFrame,text="Precio",bg=colorStock,fg="black",font=("Calibri",12))
labelUtensiliosPrecio.pack(anchor=W,padx=20,pady=(10,5))
entryUtensiliosPrecio=Entry(utensiliosFrame,font=("Calibri",12))
entryUtensiliosPrecio.pack(anchor=W,padx=20,pady=(10,5))

labelUtensiliosExistencias=Label(utensiliosFrame,text="Existencias",bg=colorStock,fg="black",font=("Calibri",12))
labelUtensiliosExistencias.pack(anchor=W,padx=20,pady=(10,5))
entryUtensiliosExistencias=Entry(utensiliosFrame,font=("Calibri",12))
entryUtensiliosExistencias.pack(anchor=W,padx=20,pady=(10,5))

#~~~~~Buscar Utensilios~~~~~#
def buscarUtensilios():
    if(entryBuscarUtensilios.get()==""):
        messagebox.showwarning("Sistema","Ingrese algo que buscar")
    else:
        buscar=(entryBuscarUtensilios.get(),)
        tabla=conexion.cursor()
        tabla.execute("SELECT * FROM utensilios WHERE codigo=?",buscar)
        datos=tabla.fetchall()
        entryUtensiliosCodigo.config(state="normal")
        entryUtensiliosCodigo.delete(0,END)
        entryUtensiliosProducto.delete(0,END)
        entryUtensiliosPrecio.delete(0,END)
        entryUtensiliosExistencias.delete(0,END)
        if(len(datos)>0):
            botonGuardarUtensilios.config(state="disabled")
            botonModificarUtensilios.config(state="normal")
            botonEliminarUtensilios.config(state="normal")
            botonLimpiarUtensilios.config(state="normal")
            for dato in datos:
                codigo=dato[0]
                producto=dato[1]
                precio=dato[2]
                existencias=dato[3]
                entryUtensiliosCodigo.insert(END,codigo)
                entryUtensiliosProducto.insert(END,producto)
                entryUtensiliosPrecio.insert(END,precio)
                entryUtensiliosExistencias.insert(END,existencias)
        else:
            messagebox.showwarning("Sistema","El utensilio no existe")
        entryUtensiliosCodigo.config(state="readonly")
botonBuscarUtensilios=Button(utensiliosFrame,text="Buscar",font=("Calibri",14),bg=colorStock,fg="black",command=buscarUtensilios)
botonBuscarUtensilios.pack(side=LEFT,pady=10,padx=20)

#~~~~~Guardar Utensilios~~~~~#
def guardarUtensilios():
    producto=entryUtensiliosProducto.get()
    precio=entryUtensiliosPrecio.get()
    existencias=entryUtensiliosExistencias.get()
    if(producto!="" and precio!="" and existencias!=""):
        datos=(producto,precio,existencias)
        tabla=conexion.cursor()
        tabla.execute("INSERT INTO utensilios(producto,precio,existencias)VALUES(?,?,?)",datos)
        conexion.commit()
        messagebox.showinfo("Sistema","Guardado con éxito!")
        limpiarUtensilios()
        listadoUtensilios()
    else:
        messagebox.showwarning("Sistema","Complete todos los campos!")
botonGuardarUtensilios=Button(utensiliosFrame,text="Guardar",font=("Calibri",14),bg=colorStock,fg="black",command=guardarUtensilios)
botonGuardarUtensilios.pack(side=LEFT,pady=10,padx=20)
botonGuardarUtensilios.config(state="normal")

#~~~~~Modificar Utensilios~~~~~#
def modificarUtensilios():
    codigo=entryUtensiliosCodigo.get()
    producto=entryUtensiliosProducto.get()
    precio=entryUtensiliosPrecio.get()
    existencias=entryUtensiliosExistencias.get()
    datos=(producto,precio,existencias,codigo)
    tabla=conexion.cursor()
    tabla.execute("UPDATE utensilios SET producto=?,precio=?,existencias=? WHERE codigo=?",datos)
    conexion.commit()
    messagebox.showinfo("Sistema","Modificado con éxito!")
    limpiarUtensilios()
    listadoUtensilios()
    botonGuardarUtensilios.config(state="normal")
botonModificarUtensilios=Button(utensiliosFrame,text="Modificar",font=("Calibri",14),bg=colorStock,fg="black",command=modificarUtensilios)
botonModificarUtensilios.pack(side=LEFT,pady=10,padx=20)
botonModificarUtensilios.config(state="disabled")

#~~~~~Eliminar Utensilios~~~~~#
def eliminarUtensilios():
    codigo=entryUtensiliosCodigo.get()
    datos=(codigo,)
    tabla=conexion.cursor()
    tabla.execute("DELETE FROM utensilios WHERE codigo=?",datos)
    conexion.commit()
    messagebox.showinfo("Sistema","Eliminado con éxito!")
    limpiarUtensilios()
    listadoUtensilios()
    botonGuardarUtensilios.config(state="normal")
botonEliminarUtensilios=Button(utensiliosFrame,text="Eliminar",font=("Calibri",14),bg=colorStock,fg="black",command=eliminarUtensilios)
botonEliminarUtensilios.pack(side=LEFT,pady=10,padx=20)
botonEliminarUtensilios.config(state="disabled")

#~~~~~Limpiar Utensilios~~~~~#
def limpiarUtensilios():
    entryBuscarUtensilios.delete(0,END)
    entryUtensiliosCodigo.config(state="normal")
    entryUtensiliosCodigo.delete(0,END)
    entryUtensiliosCodigo.config(state="readonly")
    entryUtensiliosProducto.delete(0,END)
    entryUtensiliosPrecio.delete(0,END)
    entryUtensiliosExistencias.delete(0,END)
    botonGuardarUtensilios.config(state="normal")
    botonModificarUtensilios.config(state="disabled")
    botonEliminarUtensilios.config(state="disabled")
    botonLimpiarUtensilios.config(state="disabled")
botonLimpiarUtensilios=Button(utensiliosFrame,text="Limpiar",font=("Calibri",14),bg=colorStock,fg="black",command=limpiarUtensilios)
botonLimpiarUtensilios.pack(side=LEFT,pady=10,padx=20)
botonLimpiarUtensilios.config(state="disabled")

#~~~~~Listado Utensilios~~~~~#
def listadoUtensilios():
    tabla=conexion.cursor()
    tabla.execute("SELECT * FROM utensilios ORDER BY codigo")
    conexion.commit()
    datos=tabla.fetchall()
    listaUtensilios.delete(0,END)
    for dato in datos:
        articuloUtensilios="Código: "+str(dato[0])+" | "+str(dato[1])+" $"+str(dato[2])+" | "+str(dato[3])
        listaUtensilios.insert(END,articuloUtensilios)
listaUtensilios=Listbox(utensiliosFrame,width=43,heigh=27,font=("Arial",12))
listaUtensilios.place(x=800,y=10)
botonListaUtensilios=Button(utensiliosFrame,text="Listado",font=("Calibri",14),bg=colorStock,fg="black",command=listadoUtensilios())
botonListaUtensilios.pack(side=LEFT,pady=10,padx=120)

#~~~~~Frame Maquinaria~~~~~#
labelBuscarMaquinaria=Label(maquinariaFrame,text="Buscar",bg=colorStock,fg="black",font=("Calibri",12))
labelBuscarMaquinaria.pack(anchor=W,padx=20,pady=(10,5))
entryBuscarMaquinaria=Entry(maquinariaFrame,font=("Calibri",12))
entryBuscarMaquinaria.pack(anchor=W,padx=20,pady=(10,5))

labelMaquinariaCodigo=Label(maquinariaFrame,text="Código",bg=colorStock,fg="black",font=("Calibri",12))
labelMaquinariaCodigo.pack(anchor=W,padx=20,pady=(10,5))
entryMaquinariaCodigo=Entry(maquinariaFrame,font=("Calibri",12))
entryMaquinariaCodigo.pack(anchor=W,padx=20,pady=(10,5))
entryMaquinariaCodigo.config(state="readonly")

labelMaquinariaProducto=Label(maquinariaFrame,text="Producto",bg=colorStock,fg="black",font=("Calibri",12))
labelMaquinariaProducto.pack(anchor=W,padx=20,pady=(10,5))
entryMaquinariaProducto=Entry(maquinariaFrame,font=("Calibri",12))
entryMaquinariaProducto.pack(anchor=W,padx=20,pady=(10,5))

labelMaquinariaPrecio=Label(maquinariaFrame,text="Precio",bg=colorStock,fg="black",font=("Calibri",12))
labelMaquinariaPrecio.pack(anchor=W,padx=20,pady=(10,5))
entryMaquinariaPrecio=Entry(maquinariaFrame,font=("Calibri",12))
entryMaquinariaPrecio.pack(anchor=W,padx=20,pady=(10,5))

labelMaquinariaExistencias=Label(maquinariaFrame,text="Existencias",bg=colorStock,fg="black",font=("Calibri",12))
labelMaquinariaExistencias.pack(anchor=W,padx=20,pady=(10,5))
entryMaquinariaExistencias=Entry(maquinariaFrame,font=("Calibri",12))
entryMaquinariaExistencias.pack(anchor=W,padx=20,pady=(10,5))

#~~~~~Buscar Maquinaria~~~~~#
def buscarMaquinaria():
    if(entryBuscarMaquinaria.get()==""):
        messagebox.showwarning("Sistema","Ingrese algo que buscar")
    else:
        buscar=(entryBuscarMaquinaria.get(),)
        tabla=conexion.cursor()
        tabla.execute("SELECT * FROM maquinaria WHERE codigo=?",buscar)
        datos=tabla.fetchall()
        entryMaquinariaCodigo.config(state="normal")
        entryMaquinariaCodigo.delete(0,END)
        entryMaquinariaProducto.delete(0,END)
        entryMaquinariaPrecio.delete(0,END)
        entryMaquinariaExistencias.delete(0,END)
        if(len(datos)>0):
            botonGuardarMaquinaria.config(state="disabled")
            botonModificarMaquinaria.config(state="normal")
            botonEliminarMaquinaria.config(state="normal")
            botonLimpiarMaquinaria.config(state="normal")
            for dato in datos:
                codigo=dato[0]
                producto=dato[1]
                precio=dato[2]
                existencias=dato[3]
                entryMaquinariaCodigo.insert(END,codigo)
                entryMaquinariaProducto.insert(END,producto)
                entryMaquinariaPrecio.insert(END,precio)
                entryMaquinariaExistencias.insert(END,existencias)
        else:
            messagebox.showwarning("Sistema","La maquinaria no existe")
        entryMaquinariaCodigo.config(state="readonly")
botonBuscarMaquinaria=Button(maquinariaFrame,text="Buscar",font=("Calibri",14),bg=colorStock,fg="black",command=buscarMaquinaria)
botonBuscarMaquinaria.pack(side=LEFT,pady=10,padx=20)

#~~~~~Guardar Maquinaria~~~~~#
def guardarMaquinaria():
    producto=entryMaquinariaProducto.get()
    precio=entryMaquinariaPrecio.get()
    existencias=entryMaquinariaExistencias.get()
    if(producto!="" and precio!="" and existencias!=""):
        datos=(producto,precio,existencias)
        tabla=conexion.cursor()
        tabla.execute("INSERT INTO maquinaria(producto,precio,existencias)VALUES(?,?,?)",datos)
        conexion.commit()
        messagebox.showinfo("Sistema","Guardado con éxito!")
        limpiarMaquinaria()
        listadoMaquinaria()
    else:
        messagebox.showwarning("Sistema","Complete todos los campos!")
botonGuardarMaquinaria=Button(maquinariaFrame,text="Guardar",font=("Calibri",14),bg=colorStock,fg="black",command=guardarMaquinaria)
botonGuardarMaquinaria.pack(side=LEFT,pady=10,padx=20)
botonGuardarMaquinaria.config(state="normal")

#~~~~~Modificar Maquinaria~~~~~#
def modificarMaquinaria():
    codigo=entryMaquinariaCodigo.get()
    producto=entryMaquinariaProducto.get()
    precio=entryMaquinariaPrecio.get()
    existencias=entryMaquinariaExistencias.get()
    datos=(producto,precio,existencias,codigo)
    tabla=conexion.cursor()
    tabla.execute("UPDATE maquinaria SET producto=?,precio=?,existencias=? WHERE codigo=?",datos)
    conexion.commit()
    messagebox.showinfo("Sistema","Modificado con éxito!")
    limpiarMaquinaria()
    listadoMaquinaria()
    botonGuardarMaquinaria.config(state="normal")
botonModificarMaquinaria=Button(maquinariaFrame,text="Modificar",font=("Calibri",14),bg=colorStock,fg="black",command=modificarMaquinaria)
botonModificarMaquinaria.pack(side=LEFT,pady=10,padx=20)
botonModificarMaquinaria.config(state="disabled")

#~~~~~Eliminar Maquinaria~~~~~#
def eliminarMaquinaria():
    codigo=entryMaquinariaCodigo.get()
    datos=(codigo,)
    tabla=conexion.cursor()
    tabla.execute("DELETE FROM maquinaria WHERE codigo=?",datos)
    conexion.commit()
    messagebox.showinfo("Sistema","Eliminado con éxito!")
    limpiarMaquinaria()
    listadoMaquinaria()
    botonGuardarMaquinaria.config(state="normal")
botonEliminarMaquinaria=Button(maquinariaFrame,text="Eliminar",font=("Calibri",14),bg=colorStock,fg="black",command=eliminarMaquinaria)
botonEliminarMaquinaria.pack(side=LEFT,pady=10,padx=20)
botonEliminarMaquinaria.config(state="disabled")

#~~~~~Limpiar Maquinaria~~~~~#
def limpiarMaquinaria():
    entryBuscarMaquinaria.delete(0,END)
    entryMaquinariaCodigo.config(state="normal")
    entryMaquinariaCodigo.delete(0,END)
    entryMaquinariaCodigo.config(state="readonly")
    entryMaquinariaProducto.delete(0,END)
    entryMaquinariaPrecio.delete(0,END)
    entryMaquinariaExistencias.delete(0,END)
    botonGuardarMaquinaria.config(state="normal")
    botonModificarMaquinaria.config(state="disabled")
    botonEliminarMaquinaria.config(state="disabled")
    botonLimpiarMaquinaria.config(state="disabled")
botonLimpiarMaquinaria=Button(maquinariaFrame,text="Limpiar",font=("Calibri",14),bg=colorStock,fg="black",command=limpiarMaquinaria)
botonLimpiarMaquinaria.pack(side=LEFT,pady=10,padx=20)
botonLimpiarMaquinaria.config(state="disabled")

#~~~~~Listado Maquinaria~~~~~#
def listadoMaquinaria():
    tabla=conexion.cursor()
    tabla.execute("SELECT * FROM maquinaria ORDER BY codigo")
    conexion.commit()
    datos=tabla.fetchall()
    listaMaquinaria.delete(0,END)
    for dato in datos:
        articuloMaquinaria="Código: "+str(dato[0])+" | "+str(dato[1])+" $"+str(dato[2])+" | "+str(dato[3])
        listaMaquinaria.insert(END,articuloMaquinaria)
listaMaquinaria=Listbox(maquinariaFrame,width=43,heigh=27,font=("Arial",12))
listaMaquinaria.place(x=800,y=10)
botonListaMaquinaria=Button(maquinariaFrame,text="Listado",font=("Calibri",14),bg=colorStock,fg="black",command=listadoMaquinaria())
botonListaMaquinaria.pack(side=LEFT,pady=10,padx=120)

#~~~~~Frame Servicios~~~~~#
labelBuscarServicios=Label(serviciosFrame,text="Buscar",bg=colorServicios,fg="black",font=("Calibri",12))
labelBuscarServicios.pack(anchor=W,padx=20,pady=(10,5))
entryBuscarServicios=Entry(serviciosFrame,font=("Calibri",12))
entryBuscarServicios.pack(anchor=W,padx=20,pady=(10,5))

labelServiciosCodigo=Label(serviciosFrame,text="Código",bg=colorServicios,fg="black",font=("Calibri",12))
labelServiciosCodigo.pack(anchor=W,padx=20,pady=(10,5))
entryServiciosCodigo=Entry(serviciosFrame,font=("Calibri",12))
entryServiciosCodigo.pack(anchor=W,padx=20,pady=15)
entryServiciosCodigo.config(state="readonly")

labelServicios=Label(serviciosFrame,text="Servicio Pagado",bg=colorServicios,fg="black",font=("Calibri",12))
labelServicios.pack(anchor=W,padx=20,pady=(10,5))
entryServicios=Entry(serviciosFrame,font=("Calibri",12))
entryServicios.pack(anchor=W,padx=20,pady=15)

labelServiciosMes=Label(serviciosFrame,text="Mes",bg=colorServicios,fg="black",font=("Calibri",12))
labelServiciosMes.pack(anchor=W,padx=20,pady=(10,5))
entryServiciosMes=Entry(serviciosFrame,font=("Calibri",12))
entryServiciosMes.pack(anchor=W,padx=20,pady=15)

labelServiciosPrecio=Label(serviciosFrame,text="Precio",bg=colorServicios,fg="black",font=("Calibri",12))
labelServiciosPrecio.pack(anchor=W,padx=20,pady=(10,5))
entryServiciosPrecio=Entry(serviciosFrame,font=("Calibri",12))
entryServiciosPrecio.pack(anchor=W,padx=20,pady=15)

#~~~~~Buscar Servicios~~~~~#
def buscarServicios():
    if(entryBuscarServicios.get()==""):
        messagebox.showwarning("Sistema","Ingrese algo que buscar")
    else:
        buscar=(entryBuscarServicios.get(),)
        tabla=conexion.cursor()
        tabla.execute("SELECT * FROM servicios WHERE codigo=?",buscar)
        datos=tabla.fetchall()
        entryServiciosCodigo.config(state="normal")
        entryServiciosCodigo.delete(0,END)
        entryServicios.delete(0,END)
        entryServiciosMes.delete(0,END)
        entryServiciosPrecio.delete(0,END)
        if(len(datos)>0):
            botonGuardarServicios.config(state="disabled")
            botonModificarServicios.config(state="normal")
            botonEliminarServicios.config(state="normal")
            botonLimpiarServicios.config(state="normal")
            for dato in datos:
                codigo=dato[0]
                servicio=dato[1]
                mes=dato[2]
                precio=dato[3]
                entryServiciosCodigo.insert(END,codigo)
                entryServicios.insert(END,servicio)
                entryServiciosMes.insert(END,mes)
                entryServiciosPrecio.insert(END,precio)
        else:
            messagebox.showwarning("Sistema","El servicio no existe")
        entryServiciosCodigo.config(state="readonly")
botonBuscarServicios=Button(serviciosFrame,text="Buscar",font=("Calibri",14),bg=colorServicios,fg="black",command=buscarServicios)
botonBuscarServicios.pack(side=LEFT,pady=10,padx=20)

#~~~~~Guardar Servicios~~~~~#
def guardarServicios():
    servicio=entryServicios.get()
    mes=entryServiciosMes.get()
    precio=entryServiciosPrecio.get()
    if(servicio!="" and mes!="" and precio!=""):
        datos=(servicio,mes,precio)
        tabla=conexion.cursor()
        tabla.execute("INSERT INTO servicios(servicio,mes,precio)VALUES(?,?,?)",datos)
        conexion.commit()
        messagebox.showinfo("Sistema","Guardado con éxito!")
        limpiarServicios()
        listadoServicios()
    else:
        messagebox.showwarning("Sistema","Complete todos los campos!")
botonGuardarServicios=Button(serviciosFrame,text="Guardar",font=("Calibri",14),bg=colorServicios,fg="black",command=guardarServicios)
botonGuardarServicios.pack(side=LEFT,pady=10,padx=20)
botonGuardarServicios.config(state="normal")

#~~~~~Modificar Servicios~~~~~#
def modificarServicios():
    codigo=entryServiciosCodigo.get()
    servicio=entryServicios.get()
    mes=entryServiciosMes.get()
    precio=entryServiciosPrecio.get()
    datos=(servicio,mes,precio,codigo)
    tabla=conexion.cursor()
    tabla.execute("UPDATE servicios SET servicio=?,mes=?,precio=? WHERE codigo=?",datos)
    conexion.commit()
    messagebox.showinfo("Sistema","Modificado con éxito!")
    limpiarServicios()
    listadoServicios()
    botonGuardarServicios.config(state="normal")
botonModificarServicios=Button(serviciosFrame,text="Modificar",font=("Calibri",14),bg=colorServicios,fg="black",command=modificarServicios)
botonModificarServicios.pack(side=LEFT,pady=10,padx=20)
botonModificarServicios.config(state="disabled")

#~~~~~Eliminar Servicios~~~~~#
def eliminarServicios():
    codigo=entryServiciosCodigo.get()
    datos=(codigo,)
    tabla=conexion.cursor()
    tabla.execute("DELETE FROM servicios WHERE codigo=?",datos)
    conexion.commit()
    messagebox.showinfo("Sistema","Eliminado con éxito!")
    limpiarServicios()
    listadoServicios()
    botonGuardarServicios.config(state="normal")
botonEliminarServicios=Button(serviciosFrame,text="Eliminar",font=("Calibri",14),bg=colorServicios,fg="black",command=eliminarServicios)
botonEliminarServicios.pack(side=LEFT,pady=10,padx=20)
botonEliminarServicios.config(state="disabled")

#~~~~~Limpiar Servicios~~~~~#
def limpiarServicios():
    entryBuscarServicios.delete(0,END)
    entryServiciosCodigo.config(state="normal")
    entryServiciosCodigo.delete(0,END)
    entryServiciosCodigo.config(state="readonly")
    entryServicios.delete(0,END)
    entryServiciosMes.delete(0,END)
    entryServiciosPrecio.delete(0,END)
    botonGuardarServicios.config(state="normal")
    botonModificarServicios.config(state="disabled")
    botonEliminarServicios.config(state="disabled")
    botonLimpiarServicios.config(state="disabled")
botonLimpiarServicios=Button(serviciosFrame,text="Limpiar",font=("Calibri",14),bg=colorServicios,fg="black",command=limpiarServicios)
botonLimpiarServicios.pack(side=LEFT,pady=10,padx=20)
botonLimpiarServicios.config(state="disabled")

#~~~~~Listado Servicios~~~~~#
def listadoServicios():
    tabla=conexion.cursor()
    tabla.execute("SELECT * FROM servicios ORDER BY codigo")
    conexion.commit()
    datos=tabla.fetchall()
    listaServicios.delete(0,END)
    for dato in datos:
        articuloServicios="Código: "+str(dato[0])+" | "+str(dato[1])+" | Mes: "+str(dato[2])+" $"+str(dato[3])
        listaServicios.insert(END,articuloServicios)
listaServicios=Listbox(serviciosFrame,width=43,heigh=27,font=("Arial",12))
listaServicios.place(x=800,y=10)
botonListaServicios=Button(serviciosFrame,text="Listado",font=("Calibri",14),bg=colorServicios,fg="black",command=listadoServicios())
botonListaServicios.pack(side=LEFT,pady=10,padx=120)

#~~~~~Frame Ventas~~~~~#
labelBuscarVentas=Label(comprasFrame,text="Buscar",bg=colorVentas,fg="black",font=("Calibri",12))
labelBuscarVentas.pack(anchor=W,padx=20,pady=(50,5))
entryBuscarVentas=Entry(comprasFrame,font=("Calibri",12))
entryBuscarVentas.pack(anchor=W,padx=20,pady=10)

carrito=[]

#~~~~~Buscar Ventas~~~~~#
def buscarVentas():
    if(entryBuscarVentas.get()==""):
        messagebox.showwarning("Sistema","Ingrese algo que buscar")
    else:
        datos=(entryBuscarVentas.get(),)
        tabla=conexion.cursor()
        tabla.execute("SELECT * FROM ingredientes WHERE codigo=?",datos)
        datosBuscados=tabla.fetchall()
        carrito.append(datosBuscados[0])
        if(len(datos)>0):
            botonLimpiarVentas.config(state="normal")
            botonAgregarProducto.config(state="normal")
            botonLimpiarCarrito.config(state="normal")
            botonVenderProducto.config(state="normal")
            botonTicket.config(state="disabled")
            for dato in datosBuscados:
                texto="Código: "+str(dato[0])+" | "+dato[1]+" $"+str(dato[2])
                listaVentas.insert(END,texto)
        else:
            messagebox.showwarning("Sistema","El producto no existe")
botonBuscarVentas=Button(comprasFrame,text="Buscar",font=("Calibri",14),bg=colorVentas,fg="black",command=buscarVentas)
botonBuscarVentas.pack(anchor=W,padx=20,pady=10)
listaVentas=Listbox(comprasFrame,width=40,heigh=27,font=("Arial",12))
listaVentas.place(x=775,y=43)

def listarVentas():
    tabla=conexion.cursor()
    tabla.execute("SELECT * FROM ingredientes")
    datosBuscados=tabla.fetchall()
    for dato in datosBuscados:
        texto="Código: "+str(dato[0])+" | "+dato[1]+" $"+str(dato[2])
        listaVentas.insert(END,texto)
        botonAgregarProducto.config(state="normal")
        botonLimpiarVentas.config(state="normal")
botonListaVentas=Button(comprasFrame,text="Listado",font=("Calibri",14),bg=colorVentas,fg="black",command=listarVentas)
botonListaVentas.pack(anchor=W,padx=20,pady=10)

def limpiarVentas():
    entryBuscarVentas.delete(0,END)
    listaVentas.delete(0,END)
    carrito=[]
    botonAgregarProducto.config(state="disabled")
    botonLimpiarVentas.config(state="disabled")
botonLimpiarVentas=Button(comprasFrame,text="Limpiar",font=("Calibri",14),bg=colorVentas,fg="black",command=limpiarVentas)
botonLimpiarVentas.pack(anchor=W,padx=20,pady=10)
botonLimpiarVentas.config(state="disabled")

def agregarProducto():
    listarCarrito()
    listaVentas.delete(0,END)
    entryBuscarVentas.delete(0,END)
    botonLimpiarVentas.config(state="disabled")
    botonAgregarProducto.config(state="disabled")
botonAgregarProducto=Button(comprasFrame,text="Agregar a Carrito",font=("Calibri",14),bg=colorVentas,fg="black",command=agregarProducto)
botonAgregarProducto.pack(anchor=W,padx=20,pady=10)
botonAgregarProducto.config(state="disabled")

#~~~~~Carrito~~~~~#
listadoCarrito=Listbox(carritoFrame,width=40,heigh=27,font=("Arial",12))
listadoCarrito.place(x=775,y=43)

def listarCarrito():
    for dato in carrito:
        texto="Código: "+str(dato[0])+" | "+dato[1]+" $"+str(dato[2])+"\n"
        listadoCarrito.insert(END,texto)
        entryDato.delete(0,END)
        entryDato.insert(END,texto)
        botonVenderProducto.config(state="normal")
        botonLimpiarCarrito.config(state="normal")
entryDato=Entry(carritoFrame)
botonListaCarrito=Button(carritoFrame,text="Listado",font=("Calibri",14),bg=colorVentas,fg="black",command=listarCarrito)
botonListaCarrito.pack(anchor=W,padx=20,pady=(50,10))

def limpiarCarrito():
    listadoCarrito.delete(0,END)
    carrito =[] 
    botonVenderProducto.config(state="disabled")
    botonLimpiarCarrito.config(state="disabled")
    botonTicket.config(state="disabled")
botonLimpiarCarrito=Button(carritoFrame,text="Limpiar",font=("Calibri",14),bg=colorVentas,fg="black",command=limpiarCarrito)
botonLimpiarCarrito.pack(anchor=W,padx=20,pady=10)
botonLimpiarCarrito.config(state="disabled")

def venderProducto():
    total=0
    subtotal=0
    for dato in carrito:
        subtotal=subtotal+dato[2]
        total=subtotal*0.21+subtotal
    entryTotal.insert(END,total)
    entrySubtotal.insert(END,subtotal)
    limpiarCarrito()
    botonTicket.config(state="normal")
entryTotal=Entry(carritoFrame)
entrySubtotal=Entry(carritoFrame)
botonVenderProducto=Button(carritoFrame,text="Vender",font=("Calibri",14),bg=colorVentas,fg="black",command=venderProducto)
botonVenderProducto.pack(anchor=W,padx=20,pady=10)
botonVenderProducto.config(state="disabled")

#~~~~~Ticket~~~~~#
def ticket():
    w,h=A4
    x=50
    y=h-50
    pdf=canvas.Canvas("Ticket.pdf",pagesize=A4)
    pdf.setFont("Helvetica",13)
    pdf.setTitle("Ticket de Compra")
    pdf.line(x,y-20,x+490,y-20)
    pdf.drawString(x=50,y=h-50,text="Ticket de Compra")
    
    texto1=pdf.beginText(x=50,y=h-100)
    texto2=pdf.beginText(x=50,y=h-740)
    texto3=pdf.beginText(x=500,y=h-740)

    texto1.textLines(entryDato.get())
    texto1.setFont("Courier",13)
    texto1.textLine("---------------------------------------------------------------")

    texto2.setFont("Helvetica",13)
    texto2.textLine("Subtotal: $")
    texto2.textLine()
    texto2.setFont("Courier",13)
    texto2.textLine("---------------------------------------------------------------")
    texto2.setFont("Helvetica-Bold",16)
    texto2.textLine()
    texto2.textLine("Total: $")

    texto3.setFont("Helvetica",13)
    texto3.textLines(entrySubtotal.get())
    texto3.textLine()
    texto3.textLine()
    texto3.setFont("Helvetica-Bold",16)
    texto3.textLine()
    texto3.textLines(entryTotal.get())
    
    pdf.drawText(texto1)
    pdf.drawText(texto2)
    pdf.drawText(texto3)
    pdf.showPage()
    pdf.save()
    startfile("Ticket.pdf")
botonTicket=Button(carritoFrame,text="Imprimir Ticket",font=("Calibri",14),bg=colorVentas,fg="black",command=ticket)
botonTicket.pack(anchor=W,padx=20,pady=10)
botonTicket.config(state="disabled")

#~~~~~Cierre de ventana~~~~~#
ventana.mainloop()
