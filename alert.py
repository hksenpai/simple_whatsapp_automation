import pyautogui as pat
import time
def openbrave():
    pat.press("winleft")
    pat.write("brave")
    pat.press("enter")
    time.sleep(0.5)
def openwhatsapp():
    pat.write("https://web.whatsapp.com/")
    pat.press("enter")
    time.sleep(15)
    pat.press("tab")

def send(name,msg,count=1):
    pat.write(name)
    time.sleep(0.2)
    pat.press("enter")
    time.sleep(0.75)
    for i in range(count):
        pat.write(msg)
        pat.press("enter")
    pat.keyDown("shift")
    for i in range(3):
        pat.press("tab")
    pat.keyUp("shift")
    time.sleep(0.05)
l=["91006 68244","95811 13355","73968 80910","89198 25321","97019 39599"]
#l=["8019447255","8331897847"]
msg="attendance"
openbrave()
openwhatsapp()
for i in l:
    send(i,msg)