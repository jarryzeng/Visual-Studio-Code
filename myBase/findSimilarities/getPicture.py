import os
from datetime import datetime
from pynput import keyboard
from PIL.ImageGrab import grab
from pyautogui import position

class main:
    def __init__(self, startPosition, endPosition):
        self.startPosition = startPosition
        self.endPosition = endPosition
        self.isPress = True
    
    def listener(self):
        self.listen = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listen.start()
        self.listen.join()

    def on_press(self, key):
        if key == keyboard.KeyCode.from_char("\'") and self.isPress:
            self.isPress = False
            x, y = position()
            self.startPosition = [x, y]
        elif key == keyboard.Key.esc:
            os.system(f"rm {self.name}")
            self.listen.stop()

    def on_release(self, key):
        if key == keyboard.KeyCode.from_char("\'"):
            self.isPress = True
            x, y = position()
            self.endPosition = [x, y]
            self.makePicture(self.startPosition, self.endPosition)

    def makePicture(self, start, end):
        x = [start[0], end[0]]
        y = [start[1], end[1]]
        if(x[1] < x[0]): x[1], x[0] = x[0], x[1]
        if(y[1] < y[0]): y[1], y[0] = y[0], y[1]
        bbox = (x[0], y[0], x[1], y[1])
        print(os.times())
        time = datetime.now()
        self.name = str(time.strftime("%Y-%m-%d")) + '.jpg'

        try:
            img = grab(bbox = bbox)
            img.save("./findSimilarities/" + self.name)
        except Exception as e:
            print(e)
        
        self.startPosition = False
        self.endPosition = False

listener = main(False, False)
listener.listener()