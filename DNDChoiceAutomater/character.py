
from roller import Dice
import json
import os
class Character():
    """Handles the JSON files and reads and edits them based on main script."""
#----------------------Initalizing Methods --------------------------------
    def __init__(self, character:str): 
    #{
        #Ensure you are in the correct directory:
        os.chdir(os.path.dirname(__file__))
        #Get name
        self.name = character
        #if file with name exists:
        self._get_character()
        #else:
        #make a new character  
    #}

    def __str__(self) -> str:
    #{
        """Returns a string representation of Character class, giving information about the current character."""

        if self.spellcaster is True:
            if self.char_info["iswizard"] == True:
                return "The character {}{} is a Wizard, and knows spells {}. Their HP is {}, AC is {}, and have a base spell bonus of {}".format(self.name[0].upper(), self.name[1:], self.spellList, self.char_info["hp"], self.char_info["ac"],(self.char_info["level"]+self.char_info["intellect_bonus"]))
            else:
                return "The character {}{} is a Cleric, and knows spells {}. Their HP is {}, AC is {}, and have a base spell bonus of {}".format(self.name[0].upper(), self.name[1:], self.spellList, self.char_info["hp"], self.char_info["ac"],(self.char_info["level"]+self.char_info["intellect_bonus"]))
        elif self.char_info["iswarrior"]== True:
            return "The character {}{} is a Warrior.".format(self.name[0].upper(), self.name[1:])
        else:
            return "The character {}{} is a Thief".format(self.name[0].upper(), self.name[1:])
    #}

    
    def _get_character(self):
    #{
        """Reads existing JSON file and loads nessisary info into environment"""
        #Load data into current environment
        with open('{}.json'.format(self.name), 'r') as f:
            self.infoData = json.load(f)
        
        #initialize one element list:
        self.char_info = self.infoData['info'][0]
        self.char_spellData = self.infoData['spells']
        #Check to see if character is a spellcaster:
        if self.char_info["iswizard"] is True or self.char_info["iscleric"] is True:
            self.spellcaster = True
            #Load data into current environment
            with open('spells.json', 'r') as f:
                self.spellData = json.load(f)

            #Get spells from character and add to spell list:
            self.spellList = []
            #For every spell
            for spell in self.infoData["spells"]:
                #get spell name and add to list
                self.spellList.append(spell['name'])
                '''@TODO: Note the JSON spell file will handle all the the spell effects from 12-32 
                as i belive it is the same for every spell. 
                Then the helper function here will simply get what that spell does'''
    #}
    #TODO: make method
    def _new_character(self):
    #{
        pass
    #}
#----------------------Non Initalizing Methods: Change and set --------------------------------

    def changeValue(self, value:str, number:int=0, reset:bool=False):
    #{
        """
        Changes the temporary value of the character, ENTER IN POSITIVE OR NEGITIVE. 
        Default value for resetting the temporary value is False.

        """
        
        #Initalize valid values
        valid_value_map = {
                "ac": "temp_AC",
                "hp": "temp_hp",
                "strength_bonus": "temp_strength_bonus",
                "agility_bonus": "temp_agility_bonus",
                "stamina_bonus": "temp_stamina_bonus",
                "personality_bonus": "temp_personality_bonus",
                "luck_bonus": "temp_luck_bonus",
                "intellect_bonus": "temp_intellect_bonus",
                }

        #Check to see if there is a valid value to change
        try:
            if value not in valid_value_map:
                raise ValueError
            else:
                #If there is, check to see if its removing or adding the bonus.
                if not reset:
                    self._calculateValue(number, value, valid_value_map)
                else:
                    self._resetValue(value, valid_value_map)
        except ValueError:
            print("ValueError: Invalue value to change given. valid: \n{}".format(valid_value_map))
    #}

    def setValue(self,value:str, number:int=0, boolValue:bool=False):
    #{
        """ Sets the permanent value of a character to number or boolean given. """

        #Set and check values
        valid_values = ['name', 'level', 'critdie_level', 'ac', 'hp', 'strength_bonus', 'feat_bonus', 'feat_die_level', 
                        'agility_bonus', 'stamina_bonus', 'personality_bonus', 'luck_bonus', 'intellect_bonus', 
                        'iswizard', 'iswarrior', 'isthief', 'iscleric']
        valid_bool_values = ['iswizard', 'iswarrior', 'isthief', 'iscleric']
        try:
            if value not in valid_values: raise ValueError
            else:
                #If valid, determine if changing a boolean value.
                if value not in valid_bool_values: 
                    self.char_info[value] = number
                else:
                    self.char_info[value] = boolValue
        except ValueError:
            print("Invalue value to change given. valid: {}\n or {}".format(valid_values, valid_bool_values))
    #}
    def setForgotten(self,spellName:str,boolValue:bool=False):
        """
        Changes a spell to forgotten or not forgotten
        """
        #see if the spell is valid:
        try:
            if spellName not in self.spellList:
                raise ValueError
            else:
                #get the spell to for
                for spell in self.infoData['spells']:
                    if spell['name'] == spellName:
                    #change the spell to the boolean value;
                        spell['forgotten'] = boolValue
                        break
        except:
            print("Invalid value to change given. \nvalid: {}\n given: {}".format(self.spellList, spellName))
   
    def _resetValue(self, value, valid_value_map): #WORKING
    #{
        """Resets the temporary value to match the actual value"""
        key = valid_value_map.get(value)
        self.char_info[key] == self.char_info.get(value)
    #}
    
    def _calculateValue(self, number, value, valid_value_map): #WORKING
    #{
        """Calculates new temporary value based on given number and value keys."""
        key = valid_value_map.get(value)
        self.char_info[key] += number
    #}

#------------------------------Get Methods ------------------------------
    def getSpellInfo(self, spellName, fullInfo:bool=False):
        """
        Returns info about a spell.
        Can show full information about a spell or just character specific traits.
        """
        try:
            if not self.spellcaster:
                raise NameError
            else:
                #Get specified spell
                for spell in self.infoData['spells']:
                    if spell['name'] == spellName:
                        #assign spell data specific to character
                        basicInfoData = spell
                        break
                #get spell data based on spells.json:
                if fullInfo:
                    if self.char_info['iswizard'] is True:
                        for spell in self.spellData['wizard']:
                        #pull spells from wizard only and match data based on name
                            if spell['name'] == spellName:
                                fullSpellInfo = spell
                                break
                    else:
                        for spell in self.spellData['cleric']:
                        #pull spells from cleric only and match data based on name
                            if spell['name'] == spellName:
                                fullSpellInfo = spell
                                break
                    #Combine data dictionaries
                    allSpellData= {**basicInfoData, **fullSpellInfo}
                    return self._charSpelljsonFormatter(allSpellData)
                return self._charSpelljsonFormatter(basicInfoData, False)
        except NameError:
            print("ERROR: Not a spellcaster")
#--------------- MISC Methods--------------------------------
    def _charSpelljsonFormatter(self, data, basicInfoData:bool=False):
        """Formats and return spell data into a pretty formatted string.
           Helper method to getSpellInfo.
           """
        #Depedning on basicInfoData then return a different string.
        if basicInfoData:
            forgotten_status = "not been forgotten" if not data['forgotten'] else "been forgotten"
            return "Spell {} has {} and its mercirual magic is {}. Spell check for this spell is +{} and you can find more info on page {}".format(data['name'], forgotten_status, data['mercurial'],data['spell_check'], data['page_number'])
        else:
            pass




# Test area:
Charity = Character("charity")
print(Charity.getSpellInfo("magic_missile"))
#setValue(value:str, boolValue:bool=False, number:int=0, spellName:str=None):
Charity.setForgotten('magic_missile', True)
print(Charity.getSpellInfo("magic_missile"))


    

   