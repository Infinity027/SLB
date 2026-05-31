label jack_date_eat_a_burger:
    jack.say "Mmm..."
    jack.say "I'm so hungry I could eat a horse, [hero.name]!"
    "And he's not kidding - I watch in amazement as Jack devours his burger!"
    return

label jack_date_buy_drink:
    if bree.is_visibly_pregnant:
        bree.say "I'm on the soft drinks tonight, Jack."
        bree.say "But I'm going to buy you a drink, okay?"
        "Jack smiles and nods at the offer."
        jack.say "Aw, thanks, [hero.name]!"
        jack.say "Can I get a beer?"
    else:
        bree.say "I'm going to grab a beer, Jack."
        bree.say "And I'm going to buy you a drink too, okay?"
        "Jack smiles and nods at the offer."
        jack.say "Aw, thanks, [hero.name]!"
        jack.say "Could you get me a beer too?"
    return

label jack_date_play_darts:
    "Jack seems like he's up for playing darts, but I soon see it's all bravado."
    "In fact, he's lucky to hit the board at all with most of his throws!"
    "I beat him pretty easily, but I make sure to console him afterwards."
    return

label jack_date_pub_play_pool:
    "Jack's keen to get the balls racked up and start playing."
    "And he soon proves to be better than I expected him to be."
    "It's neck and neck for a while, but in the end, he just manages to beat me!"
    return

label jack_date_buy_a_round:
    if bree.is_visibly_pregnant:
        jack.say "I'm gonna get a beer, [hero.name]."
        jack.say "Do you want one...whoops, sorry!"
        jack.say "I forgot you were pregnant!"
        "I can't help laughing at Jack's embarrassment."
        bree.say "It's okay, Jack - I'll just have a soft drink!"
    else:
        jack.say "I'm gonna get a beer, [hero.name]."
        jack.say "Do you want one too?"
        "I can't help smiling at Jack's enthusiasm."
        bree.say "Yeah, Jack, that sounds great."
        bree.say "I'll have a beer too!"
    return

label jack_date_play_arcade_intro_female:
    "I was always worried about asking a guy to come along to the arcade with me."
    "They seem to want to go places where you can make out or they can act macho."
    "But not Jack - he practically got down on his knees in thanks when I asked him!"
    "And I thought I was a massive gaming freak!"
    jack.say "This is SO cool, [hero.name]!"
    jack.say "I never thought a girl would ask me to come here with her!"
    jack.say "You're the best!"
    "I smile and giggle like a dumb blonde at the way Jack's gushing at me."
    "But the truth is that I'm burning up with emotions inside."
    "All I did was ask him to the arcade with me."
    "And Jack's acting like I made all his dreams come true at once!"
    "It's all kind of making my head swell!"
    bree.say "Ah..."
    bree.say "It's no biggie, Jack!"
    bree.say "You like video-games...I like video-games..."
    bree.say "So it's kind of a no-brainer!"
    jack.say "If you say so, [hero.name]..."
    jack.say "I still think it's almost like we're connected!"
    jack.say "You know, like on a psychic level?!?"
    "I open my mouth, trying to think of a sensible response to that question."
    "But the arcade comes to my rescue a moment later."
    "Suddenly Jack spots a game he wants to play."
    "And I'm spared the task of answering him."
    jack.say "Come on, [hero.name]..."
    jack.say "We have to play this one - NOW!"
    return

label jack_date_play_arcade_win_female:
    "Jack pumps the coins into the arcade cabinet, and we settle in to play."
    "I didn't bother to tell him, but I've played the hell out of this game."
    "And so it doesn't take long for me to leave him in the dust!"
    "Once we're out of coins, I'm the clear winner."
    jack.say "Wow, [hero.name]..."
    jack.say "I thought I was the best at this game!"
    bree.say "Well, maybe I just got lucky, Jack?"
    "For a moment, Jack looks like he's going to question me further."
    "But then he shrugs and the whole thing seems to be forgotten."
    jack.say "Sure, [hero.name], sure..."
    jack.say "Well played!"
    return

label jack_date_play_arcade_lose_female:
    "Jack pumps the coins into the arcade cabinet, and we settle in to play."
    "I didn't bother to tell him, but I've never been any good at this game."
    "And so it doesn't take long for him to leave me in the dust!"
    "Once we're out of coins, Jack's the clear winner."
    bree.say "Wow, Jack..."
    bree.say "I didn't know you were so good at this game!"
    jack.say "Well, maybe I just got lucky, [hero.name]?"
    "For a moment I look at Jack with narrowed eyes."
    "Did he trick me into playing a game he's a demon at?"
    "But then I realise I'm being petty, and I forget all about it."
    bree.say "Well played, Jack..."
    bree.say "Now, what are we gonna play next?"
    return

label jack_dick_reactions_female:
    if not bree.flags.seenJackDick:
        $ bree.flags.seenJackDick = 1
        $ bree_dick_seen = bree.flags.seenDwayneDick + bree.flags.seenScottieDick + bree.flags.seenVictorDick + bree.flags.seenDannyDick + bree.flags.seenMasterDick + bree.flags.seenMikeDick

        if bree_dick_seen > 0:
            "I stare at the sight of Jack's manhood."
            "And I have to say that it's smaller than I expected!"
            "Of course, he notices my reaction - what guy wouldn't?"
            jack.say "Is..."
            jack.say "Is there something wrong, [hero.name]?"
            bree.say "What?"
            bree.say "No...no way, Jack!"
            jack.say "Look...I know it's not the biggest..."
            bree.say "Oh no...no, no, no..."
            bree.say "It's fine, Jack - size isn't everything!"
            "Jack gives me a pained smile, but I know he's not convinced."
            $ jack.love -= 10
        else:
            "I stare at the sight of Jack's manhood."
            "And I can feel my eyes getting wider by the second."
            "It's fucking huge - far bigger than I expected!"
            "Of course, he notices my reaction - what guy wouldn't?"
            jack.say "Is..."
            jack.say "Is there something wrong, [hero.name]?"
            bree.say "Jack..."
            bree.say "It's a monster!"
            jack.say "I know, I know..."
            jack.say "I'm sorry if it's scary..."
            bree.say "Oh no...no, no, no..."
            bree.say "It's fine, Jack - better than fine!"
            "I can feel my cheeks flushing."
            "And that's because I'm imagining how it'll feel inside of me right now!"
            "Jack gives me a meek smile, probably because he can't read my mind!"
            $ jack.love += 10
    return

label jack_breast_reactions:
    if bree.flags.boobjob:
        "Jack stares at my naked breasts, not saying a word."
        "His face is a picture of amazement."
        "But I can't tell if it's good or bad!"
        bree.say "Erm, Jack..."
        bree.say "You mind telling me what you're thinking right now?"
        jack.say "Huh?!?"
        jack.say "I...I want to bury my face in them, [hero.name]!"
        jack.say "They're so BIG!"
        "I feel my cheeks flushing red at Jack's words."
        "And he sees it too, struggling to explain himself."
        jack.say "I...I'm sorry, [hero.name]!"
        jack.say "I didn't mean to be disrespectful!"
        jack.say "Little breasts are cool too..."
        jack.say "I just...love big ones more!"
        "I nod calmly at Jack's attempts to explain himself."
        "But all the time I'm smiling inside."
        "Because now I know how just how much power my boobs have over him!"
        $ jack.sub += 10
    else:
        "Jack stares at my naked breasts, not saying a word."
        "His face is a picture of amazement."
        "But I can't tell if it's good or bad!"
        bree.say "Erm, Jack..."
        bree.say "You mind telling me what you're thinking right now?"
        jack.say "Huh?!?"
        jack.say "I...I thought they'd be bigger!"
        "I feel my cheeks flushing red at Jack's words."
        "And he sees it too, struggling to explain himself."
        jack.say "Not that that's a bad thing!"
        jack.say "Little breasts are cute, [hero.name]!"
        bree.say "O...okay, Jack..."
        bree.say "Thanks...I guess!"
        $ jack.sub -= 10
    return

label jack_date_intro_halloween_female:












label jack_halloween_invitation_female:
    show jack
    "Almost the moment I agreed to the Halloween party, I knew who I wanted to invite."
    "It's going to be quirky and cute, with costumes and fun party games to boot."
    "And the only guy I can think of who would make all that even more fun is Jack."
    "I can already see him being a big, silly goof-ball while we bob for apples."
    "Or trying to impress me with his zombie moves on the make-shift dancefloor."
    "So as soon as I get the chance, I just come right out and ask him."
    bree.say "Oh, Jack..."
    bree.say "There's something I wanted to ask you."
    jack.say "Yeah, [hero.name]?"
    jack.say "What is it?"
    "I can hear genuine interest in Jack's voice."
    "And so I don't hesitate to get straight to the point."
    bree.say "We're throwing a Halloween party at the house."
    bree.say "And I wondered if you wanted to come along?"
    bree.say "You, know...kind of as my date?"
    "At the mention of a party, Jack raises his eyebrows."
    "And his eyes go even wider than usual."
    jack.say "A party?"
    jack.say "At your place?"
    jack.say "Huh..."
    jack.say "[mike.name] never said anything about it!"
    "Jack's response throws me for a moment."
    "And I have to shake my head to regain my focus."
    bree.say "What's [mike.name] got to do with it?"
    bree.say "I'm the one inviting you to the party!"
    bree.say "So do you want to come, or what?"
    if jack.love >= 100:

        "Jack seems to realise that he's said the wrong thing."
        "And he instantly starts trying to make amends."
        "He nods his head and then shakes it, again and again."
        "Like he doesn't know which one will serve him best."
        jack.say "Sure, [hero.name], sure..."
        jack.say "I'd love to come to the party."
        jack.say "Of course I would."
        "I nod too, willing to let the matter drop."
        "After all, I got the answer I wanted, in the end."
        bree.say "Great, Jack..."
        bree.say "That's just great."
        bree.say "Oh, and it's a costume party too."
        bree.say "I'm guessing you have that covered though?"
        "Jack lets out a smug laugh and nods at this."
        jack.say "Oh yeah, [hero.name]..."
        jack.say "Between cosplaying and live-action roleplaying..."
        jack.say "I got it well and truly covered!"
        "I nod, already wondering what Jack's going to be dressed as on the night."
        "And I just hope that it's going to be something that makes him look good."
        "Rather than some obscure thing that he has to spend an hour explaining to me."
        $ game.flags.halloween_girl = "jack"
    else:

        "Jack doesn't seem to pick up on the fact that he's said the wrong thing."
        "Instead he doubles down on it, frowning and furrowing his brow in thought."
        "For a moment he even seems to forget that we're in the middle of a conversation."
        jack.say "I knew it..."
        jack.say "I just knew it!"
        jack.say "The moment he moved in with girls..."
        jack.say "I knew this would happen!"
        "I keep trying to look Jack in the eye as he says all of this."
        "But in the end I have to wave a hand in his face, clicking my fingers."
        "And only then does he seem to remember I'm still here."
        bree.say "What the hell, Jack?"
        bree.say "I'm standing right here!"
        jack.say "Sorry, [hero.name]..."
        jack.say "But I think my best friend is trying to cut me out of his life."
        jack.say "And if he doesn't want me at the party, then I'm not going to go at all!"
        bree.say "But it's me asking you, not [mike.name]!"
        bree.say "And if you're right, not going is what he wants!"
        "But it seems like my words just aren't getting through to Jack."
        "He shakes his head and turns to walk away."
        jack.say "I'm sorry, [hero.name]..."
        jack.say "But I need some time alone."
        jack.say "Some time to make sense of all this."
        "I shake my head as I watch Jack walk off."
        "And I have to say that I'm kind of glad to see him go."
        "Because there's no way I want to get involved in the mess going on in his head right now!"
    return

label jack_halloween_arrival_female:
    return

label jack_halloween_party_female:

    return

label jack_halloween_dance_female:
    $ game.pass_time(2)
    scene bg livingroom
    show jack halloween
    with fade
    "As soon as the song I've been waiting for starts, I grab Jack's hand."
    "And then I begin to pull him towards the dancefloor without waiting for permission."
    "But he seems to realise what's going on, as I feel him offer no resistance."
    "In fact Jack almost beats me onto the dancefloor in his enthusiasm."
    hide jack
    show dance jack halloween
    with fade
    "And once we're out there, he's the one setting the pace."
    "Throwing himself around in a series of crazy moves."
    "Jack keeps on dancing like that, just doing whatever seems to come into his head."
    "But then I notice him slowing down a little as he sees people are looking at him."
    bree.say "What's the matter, Jack?"
    jack.say "Erm..."
    jack.say "[hero.name]..."
    jack.say "Why's everyone looking at me like that?"
    "I follow his gaze, seeing that he's right."
    "People are looking straight at him."
    "And they're laughing too!"
    menu:
        "Tell Jack the truth":
            bree.say "Huh..."
            bree.say "I think they're watching you dance, Jack."
            bree.say "Your moves are a little unusual, you know?"
            $ jack.love -= 2
            "The moment the words are out of my mouth, I know I made a mistake."
            "Jack's cheeks turn bright red, and he goes as stiff as a board."
            "I keep on trying to dance, hoping that he'll snap out of it."
            "But in the end I have to walk him off the dancefloor and out of sight."
            "It takes a good while for Jack to recover from the embarrassment."
            "And all the time he's out of action, I can't help cursing myself."
            "If I'd only thought to protect his feelings, we'd still be dancing now."
        "Start to dance like Jack":
            bree.say "Huh..."
            bree.say "Who cares, Jack?"
            bree.say "They're probably just checking out your moves!"
            $ jack.love += 2
            "With that, I start to dance again."
            "But this time I'm consciously imitating Jack's moves."
            "He keeps looking around for a moment, as if he's unsure."
            "Then he seems to forget about the watchers and get into it again."
            "Pretty soon Jack and I are dancing around like lunatics."
            "And neither of us could care if anyone's watching or not."
    scene bg black with dissolve
    pause 1
    return

label jack_halloween_sex_female:
    scene bg livingroom with dissolve
    "It's getting late by now, and the party seems to be winding down."
    "Most of the guests are tired and more than a little drunk."
    "And they seem more interested in chilling out than being wild."
    "I'm just about to take a break from my duties as host for the night."
    scene bg house
    show jack halloween
    with fade
    "Which is when I see Jack walking towards the front door."
    "The party's not over and he hasn't said anything to me about wanting to leave."
    "So I hurry after him, putting a hand on his shoulder just as he reaches the door."
    bree.say "Hey, Jack..."
    bree.say "Where are you going?"
    bree.say "Just outside for a smoke, I hope?"
    "Jack turns to face me, looking more than a little confused."
    jack.say "Erm..."
    jack.say "No, [hero.name]..."
    jack.say "I don't smoke!"
    "Now it's my turn to look confused."
    bree.say "So where are you going?"
    bree.say "The party's not over yet."
    bree.say "Have you got an early start in the morning?"
    jack.say "No, I haven't."
    jack.say "I just usually go home around this time when I'm at a party."
    jack.say "Everyone else disappears off to the bedrooms and leaves me on my own."
    jack.say "And they don't really notice that I'm gone!"
    "My level of confusion is rising steadily now."
    "And I can't help putting a hand on Jack's wrist."
    "Which I use to pull him away from the door."
    bree.say "I'd notice you're gone, Jack."
    bree.say "You're my date tonight!"
    jack.say "You mean..."
    jack.say "You want me to stay?!?"
    "In that moment, Jack just seems so clueless and sweet."
    "There's nothing that I can possibly do to resist him."
    "So this had better not be some complicated ruse on his part!"
    bree.say "I want you to do more than that, Jack."
    bree.say "But you can start by coming with me."
    scene bg secondfloor
    show jack halloween
    with fade
    "Jack offers no resistance as I lead him up the stairs."
    "And he still looks genuinely surprised when we arrive at my bedroom door."
    scene bg bedroom4
    show jack halloween
    with fade
    "I open it and push him inside, then make sure to close and lock it behind us."
    jack.say "Wow..."
    jack.say "Your room's really great, [hero.name]."
    jack.say "It's kind of pink and cute...like you!"
    "I can't help giggling and shaking my head at Jack."
    "Even as I walk him over to my bed and sit him down on the edge."
    "I perch beside him, leaning in to kiss him on the lips."
    "At first Jack seems to hesitate, returning the kiss gently."
    "But then I feel myself warming to the sensation of his lips against mine."
    "And I can already sense the way that it's waking up the rest of my body."
    "So yeah, newsflash - we girls can get seriously horny and turned-on too!"
    "Before I know it, I'm sliding my tongue into his mouth."
    "And then I all but clamber onto Jack, pushing him down onto the bed."
    "I don't know if he's going along with it or too shocked to do anything else."
    "Either way Jack doesn't stop me getting what I want."


    "Instead I find myself atop him, pinning him down."
    "And my hands are already tearing away at his skimpy costume."
    "Once it's stripped away, I begin to do the same to my own."
    "All the time Jack's looking up at me, amazement in his eyes."
    "Hardly the reaction I'd expect from a barbarian warrior!"
    "Almost as soon as I have his cock out of his furry pants, I see he's ready."
    "Rubbing the shaft with my hand only makes it swell a little more."
    "But it has a decidedly more dramatic effect on me."
    "I have to swallow and hold my breath as I feel my groin tremble with anticipation."
    "And as I lower myself down and onto him, I do it with a sense of genuine urgency."
    "Of course my body still resists just a little, despite what I want."
    "So I find myself grinding down on Jack's cock, working it hard as I can."
    "Little by little it begins to inch inside of me."
    "And the sense of relief is almost too much for me to bear."
    "I can already feel my arms beginning to become weak."
    "I don't know how long they'll be able to hold me up!"
    "That very same moment, I feel Jack's hands on me."
    "They take the weight of my body, supporting me."
    "And then he begins to move beneath me, as if waking up or coming alive."
    "Where before he was passive, now Jack seems to find his confidence."
    "He begins to thrust up from below, each subsequent one more firm than the last."
    "And before I know it, he's the one in the lead, the one setting the pace."
    "The sensation of him inside of me is almost impossible to describe."
    "At once it seems to sustain me and make me want to keep on going."
    "But at the same time it makes me aware of how weary I actually am."
    "My muscles feel like they're melting from my body."
    "Like I'm becoming liquid in Jack's arms."
    "Right now I feel like I'm sinking down onto him."
    "Lying atop him and letting him hold me up completely."
    "That is until I feel a spark of something deep inside of me."
    "It's like the very last kernel of energy, buried deep down."
    "But somehow he's managed to find it."
    "And now it's about to explode!"
    bree.say "Mmm..."
    bree.say "Jack..."
    bree.say "I'm going to..."
    "It happens before I can finish speaking."
    "My orgasm hits like a tidal wave and I can't help grinding myself down onto Jack."
    "This means that he's pushed over the edge too, and then nature takes its course."
    jack.say "Oh fuck..."
    jack.say "[hero.name]!"
    "I thought that the sensation couldn't get any more intense."
    "But as Jack loses it deep inside me, it seems to redouble."
    "This time I really do collapse atop him, almost blacking-out."
    "And the afterglow is nowhere near passed as I slide off him."
    "But there's nothing I can do to keep my eyes from closing."
    "So before I know it, I'm drifting off into a deep, satisfied sleep."
    $ jack.sexperience += 1
    $ game.pass_time(1)
    return

label jack_dance_with:
    "Jack reluctantly follows me onto the dance-floor, looking a little sheepish."
    "And it doesn't take me long to see that he's far from the best dancer in the room."
    "But he soon starts to forget himself, dancing in a goofy manner to the music."
    "It's so silly that I can't help smiling, delighted by the way he's showing off for me."
    "Sure, it's cheesy - but it's also cute that he's only interested in impressing me!"
    return

label jack_after_dance_success_with_female:
    show jack normal blush
    "I've barely finished dancing before Jack appears out of nowhere."
    "He's all worked up and excited, getting right up in my face."
    show jack smile
    jack.say "[hero.name]...[hero.name]..."
    jack.say "Where'd you learn to dance like that?"
    jack.say "You were like, totally amazing!"
    show jack normal
    "I can't help starting to blush as Jack gushes over me."
    "And not least because I know that he means every word he's saying."
    "Because Jack's one of those guys who finds it really hard to lie."
    "I mean, he can do it when he has to."
    "But he really sucks at it!"
    bree.say "Oh..."
    bree.say "Thanks, Jack..."
    bree.say "But you don't have to flatter me like that."
    bree.say "I'm sure my dancing was nothing special."
    "Okay, so I'm doing that thing where I put myself down."
    "And I hope that the guy is going to immediately start praising me."
    "It's a gamble, and some guys are all too ready to agree, rather than praise."
    "But luckily for me, Jacks not one of them."
    show jack smile
    jack.say "What are you talking about, [hero.name]?!?"
    jack.say "That was super special, totally awesome!"
    show jack normal
    bree.say "Aww..."
    bree.say "Thank you, Jack..."
    bree.say "That's so sweet of you to say!"
    show jack normal -blush
    return

label jack_after_dance_failure_with_female:
    show jack embarrassed
    "I know that something is wrong the moment that I stop dancing and look over at Jack."
    "With any other guy, I'd be seeing them giving me a disapproving look right now."
    "Or maybe even laughing and pointing at me, trying to make me feel worse than I already do."
    "But Jack's such a sweetheart that he won't even look me in the eye."
    bree.say "So, Jack..."
    bree.say "Be honest with me, okay..."
    bree.say "How bad was it?"
    show jack annoyed blush
    "The moment I put him on the spot, Jack starts to blush."
    "And he still can't bring himself to make eye-contact."
    show jack guilty
    jack.say "Oh, you know how these things are, [hero.name]..."
    jack.say "I wasn't really paying that much attention most of the time."
    jack.say "And dancing's kind of subjective, yeah?"
    jack.say "Like people are either really into it or really against it?"
    show jack annoyed
    "I take a deep breath and then let it out."
    bree.say "Urgh..."
    bree.say "It was pretty terrible, wasn't it?"
    show jack guilty
    jack.say "Erm..."
    jack.say "Yeah, [hero.name]..."
    jack.say "It wasn't the best."
    show jack normal -blush
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
