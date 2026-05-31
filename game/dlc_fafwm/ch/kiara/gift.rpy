label kiara_birthday_gift_male:
    show kiara
    "I hold out the carefully wrapped gift with a huge smile on my face."
    mike.say "Happy birthday, Kiara!"
    mike.say "I hope you like what I got you."
    if kiara.flags.birthdayknown:
        show kiara surprised
        "Kiara looks surprised as she takes the gift from me."
        kiara.say "Oh, [hero.name], how thoughtful of you!"
        show kiara smile
        kiara.say "So few people seem to remember my birthday."
    else:
        show kiara smile
        "Kiara looks totally amazed as she accepts the gift."
        kiara.say "But how did you know that it was my birthday?"
        mike.say "I can't explain it, Kiara - maybe it was a lucky guess?"
        $ kiara.flags.birthdayknown = True
    return

label kiara_gift_swimsuit_male:
    show kiara
    "I can't help getting nervous as I pull out the box and hand it over to Kiara."
    mike.say "Surprise, Kiara..."
    mike.say "I got you a little something."
    show kiara smile
    "Kiara looks totally amazed as she accepts the gift."
    kiara.say "For me?"
    kiara.say "That is so kind of you!"
    "I watch with baited breath as she unwraps the gift and opens the box."
    "And my nerves only get worse as she pulls out what's inside and holds it up."
    show kiara surprised
    kiara.say "What is this?"
    kiara.say "A swimming costume?"
    "To be more precise, it's a very sexy swimming costume."
    "One that I'd pay a great deal to see Kiara wearing."
    mike.say "That's right, Kiara..."
    mike.say "I saw it and thought of you!"
    if kiara.sub >= 70:
        show kiara smile
        "I watch as a smile spreads slowly across Kiara's face."
        "And I can't help smiling myself as she holds it up to herself."
        "Because it looks to me as though she really likes what she's seeing right now."
        "Which has to be a good thing, right?"
        mike.say "So...you like it?"
        kiara.say "I have to admit that you have good taste, [hero.name]."
        kiara.say "This is exactly what I would have chosen for myself."
        "I can hardly believe my luck as Kiara begins to compliment me."
        mike.say "Does that mean you're going to wear it?!?"
        kiara.say "Patience, [hero.name] - you will get to see me in it soon enough!"
        $ kiara.flags.sexyswimsuit = True
    else:
        show kiara mischievous
        "I watch as a smile spreads slowly across Kiara's face."
        "But then my spirits fall as I realise that it's an ironic one."
        kiara.say "Ah, but you will have to keep doing just that, [hero.name]..."
        kiara.say "You will have to keep thinking of me in it."
        kiara.say "Because I am not going to be wearing this."
        "Kiara thrusts out her hand, pushing the swimsuit back towards me."
        with hpunch
        "And I have no choice but to open my own hands and take it."
        $ hero.cancel_activity()
    return

label kiara_gift_collar_male:
    show kiara
    "I can't seem to keep my hand from shaking as I pull out the gift I have for Kiara."
    "And the fact that her face lights up as soon as she sees it only adds to my excitement."
    show kiara surprised
    kiara.say "Oh my goodness - what is this?"
    kiara.say "A gift for me?"
    mike.say "Yeah, Kiara, that's exactly what it is."
    mike.say "And I think it's something you're really going to love."
    "Kiara nods as she begins to tear open the wrapping paper."
    "Part of me wants to urge her to go faster."
    "But I manage to keep a hold on myself and wait."
    "So when she finally opens the package and pulls it out, I'm almost beside myself."
    kiara.say "But this..."
    kiara.say "This is a collar..."
    kiara.say "The kind that a dog would wear!"
    mike.say "Exactly, Kiara, just the kind that I know you want to wear."
    mike.say "But that you'd be too afraid to admit to yourself that you wanted it!"
    if kiara.sub >= 90:
        show kiara mischievous
        "It takes less than a second for the expression on Kiara's face to change."
        "I see it go from surprise to something much more intriguing."
        "And when she opens her mouth to speak, I realise that it's sheer delight."
        show kiara smile
        kiara.say "But how could you even guess such a thing?"
        $ kiara.love += 2
        $ kiara.sub += 5
        kiara.say "This is a thing that I have always desired..."
        kiara.say "Yet never had the courage to speak of out loud."
        mike.say "Ah, but all the signs were there, Kiara."
        mike.say "And I think you were giving them out, whether you knew it or not."
        "Kiara nods as she undoes the collar and hands it to me."
        "And I don't need to be told that she wants me to fasted it in place."
        "As soon as it's around her neck, she looks down at, eyes wide with wonder."
        kiara.say "Now I will never have to hide my desires again."
        $ kiara.set_sex_slave()
        kiara.say "I can belong to my master, and make a show of it too!"
    else:
        $ kiara.love -= 20
        $ kiara.sub -= 20
        show kiara upset
        "It takes less than a second for the expression on Kiara's face to change."
        "I see it go from surprise to something much darker in that short space of time."
        "And when she opens her mouth to speak, I realise the new emotion is pure, unadulterated rage!"
        show kiara angry
        kiara.say "What on earth are you talking about, you fool?"
        kiara.say "You think that I want to be collared like a dog?!?"
        "Kiara shoves the collar back at me without warning."
        with hpunch
        "In fact she does it with such strength that she hits me in the gut, almost winding me."
        mike.say "Oof..."
        mike.say "But Kiara..."
        mike.say "I read all the signs, I was so sure!"
        kiara.say "Well you obviously read them wrong, didn't you."
        kiara.say "And maybe I read you wrong too."
        $ hero.cancel_activity()
    return

label kiara_gift_slutty_dress_male:
    show kiara
    "I've been waiting for what feels like the perfect moment to surprise Kiara with my gift."
    "And when it comes I leap on the chance, whipping it out and virtually waving it under her nose."
    mike.say "Surprise, Kiara..."
    mike.say "I got you something."
    "Kiara looks totally taken by surprise as she takes the gift from me."
    "Shaking her head as if she can't believe that it's really for her."
    show kiara surprised
    kiara.say "A gift?"
    kiara.say "For me?"
    kiara.say "You shouldn't have..."
    show kiara smile
    kiara.say "But I am glad that you did!"
    "I nod my head eagerly as Kiara tears open the wrapping paper."
    "Watching the look on her face as she unfolds what's inside."
    "And only getting more excited as she realises what it actually is."
    kiara.say "It is..."
    mike.say "A dress!"
    kiara.say "A very daring one too!"
    mike.say "Well, you could call it that, I guess..."
    mike.say "But I really think it'll suit you."
    if kiara.sub >= 80:
        "Kiara begins to nod her head almost as soon as I'm done explaining myself."
        "Holding the dress up against herself as she does so."
        "And making sure that I see how well it follows the curves of her body."
        show kiara smile
        kiara.say "You will not have to imagine how it will look for too much longer."
        kiara.say "Because I intend to wear this dress the first chance that I get."
        "I can hardly believe my luck."
        "Not only does Kiara seem to love the dress, she can't wait to wear it!"
        mike.say "Erm...that's great, Kiara."
        mike.say "Do you have a particular time and place in mind?"
        "Kiara gives me an indulgent smile and a shake of the head."
        "As though she finds my eagerness endearing."
        show kiara smile
        kiara.say "Patience, [hero.name], patience."
        kiara.say "You have waited this long to see me in the dress."
        kiara.say "Surely you can wait just a little longer yet?"
        kiara.say "Though I promise you, it will not be a long wait!"
        $ kiara.flags.sexydate = False
        $ kiara.flags.sluttydate = True
    else:
        "Kiara begins shaking her head almost as soon as I'm done explaining myself."
        "And she hands me the dress back as she does so."
        "Making sure that I get the message there's no choice for me but to take it from her."
        show kiara upset
        kiara.say "That is the way things are going to stay with this dress, [hero.name]."
        kiara.say "You will have to keep on only thinking of what I would look like in it."
        kiara.say "Because it is not something that you will see in the flesh."
        mike.say "But...but why not, Kiara?"
        mike.say "Don't you like the dress?"
        "Kiara gives me an indulgent smile and a shake of the head."
        "As though I just don't get it, but she finds that cute."
        show kiara angry
        kiara.say "I love the dress, [hero.name]."
        kiara.say "But I cannot accept it from you."
        kiara.say "As this is not the place we have reached in our relationship."
        kiara.say "Maybe some day that is where we will be, you and I."
        kiara.say "But that day is not today."
        $ hero.cancel_activity()
    return


label kiara_gift_sexy_dress_male:
    show kiara
    "I've been hiding a surprise gift for Kiara behind my back in an awkward fashion ever since we met up."
    "And now feels like the perfect time for me to pull the trigger and show her that I've got her something special."
    "So I whip it out and pretty much shove the package under her nose."
    show kiara surprised
    kiara.say "Oh my goodness..."
    kiara.say "What is this?"
    kiara.say "A gift for me?"
    mike.say "It's just a little something I picked up the other day, Kiara."
    mike.say "I saw it and instantly thought that you should have it."
    "The look of intrigue on Kiara's face becomes more pronounced the more that I have to say."
    "And at the same time she hurries to tear open the wrapping paper so as to see what's inside."
    show kiara smile
    kiara.say "Well, not I really must see what you have bought for me."
    kiara.say "I cannot wait to see what could have caught your attention."
    kiara.say "Especially if it made you think of me."
    "A moment later, Kiara pulls the thing out of it's wrapping."
    "Then she gasps as it unfolds in her hands."
    show kiara talkative
    kiara.say "It is a dress..."
    kiara.say "And a very sexy dress it is too!"
    show kiara normal
    if kiara.sub >= 50:
        "I'm nodding as Kiara says all of this."
        "And as she holds the dress up against herself, I can't help smiling too."
        "Because I'm feeling ever more sure that she's going to accept my gift."
        show kiara smile
        kiara.say "Ah, [hero.name]..."
        kiara.say "I so love dresses like this one."
        kiara.say "But there was a time when I would have handed it straight back to you."
        kiara.say "I would have told you that we were not at a place where you could buy something like this for me."
        "Kiara takes a deep breath and then lets it out as a sigh."
        kiara.say "Ah...but luckily for me, we are past that point now."
        kiara.say "So I may enjoy this kind gift."
        mike.say "And what about me, Kiara?"
        mike.say "I get to enjoy seeing you in it, right?"
        show kiara flirt
        kiara.say "But of course you do!"
        kiara.say "For you, I am planning a private exhibition..."
        $ kiara.flags.sluttydate = False
        $ kiara.flags.sexydate = True
    else:
        "I'm nodding eagerly as Kiara says all of this."
        "But I begin to shake my head a moment later."
        "As I see her fold the dress up and hand it back to me."
        show kiara upset
        mike.say "What's wrong, Kiara?"
        mike.say "Don't you like sexy dresses?"
        show kiara angry
        kiara.say "What a silly thing to say!"
        kiara.say "Of course I like them - I own many of them."
        kiara.say "But we are not at a place where I can accept one from you, [hero.name]."
        kiara.say "Maybe some time soon we will be, and you can buy me the next sexy dress you see."
        kiara.say "But for now, as nice as this gift may be, I must decline it."
        show kiara upset
        "I can tell from the tone of Kiara's voice and the firmness of her stance that she's serious."
        "And there doesn't seem to be any point in arguing, as it'd only make things awkward."
        "So I nod and take the dress back, feeling more than a little humiliated as I do so."
        $ hero.cancel_activity()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
