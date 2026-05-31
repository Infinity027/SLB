init python:
    InteractActivity(**{
    "name": "fuck_lexi",
    "display_name": "Fuck",
    "label": "ACTIVE_GIRL_fuck_ROOM",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(HasRoomTag("home")),
            Not(IsRoom("alley")),
            HasStamina(),
            ),
        PersonTarget(lexi,
            IsActive(),
            MinStat("love", 75),
            MinStat("sub", 25),
            MinStat("sexperience", 2),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })

    InteractActivity(**{
    "name": "fuck_lexi_home",
    "display_name": "Fuck",
    "label": "ACTIVE_GIRL_fuck_ROOM",
    "conditions": [
        IsTimeOfDay("afternoon", "evening"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            HasStamina(),
            ),
        PersonTarget(lexi,
            IsActive(),
            InHarem('home'),
            MinStat("love", 75),
            MinStat("sexperience", 2),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })

    InteractActivity(**{
    "name": "fuck_lexi_alley",
    "display_name": "Fuck",
    "label": "ACTIVE_GIRL_fuck_ROOM",
    "duration": 1,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsRoom("alley"),
            HasStamina(),
            ),
        PersonTarget(lexi,
            IsActive(),
            MinStat("love", 75),
            MinStat("sexperience", 2),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })

    Event(**{
    "name": "lexi_hottub_sex_male",
    "label": "lexi_hottub_sex_male",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("date_hot_tub_home")),
        PersonTarget(lexi,
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


label lexi_fuck_alley:
    $ game.play_music("music/roa_music/city_nights.ogg")
    show lexi
    "The space behind the building could pretty much be the very definition of a filthy, disgusting and repellent back-alley."
    "But then we're not here to critique its lack of cleanliness, and the girl I'm with doesn't exactly scream high-class values either."
    "Indeed, if I'm distracted enough by what we have in mind, Lexi seems even less bothered about the prospect of getting it on back here."
    show lexi bubblegum
    "She leads me by the hand the whole time, blowing bubbles that pop with a crack as she sucks them back into her mouth and giggling at the prospect of misbehaving."
    "Her nonchalant acceptance of the back-alley as a place to go for a quickie and the fact that she's not even really looking where we're going makes me wonder."
    show lexi normal
    "Has Lexi been here before, and if so, how many time and under what specific circumstances?"
    "Did she bring her clients here, or do what we're about to do with Danny on this very same spot?"
    show lexi bubblegum
    "I shake my head briefly, pushing those thoughts forcibly out of my mind and concentrating on the motion of Lexi's backside instead."
    "She's a girl with a chequered past, a lot of which isn't nearly worth delving into."
    "Sure it adds a healthy dose of spice to being with her, but it's not the kind of stuff you want knocking on your front door in the middle if the night either."
    "Luckily for me, the enticing sight of Lexi as she chooses a spot between two rank dumpsters is enough to bring my mind back to the here and now."
    show lexi normal
    "This girl really is something else, as I find that I can hardly smell the foul odour of the dumpsters."
    "Not while I watch as she presses her hands against the brick wall between them and begins to shake her ass in order to lure me in."
    show lexi wink
    lexi.say "Come on now, [hero.name], what are you waiting for?"
    lexi.say "My pussy's all nice and wet for you!"
    show lexi flirt
    lexi.say "And it's not gonna fuck itself, now is it?"
    "Christ help me, but this girl's pure, unadulterated filth!"
    "And how can I hope to resist that?"
    menu:
        "Let her suck you" if "lexi_bj_alley" in DONE:
            show lexi bj alley casual nodick with fade
            "She wastes no time in getting down on her knees and fumbling with my flies."
            show lexi bj dick
            "She reaches into my unzipped flies and pulls out my cock, smiling at the sight of how stiff it is."
            "The fact that we're standing in the middle of a dodgy neighbourhood at night is more than a little exciting."
            "Or maybe it's the sight of Lexi's willing lips."
            show lexi bj showcum
            lexi.say "Mmm..."
            "Lexi makes some rather agreeable sounds as she starts to lick at the tip."
            lexi.say "So big and so hard, just for little old me!"
            show lexi bj suck closed
            "And then she takes it into her mouth, wrapping her tongue around the shaft."
            "It's not the most elegant of blowjobs, in fact it's pretty damn sloppy."
            "But what it lacks in style, it more than makes up for in terms of enthusiasm."
            show lexi bj open
            "Soon all I can hear is the sound of Lexi's lips sucking and her throat gagging."
            "I'm not being pushed back against the wall by her any longer, but leaning against it for support."
            show lexi bj normal showcum slap
            "At one point, Lexi fumbles my cock, making it pop out of her mouth and slap her on the cheek."
            lexi.say "Oops!"
            show lexi bj smile -slap
            lexi.say "I'm such a clumsy girl!"
            show lexi bj deepthroat closed
            show mouth_insert lexi zorder 1 at zoomAt(1, (820, 200))
            "And before I can as much as say a word, she crams my balls into her mouth."
            "The experience is so intense for me that I've almost forgotten just where we are."
            "My own gasping and moaning gets louder, until a passing car illuminates us with its headlights."
            "Perhaps it's the sudden realisation of just how close we are to the street that does it."
            "Or maybe Lexi's just pushed me beyond the point of no return at that exact moment."
            show lexi bj left right
            "Either way, I can't hold back from cumming any longer."
            show lexi bj normal swallow facial with vpunch
            "Still sucking on my balls, the shower of cum takes Lexi completely by surprise."
            with vpunch
            "She spits out the mouthful of testicles that she's been sucking on and yelps, far too loud for my liking."
            hide mouth_insert
            show lexi bj smile -left -right nodick with vpunch
            lexi.say "Hey, no fair!"
            lexi.say "I wanted that in my mouth, not all over my face!"
            "All I can do is shake my head and let out a rueful laugh."
        "Fuck her":
            "I don't hesitate to reach out and take hold of Lexi's shorts, twining the elastic of her panties in my fingers as I do so."
            show lexi surprised bottomless with dissolve
            "Yanking them down roughly does nothing but add to her already willing mood."
            "She wiggles and squirms as I pull them down, over her thighs and to her knees, where they finally drop her ankles."
            "The same motion exposes her a little, allowing me a fleeting glimpse of her pussy between her legs."
            show lexi flirt
            "As if sensing what I'm seeing from the way my breath quickens, Lexi glances back over her shoulder and winks at me."
            lexi.say "See, I was telling the truth - all warm, wet and just waiting for you!"
            lexi.say "What are you waiting for?"
            lexi.say "Come on in!"
            "There's not going to be any sophisticated foreplay or cinematic love-making here."
            "All I want right now is something that's quick, cheap and dirty - just like Lexi herself!"
            "I almost jam the zipper on my flies in an effort to get my cock out as quickly as I can."
            "The metal teeth of the zipper chafe as I pull my already stiffening manhood out with one hand."
            "All the time, the other is busily caressing Lexi's ass, ensuring that, by the time I have it fully out, it's fully erect as well."
            "I have no thought of pausing or letting anything come between me and having my way with Lexi, and so I press straight on."
            if persistent.xray:
                show lexi stand2 alley manoutfit casual xray with fade
            else:
                show lexi stand2 alley manoutfit casual with fade
            "She sighs appreciatively at the sensation of my cock pressing between her already slick thighs."
            "And then she actually moans as the head slithers along the lips of her pussy."
            "Taken together, the feel of her and the sounds she makes are more than enough to spur me on."
            "I thrust straight into Lexi a second later, hard and without thought for being in the least bit gentle."
            "All of my desire for her is encapsulated in that first thrust, every part of how her slutty, provocative ways turn me on so."
            "She responds in kind, delighted by the fact that I keep on pushing into her until I can go no further and then remain there for an extended moment."
            "Lexi seems to like it too, so much so that she wriggles on the end of my cock."
            "Working her ass into my groin as if trying to extract every ounce of pleasure that's to be had from it."
            "Suddenly inspired to follow her example, I push Lexi forwards with all the strength that I can muster."
            "She yelps at the sensation of losing her balance for a moment."
            "But she's already so close to the wall that it's merely a matter of a stumbling half-step until she's pressed hard against it."
            "Lexi scrabbles for purchase on the grimy wall with both hands, but it's so slippery with muck that they slip and she falls into the bricks instead."
            "Now her face and chest are squashed hard to the wall, and I'm still leaning into her as hard as I can."
            "I can see the filth smearing up Lexi's cheek, forearms and staining tiny white top, and it just makes me want to go faster."
            "By now I'm practically pounding into her, so that the only things keeping her upright are myself and the wall."
            "Caught between a rock and a hard cock, Lexi almost chokes on her bubblegum, before desperately spitting it out in order to keep breathing."
            "I'm not sure whether she's not protesting because she likes what I'm doing, or because she simply can't get the words out."
            "But I'm too deep into this thing to even think about stopping now."
            "And anyway, I'm almost ready to cum anyway!"










            "There's no chance of anything making me stop now, not when I'm this far into Lexi and so lost in the moment as I am right now."
            with hpunch
            "As the urge to cum takes me over, I find myself almost lifting Lexi off of the ground, more with each successive thrust."
            if persistent.xray:
                show lexi stand2 ahegao xray with hpunch
            else:
                show lexi stand2 ahegao with hpunch
            "Lexi feels it too, I know this because I can feel her starting to buck and twitch as she starts to cum herself."
            with hpunch
            "I didn't think I could, but as I let go inside of Lexi, I actually start pushing into her with yet more force."
            "She's literally pressed against the bricks of the wall now, her nails scraping on the mortar between them."
            "Lexi's moans are distorted and stretched as her face suffers the same fate."
            hide lexi
            show lexi blush bottomless
            with fade
            "Leaning fully against one of the dumpsters for support now, I hastily stuff my drooping cock back into my pants."
            "Lexi is slow to pull up her panties and shorts, squatting down as she does so and watching me with an oddly conflicted look in her eyes."
            show lexi -bottomless
            "On the one hand, I can see that she's still flushed with the after-effects of what we just did."
            "But there's also an element of vulnerability to her as well, as though she's taken me down to her level and is afraid of being judged harshly for doing so."
            show lexi happy -blush
            "All the same, she smiles awkwardly at me and takes my hand, leading me out of the alley-way and back into the street beyond."
            $ lexi.sexperience += 1
            hide lexi
    return

label lexi_fuck_livingroom:
label lexi_fuck_kitchen:
label lexi_fuck_pool:
label lexi_fuck_bedroom1:
label lexi_fuck_bedroom2:
label lexi_fuck_bedroom3:
label lexi_fuck_bedroom4:
label lexi_fuck_bedroom5:
label lexi_fuck_bedroom6:
label lexi_fuck_secondfloor:
label lexi_fuck_house:
label lexi_fuck_home:
    $ game.play_music("music/roa_music/city_nights.ogg")
    show lexi
    mike.say "Hey, wanna come and have fun in my bedroom?"
    lexi.say "Sure."
    if Harem.find('lexi', name='home'):
        call home_harem_fuck_choices ('lexi') from _call_home_harem_fuck_choice_2
    else:
        call lexi_fuck_date_male (called_from_date=False) from _call_lexi_fuck_date_2
    return

label lexi_fuck_date_nudistbeach:
label lexi_fuck_date_beach:
label lexi_fuck_beach:
    $ game.play_music("music/roa_music/city_nights.ogg")
    scene bg beach
    show lexi nophone
    if game.week_day % 2 == 0:
        if game.room != "date_nudistbeach":
            "She wears next to nothing on an average day, and the bikini she has on is almost non-existent."
        "I consciously choose a spot a way from the nearest beach-goers, where we'll be out of sight."
        "It's not because I resent other guys looking at Lexi, I swear."
        "More because I want to have the option of doing more than just looking."
        "If you know what I mean?"
        "Almost as soon as we have the blanket spread out on the sand, Lexi flops down upon it."
        "She lays there with all the lack of grace that you'd expect from a trailer-park princess."
        "But the sight of that body still makes my cock start to swell inside of my shorts."
        show lexi a happy
        lexi.say "Hey, [hero.name]."
        lexi.say "You can stop trying to make it look like you're not looking."
        "Despite the fact that she's caught me in the act, I still try to brush off Lexi's comment."
        mike.say "Huh...what?"
        mike.say "I have absolutely no idea what you mean, Lexi!"
        show lexi b normal
        "Lexi turns over onto her side, propping her head up on her hands to regard me."
        lexi.say "Erm, hello - remember who you're trying to bullshit here, [hero.name]!"
        lexi.say "You think I'm not smart to how a guy looks when he's checking me out?"
        "I persist in trying to deny it, shaking my head the whole time."
        mike.say "No, Lexi - that's not it at all."
        mike.say "I was...I was...just thinking how pretty you look in your swimsuit."
        mike.say "That's all..."
        "Lexi sighs at this, rolling her eyes."
        show lexi surprised
        lexi.say "Oh come on, [hero.name]."
        lexi.say "We both know you're staring because you want to fuck me!"
        "I can only shrug at her blunt honesty, and then nod in defeat."
        mike.say "Well...of course I want to, Lexi."
        mike.say "You're incredibly hot, and I'm crazy about you."
        mike.say "Why...don't you want to do...it?"
        "Lexi sighs again, as if she's being forced to state the obvious."
        show lexi a
        lexi.say "Of course I do!"
        lexi.say "Don't worry, I'm going to let you fuck me."
        show lexi happy
        lexi.say "It'd just be nice to think you didn't think that it was a sure thing."
        "I frown, starting to get more than a little confused with where this is going."
        mike.say "So you're saying that you want me to think that you won't put out."
        mike.say "Even though you're telling me that you're definitely going to put out?"
        show lexi annoyed blush
        lexi.say "Shit, [hero.name] - do you have to make it sound so complicated?!?"
        if game.room == "date_nudistbeach":
            "Lexi shakes her head."
        else:
            "Lexi shakes her head and starts unceremoniously tugging down her bikini bottoms."
        lexi.say "You'd better get on with fucking me."
        lexi.say "Before this turns into some kind of debate!"
        if game.room == "date_nudistbeach":
            "I lie down hastily on the blanket beside Lexi."
        else:
            "I lie down hastily on the blanket beside Lexi, following her lead with my own shorts."
        show lexi annoyed -blush
        "But then she holds up a finger, a stern look crossing her face as she does so."
        lexi.say "One thing, [hero.name]."
        lexi.say "We do it on the blanket, okay?"
        show lexi normal
        "I nod eagerly, and her expression becomes a little more relaxed."
        lexi.say "Good - because I don't want to be washing sand out of my butt and pussy for a month!"
        mike.say "Shame - I could have called you 'Sandy Cheeks'..."
        "Lexi greets this attempt at humour with a glare that makes me shut up almost instantly."
        show lexi annoyed blush
        lexi.say "Forget the comedy, [hero.name]."
        lexi.say "Do something you're good at - and fuck me already!"
        "By now, I'm more than happy to do as I'm told."
        show lexi missionary beach outside with fade
        "So I push Lexi down until she's flat on her back, then lie atop her."
        "She smiles at the prospect of getting the length of my cock inside."
        if game.room != "date_nudistbeach":
            "And then pulls down her bikini top, letting her breasts fall free upon her chest."
        "The gesture is more than enough to spur me on, and I thrust my cock forward without warning."
        "For a moment, the lips of Lexi's pussy resist me."
        show lexi missionary beach vaginal
        "I hear her begin to moan at the sensation of my pushing to enter her."
        "And then the resistance is no more, and I slide into the soft warmth of her body."
        "But even then, Lexi doesn't stop moaning for an instant."
        show lexi missionary beach pleasure vaginalhit
        "If anything, the sounds coming out of her become all the more loud and intense."
        "With my ears so full of such approving noises, I respond by steadily gaining more speed myself."
        "And this only serves to reduce Lexi to the state of a juddering mess."
        "So much for her professed irritation at my assuming she wanted to be fucked."
        "Now that she's on her back, legs spread and a cock inside of her, Lexi's like a sponge."
        show lexi missionary beach speed
        "She takes all that I can give her with a hunger that can be seen in the way she shakes and quivers."
        "Every part of her body is given over to the pleasure that she's taking from the act."
        "She can protest all she likes when she's vertical."
        "But as soon as she's horizontal, all Lexi wants is as much cock as she can handle!"
        "And I make sure to give her all that I have on account of that."
        "When the time comes for me to fill her, she almost clings to me."
        show lexi missionary beach cum ahegao with vpunch
        "And it's as if she's trying to eke out every single drop of it that she can catch."
        "Afterwards, we lie side by side on the blanket, letting the sun dry the sweat off of our skin."
        "Lexi seems sleepy, almost as though she needs to sleep off all the cock she's had."
        "I watch her as she drifts into sleep, noting the way that the moisture on her body glistens in the sunlight."
        "Maybe I should be thinking deep thoughts right now, or composing poetry in her name."
        "But all I can think of is just how long I should let her sleep."
        "How long would it be wise to give her, before I wake her and see if she wants to go again?"
    else:
        "Being at the beach with Lexi is kind of like living the dream, you know?"
        "Like all those fantasies you had as a sad, lonely adolescent have finally come true."
        "You're walking along the sand, feeling as though you're on top of the world."
        if game.room == "date_nudistbeach":
            "And it's all because the naked hot girl is hanging off of your arm for a change."
        else:
            "And it's all because the achingly hot girl in the skimpy bikini is hanging off of your arm for a change."
        show lexi happy
        "Whenever she laughs at your jokes and leans her head on your shoulder, you feel like pinching yourself."
        "You just know that other guys are looking on with jealously in their eyes."
        "That and the fact that young kids are wondering when it'll be there turn to be where you are now."
        "I try to live up to the image too, holding my head up and swaggering as best I can."
        "But the truth is that I'm too into Lexi to be able to hide the fact."
        "And so I end up looking almost as amazed and stunned as anyone looking on too!"
        show lexi surprised
        show fx exclamation
        lexi.say "Hey, [hero.name]!"
        lexi.say "That look on your face - what's it all about?"
        hide fx
        "I slow down a little, surprised by Lexi's sudden question."
        "I guess my admiring gazes must have caught her attention."
        mike.say "Oh, nothing..."
        mike.say "I was just thinking, that's all."
        show lexi annoyed
        show fx question
        "Lexi screws up her face, puzzled by my cryptic answer."
        lexi.say "About what?!?"
        show lexi normal
        lexi.say "Aw, come on, [hero.name]."
        lexi.say "You can't say that and not tell me!"
        hide fx
        "I can already feel the awkward, embarrassed smile spreading across my face."
        "But what other choice do I have then to be honest with her?"
        "After all, it's not like I've been dwelling on anything that's not flattering, is it?"
        mike.say "I was just thinking how lucky I am, Lexi."
        mike.say "There's all these people giving you admiring glances."
        mike.say "But I'm the guy that's actually with you."
        "Another girl might have blushed at a compliment of that kind."
        "A seriously humble girl maybe even been horrified to learn she was being admired like that."
        "But not Lexi, as she's just not that kind of girl."
        show lexi happy
        "Instead, she looks positively delighted to be the centre of attention, an object of desire."
        lexi.say "Oh, I know what you mean, [hero.name]."
        show lexi normal
        lexi.say "You don't do what I do for long without getting it."
        lexi.say "And I know what they're thinking when they look at me too."
        lexi.say "I know just how much they all want me."
        lexi.say "I know what they want to do with me."
        lexi.say "What they're picturing in their heads..."
        "I can already feel my cock stiffening in my shorts."
        "Lexi just does that to me when she starts to talk dirty."
        "I guess it's one of her gifts!"
        mike.say "Ah...y...yeah, Lexi..."
        mike.say "That's quite a mental image!"
        "She must notice how flushed I'm getting."
        "As she leans in closer, shaking her head at me."
        show lexi wink
        lexi.say "Aww..."
        lexi.say "Don't be jealous, [hero.name]!"
        mike.say "What?!?"
        mike.say "I...I'm not jealous!"
        show lexi normal
        lexi.say "You do know that they're thinking about you too, right?"
        mike.say "W...why would they be thinking of me, Lexi?"
        lexi.say "Because you're the one that gets to fuck me, [hero.name]."
        lexi.say "They're the ones that should be jealous, not you!"
        mike.say "Really?"
        lexi.say "Sure, thing."
        show lexi flirt
        lexi.say "Like right now, they're all imagining you fucking me on the beach."
        lexi.say "All envying you putting your cock inside of me and making me scream!"
        "I let out a nervous, almost manic laugh."
        mike.say "Yeah, Lexi, yeah."
        mike.say "Shame there's all these people around."
        mike.say "Or else we could do just that!"
        "Lexi stops, dead in her tracks."
        "She looks this way and that, and then shrugs."
        show lexi normal
        show fx question
        lexi.say "What other people?"
        "I follow her gaze, only now realising how far we've walked down the beach."
        "There's literally no one to be seen."
        "Only the vague impression of people far off in the distance."
        "Did she plan all of this?"
        "Did she walk me away from the crowds and get me all worked up deliberately?"
        "Fuck sake - what does it matter if she did?"
        "Lexi laughs with delight as I put my hands on her waist and pull her towards me."
        "It's a filthy sound, one that only serves to make me want her all the more."
        show lexi kiss with fade
        $ lexi.flags.kiss += 1
        "The laugh gets stifled when I plant a kiss on her lips."
        "And I don't know if my enthusiasm is too much for her or Lexi actually trips me on purpose."
        "But either way, the end result is that we collapse into a heap on the ground."
        "Luckily for me the sand is soft enough to cushion our fall."
        "This means that the desperate groping continues almost as soon as we're horizontal."
        "There's no need for either of us to say a word."
        "I know what I want and I know that Lexi wants the same thing too."
        if game.room != "date_nudistbeach":
            "And even if I didn't, she nods as I yank down my shorts, tugging aside her bikini bottoms."
        "I guess all of the flirting and beating around the bush beforehand counted as foreplay."
        scene lexi missionary
        show lexi missionary beach
        with fade
        "Which is a relief, as my cock's achingly hard."
        "And all I want is to be inside of Lexi as deep as possible!"
        "I know that I'm right when I thrust the head between the lips of her pussy."
        "There's no more than a second or two of resistance, a token show of fake restraint."
        show lexi missionary vaginal
        "And then I'm in her, sinking all the way up to my balls in one smooth motion."
        "Lexi moans as her pussy stretches around my cock."
        "Her head falls back into the lapping waves, as if she's surrendering herself to me."
        show lexi missionary speed vaginalhit
        "And all that's left now is to give her the pounding that she so rightly deserves!"
        "I take the soft sand and Lexi's eagerness as an excuse to go all out."
        "There's no gradual building up to it, I just start to thrust in and out of her."
        "She seems to be on the same page though, absorbing all I have to give like a sponge."
        "What she said to be beforehand keeps playing on my mind."
        "I can imagine all of those guys (and probably some girls too) staring at Lexi."
        "But none of them get to do this with her."
        "None of them get to fuck her brains out but me!"
        show lexi missionary pleasure
        lexi.say "Ah..."
        lexi.say "Ah...shit..."
        lexi.say "That's right..."
        lexi.say "I want... to be fucked... so I feel it... for a week!"
        "I'm doing the best I can to make her wish come true."
        "Already I feel like I'm pushing Lexi down into the wet sand with each thrust."
        "And soon enough, I see her eyes begin to glaze over and her tongue almost loll out of her mouth."
        show lexi missionary ahegao
        "Lexi's eyes roll upwards as she gets ever closer to cumming."
        "And I can't tell whether it's water or drool that's dripping off of her chin."
        show lexi missionary -vaginal -vaginalhit
        "The moment that I feel like I'm about to cum too, I yank my cock out of her pussy."
        "This makes Lexi almost curl up from the sensation, tipping her over the edge."
        with vpunch
        "She writhes in the grip of her orgasm as I kneel over her, unable to move an inch."
        show lexi missionary cum
        show chest_insert lexi cum zorder 1 at zoomAt(1, (840, 100))
        show belly_insert lexi cum zorder 1 at zoomAt(1, (20, 400))
        with vpunch
        "So there's no way she can avoid it when I shoot my load straight onto her belly and breasts."
        with vpunch
        "Almost instantly the waves begin to wash the cum off of her skin."
        "The white of the foam mixes and mingles with the white of the cum."
        "But all that Lexi can do is lie there."
        "Helpless as the last spasms of her orgasm make her twitch and convulse."
        hide chest_insert
        hide belly_insert
    $ lexi.sexperience += 1
    hide lexi
    return

label lexi_fuck_date_nightclub:
label lexi_fuck_vip:
label lexi_fuck_restroom:
label lexi_fuck_nightclub:
    $ game.play_music("music/roa_music/city_nights.ogg")
    show lexi
    lexi.say "What's up?"
    lexi.say "You look pretty miserable."
    mike.say "Ah, it's nothing - I guess I'm just a bit bored, that's all."
    show lexi annoyed
    lexi.say "Uuurrgh - bored people are the most boring thing ever!"
    lexi.say "You know what I do when I'm bored?"
    "I shake my head, noting the sudden wicked glint in Lexi's eyes."
    show lexi happy
    lexi.say "I make my own fun...so how about we sneak outside for a while?"
    lexi.say "You wanna fuck me behind a dumpster - maybe make me pop up like a Jack-in-the-box when I cum?"
    mike.say "Well...it's not really that I'm bored - more like tired."
    "Lexi chuckles in a wonderfully dirty manner and then shakes her head in mock disbelief."
    show lexi normal
    lexi.say "Like that's some kind of problem?!?"
    mike.say "Of course it is - I don't want to fall asleep before we're even halfway through!"
    lexi.say "Oh, don't worry about that."
    show lexi wink
    lexi.say "Just leave keeping you awake to me."
    show lexi normal at left4 with ease
    "She stands up and takes me firmly by the hand, clearly not taking no for an answer."
    mike.say "Where are we going?"
    lexi.say "Just follow me, and you'll see soon enough."
    "Lexi leads me across the dance-floor and into the corner of the club where the toilets are located."
    hide lexi
    show bg restroom
    show lexi at center
    with fade
    "There's nobody around and nobody further afield looking in our direction, and so she barges right into the closest toilet door."
    "As Lexi bundles me into an empty stall, I have no idea if we're in the men's or women's toilet."
    "Lexi hastily shoots the bolt on the door behind us and pushes me down onto the toilet seat."
    show lexi bj date normal nodick with fade
    "She kneels down on the less than sanitary tiled floor, seemingly unconcerned about our surroundings."
    "Her enthusiasm and the smile that's spreading across her face as she begins to unzip my flies speak volumes."
    "Taking the lead and performing a sex-act on a guy in such a public place is obviously very much Lexi's thing."
    "I guess the danger of someone walking in on us or there being a security camera trained on the cubicle the whole time only adds spice to the mix."
    "Not that my natural paranoia about being given a blowjob in such perilous circumstances seems to be stopping me from reciprocating her attentions."
    "Almost as soon as she has her hand inside of my pants and is groping around to pull my dick out, it's begins to stir to life."
    "By the time she only has it halfway out, it's already almost erect, and this makes getting it out more than a little awkward."
    "Lexi finally frees it by pulling it out mostly shaft first, making the head catch for a moment, before coming loose."
    hide lexi
    show lexi bj date normal
    with fade
    "Thanks to this, my cock waggles in her hand as she begins to massage it up and down."
    lexi.say "I thought it was gonna make a 'boing' sound when it popped up, like in a cartoon!"
    "I laugh nervously, but begin to feel genuinely more relieved once Lexi starts to put her mouth to another use."
    "She leans in to lick my cock, just above the scrotum."
    "Lexi's eyes are closed and she seems to be concentrating on nothing else as she uses her lips as well, almost lapping her way around the base."
    "From there she places her tongue on the same spot where she began, and slowly licks upwards."
    "She stops often, turning the lick into a brief kiss, before turning it back once more to climb ever higher."
    "By the time she reaches the head, I'm breathing heavily and trying not to start panting from the sensation."
    "Lexi had boasted to me on more than one occasion that she was exceptionally good at this."
    "But before now, I may have made the mistake of thinking that she was just boasting."
    show lexi bj suck
    show mouth_insert lexi zorder 1 at zoomAt(1, (820, 200))
    "Lexi slides her lips around the head, using it to part them as she takes my dick fully into her mouth for the first time."
    "She makes deliberately slow progress, drawing out every second so that it's as intense of an experience as she can make it."
    "I feel her teeth brush against the tip as it passes between them, and then her tongue wraps around the same part."
    menu:
        "Let her do her thing":
            "Lexi seems to know exactly what she's doing, and I have no complaints whatsoever."
            "I sit back and let her go to work on the shaft of my cock, feeling the fatigue of the day begin to melt away."
            show lexi bj closed
            "As she sucks and licks with expert precision, I can't help thinking of the times I've seen Lexi sucking on a lollipop."
            "I can't believe that I didn't make the obvious connection before this exact moment."
            "Feeling her doing the same to me now, I'll never be able to watch her do it again without getting massively turned on."
            "Lexi holds my eye as her lips travel up and down the shaft, a genuine pleasure in her big, blue eyes."
            "Her speed increases, and she breathes heavily as she takes me in and out, over and again."
            "I feel like she's almost insatiable, as though she'll never be able to stop what she's doing."
            "But all the same, I can already feel the urge to cum building up inside of me."
            "Lexi senses it too, and redoubles her efforts, trying to make me climax in the most dramatic way possible."
        "Take charge" if lexi.sub >= 50:
            $ lexi.sub += 1
            "I figure that, as Lexi's always boasting about how she's the queen of blowjobs, we skip the preliminaries and go straight to the deep-throat."
            show lexi bj deepthroat right closed
            "As soon as she has the tip of my cock in her mouth, I take hold of her hair and pull firmly downwards."
            "Lexi clearly either wasn't intending to give me deep-throat or else she wasn't quite ready."
            "But she recovers with a speed that surprises me, not gagging once on the head and shaft of my dick as I feel them slide down her throat."
            "I'd heard that it was possible to lose your gag-reflex with enough practice, and I guess that's just what Lexi's managed to do."
            "She can't move more than a few inches either way, but that doesn't seem to matter, as the sensation is already incredible."
            "But then she starts to do something with the muscles in her throat that takes me completely by surprise."
            "At first I'm worried that she's having some kind of spasm, choking on my cock, as her throat tightens again and again."
            show lexi bj deepthroat right open
            "I realise my mistake when I see there's no hint of panic on her face."
            "And then it occurs to me, she must be making her throat muscles clench on purpose."
            "The resulting squeezing is like nothing I've ever felt before, pushing me to within second of cumming."
    "I feel as though I can't hold myself back for another moment, and my orgasm suddenly takes hold."
    "There's no more than a second to decide where I want my cock to be when it actually happens."
    menu:
        "Cum in her mouth":
            $ f = False
            "The sensation of Lexi's tongue and lips around my dick is so nice that the last thing I want is to yank it out now."
            show mouth_insert lexi cum
            with vpunch
            "I feel myself cumming, she makes sure that she keeps me in her mouth the whole time."
            show lexi bj suck cum open with vpunch
            "Lexi takes it like a true professional, not trying to pull away or showing any signs of discomfort as I lose myself with her lips still wrapped around me."
            with vpunch
            "She holds my eye the entire time, accepting the situation and even making appreciative moans as best she can around my dick."
            "Once I'm done cumming, I pull back, sliding out of her mouth with tendrils of mixed saliva and cum trailing after me."
            hide lexi
            show lexi bj date showcum
            "Lexi opens her mouth so that I can clearly see the cum still pooled upon her tongue."
            show mouth_insert lexi -cum
            show lexi bj date swallow
            "And then, with a satisfied expression spreading across her face, she swallows the entire mess in one go."
            hide mouth_insert
        "Cum on her face":
            $ f = True
            "I can't honestly say what makes me think of pulling my cock out of the pleasant little hole that is Lexi's mouth."
            "But maybe it's the fact that she's always such a cocky little bitch, streetwise and sure of herself."
            "Perhaps that's what makes me want to see her face splattered with my cum quite so much?"
            hide mouth_insert
            hide lexi bj
            show lexi bj date normal
            "Lexi exhales noisily as I pull out of her mouth, able to breathe properly for the first time since it went in."
            show lexi bj cum with vpunch
            "But before she can get her breathing under control and compose herself at all, I cum with my cock an inch from her face."
            with vpunch
            "The angle of it means that my dick kicks upwards from the pressure, making sure it falls firstly on Lexi's hair and forehead."
            with vpunch
            "From there it spatters down into her eyes, making her crease her brows and squint as it temporarily blinds her."
            hide lexi
            show lexi bj date facial
            "Finally it dribbles down onto both cheeks and her nose, falling into her still open mouth and last of all off of her chin."
    hide lexi
    if f:
        show lexi date cum happy
    else:
        show lexi date blush
    with fade
    "Rather than feeling utterly spent, I find that the aftermath of the blowjob has left me on something of an odd temporary high."
    "For the first time all night, I feel like I'm re-energised and ready to actually enjoy the atmosphere of the nightclub."
    if f:
        "Lexi, in comparison, looks bedraggled and worn out, with sweat slicking her hair and cum spread over her face."
    else:
        "Lexi, in comparison, looks bedraggled and worn out, with sweat slicking her hair."
    mike.say "You're right, making your own fun is the best medicine for boredom."
    mike.say "Want to come dance...and maybe grab an energy drink too?"
    mike.say "You look like you could use it!"
    show lexi annoyed blush
    "Lexi rolls her head and groans at me in utter disgust."
    lexi.say "You've got to be kidding!"
    mike.say "Aww, don't be boring!"
    show lexi happy
    lexi.say "Fuck off!"
    "I try not to laugh as we stagger out of the cubicle, the toilet and back into the club."
    if f:
        "All the time wondering if having cum on your face could be a variation on the old phrase 'having egg on your face'."
    return

label lexi_fuck_date_male(location="hero", called_from_date=True):
    $ game.play_music("music/roa_music/city_nights.ogg")
    $ game.room = "bedroom1"
    scene bg bedroom1
    show lexi nophone
    $ lexi.flags.drugs = False
    $ lexi.flags.facecum = False


    call lexi_fuck_date_intro_male (location, called_from_date) from _call_lexi_fuck_date_intro_male


    call lexi_dick_reactions from _call_lexi_dick_reactions


    if lexi.sub >= 25:
        call lexi_fuck_date_foreplay_male from _call_lexi_fuck_date_foreplay_male
    $ skip_to_sleep = _return


    if not skip_to_sleep:

        call lexi_fuck_date_choices_male from _call_lexi_fuck_date_choices_male


        call handle_npc_leaving (lexi, _return) from _call_handle_npc_leaving_14
        if _return:
            $ lexi.flags.facecum = False
            return


    hide lexi
    call lexi_sleep_date_fuck_male (location) from _call_lexi_sleep_date_fuck
    $ lexi.flags.facecum = False
    return

label lexi_fuck_date_intro_male(location="hero", called_from_date=True):
    if lexi.sexperience:
        $ result = randint(1, 3)
        if result == 1:
            if called_from_date:
                "You can say what you like about being subtle and the need to keep some kind of mystery in a relationship."
                "But I find that argument tends to fall a little flat, especially when it comes to a girl the likes of Lexi."
                "Take the situation right here and now for a perfect example of what I mean."
                "We're just back from a date that went pretty well, even if I do say so myself."
                "And we've made it back to my place, shutting the door to my room behind us."
                "Some girls might have been coy about whether or not they intended to get physical at the end of the night."
                "But not Lexi, who's been telling me exactly what she wants me to do to her the whole way back."
                "And she's not stopped yet!"
            lexi.say "...and I want you to let me have all of it."
            show lexi wink
            lexi.say "Don't you go holding back a single fucking inch!"
            show lexi underwear with dissolve
            "Lexi's stripping off her clothes as she says this, flinging them aside with abandon."
            show lexi topless with dissolve
            "Not that such an act takes too long, based on the revealing nature of her clothing in general..."
            show lexi normal blush
            "I follow in her wake, trying to strip off myself while still staring at her progressively more naked body."
            mike.say "Sure, Lexi...sure."
            mike.say "That's what I had in mind too!"
            mike.say "Just let me get these damn things off..."
            show lexi naked with dissolve
            "As I struggle to make good on this promise, Lexi's already completely naked."
            "She distracts me further by crawling up and onto the bed, then turning over before me."
            "Lexi watches from this position as I tug off the last of my clothes."
            "And I don't know which is more of a turn-on - her smile or what I can see between her spread thighs."
        elif result == 2:
            "With some girls you have to be totally tuned into their wavelength to be able to know what they want one moment to the next."
            "Get it wrong and you're landing yourself in deep shit, and you'll be struggling to make it up to them for ages."
            "But that's one of the refreshing things about being with Lexi, she's not like that at all."
            "If she wants something, she tends to just come right out and say it in plain English."
            "Like right now, when she pretty much pounces on me the very moment my bedroom door closes behind us!"
            show lexi flirt
            lexi.say "Mmm..."
            lexi.say "Where is it?"
            show fx exclamation
            lexi.say "I want your cock!"
            "I almost stumble and fall as Lexi tugs at my pants."
            "She already has my flies open and starts reaching inside."
            mike.say "Okay, Lexi, okay!"
            mike.say "Just let me get into the room first!"
            show lexi wink blush
            "All this gets me is a positively filthy laugh from Lexi."
            "Well, that and a redoubled effort on her part to get her hands on my cock!"
            show lexi normal
            "But who am I trying to kid?"
            "It's not like I don't want her to get it!"
            "So I hurry to do all I can to help make it happen."
            lexi.say "Oh yeah..."
            lexi.say "That's more like it!"
            show lexi underwear with dissolve
            "Lexi offers no resistance as I begin to pull and tug at her clothes too."
            "Instead she helps me to strip her, first to the waist and then down to her bra and panties."
            "This means that by the time we collapse onto the bed, we're both ready to go."
            "Lexi's still giggling as she lies beneath me, the sound urging me on."
            "I watch as she reaches down and pulls aside the crotch of her panties."
            show lexi naked with dissolve
            "Which can only be an invitation to help myself to what lies between her thighs."
        else:
            "It's not hard to tell when Lexi's feeling horny and is up for some fun."
            "And it's not like she's ashamed of the fact or letting me know either!"
            "I mean, most girls are a little embarrassed to come right out with it."
            "Or else they have subtle ways of hinting that they want something from you."
            "But not Lexi!"
            show lexi flirt
            lexi.say "Come on, [hero.name]..."
            lexi.say "I wanna fuck!"
            "See what I mean!"
            "I smile and shake my head as I hear Lexi lay it on the line."
            "At least we're stepping into my bedroom as she comes out with it."
            "Not that she'd have shied away from saying it anywhere else."
            "Or in front of anyone else either!"
            mike.say "Okay, Lexi..."
            mike.say "I think we can make that happen!"
            show lexi happy
            "Lexi grins, letting out a snorting laugh as she does so."
            "It's a sound that should be pretty off-putting."
            "Yet somehow, coming out of her, it just sounds so hot!"
            "But the fact she's also stripping off could have something to do with it."
            "Lexi's not treating me to an elegant strip-tease either."
            show lexi topless with dissolve
            "She's literally pulling off her clothes and tossing them aside."
            lexi.say "Come on, [hero.name]..."
            show lexi annoyed
            lexi.say "Whadda ya waiting for?"
            "I shake my head, trying to snap back to reality."
            "At the same time I'm doing the best I can to get undressed too."
            mike.say "Cut me some slack, Lexi."
            mike.say "You're getting naked right in front of me."
            mike.say "It's pretty hard to do anything other than watch you!"
            "Lexi snorts with laughter again."
            show lexi normal naked with dissolve
            "But that doesn't stop her pulling down her panties."
            "Then she kicks them aside and walks over to me."
            lexi.say "Well you'd better do more than that."
            lexi.say "Like I said, I don't want you to stare at me."
            show lexi flirt
            lexi.say "I want you to fuck my brains out!"
            mike.say "Fuck sake, Lexi!"
            mike.say "You've got such a way with words!"
            show lexi happy
            lexi.say "Ah, shut up and do me!"
            "With that, Lexi closes the last of the distance between us."
            "Then she pretty much pounces on me!"
        if lexi.is_visibly_pregnant:
            "She rubs her hand underneath her pregnant belly, sticking out of her short top."
            "Even after I knocked her up earlier, she didn't want to change her wardrobe."
            "That's fine."
            "It really shows how trailer trash she is, and that's why I like her."
            "Immediately, she turns to me, grabbing my crotch and pressing her chest up against mine."
            "Her swollen breasts poke at my body, and I feel a tiny squirt of moisture on my shirt."
            lexi.say "So, why don't you and I get more comfortable?"
        elif "drugs" in hero.inventory:
            menu:
                "Offer drugs":
                    $ lexi.flags.drugs = TemporaryFlag(True, "day")
                    $ lexi.love += 5
                    $ hero.lose_item("drugs")
                    "My gaze happens to fall on the bedside table, where there's still a mirror and a rolled bill."
                    "A little white powder still clings to the mirror, betraying it's use."
                    "Normally I'd hide that stuff away for fear of someone seeing it and knowing about my habit."
                    "But as my gaze turns back to Lexi, it strikes me that she's not exactly the puritanical type."
                    mike.say "Hey, Lexi - you want something to...spice things up?"
                    show lexi surprised
                    show fx question
                    "Lexi looks at me with a puzzled expression on her face, unsure of just what I mean."
                    "But when she follows my gaze back to the mirror and bill, her eyes light up with recognition."
                    hide fx
                    show lexi normal
                    lexi.say "Well, aren't we full of surprises, [hero.name]!"
                    lexi.say "Sure thing - just line it up."
                    "I don't waste any time in getting the shit out and doing as she asks."
                    "And much as I expected, Lexi rolls over to the bedside table and helps herself eagerly."
                    show lexi wink blush
                    "A part of me winces at the value of what just disappeared up her nose like dust into a vacuum cleaner."
                    "But I keep reminding myself of the potential pay-off involved here."
                    "Once she's done, Lexi shakes her head and blows air out of her nose like a doped-up horse."
                    show lexi happy
                    lexi.say "Whooo!"
                    lexi.say "That's some good shit!"
                    "At first I don't see any noticeable change in Lexi."
                    show lexi flirt -blush
                    "But then her pupils begin to dilate, and she starts staring hungrily at my cock."
                    lexi.say "It's gonna get really fuckin' hot in here in a hot minute, [hero.name] You want a hit?"
                    menu:
                        "Accept":
                            $ lexi.love += 1
                        "Reject":
                            mike.say "Nah..."
                            mike.say "I want remember how fucked up you are without fucking myself up."
                            "I say as I sit there, waiting for her to continue."
                    lexi.say "Now, where were we..."
                "Don't":
                    pass
        else:
            "After all, both of them involve lips that are moist and glistening in the subdued light of the room."
            "And both of them are places where I'd be more than happy to stick either my cock or tongue!"
    else:
        "Lexi glances around my room. I can't tell if she's looking for something to pawn off, or judging me by my tastes."
        mike.say "So, what do you think?"
        lexi.say "Shucks, [hero.name]!"
        lexi.say "I'm just ready for a wild time, and you got a nice bed."
        if lexi.is_visibly_pregnant:
            "She rubs her hand underneath her pregnant belly, sticking out of her short top."
            "Even after I knocked her up earlier, she didn't want to change her wardrobe."
            "That's fine."
            "It really shows how trailer trash she is, and that's why I like her."
            "Immediately, she turns to me, grabbing my crotch and pressing her chest up against mine."
            "Her swollen breasts poke at my body, and I feel a tiny squirt of moisture on my shirt."
            show lexi wink
            lexi.say "So, why don't you and I get more comfortable?"
        elif "drugs" in hero.inventory:
            menu:
                "Offer drugs":
                    $ lexi.flags.drugs = TemporaryFlag(True, "day")
                    $ lexi.love += 5
                    $ hero.lose_item("drugs")
                    "I chuckle as she gropes me, but I pat her on the cheek, looking over towards my bedside table."
                    mike.say "Now, hold on there, Lexi. There's something you're probably going to want to see in that drawer first."
                    "Lexi quirks an eyebrow and pulls herself away from me a moment."
                    "She sways off and bends down, her short shorts unable to hide her booty as she bends over to look in the drawer."
                    show lexi surprised
                    show fx exclamation
                    lexi.say "Oh fuck, [hero.name]!"
                    "She gasps, pulling out the bag I had in my drawer."
                    hide fx
                    show fx question
                    lexi.say "When the hell did you get this!?"
                    "Thought a girl like you would like a little extra excitement."
                    show lexi normal
                    lexi.say "Shucks, you're a big time party animal now, [hero.name]. Quick, get me a credit card or something, fast!"
                    "I hand her the card and she sits on the bed, quickly lining up the powder just right."
                    lexi.say "It's been too fuckin' long since my last hit!"
                    lexi.say "Danny never let me try the product, not without fuckin' someone first."
                    mike.say "Well..."
                    mike.say "You are going to be fucking me, so..."
                    lexi.say "Oh, shut up, you!"
                    "She rolls up a dollar bill to the perfect consistency."
                    show lexi wink
                    "She takes in a nice, big snort, and immediately her eyes roll back."
                    show lexi flirt
                    lexi.say "Oh, fuck me that's good shit!"
                    lexi.say "It's gonna get really fuckin' hot in here in a hot minute, [hero.name] You want a hit?"
                    menu:
                        "Accept":
                            $ lexi.love += 1
                        "Reject":
                            mike.say "Nah..."
                            mike.say "I want remember how fucked up you are without fucking myself up."
                            "I say as I sit there, waiting for her to continue."
                "Don't":
                    pass
    "She leads me over towards the bed and immediately lifts her top up off of her."
    if lexi.is_visibly_pregnant:
        "Who would have ever thought that the drug dealing con artist would ever have the curves of motherhood—the full breast, the baby bump."
        "It suits her well, though I'll no doubt end up being the responsible parent."
        "Wasting no time, she undoes her shorts and shimmies out of them and her thong, leaving herself naked."
        "It takes her a little longer than she normally does, but that comes with the territory of the added baby weight."
        lexi.say "Well, come on."
        lexi.say "Don't waste my time now."
        lexi.say "Let me see that dick that done knocked me up."
        lexi.say "Just cause I got a baby on board don't mean I don't crave a taste!"
    else:
        lexi.say "Well, come on."
        lexi.say "Don't waste my time now."
    if lexi.flags.drugs:
        lexi.say "Haha, okay! Well, I'm gonna devour that dick!"
        "Her eyes are wide and filled with lustful hunger."
    "I get out of my own clothing really quickly and lay naked on my bed."
    return

label lexi_fuck_date_foreplay_male:
    menu:
        "Have her suck you off" if lexi.sub >= 25:
            call lexi_fuck_date_blowjob from _call_lexi_fuck_date_blowjob
        "Fuck her":
            return
    call stop_all_sfx from _call_stop_all_sfx_25

    return _return

label lexi_fuck_date_choices_male:
    menu:
        "Missionary":
            call lexi_fuck_date_missionary (0) from _call_lexi_fuck_date_missionary
        "Standing" if hero.sexperience >= 5:
            call lexi_fuck_date_standing (5) from _call_lexi_fuck_date_standing
        "Cowgirl" if hero.sexperience >= 10:
            call lexi_fuck_date_cowgirl (10) from _call_lexi_fuck_date_cowgirl
        "Doggy" if hero.sexperience >= 15:
            call lexi_fuck_date_doggy (15) from _call_lexi_fuck_date_doggy
    call stop_all_sfx from _call_stop_all_sfx_26

    return _return

label lexi_fuck_date_blowjob:
    $ lexi.sub += 1
    "She smirks as she climbs down onto her knees in front of me."
    show lexi bj bedroom naked nodick with fade
    "She sighs as she lowers herself, nodding once she's all settled into position."
    if lexi.is_visibly_pregnant:
        lexi.say "Whoo... not as easy as before, [hero.name] and that's all yer fault, daddy."
    "All I can see of her between my legs is her smiling face."
    if lexi.is_visibly_pregnant:
        lexi.say "Alright, [hero.name], They say there's strange cravings when a gal is bred, and I'm hankerin' for some of this dick of yers!"
    hide lexi
    show lexi bj bedroom naked
    "She snickers and then leans in, rolling her tongue out and licking up along my shaft."
    show lexi bj suck
    show mouth_insert lexi zorder 1 at zoomAt(1, (820, 200))
    if lexi.flags.drugs:
        "It's incredible how fast she can lick me, going over my shaft over and over again, as if I was a popcicle in danger of melting."
        "She growls and gasps with each lick, acting like a wild animal, hungry for more!"
    "I groan, letting her have her fun for now."
    "She keeps her hands away from my cock, instead holding onto my thighs and just wrapping her lips around my flesh."
    show lexi bj suck closed
    "The feeling is wonderful as she bobs her head up and down, sucking gently upon my skin as she slides her lips and tongue along my body."
    if lexi.flags.drugs:
        show lexi bj deepthroat closed
        "Damn, the way she's going at me like a jackhammer is bound to make me explode sooner than later."
        "There's no way I'm letting this coked up slut make me finish now, is there?"
    else:
        "Damn, she's not doing anything crazy, but just with her technique and the look she gives me, it's enough to make me explode."
        "But I can't let it end without me doing anything, can I?"
    menu:
        "Let her finish":
            "She's already doing a great job."
            "I should just let her keep going."
            if lexi.flags.drugs:
                "She growls as she pulls free from my cock just at the perfect moment, her crazed expression staring up at mine, revealing a slight sadistic glee as she stares back up at me."
            else:
                "She hums as she pulls her mouth free from my cock, just at the perfect moment."
            "I gasp, unable to hold back."
            hide mouth_insert
            hide lexi
            show lexi bj bedroom naked
            "She knows exactly when to finish a guy off, and I lift my hips just slightly, unable to control myself as I explode all over her face!"
            hide lexi
            show lexi bj bedroom naked facial with vpunch
            if lexi.flags.drugs:
                "She squeals as my hot cum coats her, and then laughs, giggling like an idiot as she rubs her fingers over her cum-soaked face."
                with vpunch
                "Her eyes roll back, her face plastered with a manic smile as she revels in her cum-drenched face."
                lexi.say "Oh, fuck yes!"
                lexi.say "I've never felt more alive! Come on, stud. Finish me off!"
            else:
                "She squeals as my hot cum coats her, dribbling down along her cheeks and chin."
                with vpunch
                "She snickers and then leans in, placing another kiss on my cock."
                lexi.say "Oh, yeah, you're a real stud—a real animal [hero.name]."
                if lexi.is_visibly_pregnant:
                    "But just because you shot true with me before, daddy, don't mean I don't want it, so you'd better be ready for the next round!"
            scene bg bedroom1
            show lexi naked cum
            if hero.fitness < 50:
                "My eyes get heavy, and a sudden rush of weariness takes me."
                "Falling back on the bed, I sigh out with a satisfied, yet tired breath."
                if lexi.flags.drugs:
                    lexi.say "H-Hey, [hero.name]!"
                    lexi.say "No, don't fall asleep on me already!"
                    "She groans, wrapping her arms around herself."
                    lexi.say "Fuck, man, I'm still riding high."
                    lexi.say "You can't leave me hanging like this."
                    "She collapses on the bed as I drift off."
                    "I can hear her touching herself, groaning in frustration as I drift off into the land of dreams."
                    $ lexi.love -= 5
                else:
                    lexi.say "H-Hey, [hero.name]. You aren't tuckered out are ya!?"
                    lexi.say "Shucks that's all you can handle?"
                    lexi.say "Damn, and here I thought you could take me all the way."
                    lexi.say "Guess I'll see myself out, then!"
                $ lexi.love -= 5
                $ lexi.flags.facecum = True
                return "skip_to_sleep"
        "Take control" if hero.sexperience >= 25:
            if not lexi.is_visibly_pregnant:
                "Oh, she think she can be the only one who can steer this relationship?"
                "She has another thing coming!"
            else:
                "Sorry, Lexi, but you lost control when I knocked you up."
            show lexi bj left right
            "I grab her by the hair and she gasps, closing one eye and looking up to me with a surprised gurgle."
            "I'm close—I can tell she has been planning to finish me off, but she's not going to finish without giving me a real gift!"
            menu:
                "Time to let her have it!":
                    show lexi bj deepthroat open with vpunch
                    "I pull her in, and she squeals around my cock as I bring her up to my crotch."
                    with vpunch
                    "Her cheeks puff out and her throat bulges as my dick slams deep into her throat."
                    if lexi.flags.drugs:
                        "Her eyes roll back, and in her drug-crazed stupor, she seems to be delivered to another world of pleasure as I release, shooting globs down deep into her."
                    show lexi bj cum
                    show mouth_insert lexi cum zorder 1 at zoomAt(1, (820, 200))
                    with vpunch
                    "Once I finish, we hold on there together for a bit, and I let go of her."
                    if lexi.flags.drugs:
                        "She pushes herself free, gasping, coughing, spitting up some of my jizz as her whole body trembles from the excitement and energy from the stimulant coursing through her."
                    hide mouth_insert
                    hide lexi
                    show lexi bj bedroom naked
                    lexi.say "D... damn!"
                    if lexi.flags.drugs:
                        lexi.say "I really am trash to you? I love it!"
                    else:
                        "She gasps, rubbing her neck."
                        lexi.say "You sure are rough...!"
                    scene bg bedroom1
                    show lexi naked cum
                    if hero.fitness < 50:
                        "My eyes get heavy, and a sudden rush of weariness takes me."
                        "Falling back on the bed, I sigh out with a satisfied, yet tired breath."
                        if lexi.flags.drugs:
                            lexi.say "H-Hey, [hero.name]!"
                            lexi.say "No, don't fall asleep on me already!"
                            "She groans, wrapping her arms around herself."
                            lexi.say "Fuck, man, I'm still riding high."
                            lexi.say "You can't leave me hanging like this."
                            "She collapses on the bed as I drift off."
                            "I can hear her touching herself, groaning in frustration as I drift off into the land of dreams."
                            $ lexi.love -= 5
                        else:
                            lexi.say "H-Hey, [hero.name]. You aren't tuckered out are ya!?"
                            lexi.say "Shucks that's all you can handle?"
                            lexi.say "Damn, and here I thought you could take me all the way."
                            lexi.say "Guess I'll see myself out, then!"
                        $ lexi.love -= 5
                        return "skip_to_sleep"
                "Maybe I should pace myself?" if hero.fitness >= 50:
                    if lexi.flags.drugs:
                        "She looks up to me with hyper focused and shaking eyes, wondering what I'm going to do with this newfound control."
                    else:
                        "She looks up to me with pleading eyes, wondering what I'm going to do with this newfound control."
                    hide sexinserts
                    hide lexi
                    show lexi bj bedroom naked
                    "I show her, pulling her head free from my grasp."
                    "She gasps once she has the air and pants, her chest rising and falling as she scans my eyes for an answer."
                    "She grits her teeth when I can't give it to her right away, her whole body a jittery mess in my grasp."
                    "She's eager for more before her crash, but we're not playing on her time."
                    "I smirk at her."
                    mike.say "We're not done yet, miss."
                    mike.say "No way I'm wasting myself on your throat today."
                    if lexi.is_visibly_pregnant:
                        mike.say "You know damn well where I like to cum, 'mommy'."
    return

label lexi_fuck_date_missionary(sexperience_min):
    scene lexi missionary with fade
    "Lexi lies on the bed before me, legs spread and an expression on her face that says she's tired of waiting."
    "And there's no way that I want to keep her from getting what she wants for a second more than I have to..."
    if game.week_day % 2 == 0:
        menu:
            "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
                $ lexi.sub += 1
                "Lexi's wide open right now, just waiting for me to take her."
                "Her pussy's already wet enough for me to slide straight in there."
                "But my eye keeps getting drawn to what lies between her buttocks."
                "Maybe it's on account of the fact that she's a pretty crazy girl."
                "Or maybe I just like the idea of taking her completely by surprise."
                show lexi missionary anal pleasure
                "But either way, I spread Lexi's ass apart and push my cock straight up there."
                lexi.say "Whoa..."
                lexi.say "My ass!"
                "By now my cock is almost half the way up her butt, squeezed tight by her muscles."
                "And the sound of her feeling that same sensation from the other side is a massive thrill."
                if lexi.flags.drugs:
                    "Lexi moans as her already glazed eyes roll back into her head."
                    "The sounds that she makes are pretty animalistic and wild."
                    "But they seem to be coming from a place of pleasure, so I press on with what I'm doing."
                else:
                    lexi.say "Mmm..."
                    lexi.say "No one's fucked my ass in SO long!"
                    lexi.say "That feels REAL good..."
                "While Lexi's ass is clenching tighter by the moment, the same can't be said for the rest of her."
                "In contrast, her entire body seems to become floppy and limp."
                "She lays sagging on the bed before me, absorbing each and every thrust like a sponge."
                "I doubt she could speak a word right now, even if the urge took her."
                "And instead her Lexi's mouth hangs wide open, her tongue almost lolling out of it."
                "I mean, I know a lot of girls are really into anal."
                "But this is like the sensation's enough to melt Lexi completely."
                "Enough to turn her into a pool of insensible goo!"
                "And speaking of viscous fluids..."
                "I become aware of the fact that I'm about to cum!"
                call cum_reaction (lexi, 'anal', sexperience_min) from _call_cum_reaction_111
                if _return == "anal_inside":
                    $ lexi.love += 1
                    "I make one last Herculean effort to pound Lexi's asshole."
                    show lexi missionary cum with hpunch
                    "And when I'm as deep as I can get, I let myself go inside of her."
                    with hpunch
                    "Suddenly, her eyes flick open, as if she's been shocked awake."
                    with hpunch
                    if lexi.flags.drugs:
                        "Lexi fixes me with a vacant stare, almost freaking me out."
                        "She twitches and gasps as I keep thrusting into her."
                        "But I honestly have no idea if she's even aware of what's happening to her."
                    else:
                        lexi.say "Oh..."
                        lexi.say "Oh wow..."
                        lexi.say "I feel you knocking - and you just came in!"
                    "In the last few moments before it's over, I enjoy the lingering sensation of being in her ass."
                    "But then all too soon, I feel myself dwindling."
                    "And the only sound is that of our heavy breathing."
                elif _return == "anal_outside":
                    $ lexi.sub += 1
                    show lexi missionary outside
                    "I whip my cock out of Lexi's ass in the nick of time."
                    "And she barely has time to gasp in surprise before I cum."
                    show lexi missionary cum with hpunch
                    "Streamers of sticky, white semen stripe Lexi's belly, some even reaching her breasts."
                    with hpunch
                    "Suddenly, her eyes flick open, as if she's been shocked awake."
                    with hpunch
                    if lexi.flags.drugs:
                        "Lexi fixes me with a vacant stare, almost freaking me out."
                        "She twitches and gasps, I guess from the sensation of me pulling out."
                        "But I honestly have no idea if she's even aware of what's happening to her."
                    else:
                        lexi.say "Oops!"
                        lexi.say "Looks like someone had an accident!"
                        "Lexi laughs, and then rubs her hands over her belly, spreading the cum all over her."
                    "I stand there, looking down at her and panting heavily."
                    "The only other sound I can hear is that of Lexi panting herself."
                $ lexi.flags.anal += 1
            "Fuck her pussy":
                show lexi missionary outside
                "I think I finally decided which pair of lips on Lexi I simply can't resist."
                "Especially when they're glistening like you'd see a precious jewel shine!"
                "Lexi's ass can wait, as it's her pussy that I want tonight..."
                call check_condom_usage (lexi, love=180) from _call_check_condom_usage_77
                if _return == False:
                    return
                if CONDOM:
                    show lexi missionary condom
                "Not wanting to waste another second, I begin to rub my cock against the lips of Lexi's pussy."
                "Even on the outside, the feeling is simply incredible against the sensitive shaft."
                "Lexi's folds are soft to the touch and already delightfully slippery too."
                "She purrs appreciatively as I tease her with my cock, burbling almost to herself."
                if lexi.flags.drugs:
                    lexi.say "Why don't you fuck me already?"
                    "Lexi seems to be enjoying what I'm doing to her."
                    "But I feel the urge to go further."
                    "Every stroke of my cock make me want to stick it in her."
                else:
                    "But then she smiles, eyes settling upon me."
                    lexi.say "Stop playing with me, [hero.name]."
                show lexi missionary vaginal
                "And so I do just that, pulling back and then pushing into Lexi, almost in one motion."
                "Lexi arches her back as I slowly sink my cock into her as far as it can go."
                "She makes no sound other than a low moan, which become more intense the more I fill her."
                show lexi missionary vaginalhit pleasure
                "Once I'm finally balls deep in Lexi, I stay there for as long as I can."
                "The feeling of her around my cock is incredible, even without the need to move in inch."
                "And in addition to this, she begins to twitch and writhe beneath me too."
                "From there I begin to move slowly in and out of her, enjoying the way she responds."
                "Lexi matches me almost move for move, becoming more animated the faster I go."
                "The sounds coming out of her are still nowhere close to being actual words."
                show lexi missionary speed
                "In fact, they remind me more of animalistic noises of pleasure and pleading."
                "But it's not like I need any kind of encouragement to keep giving her what she wants."
                show lexi missionary ahegao
                "Suddenly, Lexi starts to almost yelp, and her entire body bucks under me."
                "The only explanation I can think of is that she's about to cum."
                "And the knowledge that I've brought her to a climax sets me off too..."
                call cum_reaction (lexi, 'vaginal', sexperience_min) from _call_cum_reaction_112
                if _return == "vaginal_condom":
                    $ lexi.sub += 1
                    "I can enjoy the last few moments inside of Lexi without any sense of fear."
                    with hpunch
                    "And I do just that, holding on as I cum and riding out the whole thing."
                    with hpunch
                    "Lexi too seems to appreciate those final seconds before it's all over."
                    with hpunch
                    if lexi.flags.drugs:
                        "She pants and moans like an animal once again."
                        "But this time her cries have a definite sense of finality to them."
                    else:
                        lexi.say "Oh, yeah..."
                        lexi.say "That's it..."
                    "And then her head falls back onto the bed, her energies utterly spent."
                elif _return == "vaginal_outside":
                    $ lexi.sub += 1
                    "For all that I want to keep on going until the very last, I know that I can't."
                    show lexi missionary outside -vaginalhit
                    "Even so it's no small challenge to pull my cock out of Lexi before it's too late."
                    with hpunch
                    "This means that I cum almost the same moment that I'm free of her."
                    show lexi missionary cum
                    show belly_insert lexi cum zorder 1 at zoomAt(1, (20, 400))
                    with hpunch
                    "My cock sends its load spattering across her stomach and down over her thighs."
                    with hpunch
                    if lexi.flags.drugs:
                        "Lexi makes a satisfied noise at this, and even a vague smile."
                        "And then she stretches like a satisfied cat."
                    else:
                        "Lexi laughs as she's showered with cum, smiling gleefully the whole time."
                        "She rubs her hands over her belly, smearing it across her already sweat-soaked skin."
                elif _return == "vaginal_inside_pill":
                    $ lexi.love += 2
                    if lexi.flags.drugs:
                        "I remember suddenly that Lexi's on the pill right now."
                        "So there's no need to worry about pulling out."
                    else:
                        lexi.say "Don't stop now..."
                        lexi.say "I'm on the pill!"
                    show lexi missionary cum with hpunch
                    "So I don't stop, and instead feel the fantastic sensation of cumming inside of her."
                    with hpunch
                    "I can tell that Lexi feels it too, as she lets out a cry of sensual satisfaction a moment later."
                    with hpunch
                    "And so I ride my orgasm to the very last, until we're both utterly spent."
                elif _return == "vaginal_inside_pregnant":
                    $ lexi.love += 3
                    "I've been practically leaning on Lexi's swollen belly this whole time."
                    "So I hardly need a reminder that there's no danger in failing to pull out."
                    show lexi missionary cum with hpunch
                    "Instead I gently ride out my orgasm deep inside of her, enjoying every last moment."
                    with hpunch
                    "And she seems to appreciate it too, moaning and sighing to the very end."
                    with hpunch
                    "Afterwards, Lexi curls into a tight little ball, clutching at her belly and its precious contents."
                elif _return == "vaginal_inside_mad":
                    $ lexi.love -= 1
                    $ lexi.sub += 5
                    show lexi missionary cum with hpunch
                    "Lexi's eyes are squeezed tightly closed as I lose myself inside of her."
                    show lexi missionary ahegao with hpunch
                    "And I can see from the expression on her face that she's loving every moment."
                    $ lexi.impregnate()
                    show lexi missionary normal with hpunch
                    "But then those same eyes suddenly open, and her expression becomes one of shock and even horror."
                    lexi.say "Ah, [hero.name]..."
                    lexi.say "Did you just cum in me?"
                    lexi.say "Did you just cum in me without a condom?!?"
                    "After that, all we can do is stare at each other, as the gravity of the situation slowly dawns on us."
                elif _return == "vaginal_inside_happy":
                    $ lexi.love += 5
                    "I make to pull my cock out of Lexi, but she wraps her legs tightly around me."
                    "Surprised by this, I struggle to free myself before it's too late."
                    show lexi missionary cum with hpunch
                    "But the process is already in motion, and I cum inside of her a moment later."
                    with hpunch
                    "Lexi rides the entire thing out with a look of delight on her face."
                    with hpunch
                    "And she clings to me so there's no chance of her losing even a single drop."
                    $ lexi.impregnate()
                    "Afterwards, she slides off of my cock, a look of deep satisfaction on her face."
                    "Which is in stark contrast to the one of shock and confusion on mine..."
    else:
        menu:
            "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
                $ lexi.sub += 1
                "I can see Lexi's pussy, already glistening and slick."
                "But then I catch sight of her tight little ass-hole too."
                "And in that instant, my mind's made up."
                "She's not the only one that can be spontaneous around here!"
                "The head of my cock barely brushes Lexi's lips as it passes by her pussy."
                "And she yelps in surprise a second later, as my intentions become clear."
                show lexi missionary anal
                lexi.say "Oh, [hero.name]..."
                lexi.say "You want my ass?!?"
                "By way of answer, I thrust groin forwards, driving myself home."
                lexi.say "Ooo..."
                lexi.say "Oh my, you really do want my ass!"
                lexi.say "Not gonna take no for an answer, are you!"
                show lexi missionary pleasure
                "Lexi's words become a moan as I push my way into her."
                "The sensation of her muscles as they squeeze and clench in protest is amazing."
                "And the resistance that her body puts up only urges me onwards."
                lexi.say "Oh fuck..."
                lexi.say "You can have my ass..."
                lexi.say "It's all yours to fuck!"
                "Like I already said, Lexi's giving me more than enough encouragement."
                show lexi missionary speed
                "And pretty soon I'm thrusting in and out of her with all the energy I can muster."
                "Her entire body moves in sympathy with the force of my motions."
                "Lexi's breasts bounce like rubber balls and her thighs sway and slap against mine."
                "The resistance of her muscles begins to melt away."
                "She surrenders to the experience, losing the power of speech once more."
                "Lexi's eyes have been open this whole time."
                show lexi missionary ahegao
                "But now they start to roll upwards as she zones out."
                "I swear that there's actually drool running out of her mouth and down her chin!"
                "Even the moans that she's making are in time with me pushing into her."
                "But even though Lexi seems to be on the verge of passing out, I'm still in possession of my senses."
                "And I know that I'm going to cum any second now!"
                call cum_reaction (lexi, 'anal', sexperience_min) from _call_cum_reaction_113
                if _return == "anal_inside":
                    $ lexi.love += 1
                    show lexi missionary cum with hpunch
                    "Once I do let go and shoot my load into Lexi, she really loses it."
                    with hpunch
                    "Her head falls back onto the mattress, eyes closed and mouth lolling open."
                    with hpunch
                    "It doesn't take long until she's full to bursting with cum."
                    "This means that it begins to seep out of her ass around the shaft of my cock."
                    "Exhausted by my efforts, I can barely keep myself from collapsing."
                    "And the only sound that can be heard is that of our own breath coming gasps and pants."
                elif _return == "anal_outside":
                    $ lexi.sub += 1
                    show lexi missionary outside
                    "Gasping with the effort, I manage to pull my cock out of Lexi's ass the moment before I cum."
                    "She hardly seems to notice at first, lost as she is in the throes of her own orgasm."
                    show lexi missionary cum with hpunch
                    "But when I shoot my load over her belly, the spattering on her skin makes her eyes flicker open."
                    with hpunch
                    "Lexi can't seem to gather her wits enough to actually say as much as a single word."
                    with hpunch
                    "Though she does smile up at me, a faraway look in her eyes."
                    "And one that I choose to take as meaning that she's satisfied and happy."
                $ lexi.flags.anal += 1
            "Fuck her pussy":
                "I can see Lexi's pussy, already glistening and slick."
                "And I don't need anymore of an invitation than that."
                "I brush the head of my cock against Lexi's lips."
                "An action that rewards me with a little yelp of surprise."
                call check_condom_usage (lexi, love=180) from _call_check_condom_usage_78
                if _return == False:
                    return
                "But as wet and willing as Lexi seems to be, I still have to work for my reward."
                "Her pussy puts up a token resistance as I try to push my way into her."
                show lexi missionary vaginal
                "All this means is that I become more determined than ever to do just that."
                "And pretty soon, the sounds coming out of Lexi are almost desperate moans."
                "Her words are strained and stifled by the sensations of what I'm doing to her."
                lexi.say "Yeah..."
                lexi.say "Oh yeah..."
                lexi.say "Keep pushing - don't stop now!"
                "It's not like I need the encouragement."
                "But the need in Lexi's voice is turning me on all the more."
                "I make one massive effort to push into her."
                "And a second later, I feel all resistance give way."
                "I sink all the way into Lexi, as deep as I can possibly go."
                show lexi missionary vaginalhit
                lexi.say "Fuck, yes!"
                lexi.say "That's it - that's what I want!"
                lexi.say "Fuck me, [hero.name]...please!"
                "Eager to please, I begin to move inside of Lexi."
                "The energy that was needed to overcome her resistance wasn't all that I had to give."
                show lexi missionary speed
                "And she soon discovers that fact when I start to pound away as hard as I can."
                "We're not making gentle love here, we're fucking like a couple of animals in heat."
                show lexi missionary pleasure
                "By now Lexi's panting like a bitch, her entire body bouncing and jiggling before me."
                "I don't know whether to stare at the way her breasts sway or her hips slap against mine."
                "Or else look her in the face and watch as her eyes begin to roll back into her head."
                "I said that I felt like I had plenty left in the tank for this."
                "But that still doesn't mean I can keep nature from taking it's course!"
                call cum_reaction (lexi, 'vaginal', sexperience_min) from _call_cum_reaction_114
                if _return == "vaginal_condom":
                    $ lexi.sub += 1
                    "Thankful that we used a condom, I feel no guilt in just keeping on going."
                    "Which means that I pound away into Lexi until the very moment that I cum."
                    show lexi missionary ahegao with hpunch
                    "She twitches and squirms on the end of my cock, absorbing the whole thing like a sponge."
                    with hpunch
                    "Then her own back arches and she begins to cum too."
                    with hpunch
                    "We end with her pinned beneath me, the both of us panting in sheer exhaustion."
                elif _return == "vaginal_outside":
                    $ lexi.sub += 1
                    "I've struggled to keep in mind the fact that I'm not wearing a condom."
                    show lexi missionary outside big -vaginalhit
                    "But even so, I only just manage to remember in time before I actually cum."
                    show lexi missionary outside cum big ahegao with hpunch
                    "Lost as she is in the throes of her own orgasm, Lexi hardly seems to notice."
                    with hpunch
                    "But when I shoot my load over her belly, the spattering on her skin makes her eyes flicker open."
                    with hpunch
                    "Lexi can't seem to gather her wits enough to actually say as much as a single word."
                    "Though she does smile up at me, a faraway look in her eyes."
                    "And one that I choose to take as meaning that she's satisfied and happy."
                elif _return == "vaginal_inside_pill":
                    $ lexi.love += 2
                    lexi.say "Don't stop now..."
                    lexi.say "I'm on the pill!"
                    "I feel no guilt in just keeping on going, pounding Lexi until the moment I cum."
                    show lexi missionary cum with hpunch
                    "She twitches and squirms on the end of my cock, absorbing the whole thing like a sponge."
                    show lexi missionary ahegao with hpunch
                    "Then her own back arches and she begins to cum too."
                    with hpunch
                    "We end with her pinned beneath me, the both of us panting in sheer exhaustion."
                elif _return == "vaginal_inside_pregnant":
                    $ lexi.love += 3
                    "Her swollen belly beneath me, I feel no guilt in just keeping on going."
                    show lexi missionary cum with hpunch
                    "Which means that I pound away into Lexi until the very moment that I cum."
                    show lexi missionary ahegao with hpunch
                    "She twitches and squirms on the end of my cock, absorbing the whole thing like a sponge."
                    with hpunch
                    "Then her own back arches and she begins to cum too."
                    "We end with her pinned beneath me, the both of us panting in sheer exhaustion."
                elif _return == "vaginal_inside_mad":
                    $ lexi.love -= 1
                    $ lexi.sub += 5
                    show lexi missionary cum with hpunch
                    lexi.say "Wait..."
                    with hpunch
                    lexi.say "No condom!"
                    show lexi missionary normal with hpunch
                    "I shoot my load into Lexi the very same moment that she speaks the words."
                    "And I see the growing look of horror on her face as, unable to stop, I fill her with all I have."
                    "As soon as she can, Lexi wriggles out from under me, cursing under her breath."
                    lexi.say "You dumb sonofabitch!"
                    lexi.say "If I get pregnant from this..."
                    lexi.say "Just you wait!"
                    $ lexi.impregnate()
                elif _return == "vaginal_inside_happy":
                    $ lexi.love += 5
                    lexi.say "Wait..."
                    lexi.say "Don't pull out, please!"
                    show lexi missionary cum with hpunch
                    "I shoot my load into Lexi the very same moment that she speaks the words."
                    show lexi missionary ahegao with hpunch
                    "And I see the growing look of satisfaction on her face as I fill her with all I have."
                    with hpunch
                    lexi.say "Mmm..."
                    lexi.say "I can feel you inside me - like our baby's already growing in there!"
                    "Stunned into silence, I can only nod my head at this."
                    "But all the time my mind is racing as to what this means and why Lexi wanted me to do it."
                    $ lexi.impregnate()
    return

label lexi_fuck_date_cowgirl(sexperience_min):
    lexi.say "Someone knows what they want, don't they?"
    "All I can do is smile dumbly in response to this, nodding my head."
    show lexi happy
    "Lexi smiles and leans in closer than ever, whispering into my ear."
    lexi.say "That's good, [hero.name]."
    show lexi wink
    lexi.say "Because I'm all yours."
    lexi.say "Just here for the taking!"
    hide lexi
    show lexi kiss naked
    with fade
    $ lexi.flags.kiss += 1
    "What follows is a blur of groping hands and tangled limbs."
    "And all the while we're kissing with a hungry passion too."
    "Every time our lips are parted, we pant and gasp."
    "Our mouths searching for each other to resume the kiss."
    "Neither of us is looking where we're going, too wrapped up in the moment."
    show lexi cowgirl with hpunch
    "And so we bump into the bed, rather than finding our way to it."
    "By some minor miracle, we're actually naked as I tumble backwards."
    "Our limbs are still entangled, meaning that I take Lexi with me too."
    "She comes up atop me, straddling my waist with a wolfish grin on her face."
    lexi.say "I call on top!"
    lexi.say "I get to ride you, [hero.name]!"
    "I can't help chuckling at this, nodding eagerly."
    "After all, it's not like I'm going to argue the point."
    show lexi cowgirl mikehand pleasure
    "Instead I clap my hands on Lexi's haunches, making her yelp in surprise."
    "And I pull her downwards, making my intentions more than clear."
    mike.say "Okay, Lexi."
    mike.say "But you'd better hold on tight."
    mike.say "Because it's going to be a wild ride tonight!"
    show lexi cowgirl smile
    "Lexi laughs too, a filthy sound that only she could make."
    "And I can honestly feel my cock stiffen as I hear it too!"
    menu:
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "I can feel the urgency in Lexi's body almost as easily as its weight."
            "Every muscle is tensed for what lies ahead, every fibre coiled in anticipation."
            "And I feel the same way too, champing at the bit to get it on."
            show lexi cowgirl up pleasure
            "That's why I reach down and take hold of her buttocks again."
            "I part them and thrust upwards, aiming my cock at a certain spot..."
            lexi.say "Oh..."
            lexi.say "Oh...oh wow..."
            show lexi cowgirl smile
            lexi.say "So THAT'S what you want, huh?"
            show lexi cowgirl anal middle
            "Lexi looks down at me as I begin to push my cock into her ass."
            "She seems at least a little surprised at the route I'm taking."
            "But there's nothing in her reaction that says she disapproves either."
            mike.say "No, Lexi..."
            mike.say "This is what I'm DOING!"
            show lexi cowgirl anal down pleasure ahegao
            "With that, I push harder and further than ever."
            "In one motion, the head of my cock is inside of her."
            "And I don't stop until it's deep enough in to stay there."
            "As this happens, I see a change come over Lexi."
            "Where before she was sassy and defiant, now she begins to melt."
            "Just as the muscles of her ass give in, her expression changes too."
            "She closes her eyes, as if the sensation is almost too much for her."
            show lexi cowgirl smile
            "But she nods all the same, letting me know that she wants more."
            show lexi cowgirl down
            "As Lexi's body surrenders, her mind seems swept along for the ride."
            lexi.say "Y...yeah..."
            lexi.say "You...you're doing it..."
            lexi.say "You sure are doing it!"
            lexi.say "Just...just don't stop doing it...okay?!?"
            "I nod silently as I lie back on the bed and watch Lexi."
            show lexi cowgirl middle
            pause 0.25
            show lexi cowgirl down
            "Her eyes are closed as she rides my cock."
            "But that doesn't mean her face is blank."
            show lexi cowgirl middle
            pause 0.25
            show lexi cowgirl down
            "The sensation of being inside her is incredible right now."
            "And I can see all that I'm feeling reflected in her expression."
            show lexi cowgirl middle normal panting
            pause 0.25
            show lexi cowgirl down
            pause 0.25
            show lexi cowgirl middle
            pause 0.25
            show lexi cowgirl down
            "Lexi pants and gasps as I thrust into her from below."
            "But the sounds are somehow sensual and erotic at the same time."
            show lexi cowgirl middle
            pause 0.25
            show lexi cowgirl down
            pause 0.25
            show lexi cowgirl middle
            pause 0.25
            show lexi cowgirl down
            "Her breasts jiggle and bounce, almost touching my face."
            "More than once I swear I feel her stiff nipples brush my lips."
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            pause 0.15
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            "I'm going as fast and as hard as I can right now."
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            pause 0.15
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            "Honestly, I don't think I can give anything more."
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            pause 0.15
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            "And Lexi seems to sense that, taking matters into her own hands."
            "Before now she seemed content to ride my cock."
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            pause 0.15
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down with vpunch
            "But suddenly I feel her pressing down on me with all her weight."
            "Lexi wants more, and she's not afraid to take it!"
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            pause 0.15
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down with vpunch
            "Now I'm the one panting and gasping from her efforts."
            "And it doesn't take long for her to get results either!"
            mike.say "Ah..."
            mike.say "Shit...Lexi..."
            mike.say "I'm going to cum!"
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            pause 0.15
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            pause 0.15
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down with vpunch
            "Lexi nods at this, whimpering at the sensations she's feeling."
            "And she presses herself down with even more determination than before."
            call cum_reaction (lexi, 'anal', sexperience_min) from _call_cum_reaction_115
            if _return == "anal_inside":
                "With Lexi pressing down and me thrusting up, I'm almost pinned in place."
                "So the natural thing is to keep on going until the very end."
                show lexi cowgirl middle
                pause 0.15
                show lexi cowgirl down at startle(0.05,-10)
                pause 0.15
                show lexi cowgirl middle
                pause 0.15
                show lexi cowgirl down at startle(0.05,-10)
                "Lexi's practically grinding herself into me by now."
                show lexi cowgirl middle ahegao
                pause 0.15
                show lexi cowgirl down at startle(0.05,-10)
                pause 0.15
                show lexi cowgirl middle
                pause 0.15
                show lexi cowgirl down at startle(0.05,-10)
                pause 0.15
                show lexi cowgirl middle
                pause 0.15
                show lexi cowgirl down creampie analdrip with hpunch
                $ lexi.sub += 2
                "Which means that I lose it as deep inside of her as I can go."
                with hpunch
                "And when I do, her eyes pop open at the same moment."
                with hpunch
                "Lexi cries out as she begins to cum too, clinging onto me the whole time."
            elif _return == "anal_outside":
                show lexi cowgirl middle
                pause 0.15
                show lexi cowgirl down at startle(0.05,-10)
                pause 0.15
                show lexi cowgirl middle
                pause 0.15
                show lexi cowgirl down at startle(0.05,-10)
                "I have to pick my moment perfectly to make this work."
                "Just as Lexi lets off the pressure a little..."
                show lexi cowgirl middle ahegao
                pause 0.15
                show lexi cowgirl down at startle(0.05,-10)
                pause 0.15
                show lexi cowgirl middle
                pause 0.15
                show lexi cowgirl down at startle(0.05,-10)
                pause 0.15
                show lexi cowgirl middle
                pause 0.15
                show lexi cowgirl up pleasure -anal with vpunch
                "I somehow manage to wriggle my cock out of her ass."
                "Her eyes pop open in surprise, and her expression is quite a picture."
                "But it also pushes her into cumming too, and her eyes roll back into her head."
                show lexi cowgirl cumshot cum with vpunch
                $ lexi.sub += 1
                "I lose it too, spattering Lexi's butt with cum."
            $ lexi.flags.anal += 1
        "Fuck her pussy":
            "I can feel the urgency in Lexi's body almost as easily as its weight."
            "Every muscle is tensed for what lies ahead, every fibre coiled in anticipation."
            "And I feel the same way too, champing at the bit to get it on."
            call check_condom_usage (lexi, love=180) from _call_check_condom_usage_79
            if _return == False:
                return
            if CONDOM:
                show lexi cowgirl condom
            show lexi cowgirl up vaginal
            "I have a firm hold of Lexi's haunches, and I begin to guide her downwards."
            "But she's never been the kind of girl to let herself be lead by the hand."
            "And so she surprises me by pressing all of her weight down a moment later."
            "I gasp as I feel the head of my cock pushed hard against the lips of her pussy."
            show lexi cowgirl middle pleasure
            "But it is only for a moment, as they part without anything more than a token resistance."
            mike.say "Oh..."
            mike.say "Oh shit, Lexi..."
            show lexi cowgirl down ahegao
            lexi.say "F...fuck yeah..."
            lexi.say "That's what I want!"
            mike.say "Me too, Lexi...me too!"
            "Lexi smiles at this, looking me straight in the eye."
            "I smile back, dumbly unable to do anything else at all."
            "It just feels so good to be connected on such a deep level."
            "But not as good as it feels to be this deep inside of Lexi!"
            show lexi cowgirl middle smile
            "Together we begin to move, working together in perfect harmony."
            "Me thrusting up from below and Lexi pushing down from above."
            show lexi cowgirl down
            "I know that I'm pleasing her without needing to be told."
            "The way that Lexi closes her eyes and nods confirms it."
            show lexi cowgirl middle
            pause 0.25
            show lexi cowgirl down
            "That and the way it feels to be inside of her too."
            show lexi cowgirl middle
            pause 0.25
            show lexi cowgirl down
            "Lexi might be pushing down on me with all her weight."
            "But the sensation I can feel is as smooth as silk."
            "The muscles of her pussy squeeze me tightly."
            "And yet all I feel is pure pleasure and not a hint of pain."
            show lexi cowgirl middle
            pause 0.25
            show lexi cowgirl down
            pause 0.25
            show lexi cowgirl middle
            pause 0.25
            show lexi cowgirl down
            "This is the side of Lexi that most people don't get to see."
            "When the front of her being a tough, slutty little bitch falls away."
            "And sure, she's as horny as hell."
            show lexi cowgirl middle
            pause 0.25
            show lexi cowgirl down
            pause 0.25
            show lexi cowgirl middle
            pause 0.25
            show lexi cowgirl down
            "But she's also warm, giving and sensual too."
            "It's like a secret side of her that only I get to enjoy!"
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            pause 0.15
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            "And hearing her moan for more is almost as good too!"
            show lexi cowgirl pleasure normal
            lexi.say "Mmm..."
            lexi.say "F...fuck me harder..."
            lexi.say "Make me cum...please?!?"
            "How can I refuse a request like that?"
            show lexi cowgirl middle panting
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            pause 0.15
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            "I redouble my efforts, thrusting even harder into Lexi."
            "And she responds in an instant, nodding desperately."
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            pause 0.15
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            "Every ounce of effort I put in seems to yield a result."
            "So that before too long, Lexi is clambering for release."
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            pause 0.15
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            "But she's not the only one."
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            pause 0.15
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down at startle(0.05,-10)
            pause 0.15
            show lexi cowgirl middle
            pause 0.15
            show lexi cowgirl down with vpunch
            "All that extra effort on my part only brought me to the same point."
            "And so it looks like we're going to cum at the same time!"
            call cum_reaction (lexi, 'vaginal', sexperience_min, 190) from _call_cum_reaction_116
            if _return == "vaginal_condom":
                show lexi cowgirl middle
                pause 0.15
                show lexi cowgirl down at startle(0.05,-10)
                pause 0.15
                show lexi cowgirl middle
                pause 0.15
                show lexi cowgirl down at startle(0.05,-10)
                "With Lexi pressing down and me thrusting up, I'm almost pinned in place."
                "So the natural thing is to keep on going until the very end."
                "But we already took precautions, so that's not a problem."
                "Lexi's practically grinding herself into me by now."
                show lexi cowgirl middle ahegao
                pause 0.15
                show lexi cowgirl down at startle(0.05,-10)
                pause 0.15
                show lexi cowgirl middle
                pause 0.15
                show lexi cowgirl down at startle(0.05,-10)
                pause 0.15
                show lexi cowgirl middle
                pause 0.15
                show lexi cowgirl down pleasure with vpunch
                "Which means that I lose it as deep inside of her as I can go."
                with vpunch
                "And when I do, her eyes pop open at the same moment."
                with vpunch
                "Lexi cries out as she begins to cum too, clinging onto me the whole time."
            elif _return == "vaginal_outside":
                "I have to pick my moment perfectly to make this work."
                "Just as Lexi lets off the pressure a little..."
                show lexi cowgirl middle ahegao
                pause 0.15
                show lexi cowgirl down at startle(0.05,-10)
                pause 0.15
                show lexi cowgirl middle
                pause 0.15
                show lexi cowgirl down at startle(0.05,-10)
                pause 0.15
                show lexi cowgirl middle
                pause 0.15
                show lexi cowgirl up pleasure -vaginal with vpunch
                "I somehow manage to wriggle my cock out of her pussy."
                "Her eyes pop open in surprise, and her expression is quite a picture."
                with vpunch
                "But it also pushes her into cumming too, and her eyes roll back into her head."
                show lexi cowgirl cumshot cum with hpunch
                $ lexi.love += 1
                if CONDOM:
                    "I lose it too, filling up the rubber I put on."
                else:
                    "I lose it too, spattering Lexi's butt with cum."
            elif _return == "vaginal_inside_pill":
                lexi.say "Don't...don't pull out!"
                lexi.say "I'm on the pill..."
                show lexi cowgirl middle
                pause 0.15
                show lexi cowgirl down at startle(0.05,-10)
                pause 0.15
                show lexi cowgirl middle
                pause 0.15
                show lexi cowgirl down at startle(0.05,-10)
                "I silently thank Lexi for the timely reminder."
                "Because it lets me keep on going until the very end."
                "Lexi's practically grinding herself into me by now."
                show lexi cowgirl middle ahegao
                pause 0.15
                show lexi cowgirl down at startle(0.05,-10)
                pause 0.15
                show lexi cowgirl middle
                pause 0.15
                show lexi cowgirl down at startle(0.05,-10)
                pause 0.15
                show lexi cowgirl middle
                pause 0.15
                show lexi cowgirl down creampie vaginaldrip with vpunch
                $ lexi.love += 2
                "Which means that I lose it as deep inside of her as I can go."
                with vpunch
                "And when I do, her eyes pop open at the same moment."
                with vpunch
                "Lexi cries out as she begins to cum too, clinging onto me the whole time."
            elif _return == "vaginal_inside_pregnant":
                lexi.say "Don't...don't pull out!"
                lexi.say "You can't get me...pregnant again!"
                show lexi cowgirl middle
                pause 0.15
                show lexi cowgirl down at startle(0.05,-10)
                pause 0.15
                show lexi cowgirl middle
                pause 0.15
                show lexi cowgirl down at startle(0.05,-10)
                "I silently thank Lexi for the timely reminder."
                "Because it lets me keep on going until the very end."
                "Lexi's practically grinding herself into me by now."
                show lexi cowgirl down ahegao creampie vaginaldrip with hpunch
                $ lexi.love += 3
                "Which means that I lose it as deep inside of her as I can go."
                with vpunch
                "And when I do, her eyes pop open at the same moment."
                with vpunch
                "Lexi cries out as she begins to cum too, clinging onto me the whole time."
            elif _return == "vaginal_inside_mad":
                show lexi cowgirl middle
                pause 0.15
                show lexi cowgirl down at startle(0.05,-10)
                pause 0.15
                show lexi cowgirl middle
                pause 0.15
                show lexi cowgirl down at startle(0.05,-10)
                lexi.say "Pull out!"
                lexi.say "You have to pull out!"
                "In the same moment that I hear Lexi say this, I realise that we didn't stop to use a condom!"
                show lexi cowgirl middle
                pause 0.15
                show lexi cowgirl down at startle(0.05,-10)
                pause 0.15
                show lexi cowgirl middle
                pause 0.15
                show lexi cowgirl down at startle(0.05,-10)
                "I try in vain to pull my cock out of Lexi, but it's already too late."
                "Lexi's trying to clamber off of me too."
                show lexi cowgirl middle ahegao
                pause 0.15
                show lexi cowgirl down at startle(0.05,-10)
                pause 0.15
                show lexi cowgirl middle
                pause 0.15
                show lexi cowgirl down at startle(0.05,-10)
                pause 0.15
                show lexi cowgirl middle
                pause 0.15
                show lexi cowgirl down creampie with vpunch
                $ lexi.love -= 5
                $ lexi.impregnate()
                "But it's already too late, and I lose it as deep inside of her as I can go."
                with vpunch
                "And when I do, her eyes pop open at the same moment."
                with vpunch
                "Lexi cries out as she begins to cum too, clinging onto me the whole time."
                show lexi cowgirl up dickcum vaginaldrip -creampie
                "And only afterwards do we stare each other in the eye."
                "Both shocked and horrified by what just happened."
            elif _return == "vaginal_inside_happy":
                lexi.say "Don't...don't pull out!"
                lexi.say "I won't let you!"
                show lexi cowgirl middle
                pause 0.15
                show lexi cowgirl down at startle(0.05,-10)
                pause 0.15
                show lexi cowgirl middle
                pause 0.15
                show lexi cowgirl down at startle(0.05,-10)
                "In the same moment that I hear Lexi say this, I also feel her press down on me too!"
                "And the realisation rushes in that we didn't stop to use a condom!"
                show lexi cowgirl middle
                pause 0.15
                show lexi cowgirl down at startle(0.05,-10)
                pause 0.15
                show lexi cowgirl middle
                pause 0.15
                show lexi cowgirl down at startle(0.05,-10)
                "I try in vain to pull my cock out of Lexi, but she's too strong."
                "Lexi's practically grinding herself into me by now."
                show lexi cowgirl middle ahegao
                pause 0.15
                show lexi cowgirl down at startle(0.05,-10)
                pause 0.15
                show lexi cowgirl middle
                pause 0.15
                show lexi cowgirl down at startle(0.05,-10)
                pause 0.15
                show lexi cowgirl middle
                pause 0.15
                show lexi cowgirl down creampie with vpunch
                $ lexi.love += 5
                $ lexi.impregnate()
                "Which means that I lose it as deep inside of her as I can go."
                with vpunch
                "And when I do, her eyes pop open at the same moment."
                with vpunch
                "Lexi cries out as she begins to cum too, clinging onto me the whole time."
    "Afterwards, neither of us feels the need to say as much as a single word."
    show lexi cowgirl up normal pleasure dickcum -vaginal -anal -creampie -cumshot
    "Lexi just slides off of me and onto the bed at my side."
    "She nestles herself into me and I wrap an arm around her."
    "Just listening to the sound of her breathing and feeling the beating of her heart."
    return

label lexi_fuck_date_standing(sexperience_min):
    if game.week_day % 2 == 0:
        "I'm ready and raring to go, with nothing else on my mind save for Lexi's pussy."
        "So I waste no time in lining myself up to take the plunge."
        call check_condom_usage (lexi, love=180) from _call_check_condom_usage_80
        if _return == False:
            return
        "I snicker."
        mike.say "Oh, no, we're definitely not done yet."
        mike.say "You're my whore all night long tonight!"
        "She giggles at that , slapping me on the thigh."
        if lexi.is_visibly_pregnant:
            lexi.say "Great! Now, how you gonna treat me, the momma of yer child?"
        if lexi.flags.drugs:
            lexi.say "I'm yer crack whore!"
            lexi.say "Now, let me pay you off!"
        if lexi.flags.facecum:
            show lexi naked cum
        else:
            show lexi naked
        "I stand up , grabbing her by the arm, yanking her up so she stands with me."
        "I then spin her around, placing my hands upon her hips and whispering to her."
        mike.say "I'm going to use you however I want, for as long as I can handle."
        if not (lexi.flags.drugs or lexi.is_visibly_pregnant):
            lexi.say "Oh, [hero.name], come on and show me how a real man fucks a woman!"
        elif lexi.flags.drugs:
            lexi.say "Ah, come on! Stop teasing me! I'm so fucking hot, I can't stand it!"
        elif lexi.is_visibly_pregnant:
            "She winces a moment, but smirks."
            lexi.say "Ah, not even gentle to yer kid?"
            lexi.say "Love that reckless shit. Come on and play with your favorite baby oven!"
        if lexi.flags.facecum:
            show lexi stand grope cum
        else:
            show lexi stand grope
        "Her thighs take my dick like they were hungry for it."
        "She shudders as my cock kisses her sex."
        if lexi.is_visibly_pregnant:
            lexi.say "Not worried about getting the baby all messy?"
            mike.say "Oh, don't you worry about that."
            "I Pull back just a bit to get the right angle."
            mike.say "It's perfectly safe for me to fuck you up until your water breaks, and I intend to take advantage of that the whole nine months!"
        elif lexi.flags.drugs:
            lexi.say "Yeah, yeah! Come on, fucker! Fuck me right now!"
        else:
            lexi.say "Oooh, You're... you're gonna put it in now?"
        "I thrust inside, letting her dripping wet pussy suck me in."
        "She moans, squirming as I spread her and pump into her."
        if lexi.is_visibly_pregnant:
            lexi.say "[hero.name], yer so rough! Fuck me harder til my water bursts all over yer dick!"
        elif lexi.flags.drugs:
            lexi.say "Ah, fuck, [hero.name], what is this weak shit!"
            lexi.say "I need a better high than this! Harder, harder!"
        "I do it, but only because I want it."
        "Soon, she's bouncing on my cock, her breasts jiggling in large, sloshy movements, her messy face contorted into a mask of delight."
        "Her body is quite warm already, sweat glistening her body in such a wonderful sheen."









        menu:
            "Choke her":
                "She may be in my bedroom now, but Lexi's a bitch, through and through."
                "I think about all the shit she put me through, and decide now that we're together, I can get a little payback."

                if lexi.flags.drugs:
                    lexi.say "Dammit [hero.name]!"
                    lexi.say "Are you just gonna' sit there are are ya gonna do some-acck!"
                else:
                    lexi.say "Well, [hero.name]."
                    lexi.say "What are you going to gaah!?"
                if lexi.flags.facecum:
                    show lexi stand choke cum
                else:
                    show lexi stand choke
                "My hands move up along her body, fingers wrapping around her throat."
                if lexi.flags.drugs:
                    "She croaks and squirms, her eyes rolling back as she grips onto me, digging into my flesh."
                    "What rush must she be feeling now, knowing that I give her the thrill of air loss."
                else:
                    "She shudders, quick breaths passing through her windpipe as I hold her down tight."
                if lexi.is_visibly_pregnant:
                    "Even as I get the sick joy of this dangerous thrill, I can't think about all the things she's done to me."
                    "Instead, I see her rounded belly and all I can think of is the life inside her, the one that hasn't made her mistakes and doesn't deserve to be hurt."
                elif lexi.flags.drugs:
                    "She struggles underneath my grasp, but with little laughs escaping the gasps and gurgles that she has."
                    "At first, I wonder if I'm just imagining it, but when she grabs my cock and furiously jerks it, I know I have to keep going, but is this all I had left in me?"
                else:
                    "She squirms underneath my touch, her thighs rubbing along my cock, giving me a nice jerking off, even though she can't bend down to stroke it."
                    "The little gasps and gargles from her fill me with so much more desire."
                "I let go and give her a quick kiss on the cheek."
                mike.say "That's enough of that for now."
                "She gasps, falling forward a bit, but I catch her."
                if lexi.is_visibly_pregnant:
                    "She sighs and nods."
                    lexi.say "Shame... though after I pop this bundle out of me, you'd better choke me good, won't you?"
                elif lexi.flags.drugs:
                    lexi.say "Either my heart's gonna explode or you're gonna choke me out!"
                else:
                    "She coughs, sputtering up some drool before she wipes it off, wheezing."
                    lexi.say "D... damn, [hero.name] what more can you do to me!?"
                mike.say "Is it too much?"
                lexi.say "Fuck that."
                lexi.say "What more are you gonna do to me!? Live fast, die young! What's next!?"
                "Looks like you'll find out..."
            "Pull her hair":
                if lexi.flags.facecum:
                    show lexi stand pull cum
                else:
                    show lexi stand pull
                "I move my hands up along her body and get good handfuls of those golden locks."
                "She tilts back as I yank on her, her chest poking out."
                "I know she likes to be handled roughly."
                if lexi.flags.drugs:
                    "Pain is just another form of pleasure just like drugs, isn't it?"
                "She moves her hands back down to my waist, holding onto me as I yank at her, and I say."
                mike.say "You're mine, got that?"
                "She nods, wincing when her hair tugs at her scalp."
                if lexi.flags.drugs:
                    "Her mouth opens as if she wants to say something, but she can only make her excited screams of pure hyped up delight!"
                else:
                    lexi.say "Do whatever you want to me... I'm your plaything!"
        call cum_reaction (lexi, 'vaginal', sexperience_min) from _call_cum_reaction_117
        if _return == "vaginal_condom":
            if lexi.flags.facecum:
                show lexi stand grope ahegao cum
            else:
                show lexi stand grope ahegao
            "Both of us groan as we feel the pleasure welling up within us."
            "Soon, I release, sending my seed deep inside of her body."
            if lexi.flags.drugs:
                "Lexi's eyes roll back and she collapses her whole weight upon me, groaning as she crashes from the end of her high and the climax I gave her."
            else:
                "Lexi coos as she falls back on me."
            hide lexi stand
        elif _return == "vaginal_outside":
            if lexi.flags.facecum:
                show lexi stand grope ahegao cum
            else:
                show lexi stand grope ahegao
            with hpunch
            "With one final groan, I shoot my load, unable to hold back any longer."
            "Lexi lays back against me, spreading her thighs and admiring the cumstains that soak her."
            hide lexi stand
            scene bg bedroom1
            show lexi naked
            if lexi.flags.drugs:
                lexi.say "Haa... imagine if ya took some yerself. Fuck, you'd be spurtin' even farther, I'd bet. Whooo!"
            else:
                lexi.say "D... damn, [hero.name]."
                lexi.say "You lasted for awhile."
                lexi.say "I'm impressed!"
        else:
            if lexi.flags.facecum:
                show lexi stand grope ahegao cum
            else:
                show lexi stand grope ahegao
            with hpunch
            "Both of us groan as we feel the pleasure welling up within us."
            "Soon, I release, sending my seed deep inside of her body."
            if lexi.flags.drugs:
                "Lexi's eyes roll back and she collapses her whole weight upon me, groaning as she crashes from the end of her high and the climax I gave her."
            elif not lexi.is_visibly_pregnant:
                "Lexi coos as she falls back on me, content that I have bred her."
            else:
                "Lexi coos as she falls back on me."
            hide lexi stand
            $ lexi.impregnate()
    else:
        menu:
            "Fuck her from front":
                "Lexi leaps off the ground and wraps her arms around my neck."
                "At the same time, I feel her legs wrapping around my waist too."
                "Before I can do a thing, Lexi clamps her lips against mine."
                "And her tongue forces it's way into my mouth."
                show lexi kiss naked with fade
                $ lexi.flags.kiss += 1
                mike.say "Mmmph..."
                mike.say "Mmm..."
                "I do the best I can to support Lexi's weight."
                "But I'm also fighting to keep on my feet at the same time."
                "I find myself staggering backwards, trying to look over my shoulder."
                "And that's when I spot a flat surface nearby."
                if persistent.xray:
                    if lexi.flags.facecum:
                        show lexi stand2 xray cum
                    else:
                        show lexi stand2 xray
                else:
                    if lexi.flags.facecum:
                        show lexi stand2 cum
                    else:
                        show lexi stand2
                "Turning at the last moment, I deposit Lexi atop it."
                "The thing groans under the strain of her weight."
                "But Lexi doesn't seem to notice."
                "Instead she makes a grab for my cock."
                "Then she's rubbing it like that'll make a genie appear and grant her every wish!"
                menu:
                    "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
                        "I can practically smell Lexi's pussy right now."
                        "And there's nothing that'd me and getting it!"
                        "Lexi aims the head of my cock squarely at her pussy."
                        "And then she tries to wriggle onto it."
                        "I hardly have to do any of the work myself."
                        "So instead I lift her legs and spread them."
                        "Which makes the whole thing that much easier."
                        "All I have to do is lift her a little more."
                        "That and tip her back just so..."
                        lexi.say "Wha..."
                        lexi.say "Argh!"
                        lexi.say "Dammit!"
                        lexi.say "That's my ass!"
                        "I can't help chuckling as I have Lexi right where I want her."
                        "And I'm using her own weight to sink into her ass."
                        mike.say "I know, I know!"
                        mike.say "Just sit back and relax, Lexi."
                        mike.say "Doesn't it feel good?"
                        "I can see Lexi's eyes glazing over more with each second that passes."
                        "The deeper my cock goes into her ass, the more she seems to like it!"
                        if persistent.xray:
                            show lexi stand2 anal xray with fade
                        else:
                            show lexi stand2 anal with fade
                        lexi.say "Y...yeah..."
                        mike.say "That's right..."
                        lexi.say "Oh fuck yeah!"
                        "Suddenly my cock almost bursts into Lexi."
                        "All it takes is a little pressure in just the right spot."
                        "Then I slide straight into her, as deep as I can go."
                        "Neither of us wastes another second."
                        "We just go at it like our lives depend on it!"
                        "Lexi moans and nods desperately as I pound away at her."
                        "And from the way she's clinging to me, I know she wants more still."
                        "There's no building up to it either, just a wild charge to satisfy our desires."
                        "The table creaks and moans as we go at it."
                        "And Lexi moans even louder!"
                        "There's a danger that it might break under her weight."
                        "But neither of us has anything but sex on our minds right now."
                        "Lexi's breasts are pressed right up against my chest."
                        "And her nipples rub against me as I'm pounding her."
                        "She has her head on my shoulder, whimpering into my ear."
                        if persistent.xray:
                            show lexi stand2 ahegao xray
                        else:
                            show lexi stand2 ahegao
                        lexi.say "H...harder..."
                        lexi.say "Please...harder..."
                        "I nod, doing all I can to fulfil Lexi's demands."
                        "And with every thrust that I make into her, I feel myself edging closer."
                        "Each one gets me just a fraction closer to losing it."
                        "I don't want to, not yet."
                        "What I really want is to keep on doing this to Lexi for hours!"
                        "But it doesn't look like I'm going to have the choice..."
                        call cum_reaction (lexi, 'anal', sexperience_min) from _call_cum_reaction_118
                        if _return == "anal_inside":
                            "I silently thank the gods of getting laid that I decided to do Lexi up the ass."
                            "Because it means that I can keep right on going until I actually cum."
                            with hpunch
                            "And when I do, I make sure that it's while I'm buried deep inside Lexi."
                            with hpunch
                            "She squeals at the sensation, clinging to me even tighter than before."
                            with hpunch
                            "I can feel her starting to cum too, squeezing my cock inside of her."
                            $ lexi.sub += 2
                            "And I keep a tight hold on her as well."
                            "Just in case the table doesn't hold up to all of this punishment!"
                        elif _return == "anal_outside":
                            "I decide to pull out of Lexi before it's too late."
                            "But that's easier said than done, as she's still clinging to me!"
                            show chest_insert lexi zorder 1 at zoomAt(1, (40, 120))
                            show belly_insert lexi zorder 2 at zoomAt(1, (40, 380))
                            with hpunch
                            "I wriggle and tug, and by some minor miracle I manage to do it in time."
                            with hpunch
                            "She squeals at the sensation, clinging to me even tighter than before."
                            with hpunch
                            "I can feel her starting to cum too, squeezing me with her thighs."
                            $ lexi.sub += 1
                            show chest_insert lexi cum
                            show belly_insert lexi cum
                            with hpunch
                            "And I keep a tight hold on her as well as I shoot my load over her belly."
                            "Just in case the table doesn't hold up to all of this punishment!"
                            hide chest_insert
                            hide belly_insert
                        $ lexi.flags.anal += 1
                    "Fuck her pussy":
                        "I can practically smell Lexi's pussy right now."
                        "And there's nothing going to come between me and getting it!"
                        call check_condom_usage (lexi, love=180) from _call_check_condom_usage_81
                        if _return == False:
                            return
                        "Lexi aims the head of my cock squarely at her pussy."
                        if persistent.xray:
                            show lexi stand2 vaginal xray with fade
                        else:
                            show lexi stand2 vaginal with fade
                        "And then she practically wriggles onto it."
                        "I hardly have to do any of the work myself."
                        "So instead I lift her legs and spread them."
                        "Which makes the whole thing that much easier."
                        "The only problem is that Lexi's already pretty slick down there."
                        "Normally that would work in our favour."
                        "But right now she's so desperate that it makes her fumble around."
                        lexi.say "Wha..."
                        lexi.say "Argh!"
                        lexi.say "Dammit!"
                        mike.say "Here..."
                        mike.say "Let me..."
                        "Suddenly we're both trying to direct traffic down there."
                        "At first we get in each other's way."
                        "But then it seems to work out all at once."
                        lexi.say "Y...yeah..."
                        mike.say "That's right..."
                        lexi.say "Oh fuck yeah!"
                        "Suddenly my cock almost bursts into Lexi."
                        "All it takes is a little pressure in just the right spot."
                        "Then I slide straight into her, as deep as I can go."
                        "Neither of us wastes another second."
                        "We just go at it like our lives depend on it!"
                        "Lexi moans and nods desperately as I pound away at her."
                        "And from the way she's clinging to me, I know she wants more still."
                        "There's no building up to it either, just a wild charge to satisfy our desires."
                        "The table creaks and moans as we go at it."
                        "And Lexi moans even louder!"
                        "There's a danger that it might break under her weight."
                        "But neither of us has anything but sex on our minds right now."
                        "Lexi's breasts are pressed right up against my chest."
                        "And her nipples rub against me as I'm pounding her."
                        "She has her head on my shoulder, whimpering into my ear."
                        if persistent.xray:
                            show lexi stand2 ahegao xray
                        else:
                            show lexi stand2 ahegao
                        lexi.say "H...harder..."
                        lexi.say "Please...harder..."
                        "I nod, doing all I can to fulfil Lexi's demands."
                        "And with every thrust that I make into her, I feel myself edging closer."
                        "Each one gets me just a fraction closer to losing it."
                        "I don't want to, not yet."
                        "What I really want is to keep on doing this to Lexi for hours!"
                        "But it doesn't look like I'm going to have the choice..."
                        call cum_reaction (lexi, 'vaginal', sexperience_min) from _call_cum_reaction_119
                        if _return == "vaginal_condom":
                            "I silently thank the gods of getting laid that we used a condom."
                            "Because it means that I can keep right on going until I actually cum."
                            with hpunch
                            "And when I do, I make sure that it's while I'm buried deep inside Lexi."
                            with hpunch
                            "She squeals at the sensation, clinging to me even tighter than before."
                            with hpunch
                            "I can feel her starting to cum too, squeezing my cock inside of her."
                            "And I keep a tight hold on her as well."
                            $ lexi.love += 1
                            "Just in case the table doesn't hold up to all of this punishment!"
                        elif _return == "vaginal_outside":
                            "I need to pull out of Lexi before it's too late."
                            "But that's easier said than done, as she's still clinging to me!"
                            show chest_insert lexi zorder 1 at zoomAt(1, (40, 120))
                            show belly_insert lexi zorder 2 at zoomAt(1, (40, 380))
                            with hpunch
                            "I wriggle and tug, and by some minor miracle I manage to do it in time."
                            with hpunch
                            "She squeals at the sensation, clinging to me even tighter than before."
                            with hpunch
                            "I can feel her starting to cum too, squeezing me with her thighs."
                            $ lexi.love += 1
                            show chest_insert lexi cum
                            show belly_insert lexi cum
                            with hpunch
                            "And I keep a tight hold on her as well as I shoot my load over her belly."
                            "Just in case the table doesn't hold up to all of this punishment!"
                            hide chest_insert
                            hide belly_insert
                        elif _return == "vaginal_inside_pill":
                            lexi.say "Urgh..."
                            lexi.say "Cum...in...me..."
                            lexi.say "I'm on the fucking pill!"
                            "I silently thank the gods for the invention of the pill."
                            "Because it means that I can keep right on going until I actually cum."
                            with hpunch
                            "And when I do, I make sure that it's while I'm buried deep inside Lexi."
                            with hpunch
                            "She squeals at the sensation, clinging to me even tighter than before."
                            with hpunch
                            "I can feel her starting to cum too, squeezing my cock inside of her."
                            $ lexi.love += 2
                            "And I keep a tight hold on her as well."
                            "Just in case the table doesn't hold up to all of this punishment!"
                        elif _return == "vaginal_inside_pregnant":
                            lexi.say "Urgh..."
                            lexi.say "Cum...in...me..."
                            lexi.say "I'm fucking pregnant already!"
                            "I smirk at the thought of needing to be reminded of that fact."
                            "But it does mean that I can keep right on going until I actually cum."
                            with hpunch
                            "And when I do, I make sure that it's while I'm buried deep inside Lexi."
                            with hpunch
                            "She squeals at the sensation, clinging to me even tighter than before."
                            with hpunch
                            "I can feel her starting to cum too, squeezing my cock inside of her."
                            $ lexi.love += 3
                            "And I keep a tight hold on her as well."
                            "Just in case the table doesn't hold up to all of this punishment!"
                        elif _return == "vaginal_inside_mad":
                            lexi.say "Urgh..."
                            lexi.say "Don't...cum...in...me..."
                            lexi.say "Pull out...NOW!"
                            "Lexi's final demand catches me totally off-guard."
                            "I was just about to pull out, but now I freeze in confusion."
                            with hpunch
                            "And that's all it takes for me to cum inside her."
                            with hpunch
                            "She squeals at the sensation, clinging to me even tighter than before."
                            with hpunch
                            "I can feel her starting to cum too, squeezing my cock inside of her."
                            $ lexi.love -= 5
                            $ lexi.impregnate()
                            "And I keep a tight hold on her as well."
                            "Just in case the table doesn't hold up to all of this punishment!"
                            "But I'm already fretting about what we just did..."
                        elif _return == "vaginal_inside_happy":
                            lexi.say "Urgh..."
                            lexi.say "Cum...in...me..."
                            lexi.say "I want it!"
                            "Lexi's final demand catches me totally off-guard."
                            "I was just about to pull out, but now I freeze in confusion."
                            with hpunch
                            "And that's all it takes for me to cum inside her."
                            $ lexi.love += 5
                            $ lexi.impregnate()
                            with hpunch
                            "She squeals at the sensation, clinging to me even tighter than before."
                            with hpunch
                            "I can feel her starting to cum too, squeezing my cock inside of her."
                            "And I keep a tight hold on her as well."
                            "Just in case the table doesn't hold up to all of this punishment!"
                            "But I'm already fretting about what she just made me do..."
            "Fuck her from behind":

                "But I'm more then ready for her as she leaps at me."
                "And I just take a little step to one side."
                "Just enough so that Lexi misses me and is caught off-guard."
                "Then I step up neatly behind her, wrapping my arms around her waist."
                lexi.say "Hey!"
                lexi.say "What the..."
                "Her protests come to an end a moment later."
                "Which is when she feels my cock pressing against her ass."
                if lexi.flags.facecum:
                    show lexi stand grope cum
                else:
                    show lexi stand grope
                lexi.say "Oh..."
                lexi.say "Hello!"
                lexi.say "Is somebody knocking on my back door?"
                "All I can do is chuckle and pull Lexi closer to me."
                "Because the sensation of being this close to her is almost too much."
                "And I don't have the mental capacity to speak because of it."
                "All I know is that I have to get inside of Lexi."
                "And I need to do it now!"
                menu:
                    "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
                        "Not wasting another moment, I push my cock forwards."
                        "It goes between Lexi's thighs, already brushing against her pussy."
                        "But then I gasp as I feel her bend over and reach down there too."
                        "Because she's pinching the head of my cock with her thumb and forefinger!"
                        mike.say "Ah..."
                        mike.say "Shit, Lexi!"
                        "All the exclamation gets me in return is a filthy laugh from Lexi."
                        "But I take that as permission to get on with it."
                        "I have a firm hold on Lexi's waist, and I make good use of it."
                        "Pulling her backwards, I push myself forwards at the same time."
                        "Lexi giggles and then moans as my cock sides along her lips."
                        "But then I change the angle I'm aiming it at."
                        "And I hear her let out a squeal of surprise."
                        lexi.say "Ooh..."
                        lexi.say "What are you..."
                        lexi.say "That's not my pussy!"
                        lexi.say "That's my ass!"
                        "I allow myself a sly smile as my plan takes shape."
                        "And the fact I took Lexi by surprise means there's nothing she can do to stop me."
                        show lexi stand anal with fade
                        "I keep right on pushing my cock into her ass."
                        "And little by little the resistance begins to melt away."
                        "Which means that I can start to inch my way inside."
                        "The process is pretty slow and gradual as Lexi surrenders to me."
                        "And it feels like forever until I'm as far in as I can go."
                        "Time seems to slow down as all of this is happening."
                        "But once I'm all the way in, it feels like it snaps straight back again."
                        "Instantly I'm aware of everything all at once."
                        "The feeling of Lexi's ass around my cock."
                        "Her body pressed up against mine."
                        "And the pleading look in her eyes too!"
                        "I snap to attention the second we make eye-contact."
                        "It's like I have no choice in the matter."
                        "I just know that I've got to do all I can to please Lexi."
                        "And right now!"
                        "Not wasting any time, I start to thrust in and out."
                        "Lexi nods desperately as I do so, begging for more."
                        "And she doesn't have to wait long to get it either."
                        "I feel myself getting into the rhythm and really going for it."
                        "My hold on Lexi's strong and she's pushing herself back into me too."
                        "I'm panting and there's sweat starting to bead on my forehead."
                        show lexi stand ahegao
                        "But there's no way that I'm going to slow down now."
                        lexi.say "Uh..."
                        lexi.say "Oh yeah..."
                        lexi.say "Fuck me harder, [hero.name]!"
                        lexi.say "Harder!"
                        "By now I'm giving it all that I can."
                        "I don't think I could go faster if I tried."
                        "My thighs are slapping against Lexi's buttocks."
                        "And her breasts are giggling like crazy too!"
                        "She seems to be losing the ability to speak."
                        "Before she was actually getting out whole words."
                        "Now she's reduced to making animalistic noises instead."
                        "And even these become more like simple sounds as she near the end."
                        "Maybe that's what pushes me over the edge too."
                        "Or maybe it's just a coincidence."
                        "Either way, I'm about to lose it!"
                        call cum_reaction (lexi, 'anal', sexperience_min) from _call_cum_reaction_120
                        if _return == "anal_inside":
                            "There are definitely benefits to doing Lexi up the ass."
                            "One of which is it means that I can keep right on going until I actually cum."
                            with hpunch
                            "And when I do, I make sure that it's while I'm buried deep inside Lexi."
                            with hpunch
                            "She squeals at the sensation, pushing against me more then ever."
                            $ lexi.sub += 2
                            with hpunch
                            "I can feel her starting to cum too, squeezing my cock inside of her."
                            "And I keep a tight hold on her as well."
                            "Just in case her legs decide to give out before the end."
                        elif _return == "anal_outside":
                            "I need to pull out of Lexi before it's too late."
                            "But that's easier said than done, as she's still clinging to me!"
                            with hpunch
                            "I wriggle and tug, and by some minor miracle I manage to do it in time."
                            with hpunch
                            "She squeals at the sensation, pushing against me more then ever."
                            with hpunch
                            "I can feel her starting to cum too, squeezing me with her thighs."
                            "And I keep a tight hold on her as well as I shoot my load over her back."
                            $ lexi.sub += 1
                            "Just in case her legs decide to give out before the end."
                        $ lexi.flags.anal += 1
                    "Fuck her pussy":
                        "Not wasting another moment, I push my cock forwards."
                        "It goes between Lexi's thighs, already brushing against her pussy."
                        "But then I gasp as I feel her bend over and reach down there too."
                        "Because she's pinching the head of my cock with her thumb and forefinger!"
                        mike.say "Ah..."
                        mike.say "Shit, Lexi!"
                        "All the exclamation gets me in return is a filthy laugh from Lexi."
                        "But I take that as permission to get on with it."
                        show lexi stand
                        call check_condom_usage (lexi, love=180) from _call_check_condom_usage_82
                        if _return == False:
                            return
                        if CONDOM:
                            show lexi stand condom vaginal
                        with fade
                        "I have a firm hold on Lexi's waist, and I make good use of it."
                        "Pulling her backwards, I push myself forwards at the same time."
                        "Lexi giggles and then moans as my cock sides along her lips."
                        "She still has her hands down there."
                        "And I can feel her using them to good effect too."
                        "Lexi's pushing the head of my cock as it moves."
                        "And as she massages it against her pussy, the inevitable begins to happen."
                        "Little by little the resistance begins to melt away."
                        "Which means that I can start to inch my way inside."
                        "The process is pretty slow and gradual as Lexi surrenders to me."
                        "And it feels like forever until I'm as far in as I can go."
                        "Time seems to slow down as all of this is happening."
                        "But once I'm all the way in, it feels like it snaps straight back again."
                        "Instantly I'm aware of everything all at once."
                        "The feeling of Lexi's pussy around my cock."
                        "Her body pressed up against mine."
                        "And the pleading look in her eyes too!"
                        "I snap to attention the second we make eye-contact."
                        "It's like I have no choice in the matter."
                        "I just know that I've got to do all I can to please Lexi."
                        "And right now!"
                        "Not wasting any time, I start to thrust in and out."
                        "Lexi nods desperately as I do so, begging for more."
                        "And she doesn't have to wait long to get it either."
                        "I feel myself getting into the rhythm and really going for it."
                        "My hold on Lexi's strong and she's pushing herself back into me too."
                        "I'm panting and there's sweat starting to bead on my forehead."
                        "But there's no way that I'm going to slow down now."
                        show lexi stand ahegao
                        lexi.say "Uh..."
                        lexi.say "Oh yeah..."
                        lexi.say "Fuck me harder, [hero.name]!"
                        lexi.say "Harder!"
                        "By now I'm giving it all that I can."
                        "I don't think I could go faster if I tried."
                        "My thighs are slapping against Lexi's buttocks."
                        "And her breasts are giggling like crazy too!"
                        "She seems to be losing the ability to speak."
                        "Before she was actually getting out whole words."
                        "Now she's reduced to making animalistic noises instead."
                        "And even these become more like simple sounds as she near the end."
                        "Maybe that's what pushes me over the edge too."
                        "Or maybe it's just a coincidence."
                        "Either way, I'm about to lose it!"
                        call cum_reaction (lexi, 'vaginal', sexperience_min) from _call_cum_reaction_121
                        if _return == "vaginal_condom":
                            "I silently thank the gods of getting laid that we used a condom."
                            "Because it means that I can keep right on going until I actually cum."
                            with hpunch
                            "And when I do, I make sure that it's while I'm buried deep inside Lexi."
                            with hpunch
                            "She squeals at the sensation, pushing against me more then ever."
                            with hpunch
                            "I can feel her starting to cum too, squeezing my cock inside of her."
                            "And I keep a tight hold on her as well."
                            $ lexi.love += 1
                            "Just in case her legs decide to give out before the end."
                        elif _return == "vaginal_outside":
                            "I need to pull out of Lexi before it's too late."
                            "But that's easier said than done, as she's still clinging to me!"
                            with hpunch
                            "I wriggle and tug, and by some minor miracle I manage to do it in time."
                            with hpunch
                            "She squeals at the sensation, pushing against me more then ever."
                            with hpunch
                            "I can feel her starting to cum too, squeezing me with her thighs."
                            "And I keep a tight hold on her as well as I shoot my load over her back."
                            $ lexi.love += 1
                            "Just in case her legs decide to give out before the end."
                        elif _return == "vaginal_inside_pill":
                            lexi.say "Urgh..."
                            lexi.say "Cum...in...me..."
                            lexi.say "I'm on the fucking pill!"
                            "I silently thank the gods for the invention of the pill."
                            "Because it means that I can keep right on going until I actually cum."
                            with hpunch
                            "And when I do, I make sure that it's while I'm buried deep inside Lexi."
                            with hpunch
                            "She squeals at the sensation, pushing against me more then ever."
                            with hpunch
                            "I can feel her starting to cum too, squeezing my cock inside of her."
                            $ lexi.love += 2
                            "And I keep a tight hold on her as well."
                            "Just in case her legs decide to give out before the end."
                        elif _return == "vaginal_inside_pregnant":
                            lexi.say "Urgh..."
                            lexi.say "Cum...in...me..."
                            lexi.say "I'm fucking pregnant already!"
                            "I smirk at the thought of needing to be reminded of that fact."
                            "But it does mean that I can keep right on going until I actually cum."
                            with hpunch
                            "And when I do, I make sure that it's while I'm buried deep inside Lexi."
                            with hpunch
                            "She squeals at the sensation, pushing against me more then ever."
                            with hpunch
                            "I can feel her starting to cum too, squeezing my cock inside of her."
                            $ lexi.love += 3
                            "And I keep a tight hold on her as well."
                            "Just in case her legs decide to give out before the end."
                        elif _return == "vaginal_inside_mad":
                            lexi.say "Urgh..."
                            lexi.say "Don't...cum...in...me..."
                            lexi.say "Pull out...NOW!"
                            "Lexi's final demand catches me totally off-guard."
                            "I was just about to pull out, but now I freeze in confusion."
                            with hpunch
                            "And that's all it takes for me to cum inside her."
                            with hpunch
                            "She squeals at the sensation, pushing against me more then ever."
                            with hpunch
                            "I can feel her starting to cum too, squeezing my cock inside of her."
                            "And I keep a tight hold on her as well."
                            $ lexi.love -= 5
                            $ lexi.impregnate()
                            "Just in case her legs decide to give out before the end."
                            "But I'm already fretting about what we just did..."
                        elif _return == "vaginal_inside_happy":
                            lexi.say "Urgh..."
                            lexi.say "Cum...in...me..."
                            lexi.say "I want it!"
                            "Lexi's final demand catches me totally off-guard."
                            "I was just about to pull out, but now I freeze in confusion."
                            with hpunch
                            "And that's all it takes for me to cum inside her."
                            with hpunch
                            "She squeals at the sensation, pushing against me more then ever."
                            with hpunch
                            "I can feel her starting to cum too, squeezing my cock inside of her."
                            $ lexi.love += 5
                            $ lexi.impregnate()
                            "And I keep a tight hold on her as well."
                            "Just in case her legs decide to give out before the end."
                            "But I'm already fretting about what she just made me do..."
    return

label lexi_fuck_date_doggy(sexperience_min):
    show lexi a surprised blush
    lexi.say "Hey!"
    lexi.say "Why are you looking at me like that?"
    mike.say "Erm..."
    mike.say "Like what, Lexi?"
    show lexi wink
    lexi.say "Like I'm a dog."
    lexi.say "And you know what trick I'm going to do next!"
    "I can feel my cheeks flushing as Lexi calls me out."
    show lexi normal
    "And I struggle to think of a way to get myself out of this mess."
    "Then it strikes me - when all else fails, resort to flattery!"
    mike.say "I...I just can't keep my eyes off you, Lexi!"
    mike.say "You look so hot, it's driving me crazy!"
    "I know that Lexi's no fool, that she's been around the block more than once."
    "But I also know that she thinks I'm from a totally different world to the one she knows."
    "And while she's right, it also means that she's a little less cynical when judging me too."
    lexi.say "Really, [hero.name]?"
    show lexi happy
    lexi.say "Aw, you're so sweet!"
    show lexi wink
    lexi.say "And that means you get a reward..."
    show lexi b normal
    "Lexi chuckles as she turns her back on me and starts to walk towards the bed."
    "Well, I use the word 'walk' in the most general sense possible."
    "Because what Lexi actually does is turn movement into an act of seduction."
    "I follow the rolling of her hips and the way she tosses her head."
    "In fact I follow it so closely that I almost miss the fact that she's also stripping off."
    "So it comes as a surprise to see that she arrives at the side of the bed completely naked!"
    lexi.say "I think you can guess what your reward is, can't you?"
    "All I can do is nod eagerly as I tear off my own clothes."
    "Lexi nods as she climbs onto the bed, walking on her hands and knees."
    show lexi flirt
    lexi.say "That's right - you get to fuck me, [hero.name]."
    lexi.say "You get to fuck me nice and hard too!"
    show lexi doggy with fade
    "Needless to say my cock is hard as a rock as I clamber up behind Lexi."
    "And there's noting on my mind save for giving her exactly what she wants."
    menu:
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "Lexi waggles her ass at me, as if I needed anymore encouragement."
            "But what the gesture does do is make me sure of what I'm going to do next."
            "And that's to grab hold of Lexi's buttocks, making sure I have a firm grip."
            "She flinches a little and lets out a yelp as I do so, but that doesn't put me off."
            show lexi doggy anal
            "A moment later I'm parting her buttocks and aiming the head of my cock between them."
            "The first Lexi knows about my intentions is when I push the tip in there."
            lexi.say "Whoa..."
            lexi.say "So that's what you want, yeah?"
            lexi.say "Well, don't let me stop you!"
            "Most girls would need some cajoling to let me take them up the ass like this."
            "But Lexi seems to be at ease with the idea, making no protests against it."
            "And she even wriggles herself backwards and onto me, working it into her as she does so."
            show lexi doggy pleasure
            lexi.say "Mmm..."
            lexi.say "That feels SO good!"
            lexi.say "I love having your cock in my ass, [hero.name]."
            lexi.say "It's just so BIG!"
            "Lexi's words have an instant effect on me, urging me on to please her."
            "And so I make an effort to push into her as deep as I can possibly go."
            "I can feel her muscles fighting me for every inch, resisting for all they're worth."
            "But at the same time, Lexi moans and sighs, clearly enjoying the experience."
            "There's a couple of seconds when I feel like I can't go any further."
            "I'm literally as deep into Lexi as I can get."
            "And then I feel the tension almost melt away from her muscles."
            "Lexi's ass yields to me in that moment, and it's all the chance I need."
            "Before she can ask me for more, I'm already picking up speed."
            "My cock thrusting in and out of her faster with each second that passes."
            "For the first time tonight I feel like I'm the one taking the lead."
            "While Lexi bows her head in submission, letting me have my way with her completely."
            show lexi doggy normal
            lexi.say "Aaah..."
            lexi.say "That's it..."
            lexi.say "Don't you dare stop now..."
            lexi.say "Fuck my ass, please - fuck it harder!"
            "I'm already struggling to do that, so Lexi's plea is hardly needed."
            show lexi doggy pleasure tongueout
            "But it does sound pretty good to my ears, making me try even harder."
            "All I can think about is keeping on going, pushing myself ever further."
            "Lexi seems to be able to take all that I have to give and more besides."
            "No matter how hard I pound away at her, she just nods and demands more."
            "I'm beginning to think that the woman might be totally insatiable."
            "But I know all too well that the same can't be said for me."
            "As I can already feel myself starting to cum!"
            call cum_reaction (lexi, 'anal', sexperience_min) from _call_cum_reaction_122
            if _return == "anal_inside":
                "And so I don't stop what I'm doing for a moment, I just keep on going."
                show lexi doggy ahegao creampie with hpunch
                $ lexi.sub += 2
                "Lexi lets out a cry of release as I shoot my load into her."
                with hpunch
                "Her muscles twinge and twitch, letting me know that she's cumming too."
                with hpunch
                "But I don't even think of pulling out until I'm completely spent."
                show lexi doggy pleasure -creampie -anal dickcum analdrip -tongueout
                "And when I do, it sends streams of sticky, white semen running down her legs."
            elif _return == "anal_outside":
                show lexi doggy -tongueout -anal normal
                "I manage to pull out at the last moment, just before I feel myself lose it."
                "Lexi moans at the sensation of me dragging my cock all the way out of her."
                show lexi doggy cumshot pleasure with hpunch
                "But she only has a split second to wait before I shower her ass with cum."
                show lexi doggy -cumshot cum onbody dickcum with hpunch
                $ lexi.love += 1
                $ lexi.sub += 1
                "It spatters over her buttocks and begins to run down the inside of her thighs."
                with hpunch
                "And it's only as I stand back that I realise she's cumming too."
                "Her whole body quivering and shaking as she does so."
            $ lexi.flags.anal += 1
        "Fuck her pussy":
            "Lexi waggles her ass at me, like I really need to be teased to pounce on her."
            "Which is exactly what I do a moment later, making her yelp in surprise."
            "Lexi giggles in anticipation, grinding her butt into my groin."
            lexi.say "Mmm..."
            lexi.say "Something feels nice and hard back there!"
            lexi.say "Why don't you stick in in me and see how soft you're making me?"
            lexi.say "I'm melting to have that thing inside of me!"
            call check_condom_usage (lexi, love=180) from _call_check_condom_usage_83
            if _return == False:
                return
            if CONDOM:
                show lexi doggy condom
            "As soon as I get a hold of Lexi, I thrust my cock between her legs."
            "And the first thing I feel is just how slick and warm she is down there."
            "She wasn't lying when she said that she was ready for me just now."
            "And the sensation of my cock sliding along her lips is indescribable."
            "In fact that only thing better is when I slip inside of her a moment later."
            "Lexi's pussy parts like a flower opening for the sun."
            "There's a moment of resistance, which only makes it feel better."
            show lexi doggy vaginal pleasure
            "And then I'm inside of her, sinking in all the way in one smooth move."
            lexi.say "Oh yeah...oh fuck..."
            lexi.say "That's the prize, that's it right there..."
            show lexi doggy normal
            lexi.say "I'm your prize, [hero.name]..."
            lexi.say "So you have to hurry up and fuck me hard!"
            "I'm already doing all I can to make that happen."
            "And Lexi's words only serve to make me work that much harder."
            show lexi doggy pleasure
            "I begin to pick up speed without even thinking, thrusting in and out of her."
            "Somehow Lexi manages to feel as smooth as silk, softly caressing my cock."
            "And yet at the same time her muscles are tight, squeezing me too."
            play sound spank
            show lexi doggy slap tongueout with hpunch
            "Talk about a steel hand in a silk glove!"
            "Lexi's head sags low as she rocks back and forth."
            show lexi doggy noslap
            "It seems like she's nodding, urging me on."
            "But she could just be swaying in sympathy with my motions."
            play sound spank
            show lexi doggy slap slapmark with hpunch
            "Either way, I take it as a sign of submission."
            "A sign that Lexi's handed over control to me alone."
            show lexi doggy noslap
            "But maybe that's not as clear as I might have thought."
            "Sure, she's letting me have my way with her, offering no resistance."
            "Yet she's also showing no signs of slowing down either."
            "Every ounce of effort that I put into fucking her, Lexi soaks up like a sponge."
            "I can already feel my muscles getting tired, by heart pounding in my chest."
            "And yet she just keeps right on going, taking all that I have to give."
            "At this rate, I'm either going to pass out or shoot my load."
            "Luckily for me, it feels like the latter's about to happen..."
            call cum_reaction (lexi, 'vaginal', sexperience_min, 190) from _call_cum_reaction_123
            if _return == "vaginal_condom":
                "I don't stop what I'm doing for a moment, I just keep on going."
                "Lexi lets out a cry of release as I shoot my load into her."
                "Her muscles twinge and twitch, letting me know that she's cumming too."
                "But I don't even think of pulling out until I'm completely spent."
            elif _return == "vaginal_outside":
                show lexi doggy normal -tongueout -vaginal
                "I manage to pull out at the last moment, just before I feel myself lose it."
                "Lexi moans at the sensation of me dragging my cock all the way out of her."
                show lexi doggy cumshot
                if not CONDOM:
                    show lexi doggy pleasure with hpunch
                    "But she only has a split second to wait before I shower her ass with cum."
                    show lexi doggy cum onbody dickcum -cumshot with hpunch
                    $ lexi.love += 1
                    $ lexi.sub += 1
                    "It spatters over her buttocks and begins to run down the inside of her thighs."
                else:
                    with hpunch
                    "There's only a split second to wait before I cum."
                with hpunch
                "And it's only as I stand back that I realise she's cumming too."
                "Her whole body quivering and shaking as she does so."
            elif _return == "vaginal_inside_pill":
                mike.say "Lexi..."
                mike.say "You're...on the...pill..."
                mike.say "Right?!?"
                lexi.say "Y...yeah..."
                lexi.say "Wh...why?"
                "Lexi gets her answer a moment later in the most literal way imaginable."
                show lexi doggy creampie ahegao with hpunch
                $ lexi.love += 2
                "She lets out a cry of release as I shoot my load into her."
                with hpunch
                "Her muscles twinge and twitch, letting me know that she's cumming too."
                with hpunch
                "But I don't even think of pulling out until I'm completely spent."
                show lexi doggy pleasure -vaginal dickcum vaginaldrip -tongueout
                "And when I do, it sends streams of sticky, white semen running down her legs."
            elif _return == "vaginal_inside_pregnant":
                "Both of us know there's no danger while Lexi's pregnant."
                "And so I don't stop what I'm doing for a moment, I just keep on going."
                show lexi doggy creampie ahegao with hpunch
                $ lexi.love += 3
                "Lexi lets out a cry of release as I shoot my load into her."
                with hpunch
                "Her muscles twinge and twitch, letting me know that she's cumming too."
                with hpunch
                "But I don't even think of pulling out until I'm completely spent."
                show lexi doggy pleasure -vaginal dickcum vaginaldrip -tongueout
                "And when I do, it sends streams of sticky, white semen running down her legs."
            elif _return == "vaginal_inside_mad":
                lexi.say "You have to pull out!"
                lexi.say "NOW!"
                "But even as Lexi speaks the words, it's already too late."
                "I can't stop, I just keep on going."
                show lexi doggy creampie with hpunch
                $ lexi.love -= 5
                $ lexi.impregnate()
                "Lexi lets out a cry of release as I shoot my load into her."
                with hpunch
                "Her muscles twinge and twitch, letting me know that she's cumming too."
                show lexi doggy normal -vaginal dickcum vaginaldrip -tongueout with hpunch
                "I pull out the moment that I can manage it, the pair of us falling onto the bed."
                "And then we stare at each other in silence, our faces mirror images of horror."
            elif _return == "vaginal_inside_happy":
                "Remembering that we didn't use a condom, I make to pull out of Lexi."
                "But to my surprise, she holds on tight, refusing to let me go!"
                lexi.say "What's wrong?"
                lexi.say "Don't you like your prize?"
                show lexi doggy creampie ahegao with hpunch
                $ lexi.love += 5
                $ lexi.impregnate()
                "Lexi lets out a cry of release as I shoot my load into her."
                with hpunch
                "Her muscles twinge and twitch, letting me know that she's cumming too."
                with hpunch
                "I try to escape, but she holds onto me until I'm completely spent."
                show lexi doggy pleasure -vaginal dickcum vaginaldrip -tongueout
                "Only then does Lexi release me, the pair of us falling onto the bed."
                "But whereas she looks delighted, my face is a picture of horror."
    "Afterwards, Lexi lies on the bed, panting and slick with sweat."
    "For the first time in as long as I can remember, she's silent too."
    "Not a single word escapes her mouth as we bask in the afterglow."
    "Which for a girl with a mouth like hers is a minor miracle."
    return

label lexi_sleep_date_fuck_male(location="hero"):
    if game.hour > 19 or game.hour < 6:
        scene bg bedroom1
        show lexi naked
        with fade
        if lexi.is_sex_slave:
            lexi.say "May I share your bed tonight, Master?"
        else:
            lexi.say "Mmm...you cool with me spending the night here?"
        menu:
            "No":
                mike.say "No...I have to be up really early in the morning."
                "The sex was beyond incredible, but now I want to be alone."
                "Lexi frowns in disappointment, clearly trying to shrug off the sense of rejection."
                lexi.say "Okay...sleep well, I guess."
                "She shakes her head as she collects her things and leaves my bedroom."
                $ lexi.love -= 3
                call sleep from _call_sleep_34
                $ game.room = "bedroom1"
            "Yes":
                mike.say "YES...I mean, yes...if you want to!"
                "I try to keep from sounding too desperate and needy, but I'm not sure I manage it."
                show cuddle lexi with fade
                "Lexi curling up against me beneath the covers is almost as good as the sex - almost..."
                if lexi.is_sex_slave:
                    lexi.say "Sweet dreams, Master..."
                else:
                    lexi.say "Sweet dreams, [hero.name]..."
                mike.say "You too, Lexi..."
                $ lexi.love += 3
                call sleep ("lexi") from _call_sleep_13
                $ game.room = "bedroom1"

    return

label lexi_hottub_sex_male:
    $ game.active_date.clothes = "swimsuit"
    $ CONDOM = False
    show bg pool
    "All it takes is the mere mention of there being a hot-tub at my place for Lexi to say yes to taking a dip."
    "Well, if I'm honest, it's more like she invites herself over before I have the chance to suggest it."
    "And you only have to take a look at Lexi to know that I'm only ever going to say yes to that!"
    "But all the same, when she arrives and hurries to the bathroom to change, I try to play it cool."
    "I don't want to be the kind of jerk that just assumes Lexi's come over here with sex on her mind."
    "I want her to think that I respect her as a woman too."
    "That I don't just see her as a sex-object."
    "And that's not just me pretending to be a feminist or woke, or something."
    "I actually do want Lexi to be more to me than an easy lay!"
    show lexi swimsuit with dissolve
    lexi.say "Hey, [hero.name]!"
    lexi.say "Cannonball!"
    "But it's hard when she looks and acts like she does!"
    "Lexi comes dashing out of the house in her swimsuit, straight towards the tub."
    "She actually vaults over the side and splashes down into the water."
    "I get a face-full, and water goes sloshing over the sides of the tub and onto the ground."
    mike.say "Urgh!"
    mike.say "Lexi!"
    "I scrub the water out of my eyes, shaking my head the whole time."
    "But I don't hear anything in the way of an apology from Lexi."
    "In fact, what I can hear is the sound of her typically filthy laughter."
    hide lexi
    show hottub lexi
    with fade
    lexi.say "Aw, come on, [hero.name]."
    lexi.say "Lighten up!"
    "I force a smile onto my face, not wanting to ruin the moment."
    "Instead of dwelling on my soaking, I take in the sight of Lexi instead."
    "Of course, she has on a swimsuit that leaves nothing to the imagination."
    "Which means that my own imagination is left free to ponder the possibilities."
    "God but her body looks good in the water."
    "And the way that her breasts float too..."
    lexi.say "There you go."
    lexi.say "A good hard look at the merchandise."
    lexi.say "That's always enough to cheer a guy up!"
    "I shake my head, realising that I've been caught in the act."
    "Looking up to meet Lexi's eyes, I do the best I can to play innocent."
    mike.say "What?!?"
    mike.say "Oh no, I wasn't..."
    "Lexi lets out another peal of filthy laughter."
    lexi.say "Of course you were, [hero.name]!"
    lexi.say "What, you think a girl like me doesn't know when a guy's checking her out?"
    lexi.say "I know for sure that you're hard as rock right now too!"
    mike.say "We...we're supposed to be relaxing, Lexi."
    mike.say "You know - chilling out in the water?"
    "Lexi rolls her eyes at my continued attempts at making excuses for myself."
    lexi.say "Yeah, [hero.name], whatever!"
    lexi.say "But we're gonna fuck too, right?"
    mike.say "Ah, sure, Lexi."
    mike.say "If that's what you want..."
    "As if to answer the question, Lexi tugs at the top of her swimsuit."
    "The knot holding it in place comes apart easily, spilling her breasts as it does so."
    "Lexi gives a little shiver, like she's relieved to be free of it."
    "And this makes her chest jiggle and shake in an almost hypnotic fashion."
    lexi.say "Oh, I think you know what I want!"
    "With that, Lexi turns her back on me and leans against the edge of the tub."
    show hottub sex male lexi outside with fade
    "She pushes her ass in my direction, shaking it in a suggestive manner."
    mike.say "Yeah, Lexi."
    mike.say "I think I know what you want!"
    "Any thought of trying to play the innocent vanishes in that moment."
    "Lexi's made it more than plain that she wants to get it on."
    "So what's the point in pretending that I don't want to do it too?"
    "I tug down my trunks as quickly as I can, hurrying towards Lexi's ass."
    "She looks back over her shoulder at me, nodding eagerly as I come."
    call lexi_dick_reactions from _call_lexi_dick_reactions_1
    lexi.say "That's right, [hero.name]."
    lexi.say "You DO know what I want!"
    "I don't hesitate to reach out and take a firm hold of Lexi's ass."
    "She giggles and squirms playfully as I part her buttocks."
    show hottub sex male lexi inside
    "But when I push the head of my cock against her pussy, her mood changes."
    "Now she's moaning and panting, anticipating what's coming next."
    "I'm feeling the same way too, and so I waste no more time."
    "A second later, I shove myself forwards, forcing my cock into Lexi."
    "She shudders at the sensation of me entering her."
    "But I hold her firmly, making sure that I can slide in with one motion."
    "I don't stop once I'm as deep as I can go."
    "Instead I keep on moving back and forth, in and out."
    "I also keep my speed constant, never going faster or slower."
    "This means that Lexi is forced to ride the length of my cock over and again."
    "She rocks beneath me, the constant motion occupying her senses."
    "Before now, Lexi was all cheeky lines and teasing gestures."
    "Yet now she has no choice but to surrender as I fuck her."
    "It's not like I mind Lexi's smart comments and flirty gestures."
    "But shutting her up like this is a hell of a lot of fun!"
    "And maybe that's why I know that it's not going to be long before I cum?"
    "Maybe it's because I'm enjoying myself that much?"
    call cum_reaction (lexi, 'vaginal', 1) from _call_cum_reaction_124
    if _return == "vaginal_outside":
        show hottub sex male outside
        "I pull my cock out of Lexi without warning and in one smooth motion."
        "She yelps in alarm at the sensation, looking over her shoulder at me."
        "But it's far too late for any such protest to matter."
        $ lexi.sub += 1
        show hottub sex male cumshot with hpunch
        "I shoot my load over her a few seconds later."
        with hpunch
        "Streamers of sticky white cum stripe Lexi's buttocks."
        with hpunch
        "And then it runs down her legs to mingle with the water below."
    else:
        "I make a point of keeping my pace steady as I get ready to shoot my load."
        "And I doubt that Lexi knows it's coming until the very last moment."
        "But she's not the kind of girl to mind me cumming inside of her."
        show hottub sex male cumshot with hpunch
        $ lexi.love += 1
        "Which means that when I lost it, she gasps in mixture of surprise and delight."
        show hottub sex male ahegao with hpunch
        "Lexi makes a soft, almost delirious sound of pleasure afterwards."
        with hpunch
        "Even as it begins to seep out and run down the inside of her thighs."
    hide hottub
    show hottub lexi
    with fade
    "Once it's over, Lexi lets herself collapse against the side of the tub."
    "She lets out a long breath, emptying her lungs and shaking her head."
    lexi.say "Now we can relax, [hero.name]!"
    lexi.say "Now we've earned it!"
    "I'm too exhausted to say a word."
    "And so I simply nod in agreement."
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ lexi.sexperience += 1
    $ game.active_date.clothes = None
    return

label lexi_fuck_bathroom:
    $ game.play_music("music/roa_music/city_nights.ogg")
    scene bg secondfloor
    "When you live in a shared house, there are certain things that become really important."
    "And one of those is time in the bathroom, knowing you can get in there and get things done."
    "Which is why I can't help letting out a sigh of frustration as I arrive to find it occupied."
    "What the hell is this?"
    "Everyone knows it's my turn for a shower."
    scene bg door bathroom at center, zoomAt(1, (640, 720)) with fade
    "But the door's closed and I can hear the sound of water running in there."
    show bg door bathroom at center, traveling(1.5, 0.3, (640, 1040))
    pause 0.3
    play sound door_knock
    "I lean in and knock on the door, wanting an explanation and wanting it fast."
    mike.say "Hey, who's in there?"
    mike.say "Don't you know it's my shower time?"
    lexi.say "Huh..."
    lexi.say "What was that?"
    "I let out a grunt of frustration."
    "Barging in on people isn't something I like to do."
    "But it seems like it's either that or give up my shower."
    scene bg black with dissolve
    pause 0.5
    scene bg bathroom with fade
    play sound shower loop
    "So I open the door and slip inside."
    mike.say "I said..."
    mike.say "It's my shower time..."
    "What I meant to say trails off as I enter the bathroom."
    "The shower's already running, filling the room with steam."
    "But that's not what grabs my attention and leaves me in a stunned silence."
    show lexi a naked nophone with dissolve
    "What does that is the sight of Lexi, naked in the shower cubicle."
    show fx exclamation
    lexi.say "Hey, [hero.name]!"
    show lexi wink
    lexi.say "Like what you see?"
    hide fx
    show lexi normal
    "By now I've dropped my towel on the floor and taken a step towards her."
    "The water is cascading down over Lexi's body, dripping from every curve."
    "And she's not making any effort to cover herself up either."
    mike.say "I...wanted...shower..."
    mike.say "I...I wanted to take a shower, Lexi!"
    show lexi happy
    "Lexi smiles knowingly and beckons me to join her."
    lexi.say "What's stopping you?"
    lexi.say "Plenty of room in here with me!"
    show lexi normal
    "All of my irritation and annoyance just seems to fall away."
    "What's the point of being prickly in the face of an offer like that?"
    "Without saying a word, I strip off my clothes and hurry to join Lexi."
    show lexi b
    "She lets out a wicked chuckle as I step into the shower beside her."
    lexi.say "Hey, [hero.name]."
    show lexi wink
    lexi.say "You ever use a shower to get dirty?"
    "And with that, Lexi pushes her ass into my groin."
    "She presses me against the wall, grinding on me the whole time."
    "My cock was hard before I got into the shower."
    "And it's not like I need to be told what to do next."
    scene lexi showersex
    show lexi showersex outside
    with fade
    "I slip a hand under one of Lexi's thighs, lifting her leg."
    "She reaches back and takes hold of my neck, bracing herself against me."
    "And just like that, she's mine to do with as I like..."
    menu:
        "Fuck her ass":
            "I know that Lexi was the one that started getting wild here."
            "But that doesn't mean that I can't get in on the action too."
            "Which is why I take advantage of her buttocks being spread wide."
            "Without letting her know what I'm doing, I aim my cock between them."
            lexi.say "Ah..."
            lexi.say "Hello!"
            "Lexi makes no attempt to protest or stop me."
            "Instead she lets out a filthy peal of laughter."
            lexi.say "You really wanna get dirty, huh?"
            lexi.say "Well, you want my ass that badly..."
            show lexi showersex anal -outside
            "Lexi nods as I begin to push my way into her."
            "It's a tight fit, and her muscles protest."
            "But every fraction of an inch I sink into her feels incredible."
            "Lexi moans and gasps, but she never once tells me to stop."
            "Instead she looks back over her shoulder at me the whole time."
            "Her eyes are wide, and she nods for me to keep going."
            "That becomes easier to do once I'm in as deep as I can go."
            "Lexi's muscles are still squeezing my cock."
            "But now they're beginning to quiver and surrender."
            "By the time I start to thrust in and out, her body surrenders to me."
            "All of that effort is rewarded as Lexi's ass melts around me."
            "Now fucking her ass is as effortless as can be."
            "And it feels better than ever, making me pick up the pace."
            "Lexi follows the example of her muscles, sagging against me."
            show lexi showersex anal pleasure
            "I honestly think she'd collapse into a heap if I let her go!"
            "I have a magnificent view of her body under the shower."
            "The water running down her like a waterfall."
            "Her breasts bounce up and down as I keep on thrusting into her."
            "I don't know how much longer I can last..."
            menu:
                "Cum inside":
                    with hpunch
                    "So it comes as no surprise to me that I shoot my load a second later."
                    show lexi showersex anal creampie with hpunch
                    "I'm too deep inside of Lexi to pull out, and so she takes the whole thing."
                    show lexi showersex anal ahegao with hpunch
                    "I hold onto her as she jerks and wriggles, cumming just as quickly as I did."
                    "And as soon as we're both spent, we slide down the tiled wall and onto the floor."
                    "Lexi and I sit there, exhausted and panting, as the water washes us clean."
                    $ lexi.love += 1
                "Pull out":
                    "I try to lift Lexi up just enough..."
                    show lexi showersex outside -anal
                    show sexinserts chest lexi zorder 1 at center, zoomAt(1, (700, 860))
                    show sexinserts belly lexi as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                    "And like a charm, my cock pops out of her ass!"
                    "She seems to snap out of it at the same time as this happens."
                    lexi.say "Oh god..."
                    lexi.say "I'm gonna cum!"
                    show lexi showersex outside ahegao with hpunch
                    "Lexi writhes and wriggles in my arms as her orgasm takes hold."
                    show lexi showersex outside creampie
                    show sexinserts chest lexi cum zorder 1 at center, zoomAt(1, (700, 860))
                    show sexinserts belly lexi cum as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                    with hpunch
                    "And I shoot my load as I struggle to hold onto her."
                    with hpunch
                    "Then we slide down the tiled wall and onto the floor."
                    "We sit there, exhausted and panting, as the water washes us clean."
                    $ lexi.sub += 1
                    hide sexinserts
                    hide bellycum
            $ lexi.flags.anal += 1
        "Fuck her pussy":
            "I feel the head of my cock rubbing against the lips of Lexi's pussy."
            "Sure, everything's wet from the water raining down on us right now."
            "But I'm sure that she's a different kind of wet too!"
            "And the way she moans as I torment her with my cock lets me know I'm right."
            show lexi showersex vaginal -outside
            lexi.say "Oh...oh yeah..."
            lexi.say "My dirty little pussy likes that!"
            lexi.say "It wants you inside of it - real bad!"
            "It's not like I needed Lexi to talk dirty to me for this to work."
            "But hearing stuff like that coming out of her mouth is a nice little bonus!"
            "It spurs me on to take an even tighter hold of her."
            "And once that's done, I waste no time in pushing inside."
            show lexi showersex vaginal pleasure
            lexi.say "Mmm..."
            lexi.say "That's what I want..."
            lexi.say "Please, [hero.name], fuck me hard!"
            "Okay, I admit it - now she's talking me into trying harder!"
            "Knowing that Lexi wants this every bit as much as I do."
            "That's more than enough to make me give her all that I can."
            "I don't start off slow and build up my pace."
            "Instead I launch straight into it."
            "I push my cock as deep into Lexi as it'll go."
            "She moans as I hold it there for a moment."
            "And then I start pounding away on her in earnest."
            "It feels like every time I thrust in and out, she loses it by degrees."
            "Her cries become a little louder and she leans into me a little more."
            "Pretty soon I'm sure that I'm all that's holding her up."
            "Lexi flops helplessly in my arms, offering no resistance at all."
            "Which makes it that much harder when I feel myself starting to cum!"
            menu:
                "Cum inside":
                    "I hold onto Lexi as tightly as I can when I shoot my load."
                    show lexi showersex vaginal creampie with hpunch
                    "This means that I'm deep inside of her when it happens."
                    with hpunch
                    "Unable to escape, she wriggles and squirms in my grip."
                    lexi.say "Ah..."
                    lexi.say "Shit..."
                    show lexi showersex vaginal ahegao with hpunch
                    lexi.say "I'm cumming!"
                    "I don't loosen my hold on Lexi afterwards, just slide down the wall."
                    "Lexi and I sit on the floor, exhausted and panting, as the water washes us clean."
                    $ lexi.love += 1
                "Pull out":
                    "I lift Lexi up just enough..."
                    show lexi showersex outside -vaginal
                    show sexinserts chest lexi zorder 1 at center, zoomAt(1, (700, 860))
                    show sexinserts belly lexi as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                    "And my cock pops right out of her pussy!"
                    "Lexi's eyes open as soon as it happens."
                    lexi.say "Oh fuck..."
                    lexi.say "I'm gonna cum!"
                    show lexi showersex outside ahegao
                    lexi.say "I'm gonna cum!"
                    with hpunch
                    "Lexi squirms in my arms, unable to resist her orgasm."
                    show lexi showersex outside creampie
                    show sexinserts chest lexi cum zorder 1 at center, zoomAt(1, (700, 860))
                    show sexinserts belly lexi cum as bellycum zorder 2 at center, zoomAt(1, (-140, 970))
                    with hpunch
                    "I shoot my load as I struggle to hold onto her."
                    with hpunch
                    "Then we slide down onto the floor."
                    "We sit there, exhausted and panting, as the water washes us clean."
                    $ lexi.sub += 1
                    hide sexinserts
                    hide bellycum
    $ lexi.flags.showersex = True
    $ lexi.sexperience += 1
    stop sound fadeout 1.0
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
