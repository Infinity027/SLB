init python:
    Equip("minami_sweater", display_name="Minami's sweater", effects={"minami": 100, "charm": -5})
    Consumable("siscon_book", display_name="Sis xXx Kiss", price=100, effects=[("siscon", 5), ("time", 4)], frequency_limit="week", conditions=[HeroTarget(MinStat("energy", 2), MinStat("hunger", 2), MinStat("grooming", 2), MinStat("fun", 2))])

    Event(**{
    "name": "minami_give_a_gift",
    "label": "npc_give_a_gift",
    "conditions": [
        Or(
            HeroTarget(IsBirthday()),
            IsSpecialDate("christmas"),
            IsSpecialDate("valentine"),
            ),
        PersonTarget(minami,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "girl": "minami",
    "once_day": True,
    "do_once": False,
    "quit": False,
    }
    )

label minami_give_male:
    if "zbox_360" not in hero.inventory:
        $ gift = "zbox_360"
        "She hands me a pretty large box."
        mike.say "Wow!\nIs that a Zbox?"
        minami.say "It sure is..."
        mike.say "Thank you so much."
    if minami.love >= 50 and "siscon_book" not in hero.inventory:
        $ gift = "siscon_book"
        "She hands me a sexy looking manga titled 'Sis xXx Kiss', what a weird name..."
        mike.say "It looks fun..."
        minami.say "You'll see it's very funny and romantic."
        mike.say "Thank you Minami."
    elif minami.love >= 25 and "minami_sweater" not in hero.inventory:
        $ gift = "minami_sweater"
        "She hands me a hand knit sweater, a rather failed attempt at a hand knit sweater anyway."
        mike.say "It's beautiful..."
        minami.say "Thanks [hero.name]."
        mike.say "Thank you Minami."
    else:
        $ gift = "cake"
        "She hands me a box, obviously from a pastry shop."
        mike.say "Thanks."
    $ hero.gain_item(gift)
    return

label minami_give_valentine_male:
    "Minami walks hesitantly towards me."
    call minami_greet from _call_minami_greet_7
    show minami blush
    minami.say "Happy valentine's day [hero.name]..."
    "Minami hands me a box of chocolates."
    mike.say "Thank you, Minami."
    $ hero.gain_item("valentine_chocolates")
    return

label minami_give_birthday_male:
    "Minami walks towards me."
    call minami_greet from _call_minami_greet_8
    show minami happy
    minami.say "Happy birthday [hero.name]!"
    call minami_give_male from _call_minami_give_male
    return

label minami_give_christmas_male:
    "Minami walks towards me."
    call minami_greet from _call_minami_greet_9
    show minami happy
    minami.say "Merry Christmas [hero.name]."
    call minami_give_male from _call_minami_give_male_1
    return

label minami_birthday_gift_male:
    show minami
    if minami.flags.birthdayknown:
        mike.say "Happy birthday, Minami!"
        mike.say "I hope you like what I got you."
        minami.say "Aw, big bro - you remembered my birthday!"
        minami.say "You really are the BEST!"
    else:
        minami.say "Huh - how did you know it was my birthday?"
        minami.say "You NEVER used to remember my birthday!"
        mike.say "I almost didn't this time too."
        mike.say "I just guessed and must have got it right this time!"
        $ minami.flags.birthdayknown = True
    return

label minami_christmas_gift_male:
    show minami
    mike.say "Merry Christmas, Minami."
    mike.say "What, you didn't think I'd forget, did you?!?"
    minami.say "Well, you always did back home!"
    minami.say "But thanks, big bro - it's sweet that you remembered now."
    minami.say "It just goes to show how much closer we've gotten..."
    $ minami.love += 2
    return

label minami_valentine_gift_male:
    show minami
    mike.say "Happy valentine's day, Minami."
    mike.say "I hope you like it - I spent ages picking it out!"
    minami.say "Oh, it's perfect!"
    minami.say "Thank you for making me feel so special!"
    $ minami.love += 2
    return

label minami_gift_swimsuit_male:
    if not minami.siscon >= 100:
        "No I just can't give that to my little sister..."
        $ hero.cancel_activity()
        return
    show minami
    if minami.sub >= 60:
        mike.say "Erm, hey, Minami..."
        mike.say "I bought you something for the beach."
        mike.say "Or the pool, or the waterpark, or any place you want to wear it..."
        minami.say "Ooh, that looks SO sexy!"
        minami.say "Can't you just see me in it already!"
        $ minami.flags.sexyswimsuit = True
    else:
        mike.say "Erm, hey, Minami..."
        mike.say "I bought you something for the beach."
        mike.say "Or the pool, or the waterpark, or any place you want to wear it..."
        minami.say "Eww!"
        minami.say "That looks WAY too revealing!"
        minami.say "No...thank...you!"
        $ minami.love -= 4
        $ hero.cancel_activity()
    return

label minami_gift_slutty_dress_male:
    if not minami.siscon >= 100:
        "No I just can't give that to my little sister..."
        $ hero.cancel_activity()
        return
    $ dress = "slutty"
    call minami_gift_sexy_dress_2 from _call_minami_gift_sexy_dress_2
    return

label minami_gift_sexy_dress_male:
    if not minami.siscon >= 100:
        "No I just can't give that to my little sister..."
        $ hero.cancel_activity()
        return
    $ dress = "sexy"
    call minami_gift_sexy_dress_2 from _call_minami_gift_sexy_dress_2_1
    return

label minami_gift_sexy_dress_2:
    "The moment that she sees the gift-wrapped present that I'm holding, Minami's eyes light up."
    "It's not like I had a hope of actually hiding it behind my back anyway."
    "And it's worth seeing the look of surprise and anticipation on her face too!"
    show minami happy
    minami.say "Ooh, big bro!"
    minami.say "What's that you have there?"
    "I can't help smiling at the way Minami tries to act all innocent and unassuming."
    "It just makes the opportunity to give her a gift that much more enjoyable."
    mike.say "Well, let's just say that I might have seen something in a shop window."
    minami.say "Uh-huh!"
    mike.say "And I might have thought it'd look good on someone."
    minami.say "Yeah...yeah?"
    mike.say "And I might have bought it for that same person..."
    minami.say "Oh, big bro - you're killing me!"
    "I shake my head, unable to keep from laughing."
    "Minami looks and sounds like she's going to burst."
    "I hold out the package to her, nodding as I do so."
    mike.say "Here you go, Minami."
    mike.say "Of course it's for you!"
    "I watch as Minami eagerly takes the present from my hands."
    "She doesn't pause for a second, beginning to unwrap it immediately."
    "Pretty soon she has the paper off and the box open."
    "And then she holds up what was inside, staring at it wide-eyed."
    show minami normal
    minami.say "Whoa..."
    minami.say "This is...this is..."
    minami.say "Well, it's not what I was expecting!"
    "I get what Minami's saying as she looks the dress up and down before me."
    "In the past, she's never been afraid of wearing anything that's revealing."
    "But this is a far more adult and daring cut than she's used to."
    "And it's revealing in a whole different way too."
    "Of course, I think she'll look hot as hell in it."
    "That's the entire reason that I bought it for her in the first place!"
    "I just hope that Minami feels the same way too..."
    if (minami.sub >= 30 and dress == "sexy") or (minami.sub >= 70 and dress == "slutty"):
        "Minami holds the dress against herself to check the fit."
        "And then she looks up at me, catching my eye as she does so."
        "She seems to read my mind, to know just what I'm thinking right now."
        "Minami knows how much I want to see her in that damn dress!"
        show minami happy
        minami.say "You can already see me in it - can't you, big bro?"
        minami.say "Mmm...it's so grown-up, not like the stuff I usually wear."
        minami.say "But then maybe that's what makes you like it so much, huh?"
        "Minami presses the dress against herself."
        "And then she does this little shimmy that I swear makes my cock twitch."
        minami.say "You'd be able to see everything in this dress."
        minami.say "Every inch of me would be on show, big bro."
        show minami tehe
        minami.say "But you already know that, right?"
        minami.say "Because you've pictured it, haven't you?"
        minami.say "And you're thinking about it right now!"
        "Minami throws her arms around my waist, hugging me tight."
        "And I can't help feeling how she rubs herself against my groin too!"
        show minami happy
        minami.say "Oh, thanks, big bro!"
        minami.say "I can't wait to wear it for you!"
        if dress == "sexy":
            $ minami.flags.sluttydate = False
            $ minami.flags.sexydate = True
        elif dress == "slutty":
            $ minami.flags.sexydate = False
            $ minami.flags.sluttydate = True
    else:
        "Minami cocks her head on one side and screws up her face."
        "And then she sticks her tongue out in an expression of disgust."
        show minami annoyed
        minami.say "Eww!"
        minami.say "I can't wear this, big bro."
        minami.say "It'd make me look like a hundred years old!"
        "And with that, Minami thrusts the whole thing back into my hands."
        "She rolls her eyes and shakes her head at me."
        minami.say "And it's not like I don't have a full wardrobe already, is it?"
        "I nod too, trying to hide my disappointment."
        mike.say "Y...yeah, Minami."
        mike.say "What was I thinking!"
        minami.say "Did you keep the receipt?"
        minami.say "Maybe we could exchange it for something cute?"
        minami.say "Something like a Japanese schoolgirl's uniform?"
        "I swallow audibly as I nod."
        "And I'm already starting to think some good might come out of this..."
        $ minami.love -= 4
        $ hero.cancel_activity()
    return

label minami_gift_collar_male:
    if not minami.siscon >= 100:
        "No I just can't give that to my little sister..."
        $ hero.cancel_activity()
        return
    show minami
    "I honestly thought that I'd gotten over the nervous energy that I feel whenever I'm around Minami."
    "That sense of danger that comes from the fact that our relationship is, in the eyes of some, a taboo."
    "But almost as soon as I made up my mind to go ahead with what I intend to do today, it returned with a vengeance."
    "Now, as I stand here waiting for her to turn up, I can feel the same butterflies in my stomach and the dizziness that I remember."
    "In fact, I have such a tight grip on the box in my hands that I can feel it threatening to crumple in my hands."
    "It's only a small box, and it weighs next to nothing."
    "But I feel like that belies the importance of what's inside."
    "And if I'm right, it's exactly the kind of gesture that Minami's looking for from me."
    "If not, well..."
    "No, I'll deal with that if and when the situation arises."
    "I won't go letting my head get filled with those kind of negative thoughts before there's any need."
    minami.say "Hey, big bro!"
    minami.say "I came as soon as I could."
    minami.say "So, what's so important that it just couldn't wait?"
    "I take a deep breath as I prepare to launch into the speech that I've prepared."
    "But I find myself pausing to take a long look at Minami as she stands before me."
    "It's as if a part of me still can't believe that she's now my girlfriend, rather than just my adopted sister."
    "And I used to think that such an idea would freak me out, always seem like it was just so wrong."
    "Now it's like I was in such a state of denial, as what we have feels so natural, so right."
    mike.say "I...I have a little something for you, Minami."
    mike.say "A gift that I think you're going to like."
    "Minami's eyes go wide as she stares down at the box, still clutched in my hands."
    minami.say "Oh, wow!"
    minami.say "That's so sweet of you, big bro!"
    "To my surprise, I see that tears are threatening to well in the corner of her eyes."
    mike.say "Minami..."
    mike.say "Are you okay?"
    minami.say "Oh...what..."
    "Minami shakes her head and hastily wipes the tears out of her eyes."
    minami.say "It's nothing, big bro."
    minami.say "Just that no one ever bought me jewellery like this before!"
    minami.say "I guess...I guess no one ever loved me like you do!"
    "More than a little surprised by this unexpected show of emotion, I thrust the box towards Minami."
    mike.say "You really should open it."
    mike.say "Before you get carried away with your emotions!"
    "Minami nods, eagerly accepting the box and tearing away the wrapping."
    "She opens it with a similar amount of speed and enthusiasm, plucking the contents up as soon as they become visible."
    "Minami holds the black leather choker that was inside of the box up to study it in the light."
    "Simple in design, it's plain and unadorned, save for a red forbidden symbol in the middle of its length."
    mike.say "I want you to wear it wherever you go, Minami."
    mike.say "It's a symbol of our relationship, and it's forbidden nature."
    mike.say "Something to let everyone that sees you know that you belong only to me."
    if minami.sub < 90:
        "Minami looks up at me with a nervous smile on her face, as if she really doesn't know what to say."
        "She keeps on holding my eye and grinning in the same manner as she shoves the collar back into the box."
        mike.say "What's the matter, Minami?"
        mike.say "Don't you like it?"
        mike.say "Is it the colour - because if it is, I can get that changed!"
        "Minami shakes her head a little too hastily for me to take her subsequent answer seriously."
        minami.say "No, no, no..."
        minami.say "It's just...too much for this outfit I have on - that's it!"
        minami.say "Something like this needs to be figured in when you're picking clothes out."
        minami.say "You can't just throw it on, or else it'll overpower everything..."
        "I realise that Minami's babbling now, saying whatever comes into her head."
        "All I can do is nod in agreement as I try to keep my disappointment from showing."
        "It looks like I misjudged this one pretty badly!"
        mike.say "Well...it's yours to do with as you like, Minami."
        mike.say "Like I said - it's just a little gift from me to you..."
        "Now we both have pained grins etched onto our faces, and neither of us knows what to say next."
        "So in the end I can only excuse myself and skulk away, head hanging low with embarrassment."
        $ minami.love -= 10
        $ hero.cancel_activity()
    else:
        show minami blush
        "For what feels like an eternity, Minami just stares down at the collar in her hands."
        "She remains silent, making the whole thing that much worse as I wait for her reaction."
        "But when she finally does move again, it's to drop the box and fasten the collar around her neck."
        "Minami has it in place within the blink of an eye, and then raises her chin as she makes some final adjustments."
        "And then she lowers her head, gazing at me with a deliberately submissive expression on her face."
        minami.say "Mmm..."
        minami.say "I always wondered what this would feel like."
        minami.say "To be collared and treated like someone's property..."
        "She continues to sigh and moan, as if the thought is literally turning her on more with each second that passes."
        "I can't help notice how one of her hands is tugging at the collar, testing the way it feels."
        "And the other is sliding ever closer to her waist, threatening to slip below it..."
        mike.say "That's what you are now, Minami."
        mike.say "You're mine, and no one else has a claim on you."
        "At this, Minami actually makes a strained sound from between her open lips."
        "And it's as though my words are getting her hotter than ever."
        $ minami.set_sex_slave()
        hide minami
        show minami blush close
        minami.say "Oh, big bro..."
        minami.say "I never wanted anything as much as I want this!"
        show minami hunt close
        "Minami pauses for a moment, looking down in embarrassment."
        minami.say "Ah, big bro?"
        mike.say "What is it, Minami?"
        minami.say "Does it come with a leash?"
        $ minami.love += 2
        $ minami.sub += 5
    return

label minami_gift_butt_plug_male:
    show minami happy
    minami.say "Oh, [hero.name], is it for me?"
    "She unwraps the butt plug."
    if minami.sub <= 50 or not minami.sexperience:
        show minami annoyed
        minami.say "..."
        minami.say "Keep it... I don't want it so keep it."
        minami.say "I'm sure you'll have a better use of it than me."
        $ hero.cancel_activity()
    else:
        show minami normal blush
        minami.say "It's perfect!"
        show minami flirt
        minami.say "Thanks [hero.name], I'll make a good use of it."
        $ minami.flags.buttplug = True
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
