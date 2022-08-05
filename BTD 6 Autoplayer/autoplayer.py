import pyautogui
from random import randrange

class Monkey:
    def __init__(self, name, strength, cost):
        self.name = name
        self.strength = strength
        self.cost = cost
        self.location = pyautogui.locateOnScreen('C:/Users/Tyler/Desktop/BTD 6 Autoplayer/monkeys/' + self.name + '.png', confidence=0.75)

    def place(self):
        def locate(tile):
            placement = (pyautogui.locateOnScreen('C:/Users/Tyler/Desktop/BTD 6 Autoplayer/placements/' + str(tile) + '.png', confidence=0.80))
            return placement
        d = {n: locate('tile' + str(n)) for n in range(1,7)}    
        pyautogui.click(self.location)
        randTile = randrange(1, 7)
        print(randTile)
        pyautogui.click(d[randTile])
        
        
class Game:
    def current_money():
        pass
    
    def current_round():
        pass

    def is_playing():
        pass
        

sauda = Monkey('sauda', 10, 585)
dart = Monkey('dart', 1, 215)
boomerang = Monkey('boomerang', 300, 5)
dart.place()