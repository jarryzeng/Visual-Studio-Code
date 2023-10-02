import tkinter as tk
from time import strftime
from keyboard import is_pressed
from pyautogui import press, keyDown, keyUp, click
from datetime import datetime

def execute(list):
    for i in list:
        press(i)

def destroy():
    window.destroy()

def loop():
    global boo
    if is_pressed('`') and boo:
        start = datetime.now()
        boo = False
        execute(executeList1)
        keyDown('shift')
        click(button = 'right')
        keyUp('shift')
        execute(executeList2)
        boo = True
        end = datetime.now()
        var.set(float(end.strftime("%S.%f")) - float(start.strftime("%S.%f")))
    elif is_pressed('esc'): 
        destroy()
        return

    var1.set(strftime("%Y-%m-%d %H:%M:%S"))
    window.geometry("450x100")
    window.after(1, loop)

def startMove(event):
    global x, y
    x = event.x
    y = event.y

def stopMove(ignore):
    global x, y
    x = None
    y = None

def onMotion(event):
    global x, y
    deltax = event.x - x
    deltay = event.y - y
    window.geometry("+%s+%s" % (window.winfo_x() + deltax, window.winfo_y() + deltay))
    window.update()

times = 0
boo = True
executeList1 = ['1', 'f', '2', 'f', '1', 'f']
executeList2 = ['f', '2', 'f', '1', 'f']

window = tk.Tk()
window.config(background="gray")
window.resizable(width=0, height=0)
window.overrideredirect(1)
window.bind("<ButtonPress-1>", startMove)
window.bind("<ButtonRelease-1>", stopMove)
window.bind("<B1-Motion>", onMotion)
window.wm_attributes("-topmost", True)
window.wm_attributes("-toolwindow", True)
window.wm_attributes("-transparentcolor", "gray")

var = tk.StringVar()
label = tk.Label(window, textvariable=var, bg="gray", fg="yellow", font=('', 40))
label.pack()

var1 = tk.StringVar()
label1 = tk.Label(window, textvariable=var1, bg="gray", fg="yellow", font=('', 40))
label1.pack()

loop()
window.mainloop()