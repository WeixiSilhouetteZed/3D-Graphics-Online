import tkinter
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

root = tkinter.Tk()
root.wm_title("BZ3D Graph Generator")
root.geometry('700x830')
root.resizable(width=True, height=True)

fig=Figure(figsize=(1,1),dpi=150)
canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

def plot3DSurface(expr,xdis,ydis,render):
    ax=fig.add_subplot(111,projection='3d')
    def f(x, y):
        return eval(expr)
    x = np.linspace(-xdis, xdis, render)
    y = np.linspace(-ydis, ydis, render)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    ax.plot_surface(X, Y, Z, rstride=2, cstride=2,
                    cmap='plasma', edgecolor='none');
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_title(expr)

def plot3DContour(expr,xdis,ydis,render):
    ax=fig.add_subplot(111,projection='3d')
    def f(x, y):
        return eval(expr)
    x = np.linspace(-xdis, xdis, render)
    y = np.linspace(-ydis, ydis, render)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    ax.contour3D(X, Y, Z, 50,cmap='plasma');
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_title(expr)

def plot3DWire(expr,xdis,ydis,render):
    ax=fig.add_subplot(111,projection='3d')
    def f(x, y):
        return eval(expr)
    x = np.linspace(-xdis, xdis, render)
    y = np.linspace(-ydis, ydis, render)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    ax.plot_wireframe(X, Y, Z, cmap='plasma');
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_title(expr)

def plot3D(expr,graphType,xdis,ydis,render):
    if graphType=='contour':
        plot3DContour(expr,xdis,ydis,render)
    elif graphType=='wireframe':
        plot3DWire(expr,xdis,ydis,render)
    elif graphType=='surface':
        plot3DSurface(expr,xdis,ydis,render)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)

books = ['contour', 'wireframe','surface']

Graphtype=tkinter.StringVar()
intVar = tkinter.IntVar()
st = tkinter.StringVar()
fm1=tkinter.Frame(master=root)
fm1.pack(side=tkinter.RIGHT)
explanation = """This Tkinter application is for generating EZ4.0 MATH237 3D graphs.\n\
It is purely for educational purposes, you are required to use\n\
Python regular expression syntax and in particular, for special\n\
functions such as log, trig, and absolute functions, please add "np."\n\
in front of the function. A detailed list of syntax maybe attached but\n\
not guaranteed."""
introlabel=tkinter.Label(fm1,compound=tkinter.CENTER,text=explanation).pack(side=tkinter.BOTTOM)
fm2=tkinter.Frame(master=root)
fm2.pack(side=tkinter.LEFT)
ttk.Entry(fm2, textvariable=st,width=24,font=('StSong', 20, 'bold'),
          foreground='red').pack(fill=tkinter.BOTH, expand=tkinter.YES)
st.set("x+y")
ttk.Label(fm2, text='Select one of the available graph types').pack(fill=tkinter.BOTH, expand=tkinter.YES)
i = 0
for book in books:
    ttk.Radiobutton(fm2,
        text = book,
        variable = intVar, 
        value=i).pack(anchor=tkinter.W)
    i += 1
intVar.set(1)

def graph():
    expr=st.get()
    graphType=books[intVar.get()]
    xdis=ydis=3
    render=120
    plot3D(expr,graphType,xdis,ydis,render)
    canvas.draw()

ttk.Button(fm2, text='Graph', command=graph).pack(side=tkinter.BOTTOM)


tkinter.mainloop()
