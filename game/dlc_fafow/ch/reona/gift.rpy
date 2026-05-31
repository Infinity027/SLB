label reona_birthday_gift_male:
    show reona
    mike.say "I got you a little something, Reona..."
    reona.say "Oh wow, thanks, [hero.name]!"
    reona.say "How did you know it was my birthday?"
    if reona.flags.birthdayknown:
        mike.say "You told me yourself, remember?"
        "Reona rolls her eyes and chuckles."
        reona.say "I guess I did - I can be such a scatter-brain!"
    else:
        mike.say "Actually, Reona, I didn't!"
        mike.say "I just wanted to give you a gift and it's a total coincidence."
        reona.say "Whoa...that's SO weird!"
        $ reona.flags.birthdayknown = True
    return

label reona_gift_collar_male:
    show reona
    "I know that I'm taking a gamble giving a gift like this to Reona."
    "But she just seems to be putting out those kind of vibes all the time."
    "And if I'm right, then this could be the start of something amazing."
    "Let's just hope that I'm not wrong!"
    mike.say "Ah, Reona..."
    show reona surprised
    reona.say "Oh, [hero.name]..."
    reona.say "Is that a gift for me?"
    "I grin awkwardly as I hand it over to Reona."
    show reona normal
    play sound [paper_ripping_1, paper_ripping_2]
    "And I'm still smiling as she opens it and pulls out the contents."
    "Which just so happen to be a collar, like the kind you put on a dog."
    if reona.sub >= 90:
        reona.say "[hero.name]..."
        $ reona.love += 2
        $ reona.sub += 5
        show reona normal
        reona.say "How did you know?!?"
        show reona happy
        reona.say "I always wanted to wear one of these!"
        reona.say "And be someone's...well, someone's bitch!"
        "I feel a flood of relief at Reona's positive reaction."
        "But at the same time I'm also getting pretty turned-on too!"
        "Because she's obviously into the idea in a big way!"
        mike.say "I think I got the size right."
        mike.say "You can try it on later, if you like?"
        show reona flirt
        "Reona shakes her head and thrusts the collar towards me."
        reona.say "No, no, no!"
        reona.say "I want you to put it on me now!"
        "I'm more than happy to oblige."
        $ reona.set_sex_slave()
        "And I waste no time in fastening the collar around Reona's neck."
        "She smiles the whole time, almost bursting with joy once it's in place."
    else:
        show reona surprised
        reona.say "You got me a dog-collar?"
        $ reona.love -= 20
        $ reona.sub -= 20
        show reona angry
        reona.say "What the fuck is that about?!?"
        mike.say "I...thought you might want to wear it?"
        show reona surprised
        "Reona looks at me in sheer amazement."
        reona.say "And why would I want to do that?"
        show reona angry
        reona.say "Do I look like a dog to you?"
        mike.say "No, Reona - of course not!"
        "Reona rolls her eyes as she hands the collar back to me."
        reona.say "You know what, [hero.name]..."
        reona.say "You can be a real weirdo sometimes!"
        $ hero.cancel_activity()
    return

label reona_gift_swimsuit_male:
    show reona
    mike.say "Erm...hey, Reona..."
    mike.say "I got you something!"
    play sound [paper_ripping_1, paper_ripping_2]
    "I hand the package over to Reona, and she opens it without hesitation."
    "And then she holds up the swimsuit that's inside, studying it with interest."
    mike.say "So, what do you think - nice, huh?"
    if reona.sub >= 70:
        show reona happy
        reona.say "I think that I like it!"
        reona.say "Can't wait for the chance to try it out."
        "The smile on Reona's face makes me crack one too."
        mike.say "I'm so glad you like it, Reona."
        mike.say "And I can't wait to see you in it too!"
        $ reona.flags.sexyswimsuit = True
    else:
        show reona annoyed
        reona.say "I think I don't need your help to pick out a swimsuit!"
        "Reona unceremoniously shoves the swimsuit back into my hands."
        mike.say "But...I thought you liked that kind of thing?!?"
        reona.say "I do, [hero.name], I do."
        reona.say "But like I said, I can choose my own clothes!"
        $ hero.cancel_activity()
    return

label reona_gift_sexy_dress_male:
    show reona
    "I'm feeling more than a little nervous as I hand the gift to Reona."
    show reona surprised
    "She looks surprised at the unexpected gesture on my part."
    "And I can only hope that surprise will turn to delight when she sees what I got her."
    reona.say "What's this, [hero.name]?"
    reona.say "A gift for me?"
    mike.say "I hope you like it, Reona."
    mike.say "I just saw it and thought of you!"
    show reona normal
    play sound [paper_ripping_1, paper_ripping_2]
    "Reona opens the package and takes out what's inside."
    show reona surprised
    reona.say "Oh wow..."
    reona.say "It's a dress."
    reona.say "One hell of a sexy dress!"
    if reona.sub >= 50:
        show reona happy
        reona.say "Oh wow!"
        reona.say "This is so nice!"
        "Reona holds the dress up against herself."
        "And I can already see her sizing it up."
        reona.say "So classy too!"
        reona.say "I don't have anything this posh!"
        "I smile and try to ignore the fact I thought it was quite trashy."
        "If Reona's that into it, then I'm not going to stop her gushing."
        mike.say "I'm glad you like it, Reona."
        mike.say "And I can't wait to see you wear it."
        reona.say "Oh, don't worry..."
        reona.say "You won't have to wait long for that!"
        $ reona.flags.puredate = False
        $ reona.flags.sluttydate = False
        $ reona.flags.sexydate = True
    else:
        show reona annoyed
        reona.say "But you're going to have to take it back!"
        "Reona hands the whole thing back to me as she says this."
        "And I'm more than a little thrown by her reaction."
        mike.say "What's the matter, Reona?"
        mike.say "Don't you like it?"
        "Reona chuckles and shakes her head."
        reona.say "Sure, it's a nice dress."
        reona.say "But I chose everything in my wardrobe myself."
        reona.say "And it works for me."
        reona.say "So just leave my clothes to me, okay?"
        $ hero.cancel_activity()
    return

label reona_gift_slutty_dress_male:
    show reona
    "I can feel the palms of my hands getting sweaty."
    "But I try to ignore that fact as I clutch the gift in them."
    "And I hand it over to Reona the first chance that I get."
    mike.say "Here you go, Reona..."
    mike.say "I got you a little something."
    show reona surprised
    reona.say "For me?"
    reona.say "Aw, thanks, [hero.name]!"
    show reona happy
    play sound [paper_ripping_1, paper_ripping_2]
    "Reona happily accepts the gift and starts to open it."
    show reona surprised
    "Then I watch with baited breath as she pulls out the contents."
    reona.say "It's a dress..."
    reona.say "It's a very daring dress!"
    if reona.sub >= 80:
        show reona happy
        reona.say "Wow!"
        reona.say "This is perfect!"
        "I can't help smiling as I feel a surge of relief."
        mike.say "I'm so glad you like it, Reona!"
        mike.say "I was worried that you'd think it was..."
        mike.say "Well...too revealing!"
        show reona surprised
        "Reona looks genuinely puzzled at this."
        reona.say "Huh?"
        reona.say "What are you talking about?"
        show reona happy
        reona.say "This is way more classy than most of the stuff I wear!"
        reona.say "I'm gonna feel like a real fucking lady in this!"
        $ reona.flags.puredate = False
        $ reona.flags.sexydate = False
        $ reona.flags.sluttydate = True
    else:
        show reona annoyed
        reona.say "But you're going to have to take it back!"
        "Reona hands the whole thing back to me as she says this."
        "And I'm more than a little thrown by her reaction."
        mike.say "What's the matter, Reona?"
        mike.say "I thought you liked that kind of thing?"
        "Reona chuckles and shakes her head."
        reona.say "Sure I do. [hero.name]."
        reona.say "But I chose everything in my wardrobe myself."
        reona.say "And it works for me."
        reona.say "I don't need any help to show off what I got!"
        $ hero.cancel_activity()
    return

label reona_gift_sexy_underwear_male:
    show reona happy
    reona.say "Oh, [hero.name], is it for me?"
    "She unwraps the revealing underwear."
    if reona.purity < 20 and reona.sub >= 50:
        show reona blush
        reona.say "Thank you [hero.name]."
        $ reona.flags.sexyunderwear = True
    else:
        show reona annoyed
        $ reona.love -= 4
        reona.say "Thanks but no thanks [hero.name], I would feel very awkward with that..."
        $ hero.cancel_activity()
    return

label reona_gift_pure_date_male:
    show reona happy
    reona.say "Oh, [hero.name], is it for me?"
    "She unwraps the beautiful dress."
    if reona.purity >= 60:
        show reona blush
        reona.say "Thank you [hero.name]."
        $ reona.flags.sluttydate = False
        $ reona.flags.sexydate = False
        $ reona.flags.puredate = True
    else:
        show reona annoyed
        $ reona.love -= 4
        reona.say "Thanks but no thanks [hero.name], I would feel very awkward with that..."
        $ hero.cancel_activity()
    return

label reona_gift_pure_casual_male:
    show reona happy
    reona.say "Oh, [hero.name], is it for me?"
    "She unwraps the beautiful dress."
    if reona.purity >= 50:
        show reona blush
        reona.say "Thank you [hero.name]."
        $ reona.flags.purecasual = True
    else:
        show reona annoyed
        $ reona.love -= 4
        reona.say "Thanks but no thanks [hero.name], I would feel very awkward with that..."
        $ hero.cancel_activity()
    return

label reona_gift_butt_plug_male:
    show reona happy
    reona.say "Oh, [hero.name], is it for me?"
    "She unwraps the butt plug."
    if reona.sub <= 50 or not reona.purity <= 25 or not reona.sexperience:
        show reona annoyed
        reona.say "..."
        reona.say "Keep it... I don't want it so keep it."
        reona.say "I'm sure you'll have a better use of it than me."
        $ hero.cancel_activity()
    else:
        show reona normal blush
        reona.say "It's perfect!"
        show reona flirt
        reona.say "Thanks [hero.name], I'll make a good use of it."
        $ reona.flags.buttplug = True
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
