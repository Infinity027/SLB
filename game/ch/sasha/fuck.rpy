init python:
    Event(**{
    "name": "sasha_pool_foreplay",
    "label": "sasha_pool_foreplay",
    "max_girls": 1,
    "conditions": [
        IsSeason(0, 1),
        HeroTarget(
            IsGender("male"),
            IsRoom("pool")),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 100),
            MinStat("sexperience", 1),
            ),
        ],
    "priority": 500,
    "do_once": False,
    "once_week": True,
    "chances": 25,
    "duration": 1,
    })

    Event(**{
    "name": "sasha_hottub_sex_male",
    "label": "sasha_hottub_sex_male",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("date_hot_tub_home"),
            HasStamina(),
            ),
        PersonTarget(sasha,
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

    InteractActivity(**{
    "name": "fuck_sasha",
    "display_name": "Fuck",
    "label": "ACTIVE_GIRL_fuck_ROOM",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            HasStamina(),
            ),
        IsTimeOfDay("evening"),
        PersonTarget(sasha,
            IsActive(),
            Not(HasCheated()),
            MinStat("love", 150),
            MinStat("sexperience", 2),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })

    InteractActivity(**{
    "name": "fuck_sasha_beach",
    "display_name": "Fuck",
    "label": "ACTIVE_GIRL_fuck_ROOM",
    "conditions": [
        IsHour(14, 18),
        HeroTarget(
            IsGender("male"),
            IsRoom("beach", "date_beach", "date_nudistbeach"),
            HasStamina(),
            ),
        PersonTarget(sasha,
            IsActive(),
            Not(HasCheated()),
            MinStat("love", 150),
            MinStat("sexperience", 2),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })

    Event(**{
    "name": "sasha_dom_cunnilingus_male",
    "label": "sasha_dom_cunnilingus_male",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("watch_tv_with_everyone_male"),
            HasStamina(),
            ),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            ),
        PersonTarget(sasha,
            IsPresent(),
            MinStat("love", 100),
            MinStat("sexperience", 1),
            MaxStat("sub", -50),
            ),
        PersonTarget("lexi",
            Or(
                Not(IsPresent()),
                IsHidden(),
                ),
            ),
        PersonTarget(minami,
            Or(
                Not(IsPresent()),
                IsHidden(),
                ),
            ),
        PersonTarget(samantha,
            Or(
                Not(IsPresent()),
                IsHidden(),
                ),
            ),
        ],
    "priority": 500,
    "do_once": True,
    "duration": 1,
    })

label sasha_pool_foreplay:
    scene bg pool
    if sasha.sexperience % 2 == 1:
        "It's been one of those days, too much work and stress, plus seriously hot weather."
        "The kind of day that makes me thankful we have a pool out back that I can use to unwind."
        "So as soon as the chance presents itself, I change into my trunks and head into the garden."
        "But as soon as I make it out there, I can hear the sound of splashing from the pool."
        "At first I feel more than a little annoyed."
        "It was my idea to come out and chill on my own."
        "Bit it looks like someone's beaten me to it."
        "Now I have to either wait for them to come out, or else share the pool!"
        mike.say "Urgh..."
        mike.say "What a fucking..."
        "My words fade away as I catch my first sight of just who beat me to the pool."
        scene bg black
        show swimmingrace sasha nomc
        with fade
        "And I watch in stunned silence as Sasha swims past me, a smile on her face."
        "She waves happily at me, but I'm more interested in staring at the rest of her."
        "Sasha's wearing a bikini, so almost everything is on show right now!"
        mike.say "What a siren!"
        "I hurry over to the edge of the pool as Sasha swims towards me."
        "And then I sit down as she pulls up beside me, leaning on her forearms."
        sasha.say "Looks like you had the same idea as me, [hero.name]!"
        sasha.say "You should jump right in and join me."
        sasha.say "The water's SO cool right now!"
        "I nod eagerly at Sasha's invitation."
        "All of my irritation has vanished by now."
        "And it's been replaced with sheer lust and the need to get closer to Sasha."
        mike.say "Great minds think alike, Sasha!"
        mike.say "Move over a little, will you?"
        mike.say "Then I can get in too."
        "Sasha nods and kicks back, pushing herself away from the side of the pool."
        play sound water_splash
        pause 0.2
        scene swimmingrace_bg_03 at center, zoomAt(1.75, (1000, 1040)), blur(5) with vpunch
        "As soon as there's room, I jump right, just like she told me to."
        "The water's a little colder than I anticipated."
        scene bg black
        show swimmingrace sasha nomc at center, zoomAt (2.5, (1600, 720)) with vpunch
        "So when I pop up, I'm gasping from the change in temperature."
        mike.say "Urgh..."
        mike.say "Whoa!"
        show swimmingrace sasha nomc at center, traveling (1.85, 10.0, (440, 840))
        sasha.say "[hero.name]!"
        sasha.say "Are you okay?!?"
        "Sasha seems to think that I'm in some kind of trouble."
        "As she swims straight over to me and grabbing hold."
        "And on pure instinct, I do the same."
        "Which leaves us clinging to each other was we float in the water."
        mike.say "I...I'm fine, Sasha!"
        mike.say "The water was just a little cold, that's all!"
        sasha.say "Oh!"
        sasha.say "Okay, okay...I see."
        mike.say "We should..."
        mike.say "We should probably let go of each other now!"
        sasha.say "Y...yeah..."
        sasha.say "I mean...you kind of have your hand between my legs right now!"
        scene sasha foreplay
        show sasha foreplay pool boxer
        with fade
        "Sheer surprise makes me move the hand in question."
        "Then I feel that Sasha's right - it's practically cupping her pussy right now!"
        "But the unconscious movement seems to only make things worse."
        sasha.say "Mmm..."
        sasha.say "Oh...oh fuck..."
        mike.say "I'm so sorry, Sasha!"
        mike.say "Let me just..."
        "As I make to pull my hand away, I feel Sasha's own hand grab my wrist."
        "Surprised again, I look her in the face, and she shakes her head."
        sasha.say "No..."
        sasha.say "Don't stop!"
        show sasha foreplay pleasure
        sasha.say "It feels SO good - and nobody can see!"
        $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_low.ogg", loop=True)
        "I stare at Sasha for a few seconds, too taken aback to do anything."
        "But then I start nodding eagerly."
        "And I set my fingers to work under the water."
        "I begin by taking full advantage of where my hand ended up."
        "Cupping Sasha's pussy means I can use my thumb to stroke the top."
        "And at the same time I can explore the folds of her lips with my other fingers."
        "So that's exactly what I get down to doing."
        "The material of her bikini doesn't stop me for a moment."
        "Instead the soft, stretchy lycra actually enhances it."
        "And I find that I can rub and squeeze pretty hard right from the start."
        $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_medium.ogg", loop=True)
        "Sasha keeps her arms wrapped around me as I play with her."
        "Clinging to me, I can feel how much she's getting off on this."
        "Because she only seems to be hanging on tighter with each passing second."
        "I keep on working Sasha's pussy through her bikini bottoms."
        "Going on instinct, I really don't have a plan for what to do next."
        "But luckily for me, my fingers soon begin to slip under the fabric."
        "All of a sudden I can feel the soft, sensitive skin of Sasha's pussy."
        $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_high.ogg", loop=True)
        "And it seems like the transition is something she feels too."
        show sasha foreplay up
        "Sasha nods, burying her head into my shoulder."
        "But she also reaches down and pushes my hand deeper still."
        "Spurred on by her actions, I start to explore with my fingertips."
        "Sasha moans with pleasure as they find their way inside of her."
        show sasha foreplay orgasm
        "And her pussy mirrors this by opening up at my attentions."
        "Soon enough, I'm tracing the inside of her lips."
        "Trying to be as gentle as I can, I inch Sasha onwards."
        "And with every twitch of my fingers, she quivers even more."
        "Finally I can feel her entire body stiffening under my touch."
        "So I make sure to support her in the water as the inevitable happens."
        "Sasha cums as she floats in the water, the thighs squeezing my hand."
        $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_orgasm.ogg", loop=True)
        show sasha foreplay pussycum
        "She hangs onto me the whole time, even once her orgasm is done."
        mike.say "Are..."
        mike.say "Are you okay, Sasha?"
        stop sound
        sasha.say "Mmm..."
        sasha.say "Better than okay..."
        sasha.say "I wanna fall asleep right here!"
        "Maybe that's not such a good idea."
        "But I'm happy to stay right there for the time being."
        "Just holding onto Sasha as she floats in the grip of the afterglow."
    else:
        "While it's not exactly rare that there's a window of nice weather or that I have some time off of work in which I can lounge about the house, it is rare that both occur on the same day."
        "And it's on those few and far between occasions that having a swimming pool of your own really comes into its own."
        "But of course, there's one other thing in my own life that probably puts it over the top in terms of warm weather and the pool."
        "Which is living with a couple of rather hot female housemates that are thinking about using it to cool off as well."
        "You'll just have to take my word for it when I say that I did come down to the side of the pool in my shorts just for a swim."
        scene bg black
        show swimmingrace sasha nomc
        with fade
        "I honestly had no idea that I'd be greeted with the sight of Sasha, already in the water and swimming the short length from one end to the other."
        "She doesn't see me at first, meaning that I have the chance to sit down on one of the sun loungers at the side of the pool and watch."
        "Again, I'm not just perving on her - seriously I'm not!"
        "Okay...maybe just a little."
        "But how bad mannered would it be to just jump straight in there without letting her know that I'm here?"
        "Surely the more gentlemanly thing to do would be to let her finish up swimming her lengths and then make myself known to her?"
        "Making sure to keep quiet, I settle down to watch Sasha's progress."
        if sasha.flags.boobjob:
            "I've never seen Sasha wearing the bikini that she has on today, but then she must have had to update her wardrobe since she got her implants anyway."
            "Myself, I've gotten used to them to the point where it's almost hard to imagine her with the petite chest that she had before the operation."
            "They also look to be no impediment in the water either, and I marvel again at the confidence and even happiness they seem to have given her."
            "In fact, they float so well in the water that I can't help but wonder if, were she to get in trouble, there's be any need for another flotation device besides them."
        if sasha.flags.haircut:
            "It's still weird to see Sasha's long, lustrous hair shimmering with blonde tones, rather than her natural black."
            "But as it stretches out behind her in the water, it seems to give her a more vital appearance than before."
            "To me at least, she looks more vibrant, more alive than ever before."
        if sasha.is_visibly_pregnant:
            "I'm amazed that Sasha can still get away with wearing a bikini at all, based on the curve of her belly and the size that her breasts are swelling to."
            "I doubt it'll fit her in a week's time, and she'll likely be forced to look for something more forgiving in the maternity section of wherever they sell clothes for pregnant Heavy Metal devotees."
            "But that's not to say that she doesn't look fantastic in the thing, all the same!"
            "Pregnancy has made her body bloom ever more as she's progressed through her term, and with the water supporting her, she reminds me of a reclining goddess."
        if not any([sasha.flags.boobjob, sasha.flags.haircut, sasha.is_visibly_pregnant]):
            "I know that the normal image of the bathing beauty is buxom and blonde."
            "But maybe that's why the sight of Sasha, with her black hair and alternative look turns me on so much."
            "Even while she's in the pool, she still has her usual dark, heavy eye-shadow and lipstick on, contrasting so well with her pale skin."
            "I can already see her petite breasts and their tiny nipples beneath the stretched material of her bikini top, stiff and upright from the cold of the water."
        "I don't know if Sasha's aware of me watching her as she swims, but it seems to me that she takes a lot longer about wrapping it up than she might otherwise have."
        "She keeps switching from one stroke to another, as if she knows full well that this will allow me to see almost every curve of her body as she moves through the water."
        "This means that by the time she finally does decide to come to a gentle stop and swim to the side of the pool, I have an enormous erection that's simply impossible to hide."
        sasha.say "Hey, [hero.name] - is that a mast in your pants, or are you just glad to see me?"
        "Oh yes, she definitely knew what she was doing and no mistake!"
        sasha.say "I think you should come join me in here?"
        sasha.say "Maybe see if there's anything I can do about it - seeing as how it was my fault!"
        "Not needing any more of an invitation than that, I stand up and awkwardly hurry over to the side of the pool."
        "My erection waggles embarrassingly in front of me, threatening to stretch the waistband of my short as I go."
        scene swimmingrace_bg_03 at center, zoomAt(1.75, (1000, 1040)), blur(5) with vpunch
        "I lower myself into the water and feel the initial chill spread through me, made worse by my current state of arousal."
        scene bg black
        show swimmingrace sasha nomc at center, zoomAt (2.5, (1600, 720)) with vpunch
        show swimmingrace sasha nomc at center, traveling (1.85, 10.0, (440, 840))
        "The water at this end of the pool only comes up to my chest, meaning that I'm able to stand up as Sasha swims the short distance between us."
        scene swimmingrace_bg_03 at center, zoomAt(1.75, (1000, 1040)), blur(5)
        show sasha kiss
        with fade
        $ sasha.flags.kiss += 1
        "Letting her legs find the bottom of the pool, she leans in close for a kiss that lingers pleasantly and I swear helps to acclimatise me to the cold water with surprising speed."
        "And it's right in the middle of the kiss that I can feel her hand stroking the front of my shorts, as if sizing up lies inside."
        "Once Sasha's found what she's looking for and had enough of a squeeze and a stroke to know that wants more, she doesn't simply slip her hand under the waistband."
        "Instead I feel a hand grip my shorts on both sides, pulling them down and letting them drop to the bottom of the pool."
        "I'm not concerned about being stripped of the one item of clothing that I was wearing."
        "I happen to be standing up to my chest in a pool that's located in my own back yard."
        "And even if If there were any chance of being seen, I have enough distraction in the form of Sasha for me to forget all about it in short order."
        "Her hand's got a good hold on my cock now, sliding up and down under the water."
        "There's no way that this is going to be any kind of dexterous hand-job, just a rough tug and pull."
        "But it hardly seems fair that I should be the only one getting this kind of treatment."
        "Especially when Sasha went to all that trouble just now to get me excited and then lure me into the water with her."
        "Still with my eyes closed as I kiss her, I reach out with one hand and grope for the inside of Sasha's thigh."
        scene sasha foreplay
        show sasha foreplay pool boxer up
        with fade
        "I find it without too much effort, noting the way she draws in a ragged breath in anticipation as I begin to walk my fingers upwards."
        "Her bikini bottoms are slight, little more than enough to preserve her modesty - not that I have any such thing in mind."
        "At first I restrict myself to gently stroking Sasha through the stretchy material, enjoying the sensation of what lies beneath."
        show sasha foreplay pleasure
        $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_low.ogg", loop=True)
        "The more that I tease her, the more I can feel the way that she reacts to it in the way her tongue probes my mouth and the vigour with which she rubs my cock."
        "And of course, this only encourages me to go further, pushing one of my fingers against the gusset of her bottoms so that it presses into her pussy beneath."
        "As hard as it is to tell if Sasha's ready for more whilst stroking her under the water, I feel only soft and welcoming sensations beneath my fingertips."
        "On the strength of this, I slip those same fingers under the material and begin to stoke at the naked lips of her pussy instead."
        $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_medium.ogg", loop=True)
        "Touching Sasha with nothing in between the tips of my fingers and her delicate folds makes her begin to melt almost instantly."
        "The only thing that gets harder is the hold that she has on my cock, as she grips the shaft and rubs now like her life depended on it."
        "At the same time as I start to push two of my fingers into her, one slow inch at a time, I can feel her less than gentle attentions finally pushing me to the end."
        show sasha foreplay pussycum
        $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_high.ogg", loop=True)
        "I try desperately to keep my fingers inside of Sasha and do the same in return, even as I know my cock is letting go beneath the water of the pool."
        $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_orgasm.ogg")
        show sasha foreplay orgasm
        "Luckily for me, it's not long after this that Sasha comes to the point where I was a moment before."
        "Feeling as though I've swum the same number of lengths as she did before we got to playing in the water, I climb out after Sasha and collapse back into my sun lounger."
        stop sound fadeout 0.5
        "As I lie there, I absently begin to think about just how often we have the pool cleaned, and if we might not want to think about doing it a little more often."
    $ sasha.love += 2
    return

label sasha_hottub_sex_male:
    $ CONDOM = False
    $ game.active_date.clothes = "swimsuit"
    show bg pool
    show hottub sasha
    with fade
    sasha.say "Why don't you jump in and join me?"
    "I open my mouth to refuse the offer, still set on my whim of this morning."
    "But then it hits me - why in the hell would I say no to that offer?"
    "After all, it's not like I have don't like getting closer to Sasha, is it?"
    mike.say "Sure, Sasha."
    mike.say "That sounds like a great idea!"
    "Sasha smiles as I walk over to the tub and start to climb in."
    "She scoots a little way over to make sure there's room for me."
    "But I note that she doesn't go as far away as she could."
    "Instead she settles only a little way from where I sit down in the water."
    "And there's no way that she can have failed to see how I'm looking at her right now!"
    "But how can you blame me for that?"
    "Sasha looks super hot in her swimsuit."
    "I could believe it's her making the water bubble, not the jets in the tub!"
    sasha.say "Like what you see, huh?"
    "She raises an eyebrow as she says this."
    "And then she giggles as I flush with embarrassment."
    mike.say "What..."
    mike.say "No...I mean yeah..."
    mike.say "I mean...you know what I mean!"
    sasha.say "Yeah, [hero.name], yeah."
    sasha.say "I'm pretty sure I know what you mean!"
    sasha.say "You wanted some time to chill out in the hot-tub."
    sasha.say "And here I am, forcing you to stare at my tits, right?"
    "I shake my head, starting to laugh too."
    mike.say "Okay, Sasha, you got me."
    "Sasha gives me a playful slap on the shoulder."
    "But then she leans in closer, becoming suddenly conspiratorial."
    sasha.say "Seeing as how you've had an attack of honesty, here's a little reward."
    sasha.say "I didn't just invite you in here to relax, [hero.name]."
    mike.say "Erm..."
    mike.say "You didn't?"
    sasha.say "No - I wanted to check you out too!"
    "Leaning in closer still, Sasha plants a kiss on my unsuspecting lips."
    "It's long, lingering and insanely passionate."
    "And as such, it's more than enough to let me know where she wants this to go!"
    show hottub sex male sasha outside with fade
    "Without saying a word, I pull Sasha onto my lap."
    "She offers no resistance, coming willingly and without protest."
    "And it's only when she's actually sitting in my lap that I realise what she's done."
    "Somehow, she managed to pull down my trunks while I was distracted."
    "Now Sasha has my cock in her hands, gripping it like a joystick."
    call sasha_dick_reactions from _call_sasha_dick_reactions
    "And she wastes no time in pointing it at a target between her thighs."
    "I gasp at the sensation, breaking the kiss."
    "But Sasha doesn't stop for a second."
    "She rubs the head against the lips of her pussy."
    show hottub sex male inside
    play sound "sd/moans/sasha/sasha_moans_light_low.ogg" loop
    "Once, twice...and then she sits down on it in one smooth motion."
    "The feeling is incredible, as Sasha uses her weight to force me into her."
    "And once I'm inside, she relaxes, letting gravity do all the work."
    "All I can do is sit back and let her take the lead."
    "Sasha does just that, rocking back and forth as she rides me."
    "I have her chest in my face, like a pair of thrusting, pink airbags."
    "And so I do the only thing that makes sense in the heat of the moment."
    "I push my face between them, burying myself in Sasha's cleavage."
    "This means that I can't see what's going on around me."
    play sound "sd/moans/sasha/sasha_moans_light_medium.ogg" loop
    "But I can hear the sounds that Sasha's making the whole time."
    "And I can certainly feel the way she's bouncing in my lap too!"
    "The water splashes and slaps at her buttocks as she rides me."
    play sound "sd/moans/sasha/sasha_moans_light_high.ogg" loop
    "Almost as loud as the moans of pleasure that she's making, but not quite."
    "She keeps on grinding herself against me ever harder."
    "Which means I begin to feel something else too."
    "I can feel that I'm going to cum!"
    call cum_reaction (sasha, 'vaginal', 1) from _call_cum_reaction_158
    if _return == "vaginal_outside":
        show hottub sex male outside
        "I lift Sasha higher and pull down my groin, making my cock slide out of her."
        play sound "sd/moans/sasha/sasha_moans_light_orgasm.ogg"
        queue sound "sd/moans/sasha/sasha_panting.ogg" loop
        "Sasha makes a sound that seems to be formed of desperation."
        with vpunch
        "And she tries her best to climb back onto my cock before the end arrives."
        show hottub sex male cumshot with vpunch
        $ sasha.sub += 1
        "But even as she does so, I shoot my load up and over her."
        with vpunch
        "The cum hits Sasha's ass and her lower back."
        "And then it runs down between her legs and into the water below."
    else:
        "I grab hold of Sasha's thighs, pulling her down onto me with all my strength."
        play sound "sd/moans/sasha/sasha_moans_light_orgasm.ogg"
        queue sound "sd/moans/sasha/sasha_panting.ogg" loop
        "She yelps in surprise, clinging to me tighter still, and that's all it takes."
        show hottub sex male cumshot with vpunch
        $ sasha.love += 1
        "I let go in one sudden surge, pumping everything I have into Sasha."
        show hottub sex male ahegao with vpunch
        "She bucks in my lap, trying to pull free before the sensation becomes too much."
        with vpunch
        "But I hold her in place, my limbs feeling like they're locked in place as I cum."
    hide hottub sex male
    show hottub sasha
    with fade
    "We fall back into the water then, both of us spent."
    mike.say "I...I thought we were...relaxing?"
    stop sound
    sasha.say "Speak for yourself, [hero.name]."
    sasha.say "But right now, all I can do is relax!"
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ sasha.sexperience += 1
    $ game.active_date.clothes = None
    return

label sasha_fuck_date_nudistbeach:
label sasha_fuck_date_beach:
label sasha_fuck_beach:
    $ game.play_music("music/roa_music/city_nights.ogg")
    scene bg black with dissolve
    pause 1.0
    scene bg livingroom with dissolve
    "I made up my mind to spend the day at the beach the very moment that I glanced out of the window this morning."
    "There's not a cloud in sight, all the way to the horizon and it's already getting crazily hot out there."
    "Add to that the fact that I'm off work today, and you have the perfect excuse to hit the sand."
    "But then I check my phone, noting the date, and I remember that I was already supposed to be doing something today."
    "Instantly I start racking my brain to recall what it could be."
    "Maybe if I'm lucky, I can pull it off quickly and still make it to the beach?"
    show sasha casual
    sasha.say "Hey, [hero.name]!"
    sasha.say "You ready to head off on our date?"
    sasha.say "I'm real excited to see where you're taking me!"
    "Shit, that's what I was supposed to be doing today!"
    "I said that I'd take Sasha out somewhere, kind of as a surprise."
    if sasha.flags.haircut:
        "I steal a guilty glance at Sasha's slutty hair and clothes."
        "What in the hell am I even worrying about?"
        "I'm sure she'd jump at the chance to go lounge on the beach in a revealing swimming-costume!"
    else:
        "I steal a guilty glance at Sasha's black clothes and pale skin."
        "Is the beach even her kind of place to go and spend the day hanging out?"
        "Wouldn't she prefer somewhere dark and atmospheric instead?"
        "Fuck sake - will she actually burst into flames if she's exposed to that much direct sunlight?"
    mike.say "I...I was thinking we might go to the beach."
    mike.say "That's if you're up for it, Sasha?"
    if sasha.flags.haircut:
        show sasha happy
        sasha.say "The beach?!?"
        sasha.say "Oh wow - yay!"
        show sasha at center, startle
        sasha.say "I just LOVE the beach, [hero.name]!"
        sasha.say "And just wait until you see the cute new swimsuit I have to wear too!"
        "Yeah, that reaction wasn't the biggest surprise of all time."
    else:
        "Sasha shrugs and gives the suggestion a quick nod."
        sasha.say "Sure - why not."
        mike.say "Really?"
        show sasha happy
        sasha.say "Yeah, really - I love the beach!"
        "Well, colour me surprised!"
    scene bg beach with fade
    "No more than an hour later, we're stepping out of my car in the parking lot at the beach."
    "Sasha keeps herself covered up with a sarong while we find a secluded spot to spread out our blanket."
    "Much as I try not to be the jealous type, I like that she does this."
    "It makes me feel like she's keeping herself for my eyes only, like I'm a little special."
    "Weird, I know - but I guess Sasha just has that effect on me."
    show sasha swimsuit with dissolve
    "Once we're all set up, she finally pulls loose the knot at her waist, letting the sarong fall away."
    "Sure, I've seen Sasha wearing less before now."
    show sasha b close swimsuit at top_to_bottom with dissolve
    "But there's just something so sexy about a hot girl in a swimsuit."
    "Every curve and line of Sasha's body is on show."
    "But there's still a sense of mystery thanks to that thin layer of skin-tight material..."
    show sasha b at bottom_to_top
    "Sasha lays herself down on the blanket, clearly aware of me checking her out."
    if sasha.flags.haircut:
        show sasha flirt
        sasha.say "You like what you see, [hero.name]?"
    else:
        show sasha annoyed
        sasha.say "Put your tongue back in, [hero.name]."
        sasha.say "Otherwise someone's going to trip over it!"
    "I nod my head at this, temporarily losing the power of speech."
    show sasha normal
    "Sasha gives me a satisfied smile, and then stretches out on the blanket."
    show sasha happy
    "She closes her eyes and appears to be intent on falling asleep, or at least zoning out in the sun."
    "I wait for a couple of moments, hoping that she's just teasing me."
    "But then it becomes apparent that she's really going to just lie there."
    "Lie there, practically taunting me with the sight of her incredible body spread out before me."
    scene bg beach at blur(16), dark, dark with wipedown
    "Determined not to become frustrated, I follow her lead and close my own eyes too."
    "But no matter how hard I try, it's impossible to relax with her laid that close."
    scene bg beach
    show sasha happy swimsuit
    with wipeup
    "In the end, I can only lie there and stare at Sasha, torturing myself with the sight of her."
    "Eventually I begin to lose track of time, my mind wandering off in random directions."
    "And so by the time Sasha finally begins to stir, I've been dwelling on my own mortality for quite some time."
    show sasha normal
    sasha.say "Oh...wow."
    sasha.say "I must have dropped off for a couple of minutes back there!"
    "I nod and smile, trying my best not to let on how bored and frustrated her napping has left me."
    if sasha.flags.haircut:
        show sasha joke
        sasha.say "Aww..."
        sasha.say "Sorry I left you all on your own, [hero.name]!"
        sasha.say "I think you deserve a little something to say sorry..."
    else:
        sasha.say "Mmm..."
        sasha.say "Falling asleep's left me feeling hungry, [hero.name]."
        sasha.say "How about you?"
    show sasha topless
    "As if she needs to underline the point, Sasha pulls down the straps of her swimsuit top."
    if sasha.flags.boobjob:
        "This releases her large, round breasts so that they bob heavily upon her chest."
    else:
        "This frees her pert, petite breasts so that they stand proud upon her chest."
    mike.say "Whoa..."
    mike.say "That's something I've always got an appetite for, Sasha!"
    show sasha happy
    "Sasha smiles at my enthusiasm and beckons me closer."
    "She pushes me down flat on my back, looming over me and putting her hands on my shoulders."
    "The first thing that I notice is just how warm her entire body feels."
    "It's as though she's held onto every bit of the sun's heat that's touched her skin."
    show sasha cowgirl beach swimsuit with fade
    "I reach down and begin to tug at Sasha's swimsuit bottoms, pulling them down her thighs."
    "She leaves the task to me until they reach her knees, and then kicks them off with ease."
    "All that remains is to hastily pull off my own shorts, and then we're both naked."
    "Of course, my cock needed no encouragement to become as stiff as a board."
    "But what surprises me is just how slick Sasha's pussy feels when the tip brushes its lips for the first time."
    "She can't have gotten that wet in the few short moments since she opened her eyes and wanted to get frisky."
    "So she must have been awake for a good while before that, getting excited at the thought of doing just this."
    "As usual, the knowledge of just how horny she is makes me all the more into it myself."
    show sasha cowgirl pleasure
    $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_low.ogg", loop=True)
    "And so I don't waste another moment, pulling her down onto me in one smooth motion."
    "Sasha, it seems, is every bit as ready and willing as her pussy right now."
    "I slide into her without the smallest hint of resistance, sinking in until I'm balls deep."
    "Her entire body seems to yield to me in the exact same manner."
    "Legs parting, belly and breasts pressed against me, lips wet against my throat."
    "Maybe it's the heat of the day and the fact that we're laid under the baking sun."
    "Or maybe I just want to be able to savour every moment of this intimacy with Sasha."
    "But either way I find myself going slowly as I begin to move in and out of her."
    "Sasha's body feels so soft above me, and the release of being inside her is something to take time over."
    $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_medium.ogg", loop=True)
    "And she seems to have the same exact sentiment as I do too."
    "Because all I can hear from Sasha as I make long, lingering thrusts into her, are moans of approval."
    "By now, it's getting hard to tell if the slickness of my thighs is from sweating or Sasha herself."
    "But it's certainly sweat that's making her breasts slip and slither around above me."
    if sasha.flags.boobjob:
        "Those massive orbs are squeezed between our chests."
        "Making me feel like I'm laid beneath a pair of bouncy, wobbling balls."
    else:
        "Those palm-sized orbs are pressing against me the whole time."
        "And I can feel the stiff little nipples rubbing against me."
    "But as pleasant as this moment is, there's no way it can last forever."
    "And all too soon, I feel that I'm about to cum."
    $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_orgasm.ogg", loop=True)
    show sasha cowgirl ahegao cum with vpunch
    "It happens as gently and deeply as the rest of the encounter has, Sasha responding in kind too."
    with vpunch
    "We finish without saying a single word, our bodies slick with each other's sweat."
    "After that, there's nothing to do save lay back on the blanket."
    "And so we do just that, happy to let the sun and the warm sea breeze dry our naked bodies."
    stop sound
    hide sasha
    $ sasha.sexperience += 1
    return

label sasha_fuck_bathroom:
    $ game.play_music("music/roa_music/city_nights.ogg")
    scene bg bathroom
    show sasha naked blush
    $ renpy.sound.play("sd/shower.ogg", loop=True)
    "She's already standing under the cascading water by the time I'm finally naked, and I watch it run in rivulets over her body."
    "Sasha's hair quickly becomes a mane of soaked tendrils that surround her pale features."
    "The water trickles over her milk-white skin, making her breasts and slender legs all the more alluring to the eye."
    "I take a deep breath and step into the shower, feeling the water begin to rain down on me too."
    if Harem.together(bree, sasha, name='home') and Room.has_tag(bree.room, 'home') and not bree.hidden:
        show sasha at left
        show bree at right
        bree.say "Can I join in?"
        menu:
            "Yes":
                mike.say "That would be great."
                call home_harem_bree_sasha_shower from _call_shower_ffm_1
                $ bree.love += 2
                $ sasha.love += 2
                $ sasha.lesbian += 1
                $ bree.lesbian += 1
                $ sasha.sexperience += 1
                $ bree.sexperience += 1
                return
            "No":
                $ bree.love -= 2
                mike.say "Sorry, I wanna be alone with Sasha a little."
                hide bree
                show sasha at center with move


    if sasha.is_sex_slave:
        "Sasha waits patiently for my instruction, hands clasped behind her back."
        "I take hold of her leash and give it a gentle but firm tug, pulling her downwards."
        "In response, she nods eagerly, and begins to lower herself onto the floor of the shower."
        show shower bj breesasha sasha up with fade
        "My cock instantly begins to stiffen at the sight of Sasha's unquestioning obedience."
        "That means it stands proud and ready to greet her almost as soon as she's in position."
        "And once she is, Sasha doesn't need to be told what's expected of her."
        show shower bj breesasha sasha shoot
        "Without a moment's pause, she takes my cock into her mouth and begins to lick and suck with unrestrained enthusiasm."
        "Sasha's hands are still clasped behind her back and her eyes are closed as she works on me, as if to close out the rest of the world from her senses."
        "I watch the water soaking her and running over her features, wondering that it does nothing at all to distract her from the task she has been set."
        "Were I just to leave her to it, I have no doubt Sasha would bring me off sooner, rather than later."
        "But a firm tug on her leash lets her know that I have other things in mind."
        $ sasha.flags.showerbj = True
    elif sasha.sub <= -50:
        "Sasha has a lascivious smile on her face as she catches my eye and points downwards, drawing my attention to the point between her legs."
        show sasha close b naked flirt at top_to_bottom
        "There's no question as to just what she wants, and I hurry to get down on my knees and position myself just so."
        "Placing a hand on each of Sasha's thighs, I begin to lick gently at the outer edges of her pussy."
        "I can feel the familiar folds of her outer lips and the prickle of where she's shaved."
        "But the constant flow of water means that it's hard to smell her scent or taste the unique flavour of her like I'm used to."
        "Only when I begin to venture further in, exploring the inside of her lips, that I begin to feel the comforting tingle of Sasha on my tongue."
        "A moment later, the water dilutes the taste and then washes it away almost completely."
        "Not to be deterred, I respond by pushing my tongue yet deeper into Sasha's pussy, perhaps reaching an inch or two inside."
        $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_medium.ogg", loop=True)
        "Though almost all of my attention is focused on what my mouth is doing, I can still hear her moaning in approval at my efforts."
        "A moment later, I feel Sasha lean against the wall of the shower, holding herself up and pushing her groin further towards me."
        "This exposes her clit to me, and I waste no time in making it the centre of my attention."
        "Sasha's legs start to tremble, and I hear her gasping now."
        stop sound
        sasha.say "Yes...yes, [hero.name]..."
        sasha.say "That's it...that's right..."
        sasha.say "Make me...cum!"
        hide sasha
        show sasha b naked blush at center, zoomAt(1.5, (640, 1000)), vshake
        $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_orgasm.ogg")
        "Perhaps a second or two later, Sasha casts her head back and makes a sound that tell me I've done just that."
    else:
        "Sasha treats me to a mischievous grin as she lowers herself down onto her knees before me."
        show shower bj breesasha sasha up with fade
        "She places a hand on each of my thighs, and begins to use only her lips and tongue to tease me fully erect."
        "Soon enough my cock is standing to attention, having done so whilst in Sasha's mouth."
        show shower bj breesasha sasha shoot
        "This means that we ease from foreplay and into the actual blowjob almost seamlessly, my pleasure increasing accordingly at the same time."
        "The combination of the warm water washing over me and Sasha's attentions is quite a combination."
        "The former feels like it's bringing my body to life from the outside."
        "While the latter is touching me on the inside in much the same manner."
        "It's then that I realise I don't want to cum just yet, I want to be inside of Sasha before I do!"
        "Gently and with care not to startle her for the safety of my own private part, I pull my cock out of Sasha's willing mouth."
        $ sasha.flags.showerbj = True
    hide shower bj
    hide sasha
    show sasha b naked blush at center, zoomAt(1.5, (640, 1000))
    with fade
    $ renpy.sound.play("sd/moans/sasha/sasha_panting.ogg", loop=True)
    "Soon enough, we're both back on our feet and panting a little from the combination of the heat and the things that we were doing to each other a moment before."
    "But I can feel that I'm not done yet, and from the look in her eyes, neither is Sasha!"
    hide sasha
    show sasha showersex
    with fade
    if sasha.is_sex_slave:
        "Taking Sasha's leash in one hand and roughly grabbing one of her buttocks in the other, I pull her towards me without warning."
        "She doesn't resist for a moment, instead letting herself be dragged forwards without much effort."
        mike.say "Sasha, get on my cock - NOW!"
        sasha.say "Yes, [hero.name], right away."
        "Sasha takes my erect dick in both hands, guiding it into herself with a great deal of care and attention."
        "I hardly have to move a muscle as she inched herself forwards, doing almost all of the work."
        $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_low.ogg", loop=True)
        "But the feeling is sensational all the same, and I'm happy to sit back and let Sasha earn her keep."
        "She moans and sighs in a way that makes the whole thing that much more enjoyable, as she rides my cock."
        "All the time Sasha uses her one free hand to massage her breasts and squeeze her own nipples."
        "I can see them bouncing up and down as her breasts move in time with the rest of her body."
        "Water from the shower runs over them and they send droplets splashing away as they go up and down."
        "I could reach out and touch her right now, but I'm enjoying having her service me too much."
        "My ultimate desire is to remain as still and impassive as I can possibly manage, letting Sasha do all of the work."
        "The effort that's taking and the demands it's making on her are clear to see in her flushed cheeks and how she's panting for breath."
        "But she doesn't complain or as much as pause for a single moment."
        $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_medium.ogg", loop=True)
        "I can't tell whether it's the sensation of Sasha wearing herself out on my cock, or the degree to which I seem to have her trained."
        "But either way I can feel that she's on the brink of bringing me off any moment."
        with vpunch
        "Only now do I take a firm hold of Sasha, keeping myself inside of her as I begin to cum."
        with vpunch
        "I have no idea if she's cumming herself, even when her sighs and moans fill my ears."
    elif sasha.sub <= -50:
        "Sasha grabs my dick and squeezes it without a second pause to think how much it hurts me."
        "Still gripping it tight, she pulls me closer to her."
        sasha.say "My pussy's still hungry, [hero.name]."
        sasha.say "Feed your cock to it - right now!"
        "I rush to obey her, fumbling for her lips even before she's managed to spread her legs wide enough."
        "I don't know if she's amused more by my eagerness or how inept it makes me."
        $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_low.ogg", loop=True)
        "But I can hear Sasha laughing even as I finally find my way and thrust myself into her."
        "I know that there's nothing to be gained from objecting to her laughter which comes at my expense."
        "And so the only option open to me is to make her stop by other means."
        $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_medium.ogg", loop=True)
        "Now that I'm as deep into her as I can go, I begin to pound away on Sasha as hard as I'm able."
        "The tone in which she demanded that I fuck her was strident and firm."
        "So I'm determined to give her what she's asked for in a similar manner."
        "I can tell that she's not prepared for me to be so forceful, as she almost immediately begins to yelp and cry."
        "But she can't object to what I'm doing, as it'd be tantamount to admitting that it's too much for her to bear."
        sasha.say "Ah, [hero.name]...pull out...before you cum inside of me!"
        "Damn it - a direct order!"
        "I do as I've been told, pulling out and letting Sasha go."
        "To my surprise, she immediately grabs my dick a second time and begins to rub it mercilessly."
        sasha.say "Rub my clit...get me off..."
        "I swear that she almost says 'please'."
        "But I would have obliged her willingly, whether she said the word or not."
        $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_orgasm.ogg", loop=True)
        with vpunch
        "So stroking each other into a state of ecstasy, we keep on until the end finally comes."
        with vpunch
        "Sasha almost screams as she leans against me for support, and my cum spatters onto her belly before being washed down the inside of her legs."
    else:
        "Sasha leans her back against the tiled wall of the shower cubicle, at the same time pushing her groin out towards me."
        "I don't need a written invitation to know what she wants of me, and I close the space between us as quickly as I can."
        "With my hand holding onto the underside of Sasha's thighs, I pull her the last few inches towards me."
        "She reaches down to direct traffic, taking my cock in both hands and steering it home."
        $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_low.ogg", loop=True)
        "Wet and more than willing for what we both have in mind, the feeling as I slide into Sasha's pussy is as smooth as silk."
        "But that same wetness makes it that much harder to keep a firm grip on her."
        "And I feel my hands clutching handfuls of her firm thighs in an effort not to lose my hold on her."
        "Sasha seems to sense this danger too, wrapping her hands hastily around my waist and pressing herself against me."
        $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_medium.ogg", loop=True)
        "This adds a terrible sense of desperation to what we're doing, as if we're afraid of slipping and being separated at any moment."
        "I feel as though each and every thrust that we manage to pull off is as much thanks to us clinging to each other as it is to us staying on our feet."
        "This intensity only serves to make the experience all the more powerful for me, and I can already feel my peak approaching."
        mike.say "Sasha...I'm gonna cum!"
        stop sound
        sasha.say "Okay, okay...let me down as slow as you can."
        sasha.say "Just don't drop me!"
        stop sound
        show shower bj breesasha sasha shoot with fade
        "I do my best to help Sasha's descent, so that she slithers off of my cock and onto her knees in the bottom of the shower."
        show shower bj breesasha sasha shoot cumshot with hpunch
        "A moment later, I lose it and shoot all that I have straight into Sasha's face."
        show shower bj breesasha sasha up -cumshot facial with hpunch
        "I watch as the cum spatters across her features, and is quickly washed away by the falling water."
    scene bg bathroom
    show sasha naked
    with fade
    stop sound
    $ sasha.flags.showersex = True
    "It's only thanks to the water from the shower head that Sasha and I manage to make it out of the bathroom less filthy than when we first came in."
    "All of the sweat and other bodily fluids have been washed down the drain, but the evidence of it all is clear as we walk out exhausted and still short of breath."
    $ sasha.love += 1
    $ sasha.sexperience += 1
    return

label sasha_fuck_livingroom:
label sasha_fuck_kitchen:
label sasha_fuck_pool:
label sasha_fuck_bedroom1:
label sasha_fuck_bedroom2:
label sasha_fuck_bedroom3:
label sasha_fuck_secondfloor:
label sasha_fuck_home:
    $ game.play_music("music/roa_music/city_nights.ogg")
    show sasha
    mike.say "Hey, wanna come and have fun in my bedroom?"
    sasha.say "Sure."
    if Harem.find(sasha, name='home'):
        call home_harem_fuck_choices ('sasha') from _call_home_harem_fuck_choice_1
    else:
        call sasha_fuck_date_male from _call_sasha_fuck_date_5
    return

label sasha_fuck_date_male(location="hero"):
    $ renpy.dynamic(
        sasha_strap=False,
        sasha_beads=False,
        sasha_ropes=False,
        sasha_cunni = False,
        sasha_ballgag = False,
        sasha_naked = False,
    )
    $ CONDOM = False
    $ game.play_music("music/roa_music/city_nights.ogg")

    if "sasha_event_01" in DONE and sasha.love >= 60 and ("sasha_event_03" not in DONE or ("sasha_event_03" in DONE and game.week_day % 5 == 0 and not Room.has_tag(game.room, 'home'))):
        call sasha_event_03 from _call_sasha_event_03
    $ game.room = "bedroom1"
    scene bg bedroom1
    show sasha


    call sasha_fuck_date_intro_male (location) from _call_sasha_fuck_date_intro_male


    call sasha_dick_reactions from _call_sasha_dick_reactions_1


    call sasha_fuck_date_foreplay_male from _call_sasha_fuck_date_foreplay_male

    call handle_npc_leaving (sasha, _return, from_foreplay=True) from _call_handle_npc_leaving_23
    if _return:
        return



    call sasha_fuck_date_choices_male from _call_sasha_fuck_date_choices_male_1

    scene bg bedroom1
    if sasha_strap or sasha_ropes:
        if sasha_strap:
            show sasha strapon
        if sasha_ropes:
            show sasha rope
    else:
        show sasha naked


    call handle_npc_leaving (sasha, _return) from _call_handle_npc_leaving_24
    if _return:
        return


    hide sasha
    call sasha_sleep_date_fuck (location) from _call_sasha_sleep_date_fuck_1
    return

label sasha_fuck_date_intro_male(location="hero"):
    if not sasha.sexperience:
        show sasha underwear at right with moveinright
        "The door to my bedroom opens, and I swallow audibly as Sasha slides around it."
        "She has on a matching set of slinky, black lingerie that looks like it only comes out on special occasions."
        "As she pushes the door closed behind her using her backside, it occurs to me that this must a very special occasion indeed."
        "And it's the thought that Sasha's doing all of this for my sake, as much as the sight of her, that makes my cock begin to stir with life."
        show sasha shout
        sasha.say "Someone looks pretty pleased to see me!"
        show sasha normal
        "There's a distinct purr to Sasha's voice, seductive and with a promise of dark humour."
        menu:
            "Admit it":
                "I realise that she's looking down at the growing bulge in my shorts."
                mike.say "Erm...yeah, shouldn't I be?"
                show sasha happy at right, startle
                "Sasha shakes her head and chuckles."
                show sasha shout
                sasha.say "Aw, [hero.name]...you're so cute when you get all ruffled and defensive!"
                show sasha underwear normal at center with ease
                "She shakes her head as she sashays across the room towards me."
                "I try to mumble something in my defence."
                "But all I can do is stare in silence as I see Sasha's body through the thin veil of her underwear."
                show sasha shout
                if sasha.flags.mikeNickname:
                    sasha.say "It gratifies me to see that you're happy, [hero.name]."
                else:
                    sasha.say "It's best for the both of us when you're happy..."
                show sasha foreplay underwear boxer with fade
                "She reaches out and caresses my cock through the thin fabric of my boxers, nudging at the parting of the fly so the head of my cock slips free."
                sasha.say "Very happy."
                $ sasha.love += 1
                $ sasha.sub -= 1
            "Taunt her" if hero.charm >= 25:
                mike.say "Would you like me to show you just how happy you're making me right now?"
                "I can't help flashing a cheesy grin at Sasha, and she smiles in return."
                "I can feel her eyes eating me up, and it's particularly nice to see them linger over my growing erection."
                show sasha underwear at center with move
                "But then she's making a fine showing of her own, almost posing in her flimsy underwear."
                "I'm supposed to be the one teasing her, but there's no way I can stop my cock from getting ever harder for her."
                if sasha.flags.mikeNickname:
                    sasha.say "Shall we see how much happier I can make you, [hero.name]?"
                else:
                    sasha.say "Let's see if I can't make you even happier..."
                $ sasha.love += 1
                $ sasha.sub += 1
    else:
        $ rand_intro = game.days_played % 5
        if rand_intro == 0 and hero.sexperience >= 20:
            call sasha_fuck_date_cunnilingus_intro from _call_sasha_fuck_date_cunnilingus_intro
            call sasha_fuck_date_cunnilingus from _call_sasha_fuck_date_cunnilingus
            $ sasha_cunni = True
            $ sasha_naked = True
        elif rand_intro == 1 and sasha.sub < 25:
            scene bg livingroom
            show sasha
            with fade
            "Sasha's been pretty coy with me all night, keeping me in suspense as to what would happen when we got back to the house."
            "As we live under the same roof, it's not exactly a case of 'your place or mine'."
            "More a case of 'your room or mine', if you know what I mean?"
            "And she keeps it up right until the last possible moment, leading me through the house by the hand."
            scene bg secondfloor
            show sasha annoyed
            with fade
            "Sasha makes a point of pausing in front of the door to her own room, as if pondering her options."
            show sasha normal
            "She notes the look of mixed anticipation and concern on my face, smiling with evident glee."
            "Her hand hovers over the door-handle for a moment, and my heart sinks."
            "Any moment I expect her to announce that she's had a long, tiring day and just wants an early night."
            show sasha happy at center, startle
            "But then Sasha lets out an evil giggle, and suddenly yanks me onwards."
            show sasha normal
            "She passes her door and doesn't stop until she reaches mine."
            show bg bedroom1 with fade
            "Once there, she pushes it open and then pushes me inside before I know what's happening."
            "Sasha leans against the door, making it slam shut behind her."
            show sasha kiss with fade
            $ sasha.flags.kiss += 1
            "And then she practically leaps forward, wrapping her arms around my neck."
            "She's kissing me then, deeply and with a hell of a lot of passion."
            "And that's not something that I'm about to fight!"
            if not sasha.flags.boobjob:
                "So I return the gesture, pulling her close to me and enjoying every moment."
            else:
                "So I return the gesture, feeling the orbs of her huge breasts squashing against my chest."
            hide sasha kiss
            show sasha at center, zoomAt(2.0, (640, 1340))
            "When the kiss comes to and end, Sasha stays huddled close, smiling up at me."
            sasha.say "Mmm..."
            show sasha shout
            sasha.say "Definitely your place tonight!"
            show sasha b joke
            sasha.say "Don't ya think?"
            show sasha normal
            "I nod eagerly, unable to keep from glancing over my bed."
            "Sasha raises her eyebrows in amusement, looking after me."
            show sasha shout
            sasha.say "What's that you say, Lassie?"
            sasha.say "Is someone in trouble over by the old [hero.family_name] bed?"
            show sasha normal
            "I can't help blushing a little at the implication that I have something in common with a Collie."
            mike.say "Ha, ha, ha - very funny, Sasha."
            mike.say "I can hardly help it if you bring out the animal in me..."
            "And with that I begin to make a comical snarling sound, pretending to stalk her like a hungry beast."
            show sasha happy
            "Sasha yelps in mock fear, more than willing to play the part of the damsel in distress."
        elif rand_intro == 2:
            scene bg black
            show bg bedroom1
            with fade
            "Once we're safely behind the closed door of my bedroom, I turn around slowly."
            "Not because I don't want to see Sasha standing behind me, you understand."
            "But because I want to savour the moment when I finally do knowing what we're going to get up to."
            "And when I finally do lay eyes on her, it's more than worth the wait."
            "That's because Sasha's used the its given her to begin stripping off in anticipation."
            show sasha underwear
            "I catch sight of her just in time to see the last of her clothes come off."
            "And so she's standing there in nothing more than her panties and bra."
            mike.say "WHOA!"
            show sasha happy
            "Sasha smiles and shakes her head at my reaction to the sight of her."
            "Clearly flattered and more than a little turned-on by the effect it's having on me."
            if sasha.sub >= 25:
                if sasha.flags.mikeNickname:
                    sasha.say "Do you like what you see, [hero.name]?"
                else:
                    sasha.say "Do you like what you see, Master?"
            elif sasha.sub <= -25:
                sasha.say "Well, are you just going to stand there staring at me, or what?"
            else:
                sasha.say "[hero.name], you're making me blush!"
            "I'm getting so aroused by Sasha that I can't actually force myself to answer her."
            "So I let my actions do the talking for me as I begin to tear off my own clothes."
            "And by the time I make it over to where she's standing, I'm totally naked."
            "My hands reach behind Sasha's back and begin to fumble with the catch of her bra."
            "At the same time I can feel her reaching down to tug at the waistband of her panties."
            show sasha naked
            if sasha.flags.boobjob:
                "In the next few seconds her huge breasts bounce free and the panties are kicked off."
            else:
                "In the next few seconds her petite breasts bounce free and the panties are kicked off."
            "I can feel Sasha's nipples, brushing against my chest as they start to harden."
            "And the tip of my cock is already high enough to brush against her too."
            $ sasha_naked = True
        elif rand_intro == 3:
            scene bg bedroom1
            with fade
            "By the time I have the door to the bedroom closed, I'm literally fighting to control my own excitement."
            "Because I've been looking at Sasha with longing and desire all night, wanting desperately to get my hands on her."
            "And now it seems like I'm finally going to get what I want, and I'm hoping that it's what she wants too."
            "So I have to fight the urge to close my eyes as I turn around, afraid all of this might turn out to be an illusion."
            "That I might wake up suddenly and realise that it's just a dream, sent to torment my poor, horny soul."
            mike.say "Erm..."
            mike.say "So, Sasha..."
            mike.say "I take it that we're going to..."
            show sasha naked with dissolve
            "I stop in mid flow, the words dying in my throat as I see what's actually in front of me."
            "Because in the time it's taken me to close the door, Sasha's managed to strip-off all of her clothes."
            $ sasha_naked = True
        else:
            "Most of the trepidation that I felt the first time that Sasha and I sneaked into my room to do this has vanished."
            "All that remains now is the same thrill that I can recall feeling at the prospect of getting to mess around with her."
            show sasha flirt
            "I guess that Sasha's feeling pretty much the same way as I am too, judging from the look of anticipation on her face."
            "It's that perfect combination of sexy and wicked that makes her so different from most of the girls I've met."
            "As well as the fact that I already know she's a totally kinky freak under the covers as well!"
            "I never seem to know just what she'll want to get up to next, or what reaction she'll inspire in me when she does so."
    return

label sasha_fuck_date_foreplay_male:
    if not sasha_cunni:
        call sasha_fuck_date_foreplay from _call_sasha_fuck_date_foreplay
        $ sasha_naked = True
    menu:
        "Ask for a rimjob" if hero.sexperience >= 10 and sasha.sub <= -25:
            call sasha_fuck_date_rimjob from _call_sasha_fuck_date_rimjob
        "Ask for a handjob" if sasha.sub <= 0:
            call sasha_fuck_date_handjob from _call_sasha_fuck_date_handjob
        "Fuck her tits" if sasha.flags.boobjob and hero.sexperience >= 10 and sasha.sub >= 25:
            call sasha_fuck_date_titfuck from _call_sasha_fuck_date_titfuck
            $ sasha.sub += 1
        "Eat her pussy" if not sasha_cunni and hero.sexperience >= 20:
            "I lie Sasha back against the pillows and lower my head towards her pussy."
            call sasha_fuck_date_cunnilingus from _call_sasha_fuck_date_cunnilingus_1
        "Use the anal beads" if "anal_beads" in hero.inventory and sasha.sub >= 0:
            call sasha_beads_play from _call_sasha_beads_play
            if _return:
                return _return
            $ sasha.flags.anal = True
            $ sasha_beads = True
        "Use the rope" if "bondage_ropes" in hero.inventory and hero.has_skill("shibari") and sasha.sub >= 25:
            call sasha_bondage_sex from _call_sasha_bondage_sex
            if _return:
                return _return
            $ sasha_ropes = True
        "Just fuck her":
            return
    call stop_all_sfx from _call_stop_all_sfx_36
    return

label sasha_fuck_date_choices_male(from_event=False):
    if sasha.sub <= -25 or game.flags.sashastrapon and not from_event:
        call sasha_strap_fuck from _call_sasha_strap_fuck
        if _return != "leave_without_gain":
            return
    menu:
        "Use the rope again" if sasha_ropes:
            call sasha_bondage_sex_second_round from _call_sasha_bondage_sex_second_round
        "Missionary":
            call sasha_fuck_date_missionary (0) from _call_sasha_fuck_date_missionary
        "Cowgirl" if hero.sexperience >= 10:
            call sasha_fuck_date_cowgirl (10) from _call_sasha_fuck_date_cowgirl
        "Standing" if hero.sexperience >= 15:
            call sasha_fuck_date_standing (15) from _call_sasha_fuck_date_standing
        "Doggy" if hero.sexperience >= 20:
            call sasha_fuck_date_doggy (20) from _call_sasha_fuck_date_doggy
    call stop_all_sfx from _call_stop_all_sfx_37
    if _return:
        return _return
    return

label sasha_strap_fuck:
    if not game.flags.sashastrapon:
        sasha.say "How about we try something new?"
        menu:
            "No":
                mike.say "Ah, maybe not tonight..."
                sasha.say "Huh...too bad, you'll never know what you're missing."
                return "leave_without_gain"
            "Yes":
                mike.say "Oh yeah - just what did you have in mind?"
                show sasha shout
                sasha.say "Well, I was wondering if you fancied taking it up the ass tonight?"
                show sasha normal
                with vpunch
                mike.say "You wondered WHAT?"
                "I heard her loud and clear - I just feel the need to make my feelings known, loud and clear."
                "But still, I can't deny that I'm intrigued."
                "A part of me does wonder what it would feel like..."
                show sasha shout
                sasha.say "I wondered if you'd let me use a strap-on, that's all."
                show sasha normal at center, zoomAt(2.0, (640, 1340))
                "Sasha leans over me, stroking my chest and stomach with one hand."
                show sasha shout
                sasha.say "I promise it won't hurt."
                sasha.say "Who knows - you might just find that you like it."
                sasha.say "And it'd make me real happy too..."
                show sasha normal
                "I'm in two minds, right up until the moment that she puts on a pout, thrusting out her lower lip."
                mike.say "Ah...alright!"
                $ game.flags.sashastrapon = True
    else:
        show sasha shout
        sasha.say "You want me to use the strap-on?"
        sasha.say "Fuck you like a little bitch?"
        show sasha normal at center, zoomAt(2.0, (640, 1340))
        "Sasha leans in close, running her hand over my chest and down my stomach."
        show sasha shout
        sasha.say "Come on - you know you want to..."
        show sasha normal
        "And then she pouts, which is seriously unfair!"
        menu:
            "No":
                mike.say "No, Sasha - not tonight."
                show sasha shout
                sasha.say "That's too bad."
                sasha.say "You don't know what you're missing."
                show sasha normal
                return "leave_without_gain"
            "Yes":
                mike.say "Okay, okay - let's give it a try."
    hide sasha
    show sasha
    "I'm nervous as I lay down on the bed. Nervous, but excited; my cock is already standing tall and hard for Sasha, who smirks down at me."
    show sasha flirt
    sasha.say "Come on.. you know the position, [hero.name]."
    show sasha normal
    "I do."
    "I draw my knees up to my chest and spread my thighs."
    "It's the most vulnerable I've ever felt with a woman and for a moment I nearly change my mind..."
    show sasha a naked
    "She stands at the edge of the bed, stark naked and looking so hot."
    show sasha a strapon with dissolve
    "She's strapped her toy on, black vinyl bands making stripes along her pale skin."
    "From the pelvis protrudes a pink cylinder with a rounded top; I know that it's got some give to it, and that it vibrates."
    "I can't imagine how that's going to feel."
    "Sasha pours some lube into one hand and starts stroking that pink toy as she climbs onto the bed with me."
    hide sasha
    scene sasha strap
    with fade
    "Once she's settled between my spread legs, she reaches out with her other hand to grab my cock and start stroking me with the same rhythm."
    "I was already hard, but this just turns me on more."
    "Shivering, I grasp the backs of my thighs with each hand to keep my legs apart for her, knees drawn up so she has easy access to my backdoor."
    "Her hand drops from that toy --which is looking larger by the moment as anticipation and nervousness grows-- and I feel lube-slicked fingers circling around my anus, spreading that slippery fluid and teasing at sensitive skin."
    "To my surprise, it sends a little shiver up my spine; it feels good, especially with the slow and steady way she's stroking my cock."
    "Sasha takes her time lubricating my asshole before slipping a finger slowly in."
    "It makes me tense at first, but she strokes my dick harder and I relax with a sigh."
    "She slowly pushes that finger in, then pulls it back out, rubbing the heated walls of flesh."
    "I slowly get used to the sensation, even squirming a little when she slows down for a moment."
    "Moving her hand briefly from my cock makes me grunt in protest."
    "She dips her hand in the front of the strap-on rig and suddenly there's a buzzing sound and Sasha gasps, then laughs in a sensual manner."
    "She must be getting that vibration too..."
    "That makes it hotter, knowing that she'll be feeling that hum constantly, having it press harder as she uses that toy on me."
    "Which starts surprisingly fast; she rests it atop my balls and I nearly jump out of my skin at the sensation!"
    "I've never played with vibrators on myself before, and the sensation is incredible! "
    "I can feel it tingling all the way through me, and a drop of pre builds up quickly, then drips down the underside of my dick."
    "Before it can hit my balls, Sasha's hand is wrapped around my cock again, slowly stroking."
    sasha.say "Ready?"
    "With the way my cock is twitching, I'm beyond ready. As long as I don't think too hard about it."
    "Not trusting my voice, I just nod."
    show sasha strap
    "It hurts just a little at first, I think mostly because I was expecting it to."
    "Sasha slides the rounded tip in, guiding her toy carefully with one hand while the other continues stroking my rod and the ache gives way to pleasure."
    "She starts to rock her hips back and forth, leaning back and propping herself up on one hand so she can balance with her body on sexy display just for me."
    "I love the way her small, firm tits sway as she moves, pushing the toy just an inch or so in, then back out, giving my body time to get used to this."
    "Soon enough, I'm groaning and more pre is dribbling down my dick, getting her hand sticky."
    "Good thing she likes her sex messy."
    "Bit by bit, she inches closer to me, which ever-so-slowly pushes this humming toy deeper into my ass."
    "The vibrations are just incredible, almost too much for me to take, but by the way she's moaning, she'll wind up getting off on it."
    "Finally, my spread ass is between her thighs and only an inch or two of her fake phallus is sticking out of me."
    "She flashes me that wicked grin even as her cheeks turn pink from pleasure and starts to fuck me."
    "I choke back a cry as she starts moving faster, getting rough with me now that I've adjusted. The quicker, harder motions make her breasts bounce and the black vinyl straps slap against her thighs."
    "She's moaning like she's the one being fucked, loving the bump and vibration of the toy's base tucked into the harness, rubbing up against her pelvis low enough that her clit catches some of the humming sensation."
    "I'm growing short of breath, panting heavily in time with her movements, feeling my cock throb within her grip."
    "I groan loudly and she gives me that wicked grin again, starting to jerk me off urgently."
    sasha.say "Cum for me!"
    show sasha strap precum
    "Insistent, she sinks her hips a little lower and aims a thrust upward to judge against the swollen gland that people call the male G-spot and I'm thrown over the edge."
    "I've never felt anything like that before; combined with her thrusts and the quick and messy way she's jerking me off is enough to make me do exactly what she told me to do."
    show sasha strap cum with hpunch
    "Hot spurts of sticky cum fly up to splash down on my chest and stomach, making a flush of heat come to my cheeks just like Sasha's when I get her sloppy."
    with hpunch
    "She moans loudly, grinding against me like she's using me to get herself off --which she is, as it turns out."
    $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_orgasm.ogg", loop=True)
    show sasha strap orgasm with hpunch
    "Sasha throws her head back with a delighted cry, tremors visibly rushing through her body."
    "I know I've cum a little more than usual, probably thanks to that nudge against my prostate gland, and I slowly lift up to look down at myself."
    "What a mess! "
    stop sound
    show sasha strap normal
    mike.say "Gonna help me clean up, Sasha?"
    "She smirks at me and pulls back, tugging the toy free of my ass, then gets on her hands and knees over me."
    sasha.say "What do you think?"
    "She asks as she dips her head, licking up a line of sticky jizz."
    $ sasha.sub -= 1
    $ sasha.love += 2
    $ sasha_strap = True
    return

label sasha_beads_play(sexperience_min=1):
    $ game.play_music("music/roa_music/city_nights.ogg")
    mike.say "Let's try something new tonight, Sasha."
    "I grin a little as she looks up at me with a mixture of suspicion and anticipation."
    "I walk over to the dresser and open the top drawer."
    show sasha shout
    if sasha.is_sex_slave:
        sasha.say "Anything you like [hero.name]..."
    else:
        sasha.say "Watcha lookin' for?"
    show sasha normal
    if sasha.flags.oralTonight:
        "Sasha comes over to stand beside me, dressed in her black underwear. She peers into the drawer, wondering if anything has caught my eye."
    else:
        "Sasha pads over to stand beside me, dressed in her birthday suit. She peers into the drawer, wondering if anything has caught my eye."
    "Spotting a blue orb-shape, I reach in and pull out my set of anal beads."
    mike.say "Perfect."
    if sasha.sub < 50:
        show sasha underwear vangry
        sasha.say "Absolutely not!"
        show sasha upset
        "Sasha rushes out of the door."
        $ sasha.love -= 5
        $ sasha.sub -= 5
        return "leave_without_gain"
    show sasha shout
    sasha.say "Um.. I guess we can... I take it those are for me?"
    show sasha normal
    "Sasha tilted her head in that cute curious way she has."
    mike.say "Good guess."
    if not sasha.flags.oralTonight:
        mike.say "Also, you're wearing way too many clothes."
        "Sasha chuckles and steps back, making a small show of peeling that snug bra off and tossing it aside, displaying her lovely little breasts for me, then bending down to tug the panties down to her ankles and stepping out of them."
        show sasha naked shout
        if sasha.is_sex_slave:
            sasha.say "Is this better [hero.name]?"
        else:
            sasha.say "Better?"
        show sasha normal
        mike.say "Much."
    "She really is a hottie. I can't wait to make her moan."
    if not sasha.flags.oralTonight:
        if not sasha.is_sex_slave:
            show sasha shout
            sasha.say "Then you better get out of your clothes too. I'm not going to be the only naked one around here."
            show sasha normal
        "I smirk at her and start disrobing, not bothering with a little show like the one she put on."
    "I love the way she looks me over, a touch of desire gleaming in her eyes."
    "I'm already half-hard thinking of what I'll do to her... or have her do to me."
    "Grabbing one last thing out of the drawer -- a bottle of lube -- I turn toward the bed and motion Sasha to come with me."
    mike.say "Time to bend over."
    show sasha doggy waiting -mike with fade
    "Sasha bites her lower lip, looking with something like trepidation at the big beads I'm holding, then reluctantly bends over with her hands on the bed."
    if sasha.flags.collared and sasha.sub > 50:
        mike.say "First, let's remind both of us who's in charge."
        show sasha doggy leashing
        "I attach the lead of the leash to her collar. For her part, Sasha closes her eyes and lets me."
        show sasha doggy -leashing leash
        mike.say "That's a very good girl, Sasha."
        sasha.say "Thank you, [hero.name]."
    "But first, though..."
    show sasha doggy cockedback waiting
    pause 0.25
    show sasha doggy impact hurt
    play sound spank
    with hpunch
    "I can't resist giving her ass a slap that makes her gasp."
    show sasha doggy -impact waiting
    if sasha.is_sex_slave:
        menu:
            "Keep spanking":
                "I can't help it. When I hear her gasp, I know there has to be more."
                show sasha doggy cockedback waiting
                mike.say "Who do you belong to?"
                sasha.say "Oh, God!"
                show sasha doggy blur waiting
                mike.say "Wrong answer!"
                show sasha doggy impact hurt
                play sound spank
                with hpunch
                "My hand impacts her ass with another loud slap, and this time she shrieks."
                show sasha doggy cockedback entered
                mike.say "Who do you belong to?"
                sasha.say "You!"
                show sasha doggy blur waiting
                if sasha.flags.mikeNickname:
                    mike.say "Call me [hero.name], slave!"
                show sasha doggy impact scream
                play sound spank
                with hpunch
                "My hand impacts her ass with another loud slap, and this time she shrieks, but this time it's more like delight than pain."
                show sasha doggy cockedback entered
                mike.say "Last try, who do you belong to?"
                sasha.say "You, my [hero.name]! I belong to you!"
                show sasha doggy blur waiting
                if sasha.is_sex_slave:
                    mike.say "Yes, my slave! You're all mine!"
                else:
                    mike.say "Yes! You're all mine!"
                show sasha doggy impact ahegao
                play sound spank
                with hpunch
                "She got it right, but I let my hand fly anyway. This one is the gentlest impact of them all, though, and her moan is pure pleasure."
                show sasha doggy impact ahegao spanked
            "Get on with the beads":
                pass

    show sasha doggy waiting nohand
    "After opening the little bottle of lube, I start rubbing it over her tight asshole with two fingers, dipping them briefly inside now and then."
    "It gets Sasha to start breathing a little quicker, and I hear a small moan."
    "Then I put some lube on the end bead and press it to her tight pucker."
    mike.say "Ready?"
    sasha.say "Mm.. mhm.."
    "She doesn't sound entirely certain, but I know she's just a little nervous about having one of the toys she usually uses on submissive men turned on her."
    show sasha doggy beads5 scream
    $ renpy.sound.play("sd/moans/sasha/sasha_panting.ogg", loop=True)
    "Slowly I start to push, watching her dark pink asshole widen to take the girth of the bead."
    show sasha doggy beads4 entered
    "It then closes tight around the flexible bar between beads and Sasha whimpers."
    show sasha doggy beads3 entered
    "I love that sound."
    "I repeat this with all but the last bead, fascinated and aroused by her reactions and the way her asshole widens to take each bead."
    show sasha doggy beads2 entered
    "I wonder if it will stay stretched wide after I pull them out."
    show sasha doggy beads hurt
    "Once they're all in except a bit to use to pull them back out after, I guide her to stand and turn around."
    mike.say "Feels good to be stuffed full, doesn't it?"
    "Her cheeks redden and she looks down, nodding hesitantly."
    mike.say "Good. Now I want you on your hands and knees."
    "Again, she makes that whimpering sound, but complies, getting onto her hands and knees on the bed, licking her lips."
    show sasha bj beads mike nodick with fade
    "She knows what's next, and despite her blush and embarrassment, there's a touch of eagerness in the way she looks at me."
    "Or rather, looks at my cock."
    "By now it's rock hard and I drop one hand to give it a few slow strokes purely to tease Sasha."
    show sasha bj beads mike dickout
    "I step closer and let the wide head brush against her parted lips, shuddering when her tongue darts out to flick against sensitive skin."
    "She's so good at sucking me off."
    $ renpy.sound.play("sd/moans/sasha/sasha_blowjob_high.ogg", loop=True)
    show sasha bj mike dickin
    "Soon her mouth is stuffed with my dick; I'm thrusting my hips and pushing to the back of her throat, listening to her whimper and whine around my cock."
    "Her ass is in the air and I can get a glimpse of the bead that still sticks out, which probably explains that deep blush to her cheeks."
    "Her mouth feels so good and I know I'm close to cumming."
    "I'm panting, muscles shaky as I keep fucking her mouth, feeling her tongue caressing the sensitive underside of my cock."
    "Finally, I can't take it anymore."
    menu:
        "Cum on her face":
            stop sound
            "I pull back with a groan, grab my dick, and start jerking myself off hard and fast."
            show sasha bj beads mike dickout cum with vpunch
            "The first spurt of cum splashes her cheeks, making her gasp, and the second rope of thick cum lands in her hair, making her blush even harder."
            with vpunch
            "I close my eyes to savor the pleasure as I keep stroking myself to milk every last bit of jizz out to paint her pretty face with."
            "She moans and gasps through it like an eager little cum-slut."
            $ sasha.sub += 1
            show sasha bj beads mike dickout cumafter with vpunch
            "I slowly stop stroking myself and open my eyes to look down at Sasha's face, half-painted with my sticky seed."
            "The redness to her cheeks shows she's still feeling embarrassed, maybe even humiliated."


        "Cum in her mouth" if hero.fitness > 25:
            show mouth_insert sasha zorder 1 at center, zoomAt(1.0, (940, 440))
            "A wave of pure pleasure rolls over me, and then I explode into her mouth."
            $ sasha.love += 1
            show mouth_insert sasha cum
            show sasha bj beads mike dickin cum closed
            with hpunch
            pause 0.2
            with hpunch
            pause 0.2
            with hpunch
            "Sasha closes her eyes and drinks it all in. First the opening spurt, and then the much bigger, second spurt that erupts, causing me to moan loudly."
            show sasha bj beads mike dickin cumafter open
            play sound "sd/moans/sasha/sasha_blowjob_swallow.ogg"
            "When I pull out, she proudly displays then my cum on her tongue, before swallowing."
            hide mouth_insert
    stop sound
    return

label sasha_sleep_date_fuck(location="hero"):
    if game.hour > 19 or game.hour < 6:
        scene bg bedroom1
        show sasha naked shout
        if sasha.is_sex_slave:
            sasha.say "May I share your bed tonight, [hero.name]?"
        else:
            sasha.say "Mmm...you cool with me spending the night here?"
        show sasha normal
        menu:
            "No":
                mike.say "No...I have to be up really early in the morning."
                "The sex was beyond incredible, but now I want to be alone."
                show sasha sad
                "Sasha frowns in disappointment, clearly trying to shrug off the sense of rejection."
                show sasha shout
                sasha.say "Okay...sleep well, I guess."
                show sasha sadsmile
                "She shakes her head as she collects her things and leaves my bedroom."
                $ sasha.love -= 3
                call sleep from _call_sleep_17
                $ game.room = "bedroom1"
            "Yes":
                mike.say "YES...I mean, yes...if you want to!"
                "I try to keep from sounding too desperate and needy, but I'm not sure I manage it."
                show cuddle sasha with fade
                "Sasha curling up against me beneath the covers is almost as good as the sex - almost..."
                sasha.say "Sweet dreams, [hero.name]..."
                mike.say "You too, Sasha..."
                $ sasha.love += 3
                call sleep ("sasha") from _call_sleep_7
                $ game.room = "bedroom1"
    return

label sasha_fuck_date_cunnilingus_intro:
    $ game.play_music("music/roa_music/city_nights.ogg")
    scene bg livingroom
    show sasha
    with fade
    "Did the date go well tonight, well enough for Sasha and I to have a good time and make some pleasant memories?"
    "I'll level with you - I have no idea!"
    "Maybe it'll come back to me in time."
    "But all I can think about right now is keeping up with Sasha as she darts down the stairs to my room."
    "She keeps looking back over her shoulder, checking that I'm following on her heels."
    "More than once I almost stumble and fall in my eagerness to get my hands on her too."
    scene bg bedroom1
    show sasha
    with fade
    "Once the door's closed behind us, Sasha wastes no time in beginning to strip off her clothes."
    "I do the same, trying to keep my eyes on her at the same time."
    "It feels like every moment I look away to pull off a piece of clothing, I've missed something worth seeing."
    show sasha topless
    "Each time I glance back at her, Sasha's that little bit closer to being naked."
    "And I curse myself silently for not watching more closely as she peels every last item that she's wearing."
    show sasha naked
    "Once she's finally naked, Sasha makes a show of crawling onto my bed and lying back against the pillows."
    show sasha cunnilingus nomc with fade
    "I'm still fumbling to get my shorts off, hopping towards her at the same time."
    "Before I can free myself from them, I start to lose my balance and totter forwards."
    show sasha cunnilingus -nomc
    "This means that I end up falling onto the bed, almost right into Sasha's lap."
    sasha.say "Hello there!"
    sasha.say "We're a little keen tonight, aren't we?!?"
    "I look up at her, meaning to make my apologies for tripping up like a clumsy oaf."
    "But it's only then that I actually take in the view of Sasha from this angle."
    "She's looking down at me from behind her naked breasts, grinning at my predicament."
    "It really is quite a sight to see!"
    "I can't help liking my lips as I nod hastily."
    mike.say "C...can you blame me?"
    mike.say "I feel like a dog begging for a treat!"
    "Sasha cocks her head on one side, her expression turning cocky."
    sasha.say "Oh, really?"
    sasha.say "Well, I think a dog has to do a trick before he gets a treat."
    sasha.say "How about you make yourself useful down there?"
    "I watch as Sasha rubs her hands along her thighs and then between them."
    "My eyes follow them, catching a glimpse of the neat folds hidden down there."
    "It's not like she needs to beg me or be persuasive in asking."
    "Going down on Sasha like this is almost as good as it gets."
    "Only being inside of her could be better for me."
    "But sometimes it's good to put others first - am I right?"
    "I nod as I lower my head towards her pussy, already inhaling its scent."
    "Musky and sweet, like nothing else in this world."
    "Sasha's lips are almost as wet as my own."
    "And soon the same tongue will be licking them too!"
    return

label sasha_fuck_date_cunnilingus:
    $ game.play_music("music/roa_music/city_nights.ogg")
    show sasha cunnilingus notongue
    $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_low.ogg", loop=True)
    "I begin by teasing the very edges of Sasha's pussy, tracing its shape."
    "Even with me being so gentle, I still feel her shiver at the sensation."
    "How could anyone not want to do this?"
    "I feel like I have so much power over her right now, like she's in the palm of my hand!"
    show sasha cunnilingus up
    $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_low.ogg", loop=True)
    "My tongue starts to work its way among the folds of Sasha's pussy a moment later."
    show sasha cunnilingus middle
    "And now I can actually taste the unique flavour, the manifestation of her arousal."
    show sasha cunnilingus down
    "It's like nothing else I could ever imagine."
    show sasha cunnilingus up
    "Not appetising like food or drink, in fact more than a little sour."
    show sasha cunnilingus middle
    "Yet it's a taste that I find myself craving ever more as it fills my senses."
    show sasha cunnilingus down
    "And I can feel that I'm about to dive in here and do all I can to get more!"
    menu:
        "Use my tongue":
            show sasha cunnilingus up
            "I'm well and truly in the zone by now, totally focused on the task at hand."
            show sasha cunnilingus middle
            "And Sasha, well, let's just say that she's opening up to me like a flower."
            show sasha cunnilingus down
            "I feel the urge to go ever deeper, licking and stroking her delicate folds."
            show sasha cunnilingus up
            "But even as I do so, she opens up to me, letting me do just that."
            show sasha cunnilingus middle
            "At once this reminds me of kissing Sasha's mouth, full on and with passion."
            show sasha cunnilingus down
            "And yet it's also a different experience entirely."
            show sasha cunnilingus up
            "For one thing, I can hear her panting and moaning at my efforts."
            show sasha cunnilingus middle
            show sasha cunnilingus blush pleasure
            $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_medium.ogg", loop=True)
            "Which only serves to urge me onwards, telling me I'm hitting the spot."
            show sasha cunnilingus down
            "I have no idea just how deep the tip of my tongue has managed to go."
            show sasha cunnilingus up
            "Just that every time I twist and turn it, Sasha gasps at the motion."
            show sasha cunnilingus middle
            "And I don't need to be shown a diagram to know I'm doing the right thing."
            show sasha cunnilingus down
            "All I need to do is keep on going."
            show sasha cunnilingus up
            "That and hope that my tongue doesn't seize up before I'm done!"
            show sasha cunnilingus middle
            "Which is why, a moment later, it comes as a genuine relief to feel Sasha move beneath me."
            show sasha cunnilingus down
            "Her entire body begins to buck and twitch, as if it can't hope to stay still."
            "And I can hear her cries building to a crescendo like never before!"
        "Finger her ass" if hero.sexperience >= 30:
            $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_medium.ogg", loop=True)
            show sasha cunnilingus up
            "My hands have been cradling Sasha's ass this whole time."
            show sasha cunnilingus middle
            "And my grip's been getting tighter with every minute that passes."
            show sasha cunnilingus down
            "By now I have a buttock in each hand, squeezing them mercilessly."
            show sasha cunnilingus up
            "Sasha's lifting her ass off of the mattress too."
            show sasha cunnilingus middle
            "Like she wants to smother me with her pussy!"
            show sasha cunnilingus down
            show sasha cunnilingus fingerass
            "Acting on instinct, I take a finger and push it between her cheeks."
            show sasha cunnilingus up
            "It works like a charm, making her flinch in surprise and letting me breathe too!"
            stop sound
            show sasha cunnilingus middle
            sasha.say "Hey!"
            sasha.say "Where'd you think you're putting that thing?!?"
            show sasha cunnilingus down
            "Undeterred, I keep on pushing the finger deeper into her ass."
            show sasha cunnilingus up
            show sasha cunnilingus blush pleasure
            $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_medium.ogg", loop=True)
            "Sasha stops talking, instead making a deep moaning sound."
            show sasha cunnilingus middle
            "It's not an unpleasant one, and so I press on further still."
            show sasha cunnilingus down
            sasha.say "Mmm..."
            show sasha cunnilingus up
            sasha.say "That's nice..."
            show sasha cunnilingus middle
            "Encouraged by Sasha's words, I try to synchronise my tongue and finger."
            show sasha cunnilingus down
            "And all the time, I wonder how much it would take for one to be able to feel the other."
            "But my musings are soon cut short as I feel Sasha begin to twitch."
            "It's like she can't take any more and is about to burst!"
        "Use the dildo" if hero.has_item("dildo"):
            $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_high.ogg", loop=True)
            show sasha cunnilingus up
            "Sasha seems to be almost completely out of it already, lost in her own sensations."
            show sasha cunnilingus middle
            "And I know that I could just as easily be drawn in to the same degree too."
            show sasha cunnilingus down
            "But I hold back, just a little, as I reach for something under the bed."
            show sasha cunnilingus up
            "I know we didn't exactly discuss using toys, but the dildo's just within reach."
            show sasha cunnilingus middle
            "And I just know that it's the kind of surprise Sasha should like too!"
            show sasha cunnilingus down
            "Keeping up the attention with my tongue, I sneak the dildo between her legs."
            show sasha cunnilingus up
            "Sasha's so wrapped up in what I'm doing to her that she doesn't notice a thing."
            show sasha cunnilingus dildopussy
            show sasha cunnilingus middle
            "At first all I do is stroke the head against her pussy, as gently as I can."
            show sasha cunnilingus down
            "I doubt that she can tell the difference between it and my tongue."
            show sasha cunnilingus up
            show sasha cunnilingus shake
            "But then I begin to push the dildo deeper, so that it enters her body."
            stop sound
            show sasha cunnilingus middle
            sasha.say "What..."
            show sasha cunnilingus down
            sasha.say "What's that?!?"
            show sasha cunnilingus up
            "Though she sounds surprised, there's no alarm in Sasha's voice."
            show sasha cunnilingus vibrate
            show sasha cunnilingus middle
            $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_medium.ogg", loop=True)
            "And so I choose to take this as permission to keep on going."
            show sasha cunnilingus down
            "It doesn't take long for the dildo to sink all the way into Sasha's pussy."
            show sasha cunnilingus up
            "Her protests turning into sighs as her body surrenders to the thing too."
            stop sound
            show sasha cunnilingus middle
            show sasha cunnilingus blush pleasure
            sasha.say "Oh...oh shit..."
            show sasha cunnilingus down
            sasha.say "Shit yes..."
            $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_medium.ogg", loop=True)
            show sasha cunnilingus up
            "Pretty soon I'm working Sasha with the dildo."
            show sasha cunnilingus middle
            "I keep licking around the edges of her pussy the whole time too."
            show sasha cunnilingus down
            "And it doesn't take long for her to begin twitching."
            "In fact, Sasha's while body seems ready to explode!"
        "Use dildo and my finger." if hero.has_item("dildo") and hero.sexperience >= 30:
            $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_low.ogg", loop=True)
            show sasha cunnilingus up
            "Sasha seems lost in her own world of sensations."
            show sasha cunnilingus middle
            "So she doesn't see me reach under the bed."
            show sasha cunnilingus down
            "We never agreed to using toys, but the dildo's right there."
            show sasha cunnilingus up
            "It seems a waste just to leave it lying on the ground."
            show sasha cunnilingus middle
            "And Sasha's so wrapped up in what my tongue is doing to her she hardly notices a thing."
            show sasha cunnilingus down
            "This means it's pretty easy to sneak it up and between her legs..."
            stop sound
            show sasha cunnilingus up
            show sasha cunnilingus dildopussy
            sasha.say "Wha..."
            show sasha cunnilingus middle
            sasha.say "What the hell's that?!?"
            $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_medium.ogg", loop=True)
            show sasha cunnilingus down
            "Sasha sounds surprised, but already aroused by what I'm doing."
            show sasha cunnilingus up
            "And her half-hearted protests soon fade away as the dildo enters her body."
            show sasha cunnilingus middle
            show sasha cunnilingus vibrate
            "Her pussy has no such reservations, swallowing the toy greedily."
            show sasha cunnilingus down
            show sasha cunnilingus blush pleasure
            sasha.say "Oh...oh..."
            show sasha cunnilingus up
            sasha.say "Shit...yes...keep going!"
            show sasha cunnilingus middle
            "My free hand has been on Sasha's ass this whole time."
            show sasha cunnilingus down
            "And my grip tightens with every moan that leaves her lips."
            show sasha cunnilingus up
            "By now I'm mercilessly squeezing her buttock."
            show sasha cunnilingus middle
            "I feel her ass lift off of the mattress, and I take full advantage."
            show sasha cunnilingus down
            show sasha cunnilingus fingerass
            "I take a finger and push it between her cheeks."
            show sasha cunnilingus up
            "And before she knows it, the muscles are pulling it into her."
            show sasha cunnilingus middle
            sasha.say "Whoa..."
            show sasha cunnilingus down
            sasha.say "Hey..."
            show sasha cunnilingus up
            sasha.say "How much more are you gonna stick up me?!?"
            show sasha cunnilingus middle
            "I smile at this, but I don't stop."
            show sasha cunnilingus down
            "And soon enough, Sasha's moaning again."
            show sasha cunnilingus up
            sasha.say "Mmm..."
            show sasha cunnilingus middle
            sasha.say "That's...good..."
            show sasha cunnilingus down
            show sasha cunnilingus shake
            "I try as best I can to synchronise my finger and the dildo."
            show sasha cunnilingus up
            "Wondering how far they'd both need to be in before I could use the one to feel the other."
            show sasha cunnilingus middle
            "But there's no time for that, as Sasha's already starting to buck and twitch."
            show sasha cunnilingus down
            "I guess the combination of the two things is just too much for her to take!"
    $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_orgasm.ogg", loop=True)
    show sasha cunnilingus ahegao -up -middle -down -notongue -fingerass -dildopussy with hpunch
    "Sasha wraps her thighs around me as she cums, clinging to me like her life depends on it."
    "I can feel every moment of her orgasm, every muscles that moves to give it life."
    "Some guys might be jealous of her in that moment, envious of her climaxing instead of them."
    "But I just love the chance to see the effects of my handiwork as it overwhelms Sasha so completely."
    $ renpy.sound.play("sd/moans/sasha/sasha_panting.ogg", loop=True)
    "After all, I did say that I felt like a dog."
    "And if I have to be a dog, then I want to be the best dog a girl can own!"
    stop sound
    $ sasha.flags.oralTonight = TemporaryFlag(True, 1)
    return

label sasha_fuck_date_bj:
    if hero.sexperience % 3 == 0:
        "Sasha kneels down in front of me, holding my eye and smiling up at me the whole time."
        scene sasha bj2
        show sasha bj2 naked
        "In fact, I'm so busy staring into her eyes that I don't notice what she's doing with her hands."
        "Which is why I'm taken by surprise when she takes a firm hold of my cock!"
        mike.say "Ah..."
        mike.say "Hey, Sasha!"
        mike.say "Be gentle, okay?"
        show sasha bj2 smile
        "All this gets in response from Sasha is a wicked laugh."
        "Sasha's mouth is wide open as she laughs too."
        "Which means she's more than prepared when she pounces a moment later!"
        show sasha bj2 open
        "Sasha takes almost a third of my cock into her mouth at once."
        "There's no pause or hesitation, almost no time to take a breath."
        "And there's no messing around with foreplay here either."
        $ renpy.sound.play("sd/moans/sasha/sasha_blowjob_low.ogg", loop=True)
        show sasha bj2 suck
        "One minute she's teasing me with it."
        "And the next she's actually doing it!"
        "I gasp as Sasha bites down a little too, letting me know she's serious."
        "Right from the start she used her lips and tongue to great effect."
        "I feel them slithering over the head and shaft of my cock inside her mouth."
        $ renpy.sound.play("sd/moans/sasha/sasha_blowjob_medium.ogg", loop=True)
        show sasha bj2 closed
        "And the portion of it that's not in her mouth isn't neglected either."
        "Because Sasha rubs her hand up and down it the whole time too."
        "Head and hand are moving in perfect harmony."
        "Which means nothing is left out of the act."
        mike.say "Sasha..."
        show sasha bj2 opened
        mike.say "Of fuck..."
        mike.say "Sasha!"
        "Sasha looks at me for a moment, out of the corner of her eye."
        "It's really nothing more than the briefest of passing glances."
        "But somehow it lets me know just what she's feeling in that moment."
        "Pleasure, confidence - and more than a little amusement too."
        show sasha bj2 closed
        "Then Sasha's eye closes again, and all I can do is let her have her way with me."
        $ renpy.sound.play("sd/moans/sasha/sasha_blowjob_high.ogg", loop=True)
        "She does that by upping the stakes a moment later."
        "Specifically by taking ever more of the length into her mouth."
        "Soon enough, Sasha has all but the smallest part of my cock in there."
        "And she's not slowing down to handle it either!"
        show sasha bj2 opened
        "If anything, Sasha seems to actually be picking up speed."
        "There's no room for her hands to get in on the action now."
        "So only her head is going back and forth."
        "The motion becomes almost hypnotic as I watch her go at it."
        "But then I begin to feel the effect the muscles of her throat are having on me."
        show sasha bj2 closed
        "And I realise that she's going faster because she's pushing me towards the end!"
        menu:
            "Cum in her mouth":
                "All at once I feel it starting to happen."
                "A cascade of sensation that I can't hope to stop."
                "Sasha must know that it's coming too."
                show mouth_insert sasha zorder 1 at center, zoomAt(1.0, (940, 440))
                "She allows my cock to retreat from her throat."
                show mouth_insert sasha cum
                show sasha bj2 cum
                with vpunch
                "But she keeps it in her mouth as I shoot my load."
                show sasha bj2 closedb with vpunch
                pause 0.2
                with vpunch
                pause 0.2
                with vpunch
                "And then she swallows the entire thing, from start to finish."
                $ renpy.sound.play("sd/moans/sasha/sasha_blowjob_swallow.ogg", loop=True)
                show mouth_insert sasha -cum
                show sasha bj2 opened
                "Expertly keeping the whole thing inside of her mouth."
                $ sasha.love += 2
                hide mouth_insert
            "Cum on her face" if sasha.sub >= 50:
                "All at once I feel it starting to happen."
                "A cascade of sensation that I can't hope to stop."
                "Sasha must know that it's coming too."
                stop sound
                show sasha bj2 -suck opened
                "As she pulls her head back, releasing my cock a moment later."
                with vpunch
                "Then she leans back and smiles as I shoot my load into her face."
                with vpunch
                pause 0.2
                show sasha bj2 closedb with vpunch
                pause 0.3
                show sasha bj2 cum face opened
                "Stripe of sticky white cum paint her cheeks."
                "Then it begins to run downwards over her lips and drip from her chin."
                $ sasha.sub += 1
        stop sound
    else:
        mike.say "On your knees."
        scene sasha bj
        if sasha_beads:
            show sasha bj beads
        if sasha_ropes:
            show sasha bj rope
        with fade
        "I need more. I want to feel her bobbing on my dick."
        "Groaning, I lean back a little more and brace on one hand."
        "The other hand moves to grip her hair so I can hold her head still."
        $ renpy.sound.play("sd/moans/sasha/sasha_blowjob_low.ogg", loop=True)
        show sasha bj mike dickin
        "I don't want to force too much, so I start by just giving little bucks between her lips, pushing my cock in until her mouth is full."
        "By the gleam in her eyes, Sasha looks like she really enjoys having a mouth full of dick!"
        "Sensing that the teasing portion of the evening is done, she settles back to sit on her heels, one hand lifting to cup my balls."
        "After how she'd sucked and licked those full, rounded orbs, having her knead at them and roll them across her palm is nearly bliss."
        "Her other hand comes up and wraps around the base of my cock."
        "For long moments as I give those small, careful thrusts, she grips and squeezes in time with my movements."
        "Then she starts stroking my shaft so her index and thumb meet her lips when I push into her mouth."
        "The tandem sensations are incredible! This girl really knows how to give head."
        if sasha.is_sex_slave:
            mike.say "Take me deep slave!"
            "I command her, knowing she will obey."
        else:
            mike.say "Hnn... I wanna put my cock in your throat."
            "I murmur without thinking; when her gaze lifts to meet my eyes, I flush a little, and I'm not sure if it's shyness regarding what I blurted out, or the rapidly building pleasure."
        "She gives my balls a little squeeze, then lifts her head, letting my cock slide out of her mouth for a moment, though the tip rubs against her lower lip still."
        stop sound
        if sasha.is_sex_slave:
            sasha.say "Yes [hero.name]."
        else:
            sasha.say "Don't worry, we're getting there."
            "She smirks and tosses me a wink."
            sasha.say "Don't push it; this is my present to give."
            "Reluctantly, I take my hand away from her hair and place it on the bed again, leaning back a little and looking down my body at her."
        "She grins that wicked grin of hers and slowly takes the head of my cock into her mouth without breaking eye contact."
        "There's just something so sexy about that!"
        $ renpy.sound.play("sd/moans/sasha/sasha_blowjob_medium.ogg", loop=True)
        show sasha bj dickin
        "She continues to meet my gaze as she starts to bob on my dick, and Sasha looks incredibly hot doing so."
        "It turns me on so much, watching her watching me as she's got a mouthful of my cock."
        "I want to thrust, but I hold back, letting her go at her own pace."
        "After a moment, she starts bobbing a little further down, until I can feel the tip of my rod brushing the back of her throat."
        show sasha bj closed
        "Her eyes squeeze shut for a second as she holds herself there, then pulls back and resumes sucking, working her way up to more."
        "Meanwhile, her hands stay busy."
        "The way she fondles my balls feels great, but it's her other hand that has me a little distracted."
        "She's still stroking me firmly, and she's pressing her thumb hard against the underside of my cock, knowing that's the most sensitive zone she could be touching aside from the head."
        "It's bringing me closer and closer to climax."
        mike.say "Don't s-stop..."
        show sasha bj open
        "I groan down to her, and her eyes light up with something like joy; she really wants me ready to cum!"
        "I wonder if she'll let me cum on her face; I really want to see those pretty cheeks and lips coated with my seed, but I'm torn, since cumming down her throat would be just as incredible."
        "It seems like she's going for that second option, too."
        show sasha bj closed
        "She pushes her head down lower, and after a brief moment of struggle, she takes the head of my cock into the incredibly tight grip of her throat."
        mike.say "Fuck! Gonna make me cum!"
        "I start panting, right on the edge, and she knows it."
        "Sasha takes her hand away from my shaft, disappointing me only briefly, since it seems she just wanted it out of her way."
        "Now she starts bobbing on my dick, taking my rod into her throat for about half the length."
        show sasha bj open
        "She pauses each time she's at the lowest point and stares up at me while she swallows, making her throat grip my cock even tighter than her hand had, and squeezing downward from shaft to head."
        "It's beyond amazing."
        mike.say "Almost there."
        "I warn her, not wanting Sasha to be surprised."
        "She doesn't slow down, doesn't even hesitate!"
        "Still staring up at me, she keeps bobbing quickly on my dick, making wet and sloppy sounds as she moves faster, clearly eager for my cum."
        "I can't help myself."
        menu:
            "Cum in her mouth":
                show mouth_insert sasha zorder 1 at center, zoomAt(1.0, (940, 440))
                "I grip the back of her head with one hand as tremors start to rock through me, and I push deeper; she makes no protest though her eyes tear up a bit."
                show mouth_insert sasha cum
                show sasha bj cum dickin
                with hpunch
                $ renpy.sound.play("sd/moans/sasha/sasha_blowjob_swallow.ogg", loop=True)
                pause 0.2
                show sasha bj open with hpunch
                pause 0.2
                with hpunch
                "Groaning, I gasp for breath as my cock twitches and throbs, forcing her to swallow quickly as pleasure sends spurts of hot cum straight down her throat."
                show mouth_insert sasha -cum
                show sasha bj dickout cumafter open
                "It takes several moments for my climax to pass, and when it does, I drop back to the bed, panting, trying to catch my breath."
                "Dimly, I feel Sasha licking at my cock lightly before she pulls away and stands."
                hide mouth_insert
            "Cum on her face" if sasha.sub >= 50:
                "My breath stays quick and shallow; I can feel the heat and tension low on my stomach that lets me know climax is close."
                "I love the way she's sucking my cock, but I want something more than just cumming in her mouth, no matter how eager she seems."
                stop sound
                show sasha bj dickout cum with vpunch
                "Grabbing her hair, I pull her off my dick and start jerking off with my free hand; it doesn't take long for the first ropes of cum to splash on her pretty face, one spurt landing in her jet black hair."
                show sasha bj closed with vpunch
                "I shudder, back arching as the climax rolls through me, making sure to cover my little lover's face with the seed she wants so badly, then drop back onto the bed, panting."
                show sasha bj cumafter open
                "She stands, a little shaky, and looks down at me while wiping some of the jizz off her face, then licking it from her fingers, knowing how much of a turn-on that view will be to me."
                $ sasha.sub += 2
        if sasha.is_sex_slave:
            sasha.say "Thank you [hero.name]."
        "I let out a pleasure-filled sigh and look up at her with half-lidded eyes."
        stop sound
    return

label sasha_fuck_date_foreplay:
    "She strokes her palm over the rounded tip of my dick, encouraging a little drop of pre to appear at the slit."
    mike.say "Are you happy too?"
    "I smirk at her and arch a brow, reaching out to slip one hand between her thighs."
    "Her grin widens, so sensual, and she steps forward a little to encourage the touch."
    "I'm delighted to find out I was right; no underwear bars the way between my hand and her flesh."
    "The folds of her pussy are so soft and smooth, no hair in the way either, and I dip one fingertip into her slit to find her already a little wet."
    mike.say "Seems like it."
    sasha.say "Mm. I've been thinking about this all day."
    "She steps in so our bodies just barely touch."
    "She lifts up onto her toes and presses her lips to mine, parting them with the tip of her tongue for a slow and erotic kiss that promises so much more."
    "My arousal sky-rockets; between her kiss and the stroke of her hand as her fingers curl around my shaft, I'm so hard I ache."
    "I'm ready to fuck her right now, but the anticipation will make the pleasure even better."
    "Besides, I suspect she's the type to enjoy some thorough foreplay."
    "I put one hand on the curve of her hip to keep her close while the other stays between her thighs."
    "One fingertip finds the swollen nub of her clit and I start stroking the sensitive flesh in slow circles, drawing a soft moan from her against my lips."
    "I let my tongue seek out hers to deepen the kiss while teasing her with light flicks of my fingertip."
    "I can tell by the way she shivers how much she likes it."
    "She's eager; Sasha stops toying with my half-exposed cock, instead using her hands to carefully push my boxers down, letting them fall to the floor."
    hide sasha foreplay
    show sasha foreplay underwear
    with fade
    "I step out of them and kick them absently off to the side, too distracted by what she's doing to give the clothing much thought."
    "Now that I'm naked, she gets busier with her hands. One dips down to cup my balls, kneading them so gently within her palm; the sensation sends tingles through the flesh she's touching and makes me sigh between our kisses."
    "Her other hand wraps around the base of my cock and gives the hard flesh a squeeze firm enough to be just shy of uncomfortable."
    "It makes me groan against her lips, and she responds with a sensual chuckle in her throat, clearly enjoying teasing me."
    "Standing against one another, we both take our time in teasing each other."
    "The anticipation is building almost too high to keep ignoring, but what she's doing feels so good."
    "Sasha grips my cock and starts stroking slowly, twisting her hand from one side to the other for added friction, caressing the pad of her thumb over the tip of my cock each time her stroking leads up to the plump head."
    show sasha foreplay underwear up
    "I'm starting to breathe harder and so is she, too fast to keep up the kissing."
    "I rest my forehead against hers, looking intently into dark eyes that are filled with lust, watching the pink flush of arousal stain her cheeks."
    $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_low.ogg", loop=True)
    "My hand pushes further between her thighs and I let two fingertips rub against her opening."
    "It's already very slick, making it easy to slip the tips of the digits inside her, making her tilt her head back with a moan."
    "I start to slowly finger-fuck her, wanting her as lusty as I am, imagining how incredible it will feel when I replace my thrusting fingers with my cock."
    "I want her naked."
    "With my free hand, I push the robe off her shoulders and let it fall to the floor, then tug the nightie off over her head and toss it aside."
    show sasha foreplay naked
    stop sound
    "She's so gorgeous, with those small perky breasts, that trim figure, and long, perfectly shaped legs."
    "Each steady movement of my hand makes her whimper and her lovely eyes flutter shut as her breath quickens."
    "She starts stroking my dick a little faster, squeezing at the head, gliding her hand up and down my shaft."
    if sasha.sub >= 25:
        "Then she leans down, putting her hands on my knees."
        "She pushes them apart and then kneels between my legs; now I know what's coming."
        "I can feel my cock swell almost to full size in anticipation."
        if sasha.is_sex_slave:
            sasha.say "Can I suck your cock [hero.name]?"
            sasha.say "Please..."
            mike.say "You can, little slave."
        else:
            sasha.say "You're going to like the next part..."
        show sasha bj mike with fade
        if not sasha.flags.haircut:
            "Sasha takes a hair tie off her wrist and uses it to bind back that pretty black hair, then ducks her head to flick her tongue over the slit at the tip of my dick."
        else:
            "Sasha takes a hair tie off her wrist and uses it to bind back that pretty blonde hair, then ducks her head to flick her tongue over the slit at the tip of my dick."
        "I'm helpless to stop a little groan, and my fingers curl into my bedspread."
        if sasha.is_sex_slave:
            mike.say "Not bad."
            sasha.say "Thank you [hero.name]."
        else:
            mike.say "Nn.. good present."
            sasha.say "Thought you'd like it."
        "She whispers back, letting her warm breath caress over the head of my cock."
        "It makes me shiver and shift my hips, eager for more."
        "Apparently, Sasha is just eager to draw this out and torment me."
        $ renpy.sound.play("sd/moans/sasha/sasha_blowjob_low.ogg", loop=True)
        "She curls a finger beneath my cock and lifts it upward, then tucks her head in further to start lapping lightly at my balls."
        "That's not an experience I get very often, and I lean back, parting my thighs further to give her all the room she could want."
        "She chuckles softly and keeps licking."
        "I'm trembling by the time she's done sucking and licking at my balls, which I can feel throbbing."
        "I'm marveling over how much she's managed to work me up while barely touching my dick at all."
        "Breathing hard, I squirm as she lifts her head and pulls her hand away, letting my stiff rod drop a little until the head is pointed at her face."
        "Part of me wishes I was ready to cum right now; it would be incredibly hot to paint her cheeks and lips with my jizz, but she doesn't have me worked up quite enough for that."
        show sasha bj mike
        "Just as well, because a moment later, she's leaned in and taken the head of my cock into her mouth."
        "It's so warm and wet, and I can feel her tongue rubbing lightly at the lines and ridges just beneath the head along the underside; those spots are so sensitive!"
        "If she keeps that up, she might wind up with a mouthful of spunk before she's ready for it, and it seems she knows that too, for she stops and simply presses the flat of her tongue up against the underside."
        show sasha bj mike dickin
        "Instead of further teasing, she starts sucking, and she sucks hard!"
        "I hadn't thought my dick could get any harder, but Sasha proves me wrong."
        "I ache, wanting more, wanting her to bob her head on my dick, but for now I hold still and let her go at her own pace."
        "It's clear she wants to torment me anyway."
        "And she's very good at tormenting me."
        "Her fingertips drift up and down in a feathery caress along the underside of my shaft, sending tingles through my body and making me squirm."
        "It's almost embarrassing how much reaction she's getting out of me already. I want more."
    stop sound
    return

label sasha_fuck_date_rimjob:
    sasha.say "Okay, [hero.name]..."
    sasha.say "Lie down on the bed, yeah?"
    "Now it's my turn to nod as I hurry to do as Sasha tells me."
    show sasha rimjob with fade
    "Once I'm laid on the mattress, she climbs up beside me."
    "And I watch with intense interest as Sasha parts my legs."
    "I keep glancing down there as she lowers herself between them."
    "Watching as her head disappears from view and waiting for what happens next."
    "The first thing that I feel is the slightest touch of Sasha's tongue."
    "She must be using nothing more then the tip as she begins."
    "But all the same, I feel a shiver spread out from down there."
    "It seems to travel in all directions at once."
    "And it reaches my fingers, toes and scalp all at the same time."
    "If Sasha even notices the effect, she doesn't stop for a moment."
    "Because now I can feel her really starting to move inwards."
    "Her tongue isn't tickling and being delicate any more."
    "Instead I feel it sink deeper than before, pushing its way inside."
    "The muscles of my ass do just what they were made to do as this happens."
    "They tighten, trying as best they can to keep Sasha from getting any further."
    "Part of me thinks that this is going to be the end of it."
    "That Sasha's being presented with an impenetrable barrier."
    "But she surprised me by redoubling the strength of her efforts."
    "And rather than my tensed muscles stopping me feeling anything, the opposite is true."
    "Their resistance only serves to make what I'm experiencing that much more intense."
    "So much so that it takes me some time to notice how deep Sasha's managed to get."
    "Deep enough for her to be able to bring her lips into play too."
    "I know this because I can feel them now, kissing around the edges."
    "As if that weren't enough, Sasha reaches up to grab my cock too."
    "Obviously it's hard and standing to attention by now."
    "And she takes full advantage of that, stroking it with her hand."
    mike.say "Oh god..."
    with vpunch
    mike.say "Sasha..."
    mike.say "I can't take any more!"
    with vpunch
    "I have no idea if Sasha even hears what I'm saying."
    "And even if she does, nothing changes as a result."
    "Sasha simply keeps on going, as if I never said a word."
    "I was twitching and tensing before, helpless to keep still."
    "But now things have gone so far and become so intense, the opposite is true."
    "I feel like I'm paralysed by Sasha's touch, unable to move an inch."
    with vpunch
    "That is until the dam breaks inside of me."
    with vpunch
    "When it does, I just go with it, feeling myself lose it."
    show sasha rimjob cum with vpunch
    "I shoot my load as my entire body starts to quake from my orgasm."
    "Only then does Sasha haul herself up and release me from her grasp."
    "She leans on my thighs, waiting for me to subside and come back to reality."
    "And all the time she has a knowing smile on her face."
    "As she can see the results of her efforts upon me."
    return

label sasha_fuck_date_handjob:
    mike.say "So, Sasha..."
    "I turn around, trying to sound all manly and commanding."
    "But as soon as I do, I see Sasha's standing right in front of me."
    show sasha close
    "And in that instant, she reaches out and grabs me by the collar of my shirt."
    show sasha joke
    sasha.say "Shut up!"
    sasha.say "No time for talking!"
    "Sasha yanks my head down to her level."
    show sasha kiss -close with fade
    $ sasha.flags.kiss += 1
    "And then she pushes her lips against mine."
    "I suppose you have to call it a kiss."
    "But to me it does feel a little more like a full-on assault!"
    "Sasha's tongue is between my lips a moment later, snaking into my mouth."
    "And I can already feel my body reacting to her aggressive advances."
    "There's no thought of holding back, no desire to tell her to stop."
    "Sasha's hands are all over me too, pulling at my clothes."
    "Before I know it, she's stripping them off me at an alarming rate!"
    "I don't know how she can do it while she's still kissing me."
    "But it's happening, as I can feel every item of clothing being removed."
    "All I can do is fumble as I try to do the same to her."
    "Yet it seems that my efforts only serve to get in the way."
    "And I can feel Sasha slapping my hands away in frustration." with vpunch
    "In the end, she breaks off the kiss to put me in my place."
    show sasha close annoyed -kiss with fade
    sasha.say "Urgh..."
    sasha.say "Okay, okay..."
    show sasha flirt
    sasha.say "Just sit back and leave this to me, okay?"
    "I nod eagerly, making a point of putting my hands behind my back."
    "But I'm still not prepared for what Sasha does next."
    show sasha normal -close
    "Which is to push me backwards across the room." with vpunch
    "I can't see where I'm going."
    "And trying to look back over my shoulder only makes it worse."
    "Then I feel the backs of my legs collide with something."
    hide sasha
    "Which means I go toppling over backwards!" with vpunch
    "Luckily for me there's only a split-second of falling."
    "Then I discover that what I walked into was the bed."
    "This means that I land on the yielding mattress, rather than something hard and painful."
    show sasha underwear
    "Even so, I only have a brief moment of relief before Sasha dominates my vision."
    "I can't even make an effort to sit up before she's on the bed and then on top of me!"
    show sasha joke topless with dissolve
    "By now she's managed to strip me naked, and start doing the same to herself."
    "Sasha finishes the job while she uses her weight to pin me down."
    "But it's not like I'm resisting her efforts!"
    show sasha naked -topless with dissolve
    "I'm more than happy to lie back and watch as Sasha pulls off the last of her clothes."
    "That done, she slaps one hand down on my shoulder."
    "And the other one reaches down below my waist."
    "Needless to say that I'm good and hard by now."
    "Something that Sasha discovers for herself when she grabs hold of my cock."
    show sasha handjob with fade
    "I feel her squeeze it, and the sensation that creates is a mixture of pain and pleasure."
    sasha.say "Mmm..."
    sasha.say "Looks like someone's pretty excited!"
    "Of course she's right, I'm more than ready to have some fun."
    "But for some reason I can't help chuckling at the statement."
    mike.say "Ah..."
    mike.say "Yeah, Sasha..."
    mike.say "You could say that!"
    sasha.say "Oh!"
    sasha.say "So you think this is funny, huh?"
    mike.say "Well...yeah..."
    mike.say "I mean, no..."
    mike.say "But..."
    "Sasha shakes her head."
    "Then she squeezes my cock harder than ever."
    sasha.say "How's that, huh?"
    sasha.say "You think that's funny too?"
    mike.say "Oh fuck!"
    "Sasha laughs as my eyes bulge at the sensation of what she's doing to me."
    "But I feel a sense of relief as she eases her grip just a little."
    "And then she starts to stroke the shaft, rather than just squeezing it."
    "Sasha's still laughing as I start to nod and gasp with pleasure."
    "But there's nothing else I can do right now, even if I wanted to."
    "Her naked body is laid atop mine."
    "And she's handling me like you couldn't imagine."
    "So where else would I rather be than right here?"
    "Sasha's straddling my leg too, almost like she's riding it."
    "That means I can feel what's going on between her legs too."
    "It's hot and slippery, sliding over my thigh."
    "Which means she's getting off on all of this too!"
    show sasha handjob speed
    "Sasha's going faster now, picking up speed all the time."
    "Yet somehow she still seems to know just what she's doing."
    "Sasha pinches and squeezes just where and when it's needed."
    "And she lets go at the precise moment for the maximum effect too."
    "I begin to hear a ragged sound a few moments later."
    "One that I recognise as someone gasping for breath."
    "But it takes me a few more seconds to realise that I'm the one making it!"
    "I'm panting and groaning, my heart pounding in my chest."
    mike.say "Ah..."
    mike.say "Sasha..."
    mike.say "I'm...I'm gonna..."
    sasha.say "You bet you are!"
    sasha.say "Don't hold back, [hero.name]..."
    sasha.say "Just let it go!"
    "It's not like I'm doing as Sasha says out of obedience."
    "It's more like I don't have any kind of choice in the matter!"
    "Even so, she keeps right on going as the inevitable happens."
    show sasha handjob cum with vpunch
    "I let out a long, tortured groan as I shoot my load."
    with vpunch
    "And as my cock's pointing straight up, that's where it goes."
    with vpunch
    "Sasha looks on, smiling with delight as my cock erupts in her hand."
    show sasha handjob cum -speed with vpunch
    "Cum spurts from the tip like a miniature fountain."
    with vpunch
    "And then it spatters down onto her fingers a moment later."
    sasha.say "Yeah..."
    sasha.say "Just like that!"
    "All I can do is lie back on the mattress, panting for breath."
    "I think that I might be nodding in agreement with Sasha."
    "Or maybe I'm just shaking from the effort that I just made."
    "Either way, I know that I'm exhausted and utterly spent."
    return

label sasha_fuck_date_titfuck:
    if (game.week_day % 2 == 0 and sasha.sub >= 40):
        "There are always advantages to those involved in a relationship knowing their place and role."
        "Especially when that comes without the need for them to be reminded of it too."
        show sasha naked
        "And I'm glad to say that Sasha and I have reached that point in ours."
        "Almost as soon as we're naked, I find Sasha kneeling on the floor in front of me."
        hide sasha
        show sasha bj
        with fade
        "She looks so eager to please that I can feel myself getting hard just from the expression on her face."
        "Sasha can't seem to keep her eyes off of my cock as it slowly rises to attention, right in front of her."
        "For a moment, she manages to tear her attention away from it and looks up at me."
        "I can see the unspoken question in her eyes as plainly as if she'd said the words."
        mike.say "You can have it, Sasha."
        "Instantly her expression becomes excited, and she reaches out for take it in her hand."
        mike.say "Uh-uh...hold on a minute there."
        "Sasha freezes, her fingers a mere couple of inches from my cock."
        show sasha bj mike
        mike.say "This is about me getting off, not you."
        mike.say "So the only rule is that it doesn't go anywhere near your pussy."
        mike.say "You got that, Sasha?"
        "She nods, looking more than a little cowed by the restrictions that I've put upon her."
        "But if I'm honest, all this does is turn me on a whole lot more!"
        "Sasha's eyes are almost downcast as she finally starts to handle my cock."
        "And yet she doesn't let that make her attentions appear sullen or resentful."
        "Instead she strokes my balls with a delicate touch to begin with, almost a tickle."
        "This soon becomes more forceful as she massages and squeezes using just one hand."
        show sasha bj mike handmove
        "The other starts to caress the shaft, moving up and down almost in time to her breathing."
        "Sasha forms a ring around my cock with her thumb and finger, encircling the shaft."
        "And then she subjects it to the same increase in force and pressure as she already has my balls."
        "All the time she's sure to tease me with the rest of her body too."
        "She leans forwards, so that her lips are almost within touching distance of the tip."
        "And behind my cock, there's the ever-present backdrop of her breasts, rising and falling."
        if sasha.flags.boobjob:
            "As if noting my interest in her surgically enhanced cleavage, Sasha suddenly lets go of my cock."
            "I open my mouth to tell her off, but before I can shape the words, I feel something else envelop it instead."
            show chest_insert sasha zorder 1 at zoomAt(1, (25, 175))
            show sasha tittyfuck mouthopen with fade
            "Looking down, I'm greeted with the sight of Sasha's huge breasts, sandwiching my cock."
            "They're so big that I literally can't see more than small bit of it at the very base!"
            "And the sensation is like being squashed by a pair of warm, heavy pillows."
            "Noting the look of surprise on my face, Sasha smiles and begins to press her breasts together."
            mike.say "W...wow, Sasha."
            mike.say "That feels amazing!"
            show sasha tittyfuck mouthclosed
            "Sasha smiles at me over her chest, still massaging my cock between them."
            sasha.say "Really?"
            sasha.say "I'm so pleased to hear that!"
            sasha.say "It makes having the surgery so totally worth it!"
            show sasha tittyfuck mouthopen
            "With that, she laughs happily and continues to squeeze my cock between her breasts."
            "Every second that passes makes me more convinced that I'm going to cum."
            "Sasha seems to be working my cock upwards, so that it'll emerge from her cleavage."
            "And when it does, I'm sure she'll get a facial the very next second!"
        else:
            show chest_insert sasha zorder 1 at zoomAt(1, (25, 175))
            "Sasha doesn't seem to notice me staring at her chest."
            show sasha tittyfuck mouthopen
            "Instead her attention remains fixed upon my cock as she works it with her hands."
            "All the time she's licking her lips and leaning in ever closer."
            "Every second that passes makes me more convinced that I'm going to cum."
            "And when I do, I'm sure she'll get a facial the very next second!"
        show chest_insert sasha zorder 1 at zoomAt(1, (25, 370)) with ease
        show mouth_insert sasha zorder 2 at zoomAt(1, (20, 110)) with dissolve
        "But then Sasha takes me by surprise, catching the tip of my cock between her lips the second it emerges."
        show sasha tittyfuck blow
        "Her tongue is wrapped around it the next, and she pulls me into her mouth in one smooth motion."
        "The change from hand-job to blowjob is so sudden that I can't help gasping at the sensation of it."
        "Not that this seems to be a reason for Sasha to pause or even slow down for a second."
        "Instead her head bobs constantly before me, her mouth sucking for all it's worth."
        "Even the sound that's being made deep in her throat as she does so is adding to the effect!"
        "While I might have been wrong the last time, I know that I'm going to come for sure now..."
        menu:
            "Cum in Sasha's mouth":
                "Sasha's been totally into the idea that her mouth's just there for the sake of my pleasure so far."
                "And the way I look at it, there's no need to change that just because I'm about to cum."
                "Taking hold of her head with both hands just to be sure, I feel the inevitable end coming."
                "Sasha gags and almost chokes as the sensation makes me push even further into her mouth."
                show mouth_insert sasha cum
                show sasha tittyfuck cum
                with vpunch
                pause 0.2
                with vpunch
                "At the same time I lose myself, shooting all that I have straight into her throat."
                with vpunch
                "Forced to swallow everything for fear of gagging on it, Sasha slips off of my cock, holding her hands over her mouth."
                hide mouth_insert
                hide chest_insert
            "Cum on Sasha's face":
                "Sasha's been totally into the idea that her mouth's just there for the sake of my pleasure so far."
                "But now that the end's in sight, I feel the urge to mark my territory somehow."
                show sasha tittyfuck normal eyesclosed
                "So just before I lose myself, I pull my cock out of her mouth in one move."
                show sasha tittyfuck eyesopen
                "Sasha gags and coughs in surprise, her eyes widening at the sensation."
                show sasha tittyfuck cum eyesclosed with vpunch
                "And that's when the first streamer of cum hits her square in the face."
                show chest_insert sasha cum with vpunch
                "It splatters across her cheeks and over her nose, dripping downwards as it goes."
                show sasha tittyfuck mouthclosed facecum -cum with vpunch
                "Followed by a second and then a third in quick succession, Sasha's face is soon painted with cum."
        hide mouth_insert
        hide chest_insert
    else:
        if not sasha_naked:
            mike.say "Well, what are you waiting for?"
            mike.say "Strip."
            if sasha.is_sex_slave:
                "Sasha nods curtly, clearly enjoying being given orders by me once more."
            show sasha naked
            "She slowly peels off her underwear, easing it down over her arms."
            "As she raises her arms to drag it over her head, I'm treated to a truly magnificent view."
            "First they rise in sympathy with her arms and shoulders, spreading out and then jiggling with the jerking of her muscles."
            "And then they descend in the same manner, settling onto her chest as gravity returns them to their normal position."
            "Sasha proceeds to then caress them, weighing them in the palms of her hands and even gently squeezing their heavy, fleshy masses."
        else:
            show sasha naked
            "Sasha proceeds to caress her breasts, weighing them in the palms of her hands and even gently squeezing their heavy, fleshy masses."
        if sasha.is_sex_slave:
            sasha.say "Well, [hero.name]...will I do?"
            "I gave a grin that was almost a leer, and pointed to the floor right before me."
            mike.say "I want to fuck those."
            "Sasha again nods in obedience and kneels on the floor in front of me."
        else:
            sasha.say "Do you like them?"
            mike.say "I do."
            sasha.say "I am pretty sure you'll like them even more in a few minutes."
        "She shuffles forwards on her knees, making her enlarged breasts sway back and forth as she comes."
        "I don't see where she produces the lube from, but nevertheless, it appears in her hands."
        "Sasha makes a great show of slowly rubbing the transparent liquid onto her breasts."
        "She once more massages and caresses them as she does so, spreading the lube between them and then over their entire mass."
        "Sasha pinches her enlarged nipples as she sweeps her hands over them, the darkened skin puckering as they become suddenly erect."
        "There's little to do for my sake once she opens my flies and reaches in to pull out my dick."
        hide sasha
        show sasha tittyfuck
        "Placing the tip just beneath her now slick breasts, Sasha moves downwards so that it travels straight up and between them."
        "She makes perhaps a half-dozen more such passes, and then suddenly presses them together so that my dick is caught in the middle."
        "The unexpected pressure makes me gasp audibly as the head emerges, from the cleft."
        show chest_insert sasha zorder 1 at zoomAt(1, (25, 175)) with dissolve
        "Sasha's breasts are baffling mixture of softness and substance, both cushioning and squeezing at the same time."
        "She works me in that same way now, keeping the pressure up as she slides my dick between her breasts."
        "The way that her hands cause them to push together and then return to their resting shape is almost hypnotic to watch."
        "Sasha's new chest seems to almost possess a life of its own as she uses it to tease my and caress me all at the same time."
        show sasha tittyfuck mouthopen
        "All the while, Sasha pants and moans, as if the feeling of my dick is arousing her in the same manner as her breasts are me."
        if sasha.is_sex_slave:
            if sasha.flags.mikeNickname:
                sasha.say "Uh...uh, [hero.name]...please...may I..."
                mike.say "Speak up!"
            sasha.say "[hero.name]...please...may I...touch myself?"
            "I nod, trying not to look too turned on by her desperate desire to masturbate right in front of me."
        $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_low.ogg", loop=True)
        "Sasha wraps her breasts with one arm to keep them around my dick, while her free hand almost darts for her clit."
        "I might not be able to see what she's doing, but soon I can feel the results."
        "Sasha's pants and moans become all the more pronounced, and she begins to move in time with her ministrations to herself."
        "The rhythm this creates is immediate and intense, as she's effectively stimulating herself and then me in turn as she moves in sympathy."
        "Sasha's lips are now puckering and parting, her tongue curling with the increasing pleasure she's feeling."
        "She's in serious danger of finishing me off any moment, but now I can't take my eyes of the appealing sight of her open, gasping lips."
        mike.say "Sasha, take me in your mouth...now."
        if sasha.is_sex_slave:
            if sasha.flags.mikeNickname:
                sasha.say "Uhh...yes, yes...[hero.name]!"
            else:
                sasha.say "Yes [hero.name]!"
        $ renpy.sound.play("sd/moans/sasha/sasha_blowjob_low.ogg", loop=True)
        show sasha tittyfuck blow
        "Hurrying to obey, she wastes no time with kissing or caressing the head of my dick."
        show chest_insert sasha zorder 1 at zoomAt(1, (25, 370)) with ease
        show mouth_insert sasha zorder 2 at zoomAt(1, (20, 110)) with dissolve
        "Instead she simply wraps her lips around it and eagerly swallows as much as she can without either gagging or choking."
        "Still with her own fingers inside of herself, Sasha sucks away at the same intensifying rhythm."
        "I could swear I can feel the very emanations spreading out from her pussy and through her entire body."
        stop sound
        show mouth_insert sasha cum
        show chest_insert sasha cum
        show sasha tittyfuck blow cum
        with vpunch
        $ renpy.sound.play("sd/moans/sasha/sasha_blowjob_swallow.ogg", loop=True)
        pause 0.2
        with vpunch
        "I cum mere seconds later, and Sasha struggles to take it all, keeping it in her mouth and not following her instinct to swallow."
        with vpunch
        "A wave of my hand lets her know that she can release me, and she does so, keeping her eyes on me at the same time."
        stop sound
        if sasha.is_sex_slave:
            show sasha tittyfuck normal facecum eyesclosed -cum
            mike.say "Open wide - let me see it."
            "Sasha obliges me by opening her mouth wide, letting me see the cum still upon her tongue."
            mike.say "Very good...you may swallow it now."
            show mouth_insert sasha -cum
            "She nods demurely as she complies."
            sasha.say "Thank you, [hero.name]."
        hide chest_insert
        hide mouth_insert
    return

label sasha_fuck_date_cowgirl(sexperience_min):
    if sasha.is_sex_slave:
        sasha.say "May I be on top please [hero.name]?"
    else:
        sasha.say "I call going on top!"
    "I nod at this, already enjoying the feeling of her straddling me and not about to object in the slightest."
    mike.say "Sure thing, Sasha - you got it!"
    if hero.sexperience >= 20:
        mike.say "On one condition though."
        if sasha.is_sex_slave:
            sasha.say "Anything you want [hero.name]."
        else:
            "Clearly intrigued by my words, Sasha leans in closer and studies me intently."
            sasha.say "Oh yeah?"
            sasha.say "And just what would that condition be, huh?"
        "I smile as I grip her firmly by the haunches, pulling her down onto me."
        mike.say "That I get to choose where I stick this thing!"
        "Sasha's eyes go wide and her mouth gapes as she yelps in surprise at the sensation of my cock."
        "It's gotten pretty hard in a short space of time, and she's evidently failed to notice."
        "She laughs and makes a show of trying to struggle against my grip."
        "But I can see in her eyes that she's intrigued to discover just where I intend to put it..."
    menu:
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5) and sasha.flags.anal:
            scene sasha cowgirl with fade
            "I can't explain just how much I love the look of anticipation on Sasha's face right now."
            "And the only way I can think to top it is to do something that she's not expecting."
            "So that's why I pull Sasha forwards so that I can angle my cock in just such a way."
            "I have no idea if that give away my intentions, but I don't give her time to dwell on it."
            "Instead I thrust my groin upwards, pushing the head of my cock straight between her buttocks."
            $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_low.ogg", loop=True)
            show sasha cowgirl
            $ sasha.sub += 1
            if sasha.is_sex_slave:
                sasha.say "Oooo!"
                sasha.say "He, he...are you gonna fuck me up the ass, [hero.name]?"
            else:
                sasha.say "Wha...hey!"
                sasha.say "That's my ass...you ass!"
            "A moment later, her words are replaced by a breathless gasping sound."
            "And Sasha keeps right on making the same noise as she sinks down onto my cock."
            "The feeling is almost indescribable from my point of view."
            "Sasha's ass is so tight, yet the pull of gravity is irresistible."
            "And together, these two things mean that my cock is pressed and squeezed the whole time."
            "But as amazing as the feeling is, the sight of Sasha herself makes it that much better."
            "She pants and pouts as she rides me, looming above."
            "And slowly she begins to bounce up and down atop me."
            "Only her hands, gripping my shoulders, seem to be keeping her upright."
            if not sasha.flags.boobjob:
                "Sasha's petite, yet perfectly formed breasts bob up and down as she moves."
                "Their little round nipples as stiff as can be."
            else:
                "Sasha's augmented breasts stand proud of her pale chest."
                "They jiggle and wobble like inflated balloons as she moves."
            $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_medium.ogg", loop=True)
            show sasha cowgirl hands
            "I can't keep from reaching out for them, almost hypnotised by their motions."
            "Sasha's face shows pure pleasure as I begin to caress and then massage her breasts."
            "And when I take her nipples between my fingers and thumbs, her moans become that much deeper than before."
            "For a moment I'm convinced that tweaking Sasha's nipples has kicked her up a gear."
            "As she responds to this attention by beginning to ride me with more force than ever."
            "Soon she seems to be almost bouncing up and down on my cock like a jockey on a runaway horse."
            "The renewed intensity of her movements is all focused on my cock."
            "And before too long, I can feel that I'm about to lose it..."
            if sasha.sub >= 25 and hero.sexperience >= 25:
                menu:
                    "Make her suck you off":
                        stop sound
                        call sasha_fuck_date_bj from _call_sasha_fuck_date_bj
                        return
                    "Just go on":
                        pass
            call cum_reaction (sasha, 'anal', sexperience_min) from _call_cum_reaction_159
            if _return == "anal_inside":
                $ sasha.love += 1
                "What with all of her weight pressing down on me like this, I'm pretty much pinned down."
                "I don't know if I could hope to get out from under Sasha in time, even if I wanted to."
                "And I've certainly got no intention of moving an inch right now!"
                "This means that I lose it while my cock is buried as deep as possible in Sasha's ass."
                $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_orgasm.ogg", loop=True)
                show sasha cowgirl cum with vpunch
                "She literally presses herself down on me and that's when I cum."
                with vpunch
                "To me, it feels as if she's squeezing it out of me."
                with vpunch
                "So god alone knows how it must feel for her!"
                "And it's not like Sasha seems able to tell me that either."
                "Not with the way her head tosses this way and that."
                "Or the way her eyes are almost rolling back into her head."
                "With one last, desperate gasp, she collapses on top of me."
                "And then she slithers around on my chest, exhausted beyond reason."
            elif _return == "anal_outside":
                $ sasha.sub += 1
                "I can feel all of Sasha's weight pressing down on me, but that's not going to stop me."
                "It was a certain angle that got my cock up there in the first place."
                "And so all it takes to reverse the process is another."
                $ renpy.sound.play("sd/moans/sasha/sasha_panting.ogg", loop=True)
                show sasha cowgirl outside -hands
                show chest_insert sasha zorder 1 at zoomAt(1, (875, 55))
                show belly_insert sasha zorder 2 at zoomAt(1, (875, 300))
                "I feel a little like an escape artist, as I twist this way and that to get loose."
                "And the expression on Sasha's face as I do so seems to suggest that she's suitably amazed too."
                show sasha cowgirl outside cum with vpunch
                "She still has the same look on it when I shoot my load up at her a moment later."
                with vpunch
                "But now the surprise must be on account of the way in which my cum splashes all over her."
                show belly_insert sasha cum with vpunch
                "It mostly stripes her belly and thighs."
                show chest_insert sasha cum with vpunch
                "But some manages to spatter over her breasts as well."
                "I lie there, trying to catch my breath as it mingles with the perspiration on her skin."
                hide chest_insert
                hide belly_insert
                "And I'm still laid there when it succumbs to gravity."
                "Running down her body, soaking into the bedclothes beneath her."
            $ sasha.flags.anal += 1
        "Fuck her pussy":
            "Call me old-fashioned if you like."
            "But all I hear right now is the call of Sasha's pussy."
            "And I'm more than eager to answer it!"
            call check_condom_usage (sasha, 150) from _call_check_condom_usage_101
            if _return == False:
                return "leave_without_gain"
            scene sasha cowgirl
            show sasha cowgirl vaginal
            if CONDOM:
                show sasha cowgirl vaginal condom
            "Sasha seems to sense what my intentions are, and she leans forward to make it happen."
            "I hardly have to do a thing, as she takes hold of my cock and guides it between her thighs."
            "She rubs the head against the already slick lips of her pussy, sighing the whole time."
            $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_low.ogg", loop=True)
            "And then she pushes it a little way inside, the sensation belying the subtlety of the movement."
            "Once the head is inside of her, Sasha wriggles and writhes atop me."
            "The motion serves to ease me inside of her, letting her work herself down and onto me."
            "Apart from feeling incredible as she does this to me, the view is something else as well."
            "Every motion of Sasha's hips is mirrored in the way that her chest shakes and bounces above me."
            if not sasha.flags.boobjob:
                "Sasha's small, round and pert breasts bob up and down the whole time."
                "And her nipples top them, becoming stiff and erect."
            else:
                "Sasha's augmented chest is so large that it almost keeps me from seeing her face!"
                "They bounce and jiggle the whole time, like heavy balloons filled with water."
            show sasha cowgirl hands vaginal
            if CONDOM:
                show sasha cowgirl hands vaginal condom
            if sasha.sexperience % 3 == 0:
                "Hypnotised by the sight of them, I have to reach up and take a hold."
                "Sasha's face breaks into a sensual expression as she feels me do so."
                $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_medium.ogg", loop=True)
                "And her moaning becomes that much louder as I massage and squeeze them a moment later."
                "This seems to awaken a new level of appetite in Sasha altogether."
                "Before she was happy to ride my cock at a sedate speed, taking whatever it gave her."
                "But now she begins to quicken her pace and intensify her movements."
                "At the same time her expression tips over into one of almost dazed pleasure."
                "Sasha's mouth begins to hang open, her tongue almost lolling out over her bottom lip."
                "I don't know how much longer she can keep up this pace."
                "But one thing that I do know is I can't keep it up any longer!"
            else:
                "I can't hold back any longer anyway; it feels too good."
                "I start rocking my hips at a quick pace, keeping the angle of her lower body tilted so that each thrust teases over her G-spot."
                $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_medium.ogg", loop=True)
                "With that kind of attention, she's gasping for breath and squirming soon, her lips parted and a flush across her cheeks."
                "I love the lusty look in her eyes."
                "I don't bother to vary my pace or position."
                "It's clear by her whimpers and gasps that I'm doing just what she wants, and it feels wonderful to me too."
                "Her cunt is so tight and I can feel it getting more and more slippery the longer I fuck her."
                "The smell of sex rises in the air, arousing both of us even further."
                "I can tell by the way she trembles and how tight she holds onto my wrists that she's close."
                "Groaning, right on the edge myself, I shorten my thrusts and fuck her harder, entranced by the way her small breasts jiggle and bounce with each impact."
                "Finally, I can't hold it off any more."
                "Just as I shove deep, my cock starting to throb, she cries out and arches to grind against me."
            if sasha.sub >= 25 and hero.sexperience >= 25:
                menu:
                    "Make her suck you off":
                        stop sound
                        call sasha_fuck_date_bj from _call_sasha_fuck_date_bj_1
                        return
                    "Just go on":
                        pass
            call cum_reaction (sasha, 'vaginal', sexperience_min, 190, check_sub=True, sub_min=50) from _call_cum_reaction_160
            if _return == "vaginal_condom":
                $ sasha.love += 1
                "Knowing that I have the condom on means that I don't as much as miss a beat."
                "I keep right on thrusting into Sasha until the very end."
                with vpunch
                "And I don't have to worry about whether or not it's the right thing to do."
                $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_orgasm.ogg", loop=True)
                show sasha cowgirl ahegao vaginal condom with vpunch
                "As the way she reacts and the almost desperate sounds that she makes tell me all I need to know."
                with vpunch
                "Sasha clings to me until the very last, riding it out as we spend the last of our energies."
                "And then she collapses atop me, the only sound being our out of breath panting."
            elif _return == "vaginal_outside":
                $ sasha.sub += 1
                show sasha cowgirl outside -hands
                "As deep into the act as I might be, that doesn't stop me from knowing when to pull out."
                "And I'm sure to do so before it's too late to avoid ending this thing with an accident."
                $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_orgasm.ogg", loop=True)
                show chest_insert sasha zorder 1 at zoomAt(1, (875, 55))
                show belly_insert sasha zorder 2 at zoomAt(1, (875, 300))
                show sasha cowgirl outside with vpunch
                "I hear Sasha yelp in surprise as my cock pulls out of her."
                show sasha cowgirl outside cum with vpunch
                "And she yelps again a moment later as she's spattered with cum."
                show chest_insert sasha cum
                show belly_insert sasha cum
                with vpunch
                "The fact that she was leaning in close means that it covers her breasts and belly."
                "And then drips down again as gravity takes hold, dropping onto my own stomach too."
                hide chest_insert
                hide belly_insert
            elif _return == "vaginal_inside_pill":
                $ sasha.love += 2
                if sasha.sub < 25:
                    sasha.say "Pill...don't...stop!"
                elif sasha.is_sex_slave:
                    sasha.say "Pill...don't...stop!"
                    sasha.say "Please...[hero.name]..."
                else:
                    sasha.say "Oooh...I'm...on...the...pill!"
                "I don't need any more encouragement than those few words."
                $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_orgasm.ogg", loop=True)
                show sasha cowgirl cum ahegao with vpunch
                "And I cum a moment later, deep inside of Sasha's pussy."
                with vpunch
                "When I do, she seems to instantly lose the power of speech."
                with vpunch
                "And instead, she almost babbles as I push her into an orgasm of her own."
            elif _return == "vaginal_inside_pregnant":
                $ sasha.love += 3
                if sasha.sub < 25:
                    "Sasha smiles at me over the curve of her bump, as if to remind me it's okay to cum inside of her."
                elif sasha.is_sex_slave:
                    sasha.say "Please cum inside of me, [hero.name]."
                    sasha.say "I am already carrying your child."
                else:
                    sasha.say "You can cum inside of me, [hero.name]."
                    sasha.say "Because you can't make me MORE pregnant!"
                "That reminder of how much I love and desire her is all that I need."
                $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_orgasm.ogg", loop=True)
                show sasha cowgirl cum ahegao with vpunch
                "And I cum a moment later, deep inside of Sasha's pussy."
                with vpunch
                "When I do, she seems to instantly lose the power of speech."
                with vpunch
                "And instead, she almost babbles as I push her into an orgasm of her own."
            elif _return == "vaginal_inside_sub":
                show sasha cowgirl cum ahegao with vpunch
                "I can feel myself cumming inside of Sasha, and it feels incredible."
                with vpunch
                "But then it dawns on me that it feels a little TOO incredible."
                $ sasha.impregnate()
                hide sasha
                show sasha naked
                show sasha naked blush
                $ sasha.sub += 5
                $ sasha.love -= 5
                stop sound
                sasha.say "Oopsie!"
                sasha.say "I think we forgot the condom!"
            elif _return == "vaginal_inside_mad":
                show sasha cowgirl cum ahegao with vpunch
                "I can feel myself cumming inside of Sasha, and it feels incredible."
                with vpunch
                "But then it dawns on me that it feels a little TOO incredible."
                $ sasha.impregnate()
                hide sasha
                show sasha naked
                show sasha naked angry
                $ sasha.love -= 20
                "At the same time, Sasha looks down at me, a look of growing horror on her face."
                stop sound
                sasha.say "Oh fuck...oh fuck!"
                sasha.say "You came inside of me!"
                "Pretty soon my expression is a perfect mirror of Sasha's."
                "As we both begin to realise the enormity of what we've done."
                hide sasha
            elif _return == "vaginal_inside_happy":
                $ sasha.love += 5
                "I make to pull out of Sasha's pussy, before it's too late to prevent an accident."
                "But then I feel her hands seize my wrists, and she presses down with all her weight."
                mike.say "Sasha - what are you doing?!?"
                if sasha.sub < 50:
                    sasha.say "It's...okay..."
                    sasha.say "Cum inside me...please?"
                elif sasha.is_sex_slave:
                    sasha.say "Cum inside me...please?"
                    sasha.say "Make me yours forever..."
                else:
                    sasha.say "Mmm...I want you to fill me up, [hero.name]."
                    sasha.say "I want you to put a baby inside of me!"
                $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_orgasm.ogg", loop=True)
                show sasha cowgirl cum ahegao with vpunch
                pause 0.25
                with vpunch
                pause 0.25
                with vpunch
                "I cum a moment later, still too shocked and confused to know what's going on and why."
                $ sasha.impregnate()
    stop sound
    return

label sasha_fuck_date_missionary(sexperience_min):
    if hero.sexperience % 3 == 0:
        call check_condom_usage (sasha, 150) from _call_check_condom_usage_102
        if _return == False:
            return "leave_without_gain"
        mike.say "On your back."
        "I want to be able to see the desire and pleasure in her eyes while I'm fucking her."
        scene bg black
        show sasha missionary nomc
        if sasha_ropes:
            show sasha missionary rope
        with fade
        "Sasha gets onto the bed, leaning back and spreading her legs, knees bent."
        "She smiles seductively and lets one hand drift between her thighs, idly rubbing her clit while waiting for me."
        "The view is incredible."
        show sasha missionary -nomc
        if CONDOM:
            show sasha missionary condom
        with fade
        "I crawl up from the foot of the bed until my knees are between her parted thighs."
        "Grinning wickedly at her, I reach back and take her ankles, lifting them to my shoulders; Sasha's flexible enough to enjoy this."
        "I lean forward, pushing her legs back and elevating her hips in the process, letting my cock rub against her pussy while I steady my hands on the bed to either side of her shoulders."
        if sasha.is_sex_slave:
            sasha.say "Please, fuck me hard [hero.name]."
        else:
            sasha.say "Fuck me hard."
        "Her words ignites higher passions and makes me groan. I certainly intend to."
        show sasha missionary vaginal at stepback(speed=0.1, h=-10, v=-20)
        $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_low.ogg", loop=False)
        "This position makes her so tight as I push in, and the angle forces the head of my cock to rub firmly at the front of her walls, right along her G-spot."
        show sasha missionary sashapain
        "At the first brush to that tender patch of flesh, she arches with a moan, then flops back to lay flat, her hands moving to grip my wrists as though she's bracing herself."
        "Once I'm buried deep in her clingy cunt, I hold still for a minute so she has time to adjust to her walls being stretched for me."
        "It feels incredible, how tight her pussy grips my shaft, and I savour it during those slow-passing moments."
        "Lust darkens her eyes as she stares hotly up at me, clearly growing impatient."
        stop sound
        if sasha.flags.mikeNickname:
            sasha.say "I beg you [hero.name]..."
        else:
            sasha.say "Fuck me..."
        "I can't hold back any longer anyway; it feels too good."
        $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_low.ogg", loop=True)
        show sasha missionary at stepback(speed=0.1, h=-10, v=-20)
        "I start rocking my hips at a quick pace, keeping the angle of her lower body tilted so that each thrust teases over her G-spot."
        "With that kind of attention, she's gasping for breath and squirming soon, her lips parted and a flush across her cheeks."
        "I love the lusty look in her eyes."
        show sasha missionary at stepback(speed=0.1, h=-10, v=-20)
        "I don't bother to vary my pace or position."
        "It's clear by her whimpers and gasps that I'm doing just what she wants, and it feels wonderful to me too."
        "Her cunt is so tight and I can feel it getting more and more slippery the longer I fuck her."
        show sasha missionary at stepback(speed=0.1, h=-10, v=-20)
        "The smell of sex rises in the air, arousing both of us even further."
        "I can tell by the way she trembles and how tight she holds onto my wrists that she's close."
        $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_medium.ogg", loop=True)
        show sasha missionary speed at stepback(speed=0.07, h=-10, v=-15)
        pause 0.2
        show sasha missionary at stepback(speed=0.07, h=-10, v=-15)
        "Groaning, right on the edge myself, I shorten my thrusts and fuck her harder, entranced by the way her small breasts jiggle and bounce with each impact."
        "Finally, I can't hold it off any more."
        show sasha missionary at stepback(speed=0.07, h=-10, v=-15)
        pause 0.2
        show sasha missionary at stepback(speed=0.07, h=-10, v=-15)
        "Just as I shove deep, my cock starting to throb, she cries out and arches to grind against me."
        if sasha.sub >= 25 and hero.sexperience >= 25:
            menu:
                "Make her suck you off":
                    stop sound
                    call sasha_fuck_date_bj from _call_sasha_fuck_date_bj_2
                    return
                "Just go on":
                    pass
        $ choking = False
        if hero.sexperience >= 25:
            menu:
                "Choke her":
                    "On an instinctive whim, I move one hand to grasp her neck, strangling her throat."
                    "Her eyes get huge and she bucks hard against me while she struggles for breath, lost in sudden euphoria that draws her climax out longer."
                    "She gets my pubic hair soaked and I can feel her hot nectar dripping down my balls."
                    show sasha missionary sashacum
                    $ sasha.sub += 1
                    $ choking = True
                "Keep going":
                    pass
        call cum_reaction (sasha, 'vaginal', sexperience_min) from _call_cum_reaction_275
        if _return == "vaginal_condom":
            show sasha missionary sashacum condom with vpunch
            pause 0.25
            with vpunch
            pause 0.25
            show sasha missionary -speed with vpunch
            if choking:
                "Thrilled to have found something she likes so much, I grind deep into her as I cum."
                "It's all I can do not to collapse on top of her."
                "I let go of her neck and she gasps for breath and lets out a low whimper of intense pleasure."
            else:
                "It's a much harder orgasm than I expected; soon the condom is completely full of my jizz."
                "It's all I can do not to collapse on top of her."
        elif _return == "vaginal_outside":
            show sasha missionary -vaginal with vpunch
            "At the very last minute, I pull my dick out."
            show sasha missionary sashacum -speed with vpunch
            "I groan again as the cum explodes from my cock, letting Sasha know how thoroughly I enjoyed her beautiful pussy."
            if CONDOM:
                show sasha missionary cum
                "The condom is almost a disappointment, catching all of the cum, but it doesn't matter. The orgasm itself, not my first of the night, is absolutely incredible."
            else:
                show sasha missionary cum with vpunch
                "My load explodes out of my cock, covering her belly with globs of the sticky liquid."
                show sasha missionary -cum bodycum with vpunch
                "I just stand there for a moment, admiring my handiwork."
        else:
            show sasha missionary sashacum creampie with vpunch
            pause 0.25
            with vpunch
            pause 0.25
            show sasha missionary -speed with vpunch
            if choking:
                "Thrilled to have found something she likes so much, I grind deep into her as I cum, spurting jets of hot sticky seed deep into her squeezing tunnel."
                "It's all I can do not to collapse on top of her."
                "I let go of her neck and she gasps for breath and lets out a low whimper of intense pleasure."
            else:
                "It's a much harder orgasm than I expected; soon my jizz is dripping from her filled pussy."
                "It's all I can do not to collapse on top of her."
            $ sasha.impregnate()
    else:
        scene bg black
        show sasha missionary nomc
        with fade
        "Sasha climbs onto the bed and lay down, legs hitched up and spread apart."
        "And right now she's leaning her head on one hand, the other idly playing with her exposed pussy!"
        if sasha.sub >= 25:
            sasha.say "We're going to do whatever you want, [hero.name]!"
        elif sasha.sub <= -25:
            sasha.say "Do whatever it takes to satisfy my voracious pussy!"
        else:
            sasha.say "Fuck like a couple of animals?"
        "I blink a couple of times, genuinely stunned by what I'm seeing."
        "And the best I can manage to do is nod and begin to stutter a reply."
        mike.say "Y...yeah, Sasha..."
        mike.say "You totally read my mind!"
        "Sasha chuckles as she crooks her finger to beckon me onto the bed."
        "And I'm already stripping off my own clothes as I obey her."
        "But it doesn't take long for her eyes to wander downwards."
        "Checking out the prospect of my cock as it gets rapidly harder and begins to stand to attention."
        menu:
            "Fuck her pussy":
                "I must be naked and across the room in no more than a couple of seconds."
                "Ready to throw myself onto the bed and literally land atop Sasha."
                call check_condom_usage (sasha, 150) from _call_check_condom_usage_172
                if _return == False:
                    return "leave_without_gain"
                "I can't remember the last time that someone got me as hard as I am right now."
                "And so all that I can think about is getting myself some of that sweet little pussy."
                show sasha missionary -nomc
                if CONDOM:
                    show sasha missionary condom
                with fade
                "But almost as soon as I clamber on top of Sasha, I realise that it's not just me."
                "Because she reaches up and literally grabs hold of me, pulling me down and onto her."
                $ renpy.sound.play("sd/moans/sasha/sasha_panting.ogg", loop=True)
                "And that's when I feel the shaft of my cock press against her lips for the first time."
                "As it happens, a shudder of pure pleasure seems to spread out and make me tingle all over."
                "All thanks to the fact that Sasha's already warm and wet down there, more than ready for me."
                "It's situations like this that keep a guy awake at night, worrying about what to say and do."
                "But somehow, now that it's actually happening, my body and brain just seem to go into autopilot."
                "My hips slide between Sasha's, aiming the head of my cock straight at her pussy."
                "And at the same time, my hands explore her body above the waist."
                "This means that I'm caressing her breasts and squeezing her nipples."
                "All while stroking her back and forth down below, trying to find my way inside."
                "Sasha responds in kind, wrapping herself around me and clinging on tightly."
                "Pulling me ever closer, as if in the hope of making it happen faster."
                "But there's no need for her to worry, as nature soon takes its course."
                stop sound
                show sasha missionary sashapain
                sasha.say "Mmm…"
                sasha.say "Oh..."
                sasha.say "Oh fuck!"
                $ renpy.sound.play("sd/moans/sasha/sasha_panting.ogg", loop=True)
                show sasha missionary sashanormal
                "I can't help nodding my head at the sounds Sasha's making and the things she's saying."
                "And in all likelihood, I'd be echoing them myself, if I were capable of speech right now."
                "But the only thing I can do is hold on and push forwards as she begins to open up to me."
                "I've been wanting this for so long, doing all that I could to make it happen."
                "And now that it is, I'm totally overwhelmed."
                $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_low.ogg", loop=True)
                show sasha missionary vaginal at stepback(speed=0.1, h=-10, v=-20)
                "As the head of my cock pushes into Sasha, time seems to slow to a crawl."
                "I feel ever fraction of an inch as it happens, every degree as lower myself."
                "So by the point where I can't go any further, my mind is already totally blown."
                "Part of me feels like I should just stay there forever, never move again."
                show sasha missionary sashapain at stepback(speed=0.1, h=-10, v=-20)
                "Sasha certainly seems to be enjoying the position I'm in, wriggling and writhing beneath me."
                "But I slowly feel the desire for more rise up inside of me, making me start to move."
                show sasha missionary sashanormal at stepback(speed=0.1, h=-10, v=-20)
                "I'd like to say that I make long, sweeping thrusts into Sasha."
                "That my love-making is like something out of a tasteful Hollywood movie."
                $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_medium.ogg", loop=True)
                show sasha missionary speed at stepback(speed=0.07, h=-10, v=-15)
                pause 0.2
                show sasha missionary at stepback(speed=0.07, h=-10, v=-15)
                "In truth I start rocking my hips, rifling my cock in and out of Sasha."
                "Almost like I'm desperate to mount her and stake my claim."
                "Luckily for me, the effects of what I'm doing are more impressive than the visuals."
                show sasha missionary sashapain at stepback(speed=0.07, h=-10, v=-15)
                pause 0.2
                show sasha missionary at stepback(speed=0.07, h=-10, v=-15)
                "Because Sasha is already throwing her head back onto the bed."
                "And she's doing all that she can to angle her groin towards me as well."
                "I can feel her hands all over my shoulders and sides too."
                show sasha missionary sashanormal at stepback(speed=0.07, h=-10, v=-15)
                pause 0.2
                show sasha missionary at stepback(speed=0.07, h=-10, v=-15)
                "Trying to hold onto me, as if she's worried that the pleasure might stop."
                if hero.sexperience >= 25:
                    menu:
                        "Choke her":
                            "Suddenly an idea hits me, one that I suspect Sasha will be into."
                            "I reach up and put my hands around her neck gently covering them."
                            "And when Sasha makes no attempt to push me away, I apply just a little pressure."
                            "I'm careful to go slowly, letting her get used to the sensation."
                            "Always ready to let go if she shows the slightest sign of discomfort or distress."
                            "But to my relief and delight, my efforts seem to enhance Sasha's pleasure."
                            show sasha missionary sashacum
                            "She holds onto me even more tightly than before, the look in her eyes urging me on."
                            "And so I keep on doing what I'm doing, reaping the benefits as I do so."
                            $ sasha.sub += 1
                        "Do not choke Sasha":
                            "I could take a risk and do something pretty crazy right now."
                            "But the truth is that I'm too worried about making the wrong choice."
                            "And the last thing that I want to do is blow it with Sasha."
                            "Especially after we've made it so far and had so much fun already."
                            "So instead I double down on what I'm doing to her right now."
                show sasha missionary sashanormal at stepback(speed=0.07, h=-10, v=-15)
                pause 0.2
                show sasha missionary at stepback(speed=0.07, h=-10, v=-15)
                "It's not long before I can feel the sensation of Sasha's muscles starting to contract."
                "As if the whole of her body is trying to squeeze my cock like one massive fist."
                "Sasha looks up at me, almost like she's pleading for me to do more than I already have."
                "Silently begging for the final push that will see her find release."
                $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_high.ogg", loop=True)
                show sasha missionary sweat at stepback(speed=0.05, h=-10, v=-15)
                pause 0.15
                show sasha missionary at stepback(speed=0.05, h=-10, v=-15)
                "With that in mind, I start to thrust into Sasha like never before."
                "Putting all the strength that I have left behind them and holding nothing back."
                "Soon enough her cheeks begin to flush and her eyes roll back into her head."
                "My attentions make Sasha's entire body shake, her perfect little breasts bounce up and down."
                show sasha missionary sashapain at stepback(speed=0.05, h=-10, v=-15)
                pause 0.15
                show sasha missionary at stepback(speed=0.05, h=-10, v=-15)
                "I know that she's cuming when she arches her back and her mouth falls open."
                "But at the same time she doesn't make a sound, simply moving her lips in silence."
                "I've been watching Sasha so closely that there's nothing else on mind."
                show sasha missionary at stepback(speed=0.05, h=-10, v=-15)
                pause 0.15
                show sasha missionary at stepback(speed=0.05, h=-10, v=-15)
                "And so it comes as a genuine surprise when I feel myself starting to jerk and twitch too."
                "Just in time I realise that she's swept me along with her, that I'm cuming too!"
                call cum_reaction (sasha, 'vaginal', sexperience_min) from _call_cum_reaction_311
                if _return == "vaginal_condom":
                    "I can hardly feel the condom that I'm wearing right now."
                    "But the knowledge that it's there means I can keep on going."
                    show sasha missionary sashacum with vpunch
                    "Pushing as deep into Sasha as possible as I shoot my load."
                    play sound "sd/moans/sasha/sasha_moans_light_orgasm.ogg"
                    queue sound "sd/moans/sasha/sasha_panting.ogg" loop
                    show sasha missionary sashacum -speed with vpunch
                    "Making her moan and whimper as I explode inside of her pussy."
                elif _return == "vaginal_outside":
                    "It takes all of my concentration to hold on and pull backwards."
                    show sasha missionary -vaginal with vpunch
                    "Dragging myself all the way out of Sasha before the inevitable happens."
                    show sasha missionary sashacum with vpunch
                    "And it feels crazy after pushing forwards with such intensity all this time."
                    play sound "sd/moans/sasha/sasha_moans_light_orgasm.ogg"
                    queue sound "sd/moans/sasha/sasha_panting.ogg" loop
                    show sasha missionary cum -speed with vpunch
                    "But the sensation is still crazily intense, making her whimper and moan."
                    if CONDOM:
                        "While I shoot my load."
                    else:
                        show sasha missionary -cum bodycum with vpunch
                        "While I shoot my load over her slick belly and thighs."
                elif _return == "vaginal_inside_pill":
                    show sasha missionary sashanormal
                    sasha.say "Fill me up..."
                    sasha.say "It's okay...I'm on the pill!"
                    "I silently thank Sasha for the timely reminder."
                    show sasha missionary sashapain with vpunch
                    "But there's no way that I can hold back now, not even if I wanted too."
                    "All I can do is keep on going, right until the very last moment."
                    show sasha missionary sashacum creampie -speed with vpunch
                    "Pushing as deep into Sasha as possible as I shoot my load."
                    play sound "sd/moans/sasha/sasha_moans_light_orgasm.ogg"
                    queue sound "sd/moans/sasha/sasha_panting.ogg" loop
                    "Making her moan and whimper as I explode inside of her pussy."
                elif _return == "vaginal_inside_pregnant":
                    show sasha missionary sashanormal
                    sasha.say "Fill me up..."
                    sasha.say "It's okay...I'm pregnant!"
                    "I'm not sure how I could have forgotten that particular fact."
                    show sasha missionary sashapain with vpunch
                    "But there's no way that I can hold back now, not even if I wanted too."
                    "All I can do is keep on going, right until the very last moment."
                    show sasha missionary sashacum creampie -speed with vpunch
                    "Pushing as deep into Sasha as possible as I shoot my load."
                    play sound "sd/moans/sasha/sasha_moans_light_orgasm.ogg"
                    queue sound "sd/moans/sasha/sasha_panting.ogg" loop
                    "Making her moan and whimper as I explode inside of her pussy."
                elif _return == "vaginal_inside_mad":
                    show sasha missionary sashanormal
                    sasha.say "Pull out, [hero.name]…"
                    sasha.say "Quick, before it's too late!"
                    show sasha missionary sashapain with vpunch
                    "There's no way that I can hold back now, not even if I wanted too."
                    "All I can do is keep on going, right until the very last moment."
                    show sasha missionary sashacum creampie -speed with vpunch
                    "Pushing as deep into Sasha as possible as I shoot my load."
                    play sound "sd/moans/sasha/sasha_moans_light_orgasm.ogg"
                    queue sound "sd/moans/sasha/sasha_panting.ogg" loop
                    "Making her moan and whimper as I explode inside of her pussy."
                    $ sasha.impregnate()
                    "With her looking back over her shoulder at me in horror."
                elif _return == "vaginal_inside_happy":
                    "It takes all of my concentration to hold on and pull backwards."
                    "Dragging myself all the way out of Sasha before the inevitable happens."
                    "Or at least that's what was supposed to happen, until Sasha foils my efforts."
                    mike.say "Sasha..."
                    mike.say "What are you doing?!?"
                    show sasha missionary sashapain with vpunch
                    "But there's no way that I can hold back now, not even if I wanted too."
                    "All I can do is keep on going, right until the very last moment."
                    show sasha missionary sashacum creampie -speed with vpunch
                    "Pushing as deep into Sasha as possible as I shoot my load."
                    play sound "sd/moans/sasha/sasha_moans_light_orgasm.ogg"
                    queue sound "sd/moans/sasha/sasha_panting.ogg" loop
                    "Making her moan and whimper as I explode inside of her pussy."
                    $ sasha.impregnate()
                    "But my head is filled with panic and amazement as I wonder why."
                    "Why would Sasha do something as crazy as that?"
            "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
                "I must be naked and across the room in no more than a couple of seconds."
                "Ready to throw myself onto the bed and literally land atop Sasha."
                "I can't remember the last time that someone got me as hard as I am right now."
                "And so all that I can think about is getting myself some of that sweet little ass."
                show sasha missionary -nomc with fade
                "But almost as soon as I clamber on top of Sasha, I realise that it's not just me."
                "Because she reaches up and literally grabs hold of me, pulling me down and onto her."
                $ renpy.sound.play("sd/moans/sasha/sasha_panting.ogg", loop=True)
                "And that's when I feel the shaft of my cock press against her hole for the first time."
                "As it happens, a shudder of pure pleasure seems to spread out and make me tingle all over."
                "All thanks to the fact that Sasha's already warm and slippery down there, more than ready for me."
                "It's situations like this that keep a guy awake at night, worrying about what to say and do."
                "But somehow, now that it's actually happening, my body and brain just seem to go into autopilot."
                "My hips slide between Sasha's, aiming the head of my cock straight at her hole."
                "And at the same time, my hands explore her body above the waist."
                "This means that I'm caressing her breasts and squeezing her nipples."
                "All while stroking her back and forth down below, trying to find my way inside."
                "Sasha responds in kind, wrapping herself around me and clinging on tightly."
                "Pulling me ever closer, as if in the hope of making it happen faster."
                "But there's no need for her to worry, as nature soon takes its course."
                stop sound
                show sasha missionary sashapain
                sasha.say "Mmm…"
                sasha.say "Oh..."
                sasha.say "Oh fuck!"
                $ renpy.sound.play("sd/moans/sasha/sasha_panting.ogg", loop=True)
                show sasha missionary sashanormal
                "I can't help nodding my head at the sounds Sasha's making and the things she's saying."
                "And in all likelihood, I'd be echoing them myself, if I were capable of speech right now."
                "But the only thing I can do is hold on and push forwards as she begins to open up to me."
                "I've been wanting this for so long, doing all that I could to make it happen."
                "And now that it is, I'm totally overwhelmed."
                $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_low.ogg", loop=True)
                show sasha missionary anal at stepback(speed=0.1, h=-10, v=-20)
                "As the head of my cock pushes into Sasha, time seems to slow to a crawl."
                "I feel ever fraction of an inch as it happens, every degree as lower myself."
                "So by the point where I can't go any further, my mind is already totally blown."
                "Part of me feels like I should just stay there forever, never move again."
                show sasha missionary sashapain at stepback(speed=0.1, h=-10, v=-20)
                "Sasha certainly seems to be enjoying the position I'm in, wriggling and writhing beneath me."
                "But I slowly feel the desire for more rise up inside of me, making me start to move."
                show sasha missionary sashanormal at stepback(speed=0.1, h=-10, v=-20)
                "I'd like to say that I make long, sweeping thrusts into Sasha."
                "That my love-making is like something out of a tasteful Hollywood movie."
                $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_medium.ogg", loop=True)
                show sasha missionary speed at stepback(speed=0.07, h=-10, v=-15)
                pause 0.2
                show sasha missionary at stepback(speed=0.07, h=-10, v=-15)
                "In truth I start rocking my hips, rifling my cock in and out of Sasha."
                "Almost like I'm desperate to mount her and stake my claim."
                "Luckily for me, the effects of what I'm doing are more impressive than the visuals."
                show sasha missionary sashapain at stepback(speed=0.07, h=-10, v=-15)
                pause 0.2
                show sasha missionary at stepback(speed=0.07, h=-10, v=-15)
                "Because Sasha is already throwing her head back onto the bed."
                "And she's doing all that she can to angle her groin towards me as well."
                "I can feel her hands all over my shoulders and sides too."
                show sasha missionary sashanormal at stepback(speed=0.07, h=-10, v=-15)
                pause 0.2
                show sasha missionary at stepback(speed=0.07, h=-10, v=-15)
                "Trying to hold onto me, as if she's worried that the pleasure might stop."
                if hero.sexperience >= 25:
                    menu:
                        "Choke her":
                            "Suddenly an idea hits me, one that I suspect Sasha will be into."
                            "I reach up and put my hands around her neck gently covering them."
                            "And when Sasha makes no attempt to push me away, I apply just a little pressure."
                            "I'm careful to go slowly, letting her get used to the sensation."
                            "Always ready to let go if she shows the slightest sign of discomfort or distress."
                            "But to my relief and delight, my efforts seem to enhance Sasha's pleasure."
                            show sasha missionary sashacum
                            "She holds onto me even more tightly than before, the look in her eyes urging me on."
                            "And so I keep on doing what I'm doing, reaping the benefits as I do so."
                            $ sasha.sub += 1
                        "Do not choke Sasha":
                            "I could take a risk and do something pretty crazy right now."
                            "But the truth is that I'm too worried about making the wrong choice."
                            "And the last thing that I want to do is blow it with Sasha."
                            "Especially after we've made it so far and had so much fun already."
                            "So instead I double down on what I'm doing to her right now."
                show sasha missionary sashanormal at stepback(speed=0.07, h=-10, v=-15)
                pause 0.2
                show sasha missionary at stepback(speed=0.07, h=-10, v=-15)
                "It's not long before I can feel the sensation of Sasha's muscles starting to contract."
                "As if the whole of her body is trying to squeeze my cock like one massive fist."
                "Sasha looks up at me, almost like she's pleading for me to do more than I already have."
                "Silently begging for the final push that will see her find release."
                $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_high.ogg", loop=True)
                show sasha missionary sweat at stepback(speed=0.05, h=-10, v=-15)
                pause 0.15
                show sasha missionary at stepback(speed=0.05, h=-10, v=-15)
                "With that in mind, I start to thrust into Sasha like never before."
                "Putting all the strength that I have left behind them and holding nothing back."
                "Soon enough her cheeks begin to flush and her eyes roll back into her head."
                "My attentions make Sasha's entire body shake, her perfect little breasts bounce up and down."
                show sasha missionary sashapain at stepback(speed=0.05, h=-10, v=-15)
                pause 0.15
                show sasha missionary at stepback(speed=0.05, h=-10, v=-15)
                "I know that she's cuming when she arches her back and her mouth falls open."
                "But at the same time she doesn't make a sound, simply moving her lips in silence."
                "I've been watching Sasha so closely that there's nothing else on mind."
                show sasha missionary at stepback(speed=0.05, h=-10, v=-15)
                pause 0.15
                show sasha missionary at stepback(speed=0.05, h=-10, v=-15)
                "And so it comes as a genuine surprise when I feel myself starting to jerk and twitch too."
                "Just in time I realise that she's swept me along with her, that I'm cuming too!"
                call cum_reaction (sasha, 'anal', sexperience_min) from _call_cum_reaction_312
                if _return == "anal_inside":
                    "There's no way that I can hold back now, not even if I wanted too."
                    show sasha missionary sashapain with vpunch
                    "All I can do is keep on going, right until the very last moment."
                    "Pushing as deep into Sasha as possible as I shoot my load."
                    play sound "sd/moans/sasha/sasha_moans_hard_orgasm.ogg"
                    queue sound "sd/moans/sasha/sasha_panting.ogg" loop
                    show sasha missionary sashacum creampie with vpunch
                    "Making her moan and whimper as I explode inside of her ass."
                elif _return == "anal_outside":
                    "It takes all of my concentration to hold on and pull backwards."
                    show sasha missionary -anal with vpunch
                    "Dragging myself all the way out of Sasha's ass before the inevitable happens."
                    show sasha missionary sashacum with vpunch
                    "And it feels crazy after pushing forwards with such intensity all this time."
                    play sound "sd/moans/sasha/sasha_moans_hard_orgasm.ogg"
                    queue sound "sd/moans/sasha/sasha_panting.ogg" loop
                    show sasha missionary cum with vpunch
                    "But the sensation is still crazily intense, making her whimper and moan."
                    show sasha missionary -cum bodycum with vpunch
                    "While I shoot my load over her slick belly and thighs."
        "As soon as I'm spent, I collapse and fall face down at Sasha's side."
        "She seems to be in the same position, simply lying still on her back."
        "Part of me wants to say something, to make a really witty comment."
        "Or at the very least to thank her for totally blowing my mind like that."
        "But there's no way I can manage it, because I'm simply too exhausted."
        "The best I can manage is to half throw an arm over Sasha's immobile form."
        "Hoping that she knows how grateful I am to have been a part of something so amazing."
        call stop_all_sfx from _call_stop_all_sfx_38
    return

label sasha_fuck_date_standing(sexperience_min):
    if hero.sexperience % 3 == 0:
        call check_condom_usage (sasha, 150) from _call_check_condom_usage_103
        if _return == False:
            return "leave_without_gain"
        mike.say "Come here."
        "I lead Sasha over to the dresser."
        mike.say "Bend over."
        "She blinks, then grins when she realizes why I've chosen this spot."
        "We can watch each other in the mirror while I fuck her; it will be incredibly hot."
        "Sasha bends forward and braces her hands on the edge of the dresser, looking at me expectantly in the reflection."
        "Tense with anticipation, I put my hands on my hips and rub my cock against her slick pussy until the head nudges at her entrance."
        "With a low groan that Sasha echoes, I slowly push in until my rod is buried to the hilt."
        scene bg black
        show sasha stand vaginal normal at center, zoomAt(1.05, (640, 740))
        if sasha_ropes:
            show sasha stand rope
        if sasha_beads:
            show sasha stand beads beads1
        if CONDOM:
            show sasha stand condom
        if sasha.is_sex_slave:
            sasha.say "Do whatever you want [hero.name]."
        else:
            sasha.say "Nn.. fuck me hard, [hero.name]."
        "Lust is glowing in her eyes. She looks so incredibly sexy in the mirror."
        if sasha.is_sex_slave:
            mike.say "That's what I intend to do little slave."
        else:
            mike.say "As hard as you want."
        $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_low.ogg", loop=True)
        show sasha stand at stepback(speed=0.1, h=10, v=5)
        "Putting action to words, I pull halfway out of the heated grip of her cunt, then plunge back in hard enough to make those pretty little tits sway."
        "Being able to watch her reaction, watch her body in the mirror is so much hotter than I thought it would be."
        "She moans for me as I start thrusting, pulling only partly out before driving hard back inside, not wanting to be free of the snug cling of her pussy for long."
        "It feels so good, hot and wet walls squeezing my shaft."
        "Her expression is one of total desire, full lips parted, dark eyes half-closed and gleaming with lust, a pink flush spreading over her cheeks."
        $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_medium.ogg", loop=True)
        show sasha stand at stepback(speed=0.1, h=10, v=5)
        "Each thrust makes higher pitched moans come from her throat, getting louder and louder every time."
        "A few groans of my own join her sounds, along with the slap of flesh on flesh each time I shove deep."
        show sasha stand at stepback(speed=0.1, h=10, v=5)
        "I can feel wetness on my balls when they smack against her pussy and I can't help imagining how the insides of her thighs must glisten with how soaked she is."
        "I lose myself in the hard and fast rhythm; we watch each other in the mirror, getting more turned on by being able to see how turned on the other is."
        "Using the mirror was a perfect idea."
        show sasha stand pleasure blush
        stop sound
        if sasha.is_sex_slave:
            sasha.say "Can I cum?"
            sasha.say "Please [hero.name], I am so close..."
            mike.say "You have been a good little slave, you may enjoy yourself now."
            sasha.say "Thank you [hero.name]."
        else:
            sasha.say "Harder!"
            sasha.say "I'm so close..."
            "I'm happy to oblige, right on the edge myself."
        $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_high.ogg", loop=True)
        "Her head lowers and I frown; I want to see that pretty face painted with bliss."
        "One hand leaves the curve of her hip, moving to grip her hair initially, but my fingers find her neck first."
        "Grinning wickedly, I grip it instead."
        "She cries out, partly in surprise and partly in pleasure, the sound cutting off as my fingers squeezes at her throat."
        "Sasha lifts her head, bowing her back and raising her shoulders, pushing at the edge of the dresser."
        "Shock widens her eyes, but they glitter with intense desire; it seems she likes being choked a little."
        $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_orgasm.ogg", loop=True)
        "That combined with the harder thrusts proves enough to send her over the edge."
        show sasha stand normal blush
        "I gasp as I feel the hot wash of nectar splash against my balls and I shove deep, wanting to feel every quiver and clutch of her orgasm."
        "I can't hold back any longer anyway; it feels too good."
        "I start rocking my hips at a quick pace, keeping the angle of her lower body tilted so that each thrust teases over her G-spot."
        show sasha stand pleasure speed at stepback(speed=0.1, h=10, v=5)
        pause 0.2
        show sasha stand at stepback(speed=0.1, h=10, v=5)
        "With that kind of attention, she's gasping for breath and squirming soon, her lips parted and a flush across her cheeks."
        "I love the lusty look in her eyes."
        "I don't bother to vary my pace or position."
        "It's clear by her whimpers and gasps that I'm doing just what she wants, and it feels wonderful to me too."
        show sasha stand at stepback(speed=0.1, h=10, v=5)
        pause 0.2
        show sasha stand at stepback(speed=0.1, h=10, v=5)
        "Her cunt is so tight and I can feel it getting more and more slippery the longer I fuck her."
        "The smell of sex rises in the air, arousing both of us even further."
        "I can tell by the way she trembles and how tight she holds onto my wrists that she's close."
        show sasha stand at stepback(speed=0.07, h=10, v=5)
        pause 0.15
        show sasha stand at stepback(speed=0.07, h=10, v=5)
        "Groaning, right on the edge myself, I shorten my thrusts and fuck her harder, entranced by the way her small breasts jiggle and bounce with each impact."
        "Finally, I can't hold it off any more."
        show sasha stand at stepback(speed=0.07, h=10, v=5)
        pause 0.15
        show sasha stand at stepback(speed=0.07, h=10, v=5)
        "Just as I shove deep, my cock starting to throb, she cries out and arches to grind against me."
        if sasha.sub >= 25 and hero.sexperience >= 25:
            menu:
                "Make her suck you off":
                    stop sound
                    call sasha_fuck_date_bj from _call_sasha_fuck_date_bj_3
                    return
                "Just go on":
                    pass
        call cum_reaction (sasha, 'vaginal', sexperience_min) from _call_cum_reaction_161
        if _return == "vaginal_condom":
            "It's a much harder orgasm than I expected; soon the condom is completely full of my jizz."
        elif _return == "vaginal_outside":
            show sasha stand -vaginal
            "At the very last minute I pull my throbbing cock out of her pussy. I barely have time to clear her vulva before I explode."
            if CONDOM:
                show sasha stand cum with vpunch
                pause 0.25
                with vpunch
                pause 0.25
                with vpunch
                "The condom fills with my sticky fluid."
            else:
                show sasha stand cumshot with vpunch
                pause 0.25
                with vpunch
                pause 0.25
                with vpunch
                "My jizz spurts several times, covering her beautiful ass with hot, sticky semen."
                show sasha stand cum onbody -cumshot
        else:
            "It's a much harder orgasm than I expected; soon my jizz is dripping from her filled pussy."
            show sasha stand creampie ahegao with hpunch
            pause 0.25
            with hpunch
            pause 0.25
            with hpunch
            if _return not in ["vaginal_inside_pill", "vaginal_inside_pregnant"]:
                $ sasha.impregnate()
        "As my climax ends and hers dies down to shudders, we both fall on the bed."
        "Several moments of silence stretch as we both struggle to catch our breath."
    else:
        if sasha.sub >= 25:
            "Without saying a word, I take hold of Sasha's hand."
            "She offers no resistance as I lead her over to the corner of the room."
            "And she doesn't object when I stand her right in front of the dresser either."
        elif sasha.sub <= -25:
            "Without saying a word, Sasha takes hold of my hand."
            "I offer no resistance as she leads me over to the corner of the room."
            "And once we're there, I stand behind her as she positions herself in front of the dresser."
        else:
            mike.say "Sasha..."
            mike.say "Come over here."
            "I take hold of Sasha's hand and lead her over to the corner of the room."
            "And then I stand her in front of the dresser."
        scene bg black
        show sasha stand at center, zoomAt(1.05, (640, 740)) with fade
        mike.say "I think we're both going to have a great view from here!"
        "Sasha nods and chuckles, letting me know that she approves of what I have in mind."
        "And then she leans back, rubbing herself against me like a cat on heat."
        sasha.say "Mmm…"
        sasha.say "This is going to be so much fun!"
        mike.say "Then what are we waiting for?"
        mike.say "Bend over!"
        "Sasha nods and does as she's told, leaning towards the surface of the mirror."
        "At the same time she pushes her ass backwards, giving it a little wiggle for good measure."
        if sasha.sub >= 25:
            if sasha.flags.mikeNickname:
                sasha.say "I'm all yours, [hero.name] - what are you waiting for?"
            else:
                sasha.say "I'm all yours, Master - what are you waiting for?"
        elif sasha.sub <= -25:
            sasha.say "Come on, [hero.name] - make with the cock already!"
        else:
            sasha.say "I'm ready as I'm ever gonna be, [hero.name]!"
        menu:
            "Spank her":
                mike.say "Oh, I will..."
                mike.say "But there's something else I want to do first."
                "I see the look of curiosity that spreads across Sasha's face as I say my piece."
                "And my guess is that she's about to ask me what the hell I mean by that."
                "Which, in turn, makes me all the more thrilled to do it before she can ask."
                "My hand is already sweeping backwards, and then I bring it back again."
                "The flat of the palm connecting with Sasha's buttocks, making a sharp crack."
                play sound spank
                with hpunch
                sasha.say "Argh!"
                sasha.say "What the..."
                "The second slap connects a few moments later, cutting off Sasha's protest."
                show sasha stand spank
                play sound spank
                with hpunch
                "And I can see from the look on her face that the initial surprise is wearing off."
                "But instead of the shock and outrage I was expecting, there's something else taking its place."
                "The fire in Sasha's eyes is fading a little, and they're almost half closed too."
                show sasha stand pleasure
                play sound spank
                with hpunch
                "By the time I slap her ass again, she's gone quiet and seems to be accepting it."
                "Her lips curling into a languid smile as I continue to spank her."
                play sound spank
                with hpunch
                "As her ass turns pink and then red from my efforts, Sasha continues to get more mellow."
                play sound spank
                with hpunch
                "And by the time I'm all done spanking her, I genuinely expect her to ask for more."
                "So what she actually says to me comes as a bit of a surprise."
                sasha.say "Mmm…"
                show sasha stand normal
                sasha.say "That felt SO good!"
                sasha.say "But don't forget to actually fuck me!"
            "Just fuck her":
                pass
        menu:
            "Fuck her pussy":
                "Like I really need to be reminded!"
                "All I can think about right now is getting my hands on Sasha."
                "And so I flex my fingers in anticipation, ready make a grab for her haunches."
                call check_condom_usage (sasha, 150) from _call_check_condom_usage_173
                if _return == False:
                    return "leave_without_gain"
                if CONDOM:
                    show sasha stand condom
                "Clapping my hands onto Sasha's waist, I smile as she yelps and flinches."
                sasha.say "Oooh!"
                sasha.say "Mmm…"
                sasha.say "More please!"
                "I don't hesitate to give her what she wants, thrusting myself forwards a moment later."
                "Sasha's bent over, thighs spread wide and her butt jutting out towards me right now."
                "Which means that my cock goes straight between her legs and rubs against her pussy."
                "And as soon as the tip so much as tickles the lips, she bears down on it."
                "I can't help gasping and tightening my grip on Sasha as she does so too."
                "Because now I'm beginning to feel just how hot and wet she is down there!"
                show sasha stand pleasure
                sasha.say "Ah..."
                sasha.say "Please, [hero.name]…"
                show sasha stand normal
                sasha.say "Give it to me?"
                "It's not like I need to be convinced, I want Sasha more than anything."
                "And I'm already angling myself so that I can press hard against her pussy."
                "My fingers making deep impressions in her haunches as I hold onto her."
                "There's a couple of moments where we're both grinding and thrusting."
                "Doing the best we can to make everything line up properly down there."
                show sasha stand wiggle
                "Sasha's wiggling her ass again, and the effort is making her breasts jiggle."
                if sasha.flags.boobjob:
                    "And I can't help getting distracted as I watch those massive pink orbs sway in the mirror."
                else:
                    "And I can't help getting distracted as I watch those little pink orbs sway in the mirror."
                "But it's while I'm kind of distracted by the bouncing boobies that it happens."
                "I move in one direction just as Sasha moves in another, and suddenly it all comes together."
                sasha.say "Oh fuck!"
                mike.say "Ugh...double fuck!"
                $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_low.ogg", loop=True)
                show sasha stand pleasure vaginal at stepback(speed=0.1, h=10, v=5)
                "Sasha moves backwards, I move forwards, and my cock slides all the way into her."
                "She squeezes her eyes closed as it happens, as if the sensation is overwhelming."
                "And I feel the exact same way, my cock being held firmly by the tight walls of her pussy."
                "Before we were talking to each other, exchanging suggestions and instructions."
                "But now that I'm inside of Sasha, there doesn't seem to be any need for that."
                show sasha stand normal
                "Now it's more like the physical connection between us makes everything instinctual."
                $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_medium.ogg", loop=True)
                show sasha stand at stepback(speed=0.1, h=10, v=5)
                "Which is a fancy way of saying that I start to bang Sasha like it's going out of fashion!"
                "Soon enough she's forced to brace her arms against the dresser as I thrust into her from behind."
                "Her normally pale cheeks quickly flushing pink as the waves of pleasure spread through her body."
                "Sasha's eyes are half closed by now, her mouth hanging open as she moans."
                show sasha stand pleasure speed at stepback(speed=0.1, h=10, v=5)
                pause 0.2
                show sasha stand at stepback(speed=0.1, h=10, v=5)
                "And downstairs I can even feel the slickness of her pussy against my balls."
                "The insides of her thighs are slippery too, making her skin slide upon mine."
                "But even as overwhelmed as she seems to be, I can still see Sasha nodding."
                "Her heavy-lidded eyes holding mine in the mirror's reflective surface."
                show sasha stand normal at stepback(speed=0.1, h=10, v=5)
                pause 0.2
                show sasha stand at stepback(speed=0.1, h=10, v=5)
                "As if she's urging me on to do more to her, to push her further still."
                menu:
                    "Use the gag ball":
                        "Suddenly my gaze falls upon a ball-gag that's just within reach."
                        "Don't ask me why it's there - this isn't the time or place for that."
                        "All that matters is the fact I can reach out and grab it,"
                        "Sasha seems to see me reaching for it, and she nods her head."
                        "Letting me know that she's into the idea of using it too."
                        "Once the thing is in my hands, I hastily strap it over Sasha's mouth."
                        stop sound
                        show sasha stand gag with fade
                        "She gasps and moans as it fills her mouth, and I can feel an instant change in her."
                        "The muscles around my cock tighten almost at the same time as the straps on the gag."
                        "And part of me wishes that it was a collar and leash instead."
                        "Because Sasha pretty much leaps backwards, starting to ride me harder than ever."
                        "So that it's all I can do to match her pace and keep up now!"
                        $ sasha_ballgag = True
                    "Just fuck her":










                        "I could take a risk and do something pretty crazy right now."
                        "But the truth is that I'm too worried about making the wrong choice."
                        "And the last thing that I want to do is blow it with Sasha."
                        "Especially after we've made it so far and had so much fun already."
                        "So instead I double down on what I'm doing to her right now."
                show sasha stand speed at stepback(speed=0.07, h=10, v=5)
                pause 0.15
                show sasha stand at stepback(speed=0.07, h=10, v=5)
                if not sasha_ballgag:
                    $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_high.ogg", loop=True)
                "Sasha lowers her head and lets out an almost animalistic moan as I start to pick up speed."
                "By now she's all but slumped over the dresser, using it to hold herself up while I fuck her."
                "And I honestly believe that, were I to let go of her, she'd collapse into heap on the ground."
                show sasha stand at stepback(speed=0.07, h=10, v=5)
                pause 0.15
                show sasha stand at stepback(speed=0.07, h=10, v=5)
                "But none of that make think of stopping, or even slowing down for an instant."
                "Because while Sasha's arms and legs are getting weaker, the opposite is true of her pussy."
                "I can feel the walls squeezing me more tightly than ever before."
                show sasha stand at stepback(speed=0.07, h=10, v=5)
                pause 0.15
                show sasha stand at stepback(speed=0.07, h=10, v=5)
                "The first sensations of them starting to spasm and quiver."
                show sasha stand pleasure
                if sasha_ballgag:
                    sasha.say "Mmmph…"
                    sasha.say "Mmmm...mmph!"
                elif sasha.sub >= 25:
                    if sasha.flags.mikeNickname:
                        sasha.say "[hero.name[0]]...[hero.name]..."
                    else:
                        sasha.say "M...Master..."
                    sasha.say "May I...may I...cum?"
                elif sasha.sub <= -25:
                    sasha.say "M...more...give me more..."
                    sasha.say "Make me...cum!"
                else:
                    sasha.say "I...I'm gonna...gonna cum!"
                "I can hear the effort that Sasha had to put into every word she just said."
                "The overwhelming power of her climax colouring each utterance from her mouth."
                "And combined with the way she's working my cock right now, she hardly needs to ask."
                show sasha stand at stepback(speed=0.07, h=10, v=5)
                pause 0.15
                show sasha stand at stepback(speed=0.07, h=10, v=5)
                "I push forwards with all of my strength, using my weight to add to the force."
                "And it seems to work, as Sasha is squashed up against the dresser, but instantly gasps."
                if not sasha_ballgag:
                    $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_orgasm.ogg", loop=True)
                show sasha stand ahegao
                "Then the full cascade of her orgasm hits, sweeping away everything in its path."
                show sasha stand at stepback(speed=0.07, h=10, v=5)
                pause 0.15
                show sasha stand at stepback(speed=0.07, h=10, v=5)
                "There's no way that I can keep from being caught up in it too."
                "Feeling myself beginning to lose it as I'm all the way inside of Sasha."
                call cum_reaction (sasha, 'vaginal', sexperience_min, 190, check_sub=True, sub_min=50) from _call_cum_reaction_313
                if _return == "vaginal_condom":
                    "I can hardly feel the condom that I'm wearing right now."
                    "But the knowledge that it's there means I can keep on going."
                    "Pushing as deep into Sasha as possible as I shoot my load."
                    with vpunch
                    "Making her moan and whimper as I explode inside of her pussy."
                elif _return == "vaginal_outside":
                    "It takes all of my concentration to hold on and pull backwards."
                    show sasha stand -vaginal
                    "Dragging myself all the way out of Sasha before the inevitable happens."
                    "And it feels crazy after pushing forwards with such intensity all this time."
                    "But the sensation is still crazily intense, making her whimper and moan."
                    if CONDOM:
                        "While I shoot my load."
                        with vpunch
                    else:
                        show sasha stand cumshot
                        "While I shoot my load over her slick buttocks."
                        with vpunch
                        show sasha stand cum onbody -cumshot
                elif _return == "vaginal_inside_pill":
                    if sasha_ballgag:
                        show sasha stand -gag
                        "Just in time, Sasha manages to spit out the gag."
                    sasha.say "Fill me up..."
                    sasha.say "It's okay...I'm on the pill!"
                    "I silently thank Sasha for the timely reminder."
                    "But there's no way that I can hold back now, not even if I wanted too."
                    "All I can do is keep on going, right until the very last moment."
                    show sasha stand creampie
                    "Pushing as deep into Sasha as possible as I shoot my load."
                    with vpunch
                    "Making her moan and whimper as I explode inside of her pussy."
                elif _return == "vaginal_inside_pregnant":
                    if sasha_ballgag:
                        show sasha stand -gag
                        "Just in time, Sasha manages to spit out the gag."
                    sasha.say "Fill me up..."
                    sasha.say "It's okay...I'm pregnant!"
                    "I'm not sure how I could have forgotten that particular fact."
                    "But there's no way that I can hold back now, not even if I wanted too."
                    "All I can do is keep on going, right until the very last moment."
                    show sasha stand creampie
                    "Pushing as deep into Sasha as possible as I shoot my load."
                    with vpunch
                    "Making her moan and whimper as I explode inside of her pussy."
                elif _return == "vaginal_inside_mad":
                    if sasha_ballgag:
                        show sasha stand -gag
                        "Just in time, Sasha manages to spit out the gag."
                    sasha.say "Pull out, [hero.name]…"
                    sasha.say "Quick, before it's too late!"
                    "There's no way that I can hold back now, not even if I wanted too."
                    "All I can do is keep on going, right until the very last moment."
                    "Pushing as deep into Sasha as possible as I shoot my load."
                    show sasha stand creampie
                    "Making her moan and whimper as I explode inside of her pussy."
                    with vpunch
                    $ sasha.impregnate()
                    "With her looking back over her shoulder at me in horror."
                else:
                    "It takes all of my concentration to hold on and pull backwards."
                    "Dragging myself all the way out of Sasha before the inevitable happens."
                    "Or at least that's what was supposed to happen, until Sasha foils my efforts."
                    mike.say "Sasha..."
                    mike.say "What are you doing?!?"
                    "But there's no way that I can hold back now, not even if I wanted too."
                    "All I can do is keep on going, right until the very last moment."
                    show sasha stand creampie
                    "Pushing as deep into Sasha as possible as I shoot my load."
                    with vpunch
                    $ sasha.impregnate()
                    "Making her moan and whimper as I explode inside of her pussy."
                    "But my head is filled with panic and amazement as I wonder why."
                    "Why would Sasha do something as crazy as that?"
            "Fuck her ass" if hero.sexperience >= (sexperience_min + 5) and sasha.flags.anal:
                "Like I really need to be reminded!"
                "All I can think about right now is getting my hands on Sasha."
                "And so I flex my fingers in anticipation, ready make a grab for her haunches."
                "Clapping my hands onto Sasha's waist, I smile as she yelps and flinches."
                sasha.say "Oooh!"
                sasha.say "Mmm…"
                sasha.say "More please!"
                "I don't hesitate to give her what she wants, thrusting myself forwards a moment later."
                "Sasha's bent over, thighs spread wide and her butt jutting out towards me right now."
                "Which means that my cock goes straight between her buttocks and rubs against her hole."
                "And as soon as the tip so much as tickles the edge, she bears down on it."
                "I can't help gasping and tightening my grip on Sasha as she does so too."
                "Because now I'm beginning to feel just how hot and supple she is down there!"
                show sasha stand pleasure
                sasha.say "Ah..."
                sasha.say "Please, [hero.name]…"
                show sasha stand normal
                "It's not like I need to be convinced, I want Sasha more than anything."
                "And I'm already angling myself so that I can press hard against her hole."
                "My fingers making deep impressions in her haunches as I hold onto her."
                "There's a couple of moments where we're both grinding and thrusting."
                "Doing the best we can to make everything line up properly down there."
                show sasha stand wiggle
                "Sasha's wiggling her ass again, and the effort is making her breasts jiggle."
                if sasha.flags.boobjob:
                    "And I can't help getting distracted as I watch those massive pink orbs sway in the mirror."
                else:
                    "And I can't help getting distracted as I watch those little pink orbs sway in the mirror."
                "But it's while I'm kind of distracted by the bouncing boobies that it happens."
                "I move in one direction just as Sasha moves in another, and suddenly it all comes together."
                sasha.say "Oh fuck!"
                mike.say "Ugh...double fuck!"
                $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_low.ogg", loop=True)
                show sasha stand pleasure anal at stepback(speed=0.1, h=10, v=5)
                "Sasha moves backwards, I move forwards, and my cock slides all the way into her."
                "She squeezes her eyes closed as it happens, as if the sensation is overwhelming."
                "And I feel the exact same way, my cock being held firmly by the tight muscles of her ass"
                "Before we were talking to each other, exchanging suggestions and instructions."
                "But now that I'm inside of Sasha, there doesn't seem to be any need for that."
                show sasha stand normal
                "Now it's more like the physical connection between us makes everything instinctual."
                $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_medium.ogg", loop=True)
                show sasha stand at stepback(speed=0.1, h=10, v=5)
                "Which is a fancy way of saying that I start to bang Sasha like it's going out of fashion!"
                "Soon enough she's forced to brace her arms against the dresser as I thrust into her from behind."
                "Her normally pale cheeks quickly flushing pink as the waves of pleasure spread through her body."
                "Sasha's eyes are half closed by now, her mouth hanging open as she moans."
                show sasha stand pleasure speed at stepback(speed=0.1, h=10, v=5)
                pause 0.2
                show sasha stand at stepback(speed=0.1, h=10, v=5)
                "And downstairs I can even feel the slickness of her butt-cheeks against my balls."
                "The insides of her thighs are slippery too, making her skin slide upon mine."
                "But even as overwhelmed as she seems to be, I can still see Sasha nodding."
                "Her heavy-lidded eyes holding mine in the mirror's reflective surface."
                show sasha stand normal at stepback(speed=0.1, h=10, v=5)
                pause 0.2
                show sasha stand at stepback(speed=0.1, h=10, v=5)
                "As if she's urging me on to do more to her, to push her further still."
                menu:
                    "Use the gag ball":
                        "Suddenly my gaze falls upon a ball-gag that's just within reach."
                        "Don't ask me why it's there - this isn't the time or place for that."
                        "All that matters is the fact I can reach out and grab it,"
                        "Sasha seems to see me reaching for it, and she nods her head."
                        "Letting me know that she's into the idea of using it too."
                        "Once the thing is in my hands, I hastily strap it over Sasha's mouth."
                        stop sound
                        show sasha stand gag with fade
                        "She gasps and moans as it fills her mouth, and I can feel an instant change in her."
                        "The muscles around my cock tighten almost at the same time as the straps on the gag."
                        "And part of me wishes that it was a collar and leash instead."
                        "Because Sasha pretty much leaps backwards, starting to ride me harder than ever."
                        "So that it's all I can do to match her pace and keep up now!"
                        $ sasha_ballgag = True
                    "Just fuck her":










                        "I could take a risk and do something pretty crazy right now."
                        "But the truth is that I'm too worried about making the wrong choice."
                        "And the last thing that I want to do is blow it with Sasha."
                        "Especially after we've made it so far and had so much fun already."
                        "So instead I double down on what I'm doing to her right now."
                show sasha stand speed at stepback(speed=0.07, h=10, v=5)
                pause 0.15
                show sasha stand at stepback(speed=0.07, h=10, v=5)
                if not sasha_ballgag:
                    $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_high.ogg", loop=True)
                "Sasha lowers her head and lets out an almost animalistic moan as I start to pick up speed."
                "By now she's all but slumped over the dresser, using it to hold herself up while I fuck her."
                "And I honestly believe that, were I to let go of her, she'd collapse into heap on the ground."
                show sasha stand at stepback(speed=0.07, h=10, v=5)
                pause 0.15
                show sasha stand at stepback(speed=0.07, h=10, v=5)
                "But none of that make think of stopping, or even slowing down for an instant."
                "Because while Sasha's arms and legs are getting weaker, the opposite is true of her ass."
                "I can feel the muscles squeezing me more tightly than ever before."
                show sasha stand at stepback(speed=0.07, h=10, v=5)
                pause 0.15
                show sasha stand at stepback(speed=0.07, h=10, v=5)
                "The first sensations of them starting to spasm and quiver."
                show sasha stand pleasure
                if sasha_ballgag:
                    sasha.say "Mmmph…"
                    sasha.say "Mmmm...mmph!"
                elif sasha.sub >= 25:
                    if sasha.flags.mikeNickname:
                        sasha.say "[hero.name[0]]...[hero.name]..."
                    else:
                        sasha.say "M...master..."
                    sasha.say "May I...may I...cum?"
                elif sasha.sub <= -25:
                    sasha.say "M...more...give me more..."
                    sasha.say "Make me...cum!"
                else:
                    sasha.say "I...I'm gonna...gonna cum!"
                "I can hear the effort that Sasha had to put into every word she just said."
                "The overwhelming power of her climax colouring each utterance from her mouth."
                "And combined with the way she's working my cock right now, she hardly needs to ask."
                show sasha stand at stepback(speed=0.07, h=10, v=5)
                pause 0.15
                show sasha stand at stepback(speed=0.07, h=10, v=5)
                "I push forwards with all of my strength, using my weight to add to the force."
                "And it seems to work, as Sasha is squashed up against the dresser, but instantly gasps."
                if not sasha_ballgag:
                    $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_orgasm.ogg", loop=True)
                show sasha stand ahegao
                "Then the full cascade of her orgasm hits, sweeping away everything in its path."
                show sasha stand at stepback(speed=0.07, h=10, v=5)
                pause 0.15
                show sasha stand at stepback(speed=0.07, h=10, v=5)
                "There's no way that I can keep from being caught up in it too."
                "Feeling myself beginning to lose it as I'm all the way inside of Sasha."
                call cum_reaction (sasha, 'anal', sexperience_min) from _call_cum_reaction_314
                if _return == "anal_inside":
                    "There's no way that I can hold back now, not even if I wanted too."
                    "All I can do is keep on going, right until the very last moment."
                    show sasha stand creampie
                    "Pushing as deep into Sasha as possible as I shoot my load."
                    with vpunch
                    "Making her moan and whimper as I explode inside of her ass."
                elif _return == "anal_outside":
                    $ sasha.sub += 1
                    "It takes all of my concentration to hold on and pull backwards."
                    show sasha stand -anal
                    "Dragging myself all the way out of Sasha's ass before the inevitable happens."
                    "And it feels crazy after pushing forwards with such intensity all this time."
                    "But the sensation is still crazily intense, making her whimper and moan."
                    show sasha stand cumshot
                    "While I shoot my load over her slick buttocks."
                    with vpunch
                    show sasha stand cum onbody -cumshot
                $ sasha.flags.anal += 1
        play sound "sd/moans/sasha/sasha_panting.ogg" loop
        "Once it's over, I feel like I've been drained of all my energy."
        "And it's the most I can do to stagger over to the bed."
        "When I get there I collapse onto the mattress, gasping for breath."
        "Sasha joins me a moment later, almost falling on top of me."
        "One arm slung over my chest, she curls up at my side."
        "Pressing herself against me as the aftershocks of her orgasm make her body quiver."
    call stop_all_sfx from _call_stop_all_sfx_39
    return

label sasha_fuck_date_doggy(sexperience_min):
    if sasha_beads:
        mike.say "I'm not done with you yet."
        mike.say "Turn around."
        $ sasha.sub += 2
        scene bg black
        show sasha doggy beads2 -cumafter -cum -mike with fade
        "She does as she's told, clearly hoping to be on the receiving end of pleasure now, since she's taken the beads and the blowjob so well."
        "But I'm not sure what I want."
        "First there's that pretty pussy, hairless and glistening with arousal."
        "But there's also that perky ass stuffed with beads, that could easily be stuffed with cock instead."
        "It's a difficult choice."
        menu:
            "Fuck her ass" if sasha.flags.anal and hero.sexperience >= (sexperience_min + 5):
                "She may be eager for pleasure, but I think I want to leave her squirming for the night, her tight pussy unfucked."
                show sasha doggy beads3 entered
                "I give her ass a slap, then grasp the protruding bead and slowly start to pull the toy out of that little hole, watching as her asshole expanded and contracted to allow the beads to be removed."
                show sasha doggy beads5 scream
                "It's a pretty arousing sight, but I certainly didn't need the extra arousal. Even after that heavenly blowjob, I want more."
                show sasha doggy waiting anusopen -mike
                "I consider just tossing the beads aside, but then I get a better idea."
                show sasha doggy mouthbeads nobeads waiting anusopen
                "I lean forward over her form and stuff the bottom two beads into her surprised mouth, making her give a muffled sound of protest."
                mike.say "You keep those right there until I'm done fucking you."
                mike.say "You'll need something to bite down on."
                "It's likely those words that bring realization to her eyes, realization that she's not going to get her pussy pounded like she wants."
                show sasha doggy mouthbeads waiting mike anal
                $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_low.ogg", loop=True)
                "Before realization can turn to resentment, I lean back and grind my hips to hers, caressing her nicely-rounded butt just before I guide my dick to her hole and start pushing in."
                "It's easier like this, after she had her ass stuffed with a toy."
                "Instead of a mild ache at the tightness, I get a flush of pleasure and room enough to start fucking her hard."
                "That's exactly what I start doing."
                $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_medium.ogg", loop=True)
                "Gripping her hips, I begin thrusting quick and hard, making Sasha give a muffled scream of surprise around the beads that stuff her mouth."
                "It feels incredible, and looking down at Sasha's wincing, cum-stained face makes it even hotter for me."
                "I love the way she quivers, the way she blushes, and especially the way she starts to grind back against me."
                "After such a fantastic blowjob, it's not going to take long to get off again, and I want that burst of bliss."
                $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_high.ogg", loop=True)
                "Panting, I tighten my grip on her hips and start pounding her tight little ass faster, driving myself as deep as I can into that greedily clutching hole."
                "Finally, that squeeze of her asshole around my thick rod is enough to push me over the edge."
                call cum_reaction (sasha, 'anal', sexperience_min) from _call_cum_reaction_162
                if _return == "anal_inside":
                    $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_orgasm.ogg", loop=True)
                    show sasha doggy mouthbeads waiting mike anal cum with hpunch
                    "I slam my hips forward, making Sasha cry out again, and hold her body still with my grip on her hips."
                    with hpunch
                    "My body jerks as muscles twitch from the exciting pleasure of climax, my hot and sticky cum filling up her snug tunnel."
                    with hpunch
                    "It's longer than with the blowjob; with this load I probably could have covered her whole face."
                    show sasha doggy mouthbeads entered mike anal anusopen cumafter
                    "When the shuddering bliss subsides, I slowly pull out and watch as my cum drools from her stretched asshole."
                elif _return == "anal_outside":
                    show sasha doggy mouthbeads waiting mike -anal cum with hpunch
                    $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_orgasm.ogg", loop=True)
                    "I take my cock out of her tight asshole, pointing it toward her lovely back."
                    with hpunch
                    "My body jerks as muscles twitch from the exciting pleasure of climax, my hot and sticky cum splattering on her skin."
                    with hpunch
                    "It's longer than with the blowjob; with this load I probably could have covered her whole face, and I cover a lot of her back."
                    show sasha doggy mouthbeads waiting cumafter
                    "When the shuddering bliss subsides, I take a step back and watch the lovely mess I made of her."
                $ renpy.sound.play("sd/moans/sasha/sasha_panting.ogg", loop=True)
                "Sasha's breathing hard too, cheeks still red, beads still held in her mouth."
                "I lean forward and gently pull them out, tossing the anal beads aside, then pull back a little to pat her on the ass."
                mike.say "That was fantastic."
                "Sasha gives me a sullen look that makes me chuckle."
                mike.say "Oh, don't pout at me, Sasha. You'll get yours in the morning. I'm sure you'll still be horny."
                stop sound
                "That makes her blush even deeper and I back away from the bed to tug my pants on."
                "I take her into my arms, getting ready to sleep."
                $ sasha.sub += 2
                $ sasha.flags.anal += 1
            "Fuck her pussy":
                call check_condom_usage (sasha, 160) from _call_check_condom_usage_104
                if _return == False:
                    return "leave_without_gain"
                "My cock is still a little slippery with cum, but it doesn't look like she'll need the extra lube."
                show sasha doggy beads2 entered mike vaginal
                if CONDOM:
                    show sasha doggy beads2 entered mike vaginal condom
                "I press the broad head to her little hole and push forward, groaning as her pussy clings so tight to my still-sensitive dick."
                "It makes my muscles quiver even more; I know it won't take too long to cum."
                "Looking down at her, seeing her jizz-splashed face, arouses me further."
                "I give her ass a slap, then grab her hips with a tight grip that makes her whimper with anticipation."
                "I don't leave her anticipating long."
                "Almost immediately, I push her hips forward, then pull them back forcefully, using her body like a sex toy for a moment."
                "I stand still, pushing and pulling at her hips, making her ride my cock."
                "The blush on her face beneath the white lines of cum makes the experience so much hotter; I'll have to do that to her more often."
                "The slap of our bodies meeting gets louder as I begin to thrust my hips forward when pulling her back toward me."
                "Her moans get louder and shudders ripple down her spine; she might be close too."
                "Much as I don't want to, I hold back, intending to let her climax first."
                "She deserves it; she did such a good job sucking me off."
                "She tosses her head back and cries out when orgasm hits, her body trembling, her hips bucking back against mine as she grinds hard, trying to get my cock as deep as she can."
                "As she climaxes, I grab the bead that juts out of her ass and start pulling, dragging the beads out slowly through her orgasm."
                show sasha doggy beads2 ahegao mike vaginal
                "It makes her cry out more, feeling such intense sensation in both holes."
                "Now it's more than I can take."
                if sasha.sub >= 25 and hero.sexperience >= 25:
                    menu:
                        "Make her suck you off":
                            stop sound
                            call sasha_fuck_date_bj from _call_sasha_fuck_date_bj_4
                            return
                        "Just go on":
                            pass
                call cum_reaction (sasha, 'vaginal', sexperience_min) from _call_cum_reaction_163
                if _return == "vaginal_condom":
                    "I thrust forward, holding her hard against me as my cock twitches deep inside her."
                    $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_orgasm.ogg", loop=True)
                    show sasha doggy mike vaginal scream with hpunch
                    pause 0.25
                    with hpunch
                    pause 0.25
                    with hpunch
                    "I groan loudly and fill the condom with spurt after spurt of hot sticky cum. I stand there, panting and squeezing cum out of my cock until my climax finally ends."
                    show sasha doggy mike -vaginal cum entered
                    "When I pull out, I can see just how much of the condom I have filled."
                elif _return == "vaginal_outside":
                    "At the very last minute, I pull my dick out."
                    $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_orgasm.ogg", loop=True)
                    show sasha doggy mike cumshot -vaginal with hpunch
                    pause 0.25
                    with hpunch
                    pause 0.25
                    with hpunch
                    "I groan again as the cum explodes from my cock, letting Sasha know how thoroughly I enjoyed her beautiful pussy."
                    if CONDOM:
                        "The condom is almost a disappointment, catching all of the cum, but it doesn't matter. The orgasm itself, not my first of the night, is absolutely incredible."
                    else:
                        show sasha doggy mike cumafter waiting
                        "My load explodes out of my cock, covering her back and ass with globs of the sticky liquid."
                    "I just stand there for a moment, admiring my handiwork."
                else:
                    "I thrust forward, holding her hard against me as my cock twitches deep inside her."
                    $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_orgasm.ogg", loop=True)
                    show sasha doggy mike vaginal cum scream with hpunch
                    if _return not in ["vaginal_inside_pill", "vaginal_inside_pregnant"]:
                        $ sasha.impregnate()
                    pause 0.25
                    with hpunch
                    pause 0.25
                    with hpunch
                    "I groan loudly with every spurt of hot sticky cum that I fill her pussy with, panting, until my climax finally ends."
                    show sasha doggy mike -vaginal waiting
                    "I pull out, looking down to see some of my cum dribble out of her pussy and down the inside of one thigh."
                $ renpy.sound.play("sd/moans/sasha/sasha_panting.ogg", loop=True)
                "Arousal slowly fading, I pull her down on the bed with me to spoon together, trying to catch my breath."
                hide sasha
                show sasha naked blush
                with fade
                stop sound
                sasha.say "Wow..."
                mike.say "Glad you liked it."
                "I toss the beads aside and cuddle close, deciding we'll sleep together tonight."
                $ sasha.love += 2
                $ sasha.sub += 1
    else:
        call check_condom_usage (sasha, 150) from _call_check_condom_usage_105
        if _return == False:
            return "leave_without_gain"
        "Much as I might enjoy drawing it out longer, at this moment there's nothing I want more than to pound her little pussy until she screams."
        "So I give her a shove between the shoulder-blades, sending her to her hands and knees."
        scene bg black
        show sasha doggy waiting -mike
        if CONDOM:
            show sasha doggy waiting condom -mike
        "I kneel upright, smack her ass with both hands, then grab her hips."
        "She yelps, the sound turning to a low moan, and she grinds back against me, getting my pubic hair moist with her arousal."
        "After all this anticipation, it feels beyond amazing to slowly sink my dick into her clingy cunt."
        show sasha doggy mike vaginal entered
        $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_medium.ogg", loop=True)
        "Feeling her walls close tight around the shaft draws a groan from me and I push until I'm buried completely inside my new pet."
        if sasha.is_sex_slave:
            mike.say "Mm... Such a tight little slave."
        else:
            mike.say "Mm... my good girl is so tight."
        "Her striped ass jiggles with each impact as I shove in as deep as I can, the impact of flesh on flesh making a slapping sound in the small room."
        "She's my pet now."
        "I can do what I want with her, and by the way she's crying out, it won't be long before she cums."
        menu:
            "Fuck her ass instead" if sasha.flags.anal and hero.sexperience >= (sexperience_min + 5) and not CONDOM:
                "Shuddering, I pull out of her abruptly enough to make her whine in protest, but I'm ready to push back in."
                "Just not into her pussy."
                "I lift up a little, letting the soaked and slippery head of my cock glide up until it's pressed against the tight ring of her asshole."
                show sasha doggy anal hurt
                "Without giving her time to prepare, I start pushing in."
                "It's so tight it begins to ache, the way that tunnel grips my cock."
                "She cries out in pain but apparently she likes it despite her sounds, for she pushes back against me cautiously, taking my thick rod deeper into her ass."
                "When my cock is as deep in as it can go, I hold still for several moments, letting my little fuck-doll adjust."
                "She's panting for breath, each exhale a whimper, shivers dancing down her spine."
                "She's been so good, I know I should make her cum too, considering how close to the edge I am."
                "I slide one hand around between her thighs, pinching her throbbing clit between two fingers and wiggling those digits from side to side."
                show sasha doggy entered
                $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_high.ogg", loop=True)
                "It's apparently a way she really loves to be touched, for Sasha cries out and grinds down hard against me before doing as ordered."
                "I keep rubbing her clit to make her cum for a moment, then slide my hand further between her thighs and start fingering that slippery little cunt."
                "She shudders hard and I cup one bouncing tit with my other hand, giving the nipple a cruel pinch."
                mike.say "I know you're close, pet."
                mike.say "Cum for me."
                mike.say "Soak my hand, show me how much you love it."
                show sasha doggy scream
                $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_orgasm.ogg", loop=True)
                "Sasha probably didn't really need the encouragement; it's only a few more bounces before she throws her head back and lets out a yell of bliss."
                "As ordered, she really does soak my hand, hot nectar squirting against my palm."
                "I had no idea she could cum so hard and it almost sends me over the edge."
                "Quickly, I pull my hands back from her body and my dick out of her ass, groaning."
                show sasha doggy vaginal entered
                "I don't even give her the time to catch her breath before plunging back into her pussy."
                $ sasha.flags.anal += 1
        "I can't hold back any longer anyway; it feels too good."
        "I start rocking my hips at a quick pace, keeping the angle of her lower body tilted so that each thrust teases over her G-spot."
        show sasha doggy scream
        $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_medium.ogg", loop=True)
        "With that kind of attention, she's gasping for breath and squirming soon, her lips parted and a flush across her cheeks."
        "I love the lusty look in her eyes."
        "I don't bother to vary my pace or position."
        "It's clear by her whimpers and gasps that I'm doing just what she wants, and it feels wonderful to me too."
        "Her cunt is so tight and I can feel it getting more and more slippery the longer I fuck her."
        "The smell of sex rises in the air, arousing both of us even further."
        "I can tell by the way she trembles and how tight she holds onto my wrists that she's close."
        $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_high.ogg", loop=True)
        "Groaning, right on the edge myself, I shorten my thrusts and fuck her harder, entranced by the way her small breasts jiggle and bounce with each impact."
        "Finally, I can't hold it off any more."
        "Just as I shove deep, my cock starting to throb, she cries out and arches to grind against me."
        if sasha.sub >= 25 and hero.sexperience >= 25:
            menu:
                "Make her suck you off":
                    stop sound
                    call sasha_fuck_date_bj from _call_sasha_fuck_date_bj_5
                    return
                "Just go on":
                    pass
        call cum_reaction (sasha, 'vaginal', sexperience_min) from _call_cum_reaction_164
        if _return == "vaginal_condom":
            "I thrust forward, holding her hard against me as my cock twitches deep inside her."
            $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_orgasm.ogg", loop=True)
            show sasha doggy mike vaginal scream with hpunch
            pause 0.25
            with hpunch
            pause 0.25
            with hpunch
            "I groan loudly and fill the condom with spurt after spurt of hot sticky cum. I stand there, panting and squeezing cum out of my cock until my climax finally ends."
            show sasha doggy mike -vaginal cum entered
            "When I pull out, I can see just how much of the condom I have filled."
        elif _return == "vaginal_outside":
            "At the very last minute, I pull my dick out."
            $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_orgasm.ogg", loop=True)
            show sasha doggy mike cumshot -vaginal with hpunch
            pause 0.25
            with hpunch
            pause 0.25
            with hpunch
            "I groan again as the cum explodes from my cock, letting Sasha know how thoroughly I enjoyed her beautiful pussy."
            if CONDOM:
                "The condom is almost a disappointment, catching all of the cum, but it doesn't matter. The orgasm itself, not my first of the night, is absolutely incredible."
            else:
                show sasha doggy mike cumafter dickout waiting -cumshot
                "My load explodes out of my cock, covering her back and ass with globs of the sticky liquid."
            "I just stand there for a moment, admiring my handiwork."
        else:
            "I thrust forward, holding her hard against me as my cock twitches deep inside her."
            $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_orgasm.ogg", loop=True)
            show sasha doggy mike vaginal cum scream with hpunch
            if _return not in ["vaginal_inside_pill", "vaginal_inside_pregnant"]:
                $ sasha.impregnate()
            pause 0.25
            with hpunch
            pause 0.25
            with hpunch
            "I groan loudly with every spurt of hot sticky cum that I fill her pussy with, panting, until my climax finally ends."
            show sasha doggy mike -vaginal waiting
            "I pull out, looking down to see some of my cum dribble out of her pussy and down the inside of one thigh."
        $ renpy.sound.play("sd/moans/sasha/sasha_panting.ogg", loop=True)
        "As my climax ends and hers dies down to shudders, we both fall on the bed."
        "Several moments of silence stretch as we both struggle to catch our breath."
        $ sasha.love += 2
    stop sound
    return

label sasha_bondage_sex:
    scene bg bedroom1






    show sasha foreplay rope
    with fade
    "I tie Sasha up, using a length of rope to create a series of intricate knots across her body."
    "It snakes around her neck, chest and hips, encircling her breasts and even the space between her legs."
    "We're both already naked at this point, with her standing in front of a full-length mirror."
    sasha.say "That's it, pull it up and then tie it off, right...there!"
    "She's supposedly using the mirror to guide my efforts, but it's obvious that she's getting off on the sight of herself being trussed up."
    "I can feel the heat emanating from her body and see the way her cheeks are flushing a deep red."
    "It seems oddly contradictory to see such an outwardly strong and feisty woman being turned on by being in a compromising, even belittling situation."
    "But I can't say that it's not working for me as well, and Sasha's eyes keep stealing towards my dick as it responds in kind."
    "Sasha clambers onto the bed, looking at me the whole time with wide, expectant eyes."
    "She kneels down facing me, then moves onto all fours."
    "Sasha's eyes are huge and her expression seems to be urging me to make a move."
    "For a moment I'm lost, used to being wowed by her looks and astonishing body."
    "But then I remember, this is about something else entirely, and I swallow hard before jumping into, what I hope she's expecting."
    mike.say "What are you waiting for, instructions with a slideshow?!?"
    "Sasha's eyes widen at the brusqueness of my tone, but she eagerly shuffles forwards on her hands and knees."
    mike.say "Lips and tongue!"
    show sasha bj rope mike dickout with fade
    "I feel bad for speaking to Sasha like this, but I try to tell myself that the rules are different here."
    "Not needing to be told twice, she begins to kiss and lick eagerly at the tip of my dick."
    $ renpy.sound.play("sd/moans/sasha/sasha_blowjob_medium.ogg", loop=True)
    show sasha bj rope mike dickin
    "Soon she's swallowing the shaft as much as she's able to manage, the indignity of her situation making her work all the harder."
    mike.say "Keep it up, that's right...this'll teach you what your mouth's really good for."
    "I worry about going too far, but every word seems to make Sasha even more dogged in her attentions."
    "Soon I can feel myself starting to lose control, beginning to cum."
    menu:
        "Cum in her mouth":
            $ sasha.sub += 1
            "The feeling of her tongue around my dick and her bound breasts against my thighs is just too much."
            show sasha bj rope mike dickin cum with hpunch
            pause 0.25
            with hpunch
            "Without a single thought for the consequences, I let myself go inside of Sasha's mouth."
            $ renpy.sound.play("sd/moans/sasha/sasha_blowjob_swallow.ogg", loop=True)
            with hpunch
            "She coughs and begins to gag, but I take hold of her head, figuring this is all part of the bondage experience."
            hide sasha
            show sasha rope
            if hero.sexperience < 3:
                $ sasha.sub -= 3
                stop sound
                sasha.say "I think that's enough for one night, [hero.name]!"
                "I look disappointed at that, but Sasha shakes her head and smiles."
                sasha.say "Don't look so downhearted, man - it was your first time, you're allowed to be a bit overwhelmed!"
                return "leave_with_gain"
            else:
                mike.say "Don't just lie there panting like a bitch in heat!"
                mike.say "We're not done until I tell you we're done!"
                "Sasha keeps on playing the part of the submissive, but I can see the spark in her eye at the thought of there being more ahead."
        "Cum on her face":
            $ sasha.sub += 2
            show sasha bj rope mike dickout
            stop sound
            "Not wanting to cum in her mouth, I pull my dick hastily out from between Sasha's lips."
            "Surprised by the move, she nips at the tip with her teeth."
            show sasha bj rope mike dickout cum with vpunch
            pause 0.25
            with vpunch
            pause 0.25
            with vpunch
            "The unexpected gesture is all that's needed to tip me over the edge, and I loose myself instantly over her shocked face."
            $ renpy.sound.play("sd/moans/sasha/sasha_panting.ogg", loop=True)
            show sasha bj rope mike dickout cumafter
            "Both of us are panting now, red-faced and overcome by the excitement of what we've just done."
            hide sasha
            show sasha rope
            if hero.sexperience < 3:
                $ sasha.sub -= 3
                sasha.say "I think that's enough for one night, [hero.name]!"
                "I look disappointed at that, but Sasha shakes her head and smiles."
                sasha.say "Don't look so downhearted, man - it was your first time, you're allowed to be a bit overwhelmed!"
                return "leave_with_gain"
            else:
                mike.say "Don't just lie there panting like a bitch in heat!"
                mike.say "We're not done until I tell you we're done!"
                "Sasha keeps on playing the part of the submissive, but I can see the spark in her eye at the thought of there being more ahead."
        "Don't cum" if hero.sexperience >= 5:
            "I could easily give in and lose it here and now."
            "But the thought of just how aroused and biddable Sasha seems to be keeps me from letting go."
            hide sasha
            show sasha rope
            "With a massive dose of willpower, I manage to hold on and pull my dick out from between Sasha's eager lips."
    stop sound
    return

label sasha_bondage_sex_second_round:
    "Both of us are panting now, red-faced and overcome by the excitement of what we've just done."
    "As Sasha waits obediently on the bed before me, I take a moment to plan my next move."
    call check_condom_usage (sasha, 150) from _call_check_condom_usage_106
    if _return == False:
        return "leave_without_gain"
    "I motion for Sasha to come closer as I decide what's in store for her."
    "She crawls towards the edge of the bed, clearly eager to see what fate awaits her."
    menu:
        "Missionary":
            scene sasha missionary
            show sasha missionary rope nomc
            if CONDOM:
                show sasha missionary rope condom
            if "anal_beads" in hero.inventory and not sasha_beads:
                "With one hand I push Sasha down onto the bed and snatch up the anal beads I hid on the bedside table."
                show sasha missionary -nomc
                "Sasha's face registers surprise as I lean over her with them in my hand, using my weight to pin her beneath me."
                show sasha missionary vaginal
                "As the head of my dick pushes into her lips, I reach under her and use a finger to also insert the first of the beads in her ass."
                "I time my short thrusts forwards to the insertion of each subsequent bead, not pushing all the way into her until the entire string is inside."
                show sasha missionary sashacum
                "Only then do I start to move more rapidly inside of Sasha, enjoying the still startled look on her face."
                "It feels empowering to have shocked her at her own game, and I feel the pleasure of her body all the more because of it."
                $ sasha_beads = True
            else:
                "I push Sasha roughly backwards without a moment's hesitation, sending tumbling onto the bed."
                show sasha missionary -nomc
                "Following a step behind, I pin her shoulders with my hands even as I use my legs to part her thighs."
                show sasha missionary vaginal
                "I see no sense in waiting for a moment, so I simply steer myself between Sasha's legs and into her waiting lips."
                "She gives a slight whimper of arousal as I push as far as I am able into her, and then I pause perhaps an inch from her."
                show sasha missionary sashacum
                "I can feel the rope rubbing against the sides of my dick as I start to move, adding to the feel of her contrastingly soft folds."
                "All the while Sasha simply lays back and takes whatever I have to give her, clearly enjoying the submissive role into which she has been forced."
            "I have no idea if it's the thrill I'm getting from the bondage or from seeing Sasha react to it, but I can't keep this up much longer."
            $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_orgasm.ogg", loop=True)
            call cum_reaction (sasha, 'vaginal', 0) from _call_cum_reaction_165
            if _return == "vaginal_condom":
                if sasha_beads:
                    $ sasha.sub += 2
                    "While I keep my dick firmly inside of Sasha as I cum, I also yank the beads out of her ass without hesitation."
                    "Pulled one way by my orgasm and another by the sensation of the beads, Sasha writhes delightfully beneath me."
                else:
                    $ sasha.sub += 1
                    "Holding her down more forcefully than ever, I make her ride out every second of my orgasm, revelling in her twitches and cries as I do so."
            elif _return == "vaginal_outside":
                if sasha_beads:
                    $ sasha.sub += 1
                    show sasha missionary -vaginal cum with hpunch
                    pause 0.25
                    with hpunch
                    pause 0.25
                    with hpunch
                    "I hear Sasha almost moan in disappointment as I pull out of her before I cum."
                    "But then I take hold of the beads and virtually rip them out of her ass, making her breathless at the sensation."
                else:
                    show sasha missionary -vaginal cum with hpunch
                    pause 0.25
                    with hpunch
                    pause 0.25
                    with hpunch
                    "At the very last moment I manage to somehow drag my dick out of Sasha, sparing her from taking me as I cum."
                    "As she moans from the sensation of the sudden withdrawal, I just pant from sheer exhaustion."
            else:
                if sasha_beads:
                    $ sasha.sub += 3
                    show sasha missionary creampie
                    "While I keep my dick firmly inside of Sasha as I cum, I also yank the beads out of her ass without hesitation."
                    "Pulled one way by my orgasm and another by the sensation of the beads, Sasha writhes delightfully beneath me."
                else:
                    $ sasha.sub += 2
                    "I might have normally pulled out at that moment, but something about the bondage aspect makes me want to dominate Sasha still further."
                    show sasha missionary creampie
                    "Holding her down more forcefully than ever, I make her ride out every second of my orgasm, revelling in her twitches and cries as I do so."
                if _return not in ["vaginal_inside_pill", "vaginal_inside_pregnant"]:
                    $ sasha.impregnate()
        "Standing" if hero.sexperience >= 15:
            scene sasha stand
            show sasha stand rope
            if CONDOM:
                show sasha stand condom
            if "anal_beads" in hero.inventory and not sasha_beads:
                "I lead Sasha off the bed and walk her the short distance to the full-length mirror."
                "On the way I palm the anal beads that I had bought for just this occasion."
                show sasha stand vaginal
                "Once Sasha is standing before the mirror, I bend her over and tease her lower lips with the head of my dick."
                "At the same time I proffer the beads, making sure she sees them in the glass."
                show sasha stand beads beads4
                "As I begin to slowly ease my way inside of her, I push the first of the beads into her unprepared ass."
                show sasha stand beads2
                "With one hand grasping her wrists and the other pushing the beads further inside her, I begin to thrust ever harder."
                $ sasha_beads = True
            else:
                if sasha_beads:
                    show sasha stand beads beads2
                "Remembering the way Sasha looked at herself in the full-length mirror, I pull her off of the bed and onto her feet."
                "She offers no resistance as I take hold of her arms behind her back and bend her over until her face is almost touching the glass."
                show sasha stand vaginal
                "Sasha moans deeply as I position myself just right and then pull her bodily backwards."
                "Impaled on my awaiting dick, she stares at her own reflection as I sink into her."
                "I thrust forwards almost with a rowing motion, before loosening my grip and allowing her to sag forwards."
                "Sasha is almost screaming now, each one coming in time with my own movements."
            "I have no idea if it's the thrill I'm getting from the bondage or from seeing Sasha react to it, but I can't keep this up much longer."
            $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_orgasm.ogg", loop=True)
            call cum_reaction (sasha, 'vaginal', 15) from _call_cum_reaction_166
            if _return == "vaginal_condom":
                if sasha_beads:
                    $ sasha.sub += 2
                    "While I keep my dick firmly inside of Sasha as I cum, I also yank the beads out of her ass without hesitation."
                    "Pulled one way by my orgasm and another by the sensation of the beads, Sasha writhes delightfully beneath me."
                else:
                    $ sasha.sub += 1
                    "Holding her down more forcefully than ever, I make her ride out every second of my orgasm, revelling in her twitches and cries as I do so."
            elif _return == "vaginal_outside":
                if sasha_beads:
                    $ sasha.sub += 1
                    show sasha stand -vaginal -anal cumshot with hpunch
                    pause 0.25
                    with hpunch
                    pause 0.25
                    with hpunch
                    "I hear Sasha almost moan in disappointment as I pull out of her before I cum."
                    "But then I take hold of the beads and virtually rip them out of her ass, making her breathless at the sensation."
                else:
                    show sasha stand -vaginal -anal cumshot with hpunch
                    pause 0.25
                    with hpunch
                    pause 0.25
                    with hpunch
                    "At the very last moment I manage to somehow drag my dick out of Sasha, sparing her from taking me as I cum."
                    "As she moans from the sensation of the sudden withdrawal, I just pant from sheer exhaustion."
            else:
                if sasha_beads:
                    $ sasha.sub += 3
                    show sasha stand creampie with hpunch
                    pause 0.25
                    with hpunch
                    pause 0.25
                    with hpunch
                    "While I keep my dick firmly inside of Sasha as I cum, I also yank the beads out of her ass without hesitation."
                    "Pulled one way by my orgasm and another by the sensation of the beads, Sasha writhes delightfully beneath me."
                else:
                    $ sasha.sub += 2
                    "I might have normally pulled out at that moment, but something about the bondage aspect makes me want to dominate Sasha still further."
                    show sasha stand creampie with hpunch
                    pause 0.25
                    with hpunch
                    pause 0.25
                    with hpunch
                    "Holding her down more forcefully than ever, I make her ride out every second of my orgasm, revelling in her twitches and cries as I do so."
                if _return not in ["vaginal_inside_pill", "vaginal_inside_pregnant"]:
                    $ sasha.impregnate()
        "Doggy style" if hero.sexperience >= 20:
            scene sasha doggy
            show sasha doggy rope
            if CONDOM:
                show sasha doggy condom
            if "anal_beads" in hero.inventory and not sasha_beads:
                "Sasha makes a move to rise, but I take her by the shoulders and forced her back down onto the bed again."
                "She glances back over her shoulder at me, eyes widening, as I pick up the anal beads."
                show sasha doggy beads3
                "I make a point of parting her buttocks and inserting one bead after another, enjoying the way her body twitches as she takes them into her ass."
                show sasha doggy beads
                "Only when the last one is inserted to I quickly thrust my dick into her already slick lips."
                show sasha doggy mike vaginal
                "Reeling from the sensation of the beads, I can't tell if Sasha actually knows that I'm inside of her as well now."
                show sasha doggy ahegao
                "Not that it bothers me in the slightest, as I find that her state of flustered confusion just makes me that much more aroused."
                $ sasha_beads = True
            else:
                if sasha_beads:
                    show sasha doggy beads2
                "Liking the sight of Sasha submissive on her hands and knees, I'm not about to let her up again."
                "Instead I turn her around so that she's facing away from me and push her shoulders down to the mattress."
                "This leaves me staring down at her rounded ass, and I can't resist pulling back my hand and slapping both buttocks sharply."
                show sasha doggy impact hurt
                "Sasha squeals in shock and pain as her skin reddens, and I choose that exact moment to pull her backwards and onto my dick."
                show sasha doggy mike vaginal spanked
                "She must be feeling a mingling of pain and pleasure, as my entering her elicits more squeals and yelps, almost like a scolded dog."
                show sasha doggy ahegao
                "I can't resist squeezing and pinching her already ruddy buttocks, her flinching and crying serving to arouse me all the more."
            "I have no idea if it's the thrill I'm getting from the bondage or from seeing Sasha react to it, but I can't keep this up much longer."
            $ renpy.sound.play("sd/moans/sasha/sasha_moans_hard_orgasm.ogg", loop=True)
            call cum_reaction (sasha, 'vaginal', 20) from _call_cum_reaction_167
            if _return == "vaginal_condom":
                if sasha_beads:
                    $ sasha.sub += 2
                    "While I keep my dick firmly inside of Sasha as I cum, I also yank the beads out of her ass without hesitation."
                    "Pulled one way by my orgasm and another by the sensation of the beads, Sasha writhes delightfully beneath me."
                else:
                    $ sasha.sub += 1
                    "Holding her down more forcefully than ever, I make her ride out every second of my orgasm, revelling in her twitches and cries as I do so."
            elif _return == "vaginal_outside":
                if sasha_beads:
                    $ sasha.sub += 1
                    show sasha doggy beads3 -vaginal cumshot with hpunch
                    pause 0.25
                    with hpunch
                    pause 0.25
                    with hpunch
                    "I hear Sasha almost moan in disappointment as I pull out of her before I cum."
                    show sasha doggy anusopen ahegao
                    "But then I take hold of the beads and virtually rip them out of her ass, making her breathless at the sensation."
                else:
                    show sasha doggy -vaginal cumshot with hpunch
                    pause 0.25
                    with hpunch
                    pause 0.25
                    with hpunch
                    "At the very last moment I manage to somehow drag my dick out of Sasha, sparing her from taking me as I cum."
                    "As she moans from the sensation of the sudden withdrawal, I just pant from sheer exhaustion."
            else:
                if sasha_beads:
                    $ sasha.sub += 3
                    show sasha doggy beads ahegao cum with hpunch
                    pause 0.25
                    with hpunch
                    pause 0.25
                    with hpunch
                    "While I keep my dick firmly inside of Sasha as I cum, I also yank the beads out of her ass without hesitation."
                    show sasha doggy anusopen -beads
                    "Pulled one way by my orgasm and another by the sensation of the beads, Sasha writhes delightfully beneath me."
                else:
                    $ sasha.sub += 2
                    "I might have normally pulled out at that moment, but something about the bondage aspect makes me want to dominate Sasha still further."
                    show sasha doggy ahegao cum with hpunch
                    pause 0.25
                    with hpunch
                    pause 0.25
                    with hpunch
                    "Holding her down more forcefully than ever, I make her ride out every second of my orgasm, revelling in her twitches and cries as I do so."
                if _return not in ["vaginal_inside_pill", "vaginal_inside_pregnant"]:
                    $ sasha.impregnate()
    $ renpy.sound.play("sd/moans/sasha/sasha_panting.ogg", loop=True)
    "No one speaks as we lie there, drenched in each other's sweat and utterly exhausted."
    "I survived my first experience of bondage, and I can't say that I didn't like the vast majority of it."
    "The cheesy power ballad says that love's a battlefield."
    "And it certainly feels that way when there's a heavy dose of BDSM involved."
    stop sound
    return

label sasha_dom_cunnilingus_male:
    scene bg black
    show watch tv bree sasha
    with fade
    "I didn't notice it at first, but in the time since Sasha has begun to show how dominating she can be, there's always something hanging in the air around us."
    "No one else seems to be able to notice it, which is probably for the best."
    "But whenever we're alone, I can't help stealing sly glances in her direction, wondering if she'll make a move of some kind."
    "I think that this sense of anticipation on my part is one of the things that fuels it."
    "And I know she's feeling it too, as I often see her returning my looks with one of her own."
    "The only difference is that Sasha's looks are always filled with a knowing amusement, as if she enjoys my predicament immensely."
    "I have to say that I like it too!"
    "Sitting there, wondering if at any moment she might choose to demand something of me on a whim."
    "It's almost as exciting as actually doing what she asks of me...but not quite."
    "The exact same thing is happening to night, even as we're supposed to be doing nothing more than sitting on the sofa and watching the TV."
    show watch tv -bree sasha with fade
    "[bree.name]'s already lost the will to live and sloped off to her room, leaving us without any witnesses."
    "I can almost feel that mood come over Sasha as soon as we see our housemate leave the room."
    "And there it is again, that almost electric feeling in the air between us."
    "I risk a gaze over at Sasha, and she catches me doing so."
    "She raises her eyebrows and gives me a smile, looking for all the world as though she were completely innocent."
    "I look away again, instantly realising that I've made a rookie mistake by doing so."
    "Sasha already knows that I know that she's up to something."
    "But now she knows that I know that she knows!"
    "I should have just played it cool and held her gaze."
    "But now that I've been caught out in the open, she's well within her rights to call my bluff."
    "Sasha makes a great show of stretching out and yawning, lifting her arms over her head as she does so."
    "Every curve and line of her body is shown off in this one wave of movement, and I can't help staring in a longing fashion."
    scene bg livingroom at center, zoomAt(2.5, (0, 1400)), blur(5)
    show sasha a pain at center, zoomAt(2.0, (640, 1300))
    with fade
    sasha.say "[hero.name], baby...I'm feeling really tense tonight."
    "She has a sulky, slightly hurt expression and tone as she says this, using her voice to reel me in yet further."
    show sasha a talkative
    sasha.say "Give me a massage and make it all better?"
    show sasha a normal
    "I nod eagerly, thinking that she could have asked me to do something way more demanding has she wanted."
    mike.say "Uh, yeah - sure thing, Sasha."
    mike.say "Where exactly are you wanting it?"
    "Clever old me - I had to ask, didn't I?"
    show sasha a happy
    "Sasha smiles at my assent, fluttering her eyelashes at me."
    show sasha b sadsmile
    "She places her hands over her groin and makes a pouting face as if feeling discomfort even as she showed me the exact spot."
    show sasha b whining
    sasha.say "Right here's where it hurts."
    show sasha b talkative
    sasha.say "Oh, [hero.name] - you're an actual saint!"
    show sasha b normal
    "Well, maybe I should have seen that one coming."
    "But I'm committed now, and I don't see how I can get out of it."
    "You do understand that the problem's not that I don't want to go down on Sasha, don't you?"
    "Under the right circumstances, the prospect is a very appealing one indeed."
    "The issue here is one of exactly who's in control and who's taking the orders."
    "We both know that Sasha's in the house with us right now."
    "And it'd be a hell of a thing for her to just happen to walk into the room in the middle of me giving Sasha oral relief."
    "In fact, it'd make it plain to [bree.name] that I was pretty much Sasha's bitch!"
    "But all the same, I don't want to refuse and have her get mad at me."
    "Which would also have pretty much the same effect were Sasha to hear us going at it."
    show bg livingroom at center, traveling(2.5, 1.0, (0, 1000)), blur(5)
    show sasha at center, traveling(2.0, 1.0, (640, 720))
    "And so, understanding my role in the grand scheme of things, I crawl off of the sofa and onto my knees in front of Sasha."
    "She smiles with a mixture of approval and anticipation showing on her face as she does so."
    show sasha naked with dissolve
    "I obligingly reach up and begin to pull down the shorts that she's wearing, immediately finding that she had no panties on underneath."
    "So kind and thoughtful of her to make my job that much easier."
    scene bg black
    show sasha cunnilingus livingroom notongue
    with fade
    "Once I have her shorts off, I gently part Sasha's thighs so that I can position myself between them."
    play sound spank
    queue sound whip
    "She strokes me on the cheek as I come closer, still smiling at me, and then turns her attention back to the TV."
    "I can already feel my cheeks burning at this gesture, which is as patronising as patting me on the head or calling me a 'good boy'."
    "Rather than trying to assert myself or rebel in some way, the only way forward that I can see is to do such a good job on this that she'll thank me for it."
    "God, this girl's got me so much under her thumb it hurts to think about it!"
    show sasha cunnilingus down -notongue
    pause 0.1
    show sasha cunnilingus middle
    pause 0.1
    show sasha cunnilingus up
    pause 0.15
    show sasha cunnilingus middle
    pause 0.15
    show sasha cunnilingus down
    "I begin by licking lightly around the edges of Sasha's pussy, almost not even touching the outer folds."
    "I'm using only the tip of my tongue as I do this, feeling the prickling sensation of where she shaved herself down there."
    show sasha cunnilingus down
    pause 0.1
    show sasha cunnilingus middle
    pause 0.1
    show sasha cunnilingus up
    pause 0.15
    show sasha cunnilingus middle
    pause 0.15
    show sasha cunnilingus down
    "Her scent's already all that I can smell, but it's so fresh and appealing that it almost takes me by surprise."
    "As hard as it is to compliment someone on how pleasant their genitalia is to the senses."
    show sasha cunnilingus down
    pause 0.1
    show sasha cunnilingus middle
    pause 0.1
    show sasha cunnilingus up
    pause 0.15
    show sasha cunnilingus middle
    pause 0.15
    show sasha cunnilingus down
    "I have to admit that Sasha might just have the most pleasing pussy I've ever come across."
    show sasha cunnilingus down
    pause 0.1
    show sasha cunnilingus middle
    pause 0.1
    show sasha cunnilingus up
    pause 0.15
    show sasha cunnilingus middle
    pause 0.15
    show sasha cunnilingus down
    "It even turns out to taste pretty good too, as I discover as my tongue travels from the bottom to the top for the first time."
    $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_low.ogg", loop=True)
    "Sasha's becoming more receptive to my attentions the whole time, opening out to invite me in."
    show sasha cunnilingus down
    pause 0.05
    show sasha cunnilingus middle
    pause 0.05
    show sasha cunnilingus up
    pause 0.09
    show sasha cunnilingus middle
    pause 0.09
    show sasha cunnilingus down
    pause 0.05
    show sasha cunnilingus middle
    pause 0.05
    show sasha cunnilingus up
    pause 0.09
    show sasha cunnilingus middle
    pause 0.09
    show sasha cunnilingus down
    "But I still use the tips of a finger and thumb to open her wide enough for my tongue to begin slipping inside."
    "I can hear her moaning now, feel twinges of pleasure spreading outwards from her pussy as I lick at the inner folds ever more intently."
    show sasha cunnilingus down
    pause 0.05
    show sasha cunnilingus middle
    pause 0.05
    show sasha cunnilingus up
    pause 0.09
    show sasha cunnilingus middle
    pause 0.09
    show sasha cunnilingus down
    pause 0.05
    show sasha cunnilingus middle
    pause 0.05
    show sasha cunnilingus up
    pause 0.09
    show sasha cunnilingus middle
    pause 0.09
    show sasha cunnilingus down
    "My tongue lets me feel every ridge and furrow of Sasha's pussy so much more intensely than my fingers ever could."
    "It makes me feel a compulsion to trace every single one of them, over and again."
    stop sound
    show sasha cunnilingus pleasure
    sasha.say "Oh...[hero.name]...yes...please!"
    $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_medium.ogg", loop=True)
    "Suddenly I begin to wonder if [bree.name] hearing what's going on would actually be that much of a bad thing after all."
    "Sasha screaming out my name in relation to a tumult of passion would hardly be a reason to hang my head in shame."
    show sasha cunnilingus down
    pause 0.05
    show sasha cunnilingus middle
    pause 0.05
    show sasha cunnilingus up
    pause 0.09
    show sasha cunnilingus middle
    pause 0.09
    show sasha cunnilingus down
    pause 0.05
    show sasha cunnilingus middle
    pause 0.05
    show sasha cunnilingus up
    pause 0.09
    show sasha cunnilingus middle
    pause 0.09
    show sasha cunnilingus down
    "The thought makes me resolved to inspire more such shouts from Sasha, and I devote myself to making her as fulfilled as possible."
    stop sound
    show sasha cunnilingus pleasure blush
    sasha.say "Jesus...I think I'm gonna...I'm cumming!"
    $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_high.ogg", loop=True)
    "I have my tongue so far into Sasha when she says this that I'm afraid of it getting cramp."
    show sasha cunnilingus down
    pause 0.05
    show sasha cunnilingus middle
    pause 0.05
    show sasha cunnilingus up
    pause 0.09
    show sasha cunnilingus middle
    pause 0.09
    show sasha cunnilingus down
    pause 0.05
    show sasha cunnilingus middle
    pause 0.05
    show sasha cunnilingus up
    pause 0.09
    show sasha cunnilingus middle
    pause 0.09
    show sasha cunnilingus down
    "But nevertheless, I push on."
    show sasha cunnilingus down
    pause 0.05
    show sasha cunnilingus middle
    pause 0.05
    show sasha cunnilingus up ahegao with hpunch
    "And in doing so, push Sasha over her limit."
    stop sound
    sasha.say "Oh...oh shit...ooohhh shit!"
    $ renpy.sound.play("sd/moans/sasha/sasha_moans_light_orgasm.ogg", loop=True)
    show sasha cunnilingus down
    pause 0.05
    show sasha cunnilingus middle
    pause 0.05
    show sasha cunnilingus up with hpunch
    "Without thinking, she claps her hands around my head and knots her legs about my neck."
    show sasha cunnilingus down
    pause 0.05
    show sasha cunnilingus middle
    pause 0.05
    show sasha cunnilingus up with hpunch
    "In her attempt to prolong her orgasm, she's in real danger of smothering me at the same time."
    "I can think of worse ways to go, but still my basic instinct to survive makes me struggle to escape being suffocated by Sasha's pussy."
    $ renpy.sound.play("sd/moans/sasha/sasha_panting.ogg", loop=True)
    show sasha cunnilingus -up -notongue with fade
    "When I finally manage to tear my head free, it's at the same moment she loosens her grip."
    "Released from her passionate bondage, I topple backwards onto the sitting room floor."
    "My face is red and I'm audibly gasping from breath, as is Sasha, but for a very different reason."
    stop sound
    show sasha cunnilingus pleasure
    sasha.say "Thanks, [hero.name]..."
    show sasha cunnilingus normal
    "Her voice is coming in short bursts, just like her breath."
    show sasha cunnilingus pleasure
    sasha.say "That really loosened me up!"
    show sasha cunnilingus normal
    "I just nod slowly, already feeling the strained and knotted muscles in my neck and shoulders."
    "Somehow, I don't think I can ask her to return the favour!"
    scene bg black with dissolve
    pause 0.3
    $ hero.cancel_activity()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
