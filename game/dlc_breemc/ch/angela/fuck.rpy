init python:
    Event(**{
    "name": "angela_hottub_sex_female",
    "label": "angela_hottub_sex_female",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            IsActivity("date_hot_tub_home")),
        PersonTarget(angela,
            OnDate(),
            MinStat("love", 100),
            MinStat("sexperience", 1),
            ),
        ],
    "priority": 500,
    "do_once": False,
    "once_day": True,
    "duration": 1,
    })

label angela_hottub_sex_female:
    scene bg livingroom with fade
    "I've got to admit that I'm more than a little nervous about Angela coming over tonight."
    "It's supposed to be nothing serious, a casual dip in the hot-tub, just the two of us."
    show bg pool with fade
    "That's why I'm now looking at the hot-tub and the decking around it and wondering if I've gone too far."
    "I mean, I could have got away with making sure the lighting was subdued."
    "Or candles and a nice bottle of wine would have been nice to take the edge off."
    "Hell, I could even have sprinkled a few rose petals around the place to make it special."
    "The problem is that I've gone and done all of those things."
    "And now the place looks like I'm planning on tonight being a crazily romantic date!"
    "Plus there's no time to dial it all back either, because Angela's due any minute now."
    "Urgh..."
    "Looks like I'm just going to have to grit my teeth and get on with things."
    "Because what could be weird about a romantic dip in the hot-tub with my housemate's mom?"
    "No, no, no!"
    "I have to stop thinking of Angela like that."
    "She's more like a mature woman that happens to be my friend."
    "I don't think of her changing [mike.name]'s nappy when I see her - not at all!"
    angela.say "Hello, [hero.name]..."
    angela.say "Oh my..."
    angela.say "I hope you didn't go to all this trouble just for me!"
    "At the sound of Angela's voice, I spin around."
    show angela casual normal with dissolve
    "And at the same time I hope the smile on my face doesn't look forced."
    bree.say "Of course not, Angela."
    bree.say "I'm having a dozen or so other people come round too."
    bree.say "I thought we could make a pool party out of it, yeah?"
    show angela surprised
    "Angela looks more than a little taken aback."
    show angela normal
    "But she nods and smiles too, like she's trying to make the best of it all."
    angela.say "Oh..."
    show angela disappointed
    angela.say "Alright, [hero.name]."
    angela.say "If that's what you really want..."
    "I can't help shaking my head and chuckling."
    bree.say "I'm joking, Angela!"
    show angela normal at startle
    bree.say "Of course all of this is for you!"
    bree.say "I just wanted to make things nice for you."
    "Angela puts her hand to her mouth."
    show angela blush
    "And I can see her blushing a little."
    show angela flirt blush
    angela.say "Oh heavens, [hero.name]..."
    angela.say "What am I even saying?"
    angela.say "I...I'm just a little nervous, that's all!"
    "As soon as those words are out of Angela's mouth I feel a flood of relief."
    "The fact that she's feeling the same way as me means that I can breathe again."
    "And that she's admitting it is a good enough reason to be open about it too."
    bree.say "I'm so glad you said that, Angela!"
    bree.say "The truth is I feel a little weird too."
    bree.say "Like, I didn't know whether to make it intimate and romantic."
    bree.say "Or just act like we were a couple of friends hanging out!"
    show angela pleased
    "Angela nods and lets out a sigh of relief herself."
    show angela happy
    angela.say "I know, [hero.name], I know!"
    angela.say "You wouldn't believe how long I spent picking out my swimsuit!"
    angela.say "You'll just have to be honest with me."
    angela.say "Do you think it's appropriate?"
    "Before I can say another word, Angela takes off her clothes."
    $ game.active_date.clothes = "swimsuit"
    show angela close swimsuit at top_to_bottom with dissolve
    "Which reveals that she only has the swimsuit on underneath!"
    "I was ready to assure Angela that whatever she had on would be fine."
    "But the sight of her leaves me literally speechless."
    "She has on a black and white one-piece bathing suit."
    "And it shows off her curves magnificently!"
    show angela close swimsuit at bottom_to_top
    angela.say "Oh my..."
    angela.say "It's too much, isn't it?"
    bree.say "Fucking hell, Angela!"
    bree.say "What are you talking about?!?"
    bree.say "You look like a million dollars!"
    hide angela close
    show angela swimsuit normal blush
    with dissolve
    "If Angela was blushing a little before, she goes bright red now."
    "But I can see that she's not embarrassed enough to cover up again."
    show angela b
    "In fact she's actually starting to hold herself in a more flattering pose!"
    angela.say "Oh...I..."
    angela.say "Shouldn't we get in the hot-tub?"
    show angela normal
    angela.say "I think we should definitely get in the tub!"
    "I nod and hurry over to the side of the tub, ushering Angela to get in."
    "As she does so, I open the wine and pour us a couple of glasses."
    show hottub angela valentine with fade
    "Then I hop in too, sinking into the warm, welcoming water."
    "Angela takes the glass as soon as I hand it to her."
    "And I watch as she drains more than half of it off in one go."
    bree.say "Whoa!"
    bree.say "Slow down, Angela!"
    bree.say "We've got all night, you know?"
    "Angela nods and puts her glass down."
    angela.say "Sorry..."
    angela.say "Nerves again!"
    angela.say "You know I haven't done anything like this for a while, [hero.name]!"
    bree.say "Well...for what it's worth, Angela..."
    bree.say "I feel pretty special that you're doing it with me!"
    "Angela gives me a strange look as I say this."
    "Then I feel her take hold of my hand."
    "What happens next takes me totally by surprise."
    "She slides over to my side of the tub."
    "And without hesitation, places her lips against mine."
    if game.calendar.get_time_of_day() == "evening":
        $ renpy.show(f"hottub_bg_night_left")
    else:
        $ renpy.show(f"hottub_bg_{game.calendar.season_name}_left")
    $ renpy.show("hottub_fg_valentine_left", tag="romantic")
    show angela kiss swimsuit zorder 2 at center
    with fade
    $ angela.flags.kiss += 1
    "I'm only taken by surprise for a few seconds."
    "Then my body seems to take over where my mind hesitated."
    "I turn my head, leaning into the kiss."
    "My lips part at the same time as Angela's."
    "Then our tongues slide around each other too."
    "I feel myself dropping my glass on the decking beside the tub."
    "But I hardly care where the contents spill or if the glass breaks."
    "All that matters to me in the moment is kissing Angela."
    "That and pulling her into a tight embrace."
    "And it's an obsession that she seems to share with me."
    "As I feel her arms wrapping around me at the same time."
    "For a moment I think that Angela's going to pull me down under the water."
    "But then she leans back, pulling me onto her side of the tub."
    "I resist, but only a little, enough to break the kiss."
    "That and to ensure that I slip out of Angela's embrace."
    scene bg black
    show hottub angela valentine
    with fade
    "She looks down at me, her eyes filled with surprise and longing."
    "But I make sure to show her that I'm not pulling away entirely."
    "And I do that by lowering my head to kiss her body as I go."
    "First I kiss Angela's neck, and then her chest."
    "I pay particular attention to her breasts."
    "And I enjoy the sensation of her stiffening nipples."
    "Then I linger a little on her belly."
    "Long enough to let her dwell on what's coming next."
    "As my head finally goes down between her thighs, Angela raises her head."
    "She's straining to see what I do next, desperate to know."
    "But she feels it before she sees it."
    show hottub sex female angela with fade
    "Easing aside the crotch of her swimsuit, I begin to kiss again."
    "This time I'm planting delicate kisses around the edge of her pussy."
    "And little by little, my lips begin to touch the delicate folds of her lips."
    "I can't see how Angela's taking it, but I can hear breathing heavily."
    "And the deeper I go, the more she starts to gasp and moan."
    "Now that my lips are on hers, I part them and let my tongue go to work."
    "It moves in a way that they never could, probing and exploring."
    "At the same time I reach up with both hands, stroking Angela's body."
    "She's helpless to resist, holding onto the edge of the tub."
    "So I can play with her in any way that pleases me."
    "And I know that it's doing the same for her too."
    "Because her pussy surrenders to me, allowing my tongue to slip inside."
    angela.say "Oh..."
    angela.say "Oh, [hero.name]..."
    angela.say "You...you wicked little thing..."
    angela.say "You're going to...going to make me...cum!"
    with hpunch
    "I hold on tight to Angela's body as she begins to twitch and twist in the water."
    "My tongue's as deep into her pussy as I can possibly reach."
    "And my fingers are pinching at her now rock-hard nipples."
    with hpunch
    "When she actually cums, Angela wraps her legs around my neck."
    with hpunch
    "Squeezing so hard that I think she's going to choke me out!"
    with hpunch
    "And the wail that emerges from her mouth is one of sheer helpless pleasure."
    "Once she's spent, I have to hold Angela up in the water."
    "My arms supporting her so that she doesn't sink beneath the surface."
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ angela.sexperience += 1
    $ game.active_date.clothes = None
    scene bg black with dissolve
    return



label angela_fuck_date_female(location="hero"):
    $ game.room = "bedroom4"
    $ game.play_music("music/roa_music/smile_for_me.ogg")
    call angela_fuck_date_intro_female (location) from _call_angela_fuck_date_intro_female
    menu:
        "Go down on her":
            call angela_fuck_date_bree_cunnilingus (0) from _call_angela_fuck_date_bree_cunnilingus
        "Let her go down on me":
            call angela_fuck_date_angela_cunnilingus (0) from _call_angela_fuck_date_angela_cunnilingus
        "Use a strapon on her" if hero.sexperience >= 5:
            call angela_fuck_date_bree_missionary (5) from _call_angela_fuck_date_bree_missionary
        "Let her use a strapon on me" if hero.sexperience >= 5:
            call angela_fuck_date_angela_missionary (5) from _call_angela_fuck_date_angela_missionary
    if _return == "leave_without_gain":
        return
    $ angela.sexperience += 1
    if _return == "leave_with_gain":
        return
    hide angela
    call angela_sleep_date_fuck_female (location) from _call_angela_sleep_date_fuck_female
    return

label angela_fuck_date_intro_female(location="hero"):
    $ renpy.dynamic("result")
    $ result = game.days_played % 3
    if result == 0:
        scene bg taxi car
        show angela
        with fade
        "It doesn't take long for Angela and me to flag down a taxi."
        scene bg taxi car open
        hide angela with dissolve
        pause 1.0
        play sound car_door
        scene bg taxi car closed
        "And as soon as we pile into the back, there's decision to be made."
        "Where are we going to go?"
        "At first, neither of us says a thing, we just stare at each other."
        "But then I surprise myself by being the one to speak up."
        bree.say "My place..."
        bree.say "We're going to my place..."
        bree.say "Right?"
        "Angela nods and I feel her take hold of my hand."
        "Then she squeezes it tightly."
        angela.say "You bet, [hero.name]."
        angela.say "But you might want to give the driver your actual address!"
        "I nod and do as she says, so we can begin our journey."
        "And from there, the drive seems to pass by in the blink of an eye."
        show bg house with fade
        "When the taxi pulls up, I pay the driver and we start to walk up to the house."
        "But I can already sense that there's an unspoken question hanging in the air."
        "One that neither of us wants to be the one to bring up."
        show angela fragile at center, zoomAt(1.5, (640, 1040)) with dissolve
        "Yet it's the reason that we're slowing down as we get ever closer to the front-door."
        "In the end, just like in the taxi, I figure I should be the one to break the silence."
        bree.say "I know what you're thinking, Angela..."
        bree.say "But for all we know, [mike.name] could not be home."
        "Angela nods, and I feel her squeeze my hand all over again."
        show angela worried
        angela.say "It doesn't matter if he's home or not, [hero.name]."
        angela.say "[mike.name]'s all grown up now."
        angela.say "He's not a little boy anymore - he's a man."
        show angela sadistic
        angela.say "And I have a life of my own to lead."
        show angela normal
        "We're mounting the steps to the porch as Angela says all of this."
        "And I'm nodding, agreeing with the sentiment one hundred percent."
        "But I still feel like I want to sneak into the house unseen."
        bree.say "Totally, Angela, totally..."
        bree.say "But I'd be sneaking you into the house if you were anyone else."
        bree.say "I'm just not in the habit of announcing to my housemates that I'm getting it on!"
        "Angela nods, letting me know that she's on the same page."
        "So it's agreed - we're not hiding from [mike.name]."
        "But we're not going to sit him down and tell him what we're doing either."
        scene bg black
        show bg livingroom
        with wipeleft
        pause 0.5
        show angela at left with easeinright
        "To that end I open the door as quickly and quietly as I'm able."
        "And then we hurry up the stairs to my bedroom."
        "I must have walked that short route thousands of time already."
        show bg secondfloor with dissolve
        show angela at right5 with ease
        "But today it feels like the longest walk of my life."
        "I'm looking this way and that, expecting [mike.name] or Sasha to appear at any moment."
        "By the time we make it to my room, my heart is pounding in my chest."
        show bg bedroom4 with dissolve
        show angela at left5 with ease
        "And I all but drag Angela inside as I slam the door shut behind us."
        "Leaning against it, I try to get my breathing under control."
        "And I can see that Angela's in pretty much the same state too."
        bree.say "I..."
        bree.say "I think...we made it!"
        show angela at center, zoomAt (1, (640, 720)) with ease
        show angela at center, traveling (1.25, 1.0, (640, 940))
        "Before I can say another word, Angela walks over to me."
        hide angela
        show angela kiss at right4, startle(0.05,-10)
        $ angela.flags.kiss += 1
        "And she presses her lips against mine, kissing me with a passion!"
        "It seems like she's not trying to calm herself down."
        "Instead she's decided to give in and go with the adrenaline rush!"
        "But it's not like I've managed to calm myself down."
        "Not in the space of those few short seconds."
        "And now I can feel my pulse starting to speed up all over again."
        "What other choice do I have but to give in?"
        "Before I know it, I'm giving as good as I'm getting."
        "And I'm no longer leaning against the door either."
        "Instead I'm pushing Angela backwards as I kiss her."
        show angela kiss at center with ease
        "Each step takes us closer to the bed."
        show angela kiss underwear with dissolve
        "And our hands are tugging at each other's clothes."
        show angela kiss at left4 with ease
        "Once a garment it taken off, it gets tossed aside."
        show angela kiss naked with dissolve
    elif result == 1:
        show bg bedroom4 with fade
        pause 0.1
        show angela fragile at center, zoomAt(1.25, (640, 880)) with easeinright
        "I do the best I can not to squeeze Angela's hand too hard as I lead her into my bedroom."
        "But there's always the crazy, paranoid fear in the back of my head that I have to hand onto her."
        "Otherwise this amazing, beautiful and deeply sexy older woman might just disappear on me."
        "That I might wake up in bed, finding that Angela was just part of a dream I'd conjured up."
        "Okay, yeah...I know that sounds pretty over the top."
        "But give me a break, because I've fallen for this woman, and hard!"
        "All the same it comes as a relief when I feel Angela squeeze my hand in return."
        show angela at center, zoomAt(1.25, (340, 880)) with ease
        "She lets go of it a moment later and hurries over to sit on my bed."
        "Which leaves me to close the door behind us and then follow Angela's lead."
        show angela fragile at center, zoomAt(1.5, (640, 1040)) with fade
        "Sitting down beside her, I can feel my heart starting to pound in my chest."
        "I'm sure that if I tried to speak right now, my words would come out in a jumbled mess."
        "Which is why I feel relieved when Angela's the one to speak up first."
        show angela flirt
        angela.say "Oh, [hero.name]..."
        show angela happy
        angela.say "Being in a room like this - it takes me back..."
        angela.say "You know, right back to being as young as you are now?"
        show angela normal
        "All I can do in response to that is let out a stupid snort of laughter."
        bree.say "Hah!"
        bree.say "You're not old, Angela..."
        bree.say "You're like, totally in your prime!"
        "Angela smiles and shakes her head, giving me one of those looks."
        "The kind that tell me she's flattered, but not in the least bit convinced."
        show angela happy
        angela.say "Let's just say I'm mature, okay?"
        angela.say "But I mean it, [hero.name]..."
        angela.say "This reminds me of being young, and fooling around."
        angela.say "You know, with my girlfriends?"
        angela.say "Before [mike.name]'s dad came along..."
        show angela normal
        "I nod in agreement."
        "But the truth is that I really don't know what to say to that."
        "I'm happy that Angela's putting her past behind her and moving on with me."
        "But that doesn't mean I'm going to dump on her memories either."
        "Sure, her husband might have been the villain of the piece."
        "And yet that does nothing to lessen the love she obviously feels for [mike.name] and his sister."
        "I'm sure to make her hate me if I show that I don't respect all of that."
        bree.say "I'm glad it does, Angela."
        bree.say "Because I want to help you rediscover that part of who you are."
        hide angela
        show angela kiss
        with fade
        $ angela.flags.kiss += 1
        "Angela takes me by surprise then, leaning in and kissing me on the lips."
        "I soon recover and lean into it too, enjoying the sensation while it lasts."
        hide angela
        show angela blush at center, zoomAt(1.5, (640, 1040))
        with fade
        "And even though the kiss turns out to be brief, it leaves me tingling all over."
        "All at once, Angela looks up and reaches out for me."
        "I let her hand begin to unbutton my clothes, starting to undress me."
        show angela happy
        angela.say "Come on, [hero.name]..."
        show angela normal
        "Then both her hands are at work removing my clothes."
        show angela happy
        angela.say "What are you waiting for?"
        show angela normal
        "I take that as my cue to leap into action."
        "As well as a guarantee that Angela's on the same page as me."
        "And I start pulling off her clothes in earnest."
        show angela naked with dissolve
        "We do the best we can to keep out of each other's way."
        "But more than once we have to stop and cooperate in order to get the job done."
    else:
        show bg house
        show angela normal
        with fade
        "I feel like I should be getting more used to being around Angela by now."
        "Like, we've accepted the fact that we have serious feelings for each other."
        "Plus we've been on more than a few dates by now, and they've been great."
        "But somehow I still feel kind of intimidated, and afraid to ask her for things."
        scene bg black
        show bg livingroom
        with wipeleft
        pause 0.5
        show angela at left with easeinright
        "Like right now, we're walking into my bedroom after we had a fun date together."
        "And I want more than anything to show Angela just how I feel about her."
        show bg secondfloor with dissolve
        show angela at right5 with ease
        "How much she's turning me on right now!"
        "Urgh..."
        "This would be so much easier if I were a guy."
        show bg bedroom4 with dissolve
        show angela at left5 with ease
        "People expect them to be all forward and in your face."
        "But when you're a girl, you always worry about how things are going to look."
        "My frustration must have been showing in the grip I have on Angela's hand."
        "Because I feel her squeeze my fingers as we reach the side of the bed."
        "Then she turns to face me, a gentle smile on her face as she does so."
        show angela worried
        angela.say "[hero.name]..."
        angela.say "Is everything okay?"
        angela.say "Are you feeling up to this?"
        show angela shy
        "I know that Angela's only trying to be sensitive to my needs."
        "That she doesn't want to push herself onto me without my permission."
        "But all the same, it's the less rational part of my brain that answers her."
        "The part of me that's paranoid I'll blow it by saying something stupid."
        "And so it tries to solve the situation by blurting something out."
        "Something that probably is pretty stupid."
        bree.say "What?"
        bree.say "Of course I'm okay..."
        bree.say "I couldn't be better..."
        bree.say "I'm fine, totally fine!"
        show angela normal blush
        "Luckily for me, Angela doesn't seem to be thrown by my getting tongue-tied."
        show angela pleased at center, zoomAt (1, (640, 720)) with ease
        show angela at center, traveling (1.5, 1.0, (640, 1040))
        "Instead she responds by closing her eyes and leaning in closer."
        hide angela
        show angela kiss
        with fade
        $ angela.flags.kiss += 1
        "And then she places her lips against mine."
        "The kiss that follows is firm and brooks no resistance from me."
        "I find myself melting into it within mere moments, being swept along."
        "And as I am, all of my doubts seem to lessen and then disappear."
        "Somehow Angela answers all of my questions without saying a word."
        "She turns the kiss into a perfect affirmation of her desire for me."
        "And I can feel it flowing from her into me the whole time."
        "Neither of us seems to need to be told to begin undressing the other."
        "Instead it comes almost as natural urge, from a need to be closer."
        show angela kiss naked with dissolve
        "Before I know it, we're both naked, bodies pressed together."
    return

label angela_fuck_date_angela_cunnilingus(sexperience_min):
    $ renpy.dynamic("result")
    $ result = game.days_played % 2
    if result == 0:
        "Then we start on the next one with even greater determination."
        show bree cunnilingus angela kiss side tongue pleasureangela pleasurekiss with fade
        "By the time I feel us bump into the bed, both Angela and I are naked."
        "Neither of us stops long enough to lower ourselves onto the mattress."
        "Instead we tumble down onto it in a tangle of limbs."
        with vpunch
        "We roll on the bed, Angela coming up on top."
        scene angela cunnilingus bree
        show angela cunnilingus bree onangela
        with vpunch
        "And she wastes no time in taking advantage of that fact."
        "Angela places her hands on my shoulders, pinning me down."
        "I could struggle to free myself, try to take control."
        show angela cunnilingus bree pleasure
        "But I'm far too intrigued to see where this is going."
        "I want to discover what she has in mind for me."
        "And so I just lie back and let Angela have her way."
        show angela cunnilingus bree normal
        "She lowers herself down, holding my eye as she does so."
        "Angela doesn't stop until her head is level with my breasts."
        show angela cunnilingus bree suck neck with fade
        "Then she casts her eyes down and falls on them without mercy."
        show angela cunnilingus bree chest pleasure
        "I feel my nipples stiffen and become hard as her lips find them."
        "I was pretty turned on by what Angela's mouth did to mine."
        "But I'm totally blown away by what it's now doing to my chest."
        "Angela licks, nuzzles and bites in ways I didn't think were possible."
        "Rather and I swear that she's tweaking her technique all the time too."
        show angela cunnilingus bree down normal
        "This isn't just having someone put my nipples in her mouth."
        "It's like she's playing them, like they're a delicate musical instrument."
        show angela cunnilingus bree down pleasure
        bree.say "Aah..."
        bree.say "Angela..."
        bree.say "What are you..."
        show angela cunnilingus bree outside
        pause 0.2
        show angela cunnilingus bree inside
        bree.say "Oh...oh god!"
        "The tone and volume of my voice change as Angela surprises me again."
        "I was so tied up in what she's doing to me I didn't notice her hands move."
        show angela cunnilingus bree up pleasure
        "And they've now wandered all the way down to my belly, then below."
        "Angela's playing with my pussy too, just as skilfully as she is my breasts!"
        show angela cunnilingus bree outside down normal
        "The tips of her fingers trace the lines, slowly and deeply."
        "And they move ever closer to the centre with each pass."
        "This means that when Angela reaches the middle, she meets no resistance."
        show angela cunnilingus bree inside
        "Her fingers are able to slide straight into me, pushing me to another level."
        show angela cunnilingus bree pleasure
        "I have to close my eyes in order to keep from being overwhelmed."
        "But the moment that I do, Angela makes her next move."
        "I hardly notice as she abandons my breasts."
        "As the sensations from my pussy are drowning everything else out."
        show angela cunnilingus bree lick -inside with fade
        "Realisation only dawns when I feel those lips and that tongue down there."
        "And it's not like Angela chooses to slow down or go easy on me either."
        "Instead she takes full advantage of the groundwork her fingers have already laid down."
        "Angela all but dives in head-first, tongue pushing into me."
        "And as a woman, she knows just what to do down there too."
        "With a guy I'd be having to make the right sounds to guide him."
        "To let him know just how good it felt and when I wanted more of the same thing."
        show angela cunnilingus bree lick up
        "But Angela knows from her own experience where to go and what to do."
        "She cuts right to the point, pushing me further with each passing second."
        "Angela gives me exactly what I want, even before I know that I want it myself."
        show angela cunnilingus bree lick up outside neck
        "And if I could, I'd lie here and just soak it up forever."
        "But there's only so much that my body can take."
        "I'm already fast approaching that point, beginning to teeter on the edge."
        show angela cunnilingus bree lick up inside with vpunch
        "And then it happens, I feel myself swept away and rendered helpless."
        with vpunch
        "All I can do is lie there, letting my orgasm pass over me."
        "I don't know if Angela's aware that its happening."
        show angela cunnilingus bree lick ahegao with vpunch
        "And I can hardly feel what she's doing to me now."
        "My senses are flooded, my mind overwhelmed."
        "So I just surrender, and wait for my mind to come back to me."
    else:
        "There's no doubt in my mind that Angela's the one that's in control."
        show bree cunnilingus angela kiss side tongue pleasureangela pleasurekiss with fade
        "Because I offer no resistance as she turns me around."
        "And when I feel her pushing me down onto the bed, I go without hesitation."
        with vpunch
        "Angela doesn't speak a word of her intentions to me."
        "Yet somehow I feel like I already know what she has in mind."
        "And the thought of it begins to make a certain part of me twinge in anticipation."
        "Angela continues to kiss me as my head sinks into the pillows."
        scene angela cunnilingus bree
        show angela cunnilingus bree onangela
        with vpunch
        "But as soon as I'm horizontal, I feel her hands on my body."
        "They run downwards, over my chest and then my belly."
        "And I almost fold myself in two as they slide between my thighs."
        "Though when I try to move, Angela uses her weight to keep me pinned down."
        "One hand returns from down below to hold down my shoulder."
        "It's then that she chooses to break off the kiss."
        "There's no warning, and so I'm left open-mouthed and gasping."
        "Panting in confusion as I look down at where those lips are going next."
        "Angela heads straight downwards, stopping when she reaches my breasts."
        show angela cunnilingus bree chest pleasure
        "There's just time for me to bite my lip in anticipation."
        "And then, as her lips close around a nipple, my eyes close too."
        "Before now the sensations were all those created by my own body."
        "But now I can feel the effects of Angela's touch on me too."
        "As she moves the nipple in her mouth, her hand is active too."
        "It teases and tickles down there, always moving between my thighs."
        "First one sensation hits me, and then the other."
        show angela cunnilingus bree down normal
        "They feel like two waves crashing onto the same beach."
        "One hits and sweeps in, receding as the other washes over it."
        "This means that I can never ride one of them to the end."
        "Before I get that far, the effects of the other are already hitting me."
        "Just when I feel like I might be able to handle it, Angela makes a change."
        "Switching from one breast to the other, she renders me helpless all over again."
        "At the same time her fingers are drawing ever closer to my pussy."
        show angela cunnilingus bree outside
        "I can feel her tracing the outer edges and then going deeper still."
        "Every fraction of an inch making me gasp for the mercy of release."
        show angela cunnilingus bree inside pleasure
        "This means that when one of the waves of pleasure ends, I hardly notice."
        "By the time I manage to look down, I see that Angela's head is gone."
        show angela cunnilingus bree lick -inside with fade
        "For a moment I have no idea where she could have disappeared to."
        "But then the sensations from down below increase a hundredfold."
        show angela cunnilingus bree lick up outside normal
        "And I don't just mean they get stronger."
        "What I mean is that they explode!"
        show angela cunnilingus bree lick up inside
        "Angela finally makes it all the way inside of my pussy."
        "But I know from the feeling of it that she's not using her fingers anymore."
        "Instead I'm sure that it's her tongue I can feel, inching it's way into me."
        "I feel her probing, pushing and finding the path between my lips."
        "And the feeling is like nothing that she's done to me before this moment."
        show angela cunnilingus bree lick down outside pleasure
        "Angela must be bringing years of experience to the table right now."
        "Either that or she knows just how a woman's body works and what they want."
        "Because she hits every point and misses nothing out as she pleasures me."
        show angela cunnilingus bree lick up inside pleasure
        "More than once I find myself wishing that she would do a certain thing."
        "Or that she could linger longer in one specific spot."
        "And every time Angela does so, like she's able to read my mind."
        bree.say "Ah..."
        bree.say "Aaah..."
        bree.say "Angela!"
        "Another time I would have been embarrassed to call out as loudly as I am."
        "Simple fear of being heard would have ensured that I did all I could to keep quiet."
        "And here there's the additional danger of [mike.name] being in the house and hearing me."
        "But even the prospect of him hearing me shouting his mom's name can't keep me silent."
        with vpunch
        "And that's because she's making me cum."
        show angela cunnilingus bree lick ahegao with vpunch
        "Making me lose it like a force of fucking nature!"
        with vpunch
        "There's no way I can do anything but give in to the moment and let it take me."
        with vpunch
        "Angela keeps right on pleasuring me until my head falls back onto the pillows."
        "And even then she doesn't stop dead, instead stroking me gently with her tongue."
        "Afterwards she doesn't say a word."
        "She just crawls slowly upwards until her head is level with mine."
        "Then she lies beside me, holding me in her arms and enjoying the silence."
    return

label angela_fuck_date_bree_cunnilingus(sexperience_min):
    show bree cunnilingus angela side pleasureangela
    "I haven't told Angela what I intend to do when I reach her."
    "But somehow she seems to know just what my intentions towards her are."
    "Because she leans back on the pillows and spreads her legs wide apart."
    "I could dive straight in there and get down to business."
    "But all it takes is one lingering look at Angela to know that I can't."
    show bree cunnilingus angela kiss side
    "Instead I lean in close and begin to kiss her on the lips."
    "At the same time my hands are all over her, stroking and caressing."
    "I feel Angela quivering at my touch, her tongue slipping into my mouth."
    "And I know most of all that I'm only going to be able to keep this up for a short while."
    "Because I can already feel myself beginning to ache for what's down below."
    "Though in the end, it's Angela that makes the decision for me."
    show bree cunnilingus angela tongue
    "Suddenly I feel her pulling away from my kiss and gasping for breath."
    show bree cunnilingus angela normalangela
    angela.say "[hero.name[0]]...[hero.name]..."
    angela.say "Down there..."
    angela.say "Please?"
    "Angela does all she can to push me downwards."
    show bree cunnilingus angela suck
    "And as I already mentioned, her legs are spread wide apart."
    show bree cunnilingus angela lick pleasuredown front -tongue
    "This means that I can crawl between them, feeling like a horny, pink snake!"
    "I take one last look up at Angela as my head descends between her thighs."
    "And I just have time to see her nod her head, eyes wide with anticipation."
    "Then I lower my head and close my eyes, slowly parting my lips."
    "With one hand on each of Angela's thighs, my mouth is right next to her pussy."
    "Already the scent of it is filling my senses and making me eager to get started."
    "It's intoxicating to me, more than enough to make my own sex begin to come alive too."
    "But I fight back from the urge to indulge myself, focussing on the task at hand."
    "I can't give in to the idea of pleasuring myself and still do the same for Angela."
    "Instead I clear my mind as best I can, then I purse my lips."
    "This allows me to begin gently kissing Angela's own."
    "Instantly I feel her entire body twitch, and I hear her gasp at the sensation."
    "But it doesn't make me stop or even slow down for a moment."
    "Gently I part my lips to allow my tongue to emerge and begin its work."
    "Now I can actually trace the lines and folds of Angela's pussy."
    "Turning my head sideways to allow the tip to sink in further still."
    "I keep having to make an effort to focus my thoughts and not get distracted."
    "Because by now Angela is getting seriously excited and her pussy is showing it."
    show bree cunnilingus angela at startle(0.05,-10)
    "The natural lubricants that she's producing are flowing freely over my lips."
    "And when they touch my tongue, the taste of her is intense and powerful."
    "So much so that I can only redouble my efforts."
    "I feel like I want to taste more of Angela, to satisfy my hunger for her."
    show bree cunnilingus angela at startle(0.05,-10)
    "And in doing so, I'm pushed to probe deeper than ever with more intensity."
    "Luckily for me this means that the experience becomes more intense for her too."
    "In my almost blind rush to indulge myself, Angela receives the same treatment."
    show bree cunnilingus angela lick front at startle(0.05,-10)
    "I can feel her thighs coming together to squeeze me tightly."
    "And only now do I realise that she has her hands on either side of my head."
    "Not that I need the encouragement to complete the task at hand."
    show bree cunnilingus angela lick front pleasureangela at startle(0.05,-10)
    "With one last effort, I push deeper than ever before."
    with vpunch
    "My reward is to feel Angela begin to quake like crazy."
    show bree cunnilingus angela lick pleasureside with vpunch
    "Then my ears are filled with the sound of her crying out in sheer, unbridled ecstasy."
    with vpunch
    "I can't help smiling to myself as Angela collapses onto the bed and I come up for air."
    "Because I've just proven to myself that I can please an older, sophisticated woman."
    "That I can make her cum using only the tongue in my mouth!"
    return

label angela_fuck_date_bree_missionary(sexperience_min):
    show angela naked normal
    angela.say "Don't get me wrong, [hero.name]..."
    angela.say "I'm really looking forward to fooling around with you."
    angela.say "But I do miss one thing from my time with Dylan..."
    "I suddenly feel like Angela just sucker-punched me."
    "Like she rifled one into my guts and now I'm gasping for breath."
    "What is she going to say next?"
    "And how can I hope to give her something that a guy could?!?"
    bree.say "Oh...oh yeah?"
    bree.say "What's that?"
    show angela shy blush
    "Angela looks a little embarrassed to say it out loud."
    "But she finds the courage after a few seconds."
    show angela annoyed
    angela.say "His cock, [hero.name]!"
    angela.say "I loved the feel of having it inside me."
    "For a moment I expect to feel a sense of helplessness."
    "But then a thought occurs to me, and I reach under the bed."
    if hero.morality >= 25:
        "I'm almost shaking as I pull the thing out."
        "Afraid that Angela will be totally grossed out by the sight of it."
        bree.say "I...I don't normally do this kind of thing, Angela..."
        bree.say "But maybe this would help?"
    elif hero.morality <= -25:
        "I can feel myself getting wet as I handle the thing."
        "And I know that I want Angela to agree to it more than anything right now."
        bree.say "Who needs an actual, cock, Angela?"
        bree.say "Especially when you can have one of these!"
    else:
        "I know I'm taking a gamble here, as it's not exactly the same thing."
        "But I feel like I have to at least try, or else lose out on something."
        bree.say "Don't freak out, Angela..."
        bree.say "But maybe we could use this?"
    show angela surprised
    "I hold up the strap-on dildo that I had stashed under the bed."
    "It consists of a sturdy black harness that fastens around the waist and thighs."
    "But the focus of attention is always going to be the large, rubber phallus mounted on the front."
    "I study Angela closely as she stares at the strap-on in my hand."
    "And for a moment I think that she's going to freak-out on me."
    show angela shy
    "But then I see that her head's moving, and not side to side."
    "It's going up and down, slowly at first, then ever faster."
    show angela normal
    "Without needing to be asked, Angela reaches out and takes it from me."
    "I watch as she passes it through her hands, squeezing the shaft of the dildo."
    "It's as she does this that I see her eyes light up with anticipation."
    "And in that moment I know that she's totally committed to using it."
    "All at once, Angela looks up and reaches out for me."

    show angela flirt
    angela.say "Come on, [hero.name]..."
    show angela normal
    "Angela drops the strap-on onto the bed."
    show angela hunt
    angela.say "What are you waiting for?"
    show angela normal
    "I take that as my cue to leap into action."
    "While I attach the strap-on to myself, Angela lies back on the bed, staring up at me."
    show angela flirt
    angela.say "Oh, [hero.name]..."
    angela.say "This is such a great idea..."
    angela.say "Like having the best of both worlds!"
    show angela normal
    "I nod as she reaches out to take hold of my hands."
    "And I do the best I can to look confident as I kneel over her."
    "But the truth is that I'm nervous as hell."
    "What was I even thinking?"
    "That I could strap this thing on and compete with Angela's ex-husband?"
    "With a guy that had a lifetime's experience with a real cock that was actually part of him?"
    "I'm just a girl with a rubber toy hanging off of her!"
    "But then I finally look down at Angela, as she's gazing up at me."
    "And the glimmer I see in her eyes somehow makes it all seem doable."
    "I feel like she's silently willing me on, urging me to climb atop her."
    "Beginning to feel a rising sense of confidence, I lean over Angela."
    "At the same time I put my hands on her thighs and attempt to part them."
    "Angela nods, not resisting my efforts for a second."
    "This means that I'm getting closer with every passing second."
    "The head of the dildo bobbing and swaying before me."
    "Soon enough it's no more than a fraction of an inch from Angela's groin."
    "That's when I look down and see her pussy for the first time."
    "I don't mean that I never noticed it before, you know?"
    "More that this is the first time I looked at it with the task ahead in mind."
    "Oh boy..."
    "That thing looks so good!"
    "It's like a work of art and something I want to fuck at the same time."
    "Plus I can see that it's already glistening in the light."
    "Letting me know that the anticipation is getting Angela excited."
    show angela sad
    angela.say "Mmm..."
    show angela pleased
    angela.say "Please, [hero.name]..."
    angela.say "I want you so badly..."
    angela.say "Please don't make me wait any longer!"
    show angela fragile
    "Angela doesn't give me the chance to contemplate her demands either."
    scene bree missionary angela with fade
    "She reaches up and takes hold of the dildo, pulling me down and towards her."
    "The next thing I know, she's rubbing it hard against the lips of her pussy."
    "For moment I'm totally thrown, being pulled along by the strap-on."
    "But then I feel a switch flick in my head, and everything changes."
    "Suddenly the dildo doesn't feel like something that's just attached to me."
    "Instead it begins to read as a part of my body, one that's thrusting out in front."
    "Lowering my thighs, I begin to move back and forth."
    "Part of me is trying to remember how the guys I've been with did it."
    "But there's also part of it that's just sheer instinct too."
    "Nevertheless, my efforts seem to pay off, and quickly as well."
    "Almost instantly I can feel Angela moving beneath me."
    "In sympathy with my own motions and perfectly complementing them."
    "I recognise the same signs of arousal in Angela that I've felt myself."
    "The quivering sense of anticipation and as I wait for my body to surrender."
    "And even though the dildo I'm using is just hard rubber, I can still feel something."
    "The base is pressing hard against my own pussy as it begins to sink into Angela."
    "Which means that I'm pleasuring myself at the same time as her."
    "Once I manage to get it all the way in, I'm not even thinking about it anymore."
    show bree missionary angela pleasure
    "Before I was trying to remember past experiences and use them to please Angela."
    "But now I feel like everything is coming to me naturally and in the moment."
    "Already my movements are gaining in speed and confidence."
    "And it's starting to show in the way that Angela reacts."
    show bree missionary angela -pleasure
    "To begin with, she was looking up at me, encouragement in her eyes."
    "But now her gaze seems to be directed elsewhere, like she's looking through me."
    "And as I really start to pound away with the dildo, Angela's eyes glaze over."
    "At the same time her mouth slowly drops open, and she lets out a moan."
    "But what surprises me most of all is the way that all of this affects me."
    "I was expecting to empathise with all that Angela's feeling right now."
    "That as a woman, I'd be able to measure what I'm doing from experience."
    "Instead the way that she's visibly zoning-out only makes me want to go faster and harder."
    "It's like I'm enjoying the sight of my efforts overwhelming Angela, rendering her helpless."
    "All I want to do is push her further, feeling a sense of thrilling power."
    "Oh wow..."
    "Is this what a guy feels like when he's making love to a girl?"
    "Is he this drunk on the power of his own dick?"
    "Suddenly I feel the sensation of Angela shifting beneath me."
    "And that's enough to end the train of thought."
    show bree missionary angela pleasure
    angela.say "Mmm..."
    angela.say "[hero.name[0]]...[hero.name]..."
    angela.say "I'm...gonna...cum!"
    show bree missionary angela ahegao
    "As Angela speaks the faltering words, I can feel myself beginning to lose it too."
    with hpunch
    "She wriggles and writhes under me, and the motions of her body pull me along with her."
    show bree missionary angela ahegao squirt with hpunch
    "What follows is a cascade of sensation, pleasure and release washing over me in equal measures."
    with hpunch
    "And when it's done, I feel like every last ounce of strength has drained from my body."
    show cuddle angela with hpunch
    "My arms falter and I collapse onto the bed beside Angela."
    "The motion pops the dildo out of her pussy, eliciting a dull moan as it does so."
    "But neither of us has the energy to say a word, or even to move."
    "Instead we lie there, breathing heavily as the sweat cools on our bodies."
    return

label angela_fuck_date_angela_missionary(sexperience_min):
    show angela naked worried at center, zoomAt(1.5, (640, 1040))
    angela.say "Don't get me wrong, [hero.name]..."
    angela.say "I'm really looking forward to fooling around with you."
    angela.say "But there's one thing I always envied my Dylan for..."
    angela.say "One thing he could do to be, but I never got to do to him."
    show angela normal
    "I realise that I have no idea what Angela could be talking about."
    "And that sucks, because I'm really intrigued to know what it could be."
    bree.say "Oh...oh yeah?"
    bree.say "What's that?"
    show angela shy blush
    "Angela gives me a wry smile."
    show angela annoyed
    angela.say "His cock, [hero.name]!"
    angela.say "I always wondered what it would be like to be the one doing the fucking!"
    "I know that there's a pretty scandalised look on my face right now."
    "Because I can see it reflected in the way that Angela's looking at me."
    "But it doesn't take me long to recover, as I know she's just sharing a fantasy."
    bree.say "I know what you mean, Angela..."
    bree.say "And you're not the only one who's thought about it."
    bree.say "So your fantasy's not all that crazy!"
    show angela happy at startle
    "Angela chuckles and shakes her head."
    angela.say "But I know something you don't, [hero.name]."
    angela.say "I know how to make my fantasy become reality!"
    show angela hunt
    "For a moment I have no idea what Angela can be talking about."
    "But then she pulls something out of her bag."
    "And she holds it up for me to see."
    bree.say "Oh..."
    bree.say "Oh my..."
    bree.say "I...I see what you mean!"
    "I do the best I can not to blink as the dildo Angela just produced swings before my eyes."
    "It's one of the biggest that I've ever seen, almost making me want to cross my legs on instinct."
    "And as soon as I lean back to get a better look, I see that it's not just an ordinary dildo either."
    "Oh no, this one is attached to a set of straps that can only be meant to fasten around the waist and hips."
    bree.say "Whoa, Angela..."
    bree.say "That's one hell of a strap-on!"
    show angela happy
    angela.say "Isn't it amazing?"
    angela.say "The moment I saw it in the sex shop, I knew that I had to have it."
    angela.say "And I want to use it tonight - on you!"
    show angela normal
    "I look up from the dildo and into Angela's eyes."
    "And the moment I do, I can see that she's one hundred percent serious."
    bree.say "On me?"
    bree.say "You want to use that thing...on me?!?"
    show angela shy
    "Angela instantly looks concerned."
    show angela worried
    angela.say "Well, yes..."
    angela.say "But only if you're okay with that?"
    show angela shy
    "I nod as soon as Angela asks the question."
    "Because I don't want her to think that I'm so easily scared off."
    if hero.morality >= 25:
        bree.say "O...okay, Angela..."
        bree.say "So long as you promise to be gentle with me?"
    elif hero.morality <= -25:
        bree.say "You bet I'm okay with it!"
        bree.say "And you'd better fuck me hard too!"
    else:
        bree.say "Sure thing, Angela..."
        bree.say "So long as you promise to make me cum!"
    "My answer seems to be the one that Angela wanted."
    "Because she greets it with a genuine smile."








    show angela frustrated
    angela.say "[hero.name]..."
    angela.say "Would you mind?"
    angela.say "These things are so much easier to put on with a little help!"
    show angela annoyed
    "I nod and hurry to do as Angela asks, helping wherever I can."
    show angela shy with hpunch
    "Mainly holding the strap-on in place as she straps it to herself."
    "When it's finally in place, I sit back on the bed."
    "Propping myself up with my hands as I take in the sight."
    "Angela seems to sense that she's on display right now."
    show angela naked worried at center, traveling(2.0, 0.5, (640, 1340))
    "Because she climbs fully onto the bed, kneeling in front of me."
    "Hands behind her back, she thrusts the dildo in my general direction."
    show angela flirt
    angela.say "So what do you think, [hero.name]?"
    angela.say "Isn't this like having the best of both worlds?"
    angela.say "A hot girlfriend that can fill you up as well as any guy?"
    show angela shy
    "All I can do is nod slowly as I stare at the head of the thing."
    "It's bobbing around in front of me, my eyes following it's every move."
    bree.say "Y...yeah, Angela..."
    bree.say "It's definitely something!"
    bree.say "I...aargh!"
    "I open my mouth to say something more."
    "But the words turn into a yelp of surprise and alarm."
    "And that's because Angela doesn't give me the chance to speak."
    "Instead she tenses her body and then literally pounces on me."
    "There's no way I can do anything to keep her from pinning me to the bed."
    "Then she's all over me, pressing me down and using her body to keep me there."
    show angela worried
    angela.say "Oh, [hero.name]..."
    angela.say "I...I don't know what's gotten into me."
    angela.say "It's this thing between my legs, it's got a mind of it's own!"
    show angela shy
    "All of these words come between bouts of passionately kissing my neck."
    "And at the same time Angela's hands are all over my body too."
    "I feel like I'm being totally overwhelmed, almost smothered with affection."
    "I don't know if Angela's conscious of what she's doing down below."
    show angela hunt
    "But I can feel her legs pushing between mine, making them part."
    "And that means the dildo is right there at the centre of the action."
    "The first time I feel it brush against the lips of my pussy, that's it."
    "In those few fleeting seconds I know that there's no way I can hope to resist."
    "All I can think about is what it's going to feel like inside of me."
    bree.say "Ungh..."
    bree.say "Angela..."
    if hero.morality >= 25:
        bree.say "Please remember...to be...gentle?"
    elif hero.morality <= -25:
        bree.say "Put it in me...NOW!"
    else:
        bree.say "Please...I want it...inside me!"
    "I have no way of knowing if my pleas are what guide Angela."
    "Or if she was always going to do what I' asking for all the same."
    "But either way I feel the sensation of her pressing down from above."
    "My lips are already slick from wanting her, so the tip slips and slithers."
    scene bg black
    show angela missionary bree pain
    with fade
    "Angela leans in harder then, using her weight with more determination."
    "And slowly, agonisingly slowly, my pussy begins to surrender to her."
    "A little at a time the lips part, and she begins to sink into me."
    "Normally I'd expect a girl to be gentle with me, knowing how this feels from experience."
    "But Angela seems to be caught up in the thrill of playing the part of a typical guy right now."
    "And that's no bad thing, as it means that she acts with determination and confidence."
    "The dildo inches its way into me, and I feel bursts of pleasure all the way down."
    "She's smiling and nodding as she gets into the role, beginning to move back and forth."
    "All I can do is lie back and surrender myself to her attentions."
    "Because Angela's picking up speed with every passing second."
    "And I soon discover that she's totally right."
    "This really is like having the best of both worlds."
    show angela missionary bree pleasure
    "I'm feeling the amazing pleasure of Angela using the dildo to fill me up."
    "But at the same time I'm in the warm, caring arms of a woman that I adore."
    "In the flush of it all, I seem to have been totally overtaken pleasure."
    "So much so that I'm not even aware of Angela looking me straight in the eyes."
    "She might have said something to me, or just given me a certain look."
    "But whatever the case, I find myself nodding eagerly."
    "And this seems to be enough to get me a nod in return."
    show angela missionary bree pain
    "Then Angela starts to pick up speed and go harder than ever."
    "I guess she was asking for permission to do just that."
    "And I gave her the go ahead without even realising."
    "Which now means that I'm along for the ride!"
    "Before I was simply laying back and enjoying myself."
    "But now I feel like I'm clinging on for dear life."
    "And that's because Angela seems determined to fuck me hard."
    "Maybe even harder than a guy ever could!"
    "It's almost like I can feel all of the emotions that are inside of Angela."
    "All of the ones that were suppressed for the years she was hypnotised by her husband."
    "And the idea of them coming flooding out is a pretty scary thought."
    "But even more intimidating is the notion of them washing over me too!"
    "All I can do is hold on and hope that what Angela has to give me isn't too much."
    "I can hear the bed creaking under me as she keeps on going."
    "But the sound is almost drowned out by the noises we're both making."
    "Angela is grunting and gasping as she ploughs into me."
    "I'm moaning helplessly, the sound growing louder all the time."
    "And it doesn't take me long to figure out why either."
    show angela missionary bree pleasure
    bree.say "A...Angela..."
    bree.say "I'm going to..."
    bree.say "Going to...cum!"
    show angela missionary bree ahegao
    "It happens almost before I'm finished speaking the words."
    with hpunch
    "My orgasm washes over me and sweeps me away with it."
    show angela missionary bree ahegao squirt with hpunch
    "In the moment I lose all sense of where I am and what we're doing."
    with hpunch
    "I just feel like I'm floating on an ocean of pure pleasure and sensation."
    show angela missionary bree pain -squirt
    "Slowly the intensity of it all begins to fade, and I drift back to reality."
    "Which is when I see Angela gazing down at me."
    angela.say "[hero.name]?"
    angela.say "Are you okay?"
    angela.say "Your eye were kind of rolled up into your head just now!"
    show angela missionary bree pleasure
    bree.say "I'm good, Angela..."
    bree.say "In fact I'm better than good."
    bree.say "You kind of blew my mind?"
    show cuddle angela with fade
    "Angela gives me a genuine smile as she lays down beside me."
    "And there's no need to speak another word as she wraps me in her arms."
    "The truth is that I'm glad of the chance to simply lie still and recover."
    "Because I'm sure my legs would be like jelly were I to try standing up."
    "And any kind of movement could be enough to send me into a state of helpless ecstasy again."
    return


label angela_sleep_date_fuck_female(location="hero"):
    if game.hour > 19 or game.hour < 6:
        scene bg bedroom4
        show angela naked
        with fade
        angela.say "Mmm...you cool with me spending the night here?"
        menu:
            "No":
                bree.say "No...I have to be up really early in the morning."
                "The sex was beyond incredible, but now I want to be alone."
                "Angela frowns in disappointment, clearly trying to shrug off the sense of rejection."
                angela.say "Okay...sleep well, I guess."
                "She shakes her head as she collects her things and leaves my bedroom."
                $ angela.love -= 3
                call sleep from _call_sleep_101
                $ game.room = "bedroom4"
            "Yes":
                bree.say "YES...I mean, yes...if you want to!"
                "I try to keep from sounding too desperate and needy, but I'm not sure I manage it."
                show cuddle angela with fade
                "Angela curling up against me beneath the covers is almost as good as the sex - almost..."
                angela.say "Sweet dreams, [hero.name]..."
                bree.say "You too, Angela..."
                $ angela.love += 3
                call sleep ("angela") from _call_sleep_102
                $ game.room = "bedroom4"

    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
