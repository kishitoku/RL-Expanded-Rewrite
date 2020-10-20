# Base Actor Class (and examples?)
#
# Actors will be anything (usually a character/person) the player can interact with
# 
# Example Group
#   Example Sub-Group 
#       Written Name (variableName) (type) (other info)
#
# Actors contain:
#   Actor Information
#       Default Name (name) (string)
#       Pet Name (petName) (string)
#       Pet Names (petNames) (set)
#       Dialog Color (dialogColor) (string) (Color can be name of a supported color or a hex #)
#   Actor Stats (actorStats) (dictionary)
#       Actions (?) TODO: Get more info on how actions work
#       Addiction (addiction) (?)
#       Addiction Rate  (addictionRate)  (integer)
#       Addiction Resistance (addictionResist)  (integer)
#       Inhibition (inhbt)  (integer)
#       Love (love)  (integer)
#       Lust (lust)  (integer)
#       Obedience (obed)  (integer)
#   Other Statistics
#       Sexual interactions (N/A) (N/A) (pretty self-explanatory)
#       Dialog interactions (N/A) (N/A) (ex: # of times player spoke w/ them not including intro scenes etc)
#       Any other types of interactions (N/A) (N/A) (tbd/wip stuff)
#   Wardrobe Information
#       Current Layer Settings (N/A) (N/A)
#
# Actors handle:
#   Updates for
#       - Actor Info.
#       - Actor Stats
#       - Interaction Stats
#
# NOTE: Actors do not handle wardrobe changes!

init -2 python:
    import re
    class Actor(renpy.store.object):
        """docstring for Actor"""
        def __init__(self, name, **kwargs):
            # super(Actor, self).__init__()
            self.name = name
            self.petNames = kwargs.get('names',[name,'Nickname','Pet-Name'])
            # self.petName = petNames[0]
            self.dialogColor = kwargs.get('color',"#000000")

            self.actorStats = kwargs.get('actorStats',{'inhbt':1000,'love':0,'lust':0,'obed':0})

            # self.inhbt = kwargs.get('inhbt',1000) #1000 is leftover from og-game 
            # self.love = kwargs.get('love',0)
            # self.lust = kwargs.get('lust',0)
            # self.obed = kwargs.get('obed',0)

            # self.addiction = #???
            self.addictionRate = kwargs.get('addRate',0)
            self.addictionResist = kwargs.get('addResist',0)

            # self.actions = #???

