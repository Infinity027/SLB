init 1:
    layeredimage bg mallmap:
        always:
            "mallmap"

init python:
    Room(**{
    "name":"mallmap",
    "exits": [
        "mall1",
        "bakery",
        "bookstore",
        "clothesshop",
        "arcade",
        "tattooshop",
        "mall2",
        "flowershop",
        "coffeeshop",
        "electronic",
        "drugstore",
        "jewelrystore"
        ],
    "hours": (7, 18),
    "conditions": [
        IsHour(7, 18),
        ],
    "display_name": "Mall",
    "music": season_music(),
    "random_music": True,
    "outfit": "casual",
    "tags": ["mall_southside"],
    })

define mallmap_location_positions = {
        "mall1": (495, 490),
        "mall2": (615, 425),
        "bakery": (805, 525),
        "bookstore": (575, 670),
        "clothesshop": (955, 460),
        "arcade": (565, 225),
        "tattooshop": (800, 200),
        "flowershop": (700, 580),
        "coffeeshop": (945, 280),
        "electronic": (405, 350),
        "drugstore": (155, 500),
        "jewelrystore": (1125, 370),
    }

screen mallmap(locations):
    if not (renpy.get_screen("smartphone") or renpy.get_screen("story_tracker")):
        default destination = ""
        add "bg mallmap"
        imagebutton auto "gui/map/city_%s.png" action SetVariable("game.room", "map"), Return() xpos 1100 ypos 600 xanchor 0.5 yanchor 0.5 alt "go to city"
        text "{b}" + "City" outlines [ (3, "#06698c") ] color "#5fb2d8" xpos 1100 ypos 680 xanchor 0.5 yanchor 0.5 alt ""
        for location in [l for l in locations if l.id in mallmap_location_positions]:
            $ x, y = mallmap_location_positions[location.id]
            $ girls = location.get_present_girls_ids()
            $ glist = ""
            for index, girl in enumerate(girls[:6]):
                $ glist += f"; {girl}"
            $ self_voicing_location = location.display_name + "; " + glist
            imagebutton auto "gui/map/button_map_%s.png" xpos x ypos y xanchor 0.5 yanchor 0.5 alt self_voicing_location:
                action [SetVariable("game.room", location.id), Return()]
                hovered SetScreenVariable("destination", location)
                unhovered SetScreenVariable("destination", "")
            for index, g in enumerate(girls[:6]):
                $ x_g = x
                $ y_g = y
                if index == 1:
                    $ y_g += 35
                elif index:
                    if index in [2, 4]:
                        $ x_g += 29
                    else:
                        $ x_g = x - 29
                    if index in [2, 3]:
                        $ y_g += 19
                    else:
                        $ y_g = y - 19
                fixed:
                    xpos x_g
                    ypos y_g
                    xsize 25
                    ysize 25
                    xanchor 0.5
                    yanchor 0.5
                    add "gui/icons/icon_bg_small.png"
                    add "notify " + g
            if location.id == "mall1":
                $ location_name = "Mall Southside"
            elif location.id == "mall2":
                $ location_name = "Mall Northside"
            else:
                $ location_name = location.display_name
            text "{b}" + location_name.replace(" ", "\n") xpos x ypos y-22 xanchor 0.5 yanchor 1.0 outlines [ (2, "#06698c") ] color "#5fb2d8" size 15 text_align 0.5 alt ""
        if destination:
            if destination.id == "mall1":
                $ destination_name = "Mall"
            else:
                $ destination_name = destination.display_name
            vbox:
                align (0.5, 0.1)
                spacing 20
                text "{b}" + destination_name outlines [ (3, "#06698c") ] color "#5fb2d8" size 40 xalign 0.5
                hbox:
                    xalign 0.5
                    box_justify True
                    spacing 5
                    for p in destination.get_present_girls_ids():
                        add Composite(
                            (50, 50),
                            (0, 0), Transform("gui/phone/ico_phone_idle.png", zoom=0.8),
                            (7, 7), f"gui/action_icons/button_{p}.png"
                            ):
                            at Position(anchor=(0.5, 0.5))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
