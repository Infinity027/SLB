init python:
    Event(**{
    "name": "samantha_give_a_gift",
    "label": "npc_give_a_gift",
    "conditions": [
        Or(
            HeroTarget(IsBirthday()),
            IsSpecialDate("christmas"),
            IsSpecialDate("valentine"),
            ),
        PersonTarget(samantha,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "girl": "samantha",
    "once_day": True,
    "do_once": False,
    "quit": False,
    }
    )

label samantha_give_male:
    if "charm_book" not in hero.inventory and randint(1, 2) == 1:
        $ gift = "charm_book"
        "She hands me a book."
        mike.say "'How to talk to girls and have fun at parties'?"
        samantha.say "To help you get a girlfriend."
        mike.say "Thank you..."
    elif "funny_shirt" not in hero.inventory:
        $ gift = "funny_shirt"
        "She hands me a 'greatest gay best friend' shirt."
        mike.say "..."
        samantha.say "Come on [hero.name] it's funny!"
        mike.say "Maybe..."
    else:
        $ gift = "cake"
        "She hands me a box, obviously from a pastry shop."
        mike.say "Thanks."
    $ hero.gain_item(gift)
    return

label samantha_give_valentine_male:
    "Samantha walks hesitantly towards me."
    call samantha_greet from _call_samantha_greet_7
    show samantha close flirt
    samantha.say "Happy valentine's day [hero.name]..."
    "Samantha throws a box of chocolates towards me."
    if samantha.flags.nickname == "cupcake":
        mike.say "Thank you, Cupcake."
    else:
        mike.say "Thank you, Samantha."
    $ hero.gain_item("valentine_chocolates")
    hide samantha close
    show samantha flirt
    return

label samantha_give_birthday_male:
    "Samantha walks towards me."
    call samantha_greet from _call_samantha_greet_8
    show samantha close happy
    samantha.say "Happy birthday [hero.name]!"
    call samantha_give_male from _call_samantha_give_male
    hide samantha close
    show samantha happy
    return

label samantha_give_christmas_male:
    "Samantha walks towards me."
    call samantha_greet from _call_samantha_greet_9
    show samantha close happy
    samantha.say "Merry Christmas [hero.name]."
    call samantha_give_male from _call_samantha_give_male_1
    hide samantha close
    show samantha happy
    return

label samantha_birthday_gift_male:
    show samantha
    if samantha.flags.birthdayknown:
        if samantha.flags.nickname == "cupcake":
            mike.say "Happy birthday Cupcake."
        else:
            mike.say "Happy birthday Samantha."
        samantha.say "How sweet, you remembered my birthday!"
    else:
        samantha.say "How do you know my birthday?"
        mike.say "I didn't, it's just pure luck."
        $ samantha.flags.birthdayknown = True
    return

label samantha_gift_swimsuit_male:
    show samantha happy
    samantha.say "Oh, [hero.name], is it for me?"
    "She unwrap the sexy swimsuit."
    if samantha.sub >= 60:
        hide samantha
        show samantha close flirt
        samantha.say "It's so pretty, thank you so much [hero.name]."
        hide samantha close
        show samantha flirt
        $ samantha.flags.sexyswimsuit = True
    else:
        show samantha annoyed
        samantha.say "I am sorry I can't wear that..."
        $ hero.cancel_activity()
    return

label samantha_gift_sexy_dress_male:
    show samantha happy
    samantha.say "Oh, [hero.name], is it for me?"
    "She unwrap the sexy dress."
    if samantha.sub >= 30:
        hide samantha
        show samantha close flirt
        samantha.say "It's so pretty, thank you so much [hero.name]."
        hide samantha close
        show samantha flirt
        $ samantha.flags.sexydate = True
        $ samantha.flags.sluttydate = False
    else:
        show samantha annoyed
        samantha.say "I am sorry I can't wear that..."
        $ hero.cancel_activity()
    return

label samantha_gift_slutty_dress_male:
    "I used to spend hours on end daydreaming about seeing Sam in certain outfits."
    "And more than a little time thinking about her out of them as well, if you get my meaning?"
    "But now that we're actually an item, I have the chance to make those fantasies a reality."
    "So I've resolved to act on them and put my money where my mouth is."
    "I walked into one of the swankiest clothes shops in the mall the other day and bought something."
    "Now I just have to hope that I've spent my hard-earned cash on something that Sam's going to like."
    "Because as soon as I walked in there I was drawn straight past all the run-of-the-mill stuff."
    "And I settled on what was perhaps the most adventurous and daring dress in the whole place."
    "Now I just have to hope that Sam's broad-minded enough to be into the thing."
    "Instead of just seeing me as some kind of depraved weirdo!"
    mike.say "Erm..."
    mike.say "Hi, Sam!"
    "At the sound of my voice, Sam looks up at me, a smile on her face."
    "And instantly I'm entranced by the sweetness of her smile and the warmth of her eyes."
    show samantha talkative
    samantha.say "Hello, [hero.name]!"
    samantha.say "Ooh..."
    samantha.say "What's that you've got there?"
    samantha.say "It wouldn't be a present for someone special, would it?"
    show samantha normal
    "Sure, Sam's being pretty forward in assuming that the box behind my back is for her."
    "But who the hell am I kidding?"
    "She's already managed to reel me in with her smile."
    "And now I'm totally in her power."
    mike.say "Ha, ha..."
    mike.say "Yeah, you got me, Sam..."
    mike.say "I bought you a little something."
    "I produce the box from behind my back and hold it out to Sam."
    "She takes it with a demure and grateful look on her face."
    "Which only serves to make my heart pound for her sake all the more."
    show samantha happy
    samantha.say "Thank you, [hero.name]."
    samantha.say "You didn't have to..."
    samantha.say "But it's very touching that you did."
    show samantha flirt
    play sound [paper_ripping_1, paper_ripping_2]
    "I keep on nodding as Sam begins to tear off the wrapping-paper."
    "And I manage to keep the smile on my face as she opens the box."
    show samantha stuned
    "Then I hear her gasp as she pulls out the dress and looks it over."
    "The very slinky, tight-fitting dress that promises to leave nothing to the imagination."
    mike.say "So, Sam..."
    mike.say "What do you think?"
    mike.say "Pretty daring, huh?"
    show samantha normal
    "She unwraps the slutty dress."
    if samantha.sub >= 70:
        "Sam looks up at me, her eyes wide with what I hope is amazement."
        "And then she slowly begins to shake her head."
        show samantha talkative
        samantha.say "This is pretty out there, [hero.name]…"
        samantha.say "But I think I like it."
        show samantha happy
        "It takes me a moment to realise that Sam's being positive."
        "And when I finally do, the words just come gushing out of me."
        mike.say "You..."
        mike.say "You mean you like it?"
        mike.say "Oh my god, that's such a relief!"
        mike.say "I was terrified that you'd hate it..."
        mike.say "That you'd think..."
        "Sam holds up a hand and waves it in front of my face."
        "A gesture that I eventually realise means she wants me to shut up."
        show samantha flirt
        samantha.say "Calm down, [hero.name]…"
        samantha.say "You're starting to babble!"
        samantha.say "But yes, I do like it."
        samantha.say "Ryan would never have let me out in something like this."
        samantha.say "He was paranoid that other guys would look at me if he did."
        samantha.say "This tells me that you appreciate my body, but that you trust me too."
        show samantha blush
        "I nod eagerly, only really skimming the surface of what Sam's saying."
        "More interested in the fact that she's going to wear it than anything else."
        $ samantha.flags.sluttydate = True
        $ samantha.flags.sexydate = False
    else:
        show samantha annoyed
        $ samantha.love -= 4
        "Sam looks up at me, her eyes wide with what I hope is amazement."
        "And then she slowly begins to shake her head."
        show samantha surprised
        samantha.say "This is pretty out there, [hero.name]…"
        samantha.say "And I don't think that I can wear it."
        show samantha upset
        "I feel my hopes die inside of me as Sam hands the dress back."
        "But there doesn't seem to be any point in trying to change her mind."
        "I can see from the look on her face that her mind is made up."
        "And pushing her on something as risqué as this just feels like a bad idea."
        "So I take the dress and nod my head."
        mike.say "Okay, Sam..."
        mike.say "Maybe I can take it back and get a refund."
        mike.say "Or even ask them for store credit if not."
        $ samantha.love += 10
        $ hero.cancel_activity()
    return

label samantha_gift_collar_male:
    show samantha
    mike.say "If someone had asked me about you even as recently as a couple of months ago, I'd have described you as the one that got away."
    mike.say "The girl that I was always secretly in love with, but too much of a coward to ever tell her just how I felt."
    mike.say "But I've been lucky enough to get a second chance with you."
    mike.say "And, I know it's been messy, what with Ryan, the wedding and all of that stuff..."
    "Sam starts to say something, most likely an attempt to dismiss what I'm saying or assure me that the chaotic mess that all of this began with wasn't my fault."
    "I hold up a hand to gently ask her to hold off and let me finish what I want to say before she objects."
    if samantha.flags.nickname == "cupcake":
        mike.say "I know...I know what you're going to say, Cupcake."
    else:
        mike.say "I know...I know what you're going to say, Sam."
    mike.say "That it couldn't have been helped and it's all for the better."
    mike.say "And you're right, it is all for the better."
    mike.say "But I want to make sure that things go right from here on in, make sure we don't make the same mistakes over again."
    "I take a deep breath, steeling myself for what I know has to come next."
    if samantha.flags.nickname == "cupcake":
        mike.say "I'm not going to keep things between us under wraps any more, Cupcake."
    else:
        mike.say "I'm not going to keep things between us under wraps any more, Sam."
    mike.say "No more sneaking around behind people's backs or keeping our feelings for each other a secret."
    mike.say "I'd...I'd like to ask you to wear something that will show people that you're mine, make a statement that can't be mistaken for what it is."
    "I can see that Sam almost looks to be holding her breath right now, waiting for me to show her just what it is that I want her to wear."
    "Gathering all of the courage that I can muster, I reach into my pocket and pull it out."
    "Holding both ends of the blue leather strap in either hand, I let her see the collar for the very first time."
    "The light catches the pendant that hangs in the middle, making its curved lines for a moment unrecognizable as the cupcake it's supposed to represent."
    "For a moment, Sam's eyes are wider than ever and she remains silent as she takes in just what it is that I want her to wear."
    "And then she blinks a couple of times and her lips start to move once more."
    samantha.say "B...but...[hero.name] - that looks like a dog-collar?!?"
    "I nod at her words, unable to argue with the truth of what she's saying."
    if samantha.flags.nickname == "cupcake":
        mike.say "Well, that's because it is, Cupcake."
    else:
        mike.say "Well, that's because it is, Sam."
    "She looks at me as though I've suddenly begun to speak a foreign language, her eyes showing her incomprehension."
    samantha.say "You're asking me to do what...to pretend to be your dog?!?"
    if samantha.flags.nickname == "cupcake":
        mike.say "It might be a dog-collar, Cupcake - but that's not what you wearing it would symbolise."
    else:
        mike.say "It might be a dog-collar, Sam - but that's not what you wearing it would symbolise."
    samantha.say "It's not?"
    "I shake my head fervently at this."
    mike.say "No, of course not - it's more of a declaration that you belong to me, that you're well and truly spoken for."
    "She looks at me in a way that tells me she's less than convinced with the logic behind the whole idea."
    if samantha.sub < 90 or not "samantha_event_E01" in DONE:
        $ samantha.love -= 20
        $ samantha.sub -= 20
        show samantha angry
        "Her entire face darkens and she scowls at me with an expression of disgust the likes I've rarely seen her show in all the time I've known her."
        samantha.say "Thanks for showing me what was really going on inside of that sick head of yours the whole time!"
        "And with that, she storms off, leaving me standing alone with the collar still clutched between my fingers."
        $ hero.cancel_activity()
    else:
        "Maybe a change of approach is required here, something that she can more easily relate to from her own experience of such matters..."
        mike.say "You remember how you used to wear the engagement ring that Ryan gave you?"
        "I know that bringing his name into this is risky in the extreme, but I'm determined to either hit the jackpot or go bust on this one."
        "Sam nods, still not sure of just where I'm going with this whole thing."
        mike.say "Well that symbolised your commitment to each other - or lack of it, on his side at least."
        mike.say "This collar symbolises my feelings for you."
        mike.say "But it's not just a ring on your finger that you can slip off when it's convenient or hide when you want to flirt without it getting in the way."
        mike.say "It's bigger and more intense than what you had with Ryan, and I want everyone to see that collar and know just how strong our bond is."
        if samantha.flags.nickname == "cupcake":
            mike.say "We're bound together now, Cupcake - and that collar's a symbol of the connection between us!"
        else:
            mike.say "We're bound together now, Sam - and that collar's a symbol of the connection between us!"
        "I can see Sam weighing up the merits of what I've just said to her as she ponders in silence for a moment which drags on into minutes."
        "But then she looks up at me with a strange kind of openness in her eyes, almost as if she were waiting for me to say something more to her."
        "After an awkward period of silence, I can't stand it any longer."
        if samantha.flags.nickname == "cupcake":
            mike.say "Cupcake, say something...please!"
        else:
            mike.say "Sam, say something...please!"
        samantha.say "Well, I was just thinking back over what's happened since you came back into my life."
        samantha.say "I thought that I was happy before, but you showed me how I'd been living a lie all that time."
        samantha.say "It hurt, but since I left Ryan, things have only gotten better for me - and that's all been down to you."
        "Sam looks at me again with that same look in her eyes, and only now do I see it for what it is - submission."
        show samantha happy
        $ samantha.set_sex_slave()
        samantha.say "I'd be pretty dumb to stop listening to you now, after all that you've done to make my life so much happier - wouldn't I?"
        "I can't help but nod enthusiastically, as Sam tells me exactly what I want to hear right now."
        "She smiles nervously and holds up her hair so that I can fasten the collar around her neck, not tight enough to choke her, but tight enough so that she always knows it's there."
        hide samantha
        show samantha
        "Sam looks down at the pendant and flicks it playfully with her finger."
        samantha.say "Aww, a cupcake - [hero.name], you always did tease me for having a sweet tooth!"
        if samantha.flags.nickname == "cupcake":
            mike.say "Ah, it's probably better that you call me 'Master' whenever you have the collar on, Cupcake."
        else:
            mike.say "Ah, it's probably better that you call me 'Master' whenever you have the collar on, Sam."
        mike.say "And I'll call you Cupcake."
        $ samantha.flags.nickname = "cupcake"
        mike.say "But we can worry about the finer details of things like that when we start your obedience training, okay?"
        "The look on Sam's face at the throwaway tone of my comment is mostly surprise, though I'm sure there's also a hint of intrigued mixed in there as well."
    return

label samantha_gift_butt_plug_male:
    show samantha happy
    samantha.say "Oh, [hero.name], is it for me?"
    "She unwraps the butt plug."
    if samantha.sub <= 50 or not samantha.sexperience:
        show samantha annoyed
        samantha.say "..."
        samantha.say "Keep it... I don't want it so keep it."
        samantha.say "I'm sure you'll have a better use of it than me."
        $ hero.cancel_activity()
    else:
        show samantha normal blush
        samantha.say "It's perfect!"
        show samantha flirt
        samantha.say "Thanks [hero.name], I'll make a good use of it."
        $ samantha.flags.buttplug = True
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
