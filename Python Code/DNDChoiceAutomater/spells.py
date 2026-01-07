from roller import Dice
class ClericSpells():
    def __init__(self, bonus):
        self.bonus = bonus
     # @TODO: Imput correct spell effects, add a return for the added bonus.
    def spell_blessing(self):
        roll= Dice.d20(self.bonus)
        base = roll - self.bonus
        if roll < 12 and roll != 1:
            return "Fail {}. Forget spell, Dissaproval increased".format(roll)
        elif roll == 1:
            return "Fail {}! Corruption!".format(roll)
        elif roll in range(12, 14):
            print("Sucsess! Total {}, base {}\n".format(roll, base))
            print("+1 bonus to attack for turn, Ally for +1 attack for round.\n")
        elif roll in range(14, 18):
            print("Sucsess! Total {}, base {}\n".format(roll, base))
            print("+1 bonus to attack for turn, Ally for +1 attack for round.\n")
        elif roll in range(18, 19):
            print("Sucsess! Total {}, base {}\n".format(roll, base))
            print("+1 bonus to attack for turn, Ally for +1 attack for round.\n")
        elif roll in range(20, 24):
            print("Sucsess! Total {}, base {}\n".format(roll, base))
            print("+1 bonus to attack for turn, Ally for +1 attack for round.\n")
        elif roll in range(24, 28):
            print("Sucsess! Total {}, base {}\n".format(roll, base))
            print("+1 bonus to attack for turn, Ally for +1 attack for round.\n")
        elif roll in range(28, 30):
            print("Sucsess! Total {}, base {}\n".format(roll, base))
            print("+1 bonus to attack for turn, Ally for +1 attack for round.\n")
        elif roll in range(30, 32):
            print("Sucsess! Total {}, base {}\n".format(roll, base))
            print("+1 bonus to attack for turn, Ally for +1 attack for round.\n")
        elif roll >= 32:
            print("Sucsess! Total {}, base {}\n".format(roll, base))
            print("+1 bonus to attack for turn, Ally for +1 attack for round.\n")