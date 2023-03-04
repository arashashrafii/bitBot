import random

class DiceRoller:
    def __init__(self, num_dice, num_sides):
        self.num_dice = num_dice
        self.num_sides = num_sides
        
    def roll_dice(self):
        results = []
        for i in range(self.num_dice):
            result = random.randint(1, self.num_sides)
            results.append(result)
        return results
