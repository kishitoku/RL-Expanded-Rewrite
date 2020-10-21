# Base Actor Class (and examples?)
#
# Actors will be anything (usually a character/person) the player can interact with
# 
# Example Group
#   Example Sub-Group 
#       Written Name (variableName) (type) (other info)
#
# Actors contain:
#   Actor Information (N/A) (N/A)
#       Default Name (name) (string)
#       Pet Name (petName) (string)
#       Pet Names (petNames) (set)
#       Dialog Color (dialogColor) (string) (name of supported color or hex #)
#   Actor Stats (actorStats) (dictionary)
#       Addiction (addiction) (integer) (0-100)
#       Addiction Rate  (addRate)  (integer) (0-10)
#       Addiction Resistance (addResist)  (integer) (0-3)
#       Inhibition (inhbt)  (integer) (1000-0)
#       Love (love)  (integer) (0-1000)
#       Lust (lust)  (integer) (0-100)
#       Obedience (obed)  (integer) (0-1000)
#   Other Statistics (N/A) (N/A)
#       Actions (?) TODO: Get more info on how actions work
#       Sexual interactions (N/A) (N/A) (pretty self-explanatory)
#       Dialog interactions (N/A) (N/A) (ex: # of times player spoke w/ them not including intro scenes etc)
#       Any other types of interactions (N/A) (N/A) (tbd/wip stuff)
#   Wardrobe Information (N/A) (N/A)
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
        def __init__(self, actorName, name, **kwargs):
            # super(Actor, self).__init__()
            self.actorName = actorName # Programmers needs come first :P
            self.name = name
            self.petNames = kwargs.get('names',[name,'Nickname','Pet-Name'])
            # self.petName = petNames[0]
            self.dialogColor = kwargs.get('dialogColor',"#000000")

            self.actorStats = kwargs.get('actorStats',{'addiction':0,'addRate':0,'addResist':0,'inhbt':1000,'love':0,'lust':0,'obed':0})

            # self.actions = #???
            
