init python:
    Event(**{
    "name": "home_harem_beach_date_set_up",
    "label": "home_harem_beach_date_set_up",
    "priority": 0,
    "conditions": [
        IsActiveHarem('home'),
        IsSeason(1),
        Or(
            IsHour(9, 14),
            And(
                "game.calendar.get_future_season(game.days_played + 1) == 'summer'",
                IsHour(15, 23),
                ),
            ),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home")),
        HasVehicle(motor=True),
        ],
    "do_once": False,
    "once_day": True,
    "block_when_canceled": False,
    "quit": False,
    })

label home_harem_beach_date_set_up:
    $ beach_choices = list()
    python:
        hh_members_at_home = Harem.find_by_name("home").active_members_in_room_tag("home")
        hh_members_at_home = [i for i in hh_members_at_home if Person.find(i).activity["activity"] != "sleep" and Person.is_not_hidden(i)]
        hh_combinations = list(reversed(list(itertools.chain.from_iterable(itertools.combinations(hh_members_at_home, r) for r in range(2, len(hh_members_at_home) + 1)))))
        hh_combinations_labels = {"home_harem_" + "_".join(comb) + "_beach_date": comb for comb in hh_combinations}
        implemented_beach_dates = {k: v for k,v in hh_combinations_labels.items() if renpy.has_label(k) and not (Conditioned.done_this_week(k) or hero.calendar.find(label=k))}
        if implemented_beach_dates:
            beach_choices.extend([("Go to the beach with " + ", ".join([i.capitalize() for i in beach_date_members[:-1]]) + " and " + beach_date_members[-1].capitalize() , (beach_date_id, beach_date_members)) for beach_date_id, beach_date_members in implemented_beach_dates.items()])
            beach_choices.append(("Cancel", "canceled"))
    if beach_choices:
        $ narrator("Should I set up a date at the beach ?", interact=False)
        $ beach_choice = renpy.display_menu(beach_choices)
        if beach_choice == "canceled":
            "Maybe later."
            $ hero.cancel_event()
            python:
                for beach_label in implemented_beach_dates.keys():
                    DONE[beach_label] = game.days_played
            return
        $ (beach_label, beach_members) = beach_choice
        if len(beach_members) == 5:
            show expression beach_members[0] at mostleft5
            show expression beach_members[1] at left5
            show expression beach_members[2] at mostright5
            show expression beach_members[3] at right5
            show expression beach_members[4]
        elif len(beach_members) == 4:
            show expression beach_members[0] at mostleft4
            show expression beach_members[1] at left4
            show expression beach_members[2] at mostright4
            show expression beach_members[3] at right4
        elif len(beach_members) == 3:
            show expression beach_members[0] at left
            show expression beach_members[1]
            show expression beach_members[2] at right
        elif len(beach_members) == 2:
            show expression beach_members[0] at left
            show expression beach_members[1] at right
        if 'sasha' in beach_members:
            sasha.say "You're taking us to the beach."
        else:
            $ renpy.say(renpy.random.choice(beach_members), "You're taking us to the beach.")
        menu:
            "Yes":
                mike.say "Wow...okay!"
                call select_date_time (fixed_hour=14, fixed_season="summer", add_cancel=False) from _call_select_date_time_13
                $ (day, hour, say_string) = _return
                if day != "now":
                    $ mike.say(say_string)
                    $ hero.calendar.add(day, HaremAppointment(hour, "home", beach_members, beach_label, name=f"Beach Date ({', '.join([i.capitalize() for i in beach_members])})"))
                    if 'bree' in beach_members:
                        bree.say "This is gonna be so fun!"
                    else:
                        $ renpy.say(renpy.random.choice(beach_members), "This is gonna be so fun")
                else:
                    call expression beach_label pass (HaremAppointment(game.hour, "home", beach_members, beach_label, name=f"Beach Date ({', '.join([i.capitalize() for i in beach_members])})")) from _call_expression_511
            "No":
                python:
                    for g in beach_members:
                        Person.find(g).love -= 10
                $ DONE[beach_label] = game.days_played
                $ hero.cancel_event()
    else:
        $ hero.cancel_event()
    return

label home_harem_bree_sasha_beach_date(appointment=None):
    if not hero.has_motor_vehicle:
        mike.say "Sorry girls, my car is in the garage."
        mike.say "We'll have to postpone our trip to the beach."
        $ bree.love -= 2
        $ sasha.love -= 2
        return
    "It's the first time that the weather's been this good for what feels like weeks, the sun blazing in a clear, blue sky."
    "And there's only one thought on the minds of [bree.name], Sasha and myself - we HAVE to hit the beach and take full advantage!"
    "So we gather all of the stuff that we're going to need and pile into my car as soon as all three of us are ready."
    show bg beach with fade
    "We make it to the beach in good time, beating the first rush of people to there and ensuring that we can pick a good spot."
    "But first, we have to park the car and unload all of our things."
    show bree swimsuit at right5 with moveinright
    bree.say "I'll grab the cooler!"
    show sasha swimsuit at top_mostright with moveinright
    sasha.say "Okay, I'll get the parasol and the towels."
    "I watch as [bree.name] manhandles the cooler that we packed with drinks and snacks."
    show bree annoyed at startle
    "She struggles to haul it out of the boot of the car, almost dropping it onto the ground."
    "My natural instinct is to leap in and relieve her of what's obviously too heavy of a burden."
    show sasha annoyed
    "But then my gaze falls on Sasha, who's also having a hard time managing all of the towels and the parasol."
    "While they're lighter than the cooler, she looks like she'd need another pair of arms to handle them."
    "Save for what the girls are trying to manage, there's not really anything left for me to carry."
    "So the obvious thing would be to step in and relieve someone of their burden."
    "The only problem is that I can't do that for both of them - so I have to choose who gets my help!"
    $ beach_event = 0
    menu:
        "Choose to help [bree.name]":
            hide sasha with dissolve
            show bree swimsuit
            "I figure that the best thing to do would be to take care of the cooler."
            "That way [bree.name] and Sasha can divide the towels and the parasol between them."
            mike.say "Hey, [bree.name]."
            mike.say "That's way too heavy for you."
            mike.say "Let me handle it instead."
            $ bree.love += 2
            bree.say "Oh, are you sure, [hero.name]?"
            show bree swimsuit normal
            "I can tell from the look on [bree.name]'s face that she's only asking out of politeness."
            "And she proves me right by handing the cooler over without any further protests."
            "As soon as I have hold of the thing, I'm amazed she could lift it at all."
            "I'm not saying [bree.name]'s a weakling, but I feel myself struggling with it too!"
            mike.say "No...problem...[bree.name]!"
            "I begin to stagger off towards the sand."
            "Each and every step has me praying that I make it before my arms give out."
            show sasha swimsuit annoyed at top_mostright with dissolve
            show bree swimsuit happy at left
            show sasha swimsuit at right
            with move
            "But this also means that I can't look back to see what [bree.name] and Sasha are doing."
            "When I finally make it to a decent spot and drop the thing, I turn around to check."
            "And my heart sinks to see [bree.name] walking close behind, her arms empty of any burden."
            "She looks positively delighted with my chivalrous behaviour."
            "Which is more than can be said for Sasha."
            $ sasha.love -= 2
            "Who slowly comes into view, dragging her own burden behind her through the sand."
        "Choose to help Sasha":
            hide bree with dissolve
            show sasha swimsuit
            "I think about taking the cooler from [bree.name], just to speed things up."
            "But then it hits me that it'd be pretty insulting to think she can't handle it."
            "And I'm a very modern guy when it comes to things like that, so I decide to leave her to it."
            mike.say "Hey, Sasha."
            mike.say "Let me take some of that stuff."
            show sasha normal
            sasha.say "Are you sure, [hero.name]?"
            sasha.say "That cooler looks pretty heavy!"
            mike.say "[bree.name] can handle it - she sure works out enough!"
            $ sasha.love += 2
            "Sasha shrugs at this, and then proceeds to hand over about half of what she was carrying."
            "This means that she can handle it better than before, and I'm not overburdened either."
            show sasha happy at center with move
            "So we stroll onto the sand together, chatting and looking out for a decent spot."
            "In fact, we're having such a nice time of it that we totally forget about [bree.name]."
            mike.say "Erm, Sasha..."
            show sasha normal
            sasha.say "Yeah, [hero.name]?"
            mike.say "Where's [bree.name] gotten to?"
            "We both drop what we're carrying and begin to turn around on the spot."
            show sasha swimsuit at left4 with move
            "But it doesn't take long to spot the missing member of our threesome."
            show bree swimsuit annoyed at top_mostright with dissolve
            "[bree.name] comes slowly into view over the dunes behind us."
            show bree swimsuit lose at right with move
            "By now she looks exhausted and has given up all hope of carrying the cooler."
            "Instead she drags it behind her, making a deep channel in the sand."
    hide bree
    hide sasha
    with dissolve
    "Once enough irritated glares and passive aggressive comments have passed between us, we get down to marking our territory."
    "With the towels spread out on the sand and the parasol up, all that remains is to actually lie down and relax."
    "As we just got here, no one wants to go running off to do anything physical just yet."
    "And some of us are pretty tired from carrying the stuff here, so we just kick back and close our eyes for a while."
    show bg black with wipedown
    pause 0.5
    show bg beach with wipeup
    "I must have fallen asleep at some point, because the next thing I know I'm waking up to the sound of voices."
    "Groggily propping myself up on one elbow, I see [bree.name] and Sasha engaged in a heated discussion over the cooler."
    show bree swimsuit annoyed at left5
    show sasha swimsuit annoyed at right5
    with dissolve
    bree.say "Look, [hero.name]'s awake now."
    sasha.say "Well you probably did it with your yelling!"
    show bree angry at startle
    bree.say "What the..."
    show bree annoyed
    bree.say "More like he got a whiff of your packed lunch!"
    sasha.say "Whatever, [bree.name] - let's have him settle this for us."
    "Part of me is intrigued to see just what the girls are squabbling about."
    "But another wishes I could pretend to be asleep and let them settle it for themselves."
    mike.say "Ah...what's up?"
    show bree normal
    bree.say "I made sandwiches for lunch, like I said I would."
    show sasha normal
    sasha.say "And I made wraps, because she didn't tell me she said so."
    "I shrug at this, expecting them to tell me more, but nothing is forthcoming."
    mike.say "And the problem with that is...what, exactly?"
    show bree happy
    bree.say "I made baloney sandwiches, because that's your favourite."
    show sasha happy
    sasha.say "No it isn't, [bree.name] - his favourite is a chicken wrap."
    sasha.say "And that's what I made!"
    show bree normal
    show sasha normal
    "Suddenly I find one of each thrust into my face by their respective champions."
    "And although it's getting close to lunchtime, I wasn't anticipating it turning into a pitched battle!"
    "For all I know, I may have said they were both my favourites at different times."
    "I just never thought it'd come back to bite me in the ass like this!"
    menu:
        "Choose [bree.name]'s sandwich":
            "Sasha's chicken wrap does look pretty good from where I'm sitting."
            "But then I see that there's mustard dripping out of the baloney sandwich in [bree.name]'s hand."
            "I might live to regret this, but that tips the scales for me."
            mike.say "Wow..."
            mike.say "They both look really good."
            mike.say "But I think I fancy the sandwich today."
            show bree happy
            show sasha sad
            "I take the sandwich that [bree.name] offers me, trying to shrug an apology to Sasha at the same time."
            "But the inevitable result is that the girl I favoured beams with the victory."
            show sasha at right with move
            $ bree.love += 2
            $ sasha.love -= 2
            "And the one that I turned down mutters under her breath as she turns away."
        "Choose Sasha's wrap":
            "[bree.name]'s baloney sandwich does look pretty good from where I'm sitting."
            "But then I see that there's mayonnaise dripping out of the chicken wrap in Sasha's hand."
            "I might live to regret this, but that tips the scales for me."
            mike.say "Wow..."
            mike.say "They both look really good."
            mike.say "But I think I fancy the wrap today."
            show bree cry
            show sasha happy
            $ bree.love -= 2
            $ sasha.love += 2
            "I take the wrap that Sasha offers me, trying to shrug an apology to [bree.name] at the same time."
            "But the inevitable result is that the girl I favoured beams with the victory."
            show bree at left with move
            "And the one that I turned down mutters under her breath as she turns away."
    show bree normal
    show sasha normal
    "As I polish off the last few bites of my chosen lunch, I can feel an atmosphere settling over us."
    "And I can tell that there's going to be at least one person spending the rest of the day pissed off."
    "So as soon as I feel like what I've eaten has had a chance to settle, I get up and gesture for the others to do likewise."
    mike.say "Come on, you guys."
    mike.say "We've been sitting on our asses for long enough."
    mike.say "Let's go and get wet!"
    show bree happy
    show sasha happy
    "This suggestion seems to have the desires effect, as both girls nod eagerly."
    "[bree.name] springs to her feet first, snatching up the beach-ball that we brought along."
    bree.say "Last one in the water carries the cooler back!"
    hide bree with moveoutleft
    "And with that, she's off, running towards the water."
    show sasha angry
    sasha.say "Hey - no fair!"
    show sasha normal
    "She leaps to her feet too, throwing sand this way and that in her haste."
    "It's then that Sasha casts a sideways glance at me, her eyes narrowing at the same time."
    "I realise a little too late that the race for second place is now between the two of us."
    show sasha joke
    sasha.say "See yah later, loser!"
    hide sasha with moveoutleft
    "Sasha dashes off after [bree.name], leaving me to shake off my surprise and follow."
    show bg beach at center, zoomAt(2.25, (1440, 1275)) with dissolve
    "She makes it to the water perhaps a second or two before me, punching the air in victory."
    with vpunch
    "And I manage to make her triumph complete by tripping, so that I fall face-first into the breaking waves."
    show bree happy swimsuit at center, zoomAt(1.25, (340, 940))
    show sasha happy swimsuit at center, zoomAt(1.25, (940, 940))
    with dissolve
    "[bree.name] and Sasha give each other a high-five as I struggle to my feet."
    bree.say "Bad luck, [hero.name]!"
    sasha.say "Yeah - you might wanna conserve your energy for lugging all of that heavy shit!"
    mike.say "Ha, ha...very funny, guys."
    mike.say "Tell you what - how about we go double or quits?"
    mike.say "We play keep-up with the ball, yeah?"
    mike.say "One of you drops it in the sea, she has to help me carry our stuff."
    mike.say "I drop it, and I'll do it myself."
    show bree normal
    show sasha normal
    "Sasha frowns at this, and [bree.name] cocks her head on one side, looking puzzled."
    bree.say "But, didn't you already have to do that anyway?"
    sasha.say "Yeah, [hero.name] - sweeten the deal, or we're not biting!"
    mike.say "Okay, okay, let me think for a second..."
    "It's then that my gaze falls on the kiosk up the beach, selling all manner of refreshments."
    mike.say "Okay, I got it."
    mike.say "If I lose, I buy everyone an ice-cream, yeah?"
    show bree happy
    bree.say "Ooh, that sounds good!"
    sasha.say "Yeah, but we have to be able to choose what WE want."
    sasha.say "No getting cheap on us!"
    mike.say "Okay, whatever you want."
    show bree normal
    "A round of nodding and shaking of hands seals the deal, and we get down to playing the game."
    "Going two against one might put me at a disadvantage, if either of them were serious athletes."
    "But then I'm not that concerned about who wins or loses this little encounter."
    "After all, what's the price of a couple of ice-creams and lugging stuff to the car?"

    "Especially when the immediate pay-off is to join [bree.name] and Sasha as they splash around in their swim-suits?"
    "The game is nothing to write home about, but the sight of the girls leaping to and fro is something else entirely."
    "And while I said I wasn't worried about losing, I do all that I can to prolong the whole affair."
    show sasha surprised at center, zoomAt(1.0, (940, 940)), startle
    "But my plans are ruined when Sasha suddenly lets out an ear-piercing scream."
    show sasha cry
    "A second later, she starts hopping around in pain, letting the ball pass her by and hit the water."
    show bree sad
    bree.say "Aw, Sasha - you dropped the ball!"
    sasha.say "Oww...shit..."
    sasha.say "It hurts!"
    "As I wade over to her, trying to see what the problem is, Sasha turns towards me."
    "She waves her foot in my vague direction, and it's only now that I see what's hanging off of her big toe."
    mike.say "Hey, Sasha - you've got a crab hanging off your toe!"
    show sasha vangry
    sasha.say "Of course I do, genius!"
    show sasha at center, zoomAt(1.0, (940, 940)), startle
    sasha.say "You maybe wanna think about, I don't know - GETTING IT OFF!"
    menu:
        "Tackle the crab yourself":
            show sasha cry
            "Sasha's frantic demands are more than enough to spur me into action."
            "I leap forwards and grab the offending crustacean with both hands."
            "It makes a valiant show of trying to nip me too."
            "And it gets some pretty good shots in on my fingers before it's all over."
            "But it only has two pincers to oppose my ten digits, and it soon loses the battle."
            show sasha normal
            "Even when it's off of her toe and Sasha's safe, I don't simply toss the crab aside."
            "Instead I carry it onto the beach and deposit the creature into a nearby rock-pool."
            "And as I walk back towards the girls, I can see that this act in of itself has scored me some serious points."
            sasha.say "Oh, thanks for that, [hero.name]."
            sasha.say "It hurt SO much!"
            $ sasha.love += 2
            show bree happy
            bree.say "And you took care of the poor little thing too!"
            show bree normal
            bree.say "Sure, crabs really freak me out."
            bree.say "But you were so gentle with it!"
            $ bree.love += 3
        "Make [bree.name] tackle the crab":
            bree.say "Eww..."
            bree.say "Help her, [hero.name], quick!"
            bree.say "Urgh - I HATE crabs!"
            "I make a move to obey."
            "But then a cruel, but amusing idea pops into my head."
            mike.say "Ah...shit!"
            bree.say "Wha...what's the matter?!?"
            mike.say "I...I think I've got a cramp...in my leg!"
            mike.say "[bree.name], you'll have to help Sasha out - and quickly too!"
            show bree cry at center, zoomAt(1.0, (340, 940)), startle
            $ bree.love -= 6
            "[bree.name] shudders at the mere suggestion, shaking her head desperately."
            bree.say "I...no...I can't..."
            sasha.say "For fuck's sake, [bree.name]!"
            show sasha at center, zoomAt(1.0, (940, 940)), startle
            sasha.say "HELP ME!"
            $ bree.sub += 2
            "Sasha's cry pushes [bree.name] into action, and she rushes forwards."
            "But at the same time, she tries to avert her eyes and most of her body too."
            "What follows is a farcical scene, as Sasha waves her foot and [bree.name] tries to grab it without looking."
            "Eventually, [bree.name] gets lucky and catches hold of the crab."
            "With no regard for Sasha's comfort, she rips the crustacean free and tosses it aside."
            "The unfortunate crab goes sailing for a good distance before it disappears beneath the waves."
    show bree sad
    show sasha sad
    "With the crisis averted, all I can hear are sighs and moans coming from the girls."
    "I bite my tongue and resist the temptation to say that they're making something out of nothing."
    "And instead I decide that, under the circumstances, I can't accept such a tainted victory."
    mike.say "Would those ice-creams that I promised help you get over it?"
    "At the mere mention of ice-cream, both [bree.name] and Sasha seem to forget their respective woes."
    show bree happy
    show sasha happy
    bree.say "Ooh, are you serious?"
    sasha.say "Yeah, what gives?"
    sasha.say "Didn't you win the game?"
    "I make a point of shrugging as I turn to walk towards the kiosk."
    mike.say "Never mind that."
    mike.say "The crab kind of ruined that anyway, so let's just forget about it."
    scene bg beach
    show beach icecream sasha nomc
    with fade
    "At the kiosk, I take everyone's orders and then hand out the ice-creams as they're ready."
    "We all seem to have gone for cones, topped with scoops of ice-cream and toppings."
    show beach icecream bree nomc
    with fade
    "But [bree.name]'s is taller than the rest, and she's already struggling with it as we walk away."
    "I watch as she tries in vain to balance the precarious tower as it threatens to topple over."
    "And her efforts to use strategic licks don't seem to be having the desired effect either."
    "By the time we make it back to our spot, Sasha's watching the show too."
    mike.say "Erm, [bree.name]..."
    mike.say "Do you need a hand with that?"
    bree.say "Huh?!?"
    "The question distracts [bree.name] from her task long enough to ensure failure."
    "And I watch in helpless silence as the uppermost scoop of ice-cream topples off of the pile."
    bree.say "Aaah..."
    bree.say "Shit - that's fricking freezing!"
    "I hear what [bree.name]'s saying, but my eyes are fixed on the ice-cream."
    "All I can do is watch as it begins to slide down her chest and between her breasts..."
    menu:
        "Lick the ice-cream off of [bree.name]'s chest":
            "I don't know what makes me do it, or even think that it's what [bree.name] actually wants."
            show beach icecream bree nomc at center, zoomAt(2.0, (620, 1140)) with dissolve
            "But I find myself leaning in without a moment of hesitation and opening my mouth."
            "Most of the solid ice-cream has already run down [bree.name]'s chest and fallen onto the sand below."
            "So I busy myself with the task of licking away at the trail that it's left."
            scene bg beach
            show bree surprised blush b swimsuit at center, zoomAt(2.0, (640, 1140))
            with dissolve
            bree.say "Ooh, [hero.name]!"
            bree.say "What are you..."
            "It's not an objection, more an expression of surprise."
            "And as I actually begin to lick her chest clean, it melts like the ice-cream itself."
            $ bree.love += 4
            bree.say "Oh, [hero.name]..."
            "I can taste the flavours of the ice-cream at first."
            "But then it becomes mixed with the tang of [bree.name]'s sun-cream and perspiration."
            "Even when I seem to have taken care of the ice-cream, I still don't stop."
            "My tongue goes on, tracing the outline of [bree.name]'s breast and threatening to go further..."
            show bree flirt blush b swimsuit
            bree.say "Ah..."
            bree.say "I...I think that's got it all!"
            "Although I'd very much like to keep right on going, I can take a hint."
            "So I pull my tongue back into my mouth and lean back again."
            $ bree.sub += 10
        "Make Sasha lick the ice-cream off of [bree.name]'s chest":
            "I think about doing something myself, even starting to lean forwards."
            show beach icecream bree nomc at center, zoomAt(2.0, (620, 1140)) with dissolve
            "But then a far more intriguing possibility occurs to me, and I stop in my tracks."
            mike.say "Sasha..."
            mike.say "Why don't you help [bree.name] out?"
            scene bg beach
            show sasha swimsuit surprised
            with fade
            "Sasha looks at me for a second, clearly not sure just what I mean."
            "So I smile, and then lick my lips in a suggestive manner."
            show sasha blush
            $ sasha.sub += 4
            "She looks surprised, then nervous, but nods all the same."
            scene bg beach
            show bree surprised blush b swimsuit zorder 1 at center, zoomAt(2.0, (640, 1140))
            show sasha joke b swimsuit zorder 2 at center, zoomAt(2.0, (860, 1460))
            with dissolve
            "It's only as she leans towards [bree.name]'s chest that the other girl notices what's happening."
            bree.say "Sasha?"
            bree.say "What are you..."
            show bree flirt blush
            $ bree.love += 1
            bree.say "Ooh, Sasha..."
            "I watch with growing fascination as Sasha begins to lick at [bree.name]'s chest."
            "Most of the solid ice-cream has already run down [bree.name]'s chest and fallen onto the sand below."
            "And so she's straight down to using her tongue, lifting the sticky remains off of the other girl's skin."
            "To begin with, the sounds that [bree.name] makes are of surprise and alarm."
            "But pretty soon they melt like the ice-cream, becoming soft and sensual in nature."
            "I can almost taste the flavours of the ice-cream at first."
            "Then imagine it mixed with the tang of [bree.name]'s sun-cream and perspiration."
            "Even when she's licked up all of the ice-cream, Sasha still doesn't stop."
            "Her tongue goes on, tracing the outline of [bree.name]'s breast and threatening to go further..."
            bree.say "Ah..."
            bree.say "I...I think that's got it all!"
            $ bree.lesbian += 1
            $ sasha.lesbian += 1
            "I'd like to have seen her continue, but Sasha stops at [bree.name]'s request."
    scene bg beach
    show bree swimsuit blush at left5
    show sasha swimsuit blush at right5
    with fade
    "There's an awkward silence as we sit down on our towels to finish off the ice-cream cones."
    "It's as if the efforts to help [bree.name] get cleaned up have left us all feeling pretty flustered."
    "No one feels the urge to open their mouth and speak, so we just keep on filling them with ice-cream."
    "All the same, I know that my mind is full of images inspired by what we just did."
    "And I'm more than sure the same can be said for [bree.name] and Sasha too."
    hide bree
    hide sasha
    with moveoutright
    call home_harem_bree_sasha_beach_fuck from _call_home_harem_bree_sasha_beach_fuck
    "Nobody mentions it once as we pack up and begin to head home for the day."
    "But as I keep my promise and haul the largest share of the stuff back to the car, I allow myself a little smile."
    "As I can be pretty sure that it'll still be on everyone's mind on the drive back."
    "And there's a long evening ahead of us too."
    "One for which none of us have any real plans..."
    $ game.pass_time(4)
    scene bg black with dissolve
    return

label home_harem_bree_sasha_beach_fuck:
    "It's been a long, hot day at the beach, which I've spent relaxing and chilling out with [bree.name] and Sasha."
    "But now the sun is getting lower in the sky, and my thoughts are turning towards home."
    "So I start gathering up my stuff with a mind to heading back to the spot where I left the car."
    bree.say "Erm..."
    bree.say "Excuse me, [hero.name]!"
    bree.say "But where'd you think you're going?"
    show bree swimsuit at left5 with dissolve
    "I look up from what I'm doing to see [bree.name] standing over me."
    "She has one eyebrow raised and her hands on her hips."
    mike.say "Huh?"
    mike.say "I was just starting to pack up, [bree.name]."
    mike.say "It's almost time to go home, right?"
    show sasha swimsuit at right5 with dissolve
    "Sasha suddenly appears to the side of [bree.name]."
    "She wears a similar expression and a wry smile."
    sasha.say "Not so fast, mister!"
    sasha.say "Aren't you forgetting something?"
    sasha.say "Something really important?"
    "I look from one of them to the other."
    "And all the time my mind's racing."
    "What could I have forgotten that was so important?"
    "Did I promise to buy them an ice cream?"
    "Did I forget to rub sun cream into their hot bodies?"
    "Erm...no, I'd have remembered that!"
    mike.say "You've got me stumped, guys!"
    mike.say "What was it I forgot to do?"
    "Now it's [bree.name] and Sasha's turn to exchange glances."
    "And as they do so, they tut and roll their eyes at me."
    show bree flirt
    bree.say "Shall we show him, Sasha?"
    show sasha flirt
    sasha.say "I think we'd better, [bree.name]!"
    "They giggle to themselves and they take hold of their swimsuits."
    "And then I stare in amazement as they begin to strip off in front of me!"
    "Their giggling only becomes louder as they see my reaction."
    "And they make sure that this unexpected striptease is nice and slow too."
    show bree naked
    show sasha naked
    with dissolve
    "Soon enough they're naked, breasts jiggling as they laugh."
    bree.say "You forgot to fuck us, silly!"
    sasha.say "Yeah - you can't go home until we cum!"
    sasha.say "It's our new rule for trips to the beach."
    bree.say "You tell him, Sasha!"
    "My eyes almost pop out of their sockets as they crouch down on the sand."
    scene threesome breesasha
    show threesome breesasha beach
    with fade
    "Then they turn their backs to me and get on all fours, raising their asses."
    "[bree.name] and Sasha look back over their shoulders, wiggling their buttocks at me."
    bree.say "What are you waiting for, [hero.name]?"
    sasha.say "You want a written invitation to fuck us?"
    "What am I waiting for?!?"
    "I leap up, trying to pull down my shorts at the same time."
    "This means I stumble and sway on my knees."
    "But somehow I still manage to make it over to where the girls are waiting."
    show threesome breesasha beach slapbree breepleasure
    play sound spank
    with hpunch
    "I slap one hand down on [bree.name]'s ass to my left."
    show threesome breesasha beach -slapbree slapsasha slapedbree sashapleasure
    play sound spank
    with hpunch
    "And the other down on Sasha's to my right."
    show threesome breesasha beach -slapsasha slapedsasha
    "Both girls let out a squeal of surprise and delight."
    show threesome breesasha beach breenormal
    bree.say "Ooh..."
    bree.say "Fuck me, [hero.name]!"
    bree.say "And make it nice and hard!"
    show threesome breesasha beach sashanormal
    sasha.say "Ahh..."
    sasha.say "No way!"
    sasha.say "I want your cock inside of me!"
    show threesome breesasha beach -slapedbree -slapedsasha with dissolve
    "By now, all thoughts of feeling tired and heading for home are gone."
    "I feel like I just found a second wind, and I know just how to use it."
















































    "I don't know if it's the sweeping, raven black hair that does it."
    "Or the twinkle in those big, dark eyes."
    "But as soon as I think of fucking Sasha, I can't think of anything else!"
    show threesome breesasha squeezesasha
    "Taking my hand off of [bree.name]'s ass, I use them both to grab hold of Sasha."
    "I grip her around the waist and pull her sharply backwards."
    sasha.say "Wha..."
    sasha.say "Oh hell yeah!"
    sasha.say "Gimmie that cock, baby!"
    "I was already good and hard, ready to get down to business."
    "But hearing Sasha talking like that gives one last push."
    show threesome breesasha vaginaltip
    "I thrust myself forwards, pushing my cock between her thighs."
    "It slides along her lips, and I can feel just how wet she is down there."
    "There's no messing around with foreplay or teasing her."
    "I just pull Sasha back and shove my cock forwards."
    "Her pussy resists for a couple of seconds."
    show threesome breesasha vaginal sashapleasure
    "And then her lips part, and I sink into her."
    sasha.say "Uh..."
    sasha.say "Oh...oh fuck me..."
    sasha.say "Harder...fuck me harder!"
    "Just like there was no foreplay, there's also no starting slow."
    "Sasha's down on her hands and knees in the sand."
    "And she's spreading herself open to me like an animal."
    "So I don't hesitate to fuck her like one."
    "I hear the sound of my thighs slapping against hers."
    "She moans with each and every thrust, taking all I have to give."
    "But then I look across and see [bree.name], still on her hands and knees too."
    "She's watching us intently, a hunger in her eyes."
    show threesome breesasha fingers
    "Without slowing down for an instant, I reach out in her direction."
    show threesome breesasha vaginalfing
    "And I slide my hand between her legs."
    show threesome breesasha breepleasure
    "[bree.name] moans as I begin to stroke her pussy."
    "She's just as wet as [bree.name], just as desperate to be touched."
    "My hand and cock are moving together now."
    "And I'm trying to pleasure [bree.name] and Sasha at the same time."
    "Both of the girls are gasping and panting beneath me."
    "They look back over their shoulders at me."
    "Their heads are nodding and their eyes urging me on."
    show threesome breesasha sashaahegao
    "But then Sasha's eyes seem to glaze over."
    show threesome breesasha breeahegao
    "A moment later [bree.name]'s do the same."
    "I feel Sasha's pussy squeezing my cock."
    "And [bree.name]'s is giving my fingers the same treatment."
    show threesome breesasha with vpunch
    "They both cum within seconds of each other."
    show threesome breesasha creampie with vpunch
    "Then I lose it too, shooting my load into Sasha."
    $ sasha.sexperience += 1

    show threesome breesasha -vaginal dripsasha onbree
    "The moment I pull out, the very last of my energy seems to be spent."
    "I flop onto the sand and lie on my back, gasping for breath."
    "[bree.name] and Sasha crawl towards me, one lying down on either side."
    "They slide themselves onto me, hands caressing my softening cock."
    bree.say "Mmm..."
    bree.say "Now we can go home, [hero.name]!"
    sasha.say "Yeah, you did good!"
    sasha.say "That really hit the spot!"
    mike.say "That's great, guys."
    mike.say "I'm glad you reminded me."
    mike.say "But I might need a lie down first..."
    $ bree.love += 2
    $ sasha.love += 2
    scene bg black with dissolve
    return

label home_harem_bree_lexi_beach_date(appointment=None):
    if not hero.has_motor_vehicle:
        mike.say "Sorry girls, my car is in the garage."
        mike.say "We'll have to postpone our trip to the beach."
        $ bree.love -= 2
        $ lexi.love -= 2
        return
    $ game.room = "beach"
    "When I woke up and saw the weather report, I just knew that I had to spend the day at the beach."
    "And Ideally, I'd have asked all of the girls to come along with me - the more company the better."
    "But in the end, only [bree.name] and Lexi were around when I managed to get my ass out of bed and ask."
    "Not that I'm complaining."
    scene bg beach with fade
    "Because that means I'm hitting the sand with not one, but two blondes."
    show bree swimsuit at right5
    show lexi swimsuit at top_mostright
    "And the only thing hotter than them is the sand that we're walking on right now!"
    "Actually, the sand is REALLY hot today!"
    "It's burning my feet!"
    mike.say "Ah..."
    mike.say "Shit..."
    mike.say "My feet are on fire!"
    show bree happy at left5
    show lexi happy at right5
    with move
    "All this gets me from [bree.name] and Lexi is a round of laughter."
    "Neither of them seems to have even shred of sympathy for me."
    bree.say "Looks like you should have put something on your feet, [hero.name]!"
    lexi.say "So much for wanting to feel the sand between your toes!"
    "Both of them had the foresight to wear flip-flops."
    "And so they can afford to stand there and laugh at me as I hop around on the sand."
    mike.say "Hah-hah...very funny!"
    mike.say "Now can we please choose a spot?"
    mike.say "You know, before my feet burst into flames?"
    show bree normal
    show lexi normal
    "[bree.name] and Lexi both begin to scan the beach for a likely spot."
    "It's fairly busy today, and there are only two good spots free."
    bree.say "Hmm..."
    bree.say "How about over there?"
    bree.say "That'd be a good spot to catch some rays."
    show lexi annoyed
    lexi.say "No way, [bree.name]!"
    show lexi normal
    lexi.say "We should choose that spot over there."
    lexi.say "The one in the shade of the rocks."
    "Great, I choose to come to the beach with the two girls who can't agree on anything!"
    "I can already see [bree.name] and Lexi squaring up to each other."
    "Looks like I'm going to have to step in and settle this."
    show bree annoyed
    bree.say "I don't want to sit in the shade!"
    bree.say "What's the point of coming to the beach to do that?"
    show lexi annoyed
    lexi.say "Well I don't want to sit in the sun and get skin cancer!"
    lexi.say "Plus in the shade we can do stuff without anybody seeing it..."
    bree.say "Urgh..."
    bree.say "Do you have one clean thought in your head?"
    mike.say "Okay, okay..."
    mike.say "I'll choose the spot!"
    show bree normal
    show lexi normal
    "[bree.name] and Lexi nod in agreement, eyeing me intensely."
    "And I get the feeling they're both expecting me to side with them over the other."
    menu:
        "Choose the sun":
            mike.say "I think we should go with [bree.name]'s idea."
            mike.say "What's the point of coming to the beach and not enjoying the sun?"
            "[bree.name] can't help giving Lexi a triumphant smile."
            show bree happy
            "But it looks like she's not about to give up the fight."
            show lexi angry at right5, startle
            lexi.say "What the hell?!?"
            lexi.say "You were just moaning about burning your feet!"
            lexi.say "The sand's going to be roasting in the sun!"
            mike.say "It'll be okay once we put the towels down on the sand, Lexi!"
            show lexi sad
            "To make my point I stride across the sand to the spot [bree.name] picked out."
            "By the time I get there, I feel like the soles of my feet are peeling off."
            "But I stubbornly ignore the pain as I spread out my towel and sit down."
            "The matter being settled, [bree.name] and Lexi follow after me."
            $ bree.love += 2
            $ lexi.love -= 2
            $ beach_event = 0
        "Choose the shade":
            mike.say "I'm already burnt on the soles of my feet, [bree.name]!"
            mike.say "I don't want to end up burnt all over too."
            mike.say "I think we should go with Lexi's idea."
            show lexi happy
            "Lexi can't help giving [bree.name] a triumphant smile."
            "But it looks like she's not about to give up the fight."
            show bree angry
            bree.say "Are you serious?!?"
            bree.say "Or do you just want to fool around like she does?"
            mike.say "It's not like that, [bree.name]!"
            show bree sad
            "Of course it's not - I was hoping that all three of us could fool around!"
            "But maybe this isn't the time to admit to that."
            mike.say "I just think we need to keep cool, that's all."
            "Wanting to draw a line under the discussion, I stride over to the spot Lexi picked out."
            "By the time I get there, I feel like the soles of my feet are peeling off."
            "But I stubbornly ignore the pain as I spread out my towel and sit down."
            "The matter being settled, [bree.name] and Lexi follow after me."
            $ bree.love -= 2
            $ lexi.love += 2
            $ beach_event = 0
        "Use a parasol" if hero.charm >= 75:
            mike.say "Good thing one of us thought ahead!"
            "I hold up the parasol that I remembered to bring along just in case."
            mike.say "We can sit in the sun and make our own shade."
            mike.say "Plus if we angle it right, nobody can see us too."
            show bree annoyed
            show lexi annoyed
            "For a moment I think that [bree.name] and Lexi are both going to object."
            "But then the possibilities seem to dawn on them."
            show bree normal
            bree.say "That makes sense."
            show bree happy
            bree.say "You guys can lie in the shade and I can soak up some rays."
            show lexi normal
            lexi.say "Yeah, and we can get nice and cosy under that thing."
            lexi.say "Right, [hero.name]?"
            "I give them both a nod and an indulgent smile."
            "It all sounds good to me."
            "But I'm more pleased to have settled the argument between them."
            "We hurry over to the spot [bree.name] picked out."
            "And once we're there, I set up the parasol."
            $ bree.love += 1
            $ lexi.love += 1
            $ beach_event = 1
        "Choose a different spot" if hero.charm < 75:
            mike.say "You two are never going to agree on a spot."
            mike.say "So I'll take it out of your hands."
            "Both [bree.name] and Lexi open their mouths to object."
            show bree annoyed
            show lexi annoyed
            "But I ignore them and instead scan the beach for a third option."
            mike.say "What about over there?"
            "I point at the place where the sand meets the dunes and the rocks."
            "It's somewhere I'd never normally have chosen to settle on the beach."
            "But right now I just want to stop [bree.name] and Lexi arguing."
            bree.say "That's an awful spot!"
            bree.say "I won't be able to catch any rays there!"
            lexi.say "The ground's full of rocks!"
            lexi.say "It'll be like lying on a bed of nails!"
            mike.say "Yeah, nobody's happy with it."
            mike.say "So that's how you know it's a compromise!"
            "I walk over to the spot I picked out and drop our stuff on the ground."
            "[bree.name] and Lexi follow behind me, both muttering under their breath."
            $ bree.sub += 1
            $ lexi.sub += 1
            $ beach_event = -1
    show bree normal
    show lexi normal
    "Once we're settled down on the sand, [bree.name] and Lexi seem to forget about their quarrel."
    "Each of them is far too obsessed with their own agenda to waste any more time fighting."
    "[bree.name] finds the best possible spot in the sun and begins to soak up the rays she's been craving."
    "And Lexi contents herself with teasing me as she lies out on her towel at my side."
    "It's funny, but I've never really given a thought as to what I wanted to do today."
    "All I had on my mind was getting out of the house and making it to the beach."
    "And now I'm here, I realise I don't know what I want to get out of it!"
    "A moment later the most likely reason for that becomes painfully apparent."
    "Almost as one, [bree.name] and Lexi turn their gazes on me."
    "And I know that the temporary truce between them about to end..."
    bree.say "Mmm..."
    bree.say "[hero.name]..."
    show bree flirt
    bree.say "How about rubbing some sun cream on my back?"
    bree.say "I can't quite reach!"
    lexi.say "Ow..."
    lexi.say "Oh man!"
    lexi.say "I think I pulled a muscle!"
    show lexi flirt
    lexi.say "I'm gonna need you to give me massage!"
    "You see this is the problem with dating more than one girl at a time."
    "You think it's going to be nothing but fun and games."
    "But somehow you end up trapped between a rock and a hard place."
    menu:
        "Rub sun cream on [bree.name]":
            "I'm more than certain Lexi's putting it on for attention."
            "So I decide to answer [bree.name]'s call and ignore everything else."
            mike.say "I'll be right there, [bree.name]."
            lexi.say "Hey!"
            show lexi angry
            lexi.say "What about me?!?"
            mike.say "I don't know, Lexi."
            mike.say "I'm not a professional masseuse!"
            mike.say "Try stretching or something like that..."
            "Lexi says something that I can't quite make out."
            "But I'm sure that it's not complimentary."
            "Not that I pay it much attention."
            hide bree
            hide lexi
            show beach cream bree
            with fade
            "Instead I lie down beside [bree.name]."
            "She's smiling like the cat that got the cream!"
            bree.say "I need you to do my back, okay?"
            bree.say "All the way down to my butt."
            bree.say "And make sure you REALLY rub it in, okay?"
            "I nod eagerly as I squeeze the sun cream onto my hands."
            "And then I spend what feels like an eternity rubbing it into [bree.name]'s skin."
            "I take my time, enjoying the chance to trace the lines of her back."
            "And I must be doing a good job too, as she sighs and moans as I work away."
            "By the time I'm done, a certain part of my anatomy is stiff as a board."
            "Which makes getting back to my own spot pretty awkward."
            $ bree.love += 2
            $ lexi.love -= 2
        "Massage Lexi":
            "I'm one hundred percent sure Lexi's faking it."
            "But [bree.name]'s more than capable of rubbing sun cream on herself."
            "So I turn my attention to Lexi and ignore everything else."
            mike.say "Don't worry Lexi, I've got it under control."
            bree.say "Hey!"
            show bree angry
            bree.say "What about me?!?"
            bree.say "I asked for help first!"
            mike.say "You heard what Lexi said - this is a medical emergency!"
            "[bree.name] mutters something that I can't quite make out."
            "But I'm sure that it's not complimentary."
            "Not that I pay it much attention."
            hide bree
            hide lexi
            show beach cream lexi
            with fade
            "Instead I lie down beside Lexi."
            "She's smiling like the cat that got the cream."
            "Which is quite odd for someone supposed to be in serious pain!"
            lexi.say "It's right between my shoulders."
            lexi.say "Hurry up, [hero.name]!"
            lexi.say "It hurts so bad!"
            "I nod eagerly as I warm up my hands."
            "And then I take my time, enjoying the chance to get my hands on Lexi."
            "I must be doing a good job, as she sighs and moans as I work away."
            lexi.say "That's good!"
            lexi.say "But you need to go lower too!"
            lexi.say "All the way down to my butt!"
            "By the time I get down there, a certain part of my anatomy is stiff as a board."
            "And Lexi giggles wickedly as she feels it pressing against her thigh."
            $ bree.love -= 2
            $ lexi.love += 2
        "I need sun cream too!" if hero.charm >= 80:
            "It's pretty obvious both of them are trying to get my attention."
            "And I'm getting tired of them fighting like this all the time."
            "So maybe it's time to make somebody else the centre of attention instead?"
            mike.say "[bree.name], you're already covered in sun cream."
            mike.say "It's like the stuff's coming out of your pores!"
            mike.say "And you're obviously faking it, Lexi!"
            mike.say "You didn't pull a muscle at all."
            mike.say "So how about you both drop the bullshit?"
            mike.say "And maybe rub some sun cream on me instead?"
            show bree annoyed
            show lexi annoyed
            "[bree.name] and Lexi look a little crestfallen."
            "But they nod and crawl over to where I'm laid."
            show bree normal
            show lexi normal
            "[bree.name] doles out the sun cream and they get to work."
            "I lie on my stomach while they're at it."
            "[bree.name] takes my shoulders and works down."
            "While Lexi starts at my feet and works upwards."
            "By the time they meet in the middle, I'm pretty chilled out."
            "I could fall asleep on the spot thanks to their attentions."
            "In fact, every muscle in my body feels like it's relaxed."
            "Save for my cock, which is stiff as a board."
            $ bree.love += 1
            $ lexi.love += 1
            $ beach_event += 1
        "Go for a stroll" if hero.charm < 80:
            "It's pretty obvious both of them are trying to get my attention."
            "And I'm getting tired of them fighting like this all the time."
            "So maybe it's time for a change of scenery?"
            mike.say "Maybe you two should help each other out?"
            mike.say "Lexi, you can rub sun cream on [bree.name]."
            mike.say "And, [bree.name], you can massage Lexi at the same time."
            show lexi annoyed
            lexi.say "Huh?!?"
            show bree annoyed
            bree.say "But what about you?"
            "I get to my feet and shake the sand off of myself."
            mike.say "I need some fresh air."
            mike.say "So I'm going for a walk."
            mike.say "See you guys later."
            hide bree
            hide lexi
            with dissolve
            "With that, I stride off across the sand."
            "Behind me I can hear [bree.name] and Lexi talking."
            "And it doesn't sound like what they're saying is complimentary."
            "But my mind's made up and I need a little time away from their bickering."
            "Who knows, when I get back, maybe they'll have gotten over it?"
            $ bree.sub += 1
            $ lexi.sub += 1
            $ beach_event -= 1
    scene bg beach
    show bree swimsuit at left5
    show lexi swimsuit at right5
    with fade
    "It's getting a little bit later in the day and the heat is easing off."
    "I'm starting to feel a like it's time to get off my ass for a while."
    "And I can see [bree.name] and Lexi are starting to get restless too."
    mike.say "Hey, guys..."
    mike.say "You want to go do something?"
    mike.say "I think my ass went to sleep from lying here!"
    bree.say "Hmm?"
    bree.say "Yeah...I could stand to do something else."
    lexi.say "Uh-huh, why not."
    lexi.say "So what are we gonna do?"
    "I pause for a moment, realising I hadn't thought of that."
    "A quick glance around the beach turns up a couple of options."
    mike.say "Well..."
    show bree happy at left5, startle
    bree.say "Oh, I know!"
    show bree happy
    bree.say "Let's play volleyball!"
    show lexi angry
    lexi.say "No way!"
    show lexi happy
    lexi.say "I want to grab an ice cream!"
    show bree normal
    show lexi normal
    "For the love of all that's sacred and holy!"
    "Can these two not agree on one single fucking thing?"
    menu:
        "Play volleyball":
            mike.say "I think we should play volleyball."
            mike.say "Come on you two - there's a court free over there!"
            show bree happy
            bree.say "Yay!"
            bree.say "This is going to be so much fun!"
            show lexi annoyed
            lexi.say "Urgh..."
            lexi.say "Let's just get this over with, okay?"
            show bree normal
            "[bree.name] bounces over to where the volleyball net is set up."
            "She plucks the ball off of the sand and turns to face Lexi and me."
            bree.say "Okay..."
            bree.say "How are we going to do this?"
            bree.say "Two against one?"
            $ bree.love += 2
            $ lexi.love -= 2
            menu:
                "Team up with [bree.name]":
                    mike.say "I'll be on your team, [bree.name]!"
                    show lexi angry
                    lexi.say "What?"
                    lexi.say "How come I have to play on my own?!?"
                    "[bree.name] and I ignore Lexi's protests."
                    "And soon the game is underway."
                    scene bg black
                    show beach volleyball lexi swimsuit with fade
                    "It doesn't take long for Lexi to start losing."
                    "She's outnumbered and didn't want to play in the first place."
                    "So she gets a pretty sound beating from us, much to her chagrin."
                    lexi.say "There, you guys beat me."
                    lexi.say "Hurray for you!"
                    lexi.say "Can we do something else now?"
                    $ lexi.love -= 1
                "Team up with Lexi":
                    mike.say "I'll be on your team, Lexi!"
                    lexi.say "Okay - things are looking up!"
                    show bree surprised
                    bree.say "Huh?"
                    show bree sad
                    bree.say "I...I thought you'd want to be on my team?!?"
                    "Lexi and I ignore [bree.name]'s protests."
                    "And soon the game is underway."
                    scene bg black
                    show beach volleyball bree swimsuit with fade
                    "It doesn't take long for [bree.name] to start losing."
                    "Sure, she's pretty good at volleyball."
                    "But she's outnumbered, and soon it starts show."
                    "In the end, Lexi and I just manage to beat her."
                    bree.say "There, you guys beat me."
                    bree.say "Hurray for you!"
                    bree.say "Can we do something else now?"
                    $ bree.love -= 1
                    $ beach_event += 1
                "[bree.name] and Lexi team together":
                    lexi.say "We should team up, [bree.name] - you and me!"
                    show lexi happy
                    show bree happy
                    bree.say "Yeah, that's a great idea, Lexi!"
                    bree.say "Let's make it girls versus boys!"
                    mike.say "W...wait a minute!"
                    mike.say "That's not fair!"
                    "[bree.name] and Lexi ignore my protests."
                    scene bg black
                    show beach volleyball lexi swimsuit with fade
                    "And soon enough the game is underway."
                    "I try as best I can to hold my own against them."
                    scene bg black
                    show beach volleyball bree swimsuit with fade
                    "But I'm outnumbered and [bree.name]'s also a pretty good player."
                    "By the end of the game I'm a sweaty mess."
                    "And on top of that, they've trounced me too!"
                    mike.say "There, you guys beat me."
                    mike.say "Hurray for you!"
                    mike.say "Can we do something else now?"
                    $ bree.love += 2
                    $ lexi.love += 2
                    $ beach_event += 2
        "Get an ice cream":
            mike.say "I'm feeling pretty hot and bothered right now."
            mike.say "So an ice cream sounds like a pretty good idea."
            show lexi happy
            lexi.say "You know it does!"
            lexi.say "Let's go grab one right now!"
            show bree annoyed
            bree.say "Oh, alright..."
            show bree normal
            bree.say "If everybody else wants one!"
            "Lexi practically bounces across the sand towards the ice cream stall."
            "[bree.name] and I follow along after her, already eyeing up the menu."
            show lexi happy
            lexi.say "I want one of those - in BIG cone!"
            show bree happy
            bree.say "I guess I'll have one of these."
            "[bree.name] and Lexi point to the ice creams they want."
            "And soon enough we all have one in our hands."
            "We stroll away from the stall, licking away happily."
            "But then I notice that [bree.name]'s staring at something."
            "I follow her gaze and see that it's Lexi!"
            "[bree.name]'s watching in wide-eyed amazement as the other girl eats her ice cream."
            "Not that I can blame her, as Lexi's really going for it!"
            scene bg beach
            show beach icecream lexi nomc
            with fade
            "She's licking and slurping at it like she's giving the damn thing head!"
            "Suddenly, [bree.name] notices that I'm watching her in turn."
            "And she begins trying to copy Lexi too!"
            $ bree.love -= 2
            $ lexi.love += 2
            if bree.sexperience > lexi.sexperience:
                scene bg beach
                show beach icecream bree
                with dissolve
                "[bree.name] starts out doing exactly what she's seen Lexi doing."
                "But it doesn't take long for her to start putting her own twist on it."
                "Somehow she's more cheeky and playful in the way she licks the ice cream."
                "Just as suggestive, but more nonchalant and less obvious."
                "And when she catches me watching her, she even blushes a little."
                "But I notice that she doesn't stop!"
                scene bg beach
                show lexi swimsuit surprised at right5
                with fade
                lexi.say "Whoa!"
                lexi.say "Where did you learn to do that?"
                show bree swimsuit flirt at left5 with dissolve
                "[bree.name]'s eyes go wide with shock as the sound of Lexi's voice."
                show bree swimsuit normal blush
                "She blushes more than ever now she knows the other girl is watching her."
                show lexi normal
                lexi.say "You have to teach me how to do that!"
                "Lexi shakes her head, clearly impressed with what she's seeing."
                "I see [bree.name] smile at this, pleased to have won praise for her efforts."
                $ bree.love += 1
            else:
                scene bg beach
                show beach icecream bree
                with fade
                "[bree.name] slurps and licks at her ice cream as best she can."
                "I can see that she's trying her hardest to do it just like Lexi."
                "But the problem is that she's watching me all the time."
                "Lexi was focussing all of her attention on the ice cream."
                "[bree.name]'s distracted, and so she doesn't see the imminent danger."
                "Without warning, her ice cream begins to topple."
                "And then most of it falls off, landing in the sand by her feet."
                scene bg beach
                show bree swimsuit surprised at left5
                with fade
                bree.say "Oh dear!"
                show lexi swimsuit happy at right5 with dissolve
                lexi.say "Whoops!"
                lexi.say "I hope you're better at sucking cock than you are at eating ice cream, [bree.name]!"
                show bree swimsuit annoyed blush
                "[bree.name]'s cheeks flush red at Lexi's comment."
                "And she avoids eye-contact while she finishes off the remains of her ice cream."
                $ lexi.love += 1
                $ beach_event += 1
        "Play in the sea" if hero.charm >= 95:
            mike.say "I'm feeling pretty hot and bothered right now."
            mike.say "Let's go cool off in the sea for a while."
            "Both [bree.name] and Lexi look at me like I'm speaking a foreign language."
            show bree annoyed
            bree.say "You mean go paddling?!?"
            show lexi annoyed
            lexi.say "What other ideas you got?"
            lexi.say "Maybe make sandcastles?"
            "I shake my head at their negative reactions."
            mike.say "What, you think the sea's just for kids?"
            mike.say "Whatever - I'll go on my own!"
            scene bg beach at center, zoomAt(2.25, (1440, 1275)) with fade
            "I start towards the water, honestly intending to leave them behind."
            "But they catch up to me just as I'm walking into the waves."
            show bree swimsuit a at center, zoomAt(1.25, (340, 940)) with moveinright
            bree.say "Whoa!"
            show bree sad a at center, zoomAt(1.0, (340, 940)), hshake
            bree.say "It's so cold!"
            show lexi swimsuit b nophone at center, zoomAt(1.25, (940, 940)) with moveinright
            lexi.say "Yeah, you said it!"
            show lexi sad b at center, zoomAt(1.0, (940, 940)), hshake
            lexi.say "The water's freezing!"
            "I can't help smiling as I see [bree.name] and Lexi shivering."
            "They both have their arms wrapped around themselves."
            "Meaning that they're completely vulnerable!"
            mike.say "Is that so?"
            mike.say "So it'd be a shame if someone were to..."
            show playing water bree with hpunch
            mike.say "SPLASH YOU!"
            "Before [bree.name] and Lexi know what's happening, I fling water at them."
            "They let out screams of alarm and try to shield themselves."
            "But it's too late, and a moment later they're soaked to the skin."
            bree.say "[hero.name], you jerk!"
            show playing water lexi with hpunch
            lexi.say "You're gonna pay for that!"
            "[bree.name] and Lexi chase after me, wading through the water."
            "They splash me, trying to get revenge for my initial attack."
            show playing water bree with hpunch
            "And I give back as good as I get, laughing the whole time."
            bree.say "Okay, okay..."
            bree.say "Truce!"
            scene bg beach at center, zoomAt(2.25, (1440, 1275))
            show bree swimsuit b happy at center, zoomAt(1.25, (340, 940))
            show lexi swimsuit a happy nophone at center, zoomAt(1.25, (940, 940))
            lexi.say "Yeah, enough with the water already!"
            "All three of us are soaking wet."
            "But we're also smiling and laughing too."
            "So I'd call that mission accomplished."
            $ bree.love += 1
            $ lexi.love += 1
            $ beach_event += 2
        "Make sandcastles" if hero.charm < 95:
            mike.say "I'm feeling pretty tired right now."
            mike.say "So why don't we chill out and make some sandcastles?"
            "I smile as I hold up a plastic bucket and spade."
            "But both [bree.name] and Lexi look at me like I'm speaking a foreign language."
            show bree annoyed
            bree.say "Erm...maybe because we're not little kids?"
            show lexi annoyed
            lexi.say "What other ideas you got?"
            lexi.say "Maybe go paddle in the sea?"
            "I shake my head at their negative reactions."
            mike.say "What, you think it's just for kids?"
            mike.say "Whatever - I'll do it on my own!"
            hide bree
            hide lexi
            with dissolve
            "I walk a little way down the beach and start digging."
            "I'm hoping that [bree.name] and Lexi will come join me."
            "But they just go back to lying on their towels."
            scene bg beach
            show beach sandcastle bree alonemc mc_swimsuit mikemc 01
            with fade
            "Which leaves me to make sandcastles on my own."
            "And I stubbornly do so until I'm tired of being stared at."
            "Then I quietly go back to where the others are laid."
            "All the time hoping that they won't mention it again."
            $ bree.sub += 1
            $ lexi.sub += 1
            $ beach_event -= 2
    scene bg beach
    show bree swimsuit at left5
    show lexi swimsuit at right5
    with fade
    if beach_event >= 3:
        call home_harem_bree_lexi_beach_fuck from _call_home_harem_bree_lexi_beach_fuck
    else:
        "Once we've all had enough sands, sea and fresh air, we pack up and head home."
        "Everyone's tired and more than a little red from the baking sun."
        "But I think we managed to make a pretty good day of it."
        "And coming to the beach today was the right call."
        scene bg black with dissolve
    $ game.pass_time(4)
    return

label home_harem_bree_lexi_beach_fuck:
    "The sun is getting ever lower in the sky, and I can feel the chill of evening in the air."
    "But that's no matter, as it's been one of those days at the beach where everything just went right."
    "We got here in good time, found a great spot and the weather's been perfect the whole time too."
    "Plus I got to spend it in the company of [bree.name] and Lexi."
    "So the weather wasn't even the hottest thing at the beach!"
    "By rights, I should be feeling tired and ready to head home."
    "But I seem to have some energy left, and it's making me a little restless."
    "I keep staring at [bree.name] and Lexi in their swimsuits."
    "And pretty soon it's my own trunks that are attracting attention."
    "Or to be more precise, what's going on inside of them!"
    lexi.say "Hey, [bree.name]..."
    lexi.say "Come check this out!"
    bree.say "Huh?"
    bree.say "What is it, Lexi?"
    lexi.say "[hero.name]'s got a stiffy on!"
    show bree surprised
    show lexi happy
    lexi.say "And I think it's from staring at us!"
    "The smile on Lexi's face is almost wicked."
    "By contrast, [bree.name]'s expression is one of surprise."
    "But then she sees what Lexi's talking about."
    show bree happy
    "And together they start to giggle like sexy little imps!"
    mike.say "Hey!"
    mike.say "Will you stop that?!?"
    mike.say "It's not like I can help it!"
    mike.say "You two are just super hot, you know?"
    "[bree.name] and Lexi stop laughing, but they still look pretty evil to me."
    show bree evil
    show lexi wink
    "They exchange glances and then they both begin to smile."
    bree.say "He IS kind of paying us a compliment, Lexi."
    bree.say "So maybe we should do something nice for him in return?"
    lexi.say "Hmm...I think I know just the thing, [bree.name]."
    show lexi flirt
    lexi.say "Let's be mermaids - and seduce him!"
    "[bree.name]'s face lights up at this."
    bree.say "Oh yeah, Lexi!"
    bree.say "I always wanted to be a mermaid."
    show bree flirt
    bree.say "Sitting on a rock and combing my hair..."
    "Lexi lets out a filthy snort of laughter."
    lexi.say "Nah, [bree.name] - not that kind of mermaid!"
    lexi.say "I mean the kind that grab sailors and do them on the sand!"
    bree.say "Do...do mermaids do things like that?"
    lexi.say "Of course they do, [bree.name]!"
    lexi.say "How else to they get cock?"
    bree.say "Okay - let's do it!"
    show bree topless
    show lexi topless
    "I watch as [bree.name] and Lexi all but tear off their swimsuits."
    "And then they turn their attentions to me!"
    show bree naked
    show lexi naked
    "Before I can even say a word, they pounce on me."
    "And my own shorts go the same way as their swimsuits."
    "Watching [bree.name] and Lexi while listening to them talk has already got me aroused."
    "So it's no surprise to me that my cock pops up, standing erect once it's free."
    lexi.say "There it is, [bree.name] - that's what we want!"
    lexi.say "That's why mermaids lure human guys to their doom!"
    bree.say "Oh my!"
    bree.say "No wonder they like doing that!"
    bree.say "How about it, [hero.name]?"
    bree.say "Ready to be ravished by two horny mermaids?"
    "I'm more than ready!"
    "And I don't waste a moment."
    mike.say "Sure thing, girls."
    mike.say "But which one of you gets to ride the Kraken?"
    "Suddenly it becomes a competition between [bree.name] and Lexi."
    "They both pose and pout, trying to convince me to fuck them."
    bree.say "Ooh..."
    show bree happy
    bree.say "Pick me, pick me!"
    lexi.say "Nah, this is the pussy you want!"
    show lexi happy
    lexi.say "It's already wet and waiting for you!"
    menu:
        "Choose [bree.name]":
            "Maybe it's all the talk of mermaids that makes my mind up in the end."
            "Because of [bree.name]'s blonde locks and big, blue eyes."
            "I can just imagine her with a tail below the waist!"
            "So I don't hesitate to pounce on her a moment later."
            "She let's out a yelp of surprise and tries to scurry away."
            "But that only means that I can catch her by the haunches more easily."
            "While [bree.name]'s on all fours, I take full advantage."
            "I pull her backwards and thrust myself forwards in one motion."
            scene threesome breelexi breefuck
            show threesome breelexi breefuck beach
            with fade
            "This means my cock pushes between her thighs, rubbing against her ass."
            bree.say "Oh..."
            bree.say "Mmm..."
            bree.say "I guess you caught me, [hero.name]!"
            bree.say "Now what are you going to do with me?"
            "[bree.name]'s looking back over her shoulder at me as she says this."
            "But if she's expecting a reply in the form of words, she's going to be disappointed."
            "Because I answer her question by aiming the head of my cock just so."
            show threesome breelexi breefuck anal
            "And then I start to push my way inside of her."
            bree.say "Oh god..."
            bree.say "Yeah..."
            bree.say "You can do that to me!"
            bree.say "Oh please...do that to me!"
            "It's not like I need the encouragement [bree.name]'s giving me."
            "I'm already sinking into her, going as deep as I can possibly go."
            "And it doesn't take long for me to begin picking up speed."
            "[bree.name] was more than ready when we started, offering no resistance."
            "And her pussy feels as smooth as silk the whole time I'm inside her."
            "She arches her back, trying to get the most possible out of my motions."
            "I can see the way that her breasts are swinging beneath her."
            "And beads of sweat are beginning to appear across her back."
            show threesome breelexi breefuck lexi
            lexi.say "Hey, little mermaid..."
            lexi.say "Check this out!"
            "[bree.name] and I both look up at the same moment."
            "And we see Lexi crouching down on the sand before us."
            "She reaches out for [bree.name] at the same time."
            show threesome breelexi breefuck bree_hand fingering
            "Lexi strokes and caresses [bree.name]'s pussy, exploring with interest."
            "This makes the other girl gasp and pant."
            "Lexi has to hold herself up with one hand."
            "But with the other she increases the pace of her exploration of [bree.name]'s intimate part."
            show threesome breelexi breefuck pleasure
            "All this time I'm still pounding away at [bree.name]."
            "The sensation is amazing in its own right."
            "But with the show they're putting on in front of me..."
            "Well, let's just say that it's no surprise what happens next."
            mike.say "Oh shit..."
            mike.say "Here it comes!"
            with vpunch
            "I lose it a moment later, letting go deep inside of [bree.name]."
            show threesome breelexi breefuck creampie ahegao with vpunch
            "She gasps as I do so, and I see Lexi's fingers push deep inside her."
            with vpunch
            "A few seconds later, we're all collapsing onto the sand, our muscles giving up the fight."
            $ bree.sexperience += 1
            $ bree.flags.anal += 1
        "Choose Lexi":
            "Maybe it's all the talk of mermaids that makes my mind up in the end."
            "Because Lexi's just such an unashamedly sensual girl."
            "I can just imagine her as a wild, untamed siren!"
            "So I don't hesitate to pounce on her a moment later."
            scene threesome breelexi lexifuck
            show threesome breelexi lexifuck beach
            with fade
            "She let's out a yelp of surprise, then a filthy giggle."
            "And then she shoves her ass towards me without a hint of shame."
            "I don't hesitate to take full advantage of her offer."
            "I pull her backwards and thrust myself forwards in one motion."
            "This means my cock pushes between her thighs, rubbing against her pussy."
            show threesome breelexi lexifuck mike
            lexi.say "Ah..."
            lexi.say "Mmm..."
            lexi.say "Looks like I got myself caught!"
            lexi.say "So I'd better be nice to whoever snagged me!"
            "Lexi's looking back over her shoulder at me as she says this."
            "But if she's expecting a reply in the form of words, she's going to be disappointed."
            "Because I answer her question by aiming the head of my cock just so."
            show threesome breelexi lexifuck vaginal
            "And then I start to push my way inside of her."
            lexi.say "Whoa..."
            lexi.say "Oh yeah..."
            lexi.say "I gotta get caught more often!"
            lexi.say "And you'd better fuck me hard!"
            "It's not like I need the encouragement Lexi's giving me."
            "I'm already sinking into her, going as deep as I can possibly go."
            "And it doesn't take long for me to begin picking up speed."
            "Lexi was more than ready when we started, offering no resistance."
            "And her pussy feels as smooth as silk the whole time I'm inside her."
            "She arches her back, trying to get the most possible out of my motions."
            "I can see the way that her breasts are swinging beneath her."
            "And beads of sweat are beginning to appear across her back."
            show threesome breelexi lexifuck bree
            bree.say "Hey, you dirty little fish..."
            bree.say "Look over here!"
            "Lexi and I both look up at the same moment."
            "And we see [bree.name] standing before us."
            "She spreads her legs and reaches out for Lexi's mouth."
            "And she doesn't have to be shown what to do next."
            "Lexi starts licking [bree.name]'s pussy, exploring with interest."
            show threesome breelexi lexifuck lick
            "This makes the other girl gasp and pant."
            "[bree.name] lower herself a bit so Lexi can push her exploration deeper."
            show threesome breelexi lexifuck breepleasure
            "All this time I'm still pounding away at Lexi."
            "The sensation is amazing in its own right."
            "But with the show they're putting on in front of me..."
            "Well, let's just say that it's no surprise what happens next."
            mike.say "Oh shit..."
            mike.say "Here it comes!"
            with hpunch
            "I lose it a moment later, letting go deep inside of Lexi."
            show threesome breelexi lexifuck creampie lexiahegao with hpunch
            "She gasps as I do so, and I see that [bree.name] cannot hold herself either."
            with hpunch
            "This makes the other girl yelp as she collapses backwards onto the sand."
            "A few seconds later, we're all collapsing onto the sand, our muscles giving up the fight."
            $ lexi.sexperience += 1
    "We lie there in the sand, the sweat on our bodies drying in the sun."
    "No doubt that used up the last of the energy that I had to give."
    "And it seems like the same is true of [bree.name] and Lexi too."
    "They crawl over to me and nestle one on each side."
    "And I find myself battling to stay awake."
    "The sound of the waves is lulling me to surrender."
    "And at this rate, we might end up asleep on the beach."
    $ bree.love += 2
    $ lexi.love += 2
    scene bg black with dissolve
    return

label home_harem_lexi_minami_samantha_beach_date(appointment=None):
    if not hero.has_motor_vehicle:
        mike.say "Sorry girls, my car is in the garage."
        mike.say "We'll have to postpone our trip to the beach."
        $ lexi.love -= 2
        $ minami.love -= 2
        $ samantha.love -= 2
        return
    $ game.room = "beach"
    "It's turning out to be a scorching hot day, and for once I'm free to make the best of it."
    "I don't have to be in work today, and I'm pretty much up to date with all of my studies too."
    "All of which means the only sensible thing to do is load up the car and head to the beach!"
    "But the moment that I mention it around the house, I find that I have people to load up as well."
    "Lexi, Minami and Sam all announce that they're coming along too."
    "And why not?"
    "Why wouldn't I want to be accompanied by three hot girls?"
    scene bg beach with fade
    "As soon as we pull up in the car park, they're out of the car and unloading their junk."
    show minami swimsuit at left with moveinright
    minami.say "Yay!"
    minami.say "Beach here we come!"
    show lexi swimsuit at right with moveinright
    lexi.say "Hey!"
    lexi.say "Wait for me!"
    show samantha swimsuit with moveinright
    samantha.say "Don't worry, [hero.name]."
    samantha.say "I'm not about to run off with those two!"
    "I can't help smiling as Sam falls in by my side and we walk down to the beach."
    "I know that Sam's older than Minami - most people are!"
    "And she's about the same age as Lexi too."
    "But somehow she always feels the closest to me in years."
    "Perhaps it's because I've known her the longest and we're just closer that way?"
    "Whatever the reason, this is a chance to pump her for information."
    if samantha.flags.nickname == "cupcake":
        mike.say "Cupcake..."
    else:
        mike.say "Sam..."
    mike.say "I was wondering..."
    mike.say "Why didn't [bree.name] and Sasha want to come along today?"
    samantha.say "Oh, we didn't bother telling them."
    show samantha happy
    samantha.say "That's why!"
    mike.say "Why would you do that?"
    samantha.say "Well, we knew that you'd taken those two to the beach before."
    samantha.say "They said that they had a great time too."
    show samantha flirt
    samantha.say "So the three of us figured that it was our turn!"
    "I nod and smile."
    "But I can feel my impression of Sam's maturity draining away."
    "I ignore the childish reasons for cutting [bree.name] and Sasha out of the trip."
    "It doesn't really matter, does it?"
    "And I don't want to let it get in the way of us having a great day at the beach."
    "But the first obstacle to that pops up when we actually get onto the sand."
    show samantha normal
    "Lexi, Minami and Sam all begin to walk in different directions."
    "This causes me to stop, not knowing who to follow."
    "And a moment later the others stop too, realising there's a problem."
    show lexi annoyed
    lexi.say "Hey - what's the hold up?"
    show minami annoyed
    minami.say "You guys are all going the wrong way!"
    show samantha annoyed
    samantha.say "I don't think so!"
    "Looking at the signage around us, I think I see the problem."
    "Each of the girls seems determined to head to a different part of the beach."
    mike.say "Erm..."
    mike.say "Maybe we should have discussed this before we got here?"
    minami.say "Aww..."
    show minami normal
    minami.say "I wanted to go to the topless beach!"
    minami.say "I don't want to get tan-lines!"
    samantha.say "Now wait a minute!"
    show samantha normal
    samantha.say "I thought we were going to the normal beach?"
    samantha.say "You know, the one where you don't have to get naked?"
    lexi.say "Geez..."
    show lexi normal
    lexi.say "What a bunch of stiffs!"
    lexi.say "I'm up for the nudist beach!"
    "As one, they all turn to look at me."
    "And it looks like I'm going to have to make the casting vote!"
    menu:
        "Go to the family beach":
            "All I wanted was a great day at the beach."
            "And I never saw that involving nudity - full or partial!"
            "So it's not hard for me to make my choice."
            mike.say "You guys can all go where you like."
            mike.say "But I'm heading for the normal beach."
            mike.say "The one that's PG-13, rather than X-Rated!"
            show samantha happy
            "Sam gives me a smug smile."
            "And she takes my arm as she does so."
            samantha.say "Come on, [hero.name]."
            samantha.say "Let's go!"
            show minami annoyed
            show lexi annoyed
            "Lexi and Minami both look suitably annoyed."
            "But they soon scurry along after Sam and me."
            minami.say "Wait up, big bro!"
            show minami normal
            minami.say "I don't want to get left on my own!"
            lexi.say "Me neither."
            show lexi normal
            lexi.say "Even if you are a bunch of prudes!"
            "After that it doesn't take us long to find a spot."
            "We spread our towels out on the sand to stake our claim."
            "And then the beach is ours for the taking."
            $ lexi.love -= 1
            $ minami.love -= 1
            $ samantha.love += 1
            $ beach_event = 0
            $ beach_choice = "clothed"
        "Go to the topless beach":
            "I was just thinking of having a normal day at the beach."
            "But now that Minami's mentioned the topless part of the beach..."
            "Well, let's just say that my priorities have changed!"
            mike.say "I like the sound of the topless beach, Minami."
            mike.say "I was planning on going topless too!"
            show minami happy
            "Minami sniggers and snorts at my bad joke."
            "And she takes my arm as she does so."
            minami.say "You bet, big bro!"
            minami.say "You're gonna love it!"
            show lexi annoyed
            show samantha annoyed
            "Both Lexi and Sam look suitably annoyed."
            "But they soon scurry along after Minami and me."
            lexi.say "Hold up - wait for me!"
            show lexi normal
            lexi.say "I'll settle for being half-naked!"
            samantha.say "I'm not getting left behind!"
            show samantha normal
            samantha.say "And I'll prove I'm not a prude either!"
            "It doesn't take us long to find a spot on the topless part of the beach."
            "I spread out my towel on the sand, trying to make it look as casual as I can."
            "But I'm literally surrounded by naked breasts, all glistening in the sun!"
            minami.say "Okay, here goes!"
            minami.say "Goodbye tops, hello tan!"
            show minami topless
            "I'm trying to take in the sight of Minami's breasts as best I can."
            if samantha.flags.sexyswimsuit:
                "But a moment later, Lexi follow her lead."
                show lexi topless
                samantha.say "My swimsuit barely covers anything, I'll keep it on."
                show samantha swimsuit
            else:
                "But a moment later, Lexi and Sam follow her lead."
                show samantha topless
                show lexi topless
            "Which leaves me speechless!"
            "I lie down on the sand, trying to hide my erection."
            "But still trying to stare at them the whole time too."
            $ lexi.love -= 1
            $ minami.love += 1
            $ samantha.love -= 1
            $ beach_event = 0
            $ beach_choice = "topless"
        "Go to the nudist beach" if game.flags.nudistBeach:
            "I was just thinking of having a normal day at the beach."
            "But now that Lexi's mentioned the nude part of the beach..."
            "Well, let's just say that my priorities have changed!"
            mike.say "I like the sound of the nude beach, Lexi!"
            mike.say "I could handle getting naked too!"
            show lexi happy
            "Lexi snorts in triumph already walking onwards."
            "And she takes my arm as she does so."
            lexi.say "Any chance to see me butt naked!"
            lexi.say "You're such a dirty boy, [hero.name]!"
            show minami annoyed
            show samantha annoyed
            "Both Minami and Sam look suitably annoyed."
            "But they soon scurry along after Lexi and me."
            minami.say "Wait up, big bro!"
            show minami normal
            minami.say "I don't want to get left on my own!"
            samantha.say "I'm not getting left behind!"
            show samantha normal
            samantha.say "And I'll prove I'm not a prude either!"
            "It doesn't take us long to find a spot on the nude part of the beach."
            "I spread out my towel on the sand, trying to make it look as casual as I can."
            "But I'm literally surrounded by naked bodies, all glistening in the sun!"
            lexi.say "Okay, here goes!"
            lexi.say "Goodbye clothes, hello even tan!"
            show lexi naked
            "I'm trying to take in the sight of Lexi's naked body as best I can."
            "But a moment later, Minami and Sam follow her lead."
            show samantha naked
            show minami naked
            "Which leaves me speechless!"
            "I lie down on the sand, trying to hide my erection."
            "Which is made that much harder thanks to the fact I'm naked too!"
            $ lexi.love += 1
            $ minami.love -= 1
            $ samantha.love -= 1
            $ beach_event = 0
            $ beach_choice = "naked"
        "Choose a different spot" if hero.charm >= 75:
            "All I wanted was a day at the beach."
            "I didn't plan for a drama like this!"
            "I need to think of something that'll keep everyone happy."
            "And I need to do it fast too!"
            mike.say "Do we really need a special part of the beach to do all that?"
            "Lexi and Minami frown at this, shaking their heads."
            show lexi annoyed
            lexi.say "If there's a special part of the beach for it, then yeah!"
            minami.say "She's right, big bro."
            show minami annoyed
            minami.say "We could get in trouble doing it anywhere else!"
            mike.say "Yeah, but only if someone catches us."
            mike.say "So we find somewhere that they won't."
            "Sam seems to warm to the idea as I explain it."
            "Probably because it means the nudity will be strictly optional."
            samantha.say "He's right, you guys."
            show samantha happy
            samantha.say "So long as we find a secluded spot, we can do what we like!"
            lexi.say "Yeah..."
            show lexi happy
            lexi.say "That sounds good to me!"
            minami.say "Me too, big bro!"
            show minami happy
            minami.say "Let's go find our spot."
            "Finding the right place on the beach takes a while."
            "But we're looking for just the right spot."
            "And when we find it, everyone seems pleased."
            minami.say "Okay, here goes!"
            show minami topless
            minami.say "Goodbye tops, hello tan!"
            show lexi naked
            lexi.say "Goodbye clothes, hello even tan!"
            "I do the best I can not to stare like some crazy pervert."
            "But I've got Minami's breasts on one side."
            "And a totally naked Lexi on the other!"
            "Then I realise that Sam's spread herself out on the side beside me too."
            "Sure, she's still wearing her swimming costume, but it makes no difference."
            "It's Sam - she could turn me on in a boilersuit and welding mask!"
            samantha.say "What's the matter, [hero.name]?"
            samantha.say "You like what you see?"
            "Sam underlines her point by gazing down at my shorts."
            "Where it's plain to see that I'm more than a little aroused!"
            $ lexi.love += 1
            $ minami.love += 1
            $ samantha.love += 1
            $ beach_event = 1
            $ beach_choice = "free"
        "Choose a different spot" if hero.charm < 75:
            "I came to the beach to relax - not to deal with this kind of crap!"
            "So there's no way that I'm playing peacemaker for these guys."
            mike.say "The three of you can go wherever you like."
            mike.say "I came to have a day at the beach."
            mike.say "And that's exactly what I'm going to do!"
            "With that, I stride off across the sand."
            "And it doesn't take long for the girls to stop arguing with each other."
            "The only problem is that now they're all arguing with me!"
            lexi.say "Hey!"
            show lexi annoyed
            lexi.say "Where'd you think you're going?!?"
            minami.say "Big bro!"
            show minami annoyed
            minami.say "Don't leave me behind!"
            samantha.say "You can't just walk off and leave us!"
            show samantha annoyed
            samantha.say "Aren't you at least going to try to help?!?"
            "I make a point of ignoring them until I reach a likely spot."
            "And then I spread my towel out on the sand."
            mike.say "Here we are."
            mike.say "Anyone want to join me?"
            "The others shake their heads and mutter under their breath."
            "But nobody seem to be in the mood to keep the fight going."
            "Sure, I know it's not the perfect solution."
            "And they're all going to hold it against me."
            "But why should I always be the one to sort this stuff out?"
            $ lexi.sub += 1
            $ minami.sub += 1
            $ samantha.sub += 1
            $ beach_event = -1
            $ beach_choice = "clothed"
    if beach_choice == "topless":
        show minami swimsuit topless normal at left
        if samantha.flags.sexyswimsuit:
            show samantha swimsuit normal
        else:
            show samantha swimsuit topless normal
        show lexi swimsuit topless normal at right
    elif beach_choice == "naked":
        show minami naked normal at left
        show samantha naked normal
        show lexi naked normal at right
    elif beach_choice == "free":
        show minami swimsuit topless normal at left
        show samantha swimsuit normal
        show lexi naked normal at right
    else:
        show minami swimsuit normal at left
        show samantha swimsuit normal
        show lexi swimsuit normal at right
    "Now that everything's been resolved, the girls seem to settle down."
    "Everyone lies on the sand, just enjoying the feeling of the sun beating down."
    "In fact, I must have been so relaxed that I actually dropped off for a while."
    "Because the next thing I know, the sun is higher in the sky."
    "And there's a discussion going on around me too."
    lexi.say "Nah, it's too frikin hot!"
    lexi.say "We should grab an ice cream."
    show lexi happy
    lexi.say "You know, cool down?"
    minami.say "We can do that AFTER we play, Lexi!"
    minami.say "Look, the volleyball court is empty right now."
    show minami happy
    minami.say "We might not get another chance for hours!"
    samantha.say "I still think we should take a dip in the sea."
    show samantha happy
    samantha.say "It'll cool us off and it might get too hot later."
    "Sam looks like she's about to say something else."
    "But then she notices that I've stirred."
    "And she turns her attention to me instead."
    samantha.say "What do you think, [hero.name]?"
    menu:
        "Get an ice cream":
            mike.say "You know..."
            mike.say "I could really go for an ice cream right now!"
            mike.say "Let's go get one, then we can do whatever after that."
            show minami annoyed
            show samantha annoyed
            "Minami and Sam don't look too pleased with my choice."
            "But Lexi cuts them off before they can disagree."
            lexi.say "Great - let's go get ice cream!"
            "Lexi grabs my hand and pulls me to my feet."
            "And the next thing I know, she's dragging me across the sand."
            "Which means that the others have no choice but to follow in her wake."
            "It's only a short walk to the ice cream stand."
            "And a few moments later, everyone's clutching their choice of frozen treat."
            "But as we walk away, I can't help staring at Lexi."
            if beach_choice in ["naked", "free"]:
                show beach icecream lexi nomc naked with fade
            else:
                show beach icecream lexi nomc swimsuit with fade
            "She's not so much licking her ice cream as teasing it with her tongue!"
            "The sight instantly reminds me of other things she does with it too."
            "I tear my eyes away for a moment to check on Minami and Sam."
            "And I see that they're watching too, both spellbound by what they're seeing!"
            "But when they notice me watching them, everything changes."
            "I don't know if it's conscious, but they start doing the same thing!"
            "Minami and Sam are licking their ice creams in a suggestive manner too."
            "Or at least they're trying their best to pull it off!"
            if minami.sexperience > lexi.sexperience and samantha.sexperience > lexi.sexperience:
                "There must be a knack to this kind of thing."
                "Because Minami and Sam seem to have hit on it."
                "That's how I find myself watching all three of them doing it!"
                if beach_choice in ["naked", "free"]:
                    show beach icecream lexi nomc naked
                else:
                    show beach icecream lexi nomc swimsuit
                "Lexi, Minami and Sam all lick and lap at their ice creams."
                if beach_choice == "naked":
                    show beach icecream minami nomc naked
                else:
                    show beach icecream minami nomc swimsuit
                "But I'm not thinking about that."
                if beach_choice == "naked":
                    show beach icecream samantha nomc naked
                else:
                    show beach icecream samantha nomc swimsuit
                "All I can imagine is what else they could be doing with those tongues!"
                "In fact, I'm so engrossed that I forget all about my own ice cream."
                "That is until the sun begins to melt it."
                "And the whole thing flops over my and then onto the ground."
                mike.say "Wha..."
                mike.say "Ah shit!"
                minami.say "Aw..."
                scene bg beach
                if beach_choice == "topless":
                    show minami swimsuit topless normal at left
                    if samantha.flags.sexyswimsuit:
                        show samantha swimsuit normal
                    else:
                        show samantha swimsuit topless normal
                    show lexi swimsuit topless normal at right
                elif beach_choice == "naked":
                    show minami naked normal at left
                    show samantha naked normal
                    show lexi naked normal at right
                elif beach_choice == "free":
                    show minami swimsuit topless normal at left
                    show samantha swimsuit normal
                    show lexi naked normal at right
                else:
                    show minami swimsuit normal at left
                    show samantha swimsuit normal
                    show lexi swimsuit normal at right
                show minami annoyed
                minami.say "Too bad, big bro!"
                show samantha annoyed
                samantha.say "Whoops!"
                show lexi happy
                lexi.say "Looks like you went all floppy!"
                $ lexi.love += 1
                $ minami.love += 1
                $ samantha.love += 1
                $ beach_event += 1
            else:
                "There must be a knack to this kind of thing."
                "But whatever it is, Minami and Sam aren't finding it."
                if beach_choice == "naked":
                    show beach icecream minami nomc naked
                else:
                    show beach icecream minami nomc swimsuit
                "Instead of looking seductive, instead look downright ridiculous."
                "The two of them lick and slurp at their fast-melting ice creams."
                if beach_choice == "naked":
                    show beach icecream samantha nomc naked
                else:
                    show beach icecream samantha nomc swimsuit
                "And all they manage to do is push them towards collapse."
                "Pretty soon their ice creams flop over and fall onto the sand."
                minami.say "Ugh..."
                scene bg beach
                if beach_choice == "topless":
                    show minami swimsuit topless normal at left
                    if samantha.flags.sexyswimsuit:
                        show samantha swimsuit normal
                    else:
                        show samantha swimsuit topless normal
                    show lexi swimsuit topless normal at right
                elif beach_choice == "naked":
                    show minami naked normal at left
                    show samantha naked normal
                    show lexi naked normal at right
                elif beach_choice == "free":
                    show minami swimsuit topless normal at left
                    show samantha swimsuit normal
                    show lexi naked normal at right
                else:
                    show minami swimsuit normal at left
                    show samantha swimsuit normal
                    show lexi swimsuit normal at right
                show minami annoyed at left
                minami.say "Oh no!"
                samantha.say "Wha..."
                show samantha annoyed
                samantha.say "Darn it!"
                lexi.say "Whoops!"
                lexi.say "Looks like you girls let it go all floppy!"
                show lexi happy at right
                lexi.say "You need to learnt to keep it nice and stiff!"
                $ lexi.love += 1
                $ minami.love -= 1
                $ samantha.love -= 1
        "Play volleyball":
            mike.say "You know..."
            mike.say "I feel like I need to get moving right now!"
            mike.say "Let's play some volleyball, wake ourselves up!"
            "Lexi and Sam look less than pleased with my choice."
            "But Minami leaps on her chance before they can speak up."
            minami.say "Yay!"
            minami.say "Let's go, big bro!"
            "Minami grabs my hand and yanks me to my feet."
            "And before I know it, she's dragging me across the sand."
            show lexi annoyed
            show samantha annoyed
            "Lexi and Sam follow behind, still muttering to each other."
            "But Minami's too eager to get onto the court to hear them."
            minami.say "Okay!"
            minami.say "We need to pick teams!"
            show lexi normal
            show minami normal
            show samantha normal
            menu:
                "Choose Minami":
                    mike.say "Bags being on Minami's team!"
                    show minami happy
                    minami.say "Okay, big bro - let's go get those losers!"
                    show lexi annoyed
                    lexi.say "Hey - I ain't no loser!"
                    show samantha annoyed
                    samantha.say "Less of the losers please!"
                    $ lexi.love -= 1
                    $ minami.love += 1
                    $ samantha.love -= 1
                    $ beach_event += 1
                "Choose Lexi":
                    mike.say "Bags being on Lexi's team!"
                    lexi.say "Alright!"
                    show lexi happy
                    lexi.say "Let's batter those losers!"
                    show minami annoyed
                    minami.say "Hey - that's mean!"
                    show samantha annoyed
                    samantha.say "Less of the losers please!"
                    $ lexi.love += 1
                    $ minami.love -= 1
                    $ samantha.love -= 1
                "Choose Samantha":
                    if samantha.flags.nickname == "cupcake":
                        mike.say "Bags being on Cupcake's team!"
                    else:
                        mike.say "Bags being on Sam's team!"
                    samantha.say "Good choice, [hero.name]!"
                    samantha.say "We'll show those two losers!"
                    show lexi annoyed
                    lexi.say "Hey - I ain't no loser!"
                    show minami annoyed
                    minami.say "Hey - that's mean!"
                    $ lexi.love -= 1
                    $ minami.love -= 1
                    $ samantha.love += 1
                "Me against them":
                    mike.say "I'll take all three of you guys on!"
                    lexi.say "WHAT?!?"
                    show lexi surprised
                    lexi.say "Are you crazy?"
                    minami.say "He must be!"
                    show minami hunt
                    minami.say "We're gonna beat you, big bro!"
                    samantha.say "Three on one?"
                    show samantha annoyed
                    samantha.say "There's no way you can win!"
                    $ lexi.love += 1
                    $ minami.love += 1
                    $ samantha.love += 1
                    $ beach_event -= 1
            "Once what passes for trash-talk is over we start playing in earnest."
            scene bg black
            if beach_choice in ["naked", "free"]:
                show beach volleyball lexi naked
            else:
                show beach volleyball lexi swimsuit
            "And one thing that I soon realise is that the girls are way better than me!"
            scene bg black
            if beach_choice == "naked":
                show beach volleyball minami naked
            else:
                show beach volleyball minami swimsuit
            "I don't know if it's because I'm still sluggish from dropping off earlier."
            scene bg black
            if beach_choice == "naked":
                show beach volleyball samantha naked
            else:
                show beach volleyball samantha swimsuit
            "Or else they're just superior volleyball players."
            "But either way I end up face down in the sand most of the time."
            "Pulling my head up and spitting out sand, I beg for mercy."
            mike.say "Okay, okay..."
            mike.say "That's enough - I surrender!"
            "I have no idea of what the scores were or who won."
            "I'm just happy to know that my torture is over."
        "Play in the sea":
            mike.say "Geez..."
            mike.say "I didn't realise it was this hot!"
            if samantha.flags.nickname == "cupcake":
                mike.say "Cupcake's right - we should cool off in the sea."
            else:
                mike.say "Sam's right - we should cool off in the sea."
            "Sam wastes no time in getting up and grabbing me by the hand."
            show samantha happy
            "She has me on my feet before Lexi and Minami can protest."
            "And then she's dragging me across the sand towards the water."
            show lexi annoyed
            show minami annoyed
            "I can hear the others muttering as they follow in her wake."
            "But Sam simply ignores them and I can't hear a word either."
            samantha.say "Come on, [hero.name]."
            samantha.say "Last one in's a loser!"
            mike.say "Whoa..."
            mike.say "Wait a minute..."
            "Sam doesn't listen to me for a second."
            "Instead she pulls me straight into the water."
            "I leap and curse as she does so."
            "And that's because the water's freezing!"
            "Without thinking of the consequences, I reach down into the waves."
            if beach_choice == "naked":
                show playing water samantha naked
            else:
                show playing water samantha
            "Then I splash Sam with as much water as I can throw at her."
            samantha.say "Aah..."
            samantha.say "Oh my god!"
            samantha.say "That's so cold!"
            "Before I can say a word, Sam hears the sound of laughter behind her."
            if beach_choice in ["naked", "free"]:
                show playing water lexi naked
            else:
                show playing water lexi
            "She turns to see Lexi and Minami standing in the water a few feet away."
            if beach_choice == "naked":
                show playing water minami naked
            else:
                show playing water minami
            "Both of them are pointing and giggling."
            "But neither of them is quick enough to escape Sam's revenge."
            "She reaches down just like I did, and splashes them too."
            lexi.say "Wha..."
            lexi.say "Jesus fucking Christ!"
            if beach_choice == "naked":
                show playing water samantha naked
            else:
                show playing water samantha
            minami.say "Ooh...oh no..."
            minami.say "Help me, big bro!"
            "I smile wickedly as I do the exact opposite."
            if beach_choice == "naked":
                show playing water minami naked
            else:
                show playing water minami
            "I join Sam in her efforts to soak Lexi and Minami."
            "It doesn't take long for them to fight back."
            if beach_choice in ["naked", "free"]:
                show playing water lexi naked
            else:
                show playing water lexi
            "And soon enough we're involved in a four-way water fight."
            "Hostilities only come to an end when we're all exhausted."
            "And while we may have managed to cool down, we're more tired than when we started."
            $ lexi.love -= 1
            $ minami.love -= 1
            $ samantha.love += 1
            $ beach_event += 1
        "Go for a stroll" if hero.charm >= 80:
            mike.say "Those are all great ideas."
            mike.say "But I feel like I need to wake myself up."
            mike.say "I'm going to go for a stroll down the beach."
            mike.say "And you guys are all welcome to come along too."
            "The girls exchange unhappy glances at this."
            show lexi annoyed
            show minami annoyed
            show samantha annoyed
            "But my mind's already made up, so I just get to my feet."
            "And by the time I'm ready to go, they've changed their tunes."
            lexi.say "Are you sneaking off somewhere fun?"
            show lexi flirt
            lexi.say "Because if you are, then I want in on it!"
            minami.say "Don't leave me behind, big bro!"
            show minami hunt
            minami.say "I want to come along too."
            samantha.say "Well, I suppose I could so with stretching my legs."
            show samantha flirt
            samantha.say "Count me in too!"
            "I can't help treating myself to a sly smile as they rush to follow."
            "But I also make sure it's long gone before any of them see it too."
            "I was never intending to go on some kind of crazy endurance hike."
            "Just to walk the length of the beach and take in the atmosphere."
            "And pretty soon the others seem to see the benefits of doing so."
            "We take our time, going from one end of the beach to the other and then back again."
            "And by the time we make it back to our spot, everyone seems to have chilled out nicely."
            $ lexi.love += 1
            $ minami.love += 1
            $ samantha.love += 1
            $ beach_event += 1
        "Take a nap" if hero.charm < 80:
            mike.say "You guys can please yourselves."
            mike.say "I'm going back to sleep!"
            "With that, I lie back down and close my eyes."
            "And it doesn't take long for me to hear the fallout."
            lexi.say "Urgh..."
            show lexi annoyed
            lexi.say "What a lazy asshole!"
            show minami annoyed
            minami.say "Yeah, big bro can be a pain in the hole sometimes!"
            samantha.say "He doesn't look like he's joking this time."
            show samantha annoyed
            samantha.say "We'd best forget about him..."
            "Slowly and surely the sound of their voices begins to fade away."
            "I don't know if they're wandering away from me."
            "Or if it's because I'm drifting off to sleep."
            "Either way it looks good for me getting some rest."
            $ lexi.sub += 1
            $ minami.sub += 1
            $ samantha.sub += 1
            $ beach_event -= 1
    scene bg beach
    if beach_choice == "topless":
        show minami swimsuit topless normal at left
        if samantha.flags.sexyswimsuit:
            show samantha swimsuit normal
        else:
            show samantha swimsuit topless normal
        show lexi swimsuit topless normal at right
    elif beach_choice == "naked":
        show minami naked normal at left
        show samantha naked normal
        show lexi naked normal at right
    elif beach_choice == "free":
        show minami swimsuit topless normal at left
        show samantha swimsuit normal
        show lexi naked normal at right
    else:
        show minami swimsuit normal at left
        show samantha swimsuit normal
        show lexi swimsuit normal at right
    "As the day goes on, the sun climbs ever higher into the sky."
    "And soon enough, I feel like I'm lying on a grill, being roasted alive!"
    "Everyone put their sun-block on when we got here."
    "But almost as one we seem to realise that it's time for another layer."
    "I'm just about to slap some more on when I hear a voice to my side."
    lexi.say "Oh, [hero.name]..."
    show lexi flirt
    lexi.say "Would you be a hero and rub some of this into me?"
    "I look round to see Lexi holding out her sun-cream."
    "But more importantly, she's flaunting herself as she does so!"
    "Every inch of her body is already glistening in the rays of the sun."
    "And of course I want to run sun-cream into her!"
    "Who wouldn't?!?"
    minami.say "Erm..."
    show minami tehe
    minami.say "Big bro..."
    minami.say "Could you do me first?"
    "The sound of Minami's voice makes me turn my head."
    "And then the sight of her hits me right between the eyes."
    "She's a totally different shape and size to Lexi."
    "But she still manages to make my throat go dry with desire too."
    samantha.say "No, no, no..."
    show samantha flirt
    samantha.say "He should take care of me first!"
    "I hardly have to guess what awaits me as I turn around again."
    "Of course it's the sight of Sam."
    "Sexy, beautiful and incredibly hot Sam."
    "Yet another girl demanding that I put my hands on her body!"
    "This is getting ridiculous!"
    "As one they seem to crawl closer to me."
    show lexi normal
    show minami normal
    show samantha normal
    "Like a trio of sirens, all offering me sun-cream."
    "What the hell am I going to do?!?"
    menu:
        "Apply sunscreen on Lexi":
            mike.say "Well, you did ask first, Lexi!"
            "I take the sun-cream from Lexi's hand."
            "And she gives the others a triumphant smile."
            lexi.say "Mmm..."
            show lexi flirt
            lexi.say "This is going to feel SO good!"
            show minami annoyed
            show samantha annoyed
            "I get to work squeezing out the sun-cream and rubbing it into Lexi's skin."
            if beach_choice in ["naked", "free"]:
                show beach cream lexi naked
            else:
                show beach cream lexi swimsuit
            "And I must be doing a pretty good job, because she moans and sighs the whole time."
            "I begin at her shoulders and work my way down until I reach her feet."
            "Every inch of the way I make sure that I cover all the skin on show."
            "I keep telling myself that I'm just doing Lexi a favour here."
            "But deep down I know that there's much more to it than that."
            "Every second that my hands spend touching her turns me on even more."
            "And by the time that I'm done, all I can think about is taking it to the next step."
            "Which is really inconvenient when we're surrounded by all these other people!"
            "So instead I lie back down on my towel and try to think of something else."
            "That and keep trying to hide just how hard my cock is right now..."
            $ lexi.love += 1
            $ minami.love -= 1
            $ samantha.love -= 1
        "Apply sunscreen on Minami":
            mike.say "Well, you are the youngest, Minami."
            mike.say "And that means your skin's the most delicate."
            mike.say "So you should go first."
            "I take the sun-cream from Minami's hand."
            show minami tehe
            "And she gives the others a triumphant smile."
            show lexi annoyed
            show samantha annoyed
            minami.say "You know best, big bro."
            minami.say "This is going to feel SO good!"
            "I get to work squeezing out the sun-cream and rubbing it into Minami's skin."
            if beach_choice == "naked":
                show beach cream minami naked
            else:
                show beach cream minami swimsuit
            "And I must be doing a pretty good job, because she moans and sighs the whole time."
            "I begin at her shoulders and work my way down until I reach her feet."
            "Every inch of the way I make sure that I cover all the skin on show."
            "I keep telling myself that I'm just doing Minami a favour here."
            "But deep down I know that there's much more to it than that."
            "Every second that my hands spend touching her turns me on even more."
            "And by the time that I'm done, all I can think about is taking it to the next step."
            "Which is really inconvenient when we're surrounded by all these other people!"
            "So instead I lie back down on my towel and try to think of something else."
            "That and keep trying to hide just how hard my cock is right now..."
            $ lexi.love -= 1
            $ minami.love += 1
            $ samantha.love -= 1
        "Apply sunscreen on Samantha":
            if samantha.flags.nickname == "cupcake":
                mike.say "Well, you are lying nearest to me, Cupcake!"
            else:
                mike.say "Well, you are lying nearest to me, Sam!"
            mike.say "So it makes sense I do you first."
            "I take the sun-cream from Sam's hand."
            show samantha flirt
            "And she gives the others a triumphant smile."
            show lexi annoyed
            show minami annoyed
            samantha.say "Aw, thank you, [hero.name]."
            samantha.say "This is going to feel SO good!"
            "I get to work squeezing out the sun-cream and rubbing it into Sam's skin."
            if beach_choice == "naked":
                show beach cream samantha naked
            else:
                show beach cream samantha swimsuit
            "And I must be doing a pretty good job, because she moans and sighs the whole time."
            "I begin at her shoulders and work my way down until I reach her feet."
            "Every inch of the way I make sure that I cover all the skin on show."
            "I keep telling myself that I'm just doing Sam a favour here."
            "But deep down I know that there's much more to it than that."
            "Every second that my hands spend touching her turns me on even more."
            "And by the time that I'm done, all I can think about is taking it to the next step."
            "Which is really inconvenient when we're surrounded by all these other people!"
            "So instead I lie back down on my towel and try to think of something else."
            "That and keep trying to hide just how hard my cock is right now..."
            $ lexi.love -= 1
            $ minami.love -= 1
            $ samantha.love += 1
        "Apply sunscreen on all of them" if hero.charm >= 95:
            mike.say "Well, as all three of you asked at once..."
            mike.say "I guess it's only fair that I do all three of you at once too!"
            "For some reason, this doesn't make the girls bicker like I thought it might."
            "Instead they begin giggle to each other and hurry to lie down in a row."
            "Snatching up my own sun-cream, I squeeze a large blob onto my hand."
            "And then I take a deep breath, steeling myself for the task ahead of me."
            "I get straight to work rubbing it into their skin."
            show beach cream minami
            "And I must be doing a pretty good job, because they moan and sigh the whole time."
            if beach_choice in ["naked", "free"]:
                show beach cream lexi naked
            else:
                show beach cream lexi swimsuit
            "I begin at the shoulders and work my way down until I reach the feet."
            if beach_choice == "naked":
                show beach cream samantha naked
            else:
                show beach cream samantha swimsuit
            "Every inch of the way I make sure that I cover all the skin on show."
            "And I'm sure to give each girl an equal amount of care and attention too."
            show beach cream minami
            "I keep telling myself that I'm just doing them a favour here."
            if beach_choice in ["naked", "free"]:
                show beach cream lexi naked
            else:
                show beach cream lexi swimsuit
            "But deep down I know that there's much more to it than that."
            if beach_choice == "naked":
                show beach cream minami naked
            else:
                show beach cream minami swimsuit
            "Every second that my hands spend touching them turns me on even more."
            "And by the time that I'm done, all I can think about is taking it to the next step."
            "Which is really inconvenient when we're surrounded by all these other people!"
            "So instead I lie back down on my towel and try to think of something else."
            "That and keep trying to hide just how hard my cock is right now..."
            $ lexi.love += 1
            $ minami.love += 1
            $ samantha.love += 1
            $ beach_event += 2
        "I need some cream too" if hero.charm < 95:
            mike.say "Argh..."
            mike.say "My muscles are SO sore!"
            mike.say "It must have been from driving you all here..."
            show lexi surprised
            lexi.say "HUH?!?"
            show minami surprised
            minami.say "You can't be serious, big bro!"
            show samantha surprised
            samantha.say "I don't believe what I'm hearing!"
            mike.say "It's the truth guys!"
            mike.say "You're going to have to rub sun-cream on ME!"
            mike.say "Or else I don't think I can manage to drive us home!"
            "The girls exchange irritated glances, shaking their heads."
            "I'm pretty sure they can tell I'm lying."
            "But they don't seem to be about to call me on it."
            lexi.say "Whatever, [hero.name]!"
            show lexi annoyed
            lexi.say "Gimmie that!"
            "Lexi snatches my sun-cream and squeezes some onto her hands."
            "For a moment I think that I've won, that I'm a genius."
            "But then she begins to rub it in, and I feel the first twinges of pain."
            mike.say "OW!"
            mike.say "Hey, what are you doing?!?"
            lexi.say "Some little tricks I picked up when I worked in a massage parlour."
            show lexi wink
            lexi.say "Don't worry, they'll loosen you up a treat!"
            show minami hunt
            show samantha normal
            "Before I can object, Minami and Sam join in too."
            "What follows is the most painful massage I've ever experienced."
            "And if I wasn't sore and aching before, I certainly am when it finally comes to an end!"
            $ lexi.sub += 1
            $ minami.sub += 1
            $ samantha.sub += 1
            $ beach_event -= 2
    scene bg beach
    if beach_choice == "topless":
        show minami swimsuit topless normal at left
        if samantha.flags.sexyswimsuit:
            show samantha swimsuit normal
        else:
            show samantha swimsuit topless normal
        show lexi swimsuit topless normal at right
    elif beach_choice == "naked":
        show minami naked normal at left
        show samantha naked normal
        show lexi naked normal at right
    elif beach_choice == "free":
        show minami swimsuit topless normal at left
        show samantha swimsuit normal
        show lexi naked normal at right
    else:
        show minami swimsuit normal at left
        show samantha swimsuit normal
        show lexi swimsuit normal at right
    if beach_event >= 3:
        call home_harem_lexi_minami_samantha_beach_fuck_intro from _call_home_harem_lexi_minami_samantha_beach_fuck_intro
        call home_harem_lexi_minami_samantha_beach_blowjob from _call_home_harem_lexi_minami_samantha_beach_blowjob
        call home_harem_lexi_minami_samantha_beach_fuck from _call_home_harem_lexi_minami_samantha_beach_fuck
        $ lexi.love += 2
        $ minami.love += 2
        $ samantha.love += 2
        scene bg beach
        show minami naked normal at left
        show samantha naked normal
        show lexi naked normal at right
        if game.week_day % 2 == 0:
            "Pretty soon we're a mass of slick limbs and warm bodies, huddled together on the sand."
            "Everyone seems to be too spent to get up to anything more energetic that lying entangled together."
            "But I can feel warm breasts and still wet pussys against my naked skin."
            "And that's a pretty nice thing to feel when you're too exhausted to even move."
        else:
            "Afterwards, we take a quick dip into the sea to clean ourselves off."
            "And it feels good to wash off the sweat, waking myself up in the process."
            "I open my mouth to ask if they're finally ready to go home."
            "But to my surprise, they're already packing up their stuff."
            "Seems that everyone got what they wanted."
            "So there's no argument to be had."
    else:
        "Soon the sun is beginning to sink lower in the sky."
        "And as afternoon comes on, the heat becomes unbearable."
        "That's the point where we have to admit defeat and head for home."
        "We gather up our things and retrace our steps to the car."
        "We're hot, tired and more than a little red from the sun."
        "But I think we all got something out of our time on the beach today."
    $ game.pass_time(4)
    return

label home_harem_lexi_minami_samantha_beach_fuck_intro:
    if game.week_day % 2 == 0:
        "I'm just lying down on my towel to chill out for a while."
        "Soaking up the last few rays of the sun and listening to the sound of the sea."
        "But the moment I actually close my eyes, I hear the sound of someone coughing."
        "In fact, I hear the sound of three people coughing all at once!"
        "Opening one eye, I see three heads above me, blocking out the sun."
        "Lexi, Minami and Sam are all staring down at me."
        "And they look like they mean business too!"
        mike.say "Erm..."
        mike.say "Can I help you guys?"
        mike.say "I mean...we came to the beach to relax, right?"
        "The three of them exchange knowing glances and giggles."
        "Then they turn their attention back to me."
        lexi.say "We're done lying around in the sun, [hero.name]."
        lexi.say "Now we wanna do something more fun!"
        show lexi flirt
        minami.say "Yeah, something that's really exciting!"
        show minami tehe
        samantha.say "And I think you know what we mean..."
        show samantha flirt
        "As if she needs to make her point clear, Sam leans in closer."
        "And a moment later, her hand is creeping up my thigh."
        "I prop myself up on my elbows, looking this way and that."
        mike.say "Whoa..."
        mike.say "How long was I asleep?"
        mike.say "Everybody else has cleared out!"
        "Lexi doesn't waste any time cutting to the chase."
        "She puts her hand straight onto my groin and starts to squeeze."
        lexi.say "Exactly, [hero.name]!"
        lexi.say "So there's nobody to see us fucking!"
        "Minami giggles at Lexi's shameless behaviour."
        "But instead of grabbing a piece of me for herself, she plants a kiss on my lips."
        minami.say "So what do you say, big bro?"
        mike.say "You know what..."
        mike.say "Let's do it!"
    else:
        "They say that the secret to a good time is knowing when you're through, when it's time to quit."
        "And that seems to make just as much sense when it comes to a day at the beach too."
        "Lexi, Minami, Sam and I got here nice and early today, beating the rush and bagging a great spot."
        "The weather held, and so we were able to do anything and everything we wanted with no trouble."
        "But now the sun is starting to get low in the sky, and there's a slight chill creeping in."
        "All of which makes me think it's time to pack up and head back home."
        mike.say "You guys ready to get moving?"
        mike.say "Because I feel like it's time to go back to the car."
        "The girls have are all spread out on the sand, soaking up the last of the sun."
        "At the sound of my voice they begin to stir slowly, heads turning in my direction."
        show fx question at left
        minami.say "Huh?"
        minami.say "What was that, big bro?"
        samantha.say "Ooh..."
        samantha.say "I think he said it's time we were leaving."
        lexi.say "Urgh..."
        show lexi annoyed
        lexi.say "Who woke me up?!?"
        lexi.say "'Cos they're asking for a split lip!"
        "I shake my head at the mixed reactions from the girls."
        "And I decide to chalk it up to the fact they've been roused from slumber."
        if samantha.flags.nickname == "cupcake":
            mike.say "Got it in one, Cupcake."
        else:
            mike.say "Got it in one, Sam."
        mike.say "Time's getting on - so maybe we should pack up?"
        mike.say "I've still got to drive you guys home, remember?"
        "Sam seems to be okay with the idea of going home."
        "But Lexi and Minami are less keen."
        show lexi flirt
        "I can hear them muttering and moaning to each other."
        show minami tehe
        mike.say "Hey!"
        mike.say "What are you two talking about?"
        mike.say "Don't make me leave you to walk back home!"
        show minami normal
        minami.say "Okay, big bro, okay!"
        show lexi normal
        lexi.say "Yeah, don't be such a douche, [hero.name]!"
        minami.say "We were just saying..."
        minami.say "Isn't there time to do one last thing?"
        show lexi flirt
        lexi.say "Yeah, like something really fun!"
        "At the mention of fun, I see Sam begin to show interest."
        "She props herself up on one elbow, raising her eyebrows at the same time."
        samantha.say "Now I'm intrigued!"
        show samantha flirt
        samantha.say "Exactly what did you have in mind?"
        "Lexi nudges Minami in the ribs and nods eagerly."
        "But Minami suddenly blushes and looks away."
        minami.say "I..."
        show minami scared
        minami.say "I don't want to say!"
        lexi.say "For fuck's sake!"
        show lexi normal
        lexi.say "We want to give [hero.name] a reward for driving us to the beach and back home."
        samantha.say "That sounds like a great idea!"
        "Suddenly all three of them are staring at me."
        mike.say "Th...that sounds great!"
        mike.say "I'm sure it'd give me all the energy I need for the drive back!"
    "The girls laugh and clap their hands, starting to get naked."
    show lexi naked
    show minami naked
    show samantha naked
    "I pull off my shorts too, my cock already starting to get hard."
    "Everyone's starting to warm to the idea, casting glances here and there."
    return

label home_harem_lexi_minami_samantha_beach_blowjob:
    show lexi normal
    lexi.say "But the thing is, you gotta choose!"
    show minami normal
    minami.say "That's right, big bro - who's going to do it?"
    show samantha normal
    samantha.say "Which one of us gets to suck your cock?"
    menu:
        "Choose Lexi":
            "I look at each of the girls in turn, weighing up the possibilities."
            "Minami looks intriguingly innocent right now, but maybe a little shy."
            "And Sam seems more than game, but she wasn't the one that came up with the idea."
            "But Lexi, on the other hand, fits the bill perfectly."
            "She's up for it, and she has one hell of a filthy mouth too."
            "All the more reason to put it to good use!"
            "I leap to my feet and look straight at Lexi."
            mike.say "Lexi..."
            mike.say "I choose you."
            mike.say "Now get over here..."
            mike.say "And get my cock in your mouth!"
            show lexi flirt
            "Lexi doesn't seem in the least bit offended by my demand."
            "Instead she has a nonchalant smile on her face."
            "Lexi gets onto her hands and knees."
            scene bj leximinamisam
            show bj leximinamisam lexifront minamileft samantharight
            with fade
            "And she crawls slowly towards me."
            "Watching her come over here and thinking about what she's going to do..."
            "Well, let's just say that it's had a visible effect on my manhood!"
            "Lexi lets out a filthy giggle as my cock pops up and bobs in front of her face."
            lexi.say "Well, will you look at that!"
            lexi.say "I feel hungry all of a sudden - hungry for cock!"
            "Lexi doesn't say another word after that."
            "Instead she leans forwards and gets down to business."
            "Lexi cups my balls with one hand and grabs the shaft with the other."
            "Wherever her fingers aren't touching me, I swear I can feel her tongue."
            "She works her way upwards, not hurrying in the slightest."
            "And pretty soon I'm panting like I've run a marathon!"
            "I watch as she inches her way higher, finally reaching the top."
            "Then she all but pounces on it, swallowing the head whole!"
            show bj leximinamisam blowjob
            "I stumble and almost fall over as Lexi's head bobs up and down."
            "And it's then that I see Minami and Sam haven't been idle either."
            "The former is laid on her back, legs spread wide apart."
            "The latter has her head between them, licking away with intent."
            "While Sam can't see a thing, Minami's staring straight at me."
            "Her eyes are wide and filled with what looks like amazement."
            show bj leximinamisam blowjob titjob
            "But I can't tell if it's from what's being done to her right now."
            "Or else the fact that she's watching what Lexi's doing to me."
            "Either way, I stare back, feeling the sight turn me on even more."
            "Minami and I are both getting oral, and watching each other at the same time!"
            "I feel like we're synchronising somehow, settling into a rhythm."
            "And when I see Minami twitching like she's about to cum, I follow her lead."
            menu:
                "Cum in her mouth":
                    "For the first time since she started blowing me, Lexi's eyes pop open."
                    show bj leximinamisam blowjob cum lexiinmouth with vpunch
                    "And that's because I just blew my load straight down her throat!"
                    with vpunch
                    "But she's more than experienced when it comes to that kind of thing."
                    with vpunch
                    "So she recovers swiftly, swallowing every spurt of cum that I can manage."
                    "Lexi's breathing sounds a little laboured as I pull out of her mouth."
                    show bj leximinamisam -blowjob -cum
                    "And strings of cum trail from the head of my cock to her lips."
                "Cum on her face":
                    "For the first time since she started blowing me, Lexi's eyes pop open."
                    show bj leximinamisam -blowjob
                    "And that's because I just dragged my cock out of her mouth."
                    show bj leximinamisam cumshot with vpunch
                    "A moment later I blow my load straight into her face."
                    with vpunch
                    "But it's not like this is the first time that's happened to Lexi."
                    show bj leximinamisam -cumshot cum lexionface with vpunch
                    "And she recovers swiftly, letting the cum spatter over her features."
                    "In fact, she looks like she's kind of enjoying the hot, sticky shower."
        "Choose Minami":
            "I look at each of the girls in turn, weighing up the possibilities."
            "Lexi looks delightfully dirty right now, but maybe she's too obvious."
            "And Sam seems more than game, but she wasn't the one that came up with the idea."
            "But Minami, on the other hand, fits the bill perfectly."
            "She's shy and nervous, all of which makes me want her all the more."
            "And that mouth, I can put it to good use!"
            "I leap to my feet and look straight at Minami."
            mike.say "Minami..."
            mike.say "I choose you."
            mike.say "Now get over here..."
            mike.say "And get my cock in your mouth!"
            "Minami seems more than a little surprised by my demand."
            show minami surprised
            "She looks at the other girls, and gets a round of nods."
            show minami tehe
            "Then she gets onto her hands and knees."
            "And she crawls slowly towards me."
            scene bj leximinamisam
            show bj leximinamisam minamifront lexiright samanthaleft
            with fade
            "Watching her come over here and thinking about what she's going to do..."
            "Well, let's just say that it's had a visible effect on my manhood!"
            "Minami lets out a yelp of surprise as my cock pops up and bobs in front of her face."
            minami.say "Oh...big bro..."
            minami.say "Your cock..."
            minami.say "It's so big!"
            "Minami doesn't say another word after that."
            "In fact, she seems almost hypnotised by the sight of my manhood!"
            "Instead she leans forwards and gets down to business."
            "Minami cups my balls with one hand and grabs the shaft with the other."
            "Wherever her fingers aren't touching me, I swear I can feel her tongue."
            "She works her way upwards, not hurrying in the slightest."
            "And pretty soon I'm panting like I've run a marathon!"
            "I watch as she inches her way higher, finally reaching the top."
            "Then she all but pounces on it, swallowing the head whole!"
            show bj leximinamisam blowjob
            "I stumble and almost fall over as Minami's head bobs up and down."
            "And it's then that I see Sam and Lexi haven't been idle either."
            "The former is laid on her back, legs spread wide apart."
            "The latter has her head between them, licking away with intent."
            "While Lexi can't see a thing, Sam's staring straight at me."
            "Her eyes are wide and filled with what looks like amazement."
            show bj leximinamisam blowjob handjob
            "But I can't tell if it's from what's being done to her right now."
            "Or else the fact that she's watching what Minami's doing to me."
            "Either way, I stare back, feeling the sight turn me on even more."
            "Sam and I are both getting oral, and watching each other at the same time!"
            "I feel like we're synchronising somehow, settling into a rhythm."
            "And when I see Sam twitching like she's about to cum, I follow her lead."
            menu:
                "Cum in her mouth":
                    "For the first time since she started blowing me, Minami's eyes pop open."
                    with vpunch
                    "And that's because I just blew my load straight down her throat!"
                    show bj leximinamisam blowjob cum minamiinmouth with vpunch
                    "She's not the most experienced of girls, not by a long way."
                    with vpunch
                    "So she recovers swiftly, swallowing every spurt of cum that I can manage."
                    "Minami's breathing sounds a little laboured as I pull out of her mouth."
                    show bj leximinamisam -blowjob -cum
                    "And strings of cum trail from the head of my cock to her lips."
                "Cum on her face":
                    "For the first time since she started blowing me, Minami's eyes pop open."
                    show bj leximinamisam -blowjob
                    "And that's because I just dragged my cock out of her mouth."
                    show bj leximinamisam cumshot with vpunch
                    "A moment later I blow my load straight into her face."
                    with vpunch
                    "Minami just kneels there in front of me, eyes wide with shock."
                    show bj leximinamisam -cumshot cum minamionface with vpunch
                    "She stays still as a statue, letting the cum spatter over her features."
                    "But she looks like she's kind of enjoying the hot, sticky shower."
        "Choose Sam":
            "I look at each of the girls in turn, weighing up the possibilities."
            "Minami looks intriguingly innocent right now, but maybe a little shy."
            "Lexi looks delightfully dirty right now, but maybe she's too obvious."
            "But Sam, she's up for it, and she didn't even come up with the idea!"
            "That makes me want to choose her all the more."
            "She's up for it, and she has one hell of a talented mouth too."
            "All the more reason to put it to good use!"
            "I leap to my feet and look straight at Sam."
            if samantha.flags.nickname == "cupcake":
                mike.say "Cupcake..."
            else:
                mike.say "Sam..."
            mike.say "I choose you."
            mike.say "Now get over here..."
            mike.say "And get my cock in your mouth!"
            show samantha flirt
            "Sam doesn't seem in the least bit offended by my demand."
            "Instead she has a cheeky smile on her face."
            "Sam gets onto her hands and knees."
            "And she crawls slowly towards me."
            scene bj leximinamisam
            show bj leximinamisam samanthafront minamileft lexiright
            with fade
            "Watching her come over here and thinking about what she's going to do..."
            "Well, let's just say that it's had a visible effect on my manhood!"
            "Lexi lets out a filthy giggle as my cock pops up and bobs in front of her face."
            samantha.say "Oh my - will you look at that!"
            samantha.say "It's already standing up for me!"
            "Sam doesn't say another word after that."
            "Instead she leans forwards and gets down to business."
            "Lexi cups my balls with one hand and grabs the shaft with the other."
            "Wherever her fingers aren't touching me, I swear I can feel her tongue."
            "She works her way upwards, not hurrying in the slightest."
            "And pretty soon I'm panting like I've run a marathon!"
            "I watch as she inches her way higher, finally reaching the top."
            "Then she all but pounces on it, swallowing the head whole!"
            show bj leximinamisam blowjob
            "I stumble and almost fall over as Sam's head bobs up and down."
            "And it's then that I see Minami and Lexi haven't been idle either."
            "The former is laid on her back, legs spread wide apart."
            "The latter has her head between them, licking away with intent."
            "While Lexi can't see a thing, Minami's staring straight at me."
            "Her eyes are wide and filled with what looks like amazement."
            show bj leximinamisam blowjob titjob
            "But I can't tell if it's from what's being done to her right now."
            "Or else the fact that she's watching what Sam's doing to me."
            "Either way, I stare back, feeling the sight turn me on even more."
            "Minami and I are both getting oral, and watching each other at the same time!"
            "I feel like we're synchronising somehow, settling into a rhythm."
            "And when I see Minami twitching like she's about to cum, I follow her lead."
            menu:
                "Cum in her mouth":
                    "For the first time since she started blowing me, Sam's eyes pop open."
                    show bj leximinamisam blowjob cum samanthainmouth with vpunch
                    "And that's because I just blew my load straight down her throat!"
                    with vpunch
                    "But she's no novice when it comes to that kind of thing."
                    with vpunch
                    "So she recovers swiftly, swallowing every spurt of cum that I can manage."
                    "Sam's breathing sounds a little laboured as I pull out of her mouth."
                    show bj leximinamisam -blowjob -cum
                    "And strings of cum trail from the head of my cock to her lips."
                "Cum on her face":
                    "For the first time since she started blowing me, Sam's eyes pop open."
                    show bj leximinamisam -blowjob
                    "And that's because I just dragged my cock out of her mouth."
                    show bj leximinamisam cumshot with vpunch
                    "A moment later I blow my load straight into her face."
                    show bj leximinamisam -cumshot cum samanthaonface with vpunch
                    "But it's not like this is the first time that's happened to Sam."
                    with vpunch
                    "And she recovers swiftly, letting the cum spatter over her features."
                    "In fact, she looks like she's kind of enjoying the hot, sticky shower."
    return

label home_harem_lexi_minami_samantha_beach_fuck:
    "The only problem is that I can't fuck all three of them at once!"
    "So I decide to go with the closest and cutest."
    "As soon as she's naked, I grab Minami and pull her in close."
    "She lets out a cute little yelp of surprise."
    "But then she nestles herself into my arms, giggling as she does so."
    scene foursome leximinamisam
    show foursome leximinamisam beach
    with fade
    minami.say "Does this mean what I think it means, big bro?"
    minami.say "Do I get this all to myself?"
    "As if to make her intentions clear, I feel Minami stroking my cock."
    "It was already starting to stir to life, but her touch finishes the job."
    "By way of answer, I kiss Minami full on the lips."
    "She melts into it, tongues darting here and there."
    "And my hand finds its way between her legs at the same time."
    "Minami moans through the kiss as I trace the folds down there."
    "Her neat little pussy is already wet to the touch."
    "She offers no resistance as I pull her onto my lap."
    "But now I have to decide what I'm going to do with her..."
    menu:
        "Fuck her pussy":
            "The answer comes quite naturally almost as soon as Minami's sat astride me."
            "My cock finds its way between her thighs and begins to rub against what's hidden down there."
            "Minami's already pretty excited, so I find her wet and slick."
            "Which means the head of my cock slides down the lips of her pussy."
            minami.say "Oh my..."
            minami.say "That feels so nice, big bro!"
            minami.say "Can I have some more?"
            "By now I have my hands firmly on Minami's haunches."
            "And her petite frame means that I'm totally in control."
            mike.say "Sure, Minami..."
            mike.say "You can have the whole thing."
            mike.say "As much as you can handle!"
            show foursome leximinamisam vaginal
            "I punctuate the statement by pulling Minami downwards and on to me."
            "My aim is almost perfect, meaning her pussy squares up with my cock."
            "I feel her muscles resist me for a moment, and hear Minami gasping at the sensation."
            "But soon enough they surrender to the inevitable and she begins to slowly sink down."
            "I keep things slow and steady, only letting my cock inch its way into her."
            "And this makes sure that Minami feels every moment of the process."
            "Watching her moan and whimper with pleasure is almost as good as how it feels."
            "But not quite as nice as feeling Minami's pussy swallow me a little at a time."
            "Finally, it fills her completely, and she's hanging there helpless."
            "I let Minami wriggle around for a few moments, enjoying the show."
            minami.say "Mmm..."
            minami.say "You're so big!"
            minami.say "You filled me up, big bro!"
            "I allow myself a wicked grin, at Minami's flattering words."
            "But then I start to move inside of her, thrusting from below."
            "Almost the same moment I do so, her words fade into mere sounds."
            "It's like the sensation is enough to rob Minami of the ability to speak."
            "Instead she closes her eyes and begins to gasp as she rides my cock."
            "At first I can't believe the sheer amount of noise Minami's making."
            "But then I realise I'm hearing more than one person making the sounds."
            "I glance around to see that Lexi and Sam are mere inches away on the sand."
            show foursome leximinamisam lexi samantha with dissolve
            "Believe it or not, I'd actually forgotten they were there!"
            "Minami had one hundred percent of my attention all this time."
            "But now that I can see what they're doing, all that changes."
            "Sam and Lexi have their legs intertwined, their bodies pressed together."
            "And they're rubbing against each other with what looks like genuine desperation."
            "Their eyes are fixed on Minami and me, watching our every move."
            "All the time they're rubbing their pussys together too!"
            show foursome leximinamisam lexi samantha lexifingering
            "I can't actually believe what I'm seeing."
            "The sight is so incredibly hot!"
            "Without realising it, I'm pounding Minami ever faster."
            "My body's over whelmed by the sensation of fucking her."
            "And my mind's filled with the sight of Lexi and Sam too."
            "I honestly don't know which way to turn!"
            "As I watch them, Lexi begins to moan and buck against Sam."
            "I realise that she's starting to cum, helpless to resist."
            "Then Sam starts to do the same thing, as if in sympathy."
            minami.say "Oh fuck, big bro..."
            minami.say "That is...SO hot!"
            minami.say "I think..."
            minami.say "Ooh...I think I'm gonna cum too!"
            "I realise she's right."
            "Minami's wriggling around on my cock like crazy!"
            "And she's going to take me with her too!"
            menu:
                "Cum inside":
                    "Minami wanted as much of this as she could get."
                    "So pulling out before the end would be kind of like cheating her, right?"
                    "That's why I keep right on going as I feel myself start to lose it."
                    with vpunch
                    "I have a firm hold on Minami as I shoot my load into her."
                    show foursome leximinamisam creampie ahegao with vpunch
                    "And I make sure to keep it up as she squeals from the sensation."
                    with vpunch
                    "Pretty soon it's starting to seep out of her around my cock."
                    "Running down the inside of her thighs as she pants in helpless desperation."
                "Pull out":
                    "I think Minami's had enough cock to satisfy her."
                    "So I pull out of her pussy before it's too late."
                    "She squirms and moans, trying to protest."
                    show foursome leximinamisam -vaginal
                    "But I ignore her and slide my cock out of her pussy."
                    show foursome leximinamisam cumshot with vpunch
                    "A moment later I lose it, shooting my load over her buttocks."
                    show foursome leximinamisam -cumshot cum with vpunch
                    "Minami gasps in helpless desperation as it runs down her legs."
        "Fuck her ass":
            "The answer comes quite naturally almost as soon as Minami's sat astride me."
            "My cock finds its way between her buttocks and begins to rub against what's hidden in there."
            "Minami's already pretty excited, but her ass is still tight."
            "Which means the head of my cock presses against it without getting any further."
            minami.say "Oh my..."
            minami.say "That feels so nice, big bro!"
            minami.say "Can I have some more?"
            "By now I have my hands firmly on Minami's haunches."
            "And her petite frame means that I'm totally in control."
            mike.say "Sure, Minami..."
            mike.say "You can have the whole thing."
            mike.say "As much as you can handle!"
            "I punctuate the statement by pulling Minami downwards and on to me."
            "My aim is almost perfect, meaning her ass squares up with my cock."
            "I feel her muscles resist me, and hear Minami gasping at the sensation."
            minami.say "Big bro!"
            minami.say "That's my butt!"
            minami.say "You're putting it in my butt!"
            show foursome leximinamisam anal
            "But soon enough Minami surrenders to the inevitable and she begins to slowly sink down."
            "I keep things slow and steady, only letting my cock inch its way into her."
            "And this makes sure that Minami feels every moment of the process."
            "Watching her moan and whimper with pleasure is almost as good as how it feels."
            "But not quite as nice as feeling Minami's ass swallow me a little at a time."
            "Finally, it fills her completely, and she's hanging there helpless."
            "I let Minami wriggle around for a few moments, enjoying the show."
            minami.say "Mmm..."
            minami.say "You're so big!"
            minami.say "You filled me up, big bro!"
            "I allow myself a wicked grin, at Minami's flattering words."
            "But then I start to move inside of her, thrusting from below."
            "Almost the same moment I do so, her words fade into mere sounds."
            "It's like the sensation is enough to rob Minami of the ability to speak."
            "Instead she closes her eyes and begins to gasp as she rides my cock."
            "At first I can't believe the sheer amount of noise Minami's making."
            "But then I realise I'm hearing more than one person making the sounds."
            "I glance around to see that Lexi and Sam are mere inches away on the sand."
            show foursome leximinamisam lexi samantha with dissolve
            "Believe it or not, I'd actually forgotten they were there!"
            "Minami had one hundred percent of my attention all this time."
            "But now that I can see what they're doing, all that changes."
            "Sam and Lexi have their legs intertwined, their bodies pressed together."
            "And they're rubbing against each other with what looks like genuine desperation."
            "Their eyes are fixed on Minami and me, watching our every move."
            "All the time they're rubbing their pussys together too!"
            show foursome leximinamisam lexi samantha lexifingering
            "I can't actually believe what I'm seeing."
            "The sight is so incredibly hot!"
            "Without realising it, I'm pounding Minami ever faster."
            "My body's over whelmed by the sensation of fucking her."
            "And my mind's filled with the sight of Lexi and Sam too."
            "I honestly don't know which way to turn!"
            "As I watch them, Lexi begins to moan and buck against Sam."
            "I realise that she's starting to cum, helpless to resist."
            "Then Sam starts to do the same thing, as if in sympathy."
            minami.say "Oh fuck, big bro..."
            minami.say "That is...SO hot!"
            minami.say "I think..."
            minami.say "Ooh...I think I'm gonna cum too!"
            "I realise she's right."
            "Minami's wriggling around on my cock like crazy!"
            "And she's going to take me with her too!"
            menu:
                "Cum inside":
                    "Minami wanted as much of this as she could get."
                    "So pulling out before the end would be kind of like cheating her, right?"
                    "That's why I keep right on going as I feel myself start to lose it."
                    with vpunch
                    "I have a firm hold on Minami as I shoot my load into her."
                    show foursome leximinamisam creampie ahegao with vpunch
                    "And I make sure to keep it up as she squeals from the sensation."
                    with vpunch
                    "Pretty soon it's starting to seep out of her around my cock."
                    "Running down the inside of her thighs as she pants in helpless desperation."
                "Pull out":
                    "I think Minami's had enough cock to satisfy her."
                    "So I pull out of her ass before it's too late."
                    "She squirms and moans, trying to protest."
                    show foursome leximinamisam -anal
                    "But I ignore her and slide my cock out of her ass."
                    show foursome leximinamisam cumshot with vpunch
                    "A moment later I lose it, shooting my load over her buttocks."
                    show foursome leximinamisam -cumshot cum with vpunch
                    "Minami gasps in helpless desperation as it runs down her legs."
            $ minami.flags.anal += 1
    "Almost as soon as I'm done with my orgasm, Lexi and Sam come crawling over."
    "They don't ask permission, just begin wrapping themselves around Minami and me."
    $ minami.sexperience += 1
    return

label home_harem_samantha_sasha_beach_date(appointment=None):
    if not hero.has_motor_vehicle:
        mike.say "Sorry girls, my car is in the garage."
        mike.say "We'll have to postpone our trip to the beach."
        $ samantha.love -= 2
        $ sasha.love -= 2
        return
    "It's too nice of a day to spend it stuck in the house."
    "So I load up the car with the intention of heading to the beach."
    "I make it an open invitation for any of the girls to come along."
    "Sasha and Sam seem quite keen to jump in the car with me."
    "But the others are all busy doing one thing or another."
    "So that's how the three of us end up walking across the sand together."
    scene bg beach with fade
    $ game.room = "beach"
    "I'm looking out towards the sea, thinking about how cool it'll feel to get in there."
    "But my moment of quiet contemplation is ruined by the sound of raise voices behind me."
    show sasha angry swimsuit at right with moveinright
    sasha.say "I AM carrying my fair share!"
    sasha.say "And it's more than you are too!"
    show sasha annoyed
    show samantha angry swimsuit at top_mostright with moveinright
    samantha.say "That's a lie, and you know it!"
    samantha.say "You're always trying to shirk your responsibilities!"
    show samantha annoyed
    "I turn around to see Sasha and Sam bickering."
    "All the stuff they were carrying is in a pile around their feet."
    "What are they even thinking?"
    "We've only just walked out of the damn car park!"
    mike.say "What the hell, guys?!?"
    show sasha angry
    sasha.say "Sam's accusing me of not carrying enough stuff!"
    sasha.say "But my arms are already aching."
    sasha.say "Look - they're shaking from the effort!"
    show sasha annoyed
    show samantha angry
    samantha.say "She's lying, [hero.name]!"
    samantha.say "She deliberately chose all the light things to carry!"
    samantha.say "I might have less stuff - but it's much heavier!"
    show samantha annoyed
    "I let out a weary sigh and shake my head."
    "Do I really have to put up with this bullshit?"
    "Aren't they supposed to be a pair of grown women?"
    "Well, it looks like I'm going to have to sort it out."
    menu:
        "Side with Sasha":
            "Actually, now that I've had a chance to look at it, Sasha's right."
            "She's got one hell of a load to carry, and she's struggling with it too."
            mike.say "I see what you mean, Sasha!"
            mike.say "Let me take some of that for you..."
            show sasha happy
            "Sasha smiles sweetly as I relieve her of the largest part of her burden."
            "But Sam seems rather less than impressed by my show of chivalry."
            sasha.say "Thank you, [hero.name]."
            sasha.say "I never could have made it the whole way!"
            "I nod and smile as I shoulder Sasha's extra load."
            "And soon enough we're back trekking across the sand."
            $ samantha.love -= 1
            $ sasha.love += 1
            $ beach_event = 0
        "Side with Samantha":
            "Actually, now that I've had a chance to look at it, Sam's right."
            "The stuff that she's carrying is smaller, but it looks super heavy."
            if samantha.flags.nickname == "cupcake":
                mike.say "I see what you mean, Cupcake!"
            else:
                mike.say "I see what you mean, Sam!"
            mike.say "Let me take some of that for you..."
            show samantha happy
            "Sam smiles sweetly as I relieve her of the largest part of her burden."
            "But Sasha seems rather less than impressed by my show of chivalry."
            samantha.say "Thank you, [hero.name]."
            samantha.say "I never could have made it the whole way!"
            "I nod and smile as I shoulder Sam's extra load."
            "And soon enough we're back trekking across the sand."
            $ samantha.love += 1
            $ sasha.love -= 1
            $ beach_event = 0
        "Help them" if hero.fitness >= 75:
            "Actually, now that I've had a chance to look at it, they're both right."
            "Sasha's got one hell of a load to carry, and she's struggling with it too."
            "And the stuff that Sam's carrying is smaller, but it looks super heavy."
            "What kind of a man am I if I let either of them struggle on like that?"
            mike.say "You know, I think you're both right!"
            mike.say "Let me take care of that for you guys..."
            show samantha happy
            show sasha happy
            "As I struggle to shoulder all of the stuff, Sasha and Sam's mood seems to change."
            "They exchange glances, looking more than a little embarrassed."
            show sasha normal
            sasha.say "Actually, it's not that bad!"
            show samantha normal
            samantha.say "Yeah - we can manage most of it!"
            "I shake my head, puffing and panting as I take on the burden."
            mike.say "No..."
            mike.say "No...way..."
            mike.say "I...can...handle it!"
            "Soon we're back trekking across the sand."
            "Only now I'm sweating profusely with every step."
            "While Sasha and Sam look on, concern in their eyes."
            $ samantha.love += 1
            $ sasha.love += 1
            $ beach_event = 1
        "Let them carry everything" if hero.fitness < 75:
            "Actually, now that I've had a chance to look at it, they're both wrong!"
            "I'm carrying far more than either of them, and I'm not the one complaining."
            mike.say "What are you two even talking about?"
            mike.say "I'm the one laden down like a mule here!"
            "I drop everything that I'm carrying."
            "And it lands next to the stuff they've already dropped."
            mike.say "Change of plan - you two can carry everything."
            mike.say "I'm going on strike!"
            "With that, I turn my back on them and stride off across the sand."
            show sasha angry at right, startle
            sasha.say "HEY!"
            sasha.say "Get back here!"
            show samantha angry
            samantha.say "[hero.name], where are you going?"
            samantha.say "We can't carry all this stuff!"
            "I ignore their protests and begin to look for a spot on the beach."
            "And eventually Sasha and Sam seem to get the message."
            show sasha annoyed
            show samantha annoyed
            "They struggle to lift everything between them."
            "And then they hurry to follow me as best they can."
            "As I look back over my shoulder, I can't help smiling at their predicament."
            $ samantha.love -= 1
            $ sasha.love -= 1
            $ beach_event = -1
    show sasha normal swimsuit at left5
    show samantha normal swimsuit at right5
    with move
    "As soon as we've found a place to spread out our towels, we settle down."
    "And it's a relief to see that this seems to calm the tensions between Sasha and Sam."
    "I mean, who really wants to have an argument on a beautiful day like this?"
    "Far better to just lie back and relax on the sand, soaking up the sun."
    "And that's just what we do for the first hour or so."
    "In fact, I'm almost falling asleep when I hear Sasha and Sam talking."
    samantha.say "No way, Sasha."
    show samantha annoyed
    samantha.say "I'm already WAY too hot!"
    samantha.say "I want to cool down."
    sasha.say "We can do that later, Sam."
    show sasha annoyed
    sasha.say "I need to burn off some energy."
    sasha.say "I'm going to go crazy just sitting here!"
    "I prop myself up on my elbows and try to shake off the sleepiness."
    mike.say "Hmm..."
    mike.say "What's up?"
    "Sasha and Sam turn to look at me."
    samantha.say "I'm feel like I'm going to pass out, [hero.name]!"
    show samantha normal
    samantha.say "So I think we should go grab an ice cream, right?"
    sasha.say "Yeah, but I'm getting restless, [hero.name]!"
    show sasha normal
    sasha.say "I want to play volleyball."
    sasha.say "How about you?"
    "I can see that both of them want me to go for their preferred option."
    "So I rack my brains, trying to think which one sounds more appealing."
    menu:
        "Go grab an ice cream":
            "It's only now that I'm sitting up I realise that Sam's right."
            "It's almost too hot today, and I'm starting to feel it too."
            "There's no way I want to chase a frisbee around in heat like this!"
            mike.say "Maybe we could wait until it cools down a bit to play frisbee, Sasha?"
            if samantha.flags.nickname == "cupcake":
                mike.say "I feel like Cupcake - it's so hot I could faint!"
            else:
                mike.say "I feel like Sam - it's so hot I could faint!"
            show samantha happy
            "Of course, Sam smiles at this, as she's getting her way."
            show sasha annoyed
            "Sasha, on the other hand, looks disappointed, curling her lip and narrowing her eyes."
            "For a moment I think that she's going to argue."
            "But then she nods and shrugs her shoulders."
            sasha.say "Whatever!"
            sasha.say "I guess I've got to go with the majority."
            "We walk across the hot sand to the ice cream stall."
            "And soon enough we're all licking away at an ice cream."
            "I'm feeling the relief of it cooling me down."
            "But then I see that Sasha's not just licking her ice cream."
            show beach icecream sasha nomc with fade
            "Instead she looks like she's trying to make it as suggestive as possible!"
            "Is she...is she doing that to get back at Sam?"
            "Is Sasha trying to turn this into a flirting competition?!?"
            "Whatever Sasha's intentions, that's what Sam seems to think is happening."
            show beach icecream samantha nomc
            "And pretty soon she's doing the exact same thing!"
            if sasha.sexperience > samantha.sexperience:
                "My eyes dart from Sasha to Sam, watching as they lick away."
                "But it's Sasha that seems to be getting the better of it."
                show beach icecream sasha nomc
                "Her tongue is moving like a snake, lapping at her ice cream."
                "Sam does her best to keep up, but she's clearly out-classed."
                show beach icecream samantha nomc
                "And in the end, all she manages to do is drop most of her ice cream onto the sand!"
                samantha.say "Oops..."
                scene bg beach
                show samantha annoyed swimsuit at right5
                with fade
                samantha.say "Darn it!"
                sasha.say "Bad luck, Sam!"
                show sasha happy swimsuit at left5 with dissolve
                sasha.say "I guess I've got you licked!"
                $ samantha.love -= 1
                $ sasha.love += 1
            else:
                "My eyes dart from Sasha to Sam, watching as they lick away."
                "But it's Sam that seems to be getting the better of it."
                show beach icecream samantha nomc with fade
                "Her tongue is moving like a snake, lapping at her ice cream."
                "Sasha does her best to keep up, but she's clearly out-classed."
                show beach icecream sasha nomc
                "And in the end, all she manages to do is drop most of her ice cream onto the sand!"
                sasha.say "Oops..."
                scene bg beach
                show sasha annoyed swimsuit at left5
                with fade
                sasha.say "Darn it!"
                samantha.say "Bad luck, Sam!"
                show samantha annoyed swimsuit at right5 with dissolve
                samantha.say "I guess I've got you licked!"
                $ samantha.love += 1
                $ sasha.love -= 1
                $ beach_event += 1
        "Play volleyball":
            "Actually, now that I'm up and awake, the heat's not that bad."
            "I think that I could stand to run around a little."
            "And we can always grab an ice cream if we do get too hot."
            mike.say "I think the sun's past it's peak by now."
            mike.say "So playing volleyball should be doable!"
            "Of course, Sasha smiles at this, as she's getting her way."
            show sasha happy
            "Sam, on the other hand, looks disappointed, curling her lip and narrowing her eyes."
            show samantha annoyed
            "For a moment I think that she's going to argue."
            "But then she nods and shrugs her shoulders."
            samantha.say "Okay, okay..."
            samantha.say "I suppose that means I'm outvoted!"
            "I rummage around in our things until I find the ball."
            "And then we head out onto the volleyball court to play."
            "The game seems to go more smoothly than I thought it would."
            hide sasha
            hide samantha
            show beach volleyball sasha swimsuit with fade
            "Sasha's obviously well into it."
            "Even more so since Sam was so reluctant to play."
            show beach volleyball samantha swimsuit
            "But soon enough, Sam makes it clear she's not half-assing it either."
            "For all of her talk about being too hot, she's running around like crazy!"
            "And I get the distinct feeling she's trying to beat Sasha at her own game."
            menu:
                "I'm playing with Sasha":
                    "But for all that Sam's giving it her all, it doesn't pay off."
                    "I know that Sasha's not the most sporty girl I've ever met."
                    show beach volleyball sasha swimsuit
                    "But she does play a mean game of volleyball - I know from experience!"
                    "Pretty soon, Sam's panting and sweating as she tries to keep up."
                    show beach volleyball samantha swimsuit
                    "And I'm finding it more than a little distracting!"
                    "I watch as Sam jumps up and down, covered in a sheen of perspiration."
                    "The sight means that I soon need to adjust my shorts!"
                    "But it all comes to a crashing end when Sam leaps for the ball."
                    "It sails over her head and she lands, face first, in the sand."
                    scene bg beach
                    show samantha annoyed swimsuit at right5
                    show sasha normal swimsuit at left5
                    with fade
                    samantha.say "Ouch!"
                    samantha.say "Eww!"
                    "Sasha and I walk over as Sam spits out a mouthful of sand."
                    "I help her to her feet while Sasha retrieves the ball."
                    mike.say "I think that's enough physical activity for now!"
                    show sasha happy
                    sasha.say "Yeah, and I don't think Sam could eat anymore sand!"
                    $ samantha.love -= 1
                    $ sasha.love += 1
                    $ beach_event += 1
                "I'm playing with Samantha":
                    "But for all that this is Sasha's game, it doesn't seem to help."
                    "I know that Sasha's not the most sporty girl I've ever met."
                    show beach volleyball sasha swimsuit
                    "But she does play a mean game of volleyball - I know from experience!"
                    "And yet Sam's on a whole different level."
                    show beach volleyball samantha swimsuit
                    "Pretty soon, Sasha's panting and sweating as she tries to keep up."
                    "And I'm finding it more than a little distracting!"
                    "I watch as Sasha jumps up and down, covered in a sheen of perspiration."
                    show beach volleyball sasha swimsuit
                    "The sight means that I soon need to adjust my shorts!"
                    "But it all comes to a crashing end when Sasha leaps for the ball."
                    "It sails over her head and she lands, face first, in the sand."
                    scene bg beach
                    show samantha normal swimsuit at right5
                    show sasha annoyed swimsuit at left5
                    with fade
                    sasha.say "Ouch!"
                    sasha.say "Eww!"
                    "Sam and I walk over as Sasha spits out a mouthful of sand."
                    "I help her to her feet while Sam retrieves the ball."
                    mike.say "I think that's enough physical activity for now!"
                    show samantha happy
                    samantha.say "Yeah, and I don't think Sasha could eat anymore sand!"
                    $ samantha.love -= 1
                    $ sasha.love += 1
                    $ beach_event += 1
        "Play in the sea" if hero.charm >= 80:
            "This is a tough one and no mistake!"
            "Sam's right when she says that it's super hot today."
            "And I'd love the chance to cool down a little."
            "But Sasha's got a point too."
            "I am feeling like I need to get moving."
            "It's then that my gaze falls on the crashing waves."
            "Perhaps there's a compromise staring me right in the face?"
            mike.say "I've got a better idea."
            mike.say "Why don't we go in the sea for some time?"
            show samantha annoyed
            show sasha annoyed
            "Sasha and Sam both look at me like I'm insane."
            samantha.say "Don't you think that's a little childish?"
            sasha.say "Yeah, like what are we - a bunch of kids?"
            "I roll my eyes at them and shake my head."
            mike.say "Right now you sound like a couple of old women!"
            mike.say "You're never too old for a paddle in the sea!"
            "With that I get up and begin to walk towards the waves."
            "I'm pretty sure that it'll have the desired effect on them."
            "And sure enough, I hear Sasha and Sam scrambling to follow me."
            sasha.say "Hey!"
            show sasha normal
            sasha.say "Wait up!"
            samantha.say "Yeah, [hero.name]!"
            show samantha normal
            samantha.say "I never said that I didn't want to come too!"
            "Even though they're following close behind, I still get there first."
            "And so I get to watch as Sasha and Sam wade into the water."
            sasha.say "Geez it's cold!"
            show sasha annoyed
            samantha.say "Brr...it's freezing!"
            show samantha annoyed
            "I know that I should be saying something to encourage them."
            "The truth is that I'm too busy watching how their bodies react to the cold water."
            "At first they're both shivering and breaking out in goose-bumps."
            "But what really interest me is the fact that their nipples are getting nice and stiff!"
            "Neither Sasha nor Sam seems to notice."
            "So I can check out the sight of them."
            "They're firm and erect, pushing against the fabric of their swimsuits."
            "But then I discover exactly why Sasha and Sam have their minds on something else."
            sasha.say "Whoa!"
            show sasha flirt
            sasha.say "Looks like somebody's excited!"
            samantha.say "Oh...oh my!"
            show samantha flirt
            samantha.say "You do look pleased to see us, [hero.name]!"
            "I look down, following their eyes."
            "And then I see that my cock is as erect as their nipples!"
            "I hastily cover myself up and squat down in the water."
            show sasha happy
            show samantha happy
            "The girls giggle at me as my face turns bright red."
            "This wasn't the plan, damn it!"
            "This was supposed to cool me down and help me relax!"
            $ samantha.love += 1
            $ sasha.love += 1
            $ beach_event += 1
        "Stay here and enjoy the time that passes" if hero.charm < 80:
            "I frown at what the girls are saying, not feeling it at all."
            "The heat doesn't seem all that bad to me."
            "And I'm not itching to get up off my ass at all!"
            mike.say "Nah..."
            mike.say "I don't think I want to do either!"
            mike.say "You guys can please yourselves, do whatever."
            mike.say "I'm just going to lie back down and relax, okay?"
            show sasha annoyed
            show samantha annoyed
            "Sasha and Sam both look at me in irritation and disbelief."
            "They snort and turn their backs on me almost as one."
            sasha.say "Huh!"
            sasha.say "You lazy pig!"
            samantha.say "Hmm..."
            samantha.say "That's more than a little selfish, [hero.name]!"
            "I hear what they're saying, but I don't let it show."
            "Instead I just lie back on the sand and ignore them."
            "Eventually the sound of their complaints fades away."
            "And I'm finally free to drift off."
            $ samantha.sub += 1
            $ sasha.sub += 1
            $ beach_event -= 1
    show sasha normal
    show samantha normal
    "A little time passes and the sun sinks a little lower in the sky."
    "This means that it's cooler, but the sand still retains the heat of the sun."
    "All in all, it makes for a pleasantly lazy atmosphere."
    sasha.say "Hey, [hero.name]..."
    sasha.say "I'm going to get some shots of the coastline."
    show sasha happy
    sasha.say "You wanna come with me?"
    "I look up to see Sasha waving her camera in my face."
    "But Sam seems to have different ideas."
    samantha.say "Aww..."
    samantha.say "Don't go, [hero.name]!"
    show samantha happy
    samantha.say "I wanted you to help me read my book..."
    "I look from Sasha to Sam and back again."
    "Why do they have to do this to me?"
    "I'd love to spend time with either of them."
    "But it looks like they're going to make me choose!"
    menu:
        "Go with Sasha":
            "I knew that Sasha had a pretty nice camera."
            "But I never knew that she was into taking landscape shots with it."
            "And suddenly I'm intrigued by this side to her artistic nature."
            if samantha.flags.nickname == "cupcake":
                mike.say "Sorry, Cupcake..."
            else:
                mike.say "Sorry, Sam..."
            mike.say "Sasha got in there and asked first!"
            show samantha annoyed
            "Sam makes a point of pouting and huffing."
            "But I'm already up and following Sasha across the sand."
            "She leads me up to where the coastline is more rocky and interesting."
            show sasha normal
            "And then she starts to snap pictures of whatever takes her fancy."
            mike.say "Do you do this often, Sasha?"
            mike.say "Go out and take photos in nature, I mean?"
            "Sasha keeps on snapping away with her camera."
            "But she's not too engrossed to ignore the question."
            "And she nods her head in confirmation."
            sasha.say "Whenever I can - which isn't often enough!"
            sasha.say "It's always been my back-up plan, you know?"
            sasha.say "For if music didn't work out."
            "Sasha beckons me over and holds up her camera."
            "She shows me some of the shots she's taken on the screen."
            "I'm no expert, but they certainly look good to me."
            mike.say "Those are great, Sasha."
            mike.say "You have a really good eye!"
            sasha.say "Aw..."
            show sasha happy
            sasha.say "Thanks, [hero.name]!"
            "It's just then that Sasha pulls up a shot that looks familiar."
            "She hurries to turn off the camera before I see it."
            "But I can still make out that it's a photo of me."
            "And from what I saw, she made me look pretty moody and brooding!"
            sasha.say "You didn't see that!"
            mike.say "What, that picture of me?!?"
            show sasha blush
            sasha.say "I...I like to shoot human subjects sometimes!"
            mike.say "And you chose to shoot me?"
            mike.say "I'm flattered, Sasha!"
            show sasha happy
            "Sasha smiles and laughs, maybe a little awkwardly."
            "And we go back to her shooting the coastline."
            "But now I know that she shoots me in secret."
            "And she knows that I know it too!"
            $ samantha.love -= 1
            $ sasha.love += 1
        "Stay with Samantha":
            "I've seen the book that Sam's got on the go at the moment."
            "It's a pretty thick novel that she's getting through at a quick pace."
            "Which means that she's not being honest when she says she needs my help."
            "And that makes me all the more interested in what she's actually after!"
            mike.say "Sorry, Sasha..."
            mike.say "I'm not in the mood for a walk right now."
            show sasha annoyed
            "Sasha shakes her head as she turns and walks away."
            "And I can still hear her muttering for a good while after that too."
            "But most of my attention in now focused on Sam."
            "She smiles as she shuffles over to me and lies down against me."
            "Her back is against my chest, her head resting just below mine."
            show samantha normal
            samantha.say "What I need you to do, [hero.name]..."
            samantha.say "Is hold the book and turn the pages for me, okay?"
            "I nod eagerly, doing just as she tells me."
            "And I do it knowing that my reward is being this close to her."
            "I have Sam snuggled up against me the whole time that she's reading."
            "It's quiet and sedate, sure."
            "But the sensation of her body against mine is priceless."
            "I can feel every inch of her."
            "I can smell her scent too."
            "And I have to do nothing more than occasionally turn the page."
            "I lose track of how long we're laid there together."
            "But it's a place I'd be happy to be for the rest of my life!"
            $ samantha.love += 1
            $ sasha.love -= 1
        "Suggest a photo-shoot" if hero.charm >= 95:
            "The sight of Sasha's camera gives me an idea."
            "Maybe there's a way I can keep both of them happy."
            "And do something that'll cheer me up into the bargain."
            mike.say "You know, you two look so good in your swimsuits."
            mike.say "I should use that camera to give you a photo-shoot."
            show samantha annoyed
            show sasha annoyed
            "Sasha and Sam exchange puzzled glances and frowns."
            "Sure, the idea sounds more than a little crazy."
            "But I can see that under it, they're both intrigued."
            sasha.say "You mean like we were bikini models?"
            samantha.say "Come on, [hero.name]."
            samantha.say "They're all super young."
            sasha.say "And super skinny too!"
            mike.say "That's why you two should do it."
            mike.say "Because you're REAL women!"
            mike.say "And that's sexier than any model could be!"
            show sasha blush
            show samantha flirt
            "Now the pair of them are beginning to blush."
            "And that's how I know that I've got them hooked!"
            samantha.say "Do...do you really think so?"
            sasha.say "I never did any modelling before!"
            mike.say "That why this will be so great!"
            mike.say "It'll look natural - not forced at all."
            sasha.say "Okay, I'll do it!"
            show sasha happy
            samantha.say "Me too!"
            show samantha happy
            "Pretty soon we've chosen a spot on the beach."
            "And the girls are giving me their best poses."
            "I wasn't lying when I said all that stuff to them either."
            show sasha b flirt
            show samantha flirt
            "Sasha and Sam are totally natural the whole time."
            "And it means that they come across really well in the shots."
            "Plus I get to feel like a genuine photographer."
            "One that gets to work with hot girls in swimsuits for a living!"
            "Afterwards we go through the shots and the girls seem delighted."
            "For them it's a fun chance to play at being a model."
            "And for me it's a memento of a great day at the beach."
            "A set of photos I think I'll be coming back to over and over again!"
            $ samantha.love += 1
            $ sasha.love += 1
            $ beach_event += 1
        "Take a stroll" if hero.charm < 95:
            "I'm getting pretty tired of them fighting over my attention."
            "The idea was to come to the beach to relax, not fall out."
            "So maybe it's time to do something for myself by myself?"
            mike.say "Neither of you need my help to do any of that."
            mike.say "Sasha, you can take pictures on your own."
            if samantha.flags.nickname == "cupcake":
                mike.say "And, Cupcake, you can read, for god's sake!"
            else:
                mike.say "And, Sam, you can read, for god's sake!"
            show sasha annoyed
            sasha.say "Huh?!?"
            show samantha annoyed
            samantha.say "But what about you?"
            "Getting to my feet, I pause only long enough to shake off the sand."
            mike.say "I'm going for a walk."
            mike.say "I could use the fresh air."
            mike.say "See you back here later."
            "Before they can argue, I'm striding off across the beach."
            "I think I can hear Sasha and Sam talking behind me."
            "Or to be more accurate, I can hear them blaming each other!"
            "Maybe what they need is the space to sort out their issues."
            "And if not, that's still what I'm going to give them."
            $ samantha.sub += 1
            $ sasha.sub += 1
            $ beach_event -= 1
    if beach_event >= 3:
        call home_harem_samantha_sasha_beach_fuck from _call_home_harem_samantha_sasha_beach_fuck
    else:
        "Soon enough it's clear that the time has come for us to head home."
        "We pack up all of our stuff and haul it back up to where we parked the car."
        "Everyone's tired and more than a little burnt from the sun."
        "But I think we had a pretty good day, give or take some squabbling."
        "And thankfully the fact we're tired means a quiet drive back to the house."
        scene bg black with dissolve
    $ game.pass_time(4)
    return

label home_harem_samantha_sasha_beach_fuck:
    scene bg beach
    show sasha swimsuit at left5
    show samantha swimsuit at right5
    with fade
    "It's been a pretty great day at the beach, with perfect weather and a real chance to kick back and relax."
    "And I've had some great company too, thanks to Sasha and Sam coming along with me."
    "Not to mention spending time with two super-hot girls in their swimsuits!"
    "But the sun's starting to sink lower in the sky and the heat of the day is fading."
    "Pretty soon it won't be worth spending any more time on the beach, so I guess we should head home."
    mike.say "You guys want to start packing up your things?"
    mike.say "I think it's time to get back to the car."
    mike.say "We don't want to still be here when the sun goes down!"
    "Sasha and Sam look up from where they're laid on the sand."
    "And they don't seem too keen to heed my advice just yet."
    show sasha sadsmile
    sasha.say "Is it that time already?"
    sasha.say "I was having such a good time!"
    show sasha normal
    show samantha happy
    samantha.say "Surely we can stay a little longer, [hero.name]?"
    samantha.say "That way we'll beat the rush to get out of the car park."
    show samantha normal
    "They're not wrong - it's not like we need to head back as soon as possible."
    "But I've already started to get up and shove some stuff into my bag."
    mike.say "I dunno, guys..."
    mike.say "I feel like I've done everything I wanted to do already."
    mike.say "What other reason is there to stay here?"
    "I can see that this sets them both off thinking."
    "But it's Sasha that speaks up first."
    show sasha joke
    sasha.say "If we come up something, you'll stay longer, right?"
    show sasha normal
    mike.say "Fair enough, Sasha."
    mike.say "Think something up for me to do and we'll stay."
    show sasha at center with ease
    "Sasha leans over to Sam and begins to whisper in her ear."
    show samantha surprised
    "I see that Sam looks surprised by what she hears."
    show samantha happy
    "But her expression soon turns into one of amusement."
    "And she nods agreement to whatever Sasha is suggesting."
    show sasha joke at left5 with ease
    sasha.say "Us!"
    sasha.say "You haven't done us!"
    show samantha flirt
    samantha.say "Yeah, [hero.name]..."
    samantha.say "Stay longer and you can do whatever you want to us!"
    "I find myself blinking and just staring at them."
    "Did they just say what I think they said?"
    "That if I agree to stay at the beach, I can get it on with them?!?"
    "As if to underline the point, Sasha begins to strip off her swimsuit."
    "Sam takes the hint and starts to do the same thing."
    "And as they're only wearing swimsuits, it takes very little time indeed!"
    show sasha flirt
    sasha.say "So what do you say, [hero.name]?"
    show samantha blush
    samantha.say "Can we stay a little while longer?"
    "I'm almost hypnotised by the sight of their naked breasts before me."
    "But somehow I manage to nod my head and mutter a response."
    mike.say "Y...yeah..."
    mike.say "Anything for boobs..."
    mike.say "I...I mean...anything for you guys!"
    "This earns me a peal of giggles from the girls."
    sasha.say "Okay, [hero.name]..."
    sasha.say "So which one of us do you want?"
    samantha.say "Yeah - who gets to ride your manhood?"
    menu:
        "Choose Sasha":
            "I'm already pulling off my shorts as I nod towards Sasha."
            "She's watching me so closely that she can't fail to understand my meaning."
            sasha.say "Sorry, Sam..."
            sasha.say "Looks like I'm the one getting a ride today!"
            samantha.say "Okay, Sasha, okay!"
            samantha.say "There's no need to rub it in!"
            "By the time I'm naked, Sasha's crawled over to where I'm sitting."
            "I make to get up, but she pushes me back down onto the sand."
            "And then she proceeds to straddle my thighs, pinning me to the ground."
            scene bg black
            show threesome samsasha sashafuck beach out
            with fade
            "Sasha has her back to me, so I can't see what she's doing."
            "But I feel it the moment she takes hold of my cock."
            "Already getting hard, it stiffens rapidly as she strokes it."
            "And the sensations become even more intense as she rubs it against her pussy."
            show threesome samsasha sashafuck sasha_surprised
            sasha.say "Mmm..."
            sasha.say "It's so big and so hard!"
            sasha.say "I don't know how I'm gonna fit it in here!"
            "Even if I didn't know she was teasing me, I could answer that question."
            "Because I can already feel how wet and slippery she is down there."
            show threesome samsasha sashafuck samantha sasha_opened
            samantha.say "I don't know, Sasha."
            samantha.say "Just try it and hope, I guess!"
            sasha.say "Well..."
            sasha.say "Here goes nothing..."
            show threesome samsasha sashafuck vaginal sasha_pain -out
            "I feel Sasha sit down on my cock, gently lowering herself onto it."
            show threesome samsasha sashafuck down
            "She uses her weight carefully, letting gravity do most of the work."
            mike.say "Fuck me, Sasha..."
            mike.say "That feels incredible!"
            show threesome samsasha sashafuck
            sasha.say "Ah..."
            sasha.say "Oh god..."
            sasha.say "You got that right!"
            sasha.say "Please...fuck me...good and hard!"
            "I take a firm hold of Sasha around the waist."
            "And then I begin to do as I'm told."
            "I feel my cock sink all the way into her, until it can go no further."
            show threesome samsasha sashafuck up
            pause 0.2
            show threesome samsasha sashafuck down at startle(0.05,-10)
            pause 0.2
            show threesome samsasha sashafuck up
            pause 0.2
            show threesome samsasha sashafuck down at startle(0.05,-10)
            "And only then do I start to thrust up and down, moving with all my strength."
            "Sasha gasps and moans as she rides my cock."
            "Looking at her from behind, I can only see a little of her face."
            show threesome samsasha sashafuck up
            pause 0.2
            show threesome samsasha sashafuck down at startle(0.05,-10)
            pause 0.2
            show threesome samsasha sashafuck up
            pause 0.2
            show threesome samsasha sashafuck down at startle(0.05,-10)
            "And just the barest glimpse of her breasts as they jiggle up and down."
            "But what I can see is the shape of her buttocks."
            show threesome samsasha sashafuck up
            pause 0.2
            show threesome samsasha sashafuck down at startle(0.05,-10)
            pause 0.2
            show threesome samsasha sashafuck up
            pause 0.2
            show threesome samsasha sashafuck down at startle(0.05,-10)
            "Sasha's bouncing on them like a pair of plump cushions!"
            show threesome samsasha sashafuck samantha
            "Sam, on the other hand, I can see."
            "So I get a front row seat to watch her lean in and kiss Sasha."
            show threesome samsasha sashafuck up
            pause 0.2
            show threesome samsasha sashafuck down at startle(0.05,-10)
            pause 0.2
            show threesome samsasha sashafuck up
            pause 0.2
            show threesome samsasha sashafuck down at startle(0.05,-10)
            "At the same time she begins to play with my balls and the base of my cock."
            "Sasha eagerly returns the kiss, tongues darting between their lips."
            "And the more intense the kisses become, the tighter Sam squeezes my manhood!"
            show threesome samsasha sashafuck up sasha_pleasure
            pause 0.2
            show threesome samsasha sashafuck down at startle(0.05,-10)
            pause 0.2
            show threesome samsasha sashafuck up
            pause 0.2
            show threesome samsasha sashafuck down at startle(0.05,-10)
            mike.say "Shit..."
            mike.say "Sam..."
            mike.say "You're gonna make me..."
            "I can't resist the pressure to shoot my load."
            "And it happens just as Sasha sinks down as low as she can go."
            show threesome samsasha sashafuck up sasha_surprised sasha_pain -samantha
            pause 0.2
            show threesome samsasha sashafuck down at startle(0.05,-10)
            pause 0.2
            show threesome samsasha sashafuck up
            pause 0.2
            show threesome samsasha sashafuck down cum with vpunch
            "This means that my cock's buried deep inside of her when I cum."
            sasha.say "Oh..."
            sasha.say "Oh yeah!"
            show threesome samsasha sashafuck up squirt sasha_ahegao sasha_pleasure creampie
            pause 0.2
            show threesome samsasha sashafuck down with vpunch
            sasha.say "Fill me up...PLEASE!"
            show threesome samsasha sashafuck up
            pause 0.2
            show threesome samsasha sashafuck down -squirt with vpunch
            "Sasha quivers and quakes as I give her exactly what she wants."
            "And once it's done, we both begin to sag like puppets with severed strings."
            show threesome samsasha sashafuck samantha sasha_closed
            $ sasha.sexperience += 1
        "Choose Samantha":
            "I'm already pulling off my shorts as I nod towards Sam."
            "She's watching me so closely that she can't fail to understand my meaning."
            samantha.say "Tough luck, Sasha!"
            samantha.say "Looks like he's picking me!"
            sasha.say "Yeah, yeah..."
            sasha.say "Don't rub it in, Sam!"
            "By the time I'm naked, Sam's crawled over to where I'm sitting."
            "I make to get up, but she pushes me back down onto the sand."
            "And then she proceeds to straddle my thighs, pinning me to the ground."
            "Sam has her back to me, so I can't see what she's doing."
            scene bg black
            show threesome samsasha samfuck beach with fade
            "But I feel it the moment she takes hold of my cock."
            "Already getting hard, it stiffens rapidly as she strokes it."
            "And the sensations become even more intense as she rubs it against her pussy."
            show threesome samsasha samfuck sampleasure
            samantha.say "Mmm..."
            show threesome samsasha samfuck samnormal
            samantha.say "It's SO big, [hero.name]!"
            samantha.say "It's got to be the biggest one I've ever had!"
            samantha.say "Where am I going to put it?"
            "Even if I didn't know she was teasing me, I could answer that question."
            "Because I can already feel how wet and slippery she is down there."
            sasha.say "I don't know, Sam."
            sasha.say "Just try it and hope, I guess!"
            samantha.say "Well..."
            samantha.say "Here goes nothing..."
            "I feel Sam sit down on my cock, gently lowering herself onto it."
            "She uses her weight carefully, letting gravity do most of the work."
            mike.say "Fuck me, Sam..."
            mike.say "That feels incredible!"
            show threesome samsasha samfuck sampleasure
            samantha.say "Ah..."
            samantha.say "Oh god..."
            samantha.say "You got that right!"
            samantha.say "Please...fuck me...good and hard!"
            "I take a firm hold of Sam around the waist."
            "And then I begin to do as I'm told."
            "I feel my cock sink all the way into her, until it can go no further."
            "And only then do I start to thrust up and down, moving with all my strength."
            "Sam gasps and moans as she rides my cock."
            "Looking at her from behind, I can only see a little of her face."
            "And just the barest glimpse of her breasts as they jiggle up and down."
            "But what I can see is the shape of her buttocks."
            "Sam's bouncing on them like a pair of plump cushions!"
            show threesome samsasha samfuck sasha
            "Sasha, on the other hand, I can see."
            "So I get a front row seat to watch her lean in and kiss Sam."
            "At the same time she begins to play with my balls and the base of my cock."
            "Sam eagerly returns the kiss, tongues darting between their lips."
            "And the more intense the kisses become, the tighter Sasha squeezes my manhood!"
            mike.say "Shit..."
            mike.say "Sasha..."
            mike.say "You're gonna make me..."
            "I can't resist the pressure to shoot my load."
            show threesome samsasha samfuck -sasha
            "And it happens just as Sam sinks down as low as she can go."
            with hpunch
            "This means that my cock's buried deep inside of her when I cum."
            show threesome samsasha samfuck samahegao tongue
            samantha.say "Oh..."
            samantha.say "Oh yeah!"
            with hpunch
            samantha.say "Fill me up...PLEASE!"
            with hpunch
            "Sam quivers and quakes as I give her exactly what she wants."
            "And once it's done, we both begin to sag like puppets with severed strings."
            show threesome samsasha samfuck sasha sampleasure -tongue
            $ samantha.sexperience += 1
    "All three of us end up laid out on the sand, a sweaty tangle of limbs."
    "Any thought of getting up and heading for the car have vanished from my mind."
    "Right now, all I can do is lie still, Sasha and Sam entwined with me."
    "I got what I wanted, and now it's time for me to keep my promise."
    "We'll stay right here, lying on the sand until they tell me they're ready to go."
    $ sasha.love += 2
    $ samantha.love += 2
    scene bg black with dissolve
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
