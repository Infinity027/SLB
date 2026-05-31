label scottie_date_intro_halloween_female:



label scottie_halloween_invitation_female:
    "Almost the moment I agreed to the Halloween party, I knew who I wanted to invite."
    show scottie b swimsuit happy
    show fg_dreamy as fg
    with fade
    "The image of Scottie's muscles pops into my head almost before his face does."
    "And then all I can think about is seeing him in a cute costume that shows off the former."
    "Well, that and slow-dancing with my head nestled on those rock-hard pectorals of his!"
    hide scottie
    hide fg_dreamy as fg
    with dissolve
    "And I know that he used to be in a relationship with Sasha."
    "But that's ancient history by now, right?"
    "Surely the two of them are at the point where they can just be friends?"
    "Even where they can laugh about all the ways their relationship went wrong?"
    "Okay...maybe that's asking a little too much."
    "But I still want to invite Scottie along as my date."
    show scottie with fade
    "So I ask him the first chance that I get."
    bree.say "Hey, Scottie..."
    show scottie stuned
    scottie.say "Huh?"
    show scottie happy
    scottie.say "Oh, hey, [hero.name]!"
    scottie.say "How's it hanging?"
    show scottie normal
    bree.say "Erm..."
    bree.say "It's hanging fine, Scottie..."
    bree.say "I just wanted to ask if you're doing anything for Halloween?"
    show scottie happy
    "Scottie nods eagerly, letting out a goofy laugh."
    scottie.say "Yeah, [hero.name]..."
    scottie.say "Me and a couple of the guys usually go trick or treating."
    show scottie normal
    bree.say "Trick or treating?"
    bree.say "Really?"
    bree.say "Scottie, you're supposed to be an adult!"
    show scottie happy
    scottie.say "Well, we really more kinda dress-up in masks."
    scottie.say "Then we egg houses and TP the trees in the neighbourhood!"
    show scottie normal
    bree.say "Sounds like a riot, Scottie..."
    bree.say "But how about this year you come to my Halloween party instead?"
    if scottie.love >= 100:

        "Scottie stops to actually think about the offer for a moment."
        "The whole time he's scratching the back of his head."
        "And it's almost like I can hear the gears grinding away inside of his skull."
        "Finally I see a genuine smile spread across his face, and he nods his head."
        $ scottie.love += 1
        show scottie happy
        scottie.say "That sounds great, [hero.name]!"
        scottie.say "Much more fun than egging houses!"
        show scottie normal
        "I feel my heart begin to beat faster in my chest."
        "Because I just got the answer that I wanted."
        bree.say "That's great, Scottie!"
        bree.say "The party's at my house on Halloween night."
        bree.say "But I guess that's pretty obvious!"
        "Scottie shakes his head at this."
        show scottie happy
        scottie.say "Uh-uh, [hero.name]..."
        scottie.say "I was just going to ask when it was happening."
        show scottie normal
        bree.say "Oh, and it's a costume party too."
        bree.say "So you'll need to get yourself one, okay?"
        "Scottie nods, already beginning to look like he's in deep thought."
        "Or at least he would if he were most other guys."
        "Scottie kind of looks like that when he's trying to tie his shoelaces too!"
        $ game.flags.halloween_girl = "scottie"
    else:

        "Scottie stops to actually think about the offer for a moment."
        "The whole time he's scratching the back of his head."
        "And it's almost like I can hear the gears grinding away inside of his skull."
        "Finally I see a look of concern spread across his face."
        show scottie talkative
        scottie.say "Wait a minute..."
        scottie.say "Is the party at your house?"
        show scottie sad
        bree.say "Well, yeah, Scottie..."
        bree.say "Where else would I be holding it?"
        show scottie talkative
        scottie.say "And that means Sasha's going to be there, right?"
        scottie.say "Like, my former girlfriend Sasha?"
        scottie.say "Who's now like, my mortal enemy?!?"
        show scottie sad
        bree.say "I maybe wouldn't put it as dramatically as that..."
        bree.say "But basically, yeah."
        "Scottie shakes his head as he starts to back away from me."
        show scottie whining
        scottie.say "Oh no...no way!"
        scottie.say "I'm not coming to that party!"
        show scottie sad
        "With that, Scottie turns on his heel and runs away."
        "And by that I mean he literally runs off!"
        bree.say "Scottie!"
        bree.say "Where are you going?"
        bree.say "Sasha's not actually here, you moron!"
    return

label scottie_halloween_arrival_female:
    return

label scottie_halloween_party_female:
    $ game.pass_time(2)
    scene bg livingroom
    show scottie halloween normal at left5
    show sasha halloween normal at right5
    with dissolve
    "I'm just coming back from grabbing a glass of punch for Scottie and myself."
    "And that's when I see that he's been engaged in conversation by someone else."
    "I can't tell who it is at first, just that Scottie looks really uncomfortable."
    "And when he sees me walking over, he starts to wave his arms in the air."
    "I have no idea what the problem could be, until I see who he's talking to."
    "It looks like Sasha's got him cornered and is giving him a piece of her mind."
    "Of course she sees him waving to me, and she shoots me a knowing glance."
    bree.say "Hey, guys..."
    bree.say "What are you talking about?"
    show scottie talkative
    scottie.say "[hero.name]..."
    scottie.say "You have to help me!"
    show scottie sad
    show sasha shout
    sasha.say "Hey, [hero.name]..."
    sasha.say "Scottie and I were just talking about the time we were an item."
    sasha.say "Weren't we, Scottie?"
    sasha.say "About how he's the biggest scumbag under the sun!"
    show sasha normal
    menu:
        "Defend Scottie":
            "I know that Scottie wasn't the best boyfriend to Sasha."
            "But I still feel like I have to defend him in some way."
            "Because Sasha can't just keep beating him up about it forever."
            bree.say "Scottie's told me all about it, Sasha."
            bree.say "Just like you did too."
            bree.say "And he's really trying to be a better person."
            show scottie normal
            show sasha annoyed
            "Sasha wrinkles her face up at this."
            "And she looks less than convinced by my words."
            show sasha whining
            sasha.say "Yeah..."
            sasha.say "He's trying alright!"
            hide sasha annoyed with easeoutright
            "Sasha shoots Scottie an evil glare as she walks off."
            show scottie halloween at center with ease
            "And as soon as she's gone, he lets out a genuine sigh of relief."
            show scottie happy
            scottie.say "Phew..."
            scottie.say "Thanks for rescuing me, [hero.name]!"
            show scottie normal
            bree.say "Don't worry about it, Scottie..."
            bree.say "Just make sure you treat me better than you did her."
        "Defend Sasha":
            "I know that I should be defending Scottie."
            "But I also know that he wasn't exactly the best boyfriend to Sasha."
            "And how is he ever going to learn his lesson if people keep letting him off?"
            bree.say "Oh, I remember you telling me all about it, Sasha."
            bree.say "You were a bit of a shit back then, weren't you?"
            "Scottie almost leaps backwards when he realises I'm not on his side."
            "And his head turns this and that now he's under attack from us both."
            show scottie whining
            scottie.say "But...but..."
            scottie.say "But, [hero.name]!"
            show scottie sad
            bree.say "It's okay, Scottie..."
            bree.say "I know you're trying to change your ways."
            bree.say "And if you don't, you'll have the pair of us to contend with!"
            show sasha happy
            pause 0.2
            hide sasha with easeoutright
            "Sasha lets out a wicked laugh as she walks away."
            "And Scottie just stares at his feet."
            "Still too awkward to even look at me."
    scene bg black with dissolve
    pause 1
    return

label scottie_halloween_dance_female:
    $ game.pass_time(2)
    scene bg livingroom
    show scottie halloween happy
    with dissolve
    scottie.say "Come on, [hero.name]..."
    scottie.say "I love this song!"
    show scottie normal
    "Scottie doesn't even give me the chance to ask what's going on."
    "One moment he's standing by me, a glass of punch in his hand."
    "And the next he pretty much tosses it up in the air."
    "Then he's headed in the direction of the dancefloor!"
    "I follow on his heels, more out of surprise than anything else."
    "And within a few seconds, I find myself right in the middle of the floor."
    "Sure, Scottie's a big, dumb kind of guy."
    "But he has that weird kind of animal magnetism, you know?"
    "So I can't help smiling and going along with him as he goofs around."
    "That is until his magnetism seems to have the same effect on others too."
    "Suddenly Sasha appears right beside us, intent on dancing too."
    "Funny, I thought she was pretty pissed-off with Scottie at the moment."
    "But she doesn't seem to be acting that way right now."
    menu:
        "Pull Scottie away from Sasha":
            "What is Sasha even thinking?"
            "She told me that she was done with Scottie."
            "That the guy was a part of her life she wanted to move on from."
            "But now that he's dancing with me, she wants back in?"
            "Oh no, not going to happen!"
            "I grab hold of Scottie."
            "Pulling him away from Sasha and towards me."
            "Sasha still keeps up with us though."
            "Following on Scottie's heels."
            "Which only leaves me one choice."
            "So I pull him in even closer, planting my lips against his."
            "Luckily for me, Scottie doesn't need much encouragement."
            "Pretty soon he's kissing me with a passion."
            "And once it's over, I look around."
            "But I can't see any sign of Sasha."
            "So I guess she got the message."
        "Dance with Scottie and Sasha":
            "I guess that's why Sasha was okay with me dating Scottie."
            "She's enough of an adult to put what happened between them behind her."
            "So the best thing for me to do would be the exact same."
            "Which is why I make a point of dancing closer to her too."
            "Scottie seems more than a little puzzled at first."
            "Probably wondering if this is some kind of trick."
            "If Sasha and I are going to turn on him as one."
            "But after a short while he seems to forget his fears."
            "I suppose that's on account of his being a pretty simple guy."
            "If he's dancing with two girls at once, he must think he's winning."
            "And to him, there's probably nothing more to it."
    scene bg black with dissolve
    pause 1
    return

label scottie_halloween_sex_female:
    scene bg livingroom
    show mike halloween happy at right
    show scottie halloween happy
    show sasha halloween happy at left
    with fade
    "It's getting pretty late by now and the party's starting to wind down."
    "Everyone's either tired, drunk or both and wanting to chill out."
    "And I know that I'm feeling the same way after playing host all night."
    scene bg black
    show bg bathroom with dissolve
    "The first chance I get, I slip away to use the bathroom."
    "But when I get there, I find that I don't really need to go at all."
    "So perhaps I just wanted to have some quiet time alone?"
    "Suddenly there's the sound of someone pounding on the bathroom door."
    "So it looks like I can forget about getting that alone time!"
    scottie.say "Erm..."
    scottie.say "Hey..."
    scottie.say "Open up in there!"
    "I let out a sigh and resolve myself to the situation at hand."
    "Then I walk the two or three steps to the door and open it."
    bree.say "Okay, Scottie, okay..."
    bree.say "Just let me get out of here before you come barging in!"
    scene bg black
    show bg secondfloor
    show scottie normal halloween
    with fade
    "I open the door wide enough to see Scottie standing in the corridor outside."
    "And I know how guys get when they're desperate to use the bathroom too."
    "So I'm fully expecting him to elbow me out of the way despite my request."
    "But instead he takes me by surprise, as he steps back a little."
    "On top of that, there's also the fact that he doesn't look like he needs to go."
    "There are none of the tell-tale signs, like jumping from one foot to the other."
    "In fact, if he hadn't knocked on the door, I wouldn't have known he wanted to go at all."
    bree.say "Alright, Scottie..."
    bree.say "The bathroom's free now."
    "I make a gesture for him to walk inside."
    show scottie embarrassed
    "But Scottie still just stands there, staring down at his feet."
    bree.say "What are you waiting for?"
    bree.say "Written permission?"
    show scottie whining
    scottie.say "Well..."
    scottie.say "You see..."
    show scottie talkative
    scottie.say "The thing is...I don't really need to go."
    show scottie normal
    bree.say "What's the matter, Scottie?"
    bree.say "Can't you pee with a girl around?"
    show scottie talkative
    scottie.say "No, [hero.name], that's not it."
    show scottie whining
    scottie.say "I kind of..."
    scottie.say "I kind of followed you to the bathroom."
    show scottie blush
    scottie.say "You know, thinking we might fool around?"
    scottie.say "I had it all figured out too!"
    show scottie embarrassed
    "I narrow my eyes and cock my head on one side."
    bree.say "So what went wrong?"
    bree.say "Did you forget what you were going to say next?"
    show scottie blush
    scottie.say "Uh-uh...I figured I wouldn't need to say anything else!"
    show scottie embarrassed
    bree.say "Oh, Scottie..."
    bree.say "You actually thought you'd trick your way in."
    bree.say "And then I'd just leap into your open arms?"
    "Now Scottie's beginning to look decidedly sheepish."
    show scottie perv
    scottie.say "Well...yeah!"
    bree.say "Oh dear, Scottie..."
    bree.say "This isn't going very well, is it?"
    show scottie blush
    scottie.say "I guess not!"
    show scottie embarrassed
    "Scottie just looks so defeated and crestfallen that I can't help feeling sorry for him."
    "I'm so used to seeing him cocky and full of confidence that it's quite a surprise."
    "As I'm looking at him, I can feel something funny happening inside of me."
    "It kind of feels like the sensations I get when I look at a puppy with huge, sad eyes."
    "Oh no!"
    "Scottie's having the exact same effect on me."
    "And I have the same instinct as with a puppy too."
    "Which is why I can't help throwing my arms around him and hugging him as tightly as I can."
    "Of course the moment I do that, things get much worse."
    "Because now I can feel the sensation of his muscles against my body."
    "And you know that one thing Scottie has in abundance is muscles."
    "Big, bulging muscles!"
    "Before I know what I'm doing, my hands are moving over his entire body."
    "But one of them stops in another place where Scottie happens to be very big."
    "And that mere touch is enough to start making him bigger still!"
    show scottie surprised
    scottie.say "Whoa..."
    scottie.say "[hero.name]..."
    scottie.say "I thought you weren't up for it?"
    show scottie embarrassed
    bree.say "Let's just say you changed my mind, Scottie!"
    "It doesn't take more than a moment for Scottie's entire mood to change."
    "Before he was sad and downcast, looking like he wanted to slink away and hide."
    "But now he's becoming more confident and amorous with every passing second."
    scene bg black
    show bg bathroom
    show scottie halloween perv
    with fade
    "I start walking backwards, meaning to angle us into the bathroom."
    "Instead Scottie all but picks me up and bundles me in there himself."
    "The door slams closed behind us, and I somehow manage to lock it too."
    "A second later, Scottie lift me up against the sink."
    "My feet are well off the ground, making me cling to him with my legs."
    "At the same time our hands are tearing at each other's clothes."
    scene bg black
    show scottie standing bathroom halloween
    with fade
    "Neither of us seems willing to wait until we're undressed either."
    "As soon as I feel the heat of Scottie's cock in my hand, I know that I want it."
    "So I desperately pull down my pants and underwear, jamming it between my thighs."
    "That's almost all the work I have to do, as Scottie takes over a moment later."
    "He thrusts upwards as he pulls me down, and he's right on target too."
    "At first my body does the best it can to resist, despite my wishes."
    "But there's no way that it can keep doing so for long."
    "Not with the sensations that he's sending through every fibre of my being."
    show scottie standing vaginal
    "All at once the dam breaks down there, and Scottie slides into me."
    "Of course it's not a total surrender, and normally things would go steadily from here."
    "But Scottie's not in that kind of mindset, not at all."
    "Instead he pushes right on, filling me in a matter of seconds."
    "Almost before I can catch my breath, he's moving again."
    "Thrusting in and out of me at a speed that leaves me breathless."
    "He doesn't stop or slow down once, only seeming to get ever faster."
    "And it's not like I can raise a word of protest, even if I wanted to."
    "I feel like my insides are being melted by his efforts."
    show scottie standing ahegao with hpunch
    "Like I'm going to turn into liquid and seep though his fingers and onto the floor!"
    with hpunch
    "And then it happens, my orgasm hits and I go as limp as a ragdoll."
    show scottie standing creampie with hpunch
    "At the same time, Scottie loses it too, releasing everything he has to give."
    "I swear that I black out for a moment, that it's just too much for me."
    scene bg black
    show bg bathroom
    with fade
    "Because when I finally regain my senses, we're both slumped on the bathroom floor."
    "Neither of us can move, so we just lie still, helpless and gasping for breath."
    "And not for the first time, I'm thankful I remembered to lock the bathroom door."
    $ scottie.sexperience += 1
    $ game.pass_time(1)
    return


label scottie_after_dance_success_with_female:
    show scottie normal
    "I can see that Scottie's watching me as I'm dancing."
    "And at first I think he's just checking out my moves."
    "But then every time I catch a glimpse of his face his expression seems to change."
    "Like he's getting ever more amazed each time manage to get a look at him."
    "So as my dance comes to an end, I hurry over to where he's standing."
    "Because I want to find out what's gotten him so gobsmacked."
    bree.say "Hey, Scottie..."
    bree.say "Are you okay?"
    show scottie surprised
    "Scottie's still staring at me with the same amazed expression on his face."
    "And for a moment I think that I'm going to have to slap him to get an answer."
    "But then he seems to snap out of it, his face becoming more animated."
    show scottie happy
    scottie.say "[hero.name]..."
    scottie.say "Where did you learn to dance like that?!?"
    scottie.say "Your moves are like, out of this world!"
    show scottie normal
    "I can feel my cheeks flushing red as Scottie heaps praise on me."
    "And I can't help looking around to make sure nobody else hears him."
    bree.say "Scottie!"
    bree.say "You're making me blush!"
    show scottie happy
    scottie.say "I can't help it, [hero.name]!"
    scottie.say "I gotta be honest about this kind of thing."
    scottie.say "Your dancing is just totally amazing!"
    show scottie normal
    return

label scottie_after_dance_failure_with_female:
    show scottie joke
    "I can see that Scottie's watching me as I'm dancing."
    "And at first I think that he must be pretty impressed with what he sees."
    "Because from the few glimpses that I get of him, he seems to be smiling."
    "But as my dance comes to an end, I notice that he's actually laughing!"
    "So I hurry over to where he's standing, intent on finding out why."
    bree.say "Hey!"
    bree.say "What's so damn funny?"
    "Scottie doesn't seem to be at all worried by the way I'm confronting him."
    "Instead he just keeps right on laughing the whole time."
    show scottie joke
    scottie.say "Ha, ha..."
    scottie.say "Oh man..."
    scottie.say "Isn't it obvious, [hero.name]?"
    show scottie happy
    bree.say "Actually no, it isn't!"
    show scottie joke
    scottie.say "I'm laughing at your dancing, [hero.name]..."
    scottie.say "It's like, the worst I've ever seen!"
    show scottie happy
    "I can feel my cheeks flushing red as Scottie makes fun of me."
    "And I can't help looking around to make sure nobody else hears him."
    bree.say "Scottie!"
    bree.say "That's not very nice."
    "Scottie shrugs off my complaint."
    "And I can see that he's not in the slightest bit sorry too."
    show scottie joke
    scottie.say "You know, [hero.name]..."
    scottie.say "I'm being totally honest here."
    scottie.say "And you should to grateful for that."
    show scottie normal
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
