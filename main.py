import pyautogui
import random
import time

time.sleep(3)


size = pyautogui.size()

mytuple = size
list = list(mytuple)
axisY = list[0]
axisX = list[1]
# print(axisY, axisX)

i = False

while i == False:
    posX = random.randint(0, axisX)
    posY = random.randint(0, axisY)

    pyautogui.moveTo(posX, posY, duration = 0)
    pyautogui.click(posX, posY)

    







input("press enter")



