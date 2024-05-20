#Importación de librerías:

from tkinter import Tk, Button, Entry, Label, ttk
from tkinter import StringVar,Scrollbar, Frame, messagebox
from BaseDatos import BDatos as Bd


# Interfaz gráfica con Tkinter:
class Product(Frame):
    def __init__(self, master):
        super().__init__( master)
       
        self.descripcion = StringVar()
        self.tematica = StringVar()
        self.academia = StringVar()
        self.prioridad = StringVar()        
        self.fecha_inicio = StringVar()
        self.fecha_fin =  StringVar()

#       Adaptamos la pantalla
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0,weight=1)
        self.master.rowconfigure(1,weight=5)
        self.Bd = Bd()

        self.widgets()

    def widgets(self):
#Creamos el Frame 1 para intorducir los datos y y el frame 2 para seleccionar los datos de la base de datos
        self.frame_uno = Frame(self.master,bg='white', height=200, width=800)
        self.frame_uno.grid(column=0, row=0, sticky='nsew')
        self.frame_dos = Frame(self.master,bg='white', height=300, width=800)
        self.frame_dos.grid(column=0, row=1, sticky='nsew')

        self.frame_uno.columnconfigure([0,1,2], weight=1)
        self.frame_uno.rowconfigure([0,1,2,3,4,5], weight=1)
        self.frame_dos.columnconfigure(0, weight=1)
        self.frame_dos.rowconfigure(0, weight=1)

#Definimos las etiquetas y los botones
  
        Label(self.frame_uno, text='Agregar y actualizad datos', bg='white', fg='black',
            font=('Kaufmann BT', '13', 'bold')).grid(columnspan=2,column=0,row=0,pady=5)
        
        Label(self.frame_uno, text= 'Descripcion', fg='black',bg= 'white',
            font=('Rockwell',13,'bold')).grid(column=0,row=1,pady=5)
        Label(self.frame_uno, text= 'Tematica', fg='black',bg= 'white',
            font=('Rockwell',13,'bold')).grid(column=0,row=2,pady=5)
        Label(self.frame_uno, text= 'Academia', fg='black',bg= 'white',
            font=('Rockwell',13,'bold')).grid(column=0,row=3,pady=5)
        Label(self.frame_uno, text= 'Prioridad', fg='black',bg= 'white',
            font=('Rockwell',13,'bold')).grid(column=0,row=4,pady=5)
        Label(self.frame_uno, text= 'Fecha inicio', fg='black',bg= 'white',
            font=('Rockwell',13,'bold')).grid(column=0,row=5,pady=5)
        Label(self.frame_uno, text= 'Fecha Fin', fg='black',bg= 'white',
            font=('Rockwell',13,'bold')).grid(column=0,row=6,pady=5)    

#creamos las cajas de entrada de la informacion
        Entry(self.frame_uno, textvariable=self.descripcion, font=('Comic Sans MS', 12),
              highlightbackground='white',highlightthickness=5).grid(colum=1,row=1)
        Entry(self.frame_uno, textvariable=self.tematica, font=('Comic Sans MS', 12),
              highlightbackground='white',highlightthickness=5).grid(colum=1,row=2)
        Entry(self.frame_uno, textvariable=self.academia, font=('Comic Sans MS', 12),
              highlightbackground='white',highlightthickness=5).grid(colum=1,row=3)
        Entry(self.frame_uno, textvariable=self.prioridad, font=('Comic Sans MS', 12),
              highlightbackground='white',highlightthickness=5).grid(colum=1,row=4)
        Entry(self.frame_uno, textvariable=self.fecha_inicio, font=('Comic Sans MS', 12),
              highlightbackground='white',highlightthickness=5).grid(colum=1,row=5)
        Entry(self.frame_uno, textvariable=self.fecha_fin_prevista, font=('Comic Sans MS', 12),
              highlightbackground='white',highlightthickness=5).grid(colum=1,row=6)

#creamos los botones para ejecutar acciones
        Label(self.frame_uno, text='Opciones', bg='white', fg= 'black',
             font= ('Kaufmann BT','13','bold')).grid(column=2, row=0)
        Button(self.frame_uno, text='REFRESCAR', font= ('Arial', 9, 'bold'), comand=self.actualizar_tabla,
               fg='black', bg= 'white', width=20,bd=3).grid(column=2, row=1, pady=5)
        Button(self.frame_uno,text= 'Añadir datos', font=('arial', 9, 'bold'),bg='white',
               width=20,bd=3,command = self.agregar_datos).grid (column=2, row=2, pady=5,padx=5)
        Button(self.frame_uno,text= 'Modificar', font=('arial', 9, 'bold'),bg='white',
               width=20,bd=3,command = self.actualizar_datos).grid (column=2, row=3, pady=5,padx=5)
        Button(self.frame_uno,text= 'Limpiar', font=('arial', 9, 'bold'),bg='white',
               width=20,bd=3,command = self.limpiar_campos).grid (column=2, row=3, pady=5,padx=5)
#creamos el estilo de la tabla 
        estilo_tabla = ttk.Style()
        estilo_tabla.configure('Treeview', font= ('Helvetia', 10, 'bold'), foreground='black', background='white')
        estilo_tabla.map('Treeview',background=['selected', 'white'],foreground=['selected', 'black'])
        estilo_tabla.configure('Heading',background='white',foreground= 'black', padding=3,font=('Arial', 10, 'bold'),)
#Creamos un estilo de tabla para mostrar la información
        self.tabla = ttk.Treeview(self.frame_dos)
        self.tabla.grid(column=0, row=0, sticky='nsew')
        ladox= ttk.Scrollbar(self.frame_dos,orient='horizontal',command=self.tabla.xview)
        ladox.grid(column=0,row=1,sticky='ew')
        ladoy= ttk.Scrollbar(self.frame_dos,orient='vertical',command=self.tabla.yview)
        ladoy.grid(column=1,row=0,sticky='ns')
        self.tabla.configure(xscrollcommand= ladox.set, yscrollcommand= ladoy.set)

        self.tabla['columns'] = ('Descripción','Tematica''Academia','Prioridad','Fecha inicio','Fecha fin')
        self.tabla.column('#0', minwidth='100',width=120, anchor='center')
        self.tabla.column('Descripcion', minwidth='100',width=120, anchor='center')
        self.tabla.column('Tematica', minwidth='100',width=120, anchor='center')
        self.tabla.column('Academia', minwidth='100',width=120, anchor='center')
        self.tabla.column('Prioridad', minwidth='100',width=120, anchor='center')
        self.tabla.column('Fecha inicio', minwidth='100',width=120, anchor='center')
        self.tabla.column('Fecha fin', minwidth='100',width=120, anchor='center')

        self.tabla.heading('#0', text='Descripcion', anchor='centre')
        self.tabla.heading('Academia', text='Academia', anchor='centre')
        self.tabla.heading('Prioridad', text='Prioridad', anchor='centre')
        self.tabla.heading('Tematica', text='Tematica', anchor='centre')
        self.tabla.heading('Fecha inicio', text='Fecha inicio', anchor='centre')
        self.tabla.heading('Fecha fin', text='Fecha fin', anchor='centre')

        self.tabla.bind('<<TreeviewSelect>>', self.obtener_fila)
        self.tabla.bind('<Doble-1>', self.eliminar_datos)

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
                    tematica =self.tematica.get()
                    academia =self.academia.get()
                    prioridad =self.prioridad.get()
                    descripcion =self.descripcion.get()
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

if __name__ == "__main__":
    ventana = Tk()
    ventana.title('Gestion de proyectos')
    ventana.minsize(height=400, width=600)
    ventana.geometry('800x600')
    aplication = Product(ventana)
    aplication.mainloop()        
   
