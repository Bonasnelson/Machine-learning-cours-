import  pyautogui as spam
import time

limit = input('No. of messages')
msg = input('Message you wand to send')

i =0

time.sleep(5)
while i<int(limit):
    spam.typewrite(msg)
    spam.press('Enter')
i+=1