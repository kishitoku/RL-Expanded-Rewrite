# Base Actor Class (and examples?)
#
# Actors will be anything (usually a character/person) the player can interact with

init -2 python:
    import re

    # Inventory can be used in two ways:
    # Like a list - Inventory.append()
    # Or like an object - Inventory._money
    class Inventory(renpy.store.object):
        """ """
        def __init__(self, inv, money):
            self._inv = inv
            self._money = money

        def __getitem__(self, item):
            return self._inv[item]

        def __setitem__(self, item):
            pass
