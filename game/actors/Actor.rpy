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
#       Pet Name (petName) (dictionary?)
#       Dialog Color (color) (string) (Color can be name of a supported color or a hex #)
#   Actor Stats
#       Actions (?) TODO: Get more info on how actions work
#       Addiction (addiction) (?)
#       Addiction Rate  (addictionRate)  (integer)
#       Addiction Resistance (addictionResist)  (integer)
#       Inhibition (inhbt)  (integer)
#       Love (love)  (integer)
#       Lust (lust)  (integer)
#       Obedience (obed)  (integer)
#   Interactions Statistics
#       Sexual interactions (N/A) (N/A) (pretty self-explanatory)
#       Dialog interactions (N/A) (N/A) (ex: # of times player has spoke to them not including intro scenes etc)
#       Any other types of interactions (N/A) (N/A) (tbd/wip stuff)
#   Wardrobe Information
#       Clothes (N/A) (N/A)
#       Accessories (N/A) (N/A)
#       Hair (N/A) (N/A) (style, coloring etc)
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