screen smartphone_choice(girl="UNKNOWN", info="", show_mc=True, accept_only=False):
    predict False
    on "show" action Hide("say")
    if show_mc:
        add hero.layered_image() align (0.3, 1.0)
    style_prefix "smartphone"

    frame:
        align (0.75, 0.7)
        xysize (313, 573)
        background "gui/phone/phone_bg_home.png"
        $ girlname = girl.lower()
        $ self_voicing_name = "call from " + girlname
        frame:
            style "empty"
            if girlname and renpy.has_image(f"{girlname} smartphone"):
                add "[girlname]_smartphone" align (0.5, 0.15)
            else:
                add "gui/phone/unknown_smartphone.png" alpha 0.25 align (0.5, 0.15)
            button:
                style "empty"
                action NullAction()
                keyboard_focus False
                alt self_voicing_name

        vbox:
            yalign 0.85
            text info
            label girl
            hbox:
                spacing 50
                vbox:
                    imagebutton auto "gui/phone/ico_pickup_%s.png" action Return(True) xalign 0.5 alt "Accept"
                    text "Accept" alt ""
                if not accept_only:
                    vbox:
                        imagebutton auto "gui/phone/ico_dontpickup_%s.png" action Return(False) xalign 0.5 alt "Decline"
                        text "Decline" alt ""

screen smartphone_calling(npc="Unknown"):
    predict False
    on "show" action Hide("say")
    style_prefix "smartphone"

    frame:
        align (0.25, 0.3)
        xysize (245, 450)
        background Frame("gui/phone/phone_bg_home.png")
        $ npcname = npc.lower()
        $ self_voicing_name = "calling " + npcname
        vbox:
            ysize 0.70
            vbox:
                xysize (0.65, 0.65)
                ypos 0.15
                if npcname and renpy.has_image(f"{npcname} smartphone"):
                    add Frame(f"{npcname}_smartphone")
                else:
                    add Frame("gui/phone/unknown_smartphone.png") alpha 0.25
            vbox:
                ypos 0.15
                label npc
                add "gui/phone/ico_calling_idle.png" alt "Calling" xalign 0.5
                text "Calling" alt "" xalign 0.5

screen contact_name_line(name, return_hub=False):
    frame:
        xpos -5
        style "invisible_frame"
        xysize (263, 38)


        has button
        xysize (263, 38)
        if return_hub:
            action [SetScreenVariable("selected_char", Person.find(name)), SetScreenVariable("smartphone_screen", "contact_hub")]
        else:
            action [SetScreenVariable("selected_char", Person.find(name))]


        text Person.find(name).name style "smartphone_button_text" xpos 20 yalign 0.5


        $ path_icon = f"gui/action_icons/button_" + Person.find(name).id + ".png"
        if renpy.exists(path_icon):
            add path_icon pos (218, -2) size (35, 35)

screen scrollbar_phone(scrollbar_target):
    vbar:
        align (0.5, 0.5)
        value YScrollValue(scrollbar_target)
        left_bar "gui/inv/vertical_idle_bar.png"
        thumb "gui/inv/vertical_idle_thumb.png"
        right_bar "gui/inv/vertical_idle_bar.png"
        maximum (11, 370)
        thumb_offset 10
        top_gutter 10.5
        bottom_gutter 12.5
        alt "scroll "

screen smartphone(char=None, selected_screen="home"):
    predict False

    key ["K_ESCAPE", "mouseup_3", "pad_b_press"] action Hide("smartphone")
    on "show" action [Hide("story_tracker"), Function(hide_people)]
    on "hide" action Function(show_people)
    default selected_char = char
    default smartphone_screen = selected_screen
    default hide_back = False

    $ hero_contacts = [k for k, v in sorted({i: Person.find(i).name for i in hero.smartphone_contacts if Person.find(i)}.items(), key=lambda x: x[1])]

    if phone_show_hero:
        add hero.layered_image() align (0.3, 1.0)

    if not hide_back and not renpy.variant([ "touch", "android" ]):
        button pos (0, 0) xysize (730, 720) action Hide("smartphone") style "invisible_button" keyboard_focus False
        button pos (1100, 0) xysize (180, 720) action Hide("smartphone") style "invisible_button" keyboard_focus False
    frame:
        style_prefix "smartphone_navigation"
        align (0.75, 0.7)
        xysize (313, 573)
        if smartphone_screen == "home":
            background "gui/phone/phone_bg_home.png"
            vbox:
                xalign 0.5
                ypos 75
                ysize 350
                spacing 10
                hbox:
                    imagebutton auto "gui/phone/ico_char_%s.png" action SetScreenVariable("smartphone_screen", "character") alt "character" tooltip "" default_focus check_controller()
                    imagebutton auto "gui/phone/ico_contacts_%s.png" action SetScreenVariable("smartphone_screen", "contacts") alt "contacts" tooltip ""
                    imagebutton auto "gui/phone/ico_calendar_%s.png" action SetScreenVariable("smartphone_screen", "calendar") alt "calendar" tooltip ""
                hbox:
                    if not bool(game.active_date):
                        imagebutton auto "gui/phone/ico_call_%s.png" action SetScreenVariable("smartphone_screen", "call") alt "call" tooltip ""
                        imagebutton auto "gui/phone/ico_messages_%s.png" action SetScreenVariable("smartphone_screen", "text") alt "text" tooltip ""
                    else:
                        imagebutton auto "gui/phone/ico_call_%s.png" action None
                        imagebutton auto "gui/phone/ico_messages_%s.png" action None
                    imagebutton auto "gui/phone/ico_services_%s.png" action SetScreenVariable("smartphone_screen", "services") alt "services" tooltip ""
                hbox:
                    imagebutton auto "gui/phone/ico_wiki_%s.png" action SetScreenVariable("smartphone_screen", "wiki") alt "wiki" tooltip ""
                    if not game.flags.cheat or config.developer:
                        imagebutton auto "gui/phone/ico_achievements_%s.png" action SetScreenVariable("smartphone_screen", "achievements") alt "achievements" tooltip ""
                        for i in range(1):
                            null:
                                width 80
                                height 80
                    else:
                        for i in range(2):
                            null:
                                width 80
                                height 80
                hbox:
                    for i in range(3):
                        null:
                            width 80
                            height 80
                hbox:
                    for i in range(2):
                        null:
                            width 80
                            height 80
                    if CHEAT:
                        imagebutton auto "gui/phone/ico_cheat_on_%s.png" action SetVariable("CHEAT", False) alt "cheat is on" tooltip ""
                    else:
                        if not game.flags.cheat:
                            imagebutton auto "gui/phone/ico_cheat_off_%s.png" action SetScreenVariable("smartphone_screen", "cheats") alt "open cheat screen" tooltip ""
                        else:

                            imagebutton auto "gui/phone/ico_cheat_off_%s.png" action SetVariable("CHEAT", True) alt "cheat is off" tooltip ""

        elif smartphone_screen == "wiki":
            background "gui/phone/phone_bg_bar.png"
            label "Wiki" pos (26, 30)
            frame:
                style "invisible_frame"
                pos (1, 85)
                maximum (290, 370)
                vbox spacing 5 xoffset 10:
                    text "Hello,"
                    text "If you need help, you can visit the game's wiki page for detailed information and tips."
                    text ""
                    text "You can do so by clicking on the button below."

                vbox:
                    spacing 3
                    pos (0, 400)
                    yanchor "bottom"
                    box_reverse True
                    textbutton "Back" action SetScreenVariable("smartphone_screen", "home") default_focus check_controller()
                    textbutton "Open web wiki" action OpenURL("https://wiki.andrealphusgames.com/wiki/Love_%26_Sex")

        elif smartphone_screen == "achievements":
            background "gui/phone/phone_bg_bar.png"
            label f"Achievements ({round((Achievement.total_unlocked / Achievement.total) * 100)}%)" pos (26, 30)
            frame:
                style "invisible_frame"
                pos (1, 85)
                maximum (290, 370)
                hbox:
                    viewport id "achievements":
                        draggable True
                        mousewheel True
                        xysize (270, 370)
                        has vbox spacing 5
                        for ach_dict in Achievement.all_sorted_achievements:
                            for ach in ach_dict:
                                vbox:
                                    hbox:
                                        frame:
                                            style "empty"
                                            xysize (64, 64)
                                            add ach_dict[ach].image xoffset 5
                                            button:
                                                style "empty"
                                                action NullAction()
                                                keyboard_focus False
                                                alt f'{ach_dict[ach].name} {" unlocked" if ach_dict[ach].has() else " locked"} : {ach_dict[ach].description}'
                                        vbox:
                                            xsize 195
                                            textbutton ach_dict[ach].name:
                                                style "empty"
                                                text_size 18
                                                xpos 9
                                                text_bold True
                                                action NullAction()
                                                keyboard_focus False
                                                alt f'{ach_dict[ach].name} {" unlocked" if ach_dict[ach].has() else " locked"} : {ach_dict[ach].description}'
                                            textbutton ach_dict[ach].description:
                                                style "empty"
                                                text_size 17
                                                xoffset 9
                                                xalign 0.0
                                                text_italic True
                                                action NullAction()
                                                alt f'{ach_dict[ach].name} {" unlocked" if ach_dict[ach].has() else " locked"} : {ach_dict[ach].description}'
                                    null height 2
                                    add "gui/phone/phone_divider.png" xpos 5
                    use scrollbar_phone("achievements")
                textbutton "Back" action SetScreenVariable("smartphone_screen", "home") ypos 375 default_focus check_controller()

        elif smartphone_screen == "cheats":
            background "gui/phone/phone_bg_bar.png"
            label "Cheat" pos (26, 30)
            frame:
                style "invisible_frame"
                pos (1, 85)
                maximum (290, 370)

                text "Enabling cheats will disable the New Game+ and Achievements for this game's save.\n\nIf you want to unlock Achievements again, you need to start a new game and play without cheats." pos (10, 0)
                vbox:
                    spacing 3
                    pos (0, 400)
                    yanchor "bottom"
                    box_reverse True
                    textbutton "Back" action SetScreenVariable("smartphone_screen", "home") default_focus check_controller()
                    textbutton "I understand" action [SetVariable("CHEAT", True), SetVariable("game.flags.cheat", True), SetScreenVariable("smartphone_screen", "home")]

        elif smartphone_screen == "character":
            background "gui/phone/phone_bg_bar.png"
            python:
                hero_birthday_display_name = hero.birthday_display_name
            if hero.is_female:
                add "bree smartphone" pos (100, 85)
            else:
                add "mike smartphone" pos (100, 85)
            $ luck_value = 3 + hero.luck.val
            add f"gui/icons/icon_clover_small_{luck_value}.png" pos (250, 75) size (25, 25)
            if hero.stamina:
                add f"gui/icons/icon_stamina_small_{hero.gender}.png" pos (220, 75)
            else:
                add f"gui/icons/icon_stamina_small_{hero.gender}.png" pos (220, 75) matrixcolor SaturationMatrix(0)
            if hero.flags.pill:
                add "gui/icons/icon_pill_small.png" pos 190, 75
            $ heroname_ui = f"{hero.name.upper()} {hero.family_name.upper()}"
            label text_tag_resize(heroname_ui, 222, style.smartphone_label_text.size) pos (26, 30) maximum (220, 20) text_layout "nobreak"
            text f"{hero.age + hero.flags.age_increase}" size 18 pos (249, 41) alt ""
            text hero.status.capitalize() pos (30, 70) alt ""
            label "Birthday" text_size 21 pos (30, 85) alt ""
            text hero_birthday_display_name pos (30, 114) alt ""
            $ character_self_voicing = f"{heroname_ui} . Status: {hero.status} . Birthday: {hero_birthday_display_name}"
            $ character_self_voicing += f". luck: {luck_value}. stamina: {'ready' if hero.stamina else 'unready'}"
            frame:
                style "invisible_frame"
                pos (1, 130)
                xysize (290, 370)
                has vbox
                yalign 1.0
                spacing 3
                vbox:
                    box_reverse True
                    spacing 3
                    xpos 20
                    xmaximum 270
                    $ attr_bar_ui = None
                    if hero.is_male and Person.is_not_hidden("minami"):
                        $ attr_bar_ui = minami.siscon.for_ui()
                    elif hero.is_female:
                        $ attr_bar_ui = hero.morality.for_ui()
                    if attr_bar_ui is not None:
                        hbox:
                            align (0.0, 1.0)
                            spacing 5
                            add attr_bar_ui['icon']
                            frame:
                                style "invisible_frame"
                                xysize (220, 28)
                                bar:
                                    value attr_bar_ui['vbar']['value']
                                    range attr_bar_ui['vbar']['range']
                                    left_bar "gui/phone/bar_full.png"
                                    right_bar "gui/phone/bar_empty.png"
                                    ymaximum 21
                                bar:
                                    value attr_bar_ui['lbar']['value']
                                    range attr_bar_ui['lbar']['range']
                                    left_bar f"gui/phone/bar_{attr_bar_ui['lbar']['left']}.png"
                                    right_bar f"gui/phone/bar_{attr_bar_ui['lbar']['right']}.png"
                                    ymaximum 21
                                text attr_bar_ui['text'] align (0.5, 0.5) size 16 alt ""
                                if attr_bar_ui['lock']:
                                    add "gui/icons/icon_lock.png" align (0.87, 0.5)
                                $ character_self_voicing += f". {replace_tags_alt(attr_bar_ui['icon'])} {attr_bar_ui['text']} {' is Lock' if attr_bar_ui['lock'] else ''}"

                    if any(hero.skills):
                        $ t = ", ".join([s.display_name for s in hero.skills])
                        text "{b}Skills:{/b} [t]" size 16 alt ""
                        $ character_self_voicing += f". Skills: {t}"

                    if game.flags.ngplus and hero.min_sexperience < hero.sexperience:
                        text "{b}Sexperience:{/b} [hero.sexperience] ([hero.min_sexperience])" alt ""
                        $ character_self_voicing += f". Sexperience: {hero.sexperience} ({hero.min_sexperience})"
                    else:
                        text "{b}Sexperience:{/b} [hero.sexperience]" alt ""
                        $ character_self_voicing += f". Sexperience: {hero.sexperience}"

                    if hero.children:
                        text "{b}Children:{/b} [hero.children]" alt ""
                        $ character_self_voicing += f". Children: {hero.children}"


                    $ job_day = game.flags.job_day
                    if not job_day:
                        if hero.is_male and not game.flags.fired:
                            if game.flags.isceo:
                                $ job_day = "CEO"
                            elif game.flags.promoted:
                                $ job_day = "Manager"
                            else:
                                $ job_day = "Code Monkey"
                        else:
                            $ job_day = "Unemployed"
                    if Room.find(job_day) is not None:
                        $ job_day = Room.find(job_day).display_name
                    $ job_night = game.flags.job_night
                    if hero.is_female:
                        if not job_night:
                            $ job_night = "Unemployed"
                        if Room.find(job_night) is not None:
                            $ job_night = Room.find(job_night).display_name
                        text "{b}Job (night):{/b} [job_night]" alt ""
                    $ character_self_voicing += f". Job (night): {job_night}"
                    text "{b}Job (day):{/b} [job_day]" alt ""
                    $ character_self_voicing += f". Job (day): {job_day}"

                    if hero.is_female:
                        text "{b}Sex:{/b} Female" alt ""
                        if hero.is_visibly_pregnant or [guy for guy in Guy.all() if guy.flags.toldpreg]:
                            text "{b}Fertility:{/b} Pregnant" alt ""
                            $ character_self_voicing += f". Fertility: Pregnant"
                        else:
                            text "{b}Fertility:{/b} [hero.fertility]%" alt ""
                            $ character_self_voicing += f". Fertility: {hero.fertility}%"
                    else:
                        text "{b}Sex:{/b} Male" alt ""

                    button:
                        style "empty"
                        action NullAction()
                        keyboard_focus False
                        alt character_self_voicing
                vbox:
                    yalign 1.0
                    text " "
                    textbutton "Back" action [SetScreenVariable("selected_char", None), SetScreenVariable("smartphone_screen", "home")] default_focus check_controller()

        elif smartphone_screen == "calendar":
            $ hero_agenda = hero.calendar.get_agenda()
            background "gui/phone/phone_bg_bar.png"
            label "Appointments" pos (26, 30)
            frame:
                style "invisible_frame"
                pos (1, 85)
                maximum (290, 370)
                hbox:
                    viewport id "calendar":
                        draggable True
                        mousewheel True
                        xysize (270, 370)
                        has vbox spacing 5
                        for entry in hero_agenda:
                            frame:
                                style "empty"
                                ysize 50
                                vbox:
                                    hbox:
                                        xfill True
                                        text entry.day size 19 xoffset 18 xalign 0.0 italic True alt ""
                                        text entry.hour size 19 xoffset -18 xalign 1.0 italic True alt ""
                                    text text_tag_resize(entry.name, 350, 19) xpos 18 alt ""
                                    null height 2
                                    add "gui/phone/phone_divider.png" xpos 5
                                button:
                                    style "empty"
                                    action NullAction()
                                    keyboard_focus False
                                    alt f'{entry.name}: {find_full_day_name(entry.day)} {entry.hour}'
                    use scrollbar_phone("calendar")
                textbutton "Back" action SetScreenVariable("smartphone_screen", "home") ypos 375 default_focus check_controller()
        elif smartphone_screen == "services":
            python:
                cleaningservices_status = f'{"✔" if game.flags.cleaningservices else "❌"}'
                notexting_status = f'{"✔" if game.flags.noTexting else "❌"}'
                reminders_status = f'{"✔" if game.flags.reminders else "❌"}'
            background "gui/phone/phone_bg_bar.png"
            label "Services" pos (26, 30)
            frame:
                style "invisible_frame"
                pos (1, 85)
                xysize (290, 370)
                vbox spacing 5:
                    hbox:
                        spacing 0
                        frame:
                            style "empty"
                            xysize (240, 40)
                            label text_tag_resize(" Cleaning ($100/week)", 240) align (0.0, 0.5) alt ""
                            button:
                                style "empty"
                                action ToggleVariable("game.flags.cleaningservices", True, False)
                                alt f'Cleaning ($100/week): {"On" if game.flags.cleaningservices else "Off"}'
                        textbutton cleaningservices_status align (1.0, 0.5) style "story_type_button" action ToggleVariable("game.flags.cleaningservices", True, False) alt f'Cleaning ($100/week): {"On" if game.flags.cleaningservices else "Off"}'

                    hbox:
                        spacing 0
                        frame:
                            style "empty"
                            xysize (240, 40)
                            label text_tag_resize(" Block text messages", 240) align (0.0, 0.5) alt ""
                            button:
                                style "empty"
                                action ToggleVariable("game.flags.noTexting", True, False)
                                alt f'Block text messages: {"On" if game.flags.noTexting else "Off"}'
                        textbutton notexting_status align (1.0, 0.5) style "story_type_button" action ToggleVariable("game.flags.noTexting", True, False) alt f'Block text messages: {"On" if game.flags.noTexting else "Off"}'
                    hbox:
                        spacing 0
                        frame:
                            style "empty"
                            xysize (240, 40)
                            label text_tag_resize(" Reminder notifications", 240) align (0.0, 0.5) alt ""
                            button:
                                style "empty"
                                action ToggleVariable("game.flags.reminders", True, False)
                                alt f'Reminder notifications: {"On" if game.flags.reminders else "Off"}'
                        textbutton reminders_status align (1.0, 0.5) style "story_type_button" action ToggleVariable("game.flags.reminders", True, False) alt f'Reminder notifications: {"On" if game.flags.reminders else "Off"}'

                    text ""
                    if game.flags.hirePI:
                        textbutton text_tag_resize("Hire an Investigator", 270) action [ToggleScreen("smartphone"), Call("call_hire_PI")]
                textbutton "Back" action SetScreenVariable("smartphone_screen", "home") ypos 375 default_focus check_controller()
        elif smartphone_screen == "contacts":
            background "gui/phone/phone_bg_bar.png"
            label "Contacts" pos (26, 30)
            frame:
                style "invisible_frame"
                pos (1, 85)
                maximum (290, 370)
                hbox:
                    viewport id "contacts":
                        draggable True
                        mousewheel True
                        maximum (270, 370)
                        has vbox spacing 5
                        for i in hero_contacts:
                            use contact_name_line(i, True)
                        null height 2
                    use scrollbar_phone("contacts")
                textbutton "Back" action SetScreenVariable("smartphone_screen", "home") ypos 375 default_focus check_controller()
        elif not selected_char:
            background "gui/phone/phone_bg_bar.png"
            label "Contacts" pos (26, 30)
            frame:
                style "invisible_frame"
                pos (1, 85)
                maximum (290, 370)
                hbox:
                    viewport id "contacts":
                        draggable True
                        mousewheel True
                        maximum (270, 370)
                        has vbox spacing 5
                        if game.flags.angelaBlow:
                            textbutton "Mom" action [ToggleScreen("smartphone"), Call("angela_afterblow_call")]
                            textbutton "Dad" action [ToggleScreen("smartphone"), Call("angela_afterblow_dad_call")]
                            if game.flags.bruceNumber:
                                textbutton "Bruce (Bree's dad)" action [ToggleScreen("smartphone"), Call("angela_afterblow_bruce_call")]
                        for i in hero_contacts:
                            if smartphone_screen == "call":
                                if i not in Room.find(game.room).get_present_girls() and Person.find(i):
                                    if (not Conditioned.done_today("smartphone_call_" + i)
                                        or not Conditioned.done_today("smartphone_booty_call_" + i)
                                        and Room.has_tag(game.room, 'home')):
                                        use contact_name_line(i)
                            elif smartphone_screen == "text":
                                if (not Conditioned.done_today("smartphone_send_flirty_text_" + i) and hero.charm >= 15
                                    or not Conditioned.done_today("smartphone_send_dirty_text_" + i) and hero.charm >= 30
                                    or not Conditioned.done_today("smartphone_send_friendly_text_" + i)):
                                    use contact_name_line(i)
                            else:
                                use contact_name_line(i)
                        null height 2
                    use scrollbar_phone("contacts")
                textbutton "Back" action SetScreenVariable("smartphone_screen", "home") ypos 375 default_focus check_controller()

        else:
            $ info_self_voicing = f"{selected_char.name} . age: {selected_char.age + selected_char.flags.age_increase}"
            background "gui/phone/phone_bg_bar.png"
            $ charname_ui = f"{selected_char.name.upper()} {selected_char.family_name.upper()}"[0:13]
            label charname_ui pos (26, 30)
            text f"{selected_char.age + selected_char.flags.age_increase}" pos (248, 38) alt ""
            if smartphone_screen != "job_change":
                text selected_char.status.capitalize() pos (30, 70) alt ""
                $ info_self_voicing += f". Status: {selected_char.status}"

            if smartphone_screen == "contact_hub":
                if smartphone_screen not in ["manage", "job_change"]:
                    add f"{selected_char.id} smartphone" pos (100, 85)
                    if selected_char.flags.pill and (selected_char.sub >= 75 or selected_char.love >= 150) and selected_char.sexperience > 1:
                        add "gui/icons/icon_pill_small.png" pos (250, 75)
                        $ info_self_voicing += ". Take contraceptives pill"
                    if selected_char.flags.birthdayknown:
                        hbox:
                            spacing 4
                            pos (30, 85)
                            label "Birthday:" text_size 21 align (0.5, 0.5)
                            text selected_char.birthday_display_name align (0.5, 0.6) alt ""
                        $ info_self_voicing += f". Birthday: {selected_char.birthday_display_name}"
                vbox:
                    yanchor "bottom"
                    ypos 500
                    spacing 4
                    vbox:
                        spacing 3
                        xpos 6
                        box_reverse True
                        frame:
                            style "invisible_frame"
                            maximum (290, 370)
                            vbox:
                                xpos 10
                                yalign 1.0
                                $ traits = ", ".join([t.replace("_", " ").capitalize() for t in sorted(selected_char.traits.known)])
                                if len(traits) > 0:
                                    vbox:
                                        xpos 10
                                        xsize 220
                                        spacing -7
                                        label "Traits" text_size 21
                                        text traits alt ""
                                        $ info_self_voicing += f". Traits: {traits}"
                                null height 10
                                for attr in selected_char.get_attributes():
                                    if attr.visible():
                                        $ n = attr.scaled_val()
                                        $ m = attr.max
                                        $ mr = attr.scale
                                        $ change_love_icon = isinstance(attr, Love) and bool(selected_char.get_attention_needed())
                                        if change_love_icon:
                                            text f"A date or a hot coffee should soften {selected_char.possessive_adjective} up." size 13 italic True alt ""
                                        hbox:
                                            yalign 1.0
                                            spacing 4
                                            frame:
                                                style "invisible_frame"
                                                xysize (30, 30)
                                                if change_love_icon:
                                                    add "gui/icons/icon_love_angry.png" align (0.5, 0.5)
                                                else:
                                                    add attr.get_icon() align (0.5, 0.5)
                                            frame:
                                                style "invisible_frame"
                                                xysize (220, 28)
                                                bar value n range 100 left_bar "gui/phone/bar_full.png" right_bar "gui/phone/bar_empty.png" ymaximum 21
                                                bar value m range mr left_bar "gui/phone/bar_thru.png" right_bar "gui/phone/bar_locked.png" ymaximum 21
                                                text "[n]%" align (0.5, 0.5) size 16 alt ""
                                                $ info_self_voicing += f". {replace_tags_alt(attr.get_icon())}: {n}% {' is Lock' if attr.is_max else ''}"
                                                if attr.is_max and n < 100:
                                                    add "gui/icons/icon_lock.png" align (0.87, 0.5)
                            button:
                                style "empty"
                                action NullAction()
                                keyboard_focus False
                                alt info_self_voicing
                    vbox:
                        spacing 3
                        xpos 6
                        $ hub_buttons = []
                        if selected_char not in Room.find(game.room).get_present_girls() and not selected_char.hidden:
                            if ((not Conditioned.done_today("smartphone_call_" + selected_char.id)
                            or not Conditioned.done_today("smartphone_booty_call_" + selected_char.id)
                            and Room.has_tag(game.room, 'home'))
                            and not bool(game.active_date)):
                                textbutton "Call" action [SetScreenVariable("smartphone_screen", "call")] idle_background "gui/phone/empty_short_idle.png" hover_background "gui/phone/empty_short_hover.png" insensitive_background "gui/phone/empty_short_insensitive.png" xminimum 275
                            if (((not Conditioned.done_today(f"smartphone_send_flirty_text_{selected_char.id}") and hero.charm >= 15
                            or not Conditioned.done_today(f"smartphone_send_dirty_text_{selected_char.id}") and hero.charm >= 30
                            or not Conditioned.done_today(f"smartphone_send_friendly_text_{selected_char.id}")
                            and not bool(game.active_date)))):
                                $ hub_buttons.append("text")
                        for i in hub_buttons:
                            textbutton i.capitalize() action [SetScreenVariable("smartphone_screen", i)]
                        if selected_char.flags.managecareer:
                            textbutton "Manage" action [SetScreenVariable("smartphone_screen", "manage")]
                        textbutton "Back" action [SetScreenVariable("selected_char", None), SetScreenVariable("smartphone_screen", "contacts")] default_focus check_controller()

            elif smartphone_screen == "call":
                add f"{selected_char.id} smartphone" pos (100, 85)
                vbox:
                    spacing 3
                    xpos 6
                    yalign 0.83
                    if selected_char not in Room.find(game.room).get_present_girls() and not selected_char.hidden:
                        if not Conditioned.done_today(f"smartphone_call_{selected_char.id}"):
                            textbutton "Call" action [ToggleScreen("smartphone"), Call("smartphone_call", selected_char)]
                        if (selected_char.id not in ["bree", "sasha", "minami"] or (selected_char.id in ("lexi", "samantha") and Person.find(selected_char.id).flags.schedule != "harem")) and not Conditioned.done_today(f"smartphone_booty_call_{selected_char.id}") and Room.has_tag(game.room, 'home') and game.room != "housemap" and hero.stamina:
                            textbutton "Booty call" action [ToggleScreen("smartphone"), Call("smartphone_booty_call", selected_char)]
                    textbutton "Back" action [SetScreenVariable("smartphone_screen", "contact_hub")] default_focus check_controller()

            elif smartphone_screen == "text":
                add f"{selected_char.id} smartphone" pos (100, 85)
                vbox:
                    spacing 3
                    xpos 6
                    yalign 0.85
                    if selected_char not in Room.find(game.room).get_present_girls() and not selected_char.hidden:
                        if not Conditioned.done_today(f"smartphone_send_flirty_text_{selected_char.id}") and hero.charm >= 15 and not selected_char.flags.noFlirtyText and selected_char.flags.kiss >= 1:
                            textbutton "Send sexy text" action [ToggleScreen("smartphone"), Call("smartphone_send_flirty_text", selected_char)]
                        if not Conditioned.done_today(f"smartphone_send_dirty_text_{selected_char.id}") and hero.charm >= 30 and not selected_char.flags.noDirtyText and selected_char.sexperience >= 1:
                            textbutton "Send dirty text" action [ToggleScreen("smartphone"), Call("smartphone_send_dirty_text", selected_char)]
                        if not Conditioned.done_today(f"smartphone_send_friendly_text_{selected_char.id}") and not selected_char.flags.noFriendlyText:
                            textbutton text_tag_resize("Send friendly text", 270) action [ToggleScreen("smartphone"), Call("smartphone_send_friendly_text", selected_char)]
                    textbutton "Back" action [SetScreenVariable("smartphone_screen", "contact_hub")] default_focus check_controller()

            elif smartphone_screen == "manage":
                text "{b}Job{/b}" pos (26, 100)
                if selected_char.flags.job and selected_char.flags.job in JOBS:
                    text JOBS[selected_char.flags.job].name pos (26, 130)
                else:
                    text "None" pos (26, 130)
                vbox:
                    spacing 3
                    xpos 6
                    yalign 0.85
                    textbutton "Look for jobs" action [Call("smartphone_look_for_jobs", selected_char)]
                    textbutton "Change jobs" action [SetScreenVariable("smartphone_screen", "job_change")]
                    textbutton "Back" action [SetScreenVariable("smartphone_screen", "contact_hub")] default_focus check_controller()

            elif smartphone_screen == "job_change":
                python:
                    jobs = []

                    alljobs = AVAILABLE_JOBS.get(selected_char.id)
                    if not alljobs:
                        alljobs = []
                        AVAILABLE_JOBS[selected_char.id] = []
                    for job in alljobs:
                        jobs.append(job)
                frame:
                    style "invisible_frame"
                    pos (1, 85)
                    maximum (290, 370)
                    hbox:
                        viewport id "job_change":
                            draggable True
                            mousewheel True
                            xmaximum 270
                            has vbox
                            spacing 3
                            xpos 6
                            yalign 0.85
                            for job in jobs:
                                if selected_char.flags.job == job:
                                    textbutton text_tag_resize(JOBS[job].name, 270)
                                else:
                                    textbutton text_tag_resize(JOBS[job].name, 270) action [SetScreenVariable("smartphone_screen", "manage"), Call("smartphone_set_job", selected_char, job)]

                        use scrollbar_phone("job_change")
                    textbutton "Back" action [SetScreenVariable("smartphone_screen", "manage")] ypos 370 default_focus check_controller()


style smartphone_text is text:
    color "#ffffff"
    size 21
    font "exo2_regular"
    xalign 0.5

style smartphone_label_text is label_text:
    color "#ffffff"
    size 25
    font "palanquin_bold"
    xalign 0.5

style smartphone_button is button:
    idle_background "gui/phone/empty_idle.png"
    hover_background "gui/phone/empty_hover.png"
    insensitive_background "gui/phone/empty_insensitive.png"
    xminimum 275

style smartphone_button_text is text:
    color "#ffffff"
    font "palanquin_bold"
    yalign 0.5
    xpos 18

style smartphone_button_text is text:
    variant "small"
    color "#ffffff"
    font "palanquin_bold"
    xpos 18

style smartphone_hbox is hbox:
    xalign 0.5
    spacing 10

style smartphone_vbox is vbox:
    xalign 0.5

style smartphone_navigation_label_text is smartphone_label_text
style smartphone_navigation_button is smartphone_button
style smartphone_navigation_button_text is smartphone_button_text
style smartphone_navigation_text is smartphone_text:
    xalign 0.0

style smartphone_navigation_hbox is smartphone_hbox:
    xalign 0.0
    yalign 0.0

style smartphone_navigation_vbox is smartphone_vbox:
    xalign 0.0

style contact_short_button is button:
    idle_background "gui/phone/empty_short_idle.png"
    hover_background "gui/phone/empty_short_hover.png"

style contact_short_button_text is button_text:
    yalign 0.5

screen message(what, title=""):
    style_prefix "message"
    vbox:
        align (0.5, 0.5)
        box_reverse True
        frame:
            xsize 860
            align (0.5, 0.5)
            text what
        text title:
            ypos 20
            size 30
            outlines [(3, "#006284", 0, 0) ]

style message_frame:
    padding (20, 20, 20, 20)
    background Frame("gui/frame_message.png", Borders(22, 22, 22, 22))

style message_text:
    xalign 0.5
    color "#ffffff"
    textalign 0.5

screen choose_talk(subjects):
    default helper = False
    use npc_info(interact_girl, True)
    frame:
        style "invisible_frame"
        if len(subjects) <= 10:
            add "gui/actions_box.png" xalign 0.5 ypos 585
            $ icons_per_line = 10
        else:
            add "gui/actions_box_big.png" xalign 0.5 ypos 525
            $ icons_per_line = int(ceil(len(subjects) / 2.0))
        ypos -15
        xsize 778
        xalign 0.5
        vbox:
            xfill True
            ypos 647
            yanchor 1.0
            use old_ui_helper(helper)

            if icons_per_line == 10:
                hbox:
                    xalign 0.5
                    spacing 5
                    for subject in subjects:
                        imagebutton:
                            auto f"{subject.icon} %s"
                            hovered SetScreenVariable("helper", (subject.display_name, "talk"))
                            unhovered SetScreenVariable("helper", False)
                            action Return(subject)
                            alt subject.display_name
            else:
                hbox:
                    xsize icons_per_line * 65
                    xalign 0.5
                    spacing 5
                    for subject in subjects[:icons_per_line]:
                        imagebutton:
                            auto f"{subject.icon} %s"
                            hovered SetScreenVariable("helper", (subject.display_name, "talk"))
                            unhovered SetScreenVariable("helper", False)
                            action Return(subject)
                            alt subject.display_name
                hbox:
                    xsize (len(subjects) - icons_per_line) * 65
                    xalign 0.5
                    spacing 5
                    for subject in subjects[icons_per_line:]:
                        imagebutton:
                            auto f"{subject.icon} %s"
                            hovered SetScreenVariable("helper", (subject.display_name, "talk"))
                            unhovered SetScreenVariable("helper", False)
                            action Return(subject)
                            alt subject.display_name
            hbox:
                xalign 0.5
                text "Choose a talk subject" color "#FFFFFF" xalign 0.5

screen interact(interact_girl):
    default helper = False
    use npc_info(interact_girl, True)
    $ activities = [(valid_activity, valid_activity.icon, valid_activity.display_name) for valid_activity in InteractActivity.valid_activities()]
    use actions(activities, helper)
    if persistent.new_ui:
        use tooltip
    else:
        use tooltip_old_ui

screen npc_info(girl, clear=False):
    vbox:
        if persistent.new_ui:
            at npc_info
        else:
            at npc_info_old_ui
        xsize 313
        ypos 150
        spacing 5
        frame:
            $ text_displayed = 0
            $ info_self_voicing = ""
            background "gui/npc_info_bg.png"
            xysize (313, 215)
            add f"gui/id_chibi/{girl.id}.png" ypos 10 xpos 15
            vbox:
                xsize 313
                hbox:
                    ypos 5
                    xalign 1.0
                    xysize (200, 120)
                    yfill True
                    xfill True
                    vbox:
                        if clear:
                            $ text_color = "#FFFFFF"
                        else:
                            $ text_color = gui.text_color
                        spacing 2
                        xfill True
                        text "{b}Name:{/b} [girl.name]" size 15 color text_color font "exo2_regular" alt ""
                        $ info_self_voicing += f"{girl.name}. "
                        $ text_displayed += 1
                        if girl.status:
                            text "{b}Status:{/b} [girl.status!c]" size 15 color text_color font "exo2_regular" alt ""
                            $ info_self_voicing += f"Status: {girl.status}. "
                            $ text_displayed += 1
                        text "{b}Age:{/b} [girl.age + girl.flags.age_increase]" size 15 color text_color font "exo2_regular" alt ""
                        $ info_self_voicing += f"Age: {girl.age + girl.flags.age_increase}. "
                        $ text_displayed += 1
                        if girl.flags.birthdayknown:
                            text f"{{b}}Birthday:{{/b}} {girl.birthday[0].capitalize()}  {girl.birthday[1]}" size 15 color text_color font "exo2_regular" alt ""
                            $ info_self_voicing += f"Birthday: {girl.birthday[0]} {girl.birthday[1]}. "
                            $ text_displayed += 1
                        if girl.is_female:
                            if (girl.sub >= 75 or girl.love >= 150) and girl.sexperience > 1:
                                if girl.flags.pill:
                                    text "{b}Birth control:{/b} Yes" size 15 color text_color font "exo2_regular" alt ""
                                    $ info_self_voicing += "Birth control: Yes. "
                                else:
                                    text "{b}Birth control:{/b} No" size 15 color text_color font "exo2_regular" alt ""
                                    $ info_self_voicing += "Birth control: No. "
                                $ text_displayed += 1
                            if hero.has_skill("fertility_assessment"):
                                if girl.is_visibly_pregnant or girl.flags.toldpreg:
                                    text "{b}Fertility:{/b} Pregnant" size 15 color text_color font "exo2_regular" alt ""
                                    $ info_self_voicing += f"Fertility: Pregnant. "
                                else:
                                    text "{b}Fertility:{/b} [girl.fertility]%" size 15 color text_color font "exo2_regular" alt ""
                                    $ info_self_voicing += f"Fertility: {girl.fertility}%. "
                                $ text_displayed += 1
                        if girl.sexperience >= 1:
                            text "{b}Sex count:{/b} [girl.sexperience]" color text_color size 15 font "exo2_regular" alt ""
                            $ info_self_voicing += f"Sex count: {girl.sexperience}. "
                            $ text_displayed += 1

                        if girl.flags.mikeBabies or girl.flags.otherBabies:
                            $ babies = girl.flags.mikeBabies + girl.flags.otherBabies
                            text "{b}Babies:{/b} [babies]" color text_color size 15 font "exo2_regular" alt ""
                            $ info_self_voicing += f"Babies: {babies}. "
                            $ text_displayed += 1
                        $ job = girl.flags.job
                        if job:
                            text "{b}Job:{/b} " + JOBS[job].name size 15 color text_color font "exo2_regular" alt ""
                            $ info_self_voicing += f"Job: {JOBS[job].name}. "
                            $ text_displayed += 1
                if girl.traits.known:
                    vbox:
                        if text_displayed >= 7:
                            ypos 11 + 20 * (text_displayed - 7)
                        xpos 10
                        xsize 303
                        xfill True
                        python:
                            traits = ""
                            line_limit = 39
                            entries = remains = 0
                            for trait in girl.traits.known:
                                trait = trait.replace("_", " ").capitalize() + ", "
                                if (len(traits) - entries) + len(trait) > (line_limit * (entries + 1)) - remains: 
                                    traits += "\n" 
                                    entries += 1 
                                    remains += (line_limit * entries) - (len(traits) - entries)
                                traits += trait
                            traits = traits[:-2] 
                        text "{b}Traits{/b}" size 15 color text_color font "exo2_regular" alt ""
                        text traits size 15 color text_color font "exo2_regular" alt ""
                        $ info_self_voicing += f"Traits: {traits}, "
            button:
                style "empty"
                action NullAction()
                keyboard_focus False
                alt info_self_voicing

        for attr in girl.get_attributes():
            if attr.visible():
                $ attr_bar_ui = attr.for_ui()
                fixed:
                    xysize (313, 31)
                    bar:
                        value attr_bar_ui['vbar']['value']
                        range attr_bar_ui['vbar']['range']
                        left_bar "gui/bar_full_big.png"
                        right_bar "gui/bar_empty_big.png"
                    bar:
                        value attr_bar_ui['lbar']['value']
                        range attr_bar_ui['lbar']['range']
                        left_bar f"gui/bar_{attr_bar_ui['lbar']['left']}_big.png"
                        right_bar f"gui/bar_{attr_bar_ui['lbar']['right']}_big.png"
                    add attr_bar_ui['icon'] align (0.25, 0.5)
                    text attr_bar_ui['text'] align (0.5, 0.5) size 23 color "#ffffff" font "exo2_regular" alt ""
                    if attr_bar_ui['lock']:
                        add "gui/icons/icon_lock.png" align (0.87, 0.5)
                    button:
                        style "empty"
                        action NullAction()
                        keyboard_focus False
                        alt replace_tags_alt(f"{attr_bar_ui['icon']} {attr_bar_ui['text']} {' is Lock' if attr_bar_ui['lock'] else ''}")

        if game.active_date.on_date(girl.id):
            hbox spacing 5 yalign 0.0:
                $ score = game.active_date.score
                if score > 100:
                    $ score = 100
                if score < -100:
                    $ score = -100
                fixed:
                    xysize (313, 31)
                    bar value score range 100 left_bar "gui/bar_full_big.png" right_bar "gui/bar_empty_big.png"
                    hbox spacing 10 xalign 0.5:
                        add "gui/icons/icon_dating.png" yalign 1.0
                        text str(score) + "%" yalign 0.5 size 23 color "#ffffff" font "exo2_regular" alt ""

layeredimage button location next:
    always:
        "gui/location_button_next.png"
    group fg:
        attribute hover:
            "gui/location_button_fg_hover.png"
        attribute idle:
            "gui/location_button_fg_idle.png"
        attribute insensitive:
            "gui/location_button_fg_insensitive.png"

screen actions(activities, helper=False):

    if persistent.new_ui:
        if not renpy.get_screen(["smartphone", "story_tracker", "smartphone_choice"]):
            frame:
                at show_actions
                style "invisible_frame"
                yalign 0.6
                has hbox
                spacing 5
                if len(activities) > 8:
                    $ div = ceil(len(activities)/8)
                else:
                    $ div = 1
                for i in range(div):
                    vbox:
                        spacing 5
                        align (0.5, 0.5)
                        for (action_object, action_icon, action_display_name) in activities[i*ceil(len(activities)/div):(i+1)*ceil(len(activities)/div)]:
                            imagebutton:
                                auto f"button_{action_icon} %s"
                                action [Return(action_object)]
                                tooltip action_object
                                alt action_display_name

    else:
        frame:
            style "invisible_frame"
            if len(activities) > 10:
                add "gui/actions_box_big.png" xalign 0.5 ypos 520
                $ div = int(ceil(len(activities) / 10))
            else:
                add "gui/actions_box.png" xalign 0.5 ypos 570
                $ div = 1
            xsize 0.65
            xalign 0.5
            vbox:
                xalign 0.5
                ypos 605
                yanchor 1.0
                use old_ui_helper(helper)

                for i in range(div):
                    hbox:
                        xalign 0.5
                        spacing 5
                        for (action_object, action_icon, action_display_name) in activities[i*ceil(len(activities)/div):(i+1)*ceil(len(activities)/div)]:
                            imagebutton:
                                auto f"button_{action_icon} %s"
                                hovered SetScreenVariable("helper", (action_display_name, "activity"))
                                unhovered SetScreenVariable("helper", False)
                                action [SetScreenVariable("helper", False), Return(action_object)]
                                tooltip action_object
                                alt action_display_name


screen room(room, shown_girls, more_people_present=False, exits=[]):
    default helper = False
    if not renpy.get_screen(["smartphone", "story_tracker", "smartphone_choice"]):
        default room_start = 0

        on "show" action [Hide("quick_menu"), Hide("say"), Show("overlay_ui")]
        $ activities = []
        if more_people_present:
            $ activities.append(("+", "next", "Look around"))
        $ activities.extend((npc, npc.id, "Interact with {}".format(npc.name)) for npc in shown_girls if not npc.activity_name == "sleep" or game.active_date.on_date(npc))
        $ activities.extend((valid_activity, valid_activity.icon, valid_activity.display_name) for valid_activity in Activity.valid_activities())
        use actions(activities, helper)
        frame:
            at show_locations
            style "invisible_frame"
            xsize 778
            xalign 0.5
            has frame
            style "invisible_frame"
            xalign 0.5
            ypos 700
            yanchor 1.0
            if room_start >= len(exits):
                $ room_start = 0
            $ exits = sorted(exits, key=lambda x: x.display_name)

            for room_id in ["livingroom", "mall1", "mall2", "housemap", "map", "mallmap"]:
                if Room.find(room_id) in exits:
                    $ exits.remove(Room.find(room_id))
                    if room_id != "map" or (room_id == "map" and not game.active_date):
                        $ exits = [Room.find(room_id)] + exits
            if len(exits) > 8 and not (room == Room.find("map") or room == Room.find("mallmap")):
                $ show_rooms = exits[room_start:room_start + 7]
            else:
                $ show_rooms = exits
            hbox:
                spacing 5
                for idx, r in enumerate(show_rooms):
                    $ girls = r.get_present_girls()
                    fixed:
                        xysize (100, 60)
                        imagebutton:
                            auto "button bg " + r.id.replace("date_", "") + " %s"
                            hovered SetScreenVariable("helper", (r.display_name, "room"))
                            unhovered SetScreenVariable("helper", False)
                            if r.id != game.room:
                                clicked [SetVariable("game.room", r.id), Return()]
                                alt r.display_name
                            tooltip r
                        vbox:
                            xalign 0.5
                            ypos -10
                            hbox:
                                xalign 0.5
                                for g in girls[:3]:
                                    fixed:
                                        xysize (25, 25)
                                        add "gui/icons/icon_bg_small.png"
                                        add "notify " + g.id
                            if len(girls) > 3:
                                hbox:
                                    xalign 0.5
                                    for g in girls[3:6]:
                                        fixed:
                                            xysize (25, 25)
                                            add "gui/icons/icon_bg_small.png"
                                            add "notify " + g.id
                if len(exits) > 8:
                    fixed:
                        xysize (100, 60)
                        imagebutton:
                            auto "button location next %s"
                            hovered SetScreenVariable("helper", ("Next locations", "room"))
                            unhovered SetScreenVariable("helper", False)
                            clicked [SetScreenVariable("room_start", room_start + 7)]
                            tooltip ""
                            alt "Next locations"
        if persistent.new_ui:
            use tooltip
        else:
            use tooltip_old_ui

screen old_ui_helper(helper):

    if helper:
        $ helper_name, helper_type = helper
        if helper_type == "activity" and game.room == "map":
            vbox:
                align (0.5, 0.17)
                text helper_name size 23 font "exo2_regular" color "#fff" outlines [(1, "#0099ff", 0, 0)] xalign 0.5
        else:
            hbox:
                xalign 0.5
                if helper_type in ["talk", "activity"]:
                    text helper_name size 23 font "exo2_regular" color "#FFFFFF" outlines [(1, "#0099ff", 0, 0)] xalign 0.5 alt ""
                elif helper_type == "room":
                    text f"Go to {helper_name}" size 23 font "exo2_regular" color "#FFFFFF" outlines [(1, "#0099ff", 0, 0)] xalign 0.5


screen tooltip_old_ui():

    $ tooltip = GetTooltip()
    if tooltip:
        if isinstance(tooltip, BaseActivity):
            $ tooltip = tooltip.get_tooltip()
            if tooltip:
                if game.room == "map":
                    hbox:
                        xalign 0.5
                        ypos 25
                        text " ".join(tooltip) color "#FFFFFF" alt ""
                else:
                    hbox:
                        align (0.5, 0.88)
                        text " ".join(tooltip) color "#FFFFFF" alt ""
        elif isinstance(tooltip, ItemBase):
            $ tooltip = tooltip.get_tooltip()
            if tooltip:
                nearrect:
                    focus "tooltip"
                    style_prefix "tooltips"
                    has frame
                    yanchor 0
                    xalign 0.5
                    xpadding 20
                    text tooltip substitute False yalign 0.05
        elif isinstance(tooltip, (tuple, list)):
            hbox:
                xalign 0.5
                ypos 615
                text " ".join(tooltip) substitute False color "#FFFFFF"

screen tooltip():
    $ tooltip = GetTooltip()
    if tooltip:
        nearrect:
            at FadeInTransform
            focus "tooltip"
            style_prefix "tooltips"
            if isinstance(tooltip, Room):
                preferred_side "top"
                frame:
                    xpos 50
                    xanchor 0.5
                    style "invisible_frame"
                    text f"Go to {tooltip.display_name}" size 23 font "exo2_regular" color "#fff" outlines [(1, "#0099ff", 0, 0)] xalign 0.5
            elif isinstance(tooltip, (tuple, list)):
                preferred_side "right"
                xpos 30
                frame:
                    ypos 30
                    yanchor 0.5
                    style "overlay_ui_frame"
                    has vbox
                    align (0.5, 0.5)
                    spacing 5
                    text " ".join(tooltip) substitute False yalign 0.5
            elif isinstance(tooltip, str):
                preferred_side "right"
                xpos 30
                frame:
                    ypos 30
                    yanchor 0.5
                    style "overlay_ui_frame"
                    has vbox
                    align (0.5, 0.5)
                    spacing 5
                    text tooltip substitute False yalign 0.5
            else:
                preferred_side "right"
                if isinstance(tooltip, ItemBase):
                    xpos 30
                else:
                    xpos 10
                frame:
                    ypos 30
                    yanchor 0.5
                    style "overlay_ui_frame"
                    has vbox
                    align (0.5, 0.5)
                    spacing 5
                    $ name = tooltip.display_name if not isinstance(tooltip, Person) else f"Talk to {tooltip.name}"
                    text name size 23 font "exo2_regular" color "#fff" outlines [(1, "#0099ff", 0, 0)] xalign 0.5
                    if not isinstance(tooltip, Person) and tooltip.get_tooltip():
                        text tooltip.get_tooltip() substitute False yalign 0.5

screen overlay_notification():
    zorder 2
    if persistent.notifications == True and game.room not in ["map", "housemap", "mallmap"]:
        timer 1 action [display_notifications, Function(renpy.restart_interaction) if NOTIFICATIONS else None] repeat True

screen notification_wave(notifs):
    $ posindex = 0
    for n in notifs:
        if posindex != 0:
            timer (0.2 * posindex) action [Show("notification_popup", _tag=f"{n[0]}_{posindex}", notif=n, pos=posindex), remove_notification(n[0])]
        else:
            timer 0.1 action [Show("notification_popup", _tag=f"{n[0]}_{posindex}", notif=n, pos=posindex), remove_notification(n[0])]
        $ posindex += 1
    timer (4.2 + (0.2 * posindex)) action [display_notifications, Hide()]

screen notification_popup(notif, pos):
    frame at notification_popout():
        xalign 1.0
        ypos 120 + (pos * 55)
        background "gui/notification_box.png"
        xminimum 100
        ysize 50
        xpadding 10
        text notif[0] yalign 0.5 style "ui_text" alt ""
    timer 4.0 action [Hide()]

screen overlay_ui():
    default helper = False
    if helper:
        $ helper_name, helper_type = helper
    zorder 1
    use button_screen

    default self_voicing_date = f"{game.calendar.hour_of_day}:00\n{game.calendar.day_of_week_name} {game.calendar.day_of_season} {game.calendar.season_name}"
    if not HIDE_UI:


        if persistent.notifications == True and NOTIFICATIONS and game.room not in ["map", "housemap", "mallmap"]:
            $ display_notifications()

        hbox xalign 0.5 ypos 10 spacing 10:

            frame:
                xysize (80, 80)
                style "invisible_frame"
                has imagebutton auto "gui/phone/ico_smart_%s.png"
                align (0.5, 0.5)
                if renpy.get_screen(["room", "smartphone", "map", "housemap", "mallmap"]):
                    action ToggleScreen("smartphone")
                else:
                    sensitive False
                alt "smartphone"

            hbox spacing 10:
                python:
                    is_sick = game.flags.sick
                    is_injured = game.flags.injured
                vbox:
                    xsize 218

                    spacing 5
                    box_justify True
                    vbox:
                        spacing 0
                        frame:
                            xfill True
                            ysize 47
                            padding (14, 9)
                            if game.calendar.is_day:
                                background "gui/datebox_day.png"
                            else:
                                background "gui/datebox_night.png"



                            python:
                                hour = f"{game.calendar.hour_of_day}:00"
                                day = game.calendar.day_of_week_short_name.capitalize()
                                date = str(game.calendar.day_of_season)
                                icon = f"gui/icons/icon_{game.calendar.season_name}.png"
                            hbox:
                                align (1.0, 0.5)
                                spacing 5
                                style_prefix "ui"
                                text hour alt ""
                                text day alt ""
                                text date alt ""
                                add icon
                            button:
                                style "empty"
                                action NullAction()
                                keyboard_focus False
                                alt self_voicing_date

                        if game.flags.alarm_clock and game.room == "bedroom1":
                            frame:
                                xfill True
                                ysize 40
                                yoffset -5
                                padding (19, 10)
                                background "gui/alarm_box.png"
                                hbox spacing 10 align (0.5, 0.5):
                                    add "gui/icons/icon_hour.png" yalign 0.5
                                    text "[game.flags.alarm_time]:00" alt "" size 22 color "#006284"
                                button:
                                    style "empty"
                                    action NullAction()
                                    keyboard_focus False
                                    alt "Sickness for [game.timers.sick] day"
                    if not renpy.get_screen(["smartphone", "story_tracker", "smartphone_choice", "inventory", "shopping"]):
                        if is_sick:
                            textbutton "[game.timers.sick] ['day' if game.timers.sick == 1 else 'days']":
                                text_style "ui_text"
                                text_xalign 0.5
                                xfill True
                                padding (0, 0)
                                background "gui/physicalstates_icons/physicalstate_sickness.png"
                                sensitive None
                                action NullAction()
                                keyboard_focus False
                                alt "Sickness for [game.timers.sick] day"
                        if is_injured:
                            textbutton "[game.timers.injured] ['day' if game.timers.injured == 1 else 'days']":
                                text_style "ui_text"
                                text_xalign 0.5
                                xfill True
                                padding (0, 0)
                                background "gui/physicalstates_icons/physicalstate_bleed.png"
                                sensitive None
                                action NullAction()
                                keyboard_focus False
                                alt "Injured for [game.timers.injured] day"



                if game.room != "map" or persistent.new_ui:

                    frame xysize (297, 47) style "overlay_ui_frame":
                        has hbox align (0.5, 0.5) spacing 5
                        for need in sorted(hero.get_needs(), key=lambda x: x.name):
                            frame xysize (64, 40):
                                style "empty"
                                yalign 0.5
                                hbox spacing 3:
                                    yalign 0.5
                                    fixed xysize (32, 32):
                                        add need.icon align (0.5, 0.5)
                                    if need < 1:
                                        label str(need) alt "" xsize 30 text_style "ui_text_error"
                                    elif need < 3:
                                        label str(need) alt "" xsize 30 text_style "ui_text_warning"
                                    else:
                                        label str(need) alt "" xsize 30 text_style "ui_text"
                                button:
                                    style "empty"
                                    action NullAction()
                                    keyboard_focus False
                                    alt need.name + str(need)


                    frame xysize (297, 47) style "overlay_ui_frame":
                        has hbox align (0.5, 0.5) spacing 9
                        for attr in sorted(hero.get_attributes(), key=lambda x: x.name):
                            if attr.name != "Morality":
                                frame xysize (77, 40):
                                    style "empty"
                                    yalign 0.5
                                    hbox spacing 7:
                                        yalign 0.5
                                        fixed xysize (32, 32):
                                            add attr.get_icon() align (0.5, 0.5)
                                        label str(attr) alt "" xsize 45 text_style "ui_text"
                                    button:
                                        style "empty"
                                        action NullAction()
                                        keyboard_focus False
                                        alt attr.name + str(attr)

                    fixed xysize (150, 90):

                        frame xysize (150, 47) style "overlay_ui_frame":
                            add hero.money.icon yalign 0.5
                            $ money = str(hero.money)
                            label money alt "" align (1.0, 0.5) text_style "ui_text"
                            button:
                                style "empty"
                                action NullAction()
                                keyboard_focus False
                                alt "money" + money


                        if (
                        game.active_date or
                        (game.room in ["studio"] and game.flags.bandpractice) or
                        (Room.has_tag(game.room, 'home') and game.flags.chores < 100 and not game.flags.cleaningservices) or
                        (Room.has_tag(game.room, 'work') and (game.flags.worksatisfaction or game.flags.underinvestigation)) or
                        (game.room == 'bedroom1' and game.flags.alarm_clock)
                        ) and IN_EVENT_WITH != "tuto":
                            fixed xysize (218, 31) align (1.0, 1.0):
                                default self_voicing_progressbar = ""
                                if game.active_date:
                                    $ self_voicing_progressbar = "date: " + str(game.active_date.score) + "%"
                                    use percentile(game.active_date.score, "gui/icons/icon_dating.png", lower_bound=-100)
                                elif game.room in ["studio"] and game.flags.bandpractice:
                                    $ self_voicing_progressbar = "guitar: " + str(game.flags.bandpractice) + "%"
                                    use percentile(game.flags.bandpractice, "gui/icons/icon_guitar.png")
                                elif Room.has_tag(game.room, 'home') and game.flags.chores < 100 and not game.flags.cleaningservices:
                                    $ self_voicing_progressbar = "chores: " + str(game.flags.chores) + "%"
                                    use percentile(game.flags.chores, "gui/icons/icon_chores.png")
                                elif Room.has_tag(game.room, 'work') and game.flags.underinvestigation:
                                    $ self_voicing_progressbar = "investigation" + str(game.flags.workinvestigation) + "%"
                                    use percentile(game.flags.workinvestigation, "gui/icons/icon_investigation.png")
                                elif Room.has_tag(game.room, 'hospital') and game.flags.angelainvestigation and not game.flags.angela_test_results:
                                    $ self_voicing_progressbar = "investigation" + str(game.flags.angelainvestigation) + "%"
                                    use percentile(game.flags.angelainvestigation, "gui/icons/icon_investigation.png")
                                elif Room.has_tag(game.room, 'work') and game.flags.worksatisfaction and not game.flags.capped_promotion:
                                    $ val = game.flags.worksatisfaction * 2 if not game.flags.promoted else game.flags.worksatisfaction
                                    $ self_voicing_progressbar = "career: " + str(val) + "%"
                                    use percentile(val, "gui/icons/icon_career.png")
                                elif Room.has_tag(game.room, 'work') and game.flags.capped_promotion:
                                    bar value StaticValue(100/100.) style "overlay_ui_bar"
                                    hbox spacing 10 xalign 0.5:
                                        add "gui/icons/icon_career.png" yalign 0.5
                                        text "Max" alt "" yalign 0.5 style "ui_text"
                                    $ self_voicing_progressbar = "career: " + "Max"
                                button:
                                    style "empty"
                                    action NullAction()
                                    keyboard_focus False
                                    alt self_voicing_progressbar
                else:

                    frame:
                        style "invisible_frame"
                        xysize (536, 47)
                        if not IN_EVENT_WITH:
                            $ valid_activities = [(valid_activity, valid_activity.icon, valid_activity.display_name) for valid_activity in Activity.valid_activities()]
                            frame:
                                background Frame("gui/actions_box.png", Borders(10, 10, 10, 10)) xalign 0.5
                                xysize (450, 70)
                            hbox:
                                xalign 0.5
                                ypos 40
                                vbox:
                                    hbox spacing 5:
                                        for (action_object, action_icon, action_display_name) in valid_activities:
                                            imagebutton:
                                                auto f"button_{action_icon} %s"
                                                hovered SetScreenVariable("helper", (action_display_name, "activity"))
                                                unhovered SetScreenVariable("helper", False)
                                                action [SetScreenVariable("helper", False), Return(action_object)]
                                                tooltip action_object
                                                alt action_display_name
                    frame:
                        style "invisible_frame"
                        xysize (218, 47)


                frame:
                    xysize (80, 80)
                    style "invisible_frame"
                    imagebutton auto "gui/phone/ico_story_%s.png":
                        align (0.5, 0.5)
                        if renpy.get_screen(["room", "story_tracker", "map", "housemap"]):
                            action ToggleScreen("story_tracker")
                        else:
                            sensitive False
                        alt "story tracker"

                    if IN_EVENT_WITH:
                        text "❗" align (0.5, 0.5) size 30 color "#96AEBE" outlines [(2, "#fff", 0, 0) ] alt ""
                        $ path_icon = "gui/action_icons/button_" + IN_EVENT_WITH + ".png"
                        if renpy.exists(path_icon):
                            add "gui/phone/ico_phone_insensitive.png" align (0.5, 0.5)
                            add path_icon align (0.5, 0.5)

        if not persistent.new_ui:
            use tooltip_old_ui


screen percentile(val, icon, lower_bound=0, upper_bound=100):
    $ val = int(max(lower_bound, min(upper_bound, val)))
    bar value StaticValue(val/100.) style "overlay_ui_bar"
    hbox spacing 10 xalign 0.5:
        add icon yalign 0.5
        text "[val]%" alt "" yalign 0.5 style "ui_text":
            if val < 0:
                color "#ff0000"

style ui_text:
    size 23
    font "exo2_regular"
    color "#ffffff"

style ui_text_warning is ui_text:
    outlines [(1, "#ff8000")]

style ui_text_error is ui_text_warning

style overlay_ui_frame:
    background Frame("gui/overlay_ui_frame.png", gui.overlay_ui_frame_borders, tile=gui.frame_tile)
    padding gui.overlay_ui_frame_borders.padding

style overlay_ui_bar:
    ysize 31
    left_bar Transform("gui/bar_full.png", size=(218, 31))
    right_bar Transform("gui/bar_empty.png", size=(218, 31))

screen select(choices, title="", cancel="None", cap=True):
    on "show" action [Hide("quick_menu"), Hide("say")]
    if not persistent.new_ui and GetTooltip():
        add "gui/actions_box.png" xalign 0.5 ypos 585
    frame:
        style "invisible_frame"
        align (0.5, 0.5)
        xsize 766
        has vbox
        spacing 5
        xfill True
        if title:
            text title.capitalize() size 23 font "exo2_regular" color "#FFFFFF" outlines [(1, "#0099ff", 0, 0)] xalign 0.5
        $ choices.sort()
        for sub in choices:
            hbox:
                xsize 766
                xfill True
                if isinstance(sub, tuple):
                    if cap:
                        $ t = sub[0].capitalize()
                    else:
                        $ t = sub[0]
                    fixed:
                        xysize (766, 39)
                        imagebutton:
                            auto "gui/choicebox_%s.png"
                            clicked Return(sub[1])
                            if hasattr(sub[1],"get_tooltip") and not inspect.isclass(sub[1]):
                                tooltip sub[1].get_tooltip()
                            alt t
                        text t font "exo2_regular" color "#ffffff" align (0.5, 0.5) alt ""
                else:
                    if cap:
                        $ t = sub.capitalize()
                    else:
                        $ t = sub
                    fixed:
                        xysize (766, 39)
                        imagebutton:
                            auto "gui/choicebox_%s.png"
                            clicked Return(sub)
                            alt t
                        text t font "exo2_regular" color "#ffffff" align (0.5, 0.5) alt ""
        if cancel is not None:
            fixed:
                xysize (766, 39)
                imagebutton:
                    auto "gui/choicebox_%s.png"
                    clicked Return(cancel)
                text "Cancel" font "exo2_regular" color "#ffffff" align (0.5, 0.5)

    if persistent.new_ui:
        use tooltip
    else:
        use tooltip_old_ui

style buttonz:
    idle_color "ffffff"
    size 21

screen shopping(items=[], clerk=None):
    style_prefix "shopping"
    modal True
    key ["K_ESCAPE", "mouseup_3", "pad_b_press"] action Return("exit")
    button pos (0, 0) xysize (1280, 720) action Return("exit")
    on "show" action [Hide("quick_menu"), Hide("say")]
    if clerk:
        if persistent.new_ui:
            add clerk align (0.7, 1.0)
        else:
            add clerk align (0.25, 1.0)
    vbox:
        if persistent.new_ui:
            xalign 0.2
        else:
            xalign 0.75
        ypos 100
        spacing 10
        xsize 315
        frame:
            ysize 435
            background "gui/inv/inventory_box.png"
            label Room.find(game.room).display_name alt ""
            viewport id "inventory_vp":
                style_prefix "shopping_items"
                xfill True
                pos (10, 55)
                ysize 352
                draggable True
                mousewheel True
                has vbox
                for i, (item_name, item_id, item_price, item_tooltip) in enumerate(sorted(items, key=lambda x: x[0])):
                    hbox:
                        xsize 0.93
                        button sensitive item_price <= hero.money action Return((item_id, item_price)) default_focus (1 if i == 0 and check_controller() else 0):
                            xfill True
                            text text_tag_resize(item_name, 270) alt ""
                            hbox:
                                xalign 1.0
                                text "[item_price] " alt ""
                                add hero.money.icon yalign 0.5
                            tooltip ItemBase.find(item_id)
                            alt f"{item_name}. money cost: {item_price}. " + replace_tags_alt(" ".join(item_tooltip))
            vbar value YScrollValue("inventory_vp") left_bar "gui/inv/vertical_idle_bar.png" thumb "gui/inv/vertical_idle_thumb.png" right_bar "gui/inv/vertical_idle_bar.png" xmaximum 11 ymaximum 370 xalign 1.0 ypos 50 unscrollable "hide" alt "scroll "
        fixed:
            ysize 29
            imagebutton auto "gui/button_%s.png" action Return("exit") alt "Exit"
            text "Exit" color "#ffffff" font "palanquin_bold" xalign 0.5 alt ""

    if persistent.new_ui:
        use tooltip
    else:
        use tooltip_old_ui

style shopping_button is inventory_button

style shopping_text is inventory_text

style shopping_label is inventory_label

style shopping_label_text is inventory_label_text

style shopping_items_text is inventory_items_text:
    insensitive_color "#555"

style shopping_items_button is inventory_items_button

style shopping_items_button_text is inventory_items_button_text

style shopping_items_image_button is inventory_items_image_button


default inventory_filter = None
default discard_mode = False
screen inventory():
    style_prefix "inventory"
    modal True
    predict False
    on "show" action [Hide("quick_menu"), Hide("say"), Function(hide_people)]
    if persistent.new_ui:
        add hero.layered_image() align (0.7, 1.0)
    else:
        add hero.layered_image() align (0.25, 1.0)
    vbox:
        if persistent.new_ui:
            xalign 0.2
        else:
            xalign 0.75
        ypos 100
        spacing 10
        xsize 315
        frame:
            ysize 88
            background "gui/inv/equipment_box.png"
            vbox spacing -15:
                label "Clothes:" text_size 25 alt ""
                label "Accessory:" text_size 25 alt ""
            vbox spacing 6:
                pos (145, 10)
                $ clothes, accessory = hero.equipment_for_ui
                text "[clothes]" alt ""
                text "[accessory]" alt ""
        frame:
            ysize 435
            background "gui/inv/inventory_box.png"
            label "Inventory" alt ""
            hbox:
                ypos 52
                textbutton "🗑️":
                    text_size 18
                    xpos 8
                    action ToggleVariable("discard_mode")
                    style ("filter_title_select" if discard_mode else "filter_title")
                hbox:
                    spacing 1
                    xpos 54
                    text "Filter: " yalign 0.5 alt ""

                    $ filters = {
                        "gift": ("🎁", "gift", Gift),
                        "equip": ("👔", "equip", Equip),
                        "cons": ("🫙", "consumable", Consumable),
                        "othe": ("📦", "other", Item)
                    }
                    for filter_name, (icon, alt_text, _) in filters.items():
                        textbutton icon:
                            if store.inventory_filter == filter_name:
                                style "filter_title_select"
                                action SetVariable("inventory_filter", None)
                                alt "filter {} selected".format(alt_text)
                            else:
                                style "filter_title"
                                action SetVariable("inventory_filter", filter_name)
                                alt "filter {}".format(alt_text)
            if hero.inventory:
                viewport id "inventory_vp":
                    style_prefix "inventory_items"
                    xfill True
                    pos (10, 90)
                    ysize 324
                    draggable True
                    mousewheel True
                    $ cls = filters.get(store.inventory_filter, (None, None, ItemBase))[2]
                    $ items = cls.filtered_sort(filter=lambda x: x.name in hero.inventory, key=lambda x: x.display_name)
                    vbox:
                        for item in items:
                            if discard_mode and item.one_only:
                                continue
                            $ t = item.display_name
                            $ n = hero.has_item(item.name)
                            if n > 1:
                                $ t += " ({})".format(n)
                            $ is_valid_equip = (isinstance(item, Equip) and game.room in ["bedroom1", "bedroom4"])
                            $ is_valid_consum = (isinstance(item, Consumable) and not game.flags[item.name] and item.test())
                            $ is_sensitive = is_valid_equip or is_valid_consum
                            hbox:
                                if discard_mode:
                                    button:
                                        yalign 0.5
                                        text "❌" align (0.0, 0.5) style "inventory_items_text_icon" alt "" size 12
                                        action Function(hero.lose_item, item)
                                frame:
                                    xysize (0.93, 26)
                                    style "invisible_frame"
                                    button:
                                        if discard_mode:
                                            action NullAction()
                                            sensitive False
                                        else:
                                            action Return(item)
                                            sensitive is_sensitive
                                        xfill True
                                        yfill True
                                        yalign 0.5
                                        hbox:
                                            xfill True
                                            yalign 0.5
                                            text text_tag_resize(t, (275 if discard_mode else 295), style.inventory_items_text.size):
                                                align (0.0, 0.5)
                                                alt t + ". " + replace_tags_alt(" ".join(item.get_tooltip(True)))
                                            text item.icon align (1.0, 0.5) style "inventory_items_text_icon" alt ""
                                        tooltip item
                                    if not is_sensitive:
                                        $ insensitive_tooltip = ""
                                        if not is_valid_equip and isinstance(item, Equip):
                                            $ insensitive_tooltip += "{color=#ddddddcc}Can only be equipped in bedroom{/color}"
                                        elif not is_valid_consum and isinstance(item, Consumable):
                                            $ insensitive_tooltip += "{color=#ddddddcc}Need to wait a "
                                            if (item.frequency_limit):
                                                $ insensitive_tooltip += item.frequency_limit
                                            else:
                                                $ insensitive_tooltip += "bit"
                                            $ insensitive_tooltip += " between use{/color}"
                                        elif isinstance(item, Gift):
                                            $ insensitive_tooltip += "{color=#ddddddcc}A gift for someone{/color}"

                                        button:
                                            style "invisible_button"
                                            action NullAction()
                                            xfill True
                                            yfill True
                                            yalign 0.5
                                            tooltip insensitive_tooltip
                                            keyboard_focus False
                                            alt t + " not usable now. " + replace_tags_alt(" ".join(insensitive_tooltip))

                vbar value YScrollValue("inventory_vp") left_bar "gui/inv/vertical_idle_bar.png" thumb "gui/inv/vertical_idle_thumb.png" right_bar "gui/inv/vertical_idle_bar.png" xmaximum 11 ymaximum 324 xalign 1.0 ypos 90 unscrollable "hide" alt "scroll "
        fixed:
            ysize 29
            imagebutton auto "gui/button_%s.png" action [SetVariable("inventory_filter", None), SetVariable("discard_mode", False), Return("exit")] keysym "game_menu" alt "Exit"
            text "Exit" color "#ffffff" font "palanquin_bold" xalign 0.5 alt ""

    if persistent.new_ui:
        use tooltip
    else:
        use tooltip_old_ui


style inventory_button is invisible_button

style inventory_text is gui_text:
    font "exo2_regular"
    size 21

style inventory_label is gui_label:
    xpos 10

style inventory_label_text is gui_label_text:
    size 30


style inventory_items_text is inventory_text:
    idle_color "#fff"
    hover_color "#006284"
    insensitive_color "#ddddddcc"

style inventory_items_text_icon is inventory_text:
    idle_color "#eee"
    hover_color "#006284"
    insensitive_color "#ddddddcc"
    size 18

style filter_title is text:
    color "#fff"
    outlines [(3, "#00000000", 0, 0)]
    size 24
    yalign 0.5

style filter_title_text is filter_title:
    hover_color "#006284"
    hover_outlines [(3, "#00000000", 0, 0)]

style filter_title_select is filter_title:
    idle_color "#fff"
    outlines [(3, "#006284", 0, 0)]

style filter_title_select_text is filter_title_select:
    hover_color "#006284"
    hover_outlines [(3, "#fff", 0, 0)]

style inventory_items_button is invisible_button:
    ysize 27

style inventory_items_button_text is inventory_items_text

style inventory_items_image_button is inventory_items_button:
    yalign 0.5

style tooltips_frame is message_frame:
    padding (10, 15, 10, 15)

style tooltips_text is text:
    size 20
    xalign 0.5
    color "#ffffff"

screen choose_gift(exc=None):
    style_prefix "inventory"
    key ["K_ESCAPE", "mouseup_3", "pad_b_press"] action Return("exit")
    button pos (0, 0) xsize 1280 ysize 720 action Return("exit")
    on "show" action [Hide("quick_menu"), Hide("say")]
    vbox:
        xalign 0.75
        ypos 100
        spacing 10
        xsize 315
        frame:
            ysize 88
            background "gui/inv/equipment_box.png"
            vbox spacing -15:
                label "Clothes:" text_size 25 alt ""
                label "Accessory:" text_size 25 alt ""
            vbox spacing 6:
                pos (145, 10)
                $ clothes, accessory = hero.equipment_for_ui
                text "[clothes]"
                text "[accessory]"
        frame:
            ysize 435
            background "gui/inv/inventory_box.png"
            label "Gift" alt ""
            if hero.inventory:
                viewport id "inventory_vp":
                    style_prefix "inventory_items"
                    xfill True
                    pos (10, 55)
                    ysize 352
                    draggable True
                    mousewheel True
                    has vbox
                    for item in Gift.filtered_sort(
                            filter=lambda x: x.name in hero.inventory,
                            key=lambda x: x.display_name,
                        ):
                        $ t = item.display_name
                        $ n = hero.has_item(item.name)
                        if n > 1:
                            $ t += " ({})".format(n)
                        hbox:
                            xsize 0.93
                            button action Return(item):
                                xfill True
                                yalign 0.5
                                has hbox
                                xfill True
                                yalign 0.5
                                text t yalign 0.5
                                text item.icon align (1.0, 0.5) style "inventory_items_text_icon"
                vbar value YScrollValue("inventory_vp") left_bar "gui/inv/vertical_idle_bar.png" thumb "gui/inv/vertical_idle_thumb.png" right_bar "gui/inv/vertical_idle_bar.png" xmaximum 11 ymaximum 370 xalign 1.0 ypos 50 unscrollable "hide" alt "scroll "
        fixed:
            xysize (315, 29)
            imagebutton auto "gui/button_%s.png" action Return("exit")
            text "Exit" color "#ffffff" font "palanquin_bold" xalign 0.5

screen get_namesurname_screen(name="Mike", surname="Seeker", sex_choice="male"):
    default heroname_input = VariableInputValue("heroname", default=False)
    default family_name_input = VariableInputValue("family_name", default=False)
    key ["K_KP_ENTER", "K_RETURN"] action [heroname_input.Disable(), family_name_input.Disable()]

    style_prefix "setup"
    add gui.game_menu_background

    vbox:
        yalign 0.1
        label "‍✍️" style "setup_title" alt ""
        label "CHOOSE YOUR NAME" style "setup_title" alt ""
        text "What is your first name and last name?" alt f"What is your first name and last name? Currently: {heroname} {family_name}"

    hbox:
        xfill True
        yalign 1.0
        if sex_choice == "male":
            fixed:
                xysize (523, 700)
                null
            imagebutton:
                xalign 0.75
                auto "gui/male_button_%s.png"
                action None
        else:
            imagebutton:
                xalign 0.25
                auto "gui/female_button_%s.png"
                action None
            fixed:
                xysize (495, 700)
                null

    vbox:
        spacing 20
        yalign 0.50
        hbox:
            text "First Name: " style "setup_name_text" yalign 0.5 alt ""
            button:
                style_prefix "none"
                background Frame("gui/button/choice_idle_background.png", Borders(20, 20, 20, 20))
                hover_background Frame("gui/button/choice_hover_background.png", Borders(20, 20, 20, 20))
                selected_background Frame("gui/button/choice_selected_background.png", Borders(20, 20, 20, 20))
                yalign 0.5
                xysize (360, 40)
                action [heroname_input.Toggle()]
                alt f"enter first name: {heroname}"
                tooltip ""
                input:
                    align (0.5, 0.5)
                    color "#ffffff"
                    length 12
                    value heroname_input
        hbox:
            text "Last Name: " style "setup_name_text" yalign 0.5 alt ""
            button:
                style_prefix "none"
                background Frame("gui/button/choice_idle_background.png", Borders(20, 20, 20, 20))
                hover_background Frame("gui/button/choice_hover_background.png", Borders(20, 20, 20, 20))
                selected_background Frame("gui/button/choice_selected_background.png", Borders(20, 20, 20, 20))
                yalign 0.5
                xysize (360, 40)
                action [family_name_input.Toggle()]
                alt f"enter last name: {family_name}"
                tooltip ""
                input:
                    align (0.5, 0.5)
                    color "#ffffff"
                    length 12
                    value family_name_input

    hbox:
        yalign 1.0
        if renpy.has_label("mc_selection_female"):
            textbutton _("BACK") action Rollback() tooltip "" style "game_menu_return_button"
        else:
            frame style "empty" xysize (315, 39)
        textbutton _("CONTINUE") action Return tooltip "" style "game_menu_return_button"

screen get_birthday_screen():
    style_prefix "setup"
    add gui.game_menu_background

    vbox:
        yalign 0.1
        label "‍🎂" style "setup_title" alt ""
        label "CHOOSE YOUR BIRTHDAY" style "setup_title" alt ""
        text "What is your birthday?" alt f"What is your birthday? Currently month: {birthday_month} and day: {str(birthday_day)}"
    vbox:
        xsize 420
        yalign 0.75
        spacing 15
        hbox:
            label "Month: " + birthday_month.title() alt ""
            label "Day: " + str(birthday_day).title() alt ""
        grid 2 2:
            textbutton "Spring" action SetVariable("birthday_month","spring") alt "Set month to spring" tooltip ""
            textbutton "Fall" action SetVariable("birthday_month","fall") alt "Set month to fall" tooltip ""
            textbutton "Summer" action SetVariable("birthday_month","summer") alt "Set month to summer" tooltip ""
            textbutton "Winter" action SetVariable("birthday_month","winter") alt "Set month to winter" tooltip ""
        grid 6 6:
            style_prefix "setup_round"
            for i in range(1, 32):
                textbutton str(i) action SetVariable("birthday_day", i) alt "Set day to {}".format(i) tooltip ""
    hbox:
        yalign 1.0
        textbutton _("BACK") action Rollback() tooltip "" style "game_menu_return_button"
        textbutton _("CONTINUE") action Return tooltip "" style "game_menu_return_button"

screen get_start_date_screen():
    style_prefix "setup"
    add gui.game_menu_background

    vbox:
        yalign 0.1
        label "‍🚩" style "setup_title" alt ""
        label "CHOOSE YOUR STARTING DAY" style "setup_title" alt ""
        text "When do you want the game to start?" alt f"When do you want the game to start? Currently month: {starting_month} and day: {starting_day}"
    vbox:
        xsize 420
        yalign 0.75
        spacing 15
        hbox:
            label "Month: " + starting_month.title() alt ""
            label "Day: " + str(starting_day).title() alt ""

        grid 2 2:
            textbutton "Spring" action SetVariable("starting_month", "spring") alt "Set month to spring" tooltip ""
            textbutton "Fall" action SetVariable("starting_month", "fall") alt "Set month to fall" tooltip ""
            textbutton "Summer" action SetVariable("starting_month", "summer") alt "Set month to summer" tooltip ""
            textbutton "Winter" action SetVariable("starting_month", "winter") alt "Set month to winter" tooltip ""
        grid 6 6:
            style_prefix "setup_round"
            for i in range(1, 32):
                textbutton str(i) action SetVariable("starting_day", i) alt "Set day to {}".format(i) tooltip ""
    hbox:
        yalign 1.0
        textbutton _("BACK") action Rollback() tooltip "" style "game_menu_return_button"
        textbutton _("DONE") action Return tooltip "" style "game_menu_return_button"

style setup_hbox is hbox:
    xalign 0.5
    spacing 20

style setup_vbox is vbox:
    xalign 0.5

style setup_label is label:
    xalign 0.5

style setup_grid is grid:
    xalign 0.5
    spacing 20

style setup_round_grid is grid:
    xalign 0.5

style setup_label_text is label_text:
    font "exo2_regular"
    outlines [(2, "#006284")]

style setup_text is text:
    xalign 0.5

style setup_title is setup_label

style setup_title_text is label_text:
    outlines [(2, "#006284")]
    size 30

style setup_name_text is setup_title_text:
    size 20

style setup_button is choice_button:
    xysize (140, 40)
    background Frame("gui/button/choice_idle_background.png", Borders(20, 20, 20, 20))
    hover_background Frame("gui/button/choice_hover_background.png", Borders(20, 20, 20, 20))
    selected_background Frame("gui/button/choice_selected_background.png", Borders(20, 20, 20, 20))

style setup_button_text is setup_text

style setup_round_button is setup_button:
    xysize (48, 48)
    background Frame("gui/button/round_idle.png", Borders(5, 5, 5, 5))
    hover_background Frame("gui/button/round_hover.png", Borders(5, 5, 5, 5))
    selected_background Frame("gui/button/round_selected.png", Borders(5, 5, 5, 5))

style setup_round_button_text is setup_button_text:
    align (0.5, 0.5)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
