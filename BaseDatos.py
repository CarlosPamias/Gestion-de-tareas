
#Importación de librerías:

import sqlite3
from tkinter import messagebox as mb

#Definimos ca base de datos:

class BDatos:

#Inicializamos la tabla
    def __init__(self,):
        self.conexion = sqlite3.connect("tareas.db") #Conexion
      
              
  #Funciones para interactuar con la base de datos:

    def agregar_tarea(self,tematica, academia, prioridad, descripcion, fecha_inicio, fecha_fin_prevista,fecha_fin):
        try:
            cursor = self.conexion.cursor() 
            bd=('''INSERT INTO tareas (descripcion, tematica, academia, prioridad, fecha_inicio, fecha_fin) VALUES ({},{},{},{},{},{})'''.format
                (descripcion, tematica, academia, prioridad, fecha_inicio, fecha_fin_prevista,fecha_fin))
            cursor.execute(bd)
            self.conexion.commit()
            cursor.close()
            mb.showinfo("Tarea agregada", "La tarea se ha agregado correctamente")
        except Exception as e:
            mb.showerror("Error", f"Error al agregar la tarea: {e}")

    def obtener_todas_las_tareas(self):
        try:
            cursor = self.conexion.cursor() 
            bd=("SELECT * FROM tareas")
            cursor.execute(bd)
            datos = cursor.fetchall()
            return datos
        except Exception as e:
            mb.showerror("Error", f"Error al obtener las tareas: {e}")
           
    def modificar_tarea(self,descripcion, codigo,tematica, academia, prioridad, fecha_inicio, fecha_fin_prevista,fecha_fin):
        try:
            cursor = self.conexion.cursor() 
            bd=('''UPDATE tareas SET descripcion= {}, tematica = {}, academia = {}, prioridad = {}, fecha_inicio= {}, fecha_fin_prevista= {},fecha_fin ={} WHERE codigo = {})'''.format
                (descripcion,tematica, academia, prioridad, fecha_inicio, fecha_fin_prevista,fecha_fin,codigo))
            cursor.execute(bd)
            datos = cursor.rowcount
            self.conexion.commit()
            cursor.close()
            return datos
            mb.showinfo("Tarea agregada", "La tarea se ha agregado correctamente")
        except Exception as e:
            mb.showerror("Error", f"Error al agregar la tarea: {e}")


    def eliminar_tarea(self, codigo):
        try:
            cursor = self.conexion.cursor() 
            bd=("DELETE FROM tareas WHERE codigo = {}".format (codigo,))
            cursor.execute(bd)
            self.conexion.commit()
            cursor.close()
            mb.showinfo("Tarea eliminada", "La tarea se ha eliminado correctamente")
        except Exception as e:
            mb.showerror("Error", f"Error al eliminar la base de datos: {e}")
    
    def cerrar_tabla(self):
        try:
            self.conexion.close()
            mb.showinfo("Conexion cerrada", "La conexion se ha cerrado correctamente")
        except Exception as e:
            mb.showerror("Error", f"Error al cerrar la tabla: {e}")