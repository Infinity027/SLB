label claire_birthday_gift_male:
    show claire stuned
    "I hand the gift to Claire, seeing a smile spread across her face as I do so."
    show claire surprised
    claire.say "What's this, [hero.name]?"
    claire.say "You remembered my birthday - how thoughtful of you!"
    show claire happy
    if claire.flags.birthdayknown:
        "I shrug and give Claire a smile of my own in return."
        mike.say "Of course I remembered, Claire..."
        mike.say "I wanted to help celebrate your special day."
    else:
        "I feel a wave of relief sweep over me, as I'd forgotten it was Claire's birthday!"
        mike.say "Oh, sure thing, Claire..."
        mike.say "How could I forget something that important?"
        $ claire.flags.birthdayknown = True
    return

label claire_gift_swimsuit_male:
    show claire normal
    "Once Claire has the box containing my gift in her hands, I watch with interest."
    "In fact it's all that I can do to keep from holding my breath in anticipation."
    "Because I put a lot of thought and effort into this present, and I want to see it pay off."
    "So when she pulls it out of the box and holds it up to the light, my heart begins to beat faster than ever."
    show claire surprised
    claire.say "Oh my goodness!"
    show claire stuned
    "Claire's eyes go wide as she holds up the skimpy swimsuit that was inside the box."
    "The one that I bought with great haste as soon as I pictured her wearing it."
    mike.say "So, Claire..."
    mike.say "What do you think?"
    mike.say "Pretty nice, huh?"
    "At the sound of my voice, Claire looks up from studying my gift."
    "And I brace myself to hear what she has to say about it."
    if claire.sub >= 70:
        show claire happy
        "Claire smiles as she holds the swimsuit up to herself."
        "And I feel a surge of relief as she seems to be accepting the gift."
        "Plus she'd nodding the whole time too, which has to be a good sign."
        show claire talkative
        claire.say "This is so nice, [hero.name]..."
        claire.say "I never bought myself a swimsuit like this."
        claire.say "I don't think I'd ever have the courage to."
        claire.say "But if you think I can pull it off, then I'll happily wear it!"
        show claire normal
        mike.say "That's great, Claire - you're going to look stunning in it."
        show claire wink
        "Claire gives me a cheeky little wink."
        show claire talkative
        claire.say "Don't worry, you'll be the first person to see me in it!"
        show claire normal
        $ claire.flags.sexyswimsuit = True
    else:
        "Claire shakes her head as she folds the swimsuit back up."
        show claire sad
        "Then she slips it into the box it came out of."
        "And finally she hands the whole lot back to me."
        show claire whining
        claire.say "I'm sorry, [hero.name]..."
        claire.say "But I just can't accept this."
        claire.say "It's way too revealing for a woman of my age."
        show claire sad
        "I nod as Claire hands the swimsuit back to me, trying to hide my disappointment."
        mike.say "Sorry, Claire - I'll try harder to pick the right gift next time."
        show claire talkative
        claire.say "It was a nice gesture."
        claire.say "But I'm just not that kind of a girl!"
        show claire sadsmile
        $ hero.cancel_activity()
    return

label claire_gift_collar_male:
    show claire normal
    "Once Claire has the box containing my gift in her hands, I watch with interest."
    "In fact it's all that I can do to keep from holding my breath in anticipation."
    "Because I put a lot of thought and effort into this present, and I want to see it pay off."
    "So when she pulls it out of the box and holds it up to the light, my heart begins to beat faster than ever."
    show claire surprised
    claire.say "Oh my goodness!"
    show claire stuned
    "Claire's eyes go wide as she holds up the leather collar that was inside the box."
    "The one that I bought with great haste as soon as I pictured her wearing it."
    mike.say "So, Claire..."
    mike.say "What do you think?"
    mike.say "Pretty nice, huh?"
    "At the sound of my voice, Claire looks up from studying my gift."
    "And I brace myself to hear what she has to say about it."
    if claire.sub >= 90:
        show claire happy
        "Claire looks up at me, amazement written all over her face."
        "She blinks and shakes her head, as if she can't believe what she's seeing."
        show claire talkative
        claire.say "But how..."
        claire.say "How did you know?"
        show claire happy
        $ claire.love += 2
        $ claire.sub += 5
        mike.say "Let's just say that I picked up on the clues, Claire."
        mike.say "They were pretty subtle, but they were definitely there."
        "Claire's still shaking her head as she raises the collar to her neck."
        "And I hurry to help, stepping behind her to fasten it in place."
        show claire happy
        claire.say "I always felt like I wanted to try being a sub."
        claire.say "That I was into that kind of thing."
        claire.say "But I knew that Hector wouldn't get it, you know?"
        claire.say "That he'd not know the difference between that and me just being under his thumb?"
        show claire happy
        mike.say "I hear you, Claire."
        mike.say "And I'm one hundred percent behind you too."
        mike.say "This is going to be one hell of an adventure!"
        $ claire.set_sex_slave()
    else:
        $ claire.love -= 20
        $ claire.sub -= 20
        show claire upset
        "Claire's face suddenly changes from a look of amazement to one of annoyance."
        "And the change is so quick and unexpected that I almost flinch at the sight."
        show claire annoyed
        claire.say "What in the hell is this supposed to be?!?"
        claire.say "Last time I checked, I wasn't a damn dog!"
        show claire pout
        "I'm already holding up my hands to ward off Claire's anger."
        "Shaking my head as I struggle to find the words to explain myself."
        mike.say "No, no, no...you don't understand, Claire..."
        mike.say "It's like...like a bondage thing, yeah?"
        mike.say "I thought you were into being a sub!"
        show claire annoyed
        claire.say "Well you thought wrong, didn't you!"
        show claire pout
        "Claire makes a point of throwing the collar at my feet."
        hide claire with easeoutright
        "Then she turns her back on me and walks away."
        "Leaving me with the distinct impression following her would be a very bad idea."
        $ hero.cancel_activity()
    return

label claire_gift_slutty_dress_male:
    show claire normal
    "Once Claire has the box containing my gift in her hands, I watch with interest."
    "In fact it's all that I can do to keep from holding my breath in anticipation."
    "Because I put a lot of thought and effort into this present, and I want to see it pay off."
    "So when she pulls it out of the box and holds it up to the light, my heart begins to beat faster than ever."
    show claire surprised
    claire.say "Oh my goodness!"
    show claire stuned
    "Claire's eyes go wide as she holds up the revealing dress that was inside the box."
    "The one that I bought with great haste as soon as I pictured her wearing it."
    mike.say "So, Claire..."
    mike.say "What do you think?"
    mike.say "Pretty nice, huh?"
    "At the sound of my voice, Claire looks up from studying my gift."
    "And I brace myself to hear what she has to say about it."
    if claire.sub >= 70:
        show claire happy
        "Claire smiles as she holds the dress up to herself."
        "And I feel a surge of relief as she seems to be accepting the gift."
        "Plus she'd nodding the whole time too, which has to be a good sign."
        show claire talkative
        claire.say "This is so nice, [hero.name]..."
        claire.say "I never bought myself a dress like this."
        claire.say "I don't think I'd ever have the courage to."
        claire.say "But if you think I can pull it off, then I'll happily wear it!"
        show claire normal
        mike.say "That's great, Claire - you're going to look stunning in it."
        show claire wink
        "Claire gives me a cheeky little wink."
        show claire talkative
        claire.say "Don't worry, you'll be the first person to see me in it!"
        show claire normal
        $ claire.flags.sluttydate = True
        $ claire.flags.sexydate = False
    else:
        show claire sad
        "Claire shakes her head as she folds the dress back up."
        "Then she slips it into the box it came out of."
        "And finally she hands the whole lot back to me."
        show claire whining
        claire.say "I'm sorry, [hero.name]..."
        claire.say "But I just can't accept this."
        claire.say "It's way too revealing for a woman of my age."
        show claire sad
        "I nod as Claire hands the dress back to me, trying to hide my disappointment."
        mike.say "Sorry, Claire - I'll try harder to pick the right gift next time."
        show claire talkative
        claire.say "It was a nice gesture."
        claire.say "But I'm just not that kind of a girl!"
        show claire sadsmile
        $ hero.cancel_activity()
    return

label claire_gift_sexy_dress_male:
    show claire normal
    "Once Claire has the box containing my gift in her hands, I watch with interest."
    "In fact it's all that I can do to keep from holding my breath in anticipation."
    "Because I put a lot of thought and effort into this present, and I want to see it pay off."
    "So when she pulls it out of the box and holds it up to the light, my heart begins to beat faster than ever."
    show claire surprised
    claire.say "Oh my goodness!"
    show claire stuned
    "Claire's eyes go wide as she holds up the stylish, yet daring that was inside the box."
    "The one that I bought with great haste as soon as I pictured her wearing it."
    mike.say "So, Claire..."
    mike.say "What do you think?"
    mike.say "Pretty nice, huh?"
    "At the sound of my voice, Claire looks up from studying my gift."
    "And I brace myself to hear what she has to say about it."
    if claire.sub >= 50:
        show claire happy
        "Claire smiles as she holds the dress up to herself."
        "And I feel a surge of relief as she seems to be accepting the gift."
        "Plus she'd nodding the whole time too, which has to be a good sign."
        show claire talkative
        claire.say "This is so nice, [hero.name]..."
        claire.say "I never bought myself a swimsuit like this."
        claire.say "I don't think I'd ever have the courage to."
        claire.say "But if you think I can pull it off, then I'll happily wear it!"
        show claire normal
        mike.say "That's great, Claire - you're going to look stunning in it."
        show claire wink
        "Claire gives me a cheeky little wink."
        show claire talkative
        claire.say "Don't worry, you'll be the first person to see me in it!"
        $ claire.flags.sluttydate = False
        $ claire.flags.sexydate = True
    else:
        show claire sad
        "Claire shakes her head as she folds the dress back up."
        "Then she slips it into the box it came out of."
        "And finally she hands the whole lot back to me."
        show claire whining
        claire.say "I'm sorry, [hero.name]..."
        claire.say "But I just can't accept this."
        claire.say "It's way too revealing for a woman of my age."
        show claire sad
        "I nod as Claire hands the dress back to me, trying to hide my disappointment."
        mike.say "Sorry, Claire - I'll try harder to pick the right gift next time."
        show claire talkative
        claire.say "It was a nice gesture."
        claire.say "But I'm just not that kind of a girl!"
        show claire sadsmile
        $ hero.cancel_activity()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
