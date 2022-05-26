import cv2
import cvzone
from tkinter import Tk, Text
from time import sleep
import numpy as np

btList = [] #List of button
GapX  = 200 # Gap of Button from left side
GapY  = 290 # Gap of Button from   Up side
KeyGap = 10 #Gap between buttons vertical horizontal
ButtonSize =68
KeysInLine = 12

final_text = "-"


keyboard_keys = [
    ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0","-","="],
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[","]"],
    ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";","'","Entr"],
    ["sft","Z", "X", "C", "V", "B", "N", "M", ",", ".", "/","sft"]
]


def nothing(self):
    pass


############      class Button       ############
class Button():
    def __init__(self, pos, text, size=[ButtonSize, ButtonSize]):

        self.pos = pos
        self.size = size
        self.text = text

###########     KeyBoard    Class  #############
class  KeyBoard:
    def __init__(self, kbd, msg):

        self.kbd = kbd
        self.msg = msg
        #self.GapY = 65


    def GetKey(self,i):
        x ,y = i[0], i[1]
        #print("pos = [ ", x, y, "]")
        #print("self.GapXY = [ ", self.GapX, self.GapY, "]")
        m = int((x - GapX) / (KeyGap + ButtonSize))
        n = int((y - GapY) / (KeyGap + ButtonSize))

        print(m,n)

        i = (KeysInLine) * n + m
        print('line=', n, i, len(btList))
        if (i<len(btList)):
            print(btList[i].text)
            self.msg = self.msg + btList[i].text
            #print('pos  x, y = [', btList[i].pos[0], btList[i].pos[1], ']')
        print(self.msg)

    def key_clk(self ,event, x, y, flags, param):

        if event ==  cv2.EVENT_LBUTTONDOWN:
            point = [x, y]
            self.GetKey(point)

    def DrawKeyBoard0(self ,img, buttonList):

        for button in buttonList:
            x, y = button.pos
            w, h = button.size


            cvzone.cornerRect(img, (button.pos[0], button.pos[1],
                                    button.size[0], button.size[0]), 20, rt=0)
            cv2.rectangle(img, button.pos, (int(x + w), int(y + h)), (255, 144, 30), cv2.FILLED)
            cv2.putText(img, button.text, (x + 20, y + 65),
                        cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 4)
        return img


    def DrawKeyBoard(self,img, buttonList):
        imgNew = np.zeros_like(img, np.uint8)
        for button in buttonList:
            x, y = button.pos
            cvzone.cornerRect(imgNew, (button.pos[0], button.pos[1],
                                       button.size[0],button.size[0]), 20 ,rt=0)
            cv2.rectangle(imgNew, button.pos, (x + button.size[0], y + button.size[1]),
                          (255, 194, 230), cv2.FILLED)
            cv2.putText(imgNew, button.text, (x + 15, y + 60),
                        cv2.FONT_HERSHEY_PLAIN,ButtonSize/20, (0, 0, 0), 4)

        out = img.copy()
        alpaha = 0.5
        mask = imgNew.astype(bool)
        out[mask] = cv2.addWeighted(img, alpaha, imgNew, 1-alpaha, 0)[mask]
        return out




    #########Create Button List#######
    def CreateBtnlList(self):
        for k in range(len(self.kbd)):  # k = Number of keybord line
            for x, key in enumerate(self.kbd[k]):  # x = Number of column in the line

                btList.append(Button([(ButtonSize + KeyGap) * x + GapX,
                                      (ButtonSize + KeyGap) * k +GapY],
                                     key))

        return  btList
#######################

def main():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(3, 1280)
    cap.set(4, 720)

    cv2.namedWindow('output')
    keybrd = KeyBoard(keyboard_keys, final_text)
    cv2.setMouseCallback('output', keybrd.key_clk)

    while True:


        success, img = cap.read()
        buttonL = keybrd.CreateBtnlList()
        img01 = keybrd.DrawKeyBoard(img, buttonL)

        cv2.rectangle(img01, (25,30), (1100, 180),
                      (255, 255, 255), cv2.FILLED) #output Window
        cv2.putText(img01, keybrd.msg , (40, 90),
                    cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 4)

        cv2.imshow("output", img01)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
if __name__ == "__main__":
    main()