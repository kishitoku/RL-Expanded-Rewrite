# Testing Enviroment
#
# This file is for all major/minor testing. This eventually be replaced by playground mode (Fully functional game but w/ dev cheats)

define testenv = Location("University Square", adjacent=
                            ["Classroom","Danger Room", "Image Test"], dayCycle=True)

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
        "Image System Test":
            jump imageTest
        "Main Menu":
            $ MainMenu(confirm=False)()
        "Go somewhere else":
            $ locationMenu(testenv)

    jump testenv