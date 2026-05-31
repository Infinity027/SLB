screen choose_sex():
    style_prefix "setup"
    add gui.game_menu_background

    vbox:
        yalign 0.1
        label "‍♀️♂️" style "setup_title" alt ""
        label "CHOOSE YOUR CHARACTER" style "setup_title" alt ""
        text "Do you want to play as a woman or a man?"

    hbox:
        xfill True
        yalign 1.0
        imagebutton:
            xalign 0.25
            auto "gui/female_button_%s.png"
            action Return("female")
            alt "female"
            tooltip ""
        imagebutton:
            xalign 0.75
            auto "gui/male_button_%s.png"
            action Return("male")
            alt "male"
            tooltip ""
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
