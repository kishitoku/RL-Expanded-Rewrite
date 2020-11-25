# Image system based on LayeredImage()



# Attempting to define a layeredImage here.
# TODO: Transition this to a statement equivalannt.
# TODO: Tie into Girl().
init python:
    from collections import OrderedDict
    class LayeredImageT(layeredimage.LayeredImage):
        def format(self, what, attribute=None, group=None, variant=None, image=None):
            ff = layeredimage.format_function

            debugvar =  ff(
                what=what,
                name=self.name,
                group=group,
                variant=variant,
                attribute=attribute,
                image=image,
                image_format=self.image_format)
            print "NEW"
            print debugvar
            return debugvar
            
    timg = renpy.image(u'test_body_bare_none',"images/characters/test/test_body_bare_barbell.png")
    timg2= Image("images/characters/test/test_body_bare_none.png")
    tdsp = renpy.Displayable()

    ptest = LayeredImage([
                Attribute("body","none",if_any="bare",variant='bare',default=True,
                image=timg,anchor=(0.0,0.0),zoom=(0.75)),
                #Attribute("body","none",if_not='bare',variant='hairy',default=True),
                #Attribute("head" ,'base',default=True),
                #Attribute("brows",'normal',default=True),
                #Attribute("eyes" ,'normal',default=True),
                #Attribute("mouth",'normal',default=True),
                #Attribute("hair" ,'normal',default=True),
                #Attribute("arms"),
                #Attribute("Chest"),
                ],name='ptest')#,image_format="images/characters/test/{image}.png")
    
    
    
    #prawatt = layeredimage.RawAttribute('none')
    #patt = prawatt.execute(group='body',properties={u'if_any': u'bare', u'variant': u'bare', u'anchor': (0.0, 0.0), u'zoom': 0.75})[0]
    prawattg = layeredimage.RawAttributeGroup('ptest','body')
    prawattg.properties = OrderedDict([(u'if_any', u'"bare"'), (u'auto', 'True'), (u'variant', u'"bare"'), (u'anchor', u'(0.0,0.0)'), (u'zoom', u'0.75')])
    pattg = prawattg.execute()[0]
    prawlimg = layeredimage.RawLayeredImage('ptest')
    prawlimg.children = [prawattg]
    ptest = prawlimg.execute()
    print('TYPE: {}'.format(type(ptest)))
    #ptest = layeredimage.LayeredImage([pattg],name='ptest')
    
    print "DONE"

layeredimage test:
    #image_format "character/test/{image}.png"

    # body > head (eyes > mouth > eyebrows > hair) > breasts > pubes > arms
    attribute body null
    group body if_any "bare" auto variant "bare":
        anchor (0.0,0.0)
        zoom 0.75
        attribute none default

    group body if_not "bare" auto variant "hairy":
        anchor (0.0,0.0)
        zoom 0.75
        attribute none default

    group head auto prefix "head":
        anchor (0.0,0.0)
        zoom 0.75
        attribute base default

    group brows auto prefix "brows":
        anchor (0.0,0.0)
        zoom 0.75
        attribute normal default

    group eyes auto prefix "eyes":
        anchor (0.0,0.0)
        zoom 0.75
        attribute normal default

    group mouth auto prefix "mouth":
        anchor (0.0,0.0)
        zoom 0.75
        attribute normal default

    group hair auto:
        anchor (0.0,0.0)
        zoom 0.75
        attribute normal default

#    attribute pubic null #IDEA: May not work, possible bug
#    group pubic auto

    attribute arms null
    group arms if_any "up" auto variant "up":
        anchor (0.0,0.0)
        zoom 0.75
        attribute collargloves default

    group arms if_not "up" auto variant "normal":
        anchor (0.0,0.0)
        zoom 0.75
        attribute collargloves default

    # Chest layer must happen after arms to avoid bad overlapping.
    group chest auto:
        anchor (0.0,0.0)
        zoom 0.75
        attribute none default

    # bra > panty > inner > lower > dress > outer > neck > wrist
#    group bra auto

    group panty auto

    group lower auto variant "down"

    group lower auto variant "wet"

    group hose auto

    group inner auto

    group inner auto variant "up"

    group bottom auto

    group bottom auto variant "down"

    attribute dress null  #IDEA: See above
    group dress auto

    group outer auto

    group outer auto variant "up"

#IDEA: Check about separating arms and accessories.
    #group neck auto

    #group wrist auto

    group overlay auto multiple

    group overlay auto variant "pussy" multiple

    group overlay auto variant "face" multiple

