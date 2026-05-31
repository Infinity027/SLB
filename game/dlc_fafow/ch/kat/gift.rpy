label kat_birthday_gift_male:
    show kat
    mike.say "Surprise, Kat!"
    mike.say "I got you a little something - hope you like it."
    show kat happy
    kat.say "Oh, [hero.name], you remembered my birthday!"
    if kat.flags.birthdayknown:
        mike.say "Well you did tell me the date, Kat."
        mike.say "And I made a special effort to remember."
        show kat smile
        kat.say "That's so great of you - everyone else seems to forget it!"
    else:
        mike.say "Ah...no, Kat!"
        mike.say "To be honest, I didn't - I just wanted to treat you."
        show kat smile
        kat.say "Wow...what a weird coincidence!"
        $ kat.flags.birthdayknown = True
    return

label kat_birthday_gift_female:
    show kat
    bree.say "Surprise, Kat!"
    bree.say "I got you a little something - hope you like it."
    show kat happy
    kat.say "Oh, [hero.name], you remembered my birthday!"
    if kat.flags.birthdayknown:
        bree.say "Well you did tell me the date, Kat."
        bree.say "And I made a special effort to remember."
        show kat smile
        kat.say "That's so great of you - everyone else seems to forget it!"
    else:
        bree.say "Ah...no, Kat!"
        bree.say "To be honest, I didn't - I just wanted to treat you."
        show kat smile
        kat.say "Wow...what a weird coincidence!"
        $ kat.flags.birthdayknown = True
    return

label kat_gift_swimsuit_male:
    show kat
    mike.say "Ah, Kat..."
    mike.say "I got you a little something!"
    show kat happy
    "Kat smiles in surprise as I hand her the gift."
    "She wastes no time in opening it."
    "And then she holds up the contents."
    show kat surprised blush
    kat.say "Oh..."
    kat.say "It really is a LITTLE something!"
    mike.say "Well, swimsuits aren't supposed to be big and bulky, Kat!"
    mike.say "So what do you think?"
    if kat.sub >= 70:
        "I can see that Kat's blushing a little."
        "And I get that, as a swimsuit's a pretty intimate gift."
        "For a moment I think she's going to reject it."
        show kat smile -blush
        "But then a look of determination comes over her face."
        "And she gives me a firm nod."
        kat.say "I wouldn't normally wear something like this."
        show kat shy blush
        kat.say "But as you went to the trouble of picking it out for me..."
        show kat happy
        kat.say "I think I should give it a try."
        $ kat.flags.sexyswimsuit = True
    else:
        show kat shy blush
        $ kat.love -= 4
        "Kat's cheeks are already burning with embarrassment."
        "And I understand that, as it's a pretty intimate gift."
        "But I thought that she might make a special effort this time."
        "Especially as it was a gift from me."
        show kat angry -blush
        "But then a look of determination comes over Kat's face."
        "And she shakes her head like she means it."
        kat.say "If I choose to wear something like this..."
        kat.say "Then it'll be my choice alone."
        show kat normal
        kat.say "I'm sorry, [hero.name]."
        kat.say "But I can't accept this."
        $ hero.cancel_activity()
    return

label kat_gift_collar_male:
    show kat
    "I've been waiting for the right moment to give my gift to Kat."
    "And it's one that represents a pretty bug risk on my part."
    "So there's no small amount of nerves involved on my end too."
    "But I'm committed now, and there's no way I'm backing out."
    mike.say "Surprise, Kat!"
    mike.say "I got you a little something - hope you like it."
    show kat surprised
    kat.say "Oh, [hero.name]!"
    show kat happy
    kat.say "How thoughtful of you!"
    "I hand over the box and then watch with baited breath."
    "Kat opens it up and pulls out what's inside."
    show kat surprised
    show fx exclamation
    "She holds it in her hands, staring in amazement."
    kat.say "It's..."
    kat.say "It's a collar..."
    hide fx
    kat.say "It looks like a dog collar!"
    if kat.sub >= 90:
        "Kat looks up at me with amazement in her eyes."
        kat.say "But..."
        show kat happy
        kat.say "But how did you know?"
        kat.say "I never told anyone that I wanted this!"
        "All I can do is shrug and smile."
        mike.say "I don't know what to tell you, Kat."
        mike.say "I just got a feeling, that's all."
        show kat close smile
        "Kat hands me the collar and waits patiently while I put it on."
        $ kat.set_sex_slave()
        "And then she adjusts it a little, beaming with pride."
        show kat happy
        $ kat.love += 2
        $ kat.sub += 5
        kat.say "I love it!"
        kat.say "I'm never going to take it off!"
    else:
        show kat normal
        "Kat looks up at me with a confused expression in her eyes."
        kat.say "But..."
        show fx drop
        kat.say "I don't have a dog!"
        mike.say "Ah, no, Kat..."
        mike.say "It's for you to wear!"
        hide fx
        show kat surprised
        "Kat drops the collar and takes a step away from me."
        kat.say "But...why?"
        kat.say "Why would you want me to wear a collar?"
        mike.say "I just...thought you were into that kind of thing!"
        show kat angry
        $ kat.love -= 20
        $ kat.sub -= 20
        kat.say "Well I'm not."
        kat.say "So I won't be wearing it!"
        $ hero.cancel_activity()
    return

label kat_gift_sexy_dress_male:
    show kat
    mike.say "Surprise, Kat!"
    mike.say "I got you a gift!"
    show kat surprised
    "Kat looks at me with genuine surprise on her face."
    "And it's a few seconds before she actually takes it from me."
    kat.say "Oh wow..."
    kat.say "That's so unexpected, [hero.name]!"
    show kat smile
    kat.say "Thank you."
    show kat surprised
    show fx exclamation
    "As soon as she opens it up, Kat gasps."
    "Then she holds the thing up against herself."
    hide fx
    kat.say "It's a dress!"
    kat.say "A really beautiful dress too!"
    if kat.sub >= 50:
        kat.say "I..."
        show kat shy blush
        kat.say "I never picked out anything like this before!"
        mike.say "I know it's a bit daring, Kat."
        mike.say "And I'll understand if you don't want to wear it..."
        "Kat shakes her head, dismissing my concerns."
        show kat smile -blush
        kat.say "No, no, no..."
        kat.say "If you want to see me in this..."
        show kat happy blush
        kat.say "Then I want to wear it!"
        "Kat smiles as she folds the dress back into the box."
        "And I can't help smiling at the thought of seeing her in it too."
        $ kat.flags.sluttydate = False
        $ kat.flags.sexydate = True
    else:
        kat.say "I..."
        show kat shy
        kat.say "I never picked out anything like this before!"
        mike.say "I know it's a bit daring, Kat."
        mike.say "And I'll understand if you don't want to wear it..."
        show kat smile
        "Kat looks at me with relief written all over her face."
        kat.say "I don't want to sound ungrateful, [hero.name]..."
        kat.say "But I just don't think I could ever wear this!"
        "I nod and force a smile onto my face."
        "And I watch Kat as she folds the dress back into the box."
        "I guess I misjudged the situation pretty badly right there."
        $ hero.cancel_activity()
    return

label kat_gift_slutty_dress_male:
    show kat
    mike.say "Surprise, Kat!"
    mike.say "I got you a gift!"
    show kat surprised
    "Kat looks at me with genuine surprise on her face."
    "And it's a few seconds before she actually takes it from me."
    kat.say "Oh wow..."
    kat.say "That's so unexpected, [hero.name]!"
    show kat smile
    kat.say "Thank you."
    show kat surprised
    show fx exclamation
    "As soon as she opens it up, Kat gasps."
    "Then she holds the thing up against herself."
    hide fx
    kat.say "It's a dress!"
    kat.say "A pretty daring dress too!"
    if kat.sub >= 80:
        kat.say "I..."
        show kat shy blush
        kat.say "I never picked out anything like this before!"
        mike.say "I know it's a bit risque, Kat."
        mike.say "And I'll understand if you don't want to wear it..."
        "Kat shakes her head, dismissing my concerns."
        show kat smile -blush
        kat.say "No, no, no..."
        kat.say "If you want to see me in this..."
        show kat happy blush
        kat.say "Then I want to wear it!"
        "Kat smiles as she folds the dress back into the box."
        "And I can't help smiling at the thought of seeing her in it too."
        $ kat.flags.sexydate = False
        $ kat.flags.sluttydate = True
    else:
        kat.say "I..."
        show kat shy
        kat.say "I never picked out anything like this before!"
        mike.say "I know it's a bit risque, Kat."
        mike.say "And I'll understand if you don't want to wear it..."
        show kat smile
        "Kat looks at me with relief written all over her face."
        kat.say "I don't want to sound ungrateful, [hero.name]..."
        kat.say "But I just don't think I could ever wear this!"
        "I nod and force a smile onto my face."
        "And I watch Kat as she folds the dress back into the box."
        "I guess I misjudged the situation pretty badly right there."
        $ hero.cancel_activity()
    return

label kat_gift_butt_plug_male:
    show kat happy
    kat.say "Oh, [hero.name], is it for me?"
    "She unwraps the butt plug."
    if kat.sub <= 50 or not kat.sexperience:
        show kat annoyed
        kat.say "..."
        kat.say "Keep it... I don't want it so keep it."
        kat.say "I'm sure you'll have a better use of it than me."
        $ hero.cancel_activity()
    else:
        show kat normal blush
        kat.say "It's perfect!"
        kat.say "Thanks [hero.name], I'll make a good use of it."
        $ kat.flags.buttplug = True
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
