import cv2
import cvzone

from time import sleep
import numpy as np

btList = [] #List of button
GapX  = 45 # Gap of Button from left side
GapY  = 25 # Gap of Button from   Up side
KeyGap = 25 #Gap between buttons vertical horizontal
ButtonSize =85
KeysInLine = 10

final_text = "-"


keyboard_keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
                  ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
                  ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]



def key_clk(event, x, y, flags, param):

    if event ==  cv2.EVENT_LBUTTONDOWN:
          print("[ ", x, y,"]")
          m = int((x - GapX) / (KeyGap + ButtonSize ))
          n =  int ((y - GapY) / ( KeyGap + ButtonSize))
          print('Column=',m )
          print('line=',n  )
          i = KeysInLine * n + m
          print( btList[i].text)
          print('pos  x, y = [', btList[i].pos[0], btList[i].pos[1], ']')


def DrawKeyBoard(img, buttonList):
    imgNew = np.zeros_like(img, np.uint8)
    for button in buttonList:
        x, y = button.pos
        cvzone.cornerRect(imgNew, (button.pos[0], button.pos[1],
                                                   button.size[0],button.size[0]), 20 ,rt=0)
        cv2.rectangle(imgNew, button.pos, (x + button.size[0], y + button.size[1]),
                                   (255, 194, 230), cv2.FILLED)
        cv2.putText(imgNew, button.text, (x + 20, y + 73),
                    cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 0), 4)

    out = img.copy()
    alpaha = 0.5
    mask = imgNew.astype(bool)
    out[mask] = cv2.addWeighted(img, alpaha, imgNew, 1-alpaha, 0)[mask]
    return out


class Button():
    def __init__(self, pos, text, size=[ButtonSize, ButtonSize]):
        self.pos = pos
        self.size = size
        self.text = text

#########Create Button List#######
def CreateBtnlList(keysList):
    for k in range(len(keysList)):  # k = Number of keybord line
        for x, key in enumerate(keysList[k]):  # x = Number of column in the line

            btList.append(Button([(ButtonSize + KeyGap) * x + GapX,
                                      (ButtonSize + KeyGap) * k + GapY],
                                     key))

    return  btList
#######################
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, 1280)
cap.set(4, 720)

cv2.namedWindow('output')
cv2.setMouseCallback('output',key_clk  )

while True:
    success, img = cap.read()
    buttonL = CreateBtnlList(keyboard_keys)
    img = DrawKeyBoard(img, buttonL)

    cv2.rectangle(img, (25,350), (800, 410),
                  (255, 255, 255), cv2.FILLED) #output Window
    cv2.putText(img, final_text, (40, 400),
                cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 4)
    cv2.imshow("output", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break