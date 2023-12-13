
from roller import Dice
import json
import os
#Handles the JSON files and reads and edits them based on main script.
class Character():

    def __init__(self, character:str): 
    #{
        #Ensure you are in the correct directory:
        os.chdir(os.path.dirname(__file__))
        #Get name
        self.name = character
        #if file with name exists:
        self._initilize_character()
        #else:
        #make a new character
        
    #}

    def __str__(self) -> str:
        """Returns a string representation of Character class, giving information about the current character."""
        if self.char_info["iswizard"] == True or self.char_info["iscleric"] == True:
            if self.char_info["iswizard"] == True:
                return "The character {} is a Wizard, and knows spells {}. Their HP is {}, AC is {}, and have a base spell bonus of {}".format(self.name, self.spellList, self.char_info["hp"], self.char_info["ac"],(self.char_info["level"]+self.char_info["intellect_bonus"]))
            else:
                return "The character {} is a Cleric, and knows spells {}. Their HP is {}, AC is {}, and have a base spell bonus of {}".format(self.name, self.spellList, self.char_info["hp"], self.char_info["ac"],(self.char_info["level"]+self.char_info["intellect_bonus"]))
        elif self.char_info["iswarrior"]== True:
            return "The character {} is a Warrior.".format(self.name)
        else:
            return "The character {} is a Thief".format(self.name)
        
        
    #Note the JSON spell file will handle all the the spell effects from 12-32 as i belive it is the same for every spell. Then the helper function here will simply get what that spell does
    def _initilize_character(self):
        #Open Character Json file will correct name
        with open('{}.json'.format(self.name), 'r') as f:
            infoData = json.load(f)
        #Load data into current environment
        self.infoData = infoData
        #initialize one element list:
        self.char_info = infoData['info'][0]
        #Check to see if character is a spellcaster:
        if self.char_info["iswizard"] is True or self.char_info["iscleric"] is True:
            #Open spells Json file
            with open('spells.json', 'r') as f:
                spellData = json.load(f)
            #Load data into current environment
            self.spellData = spellData
            #Get spells from character and add to spell list:
            self.spellList = []
            #For every spell
            for spell in self.infoData["spells"]:
                #get spell name and add to list
                self.spellList.append(spell['name'])
    #TODO: make method
    def _new_character(self):
        pass
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
            self.char_info["temp_AC"] += number
        elif value == "hp":
            self.char_info["temp_AC"] += number
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
            self.char_info["temp_AC"] = self.char_info["ac"]
        elif value == "hp":
            self.char_info["temp_hp"] = self.char_info["hp"]
        elif value == "strength":
            self.char_info["temp_strength_bonus"] = self.char_info["strength_bonus"]
        elif value == "agility":
            self.char_info["temp_agility_bonus"] = self.char_info["agility_bonus"]
        elif value == "stamina":
            self.char_info["temp_stamina_bonus"] = self.char_info["stamina_bonus"]
        elif value == "personality":
            self.char_info["temp_personality_bonus"] = self.char_info["personality_bonus"]
        elif value == "luck":
            self.char_info["temp_luck_bonus"] = self.char_info["luck_bonus"]


# Test area:
Charity = Character("charity")
print(Charity)
    

   