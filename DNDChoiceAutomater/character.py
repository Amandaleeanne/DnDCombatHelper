
from roller import Dice
import json
import os
'''
TODO:
-Make the Character method create new characters
-Save changed data
-get what happens at different rolls of a character (might be handled by a different script)
'''
class Character():
    """Handles the JSON files and reads and edits them based on main script."""
#----------------------Initalizing Methods --------------------------------
    def __init__(self, character:str): 
    #{
        #Ensure you are in the correct directory:
        os.chdir(os.path.dirname(__file__))
        #Get name
        self.name = character.lower()
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
            self.data = json.load(f)
        
        #initialize one element list:
        self.char_info = self.data['info'][0]
        self.char_spellData = self.data['spells']
        #Check to see if character is a spellcaster:
        if self.char_info["iswizard"] is True or self.char_info["iscleric"] is True:
            self.spellcaster = True
            #Load data into current environment
            with open('spells.json', 'r') as f:
                self.spellData = json.load(f)

            #Get spells from character and add to spell list:
            self.spellList = []
            #For every spell
            for spell in self.data["spells"]:
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
#----------------------Non Initalizing Methods: Change --------------------------------

    def changeValue(self, value:str, number:int=0, reset:bool=False): #WORKING
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

    def _calculateValue(self, number, value, valid_value_map): #WORKING
    #{
        """Calculates new temporary value based on given number and value keys."""
        key = valid_value_map.get(value)
        self.char_info[key] += number
    #}
    def _resetValue(self, value, valid_value_map): #WORKING
    #{
        """Resets the temporary value to match the actual value"""
        key = valid_value_map.get(value)
        self.char_info[key] == self.char_info.get(value)
    #}
#----------------------Non Initalizing Methods: Set --------------------------------

    def setValue(self,key:str, value):#RETEST
    #{
        """ Sets the permanent stat value of a character to number or boolean given. """

        #Set and check values
        valid_values = ['name', 'level', 'critdie_level', 'ac', 'hp', 'strength_bonus', 'feat_bonus', 'feat_die_level', 
                        'agility_bonus', 'stamina_bonus', 'personality_bonus', 'luck_bonus', 'intellect_bonus', 
                        'iswizard', 'iswarrior', 'isthief', 'iscleric']
        bool_values = ['iswizard', 'iswarrior', 'isthief', 'iscleric']
        try:
            if key not in valid_values: raise ValueError
            else:
                    if value is bool or value is str:
                        self.char_info[key] = value
                    else: raise ValueError
        except ValueError:
            print("Invalue value to change given. valid: {}\n or {}".format(valid_values, bool_values))
    #}
    def setForgotten(self,spellName): #WORKING
    #{
        """
        Changes a spell to forgotten or not forgotten based on 
        what it already is. (Flips the value)
        Can enter in a list of spell names (str)
        """
        #determine if its a string:
        try:
            #see if the spell is valid:
            if spellName not in self.spellList:
                raise ValueError
            else:
                #get the spell to for
                for spell in self.data['spells']:
                    if spell['name'] == spellName:
                    #flip boolean value;
                        if not spell['forgotten']:
                            spell['forgotten'] = True
                        else:
                            spell['forgotten'] = False
                        break
        except:
            print("Invalid value to change given. \nvalid: {}\n given: {}".format(self.spellList, spellName))
    #}
    def setSpellcheck(self,spellName:str, number): #WORKING
    #{
        """
        Changes a spells spell check value.
        """
        #see if the spell is valid:
        try:
            if spellName not in self.spellList:
                raise ValueError
            else:
                #get the spell to for
                for spell in self.data['spells']:
                    if spell['name'] == spellName:
                    #change the spell to the value;
                        spell['spell_check'] = number
                        break
        except:
            print("Invalid value to change given. \nvalid: {}\n given: {}".format(self.spellList, spellName))
    #}
    def setMultiple(self, changeWhat:str, toChange): #TEST, 'forgotten' workiNG
    #{
        """
        Takes a list or dictionary (toChange) and sets multiple spell forotten or character info values.
        changeWhat recieves a string 'forgotten', 'reset', 'setInfo', and 'change'.
        'forgotten' : list of spells, use to flip the forgotten or not forgotten.
        'setInfo' : dict, sets the permanent value of the given key:value pairs.
        'spellInfo' : list, gets the basic spell info related to the character.
        'change' : dict, Sets the temporary valuee of the given key:value pairs.
        'reset': list of charater info ('ac','hp'), resets the temporary values.
        List must be a list of strings and are used for forgetting spells.
        dictionary must be a dictionary of str:int or str:bool pairs.

        """
        #Confirm type
        if type(toChange) == list:
            #Change corresponding type
            if changeWhat == 'forgotten':
                for spell in toChange:
                    if spell in self.spellList:
                        self.setForgotten(spell)
            elif changeWhat == 'reset':
                for change in toChange:
                    self._resetValue(change)
            elif changeWhat == 'spellInfo':
                for spell in toChange:
                    print(self.getSpellInfo(spell))
            else:
                print("invalid changeWhat value, list")
        #Confirm type
        elif type(toChange) == dict:
            #Change corresponding type
            if changeWhat == 'change':
                keys = toChange.keys()
                for key in keys:
                    self.changeValue(key, toChange[key])
            elif changeWhat == 'setInfo':
                keys = toChange.keys()
                for key in keys:
                    self.setValue(key, toChange[key])
        else:
            print("Invalid list/dictionary type. Did not recieve a list or dictionary. \nOR did not recive a valid toChange string.")
    #}

    

#----------------------Non Initalizing Methods: Get --------------------------------

    def getSpellInfo(self, spellName, fullInfo:bool=False):#WORKING
        """
        Returns string info about a spell.
        Can show full information about a spell or just character specific traits.
        """
        try:
            if not self.spellcaster:
                raise NameError
            else:
                #Get specified spell
                for spell in self.data['spells']:
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
                    return self.charSpelljsonFormatter(allSpellData, True)
                return self.charSpelljsonFormatter(basicInfoData, False)
        except NameError:
            print("ERROR: Not a spellcaster")
    #@TODO: Make method
    def getSpellData(self, spellRoll):
        """
        Returns spell data for a given spell in a list. Use of this method is to
        retrieve what happens when a roll is say, 12 or 24 to program as well as
        throw an error or tell if the spell is forgotten for programming pourposes.
        [dice_level_effect:int,mercurial_dice_level:int,spell_effect_bonus:int,full_description:string ]
        
        """
    def getSpells(self):
        """Returns known spell list"""
        return self.spellList
#----------------------Non Initalizing Methods: MISC --------------------------------
    def writeToFile(self,resetTemp:bool=False):
        """
            Saves existing temporary data and spell data.
            if resetTemp is True, temporary data and spell data will be reset
        """
        #Match up all data
        self.data['info'][0] = self.char_info
        self.data['spells'] = self.char_spellData
        #open and push data to file.
        with open('{}.json'.format(self.name), 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def charSpelljsonFormatter(self, data:dict, fullInfo:bool=False):
       """Formats and return spell data into a pretty formatted string.
          Helper method to getSpellInfo.
          """
       forgotten_status = "not been forgotten" if not data['forgotten'] else "been forgotten"
       basicInfoString = "Spell {}{} has {} and its mercirual magic is {}. Spell check for this spell is +{} and you can find more info on page {}.".format(data['name'][0].upper(),data['name'][1:], forgotten_status, data['mercurial'],data['spell_check'], data['page_number'])
       #Depedning on basicInfoData then return a different string.
       if fullInfo:
           moreInfoString = "\nSpell tier and its effects:\n {}".format(data['1rst_level'])
           return basicInfoString + moreInfoString
       else:
           return basicInfoString




# Test area:
Charity = Character("charity")
print(Charity)
listt = ['magic_missile','sleep']
print('Type of toChange is:{}'.format(type(list)))
Charity.setMultiple('spellInfo', listt)

   