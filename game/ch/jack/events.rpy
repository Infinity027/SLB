init python:
    Event(**{
    "name": "jack_event_01",
    "label": "jack_event_01",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDayOfWeek(6, 7),
        IsHour(14, 17),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom")
            ),
        PersonTarget(bree,
            Not(IsHidden())
            ),
        PersonTarget(sasha,
            Not(IsHidden())
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "jack_event_02",
    "label": "jack_event_02",
    "priority": 500,
    "conditions": [
        IsDone("jack_event_01"),
        IsDayOfWeek("12345"),
        IsHour(14, 17),
        HeroTarget(
            IsGender("male"),
            IsFlag("jackrpg", False)
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "jack_event_03",
    "label": "jack_event_03",
    "priority": 500,
    "duration": 4,
    "conditions": [
        IsDone("jack_event_02"),
        IsDayOfWeek(6, 7),
        IsHour(14, 17),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom")
            ),
        PersonTarget(bree,
            Not(IsHidden())
            ),
        PersonTarget(sasha,
            Not(IsHidden())
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "jack_event_04",
    "label": "jack_event_04",
    "priority": 500,
    "duration": 4,
    "conditions": [
        IsDone("jack_event_03"),
        IsDayOfWeek(6, 7),
        IsHour(14, 17),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom")
            ),
        PersonTarget(bree,
            Not(IsHidden()),
            MinFlag("likerpg", 1)
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            MinFlag("likerpg", 1)
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "jack_event_05",
    "label": "jack_event_05",
    "priority": 500,
    "duration": 2,
    "conditions": [
        IsDone("jack_event_04"),
        IsTimeOfDay("afternoon", "evening"),
        InInventory("zbox_360"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            ),
        PersonTarget(bree,
            Not(IsHidden()),
            InHarem('home'),
            HasRoomTag("home"),
            MinFlag("kiss", 1),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            InHarem('home'),
            HasRoomTag("home"),
            MinFlag("kiss", 1),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "jack_nude_beach",
    "label": "jack_nude_beach",
    "conditions": [
        IsDone("jack_event_01"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("pub"),
            ),
        "hero.sexperience >= 10"
        ],
    "priority": 500,
    "do_once": True,
    })


label jack_event_01:
    play sound door_knock
    "The sound of a knock at the door makes me look up from what I'm doing."
    "Funny - I wasn't expecting any visitors today."
    "And neither of the girls warned me that they were either."
    "I'm up and on my way to the door by the time whoever it is knocks for a second time."
    scene bg house
    show jack normal
    with wiperight
    "I open the door to be greeted by Jack's smiling face."
    "Sure, it's great to see my old friend."
    "But what does he want?"
    show jack happy
    jack.say "Hey, [hero.name]!"
    jack.say "How's it hanging?"
    mike.say "Ah...hey, Jack."
    jack.say "Well, aren't you gonna invite me in?"
    mike.say "Oh..."
    mike.say "Sure, sure - come on in."
    scene bg livingroom
    "Jack purses his lips and whistles as we walk into the sitting room."
    jack.say "Sweet place you got here, man."
    jack.say "In fact, it's perfect!"
    mike.say "P...perfect?"
    mike.say "Perfect for what?"
    show jack normal
    jack.say "Playing a game of Demons and Demi-Gods of course!"
    jack.say "You remember - 'The Double D RPG'!"
    "I can't help looking like I just noticed a bad smell in the room."
    mike.say "Really, Jack?"
    mike.say "Fourth edition totally sucked..."
    jack.say "I have fifth edition now - much better!"
    jack.say "We could even play it out by the pool."
    jack.say "Roll the dice on the edge!"
    mike.say "Well, yeah...I guess so."
    mike.say "But isn't this all a bit out of the blue?"
    jack.say "Oooh, yeah - you didn't hear about Spencer?"
    mike.say "Used to play at the games store?"
    mike.say "Sweat pants and personal hygiene issues?"
    jack.say "That's the one."
    jack.say "Well, he went postal in the middle of a game."
    mike.say "You mean he killed a bunch of people?!?"
    jack.say "What?"
    jack.say "No, I mean he lost his shit."
    jack.say "Hadn't been taking his medication or something."
    jack.say "Anyway, that got the game kicked out of the store."
    jack.say "And I've been looking for somewhere to host it ever since..."
    "I'm beginning to see where this is going."
    "But before I can get a word out in response, the door opens."
    "*door opens*"
    "I see [bree.name] standing in the doorway."
    "She's dressed in her pyjamas and looks pretty sleepy."
    hide jack
    show bree sleep
    bree.say "Is everything okay down here?"
    bree.say "I heard you talking all the way upstairs!"
    mike.say "It's fine, [bree.name] - nothing to worry about."
    mike.say "This is Jack."
    mike.say "An old friend from school..."
    hide bree
    show bree sleep at left
    show jack perv at right
    "Jack's eyes are practically out on stalks right now."
    jack.say "Holy crap, man - is this your housemate?!?"
    mike.say "Uh...yeah, Jack."
    mike.say "This is [bree.name]."
    jack.say "Hey, nice Rainbow Smash shirt!"
    bree.say "Huh?"
    bree.say "Thanks, Jack - good eye!"
    bree.say "Did I hear you talking about RPGs just now?"
    jack.say "Oh hell yeah, [bree.name] - I'm a veteran Gamesmaster!"
    jack.say "In fact...[hero.name] and me are starting up a new game."
    jack.say "Would you like to play too?"
    bree.say "Like co-op?"
    bree.say "What platform?"
    mike.say "He means tabletop role playing, [bree.name]."
    mike.say "You know - pens, paper and dice?"
    show bree sleep happy
    bree.say "Oooh - that sounds SO retro!"
    bree.say "I always wanted to try it out."
    jack.say "Awesome - this is going to be SO cool!"
    "I can see that he's almost shaking with excitement at the prospect."
    "And I can't say that I blame him."
    "We've never played with a girl before, let alone one as hot as [bree.name]!"
    hide bree
    show jack normal
    "But, then I see Jack sag, like the air's been let out of him."
    jack.say "Urrgh!"
    jack.say "The game I wanted to run needs THREE players."
    jack.say "It won't work with just two..."
    show sasha towel at left
    show jack perv at right
    sasha.say "What the fuck are you all yelling about, huh?"
    "All three of us look around to see Sasha standing in the doorway."
    "She has her arms crossed over her chest."
    "But I can't tell if that's because she's pissed or just to hold up the towel she's wearing."
    sasha.say "I was trying to unwind in the bath!"
    "Jack turns to face me, a look of amazement on his face."
    jack.say "You have ANOTHER housemate that's a girl?!?"
    jack.say "Wow - she's like a goddess or something!"
    show sasha annoyed
    "Sasha raises an eyebrow at the comment."
    "Like she doesn't know whether to be annoyed or amused."
    sasha.say "I've attracted a few worshippers in my time."
    hide jack
    show sasha towel at left
    show bree casual happy at right
    "[bree.name] suddenly lets out a high-pitched squeal and claps her hands together."
    bree.say "Guess what, Sasha - we're gonna play a roleplaying game."
    bree.say "Right here in the house - and you can play too!"
    sasha.say "Huh, is that so?"
    sasha.say "I suppose I could give it a try."
    sasha.say "But it better not be all unicorns and rainbows."
    sasha.say "Urgh...that stuff makes me want to puke!"
    hide bree
    show sasha towel at left
    show jack perv at right
    "Jack lets out a snicker of sheer delight."
    jack.say "It's called Demons and Demi-Gods."
    sasha.say "Well...that sounds more promising."
    jack.say "And don't worry, I'll make sure it's adult."
    jack.say "Very adult indeed..."
    "I can see that Jack's getting distracted by what's under Sasha's towel."
    "And so I give him an elbow in the ribs."
    jack.say "Oh...I...I'll give you a call!"
    hide jack
    hide sasha
    "Jack hurries to let himself out, and I hear the door slam shut behind him."
    "I sigh to myself, mentally clearing my evenings to make way for his game."
    "Probably better that I'm here to keep an eye on him the whole time."
    "Leaving him alone with [bree.name] and Sasha seems like a bad idea."
    "Especially if he's planning on making this game as adult as it sounds..."
    $ game.flags.jackrpg = TemporaryFlag(True, 7)
    return

label jack_event_02:
    "When my phone rings, I don't even bother to look at the caller ID."
    "Instead I just put it to my ear, relying on the person calling to identify themselves."
    mike.say "Hey."
    mike.say "What's up?"
    jack.say "Hey, man!"
    jack.say "Sorry it took me so long to call."
    mike.say "It did?"
    mike.say "I mean...sure it did."
    mike.say "Ah...what was this all about again?"
    jack.say "The RPG, man!"
    jack.say "The game of Demons and DemiGods."
    jack.say "You remember - the one I'm running for your hot housemates?"
    mike.say "Oh...yeah, of course."
    mike.say "And me, right?"
    jack.say "Huh?"
    mike.say "And me - you said you needed three of us?"
    jack.say "Yeah, yeah...sure I did!"
    jack.say "Anyway..."
    jack.say "I've got everything ready to go."
    jack.say "I finished writing the scenario and I rolled up some characters too."
    mike.say "Huh..."
    mike.say "I was kinda looking forward to rolling up my own."
    mike.say "I feel like playing a bard or a ranger this time around."
    jack.say "Ah...I already rolled you up a paladin, man."
    jack.say "And the scenario really needs you to play one too."
    mike.say "Oh...okay, if you say so."
    jack.say "It's just for [bree.name] and Sasha, you know?"
    jack.say "To ease them into it - help them get to grips with the rules."
    jack.say "Plus there's some changes from fourth edition that might throw you too."
    mike.say "Well, that makes sense, I guess."
    jack.say "Great, that's great, [hero.name]."
    jack.say "So, how does this weekend sound - afternoon?"
    mike.say "Fine, I think."
    mike.say "I know I'm free."
    mike.say "But I'll run it by [bree.name] and Sasha."
    mike.say "Just assume it's on if you don't hear from me, okay?"
    jack.say "You got it, buddy."
    jack.say "This is gonna be SO cool!"
    "And with that, he hangs up, leaving me to tell [bree.name] and Sasha the good news."
    $ game.flags.jackrpg = TemporaryFlag(True, 7)
    return

label jack_event_03:
    scene bg livingroom
    show bree casual at left
    show sasha casual at right
    show jack normal
    with fade
    "Jack turns up early on the allotted day, and I help him to set up everything we'll need for the game."
    "This means that we have to entirely take over the dining room table with books, dice and paper."
    "But also that I have to hustle [bree.name] and Sasha out of the way until he's satisfied that we're ready."
    "Which is a far harder task than it sounds, as both of them are pretty curious to see what we're doing."
    jack.say "[hero.name], stop her - those are my GM's notes!"
    mike.say "Hey, [bree.name] - stop peeking at those!"
    show bree lose
    bree.say "Aww, no fair!"
    bree.say "And it's not like I can read Jack's handwriting anyway..."
    show bree normal
    jack.say "[hero.name], the other one, the other one!"
    mike.say "Sasha, that's the GM's Guide - only Jack gets to read that!"
    show sasha angry
    sasha.say "I just wanted to look at the artwork."
    show sasha normal
    sasha.say "There are some great pictures of monsters and demons in here!"
    scene bg livingroom
    show rpg
    with fade
    "Pretty soon we're all set up and ready to go."
    "Jack stares at us over the top of his GM's screen."
    jack.say "Okay, here are you character sheets."
    bree.say "Thanks, Jack!"
    "Jack waves a finger in [bree.name]'s direction, shaking his head at her."
    bree.say "Ooh..."
    bree.say "What's the matter - did I do something wrong?"
    mike.say "Ah, Jack likes people to call him 'Gamesmaster' while we play the game..."
    bree.say "Okay - thank you, Gamesmaster!"
    "Jack nods and smiles, pleased with the tone of [bree.name]'s voice."
    "But I see Sasha roll her eyes at the same time."
    jack.say "[bree.name], you'll be playing an elven cleric of the God of Love."
    bree.say "Aww!"
    bree.say "I promise to spread the wonder of true love and happiness wherever I may roam!"
    sasha.say "Urgh..."
    sasha.say "Passeth ye olde bucket, because I think I'm gonna be sick!"
    jack.say "Sasha, you're half-demon warlock."
    sasha.say "So, I'm like what - a witch from Hell?"
    jack.say "Pretty much, yeah."
    sasha.say "Sweet!"
    sasha.say "Can I turn [bree.name] into a frog?"
    bree.say "Hey, Sasha!"
    mike.say "Let's just get to grips with the basics, maybe?"
    mike.say "We can worry about turning each other into things later."
    bree.say "Oh, but what about [hero.name]?"
    sasha.say "Yeah, who is he supposed to be?"
    bree.say "I bet he's like a swashbuckling pirate or something!"
    sasha.say "Nah, he has to be a barbarian, with huge muscles and a massive chopper too!"
    jack.say "Both wrong - he's a Paladin."
    bree.say "A what?!?"
    jack.say "A holy warrior devoted to the cause of all that's good and pure."
    sasha.say "Oh...sucks to be you, [hero.name]!"
    mike.say "Thanks, Sasha!"
    mike.say "So just to be sure, Jack - we HAVE to play these characters?"
    jack.say "Yeah, it's essential to the plot of the scenario."
    mike.say "Okay, whatever..."
    hide rpg
    show rpg tavern
    with fade
    jack.say "Right, you have all been drawn to the sleepy village of Little Snoring by the promise of adventure."
    jack.say "Goblins have been raiding the outlying farms."
    jack.say "And the call has gone out for stout adventurers to put an end to their attacks."
    jack.say "The three of you find yourselves in the taproom of the local tavern."
    bree.say "Uhm...what's a tavern?"
    sasha.say "An old-fashioned pub."
    bree.say "Oh, okay!"
    jack.say "What do you do?"
    sasha.say "I stride up to the bar and demand ale!"
    bree.say "Ooh, that sounds like fun - me too!"
    mike.say "I follow them."
    jack.say "The wench behind the bar eyes [bree.name] and Sasha suspiciously."
    jack.say "'We don't serve their kind!' she says as she looks between them."
    sasha.say "What the hell?"
    bree.say "Erm...isn't that racist or something?!?"
    menu:
        "Defend [bree.name]":
            mike.say "I step up and challenge the wench."
            mike.say "'You should be thankful that an elf would even set foot in a pigsty like this!'"
            mike.say "'Now show some respect, wench!'"
            bree.say "Wow - my knight in shining armour!"
            jack.say "The wench looks justly chastened by the paladin's words."
            jack.say "'Very well,' she says, 'the elf I'll serve.'"
            jack.say "'But not the hellspawned bitch by her side!'"
            show rpg sashabored
            sasha.say "Hey!"
            $ bree.flags.likerpg += 1
        "Defend Sasha":
            mike.say "I step up and challenge the wench."
            mike.say "'I am a paladin of the holy order, and I vouch for this maiden.'"
            mike.say "'Would you question my judgement, wench!'"
            sasha.say "Yeah, you tell the bitch, [hero.name]!"
            jack.say "The wench looks justly chastened by the paladin's words."
            jack.say "'Very well,' she says, 'the hellspawn I'll serve.'"
            jack.say "'But not the pointy-eared bitch by her side!'"
            show rpg breebored
            bree.say "Hey!"
            $ sasha.flags.likerpg += 1
    show rpg livingroom sashanormal breenormal
    jack.say "Now that you have your drinks, you head over to a free table."
    jack.say "It's then that you see a little old man coming over to join you."
    jack.say "'Greetings,' he says, 'you have the look of mighty adventurers about you.'"
    jack.say "'My name is Elder Perkins, and I would like to enlist your help to deal with the goblins in the hills."
    show rpg tavern
    sasha.say "I lean forwards and look him straight in the eye."
    sasha.say "'Hey, old man - we don't work for free!'"
    bree.say "That's mean, Sasha!"
    bree.say "'Do not worry, Elder Perkins - my companion is mistaken.'"
    bree.say "'We will do this thing out of the goodness of our hearts.'"
    menu:
        "Side with [bree.name]":
            mike.say "[bree.name]'s right, Sasha."
            mike.say "Plus, we might find some loot when we fight the goblins."
            mike.say "'Yes, Elder - we will do this deed because it is the right thing to do.'"
            bree.say "See, Sasha?"
            bree.say "It's nice to be nice!"
            show rpg sashabored
            sasha.say "You two are no fun!"
            $ bree.flags.likerpg += 1
        "Side with Sasha":
            mike.say "Sasha's right, [bree.name]."
            mike.say "We need some cash to buy gear and stuff like that."
            mike.say "'No, Elder - we must insist on some monetary sum.'"
            mike.say "'Even if only for the sake of ensuring we are able to succeed at the quest.'"
            sasha.say "See, [bree.name]?"
            sasha.say "You've got to know your own value!"
            show rpg breebored
            bree.say "You two are SO mean!"
            $ sasha.flags.likerpg += 1
    show rpg livingroom sashanormal breenormal
    jack.say "Elder Perkins nods in agreement."
    jack.say "'It is agreed,' he says."
    jack.say "'In order to aid you on your quest, I can offer you the choice of these two items.'"
    jack.say "He reaches into the folds of his robe and pulls out two vials of liquid."
    jack.say "One blue and one red in colour."
    show rpg tavern
    sasha.say "What is this - the fucking Matrix with added mud?"
    bree.say "Sasha!"
    jack.say "'A potion of healing or a potion of fireballs.'"
    jack.say "'Choose only one, and choose wisely!'"
    bree.say "Shouldn't we take the healing one?"
    bree.say "You know, in case one of us gets hurt?"
    sasha.say "Screw that - I want to take the fireball potion!"
    mike.say "Well, [bree.name]'s a cleric."
    mike.say "So she already has healing spells."
    sasha.say "That settles it then - we take the fireball potion."
    bree.say "Aww!"
    menu:
        "Side with [bree.name]":
            mike.say "Wait a minute, Sasha."
            mike.say "If [bree.name] gets too hurt to use her spells, we might need a backup."
            mike.say "So we should take the healing potion."
            bree.say "See - I told you I was right!"
            show rpg sashabored
            sasha.say "BORING!"
            $ bree.flags.likerpg += 1
        "Side with Sasha":
            mike.say "We should take the fireball potion, [bree.name]."
            mike.say "Healing's the cleric's job, kind of like a first-aider."
            mike.say "You kind of need to get that about your character."
            sasha.say "Yeah, [bree.name] - know your role!"
            show rpg breebored
            bree.say "I...I'm sorry, [hero.name]."
            bree.say "I never played this kind of game before..."
            $ sasha.flags.likerpg += 1
    show rpg livingroom sashanormal breenormal
    "Briefed on our first quest and armed with our chosen potion, Jack chooses that point to call it a day."
    jack.say "I think we'll leave it there for now."
    jack.say "So how did you girls find your first roleplaying session?"
    if bree.flags.likerpg == 0:
        bree.say "Please don't be mad at me, [hero.name]."
        show rpg breebored
        bree.say "But I didn't like it."
        jack.say "Huh?"
        mike.say "Why, [bree.name]?"
        "[bree.name] takes a deep breath before she explains herself."
        bree.say "Well..."
        bree.say "I kinda felt like you and Sasha were picking on me, you know?"
        mike.say "Oh..."
        mike.say "I'm sorry, [bree.name]."
        sasha.say "Urgh..."
        sasha.say "It's just a game, [bree.name]."
        sasha.say "Why'd you have to take it personally?"
        bree.say "That's just how I feel."
        bree.say "And I don't think I want to play anymore."
        sasha.say "Well I do!"
        sasha.say "Can we do it next weekend?"
        mike.say "I'm up for it."
        mike.say "We could maybe make it a regular thing?"
    elif sasha.flags.likerpg == 0:
        show rpg sashabored
        sasha.say "I thought it sucked - big time!"
        jack.say "Huh?"
        mike.say "Why, Sasha?"
        "Sasha shakes her head in frustration."
        sasha.say "It's lame, you know?"
        sasha.say "I want to be bad, because I'm playing a demon."
        sasha.say "But you two are such a pair of do-gooders!"
        mike.say "Oh..."
        mike.say "I'm sorry, Sasha."
        bree.say "Oh, Sasha."
        bree.say "It's just a game!"
        sasha.say "Exactly, [bree.name]."
        sasha.say "It's just a lame kid's game, that's all."
        sasha.say "And I've got better things to do with my time!"
        bree.say "Well I want to keep playing."
        bree.say "Can we do it next weekend?"
        mike.say "I'm up for it."
        mike.say "We could maybe make it a regular thing?"
    else:
        bree.say "Well, I liked it a lot."
        mike.say "Really?!?"
        mike.say "That's great, [bree.name]!"
        sasha.say "Yeah, I got a kick out of it."
        sasha.say "I want to see what my spells do!"
        bree.say "Ooh - me too!"
        jack.say "So you want to play again?"
        bree.say "You bet I do!"
        sasha.say "Can we do it next weekend?"
        mike.say "I'm up for it."
        mike.say "We could maybe make it a regular thing?"
        sasha.say "So long as we get to slay some goblins next time!"
        bree.say "Leave some for me, Sasha!"
    $ game.flags.jackrpg = TemporaryFlag(True, 7)
    $ sasha.love += sasha.flags.likerpg
    $ bree.love += bree.flags.likerpg
    scene bg livingroom
    show jack normal
    with fade
    "After [bree.name] and Sasha have left the room, I help Jack to pack away all of his stuff."
    jack.say "I thought that went pretty well."
    mike.say "Not bad for a bunch of first-timers."
    jack.say "So I'll see you next weekend - same time?"
    mike.say "Sure thing, Gamesmaster!"
    $ hero.replace_activity()
    return

label jack_event_04:
    $ renpy.dynamic("today")
    $ today = game.calendar.day_of_week_name.capitalize()
    scene bg livingroom
    show bree casual at left
    show sasha casual at right
    with fade
    "By the time the next [today] afternoon rolls around, [bree.name] and Sasha are getting pretty excited."
    "And I have to admit to being more than a little surprised by how much they're looking forward Jack's arrival."
    "I never would have thought that two such hot girls could be so into the idea of playing Double D!"
    show fx question at left
    bree.say "What time is it, [hero.name]?"
    mike.say "Erm, it's about five minutes since you last asked me, [bree.name]!"
    show sasha annoyed
    show fx anger at right
    sasha.say "Urgh..."
    sasha.say "It feels like we've been waiting forever!"
    mike.say "Really, Sasha?"
    mike.say "Because it's not like Jack's actually late or anything..."
    scene bg black
    show rpg nojack
    with fade
    "We're already sitting at the table in the dining room, and I have everything ready to go."
    "I figured that it'd be quicker to break out my roleplaying stuff than have Jack set up when he got here."
    "But all that seems to have done is make [bree.name] and Sasha all the more desperate to get started."
    "I watch as Sasha leans back in her chair, rolling her eyes."
    "And [bree.name] slumps forward onto the table, leaning her head on her arms over her character sheet."
    mike.say "Hey, cheer up, guys!"
    mike.say "I'm sure he'll be here on time."
    "I look desperately for something to distract the girls."
    "And it's then that I notice they've each got a set of new dice."
    mike.say "Wow - you guys bought your own dice?"
    mike.say "You really are serious gamers now!"
    "Both of the girls seem to perk up at this."
    "And I remember how much they like to show off a new outfit when they've been shopping."
    "Seems like their purchases for playing the game are no different either!"
    bree.say "Look at my dice, [hero.name]."
    bree.say "They're so cute!"
    show rpg sashabored
    sasha.say "Whatever, [bree.name]..."
    show rpg sashanormal
    sasha.say "He really wants to check mine out - they're seriously badass!"
    "Suddenly they're both waving their dice in my face!"
    "I can see that [bree.name]'s are bright pink, and glittery too."
    "Sasha's are a glossy black and veined with a red the shade of blood."
    menu:
        "Look at [bree.name]'s dice":
            mike.say "Hah!"
            mike.say "I should have known you'd choose pink, [bree.name]!"
            bree.say "Huh?"
            bree.say "Why's that?"
            mike.say "Well..."
            mike.say "You're a cleric of the goddess of love."
            mike.say "Pink is kind of a healing, caring colour, you know?"
            bree.say "I see what you mean."
            bree.say "It's my mission to spread love and harmony wherever I go!"
            show rpg sashabored
            sasha.say "Eww..."
            sasha.say "Pass the barf bucket!"
            bree.say "SASHA!"
            $ bree.flags.likerpg += 1
        "Look at Sasha's dice":
            mike.say "Ooh..."
            mike.say "Those are pretty dark, Sasha."
            mike.say "I like it!"
            sasha.say "Is that so?"
            sasha.say "What is it that you like, precisely?"
            mike.say "It's like they're all part of your vibe, you know?"
            mike.say "A dark, troubled spellcaster that's got a mysterious past."
            sasha.say "Yeah...yeah, I like that!"
            sasha.say "It's like I'm bad, but I have layers that go really deep."
            show rpg breebored
            bree.say "Or you're just like a gothy tramp!"
            sasha.say "BREE!"
            $ sasha.flags.likerpg += 1
    show rpg sashanormal breenormal
    play sound door_bell
    "It's right about then I hear the sound of someone ringing the doorbell."
    "Saved by bell or what?"
    "And for all that I was sure he'd make it, I'm relieved to see Jack when I open the door!"
    scene bg house
    show jack normal
    with wiperight
    jack.say "Hey, man."
    mike.say "Hey, Jack - am I ever glad to see you!"
    "I hurry Jack through the house, not letting him as much as catch his breath."
    jack.say "Wha...what's up?!?"
    mike.say "The natives are restless!"
    "Jack looks suitably confused."
    "But then I shove him into the dining room and he sets eyes on [bree.name] and Sasha."
    scene bg livingroom
    show bree casual at left
    show sasha casual at right
    show jack happy
    jack.say "HEY LADIES!"
    jack.say "Who's ready for a session of hot and heavy roleplaying action?!?"
    show bree happy at left
    bree.say "Ooh, me...I do!"
    show sasha happy at right
    sasha.say "Count me in, Gamesmaster!"
    scene rpg
    "Jack smiles at me as he sits down, gleeful to have their undivided attention."
    "I'll bet his dick's so hard right now he could cut glass with it!"
    "I take my seat at the table as Jack unpacks his stuff and gets into his stride."
    jack.say "Okay, quick recap."
    jack.say "Beautiful cleric [bree.name] and Smouldering Sorceress Sasha had answered the call to fight the goblins!"
    bree.say "That's right!"
    sasha.say "Fuck those goblin bastards!"
    mike.say "Erm...what about me?"
    jack.say "What?!?"
    jack.say "Oh yeah...and [hero.name] the paladin was tagging along too."
    "I try not to let my annoyance with Jack show."
    "I guess I should let him off."
    "After all, it's not often he has girls hanging off his every word."
    if Person.is_not_hidden("minami"):
        minami.say "Ooh!"
        "As one, we all look up to see Minami bound into the room."
        minami.say "Dice...pencils and paper...a sweaty nerd..."
        jack.say "Hey!"
        minami.say "Are you guys playing an RPG?!?"
        mike.say "Ah, yeah, Minami."
        mike.say "What's it to you?"
        minami.say "I wanna play too!"
        "[bree.name], Sasha and I exchange worried glances."
        mike.say "I don't know, Minami..."
        bree.say "We already have our characters..."
        sasha.say "We're in the middle of a quest..."
        jack.say "Of course you can play, Minami!"
        "Open-mouthed, we all stare at Jack."
        jack.say "I'm the Gamesmaster, and I say she can play."
        show rpg minami
        minami.say "YAY!"
        jack.say "In fact, it just so happens that I rolled up a character for Minami."
        jack.say "Just in case she wanted to join in."
        "Minami beams at Jack as he hands her a character sheet."
        "And I begin to recall the obvious crush he's always tried to deny having on her."
        minami.say "What's this - it says I'm a halfling!"
        jack.say "That's right - you're a halfling thief, dexterous and wily!"
        show rpg minamibored
        minami.say "Aww, but I don't want to be a halfling."
        "Minami aims all of her whining and pouting towards Jack."
        minami.say "I want to be a cat-girl instead - can I, Jack?"
        jack.say "Of course you can, Minami."
        "Jack grabs her character sheet and hastily rubs out some of the pencil scrawled on it."
        "Once he's made the appropriate changes, he hands it straight back."
        show rpg minaminormal
        jack.say "Overnight you meet Minami, the cat-girl thief."
        jack.say "Whom you realise would be a valuable addition to the party."
        show rpg sashabored breebored
        "[bree.name] and Sasha roll their eyes, while I can only sigh in annoyance."
        "It's pretty obvious to all three of us that Jack's going to let Minami get away with murder."
        show rpg sashanormal breenormal
    jack.say "First things first - experience points!"
    sasha.say "Huh - what are those?"
    mike.say "It's a reward for doing heroic things, Sasha."
    bree.say "Yeah, like when you upgrade your character in a videogame."
    menu:
        "Jack gives [bree.name] enough XP to level up":
            jack.say "Okay..."
            jack.say "Sasha and [hero.name], you got nine hundred points each."
            jack.say "Write that down on your character sheet."
            jack.say "But [bree.name] - you got one thousand."
            jack.say "And that means you level up!"
            bree.say "YAY!"
            show rpg sashabored
            sasha.say "Hey, wait a minute - how come she gets more than we do?"
            jack.say "Uh...well..."
            jack.say "It was for...it was for roleplaying her character - that's it!"
            jack.say "[bree.name] was super nice to people, just like a cleric of the love god should be."
            "[bree.name] continues to bask in Jack's praise."
            "But I can almost feel Sasha scowling at him without the need to look!"
            $ bree.flags.likerpg += 1
        "Jack gives Sasha enough XP to level up":
            jack.say "Okay..."
            jack.say "[bree.name] and [hero.name], you got nine hundred points each."
            jack.say "Write that down on your character sheet."
            jack.say "But Sasha - you got one thousand."
            jack.say "And that means you level up!"
            sasha.say "Alright!"
            show rpg breebored
            bree.say "No fair - how come she gets more than we do?"
            jack.say "Uh...well..."
            jack.say "It was for...it was for roleplaying her character - that's it!"
            jack.say "Sasha was mean and sassy, just like a half-demon sorceress should be."
            "Sasha continues to bask in Jack's praise."
            "But [bree.name] crosses her arms over her chest and lets out an annoyed grunt."
            $ sasha.flags.likerpg += 1
    scene rpg
    if Person.is_not_hidden("minami"):
        show rpg minami

    jack.say "Moving swiftly on..."
    jack.say "The very next morning you set out from the village in the direction of the goblin lair."
    show bg rpgroad
    show bree rpg at left
    show sasha b rpg at right
    if Person.is_not_hidden("minami"):
        show minami rpg
    "Jack makes us roleplay most of the journey."
    "And so we have to make rolls for random encounters and that kind of stuff."
    "It's pretty boring for me, but I guess he wants the girls to learn the ropes."
    "In fact, he seems to be behaving himself and keeping it nice and clean too."
    "Until it's time for us to strike camp for the night, that is..."
    scene bg rpgforest
    jack.say "So, you find a decent spot and collect wood for a fire."
    jack.say "But as you get out your bedrolls, [hero.name] - you get a shock."
    jack.say "There's a broken strap on your pack, and your bedroll is nowhere to be seen!"
    sasha.say "Oops - sucks to be you, [hero.name]!"
    bree.say "Oh no, you'll be cold and shivering all night long!"
    "I look at Jack as if asking for an explanation."
    "And he raises his eyebrows in a suggestive manner."
    jack.say "You could always SHARE a bedroll..."
    "Ah, so that's his game!"
    menu:
        "Ask to share [bree.name]'s bedroll":
            show mike rpg at left
            show bree rpg at right
            mike.say "Ah, [bree.name]..."
            mike.say "Do you think I could bed down with you for the night?"
            "[bree.name] positively beams at the question."
            bree.say "Of course you may, noble paladin."
            bree.say "Is it not the creed of my divine mistress that the warmth of her love be shared?"
            "I smile nervously back at [bree.name]."
            "But I can see that I've made Sasha feel left out."
            $ bree.flags.likerpg += 1
        "Ask to share Sasha's bedroll":
            show mike rpg at left
            show sasha b rpg at right
            mike.say "Ah, Sasha..."
            mike.say "Do you think I could bed down with you for the night?"
            "Sasha gives me an almost lascivious smile."
            sasha.say "Come over here, god-boy."
            sasha.say "Let's see if you can stay pure when you're that close to me all night!"
            "I smile nervously back at Sasha."
            "But I can see that I've made [bree.name] feel left out."
            $ sasha.flags.likerpg += 1
        "Ask to share Minami's bedroll" if Person.is_not_hidden("minami"):
            show mike rpg at left
            show minami rpg at right
            mike.say "Ah, Minami..."
            mike.say "Do you think I could bed down with you for the night?"
            "Minami positively beams at the question."
            minami.say "Purr...sure thing, big bro..."
            minami.say "Oops - I mean, sure thing, Mr Paladin!"
            minami.say "Purr...my claws are sharp, but my fur's soft and warm!"
            minami.say "Purr...and I won't tell anyone if you want to play with my tail either..."
            "I smile nervously back at Minami."
            "But I can see that I've made [bree.name] and Sasha feel left out."
            $ minami.flags.likerpg += 1
        "I will rough it out alone":
            "I know Jack's deliberately trying to make this awkward for me."
            "But that doesn't mean I have to play along."
            show mike rpg at left
            mike.say "Ah, keep your bedrolls."
            mike.say "I'll just wrap myself up in my woollen cloak."
            show bree rpg at right
            bree.say "Oh, [hero.name]!"
            show sasha b rpg
            sasha.say "You sure about that?"
            "I can almost sense the panic rising in Jack."
            "He wasn't counting on seeing his carefully laid plans thwarted like this!"
            jack.say "Ah...it's going to get REALLY cold, man!"
            jack.say "Like below zero or something!"
            mike.say "Don't worry about me."
            mike.say "I'm a hardy paladin - physical suffering hold no fear for me!"
            "It's then I see [bree.name] pondering something."
            bree.say "Sasha, why don't we share a bedroll?"
            sasha.say "Yeah, then we could let [hero.name] have the spare one!"
            "The look on Jack's face is incredible."
            "He's seeing the foiling of his original plan result in something better still!"
            mike.say "It's okay..."
            jack.say "No, they can do that if they want to!"
            if Person.is_not_hidden("minami"):
                hide mike
                show minami rpg at left
                minami.say "Hey, what about me!"
                bree.say "What about you?"
                sasha.say "Yeah, you've got a bedroll all to yourself!"
                minami.say "Aw...but I'll be all on my own!"
                sasha.say "Ah, go snort some catnip!"
            $ bree.flags.likerpg += 1
            $ sasha.flags.likerpg += 1
            $ minami.flags.likerpg += 1
    jack.say "You feel the need to snuggle down and get real close, yeah?"
    jack.say "Really share that body-heat!"
    "I can see Jack almost starting to sweat visibly as he imagines the scene."
    "And it's making me feel pretty uncomfortable too!"
    scene rpg
    if Person.is_not_hidden("minami"):
        show rpg minami
    mike.say "Ah...can we leave it there for now?"
    mike.say "I just remembered that my Mom's going to call me!"
    if Person.is_not_hidden("minami"):
        show rpg minamibored
        minami.say "Huh...she didn't say anything about it to..."
        minami.say "Hmmm...mmh...mmh..."
        "I cut Minami off by clapping a hand over her mouth before she can ruin my hasty excuse."
        show rpg minaminormal
    jack.say "Aww, man - just when it was getting good!"
    jack.say "Okay, whatever."
    "He turns to face [bree.name] and Sasha."
    if Person.is_not_hidden("minami"):
        "Then nods to Minami too."
    jack.say "Same time next week, ladies?"
    if bree.flags.likerpg < 2:
        show rpg breebored
        bree.say "Oh, I don't know..."
        jack.say "Huh?"
        mike.say "What's the matter, [bree.name]?"
        bree.say "I don't know - it just didn't feel as much fun as last time."
        bree.say "Count me out next for next week."
    elif sasha.flags.likerpg < 2:
        show rpg sashabored
        sasha.say "Nah, I think I'll pass."
        jack.say "Huh?"
        mike.say "What's the matter, Sasha?"
        sasha.say "I think the novelty of playing make-believe with sweaty nerds wore off!"
        sasha.say "Count me out next for next week."
    elif Person.is_not_hidden("minami") and minami.flags.likerpg == 0:
        show rpg minamibored
        minami.say "Meh..."
        jack.say "Huh?"
        mike.say "What's the matter, Minami?"
        minami.say "This is SO boring!"
        minami.say "I mean, I didn't get to kill ANYTHING!"
        minami.say "I'm out - not playing anymore."
    else:
        bree.say "Oh yeah."
        bree.say "I can't wait to get my hands on those mean goblins!"
        sasha.say "I want to see what my spells can do too!"
        if Person.is_not_hidden("minami"):
            minami.say "Purr...don't forget the cute, cat-girl too!"
        jack.say "Okay, it's a date!"
        $ game.flags.jackrpg = TemporaryFlag(True, 7)
    $ sasha.love += sasha.flags.likerpg
    $ bree.love += bree.flags.likerpg
    scene bg house
    show jack normal
    "Jack grabs his things and I show him to the door."
    "Walking back into the dining room, I'm already calling out to [bree.name] and Sasha."
    if Person.is_not_hidden("minami"):
        "Between them, Minami and me, it should be a quick clean-up operation!"
    mike.say "You guys want to help me tidy this stuff up?"
    mike.say "Guys?"
    scene bg black
    show rpg mikealone
    "I glance around the room, seeing empty chairs where the girls should have been."
    "Shaking my head, I begin the task of clearing away the roleplaying paraphernalia."
    "I'm just thankful neither of them is around to ask why my Mom didn't bother to call!"
    $ hero.replace_activity()
    return

label jack_event_05:
    $ game.room = "livingroom"
    scene bg livingroom with fade
    "I've been jealously guarding the Zbox in the sitting room for most of the day."
    "Every time [bree.name]'s as much as glanced at the thing, I've shooed her away from it."
    "And that's because she already agreed that it's mine until dawn tomorrow."
    "Look, I know that all of that sounds really crazy."
    "But trust me, there's a good reason I'm acting like such a possessive jerk."
    "And it's because I'm waiting to hear a knock at the door."
    play sound door_knock
    "As soon as that happens, I dart into the hallway and open the front door."
    "And there I see what at first seems to be a walking pile of snacks!"
    scene bg black with dissolve
    pause 0.1
    scene bg house
    show jack smile
    with wiperight
    jack.say "H...hey, buddy!"
    jack.say "Would you mind..."
    jack.say "Maybe grabbing some of this stuff?"
    show jack normal at center, zoomAt(1.5, (640, 1040)) with vpunch
    "I leap forwards, grabbing what I can and holding onto it."
    "And I just manage to stop an avalanche of unhealthy food spilling into the hallway."
    "This also allows me to see Jack's face beaming at me above the stuff he's still carrying."
    show jack smile
    jack.say "Well, are you going to ask me in or what?!?"
    jack.say "Last time I checked, you kept your Zbox inside the house!"
    show jack normal
    mike.say "Oh yeah..."
    mike.say "Sure, sure..."
    mike.say "Come on in!"
    "I step aside and let Jack waddle into the house with his load of snacks."
    hide jack with easeoutleft
    "He doesn't need to be shown the way, as he just forges a path to the sitting room."
    "Closing the door, I follow in his wake, still clutching the rest of the snacks."
    "Once we're in front of the TV, Jack raises his arms above his head."
    "And he lets all of the food he was carrying fall to the floor."
    show bg livingroom
    show jack happy
    with fade
    jack.say "The hour is upon us!"
    jack.say "Let the games commence!"
    show jack normal
    "I copy the gesture, dropping my load of snacks too."
    mike.say "In this hallowed arena, men will be tested!"
    mike.say "And only the strongest will triumph!"
    bree.say "Geez!"
    bree.say "I thought you two were just playing videogames?"
    show bree casual evil at top_mostright
    "Jack and I turn as one to see [bree.name] leaning against the doorframe."
    "Suddenly we both lower our arms, unable to hide our embarrassment."
    mike.say "That's exactly what we are doing, [bree.name]!"
    show jack blush
    jack.say "Y...yeah!"
    jack.say "We were just getting psyched up, that's all!"
    show bree happy at top_mostright, startle
    "[bree.name] snorts with laughter and shakes her head."
    show bree evil
    bree.say "Psyched up?"
    bree.say "Give me a break!"
    bree.say "You're such a pair of nerds."
    hide bree with easeoutright
    "Before I can think of a witty comeback, [bree.name] turns on her heel and walks away."
    "I can see Jack staring at the doorway, like he's waiting for the coast to be clear."
    "Then he looks me in the eye and whistles."
    show jack smile
    jack.say "Dude, seriously..."
    jack.say "I don't know how you can even think straight living here."
    show jack perv
    jack.say "I mean, just knowing a girl as hot as [bree.name]'s under the same roof as you!"
    show jack normal
    "I wave the comment off, trying to make it seem like nothing."
    "After all, I want to focus on gaming, not perving over my housemates."
    mike.say "Ah..."
    mike.say "It's not all it's cracked up to be, Jack."
    mike.say "Sure, girl housemates look better than guys."
    mike.say "But they still do stuff like leaving the dishes for you to wash."
    mike.say "And they dump their dirty laundry around the place too!"
    show jack blush
    "Jack's eyes light up at the mere mention of the word."
    show jack perv at startle
    jack.say "You mean like panties and bras?!?"
    mike.say "Yes...no...I mean..."
    mike.say "Look, can we just focus on playing some videogames?"
    "This seems to have the desired effect on Jack."
    show jack normal
    "He shakes his head, as if resetting his brain."
    "And then he picks up a joypad, sitting down in front of the TV."
    show jack smile
    jack.say "Okay man, okay..."
    jack.say "So what are we playing first?"
    show jack normal
    "Picking up the second joypad, I turn on the Zbox."
    mike.say "I'm in the mood for some retro goodness."
    mike.say "Hyper Plumber Siblings?"
    mike.say "You can be Maria?"
    show jack happy
    jack.say "You're on!"
    "Pretty soon everything else is forgotten as Jack and I lose ourselves in the game."
    "We're stomping on killer mushrooms and turtles, snatching power-ups and generally having a great time."
    "And when I see that my high-score beats Jack's own efforts, I punch the air."
    mike.say "Oh yeah!"
    mike.say "Hail to the king, baby!"
    bree.say "Hail to the king indeed!"
    show jack blush with vpunch
    "Both Jack and I jump at the sound of [bree.name]'s voice."
    "Neither of us knew that she was standing behind us."
    "She must have sneaked back into the room while we were engrossed in the game."
    show bree casual happy at right
    bree.say "A performance like that deserves a reward..."
    hide bree
    show bree kiss casual
    $ bree.flags.kiss += 1
    "Before I can say a word, [bree.name] leans in and kisses me."
    "It's a long, lingering affair, and it leaves me gasping."
    hide bree kiss
    show jack blush at left
    show bree casual normal at right
    with dissolve
    "But when she breaks it off and sits down on the sofa, I see Jack staring in amazement."
    show jack perv
    jack.say "Wha..."
    jack.say "Did she..."
    jack.say "What did I just see?!?"
    show jack blush
    mike.say "Erm..."
    mike.say "It's nothing, Jack..."
    mike.say "Just a little joke [bree.name] and I have going on, you know?"
    "The expression on Jack's face says that he doesn't get it at all."
    "But he nods all the same."
    mike.say "Anyway..."
    mike.say "What shall we play next?"
    show jack smile
    jack.say "Oh...let me think..."
    jack.say "What about Guitar Heroine?"
    "The choice seems a little out of leftfield."
    "But I nod and begin to hunt out the guitar-shaped joypads."
    "Anything to get Jack's mind off the fact that [bree.name] just kissed me in front of him!"
    show bree at startle
    bree.say "Ooh!"
    show bree happy
    bree.say "Sasha loves this game!"
    show bree evil
    bree.say "SASHA...SASHA!"
    show bree normal
    "Jack and I watch as [bree.name] calls Sasha into the sitting room."
    show sasha casual annoyed at mostright5 with moveinright
    sasha.say "Huh?"
    sasha.say "What do you guys want?"
    "Sasha looks a little pissed at being summoned from wherever she was a moment ago."
    "But when she sees the guitar-shaped joypads in our hands, her mood instantly changes for the better."
    show sasha normal
    sasha.say "Oh, cool!"
    show sasha happy
    sasha.say "We haven't busted those things out in ages."
    "She plants her ass on the sofa beside [bree.name]."
    "And I guess we have an audience."
    show sasha normal
    "It's right about then that I see the grin on Jack's face."
    "And I start to understand why he wanted to play this particular game."
    "He knows Sasha's in a band, so it makes sense she'd be into it."
    "Jack's trying to impress her with his talent for the game!"
    "Well, that's not going to make me go easy on him."
    "The game starts, and for a moment in time, Jack and I are transformed into rock gods!"
    "We duel each other with the guitar-shaped joypads, shredding and riffing like our lived depend on it."
    "More than once I think that Jack's edged me out this time."
    "But when it's all over, the scores are displayed on the screen."
    show jack smile at startle
    jack.say "WHAT?!?"
    jack.say "You beat me again?!?"
    mike.say "I guess I'm just in the zone today, man!"
    sasha.say "In the zone?"
    show sasha joke
    sasha.say "You're a fucking guitar god!"
    hide sasha
    show sasha kiss casual
    $ sasha.flags.kiss += 1
    "Before I know what's happening, Sasha's got her arms around me."
    "And then she's sticking her tongue down my throat!"
    "Jack stares at what's happening."
    "His eyes are wide and his mouth is hanging open."
    hide sasha kiss
    show jack perv at left
    show bree normal at right
    show sasha casual normal at right4
    with dissolve
    jack.say "Did she just..."
    jack.say "Like the other one did..."
    mike.say "Ah..."
    mike.say "Sasha's joking around too, Jack!"
    mike.say "I'm sure she'd have kissed you if you'd won..."
    "Jack watches as Sasha walks back over to the sofa."
    "She clearly heard my hasty explanation for her actions."
    "And I can see that she's making sure not to give Jack any clear hint that it's the truth or not."
    if Person.is_not_hidden("minami") and Room.has_tag(minami.room, "home") and minami.flags.kiss > 0:
        scene bg black with timelaps
        scene bg livingroom
        show jack at left
        with timelaps
        pause 0.1
        show minami casual happy at mostright5 with moveinright
        minami.say "Ooh..."
        minami.say "Videogames - so cool!"
        "At the sound of Minami's voice, I see Jack's attention shift in her direction."
        "And I follow his gaze, pleased to have her walk into the room and distract him."
        "Yeah, I know that Jack's looking at her in the same way he looks at the other girls."
        "But it's almost like she was designed to turn guys like him into a helpless puddle of goo!"
        show jack smile
        jack.say "H...hi, Minami!"
        minami.say "Oh...hi, Jack!"
        show minami normal
        minami.say "You mind if I watch you boys play?"
        "Jack shakes his head, falling over himself to please Minami."
        jack.say "Sure thing, Minami!"
        jack.say "I'd do anything for you..."
        jack.say "I...I mean, yeah - that's cool!"
        mike.say "So..."
        mike.say "What are we going to play next?"
        jack.say "Huh?"
        jack.say "Oh...oh yeah..."
        jack.say "I know, let's play Luna Mariner!"
        show jack normal
        "I can't help smirking at Jack's choice."
        "A game featuring Japanese girls in short skirts."
        "I mean, could he be any more obvious?"
        "But I don't call him on it, and instead just set up the game."
        minami.say "Oh wow!"
        show minami happy
        minami.say "I love this anime!"
        minami.say "I've cosplayed almost all of the characters!"
        show minami blush
        "Jack's eyes are almost out on stalks as he processes this information."
        "And as the game gets started, I can tell that his head is still turning it over."
        "Because he's certainly not concentrating on playing, and I trounce him with ease."
        show jack smile
        jack.say "What the hell?!?"
        jack.say "Are you kidding me?"
        mike.say "Sorry, Jack - you snooze you lose!"
        show minami tehe
        minami.say "And if you win, you get a prize!"
        "Minami skips over to my side and leans in close."
        hide minami
        show minami kiss casual
        $ minami.flags.kiss += 1
        "Then she treats me to a long, lingering kiss!"
        "Once it's over, I can see that Jack's more shocked than ever."
        hide minami kiss
        show minami casual normal
        hide minami with moveoutright
        mike.say "Ah...yeah..."
        mike.say "That's kind of how we celebrate back home!"
    if Person.is_not_hidden("lexi") and Room.has_tag(lexi.room, "home") and lexi.flags.kiss > 0:
        scene bg black with timelaps
        scene bg livingroom
        show jack at left
        with timelaps
        pause 0.1
        show lexi casual normal at mostright5 with moveinright
        lexi.say "Oh, you guys playing videogames again?"
        lexi.say "Mind if I watch?"
        "At the sound of Lexi's voice, I can't help glancing at Jack."
        "And true to form, he's already staring at her with his tongue hanging out!"
        "Can you really blame him?"
        "Lexi looks hot as fuck, like the perfect bad girl."
        mike.say "Sure, Lexi."
        mike.say "I mean, if that's okay with you, Jack?"
        show jack smile
        jack.say "Of course it is!"
        jack.say "Hey, we should play Futile Fight!"
        show jack normal
        mike.say "Sounds good to me..."
        "I guess seeing Lexi made Jack think of the mean streets."
        "There are even some characters in that game that remind me of Lexi too!"
        "She seems to approve of the choice too, nodding as we start to play."
        lexi.say "Oh yeah...I grew up a neighbourhood like that!"
        lexi.say "And that looks like a guy that stiffed me on some money!"
        lexi.say "You guys beat the living crap out of him for me!"
        "I'm pretty used to the sound of Lexi getting excited."
        "It's a massive turn-on, but I can handle it by now."
        "Unlike Jack, who seems to be getting pretty hot under the collar."
        "Lexi keeps leaping up and throwing punches in the air."
        "And whenever she does, her curvy anatomy moves in very energetic ways."
        "Jack keeps straining to get a look instead of paying attention to the game."
        "Pretty soon this results in me leaving him far behind."
        show jack smile
        jack.say "Ah, shit!"
        jack.say "I can't believe it - you beat me again!"
        mike.say "Don't blame me, Jack."
        mike.say "Your head's not in the game!"
        lexi.say "Oh yeah..."
        show lexi happy
        lexi.say "My hero!"
        hide lexi
        show lexi kiss casual
        $ lexi.flags.kiss += 1
        "Lexi sways over to me and kisses me, sticking her tongue straight down my throat."
        "At the same time she makes a point of squeezing my cock too!"
        "All Jack can do is watch in stunned silence as she almost mounts me."
        hide lexi kiss
        show lexi casual
        hide lexi with moveoutright
    if Person.is_not_hidden("samantha") and Room.has_tag(samantha.room, "home") and samantha.flags.kiss > 0:
        scene bg black with timelaps
        scene bg livingroom
        show jack at left
        with timelaps
        pause 0.1
        show samantha casual normal at mostright5 with moveinright
        samantha.say "Oh..."
        samantha.say "I didn't know you guys were playing videogames!"
        samantha.say "I'll go do something in another room, okay?"
        "Jack and I both turn around at the sound of Sam's voice."
        "And seeing her standing in the doorway, I'm about to nod in agreement."
        "But Jack beats me to it, shaking his head as if his life depends on it."
        jack.say "Oh no..."
        jack.say "No way, Samantha!"
        show jack perv
        jack.say "You can totally come in and watch us play - if you'd like?"
        "Sam smiles one of those sweet smiles that she's famous for."
        "The kind that still make my heart melt even after I've known her so long."
        "So there's no wonder it's having such an effect on Jack right now!"
        "Sam looks at me, raising her eyebrows."
        mike.say "I'm cool with that, Sam."
        mike.say "Come and watch us play with each other..."
        mike.say "I...I mean play videogames!"
        show samantha happy
        "Sam chuckles and shakes her head as she sits down."
        samantha.say "Don't worry, I know what you mean!"
        show jack -perv
        show samantha normal
        "I decide that we're going to play Barmaid Blues."
        "It's a really old game, but I know it's one Sam's aware of."
        "And pretty soon we're into it, Jack and I going head to head."
        "Sam claps happily, offering advice where she thinks we need it."
        "I just nod at this, mostly ignoring her in favour of actually playing the game."
        "But Jack seems to be hanging on her every word."
        "And it's really making him play badly!"
        "Once we're done, Jack's been soundly beaten."
        jack.say "Aw, man!"
        jack.say "I thought I had this one won!"
        mike.say "I guess you just got distracted, Jack."
        show samantha happy
        samantha.say "Well done!"
        "I turn my head to see Sam's face an inch from mine."
        hide samantha
        show samantha kiss casual
        $ samantha.flags.kiss += 1
        "And then she kisses me without waiting for permission."
        "Jack looks on in amazement, even after she's done."
        hide samantha kiss
        show samantha casual
        hide samantha with moveoutright
    scene bg black with timelaps
    scene bg livingroom
    show jack normal
    with timelaps
    "Once we're done gaming, I can see the way Jack's looking at me."
    "He's narrowing his eyes and stealing glances, like he wants to ask something."
    "And finally he plucks up the courage to come out with it."
    show jack smile
    jack.say "You're bullshitting me, aren't you?"
    mike.say "Huh?"
    mike.say "What are you talking about?"
    jack.say "Your housemates, and them all kissing you!"
    jack.say "It's not just some weird celebration you all do together, is it?"
    "I open my mouth, intending to deny it all."
    "But Jack beats me to the punch."
    jack.say "If you don't tell me the truth..."
    jack.say "Then...then I'll ask them myself!"
    "Ah shit - that's the last thing I want!"
    "So I don't see how I have any other choice."
    mike.say "Yeah, Jack..."
    mike.say "I admit it - we're all doing it, okay!"
    mike.say "Are you happy now?"
    show jack blush
    "Jack's eyes almost pop out of his head at my admission."
    "And I honestly think he's going to explode or do something similarly dramatic."
    show jack perv
    jack.say "Of course I'm not happy!"
    jack.say "You're the one screwing all your housemates!"
    jack.say "Why would I be happy about that?!?"
    mike.say "Hey man!"
    mike.say "Don't be like that..."
    mike.say "It's not like I wanted to rub it in your face!"
    jack.say "Well you did!"
    jack.say "And I think I need to go home now."
    hide jack with moveoutright
    "With that, Jack gets up and walks towards the door."
    "All I can do is follow him and try to apologise."
    show bg house
    show jack
    with fade
    "But every time I open my mouth, he holds up a hand to silence me."
    "Then he strides out of the door and away down the street."
    hide jack with dissolve
    "Leaving me shaking my head, as I don't know how to deal with this problem."
    "I don't want to lose an old friend like Jack."
    "But I also don't want to lose what I have with my housemates either."
    "Urgh...this is going to take some serious thought to work out."
    return

label jack_nude_beach:
    show jack normal
    "The moment that I set eyes on him, I can tell that Jack's bursting to tell me something."
    "He's doing that thing where he's trying to pick his moment so it makes a serious impression on me."
    "But that also means that he's hardly paying attention to anything else that we're talking about."
    "And to be honest, it's getting more than a little annoying!"
    "So I decide to burst his bubble and make him tell me his news."
    mike.say "Jack, just come out with it already!"
    jack.say "Huh?"
    jack.say "What do you mean?"
    "I roll my eyes and shake my head at this."
    mike.say "Come on, Jack!"
    mike.say "You're all but dancing on the spot!"
    mike.say "That means you've got something to tell me."
    mike.say "Something you think is so cool it'll blow my mind!"
    "For a moment Jack looks like he's going to try and keep up the pretence."
    "But then he sags a little and lets out a sigh that signals defeat."
    jack.say "Okay, okay..."
    jack.say "You got me."
    jack.say "But this really is something super cool!"
    "And just like that, his mood changes again."
    "The sullen disappointment at being found out disappears."
    show jack happy
    "Instead Jack becomes enthusiastic and animated once again."
    jack.say "You're not going to believe what's opening up near here, man!"
    jack.say "Trust me, you're going to freak out the moment I tell you!"
    mike.say "Well, none of that's going to happen unless you actually tell me, Jack!"
    mike.say "Come on, enough beating about the bush - spit it out already!"
    "Jack holds up a hand to show that he understands."
    jack.say "Okay, yeah, okay..."
    jack.say "Here it is..."
    jack.say "They're opening a beach!"
    "I wrinkle up my face, looking at him with a puzzled expression."
    mike.say "So what?!?"
    mike.say "There are miles of beach around here!"
    "Jack looks at me like I'm speaking a foreign language for a moment."
    "But then he shakes his head, realising he left something out."
    jack.say "Sorry, man!"
    jack.say "This whole thing's got my head all twisted up."
    show jack perv
    jack.say "I meant to say it's a NUDIST beach!"
    "Even now that he's said it out loud, the news still doesn't sink in."
    "It's like I know what all the words mean, but they don't fit together at first."
    "All I can do is blink stupidly as Jack grins at me like a fool."
    mike.say "You mean..."
    jack.say "Yes, I do!"
    mike.say "Nudist as in..."
    jack.say "I certainly do!"
    mike.say "With no clothes on at all..."
    jack.say "Now do you see why I'm so excited?!?"
    "Suddenly everything seems to click into place for me."
    "And it's like waking up from a dream to see a beautiful sunrise."
    mike.say "We're getting a nudist beach!"
    jack.say "You bet we are!"
    mike.say "Wow...just, wow!"
    jack.say "I know, man - we have to start planning for this right away!"
    jack.say "We need to scout the location, pick out the best spots!"
    "It's only as Jack babbles on that I start to wonder about the nudist beach."
    "Part of me is honestly excited about the prospect of seeing what's on show."
    "Yet there's also a smaller part of me that's a little worried about being on show too!"
    "But I try as best I can to push that second part of me aside and be positive."
    "This could be the start of a whole new adventure!"
    $ game.flags.nudistBeach = True
    return
