import pyautogui
import time

act = []

for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

print("action")
try:
    act.append(pyautogui.keyDown('ctrl'))
    act.append(pyautogui.keyDown('c'))
    act.append(pyautogui.keyUp('ctrl'))
    act.append(pyautogui.keyUp('c'))
except Exception as exc:
    print(f"Error: {exc}")
finally:
    del act
    print("finished")