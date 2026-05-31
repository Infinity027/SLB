label peeping_result_female:
    $ hero.fun += 1





    return

label caught_peeping_dialogues_1_female(caught_girl):
    bree.say "Ah..."
    bree.say "H...hey, [caught_girl]!"
    bree.say "I was just..."
    bree.say "Just checking..."
    return

label vacuum_sasha_sleep_female:
    $ renpy.sound.play("sd/vacuum.ogg", loop=True)
    "There's nothing that I particularly look forward to getting assigned on the cleaning rota for the house."
    "But when it comes around to being my turn to use the vacuum-cleaner, it's at least a small mercy."
    "With the nozzle in one hand and pulling the rest of the thing behind me, I can hurry here and there."
    "It might be getting late, but if I'm as quick as usual, then I can be in bed in record time!"
    "With that in mind, I power through the rooms and head upstairs to finish off."
    stop sound
    "But I'm no more than halfway down the corridor when the vacuum-cleaner just seems to stop working."
    "Puzzled, I stare down the nozzle, wondering if something got jammed in there."
    "And that's when I hear the sound of someone coughing behind me."
    scene secondfloor
    show sasha sleep annoyed
    sasha.say "Ahem..."
    "I almost jump out of my skin before I realise it's just Sasha."
    "But then I get a better look at the expression on her face."
    "That and the fact she's in her pyjamas."
    "She regards me with an ominous air as she swings the vacuum-cleaner's plug in the air."
    bree.say "Oh...hi, Sasha."
    bree.say "Just getting on with the vacuuming, you know?"
    bree.say "Doing my part to keep the house clean!"
    "Sasha shakes her head like she's being spoken to by a complete moron."
    sasha.say "Yeah, I kind of gathered that, [hero.name]."
    sasha.say "What's bugging me is why you're doing it right now, huh?"
    sasha.say "Why are you doing it while I'm trying to sleep?"
    "I can already feel the guilt beginning to take a hold of me."
    "And it makes me start running off at the mouth a few moments later."
    bree.say "Oh..."
    bree.say "You were asleep?"
    bree.say "Sorry, Sasha - I didn't realise!"
    sasha.say "Oh, don't worry about that, [hero.name]."
    sasha.say "I'm not asleep anymore, thanks to you."
    sasha.say "And you should be a lot more concerned with something else."
    show sasha angry
    sasha.say "Namely where I'm going to stick this plug!"
    menu:
        "Apologise":
            "I'm about to open my mouth and argue the toss with Sasha."
            "But then I notice the tiredness in her eyes."
            "And I remember that I wasted most of the night on the Zbox."
            "She's right, I'm being a pretty selfish ass right now."
            bree.say "I...I'm sorry, Sasha."
            bree.say "You're right, I should have done this hours ago."
            bree.say "I'll finish up in the morning."
            "Sasha blinks, as though she doesn't quite believe what she's hearing."
            "But then I see her mood soften and she shakes her head."
            show sasha normal
            sasha.say "Thanks, [hero.name]."
            sasha.say "And I'm sorry too - for blowing up like that."
            sasha.say "I guess I'm extra tetchy right now!"
            "I nod, appreciating the change in her mood."
            bree.say "No problem, Sasha."
            bree.say "Just let me know if you need anything."
            "Sasha smiles as she passes me the plug to the vacuum-cleaner."
            sasha.say "I just might do that."
            sasha.say "But for now, all I need is some sleep."
            $ sasha.love += 1
            "I stand and wind the cord of the vacuum-cleaner around my arm."
            "Watching Sasha as she walks back to her room and closes the door."
            hide sasha
            "Even after so long living with housemates, I can still screw up."
            "Maybe I should make sure I do this kind of thing before I turn on the Zbox in future..."
        "Argue":
            "Geez, can't a girl catch a break around here?"
            "All I'm doing is making sure that I keep up my end of the cleaning!"
            "I'm pretty sure Sasha would be on my case if I wasn't too."
            "So what if I woke her up by accident?"
            "It's not as if she doesn't like to play heavy metal at maximum volume whenever she pleases!"
            bree.say "Aw, come on, Sasha."
            bree.say "Isn't the important thing that I'm doing it at all?"
            "I see an instant change in Sasha's mood."
            "And I know that I just messed up, big time!"
            "Before she looked pissed at me."
            show sasha vangry
            "But now I can see genuine irritation and annoyance flare in her eyes."
            sasha.say "Oh, so that's how it is, yeah?"
            sasha.say "We should be grateful you do your bit?"
            sasha.say "Grateful that you gets your hands dirty?!?"
            bree.say "No..."
            bree.say "Sasha, that's not what I meant!"
            sasha.say "Well that's what it sounded like from here."
            sasha.say "You know maybe if you spent less time on the Zbox."
            sasha.say "Then you wouldn't have to vacuum in the middle of the night!"
            $ sasha.love -= 1
            "Sasha underlines her point by shoving the plug into my stomach."
            "It's not quite a punch, but the blow's strong enough to make me gasp."
            hide sasha
            "I clutch for the plug as she turns her back on me and stalks away."
            "You know something, maybe she's right."
            "Maybe I should finish off the vacuuming in the morning..."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
