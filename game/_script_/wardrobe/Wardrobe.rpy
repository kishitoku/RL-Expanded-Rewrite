# wardrobe can call an outfit, events, actors, image handler

init -2 python:

    # single state of a characters current clothing, data store
    # collection of clothing pieces and associated values for things character wears
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
            self.panties = kwargs.get('panties',"N/A") # panties
            self.bra = kwargs.get('bra',"N/A") # bra
            self.legs = kwargs.get('leg',"N/A") # below bottoms
            self.inner = kwargs.get('inner',"N/A") # inner top
            self.bottom = kwargs.get('bottom',"N/A") # legs
            self.dress = kwargs.get('dress',"N/A") # duh
            self.top = kwargs.get('top',"N/A") # 
            self.outer = kwargs.get('outer',"N/A") #

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
        def getLayers(self, justPrint):
            if justPrint:
                for i, v in enumerate(self.layers):
                    print("Layer {}: {}".format(i,v))
                return
            strOut = ""
            for i, v in enumerate(self.layers):
                strOut += "Layer {}: {}\n".format(i,v)
                if i+1 > len(self.layers):
                    strOut += "Layer {}: {}".format(i,v)
                renpy.log(strOut)
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
            
            
            

