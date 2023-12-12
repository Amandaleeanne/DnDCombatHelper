
from roller import Dice
import csv
class Character():

    def __init__(self, name:str,level:int,warrior: False, wizard: False, cleric: False, thief:False,AC:int,HP:int,strength_bonus:int,agility_bonus:int,stamina_bonus:int,personality_bonus:int,luck_bonus:int, weapon_count:int, spell_count:int
):
        self.spell_bonus = spell_bonus
        self.d20attack_bonus = d20attack_bonus
        self.attack_bonus = attack_bonus
        self.missile_bonus = missile_bonus
        self.initiative = initiative
        self.name = name
        self.warrior = warrior
    def __str__(self) -> str:
        """Returns a string representation of Character class"""
        return "The character {} has a attack bonus of {} , melee bonus of {}, and spell check of {}".format(self.attack_bonus, self.melee_bonus,self.spell_check)
    def changeValue(self, file):
        pass
                


    #Basic Spellcasting----------------------------------------
    def spellcast(self):

        roll= Dice.d20(self.spell_bonus)
        if roll[1] >= 12:
            return "Sucsess! Total {}, base {}".format(roll[1], roll[0])
        elif roll[1] < 12 and roll[0] != 1:
            return "Fail {}. Forget spell, Dissaproval increased".format(roll[1])
        else:
            return "Fail {}! Corruption!".format(roll[0])
    #Attack -----------------------------------------------------
    def attack(self):
        roll = Dice.d20(self.d20attack_bonus)
        base = roll - self.d20attack_bonus
        feat_sucsess = False
        if self.warrior:
            feat = self.d4(4)
            feat_base = feat - 4
            if feat_base >= 3:
                feat_sucsess = True
            if feat_sucsess:
                roll += feat
                return "Feat sucseeded {}. Rolled a {}, base {}".format(feat,roll, base)
            else:
                roll += feat
                return "Feat fail {}. Rolled a {}, base {}".format(feat,roll, base)
        return "Rolled a {}, base {}".format(roll, base)
someone = Character(1, 1, 1, 1, 1, "someone", False)
print(someone.spellcast())