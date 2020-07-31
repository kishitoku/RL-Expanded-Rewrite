# Base Game Locations
#
# Location Class allows for quick creation of new locations.
# Add new base game locations to this file.

init -2 python

    class Location(renpy.store.object):
        def __init__(self,
                    name,
                    adjacent,
                    locked = False,
                    path = "backgrounds/",
                    public = False,):
            self.name = name
            self.adjacent = adjacent
            self.isLocked = locked
            self.people = []
            self.public = public

        def getBackground(self, current_time):
            """ Returns background image and path based on time of day.

            Args:
                time_: Current time segment
            Returns:
                string: Path to proper background image file.
            """
            # Uses re modules to run regex on a string that is being formated by the built-in string function.
            if self.public:
                return re.sub('[ ]','_',re.sub('[']','',"{}{}_{}.png".format(self.path,self.name,current_time)).lower)

            else:
                return re.sub('[ ]','_',re.sub('[']','',"{}{}.png".format(self.path,self.name)).lower)

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
        #consider creating a function to do this instead
        # Creates a list of tuples using the location name as a base.
        adjacent = []
        for l in Location.getAdjacent():
            # Replaces any spaces with underscores and forces lowercase on the string
            # for the second entry. This will be used as the format for location labels.
            adjacent.append(tuple(l,re.sub('[ ]','_',re.sub('[']','',l)).lower))

        adjacent.append("Don't go anywhere")

        # Displays a menu of locations found in adjacent
        nextLoc = renpy.display_menu(adjacent, interact = True)

        # Jumps to chosen location label
        renpy.jump(nextLoc)


# Test definition using Location.
define university_square = Location("University Square", ["Classroom","Danger Room"])
define classroom = Location("Classroom",["University Square","Danger Room"])
define danger_room = Location("Danger Room",["University Square","Classroom"])

# Test label using Location.
label university_square
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
        "Go somewhere else"
            $ locationMenu(university_square)

    jump university_square

label danger_room
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
        "Go somewhere else"
            $ locationMenu(danger_room)

    jump danger_room

label classroom
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
        "Go somewhere else"
            $ locationMenu(classroom)

    jump classroom
