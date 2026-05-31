default CHEAT = False

init python:
    Activity(**{
    "name": "cheats",
    "duration": 0,
    "conditions": [
        "CHEAT",
        HeroTarget(
            MinStat("energy", 0),
            MinStat("hunger", 0),
            MinStat("grooming", 0),
            MinStat("fun", 0),
            ),
    ],
    "icon": "cheat",
    "display_name": "Cheats",
    "label": "cheats",
    })

label cheats:
    call screen cheats
    return

screen cheats():
    style_prefix "cheats"
    modal True
    layer "ui"
    key ["K_ESCAPE", "mouseup_3", "pad_b_press"] action [Return()]
    default cheat_screen = "home"
    default cheat_char = None
    if not renpy.variant( [ "touch", "android" ] ):
        button pos 0,0 xsize 490 ysize 720 action Return() background None
        button pos 790,0 xsize 490 ysize 720 action Return() background None
    frame style "cheats_frame":
        xalign 0.5
        yalign 0.3
        xsize 300
        ysize 470
        xpadding 20
        ypadding 20
        frame style "cheats_title_frame":
            pos -25,-30
            text "CHEATS" style "cheats_title_frame_text"
        if cheat_screen == "home":
            use cheats_viewport("characters"):
                vbox:
                    ypos 20
                    spacing 5
                    if hero.hunger.min == 0:
                        textbutton "God mode: OFF" action [Function(cheat_god_mode, 8)] style "cheats_button"
                    else:
                        textbutton "God mode: ON" action [Function(cheat_god_mode, 0)] style "cheats_button"
                    if hero.is_male:
                        if game.flags.nopreg:
                            textbutton "MC: Infertile" action [Function(cheat_nopreg, False)] style "cheats_button"
                        else:
                            textbutton "MC: Fertile" action [Function(cheat_nopreg, True)] style "cheats_button"
                    textbutton "Attributes" action [SetScreenVariable("cheat_char", hero), SetScreenVariable("cheat_screen", "attributes")] style "cheats_button"
                    textbutton "Needs" action [SetScreenVariable("cheat_screen", "needs")] style "cheats_button"
                    textbutton "Money" action [Function(cheat_money, 1000)] style "cheats_button"
                    textbutton "Lucky!" action [Function(cheat_luck)] sensitive cheat_is_not_lucky() style "cheats_button"
                    textbutton "Stamina!" action [Function(cheat_stamina)] sensitive cheat_no_stamina() style "cheats_button"
                    textbutton "Characters" action [SetScreenVariable("cheat_screen", "characters")] style "cheats_button"

                    textbutton "Skills" action [SetScreenVariable("cheat_screen", "skills")] style "cheats_button"
                    textbutton "Date" action [Function(cheat_date)] sensitive cheat_has_date() style "cheats_button"
            textbutton "Close" action [Return()] style "cheats_button" yalign 1.0
        elif cheat_screen == "attributes":
            use cheats_attr_change(cheat_char)
            if isinstance(cheat_char, Hero):
                textbutton "Back" action SetScreenVariable("cheat_screen", "home") style "cheats_button" yalign 1.0
            else:
                textbutton "Back" action SetScreenVariable("cheat_screen", "characters") style "cheats_button" yalign 1.0
        elif cheat_screen == "needs":
            vbox:
                ypos 20
                spacing 5
                textbutton "ALL" action [Function(cheat_need)] style "cheats_button"
                for need in hero.get_needs():
                    textbutton need.name action [Function(cheat_need, need)] style "cheats_button"
            textbutton "Back" action SetScreenVariable("cheat_screen", "home") style "cheats_button" yalign 1.0
        elif cheat_screen == "characters":
            use cheats_viewport("characters"):
                vbox spacing 5:
                    for person in Person.sort(key=lambda x: x.id):
                        if (hero.gender == "female" and person.id == "bree") or (hero.gender == "male" and person.id == "mike"):
                            continue
                        else:
                            textbutton person.name action [SetScreenVariable("cheat_char", person.id), SetScreenVariable("cheat_screen", "attributes")] style "cheats_button"
            textbutton "Back" action SetScreenVariable("cheat_screen", "home") style "cheats_button" yalign 1.0
        elif cheat_screen == "skills":
            use cheats_viewport("characters"):
                vbox spacing 5:
                    $ skill_list = sorted([(id, skill) for (id, skill) in YAML_SKILLS.items() if skill.gainable])
                    for id, skill in skill_list:
                        if id not in ['hung', 'smalldick'] or (id == "hung" and not hero.has_skill("smalldick")) or (id == "smalldick" and not hero.has_skill("hung")):
                            textbutton skill.display_name action [ToggleField(hero.skills[id], "value", true_value=100, false_value=0), SelectedIf(hero.has_skill(id))] style "cheats_button"
            textbutton "Back" action SetScreenVariable("cheat_screen", "home") style "cheats_button" yalign 1.0
        elif cheat_screen == "time":
            vbox:
                ypos 20
                spacing 5
                textbutton "Next Hour" action [Function(cheat_time, 1)] style "cheats_button" yalign 1.0
                textbutton "Next Day" action [Function(cheat_time, 24)] style "cheats_button" yalign 1.0
                null height 20
                for i in range(0, 4):
                    textbutton SEASONS[i].capitalize() action [Function(cheat_season, i)] sensitive game.season != i style "cheats_button" yalign 1.0
            textbutton "Back" action SetScreenVariable("cheat_screen", "home") style "cheats_button" yalign 1.0

screen cheats_viewport(vpid):
    side "c r":
        area (0, 22, 266, 366)
        viewport id vpid:
            draggable True
            mousewheel True
            transclude
        vbar value YScrollValue(vpid) left_bar "gui/inv/vertical_idle_bar.png" thumb "gui/inv/vertical_idle_thumb.png" right_bar "gui/inv/vertical_idle_bar.png" xpos 5 thumb_offset 10 top_gutter 10.5 bottom_gutter 10.5 unscrollable "hide"

screen cheats_attr_change(owner):
    use cheats_viewport("characters"):
        vbox:
            if isinstance(owner, Hero):
                $ tgt = hero
                $ tgt_type = "hero"
                $ room_key = game.room
            else:
                $ tgt = Person.find(owner)
                $ tgt_type = "npc"
                $ room_key = tgt.room
            text tgt.name size 30 style "cheats_display_text" yalign 0
            $ room = Room.find(room_key).display_name if Room.find(room_key) is not None else room_key.capitalize()
            text f"Location: {room}" style "cheats_display_text" yalign 0
            null height 10
            textbutton "Learn All Traits" action [Function(cheat_traits, tgt)] sensitive cheat_has_traits(tgt) style "cheats_button" yalign 0
            if tgt_type == "hero":
                if tgt.is_male:
                    if game.flags.nopreg:
                        textbutton "MC: Infertile" action [Function(cheat_nopreg, False)] style "cheats_button"
                    else:
                        textbutton "MC: Fertile" action [Function(cheat_nopreg, True)] style "cheats_button"

                if tgt.is_female:
                    if tgt.pregnant:
                        textbutton "Stop MC pregnancy" action [Function(cheat_pregnancy, tgt, False)] selected tgt.pregnant style "cheats_button"
                    else:
                        textbutton "Make MC pregnant" action [Function(cheat_pregnancy, tgt, True)] style "cheats_button"

                    if tgt.is_collared:
                        textbutton "Remove MC collar" action [SetVariable("hero.flags.collared", False)] selected tgt.is_collared style "cheats_button"
                    else:
                        textbutton "Add MC collar" action [SetVariable("hero.flags.collared", True)] style "cheats_button"

                    if tgt.flags.pubes:
                        textbutton "Remove MC pubes" action [SetVariable("hero.flags.pubes", False)] selected tgt.flags.pubes style "cheats_button" yalign 0
                    else:
                        textbutton "Add MC pubes" action [SetVariable("hero.flags.pubes", True)] style "cheats_button" yalign 0

                    textbutton "Switch MC haircut" action [ToggleVariable("hero.flags.haircut", True, False)] style "cheats_button" yalign 0
            else:
                if tgt.is_female:
                    if tgt.pregnant:
                        textbutton "Stop her pregnancy" action [Function(cheat_pregnancy, tgt, False)] style "cheats_button" yalign 0
                    else:
                        textbutton "Make her pregnant" action [Function(cheat_pregnancy, tgt, True)] style "cheats_button" yalign 0
            if tgt.id == "sasha":
                if tgt.flags.boobjob:
                    textbutton "Switch to small breasts" action [SetVariable(f"{tgt.id}.flags.boobjob", False)] style "cheats_button" yalign 0
                else:
                    textbutton "Switch to big breasts" action [SetVariable(f"{tgt.id}.flags.boobjob", True)] style "cheats_button" yalign 0

            textbutton "Wear all piercings" action [Function(cheat_piercings, tgt)] selected cheat_has_piercings(tgt) style "cheats_button" yalign 0
            null height 10
            $ attrs = sorted(cheat_get_attributes(owner), key=lambda x: x.name)
            $ cnt = len(attrs)
            grid 1 cnt:
                for attr in attrs:
                    hbox:
                        spacing 0
                        ysize 25
                        fixed:
                            xsize 160
                            $ npc_attr = attr.name.split("'s ")
                            if len(npc_attr) > 1:
                                text attr.name.split("'s ")[1].capitalize() style "cheats_button_text"
                            else:
                                text attr.name style "cheats_button_text"
                        textbutton "-" action [Function(cheat_attribute, attr, -10)] sensitive not attr.is_min xsize 40 text_size 30 style "cheats_button" text_xalign 0.5 text_yalign 0.63
                        textbutton "+" action [Function(cheat_attribute, attr, 10)] sensitive not attr.is_max xsize 40 text_size 30 style "cheats_button" text_xalign 0.5 text_yalign 0.63

init -10 python:
    def cheat_piercings(target):
        value = not cheat_has_piercings(target)
        for k, v in target.piercings.items():
            v.pierced = value
            v.worn = value


    def cheat_has_piercings(target):
        return all([v.worn for _, v in target.piercings.items()])


    def cheat_is_not_lucky():
        
        return not hero.is_lucky


    def cheat_no_stamina():
        
        return not hero.stamina


    def cheat_god_mode(val):
        hero.hunger.min = val
        hero.energy.min = val
        hero.grooming.min = val
        hero.fun.min = val
        hero.flags.god_mode = True


    def cheat_nopreg(val):
        game.flags.nopreg = val


    def cheat_time(val):
        game.pass_time(val)


    def cheat_season(val):
        game.season = val


    def cheat_money(val):
        hero.money += val


    def cheat_stamina():
        hero.flags.last_sex = (game.hour, game.days_played - 11)


    def cheat_luck():
        hero.luck.val = hero.luck.max


    def cheat_has_date():
        return isinstance(game.active_date, DateAppointment)


    def cheat_has_traits(owner):
        if isinstance(owner, Hero):
            return False
        return not owner.traits.all_known


    def cheat_traits(owner):
        owner.traits.discover_all()


    def cheat_date():
        game.active_date.score = 100


    def cheat_find_target(owner):
        
        if isinstance(owner, Person):
            return owner
        
        return Person.find(owner) if isinstance(owner, basestring) else hero


    def cheat_get_attributes(owner):
        tgt = cheat_find_target(owner)
        for attr in tgt.get_attributes():
            yield attr


    def cheat_pregnancy(owner, value):
        tgt = cheat_find_target(owner)
        if value:
            if isinstance(tgt, Hero):
                tgt.counters.pregnant = 30
            else:
                tgt.counters.pregnant = 9
        else:
            tgt.unpreg()


    def cheat_attribute(attr, increment):
        if attr.scale:
            increment *= attr.scale / 100
        attr += floor(increment)
        return


    def cheat_need(need=None):
        if need is None:
            for need in hero.get_needs():
                need.fill()
        else:
            need.fill()
        return


    def remove_following_date_girl():
        renpy.set_return_stack(renpy.get_return_stack()[:2])
        game.active_date = NoDateEvent()
        active_girl.object = None
        date_girl.object = None

style cheats_button is button:
    idle_background Frame("gui/button_idle.png", Borders(20, 20, 20, 20))
    hover_background Frame("gui/button_hover.png", Borders(20, 20, 20, 20))
    insensitive_background Frame("gui/button_insensitive.png", Borders(20, 20, 20, 20))
    selected_background Frame("gui/button_hover.png", Borders(20, 20, 20, 20))
    selected_hover_background Frame("gui/button_idle.png", Borders(20, 20, 20, 20))
    xfill True
    yalign 0.5

style cheats_button_text is text:
    color "#ffffff"
    font "palanquin_medium"
    yalign 0.5
    xpos 15
    size 20

style cheats_display_text is text:
    color "#ffffff"
    font "palanquin_medium"
    xpos 15
    size 20

style cheats_title is text:
    font "palanquin_medium"
    size 30
    color "#ffffff"

style cheats_select_text is text:
    color "#fff"
    font "exo2_regular"
    size 23
    hover_color "#D84747"

style cheats_frame is frame:
    background Frame("gui/textbox.png", Borders(20, 20, 20, 20))

style cheats_title_frame is frame:
    background Frame("gui/pname_box.png", Borders(20, 20, 20, 20))
    xpadding 20
    ypadding 0

style cheats_title_frame_text is text:
    font "palanquin_bold"
    size 25
    color "#D84747"
    ypos -3
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
