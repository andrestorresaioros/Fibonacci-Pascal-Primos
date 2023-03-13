import tkinter as tk
from tkinter import *
num1= int(input("Filas: "))+1
num2= int(input("Columnas: "))+1
nax= int(input("Fila A: "))
nay= int(input("Columna A: "))
nbx= int(input("Fila B: "))
nby= int(input("Columna B: "))
root = Tk()
for r in range(1, num1):
    for c in range(1, num2):
        cell = Entry(root, width=10,fg='red')
        cell.grid(padx=num1, pady=num2, row=r, column=c)
        cell.config(state=tk.DISABLED)
        if(nax==r and nay==c):
            cell.config(state=tk.NORMAL)
            cell.insert(0, "A")
        elif(nbx==r and nby==c):
            cell.config(state=tk.NORMAL)
            cell.insert(0, "B")
root.mainloop()
num1=num1-1
num2=num2-1
rutas=((num1+num2)*((num1+num2)-1))/2
print("La cantidad de rutas para ir de A a B son: ",rutas)