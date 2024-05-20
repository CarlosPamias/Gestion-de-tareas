#Importación de librerías:

from tkinter import Tk, Button, Entry, Label
from tkinter import ttk
from tkinter import StringVar,Scrollbar, Frame, messagebox
from BaseDatos import BDatos as Bd


# Interfaz gráfica con Tkinter:
class App(Tk):
    
    COLOR_VENTANA = '#1d2d44'

    def __init__(self):
        super().__init__()

# Configuramos la ventana
        self.config_ventana()
# configuramos el Grid
        self.conf_grid()
# Mostramos las ventana
        self.mostrar_ventana
#Mostramos el titulo   
        self.mostrar_titulo    
# Mostramos formulario 
        self.mostrar_formulario()
#Mostramos la tabla de la tabla
        self.mostrar_tabla()

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
        #nombres
        descripcion_l = ttk.Label(self.frame_f,text='Descripcion')
        descripcion_l.grid(row=0, column=0, sticky=Tk.W, pady=30,padx=5)
        self.descripcion_t = ttk.Entry(self.frame_f)
        self.descripcion_t.grid(row=0, column=1,)


    #Publicamos el Frame
        self.frame_f.grid(row=1, column=0)
   
    def mostrar_tabla(self):
        #Creamos un frame para mostrar la tabla de la tab
        self.frame_tabla = ttk.Frame(self)
        self.estilos.configure('Treeview', background='black', foreground='white',
                               fieldbackground='black',rowheight=30)
        columnas = ('DescripciÓn','Tematica''Academia','Prioridad','Fecha inicio','Fecha fin')
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

        self.actualizar_datos

        # Agregamos el ScrollBar
        scrollbar = ttk.ScrollBar(self.frame_tabla, orient=Tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0,column=1,sticky=Tk.NS)

        #Mostramos la tabla de la tabla
        self.tabla.grid(row=0, column=0)
        self.frame_tabla.grid(row=1, column=1, padx=30)
 
   
 

    def obtener_fila(self,event):
        item = self.tabla.focus()
        self.data =self.tabla.item(item)
        self.descripcion.set(self.data['text'])
        self.tematica.set(self.data['values'][0])
        self.acadeSmia.set(self.data['values'][1])
        self.prioridad.set(self.data['values'][2])
        self.descripcion.set(self.data['values'][3])
        self.fecha_inicio.set(self.data['values'][4])
        self.fecha_fin.set(self.data['values'][5])

    def eliminar_datos(self, event):
        self.limpiar_datos()
        item = self.tabla.selection()[0]
        x = messagebox.askquestion('Informacion', '¿Desea eliminar?')
        if x == 'yes':
            self.tabla.delete(item)
            self.Bd.eliminar_tarea(self.data['text'])
            
    def agregar_datos(self):
        descripcion = self.descripcion.get()
        tematica = self.tematica.get()
        academia = self.academia.get()
        prioridad = self.prioridad.get()
        fecha_inicio = self.fecha_inicio.get()
        fecha_fin = self.fecha_fin.get()
        datos = (descripcion,tematica,academia,prioridad,fecha_inicio,fecha_fin)
        if tematica and academia and prioridad and descripcion != ' ':
            self.tabla.insert('',0,text = tematica, value = datos)
            self.Bd.agregar_tarea(tematica, academia,prioridad,fecha_inicio,fecha_fin)
            self.limpiar_campos()
        
    def actualizar_tabla(self):
        self.limpiar_campos()
        datos = self.Bd.obtener_todas_las_tareas()
        self.tabla.delete(*self.tabla.get_children())
        i = -1
        for dato in datos:
            i=i+1
            self.tabla.insert('', i,text=datos[i][1:2][0], values=datos[i][2:7])
    
    def actualizar_datos(self):
        item = self.tabla.focus()
        self.data = self.data.item(item)
        nombre = self.tabla['text']
        datos = self.Bd.obtener_todas_las_tareas()
        for fila in datos:
            codigo = fila[0]
            tematica_db = fila[1]
            if tematica_db == tematica:
                if codigo != None:
                    descripcion =self.descripcion.get()
                    tematica =self.tematica.get()
                    academia =self.academia.get()
                    prioridad =self.prioridad.get()
                    fecha_inicio =self.fecha_inicio.get()
                    fecha_fin =self.fecha_fin.get()
                    if tematica and academia and prioridad and descripcion != '':
                        self.Bd.modificar_tarea(codigo,descripcion,tematica,prioridad,fecha_inicio,fecha_fin)
                        self.tabla.delete(*self.tabla.get_children())
                        datos = self.Bd.obtener_todas_las_tareas()
                        i = -1
                        for dato in datos:
                            i=i+1
                            self.tabla.insert('', i,text=datos[i][1:2][0], values=datos[i][2:7])
    
    def limpiar_campos(self):
        self.descripcion.set('')
        self.tematica.set('')
        self.academia.set('')
        self.prioridad.set('')
        self.fecha_inicio.set('')
        self.fecha_fin.set('')

          

if __name__ == '__main__': 
    app = App()
    app.mainloop()
