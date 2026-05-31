label lexi_after_dance_success_with_female:
    show lexi normal nophone
    lexi.say "[hero.name]!"
    lexi.say "Hey, [hero.name]!"
    show lexi smile
    "I hear the sound of Lexi calling my name as I'm dancing."
    "And so I stop, walking over to where she's standing."
    bree.say "Oh..."
    bree.say "Hey, Lexi..."
    bree.say "What's up?"
    bree.say "Did you want to come dance with me?"
    "Much to my delight, Lexi nods her head with enthusiasm."
    show lexi normal
    lexi.say "I'd love to, [hero.name]!"
    lexi.say "You've got some really sweet moves."
    show lexi smile
    "I can feel myself starting to blush as Lexi praises me."
    "But I'm feeling a little word out from my efforts."
    "And so I hold my hands up in a gesture of surrender."
    bree.say "Okay, but in a little while."
    bree.say "I need a chance to rest."
    "Lexi looks more than a little disappointed."
    "But she nods her head and follows me as I walk off."
    show lexi normal
    lexi.say "Just don't leave it too long, okay?"
    lexi.say "I want you to teach me some of those moves!"
    return

label lexi_after_dance_failure_with_female:
    show lexi normal nophone
    lexi.say "[hero.name]!"
    lexi.say "Hey, [hero.name]!"
    show lexi smile
    "I hear the sound of Lexi calling my name as I'm dancing."
    "And so I stop, walking over to where she's standing."
    bree.say "Oh..."
    bree.say "Hey, Lexi..."
    bree.say "What's up?"
    bree.say "Did you want to come dance with me?"
    "Much to my surprise, Lexi shakes her head at this."
    show lexi sadsmile
    lexi.say "Nah, [hero.name]..."
    lexi.say "I came over to ask you to stop dancing."
    show lexi sad
    "Again I'm surprised."
    "But this time by what Lexi just said to me."
    bree.say "Are you serious?"
    bree.say "You really want me to stop dancing?"
    "This time Lexi nods."
    show lexi sadsmile
    lexi.say "Yeah, [hero.name]..."
    lexi.say "Thing is, you're really bad at it."
    lexi.say "And you're totally embarrassing me right now."
    show lexi sad
    bree.say "I am?!?"
    show lexi normal
    lexi.say "Oh yeah..."
    lexi.say "We're talking wishing the ground would open and swallow me up level embarrassment!"
    show lexi smile
    "I can feel myself starting to blush as Lexi lays it on thick."
    "And after that, I don't feel like there's anything else I can say or do."
    "So I nod and then shuffle away, feeling totally humiliated."
    show lexi normal
    return

label lexi_halloween_invitation_female:
    show lexi
    "Almost the moment I agreed to the Halloween party, I knew who I wanted to invite."
    "I can't imagine a party at the house without someone inviting Lexi along."
    "She's always the life and soul of any party she goes to."
    "And if there isn't one, then she turns what's going on into one!"
    "Plus there's the added bonus that this is a costume party."
    "And well, I kinda want to see what she comes dressed as."
    "Because she's so outrageous the rest of the time."
    "Imagine what that fertile imagination of hers could come up with!"
    "If it'd been anyone else, I'd have put some serious thought into what I'd say."
    "But I get the feeling that Lexi's the kind of girl who appreciates the direct approach."
    "And I'm sure she's more than up for having some fun on Halloween."
    "So as soon as I get the chance, I just come straight out and ask her."
    show lexi at center, zoomAt(1.5, (640, 1040)) with fade
    bree.say "Hey, Lexi..."
    bree.say "We're throwing a Halloween party at my place."
    bree.say "Would you like to come along?"
    "Lexi cocks her head on one side as she listens to my pitch."
    "And I can from the look in her eyes that she's interested."
    lexi.say "A proper Halloween party?"
    lexi.say "Like with spooky shit?"
    lexi.say "Bobbing for apples and all that crap?"
    "I'm nodding and smiling as Lexi asks all of her questions."
    "Willing to agree to almost anything in order to get her on board."
    bree.say "Exactly that, Lexi..."
    bree.say "It's a costume party too."
    bree.say "So you'd need to dress-up."
    bree.say "I kind of wanted you to come as..."
    bree.say "Well, to come as my date!"
    if lexi.love >= 100:

        show lexi happy
        "Lexi wrinkles up her nose as she smiles at me."
        "And then, much to my delight, she nods her head."
        lexi.say "You know what, [hero.name] - that sounds kinda fun!"
        lexi.say "I haven't been to a party like that since I was a kid."
        bree.say "This one's going to be even better, Lexi."
        bree.say "Because it's for grown-ups!"
        "Lexi keeps on smiling as she nods at this."
        "And I can see that the idea's growing on her the whole time."
        lexi.say "And you said it's a costume party too, right?"
        bree.say "Yeah, Lexi."
        bree.say "Everyone's dressing-up for the occasion."
        lexi.say "That's great!"
        show lexi flirt
        lexi.say "Because I've got one I've been itching to wear for ages."
        lexi.say "I was just waiting for the chance to bust it out."
        lexi.say "And trust me - you're gonna freak when you see it!"
        "By now I'm nodding and smiling too, eager to encourage Lexi."
        "And I feel like pinching myself to see if I'm actually awake."
        "Not only is Lexi coming to the party, just like I wanted."
        "But she's also promising to blow my mind with her costume!"
        "I must be dreaming, because doesn't get any better than this."
        $ game.flags.halloween_girl = "lexi"
    else:

        show lexi sad
        "Lexi takes me by surprise when she wrinkles up her nose and shakes her head."
        lexi.say "Nah, I think I'll pass."
        lexi.say "That sounds kinda lame, [hero.name]."
        lexi.say "I usually do something pretty wild on Halloween."
        "For a moment I'm left stunned and unsure of what to say."
        "I was so desperate for Lexi to agree to come to the party."
        "My head just isn't ready to handle rejection right now."
        "I guess I should have made a better pitch to her."
        bree.say "Oh..."
        bree.say "Okay, Lexi."
        bree.say "I mean, if you already have plans..."
        "Lexi nods happily at this, not in the least bit concerned for my feelings."
        "It also seems she's not the least bit worried about letting me down."
        lexi.say "Yeah, I'm kind of a creature of habit."
        lexi.say "Say, why don't you sack off the party too?"
        lexi.say "We could do something together on Halloween."
        lexi.say "And I promise you'll have more fun with me!"
        bree.say "Erm..."
        bree.say "That's an intriguing offer, Lexi."
        bree.say "I'm going to need some time to think it over."
    return

label lexi_halloween_arrival_female:
    scene bg house
    "Opening the door, I stagger back instantly."
    "And that's because there's an actual chainsaw right in front of my face!"
    lexi.say "HAPPY HALLOWEEN!"
    "Lexi's face appears over the blade of the chainsaw."
    "A crazy smile spreading beneath her wide eyes."
    "She seems to be dressed in a crazy cheerleader's uniform."
    "And it takes me a moment to recognise it."
    "Maybe because of the chainsaw in my face!"
    bree.say "Lollipop Chainsaw!"
    lexi.say "Got it!"
    lexi.say "Well, [hero.name], I'm waiting."
    lexi.say "What do you think of my costume?"
    "Now I finally have the chance to check Lexi out."
    "And I take a deep breath as I do so."
    "Because I want to be able to tell her exactly what I think."
    menu:
        "Compliment":
            bree.say "Wow, Lexi...!"
            bree.say "You look SO hot!"
            "Lexi almost purrs at the compliment."
            "So I guess that's what she wants to hear."
            lexi.say "Yeah, I thought it'd pop you."
            lexi.say "You being a massive game-geek and all that!"
            bree.say "Oh this is so frustrating!"
            bree.say "I've got to be the host tonight."
            bree.say "But I so want to spend some time alone with you!"
            "Lexi lets out the dirtiest laugh I ever heard."
            "And she nods her head in a conspiratorial manner."
            lexi.say "Oh, don't, worry, [hero.name]."
            lexi.say "My skirts real short and my panties are real high."
            lexi.say "You could slip something in there without anyone noticing!"
            "With that, she turns and walks away."
            "Leaving me to hurry after her."
            "Already wondering when the chance to be alone with her will arise."
        "Criticize":
            bree.say "Er..."
            bree.say "It's really great, Lexi."
            bree.say "A really great costume."
            "Lexi squints at me, almost sneering."
            "It's clear that wasn't the answer she wanted."
            lexi.say "Huh?"
            lexi.say "It's nice - is that all?"
            lexi.say "I thought you were a game-geek?!?"
            bree.say "I...I am, Lexi."
            bree.say "It's just that...that game's getting old now."
            bree.say "And it's been ages since I played it!"
            "Lexi's eyes go wide and her mouth drops open."
            "Then she plants her balled fists on her hips."
            lexi.say "Is that so?"
            lexi.say "Well, you know what never gets old, [hero.name]?"
            lexi.say "Tits and ass - that's what!"
            lexi.say "Let's see what the other guys and girls at the party think of my costume!"
            "Lexi storms past me in a huff."
            "And I hurry after her, cursing my big mouth the whole time."
    return

label lexi_halloween_party_female:
    $ game.pass_time(2)
    scene bg livingroom
    show lexi halloween
    with dissolve
    lexi.say "Hey, [hero.name]!"
    lexi.say "You want another of these?!?"
    "I turn around just in time to catch Lexi as she tumbles into me."
    "She's waving around her empty up and pointing towards the punch-bowl."
    "How many of those has she had already?"
    "She looks like she's about to fall flat on her face!"
    bree.say "Are you okay, Lexi?"
    bree.say "You look totally wasted!"
    "Lexi makes a visible effort to stand up straight."
    "But she's still wobbling around the whole time."
    lexi.say "I'm okay..."
    lexi.say "In fact..."
    lexi.say "I'm better than okay!"
    menu:
        "Indulge Lexi":
            "Ah, what the hell am I worrying about?"
            "This is supposed to be a party."
            "Who cares if Lexi wants to let her hair down."
            bree.say "Here, Lexi."
            bree.say "Let me get you another."
            "Lexi beams at me as I ladle the punch into her glass."
            "And then she drinks more than half of it straight off."
            lexi.say "Yeah..."
            lexi.say "Now that's what I'm talking about!"
            "She sways and falls into me again."
            "Snorting and giggling as I have to hold her up."
        "Chastise Lexi":
            "For god's sake - she's practically on her ass!"
            "Lexi's going to be unconscious before too long."
            "I take the empty glass out of her hand."
            lexi.say "Hey!"
            lexi.say "What the hell?!?"
            bree.say "I think you've had enough, Lexi."
            bree.say "At least until you sober up a little."
            "Lexi protests and tries to snatch back her glass."
            "But all she succeeds in doing is overbalancing."
            "She sways and falls into me again."
            "Snorting and giggling as I have to hold her up."
    return

label lexi_halloween_dance_female:
    $ game.pass_time(2)
    scene bg livingroom
    show lexi halloween
    with dissolve
    "The moment that a certain track starts to play, I can see Lexi's foot tapping."
    "We're supposed to be having a conversation, but it's clear her mind's elsewhere."
    "And I can see that she's itching to get out onto the makeshift dance-floor."
    "But I was right in the middle of trying to talk to her."
    "So I can't help feeling a little put out."
    bree.say "Erm..."
    bree.say "Am I boring you, Lexi?"
    lexi.say "Huh...what?"
    lexi.say "Well...yeah, I suppose so!"
    lexi.say "Screw the chit-chat, [hero.name]."
    lexi.say "I wanna dance!"
    "Well, at least she's honest."
    menu:
        "Accept":
            bree.say "You're right, Lexi."
            bree.say "This is supposed to be a party."
            "Lexi's face lights up as I give her answer she wants to hear."
            "But I don't have time to say another word."
            "As by now she's taken hold of my hand."
            "And I'm already being dragged the dance-floor."
            lexi.say "Oh yeah."
            lexi.say "Now that's what I'm talking about!"
            "Of course, I'm not going to be treated to a slow-dance."
            "And Lexi makes that apparent right from the start."
            "I don't think there's even a moment she's not rubbing against me!"
            "Lexi gyrates and grinds the whole time, never letting up."
            "It's all that I can do to keep from blushing."
            "But that doesn't mean I want her to stop."
            "I can almost feel the eyes of the other guests on us."
            "As Lexi dances like a stripper in a gentleman's club."
            "By the time the song ends, I'm panting and exhausted."
            "And my heart is beating so loud I swear you can hear it over the music!"
        "Refuse":
            bree.say "Not now, Lexi."
            bree.say "There's plenty of time for that later."
            "Lexi looks instantly disappointed with my answer."
            "She crosses her arms over her chest and frowns."
            lexi.say "Aww, come on!"
            lexi.say "Don't be a boring cunt!"
            bree.say "I already said no, Lexi!"
            "Lexi shrugs and shakes her head."
            lexi.say "Alright, suit yourself."
            lexi.say "I'll dance by myself if I have to!"
            "Before I can protest, Lexi's gone."
            "I watch her hit the dance-floor alone."
            "But it doesn't take long for that to change."
            "And I have to watch as Sasha and [mike.name] join her."
            "Then she manages to rope in Scottie and Jack too!"
            "All four of them seem to be drawn into her orbit."
            "And Lexi doesn't hesitate to flaunt herself in front of them either."
            "The whole time she must be aware of me watching her too."
            "But all I can do is stand there helplessly as she humiliates me."
    return

label lexi_halloween_sex_female:
    scene bg livingroom
    show lexi smile halloween nophone
    with fade
    "It's getting late by now, and the party seems to be winding down."
    "Most of the guests are tired and more than a little drunk."
    "And they seem more interested in chilling out than being wild."
    "Well, all except for one of them."
    "Lexi shows no signs of burning out just yet."
    "In fact, she seems to be in the mood for a bit of exercise."
    show lexi normal
    lexi.say "Come on, [hero.name]..."
    lexi.say "Move your ass!"
    show lexi smile
    bree.say "O...okay, Lexi..."
    bree.say "I'm coming!"
    "Lexi has a firm grip on my wrist, dragging me after her."
    show bg bathroom at center, zoomAt(1.0, (640, 720))
    show lexi halloween at center, zoomAt(1.0, (640, 720))
    with fade
    "And she's making for the upstairs bathroom."
    "Which, as luck would have it, is unoccupied."
    "In fact, I shudder to think what would have happened if someone were already in there!"
    show bg bathroom at center, traveling(1.5, 0.3, (640, 1040))
    show lexi halloween at center, traveling(1.5, 0.3, (640, 1040))
    with hpunch
    "With a show of strength that's a little scary, Lexi all but tosses me inside."
    bree.say "Lexi..."
    bree.say "Slow the hell down!"
    bree.say "You really need to go that badly?!?"
    play sound door_slam
    show lexi happy at startle
    "Lexi slams the door behind us, laughing as she does so."
    "And then she pretty much spins around on the spot."
    "I can't help gulping and backing off a little."
    "Because there's just something about her posture and the look on her face."
    "I'm instantly put in mind of something from a wildlife documentary."
    "It reminds me of the way a predator stares down it's prey."
    show lexi normal
    lexi.say "Oh, I need something alright."
    lexi.say "But it's not that."
    show lexi smile
    bree.say "Erm..."
    bree.say "Then what is it, Lexi?"
    "Like I don't already know!"
    show lexi normal
    lexi.say "Your tongue, [hero.name]..."
    lexi.say "I want it inside my pussy!"
    show lexi smile
    bree.say "You...you could have just asked, Lexi!"
    bree.say "No need to do it in private."
    bree.say "I...I mean asking for it - not doing it!"
    bree.say "Come on, let's go to my room."
    "My hand is already on the door, opening it perhaps an inch."
    "But Lexi slams the palm of her own hand into it, slamming it shut again."
    "I jump in surprise, looking at her wide-eyed and puzzled."
    show lexi normal
    lexi.say "No way!"
    lexi.say "I want it NOW!"
    scene bg black
    show lexi fingering bree bathroom halloween with hpunch
    "Before I can say as much as a word, Lexi jumps on me."
    "And I don't mean that metaphorically either."
    show lexi fingering bree closed
    "She literally leaps off her feet and pounces on me!"
    "I struggle to keep from falling over."
    "And in doing so I turn and tumble against the door."
    "But don't get me wrong - I'm not trying to get Lexi off of me!"
    "What do you think I am, insane?!?"
    "No, I'm trying to keep her aloft while tugging at my costume!"
    "I have no clue how she manages it."
    "But a moment later, I feel Lexi's hand in my underwear."
    show lexi fingering bree pleasure
    lexi.say "Ah!"
    lexi.say "There it is..."
    "And the next thing I know, she's stroking between my thighs."
    "Lexi uses her fingers with astonishing expertise."
    "And I can't help gasping as she begins to work my pussy."
    lexi.say "Oh..."
    lexi.say "Mmm...yeah...yeah..."
    lexi.say "That's it...that's what I want!"
    show lexi fingering bree ahegao
    "That's good to hear - because it's what I want too!"
    "Suddenly I'm not feeling tired anymore."
    "And I couldn't care less about occupying the bathroom either."
    "All I want to do is have Lexi keep on playing with me."
    "And that's just what I set to doing."
    scene bg black
    show bree licking lexi halloween bathroom
    with fade
    "But then I feel her taking hold of the back of my head."
    "The next thing I know, Lexi's forcing it down and into her groin."
    "And I remember what she said about my tongue and where she wanted it."
    "I figure that giving Lexi what she wants is the best way to get what I want too."
    "So I don't hesitate to get down to it, exploring her lips with my tongue."
    show bree licking lexi at startle(0.2, -15)
    "I keep on probing, pushing into her pussy as much as I possibly can."
    "She nods and demands more each and every time I do so."
    show bree licking lexi at startle(0.2, -15)
    "The force of my tongue only seems to make her that much more excited."
    show bree licking lexi closed
    "Pretty soon I can hear what sound like muffled voices outside."
    show bree licking lexi at startle(0.2, -15)
    "Which is understandable, as we're at it so noisily!"
    play sound door_banging
    "And then a fist starts pounding on the other side of the door."
    "Any other time I'd have been mortified."
    show bree licking lexi at startle(0.2, -15)
    "But right now I'm lips deep in Lexi."
    show bree licking lexi pleasure with vpunch
    "And I'll be damned if I'm pulling out before I make her cum!"
    "Luckily for me, Lexi seems to have been desperate for it."
    show bree licking lexi closed with hpunch
    "Pushed by her pelvis, my head bangs against the door over and over again."
    show bree licking lexi pleasure
    "And pretty soon I can hear her crying out."
    "She's loving this - she's such a dirty little bitch!"
    "Finally Lexi begins to quiver and shake."
    show bree licking lexi closed with vpunch
    "I swear I can actually feel her going weak at the knees too."
    "At the same time she pushes me over the edge."
    "Waves of pleasure spreading out through my entire body."
    "The door's the only thing that stops us collapsing into a pile on the floor."
    "But somehow we still manage to stand up and begin to sort ourselves out."
    "That's why, as soon as we're half-decent, I can't stop her opening the door."
    scene bg black
    pause 0.2
    scene bg secondfloor
    show scottie halloween angry
    with wiperight
    "This reveals Scottie, standing with his legs crossed."
    scottie.say "Not cool, guys."
    scottie.say "Not cool at all."
    scottie.say "If I piss myself in this thing, I lose my deposit!"
    bree.say "Ah, sorry, Scottie..."
    bree.say "You do know there's a bathroom downstairs, right?"
    lexi.say "What's the matter, fish-boy?"
    lexi.say "I though Aquaman was supposed to be wet?"
    $ lexi.sexperience += 1
    $ game.pass_time(1)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
