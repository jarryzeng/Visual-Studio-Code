import tkinter as tk
from time import strftime

def loop():
    var.set(strftime("%Y-%m-%d %H:%M:%S"))
    window.geometry("450x75")
    window.after(1000, loop)

def startMove(event):
    global x, y
    x = event.x
    y = event.y

def stopMove(event):
    global x, y
    x = None
    y = None

def onMotion(event):
    global x, y
    deltax = event.x - x
    deltay = event.y - y
    window.geometry("+%s+%s" % (window.winfo_x() + deltax, window.winfo_y() + deltay))
    window.update()

def destroy(event):
    if event.keysym == 'Escape':
        window.destroy()

window = tk.Tk()
window.config(background="gray")
window.resizable(width=0, height=0)
window.overrideredirect(1)
window.bind("<ButtonPress-1>", startMove)
window.bind("<ButtonRelease-1>", stopMove)
window.bind("<B1-Motion>", onMotion)
window.bind("<Key>", destroy)
window.wm_attributes("-topmost", True)
window.wm_attributes("-toolwindow", True)
window.wm_attributes("-transparentcolor", "gray")

var = tk.StringVar()
label = tk.Label(window, textvariable=var, bg="gray", fg="yellow", font=('', 40))
label.pack()

loop()
window.mainloop()