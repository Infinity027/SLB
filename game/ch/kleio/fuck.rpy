init python:
    Event(**{
    "name": "kleio_hottub_sex_male",
    "label": "kleio_hottub_sex_male",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("date_hot_tub_home")),
        PersonTarget(kleio,
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

    Event(**{
    "name": "kleio_garage_fuck",
    "priority": 500,
    "label": "kleio_garage_fuck",
    "duration": 1,
    "conditions": [
        IsDone("kleio_event_05b"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsRoom("garage"),
            ),
        PersonTarget(kleio,
            Not(IsHidden()),
            IsRoom("garage"),
            MinStat("love", 120),
            ),
        ],
    "music": "music/roa_music/horizon.ogg",
    "do_once": False,
    "once_month": True,
    })

    Event(**{
    "name": "kleio_studio_bj",
    "priority": 500,
    "label": "kleio_studio_bj",
    "duration": 1,
    "conditions": [
        IsDone("kleio_fuck_date_bj"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsRoom("studio"),
            ),
        PersonTarget(kleio,
            Not(IsHidden()),
            IsRoom("studio"),
            MinStat("love", 160),
            ),
        ],
    "music": "music/roa_music/horizon.ogg",
    "do_once": False,
    "once_month": True,
    })


label kleio_hottub_sex_male:
    $ game.active_date.clothes = "swimsuit"
    $ CONDOM = False
    show bg pool
    "When I asked Kleio over to take a dip in the hot-tub, I tried to make it sound innocent."
    "You know, like it was just a chance to relax and hang out?"
    "Just the kind of hanging out that would need the both of us to be half-naked."
    "Well, half-naked and sitting in warm, bubbling water too!"
    "It's not like Kleio's a killjoy, you know?"
    "She's up for fun as much as the next girl."
    "It's just that she can be...well, spikey at times."
    "And she loves to tease me when it comes to my manly need too!"
    "I guess that's part of why she agrees to come over."
    show kleio swimsuit with dissolve
    "It's also probably why she's standing by the edge of the tub right now."
    "Just standing there and letting my eyes take in the sight of her in that swimsuit."
    "A large part of me is glad that a part of me that's getting larger is under the water!"
    kleio.say "Why are you looking at me like that, Loverboy?"
    mike.say "Ah..."
    mike.say "Like what, Kleio?"
    kleio.say "Like you're dying of thirst and I'm a glass of water!"
    mike.say "I...I don't know what you mean, Kleio!"
    mike.say "I'm just happy we're getting the chance to hang out together, that's all."
    "I can't help swallowing after I say this."
    "Who am I trying to kid?"
    "Kleio looks straight up amazing, just standing there in her swimsuit."
    "It shows off every inch of her sexy, petite little body so well."
    "I'm almost panting at the thought of getting my hands on her."
    "And the worst thing is that she knows it too!"
    "Kleio shrugs and lets out a little chuckle."
    kleio.say "Okay, Loverboy."
    kleio.say "Whatever you say..."
    hide kleio
    show hottub kleio
    with fade
    "And with that, she climbs into the tub beside me."
    "Kleio sighs as she lowers herself into the warm, bubbling water."
    kleio.say "Mmm..."
    kleio.say "That feels really good."
    kleio.say "It's like someone's touching me all over."
    kleio.say "Caressing every inch of my body..."
    mike.say "Ah..."
    mike.say "Mmm..."
    mike.say "Stop it, Kleio!"
    "At this, Kleio looks me straight in the eye."
    "She has an exaggerated expression on her face."
    "Mock innocence oozing out of every pore."
    kleio.say "Why, whatever's the matter, Loverboy?"
    kleio.say "Did the water just get too hot for you?"
    mike.say "Aww..."
    mike.say "Stop it, Kleio!"
    mike.say "Okay, I admit it - all I can think about is fucking you right now!"
    mike.say "There, I said it."
    mike.say "Are you happy now?"
    "The expression on Kleio's face becomes amused and knowing."
    "But the smile spreading across it is warm and reassuring."
    kleio.say "Oh, Loverboy!"
    kleio.say "All you had to be was honest..."
    "Kleio snakes through the water, wrapping herself around me."
    "She hugs me then, making sure there's no space between us."
    kleio.say "Because that's what I want too!"
    kleio.say "So let's quit beating around the bush, huh?"
    kleio.say "Then we can get your cock inside of me!"
    "Kleio raises her eyebrows in the most suggestive manner."
    "And I can feel her hand as it reaches inside of my trunks to squeeze my dick."
    "Happy that we've managed to get past the stage of playing games, I hurry to obey."
    "Kleio chuckles to herself as I desperately tug down my trunks."
    "But I see her eyes go wide and the chuckle almost become a growl a moment later."
    "And it can't help but make me all the more eager to my hands on her."
    "All thought of the previous awkwardness seems to vanish as we get down to it."
    "Now the only thing that I can think of is Kleio."
    show hottub sex male kleio outside with fade
    call kleio_dick_reactions from _call_kleio_dick_reactions
    "She leans forwards, pushing her ass into my lap."
    "And I don't need to be told what needs to happen next."
    "The sensation of my cock against her pussy is almost too much to bear."
    show hottub sex male kleio inside
    "But when it finally begins to push inside, the feeling of release is incredible."
    "Kleio seems to be in the exact same place as me too."
    "As she gasps more with each inch that sinks into her!"
    "She looks over her shoulder at me, mouth open and eyes wide."
    "And she nods the whole time, urging me on until I can't go any deeper."
    "I stay still for a moment, and then start to move slowly back and forth."
    "Kleio moves in sympathy too, breasts swaying as she does so."
    "But it's almost impossible to keep from picking up speed."
    "That means it's not long before I'm slapping my thighs against Kleio's."
    "She yelps and squeals the whole time, unable to keep quiet."
    "And I hear myself making deeper sounds too, panting and groaning."
    kleio.say "Oh...my...god!"
    kleio.say "You're making me cum..."
    kleio.say "Please...don't...stop!"
    "Kleio's words are like a magic spell that takes an instant hold of me."
    "The mere mention of how close she is to her climax pushes me over the edge too!"
    menu:
        "Cum inside":
            "There's no way I can stop it now, I'm already losing it."
            show hottub sex male kleio cumshot with hpunch
            $ kleio.love += 1
            "I feel myself shooting my load into Kleio, as deep as it can go."
            show hottub sex male kleio ahegao with hpunch
            "She loses the power of speech in that moment, making animal sounds instead."
            with hpunch
            "And I just manage to catch her before she collapses, face first, into the water."
        "Cum outside":
            show hottub sex male kleio outside
            "I pull back at the very last moment, enough to make my cock pop out of Kleio."
            "She makes an almost desperate animal sound as it slides out."
            "But the sensation is more than enough to finish her off."
            $ kleio.sub += 1
            show hottub sex male kleio cumshot with hpunch
            "And Kleio surrenders to her orgasm as I shoot my load over her."
            with hpunch
            "It splashes down across her back, buttocks and thighs."
    "Kleio lays her back against my chest as we bask in the afterglow."
    "And I know that she's well and truly satisfied for one reason above all."
    "Which is the fact that she's content to snuggle against me in complete silence."
    "And so I simply enjoy the moment, and the sensation of her head upon my shoulder."
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ kleio.sexperience += 1
    $ game.active_date.clothes = None
    return

label kleio_fuck_date_male(location="hero"):
    $ game.play_music("music/roa_music/city_nights.ogg")
    scene bg bedroom1
    $ game.room = "bedroom1"


    call kleio_fuck_date_intro_male (location) from _call_kleio_fuck_date_intro


    call kleio_dick_reactions from _call_kleio_dick_reactions_2


    if hero.sexperience >= 20:
        call kleio_fuck_date_foreplay_male from _call_kleio_fuck_date_foreplay_male
    if kleio.sub >= 25 and ("kleio_fuck_date_bj" not in DONE or hero.sexperience < 20):
        call kleio_fuck_date_bj from _call_kleio_fuck_date_bj

    call handle_npc_leaving (kleio, _return, from_foreplay=True) from _call_handle_npc_leaving_10
    if _return:
        return



    call kleio_fuck_date_choices_male from _call_kleio_fuck_date_choose


    call handle_npc_leaving (kleio, _return) from _call_handle_npc_leaving_11
    if _return:
        return


    scene bg bedroom1
    show kleio naked
    "Neither of us speaks as we lie still and feel our bodies quickly cooling and becoming chilly where we were so recently burning with heat."
    "I can't help feeling reassured by the feeling of Kleio's back against my stomach and her buttocks nestled in my lap."
    "Part of me wonders if I'm actually getting to know and understand her with the time we're spending together."
    "While another wonders if all I'm doing is uncovering more mysteries in her complicated and yet compelling personality."
    call kleio_sleep_date_fuck (location) from _call_kleio_sleep_date_fuck_2
    $ game.room = "bedroom1"
    return

label kleio_fuck_date_intro_male(location="hero"):
    $ game.play_music("music/roa_music/city_nights.ogg")
    show kleio
    if kleio.sub >= 75 and kleio.sexperience:
        "I open the door to my bedroom, leading Kleio by the hand until she's over the threshold and then giving her a sharp tap on the backside."
        "Caught unawares, she yelps and leaps a little way into the air, but runs the rest of the way into the room at the same time."
        "When she reaches the side of the bed, she stops and turns around slowly to regard me, her eyes full of anticipation for what comes next."
        "For all of her apparent enthusiasm, Kleio doesn't say a word her body language tells me she's not even thinking of making the first move."
        "Sometimes it strikes me just how much she's changed from the feisty, even aggressive girl that I first met all those months before."
        "But all the same, she seems perfectly happy with the way things have come to be between us."
        "And if that's not the case, I can hardly be blamed for her being too submissive to say so, now can I?"
        mike.say "Take your clothes off, Kleio."
        show kleio naked blush with dissolve
        "At this, Kleio nods obediently, beginning to hastily tug at what she's wearing."
        mike.say "But don't be too hasty about it, okay?"
        kleio.say "Erm...yeah, okay."
        kleio.say "I'm sorry..."
        "This stops Kleio in her tracks, and she nods, looking as though she's afraid to have done wrong."
        "The look of trepidation doesn't quite leave her face as she starts to pull her clothes off with less speed."
        "And though I'm more pleased with the new pace she's adopted, I don't hurry to disabuse her of her notion I'm a little unhappy."
        "It's sometimes good to let her feel a tiny bit on edge, as though she has to work harder than ever to try to win her way back into my affections."
        "Once she's finished stripping and stands before me naked, I see Kleio make a move to cover herself with her hands."
        "A slight shake of the head on my part makes them return to her sides, and she smiles nervously the whole time."
        "I take some time to admire her naked body, excited both by the sight of her and the way in which she's so exposed."
    elif kleio.sub >= 50 and kleio.sexperience:
        "It's not exactly hard to spot that Kleio's had a good time tonight."
        "She's been upbeat all the way through our date, laughing and joking."
        "And now she's practically pulling me into me bedroom too!"
        kleio.say "Come on, Loverboy!"
        kleio.say "What are you waiting for?"
        mike.say "Whoa..."
        mike.say "Hold on there, Kleio!"
        mike.say "I'm coming as fast as I can!"
        play sound door_slam
        "The door slams behind us, meaning that we're finally alone."
        "And Kleio wastes no time in tugging and pulling at my clothes."
        "I return the favour, trying to strip her off too."
        "But all that means is we get in each other's way."
        "Kleio's hands pull at my pants while I'm tugging at her top."
        "And soon we're locked in a desperate tangle of limbs."
        kleio.say "Ah...what..."
        kleio.say "What gives, Loverboy?"
        kleio.say "I want what's inside of your damn pants!"
        kleio.say "I want it out of there and inside of me, damn it!"
        mike.say "Urgh..."
        mike.say "Me...me too, Kleio!"
        "Anybody else would stand back and get their shit together, right?"
        "But not Kleio, oh no."
        "She'd see that as an admission of defeat."
        "And as stubborn as ever, she keeps on trying until she gets what she wants."
        "Somehow I feel her hands inside of my shorts, fingers closing around my cock."
        "What follows is kind of a blur, as clothes come off and we tumble onto the bed."
        show kleio naked blush
        "But when I regain my senses, I find myself looking up at Kleio."
        "She has an almost desperate look on her face, and my cock in one hand."
        kleio.say "Mmm..."
        kleio.say "I've been thinking about this all night."
        mike.say "Y...yeah?"
        kleio.say "Oh yeah!"
        kleio.say "So you'd better fuck me good and hard, Loverboy!"
        "Kleio gives me a particularly dirty wink."
        "And she rubs my cock hard against the lips of her pussy."
        "She bites her lip as I feel just how wet she is down there."
        kleio.say "Come on, Loverboy - fuck my brains out!"
    elif kleio.sexperience:
        "I've heard guys say that they need to try doing new and crazy stuff to keep the sex from getting boring in a relationship."
        "But if that's something that'll happen to Kleio and me, then it feels like it's still a long way off from where we are right now!"
        "She has a firm hold of my hand as she drags me into the bedroom, already stripping off with her free hand."
        "Not that I need to be persuaded, following on her heels as eagerly as if this were our first time together."
        kleio.say "Come on, Loverboy."
        kleio.say "Don't think I haven't seen how you've been looking at me all night!"
        "By now she's almost finished stripping off her clothes and tossing them aside."
        show kleio naked blush with dissolve
        "She doesn't make a strip-tease of it, but somehow her tearing them off with such a purpose is a real turn-on."
        "I struggle to follow her example, almost blushing as her eyes seem to devour me the whole time."
        kleio.say "I've been looking too."
        kleio.say "And I've seen a part of you that I want inside of me - REAL bad!"
        "Well, with an invitation like that, how can I possibly refuse?"
        "I let Kleio put a hand on my chest and push me backwards onto the bed, enjoying her predatory smile as she does so."
        "With me flat on my back, she climbs slowly atop me until she comes to rest straddling my thighs."
        "I don't know how much my expression's betraying right now, but I can't hide the reaction of other parts of my body."
        "And the way that Kleio eyes me as my cock steadily stiffens at her approach only makes it go that much faster."
        kleio.say "That's it."
        "Kleio leans forward and taps the head of my penis as it's now standing to attention."
        "It bobs and nods in reaction to the touch, making her giggle and sending a shudder running through me at the same time."
        kleio.say "That's what I want inside of me..."
        "At this, she leans in even closer and kisses me deeply."
        "I can feel her tongue on my lips, her breasts pressed against my chest, and the warmth between her thighs rubbing at my cock."
        "As much as I love the foreplay - as if she needs to ask for what she wants right now!"
        "It's exactly what I want too, as soon as I can get it..."
    else:
        "I open the door to my bedroom, leading Kleio by the hand until she's over the threshold and then giving her a sharp tap on the backside."
        "Caught unawares, she yelps and leaps a little way into the air, but runs the rest of the way into the room at the same time."
        "A moment later and I swear she'd have made me do her, right there and then in the hallway."
        "She points at my already rising cock as she pulls off her own jacket and t-shirt, then unhooks her bra."
        show kleio naked with dissolve
        "It takes her no time at all to yank off the rest of her clothes, and then she parts my legs and kneels on the floor in front of me."
    call kleio_dick_reactions from _call_kleio_dick_reactions_1
    return

label kleio_fuck_date_foreplay_male:
    menu:
        "Go down on her":
            call kleio_fuck_date_cunni from _call_kleio_fuck_date_cunni
        "Let her go down on me" if "kleio_fuck_date_bj" in DONE:
            call kleio_fuck_date_bj from _call_kleio_fuck_date_bj_1
        "Skip":
            return
    call stop_all_sfx from _call_stop_all_sfx_19

    return _return

label kleio_fuck_date_choices_male:
    $ game.play_music("music/roa_music/city_nights.ogg")
    if randint(1, 2) == 1:
        "I can hear Kleio panting in anticipation, and I must be doing the same."
        "Then it occurs to me that she's wide open and willing me to take her."
        "But where am I going to put it?"
    else:
        "Kleio laughs in a wonderfully filthy manner as I try to maneuver her into the position that I have in mind."
        "She makes a show of resisting a little, pretending to snap and bite at me, but soon submits herself to being bent in the way I want."
    menu:
        "Missionary":
            hide kleio
            call kleio_fuck_date_missionary (0) from _call_kleio_fuck_date_missionary
        "Cowgirl" if kleio.sub < 75 and hero.sexperience >= 5:
            hide kleio
            call kleio_fuck_date_cowgirl (5) from _call_kleio_fuck_date_cowgirl
        "Cowgirl" if kleio.sub >= 75 and hero.sexperience >= 5:
            hide kleio
            call kleio_fuck_date_cowgirl2 (5) from _call_kleio_fuck_date_cowgirl2
        "Doggy" if kleio.sub < 75 and hero.sexperience >= 10:
            hide kleio
            call kleio_fuck_date_doggy2 (10) from _call_kleio_fuck_date_doggy2
        "Doggy" if kleio.sub >= 75 and hero.sexperience >= 10:
            hide kleio
            call kleio_fuck_date_doggy (10) from _call_kleio_fuck_date_doggy
    call stop_all_sfx from _call_stop_all_sfx_20

    return _return


label kleio_fuck_date_cunni:
    "She stands there, rubbing the edges of her neat little pussy for a few brief seconds."
    "And then she makes a show of sauntering over to the bed."
    show kleio cunnilingus with fade
    "Kleio glances back over her shoulder and she sits down on the mattress."
    "With the one hand still on her lower lips, she beckons to me with the other."
    "The sight of it is enough to get me hard as I walk towards her."
    "But the truth is that Kleio really doesn't need to try so hard."
    "I'd have done what she wants anyway, without complaint."
    "Hell, I'd even have paid for the privilege!"
    show kleio cunnilingus lick
    "I don't say another word, just lower my head between Kleio's open thighs."
    "I can smell the scent of her already, luring me in."
    "My tongue finds the edges of her lips, the stubble where she's shaved down there."
    "And once I get a taste of her, there's no turning back..."
    menu:
        "Use my tongue":
            show kleio cunnilingus pleasure
            "Kleio reacts almost the second that my tongue begins to stroke the folds of her pussy."
            "She makes a sound that reminds me of nothing more than a cat, purring happily."
            "And it serves to spur me on with what I'm doing, knowing that she's getting off on it."
            show kleio cunnilingus normal
            "Not that this is only fun for her."
            "I wasn't kidding when I said that Kleio's pussy is neat."
            "In fact, it's pretty much a work of art."
            "All I can compare it to is a little flower between her thighs."
            "One that has an intoxicating scent and petals that open before my tongue."
            "I wonder if this is how a bee feels, as it buries into a flower in search of nectar."
            "I wonder if the stuff tastes as sweet as the juices coming out of Kleio's pussy."
            show kleio cunnilingus pleasure
            "My tongue goes deeper still, making her begin to pant and gasp."
            "The sound alone is enough to make me explore all that I can."
            "And pretty soon I'm probing the inside walls with the tip of my tongue."
            "All the while I can feel Kleio as she bucks and twitches above me."
            "Her thighs wrap around my head, as if she's afraid to let me go before it's done."
            "Finally, I don't think I can get anything more out of my tongue."
            "Not depth or stamina - it's actually beginning to feel numb."
        "Finger her ass" if hero.sexperience >= 30:
            show kleio cunnilingus pleasure
            "Kleio's into it almost the same moment that I begin to lick at her pussy."
            "She's moaning and cooing so much that I'm sure she's pretty distracted."
            "That makes slipping a hand under one of her buttocks an easy task."
            "I keep right on enjoying the taste and texture on my tongue for a few moments."
            show kleio cunnilingus alone
            "And then I give Kleio's pert little buttock a good, firm squeeze."
            kleio.say "Ooh..."
            kleio.say "What are you..."
            "I already have one finger in position."
            "Just waiting for the second she lowers her ass back down..."
            kleio.say "HEY!!!"
            kleio.say "What are you..."
            show kleio cunnilingus ahegao assfinger
            kleio.say "Oh...oooh...oh shit!"
            "I feel the resistance melt from Kleio's body as she sinks down and onto the finger."
            "Her muscles judder and protest, but then give way as she feel the pleasure it brings."
            show kleio cunnilingus pleasure
            "Pretty soon, Kleio's back is arched from the sensation of being worked from both angles."
            "And my finger has sunk in all the way to the knuckle too."
            "But soon I begin to wonder if this is more than I can handle."
        "Use the dildo" if hero.has_item("dildo") and hero.sexperience >= 15:
            show kleio cunnilingus pleasure
            "I know that I have Kleio completely in my power almost as soon as I get started."
            "The sounds that she's making remind me of a satisfied cat, purring away happily."
            "And I'm sure that nothing save for me actually stopping would distract her now."
            "The taste and feel of her is almost enough to draw me all the way in too."
            "But then I remember something just within reach, and grab it with one hand."
            show kleio cunnilingus alone dildo anal
            "The first thing that Kleio knows about it is when I push the dildo into her, just a little."
            kleio.say "What the hell..."
            kleio.say "That feels..."
            kleio.say "Good...it feels good!"
            "I take this as permission to follow through with my plan."
            "And so push the dildo still deeper into Kleio's ass."
            "It sinks in gradually, and she moans ever more deeply as it does so."
            "Kleio twitches and jumps as I work her with the toy."
            "The sounds that she's making now are that much more intense than before."
            "In fact, it's getting harder to keep it up the more she moves!"
        "Use the anal beads" if "anal_beads" in hero.inventory and hero.sexperience >= 15:
            show kleio cunnilingus pleasure
            "Luckily for me, Kleio's totally into it when I begin to lick at her pussy."
            "In fact, she's so engrossed in my efforts that she doesn't notice me reach under the bed."
            "My hand easily finds the string of anal beads that are hidden down there."
            "All it takes is for me to push my tongue a little deeper between Kleio's lips..."
            "She moans, her pelvis rising unconsciously as she tries to push me deeper still."
            show kleio cunnilingus alone
            "I take the chance and reach under her ass, pushing the first of the beads up there."
            kleio.say "Ugh..."
            kleio.say "Wha...what are you..."
            show kleio cunnilingus ahegao beads
            "But it's already too late for Kleio to object or stop me."
            "My working on her pussy is simply too much for her to risk spoiling right now."
            "And so she has no choice but to let me keep on stuffing the beads up her ass."
            "I can tell from the moaning sounds she makes that it's giving her pleasure, not pain."
            "And I redouble my efforts at probing between her lips, just to make sure."
            show kleio cunnilingus pleasure
            "Soon enough, Kleio's moans reach a peak and she begins to quiver all over."
            "I can sense that the perfect moment is getting closer by the second."
            "But I wait until I'm absolutely sure, and then tug the cord attached to the beads."
            "They pop out of Kleio's clenching ass one after another."
            "I swear each and every one makes her yelp out loud too."
            "The cascade of beads pushes Kleio over the edge."
            "And it also saves me from utter exhaustion too!"
        "Use dildo and my finger." if hero.has_item("dildo") and hero.sexperience >= 30:
            show kleio cunnilingus pleasure
            "Kleio's into it almost the same moment that I begin to lick at her pussy."
            "She's moaning and cooing so much that I'm sure she's pretty distracted."
            "That makes slipping a hand under one of her buttocks an easy task."
            "I keep right on enjoying the taste and texture on my tongue for a few moments."
            "And then I give Kleio's pert little buttock a good, firm squeeze."
            kleio.say "Ooh..."
            kleio.say "What are you..."
            "I already have one finger in position."
            "Just waiting for the second she lowers her ass back down..."
            kleio.say "HEY!!!"
            kleio.say "What are you..."
            show kleio cunnilingus alone ahegao assfinger two
            kleio.say "Oh...oooh...oh shit!"
            "I feel the resistance melt from Kleio's body as she sinks down and onto the finger."
            "Her muscles judder and protest, but then give way as she feel the pleasure it brings."
            show kleio cunnilingus pleasure
            "Pretty soon, Kleio's back is arched from the sensation of being worked from both angles."
            "And I'm sure that nothing save for me actually stopping would distract her now."
            "The taste and feel of her is almost enough to draw me all the way in too."
            "But then I remember something just within reach, and grab it with one hand."
            show kleio cunnilingus dildo vaginal
            "The first thing that Kleio knows about it is when I push the dildo into her, just a little."
            kleio.say "What the hell..."
            kleio.say "That feels..."
            kleio.say "Good...it feels good!"
            "I take this as permission to follow through with my plan."
            "And so push the dildo still deeper into Kleio's pussy."
            "It sinks in gradually, and she moans ever more deeply as it does so."
            "I keep on licking and probing the outer folds the whole time."
            "Kleio twitches and jumps as I work her with my tongue, finger and the toy."
            "The sounds that she's making now are that much more intense than before."
            "In fact, it's getting harder to keep it up the more she moves!"
    "But just then, the first twinges of Kleio's climax come to my aid!"
    "And when it does take hold of her, my fears are realised."
    show kleio cunnilingus ahegao
    "Kleio clamps her thighs around me like a vice!"
    "I can barely hear her yowling with release as she muffles my ears."
    "For a moment, I actually think that she's going to choke me out."
    "I fear she'll render me unconscious with the death grip she's exerting."
    show kleio cunnilingus alone pleasure -assfinger -dildo -beads
    "But then, just as quickly, Kleio's entire body goes suddenly limp."
    "She falls back onto the bed, letting me shoot up, sucking in a lungful of air."
    mike.say "Ah...ah..."
    kleio.say "Wh...what's that, Loverboy?"
    kleio.say "Are you okay?"
    mike.say "I...I think so, Kleio."
    mike.say "And you?"
    kleio.say "Oh, I'm better than okay."
    kleio.say "Thanks to that smart mouth of yours!"
    return

label kleio_fuck_date_bj:
    $ DONE["kleio_fuck_date_bj"] = game.days_played
    $ game.play_music("music/roa_music/city_nights.ogg")
    if kleio.sub < 75:
        "Kleio finally shoves me back and I fall onto the bed, stripped to the waist and with my pants halfway down my thighs."
    else:
        "Kleio submissively kneel between my legs."
    if kleio.flags.mikeNickname:
        kleio.say "Can I have that [hero.name]?"
    else:
        kleio.say "That's mine!"
    "Kleio wraps her arms around my waist and slides my cock between her petite breasts."
    "At the same time she gently kisses my stomach and eyes me in a provocative manner."
    if kleio.flags.mikeNickname:
        kleio.say "Please let me worship your dick [hero.name]."
    else:
        kleio.say "Imagine we're still out, and I'm under the table...doing this."
    hide kleio
    show kleio bj bedroom naked
    with fade
    "With that, she slides down and releases my cock from between her breasts."
    show kleio bj lick
    show mouth_insert kleio zorder 1 at zoomAt(1, (860, 140))
    "It traces its way up her neck, and then over her chin, and she doesn't even hesitate to allow it into her open mouth."
    show kleio bj suck
    "As if the feeling of Kleio, lips, tongue, piercings and all, going to work on me wasn't enough, now I can't help imagining her doing the same in public."
    show kleio bj deep
    "She takes me in deep all of a sudden, almost swallowing the entire length whilst cupping my balls and squeezing them tightly."
    "I feel myself stiffen, and realise that she's in real danger of making me cum within mere moments."
    menu:
        "Cum on her face":
            "Sensing what's about to happen, Kleio releases me and gasps for breath."
            show kleio bj lick
            hide mouth_insert
            "But it's too late, and with her face mere inches from the tip of my cock, she takes it all a second later."
            show kleio bj facial cumshot with vpunch
            "Her face is glistening with the slowly dripping semen, but she doesn't seem in the slightest bit upset."
            show kleio bj facial -cumshot dickcum with vpunch
            if kleio.flags.mikeNickname:
                kleio.say "Thank you [hero.name]."
            else:
                kleio.say "I told you it was mine...all of it."
                "Almost to emphasize the point, she licks her lips and grins wickedly."
            $ kleio.love += 1
            hide kleio bj
            scene bg bedroom1
            if not hero.fitness >= 50:
                return "leave_with_gain"
        "Cum in her mouth":
            with vpunch
            "I cup my hands behind Kleio's head, holding her down as I cum."
            show kleio bj deep cum
            show mouth_insert kleio cum
            with vpunch
            "She struggles a little at first, more thanks to surprise than objection."
            with vpunch
            "But then she resigns herself to it and rides out the thrusts of the climax, her submission making it all the more gratifying to feel."
            if kleio.is_collared:
                mike.say "Don't let a drop out little slut."
                show kleio bj suck cum
                "Kleio's breathless expression slowly turns into one of excitation, betraying the enjoyment she derives from the dirty talk."
            else:
                mike.say "It's yours, Kleio...but I get a say in how you take it from me."
                show kleio bj out cum dickcum
                "Kleio's breathless expression slowly turns into one of knowing amusement, betraying the enjoyment she derives from the occasional act of domination."
            $ kleio.sub += 1
            hide mouth_insert
            hide kleio bj
            scene bg bedroom1
            if not hero.fitness >= 50:
                return "leave_with_gain"
        "Stop before cumming" if hero.sexperience >= 10:
            mike.say "Oh fuck...Kleio, no more...I want to blow it inside of you!"
            "Not exactly the most poetic of lines, I know - but then Kleio's not the most conventional of girls."
            "Kleio releases my cock with a gentleness that belies her usually forceful demeanour."
            scene bg bedroom1
            show kleio naked
            with fade
            if kleio.flags.mikeNickname in nickname_master:
                kleio.say "I am yours to use as you please Master."
            else:
                kleio.say "Whatever you say, [hero.name]...but now you better do something to REALLY impress me!"
    return

label kleio_sleep_date_fuck(location="hero"):
    if game.hour > 19 or game.hour < 6:
        scene bg bedroom1
        show kleio naked
        with fade
        if kleio.is_sex_slave:
            kleio.say "May I share your bed tonight, Master?"
        else:
            kleio.say "Mmm...you cool with me spending the night here?"
        menu:
            "No":
                mike.say "No...I have to be up really early in the morning."
                "The sex was beyond incredible, but now I want to be alone."
                "Kleio frowns in disappointment, clearly trying to shrug off the sense of rejection."
                kleio.say "Okay...sleep well, I guess."
                "She shakes her head as she collects her things and leaves my bedroom."
                $ kleio.love -= 3
                call sleep from _call_sleep_21
                $ game.room = "bedroom1"
            "Yes":
                mike.say "YES...I mean, yes...if you want to!"
                "I try to keep from sounding too desperate and needy, but I'm not sure I manage it."
                show cuddle kleio with fade
                "Kleio curling up against me beneath the covers is almost as good as the sex - almost..."
                if kleio.is_sex_slave:
                    kleio.say "Sweet dreams, Master..."
                else:
                    kleio.say "Sweet dreams, [hero.name]..."
                mike.say "You too, Kleio..."
                $ kleio.love += 3
                call sleep ("kleio") from _call_sleep_1
                $ game.room = "bedroom1"
    return

label kleio_fuck_date_cowgirl(sexperience_min):
    menu:
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5) and kleio.sub > 50:
            "I love to play games with Kleio, and teasing to see her reaction is a massive turn on."
            "And it's with that in mind that an idea springs into my mind at that very moment."
            "Adjusting my backside to change the angle of my cock just so, I pull Kleio down onto me."
            show kleio cowgirl anal with fade
            "I see her eyes go wide a moment later, telling me that I was right on the money."
            kleio.say "Ahh...shit..."
            kleio.say "[hero.name]...that's...my ass!"
            mike.say "You said you wanted me inside of you, Kleio."
            mike.say "You didn't say where!"
            "Kleio makes to answer, but then I see her eyes close and her head roll."
            "She puts her hands flat on my chest and moans as she sinks further onto my cock."
            mike.say "How does it feel, Kleio?"
            "She whimpers a little and I can feel her muscles trembling as she takes all of me into her."
            kleio.say "It's...good..."
            kleio.say "It feels...really good!"
            show kleio cowgirl pleasure
            kleio.say "Please...don't take it out...don't stop!"
            "At this point I don't know what's keeping me harder."
            "Whether it's the tight sensation of her asshole around my cock."
            "Or seeing Kleio's reaction to having it up her so deep."
            "I feel like I'm watching her melt, right before my eyes."
            "And every time she sighs or her body twitches with pleasure I feel a sense of gratification."
            "She had no idea that this was going to happen to her until the very moment that it began."
            "Now here she is, moaning and biting her lip as she goes up and down with my cock up her ass!"
            "I don't know if this is going to be enough to make Kleio cum."
            "But it's sure as hell going to do it for me!"
            call cum_reaction (kleio, 'anal', sexperience_min) from _call_cum_reaction_87
            if _return == 'anal_inside':
                "I grasp Kleio around the waist, my hands instantly slipping down to her thighs thanks to her sweat-slick skin."
                "But my grip is as firm as I can make it, enough to be sure that she won't escape what's coming next."
                show kleio cowgirl ahegao creampie with vpunch
                $ kleio.sub += 2
                "As my orgasm takes me, I begin to push into Kleio, harder than ever before."
                with vpunch
                "She's actually crying by now, the mixture of pleasure and pain threatening to become too much."
                with vpunch
                "The problem is that I'm not about to release her until it's over."
                "I can't imagine what it feels like for her when I let go that deep inside of her ass."
                "All I know is that it takes everything out of me on one massive push."
                "Afterwards, Kleio collapses atop me, like a marionette with its strings suddenly severed."
            elif _return == 'anal_outside':
                "I'd like to say that I make the effort of pulling my cock out of Kleio's ass before I cum as a mercy to her."
                "But the truth is that I'm not feeling anything like as charitable."
                show kleio cowgirl -anal ahegao
                show sexinserts chest kleio zorder 1 at center, zoomAt(1, (710, 740))
                show sexinserts belly kleio as bellycum zorder 2 at center, zoomAt(1, (725, 970))
                "Instead I enjoy the sight of my manhood bobbing up the moment that it emerges from her with an audible popping sound."
                show kleio cowgirl pleasure cumshot with vpunch
                "A second later I cum, sending streamers of hot, white semen spattering all over Kleio's naked body."
                show sexinserts chest kleio cum zorder 1 at center, zoomAt(1, (710, 740))
                show sexinserts belly kleio cum as bellycum zorder 2 at center, zoomAt(1, (725, 970))
                with vpunch
                "It showers down on her breasts and stomach as she yelps in surprise."
                show kleio cowgirl -cumshot dickcum cum onbody with vpunch
                $ kleio.sub += 1
                "And then it runs over her tight belly and down the inside of her already slick thighs."
                "Still overcome by the sensations of having me inside her, Kleio can't keep from caressing herself the whole time."
                "I watch as she rubs the semen all over her sweat-covered skin, seemingly unable to stop herself now that she's started."
                hide sexinserts
                hide bellycum
            $ kleio.flags.anal += 1
        "Fuck her pussy":
            call check_condom_usage (kleio, love=180, drinks=3) from _call_check_condom_usage_62
            if _return == False:
                return "leave_without_gain"
            show kleio cowgirl vaginal
            if CONDOM:
                show kleio cowgirl condom
            with fade
            "I can already feel the warmth of Kleio's pussy, how wet she is too."
            "Just knowing that she's been thinking of this moment all night is enough to make my mind up."
            "The head of my cock barely has a chance to brush at the folds or feel her lips."
            "It slips inside of her almost the first moment it can, and Kleio sinks down upon it just as quickly."
            "I can almost feel the hunger inside of her, the sheer appetite that she has for me right now."
            kleio.say "Now...that...is what...I'm talking about!"
            kleio.say "I don't meet many cocks that I like."
            kleio.say "But when I do, I like them inside of me!"
            "Kleio smiles down at me as she begins to ride my cock, making me feel every tiny movement she makes."
            "She plants her hands on my chest and seems to revel in doing most of the work."
            mike.say "My...my cock...loves you, Kleio!"
            mike.say "Loves...your...pussy..."
            "By now, Kleio's smile has become a grin worthy of a Cheshire Cat."
            "And she beams as she continues to ride me without mercy."
            "When I reach up to touch her breasts as they sway in time to her movements, she teases me by pulling them away."
            "Almost entranced, I keep reaching for them all the same, making her laugh at my efforts."
            "When she finally relents and lets me cup one in each hand, her small nipples are as stiff as they could be."
            "Kleio moans in appreciation as I lose my inhibitions and become rougher with her breasts."
            "The harder I massage and squeeze, the faster her thighs seem to move up and down in sympathy."
            "Soon she casts her head back and begins to bite her lip, making me wonder just how close she is to cumming."
            "My hands move to Kleio's backside, grabbing her buttocks and almost forcing her down onto me with ever greater urgency."
            "I don't know if I'm racing to keep up with her, or else in the hope of beating her to the punch."
            "But either way, the effect is the same, and I can feel myself tipping over the edge..."
            call cum_reaction (kleio, 'vaginal', sexperience_min) from _call_cum_reaction_88
            if _return == "vaginal_outside":
                "As much fun as pounding Kleio almost into submission has been, I don't want to knock her up."
                "With her weight atop me and the state that she's worked herself into, it falls to me to get myself free."
                show kleio cowgirl -vaginal ahegao
                show sexinserts chest kleio zorder 1 at center, zoomAt(1, (710, 740))
                show sexinserts belly kleio as bellycum zorder 2 at center, zoomAt(1, (725, 970))
                "Almost at the last moment, I manage to wriggle out from under Kleio."
                show kleio cowgirl pleasure cumshot with vpunch
                "A second later I cum, sending streamers of hot, white semen splattering all over Kleio's naked body."
                show sexinserts chest kleio cum zorder 1 at center, zoomAt(1, (710, 740))
                show sexinserts belly kleio cum as bellycum zorder 2 at center, zoomAt(1, (725, 970))
                with vpunch
                "It showers down on her breasts and stomach as she yelps in surprise."
                show kleio cowgirl -cumshot dickcum cum onbody with vpunch
                $ kleio.sub += 1
                "And then it runs over her tight belly and down the inside of her already slick thighs."
                "Still overcome by the sensations of having me inside her, Kleio can't keep from caressing herself the whole time."
                "I watch as she rubs the semen all over her sweat-covered skin, seemingly unable to stop herself now that she's started."
                hide sexinserts
                hide bellycum
            elif _return == "vaginal_condom":
                "Grateful to myself for having remembered to take precautions before we got started, I keep right on going."
                with vpunch
                "This means that all of the effort and energy that goes into my climax is felt by Kleio at the same time."
                show kleio cowgirl ahegao with vpunch
                $ kleio.love += 1
                "Even as I let go and make one last push into her, she succumbs too."
                with vpunch
                "It might not be a perfect example of a double orgasm, but it's close enough for me."
                "The strength of it takes my last little reserve, and I can't hold Kleio up any longer."
                "Not that the afterglow seems to have left her feeling any less drained, as she proceeds to flop down atop me."
                "I feel myself slide out of Kleio even as she slithers over my sweat-soaked body."
            elif _return == "vaginal_inside_pill":
                "Remembering that I don't want to have an accident in the middle of all this fun, I make to pull out."
                "But then I feel Kleio bracing herself atop me, as if trying to keep me from doing just that."
                "I look at her in surprise, wondering if she's let the danger slip her mind."
                "She shakes her head at me, urging me to keep going."
                kleio.say "Pill...remember...dumbass!"
                "Of course, how could I have forgotten - Kleio's on the pill!"
                show kleio cowgirl creampie ahegao with vpunch
                $ kleio.love += 2
                "But in the time it's taken her to remind me, I've already managed to cum."
                with vpunch
                "It might not be a perfect example of a double orgasm, but it's close enough for me."
                with vpunch
                "The strength of it takes my last little reserve, and I can't hold Kleio up any longer."
                "Not that the afterglow seems to have left her feeling any less drained, as she proceeds to flop down atop me."
                "I feel myself slide out of Kleio even as she slithers over my sweat-soaked body."
            elif _return == "vaginal_inside_pregnant":
                "I keep right on going, reasoning that I can hardly make Kleio more pregnant than I already have."
                "In fact, the extra weight of her swelling belly above me means that she's pressed down onto my cock more than ever."
                show kleio cowgirl ahegao
                "And in truth, I have to struggle to keep her upright as she begins to cum herself."
                "But all the same, I love the feeling of holding her like this."
                "She looks so healthy and full of vigour, with a new life growing inside of her..."
                show kleio cowgirl creampie with vpunch
                $ kleio.love += 3
                "I cum a second later, still supporting Kleio as she goes limp in the wake of her own orgasm."
                with vpunch
                "Gently cradling her in my arms, I guide her down onto the bed beside me, wrapping her in my arms."
            elif _return == "vaginal_inside_mad":
                if kleio.sub <= 75:
                    "All that I can hear is the sound of Kleio and myself panting in delighted exhaustion."
                    "And all that I can feel is the sensation of being inside of her at the same time."
                    "I guess that's why neither of us recalls the fact that I'm not using protection."
                    "Maybe both of us are expecting the other to be the one to make the call."
                    "Or maybe we're just enjoying ourselves too much to be able to think straight."
                    with vpunch
                    "Either way, I feel myself cum inside of Kleio, filling her with all that I have."
                    show kleio cowgirl creampie with vpunch
                    $ kleio.impregnate()
                    $ kleio.love -= 5
                    "And a second later the realisation of what I've just done fills me in turn."
                    with vpunch
                    kleio.say "[hero.name]...what's up?"
                    kleio.say "Tell me we didn't just..."
                    kleio.say "Ah, fuck!"
                else:
                    "As I begin to go through the motions of cumming, Kleio seems to become aware of my intentions."
                    "For the first time since we started screwing tonight, she makes an effort to assert herself."
                    with vpunch
                    "But as her attempt to wriggle out from under me is weak and half-hearted, I can easily press my weight down, keeping her in place."
                    with vpunch
                    "This done, Kleio stops struggling, although I can't tell if she's shaking from her climax or my holding her there."
                    show kleio cowgirl creampie with vpunch
                    $ kleio.impregnate()
                    $ kleio.love -= 1
                    $ kleio.sub += 2
                    "She begins to sob quietly as I fill her, burying her head in the pillow for the sake of not being seen as she weeps."
            elif _return == "vaginal_inside_happy":
                "Remembering that I don't want to have an accident in the middle of all this fun, I make to pull out."
                "But then I feel Kleio bracing herself atop me, as if trying to keep me from doing just that."
                "I look at her in surprise, wondering if she's let the danger slip her mind."
                "She shakes her head at me, urging me to keep going."
                kleio.say "Don't stop, [hero.name], please!"
                kleio.say "I...I want this."
                kleio.say "Please...cum inside me?"
                "Kleio says this with such desperate pleading, her face reflecting the same emotion."
                "I've never seen her like this before, and the sight almost stuns me."
                "It certainly distracts me long enough to ensure that she gets her wish."
                show kleio cowgirl ahegao creampie with vpunch
                $ kleio.impregnate()
                $ kleio.love += 5
                "A moment later I lose myself, deep inside of Kleio."
                with vpunch
                "I watch as she casts her head back and her own climax takes her."
                "Afterwards she lowers herself down and slithers over by cooling body, wrapping herself around me."
                "But my mind is already racing with the possible consequences of what we've just done."
    return

label kleio_fuck_date_cowgirl2(sexperience_min):
    menu:
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5) and kleio.sub > 50:
            "I know that Kleio's teasing me with her pussy right now."
            "And so I can't help doing what comes next, just to surprise her."
            "So I take a firm hold of her haunches, and pull downwards."
            "The smile on Kleio's face soon turns into an expression of surprise."
            "And her eyes go wide as she realises what I'm doing."
            kleio.say "Oh...you..."
            kleio.say "You...you wouldn't..."
            kleio.say "You...you can't..."
            show kleio cowgirl anal with fade
            "Even as Kleio's saying the words, my cock is pushing into her ass."
            "It's as tight as a fist to begin with, making me inch inside."
            "But I push upwards as she sinks down onto it at the same time."
            kleio.say "Shit...shit..."
            kleio.say "You did it..."
            kleio.say "You fucking did it!"
            "Kleio squirms and wriggles on my cock, panting for breath."
            "She holds my eye the whole time, every sensation written on her face."
            "Finally, her cheeks flush red and she looks away in shame."
            kleio.say "I...I like it..."
            kleio.say "I...mean I love it!"
            kleio.say "Please...fuck my ass?"
            "I can't help smiling as I begin to move inside of her."
            "The feeling of Kleio's ass around my cock is incredible."
            "And knowing that she wants it makes it that much sweeter."
            "She reacts almost the same moment that I move."
            "The muscles of her ass clenching and relaxing."
            show kleio cowgirl pleasure
            "Kleio nods desperately, moving up and down in sympathy."
            "The motion makes her breasts bob and bounce above me."
            "I can't tear my eyes away from them."
            "It's almost like they're hypnotizing me!"
            "Keeping one hand on Kleio's waist, I reach out with the other."
            "At first I just cup her breast in the palm of my hand, squeezing it gently."
            "But even this is enough to make Kleio nod more quickly, biting her lip."
            "And so I step up my efforts, pinching her nipple between my fingertips."
            "It stiffens in mere seconds, and Kleio lets out a moan of pleasure."
            "At the same time she pushes down with all of her weight."
            "Kleio's literally grinding herself into my groin by now."
            "Every time she does it, I feel myself twitch in response."
            "And it's not long before she pushes me straight over the edge!"
            call cum_reaction (kleio, 'anal', sexperience_min) from _call_cum_reaction_89
            if _return == 'anal_inside':
                "My cock is buried as deep into Kleio as it'll go right now."
                show kleio cowgirl ahegao creampie with vpunch
                $ kleio.sub += 2
                "So when I shoot my load, she takes everything I have to give."
                with vpunch
                "Kleio's mouth hangs open as she cums with the sensation."
                with vpunch
                "I can already feel it beginning to seep out of her ass."
                "But she keeps on pushing down on me until the very last."
                "And then she collapses forwards, exhausted and utterly spent."
            elif _return == 'anal_outside':
                "I push Kleio upwards and pull myself down at the same time."
                "And it's just enough to ensure my cock pops out of her before it's too late."
                show sexinserts chest kleio zorder 1 at center, zoomAt(1, (710, 740))
                show sexinserts belly kleio as bellycum zorder 2 at center, zoomAt(1, (725, 970))
                show kleio cowgirl -anal ahegao
                "Kleio moans as it bobs beneath her, shooting cum over her slick belly."
                show kleio cowgirl pleasure cumshot
                show sexinserts chest kleio cum zorder 1 at center, zoomAt(1, (710, 740))
                show sexinserts belly kleio cum as bellycum zorder 2 at center, zoomAt(1, (725, 970))
                with vpunch
                "She collapses onto me, slick with sweat and rubbing semen between us."
                show kleio cowgirl -cumshot dickcum cum onbody with vpunch
                $ kleio.sub += 1
                "Kleio cums a moment later, writhing on top of me the whole time."
                "And then her head flops onto my shoulder, exhausted and utterly spent."
                hide sexinserts
                hide bellycum
            $ kleio.flags.anal += 1
        "Fuck her pussy":
            call check_condom_usage (kleio, love=180, drinks=3) from _call_check_condom_usage_63
            if _return == False:
                return "leave_without_gain"
            show kleio cowgirl vaginal
            if CONDOM:
                show kleio cowgirl condom
            "I know I said that Kleio was already nice and slippery down there."
            "And of course, that means I slide straight into her."
            "But that doesn't mean it's not a feeling that takes my breath away."
            "Kleio squirms and wriggles as she sinks down onto me."
            "She grinds herself against me, giggling and biting her lip."
            kleio.say "Mmm..."
            kleio.say "Your cock feels good tonight, Loverboy!"
            kleio.say "Nice and big too - enough to fill me right up!"
            "I nod as I begin to move inside of Kleio."
            "Enjoying the sensation of her tight little pussy."
            "She smiles down at me, massaging her breasts as she does so."
            kleio.say "C'mon, Loverboy."
            kleio.say "Don't hold out on me now."
            kleio.say "I want to be feeling your dick inside of me for hours after we're done!"
            "I have to try hard to remember a time when I wasn't turned on by Kleio's mouth."
            "It's filthy and always spouting her own unique brand of insults too."
            "But the sound of her voice just seems to do something to me."
            "And all I want to do is fuck her that much harder!"
            kleio.say "Oh yeah..."
            kleio.say "That's it...that's..."
            kleio.say "Oh god...I...oh shit..."
            "I watch as Kleio's eyes glaze over."
            "And she slowly seems to lose the power of speech too."
            "Most likely because I'm hammering her like a piston by now!"
            "Kleio's mouth hangs open, her words replaced by animal moans."
            "Her breasts are bouncing freely on her chest in sympathy."
            "And she just groans when I reach up to squeeze them."
            "Kleio's almost like a puppet dancing on my dick."
            "Her movements dictated by how hard and fast I'm fucking her."
            "Sweat stands out on her skin, glistening in the low light."
            "And her tattoos move like animated pictures too!"
            "All of it makes me wonder what my little puppet will do when I cum..."
            call cum_reaction (kleio, 'vaginal', sexperience_min) from _call_cum_reaction_90
            if _return == "vaginal_outside":
                show sexinserts chest kleio zorder 1 at center, zoomAt(1, (710, 740))
                show sexinserts belly kleio as bellycum zorder 2 at center, zoomAt(1, (725, 970))
                "I push Kleio upwards and pull myself down at the same time."
                "And it's just enough to ensure my cock pops out of her before it's too late."
                show sexinserts chest kleio cum zorder 1 at center, zoomAt(1, (710, 740))
                show sexinserts belly kleio cum as bellycum zorder 2 at center, zoomAt(1, (725, 970))
                show kleio cowgirl -vaginal ahegao cumshot
                with vpunch
                "Kleio moans as it bobs beneath her, shooting cum over her slick belly."
                show kleio cowgirl pleasure with vpunch
                "She collapses onto me, slick with sweat and rubbing semen between us."
                with vpunch
                "Kleio cums a moment later, writhing on top of me the whole time."
                show kleio cowgirl -cumshot dickcum cum onbody with vpunch
                $ kleio.sub += 1
                "And then her head flops onto my shoulder, exhausted and utterly spent."
                hide sexinserts
                hide bellycum
            elif _return == "vaginal_condom":
                "My cock is buried as deep into Kleio as it'll go right now."
                "But that's not a problem, as we already took precautions."
                show kleio cowgirl ahegao
                $ kleio.love += 1
                "So when I shoot my load, she takes everything I have to give."
                "Kleio's mouth hangs open as she cums with the sensation."
                "I can already feel it beginning to seep out of her pussy."
                "But she keeps on pushing down on me until the very last."
                "And then she collapses forwards, exhausted and utterly spent."
            elif _return == "vaginal_inside_pill":
                kleio.say "Keep going..."
                kleio.say "Please?!?"
                "I remember Kleio telling me she's on the pill."
                show kleio cowgirl creampie ahegao with vpunch
                $ kleio.love += 2
                "So when I shoot my load, there's no need to worry."
                with vpunch
                "Kleio's mouth hangs open as she cums with the sensation."
                with vpunch
                "I can already feel it beginning to seep out of her pussy."
                "But she keeps on pushing down on me until the very last."
                "And then she collapses forwards, exhausted and utterly spent."
            elif _return == "vaginal_inside_pregnant":
                kleio.say "Keep going..."
                kleio.say "Please?!?"
                show kleio cowgirl ahegao
                "I take hold of Kleio, cradling her belly."
                with vpunch
                "And when I shoot my load, she takes everything I have to give."
                with vpunch
                "Kleio's mouth hangs open as she cums with the sensation."
                show kleio cowgirl creampie with vpunch
                $ kleio.love += 3
                "I can already feel it beginning to seep out of her pussy."
                with vpunch
                "But she keeps on pushing down on me until the very last."
                "And then she collapses forwards, exhausted and utterly spent."
            elif _return == "vaginal_inside_mad":
                kleio.say "Oh shit..."
                kleio.say "Pull out - NOW!"
                with vpunch
                "I shoot my load literally the second before Kleio warns me."
                show kleio cowgirl creampie with vpunch
                $ kleio.impregnate()
                $ kleio.love -= 5
                "And I'm too deep in her to have a hope of pulling out."
                with vpunch
                "Kleio cums a moment later, and we're locked together as it happens."
                "Afterwards, neither of us speaks, we just stare at each other in horror."
            elif _return == "vaginal_inside_happy":
                kleio.say "Oh shit..."
                kleio.say "Keep going..."
                kleio.say "Cum inside of me - PLEASE?!?"
                with vpunch
                "Shoot my load literally the second that I realise the danger."
                show kleio cowgirl ahegao creampie with vpunch
                $ kleio.impregnate()
                $ kleio.love += 5
                "But Kleio clings to me for all she's worth, making sure I can't pull out."
                with vpunch
                "She cums as I shoot my load into her, gasping the whole time."
                "Afterwards she seems elated, but I just stare at her in horror."
    return

label kleio_fuck_date_doggy2(sexperience_min):
    mike.say "Climb up on the bed, Kleio."
    mike.say "I want you on your hands and knees tonight."
    "Kleio takes a step towards the bed, but then hesitates."
    kleio.say "But, I thought..."
    kleio.say "I thought I might go on top?"
    kleio.say "You know...for a change?"
    "I let out an rueful laugh and shake my head at this, dismissing her without pause or hesitation."
    mike.say "Come on, Kleio - it can't always be about what you want, now can it?"
    mike.say "And anyway, I'm the one that's going to have to be doing all the work."
    mike.say "All you need to do is just spread your legs and take it!"
    "Kleio bites her lip and then nods, the look in her eyes not matching the sentiment of the gesture."
    "All the same, she climbs onto the bed and does as she's told."
    scene kleio_doggy2 with fade
    "Once she's standing on all fours, legs spread as instructed, she glances back at me again."
    "I strip off slowly, making Kleio wait in that position until I'm ready to indulge her."
    "Only when I'm good and ready do I climb up behind her, placing both hands on her buttocks as I do so."
    "A shudder of anticipation passes through Kleio's body, and I can't help smiling at the wisdom of making her wait."
    "I stroke a single finger between her thighs and along the lips of her pussy, testing her state of readiness for me."
    show kleio_doggy2 mike
    "Finding that she's already good and slick, I push my now stiff cock forwards, just enough so she can feel its presence."
    "Kleio whimpers a little at this, anticipating what's to come next."
    "And that sound only serves to make me all the more ready for it too."
    "I've made no comment as to just what I intend to do to Kleio before now."
    "And the mystery only serves to add to the moment, as she waits to discover what comes next."
    "Truth be told, I haven't decided that for myself yet."
    "My plan was always to see how the mood took me when this moment came along."
    menu:
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5) and kleio.sub > 50:
            "I think that keeping things new and exciting is a pretty important part of a long-term relationship."
            "Well, that and I love the sight of Kleio's tight little ass, just there for the taking!"
            "I make a point of dragging the head of my cock along the lips of her pussy."
            "And I can sense that she's waiting for me to slip in there at any moment."
            "All of which makes it that much more enjoyable when I part her buttocks with my hands and push into her ass."
            "The move seems to take Kleio by complete surprise, and I feel the proof of this as her body shudders."
            "But it also means that she can do nothing to keep me from having my way with her too."
            show kleio_doggy2 anal
            "Before the muscles of her ass can even begin to react, the head of my cock is already in there."
            "Too late, her sphincter wakes up to the reality of what's happening and begins to tighten."
            "Yet this only means that the few inches of my cock already up her are held more firmly in place."
            mike.say "Don't fight it, Kleio."
            mike.say "It'll only make me enjoy the feeling all the more!"
            "In way of response, Kleio can only whimper and nod her head at first."
            "She keeps on staring ahead, as if afraid to look back and see what's happening to her right now."
            kleio.say "Please...be gentle..."
            "The words are a whisper, barely loud enough to reach my ear."
            "But all the same they're enough to inspire me to do the exact opposite."
            "I begin moving slowly inside of her, but with more force than is strictly necessary."
            "Kleio instantly groans and bows her head at the sensation, clearly feeling discomfort at this."
            show kleio_doggy2 anal pleasure
            "But as I already warned her, that only serves to make me all the more determined."
            "My pace begins to quicken almost as soon as the second push into her ass, and it doesn't slow."
            "Pretty soon I'm moving in and out of her ass as fast as I ever would have in her pussy."
            "I swear that I can hear the sounds of tortured pleasure beginning to creep into Kleio's constant cries."
            "And the thought that she's getting off on what I'm doing in spite of herself makes me work harder still."
            "By now I can feel the muscles of Kleio's ass starting to quiver and shake."
            "They squeeze at my cock, which is already held tightly inside of her."
            "And the result is that I can't keep myself from cumming..."
            call cum_reaction (kleio, 'anal', sexperience_min) from _call_cum_reaction_91
            if _return == 'anal_inside':
                "As I'm not fucking her pussy, I see no reason to show Kleio the mercy of pulling out of her now."
                "Instead I redouble my efforts, trying to push my cock still deeper into her ass before I finally cum."
                show kleio_doggy2 anal creampie with hpunch
                "When I lose myself and fill her back passage, I'm practically leaning on her shaking back to make this happen."
                with hpunch
                "Kleio is still quivering around me as the moment passes and my cock begins to slacken off."
                show kleio_doggy2 anal ahegao with hpunch
                "With me making no more effort to hold her up, she quickly slides off of me and onto the bed below."
                "I stay where I am, kneeling over her and allowing the last few spurts of cum to drip down onto her thighs."
            elif _return == 'anal_outside':
                "I practically have to yank my cock out of the grip of Kleio's ass."
                show kleio_doggy2 -anal cumshot ahegao with hpunch
                "And this means that I'm losing myself almost at the same moment that it finally pops out of there."
                with hpunch
                "The strangled gasp that she lets out must be from the sensation itself."
                with hpunch
                "But as it comes in time with her ass being splattered by streamers of semen, it's easy to believe otherwise."
                show kleio_doggy2 -cumshot dickcum
                "Without me to support her weight, Kleio's legs buckle and she collapses onto the bed in a sweaty pile of limbs."
                "I stay where I am, kneeling over her and allowing the last few spurts of cum to drip down onto her thighs."
            $ kleio.flags.anal += 1
        "Fuck her pussy":
            call check_condom_usage (kleio, love=180, drinks=3) from _call_check_condom_usage_64
            if _return == False:
                return "leave_without_gain"
            "If I were feeling more cruel than I am right now, I might do something like take Kleio up the ass without warning."
            "But this is supposed to be fun for both of us, right?"
            "And anyway, the feeling of those slick lips down there is almost too much to resist."
            "I take a firm hold of her buttocks, using them as an anchor as I pull her back and onto my waiting cock."
            "For all of her nervous glances and whimpering beforehand, there's no question in my mind that Kleio wanted this as much as me."
            show kleio_doggy2 vaginal
            if CONDOM:
                show kleio_doggy2 vaginal condom
            "She parts like a flower opening for the sunlight, letting me straight into her in one smooth motion."
            "The sound of her gasping in reaction to my entry is almost as much of a turn on as the actual sensation of the thing."
            "And I don't stop pushing into her on that first thrust until I can't go any deeper."
            "I see Kleio grabbing handfuls of the bedclothes beneath her, and I know she's feeling the same kind of pleasure as me."
            mike.say "You like the feel of me so deep inside you, Kleio?"
            mike.say "It feels good?"
            "Kleio tries to answer, but her first attempt turns into another moan as I slowly begin to move inside of her."
            mike.say "Huh - what was that?"
            kleio.say "Yeah...yeah...I love it..."
            show kleio_doggy2 pleasure
            kleio.say "I love having...your cock in me, [hero.name]!"
            "Her words melt away into cries of pleasure once more as I quicken my pace to reward her for that admission."
            "I've never thought of myself as a sadistic kind of guy, or one that gets off on dominating a girl."
            "But somehow the fact that Kleio's become so submissive to me after she used to be so prickly and outspoken..."
            "Well, it just makes me want to pound her that much harder!"
            "With the gusto I start to put into each thrust in and out of Kleio, she jumps forward a little on the bed."
            "It's a wonder that she doesn't end up with her face pressed against the wall as I go at her."
            "Soon enough I can tell from the way that she's beginning to moan and shake that Kleio's about to cum."
            "The feeling of this and the knowledge that I've driven her to it with my efforts ensures that she won't be alone either."
            call cum_reaction (kleio, 'vaginal', sexperience_min) from _call_cum_reaction_92
            if _return == "vaginal_outside":
                "It takes a lot to make me drag my cock out of Kleio in the few seconds before I cum."
                show kleio_doggy2 -vaginal cumshot with hpunch
                "But I can't let what's supposed to be a bit of fun turn into an accident that we'll both regret."
                with hpunch
                "Kleio gasps as she cums herself, a sound tinged with a little disappointment."
                show kleio_doggy2 -cumshot ahegao dickcum with hpunch
                "I can hardly pay her any attention, as my cock chooses that exact moment to spatter her buttocks."
                "Hot, wet, streamers of semen stripe Kleio's ass, making her yelp again in surprise."
                "I stay where I am, kneeling over her and allowing the last few spurts of cum to drip down onto her thighs."
                $ kleio.sub += 1
            elif _return == "vaginal_condom":
                "Sparing a moment to be thankful that I did the same to use protection, I keep right on going."
                "All of my remaining strength goes into making sure we both cum with as much force as I can manage."
                show kleio_doggy2 creampie ahegao with hpunch
                "So when I finally cum, I'm gasping and panting just as much as Kleio has been the whole time."
                with hpunch
                "But by now she's stopped making any sound at all, and simply lets the orgasm take her."
                with hpunch
                "The moment that I stop holding up her weight, Kleio slithers off of my cock and collapses onto the bed."
                "All I can do is kneel over her, panting in an effort to catch my breath and make the room stop spinning."
                $ kleio.love += 1
            elif _return == "vaginal_inside_pill":
                "A twinge of disappointment twists in my gut as I realise it's time to pull out before I cum."
                "But then I recall the fact that Kleio had specifically told me she was going on the pill before now."
                "The fact that she must be aware I'm on the brink and hasn't made to wriggle out from under me makes me sure of this too."
                show kleio_doggy2 creampie ahegao with hpunch
                "So I push on, using the last of my strength to push myself as deep into Kleio as I can manage."
                with hpunch
                "The moment after I cum, Kleio slithers off of my cock and collapses onto the bed."
                with hpunch
                "All I can do is kneel over her, panting in an effort to catch my breath and make the room stop spinning."
                $ kleio.love += 2
            elif _return == "vaginal_inside_pregnant":
                "The reassuring weight of Kleio's swelling belly is there the whole time, swaying gently."
                "It reminds me that I have nothing to fear from keeping right on going to the end."
                with hpunch
                "So I push myself with all I have left, using the last of my strength to get deep into Kleio."
                show kleio_doggy2 creampie ahegao with hpunch
                "The moment after I cum, Kleio slithers off of my cock and collapses onto the bed, cradling her belly in a protective hug."
                with hpunch
                "All I can do is kneel over her, panting in an effort to catch my breath and make the room stop spinning."
                $ kleio.love += 2
            elif _return == "vaginal_inside_mad":
                if kleio.sub <= 75:
                    "I'm so lost in the moment right now that the fact I'm not wearing a condom is the last thing on my mind."
                    "Kleio too seems to be totally caught up in what we're doing to be able to keep her head and remind me."
                    with hpunch
                    "That's why I find myself losing it inside of her a couple of moments later."
                    with hpunch
                    "The feeling is incredible, until it finally dawns on me what just happened."
                    show kleio_doggy2 creampie ahegao with hpunch
                    $ kleio.impregnate()
                    "I find myself going stiff, even as my cock is going limp."
                    "And Kleio glances back at me, over her shoulder."
                    "The shocked look on her face seems to say that she knows exactly what just happened."
                    $ kleio.love -= 10
                else:
                    "As I begin to go through the motions of cumming, Kleio seems to become aware of my intentions."
                    "For the first time since we started screwing tonight, she makes an effort to assert herself."
                    with hpunch
                    "But as her attempt to wriggle out from under me is weak and half-hearted, I can easily press my weight down, keeping her in place."
                    with hpunch
                    "This done, Kleio stops struggling, although I can't tell if she's shaking from her climax or my holding her there."
                    show kleio_doggy2 creampie ahegao with hpunch
                    $ kleio.impregnate()
                    "She begins to sob quietly as I fill her, burying her head in the pillow for the sake of not being seen as she weeps."
                    $ kleio.love -= 1
                    $ kleio.sub += 2
            elif _return == "vaginal_inside_happy":
                "I keep expecting Kleio to tell me it's time to pull out at any given second."
                "The very least I expect is for her to try to wriggle out from under me."
                "But she does neither of these things, merely riding out the thrusts of my orgasm on the end of my cock."
                show kleio_doggy2 creampie ahegao with hpunch
                "My surprise is such that I couldn't have pulled out of her had I tried."
                with hpunch
                "And so, when I cum, I fill her completely and without a shred of protection to show for it."
                with hpunch
                "As she collapses to the bed beneath her, all I can hear from Kleio are muffled gasps of what sound like satisfied pleasure."
                $ kleio.impregnate()
                "I kneel there and watch in puzzlement, as the last of the semen it drips from my cock and onto her bare thighs."
                $ kleio.love += 5
    return

label kleio_fuck_date_doggy(sexperience_min):
    $ sexperience_min = 0
    show kleio doggy mike with fade
    $ kleio.sub += 1
    "I turn Kleio so that she's on all fours, then give her ass a sharp slap that sends her inching forwards in surprise."
    kleio.say "Hey, [hero.name]...have I been so bad that I need a spanking?"
    "The delight in her eyes tells me instantly that she's enjoying this, and that she wants some more."
    mike.say "No amount of spanking's ever going to fix you, Kleio...no amount of cock, either...but that's not gonna stop me from trying."
    menu:
        "Fuck her pussy":
            call check_condom_usage (kleio, love=180, drinks=3) from _call_check_condom_usage_65
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show kleio doggy condom
            show kleio doggy vaginal hurt
            "I mount her before she can say another word, enjoying the sensation of pushing into Kleio's tight lips and feeling her tremble in reply."
            show kleio doggy shake
            "My chest is pressing down on her back, my face in her sweat-soaked hair, and I can feel her breasts as I reach for them."
            "We're like animals fucking in an alleyway, nothing but the moment and our coupling seems to matter."
            show kleio doggy sweat
            "A moment later I feel Kleio toss her head back as she senses that I'm about to cum."
            kleio.say "Don't hold back - take me with you!"
            call cum_reaction (kleio, 'vaginal', sexperience_min) from _call_cum_reaction_93
            if _return == "vaginal_outside":
                "Somehow the craziness and reckless streak that Kleio's capable of bringing out in me looses its hold as I peak."
                show kleio doggy out cumshot ahegao -shake with hpunch
                $ kleio.love += 1
                "It takes all the effort that I can summon, but somehow I manage to drag myself out of her a few short seconds before my climax takes over."
                with hpunch
                "I try to make up for it by pulling her close to me and beginning to stroke her roughly to orgasm with my fingers."
                show kleio doggy dickcum normal -cumshot with hpunch
                "But instinct tells me that the sighs Kleio is now making are heavily tinged with disappointment, and when she cums it's an anticlimax for her."
                "I try to be positive, thinking that her not objecting means she understands the reason for my actions."
                "But I can't help sharing in her sense of disappointment a little as well."
            elif _return == "vaginal_condom":
                "I can't tell if Kleio is clawing at the sheets in passion or else in an effort to free herself."
                "Either way it doesn't matter - my weight is too much for her to slip out from under, and there's no time left."
                show kleio doggy ahegao creampie squirt -shake with hpunch
                $ kleio.love += 1
                "The convulsions grip me and are instantly transferred into Kleio's body, making her buck in sympathy."
                with hpunch
                "She cries out, almost like she's in pain, and I can feel her nails digging into my skin, drawing blood."
                show kleio doggy smoke -squirt with hpunch
                "Kleio's cries fade along with my own motions as the climax passes and we sink into a tangled mess amongst the tossed sheets."
            elif _return == "vaginal_inside_pill":
                "I can't tell if Kleio is clawing at the sheets in passion or else in an effort to free herself."
                "Either way it doesn't matter - my weight is too much for her to slip out from under, and there's no time left."
                show kleio doggy ahegao creampie squirt -shake with hpunch
                $ kleio.love += 2
                "The convulsions grip me and are instantly transferred into Kleio's body, making her buck in sympathy."
                with hpunch
                "She cries out, almost like she's in pain, and I can feel her nails digging into my skin, drawing blood."
                show kleio doggy smoke -squirt with hpunch
                "Kleio's cries fade along with my own motions as the climax passes and we sink into a tangled mess amongst the tossed sheets."
            elif _return == "vaginal_inside_pregnant":
                "I can't tell if Kleio is clawing at the sheets in passion or else in an effort to free herself."
                "Either way it doesn't matter - my weight is too much for her to slip out from under, and there's no time left."
                show kleio doggy ahegao creampie squirt -shake with hpunch
                $ kleio.love += 3
                "The convulsions grip me and are instantly transferred into Kleio's body, making her buck in sympathy."
                with hpunch
                "She cries out, almost like she's in pain, and I can feel her nails digging into my skin, drawing blood."
                show kleio doggy smoke -squirt with hpunch
                "Kleio's cries fade along with my own motions as the climax passes and we sink into a tangled mess amongst the tossed sheets."
            else:
                "I can't tell if Kleio is clawing at the sheets in passion or else in an effort to free herself."
                "Either way it doesn't matter - my weight is too much for her to slip out from under, and there's no time left."
                show kleio doggy ahegao creampie squirt -shake with hpunch
                $ kleio.impregnate()
                $ kleio.love += 5
                "The convulsions grip me and are instantly transferred into Kleio's body, making her buck in sympathy."
                with hpunch
                "She cries out, almost like she's in pain, and I can feel her nails digging into my skin, drawing blood."
                show kleio doggy smoke -squirt with hpunch
                "Kleio's cries fade along with my own motions as the climax passes and we sink into a tangled mess amongst the tossed sheets."
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5) and kleio.sub > 50:
            show kleio doggy anal hurt
            "Without a word, I give in to a wicked impulse and part Kleio's buttocks so that I can push myself into her exposed ass."
            "She yelps in surprise, far more loudly than I had expected, but she can't hope to either shake me off or slip out from under me now."
            "I don't waste time being gentle, and yet I can already feel Kleio shuddering and continuing to yelp as I move inside of her."
            show kleio doggy shake
            mike.say "You deserve this, Kleio...you've been a real bad girl, and this is your punishment."
            "I catch a glimpse of Kleio's face and see that her cheeks are red and burning, maybe from the effects of my scolding words."
            show kleio doggy sweat
            "The combination of taking her up the ass and knowing that I've somehow humbled, even dominated a fiery spirit like hers pushes me quickly towards my climax."
            $ kleio.sub += 1
            kleio.say "Don't hold back - take me with you!"
            call cum_reaction (kleio, 'anal', sexperience_min) from _call_cum_reaction_94
            if _return == 'anal_inside':
                "I can't tell if Kleio is clawing at the sheets in passion or else in an effort to free herself."
                "Either way it doesn't matter - my weight is too much for her to slip out from under, and there's no time left."
                show kleio doggy ahegao creampie squirt -shake with hpunch
                $ kleio.sub += 2
                "The convulsions grip me and are instantly transferred into Kleio's body, making her buck in sympathy."
                with hpunch
                "She cries out, almost like she's in pain, and I can feel her nails digging into my skin, drawing blood."
                show kleio doggy smoke -squirt with hpunch
                "Kleio's cries fade along with my own motions as the climax passes and we sink into a tangled mess amongst the tossed sheets."
            elif _return == 'anal_outside':
                "Somehow the craziness and reckless streak that Kleio's capable of bringing out in me looses its hold as I peak."
                show kleio doggy out cumshot ahegao -shake with hpunch
                $ kleio.sub += 1
                "It takes all the effort that I can summon, but somehow I manage to drag myself out of her a few short seconds before my climax takes over."
                with hpunch
                "I try to make up for it by pulling her close to me and beginning to stroke her roughly to orgasm with my fingers."
                show kleio doggy dickcum normal -cumshot with hpunch
                "But instinct tells me that the sighs Kleio is now making are heavily tinged with disappointment, and when she cums it's an anticlimax for her."
                "I try to be positive, thinking that her not objecting means she understands the reason for my actions."
                "But I can't help sharing in her sense of disappointment a little as well."
            $ kleio.flags.anal += 1
    hide kleio doggy
    return

label kleio_fuck_date_missionary(sexperience_min):
    show kleio rough bedroom
    "I push Kleio down onto her back, using all of my weight to pin her to the bed."
    "The force makes her legs ride up in the air, and she quickly wraps them around my back."
    menu:
        "Fuck her pussy":
            call check_condom_usage (kleio, love=180, drinks=3) from _call_check_condom_usage_66
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show kleio rough condom
            show kleio rough vaginal pleasure
            with fade
            "I'm inside of her before she can fully make sense of what's happening."
            "I deliberately keep myself from kissing her for the sake of hearing the way that she cries and moans."
            kleio.say "Oh, shit...[hero.name]...you're turning me into human origami!"
            kleio.say "You can snap anything you want...just don't fucking stop!"
            "Her hands are clasped behind her ass, and I'm almost rolling her onto her shoulders when I feel my climax coming over me."
            "Unable to stop myself, I bite down my lips, thinking that I can taste the copper tang of blood as I cum."
            call cum_reaction (kleio, 'vaginal', 5) from _call_cum_reaction_95
            if _return == "vaginal_outside":
                "Somehow the craziness and reckless streak that Kleio's capable of bringing out in me looses its hold as I peak."
                "It takes all the effort that I can summon, but somehow I manage to drag myself out of her a few short seconds before my climax takes over."
                show kleio rough -vaginal cumshot with vpunch
                "I try to make up for it by pulling her close to me and beginning to stroke her roughly to orgasm with my fingers."
                with vpunch
                "But instinct tells me that the sighs Kleio is now making are heavily tinged with disappointment, and when she cums it's an anticlimax for her."
                with vpunch
                "I try to be positive, thinking that her not objecting means she understands the reason for my actions."
                "But I can't help sharing in her sense of disappointment a little as well."
                hide kleio rough
            else:
                "I can't tell if Kleio is clawing at the sheets in passion or else in an effort to free herself."
                "Either way it doesn't matter - my weight is too much for her to slip out from under, and there's no time left."
                show kleio rough ahegao
                if not CONDOM:
                    show kleio rough creampie
                    $ kleio.impregnate()
                    "The convulsions grip me and are instantly transferred into Kleio's body, making her buck in sympathy."
                with vpunch
                "She cries out, almost like she's in pain, and I can feel her nails digging into my skin, drawing blood."
                with vpunch
                "Kleio's cries fade along with my own motions as the climax passes and we sink into a tangled mess amongst the tossed sheets."
                hide kleio rough
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5) and kleio.sub > 50:
            show kleio rough anal pleasure
            "I'm guessing that Kleio's expecting me to slip into her vagina, but my dick is already sinking into her ass."
            "She cries out in shock as I push myself all the way in, her mouth forming an exaggerated 'O'."
            mike.say "Hold that expression, Kleio...it makes you look like a sex-doll!"
            kleio.say "You'd like that, huh - if I were a fuck toy you could toss around?"
            mike.say "Only if you had a pull cord that'd make you talk filth when I pulled it."
            "The combination of her acid tongue and amazing body make me redouble my efforts, and I soon can't hold myself back any longer."
            $ kleio.sub += 1
            kleio.say "Don't hold back - take me with you!"
            call cum_reaction (kleio, 'anal', sexperience_min) from _call_cum_reaction_96
            if _return == 'anal_inside':
                "I can't tell if Kleio is clawing at the sheets in passion or else in an effort to free herself."
                "Either way it doesn't matter - my weight is too much for her to slip out from under, and there's no time left."
                show kleio rough ahegao
                show kleio rough creampie
                with vpunch
                "The convulsions grip me and are instantly transferred into Kleio's body, making her buck in sympathy."
                with vpunch
                "She cries out, almost like she's in pain, and I can feel her nails digging into my skin, drawing blood."
                with vpunch
                "Kleio's cries fade along with my own motions as the climax passes and we sink into a tangled mess amongst the tossed sheets."
                hide kleio rough
            elif _return == 'anal_outside':
                "Somehow the craziness and reckless streak that Kleio's capable of bringing out in me looses its hold as I peak."
                "It takes all the effort that I can summon, but somehow I manage to drag myself out of her a few short seconds before my climax takes over."
                show kleio rough -anal cumshot with vpunch
                "I try to make up for it by pulling her close to me and beginning to stroke her roughly to orgasm with my fingers."
                with vpunch
                "But instinct tells me that the sighs Kleio is now making are heavily tinged with disappointment, and when she cums it's an anticlimax for her."
                with vpunch
                "I try to be positive, thinking that her not objecting means she understands the reason for my actions."
                "But I can't help sharing in her sense of disappointment a little as well."
                hide kleio rough
            $ kleio.flags.anal += 1
    return

label kleio_garage_fuck:
    $ CONDOM = False
    scene bg garage
    "When the chance to meet up with Kleio comes along, I'm almost always going to take it."
    "But when she asked me to meet her this time, I kind of jumped on it without hesitation."
    "And that was because she said that she had some stuff to finish off at work."
    "Which also means that she wants me to meet her there before we go do something fun."
    "I know what you're thinking."
    "What's so great about meeting Kleio at work, right?"
    "But remember, Kleio's like one of those hot mechanic chicks!"
    "She spends all day getting greasy and sweaty around really cool cars!"
    "And, well...we kind of did it in her garage once before, so..."
    "Yeah, yeah...there's no guarantee she's going to want to go there again."
    "But you can't blame me for holding out hope, can you?"
    "Knowing that Kleio's likely to be distracted, I let myself into the garage."
    "Once inside, I glance around, trying to figure out where she might be."
    mike.say "Ah, Kleio..."
    mike.say "It's me..."
    mike.say "Where in the hell are you?"
    kleio.say "In the back, Loverboy."
    kleio.say "I'll be with you in a minute."
    kleio.say "Til then, just make yourself comfortable, okay?"
    "As I walk towards the sound of Kleio's voice I look around."
    "All I can see are cars and car parts, as well as tools to fix them."
    mike.say "I don't know if I can make myself comfortable, Kleio."
    mike.say "It's not like there's a sofa anywhere round here!"
    kleio.say "I dunno, Loverboy..."
    kleio.say "Maybe play with yourself or something!"
    "I open my mouth to say something as cutting in response."
    "But that's when I walk around the corner and see Kleio for the first time."
    "She's halfway through winching the engine out of a car."
    show kleio work c with dissolve
    "And from the looks of it, she's having to work pretty hard to do so."
    "I watch in silence as she gasps with the effort."
    "She's glistening with perspiration in the artificial light."
    "And I can see that her face is smeared with grease."
    "The mere sight of her is enough to make my cock harden."
    "Even if I could find a seat, I don't think that I could sit down properly!"
    "Kleio finally finishes the task and secures the winch."
    show kleio work a
    "Then she turns to face me, wiping her hands on a dirty rag."
    kleio.say "Don't worry about helping me out, Loverboy."
    show kleio punk
    kleio.say "I wouldn't want to ruin your manicure!"
    "She tosses the rag over her shoulder and crosses her arms over her chest."
    kleio.say "What the fuck are you staring at, huh?"
    show kleio annoyed
    kleio.say "You never seen a mechanic at work before?"
    mike.say "Y...yeah, Kleio..."
    mike.say "But not one that looked like you!"
    "For a moment I think I've said the wrong thing."
    "I'm expecting Kleio to call me a sexist pig."
    "Or maybe even to throw something heavy in my direction."
    "But much to my relief, she bursts out laughing."
    kleio.say "That is SO cute, Loverboy!"
    show kleio seductive
    kleio.say "You're like one of those helpless little women, you know?"
    kleio.say "The ones they used to have in ads, lusting over manly men!"
    mike.say "Hey!"
    mike.say "I am a manly man!"
    kleio.say "Sure you are, Loverboy!"
    show kleio normal
    kleio.say "You don't know how hot I get thinking about you behind that desk!"
    kleio.say "Your bulging biceps pushing all those sheets of paper around!"
    kleio.say "Oh no, I think I'm going to lose control!"
    mike.say "Stop it, Kleio!"
    mike.say "Okay, I admit it - your job is more macho than mine!"
    "Kleio chuckles and shakes her head."
    "Then she walks over to where I'm standing."
    "She wraps her arms around my neck and leans in close."
    show kleio happy
    kleio.say "I'm just fucking with you, Loverboy!"
    kleio.say "The thought of your job isn't what's been on my mind all day."
    kleio.say "But what has is the thought of you..."
    hide kleio
    show kleio kiss work
    with fade
    $ kleio.flags.kiss += 1
    "Kleio kisses me, full on the lips and with passion."
    "In that moment I forget everything she's said to me."
    "And the only thing that seems to matter is kissing her back."
    "At the same time, Kleio guides my hands to begin undressing her too."
    "It doesn't take me long to strip her down to her underwear."
    "And Kleio returns the favour, undressing me as well."
    "I keep my lips pressed against Kleio's as she walks backwards."
    "She only stops when she backs into the front bumper of a car."
    "But then she scrambles up and onto the hood."
    "Together we tear off the last of her clothes."
    "And then Kleio leans back on the car, panting heavily."
    scene kleio missionary with fade
    kleio.say "You'd better fuck me good and hard, Loverboy!"
    kleio.say "Good and hard, you hear me?"
    "I nod eagerly, panting just like Kleio."
    "My cock's good and hard, ready to give the lady what she wants!"
    "Kleio smiles, parting her legs and grabbing hold of her ankles."
    "She's practically offering herself up to me right now!"
    show kleio missionary mike
    menu:
        "Fuck her pussy":
            "I'm not going to over-think things here, oh no!"
            "Kleio's pussy is right there in front of me."
            "And from the look of it, ripe for the taking too!"
            "So that's exactly where I aim for..."
            call check_condom_usage (kleio, love=180, drinks=3) from _call_check_condom_usage_67
            if _return == False:
                return "leave_without_gain"
            show kleio missionary vaginal
            if CONDOM:
                show kleio missionary vaginal condom
            "Kleio stares downwards, wide-eyed as I push my cock against her lips."
            "She gasps as the head begins to slip between them, a little at a time."
            "There's resistance at first, enough to spur me on to push harder."
            "But all too soon I feel the inevitable happen, and she surrenders to me."
            kleio.say "Mmm..."
            kleio.say "Oh yeah..."
            kleio.say "That's what I want!"
            kleio.say "I've been waiting for this all day!"
            "Kleio's words are music to my ears, letting me know that she's loving this."
            "But it's not like I need any kind of encouragement right now."
            "Just the sensation of my cock sinking into her is enough to spur me on."
            show kleio missionary vaginal pleasure
            "I keep on going, as deep as I can possibly get."
            "But once I'm there, I don't stop to savour the feeling."
            "Instead I launch straight into it, moving in and out."
            "My speed builds quickly too, increasing by the second."
            "Soon Kleio is clinging onto me as if for dear life."
            show kleio missionary flirt
            "She's moaning and crying out as I pound her."
            "And I'm not holding back, but rather going as hard as I can."
            "Kleio doesn't seem to mind either, taking all I can give her."
            "She lies back on the hood of the car, offering no resistance."
            "In fact I realise that she's nodding, actually asking for more!"
            show kleio missionary blush sweat
            "I nod in response, already redoubling my efforts."
            "Kleio begins to cry out even more as I use the rest of my strength."
            "The sound gets ever louder as I thrust in and out of her."
            "I'm not thinking about where we are or how loud we're being."
            "Hell, I don't even care if we leave the shape of her buttocks pressed into the hood of the car!"
            "All that matters is hammering Kleio as hard as I possibly can."
            kleio.say "Th...that's it..."
            kleio.say "Fuck me...Loverboy..."
            show kleio missionary pleasure
            kleio.say "Make...me...cum!"
            mike.say "Oh fuck..."
            mike.say "Here it comes!"
            call cum_reaction (kleio, 'vaginal', 5) from _call_cum_reaction_97
            if _return == "vaginal_outside":
                "At the last moment possible, I remember that we didn't use a condom."
                "And that sends me into a desperate struggle to pull out before it's too late."
                show sexinserts chest kleio zorder 1 at center, zoomAt(1, (710, 740))
                show sexinserts belly kleio as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                show kleio missionary -vaginal
                "Kleio seems to take my efforts as just part of me finishing her off."
                "And luckily for me it also seems to push her over the edge too."
                show kleio missionary cumshot with vpunch
                "She cums as I finally pull my cock out of her and shoot my load."
                show sexinserts chest kleio cum zorder 1 at center, zoomAt(1, (710, 740))
                show sexinserts belly kleio cum as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                with vpunch
                "It rains down on Kleio's belly in spurts, painting her skin with sticky white stripes."
                with vpunch
                "As soon as I'm spent, I fall forwards onto the hood of the car."
                "And Kleio wraps her arms and legs around me, holding me against her."
                $ kleio.love += 1
                hide sexinserts
                hide bellycum
            elif _return == "vaginal_condom":
                "I grab hold of Kleio and thrust myself into her one last time."
                "The fact we used a condom means there's no danger in me doing so."
                "And I can instantly see the pleasure that this gives to Kleio too."
                "She nods desperately as I shoot my load into her, eyes wide with the sensation."
                "As soon as I'm spent, I fall forwards onto the hood of the car."
                "And Kleio wraps her arms and legs around me, holding me against her."
                "But also keeping me inside of her as she cums too."
                $ kleio.love += 1
            elif _return == "vaginal_inside_pill":
                kleio.say "Do it, Loverboy!"
                kleio.say "Cum in me!"
                kleio.say "I'm on the pill, remember?!?"
                "I grab hold of Kleio and thrust myself into her one last time."
                "The fact that she's on the pill means there's no danger in me doing so."
                "And I can instantly see the pleasure that this gives to Kleio too."
                show kleio missionary creampie ahegao with vpunch
                $ kleio.love += 2
                "She nods desperately as I shoot my load into her, eyes wide with the sensation."
                with vpunch
                "As soon as I'm spent, I fall forwards onto the hood of the car."
                with vpunch
                "And Kleio wraps her arms and legs around me, holding me against her."
                "But also keeping me inside of her as she cums too."
            elif _return == "vaginal_inside_pregnant":
                kleio.say "Do it, Loverboy!"
                kleio.say "Cum in me!"
                kleio.say "You already knocked me up!"
                "I grab hold of Kleio and thrust myself into her one last time."
                "The fact that she's pregnant means there's no danger in me doing so."
                "And I can instantly see the pleasure that this gives to Kleio too."
                show kleio missionary creampie ahegao with vpunch
                $ kleio.love += 3
                "She nods desperately as I shoot my load into her, eyes wide with the sensation."
                with vpunch
                "As soon as I'm spent, I fall forwards onto the hood of the car."
                with vpunch
                "And Kleio wraps her arms and legs around me, holding me against her."
                "But also keeping me inside of her as she cums too."
            elif _return == "vaginal_inside_mad":
                kleio.say "Y...you have to pull out!"
                kleio.say "You have to - NOW!"
                "I don't know if it's Kleio's words that do it."
                "Or if it's just that we already left it too late."
                "Either way, the result is the same."
                show kleio missionary creampie with vpunch
                $ kleio.impregnate()
                $ kleio.love -= 5
                "She shakes her head as I shoot my load into her, eyes wide with the sensation."
                with vpunch
                "As soon as I'm spent, I fall forwards onto the hood of the car."
                with vpunch
                "Kleio pushes against me, trying to separate us."
                "But the damage has already been done."
                "What in the hell did I just do?"
                "And what are the consequences going to be too?"
            elif _return == "vaginal_inside_happy":
                "At the last moment possible, I remember that we didn't use a condom."
                "And that sends me into a desperate struggle to pull out before it's too late."
                "But as soon as I start to do so, Kleio wraps her arms and legs around me!"
                kleio.say "Do it, Loverboy!"
                kleio.say "Cum in me!"
                "I don't know if it's Kleio holding onto me that does it."
                "Or if it's the genuine shock at hearing her say those words."
                "Either way, the result is the same."
                show kleio missionary creampie ahegao with vpunch
                $ kleio.impregnate()
                $ kleio.love += 5
                "She nods desperately as I shoot my load into her, eyes wide with the sensation."
                with vpunch
                "As soon as I'm spent, I fall forwards onto the hood of the car."
                with vpunch
                "And Kleio wraps her arms and legs around me, holding me against her."
                "But also keeping me inside of her as she cums too."
                "I hardly notice as my mind is already racing."
                "What in the hell did Kleio just do?"
                "And what are the consequences going to be too?"
        "Fuck her ass":

            "I love getting into situations like this with Kleio."
            "She comes up with the craziest places to do it."
            "And that makes me feel like I have to get crazy too."
            "Which is why I part her thighs that little bit more."
            "And why I aim the head of my cock a little bit lower too!"
            kleio.say "Whoa, Loverboy..."
            kleio.say "Where'd you think you're going?"
            mike.say "You just wait and see!"
            show kleio missionary anal
            "Kleio shakes her head as I begin to push my cock into her ass."
            "And then her eyes go wide as she feels what I'm trying to do."
            "For a moment I think she's going to tell me to stop."
            "But then she laughs and nods her head."
            kleio.say "You've got some balls, Loverboy!"
            kleio.say "I'll give you that!"
            "I give her a wry smile in response."
            "And then I push as hard as I dare."
            show kleio missionary pleasure
            "Instantly Kleio's expression changes."
            "She closes her eyes and lets out a deep moan."
            "At the same time I can feel the way her muscles are trying to resist me."
            "They're squeezing my cock tight, but that doesn't stop me for an instant."
            "The sensation is more thrilling than anything else, making me try even harder."
            "Slowly, Kleio's muscles surrender to me, and I sink ever deeper."
            kleio.say "Oh fuck..."
            kleio.say "That feels good..."
            show kleio missionary blush sweat
            kleio.say "Give me some more of that!"
            "Eager to give Kleio what she wants, I start moving inside of her."
            "There's no time to savour the sensation or pause before we're at it."
            "Instead I find myself rushing to satisfy her with everything I have."
            "Kleio lays back on the hood of the car, abandoning herself to the experience."
            "She's panting and sighing most of the time, but still urging me on!"
            kleio.say "Mmm..."
            kleio.say "Oh yeah..."
            kleio.say "That's what I want!"
            kleio.say "I've been waiting for this all day!"
            "All of this feels pretty incredible from where I'm standing."
            "But there's a stubborn part of me that's more interested in proving myself to Kleio."
            "And that means I'm going to keep right on pounding her as hard as I can."
            "I'm not going to stop until she's been completely satisfied."
            "Hell, I don't even care if we leave the shape of her buttocks pressed into the hood of the car!"
            "All that matters is hammering Kleio as hard as I possibly can."
            "Every thrust brings me closer to that goal."
            "Every gasp from Kleio tells me that I'm getting close."
            "Her eyes are open now, and she's urging me on!"
            kleio.say "Th...that's it..."
            kleio.say "Fuck me...Loverboy..."
            show kleio missionary pleasure
            kleio.say "Make...me...cum!"
            mike.say "Oh fuck..."
            mike.say "Here it comes!"
            call cum_reaction (kleio, 'anal', 5) from _call_cum_reaction_98
            if _return == 'anal_inside':
                "I grab hold of Kleio and thrust myself into her one last time."
                "I can instantly see the pleasure that this gives to Kleio too."
                show kleio missionary creampie ahegao with vpunch
                "She nods desperately as I shoot my load into her, eyes wide with the sensation."
                with vpunch
                "As soon as I'm spent, I fall forwards onto the hood of the car."
                with vpunch
                "And Kleio wraps her arms and legs around me, holding me against her."
                "But also keeping me inside of her as she cums too."
                $ kleio.sub += 2
            elif _return == 'anal_outside':
                show sexinserts chest kleio zorder 1 at center, zoomAt(1, (710, 740))
                show sexinserts belly kleio as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                "At the last moment possible, I pull out before it's too late."
                "Kleio seems to take my efforts as just part of me finishing her off."
                show kleio missionary -anal
                "And luckily for me it also seems to push her over the edge too."
                show kleio missionary cumshot with vpunch
                "She cums as I finally pull my cock out of her and shoot my load."
                show sexinserts chest kleio cum zorder 1 at center, zoomAt(1, (710, 740))
                show sexinserts belly kleio cum as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                with vpunch
                "It rains down on Kleio's belly in spurts, painting her skin with sticky white stripes."
                with vpunch
                "As soon as I'm spent, I fall forwards onto the hood of the car."
                "And Kleio wraps her arms and legs around me, holding me against her."
                hide sexinserts
                hide bellycum
                $ kleio.sub += 1
            $ kleio.flags.anal += 1
    $ kleio.sexperience += 1
    if kleio.lesbian > MIN_LES_GIRL_SEX:
        $ kleio.lesbian -= 1
    return

label kleio_studio_bj:
    "There's only Kleio and me in the practice room right now."
    "Sasha and Anna left the studio for a while, doing... then whatever Sash and Anna needed to do."
    "And I'm just taking the time to set up my amp and practice a bit."
    "That's when I hear the sound of cursing from the other side of the room."
    show kleio angry bbis
    kleio.say "Argh..."
    kleio.say "Dammit!"
    "I look up to see Kleio frowning and shaking her head."
    mike.say "What's up, Kleio?"
    mike.say "You okay over there?"
    "At the sound of my voice, Kleio eyeballs me."
    "Then she hurries over to where I'm setting up."
    show kleio annoyed bbis
    kleio.say "My voice is pretty fucked, Loverboy!"
    kleio.say "Dunno why, but it is."
    mike.say "Huh...that sucks."
    mike.say "You want to cancel practice for tonight?"
    "Kleio looks annoyed at the very suggestion."
    "She shakes her head."
    show kleio normal
    kleio.say "Nah."
    kleio.say "I just need something to soothe my throat."
    kleio.say "Something warm and thick, you know?"
    "A moment later, I see a sly smile spread across her face."
    show kleio seductive
    kleio.say "And I think I know just the thing..."
    "Kleio doesn't give me a chance to react."
    "Instead she grabs my groin with one hand."
    "And with the other, she shoves me up against my amp."
    mike.say "Wha..."
    mike.say "What are you..."
    "But even as I'm spluttering out the question, Kleio's already moving."
    "She crouches down in front of me, pulling my flies open."
    "Then she shoves a hand into my pants, yanking my cock out."
    kleio.say "There you are!"
    show kleio happy
    kleio.say "Come to Kleio!"
    "I open my mouth to protest."
    "But then the words die in my throat."
    "What in the hell am I objecting for?"
    "My kick-ass, punk-bitch girlfriend's decided that she wants my cock."
    "What could be less rock and roll than trying to stop her?"
    "So instead I lean back against the amp and let Kleio have her way."
    "At the same time trying to dwell on just how good this is going to feel."
    "And not the fact that Sasha and Anna could walk in on us any moment!"
    kleio.say "Come on, Loverboy..."
    show kleio annoyed
    kleio.say "I need you good and hard!"
    "Kleio smiles up at me as she says this."
    "And when I look down at her, she shoots me a wink."
    scene kleio bj
    show kleio bj casual
    with fade
    "Then she opens her mouth and sticks out her tongue."
    "She closes her eyes as she licks the head."
    "And the sounds she makes as she does so ensure I'm soon good and hard."
    show kleio bj lick
    show sexinserts head kleio zorder 1 at center, zoomAt(1, (720, 810))
    "Which is exactly what Kleio wants."
    "There's no time for teasing and beating around the bush here."
    "So she simply swallows the head and begins to work it with her tongue."
    show kleio bj suck
    "And pretty soon I'm not just pressed up against my amp."
    "I'm actually using it for support as Kleio's efforts intensify."
    "It's not the technique that's doing it."
    "But instead the hunger with which she's sucking my cock."
    "Kleio moans and gasps like she needs it so badly."
    "At times even sounding like she's gagging for breath."
    "All the while she won't ease up for a moment."
    show kleio bj deep
    pause 0.25
    show kleio bj suck
    "Her head bobs up and down as she takes me ever deeper."
    "And I swear that I can see one of her hands pushing into her shorts."
    "The mere thought of Kleio playing with herself right now is so hot."
    show kleio bj deep
    pause 0.25
    show kleio bj suck
    "It almost makes me shoot my load straight away."
    show kleio bj deep
    pause 0.25
    show kleio bj suck
    "As if sensing the urge in me, Kleio bites down on my cock."
    "It's not enough to hurt, just a playful nibble."
    show kleio bj deep
    pause 0.25
    show kleio bj suck
    pause 0.25
    show kleio bj deep
    pause 0.25
    show kleio bj suck
    "And I look down to see her raise her eyebrows at me."
    "I nod, guessing that she's telling me to hold on for something."
    show kleio bj deep at startle(0.05,-10)
    pause 0.25
    show kleio bj suck
    pause 0.25
    show kleio bj deep
    pause 0.25
    show kleio bj suck
    "And I don't have to wait long for my reward either."
    "Kleio squeezes my balls, good and hard."
    "But at the same time she does something to my cock in her mouth."
    show kleio bj deep at startle(0.05,-10)
    pause 0.25
    show kleio bj suck
    pause 0.25
    show kleio bj deep at startle(0.05,-10)
    pause 0.25
    show kleio bj suck
    "I have no idea what it is, just that if feels amazing."
    "That and the fact it makes me begin to cum a second later."
    "So it wasn't the orgasm that was the issue."
    show kleio bj deep at startle(0.05,-10)
    pause 0.25
    show kleio bj suck
    pause 0.25
    show kleio bj deep at startle(0.05,-10)
    pause 0.25
    show kleio bj suck
    pause 0.25
    show kleio bj deep at startle(0.05,-10)
    pause 0.25
    show kleio bj suck
    "It was just that I wasn't supposed to cum until Kleio wanted me to!"
    menu:
        "Cum on her face":
            "As I feel myself losing it, Kleio pulls her head back."
            show kleio bj lick
            "She leans at an angle that puts her in just the right position."
            show kleio bj facial cumshot with vpunch
            "Then she smiles as I shoot my load over her face."
            show sexinserts head kleio cum zorder 1 at center, zoomAt(1, (720, 810))
            with vpunch
            "I see that she has her mouth wide open, catching as much as she can."
            show kleio bj facial -cumshot dickcum with vpunch
            "And anything that lands around her lips, she laps up with her tongue too."
            $ kleio.love += 1
        "Cum in her mouth":
            "As I feel myself losing it, Kleio takes me cock as deep into her mouth as she can."
            show sexinserts head kleio cum zorder 1 at center, zoomAt(1, (720, 810))
            show kleio bj deep cum
            with vpunch
            "At first I'm worried that she's going to choke."
            with vpunch
            "But as I shoot my load down her throat, Kleio goes into action."
            with vpunch
            "She controls the flow with some serious expertise."
            show kleio bj suck -cum
            show sexinserts head kleio -cum zorder 1 at center, zoomAt(1, (720, 810))
            "And I watch in amazement as she gulps down everything I have to give."
            $ kleio.sub += 1
    "Afterwards, Kleio gets to her feet, stretching like a satisfied cat."
    hide sexinserts
    hide kleio bj
    show kleio normal
    with fade
    "She smiles as she shoves my cock back into my pants, giving it a playful slap for good measure."
    kleio.say "Mmm..."
    kleio.say "That really hit the spot, Loverboy!"
    show kleio happy
    kleio.say "I can still feel it coating my throat!"
    "It's at that very moment Sasha and Anna come bustling into the room."
    show sasha casual normal at top_mostright
    show anna casual normal at right5
    with easeinright
    "They're talking about something or another that I can't make out."
    "And luckily there's no way they can see what we were just doing."
    "Kleio shoots me one more knowing glance."
    "Then she adds a wink for good measure before turning to greet them."
    "I follow her example, all the time still aching for more of the same from her."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
