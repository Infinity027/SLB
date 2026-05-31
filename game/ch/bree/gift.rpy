init python:
    Equip("bree_sweater", display_name="[bree.name]'s sweater", effects={"bree": 100, "charm": -5})

    Event(**{
    "name": "bree_give_a_gift",
    "label": "npc_give_a_gift",
    "conditions": [
        Or(
            HeroTarget(IsBirthday()),
            IsSpecialDate("christmas"),
            IsSpecialDate("valentine"),
            ),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "girl": "bree",
    "once_day": True,
    "do_once": False,
    "quit": False,
    }
    )

label bree_give_male:
    if "zbox_360" not in hero.inventory:
        $ gift = "zbox_360"
        "She hands me a pretty large box."
        mike.say "Wow!\nIs that a Zbox?"
        bree.say "It sure is..."
        mike.say "Thank you so much."
    elif bree.love >= 25 and "bree_sweater" not in hero.inventory:
        $ gift = "bree_sweater"
        "She hands me a hand knit sweater, a rather failed attempt at a hand knit sweater anyway."
        mike.say "It's beautiful..."
        bree.say "Thanks [hero.name]."
        mike.say "Thank you [bree.name]."
    else:
        $ gift = "cake"
        "She hands me a box, obviously from a pastry shop."
        mike.say "Thanks."
    $ hero.gain_item(gift)
    return

label bree_give_valentine_male:
    "[bree.name] walks hesitantly towards me."
    call bree_greet from _call_bree_greet_7
    show bree flirt blush
    bree.say "Happy valentine's day [hero.name]..."
    "[bree.name] hands me a box of chocolates."
    mike.say "Thank you, [bree.name]."
    $ hero.gain_item("valentine_chocolates")
    return

label bree_give_birthday_male:
    "[bree.name] walks towards me."
    call bree_greet from _call_bree_greet_8
    show bree happy
    bree.say "Happy birthday [hero.name]!"
    call bree_give_male from _call_bree_give_male
    return

label bree_give_christmas_male:
    "[bree.name] walks towards me."
    call bree_greet from _call_bree_greet_9
    show bree happy
    bree.say "Merry Christmas [hero.name]."
    call bree_give_male from _call_bree_give_male_1
    return

label bree_birthday_gift_male:
    show bree
    if bree.flags.birthdayknown:
        mike.say "Happy birthday [bree.name]."
        bree.say "How sweet, you remembered my birthday!"
    else:
        bree.say "How do you know my birthday?"
        mike.say "I didn't, it's just pure luck."
        $ bree.flags.birthdayknown = True
    return

label bree_christmas_gift_male:
    show bree
    mike.say "Merry Christmas [bree.name]."
    bree.say "Thanks!"
    $ bree.love += 2
    return

label bree_valentine_gift_male:
    show bree
    mike.say "Happy valentine's day [bree.name]."
    bree.say "Thank you."
    $ bree.love += 2
    return

label bree_gift_swimsuit_male:
    show bree happy
    bree.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy swimsuit."
    if bree.sub >= 60:
        show bree flirt blush
        bree.say "It's so pretty, thank you so much [hero.name]."
        $ bree.flags.sexyswimsuit = True
    else:
        show bree annoyed
        $ bree.love -= 4
        bree.say "Thanks but no thanks [hero.name], I would feel very awkward with that..."
        bree.say "Even worse than being naked..."
        $ hero.cancel_activity()
    return

label bree_gift_collar_male:
    show bree
    if randint(1, 2) == 1:
        bree.say "Oh... I.. Is it for me?"
        "[bree.name] sits up, reaching for the wrapped gift."
        "I lean down and give her the box."
        $ bree.love += 2
        "After a few moments of looking at the box she starts unpacking it and get the collar out."
        "I wish I could see her expression, but with her head lowered, I can't see her face."
        if bree.sub < 90:
            show bree angry
            bree.say "What the fuck!"
            "[bree.name] throws the collar away and leaves."
            $ bree.love -= 20
            $ bree.sub -= 5
            $ bree.flags.gone = True
            $ bree.flags.goneDelay = TemporaryFlag(1, "day")
            $ bree.hide()
            $ hero.cancel_activity()
        else:
            bree.say "Oh... it's beautiful. Do you have the key?"
            "I nod, dipping my fingers into my pocket to flash the key at her briefly before putting it away, already feeling a little thrill at how she's reacting to her gift."
            "And, of course, anticipation of putting it on her."
            $ bree.set_sex_slave()
            bree.say "Can I wear it now?"
            hide bree
            show bree close at bottom_to_top
            "I go over and take the collar, then step behind the couch to loop it carefully around her neck and buckle it."
            "She lets out a little sigh as she hears the lock click."
            $ bree.love += 2
            $ bree.sub += 5
    else:
        "I thought that I had [bree.name] pegged pretty much from the first time that we met."
        "When she moved in, I saw a cute, fun gamer girl that was up for fun."
        "And as we started to get closer, all of that turned out to be true."
        "But there's another side to her, one that I wasn't aware of at first."
        "I only got to see it as we became more intimate on a physical level."
        "And that's the side of [bree.name] that's pretty kinky and into risque stuff."
        "It's not something that shocked me or turned me off in the slightest."
        "I mean, I'm a pretty adventurous guy myself, so it was a pleasant discovery!"
        "I just feel like we've never really agreed that it's become a part of our relationship."
        "And that stops me from suggesting we up the stakes and get even crazier together."
        "So what I think the situation needs is a gesture on my behalf."
        "I need to make a statement to [bree.name] about the direction I see us going."
        "And it doesn't take me long to settle on the perfect thing to do it."
        "Then all I need to do is pick my moment..."
        mike.say "Hey, [bree.name]..."
        mike.say "I got you a little something."
        mike.say "You know, as a surprise?"
        hide bree
        show bree close happy
        "[bree.name]'s eyes light up at the mere mention of me having a gift for her."
        "After all, she's only human, and what girl doesn't like being spoilt?"
        bree.say "Oh, wow!"
        bree.say "That's SO sweet of you, [hero.name]!"
        show fx question
        bree.say "What is it?!?"
        "I chuckle, feeling pleased with [bree.name]'s enthusiasm."
        "But I shake my head, fondly chastising her for the question."
        mike.say "It's a surprise, remember?"
        mike.say "Let's just say it's something to wear."
        mike.say "Something that I think will look good on you."
        "[bree.name] claps her hands together in delight."
        "And I can see that I've got her mind racing."
        bree.say "Ooh..."
        bree.say "Is it a cute t-shirt?"
        bree.say "Maybe something to wear around the pool?"
        bree.say "Or...or is it some sexy underwear, huh?!?"
        "I don't give [bree.name] the chance to get too far down the line of speculation."
        "Instead I take out the gift from where I've been keeping it hidden."
        "[bree.name] giggles and strains to see what I have in my hands."
        "And then I open them, to reveal a pink, leather collar."
        "It looks like the kind a dog would wear, but scaled up."
        "The badge on the front reads 'Pet' in capital letters."
        "[bree.name]'s giggling stops all of a sudden."
        "And she covers her mouth with both hands."
        "Though I can't tell if it's in delight or horror!"
        if bree.sub >= 90:
            "But [bree.name]'s quick to answer that question for me."
            "She lets out a squeal of what can only be delight."
            "And she practically snatches the collar out of my hand."
            show fx exclamation
            bree.say "Oh WOW!"
            bree.say "I mean really WOW!"
            bree.say "How in the hell did you know?!?"
            "[bree.name]'s sudden show of enthusiasm catches me on the back-foot."
            "And I struggle to regain my composure and answer the question."
            mike.say "Ah, you know how it is, [bree.name]."
            mike.say "Us modern guys, we're sensitive to these kind of things."
            mike.say "It's like we can pick up on the subtlest of hints from a girl..."
            "[bree.name] nods eagerly, but I get the impression she's not actually listening."
            "Instead she holds up the collar and begins to push her hair out of the way."
            bree.say "Yeah, yeah..."
            bree.say "Whatever..."
            bree.say "Can you give me a hand with this thing?"
            $ bree.set_sex_slave()
            if bree.flags.daddy == True:
                $ bree.flags.mikeNickname in nickname_daddy
            "I nod and hurry to do as I'm told."
            hide bree
            show bree close blush at bottom_to_top
            "And a few seconds later, I have the collar fastened in place."
            "[bree.name] looks down at it happily and then laughs."
            "She holds up her hands like a dog that's been told to beg."
            "And she sticks out her tongue, making a panting sound."
            bree.say "What do you think, [hero.name]?"
            bree.say "Will you let me be your pet bitch?"
            bree.say "I may not be a pedigree, but I'm VERY obedient!"
            bree.say "And you should see some of the tricks I can do for you..."
            "Suddenly I can feel my cheeks flushing red with embarrassment."
            "I was supposed to be the one convincing [bree.name] this was a good idea."
            "Now she's somehow managed to flip the tables on me!"
            mike.say "Th...that sounds great, [bree.name]!"
            mike.say "But maybe we should wait, yeah?"
            mike.say "At least until we're somewhere more private?"
            "[bree.name]'s smile turns into an exaggerated pout."
            "And she makes a VERY convincing whining sound."
            bree.say "Aw...now your puppy's sad!"
            bree.say "You're going to have to play with her, [hero.name]!"
            bree.say "And she knows just what kind of games she wants to play too..."
            "[bree.name] takes me by the hand, leading me away to god-knows-where."
            "And I'm excited at the prospect of what she has in mind."
            "Only I hope it's going to go down somewhere a little less public!"
            $ bree.love += 2
            $ bree.sub += 5
        else:
            "But [bree.name]'s quick to answer that question for me."
            hide bree
            show bree angry
            "She lets out a gasp of what can only be horror."
            "And then she points at the collar in my hands."
            bree.say "What in the HELL is that?!?"
            bree.say "It looks like something a dog should wear!"
            bree.say "Is this your idea of a joke?!?"
            "I shake my head, caught on the backfoot."
            "This was definitely not the reaction I was expecting."
            "And I don't have an argument or explanation ready either."
            mike.say "It...it's just a little fun, [bree.name]!"
            mike.say "You know - something you could wear for a laugh!"
            mike.say "What's the problem here?"
            "[bree.name] shakes her head at my words."
            "It's like she can't believe what she's hearing."
            $ bree.love -= 20
            $ bree.sub -= 5
            bree.say "Are you out of your tiny mind?"
            bree.say "That's a fucking dog collar!"
            bree.say "What am I supposed to do with that thing on, huh?"
            bree.say "Sniff your crotch?"
            bree.say "Piss and shit in public?!?"
            "[bree.name] holds up her hands in sheer frustration."
            "And she stamps her foot loudly on the ground."
            "I can't help jumping back."
            "As I'm wondering if she'll take a swing at me!"
            mike.say "Okay, [bree.name], okay!"
            mike.say "Message received!"
            mike.say "You don't like the collar - I get it!"
            bree.say "Do you, [hero.name]?"
            bree.say "Do you really?"
            bree.say "Because shit like this makes me wonder!"
            "With that, [bree.name] turns on her heel and storms off."
            "Which leaves me alone, still clutching the collar."
            "Part of me's not sure of all that just happened here."
            "Did I really misjudge the situation that badly?"
            "And if so, have I damaged my relationship with [bree.name]?"
            "Maybe even damaged it beyond hope of repair?"
            $ bree.flags.gone = True
            $ bree.flags.goneDelay = TemporaryFlag(1, "day")
            $ bree.hide()
            $ hero.cancel_activity()
    return

label bree_gift_sexy_dress_male:
    show bree happy
    bree.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy dress."
    if bree.sub >= 30:
        show bree flirt blush
        bree.say "Thank you [hero.name]."
        $ bree.flags.sexydate = True
        $ bree.flags.sluttydate = False
    else:
        show bree annoyed
        $ bree.love -= 4
        bree.say "Thanks but no thanks [hero.name], I would feel very awkward with that..."
        $ hero.cancel_activity()
    return

label bree_gift_slutty_dress_male:
    show bree talkative
    bree.say "Hey, [hero.name]..."
    bree.say "What's that you got there, huh?"
    show bree normal
    "[bree.name] seems to pop up in front of me like she's appeared out of thin-air."
    "Seriously, one minute she's nowhere to be seen, and then she's right in my face."
    "Making me jump and struggle to hide what I'm carrying behind my back."
    mike.say "AARGH!"
    mike.say "What the..."
    "[bree.name] makes to dart behind me, and I only just manage to keep up with her."
    "Dancing around in an awkward circle and feeling like a harassed crab."
    show bree talkative
    bree.say "Oh come on, [hero.name]..."
    bree.say "I can see it's got wrapping paper and a bow on it."
    bree.say "So it's got to be a present."
    bree.say "And if it's not for me, why are you hiding it?"
    show bree evil
    "I can see that [bree.name]'s not going to be convinced."
    "And the fact is she's one hundred percent correct."
    "So what's the point in keeping up the charade?"
    mike.say "Okay, okay..."
    mike.say "You win, [bree.name] - you've worn me down!"
    "I produce the box and hand it over to [bree.name]."
    "Who instantly starts to jump up and down on the spot."
    show bree surprised
    bree.say "Oh wow!"
    bree.say "Thank you so much, [hero.name]!"
    bree.say "This is so..."
    bree.say "Oh man!"
    show bree stuned
    "[bree.name] pulls out the daring dress that I stashed in the box so that it unfolds."
    "And then she stares at the thing in what seems to be total amazement."
    show bree normal
    "But when she doesn't seem to be saying anything, I feel the need to speak up."
    mike.say "So..."
    mike.say "I take it the silence is, like, stunned astonishment?"
    mike.say "That you're totally blown away?"
    if bree.sub >= 70:
        "[bree.name] seems to be jolted out of her trance by the sound of my voice."
        "And she's nodding her head even before she says a word in response."
        show bree smile
        bree.say "Yeah, [hero.name]..."
        bree.say "Totally blown away by how daring you are!"
        bree.say "Seriously, I'd never have thought of something like this."
        show bree happy
        "I watch with growing delight as [bree.name] holds the dress up against herself."
        "Because I can see just how much she seems to like the look of it."
        show bree flirt
        bree.say "But now I think I've been missing out!"
        "I'm nodding my head eagerly as [bree.name] says all of this."
        "Still struggling to believe that she's really so enthusiastic."
        mike.say "Well it's not all my doing, [bree.name]."
        mike.say "Without you, I'd never even have thought of it."
        mike.say "It was the mental image of you in something like that..."
        mike.say "That's what inspired me to take a leap of faith."
        "[bree.name] fixes me with a stare that's almost smouldering."
        "And now I can see that she's got an almost hungry smile on her face too."
        show bree talkative
        bree.say "We need an excuse for me to wear this thing, [hero.name]..."
        bree.say "And we need it fast!"
        show bree flirt
        mike.say "Whoa..."
        mike.say "Okay, okay..."
        mike.say "I'm racking my brain, going as fast as I can!"
        "And that's not an exaggeration either, as my brain is genuinely racing."
        "Desperately trying to think up a plan on the fly."
        "Because there's nothing I want more right now than to see [bree.name] in that dress!"
        $ bree.flags.sexydate = False
        $ bree.flags.sluttydate = True
    else:
        "[bree.name] seems to be jolted out of her trance by the sound of my voice."
        "And she's shaking her head even before she says a word in response."
        show bree vangry
        bree.say "Yeah, [hero.name]..."
        bree.say "Totally blown away by how bad your taste in dresses is!"
        show bree angry
        "I can't help feeling more than a little deflated by [bree.name]'s response."
        "Because sure, the dress is pretty dramatic, but it's not totally slutty."
        "In fact I'd say it's more avant garde than anything else."
        mike.say "Really, [bree.name]?"
        mike.say "I thought you were more broad-minded than that!"
        show bree vangry
        bree.say "Well you sound so broad-minded your brain fell out!"
        bree.say "Man, I hope you kept the receipt for this thing."
        show bree angry
        "With that, [bree.name] shoves the dress back into my open hands."
        "And she walks off, shaking her head and muttering under her breath."
        $ bree.love -= 10
        $ hero.cancel_activity()
    return

label bree_gift_butt_plug_male:
    show bree happy
    bree.say "Oh, [hero.name], is it for me?"
    "She unwraps the butt plug."
    if bree.sub <= 50 or not bree.sexperience:
        show bree annoyed
        bree.say "..."
        bree.say "Keep it... I don't want it so keep it."
        bree.say "I'm sure you'll have a better use of it than me."
        $ hero.cancel_activity()
    else:
        show bree normal blush
        bree.say "It's perfect!"
        show bree flirt
        bree.say "Thanks [hero.name], I'll make a good use of it."
        $ bree.flags.buttplug = True
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
