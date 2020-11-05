init -2 python:

    # single state of a characters current clothing
    class Outfit(renpy.store.object)
        """ data store """
        # collection of clothing pieces and associated values for things character wears
        # wardrobe can call an outfit, events, actors, image handler
        def __init__(self):
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

            # functions
            #   check taboo (ex: response from actor)
            #   check exposure
            #   check traits
            #   checks but not the fun/money kind
            

            # self.acc = ["","",""] # top accessories

            
            
            

