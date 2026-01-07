import requests
class Dice():
    def random(min:int, max:int):
        """Generates a random number as close to true random as possible"""
        url = "https://www.random.org/integers/?num=1&min={}&max={}&col=5&base=10&format=plain&rnd=new".format(min, max)
        number = requests.get(url)
        return int(number.text)
#d3 – d4 – d5 – d6 – d7 – d8 – d10 – d12 – d14 – d16 – d20 – d24 – d30
    def d20(bonus: int):
        """Returns a list with a roll between 1 and 20.Returns as [baseRoll, baseRoll+bonus]"""
        baseRoll = Dice.random(1,20)
        return [baseRoll,baseRoll+bonus]
    def d12(bonus: int):
        """Returns a list with a roll between 1 and 12.Returns as [baseRoll, baseRoll+bonus]"""
        baseRoll = Dice.random(1,12)
        return [baseRoll,baseRoll+bonus]
    def d8(bonus: int):
        """Returns a list with a roll between 1 and 8.Returns as [baseRoll, baseRoll+bonus]"""
        baseRoll = Dice.random(1,8)
        return [baseRoll,baseRoll+bonus]
    def d6(bonus: int):
        """Returns a list with a roll between 1 and 6.Returns as [baseRoll, baseRoll+bonus]"""
        baseRoll = Dice.random(1,6)
        return [baseRoll,baseRoll+bonus]
    def d4(bonus: int):
        """Returns a list with a roll between 1 and 4.Returns as [baseRoll, baseRoll+bonus]"""
        baseRoll = Dice.random(1,4)
        return [baseRoll,baseRoll+bonus]
    def diceRoll(bonus: int, diceNum: int):
        """Returns a list with a roll between 1 and the diceNum given. Returns as [baseRoll, baseRoll+bonus]"""
        baseRoll = Dice.random(1,diceNum)
        return [baseRoll,baseRoll+bonus]
