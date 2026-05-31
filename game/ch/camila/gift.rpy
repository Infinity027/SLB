init python:
    Item("taser")
    Item("gun")

    Event(**{
    "name": "camila_give_a_gift",
    "label": "npc_give_a_gift",
    "conditions": [
        Or(
            HeroTarget(IsBirthday()),
            IsSpecialDate("christmas"),
            IsSpecialDate("valentine"),
            ),
        PersonTarget(camila,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "girl": "camila",
    "once_day": True,
    "do_once": False,
    "quit": False,
    }
    )

label camila_give_valentine_male:
    "Camila walks confidently towards me."
    call camila_greet from _call_camila_greet
    show camila blush
    camila.say "Happy valentine's day [hero.name]..."
    call camila_give_male from _call_camila_give_male
    return

label camila_give_birthday_male:
    "Camila walks towards me."
    call camila_greet from _call_camila_greet_1
    show camila happy
    camila.say "Happy birthday [hero.name]!"
    call camila_give_male from _call_camila_give_male_1
    return

label camila_give_christmas_male:
    "Camila walks towards me."
    call camila_greet from _call_camila_greet_2
    show camila happy
    camila.say "Merry Christmas [hero.name]."
    call camila_give_male from _call_camila_give_male_2
    return

label camila_give_male:
    if "handcuffs" not in hero.inventory:
        $ gift = "handcuffs"
        "Camila gives me a pair of handcuffs."
    elif "taser" not in hero.inventory:
        $ gift = "taser"
        "Camila gives me a taser."
    elif "gun" not in hero.inventory:
        $ gift = "gun"
        "Camila gives me a gun."
    else:
        $ gift = "condom"
        "Camila gives me a condom."
    mike.say "Thank you, Camila."
    $ hero.gain_item(gift)
    return

label camila_birthday_gift_male:
    show camila
    if camila.flags.birthdayknown:
        mike.say "Happy birthday Camila."
        camila.say "How sweet, you remembered my birthday!"
    else:
        camila.say "How do you know my birthday?"
        mike.say "I didn't, it's just pure luck."
        $ camila.flags.birthdayknown = True
    return

label camila_christmas_gift_male:
    show camila
    mike.say "Merry Christmas Camila."
    camila.say "Thanks!"
    $ camila.love += 2
    return

label camila_valentine_gift_male:
    show camila
    mike.say "Happy valentine's day Camila."
    camila.say "Thank you."
    $ camila.love += 2
    return

label camila_gift_sexy_dress_male:
    "I can hardly wait to give Camila the gift that I have for her, and so I waste no time."
    "The very first chance that I get, I don't hesitate to thrust it into her hands."
    "She looks like she was just about to say something and so I take her by surprise."
    "Camila takes the gift without question, looking a little suspicious as she does so."
    "But I know that she's a cop and doesn't like people to get the drop on her."
    "So that kind of reaction doesn't really bother me."
    show camila happy
    camila.say "Oh, [hero.name], what the hell!"
    "Almost as soon as the words are out of her mouth, I see Camila check herself."
    "She visibly shakes her head, trying her best to remember that she's not on duty right now."
    camila.say "I mean...you shouldn't have, [hero.name]."
    camila.say "But what a nice surprise!"
    play sound [paper_ripping_2, paper_ripping_1]
    "I watch with baited breath as Camila tears at the wrapping paper and opens the package."
    "It takes her a couple of seconds to realise what it is that she's holding."
    "But then I see recognition spread across Camila's face all of a sudden."
    "She looks up at me, the surprise in her eyes clear to be seen."
    camila.say "It's..."
    camila.say "It's a dress!"
    "She's right, of course - it is a dress."
    "But she's also wrong, because it's not just any old dress."
    "What Camila's holding in her hands is a pretty dramatic piece of clothing."
    "One that since I laid eyes on it, I can't stop picturing her in too!"
    mike.say "Yeah, Camila - it's a dress."
    mike.say "You know, one of those things that girls sometimes wear?"
    mike.say "Instead of pants?"
    show camila normal
    "Camila doesn't say anything in response, just blinks at me."
    "And her silence makes me instantly worried that I've insulted her."
    mike.say "I...I just saw it and thought of you, Camila."
    mike.say "I know you have to dress practically in your line of work."
    mike.say "But I can't help wondering what you'd look like in a dress."
    mike.say "And I think you'd look kind of great..."
    "Camila bites her lip as she looks down at the dress and then back up at me."
    "And I try not to hold my breath as I wait for her answer..."
    "She unwraps the sexy dress."
    if camila.sub >= 30:
        "Camila looks to her left and then her right, quick as a flash."
        "She seems to be checking that there's nobody around to see what she does next."
        "Which is to throw her arms around my neck and kiss me with a passion!"
        "The kiss doesn't last too long, but it's intense and unexpected enough to leave me stunned."
        show camila blush
        camila.say "Oh, [hero.name] - thank you SO much!"
        camila.say "How in the hell did you know?!?"
        mike.say "Ah...know what, Camila?"
        "Camila leans in close, whispering in a conspiratorial manner."
        camila.say "That I always wanted a dress like this - that's what!"
        mike.say "Really?!?"
        camila.say "Sure, [hero.name]."
        camila.say "Whenever I'm busting hookers, I'm always jealous."
        mike.say "Y...you are?!?"
        camila.say "Sure I am!"
        camila.say "The stuff they get to wear!"
        camila.say "The way they get to show off what they got!"
        camila.say "And don't get me started on the way people look at them!"
        camila.say "I'm always the good cop at work."
        show camila flirt
        camila.say "Sometimes I want to be the bad girl on my own time..."
        "As if she needs to emphasize the point, Camila leans against me."
        "I try to say something coherent, but all I can do is grin like a fool."
        "And that's because my mind is already full of the possibilities her confession just made possible..."
        $ camila.flags.sexydate = True
        $ camila.flags.sluttydate = False
    else:
        show camila annoyed
        "Without warning, Camila shoves the dress and the box it came in back at me."
        "In fact, she shoves it so hard that I feel like I've been punched in the gut!"
        "I wheeze and double over, dropping the spurned gift on the floor as I do so."
        camila.say "Geez, [hero.name], way to be a slimeball!"
        camila.say "I bust hookers wearing more than this!"
        mike.say "I...I'm sorry, Camila..."
        mike.say "I didn't think..."
        show fx exclamation
        camila.say "Well, maybe you should have!"
        "I nod through the pain I'm feeling."
        "And I try to gather up the dress as I do so."
        "Maybe I can take it back to the store."
        "You know, exchange it for something more appropriate?"
        "Like a pair of boxing gloves?"
        $ hero.cancel_activity()
    return

label camila_gift_slutty_dress_male:
    "I'm always wary of springing surprises on Camila."
    "You know, what with her being a cop and stuff?"
    "I'm pretty sure she'd never actually pull out a gun and fill me full of lead."
    "But that's one of those things in life it's never really worth taking a chance with."
    "And anyway, she always seems to sniff it out anyway, no matter how hard I try to hide it."
    show camila talkative
    camila.say "Okay, [hero.name], the game's up..."
    camila.say "Hand it over nice and quietly."
    camila.say "That way nobody gets hurt."
    show camila normal
    "Like I already said, I know that it's pointless to resist."
    "But my subconscious mind still seems to want to put up a fight."
    mike.say "Huh?"
    mike.say "What are you talking about, Camila?"
    "Camila gives me a crooked smile and raises an eyebrow."
    show camila weird
    camila.say "Are we really going to do this?"
    camila.say "With me tackling you to the ground and putting you in cuffs?"
    camila.say "No...wait a minute - you might actually enjoy that!"
    show camila flirt
    mike.say "Alright, alright..."
    mike.say "You win - take it!"
    mike.say "Before you start using pepper-spray on me or something..."
    "I produce the gift-wrapped box from behind my back."
    "And then I hold it out in front of me, urging Camila to take it."
    "Which she does, but not without narrowing her eyes at me."
    show camila talkative
    camila.say "Hey..."
    camila.say "You'd better not be accusing me of police brutality!"
    show camila normal
    mike.say "Oh no - no way!"
    "This seems to be enough to mollify Camila, who turns her attention to the package instead."
    play sound [paper_ripping_2, paper_ripping_1]
    "Allowing me to watch eagerly as she tears off the wrapping-paper."
    "And as soon as she pulls the dress out of the box, I feel the urge to hold my breath."
    if camila.sub >= 70:
        "Camila makes a point of holding the dress up to herself."
        "At the same time she kind of wiggles her hips and moves her thighs."
        "It should really be nothing more than a few simple motions of her body."
        "But somehow the sight of it is enough to make me start sweating."
        show camila talkative
        camila.say "You know what, [hero.name]..."
        camila.say "I must have busted a hundred hookers in my time on the force."
        camila.say "And every last one of them was wearing something like this."
        show camila upset
        mike.say "Oh..."
        mike.say "Oh, I'm sorry, Camila..."
        mike.say "I had no idea!"
        "Camila shakes her head, dismissing my apology as hastily as it was made."
        show camila talkative
        camila.say "Nah, it's okay."
        camila.say "That's not what I was getting at anyway."
        camila.say "What I really meant to say was that I always..."
        show camila flirt
        camila.say "Well, I always kind of envied them, you know?"
        camila.say "Like, I wanted to dress up like that myself!"
        "Camila looks up from the dress, catching my eye as she does so."
        "And I can see the intensity of the emotion in her gaze."
        show camila happy
        camila.say "And now you've given the excuse I needed."
        "I feel like my mouth's suddenly gone dry, and my heart is pounding in my chest."
        "Because, unless I'm very much mistaken, all of that means Camila likes the dress."
        "And if so, then I'm that much closer to actually seeing her in it!"
        $ camila.flags.sexydate = False
        $ camila.flags.sluttydate = True
    else:
        "Camila holds it up, examining the garment from every possible angle."
        "And it looks to me almost like she's searching in vain for something."
        mike.say "What's wrong, Camila?"
        mike.say "What are you looking for?"
        show camila talkative
        camila.say "The rest of the damn dress, [hero.name]..."
        camila.say "That's what I'm looking for!"
        show camila normal
        "I don't need to see the expression on Camila's face to know how badly this is going."
        "But I still feel the need to do all I can in the hope of salvaging it."
        mike.say "I...I suppose it is a little skimpy."
        "Camila shakes her head has she tosses the dress back to me."
        "And I rush to catch it before the thing lands on the ground."
        "Because I remember just how much it cost!"
        show camila angry
        camila.say "Come on, [hero.name]..."
        camila.say "I've busted hookers that'd blush at that thing!"
        camila.say "So if you think I'm gonna wear it..."
        camila.say "Well, you must be out of your mind!"
        show camila upset
        "That seems to be the last Camila's prepared to say on the matter."
        "So I find myself nodding in agreement and keeping my mouth shut."
        "At the same time feeling relieved that I remembered to keep the receipt."
        $ camila.love -= 10
        $ hero.cancel_activity()
    return

label camila_gift_swimsuit_male:
    "I'm so eager to give Camila the gift I have for her that I don't waste as much as a second."
    "The very moment I have the chance, I whip it out and thrust it under her nose."
    show camila happy
    mike.say "Surprise, Camila!"
    mike.say "I got you something as a surprise!"
    "Camila jumps in surprise, clearly not prepared for my springing the gift on her."
    "The thought that it might have been dumb to shock a tough cop like that passes through my mind."
    "But I'm way too excited to actually consider the thought, eager to have Camila open the gift."
    camila.say "Whoa..."
    camila.say "Okay, [hero.name], okay!"
    camila.say "Way to surprise me, by the way!"
    "Camila takes the gift from me and starts to tear at the wrapping paper."
    "And it's all I can do to keep quiet and wait while she does so."
    "But when she pulls the gift out of the paper, I almost hold my breath."
    camila.say "Wow, [hero.name]..."
    show fx exclamation
    camila.say "That's some gift right there!"
    "Camila holds the hanger from which the garment dangles out at arm's length."
    "But I can't tell if this is because she's alarmed by it or else wants a better look."
    "Either way, I know exactly what the gift is and what it looks like."
    "It's a swimsuit, and I've already pictured Camila in it countless times since I bought it!"
    mike.say "Well, what do you think?"
    mike.say "When I saw it, I instantly thought of you!"
    show camila normal
    "Camila nods at this, slowly and with more control than I could hope to manage."
    "Clearly she wasn't expecting my level of enthusiasm either."
    "I wait as patiently as I can for her answer."
    "And I can feel my sense of anticipation growing as she opens her mouth..."
    if camila.sub >= 60:
        show camila happy
        "Camila looks almost disappointed for a moment."
        "And I'm sure that she's going to reject the gift."
        "But then she looks up and me, as if she's reading my face."
        camila.say "You...thought of me?"
        camila.say "This made you think of me?"
        "I look around, feeling like I'm suddenly being cross-examined."
        "But there's no way to escape Camila when she's like this."
        "She's as determined as a bloodhound on a scent!"
        mike.say "Well...yeah, Camila."
        mike.say "I...I think it'd look amazing on you!"
        camila.say "But you've..."
        camila.say "You've seen some of my scars, haven't you?"
        "All I can do is blink at Camila's question."
        "It just doesn't seem to make any sense to me."
        mike.say "Well, yeah, Camila."
        mike.say "But why would that be an issue?"
        mike.say "You got those in the line of duty, didn't you?"
        mike.say "And I...I kinda think they're a turn-on too!"
        "Camila's cheeks turn red at what I just said."
        "And it takes me a moment to realise she's actually blushing."
        "I actually made this tough, no-nonsense cop blush!"
        camila.say "Y...you do?!?"
        camila.say "Well, I guess I could try it on."
        camila.say "Since you went to all that trouble picking it out..."
        "I think Camila says something else after that."
        "But if I'm honest, it passes me by completely."
        "And that's because my head's already filling with images of her."
        "Images of her in that very same swimsuit..."
        $ camila.flags.sexyswimsuit = True
    else:
        show camila angry
        $ camila.love -= 4
        "Camila screws her face up into a helpless look of disappointment."
        "And when she shakes her head too, I know this isn't going to go my way."
        camila.say "Erm...it's...nice, [hero.name]."
        camila.say "But the problem's that it's not me!"
        camila.say "Don't get me wrong - it's sweet that you got me a gift though!"
        "I nod my head as she hands the swimsuit back to me."
        "And all the time I'm trying to look like I'm not crushed."
        mike.say "I...I'm sorry, Camila."
        mike.say "I guess I should have asked first..."
        "At this, Camila begins to shake her head."
        "And it doesn't need a genius to see that I've made her feel guilty."
        camila.say "No, [hero.name], it's not your fault - it's mine."
        camila.say "I...I have some issues with showing off my body, that's all."
        camila.say "It's stupid, but I can't help it!"
        "I know that she's trying to make me feel better."
        "But all that really does is make me feel even more clueless."
        "Camila clearly has a problem and I trampled over it like a moron!"
        mike.say "Let's just forget about it, okay?"
        camila.say "Sure thing, [hero.name]."
        camila.say "As far as I'm concerned, it never happened!"
        "I nod and smile, but it really doesn't help me to feel any better."
        $ hero.cancel_activity()
    return

label camila_gift_collar_male:
    "I make sure to keep the gift that I have for Camila hidden from sight until the time feels just right."
    "This is one of those things that could go south very quickly if I choose the wrong moment."
    "And believe me when I say that's the last thing that I want to happen!"
    "So I wait for Camila to be in the best mood possible."
    "When she's laughing and joking like she hasn't got a care in the world."
    "That's the moment I choose to reach into my pocket and pull out what I have for her..."
    show camila normal
    mike.say "Ah, Camila..."
    mike.say "I know it's not a special occasion or anything like that."
    mike.say "But I bought you something that I think you'll get a kick out of..."
    "I see Camila raise her eyebrows at this, clearly intrigued by my admission."
    "She tries as best she can to keep up her image as a tough, hard-bitten cop."
    "But all the same I can see that she's as interested in a gift as any other girl."
    show camila happy
    camila.say "Ah, [hero.name]!"
    camila.say "You didn't have to do that."
    camila.say "It's sweet that you did though!"
    mike.say "Like I already said, Camila - I'm sure you'll like it."
    mike.say "I mean, you never came out and said this was your kind of thing."
    mike.say "But I think I've been reading the signals you send out."
    mike.say "Am I right?"
    "Right there and then is the moment that I let Camila see what I have for her."
    "She looks down just as I reveal that what I have in my hands is a leather choker."
    "It looks for all the world like the kind of collar that you might find on a dog."
    "Save for the fact that the pendant hanging from it is a golden star, echoing a cop's badge."
    mike.say "It's a collar, Camila."
    mike.say "You can wear it to let everyone know you're mine!"
    show camila annoyed
    "I watch as Camila's eyes go wider than I can ever remember seeing them before."
    "She doesn't say anything at first, just shakes her head at the sight of it."
    mike.say "Camila?"
    mike.say "You do like it?"
    mike.say "Don't you?"
    if camila.sub < 90 or not "camila_collar_request" in DONE:
        "Suddenly, Camila begins to shake her head faster than ever."
        "And at the same time, I can see a frown spreading across her face."
        "When she looks up at me she's scowling and narrowing her eyes."
        show camila angry
        camila.say "No, of course I don't fucking like it!"
        camila.say "What kind of a moron are you?!?"
        "Before I can think of an answer, Camila slaps the collar out of my hand."
        mike.say "Ow!"
        mike.say "Hey, that hurt!"
        camila.say "Yeah, well it was supposed to, you jerk!"
        camila.say "You're just lucky I don't choke you out with that thing, buddy!"
        "I can't help backing off a little and raising my hands in a defensive gesture."
        "There are actually veins standing out on Camila's neck right now!"
        camila.say "What did you think?"
        camila.say "That I work my ass off all day to let some asshole treat me like a damn dog?!?"
        camila.say "You don't own me, [hero.name] - nobody does!"
        "And with that, Camila turns on her heel and storms off."
        "Which leaves me alone to sheepishly pick up the collar and watch her leave."
        $ camila.love -= 20
        $ camila.sub -= 20
        $ hero.cancel_activity()
    else:
        "Camila's cheeks turn a deep shade of red as she stares at the collar."
        "I see her swallow and look around, as if she's afraid of someone seeing."
        "And then she comes as close as she can, almost pressing herself against me."
        show camila happy
        camila.say "B...but that's like a dog collar, [hero.name]!"
        camila.say "I'd be like your..."
        mike.say "My pet, Camila?"
        mike.say "Would you like that?"
        camila.say "Would you treat me like a dog?"
        camila.say "W...would you tell me I'm a good girl?"
        camila.say "Maybe...punish me when I'm a bad girl?"
        "Camila's leaning in so close to me by now."
        "And the look in her eyes is so pleading too."
        "I don't think I could say no."
        "Even if this wasn't something I wanted!"
        mike.say "Of course, Camila."
        mike.say "Whatever you want!"
        $ camila.set_sex_slave()
        show camila close happy
        "Camila smiles as she lets me fasten the collar around her neck."
        "And once it's in place, she looks at me in an almost bashful manner."
        "A look that puts me in mind of a dog that was all bark beforehand."
        "But one that turns into an obedient lapdog the moment it's belly is rubbed!"
        $ camila.love += 2
        $ camila.sub += 5
    return

label camila_gift_butt_plug_male:
    show camila happy
    camila.say "Oh, [hero.name], is it for me?"
    "She unwraps the butt plug."
    if camila.sub <= 50 or not camila.sexperience:
        show camila annoyed
        camila.say "..."
        camila.say "Keep it... I don't want it so keep it."
        camila.say "I'm sure you'll have a better use of it than me."
        $ hero.cancel_activity()
    else:
        show camila blush
        camila.say "It's perfect!"
        show camila flirt
        camila.say "Thanks [hero.name], I'll make a good use of it."
        $ camila.flags.buttplug = True
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
