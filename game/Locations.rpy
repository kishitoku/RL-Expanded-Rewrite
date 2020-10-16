# Base Game Locations
#
# Location Class allows for quick creation of new locations.
# Add new base game locations to this file.

init -2 python:
    import re

    class Location(renpy.store.object):
        def __init__(self, name, adjacent, **kwargs):
            self.name = name
            self.trimmed = re.sub('[ ]','_',re.sub("[']",'',self.name)).lower()
            self.people = []
            self.dayCycle = kwargs.get('dayCycle', False)
            self.isLocked = kwargs.get('locked', False)
            self.path = kwargs.get('path', "/images/backgrounds/")
            self.public = kwargs.get('public', 100)


            # Replaces any spaces with underscores and forces lowercase on the string
            # for use as a jump to label. This will be used as the format for location labels.
            self.jumpTo = [re.sub('[ ]','_',re.sub("[']",'',loc)).lower() for loc in adjacent]
            # Iterate through adjacent, create a tuple, and append to self.adjacent
            self.adjacent = [(adjacent[i], self.jumpTo[i]) for i in range(0, len(adjacent))]
            # Add a leave line at the end.
            self.adjacent.append(("Don't go anywhere",self.trimmed))

            # Defines renpy images for location background based on if the location has
            # time variants or not
            if self.dayCycle:
                renpy.image("bg {}_{}".format(self.trimmed,"day") ,"{}{}_{}.png".format(self.path,self.trimmed,"day"))
                renpy.image("bg {}_{}".format(self.trimmed,"evening") ,"{}{}_{}.png".format(self.path,self.trimmed,"evening"))
                renpy.image("bg {}_{}".format(self.trimmed,"night") ,"{}{}_{}.png".format(self.path,self.trimmed,"night"))

            else:
                renpy.image("bg {}".format(self.trimmed) ,"{}{}.png".format(self.path,self.trimmed))

        def getBackground(self):
            """ Returns background image based on time of day.

            Returns:
                string: Proper renpy image name.
            """
            if self.dayCycle:
                return "bg {}_{}".format(self.trimmed,current_time.lower())
            else:
                return "bg {}".format(self.trimmed)


        def getLocked(self):
            return self.isLocked

        def setLocked(self, locked):
            self.isLocked = locked

        def getAdjacent(self):
            return self.adjacent

        def clearLocation(self):
            self.people.clear()

        def addPerson(self, person):
            self.people.append(person)

        def getPeople(self):
            return self.people


    def locationMenu(Location):

        # Displays a menu of locations found in adjacent
        nextLoc = renpy.display_menu(Location.getAdjacent(), interact = True)

        # Jumps to chosen location label
        renpy.jump(nextLoc)


# Test definition using Location.
define testenv = Location("University Square", adjacent=
                            ["Classroom","Danger Room", "Image Test"], dayCycle=True)
define classroom = Location("Classroom",["University Square","Danger Room"])
define danger_room = Location("Danger Room",["University Square","Classroom"], public = 50)

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
        "Go somewhere else":
            $ locationMenu(testenv)

    jump testenv

label danger_room:
    $ renpy.scene()
    $ renpy.show(danger_room.getBackground())
    menu:
        "You are in the Danger Room. What would you like to do?"

        "Chat":
            #call Chat
            pass
        "Wait" if current_time != "Night":
            "You wait around a bit."
            # call Wait
            # call EventCalls
            # call Girls_Location
            pass
        "Go somewhere else":
            $ locationMenu(danger_room)

    jump danger_room

label classroom:
    $ renpy.scene()
    $ renpy.show(classroom.getBackground())
    menu:
        "You are in the Classroom. What would you like to do?"

        "Chat":
            #call Chat
            pass
        "Wait" if current_time != "Night":
            "You wait around a bit."
            # call Wait
            # call EventCalls
            # call Girls_Location
            pass
        "Go somewhere else":
            $ locationMenu(classroom)

    jump classroom
