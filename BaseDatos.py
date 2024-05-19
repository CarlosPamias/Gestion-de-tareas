
#Importación de librerías:

import sqlite3

#Definimos ca base de datos:


class BaseDatos:
    def __init__(self, codigo, nombre, estado, fecha_fin):
        self.codigo = codigo
        self.nombre = nombre
        self.estado = estado
        self.fecha_fin = fecha_fin

    def __str__(self):
        return f"{self.codigo}. {self.nombre} ({self.estado}) - Fecha fin: {self.fecha_fin}"

    def como_diccionario(self):
        return {"codigo": self.codigo, "nombre": self.nombre, "estado": self.estado, "fecha_fin": self.fecha_fin}

#Funciones para interactuar con la base de datos:

def conectar_bd():
    try:
        conexion = sqlite3.connect("tareas.db") #Conexion

        cursor = conexion.cursor() # Creamos cursosr
        return conexion, cursor
    except Exception as e:
        mb.showerror("Error", f"Error al conectar a la base de datos: {e}")
        return None, None

def crear_tabla(conexion, cursor):
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tareas (
                código INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                estado TEXT NOT NULL DEFAULT 'Pendiente',
                fecha_fin TEXT
            )
        """)
        conexion.commit() # Guardamos los datos
    except Exception as e:
        mb.showerror("Error", f"Error al crear la tabla: {e}")

def agregar_tarea(conexion, cursor, nombre, estado, fecha_fin):
    try:
        cursor.execute("INSERT INTO tareas (nombre, estado, fecha_fin) VALUES (?, ?, ?)", (nombre, estado, fecha_fin))
        conexion.commit()
        mb.showinfo("Tarea agregada", "La tarea se ha agregado correctamente")
    except Exception as e:
        mb.showerror("Error", f"Error al agregar la tarea: {e}")

def obtener_todas_las_tareas(cursor):
    try:
        cursor.execute("SELECT * FROM tareas")
        tareas_bd = cursor.fetchall()
        tareas = []
        for tarea_bd in tareas_bd:
            tareas.append(Tarea(*tarea_bd))
        return tareas
    except Exception as e:
        mb.showerror("Error", f"Error al obtener las tareas: {e}")
        return []

def modificar_estado_tarea(conexion, cursor, codigo, estado):
    try:
        cursor.execute("UPDATE tareas SET estado = ? WHERE codigo = ?", (estado, codigo))
        conexion.commit()
        mb.showinfo("Tarea modificada", "El estado de la tarea se ha modificado correctamente")
    except Exception as e:
        mb.showerror("Error", f"Error al modificar la tarea: {e}")

def eliminar_tarea(conexion, cursor, codigo):
    try:
        cursor.execute("DELETE FROM tareas WHERE codigo = ?", (codigo,))
        conexion.commit()
        mb.showinfo("Tarea eliminada", "La tarea se ha eliminado correctamente")
    except Exception as e:
        mb.showerror("Error", f"Error al eliminar la tarea: {e}")
