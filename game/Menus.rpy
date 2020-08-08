# Dynamic Menu
#
# Generates menus in a specified order.


init python:

    def getMenuOptions(Location):
        options = []
        if Location.getPeople():
            options.append(("Chat","chat"))
        #options.append(("Cell Phone","cell_phone")) #Uncomment to test phone. Remove if adding clickable phone.
        if current_time is not "Night":
            options.append(("Wait Here","wait"))
        return options

    def dynamicMenu(Location):

        # Call event handler to check for proccable events.

        # Get regular menu options
        options = getMenuOptions(Location)
        # Get location specific menu options (events)
        options.extend(Location.getMenu())
        options.append(("Move To", "locationMenu"))

        select = renpy.display_menu(options)

        renpy.jump(select)
