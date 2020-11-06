# wardrobe can call an outfit, events, actors, image handler

init -2 python:

    # single state of a characters current clothing, data store
    # collection of clothing pieces and associated values for things character wears
    class Outfit(renpy.store.object)
        def __init__(self):
            # outfit statistics
            self._nude = 0  # no clothes at all (does not include acces.)
            self._undressed = 0 # aka functionally nude (includes acces.)
            self._upSkirt = 0
            self._upTop = 0
            self._pantiesDown = 0

            """
            layers by priority:
                0 panties
                1 bra
                2 legs (hose)
                3 inner
                4 bottom
                5 dress
                6 top
                7 outer
            """
            
            self.panties = "" # panties
            self.bra = "" # bra
            self.legs = "" # below bottoms
            self.inner = "" # inner top
            self.bottom = "" # legs
            self.dress = "" # duh
            self.top = "" # 
            self.outer = "" #

            def __getpiece__(self,piece):
                try:
                    return self.piece
                except AttributeError:
                    renpy.log("ERROR, OUTFIT PIECE %s DOES NOT EXIST" % piece)

            def __getstat__(self,stat):
                pass

            # functions
            #   check taboo (ex: response from actor)
            #   check exposure
            #   check traits
            #   checks but not the fun/money kind
            # come up with more checks if needed
            

            # self.acc = ["","",""] # top accessories

            
            
            

