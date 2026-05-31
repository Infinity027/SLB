
define _renpysteam.keyboard_mode = "always"


init python:
    import pygame

    def check_controller():
        if pygame.joystick.get_count() == 0:
            return False
        else:
            return True

    config.always_shown_screens.append("overlay_selector")


screen overlay_selector():
    zorder 999
    if check_controller() and not is_input_screen() and persistent.selector:
        if not renpy.focus_coordinates() == (None, None, None, None):
            $ coor = tuple(int(num) for num in renpy.focus_coordinates())
            $ posit = (coor[0] - 5, coor[1] - 5)
            $ siz = (coor[2] + 10, coor[3] + 10)
            frame pos posit xysize siz style "frame_selector"
        timer 0.2 action Function(renpy.restart_interaction) repeat True

style frame_selector:
    background Frame("gui/selector.png", Borders(23, 23, 23, 23))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
