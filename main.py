#Importación de librerías:
from Cliente.Pantalla import Product
import tkinter as Tk


if __name__ == "__main__":
    window = Tk.Tk()
    aplication = Product(window)
    window.mainloop()