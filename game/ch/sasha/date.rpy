label sasha_date_intro_valentine_male:
    sasha.say "Happy Valentine's day, [hero.name]."
    sasha.say "And I just wanna say..."
    sasha.say "I'm really glad you're my valentine!"
    "I nod eagerly at Sasha's words."
    mike.say "Me too, Sasha, me too!"
    mike.say "I can't think of anyone I'd rather have as my valentine!"
    return

label sasha_date_intro_halloween_male:
    sasha.say "I was gonna really goth it up tonight, [hero.name]."
    sasha.say "But then I thought, everyone's going to be doing that, yeah?"
    "I can't help looking puzzled as Sasha says all of this."
    mike.say "Why's that, Sasha?"
    sasha.say "Erm...because it's Halloween?"
    "I slap my forehead and groan."
    mike.say "Oh man, I totally forgot!"
    sasha.say "Ah, don't worry about it, [hero.name]."
    sasha.say "I can be dark enough for the both of us!"
    return

label sasha_date_intro_christmas_male:
    mike.say "Happy Christmas, Sasha!"
    sasha.say "Happy Christmas, [hero.name]!"
    "Sasha leans into me, smiling and laughing."
    "And the feeling of her doing so makes me feel perfectly happy."
    sasha.say "So what are we waiting for?"
    sasha.say "Let's go have some festive fun!"
    return

label sasha_date_intro_birthday_male:
    mike.say "Happy birthday, Sasha!"
    mike.say "I'm going to take you on the best date ever."
    mike.say "The birthday girl deserves to have a great time!"
    sasha.say "Aw...thanks, [hero.name]!"
    sasha.say "But you'd better be able to back that up."
    sasha.say "Because I won't be holding back!"
    return

label sasha_date_intro_mc_birthday_male:
    sasha.say "Happy birthday, [hero.name]!"
    sasha.say "We're going to have an awesome date tonight, okay?"
    mike.say "Sure thing, Sasha!"
    mike.say "And thanks for remembering the date."
    mike.say "It really makes me feel special."
    sasha.say "Aww...aren't you adorable!"
    sasha.say "But what are we standing around here talking for?"
    sasha.say "Let's go party already!"
    return

label sasha_date_eat_a_burger:
    "I see Sasha taking a couple of bites out of her burger for sure."
    "But she seems to be intent on using her mouth more for other purposes."
    "In all the time we're eating, I don't think she stops talking even once."
    return

label sasha_date_buy_drink:
    if sasha.is_visibly_pregnant:
        show sasha angry
        $ sasha.love -= 10
        sasha.say "What the..."
        sasha.say "Are you taking the piss or what?"
        sasha.say "Did you forget that I'm bloody pregnant?!?"
        $ hero.cancel_activity()
        hide sasha
    else:
        "Sasha seems to loosen up and crack a smile almost the same moment she has a drink in her hand."
        "Not that I'm suggesting she spends most of her time being moody, of course."
        "She just comes over as happier in general."
    return

label sasha_date_play_darts:
    "It's pretty clear that Sasha doesn't want to play darts."
    "And she isn't about to try and hide it, either."
    "She hardly makes an effort to play, and keeps on yawning the whole time."
    return

label sasha_date_pub_play_pool:
    "At the mere suggestion that we play pool, Sasha's up and over to the table in the blink of an eye."
    "As she leans over the table to take her first shot, she eyes me in an almost threatening manner."
    "Which makes me wonder if she's actually a secret pool shark and I'm going to be her next meal!"
    return

label sasha_date_buy_a_round:
    if sasha.is_visibly_pregnant:
        show sasha angry
        $ sasha.love -= 10
        sasha.say "What the..."
        sasha.say "Are you taking the piss or what?"
        sasha.say "Did you forget that I'm bloody pregnant?!?"
        $ hero.cancel_activity()
    elif (hero.charm >= 60 - sasha.love and sasha.flags.drinks < 2):
        show drink sasha
        "Sasha smiles and thanks me almost before I've said that I'll get the next round."
        "It's not like she's expecting me to pay for her drinks all night either."
        "But much more like we're mates hanging out, drinking and having a laugh together."
        $ game.active_date.score += 5
        if "rebel" in sasha.traits:
            $ game.active_date.score += 5
        $ sasha.set_flag("drinks", 1, "day", mod="+")
        hide drink
    else:
        "I want to pay a round of beers to the whole pub."
        "But Sasha doesn't seem to want to drink, so I refrain from doing so."
        $ hero.cancel_activity()
    return

label sasha_dance_with:
    "Every ounce of Sasha's dark, sensual side seems to come out once she's on the dance-floor."
    "She leans in close against me and fixes me with smokey, seductive eyes."
    "All I want to do is pull her ever closer to me as we move in time to the music."
    return

label sasha_date_play_arcade_intro_male:
    sasha.say "Ahh..."
    sasha.say "I'm not too sure about this, [hero.name]."
    sasha.say "Videogames have never really been my thing!"
    "I tear my attention away from the lights and sounds of the arcade for a moment."
    "Long enough to shake my head at Sasha's confession, finding it hard to believe."
    mike.say "I thought you'd be into them, Sasha."
    mike.say "I mean, you're into some pretty dark, hardcore stuff."
    mike.say "And videogames are full of that!"
    "Sasha frowns and looks at me sideways."
    "I'm not sure she quite agrees with my description of her interests."
    mike.say "Just give it a chance, Sasha."
    mike.say "That's all I'm asking, yeah?"
    "Sasha stays quiet, but she gives me a slight nod."
    "Which I take as permission to start looking for a suitable game."
    "And then my eyes settle on what could be the perfect choice."
    mike.say "'Ghasts and Ghoulies'!"
    mike.say "That's perfect, Sasha, trust me!"
    "I'm already pumping coins into the slot as Sasha walks over."
    "And as soon as I'm done, we start playing."
    return

label sasha_date_play_arcade_win_male:
    "Sasha seems to get into the game pretty quickly."
    "The cartoonish graphics and sounds drawing her in."
    "But things soon take a downward turn."
    "And that's as the toughness of the game starts to bite."
    sasha.say "Geez..."
    sasha.say "This thing just seems to keep getting harder!"
    sasha.say "Is it supposed to do that, [hero.name]?"
    mike.say "Yeah, Sasha, it is."
    mike.say "That's one of the coolest things about the game!"
    "I don't think my explanation does much to help matters."
    "And the fact that I'm pretty good at this game doesn't either."
    "Sasha keeps on dying while I waltz through the same levels."
    "And by the time we're done, she's been left far behind."
    sasha.say "Urgh..."
    sasha.say "Am I ever glad that's over!"
    mike.say "How can you say that, Sasha?"
    mike.say "I was having a blast!"
    sasha.say "Yeah, well..."
    sasha.say "Sorry to bring you down!"
    sasha.say "But can we go do something else already?"
    mike.say "I...I guess so, Sasha."
    mike.say "Maybe we can try again another time..."
    return

label sasha_date_play_arcade_lose_male:
    "I was expecting the notorious difficulty of the game to take its toll."
    "That it might make the game too hard for Sasha to be able to beat me."
    "But she's so into the game that she just doesn't seem to notice!"
    sasha.say "This is actually pretty cool, [hero.name]!"
    sasha.say "It's like filled with horrible stuff."
    sasha.say "But it's cartoonish too."
    sasha.say "I'd love to have some of these things on a T-shirt!"
    mike.say "Ah, yeah, Sasha..."
    mike.say "But what about the actual game?"
    mike.say "What do you think about that?"
    "I really should have spent more time playing this game."
    "Because it's bad enough that Sasha's not actually interested in playing it."
    "But she's somehow proving to be better at it than me!"
    mike.say "Urgh..."
    mike.say "Am I ever glad that's over!"
    sasha.say "How can you say that, [hero.name]?"
    sasha.say "I was having a blast!"
    mike.say "Yeah, well..."
    mike.say "Sorry to bring you down!"
    mike.say "But can we play something else already?"
    sasha.say "I guess so, [hero.name]."
    sasha.say "So long as we can come back to this one later!"
    return

label sasha_dick_reactions:
    if not sasha.flags.seendick:
        $ sasha.flags.seendick = 1
        if hero.has_skill("hung"):
            show dick reactions sasha scared
            sasha.say "Where did that thing come from, [hero.name]?"
            sasha.say "It's fucking huge!"
            mike.say "Who's fault do you think that is, Sasha?"
            show dick reactions sasha tasty
            sasha.say "Well, I better do something about it then..."
            $ sasha.sub += 10
        elif hero.has_skill("smalldick"):
            show dick reactions sasha mock
            sasha.say "Is that all I'm getting out of you?"
            mike.say "I...I guess so - sorry!"
            show dick reactions sasha smile
            sasha.say "Don't apologise, [hero.name] - size isn't everything."
            show dick reactions sasha tasty
            sasha.say "Come over here and let me show you what I mean..."
            $ sasha.sub -= 10
        hide dick reactions
    return

label sasha_peeping_scene_male:
    "I wouldn't normally stop at the sound of running water in the bathroom."
    "Because that's nothing out of the ordinary, now is it?"
    "But on this occasion, the door's been left ajar."
    "Now I admit that I've thought about my housemates showering from time to time."
    "Living with a couple of hot girls - who wouldn't?"
    "And so I can't help sneaking a peak around the door."
    "Steam is already starting to fill the bathroom up."
    "It's spilling out of the shower cubicle and obscuring everything."
    "Well, apart from the outline of Sasha herself!"
    "She's standing under the shower-head, busy washing herself."
    "It's a pretty mundane task, just an everyday thing."
    "But the way she's framed by the steam, her naked body..."
    "Well, it's like watching something out of a Hollywood movie."
    "Or maybe like a movie with a more adult theme!"
    "All I can hear is the sound of the falling water."
    "And there's no way I can tear my eyes away from Sasha."
    "I might have spent time fantasising about this."
    "But the real thing is infinitely better."
    return

label sasha_peeping_reactions_male:
    if (sasha.love >= 150 or sasha.sub >= 50) and sasha.sexperience:
        show sasha naked
        "In fact, I'm so engrossed that I zone out completely."
        "And I don't even notice when Sasha turns to look right at me!"
        "For a moment I hold my breath, waiting for the inevitable tirade of abuse."
        show sasha happy
        "But then I see a smile spread across Sasha's face and she shakes her head."
        show sasha shout
        sasha.say "I see you there, [hero.name]!"
        sasha.say "I see you watching me!"
        sasha.say "You want me to put on a show, yeah?"
        show sasha normal
        "Now it's my turn to nod."
        "My head bobs up and down without a single conscious thought."
        "Sasha chuckles, the look in her eye knowing."
        "She's got me hooked, and she knows it too!"
        hide sasha
        $ sasha.love += 1
        $ sasha.sub += 1
        show peeping sasha
        "What follows is an experience that I'll never forget."
        "It could have lasted a couple of minutes or gone on for an hour."
        "But there's no way for me to tell."
        "All I can remember is the way that Sasha's hands move."
        "Caressing each and every part of her body before me."
        "I'm treated to the sight of her twisting and turning."
        "The water from the shower head cascading over her naked body."
        "In no time at all, my cock is painfully hard."
        "And what makes it harder is the fact Sasha knows exactly what she's doing to me."
        "She knows just how much I'm lusting after her body right now, wanting her so badly."
        "But she's out of reach, tempting me with what I know I can't have."
        "Before she's finished, I can't take it anymore."
        "And I hurry away to the safety of my room."
        "My cock still hard and the memory of what I've seen fresh in my mind."
        hide peeping
    else:
        show sasha naked
        "In fact, I'm so engrossed that I zone out completely."
        "And I don't even notice when Sasha turns to look right at me!"
        "She's out of the shower and wrapping a towel around herself."
        "Yelling at me while I'm still trying to get my brain in gear."
        show sasha naked vangry
        sasha.say "WHAT THE HELL?!?"
        show sasha angry
        sasha.say "Were you...were you...were you..."
        sasha.say "You were watching me in the damn shower!"
        show sasha upset
        "Suddenly reality rushes back in around me."
        "I snap out of it and stand up straight."
        mike.say "Wha...what?!?"
        mike.say "No, no, no..."
        mike.say "I was...I was just checking..."
        mike.say "To...to see if the bathroom was free!"
        show sasha naked vangry
        sasha.say "Bullshit, you were ogling me in the shower!"
        show fx anger
        sasha.say "Get the hell out of my sight, [hero.name]!"
        sasha.say "Or else I'll give you a sex-change with my nail-clippers!"
        show sasha upset
        $ sasha.love -= 20
        $ sasha.sub -= 10
        "I don't need to be told twice, or threatened with more violence."
        "Turning on my heel, I hurry away to the safety of my bedroom."
        "Maybe a good night's sleep will make everything better."
        "And maybe Sasha will have cooled off in the morning too!"
    return

label sasha_halloween_invitation:
    show sasha
    "I know that I should be putting all of my energy into making sure the party is a success."
    "But there's a part of me that keeps getting hung up on who exactly Sasha's going with."
    "Yeah, yeah - I know that none of us are technically 'going' to our own Halloween party."
    "Yet I can't keep from wanting to know that Sasha and I will be there as a couple."
    "Maybe I'm paranoid, but I can't stand the idea of her going off with another guy!"
    "It took time and effort to get this far with her."
    "And I kind of want to enjoy being with her whenever I can!"
    "So as soon as I know that [bree.name]'s out of the way, I ask the question."
    mike.say "Ah, Sasha..."
    sasha.say "Hmm..."
    show sasha shout
    sasha.say "Yeah, [hero.name]?"
    sasha.say "What's bugging you?"
    show sasha normal
    "I can't keep myself from sounding spooked."
    "Seriously - how does she always know there's something on my mind?"
    mike.say "Bugging me?"
    mike.say "Who said there was anything bugging me?"
    "Sasha chuckles and shakes her head."
    show sasha shout
    sasha.say "You're pretty transparent, [hero.name]!"
    sasha.say "But don't get caught up on it."
    sasha.say "Just tell me what's the matter."
    show sasha normal
    "I try as best I can to shake it off."
    mike.say "Okay, Sasha, okay..."
    mike.say "It's the Halloween party."
    mike.say "We're going to be there together, right?"
    show sasha shout
    sasha.say "Yeah, [hero.name], you, me and [bree.name]."
    sasha.say "How else can we host it?"
    show sasha normal
    mike.say "No, no, no..."
    mike.say "I mean we're going to be there as couple, you and me."
    mike.say "Like officially we're the hosts, but you're my date and I'm yours."
    show sasha annoyed
    if sasha.love >= 100 or sasha.is_sex_slave or Harem.together(bree, sasha, name='home'):
        "Sasha looks thoughtful for a moment."
        show sasha normal
        $ sasha.love += 1
        "And then she nods her head."
        show sasha shout
        sasha.say "I don't see why not."
        sasha.say "We're all going to be busy hosting on the night."
        sasha.say "But if we get the chance to have fun, we can do it together!"
        show sasha normal
        "I find myself instantly nodding and smiling."
        "That's just the answer I was hoping for!"
        mike.say "That's great, Sasha!"
        mike.say "I'm sure we'll be able to do that."
        show sasha shout
        sasha.say "Well, let's just see how things go, yeah?"
        show sasha joke
        sasha.say "But I promise you this, [hero.name]..."
        sasha.say "We'll make some time so sneak away from the party."
        sasha.say "Then we can have a little fun on our own!"
        show sasha normal
        "Wow..."
        "This just keeps getting better and better!"
        $ game.flags.halloween_girl = "sasha"
    else:
        "Sasha wrinkles up her nose and shakes her head."
        show sasha shout
        sasha.say "Yeah, [hero.name], I get what you mean."
        sasha.say "But you're really over-thinking this."
        sasha.say "We're going to have our hands full hosting the party."
        show sasha normal
        mike.say "You don't have to do anything, Sasha."
        mike.say "Just remember that we're together the whole time!"
        "Sasha puts a hand on my arm."
        show sasha annoyed
        "But at the same time she shakes her head again."
        show sasha shout
        $ sasha.sub -= 1
        sasha.say "Look, just let it go, [hero.name]."
        sasha.say "We're going to have plenty of time to do couple stuff."
        sasha.say "But you'll ruin the party if you get hung-up like this."
        show sasha normal
        mike.say "If you say so, Sasha..."
        show sasha shout
        sasha.say "I do!"
        show sasha normal
        "I force a smile onto my face."
        "Seeing this, Sasha winks at me."
        show sasha joke
        sasha.say "And don't worry, [hero.name]."
        sasha.say "I'll make it up to you when the party's over!"
        show sasha normal
        "At that, my smile becomes a real."
        "Maybe there's going to be an upside to this after all?"
    return

label sasha_halloween_arrival:
    scene bg house
    "I stare at the door for a moment longer, and then I strike myself on the forehead."
    "Of course, Sasha lives here too."
    "So my date's already in the house!"
    "Geez, I must have scrambled my brain putting so much effort into the party."
    scene bg livingroom
    show sasha halloween joke
    "But the same can't be said for Sasha, as she looks at me expectantly."
    show sasha shout
    sasha.say "Well, [hero.name], I'm waiting."
    sasha.say "What do you think of my costume?"
    show sasha normal
    "I look Sasha up and down one last time."
    "And then I take a deep breath."
    "All in preparation to tell her exactly what I think."
    menu:
        "Compliment":
            mike.say "I didn't want to say in front of the others."
            mike.say "But I love it, Sasha."
            mike.say "You look super hot!"
            show sasha happy
            $ sasha.love += 1
            "Sasha smiles at this, clearly liking the praise."
            sasha.say "Thanks, [hero.name]!"
            sasha.say "That's just the answer I was looking for."
            show sasha shout
            sasha.say "I know we're supposed to be the hosts tonight."
            sasha.say "But that doesn't mean we can't find time for each other."
            show sasha joke
            sasha.say "Time to have fun, you know?"
            show sasha normal
            "I nod eagerly at this."
            "My head already filling with possibilities."
            mike.say "Sure thing, Sasha."
            mike.say "Until then, I might have to keep staring at you."
            mike.say "Just to warn you, I don't think I'll be able to stop!"
        "Criticize":
            mike.say "Ah..."
            mike.say "I don't know, Sasha."
            mike.say "I mean...it looks like you worked really hard on it!"
            show sasha annoyed
            $ sasha.love -= 2
            "Sasha cocks her head on one side and narrows her eyes."
            "It looks like she doesn't know what to make of my answer."
            show sasha whining
            sasha.say "Erm..."
            sasha.say "Thanks...I guess!"
            sasha.say "I thought you might have been more into it than that!"
            show sasha annoyed
            "I can't help wrinkling up my nose as Sasha says this."
            "And I want to be as honest with her as I can."
            "Because maybe that way I won't hurt her feelings too much."
            mike.say "It's not the costume, Sasha."
            mike.say "That's great, really great."
            show sasha angry
            sasha.say "Then what is it?!?"
            show sasha annoyed
            mike.say "I think I like you better as a rock-chick, Sasha."
            mike.say "The whole goth thing..."
            mike.say "Well...it just doesn't do it for me!"
            "Sasha rolls her eyes and lets out a sigh."
            show sasha whining
            sasha.say "At least you're honest, [hero.name]."
            sasha.say "But that's kind of put a dampener on things for me!"
    scene bg black with dissolve
    pause 1
    return

label sasha_halloween_party:
    $ game.pass_time(2)
    scene bg livingroom
    show sasha halloween annoyed at left
    show scottie halloween blush at right
    with dissolve
    scottie.say "Whoa..."
    scottie.say "Sasha - you look SO hot!"
    show sasha shout
    sasha.say "Ah..."
    sasha.say "Thanks, Scottie, I guess..."
    show sasha normal
    "I turn around to see Scottie leaning in close to Sasha."
    "She has an awkward smile on her face."
    "And I can see that she's uncomfortable with the attention."
    show scottie perv
    scottie.say "No, seriously, Sasha."
    scottie.say "That's a real sexy look."
    scottie.say "Makes me sit up and pay attention!"
    "Sasha glances back over her shoulder at me."
    "And I guess she wants me to step in and rescue her."
    menu:
        "Defend Sasha":
            mike.say "That's close enough, Scottie."
            mike.say "Sasha doesn't need you drooling on her costume!"
            show scottie angry
            scottie.say "Wha...what?"
            scottie.say "I wasn't drooling - was I, Sasha?"
            scottie.say "We were just chatting, that's all."
            "I step forwards, putting myself between Scottie and Sasha."
            "I try not to make it an aggressive move."
            "But he still seems to get the message."
            show sasha shout
            $ sasha.sub += 1
            $ sasha.love += 1
            sasha.say "He's right, Scottie."
            sasha.say "I don't need to be able to smell your armpits!"
            show sasha normal
            "Scottie opens his mouth to say something."
            hide scottie
            hide sasha
            show sasha halloween normal
            "But then he nods and turns to walk away."
        "Defend Scottie":
            mike.say "Give the guy a break, Sasha."
            mike.say "He's just trying to pay you a compliment."
            show scottie -perv
            scottie.say "Yeah..."
            scottie.say "Yeah, that's right!"
            show sasha upset
            $ sasha.love -= 4
            "Sasha takes a step backwards."
            "She shakes her head like she can't understand my actions."
            show sasha vangry
            sasha.say "Y...you're fucking with me, right?"
            show sasha angry
            sasha.say "You have to be fucking with me!"
            show sasha upset
            mike.say "Geez, Sasha - lighten up."
            mike.say "This is supposed to be a party."
            mike.say "Don't take it so seriously!"
            "Sasha doesn't say anything."
            hide sasha
            "She just shakes her head and turns away from me."
    scene bg black with dissolve
    pause 1
    return

label sasha_halloween_dance:
    $ game.pass_time(2)
    scene bg livingroom
    show sasha halloween annoyed at left
    show scottie halloween at right
    with dissolve
    scottie.say "Aw, come on, Sasha!"
    scottie.say "It's only one dance - for old time's sake!"
    "I hadn't seen Scottie walk up to where Sasha I are standing."
    "And I only manage to catch his side of the conversation."
    "But it's not that hard to figure out what's going on."
    "Sasha is backing off from him, trying to put me between them."
    show sasha whining
    sasha.say "I already said no, Scottie."
    sasha.say "I want to hang out with [hero.name] tonight!"
    show sasha annoyed
    "Sasha looks at me for support."
    "And I can see that I'm going to have to step in here."
    menu:
        "Side with Sasha":
            mike.say "The lady already said no, Scottie."
            mike.say "I think you've had your answer."
            show scottie angry
            "Scottie opens his mouth to protest."
            "But I take a step forward, shaking my head."
            "He seems to get the message, and backs off."
            scottie.say "Okay, okay!"
            scottie.say "I don't need to be told twice!"
            hide scottie
            hide sasha
            show sasha halloween shout
            $ sasha.sub += 1
            $ sasha.love += 2
            sasha.say "Thanks for that, [hero.name]."
            sasha.say "I owe you one!"
            show sasha normal
            mike.say "How about you pay me back with a dance?"
            "Sasha gives me a smile and a nod."
            hide sasha
            show dance sasha halloween
            "And as soon as a song she likes comes on, we hit the dance-floor."
            "Sasha shows none of the reluctance to me that she had for Scottie."
            "The action is pretty much hot and heavy right from the start!"
            "She moves in time to the music, never more than an inch from me."
            "And I move in time with Sasha, all of my attention focused on her."
            "She really wasn't kidding when she said she wanted to be with me!"
        "Side with Scottie":
            mike.say "It's no big deal, Sasha."
            mike.say "I can spare you for one dance."
            show sasha upset
            $ sasha.love -= 4
            "Sasha's eyes go wide at this."
            "She clearly wasn't expecting that answer."
            show sasha vangry
            sasha.say "I...I don't..."
            show sasha upset
            scottie.say "You see, Sasha?"
            scottie.say "I told you it was no biggie!"
            hide scottie
            hide sasha
            "I watch as Scottie bundles her onto the makeshift dance-floor."
            "And it's only then that I begin to wonder of I made a mistake."
            "Sasha keeps on looking daggers at me the whole time."
            "She tries as best she can to keep her distance."
            "But Scottie seems determined to invade her personal space."
            "And when they're done, she storms away from him."
            "I suddenly feel uneasy as she approaches me."
            "If she's that mad with Scottie."
            "Then how angry is she going to be with me?"
    scene bg black with dissolve
    pause 1
    return

label sasha_halloween_sex:
    scene bg livingroom
    show sasha halloween
    with fade
    "It's getting pretty late by now and the party seems to be winding down too."
    "Everyone that's still here is either drunk, tired or both."
    "So the need for Sasha and I to play host is pretty much over for the night."
    "Which is great, because I feel like I spent the last of my energy already."
    "And all of it went on making sure that our guests had the best time possible."
    mike.say "Wow, Sasha..."
    mike.say "I'm done in!"
    "I was expecting Sasha to say the same."
    "But then I see she has a look of mischief in her eye."
    show sasha joke
    sasha.say "Oh no, [hero.name] - you're not off duty yet."
    sasha.say "There's one more person you have to entertain."
    show sasha normal
    mike.say "Aw, no way, Sasha."
    mike.say "Everyone's beat, look!"
    show sasha shout
    sasha.say "Not everyone, [hero.name]."
    show sasha flirt
    sasha.say "I've still got a little life left in me!"
    show sasha shy
    "With that, Sasha takes hold of my wrist."
    hide sasha
    "She drags me after her without asking permission."
    scene bg secondfloor
    show sasha halloween
    with fade
    "And when we're getting close to her bedroom, I can pretty much guess what she wants."
    mike.say "Okay, Sasha, okay."
    mike.say "I suppose I can manage that!"
    "Sasha gives me a wicked smile as she opens a door and slips inside."
    scene bg bedroom2
    show sasha halloween
    with fade
    "But it's only when I follow her through that I see why she's grinning."
    mike.say "W...wait a minute, Sasha."
    mike.say "This is [bree.name]'s room!"
    show sasha surprised
    "At this, Sasha claps her hands on her cheeks in mock horror."
    sasha.say "Oh no, how did we end up in here?!?"
    show sasha joke
    sasha.say "Come on, [hero.name], lighten up!"
    sasha.say "It's Halloween, so let's have fun."
    show sasha flirt
    sasha.say "Let's fuck in [bree.name]'s!"
    show sasha shy
    mike.say "B...but why?!?"
    show sasha joke
    "By way of answer, Sasha presses herself against me."
    "She massages my cock at the same time too."
    "And I can already feel myself getting hard."
    show sasha shout
    sasha.say "Because I want to live dangerously, [hero.name]."
    show sasha flirt
    sasha.say "And because I want your cock inside me while I do!"
    sasha.say "Come on, come one - I'm REALLY horny right now!"





    show sasha stand halloween bedroom2 with fade
    "We're standing in front of the full-length mirror in [bree.name]'s room."
    "Sasha in front of me, pushing her ass into my groin."
    "And I'm still not sure this is a good idea."
    "Or at least I am until the head of my cock slides against Sasha's pussy."
    "From then I seem to be on autopilot, one thing alone on my mind."
    sasha.say "Oh yeah..."
    sasha.say "Please..."
    sasha.say "Put it in me!"
    "Like I was ever going to do something else with it!"
    "Sasha's as ready for me as she sounds, wet and willing."
    play sound "sd/moans/sasha/sasha_moans_light_low.ogg" loop
    show sasha stand vaginal pleasure blush
    "We both moan and gasp as I sink into her."
    "She clings tightly to me as I begin to thrust in and out."
    "And I don't waste any time playing around either."
    show sasha stand -blush
    "Within mere moments, I'm pounding away at Sasha, going as hard as I can."
    "She takes everything that I have to give as well, never holding back."
    "In fact I can feel from the way she rides me that she wants even more!"
    play sound "sd/moans/sasha/sasha_moans_light_medium.ogg" loop
    show sasha stand speed
    "I do the best I can to satisfy her, burning the very last of my energy."
    "The mirror reflects an image of us the whole time."
    play sound "sd/moans/sasha/sasha_moans_light_high.ogg" loop
    "And I watch as Sasha's wails with pleasure."
    "For a few seconds, I wonder which one of us is going to give first."
    "Will it be me, or her?"
    "Sasha answers the question a moment later."
    stop sound
    show sasha stand blush
    sasha.say "Oh fuck..."
    sasha.say "That's so fucking good..."
    sasha.say "You're gonna make me cum!"
    "She's not lying either, as I feel her pussy clench around my cock."
    mike.say "Oh...oh god..."
    with hpunch
    mike.say "BREE!"
    show sasha stand creampie ahegao with hpunch
    "I shoot my load into Sasha a second later."
    with hpunch
    "But the look on her face is less than pleased as I do so."
    show sasha stand pleasure with hpunch
    sasha.say "Y...you prick!"
    sasha.say "You...said..."
    sasha.say "You said another girl's name!"
    mike.say "N...no, Sasha..."
    mike.say "I mean...[bree.name]'s here!"
    hide sasha
    show sasha halloween surprised at flip, center, zoomAt(1.5, (540, 1040))
    show bree halloween angry at top_mostright
    with hpunch
    "We both look round to see [bree.name] standing in the open doorway."
    "Her mouth hangs open and her eyes are as wide as saucers."
    show bree vangry
    bree.say "Eww!"
    bree.say "You did it - in my room?!?"
    show bree angry
    mike.say "Ah...I guess so, [bree.name]!"
    show sasha whining
    sasha.say "Would you believe we got lost on the way to my room?"
    show sasha annoyed
    show bree vangry
    bree.say "Well, I certainly know where your room is, [hero.name]."
    bree.say "And that's where I'll be sleeping until you wash my sheets!"
    hide bree with easeoutright
    show sasha surprised at center, zoomAt(1.5, (640, 1040)) with ease
    "And with that, [bree.name] turns on her heel and storms off."
    show sasha happy at startle
    "Sasha burst out laughing, and for a moment I feel like telling her off."
    "But then the urge passes, and I find myself seeing the funny side."
    "[bree.name]'ll get over it in time."
    "And it was worth it to see the look on her face."
    "Well, that and the chance to fuck Sasha too!"
    $ sasha.sexperience += 1
    $ game.pass_time(1)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
