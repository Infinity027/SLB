label kleio_date_intro_valentine_male:
    mike.say "Happy Valentine's day, Kleio."
    mike.say "I can't think of anyone I'd rather have as my valentine today."
    "Kleio bursts out laughing at this."
    kleio.say "You sure about that, Loverboy?"
    kleio.say "Because with me, Valentine's day can be a little spicy!"
    mike.say "Of course I'm sure, Kleio."
    mike.say "You know I love it when you're spicy!"
    kleio.say "Aw, you're such a dope, Loverboy!"
    kleio.say "But I love you all the same!"
    return

label kleio_date_intro_halloween_male:
    mike.say "Hey, Kleio, I forgot it was Halloween tonight."
    mike.say "We should have got all dressed up, you know?"
    "Kleio chuckles and shakes her head at this."
    kleio.say "So you want me to put on a cute little costume and parade around for you?"
    kleio.say "Is that what you're trying to say, Loverboy?"
    "I can feel myself starting to blush a little as Kleio puts me on the spot."
    mike.say "No...I mean yeah...I mean, only if you wanted to, Kleio!"
    "Kleio laughs again, clearly enjoying the way this is going."
    kleio.say "Yeah, we could do that - or you could parade around for me instead!"
    return

label kleio_date_intro_christmas_male:
    kleio.say "Hey, Loverboy - you full of festive cheer and all that crap?"
    "I can't help smiling at Kleio's acid tongue, that and the twinkle in her eye."
    mike.say "What if I am, little Miss Grinch?"
    mike.say "What are you gonna do, suck it out of me?"
    "Kleio lets out a filthy laugh, liking the fact I'm giving as good as I'm getting."
    kleio.say "You just wait until we're under the mistletoe, Loverboy."
    kleio.say "Because I'm going to be sucking the fucking life out of you!"
    return

label kleio_date_intro_birthday_male:
    mike.say "Happy birthday, Kleio!"
    kleio.say "Aah..."
    kleio.say "What's so happy about it, Loverboy?"
    kleio.say "All it means is that I'm a year older!"
    mike.say "Erm...yeah, Kleio...I kinda see your point..."
    mike.say "But if nothing else, it's an excuse to have a good time, right?"
    kleio.say "Now you're speaking my language!"
    return

label kleio_date_intro_mc_birthday_male:
    kleio.say "Happy birthday, Loverboy!"
    kleio.say "So, are we gonna tear it up tonight, huh?"
    kleio.say "Really celebrate your big day?"
    mike.say "Y...yeah, Kleio!"
    mike.say "That sounds totally amazing!"
    mike.say "What were you thinking of?"
    kleio.say "Oh, just you wait and see!"
    kleio.say "You're gonna love it, I promise."
    return

label kleio_date_eat_a_burger:
    "Kleio seems to be waiting with baited breath for her burger to arrive."
    "And when it does she reclines and eats it slowly, savouring every bite."
    "Somehow, I'm savouring it too - and I'm only watching her!"
    return

label kleio_date_buy_drink:
    if kleio.is_visibly_pregnant:
        show kleio angry
        $ kleio.love -= 10
        kleio.say "You already knocked me up, you jerk!"
        kleio.say "Now you're trying to screw the baby up too?!?"
        $ hero.cancel_activity()
        hide kleio
    else:
        "Kleio takes a healthy swig from her glass, hardly pausing for a second as she does so."
        "I swear that the amount she just swallowed would have made a man twice her size proud of the effort."
        "But she just wipes her mouth on the back of her hand and smiles."
    return

label kleio_date_play_darts:
    "Nothing seems awry as Kleio steps up to the oche with her darts in hand."
    "But then she proceeds to cover her eyes with one hand and toss them in random directions with the other."
    "In the chaos that follows, I honestly don't know whether to be terrified or amused!"
    return

label kleio_date_pub_play_pool:
    "Kleio has all the swagger of a seasoned hustler as we start to play a game of pool."
    "That is until she hops onto the edge of the table and takes her shots backwards."
    "She sticks her tongue out at me the whole time, as if daring me to be mad with her."
    return

label kleio_date_buy_a_round:
    if kleio.is_visibly_pregnant:
        show kleio angry
        $ kleio.love -= 10
        kleio.say "You already knocked me up, you jerk!"
        kleio.say "Now you're trying to screw the baby up too?!?"
        $ hero.cancel_activity()
    elif (hero.charm >= 60 - kleio.love and kleio.flags.drinks < 2):
        show drink kleio
        "As soon as I mention that I'm headed to the bar, Kleio gives me a resounding cheer."
        "But then she finds out that I'm planning on buying a round, rather than just one for me."
        "And she positively howls with enthusiasm."
        $ game.active_date.score += 5
        if "rebel" in kleio.traits:
            $ game.active_date.score += 5
        $ kleio.set_flag("drinks", 1, "day", mod="+")
        hide drink
    else:
        "I want to pay a round of beers to the whole pub."
        "But Kleio doesn't seem to want to drink, so I refrain from doing so."
        $ hero.cancel_activity()
    return

label kleio_dance_with:
    "Almost the instant that we're on the dance-floor, Kleio turns around and leans into me."
    "She grabs both of my hands and practically forces me to caress her body as she does so."
    "I swallow nervously, feeling the sensation of her as she rubs her tight little body against me."
    return

label kleio_date_play_arcade_intro_male:
    kleio.say "This place smells pretty funky, Loverboy!"
    kleio.say "You really like to come and hang out here?"
    "I turn my head just in time to see the smile on Kleio's face."
    "It's ironic and amused, like she's looking down on me."
    mike.say "Try to be nice, Kleio."
    mike.say "I don't piss on stuff we do that YOU like!"
    kleio.say "Of course you don't."
    kleio.say "Because all the stuff I make us do isn't lame!"
    "Part of me is beginning to think this was a bad idea."
    "That I shouldn't have invited Kleio along to the arcade."
    "But another part of me is wanting to stand up to her."
    "The part of me that actually enjoys our verbal sparring sessions."
    "Plus it'd be a feather in my cap to prove her wrong."
    mike.say "This isn't lame, Kleio."
    mike.say "We're surrounded by classic games."
    mike.say "There's something for everyone."
    mike.say "You just need to give it a chance!"
    "Kleio snorts and rolls her eyes at this."
    "But my gaze has already settled on a potential candidate."
    mike.say "You're a petrol-head, right, Kleio?"
    mike.say "So how about 'First Place'?"
    mike.say "That's a real classic racing game!"
    "Kleio frowns at this, but she nods all the same."
    "And I leap on the chance, pumping coins into the slot."
    return

label kleio_date_play_arcade_win_male:
    "I have no doubt Kleio knows cars better than I do."
    "And she's probably a better driver than me too."
    "But that just doesn't translate into the game."
    kleio.say "Urgh..."
    kleio.say "This thing handles like shit!"
    kleio.say "My car looks like a million dollars."
    kleio.say "But it drives like a piece of crap!"
    mike.say "Ah...you're falling way back there, Kleio."
    mike.say "And the idea is to AVOID crashing, yeah?"
    "Kleio grunts and swears her way through the game."
    "And by the time we're done, she looks pretty frazzled."
    "Her breathing is heavy, her eyes wide."
    "And I swear she's worn holes in the buttons on the console!"
    kleio.say "There you go, Loverboy."
    kleio.say "You won, so yippee for you!"
    kleio.say "Can we actually go now?!?"
    mike.say "Okay, Kleio..."
    mike.say "Let's go do something else."
    mike.say "Maybe something that'll help lower your blood pressure?"
    return

label kleio_date_play_arcade_lose_male:
    "Kleio's definitely more knowledgeable than me when it comes to cars."
    "And she's pretty mean behind the wheel of one too."
    "So maybe it shouldn't be a surprise that she takes to this game."
    "Almost from the start I'm left eating her proverbial dust."
    kleio.say "Whoo-hoo!"
    kleio.say "Smell you later, Loverboy!"
    kleio.say "I am burning some serious rubber here!"
    mike.say "Hey...I...I can't seem to..."
    mike.say "My car - what's the matter with it?!?"
    "I grunt and swear my way through the game."
    "And by the time we're done, I'm completely frazzled."
    "My heart is pounding and my breath is coming in gasps."
    "I have to tear my hands off of the console too!"
    kleio.say "There you go, Loverboy."
    kleio.say "I beat you at your own game!"
    mike.say "You sure did, Kleio."
    mike.say "So, do you want to go someplace else now?"
    kleio.say "Hell no!"
    kleio.say "I want a rematch!"
    mike.say "Wait a minute, Kleio..."
    mike.say "I don't know if my heart can take it!"
    return

label kleio_dick_reactions:
    if not kleio.flags.seendick:
        $ kleio.flags.seendick = 1
        if hero.has_skill("hung"):
            show dick reactions kleio smile
            kleio.say "Ahah!"
            kleio.say "I always said you were a big prick!"
            mike.say "Gee, thanks, Kleio!"
            kleio.say "Ah, don't be like that, Loverboy."
            show dick reactions kleio tasty
            kleio.say "Get over here and thank me with that thing instead!"
            $ kleio.sub += 10
        elif hero.has_skill("smalldick"):
            show dick reactions kleio mock
            kleio.say "I take it back, Loverboy."
            kleio.say "You're a little prick, not a big one!"
            mike.say "Hey!"
            kleio.say "Oh, you don't like that, huh?"
            show dick reactions kleio tasty
            kleio.say "Then show me what you can do with that thing!"
            $ kleio.sub -= 10
        hide dick reactions
    return

label kleio_halloween_invitation:
    show kleio
    "As soon as we agreed to host the Halloween party at my place, my mind was made up."
    "I know that there's only one girl I want to invite, that I want to be my date."
    "And that girl's Kleio."
    "She's sure to make the night fun, what with her spikey sense of humour."
    "And I just know that she'll look as hot as hell in a cute Halloween costume too!"
    "All I have to do is be careful pitching the idea to her when I ask."
    "The last thing I need is for her to think that I'm just putting her on show."
    "I mean, Kleio's never been one to shy away from an audience."
    "But I know that she likes that kind of thing to be on her own terms."
    "She'll be furious if she thinks I'm taking advantage of her!"
    "So I'll just have to try to make it sound like a bit of casual fun."
    mike.say "Hey, Kleio..."
    mike.say "[bree.name], Sasha and I are having a Halloween party."
    show fx question
    kleio.say "Huh..."
    kleio.say "You are?"
    "Damn it - that's not the answer I was hoping for!"
    "I expected her to be more enthusiastic."
    mike.say "Yeah, that's right."
    mike.say "And I was wondering if you wanted to come?"
    mike.say "You know...kind of as my date?"
    "Kleio cocks her head on one side."
    "And I can see a crooked smile spreading across her face."
    show kleio annoyed
    kleio.say "Oh, I see."
    kleio.say "And this wouldn't happen to be a costume party, would it?"
    mike.say "Erm..."
    mike.say "There might have been mention of costumes...yeah."
    kleio.say "And you might have gotten an image in your head, right, Loverboy?"
    kleio.say "Maybe an image of your's truly in a certain kind of costume, huh?"
    mike.say "I...I..."
    show kleio happy
    if kleio.love >= 100:
        $ kleio.love += 1
        "Kleio shakes her head and lets out a peal of laughter."
        kleio.say "Okay, Loverboy."
        kleio.say "If that's what you want, I'll come to the party."
        mike.say "You will?"
        mike.say "That's great news, Kleio."
        mike.say "I promise you'll have a great time!"
        show kleio normal
        "Kleio stops me dead in my tracks."
        "She holds up her hand and shakes her head a second time."
        kleio.say "Whoa!"
        kleio.say "Hold on there, Loverboy."
        kleio.say "There's one condition."
        "Suddenly my elation begins to ebb away a little."
        "What on earth can she be talking about?"
        kleio.say "You want to see me in a cute costume, right?"
        mike.say "Um...yeah, Kleio."
        mike.say "I mean...that is...if you want to wear one."
        kleio.say "Okay, then here's the deal."
        kleio.say "It only happens if you're dressed up too."
        kleio.say "And I'm not talking some lame mask or face-paint either."
        kleio.say "You better make an effort."
        show kleio angry
        kleio.say "Or else I'll just turn around and walk away!"
        mike.say "Sure thing, Kleio."
        mike.say "Whatever you say!"
        show kleio normal
        "Oh god - what have I let myself in for?"
        $ game.flags.halloween_girl = "kleio"
    else:
        "Kleio lets out a peal of laughter and shakes her head."
        kleio.say "Fuck's sake, Loverboy!"
        kleio.say "Could you be anymore transparent?"
        kleio.say "You know I like it when you're looking at me."
        show kleio punk
        kleio.say "But I'm not dressing up like a whore for a house full of horny douche-bags!"
        "I nod at this, trying to conceal my disappointment."
        "Well, that and my embarrassment at being found out so easily."
        mike.say "I'm sorry, Kleio."
        mike.say "I guess I just didn't think..."
        show kleio normal
        kleio.say "Aww, don't be like that, Loverboy."
        kleio.say "I'm not mad at you."
        kleio.say "I just think we'd have more fun if we hit up a club instead."
        kleio.say "You know - just you and me?"
        mike.say "You mean just ditch the party?"
        kleio.say "Yeah, Loverboy."
        show kleio seductive
        kleio.say "We can dance real close all night."
        kleio.say "And then we can make each other scream."
        kleio.say "If you know what I mean?"
        "I nod at this, because it does sound more than a little appealing."
        mike.say "I...I'll think about it, Kleio."
        show kleio normal
        kleio.say "Well, don't think about it too long, Loverboy."
        kleio.say "Or else I might go and change my mind!"
    return

label kleio_halloween_arrival:
    scene bg house
    "Opening the door, I guess I should have been more cautious."
    "Especially after the incidents with Jack's sword and Scottie's trident."
    "But I get caught out again as an over-sized mallet swings at me."
    mike.say "SHIT!"
    mike.say "What the actual fuck?!?"
    "I stagger backwards and almost fall into the doorway."
    "Even so, I end up landing on my ass."
    show kleio halloween
    "And it's then that I see Kleio standing over me."
    "She has the mallet slung over her shoulder and a manic grin on her face."
    "All of which makes sense only when I realise what she's come to the party as."
    mike.say "Ch...Charley Queen?!?"
    show kleio punk
    kleio.say "Yeah, that's me!"
    kleio.say "Whadda yah think, puddin?"
    menu:
        "Compliment":
            "I should maybe feel more pissed at being on my ass right now."
            "But all I can think about is how amazing Kleio looks in her costume."
            "She's the perfect Charley Queen, right down to her crazy smile!"
            mike.say "I...if this is what madness looks like..."
            mike.say "I want to share a padded cell with it!"
            show kleio normal blush
            $ kleio.love += 1
            "Kleio tries to keep up the pretence of her character."
            "But I can see her smile turn suddenly genuine and almost bashful."
            kleio.say "You..."
            kleio.say "You mean that, puddin?"
            kleio.say "I...I mean, Loverboy?"
            "I nod with unabashed enthusiasm."
            mike.say "You look hot, Kleio."
            mike.say "Crazy, too - but like crazy hot!"
            kleio.say "I'll take that as a compliment."
            show kleio normal -blush
            "With that, she hefts her mallet back onto her shoulder."
            kleio.say "Come on, puddin."
            show kleio punk
            kleio.say "Let's make this party go with a bang!"
        "Criticize":
            mike.say "Very nice, Kleio."
            mike.say "Or at least it would have been if I weren't laid out on my ass!"
            show kleio annoyed
            "Kleio frowns as she looks down at me."
            kleio.say "Hey, don't be such a scaredy-cat!"
            show kleio normal
            kleio.say "It's Halloween, after all."
            kleio.say "You're supposed to scare people on Halloween!"
            "I shake my head as I pick myself up."
            "Sure, I should be in a better mood for the party."
            "But three people in a row?"
            "All of them swinging weapons in my face?"
            "Even if the last one is my date, it still pisses me off."
            mike.say "Ah..."
            mike.say "How about we leave the bat in the hallway, Kleio?"
            mike.say "That way nobody else needs to get hurt!"
            show kleio annoyed
            $ kleio.love -= 1
            "Kleio sticks her tongue out at me."
            "But she still does as I ask."
            kleio.say "Aw..."
            kleio.say "Party-pooper!"
    scene bg black with dissolve
    pause 1
    return

label kleio_halloween_party:
    $ game.pass_time(2)
    scene bg livingroom
    with dissolve
    kleio.say "Hah..."
    kleio.say "That's cute!"
    "I turn my head to see what Kleio's talking about."
    show kleio halloween at left
    show bree halloween at right
    "And it's then I see she's pointing at [bree.name]'s costume."
    show fx question at right
    bree.say "Huh..."
    bree.say "Is there something the matter?"
    kleio.say "Cute costume, blondie."
    kleio.say "What are you supposed to be?"
    kleio.say "Mechanic Barbie?"
    show bree angry
    "[bree.name]'s cheeks flush with colour."
    "But I see her ball her fists at her sides too."
    "I have to step, and fast."
    "Before this gets out of hand!"
    menu:
        "Defend Kleio":
            mike.say "Ah..."
            mike.say "Kleio's just joking, [bree.name]!"
            show kleio surprised
            kleio.say "Oh, I am, am I?!?"
            mike.say "Yeah, Kleio - of course you are!"
            bree.say "Well, it wasn't very funny!"
            show kleio normal
            mike.say "Look, [bree.name] - Kleio's a mechanic."
            mike.say "And I'm sure she just got a kick out of your costume."
            "[bree.name] narrows her eyes at me."
            show bree normal
            "But then she nods her head."
            bree.say "Okay, [hero.name], I believe you."
            hide bree
            hide kleio
            show kleio halloween
            "She turns her back on us and walks away."
            "And I feel like I can finally breathe out."
            show kleio happy
            $ kleio.love += 2
            kleio.say "Nice save, Loverboy!"
        "Defend [bree.name]":
            mike.say "Hey, Kleio, back off already!"
            mike.say "It's just a costume."
            mike.say "Sure, [bree.name]'s dressed like you do at work."
            mike.say "But you're a mechanic, not a Green Beret!"
            $ bree.love += 2
            $ kleio.love -= 2
            show bree happy
            show kleio angry
            "[bree.name] smiles, pleased at my coming to her defence."
            "But Kleio snorts and shakes her head."
            kleio.say "Geez, Loverboy."
            kleio.say "Way to be blondie's knight in shining armour!"
            kleio.say "What happened to you being MY date tonight?"
            show bree normal
            mike.say "Of course I'm your date, Kleio."
            mike.say "But you were being a bit of an ass just now!"
            "Kleio snorts again and rolls her eyes."
            "She's clearly unhappy with me defending [bree.name]."
    scene bg black with dissolve
    pause 1
    return

label kleio_halloween_dance:
    $ game.pass_time(2)
    scene bg livingroom
    with dissolve
    "This really shouldn't be a big deal."
    "I mean, we're at a party and there's music."
    "Sooner or later the notion of dancing has to come up."
    "But part of me is still a little nervous to actually ask Kleio!"
    "She's just so spikey and independent, you know?"
    "I'm kind of afraid that she'll think it's sexist or something."
    show kleio halloween
    kleio.say "Hey, Loverboy!"
    mike.say "Uh..."
    mike.say "Yeah, Kleio?"
    kleio.say "Come on - let's dance already!"
    menu:
        "Accept":
            "I almost say something to Kleio."
            "Like I'm going to complain that I wanted to ask her."
            "But then the idea just seems totally dumb to me."
            "Why in the hell am I overthinking things?"
            "What does it matter who asked who to dance?"
            hide kleio
            mike.say "W...wait up, Kleio."
            $ kleio.love += 2
            mike.say "I'm coming!"
            show dance kleio halloween
            "The song that Kleio's chosen is a classic punk anthem."
            "So there's no thought of us doing a slow dance to it."
            "But the energy she puts out is enough to hypnotise me."
            "All I can do is follow her lead, trying to keep up."
            "And I don't know what makes me more breathless."
            "Matching Kleio's pace or the sight of her body moving!"
            "The only time that she actually touches me is afterwards."
            "And that's as she almost collapses into my arms."
            "She's panting, exhausted and utterly spent."
            "I can feel the sweat that's soaking her skin."
            "Her chest is heaving, pushing her breasts against me."
            "And I don't think I've ever wanted her more than in that moment."
        "Object":
            mike.say "Aw, Kleio!"
            mike.say "I was waiting to ask you to dance!"
            show fx question
            "Kleio shakes her head at me."
            show kleio seductive
            "And I can see that she's amused."
            kleio.say "Oops!"
            kleio.say "Did I bruise your manhood!"
            mike.say "Hey - it's not funny!"
            show kleio annoyed
            $ kleio.love -= 2
            "Kleio rolls her eyes and chuckles."
            kleio.say "Tell you what, Loverboy - let's take a rain check."
            kleio.say "I don't want to do any more damage!"
            hide kleio
            "I don't know what's worse."
            "Knowing that I blew my chance to dance with Kleio."
            "Or the sting of the insults that I got along the way."
    scene bg black with dissolve
    pause 1
    return

label kleio_halloween_sex:
    scene bg livingroom
    show kleio halloween
    with fade
    "The party's started to wind down a little by now, and the house is much quieter."
    "Almost everyone is feeling tired, drunk or a mixture of both, and wants to relax."
    "But I can see from the look on Kleio's face that she's not feeling that vibe."
    scene bg secondfloor
    show kleio halloween
    with fade
    "We're upstairs, and she's leading me towards my bedroom."
    kleio.say "Come on, pudding."
    show kleio punk
    kleio.say "Let's go have some fun on our own!"
    mike.say "Sure thing, Kleio."
    mike.say "That sounds like a great idea!"
    show kleio normal
    "Kleio grins at me, the make-up she's wearing exaggerating the effect."
    "It's weird, for sure - but somehow makes her seems sexy in a crazy way."
    "I'm so caught up in staring at Kleio in that moment."
    "I almost fail to notice what door she's actually opening."
    mike.say "Erm, Kleio..."
    mike.say "You do realise that's Sasha's bedroom?"
    show kleio seductive
    "Kleio only grins wider and laughs at this."
    "And I hope she's just playing around."
    "You know, getting into character?"
    kleio.say "Of course I know that, pudding."
    show kleio punk
    kleio.say "But tonight I'm channelling Charley Queen."
    kleio.say "So I'm gonna be crazy and live dangerously!"
    "Kleio still has me by the wrist."
    "And now she's dragging me into Sasha's bedroom."
    "I try to resist, but she's scarily strong."
    mike.say "Wh...what if Sasha finds us?"
    mike.say "Kleio, you know she'll freak!"
    kleio.say "If she walks in, then I'll handle it, pudding."
    show kleio punk
    kleio.say "She can either join in or get the hell out!"
    kleio.say "Her choice..."
    show kleio normal
    "Kleio keeps on pulling me over the threshold."
    "But seeing I can't talk her out of it, I change my tactics."
    "I stop resisting all at once, but this backfires on me."
    "Suddenly there's nothing to stop Kleio getting her way."
    scene bg bedroom3
    show kleio halloween
    with hpunch
    play sound door_slam
    "And we both tumble into Sasha's room, the door slamming behind us."
    "Somehow Kleio and I end up on the bed in a tangle of limbs."
    show kleio kiss halloween with fade
    $ kleio.flags.kiss += 1
    "She clings onto me, pushing her tongue into my mouth."
    "Look, I might have been scared of Sasha walking in on us."
    "But I'm only human."
    "And the mere thought of Kleio can get me hot as hell!"
    "Before I know it, I'm kissing Kleio with a passion."
    "That and tearing at her costume, trying to strip her naked."
    kleio.say "Ah..."
    kleio.say "That's more like it, pudding."
    kleio.say "Mmm..."
    kleio.say "Charley wants you inside of her!"
    "We're making such a mess of limbs, struggling with buttons and zippers."
    show kleio rough bedroom halloween with fade
    "So much so that I'm not sure either of us is prepared when it happens."
    "I feel the head of my cock slide against something warm and slick."
    show kleio rough pleasure
    "And at the same moment, Kleio moans with desire and need."
    kleio.say "Ah..."
    show kleio rough normal
    kleio.say "Please..."
    "All it takes is a thrust forwards..."
    show kleio rough vaginal pleasure
    "And I'm inside of her."
    "Kleio wraps her legs around me, pulling me atop her."
    "I'm not sure if I push my cock into her."
    "Or if she clambers onto it herself!"
    "But either way, we're intertwined and going for it."
    "Somehow, Kleio ends up almost upside down, my weight pinning there."
    "There's no time for foreplay or a slow build."
    show kleio rough stomp
    "Instead I'm pounding away at Kleio with all my strength."
    "And she's soaking it up, taking everything I have to give."
    kleio.say "Yes..."
    kleio.say "Oh shit..."
    kleio.say "Fuck me harder!"
    "I only half hear Kleio's demands for more."
    "And even if I could make sense of them, I can't do any more."
    "I can already feel Sasha's bed rocking and creaking under us."
    "And I might have accepted that she could walk in any moment."
    "But that doesn't mean I'm going to break her bed to get Kleio off!"
    show kleio rough creampie ahegao with vpunch
    "Not that it matters, as I can already feel myself cumming."
    with vpunch
    "Kleio clings onto me as I shoot my load into her."
    with vpunch
    "She cries and wails as she cums too."
    show kleio rough pile with vpunch
    "If Sasha were to walk in on us now..."
    "Well, what could she say that would change a thing?"
    "And what if she were mad at me?"
    "It'd be worth it for the chance to fuck Kleio!"
    show kleio rough pleasure
    kleio.say "Mmm..."
    kleio.say "I love ya, pudding!"
    mike.say "I love you too, Kleio!"
    $ kleio.sexperience += 1
    $ game.pass_time(1)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
