init python:
    Event(**{
    "name": "reona_give_phone_number",
    "label": "give_phone_number",
    "girl": "reona",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(reona,
            Not(IsHidden()),
            IsPresent(),
            Not(ContactKnown()),
            Not(IsActivity("sleep")),
            MinStat("love", 40),
            ),
        ],
    "chances": 25,
    "do_once": True,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "reona_send_text",
    "label": "send_text",
    "priority": 100,
    "fun": 1,
    "girl": "reona",
    "conditions": [
        IsHour(13, 14),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            ),
        GameTarget(IsFlag("noTexting", False)),
        PersonTarget(reona,
            Not(IsHidden()),
            Not(IsPresent()),
            ContactKnown(),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "reona_auto_greet",
    "label": "auto_greet",
    "girl": "reona",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("None")),
        PersonTarget(reona,
            Not(IsHidden()),
            IsPresent(),
            Not(IsActivity("sleep")),
            IsFlag("greeted", False),
            MinStat("love", 50),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "reona_auto_chat",
    "label": "auto_chat",
    "girl": "reona",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(reona,
            Not(IsHidden()),
            IsPresent(),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "chances": 10,
    "do_once": False,
    "once_day": True,
    })

    Event(**{
    "name": "reona_are_you_sick",
    "label": "are_you_sick",
    "girl": "reona",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(reona,
            Not(IsHidden()),
            IsPresent(),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (reona, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "reona_ask_out",
    "label": "ask_out",
    "girl": "reona",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("ask_date"))),
        PersonTarget(reona,
            Not(IsHidden()),
            IsPresent(),
            Not(IsActivity("sleep")),
            Not(IsDatePlanned()),
            IsFlag("nodate", False),
            IsFlag("noaskout", False),
            IsFlag("schedule", "default"),
            MinStat("love", 100),
            ),
        ],
    "chances": 5,
    "do_once": False,
    "once_day": True,
    })

    Event(**{
    "name": "reona_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "reona",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(reona,
            Not(IsHidden()),
            IsPresent(),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

label reona_ask_date_male:
    if Harem.find(reona) or ("reona_jack_02b" in DONE):
        menu:
            "Ask Reona on a date":
                call reona_ask_date_alone_male from _call_reona_ask_date_alone_male
            "Set up a date with Reona and Jack" if reona.love >= 130 and "reona_jack_02b" in DONE and not "reona_jack_03b" in DONE:
                call reona_ask_date_reona_jack_03b from _call_reona_ask_date_reona_jack_03b
            "Set up a date with Reona and Jack" if reona.love >= 150 and "reona_jack_03b" in DONE and not "reona_jack_04b" in DONE and game.season == 1:
                call reona_ask_date_reona_jack_04b from _call_reona_ask_date_reona_jack_04b
            "Set up a date with Alexis and Reona" if Harem.together(alexis, reona, name="thot") and reona.love >= 200 and reona.sub >= 90 and alexis.love >= 200 and alexis.sub >= 90 and not alexis.hidden and audrey.love >= 200 and audrey.sub >= 90 and not audrey.hidden and "thot_harem_event_04" in DONE and not "thot_harem_event_05" in DONE and not hero.calendar.find(girl=reona, date_only=True) and not hero.calendar.find(girl=alexis, date_only=True) and not hero.calendar.find(girl=audrey, date_only=True):
                call reona_ask_date_thot_harem_05 from _call_reona_ask_date_thot_harem_05
            "Meet Alexis and Reona for some pool fun" if Harem.together(alexis, reona, name="thot") and game.season in [0, 1]:
                call reona_ask_date_alexis from _call_reona_ask_date_alexis
            "Meet Alexis, Audrey and Reona for a 'hot coffee'" if Harem.together(alexis, audrey, reona, name="thot"):
                call reona_ask_date_alexis_audrey from _call_reona_ask_date_alexis_audrey
            "Set up a date with Lexi and Reona" if game.season == 1 and Harem.find_by_name("whore") and "whore_harem_event_05" in DONE and not hero.calendar.find(label="whore_harem_beach_fuck_intro"):
                call reona_ask_date_lexi from _call_reona_ask_date_lexi
    else:
        call reona_ask_date_alone_male from _call_reona_ask_date_alone_male_2
    return _return

label reona_ask_date_alone_male:
    mike.say "Reona, would you like to go on a date with me?"
    if reona.flags.nodate:
        if "reona_event_09" in DONE and "reona_event_10" not in DONE:
            reona.say "[hero.name]... I can't, you know it..."
            reona.say "At least not now..."
        else:
            reona.say "I'm sorry [hero.name], I don't see you that way."
        return False
    else:
        reona.say "Sure, it might be fun, when do you want us to go?"
        return True

label reona_ask_date_reona_jack_03b:
    mike.say "You want to get together with Jack and have some fun?"
    if reona.flags.nodate:
        reona.say "I don't feel like it, sorry."
        return False
    else:
        reona.say "Sure, it might be fun, when do you want us to go?"
        mike.say "Let's meet at home."
        return DateAppointment((8, 18), "reona", "Date with Jack and Reona", "reona_jack_03b", "missed_reona_jack_03b")

label reona_ask_date_reona_jack_04b:
    mike.say "You want to get together with Jack and have some fun?"
    if reona.flags.nodate:
        reona.say "I don't feel like it, sorry."
        return False
    else:
        reona.say "Sure, it might be fun, when do you want us to go?"
        mike.say "Let's meet at the beach."
        return DateAppointment((8, 18), "reona", "Date with Jack and Reona", "reona_jack_04b", "missed_reona_jack_04b")

label reona_ask_date_thot_harem_05:
    mike.say "Hey Reona. Are you okay to spend the night with Alexis and I?"
    if reona.flags.nodate:
        reona.say "I don't feel like it, sorry."
        return False
    else:
        reona.say "Of course [hero.name]! You already have a place in mind?"
        mike.say "Yeah, let's meet at the nightclub opening."
        return HaremAppointment((22, 23), "thot", ["alexis", "reona"], "thot_harem_event_05", fail_label="missed_thot_harem_event_05")

label reona_ask_date_alexis:
    mike.say "Do you want to have some fun around the pool with Alexis?"
    reona.say "I'd love to."
    call select_date_time (fixed_season=["spring", "summer"]) from _call_select_date_time_36
    $ (day, hour, say_string) = _return
    if day == "cancel":
        return
    $ mike.say(say_string)
    if day == "now":
        call thot_harem_pool_fuck_intro from _call_thot_harem_pool_fuck_intro_1
    else:
        $ hero.calendar.add(day, HaremAppointment(hour, "thot", ["alexis", "reona"], "thot_harem_pool_fuck_intro"))
    return

label reona_ask_date_alexis_audrey:
    mike.say "Do you want to get together with Alexis and Audrey and have some fun?"
    reona.say "I'd love to."
    call select_date_time from _call_select_date_time_37
    $ (day, hour, say_string) = _return
    if day == "cancel":
        return
    $ mike.say(say_string)
    if day == "now":
        call thot_harem_foursome_intro from _call_thot_harem_foursome_intro_2
    else:
        $ hero.calendar.add(day, HaremAppointment(hour, "thot", ["alexis", "audrey",  "reona"], "thot_harem_foursome_intro"))
    return

label reona_ask_date_lexi:
    call select_date_time (fixed_hour=14, fixed_season="summer") from _call_select_date_time_24
    $ (day, hour, say_string) = _return
    if day == "cancel":
        return
    $ mike.say(say_string)
    if day != "now":
        $ hero.calendar.add(day, HaremAppointment(hour, "whore", ["lexi", "reona"], "whore_harem_beach_fuck_intro", "Date (Lexi & Reona)", "missed_whore_harem_date"))
    else:
        call whore_harem_beach_fuck_intro from _call_whore_harem_beach_fuck_intro_1
        $ game.pass_time(2)
    return

label reona_greet:
    if renpy.has_label(f"reona_greet_dialogues_{hero.gender}") and not reona.flags.greeted:
        scene expression f"bg {game.room}"
        show reona
        $ reona.flags.greeted = TemporaryFlag(True, 1)
        $ result = randint(1, 3)
        if result == 1:
            reona.say "Hello, [hero.name]."
        elif result ==2:
            reona.say "Hi, [hero.name]."
        else:
            if game.hour < 12:
                reona.say "Good morning [hero.name]."
            elif game.hour < 19:
                reona.say "Good afternoon [hero.name]."
            else:
                reona.say "Good evening [hero.name]."
        call expression f"reona_greet_dialogues_{hero.gender}" from _call_expression_465
        hide reona
    return

label reona_greet_dialogues_male:
    $ result = randint(1, 3)
    if result == 1:
        mike.say "Hello, Reona."
    elif result == 2:
        mike.say "Hi."
    else:
        if game.hour < 6:
            mike.say "Hello Reona."
        elif game.hour < 12:
            mike.say "Good morning Reona."
        elif game.hour < 19:
            mike.say "Good afternoon Reona."
        else:
            mike.say "Good evening Reona."
    return

label reona_bye(bye_outfit=None):
    call npc_bye_outfit (npc=reona, bye_outfit=bye_outfit) from _call_npc_bye_outfit_25
    $ (day, h, activity, bye_outfit) = _return
    if not activity == reona.activity:
        if day != game.week_day:
            $ reona.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ reona.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"reona {bye_outfit}")
        if activity["activity"] == "sleep":
            reona.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            reona.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            reona.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            reona.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            reona.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            reona.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            reona.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            reona.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            reona.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            reona.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            reona.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            reona.say "I'll go get dressed."
        hide reona
    return
































label reona_kiss:
    scene expression f"bg {game.room}"
    show reona
    "I've been waiting for this moment so long, it feels like forever."
    "Every time I look at Reona's lips, I feel my heart skip a beat."
    "It feels like wanting to kiss them is becoming an obsession for me!"
    show reona flirt
    "Just at that moment, she makes it a thousand times worse."
    "Because she chooses to lick her lips in a long, slow motion."
    "That's when I decide that I can't wait any longer."
    show reona surprised close
    "So I make my move, leaning in and closing my eyes..."




















    if not reona.flags.kiss:
        hide reona
        show reona kiss
        with dissolve
        $ reona.love += 5
        $ reona.flags.kiss += 1
        if reona.lesbian > MAX_LES_GUY_SEX:
            $ reona.lesbian -= 1
        "The moment that Reona's lips touch mine, it just feels right."
        "I hear her let out a yelp of surprise at the unexpected kiss."
        "But then that melts into a sigh of delight as she surrenders."
        "Reona doesn't take long to lean into the kiss either."
        "Within seconds, she's returning it with an equal amount of passion."
        "Part of me can't believe this is actually happening to me."
        "It feels like I've been waiting forever to kiss Reona."
        "And now she's as into it as I am!"
        "It's not a short thing either, the kiss going on and on."
        "As neither of is seems to be the one to break it."
        hide reona kiss
    else:
        hide reona
        show reona kiss
        $ reona.love += 2
        $ reona.flags.kiss += 1
        if reona.lesbian > MAX_LES_GUY_SEX:
            $ reona.lesbian -= 1
        "Reona jumps a little, surprised by the kiss."
        "But she doesn't pull away or try to stop me."
        "In fact she giggles and leans into it herself."
        "Pretty soon Reona is the one taking the lead too."
        "And I'm happy to let her assert herself."
        hide reona kiss
    return

label reona_sleep_date_fuck(location="hero"):


    show bg black with dissolve
    "The both of us are asleep before we can even consider cleaning up."
    call sleep ("reona") from _call_sleep_79
    $ game.room = "bedroom1"
    return







label reona_propose_male:
    if randint(0, 1) == 0:
        call reona_proposal_male_02 from _call_reona_proposal_male_02
        return
    show reona
    "I don't know if I'm being rash because I haven't known Reona long enough."
    "Or rational because I feel like I know exactly what I want for the first time."
    "But I know that I have to do something about it, something dramatic too."
    "And that's why there's a ring in my pocket, which feels like a lead weight!"
    "Part of me wants to forget the whole thing out of fear of rejection."
    "But another part of me desperately needs the release of an answer, no matter what it is."
    "Luckily for me, Reona doesn't seem to have noticed the state I'm in."
    "She's more interested in recounting the latest bit of gossip to me."
    reona.say "And you know what he said then?"
    reona.say "I'll tell you what he said..."
    reona.say "He said I was self-absorbed!"
    reona.say "Can you believe that?!?"
    show reona annoyed
    reona.say "[hero.name]..."
    reona.say "What are you doing down there?"
    "I force a smile onto my face as I hold up the ring."
    mike.say "Reona..."
    mike.say "I love you..."
    mike.say "And I have to know..."
    show reona surprised
    mike.say "Will you marry me?"
    "I watch Reona's eyes go wide as realisation dawns upon her."
    "But all I can do now is wait for an answer..."
    if reona.love >= 195 and hero.sexperience >= 110:
        "Reona's expression only becomes more confused as she stares at the ring."
        "It's almost like she can't believe what's happening right before her eyes."
        reona.say "You..."
        "She points a finger at me."
        show reona blush
        reona.say "Want to marry me?"
        "Now the she's pointing the finger at herself."
        mike.say "That's about the size of it, Reona."
        mike.say "So what do you say?"
        "Reona shakes her head and seems to snap back to reality."
        "Almost like she'd forgotten the actual question."
        show reona normal
        reona.say "Oh..."
        show reona happy
        reona.say "Oh yeah!"
        reona.say "Yes..."
        reona.say "Yes, I'll marry you!"
        "I almost leap up and begin to push the ring onto her finger."
        "Reona smiles as she watches my progress."
        mike.say "Oh, man..."
        mike.say "I was so nervous asking you the question, Reona!"
        show reona -blush
        reona.say "Well you can stop worrying now, can't you!"
        "I nod happily, wondering if I'll ever come down from this emotional high."
        $ reona.set_fiance()
        hide reona
    else:
        "Reona's expression goes from surprised to annoyed right before my eyes."
        "She crossed her arms over her chest and looks anything but pleased."
        show reona annoyed
        reona.say "Oh, [hero.name]..."
        reona.say "You're always thinking about yourself!"
        reona.say "What about me?"
        reona.say "What about what I want?"
        "Now it's my turn to look surprised."
        "My worst fear was for Reona to say no."
        "But I wasn't prepared for her to turn it around on me like this."
        "Somehow she's making it sound like me proposing was totally selfish!"
        mike.say "No, Reona..."
        mike.say "It's not like that at all!"
        mike.say "I like you...I mean, I LOVE you!"
        mike.say "That's why I want to marry you!"
        $ reona.love -= 25
        $ reona.sub -= 25
        reona.say "Like I said..."
        reona.say "It's all about you!"
        "With that, Reona stamps her foot."
        hide reona
        "Then she turns on her heel and storms off."
        "Which leaves me standing there, the ring still in my hand."
        "And a sense of confusion keeping me rooted to the spot."
    return

label reona_proposal_male_02:
    show reona
    "I feel like things have only gotten better for Reona and me since we got everything out in the open."
    "Now I understand the sequence of events that was responsible for making her the sexual being she is."
    "And on top of that, her confession helped me to come to terms with my own feelings towards her."
    "Everything seems to have been brought out into the open and made sense of, much to our benefit."
    "But I still can't escape the feeling that there's something more I need to do."
    "One more thing that will finally line everything up and make sure it clicks."
    "For a short while it seems to elude me, and I can't put a finger on what it is."
    "That is until I happen to walk by the window of a jeweller's shop."
    "And there I see row upon row of bright, shiny rings, all trying to catch my eye."
    "Now I know what I need to do in order to make things permanent between Reona and I."
    "So with one of those same rings stashed in my pocket, I start making plans to pop the question."
    show reona at center, zoomAt(1.5, (640, 1040)) with fade
    "Of course I do the very best I can to play it cool when I next meet up with Reona."
    "Even though the ring feels like a brick in my pocket, I want this to be a surprise."
    show reona pensive
    reona.say "What's wrong with you, huh?"
    show reona normal
    "Ah shit..."
    "Am I really that transparent?"
    mike.say "Huh?"
    mike.say "What are you talking about, Reona?"
    mike.say "There's nothing wrong with me, nothing at all."
    mike.say "I'm totally normal, one hundred percent normal, even!"
    show reona annoyed
    reona.say "Yeah..."
    reona.say "Because that's how you'd normally respond to a simple question!"
    show reona devious
    "I can see my plans crumbling right before my eyes."
    "And the worst thing is that it's going to be my own fault!"
    "So as I see it, I basically have two choices."
    "I can abort the whole thing, retreat and regroup."
    "Or I can throw caution to the wind and just go for it."
    "And I bet you can guess which one I'm going to choose, right?"
    "Without waiting for Reona to say another word, I reach into my pocket."
    "Then I whip out the ring."
    "What, you didn't think I was going to choose the sensible option, did you?"
    "At the same time I begin to get down on one knee, right in front of Reona."
    show reona shock at startle
    reona.say "[hero.name]…"
    reona.say "What are you..."
    reona.say "Oh my god..."
    reona.say "Are you..."
    reona.say "You are, aren't you?!?"
    "I do the best I can to ignore the fact that Reona sounds like she's starting to babble."
    "And instead I clear my throat as I pop open the box with the ring inside of it."
    "Then I look up, doing the best I can to put a serene yet confident smile on my face."
    mike.say "Ahem..."
    mike.say "Reona, you already know that I love you."
    mike.say "But I need to know - will you make me the happiest man in the world?"
    mike.say "Will you marry me?"
    if reona.love < 195 and hero.sexperience < 110:

        show reona sadshock
        "As soon as she sees the ring, Reona starts backing off."
        "She's shaking her head as she does so, almost like she's afraid of it!"
        "So I get to my feet again, putting the ring away in an attempt to calm her down."
        mike.say "Reona..."
        mike.say "What's wrong?"
        "Reona's still shaking her head right now."
        "But at least she seems to have stopped backing away."
        reona.say "Too fast, [hero.name]…"
        reona.say "This is all going too fast for me!"
        "I take one last look at the ring."
        "Then I shove it hastily into my pocket."
        mike.say "So..."
        mike.say "You don't want to marry me?"
        show reona sadsmile
        "Reona shakes her head at this."
        "But I can see from the look on her face that she's not being malicious."
        reona.say "I don't know, [hero.name]."
        reona.say "All I know is that I don't want to do it now!"
        mike.say "You mean you might want to some time in the future?"
        mike.say "Because that's good enough for me!"
        "Now that the ring's disappeared, Reona seems to have calmed down."
        "She nods her head, and I feel a surge of relief run through my entire body."
        "Because that really is better than being told she'll never want to marry me!"
        $ reona.love -= 25
        $ reona.sub -= 25
    else:

        "As soon as she sees the ring, Reona starts nodding."
        "And she can't help reaching out to touch the ring."
        "Almost as if she won't believe it's real until she touches it."
        show reona happy
        reona.say "Of course I will!"
        reona.say "So?"
        reona.say "What are you waiting for?!?"
        "I realise that I've been standing still, staring at Reona this whole time."
        "The fact she just said yes is only now beginning to sink in."
        "And I hurry to do as she asks."
        hide reona
        show dick reactions reona smile nodick
        with vpunch
        "As soon as the ring is on her finger, Reona throws her arms around my neck."
        reona.say "So this is what was up with you?"
        mike.say "Yeah, Reona..."
        mike.say "I guess so!"
        reona.say "And here I was expecting a nasty surprise."
        reona.say "But this is the best thing that ever happened to me!"
        "I have to say that I feel the same way as Reona does right now."
        "Sure, the proposal wasn't a surprise for me."
        "But I was terrified that she might not say yes."
        "So maybe what I'm feeling is more a sense of relief!"
        "Now all I have to worry about is arranging a wedding."
        "Which, after all this messing about, should be easy, right?"
        $ reona.set_fiance()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
