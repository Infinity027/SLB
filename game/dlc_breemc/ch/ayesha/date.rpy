label ayesha_after_dance_success_with_female:
    show ayesha blush
    "The moment I finish dancing, I look up to see Ayesha hurrying over."
    "She has a look of amazement on her face, like she's seen something astonishing."
    "And I'm already flattering myself by imagining that it's my dancing."
    ayesha.say "[hero.name]..."
    ayesha.say "Why didn't you tell me you could do that?"
    show ayesha happy
    "Doing the best I can to play the innocent, I look around."
    "And the I direct my attention back to Ayesha."
    bree.say "Do what, Ayesha?"
    bree.say "That was just be dancing, nothing special!"
    show ayesha a joke
    "Ayesha crosses her arms over her chest and gives me a hard stare."
    "All of which I guess is supposed to tell me that she's not taken in."
    show ayesha happy
    ayesha.say "Cut it out, [hero.name]..."
    ayesha.say "Fake modesty is just as bad as having a big head!"
    show ayesha normal
    bree.say "Okay, okay..."
    bree.say "I admit it, I can dance!"
    bree.say "There, are you happy now?"
    show ayesha joke
    ayesha.say "No I'm not!"
    show ayesha happy
    ayesha.say "And I won't be until you teach me some of those moves."
    show ayesha normal
    return

label ayesha_after_dance_failure_with_female:
    show ayesha sad
    "I can already see the look on Ayesha's face as I stop dancing."
    "And the pain that's written all over it is pretty plain to see."
    "Mainly thanks to the fact that I'm feeling the same thing myself right now."
    "So much so that I almost think about not saying a single word."
    "Maybe if I don't mention it, then Ayesha will be relieved."
    "Because it already looks like I embarrassed the hell out of her!"
    show ayesha surprised
    ayesha.say "Ah, yeah..."
    ayesha.say "That was an interesting dance, [hero.name]!"
    show ayesha sad
    "All I can do is wince and shrug my shoulders."
    "As every word Ayesha speaks feels like a stab in the gut."
    bree.say "It wasn't really that bad, was it?"
    bree.say "Surely not?"
    show ayesha normal
    "I'm waiting for Ayesha to leap to my defence."
    "Or at least to tell me that it doesn't matter all that much."
    show ayesha joke
    ayesha.say "Oh, I might have seen a couple that were worse."
    ayesha.say "But it's definitely up there in the top five worst!"
    show ayesha happy
    "I manage to nod and smile."
    "All the while feeling like I'm dying on the inside."
    "And making a promise to myself that I'll never dance in front of Ayesha again."
    show ayesha normal
    return

label ayesha_date_intro_halloween_female:
    bree.say "Hey, Ayesha - you look great tonight!"
    "Ayesha blushes and smiles at my compliment."
    ayesha.say "Thanks, [hero.name] - you too."
    ayesha.say "I'm pretty excited about tonight."
    ayesha.say "I don't think I ever went on a Halloween date before!"
    "At the mention of Halloween, I slap my forehead."
    bree.say "It's Halloween, and I totally forgot!"
    bree.say "We should have gotten dressed up for the occasion."
    "Ayesha shakes her head at this."
    ayesha.say "Oh no, [hero.name] - I only dress up in strange costumes when I wrestle."
    return

label ayesha_halloween_invitation_female:
    show ayesha
    "Almost the moment I agreed to the Halloween party, I knew who I wanted to invite."
    "Ayesha's the only person that fits the bill, the only one I know I'll have fun with."
    "But the problem is that I've noticed she has a few little issues with socialising."
    "Well, when she's not actually in the wrestling ring, that is."
    "Which sounds kind of contradictory, I know."
    "But I guess people are just quirky like that and you have to work around it."
    "Maybe if I sell it to her as a costume party, that'll make a difference?"
    "Kind of link it back to her wearing a costume when she wrestles?"
    "There's only one way to find out..."
    show ayesha at center, zoomAt(1.5, (640, 1040)) with fade
    bree.say "Hey, Ayesha..."
    bree.say "Have you made any plans for Halloween yet?"
    "At the mere mention of the holiday, Ayesha's mood seems to change."
    show ayesha sad
    "She looks down at her feet, like she's embarrassed to talk about it."
    show ayesha whining
    ayesha.say "Oh..."
    ayesha.say "No, [hero.name]."
    ayesha.say "I don't normally do anything on Halloween."
    ayesha.say "I don't even open my door to trick or treaters."
    show ayesha sad
    "I can't help frowning at the admission."
    "It just sounds so strange."
    bree.say "Huh?"
    bree.say "Why's that?"
    show ayesha whining
    ayesha.say "Well..."
    ayesha.say "I once scared a little girl so much she cried."
    ayesha.say "I think she thought I was a giant or an ogre, or something like that!"
    show ayesha sadsmile
    bree.say "Then I have the perfect solution!"
    bree.say "We're having a party, and you should come too."
    bree.say "Plus it's a costume party, so you can go crazy with your outfit!"
    show ayesha normal
    if ayesha.love >= 100:

        "Ayesha seems to weigh up the proposition for a couple of seconds."
        "And while that's happening, I try to guess what she's thinking."
        "But nothing about her expression gives me a clue."
        ayesha.say "Hmm..."
        show ayesha talkative
        ayesha.say "I normally stay at home on Halloween."
        ayesha.say "It's become kind of a tradition for me."
        show ayesha curious
        "I can already feel my mood beginning to turn sour."
        "But I do all that I can to keep on smiling all the same."
        bree.say "Oh..."
        bree.say "Okay, Ayesha..."
        show ayesha talkative
        ayesha.say "But the party's at your place, right?"
        ayesha.say "So technically I'd still be staying home."
        ayesha.say "Just at somebody else's home."
        show ayesha normal
        "I can't say that I follow the logic of what Ayesha just said."
        "But it means that she'll be coming to the party."
        "So that hardly matters."
        bree.say "Sure thing, Ayesha!"
        bree.say "So you'll come?"
        $ ayesha.love += 1
        show ayesha happy
        ayesha.say "I will."
        ayesha.say "And I'd better start working on my costume too!"
        $ game.flags.halloween_girl = 'ayesha'
    else:

        "Ayesha seems to weigh up the proposition for a couple of seconds."
        "And while that's happening, I try to guess what she's thinking."
        "But nothing about her expression gives me a clue."
        ayesha.say "Hmm..."
        show ayesha talkative
        ayesha.say "I normally stay at home on Halloween."
        ayesha.say "It's become kind of a tradition for me."
        show ayesha normal
        "I can already feel my mood beginning to turn sour."
        "But I do all that I can to keep on smiling all the same."
        bree.say "Oh..."
        bree.say "Okay, Ayesha..."
        show ayesha whining
        ayesha.say "I'm sorry, [hero.name]..."
        ayesha.say "Your party really sounds like a lot of fun."
        ayesha.say "But I'm not ready to break that tradition yet."
        show ayesha sad
        "I can't say that I follow the logic of what Ayesha just said."
        "But I make a point of nodding all the same."
        bree.say "I understand."
        bree.say "You gotta do what you gotta do."
    hide ayesha with fade
    return

label ayesha_halloween_arrival_female:
    scene bg house
    "I open the door, expecting to see Ayesha standing there."
    show ayesha halloween upset
    "Instead I'm greeted by a huge figure, filling the doorway."
    "It's shadow covers me, and I can almost feel myself quaking."
    show ayesha angry
    ayesha.say "Kneel before the prophet of the Great Kraken!"
    show ayesha upset
    "I don't hesitate to do as I'm told."
    with vpunch
    "Getting down on my knees in the hope of being shown mercy."
    show ayesha surprised at center, zoomAt(1.5, (640, 1040))
    "But then the giant leans forwards."
    show ayesha halloween sad
    "And it's expression goes from ferocious to worried."
    show ayesha whining
    ayesha.say "Ah, [hero.name]..."
    ayesha.say "You don't actually have to do it!"
    show ayesha sad
    bree.say "Ayesha?"
    bree.say "Oh...my...goddess!"
    bree.say "Is that you?!?"
    "Ayesha looks down at me with her massive icon hoisted on her shoulder."
    "The costume is perfect, she looks just like the priestess in the game."
    show ayesha sadsmile
    "With the spell broken, Ayesha starts to look a little embarrassed."
    "She looks around, like she's afraid of being seen in her costume."
    show ayesha whining
    ayesha.say "I...I almost didn't come as Illaoi."
    show ayesha talkative
    ayesha.say "But she's my favourite character in the game!"
    ayesha.say "And now I'm staring to wonder if I made the right choice..."
    show ayesha normal
    menu:
        "Compliment":
            with vpunch
            "Getting back to my feet, I shake my head."
            "Keen to allay Ayesha's fears."
            bree.say "It doesn't matter what people think, Ayesha."
            bree.say "If you like it, that's all that matters."
            bree.say "And just for the record, I think you look divine!"
            bree.say "Ooh...sorry about the pun."
            show ayesha blush
            $ ayesha.love += 1
            "Ayesha really is looking embarrassed now."
            "Blushing as I compliment her."
            ayesha.say "Stop it, [hero.name]!"
            show ayesha happy
            ayesha.say "Actually, don't stop it!"
            ayesha.say "You really like my costume?"
            show ayesha sadsmile
            "I nod."
            bree.say "Of course I do, Ayesha."
            bree.say "You've made her my favourite character too!"
        "Criticize":
            "Well, she is kind of asking for it, isn't she?"
            "Ayesha's the tallest and most muscular girl I know."
            "And dressing up like Illaoi makes that even more obvious."
            bree.say "It's not exactly subtle, Ayesha!"
            bree.say "People are going to be staring at you all night."
            $ ayesha.love -= 2
            show ayesha sad
            "Ayesha looks hurt by my answer."
            "She looks down at her feet, frowning."
            show ayesha whining
            ayesha.say "You didn't have to come right out and say it, [hero.name]."
            ayesha.say "Maybe you could have spared my feelings - just a little?"
            show ayesha sad
            "I feel a flush of annoyance as Ayesha says all of this."
            "I've worked so hard to make this party a thing."
            "And I don't need to be guilt-tripped right now."
            bree.say "We're throwing a party, Ayesha."
            bree.say "So maybe try to lighten up a little?"
            show ayesha annoyed
            "Ayesha curls her lip, clearly not happy with me."
            "But she still walks into the house and lets me close the door."
            "Maybe I'll try to be nicer to her from now on."
            "After all, I don't want to be smited by her righteous fury!"
    scene bg black with dissolve
    $ renpy.pause(1)
    return

label ayesha_halloween_party_female:
    $ game.pass_time(2)
    scene bg livingroom
    with dissolve
    ayesha.say "Back, foul heathen!"
    ayesha.say "Back I say!"
    ayesha.say "If I like something I take it, if I hate something I break it."
    ayesha.say "In the name of the Great Kraken, I smite thee!"
    "I recognise the sound of Ayesha's voice as soon as I hear it."
    "And at first I think she's just playing up to her costume."
    show ayesha a halloween upset at center, zoomAt(1.25, (900, 880))
    show jack halloween embarrassed at center, zoomAt(1.25, (380, 900))
    with fade
    "But then I see that she has the huge icon that she carries held before her."
    "That and the fact that Jack's pretty much cowering before her!"
    show jack lying
    jack.say "Smited by Illaoi!"
    jack.say "Wow - what a way to go!"
    jack.say "I want that written on my tombstone!"
    show jack embarrassed
    "I hurry over as quickly as I can."
    show ayesha a upset at center, zoomAt(1.25, (960, 880))
    show jack normal at center, zoomAt(1.25, (320, 900))
    "Determined to put myself between Jack and Ayesha's massive weapon."
    menu:
        "Defend Ayesha":
            bree.say "Whoa, whoa..."
            bree.say "What's going on, Ayesha?!?"
            bree.say "What did he do to you?"
            show ayesha b annoyed
            "Ayesha lowers the blunt object."
            "But she keeps one eye on Jack all the same."
            show ayesha angry
            ayesha.say "The little creep pinched my ass!"
            show ayesha upset
            show jack whining
            jack.say "It was only a little pinch."
            jack.say "I couldn't help it - I was hypnotised!"
            show jack sad
            "I turn to face Jack, frowning at his excuses."
            bree.say "You creep!"
            bree.say "You're lucky she didn't bash your brains out!"
            bree.say "Ayesha here could tie you up in knots without breaking a sweat."
            "That last comment was meant to scare Jack."
            show jack perv
            "But instead I see his eyes light up at the prospect."
            jack.say "She's welcome to try that on me anytime!"
            "Without thinking, I grab the icon out of Ayesha's hands."
            $ jack.love -= 1
            show jack halloween surprised
            "And then I use it to threaten Jack myself."
            "He lets out a yelp and scuttles off."
            hide jack
            show ayesha sad at center
            with easeoutleft
            "Which leaves Ayesha and me alone."
            show ayesha talkative
            ayesha.say "You wouldn't really have hit him, would you?"
            show ayesha normal
            bree.say "I could ask you the same question, Ayesha!"
            $ ayesha.love += 2
            show ayesha happy
            "Ayesha chuckles and shakes her head."
            "She leans to take the icon back and whispers in my ear."
            show ayesha joke
            ayesha.say "You can touch my ass all you like, [hero.name]."
            ayesha.say "And I promise you'll enjoy me tying you up in knots too!"
        "Defend Jack":
            bree.say "Whoa, whoa..."
            bree.say "What's going on, Ayesha?!?"
            bree.say "You're not going to use that thing on him, are you?"
            show ayesha b upset
            "Ayesha glowers at me, clearly still angry."
            "But she lowers the blunt object all the same."
            show ayesha b angry
            ayesha.say "I should brain him with it."
            ayesha.say "The little creep pinched my ass!"
            show ayesha upset
            show jack whining
            jack.say "It was only a little pinch."
            jack.say "I couldn't help it - I was hypnotised!"
            show jack sad
            bree.say "You could have just told me, Ayesha."
            bree.say "I'd have made sure it never happened again."
            $ ayesha.love -= 2
            hide jack
            show ayesha blush at center
            with easeoutleft
            "Jack takes the chance to slip away while I talk to Ayesha."
            "And she hardly seems to notice him leave."
            "She's too busy looking embarrassed and a little ashamed of herself."
            ayesha.say "I...I'm sorry, [hero.name]."
            ayesha.say "I didn't think!"
            bree.say "Well, try to do that next time, okay?"
    scene bg black with dissolve
    $ renpy.pause(1)
    return

label ayesha_halloween_dance_female:
    $ game.pass_time(2)
    scene bg livingroom
    show ayesha halloween
    with dissolve
    "Ayesha's looking over at the dancefloor all night."
    "She glances over and then looks back at me too."
    "But whenever I catch her doing it, turns away pretty quickly."
    "I can see her cheeks flushing too, like she's embarrassed."
    "It takes me a while to get my head around what's going on."
    "But then I think I actually figure it out."
    "Ayesha must want to dance, but she's not asking me."
    "So I guess she's waiting for me to do the asking."
    bree.say "Hey, Ayesha..."
    bree.say "Do you want to dance with me?"
    show ayesha blush
    "I thought that asking the question would be all it took."
    "But Ayesha just seems to look even more embarrassed than before."
    ayesha.say "I...I don't know, [hero.name]..."
    ayesha.say "I guess we could..."
    ayesha.say "If you really want to?"
    menu:
        "Dance":
            "I'm still kind of puzzled by how Ayesha's behaving."
            "But I figure that means I need to step up and take the lead."
            "So I give her a smile and take hold of her hand."
            bree.say "Yeah, Ayesha - it's what I want."
            bree.say "So let's go dance!"
            show dance ayesha halloween with fade
            "Ayesha follows behind me as I lead her out there."
            "Which must look a little strange, as she's so much taller than me!"
            "She looks nervous the whole time, glancing this way and that."
            "So I do the best I can to keep her eyes on me."
            "But it doesn't seem to have the desired effect."
            "Because Ayesha stays stiff and awkward the whole time."
            "And she makes her excuses to leave the dancefloor as soon as the song is over."
            hide dance
            show ayesha halloween upset
            $ ayesha.love -= 2
            "I follow her this time, thinking I just made a mistake."
        "Do not dance":
            "I'm still kind of puzzled by how Ayesha's behaving."
            "But she just doesn't seem to be ready to take that next step."
            "So the best thing I can think of is not to push her into it."
            bree.say "Not if it's not what YOU want, Ayesha."
            bree.say "And I don't think it is."
            bree.say "Am I right?"
            show ayesha happy
            "Now I see a real change in Ayesha's expression."
            "Suddenly she looks genuinely relieved."
            "Like a weight's been lifted off of her shoulders."
            show ayesha happy
            ayesha.say "I always feel self-conscious when I dance."
            ayesha.say "And being all dressed up like this makes it worse!"
            show ayesha normal
            bree.say "No problem, Ayesha."
            bree.say "Forget about dancing."
            bree.say "Let's just grab another drink instead."
            $ ayesha.love += 2
            "Ayesha nods and smiles at this."
            "And I feel like I made the right decision."
    scene bg black with dissolve
    $ renpy.pause(1)
    return

label ayesha_halloween_sex_female:
    scene bg livingroom
    show ayesha halloween
    with dissolve
    "I've really tried to think about something other than Ayesha all night."
    "But the costume she's wearing makes her look even better than normal."
    "I did the best I could not to get caught stealing glances at her."
    "But whenever Ayesha catches me looking, she gives me a smile right back."
    "At first I thought it was just her being happy to be the centre of my attention."
    "But then I realised just how much punch she's been downing over the course of the night."
    scene bg secondfloor
    show ayesha halloween at center, zoomAt(1.5, (640, 1040))
    with fade
    "And so by the time the party is coming to an end, I'm dealing with a rather drunk Amazon!"
    show ayesha talkative
    ayesha.say "Come here, puny girlthing!"
    ayesha.say "Let me grab you and take you!"
    show ayesha happy
    "Ayesha grabs hold of me with one hand, opening the door to my room with the other."
    scene bg bedroom4
    with hpunch
    "The next thing I know, she's tossing me inside without any perceivable effort."
    play sound door_slam
    show ayesha a halloween flirt
    with hpunch
    "Then she slams the door behind her, crossing her arms over her chest."
    bree.say "Erm..."
    bree.say "Are you feeling okay, Ayesha?"
    bree.say "Your breath smells like I could light it on fire!"
    show ayesha at center, zoomAt(2.0, (640, 1340))
    "Ayesha strides over to me and stops when we're almost nose to nose."
    "And by that I mean she leans down to address the height difference."
    "Then, without even stopping to ask permission, she starts tearing off my clothes."
    bree.say "Huh..."
    bree.say "Ayesha..."
    bree.say "What are you doing?!?"
    "Ayesha doesn't even look up from what she's doing."
    "Instead her pace quickens as she removes more of my clothes."
    show ayesha angry
    ayesha.say "Silence your prattle, girlthing."
    ayesha.say "I have needs that must be satisfied!"
    show ayesha upset
    "Suddenly I find myself totally naked."
    "Ayesha stands back, nodding as she admires her work."
    show ayesha happy
    ayesha.say "You will do - for now!"
    show ayesha normal
    "Before I can protest, Ayesha places her hand flat on my chest."
    "And then she shoves me backwards, sending me sprawling onto the bed."
    "It's only when I hit the mattress that my thoughts seem to clear."
    "Ayesha hasn't taken a blow to the head and regressed to the mentality of cavewoman."
    "She's just managed to down enough alcohol to bypass her usual inhibitions."
    "And now she's playing out the character that she came to the party dressed as."
    "That means I have maybe two choices here."
    "I can go along with it and let her have her way."
    "Or I can step up to the challenge and give as good as I get."
    "I make my choice as soon as Ayesha lowers herself onto the bed."
    "She tries to lie down atop me, pinning me to the mattress."
    "But I manage to slip out from beneath her at the last moment."
    "Normally, Ayesha's reactions are pretty fast."
    "But I have the booze to thank for making her a little sluggish."
    play sound bed_jump
    show ayesha stuned with vpunch
    "She hits the bedclothes, then looks up in surprise, turning onto her back."
    show ayesha surprised
    ayesha.say "Girlthing!"
    ayesha.say "Where did you go?!?"
    show ayesha stuned
    "I take this as my opportunity to pounce on Ayesha."
    scene bg black
    show ayesha fingering halloween mc_naked
    with vpunch
    "She lets out a cry of alarm as I land on her."
    "But I notice that her efforts to throw me off are less than effective."
    "For all that Ayesha makes a show of it, I see that she's not really trying."
    "Which tells me that she's actually enjoying the experience!"
    "I hastily start to tear at Ayesha's costume."
    "And from there it doesn't take me long to peel it off her shoulders"
    show ayesha fingering naked tattoo with fade
    ayesha.say "Oh..."
    ayesha.say "Girlthing - I am at your mercy!"
    "I'm already excited from being manhandled by Ayesha."
    "And so I don't even think about what I do next."
    "I aim my head between Ayesha's exposed breasts."
    "Then I dive forwards, landing right in the middle of them."
    ayesha.say "Mmm..."
    ayesha.say "I am at your mercy..."
    ayesha.say "I am in your power..."
    ayesha.say "Do with me as you will!"
    "I don't need to be told what to do next."
    "Parting my lips, I begin to nuzzle away at Ayesha's breasts."
    "If I don't have a nipple in my mouth then it's between my fingers."
    show ayesha fingering tattoo at stepback(speed=0.05, h=10, v=-5)
    "And I'm squeezing it for all I'm worth."
    "There are no more words from Ayesha now."
    "Instead she moans and gasps beneath me."
    "Where before she was the one dominating me, now she succumbs totally."
    "That is until I feel her reaching down, putting a hand between my thighs."
    show ayesha fingering at stepback(speed=0.05, h=10, v=-5)
    "A second later, Ayesha starts to stroke away at my pussy."
    "And now it's my turn to moan as I keep on working her nipples."
    "Ayesha knows exactly what she's doing down there."
    show ayesha fingering at stepback(speed=0.05, h=10, v=-5)
    "So there's not a thing I can do to resist her efforts."
    "Ayesha looks down at me, her face begging for more of the same."
    "I try as best I can to give her what she wants."
    show ayesha fingering at stepback(speed=0.05, h=10, v=-5)
    "The last reserves of energy that I have go into my efforts."
    "Ayesha nods desperately as I push myself to the limit for her."
    show ayesha fingering at stepback(speed=0.05, h=10, v=-5)
    "And she begins to let out cries of sheer pleasure."
    "I don't know if it's me coming to the end of my endurance."
    show ayesha fingering at stepback(speed=0.05, h=10, v=-5)
    "Or else the feeling of Ayesha beginning to cum beneath me."
    "But either way I can't keep this up any longer."
    show ayesha fingering at stepback(speed=0.05, h=10, v=-5)
    "At the very last moment, I let go of Ayesha's breasts."
    show ayesha fingering ahegao at stepback(speed=0.05, h=10, v=-5)
    "She gasps in surprise, but before she can object, it happens."
    show ayesha fingering squirt with hpunch
    "Ayesha let's out a deep moan, vocalising her orgasm."
    with hpunch
    "And I cum too, wriggling and writhing atop her."
    show ayesha fingering -squirt with hpunch
    "Then I slump down onto the bed beside her."
    show ayesha fingering normal
    "Neither of us seems able to move."
    "So there we stay, panting and slick with sweat."
    $ ayesha.sexperience += 1
    $ game.pass_time(1)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
