label bree_date_intro_valentine_male:
    mike.say "Happy Valentine's day, [bree.name]!"
    bree.say "And a happy Valentine's day to you too, [hero.name]!"
    "[bree.name]'s smile is infectious, making me crack one too."
    "She seems to notice this, adding a giggle into the mix."
    bree.say "Okay, valentine..."
    bree.say "Shall we get started on our date?"
    mike.say "Y..yeah, of course, [bree.name]."
    mike.say "I can't wait!"
    return

label bree_date_intro_halloween_male:
    mike.say "Whoa, [bree.name] - you look amazing tonight!"
    "[bree.name] smiles at my compliment, even blushes a little."
    bree.say "Thanks, [hero.name] - you scrub up pretty nice too!"
    bree.say "Where are we going tonight?"
    mike.say "Oh, I figured anywhere would be good, as it's Halloween."
    "[bree.name] rolls her eyes and lets out a groan."
    bree.say "Oh man, I totally forgot!"
    bree.say "We should have dressed up or something, made an effort."
    mike.say "Yeah, that would have been fun - maybe next year?"
    return

label bree_date_intro_christmas_male:
    mike.say "Are you ready for our date, [bree.name]?"
    mike.say "You'd better wrap up warm too, because it's cold outside!"
    "[bree.name] nods and smiles as she hurries to grab her things."
    bree.say "No worries, [hero.name]."
    bree.say "And I'm feeling pretty festive too!"
    bree.say "I guess I'm ready for it to be that special time of year again!"
    return

label bree_date_intro_birthday_male:
    mike.say "Happy birthday, [bree.name]!"
    mike.say "And don't worry about our date."
    mike.say "I have it all planned out, and it's going to be awesome."
    bree.say "Thanks, [hero.name]..."
    bree.say "So, what are we waiting for?"
    bree.say "I can't wait to see what you've got planned!"
    return

label bree_date_intro_mc_birthday_male:
    bree.say "Happy birthday, [hero.name]!"
    bree.say "Come on - let's go out and celebrate already!"
    mike.say "Whoa...wait for me, [bree.name]!"
    mike.say "And you remembered my birthday too?"
    bree.say "Oh please - we live in the same house, remember?"
    bree.say "I must have seen mail with your details on it a hundred times."
    bree.say "Plus you wrote it on every calendar in the house - in big red letters too!"
    return

label bree_date_pub_male:
    show bree
    bree.say "I like the Winchester, it's nice and cozy."
    hide bree
    return

label bree_date_cinema_male:
    show bree
    bree.say "You know, I am not a big fan a sitting next to each other and not talking at all."
    hide bree
    return

label bree_date_familyrestaurant_male:
    show bree
    bree.say "Simple food is the best."
    hide bree
    return

label bree_date_restaurant_male:
    show bree
    bree.say "I appreciate the effort but this kind of restaurant is not really my cup of tea."
    hide bree
    return

label bree_date_amusmentpark_male:
    show bree
    bree.say "I just love this park, I came here a lot when I was a child."
    hide bree
    return

label bree_date_ride_the_ferris_wheel:
    show bree
    bree.say "Yes, I love the ferris wheel, it's so romantic!"
    $ bree.love += 1
    hide bree
    return

label bree_date_waterpark_male:
    show bree
    bree.say "This will be pure fun!"
    hide bree
    return

label bree_date_park_male:
    show bree
    bree.say "It's nice to have this park so close to the house."
    hide bree
    return

label bree_date_eat_a_burger:
    "[bree.name] eats most of her burger, leaving only a couple of bites in the wrapper."
    "But all the same, she doesn't seem to be blown away by it."
    "Maybe she was just eating it to line her stomach for the sake of the booze?"
    return

label bree_date_buy_drink:
    if bree.is_visibly_pregnant:
        show bree angry
        $ bree.love -= 10
        bree.say "Are you serious?!?"
        bree.say "I can't drink when I'm pregnant!"
        bree.say "What are you thinking?!?"
        $ hero.cancel_activity()
        hide bree
    else:
        "When I put the drink she ordered into her hand, [bree.name] looks almost surprised."
        "She thanks me and takes a couple of sips before putting it down."
        "And even then I get the feeling she was doing it to be polite."
    return

label bree_date_play_darts:
    "[bree.name] nods with enthusiasm at the prospect of a game of darts."
    "And as soon as she's stood at the oche, she looks super serious too!"
    "Have I gone and gotten into a game with a secret hustler?!?"
    return

label bree_date_pub_play_pool:
    "Cue in hand, [bree.name] proceeds to make me fight for my life at the pool-table."
    "Seriously, where did the girl learn to sink balls like that?!?"
    "And she makes it look like such a breeze too!"
    return

label bree_date_buy_a_round:
    if bree.is_visibly_pregnant:
        show bree angry
        $ bree.love -= 10
        bree.say "Are you serious?!?"
        bree.say "I can't drink when I'm pregnant!"
        bree.say "What are you thinking?!?"
        $ hero.cancel_activity()
    elif (hero.charm >= 60 - bree.love and bree.flags.drinks < 2):
        show drink bree
        "When I offer to stand a round, [bree.name] just nods happily."
        "I know I'm supposed to be a modern guy and all that."
        "But sometimes it's nice to feel appreciated for the small gestures!"
        $ game.active_date.score += 5
        if "rebel" in bree.traits:
            $ game.active_date.score += 5
        $ bree.set_flag("drinks", 1, "day", mod="+")
        hide drink
    else:
        "I want to pay a round of beers to the whole pub."
        "But [bree.name] doesn't seem to want to drink, so I refrain from doing so."
        $ hero.cancel_activity()
    return

label bree_dance_with:
    "Although she seems to be having a good time on the dance-floor, [bree.name]'s reluctant to meet my eye the whole time we're up there."
    "I can't figure out if she's embarrassed to be there or to let her true emotions show."
    "And so I try to ignore the matter and simply enjoy the chance to be this close to her instead."
    return

label bree_date_play_arcade_intro_male:
    bree.say "Why did we never do this before, [hero.name]?"
    bree.say "This is the BEST arcade in town!"
    bree.say "I've never seen so many retro games in one place!"
    "I'm usually the one trying to drag a girl into the arcade."
    "But right now [bree.name] has me by the hand and is yanking me along."
    "And she's giving me a run for my money in the geekdom stakes too!"
    mike.say "Whoa..."
    mike.say "Slow down, [bree.name]!"
    mike.say "We've got plenty of time to take it all in."
    "[bree.name] looks at me like I'm speaking nonsense."
    "And she shakes her head in disbelief."
    bree.say "Wow!"
    bree.say "What's the matter with you, [hero.name]?"
    bree.say "We have the run of this place and there's nobody to stop us!"
    bree.say "Come on - let's binge on some retro classics!"
    "And that's how I find myself standing in front of an arcade cabinet."
    "'Hyper Plumber Siblings' to be exact - the quintessential retro classic."
    "[bree.name] doesn't even wait for me to offer an opinion."
    "She's already stuffing coins into the slot as if her life depends on it!"
    "Well, I guess the lives of her character in the game kind of does!"
    bree.say "You ready, [hero.name]?"
    bree.say "You're Maria, and I'm Luciana."
    bree.say "Here we go..."
    return

label bree_date_play_arcade_win_male:
    "I don't think I've ever been pushed like this before."
    "But then [bree.name]'s probably the most hardcore gamer I know!"
    "She's almost as good as me - but not quite."
    bree.say "That mushroom's mine!"
    bree.say "HEY!"
    bree.say "I needed that, [hero.name]!"
    mike.say "Sorry, [bree.name]."
    mike.say "You snooze, you lose!"
    "We're neck and neck almost the whole time."
    "One moment [bree.name] pulls ahead of me."
    "And the next I find a way to turn the tables on her."
    "I can hear the sound of us both hammering buttons."
    "But I can also hear [bree.name] muttering and cursing too."
    "She must be bouncing up and down on the spot right now!"
    "I want to sneak a look at her, you know?"
    "Check out her curves as they go up and down."
    "But instead I focus on the game and play to win."
    "Once it's all over and we're out of coins, the scores are in."
    "And I'm the clear winner!"
    mike.say "YES!"
    mike.say "I'm the champion!"
    "[bree.name] shakes her head and snorts in frustration."
    "But she still makes an effort to be a good loser."
    bree.say "You win, [hero.name]."
    bree.say "But I'll get you next time!"
    return

label bree_date_play_arcade_lose_male:
    "I don't think I've ever been pushed like this before."
    "But then [bree.name]'s probably the most hardcore gamer I know!"
    "I mean, I'm good - but she's better."
    mike.say "That mushroom's mine!"
    mike.say "HEY!"
    mike.say "I needed that, [bree.name]!"
    bree.say "Aw...sorry, [hero.name]!"
    bree.say "You snooze, you lose!"
    "I'm fighting to even keep up the whole time we're playing."
    "But then [bree.name] starts to pull ahead of me."
    "And there's nothing I can do to catch her."
    "I can hear the sound of us both hammering buttons."
    "But I can also hear [bree.name] breathing heavily too."
    "She must be bouncing up and down on the spot right now!"
    "I want to sneak a look at her, you know?"
    "Check out her curves as they go up and down."
    "And when I do, it's better than any videogame!"
    "[bree.name]'s ass is shaking behind her."
    "And her breasts are swaying under her shirt."
    "Just the sight of it makes me start to get hard!"
    "Before I know it, the game is over."
    "And of course, [bree.name]'s the clear winner."
    bree.say "YES!"
    bree.say "I'm the champion!"
    "I give [bree.name] a smile, trying to be a good loser."
    mike.say "You win, [bree.name]."
    mike.say "But I'll get you next time!"
    "But I still have that image of her bouncing up and down in my head."
    "And that's far more of a prize to me than beating her at a videogame!"
    return

label bree_pet_activity_male:
    show bree close pat
    "I pet [bree.name]'s gorgeous blonde hair."
    $ bree.sub += 1
    $ bree.love += 1
    if bree.flags.mikeNickname:
        bree.say "Thank you [hero.name]."
    else:
        bree.say "It feels so nice..."
    hide bree
    return

label bree_dick_reactions:
    if not bree.flags.seendick:
        $ bree.flags.seendick = 1
        if hero.has_skill("hung"):
            show dick reactions bree scared
            bree.say "O...M...G!"
            bree.say "We've been living together so long, [hero.name]."
            bree.say "How did you manage to keep this thing hidden?!?"
            mike.say "Well...I could show you where I like to hide it?"
            show dick reactions bree tasty
            bree.say "Oooh...that sounds like fun!"
            $ bree.sub += 10
        elif hero.has_skill("smalldick"):
            show dick reactions bree smile
            bree.say "Oh..."
            show dick reactions bree mock
            bree.say "Oh well - you can't win them all!"
            mike.say "Is there a problem, [bree.name]?"
            bree.say "Well...let's just say it's a good thing I like your personality!"
            $ bree.sub -= 10
        hide dick reactions
    return

label bree_peeping_scene_male:
    "Normally it's just a part of the daily grind to discover that the bathroom's occupied."
    "I mean, at worst it means that I'll have to hold it in a little longer, which is no big deal."
    "But on this occasion it's not a locked door that lets me know I'm going to have to wait."
    "Rather it's the sound of running water from around the half-open door I'm presented with."
    "Well, I say the door's half-open - it's really more ajar."
    "But whatever term best describes it, I can at least take a peek around it."
    "And no, that doesn't make me a pervert!"
    "For all I know, one of the girls could have left the shower running."
    "She could be coming back when it gets hot enough for her to actually bathe."
    "In that case I can nip in, do my business and be gone before she's back."
    "No, what makes me feel like a bit of a perv is what I see when I peek round the door."
    "I was wrong, they're already in the shower and well into bathing too!"
    "At first I can't tell just who is in the shower cubicle."
    "But then the girl inside throws back her head and I see a flurry of blonde hair."
    "And that can only mean it's [bree.name]!"
    "Instantly the better part of me knows that I should back off."
    "Yet I can't seem to make myself do it."
    "Instead I remain rooted to the spot, watching [bree.name]'s every move."
    "I can't see everything thanks to the steam and the glass."
    "But just the outline of her body is more than enough to hold me entranced."
    return

label bree_peeping_reactions_male:
    if (bree.love >= 150 or bree.sub >= 50) and bree.sexperience:
        show bree naked stuned
        "So much so that I don't even notice the fact that I've been spotted!"
        show bree talkative
        bree.say "Hey - who's out there?"
        bree.say "Is that you, [hero.name]?"
        show bree happy blush
        bree.say "That's so naughty of you - watching me in the shower!"
        show bree normal
        "I hold my breath, waiting for the inevitable tirade of abuse."
        "But instead I watch as [bree.name] covers her hands in shower gel."
        "She works up a lather of bubbles, making sure that I see this."
        show bree smile
        bree.say "All I'm doing is getting myself all nice and clean!"
        bree.say "Why would you want to spy on me doing that?"
        show bree normal
        "And then she begins to rub the lather of bubbles all over herself."
        "If this is really how [bree.name] gets clean in the shower..."
        "Well, then maybe my fantasies about other things are true too!"
        "She soaps herself everywhere - and I mean everywhere."
        "But I guess the parts she lingers on must be the dirtiest of all."
        "And that's because [bree.name] takes so much time over them."
        "All of those curves, I guess they just attract dirt."
        "Her breasts, belly, buttocks and thighs."
        "I'm entranced as she not only traces them with the bubbles."
        "But impressed as she goes back over them time and again."
        "And when she's done, all I can do is stare in amazement."
        "Honestly, I've never gotten so hard over personal hygiene before!"
        show bree close smile
        $ bree.love += 1
        $ bree.sub += 1
        bree.say "There you go, [hero.name]."
        bree.say "I'm all squeaky clean!"
        show bree happy
        "[bree.name] giggles, knowing what she must be doing to me."
        show bree smile
        bree.say "And don't worry."
        bree.say "You can have the shower after me."
        bree.say "If you want to get cleaned up too!"
    else:
        show bree naked stuned
        "So much so that I don't even notice the fact that I've been spotted!"
        show bree surprised
        bree.say "HEY!"
        bree.say "WHO IS THAT?!?"
        bree.say "I know there's somebody out there!"
        show bree angry
        "I stand up and try to back away as quietly as I can."
        "But [bree.name]'s just too fast for me to make my escape."
        "Wrapped in a towel and fuming with rage, she bursts out of the bathroom."
        $ bree.love -= 20
        $ bree.sub -= 10
        show bree vangry
        show fx anger
        bree.say "So there WAS someone there!"
        bree.say "[hero.name], you dirty little pervert!"
        bree.say "I knew it had to be you!"
        show bree close angry
        mike.say "Whoa...back up a little, [bree.name]!"
        mike.say "I was just checking to see if the bathroom was free."
        mike.say "Honestly, that's all I was doing!"
        "[bree.name] narrows her eyes at me."
        "And then she pokes a finger in my face."
        show bree vangry
        bree.say "Then try knocking next time, okay?!?"
        show bree angry
        play sound door_slam
        pause 0.4
        scene bg door bathroom at center, zoomAt(1.25, (640, 880))
        with hpunch
        "And with that, she turns on her heel and slams the door in my face."
    return

label bree_halloween_invitation:
    show bree
    "I know it might sound weird, because we're all kind of hosting the party together."
    "But part of me still wants to have [bree.name] there as my date, and for me to be hers too."
    "I guess that I'm just a little too possessive of her to be casual about it."
    "It's not like I want her to follow me around all night and never leave my side."
    "And I'm not going to get all jealous and sulky if she happens to talk to other guys either."
    "I just feel that I need to know we're there as a couple, and not on our own."
    "So I wait until Sasha's well out of earshot."
    "And then I try to explain myself to [bree.name]."
    mike.say "[bree.name]..."
    mike.say "About the Halloween party..."
    bree.say "Yeah, [hero.name]?"
    bree.say "What about it?"
    show bree happy
    bree.say "It's going to be great - I just know it!"
    mike.say "I think so too, [bree.name]."
    mike.say "But I just wanted to ask - we're going together, right?"
    show bree normal
    "[bree.name] looks at me oddly."
    "It's clear that she's a little thrown by the question."
    bree.say "But, [hero.name]..."
    bree.say "We can't go to the party if we're throwing it!"
    mike.say "Yeah, [bree.name], I know that."
    mike.say "What I mean is we can be there as a couple, officially."
    mike.say "Like if anyone asks or we need to dance, you know?"
    show bree dazed
    "[bree.name] looks at me strangely for a moment."
    "She has her head cocked on one side."
    "And I can tell she's weighing up what I just said."
    if bree.love >= 100 or bree.is_sex_slave or Harem.together(bree, sasha, name='home'):
        show bree normal
        bree.say "Oh, I get it!"
        "[bree.name] nods and smiles."
        bree.say "You mean it can be our little secret - right?"
        bree.say "You, me and Sasha will be the hosts."
        show bree wink
        bree.say "But if anyone asks - we're spoken for!"
        "I'm nodding too by now."
        "At last - she gets it!"
        mike.say "That's it, [bree.name]."
        mike.say "Sorry if it sounds all possessive and weird!"
        show bree happy
        bree.say "No, [hero.name], don't be silly!"
        $ bree.love += 1
        show bree normal
        bree.say "Actually, it's kind of romantic."
        bree.say "Like there's going to be all this fun happening."
        bree.say "But the only girl you want there is me!"
        show bree flirt blush
        "Suddenly, [bree.name] stops and looks at me sideways."
        "Then she lets out a mischievous chuckle."
        bree.say "Well, you'll want me like crazy anyway."
        bree.say "Just as soon as you see my costume!"
        mike.say "Why, [bree.name]?"
        mike.say "What are you coming as?"
        bree.say "Uh-uh - be patient, [hero.name]."
        bree.say "Don't spoil the surprise!"
        $ game.flags.halloween_girl = "bree"
    else:
        bree.say "You know what, [hero.name] - I'd rather we didn't."
        bree.say "It's hard enough organising the party as it is."
        bree.say "We have to decide who to invite, decorate the house too."
        "[bree.name] pauses to take a deep breath."
        "Then she lets it out again as a sigh."
        bree.say "And then when the guests get here, there's more work."
        bree.say "All three of us are going to have to be good hosts."
        bree.say "I don't think I can handle being your date too."
        bree.say "I'm sorry!"
        "I nod, trying to hide the fact that I'm disappointed."
        "[bree.name]'s right, we do have to work hard to make this a success."
        mike.say "Ah, yeah, [bree.name]."
        mike.say "When you put it like that..."
        show bree normal -blush
        "[bree.name] gives me a consoling smile."
        "Though it doesn't seem to help my feelings all that much."
        bree.say "Thanks for understanding, [hero.name]."
        bree.say "I'm sure the party will be great."
        bree.say "And we'll both be so busy on the night..."
        bree.say "So busy you'll forget all about this!"
        mike.say "Sure, [bree.name]."
        mike.say "That sounds great..."
    return

label bree_halloween_arrival:
    scene bg house
    "I stare at the door for a moment longer, and then I strike myself on the forehead."
    "Of course, [bree.name] lives here too."
    "So my date's already in the house!"
    "Geez, I must have scrambled my brain putting so much effort into the party."
    scene bg livingroom
    show bree halloween
    "But the same can't be said for [bree.name], as she looks at me expectantly."
    bree.say "Well, [hero.name], I'm waiting."
    bree.say "What do you think of my costume?"
    "I look [bree.name] up and down one last time."
    "And then I take a deep breath."
    "All in preparation to tell her exactly what I think."
    menu:
        "Compliment":
            mike.say "Wow, [bree.name]..."
            mike.say "I didn't want to say in front of the others."
            mike.say "But you look SO hot in that costume!"
            show bree flirt blush
            $ bree.love += 1
            "[bree.name] smiles and lets out a giggle."
            "I can see that was the answer she wanted to hear."
            bree.say "Aw, thanks, [hero.name]."
            bree.say "I was thinking of you when I picked it."
            mike.say "You were?"
            bree.say "Yeah, [hero.name]."
            bree.say "I've seen the way you look at Sindee when you play the game."
            bree.say "And I was getting kind of jealous for a while there!"
            "I feel my cheeks flush a little at [bree.name]'s admission."
            "Am I really that transparent, that easy to read?"
            mike.say "I...I didn't mean to..."
            bree.say "It's okay, [hero.name] - you're only human."
            bree.say "And this way, we both get to enjoy my costume!"
        "Criticize":
            mike.say "Ah..."
            mike.say "That's a really nice costume, [bree.name]."
            mike.say "Looks like it took you an age to put together too."
            "A pained smile appears on [bree.name]'s face as she listens to me."
            bree.say "But?"
            mike.say "But what, [bree.name]?"
            bree.say "There's a but hanging in the air, [hero.name]."
            bree.say "Like you want to say something about my costume."
            bree.say "But you're scared to come out with it."
            "Suddenly I feel like I've been put on the spot."
            "I look around, but there's no means of escape."
            mike.say "Well..."
            mike.say "It's just I never saw you as Sindee."
            mike.say "I always saw you more as Aranea."
            show bree annoyed
            $ bree.love -= 4
            bree.say "Urgh..."
            bree.say "Really, [hero.name]?"
            bree.say "Ah...let's just forget it, okay?"
            mike.say "Okay, [bree.name] - if you say so."
            "I try to let it go and turn my mind to the party."
            "But I can't help feeling like I just screwed up."
    scene bg black with dissolve
    pause 1
    return

label bree_halloween_party:
    $ game.pass_time(2)
    scene bg livingroom
    show bree halloween dazed at left
    show jack halloween normal at right
    with dissolve
    bree.say "Ah...yeah, Jack."
    bree.say "That's really fascinating!"
    bree.say "You know so much about D&D!"
    jack.say "You really think so, [bree.name]?"
    jack.say "Then you'll freak when you hear this!"
    "I turn around to see that Jack has [bree.name] cornered."
    "He's in full-on geek mode, talking constantly."
    "And from the look on [bree.name]'s face, she needs rescuing!"
    "I lean in closer, inserting myself into the conversation."
    menu:
        "Save [bree.name]":
            mike.say "Urgh..."
            mike.say "Come on, Jack!"
            mike.say "We're all nerds here."
            mike.say "But there's a time and a place, yeah?"
            show bree normal
            "Jack looks suddenly bashful."
            "And he finally stops talking."
            bree.say "He's right, Jack."
            bree.say "We can chat about D&D anytime."
            bree.say "You should really try to mingle a little."
            jack.say "Erm...okay..."
            jack.say "I'll give it a try."
            hide jack
            hide bree
            show bree halloween normal
            "With that, Jack wanders off to bother someone else."
            bree.say "Ah..."
            show bree happy
            $ bree.love += 2
            bree.say "Thanks, [hero.name]."
            bree.say "You saved me from a slow death via boredom!"
        "Back up Jack":
            mike.say "I'm going to have to stop you there, Jack!"
            show bree normal
            "At the sound of my voice, both [bree.name] and Jack look around."
            "Jack looks confused, but [bree.name] seems to think she's been saved."
            mike.say "Because you've left out an important point."
            mike.say "That rule WAS included in second edition!"
            show bree annoyed
            $ bree.love -= 2
            "Jack looks instantly intrigued."
            "But [bree.name]'s face falls."
            bree.say "Oh great - more D&D talk!"
            "Jack listens with great interest as I go on."
            "And [bree.name] has no choice but to stand there and endure it."
    scene bg black with dissolve
    pause 1
    return

label bree_halloween_dance:
    $ game.pass_time(2)
    scene bg livingroom
    show bree halloween
    with dissolve
    bree.say "Aw, come on, [hero.name]."
    bree.say "I want to dance!"
    bree.say "What are we waiting for?"
    "[bree.name]'s been pestering me to dance for what feel like forever."
    "But every song that comes on just doesn't do it for me tonight."
    "And I must have asked her to wait for the next one a dozen times by now!"
    "Pretty soon I'm going to have to give up or just take whatever comes."
    "Because [bree.name]'s not going to wait all night."
    menu:
        "Accept":
            mike.say "You know what, [bree.name] - you're right."
            mike.say "This is a party."
            mike.say "And we're supposed to be having fun!"
            show bree happy
            $ bree.love += 2
            "[bree.name] giggles with delight as I lead her onto the dance-floor."
            hide bree
            show dance bree halloween
            "And as soon as we start dancing, the music doesn't seem to matter."
            "All that does is the fact we're together and having a good time."
            "I'm cool with keeping things light and fun."
            "But I soon get the impression [bree.name] has other things in mind."
            "She dances as close to me as she can."
            "And she seems to be pressed close against me the whole time."
            "I'm not complaining about this, not at all."
            "In fact, I can already feel myself stiffening in a certain area!"
            "[bree.name] seems to notice this too."
            "She giggles again as she rubs my crotch with her hand."
            bree.say "Hey, [hero.name]!"
            bree.say "I'm the one that's supposed to be a mechanic."
            bree.say "So how come you're the one with the massive tool?"
        "Refuse":
            mike.say "Nah, [bree.name]."
            mike.say "I have to have the right song."
            mike.say "So I'm going to pass."
            show bree annoyed
            $ bree.love -= 1
            "[bree.name] frowns and shakes her head at me."
            bree.say "You're no fun!"
            bree.say "So forget you!"
            hide bree
            "With that, [bree.name] walks away from me."
            "I watch as she storms onto the dance-floor alone."
            "But it doesn't take long for her to attract company."
            "Jack and Scottie are right there, dancing for all they're worth."
            "All I can do is watch as [bree.name] laughs and flirts with them."
            "And all the time she's making sure that I can see it too!"
    scene bg black with dissolve
    pause 1
    return

label bree_halloween_sex:
    scene bg secondfloor
    show bree halloween
    with dissolve
    "It's getting pretty late by now and the party's starting to wind down."
    "Everyone's either tired, drunk or both and wanting to chill out."
    "And I know that I'm feeling the same way after playing host all night."
    "[bree.name] looks like she's exhausted too, but her eyes are still bright."
    bree.say "I think we did pretty well tonight, [hero.name]."
    bree.say "We turned out to be good hosts after all!"
    mike.say "Yeah, [bree.name]."
    mike.say "Everyone seemed to have a good time."
    show bree happy
    "[bree.name] nods, smiling happily."
    bree.say "In fact, I think we did so well we deserve a reward."
    show bree flirt blush
    bree.say "Maybe a little celebration for just the two of us?"
    "It's only now that I realise we're standing outside [bree.name]'s bedroom door."
    "She leans against it and gives me a suggesting wink."
    mike.say "Sounds good to me, [bree.name]."
    mike.say "We worked our asses of tonight."
    mike.say "But...are you thinking what I think you're thinking?"
    "By way of answer, [bree.name] takes me by the hand."
    scene bg bedroom2
    show bree halloween flirt blush
    with fade
    "And with the other, she opens the door to her room."
    "There's nothing more that either of us needs to say."








    "[bree.name] doesn't make any demands of me."
    "And all I want right now is her."
    "And so we come together simply and almost on instinct."
    show bree cowgirl halloween with fade
    "I lie down on the bed and [bree.name] climbs atop me."
    show bree cowgirl out
    "I can feel the fatigue melt away as my cock gets hard."
    "It's still there in the background."
    "But I know that I have enough energy in reserve for this."
    "Enough to make sure that this is a memorable end to the night."
    "[bree.name] nods, encouraging me without the need for words."
    "The head of my cock brushes against the lips of her pussy."
    show bree cowgirl blush
    "And she closes her eyes, moaning with the anticipation of pleasure."
    show bree cowgirl pleasure vaginal
    "I go slowly, coaxing my way inside of her rather than teasing."
    show bree cowgirl smile
    "And [bree.name] nods all the more, urging me on."
    "She opens slowly but surely, like a flower parting its petals."
    "I sink into her with the same slow progress until I can go no further."
    "It's like I can feel the fatigue in [bree.name]'s body."
    "I can sense the way that it's being burnt away."
    "My movements are still slow and deliberate."
    show bree cowgirl pleasure
    "But I can already feel that [bree.name] wants more from me."
    "It's not enough to simply end the night with a lazy fuck."
    "She wants to use up every last ounce of her strength."
    "That and then to fall asleep satisfied and sated."
    "My speed is picking up now, adrenaline masking my exhaustion."
    "I can feel the sweat running down the length of my spine."
    "But still I keep on pushing myself harder."
    show bree cowgirl up
    "[bree.name] begins to moan atop me, a deep and helpless sound."
    "I'm panting, struggling to fill my lungs with each breath."
    "And yet I keep on going, by now pounding away at [bree.name]."
    "She writhes and wriggles above me, mewling softly."
    "My guess is that she doesn't have the energy to do anything more."
    "And finally I can feel the night catching up with me."
    "I know that I've used up the very last of my strength."
    "So there's nothing I can do to hold on when the end comes."
    show bree cowgirl creampie ahegao with vpunch
    "My body stiffens as I shoot my load into [bree.name]."
    with vpunch
    "And she quivers, taking it all without hesitation."
    show bree cowgirl resting dickcum cum onpussy
    show pussy_insert bree zorder 1 at zoomAt(0.75, (820, 200))
    with vpunch
    "With that, I feel my muscles turn to water."
    "[bree.name] collapses atop me, almost unable to move."
    show bree cowgirl down
    "And she clings onto me, riding out the last moments of her orgasm."
    "Her face is the last thing I see before my eyes close."
    "Then I'm asleep and probably snoring too!"
    hide pussy_insert
    $ bree.sexperience += 1
    $ game.pass_time(1)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
