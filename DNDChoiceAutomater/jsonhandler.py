import json
import os
class JSONHandler():
    """Handles specific JSON formatting and creating not tied specificly to Characters."""
    def charSpelljsonFormatter(self, data, fullInfo:bool=False):
        """Formats and return spell data into a pretty formatted string.
           Helper method to getSpellInfo.
           """
        forgotten_status = "not been forgotten" if not data['forgotten'] else "been forgotten"
        basicInfoString = "Spell {} has {} and its mercirual magic is {}. Spell check for this spell is +{} and you can find more info on page {}.".format(data['name'], forgotten_status, data['mercurial'],data['spell_check'], data['page_number'])
        #Depedning on basicInfoData then return a different string.
        if fullInfo:
            moreInfoString = "\nSpell tier and its effects:\n {}".format(data['1rst_level'])
            return basicInfoString + moreInfoString
        else:
            return basicInfoString
    def writeToFile(self, data):
        pass