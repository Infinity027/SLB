label ryan_after_dance_success_with_female:
    show ryan normal
    "I can see that Ryan's got a smile on his face even before I'm done dancing."
    "And the strangest thing of all is that from here at least, it looks genuine!"
    "Which is strange when I'm so used to him being snarky and superior all the time."
    bree.say "Hey, Ryan..."
    bree.say "Are you feeling okay?"
    "Ryan raises an eyebrow at this."
    "Like he's more than a little confused."
    show ryan smile
    ryan.say "Of course I am, [hero.name]..."
    ryan.say "Why wouldn't I be?"
    show ryan normal
    "I shrug at this."
    bree.say "I dunno..."
    bree.say "Maybe I thought you were going to say something mean about my dancing?"
    "Ryan chuckles and shakes his head."
    show ryan smile
    ryan.say "Oh, [hero.name]..."
    ryan.say "You couldn't be further from the truth."
    ryan.say "Your dancing is great, really very good."
    "I blink in sheer amazement."
    "Almost stunned by the honest nature of the compliment."
    bree.say "You really mean that?"
    show ryan smile
    ryan.say "Of course I do."
    ryan.say "You're almost good enough to be seen dancing with me!"
    return

label ryan_after_dance_failure_with_female:
    show ryan sad
    "I can see that Ryan's got a smirking look on his face even before I'm done dancing."
    "And so I walk over to where he's standing expecting to experience his usual snarkiness."
    "But what I'm not prepared for is the way that he starts laughing before I even reach him."
    bree.say "Hey!"
    bree.say "What are you laughing at?"
    "Ryan raises an eyebrow."
    "And then he shakes his head."
    show ryan angry
    ryan.say "You really need me to tell you that?"
    ryan.say "After you spent all that time jerking around out there?"
    show ryan sad
    "I can't help feeling wounded by what Ryan's saying."
    "Not least because I was sure that my dancing was pretty good."
    bree.say "Do you have to be so mean?"
    bree.say "I was just dancing, that's all."
    bree.say "And isn't it supposed to be about having fun?"
    "Ryan chuckles and shakes his head."
    show ryan angry
    ryan.say "Oh, [hero.name]..."
    ryan.say "That's just what people with no rhythm tell themselves!"
    ryan.say "What you need to do is take lessons and get good."
    ryan.say "That or quit dancing altogether."
    show ryan normal
    return

label ryan_halloween_invitation_female:
    show ryan
    "Almost the moment I agreed to the Halloween party, I knew who I wanted to invite."
    "I know that [mike.name]'s always telling me how much of a jerk the guy can be."
    "And sure, sometimes he can come off as more than a little arrogant."
    "But I'm still intrigued by Ryan and I want to get to know him better."
    "So the Halloween party strikes me as a great chance to make that happen."
    "The only problem is that it's happening at the house where he used to live."
    "And my guess is that Ryan's going to have a lot of emotional baggage tied to it."
    "So I'm just going to have to try extra hard to convince him it's going to be super fun."
    "So much fun that he'll just have to come along for fear of missing out."
    show ryan at center, zoomAt(1.5, (640, 1040)) with fade
    bree.say "Hey, Ryan..."
    bree.say "I don't suppose you've got plans for Halloween?"
    bree.say "You know, that you're looking for something to do on the actual night?"
    show ryan blank
    "Ryan turns to regard me with one of his questioning looks."
    "The kind that automatically makes you think that you just said something totally dumb."
    show ryan normal
    ryan.say "Plans for Halloween?"
    ryan.say "Oh please, [hero.name]..."
    ryan.say "You sound like you're going to ask me to come trick or treating with you!"
    "Okay, okay...I admit that I see now how this guy can be a total jerk."
    "But that doesn't mean there's not a nicer version of him underneath all that."
    "And he's handsome enough to make digging for it worth the effort too."
    bree.say "Of course not, Ryan!"
    bree.say "We're throwing a Halloween party at the house."
    bree.say "And I wondered if you'd like to come?"
    bree.say "You know...as my guest?"
    "The mention of a party seems to pique Ryan's interest."
    "And now he's paying more attention to me than before."
    show ryan smile
    ryan.say "A Halloween party at the house?"
    ryan.say "Well why didn't you say so, [hero.name]?"
    ryan.say "You should have seen the parties that Sam and I used to throw when we lived there."
    show ryan normal
    ryan.say "Well, I say we...most of it was down to yours truly, of course!"
    ryan.say "Sam and poor old [mike.name] used to mainly get under my feet."
    "I can feel my brows furrowing as Ryan starts talking about himself."
    "Somehow he always seems to be able to do that, no matter the subject of the conversation."
    "Before you know it, you're listening to him explaining how he's the centre of everything."
    "So maybe the way to get him to do what I want is to flatter that massive ego of his?"
    bree.say "Well why don't you come along and see how [mike.name], Sasha and I manage it?"
    bree.say "If things go well, we'll probably do one next year too."
    bree.say "And we could use your feedback to make it even better."
    if ryan.love >= 100:
        "Ryan rest his elbow on one hand and strokes his chin with the other."
        "And I can see that he's considering what I've said pretty deeply."
        "So I wait with baited breath to hear what his answer's going to be."
        show ryan smile
        ryan.say "Hmm..."
        ryan.say "You know it's really mature of you to acknowledge your shortcomings, [hero.name]."
        ryan.say "And to be able to humbly ask someone with more experience, like me, for help."
        ryan.say "So I'll do you a favour and agree to come along to the party for a while."
        show ryan normal
        "I'm so eager to get Ryan to say yes that I kind of filter out all of his condescension."
        "And instead I focus on he fact that he's actually agreed to come."
        bree.say "Oh, that's great news, Ryan..."
        bree.say "I'm sure Sasha and [mike.name] will be happy to hear you're coming."
        ryan.say "Well, [mike.name]y-Boy sure will."
        ryan.say "He's pretty much hopeless without me to tell him what to do!"
        bree.say "Erm...yeah..."
        bree.say "That sounds like [mike.name] alright!"
        bree.say "Oh, it's a costume party, of course..."
        bree.say "So you'll want to get yourself one too."
        "Ryan nods and does that thing where someone points their fingers at you."
        "You know, like they're firing a pair of pistols in your general direction?"
        show ryan smile
        ryan.say "Don't worry, [hero.name]..."
        ryan.say "My Halloween costumes are totally legendary!"
        show ryan normal
        bree.say "Yeah..."
        bree.say "I kinda thought they might be."
        $ game.flags.halloween_girl = "ryan"
    else:
        "Ryan rest his elbow on one hand and strokes his chin with the other."
        "And I can see that he's considering what I've said pretty deeply."
        "So I wait with baited breath to hear what his answer's going to be."
        ryan.say "Hmm..."
        ryan.say "You know, it really sounds like you guys could use my help."
        show ryan annoyed
        ryan.say "But I already made plans for Halloween night."
        ryan.say "So your loss is someone else's gain."
        show ryan normal
        "I feel my spirits sink as Ryan turns down the invitation."
        "Feeling like I went to all that trouble for nothing."
        bree.say "Are you sure?"
        bree.say "You couldn't like, just call in for a while?"
        "Ryan shakes his head."
        show ryan smile
        ryan.say "Sorry, [hero.name] - I'm an all or nothing kind of guy."
        ryan.say "Half-measures just aren't my style."
        show ryan normal
        "Ryan nods and does that thing where someone points their fingers at you."
        "You know, like they're firing a pair of pistols in your general direction?"
        ryan.say "Don't worry, [hero.name]..."
        ryan.say "Just don't go telling anyone I was supposed to be there."
        ryan.say "Then they won't be disappointed by how lame the party is without me!"
    return

label ryan_halloween_arrival_female:
    scene bg livingroom
    pause 1.0
    play sound door_bell
    "I'm kind of being pulled in multiple directions at once when the door-bell rings."
    pause 1.0
    scene bg black with dissolve
    play sound door_open
    scene bg house with wiperight
    pause 1.0
    "Which means that my attention isn't totally focussed on the task at hand when I open it."
    "And so it's a minor miracle that I manage to react to what happens next."
    show ryan halloween smile at center, zoomAt(1.0, (640, 720)) with easeinright
    ryan.say "Hey, [hero.name]..."
    ryan.say "Think quickly!"
    show ryan halloween normal
    "I barely have time to recognise the voice before it's owner whips up his arms."
    "He has his palms upwards and his wrists bared in some kind of weird pose."
    "And then two streamers of something white and stick shoot outwards from them."
    with vpunch
    bree.say "Wha..."
    bree.say "Aargh!"
    "I instinctively crouch down, throwing my hands over my head."
    "And luckily for me, the twin streamers of mysterious white stuff shoot overhead."
    "Once they've stopped, I open my eyes and stand up again, looking at the culprit."
    "And it's only now that I see the person standing in front of me is dressed as a superhero."
    show ryan halloween smile at center, traveling(1.25, 0.8, (640, 880))
    ryan.say "Those are some sharp reflexes you got there, [hero.name]!"
    ryan.say "I must have caught a dozen people with these things on the way over here."
    ryan.say "But not you - you were way too fast!"
    show ryan halloween normal
    "It's only now that I have the time to put a name to the voice."
    "And I can't help sounding pretty pissed as I do so."
    bree.say "Ryan, is that you?"
    "Ryan pulls the hood of his costume back to reveal his familiar face."
    "And I can already see that he's looking pretty smug too."
    show ryan halloween smile at center, traveling(1.4, 0.5, (640, 975))
    ryan.say "You got me again, [hero.name]!"
    ryan.say "So, what do you think?"
    ryan.say "I make a pretty good Arachnaman, right?"
    show ryan halloween normal
    "Urgh...is he for real?"
    "First thing he shoots me with his webbing at point-blank range."
    "Then he totally forgets which superhero he's actually come dressed as."
    "The costume he has on is clearly Spiderdude from the latest Marvellous movie."
    "And there's no such thing as Arachnaman!"
    menu:
        "Praise":
            "But the problem is that I know there's no point in correcting Ryan."
            "At the best it'll make him go on the defensive and get all pissy."
            "And at the worst he'll turn it around on me somehow."
            "Like, he'll call me petty for being obsessed with nerdy little details."
            "So the best thing is to just put on a smile and ignore all of that."
            bree.say "Ah..."
            bree.say "Yeah, Ryan..."
            bree.say "That's a pretty sweet costume."
            bree.say "He was always one of my favourite Marvellous superheroes."
            "Ryan nods at this, clearly getting the kind of response he wanted."
            "And I notice that he's doing the best he can to pose in it too."
            show ryan halloween smile at center, traveling(1.25, 0.6, (640, 880))
            ryan.say "I have to admit..."
            ryan.say "I wasn't totally sold on how tight it is."
            ryan.say "But I guess the gym bill helps with that too!"
            show ryan halloween normal
            "I can't help rolling my eyes as I usher Ryan inside."
            bree.say "Okay, okay, I get it."
            bree.say "You have a perky butt."
            bree.say "Now how about you get it inside already?"
            $ ryan.love += 2
        "Chastise":
            "So I feel like I have to put him right here and now."
            "Otherwise it's going to bug me all night long."
            bree.say "Ah, Ryan..."
            bree.say "Firstly, it's 'Spiderdude', yeah?"
            bree.say "There's no such thing as 'Arachnaman'."
            bree.say "Secondly, please don't randomly shoot webbing at me like that."
            bree.say "It's kind of rude, you know?"
            "Ryan listens to what I have to say before responding."
            "But all the time I'm talking, he's rolling his eyes."
            "And I can see that he's not particularly impressed."
            show ryan halloween annoyed at center, traveling(1.6, 0.4, (640, 1090))
            ryan.say "Geez, [hero.name]..."
            ryan.say "Do you hear yourself?"
            ryan.say "You sound like [mike.name] and his loser buddies!"
            ryan.say "You sound like a total nerd."
            ryan.say "Nobody really cares about all that stuff."
            ryan.say "At least nobody that matters!"
            show ryan halloween normal
            "I open my mouth to protest, my cheeks already burning."
            "But Ryan simply breezes past me and into the house."
            "Leaving me to hurry after him, silently fuming with rage."
            $ ryan.love -= 1
    return

label ryan_halloween_party_female:
    $ game.pass_time(2)
    scene bg livingroom
    show mike halloween at mostright5
    show jack halloween at center
    show sasha halloween at left
    with fade
    "Things seem to be looking up as Ryan and I start to mingle."
    "He actually looks like he's impressed with what he's seeing."
    "And I can feel some of my former misgivings melting away."
    "At first I think it's the décor that's caught Ryan's attention."
    "But then I notice that he's paying more attention to the other guests."
    show ryan halloween smile at center, zoomAt(1.4, (930, 970)) with easeinright
    ryan.say "Hmm..."
    ryan.say "Now that really is something!"
    ryan.say "These guys have totally gone all out on their costumes, [hero.name]."
    show ryan halloween normal
    "I do the best I can to follow Ryan's gaze as he looks around the room."
    "And I have to admit that he's right, there are some pretty sweet costumes."
    bree.say "I know what you mean, Ryan..."
    bree.say "[mike.name] and his buddies really put in a lot of effort this year."
    "As soon as I say this, Ryan shoots me a sideways glance."
    "And then he lets out a chuckle as he shakes his head."
    show ryan halloween annoyed at center, traveling(1.6, 0.5, (930, 1070))
    ryan.say "Like I'm talking about those nerds!"
    ryan.say "Nah, [hero.name]..."
    show ryan halloween smile
    ryan.say "I'm more impressed by the costumes on the ladies."
    ryan.say "Like that rocker chick you live with."
    ryan.say "She totally looks like she were poured into that outfit she has on!"
    show ryan halloween normal
    "I can already feel my cheeks beginning to burn."
    "Because Ryan's just admitted he's not actually interested in the costumes."
    "He's just using this as a chance to shamelessly ogle the girls at the party."
    "And he's being pretty open about it too!"
    menu:
        "Try to get his attention":
            "The worst thing is that what Ryan's doing isn't making me mad."
            "It's actually making me feel super jealous!"
            "I'm the one that invited him to the damn party in the first place."
            "And it's not like I'm standing here dressed like a nun either."
            "So why isn't he ogling me?!?"
            bree.say "Why are you straining to look all the way over there, Ryan?"
            bree.say "When you can just look down here, and get an eyeful like this!"
            "I make a point of standing as tall as I can when Ryan looks around."
            "And I also make sure to thrust my chest towards him at the same time."
            "This means that he gets a properly panoramic view of my breasts."
            show ryan halloween smile at center, traveling(1.8, 0.7, (640, 1200))
            ryan.say "Oh man..."
            ryan.say "I..."
            ryan.say "I see what you mean, [hero.name]!"
            show ryan halloween normal
            "I can't help smiling as I see Ryan's eyes bulge."
            "And for the first time I feel like I have his undivided attention."
            "Now all I have to do is figure out how to keep it on me all night."
            $ ryan.love += 2
        "Aren't you my date tonight!":
            "Okay, okay...I know that all guys look at other girls."
            "Hell, we girls are as guilty of it as they are too!"
            "But I just can't believe Ryan would be so brazen about it."
            "I mean, he's not even trying to disguise how thirsty he is!"
            bree.say "Ryan!"
            bree.say "You're supposed to be my date, remember?"
            bree.say "I didn't invite you along to ogle my housemate!"
            "Ryan raises an eyebrow as I try to confront him."
            "And I can see that he's not going to apologise too."
            "Instead he lets out a bland chuckle and shakes his head."
            show ryan halloween annoyed at center, traveling(1.8, 0.7, (640, 1200))
            ryan.say "Oh, [hero.name]..."
            ryan.say "You really shouldn't get so jealous, you know?"
            ryan.say "There's nothing wrong with a little window-shopping."
            ryan.say "All you're doing is making yourself look jealous and needy."
            "I open my mouth to protest, but then I close it again."
            "Because Ryan's doing that thing he always does in situations like this."
            "Somehow he manages to make it sound like I'm the one being ridiculous."
            "I know full well that he's totally gaslighting me right now."
            "But it's like he's able to hit me right where I'm vulnerable."
            "And so I feel like arguing is only going to make it worse."
            bree.say "I..."
            bree.say "I'm not jealous, Ryan!"
            show ryan halloween smile at startle(0.1, 5)
            ryan.say "Really, [hero.name]?"
            ryan.say "Which one of us are you trying to convince of that?"
            $ ryan.love -= 1
    return

label ryan_halloween_dance_female:
    $ game.pass_time(2)
    scene bg livingroom
    scene bg livingroom
    show jack halloween at mostright5
    show mike halloween at center, zoomAt(1, (540, 720))
    show sasha halloween at center, zoomAt(1, (340, 720))
    with fade
    "I keep stealing an occasional look towards the make-shift dance-floor."
    "And that's because I've been aching to get out there with Ryan all night."
    "I've never asked [mike.name] about it, but I'm sure he must be a great dancer."
    "So I'm just waiting for the right moment to ask him if he wants to."
    "And when it comes, I pluck up the courage to pop the question."
    bree.say "Erm, Ryan..."
    bree.say "I don't suppose that you..."
    bree.say "Maybe want to...dance?"
    show ryan halloween at center, zoomAt(1.0, (640, 720)) with easeinright
    "Ryan looks at me like he genuinely wasn't expecting to be asked."
    "And for a moment I'm sure that he's going to say no."
    "But then I see that Sasha's already heading out there herself."
    "Which seems too cause a sudden change in Ryan's attitude."
    show ryan halloween smile at center, traveling(1.25, 0.5, (640, 880))
    ryan.say "Sure, [hero.name], sure..."
    ryan.say "That sounds like a great idea."
    show ryan halloween normal
    "Ryan takes hold of my hand and starts leading me onto the dance-floor."
    "But I notice that he's kind of making a bee-line towards Sasha at the same time."
    "And that kind of makes me think he's keener to get close to her than to me!"
    menu:
        "Stop him":
            "I dig in my heels before we make it to the dance-floor."
            "Using all of my weight to make Ryan stop in his tracks."
            "He turns to face me, furrowing his brows."
            show ryan halloween annoyed at center, traveling(1.4, 0.4, (640, 975))
            ryan.say "What's the matter, [hero.name]?"
            ryan.say "Did you change your mind already?"
            show ryan halloween normal
            "I point to where Sasha is standing on the dance-floor."
            bree.say "I asked you to dance with me, Ryan."
            bree.say "But you seem awfully keen to get over there."
            bree.say "Over to where Sasha's dancing."
            "Ryan glances in the direction I'm pointing."
            "And then he looks back at me again."
            show ryan halloween annoyed at center, traveling(1.6, 0.3, (640, 1100))
            ryan.say "What are you saying, [hero.name]?"
            ryan.say "That she's not your friend?"
            ryan.say "That I can't dance near any other girls?"
            show ryan halloween normal
            "I can feel Ryan twisting what's happening right in front of me."
            "Just like that he's made it all about me, made me look jealous."
            "And I totally wasn't prepared for that."
            bree.say "Yes..."
            bree.say "No..."
            bree.say "I mean...I don't know!"
            with hpunch
            "Ryan shakes his head at this, looking concerned."
            show ryan halloween smile at center, traveling(1.0, 0.8, (640, 720))
            ryan.say "Wow, [hero.name]..."
            ryan.say "Sounds to me like you need to work some stuff out!"
            show ryan halloween normal
            $ ryan.love -= 1
        "Let him lead":
            "I feel like I should put the brakes on right about now."
            "Like I should call Ryan out on wanting to dance with Sasha."
            "But then I think about it for a moment, and I change my mind."
            "Because all that's going to do is make me look paranoid."
            "And he'll probably twist it around anyway, make me look even worse."
            "So instead I allow Ryan to lead me over to where Sasha's already dancing."
            "The moment that she sees me, Sasha waves her arms in the air."
            "Then she pulls me into a tight embrace, refusing to let go."
            "My intention was to encourage everyone to dance together."
            "But Sasha doesn't seem to even notice Ryan as he stands close by."
            "All of her attention is focussed on me and making me dance with her."
            show ryan halloween annoyed
            ryan.say "Ahem..."
            ryan.say "I'm standing right here!"
            show ryan halloween normal
            bree.say "Ah, Sasha..."
            bree.say "Did you meet..."
            sasha.say "Shhh!"
            sasha.say "No time for that now, [hero.name]..."
            sasha.say "Just surrender to the music, yeah?"
            sasha.say "Let go and feel it carry you along!"
            "I try my best, honestly I do!"
            "But Sasha's just too lost in the moment to be able to hear me."
            "Either that or she's had a little too much to drink!"
            "Whichever it is, the end result is still the same."
            "The two of us end up dancing as close as physically possible."
            "While Ryan's forced to watch on from the sidelines."
            "Which is kind of awkward - at least from his point of view!"
            $ ryan.love += 1
    return

label ryan_halloween_crash_sex_female:
    scene bg livingroom
    with fade
    "By now the mood in the house has subtly changed from what it was at the start of the night."
    "Back then there was the palpable buzz of excitement that comes with the beginning of a party."
    "But the hours that have passed since then have seen all of that indulged pretty much completely."
    "And now everyone is kind of sinking into a satisfied state of relaxation and general chill."
    "Most of the party-goers are sitting, or slumping, in corners and just chatting the time away."
    "But those with a little energy left have snuck off to the quieter corners of the house."
    "Looking for privacy, if you know what I mean?"
    "And it just so happens that Ryan and I fall into the latter category."
    show bg secondfloor at center, zoomAt(1.4, (640, 920)) with fade
    show ryan halloween normal at center, zoomAt(1.0, (640, 720)) with easeinleft
    "But we kind of have an advantage when it comes to finding a spot in the house."
    "You know, because he used to live here and I live here right now?"
    "Which is why I'm kind of surprised when Ryan makes straight for Sasha's bedroom door."
    show ryan halloween normal at center, zoomAt(1.0, (840, 720)) with ease
    bree.say "Hey, Ryan..."
    show bg secondfloor at center, traveling(1.6, 0.6, (540, 1020))
    show ryan at center, traveling(1.2, 0.6, (740, 840))
    bree.say "That's not my bedroom - it's Sasha's!"
    show ryan halloween smile
    play sound door_open
    "Ryan looks over his shoulder as he opens the door."
    "And I can see from the look on his face that he's not in the least bit concerned."
    show ryan halloween whining at startle(0.1, 5)
    ryan.say "Yeah, well..."
    ryan.say "It was mine before she moved in here, [hero.name]."
    ryan.say "So that means I have a prior claim on it."
    show ryan halloween evil
    bree.say "You..." with hpunch
    bree.say "You have a what?"
    bree.say "What's that even supposed to mean?!?"
    "My line of questioning gets more desperate as Ryan walks straight into Sasha's bedroom."
    "And it's pretty clear that nothing I say is going to make him back up and get out of there."
    "Which is how I end up following him into the room and closing the door behind us."
    "I hold my breath as I do so, fearing that we're walking in on Sasha in an intimate moment."
    scene bg black

    show ryan_cowgirl_bedroom3 as background
    with fade
    play sound door_close
    "But luckily for me, it turns out that we're alone in the room."
    "And I find Ryan standing in the middle of the floor, hands on his hips."
    show ryan evil halloween at hshake
    ryan.say "Oh man..."
    ryan.say "I never knew there were so many shades of black!"
    ryan.say "This place was so much lighter when Sam and I were in here."
    ryan.say "And it felt like there was twice as much space!"
    show ryan upset
    bree.say "Okay, Ryan, okay..."
    bree.say "Matters of interior decor aside..."
    bree.say "We can't be in here!"
    "Ryan turns to face me, an amused smile on his face."
    "And I notice that he has a hand on the zipper of his costume too!"
    show ryan smile
    ryan.say "Oh, is that so?"
    ryan.say "Well I beg to differ, [hero.name]."
    ryan.say "I was here before Sasha, and I don't want to leave just yet."
    show ryan evil
    ryan.say "But there's something you could do to encourage me..."










    "As if I needed it spelled out to me, Ryan sweeps his hand downwards as he climbs onto Sasha's bed."
    "And the next thing I know, he's reclining on her pillows, beckoning to me."
    "Okay, okay...I need to take a moment to explain what happens next."
    "Because I know that you're thinking Ryan's an asshole."
    "And you're right, he is."
    "But more importantly, he's a seriously hot asshole!"
    "I can't explain the power he seems to have over me."
    "Like, I know he's a jerk - but I still want him so badly."
    "As if the fact he's into me is proof that I'm different to other girls."
    "That I'm the one he's into, maybe even the one that can change him."
    "Oh god, [hero.name]...you're starting to sound like one of the crazies!"
    "Why else would I be tearing off my own costume, nodding the whole time."
    "Walking towards Sasha's bed and already longing for his touch."
    "I don't know if Ryan's aware of the effect he has on me."
    "Maybe he just takes it as written that girls fall for him."
    scene ryan cowgirl
    show ryan cowgirl sashabedroom bottom bra top hat
    with fade
    "Either way, he opens his arms to me as I clamber atop him."
    show ryan cowgirl sashabedroom bottom -bra top hat pleasure with dissolve
    "And the moment that his lips touch mine, there's no going back."
    show ryan cowgirl sashabedroom -bottom -bra top hat with dissolve
    "Oh, and I should mention that, for an asshole, Ryan's pretty great in bed!"
    show ryan cowgirl sashabedroom nakedryan -bottom -bra top hat normal with dissolve
    "I can already feel the sensation of him rising to meet me."
    "And I instinctively begin to steer him home between my thighs."
    "Ryan kisses me passionately at first, making me gasp."
    "But as I feel myself begin to melt down below, his lips move downwards."
    "He's planting kisses on my neck when it happens."
    "There's no way that my body can resist him any longer."
    "First a little crack opens, and then the dam is broken."
    "Every move we make pushes me closer, pushes him closer too."
    "To me it doesn't feel like he's pushing inside of me."
    "Instead I imagine him melting into me, our bodies flowing into each other."
    "Slowly but surely, he makes it all the way inside, filling me."
    "But it's me that begins to move first, gently lifting my thighs."
    "Even this causes a flood of pleasure to pass over and through me."
    play sexsfx1 fuck_calm loop
    show ryan cowgirl sashabedroom nakedryan -bottom -bra top hat pleasure with dissolve
    "And the effect is such that I can't keep from going ever faster."
    "Soon enough I'm riding Ryan as if my life depends on it."
    "My hands are braced against his shoulders, supporting my weight."
    "But his own are roaming around my body at the same time."
    "And I feel them exploring every inch of me, touching every sensitive place."
    play sexsfx1 fuck_moderate loop
    show ryan cowgirl sashabedroom nakedryan -bottom -bra top hat pleasure with dissolve
    "Right now I can't say that I'd care if Sasha did walk in on us."
    "The idea of being embarrassed seems small and unimportant."
    "And the only thing that concerns me is seeing this through to the end."
    "Pushing my weight down for all I'm worth, I demand more from Ryan."
    "The gesture seems to get the response I was looking for."
    play sexsfx1 fuck_speed loop
    "As he instantly kicks things up a gear, moving faster and harder."
    "I begin digging my nails into his shoulders in an effort to hold on."
    play sexsfx1 fuck_sprint loop
    show ryan cowgirl sashabedroom nakedryan -bottom -bra top hat ahegao with dissolve
    "But the pain just seems to make Ryan go harder than ever."
    "Soon enough I can't take any more, and I feel myself starting to cum."
    "The walls of my pussy squeeze like a fist, gripping Ryan's cock."
    play sexsfx1 final_thrust
    with hpunch
    "And it's no surprise that he loses it mere seconds later."
    "I want to lie there longer, savouring the moment."
    "But suddenly I remember where we are right now."
    "So instead I leap off Sasha's bed and start to get dressed."
    "Ryan follows my lead at a somewhat less urgent pace."
    stop sexsfx1
    scene bg secondfloor
    show ryan halloween normal at center
    with timelaps
    "But soon enough we're both dressed and creeping out of Sasha's bedroom."
    "And I'm pretty confident that we're going to get away with it too."
    "Because let's just say she's not the tidiest of people, you know?"
    "And we leave the place looking pretty much like it did when we found it!"
    $ ryan.love += 3
    $ ryan.sexperience += 1
    $ game.pass_time(1)
    call stop_all_sfx from _call_stop_all_sfx_42
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
