import pyautogui as pag
import time
import os

def runMe():
    e = 280.0
    a = 0.1
    b1 = 0.000005
    pag.click(1000, 500)
    while True:
        #print(e)
        #print(pag.position()[0], pag.position()[1])

        #print(int(e))
        if pag.pixel(935, 520)[0] == 8:
            break

        x, y = int(e), 619
        r, g, b = pag.pixel(x, y)

        xe, ye = int(e-50), 619
        re, ge, be = pag.pixel(x,y)
        #print(x, y)
        #print(pag.pixel(x,y))

        bx, by = int(e), 536
        br, bg, bb = pag.pixel(bx, by)

        bxe, bye = int(e-50), 536
        bre, bge, bbe = pag.pixel(bx, by)
        
        if [r, g, b] == [172, 172, 172] or [r, g, b] == [0, 0, 0] or [br, bg, bb] == [172, 172, 172] or [bre, bge, bbe] == [172, 172, 172] or [re, ge, be] == [172, 172, 172] or [re, ge, be] == [0, 0, 0]:
            pag.keyDown("space")
            print("e")
            os.system('cls')
        else:
            #print(val)
            pass

        e+=a
        if a < 0.6:
            a += b1
            #print(a)
        b1 += 0.0000015
        #print(b1)
    
def getInfo(e):
    if pag.pixel(935, 520)[0] == 8:
        return ["e"]
    
    things = []
    x, y = int(e), 619
    r, g, b = pag.pixel(x, y)

    bx, by = int(e), 536
    br, bg, bb = pag.pixel(bx, by)
    
    for val in list([r, g, b]):
        if val > 150 and val < 180:
            things.append(x)
            things.append(y)
            break
        
    if len(things) == 0:
        things.append(0)
        things.append(0)
        
    for val in list([br, bg, bb]):
        if val > 150 and val < 180:
            things.append(bx)
            things.append(by)
            break

    if len(things) == 2:
        things.append(0)
        things.append(0)

    return things

if __name__ == "__main__":
    runMe()