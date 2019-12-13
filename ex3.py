"""
Cet exercice consiste à réaliser une interface graphique qui trace x(t) et y(t) de l’exercice précédent,
mais cette fois on peut sélectionner si on veut afficher juste x(t) ou y(t) ou bien les 2.

"""

import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np
from PIL import Image, ImageTk


def R(t):
    if t>0: 
        return t
    else: 
        return 0
def X(t):
     x = [ ]
     y = [ ]
     i = 0
     Ak = [1, -2, 1, -1, 1]
     Tk = [0, 3, 4, 6, 8]
     for j in t:
          s1 = 0
          s2 = 0
          for i in range( 5 ):  # Pour calculer la somme x(t) et y(t)
               s1 += ( Ak[ i ] * R( j - Tk[ i ] ) ) 
               s2 += ( Ak[ i ] * R( ( - 4 * j ) + 8 - Tk [ i ] ) )
          x.append(s1) # Ajouter la valeur s1 a la fin de la liste x 
          y.append(s2) # Ajouter la valeur s2 a la fin de la liste y 
     return [x,y] 

root = tkinter.Tk()
root.wm_title("TP - EX - 3")
T = np.linspace(0 , 9 , 1000) 
F = X(T)
fig = Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)




def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate
def _plotX():
    fig.clf()
    fig.add_subplot(111).plot(T,F[0], ls='-', label = "x(t)", c = "green")

    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    canvas.mpl_connect("key_press_event", on_key_press)

def _plotY():
    fig.clf()
    fig.add_subplot(111).plot(T,F[1], ls='-', label = "y(t)", c = "blue")
    
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    canvas.mpl_connect("key_press_event", on_key_press) 

def _plotXY():
    
    fig.clf() 
    fig.add_subplot(111).plot(T,F[0], ls='-', label = "x(t)", c = "green")
    fig.add_subplot(111).plot(T,F[1], ls='--', label = "y(t)", c = "blue")

    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    canvas.mpl_connect("key_press_event", on_key_press) 
    


_plotX()
signalYBtn = tkinter.Button(master=root, text="X(t)", command=_plotX)
signalXBtn = tkinter.Button(master=root, text="Y(t)", command=_plotY) 
signalXYBtn = tkinter.Button(master=root, text="X(t) et Y(t)", command=_plotXY)
text = tkinter.Label(root, text="BY Ibrahim EL MOUNTASSER et Mohamed Amine FAROUQ  - FST SETTAT")
text.config(height = 6) 
button = tkinter.Button(master=root, text="Quit", command=_quit)
signalXBtn.config(width = 40 )
signalYBtn.config(width = 40 )
signalXYBtn.config(width = 40 )
button.config(width = 40 )
text.pack(side=tkinter.BOTTOM)
button.pack(side=tkinter.BOTTOM)
signalXYBtn.pack(side=tkinter.BOTTOM)
signalXBtn.pack(side=tkinter.BOTTOM)
signalYBtn.pack(side=tkinter.BOTTOM)
tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.
