init python:
    Event(**{
    "name": "kleio_give_a_gift",
    "label": "npc_give_a_gift",
    "conditions": [
        Or(
            HeroTarget(IsBirthday()),
            IsSpecialDate("christmas"),
            IsSpecialDate("valentine"),
            ),
        PersonTarget(kleio,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "girl": "kleio",
    "once_day": True,
    "do_once": False,
    "quit": False,
    }
    )

label kleio_give_male:
    if "cool_sunglasses" not in hero.inventory:
        $ gift = "cool_sunglasses"
        "She hands me a small box."
        mike.say "Wow!\nThose glasses looks great!"
        mike.say "Thank you so much."
    elif kleio.love >= 50 and "military_boots" not in hero.inventory:
        $ gift = "military_boots"
        "She hands me a pair of boots."
        mike.say "They look fantastic."
        kleio.say "You're welcome [hero.name]."
    else:
        $ gift = "cake"
        "She hands me a box, obviously from a pastry shop."
        mike.say "Thanks."
    $ hero.gain_item(gift)
    return

label kleio_give_valentine_male:
    "Kleio walks hesitantly towards me."
    call kleio_greet from _call_kleio_greet_7
    show kleio
    kleio.say "Happy valentine's day [hero.name]..."
    "Kleio throws a box of chocolates towards me."
    mike.say "Thank you, Kleio."
    $ hero.gain_item("valentine_chocolates")
    return

label kleio_give_birthday_male:
    "Kleio walks towards me."
    call kleio_greet from _call_kleio_greet_8
    show kleio happy
    kleio.say "Happy birthday [hero.name]!"
    call kleio_give_male from _call_kleio_give_male
    return

label kleio_give_christmas_male:
    "Kleio walks towards me."
    call kleio_greet from _call_kleio_greet_9
    show kleio happy
    kleio.say "Merry Christmas [hero.name]."
    call kleio_give_male from _call_kleio_give_male_1
    return

label kleio_birthday_gift_male:
    show kleio
    if kleio.flags.birthdayknown:
        mike.say "Happy birthday Kleio."
        kleio.say "How sweet, you remembered my birthday!"
    else:
        kleio.say "How do you know my birthday?"
        mike.say "I didn't, it's just pure luck."
        $ kleio.flags.birthdayknown = True
    return

label kleio_gift_swimsuit_male:
    show kleio happy
    kleio.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy swimsuit."
    if kleio.sub >= 60:
        show kleio blush
        kleio.say "Thank you [hero.name]."
        $ kleio.flags.sexyswimsuit = True
    else:
        show kleio annoyed
        $ kleio.love -= 4
        kleio.say "Thanks but no thanks [hero.name], it's objectifying..."
        kleio.say "Even worse than being naked..."
        $ hero.cancel_activity()
    return

label kleio_gift_sexy_dress_male:
    show kleio happy
    kleio.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy dress."
    if kleio.sub >= 30:
        show kleio blush
        kleio.say "Thank you [hero.name]."
        $ kleio.flags.sexydate = True
        $ kleio.flags.sluttydate = False
    else:
        show kleio annoyed
        $ kleio.love -= 4
        kleio.say "Thanks but no thanks [hero.name], I would feel very awkward with that..."
        $ hero.cancel_activity()
    return

label kleio_gift_slutty_dress_male:
    "I feel like I should know Kleio well enough by now not to be getting myself into a situation like this."
    "I've dealt with all of her quirks already and been on the receiving end of her temper more than once too."
    "But for some reason I just couldn't help myself, as soon as I saw the damn thing in the window of the store."
    "Before I knew it, I was in there buying the thing, even asking them to gift-wrap it for me as well."
    "And now here I am, holding it behind my back and waiting for the right moment to spring my surprise on her."
    "All the time knowing that I might be about to make a pretty devastating mistake."
    "Yet pushing that fear aside every time I imagine the possibility of it going the other way instead."
    mike.say "Erm..."
    mike.say "Kleio?"
    show kleio talkative
    kleio.say "Yeah, Loverboy?"
    show kleio normal
    mike.say "I..."
    mike.say "I've got to tell you something."
    "Kleio raises a single eyebrow."
    show kleio talkative
    kleio.say "Let me guess..."
    kleio.say "Does it have something to do with that box?"
    kleio.say "The one you're failing to hide behind your back?"
    show kleio normal
    "I smile and let out a dumb-sounding laugh as I pull it out."
    "Shaking my head as I hand the box over to Kleio."
    mike.say "Oh boy..."
    mike.say "There are no flies on you, Kleio!"
    mike.say "Not that there would be - I'm sure you don't attract flies!"
    "Kleio looks at me with her usual withering frown."
    "But she takes the box from me all the same."
    show kleio talkative
    kleio.say "Okay..."
    kleio.say "So I take it this is...what, a gift?"
    kleio.say "You know most people explain that kind of thing when they hand it over?"
    show kleio normal
    mike.say "Oh yeah...oh course!"
    mike.say "That's exactly what it is - a gift, from me to you."
    play sound [paper_ripping_1, paper_ripping_2]
    "I watch as Kleio tears off the wrapping-paper and opens the box."
    "And I watch more intently still as she pulls out the contents."
    "Because now she's raising both of her eyebrows in genuine surprise."
    "Looking in amazement at the slinky dress that unfolds in her hands."
    "The slinky and also very revealing dress that I desperately want to see her in."
    mike.say "So..."
    mike.say "I'm guessing this is a bit of a surprise, yeah?"
    if kleio.sub >= 70:
        "Kleio's expression changes right in front of my eyes."
        "Going from surprise to knowing amusement in mere seconds."
        show kleio seductive
        kleio.say "Oh, I don't know about that, Loverboy..."
        kleio.say "It kinda figures that you'd want to see me in something like this."
        kleio.say "After all, you are a shameless little perv, aren't you?"
        show kleio shy
        "Just like that, Kleio switches things around on me."
        "Putting me on the spot and making me start to sweat."
        mike.say "Erm..."
        mike.say "Well..."
        mike.say "I just thought you'd look nice in it, you know?"
        "Kleio laughs out loud, throwing her head back as she does so."
        "And she tosses the dress over her shoulder, holding it there like a jacket."
        "A move that instantly reminds me of how much the damn thing cost!"
        show kleio talkative
        kleio.say "Tell you what, Loverboy..."
        kleio.say "I'll take this thing home with me."
        kleio.say "And I'll promise to wear it some time soon."
        kleio.say "But I'm not going to tell you when."
        show kleio seductive
        kleio.say "That way you get to see what makes you hot."
        kleio.say "And I get to stay in control of my own body."
        kleio.say "Deal?"
        show kleio shy
        "What else can I do but agree to Kleio's offer?"
        mike.say "It's a deal Kleio."
        "Kleio nods and holds out her hand."
        "Which I take and shake, already wondering when she's going to pull the trigger."
        $ kleio.flags.sluttydate = True
        $ kleio.flags.sexydate = False
    else:
        "Kleio's expression changes right in front of my eyes."
        "Going from surprise to tired irritation in mere seconds."
        show kleio angry
        kleio.say "Urgh..."
        kleio.say "I thought we were past this kind of shit, Loverboy?"
        kleio.say "I really thought you weren't one of those guys!"
        show kleio annoyed
        "Just like that, Kleio switches things around on me."
        "Putting me on the spot and making me start to sweat."
        mike.say "What do you mean?"
        mike.say "What kind of guy?"
        "Kleio shakes her head as she tosses the dress and the box back to me."
        "And I struggle to catch them before they land on the floor at my feet."
        show kleio angry
        kleio.say "The kind of guy who thinks he can tell me what to wear."
        kleio.say "Then starts to think that he can tell me what to do too."
        kleio.say "And before you think this is about the dress - it isn't."
        kleio.say "I might choose to wear something like that, but it'd be MY choice alone."
        kleio.say "So if you want this thing to work out between us..."
        kleio.say "Then you'd better get that through your thick skull, and quickly too!"
        show kleio annoyed
        $ kleio.love -= 10
        $ hero.cancel_activity()
    return

label kleio_gift_collar_male:
    "I knew that this idea was a gamble right from the start."
    "That if I've got it wrong, this could really blow up in my face."
    "But the vibes that I've been getting off of Kleio recently..."
    "Well, my gut just tells me that this is something that she could really be into."
    "And I already know just how hot under the collar the idea of it makes me feel too!"
    "But I still have to keep a lid on it until I can make my move."
    "If I don't choose just the right moment, it really will end in disaster!"
    kleio.say "Uh, Loverboy..."
    kleio.say "Are you feeling okay?"
    mike.say "Huh...what?"
    kleio.say "I said are you feeling okay?"
    kleio.say "You've been weird since we met up."
    kleio.say "It's like your body's here, but your mind's on another planet!"
    "Shit - I didn't want it to happen like this."
    "But she already figured that something's up with me."
    "I guess that means it's now or never..."
    mike.say "Ah..."
    mike.say "I kind of got you something, Kleio."
    mike.say "And I was waiting for the right moment to give it to you."
    "Kleio raises an eyebrow at this."
    "I can see that she's intrigued at the mention of a surprise gift."
    "But she's also trying to keep up her image at the same time."
    "It wouldn't do for her to look TOO eager."
    kleio.say "You soft bastard!"
    kleio.say "Why didn't you just say so?"
    mike.say "I...I guess I wanted it to be a surprise, Kleio."
    kleio.say "Go on then - hand it over!"
    "I try to look confident as I pass her the box."
    "But Kleio seems more intent on opening it than reading the expression on my face."
    kleio.say "What is it - a necklace or something?"
    mike.say "Well..."
    mike.say "That's not a million miles away!"
    "Kleio holds up the black leather choker that was inside of the box."
    "It's broad and studded with spikes that make it look like a dog collar."
    "A red pendant hangs from the front in the shape of the symbol for anarchy."
    mike.say "I just saw it the other day."
    mike.say "And I instantly thought of you..."
    if kleio.sub < 90:
        show kleio angry
        $ kleio.love -= 20
        $ kleio.sub -= 20
        kleio.say "What were you doing at that time, Loverboy?"
        kleio.say "Walking a dog?"
        kleio.say "I know - maybe you were browsing the local pet store!"
        mike.say "Ah...no, Kleio."
        mike.say "It's not what you think!"
        show kleio annoyed
        "Kleio cocks her head on one side, considering what I just said."
        kleio.say "It's not, huh?"
        kleio.say "Because it just says 'walkies' to me!"
        mike.say "Sure, it's a collar, Kleio."
        mike.say "But it's not a dog collar."
        mike.say "Because...because you're not a dog!"
        kleio.say "You sure, Loverboy?"
        kleio.say "You're not trying to tell me you want to discipline me?"
        kleio.say "You don't want me to beg for treats, yeah?"
        mike.say "Kleio, please..."
        show kleio d
        "Kleio shakes her head as she shoves the collar back into my open hands."
        kleio.say "Nice thought, Loverboy."
        kleio.say "But how about you let me pick my own accessories in future, okay?"
        $ hero.cancel_activity()
    else:
        show kleio happy
        $ kleio.love += 8
        $ kleio.set_sex_slave()
        kleio.say "You thought I needed a collar?"
        kleio.say "Like a dog?!?"
        mike.say "Ah...maybe not in so many words..."
        kleio.say "Oh, Loverboy."
        kleio.say "That is so....HOT!"
        mike.say "It...it is?!?"
        "I see Kleio almost shudder as she nods her head."
        kleio.say "It's like I'm a mean little bitch."
        kleio.say "A stray that you found on the street."
        mike.say "Uhm...okay, I guess!"
        $ kleio.sub += 4
        kleio.say "And you're gonna discipline me too."
        kleio.say "Break your little bitch in - good and proper!"
        hide kleio
        show kleio close
        "She's leaning in really close as she says all of this."
        "And I can see the look in her eye as she does so."
        kleio.say "And maybe you notice that she's in heat, your little bitch."
        kleio.say "Maybe you know just what she needs..."
        mike.say "I...I think I can guess what she needs!"
        kleio.say "Then you better give it to her, Loverboy!"
        kleio.say "Because this bitch bites!"
    return

label kleio_gift_butt_plug_male:
    show kleio happy
    kleio.say "Oh, [hero.name], is it for me?"
    "She unwraps the butt plug."
    if kleio.sub <= 50 or not kleio.sexperience:
        show kleio annoyed
        kleio.say "..."
        kleio.say "Keep it... I don't want it so keep it."
        kleio.say "I'm sure you'll have a better use of it than me."
        $ hero.cancel_activity()
    else:
        show kleio normal blush
        kleio.say "It's perfect!"
        show kleio flirt
        kleio.say "Thanks [hero.name], I'll make a good use of it."
        $ kleio.flags.buttplug = True
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
