
from roller import Dice
import json
#Handles the JSON files and reads and edits them based on main script.
class Character():

    def __init__(self, character:str):
        #Get name
        self.name = character
        #Open Json file will corrent name
        with open('{}.json'.format(self.name), 'r') as f:
            data = json.load(f)
        #Load data into current environment
        self.data = data
    def __str__(self) -> str:
        """Returns a string representation of Character class"""
        return "The character {} has a attack bonus of {} , melee bonus of {}, and spell check of {}".format(self.attack_bonus, self.melee_bonus,self.spell_check)
    
    #Note the JSON file will handle all the the spell effects from 12-32 as i belive it is the same for every spell. Then the helper function here will simply get what that spell does

    def changeValue(self, number:int, value:str, reset:bool=False):
        """Changes the temporary value of the character, ENTER IN POSITIVE OR NEGITIVE"""
        #Apply valid values
        valid_values = ["ac","hp","strength","agility","stamina","personality","luck"]
        #Check to see if there is a valid value to change
        try:
            if value not in valid_values:
                raise ValueError
            else:
                #If there is, check to see if we are removing or adding the bonus.
                #If you are adding the bonus:
                if not reset:
                    self._calculateValue(number, value)
                else:
                    self._resetValue(number, value)
        except ValueError:
            print("Invalue value to change given. valid: ac,hp,strength,agility,stamina,personality,luck")

    #calculates new temporary value based on given number
    def _calculateValue(self, number, value):
        if value == "ac":
            self.data["info"]["temp_AC"] += number
        elif value == "hp":
            self.data["info"]["temp_AC"] += number
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

    #Resets the temporary value to match the actual value
    def _resetValue(self, value):
        if value == "ac":
            self.data["info"]["temp_AC"] = self.data["info"]["ac"]
        elif value == "hp":
            self.data["info"]["temp_hp"] = self.data["info"]["hp"]
        elif value == "strength":
            self.data["info"]["temp_strength_bonus"] = self.data["info"]["strength_bonus"]
        elif value == "agility":
            self.data["info"]["temp_agility_bonus"] = self.data["info"]["agility_bonus"]
        elif value == "stamina":
            self.data["info"]["temp_stamina_bonus"] = self.data["info"]["stamina_bonus"]
        elif value == "personality":
            self.data["info"]["temp_personality_bonus"] = self.data["info"]["personality_bonus"]
        elif value == "luck":
            self.data["info"]["temp_luck_bonus"] = self.data["info"]["luck_bonus"]







   