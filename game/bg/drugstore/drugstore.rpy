init python:
    Consumable("condom", price=10, tooltip="A single-use contraceptive", inventory_usable=False)
    Consumable("box_of_condoms", price=100, tooltip="A pack of condoms for ongoing protection", label="box_of_condoms")
    Consumable("pierced_condom", price=0, tooltip="A single-use defective contraceptive", inventory_usable=False)
    Consumable("box_of_pierced_condoms", price=0, tooltip="A pack of pierced condoms for nonexistent protection", label="box_of_pierced_condoms")
    Consumable("medicine", price=50, tooltip="General-purpose medicine", label="cured")
    Consumable("lotion", display_name="Sunscreen lotion", price=50, tooltip="Lotion for sun protection", uses=4)
    Consumable("bigger_staff_pill", display_name="Bigger Staff Pill", price=5000, tooltip="Enhancement pill for penis enlargement", label="enhance_penis")
    Consumable("smaller_staff_pill", display_name="Smaller Staff Pill", price=5000, tooltip="Reduction pill for penis size", label="diminish_penis")
    Consumable("blue_pill", price=200, tooltip="A pill used to treat erectile dysfunction", label="blue_pill")
    Consumable("pink_pill", price=200, tooltip="A pill used to treat sexual dysfunction", label="pink_pill")
    Consumable("contraceptive_pill", display_name="Contraceptive pill", price=100, tooltip="A pill to prevent pregnancy", label="contraceptive_pill")
    Item("pregnancy_test", display_name="Pregnancy test", price=100, tooltip="A test to detect pregnancy")
    Item("dna_test", display_name="DNA test", price=500, tooltip="A test to analyze DNA")
    Gift("bigger_staff_pill_gift", display_name="Bigger Staff Pill", price=5000, tooltip="A gift of enhancement for penis enlargement", label="mike_bigger_staff_pill_gift_female")
    Gift("smaller_staff_pill_gift", display_name="Smaller Staff Pill", price=5000, tooltip="A gift of reduction for penis size", label="mike_smaller_staff_pill_gift_female")

    Room(**{
    "name": "drugstore",
    "exits": ["mall2","flowershop","coffeeshop","electronic", "jewelrystore", "mallmap"],
    "display_name": "Drug Store",
    "hours": (9, 18),
    "conditions": [
        IsHour(9, 18),
        ],
    "music": season_music(),
    "random_music": True,
    "outfit": "casual",
    "tags": ["mall_southside", "mall_northside"],
    "inventory": (
        "condom",
        "box_of_condoms",
        "medicine",
        "lotion",
        {"id": "bigger_staff_pill", "conditions": ("not hero.is_female", "not hero.has_skill('hung')")},
        {"id": "smaller_staff_pill", "conditions": ("not hero.is_female", "not hero.has_skill('smalldick')")},
        {"id": "blue_pill", "conditions": ("hero.is_male",)},
        {"id": "pink_pill", "conditions": ("hero.is_female",)},
        {"id": "contraceptive_pill", "conditions": ("hero.is_female",)},
        {"id": "pregnancy_test", "conditions": ("hero.is_female",)},
        {"id": "dna_test", "conditions": ("hero.is_female",)},
        {"id": "bigger_staff_pill_gift", "conditions": ("hero.is_female", "hero.morality <= -50", "mike.sexperience >= 1")},
        {"id": "smaller_staff_pill_gift", "conditions": ("hero.is_female", "mike.sexperience >= 1")},
        ),
    })

    Activity(**{
    "name": "drugstore_shop",
    "duration": 0,
    "display_name": "Shop",
    "icon": "shop",
    "rooms": "drugstore",
    "label": "drugstore_shop",
    })

    Event(**{
    "name": "heart_attack",
    "label": "heart_attack",
    "duration": 1,
    "priority": 500,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsRoom("map")
            ),
        "randint(1, 100) <= hero.flags.bluepills -25"
        ],
    "do_once": True
    })

label drugstore_shop:
    $ Room.find("drugstore").shop("gwen teaser")
    return

label box_of_condoms:
    $ hero.gain_item("condom", 10)
    return

label box_of_pierced_condoms:
    $ hero.gain_item("pierced_condom", 10)
    return

label blue_pill:
label pink_pill:
    python:
        hero.flags.last_sex = 0
        if hero.flags.bluepills <= 1:
            hero.flags.bluepills += 2
        else:
            hero.flags.bluepills = hero.flags.bluepills * 2
    return

label contraceptive_pill:
    $ hero.flags.pill = TemporaryFlag(True, 7)
    return

label heart_attack:
    show bg street
    if not game.flags.cheat:
        if renpy.has_label("mike_achievement_0") and (game.days_played == 0 or (game.days_played == 1 and game.hour <= 10)):
            call mike_achievement_0 from _call_mike_achievement_0_2
        if renpy.has_label("bluepill_achievement_1"):
            call bluepill_achievement_1 from _call_bluepill_achievement_1
    "I'm walking down the street today in a rare state of almost complete happiness."
    "Sure, there are things that could be going better for me right now."
    "But isn't that always going to be the case?"
    "Instead of thinking about negative stuff like that, I'm dwelling on the positives."
    "Like the fact that I'm seriously killing it in the bedroom."
    "I mean I'm really knocking the ladies dead with my performance between the sheets!"
    "And it's all because of one little blue pill."
    "Yeah, yeah - I know what you're thinking."
    "That stuff's supposed to be just for old men with limp dicks."
    "But why settle for being average when you can be so much more than that?"
    "And you should see the size of the smile it puts on my face."
    "It's almost as large as the one's I've been leaving on the faces of the girls I'm doing!"
    "My smile fades for a moment and my step falters as I feel a twinge in my chest." with hpunch
    "It's nothing really, just a twitch that leaves me a little shaken."
    "I put it down to being just one of those things."
    "And I stride on down the street, trying to put it out of my mind."
    "But the next twinge comes a few seconds later." with hpunch
    "And this one's much worse, impossible to ignore."

    show heart attack with hpunch
    "My hand clutches at my chest as another one hits, then another." with hpunch
    "There's a tingling sensation in my hands, and my head is getting light."
    "Then my knee's buckle under me, and I fall onto the ground."
    "I can't move, my heart feeling like it's going to explode in my chest."
    hide heart attack
    show heart attack at zoomAt (1.25, (-170, 0))
    show layer master at blur(4)
    "My vision's getting blurry, going dark around the edges too."
    "People seem to be looking down at me from above."
    "But those could be spots clouding my eyes."
    show layer master at blur(8)
    "I don't know if the muffled sounds I can hear are the voices of those people." with dissolve
    "Or they could be the distant sounds of an ambulance siren."
    show layer master at blur(16), dark
    "All I know for sure is that everything's fading to black." with dissolve
    "There's nothing I can do to stop it."
    scene bg black
    "And now there's only black..." with dissolve
    $ renpy.full_restart()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
