# Base Game Locations
#
# Location Class allows for quick creation of new locations.
# Add new base game locations to this file.

init -1 python

    class Location(renpy.store.object):
        def __init__(self,
                    name,
                    adjacent,
                    locked = False,
                    path = "backgrounds/",
                    outside = False,):
            self.name = name
            self.adjacent = adjacent
            self.locked = locked
            self.people = []
            self.background_ = "{}{}.png".format(path,name)

        def getLocked():
            return self.locked

        def setLocked(locked):
            self.locked = locked

        def getAdjacent():
            return self.adjacent

        def clearLocation():
            self.people.clear()

        def addPerson(person):
            self.people.append(person)

        def getPeople():
            return self.people

label locationMenu(location):

    python:
        adjacent = []
        for p in location.getAdjacent():
            adjacent.append(tuple(p,p.lower(p.replace(" ","_"))))
