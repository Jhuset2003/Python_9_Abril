import tkinter as tk
from tkinter import ttk,messagebox
from tkinter.font import BOLD
import mysql.connector
from tkinter import *

def Buscar ():
    id = e1.get()
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="alma oscura")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "SELECT * FROM personajes_ds WHERE id='"+id+"'"
       mycursor.execute(sql)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("Atencion", "Buscando...")

       datos=listBox.get_children()
       for dato in datos:
           listBox.delete(dato)
       Conexion()

    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()

def Actualizar():
    id = e1.get()
    nombre = e2.get()
    clase = e3.get()
    arma = e4.get()
    armadura = e5.get()
    nivel = e6.get()
 
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="alma oscura")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "UPDATE personajes_ds set nombre='"+nombre+"',id_clase='"+clase+"', id_arma='"+arma+"', id_armaduras='"+armadura+"', nivel='"+nivel+"' where id='"+id+"'"
       val = (id,nombre,clase,arma,armadura,nivel)
       mycursor.execute(sql)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("Atencion", "Actualizando...")

       datos=listBox.get_children()
       for dato in datos:
           listBox.delete(dato)
       Conexion()

    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()
       

    except Exception as e:

       print(e)
       mysqldb.rollback()
       mysqldb.close()
#El dato se elimina a travez del ID
def Eliminar():
    dl = e1.get()

    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="alma oscura")
    mycursor=mysqldb.cursor()

    try:
       sql = "delete from personajes_ds where id = %s"
       val = (dl,)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("Atencion", "Personaje Eliminado.....")
       registros = listBox.get_children()
       for registro in registros:
           listBox.delete(registro)
       Conexion()

    except Exception as e:

       print(e)
       mysqldb.rollback()
       mysqldb.close()

def Agregar():
    id = e1.get()
    nombre = e2.get()
    clase = e3.get()
    arma = e4.get()
    armadura = e5.get()
    nivel = e6.get()
 
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="alma oscura")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "INSERT INTO  personajes_ds (id,nombre,id_clase,id_arma,id_armaduras,nivel) VALUES (%s, %s, %s, %s,%s,%s)"
       val = (id,nombre,clase,arma,armadura,nivel)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("Atencion", "Personaje Creado.....")
       registros = listBox.get_children()
       for registro in registros:
           listBox.delete(registro)
       Conexion()
    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()

consulta_tabla = "SELECT id,nombre,id_clase,id_arma,id_armaduras,nivel FROM personajes_ds"

def Conexion(query = consulta_tabla):
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="alma oscura")
        mycursor = mysqldb.cursor()
        mycursor.execute(query)
        DDC = mycursor.fetchall()
        print(DDC)
 
        for i,(id,nombre,id_clase,id_arma,id_armaduras,nivel) in enumerate(DDC, start=1):
            listBox.insert("", "end", values=(id,nombre,id_clase,id_arma,id_armaduras,nivel))
            mysqldb.close()


root = Tk()
root.geometry("1225x520")
root.config(bg="black")

global e1
global e2
global e3
global e4
global e5
global e6

tk.Label(root, text="CRUD Del Alma Oscura ", fg="white",bg="black", font=(None, 25)).place(x=600, y=70)

tk.Label(root, text="ID",width="10", fg="white", bg="black", font=(None,13) ).place(x=10, y=10)
Label(root, text="Nombre",width="10", fg="white", bg="black", font=(None,13)).place(x=10, y=40)
Label(root, text="Id_Clase",width="10", fg="white", bg="black", font=(None,13)).place(x=10, y=70)
Label(root, text="Id_arma",width="10", fg="white", bg="black", font=(None,13)).place(x=10, y=100)
Label(root, text="Id_Armaduras",width="10", fg="white", bg="black", font=(None,13)).place(x=10, y=130)
Label(root, text="Nivel",width="10", fg="white", bg="black", font=(None,13)).place(x=10, y=160)

e1 = Entry(root)
e1.place(x=140, y=10)
 
e2 = Entry(root)
e2.place(x=140, y=40)
 
e3 = Entry(root)
e3.place(x=140, y=70)
 
e4 = Entry(root)
e4.place(x=140, y=100)

e5 = Entry(root)
e5.place(x=140, y=130)

e6 = Entry(root)
e6.place(x=140, y=160)


Button(root, text="Agregar",fg="white",bg="#1CA73B",font=(None,10,BOLD),command = Agregar,height=2, width= 9).place(x=30, y=200)
Button(root, text="Eliminar",fg="white",bg="#B61515",font=(None,10,BOLD),command = Eliminar,height=2, width= 9).place(x=140, y=200)
Button(root, text="Editar",fg="white",bg="#0035BD",font=(None,10,BOLD),command = Actualizar,height=2, width= 9).place(x=250, y=200)
Button(root, text="Buscar",fg="white",bg="silver",font=(None,10,BOLD),command = Buscar,height=2, width= 9).place(x=360, y=200)

cols = ('id','nombre', 'id_clase','id_arma','id_armaduras','nivel')
listBox = ttk.Treeview(root, columns=cols, show='headings' )

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=270)
Conexion()
 

root.mainloop()