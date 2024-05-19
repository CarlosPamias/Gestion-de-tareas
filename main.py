#Importación de librerías:

import tkinter as tk
from tkinter import messagebox as mb

# Interfaz gráfica con Tkinter:

#Creamos una ventana
ventana = tk.Tk

#Redimensionamos la ventana
ventana.geometry('900x600')

#Evitamos redimensionar la ventana
ventana.resizable(0,0)

#Modificamos el Titulo
ventana.title('Gestion de tareas')


#Hacemos visible la ventana
ventana.mainloop()



def actualizar_lista_tareas():
    tareas = obtener_todas_las_tareas(cursor)
    lista_tareas.delete(0, tk.END)
    for tarea in tareas:
        lista_tareas.insert(tk.END, tarea)


def agregar_tarea():
    nombre = ventana_agregar_tarea.entry_nombre.get()
    estado = ventana_agregar_tarea.var_estado.get()
    fecha_fin = ventana_agregar_tarea.entry_fecha_fin.get()

    if not nombre or not fecha_fin:
        mb.showwarning("Error", "Debes completar todos los campos")
        return

    agregar_tarea(conexion, cursor, nombre, estado, fecha_fin)
    actualizar_lista_tareas()
    ventana_agregar_tarea.destroy()


def marcar_completada():
    try:
        indice = lista_tareas.curselection()[0]
        codigo = tareas[indice].codigo

