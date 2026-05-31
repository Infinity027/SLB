label shiori_date_intro_valentine_male:
    mike.say "Happy Valentine's day, Shiori."
    mike.say "And I just wanted to say..."
    mike.say "I can't think of anyone I'd rather have as my valentine!"
    "Shiori's eyes light up at my words, and she clasps her hands together."
    shiori.say "D...do you really mean that?!?"
    mike.say "Of course I do, Shiori."
    mike.say "You're the most special person in the world to me!"
    "Shiori throws her arms around me, hugging me and refusing to let go."
    return

label shiori_date_intro_halloween_male:
    mike.say "Hey, Shiori - no Halloween costume?"
    "The moment she hears the question, Shiori begins to shake her head."
    shiori.say "Oh dear...was I supposed to wear a costume?"
    shiori.say "I must have forgotten all about it - I'm such a scatter-brain!"
    "I hold my hands up, trying to stop Shiori chastising herself."
    mike.say "Whoa, Shiori, it's okay!"
    mike.say "We never agreed to Halloween costumes - I was just kidding!"
    "Shiori looks instantly relieved to hear this."
    shiori.say "Oh, thank goodness!"
    shiori.say "But...I could wear a costume next Halloween, if you like?"
    return

label shiori_date_intro_christmas_male:
    shiori.say "Happy Christmas, [hero.name]."
    shiori.say "And thank you so much for choosing to spend it with me!"
    "Shiori clings to my arm, looking up at me with sheer adoration in her eyes."
    "My heart swells at the sight, making me want to protect her with all my strength."
    mike.say "There's nobody else I'd rather be with, Shiori."
    mike.say "And all I want for Christmas this year is you."
    return

label shiori_date_intro_birthday_male:
    mike.say "Happy birthday, Shiori!"
    mike.say "I'm going to make this the best birthday ever."
    mike.say "Just because you're so special!"
    shiori.say "Oh, [hero.name]!"
    shiori.say "Do you really mean that?"
    shiori.say "Oh my goodness - I feel like the luckiest girl in the world!"
    return

label shiori_date_intro_mc_birthday_male:
    shiori.say "Happy birthday, [hero.name]!"
    shiori.say "And don't you worry - I'll make sure our date is extra special!"
    mike.say "Oh...thank you, Shiori!"
    mike.say "It's so sweet of you to remember my birthday."
    shiori.say "Of course I did, [hero.name]!"
    shiori.say "I want to be the best girlfriend in the world."
    shiori.say "Because that's what you deserve!"
    return

label shiori_date_eat_a_burger:
    "Shiori seems to think it's a source of great joy to be eating a burger with me in public."
    "Not once does she stop giggling and grinning like a giddy little kid."
    "In fact, I'm surprised that she doesn't give herself serious wind!"
    return

label shiori_date_buy_drink:
    if shiori.is_visibly_pregnant:
        show shiori angry
        $ shiori.love -= 10
        shiori.say "Oh...how could you, [hero.name]?"
        shiori.say "You know I can't drink when I'm pregnant!"
        shiori.say "I thought you cared about me and the baby?!?"
        $ hero.cancel_activity()
        hide shiori
    else:
        "When we order drinks, Shiori acts as though she's got literally no idea what to do or say."
        "In the end, I have to choose a drink for her."
        "And when it arrives, she looks at it with genuine fascination."
        "By the look of her, you'd think she was about to drink some fantastical magic potion."
    return

label shiori_date_play_darts:
    "Shiori obligingly steps up to the oche, but she's visibly flustered by the darts in her hand."
    "I'm not sure whether she's more scared of the sharp points, or else of being embarrassed in public."
    "Eventually, she does pluck up the courage to throw them."
    "And one even manages to hit the board before it bounces off and into the crowd."
    return

label shiori_date_pub_play_pool:
    "Shiori clearly doesn't have the first clue about playing pool."
    "She stares at the cue in her hand like it was a loaded gun."
    "It's all that I can do to make sure she hits the cue ball, let alone anything else."
    return

label shiori_date_buy_a_round:
    if shiori.is_visibly_pregnant:
        show shiori angry
        $ shiori.love -= 10
        shiori.say "Oh...how could you, [hero.name]?"
        shiori.say "You know I can't drink when I'm pregnant!"
        shiori.say "I thought you cared about me and the baby?!?"
        $ hero.cancel_activity()
    elif (hero.charm >= 60 - shiori.love and shiori.flags.drinks < 2):
        show drink shiori
        "When I offer to buy another round, Shiori smiles sweetly."
        "But her expression clearly says that she's not bothered either way."
        "Maybe she's just not that big of a drinker?"
        $ game.active_date.score += 5
        if "rebel" in shiori.traits:
            $ game.active_date.score += 5
        $ shiori.set_flag("drinks", 1, "day", mod="+")
        hide drink
    else:
        "I want to pay a round of beers to the whole pub."
        "But Shiori doesn't seem to want to drink, so I refrain from doing so."
        $ hero.cancel_activity()
    return

label shiori_dance_with:
    "Though she's a little clumsy and lacking in confidence, Shiori gives it her all once she's on her feet."
    "And it's the enthusiasm that she seems to have for just being on the dance-floor with me that wins me over."
    "It makes me begin to feel the exact same way about her too."
    return

label shiori_date_play_arcade_intro_male:
    shiori.say "Oh dear..."
    shiori.say "I don't think this is my kind of place, [hero.name]!"
    shiori.say "I mean, I HAVE played with Kanta on his Zbox."
    shiori.say "But I've never been any good at it!"
    "I try to give Shiori my most reassuring smile as she hangs off my arm."
    "But at the same time I can feel the irresistible pull of the games around me."
    "I had to try pretty hard to convince her the arcade was a good idea."
    "And I don't want her running off now that we're here."
    mike.say "Don't worry, Shiori."
    mike.say "I'll bet Kanta only plays new games, right?"
    mike.say "One's that are really complicated?"
    shiori.say "Erm...I suppose so, [hero.name]."
    mike.say "Well, most of these are really old games."
    mike.say "Classics, you know?"
    mike.say "They're much easier to play, Shiori."
    shiori.say "If you say so, [hero.name]."
    mike.say "Let's try this one - 'Bubble Booble'!"
    "Shiori looks on with an expression of concern."
    "But I'm already shoving coins into the slot."
    shiori.say "Are those...dragons?"
    shiori.say "Dragons with breasts?!?"
    mike.say "Don't worry about the dragon breasts, Shiori."
    mike.say "Just watch me and you'll be playing in no time at all!"
    return

label shiori_date_play_arcade_win_male:
    "Pretty soon I'm concentrating on the game and nothing else."
    "Which means I have no idea if Shiori's taking my advice."
    "But from what I can hear, it's not making any difference either way!"
    shiori.say "Oh...oh my..."
    shiori.say "What does this button do?"
    shiori.say "Oh goodness - I made it blow a bubble!"
    shiori.say "How do I make it do that again?!?"
    mike.say "It can't be that hard, Shiori."
    mike.say "There are only two buttons!"
    "Shiori blunders her way through the rest of the game."
    "And she punctuates everything she does with more worried exclamations."
    "By the time we've exhausted all of our credits, she's almost in tears!"
    shiori.say "Can we stop now, [hero.name]?"
    shiori.say "Please don't make me play again!"
    shiori.say "I'll do anything if you say I don't have to play again!"
    mike.say "Geez, Shiori - calm down!"
    mike.say "We won't play again, okay?"
    "Shiori breathes a sigh of relief."
    "And she wraps her arm in mine again."
    mike.say "Now then, Shiori."
    mike.say "About that promise to do anything..."
    return

label shiori_date_play_arcade_lose_male:
    "I try to focus on the game and tune out Shiori's pleas for help."
    "But she keeps on asking her questions, and I get ever more distracted."
    "And to make things worse, she seems to be benefiting from my advice too!"
    shiori.say "Oh...I see what that button does!"
    shiori.say "And this one too..."
    shiori.say "He he...I made the dragon's boobs bounce!"
    mike.say "Quit jabbering in my ear, Shiori."
    mike.say "You're distracting me!"
    "If she hears me at all, Shiori chooses to ignore what I said."
    "Instead she continues to prattle on all the time we're playing."
    "And as she seems to be getting into the swing of it, I'm falling behind."
    "By the time we've exhausted our credits, I'm almost crying tears of frustration!"
    mike.say "Can we stop now, Shiori?"
    mike.say "Please, don't make me play again!"
    shiori.say "Are...are you serious, [hero.name]?"
    shiori.say "I thought you loved this kind of thing?"
    mike.say "I don't know, Shiori..."
    mike.say "I just feel like I can't concentrate today, you know?"
    shiori.say "Aw, poor you, [hero.name]!"
    shiori.say "Let's go sit down somewhere quiet."
    shiori.say "And I can tell you all about how I won the game!"
    return

label shiori_dick_reactions:
    if not shiori.flags.seendick:
        $ shiori.flags.seendick = 1
        if hero.has_skill("hung"):
            show dick reactions shiori scared
            shiori.say "Oh dear...oh dear..."
            shiori.say "You never said it would be THAT big!"
            mike.say "Don't worry, Shiori - I promise I'll be gentle."
            shiori.say "R...really?"
            show dick reactions shiori smile
            shiori.say "Well...okay - if you say so..."
            $ shiori.sub += 10
        elif hero.has_skill("smalldick"):
            show dick reactions shiori smile
            shiori.say "Oh...so neat!"
            mike.say "Are...are you saying it's small?!?"
            shiori.say "Oh no - it's perfect!"
            shiori.say "The bigger they are, the more they hurt."
            shiori.say "I like it when someone's gentle with me..."
            $ shiori.sub -= 10
        hide dick reactions
    return

label shiori_halloween_invitation:
    show shiori
    "I know from the start that Shiori's the girl I want to ask along to the Halloween party."
    "It just feels right, and I can see her having a great time with all the people that'll be there."
    "And from my point of view, it means I'll have the chance to spend most of the night with her too."
    "All in all, it feels like the perfect way to celebrate Halloween and have fun with Shiori at the same time."
    "So as soon as I get the chance, I don't hesitate to ask her to the party."
    mike.say "Shiori..."
    mike.say "Have you got anything planned for Halloween?"
    show shiori surprised
    "Shiori's eyes open wide at the question."
    "And she looks suddenly surprised as well."
    shiori.say "Oh..."
    shiori.say "Halloween?"
    show shiori normal
    shiori.say "No, [hero.name], I haven't."
    shiori.say "Normally I just take Kanta trick or treating!"
    "I nod, feeling a little guilty at pushing past Shiori's explanation."
    "But if I don't do that, I'll never get to the point."
    mike.say "Well..."
    mike.say "We're having a Halloween party at my place."
    mike.say "And I'd like you to come along - as my date."
    show shiori surprised
    "Shiori's eyes go wider still."
    "And she begins to blush too."
    shiori.say "A party?"
    show shiori happy
    shiori.say "Oh, [hero.name] - that's so kind of you to invite me!"
    mike.say "Sure, Shiori, sure."
    mike.say "But are you going to come or not?"
    if shiori.love >= 100:
        show shiori normal
        "Shiori nods her head slowly."
        "And the speed of the nods quickly increases."
        "Which means I can feel my heart quickening too!"
        shiori.say "Normally I take Kanta trick or treating on Halloween."
        shiori.say "But this year he wanted to go with one of his school friends and his mom."
        shiori.say "I was going to say no, but if let him..."
        mike.say "Then you could come to the party?"
        $ shiori.love += 1
        show shiori happy
        "Shiori nods and smiles."
        "Clearly she's happy to be able to please me."
        show shiori normal
        shiori.say "Kanta's father always used to take him trick or treating."
        shiori.say "And I tried to keep it up as a tradition to make him happy."
        shiori.say "But maybe it's time I started to let go of things like that?"
        show shiori flirt
        shiori.say "And...you know, made some new traditions of my own?"
        "Shiori takes hold of my hand as she says this."
        "And I can feel a smile spreading across my face too!"
        $ game.flags.halloween_girl = "shiori"
    else:
        show shiori sad
        "Shiori shakes her head slowly."
        "But I can see regret in her eyes."
        "She wants to say yes."
        "But something's stopping her."
        shiori.say "I can't, [hero.name]."
        shiori.say "I have to make sure Kanta gets to go trick or treating."
        shiori.say "It was something his father used to do with him."
        shiori.say "And he'd be heartbroken if I didn't take him!"
        "In want to argue with Shiori, to make her change her mind."
        "But I know how much she loves her son."
        "And I also know how tough the kid's had it since his father left them."
        "So it'd be selfish to pressure her into doing what I want."
        mike.say "It's okay, Shiori."
        mike.say "I understand that you have to be there for Kanta."
        $ shiori.love += 1
        show shiori normal
        "Shiori smiles up at me, genuinely happy with my response."
        "Maybe I didn't get what I wanted this time."
        "But I feel like I did the right thing."
        "And earned some points with Shiori at the same time too."
    return

label shiori_halloween_arrival:
    if shiori.love < 150 and 'shiori_event_05' in DONE:
        call shiori_kanta_halloween_arrival from _call_shiori_kanta_halloween_arrival
    else:
        scene bg house
        with wiperight
        "My mind's not really focused on what I'm doing as I open the door."
        "Worries about the party are still running around inside my head."
        show shiori halloween with dissolve
        "But all of that disappears when I see what's standing in front of me."
        mike.say "Whoa..."
        mike.say "Those things are..."
        show shiori embarrassed
        shiori.say "Oh, I know, I know!"
        shiori.say "They're so tight, these kinds of costume."
        shiori.say "I almost couldn't get the thing on at all!"
        "I nod mechanically at Shiori's words, not looking her in the face."
        "And that's because I can't tear my eyes away from her chest!"
        "Normally it's distracting enough."
        "But now it's covered in skin-tight red and black-spotted latex rubber!"
        shiori.say "I'm sorry, [hero.name]."
        shiori.say "I must look so silly in this costume!"
        shiori.say "I just recognised it from a show that Kanta watches."
        shiori.say "I grabbed it without thinking..."
        mike.say "Bugwoman, Shiori."
        mike.say "The character's called Bugwoman."
        show shiori normal
        "Shiori gives me a helpless smile."
        shiori.say "Well, that would explain the colour!"
        shiori.say "You must think I look so ridiculous..."
        menu:
            "Disagree":
                mike.say "Are you crazy, Shiori?"
                mike.say "You look super hot in that costume!"
                mike.say "In fact, I wish you'd wear it more often."
                $ shiori.love += 1
                show shiori happy
                "Shiori's entire demeanour changes as I begin to compliment her."
                "She smiles broadly, beginning to blush."
                "And she even holds herself with more confidence."
                shiori.say "D...do you really mean that, [hero.name]?"
                show shiori normal
                shiori.say "I suppose it's okay for me to wear it then."
                shiori.say "So long as it makes you happy?"
                "My own smile is almost as broad as Shiori's."
                "And I can't help nodding my head eagerly too."
                mike.say "I love it, Shiori."
                mike.say "I don't think I'll be able to take my eyes off of you all night!"
                show shiori happy
                "Shiori takes hold of my arm, clinging to me tightly."
                "Then she all but drags me into the house."
            "Agree":
                mike.say "Yeah..."
                mike.say "It is a bit of an odd choice, Shiori!"
                $ shiori.love -= 2
                show shiori sad
                "Shiori nods at this, wringing her hands together."
                shiori.say "I knew it."
                shiori.say "I just knew it!"
                shiori.say "Oh, this is SO embarrassing."
                "I suddenly realise that I might have done the wrong thing here."
                "Shiori's supposed to be my date tonight."
                "And so what does it matter if I don't like her costume?"
                "At this rate she'll turn on her heel and run home again."
                "Which means I'll be left alone at my own party!"
                mike.say "Ah..."
                mike.say "Maybe you should come inside?"
                mike.say "There's fewer people to see you in here than out there!"
                show shiori surprised
                "Shiori almost yelps in alarm at the thought."
                "And she hurries inside as quickly as she can."
    scene bg black with dissolve
    pause 1
    return

label shiori_kanta_halloween_arrival:
    scene bg house
    with wiperight
    "My mind's not really focused on what I'm doing as I open the door."
    "Worries about the party are still running around inside my head."
    show shiori halloween with dissolve
    "But all of that disappears when I see what's standing in front of me."
    mike.say "Whoa..."
    mike.say "Those things are..."
    show shiori embarrassed
    shiori.say "Oh, I know, I know!"
    shiori.say "They're so tight, these kinds of costume."
    shiori.say "I almost couldn't get the thing on at all!"
    "I nod mechanically at Shiori's words, not looking her in the face."
    "And that's because I can't tear my eyes away from her chest!"
    "Normally it's distracting enough."
    "But now it's covered in skin-tight red and black-spotted latex rubber!"
    shiori.say "I'm sorry, [hero.name]."
    shiori.say "I must look so silly in this costume!"
    shiori.say "I just recognised it from a show that Kanta watches."
    shiori.say "I grabbed it without thinking..."
    mike.say "Ladybug, Shiori."
    mike.say "The character's called Ladybug."
    show shiori normal
    "Shiori gives me a helpless smile."
    shiori.say "Well, that would explain the colour!"
    shiori.say "You must think I look so ridiculous..."
    menu:
        "Disagree":
            mike.say "Are you crazy, Shiori?"
            mike.say "You look super hot in that costume!"
            mike.say "In fact, I wish you'd wear it more often."
            $ shiori.love += 1
            show shiori happy
            "Shiori's entire demeanour changes as I begin to compliment her."
            "She smiles broadly, beginning to blush."
            "And she even holds herself with more confidence."
            shiori.say "D...do you really mean that, [hero.name]?"
            show shiori normal
            shiori.say "I suppose it's okay for me to wear it then."
            shiori.say "So long as it makes you happy?"
            "My own smile is almost as broad as Shiori's."
            "And I can't help nodding my head eagerly too."
            mike.say "I love it, Shiori."
            mike.say "I don't think I'll be able to take my eyes off of you all night!"
        "Agree":
            mike.say "Yeah..."
            mike.say "It is a bit of an odd choice, Shiori!"
            $ shiori.love -= 2
            show shiori sad
            "Shiori nods at this, wringing her hands together."
            shiori.say "I knew it."
            shiori.say "I just knew it!"
            shiori.say "Oh, this is SO embarrassing."
            "I suddenly realise that I might have done the wrong thing here."
            "Shiori's supposed to be my date tonight."
            "And so what does it matter if I don't like her costume?"
            "At this rate she'll turn on her heel and run home again."
            "Which means I'll be left alone at my own party!"
            mike.say "Ah..."
            mike.say "Maybe you should come inside?"
            mike.say "There's fewer people to see you in here than out there!"
            show shiori surprised
            "Shiori almost yelps in alarm at the thought."
    show shiori embarrassed
    shiori.say "Ah..."
    shiori.say "About that, [hero.name]..."
    "Shiori steps aside to reveal that she's not alone."
    "Standing on the doorstep behind her is Kanta."
    "He's looking more than a little nervous."
    "And he's dressed as Kitty Noir, so he matches his mother."
    mike.say "Erm...hi, Kanta."
    mike.say "I thought you were going trick or treating tonight?"
    "Shiori starts wringing her hands at this."
    shiori.say "I'm so sorry, [hero.name]."
    shiori.say "That other mom I mentioned - she cancelled on me at the last minute!"
    mike.say "Well you can't bring him to the party, Shiori."
    mike.say "There's going to be loud music and people drinking."
    show shiori sad
    "I watch as a helpless look spreads across Shiori's face."
    "She honestly looks like she wants a hole to swallow her up right now!"
    mike.say "You're not coming to the party, are you?"
    "Shiori nods."
    shiori.say "No..."
    shiori.say "I'm going to take Kanta trick or treating around your neighbourhood instead."
    show shiori embarrassed blush
    "Shiori looks away for a moment and then back at me."
    "I can see that she's trying hard to say something."
    "Not able to meet my eye as she does so."
    shiori.say "I..."
    shiori.say "I could use some company."
    shiori.say "Or not..."
    "I look at Shiori and Kanta."
    "Then I look back at the house I spent so long decorating for the party."
    menu:
        "Stay at the party":
            mike.say "Any other time I would, Shiori."
            mike.say "But I put too much into this party."
            $ shiori.love -= 5
            show shiori sad -blush
            "Shiori looks instantly downcast."
            "But as always, she puts a brave face on."
            shiori.say "Oh..."
            shiori.say "Okay, [hero.name] - have a nice time!"
            shiori.say "Come on, Kanta."
            hide shiori
            $ game.flags.halloween_girl = "nodate"
            "I watch as she takes hold of her son's hand."
            "They walk away into the night, leaving without a date."
            "I can only roll my eyes and head back inside alone."
        "Go trick or treating":
            mike.say "Sure I'll come along, Shiori."
            mike.say "I can come back to the party later."
            $ shiori.love += 3
            show shiori happy -blush
            $ game.flags.halloween_girl = "shiori_kanta"
            "Shiori's face lights up at my answer."
            "And even Kanta seems to cheer up too."
            "Probably because he sees his mother happy and it's rubbing off on him."
            shiori.say "Really?!?"
            shiori.say "Oh, thank you, [hero.name]!"
            shiori.say "Did you hear that, Kanta?"
            shiori.say "[hero.name] is coming along too!"
            "Shiori practically beams as she takes my arm."
            "And we set off down the street."
            scene bg street
            show shiori halloween normal
            with fade
            "All three of us looking for likely doors to knock on."
            "But I notice that Kanta's looking a little nervous."
            "Like he's scared or something."
            "Maybe I should try to get him into the Halloween spirit?"
            menu:
                "Tell scary story":
                    mike.say "Hey, Kanta..."
                    mike.say "You want to hear a scary story?"
                    "Kanta's eyes go wide at this."
                    "And he looks at Shiori, then back to me."
                    "Kanta" "I...I guess so."
                    show shiori sad
                    shiori.say "Oh dear..."
                    shiori.say "I'm not sure this is a good idea!"
                    "I wave a hand in the air, dismissing Shiori's concerns."
                    mike.say "Ah, lighten up, Shiori."
                    mike.say "It's just a scary story, that's all!"
                    shiori.say "Oh dear, oh dear..."
                    mike.say "When I was a kid, there was a scary old lady who lived on my street."
                    mike.say "Everyone said she was a witch, and she sure as hell looked like one."
                    mike.say "And every Halloween, she'd give the trick or treaters sausage rolls!"
                    "Kanta" "Huh?!?"
                    "Kanta" "What about candy?"
                    mike.say "I know, right?"
                    mike.say "We all wanted candy, so we hated her for that."
                    show shiori annoyed
                    shiori.say "Oh, that's so mean!"
                    shiori.say "You should have been grateful what she gave you!"
                    mike.say "Whatever..."
                    show shiori normal
                    mike.say "Anyway, one year, my friend Jack decided to pay her back."
                    mike.say "I always remember because it was after his birthday and he got a sweet Power Rangers watch."
                    mike.say "Jack said he was going to sneak into the witch's house and pee in her teapot!"
                    "Kanta" "NO WAY!"
                    "Kanta" "And did he?!?"
                    mike.say "I don't know, Kanta."
                    mike.say "Because that was when Jack just disappeared."
                    mike.say "But you know what I found in my sausage roll that Halloween?"
                    "Kanta" "W...what did you find?"
                    show shiori surprised
                    mike.say "JACK'S POWER RANGERS WATCH IN THE SAUSAGE MEAT!"
                    "Kanta" "AAARRRGGGH!!!"
                    "Kanta throws his arms up in the air and runs off down the street."
                    $ shiori.love -= 2
                    $ shiori.sub += 1
                    hide shiori
                    "Shiori goes running after him, and I watch them go."
                "Knock on doors with Kanta":
                    mike.say "Hey, Kanta..."
                    mike.say "Let's hit that house over there!"
                    "Kanta's eyes go wide at this."
                    "And he looks at Shiori, then back to me."
                    "Kanta" "C...can I, Mom?"
                    "Shiori looks almost as stunned as Kanta himself."
                    "She nods and then stammers an answer."
                    shiori.say "O...of course you can..."
                    show shiori happy
                    shiori.say "Off you go then!"
                    hide shiori
                    "Together with Kanta, I hurry to the nearest front door."
                    mike.say "TRICK OR TREAT!"
                    "Kanta" "YEAH - TRICK OR TREAT!"
                    show shiori halloween happy
                    "As the candy changes hands, I glance back at Shiori."
                    "She's standing a little way off, watching us from the sidewalk."
                    "And she's smiling broadly, looking genuinely happy."
                    "The sight is so welcome that I can't help smiling back."
                    hide shiori
                    "After that we hit perhaps a dozen more houses on my street."
                    "Soon enough Kanta has more than enough candy in his pail."
                    "So Shiori calls time on us knocking on anymore doors."
                    show shiori halloween normal
                    "Kanta" "Aw..."
                    "Kanta" "Do we have to go home, Mom?"
                    "Kanta" "I'm having a so much fun!"
                    shiori.say "Yeah, Kanta, we do!"
                    shiori.say "[hero.name] has to get back to his party."
                    "She turns to me next, still smiling."
                    $ shiori.love += 5
                    hide shiori
                    show shiori kiss halloween
                    $ shiori.flags.kiss += 1
                    "Then she hops up and kisses me on the lips."
                    shiori.say "Thank you, [hero.name]."
                    shiori.say "You really made tonight feel special."
                    shiori.say "For the both of us!"
                    hide shiori
            "I wave Shiori and Kanta off as they disappear down the street."
            "And as I walk back to my place, I consider that a job well done."
            "Everybody got what they wanted in the end."
            "And I can still get in a good few hours of partying too!"
    return

label shiori_halloween_party:
    $ game.pass_time(2)
    scene bg livingroom
    with dissolve
    scottie.say "Aw, come on, babe."
    scottie.say "You can do better than that!"
    jack.say "Yeah - jump for it!"
    shiori.say "I...I can't reach."
    shiori.say "You're just being mean to me!"
    show shiori halloween embarrassed at left
    show scottie halloween perv at right4
    show jack halloween perv at mostright4
    with dissolve
    "I turn the corner to see a baffling scene before me."
    "Scottie's holding the drink I fixed for Shiori in the air."
    "And all the while, he and Jack are urging her to jump for it."
    "Every time Shiori tries, Scottie jerks it out of her reach."
    "And the whole time their eyes are fixed on Shiori's chest as it bounces in sympathy."
    "Just then, Shiori sees me, and hope fills her eyes."
    "Likewise, Scottie and Jack look like naughty schoolboys caught in the act."
    menu:
        "Defend Shiori":
            mike.say "What the hell are you jerks doing?!?"
            mike.say "We're not back in the school-yard!"
            show shiori normal
            show jack halloween normal
            show scottie sad
            "Shiori's face shows her gratitude at my stepping in to save her."
            "But Scottie and Jack suddenly don't know where to look."
            "They stare at the ground and mutter to themselves."
            "Which only serves to make them look even more like guilty kids."
            scottie.say "We were only playing around!"
            jack.say "It was just a game - that's all!"
            mike.say "Well Shiori didn't seem like she wanted to play!"
            mike.say "Quit it, or I'll kick you out the door myself!"
            hide jack
            hide scottie
            show shiori at center
            with easeoutright
            "Scottie and Jack slope away, still muttering."
            "And Shiori throws her arms around me."
            $ shiori.love += 2
            show shiori happy
            shiori.say "Oh..."
            shiori.say "My hero!"
        "Defend Scottie and Jack":
            mike.say "Don't stop on my account, Shiori."
            mike.say "This looks like a fun party game!"
            show shiori surprised
            "Shiori looks horrified at this."
            "But Scottie and Jack are instantly relieved."
            show shiori sad
            shiori.say "B...but..."
            shiori.say "They were laughing at me!"
            "I shake my head and roll my eyes."
            "Dismissing Shiori's pleas with a chuckle."
            mike.say "I think you'll find they were laughing with you, not at you, Shiori."
            mike.say "You need to lighten up a little, let yourself have some fun."
            scottie.say "That's right, man!"
            jack.say "My thoughts exactly!"
            $ shiori.love -= 4
            "I nod to Scottie, and he gets right back into it."
            "All three of us laughing as Shiori jumps up and down."
            "And pretty soon, her face is as red as her costume!"
    scene bg black with dissolve
    pause 1
    return

label shiori_kanta_halloween_party:
    $ game.pass_time(2)
    $ game.flags.halloween_girl = "nodate"
    return

label shiori_halloween_dance:
    $ game.pass_time(2)
    scene bg livingroom
    show shiori halloween embarrassed
    with dissolve
    shiori.say "I...I..."
    shiori.say "Would you..."
    shiori.say "Do you think that..."
    "I keep on waiting for Shiori to get to the point."
    "But every time I think she's about to come out with it, she stops short."
    "It's like she wants to ask me something, but can't find the courage."
    "Maybe she needs me to join up the dots for her."
    "So what could she actually want?"
    "She doesn't have a drink right now."
    "But then she does keep looking at the dance-floor too."
    "Which one should I go with?"
    menu:
        "Ask Shiori to dance":
            mike.say "Shiori..."
            mike.say "Do you want to dance?"
            show shiori happy
            "The question seems to have an instant effect on Shiori."
            "Her mood perks up and a smile spreads across her face."
            "She nods eagerly, grasping my hand in her own."
            $ shiori.love += 2
            shiori.say "Oh, yes, [hero.name]."
            shiori.say "I'd love to!"
            hide shiori
            show dance shiori halloween
            with fade
            "Shiori beams up at me as I lead her onto the dance-floor."
            "And she doesn't stop the whole time we're up there either."
            "Her arms are wrapped tightly around me."
            "Her head resting against my chest."
            "And the fact that she's silent no longer seems to matter."
        "Offer Shiori a drink":
            mike.say "Don't worry, Shiori."
            mike.say "I guess your throat must be dry."
            mike.say "And that's why your tongues in a twist!"
            "Shiori looks at me for a moment in silence."
            "And I think that she's about to tell me that I'm wrong."
            show shiori normal
            "But then her face cracks into a smile and she nods her head."
            shiori.say "Y...yes, that's right!"
            shiori.say "I'm so parched, [hero.name]."
            shiori.say "A drink would be wonderful!"
            "Glad to have solved the problem, I lead Shiori towards the drinks."
            "Although she keeps on casting glances at the dance-floor too."
            "But if she wanted to dance, she'd have said so, right?"
    scene bg black with dissolve
    pause 1
    return

label shiori_halloween_sex:
    scene bg livingroom
    show shiori halloween
    with fade
    "Shiori's been her usual self most of the night, shy and demure, clinging to my side."
    "And while that's pretty flattering, it doesn't make for the most exciting of times."
    "So call me a bad guy, but I might have encouraged her to partake of the punch a little."
    "Okay, okay...I encouraged her to drink a hell of a lot!"
    "But it's not like I was trying to get her drunk so that I could have my way with her."
    "All I wanted to do was get her to loosen up a little and enjoy herself."
    "And I was matching her, drink for drink, the entire time too."
    scene bg bedroom1
    show shiori halloween happy
    with fade
    "That means by the time we stagger to my bedroom, we're both pretty wasted!"
    shiori.say "Ooh..."
    shiori.say "[hero.name], why is the whole room spinning?"
    mike.say "I...I don't think it's the room, Shiori."
    mike.say "I think it's us!"
    "Shiori stumbles as she tries to walk across the room."
    "And I only just manage to catch her before she tumbles to the floor."
    "But the momentum is too great for me to be able to stop her completely."
    "This means that Shiori staggers forwards and falls onto the bed." with vpunch
    show shiori halloween close surprised
    "She lands on her back, legs in the air."
    "And I land atop her, pinning her to the mattress."
    show shiori happy
    shiori.say "Oh, there you are, [hero.name]!"
    shiori.say "I think I might have lost my balance a little!"
    show shiori normal
    "I'm almost nose to nose with Shiori right now."
    "And we seem to be having one of those rare, strange moments."
    "You know the kind I mean?"
    "The ones where you both fall silent."
    "And you're just looking into each other's eyes."
    mike.say "M...maybe I should get up?"
    show shiori surprised
    shiori.say "NO!"
    show shiori embarrassed
    shiori.say "I mean...no...please don't!"
    shiori.say "You're...well, you're rubbing my pussy, [hero.name]."
    shiori.say "And it feels really good!"
    "I'm not used to Shiori coming out with lines like that."
    "And she's not used to being able to say them either."
    "Her cheeks are already flushing red as she bites her lip."
    hide shiori
    show shiori piledriver halloween nomike
    with fade
    "Looking down, I can clearly see the outline of Shiori's pussy."
    "The material of her costume is pulled tight against it."
    "And so every detail is visible beneath a layer of red."
    show shiori piledriver pleasure
    "Without saying another word, I begin to stroke her with a finger and thumb."
    "Shiori whimpers instantly, her entire body starting to quiver."
    "She doesn't say anything either."
    "But she nods to urge me on."
    "I can feel Shiori's lips getting slicker with every second that passes."
    "And soon enough, rubbing through the material of her costume just won't do."
    show shiori piledriver normal
    "Pausing my attentions, I take hold of the crotch with both hands."
    show shiori piledriver torn
    "Then I tear the gusset out of the costume with a couple of tugs."
    shiori.say "Oh, [hero.name]!"
    shiori.say "Please don't stop!"
    "Shiori looks up at me with wide eyes full of desire."
    "I can see the way her pussy is glistening in the light."
    "And I can smell the scent of it too!"
    "Just touching it with my fingers isn't going to be enough."
    "My cock's more than ready to take things to the next level."
    show shiori piledriver -nomike
    "So I waste no more time in pushing the tip against Shiori's lips."
    "She nods desperately, urging me on."
    show shiori piledriver
    "And a moment later I know she wasn't lying when she said she was ready."
    "I don't have to put more than a little effort into getting inside of her."
    show shiori piledriver inside pleasure
    "Shiori's pussy surrenders to me without putting up a shred of resistance."
    "And a second afterwards, I start to thrust my cock in and out of her."
    "I push down on Shiori with all my weight, driving her into the mattress."
    "But she takes all that I have to give without a murmur of complaint."
    "In fact, her curvy little body eats it up as quickly as I can give it to her!"
    "I don't know which one of us has more passion built up inside of us right now."
    "I've been waiting to do this all night."
    "Turned on by Shiori's body under that costume."
    "But I feel like I've tapped that well of repressed desire in Shiori."
    "The one that she buries under her duties as a working mother and single parent."
    "There's so much pent up emotion in her that I worry I can't satisfy her!"
    "And for now she'll have to make do with what I have to give."
    "Because I can feel myself cumming right now!"
    "Shiori seems to sense it too."
    show shiori piledriver ahegao with hpunch
    "And she clings to me tightly as I lose control."
    show shiori piledriver cumshot with hpunch
    "This means that I shoot my load into her when I'm as deep as I can go."
    with hpunch
    "Shiori keeps a hold of me to the very end, like she's afraid to release me."
    "Then we collapse onto the mattress together, a mess of tangled limbs."
    $ shiori.sexperience += 1
    $ game.pass_time(1)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
