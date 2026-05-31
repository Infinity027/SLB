label amy_birthday_gift_male:
    show amy surprised
    amy.say "Oh...what's this?"
    amy.say "You got me a gift?"
    show amy happy
    amy.say "That's so kind of you!"
    if amy.flags.birthdayknown:
        mike.say "Well, it is your birthday, Amy!"
        amy.say "You remembered?"
        amy.say "Aw, that's almost as good as getting a gift!"
    else:
        amy.say "You remembered it's my birthday!"
        mike.say "It is?!?"
        mike.say "I mean...of course it is!"
        $ amy.flags.birthdayknown = True
    return

label amy_gift_butt_plug_male:
    show amy happy
    amy.say "Oh, [hero.name], is it for me?"
    "She unwraps the butt plug."
    if amy.sub <= 50 or not amy.sexperience:
        show amy annoyed
        amy.say "..."
        amy.say "Keep it... I don't want it so keep it."
        amy.say "I'm sure you'll have a better use of it than me."
        $ hero.cancel_activity()
    else:
        show amy normal blush
        amy.say "It's perfect!"
        show amy flirt
        amy.say "Thanks [hero.name], I'll make a good use of it."
        $ amy.flags.buttplug = True
    return

label amy_gift_collar_male:
    show amy
    mike.say "Here you go, Amy..."
    mike.say "If I'm any judge of character, you're going to love this!"
    play sound [paper_ripping_1, paper_ripping_2]
    "Amy takes the gift from me and proceeds to tear it open."
    "Then she lifts up the contents, a collar, similar to that a dog would wear."
    show amy surprised
    amy.say "It's..."
    amy.say "It's a collar?"
    mike.say "Yeah, Amy - a collar for you to wear!"
    mike.say "Because I think that's the way this relationship's going."
    mike.say "Right?"
    if amy.sub >= 90:
        show amy shy
        "Amy doesn't hesitate to undo the collar and place it around her neck."
        amy.say "[hero.name], would you..."
        amy.say "Would you help me out here?"
        "I rush to do as she asks, fastening the collar in place."
        show amy happy
        "Once it's there, Amy looks down at it with a happy expression on her face."
        amy.say "Oh, [hero.name]..."
        $ amy.love += 2
        $ amy.sub += 5
        amy.say "How did you know?"
        mike.say "Ah, I just picked up on the hints you're always dropping."
        mike.say "Seems like I was on the right track too!"
        amy.say "Yeah...I could never have come right out and said it."
        $ amy.set_sex_slave()
        amy.say "And I'm glad you figured it out."
    else:
        $ amy.love -= 20
        $ amy.sub -= 20
        show amy upset
        "Amy doesn't hesitate to shove the collar and box into my chest."
        with hpunch
        "And she does it with some force too!"
        mike.say "OUCH!"
        mike.say "What the hell, Amy?"
        mike.say "I thought you were into that kind of thing?!?"
        show amy angry
        amy.say "What, just because I'm a goth?"
        amy.say "That doesn't mean that I want to be treated like an animal!"
        amy.say "I'm not a damn dog, [hero.name]!"
        amy.say "I'm a fucking human being!"
        amy.say "So how about you shove your gift up your ass?"
        $ hero.cancel_activity()
    return

label amy_gift_swimsuit_male:
    show amy
    mike.say "There you go, Amy..."
    mike.say "I hope you like it!"
    show amy surprised
    amy.say "You got me something to wear?"
    amy.say "And it's a swimsuit..."
    amy.say "A pretty revealing one too!"
    mike.say "Yeah..."
    mike.say "I just kinda saw it and thought of you!"
    if amy.sub >= 70:
        show amy happy
        "Amy holds the swimsuit up against herself and smiles."
        amy.say "This is amazing, [hero.name]!"
        amy.say "Seriously, you don't know how hard it is for a goth to find swim-wear!"
        mike.say "I'm glad you like it, Amy."
        mike.say "And I can't wait to see you wearing it!"
        $ amy.flags.sexyswimsuit = True
    else:
        show amy upset
        amy.say "Thought you'd like to see my tits in it, more like!"
        amy.say "Seriously, [hero.name], have you ever seen me in something like this?!?"
        with hpunch
        "Amy shoves the swimsuit back into my hands with some force."
        mike.say "Ouch!"
        amy.say "I hope you can get your money back on that thing!"
        $ hero.cancel_activity()
    return

label amy_gift_sexy_dress_male:
    show amy
    mike.say "There you go, Amy..."
    mike.say "I hope you like it!"
    show amy surprised
    amy.say "You got me something to wear?"
    amy.say "Oh, it's a dress..."
    amy.say "A very sexy dress!"
    mike.say "Yeah..."
    mike.say "When I saw it, I just thought of you!"
    if amy.sub >= 50:
        show amy happy
        "Amy looks at me with a knowing smile on her face."
        amy.say "I bet you did, [hero.name]!"
        amy.say "You know, I don't normally wear stuff like this?"
        mike.say "Oh...you can always take it back..."
        mike.say "You know, if you don't want to wear it?"
        show amy shy
        "Amy shakes her head at this."
        amy.say "I never said I wouldn't wear it."
        amy.say "And I kind of like that you want to see me in it too!"
        show amy happy
        amy.say "So I'm willing to make an exception."
        amy.say "Because I want to see the look on your face so badly!"
        $ amy.flags.sluttydate = False
        $ amy.flags.sexydate = True
    else:
        show amy upset
        "Amy glares at me as she shoves the dress back into my hands."
        mike.say "What's the problem, Amy?"
        mike.say "Did I get your size wrong?"
        show amy angry
        amy.say "No, [hero.name]..."
        amy.say "Just my entire image!"
        mike.say "Huh?"
        mike.say "What do you mean?"
        show amy upset
        amy.say "How many times have you seen me in something like this?"
        amy.say "It's not exactly my kind of look!"
        amy.say "So I take it you're saying I need to change my style?"
        mike.say "Yes...I mean no...I mean maybe?"
        $ hero.cancel_activity()
    return

label amy_gift_slutty_dress_male:
    show amy
    mike.say "There you go, Amy..."
    mike.say "I hope you like it!"
    show amy surprised
    amy.say "You got me something to wear?"
    amy.say "Oh, it's a dress..."
    amy.say "A very revealing dress!"
    mike.say "Yeah..."
    mike.say "When I saw it, I just thought of you!"
    if amy.sub >= 80:
        show amy happy
        "Amy looks at me with a knowing smile on her face."
        amy.say "I bet you did, [hero.name]!"
        amy.say "You know, I don't normally wear stuff this revealing?"
        mike.say "Oh...you can always take it back..."
        mike.say "You know, if you don't like it?"
        show amy shy
        "Amy shakes her head at this."
        amy.say "I never said I didn't like it."
        amy.say "And I kind of like that you want to see me in it too!"
        show amy happy
        amy.say "So I'm willing to make an exception."
        amy.say "Because I want to see the look on your face so badly!"
        $ amy.flags.sexydate = False
        $ amy.flags.sluttydate = True
    else:
        show amy upset
        "Amy frowns as she shoves the dress back into my open hands."
        mike.say "Whoa..."
        mike.say "What's the matter, Amy?"
        mike.say "Don't you like it?"
        show amy angry
        amy.say "Like it?!?"
        amy.say "There's more material goes into making a napkin!"
        amy.say "In future, how about you let me choose my own clothes, huh?"
        mike.say "Ah..."
        mike.say "Okay, Amy, if that's what you want..."
        $ hero.cancel_activity()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
