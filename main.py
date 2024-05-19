#Importación de librerías:

from tkinter import Tk, Button, Entry, Label, ttk
from tkinter import StringVar,Scrollbar, Frame, messagebox
from BaseDatos import BDatos as Bd



# Interfaz gráfica con Tkinter:
class Ventana(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.codigo = StringVar()
        self.nombre = StringVar()
        self.descripcion = StringVar()
        self.estado = StringVar()

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0,weight=1)
        self.master.rowconfigure(1,weight=5)
        self.base_datos = Bd()

        self.widgets()

    def widgets(self):
#Creamos el Frame 1 para intorducir los datos y y el frame 2 para seleccionar los datos de la base de datos
        self.frame_uno = Frame(self.master, bg='white', height=200, width=800)
        self.frame_uno.grid(column=0, row=0, sticky='nsew')
        self.frame_dos = Frame(self.master, bg='white', height=300, width=800)
        self.frame_dos.grid(column=0, row=0, sticky='nsew')

        self.frame_uno.columnconfigure([0,1,2], weight=1)
        self.frame_uno.rowconfigure([0,1,2,3,4,5], weight=1)
        self.frame_uno.columnconfigure(0, weight=1)
        self.frame_dos.rowconfigure(0, weight=1)

#Definimos las etiquetas y los botones
        Label(self.frame_uno, text='Opciones', bg='white', fg= 'black',
             font= ('Kaufmann BT','13','bold')).grid(column=2, row=0)
        Button(self.frame_uno, text='REFRESCAR', font= ('Arial', 9, 'bold'), comand=self.actualizar_tabla,
               fg='black', bg= 'white', width=20,bd=3).grid(column=2, row=1, pady=5)


        Label(self.frame_uno, text='Agregar y actualizad datos', bg='white', fg='black',
            font=('Kaufmann BT', '13', 'bold')).grid(columnspan=2,column=0,row=0,pady=5)
        Label(self.frame_uno, text= 'Tematica', fg='black',bg= 'white',
            font=('Rockwell',13,'bols')).grid(column=0,row=1,pady=5)

#creamos las cajas de entrada de la informacion
        Entry(self.frame_uno, textvariable=self.tematica, font=('Comic Sans MS', 12),
              highlightbackground='white',highlightthickness=5).grid(colum=1,row=1)

#creamos los botones para ejecutar acciones
        Button(self.frame_uno,text= 'Añadir datos', font=('arial', 9, 'bold'),bg='white',
               width=20,bd=3,command = self.agregardatos).grid (column=2, row=2, pady=5,padx=5)

#Creamos un estilo de tabla para mostrar la información
        self.tabla[columnas]= ()

    if __name__ == "__main__":
        ventana = Tk()
        ventana.title('Gestion de formación')
        ventana.minsize(height= 400, width=600)
        ventana.geometry('800x500')
        app = Ventana(ventana)
        app.mainloop()