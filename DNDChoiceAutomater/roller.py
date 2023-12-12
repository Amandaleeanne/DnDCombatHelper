import requests
class Dice():
    def random(min:int, max:int):
        """Generates a random number as close to true random as possible"""
        url = "https://www.random.org/integers/?num=1&min={}&max={}&col=5&base=10&format=plain&rnd=new".format(min, max)
        number = requests.get(url)
        return int(number.text)
    def d20(bonus: int):
        """Returns a list with a roll between 1 and 20 with added bonus and base roll"""
        baseRoll = Dice.random(1,20)
        return [baseRoll,baseRoll+bonus]
    def d12(bonus: int):
        """Returns a list with a roll between 1 and 12 with added bonus and base roll"""
        baseRoll = Dice.random(1,12)
        return [baseRoll,baseRoll+bonus]
    def d8(bonus: int):
        """Returns a list with a roll between 1 and 8 with added bonus and base roll"""
        baseRoll = Dice.random(1,8)
        return [baseRoll,baseRoll+bonus]
    def d6(bonus: int):
        """Returns a list with a roll between 1 and 6 with added bonus and base roll"""
        baseRoll = Dice.random(1,6)
        return [baseRoll,baseRoll+bonus]
    def d4(bonus: int):
        """Returns a list with a roll between 1 and 4 with added bonus and base roll"""
        baseRoll = Dice.random(1,4)
        return [baseRoll,baseRoll+bonus]
