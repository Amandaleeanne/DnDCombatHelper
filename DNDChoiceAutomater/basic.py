from roller import Dice
 #Basic Spellcasting----------------------------------------
def spellcast(bonus):
    roll= Dice.d20(bonus)
    if roll[1] >= 12:
        return "Sucsess! Total {}, base {}".format(roll[1], roll[0])
    elif roll[1] < 12 and roll[0] != 1:
        return "Fail {}. Forget spell, Dissaproval increased".format(roll[1])
    else:
        return "Fail {}! Corruption!".format(roll[0])
#Attack -----------------------------------------------------
def attackk(bonus, warrior):
    roll = Dice.d20(bonus)
    feat_sucsess = False
    if warrior:
        feat = Dice.d4(4)
        total = roll[1] + feat[1]
        if feat[0] >= 3:
            feat_sucsess = True
        if feat_sucsess:
            return "Feat sucseeded {}. Total {}, base {}".format(feat,total, roll[0])
        else:
            return "Feat fail {}. Total {}, base {}".format(feat,total, roll[0])
    return "Rolled a {}, base {}".format(roll[1], roll[0])

def main():
    exit = False
    while not exit:
        validInput = ["y","n","Y","N","attack","a","spell","spellcast","s"]
        spell = ["spell","spellcast","s"]
        attack = ["attack","a",]
        warrior = False
        user = input("What do you want to do? (a)ttack/(s)pell: ").strip()
        bonus = int(input("bonus: "))
        print("\n")
        if user in validInput:
            if user in spell:
                print(spellcast(bonus))
            else:
                user = input("Warrior? (y/n): ").strip()
                if user == "y":
                    warrior=True
                    user = ""
                else:
                    warrior = False
                print(attackk(bonus, warrior))
            #Exit case
            user = ""
            user = input("do you want to exit? (y/n): ")
            print("\n")
            if user == "y":
                exit = True
        else: print("Invalid input\n")
main()
