#Importación de librerías:

import tkinter as Tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo

from Proyecto import proyecto
from BaseDatos import BDatos


# Interfaz gráfica con Tkinter:
class App(Tk.Tk):
    
    COLOR_VENTANA = '#1d2d44'

    def __init__(self):
        super().__init__()

        self.codigo = None
        self.config_ventana()
        self.conf_grid()
      
#Mostramos el titulo   
        self.mostrar_titulo()    
# Mostramos formulario 
        self.mostrar_formulario()
#Mostramos la tabla de la tabla
        self.cargar_tabla()
#Nostramos los bortones
        self.mostrar_botones()

    def conf_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
      
    def config_ventana(self):  
        self.title('Gestion de proyectos')
        self.minsize(height=800, width=600)
        self.geometry('900x600')
        self.configure(background=App.COLOR_VENTANA)
# Aplicamos estilo
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam')
        self.estilos.configure(self,
                               background=App.COLOR_VENTANA,
                               foreground='white',
                               fieldbackground='black')

    def mostrar_titulo(self):
        etiqueta = ttk.Label(self, text='Gestion de proyectos', font=('Arial',30), 
                             background=App.COLOR_VENTANA, foreground='white')
        etiqueta.grid(row=0, column=0, columnspan=2, pady=30)

    def mostrar_formulario(self):
        self.frame_f = ttk.Frame()
        #Descripcion
        descripcion_l = ttk.Label(self.frame_f,text='Descripcion')
        descripcion_l.grid(row=0, column=0, sticky=Tk.W, pady=30,padx=5)
        self.descripcion_t = ttk.Entry(self.frame_f)
        self.descripcion_t.grid(row=0, column=1,)
        #tematica
        tematica_l = ttk.Label(self.frame_f,text='tematica')
        tematica_l.grid(row=1, column=0, sticky=Tk.W, pady=30,padx=5)
        self.tematica_t = ttk.Entry(self.frame_f)
        self.tematica_t.grid(row=1, column=1,)
         #academia
        academia_l = ttk.Label(self.frame_f,text='academia')
        academia_l.grid(row=2, column=0, sticky=Tk.W, pady=30,padx=5)
        self.academia_t = ttk.Entry(self.frame_f)
        self.academia_t.grid(row=2, column=1,)
         #prioridad
        prioridad_l = ttk.Label(self.frame_f,text='prioridad')
        prioridad_l.grid(row=3, column=0, sticky=Tk.W, pady=30,padx=5)
        self.prioridad_t = ttk.Entry(self.frame_f)
        self.prioridad_t.grid(row=3, column=1,)
          #Fecha inicio
        fecha_inicio_l = ttk.Label(self.frame_f,text='Fecha desde')
        fecha_inicio_l.grid(row=4, column=0, sticky=Tk.W, pady=30,padx=5)
        self.fecha_inicio_t = ttk.Entry(self.frame_f)
        self.fecha_inicio_t.grid(row=4, column=1,)
          #Fecha inicio
        fecha_fin_l = ttk.Label(self.frame_f,text='Fecha fin')
        fecha_fin_l.grid(row=5, column=0, sticky=Tk.W, pady=30,padx=5)
        self.fecha_fin_t = ttk.Entry(self.frame_f)
        self.fecha_fin_t.grid(row=5, column=1,)

    #Publicamos el Frame
        self.frame_f.grid(row=1, column=0)
   
    def cargar_tabla(self):
        #Creamos un frame para mostrar la tabla de la tab
        self.frame_tabla = ttk.Frame(self)
        # Definimos los estilos de la tabla 
        self.estilos.configure('Treeview', background='black', foreground='white',
                               fieldbackground='black',rowheight=30)
        columnas = ('Descripcion','Tematica''Academia','Prioridad','Fecha inicio','Fecha fin')
        # Creamos el objeto tabla
        self.tabla = ttk.Treeview(self.frame_tabla, columnas=columnas,show='headings')
        
        #DEFINIMOS LAS CABEZERAS
        self.tabla.heading('Descripcion', text= 'Descripción',anchor=Tk.CENTER)
        self.tabla.heading('Tematica', text= 'Tematica',anchor=Tk.W)
        self.tabla.heading('Academia', text= 'Academia',anchor=Tk.W)
        self.tabla.heading('Prioridad', text= 'Prioridad',anchor=Tk.CENTER)
        self.tabla.heading('Fecha inicio', text= 'Fecha inicio',anchor=Tk.CENTER)
        self.tabla.heading('Fecha fin', text= 'Fecha fin',anchor=Tk.CENTER)
        
        #Definimos las columnas
        self.tabla.column('Descripcion', anchor=Tk.CENTER, width=180)
        self.tabla.column('Tematica', anchor=Tk.W, width=120)
        self.tabla.column('Academia', anchor=Tk.W, width=120)
        self.tabla.column('Prioridad', anchor=Tk.CENTER, width=80)
        self.tabla.column('Fecha inicio', anchor=Tk.CENTER, width=80)
        self.tabla.column('Fecha fin', anchor=Tk.CENTER, width=80)

        proyectos = BDatos.seleccionar()
        for c in proyectos:
            self.tabla.insert(parent='',
                        index=Tk.END,
                        values=(c.codigo, c.descripcion, c.tematica, c.academia, c.prioridad, c.fecha_inicio, c.fecha_fin))

        # Agregamos el ScrollBar
        scrollbar = ttk.ScrollBar(self.frame_tabla, orient=Tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0,column=1,sticky=Tk.NS)

        #Mostramos la tabla de la tabla
        self.tabla.grid(row=0, column=0)
        self.frame_tabla.grid(row=1, column=1, padx=30)
 
    def mostrar_botones(self):
        self.frame_b = ttk.Frame()
        #Creamos los botones
        agregar_b = ttk.Button(self.frame_b, text='Guardar',command=self.agregar_datos)
        agregar_b.grid(row=0, column=0, padx=30)

        eliminar_b = ttk.Button(self.frame_b, text='Eliminar',command=self.eliminar_datos)
        eliminar_b.grid(row=0, column=1, padx=30)

        limpiar_b = ttk.Button(self.frame_b, text='Limpiar',command=self.limpiar_datos)
        limpiar_b.grid(row=0, column=2, padx=30)

        # Aplicamos un estilo para los botones
        self.estilos.configure('TButton', background='#005f73')
        self.estilos.map('TButton', background=[('active', '#0a9396')])
        #Piblicamos el Frame
        self.frame_b.grid(row=0, column=2,columnspan=2 ,pady=40)
 
        def agregar_datos(self):
        # Validamos los campos
            if (self.descripcion_t.get() and self.tematica_t.get()
            and self.academia_t.get()):
                showerror(title='Atencion', message='Debe llenar el formulario')
                self.descripcion_t.focus_set()

    
    def guardar_cliente(self):
        # Recuperar los valores de las cajas de texto
        descripcion = self.descripcion_t.get()
        tematica = self.tematica_t.get()
        academia = self.academia_t.get()
        prioridad = self.prioridad_t.get()
        fecha_inicio = self.fecha_inicio_t.get()
        fecha_fin = self.fecha_fin_t.get()

        # Validamos el valor del self.id_cliente
        if self.codigo is None:  # Insertar
            proyecto = BDatos(descripcion=descripcion, tematica=tematica, academia=academia, prioridad=prioridad, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin)
            BDatos.insertar(proyecto)
            showinfo(title='Agregar', message='Proyecto agregado...')
        else:  # Actualizar
            proyecto = BDatos(self.codigo, descripcion, tematica, academia, prioridad, fecha_inicio, fecha_fin)
        BDatos.actualizar(proyecto)
        showinfo(title='Actualizar', message='Protecto actualizado...')
        # Volvemos a mostrar los datos
        self.recargar_datos()

    def cargar_cliente(self, event):
        elemento_seleccionado = self.tabla.selection()[0]
        elemento = self.tabla.item(elemento_seleccionado)
        proyecto_t = elemento['values']  # tupla con los valores
        # Recuperamos cada valor del cliente
        self.codigo = proyecto_t[0]
        descripcion= proyecto_t[1]
        tematica = proyecto_t[2]
        academia = proyecto_t[3]
        prioridad =proyecto_t[4]
        fecha_inicio = proyecto_t[5]
        fecha_fin =proyecto_t[6]
        # Antes de cargar, limpiamos el formulario
        self.limpiar_formulario()
        # Cargar los valores en el formulario
        self.descripcion_t.insert(0, descripcion)
        self.tematica_t.insert(0, tematica)
        self.academia_t.insert(0, academia)
        self.prioridad_t.insert(0, prioridad)
        self.fecha_inicio_t.insert(0, fecha_inicio)
        self.fecha_fin_t.insert(0, fecha_fin)
        
    def recargar_datos(self):
        # volvemos a cargar la tabla
        self.cargar_tabla()
        # limpiamos datos
        self.limpiar_datos()

    def limpiar_datos(self):
        self.limpiar_formulario()
        self.codigo = None

    def limpiar_formulario(self):
        self.descripcion_t.delete(0, tk.END)
        self.tematica_t.delete(0, tk.END)
        self.academia_t.delete(0, tk.END)
        self.prioridad_t.delete(0, tk.END)
        self.fecha_inicio_t.delete(0, tk.END)
        self.fecha_fin_t.delete(0, tk.END)

    def eliminar_cliente(self):
        if self.codigo is None:
            showerror(title='Antencion',
                     message='Debe seleccionar un proyecto a eliminar')
        else:
            proyecto = proyecto(id=self.codigo)
            BDatos.eliminar(proyecto)
            showinfo(title='Eliminado', message='Proyecto eliminado...')
            self.recargar_datos()


 
          

if __name__ == '__main__': 
    app = App()
    app.mainloop()
