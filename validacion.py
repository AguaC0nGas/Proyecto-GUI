import tkinter  as tk 
from tkinter import ttk, messagebox
import re

#crear ventana
ventana = tk.Tk()
ventana.title("Validar datos")
ventana.geometry ("750x500")
ventana.config(bg="#0b4e90")

#titulo
titulo = tk.Label (
    ventana, 
    text="VALIDADOR DE DATOS",
    font=("Arial", 20, "bold"),
    bg="#f1f5f9",
    fg="#1d4ed8"
)
titulo.pack(pady=15)

#Instrucciones
tk.Label(
    ventana,
    text="Introduce los datos y pulsa Validar",
    font=("Arial", 11),
    bg="#f1f5f9"
).pack()

# Formulario
formulario = tk.Frame(ventana, bg="#f1f5f9")
formulario.pack(pady=15)

tk.Label(formulario, text="Nombre:", bg="#f1f5f9").grid(
    row=0, column=0, padx=10, pady=8, sticky="w"
)
nombre = tk.Entry(formulario, width=35)
nombre.grid(row=0, column=1, padx=10, pady=8)

tk.Label(formulario, text="Correo:", bg="#f1f5f9").grid(
    row=1, column=0, padx=10, pady=8, sticky="w"
)
correo = tk.Entry(formulario, width=35)
correo.grid(row=1, column=1, padx=10, pady=8)

tk.Label(formulario, text="Edad:", bg="#f1f5f9").grid(
    row=2, column=0, padx=10, pady=8, sticky="w"
)
edad = tk.Entry(formulario, width=35)
edad.grid(row=2, column=1, padx=10, pady=8)

# Tabla de resultados
tabla = ttk.Treeview(
    ventana,
    columns=("Campo", "Valor", "Resultado"),
    show="headings",
    height=6
)
tabla.heading("Campo", text="Campo")
tabla.heading("Valor", text="Valor")
tabla.heading("Resultado", text="Resultado")

tabla.column("Campo", width=130)
tabla.column("Valor", width=250)
tabla.column("Resultado", width=180)

tabla.pack(padx=20, pady=10, fill="x")

tabla.tag_configure("correcto", foreground="green")
tabla.tag_configure("error", foreground="red")


# Funcion para validar los datos
def validar():
    # Limpiar resultados anteriores
    for fila in tabla.get_children():
        tabla.delete(fila)

    n = nombre.get().strip()
    c = correo.get().strip()
    e = edad.get().strip()

    errores = 0

    # Validar nombre
    if len(n) >= 2 and any(letra.isalpha() for letra in n):
        tabla.insert(
            "", "end",
            values=("Nombre", n, "Correcto"),
            tags=("correcto",)
        )
    else:
        tabla.insert(
            "", "end",
            values=("Nombre", n, "Nombre inválido"),
            tags=("error",)
        )
        errores += 1

    # Validar correo
    patron = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"

    if re.fullmatch(patron, c):
        tabla.insert(
            "", "end",
            values=("Correo", c, "Correcto"),
            tags=("correcto",)
        )
    else:
        tabla.insert(
            "", "end",
            values=("Correo", c, "Correo inválido"),
            tags=("error",)
        )
        errores += 1

    # Validar edad
    try:
        numero = int(e)
        edad_valida = 0 <= numero <= 120
    except ValueError:
        edad_valida = False

    if edad_valida:
        tabla.insert(
            "", "end",
            values=("Edad", e, "Correcto"),
            tags=("correcto",)
        )
    else:
        tabla.insert(
            "", "end",
            values=("Edad", e, "Edad inválida"),
            tags=("error",)
        )
        errores += 1

    # Mostrar resumen
    if errores == 0:
        mensaje.config(
            text="Todos los datos son válidos",
            fg="green"
        )
    else:
        mensaje.config(
            text=f"Se encontraron {errores} errores",
            fg="red"
        )


# Boton
tk.Button(
    ventana,
    text="VALIDAR DATOS",
    command=validar,
    bg="#2563eb",
    fg="white",
    font=("Arial", 11, "bold"),
    padx=20,
    pady=8
).pack(pady=10)

mensaje = tk.Label(
    ventana,
    text="Esperando validación...",
    bg="#f1f5f9",
    font=("Arial", 11, "bold")
)
mensaje.pack(pady=5)

# Ejecutar programa
ventana.mainloop()
