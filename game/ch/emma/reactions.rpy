label emma_ice_cream_reaction_male:
    mike.say "Phew, it's just too hot today, Emma - I need an ice cream!"
    emma.say "Yeah, I could go for one too!"
    "At the ice cream stall, I buy myself a cone with a couple of different scoops."
    "Emma chooses one too, but smaller and neater - oddly it reminds me of her!"
    emma.say "Oh...oh dear!"
    mike.say "What's the matter, Emma?"
    "I look around to see Emma staring a the end of her own nose."
    "Or more specifically, the blob of ice cream sitting on it."
    emma.say "Urgh...how did I manage to do that?!?"
    "I do my best to keep from laughing out loud."
    "But she just looks so comical that I can't help myself."
    return

label emma_study_with_intro_male:
    "Emma seems to be pretty serious about her studies, devoting a lot of her free time to it."
    "I could easily get jealous of coming second in her list of priorities."
    "But instead I decided to try to be helpful instead, by studying with her."
    "That way we can still spend time together, and I get to help her out too."
    emma.say "Are you sure that you want to do this, [hero.name]?"
    emma.say "I mean, I'm really grateful for the your help."
    emma.say "But some of this stuff is pretty heavy-going!"
    "I shake my head, dismissing Emma's concerns."
    mike.say "Ah, don't worry about me, Emma."
    mike.say "I'm no stranger to hitting the books!"
    mike.say "We can handle it between the two of us."
    "Emma nods and wastes no time diving into the first of her books."
    "But soon enough I begin to see what she meant by that comment."
    "And my respect for how smart she is goes up by quite a way!"
    emma.say "Urgh..."
    emma.say "This kind of thing always trips me up, [hero.name]."
    emma.say "Would you take a look at it?"
    emma.say "A fresh pair of eyes might be what it needs."
    "I give Emma what I hope is a reassuring smile."
    "And then I lean over the page to see what's got her stumped."
    return

label emma_study_with_success_male:
    "I scan the whole thing from top to bottom."
    "And then I let out a sigh of amazement."
    mike.say "Wow..."
    mike.say "You weren't kidding, Emma."
    mike.say "This is some seriously hard stuff!"
    emma.say "If it's too complex, [hero.name]..."
    mike.say "Just a second - let me have a think."
    "At first I think this one has me well and truly stumped."
    "But then something seems to click inside of my head."
    mike.say "What about this, Emma?"
    "I point to a certain line on the page."
    "Emma leans in closer to see for herself."
    "And I can feel the softness of her chest against my arm."
    "It's so distracting that I have to fight to stay focused."
    mike.say "Have you looked at it from this angle?"
    emma.say "Oh no, that's not..."
    emma.say "No...wait a minute..."
    emma.say "Yes...that's it!"
    emma.say "Thank you, [hero.name]."
    emma.say "That makes so much more sense!"
    "I don't know what makes me feel better in that moment."
    "The feel of Emma's body pressed against mine."
    "Or the sound of delight in her voice."
    return

label emma_study_with_failure_male:
    "I hope that Emma doesn't see what happens to that smile a moment later."
    "Because it doesn't take long for it to drop right off of my face."
    "And in it's place I'm soon wearing a look of blank confusion."
    mike.say "I..."
    mike.say "Well..."
    mike.say "Erm..."
    "Emma listens to me muttering and mumbling for a while."
    "But soon enough I can feel her patience beginning to wear thin."
    emma.say "[hero.name]..."
    emma.say "Do you actually know what you're looking at?"
    emma.say "Because it doesn't sound like you do!"
    "I can feel my cheeks flushing with colour."
    "And Emma's eyes seem to be boring into me the whole time."
    mike.say "Don't rush me, Emma!"
    mike.say "I almost had it for a moment there..."
    "Emma rolls her eyes and elbows me aside."
    "I don't know if she meant to be that rough."
    "But she really drove it into my ribs!"
    emma.say "You're not helping me if you don't get this stuff, [hero.name]."
    emma.say "All it means is that you're getting in the way!"
    emma.say "So I think I'd better study alone from now on."
    return

label emma_ask_phone_male:
    mike.say "Hey, Emma..."
    mike.say "Can I get your number?"
    if hero.charm >= 20 - emma.love:
        $ hero.smartphone_contacts.append("emma")
        emma.say "Oh, sure thing..."
        emma.say "There you go, [hero.name]!"
        emma.say "Don't you lose it now!"
    else:
        $ emma.love -= 1
        $ emma.sub -= 1
        emma.say "Hmm..."
        emma.say "I don't think so, [hero.name]."
        emma.say "I'm just not ready for that yet."
    return

label emma_ask_birthday_male:
    mike.say "Emma, I wanted to ask you something..."
    mike.say "When is your birthday?"
    if hero.charm >= 40 - emma.love:
        $ emma.flags.birthdayknown = True
        emma.say "D...didn't I tell you already?"
        emma.say "Oh, I can be such a scatter-brain!"
        emma.say "It's Spring 27."
    else:
        show emma annoyed
        $ emma.sub -= 1
        $ emma.love -= 1
        emma.say "I know that I already told you that, [hero.name]!"
        emma.say "You'd better try harder to remember it!"
    return

label emma_offer_a_drink_male:
    mike.say "You ready for a drink, Emma?"
    mike.say "I know I am!"
    "Almost the second the words are out of my mouth, Emma turns to face me."
    if emma.is_visibly_pregnant:
        $ emma.love -= 10
        emma.say "I can't drink alcohol when I'm pregnant!"
        emma.say "Oh, [hero.name], that's so thoughtless of you!"
        $ hero.cancel_activity()
        hide emma
    elif (hero.charm >= 60 - emma.love and emma.flags.drinks < 2) or date_girl == emma:
        emma.say "Erm..."
        emma.say "Okay, [hero.name], I guess."
        emma.say "Can I get a cider or whatever?"
        hide emma
        show drink emma
        if emma.love <= 25:
            $ emma.love += 1
        elif date_girl == emma and game.active_date:
            $ game.active_date.score += 5
        call expression emma.get_chat from _call_expression_227
        hide drink emma
        $ emma.set_flag("drinks", 1, "day", mod="+")
    else:
        emma.say "Oh no!"
        emma.say "No way, [hero.name]!"
        emma.say "Are you trying to get me drunk?!?"
        $ hero.cancel_activity()
        hide emma
    return

label emma_slap_ass_intro_male:
    "It's probably the last thing that Emma would expect."
    "But her ass has been calling to be all the time we've been together today."
    "It's like a siren, summoning me with it's song!"
    "Only this is the way it moves under her clothes."
    "I don't have a choice - I just have to slap it!"
    return

label emma_slap_ass_happy_male:
    emma.say "Wha..."
    emma.say "What...what was that?!?"
    "Emma looks this way and that in a state of confusion."
    "And it takes a couple of seconds for reality to dawn on her."
    emma.say "[hero.name], was that you?"
    emma.say "Did you slap my butt?!?"
    "I give her a guilty nod in way of an answer."
    "And Emma blushes, but smiles."
    emma.say "Oh...okay..."
    emma.say "I guess that means you like it!"
    return

label emma_slap_ass_angry_male:
    emma.say "Wha..."
    emma.say "What...what was that?!?"
    "Emma looks this way and that in a state of confusion."
    "And it takes a couple of seconds for reality to dawn on her."
    emma.say "[hero.name], was that you?"
    emma.say "Did you slap my butt?!?"
    "I give her a guilty nod in way of an answer."
    "And Emma blushes, but her eyes flare with anger."
    emma.say "That is SO not okay!"
    emma.say "Don't do it again!"
    return

label emma_breakup_male:
    show emma
    "You know those times when you have a dream come true?"
    "It seems like the best thing in the world when it happens."
    "But once the shine starts to come off of the thing..."
    "Well, there's a danger that it could turn into a nightmare!"
    "And that's what I want to keep from happening."
    mike.say "Emma..."
    mike.say "We need to have a talk..."
    "Now Emma's a girl that has big eyes to begin with."
    "But now they seem to grow right before my own eyes."
    "And she's staring at me with them, like a deer in the headlights!"
    show emma fear
    emma.say "Oh no..."
    emma.say "Oh no, no, no..."
    emma.say "I know what that means, [hero.name]!"
    "I can feel myself starting to sweat already."
    "This wasn't supposed to be so hard."
    "I was going to let her down gently."
    "I was going to say we could still be friends!"
    mike.say "No, Emma - it's not what you think!"
    mike.say "Well, no...it's exactly what you think..."
    mike.say "But it doesn't have to be as bad as you think, you get me?"
    "I see hope blossom in Emma's eyes."
    "And then it dies again, just as quickly."
    emma.say "What are you trying to say, [hero.name]?"
    emma.say "Are you breaking up with me?"
    emma.say "Or are you just trying to confuse me?!?"
    mike.say "Ah..."
    mike.say "The first one, Emma."
    mike.say "I think we should end it..."
    show emma annoyed
    "Emma's mouth becomes a thin line."
    "She gives me one quick nod of the head, nothing more."
    emma.say "If that's what you want, [hero.name]."
    emma.say "Because what you want is obviously all that matters!"
    show emma cry
    emma.say "Urgh..."
    emma.say "I wish you'd never had that stupid dream."
    emma.say "But that's the only place you'll be seeing me from now on!"
    return

label emma_go_steady_intro_male:
    mike.say "Emma, we really should be going steady."
    mike.say "I mean, this thing is working out pretty well."
    mike.say "And I'm loving every moment of it!"
    return

label emma_go_steady_yes_male:
    emma.say "Of course we should, [hero.name]!"
    emma.say "Let's make it official - right now!"
    "Emma stands on her tiptoes to kiss me."
    "Which feels like it seals the deal."
    return

label emma_go_steady_no_male:
    emma.say "Oh no, [hero.name], not now."
    emma.say "I mean, maybe sometime soon."
    emma.say "But not now."
    return

label emma_pet_intro_male:
    "I can't resist reaching out and patting Emma on the head."
    "I only mean it as a gesture of affection, nothing more."
    "But as soon as I do it, I realise it could be take the wrong way!"
    return

label emma_pet_happy_male:
    emma.say "Ooh...oh my!"
    emma.say "That's different, [hero.name]!"
    emma.say "But I think I like it..."
    return

label emma_pet_annoyed_male:
    emma.say "I..."
    emma.say "I don't know what you're doing, [hero.name]."
    emma.say "But please, don't do it again!"
    return

label emma_massage_intro_male:
    mike.say "What's the matter, Emma?"
    mike.say "You look really tense today!"
    mike.say "Maybe a massage from yours truly would help?"
    return

label emma_massage_accept_male:
    emma.say "What?"
    emma.say "Oh...I guess so, [hero.name]."
    emma.say "I do have a pain in my neck!"
    emma.say "That massage sounds like a good idea."
    return

label emma_massage_refuse_male:
    emma.say "What?"
    emma.say "Oh...no, [hero.name]."
    emma.say "It hurts bad enough already."
    emma.say "I don't want someone else messing with it too!"
    return

label emma_piercing_nipples_reaction_male:
    emma.say "I...I really wasn't sure about this, [hero.name]."
    emma.say "But now that I actually had my nipples pierced..."
    emma.say "I...I kinda like it!"
    return

label emma_piercing_navel_reaction_male:
    emma.say "Huh...it looks...really nice!"
    emma.say "Maybe I should have pierced my belly-button before now."
    emma.say "Thanks for talking me into it, [hero.name]!"
    return

label emma_piercing_clit_reaction_male:
    emma.say "Ah...it feels kind of weird, [hero.name]..."
    emma.say "But that doesn't mean I don't like it!"
    emma.say "Because...I do...I really do!"
    return

label emma_piercing_head_reaction_male:
    emma.say "Ah...uh..."
    emma.say "This feels strange!"
    emma.say "But I think I'm getting used to it."
    emma.say "And I think I like it too!"
    return

label emma_piercing_nose_reaction_male:
    emma.say "Do you like it, [hero.name]?"
    emma.say "Because I DO like it myself."
    emma.say "But I like it when you like things too!"
    return

label emma_movie_disliked_reaction_male:
    emma.say "Oh...I...I really didn't like that movie - I wish we'd seen something else instead!"
    return

label emma_movie_indifferent_reaction_male:
    emma.say "That was...well...that was just kind of okay...I guess."
    return

label emma_movie_liked_reaction_male:
    emma.say "Oh wow...I LOVED that movie, just loved it!"
    return

label emma_belly_kiss_male:
    show emma stuned at center, zoomAt(1.25, (640, 880))
    mike.say "Emma..."
    mike.say "You know how you're kind of okay with me touching your bump?"
    "Emma's eyebrows rise as she hears the tone of my voice."
    "Which means that she's taking great care to analyse what I'm saying."
    show emma talkative
    emma.say "Yeah, [hero.name], I do."
    emma.say "And I seem to recall a part of that was based on you not making things weird."
    emma.say "Which I'm pretty sure you're about to test to it's limits, yeah?"
    show emma normal
    "I frown and wave a dismissive hand in the air."
    "Trying the best I can to make Emma's words sound ludicrous."
    mike.say "Of course I'm not!"
    mike.say "All I wanted to ask was for permission to touch it again."
    mike.say "Same thing as before, only this time using a different part of my body."
    "Now I'm doing everything I can to make it look like I'm not about to ask something weird."
    "Because I'm really not, I swear it!"
    show emma surprised
    emma.say "Oh, [hero.name]…"
    emma.say "Just tell me already, yeah?"
    show emma talkative
    emma.say "What are you wanting to do?"
    show emma normal
    "I shrug as I decide that I'm going to have to come clean."
    mike.say "I just wanted to kiss it, Emma."
    mike.say "Your belly, that is..."
    show emma blank
    "Emma stares at me blankly for a moment, like she's not sure what I actually mean."
    "Then she blinks a couple of times, as if her brain is finally processing my words."
    show emma surprised
    emma.say "You just want to kiss my belly?"
    show emma stuned
    mike.say "Yeah, Emma."
    show emma talkative
    emma.say "Well that sounds okay."
    show emma normal
    "Emma's already lifting her top as she says this."
    "So I know that she's totally onboard with the idea."
    show emma at center, traveling(2.0, 0.5, (640, 980))
    "And I don't waste any time in getting down on my knees."
    "Then I start planting gentle kisses on the curve of her belly."
    "All the time wondering why people always seems to assume I have something weird in mind."
    "Oh, and pondering the notion that this might also mean Emma's up for other stuff too."
    "Like maybe involving her feet..."
    return

label emma_belly_caress_male:
    show emma annoyed at center, zoomAt(1.25, (640, 880))
    "I can see that Emma's looking uncomfortable with her bump today."
    "Shifting this way and that as she tries to make it rest comfortably."
    "And who could blame her when the thing is already as big as that?"
    "I sometimes think, when I see her staggering along and holding it..."
    "That she's going to lose her balance without warning and topple over."
    "Which is one of the reasons that I've been keeping such a close eye on her."
    mike.say "Emma..."
    mike.say "Are you okay?"
    mike.say "Like, do you need a hand with anything?"
    show emma blush
    "Emma looks up at me, her cheeks red and her expression one of genuine frustration."
    "And for a moment I don't know how she's going to react to the question."
    "Whether she's going to accept the offer or tell me off for patronising her."
    show emma whining
    emma.say "I..."
    emma.say "I don't know, [hero.name]!"
    emma.say "I...I don't feel like I know anything anymore!"
    show emma cry
    "Emma takes me by surprise when she suddenly gets teary."
    "Like her emotions are in as much turmoil as her balance."
    show emma at center, traveling(1.75, 0.5, (640, 1190))
    "So without saying another word, I hurry over to her."
    "Then I put an arm around Emma's shoulder, offering support."
    "And it comes as a relief when I feel her lean her weight against me."
    show emma sad
    "It's also a relief when Emma seems to stop having an emotional breakdown too."
    "Instead she lets out a sigh and kind of lets me support her."
    show emma normal
    "Almost like she's letting me know that she needs it without saying so."
    "In return I just keep right on holding her up."
    "At the same time my hand is caressing Emma's belly."
    "Feeling the curve of it and enjoying the warmth of her skin."
    "Maybe this is the answer to the problem when she gets into this kind of a state."
    "Rather than trying to talk it out or offer clever advice, I should just do this."
    "Because it sure seems to be hitting the spot right now."
    return

label emma_belly_listen_male:
    show emma annoyed at center, zoomAt(1.25, (640, 880))
    pause 0.2
    show emma at center, traveling(2.0, 1.0, (640, 980))
    "I lean in closer to Emma's belly, doing the best I can to tune out everything else."
    "And as soon as I have my ear pressed against it, I'm listening for the faintest sound."
    "I have no idea if this is going to work, or if I'm just going to look like a fool."
    "But of there's the slightest chance of hearing my unborn child moving in there..."
    "Well then I don't really care in the slightest what I look like when I hear it!"
    show emma talkative
    emma.say "Well?"
    emma.say "How's it going down there?"
    emma.say "Can you hear anything at all?"
    show emma normal at center, traveling(2.0, 0.5, (640, 1280))
    "I do the best I can to turn my head upwards without dislodging my ear."
    "But all I can manage is to be able to see Emma's face out of the corner of my eye."
    "It doesn't help matters that her belly is in the way either."
    mike.say "Shhh!"
    mike.say "How am I supposed to hear anything with you asking me all those questions?"
    mike.say "Plus the sound of your voice comes from inside of you, Emma."
    mike.say "The exact same place where the baby is right now."
    mike.say "So you're drowning them out!"
    show emma surprised
    "Emma opens her mouth to say something in response to this."
    show emma normal
    "And I don't know if it's to apologise or tell me off for telling her off."
    "But the she seems to realise what I'm talking about and nods."
    show emma at center, traveling(2.0, 1.0, (640, 980))
    "I take Emma's silence as permission to get back to the task at hand."
    "And so I close my eyes, focussing all of my attention on what I can hear."
    "There's little that I can make out to begin with."
    "Just a confused jumble of random sounds that I can't identify."
    "But now that I'm concentrating, I start to be able to tell them apart."
    "One by one, I figure out what each of them must be."
    "Like the constant thumping has to be the sound of Emma's heart beating."
    "And the rising and falling sound the breath going in and out of her lungs."
    "Which means that..."
    "Yes, there it is!"
    "The more random sound must be the baby moving in there."
    "It's muffled and softened by the fluid that they're suspended in."
    "But those are definitely the sounds of the baby moving inside Emma's belly!"
    "I know that she must be eager to know what I can hear right now."
    "And I'll be sure to tell Emma all about it as soon as I'm done listening."
    "But right now all I want to do is enjoy the moment and take it all in."
    "Because this is a big moment for me, the first time I've ever heard my kid with my own ears!"
    "And I want to spend as much time as I can listening to that strange, wonderful sound as I can."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
