
#Importación de librerías:

import sqlite3
from tkinter import messagebox as mb

#Definimos ca base de datos:

class BDatos:

    def __init__(self, codigo, tematica, academia, prioridad, descripcion, fecha_inicio, fecha_fin_prevista):
        self.codigo = codigo
        self.tematica = tematica
        self.academia = academia
        self.prioridad = prioridad
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin_prevista = fecha_fin_prevista
        self.fecha_fin = None  # Inicialmente sin fecha de finalización

        self.conexion = sqlite3.connect("tareas.db") #Conexion
        cursor = self.conexion.cursor() # Creamos cursos
        cursor.execute('''CREATE TABLE IF NOT EXISTS tareas (
                        codigo INTEGER PRIMARY KEY,
                        tematica TEXT,
                        Academia TEXT,
                        Prioridad TEXT,
                        Descripcion TEXT,
                        FechaInicio DATE,
                        FechaFinPrevista DATE,
                        FechaFin DATE,
                    
                    )''')
        self.conexion.commit()  # Guardamos los datos
        cursor.close()
              
  #Funciones para interactuar con la base de datos:

    def agregar_tarea(self,tematica, academia, prioridad, descripcion, fecha_inicio, fecha_fin_prevista):
        try:
            cursor = self.conexion.cursor() 
            bd=('''INSERT INTO tareas (tematica, academia, prioridad, descripcion, fecha_inicio, fecha_fin_prevista) VALUES ({},{},{},{},{},{})'''.format
                (tematica, academia, prioridad, descripcion, fecha_inicio, fecha_fin_prevista))
            cursor.execute(bd)
            self.conexion.commit()
            cursor.close()
            mb.showinfo("Tarea agregada", "La tarea se ha agregado correctamente")
        except Exception as e:
            mb.showerror("Error", f"Error al agregar la tarea: {e}")

    def obtener_todas_las_tareas(cursor):
        try:
            cursor = self.conexion.cursor() 
            bd=("SELECT * FROM tareas")
            cursor.execute(bd)
            datos = cursor.fetchall()
            return datos
        except Exception as e:
            mb.showerror("Error", f"Error al obtener las tareas: {e}")
           
     def modificar_tarea(self,codigo,tematica, academia, prioridad, descripcion, fecha_inicio, fecha_fin_prevista):
        try:
            cursor = self.conexion.cursor() 
            bd=('''UPDATE tareas SET tematica = {}, academia = {}, prioridad = {}, descripcion= {}, fecha_inicio= {}, fecha_fin_prevista= {}WHERE codigo = {})'''.format
                (tematica, academia, prioridad, descripcion, fecha_inicio, fecha_fin_prevista,codigo))
            cursor.execute(bd)
            self.conexion.commit()
            cursor.close()
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