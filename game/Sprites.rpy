# Image system based on LayeredImage()
#
#
#


# Attempting to define a layeredImage here.
# TODO: Transition this to a statement equivalannt.
# TODO: Tie into Girl().
layeredimage test standing:
    #image_format "character/test/{image}.png"

    # body > head (eyes > mouth > eyebrows > hair) > breasts > pubes > arms
    group body auto:
        attribute bare default

    group body auto variant "hairy":
        attribute bare default

    group head auto prefix "head":
        attribute base default

    group brows auto prefix "brows":
        attribute normal default

    group eyes auto prefix "eyes":
        attribute normal default

    group mouth auto:
        attribute normal default

    group hair auto:
        attribute normal default

    group chest auto:
        attribute bare default

#    attribute pubic null #IDEA: May not work, possible bug
#    group pubic auto

    group arms auto:
        attribute bare default

    group arms auto variant "up":
        attribute bare default

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


# Test label for layeredimage
# TODO: Make a proper sprite test environment
# TODO: Remove this label
label imageTest:

    show test

    #Base test
    test bare "I should be bare."
    test "I should even be bare down there!"
    test hairy "Not any more though."
    test hairy gloves "I prefer to wear gloves even when naked."
    test "If this worked, the test should end now and return you to the menu."

    jump university_square
