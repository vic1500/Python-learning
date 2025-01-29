import random as rd

class Dice:
    def roll(self):
        side1 = rd.randint(1, 6)
        side2 = rd.randint(1, 6)
        rolled_dice = (side1, side2)
        return rolled_dice

dice = Dice()

print(dice.roll())