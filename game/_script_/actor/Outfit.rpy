# Outfit Class
#
# Instanced for all Actor(renpy.store.object) objects

init -2 python:
    # single state of a characters current clothing, data store
    # collection of clothing pieces and associated vals. for things character wears
    class Outfit(renpy.store.object):
        def __init__(self, **kwargs):
            # outfit statistics
            self._nude = 0  # no clothes at all (does not include acces.)
            self._undressed = 0 # aka functionally nude (includes acces.)
            self._upSkirt = 0
            self._upTop = 0
            self._pantiesDown = 0

            # outfit other stats
            self._exposure = 0
            self._shame = 0 # move this over to actor?
            
            # outfit layers
            self.panties = kwargs.pop('panties',"N/A") # panties
            self.bra = kwargs.pop('bra',"N/A") # bra
            self.legs = kwargs.pop('leg',"N/A") # below bottoms
            self.inner = kwargs.pop('inner',"N/A") # inner top
            self.bottom = kwargs.pop('bottom',"N/A") # legs
            self.dress = kwargs.pop('dress',"N/A") # "full-body" clothing
            self.top = kwargs.pop('top',"N/A") # upper body
            self.outer = kwargs.pop('outer',"N/A") # upper body (ex: jackets, coats)

            self.layers = [self.panties, self.bra, self.legs, 
                            self.inner, self.bottom, self.dress, self.top, self.outer]

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
        def getLayers(self):
            strOut = ""
            for i, v in enumerate(self.layers):
                strOut += "Layer {}: {}\n".format(i,v)
                # renpy.log(strOut)
            return strOut

        def getExposure(self):
            try:
                return self._exposure
            except AttributeError:
                renpy.log("ERROR, ATTRIBUTE %s DOES NOT EXIST" % _exposure)

            # functions
            #   check taboo (ex: response from actor)
            #   check exposure
            #   check traits
            #   checks but not the fun/money kind
            # come up with more checks if needed
            

            # self.acc = ["","",""] # top accessories
