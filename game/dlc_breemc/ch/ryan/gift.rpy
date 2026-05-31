init python:
    Event(**{
    "name": "ryan_give_a_gift",
    "label": "npc_give_a_gift",
    "conditions": [
        Or(
            HeroTarget(IsBirthday()),
            IsSpecialDate("christmas"),
            IsSpecialDate("valentine"),
            ),
        PersonTarget(ryan,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "girl": "ryan",
    "once_day": True,
    "do_once": False,
    "quit": False,
    }
    )

label ryan_give_female:
    if "skill_book_cooking" not in hero.inventory and not hero.has_skill("cooking") and ryan.love >= 60:
        $ gift = "skill_book_cooking"
        "He hands me a pretty large book."
        bree.say "No way!\nIs it for real?!"
        ryan.say "Sure it is!"
        bree.say "Thank you! Thank you sooo much!"
    else:
        $ gift = "flowers"
        "He hands me some flowers."
        bree.say "Thanks."
    $ hero.gain_item(gift)
    return

label ryan_give_birthday_female:
    ryan.say "A little bird told me that it's somebody's birthday, right?"
    "I look up to see Ryan standing there, a knowing smile on his face."
    bree.say "Erm..."
    bree.say "I think I told you the date of my birthday, Ryan..."
    bree.say "So well done you for remembering it - or writing it down, I guess."
    "Ryan's enthusiasm doesn't seem to be dimmed by my reaction."
    "In fact his smile gets wider still as he whips out a gift-wrapped package."
    ryan.say "So there you go - happy birthday, [hero.name]!"
    bree.say "Thank you, Ryan..."
    bree.say "That's so thoughtful of you."
    call ryan_give_female from _call_ryan_give_female
    return

label ryan_give_christmas_female:
    ryan.say "Merry Christmas, [hero.name]..."
    ryan.say "I think I have something in my sack for you!"
    "I can't help raising an eyebrow at this."
    bree.say "Something in your sack?"
    bree.say "That's a bit rude, isn't it?"
    "Ryan looks nonplussed as he pulls out a gift-wrapped package."
    ryan.say "What are you talking about, [hero.name]?"
    ryan.say "I just got you a Christmas present!"
    bree.say "Oh..."
    bree.say "Okay..."
    bree.say "Thank you, Ryan..."
    bree.say "That's so thoughtful of you."
    call ryan_give_female from _call_ryan_give_female_1
    return

label ryan_give_valentine_female:
    ryan.say "I bet there's someone that wants to be my Valentine!"
    "I turn around to see Ryan standing there, holding a package in his hand."
    "It's wrapped in the gaudiest Valentines-themed paper imaginable."
    "And so there's no hiding who he's talking about."
    bree.say "Oh..."
    bree.say "Is that for me?"
    ryan.say "Who else would it be for, [hero.name]?"
    ryan.say "You know that you want to be my Valentine."
    bree.say "Thank you, Ryan..."
    bree.say "That's so thoughtful of you."
    $ hero.gain_item("valentine_chocolates")
    return

label ryan_gift_collar_female:
    "I feel like the smile on my face is going to make my jaw seize up."
    "Because I'm super tense and waiting to see what Ryan's reaction is going to be."
    "Though when he finally gets the box open and looks inside, he seems confused."
    "I watch as he reaches inside and pulls out a leather collar with a metal medallion."
    "One that looks like the kind of thing you'd put around the neck of a dog or cat."
    "But this one is definitely more sized for a human being."
    "I'm still smiling as Ryan holds it up and takes a closer look."
    if hero.morality <= -25:
        bree.say "Nice, huh?"
        bree.say "And just the right size for your neck!"
    elif hero.morality >= 25:
        bree.say "So..."
        bree.say "What do you think?"
    else:
        bree.say "Pretty special, huh?"
        bree.say "A unique gift for a special guy!"
    if ryan.sub >= 90:
        "Ryan looks totally amazed at the sight of the collar."
        "And he turns it over in his hands, shaking his head as he does so."
        "For a moment I'm worried that he's going to hand it straight back to me."
        "But then he looks up, a huge smile spreading over his face."
        $ result = randint(1, 3)
        if result == 1:
            ryan.say "[hero.name], this is amazing!"
            ryan.say "How did you know?"
        elif result == 2:
            ryan.say "Man...I always wanted one of these!"
            ryan.say "It's like you read my mind."
        else:
            ryan.say "[hero.name], I always secretly wanted one of these!"
            ryan.say "How did you guess?"
        "All I can do is shrug and shake my head, tyring to look nonchalant."
        if hero.morality >= 25:
            bree.say "I don't know, Ryan...maybe it was luck?"
            bree.say "I saw the collar and thought of you."
        elif hero.morality <= -25:
            bree.say "Oh, I picked up on the signs, Ryan..."
            bree.say "I'm tuned into that kind of stuff!"
        else:
            bree.say "Ah, well...I'd kind of been getting hints."
            bree.say "A girl can pick up on that kind of thing, you know?"
        "Ryan nods as he makes to put the collar on."
        "And I hurry to help him fasten it around his neck."
        $ ryan.love += 5
        $ ryan.set_sex_slave()
    else:
        "Ryan looks up from the collar, his gaze meeting my eye."
        "And I can already see that he's far from impressed."
        "Even before he hands the collar and box back to me."
        if ryan.sub >= 50:
            ryan.say "What's this supposed to mean, [hero.name]?"
            ryan.say "You think I'm some kind of degenerate?!?"
        elif ryan.sub <= -50:
            ryan.say "Okay, [hero.name], I'm really not into this kind of thing."
            ryan.say "I'm the kind of guy that takes charge - not one that you put on a leash!"
        else:
            ryan.say "What were you thinking, [hero.name]?"
            ryan.say "Unless you hadn't noticed - I'm not a dog!"
        "I don't have any choice but to take hold of the collar and box."
        "Because it's that or letting them fall to the ground."
        if hero.morality >= 25:
            bree.say "Erm...okay, Ryan..."
            bree.say "I'm sorry that I screwed-up so badly."
        elif hero.morality <= -25:
            bree.say "Geez, Ryan, I get it, okay?"
            bree.say "I just wanted to add some spice to our relationship!"
        else:
            bree.say "Okay, okay...I get the message."
            bree.say "You don't like the damn collar!"
        "I make a point of hiding the collar behind my back."
        "And I even consider shoving it into the next trash-can I see."
        $ ryan.love -= 20
        $ ryan.sub -= 10
        $ hero.cancel_activity()
    return

label ryan_gift_slutty_dress_female:
    show ryan smile
    ryan.say "Oh, [hero.name], is it for me?"
    show ryan normal
    "He unwraps the slutty outfit."
    show ryan whining
    jack.say "Thanks but no thanks [hero.name], I'm not ready to wear this..."
    show ryan normal
    $ hero.cancel_activity()
    return




























































label ryan_gift_sexy_dress_female:
    show ryan smile
    ryan.say "Oh, [hero.name], is it for me?"
    show ryan normal
    "He unwraps the slutty outfit."
    show ryan whining
    jack.say "Thanks but no thanks [hero.name], I'm not ready to wear this..."
    show ryan normal
    $ hero.cancel_activity()
    return


























































    return

label ryan_birthday_gift_female:
    "I make a point of smiling broadly as I hand the package over to Ryan."
    bree.say "There you go..."
    bree.say "I hope you like it!"
    "Ryan returns the smile as he accepts the gift and begins to open it."
    ryan.say "Wow, [hero.name] - you remembered my birthday?"
    if ryan.flags.birthdayknown:
        "I nod as I watch Ryan tearing at the wrapping paper."
        if hero.morality >= 25:
            bree.say "Of course I did!"
        elif hero.morality <= -25:
            bree.say "Sure I did - because I want something in return!"
        else:
            bree.say "I made sure to keep it in my head."
    else:
        "I shake my head as I watch Ryan tearing at the wrapping paper."
        if hero.morality >= 25:
            bree.say "Erm, no...lucky guess!"
        elif hero.morality <= -25:
            bree.say "Nah, I just wanted to see the look on your face!"
        else:
            bree.say "Nope, I just got lucky!"
        $ ryan.flags.birthdayknown = True
    return

label ryan_gift_swimsuit_female:
    "Ryan seems really eager to find out what's inside the box."
    "Because he pretty much tears off the paper and tosses it aside."
    "And I can feel my own excitement building as he does so too."
    "Obviously as I know what's in there and I picked it out for him."
    "So when he holds up the smallest pair of swimming trunks known to man, I almost hold my breath."
    "But it seems to take Ryan another couple of moments to figure out what they actually are."
    "And I watch him turning it over in his hands, stretching the fabric as he does so."
    bree.say "Erm..."
    bree.say "So..."
    bree.say "What do you think?"
    bree.say "They're pretty great, huh?"
    if ryan.sub >= 60:
        "Ryan finally seems to get just what they are as he holds them against his waist."
        "And I feel relieved as a smile spreads across his face too."
        if ryan.sub >= 80:
            ryan.say "These are so great, [hero.name]!"
            ryan.say "And daring too..."
            ryan.say "I'd never have had the courage to buy then for myself!"
        elif ryan.sub >= 70:
            ryan.say "These are pretty wild, [hero.name]!"
            ryan.say "But I've been working out more recently."
            ryan.say "So I think I can pull them off."
        else:
            ryan.say "Normally I don't let other people pick out my clothes, [hero.name]."
            ryan.say "But with these, it kind of feels like a challenge."
            ryan.say "Which is all the more reason to wear them!"
        "I can't help clapping my hands together in glee at that Ryan's saying."
        "Already imagining the sight of him in the skimpy trunks."
        $ ryan.flags.sexyswimsuit = True
    else:
        "Ryan hooks his thumb into the elastic of the waistband."
        "And then he uses it to fire the trunks back at me like a slingshot."
        "Instinctively I dive to catch them, already worrying about returns and exchange."
        if ryan.sub >= 50:
            ryan.say "Oh no, [hero.name], I couldn't wear those!"
            ryan.say "I've never seen anything so tight in my entire life."
            ryan.say "They're so tight people would be able guess my religion!"
        elif ryan.sub <= -50:
            ryan.say "I appreciate the thought, [hero.name]..."
            ryan.say "But these are way too tight for me."
            ryan.say "And I like to pick out my own clothes too."
        else:
            ryan.say "I prefer baggier trunks, [hero.name]."
            ryan.say "Something with more room to breathe."
            ryan.say "So I could never wear those."
        "I open my mouth to argue, but then think better of it."
        "Because it was a total gamble to begin with."
        "So I just have to accept that and move on."
        $ hero.cancel_activity()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
