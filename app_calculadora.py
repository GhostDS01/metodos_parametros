print(" APP DE CALCULADORA")

from cmath import e
from tkinter import * 
import ast

root = Tk() # con esto iniciamos la ventana


root.title("Mi primera Calculadora") # con esto le damos un título a la ventana

display = Entry(root)
display.grid(row = 1, columnspan = 6, sticky=W+E) # con esto creamos la entrada de texto

# aqui voy a crear una funcion para que se empiece a utilizar los botones
i = 0

def obtener_numero(n):
    global i
    display.insert(i, n)
    i+=1

# aqui va las funciones para que las teclas especiales funcionen
def obtener_operador(operator):
    global i
    operator_length = len(operator)
    display.insert(i, operator)
    i+=operator_length

# aqui va una funcion para que se limpie la pantalla de la calculadora
def clear_display():
    display.delete(0, END)

def undo():
    display_state = display.get() # aqui me da el valor actual de la pantalla
    if len(display_state): # si 
        display_new_state = display_state[:-1] # aqui le quito el ultimo valor de lo que se muestra en pantalla
        clear_display() # aqui limpio pantalla
        display.insert(0, display_new_state) # vuelvo a mostrar la pantalla con el valor nuevo
    else:
        clear_display()
        display.insert(0, "MATH ERROR")

# aqui vamos a crear una funcion del igual la cual me va a permitir hacer las operaciones
def calculate():
    display_state = display.get() # obtenemos el valor actual de la pantalla
    try:
        result = eval(display_state) # aqui se compila la expresion
        #result = eval(math_expression) # aqui se evalua la expresion
        clear_display() # aqui limpiamos la pantalla
        display.insert(0, result) # aqui mostramos el resultado
    except Exception as e:
        print(e)
        clear_display()
        display.insert(0, "MATH ERROR")


# Numeric Buttons / en esta parte van a ir los botones
Button(root, text="1", command=lambda:obtener_numero(1)).grid(row = 3, column = 0, sticky=W+E)
Button(root, text="2", command=lambda:obtener_numero(2)).grid(row = 3, column = 1, sticky=W+E)
Button(root, text="3", command=lambda:obtener_numero(3)).grid(row = 3, column = 2, sticky=W+E)

Button(root, text="4", command=lambda:obtener_numero(4)).grid(row = 4, column = 0, sticky=W+E)
Button(root, text="5", command=lambda:obtener_numero(5)).grid(row = 4, column = 1, sticky=W+E)
Button(root, text="6", command=lambda:obtener_numero(6)).grid(row = 4, column = 2, sticky=W+E)

Button(root, text="7", command=lambda:obtener_numero(7)).grid(row = 5, column = 0, sticky=W+E)
Button(root, text="8", command=lambda:obtener_numero(8)).grid(row = 5, column = 1, sticky=W+E)
Button(root, text="9", command=lambda:obtener_numero(9)).grid(row = 5, column = 2, sticky=W+E)

# Buttons Help / botones de ayuda
Button(root, text="AC", command=lambda:clear_display()).grid(row = 6, column = 0, sticky=W+E)
Button(root, text="0", command=lambda:obtener_numero(0)).grid(row = 6, column = 1, sticky=W+E)
Button(root, text="%", command=lambda:obtener_operador('%')).grid(row = 6, column = 2, sticky=W+E)

# botones de operaciones
Button(root, text="+", command=lambda:obtener_operador('+')).grid(row = 3, column = 3,sticky=W+E)
Button(root, text="-", command=lambda:obtener_operador('-')).grid(row = 4, column = 3,sticky=W+E)
Button(root, text="x", command=lambda:obtener_operador('*')).grid(row = 5, column = 3, sticky=W+E)
Button(root, text="/", command=lambda:obtener_operador('/')).grid(row = 6, column = 3, sticky=W+E)

# botones de otras funciones 
# row es un parametro en el metodo grid() que indica la fila en la que se va a colocar el widget
Button(root, text="←", command=lambda:undo()).grid(row = 3, column = 4,sticky=W+E, columnspan = 2)
Button(root, text="exp", command=lambda:obtener_operador('**')).grid(row = 4, column = 4,sticky=W+E)
Button(root, text="^2", command=lambda:obtener_operador('**2')).grid(row = 4, column = 5,sticky=W+E)
Button(root, text="(", command=lambda:obtener_operador('(')).grid(row = 5, column = 4,sticky=W+E)
Button(root, text=")", command=lambda:obtener_operador(')')).grid(row = 5, column = 5,sticky=W+E)
Button(root, text="=", command=lambda:calculate()).grid(row = 6, column = 4,sticky=W+E, columnspan = 2)


root.mainloop() # con esto mantenemos la ventana abierta, ya se ejecuta nuestra app


