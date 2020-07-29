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

            #create function to handle backgrounds instead. Need day, evening, night
            #or just a regular backgroun. Function should choose based on outside.
            self.background_ = "{}{}.png".format(path,name)

        def setBackground(name, path, public):
            pass

        def getLocked():
            return self.isLocked

        def setLocked(locked):
            self.isLocked = locked

        def getAdjacent():
            return self.adjacent

        def clearLocation():
            self.people.clear()

        def addPerson(person):
            self.people.append(person)

        def getPeople():
            return self.people

label locationMenu(Location):

    python:

        #consider creating a function to do this instead
        # Creates a list of tuples using the location name as a base.
        adjacent = []
        for l in Location.getAdjacent():
            # Replaces any spaces with underscores and forces lowercase on the string
            # for the second entry. This will be used as the format for location labels.
            adjacent.append(tuple(l,l.lower(re.sub('[ ']','',l))))

        # Displays a menu of locations found in adjacent
        nextLoc = renpy.display_menu(adjacent, interact = True)

        # Jumps to chosen location label
        renpy.jump(nextLoc)
