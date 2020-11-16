# Wardrobe Class
#
# Instanced for all Actor(renpy.store.object) objects


init -2 python:

    # Wardrobe takes care of tracking a characters complete clothes and outfit sets
    class Wardrobe(renpy.store.object):              
        def __init__(self, fallback, outfits):
            """
            Wardrobe contains the Outfits for a character 
            and handles changing the active outfit

            :param fallback: fallback/default outfit for a character
            :type fallback: Outfit(renpy.store.object)
            :param outfits: Collection of possible outfits for Actor
            :type outfits: Set (TODO: change data structure used?)
            """
            self.active = fallback
            self.fallback = fallback
            self.outfits = outfits
