init python:
    Event(**{
    "name": "lexi_home_date_weed_intro",
    "label": "lexi_date_home_weed_intro",
    "conditions": [
        IsTimeOfDay("evening", "night"),
        HeroTarget(IsRoom("date_livingroom")),
        PersonTarget("lexi",
            OnDate(),
            MinStat("love", 120),
            ),
        ],
    "music": "music/roa_music/alley.ogg",
    "chances": 5,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "lexi_date_mall_weed",
    "label": "lexi_date_mall_weed",
    "conditions": [
        HeroTarget(IsRoom("date_mall1"),),
        PersonTarget("lexi",
            OnDate(),
            MinStat("love", 120),
            ),
        ],
    "music": "music/roa_music/alley.ogg",
    "chances": 5,
    "do_once": True,
    "quit": False,
    })

label lexi_date_intro_valentine_male:
    lexi.say "Mmm..."
    show lexi happy
    lexi.say "Happy Valentine's day, [hero.name]."
    show lexi wink
    lexi.say "And I bet it never looked this good before, huh?"
    "Lexi wiggles her hips and shakes her chest at me."
    show lexi normal
    "And she's right, there's nothing much that looks as good as that!"
    mike.say "Oh yeah, Lexi!"
    mike.say "I've never had a valentine as hot as you before!"
    return

label lexi_date_intro_halloween_male:
    mike.say "Hey, Lexi - no Halloween costume?"
    "Lexi cocks her head on one side, chuckling to herself."
    "Then she waves a hand like she wants me to study her outfit."
    lexi.say "Yeah, [hero.name], check it out."
    show lexi wink
    lexi.say "I came as a hot girl that's out of your league!"
    mike.say "Ha, ha, Lexi!"
    mike.say "You should try doing stand-up."
    show lexi normal
    lexi.say "Ah, come on, [hero.name], don't get all butt-hurt!"
    lexi.say "We're supposed to be on a date, aren't we?"
    return

label lexi_date_intro_christmas_male:
    lexi.say "Mmm...Merry Christmas, [hero.name]!"
    "I can't help hearing the hunger in Lexi's voice."
    "And I recognise the way she's looking at me right now."
    mike.say "Same to you, Lexi."
    mike.say "You're looking a little...hungry!"
    "Lexi nods, already eyeing me up."
    lexi.say "Oh yeah...this time of year always makes me feel...hungry!"
    return

label lexi_date_intro_birthday_male:
    mike.say "Happy birthday, Lexi!"
    show lexi surprised
    show fx question
    lexi.say "Huh?!?"
    lexi.say "Who's birthday is it supposed to be?"
    mike.say "Erm...yours, Lexi."
    mike.say "At least this is the day you told me it was on."
    lexi.say "I did?"
    show lexi annoyed
    lexi.say "Hmm...I have trouble remembering the actual date."
    show lexi happy
    lexi.say "But who cares, right?"
    show lexi normal
    lexi.say "Today is as good as any other day to celebrate!"
    return

label lexi_date_intro_mc_birthday_male:
    show lexi happy
    lexi.say "Happy birthday, [hero.name]!"
    lexi.say "We got to have some serious fun, yeah?"
    lexi.say "Like, we got to celebrate and stuff!"
    mike.say "Thanks, Lexi!"
    mike.say "I wasn't sure you'd remember."
    show lexi normal
    lexi.say "Oh, trust me - I never forget an excuse to party!"
    return

label lexi_date_eat_a_burger:
    "Lexi wastes no time, practically grabbing her burger the moment that it arrives."
    "She proceeds to tear through it as if she doesn't know when she'll get to eat again."
    "Watching her go, I really don't know whether to be impressed or concerned!"
    return

label lexi_date_buy_drink:
    if lexi.is_visibly_pregnant:
        show lexi angry
        $ lexi.love -= 10
        lexi.say "Hey, my mom drank while she was having me."
        lexi.say "And some people said it made me turn out bad!"
        lexi.say "I want things to be different for our kid."
        $ hero.cancel_activity()
        hide lexi
    else:
        "Drink in one hand and the other waving about in the air, Lexi is constantly either sipping or chattering."
        "And in between doing one and then the other, she pauses only to take in great gulps of air."
        "Try as I might, I can't seem to get a word in edgeways."
    return

label lexi_date_play_darts:
    "What Lexi lacks in skill when it comes to playing darts, she more than makes up for in enthusiasm."
    "Every time she manages to as much as hit the board with one of her throws seems to be cause for a celebration."
    "She jumps up and down on the spot, pumping her fist into the air with an unlit cigarette hanging from her lip."
    "A regular image of feminine grace..."
    return

label lexi_date_pub_play_pool:
    "While she seems really eager for a game of pool, I don't know if Lexi's actually that interested in actually playing."
    "Sure, she takes her shots and sinks a few balls here and there."
    "But she seems to take fare more pleasure in leaning on the table in whatever provocative pose she can pull off."
    return

label lexi_date_buy_a_round:
    if lexi.is_visibly_pregnant:
        show lexi angry
        $ lexi.love -= 10
        lexi.say "Hey, my mom drank while she was having me."
        lexi.say "And some people said it made me turn out bad!"
        lexi.say "I want things to be different for our kid."
        $ hero.cancel_activity()
    elif (hero.charm >= 60 - lexi.love and lexi.flags.drinks < 2):
        show drink lexi
        "At the mere mention of my buying another round, Lexi's up out of her seat and literally bouncing around."
        "She looks far too happy for someone that's simply been told that their next drink is on the way."
        "It makes me wonder just how much more energy she can have and how long she can keep this up!"
        $ game.active_date.score += 5
        if "rebel" in lexi.traits:
            $ game.active_date.score += 5
        $ lexi.set_flag("drinks", 1, "day", mod="+")
        hide drink
    else:
        "I want to pay a round of beers to the whole pub."
        "But Lexi doesn't seem to want to drink, so I refrain from doing so."
        $ hero.cancel_activity()
    return

label lexi_dance_with:
    "There's nothing subtle or chaste about Lexi, and this shows on the dance-floor."
    "Within moments, she's shaking her ass in my general direction and flaunting herself like a piece of meat."
    "And a very appealing one at that, as she encourages me to reach out and touch what's on offer!"
    return

label lexi_date_play_arcade_intro_male:
    lexi.say "Whoa..."
    lexi.say "This place is dark, dingy and the carpet's sticky."
    lexi.say "And you say that I take YOU to some dives, [hero.name]!"
    "I tear my attention away from the games for a moment."
    "Long enough for what Lexi just said to fully sink in."
    mike.say "Hey!"
    mike.say "This place is about playing the games and having fun, Lexi."
    mike.say "It's not about the decor!"
    lexi.say "Yeah, well..."
    lexi.say "I still say you can play games that are more fun where I take you!"
    "It's then that Lexi's ears perk up."
    "And she looks around her with interest."
    lexi.say "Hey, I recognise that laugh!"
    "She hurries over to one of the nearby arcade cabinets."
    "Just as she reaches it, the laugh can be heard again."
    lexi.say "Wow..."
    lexi.say "This is going to sound crazy, [hero.name]."
    lexi.say "But that sounds just like a guy I used to know."
    lexi.say "And the guy on the screen looks like him too!"
    mike.say "That's 'Futile Fight', Lexi."
    mike.say "It's a classic beat-em-up."
    "Lexi watches in fascination as the demo for the game plays."
    "She shakes her head the whole time, as if amazed."
    lexi.say "I know all of these guys - the ones getting beaten up!"
    lexi.say "Or at least guys like them."
    lexi.say "I must have dated them all one time or another!"
    "I try to ignore the implications of what Lexi just said."
    "And I begin to feed coins into the slot instead."
    mike.say "Come on, Lexi."
    mike.say "Let's give this one a whirl..."
    return

label lexi_date_play_arcade_win_male:
    "Sure, Lexi might claim to recognise the characters."
    "But that doesn't translate into her being any good at the game."
    "Whereas I, on the other hand, happen to be VERY good at it."
    lexi.say "Hey!"
    lexi.say "That guy just punched me in the gut!"
    lexi.say "That'd never happen in real life."
    lexi.say "Guys like that are pussies!"
    mike.say "This isn't real life, Lexi!"
    mike.say "It's just a game, remember?"
    "Lexi shoots me a dirty look and mutters something under her breath."
    "But I'm too busy paying attention to what's happening onscreen."
    "We fight our way through slums, subway stations and factories."
    "And I'm cutting a swathe through wave after wave of enemies."
    "Thugs, punks and scum, all fall before my mighty fists."
    "Once it's all over, my score is way higher than Lexi's."
    lexi.say "Yeah, yeah, [hero.name]."
    lexi.say "So you won - big deal."
    lexi.say "You'd have turned tail and run from those guys in real life!"
    mike.say "But what about you, Lexi?"
    mike.say "Did you have fun?"
    lexi.say "Yeah..."
    lexi.say "I guess it was okay!"
    return

label lexi_date_play_arcade_lose_male:
    "Somehow Lexi claiming to recognise the characters seems to affect how she plays."
    "She's never played the game before in her entire life."
    "But she picks it up in seconds and then plays like a natural!"
    mike.say "Hey!"
    mike.say "I had that guy in my sights, Lexi!"
    mike.say "And stop stealing all the best power-ups too!"
    "Lexi sniggers and shakes her head."
    lexi.say "You can't handle guys like these, [hero.name]."
    lexi.say "Just leave them to me!"
    mike.say "Handling more than one guy at once, Lexi?"
    mike.say "In guess you'd know all about that!"
    lexi.say "What was that, [hero.name]?!?"
    mike.say "Ah...nothing, Lexi, nothing!"
    "Lexi shoots me a dirty look and mutters something under her breath."
    "But I'm too busy paying attention to what's happening onscreen."
    "We fight our way through slums, subway stations and factories."
    "And she's cutting a swathe through wave after wave of enemies."
    "Thugs, punks and scum, all fall before her mighty fists."
    "Once it's all over, my score is way lower than Lexi's."
    mike.say "Well..."
    mike.say "It's only a game!"
    lexi.say "You're damn lucky it was, [hero.name]."
    lexi.say "You'd have turned tail and run from those guys in real life!"
    mike.say "But what about you, Lexi?"
    mike.say "Did you have fun?"
    lexi.say "Yeah..."
    lexi.say "I guess it was okay!"
    return

label lexi_date_swim_pool_home_male:
    $ game.active_date.clothes = "swimsuit"
    if lexi.sub < 25:
        show playing water pool lexi
        "We go to the pool and play in the water."
        hide playing water pool lexi
    else:
        show lexi swimsuit normal a
        "The weather's been pretty decent lately, warm days leading into cooler evenings."
        "So I've decided that we should take advantage of it while it lasts."
        "And rather than take Lexi out somewhere, we're hanging out by the pool at home."
        "I'm enjoying the chance to just chill out and take things slowly for a change."
        show lexi annoyed
        "But I kind of get the feeling Lexi's a little pissed."
        "She's sitting on the edge of the pool, kicking her legs in the water."
        mike.say "What's the matter, Lexi?"
        mike.say "We've got great weather."
        mike.say "And a private pool all to ourselves."
        mike.say "What's not to like?"
        "Lexi looks at me and lets out a little huff of frustration."
        lexi.say "I'm bored, [hero.name]!"
        lexi.say "I wanna do something fun."
        lexi.say "Not just sit around all day!"
        "I can't help frowning and shaking my head."
        mike.say "The view looks pretty good from over here, Lexi."
        mike.say "I could stare at it for hours!"
        "I pull down my sunglasses and raise an eyebrow."
        "But at first, Lexi doesn't seem to get my meaning."
        "When she finally realises I'm talking about her, she lets out a snorting laugh."
        show lexi normal
        lexi.say "Aw, [hero.name]!"
        lexi.say "You don't need to be by the pool to see me in my swimsuit."
        lexi.say "You can see me in even less if you want to, anytime!"
        "I'm relieved that we're both smiling now."
        "But I still shake my head."
        mike.say "I don't know, Lexi..."
        mike.say "There's just something about the sight of girl in a bikini at poolside."
        mike.say "Mmm...you know what I mean?"
        "Lexi giggles and kicks her legs together in the water."
        lexi.say "I always wanted to be a mermaid when I was a kid."
        show lexi wink
        lexi.say "I could be your little mermaid if you like?"
        "Lexi winks at me, pulling her legs out of the pool."
        "Then she reclines and does her best impression of a sultry siren."
        mike.say "I think mermaids are a little more innocent and pure than you, Lexi!"
        mike.say "You're not exactly fairy-tale material!"
        lexi.say "Hey!"
        show lexi annoyed
        lexi.say "Don't be mean!"
        lexi.say "I'll show you the kind of mermaid I'd make."
        lexi.say "Much better than the kind in some dumb fairy-tale!"
        "I watch as Lexi remove her swimsuit and slips into the water."
        show lexi naked flirt
        "Watching her swimming towards me, I have to admit, she does look damn good in the water."
        "The way it runs off the curves of her body."
        "Not to mention how her breasts float in the water too!"
        "As she reaches me, Lexi pushes my legs apart and swims between them."
        lexi.say "Let's start by getting rid of these!"
        "Lexi grabs the waistband of my trunks as she says this."
        scene lexi bj
        show lexi bj pool naked nopants
        "Then she pulls them down my legs, tossing them aside."
        "I don't do a thing to stop her, enjoying the treatment."
        "And as soon as she has me naked, Lexi makes a grab for my cock."
        lexi.say "Mmm..."
        lexi.say "There it is!"
        "She leans in closer, closing her eyes as she opens her mouth."
        "Then Lexi begins to lick and caress, devoting herself to the task."
        "All I have to do is lie back and let her have her way with me."
        "Lexi soon has my cock as hard as it can be."
        "She uses her hands to stroke the parts her mouth isn't touching."
        "Switching between the two with an ease that comes only with practice."
        "I guess my earlier comments really got under Lexi's skin."
        show lexi bj suck
        "Now she's determined to show me what she can really do."
        "And I've got to say, she's already impressing the hell out of me!"
        show lexi bj deepthroat
        "I already feel like I'm clinging onto the edge of the pool for dear life."
        "On top of that I'm gasping and moaning like I'm starting to hyperventilate!"
        show lexi bj suck closed
        "Lexi's head is going up and down."
        show lexi bj deepthroat
        "But she pauses for a brief moment, just long enough to gaze up at me."
        show lexi bj deepthroat open
        "And when she does so, I see the glint of pure mischief in her eyes."
        "Oddly that sends a jolt of excitement through my body I actually feel."
        mike.say "Oh fuck!"
        mike.say "Lexi..."
        mike.say "What are you..."
        "At the sound of my voice, Lexi doesn't pause or hesitate."
        show lexi bj suck closed
        "In fact she seems to redouble her efforts."
        "Her head moves faster, her tongue and lips caress even more."
        show lexi bj deepthroat
        "And I can feel myself beginning to be overwhelmed by what she's doing to me."
        "In a rare moment of clarity, I realise what's happening right now."
        "Lexi's not pushing herself at all."
        show lexi bj suck
        "In fact, she was holding back before now!"
        "I feel like I'm going to collapse any second."
        "Like I couldn't move if I tried."
        "I guess I was wrong about Lexi being mermaid material."
        show lexi bj deepthroat
        "Because she's actually a siren."
        "The kind that's lure a guy to his death!"
        mike.say "Lexi..."
        mike.say "I'm gonna..."
        show lexi bj suck open
        mike.say "I'm gonna cum!"
        menu:
            "Cum on her face":
                "I have no idea if Lexi even heard what I just said."
                "That is until I feel the sensation of her letting me go."
                show lexi bj -suck smile
                "Lexi gasps with satisfaction and tosses her head back."
                "But she makes sure that she's right in the firing line all the same."
                show lexi bj cum
                "So when I shoot my load, it hits her square in the face."
                show lexi bj facial smile
                "Lexi takes it all with a smile on her face."
                "And her expression is so joyful this could be a damn shampoo commercial."
                "The only difference is that her face is getting striped with cum right now!"
            "Cum in her mouth":
                "I have no idea if Lexi even heard what I just said."
                "That is until I feel the sensation of her bearing down on me."
                show lexi bj deepthroat open
                "Then I know exactly what she has in mind."
                "And all I can do is keep on gasping as she puts her plan into action."
                "Lexi takes me as deep as she possibly can, then she waits."
                "A moment later I begin to shoot my load straight down her throat."
                show lexi bj cum
                "An experienced pro, Lexi swallows it without pause or hesitation."
                "In fact she gulps it down with what looks like a genuine hunger."
                "Finally I feel the sensation of her letting me go."
                show lexi bj -deepthroat -cum smile
                "Lexi gasps with satisfaction and tosses her head back."
        scene bg pool
        show lexi naked happy
        lexi.say "Mmm..."
        lexi.say "That feels SO good!"
        "All I can do is nod, eyes wide and heart pounding."
        "Lexi's grinning from ear to ear, clearly enjoying the sight."
        lexi.say "So whadda yah think?"
        show lexi wink
        lexi.say "Am I mermaid material, or what?"
        mike.say "Whoa..."
        mike.say "Lexi..."
        mike.say "You could suck barnacles off a rock!"
        mike.say "Or the rivets off of a submarine!"
        show lexi happy
        "Lexi laughs out loud, then kicks herself off into the water."
        "She swims in what looks like little victory circle."
        "Making sure that I can see what's on show the whole time too!"
        $ lexi.love += 2
        $ game.active_date.score += 10
    $ game.active_date.clothes = None
    return

label lexi_dick_reactions:
    if not lexi.flags.seendick:
        $ lexi.flags.seendick = 1
        if hero.has_skill("hung"):
            show dick reactions lexi tasty
            lexi.say "Oh yeah - now THAT's what I'm talkin' about!"
            lexi.say "You come on and park that thing in me, right now!"
            mike.say "Ah...so, you like what you see?"
            lexi.say "Yeah, but I don't want to just look."
            lexi.say "I want that thing inside of me!"
            $ lexi.sub += 10
            $ lexi.love += 10
        elif hero.has_skill("smalldick"):
            show dick reactions lexi mock
            lexi.say "Whoops!"
            mike.say "Wha...what's wrong?"
            lexi.say "Nothing...nothing at all!"
            mike.say "It's too small, isn't it?"
            show dick reactions lexi smile
            lexi.say "No...oh no!"
            lexi.say "Just...just be sure to tell me when it's in there, okay?"
            $ lexi.sub -= 10
            $ lexi.love -= 10
        hide dick reactions
    return

label lexi_peeping_scene_male:
    "Walking out of my room I pass the door to the bathroom on my way downstairs."
    "I can hear the sound of the shower running inside, which is no big deal."
    "But what catches my attention is the steam around the door."
    "Normally that stuff stays inside of the bathroom."
    "That is unless..."
    "Stopping and taking a closer look, my suspicions are confirmed."
    "Someone left the bathroom door open while taking a shower."
    "Just a crack, but enough to let the steam out."
    "I take hold of the handle, meaning to shut the door."
    "But then a thought occurs to me."
    "I wonder who's in there right now?"
    "I know that I shouldn't be doing this."
    "And yet I can't help sneaking a quick peek around the door."
    "I'm not really snooping, just satisfying my natural curiosity, that's all."
    "But the moment I look inside, I can't tear my eyes away from what I see."
    "It's Lexi, I know it is!"
    "I can tell from the shape of the body in the shower cubicle."
    "I hardly need to catch a sight of her face to know that it's her."
    "And yeah, I know Lexi hardly tries to cover herself up most of the time."
    "But seeing her like this is somehow different, more intimate."
    "Even a little dangerous too!"
    "I can't seem to tear myself away from the crack in the door."
    "All I want to do is watch the water cascading down her body!"
    return

label lexi_peeping_reactions_male:
    if (lexi.love >= 150 or lexi.sub >= 50) and lexi.sexperience:
        show lexi naked nophone
        "But then I see her head snap up and turn towards the door."
        "What did I do?"
        "How did she know I'm out here?!?"
        show lexi naked happy
        lexi.say "Hey..."
        lexi.say "I know you're out there, [hero.name]!"
        lexi.say "And I know that you're watching me too."
        "I can hear something in Lexi's voice as she calls me out."
        "Something that reminds me of how sultry she can be."
        "It's already enough to make me start to get hard."
        if (lexi.love >= 180 or lexi.sub >= 70):
            lexi.say "You're so interested in me getting a shower, huh?"
            lexi.say "Then maybe you should help me get clean..."
            hide lexi
            show bg bathroom
            show lexi a naked nophone
            with hpunch
            play sound shower loop
            "Lexi grabs me by the wrist and yanks me into the bathroom."
            "Before I can protest, she's stripping off my clothes."
            "Then she shoves me into the shower cubicle."
            "The water's in my eyes and I struggle to see what's going on."
            "And that's how Lexi manages to hop into the shower with me."
            "I can feel that she's naked in an instant."
            show lexi close
            "Her body presses against mine, already wet and slippery."
            "I feel her shove the shower-gel into my hand."
            lexi.say "There you go - now make with the lather!"
            show lexi wink
            lexi.say "And you'd better do a good job too!"
            show lexi b flirt
            "What else can I do?"
            "I squeeze the shower-gel onto my hands."
            "And then I get to work."
            "Lexi has her back to me, and I take full advantage."
            "Sure, I make sure to actually rub the later all over her body."
            "I spread it over her arms, legs and back."
            "But then it comes time to clean the more intimate areas."
            "And as you can imagine, I spend a lot more time on those!"
            "I soap Lexi's breasts, massaging them at the same time."
            "I know that her nipples are getting washed in the process."
            "But that doesn't stop me from pinching them whenever I get the chance."
            "Lexi giggles and gasps as I take full advantage of her."
            "She pushes herself against me, wriggling her ass into my groin."
            "I think she's trying to send me a message."
            "And it's a pretty clear one from where I'm standing!"
            "I move one of my hands downwards, over her belly."
            "From there I trace a line between her thighs."
            "Lexi's panting now, like she's desperate for more."
            "So I begin to stroke her with my fingers."
            scene lexi showersex
            show lexi showersex outside
            with fade
            "It takes no more than a few seconds for her to reach down and grab them."
            "And then Lexi practically forces them into her pussy!"
            show lexi showersex vaginal -outside
            lexi.say "Mmm..."
            lexi.say "I'm all nice and clean now."
            lexi.say "And you did such a good job, [hero.name]."
            lexi.say "So your rewards is to help me get dirty again!"
            "I feel Lexi grab hold of my cock with her free hand."
            "She's aiming it where she wants it."
            "And I grab her ass, making sure it hits the spot."
            "The water and the later mean that we slip and slide."
            "But then we find the sweet spot, and I sink into Lexi's pussy."
            "What follows isn't a long, agonising session of Hollywood sex."
            "Lexi's already begging to be fucked."
            show lexi showersex vaginal pleasure
            "And I'm desperate to give her what she wants too."
            "For a while we're locked together, her back against my belly."
            "Lexi grinds herself on me, using all of her weight to ride my cock."
            "I'm forced to hold onto her and try to keep us upright."
            "Which means that I have to let her do most of the hard work."
            "But that doesn't mean I'm not enjoying the experience."
            "I get to stand there and let Lexi use me for her own gratification."
            "And every time she slaps her buttocks into my thighs, it feels like heaven!"
            "It doesn't take long for her to bring me off."
            "And when she does, I lean forwards, pressing her against the wall."
            "Only now do I begin thrusting into Lexi."
            show lexi showersex vaginal creampie with hpunch
            "I cum as I do this, making sure she takes all I have to give."
            "Her orgasm hits just as I'm done, and I hold her tightly as it happens."
            show lexi showersex vaginal ahegao
            "This means I get to enjoy the sensation of her quivering on the end of my cock."
            "Lexi's panting and gasping."
            "But I can just make out words in those sounds."
            hide lexi showersex
            show bg bathroom
            show lexi naked happy nophone
            with fade
            lexi.say "Y...you did good..."
            lexi.say "Cleaned me..."
            lexi.say "Inside and out!"
            stop sound fadeout 1.0
        else:
            hide lexi
            show bg bathroom
            show lexi a naked nophone
            with fade
            play sound shower loop
            lexi.say "It's okay, you don't have to say a word."
            lexi.say "You can just watch me if you like."
            lexi.say "I love it when someone watches me..."
            show lexi b
            "As if to make her point, Lexi reaches up and cups her breasts."
            "She squeezes them with her fingers, tips pinching her nipples."
            "And then she reaches down with one hand."
            "The fingers travel down her belly."
            "Then they disappear between her thighs."
            show lexi c wink
            lexi.say "Mmm..."
            lexi.say "I'm slick as hell, [hero.name]!"
            show lexi blush
            lexi.say "Thinking about how hard you must be right now."
            lexi.say "Thinking how you'd feel inside of me..."
            show lexi flirt
            "Lexi moans and gasps as she plays with herself."
            "And she's right too - I'm rock hard!"
            "It's all I can do to keep my hand off of it."
            lexi.say "Ah...[hero.name]..."
            lexi.say "I'm gonna...gonna cum!"
            "I watch as Lexi leans against the wall of the shower cubicle."
            "Then she slowly slides downwards, like she just can't stand up anymore."
            stop sound fadeout 1.0
            scene bg bedroom1 with fade
            "Scared of being discovered like this, I scurry back to my bedroom."
            "My cock still hard and my head full of desire for Lexi."
            $ game.room = "bedroom1"
        $ lexi.love += 1
        $ lexi.sub += 1
    else:
        show lexi naked nophone annoyed
        "But then I see her head snap up and turn towards the door."
        "What did I do?"
        "How did she know I'm out here?!?"
        show lexi angry at center, hshake
        lexi.say "Hey?"
        lexi.say "What the hell?!?"
        show fx anger
        "Before I can straighten up and turn around, she's onto me."
        "Lexi barrels out of the shower cubicle."
        hide lexi
        show lexi close naked nophone annoyed
        "She grabs a towel as she comes, wrapping herself in it."
        "And then she shoves the door open to confront me."
        $ lexi.love -= 20
        $ lexi.sub -= 5
        show lexi angry
        lexi.say "[hero.name]!"
        lexi.say "You fucking sleaze!"
        mike.say "Whoa, Lexi!"
        mike.say "This isn't what it looks like!"
        lexi.say "Don't give me that shit."
        lexi.say "You were perving on me in the shower!"
        "Lexi pokes me in the chest with a finger."
        lexi.say "You might have let me move in here as a favour, [hero.name]."
        lexi.say "But that doesn't mean I'm some kind of live-in wank-fantasy, yeah?"
        lexi.say "I catch you doing that again, and I'll cut it off!"
        "And with that, Lexi turns on her heel and storms back into the bathroom."
        play sound door_slam
        pause 0.4
        scene bg door bathroom at center, zoomAt(1.25, (640, 880))
        with hpunch
        "The door slams closed behind her, and I hear it click shut too."
        "But oddly, I don't feel the need to check it this time..."
    return

label lexi_halloween_invitation:
    show lexi
    "There's no way we can celebrate Halloween at the house without inviting Lexi."
    "She's always the life and soul of the party wherever she goes."
    "And on top of that, it's going to be a costume party."
    "So I can't wait to see what she'll come dressed as!"
    "Any other girl and I might have felt the need to beat about the bush."
    "But this is Lexi we're talking about, and she's pretty laid back."
    "I'm sure she's going to be up for having some serious fun at my place."
    mike.say "Hey, Lexi..."
    mike.say "We're throwing a Halloween party at my place."
    mike.say "You want to come along, right?"
    "Lexi cocks her head on one side as she listens to my pitch."
    "And I can from the look in her eyes that she's interested."
    show lexi surprised
    lexi.say "A Halloween party?"
    lexi.say "Like with spooky stuff?"
    lexi.say "Bobbing for apples and shit?"
    "I nod eagerly, wanting to sell her on the idea."
    mike.say "That's right, Lexi."
    mike.say "And costumes too."
    mike.say "Would you like to come?"
    mike.say "Maybe as my date?"
    if lexi.love >= 100 or lexi.sub >= 35 or Harem.together(bree, sasha, lexi, name='home'):
        $ lexi.love += 1
        show lexi normal
        "Lexi wrinkles up her nose as she smiles at me."
        "And then, much to my delight, she nods her head."
        $ lexi.love += 1
        lexi.say "You know what, [hero.name] - that sounds kinda fun!"
        lexi.say "I haven't been to a party like that since I was a kid."
        mike.say "Well, it'll be one for the grown-ups, Lexi."
        mike.say "I promise you that!"
        "Lexi keeps on smiling as she nods at this."
        "And I can see that the idea's growing on her the whole time."
        lexi.say "And you said it's a costume party too, right?"
        mike.say "Yeah, Lexi."
        mike.say "Everyone's dressing-up for the occasion."
        show lexi happy
        lexi.say "That's great!"
        lexi.say "Because I've got one I've been itching to wear for ages."
        show lexi normal
        lexi.say "I was just waiting for the chance to bust it out."
        lexi.say "And trust me - you're gonna freak when you see it!"
        "By now I'm nodding and smiling too."
        "And I feel like pinching myself."
        "Not only is Lexi coming to the party."
        "But she's also promising to blow my mind with her costume!"
        "It doesn't get any better than this."
        $ game.flags.halloween_girl = "lexi"
    else:
        show lexi sad
        "Lexi takes me by surprise when she wrinkles up her nose and shakes her head."
        $ lexi.sub -= 1
        lexi.say "Nah, I think I'll pass."
        lexi.say "That sounds kinda lame, [hero.name]."
        show lexi normal
        lexi.say "I usually do something pretty wild on Halloween."
        "For a moment I'm left stunned and unsure of what to say."
        "I'd just assumed that Lexi would be up for it."
        "But I guess that serves me right."
        "I really shouldn't have taken her for granted like that!"
        mike.say "Oh..."
        mike.say "Okay, Lexi."
        mike.say "I mean, if you already have plans..."
        "Lexi nods happily at this."
        "As if she's not the least bit worried about letting me down."
        lexi.say "Yeah, I'm kind of a creature of habit."
        lexi.say "Say, why don't you sack off the party too?"
        lexi.say "We could do something together on Halloween."
        show lexi wink
        lexi.say "And I promise you'll have more fun with me!"
        mike.say "Ah..."
        mike.say "Let me think about it okay?"
    return

label lexi_halloween_arrival:
    scene bg house
    if Harem.together(bree, sasha, lexi, name='home'):
        "I stare at the door for a moment longer, and then I strike myself on the forehead."
        "Of course, Lexi lives here too."
        "So my date's already in the house!"
        "Geez, I must have scrambled my brain putting so much effort into the party."
        scene bg livingroom
        show lexi a halloween nophone
        with fade
        "But the same can't be said for Lexi, as she looks at me expectantly."
        lexi.say "Well, [hero.name], I'm waiting."
        lexi.say "What do you think of my costume?"
        "I look Lexi up and down one last time."
        "And then I take a deep breath."
        "All in preparation to tell her exactly what I think."
        menu:
            "Compliment":
                mike.say "Wow, Lexi...just, wow!"
                mike.say "I didn't want to say this in front of the others."
                mike.say "But you look SO hot!"
                $ lexi.love += 1
                $ lexi.sub += 1
                show lexi happy
                "Lexi almost purrs at the compliment."
                "And I can see that was the answer she wanted to hear."
                lexi.say "Yeah, I thought it'd pop you."
                lexi.say "You being a massive game-geek and all that!"
                mike.say "I know we've got to be good hosts tonight."
                mike.say "But I really want to spend some time alone."
                mike.say "If you know what I mean?"
                show lexi wink
                "Lexi lets out the dirtiest chuckle I've ever heard."
                "But she nods her head in a conspiratorial manner too."
                lexi.say "Oh, don't you worry, [hero.name]."
                lexi.say "My skirts real short and my panties are real high."
                lexi.say "You could slip it into me without anyone noticing!"
                "With that, she turns and walks away."
                "Leaving me to follow, awkwardly trying to hide my sudden erection."
            "Criticize":
                mike.say "Ah..."
                mike.say "It's great, Lexi."
                mike.say "Really nice costume."
                show lexi sad
                "Lexi squints at me, almost sneering."
                "It's clear that wasn't the answer she wanted."
                lexi.say "Huh?"
                lexi.say "It's nice - is that all?"
                lexi.say "I thought you were a game-geek?!?"
                mike.say "I...I am, Lexi."
                mike.say "It's just that...that game's getting old now!"
                $ lexi.love -= 2
                show lexi angry
                "Lexi's eyes go wide and her mouth drops open."
                "Then she plants her balled fists on her hips."
                lexi.say "Is that so?"
                lexi.say "Well, you know what never gets old, [hero.name]?"
                lexi.say "Tits and ass - that's what!"
                lexi.say "Let's see what the other guys at the party think of my costume!"
                hide lexi with dissolve
                "Lexi storms past me in a huff."
                "And I hurry after her, cursing myself the whole time."
    else:
        "Opening the door, I guess I should have been more cautious."
        "Especially after the incidents with Jack's sword and Scottie's trident."
        "But this time it's an actual chainsaw that sends me reeling backwards."
        show lexi a halloween happy nophone with hpunch
        lexi.say "HAPPY HALLOWEEN!"
        "It's only now I see that Lexi's the one holding the chainsaw."
        "She's dressed in what looks like a crazy cheerleader's uniform."
        "And then I recognise it."
        mike.say "Lollipop Chainsaw!"
        lexi.say "Got it!"
        show lexi normal
        lexi.say "Well, [hero.name], I'm waiting."
        lexi.say "What do you think of my costume?"
        "I look Lexi up and down."
        "And then I take a deep breath."
        "All in preparation to tell her exactly what I think."
        menu:
            "Compliment":
                mike.say "Wow, Lexi...just, wow!"
                mike.say "You look SO hot!"
                $ lexi.love += 1
                $ lexi.sub += 1
                show lexi happy
                "Lexi almost purrs at the compliment."
                "And I can see that was the answer she wanted to hear."
                lexi.say "Yeah, I thought it'd pop you."
                lexi.say "You being a massive game-geek and all that!"
                mike.say "I've got to be good host tonight."
                mike.say "But I really want to spend some time alone."
                mike.say "If you know what I mean?"
                show lexi wink
                "Lexi lets out the dirtiest chuckle I've ever heard."
                "But she nods her head in a conspiratorial manner too."
                lexi.say "Oh, don't you worry, [hero.name]."
                lexi.say "My skirts real short and my panties are real high."
                lexi.say "You could slip it into me without anyone noticing!"
                "With that, she turns and walks away."
                "Leaving me to follow, awkwardly trying to hide my sudden erection."
            "Criticize":
                mike.say "Ah..."
                mike.say "It's great, Lexi."
                mike.say "Really nice costume."
                show lexi sad
                "Lexi squints at me, almost sneering."
                "It's clear that wasn't the answer she wanted."
                lexi.say "Huh?"
                lexi.say "It's nice - is that all?"
                lexi.say "I thought you were a game-geek?!?"
                mike.say "I...I am, Lexi."
                mike.say "It's just that...that game's getting old now!"
                $ lexi.love -= 2
                show lexi angry
                "Lexi's eyes go wide and her mouth drops open."
                "Then she plants her balled fists on her hips."
                lexi.say "Is that so?"
                lexi.say "Well, you know what never gets old, [hero.name]?"
                lexi.say "Tits and ass - that's what!"
                lexi.say "Let's see what the other guys at the party think of my costume!"
                hide lexi with dissolve
                "Lexi storms past me in a huff."
                "And I hurry after her, cursing myself the whole time."
    scene bg black with dissolve
    pause 1
    return

label lexi_halloween_party:
    $ game.pass_time(2)
    scene bg livingroom with dissolve
    lexi.say "Hey, [hero.name]!"
    lexi.say "You want another of these?!?"
    show lexi halloween flirt nophone with dissolve
    "I turn around just in time to catch Lexi as she tumbles into me."
    "She's waving around her empty cup and pointing towards the punch-bowl."
    "How many of those has she had already?"
    "She looks like she's about to fall flat on her face!"
    mike.say "Are you okay, Lexi?"
    mike.say "You look a little unsteady!"
    "Lexi makes a visible effort to stand up straight."
    "But she's still wobbling around the whole time."
    lexi.say "I'm okay..."
    lexi.say "I'm better than okay!"
    menu:
        "Indulge Lexi":
            "Ah, what the hell am I worrying about?"
            "This is supposed to be a party."
            "Who cares if Lexi wants to let her hair down."
            mike.say "Here, Lexi."
            mike.say "Let me get you another."
            $ lexi.love += 2
            show lexi happy
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
            $ lexi.love -= 2
            show lexi angry
            lexi.say "Hey!"
            lexi.say "What the hell?!?"
            mike.say "I think you've had enough, Lexi."
            mike.say "At least until you sober up a little."
            show lexi annoyed
            "Lexi protests and tries to snatch back her glass."
            "But all she succeeds in doing is overbalancing."
            "She sways and falls into me again."
            "Snorting and giggling as I have to hold her up."
    scene bg black with dissolve
    pause 1
    return

label lexi_halloween_dance:
    $ game.pass_time(2)
    scene bg livingroom
    show lexi a halloween surprised lolly nophone
    with dissolve
    "The moment that the music starts to play, I can see Lexi's foot tapping."
    "We're supposed to be having a conversation, but her mind's elsewhere."
    "And I can see that she's itching to get out onto the makeshift dance-floor."
    mike.say "Ah..."
    mike.say "Am I boring you, Lexi?"
    lexi.say "Huh...what?"
    lexi.say "Well...yeah, I suppose so!"
    lexi.say "Screw the chit-chat, [hero.name]."
    show lexi a normal outside
    lexi.say "I wanna dance!"
    "Well, at least she's honest."
    menu:
        "Accept":
            mike.say "You're right, Lexi."
            mike.say "This is supposed to be a party."
            show lexi a happy
            "Lexi's face lights up at my answer."
            "But she doesn't have time to reply."
            hide lexi with dissolve
            "As by then I've taken hold of her hand."
            "And I'm already headed for the dance-floor."
            $ lexi.sub += 1
            show dance lexi halloween with dissolve
            lexi.say "Oh yeah."
            lexi.say "Now that's what I'm talking about!"
            "Of course, this isn't going to be a slow-dance."
            "And Lexi makes that apparent right from the start."
            "I don't think there's even a moment she's not rubbing against me!"
            "Lexi gyrates and grinds the whole time, never letting up."
            "It's all that I can do to keep from blushing."
            "But that doesn't mean I want her to stop."
            "I can almost feel the eyes of the other guests on us."
            "As Lexi dances like a stripper in a gentleman's club."
            "By the time the song ends, I'm panting and exhausted."
            "My cock as hard as a rock in my pants."
        "Refuse":
            mike.say "Not now, Lexi."
            mike.say "There's plenty of time for that later."
            show lexi a sad inside
            "Lexi looks instantly disappointed with my answer."
            lexi.say "Aww, come on!"
            lexi.say "Don't be a boring prick!"
            mike.say "I already said no, Lexi!"
            $ lexi.sub -= 1
            show lexi a angry outside
            "Lexi shrugs and shakes her head."
            lexi.say "Alright, suit yourself."
            lexi.say "I'll dance by myself if I have to!"
            hide lexi
            "Before I can protest, Lexi's gone."
            "I watch her hit the dance-floor alone."
            "But it doesn't take long for that to change."
            "And I have to watch as Jack and Scottie join her."
            "They both seem to be drawn into her orbit."
            "And Lexi doesn't hesitate to flaunt herself for them."
            "The whole time she must be aware of me watching her too."
            "But all I can do is stand there like an impotent prick."
    scene bg black with dissolve
    pause 1
    return

label lexi_halloween_sex:
    scene bg livingroom with dissolve
    "It's getting late by now, and the party seems to be winding down."
    "Most of the guests are tired and more than a little drunk."
    "And they seem more interested in chilling out than being wild."
    "Well, all except for one of them."
    show lexi halloween nophone with dissolve
    "Lexi shows no signs of burning out just yet."
    "In fact, she seems to be in the mood for a bit of exercise."
    lexi.say "Come on, [hero.name]."
    lexi.say "Move your ass!"
    mike.say "O...okay, Lexi..."
    mike.say "I'm coming!"
    "Lexi has a firm grip on my wrist, dragging me after her."
    scene bg bathroom
    show lexi halloween nophone
    with fade
    "And she's making for the upstairs bathroom."
    "Which, as luck would have it, is unoccupied."
    "In fact, I shudder to think what would have happened if someone were already in there!"
    "With a show of strength that's a little scary, Lexi all but tosses me inside."
    mike.say "Whoa, Lexi!"
    mike.say "You really need to go that badly?!?"
    show lexi happy
    play sound door_slam
    "Lexi slams the door behind us, laughing as she does so."
    "And then she pretty much spins around on the spot."
    "I can't help gulping and backing off a little."
    show lexi flirt
    "Because there's just something about her posture and the look on her face."
    "I'm instantly put in mind of something from a wildlife documentary."
    "It reminds me of the way a predator stares down it's prey."
    lexi.say "Oh, I need something alright."
    lexi.say "But it's not that."
    mike.say "Erm..."
    mike.say "Then what is it, Lexi?"
    "Like I don't already know!"
    lexi.say "Your cock, [hero.name]."
    lexi.say "I want it inside me!"
    mike.say "You...you could have just asked, Lexi!"
    mike.say "No need to do it in private."
    mike.say "Come on, let's go to my room."
    show lexi annoyed
    "My hand is already on the bathroom door, opening it perhaps an inch."
    "But Lexi slams the palm of her own hand into it, slamming it shut again."
    "I jump in surprise, looking at her wide-eyed and puzzled."
    show lexi angry
    lexi.say "No way!"
    lexi.say "I want it NOW!"
    show lexi normal
    "Before I can say as much as a word, Lexi jumps on me."
    "And I don't mean that metaphorically either."
    "She literally leaps off her feet and pounces on me!"
    "I struggle to keep from falling over."
    "And in doing so I turn and tumble against the door."
    "But don't get me wrong - I'm not trying to get Lexi off of me!"
    "What do you think I am, insane?!?"
    "No, I'm trying to keep her aloft while tugging at my costume!"
    "I have no clue how she manages it."
    "But a moment later, I feel Lexi's hand on my cock."
    show lexi flirt
    lexi.say "Ah!"
    lexi.say "There it is..."
    show lexi missionary halloween with fade
    "And the next thing I know, she's guiding me inside of her."
    "Lexi uses her weight and the force of gravity to great effect."
    show lexi missionary vaginal pleasure
    if hero.has_skill("hung"):
        show lexi missionary vaginalhit
    "She moans and cries out as she sinks down onto my cock."
    lexi.say "Oh..."
    lexi.say "Mmm...yeah...yeah..."
    show lexi missionary normal -vaginalhit
    lexi.say "That's it...that's what I want!"
    "That's good to hear - because it's what I want too!"
    "Suddenly I'm not feeling tired anymore."
    "And I couldn't care less about occupying the bathroom either."
    "All I want to do is pound Lexi as hard as I can possibly manage."
    "And that's just what I set to doing."
    show lexi missionary speed pleasure
    "I thrust into Lexi with all the energy that I have left."
    "Each motion slamming her into the door and rattling the whole thing."
    "She nods and demands more each and every time I do so."
    "The force of the thrusts only seems to make her that much more excited."
    "Pretty soon I can hear what sound like muffled voices outside."
    show lexi missionary blush
    "Which is understandable, as we're fucking so noisily!"
    "And then a fist starts pounding on the other side of the door."
    "Any other time I'd have been mortified."
    "But right now I'm balls deep in Lexi."
    "And I'll be damned if I'm pulling out before I cum!"
    "The sound of someone outside only seems to turn on all the more."
    "I hear her laughing between the moans of pleasure."
    "She's loving this - the dirty little bitch!"
    with hpunch
    "It's that thought which pushes me over the edge."
    show lexi missionary cum ahegao -speed with hpunch
    "I shoot my load into Lexi and she cries out as she cums too."
    with hpunch
    "My legs are shaking as I lower Lexi to the ground."
    show lexi missionary pleasure -blush -vaginal -cum
    show pussy_insert lexi cum zorder 1 at zoomAt(0.75, (820, 100))
    with hpunch
    "But she seems to be in a far better state than me."
    "That's why, as soon as we're half-decent, I can't stop her opening the door."
    hide lexi
    show lexi halloween surprised at right
    show scottie halloween angry at left4
    with fade
    "This reveals Scottie, standing with his legs crossed."
    scottie.say "Not cool, guys."
    scottie.say "Not cool at all."
    scottie.say "If I piss myself in this thing, I lose my deposit!"
    show lexi wink
    lexi.say "What's the matter, fish-boy?"
    lexi.say "I though Aquaman was supposed to be wet?"
    $ lexi.sexperience += 1
    $ game.pass_time(1)
    return

label lexi_date_home_weed_intro:
    scene bg livingroom
    "Tonight's already down in the diary as date night for Lexi and me."
    "But there's a problem with that, and it's not that I don't want to see her."
    "It's actually that I'm really burned out from work by the time I get home."
    "We've deliberately kept our plans vague because neither of us had a clue that we wanted to do."
    "The only decision we made was to meet up at my place and take it from there."
    "I was hoping that all the coffee I've been drinking would do the trick."
    "Even that it might inspire me to think of something fun we could do together."
    show lexi b nophone at center with easeinright
    "But by the time Lexi comes bouncing in, I'm feeling more exhausted than ever!"
    show lexi b happy
    lexi.say "Hey, [hero.name]!"
    lexi.say "I hope you're ready for a wild time tonight!"
    lexi.say "Because I'm revved up and ready to party!"
    mike.say "Ah..."
    mike.say "Yeah, Lexi..."
    mike.say "Sure thing..."
    "I just about manage to get the words out before they turn into a massive yawn."
    show lexi b surprised
    "I can't help it, as soon as I open my mouth, it just comes out and takes over."
    show lexi b surprised at startle
    lexi.say "Whoa..."
    show lexi b annoyed
    lexi.say "What are you - sleep-deprived or something?"
    lexi.say "Shit, you're making me want to yawn too!"
    show lexi a sad
    "Lexi's not kidding either."
    "I watch as she tries to fight it."
    show lexi a yawn at hshake
    "But then she begins yawning too!"
    show lexi a angry
    lexi.say "Damn it!"
    show lexi a normal
    lexi.say "I was all geared up to have a wild night."
    lexi.say "Now all I want to do is slob in front of the TV!"
    "Those words are like music to my extremely tired ears."
    "But I make sure to hide my enthusiasm when I speak up."
    mike.say "Yeah..."
    mike.say "Me too, Lexi!"
    mike.say "I had everything figured out in my head."
    mike.say "Where we were going to go and what we were going to do."
    mike.say "But it's like something just sucked the energy right out of me!"
    show lexi a sad
    "Lexi snorts and shakes her head."
    "Which isn't as bad as it sounds."
    "Trust me, she's really cute when she pouts!"
    lexi.say "Well what in the hell are we gonna do then?"
    show lexi a sad
    lexi.say "I'm too tired to go anywhere else!"
    "I shrug and cast my gaze around the house."
    "Maybe the perfect answer is staring me in the face?"
    mike.say "We could do what you said you feel like, Lexi."
    mike.say "Just stay here and slob in front of the TV."
    mike.say "Everyone else is out, so we have the place to ourselves."
    mike.say "Getting intimate in the sofa doesn't take that much energy..."
    show lexi a normal
    "I see a smile begin to creep over Lexi's face."
    "Luckily for me it seems she likes the sound of that idea."
    show lexi a at center, zoomAt(1.5, (640, 1040))
    "Lexi raises her eyebrows as she takes hold of my hand."
    show lexi a wink
    lexi.say "Come on then, [hero.name]."
    lexi.say "Let's go make ourselves comfortable."
    lexi.say "Then we can see how tired you really are!"
    "The lights are already turned down low, so the atmosphere is perfect."
    "I hardly have the chance to sit down on the sofa before she pounces."
    hide lexi
    show lexi kiss
    with fade
    $ lexi.flags.kiss += 1
    "Lexi almost wraps herself around me as we land, squeezing me tight."
    "And what follows is all that I'd hoped for when suggesting it."
    "There's something on the TV, but I have no idea what it is."
    "Because all of my attention is devoted to Lexi."
    "Right now she reminds me of a sleepy, yet sensual snake."
    "Her limbs are entwined with my own."
    "Her lips are either against mine or else wandering elsewhere."
    "All in all it's more than enough to make me forget about going out tonight."
    "Hell, it's almost enough to make me never want to leave the house again!"
    "I'd be happy to spend most of the night like this."
    "But after a little while, Lexi wants to come up for air."
    hide lexi kiss
    scene bg black
    show watch date tv lexi
    with fade
    "She sits up, looking down at me with a smile."
    lexi.say "Mmm..."
    lexi.say "That's better."
    lexi.say "I feel so much more chilled out now!"
    lexi.say "But I know something that'd take me all the way..."
    "I nod eagerly, thinking that Lexi means something pretty kinky."
    "The thought of her giving me a some attention below the waist sounds really good right now!"
    "But then I see that she's pulled out a small plastic bag."
    "I think I can guess what's inside just from looking at it."
    "And as soon as she opens it up, the pungent scent confirms my suspicions."
    mike.say "Lexi..."
    mike.say "Is that what I think it is?"
    mike.say "Is that marijuana?"
    "Lexi chuckles and rolls her eyes at me."
    scene bg livingroom
    show lexi a surprised nophone at center, zoomAt(1.5, (640, 1040))
    with fade
    lexi.say "What's the matter, [hero.name]?"
    lexi.say "You're not that square, are you?"
    show lexi wink
    lexi.say "Not frightened of a little weed?"
    menu:
        "Sure, why not":
            "Why in the hell not?"
            "I haven't had a good smoke in ages."
            "And I trust Lexi to know the good stuff from the bad."
            mike.say "Sure, Lexi..."
            mike.say "I could use something to soothe my nerves."
            show smoking pot lexi lexismoke with fade
            "Lexi nods and proceeds to light the spliff."
            "She takes a couple of long drags, holding the smoke in her lungs."
            show smoking pot lexi lexihold lexiclose -lexismoke
            "Then she lets it all out, exhaling fragrant clouds into the air."
            show smoking pot lexi lexiexhale lexiopen
            lexi.say "Fuck..."
            lexi.say "That feels SO good!"
            show smoking pot lexi lexigive -lexiexhale
            "She hands the spliff to me and I follow her lead."
            show smoking pot lexi mikesmoke mikeclose
            "Lexi's right - this really is some good shit!"
            "The moment that I breathe out, I feel it hit me."
            show smoking pot lexi mikeexhale mikeopen mikehold -mikesmoke
            "It's like the top of my head is lifting off!"
            show smoking pot lexi lexinormal lexiclose
            "Lexi starts to giggle a couple of seconds later."
            "Then I hear the sound of myself joining in too."
            show smoking pot lexi mikenormal mikeclose
            "And from that point on, were like a couple of stereotypical stoners."
            "Everything's funny one moment and full of deep, spiritual meaning the next."
            "But the best thing is that it makes her cling onto me for the rest of the night."
            "If this is the effect that smoking that stuff has on her, then I'm all for it."
            "Anything that makes Lexi want nothing more than to be in my arms is alright with me!"
            $ lexi.flags.drugs = TemporaryFlag(True, "day")
            $ hero.fun += 5


            $ game.active_date.score += 10
        "Do it, I won't":
            "I'm not too keen on the idea of smoking that stuff myself."
            "But it's not like I'm some kind of puritan either."
            mike.say "I'll pass, Lexi."
            mike.say "But you feel free to go ahead."
            show lexi surprised
            lexi.say "You sure, [hero.name]?"
            show lexi happy
            lexi.say "This is some pretty good shit!"
            mike.say "Nah, I'm cool."
            show smoking pot lexi lexismoke with fade
            "Lexi shrugs and proceeds to light the spliff."
            "She takes a couple of long drags, holding the smoke in her lungs."
            show smoking pot lexi lexihold lexiclose -lexismoke
            "Then she lets it all out, exhaling fragrant clouds into the air."
            show smoking pot lexi lexiexhale lexiopen
            lexi.say "Fuck..."
            lexi.say "That feels SO good!"
            show smoking pot lexi lexigive -lexiexhale
            "She starts to giggle a couple of seconds later."
            show smoking pot lexi lexinormal lexiclose
            "And from that point on, Lexi's like a stereotypical stoner."
            "Everything's funny one moment and full of deep, spiritual meaning the next."
            "But the best thing is that it makes her cling onto me for the rest of the night."
            "If this is the effect that smoking that stuff has on her, then I'm all for it."
            "Anything that makes Lexi want nothing more than to be in my arms is alright with me!"
            $ lexi.flags.drugs = TemporaryFlag(True, "day")
            $ game.active_date.score += 10
        "Not in this house":
            "What does she think this is - some kind of drug-den?"
            "I'm not going to stand by and let Lexi turn my home into a crack-house!"
            mike.say "There is no way you're smoking that stuff in here, Lexi!"
            mike.say "The smell alone is enough to give it away."
            show lexi surprised
            lexi.say "Are you for real?!?"
            lexi.say "It's only a spliff, [hero.name]!"
            show lexi angry
            lexi.say "I'm not suggesting we smoke crack or shoot up heroin!"
            mike.say "No, Lexi, just no, okay?"
            show lexi annoyed
            "Lexi makes a disgruntled sound as she shoves the bag back into her pocket."
            scene bg black
            show watch date tv lexi
            with fade
            "Then she slouches back down on the sofa, muttering under her breath."
            "And I note that she's also put a little distance between us too."
            $ game.active_date.score -= 10
    return

label lexi_date_mall_weed:
    scene bg mall1 with fade
    "I sometimes come to the mall on my own, just to get a little bit of time to think."
    "It can be way better for me than being someplace on my own, you know?"
    "Somehow the bustle of the people and the background noise lets me tune out reality."
    show lexi smile at center, zoomAt(1.25, (440, 880)) with dissolve
    "But it's nothing like that when you invite someone like Lexi to come along too..."
    show bg clothesshop
    show lexi normal at center, zoomAt(1.25, (440, 880))
    with fade
    lexi.say "Oooh..."
    lexi.say "Look at those shorts - they're so tight!"
    show lexi normal at center, traveling(1.25, 0.5, (640, 880))
    lexi.say "And those trainers - so expensive!"
    lexi.say "You think I could get away with trying them on and walking out of the store?"
    show lexi wow at center, traveling(1.25, 0.3, (940, 880))
    lexi.say "Oh...come look at this!"
    lexi.say "How do you think I'd look in this thong bikini, [hero.name]?"
    show lexi wink
    lexi.say "Pretty sexy, huh?"
    show lexi smile
    "No sooner has she set eyes on one thing than she's flitting to another."
    "It's like she has the attention span and memory of a goldfish!"
    "But don't get me wrong - I'm not complaining."
    show bg mall1
    show lexi normal at center, zoomAt(1.25, (640, 880))
    with fade
    "I'm actually enjoying being swept along in her wake right now."
    "There's just something endearing about Lexi when she's like this."
    "Like she's somehow more innocent, almost playful in nature."
    "Rather than being the tough, no-nonsense street-girl she usually seems to be."
    mike.say "Whoa..."
    mike.say "Slow down a little, Lexi!"
    mike.say "You're making me dizzy!"
    show lexi blank
    "Lexi stops dead in her tracks, looking back at me over her shoulder."
    show lexi smile
    "She has one of those lop-sided smiles on her face and a twinkle in her eye."
    show lexi yawn
    lexi.say "Aw..."
    show lexi happy
    lexi.say "Am I too much for you, [hero.name]?"
    show lexi normal
    lexi.say "Can't you keep up the pace?"
    show lexi smile
    mike.say "I can keep up, Lexi!"
    mike.say "But I want to slow things down a little."
    mike.say "At this rate we'll be done in no time."
    mike.say "Then what are we going to do?"
    mike.say "We can't window-shop if we run out of windows!"
    "Lexi shakes her head and waves a finger in my face."
    show lexi normal
    lexi.say "You know what you need, [hero.name]?"
    lexi.say "You need to chill out."
    lexi.say "You need to unwind."
    show lexi wink at center, traveling(1.5, 0.3, (640, 1040))
    lexi.say "And I've got just the thing!"
    show lexi smile
    "Lexi pulls out what looks like a hand-rolled cigarette."
    "But when she waves it under my nose, I catch an unmistakable scent."
    "It's not a cigarette - it's a joint!"
    "Lexi seems to mistake my surprise for enthusiasm."
    show lexi wink
    "She gives me a lascivious wink and a grin."
    show lexi normal
    lexi.say "So, [hero.name]..."
    lexi.say "What do you say?"
    show lexi smile
    menu:
        "Sure, why not":
            "I put my hand over the joint, just to make sure nobody sees it."
            "But at the same time I give Lexi a nod and a smile."
            mike.say "Why the hell not?"
            mike.say "I could do with something to chill me out."
            show lexi happy at startle
            "Lexi giggles and grabs hold of my wrist."
            "And before I know it, she's leading me away from the main part of the mall."
            show smoking pot lexi lexismoke parking with fade
            "I soon find myself in a remote part of the car park, away from prying eyes."
            "Lexi wastes no time in whipping out the joint and a lighter."
            show smoking pot lexi lexihold lexiclose -lexismoke
            "She lights the joint and takes a long, deep drag."
            show smoking pot lexi lexiexhale lexiopen
            "Then she lets it all out in one long cloud of pungent smoke."
            lexi.say "Oh yeah..."
            show smoking pot lexi lexigive -lexiexhale
            lexi.say "That hit the spot!"
            show smoking pot lexi mikesmoke mikeclose
            "Lexi hands the joint over to me and I take a drag myself."
            if hero.fitness >= 60:
                "The spliff is damn strong, far stronger than I was expecting."
                "But it's nothing that I can't handle, so long as I'm sensible."
                show smoking pot lexi mikeexhale mikeopen mikehold -mikesmoke
                "I hold the smoke in for a short while and then exhale."
                "And I enjoy the sensation of my head getting lighter by the second."
                lexi.say "Good shit, huh?"
                mike.say "Yeah, Lexi..."
                mike.say "It's pretty good!"
                show smoking pot lexi lexismoke -mikeexhale mikeopen -mikehold
                "The joint goes back and forth between us."
                "And soon I know that I'm getting dangerously high."
                "But I'm not too far gone to see the same signs in Lexi too."
                mike.say "Damn, Lexi..."
                mike.say "I feel like my head's full of helium!"
                "Lexi bursts out laughing, which confirms that she's high."
                "There's no way that comment deserved such a response."
                show smoking pot lexi lexinormal lexiopen
                lexi.say "Me too!"
                lexi.say "But you know what always makes it better?"
                "I shake my head, expecting her to say something pretty obvious."
                "You know, like getting pizza or going for a beer."
                scene bg black
                show lexi bj alley casual nodick
                with fade
                "But instead, Lexi holds my eye as she gets down on her knees."
                "I watch in silent fascination as she unzips my flies."
                show lexi bj slap
                pause 0.1
                show lexi bj -slap dick with hpunch
                "And then I burst out laughing too as she pulls out my cock."
                mike.say "Y...you're fooling around, right?"
                mike.say "Right, Lexi?"
                "Lexi answers the question by raising her eyebrows."
                play sexsfx1 bj_sucking loop
                show lexi bj suck closed
                "And at the same time she slides my cock into her mouth."
                "All I can do is gasp in shock as she begins to work it with her lips and tongue."
                "After the high of the joint, what she's doing feels incredible."
                show lexi bj open
                "It's so good that it's making my head spin more than the drugs!"
                "Any other time I might have been worried about getting caught."
                "But right now all I can think of is letting Lexi have her way."
                play sexsfx1 bj_deepthroat loop
                show lexi bj suck
                pause 0.2
                show lexi bj deepthroat -suck closed at startle(0.05,-10)
                pause 0.2
                show lexi bj suck
                pause 0.2
                show lexi bj deepthroat -suck at startle(0.05,-10)
                "Stoned as she is, Lexi doesn't lose any of her talent for the art of the blow-job."
                "Hands, head, lips and tongue all work in perfect harmony."
                show lexi bj suck
                pause 0.2
                show lexi bj deepthroat -suck at startle(0.05,-10)
                pause 0.2
                show lexi bj suck
                pause 0.2
                show lexi bj deepthroat -suck at startle(0.05,-10)
                "And every time she makes a slight change, I gasp in response."
                "In fact, I totally forget where we are in favour of what she's doing."
                show lexi bj suck
                pause 0.2
                show lexi bj deepthroat -suck at startle(0.05,-10)
                pause 0.2
                show lexi bj suck
                pause 0.2
                show lexi bj deepthroat -suck at startle(0.05,-10)
                "That is until I hear the sound of a car engine being started nearby!"
                show lexi bj suck
                pause 0.15
                show lexi bj deepthroat -suck at startle(0.05,-10)
                pause 0.15
                show lexi bj suck
                pause 0.15
                show lexi bj deepthroat -suck at startle(0.05,-10)
                "I jump at the noise, making Lexi gag."
                "And the whole thing means I shoot my load too early as well!"
                $ facial = False
                menu:
                    "Swallow":
                        "Lexi simply doesn't have time to react."
                        play sexsfx1 final_thrust
                        show lexi bj cum open with vpunch
                        "And I'm practically shoving my cock down her throat too!"
                        with vpunch
                        "She gasps and chokes as I shoot my load."
                        show lexi bj showcum -cum nodick -deepthroat
                        pause 0.3
                        show lexi bj swallow with vpunch
                        "But somehow she still manages to swallow it all."
                    "Facial":
                        play sexsfx1 slide_out
                        show lexi bj normal -deepthroat open
                        "Before Lexi can react, I pull my cock out of her mouth."
                        "She gasps and chokes, taken completely by surprise."
                        play sexsfx1 final_thrust
                        show lexi bj cum with vpunch
                        "And a moment later I shoot my load into her face too!"
                        show lexi bj facial -cum with vpunch
                        "It spatters all over her, painting her face with sticky white lines."
                        $ facial = True
                stop sexsfx1
                "Luckily for me, the car turns out to have been on the far side of the car-park."
                "So it pulls away none the wiser as to what we were doing."
                scene bg black
                show smoking_pot_bg_parking with fade
                mike.say "Phew..."
                mike.say "That was lucky!"
                show lexi casual angry at center, zoomAt(1.5, (640, 1040))
                if facial:
                    show lexi cum
                with easeinbottom
                lexi.say "Speak for yourself!"
                lexi.say "Because you sure made a mess of me, asshole!"
                show lexi annoyed
                "I look round to see Lexi, still trying to clean herself up."
                "And I can't help chuckling as I stuff my cock back into my pants."
                show lexi smile
                "Sure, she'll probably make me pay for it later."
                "But right now, while I'm stoned, it's funny as hell!"
                $ game.active_date.score += 10
            else:
                "Almost as soon as I fill my lungs, I know something is wrong."
                "My head starts swimming and my vision becomes blurred."
                scene bg black
                show smoking_pot_bg_parking
                show lexi sad at center, zoomAt(1.5, (640, 1040))
                with fade
                "Lexi looks instantly concerned."
                show lexi surprised
                lexi.say "Fuck!"
                lexi.say "Are you okay?!?"
                show lexi blank
                mike.say "I..."
                mike.say "I don't think so!"
                mike.say "In fact...I feel a little..."
                "Before I can finish speaking, I bend over double."
                show lexi at center, traveling(1.25, 0.2, (640, 880)) with ease
                "And Lexi just manages to jump backwards as I puke."
                show lexi angry
                lexi.say "Eww!"
                lexi.say "Gross!"
                show lexi annoyed
                mike.say "Urgh..."
                mike.say "S...sorry, Lexi..."
                mike.say "I dunno what happened!"
                "Lexi gingerly steps over the puddle of puke at my feet."
                "And then she takes me gently by the arm."
                show lexi normal
                lexi.say "Geez..."
                lexi.say "Let's get you cleaned up, okay?"
                "I nod weakly, letting Lexi lead me away."
                "And that marks the rather ignominious end of our trip to the mall."
                $ game.active_date.score -= 10
        "WTF Lexi!":
            "I glance around furtively, looking for security guards."
            "I'm suddenly certain that somebody must have seen Lexi waving the joint around."
            mike.say "Will you put that thing away?!?"
            mike.say "We can't smoke it here!"
            show lexi annoyed
            "Lexi frowns and shakes her head."
            "But at least she puts the joint away again."
            show lexi surprised
            lexi.say "Huh?"
            lexi.say "Why the hell not?"
            show lexi angry
            lexi.say "There must be a hundred places nobody'd see us around here!"
            lexi.say "We could light up this bad boy in any one of them!"
            show lexi annoyed
            "I wave my hands in the air, dismissing the suggestion."
            mike.say "No way, Lexi!"
            mike.say "Wait until we get back to your place or mine, okay?"
            "Lexi rolls her eyes and lets out grunt."
            show lexi angry
            lexi.say "Okay, okay..."
            lexi.say "Spoilsport!"
            show lexi annoyed
            "Luckily for me, Lexi seems to move on pretty quickly."
            "She doesn't sulk, and before too long she's back to normal."
            "And we complete our tour of the mall without further incident."
            $ game.active_date.score -= 5
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
