from Laptop_Business import laptop_business
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk 
import random

class App:
    def __init__(self,root):
        self.root=root
        self.laptops=[]
        self.imagenes=["C:\\Users\\israe\\Documents\\Programacion\\Modulo 5\\Classes\\img\\6.jpg","C:\\Users\\israe\\Documents\\Programacion\\Modulo 5\\Classes\\img\\7.jpg","C:\\Users\\israe\\Documents\\Programacion\\Modulo 5\\Classes\\img\\8.jpg"]

        root.title("Ingresar Datos Laptops Business")

        self.setup_ui()

    def setup_ui(self):
        ttk.Label(self.root,text="Marca: ").grid(row=0,column=0)
        self.marca=tk.StringVar()
        ttk.Entry(self.root,textvariable=self.marca).grid(row=0,column=1)

        ttk.Label(self.root,text="Procesador: ").grid(row=1,column=0)
        self.procesador=tk.StringVar()
        ttk.Entry(self.root,textvariable=self.procesador).grid(row=1,column=1)

        ttk.Label(self.root,text="Memoria: ").grid(row=2,column=0)
        self.memoria=tk.StringVar()
        ttk.Entry(self.root,textvariable=self.memoria).grid(row=2,column=1)

        ttk.Label(self.root,text="Espacio Disco: ").grid(row=3,column=0)
        self.espacio=tk.StringVar()
        ttk.Entry(self.root,textvariable=self.espacio).grid(row=3,column=1)

        ttk.Label(self.root,text="Duracion Bateria: ").grid(row=4,column=0)
        self.bateria=tk.StringVar()
        ttk.Entry(self.root,textvariable=self.bateria).grid(row=4,column=1)

        ttk.Button(self.root,text="Agregar Laptop Oficina",command=self.agregar_laptop).grid(row=5,column=0)

        self.mostrar_laptops=tk.Text(self.root,height=10,width=50)
        self.mostrar_laptops.grid(row=6,column=0,columnspan=2)

        self.canva=tk.Canvas(self.root,width=200,height=200)
        self.canva.grid(row=2,column=3,rowspan=6)
    
    def agregar_laptop(self):
        nueva_laptop=laptop_business(self.marca.get(),self.procesador.get(),self.memoria.get(),self.espacio.get(),self.bateria.get())
        self.laptops.append(nueva_laptop)
        # print(self.laptops[0])
        self.mostrar_laptops.insert(tk.END,f"{nueva_laptop}")
        self.mostrar_imagen_aleatoria()
        

    def mostrar_imagen_aleatoria(self):
        imagen_path=random.choice(self.imagenes)
        imagen=Image.open(imagen_path)
        imagen=imagen.resize((200,200),Image.Resampling.LANCZOS)
        photo=ImageTk.PhotoImage(imagen)

        self.canva.create_image(0,0, anchor=tk.NW,image=photo)
        self.canva.image=photo

        pass

root=tk.Tk()
app=App(root)
root.mainloop()