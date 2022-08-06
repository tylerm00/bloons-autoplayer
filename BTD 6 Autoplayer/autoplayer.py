import pyautogui
from random import randrange
import cv2
import numpy as np
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

class Monkey:
    def __init__(self, name, strength, cost):
        self.name = name
        self.strength = strength
        self.cost = cost
        self.location = pyautogui.locateOnScreen('C:/Users/Tyler/Desktop/BTD 6 Autoplayer/monkeys/' + self.name + '.png', confidence=0.75)

    def locate(tile):
            placement = (pyautogui.locateOnScreen('C:/Users/Tyler/Desktop/BTD 6 Autoplayer/placements/' + str(tile) + '.png', confidence=0.80))
            return placement

    def place(self):
        d = {n: Monkey.locate('tile' + str(n)) for n in range(1,7)}    
        pyautogui.click(self.location)
        randTile = randrange(1, 7)
        pyautogui.click(d[randTile])
        
        
class Game:
    def current_money():
        #pyautogui.screenshot(region=(566,400, 63, 31))
        cash_location = pyautogui.locateOnScreen('money.png', confidence=0.99)
        #print(loca)
        #print(loca[0])
        if cash_location is not None:
            curr_cash = pyautogui.screenshot(region=(cash_location[0] + cash_location[2] + 15, cash_location[1], 110, cash_location[3])) #left, top, width, height
            curr_cash = cv2.cvtColor(np.array(curr_cash), cv2.COLOR_RGB2BGR)
            cv2.imwrite("curr_cash.png", curr_cash)
            img = Image.open('curr_cash.png')
            thresh = 200
            fn = lambda x : 255 if x > thresh else 0
            r = img.convert('L').point(fn, mode='1')
            r.save('bwcash.png')
            curr_cash = cv2.imread('bwcash.png') # This entire process first takes a screenshot to the right of the money indicator to retrieve an image of the amount of money we have,
            curr_cash = pytesseract.image_to_string(curr_cash)# it then converts it to a pure black and white image, improving the reliability of pytesseract.image_to_string
            print(curr_cash)
            return curr_cash
        if cash_location is None:
            Game.current_money()

    def current_round():
        pass

    def is_playing():
        pass
        

sauda = Monkey('sauda', 10, 585)
dart = Monkey('dart', 1, 215)
boomerang = Monkey('boomerang', 300, 5)
Game.current_money()
