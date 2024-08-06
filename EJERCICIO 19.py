#Capitulo 3. Ejercicio propuesto 19

import tkinter as tk
from tkinter import messagebox
import math

def calcular_triangulo_equilatero(lado):
    perimetro = 3 * lado
    altura = (math.sqrt(3) / 2) * lado
    area = (math.sqrt(3) / 4) * lado ** 2
    return perimetro, altura, area

def calcular():
    try:
        lado = float(entry_lado.get())
        if lado <= 0:
            raise ValueError("El lado debe ser mayor que cero.")
        
        perimetro, altura, area = calcular_triangulo_equilatero(lado)
        
        result_text = (f"El perímetro del triángulo es: {perimetro}\n"
                       f"La altura del triángulo es: {altura}\n"
                       f"El área del triángulo es: {area}")
        messagebox.showinfo("Resultados", result_text)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

ventana = tk.Tk()
ventana.title("Cálculo")

tk.Label(ventana, text="Ingrese la longitud del lado del triángulo equilátero:").pack(pady=10)
entry_lado = tk.Entry(ventana)
entry_lado.pack(pady=5)

tk.Button(ventana, text="Calcular", command=calcular).pack(pady=20)

ventana.mainloop()
