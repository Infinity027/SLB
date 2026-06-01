init python:
    Event(**{
    "name": "anna_hottub_sex_male",
    "label": "anna_hottub_sex_male",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("date_hot_tub_home")),
        PersonTarget(anna,
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

label anna_hottub_sex_male:
    $ game.active_date.clothes = "swimsuit"
    $ CONDOM = False
    show bg pool
    show anna swimsuit
    with fade
    mike.say "Whoa..."
    mike.say "Slow down, Anna!"
    show anna happy at startle
    anna.say "Ha, ha..."
    anna.say "No way, [hero.name]!"
    show anna evil
    anna.say "That hot-tub's got my name on it!"
    "When I asked Anna over to take a dip in the hot-tub with me, I never expected this!"
    "But then she did say yes on the spot, then bug me until the appointed day arrived."
    "Now she's wearing nothing but her swimsuit and dragging me behind her to the tub."
    "It's all that I can do to pull my trunks on before she pulls me out of the house naked!"
    "Anna leads me across the patio and over to where the hot-tub stands."
    "Seeing that it's already full of hot, bubbling water, she jumps straight in."
    hide anna
    show hottub anna with fade
    "As she still has a death-grip on my hand, I'm pulled in along with her too."
    "Totally unprepared, I disappear under the surface of the water with a wail."
    mike.say "Anna..."
    mike.say "What the..."
    mike.say "Glug..."
    "And then I pop up a few seconds later, coughing and spluttering."
    "But even before I've managed to regain my senses, I feel Anna grab me again."
    anna.say "Oh no you don't, [hero.name]."
    anna.say "You're not getting away that easily!"
    "I find myself thrashing around in the water, not knowing what's happening to me."
    "And in my state of confusion, I almost disappear under the surface a second time."
    mike.say "Anna..."
    mike.say "What are you trying to do?"
    mike.say "Fucking drown me?!?"
    "All of a sudden, Anna stops dead in her tracks."
    "She looks at me wide eyes with surprise."
    anna.say "I...I was just being playful."
    anna.say "I didn't mean to hurt you, [hero.name]!"
    "I can see from the look in Anna's eyes that she's getting upset."
    "She thinks that she's done something to seriously piss me off."
    "I might have been none too pleased to be dragged into the tub just now."
    "But I'm not about to let it ruin the chances of us having a good time together!"
    mike.say "You...you didn't, Anna."
    mike.say "It's okay, really it is."
    mike.say "I was just a little shaken up, that's all."
    mike.say "But I'm fine now, see?"
    "Anna nods, still not looking totally convinced."
    "She looks down at the water, clearly thinking it over."
    "And then she looks up at me again, a smile spreading across her face."
    anna.say "I know what, [hero.name]."
    anna.say "How about I do something to make it up to you, huh?"
    anna.say "Something REALLY special?"
    "Now that sounds more like the time in the hot tub that I had in mind!"
    "I make sure that my smile communicates the fact that Anna's forgiven."
    "And I nod my head in agreement at the same time."
    mike.say "Sure thing, Anna."
    mike.say "That sounds like a great idea!"
    mike.say "What did you have in mind?"
    show hottub sex male anna outside with fade
    "By way of answer, Anna returns my smile and turns around in the water."
    "She presents her ass to me, shaking it in the most provocative manner."
    "Anna glances back over her shoulder at me, winking wickedly."
    "But it's not like I really need to be given such a strong hint."
    "What she has in mind is exactly what I do too!"
    "I grab hold of Anna at the waist with one hand."
    "And with the other I pull down my trunks."
    "She giggles with anticipation as I do this."
    "And her eyes go wide as soon as she sees how hard I am for her."
    call anna_dick_reactions from _call_anna_dick_reactions_1
    "Anna bites her lips and turns her head back so that she's looking forwards."
    show hottub sex male anna inside
    "Which I take as my cue to begin probing between her legs with my cock."
    "She's already nicely slick when the head finds her pussy."
    "The lips tell me just how much she wants this."
    "And there's little resistance as I find my way inside of her."
    "Anna makes a satisfied sound as I push the length of my cock further."
    "A sound that doesn't stop until it's buried as deep in her as it'll go."
    "But as soon as I start moving back and forth, the sound changes."
    "Within seconds, I hear it transform into a panting and moaning."
    "And Anna begins to rock to the rhythm that I'm fucking her with."
    "I feel like she's totally surrendering herself to me."
    "Like she's losing the will to do anything but let me have my way."
    "Which only makes me all the more eager to push deeper and harder."
    "By now I have one hand on Anna's shoulder, holding her in place."
    "The other is resting on the edge of the tub behind me, stopping me from falling."
    "And between the two, I move in and out of Anna like a tireless machine."
    "Yet for all that I'm making a show of being tireless, I'm only human."
    "Anna might seem to be able to keep on taking what I'm giving her forever."
    "But that doesn't mean that the same is true of my ability to keep it up!"
    "Even as her hot little body is eating it up, I can feel the end approaching."
    "And so I redouble my efforts, not caring that doing so might end it quicker."
    "If this has to be a short burst of passion, then so be it."
    "But I'm damned if it's not going to be an explosive one too!"
    call cum_reaction (anna, 'vaginal', 1) from _call_cum_reaction_18
    if _return == "vaginal_outside":
        show hottub sex male outside
        "Anna quivers and wriggles as I pull my cock out of her before the end."
        "The sensation seems to have a dramatic effect, making her moan and yelp."
        show hottub cumshot with vpunch
        $ anna.sub += 1
        "And I only realise that it's pushed her over the edge as I shoot my load a second later."
        with vpunch
        "I hold Anna in place as the cum rains down on her ass and spatters her thighs."
        with vpunch
        "She cums at the same time, writhing in my grip as it takes a hold of her."
        "And only when I feel it passing do I finally let her go."
    else:
        "Anna's shaking with the sensation of what I'm doing to her by now."
        "And even she's starting to show signs of reaching her climax."
        show hottub cumshot with hpunch
        $ anna.love += 1
        "So when I shoot my load inside of her, it has a dramatic effect."
        show hottub sex male ahegao with hpunch
        "She seems to cum a second later, wriggling on the end of my cock."
        with hpunch
        "I hold her in place the entire time, making sure Anna takes the whole thing."
        "And only when I can feel the cum seeping out of her do I finally let go."

    hide hottub sex male
    show hottub anna
    with dissolve
    "I sit down in the water a moment before my legs give way under my own weight."
    "And Anna collapses in front of me no more than a second later."
    "She lays her back against my chest and snuggles against me happily."
    "There's no need to speak, just for me to hold her in the water."
    "What we just did together says more than words ever could."
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ anna.sexperience += 1
    $ game.active_date.clothes = None
    return

label anna_fuck_date_male(location="hero"):
    $ game.play_music("music/roa_music/city_nights.ogg")
    scene bg bedroom1
    $ game.room = "bedroom1"


    call anna_fuck_date_intro_male (location) from _call_anna_fuck_date_intro_male


    call anna_dick_reactions from _call_anna_dick_reactions


    call anna_fuck_date_foreplay_male from _call_anna_fuck_date_foreplay_male




    call anna_fuck_date_choices_male from _call_anna_fuck_date_choices_male


    call handle_npc_leaving (anna, _return) from _call_handle_npc_leaving_2
    if _return:
        return


    hide anna
    call anna_sleep_date_fuck (location) from _call_anna_sleep_date_fuck
    return

label anna_fuck_date_intro_male(location="hero"):
    if not anna.sexperience:
        "I close the bedroom door behind Anna, still not quite believing we're going to do this."
        "I try to look confident, but my smile ends up being too much."
        show anna
        show anna happy at startle
        "Anna can't help giggling, which sets me off laughing too."
        menu:
            "Say something to break the ice":
                mike.say "Hope you're not laughing when we're naked."
                show anna embarrassed
                anna.say "Sorry, I guess I'm more nervous than I thought."
                show anna blush
                anna.say "Don't worry, it's not you, just doing this kind of thing."
            "Kiss her to break the ice":
                show anna kiss with fade
                $ anna.flags.kiss += 1
                "I gently lean in to kiss her, stopping her giggles in their tracks."
                "Anna stiffens for a second, then relaxes, melting into the kiss."
                hide anna
                show anna blush with fade
                "She pulls away a few seconds later, her cheeks a little flushed."
        mike.say "Are we going too fast for you?"
        mike.say "If you want to slow down, just say so - I won't be mad."
        show anna blush
        "Anna looks away for a moment, then back to meet my eye."
        anna.say "It's just...it's been a long time since I dated..."
        anna.say "Well, since I dated a guy...or been with one."
        "I know all about her being bi-sexual, and it doesn't bother me in the least."
        "In fact, I've never been with a bi-sexual girl before, and so I'm feeling a little nervous as well."
        menu:
            "Try to sound confident":
                mike.say "Don't worry about it, Anna."
                mike.say "We can go as slow, or as fast as you like."
                $ anna.sub += 1
            "Try to sound sensitive":
                mike.say "Don't laugh at me, Anna..."
                mike.say "But I'm feeling a bit scared too."
                $ anna.love += 1
        show anna happy
        "Anna nods and gives me a little smile, silently thanking me for my words."
        show anna blush
        anna.say "It's not just that, [hero.name]."
        anna.say "I have to show you something before we go any further."
        "I nod, trying to be all woke and understanding."
        "But inside I'm afraid that she's going to show me something that'll freak me out or turn me off."
        "Anna returns my nod and quickly turns her back to me."
        show anna a close naked at top_to_bottom with dissolve
        "She yanks off her t-shirt and then pulls down the back of her jeans."
        "There, on the small of her back, is a tattoo which reads ANAL WHORE."
        show anna blush at bottom_to_top
        menu:
            "Gasp in shock" if hero.charm >= 25:
                "I let out a gasp, genuinely shocked at the tattoo."
                show anna embarrassed
                anna.say "Ah shit, I knew you'd hate it!"
                anna.say "I didn't want to show you, but how could I not if we're going to do this?"
                mike.say "I don't hate it."
                mike.say "It's just...a surprise, that's all."
                $ anna.love += 1
            "Laugh in surprise":
                "I laugh before I can stop myself."
                show anna embarrassed
                anna.say "You think it's funny?!?"
                mike.say "No...yes...well, maybe a little bit."
                mike.say "It's kind of like something that makes you laugh at an awkward time."
            "Whistle and shake head" if hero.charm >= 50:
                "All I could do was whistle and then chuckle."
                show anna embarrassed
                anna.say "You hate it, don't you?"
                mike.say "Nah, it's just so crazy that it knocked me for six!"
                anna.say "So you think I'm crazy too now?"
                mike.say "Not crazy like a psycho, crazy like a wild thing!"
                mike.say "Anna, I don't know what you're gonna show me next, but I want to find out!"
                $ anna.love += 1
                $ anna.sub += 1
        hide anna
        show anna a naked
        "Anna looks back at me over her shoulder, a weak smile growing on her face."
        "She seems reassured by my words."
        mike.say "So are you?"
        show anna annoyed
        "Anna looks puzzled at the question."
        anna.say "Am I what?"
        mike.say "An anal whore?"
        show anna close happy
        "Anna's smile becomes wider, and much more wicked."
        show anna blush
        anna.say "Would you like me to be your anal whore?"
        "I feel a genuine twinge of delight at the way her eyes are sizing me up right now."
        "I realise that I've been let in on one of the most intimate secrets of what turns this girl on in the bedroom."
        "I nod."
        anna.say "Big talk, [hero.name]!"
        anna.say "If you want me to be your little anal whore, then you better show me how you're gonna make me into one!"
        "She's taunting me now, wanting me to make good on my promises."


        show anna a close naked at top_to_bottom
        "Leaning in close, I begin to massage her buttocks."
        "Anna moans a little at first, encouraging me to squeeze harder, which makes her moaning become louder in response."
        mike.say "Hello, little ass."
        mike.say "I'm going to have to fuck you now, quite hard."
        mike.say "I'm going to have to fuck you, because the little whore you belong to likes it rough."
        show anna a close naked happy at bottom_to_top
        "Anna twists round at this, eyes twinkling with anticipation after my talking dirty to her ass."
        "She takes me firmly by the hand as she kicks off her jeans, using the other to take off her underwear as she leads me quickly to the bed."
        "We struggle for a moment, as she tries to pull off the same clothes as me at the same time, but soon we're both naked and rolling on the unmade bed."
    elif anna.sub >= 50:
        show anna
        if anna.sexperience % 3:
            "As I open the door into the bedroom and step inside, I turn to see that Anna's still standing on the threshold."
            "For a moment this throws me, and I can't help thinking that something's wrong."
            "Not only that, but it's somehow managed to completely escape my attention too."
            mike.say "What is it, Anna?"
            mike.say "What's up?"
            "By way of response, Anna glances down at the floor before looking up at me with a bashful expression on her face."
            anna.say "You didn't invite me in yet, [hero.name]..."
            "I stare at her for a good few seconds, until what she's actually saying fully sinks in."
            "Is she kidding me, or what?"
            mike.say "What was I thinking!"
            mike.say "Come on in, Anna..."
            show anna happy
            "I watch as she smiles broadly and strolls into the room, a look of disbelief still on my face."
            "Sure, she likes me to take the lead in our relationship, and I'm into that."
            "But is she turning into some kind of vampire now, needing permission to cross a threshold before she'll come in?"
            "I try to shake off the thought as I close the door behind her and nod in the direction of the bed."
            "The date's gone pretty well, and we've both had a really good time."
            "So I want to end the night on a high note too."
            "And as usual, Anna seems more than willing to bend herself to my will."
            "Especially seeing as we're now in the bedroom!"
            "She practically skips to the bed and starts to pull off her clothes."
            "But then she suddenly pauses and stares at me, looking like she's afraid of getting ahead of herself."
            "What does she think - that I'm seriously going to invite her back to my place and then get pissed that she's stripping off?"
            "I nod eagerly, trying to encourage her to continue with what she was doing, and beginning to undress at the same time."
            show anna a naked with dissolve
            "Anna smiles, instantly reassured, and quickly finishes off the act of removing her clothes."
            show anna close at bottom_to_top with dissolve
            "But still she makes no move towards the bed, no effort to initiate anything between us."
            "The desire is definitely there in her eyes, and I'm sure she wants the same thing as I do right now."
            "Yet it looks like I'm going to have to be the one to take things in hand, or else we'll get nowhere fast."
        else:
            "Anna practically skips out of the taxi and up the path to the front door of my house."
            "She keeps on looking back over her shoulder, winking and beckoning for me to hurry up."
            "So I pay the taxi driver and chase after her as soon as I can, opening the door so we can go inside."
            "Anna giggles and hurries off in the direction of my bedroom with me close on her heels."
            scene bg bedroom1
            show anna
            with fade
            "I mean, I thought the date went pretty well tonight, that we both had a great time."
            "But it seems like Anna enjoyed herself more than I realised."
            "And she's not about to let the fun come to an end just yet!"
            anna.say "Come on, [hero.name]!"
            anna.say "What are you waiting for?"
            show anna happy
            anna.say "Don't you want some of this?"
            "I'm just closing the door behind me as Anna asks the question."
            "And I shake my head as I turn to face her, amazed that she even needs to ask."
            "But when I finally lay eyes on her, the words I was going to say die in my mouth."
            show anna underwear with dissolve
            "Anna's already stripped down to her underwear in the middle of the room."
            "And now she's unhooking her bra so that she can slip it off."
            show anna topless with dissolve
            "A moment later, her breasts are free, swaying gently as she moves."
            "Then she bends over to pull down her panties and kick them off."
            show anna naked with dissolve
            "Now I can see every part of Anna's naked body."
            "Her petite form and exaggerated curves are all right there."
            "And I can already feel my cock straining against the elastic of my shorts!"
            mike.say "Y...yeah, Anna!"
            mike.say "I want some of that!"
            "Anna lets out a mischievous giggle."
            "Then she rushes over to the bed and jumps onto the mattress."
            show anna blush
            anna.say "Then you'd better come get it!"
            anna.say "You think you can do that?"
            "I nod eagerly, already starting to strip off as I do so."
            "Every step I take towards the bed sees me shed another item of clothing."
            "And so, hopping and staggering, I make it to the bed as I finally get naked."
            "Anna's sitting up on her haunches, watching my progress."
            "And she claps her hands together with glee as I climb onto the bed."
            anna.say "That's it!"
            anna.say "That's what I want right there!"
    elif randint(1, 2) == 1:
        show anna naked
        "Anna peels off the last of her clothes and hurries over to the bed, beckoning for me to follow."
        "I try to shed the last of my own at the same time, almost tripping over as I do so."
        "She chuckles as she clambers backwards onto the mattress, not stopping until her head hits the pillows."
        anna.say "Don't hit your head, [hero.name]."
        anna.say "You're a guy - you're not supposed to fall unconscious until AFTER you cum!"
        "As if the sight of her naked body before me wasn't enough, Anna's giggles are driving me mad too."
        "For a moment I'm actually afraid that I will knock myself out in my desperation to reach her."
    else:
        "I have to practically chase Anna in to the bedroom if I want to keep up to her as she darts through the door before me."
        "The exact details of what went down on our date and how it ended are already starting to be pushed out of my mind by thoughts of what lies ahead."
        "I can't remember if it went well or not, and likewise I have no idea if Anna's in this mood because she's happy with me or just plain drunk."
        "Either way, I'm not about to stop her and ask for a blow-by-blow reminder of how we got to this point."
        "Not when Anna grabs me by the wrist and drags me towards the bed, looking back over her shoulder at me with a mischievous grin."
        "The promise implied by that smile is enough for me, regardless of just where it came from exactly."
        "I offer no resistance, allowing myself to be pulled in Anna's wake all the way to within a few feet of the bed."
        show anna naked with dissolve
        "Neither of us speaks a word as we begin to strip off, each helping the other at opportune moments."
        show anna close naked happy at bottom_to_top with dissolve
        "Once we're naked, Anna gives me another one of those irresistible smiles."
        hide anna
        show anna kiss naked with fade
        $ anna.flags.kiss += 1
        "And then she stands on her tip-toes to be able to plant a long and very pleasant kiss on my lips."
        hide anna
        show anna naked
        with fade
        "When it's over, she cocks her head on one side, looking quizzical."
        anna.say "Well, [hero.name] - did you like that?"
        mike.say "Of...of course, Anna."
        mike.say "It was really something else!"
        anna.say "Good, because there's more where that came from."
        anna.say "If you come and get it!"
        "With that, she backs to the edge of the bed and climbs onto it still holding my eye."
        "I watch as Anna reaches the head of the bed and lays down to recline with her head on the pillows."
        "As if she needs to tempt me to follow her lead!"
        "I waste no time in clambering onto the bed after Anna, almost as though I have to catch her and hold onto her."
        "She makes no sign whatsoever of being about to evade my grasp, but still I feel the need to pin her down, just to be sure."
        "Anna giggles as I take hold of her, wriggling almost as eagerly into my arms as I embrace her."
        anna.say "Okay, [hero.name] - you can have it."
        anna.say "But there's one little problem..."
        "I look at her wide-eyed for a moment, worried that she's about to sink my hopes for ending the evening in a pleasant manner."
        mike.say "What is it, Anna?"
        anna.say "All of that good stuff I promised you?"
        anna.say "It's all hidden up here."
        "She looks down and points between her thighs."
        anna.say "So if you want it that bad, you have to dig for it!"
        "I shake my head at this, relieved that she's only joking around."
        mike.say "Don't you worry, Anna."
        mike.say "I have just the tool for the job, right here!"

    return _return

label anna_fuck_date_foreplay_male:
    if anna.sub >= 50 and hero.sexperience >= 10:
        menu:
            "Go down on her":
                call anna_cunnilingus from _call_anna_cunnilingus
            "Make her suck you off":
                call anna_fuck_date_blowjob from _call_anna_fuck_date_blowjob
            "Fuck her tits" if anna.sub >= 50 and hero.sexperience >= 10:
                call anna_fuck_date_titjob from _call_anna_fuck_date_titjob
            "Just fuck her":
                return
    call stop_all_sfx from _call_stop_all_sfx_4

    return _return

label anna_fuck_date_choices_male:
    scene bg bedroom1
    show anna naked
    menu:
        "Cowgirl":
            call anna_fuck_date_cowgirl (0) from _call_anna_fuck_date_cowgirl
        "Doggy" if hero.sexperience >= 5:
            call anna_fuck_date_doggy (5) from _call_anna_fuck_date_doggy
        "Missionary" if hero.sexperience >= 10:
            call anna_fuck_date_missionary (10) from _call_anna_fuck_date_missionary
    call stop_all_sfx from _call_stop_all_sfx_5

    return _return

label anna_sleep_date_fuck(location="hero"):
    if game.hour > 19 or game.hour < 6:
        scene bg bedroom1
        show anna naked
        if anna.is_sex_slave:
            anna.say "May I share your bed tonight, Master?"
        else:
            anna.say "Mmm...you cool with me spending the night here?"
        menu:
            "No":
                mike.say "No...I have to be up really early in the morning."
                "The sex was beyond incredible, but now I want to be alone."
                "Anna frowns in disappointment, clearly trying to shrug off the sense of rejection."
                anna.say "Okay...sleep well, I guess."
                "She shakes her head as she collects her things and leaves my bedroom."
                $ anna.love -= 3
                call sleep from _call_sleep_18
                $ game.room = "bedroom1"
            "Yes":
                mike.say "YES...I mean, yes...if you want to!"
                "I try to keep from sounding too desperate and needy, but I'm not sure I manage it."
                show cuddle anna
                "Anna curling up against me beneath the covers is almost as good as the sex - almost..."
                if anna.is_sex_slave:
                    anna.say "Sweet dreams, Master..."
                else:
                    anna.say "Sweet dreams, [hero.name]..."
                mike.say "You too, Anna..."
                $ anna.love += 3
                call sleep ("anna") from _call_sleep_14
                $ game.room = "bedroom1"
    return

label anna_cunnilingus:
    show anna cunnilingus
    anna.say "Wh...what are you going to do to me?"
    mike.say "I'm going to lick and lick, until you can't take anymore."
    mike.say "I'm going to lick that little pussy of yours until you beg me to stop!"
    anna.say "Oh, you...you beast!"
    anna.say "My poor little pussy!"
    show anna cunnilingus mike pleasure
    "Before Anna can say another word, my head is between her thighs."
    "She lets out one more giggle, and then my tongue makes contact with her lips."
    anna.say "Mmmm..."
    show anna cunnilingus normal
    anna.say "Oooh..."
    "Now, I'm a big fan of Anna's pussy."
    "I love the look, the feel and the scent of it."
    "But feeling it under my tongue is like something else entirely."
    "It's intricate folds draw my tongue in towards the centre."
    "And the taste of her, now that she's wet for me, is amazing."
    "I feel Anna flop backwards onto the bed, surrendering to the experience."
    "A move that I take as my cue to go deeper still."
    menu:
        "Use my tongue":
            "All I can think about is Anna's pussy and getting as deep into it as I can."
            show anna cunnilingus pleasure
            "I turn my tongue sideways, slipping it between her lips and pushing deeper still."
            "It almost feels like kissing her on the mouth, my lips against hers."
            "Anna's still moaning and letting out gasps of breath."
            "But the sounds seem to be coming from far away, indistinct and unformed."
            "All they are to me is permission to keep on doing more of the same."
            "What I wouldn't give right now for a longer tongue!"
            "No matter how I try, I just can't seem to get as deep as I'd like."
            "Not that my efforts are going unappreciated though."
            "I can feel Anna's thighs twitching and jumping as I push right on."
            "They squeeze against the sides of my head, threatening to press even harder."
            "Anna's petite body is quivering all over now."
            "It's like the movement of my tongue is touching every part of her."
            "The sensations spreading out like sympathetic vibrations."
            show anna cunnilingus ahegao onmike
            "Suddenly I can hear her for the first time, clear as crystal."
            "She's beginning to cry out, making little whining sounds."
            "Then Anna's thighs really do clamp down on me."
            "And I find my face pressed tightly against her groin!"
        "Finger her ass":
            "I know Anna pretty well, you know?"
            "Well enough to have been storing up all those little quirks she possesses."
            show anna cunnilingus -onmike finger normal
            "Which is why I slide a cold hand under her backside without warning."
            anna.say "Whoa!"
            anna.say "That's freezing!!!"
            "Anna instinctively lifts her ass off of the mattress."
            "But I keep my hand right where it is, one finger pointing upwards."
            "This means that when she lowers it back down..."
            show anna cunnilingus pleasure
            anna.say "Oooh!"
            anna.say "What's...wha..."
            anna.say "Mmm..."
            "Any other girl and I might have been taking a gamble with sticking a finger up their ass."
            "But I know full well that this is one of those kinky little things that Anna just loves."
            "Which is why she sinks happily down, letting me probe her ass to my heart's desire."
            "I probe deeper with my finger."
            "And all the time Anna squirms with delight, helplessly in my power."
            "All she can do is let out whines of pleasure, which build in intensity."
            show anna cunnilingus ahegao
            "Before I know it, she's twitching and writhing."
            "Which I guess means that she's about to cum!"
        "Use the anal beads" if "anal_beads" in hero.inventory and hero.sexperience >= 15:
            "I keep up the attention to Anna's pussy with almost religious devotion."
            "Because after all, it's not like I don't actually enjoy giving her oral!"
            "But at the same time, I'm groping under the bed for something."
            "Specifically I'm looking for something that I know will make this much more interesting."
            "As luck would have it, Anna's pelvis bucks almost the same moment I grasp the anal beads."
            show anna cunnilingus -onmike beads normal
            "And I don't waste the chance to shoot that same hand under her with them at the ready."
            "When she comes back down again, she almost does the hard work for me!"
            anna.say "Oooh!"
            anna.say "What's that?!?"
            anna.say "Oh...oh...you naughty boy!"
            show anna cunnilingus pleasure
            "Anna giggles in pure delight, wriggling so that the beads work their way in yet further."
            "Sure, she wasn't expecting it, but I know just how much she loves this kind of thing."
            "With each bead that I push up there, Anna moans in sheer delight."
            "And she moves so much that it's hard for me to keep up with my tongue!"
            "But still I keep it up as best I can, feeling like Anna might smother me at any moment."
            "Once all the beads are finally up there, I know that it's time to put on a show."
            "And so I redouble my efforts, probing ever deeper into Anna's ass."
            "I swear that there's not a part of it within reach that I haven't touched."
            show anna cunnilingus ahegao
            "The fruits of my labour being that she's soon worked into a state of helplessness."
            "Anna's so far gone by the time that I tug on the beads, I swear she's forgotten where she is!"
            "But when they come popping out of her ass like a string of bullets, she wails for all she's worth."
        "Use the dildo" if hero.has_item("dildo") and anna.sub >= 60:
            "I know full well that my attention to her pussy is keeping Anna occupied."
            "Which means that she doesn't notice as I reach under the bed."
            "My hand closes around the dildo I know is hidden down there."
            "And then I inch it ever closer to Anna's pussy while still probing with my tongue."
            show anna cunnilingus -onmike normal dildo
            "This means that when I push it into her, she has no idea what's coming!"
            anna.say "Mmm..."
            anna.say "Wha...what are you..."
            "The dildo is already halfway into her by now, sinking deeper every second."
            show anna cunnilingus pleasure
            anna.say "Oh...oh yeah..."
            anna.say "Fuck me with that thing!"
            "Not wanting to disappoint the lady, I do just as she asks."
            "I still take care to lick at the outer fold of her pussy."
            "But at the same time, I plunge the dildo as deep into Anna as it'll go."
            "She bucks and twitches atop the mattress, as I do so."
            "Her body greedily swallows the thing with a sensual sound."
            "I work her with it as best I can, trying to keep time with my tongue."
            "And I must be doing a good job, as Anna soon begins to pant desperately."
            show anna cunnilingus ahegao
            "I can feel her muscles clenching as she begins to build towards something big."
            "But it's when she lets out a high-pitched wail that I finally know she's cumming!"
    show anna cunnilingus pleasure -onmike
    "Anna wriggles beneath me, her orgasm shaking every inch of her petite body."
    "I might not be the one getting to let off steam right now."
    "But it feels amazing to know what it was my efforts that put her in such a state!"
    show anna cunnilingus -mike
    "Anna moans as the aftershocks take hold, her breasts quivering the whole time."
    "She looks me in the eye a moment later, smiling happily and satisfied beyond words."
    return

label anna_fuck_date_titjob:
    "She beckons me closer as I climb onto the bed and crawl towards her, smiling over her breasts in approval."
    scene bg black
    show anna tittyfuck with fade
    "By the time I've made it and I'm straddling Anna's belly, my cock is already painfully stiff."
    "It sways and bobs above her breasts, and she eyes it with a hunger that gets me even hotter than before."
    anna.say "Well hello there, big boy!"
    anna.say "I've got a couple of friends that are just dying to meet you..."
    "And with that, Anna wastes no more time on innuendo and foreplay."
    "Instead she pushes her breasts together, lightly at first."
    show anna tittyfuck up
    "Their heavy, rounded shapes completely cover the head and perhaps half the length the shaft."
    show anna tittyfuck down
    "The feeling is instantly incredible, like my cock's been wrapped in warm dough."
    if False:
        "In my rush to catch up to Anna, I almost forgot that we'd agreed that I'd film this."
        "Luckily I can see my phone on the floor, where it must have tumbled from my pocket as I stripped off."
        "I strain and just manage to reach it, hurriedly setting it to record and getting Anna fully in frame."
        "She grins wickedly, clearly recalling just what we're going to use the video for."
    else:
        "Anna grins wickedly, clearly ready to go and relishing the thought of what we're about to do."
    show anna tittyfuck up
    pause 0.35
    show anna tittyfuck down
    "Slowly, she begins to massage my cock with her breasts, kneading them as though they actually were dough."
    "It doesn't take long for the head to emerge from between them, swollen and red from the pressure."
    "Which in turn means that all of the sensations are now concentrated in the shaft instead."
    show anna tittyfuck up
    pause 0.35
    show anna tittyfuck down
    "I can't fully describe how it feels to have Anna doing this to me right now."
    "The only thing I can compare it to would be a regular hand-job."
    "But then where could you find a hand so big and so soft?"
    show anna tittyfuck up
    pause 0.35
    show anna tittyfuck down
    "The focus of the pressure might be moving up and down the whole time."
    "Yet Anna's breasts are so large that almost all of my cock is caught between them just the same."
    show anna tittyfuck concentrate
    "And while the feeling of what she's doing to me is simply amazing, there's also the look on her face too."
    show anna tittyfuck up
    pause 0.35
    show anna tittyfuck down
    "Anna divides her attention between looking down at what she's doing and up at me."
    "One moment she's staring at the sight of my cock, jutting through her breasts."
    show anna tittyfuck normal
    "And the next she looks up and catches my eye, grinning at reactions she sees written across my face."
    show anna tittyfuck up
    pause 0.25
    show anna tittyfuck down at startle(0.05, -10)
    pause 0.25
    show anna tittyfuck up
    pause 0.25
    show anna tittyfuck down at startle(0.05, -10)
    "Suddenly I can feel a spasm travelling through my entire body."
    show anna tittyfuck up
    pause 0.25
    show anna tittyfuck down at startle(0.05, -10)
    pause 0.25
    show anna tittyfuck up
    pause 0.25
    show anna tittyfuck down at startle(0.05, -10)
    "I've been so caught up in watching Anna's face that I totally fail to notice how much she's sped up."
    show anna tittyfuck up
    pause 0.25
    show anna tittyfuck down at startle(0.05, -10)
    pause 0.25
    show anna tittyfuck up
    pause 0.25
    show anna tittyfuck down at startle(0.05, -10)
    show chest_insert anna zorder 1 at zoomAt(1, (40, 200))
    "By now she's practically working her breasts into a lather around my cock."
    show anna tittyfuck up speed
    pause 0.15
    show anna tittyfuck down at startle(0.05, -10)
    pause 0.15
    show anna tittyfuck up
    pause 0.15
    show anna tittyfuck down at startle(0.05, -10)
    pause 0.15
    show anna tittyfuck -speed
    "And the spasm that I just felt is the first hint that I'm about to cum."
    show anna tittyfuck up speed concentrate
    pause 0.15
    show anna tittyfuck down at startle(0.05, -10)
    pause 0.15
    show anna tittyfuck up
    pause 0.15
    show anna tittyfuck down at startle(0.05, -10)
    pause 0.15
    show anna tittyfuck -speed
    "Before I can speak a single word to warn Anna, I realise that it's already too late."
    show anna tittyfuck up speed
    pause 0.15
    show anna tittyfuck down at startle(0.05, -10)
    pause 0.15
    show anna tittyfuck up
    pause 0.15
    show anna tittyfuck down cum cumshot with vpunch
    pause 0.15
    show anna tittyfuck -speed
    "I thrust my cock forward, sending a surge of cum straight into her face."
    show anna tittyfuck down surprise with vpunch
    "Anna's expression goes from intense to shocked in the blink of an eye."
    "And blinking might have been a good idea for her in the same moment."
    "Not to mention keeping her mouth shut as well."
    show chest_insert anna cum
    show anna tittyfuck down cum face
    with vpunch
    "Instead she lays there, wide-eyed and with an open mouth as the streamers splatter over her."
    show anna tittyfuck normal cum face -cumshot
    "But then her surprise seems to fade, and she smiles broadly before bursting into a fit of giggles."
    mike.say "Ah..."
    mike.say "Sorry, Anna!"
    "Anna cocks her head on one side, still grinning up at me through a mask of cum."
    "She's still working away at my cock as she does so, as if determined to milk it dry."
    anna.say "You ever see those skits where someone looks down a hose-pipe for the water?"
    anna.say "I think I knew what I was gonna get when I agreed to this!"
    hide chest_insert
    $ anna.sub += 1
    return

label anna_fuck_date_missionary(sexperience_min):
    $ game.play_music("music/roa_music/city_nights.ogg")
    "Anna looks at me with naked anticipation in her eyes, and I know she's imagining what's coming next."
    "She's literally placed herself in my power and seems happy to wait and see what I choose to do with her."
    "But now that I come to it - what am I going to do with her?"
    menu:
        "Fuck her ass":
            "Normally I might think twice before beating a path to a girl's ass at a moment like this."
            "But I think I know Anna well enough by now to be wise to most of those little quirks that she has in the bedroom."
            "Where most girls might need to be persuaded to take it that way, she needs no such convincing."
            show anna missionary with fade
            "I watch Anna's reaction as she feels the head of my cock brush past the lips of her pussy and keep going."
            "Her face becomes a picture of excitement and anticipation, and she's already doing all she can to make herself open to me."
            show anna missionary lookup anal
            anna.say "Oh, [hero.name], how ever did you know?"
            "She says with an amused irony in her voice, raising her eyebrows in mock surprise."
            anna.say "With this anal, you're really spoiling me!"
            "By then my cock is just starting to push its way into Anna's ass, persuading the muscles as it goes."
            "The feeling is incredible, as her body yields to me a little at a time."
            show anna missionary pleasure
            "And the experience is made all the more enjoyable by the way in which Anna's face betrays her own pleasure at the same time."
            "The amusement fades from her features, replaced with ever more intense arousal."
            "And she seems to melt almost into a state of oblivion just as her muscles do the same, allowing me to push all the way inside."
            "Anna doesn't speak another word from that moment on, as if she's unable to do anything but lay back and take it."
            "I feel the soft cushion of her breasts against my chest and the warmth of her thighs as she wraps them around me."
            "Instead of words, Anna now speaks through sighs and moans."
            "She clings on to me, pulling me in as close as possible and riding me for every moment that I'm inside of her."
            "From all of the details I'm providing of how much Anna's getting off on this, it might sound like she's the only one that is."
            "But believe me, that's not the case at all!"
            "There's nothing worse than anal when the girl's not into it, and nothing quite as good when she is!"
            "The tightness of Anna's ass feels incredible around my cock."
            "And she seems to have an endless appetite for it pushing ever further up her."
            "I honestly wonder how far I could end up going if my cock kept growing to match her desire for it."
            "But as bottomless as Anna's need for me to be deep in her ass might be, I can't go on forever."
            "The way her muscles are squeezing the shaft means that I can't hold back from cumming any longer."
            call cum_reaction (anna, 'anal', sexperience_min) from _call_cum_reaction_19
            if _return == 'anal_inside':
                "I can't think of any good reason to stop what I'm doing right now."
                show anna missionary creampie with hpunch
                "And so I push on until the very moment that I finally cum."
                show anna missionary ahegao with hpunch
                $ anna.sub += 4
                $ anna.love += 4
                "Anna clings to me the whole time, riding me to the very last."
                "We stay like that, as my manhood dwindles back down and slips slowly out of her once more."
            elif _return == 'anal_outside':
                show chest_insert anna zorder 1 at zoomAt(1, (440, 40))
                show belly_insert anna zorder 2 at zoomAt(1, (0, 380))
                show anna missionary -anal lookup
                "As I go to pull myself out of Anna's ass, I almost expect her to hold me in there and not let me go."
                "But I manage to free my cock as gently as possible, seeing the look of disappointment on her face as I do so."
                show chest_insert anna cum
                show belly_insert anna cum
                show anna missionary cumshot pleasure
                with hpunch
                "Her mood picks up a couple of seconds later, when my bobbing cock shoots its load across her belly and then over her breasts."
                show anna missionary cum onbody -cumshot dickcum with hpunch
                $ anna.sub += 5
                $ anna.love += 3
                anna.say "Eww - [hero.name]!"
                anna.say "You dirty boy!"
                "Anna smiles up at me, the happiness she's feeling more than a little infectious."
                hide chest_insert
                hide belly_insert
            $ anna.flags.anal += 1
        "Fuck her pussy" if hero.sexperience >= (sexperience_min + 5):
            show anna missionary
            call check_condom_usage (anna) from _call_check_condom_usage_9
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show anna missionary condom
            "I pull Anna closer to me, making sure that she can feel just how much of an effect she's having on me down there already."
            "She starts to giggle and twist as the head of my cock brushes against the inside of her thighs, trying to sneak closer the whole time."
            "I know just how much of an appetite Anna has for anal, and I have every intention of making for her ass."
            "But on the way there, something happens to divert me and make sure that she won't be getting that particular fetish indulged tonight."
            "I don't know if I misjudge the exact angle of my approach, or Anna just happens to move at precisely the wrong moment."
            "Either way, the head of my cock presses against the lips of her pussy and with the right amount of pressure too."
            "As she's already more than a little slick down there and rather excited, there's little to keep the inevitable from happening."
            show anna missionary lookup vaginal
            "Before I know where I am, my cock has slipped inside of Anna, and I'm already sliding all the way up to my balls in her."
            "She cries out in surprise, but not disappointment, writhing on the bed beneath me."
            "Somehow the thought that she's been taken so quickly and without warning makes me want her this way all the more."
            "And before she can even think of objecting, I begin to quicken my pace, thrusting in and out of her with ever more enthusiasm."
            "While Anna might be more than partial to taking it up the ass, she's not adverse to being fucked in the pussy by any means."
            "So it doesn't take long for her to feel the same kind of sensations that I'm feeling right now."
            "I sense Anna surrendering to my attentions, allowing her weight to fall back onto the pillows behind her."
            "And this only makes me redouble my efforts, pressing down on her and using all of my own weight to add to what she's feeling."
            show anna missionary pleasure
            "Anna's cries of surprise are soon replaced with a low and quiet moan of pleasure."
            "She makes no effort to move as much as a single muscle, simply allowing me to have my way with her."
            "Now that I'm laid atop of her body, I can feel her large breasts pressing against my chest."
            "In the same way, her thighs are under my own legs, soft and yielding."
            "She's so comfortable to lay on, and almost as passive as a doll right now."
            "And yet my cock is still thrusting in and out of her with enough urgency to make me sweat profusely."
            "But no matter what I have to give, Anna's body simply soaks it up like a sponge."
            "At this stage, I honestly don't know if she's given herself up to me, or else has fallen into a stupor."
            "I guess that, in the heat of the moment, it hardly matters all that much."
            "And yet, even with so much desire for her and so much to give, I can't go on like this forever..."
            call cum_reaction (anna , 'vaginal', sexperience_min, check_sub=True) from _call_cum_reaction_20
            if _return == "vaginal_outside":
                "With Anna so clearly out of it right now, it falls to me to make sure there are no accidents."
                show chest_insert anna zorder 1 at zoomAt(1, (440, 40))
                show belly_insert anna zorder 2 at zoomAt(1, (0, 380))
                show anna missionary -vaginal lookup
                "At the last moment I can safely manage it, I pull out of her pussy and lose myself over her belly and breasts."
                show chest_insert anna cum
                show belly_insert anna cum
                show anna missionary cumshot
                with hpunch
                "The only thing that tells me Anna's aware of me doing so is a long, disappointed sigh she lets out as I do so."
                show anna missionary cum onbody -cumshot dickcum with hpunch
                $ anna.sub += 1
                "But for all that she sounds deflated, I'm sure she'd rather that than ending up pregnant!"
                with hpunch
                "As soon as I'm done, I crawl off of Anna and collapse at her side."
                hide chest_insert
                hide belly_insert
            elif _return == "vaginal_condom":
                "I guess it's lucky for Anna that I remembered to wear protection."
                "As out of it as she is right now, I doubt she could object to be cumming inside of her if she tried."
                with hpunch
                "So I keep on pushing into her until the very last moment possible, using the momentum of my own orgasm to push towards her own."
                with hpunch
                "Anna makes a keening, animal sound as she's tipped over and into a climax."
                $ anna.love += 1
                with hpunch
                "But still she makes no effort to move, staying laid still, as if her bones had turned to jelly."
                "As soon as I'm done, I crawl off of Anna and collapse at her side."
            elif _return == "vaginal_inside_pill":
                anna.say "Don't...stop...pill..."
                "Each of the words Anna manages to blurt out come in time with me pushing into her as I'm about to cum."
                "In my haste to fuck her as hard as possible, I'd clean forgotten that she was actually on the pill!"
                show anna missionary creampie with hpunch
                $ anna.love += 2
                "As it is, I don't have time to do or say anything in response, as I lose myself and fill her a moment later."
                with hpunch
                "Anna takes all that I have to give and can only moan from that point on."
                with hpunch
                "As soon as I'm done, I crawl off of Anna and collapse at her side."
            elif _return == "vaginal_inside_pregnant":
                "I hardly need reminding of the fact that there's no danger to shooting my load inside of Anna right now."
                "After all, I am practically leaning on the curve of her rather pregnant belly."
                "If she in any way resembles a beached whale right now, then it's a particularly sexy species of aquatic mammal!"
                show anna missionary creampie with hpunch
                $ anna.love += 2
                "Anna makes no visible sign of objection as I lose myself inside of her."
                with hpunch
                "Instead she remains where she is, panting and moaning softly."
                with hpunch
                "As soon as I'm done, I crawl off of Anna and collapse at her side."
            elif _return == "vaginal_inside_sub":
                "I should really drag my cock out of Anna, before I cum inside of her."
                "But what would she actually do if I just chose to keep on going and not bother to warn her?"
                "After all, she's been happy for me to make all of the decisions up to this point."
                "Why not this one too?"
                "By now I've used up too much time thinking about it to be able to pull out anyway."
                show anna missionary creampie with hpunch
                #$ anna.impregnate()
                $ anna.sub += 5
                $ anna.love -= 5
                "And so I can only hold on tightly as I fill Anna with one final thrust."
                with hpunch
                "As she realises what's just happened, she lowers her head into the pillows, shaking it in disbelief."
            elif _return == "vaginal_inside_mad":
                "Knowing just how out of it Anna is right now, I push on beyond the point of no return."
                "By now I couldn't pull out in time even if I wanted to!"
                show anna missionary creampie with hpunch
                #$ anna.impregnate()
                "As I lose myself inside of her, Anna takes it in much the same way she has what came before."
                show anna missionary ahegao with hpunch
                $ anna.love -= 25
                "She moans and sighs in an appreciative manner, but as I finish off and finally pull out of her, the noises she's making begin to change."
                "There are words discernible now, even as she turns away from me, keeping me from seeing the expression on her face."
                anna.say "What...what have you done..."
                anna.say "You fucking asshole..."
            elif _return == "vaginal_inside_happy":
                "As out of it as Anna is right now, I'm not much better myself."
                "In fact, I'm so caught up in the moment that I don't notice how close I am to actually cumming."
                show anna missionary creampie with hpunch
                #$ anna.impregnate()
                "This means that when the time comes, I just keep right on thrusting into her with all of my remaining strength."
                show anna missionary ahegao with hpunch
                $ anna.love += 5
                "It's only afterwards, when I've filled her and begin to slide off that the truth dawns on me."
                with hpunch
                "Any second I expect Anna to wake up to what's happened too and get seriously freaked out."
                show anna missionary lookup
                "And yet instead she smiles up at me, glowing with what can only be described as happiness."
                "Sure, I'm relieved not to be in the firing line of her anger."
                "But why in the hell is she so elated to have had me cum in her like that?"
    return

label anna_fuck_date_doggy(sexperience_min):
    $ game.play_music("music/roa_music/city_nights.ogg")
    show anna a naked at center
    mike.say "You know what, Anna - I've been eyeing up your ass all night long."
    mike.say "So why don't you hop up on the bed and let me have a good look at it, huh?"
    anna.say "Okay, [hero.name], just watch me!"
    "Anna practically beams at me as she hurries to carry out my instructions."
    "Who knows, maybe being the one giving the orders and being obeyed has its advantages?"
    scene bg black
    show anna doggy eyes_pleasure with fade
    "Once she's knelt on the bed with her back to me, Anna glances over her shoulder with a nervous grin."
    "I wasn't just saying all of that stuff about her ass to get things moving."
    "She really does look phenomenal as she's standing there in front of me."
    "By now I'm no longer worrying about being the one in charge."
    "As I know what I want to do to Anna, and I also have a pretty good idea of how I want to do it to her too."
    show anna doggy mike eyes_open
    "Climbing up onto the bed behind her, I push Anna down so that she's on all fours before me."
    "She offers no resistance whatsoever, and her breathing audibly quickens as she feels me touching her for the first time tonight."
    "Pressing my groin hard against Anna's buttocks, I put my hands on her thighs and pull her back onto me."
    "My reward is a sudden gasp of surprise and an appreciative shiver spreading through her entire body."
    "It seems like Anna is more than ready to take whatever I happen to have in mind for her."
    "If I can decide just what that's going to be..."
    menu:
        "Fuck her ass":
            "Let's just say that I know what the lady loves, and I'm quite partial to a little bit of it myself."
            "Taking Anna up the ass has become almost the natural choice in the time that we've been together."
            "Her deep love of equally deep anal seems to have rubbed off on me too."
            "And I like to think that all of the experience I've gotten at it has improved my game in that area by some way."
            "So it's hardly surprising that Anna shows no sign of shock as I part her buttocks in preparation."
            "Indeed, her breathing quickens in anticipation as I push the tip of my cock into her exposed anus."
            "And if I'm well-practiced in the art of giving it up the ass, Anna's more so when it comes to actually taking it."
            show anna doggy inside eyes_close mouth_hurt
            "Her experienced sphincter almost quivers as I push in further still, offering a token show of resistance."
            "But there's no shoving match involved in the act, and Anna's ass yields slowly and smoothly to being penetrated."
            anna.say "Oh, [hero.name]..."
            show anna doggy eyes_open mouth_moan
            anna.say "Don't stop, please!"
            anna.say "I just love it when you're inside of my ass!"
            "These words come between grateful gasps and moans, all of which only add to the pleasure of what I'm doing right now."
            "While Anna's ass is well-used to being fucked, her muscles are still tight and strong enough to grip my cock like a fist."
            "It feels like the best combination of sex and a hand-job all at once."
            "But with the person giving it getting off as much as the one getting it."
            "And it's not just the feeling of actually being inside of Anna's ass that's making me hot, either."
            show anna doggy eyes_close grab
            "The harder I pound her, the more her body moves in sympathy, her heavy breasts swaying in time."
            "Seeing her naked form animated by passion in such a way would be enough to make me lose it without even laying a finger on her."
            "For all of her need to be almost lead by the hand, Anna seems to have more than enough appetite for all I can give her."
            "Soon enough I can feel my own stamina begin to wane, while she shows no sign of tiring whatsoever."
            "Sure, her position looks less energetic than mine, but it's not as passive as it seems at first sight."
            "But if she's going to put me to shame with her superior reserves of stamina, then I'm determined to go out with a bang."
            show anna doggy eyes_pleasure mouth_hurt
            "Summoning the last of my own reserves, I thrust myself into Anna's ass with renewed determination."
            "And while she absorbs all that I can give her, Anna still begins to moan loudly as the sensation of it all threatens to overwhelm her."
            call cum_reaction (anna, 'anal', sexperience_min) from _call_cum_reaction_21
            if _return == 'anal_inside':
                "From the sounds that Anna's making, even while her head is buried in the pillows, I know she's not about to speak up."
                "And I'm so much into the stride of it by now that all I want to do is go right on ploughing her ass."
                "So I do just that, and keep on thrusting into her until the very last possible moment."
                show anna doggy eyes_ahegao with hpunch
                "I have no way of knowing if she feels any difference between the thrust on which I cum and the one before it."
                show anna doggy mouth_pleasure with hpunch
                "But maybe she can feel me shooting my load and filling her back-passage a moment later."
                "Now utterly spent, I can't keep going and so begin to slow my pace as I sag forwards with exhaustion."
                "I fall back onto my own ass soon afterwards, dragging my now slack cock out from between Anna's buttocks as I go."
                "It leaves a string of semen that turns into a drip from the tip and a stream running down the inside of her thigh."
                $ anna.sub += 5
                $ anna.love += 3
            elif _return == 'anal_outside':
                show anna doggy mouth_moan outside
                "On whim, I turn all of my energies to pulling my cock out of Anna's ass the very moment before I actually cum."
                "She moans and whimpers at the sensation of this, her anus showing a similar reaction as it quivers now that it's empty."
                show anna doggy eyes_close mouth_pleasure cum with hpunch
                "Without warning, I cum and shower the same part of her body with drops of semen that make her jump and twitch."
                show anna doggy eyes_pleasure bodycum with hpunch
                "My cum also spatters across Anna's back, buttocks and thighs, running down her and towards the bed below."
                show anna doggy -cum
                "I can sense that she's disappointed by the fact that I didn't care to stay inside of her while I came."
                "But the thrill that I get from marking Anna in this way keeps me from feeling too bad about her hurt feelings."
                "It's as though I've made a statement that she's mine, and mine alone!"
                $ anna.sub += 4
                $ anna.love += 4
            $ anna.flags.anal += 1
        "Fuck her pussy" if hero.sexperience >= (sexperience_min + 5):




            $ CONDOM = False
            "I know full well just how much Anna's addicted to taking it up the ass."
            if anna.flags.anal >= 5:
                "And I should do, the sheer number of times I've indulged her in that little fetish of hers."
            "But as much fun as ploughing Anna's back passage undoubtedly is, I'm not inclined to be so kind tonight."
            "If she's not going to speak up for what she wants, then she doesn't get a say in what gets done to her either!"
            "So taking a firm grip on Anna's rounded little haunches, I pull her firmly backwards and onto my cock."
            "The angle is just right, as I feel the token resistance of her pussy's lips against the head a moment later."
            show anna doggy grab mouth_pleasure
            "Anna yelps in surprise, but this only serves to turn me on all the more."
            "As much as she might want it up the ass, her pussy has a similarly one-tracked mind too."
            "And all it wants is to have a cock shoved inside of it, and as soon as possible!"
            show anna doggy inside eyes_close mouth_hurt
            "Within mere moments, all resistance gives way, and I feel myself sink slowly into her."
            mike.say "Just wanted to remind you that your pussy's there, Anna."
            mike.say "I don't like to think of it getting rusty from lack of use!"
            "Anna's quaking by now, as the length of my cock is finally all of the way in her."
            "It feels so good to be fucking her this way, and it's made all the better by knowing she wanted it elsewhere."
            show anna doggy mouth_moan
            "I don't waste time in building up slowly now that I'm in, and begin moving swiftly almost straight away."
            "And the way that Anna angles her backside towards me, almost thrusting in my direction, shows how much it's affecting her."
            anna.say "Ahh...fuck..."
            anna.say "Yes...please..."
            show anna doggy eyes_pleasure
            anna.say "That feels...so...so good!"
            "Hearing Anna beg for more, knowing she prefers it up the ass, turns me on even more."
            "I don't know if Anna says another word before it's all over."
            "Because all I can hear is the sound of my thighs slapping against her buttocks as I pound away at her."
            "With the noises of our bodies and the meaningless sounds emerging from Anna's lips as a backdrop, I can feel myself building to a climax."
            "I don't know whether or not she's as close as I am right now."
            "But if she's not, then I can't hope to wait for Anna to catch me up!"
            call cum_reaction (anna , 'vaginal', sexperience_min, check_sub=True) from _call_cum_reaction_22
            if _return == "vaginal_outside":
                "This is usually the point where I'd be forgetting that I've not bothered to use a condom, with hilarious consequences."
                "But the simple fact that it's a novelty to be fucking Anna in the pussy means that I'm totally aware of what's going on."
                "It feels so good that there's the obvious urge to keep on going until the final moment or beyond."
                show anna doggy mouth_pleasure outside
                "But I steel myself and pull out just in time to lose myself over Anna's quivering ass instead."
                show anna doggy cum with hpunch
                "She yelps at the feeling of my cock being suddenly whipped out of her, and then again as she's showered in semen."
                show anna doggy bodycum mouth_smile with hpunch
                $ anna.sub += 1
                "It spatters over her buttocks and runs down the back of her thighs as the sound of our panting fills the room."
            elif _return == "vaginal_condom":
                "It's at times like this that I'm glad to be a cautious guy."
                "Sure, leaping on Anna without protection would have won me a couple more seconds of fun."
                "But by now I'd have been either struggling to whip my dick out of her in time or in danger of knocking her up!"
                show anna doggy eyes_close mouth_hurt with hpunch
                "Instead I can just keep right on going until the very moment that I lose it inside of her."
                show anna doggy eyes_pleasure with hpunch
                "By the time I'm done, the only things keeping Anna upright are the pillows her face is buried in."
                show anna doggy mouth_moan
                $ anna.love += 1
                "Well, that and the fact that my cock is still holding her ass in the air too!"
            elif _return == "vaginal_inside_pill":
                anna.say "Don't stop..."
                anna.say "It's okay...I'm..."
                anna.say "On the...pill...remember!"
                "I've never been so glad to hear those words as I am right now."
                "I'd kiss Anna - if I wasn't already balls deep inside of her!"
                show anna doggy mouth_hurt eyes_ahegao cum with hpunch
                $ anna.love += 2
                "I just keep right on going until the very moment that I lose it inside of her."
                show anna doggy mouth_pleasure with hpunch
                "By the time I'm done, the only things keeping Anna upright are the pillows her face is buried in."
                "Well, that and the fact that my cock is still holding her ass in the air too!"
            elif _return == "vaginal_inside_pregnant":
                "It'd be hard not to notice the size of Anna's swollen belly, or feel its weight as I go at her."
                "Along with her heavy breasts, it brushes the bedclothes as she kneels on all fours in front of me."
                "But what it means right now is that I don't have to worry about being inside of her when I cum."
                show anna doggy mouth_hurt eyes_ahegao cum with hpunch
                $ anna.love += 2
                "I just keep right on going until the very moment that I lose it inside of her."
                show anna doggy mouth_pleasure with hpunch
                "By the time I'm done, the only things keeping Anna upright are the pillows her face is buried in."
                "Well, that and the fact that my cock is still holding her ass in the air too!"
            elif _return == "vaginal_inside_sub":
                "I should really drag my cock out of Anna, before I cum inside of her."
                "But what would she actually do if I just chose to keep on going and not bother to warn her?"
                "After all, she's been happy for me to make all of the decisions up to this point."
                "Why not this one too?"
                "By now I've used up too much time thinking about it to be able to pull out anyway."
                show anna doggy mouth_hurt eyes_ahegao cum with hpunch
                $ anna.sub += 5
                $ anna.love -= 5
                #$ anna.impregnate()
                "And so I can only hold on tightly as I fill Anna with one final thrust."
                show anna doggy mouth_pleasure with hpunch
                "As she realises what's just happened, she lowers her face into the pillows, shaking her head in disbelief."
            elif _return == "vaginal_inside_mad":
                "I should have pulled out of Anna by now, but I'm so lost in the moment that I forget completely."
                "Anna too seems to have forgotten that I'm not wearing protection, and makes no protest herself."
                "Well, either that or she's totally given up any kind of responsibility and left me in charge!"
                show anna doggy mouth_hurt eyes_open cum with hpunch
                $ anna.love -= 5
                #$ anna.impregnate()
                "In the end, the result is the same - I lose myself as deep into Anna as I can possibly get."
                show anna doggy mouth_moan with hpunch
                "She moans and writhes from the pleasure of the sensation, but then her cries slowly fall silent."
                anna.say "Erm...[hero.name]...did you just?"
                anna.say "Oops!"
            elif _return == "vaginal_inside_happy":
                "I make to pull my cock out of Anna's pussy before it's too late."
                "But she instantly wriggles her ass backwards, trying to push it back in again."
                show anna doggy eyes_close
                anna.say "Uh...no...don't..."
                mike.say "Anna - what are you..."
                show anna doggy mouth_hurt eyes_ahegao cum with hpunch
                $ anna.love += 5
                #$ anna.impregnate()
                "By then it's already too late, and I can feel myself cumming."
                show anna doggy mouth_pleasure with hpunch
                "I grab hold of Anna, meaning that I fill her with my cock almost all of the way up inside of her."
                show anna doggy mouth_moan with hpunch
                "And the whole time, she rides it eagerly, making appreciative noises between panting breaths."
                "She seems pleased with the way things ended, but I don't know if I share her feelings on the matter myself..."
    return

label anna_fuck_date_cowgirl(sexperience_min):
    $ game.play_music("music/roa_music/city_nights.ogg")
    "She turns her back on me, taunting my painfully aroused cock with her ass."
    "I try to pounce on her, but she's too fast and I only manage to grab hold of her with one hand."
    "We roll on the bed until we come up with her on top, my cock just inches from all the possibilities of her ass and vagina."
    menu:
        "Fuck her ass":
            hide anna
            show anna cowgirl b anal
            with fade
            "Anna lives up to her tattoo, wasting no time in angling herself so that my cock is rubbing against her buttocks and then pressing herself down suddenly."
            "There's no pause or hesitation as I slip inside of her ass, telling me that she's done this before and knows how to handle it."
            show anna cowgirl a anal
            anna.say "Well hello, it looks like you caught me."
            "Even though her ass is spreading to take me in, her muscles are squeezing me tighter all the time."
            anna.say "Now I want you to make your little whore feel sore down there for a week!"
            show anna cowgirl b anal
            "She's riding me like a woman possessed now, the shy girl that followed me to my bedroom nowhere to be seen."
            "I can't help but believe that she's not been with a man for a long time, as having me inside of her seems to have awoken something that's taking over."
            "Whenever I can spare a hand from trying to hold on, I reach up and caress her breasts as they're hanging above me."
            mike.say "If I ever want to kill myself, Anna, promise you'll smother me with these things!"
            "She giggles frantically, and I realise that it must be a novelty to be fucking someone without breasts of their own, who finds hers so desirable."
            anna.say "Death by anal whore...that'd look so cool on your tombstone!"
            "She's panting by now, and I can sense that I'm soon going to cum."
            "It'd be nice to lie here and let her ride me to the end, but I want to change the balance, to be the one on top at the end."
            "My pace quickens, and soon she's almost yelping in time with my thrusts, arching her back in sympathy."
            show anna cowgirl cum anal with vpunch
            "Finally she wraps her legs around mine and cries out as I climax inside of her, the waves of her own orgasm already taking hold."
            with vpunch
            "I stay inside of her as she gives in and cums, enjoying the sensation of it making her twitch and twinge."
            mike.say "Worth the wait, to have a real cock back inside of you?"
            anna.say "Mmm...more like a magic wand...one that turns me into a little anal whore!"
            $ anna.sub += 5
            $ anna.love += 3
            $ anna.flags.anal += 1
        "Fuck her pussy" if hero.sexperience >= (sexperience_min + 5):
            call check_condom_usage (anna) from _call_check_condom_usage_11
            if _return == False:
                return "leave_without_gain"
            hide anna
            if CONDOM:
                show anna cowgirl vaginal condom
            else:
                show anna cowgirl vaginal
            with fade
            "Anna throws me a curve ball by angling herself forward so that my cock rubs against her clit and then begins to push inside."
            "She feels tight and it seems like an age as she sinks down onto me, but that only makes it all the more incredible, almost like it's her first time."
            mike.say "Anna...I...I thought you wanted it in your ass!"
            anna.say "Ahh, fuck...it's been so long, since I had a real cock inside of me...couldn't help myself."
            "She's squeezing me so tight already, and knowing she's so desperate for my cock just makes it more intense."
            $ anna.love += 2
            if hero.sexperience >= 15 or "anal_beads" in hero.inventory:
                menu:
                    "Finger her ass" if hero.sexperience >= 15:
                        show anna cowgirl a finger
                        mike.say "No reason for me to let you miss out on what you love."
                        "I slide my fingers between her legs, using the slickness of her own skin to slip two digits up her ass."
                        "Anna moans as she's penetrated from two different angles, moving in either direction only making the sensation of both more intense."
                        $ anna.sub += 1
                    "Use anal beads" if "anal_beads" in hero.inventory:
                        show anna cowgirl a beads
                        mike.say "Oh fuck, Anna...that's amazing...but what about your ass?"
                        "She smiles wickedly, clearly enjoying being in control."
                        anna.say "I already thought ahead...give me your hand."
                        "She guides one of my hands under her, where I can feel something hanging below her ass, it feels like anal beads, she must have found them in the drawer..."
                        "Anna's smile turns into a grin, and she nods as I take hold and pull."
                        anna.say "Oh shit, [hero.name]...oh yes...pull my cord, pull this little whore's cord right out of her ass!"
                        $ anna.sub += 3
            show anna cowgirl b
            "She's riding me like a woman possessed now, the shy girl that followed me to my bedroom nowhere to be seen."
            "I can't help but believe that she's not been with a man for a long time, as having me inside of her seems to have awoken something that's taking over."
            "Whenever I can spare a hand from trying to hold on, I reach up and caress her breasts as they're hanging above me."
            mike.say "If I ever want to kill myself, Anna, promise you'll smother me with these things!"
            "She giggles frantically, and I realise that it must be a novelty to be fucking someone without breasts of their own, who finds hers so desirable."
            anna.say "Death by anal whore...that'd look so cool on your tombstone!"
            "She's panting by now, and I can sense that I'm soon going to cum."
            "It'd be nice to lie here and let her ride me to the end, but I want to change the balance, to be the one on top at the end."
            "My pace quickens, and soon she's almost yelping in time with my thrusts, arching her back in sympathy."
            call cum_reaction (anna, 'vaginal', sexperience_min) from _call_cum_reaction_23
            if _return == "vaginal_outside":
                "This is usually the point where I'd be forgetting that I've not bothered to use a condom, with hilarious consequences."
                "But the simple fact that it's a novelty to be fucking Anna in the pussy means that I'm totally aware of what's going on."
                "It feels so good that there's the obvious urge to keep on going until the final moment or beyond."
                show anna cowgirl out
                "But I steel myself and pull out just in time to lose myself over Anna's back instead."
                show anna cowgirl cum with vpunch
                "She yelps at the feeling of my cock being suddenly whipped out of her, and then again as she's showered in semen."

                with vpunch
                "It spatters over her buttocks and runs down the back of her thighs as the sound of our panting fills the room."
                $ anna.sub += 1
            elif _return == "vaginal_condom":
                "It's at times like this that I'm glad to be a cautious guy."
                "Sure, leaping on Anna without protection would have won me a couple more seconds of fun."
                "But by now I'd have been either struggling to whip my dick out of her in time or in danger of knocking her up!"
                show anna cowgirl cum vaginal with vpunch
                "Instead I can just keep right on going until the very moment that I lose it inside of her."
                $ anna.love += 1
            elif _return == "vaginal_inside_pill":
                anna.say "Don't stop..."
                anna.say "It's okay...I'm..."
                anna.say "On the...pill...remember!"
                "I've never been so glad to hear those words as I am right now."
                "I'd kiss Anna - if I wasn't already balls deep inside of her!"
                show anna cowgirl cum vaginal with vpunch
                "I just keep right on going until the very moment that I lose it inside of her."
                $ anna.love += 2
                with vpunch
                "By the time I'm done, the only things keeping Anna upright are my hand squeezing her tits."
                "Well, that and the fact that my cock is still holding her ass in the air too!"
            elif _return == "vaginal_inside_pregnant":
                "It'd be hard not to notice the size of Anna's swollen belly, or feel its weight as I go at her."
                "Along with her heavy breasts, it jumps up and down as she bounce on my cock."
                "But what it means right now is that I don't have to worry about being inside of her when I cum."
                show anna cowgirl cum vaginal with vpunch
                "I just keep right on going until the very moment that I lose it inside of her."
                $ anna.love += 2
                with vpunch
                "By the time I'm done, the only things keeping Anna upright are my hand squeezing her tits."
                "Well, that and the fact that my cock is still holding her ass in the air too!"
            elif _return == "vaginal_inside_sub":
                "I should really drag my cock out of Anna, before I cum inside of her."
                "But what would she actually do if I just chose to keep on going and not bother to warn her?"
                "After all, she's been happy for me to make all of the decisions up to this point."
                "Why not this one too?"
                "By now I've used up too much time thinking about it to be able to pull out anyway."
                show anna cowgirl cum vaginal with vpunch
                "And so I can only hold on tightly as I fill Anna with one final thrust."
                #$ anna.impregnate()
                with vpunch
                "As she realises what's just happened, she lowers her face over my shoulder, shaking her head in disbelief."
                $ anna.sub += 5
                $ anna.love -= 5
            elif _return == "vaginal_inside_mad":
                "Anna's out of it right now, and so am I."
                "This means that neither of us realise we've gone beyond the point of no return."
                "By now I couldn't pull out in time even if I remembered to!"
                show anna cowgirl cum vaginal with vpunch
                "As I lose myself inside of her, Anna takes it in much the same way she has what came before."
                with vpunch
                "She moans and sighs in an appreciative manner, but as I finish off and finally pull out of her, the noises she's making begin to change."
                #$ anna.impregnate()
                "There are words discernible now, even as she turns away from me, keeping me from seeing the expression on her face."
                anna.say "What...what have we done..."
                anna.say "Oh shit...what if I get pregnant from this?!?"
                $ anna.love -= 5
            elif _return == "vaginal_inside_happy":
                "I make to pull my cock out of Anna's pussy before it's too late."
                "But she instantly wriggles her ass downwards, trying to push it back in again."
                anna.say "Uh...no...don't..."
                mike.say "Anna - what are you..."
                show anna cowgirl cum vaginal with vpunch
                "By then it's already too late, and I can feel myself cumming."
                #$ anna.impregnate()
                with vpunch
                "I grab hold of Anna, meaning that I fill her with my cock almost all of the way up inside of her."
                "And the whole time, she rides it eagerly, making appreciative noises between panting breaths."
                "She seems pleased with the way things ended, but I don't know if I share her feelings on the matter myself..."
                $ anna.love += 5
    return

label anna_fuck_date_blowjob:
    scene anna blowjob with fade
    "Anna takes a firm hold of my cock a moment later."
    "She doesn't squeeze me hard enough to make it hurt."
    "But I'm under no illusions, I know she's not going to let go anytime soon!"
    "Anna lies down on her back, my cock over her face."
    "Then she opens her mouth, and her tongue goes to work."
    "Anna's left me in an odd position, kneeling over her and to the side."
    "But there's no way I'm going to ask her to stop so I can move a couple of inches."
    "Instead I brace myself with one arm and give her as much help as I can."
    "Though it's hard to think about anything like that while she's licking my cock!"
    "Seriously, the feeling is incredible."
    "Instinctively, I lean further forwards."
    "And in an instant, Anna takes full advantage."
    "Her lips close around the head, and she takes it into her mouth."
    show anna blowjob suck
    "Now things are getting really intense for me."
    "Anna's working the entire thing, head bobbing up and down."
    "Fully half my cock must be in her mouth most of the time."
    "I want to give her as much help as I can."
    "So I reach out with my free arm, trying to brace myself better."
    "But instead, my hand comes down squarely between Anna's thighs."
    "Believe me, I wasn't aiming for her pussy."
    "But that's exactly where my hand ends up!"
    "And the moment my fingers brush Anna's lips, she moans with pleasure."
    "Well, when I say she moans, what I mean is she mumbles around my cock!"
    "Though I'm sure it would have been a moan if she hadn't had a mouthful..."
    "Anyway, I feel my fingers sliding over Anna's wet folds."
    "She's putting so much effort in on my part right now."
    "She's giving me so much pleasure."
    "What kind of a gentleman would I be if I didn't return the favour?"
    "I start stroking Anna's pussy."
    "I go slow at first, to gauge her reaction."
    "But all it takes is a couple of passes for the effects to be visible."
    "Anna quivers under my touch, and she nods her head as best she can."
    "I take this as a cue to keep going, to give her more."
    "Soon enough, my fingers are creeping deeper into her pussy."
    "They inch inside of her as she opens up to me."
    "At the same time, I seem to be fuelling Anna's efforts too."
    "The more I pleasure her, the harder she works to do the same for me."
    "Before too long, it's hard to tell who's pushing who onwards."
    "We seem to be keeping each other going in an endless cycle."
    "But that's obviously just the way it feels."
    "Because all too soon, I can feel myself reaching the end."
    "I'm going to cum, and it's going to happen soon!"
    menu:
        "Cum in her mouth":
            show mouth_insert anna zorder 1 at zoomAt(1, (840, 160))
            "There's no way I'm pulling out of Anna's mouth now."
            "I just have to take the gamble that she's ready for it."
            "So at the very last moment, I keep right on going."
            show mouth_insert anna cum
            show anna blowjob creampie cum
            with hpunch
            "Which means I shoot my load while deep in Anna's mouth."
            with hpunch
            "Her eyes pop open and she begins to gag."
            with hpunch
            "And for a moment I actually think she's going to choke."
            show mouth_insert anna -cum
            "But then she regains control, swallowing like a pro."
            "In the end, Anna handles everything I have to give."
            hide mouth_insert
            $ anna.sub += 1
        "Cum on her face":
            "I can't be sure that Anna's ready for me to cum in her mouth."
            show anna blowjob -suck
            "So I make sure to pull my cock out of her mouth before it happens."
            "This takes her by surprise, her eyes popping open."
            "But there's no time for her to ask any questions."
            show anna blowjob cumshot with hpunch
            "Because a moment later I shoot my load straight into her face."
            with hpunch
            "Sticky streamers of warm, white cum paint stripes on Anna's cheeks."
            with hpunch
            "The stuff drips from the tip of her nose and chin."
            "Some even lands on her tongue, and she swallows it helplessly."
            $ anna.love += 2
    "Finally I collapse backwards onto the bed, panting with exhaustion."
    "Anna rolls onto her belly and crawls over to lay beside me."
    "She nestles herself into my side, stroking my now drooping cock."
    "Neither of us seems to feel the need to say anything."
    "Because what we just did speaks louder than words."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
