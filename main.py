#Importación de librerías:

import tkinter as Tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo

from proyecto import Proyecto
from BaseDatos import BDatos


# Interfaz gráfica con Tkinter:
class App(Tk.Tk):
    
    COLOR_VENTANA = '#DBDFDF'

    def __init__(self):
        super().__init__()

        self.codigo = None
        self.config_ventana()
        self.conf_grid()
        self.mostrar_titulo()    
        self.mostrar_formulario()
        self.cargar_tabla()
        self.mostrar_botones()

 
    def config_ventana(self):  
        self.title('Gestion de proyectos')
        self.geometry('1300x750')
        self.configure(background=App.COLOR_VENTANA)
        self.resizable(0,0)
# Aplicamos estilo
        self.estilos = ttk.Style()
        self.estilos.theme_use('alt')
        self.estilos.configure(self, background=App.COLOR_VENTANA,
                               foreground='black',
                               fieldbackground='white')
        
    
    def conf_grid(self):
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)
      

    def mostrar_titulo(self):
        etiqueta = ttk.Label(self, text='Gestion de proyectos', font=('Algerian',35), 
                             background=App.COLOR_VENTANA, foreground='black')
        etiqueta.grid(row=0, column=0, columnspan=2, pady=30)



    def mostrar_formulario(self):

        self.frame_f = ttk.Frame()

        #Descripcion
        descripcion_l = ttk.Label(self.frame_f,text='Descripcion:',font=('Arial',12))
        descripcion_l.grid(row=1, column=0, sticky=Tk.W, pady=10,padx=5)
        self.descripcion_t = ttk.Entry(self.frame_f)
        self.descripcion_t.grid(row=1, column=1,)
        #tematica
        tematica_l = ttk.Label(self.frame_f,text='Tematica:',font=('Arial',12))
        tematica_l.grid(row=2, column=0, sticky=Tk.W, pady=10,padx=5)
        self.tematica_t = ttk.Entry(self.frame_f)
        self.tematica_t.grid(row=2, column=1,)
         #academia
        academia_l = ttk.Label(self.frame_f,text='Academia:',font=('Arial',12))
        academia_l.grid(row=3, column=0, sticky=Tk.W, pady=10,padx=5)
        self.academia_t = ttk.Entry(self.frame_f)
        self.academia_t.grid(row=3, column=1,)
         #prioridad
        prioridad_l = ttk.Label(self.frame_f,text='Prioridad:',font=('Arial',12))
        prioridad_l.grid(row=4, column=0, sticky=Tk.W, pady=10,padx=5)
        self.prioridad_t = ttk.Entry(self.frame_f)
        self.prioridad_t.grid(row=4, column=1,)
          #Fecha inicio
        fecha_inicio_l = ttk.Label(self.frame_f,text='Fecha desde:',font=('Arial',12))
        fecha_inicio_l.grid(row=5, column=0, sticky=Tk.W, pady=10,padx=5)
        self.fecha_inicio_t = ttk.Entry(self.frame_f)
        self.fecha_inicio_t.grid(row=5, column=1,)
          #Fecha inicio
        fecha_fin_l = ttk.Label(self.frame_f,text='Fecha fin:',font=('Arial',12))
        fecha_fin_l.grid(row=6, column=0, sticky=Tk.W, pady=10,padx=5)
        self.fecha_fin_t = ttk.Entry(self.frame_f)
        self.fecha_fin_t.grid(row=6, column=1,)

    #Publicamos el Frame
        self.frame_f.grid(row=1, column=0)
   
    def cargar_tabla(self):
        #Creamos un frame para mostrar la tabla de la tab
        self.frame_tabla = ttk.Frame(self)
        # Definimos los estilos de la tabla 
        self.estilos.configure('Treeview', background='black', foreground='white',
                               fieldbackground='black',rowheight=25)
        columnas = ('Codigo', 'Descripcion','Tematica','Academia','Prioridad','Fecha inicio','Fecha fin')
        # Creamos el objeto tabla
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas,show='headings')
        
        #DEFINIMOS LAS CABEZERAS
        self.tabla.heading('Codigo', text= 'Codigo',anchor=Tk.N)
        self.tabla.heading('Descripcion', text= 'Descripción',anchor=Tk.NW)
        self.tabla.heading('Tematica', text= 'Tematica',anchor=Tk.NW)
        self.tabla.heading('Academia', text= 'Academia',anchor=Tk.NW)
        self.tabla.heading('Prioridad', text= 'Prioridad',anchor=Tk.NW)
        self.tabla.heading('Fecha inicio', text= 'Fecha inicio',anchor=Tk.N)
        self.tabla.heading('Fecha fin', text= 'Fecha fin',anchor=Tk.N)
        
        #Definimos las columnas
        self.tabla.column('Codigo', anchor=Tk.N, width=60)
        self.tabla.column('Descripcion', anchor=Tk.NW, width=250)
        self.tabla.column('Tematica', anchor=Tk.NW, width=120)
        self.tabla.column('Academia', anchor=Tk.NW, width=120)
        self.tabla.column('Prioridad', anchor=Tk.N, width=80)
        self.tabla.column('Fecha inicio', anchor=Tk.N, width=80)
        self.tabla.column('Fecha fin', anchor=Tk.N, width=80)

        # Cargar los datos de la BD
        proyectos = BDatos.seleccionar()
        for c in proyectos:
            self.tabla.insert(parent='',
                        index=Tk.END,
                        values=(c.codigo, c.descripcion, c.tematica, c.academia, c.prioridad, c.fecha_inicio, c.fecha_fin))

        # Agregamos el ScrollBar
        scrollbar = ttk.Scrollbar(self.frame_tabla, orient=Tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0,column=1,sticky=Tk.NS)

        #Mostramos la tabla de la tabla
        self.tabla.grid(row=0, column=0)
            # Asociamos el evento select
        self.tabla.bind('<<TreeviewSelect>>', self.cargar_cliente)
        # Mostramos el frame
        self.frame_tabla.grid(row=1, column=1, padx=30)
         
    def mostrar_botones(self):
        self.frame_b = ttk.Frame()
        #Creamos los botones
        agregar_b = ttk.Button(self.frame_b, text='Guardar',command=self.guardar_proyecto)
        agregar_b.grid(row=0, column=0, padx=30)

        eliminar_b = ttk.Button(self.frame_b, text='Eliminar',command=self.eliminar_proyecto)
        eliminar_b.grid(row=0, column=1, padx=30)

        limpiar_b = ttk.Button(self.frame_b, text='Limpiar',command=self.limpiar_datos)
        limpiar_b.grid(row=0, column=2, padx=30)

        # Aplicamos un estilo para los botones
        self.estilos.configure('TButton', background='#005f73')
        self.estilos.map('TButton', background=[('active', '#0a9396')])
        #Piblicamos el Frame
        self.frame_b.grid(row=2, column=0,columnspan=2 ,pady=30)
 
    def agregar_datos(self):
        # Validamos los campos
        if (self.descripcion_t.get() and self.tematica_t.get()
            and self.academia_t.get()):
            showerror(title='Atencion', message='Debe llenar el formulario')
            self.descripcion_t.focus_set()

    
    def guardar_proyecto(self):
        # Recuperar los valores de las cajas de texto
        descripcion = self.descripcion_t.get()
        tematica = self.tematica_t.get()
        academia = self.academia_t.get()
        prioridad = self.prioridad_t.get()
        fecha_inicio = self.fecha_inicio_t.get()
        fecha_fin = self.fecha_fin_t.get()

        # Validamos el valor del self.id_cliente
        if self.codigo is None:  # Insertar
            proyecto = Proyecto(descripcion=descripcion, tematica=tematica, academia=academia, prioridad=prioridad, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin)
            BDatos.insertar(proyecto)
            showinfo(title='Agregar', message='Proyecto agregado...')
        else:  # Actualizar
            proyecto = Proyecto(self.codigo, descripcion, tematica, academia, prioridad, fecha_inicio, fecha_fin)
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
        self.descripcion_t.delete(0, Tk.END)
        self.tematica_t.delete(0, Tk.END)
        self.academia_t.delete(0, Tk.END)
        self.prioridad_t.delete(0, Tk.END)
        self.fecha_inicio_t.delete(0, Tk.END)
        self.fecha_fin_t.delete(0, Tk.END)

    def eliminar_proyecto(self):
        if self.codigo is None:
            showerror(title='Antencion',
                     message='Debe seleccionar un proyecto a eliminar')
        else:
            proyecto = Proyecto(codigo=self.codigo)
            BDatos.eliminar(proyecto)
        #    showinfo(title='Eliminado', message='Proyecto eliminado...')
            self.recargar_datos()


         

if __name__ == '__main__': 
    app = App()
    app.mainloop()
