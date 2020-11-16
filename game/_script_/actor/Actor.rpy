# Base Actor Class (and examples?)
#
# Actors will be anything (usually a character/person) the player can interact with

"""
Actor INTENT:
    (data storage) RELATIONSHIPS (helper functions)
    ADVCharacter extended functionality
    INVENTORY (object)
    WARDROBE (object)
    SCHEDULE (?)
    SEX
    STATS (dynamic)
        parsed variables
        relationships
        ex: Actor.statA (after creation)
    LOCATION
        current, past, going, home
    ACTIONS (MAYBE: integrate action history w/ dialog history?)
        current,
"""

init -2 python:
    import re

    class Actor(renpy.store.ADVCharacter):                
        def __init__(self, name, **kwargs):
            """
            Actors are all non-player characters whom the player might interact with.
            TODO: Layout definition of Actor a little more precisely?

            :param name: [description]
            :type name: string
            """                   

            ### DEFAULT

            # Actor's Name
            # Seperate from actName so we can have thing's like "Player's Conscience",
            # thus keeping problems related to our Actor's name have special characters-
            # minimized if not outright prevented.
            self.name = name
            # Actor's Name for progammatic purposes
            # TODO: Get a better regex to replace the copied from location below
            self.actName =  = re.sub('[ ]','_',re.sub("[']",'',self.name)).lower()

            # Constructs a ADVCharacter(object) or Adventure Character,
            # to be used for dialog etc.
            # TODO: Add param(s) for character base image
            #       (This will be overlayed with the Outfit as a LayeredImage)
            # TODO: Add params (etc) which determine prefixes and suffixes
            self.ADVChar = ADVCharacter(actName)

            ### INVENTORY

            # Construct Actor's Inventory(renpy.store.object) (_script_/actor/Inventory.rpy)
            # TODO: Scope out how inventory is used for NPCs (because atm,
            #       it seems like having a player-like inventory is pretty impractical)
            self.inventory = Inventory()

            ### CLOTHING AND WARDROBE

            # Construct Actor's Wardrobe(renpy.store.object) (_script_/actor/Wardrobe.rpy)
            # Contains a default fallback outfit and a Set of possible outfits
            self.wardrobe = Wardrobe(kwargs.pop('fallback',"nude"),
                                        kwargs.pop('outfits',{"nude","clothed"}))
            # Set Actor's Active Outfit(renpy.store.object) (_script_/actor/Outfit.rpy)
            self.outfit = wardrobe.active

            ### SCHEDULE AND BEHAVIOR

            # Construct Actor's Schedule(renpy.store.object) (_script_/actor/Schedule.rpy)
            self.schedule = Schedule()

