
from roller import Dice
import csv
import os
import json
class Character():

    def __init__(self, character:str):
        #Get name
        self.name = character
        #Open Json file will corrent name
        with open('{}.json'.format(self.name), 'r') as f:
            data = json.load(f)

    def __str__(self) -> str:
        """Returns a string representation of Character class"""
        return "The character {} has a attack bonus of {} , melee bonus of {}, and spell check of {}".format(self.attack_bonus, self.melee_bonus,self.spell_check)
    def changeValue(self, number:int, value:str):
        """Changes the temporary value of the character, ENTER IN POSITIVE OR NEGITIVE"""
        #Open Json file will corrent name
        valid = ["ac","hp","strength","agility","stamina","personality","luck"]
        with open('{}.json'.format(self.name), 'r') as f:
            data = json.load(f)
        try:
            if value not in valid:
                raise ValueError
            else:
                if value == "ac":
                    pass
                elif value == "hp":
                    pass
                elif value == "strength":
                    pass
                elif value == "agility":
                    pass
                elif value == "stamina":
                    pass
                elif value == "personality":
                    pass
                elif value == "luck":
                    pass
        except ValueError:
            print("Invalue value to change given. valid: ac,hp,strength,agility,stamina,personality,luck")
                


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