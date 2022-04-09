from tkinter import *
from tkinter import ttk
import mysql.connector as mysql

class Estudiante:
    def __init__(self, ventana):
        self.ventana = ventana

        self.ventana.title('Hola mundo')

        marco = LabelFrame(self.ventana, text='Estudiante')

        marco.grid(row=0, column=0, columnspan=3, pady=20)

        Label(marco, text="Nombre").grid(row=0,column=0)
        self.nombre = Entry(marco)
        self.nombre.grid(row=0,column=1)
        self.nombre.focus()

        Label(marco, text="Clave").grid(row=1,column=0)
        self.clave = Entry(marco)
        self.clave.grid(row=1,column=1)

        self.crear = Button(marco, text="Crear Estudiante" ,bg="green" ,fg="white" ).grid(row=2, column=2, sticky=W+E)

        self.Elminar = Button(marco, text="Eliminar Estudiante" ,bg="red" ,fg="white" ).grid(row=3, column=2, sticky=W+E)

        self.editar = Button(marco, text="Editar Estudiante" ,bg="blue" ,fg="white" ).grid(row=4, column=2, sticky=W+E)
        # self.editar ["state"] = "disabled"


        self.mensaje = Label(text="",fg="green")
        self.mensaje.grid(row=5,column=0,columnspan=2,sticky=W+E)

        Label(self.ventana, text="Buscar Nombre").grid(row=6,column=0)
        self.buscarNombre = Entry(self.ventana)
        self.buscarNombre.grid(row=6,column=1)

        Label(self.ventana, text="Buscar Clave").grid(row=7,column=0)
        self.buscarClave = Entry(self.ventana)
        self.buscarClave.grid(row=7,column=1)


        Button(self.ventana, text="Buscar Estudiante" ,bg="white", fg="black", command=self.buscarRegistro,).grid(row=8, columnspan=2,sticky=W+E)


        self.tabla = ttk.Treeview(self.ventana, columns=2)
        self.tabla.bind("<Double-Button-1>")
        self.tabla.grid(row=9,column=0,columnspan=2)
        self.tabla.heading("#0",text="Nombre",anchor=CENTER)
        self.tabla.heading("#1",text="Clave",anchor=CENTER)
        
        # Entry(marco, text='Guardar estudiante').grid(row=2, columnspan=2, sticky=W+E)
    
    def consultaEstudiante(self, query):
        try:
            self.conn = mysql.connect(host="localhost",user="root",password="",database="colegio")
            print('Conexión establecida')
        except mysql.Error as e:
            print('Error al conectarse a la base de datos', e)

        self.cur = self.conn.cursor()
        self.cur.execute(query)
        return self.cur

    def mostrarDatos(self,where = ""):
        registros = self.tabla.get_children()

        for registro in registros:
            self.tabla.delete(registro) 

        if len(where) > 0:
            cur = self.consultaEstudiante('SELECT `nombre`, `clave` FROM `estudiante`'+ where)
        else:
            cur = self.consultaEstudiante('SELECT `nombre`, `clave` FROM `estudiante`')

        for (nombre, clave) in cur:
            self.tabla.insert('',0,text=nombre,values=clave)

    def buscarRegistro(self):
        where = "where 1 = 1"
        if len(self.buscarNombre.get()) > 0:
            where = where + " and nombre ='"+self.buscarNombre.get()+"'"
        if len(self.buscarClave.get()) > 0:
            where = where + " and clave ='"+self.buscarClave.get()+"'"
        self.mostrarDatos(where)

if __name__ == '__main__':
    ventana = Tk()
    aplicacion = Estudiante(ventana)
    aplicacion.mostrarDatos()
    ventana.mainloop()