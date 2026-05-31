init python:
    InteractActivity(**{
    "name": "fuck_amy",
    "display_name": "Fuck",
    "label": "ACTIVE_GIRL_fuck_ROOM",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            HasStamina(),
            ),
        PersonTarget(amy,
            IsActive(),
            MinStat("love", 100),
            MinStat("sub", 25),
            MinStat("sexperience", 2),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })

    Event(**{
    "name": "amy_hottub_sex_male",
    "label": "amy_hottub_sex_male",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            HasStamina(),
            IsActivity("date_hot_tub_home")),
        PersonTarget(amy,
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


label amy_hottub_sex_male:
    $ game.active_date.clothes = "swimsuit"
    $ CONDOM = False
    scene bg pool with fade
    "When I invited Amy over to take a dip in the hot-tub, I had no idea what she'd say."
    "I mean, who knows if goths are really into that kind of thing?"
    "They seem to spend most of their time wearing multiple layers of black clothing."
    "And the fact they're all pretty pale doesn't suggest they spend much time naked either!"
    "So even when Amy said yes, I was still kind of paranoid that she was just being polite."
    "Like she'd wait until the last possible minute, then call me up and cancel the whole thing."
    "But as the appointed time draws ever closer, that phone-call doesn't happen."
    "And so I make myself go about preparing the hot-tub as I would for any other girl."
    "I make sure that it's clean enough to eat your dinner off of."
    "Filled to the brim with clean, bubbling water too."
    "I put candles around the edge to create a more intimate ambiance."
    "Hell, I even manage to find some flower petals to scatter about the place too!"
    "And I'm just in the process of uncorking the wine when I hear the sound of footsteps approaching."
    amy.say "Hi, [hero.name]..."
    amy.say "I hope I'm not late!"
    "I turn at the sound of Amy's voice, replying as I do so."
    mike.say "Hey, Amy..."
    mike.say "No worries..."
    mike.say "You're not..."
    show amy swimsuit with easeinleft
    "I stop before I can finish what I was going to say."
    "Because the mere sight of Amy is enough to render me speechless."
    "Luckily for me, she seems to be suffering from the same thing too."
    "Then we both notice that the other is in a similar state."
    amy.say "Sorry, I was just..."
    show amy surprised
    amy.say "Woah..."
    amy.say "You went to all this effort?"
    show amy blush
    amy.say "And just for me?"
    mike.say "You...you look amazing, Amy!"
    mike.say "I feel like all the effort I put in..."
    mike.say "Well...like it wasn't nearly enough!"
    "When I'm done talking, Amy's still got that same look on her face."
    "Only now it's me that she's looking at in amazement."
    amy.say "Wh...what do you mean?"
    "My eyes travel up and down over Amy's body as I wonder what in the hell she's talking about."
    "Amy must have come dressed in something that she could just slip off as soon as she arrived."
    "Because right now she's standing in front of me in only her swimming costume."
    "And the sight of her is pretty amazing."
    "Of course she's pale, like I was expecting her to be."
    "But the shape of her body and the way that it curves in and out..."
    mike.say "I mean you look stunning in that swimming costume, Amy!"
    show amy shy
    "Only now do I see some colour appear upon Amy's skin."
    "Because her cheeks flush red as she hears my compliment."
    amy.say "Oh..."
    amy.say "Thank you, [hero.name]!"
    amy.say "I don't often get the chance to wear something like this."
    amy.say "You know how we goths are."
    show amy happy
    amy.say "We don't often hang out poolside!"
    mike.say "Well you should!"
    mike.say "Or at least you specifically should, Amy!"
    show amy normal
    "By now Amy's cheeks are as red as they can be."
    "She waves away my comments as she hurries towards me."
    show amy kiss with fade
    $ amy.flags.kiss += 1
    "And finally puts a stop to them by standing on her tip-toes to kiss me."
    "It only starts out as an innocent kiss, one to say hello."
    "But now that Amy's so close to me, I can't seem to help myself."
    "Before I know what's happening, I've wrapped my arms around her."
    "And I'm all but lifting her off the ground."
    "Amy seems to respond in kind, clinging to me even more tightly than before."
    "She also sticks her tongue deep into my mouth too!"
    "I'm in my trunks, so I can feel the softness and warmth of her body against mine."
    "Which soon starts to make a part of me go in the opposite direction, getting harder."
    hide amy kiss
    show hottub amy at blur(5)
    with fade
    "I'd envisioned this thing starting out slowly."
    "Maybe with us chatting as we drank some of the wine."
    "Then slipping into the water to relax as we had some more of it."
    "The ace up my sleeve after that was going to be the offer of a massage."
    "And from there I was hoping that Amy would be in the mood to get it on."
    hide hottub amy
    show amy kiss
    with fade
    $ amy.flags.kiss += 1
    "But I can already feel her hands reaching into my trunks!"
    "So it looks like she's skipping ahead a good couple of steps."
    "Which, for the record, is fine by me!"
    hide amy kiss
    show hottub sex male amy outside
    with fade
    "I move towards the edge of the hot-tub, hoping all the time that I don't fall in."
    "Amy matches my steps perfectly, so that we can slip into the water together."
    "At the same time we're doing all we can to undress each other too."
    "Amy has my shorts down just as I manage to free her breasts."
    "The bob and float in the water as we sink down."
    "And I stare in sheer awe as her nipples stiffen before my eyes."
    "Amy chuckles as she strokes my cock, slipping off her swimming costume."
    "Then she turns her back to me, pushing her ass in my direction."
    "I hardly need to pull her onto me, as she sits on my cock herself."
    "Then Amy starts to work herself backwards, pushing it between her buttocks."
    "All this time her bunches are swaying this way and that."
    "I find my eyes following them closely, like I can't look away."
    "Without a conscious thought, my hands reach out."
    "And then I grab hold of them."
    "Amy lets out a squeal of surprise."
    "But I note that she doesn't tell me to stop."
    "At the same time, I can feel the head of my cock rubbing against the lips of her pussy."
    "Amy's wriggling around, like she's trying to make it sink into her without me getting involved."
    show hottub sex male inside
    "So I pull back on her hair while thrusting my groin forwards at the same time."
    amy.say "OH..."
    amy.say "Oh fuck..."
    amy.say "Y...yeah!"
    "I can feel myself sinking into Amy in that moment."
    "But it can't just be on account of me tugging at her hair."
    "It must be from that sensation making her pussy surrender."
    "Which must in turn mean that she's getting off on it!"
    "The realisation spurs me on, making me pick up pace."
    "Now I'm thrusting into her faster and harder than ever."
    "I keep a firm hold on Amy's hair, but more to keep her in place than anything else."
    "Even so, it doesn't seem to do anything to lessen her desire for more."
    "Amy braces her hands against my thighs, holding on as best she can."
    amy.say "H...harder..."
    amy.say "Fuck me...harder..."
    amy.say "Please?"
    "I do all that I can to obey Amy's demands."
    "But the truth is that I'm already going all out."
    "So I pull harder and make more noise in the hope that it'll have the desired effect."
    "And it seems that it does the trick, as Amy stops forming actual words."
    "Instead her mouth hangs open and nothing but animalistic moans emerge from it."
    show hottub cumshot with hpunch
    $ amy.impregnate()
    "With one last gasp of my own, I realise that I can't hold on any longer."
    $ amy.love += 1
    show hottub sex male ahegao with hpunch
    "As soon as I'm as deep into Amy as I can go, I shoot my load."
    with hpunch
    "And then I collapse into the water, my muscles losing all strength."
    "Amy falls with me, floating in front of me as she begins to cum too."
    "I can barely hold onto her as it happens, just floating in the water."
    "Maybe now we can enjoy the wine and the warmth."
    "Just as soon as we regain the power of speech."
    "That and the ability to move our limp bodies again."
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ amy.sexperience += 1
    $ game.active_date.clothes = None
    return


label amy_fuck_date_male(location="hero"):
    $ game.play_music("music/roa_music/city_nights.ogg")
    scene bg street
    show amy


    call amy_fuck_date_intro_male (location) from _call_amy_fuck_date_intro


    call amy_dick_reactions from _call_amy_dick_reactions


    call amy_fuck_date_foreplay_male from _call_amy_fuck_date_foreplay_male


    call amy_fuck_date_choices_male from _call_amy_fuck_date_choices_male


    call handle_npc_leaving (amy, _return) from _call_handle_npc_leaving_27
    if _return:
        return


    hide amy
    call amy_fuck_date_sleep (location="hero") from _call_amy_fuck_date_sleep
    return

label amy_fuck_date_intro_male(location="hero"):
    $ rand_intro = randint(0, 4)
    if rand_intro == 0:
        scene bg livingroom
        with fade
        pause 0.5
        show amy at center, zoomAt(1.5, (940, 1040)) with easeinright
        "Amy and I hurry through the house as quickly and quietly as we possibly can."
        "Because neither of us wants to risk waking my housemates before we get to my room."
        "All the same we can't help laughing and telling each other to keep the noise down."
        show amy upset at center, zoomAt(1.5, (640, 1040)) with ease
        amy.say "Shh!"
        mike.say "What the..."
        mike.say "I am being quiet!"
        amy.say "You so are not!"
        mike.say "Shh!"
        mike.say "Now you're the one being loud!"
        show amy normal
        "I open the door to my bedroom and then step inside."
        "Amy hesitates on the threshold, like she's going to argue with me."
        show amy surprised at startle
        "So I take hold of her wrist and pull her thought the doorway."
        amy.say "Whoa..."
        hide amy with easeoutleft
        pause 0.5
        scene bg bedroom1
        with fade
        pause 0.5
        show amy upset at center, zoomAt(1.5, (640, 1040)) with easeinright
        amy.say "Hey!"
        mike.say "No time for that..."
        mike.say "We've got business to take care of!"
        "Amy changes her tune almost as soon as the door is closed behind us."
        "She slips out of my hold and darts across the room to my bed."
        show amy flirt
        amy.say "Oh yeah?"
        amy.say "Well you're gonna have to catch me first!"
        hide amy
        show amy flirt
        "It's not like I need any serious encouragement to do that."
        "So I launch myself after Amy almost the second she starts moving."
        hide amy with moveoutleft
        "But she's still somehow faster than me, ducking out of reach."
        "This means that she makes it to the bed first, and hops onto it."
        "I leap in the same direction before she's all the way there."
        "And the result is that we land in a tangle of limbs on the mattress."
        show amy surprised at center, zoomAt(1.5, (640, 1040)) with hpunch
        "Amy squeals with surprise and delight as I grab hold of her."
        "Though the sound the bed makes under our weight is pretty loud."
        show amy flirt
        "And for a moment I'm worried that it's going to collapse under us!"
        hide amy
        show amy kiss
        with fade
        $ amy.flags.kiss += 1
        "Amy cures me of that fear by putting her lips firmly against mine."
        "Her tongue pushes between them as she kisses me deeply and with genuine passion."
        "As soon as she does so, I lose all interest in anything else."
        "We're still kissing each other as we struggle to undress."
        "Hands blindly tearing at our clothes in an effort to get undressed."
        show amy kiss naked with dissolve
        "Somehow we actually seem to manage pretty well."
        "Because when I next open my eyes, we're both naked!"
    elif rand_intro == 1:
        scene bg livingroom
        show amy
        mike.say "Phew..."
        mike.say "Am I ever glad we're back here, Amy!"
        mike.say "I mean, I had a GREAT night..."
        show amy annoyed
        mike.say "But the whole time I was looking forward to getting home."
        mike.say "Well...to be more honest, getting home with you!"
        mike.say "If you know what I mean?"
        scene bg bedroom1 with fade
        mike.say "Wha..."
        "I'm turning around from shutting my bedroom door behind us."
        show amy annoyed at center, zoomAt(1.5, (640, 1040)) with hpunch
        "But when I'm done, I find myself cut off by a hand in my face."
        "And seeing as how there's only two of us in the room, it has to belong to Amy."
        show amy angry
        amy.say "Fucking hell, man!"
        amy.say "Will you like shut up for two damn seconds!"
        hide amy
        show amy annoyed
        "Looking more than a little surprised, I take a step backwards."
        "And I do as Amy asks more out of shock than obedience."
        show amy normal
        amy.say "Ah..."
        amy.say "That's better!"
        "I open my mouth to speak again."
        show amy upset
        "But Amy cuts me off for a second time."
        amy.say "Not so fast, mister!"
        amy.say "New rule - you can only speak when I give you permission."
        amy.say "You got it?"
        "I nod, not wanting to be cut off for a third time."
        "And after a few seconds of making sure I'm silent, Amy nods too."
        show amy annoyed
        amy.say "Okay..."
        amy.say "Out with it."
        amy.say "But you'd better keep it short and sweet!"
        mike.say "I have to do this how long?"
        mike.say "All night?"
        show amy normal
        amy.say "Yup."
        amy.say "Until I say otherwise."
        "I let out a sigh and nod in agreement."
        "The last thing I want is to piss Amy off."
        "That way I might not get any action tonight!"
        "Amy seems to pick up on my mood."
        "And she offers me a smile."
        show amy happy
        amy.say "Oh..."
        amy.say "Don't worry about it, [hero.name]."
        show amy flirt
        amy.say "I'll give your mouth something else to do!"
        "Amy takes hold of my hand, then she leads me over to the bed."
        "And the next thing I know she's stripping off my clothes!"
        "Obviously I don't do anything to get in her way."
        "But somehow I still manage to earn a disapproving glance from her!"
        show amy upset
        amy.say "What are you waiting for?"
        amy.say "Start taking my clothes off too, dummy!"
        show amy normal
        "I leap into action almost as soon as Amy issues the command."
        "And pretty soon hands are darting this way and that."
        "At times we seem to be getting in each other's way."
        show amy naked with dissolve
        "But soon enough we're both stripped off and naked."
    elif rand_intro == 2:
        scene bg livingroom
        show amy flirt at center, zoomAt(1.5, (640, 1040))
        with fade
        "Neither Amy nor I seem to feel the need to say a single word as we hurry into my room."
        "I hold the door open for her to scurry inside, then turn to make sure it's firmly closed."
        "But when I turn back again, I'm treated to sight that literally stops me in my tracks."
        scene bg bedroom1 with fade
        "Somehow, in that short space of time, Amy's made it all the way across the room to my bed."
        "Not only that, there's a trail of her clothes leading from where I'm standing to over there."
        "And it's this that I find my eyes following as I search for her."
        "Every single item of clothing that she had on is there, from large to small."
        "And they get ever more intimate the closer I get to the bed as well."
        "My eyes take in each and every one of them as I follow the trail."
        show amy flirt naked with dissolve
        "Then I'm rewarded with the sight of Amy, laid on the bed as she waits for me."
        "Of course she's totally naked by now, smiling in amusement as I stare at her."
        amy.say "What are you looking at me like that for, [hero.name]?"
        amy.say "You never had a naked girl in here before now?"
        "I shake my head as I make it to the side of the bed."
        show amy close
        mike.say "Sure I did, Amy."
        mike.say "But that doesn't mean I take it for granted!"
        mike.say "Especially when the girl's as cute as this one."
        show amy normal blush
        "Amy chuckles and tries to shrug off the compliment."
        "But all the same I can see that she likes to be flattered like that."
        amy.say "Ah, shut up trying to sound all romantic."
        show amy flirt
        amy.say "And get over here already!"
        "I do as she says, lowering myself onto the bed."
        show amy kiss -blush -close with fade
        $ amy.flags.kiss += 1
        "As I do so, Amy leans over and puts her lips against mine."
        "She helps to pull off my clothes as we kiss, making the whole thing a little awkward."
        "But it also means that we're soon in a tangle of limbs that presses us close together."
        "And in that confusion of movement, I can hear Amy giggling and gasping the whole time."
        "It's odd, but that intimacy is almost as much what's making me hard as anything else."
        "That and the promise of what we're going to do next."
    elif rand_intro == 3:
        scene bg street
        show amy blush
        with fade
        "Amy and I have been behaving all night, keeping things nice and clean."
        "But the whole time there's been one of those undercurrents going on."
        "I know for sure that's where I am in terms of my feelings and emotions."
        "And I'm pretty sure that Amy's in the same place too right now."
        "It's like you can feel it every time we touch each other."
        "A little spark of excitement seems to jump between us like static electricity."
        "Neither of us says a thing about it either, not while we're out in public."
        "But the moment we make it back to my place, things start to change."
        scene bg house
        show amy blush at center, zoomAt(1.5, (640, 1040))
        with fade
        "As we hurry to my room, I can feel Amy squeezing my hand ever tighter."
        "And she's quickening her pace, almost pulling me after her."
        "When we finally reach my door, she's actually jumping on the spot."
        show amy happy at startle
        amy.say "Come on, [hero.name]..."
        amy.say "Hurry up already!"
        mike.say "Okay, Amy, okay..."
        mike.say "I'm going as fast as I can!"
        scene bg livingroom
        show amy at center, zoomAt(1.5, (640, 1040))
        with fade
        "I'm telling the truth, but haste is also making me clumsy."
        "I keep on fumbling with the door handle in my eagerness to get inside."
        "Finally it opens and Amy pushes me inside without warning."
        show amy normal with hpunch
        mike.say "Whoa..."
        scene bg bedroom1
        show amy flirt at center, zoomAt(1.5, (640, 1040))
        with fade
        "But even once we're in my bedroom, the pace doesn't let up."
        "Amy takes hold of my hand again and leads me straight over to the bed."
        amy.say "Clothes off, [hero.name]..."
        show amy upset at startle
        amy.say "NOW!"
        "I nod and begin to do as I'm told, desperately pulling off my clothes."
        hide amy
        show amy flirt
        with fade
        "Amy's doing the same thing too, tearing off everything she's wearing."
        "It's no contrived strip-tease, just a rush to get naked as quickly as possible."
        "But it's not like the same thrill isn't there as we strip off."
        show amy topless with dissolve
        "There's no need for Amy to tease me, to work me into a state of arousal."
        "Because that same undercurrent of attraction is more than enough to do it."
        "As I pull down my shorts, my cock bobs up."
        "It's hard and standing to attention."
        "And like me, it's more than ready to have some fun with Amy."
        show amy naked with dissolve
        "For her own part, she turns to face me with a knowing smile."
        "I honestly think this was the part where Amy thought she'd be taking the lead."
        show amy surprised at startle
        "But as soon as she sets eyes on my manhood, her eyes become very wide indeed!"
        mike.say "Are you okay, Amy?"
        mike.say "You look a little surprised!"
        show amy blush
        amy.say "Wh...what?"
        amy.say "Oh...no, I'm fine."
        show amy flirt
        amy.say "Or at least I will be - once I have that thing inside of me!"
    elif rand_intro == 4:
        scene bg bedroom1
        show amy
        with fade
        "As I close my bedroom door and turn to face Amy, I've only got one thing on my mind."
        "And when I'm with a girl as hot as she is, can you really blame me?"
        "Amy seems to be able to sense what I'm thinking too."
        "As when I set eyes on her, she's already starting to get undressed."
        show amy flirt topless
        amy.say "Hey, [hero.name]..."
        amy.say "What are you staring at?"
        mike.say "Oh, I think you know, Amy!"
        show amy blush at startle
        "She giggles and keeps on removing her clothes."
        amy.say "You're so obvious."
        amy.say "Your tongue is hanging out of your mouth."
        show amy naked
        amy.say "So much so it's practically touching the floor!"
        "I start to walk over to where Amy's standing."
        "And at the same time I begin to get undressed too."
        mike.say "Can you really blame me?"
        mike.say "I can't wait to get my hands on you!"
        "By now I'm almost within reach of Amy."
        show amy surprised at center, zoomAt(1.5, (640, 1040)) with vpunch
        "So I make a move to grab hold of her."
        show amy surprised at hshake, center, zoomAt(1.25, (540, 900))
        "But she senses my intentions and ducks out of the way."
        show amy happy at center, zoomAt(1.25, (340, 900)) with ease
        amy.say "Hah!"
        show amy flirt
        amy.say "What if I'm more than you can handle, huh?"
        amy.say "You ever think about that?"
        show amy surprised at center, zoomAt(1.5, (640, 1040)) with vpunch
        "I make another attempt to catch Amy."
        show amy happy at center, zoomAt(1.25, (940, 900)) with ease
        "But she evades me a second time."
        mike.say "Oh, I think I can handle you!"
        show amy flirt at center, zoomAt(1.25, (640, 900)) with ease
        mike.say "But I don't know if you can handle me!"



























































































    $ game.room = "bedroom1"
    return

label amy_fuck_date_foreplay_male:
    menu:
        "Suggest a blowjob" if amy.sub >= 10:
            call amy_fuck_date_blowjob from _call_amy_fuck_date_blowjob
        "Ask for a footjob" if amy.sub >= 25:
            call amy_fuck_date_footjob from _call_amy_fuck_date_footjob
        "Eat her pussy" if hero.sexperience >= 5:
            call amy_fuck_date_cunnilingus from _call_amy_fuck_date_cunnilingus
        "Fuck her right now":
            pass
    call stop_all_sfx from _call_stop_all_sfx_43

    return _return

label amy_fuck_date_choices_male:
    menu:
        "Missionary":
            call amy_fuck_date_missionary (0) from _call_amy_fuck_date_missionary
        "Doggy" if hero.sexperience >= 5:
            call amy_fuck_date_doggy (5) from _call_amy_fuck_date_doggy
        "Cowgirl" if hero.sexperience >= 10:
            call amy_fuck_date_cowgirl (10) from _call_amy_fuck_date_cowgirl
    call stop_all_sfx from _call_stop_all_sfx_44

    return _return

label amy_fuck_date_sleep(location="hero"):
    scene bg bedroom1
    if game.hour > 19 or game.hour < 6:
        show amy naked
        if amy.is_sex_slave:
            amy.say "May I share your bed tonight, Master?"
        else:
            amy.say "Mmm...you cool with me spending the night here?"
        menu:
            "No":
                mike.say "No...I have to be up really early in the morning."
                "The sex was beyond incredible, but now I want to be alone."
                "Amy frowns in disappointment, clearly trying to shrug off the sense of rejection."
                amy.say "Okay...sleep well, I guess."
                "She shakes her head as she collects her things and leaves my bedroom."
                $ amy.love -= 3
                call sleep from _call_sleep_95
            "Yes":
                mike.say "YES...I mean, yes...if you want to!"
                "I try to keep from sounding too desperate and needy, but I'm not sure I manage it."
                show cuddle amy
                "Amy curling up against me beneath the covers is almost as good as the sex - almost..."
                if amy.is_sex_slave:
                    amy.say "Sweet dreams, Master..."
                else:
                    amy.say "Sweet dreams, [hero.name]..."
                mike.say "You too, Amy..."
                $ amy.love += 3
                call sleep ("amy") from _call_sleep_96
    return

label amy_fuck_date_blowjob:
    "Then I watch as Amy slides off the bed."
    "I move at the same time, lowering myself onto it."
    "And so in this odd way we change places without a word."
    scene bg black
    show amy bj naked handjob
    with fade
    "Once she's kneeling on the floor, Amy wastes no time."
    "In fact she seems to move with an almost desperate urgency."
    "So I just lean back and watch."
    "Amy has my cock in her hands and from the look on her face right now, she's happy to have it."
    "Needless to say, I'm already good and hard."
    "Which means I'm ready for what she has in mind."
    "I'm honestly expecting her to put it straight into her mouth."
    "So when she takes hold of her breasts and parts them, it's a surprise."
    show amy bj -handjob with vpunch
    "My mouth is open as Amy clasps my cock between her breasts."
    "So that as she starts to move up and down a moment later, I begin to gasp."
    "She's pushing them together with both hands, squeezing my cock at the same time."
    "And the sensation is pretty hard to put into words!"
    "Soft and yet firm at the same time, totally enveloping my cock."
    "No hand-job could ever feel as good as this!"
    "Amy looks up at me as she massages me with her breasts."
    "And I can see the mischief in her smile as she does so."
    "It's almost impossible to see from my viewpoint."
    "But I can feel that she's slowly working her way downwards."
    "Little by little, the tip of my cock begins to emerge from her cleavage."
    "At first there's no way Amy can reach it with her mouth."
    "So she makes do by casting longing glances down at it."
    "And she underlines her desire for it by slowly licking her lips too."
    "A fraction of an inch at a time, it rises higher."
    "And as soon as it's within reach, Amy leans her head forwards."
    show amy bj down mouthtongue
    "I barely manage to suppress a gasp of anticipation as it happens."
    "But once it does, there's no turning back."
    show amy bj eyesclosed blow
    "Amy treats the head of my cock just like I did her nipple."
    "She employs lips, tongue and teeth as she sees fit."
    "And I never seem to know what's going to come next."
    show amy bj hard eyeslust
    "In my state of confused arousal, I hardly notice what she's doing."
    "So I'm surprised to see that I'm suddenly pretty deep into her mouth!"
    "In fact, Amy's pretty much taking me into her throat!"
    "The deeper she takes me the more intense the sensations become."
    "I have no idea how she's able to do all of this."
    "But I do know that I can't hold on for much longer!"
    menu:
        "Free meal in{b}cum{/b}ing!" if amy.sub >= 20:
            "I have no idea if I could even get my cock out of Amy's mouth right now."
            "So I make the decision to stay exactly where I am until the very end."
            "She seems to pick up on this and doesn't stop what she's doing for an instant."
            "This means that when it happens, Amy's more than ready to handle it."
            show amy bj eyesahegao cum with vpunch
            $ amy.love += 2
            "She lets out a slight gasp as I shoot my load, but then recovers a second later."
            with vpunch
            "Then I collapse onto my back as she swallows every last drop."
            show amy bj up mouthcum -blow -cum
        "Watch out, it's about to explode!":
            "I do all that I can to pull out before the last moment."
            "And luckily for me, Amy seems to realise what I'm trying to do."
            show amy bj eyeslust mouthpleasure -blow
            "In one smooth motion she releases me from her mouth."
            "Then she sits patiently before me, waiting for the inevitable to happen."
            show amy bj eyesclosed mouthtongue cum with vpunch
            $ amy.sub += 1
            "A moment later I shoot my load straight into her face."
            with vpunch
            "Then I collapse onto my back as she licks the cum from her lips."
            show amy bj up eyeslust facecum -cum
    return

label amy_fuck_date_footjob:
    "Amy gives me an enigmatic smile as she walks over to the bed."
    scene bg black
    show amy cunnilingus open naked
    with fade
    "Once there, she lies down on her back, hands under her."
    "Then she looks up at me, as if daring me to come closer."
    "Needless to say, I'm more than a little intrigued."
    "And I want to see exactly what she has in mind."
    "So with a shrug, I walk over and stand in front of her."
    "Amy doesn't have to do much to get me interested."
    "The mere sight of her lying there naked is getting me hard."
    show amy cunnilingus pleasure
    "And when she raises her legs into the air, I can see even more!"
    "For a moment I think that this is going to be her game."
    "To get me so worked up that I do the job myself."
    "But then Amy stretches her feet out towards me."
    "And I can see that she's flexing her toes too."
    "What does she think?"
    "That I'm some kind of foot-fetishist?"
    "Unless..."
    "Is she actually going to..."
    "My questions are answered a moment later."
    show amy cunnilingus footjob
    "Specifically when Amy wraps her toes around the shaft of my cock." with vpunch
    "She is!"
    "She's going too give me a foot-job!"
    "Amy's smiling up at me the whole time, apparently amused by my surprise."
    "And right away I can see that she's got amazingly mobile toes."
    "I mean, they're not freakishly long like a monkey's or anything."
    "But still they move almost like fingers!"
    show amy cunnilingus at startle(0.05,-10)
    "Before I know it, Amy's using them just like she would her hands too."
    "Her toes have hold of the shaft of my cock."
    "And they're working it with incredible dexterity."
    "Sure, it's not as precise or delicate as hands would be."
    show amy cunnilingus at startle(0.05,-10)
    "But it's more than enough to get the job done."
    "It's not just the toes that Amy uses either."
    "The soles of her feet cradle my cock as well."
    "And those are much larger than the palms of her hands."
    show amy cunnilingus at startle(0.05,-10)
    "Which means the sensation of them is that much more intense too!"
    show amy cunnilingus speed with vpunch
    "Her speed seems to be picking up as well."
    "Not that it makes her efforts any less dextrous."
    "Soon it's hard to tell which one of Amy's feet is where."
    show amy cunnilingus at startle(0.05,-10)
    "Because they're moving too fast for me to spot!"
    "And they're totally in control of me too."
    "Amy's got me in the palm of her hand."
    "Or to be more specific, on the sole of her foot!"
    show amy cunnilingus normal
    amy.say "See, [hero.name]..."
    amy.say "I told you!"
    "I nod desperately, unable to do anything else."
    "Amy seems gratified by this."
    show amy cunnilingus at startle(0.05,-10)
    "And I feel her squeeze with her toes, even more intensely than before."
    show amy cunnilingus at startle(0.05,-10)
    "It's like she knows exactly what she's doing and the effect it will have."
    show amy cunnilingus at startle(0.05,-10)
    "Because a moment later I can feel myself starting to lose it."
    show amy cunnilingus orgasm cumshot -speed with vpunch
    "I gasp as I shoot my load, helpless to resist."
    with vpunch
    "Amy keeps right on squeezing the whole time, even as I shoot my load."
    with vpunch
    "The result is that it oozes from between her toes, then runs down her legs."
    $ amy.love += 2
    show amy cunnilingus open normal -footjob -cumshot
    "Only when I'm finished does she let me go, allowing me to flop onto the bed beside her."
    mike.say "Oh fuck..."
    mike.say "Amy..."
    mike.say "What else...can you do...with your feet?"
    show amy cunnilingus pleasure
    amy.say "Just you wait and see, [hero.name]."
    amy.say "Just you wait and see."
    return

label amy_fuck_date_cunnilingus:
    "Amy turns her back on me for a moment."
    "Long enough to climb onto the bed and lay down."
    scene bg black
    show amy cunnilingus open naked
    with fade
    "Then she rolls onto her back, spreading her legs."
    amy.say "Now then..."
    show amy cunnilingus masturbating at startle(0.05,-10)
    amy.say "Eyes down here, if you please!"
    "Amy points a finger between her thighs."
    "And my gaze is drawn down to where I can see her exposed pussy."
    amy.say "I want you to put your mouth to good use for once, okay?"
    amy.say "I want you to get down there and give it all you've got."
    amy.say "And I don't want you to stop until I can't take it anymore!"
    show amy cunnilingus mikelick mikehand pleasure -masturbating at startle(0.05,-10)
    "I'm down on my knees almost before Amy's stopped talking."
    "And my head's between her thighs a second later."
    "I know that she told me to use my mouth."
    "But there's nothing wrong with a little bit of innovation."
    show amy cunnilingus finger fingerin hurt -mikelick at startle(0.05,-10)
    "So I begin by reaching out with my fingers instead."
    amy.say "Hey!"
    amy.say "I thought I told you to..."
    show amy cunnilingus orgasm at startle(0.05,-10)
    amy.say "Urgh..."
    amy.say "Oh god!"
    "I can't help chuckling to myself as Amy feels the first of my efforts."
    "All I'm doing is stroking the edges of her pussy right now."
    "And she's already almost helpless from the effect it's having on her!"
    show amy cunnilingus fingerspeed at startle(0.05,-10)
    "Not waiting for permission, I begin to probe deeper still."
    "It's not only Amy's head that's responding so positively either."
    "I can feel her pussy opening up like a flower as I stroke it."
    "It's almost like I don't have to push my way in at all."
    "As her lips are already opening in anticipation of what I'll do next."
    "By now I'm sure that Amy's into the rhythm of me using my fingers."
    "And so I wait for what feels like the perfect moment."
    "The moment when she's opened herself up to me."
    "And that's when I choose to change things up."
    show amy cunnilingus mikelick tonguemiddle up closeup -finger at startle(0.05,-10)
    "Opening my mouth, I stick out my tongue."
    "And I push it as far into Amy's pussy as I can."
    "The effect is instant and more dramatic than I expected."
    show amy cunnilingus at startle(0.05,-10)
    "Amy begins to buck and twist on the bed, moaning with pleasure."
    "I'm forced to almost hold her in place to be able to keep going."
    "But there's no way I'm going to stop now."
    "Not when I'm making her react like this!"
    "I don't know if I've ever had my tongue this far inside a girl before."
    "Hell, I didn't know I could even stick it out this far either!"
    show amy cunnilingus down at startle(0.05,-10)
    "I try as best I can not to think about it though."
    show amy cunnilingus tonguemiddle
    pause 0.2
    show amy cunnilingus tongueup
    pause 0.2
    show amy cunnilingus tonguedown
    pause 0.2
    show amy cunnilingus tonguemiddle
    pause 0.2
    show amy cunnilingus tongueup
    pause 0.2
    show amy cunnilingus tonguedown
    "Instead I concentrate all of my energy on pleasing Amy."
    show amy cunnilingus orgasm tonguemiddle
    pause 0.15
    show amy cunnilingus tongueup
    pause 0.15
    show amy cunnilingus tonguedown
    pause 0.15
    show amy cunnilingus tonguemiddle
    pause 0.15
    show amy cunnilingus tongueup
    pause 0.15
    show amy cunnilingus tonguedown
    pause 0.15
    show amy cunnilingus tonguemiddle
    pause 0.15
    show amy cunnilingus tongueup
    pause 0.15
    show amy cunnilingus tonguedown
    "To begin with I was pretty sure that I could hold her down."
    "After all, I'm a lot taller and heavier than she is."
    "Plus I have the advantage of being in a better position too."
    show amy cunnilingus holding at startle(0.05,-10)
    "But now she's really starting to move with a strength that's surprising me."
    show amy cunnilingus at startle(0.05,-10)
    "More than once Amy nearly manages to throw me off the bed completely."
    show amy cunnilingus tonguemiddle at startle(0.05,-10)
    pause 0.1
    show amy cunnilingus tongueup
    pause 0.1
    show amy cunnilingus tonguedown
    pause 0.1
    show amy cunnilingus tonguemiddle
    pause 0.1
    show amy cunnilingus tongueup
    pause 0.1
    show amy cunnilingus tonguedown
    pause 0.1
    show amy cunnilingus tonguemiddle
    pause 0.1
    show amy cunnilingus tongueup
    pause 0.1
    show amy cunnilingus tonguedown
    pause 0.1
    show amy cunnilingus up tonguemiddle
    pause 0.1
    show amy cunnilingus tongueup
    pause 0.1
    show amy cunnilingus tonguedown
    pause 0.1
    show amy cunnilingus tonguemiddle
    pause 0.1
    show amy cunnilingus tongueup
    pause 0.1
    show amy cunnilingus tonguedown
    pause 0.1
    show amy cunnilingus tonguemiddle
    pause 0.1
    show amy cunnilingus tongueup
    pause 0.1
    show amy cunnilingus tonguedown
    "And I respond by holding on tighter and probing even deeper."
    "That is until I realise what's really happening."
    show amy cunnilingus at startle(0.05,-10)
    pause 0.3
    show amy cunnilingus at startle(0.05,-10)
    "Amy isn't trying to throw me off - she's about to cum!"
    show amy cunnilingus at startle(0.05,-10)
    pause 0.2
    show amy cunnilingus at startle(0.05,-10)
    "Instead of keeping on fighting, I come up for air."
    show amy cunnilingus up openpussy -mikelick with vpunch
    $ amy.love += 4
    "And I'm still gasping as she finally loses it."
    "Amy wriggles and writhes on the bed, lost in her orgasm."
    "All I can do is sit and watch."
    show amy cunnilingus down ahegao at startle(0.05,-10)
    "While I try to rub some life back into my aching jaw."
    return

label amy_fuck_date_missionary(sexperience_min):
    scene bg black
    show amy missionary lock finger
    with fade
    "Amy's laid on her back and I'm leaning over her."
    "And I like the view so much that I'm not about to let her move an inch!"
    amy.say "What are you waiting for, [hero.name]?"
    show amy missionary openpussy
    amy.say "I'm all yours!"
    "I shake my head, getting myself back into the moment."
    "And then I set my sights on my ultimate goal."
    menu:
        "Fuck her pussy":
            "Amy's pussy is calling to me right now."
            "Like it's impossible to think of anything else."
            "So I decide to go for it."
            call check_condom_usage (amy) from _call_check_condom_usage_124
            if _return == False:
                return "leave_without_gain"
            show amy missionary spread mike
            if CONDOM:
                show amy missionary condom
            "I begin to lower myself down onto Amy."
            "I can already image the sensation of sinking into her."
            if amy.flags.buttplug:
                "But just before I can make it happen, she holds up a hand."
                amy.say "Wait..."
                amy.say "I wondered if..."
                amy.say "If we could use this?"
                "I look down and see that Amy's holding something small and made of rubber."
                "Then my eyes go wide as I realise that it's a butt-plug!"
                menu:
                    "Use the butt-plug":
                        show amy missionary -mike
                        "Taking the plug from Amy, I nod."
                        mike.say "Sure thing, Amy."
                        mike.say "Do I need to..."
                        amy.say "No need for anything fancy, [hero.name]."
                        amy.say "Just push it right in there!"
                        "I nod and then set about doing as I'm told."
                        "Amy must have done this before."
                        "Because her ass only resists for a short time."
                        show amy missionary buttplug pleasure
                        "Then the plug slides into her slowly."
                        "She moans with pleasure as it fills her ass."
                        "The sound of which only makes me more eager be inside of her myself!"
                    "Don't use it":
                        "I shake my head, showing my disapproval."
                        mike.say "No time for that now, Amy."
                        mike.say "I want to get inside of you."
                        mike.say "And I'm not waiting a second longer!"
                        "Amy looks a little disappointed."
                        "But she nods all the same."
                        amy.say "Okay, okay..."
                        amy.say "Maybe next time."
            show amy missionary normal mike
            "Amy has her legs spread so wide that it makes what I have in mind is easy."
            show amy missionary vaginal pleasure
            "Wrapping them around my waist, I manage to almost sit on the back of her thighs."
            "This means that my body is pinning her to the bed, my weight pressing down on her too."
            show amy missionary lock orgasm at startle(0.05,-10)
            "And I don't hesitate to use my position to push my cock home."
            "Amy moans as the head presses against the lips of her pussy."
            "And she nods eagerly, letting me know that she wants it too."
            "I keep right on lowering myself, putting more pressure on her lips."
            "Then suddenly they begin to part for me."
            amy.say "Oh fuck..."
            show amy missionary pleasure
            amy.say "Don't..."
            amy.say "Don't stop!"
            "Like I'd even think of doing that right now!"
            "The sensation of Amy opening up for me is impossible to describe."
            "Even using all of my weigh the progress is achingly slow."
            "And that means the feeling is so much more intense too."
            "So much so that I pause once I can't get any further."
            "The muscles of Amy's pussy are already squeezing me."
            "Massaging the entire length of my cock the whole time."
            "I could stay like this forever, or at least that's how it feels."
            "But the look of urgency in Amy's eyes is more than enough to get me moving."
            "There's a genuine hunger in the way she's looking at me right now."
            "Letting me know how much she wants it."
            "When I finally start to move, I expect her to look relieved."
            "So it comes as something of a shock when that look intensifies."
            "I'm picking up speed with each second that passes."
            "But it seems to be doing nothing to sate Amy's desire."
            "Instead she takes all that I have to give."
            "And the whole time she's nodding her head."
            "Like she's begging for more!"
            "That's when I start to bring my weight into it."
            "I already have Amy almost folded in two."
            "So I don't hesitate to press my entire body downwards."
            "Each thrust I make has all the force I can muster behind it."
            "And it's not like I slow down at all either."
            "So I'm going harder and faster with each passing second."
            "Finally I begin to see a change in Amy's expression."
            "The need seems to be ebbing out of her a little at a time."
            "In fact, her eyes are starting to almost glaze over."
            show amy missionary orgasm
            "At the same time Amy's mouth opens ever wider."
            "And it doesn't take long for her tongue to start hanging out too!"
            "I think...I think I finally did it."
            "Amy's actually starting to cum!"
            "But the effort that it took means I'm about to lost it too."
            call cum_reaction (amy, 'vaginal', sexperience_min) from _call_cum_reaction_227
            if _return == "vaginal_outside":
                "I almost forget to pull out before it happens."
                "And even though I do, it's hard to manage."
                "All of my weight is leaning forwards, pushing down."
                "So I have to all but roll off of Amy and onto the bed."
                show amy missionary spread out
                "Just in time my cock pops out of her."
                show amy missionary cum with hpunch
                if CONDOM:
                    "And I shoot my load."
                else:
                    $ amy.love += 1
                    show amy missionary bodycum with hpunch
                    "And I shoot my load over her thighs."
            elif _return == "vaginal_condom":
                "I'm glad we remembered to use a condom."
                with vpunch
                "Because it means I can keep on until the end."
                with vpunch
                "And I don't let up until it happens either."
                with vpunch
                "Only when I shoot my load do I let myself stop."
                show amy missionary spread
                "Falling sideways and hitting the mattress beside Amy."
            elif _return == "vaginal_inside_pregnant":
                "I've been making sure Amy's belly was safe this whole time."
                "And now it serves as a reminder of the fact I don't need to pull out."
                "It means I can keep on until the end."
                with vpunch
                "And I don't let up until it happens either."
                $ amy.love += 2
                show amy missionary cum ahegao with vpunch
                "Only when I shoot my load do I let myself stop."
                show amy missionary spread
                "Falling sideways and hitting the mattress beside Amy."
            elif _return == "vaginal_inside_pill":
                amy.say "Don't stop..."
                amy.say "I'm on the pill!"
                "I silently thank Amy for the reminder that I don't need to pull out."
                "It means I can keep on until the end."
                with vpunch
                "And I don't let up until it happens either."
                $ amy.love += 2
                show amy missionary cum ahegao with vpunch
                "Only when I shoot my load do I let myself stop."
                show amy missionary spread
                "Falling sideways and hitting the mattress beside Amy."
            elif _return == "vaginal_inside_happy":
                amy.say "Don't stop..."
                amy.say "I don't want you to stop!"
                "Amy's demands catch me off-guard."
                with vpunch
                "And they mean I'm not concentrating when it happens."
                $ amy.love += 5
                $ amy.impregnate()
                show amy missionary cum ahegao with vpunch
                "Only when I shoot my load do I realise what just happened."
                show amy missionary spread orgasm
                "I roll off of her, already afraid of the consequences."
                "But from what I can tell, Amy seems to be delighted!"
            elif _return == "vaginal_inside_mad":
                show amy missionary hurt
                amy.say "Stop!"
                amy.say "You can't cum in me!"
                "Amy's demands catch me off-guard."
                with vpunch
                "And they mean I'm not concentrating when it happens."
                $ amy.impregnate()
                show amy missionary cum ahegao with vpunch
                "Only when I shoot my load do I realise what just happened."
                show amy missionary spread orgasm
                "I roll off of her, already afraid of the consequences."
                $ amy.love -= 5
                show amy missionary hurt
                "And I can already hear Amy cursing me too."
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "Amy's ass is calling to me right now."
            "Like it's impossible to think of anything else."
            "So I decide to go for it."
            show amy missionary spread mike
            "I begin to lower myself down onto Amy."
            "I can already image the sensation of sinking into her."
            "Amy has her legs spread so wide that it makes what I have in mind is easy."
            show amy missionary anal pleasure
            "Wrapping them around my waist, I manage to almost sit on the back of her thighs."
            "This means that my body is pinning her to the bed, my weight pressing down on her too."
            show amy missionary lock orgasm at startle(0.05,-10)
            "And I don't hesitate to use my position to push my cock home."
            "Amy moans as the head presses between the cheeks of her ass."
            "And she nods eagerly, letting me know that she wants it too."
            "I keep right on lowering myself, putting more pressure on her hole."
            "Then suddenly they begin to part for me."
            amy.say "Oh fuck..."
            show amy missionary pleasure
            amy.say "Don't..."
            amy.say "Don't stop!"
            "Like I'd even think of doing that right now!"
            "The sensation of Amy opening up for me is impossible to describe."
            "Even using all of my weigh the progress is achingly slow."
            "And that means the feeling is so much more intense too."
            "So much so that I pause once I can't get any further."
            "The muscles of Amy's ass are already squeezing me."
            "Massaging the entire length of my cock the whole time."
            "I could stay like this forever, or at least that's how it feels."
            "But the look of urgency in Amy's eyes is more than enough to get me moving."
            "There's a genuine hunger in the way she's looking at me right now."
            "Letting me know how much she wants it."
            "When I finally start to move, I expect her to look relieved."
            "So it comes as something of a shock when that look intensifies."
            "I'm picking up speed with each second that passes."
            "But it seems to be doing nothing to sate Amy's desire."
            "Instead she takes all that I have to give."
            "And the whole time she's nodding her head."
            "Like she's begging for more!"
            "That's when I start to bring my weight into it."
            "I already have Amy almost folded in two."
            "So I don't hesitate to press my entire body downwards."
            "Each thrust I make has all the force I can muster behind it."
            "And it's not like I slow down at all either."
            "So I'm going harder and faster with each passing second."
            "Finally I begin to see a change in Amy's expression."
            "The need seems to be ebbing out of her a little at a time."
            "In fact, her eyes are starting to almost glaze over."
            show amy missionary orgasm
            "At the same time Amy's mouth opens ever wider."
            "And it doesn't take long for her tongue to start hanging out too!"
            "I think...I think I finally did it."
            "Amy's actually starting to cum!"
            "But the effort that it took means I'm about to lost it too."
            call cum_reaction (amy, 'anal', sexperience_min) from _call_cum_reaction_228
            if _return == 'anal_inside':
                "I'm glad I chose to fuck Amy's ass over her pussy."
                "Because it means I can keep on until the end."
                with vpunch
                "And I don't let up until it happens either."
                $ amy.sub += 2
                show amy missionary cum ahegao with vpunch
                "Only when I shoot my load do I let myself stop."
                show amy missionary spread
                "Falling sideways and hitting the mattress beside Amy."
            elif _return == 'anal_outside':
                "I could keep right on going, but I feel the need to pull out instead."
                "Even though it's what I want to do, it's hard to manage."
                "All of my weight is leaning forwards, pushing down."
                "So I have to all but roll off of Amy and onto the bed."
                show amy missionary spread out with vpunch
                "Just in time my cock pops out of her."
                $ amy.sub += 1
                show amy missionary cum bodycum with hpunch
                "And I shoot my load over her thighs."
    return

label amy_fuck_date_doggy(sexperience_min):
    scene bg black
    show amy doggy nomc
    with fade
    "Amy climbs onto the bed."
    "And she looks back over her shoulder at me."
    "Which is an invitation that I can't mistake."
    "So I hurry to clamber up there after her."
    menu:
        "Fuck her pussy":
            "I feel like I've been waiting for this moment all night."
            "Like everything's been building up to it since the very beginning."
            "All I can think about is the sweet spot between Amy's thighs."
            show amy doggy -nomc
            call check_condom_usage (amy) from _call_check_condom_usage_125
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show amy doggy condom
            call amy_fuck_doggy_ask_accessories from _call_amy_fuck_doggy_ask_accessories
            if BEADS:
                "Though it doesn't take me long to see the problem here."
                if PLUG:
                    "Amy's gone and filled up all the holes on offer!"
                else:
                    "Amy's gone and filled up the hole I'm interested in!"
                "Not only that, she's told me not to pull anything out until she cums!"
                "Which I guess means that I'm going to have to improvise."
                "With that in mind, I reach down between her thighs."
                show amy doggy finger -nomc
                "My fingers find the folds of her pussy."
                "Then I start to stroke and tickle with my fingertips."
                show amy doggy pleasure fingerup
                pause 0.25
                show amy doggy fingerdown
                pause 0.25
                show amy doggy fingerup
                pause 0.25
                show amy doggy fingerdown
                "Almost instantly, Amy starts to moan with pleasure."
                "But I don't take it slowly or build it gradually."
                show amy doggy fingerup
                pause 0.2
                show amy doggy fingerdown
                pause 0.2
                show amy doggy fingerup
                pause 0.2
                show amy doggy fingerdown
                pause 0.2
                show amy doggy fingerup
                pause 0.2
                show amy doggy fingerdown
                "Instead I work her as fast and intensely as I can."
                "Using all the tricks I know, I try to make Amy cum."
                "Because she never said I could only do it once."
                "Or which orgasm meant I could pull something out of her."
                "Pretty soon it's obvious Amy can't hold on any longer."
                show amy doggy fingerup
                pause 0.1
                show amy doggy fingerdown
                pause 0.1
                show amy doggy fingerup
                pause 0.1
                show amy doggy fingerdown
                pause 0.1
                show amy doggy fingerup
                pause 0.1
                show amy doggy fingerdown
                pause 0.1
                show amy doggy fingerup
                pause 0.1
                show amy doggy fingerdown
                pause 0.1
                show amy doggy fingerup
                pause 0.1
                show amy doggy fingerdown
                "She's tossing her head around and almost grunting."
                "So I take hold of the cord and pull the beads out of her."
                show amy doggy nomc lookup pleasure beads2 squirt
                pause 0.1
                show amy doggy beads3
                pause 0.1
                show amy doggy beads4
                pause 0.1
                show amy doggy beads5
                pause 0.1
                show amy doggy ahegao beads6
                amy.say "Ah..."
                amy.say "Oh...oh fuck!"
                show amy doggy lookdown pleasure -beads -squirt
            show amy doggy normal -nomc -finger
            "My hands have a good grip on Amy's waist."
            "And I take advantage of that by pulling her backwards."
            "She yelps in surprise."
            show amy doggy pleasure vaginal
            "But a second later, that sound becomes a moan of pleasure."
            "Because I can feel the head of my cock pressing home."
            "And the lips of her pussy are already beginning to part."
            show amy doggy normal
            "I only tease Amy for the shortest amount of time."
            "Because that's all that she needs to let me inside."
            "Within what feels like mere seconds, I feel her opening up."
            "And once that happens, I waste no time in taking advantage."
            show amy doggy lookup trust
            "Amy moans for a second time as I slide into her."
            "I make a point of not stopping until I'm all the way inside."
            show amy doggy lookdown pleasure
            "And when I can't go any further, I pause for a moment."
            "The sensations that I'm feeling are enough in of themselves."
            "But the feeling of Amy moving around me is something else."
            "Her muscles are clenching and quivering around my cock."
            "Letting me know that she's almost helpless right now."
            "And those movements only become more intense as I begin to move."
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            "My plan had been to start of slowly and build up my speed."
            "But within seconds I can see that Amy's too desperate for that."
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            pause 0.2
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            "She's already panting and gasping, slamming her ass backwards into me!"
            "Without a conscious thought, I do all that I can to match her pace."
            "And before I know it, I'm thrusting into Amy for all I'm worth."
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            pause 0.2
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            "This sends her body rocking back and forth from the motion."
            "I can see her breasts swaying in sympathy too."
            "They move in a hypnotic pattern, my eyes following their every move."
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            pause 0.2
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            amy.say "Oh fuck..."
            amy.say "I'm gonna cum!"
            call cum_reaction (amy, 'vaginal', sexperience_min) from _call_cum_reaction_229
            if _return == "vaginal_outside":
                show amy doggy -trust
                pause 0.1
                show amy doggy trust speed up with hpunch
                pause 0.1
                show amy doggy -speed down
                "I just have time to pull myself out of Amy before I lose it."
                "And as I do so, her arms and legs seem to lose their ability to support her."
                show amy doggy out ease cum openpussy with hpunch
                if not CONDOM:
                    $ amy.love += 1
                    "Amy collapses onto the bed as I shoot my load over her."
                    show amy doggy normal nomc screencum -cum with hpunch
                    "Which means that I paint white, sticky stripes across her thighs and ass."
                else:
                    "Amy collapses onto the bed as I shoot my load."
            elif _return == "vaginal_condom":
                "Remembering the condom means that there's no danger in going all the way."
                "And that's just what I do, holding Amy up as I make one that thrust into her."
                show amy doggy -trust
                pause 0.1
                show amy doggy trust speed up with hpunch
                pause 0.1
                show amy doggy cum down -speed with hpunch
                "Amy's arms and legs wobble, then they give out and she collapses onto the bed."
            elif _return == "vaginal_inside_pregnant":
                show amy doggy normal
                amy.say "Don't stop..."
                show amy doggy -trust
                pause 0.1
                show amy doggy trust speed up with hpunch
                pause 0.1
                show amy doggy -speed down
                amy.say "I'm pregnant - remember?!?"
                "Amy being pregnant means that there's no danger in going all the way."
                "And that's just what I do, holding Amy up as I make one that thrust into her."
                show amy doggy ahegao -trust
                pause 0.1
                show amy doggy trust speed up with hpunch
                pause 0.1
                show amy doggy cum down -speed with hpunch
                $ amy.love += 2
                "Amy's arms and legs wobble, then they give out and she collapses onto the bed."
                show amy doggy pleasure nomc openpussy screencum with hpunch
                "My cock slides out of her at the same time, bobbing over her ass."
            elif _return == "vaginal_inside_pill":
                show amy doggy normal
                amy.say "Don't stop..."
                show amy doggy pleasure -trust
                pause 0.1
                show amy doggy trust speed up with hpunch
                pause 0.1
                show amy doggy -speed down
                amy.say "I'm on the pill!"
                "Amy being on the pill means that there's no danger in going all the way."
                "And that's just what I do, holding Amy up as I make one that thrust into her."
                show amy doggy ahegao -trust
                pause 0.1
                show amy doggy trust speed up with hpunch
                pause 0.1
                show amy doggy cum down -speed with hpunch
                $ amy.love += 2
                "Amy's arms and legs wobble, then they give out and she collapses onto the bed."
                show amy doggy pleasure nomc openpussy screencum with hpunch
                "My cock slides out of her at the same time, bobbing over her ass."
            elif _return == "vaginal_inside_happy":
                show amy doggy normal
                amy.say "Don't stop..."
                show amy doggy pleasure -trust
                pause 0.1
                show amy doggy trust speed up with hpunch
                pause 0.1
                show amy doggy -speed down
                amy.say "Don't you dare stop!"
                "Amy's demands comes out of nowhere."
                "And it means that's just what I do, holding Amy up as I make one that thrust into her."
                show amy doggy ahegao -trust
                pause 0.1
                show amy doggy trust speed up with hpunch
                pause 0.1
                show amy doggy cum down -speed with hpunch
                $ amy.love += 5
                $ amy.impregnate()
                "Amy's arms and legs wobble, then they give out and she collapses onto the bed."
                show amy doggy pleasure nomc openpussy screencum with hpunch
                "My cock slides out of her at the same time, bobbing over her ass."
                "I can hear her chuckling with delight."
                "But I'm already filled with dread."
            elif _return == "vaginal_inside_mad":
                amy.say "Stop..."
                show amy doggy -trust
                pause 0.1
                show amy doggy trust speed up with hpunch
                pause 0.1
                show amy doggy -speed down
                amy.say "Don't you dare..."
                show amy doggy -trust
                pause 0.1
                show amy doggy trust speed up with hpunch
                pause 0.1
                show amy doggy -speed down normal
                amy.say "Don't cum in me!"
                "Amy's demands comes out of nowhere."
                "But the irony is that it means that's the opposite of what I do."
                "Holding Amy up as I make one that thrust into her, I shoot my load."
                show amy doggy ahegao -trust
                pause 0.1
                show amy doggy trust speed up with hpunch
                pause 0.1
                show amy doggy cum down -speed with hpunch
                $ amy.love -= 5
                $ amy.impregnate()
                "Amy's arms and legs wobble, then they give out and she collapses onto the bed."
                show amy doggy normal nomc openpussy screencum with hpunch
                "My cock slides out of her at the same time, bobbing over her ass."
                "I can hear her moaning as she shakes her head in disbelief."
                "But I'm already filled with dread."
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "I feel like I've been waiting for this moment all night."
            "Like everything's been building up to it since the very beginning."
            "All I can think about is the sweet spot between her thighs."
            show amy doggy normal -nomc
            "My hands have a good grip on Amy's waist."
            "And I take advantage of that by pulling her backwards."
            "She yelps in surprise."
            show amy doggy pleasure vaginal
            "But a second later, that sound becomes a moan of pleasure."
            "Because I can feel the head of my cock pressing home."
            "Right up until the last moment I'm aiming for her pussy."
            "But then something just clicks inside of my head."
            "And I find myself aiming for the other hole instead."
            show amy doggy anal normal
            amy.say "Oh..."
            amy.say "What are you..."
            amy.say "I never saw that coming!"
            "The muscles of her ass are already beginning to relax."
            "I only tease Amy for the shortest amount of time."
            "Because that's all that she needs to let me inside."
            "Within what feels like mere seconds, I feel her opening up."
            "And once that happens, I waste no time in taking advantage."
            show amy doggy lookup trust
            "Amy moans for a second time as I slide into her."
            "I make a point of not stopping until I'm all the way inside."
            show amy doggy lookdown pleasure
            "And when I can't go any further, I pause for a moment."
            "The sensations that I'm feeling are enough in of themselves."
            "But the feeling of Amy moving around me is something else."
            "Her muscles are clenching and quivering around my cock."
            "Letting me know that she's almost helpless right now."
            "And those movements only become more intense as I begin to move."
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            "My plan had been to start of slowly and build up my speed."
            "But within seconds I can see that Amy's too desperate for that."
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            pause 0.2
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            "And it's partially responsible for me trying to speed things up."
            "She's already panting and gasping, slamming her ass backwards into me!"
            "Without a conscious thought, I do all that I can to match her pace."
            "And before I know it, I'm thrusting into Amy for all I'm worth."
            show amy doggy lookup -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            pause 0.2
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            "This sends her body rocking back and forth from the motion."
            "I can see her breasts swaying in sympathy too."
            amy.say "Oh fuck..."
            show amy doggy lookdown
            amy.say "I'm gonna cum!"
            call cum_reaction (amy, 'anal', sexperience_min) from _call_cum_reaction_230
            if _return == "anal_inside":
                "Taking Amy up the ass means that there's no danger in going all the way."
                "And that's just what I do, holding Amy up as I make one that thrust into her."
                show amy doggy -trust
                pause 0.1
                show amy doggy ahegao trust speed up with hpunch
                pause 0.1
                show amy doggy ease cum down -speed with hpunch
                $ amy.sub += 2
                "Amy's arms and legs wobble, then they give out and she collapses onto the bed."
                show amy doggy pleasure nomc -anal assgap screencum -cum with hpunch
                "My cock slides out of her at the same time, bobbing over her ass."
            elif _return == "anal_outside":
                show amy doggy -trust
                pause 0.1
                show amy doggy trust speed up with hpunch
                pause 0.1
                show amy doggy -speed down
                "I just have time to pull myself out of Amy before I lose it."
                "And as I do so, her arms and legs seem to lose their ability to support her."
                show amy doggy out ease cum with hpunch
                $ amy.sub += 1
                "Amy collapses onto the bed as I shoot my load over her."
                show amy doggy pleasure nomc -anal assgap screencum -cum with hpunch
                "Which means that I paint white, sticky stripes across her thighs and ass."
    return

label amy_fuck_date_cowgirl(sexperience_min):
    scene bg black
    show amy cowgirl with fade
    "Amy pushes me gently down onto my back."
    amy.say "So..."
    amy.say "You like the view?"
    amy.say "You like what you see?"
    "I'm staring up at Amy's body as she asks me this."
    "So what else can I do but nod in agreement."
    mike.say "Oh yeah, Amy..."
    mike.say "I love it!"
    "Amy nods as she hovers over me."
    amy.say "Then I guess you'd better stay right where you are."
    amy.say "That way you can get a real good view the whole time."
    "Again there's no way I'm going to argue as Amy straddles me."
    "I sigh as the weight of her body presses down on mine."
    "And then I gasp as I feel her reach out and grab hold of my cock."
    amy.say "You'd better understand one thing though..."
    amy.say "I'm not going to let you just lie back and enjoy the view!"
    "Amy squeezes my cock to underline her point."
    "Which makes me wince at the sensation, and nod eagerly."
    amy.say "Well then?"
    amy.say "What are you waiting for?"
    menu:
        "Fuck her pussy":
            "Amy's question has an instant effect on me."
            "For the first time my hands reach out."
            "And I find myself taking the lead."
            call check_condom_usage (amy) from _call_check_condom_usage_126
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show amy cowgirl condom
            show amy cowgirl mikehand
            "My hands firmly gripping Amy's waist, I begin to pull her downwards."
            "She doesn't resist for a moment, letting me guide her where I desire."
            show amy cowgirl vaginal pleasure
            "I watch as she reacts to the head of my cock touching the lips of her pussy."
            "Amy gasps as it runs along their length, then bites her lip as it stops."
            "And that's because I seem to have found the perfect spot to apply more pressure."
            "The muscles down there have begun to surrender just a little."
            "Just enough for the tip of my cock to catch and begin to make progress."
            amy.say "Mmm..."
            amy.say "Oh...oh fuck..."
            mike.say "How does that feel, Amy?"
            mike.say "You like that, huh?"
            "Amy doesn't seem to be able to summon the words to answer me."
            show amy cowgirl normal
            "Instead she nods her head desperately, almost begging for more."
            "And in answer I pull her downwards again."
            "But this time I do it with considerably more force."
            "It's more than enough to take advantage of the way Amy's body is surrendering."
            show amy cowgirl down pleasure
            "I feel my cock begin to sink into her, slowly at first and the with greater speed."
            "Amy sits down at the same time, ensuring that I get as deep into her as possible."
            "But I only let her relax for a few moments, just long enough for me to savour the sensation."
            "Then I strengthen my grip on her."
            "And I begin to move in earnest."
            show amy cowgirl up
            pause 0.45
            show amy cowgirl down at startle(0.05,-10)
            pause 0.45
            show amy cowgirl up
            pause 0.45
            show amy cowgirl down at startle(0.05,-10)
            pause 0.45
            show amy cowgirl up
            pause 0.45
            show amy cowgirl down at startle(0.05,-10)
            "Finally I can feel the balance of power between us start to shift as I do so."
            "I'm not trying to dominate Amy in any negative sense, just to steer what we're doing."
            "And she seems to sense that, surrendering to me and letting herself be taken for the ride."
            show amy cowgirl normal
            "Soon enough she's happy to allow her movements to be guided by my hands."
            show amy cowgirl up
            pause 0.45
            show amy cowgirl down at startle(0.05,-10)
            pause 0.45
            show amy cowgirl up
            pause 0.45
            show amy cowgirl down at startle(0.05,-10)
            pause 0.45
            show amy cowgirl up
            pause 0.45
            show amy cowgirl down at startle(0.05,-10)
            "Her entire body is rising and falling in sympathy with mine."
            "The reason for that can only be the way that I'm moving inside of her."
            "All of the passion and desire that Amy inspired in me is being realised."
            "And it's being translated straight into what she's feeling too."
            "My speed is only increasing, the depth of my thrusts likewise."
            show amy cowgirl up pleasure
            pause 0.35
            show amy cowgirl down speed at startle(0.05,-10)
            pause 0.35
            show amy cowgirl up
            pause 0.35
            show amy cowgirl down at startle(0.05,-10)
            pause 0.35
            show amy cowgirl up
            pause 0.35
            show amy cowgirl down -speed at startle(0.05,-10)
            "As this happens, Amy bounces up and down atop me the whole time."
            "And when I say bounces, I really mean it too!"
            "Her buttocks are squashed against my own thighs."
            "Her head is bobbing around like she's a Jack-in-the-Box."
            "And her breasts are moving like they have a life of their own!"
            show amy cowgirl up
            pause 0.35
            show amy cowgirl down speed at startle(0.05,-10)
            pause 0.35
            show amy cowgirl up
            pause 0.35
            show amy cowgirl down at startle(0.05,-10)
            pause 0.35
            show amy cowgirl up
            pause 0.35
            show amy cowgirl down -speed at startle(0.05,-10)
            "Swinging, swaying and slapping together, they almost totally fill my view."
            "At times I can only see Amy's face in fleeting glimpses."
            "And part of me is curious as to what it would be like to be caught between them."
            "Probably a lot like being slapped hard across the face!"
            show amy cowgirl up
            pause 0.25
            show amy cowgirl down speed at startle(0.05,-10)
            pause 0.25
            show amy cowgirl up
            pause 0.25
            show amy cowgirl down -speed at startle(0.05,-10)
            "There seems to be no sign of them slowing down either."
            "Instead the speed with which they're moving only increases."
            "In fact Amy seems to be going at an alarming pace."
            "Which must mean that she's building up to a climax!"
            show amy cowgirl up
            pause 0.25
            show amy cowgirl down speed at startle(0.05,-10)
            pause 0.25
            show amy cowgirl up
            pause 0.25
            show amy cowgirl down -speed at startle(0.05,-10)
            amy.say "Oh god..."
            show amy cowgirl up
            pause 0.25
            show amy cowgirl down speed at startle(0.05,-10)
            pause 0.25
            show amy cowgirl up
            pause 0.25
            show amy cowgirl down -speed at startle(0.05,-10)
            amy.say "Here it comes!"
            call cum_reaction (amy, 'vaginal', sexperience_min) from _call_cum_reaction_231
            if _return == "vaginal_outside":
                "Amy's timely warning gives me the chance to pull out before the end."
                "And the act of doing so only seems to make it all the more intense for her too."
                "Amy moans and quivers as her orgasm takes hold."
                show amy cowgirl up speed
                pause 0.15
                show amy cowgirl down ahegao at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up out -speed
                pause 0.5
                show amy cowgirl cum with vpunch
                pause 0.75
                show amy cowgirl pleasure
                if not CONDOM:
                    show amy cowgirl bodycum -cum with vpunch
                    $ amy.love += 1
                "At the same time I feel myself letting go too."
                with vpunch
                "Shooting my load up and over her belly."
            elif _return == "vaginal_condom":
                "Luckily for me we remembered to use a condom."
                "And so I can keep right on going until the very last moment."
                "When it comes, I put all of my effort into one final push."
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down speed at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down ahegao cum -speed with vpunch
                pause 0.35
                show amy cowgirl up
                pause 0.35
                show amy cowgirl down with vpunch
                pause 0.5
                show amy cowgirl up
                pause 0.5
                show amy cowgirl down with vpunch
                pause 0.75
                show amy cowgirl up
                "Which means that I cum a few moments after Amy."
                show amy cowgirl down pleasure at startle
                "Releasing my own energies and adding to the intensity of her own."
            elif _return == "vaginal_inside_pregnant":
                amy.say "Don't stop..."
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down speed at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down at startle(0.05,-10)
                amy.say "I'm pregnant - remember?!?"
                "Amy's timely warning gives me the permission I needed."
                "And so I can keep right on going until the very last moment."
                "When it comes, I put all of my effort into one final push."
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down speed at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down ahegao cum -speed with vpunch
                $ amy.love += 2
                pause 0.35
                show amy cowgirl up
                pause 0.35
                show amy cowgirl down with vpunch
                pause 0.5
                show amy cowgirl up
                pause 0.5
                show amy cowgirl down with vpunch
                pause 0.75
                show amy cowgirl up
                "Which means that I cum a few moments after Amy."
                show amy cowgirl down pleasure at startle
                "Releasing my own energies and adding to the intensity of her own."
            elif _return == "vaginal_inside_pill":
                amy.say "Don't stop..."
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down speed at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down at startle(0.05,-10)
                amy.say "I'm on the pill!"
                "Amy's timely warning gives me the permission I needed."
                "And so I can keep right on going until the very last moment."
                "When it comes, I put all of my effort into one final push."
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down speed at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down ahegao cum -speed with vpunch
                $ amy.love += 2
                pause 0.35
                show amy cowgirl up
                pause 0.35
                show amy cowgirl down with vpunch
                pause 0.5
                show amy cowgirl up
                pause 0.5
                show amy cowgirl down with vpunch
                pause 0.75
                show amy cowgirl up
                "Which means that I cum a few moments after Amy."
                show amy cowgirl down pleasure at startle
                "Releasing my own energies and adding to the intensity of her own."
            elif _return == "vaginal_inside_happy":
                amy.say "Don't stop..."
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down speed at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down at startle(0.05,-10)
                amy.say "Don't you dare stop!"
                show amy cowgirl up normal
                pause 0.15
                show amy cowgirl down speed at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down at startle(0.05,-10)
                "Amy's demands catch me totally off-guard."
                "Which means that I'm not paying attention at the end."
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down speed at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down ahegao cum -speed with vpunch
                $ amy.love += 5
                $ amy.impregnate()
                pause 0.35
                show amy cowgirl up
                pause 0.35
                show amy cowgirl down with vpunch
                pause 0.5
                show amy cowgirl up
                pause 0.5
                show amy cowgirl down with vpunch
                pause 0.75
                show amy cowgirl up
                "And as a result, I shoot my load deep inside of her."
                show amy cowgirl down pleasure at startle
                "She moans and smiles, seemingly happy with this outcome."
                "But what just happened is already filling me with dread."
            elif _return == "vaginal_inside_mad":
                amy.say "Stop..."
                amy.say "Don't you dare..."
                show amy cowgirl hurt
                amy.say "Don't cum in me!"
                "Amy's demands catch me totally off-guard."
                "Which means that I'm not paying attention at the end."
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down speed at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down ahegao cum -speed with vpunch
                $ amy.love -= 5
                $ amy.impregnate()
                pause 0.35
                show amy cowgirl up
                pause 0.35
                show amy cowgirl down with vpunch
                pause 0.5
                show amy cowgirl up
                pause 0.5
                show amy cowgirl down with vpunch
                pause 0.75
                show amy cowgirl up
                "And as a result, I shoot my load deep inside of her."
                show amy cowgirl down hurt at startle
                "She moans and looks horrified."
                "And what just happened is already filling me with dread."
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "Amy's question has an instant effect on me."
            show amy cowgirl mikehand
            "For the first time my hands reach out."
            "And I find myself taking the lead."
            "My hands firmly gripping Amy's waist, I begin to pull her downwards."
            "She doesn't resist for a moment, letting me guide her where I desire."
            show amy cowgirl anal pleasure
            "I watch as she reacts to the head of my cock pushing between her buttocks."
            "Amy gasps as it begins to sink into her ass."
            "And that's because I seem to have found the perfect spot to apply more pressure."
            "The muscles down there have begun to surrender just a little."
            "Just enough for the tip of my cock to catch and begin to make progress."
            amy.say "Mmm..."
            amy.say "Oh...oh fuck..."
            mike.say "How does that feel, Amy?"
            mike.say "You like that, huh?"
            "Amy doesn't seem to be able to summon the words to answer me."
            show amy cowgirl normal
            "Instead she nods her head desperately, almost begging for more."
            "And in answer I pull her downwards again."
            "But this time I do it with considerably more force."
            "It's more than enough to take advantage of the way Amy's body is surrendering."
            show amy cowgirl down pleasure
            "I feel my cock begin to sink into her, slowly at first and the with greater speed."
            "Amy sits down at the same time, ensuring that I get as deep into her as possible."
            "But I only let her relax for a few moments, just long enough for me to savour the sensation."
            "Then I strengthen my grip on her."
            "And I begin to move in earnest."
            show amy cowgirl up
            pause 0.45
            show amy cowgirl down at startle(0.05,-10)
            pause 0.45
            show amy cowgirl up
            pause 0.45
            show amy cowgirl down at startle(0.05,-10)
            pause 0.45
            show amy cowgirl up
            pause 0.45
            show amy cowgirl down at startle(0.05,-10)
            "Finally I can feel the balance of power between us start to shift as I do so."
            "I'm not trying to dominate Amy in any negative sense, just to steer what we're doing."
            "And she seems to sense that, surrendering to me and letting herself be taken for the ride."
            "Soon enough she's happy to allow her movements to be guided by my hands."
            show amy cowgirl up
            pause 0.45
            show amy cowgirl down at startle(0.05,-10)
            pause 0.45
            show amy cowgirl up
            pause 0.45
            show amy cowgirl down at startle(0.05,-10)
            pause 0.45
            show amy cowgirl up
            pause 0.45
            show amy cowgirl down at startle(0.05,-10)
            "Her entire body is rising and falling in sympathy with mine."
            "The reason for that can only be the way that I'm moving inside of her."
            "All of the passion and desire that Amy inspired in me is being realised."
            "And it's being translated straight into what she's feeling too."
            "My speed is only increasing, the depth of my thrusts likewise."
            show amy cowgirl up pleasure
            pause 0.35
            show amy cowgirl down speed at startle(0.05,-10)
            pause 0.35
            show amy cowgirl up
            pause 0.35
            show amy cowgirl down at startle(0.05,-10)
            pause 0.35
            show amy cowgirl up
            pause 0.35
            show amy cowgirl down -speed at startle(0.05,-10)
            "As this happens, Amy bounces up and down atop me the whole time."
            "And when I say bounces, I really mean it too!"
            "Her buttocks are squashed against my own thighs."
            "Her head is bobbing around like she's a Jack-in-the-Box."
            "And her breasts are moving like they have a life of their own!"
            show amy cowgirl up
            pause 0.35
            show amy cowgirl down speed at startle(0.05,-10)
            pause 0.35
            show amy cowgirl up
            pause 0.35
            show amy cowgirl down at startle(0.05,-10)
            pause 0.35
            show amy cowgirl up
            pause 0.35
            show amy cowgirl down -speed at startle(0.05,-10)
            "Swinging, swaying and slapping together, they almost totally fill my view."
            "At times I can only see Amy's face in fleeting glimpses."
            "And part of me is curious as to what it would be like to be caught between them."
            "Probably a lot like being slapped hard across the face!"
            show amy cowgirl up
            pause 0.25
            show amy cowgirl down speed at startle(0.05,-10)
            pause 0.25
            show amy cowgirl up
            pause 0.25
            show amy cowgirl down -speed at startle(0.05,-10)
            "There seems to be no sign of them slowing down either."
            "Instead the speed with which they're moving only increases."
            "In fact Amy seems to be going at an alarming pace."
            "Which must mean that she's building up to a climax!"
            "Which must mean that she's building up to a climax!"
            show amy cowgirl up
            pause 0.25
            show amy cowgirl down speed at startle(0.05,-10)
            pause 0.25
            show amy cowgirl up
            pause 0.25
            show amy cowgirl down -speed at startle(0.05,-10)
            amy.say "Oh god..."
            show amy cowgirl up
            pause 0.25
            show amy cowgirl down speed at startle(0.05,-10)
            pause 0.25
            show amy cowgirl up
            pause 0.25
            show amy cowgirl down -speed at startle(0.05,-10)
            amy.say "Here it comes!"
            call cum_reaction (amy, 'anal', sexperience_min) from _call_cum_reaction_232
            if _return == 'anal_inside':
                "Luckily for me I chose to take Amy up the ass."
                "And so I can keep right on going until the very last moment."
                "When it comes, I put all of my effort into one final push."
                show amy cowgirl up speed
                pause 0.15
                show amy cowgirl down at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down ahegao cum -speed with vpunch
                $ amy.sub += 2
                pause 0.35
                show amy cowgirl up
                pause 0.35
                show amy cowgirl down with vpunch
                pause 0.5
                show amy cowgirl up
                pause 0.5
                show amy cowgirl down with vpunch
                pause 0.75
                show amy cowgirl up
                "Which means that I cum a few moments after Amy."
                show amy cowgirl down pleasure at startle
                "Releasing my own energies and adding to the intensity of her own."
            elif _return == 'anal_outside':
                "Amy's timely warning gives me the chance to pull out before the end."
                "And the act of doing so only seems to make it all the more intense for her too."
                "Amy moans and quivers as her orgasm takes hold."
                show amy cowgirl up speed
                pause 0.15
                show amy cowgirl down ahegao at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up
                pause 0.15
                show amy cowgirl down at startle(0.05,-10)
                pause 0.15
                show amy cowgirl up out -speed
                pause 0.5
                show amy cowgirl cum with vpunch
                pause 0.75
                show amy cowgirl pleasure bodycum -cum with vpunch
                $ amy.sub + 1
                "At the same time I feel myself letting go too."
                "Shooting my load up and over her belly."
    return

label amy_fuck_date_nudistbeach:
label amy_fuck_date_beach:
label amy_fuck_beach:
    menu:
        "Doggy":
            call amy_fuck_beach_doggy (0) from _call_amy_fuck_beach_doggy
        "Cowgirl" if hero.sexperience >= 10 and not game.room == "date_nudistbeach":
            call amy_fuck_beach_cowgirl (10) from _call_amy_fuck_beach_cowgirl
    return

label amy_fuck_beach_doggy(sexperience_min):
    scene bg beach
    show amy
    "One of the best things about coming to the beach with Amy is the looks that we get from people."
    "And by that I mean the first glance that turns their heads."
    "Then the second one that they have to take to make sure of what they just saw!"
    "I mean, it's probably the last place on earth you'd expect to see a genuine goth."
    "Never mind one that looks as downright stunning in a swimsuit as Amy does."
    "And the best thing is that she's here with me!"
    "Another guy might get jealous of all the attention that Amy's getting."
    "But not me - it just makes me prouder to be seen with her than ever."
    "In fact, I want to choose a spot on the beach where everyone can see us."
    mike.say "This looks like a good spot, Amy."
    mike.say "How about we sit down here for a while?"
    show amy annoyed
    "Amy turns to regard the spot I'm talking about."
    "And I can instantly tell that she's not impressed."
    show amy upset
    amy.say "No way, [hero.name]."
    amy.say "There's way too many people around here."
    amy.say "I want somewhere a little more private."
    hide amy with easeoutleft
    "With that, she turns and walks off down the beach."
    "I watch her go with my mouth hanging open."
    "Because I was just about to argue for my choice of spot."
    "And the fact Amy just rejected it out of hand makes me feel more than a little annoyed."
    "So I hurry after her, already rehearsing the points that I'm going to make in my head."
    scene black with dissolve
    pause 1
    scene bg beach
    show amy flirt
    with dissolve
    "Catching up to her takes longer than I expected it to, as she's walking fairly fast."
    "And when I do, Amy's reached a deserted part of the beach, out of sight from the rest of it too."
    mike.say "Amy..."
    mike.say "I was going to say..."
    "Amy has her back to me as I arrive."
    "And I don't really notice what she's doing."
    if not game.room == 'date_nudistbeach':
        show amy topless with dissolve
        "That is until she unties the top of her swimsuit, revealing her breasts."
        "And yeah, I know that I said she has her back turned to me already."
        "But maybe you don't really understand how large her breasts really are!"
        amy.say "Huh?"
        amy.say "What was that, [hero.name]?"
        mike.say "Oh..."
        mike.say "It was nothing, Amy!"
        mike.say "I didn't realise you wanted to sunbathe topless!"
        show amy normal
        "Amy chuckles at this and shakes her head."
        "Like I just said something dumb as hell."
        amy.say "I don't want to sunbathe, [hero.name]."
        show amy flirt
        amy.say "I want to do something far more fun than that!"
        show amy naked with dissolve
        "With that, Amy pulls down the rest of her swimsuit."
        "Then she steps out of it completely and turns to face me."
    amy.say "Come on, [hero.name]..."
    amy.say "Don't just stand there staring."
    amy.say "Let's fuck!"
    "My head starts to nod and my hands to move before I even think about it."
    if not game.room == 'date_nudistbeach':
        "Which means that I'm more than half out of my shorts before I snap back to reality."
        "And what the hell was I even thinking wanting to be where we could be seen?"
        "Amy's idea is a hundred times better than that!"
        "By the time I kick my shorts off, she's already down on her hands and knees."
    "She looks back over her shoulder at me, beckoning with her eyes."
    amy.say "Let's get going."
    amy.say "Because you look like you're ready for it!"
    "A quick glance down at myself proves that she's right."
    "My cock is already standing to attention, as hard as it can get."
    "So I hurry to kneel down in the sand behind Amy."
    show amy doggy beach with fade
    "And as soon as I have my hands on her waist, I'm ready to go."
    menu:
        "Fuck her pussy":
            "I can already see the pink folds of Amy's pussy between her thighs."
            "And the mere sight of it makes up my mind as to where I'm aiming for."
            "I'm all ready and set to go, so I pull back and take a deep breath."
            call amy_fuck_doggy_ask_accessories from _call_amy_fuck_doggy_ask_accessories_1
            if BEADS:
                "Though it doesn't take me long to see the problem here."
                if PLUG:
                    "Amy's gone and filled up all the holes on offer!"
                else:
                    "Amy's gone and filled up the hole I'm interested in!"
                "Not only that, she's told me not to pull anything out until she cums!"
                "Which I guess means that I'm going to have to improvise."
                "With that in mind, I reach down between her thighs."
                show amy doggy finger -nomc
                "My fingers find the folds of her pussy."
                "Then I start to stroke and tickle with my fingertips."
                show amy doggy pleasure fingerup
                pause 0.25
                show amy doggy fingerdown
                pause 0.25
                show amy doggy fingerup
                pause 0.25
                show amy doggy fingerdown
                "Almost instantly, Amy starts to moan with pleasure."
                "But I don't take it slowly or build it gradually."
                show amy doggy fingerup
                pause 0.2
                show amy doggy fingerdown
                pause 0.2
                show amy doggy fingerup
                pause 0.2
                show amy doggy fingerdown
                pause 0.2
                show amy doggy fingerup
                pause 0.2
                show amy doggy fingerdown
                "Instead I work her as fast and intensely as I can."
                "Using all the tricks I know, I try to make Amy cum."
                "Because she never said I could only do it once."
                "Or which orgasm meant I could pull something out of her."
                "Pretty soon it's obvious Amy can't hold on any longer."
                show amy doggy fingerup
                pause 0.1
                show amy doggy fingerdown
                pause 0.1
                show amy doggy fingerup
                pause 0.1
                show amy doggy fingerdown
                pause 0.1
                show amy doggy fingerup
                pause 0.1
                show amy doggy fingerdown
                pause 0.1
                show amy doggy fingerup
                pause 0.1
                show amy doggy fingerdown
                pause 0.1
                show amy doggy fingerup
                pause 0.1
                show amy doggy fingerdown
                "She's tossing her head around and almost grunting."
                "So I take hold of the cord and pull the beads out of her."
                show amy doggy nomc lookup pleasure beads2 squirt
                pause 0.1
                show amy doggy beads3
                pause 0.1
                show amy doggy beads4
                pause 0.1
                show amy doggy beads5
                pause 0.1
                show amy doggy ahegao beads6
                amy.say "Ah..."
                amy.say "Oh...oh fuck!"
                show amy doggy lookdown pleasure -beads -squirt
                "By now Amy's more than ready for me."
            show amy doggy normal vaginal -nomc
            "And I feel myself sliding into her with almost no resistance."
            "I make sure to go as deep into her as I possibly can."
            show amy doggy trust pleasure
            "And only then do I start to move back and forth."
            "Amy has her hands and knees spread wide right now."
            "So that means they're bracing her posture."
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            "But all the same she still starts to be pushed forwards."
            "Pretty soon I can see her carving tracks into the sand."
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            "Each thrust I make pushing her a little way forwards."
            "Not that it seems to bother Amy in the slightest."
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            "She keeps right on nodding and gasping with pleasure the whole time."
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            "In fact, I can even see her breasts swaying back and forth too!"
            "The sheer size of them means that I get an eyeful every time they do so."
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            "Part of me keeps on willing Amy to keep her head up."
            "Because I'd hate to see what would happen if they were to hit her in the face!"
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            pause 0.2
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            "Pushing that thought aside, I redouble my efforts."
            "We might have come to a deserted part of the beach to do this."
            "But that doesn't mean it's going to stay that way."
            "I can feel a tinge of paranoia creeping over me as I realise that."
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            pause 0.2
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            "And it's partially responsible for me trying to speed things up."
            show amy doggy lookup
            "Luckily for me, Amy doesn't seem to notice."
            "Instead she soaks up my efforts and hangs in there for more."
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            pause 0.2
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            "Or at least she does until I start to feel her quivering inside."
            "Which I guess means she's going to cum any second!"
            amy.say "Oh shit..."
            show amy doggy lookdown
            amy.say "Here it comes!"
            menu:
                "Cum inside":
                    show amy doggy ahegao -trust
                    pause 0.1
                    show amy doggy trust speed up with hpunch
                    pause 0.1
                    show amy doggy -speed down
                    "By now I'm practically holding Amy up as she cums."
                    "I can feel the strength draining out of her body, consumed by her orgasm"
                    show amy doggy ahegao -trust
                    pause 0.1
                    show amy doggy trust speed up with hpunch
                    pause 0.1
                    show amy doggy cum down -speed with hpunch
                    $ amy.love += 2
                    $ amy.impregnate()
                    "But now I'm shooting my load into her at the same time, climaxing too."
                    with hpunch
                    "And that means I'm becoming as drained of energy as she is."
                    show amy doggy pleasure nomc openpussy screencum with hpunch
                    "Once it's over, I can't keep it up any longer and I have to let go."
                    "So Amy slides off of my cock and collapses onto the sand before me."
                "Pull out":
                    show amy doggy ahegao -trust
                    pause 0.1
                    show amy doggy trust speed up with hpunch
                    pause 0.1
                    show amy doggy -speed down
                    "By now I'm practically holding Amy up as she cums."
                    "I can feel the strength draining out of her body, consumed by her orgasm"
                    show amy doggy out ease cum openpussy with hpunch
                    $ amy.love += 1
                    "But now I'm pulling out of her at the same time as climaxing too."
                    with hpunch
                    "And that means I'm becoming as drained of energy as she is."
                    show amy doggy pleasure nomc screencum -cum with hpunch
                    "I can't keep it up any longer and I have to let go."
                    "So Amy slides off of my cock and collapses onto the sand before me."
                    show amy doggy normal
                    "Where my cum rains down on her ass and thighs."
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5) and amy.sub >= 50:
            "I can already see the pink shape of Amy's ass between her buttocks."
            "And the mere sight of it makes up my mind as to where I'm aiming for."
            "I'm all ready and set to go, so I pull back and take a deep breath."
            call amy_fuck_doggy_ask_accessories from _call_amy_fuck_doggy_ask_accessories_2
            if PLUG:
                "Though it doesn't take me long to see the problem here."
                if BEADS:
                    "Amy's gone and filled up all the holes on offer!"
                else:
                    "Amy's gone and filled up the hole I'm interested in!"
                "Not only that, she's told me not to pull anything out until she cums!"
                "Which I guess means that I'm going to have to improvise."
                "With that in mind, I reach down between her thighs."
                show amy doggy finger -nomc
                "My fingers find the folds of her pussy."
                "Then I start to stroke and tickle with my fingertips."
                show amy doggy pleasure fingerup
                pause 0.25
                show amy doggy fingerdown
                pause 0.25
                show amy doggy fingerup
                pause 0.25
                show amy doggy fingerdown
                "Almost instantly, Amy starts to moan with pleasure."
                "But I don't take it slowly or build it gradually."
                show amy doggy fingerup
                pause 0.2
                show amy doggy fingerdown
                pause 0.2
                show amy doggy fingerup
                pause 0.2
                show amy doggy fingerdown
                pause 0.2
                show amy doggy fingerup
                pause 0.2
                show amy doggy fingerdown
                "Instead I work her as fast and intensely as I can."
                "Using all the tricks I know, I try to make Amy cum."
                "Because she never said I could only do it once."
                "Or which orgasm meant I could pull something out of her."
                "Pretty soon it's obvious Amy can't hold on any longer."
                show amy doggy fingerup
                pause 0.1
                show amy doggy fingerdown
                pause 0.1
                show amy doggy fingerup
                pause 0.1
                show amy doggy fingerdown
                pause 0.1
                show amy doggy fingerup
                pause 0.1
                show amy doggy fingerdown
                pause 0.1
                show amy doggy fingerup
                pause 0.1
                show amy doggy fingerdown
                pause 0.1
                show amy doggy fingerup
                pause 0.1
                show amy doggy fingerdown
                "She's tossing her head around and almost grunting."
                "So I take hold of the plug and pull it out of her."
                show amy doggy lookup pleasure squirt fingerup
                pause 0.1
                show amy doggy fingerdown
                pause 0.1
                show amy doggy fingerup
                pause 0.1
                show amy doggy fingerdown
                pause 0.1
                show amy doggy nomc
                pause 0.1
                show amy doggy ahegao plugout
                amy.say "Ah..."
                amy.say "Oh...oh fuck!"
                show amy doggy lookdown pleasure -buttplug -squirt
                "By now Amy's more than ready for me."
            show amy doggy normal anal -nomc
            "And I feel myself sliding into her with almost no resistance."
            "I make sure to go as deep into her as I possibly can."
            show amy doggy trust pleasure
            "And only then do I start to move back and forth."
            "Amy has her hands and knees spread wide right now."
            "So that means they're bracing her posture."
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            "But all the same she still starts to be pushed forwards."
            "Pretty soon I can see her carving tracks into the sand."
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            "Each thrust I make pushing her a little way forwards."
            "Not that it seems to bother Amy in the slightest."
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            "She keeps right on nodding and gasping with pleasure the whole time."
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            "In fact, I can even see her breasts swaying back and forth too!"
            "The sheer size of them means that I get an eyeful every time they do so."
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            "Part of me keeps on willing Amy to keep her head up."
            "Because I'd hate to see what would happen if they were to hit her in the face!"
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            pause 0.2
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            "Pushing that thought aside, I redouble my efforts."
            "We might have come to a deserted part of the beach to do this."
            "But that doesn't mean it's going to stay that way."
            "I can feel a tinge of paranoia creeping over me as I realise that."
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            pause 0.2
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            "And it's partially responsible for me trying to speed things up."
            show amy doggy lookup
            "Luckily for me, Amy doesn't seem to notice."
            "Instead she soaks up my efforts and hangs in there for more."
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            pause 0.2
            show amy doggy -trust
            pause 0.1
            show amy doggy trust speed up with hpunch
            pause 0.1
            show amy doggy -speed down
            "Or at least she does until I start to feel her quivering inside."
            "Which I guess means she's going to cum any second!"
            amy.say "Oh shit..."
            show amy doggy lookdown
            amy.say "Here it comes!"
            menu:
                "Cum inside":
                    show amy doggy ahegao -trust
                    pause 0.1
                    show amy doggy trust speed up with hpunch
                    pause 0.1
                    show amy doggy -speed down
                    "By now I'm practically holding Amy up as she cums."
                    "I can feel the strength draining out of her body, consumed by her orgasm"
                    show amy doggy ahegao -trust
                    pause 0.1
                    show amy doggy trust speed up with hpunch
                    pause 0.1
                    show amy doggy ease cum down -speed with hpunch
                    $ amy.sub += 2
                    "But now I'm shooting my load into her at the same time, climaxing too."
                    with hpunch
                    "And that means I'm becoming as drained of energy as she is."
                    show amy doggy pleasure nomc -anal assgap screencum -cum with hpunch
                    "Once it's over, I can't keep it up any longer and I have to let go."
                    "So Amy slides off of my cock and collapses onto the sand before me."
                "Pull out":
                    show amy doggy ahegao -trust
                    pause 0.1
                    show amy doggy trust speed up with hpunch
                    pause 0.1
                    show amy doggy -speed down
                    "By now I'm practically holding Amy up as she cums."
                    "I can feel the strength draining out of her body, consumed by her orgasm"
                    show amy doggy out ease cum with hpunch
                    $ amy.sub += 1
                    "But now I'm pulling out of her at the same time as climaxing too."
                    with hpunch
                    "And that means I'm becoming as drained of energy as she is."
                    show amy doggy pleasure nomc -anal assgap screencum -cum with hpunch
                    "I can't keep it up any longer and I have to let go."
                    "So Amy slides off of my cock and collapses onto the sand before me."
                    show amy doggy normal
                    "Where my cum rains down on her ass and thighs."
    $ amy.sexperience += 1
    return

label amy_fuck_doggy_ask_accessories:
    $ BEADS = PLUG = False
    menu:
        "Use beads" if "anal_beads" in hero.inventory:
            $ BEADS = True
            amy.say "Wait a minute..."
            amy.say "I want to use these."
            "I pause as Amy hands me a string of pleasure beads."
            "Then she nods back over her shoulder."
            amy.say "Push them up my pussy, okay?"
            amy.say "Then pull them out just as I cum!"
            show amy doggy nomc
            "I nod as I take the beads."
            "And then I do as Amy says."
            show amy doggy pleasure beads beads4
            pause 1
            show amy doggy beads3
            "She gasps and sighs as I push each bead home."
            show amy doggy beads2
            pause 1
            show amy doggy normal beads1
            "Then we're ready to get on with it."
        "Use butt-plug" if amy.flags.buttplug:
            $ PLUG = True
            amy.say "Wait a minute..."
            amy.say "I want to use this."
            "I pause as Amy hands me what can only be a butt-plug."
            "Then she nods back over her shoulder."
            amy.say "Push it up my ass, okay?"
            amy.say "Then pull it out just as I cum!"
            show amy doggy nomc
            "I nod as I take the plug."
            "And then I do as Amy says."
            show amy doggy pleasure buttplug
            "She gasps and sighs as I work it up there."
            show amy doggy normal
            "Then we're ready to get on with it."
        "Use beads and butt-plug" if "anal_beads" in hero.inventory and amy.flags.buttplug:
            $ BEADS = PLUG = True
            amy.say "Wait a minute..."
            amy.say "I want to use these."
            "I pause as Amy hands me a string of pleasure beads and a butt-plug."
            "Then she nods back over her shoulder."
            amy.say "Push the beads into my pussy and the plug up my ass, okay?"
            amy.say "Then pull them out just as I cum!"
            show amy doggy nomc
            "I nod as I take the beads and the butt-plug."
            "And then I do as Amy says."
            show amy doggy pleasure beads beads4
            pause 1
            show amy doggy beads3
            "She gasps and sighs as I push each bead home."
            show amy doggy buttplug
            "Then she moans as I work the plug up her ass."
            show amy doggy beads2
            pause 1
            show amy doggy normal beads1
            "Then we're ready to get on with it."
        "No time for toys":
            amy.say "Hurry up, [hero.name]!"
            amy.say "Let's get going already!"
    return

label amy_fuck_beach_cowgirl(sexperience_min):
    scene bg beach
    "It's one of those days when the sun's high in the sky and there's not a cloud in sight."
    "One of those days when the only logical thing to do is head straight to the beach."
    "And once you're there, it's so hot all you want to do is lie back on the sand and relax."
    "Or at lease that's what any normal and sane person would want to do."
    "Unfortunately for me, it looks like Amy didn't get the memo on that one."
    scene bg beach at center, zoomAt (1.75, (980, 1160))
    show minami_bj_ambient
    show amy swimsuit upset at center, zoomAt (1.5, (640, 840)), dark
    with fade
    amy.say "Is that all you're going to do today, [hero.name]?"
    amy.say "Laze around on the sand like a beached whale?"
    "Amy's leaning over me as she says all of this."
    "And what's worse, she's blocking out the sunlight too!"
    "I squint as I try to look up at her."
    "Frowning as well to make it clear I'm annoyed."
    mike.say "Hey!"
    mike.say "Who are you calling a whale?!?"
    mike.say "I'll have you know that I've been working out extra hard at the gym lately!"
    "Amy rolls her eyes."
    "Then she makes a point of poking me in the stomach."
    mike.say "OUCH!"
    amy.say "Okay, okay..."
    show amy annoyed
    amy.say "You're lazing around like a buff beached whale!"
    amy.say "The point is you're still killing me with boredom here."
    show amy upset
    amy.say "When are we going to get off our asses and do something?"
    mike.say "We are doing something, Amy."
    mike.say "We're soaking up the sun!"
    show amy annoyed
    "I can see that Amy's not going to let it go."
    "But I'm also not going to give up on a chance to do nothing for a change."
    mike.say "Okay, Amy..."
    mike.say "I'll do whatever you can think of."
    show amy normal
    "I see Amy's mood change instantly."
    "Because she's taking my words as me giving up and letting her have her way."
    mike.say "On one condition!"
    amy.say "And what's that?"
    mike.say "Whatever you can think of..."
    mike.say "So long as I don't have to get up!"
    show amy upset
    "Amy wrinkles her brows and opens her mouth, like she's going to argue with me."
    show amy shy
    "But then she seems to have a change of mind, cocking her head on one side."
    show amy flirt
    amy.say "Okay, [hero.name]..."
    amy.say "It's a deal!"
    "Now I have to admit that I'm getting interested."
    "I never expected Amy to agree to my conditions so easily."
    "So I'm intrigued to see what she's cooking up inside of her head."
    "Amy seems to know that she has my attention too."
    "As she's still wearing that same knowing smile."
    "And it remains on her face as she reaches behind her back."
    show amy topless with dissolve
    "The next thing I know, Amy's untied her swimsuit."
    "It falls down, releasing her breasts as it does so."
    "And believe me, I do mean releases them."
    "Amy's breasts are large enough for the whole thing to be pretty dramatic!"
    "Unfortunately, my first thought isn't of an amorous nature."
    "Instead I prop myself up on my elbows and look around nervously."
    mike.say "Amy!"
    mike.say "What are you doing?"
    mike.say "This isn't the nudist beach!"
    show amy happy
    amy.say "Weren't you talking about relaxing just now?"
    amy.say "And here you are, freaking out like crazy!"
    mike.say "That was before you started getting naked!"
    show amy normal
    amy.say "Oh please!"
    amy.say "There's nobody around here - I already checked."
    mike.say "You're sure?"
    "Amy doesn't dignify that with an answer."
    show amy naked with dissolve
    "She simply keeps on smiling as she pulls off her swimsuit."
    "I guess that she's serious about us being alone."
    "And she did come up with something I can do without moving too."
    "So I just shrug and begin to pull down my trunks."
    show amy flirt
    "Amy's smile becomes wider still as she sees me getting with the program."
    "And she doesn't hesitate to straddle me as soon as she's able."
    show amy blush
    amy.say "Hmm..."
    amy.say "Looks like one part of you is already up for it!"
    "She reaches out and takes hold of my cock, rubbing the shaft."
    "And she's right too."
    "As much as I needed convincing, it's already getting good and hard!"
    show amy -blush
    amy.say "So..."
    amy.say "What are we going to do with this?"
    scene bg black
    show amy cowgirl beach
    with fade
    "To me, that's an academic question."
    "Because as Amy climbed onto me, I saw what I want."
    menu:
        "Fuck her pussy":
            "And now I'm in the perfect position to get it."
            "Amy's not expecting me to be the one to make the first move."
            show amy cowgirl hurt mikehand
            "So it takes her by surprise when my hands grab hold of her."
            amy.say "Wha..."
            amy.say "What are you..."
            show amy cowgirl vaginal pleasure
            "And there's nothing she can do as I pull her downwards either."
            amy.say "Oh..."
            amy.say "Oh fuck..."
            amy.say "That feels...so good!"
            "I don't waste any time with foreplay."
            "I just take hold of Amy and begin to push into her."
            "The fact that her pussy isn't one hundred percent ready doesn't bother me."
            "In fact it makes the experience that much more enjoyable."
            "Because it means that I have to work harder to get in there."
            "So the sensations are that much more intense as a result."
            "I don't hesitate in what I'm doing because I can read Amy's face."
            "And I know the look on it very well."
            "She doesn't even need to add the nods to make it clear."
            "She's loving this every bit as much as me."
            show amy cowgirl down
            "My cock inches into Amy at an achingly slow rate."
            "Every new degree it reaches heightens the sensations of pleasure I'm feeling."
            "By now Amy's taken me as far inside as she possibly can."
            show amy cowgirl normal
            "And she sits there for a while, just enjoying the experience."
            "It's hard for me to see her face right now."
            "And that's because her breasts are blocking my view."
            "But soon enough Amy starts to move atop me."
            show amy cowgirl up
            pause 0.45
            show amy cowgirl down at startle(0.05,-10)
            pause 0.45
            show amy cowgirl up
            pause 0.45
            show amy cowgirl down at startle(0.05,-10)
            pause 0.45
            show amy cowgirl up
            pause 0.45
            show amy cowgirl down at startle(0.05,-10)
            "She's like a genuine cowgirl getting her mount up to speed."
            "Amy begins to bounce up and down on my thighs."
            "And more importantly on my cock too!"
            "This means that her entire body is in motion."
            "Which includes her impressive cleavage."
            show amy cowgirl up
            pause 0.35
            show amy cowgirl down speed at startle(0.05,-10)
            pause 0.35
            show amy cowgirl up
            pause 0.35
            show amy cowgirl down at startle(0.05,-10)
            pause 0.35
            show amy cowgirl up
            pause 0.35
            show amy cowgirl down -speed at startle(0.05,-10)
            "Pretty soon she's built up some serious speed."
            "And her breasts are swinging around like crazy."
            "Part of me is glad that I'm laid on my back."
            "Because taking one in the face would be dangerous."
            "Like getting slapped with a wet sack of sand!"
            "In fact, they're kind of hypnotic."
            "Moving in time with Amy's motions and holding my eye."
            show amy cowgirl pleasure up
            pause 0.35
            show amy cowgirl down speed at startle(0.05,-10)
            pause 0.35
            show amy cowgirl up
            pause 0.35
            show amy cowgirl down at startle(0.05,-10)
            pause 0.35
            show amy cowgirl up
            pause 0.35
            show amy cowgirl down at startle(0.05,-10)
            pause 0.35
            show amy cowgirl up -speed
            "It's impossible not to look at them, to be drawn in by them!"
            "So much so that the sensations of Amy riding me become unconscious."
            "They're still there, pushing me ever further into a state of ecstasy."
            "But those swinging breasts are the only thing on my mind."
            "Or at least they are until Amy pushes down with all her weight."
            show amy cowgirl up
            pause 0.25
            show amy cowgirl down speed at startle(0.05,-10)
            pause 0.25
            show amy cowgirl up
            pause 0.25
            show amy cowgirl down -speed at startle(0.05,-10)
            amy.say "I..."
            amy.say "I'm gonna..."
            show amy cowgirl up speed
            pause 0.25
            show amy cowgirl down at startle(0.05,-10)
            pause 0.25
            show amy cowgirl up
            pause 0.25
            show amy cowgirl down -speed at startle(0.05,-10)
            amy.say "I'm gonna cum!"
            mike.say "Oh shit..."
            mike.say "Me too!"
            menu:
                "Cum inside":
                    "There's no way I can get out from under Amy."
                    "Not before I lose it anyway."
                    show amy cowgirl up
                    pause 0.15
                    show amy cowgirl down speed at startle(0.05,-10)
                    pause 0.15
                    show amy cowgirl up
                    pause 0.15
                    show amy cowgirl down at startle(0.05,-10)
                    pause 0.15
                    show amy cowgirl up
                    pause 0.15
                    show amy cowgirl down at startle(0.05,-10)
                    pause 0.15
                    show amy cowgirl up
                    pause 0.15
                    show amy cowgirl down at startle(0.05,-10)
                    pause 0.15
                    show amy cowgirl up
                    pause 0.15
                    show amy cowgirl down ahegao cum -speed with vpunch
                    $ amy.love += 2
                    $ amy.impregnate()
                    pause 0.35
                    show amy cowgirl up
                    pause 0.35
                    show amy cowgirl down with vpunch
                    pause 0.5
                    show amy cowgirl up
                    pause 0.5
                    show amy cowgirl down with vpunch
                    pause 0.75
                    show amy cowgirl up
                    "So I stay right where I am and ride it out."
                    "Soon enough Amy's orgasm drags me along too."
                    show amy cowgirl down pleasure at startle
                    "And we both climax right there, laid on the sand."
                "Pull out":
                    "I have no idea how I manage to pull it off."
                    "But somehow I wriggle my way out from under Amy."
                    "Or at least enough to free my cock before it's too late."
                    show amy cowgirl up
                    pause 0.15
                    show amy cowgirl down ahegao speed at startle(0.05,-10)
                    pause 0.15
                    show amy cowgirl up
                    pause 0.15
                    show amy cowgirl down at startle(0.05,-10)
                    pause 0.15
                    show amy cowgirl up
                    pause 0.15
                    show amy cowgirl down at startle(0.05,-10)
                    pause 0.15
                    show amy cowgirl up out -speed
                    pause 0.5
                    show amy cowgirl cum with vpunch
                    pause 0.75
                    show amy cowgirl pleasure bodycum -cum with vpunch
                    $ amy.love += 1
                    "I shoot my load a moment later, all over her belly."
                    show amy cowgirl down normal at startle
                    "And we both climax right there, laid on the sand."
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5) and amy.sub >= 50:
            "I want to sneak into her tight little ass!"
            "And now I'm in the perfect position to get it."
            "Amy's not expecting me to be the one to make the first move."
            show amy cowgirl hurt mikehand
            "So it takes her by surprise when my hands grab hold of her."
            amy.say "Wha..."
            amy.say "What are you..."
            show amy cowgirl anal pleasure
            "And there's nothing she can do as I pull her downwards either."
            amy.say "Oh..."
            amy.say "Oh fuck..."
            amy.say "That feels...so good!"
            "I don't waste any time with foreplay."
            "I just take hold of Amy and begin to push into her."
            "The fact that her pussy isn't one hundred percent ready doesn't bother me."
            "In fact it makes the experience that much more enjoyable."
            "Because it means that I have to work harder to get in there."
            "So the sensations are that much more intense as a result."
            "I don't hesitate in what I'm doing because I can read Amy's face."
            "And I know the look on it very well."
            "She doesn't even need to add the nods to make it clear."
            "She's loving this every bit as much as me."
            show amy cowgirl down
            "My cock inches into Amy at an achingly slow rate."
            "Every new degree it reaches heightens the sensations of pleasure I'm feeling."
            "By now Amy's taken me as far inside as she possibly can."
            show amy cowgirl normal
            "And she sits there for a while, just enjoying the experience."
            "It's hard for me to see her face right now."
            "And that's because her breasts are blocking my view."
            "But soon enough Amy starts to move atop me."
            show amy cowgirl up
            pause 0.45
            show amy cowgirl down at startle(0.05,-10)
            pause 0.45
            show amy cowgirl up
            pause 0.45
            show amy cowgirl down at startle(0.05,-10)
            pause 0.45
            show amy cowgirl up
            pause 0.45
            show amy cowgirl down at startle(0.05,-10)
            "She's like a genuine cowgirl getting her mount up to speed."
            "Amy begins to bounce up and down on my thighs."
            "And more importantly on my cock too!"
            "This means that her entire body is in motion."
            "Which includes her impressive cleavage."
            show amy cowgirl speed up
            pause 0.35
            show amy cowgirl down at startle(0.05,-10)
            pause 0.35
            show amy cowgirl up
            pause 0.35
            show amy cowgirl down at startle(0.05,-10)
            pause 0.35
            show amy cowgirl up
            pause 0.35
            show amy cowgirl down -speed at startle(0.05,-10)
            "Pretty soon she's built up some serious speed."
            "And her breasts are swinging around like crazy."
            "Part of me is glad that I'm laid on my back."
            "Because taking one in the face would be dangerous."
            "Like getting slapped with a wet sack of sand!"
            "In fact, they're kind of hypnotic."
            "Moving in time with Amy's motions and holding my eye."
            show amy cowgirl pleasure up
            pause 0.35
            show amy cowgirl down speed at startle(0.05,-10)
            pause 0.35
            show amy cowgirl up
            pause 0.35
            show amy cowgirl down at startle(0.05,-10)
            pause 0.35
            show amy cowgirl up
            pause 0.35
            show amy cowgirl down at startle(0.05,-10)
            pause 0.35
            show amy cowgirl up -speed
            "It's impossible not to look at them, to be drawn in by them!"
            "So much so that the sensations of Amy riding me become unconscious."
            "They're still there, pushing me ever further into a state of ecstasy."
            "But those swinging breasts are the only thing on my mind."
            "Or at least they are until Amy pushes down with all her weight."
            show amy cowgirl up speed
            pause 0.25
            show amy cowgirl down at startle(0.05,-10)
            pause 0.25
            show amy cowgirl up
            pause 0.25
            show amy cowgirl down -speed at startle(0.05,-10)
            amy.say "I..."
            amy.say "I'm gonna..."
            show amy cowgirl up speed
            pause 0.25
            show amy cowgirl down at startle(0.05,-10)
            pause 0.25
            show amy cowgirl up
            pause 0.25
            show amy cowgirl down -speed at startle(0.05,-10)
            amy.say "I'm gonna cum!"
            mike.say "Oh shit..."
            mike.say "Me too!"
            menu:
                "Cum inside":
                    "There's no way I can get out from under Amy."
                    "Not before I lose it anyway."
                    show amy cowgirl up speed
                    pause 0.15
                    show amy cowgirl down at startle(0.05,-10)
                    pause 0.15
                    show amy cowgirl up
                    pause 0.15
                    show amy cowgirl down at startle(0.05,-10)
                    pause 0.15
                    show amy cowgirl up
                    pause 0.15
                    show amy cowgirl down at startle(0.05,-10)
                    pause 0.15
                    show amy cowgirl up
                    pause 0.15
                    show amy cowgirl down at startle(0.05,-10)
                    pause 0.15
                    show amy cowgirl up
                    pause 0.15
                    show amy cowgirl down ahegao cum -speed with vpunch
                    $ amy.sub += 2
                    pause 0.35
                    show amy cowgirl up
                    pause 0.35
                    show amy cowgirl down with vpunch
                    pause 0.5
                    show amy cowgirl up
                    pause 0.5
                    show amy cowgirl down with vpunch
                    pause 0.75
                    show amy cowgirl up
                    "So I stay right where I am and ride it out."
                    "Soon enough Amy's orgasm drags me along too."
                    show amy cowgirl down pleasure at startle
                    "And we both climax right there, laid on the sand."
                "Pull out":
                    "I have no idea how I manage to pull it off."
                    "But somehow I wriggle my way out from under Amy."
                    "Or at least enough to free my cock before it's too late."
                    show amy cowgirl up speed
                    pause 0.15
                    show amy cowgirl down ahegao at startle(0.05,-10)
                    pause 0.15
                    show amy cowgirl up
                    pause 0.15
                    show amy cowgirl down at startle(0.05,-10)
                    pause 0.15
                    show amy cowgirl up
                    pause 0.15
                    show amy cowgirl down at startle(0.05,-10)
                    pause 0.15
                    show amy cowgirl up out -speed
                    pause 0.5
                    show amy cowgirl cum with vpunch
                    pause 0.75
                    show amy cowgirl pleasure bodycum -cum with vpunch
                    $ amy.sub + 1
                    "I shoot my load a moment later, all over her belly."
                    show amy cowgirl down normal at startle
                    "And we both climax right there, laid on the sand."
    return

label amy_fuck_date_cinema:
label amy_fuck_cinema:
    scene bg cinema
    show amy casual shy blush
    "As far as I'm concerned, Amy and I have come out to watch a movie today."
    "We've agreed on what to see, paid for the tickets, even bought some popcorn."
    "But there's just something bugging me about the way she's behaving."
    "I haven't been able to put my finger on just what it is though."
    scene bg cinemaroom
    show amy casual shy blush
    with fade
    "Even now that we're sitting in the theatre and the lights are going down."
    "It's still like there's something stopping her getting into it."
    "But if she's not going to tell me about it, then that's her problem, right?"
    "No reason I can't ignore her and just enjoy the film."
    "And that's just what I try to do."
    show amy cunnilingus cinema mikesit popcorn orgasm
    "I look straight forwards and at the screen."
    "Doing the best I can to immerse myself in the movie."
    "But then I start to realise there's something else bugging me as well."
    "It's like a buzzing sound, making me worry I'm getting tinnitus."
    "What's going on here?"
    "Am I losing my mind?"
    "It's no good."
    "I have to ask Amy if she can hear that damn buzzing sound too!"
    "I lean in as close as I can, whispering into her ear."
    show amy cunnilingus pleasure
    mike.say "Amy..."
    mike.say "Can you hear that sound?"
    mike.say "It's like a buzzing!"
    "Amy keeps on staring straight ahead as I ask her the question."
    "But I see that she shakes her head all the same."
    mike.say "Are you sure?"
    mike.say "I swear that I can..."
    "I stop speaking as the sound begins to fade away."
    "And within seconds it's gone altogether."
    mike.say "Huh..."
    mike.say "Never mind, Amy."
    mike.say "It just stopped!"
    "It's only now that I notice how Amy's sitting."
    "She has her knees drawn up almost to her chin."
    "Which is weird, as this isn't supposed to be a scary movie!"
    mike.say "Amy..."
    mike.say "Are you okay?"
    "Amy shakes her head, still refusing to actually speak."
    show amy cunnilingus open vibrator_remote masturbating
    "Then she parts her legs and points between them."
    "I have to admit that I've got no idea what the problem could be."
    "But I figure that I owe it to her to take a look."
    "Who knows, maybe I can figure it out?"
    "Then we can get back to watching the damn film!"
    show amy cunnilingus -mikesit
    "Sliding out of my seat and onto the floor, I try to keep from being seen."
    "Luckily for me there's nobody sitting close to us in the dark theatre."
    "So the chance of anyone noticing what I'm doing are pretty small."
    show amy cunnilingus mikelick -masturbating
    "Once I'm on the floor, I don't waste time in checking Amy out."
    "And even in these gloomy surroundings there's no mistaking what I see."
    "Amy's got a battery pack strapped to one of her thighs."
    "And there's a wire leading from it into her panties."
    "A quick glance underneath them tells me where the buzzing was coming from."
    "Amy's been walking around with a love-egg inside of her this whole time!"
    "But now it seems that the batteries have run out."
    "And Amy's stuck on the brink of getting off."
    "All thought of the film is forgotten as I make a decision."
    "I'm far from being annoyed at Amy because of my discovery."
    "In fact I'm getting more turned on by the moment."
    "And I feel like it's my duty to help her out too."
    "Pulling the gusset of Amy's panties aside, I lean in closer."
    show amy cunnilingus finger fingerin -mikelick
    "Taking hold of the wire, I slowly pull at the toy inside of her."
    "At first it refuses to move an inch."
    "And I'm worried the wire will come away leaving the egg inside."
    "But then I feel relief as it begins to move."
    show amy cunnilingus orgasm fingerspeed
    "Amy moans, then bites her lip as I pull it out of her."
    "The act feels like it takes forever, like it'll never end."
    show amy cunnilingus openpussy vibrator -vibrator_remote -finger
    "So when it pops out with unexpected speed, I'm taken by surprise."
    "My distraction doesn't last for long, however."
    show amy cunnilingus -vibrator
    "As now I can see the way it's left Amy's pussy wide open."
    "And I can smell the scent of her too."
    "Now all I want is to get in there before it closes up again."
    show amy cunnilingus pleasure mikelick mikehand
    "So forgetting all about the egg, I push my head between her thighs."
    "I have no idea if Amy knows what I intend to do."
    "But that doesn't stop me for a moment."
    show amy cunnilingus orgasm closeup
    "My tongue is out and I'm down to business within mere seconds."
    "At first I just tease around the edges of Amy's pussy."
    "Using only the tip of my tongue, I trace the outline of her lips."
    "And then I start to slowly make my way inwards."
    show amy cunnilingus tonguemiddle
    pause 0.2
    show amy cunnilingus tongueup
    pause 0.2
    show amy cunnilingus tonguedown
    pause 0.2
    show amy cunnilingus tonguemiddle
    pause 0.2
    show amy cunnilingus tongueup
    pause 0.2
    show amy cunnilingus tonguedown
    "I do the best I can to explore every fold that I find."
    "My tongue describes a clockwise motion, spiralling inwards."
    show amy cunnilingus tonguemiddle
    pause 0.2
    show amy cunnilingus tongueup
    pause 0.2
    show amy cunnilingus tonguedown
    pause 0.2
    show amy cunnilingus tonguemiddle
    pause 0.2
    show amy cunnilingus tongueup
    pause 0.2
    show amy cunnilingus tonguedown
    "The deeper I go, the more effect I seem to please Amy."
    "Before I was holding her thighs apart to get down here."
    show amy cunnilingus pleasure at startle(0.05,-10)
    "But now she's using them to hold me in place."
    "Her legs are squeezing me tightly, pulling me inwards."
    "This means my face is pressed into her groin."
    "And the only thing filling my senses is Amy herself."
    "By now my tongue is beginning to dip deeper into her."
    "No longer tracing lines, it's now going all the way inside."
    show amy cunnilingus orgasm tonguemiddle at startle(0.05,-10)
    pause 0.15
    show amy cunnilingus tongueup
    pause 0.15
    show amy cunnilingus tonguedown
    pause 0.15
    show amy cunnilingus tonguemiddle
    pause 0.15
    show amy cunnilingus tongueup
    pause 0.15
    show amy cunnilingus tonguedown
    pause 0.15
    show amy cunnilingus tonguemiddle
    pause 0.15
    show amy cunnilingus tongueup
    pause 0.15
    show amy cunnilingus tonguedown
    "The flavour of her is at once both sweet and sour."
    "Impossible to compare to anything else imaginable."
    "And totally addictive as it overwhelms me."
    "I can't hear the sound of the film anymore."
    "Only Amy's subdued moans seem to be reaching my ears."
    "But there's something else too."
    "Something that sounds like the tearing of cloth."
    "I realise that it must be Amy's nails, clawing on the arms of her chair."
    "And that knowledge makes me aware of the fact she's building towards something big."
    show amy cunnilingus tonguemiddle at startle(0.05,-10)
    pause 0.1
    show amy cunnilingus tongueup
    pause 0.1
    show amy cunnilingus tonguedown
    pause 0.1
    show amy cunnilingus tonguemiddle
    pause 0.1
    show amy cunnilingus tongueup
    pause 0.1
    show amy cunnilingus tonguedown
    pause 0.1
    show amy cunnilingus tonguemiddle
    pause 0.1
    show amy cunnilingus tongueup
    pause 0.1
    show amy cunnilingus tonguedown
    pause 0.1
    show amy cunnilingus up tonguemiddle
    $ amy.love += 4
    pause 0.1
    show amy cunnilingus tongueup
    pause 0.1
    show amy cunnilingus tonguedown
    pause 0.1
    show amy cunnilingus tonguemiddle
    pause 0.1
    show amy cunnilingus tongueup
    pause 0.1
    show amy cunnilingus tonguedown
    pause 0.1
    show amy cunnilingus tonguemiddle
    pause 0.1
    show amy cunnilingus tongueup
    pause 0.1
    show amy cunnilingus tonguedown with vpunch
    "A few moments later, Amy lets out a muffled moan as she loses it."
    "Luckily for the both of us, it's covered by a loud sound from movie still playing."
    "So nobody else in the place is any the wiser as to what's going on."
    show amy cunnilingus mikesit down ahegao at startle(0.05,-10)
    "My job done, I creep back over to my seat and climb into it."
    "Amy smooths her skirt down without as much as a single word."
    "But I can see from the look on her face that she's totally sated."
    "And the smile on her face seems to be fixed in place."
    "Lasting until well after the film is over."
    return

label amy_fuck_date_park_male:
label amy_fuck_park:
    mike.say "You know, it's weird..."
    mike.say "There's normally so many more people here."
    show fx question
    "Amy looks around, as if she needs proof of my claim."
    "But then she raises her eyebrows and nods in agreement."
    amy.say "Hmm..."
    hide fx
    amy.say "I guess you're right."
    amy.say "No wonder I'm enjoying myself so much more than usual!"
    "As if we needed to be sure of it, Amy and I keep quiet for a while."
    "And in all that time, we don't see another soul pass by the bench."
    "Not even someone on any of the paths that we can see from where we're sitting."
    show amy happy
    amy.say "It's like we have the whole place to ourselves."
    amy.say "Like. we could do anything we wanted without getting caught!"
    "I feel a smile creeping onto my face as Amy says this."
    "And I just know that I have to call her on that boast."
    mike.say "Oh yeah?"
    mike.say "You want to bet on that, Amy?"
    show amy normal
    "Amy frowns as she looks me in the eye."
    amy.say "What's that supposed to mean?"
    mike.say "Oh, nothing..."
    mike.say "Just that I bet I can think of something you wouldn't do."
    mike.say "Something you'd chicken out on..."
    show amy mad
    amy.say "Oh yeah?"
    amy.say "And just what would that be?"
    "I do the best I can to keep from showing my satisfaction."
    "Because Amy's not just taking the bait."
    "More like she's swallowing it whole!"
    show amy surprised
    mike.say "A blow-job, Amy."
    mike.say "You'd never have the courage to do that."
    mike.say "Not right here and now."
    "Amy raises an eyebrow."
    show amy flirt
    "She smiles, making it knowing and ironic."
    "And rather than answering, she stands up."
    "For a moment I think that she's just going to walk off."
    "But then she turns to face me, going down on her knees."
    "Amy looks me in the eye as she settles down between my thighs."
    amy.say "Okay, [hero.name]..."
    amy.say "I'll see your blow-job."
    amy.say "And raise you one of these..."
    "I open my mouth to say something, but no words come out."
    "I'm stumped and speechless, because Amy really has upped the stakes."
    "Here I was thinking that she's want to do this quickly and quietly."
    "Taking advantage of me being stunned, Amy leaps into action."
    "She unzips my flies and proceeds to reach inside."
    "And as soon as she finds my cock, she pulls it out."
    show amy bj street down handjob noleftarm with fade
    "Her touch isn't particularly gentle, making me gasp."
    "But I'm not about to complain for fear of blowing being blown."
    "Amy smiles as she sees how hard I am already."
    "I guess she's either flattered that I'm aroused by her antics."
    "Or else she's grateful that she won't have to do all the work herself."
    show amy bj up -handjob with hpunch
    "Either way she wastes no time is pushing my cock between her breasts."
    "All I can do is lean back and cling onto the bench."
    "Because the moment it's in there, I hear myself moaning helplessly."
    "Amy doesn't hesitate, she just pushes onwards."
    "A hand on either side of her chest, she begins to massage me."
    "Like I already said, her breasts are an impressive size."
    "They're solid and reassuringly firm, yet they feel soft against my cock."
    "At first it's totally buried in her cleavage and out of sight."
    "But as Amy works away, kneading her breasts, it inches upwards."
    "Once the tip and then the head emerge, she giggles at the sight."
    "And then she starts to work it harder still."
    "Though that's the last time Amy uses her mouth to actually utter a sound."
    "At least one that's meant to convey meaning."
    show amy bj down mouthtongue
    "Because she leans forwards and begins to lick at the tip."
    "All the time she's still using her breasts to work the shaft."
    "But by now my cock is getting ever closer to her mouth."
    "And she takes full advantage, using her lips and tongue."
    "Together they start paying attention to the head."
    show amy bj eyesclosed blow
    "As soon as she's able, Amy takes it into her mouth."
    "And I feel my head beginning to swim as she does so."
    "Every inch of my cock is being tended to right now."
    show amy bj eyeslust
    "The head in her mouth."
    "The shaft between her breasts."
    "Hell, she's even squeezing my balls whenever she gets the chance!"
    "If I could manage to speak, I'd admit that she's won the bet."
    "That she's proven to me just how brave she actually is."
    "But I'm afraid that if I open my mouth, I'd just end up groaning like an animal."
    "Or even simply sitting here drooling like a helpless vegetable."
    show amy bj eyesclosed hard
    "Amy has her eyes closed as she starts to go faster."
    "I feel like I'm crazily deep inside her mouth by now."
    "And I don't think I'm going to be able to hold on much longer."
    "But If I'm going to cum, then I need to make a choice."
    "I need to decide where it's going to happen."
    menu:
        "Give her some nutrients":
            "I don't even know if I could pull myself out of Amy's mouth."
            "If I could summon the will to do it, even if I wanted to."
            "So the only thing to do is sit back and let the inevitable happen."
            "I feel like my hands are freezing in place, my fingers digging into the wood of the bench."
            "Then it happens, and I just hope that Amy's ready for it."
            show amy bj eyessurprised cum with vpunch
            $ amy.sub += 2
            pause 0.3
            show amy bj eyesahegao with vpunch
            "Because I shoot my entire load straight into her mouth."
            with vpunch
            "And from what it feels like, straight down her throat too!"
            show amy bj eyesclosed gentle
            $ amy.love += 1
            "Amy begins to swallow as soon as it happens, gulping everything down."
            "Sure, she gags a little, but then she recovers and rides it out to the end."
            "Afterwards I can't say a word, let alone admit she was right all along."
            show amy bj eyeslust mouthcum up -cum -blow
            "But the knowing look of satisfaction on her face says it all."
        "Add more makeup to her face":
            "I have no idea how I manage to do it."
            "But at the very last moment, I pull my cock out of Amy's mouth."
            show amy bj eyeslust mouthpleasure up -blow
            "Her eyes pop open as I do so, but she doesn't look surprised."
            "In fact it's more like she's prepared for the eventuality."
            "And now she's putting an alternate plan into action."
            show amy bj mouthlust
            "Amy smiles happily as my cock bobs in front of her face."
            "And she makes no effort to move as the inevitable happens."
            show amy bj eyesclosed mouthpleasure cum with vpunch
            $ amy.love += 2
            "I shoot my load straight into her face a mere second later."
            show amy bj facecum with vpunch
            $ amy.sub += 1
            "The cum striped her nose, cheeks and mouth."
            with vpunch
            "Then it starts to run downwards towards her chin."
            show amy bj -cum
            "Afterwards I can't say a word, let alone admit she was right all along."
            show amy bj eyeslust mouthlust
            "But the knowing look of satisfaction on her face says it all."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
