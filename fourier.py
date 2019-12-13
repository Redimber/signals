import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np
from PIL import Image, ImageTk


def S(T,n):
    s=[]
    for t in T:
        a0 = 5
        an = 0
        for i in range(1,n.get()+1):
            if i % 2 != 0 :
                an += (-40/(np.pi*i)**2) * np.cos(i * ((np.pi)/2)*t)     # 𝑎𝑛=  (−40)/(𝜋^2∗𝑛^2 )  cos⁡〖(𝑖 𝜔 𝑡)〗
            else :
                continue
        s.append(a0 + an)
    return s


root = tkinter.Tk()
root.geometry("1000x800")  
root.wm_title("FOURIER - DEMO")
T = np.linspace(-5,5,1000)
fig = Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=root)
var = tkinter.IntVar()
def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)

def _plotX(n):
    F = S(T,var)
    fig.clf()
    fig.add_subplot(111).plot(T,F, ls='-', label = "x(t)", c = "green")
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    canvas.mpl_connect("key_press_event", on_key_press)
    



def _quit():
    root.quit()     
    root.destroy()  
                    


_plotX(1)
scale = tkinter.Scale(root, from_ = 1,to = 20, variable = var, resolution=1, length = 400 ,orient = tkinter.HORIZONTAL, command=_plotX)
text = tkinter.Label(root, text="BY Ibrahim EL MOUNTASSER et Mohamed Amine FAROUQ  - FST SETTAT")
text.pack(side=tkinter.BOTTOM)
scale.pack(side=tkinter.BOTTOM) 
text.config(height = 3) 
tkinter.mainloop()
