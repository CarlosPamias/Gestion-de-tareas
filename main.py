#Importación de librerías:
from Cliente.Pantalla import Frame
import tkinter as Tk

def main():
    root = Tk.Tk()
    root.title('Gestion de formación')
     
    app = Frame(root=root)
    app.mainloop()

if __name__ == "__main__":
    main()