label cherie_birthday_gift_male:
    show cherie stuned
    "Cherie's eyes go wide with surprise as she takes the gift from me."
    show cherie surprised
    cherie.say "For me?"
    show cherie happy
    cherie.say "Oh my goodness, how thoughtful of you, [hero.name]!"
    if cherie.flags.birthdayknown:
        show cherie talkative
        cherie.say "I remember that I told you the date of my birthday."
        cherie.say "But I did not think that you would remember it."
        show cherie smile blush
        cherie.say "You must think a lot more of me than I realised!"
        show cherie normal -blush
    else:
        show cherie talkative
        cherie.say "And you will not believe this, really you will not."
        show cherie surprised
        cherie.say "But today just so happens to be my birthday!"
        show cherie happy
        cherie.say "This is an incredible coincidence, is it not?"
        show cherie normal
        $ cherie.flags.birthdayknown = True
    return

label cherie_gift_swimsuit_male:
    "I feel the nerves almost getting the better of me as I hand over the gift."
    show cherie stuned
    "Cherie's eyes are wide open and full of surprise as she realises that it's for her."
    "She takes it from me, but the whole time she's looking me in the eyes."
    show cherie surprised
    cherie.say "What is this, {i}mon ami{/i}?"
    cherie.say "A gift, when it is not my birthday?"
    show cherie happy
    cherie.say "And so thoughtfully wrapped too!"
    show cherie talkative
    cherie.say "Whatever can it be?"
    show cherie smile
    mike.say "Well there's one way to find out, Cherie..."
    mike.say "And that would be to open it up, yeah?"
    show cherie normal
    "Part of me can't believe that Cherie's taking so long about this."
    "Another girl would have torn the thing open and been looking it over by now."
    "But I do the best I can to keep myself from blurting out what's inside."
    "Even as Cherie carefully opens the package."
    show cherie surprised
    cherie.say "My goodness..."
    cherie.say "This is a swimsuit."
    show cherie happy
    cherie.say "And a very daring one at that!"
    show cherie amused
    mike.say "Well, Cherie - what do you think?"
    mike.say "I saw it and could just picture you in it."
    if cherie.sub >= 70:
        show cherie smile
        "Cherie greets my question with a knowing smile."
        "And at the same time I notice that there's a certain twinkle in her eye too."
        show cherie happy
        cherie.say "You know, {i}mon ami{/i}..."
        cherie.say "Some would say that this is intended for a far younger woman than I."
        cherie.say "But something tells me that you are far more wise and discerning than that."
        cherie.say "That you are the kind of man who appreciates a woman with experience, no?"
        show cherie flirt
        "I can't keep from nodding my head as Cherie says all of this."
        "Wobbling it back and forth, while grinning like a demented fool."
        mike.say "So...you'll wear it, yeah?"
        show cherie smile
        "Cherie's own nod is far slower and more considered than mine."
        show cherie happy
        cherie.say "Oh yes, {i}mon ami{/i} - when the time is right, you will see me in it."
        show cherie normal
        $ cherie.flags.sexyswimsuit = True
    else:
        show cherie smile
        "Cherie greets my question with a pleasant smile."
        "But I note that at the same time she's folding the swimsuit up in her hands."
        show cherie happy
        cherie.say "You have very good taste, {i}mon ami{/i}."
        show cherie whining
        cherie.say "But sadly you are aware of how an older woman must dress."
        cherie.say "This is intended for a far younger, less refined person than me."
        show cherie sadsmile
        "Cherie hands the swimsuit back to me as she says all of this."
        "And the only thing I can do is reach out and take it."
        "That and nod in agreement."
        "Because what else am I going to do right now?"
        "Get down on my knees and beg her to wear it for me?"
        "Even I'm not that desperate."
        $ hero.cancel_activity()
    return

label cherie_gift_collar_male:
    "My hand is almost shaking as I pull out the carefully wrapped gift."
    "And I can feel myself getting anxious as I hold it out towards Cherie."
    "So much so that I feel like I must have a rictus of a grin on my face right now."
    "But if that's the case, Cherie doesn't let it show on her own face."
    show cherie stuned
    "Instead she takes the gift with a polite nod and look of surprise."
    show cherie surprised
    cherie.say "A gift, {i}mon ami{/i}?"
    show cherie happy
    cherie.say "How thoughtful and unexpected, but very welcome!"
    cherie.say "I must open it up and see what is inside."
    show cherie smile
    "I'm nodding now, starting to lose that grip on myself again."
    "And that's because I know that the stakes are perilously high on this one."
    "I'm pinning all of my hopes on it being a success."
    "As well as facing a complete and utter disaster if it isn't."
    show cherie talkative
    cherie.say "But what is this?"
    cherie.say "Is it a choker of some kind?"
    show cherie normal
    "Cherie turns the leather collar over in her hands."
    show cherie stuned
    "But when she finds the medallion with her name on it, she stops and stares at me."
    show cherie talkative
    cherie.say "But this..."
    cherie.say "This is a collar for..."
    show cherie surprised
    cherie.say "For a dog!"
    if cherie.sub >= 90:
        show cherie normal
        "Before I can say a word to explain myself, Cherie closes her eyes and takes a deep breath."
        "And then she holds the collar up to her face, almost like she's savouring the aroma of it."
        show cherie talkative
        cherie.say "Oh, {i}mon ami{/i}..."
        cherie.say "If only you could know..."
        show cherie happy blush
        $ cherie.love += 2
        $ cherie.sub += 5
        cherie.say "If only you could know how long I have wanted something like this!"
        cherie.say "But I have been too afraid to ask for it myself."
        show cherie talkative
        cherie.say "Would you..."
        show cherie normal
        "Cherie holds out the collar for me, waiting for me to take it."
        "And then she turns her back to me, holding up her hair."
        "My hands feel clumsy as I loop it around her neck and struggle to buckle it in place."
        show cherie smile
        "But once the job is done, Cherie turns around again, a delighted look on her face."
        show cherie happy
        $ cherie.set_sex_slave()
        cherie.say "There, it is done, {i}mon ami{/i}..."
        cherie.say "Or should I say, my master?"
        show cherie normal
    else:
        $ cherie.love -= 20
        $ cherie.sub -= 20
        show cherie annoyed
        "Before I can say a word to explain myself, Cherie shoves the collar back into my hands."
        "In fact she shoves it so hard that it slams into my chest and I'm forced back a step."
        show cherie talkative
        cherie.say "Is this what you think of me?"
        show cherie angry
        cherie.say "That I am some kind of..."
        cherie.say "Some kind of animal?!?"
        show cherie upset
        mike.say "No..."
        mike.say "I..."
        mike.say "It's not like that, Cherie!"
        show cherie annoyed
        "Cherie's about as impressed with my attempt to explain myself as she was with the collar itself."
        "And she cuts me off with a wave of her hand and a stamp of her foot."
        hide cherie with easeoutright
        "Then she turns her back on me and storms off."
        "Which leaves me alone and holding onto the damn collar."
        "As well as realising what it feels like to bet everything and then lose."
        $ hero.cancel_activity()
    return

label cherie_gift_slutty_dress_male:
    "I've been waiting for the right moment to do this, almost fretting for it to arrive."
    "And the very second that I think it's upon me, I pull out the gift from behind my back."
    "Then I unceremoniously thrust it towards Cherie, leaving no room for doubt that it's for her."
    show cherie stuned
    "Cherie looks about as surprised as you'd imagine, even taking a step backwards."
    "She puts one hand to her chest and holds out the other to take the package from me."
    show cherie surprised
    cherie.say "A gift?"
    cherie.say "For me?"
    show cherie happy
    cherie.say "My goodness, how kind and thoughtful you are, {i}mon ami{/i}!"
    show cherie smile
    mike.say "Yeah, Cherie..."
    mike.say "That's right - it's a present for you...from me!"
    show cherie happy
    cherie.say "But of course it is."
    cherie.say "What else could it be when it comes to me, delivered by your own hand."
    show cherie normal
    "Cherie's unwrapping the package all the time that she's saying this."
    "But when she feels the sensation of what's inside against her hands, she stops and looks down."
    "And then she holds up the dress that was wrapped up in there so that it unfolds."
    "I should probably add that it's a very daring dress too."
    "One that I feel all funny from imagining Cherie wearing!"
    show cherie surprised
    cherie.say "Oh my, it is a dress..."
    show cherie surprised blush
    cherie.say "But where is the rest of it?"
    show cherie stuned
    if cherie.sub >= 70:
        mike.say "Erm..."
        mike.say "No, Cherie - that's all of it, I promise you!"
        show cherie amused
        "Cherie raises an eyebrow at this, and I can feel her sizing me up at the same time."
        show cherie talkative
        cherie.say "But you must know that I am joking with you, {i}mon ami{/i}?"
        show cherie happy
        cherie.say "And that I am delighted that you would give me such a dress."
        show cherie normal
        "Cherie folds out the dress, holding up against herself."
        show cherie happy
        cherie.say "Many men would want a woman of my age to cover herself up, no?"
        cherie.say "But not you, as you appreciate what you see before you."
        show cherie wink
        "Cherie gives me a little wink to underline her point."
        "And I can't help nodding like crazy."
        mike.say "And I can't wait to see you in it either!"
        show cherie talkative
        cherie.say "Patience, patience..."
        show cherie happy
        cherie.say "This you will see soon enough, I promise you."
        show cherie normal
        $ cherie.flags.sluttydate = True
        $ cherie.flags.sexydate = False
    else:
        mike.say "Erm..."
        mike.say "No, Cherie - that's all of it, I promise you!"
        show cherie annoyed
        "Cherie raises an eyebrow at this, and I can feel her sizing me up at the same time."
        "Then she deftly folds the dress up again, wrapping it in the paper once more."
        show cherie talkative
        cherie.say "No, no, no..."
        cherie.say "I think that I know a little more about women's fashion than you."
        show cherie angry
        cherie.say "And I would advise you to take this dress back to the place you bought it."
        cherie.say "Take it back and tell them that you want all of the missing pieces."
        show cherie annoyed
        "By now I'm staring to have trouble telling whether Cherie's serious or not."
        "But whatever the case, it's obvious she's not going to accept the dress."
        "So I make no protest as she hands it back to me."
        "And instead I just nod, feeling relived that at least this whole thing is now over."
        $ hero.cancel_activity()
    return


label cherie_gift_sexy_dress_male:
    "Ever since I picked up the gift that I have for Cherie, I've been waiting for this moment."
    "The chance to hand it over to her and see the look on her face when she opens it."
    "So the first chance that presents itself, I pull it out and thrust it towards her."
    show cherie stuned
    "The look of surprise on her face as she takes it setting my heart racing."
    show cherie surprised
    cherie.say "A gift?"
    cherie.say "For me?"
    show cherie happy
    cherie.say "Oh, {i}mon ami{/i}, but you shouldn't have!"
    show cherie normal
    "I not that for all of Cherie's protests, she doesn't stop unwrapping the package."
    "Nor does she show any sign of handing it back to me either."
    mike.say "I..."
    mike.say "I really hope that you like it, Cherie..."
    mike.say "I spent a long time picking it out and..."
    mike.say "And I think it'll really suit you."
    show cherie surprised
    "Cherie lets out a gasp as she sees what's inside."
    "And then she pulls it out, letting it fall to its full length."
    show cherie talkative
    cherie.say "It is a dress..."
    show cherie happy
    cherie.say "A most elegant and flattering dress too!"
    show cherie normal
    mike.say "You see what I mean, Cherie?"
    mike.say "I saw it, and it instantly made me think of you."
    if cherie.sub >= 50:
        show cherie normal
        "Cherie nods as she carefully holds the dress up to herself."
        "And I can already see that she's pretty pleased with the way it looks."
        show cherie smile
        cherie.say "Hmm..."
        show cherie happy
        cherie.say "And it would seem that you have a very good eye for this type of thing too!"
        cherie.say "I believe this will fit me like a glove - but a very sexy glove, no?"
        show cherie normal
        "I'm nodding like crazy now, as if I can't make myself stop."
        mike.say "You know it, Cherie!"
        mike.say "Oh man, I can't wait to see you try it on!"
        show cherie smile
        "Cherie greets this with a smile and a coy nod of the head."
        show cherie talkative
        cherie.say "But of course, {i}mon ami{/i}."
        show cherie happy
        cherie.say "And you will - when the time is right."
        show cherie normal
        $ cherie.flags.sluttydate = False
        $ cherie.flags.sexydate = True
    else:
        show cherie normal
        "Cherie nods as she carefully folds the dress up in front of me."
        "But then to my great surprise, she hands it back to me again."
        mike.say "What's the matter, Cherie?"
        mike.say "Did I get the wrong size?"
        show cherie sadsmile
        "Cherie shakes her head at this and lets out a sigh."
        show cherie whining
        cherie.say "Ah..."
        cherie.say "No, {i}mon ami{/i}, you got the wrong dress."
        cherie.say "And for the wrong woman too."
        show cherie sad
        mike.say "But...but...but..."
        mike.say "What do you mean?"
        show cherie talkative
        cherie.say "Me in such a dress?"
        cherie.say "That is not for you, {i}mon ami{/i}."
        show cherie wink
        cherie.say "At least not yet."
        show cherie happy
        cherie.say "But who knows - maybe someday soon."
        show cherie normal
        $ hero.cancel_activity()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
