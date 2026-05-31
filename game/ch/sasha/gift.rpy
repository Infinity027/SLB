init python:
    Event(**{
    "name": "sasha_give_a_gift",
    "label": "npc_give_a_gift",
    "conditions": [
        Or(
            HeroTarget(IsBirthday()),
            IsSpecialDate("christmas"),
            IsSpecialDate("valentine"),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "girl": "sasha",
    "once_day": True,
    "do_once": False,
    "quit": False,
    }
    )

label sasha_give_male:
    if "skill_book_massage" not in hero.inventory and sasha.sub <= 25 and not hero.has_skill("massage"):
        $ gift = "skill_book_massage"
        "She hands me a pretty large book."
        mike.say "Wow!\nIs that a book about massages?"
        sasha.say "It sure is..."
        mike.say "Thank you so much."
    elif "dildo" not in hero.inventory and sasha.love >= 50:
        $ gift = "dildo"
        "She hands me a small box."
        mike.say "A dildo?"
        sasha.say "I am pretty sure you know how to use it."
        mike.say "Thank you I guess."
    elif "anal_beads" not in hero.inventory and sasha.sub >= 25 and sasha.love >= 25:
        $ gift = "anal_beads"
        "She hands me a small box."
        mike.say "Anal beads?"
        sasha.say "It goes in the butt, if you wonder."
        mike.say "Thank you I guess."
    elif "handcuffs" not in hero.inventory and sasha.sub >= 25:
        $ gift = "handcuffs"
        "She hands me a small box."
        mike.say "Handcuffs?"
        sasha.say "So you can play cops."
        mike.say "Thank you I guess."
    elif "bondage_ropes" not in hero.inventory and sasha.sub >= 50:
        $ gift = "bondage_ropes"
        "She hands me a small box."
        mike.say "Ropes?"
        sasha.say "They are made to tie up girls, willing ones preferably."
        mike.say "Thank you I guess."
    else:
        $ gift = "cake"
        "She hands me a box, obviously from a pastry shop."
        mike.say "Thanks."
    $ hero.gain_item(gift)
    return

label sasha_give_valentine_male:
    "Sasha walks confidently towards me."
    call sasha_greet from _call_sasha_greet_3
    show sasha blush
    sasha.say "Happy valentine's day [hero.name]..."
    call sasha_give_male from _call_sasha_give_male
    return

label sasha_give_birthday_male:
    "Sasha walks towards me."
    call sasha_greet from _call_sasha_greet_4
    show sasha happy
    sasha.say "Happy birthday [hero.name]!"
    call sasha_give_male from _call_sasha_give_male_1
    return

label sasha_give_christmas_male:
    "Sasha walks towards me."
    call sasha_greet from _call_sasha_greet_6
    show sasha happy
    sasha.say "Merry Christmas [hero.name]."
    call sasha_give_male from _call_sasha_give_male_2
    return

label sasha_birthday_gift_male:
    show sasha
    if sasha.flags.birthdayknown:
        mike.say "Happy birthday Sasha."
        sasha.say "How sweet, you remembered my birthday!"
    else:
        sasha.say "How do you know my birthday?"
        mike.say "I didn't, it's just pure luck."
        $ sasha.flags.birthdayknown = True
    return

label sasha_christmas_gift_male:
    show sasha
    mike.say "Merry Christmas Sasha."
    sasha.say "Thanks!"
    $ sasha.love += 2
    return

label sasha_valentine_gift_male:
    show sasha
    mike.say "Happy valentine's day Sasha."
    sasha.say "Thank you."
    $ sasha.love += 2
    return

label sasha_gift_swimsuit_male:
    show sasha happy
    sasha.say "Oh, [hero.name], is it for me?"
    "She unwrap the sexy swimsuit."
    if sasha.sub >= 60:
        show sasha blush
        sasha.say "It's so pretty, thank you so much [hero.name]."
        $ sasha.flags.sexyswimsuit = True
    else:
        show sasha angry
        $ sasha.love -= 2
        sasha.say "Thanks but no thanks [hero.name], I am not that eager to fuel your fantasies."
        $ hero.cancel_activity()
    return

label sasha_gift_sexy_dress_male:
    show sasha happy
    sasha.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy dress."
    if sasha.sub >= 30:
        show sasha blush
        sasha.say "Thank you [hero.name]."
        $ sasha.flags.sexydate = True
        $ sasha.flags.sluttydate = False
    else:
        show sasha sad
        $ sasha.love -= 2
        sasha.say "Dream on perv, I won't wear that..."
        $ hero.cancel_activity()
    return

label sasha_gift_slutty_dress_male:
    "Sasha's a daring sort of girl, right?"
    "I mean, she listens to heavy metal, dresses in black and plays guitar in a band."
    "So that means she's got to be more than a little broad-minded when it comes to clothes, doesn't it?"
    "Yeah, you guessed it - someone went and bought a certain kind of dress for the lady in question."
    "The kind of dress that leapt out at me the moment I saw it, and would make Sasha look incredible."
    "The only problem is that it'd be doing so by leaving almost nothing to the imagination."
    "Now I have the dress in a gift-wrapped box that's hidden behind my back."
    "And I need to figure out how to convince Sasha that wearing it is a good idea."
    "That it's not just me being some kind of massive perv as well."
    show sasha talkative
    sasha.say "Hey, [hero.name]…"
    sasha.say "Watcha got there?"
    show sasha normal
    "Oh shit!"
    "She's already here - and she's spotted the box too!"
    mike.say "Ah..."
    mike.say "Hi, Sasha!"
    mike.say "How are you doing on this fine, fine day?"
    "Sasha doesn't seem to be the least bit interested in my attempts a small-talk."
    "Instead she instantly tries to sneak a look behind my back."
    "Which results in me doing a weird, sideways kind of crab walk to hide it."
    show sasha talkative
    sasha.say "What are you talking about?"
    sasha.say "Of course I'm fine!"
    sasha.say "You're the one that's being weird in that sweaty kind of way."
    show sasha joke
    sasha.say "Aha...got it!"
    show sasha normal
    mike.say "HEY!"
    "Sasha plucks the box out of my hands, then dances out of my reach."
    play sound [paper_ripping_1, paper_ripping_2]
    "And I'm forced to watch as she begins to open it in front of me."
    mike.say "Sasha!"
    mike.say "How do you know that's even for you?!?"
    show sasha joke
    sasha.say "Oh come on, [hero.name]…"
    sasha.say "How many other girls are you seeing besides me?"
    sasha.say "Wait...don't answer that!"
    show sasha normal
    "Sasha gets the box open and pulls out the dress as finishes speaking."
    "And then she falls silent as she gets a good look at the whole thing."
    "Which is perfectly understandable, as it's much more racy then most of her wardrobe."
    "And if she were to have it on, literally every inch of her body would be on display."
    mike.say "Surprise, Sasha!"
    mike.say "I hope you like it?"
    if sasha.sub >= 70:
        show sasha stuned
        "Sasha's eyes have gone as wide as saucers by now."
        "And she's running her hand up and down the dress."
        show sasha surprised
        sasha.say "This is crazy..."
        sasha.say "This is totally crazy!"
        show sasha stuned
        mike.say "Erm..."
        mike.say "Is that crazy as in good, or crazy as in bad?"
        "Sasha looks up at me, shaking her head."
        show sasha joke
        sasha.say "Crazy as in good, obviously!"
        show sasha embarrassed
        "I feel a wave of relief wash over me."
        "And I can't help voicing that same feeling."
        mike.say "Thank god for that!"
        mike.say "I was worried that you'd hate it."
        show sasha joke
        sasha.say "Are you kidding?!?"
        sasha.say "I've always wanted to own a dress like this."
        sasha.say "But somehow I never got round to buying one."
        show sasha flirt
        "I don't know if I believe Sasha's explanation."
        "Or if she's using it as an excuse to hide her own timidity."
        "But in the end it doesn't really matter."
        "All that does matter is the fact she likes the dress."
        mike.say "So..."
        mike.say "When are you going to wear it?"
        show sasha shy
        sasha.say "Oh, don't worry, [hero.name]…"
        sasha.say "It'll be soon, and you'll be there to see it too."
        $ sasha.flags.sluttydate = True
        $ sasha.flags.sexydate = False
    else:
        show sasha stuned
        "Sasha's eyes have gone as wide as saucers by now."
        "And she's running her hand up and down the dress."
        show sasha annoyed
        sasha.say "This is awful..."
        sasha.say "This is totally awful!"
        show sasha angry
        "I feel a wave of despair wash over me."
        "But when Sasha thrusts the dress back into my hands, I take it."
        mike.say "I..."
        mike.say "I just thought that..."
        mike.say "Well, you're kind of into rebellious stuff, yeah?"
        show sasha vangry
        sasha.say "There's rebellious, and there's whorish!"
        sasha.say "And just for the record - this is whorish."
        show sasha angry
        "All I can do is stand there and nod my head."
        mike.say "Okay, Sasha..."
        mike.say "Maybe I can take it back and get a refund."
        mike.say "Or even ask them for store credit if not."
        $ sasha.love -= 10
        $ hero.cancel_activity()
    return

label sasha_gift_collar_male:
    show sasha
    sasha.say "Oh, [hero.name], is it for me?"
    "Sasha sits up, reaching for the wrapped gift."
    menu:
        "Hand it over":
            "I lean down and give her the box."
            $ sasha.love += 2
        "Tease her":
            "I lean back and look down at her with a smirk."
            mike.say "How bad do you want it?"
            if sasha.sub < 25:
                "Sasha blinks, then quirks a wry eyebrow at me."
                sasha.say "Not bad enough to stroke your ego to get them. The room's already crowded with you, me, and your ego as it is."
                "I snicker at her comment."
                mike.say "Touché."
                "Handing the box over, I enjoy seeing her smile at the gift."
                $ sasha.love += 1
            else:
                "Sasha blinks, then sticks her lower lip out at me playfully."
                sasha.say "So bad. Please can't I have it?"
                "She's so cute when she begs."
                "I hand the box over, pleased to see her happy smile."
                $ sasha.love += 2
                $ sasha.sub += 2
    "After a few moments of looking at the box she starts unpacking it and get the collar out."
    "I wish I could see her expression, but with her head lowered, those big dark eyes are impossible to read."
    if sasha.sub < 0:
        show sasha happy
        sasha.say "Oh! This is beautiful..."
        "Sasha says, unfastening the buckle and unwinding the collar from around the stems. She looks at me with a catlike grin."
        sasha.say "I think it'll just barely fit you. Give me the key and we can go play."
        "She purrs."
        mike.say "That wasn't what I had in mind."
        mike.say "Oh, the collar is for you. The key is for me."
        "Sasha snickers and shakes her head."
        sasha.say "I only do it the other way around. Nice try though."
        $ sasha.love -= 2
        $ hero.cancel_activity()
        return
    elif hero.charm + sasha.love < 150:
        $ sasha.set_sex_slave()
        sasha.say "Wow, [hero.name]."
        "She looks at me a little uncertainly."
        sasha.say "This collar is gorgeous. Must have cost a pretty penny."
        "Looks like I presumed a little too much."
        mike.say "Nah, it didn't set me back much. Besides, it'll look awesome on you!"
        "I grin, voice a bit joking."
        mike.say "And it'll match everything you own."
        "I take the key from my pocket and hand it over."
        hide sasha
        show sasha happy
        "Sasha grins happily and takes the key, then cinches the collar around her neck. I was right; it does look amazing on her."
        sasha.say "Thanks so much, [hero.name]! It's gorgeous."
        $ sasha.love += 2
    elif hero.charm + sasha.love >= 150 and sasha.sub < 90:
        $ sasha.set_sex_slave()
        "Looks like Sasha's not ready to be a good pet after all."
        "Maybe she can be encouraged in that direction down the line."
        "I don't want her to think poorly of me for pushing, so I pull the key out of my pocket and hold it out to her."
        mike.say "I saw it and thought it would look amazing on you."
        "Sasha grins happily and takes the key, then cinches the collar around her neck. I was right; it does look amazing on her."
        sasha.say "Thanks so much, [hero.name]! It's gorgeous."
        hide sasha
        show sasha happy
        "She gives me a flirtatious wink."
        sasha.say "Maybe you'll get a present from me pretty soon too."
        $ sasha.love += 2
        $ sasha.sub += 2
    else:
        $ sasha.set_sex_slave()
        sasha.say "Oh... it's beautiful. Do you have the key?"
        "I nod, dipping my fingers into my pocket to flash the key at her briefly before putting it away, already feeling a little thrill at how she's reacting to her gift."
        "And, of course, anticipation of putting it on her."
        sasha.say "Can I wear it now?"
        hide sasha
        show sasha happy
        "I go over and take the collar, then step behind the couch to loop it carefully around her neck and buckle it."
        "She lets out a little sigh as she hears the lock click."
        $ sasha.love += 2
        $ sasha.sub += 5
    return

label sasha_gift_butt_plug_male:
    show sasha happy
    sasha.say "Oh, [hero.name], is it for me?"
    "She unwraps the butt plug."
    if sasha.sub <= 50 or not sasha.sexperience:
        show sasha annoyed
        sasha.say "..."
        sasha.say "Keep it... I don't want it so keep it."
        sasha.say "I'm sure you'll have a better use of it than me."
        $ hero.cancel_activity()
    else:
        show sasha blush
        sasha.say "It's perfect!"
        show sasha flirt
        sasha.say "Thanks [hero.name], I'll make a good use of it."
        $ sasha.flags.buttplug = True
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
