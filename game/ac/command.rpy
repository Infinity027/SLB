init python:
    InteractActivity(**{
    "name": "command",
    "label": "command_girl",
    "display_name": "Command",
    "icon": "command",
    "duration": 0,
    "conditions": [
        ActiveTarget(
            IsFlag("breakup", False),
            MinStat("sub", 50),
            ),
        ],
    "once_day": "ACTIVE",
    })


label command_girl:
    $ shuffle_choices = False
    call expression f"{active_girl.id}_greet" from _call_expression_70
    $ renpy.show(active_girl.id)
    menu:
        "Do something for me":
            menu:
                "Give me some money":
                    $ hero.money += 25
                    $ active_girl.love -= 2
                "Clean this room" if game.room == "secondfloor" and not Conditioned.done_yesterday("clean_the_secondfloor") and active_girl.sub >= 25:
                    $ game.set_flag("chores", 25, "week", "+")
                    $ DONE["clean_the_secondfloor"] = game.days_played
                    if active_girl.sub <= 50:
                        $ active_girl.love -= 1
                        $ active_girl.sub += 1
                "Clean this room" if game.room == "livingroom" and not Conditioned.done_yesterday("clean_the_livingroom") and active_girl.sub >= 25:
                    $ game.set_flag("chores", 25, "week", "+")
                    $ DONE["clean_the_livingroom"] = game.days_played
                    if active_girl.sub <= 50:
                        $ active_girl.love -= 1
                        $ active_girl.sub += 1
                "Clean this room" if game.room == "bathroom" and not Conditioned.done_yesterday("clean_the_bathroom") and active_girl.sub >= 25:
                    $ game.set_flag("chores", 25, "week", "+")
                    $ DONE["clean_the_bathroom"] = game.days_played
                    if active_girl.sub <= 50:
                        $ active_girl.love -= 1
                        $ active_girl.sub += 1
                "Clean the pool" if game.room == "pool" and not Conditioned.done_yesterday("clean_the_pool") and active_girl.sub >= 25:
                    $ game.set_flag("chores", 25, "week", "+")
                    $ DONE["clean_the_pool"] = game.days_played
                    if active_girl.sub <= 50:
                        $ active_girl.love -= 1
                        $ active_girl.sub += 1
                "Do the dishes" if game.room == "kitchen" and not Conditioned.done_today("do_the_dishes") and active_girl.sub >= 25:
                    $ game.set_flag("chores", 5, "week", "+")
                    $ DONE["do_the_dishes"] = game.days_played
                "Work extra hours at the strip club" if active_girl.id == "shiori" and "shiori_payoff_conversation" in DONE and shiori.flags.schedule == "default" and shiori.sub >= 75:
                    $ shiori.flags.schedule = "stripclub"
                "Stop working at the strip club" if active_girl.id == "shiori" and "shiori_payoff_conversation" in DONE and shiori.flags.schedule == "stripclub":
                    $ shiori.flags.schedule = "default"
                "Work extra hours at the strip club" if active_girl.id == "hanna" and "hanna_event_09" in DONE and hanna.flags.schedule == "default" and hanna.sub >= 75:
                    $ hanna.flags.schedule = "stripclub"
                "Stop working at the strip club" if active_girl.id == "hanna" and "hanna_event_09" in DONE and hanna.flags.schedule == "stripclub":
                    $ hanna.flags.schedule = "default"
                "Work extra hours at the strip club" if active_girl.id == "harmony" and "harmony_stripclub_event_02" in DONE and harmony.flags.schedule == "default" and harmony.sub >= 75:
                    $ harmony.flags.schedule = "stripclub"
                "Stop working at the strip club" if active_girl.id == "harmony" and "harmony_stripclub_event_02" in DONE and harmony.flags.schedule == "stripclub":
                    $ harmony.flags.schedule = "default"
                "Work extra hours at the strip club" if active_girl.id == "bree" and "bree_stripclub_intro" in DONE and not bree.flags.work_stripclub:
                    $ bree.flags.work_stripclub = True
                "Stop working at the strip club" if active_girl.id == "bree" and "bree_stripclub_intro" in DONE and bree.flags.work_stripclub:
                    $ bree.flags.work_stripclub = False
                "Work extra hours at the strip club" if active_girl.id == "lexi" and lexi.flags.schedule == "harem" and lexi.flags.giftsexy_dress and active_girl.sub >= 50 and not lexi.flags.work_stripclub:
                    $ lexi.flags.work_stripclub = True
                "Stop working at the strip club" if active_girl.id == "lexi" and lexi.flags.schedule == "harem" and lexi.flags.giftsexy_dress and active_girl.sub >= 50 and lexi.flags.work_stripclub:
                    $ lexi.flags.work_stripclub = False
                "Ask me out sometime" if not active_girl.flags.nodate and active_girl.flags.noaskout:
                    $ active_girl.flags.noaskout = False
                "Stop asking me out" if not active_girl.flags.nodate and not active_girl.flags.noaskout:
                    $ active_girl.flags.noaskout = True
                "Cancel":
                    $ hero.cancel_activity()
        "About what we call each other" if hero.gender == 'male':
            menu:


                "Call me Master" if active_girl.flags.mikeNickname not in nickname_master and active_girl.is_collared:
                    $ active_girl.flags.mikeNickname = "Master"
                "Stop calling me Master" if active_girl.flags.mikeNickname in nickname_master:
                    $ active_girl.flags.mikeNickname = None

                "Call me Daddy" if active_girl.flags.mikeNickname not in nickname_daddy and active_girl.love > 150:
                    $ active_girl.flags.mikeNickname = "Daddy"
                "Stop calling me Daddy" if active_girl.flags.mikeNickname in nickname_daddy:
                    $ active_girl.flags.mikeNickname = None

                "Call me Sweetie" if active_girl.flags.mikeNickname not in nickname_sweetie and not active_girl.flags.cheated:
                    $ active_girl.flags.mikeNickname = "Sweetie"
                "Stop calling me Sweetie" if active_girl.flags.mikeNickname in nickname_sweetie:
                    $ active_girl.flags.mikeNickname = None

                "Call me Handsome" if active_girl.flags.mikeNickname not in nickname_handsome and hero.charm > 50:
                    $ active_girl.flags.mikeNickname = "Handsome"
                "Stop calling me Handsome" if active_girl.flags.mikeNickname in nickname_handsome:
                    $ active_girl.flags.mikeNickname = None

                "Call me Bro" if active_girl.flags.mikeNickname not in nickname_bro and active_girl.love > 100:
                    $ active_girl.flags.mikeNickname = "Bro"
                "Stop calling me Bro" if active_girl.flags.mikeNickname in nickname_bro:
                    $ active_girl.flags.mikeNickname = None

                "Call me Stud" if active_girl.flags.mikeNickname not in nickname_stud and active_girl.love > 130:
                    $ active_girl.flags.mikeNickname = "Stud"
                "Stop calling me Stud" if active_girl.flags.mikeNickname in nickname_stud:
                    $ active_girl.flags.mikeNickname = None

                "Call me Husband" if active_girl.flags.mikeNickname not in nickname_husband and active_girl.status in ["fiance"]:
                    $ active_girl.flags.mikeNickname = "Husband"
                "Stop calling me Husband" if active_girl.flags.mikeNickname in nickname_husband:
                    $ active_girl.flags.mikeNickname = None

                "Talk about personal nickname" if renpy.has_label(f"command_nickname_{active_girl.id.lower()}"):
                    call expression "command_nickname_" + active_girl.id.lower() from _call_expression_68

                "Let's spice up our interactions" if renpy.has_label(f"submissive_interact_{active_girl.id}_{hero.gender}"):
                    call expression f"submissive_interact_{active_girl.id}_{hero.gender}" from _call_expression_14
                "Cancel":

                    $ hero.cancel_activity()
        "About birth control" if active_girl.is_female:
            menu:
                "You should start taking the pill" if active_girl.is_female and not active_girl.id == "palla" and not active_girl.flags.pill and active_girl.counters.pregnant == 0 and (active_girl.sub >= 50 or active_girl.love >= 100) and active_girl.sexperience >= 1:
                    $ active_girl.flags.pill = True
                    $ active_girl.flags.unpilled = False
                "You should stop taking the pill" if active_girl.is_female and not active_girl.id == "palla" and active_girl.flags.pill and (active_girl.sub >= 50 or active_girl.love >= 150) and active_girl.sexperience >= 1:
                    $ active_girl.flags.pill = False

                "You should stop taking the pill" if active_girl.id == "palla" and palla.flags.pill and (palla.sub >= 50 and palla.love >= 150) and palla.sexperience and not palla.flags.babyok:
                    call palla_pill_talk from _call_palla_pill_talk
                "You should start taking the pill" if active_girl.id == "palla" and palla.flags.babyok and not palla.flags.pill and active_girl.counters.pregnant == 0 and (palla.sub >= 50 and palla.love >= 100) and palla.sexperience:
                    $ palla.flags.pill = True
                "You should stop taking the pill" if active_girl.id == "palla" and palla.flags.babyok and palla.flags.pill and (palla.sub >= 50 and palla.love >= 150) and palla.sexperience:
                    $ palla.flags.pill = False
                "Cancel":
                    $ hero.cancel_activity()
        "About your body/appearance":
            call screen appearance(active_girl) onlayer screens
        "Cancel":
            $ hero.cancel_activity()
    $ renpy.hide(active_girl.id)
    $ shuffle_choices = True
    return


screen appearance(npc=None):
    style_prefix "appearance"

    key ["K_ESCAPE", "mouseup_3", "pad_b_press"] action Return()

    on "show" action [Hide("smartphone"), Hide("story_tracker"), Function(hide_people)]
    on "hide" action Function(show_people)

    default submenu = None
    default shown_npc = npc
    default shown_attributes = set()
    default refresh = False

    $ pierced_piercings = [v for _, v in shown_npc.piercings.items() if v.pierced]

    frame:
        background None
        if not shown_attributes:
            $ shown_attributes = {shown_npc.get_clothes()}
        $ shown_attributes.update({pi.location for pi in pierced_piercings if pi.worn})
        $ display_shown = " ".join(shown_attributes)
        add "[shown_npc.id] ['anim' if npc.id in anim_tag and persistent.live2d_on else ''] [display_shown]" xalign 0.25

    vbox:
        xalign 0.75
        ypos 100
        spacing 10
        xsize 315
        frame:
            ysize 435
            background "gui/inv/inventory_box.png"
            label "[npc.name]"
            viewport id "inventory_vp":
                style_prefix "appearance_items"
                xfill True
                xpos 10
                ypos 55
                ysize 352
                draggable True
                mousewheel True
                has vbox

                vbox:
                    xfill True
                    textbutton "Casual outfit":
                        action [
                                ToggleScreenVariable("submenu", "casual", None),
                                SetScreenVariable("shown_attributes", {"casual"})
                                ]
                        hovered If(not submenu, SetScreenVariable("shown_attributes", {"casual"}))
                if shown_npc.flags.giftpure_casual and (shown_npc.id != "reona" or shown_npc.purity >= 50) or shown_npc.flags.giftinnocent_casual:
                    if submenu == "casual":
                        vbox:
                            style_prefix "appearance_submenu_items"
                            xfill True
                            textbutton "Casual":
                                xpos 0.10
                                action [
                                        SetField(shown_npc, "flags.purecasual", False),
                                        SetField(shown_npc, "flags.innocentcasual", False),
                                        SetScreenVariable("shown_attributes", {"casual"})
                                        ]
                                selected not(shown_npc.flags.purecasual or shown_npc.flags.innocentcasual)
                                hovered [
                                        SetScreenVariable("shown_attributes", {"casual"})
                                        ]
                            if shown_npc.flags.giftpure_casual and (shown_npc.id != "reona" or shown_npc.purity >= 50):
                                textbutton "Pure casual":
                                    xpos 0.10
                                    action [
                                            SetField(shown_npc, "flags.purecasual", True),
                                            SetField(shown_npc, "flags.innocentcasual", False),
                                            SetScreenVariable("shown_attributes", {"casual"})
                                            ]
                                    selected shown_npc.flags.purecasual
                                    hovered [
                                            SetScreenVariable("shown_attributes", {"purecasual"})
                                            ]
                            if shown_npc.flags.giftinnocent_casual:
                                textbutton "Innocent casual":
                                    xpos 0.10
                                    action [
                                            SetField(shown_npc, "flags.purecasual", False),
                                            SetField(shown_npc, "flags.innocentcasual", True),
                                            SetScreenVariable("shown_attributes", {"casual"})
                                            ]
                                    selected shown_npc.flags.innocentcasual
                                    hovered [
                                            SetScreenVariable("shown_attributes", {"innocentcasual"})
                                            ]


                if (shown_npc.flags.giftsexy_dress and (shown_npc.id != "reona" or shown_npc.purity < 20)) or (shown_npc.flags.giftslutty_dress and (shown_npc.id != "reona" or shown_npc.purity < 10)) or (shown_npc.flags.giftpure_date and (shown_npc.id != "reona" or shown_npc.purity >= 60)):
                    vbox:
                        xfill True
                        textbutton "Date outfit":
                            action [
                                    ToggleScreenVariable("submenu", "date", None),
                                    SetScreenVariable("shown_attributes", {"date"})
                                    ]
                            hovered If(not submenu, SetScreenVariable("shown_attributes", {"date"}))
                    if submenu == "date":
                        vbox:
                            style_prefix "appearance_submenu_items"
                            xfill True
                            textbutton "Date":
                                xpos 0.10
                                action [
                                        SetField(shown_npc, "flags.sexydate", False),
                                        SetField(shown_npc, "flags.sluttydate", False),
                                        SetField(shown_npc, "flags.puredate", False),
                                        SetScreenVariable("shown_attributes", {"casual_date"})
                                        ]
                                selected not(shown_npc.flags.sexydate or shown_npc.flags.sluttydate or shown_npc.flags.puredate)
                                hovered [
                                        SetScreenVariable("shown_attributes", {"casual_date"})
                                        ]
                            if shown_npc.flags.giftsexy_dress and (shown_npc.id != "reona" or shown_npc.purity < 20):
                                textbutton "Sexy date":
                                    xpos 0.10
                                    action [
                                            SetField(shown_npc, "flags.sexydate", True),
                                            SetField(shown_npc, "flags.sluttydate", False),
                                            SetField(shown_npc, "flags.puredate", False),
                                            SetScreenVariable("shown_attributes", {"date"})
                                            ]
                                    selected shown_npc.flags.sexydate
                                    hovered [
                                            SetScreenVariable("shown_attributes", {"sexydate"})
                                            ]
                            if shown_npc.flags.giftslutty_dress and (shown_npc.id != "reona" or shown_npc.purity < 10):
                                textbutton "Slutty date":
                                    xpos 0.10
                                    action [
                                            SetField(shown_npc, "flags.sexydate", False),
                                            SetField(shown_npc, "flags.sluttydate", True),
                                            SetField(shown_npc, "flags.puredate", False),
                                            SetScreenVariable("shown_attributes", {"date"})
                                            ]
                                    selected shown_npc.flags.sluttydate
                                    hovered [
                                            SetScreenVariable("shown_attributes", {"sluttydate"})
                                            ]
                            if shown_npc.flags.giftpure_date and (shown_npc.id != "reona" or shown_npc.purity >= 60):
                                textbutton "Pure date":
                                    xpos 0.10
                                    action [
                                            SetField(shown_npc, "flags.sexydate", False),
                                            SetField(shown_npc, "flags.sluttydate", False),
                                            SetField(shown_npc, "flags.puredate", True),
                                            SetScreenVariable("shown_attributes", {"date"})
                                            ]
                                    selected shown_npc.flags.puredate
                                    hovered [
                                            SetScreenVariable("shown_attributes", {"puredate"})
                                            ]


                if shown_npc.flags.giftsexy_swimsuit or shown_npc.flags.giftslutty_swimsuit:
                    vbox:
                        xfill True
                        textbutton "Swimsuit outfit":
                            action [
                                    ToggleScreenVariable("submenu", "swimsuit", None),
                                    SetScreenVariable("shown_attributes", {"swimsuit"})
                                    ]
                            hovered If(not submenu, SetScreenVariable("shown_attributes", {"swimsuit"}))
                    if submenu == "swimsuit":
                        vbox:
                            style_prefix "appearance_submenu_items"
                            xfill True
                            textbutton "Swimsuit":
                                xpos 0.10
                                action [
                                        SetField(shown_npc, "flags.sexyswimsuit", False),
                                        SetField(shown_npc, "flags.sluttyswimsuit", False),
                                        SetScreenVariable("shown_attributes", {"casual_swimsuit"})
                                        ]
                                selected not(shown_npc.flags.sexyswimsuit or shown_npc.flags.sluttyswimsuit)
                                hovered [
                                        SetScreenVariable("shown_attributes", {"casual_swimsuit"})
                                        ]
                            if shown_npc.flags.giftsexy_swimsuit:
                                textbutton "Sexy swimsuit":
                                    xpos 0.10
                                    action [
                                            SetField(shown_npc, "flags.sexyswimsuit", True),
                                            SetField(shown_npc, "flags.sluttyswimsuit", False),
                                            SetScreenVariable("shown_attributes", {"swimsuit"})
                                            ]
                                    selected shown_npc.flags.sexyswimsuit
                                    hovered [
                                            SetScreenVariable("shown_attributes", {"sexyswimsuit"})
                                            ]
                            if shown_npc.flags.giftslutty_swimsuit:
                                textbutton "Slutty swimsuit":
                                    xpos 0.10
                                    action [
                                            SetField(shown_npc, "flags.sexyswimsuit", False),
                                            SetField(shown_npc, "flags.sluttyswimsuit", True),
                                            SetScreenVariable("shown_attributes", {"swimsuit"})
                                            ]
                                    hovered [
                                            SetScreenVariable("shown_attributes", {"sluttyswimsuit"})
                                            ]
                                    selected shown_npc.flags.sluttyswimsuit


                if shown_npc.flags.giftlingerie and (shown_npc.id != "reona" or (shown_npc.purity < 20 and shown_npc.sub >= 50)):
                    vbox:
                        xfill True
                        textbutton "Underwear outfit":
                            action [
                                    ToggleScreenVariable("submenu", "underwear", None),
                                    SetScreenVariable("shown_attributes", {"underwear"})
                                    ]
                            hovered If(not submenu, SetScreenVariable("shown_attributes", {"underwear"}))
                    if submenu == "underwear":
                        vbox:
                            style_prefix "appearance_submenu_items"
                            xfill True
                            textbutton "Underwear":
                                xpos 0.10
                                action [
                                        SetField(shown_npc, "flags.sexyunderwear", False),
                                        SetScreenVariable("shown_attributes", {"casual_underwear"})
                                        ]
                                selected not shown_npc.flags.sexyunderwear
                                hovered [
                                        SetScreenVariable("shown_attributes", {"casual_underwear"})
                                        ]
                            if shown_npc.flags.giftlingerie and (shown_npc.id != "reona" or (shown_npc.purity < 20 and shown_npc.sub >= 50)):
                                textbutton "Sexy underwear":
                                    xpos 0.10
                                    action [
                                            SetField(shown_npc, "flags.sexyunderwear", True),
                                            SetScreenVariable("shown_attributes", {"underwear"})
                                            ]
                                    selected shown_npc.flags.sexyunderwear
                                    hovered [
                                            SetScreenVariable("shown_attributes", {"sexyunderwear"})
                                            ]


                if shown_npc.flags.giftslave_collar:
                    vbox:
                        xfill True
                        textbutton "Collar":
                            action [
                                    ToggleScreenVariable("submenu", "collar", None)
                                    ]
                    if submenu == "collar":
                        vbox:
                            style_prefix "appearance_submenu_items"
                            xfill True
                            textbutton "Wear your collar":
                                xpos 0.10
                                action [
                                        SetField(shown_npc, "flags.collared", True),
                                        SetScreenVariable("shown_attributes", {})
                                        ]
                                hovered [
                                        SetScreenVariable("shown_attributes", {"collar"})
                                        ]
                                selected shown_npc.flags.collared
                            textbutton "Remove your collar":
                                xpos 0.10
                                action [
                                        SetField(shown_npc, "flags.collared", False),
                                        SetScreenVariable("shown_attributes", {})
                                        ]
                                hovered [
                                        SetScreenVariable("shown_attributes", {"-collar"})
                                        ]
                                selected not shown_npc.flags.collared


                if pierced_piercings:
                    vbox:
                        xfill True
                        textbutton "Piercings":
                            action [
                                    ToggleScreenVariable("submenu", "piercings", None),
                                    SetScreenVariable("shown_attributes", {"naked"})
                                    ]
                            hovered If(not submenu, SetScreenVariable("shown_attributes", {"naked"}.union({pi.location for pi in pierced_piercings if pi.worn})))
                    if submenu == "piercings":
                        vbox:
                            style_prefix "appearance_submenu_items"
                            xfill True
                            for piercing in pierced_piercings:
                                textbutton "[piercing.location!cl]":
                                    selected piercing.worn
                                    xpos 0.10
                                    action [
                                            ToggleField(shown_npc.piercings, f"{piercing.location}.worn", True, False),
                                            ToggleSetMembership(shown_attributes, piercing.location)
                                            ]


                if shown_npc.is_female and shown_npc.sub >= 75:
                    vbox:
                        xfill True
                        textbutton "Pubes":
                            action [
                                    ToggleScreenVariable("submenu", "pubes", None),
                                    SetScreenVariable("shown_attributes", {"naked"})
                                    ]
                            hovered If(not submenu, SetScreenVariable("shown_attributes", {"naked", "pubes" if shown_npc.flags.pubes else ""}))
                    if submenu == "pubes":
                        vbox:
                            style_prefix "appearance_submenu_items"
                            xfill True
                            textbutton "Shave your pussy":
                                xpos 0.10
                                action [
                                        SetField(shown_npc, "flags.pubes", False),
                                        SetScreenVariable("shown_attributes", {"naked"})
                                        ]
                                hovered [
                                        SetScreenVariable("shown_attributes", {"naked", "-pubes"})
                                        ]
                                selected not shown_npc.flags.pubes
                            textbutton "Stop shaving":
                                xpos 0.10
                                action [
                                        SetField(shown_npc, "flags.pubes", True),
                                        SetScreenVariable("shown_attributes", {"naked"})
                                        ]
                                hovered [
                                        SetScreenVariable("shown_attributes", {"naked", "pubes"})
                                        ]
                                selected shown_npc.flags.pubes


                if shown_npc.id in ["hanna"] and shown_npc.is_female and shown_npc.sub >= 50:
                    vbox:
                        xfill True
                        textbutton "Armpits":
                            action [
                                    ToggleScreenVariable("submenu", "armpits", None),
                                    SetScreenVariable("shown_attributes", {"naked"})
                                    ]
                    if submenu == "armpits":
                        vbox:
                            style_prefix "appearance_submenu_items"
                            xfill True
                            textbutton "Shave your armpits":
                                xpos 0.10
                                action [
                                        SetField(shown_npc, "flags.armpits", False),
                                        SetScreenVariable("shown_attributes", {})
                                        ]
                                hovered [
                                        SetScreenVariable("shown_attributes", {"-armpits"})
                                        ]
                                selected not shown_npc.flags.armpits
                            textbutton "Stop shaving":
                                xpos 0.10
                                action [
                                        SetField(shown_npc, "flags.armpits", True),
                                        SetScreenVariable("shown_attributes", {})
                                        ]
                                hovered [
                                        SetScreenVariable("shown_attributes", {"armpits"})
                                        ]
                                selected shown_npc.flags.armpits


                if shown_npc.id in ["aletta", "camila", "kleio", "minami", "sasha", "reona", "cherie", "claire", "kiara"] and shown_npc.sub >= 25 and not shown_npc.flags.haircutDelay:
                    if shown_npc.id == "aletta" and ("aletta_event_03b" in DONE or "aletta_event_05b" in DONE) and shown_npc.sub >= 50:
                        $ text_do = "Untie your hair"
                        $ text_undo = "Tie your hair"
                    elif shown_npc.id == "camila" and "camila_event_06" in DONE:
                        $ text_do = "Tie your hair"
                        $ text_undo = "Untie your hair"
                    elif shown_npc.id == "kleio" and "kleio_twintails_02" in DONE and shown_npc.sub >= 35:
                        $ text_do = "Grow your hair"
                        $ text_undo = "Cut your hair"
                    elif shown_npc.id == "minami" and "minami_likes_blondes" in DONE:
                        $ text_do = "Dye your hair"
                        $ text_undo = "Undye your hair"
                    elif shown_npc.id == "sasha" and "sasha_likes_blondes_2" in DONE:
                        $ text_do = "Dye your hair"
                        $ text_undo = "Undye your hair"
                    elif shown_npc.id == "reona" and shown_npc.purity >= 50:
                        $ text_do = "Undye your hair"
                        $ text_undo = "Dye your hair"
                    elif shown_npc.id == "cherie":
                        $ text_do = "Tie your hair"
                        $ text_undo = "Untie your hair"
                    elif shown_npc.id == "claire":
                        $ text_do = "Untie your hair"
                        $ text_undo = "Tie your hair"
                    elif shown_npc.id == "kiara":
                        $ text_do = "Tie your hair"
                        $ text_undo = "Untie your hair"
                    else:
                        $ text_do = None
                        $ text_undo = None

                    if text_do:
                        vbox:
                            xfill True
                            textbutton "Haircut":
                                action [
                                        ToggleScreenVariable("submenu", "haircut", None)
                                        ]
                            if submenu == "haircut":
                                vbox:
                                    style_prefix "appearance_submenu_items"
                                    xfill True
                                    textbutton text_do:
                                        xpos 0.10
                                        action [
                                                SetField(shown_npc, "flags.haircut", True),
                                                SetScreenVariable("shown_attributes", {})
                                                ]
                                        hovered [
                                                SetScreenVariable("shown_attributes", {"haircut"})
                                                ]
                                        selected shown_npc.flags.haircut
                                    textbutton text_undo:
                                        xpos 0.10
                                        action [
                                                SetField(shown_npc, "flags.haircut", False),
                                                SetScreenVariable("shown_attributes", {})
                                                ]
                                        hovered [
                                                SetScreenVariable("shown_attributes", {"nohaircut"})
                                                ]
                                        selected not shown_npc.flags.haircut


                if shown_npc.id in ["morgan"] and shown_npc.male < 40:
                    vbox:
                        xfill True
                        textbutton "Makeup":
                            action [
                                    ToggleScreenVariable("submenu", "makeup", None),
                                    ]

                    if submenu == "makeup":
                        vbox:
                            style_prefix "appearance_submenu_items"
                            xfill True
                            textbutton "Wear makeup":
                                xpos 0.10
                                action [
                                        SetField(shown_npc, "flags.nomakeup", False),
                                        SetScreenVariable("shown_attributes", {})
                                        ]
                                hovered [
                                        SetScreenVariable("shown_attributes", {"makeup"})
                                        ]
                                selected not shown_npc.flags.nomakeup
                            textbutton "Remove makeup":
                                xpos 0.10
                                action [
                                        SetField(shown_npc, "flags.nomakeup", True),
                                        SetScreenVariable("shown_attributes", {})
                                        ]
                                hovered [
                                        SetScreenVariable("shown_attributes", {"-makeup"})
                                        ]
                                selected shown_npc.flags.nomakeup


                if shown_npc.id in ["bree", "lexi", "minami", "samantha", "sasha"] and shown_npc.sub >= 90:
                    vbox:
                        xfill True
                        label "At home:"
                        textbutton "Clothes policy":
                            action [
                                    ToggleScreenVariable("submenu", "home_policy", None),
                                    SetScreenVariable("shown_attributes", {"casual"}),
                                    ]
                            hovered [
                                    If(not submenu, SetScreenVariable("shown_attributes", {"casual", "topless" if shown_npc.flags.topless else "", "naked" if shown_npc.flags.naked else ""})),
                                    ]
                    if submenu == "home_policy":
                        vbox:
                            style_prefix "appearance_submenu_items"
                            xfill True
                            textbutton "Clothed":
                                xpos 0.10
                                action [
                                            SetField(shown_npc, "flags.topless", False),
                                            SetField(shown_npc, "flags.naked", False),
                                            SetScreenVariable("shown_attributes", {"casual"})
                                            ]
                                hovered [
                                        SetScreenVariable("shown_attributes", {"casual", "-topless", "-naked"})
                                        ]
                                selected not (shown_npc.flags.topless or shown_npc.flags.naked)
                            textbutton "Topless":
                                xpos 0.10
                                action [
                                            SetField(shown_npc, "flags.topless", True),
                                            SetField(shown_npc, "flags.naked", False),
                                            SetScreenVariable("shown_attributes", {"casual", "topless"})
                                            ]
                                hovered [
                                        SetScreenVariable("shown_attributes", {"casual", "topless"})
                                        ]
                                selected shown_npc.flags.topless
                            textbutton "Naked":
                                xpos 0.10
                                action [
                                            SetField(shown_npc, "flags.topless", False),
                                            SetField(shown_npc, "flags.naked", True),
                                            SetScreenVariable("shown_attributes", {"casual", "naked"})
                                            ]
                                hovered [
                                        SetScreenVariable("shown_attributes", {"casual", "naked"})
                                        ]
                                selected shown_npc.flags.naked



                if shown_npc.id == "cassidy" and shown_npc.status in ["pet", "sex slave"]:
                    vbox:
                        xfill True
                        label "At work:"
                    vbox:
                        xfill True
                        textbutton "Uniform policy":
                            action [
                                    ToggleScreenVariable("submenu", "work_policy", None),
                                    SetScreenVariable("shown_attributes", {"work"}),
                                    ]
                            hovered [
                                    If(not submenu, SetScreenVariable("shown_attributes", {"work"})),
                                    ]
                    if submenu == "work_policy":
                        vbox:
                            xfill True
                            style_prefix "appearance_submenu_items"
                            textbutton "Fully clothed":
                                xpos 0.10
                                action [
                                            SetField(shown_npc, "flags.topless", False),
                                            SetScreenVariable("shown_attributes", {"work"})
                                            ]
                                hovered [
                                        SetScreenVariable("shown_attributes", {"work", "-topless"})
                                        ]
                                selected not (shown_npc.flags.topless or shown_npc.flags.naked)
                            textbutton "Topless":
                                xpos 0.10
                                action [
                                            SetField(shown_npc, "flags.topless", True),
                                            SetScreenVariable("shown_attributes", {"work", "topless"})
                                            ]
                                hovered [
                                        SetScreenVariable("shown_attributes", {"work", "topless"})
                                        ]
                                selected shown_npc.flags.topless

                if shown_npc.id in ["aletta", "audrey", "lavish", "shiori"] and game.flags.isceo and shown_npc.sub >= 50:
                    vbox:
                        xfill True
                        label "At work:"

                    if shown_npc.sub >= 90:
                        vbox:
                            xfill True
                            textbutton "Uniform policy":
                                action [
                                        ToggleScreenVariable("submenu", "work_policy", None),
                                        SetScreenVariable("shown_attributes", {"work"}),
                                        ]
                                hovered [
                                        If(not submenu, SetScreenVariable("shown_attributes", {"work", "topless" if shown_npc.flags.topless else ""})),
                                        ]
                        if submenu == "work_policy":
                            vbox:
                                xfill True
                                style_prefix "appearance_submenu_items"
                                textbutton "Fully clothed":
                                    xpos 0.10
                                    action [
                                                SetField(shown_npc, "flags.topless", False),
                                                SetScreenVariable("shown_attributes", {"work"}),
                                                ]
                                    hovered [
                                            SetScreenVariable("shown_attributes", {"work", "-topless"})
                                            ]
                                    selected not shown_npc.flags.topless
                                textbutton "Topless":
                                    xpos 0.10
                                    action [
                                                SetField(shown_npc, "flags.topless", True),
                                                SetScreenVariable("shown_attributes", {"work", "topless"})
                                                ]
                                    hovered [
                                            SetScreenVariable("shown_attributes", {"work", "topless"})
                                            ]
                                    selected shown_npc.flags.topless

                    vbox:
                        xfill True
                        textbutton "Work uniform":
                            action [
                                    ToggleScreenVariable("submenu", "work", None),
                                    SetScreenVariable("shown_attributes", {"work"}),
                                    ]
                            hovered [
                                    If(not submenu, SetScreenVariable("shown_attributes", {"work", "topless" if shown_npc.flags.topless else ""})),
                                    ]
                    if submenu == "work":
                        vbox:
                            style_prefix "appearance_submenu_items"
                            xfill True
                            textbutton "Casual uniform":
                                xpos 0.10
                                action [
                                        SetField(shown_npc, "flags.sexywork", False),
                                        SetScreenVariable("shown_attributes", {"work", "topless" if shown_npc.flags.topless else ""}),
                                        ]
                                selected not shown_npc.flags.sexywork
                                hovered [
                                        SetScreenVariable("shown_attributes", {"work", "topless" if shown_npc.flags.topless else ""}),
                                        ]
                            textbutton "Sexy uniform":
                                xpos 0.10
                                action [
                                        SetField(shown_npc, "flags.sexywork", True),
                                        SetScreenVariable("shown_attributes", {"sexywork", "topless" if shown_npc.flags.topless else ""}),
                                        ]
                                selected shown_npc.flags.sexywork
                                hovered [
                                        SetScreenVariable("shown_attributes", {"sexywork", "topless" if shown_npc.flags.topless else ""}),
                                        ]

                if shown_npc.id in ["bree", "hanna", "harmony", "lexi", "reona", "shiori"] and (shown_npc.flags.schedule == "stripclub" or shown_npc.flags.work_stripclub) and ((shown_npc.flags.giftsexy_dress and (shown_npc.id != "reona" or shown_npc.purity < 20)) or (shown_npc.flags.giftslutty_dress and (shown_npc.id != "reona" or shown_npc.purity < 10))):
                    vbox:
                        xfill True
                        label "At the stripclub:"

                    vbox:
                        xfill True
                        textbutton "Stripper outfit":
                            action [
                                    ToggleScreenVariable("submenu", "stripclub", None),
                                    SetScreenVariable("shown_attributes", {shown_npc.flags.stripper_outfit if shown_npc.flags.stripper_outfit else "stripper"}),
                                    ]
                            hovered [
                                    If(not submenu, SetScreenVariable("shown_attributes", {shown_npc.flags.stripper_outfit if shown_npc.flags.stripper_outfit else "stripper"})),
                                    ]
                    if submenu == "stripclub":
                        vbox:
                            style_prefix "appearance_submenu_items"
                            xfill True
                            textbutton "Stripper":
                                xpos 0.10
                                action [
                                        SetField(shown_npc, "flags.stripper_outfit", "stripper"),
                                        SetScreenVariable("shown_attributes", {"stripper",}),
                                        ]
                                selected shown_npc.flags.stripper_outfit == "stripper" or not shown_npc.flags.stripper_outfit
                                hovered [
                                        SetScreenVariable("shown_attributes", {"stripper"}),
                                        ]
                            if shown_npc.flags.giftsexy_dress and (shown_npc.id != "reona" or shown_npc.purity < 20):
                                textbutton "Sexy date":
                                    xpos 0.10
                                    action [
                                            SetField(shown_npc, "flags.stripper_outfit", "sexydate"),
                                            SetScreenVariable("shown_attributes", {"sexydate"}),
                                            ]
                                    selected shown_npc.flags.stripper_outfit == "sexydate"
                                    hovered [
                                            SetScreenVariable("shown_attributes", {"sexydate"}),
                                            ]
                            if shown_npc.flags.giftslutty_dress and (shown_npc.id != "reona" or shown_npc.purity < 10):
                                textbutton "Slutty date":
                                    xpos 0.10
                                    action [
                                            SetField(shown_npc, "flags.stripper_outfit", "sluttydate"),
                                            SetScreenVariable("shown_attributes", {"sluttydate"}),
                                            ]
                                    selected shown_npc.flags.stripper_outfit == "sluttydate"
                                    hovered [
                                            SetScreenVariable("shown_attributes", {"sluttydate"}),
                                            ]

            vbar value YScrollValue("inventory_vp") left_bar "gui/inv/vertical_idle_bar.png" thumb "gui/inv/vertical_idle_thumb.png" right_bar "gui/inv/vertical_idle_bar.png" xmaximum 11 ymaximum 370 xalign 1.0 ypos 50 unscrollable "hide"

        fixed:
            xsize 315
            ysize 29
            imagebutton auto "gui/button_%s.png" action [SetScreenVariable("shown_attributes", {shown_npc.get_clothes()}), Function(hero.cancel_activity), Return()]
            text "Exit" color "#ffffff" font "palanquin_bold" xalign 0.5

        if config.developer:
            vbox:
                text "[shown_npc.id] [display_shown]" color "#ff0000"
                text "[submenu]" color "#ff0000"


label toggle_collar(npc, value):
    if value:
        $ npc.flags.collared = True
        $ npc.flags.previous_status = npc.status
        $ npc.status = "sex slave"
        $ npc.flags.mikeNickname = "Master"
    else:
        $ npc.flags.collared = False
        if npc.flags.previous_status:
            $ npc.status = npc.flags.previous_status
        else:
            $ npc.status = "friend"
        $ npc.flags.mikeNickname = None
    return npc.flags.collared

style appearance_button is shopping_button
style appearance_text is shopping_text
style appearance_label is shopping_label
style appearance_label_text is shopping_label_text
style appearance_items_text is shopping_items_text
style appearance_items_button is shopping_items_button:
    idle_background "gui/small_button_idle.png"
    hover_background "gui/small_button_hover.png"
    selected_background "gui/small_button_selected_idle.png"
    selected_hover_background "gui/small_button_hover.png"
    xminimum 275
    ysize 40
style appearance_items_button_text is shopping_items_button_text:
    hover_color "#ffffff"
    selected_color "#ffffff"
    xpos 0.1
style appearance_items_image_button is shopping_items_image_button
style appearance_submenu_items_button is appearance_items_button:
    idle_background "gui/small_button_idle.png"
    hover_background "gui/small_button_hover.png"
    selected_background "gui/small_button_selected_idle.png"
    selected_hover_background "gui/small_button_hover.png"
    yalign 0.5
    ysize 39
    xsize 230
style appearance_submenu_items_button_text is appearance_items_button_text:
    hover_color "#ffffff"
    selected_color "#ffffff"
    xpos 0.1
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
