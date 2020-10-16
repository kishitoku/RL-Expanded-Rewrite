
image study_day = "StudyDay.jpg"

define p = Character("Zero",
                     who_color="#000000")

$ PlayerSkinTone = "#028800"

label intro:
    $ renpy.scene()
    $ renpy.show("study_day")

    "YOU'VE ARRIVED IN EARLY EVENING AT THE XAVIER INSTITUE, WHERE YOU'VE BEEN PROMISED A NEW HOME."

    "THINGS HAVE BEEN TOUGHT FOR MUTANTS IN THE YEARS SINCE APOCALYPSE'S FALL, BUT THIS SOUNDS LIKE IT MIGHT BE A GOOD DEAL."

    # "SELECT CHARACTER NAME HERE"

    $ p.name = renpy.input("What is your name?", default="Zero", length = 10)

    "[p.name]"

    # if in developer mode, test player text color

    if config.developer:
        $ renpy.say(p, "text")

    menu:
        "What is your skin color?"
        "Green":
            $ PlayerSkinTone = "#028800"
        "Black":
            $ PlayerSkinTone = "#7a4e0a"
        "Brown":
            $ PlayerSkinTone ="#ad7114"
        "White":
            $ PlayerSkinTone = "#000cff"

    if config.developer:
        $ renpy.say(p, "text")
