init python:
    Event(**{
    "name": "alexis_give_a_gift",
    "label": "npc_give_a_gift",
    "conditions": [
        Or(
            HeroTarget(IsBirthday()),
            IsSpecialDate("christmas"),
            IsSpecialDate("valentine"),
            ),
        PersonTarget(alexis,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "girl": "alexis",
    "once_day": True,
    "do_once": False,
    "quit": False,
    }
    )

label alexis_give_male:
    alexis.say "What do you think about your present?"
    mike.say "What present?"
    alexis.say "The necklace I am wearing, silly."
    mike.say "!?"
    alexis.say "I bought it just so that you could see me wearing it..."
    return

label alexis_give_valentine_male:
    "Alexis walks hesitantly towards me."
    call alexis_greet from _call_alexis_greet_7
    show alexis blush
    alexis.say "Happy valentine's day [hero.name]..."
    "Alexis hands me a box of chocolates."
    mike.say "Thank you, Alexis."
    $ hero.gain_item("valentine_chocolates")
    return

label alexis_give_birthday_male:
    "Alexis walks towards me."
    call alexis_greet from _call_alexis_greet_8
    show alexis happy
    alexis.say "Happy birthday [hero.name]!"
    call alexis_give_male from _call_alexis_give_male
    return

label alexis_give_christmas_male:
    "Alexis walks towards me."
    call alexis_greet from _call_alexis_greet_9
    show alexis happy
    alexis.say "Merry Christmas [hero.name]."
    call alexis_give_male from _call_alexis_give_male_1
    return

label alexis_birthday_gift_male:
    show alexis
    if alexis.flags.birthdayknown:
        mike.say "Happy birthday Alexis."
        alexis.say "How sweet, you remembered my birthday!"
    else:
        alexis.say "How do you know my birthday?"
        mike.say "I didn't, it's just pure luck."
        $ alexis.flags.birthdayknown = True
    return

label alexis_gift_swimsuit_male:
    show alexis happy
    alexis.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy swimsuit."
    if alexis.sub >= 60:
        show alexis blush
        alexis.say "It's so pretty, thank you [hero.name]."
        $ alexis.flags.sexyswimsuit = True
    else:
        show alexis angry
        alexis.say "Thanks but no thanks [hero.name]."
        alexis.say "You think I would wear that?"
        $ alexis.love -= 4
        $ hero.cancel_activity()
    return

label alexis_gift_sexy_dress_male:
    show alexis happy
    alexis.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy dress."
    if alexis.sub >= 30:
        show alexis blush
        alexis.say "Thank you [hero.name]."
        $ alexis.flags.sexydate = True
        $ alexis.flags.sluttydate = False
    else:
        show alexis confused
        $ alexis.love -= 4
        alexis.say "Thanks but no thanks [hero.name], I would feel very awkward with that..."
        $ hero.cancel_activity()
    return

label alexis_gift_slutty_dress_male:
    "I do the best I can to wait for the moment to be just right."
    "Keeping a close eye on Alexis's mood the whole time."
    "And only when I'm sure that everything's perfect, that's when I make my move."
    "Which basically involves pulling the box out from behind my back."
    "Then waving it around in front of Alexis to get her attention."
    mike.say "SURPRISE!"
    mike.say "Look, Alexis..."
    mike.say "I got you a surprise!"
    "Alexis blinks as she stares at me capering in front of her."
    show alexis talkative
    alexis.say "Yeah, [hero.name], I can see that."
    alexis.say "I thought I was supposed to be one getting excited right now."
    alexis.say "But it looks like you're about to burst a blood-vessel!"
    show alexis annoyed
    "I'm nodding and shaking my head almost at the same time right now."
    "The nerves and anxious energy of handing over the gift really getting to me."
    mike.say "Yeah, yeah, yeah..."
    mike.say "I get all of that, Alexis..."
    mike.say "Just open the box, okay?"
    "Alexis seems to realise that she won't get any peace until she does as I ask."
    show alexis happy
    "So she puts a pleasant smile on her face and plucks the box out of my hands."
    play sound [paper_ripping_1, paper_ripping_2]
    "Then I'm forced to watch with baited breath as she takes her time unwrapping it."
    "And by the time she pulls out the dress inside, I feel like I'm going to explode."
    mike.say "So?"
    mike.say "Why aren't you saying anything?"
    mike.say "You like it, right?"
    "Alexis doesn't answer me straight away."
    "Instead she keeps me waiting as she examines the dress."
    show alexis normal
    "Reminding me as she does so of just how dramatic and daring it is."
    if alexis.sub >= 30:
        show alexis happy
        "And when I see Alexis holding it up against herself, I feel a surge of relief."
        "Not to mention some serious excitement as she smooths it over her thighs too!"
        show alexis talkative
        alexis.say "Wow..."
        alexis.say "This is pretty daring, [hero.name]."
        alexis.say "I don't know if I'd have had the guts to buy it myself."
        show alexis flirt
        alexis.say "But now that you got it for me, I can't wait to try it on!"
        "I can feel a wave of emotions washing over me right now."
        "Relief is definitely one of the most prominent ones."
        "But I can also detect desire, and not a small amount of bravado too."
        "And after all, I pulled it off - so why the hell not?"
        mike.say "Oh, I think you always knew it was your kind of thing, Alexis."
        mike.say "Sometimes you just need someone to give you permission, you know?"
        mike.say "To help you pull the trigger."
        show alexis normal
        "Alexis is nodding as I'm saying all of this."
        "Still holding the dress up against herself and gazing at it intently."
        show alexis flirt
        alexis.say "Now what I need is an excuse to wear it."
        alexis.say "So that you can see just how good it looks on me."
        mike.say "Just name the date, Alexis - I'll be right there!"
        $ alexis.flags.sexydate = False
        $ alexis.flags.sluttydate = True
    else:
        "But when she begins folding it up again, I feel my guts begin to churn."
        mike.say "What's the matter, Alexis?"
        mike.say "Is there something wrong with it?"
        "Alexis shakes her head as she continues to fold the dress up again."
        "And then places it neatly back in the box, offering it to me."
        alexis.say "It was very thoughtful of you to get me a gift, [hero.name]."
        alexis.say "But I think you should have taken a little more time over it."
        alexis.say "Because it seems like you don't really know what I like."
        alexis.say "Even after we've known each other for so long."
        "I can detect a hint of frustration in what Alexis is saying."
        "Maybe even some disappointment too."
        "Just having her turn down the dress would have been bad enough."
        "But now I feel like I've totally let her down on a personal level too."
        mike.say "I'm sorry, Alexis - I'll try harder next time, I promise!"
        alexis.say "That's sweet of you to say, [hero.name]."
        alexis.say "But I'll believe it when I see it."
        $ alexis.love -= 10
        $ hero.cancel_activity()
    return

label alexis_gift_collar_male:
    show alexis
    if game.room == "date_restaurant":
        mike.say "I've really had a great time tonight, Alexis."
        mike.say "And I feel that we've really come a long way since we were reunited - don't you?"
    else:
        mike.say "I feel that we've really come a long way since we were reunited - don't you?"
    "Again she nods in agreement."
    mike.say "That's why I slipped out of the office this lunchtime and bought this for you."
    "At the mere mention of something being purchased for her, I see a glimmer of the old fire spark into life in Alexis's eyes."
    "She looks up, the confident smile creeping back onto her face as the gold-digger in her is suddenly given an unexpected jolt of life."
    "Her gaze fixes upon the jewellery box that I've pulled out of my jacket pocket and now hold in the palm of my hand."
    "I can almost read the calculations that must be flashing through her cynical little mind right now."
    "The box is perhaps a little too large to contain a ring, which would have been her prime goal in these stakes."
    "But these are modern times, and you can't bank on a proposal any longer."
    "So maybe it's actually a necklace that's worth almost as much instead?"
    alexis.say "Oh, [hero.name]...this is all so sudden!"
    alexis.say "I really don't know what to say!"
    if game.room == "date_restaurant":
        "By this time the sight of the jewellery box and the undoubtedly beautiful girl filling up with emotion has been noticed by the other diners and staff alike."
        "I can already hear oohs and ahhs, as well as gushing comments about how romantic it all is."
        "Which is exactly what I wanted to have happen at this stage."
        "I stand up to add to the drama of the moment and let more people see what I'm doing."
        "No one seems to find it odd that I'm getting to my feet, rather than going down on one knee."
        "But they're all too swept up in the moment to even notice."
    "I pop open the box and give Alexis a wide and genuine smile."
    mike.say "Alexis...will you do me the inestimable honour of being my bitch?"
    if game.room == "date_restaurant":
        "For a moment, the imagined magic seems to linger in the air, as no one but Alexis notices what I actually just said."
        "But then, as she looks down at what's sitting in the box, I can hear people beginning to snap out of it and make scandalised comments in hushed whispers."
    "Curled up tightly in the box is a shiny, red collar of leather with a diamond-shaped pendant hanging from it."
    "It's the kind of thing that a person might put around the neck of their dog."
    "Only this one, I know quite well, is a perfect fit for Alexis."
    "And printed on the front is the word 'TAINTED'."
    "Alexis says nothing, but looks up at me, her eyes wide and her lip quivering as if she might begin to cry at any moment."
    mike.say "I'll take your silence as a positive, shall I?"
    if alexis.sub < 90:
        alexis.say "I won't wear that damn thing, and there's nothing that you can do to make me!"
        "She still sounds as though she's on the brink of tears, but now there's a definite shade of anger to her wavering voice."
        alexis.say "I really thought you were different, [hero.name]."
        alexis.say "But I guess I was wrong - you're just a disgusting creep, like all the others!"
        "I don't see the slap coming, and it's a good one too."
        "I see stars as my head snaps to one side, my cheek burning from the blow."
        "By the time I manage to shake myself back into awareness, Alexis is still in the act of storming out of the door."
        "She leaves me alone, with the collar still in my hand, my cheek stinging from her slap and the disapproving sound of the other diner's voices in my ears."
        $ alexis.love -= 20
        $ alexis.sub -= 20
        $ hero.cancel_activity()
    else:
        "When she makes no effort to reach for the collar, I pull it from the box myself and proceed to place it around her neck."
        "Alexis doesn't even try to stop me, the former glimmer of her more confident self collapsing into a sense of defeat and acceptance."
        $ alexis.set_sex_slave()
        hide alexis
        show alexis
        mike.say "There, isn't that better, Alexis?"
        if game.room == "date_restaurant":
            "I sit back down across the table from her and offer a reassuring smile."
        mike.say "You see, I think what sank our relationship back when we were kids was the fact that I didn't really know who you were."
        mike.say "Sure, I thought you were a cheating bitch at the time."
        mike.say "But since we got back together, I realised that a bitch like that is really just crying out for someone to keep her in line."
        mike.say "So that's what I'm going to do for you, Alexis."
        mike.say "From now on, I'll keep you on a short leash, and teach you how to be good and obedient."
        "Alexis is silent for a while, but then she speaks meekly for the first time."
        alexis.say "Okay, [hero.name]...if that's what you think is best..."
        "I shake my head and wave an admonishing finger in her face at this."
        mike.say "No, no...let's get some ground-rules straight from the start."
        mike.say "It's more appropriate that you call me 'Master' from now on, okay?"
        "Alexis looks up at me and I can see in her eyes that a part of her is still hoping this will all prove to be a joke of some sick and cruel variety."
        "I narrow my own eyes in response, silently urging an answer from her."
        alexis.say "Y...yes...Master..."
        "I smile at her indulgently, as if all is forgiven instantly."
    return

label alexis_gift_butt_plug_male:
    show alexis happy
    alexis.say "Oh, [hero.name], is it for me?"
    "She unwraps the butt plug."
    if alexis.sub <= 50 or not alexis.sexperience:
        show alexis annoyed
        alexis.say "..."
        alexis.say "Keep it... I don't want it so keep it."
        alexis.say "I'm sure you'll have a better use of it than me."
        $ hero.cancel_activity()
    else:
        show alexis normal blush
        alexis.say "It's perfect!"
        show alexis flirt
        alexis.say "Thanks [hero.name], I'll make a good use of it."
        $ alexis.flags.buttplug = True
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
