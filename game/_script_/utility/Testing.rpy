# Testing Enviroment
#
# This file is for all major/minor testing. This eventually be replaced by playground mode 
# (Functional "gameplay-loop" but w/ dev cheats)

define testenv = Location("University Square", adjacent=
                            ["Classroom","Danger Room", "Image Test"], dayCycle=True)

define exampleOutfit = Outfit(top="Nothing")
init python:
    class permachar(renpy.character.ADVCharacter):
        def __init__(s, name, **kwargs):
            s.name = name
            s.argpile = {}
        def __setitem__(s,key,value):
            s.argpile.update({key:value})
        def __getitem__(s,key):
            return argpile[key]
        
        

# Test label for layeredimage
# TODO: Make a proper sprite test environment
# TODO: Remove this label
label imageTest:

    show test

    "This is the layeredimage system test."

    #Base test
    test bare "I should be bare."
    test "I should even be bare down there!"
    show test -bare
    test none "Not any more though."
    show test -none
    test "I prefer to wear gloves even when naked."
    show test
    test "Starting baseline actor reference"
    show ptest
    ptest "Now showing prototype persistent-wardrobe actor"
    show test up
    test "If this worked, the test should end now and return you to the menu."

    jump testenv


# Testing label for Wardrobe System
label wardTest:
    show danger_room
    # call wardrobe # this is where I would summon a wardrobe system
    ## IF I HAD ONE
    # "Outfit Piece Logged"
    menu:
        "Get Piece Names":
            $ print(exampleOutfit.getLayers())
        "Back":
            jump testenv
        # "Main Menu":
        #     $ MainMenu(confirm=False)()
    jump wardTest

# Test label using Location.
label testenv:
    $ renpy.scene()
    $ renpy.show(testenv.getBackground())
    menu:
        "You are in the University Square. What would you like to do?"

        "Chat":
            #call Chat
            pass
        "Wait" if current_time != "Night":
            "You wait around a bit."
            # call Wait
            # call EventCalls
            # call Girls_Location
            pass
        "Systems Testing":
            menu:
                "Image System Test":
                    jump imageTest
                "Wardrobe System Test":
                    jump wardTest
                "Back":
                    jump testenv
        "Go somewhere else":
            $ locationMenu(testenv)
        "Main Menu":
            $ MainMenu(confirm=False)()

    jump testenv