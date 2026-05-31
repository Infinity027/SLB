label angela_after_dance_success_with_female:
    show angela blush
    "The moment I finish dancing, I can't help glancing over to where Angela's standing."
    "Because I really want to know what she thought of my moves, and if she liked them."
    "So it's a real thrill to see the look of amazement on her face when I do so!"
    "A moment later, it gets even better as Angela hurries over to me as well."
    show angela happy -blush
    angela.say "[hero.name]..."
    angela.say "Where did you learn to dance like that?"
    angela.say "You were amazing!"
    show angela normal
    "I do the best I can to wave away Angela's gushing praise and act like it's nothing."
    "But the truth is that inside, I'm bursting with pride as she showers me with it."
    bree.say "Oh, that?"
    bree.say "It was nothing really."
    bree.say "Just something I came up with on the spot."
    "Angela narrows her eyes and gives me a sideways look."
    "Which makes me think that she doesn't quite believe me."
    "But all the same, she's not about to call me out on it."
    return

label angela_after_dance_failure_with_female:
    show angela shy
    "The moment I finish dancing, I do the best I can to avoid looking in Angela's direction."
    "Because I can already feel my cheeks starting to turn red with embarrassment."
    "And all thanks to the fact that was the worst time I ever spent trying to dance!"
    "Part of me wishes I could just run away before Angela even reaches me."
    show angela worried
    angela.say "[hero.name]..."
    angela.say "That was..."
    angela.say "Erm...shall we say unique?"
    show angela shy
    "I can't help physically cringing as I turn to face Angela."
    "And it gets worse when I see the look on her face."
    "Because it's pretty pained, like she's trying to ignore how bad it really was."
    bree.say "I really don't know what happened out there, Angela."
    bree.say "My feet felt like they weren't doing what I told them to."
    bree.say "It was totally crazy!"
    show angela normal
    "Angela gives this a quick, curt nod."
    "But then she changes the subject, like she doesn't want to talk about it any more."
    show angela happy
    angela.say "Anyway..."
    angela.say "Let's go and do something that doesn't involve dancing."
    show angela normal
    bree.say "Like what?"
    show angela sadistic
    angela.say "Absolutely anything at all - so long as there's no dancing!"
    show angela normal
    return

label angela_halloween_invitation_female:
    show angela
    "Almost the moment I agreed to the Halloween party, I knew who I wanted to invite."
    "And it might be a little awkward, but there's nobody else that I want there with me."
    "I just have to hope that [mike.name]'s big enough to handle the fact that person is his mom!"
    "Because I'm dead set on asking Angela to come along to the party as..."
    "Well, I guess as my date!"
    "Of course all of this stuff is running around in my head the next time I see her."
    "But I do the best that I can to push it all aside, and I steel my nerves to ask."
    "And much to my surprise, Angela beats me too it!"
    show angela talkative at center, zoomAt(1.5, (640, 1040)) with fade
    angela.say "[hero.name]..."
    angela.say "You look like you have a lot on your mind right now."
    angela.say "Are you wanting to invite me to your Halloween party?"
    show angela normal
    "I stare at Angela for a moment, my mouth hanging open."
    "Then I finally manage to blink and shake a little of it off."
    "Just enough to be able to answer the question."
    bree.say "Huh?!?" with hpunch
    bree.say "How do you know about that?"
    show angela smile with dissolve
    "Angela pulls one of those knowing smiles that she does so well."
    "The kind that only a mature and confident woman is capable of."
    show angela happy
    angela.say "Oh, [hero.name]..."
    angela.say "Do you think that [mike.name] doesn't talk to his mother?"
    angela.say "He was on the phone to me almost as soon as you agreed to it!"
    show angela smile
    "I can't help raising my eyebrows at this."
    "Because I had no idea [mike.name] was such a mummy's boy!"
    bree.say "Okay, Angela..."
    bree.say "I really should have seen that one coming."
    bree.say "And you kind of guessed my question already."
    bree.say "But you never answered it."
    show angela normal
    "Angela nods, but her expression is a little hard to read as she does so."
    if angela.love >= 100:

        show angela happy
        angela.say "Of course I want to come to the party, [hero.name]."
        angela.say "Any chance to spend time with you is worth it."
        show angela smile
        "I feel a surge of relief as I get the answer I wanted."
        "And I'm already thinking of the things we can get up to on the night."
        "But there's still the proverbial elephant in the room."
        "The fact that I want to bring one of my housemates parents to the party."
        "So I feel like I should at least bring it up."
        bree.say "That's great, Angela!"
        bree.say "But..."
        bree.say "You think [mike.name]'s going to be okay with it?"
        show angela happy
        "Angela gives me an indulgent smile and shakes her head."
        angela.say "[mike.name]'s a big boy now, [hero.name]."
        show angela talkative
        angela.say "And I spent a large part of my life devoting it to him."
        angela.say "The least he can do now is accept that I'm a woman with needs."
        show angela happy
        angela.say "And if not, then it's a lesson he needs to learn!"
        show angela normal
        "I nod, feeling relieved by Angela's answer."
        bree.say "Okay, well..."
        bree.say "It's a costume party, so get creative!"
        show angela happy
        angela.say "Oh, don't worry, [hero.name]..."
        angela.say "I already have some good ideas."
        angela.say "But you'll have to wait until the party to see what I come up with."
        show angela smile
        "I nod eagerly, unable to contain my curiosity at what Angela will be wearing."
        $ game.flags.halloween_girl = "angela"
    else:

        show angela talkative
        angela.say "I'd love to go to the party with you, [hero.name]..."
        angela.say "But don't you think it'd be a little unfair on [mike.name]?"
        show angela normal
        "I feel a twist in my guts as the disappointment hits me."
        "I should have known that this would be the thing that sank me."
        "Of course Angela's going to think of [mike.name] first."
        "She's his mother, after all - and that's an impossibly strong bond."
        bree.say "Ah..."
        bree.say "He's a big boy now, Angela..."
        bree.say "All grown-up and a credit to you as well."
        bree.say "Don't you think he can handle seeing us together?"
        show angela smile
        "Angela gives me an indulgent smile."
        "But at the same time she shakes her head too."
        "Letting me know that she's about to put me in my place in the nicest way possible."
        show angela happy
        angela.say "Oh, [hero.name]..."
        angela.say "All of that may be true."
        show angela talkative
        angela.say "But a mother has to think of her children."
        angela.say "No matter what she might want for herself."
        angela.say "If you ever become a mother yourself, you'll understand."
        show angela normal
        "All I can do is nod and try to put a smile on my face."
        "Because I know that Angela's just put the argument beyond me."
        "Once she starts talking about the sacred status of motherhood, it's all over."
        "I might as well make the most of it and save myself any further humiliation."
        bree.say "Okay, Angela..."
        bree.say "Answer accepted."
        bree.say "I'm sure we can make up for it another time."
        show angela smile with dissolve
        "Angela's smile becomes wider and warmer as I say all of this."
        "As she accepts my surrender and acknowledges it too."
        show angela happy
        angela.say "I knew you'd understand, [hero.name]."
        angela.say "And thank you again for the invitation."
        angela.say "It was very thoughtful of you."
    hide angela with fade
    return

label angela_halloween_arrival_female:
    scene bg house
    "I thought I was prepared to see Angela standing on the doorstep tonight."
    "Because I've seen so many Halloween costumes in my time."
    "What could she possibly be wearing that would take me by surprise?"
    "Oh, but how wrong I was!"
    show angela halloween happy with dissolve
    angela.say "Hi, [hero.name]..."
    angela.say "You like my costume?"
    show angela smile
    bree.say "Buh..."
    bree.say "Urgh..."

    "I'm left speechless at the sight of Angela dressed as Rogue."
    "Thigh-high boots, long gloves, and a tight bodysuit that doesn't leave much to the imagination!"
    show angela surprised
    angela.say "Oh dear..."
    angela.say "Are you feeling okay?"
    show angela fragile
    "I finally manage to get my brain back in gear."
    "And a quick shake of the head sees me able to speak again."
    bree.say "I'm fine, Angela..."
    bree.say "It's just your costume."
    bree.say "It kind of left me speechless back there!"
    show angela smile
    "Angela beams with delight at my compliments."
    show angela at center, traveling(1.8, 1.7, (440, 1170))
    "And she looks over my shoulder into the house."
    show angela a disappointed with dissolve
    angela.say "Oh my..."
    show angela worried at center, traveling(1.8, 0.3, (640, 1170))

    angela.say "You don't think [mike.name]'ll disapprove of my costume, do you?"
    show angela fragile with dissolve
    menu:
        "Compliment":
            "I let out a snort of amusement at the question."
            "And I wave my hand in the air, dismissing Angela's concerns."
            bree.say "Who cares if he does, Angela?"
            bree.say "You're my date tonight."
            bree.say "And you're his step-mom, remember?"
            show angela smile at startle(0.05, -10)
            "Angela seems to be reassured by my answer."
            show angela b at center, traveling(1.8, 0.1, (640, 1150))
            "Because she stands up a little straighter than before."
            "And this in turn means her breasts are thrust out more proudly too."
            "In fact, I have to take a step backwards to avoid being poked in the eye!"
            "Luckily for me, Angela seems to take this as an invite to step inside."
            "So I don't hesitate to usher her into the hallway."
            "And call me a little cruel if you like."
            "But I for one can't wait to see [mike.name]'s reaction."
            "Especially as I turn to follow Angela's butt into the house."
        "Criticize":
            "I can't help bristling a little when Angela asks the question."
            "After all the bother I went through to get her to come in the first place."
            "Wasn't she the one that assured me [mike.name] needed to get used to this kind of thing?"
            "Now she's asking me if his seeing her assets on show is too much!"
            bree.say "Well if he does, then it's not my problem."
            bree.say "And maybe you should have thought about that, Angela."
            bree.say "You know, before you showed up with everything on display?"
            show angela surprised at startle(0.05, -10)
            "Angela looks taken aback by my words."
            show angela grudge at hshake
            "She stiffens a little, standing up straighter than before."
            show angela disappointed with dissolve
            pause 0.7
            show angela talkative
            angela.say "I was only asking your opinion, [hero.name]."
            angela.say "There's no need to be so sharp with me!"
            show angela normal
            bree.say "We're supposed to be having a party, Angela."
            bree.say "And we're also supposed to be a bunch of adults."
            bree.say "I think [mike.name] can cope with seeing some tits and ass!"
            show angela sad
            "Angela still doesn't seem pleased with my attitude."
            show angela fragile at hshake
            "And she does the best she can to cover up as she steps into the house."
            "But at least she's actually in there."
            "So I can worry about making it up to her later."
    return

label angela_halloween_party_female:
    $ game.pass_time(2)
    scene bg kitchen
    with dissolve
    mike.say "No, mom..."
    mike.say "It is NOT okay!"
    angela.say "P...please, honey..."
    angela.say "You're making a scene!"
    angela.say "All of your friends are looking at us..."
    "I recognise both of the raised voices as soon as I hear them."
    "And I hurry over as quickly as I can, already preparing to intervene."
    "Looks like my worst fears about inviting Angela to the party have come true."
    scene bg livingroom
    show angela halloween worried at right5
    show mike halloween upset at left5
    with dissolve
    "Because as soon as I get over there, I see her and [mike.name] engaged in an argument."
    show angela disappointed with dissolve
    "Or more accurately, he's the one doing most of the arguing."
    show angela annoyed with dissolve
    "Angela seems to be doing all that she can to calm the situation down."
    show mike at hshake
    "But [mike.name]'s having none of it."
    "And as soon as I get involved, he rounds on me too!"
    bree.say "Settle down, [mike.name]!"
    show mike shout
    mike.say "No, [hero.name]..."
    show mike angry
    mike.say "I will not settle down!"
    mike.say "What were you thinking inviting my mom to the party?"
    show mike shout
    mike.say "What was she thinking coming along?"
    show mike upset
    menu:
        "Defend Angela":
            "I've never really seen [mike.name] get like this before."
            "He's normally so calm and chilled-out."
            "He's actually kind of scaring me right now."
            "But that's not going to stop me from standing up to him."
            bree.say "Angela's a grown woman, [mike.name]."
            bree.say "And you're supposed to be a grown man too."
            bree.say "But right now, you're acting like spoiled child!"
            "[mike.name] seems to hear what I'm saying."
            show mike annoyed
            "And he even appears to calm down a little too."
            "But I can still see that he's pretty pissed."
            show mike talkative
            mike.say "I know all that, [hero.name]..."
            mike.say "This is just hard, you know?"
            mike.say "I can't be cool with it overnight!"
            show mike annoyed
            show angela worried
            angela.say "It's hard for me too, honey."
            angela.say "But you know I still love you, right?"
            show mike blush with dissolve
            angela.say "Me dating again doesn't change that."
            "[mike.name] gives Angela a curt nod."
            hide mike with easeoutleft
            "But then he stalks off, leaving us alone."
            bree.say "I think that's the best we can hope for, Angela."
            bree.say "I'm sure he'll come around in the end."
            show angela disappointed
            angela.say "Ah..."
            show angela fragile
            angela.say "I hope so, [hero.name]."
            angela.say "And I hope this hasn't ruined the party?"
            bree.say "No, Angela - we can put it behind us."
        "Defuse the situation":
            "I've never really seen [mike.name] get like this before."
            "He's normally so calm and chilled-out."
            "He's actually kind of scaring me right now."
            "But then he does have a right to be feeling that way."
            "It can't be easy to be handling all of those emotions."
            "So I need to keep that in mind and protect Angela at the same time."
            bree.say "Whoa..."
            bree.say "I think we all need to calm down."
            "I look around until I see Sasha."
            "And then I wave her over."
            show sasha halloween with easeinleft
            bree.say "Sasha, can you take [mike.name] for a breath of fresh air?"
            show sasha talkative
            sasha.say "Sure thing, [hero.name]..."
            show sasha embarrassed
            sasha.say "Come on, [mike.name]."
            show mike annoyed
            "For a moment I think [mike.name]'s going to refuse."
            hide mike with easeoutleft
            hide sasha with easeoutleft
            "But then he lets Sasha take his arm and lead him away."
            "Though not before he's shot Angela and me a stern look."
            show angela disappointed at center, traveling(1.6, 1.6, (640, 1070))
            angela.say "Oh dear..."
            show angela talkative
            angela.say "I really think you should have let me talk to him, [hero.name]."
            show angela normal
            bree.say "Are you crazy?"
            bree.say "The mood he was just in?!?"
            "Angela shakes her head in that annoying way of hers."
            "Letting me know that she's sure I just don't understand."
            show angela talkative
            angela.say "I'm his mother, [hero.name]!"
            angela.say "I might not have given birth to him."
            angela.say "But I raised him, and that means I know him better than anyone."
            angela.say "I could always get through to [mike.name] when nobody else could."
            show angela disappointed
            "Well that makes me feel like all of my efforts were for shit!"
            "Maybe next time I won't bother at all."
    return

label angela_halloween_dance_female:
    $ game.pass_time(2)
    scene bg livingroom
    show angela halloween zorder 9 at center, zoomAt(1.8, (320, 1170))
    show jack happy halloween zorder 1 at swing(1.0, 0.8, 1.0, -0.7, 0.6), center, zoomAt(1, (440, 900))
    show sasha happy halloween zorder 2 at swing(1.0, 0.8, 1.0, -0.7, 0.6), center, zoomAt(1, (900, 900))
    show mike b happy halloween zorder 3 at swing(1.0, 0.8, 1.0, -0.7, 0.6), center, zoomAt(1, (700, 900))
    with dissolve
    "Angela and I are standing on the edge of the dancefloor."
    "And it's starting to feel like we've been here forever."
    "I keep on glancing over at where other guests are dancing."
    "And then back at Angela in the hope of her getting the hint."
    "I'm actually pretty sure she knows what's up."
    "But for some reason she won't bite."
    "So in the end, I decide to call her bluff."
    bree.say "Angela..."
    bree.say "I really want to dance!"
    bree.say "Are you going to come dance with me, or what?"




    show angela lose
    angela.say "I want to, [hero.name]."
    show angela afraid blush with dissolve
    angela.say "It's just..."
    show angela shy
    angela.say "I didn't hit the dance floor since a while and..."
    angela.say "I'm worried about ruining the mood!"
    show angela sad
    menu:
        "Stay with Angela":
            "I really want to pull Angela onto the dancefloor."
            "To make her do what I want in spite of her protests."
            "But she already agreed to come to the party as my date."
            "Even though being here with [mike.name] could make things awkward."
            "So I dismiss the thought and give Angela a nod instead."
            bree.say "Okay, Angela..."
            bree.say "The last thing we want is you being frustrated!"
            show angela smile at startle(0.2, 5)
            "Angela smiles and nods, clearly relieved at my answer."
            show angela talkative
            angela.say "You go dance if you want to, [hero.name]."
            show angela fragile
            bree.say "No, I'm good."
            bree.say "I'm going to stay right here."
            $ angela.love += 2
        "Dance without Angela":
            "If Angela doesn't want to dance, then that's okay."
            "But it doesn't mean that I have to miss out too."
            bree.say "Okay, Angela..."
            bree.say "I'll just go and dance on my own then."
            "Angela raises her hand and opens her mouth."
            "As if she's going to say something."
            "But then she lowers it and purses her lips."
            "I take this as permission to go right ahead."
            hide angela with easeoutleft
            pause 0.3
            show bg livingroom at center, zoomAt(1.2, (640, 920))
            show jack happy halloween zorder 1 at swing(1.0, 0.8, 1.0, -0.7, 0.6), center, zoomAt(1.6, (340, 1400))
            show sasha happy halloween zorder 2 at swing(1.0, 0.8, 1.0, -0.7, 0.6), center, zoomAt(1.6, (1100, 1400))
            show mike b happy halloween zorder 3 at swing(1.0, 0.8, 1.0, -0.7, 0.6), center, zoomAt(1.6, (680, 1400))
            with dissolve
            "And in a couple of moments I'm on the dancefloor."
            "For a short while I can see Angela watching me."
            "She seems to be more than a little uncomfortable."
            "But soon enough I lose myself in the music."
            "And I stop gazing in her direction the rest of the time I'm dancing."
    return

label angela_halloween_sex_female:
    scene bg livingroom
    with dissolve
    "The party's been going a good few hours now, and the atmosphere is better than it's ever been."
    "We're well past the point where I have to worry about things not working out or going wrong."
    "All of the guests seem to be in a good mood, and the general vibe is moving towards chilled."
    "So now would be a good time to sit back and just enjoy the fruits of my labour."
    "And I intend to do just that, until I feel the sensation of someone taking my hand."
    show angela halloween a at center, zoomAt(4, (100, 1220))
    show bg livingroom at center, zoomAt(2, (640, 720))
    with dissolve
    "I look down to where fingers are intertwining themselves with mine."
    "Then I follow the line of the arm that the hand is attached to all the way up."
    show angela smile a at center, traveling(4, 1, (640, 2550))
    show bg livingroom at center, traveling(2, 1, (840, 920))
    "And I find myself looking into Angela's eyes."
    "She's giving me one of those knowing half-smiles."
    "And for a moment, her eyes dart away, looking towards the stairs in the hallway."
    "As soon as they're looking into mine again, I think I know what she's asking me."
    bree.say "Angela..."
    bree.say "You want to..."
    show angela happy
    angela.say "Y...yes..."
    angela.say "Well...if you do?"
    show angela smile
    "I take one last, quick look around the room."
    "And then I nod my head."
    "That's all it takes for the both of us to be agreed, to be set on the same path."
    "Together we make it across the room and into the hallway, winding between everyone in our path."
    "We try to go as fast as we can, but at the same time keep it looking like we're being nonchalant."
    "So I guess the image of it all must be pretty crazy to watch."
    "But all I know is how fast my heart is beating inside of my chest."
    "That and how tightly Angela is squeezing my hand right now."
    "As soon as we make it to the hallway, Angela takes the lead."
    "She practically drags me after her, making me hurry to keep up."
    "And the need to quicken my pace means that I'm not thinking straight when we reach our destination."
    "My mind doesn't clear until we're through a door and Angela closes it behind us."
    "It's only then that I'm able to look around and realise something important."
    scene bg black
    show bg bedroom1
    show angela halloween
    with fade
    bree.say "Angela..."
    show bg bedroom1 at center, traveling(1.2, 1, (640, 770))
    show angela at center, traveling(1.6, 1, (640, 1070))
    bree.say "This isn't my room!"
    bree.say "This is..."
    show angela happy
    angela.say "[mike.name]'s room - I know, I know."
    show angela smile
    "I hear the sound of the lock on the door clicking, sealing us inside."
    "Then Angela turns and takes hold of my hand for a second time."
    "Now pulling me towards [mike.name]'s bed!"
    bree.say "But we can't do this here!"
    bree.say "We should go to my room instead."
    "Angela shakes her head, still pulling me towards the bed."
    "And I have to admit that, for all my protests, I'm not resisting as much as I could."
    show angela talkative
    angela.say "No, [hero.name]..."
    angela.say "I want to do it here, in [mike.name]'s room."
    show angela smile
    bree.say "Why here?"
    bree.say "Aren't you worried this could get weird?"
    show angela talkative
    angela.say "Oh, [hero.name]..."
    angela.say "This whole thing between us is already weird."
    angela.say "With all that we've been through to get here..."
    show angela happy
    angela.say "How could it be anything else?"
    show angela smile
    "I've got to admit, Angela does have a point."
    show angela talkative
    angela.say "Don't you see?"
    show angela happy
    angela.say "If we can do this here, then we can do anything!"
    show angela smile
    "I'm in the act of opening my mouth to answer, the words already forming."
    "But that's when Angela grabs hold of me with her other hand too."
    "And then she tosses me bodily onto the bed!"
    "I'm taken completely by surprise."
    "Firstly by the fact she's decided to close end the discussion there."
    "And secondly by how strong she actually is!"
    "I barely have time to realise that I'm laid on my back before she pounces."
    "And I do mean pounces!"
    scene bg black
    show angela finger bree halloween bedroom1
    "In the next second, Angela lands on top of me, pinning me to the bed."
    "Again I find myself reminded of Angela's size advantage."
    "She effortlessly uses her legs to press down on mine."
    "And she also manages to pin my arms above my head too."
    "But none of that means that I'm struggling for a moment."
    "Because as soon as she leans down over me, all of my reservations seem to disappear."
    "By the time Angela's leaned in close enough to kiss me, I'm pulling up to meet her."
    "And the moment that our lips meet, I know there's going to be no holding back."
    "Angela seems to know this too, because she releases my arms."
    "This leaves her hands free to begin roaming over my trapped body."
    "She tries to explore me and undress me at the same time."
    "One task mixing with the other until there's no way to tell them apart."
    "At the same time I'm also trying to undress Angela too."
    "So little by little, we strip away what each other is wearing."
    "The angle she's at helps to make Angela's job easier than mine."
    "And so I'm almost naked long before she is."
    "But gravity also seems to be on her side as well."
    "Because as soon as I open the back of her costume, it takes effect."
    show angela finger bree naked with fade
    "This means that Angela's formidable bosom almost hits me in the face!"
    "And even though I'm spared that fate, the sight stops me in my tracks."
    "All I can do is lie there and stare up at them as they obscure my view."
    "I can hardly make out Angela's face above me as she chuckles at my reaction."
    angela.say "Oh, [hero.name]..."
    angela.say "You look like you've been hypnotised!"
    bree.say "W...wasn't that..."
    bree.say "Wasn't that part of your act?"
    "Angela nods at this."
    angela.say "Sure it was - but I never used my breasts before now!"
    angela.say "And I was never a one-trick pony, you know?"
    angela.say "I was also really good at sleight-of-hand..."
    "It's only as she says this that I realise what Angela has in mind."
    "Because the entranced look on my face changes in that moment."
    "Instead my expression becomes one of helpless pleasure."
    "And it happens as I feel Angela's hand slide between my thighs!"
    "Just like all of the other actions she's taken before, she's not playing either."
    "Angela's fingers find their prize quickly and without fail."
    "Before I know it, they're stroking and teasing me."
    "And it doesn't take long for the effects to sweep my senses."
    "Angela's not fumbling in the dark here, she knows exactly what she's doing."
    "Her natural knowledge of a woman's body is accompanied by years of experience."
    "So all of that is being focussed on my pussy as she traces it's outline."
    "I can't make a sound the whole time, so instead I nod eagerly."
    "This seems to please Angela, a smile spreading across her face."
    "And she rewards me by beginning to spiral inwards down there."
    "Each orbit her fingers complete brings them closer, deeper."
    "And it makes the sensations I'm feeling that much more intense too."
    "It has to be an illusion, but I swear they redouble every time."
    show angela finger bree pleasure
    "On top of this, I have the sight of Angela's chest before me too."
    "Her breasts sway in time with her movements."
    "Part of me wants nothing more than to reach out and touch them."
    "But the hold she has on me seems to paralyse my entire body."
    "All I can do is lie there, helpless as she has her way with me."
    show angela finger bree normal blush
    "I feel like I've been here forever, like time's lost it's meaning."
    "But all of that changes as I feel Angela's fingers slip inside of me."
    "They travel deep, again knowing exactly where to go and what to seek."
    "And when they reach their ultimate destination, it's just too much."
    show angela finger bree pleasure
    "For all of Angela's weight pinning me down, now I manage to move."
    "As she makes me lose it, my back arches, lifting off the mattress."
    "Of course, all this does is push her probing fingers deeper still."
    show angela finger bree ahegao squirt sparks
    "I can only hold the position for a few seconds, muscles quaking the whole time."
    "And then the strength just seems to drain out of me, and I collapse onto the bed."
    "Angela lies at my side, stroking my hair as I slowly recover."
    scene bg black
    show bg bedroom1 at center, zoomAt(1.2, (640, 770))
    show angela naked at center, zoomAt(1.6, (640, 1070))
    with fade
    "Once we're able, we dress and make ourselves look as decent as possible."
    show angela -naked halloween with dissolve
    "Then we sneak to the door and listen for anyone outside."
    hide angela with dissolve
    show bg bedroom1 at center, traveling(2, 2, (240, 1420))
    "I'm sure it's clear, so I flip the lock and slip out into the corridor."
    "But I almost leap backwards when I see Jack standing out there." with vpunch
    "At first the door means that he can't see me."
    "And instead of shock, I get a conspiratorial chuckle."
    jack.say "Uh, sorry, [mike.name]..."
    jack.say "I was just passing, that's all."
    jack.say "But...like...way to go man!"
    jack.say "Sounded like you were having fun in there, yeah?"
    "There's not enough time for me to duck back into [mike.name]'s bedroom."
    "And Angela doesn't even hear what Jack's saying."
    scene bg black
    show bg livingroom
    with vpunch
    "Because she almost pushes me over as she follows me out of the door."
    "This in turn sends the door swinging into Jack."
    show jack halloween with easeinleft
    "He jumps back, finally seeing who's really emerging from the room."
    show jack perv
    "But even then he doesn't seem to believe his eyes."
    "He looks from me to Angela and back again."
    show jack guilty with dissolve
    "And before he can say a word, we hurry back to the party."
    "I have no idea what Jack will do after what he heard and saw."
    "We'll just have to hope that he stays in that stunned state of silence."
    "At least until the party is over and everyone's gone home."
    $ angela.sexperience += 1
    $ game.pass_time(1)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
