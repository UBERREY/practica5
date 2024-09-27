import tkinter as tk
from tkinter import messagebox
import re

def borrar_valores():
    tbNombre.delete(0, tk.END)
    tbApellido.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    var_genero.set(0)  

def guardar_valores():
    nombre = tbNombre.get()
    apellidos = tbApellido.get()
    telefono = tbTelefono.get()
    edad = tbEdad.get()
    estatura = tbEstatura.get()

    if not TextoValido(nombre):
        messagebox.showerror("Nombre invalido")
        return
    if not TextoValido(apellidos):
        messagebox.showerror("Apellidos invalidos")
        return
    if not TelefonoValido(telefono):
        messagebox.showerror("Telefono invalido")
        return
    if not EdadValido(edad):
        messagebox.showerror("Edad invalida")
        return
    if not EstaturaValido(estatura):
        messagebox.showerror("Estatura invalida en metros")
        return


    genero = "No especificado"
    if var_genero.get() == 1:
        genero = "Hombre"
    elif var_genero.get() == 2:
        genero = "Mujer"


    datos = (f"Nombre: {nombre}\n"
             f"Apellidos: {apellidos}\n"
             f"Telefono: {telefono}\n"
             f"Estatura: {estatura}\n"
             f"Edad: {edad}\n"
             f"Sexo: {genero}\n")


    nombre_archivo = "Registro_datos_python.txt"
    with open(nombre_archivo, "w") as archivo:
        archivo.write(datos)


    messagebox.showinfo("Guardado", "Datos guardados exitosamente.")

def TelefonoValido(valor):
    return valor.isdigit() and len(valor) == 10
def TextoValido(valor):
    return bool(re.match("^[a-zA-Z\s]+$", valor))
def EstaturaValido(valor):
    try:
        return 0.5 <= float(valor) <= 2.5
    except ValueError:
        return False
def EdadValido(valor):
    return valor.isdigit() and 1 <= int(valor) <= 120 

ventana = tk.Tk()
ventana.geometry("520x500")
ventana.title("Formulario: Vr.01")

var_genero = tk.IntVar()


lbNombre = tk.Label(ventana, text="Nombres: ")
lbNombre.pack()
tbNombre = tk.Entry(ventana)
tbNombre.pack()


lbApellido = tk.Label(ventana, text="Apellidos: ")
lbApellido.pack()
tbApellido = tk.Entry(ventana)
tbApellido.pack()


lbTelefono = tk.Label(ventana, text="Telefono: ")
lbTelefono.pack()
tbTelefono = tk.Entry(ventana)
tbTelefono.pack()


lbEdad = tk.Label(ventana, text="Edad: ")
lbEdad.pack()
tbEdad = tk.Entry(ventana)
tbEdad.pack()


lbEstatura = tk.Label(ventana, text="Estatura: ")
lbEstatura.pack()
tbEstatura = tk.Entry(ventana)
tbEstatura.pack()


lbGenero = tk.Label(ventana, text="Genero:")
lbGenero.pack()

rbHombre = tk.Radiobutton(ventana, text="Hombre", variable=var_genero, value=1)
rbHombre.pack()

rbMujer = tk.Radiobutton(ventana, text="Mujer", variable=var_genero, value=2)
rbMujer.pack()


btnBorrar = tk.Button(ventana, text="Borrar valores", command=borrar_valores)
btnBorrar.pack()


btnGuardar = tk.Button(ventana, text="Guardar", command=guardar_valores)
btnGuardar.pack()


ventana.mainloop()