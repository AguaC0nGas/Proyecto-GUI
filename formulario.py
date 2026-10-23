

import tkinter as tk
from tkinter import messagebox

def registrar():
    nombre = caja_nombre.get()
    edad = caja_edad.get()
    correo = caja_correo.get()

    messagebox.showinfo(
        "Registro",
        "Nombre: " + nombre +
        "\nEdad: " + edad +
        "\nCorreo: " + correo
    )

ventana = tk.Tk()
ventana.title("Formulario de Registro")
ventana.geometry("300x250")

tk.Label(ventana, text="Nombre:").pack()
caja_nombre = tk.Entry(ventana)
caja_nombre.pack()

tk.Label(ventana, text="Edad:").pack()
caja_edad = tk.Entry(ventana)
caja_edad.pack()

tk.Label(ventana, text="Correo:").pack()
caja_correo = tk.Entry(ventana)
caja_correo.pack()

tk.Button(
    ventana,
    text="Registrar",
    command=registrar
).pack(pady=10)

ventana.mainloop()


