import os
import numpy as np
from PIL import Image
import tkinter as tk
from pynput import keyboard
import pyautogui
import cv2

class main:
    def __init__(self, startPosition, endPosition):
        self.startPosition = startPosition
        self.endPosition = endPosition
        self.isPress = True
        self.local = "./findSimilarities/"
    
    def listener(self):
        self.listen = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listen.start()
        self.listen.join()

    def on_press(self, key):
        if key == keyboard.KeyCode.from_char("\'") and self.isPress:
            self.isPress = False
            x, y = pyautogui.position()
            self.startPosition = [x, y]
        elif key == keyboard.Key.esc:
            try:
                # pass
                os.remove(f"{self.local}img.jpg")
                os.remove(f"{self.local}screen.jpg")
            except Exception as exc:
                print(exc)
            self.listen.stop()

    def on_release(self, key):
        if key == keyboard.KeyCode.from_char("\'"):
            self.isPress = True
            x, y = pyautogui.position()
            self.endPosition = [x, y]
            self.makePicture(self.startPosition, self.endPosition)

    def makePicture(self, start, end):
        x = [start[0], end[0]]
        y = [start[1], end[1]]
        if(x[1] < x[0]): x[1], x[0] = x[0], x[1]
        if(y[1] < y[0]): y[1], y[0] = y[0], y[1]
        width = x[1] - x[0]
        height = y[1] - y[0]
        imgPosition = (x[0], y[0], width, height)

        try:
            img = pyautogui.screenshot(region=imgPosition)
            screen = pyautogui.screenshot()
            img = np.array(img)
            screen = np.array(screen)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(f"{self.local}screen.jpg", screen)
            cv2.imwrite(f"{self.local}img.jpg", img)
        except Exception as e:
            print(e)
        
        self.startPosition = False
        self.endPosition = False

listener = main(False, False)
listener.listener()