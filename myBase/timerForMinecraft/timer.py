import tkinter as tk
from time import strftime
from keyboard import is_pressed
from pyautogui import press, keyDown, keyUp, click
from datetime import datetime

class window:
    def __init__(self, times=None, boo=None, start=None, end=None):
        self.setWindow()
        self.createObject()

        self.times = times
        self.boo = boo
        self.start = start
        self.end = end
        self.loop()

    def setWindow(self):
        self.window = tk.Tk()
        self.window.config(background="gray")
        self.window.resizable(width=0, height=0)
        self.window.overrideredirect(1)
        self.window.bind("<ButtonPress-1>", self.startMove)
        self.window.bind("<ButtonRelease-1>", self.stopMove)
        self.window.bind("<B1-Motion>", self.onMotion)
        self.window.wm_attributes("-topmost", True)
        self.window.wm_attributes("-toolwindow", True)
        self.window.wm_attributes("-transparentcolor", "gray")
    
    def createObject(self):
        self.var1 = tk.StringVar()
        self.label1 = tk.Label(self.window, textvariable=self.var1, bg="gray", fg="yellow", font=('', 40))
        self.label1.pack()

        self.var2 = tk.StringVar()
        self.label2 = tk.Label(self.window, textvariable=self.var2, bg="gray", fg="yellow", font=('', 40))
        self.label2.pack()
        
    def destroy(self):
        self.window.destroy()

    def loop(self):
        if is_pressed('`') and self.start == None and self.end == None:
            self.boo = False
            self.start = datetime.now()
        if is_pressed(';') and self.start != None and self.end == None:
            self.boo = True
            self.end = datetime.now()
        if self.start != None and self.end != None:
            self.var1.set(str(float(self.end.strftime("%S.%f")) - float(self.start.strftime("%S.%f"))))
            self.start = None
            self.end = None
        elif is_pressed('esc'): 
            self.destroy()
            return

        self.var2.set(strftime("%Y-%m-%d %H:%M:%S"))
        self.window.geometry("450x170")
        self.window.after(1, self.loop)

    def startMove(self, event):
        self.x = event.x
        self.y = event.y

    def stopMove(self, ignore):
        self.x = None
        self.y = None

    def onMotion(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        self.window.geometry("+%s+%s" % (self.window.winfo_x() + deltax, self.window.winfo_y() + deltay))
        self.window.update()

    def startWindow(self):
        self.window.mainloop()

times = 0
boo = True
start = None
end = None

project = window(times, boo, start, end)
project.startWindow()

# def destroy():
#     window.destroy()

# def loop():
#     global boo, start, end
#     if is_pressed('`') and boo:
#         boo = False
#         start = datetime.now()
#     if is_pressed(';') and not boo:
#         boo = True
#         end = datetime.now()
#     if start != None and end != None:
#         var1.set(str(float(end.strftime("%S.%f")) - float(start.strftime("%S.%f"))))
#         print(start)
#         print(end)
#         start = None
#         end = None
#     elif is_pressed('esc'): 
#         destroy()
#         return

#     var2.set(strftime("%Y-%m-%d %H:%M:%S"))
#     window.geometry("450x170")
#     window.after(1, loop)

# def startMove(event):
#     global x, y
#     x = event.x
#     y = event.y

# def stopMove(ignore):
#     global x, y
#     x = None
#     y = None

# def onMotion(event):
#     global x, y
#     deltax = event.x - x
#     deltay = event.y - y
#     window.geometry("+%s+%s" % (window.winfo_x() + deltax, window.winfo_y() + deltay))
#     window.update()

# window = tk.Tk()
# window.config(background="gray")
# window.resizable(width=0, height=0)
# window.overrideredirect(1)
# window.bind("<ButtonPress-1>", startMove)
# window.bind("<ButtonRelease-1>", stopMove)
# window.bind("<B1-Motion>", onMotion)
# window.wm_attributes("-topmost", True)
# window.wm_attributes("-toolwindow", True)
# window.wm_attributes("-transparentcolor", "gray")

# var1 = tk.StringVar()
# label1 = tk.Label(window, textvariable=var1, bg="gray", fg="yellow", font=('', 40))
# label1.pack()

# var2 = tk.StringVar()
# label2 = tk.Label(window, textvariable=var2, bg="gray", fg="yellow", font=('', 40))
# label2.pack()

# loop()
# window.mainloop()