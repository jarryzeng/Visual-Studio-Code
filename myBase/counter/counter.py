import tkinter as tk
import keyboard

class windows:
    def __init__(self):
        self.keyoff = True
        self.times = 0
        self.total = 0
        self.setWindow()
        self.createObject()
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
    
    def createObject(self):
        self.var1 = tk.StringVar()
        self.label1 = tk.Label(self.window, textvariable=self.var1, bg="gray", fg="yellow", font=('', 40))
        self.label1.pack()

        self.var2 = tk.StringVar()
        self.label2 = tk.Label(self.window, textvariable=self.var2, bg="gray", fg="yellow", font=('', 40))
        self.label2.pack()

    def destroy(self, event):
        self.window.destroy()
        keyboard.remove_hotkey(event)

    def release(self, event):
        self.times += 1
        keyboard.remove_hotkey(event)

    def attack(self, event):
        self.total += 1
        keyboard.remove_hotkey(event)

    def loop(self):
        keyboard.on_release_key('j', self.release, suppress=True)
        keyboard.on_release_key('e', self.attack, suppress=True)
        keyboard.on_release_key('f5', self.destroy, suppress=True)
        self.var1.set(str(self.times))
        self.var2.set(str(self.total))
        self.window.geometry("450x170")
        self.window.after(100, self.loop)

    def start(self):
        self.window.mainloop()

window = windows()
window.start()