init python:
    InteractActivity(**{
    "name": "fuck_bree",
    "display_name": "Fuck",
    "label": "ACTIVE_GIRL_fuck_ROOM",
    "conditions": [
        IsTimeOfDay("evening"),
        HeroTarget(
            IsGender("male"),
            HasStamina()
            ),
        PersonTarget(bree,
            IsActive(),
            MinStat("love", 150),
            MinStat("sexperience", 2),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })

    InteractActivity(**{
    "name": "fuck_bree_beach",
    "display_name": "Fuck",
    "label": "ACTIVE_GIRL_fuck_ROOM",
    "conditions": [
        IsHour(14, 18),
        HeroTarget(
            IsGender("male"),
            IsRoom("beach", "date_beach", "date_nudistbeach"),
            HasStamina(),
            ),
        PersonTarget(bree,
            IsActive(),
            MinStat("love", 150),
            MinStat("sexperience", 2),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })


    Event(**{
    "name": "bree_fuck_sasha_bedroom",
    "label": "bree_fuck_sasha_bedroom_intro",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            ),
        PersonTarget(bree,
            IsActive(),
            MinStat("love", 160),
            MinStat("sexperience", 2),
            HasRoomTag("home"),
            ),
        PersonTarget(sasha,
            Not(HasRoomTag("home")),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "bree_hottub_sex_male",
    "label": "bree_hottub_sex_male",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("date_hot_tub_home")),
        PersonTarget(bree,
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

label bree_fuck_bathroom:
    $ game.play_music("music/roa_music/city_nights.ogg")
    scene bg bathroom
    show bree naked
    $ renpy.sound.play("sd/shower.ogg", loop=True)






    "I pull the shower-curtain aside and step in behind her, the first thing [bree.name] knows about it is the sensation of my cock against her backside."
    mike.say "Surprise, [bree.name]!"
    show bree naked surprised at startle
    "She lets out a yelp of surprise, throwing her arms up and allowing me to step forwards and wrap my arms around her."
    bree.say "Oh, [hero.name] - you scared the life out of me!"
    show bree naked annoyed at center, zoomAt(1.5, (640, 1000))
    "She's leaning back into me by now, letting me take a little of her weight."
    mike.say "I'm sorry, [bree.name]...would you like me to get out of your hair?"
    "I run my hands over her thighs as I say this, letting her feel my dick up against her buttocks."
    show bree happy at center, zoomAt(1.0, (640, 1000)), startle
    "She lets out a chuckle, and I feel her reach around to stroke my cock."
    show bree normal blush
    bree.say "No...you're here now, so you might as well stay and let me help you get cleaned up!"
    if Harem.find_by_name("home") and sasha.room == game.room and not sasha.hidden and not sasha.flags.cheated:
        hide bree
        show bree naked normal at right
        show sasha at left
        sasha.say "Can I join in?"
        menu:
            "Yes":
                mike.say "That would be great."
                call home_harem_bree_sasha_shower from _call_shower_ffm
                $ bree.love += 2
                $ sasha.love += 2
                $ sasha.lesbian += 1
                $ bree.lesbian += 1
                $ sasha.sexperience += 1
                $ bree.sexperience += 1
                return
            "No":
                $ sasha.love -= 2
                mike.say "Sorry, I wanna be alone with [bree.name] a little."
                hide sasha































    $ bree.flags.showersex = True
    hide bree
    show bree showersex wet
    with fade
    if bree.is_visibly_pregnant:
        "Aware of just how delicate [bree.name]'s condition is right now, I loop one arm under hers to hold her up."
        "The other I use to reach around and cradle her belly so that I can support her and make sure she won't slip while we make love."
        "Though she's bent like a bow, I move my legs and abdomen to bring my cock into a position where I can find my way into [bree.name]."
        "I enter her slowly and with infinite care, caressing her swollen belly as she sinks onto me."
    elif bree.is_collared:
        "I'm more than ready to have my way with [bree.name] by now, and she needs to be taken in hand to make that happen."
        "I seize her arms with one of my own and grab hold of her collar firmly with the other."
        "Forced against the wall, breasts and belly pressed to the tiles, [bree.name] yelps as she feels me searching for her pussy."
        "Almost as soon as I find it, I thrust myself into her, enjoying the sounds that she makes as I do so."
    else:
        "I can already feel [bree.name] slipping and sliding around thanks to the fact that we're both so wet from the shower."
        "Not wanting to be chasing her around like a bar of slick soap, I put my arms under hers and pin them against my chest."
        "At the same time, I push my groin forwards, lifting her just enough to make it easier for my cock to snake between her legs and find her pussy."
        "Pushing myself as deep into her as I can go, [bree.name]'s belly and breasts are pressed up against the tiled wall."
    "The warmth of the water and the steam rising around us seems to make the act all the more intense and enjoyable."
    "I settle into a steady rhythm that [bree.name] mirrors, meaning that we both move as one, our bodies taking and giving in almost equal measures."
    "[bree.name] has her head thrown back by now, resting on my shoulder and sending her hair falling down my back."
    "I can feel the water running through it, turning her locks into heavy tendrils, as it flows like a river through it."
    "[bree.name]'s legs twine with my own, as though she's trying to climb upwards and let me come yet further into her."
    "I want to pick her up, but there's nowhere to go but up against the wall, and she's already almost pressed too close to it."
    "So instead I redouble the intensity of my thrusts, making [bree.name] keep up even as she begins to pant quite dramatically."
    "I can't blame her for that - the heat in the shower is starting to become almost overwhelming."
    "We've been kept from realising this by the fact that, as much as we might be sweating right now, the water is just washing it straight away."
    "I begin to feel [bree.name]'s muscles getting weaker with each moment that passes, as if the heat is leeching her strength away."
    "More and more I start to find myself supporting her, rather than simply holding onto her."
    "And I can't help worrying that she will pass out if I don't do something sooner, rather than later."
    show bree showersex wet speed




























    "I can feel myself getting overcome by the heat in the exact same way as [bree.name]."
    "And I realise that, if I up the pace now, I can maybe cum before I have to admit defeat and carry her out of the shower in a dead faint."
    bree.say "[hero.name]...I'm feeling...feeling light-headed!"
    "I try to pretend like I can't hear [bree.name]'s warning, instead keeping myself going the whole time."
    bree.say "Please...[hero.name]...I can see weird shit flashing...before my...eyes!"
    with vpunch
    "It's perhaps a second after this last plea that I cum."
    with vpunch
    pause 0.25
    with vpunch
    "Even though she's out of it, [bree.name] feels the full force of the orgasm."
    "For a moment, she seems to go limp in my arms and I'm convinced that she's passed out."
    "But then she shudders and manages to support some of her own weight once more."
    "[bree.name] shudders and looks around her, as if not sure how she came to be so disoriented in the middle of the bathroom."
    scene bg bathroom
    show bree naked mindless blush at center, zoomAt(1.5, (640, 1000))
    with fade
    bree.say "Oooh, [hero.name]...I feel so dizzy - what happened?"
    mike.say "You blacked out for a couple of seconds back there, [bree.name]."
    mike.say "I only just managed to catch you in time, otherwise you could have had a nasty fall!"
    "Well, if she doesn't recall my rather selfish efforts to cum before she passed out, I'm not going to be the one to remind her."
    "[bree.name] shakes her head, clearly still feeling the effects of being overcome by the heat."
    $ bree.love += 1
    show bree wink
    bree.say "Maybe next time, we should think about the benefits of taking a COLD shower, yeah?"
    "I shrug and nod in agreement, just happy not to have been caught out putting my own orgasm before [bree.name]'s bodily well-being."
    stop sound fadeout 1.0
    scene bg black with dissolve
    $ bree.sexperience += 1
    return

label bree_fuck_livingroom:
label bree_fuck_kitchen:
label bree_fuck_pool:
label bree_fuck_bedroom1:
label bree_fuck_bedroom2:
label bree_fuck_secondfloor:
label bree_fuck_home:
    $ game.play_music("music/roa_music/city_nights.ogg")
    show bree
    mike.say "Hey, wanna come and have fun in my bedroom?"
    bree.say "Sure."
    if Harem.find(bree, name='home'):
        call home_harem_fuck_choices ('bree') from _call_home_harem_fuck_choice_4
    else:
        call bree_fuck_date_male from _call_bree_fuck_date
    return

label bree_fuck_date_nudistbeach:
label bree_fuck_beach:
label bree_fuck_date_beach:
    $ game.play_music("music/roa_music/city_nights.ogg")
    "I know that [bree.name] and I are both really fond of the beach, slipping off there whenever the season and the weather are right and we have enough free time on our hands."
    "But the weird thing is that in all of the time we've been living together, we've never really made an effort to go to the beach together."
    "Maybe it's just that urge you get to run off and do something on your own whenever you really want get away from the daily grind and relax."
    "I honestly don't think either of us has been deliberately avoiding going there with the other - well, at least I haven't."
    "So today, when I decided that I was intent upon another day at the beach, I made a point of coming straight out and asking [bree.name] if she wanted to tag along."
    "My suspicions that we'd just been overlooking the possibility before now seemed to be confirmed."
    "It only took [bree.name] a couple of seconds to think about it before nodding and hurrying to collect her beach stuff."
    "And then we were into the car and off."
    show bree annoyed at right with easeinright
    "Once we pull up in the car park a little way from where the dunes begin, I can see [bree.name] glancing around as if she's looking for someone."
    "Normally I'd be starting to get jealous at this point, wondering if she had a crush on some tanned beach-bum or surfer type that I don't know about."
    "But she looks nervous and maybe even a little embarrassed, so much so that I soon forget any suspicions that I might have had out of concern."
    mike.say "[bree.name], are you feeling okay?"
    show bree surprised at right, startle
    pause 0.5
    show bree annoyed
    bree.say "What...oh, yeah...I'm fine."
    mike.say "You sure?"
    mike.say "You look like something's bugging you!"
    show bree normal
    "[bree.name] shakes her head, her expression becoming visibly more calm and collected as she does so."
    bree.say "Oh, it's nothing really - just some weird guy I bumped into the last time I was here."
    "She punctuates the statement with a dismissive wave of her hand, which I find less than convincing."
    bree.say "And anyway, it's not a problem today, now is it?"
    show bree happy
    bree.say "Because I have you here with me for company, [hero.name]."
    "I just nod and smile, already envisioning the muscle-bound admirer that's just waiting to kick sand in my face and bury me up to my neck as the tide's coming in."
    show bree normal at right5 with ease
    "I'm already wearing my shorts and a T-shirt when we start to make our way across the sand, carrying my few things under one arm."
    "[bree.name]'s likewise carrying little, but keeping the swimsuit she's chosen to wear hidden beneath a sarong that's tied over one of her shoulders."
    show bree normal at right4 with ease
    "Happy to let her pick the spot where we spread our towels, I trudge through the warm sand a little behind her."
    "And all the while I'm enjoying a little of her behind, if you'll forgive me the awful pun."
    show bree normal at center with ease
    "Eventually, after walking past literally dozens of free spots that seemed more than adequate to my eyes, [bree.name] settles on one that looks no different to any of the others."
    "We drop our stuff down and spread out the towels next to each other, after which I whip off my T-shirt, eager to get down to the serious business of doing nothing in the sun."
    "But I note that [bree.name] doesn't seem to be in anywhere near as much of a hurry, as she shakes her head at my hastiness."
    "I begin to feel a little insulted by this, but the thought disappears from my mind, along with pretty much everything else, a moment later."
    "All of which happens because [bree.name] puts a hand up to the knot that's tying her sarong in place and undoes it deftly."
    "In one smooth motion, the entire thing falls away and reveals the skimpy, white bikini that she's wearing underneath."
    "The move reminds me of the unveiling ceremonies that they have for works of art, and [bree.name] certainly qualifies as one of those."
    "She seems to note my appreciation of her outfit and she finally sits down on her towel beside me."
    "At least I think that's what the knowing smile on her face is on account of..."
    "I watch as she reaches into her bag and pulls out a bottle of sun-cream, already shielding her eyes from the glaze of the rays beating down on us."
    menu:
        "Watch":
            "[bree.name] squeezes a good-sized dollop of the greasy, white cream into the palm of her hand and begins to rub it up her arms."
            "The sound, the colour and the stuff being all over [bree.name]'s hands instantly puts me in mind of the most inappropriate things possible."
            show bree close at top_to_bottom
            "But then how can I be expected to think of literally anything else, especially when I'm sitting so close to her and watching every move she makes?"
            "[bree.name] may well be conscientiously covering every inch of her exposed skin with a generous amount of cream for the sake of her health."
            "Though from my point of view it looks like nothing more than her deliberately oiling herself up in front of me."
            show bree at bottom_to_top
            "I watch in rapt silence as her shoulders, chest and stomach all begin to glisten temptingly in the sun."
            "And then she'd moving on to her hips, thighs, calves and feet - enough to make a leg fetishist openly weep."
            "Once she's finally covered from head to toe, [bree.name] lies back on her towel, the cream making her almost shimmer in the sunlight."
        "Help":
            $ bree.love += 1
            mike.say "Hey, [bree.name] - why don't you let me get that for you?"
            show bree annoyed
            "[bree.name] regards me with a raised eyebrow, clearly not believing that my motives are purely altruistic in nature."
            show bree flirt
            "But then she shrugs and gives me a languid smile, tossing the sun-cream to me so that I have to struggle to catch it."
            bree.say "Sure, why not?"
            bree.say "Get rubbing, [hero.name] - and don't skimp on the cream!"
            "I squeeze a generous amount of sun-cream onto the palm of my hand as [bree.name] rolls obligingly onto her belly."
            "The temptation would be to go straight for her more than inviting buttocks."
            show bree at center, zoomAt(2.5, (640, 1640))
            "But I manage to restrain myself enough to begin in the more sensible and less pervy staring point of [bree.name]'s shoulders and the nape of her neck."
            "[bree.name] sighs and lets out appreciative oohs and aahs as I work the cream into her skin."
            hide bree
            show bree flirt close at top_to_bottom
            "The noises she's making might sound perfectly innocent to any casual passer-by, but I know that she's deliberately teasing me the whole time."
            "This only gets worse as I make my way down her back and start working my way over her buttocks and lower."
            "By now [bree.name]'s sighs have almost turned into genuine moans of pleasure."
            show bree at bottom_to_top
            "Clearly she's enjoying teasing me all the while I'm massaging the cream into parts of her body that are making me so hot under the collar - even though I'm not even wearing one."
            "By the time I've finished the job, [bree.name] rolls onto her side and looks herself up and down, as if admiring the job I've done."
    "[bree.name] chuckles at my quite obvious state of discomfort after what I've just been witness to."
    show bree wink
    bree.say "[hero.name], are YOU feeling okay?"
    "She takes great amusement in turning my question from earlier around on me."
    bree.say "Maybe I could help you out by returning the favour?"
    bree.say "Is there something of yours that I could rub?"
    show bree flirt
    "As if her tone of voice wasn't enough to impress upon me the true meaning of her words, [bree.name] reaches out and stokes my now painfully visible erection through my shorts."
    "I glance this way and that, my face making it clear how much I want to take her up on the offer, but noting the sheer number of other people around us on the beach."
    "[bree.name] picks up on the source of my reluctance almost instantly, a knowing smile spreading across her face as she shakes her head."
    bree.say "Oh no, don't you worry about anyone seeing us."
    bree.say "Trust me - I know a place that's just perfect for what I have in mind!"
    mike.say "Erm, okay...if you say so."
    hide bree
    show bree evil blush with vpunch
    "[bree.name]'s smile grows even wider and becomes intriguingly mischievous as she takes my hand and almost pulls me to my feet."
    show bree at left4 with ease
    "I hurry to follow as she leads me further up the beach and away from the shoreline, up to the point where the sand becomes dunes that are covered in long grass."
    show bree at left5 with ease
    "But rather than the dunes and the grass, I begin to see that [bree.name]'s actually making straight for a line of wooden beach-huts."
    show bree at left with ease
    "Once we reach them, [bree.name] wastes no time in walking around the back of them and choosing a particular spot for what she intends to do."
    "Even without taking the time to really study all of the angles, I'm pretty certain that we won't be seen from here."
    "In fact, I'd guess that the only way someone could spot us would be to actually walk around the back in the same way we just did."
    "While I'm definitely intrigued as to just how [bree.name] came to know about this place, I keep my interest to myself."
    "I can't think of a better way to ruin the moment and cheat myself out of something that promises to be enjoyable in the extreme by suddenly asking a load of awkward questions."
    "Instead I give [bree.name] what I hope is an encouraging smile and allow her to back me up against the plank wall of the nearest beach-hut."
    "She takes hold of the waistband of my shorts, tugging them suddenly down so that my erection is pulled down and then released like a spring."
    hide bree
    show bree beach bj
    with fade
    "Giggling at my expression of discomfort, [bree.name] takes my cock in one hand and begins to stroke it whilst making the same kind of sound you might use to comfort a child in pain."
    "She keeps on stroking the shaft as she gets down onto her knees, the motion slowly turning into an ever more vigorous rubbing the whole time."
    show bree beach bj tongue
    "By now her soothing tones have taken on a distinctly more hungry, almost carnal tone."
    show bree beach bj blowjob
    "[bree.name] surprises me then by almost making a lunge to bite at the head of my cock, seizing it between her teeth and encircling it with her tongue at the same time."
    show mouth_insert bree zorder 1 at zoomAt(1, (840, 160))
    "This level of intensity only increases as she starts to take me deeper into her mouth in what feels like mouthfuls being swallowed by a hungry animal."
    show bree beach bj blowjob
    "I've never seen [bree.name] like this before, certainly never felt her like this before."
    "It's almost as though she's doing this because she feels that she had something to prove."
    show bree beach bj blowjob cheek_bulge
    "But what that is and to whom she had to prove it, I have no idea."
    "She's certainly proving to me that she has a wild side, and I'm glad of the hut wall to support me, so intense is the feeling of her lips and tongue on my cock."
    show bree beach bj blowjob -cheek_bulge
    "I can feel her starting to squeeze my balls now, just when I thought that there was nothing more she could do to ramp up the pressure."
    "I'm honestly trying to keep my mouth shut, biting at my lip when I want to be shouting out loud."
    show bree beach bj blowjob cheek_bulge
    "Instead I make do with balling one of my hands into a fist and pounding it against the planks of the wall, hoping that it's sturdy enough to take the abuse."
    "If she takes me any deeper now, I'll literally be in her throat!"
    show bree beach bj blowjob surprised with hpunch
    "And that's the thought that breaks me and lets [bree.name] know that I'm starting to cum."
    show bree beach bj handjob cumshot
    show mouth_insert bree cum
    with hpunch
    "Quickly and deliberately, she releases me from her mouth so that she can receive the full effect of the orgasm."
    show bree beach bj handjob -cumshot cum onface with hpunch
    "Rather than being caught off guard when the cum spatters across her face, [bree.name] seems to relish the sensation, even opening her mouth to catch what she can of it."
    hide mouth_insert
    hide bree beach bj
    show bree naked flirt cum at center, zoomAt(2.5, (640, 1640))
    with fade
    "I look down at her, still panting and exhausted as I let the wall do most of the work of keeping me on my feet."
    bree.say "I don't suppose you remembered to bring something for me to clean up with?"
    show bree happy
    "[bree.name] laughs as I shake my head, already beginning to lick at the cum on her lips as she does her best to make herself look presentable again."
    $ bree.flags.beachsex = True
    $ bree.flags.bj += 1
    scene bg black with dissolve
    return


label bree_hottub_sex_male:
    $ game.active_date.clothes = "swimsuit"
    $ CONDOM = False
    show bg pool
    show hottub bree
    "Today's one of those days when everyone's trying to act normal, like there's nothing on their minds."
    "It's just one of those times when [bree.name] and I both happened to feel like taking a dip in the hot-tub."
    "There's no deeper meaning to that, no undercurrent of barely suppressed sexual tension."
    "We're just taking some time out of the day to unwind in the warm, bubbling water."
    "And we happen to be doing it at exactly the same time too."
    "[bree.name] just keeps smiling at me because she's having a good time."
    "It's not because she's thinking about doing something more intimate the whole time."
    "And as for me, well..."
    "I can get a massive erection at the most random and inappropriate of times."
    "I'm not hard as a rock because [bree.name]'s sitting there in her swimsuit."
    "Sitting there with her blonde locks cascading down her shoulders like a golden waterfall."
    "Sitting there with her fantastic body on show like something out of a dream."
    "Her lips parting with barely suppressed desire..."
    "Oh shit, who am I trying to kid?"
    "[bree.name]'s got me worked up like a horny teenager!"
    bree.say "Ah, [hero.name]?"
    bree.say "Are you feeling okay?"
    "At the sound of [bree.name]'s voice, I snap out of my funk."
    "Shaking my head, I try to focus on what she was saying."
    mike.say "Huh...what..."
    mike.say "Oh, no...I'm okay, [bree.name]."
    mike.say "I was just miles away, that's all!"
    "[bree.name] nods and smiles at this."
    "Though she still looks less than convinced."
    bree.say "Are you sure, [hero.name]?"
    bree.say "Maybe the water's too hot for you today?"
    "I shake my head again."
    mike.say "Nah, [bree.name]."
    mike.say "I'm fine, really."
    mike.say "I just have stuff on my mind."
    "[bree.name] cocks her head on one side."
    "A thoughtful look forms on her face."
    bree.say "Well..."
    bree.say "Maybe I could, you know..."
    bree.say "Do something to help take your mind off of it?"
    "As she says this, [bree.name] moves closer to me."
    "She puts her hand on my wrist."
    "And then she gently guides my hand to her chest."
    "I'm taken by surprise for a moment, staring open-eyed."
    "But then, almost as quickly, I manage to shake it off."
    "Maybe [bree.name] was thinking along the same lines as me this whole time."
    "Or maybe she really is trying her best to help me out."
    "Either way, I'm not about to look a gift horse in the mouth!"
    mike.say "Oh, wow, [bree.name]!"
    mike.say "You sure know how to help me out!"
    "[bree.name]'s cheeks colour a little."
    "And she lets out a nervous giggle."
    bree.say "Well..."
    bree.say "I kinda wanted to ask if you felt..."
    bree.say "You know...frisky?"
    "I can't help laughing at her choice of words."
    mike.say "Yeah, [bree.name]."
    mike.say "You always make me feel frisky!"
    "[bree.name] giggles again, but then begins to moan as I squeeze her breast."
    "It feels so good in the palm of my hand, like kneading dough."
    "She reaches out as I massage it, slipping her hand into my trunks."
    bree.say "Oh, [hero.name]!"
    bree.say "You weren't kidding!"
    "[bree.name] wastes no time in pulling down my trunks to reveal my stiff cock."
    "And she can't help eyeing it with what looks like real hunger too!"
    call bree_dick_reactions from _call_bree_dick_reactions_1
    bree.say "I...I think we'd better get that inside of me, [hero.name]."
    bree.say "We'll both feel so much better then!"
    show hottub sex male bree outside with fade
    "With that, [bree.name] crouches in the water and angles herself towards my cock."
    "I sit back and watch in fascination as she lowers herself onto it."
    "Even as keen as she is, it still takes a little teasing to convince her pussy."
    "And so [bree.name] rubs the head up and down her lips until they're good and slick."
    show hottub sex male bree inside
    "Then she guides the tip in just enough to be sure."
    "As if watching her do this wasn't hot to begin with, the feeling is incredible."
    "[bree.name] looks like a work of art as she sinks down onto me."
    "And all I have to do is support her as she rides my cock."
    "The smile that she has on her face the whole time sweet too."
    "Almost as sweet as her pussy feels around my dick."
    mike.say "Oh, shit, [bree.name]!"
    mike.say "That feels amazing!"
    bree.say "Ah..."
    bree.say "It...it's pretty good for me too!"
    "I reach out and take hold of [bree.name] around the waist."
    "This means that I can start to use my own strength as well."
    "And the effect seems to be instant, making her toss her head from side to side."
    "I feel like [bree.name] was the one that started this thing off."
    "But now it's my turn to do all that I can to take it to the next level."
    "And so I use all of the energy that I possess to make that happen."
    "Pretty soon I can see the rewards of my efforts."
    "[bree.name] had her eyes squeezed tightly shut, like she's about to lose it."
    "And I can feel the way that her muscles are starting to twitch."
    "She's about to cum, and she's squeezing me until I cum too!"
    call cum_reaction (bree, 'vaginal', 1) from _call_cum_reaction_51
    if _return == "vaginal_outside":
        show hottub sex male outside
        "Somehow I manage to pull out of [bree.name] at the very last moment."
        "She lets out a moan at the sensation, clinging to me the whole time."
        show hottub sex male cumshot with vpunch
        pause 0.25
        with vpunch
        pause 0.25
        with vpunch
        "And that means I shoot my load all over her chest and belly."
        $ bree.sub += 1
        "I pant as I watch it hit her skin and then start to run down into the water."
    else:
        "I was right, [bree.name]'s cumming right now - and she's taking me with her!"
        show hottub sex male cumshot with vpunch
        "All I can do is hold on until the end, and then lose myself totally."
        show hottub sex male ahegao with vpunch
        "I hear myself groan as I fill [bree.name] with all I have, and she moans in turn."
        with vpunch
        $ bree.love += 1
        "We cum almost in the same moment, clinging to each other for support."
    hide hottub sex male
    show hottub bree
    with fade
    "Utterly spent, I sit down in the water, my muscles finally failing me."
    "[bree.name] falls atop me, wrapping her limp limbs around my body."
    "She sighs, still not able to form as much as a single word."
    "But it doesn't matter, as she's done what she set out to."
    "She really has helped with what was on my mind, by making it a reality."
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ bree.sexperience += 1
    $ game.active_date.clothes = None
    return

label bree_fuck_date_male(location="hero"):
    $ game.play_music("music/roa_music/city_nights.ogg")
    $ intro_foreplay = False


    call bree_fuck_date_intro_male (location) from _call_bree_fuck_date_intro_male


    if not intro_foreplay:
        call bree_dick_reactions from _call_bree_dick_reactions_2


    if "bree_event_07b" in DONE and bree.sexperience > 1 and not bree.flags.tittyfuck:
        call bree_fuck_date_titfuck from _call_bree_fuck_date_titfuck
        $ bree.flags.tittyfuck = True
        call handle_npc_leaving (bree, _return) from _call_handle_npc_leaving_5
        return


    call bree_fuck_date_foreplay_male from _call_bree_fuck_date_foreplay_male


    call bree_fuck_date_choices_male from _call_bree_fuck_date_choices_male


    call handle_npc_leaving (bree, _return) from _call_handle_npc_leaving_6
    if _return:
        return


    hide bree
    call bree_sleep_date_fuck (location) from _call_bree_sleep_date_fuck
    return

label bree_fuck_date_intro_male(location="hero"):
    if bree.sexperience <= 1:
        scene bg street
        show bree
        with fade
        "Holding hands for the first time, [bree.name] and I decide to walk home."
        show bree happy
        "The chat and laughter from the evening continues on the way back to the house."
        "[bree.name] gets a little loud on occasion, but none of the stares that we get are enough to spoil our mood."
        scene bg livingroom
        show bree normal
        with fade
        "Neither of us has a clue if Sasha's even in when we stagger through the front door."
        "But the thought that she might seems to have us both instantly in stitches for some reason."
        show bree happy
        "I manage to mess up a knock knock joke as we stand in the hall, and I can't tell if [bree.name]'s genuinely amused or just laughing from sympathy."
        scene bg bedroom1
        $ game.room = "bedroom1"
        show bree
        with fade
        "Either way, it lasts until we're in my bedroom and the door closes behind us."
        "[bree.name] almost collapses onto my bed, and I flop down beside her."
        show bree b blush
        bree.say "I...I had a really nice time tonight, [hero.name]."
        mike.say "Me too, [bree.name]..."
        bree.say "Why are you always so nice to me?"
        if not bree.is_sex_slave:
            mike.say "Because you're my girlfriend...you are my girlfriend, aren't you?"
        elif bree.flags.mikeNickname in nickname_daddy:
            mike.say "Because you're my girlfriend...you are my little girl, aren't you?"
        else:
            mike.say "Because you're my slave...you are my slave, aren't you?"
        show bree b evil
        "[bree.name] giggles, looking away for a moment."
        "I catch the barest hint of red on her cheeks as she takes a deep breath."
        "I sense that she's plucking up the courage for something."
        show bree b normal
        "[bree.name] takes a deep breath, looking me in the eye as she takes my hand in her own."
        if not bree.is_sex_slave:
            bree.say "Yeah, [hero.name]...I'm your girlfriend."
            bree.say "And I want to do the kind of things that a boyfriend and girlfriend do together..."
        elif bree.flags.mikeNickname in nickname_daddy:
            bree.say "Yeah, [hero.name]...I'm your little girl."
            bree.say "And I want to be a good girl to you Daddy, I would do anything to be a good girl."
        else:
            bree.say "Yeah, Master...I'm your slave."
            bree.say "And I want you to use me in everyway a Master can use his prized sex slave..."
        play music "music/roa_music/juice.ogg" loop fadein 0.5 fadeout 0.5
        "I can feel my heart begin to pound in my chest in anticipation of just what [bree.name] might have in mind."
        "And my body is already reacting without asking permission, as a bulge begins to show in the front of my pants."
        "[bree.name] follows my eyes downward, seeing the same evidence of my arousal."
        show bree b flirt
        "She giggles at the sight of it, her cheeks colouring in a way that somehow makes her look even cuter."
        "[bree.name] slides off of the bed and kneels before me, encouraging me to strip off my shirt."
        "While it's only half over my head, I can already feel her hands unbuttoning my pants and then unzipping my flies."
        "Tossing away my shirt, I'm treated to the sight of [bree.name] enthusiastically pulling down and then off both my pants and my underwear."
        call bree_dick_reactions from _call_bree_dick_reactions
        show bree b naked normal with dissolve
        "I could return the favour and help [bree.name] strip off her own clothes."
        "But I'm just too taken with the sight of her revealing herself a little at a time to be able to do anything but watch in silence."
        "I have no idea of what [bree.name] intends to do next, and once she's totally naked, I can't think of anything else at all."
        "So I simply stare at her, waiting with baited breath to see what happens next."
    else:
        play music "music/roa_music/juice.ogg" loop fadeout .5 fadein .5
        if bree.sexperience % 3 == 1 and hero.sexperience >= 20:
            call bree_fuck_date_oral_intro from _call_bree_fuck_date_oral_intro
            call bree_dick_reactions from _call_bree_dick_reactions_3
            call bree_fuck_date_oral from _call_bree_fuck_date_oral
            $ intro_foreplay = True
        elif bree.sexperience % 3 == 0:
            scene bg bedroom1
            $ game.room = "bedroom1"
            show bree
            with fade
            "It's not like this is the first time [bree.name]'s ever set foot inside of my bedroom."
            "But there's still an odd feeling in the air, as if neither of us really knows what to do next."
            "We glance at each other and then quickly away again."
            show bree evil
            "And then [bree.name] seems to find the courage from somewhere to break the awkward silence between us."
            bree.say "This is so stupid!"
            mike.say "Yeah, I know..."
            bree.say "We're sitting here, acting like a couple of strangers!"
            "I shrug at her comment."
            mike.say "Well, this is kind of a new situation for us to be in together..."
            mike.say "I guess I'm just afraid that I'm going to say something stupid or mess up!"
            show bree happy at center, startle
            "[bree.name]'s laughter at this makes me think I've done just that."
            show bree normal
            bree.say "I was thinking the exact same thing!"
            bree.say "Is it the thought of us being in your room?"
            bree.say "We can go up the stairs to mine, if you'd like?"
            mike.say "I'm not sure it's the location that's the problem..."
            "It's about this time that both of us seem to stop talking at the exact same moment."
            "Words might have failed us, but I swear I can feel us begin to communicate on another level entirely."
            show bree normal blush at center, zoomAt(2.0, (640, 1340)) with dissolve
            "Looking each other straight in the eye, I feel [bree.name]'s hand reach out for mine."
            "Our fingers twine together, and we finally close the distance between us."
            hide bree
            show bree kiss
            with fade
            $ bree.flags.kiss += 1
            "She's as tentative as me when we begin to kiss, and so it's a slow, sensual process of almost feeling each other out."
            "But with each pass we make, I can feel her instinctively pulling closer to me, until we're pressed together, belly-to-belly."
            "Rather than making the whole thing chaste, I find that [bree.name]'s need to build her confidence with me means my own passion builds at the same time."
            "This means that by the time we're wrapped up in a close embrace, my anticipation is becoming almost unbearable."
            "I can hear [bree.name] making little sighing and almost mewing sounds between kisses, almost like a preamble for what's still to come."
            "Her hand begins to explore my body, travelling over my stomach and down, below my belt."
            "Here, [bree.name] finds the unavoidable proof of just what kind of an effect she's having on me."
            "She breaks the kiss for a moment, stroking my cock through the fabric of my pants."
            "And then she shoulders off her jacket and begins to pull off her top."
            "As if suddenly brought back to life by [bree.name]'s example, I start to strip off my own clothes a second later."
            hide bree kiss
            show bree naked blush
            with fade
            "[bree.name] and I have seen each other every day for as long as we've been living under the same roof."
            "But this is the very first time that we've seen each other naked."
            show bree b naked close at top_to_bottom
            "I couldn't have imagined anything that would come close to doing the sight of her unclothed body justice."
            "She's just perfect - smooth skin, flawless curves, pert breasts and blonde hair tumbling over her shoulders."
            "And then there's the bashful expression on her face and the blush spreading across her cheeks."
            show bree b naked at bottom_to_top
            "Is she blushing from embarrassment?"
            "No, I realise in that moment that I'm staring at her like a starving man seeing food."
            "I look away quickly."
            mike.say "I...I didn't think you could look any more beautiful, [bree.name]..."
            mike.say "But I was wrong!"
            hide bree
            show bree b naked flirt
            "There's a look in her eyes that takes a moment for me to understand."
            "It's like a glistening, almost as though she's going to shed a tear."
            "But then I finally understand that I've managed to say just the right thing at just the right moment."
        else:
            scene bg street
            show bree blush
            with fade
            "[bree.name]'s practically walking on air by the time we make it back to the house."
            "And that's thanks to your's truly pretty much being the wizard of dates!"
            "I spent a hell of a lot of time planning what went down tonight."
            "And what can I say - [bree.name] loved every minute of it!"
            "And now it looks like I'm about to be rewarded for my efforts."
            scene bg livingroom with fade
            show bree blush at right with easeinright
            "Because she's not making for the kitchen to get a coffee."
            "And she's not looking around for Sasha to brag about the date either."
            show bree at center with ease
            "Oh no - [bree.name]'s making straight for my bedroom!"
            "It's not like I want to be going anywhere else right now."
            show bree at left with ease
            "And even if I had some kind of explosion in my brain, I wouldn't have a choice either."
            with hpunch
            "Because [bree.name]'s got a hold of my hand, pulling me after her, and her grip's like iron!"
            scene bg bedroom1
            $ game.room = "bedroom1"
            show bree blush
            with hpunch
            "She practically kicks my door open and hurls me through it."
            "I stagger into my room, making it halfway to the bed before I can slow myself down."
            play sound door_slam
            "Then I hear the door slam behind us, and footsteps pounding towards me."
            show bree flirt
            bree.say "What are you waiting for?"
            bree.say "Why aren't you already getting undressed?"
            bree.say "How can you not be as horny as me right now?!?"
            show bree normal at center, zoomAt(1.5, (640, 1040)) with hpunch
            "[bree.name] spins me round to face her, already tugging at my clothes."
            "And the moment I look her in the face, I can see that she's not kidding."
            "There's something in her eyes that looks almost like desperation!"
            mike.say "Okay, [bree.name], okay!"
            mike.say "Let's get things moving..."
            "I start doing the same thing as [bree.name], trying to undress her."
            "But together all we seem to be able to do is get in each other's way."
            "Arms get tangled together and hands start slapping hands."
            "But neither of us is going to stop until we get the job done."
            show bree underwear with dissolve
            "So, little by little, we strip each other down to our underwear."
            "The sight of ever more flesh on show seems to get [bree.name] even more worked up."
            "So much so that she practically tears my shorts off of me!"
            "And I swear she's going to do the same thing with her bra and panties too!"
            "I can't actually tell whether she does that in the end."
            show bree naked with dissolve
            "Because I'm too busy staring at [bree.name]'s naked body."
            show bree flirt
            bree.say "Like what you see?"
            mike.say "Ah..."
            mike.say "Yeah, [bree.name]..."
            mike.say "You bet I do!"
            show bree happy at startle
            "[bree.name] giggles in a way that's impossibly sexy."
            show bree normal
            "And she takes hold of my hand again."
            "This time her grip is firm, but infinitely more gentle."
            hide bree
            show bree naked blush
            "She walks in front of me, leading the way to the bed."
            "Once we're there, [bree.name] glances back over her shoulder."
            bree.say "Why don't you come get a closer look?"
            show bree normal at center, zoomAt(1.5, (640, 1040)) with hpunch
            "As soon as I come closer, [bree.name] grabs me for a third time."
            "She takes full advantage of me being caught off-balance."
            hide bree
            show bree naked blush
            with vpunch
            "And she sends me tumbling onto the mattress."
    return

label bree_fuck_date_foreplay_male:
    if bree.flags.tittyfuck and bree.sub >= 50:
        bree.say "Um, well like, do you want me to do it again?"
        bree.say "Show my appreciation..."
        menu:
            "Yes":
                "[bree.name] slides off of the bed and kneels before me."
                call bree_fuck_date_titfuck from _call_bree_fuck_date_titfuck_1
            "Show your appreciation instead" if hero.sexperience >= 20 and not intro_foreplay:
                mike.say "How about I show you my appreciation..."
                call bree_fuck_date_oral from _call_bree_fuck_date_oral_1
            "No":
                $ bree.love -= 1
    else:
        menu:
            "Give [bree.name] some oral attention" if hero.sexperience >= 30 and not intro_foreplay:
                call bree_fuck_date_oral from _call_bree_fuck_date_oral_2
            "Just fuck her":
                return
    call stop_all_sfx from _call_stop_all_sfx_10

    return _return

label bree_fuck_date_choices_male:
    menu:
        "Anal" if bree.flags.anal >= 2:
            call bree_fuck_date_anal (2) from _call_bree_fuck_date_anal
        "Missionary":
            call bree_fuck_date_missionary (0) from _call_bree_fuck_date_missionary
        "Spoon" if hero.sexperience >= 5:
            call bree_fuck_date_spoon (5) from _call_bree_fuck_date_spoon
        "Doggy" if hero.sexperience >= 10 and bree.sub >= 25:
            if hero.sexperience >= 20 and bree.sub >= 50:
                menu:
                    "Vanilla":
                        call bree_fuck_date_doggy (10) from _call_bree_fuck_date_doggy
                    "Rough":
                        call bree_fuck_date_doggy_rough (20) from _call_bree_fuck_date_doggy_rough
                    "Sneak in Sasha's room" if 'bree_fuck_sasha_bedroom' in DONE and not Room.has_tag(sasha.room, "home"):
                        call bree_fuck_sasha_bedroom_intro (False) from _call_bree_fuck_sasha_bedroom_intro
            elif 'bree_fuck_sasha_bedroom' in DONE and not Room.has_tag(sasha.room, "home"):
                menu:
                    "Vanilla":
                        call bree_fuck_date_doggy (10) from _call_bree_fuck_date_doggy_1
                    "Sneak in Sasha's room" if 'bree_fuck_sasha_bedroom' in DONE and not Room.has_tag(sasha.room, "home"):
                        call bree_fuck_sasha_bedroom_intro (False) from _call_bree_fuck_sasha_bedroom_intro_1
            else:
                call bree_fuck_date_doggy (10) from _call_bree_fuck_date_doggy_2
        "Cowgirl" if hero.sexperience >= 15 and bree.sub >= 15:
            call bree_fuck_date_cowgirl (15) from _call_bree_fuck_date_cowgirl
        "Reverse cowgirl" if hero.sexperience >= 20:
            call bree_fuck_date_reverse_cowgirl (20) from _call_bree_fuck_date_reverse_cowgirl
    call stop_all_sfx from _call_stop_all_sfx_11

    return _return

label bree_sleep_date_fuck(location="hero"):
    if game.hour > 19 or game.hour < 6:
        scene bg bedroom1
        show bree naked
        with fade
        bree.say "[hero.name], can I... Can I spend the night?"
        menu:
            "No":
                mike.say "No, you shouldn't; I have to get up early tomorrow."
                "The sex was beyond incredible."
                "Frowning a little, [bree.name] straightens and collects her clothes in silence."
                bree.say "That's OK, sleep well [hero.name]!"
                "She then grins at me, before leaving."
                $ bree.love -= 3
                call sleep from _call_sleep_19
            "Yes":
                show cuddle bree with fade
                mike.say "Of course you can."
                "I catch a brief moment of joy flash across her face, before she pulls me into a hug, nuzzling into me once again."
                bree.say "Thank you..."
                "I'm not sure why she seems so happy about this, but it looks like I picked the right answer."
                bree.say "Sleep well, [hero.name]."
                if not bree.is_sex_slave:
                    mike.say "You too."
                elif bree.flags.mikeNickname in nickname_daddy:
                    mike.say "You too my cute little girl."
                else:
                    mike.say "You too my cute little slave."
                "We both cuddle in silence, drifting off to sleep in each others arms."
                $ bree.love += 3
                call sleep ("bree") from _call_sleep_20
        $ game.room = "bedroom1"
    return

label bree_fuck_date_oral_intro:
    $ game.play_music("music/roa_music/city_nights.ogg")
    scene bg street
    show bree
    with fade
    "I can tell that there's something on [bree.name]'s mind the whole way home from the date we've just been on."
    "More than once I think that she's going to come right out and say it."
    "But every time she seems to either clam up or start talking about something random instead."
    "I'm pretty sure it's nothing serious, you know -- nothing that I need to be worried about."
    "Still, I'd rather she spit it out than leaving me in the dark."
    "That's one sure way to make a guy get paranoid!"
    scene bg bedroom1
    show bree
    with fade
    "So as soon as we're back home and in my bedroom, I decide to call her out."
    mike.say "Erm, [bree.name]?"
    bree.say "Yeah, [hero.name]?"
    mike.say "Was there something that, you know..."
    mike.say "Something you wanted ask me?"
    mike.say "But maybe you were too shy to say it?"
    show bree flirt blush
    "Almost instantly I see [bree.name]'s cheeks flush a bright shade of red."
    "Which lets me know that I was right on the money."
    "But also that I've just managed to put [bree.name] on the spot too!"
    mike.say "Hey, hey!"
    mike.say "It's okay, [bree.name]."
    mike.say "You can tell me, whatever it is."
    "She nods, the glow on her cheeks fading a little as she does so."
    show bree -blush
    bree.say "Okay, [hero.name]."
    bree.say "But I never asked a guy this before!"
    "Well, now I'm more than a little intrigued."
    "I strain to hear whatever [bree.name] says next."
    if bree.flags.bj:
        bree.say "You know that I like to suck your dick sometimes?"
        "I nod at this, thinking I like where this is going."
        bree.say "Well..."
        bree.say "I think I might like it if you did the same for me..."
    else:
        bree.say "Could....could you fulfill a desire for me?"
        "An eyebrow tweaks up as I consider her body language."
        bree.say "Could you go down on me?"
    "I have to resist the urge to laugh at the tentative nature of the request."
    "It's not like I need much convincing to go down on [bree.name]."
    "But she's being earnest, and I need to be careful not to hurt her feelings."
    "If I make fun of her shyness then I'll probably blow the chance of getting any action at all tonight!"
    mike.say "Sure thing, [bree.name]."
    mike.say "I'd be up for that, no problem."
    show bree happy
    "I can see that my words have had the desired effect."
    "A genuine smile spreads across her face as she perks up."
    "By way of answer, she grabs ahold of my hand and leads me over to the bed."
    "It's odd to think that she can be so forward sometimes and yet so shy at others."
    "But I guess that's just one of those little quirks that makes you fall for a girl."
    show bree naked with dissolve
    "[bree.name] can't help but giggle as we undress in front of each other."
    "And the sight of her obvious excitement means I'm hard as soon as my pants come off."
    "The giggles only intensify as she sees this for herself."
    return

label bree_fuck_date_oral:
    $ game.play_music("music/roa_music/city_nights.ogg")
    scene bg bedroom1
    show bree cunnilingus bree
    with fade
    "[bree.name] clambers onto the bed backwards, beckoning for me to follow her."
    "Which is something that I don't need any serious encouragement to do!"
    "I follow [bree.name] down onto the mattress, lowering myself between her thighs."
    "She watches me all the way down, her eyes full of anticipation."
    "There's nothing for her to worry about, save for my performance."
    "[bree.name]'s as beautiful down here as anywhere else, like a natural work of art."
    "In fact, I don't think I've ever seen such an appetising pussy in my life!"
    show bree cunnilingus notongue
    "I start out slow and gentle, doing no more than kissing the edges of [bree.name]'s folds."
    "But already I can hear her gasping at the sensation."
    "That and the scent of her down here, as she starts to get wet..."
    "It's all that I can do to keep to the original plan."
    "The whole experience makes me want to go crazy!"
    "Using every last ounce of my willpower, I force myself to stay the course."
    show bree cunnilingus down
    pause 0.25
    show bree cunnilingus middle
    pause 0.25
    show bree cunnilingus up
    "Slowly and surely I make my way around her lips, moving inwards a little at a time."
    "Soon enough, my tongue is exploring the delicate skin that leads deeper into her."
    show bree cunnilingus down
    pause 0.25
    show bree cunnilingus middle
    pause 0.25
    show bree cunnilingus up
    menu:
        "Use my tongue":
            "I could get fancy, but I already know that [bree.name]'s pretty nervous about this whole thing."
            "And so I concentrate on building up what I'm doing with my tongue and forget about anything else."
            show bree cunnilingus down
            pause 0.25
            show bree cunnilingus middle
            pause 0.25
            show bree cunnilingus up
            "I keep myself from going in too strong, just dipping the tip of my tongue into her."
            show bree cunnilingus down
            pause 0.2
            show bree cunnilingus middle
            pause 0.2
            show bree cunnilingus up
            "[bree.name] seems to enjoy the teasing nature of this, cooing as well as moaning in response."
            show bree cunnilingus down
            pause 0.2
            show bree cunnilingus middle
            pause 0.2
            show bree cunnilingus up
            "I only begin to use more of my tongue when I'm sure that she's ready for it."
            show bree cunnilingus down blush
            pause 0.2
            show bree cunnilingus middle
            pause 0.2
            show bree cunnilingus up
            "And my patience is rewarded by a steady rise in the volume of [bree.name]'s moans."
            show bree cunnilingus down
            pause 0.2
            show bree cunnilingus middle
            pause 0.2
            show bree cunnilingus up
            "In fact, her entire body responds at the same time, flexing with unrestrained pleasure."
            show bree cunnilingus down
            pause 0.2
            show bree cunnilingus middle
            pause 0.2
            show bree cunnilingus up
            "I'm enjoying the experience myself."
            show bree cunnilingus down
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up at startle(0.05,-10)
            "The intense taste of her on my tongue and the scent of her obscures all else."
            show bree cunnilingus middle
            "But there's something so warm and wonderful about what I'm doing too."
            show bree cunnilingus down pleasure
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up
            "As if the trust that [bree.name]'s showing in letting me do this is almost as important."
            show bree cunnilingus down
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up
            "It makes what I'm doing all the more special and meaningful."
            show bree cunnilingus down
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up
            "And every time she shows her gratitude, I want to please her that much more."
            show bree cunnilingus down
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up at startle(0.05,-10)
            "This all means that I keep right on, stepping up my efforts."
            show bree cunnilingus middle pleasure
            pause 0.15
            show bree cunnilingus down
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus down
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up at startle(0.05,-10)
            "Right until the moment when I hear [bree.name] begin to almost wail above me."
        "Finger her ass" if hero.sexperience >= 30:
            "I know that I should probably keep things simple tonight."
            "But I just can't seem to get enough of [bree.name] to keep me satisfied."
            show bree cunnilingus down
            pause 0.25
            show bree cunnilingus middle
            pause 0.25
            show bree cunnilingus up
            "So the very moment that she shifts her ass in inch, I take a firm hold of it."
            show bree cunnilingus down
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up
            "[bree.name] yelps in surprise, trying to wriggle away."
            show bree cunnilingus down blush
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up
            "But I already have a finger in just the right spot to take advantage of..."
            bree.say "Ooo..."
            bree.say "What are you..."
            show bree cunnilingus down
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up fingerass
            "Before she can even get the words out, it's sinking into her ass."
            show bree cunnilingus down pleasure
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up
            bree.say "Oh...oh my..."
            bree.say "That feels...good!"
            show bree cunnilingus down
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up
            "I take full advantage of how distracted [bree.name] is in that moment."
            show bree cunnilingus down
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up
            "My tongue snakes out and pushes further than ever before into her pussy."
            show bree cunnilingus down
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up at startle(0.05,-10)
            "By now she's quivering from what I'm doing to her."
            show bree cunnilingus down
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up at startle(0.05,-10)
            "And there's nothing that she can do to resist as I do yet more."
            show bree cunnilingus middle pleasure
            pause 0.15
            show bree cunnilingus down
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus down
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up at startle(0.05,-10)
            "[bree.name] begins to almost wail, letting me know that she's reaching her limit..."
        "Use the dildo" if hero.has_item("dildo"):
            "I could keep things simple tonight, which would probably suit [bree.name] down to the ground."
            "But I just can't resist the temptation to slide one hand off of the mattress and under the bed."
            show bree cunnilingus down
            pause 0.25
            show bree cunnilingus middle
            pause 0.25
            show bree cunnilingus up
            "[bree.name] doesn't notice a thing as I grab the dildo that I know is down there."
            show bree cunnilingus down
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up
            "But I make damn sure that she catches sight of it as my hand returns with the thing."
            show bree cunnilingus down blush
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up
            bree.say "Wha..."
            bree.say "What are you..."
            show bree cunnilingus down dildopussy
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up
            "I don't give her time to object as I slide the head against the lips of her pussy."
            "All I hear is her begin to yelp a little as I push it inside of her."
            show bree cunnilingus down vibrate
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up
            "While [bree.name] might have conscious reservations, her body is more than willing."
            show bree cunnilingus down
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up
            "The toy fills her in one smooth motion, meeting almost no resistance at all."
            show bree cunnilingus down blush
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up
            bree.say "Mmm..."
            show bree cunnilingus down
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up
            bree.say "Oh God..."
            show bree cunnilingus down
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up
            bree.say "Yes...yes..."
            show bree cunnilingus down
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up at startle(0.05,-10)
            "As much as she might not have been expecting the toy, I'm still gentle with her."
            show bree cunnilingus down shake
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up at startle(0.05,-10)
            "I work the dildo in and out of [bree.name]'s pussy in a smooth and regular motion."
            show bree cunnilingus down
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up at startle(0.05,-10)
            "All the time I'm still kissing and licking at the edges too."
            show bree cunnilingus down
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up at startle(0.05,-10)
            "Pretty soon she's shaking and moaning, straining to keep from losing control."
            show bree cunnilingus middle pleasure
            pause 0.15
            show bree cunnilingus down
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus down
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up at startle(0.05,-10)
            "It won't be long before she reaches her climax..."
        "Use dildo and my finger." if hero.has_item("dildo") and hero.sexperience >= 30 and bree.sub >= 50:
            "I should just keep right on using my tongue tonight."
            "But I'm already reaching under the bed for what's hidden down there."
            show bree cunnilingus down
            pause 0.25
            show bree cunnilingus middle
            pause 0.25
            show bree cunnilingus up
            "[bree.name]'s too engrossed in my efforts to even notice the move."
            show bree cunnilingus down
            pause 0.2
            show bree cunnilingus middle
            pause 0.2
            show bree cunnilingus up
            "She only spots the thing when it passes by on it's way to her pussy."
            show bree cunnilingus down
            pause 0.2
            show bree cunnilingus middle
            pause 0.2
            show bree cunnilingus up
            bree.say "What..."
            bree.say "What are you doing with that?"
            show bree cunnilingus down
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up
            "Does she actually think I'm going to dignify that with an answer?"
            show bree cunnilingus down
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up
            "Especially with the way she starts to yelp as it strokes her lips?"
            show bree cunnilingus down dildopussy vibrate
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up
            "And even if she isn't convinced, her body is more than willing."
            "The dildo slides into her with only a token of resistance."
            show bree cunnilingus down blush
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up
            bree.say "Ah..."
            show bree cunnilingus down
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up
            bree.say "Oh my god..."
            show bree cunnilingus down shake
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up
            bree.say "Yeah...oh yeah..."
            show bree cunnilingus down shake
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up
            "I smile, knowing that I'm not done yet."
            show bree cunnilingus down shake
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up
            "I'm just waiting for the moment [bree.name] shifts her ass just so..."
            show bree cunnilingus down shake
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up
            "And then I take hold of it with my free hand."
            "[bree.name] wails in surprise, trying to wriggle herself free."
            show bree cunnilingus down shake
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up
            "But my finger's already in just the right position..."
            show bree cunnilingus down fingerass
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up
            bree.say "Oh no..."
            bree.say "Not that as well..."
            "But it's too late, as [bree.name] sinks down onto the finger."
            show bree cunnilingus down pleasure
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up
            "I feel it pulled into her ass by the clenching of muscles."
            show bree cunnilingus down
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up at startle(0.05,-10)
            "Then I have her, trapped between the dildo and my finger."
            show bree cunnilingus middle pleasure
            pause 0.15
            show bree cunnilingus down
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus down
            pause 0.15
            show bree cunnilingus middle
            pause 0.15
            show bree cunnilingus up at startle(0.05,-10)
            "[bree.name] can't move in either direction without feeling one or the other."
            "And it seems like only a matter of seconds until she's on the brink of cumming..."
    show bree cunnilingus down
    pause 0.15
    show bree cunnilingus middle
    pause 0.15
    show bree cunnilingus up at startle(0.05,-10)
    "For a moment, I think that [bree.name]'s actually going to beg for mercy."
    show bree cunnilingus down
    pause 0.15
    show bree cunnilingus middle
    pause 0.15
    show bree cunnilingus up at startle(0.05,-10)
    "That she's about to ask me to stop what I'm doing to her."
    show bree cunnilingus down
    pause 0.15
    show bree cunnilingus middle
    pause 0.15
    show bree cunnilingus up at startle(0.05,-10)
    "And that's exactly when she tips over the edge."
    show bree cunnilingus middle ahegao
    pause 0.15
    show bree cunnilingus down
    pause 0.15
    show bree cunnilingus middle
    pause 0.15
    show bree cunnilingus up
    pause 0.15
    show bree cunnilingus middle
    pause 0.15
    show bree cunnilingus down
    pause 0.15
    show bree cunnilingus middle
    pause 0.15
    show bree cunnilingus up at startle(0.05,-10)
    "Every muscle in her body seems to clench at the exact same second."
    with vpunch
    "It's like she's pulling all of her energy into the very centre of her being."
    with vpunch
    "And then it's all released with the next breath that leaves her body."
    "Those same muscles are suddenly limp as she melts into the afterglow."
    show bree cunnilingus -up -middle -down -notongue -fingerass -dildopussy
    "[bree.name] doesn't seem capable of saying anything to me, just lying there in stunned silence."
    show bree cunnilingus normal
    "She practically glows as she silently enjoys the slowly fading orgasm. Her look of absolute contentment lets me know that I did good."
    "Which is all I needed to know."
    return

label bree_fuck_date_titfuck:
    scene bg black
    show bree titfuck
    show chest_insert bree zorder 1 at zoomAt(1, (40, 200))
    with fade
    "[bree.name] takes me by surprised when she leans forward and presses my cock between her breasts."
    "I would have been blown away (if you pardon the pun) by either a blowjob or just her hands."
    "They're soft and yet firm at the same time, and so warm I can't help biting my lip at the sensation."
    bree.say "H...How does it feel?"
    "[bree.name] looks up at me as she whispers the question."
    "The faint blush across her cheeks has now become a flush that's turned both her cheeks red."
    mike.say "It feels...amazing!"
    "I try to say something romantic and manly, but the words just blurt out of me all the same."
    "She smiles, and I feel that my own nervousness has somehow helped to stamp down hers too."
    hide chest_insert
    show bree titfuck up
    pause 0.45
    show bree titfuck down
    pause 0.45
    show bree titfuck up
    pause 0.45
    show bree titfuck down
    "[bree.name] begins to move her breasts up and down, slowly and steadily."
    "Pinned between them, I feel my cock pulled and pressed in sympathy."
    "I've had this kind of treatment before, but not from a girl that I liked as much as [bree.name]."
    "Which is already making the whole thing feel so much better than the last time I can recall."
    show bree titfuck up
    pause 0.35
    show bree titfuck down
    pause 0.35
    show bree titfuck up
    pause 0.35
    show bree titfuck down
    "By now, she's settled into a steady rhythm that's hard to describe as anything other than divine."
    show bree titfuck up
    pause 0.35
    show bree titfuck down
    pause 0.35
    show bree titfuck up
    pause 0.35
    show bree titfuck down
    "But I can feel her beginning to speed things up a little more as time passes."
    show bree titfuck up
    pause 0.25
    show bree titfuck down
    pause 0.25
    show bree titfuck up
    pause 0.25
    show bree titfuck down
    "All the while, she keeps catching my eye, seeking for my approval of what she's doing."
    show bree titfuck tongueout
    bree.say "Do...do my tits feel good around your c...cock, [hero.name]?"
    "I've never heard this kind of talk coming from [bree.name]'s mouth before this moment."
    "She's trying her best to talk dirty, stumbling over the words in embarrassment."
    show bree titfuck up
    pause 0.25
    show bree titfuck down
    pause 0.25
    show bree titfuck up
    pause 0.25
    show bree titfuck down
    bree.say "Uh...oh, it looks so good to me..."
    "Somehow the fact that she's no good at this makes it all the more endearing to hear."
    bree.say "I...I can't wait for it to go pop in my face..."
    show bree titfuck up
    pause 0.25
    show bree titfuck down
    pause 0.25
    show bree titfuck up
    pause 0.25
    show bree titfuck down
    "I've started moving my cock up and down in the tight cleft of her breasts now."
    show bree titfuck up
    pause 0.15
    show bree titfuck down at startle(0.05,-10)
    pause 0.15
    show bree titfuck up
    pause 0.15
    show bree titfuck down at startle(0.05,-10)
    "Sweat from both our bodies making it move that much faster with little effort."
    mike.say "Fuck, [bree.name] - you're so damn hot..."
    show bree titfuck up
    pause 0.15
    show bree titfuck down at startle(0.05,-10)
    pause 0.15
    show bree titfuck up
    pause 0.15
    show bree titfuck down at startle(0.05,-10)
    "I'm muttering the words, but I guess that she hears them, as I can feel her efforts redouble."
    show bree titfuck up
    pause 0.15
    show bree titfuck down at startle(0.05,-10)
    pause 0.15
    show bree titfuck up
    pause 0.15
    show bree titfuck down at startle(0.05,-10)
    "[bree.name]'s nipples are getting pressed into my stomach with the force that we're rubbing against each other now."
    bree.say "Do...do my tits feel good around your c...cock?"
    bree.say "[hero.name]...will you cum soon?"
    "[bree.name]'s voice is quiet and yet filled with intensity as she asks the question."
    if not bree.flags.tittyfuck:
        mike.say "Yeah...I think I'm on the brink."
        bree.say "I want to make you...make you cum."
        bree.say "I want you to use me, [hero.name] - use me to get off."
        show mouth_insert bree zorder 1 at zoomAt(1, (840, 160))
        show bree titfuck up tongueout
        pause 0.15
        show bree titfuck down at startle(0.05,-10)
        pause 0.15
        show bree titfuck up
        pause 0.15
        show bree titfuck down at startle(0.05,-10)
        bree.say "Come on me...cum for me..."
        bree.say "Please?!?"
        "The look on her face as she literally pleads for me to cum over her is all I need to lose it."
        show bree titfuck up
        pause 0.15
        show bree titfuck down at startle(0.05,-10)
        pause 0.15
        show bree titfuck up
        pause 0.15
        show bree titfuck down cum closed with vpunch
        mike.say "Oh, god - [bree.name]!"
        show mouth_insert bree cum
        with vpunch
        "[bree.name] makes little strangled cries as she's spattered across the face with my cum."
        with vpunch
        "It's hard to tell if they're from surprise, disgust or satisfaction."
        show bree titfuck open facecum tonguecum -cum
        if bree.sub >= 75:
            show bree titfuck swallow -tonguecum
            show mouth_insert bree -cum
            "Before she finally releases my cock from between her breasts, [bree.name] licks the last droplets of cum from the tip of her fingers."
        "I can't keep from almost grabbing her in a bear-hug the moment that she relaxes."
        "I pull [bree.name] under the covers with me, feeling a second burst of energy run through me."
        hide bree
        hide mouth_insert
        call sleep ("bree") from _call_sleep_9
        $ game.room = "bedroom1"
    else:
        menu:
            "Keep going":
                $ bree.sub += 1
                mike.say "Yeah...I think I'm on the brink."
                bree.say "I want to make you...make you cum."
                if bree.is_sex_slave:
                    bree.say "Please use me, [hero.name]."
                show mouth_insert bree zorder 1 at zoomAt(1, (840, 160))
                show bree titfuck up tongueout
                pause 0.15
                show bree titfuck down at startle(0.05,-10)
                pause 0.15
                show bree titfuck up
                pause 0.15
                show bree titfuck down at startle(0.05,-10)
                bree.say "Come on me...cum for me..."
                bree.say "Please?!?"
                "The look on her face as she literally pleads for me to cum over her is all I need to lose it."
                show bree titfuck up
                pause 0.15
                show bree titfuck down at startle(0.05,-10)
                pause 0.15
                show bree titfuck up
                pause 0.15
                show bree titfuck down cum closed with vpunch
                mike.say "Oh, god - [bree.name]!"
                show mouth_insert bree cum
                with vpunch
                "[bree.name] makes little strangled cries as she's spattered across the face with my cum."
                with vpunch
                "It's hard to tell if they're from surprise, disgust or satisfaction."
                show bree titfuck open facecum tonguecum -cum
                if bree.sub >= 75:
                    show bree titfuck swallow -tonguecum
                    show mouth_insert bree -cum
                    "Before she finally releases my cock from between her breasts, [bree.name] licks the last droplets of cum from the tip of her fingers."
                    hide mouth_insert
                if not (hero.energy >= 8 or hero.fitness >= 75):
                    "I can hardly catch my breath once [bree.name]'s wrapped everything up."
                    "It's though she's sucked the last ounce of energy right out of my body."
                    "Along with everything else that comes along with it too!"
                    hide mouth_insert
                    "But I can see from the look in her eyes that she's far from spent."
                    mike.say "Ah, [bree.name]...you've kinda worn me out here!"
                    mike.say "I'm a blink away from passing out and sleeping for a week!"
                    show bree titfuck smile
                    "Instantly I see a flash of disappointment in her eyes, but then she shakes her head and smiles."
                    if not bree.is_sex_slave:
                        bree.say "Huh - I guess I'm just too handy for my own good."
                        bree.say "Maybe I won't try so hard next time!"
                    elif bree.flags.mikeNickname in nickname_daddy:
                        bree.say "Am I a good girl Daddy?"
                        mike.say "You are a good girl [bree.name]."
                    else:
                        bree.say "Did I do good Master?"
                        mike.say "You did real good [bree.name]."
                    hide bree
                    call sleep ("bree") from _call_sleep_3
                    $ game.room = "bedroom1"
                    return
            "Stop her":
                mike.say "No, [bree.name] - I really want to fuck you right now..."
                $ bree.love += 1
    return

label bree_fuck_date_anal(sexperience_min):
    "I can hear panting in my ears right now, but I can't be sure if it's coming from [bree.name], myself or the both of us."
    "Not that it matters, as I turn [bree.name] around to face away from me and guide her down onto the bed, not giving her time to question or object."
    "As she clambers onto the mattress, she's forced to go down on all fours to avoid falling onto her face."
    show bree doggy anal with fade
    "And before she can either sit back up or try to lie down on her belly, I take a firm hold of her around the waist."
    "[bree.name] seems to understand the gesture, and remains obligingly down on all fours as I climb up behind her."
    "She can't know what I'm intending to do to her, and the fleeting glances that she gives me over her shoulder are testament to this."
    "But I'm enjoying her being in the dark, and so am in no mood to offer her any solid clues as to my intentions just yet."
    "Instead I make a point of seizing her buttocks, one in the palm of each hand, and massaging them as though I was kneading dough."
    "[bree.name] moans at the sensation, the movement creating sympathetic twinges from between her thighs."
    "Slowly, I part her buttocks to reveal the crease that they serve to hide from me."
    "And there, glistening like a wondrous prize, is the sight of [bree.name]'s tight little pussy."
    "It's already so wet that I can smell it's scent, almost quivering with anticipation enough for the eye to perceive it."
    "But my goal is just a little way above it, a much more challenging and rare objective."
    "It'd be so easy to just slip inside of [bree.name]'s pussy right now..."
    "And so maybe that's why I choose the more demanding option."
    "And maybe that's why she's so surprised when I do so."
    "I rub my fingers along the sides of [bree.name]'s pussy, collecting a little of the juices flowing so freely there."
    "As she squeals in genuine surprise, I use this to lube up the head of my cock."
    show bree doggy speed
    "A moment later, I spread her buttocks wider still, and then begin to push my way into her ass."
    "Where she squealed before, [bree.name] now lets out a long, low moan as she feels my cock forcing its way inside of her."
    "In contrast to the welcome that her pussy had laid out for me, her ass is as tight as can be."
    "It feels incredible as the muscles squeeze against me, trying in vain to keep my cock from penetrating further."
    "There's nothing but forward motion of short pauses to begin with, as I battle against [bree.name]'s body."
    "She's doing nothing to stop me on a conscious level, but the need to fight for every inch is making me all the more determined."
    show bree doggy ahegao
    "By the time I'm almost balls deep into her, [bree.name]'s clawing at the sheets and tossing her head around like an animal in heat."
    "And then, it's as if her body finally surrenders to the inevitable, and the walls come down all at once."
    "I feel the last shred of resistance drain away, and her muscles accept the inevitable."
    "Like a doe that needed to be conquered by a rutting stag, [bree.name]'s body melts beneath me."
    "And only then do I really start to fuck her ass."
    "Now the thrusts that I begin to push into her with are hitting on already spent, exhausted muscles."
    "This means that [bree.name] feels the full force of my every movement with nothing at all held back."
    "Every second that I'm inside of her makes her legs, stomach and arms shudder with sensation."
    "I can see her breasts shaking in sympathy, her head hanging down in sheer submission."
    "It's as though, by bending her ass to my will, I've unlocked the key to conquering every part of her body afterwards."
    "Right now I can't imagine this hole being meant for anything but taking my cock."
    "And the resigned nodding that [bree.name]'s head has settled into seems to confirm me as being the one in charge."
    show bree doggy cuminass with hpunch
    pause 0.25
    with hpunch
    pause 0.25
    with hpunch
    "By the time that I make one final push into her, spending myself in the effort, I doubt [bree.name] could have objected if she'd tried."
    $ bree.sub += 1
    $ bree.flags.anal += 1
    return

label bree_fuck_date_doggy(sexperience_min):
    hide bree
    show bree doggy
    with fade
    call check_condom_usage (bree) from _call_check_condom_usage_23
    if _return == False:
        return "leave_without_gain"
    "[bree.name] offers no resistance whatsoever as I turn her around and push her gently onto the bed before me."
    "For a moment she goes to lay flat upon her stomach, but I put a hand at the top of each of her thighs and pull her upright once more."
    "She seems to get the message, and raises herself up on her elbows and knees, shuffling the last bit of the way onto the bed."
    "I climb up behind her, noting the look of anticipation on her face as she glances back, over her shoulder."
    "I can see [bree.name]'s breasts, still swaying slightly from the momentum of her movements."
    "I can see her buttocks, standing still and unprotected before me."
    "As I part them to reveal her already glistening pussy, I hear a faint moan of anticipation from her other lips."
    "And that makes me want her all the more."
    if not bree.flags.anal and game.days_played % 4 == 0:
        show bree doggy anal
        "[bree.name] moans more audibly as she feels my cock begin to push its way into her."
        "It's a sensation that I can certainly appreciate, as she's much tighter than I'd anticipated."
        "I try not to be dissuaded by this unexpected discovery, instead redoubling my efforts."
        "[bree.name] actually cries out in response to this, yelping and sighing more with every inch that I make it into her."
        "It's baffling me how I could have just seen her so wet and ready for this, yet find so much resistance."
        "Glancing down to see if I was mistaken, I soon discover the actual source of the problem."
        "I'm not in [bree.name]'s pussy after all, but by now, balls deep in her ass!"
        mike.say "Whoops!"
        "[bree.name] looks back at me over her shoulder, her expression not outraged or angry in any way."
        show bree doggy anal scream
        "In fact, she looks pretty accepting of what I've been doing to her..."
        menu:
            "Pull out, Pull out!":
                show bree doggy dickout -scream
                "I pull out of [bree.name]'s ass as quickly as I can manage, still trying to be as gentle as I can with her."
                "But the sigh of (what I assume is) relief that she lets out while I withdraw makes me wonder if I've misjudged the situation entirely."
                mike.say "Erm...[bree.name]...I'm sorry."
                mike.say "That was kind of an accident..."
                bree.say "Ah...It's okay, [hero.name]...really it is."
                if not bree.is_sex_slave:
                    bree.say "Just warn me the next time you want to go there, okay?"
                "I nod quickly."
                mike.say "Do you still want to..."
                bree.say "If you do too..."
                "With that, she looks away a little, as if inviting me to try again."
            "Keep going":
                show bree doggy anal speed
                "I choose to take the fact that [bree.name]'s not telling me to stop as tacit approval for what I'm doing."
                "Rather than stopping, I begin to thrust into her that much harder and with more force than before."
                "As she's still looking back at me over her shoulder, I can see the instant effect this has upon [bree.name]'s expression."
                "Her eyes seem to lose their focus and her features almost slacken a little in response to the way she's being used."
                "A part of me feels as though, in her acceptance, she's become almost like a passive receptacle for my desires."
                "This impression is only helped by the fact that she makes no sounds that could be taken as words from this point on."
                "Instead, [bree.name] beginning to gasp and almost yelp like a dog."
                "I feel as though with every push into her from my cock, she becomes ever more like a beast that's being mounted."
                show bree doggy ahegao
                "Any issues that I might have had from there being no natural lubrication from [bree.name]'s ass is no longer a problem."
                "Thanks to the sheer amount that we're sweating, she's as wet and slippery down there as her pussy could ever be."
                "I can see her hands grabbing at the bedclothes, gripping onto them as if for dear life."
                "The only sounds that she's making now are coming in the form of low groans, almost turning into growls."
                "I've never seen [bree.name] like this before, as though being fucked up the ass is turning her into a primitive, yowling animal."
                "Part of me is worried that I've gone too far, but the larger part of me is simply too aroused to even think of stopping."
                "And now it's my turn to let out an animalistic cry, as I feel myself cumming."
                call cum_reaction (bree, 'anal', sexperience_min) from _call_cum_reaction_52
                if _return == "anal_inside":
                    if CONDOM:
                        "I can't stop now, and I'm pretty sure that [bree.name] wouldn't want me to either."
                        with hpunch
                        "I push further into her than I ever thought possible, making her squeal like an animal caught in a trap."
                        with hpunch
                        "[bree.name]'s limbs begin to shake, and then they go limp as she collapses onto the bed."
                        show bree doggy anal cuminass with hpunch
                        "Even after I've climaxed whilst do deep inside of her ass, [bree.name] doesn't stir from where she fell."
                        "All I can do is pull myself gingerly out of her and take care of the condom still clinging to my cock."
                    else:
                        "I didn't think that I could possibly push any further inside of [bree.name] than I already had."
                        with hpunch
                        "But as I cum, I thrust with such determination that she almost screams from the sensation."
                        with hpunch
                        "A moment later, her arms and legs collapse beneath her, and [bree.name]'s head slumps onto the pillows."
                        show bree doggy anal cuminass with hpunch
                        "Even once it's over, [bree.name] doesn't snap out of her stupor."
                        "Instead, she only manages to turn her head a little, so that she can stare at me out of the corner of her eye."
                        "Her expression is still that of a stunned animal, not fully conscious of what just happened or why."
                elif _return == "anal_outside":
                    "I managed to pull my cock out of [bree.name]'s ass the second before I cum."
                    "Suddenly left a gaping void, I see her shudder as her backside finally relaxes."
                    show bree doggy -anal cumshot with vpunch
                    pause 0.25
                    with vpunch
                    "Her buttocks quiver as I splatter them with a shower of white."
                    show bree doggy cumonass -cumshot with vpunch
                    "[bree.name] seems to shiver bodily more with each drop that lands upon her naked, exposed skin."
                hide bree with fade
                "To me, it feels like what we just did was amazing, and I fall back onto the bed in a state of satisfied triumph."
                show bree naked blush with dissolve
                "But the moment that [bree.name] regains her senses, she darts off of the bed."
                "She hurriedly gathers up her clothes, not even bothering to dress, her face bright red as she does so."
                hide bree with moveoutright
                play sound door_slam
                "Then she almost runs out of the room, and I hear her cross the hallway, slamming her own bedroom door behind her."
                "I begin to wonder if I really messed up back there."
                "Or maybe [bree.name]'s just embarrassed at being taken up the ass without warning?"
                "Either way, it's not how I'd have wanted things to work out."
                $ bree.flags.anal = 1
                return "leave_with_gain"
    show bree doggy vaginal with fade
    "I don't make straight for [bree.name]'s pussy with my cock, instead allowing it to rub against the folds and lips for a little while."
    "My reward is to feel her shudder in anticipation and let out a series of little moans as she's teased with the promise of what's still to come."
    "By this time, [bree.name] is literally wet and almost leaking onto me."
    "And so when I finally adjust my hips just so, I slide into her as smoothly as if she was greased slick."
    "I go slowly, knowing just how much she's wanting this, and hoping to make her savour the feeling as much as possible."
    "[bree.name] tosses her head more with every inch that I push into her, almost reacting to my movements before I can make them."
    "Indeed, she begins to try to push herself backwards, wanting to have more than I'll allow her."
    "But I take a firm hold of her buttocks, using my arms to arrest her progress."
    "[bree.name] struggles and whines at this, like a dog denied a treat by its master."
    "And so I'm forced to reward her by pushing the last few inches into her, until I can go no deeper."
    "She writhes as I do this, lowering herself to the mattress so that my angle of entry is as acute as possible."
    "At the same time, [bree.name] grabs handfuls of the bedclothes, almost tearing at them in her passion."
    "I'm going as fast as I can by this point, the sound of my thighs slapping against her buttocks a sharp crack."
    "[bree.name] buries her face in the pillows, but I can still hear her moans and cries, muffled as they are."
    "I can't keep this up much longer - something's got to give!"
    call cum_reaction (bree, 'vaginal', sexperience_min, 150) from _call_cum_reaction_53
    if _return == "vaginal_condom":
        with hpunch
        "This is it, I let go of myself and cum without restraint."
        show bree doggy vaginal condom with hpunch
        "[bree.name] bucks beneath me, my own orgasm seeming to push her over the brink herself."
        with hpunch
        "Even though I'm absolutely spent, I use the last of my energy to make sure she feels all of it that I can manage."
        "In the end, I don't so much pull out of [bree.name] as slide out as I collapse onto the bed."
        show bree naked blush
        "A moment later, I feel her snuggling against me, pushing her way into my arms."
        bree.say "Oh, thank you, [hero.name] - that was perfect!"
        "I don't think she's ever looked as beautiful to me as she does right now."
        "She fits into the crook of my body so well that I don't even need to move an inch."
    elif _return == "vaginal_outside":
        if bree.is_visibly_pregnant:
            "As much as I'd like to finish inside her, a part of me gets off on seeing my cum on her skin."
            show bree doggy -vaginal cumshot with hpunch
            "I hear [bree.name] give a small sigh as I pull out, but it's replaced with a sharp intake of breath through her teeth as my hot cum hits her skin."
            with hpunch
            "It spatters down on the small of her back, running down her spine and between her buttocks."
            show bree doggy -cumshot cumonass with hpunch
            "She looks at me with an embarrassed expression on her face."
            scene expression f"bg {game.room}"
            show bree naked blush
            bree.say "Wow...that was crazy!"
            bree.say "I honestly thought you were going to cum in me for a moment back there!"
            "I chuckle softly, still breathing a little heavily from my exertions."
            mike.say "I know...it was touch and go for a while!"
            "My compliment does nothing to keep her from blushing all the more."
            $ bree.sub += 1
            "[bree.name] doesn't say anything more, but she wraps her arms around me in an embrace that's worth a thousand words."
        else:
            "I manage to keep my head and pull out just before it's too late."
            show bree doggy -vaginal cumshot with hpunch
            "I hear [bree.name] sigh in unconscious disappointment, but I know she'd have been rather more irate to feel me cumming inside of her."
            with hpunch
            "The consequence of my conscientiousness is that she almost instantly gets showered with all that I have to give."
            show bree doggy -cumshot cumonass with hpunch
            "It spatters down on the small of her back, running down her spine and between her buttocks."
            "She looks at me with an embarrassed expression on her face."
            scene expression f"bg {game.room}"
            show bree naked blush
            bree.say "Wow...that was crazy!"
            bree.say "I honestly thought you were going to cum in me for a moment back there!"
            "I shake my head, still breathing a little heavily from my exertions."
            mike.say "I know...it was touch and go for a while!"
            mike.say "You get me so worked up with passion, [bree.name] - I think we need to use a condom in future!"
            "My compliment does nothing to keep her from blushing all the more."
            "[bree.name] doesn't say anything more, but she wraps her arms around me in an embrace that's worth a thousand words."
    elif _return == "vaginal_inside_pill":
        $ bree.sub += 1
        "I'm too far gone to even think about pulling out of [bree.name] by now, and so I press on regardless."
        with hpunch
        pause 0.25
        with hpunch
        "As I cum into her, I press down with all of my weight, making sure that she stays put until I'm utterly spent."
        show bree doggy vaginal cuminpussy with hpunch
        "I can hear [bree.name] whimpering and moaning at the feelings of ecstasy she's experiencing and the knowledge of what I've done to her."
        "But I'm too exhausted to either feel triumphant or else let the implications of it all sink in."
        "So I lie down on the bed and leave [bree.name] to deal with it on her own for a while."
        scene expression f"bg {game.room}"
        show bree naked blush
        $ bree.love += 1
        "[bree.name] looks around at me eagerly, even as my cum is starting to drip out and run down the inside of her thighs."
        bree.say "Mmm...I feel so good when you fill me up to the brim [hero.name]!"
        bree.say "All warm and melty inside, like you've turned my pussy into a jar of warm honey..."
        "I can't help laying myself atop her as she says this, covering her body with mine."
        mike.say "I promise that next time, I'll lick that pot clean!"
        show bree happy
        "[bree.name] laughs as we collapse onto the bed together in a tangle of sweaty limbs."
    elif _return == "vaginal_inside_pregnant":
        $ bree.sub += 1
        "I'm too far gone to even think about pulling out of [bree.name] by now, and so I press on regardless."
        "She must realise what's going on, as I feel her begin to wriggle almost desperately."
        "But she's given up too much of her leverage in lowering herself down to allow me further in, and she can't hope to free herself in time."
        with hpunch
        pause 0.25
        with hpunch
        "As I cum into her, I press down with all of my weight, making sure that she stays put until I'm utterly spent."
        show bree doggy vaginal cuminpussy with hpunch
        "I can hear [bree.name] whimpering and moaning at the feelings of ecstasy she's experiencing and the knowledge of what I've done to her."
        "But I'm too exhausted to either feel triumphant or else let the implications of it all sink in."
        "So I lie down on the bed and leave [bree.name] to deal with it on her own for a while."
        scene expression f"bg {game.room}"
        show bree naked blush
        $ bree.love += 1
        "[bree.name] looks around at me eagerly, even as my cum is starting to drip out and run down the inside of her thighs."
        bree.say "Mmm...I feel so good when you fill me up to the brim [hero.name]!"
        bree.say "All warm and melty inside, like you've turned my pussy into a jar of warm honey..."
        "I can't help laying myself atop her as she says this, covering her body with mine."
        mike.say "I promise that next time, I'll lick that pot clean!"
        show bree happy
        "[bree.name] laughs as we collapse onto the bed together in a tangle of sweaty limbs."
    elif _return == "vaginal_inside_mad":
        "I'm too far gone to even think about pulling out of [bree.name] by now, and so I press on regardless."
        "She must realise what's going on, as I feel her begin to wriggle almost desperately."
        "But she's given up too much of her leverage in lowering herself down to allow me further in, and she can't hope to free herself in time."
        with hpunch
        pause 0.5
        with hpunch
        "As I cum into her, I press down with all of my weight, making sure that she stays put until I'm utterly spent."
        show bree doggy vaginal cuminpussy
        "I can hear [bree.name] whimpering and moaning at the feelings of ecstasy she's experiencing and the knowledge of what I've done to her."
        $ bree.impregnate()
        $ bree.sub += 1
        "But I'm too exhausted to either feel triumphant or else let the implications of it all sink in."
        "So I lie down on the bed and leave [bree.name] to deal with it on her own for a while."
        scene expression f"bg {game.room}"
        show bree naked blush
        bree.say "[hero.name]...you're gonna..."
        "But it's way too late for that now, and I feel myself letting go inside of her."
        "I expected [bree.name] to freak out and instantly try to clamber out from under me, at least chew me out verbally."
        "So when she stays perfectly still and allows me to thrust my last into her, I'm more than a little puzzled."
        "Afterwards, she gasps as I pull out, a strange look of fear and...what looks like excitement, in her eyes."
        mike.say "[bree.name], I'm sorry - I..."
        "She holds a hand up and shakes her head, silencing me."
        bree.say "Don't say it..."
        bree.say "Just please, use a condom next time...okay?"
        "I nod hastily, already seizing upon the mention of the next time as a possible sign."
        "Hopefully I've not marked my card with her permanently here."
        $ bree.love -= 20
    elif _return == "vaginal_inside_happy":
        "I'm too far gone to even think about pulling out of [bree.name] by now, and so I press on regardless."
        "She must realise what's going on, as I feel her begin to wriggle almost desperately."
        "But she's given up too much of her leverage in lowering herself down to allow me further in, and she can't hope to free herself in time."
        with hpunch
        pause 0.25
        with hpunch
        "As I cum into her, I press down with all of my weight, making sure that she stays put until I'm utterly spent."
        show bree doggy vaginal cuminpussy with hpunch
        "I can hear [bree.name] whimpering and moaning at the feelings of ecstasy she's experiencing and the knowledge of what I've done to her."
        $ bree.impregnate()
        $ bree.sub += 1
        "But I'm too exhausted to either feel triumphant or else let the implications of it all sink in."
        "So I lie down on the bed and leave [bree.name] to deal with it on her own for a while."
        scene expression f"bg {game.room}"
        show bree naked blush
        $ bree.love += 1
        "[bree.name] looks around at me eagerly, even as my cum is starting to drip out and run down the inside of her thighs."
        bree.say "Mmm...I feel so good when you fill me up to the brim [hero.name]!"
        bree.say "All warm and melty inside, like you've turned my pussy into a jar of warm honey..."
        "I can't help laying myself atop her as she says this, covering her body with mine."
        mike.say "I promise that next time, I'll lick that pot clean!"
        show bree happy
        "[bree.name] laughs as we collapse onto the bed together in a tangle of sweaty limbs."
    return

label bree_fuck_date_doggy_rough(sexperience_min):
    hide bree
    show bree doggy noone
    with fade
    "[bree.name] offers no resistance whatsoever as I turn her around and push her gently onto the bed before me."
    "Then she beckons me over with one finger, her eyes full of unspoken promises."
    "Needless to say I hurry straight over there."
    show bree doggy -noone
    "I clamber up onto the bed behind her, my cock hard and swinging before me."
    mike.say "Okay, [bree.name]..."
    mike.say "Here I come!"
    "Before I can go any further, [bree.name] looks back over her shoulder."
    "And she catches my eye with a pretty serious look on her face."
    bree.say "Oh, [hero.name]..."
    bree.say "I want you to be a little...firm with me, yeah?"
    bree.say "You know what I mean?"
    "[bree.name] winks to underline the point."
    "And I nod, letting her know that I understand."
    "Or at least I hope that I do!"
    menu:
        "Fuck her pussy":
            "I make a grab at [bree.name]'s ass."
            "Well, it's really more like a slap from the sound it makes."
            "And I take it that she likes where this is going."
            "As she lets out a cry of surprise and then a filthy giggle."
            "But a moment later, [bree.name] seems to remember something important."
            bree.say "Aren't you forgetting something?"
            call check_condom_usage (bree) from _call_check_condom_usage_24
            if _return == False:
                return "leave_without_gain"
            show bree rough doggy
            if CONDOM:
                show bree rough doggy condom
            with fade
            "The first thing that springs to mind is the fact that [bree.name] wanted me to be firm."
            "You know, like she wanted me to take charge from the beginning."
            "And with that in mind, I reach out and take hold of her hair."
            "Wrapping my fingers into the long, blonde locks, I clench them into a fist."
            "And then I pull backwards, not brutally, but enough to let [bree.name] feel it."
            "She lets out a gasp of genuine surprise, but there's no sound of pain in there."
            "In fact, the first thing I see is that she's nodding eagerly."
            "Or at least as much as my hold on her hair will allow."
            show bree rough doggy pleasure
            bree.say "Oh yeah..."
            bree.say "That's what I'm talking about!"
            "Her voice is quivering with anticipation as she waits to see what I do next."
            "And I can feel a matching thrill starting to course through me too!"
            mike.say "Oh yeah?"
            mike.say "You like that, [bree.name]?"
            mike.say "You like the idea of me fucking you like this?"
            "I hear [bree.name] whimper as I speak to her with an air of authority."
            "And I can see that she's shuffling her ass backwards the whole time too!"
            bree.say "Yes..."
            bree.say "Yes please!"
            bree.say "Please, [hero.name], please fuck me!"
            show bree rough doggy happy vaginal
            "With one smooth movement and totally without warning, I thrust myself forwards."
            "At this range, there's no way I can miss."
            "And I don't need to feel my cock sinking into [bree.name] to know that I've hit it."
            "She squeals as it pushes between the lips of her pussy."
            show bree rough doggy pleasure
            "Then the sound turns into a moan as I begin to go ever deeper."
            "All the time I'm still holding onto [bree.name]'s hair."
            "And giving it an experimental tug has an instant effect."
            show bree rough doggy blush
            "[bree.name] makes a sound like a whinnying horse."
            "And she scoots backwards, desperately pushing her ass against me."
            "I can't help smiling at the sensation of her doing that."
            "But I promise myself that I won't abuse the power it gives me over her."
            show bree rough doggy boobs
            "What follows is an amazing experience for the both of us."
            "I keep on making sparing use of my grip on [bree.name]'s hair to control her."
            "Making sure that things go at a pace which suits me."
            "And at the same time I also make sure to satisfy her desires too."
            "Pretty soon, [bree.name]'s panting and moaning with every move I make."
            "And I know that I can't keep on going too long either."
            "Because it feels like I'm going to cum any moment!"
            call cum_reaction (bree, 'vaginal', sexperience_min, 150) from _call_cum_reaction_54
            if _return == "vaginal_condom":
                "I make sure to keep a hold on [bree.name] as I reach my climax."
                "Because I have no idea if she even knows it's coming."
                with hpunch
                "And when it does, I'm thankful that I did!"
                show bree rough doggy ahegao cum -boobs with hpunch
                "[bree.name] starts to cum almost a second after I do."
                with hpunch
                "And she keeps on going even after I'm done."
                "So I keep her supported the whole time, then guide her down onto the bed."
            elif _return == "vaginal_outside":
                show bree rough doggy -vaginal -boobs
                "I make sure to pull out of [bree.name] before I reach my climax."
                "Because I have no idea if she even knows it's coming."
                with hpunch
                "And when it does, I'm thankful that I did!"
                show bree rough doggy ahegao cum cumshot with hpunch
                $ bree.love += 1
                "[bree.name] starts to cum almost a second after I pull out of her."
                with hpunch
                "And she keeps on going even after I'm done."
                show bree rough doggy onbody -cumshot
                "So I keep her supported the whole time, then guide her down onto the bed."
            elif _return == "vaginal_inside_pill":
                bree.say "Please..."
                bree.say "Cum...in...me..."
                bree.say "I'm on...the pill!"
                "I silently thank [bree.name] for the permission to keep on going."
                show bree rough doggy ahegao cum -boobs with hpunch
                $ bree.love += 2
                "And within mere seconds I'm shooting my load into her."
                with hpunch
                "[bree.name] starts to cum almost a second after I do."
                with hpunch
                "And she keeps on going even after I'm done."
                "So I keep her supported the whole time, then guide her down onto the bed."
            elif _return == "vaginal_inside_pregnant":
                bree.say "Please..."
                bree.say "Cum...in...me..."
                bree.say "I'm already...pregnant!"
                "I silently thank [bree.name] for the permission to keep on going."
                show bree rough doggy ahegao cum -boobs with hpunch
                $ bree.love += 3
                "And within mere seconds I'm shooting my load into her."
                with hpunch
                "[bree.name] starts to cum almost a second after I do."
                with hpunch
                "And she keeps on going even after I'm done."
                "So I keep her supported the whole time, then guide her down onto the bed."
            elif _return == "vaginal_inside_happy":
                "I remember that I need to pull out of [bree.name] before I reach my climax."
                "Because I have no idea if she even knows it's coming."
                "But the moment I do, [bree.name] pushes against me with all her strength."
                bree.say "No!"
                bree.say "Don't stop!"
                "[bree.name] takes me totally by surprise, making me forget what's happening."
                "And those few seconds are all it takes for disaster to strike."
                show bree rough doggy ahegao cum -boobs with hpunch
                $ bree.love += 5
                $ bree.impregnate()
                "Within mere seconds I'm shooting my load into her."
                with hpunch
                "[bree.name] starts to cum almost a second after I do."
                with hpunch
                "And she keeps on going even after I'm done."
                show bree rough doggy pleasure -vaginal
                "My mind already racing with worry over what we just did."
            elif _return == "vaginal_inside_mad":
                bree.say "No!"
                bree.say "Stop!"
                "[bree.name] takes me totally by surprise, making me forget what's happening."
                "And those few seconds are all it takes for disaster to strike."
                show bree rough doggy ahegao cum -boobs with hpunch
                $ bree.love -= 5
                $ bree.impregnate()
                "Within mere seconds I'm shooting my load into her."
                with hpunch
                "[bree.name] starts to cum almost a second after I do."
                with hpunch
                "And she keeps on going even after I'm done."
                show bree rough doggy pleasure -vaginal
                "My mind already racing with worry over what we just did."
        "Fuck her ass" if bree.flags.anal >= 2 and hero.sexperience >= (sexperience_min + 5):
            "I make a grab at [bree.name]'s ass."
            "Well, it's really more like a slap from the sound it makes."
            "And I take it that she likes where this is going."
            "As she lets out a cry of surprise and then a filthy giggle."
            "The first thing that springs to mind is the fact that [bree.name] wanted me to be firm."
            "You know, like she wanted me to take charge from the beginning."
            show bree rough doggy with fade
            "And with that in mind, I reach out and take hold of her hair."
            "Wrapping my fingers into the long, blonde locks, I clench them into a fist."
            "And then I pull backwards, not brutally, but enough to let [bree.name] feel it."
            "She lets out a gasp of genuine surprise, but there's no sound of pain in there."
            "In fact, the first thing I see is that she's nodding eagerly."
            "Or at least as much as my hold on her hair will allow."
            show bree rough doggy pleasure
            bree.say "Oh yeah..."
            bree.say "That's what I'm talking about!"
            "Her voice is quivering with anticipation as she waits to see what I do next."
            "And I can feel a matching thrill starting to course through me too!"
            mike.say "Oh yeah?"
            mike.say "You like that, [bree.name]?"
            mike.say "You like the idea of me fucking you like this?"
            "I hear [bree.name] whimper as I speak to her with an air of authority."
            "And I can see that she's shuffling her ass backwards the whole time too!"
            bree.say "Yes..."
            bree.say "Yes please!"
            bree.say "Please, [hero.name], please fuck me!"
            show bree rough doggy happy vaginal
            "With one smooth movement and totally without warning, I thrust myself forwards."
            "At this range, there's no way I can miss."
            "A little higher than she's expecting, not actually aiming for her pussy..."
            "And I don't need to feel my cock sinking into [bree.name] to know that I've hit it."
            "She squeals as it pushes into her ass."
            show bree rough doggy pleasure
            "Then the sound turns into a moan as I begin to go ever deeper."
            "All the time I'm still holding onto [bree.name]'s hair."
            "And giving it an experimental tug has an instant effect."
            show bree rough doggy blush
            "[bree.name] makes a sound like a whinnying horse."
            "And she scoots backwards, desperately pushing her ass against me."
            "I can't help smiling at the sensation of her doing that."
            "But I promise myself that I won't abuse the power it gives me over her."
            show bree rough doggy boobs
            "What follows is an amazing experience for the both of us."
            "I keep on making sparing use of my grip on [bree.name]'s hair to control her."
            "Making sure that things go at a pace which suits me."
            "And at the same time I also make sure to satisfy her desires too."
            "Pretty soon, [bree.name]'s panting and moaning with every move I make."
            "And I know that I can't keep on going too long either."
            "Because it feels like I'm going to cum any moment!"
            call cum_reaction (bree, 'anal', sexperience_min) from _call_cum_reaction_55
            if _return == 'anal_inside':
                "I make sure to keep a hold on [bree.name] as I reach my climax."
                "Because I have no idea if she even knows it's coming."
                with hpunch
                "And when it does, I'm thankful that I did!"
                show bree rough doggy ahegao cum -boobs with hpunch
                $ bree.sub += 2
                "[bree.name] starts to cum almost a second after I do."
                with hpunch
                "And she keeps on going even after I'm done."
                "So I keep her supported the whole time, then guide her down onto the bed."
            elif _return == 'anal_outside':
                show bree rough doggy -vaginal -boobs
                "I make sure to pull out of [bree.name] before I reach my climax."
                "Because I have no idea if she even knows it's coming."
                with hpunch
                "And when it does, I'm thankful that I did!"
                show bree rough doggy ahegao cum cumshot with hpunch
                $ bree.sub += 2
                "[bree.name] starts to cum almost a second after I pull out of her."
                with hpunch
                "And she keeps on going even after I'm done."
                show bree rough doggy onbody -cumshot
                "So I keep her supported the whole time, then guide her down onto the bed."
            $ bree.flags.anal += 1
    "Afterwards, [bree.name] lies in a heap on the bed, trying to catch her breath."
    return

label bree_fuck_date_cowgirl(sexperience_min):
    bree.say "[hero.name]..."
    bree.say "Did you ever see those rodeo rides they have in some bars?"
    "I frown at the random nature of the question, unsure of where this is going."
    "But I nod all the same as I know what she's talking about."
    mike.say "Ah...you mean a mechanical bull, right?"
    bree.say "Yeah, that's it."
    mike.say "What about it, [bree.name]?"
    bree.say "Well..."
    bree.say "I always wondered what it'd be like to ride on one."
    mike.say "Okay, [bree.name]."
    mike.say "But you do realise I don't have one sitting around the house?"
    bree.say "Of course I do!"
    bree.say "But...I wondered if..."
    bree.say "Maybe I could ride you like one tonight?"
    "[bree.name] wants to try going cowgirl?"
    "What's not to like about that?!?"
    mike.say "Sure thing, [bree.name]."
    mike.say "I might not be able to buck like a mechanical bull."
    mike.say "But I'll give you a ride you'll never forget!"
    "[bree.name] giggles again, but this time she blushes at the same time."
    "And I can hear her excitement in every sound she makes."
    hide bree
    show bree cowgirl
    with fade
    "[bree.name] backs up enough for me to hop onto the bed and lie down on my back."
    "I'm already more than a little aroused at the mere sight of her."
    "And the promise of what's still to come means that I'm hard mere moments later."
    show bree cowgirl out
    "As [bree.name] stares at my cock in anticipation, I can't resist the urge to ham it up."
    mike.say "My lady, your steed awaits!"
    bree.say "Ooh, it's so big!"
    bree.say "Promise you'll break me in gently?!?"
    "[bree.name] takes my hands as she says this, swinging herself over my thighs."
    "The view is incredible as she looks down on me from above."
    "Her thighs and belly, the sight of her face between her breasts."
    "For a moment I almost forget what I've promised to do for her."
    "All I'm able to do is gaze up at [bree.name], lost in just how hot she actually is."
    "It's only when she reaches between my thighs and caresses my cock that I snap out of it."
    "I respond by taking hold of her waist and guiding her downwards."
    "[bree.name] smiles in anticipation as she comes ever closer to getting what she wants."
    menu:
        "Fuck her ass" if bree.flags.anal >= 2 and hero.sexperience >= (sexperience_min + 5):
            "I know that [bree.name] went out on a limb in asking me to do things this way."
            "And yes, I know that she's probably feeling nervous deep down."
            "But that doesn't mean we can't have some fun by mixing things up just a little."
            "Which is why I move [bree.name] forwards just before she sits on me."
            "It's a subtle change of position, but enough to make sure my cock misses her pussy."
            "Instead it slips neatly between her buttocks, pressing against her ass."
            bree.say "Oops..."
            bree.say "I think you missed..."
            show bree cowgirl anal up pleasure blush
            "I pull [bree.name] downwards the same moment that she begins to speak."
            "This means that her own weight is what makes her sink down onto my cock."
            bree.say "Oh..."
            bree.say "Oooh..."
            "I see [bree.name]'s eyes go wide as she feels me entering her."
            "And it seems that she might protest at what I'm doing."
            "For a moment I fully expect her to protest or try to wriggle off of me."
            show bree cowgirl down
            "But then the expression on her face seems to change to one of unexpected pleasure."
            "All at once, [bree.name] melts to the sensations that she's feeling."
            "And then she gives in to the whole thing, sinking all the way down onto me."
            show bree cowgirl smile
            bree.say "Mmm..."
            bree.say "That's SO good!"
            "Encouraged by [bree.name]'s words, I begin to move inside of her."
            "I make sure to go slowly at first, letting her get used to the feeling."
            "But soon enough the muscles of her ass surrender to the experience."
            show bree cowgirl pleasure
            "This means that I can pick up speed, making her start to move atop me."
            "Soon enough [bree.name]'s literally riding me, bouncing up and down as I push into her."
            "The feeling of her ass as it twitches and grabs at my cock is something else."
            "And I can't take my eyes off of her as she takes all I have to give."
            "Maybe she's not bucking and clinging on for dear life right now."
            "But [bree.name]'s body is moving in sympathy to what I'm making her feel."
            show bree cowgirl ahegao
            "She throws her head this way and that, tossing her hair as she does so."
            "And her breasts jiggle to and fro, threatening to hypnotise me the whole time!"
            "It's not all they're doing either, as I can feel them having another effect on me."
            "Or maybe that's thanks to [bree.name]'s muscles clenching around my cock."
            "Either way, I can already feel myself starting to cum!"
            call cum_reaction (bree, 'anal', sexperience_min) from _call_cum_reaction_56
            if _return == "anal_inside":
                "I'm so deep inside of [bree.name] by now that I don't know if I could actually get out in time."
                "And so I just keep right on going, thrusting until the very last moment possible."
                "Which means that when I lose it, my cock is deep inside of her ass."
                "I feel her muscles tighten like fist around me, making sure I can't pull out."
                show bree cowgirl creampie up with vpunch
                $ bree.sub += 2
                "I shoot my entire load a second later, and [bree.name] rides me every second that it lasts."
                with vpunch
                "She sighs and moans, massaging her breasts while I cum."
                show bree cowgirl down resting dickcum cum onass with vpunch
                "And then she collapses atop me, utterly spent and exhausted."
            elif _return == "anal_outside":
                show bree cowgirl out
                show chest_insert bree zorder 1 at zoomAt(1, (840, 120))
                show belly_insert bree zorder 2 at zoomAt(1, (40, 300))
                "It takes all of the strength that I have left, but I manage to pull out of [bree.name]'s ass."
                "The act takes her completely by surprise, meaning that she leans forwards as I do so."
                show bree cowgirl cumshot with vpunch
                $ bree.sub += 1
                "And so she puts herself in just the right position to catch a face-full."
                show chest_insert bree cum
                show belly_insert bree cum
                show bree cowgirl cum onbody
                with vpunch
                "What doesn't hit [bree.name]'s startled face spatters over her breasts and runs down her stomach."
                with vpunch
                "She gasps the whole time that this is going on, eyes and mouth open in surprise."
                show bree cowgirl resting dickcum
                "But it's impossible to tell if the panting is on account of shock or exhaustion!"
                hide chest_insert
                hide belly_insert
            $ bree.flags.anal += 1
        "Fuck her pussy":
            "I'm sure [bree.name]'s eager to get down to it, the look on her face tells me as much."
            "And I know that I'm feeling the same way too!"
            "Which means the moment I pull her towards me I feel a thrill."
            "All it takes is for the tip of my cock to brush against [bree.name]'s lips."
            "Just that and I know that we're both ready to go!"
            call check_condom_usage (bree) from _call_check_condom_usage_25
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show bree cowgirl condom
            "By now my cock is practically begging for me to put it inside of [bree.name]."
            "And I can tell from the feeling of her atop me that her pussy wants it badly too!"
            "Wasting no more time, I thrust my groin upwards and pull [bree.name] down in one move."
            show bree cowgirl vaginal pleasure blush
            "All of my suspicions are proven right as she sinks straight onto my cock."
            "There's no more than a heartbeat of resistance before she lets me in."
            "And then she slides all the way down the shaft of my cock in one smooth motion."
            bree.say "Mmm..."
            bree.say "Ah, shit..."
            bree.say "That's it - right there..."
            "I let [bree.name] sit there for a couple of seconds, allowing the sensations to build in her."
            "Then I begin to move in and out of her, slowly at first, but always gaining speed."
            "[bree.name] has to put her hands flat on my chest, steadying herself to take what I'm giving her."
            "But it doesn't take long for her to get into the swing of things."
            "And before I know it, she goes from passively taking it to actually riding my cock."
            "[bree.name]'s hands leave my chest and begin to explore her own body."
            "As I look up from her, she caresses her thighs and then her belly."
            "All the time she's moving atop me like someone riding a spirited horse."
            "Her hands soon make their way upwards and reach her breasts."
            "Trust me, it's not as if the sight of them bouncing in sympathy wasn't enough."
            "But now she's squeezing and squashing them like her life depends on it!"
            "I watch as [bree.name] presses her tits together, like she's trying to knead dough."
            "She's pinching and pulling her nipples too."
            "And it's as if she thinks it'll let off the pressure building inside of her."
            "There's no doubt that I feel like I'm being ridden hard now."
            show bree cowgirl ahegao
            "I'm thrusting and bucking beneath [bree.name], just like a mechanical bull."
            "I don't know if I'm more turned on by the idea of [bree.name] riding me like this."
            "Or else it's her performance atop me that's really turned me onto the experience."
            "But whichever the reason is, I just keep on getting wilder with my thrusts."
            "[bree.name] really does look like she's fighting to stay on top of me by now."
            "She's gasping and sweating as I push myself all the way into her."
            "It's only now that I realise the other sound I can hear is me gasping too!"
            "I'm going to cum, I know it."
            "There's no stopping it now!"
            call cum_reaction (bree, 'vaginal', sexperience_min, 175) from _call_cum_reaction_57
            if _return == "vaginal_condom":
                "And thanks to the fact that we took precautions, there's no need to stop at all."
                "I just keep right on going, letting [bree.name] ride me until the very moment I shoot my load."
                with vpunch
                "Even after all the time she's spent working herself into a frenzy, I can still see it hit her."
                with vpunch
                "[bree.name]'s eyes open wide, almost like they're going to pop out of their sockets."
                with vpunch
                "And she pushes herself down onto me one last time, milking it for every last sensation."
                $ bree.love += 1
                "Then she collapses onto me, utterly spent and panting for breath."
            elif _return == "vaginal_outside":
                show chest_insert bree zorder 1 at zoomAt(1, (840, 120))
                show belly_insert bree zorder 2 at zoomAt(1, (40, 300))
                "I have no idea just how I manage to pull off move before I lose it."
                "But just as [bree.name]'s going up, I reverse the motion of my groin."
                show bree cowgirl out
                "My cock slips out of her without a fraction of an inch to spare."
                if not CONDOM:
                    show bree cowgirl cumshot with vpunch
                    $ bree.sub += 1
                    "And I shoot my load as she's coming back down again."
                    show bree cowgirl -cumshot cum onbody with vpunch
                    "[bree.name] hardly has time to notice that I'm out of her before it happens."
                    show chest_insert bree cum
                    show belly_insert bree cum
                    show bree cowgirl resting dickcum cum onbody
                    with vpunch
                    "So she can't hope to cover herself as it spatters all over her."
                    with vpunch
                    "Her breasts take the majority of it, but some still hits her in the face."
                    "[bree.name] stares at me, her mouth hanging open as the cum begins to drip off of her."
                    hide chest_insert
                    hide belly_insert
                else:
                    show bree cowgirl condomcum with vpunch
                    pause 0.25
                    with vpunch
                    pause 0.25
                    with vpunch
                    "[bree.name] hardly has time to notice that I'm out of her before it happens."
                    "She stares at me, her mouth hanging"
            elif _return == "vaginal_inside_pill":
                bree.say "Oh..."
                bree.say "Don't stop..."
                bree.say "Pill..."
                "I silently thank [bree.name] for the timely reminder that she's on the pill."
                "Because it means that I can keep right on going until the very end."
                show bree cowgirl creampie up with vpunch
                $ bree.love += 2
                "And my reward is seeing the way that [bree.name]'s eyes pop open as I fill her."
                with vpunch
                "She clings to me, wanting every last moment of the sensation."
                show bree cowgirl -creampie down resting dickcum cum onpussy
                show pussy_insert bree zorder 1 at zoomAt(0.75, (820, 200))
                with vpunch
                "But afterwards she collapses atop me, panting and spent."
            elif _return == "vaginal_inside_pregnant":
                "The weight of [bree.name]'s swelling belly has been there the whole time."
                "And now it reminds me of the fact that I don't have to think of pulling out in time."
                "I keep on going, and [bree.name] rides me until the very last moment."
                show bree cowgirl creampie up with vpunch
                $ bree.love += 3
                "It hits her hard, even through she's already worked into a lather."
                with vpunch
                "She gasps as her eyes pop open, looking almost overwhelmed."
                with vpunch
                "But all the same she pushes herself down, wanting every moment of it."
                show bree cowgirl -creampie down smile resting dickcum cum onpussy
                show pussy_insert bree zorder 1 at zoomAt(0.75, (820, 200))
                "Afterwards she looks down at me happily, hands cradling her round belly."
            elif _return == "vaginal_inside_mad":
                bree.say "Oh no..."
                bree.say "We have to..."
                bree.say "We can't..."
                "I hear the words that are coming out of [bree.name]'s mouth."
                "But by then, it's already too late to stop what's happening."
                show bree cowgirl creampie pleasure -blush with vpunch
                $ bree.love -= 5
                $ bree.impregnate()
                "She loses the ability to speak a moment later as I cum inside of her."
                with vpunch
                "What should be an intense and pleasurable thing becomes instantly tainted."
                show bree cowgirl -creampie resting dickcum cum onpussy
                show pussy_insert bree zorder 1 at zoomAt(0.75, (820, 200))
                with vpunch
                "And I can already tell that there's a rising panic in the way [bree.name]'s panting and gasping for breath..."
            elif _return == "vaginal_inside_happy":
                bree.say "Oh no..."
                bree.say "Don't stop..."
                bree.say "I want it!"
                "It's more the surprise at [bree.name]'s plea that keeps me from pulling out of her rather than any conscious wish to do as she says in those final moments."
                show bree cowgirl creampie up with vpunch
                $ bree.love += 5
                $ bree.impregnate()
                "And so I shoot my load into her while feeling more than a little confused."
                with vpunch
                "But she confirms that this is what she wants by clinging onto me the whole time."
                with vpunch
                "[bree.name] moans and nods desperately as I cum inside of her, elated to be getting her way."
    return

label bree_fuck_date_reverse_cowgirl(sexperience_min):
    hide bree
    show bree naked at center, zoomAt (2.0, (640, 1300))
    with vpunch
    "[bree.name] lands atop me, pinning me to the bed."
    bree.say "You know those mechanical bulls they have in western bars?"
    mike.say "Y...yeah, bree..."
    mike.say "Like a bucking bronco, right?"
    bree.say "I never plucked up the courage to ride one of those."
    show bree flirt
    bree.say "So I'm going to ride you instead, [hero.name]!"
    bree.say "You think you can live up to one of those things?"
    mike.say "You bet, [bree.name]!"
    show bree happy at center, zoomAt (1.0, (640, 1300)), startle
    "[bree.name] claps her hands and giggles with genuine glee."
    "Then she wastes no time in straddling me around the middle."
    "She has her back turned to me, glancing over her shoulder."
    scene bree reverse cowgirl with fade
    bree.say "You're not like a mechanical bull, [hero.name]."
    bree.say "For a start there's nothing to hold onto!"
    mike.say "Maybe not, [bree.name]."
    mike.say "But I bet you I've got more stamina!"
    mike.say "And more skill where it counts too!"
    "[bree.name] raises an eyebrow at this."
    bree.say "Big talk!"
    bree.say "Let's see if you can back it up!"
    "With that, she takes hold of my cock, squeezing it hard."
    "I let out a grunt, more for show than to express pain."
    "The truth is that it feels good to have her manhandle me like this."
    "And I can already feel my cock getting hard as a rock from the sensation."
    "[bree.name]'s acting like she's the one in control here, like she's in charge."
    "But I think I have a couple of little surprises in store for her along the way."
    "The first of them being just where she's about to sit down."
    "And exactly where my cock's going to end up..."
    menu:
        "Fuck her ass" if bree.flags.anal >= 2 and hero.sexperience >= (sexperience_min + 5):
            "Part of me kind of resents being compared to a mechanical bull."
            "And so maybe that's why I think up a small measure of revenge."
            "[bree.name] lifts herself up to allow me the space to get my cock ready for her."
            "But as I do so, I'm sure to aim it at just the right angle..."
            show bree reverse cowgirl blush
            bree.say "Okay, [hero.name]..."
            bree.say "Here I come!"
            bree.say "Ooh...oh no!"
            "[bree.name] wriggles in surprise as she feels my cock between her buttocks."
            "Of course she thinks that it just missed the target."
            "No doubt she's expecting me to just rearrange things down there."
            "But as far as I'm concerned, it's right on target!"
            mike.say "Don't worry, [bree.name]!"
            mike.say "Just making sure you're strapped in."
            mike.say "And it needs to be nice and tight for a ride like this!"
            "I know that my cock is in just the right position."
            "And that's because I can feel the soft texture of [bree.name]'s hole."
            "All it takes is one firm pull downwards with my arms."
            "And one firm thrust upwards from my hips."
            show bree reverse cowgirl anal pain
            bree.say "Aah..."
            bree.say "Oh god..."
            bree.say "You...you're in my butt!"
            "I watch [bree.name]'s reaction carefully as she sinks down onto me."
            "Sure, I want to fuck her ass pretty badly right now."
            "But it's not worth hurting her just to get what I want."
            "That's why I feel a real sense of relief as I see her expression change."
            "I can only see [bree.name]'s face in profile, but it's enough."
            "There's no mistaking the pleasure that spreads over it."
            "And at the same time I can feel her muscles yielding to me."
            show bree reverse cowgirl normal
            "So by the time she's swallowed me whole, [bree.name]'s seriously into it!"
            "Still I take my time and make sure to build up slowly."
            "I want [bree.name] to enjoy this, not to be unable to sit down for a week!"
            "This means that I start out gently moving inside of her."
            "She seems to appreciate this, moaning softly and nodding."
            "A little at a time I up my speed and thrust with more force."
            "And each time I do this, [bree.name] takes it at a similar pace."
            "Her moans become sighs, and then gasps as this happens."
            with vpunch
            "She starts to move too, body riding the motion of my hips."
            show bree reverse cowgirl at startle(0.05,-10)
            "I know that this is more like a sedate pony ride than a bucking bronco."
            "But the way it's making me feel, I couldn't care less!"
            show bree reverse cowgirl at startle(0.05,-10)
            "I had no idea that this hole could be so smooth, so sensual."
            "[bree.name]'s ass feels like velvet around my cock."
            show bree reverse cowgirl at startle(0.05,-10)
            "And the way her muscles are gripping me is just magical!"
            "So there you have it - anal sex is magic!"
            with vpunch
            "Seriously though, [bree.name] looks like she's having the time of her life too."
            show bree reverse cowgirl at startle(0.05,-10)
            "I'm using my hands to guide her up and down on my cock."
            show bree reverse cowgirl at startle(0.05,-10)
            "But as time goes on, it feels more like I'm holding her up."
            show bree reverse cowgirl at startle(0.05,-10)
            "[bree.name]'s swaying and her head keeps sagging this way and that."
            show bree reverse cowgirl at startle(0.05,-10)
            "She really looks like her head's spinning!"
            bree.say "Oh, [hero.name]..."
            bree.say "I feel funny..."
            show bree reverse cowgirl pain
            bree.say "Like I'm gonna cum!"
            mike.say "Oh yeah?"
            mike.say "Well I've got news for you, [bree.name]..."
            mike.say "You're not the only one!"
            call cum_reaction (bree, 'anal', sexperience_min) from _call_cum_reaction_207
            if _return == 'anal_inside':
                "There's no time to do anything but hold on tight to [bree.name] as it happens."
                show bree reverse cowgirl creampie with vpunch
                "Luckily for me there's no danger involved in shooting my load in her ass!"
                with vpunch
                "And even better, doing that seems to be just what [bree.name] wants right now."
                show bree reverse cowgirl ahegao with vpunch
                "At least that's what she reaction leads me to believe."
                "[bree.name] throws her head back, hands gripping my thighs."
                $ bree.sub += 2
                "She looks just like she's riding one of the mechanical bulls she described."
                "But the thrill's coming from me filling her ass as I shoot my load!"
            elif _return == 'anal_outside':
                show bree reverse cowgirl -anal
                show chest_insert bree zorder 1 at zoomAt(1, (840, 120))
                show belly_insert bree zorder 2 at zoomAt(1, (0, 380))
                "I only just manage to pull my cock out of [bree.name]'s ass before I lose it."
                show bree reverse cowgirl ahegao
                "She squirms and wriggles the whole time, not happy with me pulling out."
                "But there's nothing she can do to stop me, as the sensation pushes her over the edge."
                "This means that [bree.name] cums while wriggling in my lap, moaning and wailing."
                show bree reverse cowgirl cumshot with vpunch
                $ bree.sub += 2
                "And those sounds become even more intense when I shoot my load up her body a moment later."
                show chest_insert bree cum
                show belly_insert bree cum
                with vpunch
                "[bree.name] pants with genuine exhaustion as it spatters her breasts and runs downwards."
                with vpunch
                "Soon it's trickling down her belly and back onto my own thighs too."
                hide chest_insert
                hide belly_insert
            $ bree.flags.anal += 1
        "Fuck her pussy":
            "Part of me kind of resents being compared to a mechanical bull."
            "And so maybe that's why I think up a small measure of revenge."
            call check_condom_usage (bree) from _call_check_condom_usage_118
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show bree reverse cowgirl condom
            "[bree.name] lifts herself up to allow me the space to get my cock ready for her."
            "And that's the moment I choose to strike!"
            "I tighten my grip on her haunches and then pull her downwards."
            show bree reverse cowgirl blush
            bree.say "Wha..."
            bree.say "Whoa..."
            bree.say "What are you..."
            "[bree.name] doesn't have time to finish what she was trying to say."
            "Because a moment later the head of my cock is pressing against the lips of her pussy."
            "Her words turn into a helpless moan as the pressure translates into desperate pleasure."
            "The head slides around for a few seconds, slipping on the already glistening folds."
            "But soon enough nature takes its course, and they begin to part slowly, letting me inside."
            show bree reverse cowgirl vaginal pain
            "[bree.name] inches her way down and onto my cock, gasping the whole time."
            "She only stops once she's actually sitting astride me again."
            "But now, when she looks back over her shoulder, her face is very different."
            show bree reverse cowgirl normal
            "[bree.name]'s cheeks are flushed with colour and her eyes are a little glassy."
            "She looks overwhelmed and more than a little helpless right now!"
            mike.say "Are you ready, [bree.name]?"
            bree.say "Huh..."
            bree.say "Wha..."
            bree.say "Ready for what?"
            mike.say "For your ride on the bucking bronco!"
            mike.say "Hold on tight..."
            mike.say "Because here we go!"
            "I don't honestly know if [bree.name] understands what I just said to her."
            "But I have a good grip on her and I'm not about to stop now."
            "If bree wants to ride a mechanical bull, then I'm going to make it happen."
            "Sure, I might not have the same stamina as one of those things."
            "But I'll do my best to imitate the experience!"
            "Normally I'd start out slow and build my speed gradually."
            "But this isn't a normal occasion, and so I start out as I mean to go on."
            with vpunch
            "My first thrust into [bree.name] is hard and fast, going as deep as I can."
            "She's not expecting it, and she arches her back, moaning at the sensation."
            "And this is the important part, the part where I hold back a moment."
            "Just long enough to gauge her response to the pace I'm setting."
            "Sure, I want to have some fun and make [bree.name] dance on the end of my cock."
            "But I'm not a sadist and I don't want to actually hurt her."
            "So I'm waiting to see if she objects..."
            "And then I see her nodding her head, which is all the answer I need."
            "I launch into it, not stopping for another second."
            with vpunch
            "I keep a tight hold of [bree.name]'s haunches as I thrust upwards."
            show bree reverse cowgirl at startle(0.05,-10)
            "Instantly she's bucking and twisting atop me."
            "It looks like she's fighting to stay on me."
            "But in reality I have a firm grip on [bree.name], and she's not going anywhere."
            show bree reverse cowgirl at startle(0.05,-10)
            "She tries her best to stay upright, to ride me with confidence."
            "But I'm not holding anything back tonight, and it shows."
            show bree reverse cowgirl at startle(0.05,-10)
            "[bree.name] sways this way and that, like tall grass in the wind."
            "And all the time she's crying out from the sensations she's feeling."
            show bree reverse cowgirl at startle(0.05,-10)
            "I can feel those same things too, every time I thrust into her."
            "She's not the only one getting something out of this."
            show bree reverse cowgirl at startle(0.05,-10)
            "The sensation of [bree.name] riding my cock is incredible from down here too!"
            with vpunch
            "[bree.name]'s pushing down on me with all of her weight."
            show bree reverse cowgirl at startle(0.05,-10)
            "I don't know if she's aware of what she's doing."
            show bree reverse cowgirl at startle(0.05,-10)
            "Or if it's just a desperate attempt to keep from falling off."
            show bree reverse cowgirl at startle(0.05,-10)
            "But the result is the same, magnifying what I'm feeling many times over."
            bree.say "Oh, [hero.name]..."
            bree.say "I feel funny..."
            show bree reverse cowgirl pain
            bree.say "Like I'm gonna cum!"
            mike.say "Oh yeah?"
            mike.say "Well I've got news for you, [bree.name]..."
            mike.say "You're not the only one!"
            call cum_reaction (bree, 'vaginal', sexperience_min, 150) from _call_cum_reaction_208
            if _return == "vaginal_condom":
                "There's no time to do anything but hold on tight to [bree.name] as it happens."
                "Luckily for me there's no danger involved in shooting my load in her."
                "We took the time to use a condom, so there's no need to hold back."
                "And even better, doing that seems to be just what [bree.name] wants right now."
                "At least that's what she reaction leads me to believe."
                show bree reverse cowgirl ahegao with vpunch
                "[bree.name] throws her head back, hands gripping my thighs."
                with vpunch
                "She looks just like she's riding one of the mechanical bulls she described."
                show bree reverse cowgirl out cum with vpunch
                "But the thrill's coming from me filling her pussy as I shoot my load!"
            elif _return == "vaginal_outside":
                show bree reverse cowgirl -vaginal
                show chest_insert bree zorder 1 at zoomAt(1, (840, 120))
                show belly_insert bree zorder 2 at zoomAt(1, (0, 380))
                "I only just manage to pull my cock out of [bree.name]'s pussy before I lose it."
                show bree reverse cowgirl ahegao
                "She squirms and wriggles the whole time, not happy with me pulling out."
                "But there's nothing she can do to stop me, as the sensation pushes her over the edge."
                "This means that [bree.name] cums while wriggling in my lap, moaning and wailing."
                show bree reverse cowgirl cumshot with vpunch
                $ bree.love += 1
                "And those sounds become even more intense when I shoot my load up her body a moment later."
                show chest_insert bree cum
                show belly_insert bree cum
                with vpunch
                "[bree.name] pants with genuine exhaustion as it spatters her breasts and runs downwards."
                with vpunch
                "Soon it's trickling down her belly and back onto my own thighs too."
                hide chest_insert
                hide belly_insert
            elif _return == "vaginal_inside_pill":
                bree.say "I'm...on...the...pill!"
                bree.say "So...don't...stop!"
                "There's no time to do anything but hold on tight to [bree.name] as it happens."
                "Luckily for me there's no danger involved in shooting my load in her."
                "As she just reminded me, she's on the pill."
                "And even better, doing that seems to be just what [bree.name] wants right now."
                "At least that's what she reaction leads me to believe."
                $ bree.love += 2
                show bree reverse cowgirl ahegao with vpunch
                "[bree.name] throws her head back, hands gripping my thighs."
                with vpunch
                "She looks just like she's riding one of the mechanical bulls she described."
                show bree reverse cowgirl creampie with vpunch
                "But the thrill's coming from me filling her pussy as I shoot my load!"
            elif _return == "vaginal_inside_pregnant":
                bree.say "I'm...already...pregnant!"
                bree.say "So...don't...stop!"
                "There's no time to do anything but hold on tight to [bree.name] as it happens."
                "Luckily for me there's no danger involved in shooting my load in her."
                "As if I needed reminding that she's pregnant!"
                "And even better, doing that seems to be just what [bree.name] wants right now."
                "At least that's what she reaction leads me to believe."
                show bree reverse cowgirl ahegao with vpunch
                $ bree.love += 3
                "[bree.name] throws her head back, hands gripping my thighs."
                with vpunch
                "She looks just like she's riding one of the mechanical bulls she described."
                show bree reverse cowgirl creampie with vpunch
                "But the thrill's coming from me filling her pussy as I shoot my load!"
            elif _return == "vaginal_inside_happy":
                bree.say "Please...keep going..."
                bree.say "Don't...stop!"
                "There's no time to do anything but hold on tight to [bree.name] as it happens."
                "And [bree.name]'s words are more than enough to throw me in the last few seconds."
                "It's only as I feel myself lose it that I remember we didn't use a condom!"
                show bree reverse cowgirl ahegao with vpunch
                "[bree.name] throws her head back, hands gripping my thighs."
                with vpunch
                "She's nodding and gasping like she's delighted with what's happening."
                with vpunch
                "She looks just like she's riding one of the mechanical bulls she described."
                show bree reverse cowgirl creampie with vpunch
                $ bree.impregnate()
                "But the thrill's coming from me filling her pussy as I shoot my load!"
                $ bree.love += 5
                "I don't feel the same way, as I'm already beginning to panic!"
            elif _return == "vaginal_inside_mad":
                bree.say "Please...stop..."
                bree.say "You have to stop!"
                "There's no time to do anything but hold on tight to [bree.name] as it happens."
                "And [bree.name]'s words are more than enough to throw me in the last few seconds."
                "It's only as I feel myself lose it that I remember we didn't use a condom!"
                "[bree.name] throws her head back, hands gripping my thighs."
                show bree reverse cowgirl ahegao with vpunch
                "She's shaking her head like crazy, like she can't believe what's happening"
                with vpunch
                "She looks just like she's riding one of the mechanical bulls she described."
                show bree reverse cowgirl creampie with vpunch
                $ bree.impregnate()
                "But the thrill's coming from me filling her pussy as I shoot my load!"
                "The moment it's over, she looks at me with shock, even anger in her eyes."
                $ bree.love -= 5
                "Of shit - what have we done?!?"
    "Once it's over [bree.name] literally flops into my arms, resting against me."
    show cuddle bree with fade
    "She remains still and silent as I gently lower her onto the bed at my side."
    "The only sign of life that she shows is to take hold of my arm and pull it over her."
    "I take this as her wanting to cuddle, and so draw her into my embrace."
    "And we lie there for a while, silent and still, just enjoying the afterglow."
    return

label bree_fuck_date_missionary(sexperience_min):
    call check_condom_usage (bree) from _call_check_condom_usage_26
    if _return == False:
        return "leave_without_gain"
    "I take [bree.name] firmly by the hand and lead her over to the side of the bed."
    "She still seems nervous, stealing glances at me as we go and smiling weakly."
    mike.say "You don't have to be afraid, [bree.name]."
    if not bree.is_sex_slave:
        mike.say "I want you so badly right now - but whatever happens, you can always say no."
    "[bree.name] gulps audibly, but nods all the same."
    bree.say "O...okay, [hero.name]...I trust you."
    "I can see that she's aware of just how hungrily I'm looking at her right now."
    if not bree.is_sex_slave:
        bree.say "You can...you can do whatever...whatever you want to do to me..."
    elif bree.flags.mikeNickname in nickname_daddy:
        bree.say "You can...you can do whatever...whatever you want to do to your little girl Daddy..."
    else:
        bree.say "You can...you can do whatever...whatever you want to do to me Master..."
    "Slowly, I climb atop her, making sure that my weight is lowered onto her gently and a little at a time."
    "[bree.name] remains still and compliant, the only sound she makes being the sound of her quickening breath."
    "I part her thighs and begin to rub my now stiff cock against the folds of her perfect pink pussy."
    if bree.is_sex_slave:
        bree.say "[hero.name]..."
    "She's already slick and warm, so soft and inviting that I have to struggle to keep from taking her right there and then."
    "But instead, I continue to tease her with the promise of my cock."
    if CONDOM:
        show bree missionary arm condom
    else:
        show bree missionary arm
    with fade
    "All the while that I'm tormenting [bree.name]'s pussy, I make sure to rub my chest against her stiffening nipples."
    "At the same time, I keep on nuzzling and nipping at her neck, my hands entwined in her hair."
    "She tries to writhe and move beneath me, lowering herself in the hope of capturing my cock."
    "But I can feel her every effort coming and move just enough to keep her constantly frustrated."
    bree.say "Please...[hero.name]...I want..."
    "I lean in close, my lips next to her ear as she pushes her head back into the pillows, looking for release."
    mike.say "What do you want, [bree.name]?"
    mike.say "Tell me, and you can have it...right now."
    "[bree.name] let's out a strangled cry of frustration before she's able to reply."
    bree.say "Uhhh...your cock..."
    bree.say "I want your cock inside of me..."
    bree.say "[hero.name], please...let me have your cock!"
    show bree missionary vaginal arm pleasure
    "Not wanting to disappoint her, I instantly oblige."
    "By now, I'm laid completely atop [bree.name], my arms pinning her shoulders and legs upon her thighs."
    "All it takes is a subtle movement and I'm inside of her in less than a second."
    "I don't go slowly, either - using my superior weight and angle to push as far into [bree.name] as I can physically manage."
    "Not stopping until I feel my balls against her ass, I use my entire body to push her further downwards."
    "If she was struggling to get her words out before now, [bree.name] loses the power of speech entirely at this point."
    "As I begin to thrust up and down, always careful never to fully pull out of her, she's reduced to mere cries and moans."
    "I'm being as relentless as I can be on [bree.name]'s pussy, actively trying to push her as far as I can."
    "She must be getting sore from the friction, as wet as she was when I began."
    "But still she shows no signs of begging me to stop, and so I press on with yet more gusto."
    "In the end, [bree.name]'s clinging to me, almost as though the only torture worse than going on would be to suddenly stop dead."
    "The latter of which might soon be the only option though, as I can already feel myself cumming."
    call cum_reaction (bree, 'vaginal', sexperience_min, 175) from _call_cum_reaction_58
    if _return == "vaginal_condom":
        show bree missionary arm pleasure condom with hpunch
        "I keep myself firmly inside of [bree.name] as I cum, feeling oddly thankful for the condom that lets me do so without fear of the consequences."
        with hpunch
        bree.say "Oh god...[hero.name]...I'm going to cum!"
        with hpunch
        "And then she does, her pussy clamping down on me like a man-trap as she shakes and quivers helplessly."
        with hpunch
        "I push into her as best I can, even with my cock already losing its stiffness, trying to give her all that I can."
        if bree.sub >= 75:
            "I carefully strip the condom off of my dick, taking care to catch as much of the cum as I can in the top as I do so."
            "Holding it in one hand, I beckon [bree.name] to come closer from where she's lying in a sweaty mess upon the bed."

            "I gently open her mouth, and then tip up the condom so that the contents drizzle onto her tongue."
            "[bree.name] swallows the dregs of my cum without complaint, even taking the time to lick her lips to ensure she's captured every last drop."
        "And in so short of a time after that crazy exertion and tumult, [bree.name]'s wrapped in my arms as still as if she were sleeping."
    elif _return == "vaginal_outside":
        show bree missionary -vaginal arm
        "I pull out just the moment before I cum."
        "Beneath me, [bree.name] moans in unconscious disappointment at her now empty pussy."
        show bree missionary arm cumshot with hpunch
        pause 0.25
        with hpunch
        pause 0.25
        with hpunch
        "I hardly notice her reaction, as I release a stream of warm cum onto her slick breasts, which runs around her nipples and onto her sweat-covered belly below."
        hide bree
        show bree missionary arm cum onbelly
        "[bree.name] looks seriously fucked, in every sense of the word."
        "But I'm guessing a degree of the delight that I can see in her eyes is on account of me not cumming inside her unprotected."
        "Still slippery and wet from everything that's been showered over her, she snakes into my arms and nestles there happily."
    elif _return == "vaginal_inside_pill":
        $ bree.sub += 1
        show bree missionary arm pleasure with hpunch
        "There's nothing I can do to stop myself from cumming, long and hard."
        show bree missionary arm ahegao creampie with hpunch
        bree.say "Ah...ah...[hero.name]!"
        with hpunch
        "[bree.name] begins to quiver and shake, her own orgasm taking hold of her."
        "I feel the muscles inside of her pussy clamp down on me, holding me inside of her."
        "It's hard to reconcile what she's doing with the look on her face right now."
        "Which is showing the strangest combination of ecstasy and concern."
        show bree missionary -vaginal
        show pussy_insert bree zorder 1 at zoomAt(0.75, (20, 200))
        with fade
        "Once she finally releases me, [bree.name] pulls herself up on her elbows and a little away from where I'm lying."
        "The look on her face reminds me of one of those classical oil paintings, in which someone's been mortally wounded and lies dying."
        "It's only when I follow her gaze down and see the sheer amount of glistening cum that's oozing out of her that I finally understand."
        bree.say "That's quite something..."
        $ bree.love += 1
    elif _return == "vaginal_inside_pregnant":
        $ bree.sub += 1
        show bree missionary arm pleasure with hpunch
        "There's nothing I can do to stop myself from cumming, long and hard."
        show bree missionary arm ahegao creampie with hpunch
        bree.say "Ah...ah...[hero.name]!"
        with hpunch
        "[bree.name] begins to quiver and shake, her own orgasm taking hold of her."
        "I feel the muscles inside of her pussy clamp down on me, holding me inside of her."
        "It's hard to reconcile what she's doing with the look on her face right now."
        "Which is showing the strangest combination of ecstasy and concern."
        show bree missionary -vaginal
        show pussy_insert bree zorder 1 at zoomAt(0.75, (20, 200))
        with fade
        "Once she finally releases me, [bree.name] pulls herself up on her elbows and a little away from where I'm lying."
        "The look on her face reminds me of one of those classical oil paintings, in which someone's been mortally wounded and lies dying."
        "It's only when I follow her gaze down and see the sheer amount of glistening cum that's oozing out of her that I finally understand."
        bree.say "That's quite something..."
        $ bree.love += 1
    elif _return == "vaginal_inside_mad":
        show bree missionary arm pleasure with hpunch
        "There's nothing I can do to stop myself from cumming, long and hard."
        $ bree.impregnate()
        $ bree.sub += 1
        show bree missionary arm ahegao creampie with hpunch
        bree.say "Ah...ah...[hero.name]!"
        with hpunch
        "[bree.name] begins to quiver and shake, her own orgasm taking hold of her."
        "I feel the muscles inside of her pussy clamp down on me, holding me inside of her."
        "It's hard to reconcile what she's doing with the look on her face right now."
        "Which is showing the strangest combination of ecstasy and concern."
        show bree missionary -vaginal
        show pussy_insert bree zorder 1 at zoomAt(0.75, (20, 200))
        with fade
        "Once she finally releases me, [bree.name] pulls herself up on her elbows and a little away from where I'm lying."
        "The look on her face reminds me of one of those classical oil paintings, in which someone's been mortally wounded and lies dying."
        "It's only when I follow her gaze down and see the sheer amount of glistening cum that's oozing out of her that I finally understand."
        bree.say "That's quite something..."
        bree.say "But did you have to...cum inside?"
        menu:
            "Not sorry!":
                mike.say "The way I felt, I was never going to pull out of you!"
                "I shake my head at her."
                mike.say "Do you have a problem with that?"
                "I know I sound like an asshole here - but she did tell me that she'd do whatever I wanted."
                show bree naked angry
                bree.say "I...I have to...I have to go - now!"
                $ bree.love -= 25
                "[bree.name]'s on her feet and out of the room before I can say a word."
                "Was it something I said?"
                return "leave_with_gain"
            "Sorry...":
                mike.say "God, I'm so sorry, [bree.name]."
                mike.say "I guess I just got so caught up in the moment I was swept away..."
                "[bree.name]'s clearly unhappy with the way things turned out here."
                "But there's something else on her mind, something I can't quite put my finger on."
                bree.say "Ah, I suppose it can't be helped now."
                bree.say "But you have to promise me that you'll use a condom next time, okay?"
                bree.say "We can't take that risk every time."
                "I'm a little hesitant to snuggle closer to her after that, for fear of her still being mad."
                "But [bree.name] soon puts my fears to rest by pulling my arm around her and placing herself firmly in my embrace."
    elif _return == "vaginal_inside_happy":
        show bree missionary arm pleasure with hpunch
        "There's nothing I can do to stop myself from cumming, long and hard."
        $ bree.impregnate()
        $ bree.sub += 1
        show bree missionary arm ahegao creampie with hpunch
        bree.say "Ah...ah...[hero.name]!"
        with hpunch
        "[bree.name] begins to quiver and shake, her own orgasm taking hold of her."
        "I feel the muscles inside of her pussy clamp down on me, holding me inside of her."
        "It's hard to reconcile what she's doing with the look on her face right now."
        "Which is showing the strangest combination of ecstasy and concern."
        show bree missionary -vaginal
        show pussy_insert bree zorder 1 at zoomAt(0.75, (20, 200))
        with fade
        "Once she finally releases me, [bree.name] pulls herself up on her elbows and a little away from where I'm lying."
        "The look on her face reminds me of one of those classical oil paintings, in which someone's been mortally wounded and lies dying."
        "It's only when I follow her gaze down and see the sheer amount of glistening cum that's oozing out of her that I finally understand."
        bree.say "That's quite something..."
        bree.say "But did you have to...cum inside?"
        menu:
            "Not sorry!":
                mike.say "The way I felt, I was never going to pull out of you!"
                "I shake my head at her."
                mike.say "Do you have a problem with that?"
                "I know I sound like an asshole here - but she did tell me that she'd do whatever I wanted."
                bree.say "Oh...okay, [hero.name]...so long as you're happy, so am I..."
                "I can tell that she's not, but as long as she's trying to hide it, I win."
                $ bree.flags.cumin = 1
                $ bree.love += 1
            "Sorry...":
                mike.say "God, I'm so sorry, [bree.name]."
                mike.say "I guess I just got so caught up in the moment I was swept away..."
                "[bree.name]'s clearly unhappy with the way things turned out here."
                "But there's something else on her mind, something I can't quite put my finger on."
                bree.say "Ah, I suppose it can't be helped now."
                bree.say "But you have to promise me that you'll use a condom next time, okay?"
                bree.say "We can't take that risk every time."
                "I'm a little hesitant to snuggle closer to her after that, for fear of her still being mad."
                "But [bree.name] soon puts my fears to rest by pulling my arm around her and placing herself firmly in my embrace."
    return

label bree_fuck_date_spoon(sexperience_min):
    "As if to make her intentions plain, [bree.name] reaches behind her back."
    "And I feel her hand stroking my half-erect cock."
    "I feel myself shrugging and decide that sleep can wait a while."
    "And if I drop off halfway through, then maybe [bree.name] can take care of herself!"
    mike.say "Okay, [bree.name]."
    mike.say "But we keep it slow and gentle, yeah?"
    "[bree.name] nods and lets out a sleepy little giggle."
    bree.say "You got it!"
    menu:
        "Fuck her pussy":
            show bree spoon with fade
            "Placing a hand on [bree.name]'s waist, I pull her towards me."
            "Now she's snuggling down into my lap with nothing at all between us."
            "And the sensation is a hundred times more pleasurable than before."
            call check_condom_usage (bree) from _call_check_condom_usage_27
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show bree spoon condom
            "[bree.name] seems more than content just to lie back and leave things to me."
            "So I take full advantage, gently sliding my cock between her thighs."
            "I begin by slowly teasing the lips of her pussy with the head."
            "And by doing this I start to feel that part of her waking up."
            "While [bree.name]'s head is getting drowsy, her pussy is coming alive."
            "Every time I rub my cock up and down her lips, they're slicker than before."
            "I hardly have to try at all to make them part when the time comes."
            "It's like [bree.name]'s pussy has a mind of it's own as it opens up for me."
            show bree spoon vaginal eyes_surprised mouth_pain
            "And I slip into her smoothly, in one continuous motion."
            "[bree.name] moans with half-conscious pleasure as I fill her."
            "Then I feel her reach around to grab hold of my wrist."
            "I don't resist as she guides my hand around to her front."
            show bree spoon eyes_closed
            "Then she presses it against the folds of her pussy."
            "At the same time, I start moving lazily in and out of her."
            "Plucking idly at her pussy as I do so."
            show bree spoon mouth_pleasure
            "I can feel the effect that my efforts are having on [bree.name]."
            "She's still moaning and gasping with each thrust I make."
            "But her body never moves more than a slight quiver the whole time."
            "It's like she simply doesn't have the energy to do anything but lie there."
            "Lie there and take it as I keep on pushing her further onwards."
            "And it's not like I've been given a new lease of life either."
            "My motions are almost lethargic, my limbs heavy and slow."
            "But somehow I can find the energy to keep on making idle love to [bree.name]."
            "It's like the sensation of being inside her is keeping me going."
            "The feeling of what I'm doing to her sustaining me as I fuck her."
            "That's why the sensation of being about to cum creeps up on me."
            "Before I know it, I can't hold back any longer."
            mike.say "B...[bree.name]..."
            mike.say "I'm gonna cum!"
            bree.say "Oh..."
            show bree spoon eyes_ahegao
            bree.say "Me too!"
            call cum_reaction (bree, 'vaginal', sexperience_min, 190) from _call_cum_reaction_59
            if _return == 'vaginal_condom':
                "Neither of us has a thing to worry about."
                "And that's because we remembered to use a condom."
                with hpunch
                "[bree.name] pushes herself back into me as I lose it."
                with hpunch
                "Which means I can feel how much she enjoys the sensation."
                with hpunch
                "Then I get to experience the pleasure of her orgasm too."
            elif _return == 'vaginal_outside':
                show bree spoon out
                "I just manage to muster the strength to pull out before the end."
                show bree spoon cum with hpunch
                $ bree.love += 1
                "This means I shoot my load up [bree.name]'s back a moment later."
                with hpunch
                "And the sensation of me pulling out makes her cum too."
                with hpunch
                "We keep on spooning as we both orgasm at the same time."
            elif _return == 'vaginal_inside_pill':
                bree.say "Don't worry..."
                bree.say "I'm on the pill..."
                with hpunch
                "[bree.name] pushes herself back into me as I lose it."
                show bree spoon cum mouth_ahegao with hpunch
                $ bree.love += 2
                "Which means I can feel how much she enjoys the sensation."
                with hpunch
                "Then I get to experience the pleasure of her orgasm too."
            elif _return == 'vaginal_inside_pregnant':
                "[bree.name] guides my hand to her swelling belly as a reminder that she's already pregnant."
                with hpunch
                "Then she pushes herself back into me as I lose it."
                show bree spoon cum mouth_ahegao with hpunch
                $ bree.love += 3
                "Which means I can feel how much she enjoys the sensation."
                with hpunch
                "Then I get to experience the pleasure of her orgasm too."
            elif _return == 'vaginal_inside_happy':
                mike.say "Uh..."
                mike.say "I gotta..."
                mike.say "Gotta pull out..."
                with hpunch
                "[bree.name] pushes herself back into me before I can actually do it."
                show bree spoon cum mouth_ahegao with hpunch
                $ bree.love += 5
                $ bree.impregnate()
                "Which means I can feel how much she enjoys the sensation."
                with hpunch
                "Then I get to experience her orgasm too."
            elif _return == 'vaginal_inside_mad':
                bree.say "You have to..."
                bree.say "You have to pull out..."
                "[bree.name] warns me at the moment it's already too late."
                show bree spoon cum eyes_closed mouth_pain with hpunch
                $ bree.love -= 5
                $ bree.impregnate()
                pause 0.25
                with hpunch
                "I shoot my load into her, and she cums as I do so."
                with hpunch
                "We should be up and awake, trying to do something about this mess."
        "Fuck her ass" if bree.flags.anal >= 2 and hero.sexperience >= (sexperience_min + 5):
            show bree spoon with fade
            "Placing a hand on [bree.name]'s waist, I pull her towards me."
            "Now she's snuggling down into my lap with nothing at all between us."
            "And the sensation is a hundred times more pleasurable than before."
            "[bree.name] seems more than content just to lie back and leave things to me."
            "So I take full advantage, gently sliding my cock between her thighs."
            "What I have in mind might wake [bree.name] up a little."
            "But I'm kind of counting on her being too out of it to protest."
            "As boldly as I dare, I aim my cock towards [bree.name]'s ass."
            show bree spoon anal eyes_surprised mouth_pain
            "And then I use the last of my reserves to push it straight in there!"
            bree.say "Mmm..."
            bree.say "Oh, [hero.name]..."
            bree.say "My ass!"
            "[bree.name] wriggles a little, moaning as she does so."
            "But by now my cock is already a few inches into her."
            "And a moment later she seems to realise it's pointless to resist."
            show bree spoon eyes_closed
            bree.say "Okay..."
            bree.say "Okay..."
            bree.say "You can fuck my ass!"
            show bree spoon mouth_pleasure
            "[bree.name] moans with half-conscious pleasure as I fill her."
            "Then I feel her reach around to grab hold of my wrist."
            "I don't resist as she guides my hand around to her front."
            "Then she presses it against the folds of her pussy."
            "At the same time, I start moving lazily in and out of her."
            "Plucking idly at her pussy as I do so."
            "I can feel the effect that my efforts are having on [bree.name]."
            "She's still moaning and gasping with each thrust I make."
            show bree spoon eyes_pleasure
            "But her body never moves more than a slight quiver the whole time."
            "It's like she simply doesn't have the energy to do anything but lie there."
            "Lie there and take it as I keep on pushing her further onwards."
            "And it's not like I've been given a new lease of life either."
            "My motions are almost lethargic, my limbs heavy and slow."
            "But somehow I can find the energy to keep on making idle love to [bree.name]."
            "It's like the sensation of being inside her is keeping me going."
            "The feeling of what I'm doing to her sustaining me as I fuck her."
            "That's why the sensation of being about to cum creeps up on me."
            "Before I know it, I can't hold back any longer."
            mike.say "B...[bree.name]..."
            mike.say "I'm gonna cum!"
            bree.say "Oh..."
            show bree spoon eyes_ahegao
            bree.say "Me too!"
            call cum_reaction (bree, 'anal', sexperience_min) from _call_cum_reaction_60
            if _return == 'anal_inside':
                "Neither of us has a thing to worry about."
                "And that's one of the advantages of going in this way."
                with hpunch
                "[bree.name] pushes herself back into me as I lose it."
                show bree spoon cum mouth_ahegao with hpunch
                $ bree.sub += 2
                "Which means I can feel how much she enjoys the sensation."
                with hpunch
                "Then I get to experience the pleasure of her orgasm too."
            elif _return == 'anal_outside':
                show bree spoon out
                "I just manage to muster the strength to pull out before the end."
                with hpunch
                "This means I shoot my load up [bree.name]'s back a moment later."
                show bree spoon cum with hpunch
                $ bree.sub += 1
                "And the sensation of me pulling out makes her cum too."
                with hpunch
                "We keep on spooning as we both orgasm at the same time."
            $ bree.flags.anal += 1
    return


label bree_fuck_sasha_bedroom_intro(from_event=True):
    if from_event:
        scene expression f"bg {game.room}"
        "I'm just sitting there, minding my own business, when [bree.name] pokes her head around the door."
        bree.say "Psst..."
        bree.say "Hey..."
        show bree flirt casual with dissolve
        bree.say "Hey, [hero.name]!"
        "Looking up in surprise, I see that there's a look of mischief on her face."
        mike.say "Oh.."
        mike.say "Hey, [bree.name]!"
        mike.say "What's up?"
        "[bree.name] beckons for me to get up and come to her."
        "And for want of anything else to do, I get off my ass."
        show bree evil
        "As I get to the door, I notice that she's glancing around."
        "It's almost like she's afraid of being caught."
        "Which makes me intrigued to find out what this is all about."
        show bree normal
        bree.say "No questions!"
        bree.say "Just come with me."
        show bree at startle
        bree.say "NOW!"
        show bree at right with move
        "[bree.name] grabs hold of my hand and pulls me after her."
        "And I stop resisting once I see she's pulling me upstairs."
        "Because we all know what happens behind bedroom doors, right?"
        "But then she drags me straight past the door to her room."
        "And we end up standing outside Sasha's bedroom instead."
        scene bg secondfloor
        show bree casual evil
        with fade
        mike.say "[bree.name]..."
        mike.say "What the..."
        show bree annoyed
        bree.say "Shhh!"
        bree.say "I said no questions!"
        show bree evil
        "[bree.name] turns the door-handle."
        "And to my surprise, it opens!"
        mike.say "Oh..."
        mike.say "Sasha left her door unlocked!"
        "[bree.name] doesn't pause for a second."
        "She opens it up and slips inside."
        mike.say "And you're just going to walk straight in there, huh?"
    else:
        scene bg secondfloor
        show bree casual evil
        with fade
        "Without a word, [bree.name] leads me outside of Sasha's bedroom."
        "She turns the door-handle."
        "And, it opens!"
        "[bree.name] doesn't pause for a second."
        "She opens it up and slips inside."
    call bree_fuck_sasha_bedroom (sexperience_min=10) from _call_bree_fuck_sasha_bedroom
    if _return:
        return _return
    $ bree.sexperience += 1
    return


label bree_fuck_sasha_bedroom(sexperience_min=10):
    $ game.room = "bedroom3"
    scene bg bedroom3
    show bree casual normal
    with wiperight
    "For fear of being left alone in the corridor, I follow [bree.name] inside."
    "And then I push the door closed behind me."
    "Turning around, I see [bree.name] already rummaging through Sasha's stuff."
    mike.say "[bree.name]!"
    mike.say "We're not supposed to be in here!"
    if Harem.together('bree', 'sasha', name="home") and game.flags.bree_sasha_threesome:
        mike.say "Like, if Sasha invited us in, that's be different."
        mike.say "But she's not here, so we shouldn't be either!"
        "[bree.name] looks at me and shakes her head."
        bree.say "Ah..."
        bree.say "Don't be such a wuss!"
        bree.say "Sasha's probably cool with it."
        bree.say "I mean, she already let us fuck on her bed!"
        mike.say "Yeah, [bree.name] - with her!"
        mike.say "We fucked in here WITH HER!"
        bree.say "It's okay."
        bree.say "She's probably out at band practice or something..."
        bree.say "Ooh!"
        bree.say "Look at this!"
    else:
        mike.say "What if Sasha comes back and catches us?"
        "[bree.name] looks at me and shakes her head."
        bree.say "Ah..."
        bree.say "Don't be such a wuss!"
        bree.say "She's probably out at band practice or something..."
        bree.say "Ooh!"
        bree.say "Look at this!"
    "[bree.name] hurries over to a pile of Sasha's CD."
    "She randomly puts on of them into the stereo."
    play music "music/deathless_harpies/Deathless_Harpies.ogg" loop
    "And starts an air guitar performance."
    bree.say "Look at me, [hero.name]."
    show bree evil at startle
    bree.say "I'm Sasha - and I'm a moody bass player!"
    bree.say "I'm working on my solo and mooch around the house all day being complicated!"
    "I want to tell [bree.name] off and drag her out of the room."
    "But part of me can't help chuckling at her impression."
    mike.say "Okay, [bree.name]..."
    mike.say "I think you got Sasha down there!"
    mike.say "Now can we get the hell out of here?"
    "[bree.name] shakes her head and backs away from me."
    bree.say "Uh-uh!"
    show bree happy
    bree.say "You gotta catch me first!"
    "[bree.name] pulls off her T-shirt."
    show bree topless with dissolve
    "Then pulls down her own panties."
    show bree naked with dissolve
    "Kicking them aside, she sticks out her tongue."
    "Then she darts towards the bed."
    "Unable to think what else to do, I chase after her."
    "And I see my chance once [bree.name]'s on the bed."
    "I pounce on her and try to get a hold."
    "But [bree.name] has other ideas."
    scene bree doggy
    show bree doggy bedroom3 noone
    with fade
    bree.say "Mmm..."
    bree.say "Come on, [hero.name]."
    bree.say "Don't you wanna have some fun?"
    bree.say "Don't you wanna fuck me on Sasha's bed?"
    "Before I know what's happening, I'm pulling down my pants."
    "Pretty soon we're both naked on Sasha's bed."
    "Which I guess means we're really doing this thing!"
    show bree doggy bedroom3 -noone
    $ bree_bj = False
    menu:
        "Let's start with a blowjob":
            "I move around so that I'm kneeling in front of [bree.name]."
            show bree doggy front
            "And I pretty much shove my cock straight into her face."
            "[bree.name]'s eyes go wide with surprise for a moment."
            "But then she smiles and nods."
            bree.say "Okay!"
            bree.say "A blowjob it is!"
            "She licks her lips and leans forwards."
            show bree doggy suck normal
            "And at the same time, she takes hold of it with one hands."
            "[bree.name] closes her eyes as she parts her lips."
            "Which means she has to guide the tip into her mouth by feeling for it."
            "And I've got to admit I like the sight of her wrapping her lips around the head."
            show bree doggy scream
            "[bree.name] makes soft little moaning sounds as she starts to suck."
            "But these soon begin to increase in volume."
            "And at the same time, my feelings of pleasure increase too."
            "As [bree.name]'s head moves back and forth, it's my turn to get vocal."
            "I find that I can't keep from gasping as she works on me."
            "The fear of being discovered does nothing to silence me either."
            "[bree.name] begins to take my cock deeper into her mouth."
            show bree doggy normal
            "And I find myself wondering just how much she can take."
            menu:
                "Let's find out":
                    "With that in mind, I lean forwards a little."
                    "This doesn't seem to cause [bree.name] any problems."
                    show bree doggy deep
                    "She takes the extra length in with ease."
                    "So I push further still, just to satisfy my curiosity."
                    show bree doggy scream
                    "This keeps on going until my cock is literally down [bree.name]'s throat."
                    $ bree.sub += 1
                    $ bree.love -= 1
                    "She's giving me deep-throat, without any complaints too!"
                "Keep the pace":
                    "I have no idea if [bree.name] can handle anything like deep-throat."
                    "So I make doubly sure that she doesn't take it too deep."
                    show bree doggy scream
                    "That's not to say my cock isn't well in there."
                    $ bree.love += 1
                    "It's just not pushing down on [bree.name]'s tonsils, that's all!"
            "Suddenly I feel a change in the sensations from down there."
            "Before everything was building up."
            show bree doggy normal suck
            "But now I feel like it's going to explode!"
            menu:
                "Cum on her face":
                    "Pulling my cock out of [bree.name]'s mouth, I take aim for her face."
                    show bree doggy -suck
                    "Which just so happens to have a look of genuine surprise on it."
                    "And that makes what happens next all the more gratifying."
                    show bree doggy ahegao cumshot with hpunch
                    pause 0.25
                    with hpunch
                    "I shoot my load right at the target, spattering it all over [bree.name]'s face."
                    with hpunch
                    "Her mouth open, a good deal of it lands in her mouth too!"
                    show bree doggy ahegao cumonface -cumshot
                    "[bree.name] gasps and splutters as she struggles to swallow it down."
                    "But I'm too busy smiling to be able to offer her any help."
                "Cum in her mouth":
                    "I don't want to pull out, not when I'm so deep in [bree.name]'s mouth!"
                    with hpunch
                    "So I keep on going until I cum, shooting my load down her throat."
                    show bree doggy cuminmouth ahegao with hpunch
                    "[bree.name]'s eyes pop open, and she almost chokes on it."
                    with hpunch
                    "But through sheer force of will she makes herself swallow."
                    "Though her eyes are watering from the effort, [bree.name] pulls it off."
                    "And when she opens her mouth to gasp for air, there's no trace of it left."
            $ bree_bj = True
        "Just fuck her":
            pass
    menu:
        "Fuck her pussy":
            "Without saying a word, I get behind [bree.name] and grab hold of her haunches."
            "My hands hit her flesh with an audible slap, which makes [bree.name] jump."
            show bree doggy -suck -front -cuminmouth
            "And I take full advantage of the fact, pushing my cock between her legs."
            bree.say "Oh my!"
            bree.say "[hero.name] - you beast!"
            call check_condom_usage (bree) from _call_check_condom_usage_28
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show bree doggy condom
            "Strengthening my grip on [bree.name]'s waist, I push myself forwards."
            "This means that my cock slides along her pussy."
            "And as it does so there are no smart remarks or quips from [bree.name]."
            "Instead she lets out an almost desperate moan of desire."
            "One that seems to make me harder than ever."
            "And definitely makes me desperate to get inside of her too!"
            "[bree.name] reaches down and pushes the head of my cock against her lips."
            "She does this as I'm beginning to move back and forwards."
            "But still this doesn't mean that I sink straight into her."
            "The lips of her pussy put up a few more seconds of resistance."
            "This drags out the experience, but also makes us both want it more."
            "So when they finally part, it's to desperate gasps of release."
            show bree doggy vaginal scream
            if CONDOM:
                show bree doggy vaginal condom
            bree.say "Oh yeah..."
            bree.say "Don't hold back..."
            bree.say "Please...fill me up!"
            "My instinct is to give [bree.name] exactly what she wants."
            "To shove my cock as deep into her as it'll go."
            "But I know that a lot of her pleasure right now is coming from anticipation."
            "So instead I feed her a little bit of my cock at a time."
            "Sure, this makes her pant and huff in frustration at being denied."
            "But by the time I'm all the way in, she's almost helpless."
            "[bree.name] nods desperately as I begin to thrust in and out of her."
            "It's like every movement I make is something she needs to keep herself sane."
            "And before too long, I'm picking up speed, fucking her ever harder."
            "Now that she's getting what she wants, [bree.name] doesn't hold back either."
            "She rides my cock like her life depends on it."
            show bree doggy scream
            "And I can hear Sasha's bed creaking under us the whole time."
            "I just pray that we don't end up breaking it before we're done!"
            "It's just then that I see a basket by Sasha's bed."
            "The thing is poking out from underneath, and it's full of toys!"
            menu:
                "Use the anal beads":
                    "I can't resist the sight of the anal beads in the basket."
                    "So I lean down and scoop them up in one move."
                    "Before [bree.name] can even ask what's going on, I put them to use."
                    show bree doggy beads
                    "She lets out a yelp of surprise as I push the first bead home."
                    $ bree.sub += 1
                    "And then each successive bead in her ass earns a muted moan of pleasure."
                    "Once all of them are up there, I leave them in place for a short while."
                    "Then I tug the whole lot out again in one go."
                    show bree doggy beads ahegao
                    "Now [bree.name] doesn't yelp or moan, she cries out at the sensation instead!"
                "Pull her hair":
                    "Invigorated by the sight of the toys, I make a grab for [bree.name]'s hair."
                    "With a good handful in my hand, I start to pound her harder than ever."
                    show bree doggy pull ahegao
                    $ bree.sub += 2
                    "If anything, the sensation of me pulling on her hair seems to turn [bree.name] on even more."
                    "She gasps and moans with pleasure the whole time."
                    "And when she has the chance to move her head she does so."
                    "Nodding almost desperately for more of the same treatment."
                "Stay simple":
                    "But I choose to ignore all of those things and keep right on going."
                    "I don't need toys, battery-operated or otherwise, to get the job done."
                    show bree doggy ahegao
                    $ bree.love += 2
                    "And the evidence of that is written all over [bree.name]'s face right now!"
                    "She's nodding, moaning and panting for more."
                    "So I redouble my efforts, giving her all that I can possibly give."
            bree.say "Oh..."
            bree.say "Oh fuck..."
            show bree doggy scream
            bree.say "I can't...can't take it!"
            "As soon as the words are out of [bree.name]'s mouth, I breathe a sigh of relief."
            "Because I'm pretty much in the same place she is right now as well!"
            "So I don't feel any shame in the act of letting myself go."
            call cum_reaction (bree, 'vaginal', sexperience_min) from _call_cum_reaction_61
            if _return == "vaginal_condom":
                "It's now that I'm thankful we bothered to use a condom."
                "Because it means there's no need to bother thinking it out."
                "I can just keep right on going until the very end."
                with hpunch
                $ bree.love += 1
                "And that's just what I do, enjoying every second of my orgasm."
                show bree doggy ahegao with hpunch
                "Moments later I get a second helping of pleasure as [bree.name] cums too."
                with hpunch
                "The muscles inside her body squeezing my cock as she shudders from head to toe."
            elif _return == "vaginal_outside":
                "I need to pull my cock out of [bree.name] before it's too late."
                "And I manage to do that with a couple of seconds to spare."
                show bree doggy -vaginal cumshot ahegao with hpunch
                "I shoot my load over [bree.name]'s helpless form, showering her in cum."
                with hpunch
                $ bree.love += 1
                "Enjoying every second of my orgasm, I savour the sight."
                show bree doggy cumonass -cumshot with hpunch
                "Moments later I get a second helping of pleasure as [bree.name] cums too."
                with hpunch
                "The muscles inside her body making her shudder from head to toe."
            elif _return == "vaginal_inside_pill":
                bree.say "Go ahead..."
                bree.say "Do it..."
                bree.say "I'm on...the pill!"
                "It's now that I'm thankful [bree.name] started taking that thing."
                "Because it means there's no need to bother thinking it out."
                "I can just keep right on going until the very end."
                show bree doggy cuminpussy ahegao with hpunch
                "And that's just what I do, enjoying every second of my orgasm."
                $ bree.love += 2
                with hpunch
                "Moments later I get a second helping of pleasure as [bree.name] cums too."
                with hpunch
                "The muscles inside her body squeezing my cock as she shudders from head to toe."
            elif _return == "vaginal_inside_pregnant":
                bree.say "Go ahead..."
                bree.say "Do it..."
                bree.say "I'm pregnant...remember?!?"
                "It's now that I'm thankful I already got [bree.name] pregnant."
                "Because it means there's no need to bother thinking it out."
                "I can just keep right on going until the very end."
                show bree doggy cuminpussy ahegao with hpunch
                "And that's just what I do, enjoying every second of my orgasm."
                $ bree.love += 2
                with hpunch
                "Moments later I get a second helping of pleasure as [bree.name] cums too."
                with hpunch
                "The muscles inside her body squeezing my cock as she shudders from head to toe."
            elif _return == "vaginal_inside_mad":
                bree.say "[hero.name]..."
                bree.say "Don't do it..."
                bree.say "Don't cum in me!"
                "I was just about to pull out of [bree.name] before it happened."
                "But her demand catches me totally off-guard."
                "And before I can get my head around it, the inevitable happens."
                show bree doggy cuminpussy ahegao
                "Ironically it's her very warning that seals her fate!"
                with hpunch
                pause 0.25
                with hpunch
                "I shoot my load deep inside of [bree.name], much to her apparent horror."
                $ bree.love -= 5
                $ bree.impregnate()
                with hpunch
                "But I don't feel a thing, save for the horror growing inside of me."
            elif _return == "vaginal_inside_happy":
                bree.say "Go ahead..."
                bree.say "Do it..."
                bree.say "Cum in me!"
                "I was just about to pull out of [bree.name] before it happened."
                "But her demand catches me totally off-guard."
                show bree doggy cuminpussy ahegao
                "And before I can get my head around it, the inevitable happens."
                with hpunch
                pause 0.25
                with hpunch
                pause 0.25
                with hpunch
                "I shoot my load deep inside of [bree.name], much to her apparent delight."
                $ bree.love += 5
                $ bree.impregnate()
                "But I don't feel a thing, save for the horror growing inside of me."
        "Fuck her ass" if bree.flags.anal >= 2 and hero.sexperience >= (sexperience_min + 5):
            "Without saying a word, I get behind [bree.name] and grab hold of her haunches."
            "My hands hit her flesh with an audible slap, which makes [bree.name] jump."
            show bree doggy -suck -front -cuminmouth
            "And I take full advantage of the fact, pushing my cock between her legs."
            bree.say "Oh my!"
            bree.say "[hero.name] - you beast!"
            mike.say "Oh, you have no idea, [bree.name]!"
            "Strengthening my grip on [bree.name]'s waist, I push myself forwards."
            "This means that my cock slides along her pussy for the first time."
            "And as it does so there are no smart remarks or quips from [bree.name]."
            "Instead she lets out an almost desperate moan of desire."
            "One that seems to make me harder than ever."
            "And definitely makes me desperate to get inside of her too!"
            "[bree.name] reaches down and pushes the head of my cock against her lips."
            "She does this as I'm beginning to move back and forwards."
            "But then I decide that it's time to change the plan."
            "Before [bree.name] can react, I push my cock between her buttocks."
            "And I start to sink into her ass!"
            show bree doggy scream
            bree.say "Wha..."
            bree.say "What are you..."
            bree.say "Oh god!"
            "[bree.name] moans with unexpected pleasure as I inch into her ass."
            "And soon enough she's nodding her head, begging for more."
            show bree doggy anal normal
            bree.say "Oh yeah..."
            bree.say "Don't hold back..."
            bree.say "Please...fill me up!"
            "My instinct is to give [bree.name] exactly what she wants."
            "To shove my cock as deep into her as it'll go."
            "But I know that a lot of her pleasure right now is coming from anticipation."
            "So instead I feed her a little bit of my cock at a time."
            "Sure, this makes her pant and huff in frustration at being denied."
            "But by the time I'm all the way in, she's almost helpless."
            "[bree.name] nods desperately as I begin to thrust in and out of her."
            "It's like every movement I make is something she needs to keep herself sane."
            "And before too long, I'm picking up speed, fucking her ever harder."
            "Now that she's getting what she wants, [bree.name] doesn't hold back either."
            "She rides my cock like her life depends on it."
            "And I can hear Sasha's bed creaking under us the whole time."
            "I just pray that we don't end up breaking it before we're done!"
            "It's just then that I see a basket by Sasha's bed."
            show bree doggy scream
            "The thing is poking out from underneath, and it's full of toys!"
            menu:
                "Use the vibrator":
                    "I can't resist the sight of a vibrator in the basket."
                    show bree doggy dildoout
                    "So I lean down and scoop it up in one move."
                    "Before [bree.name] can even ask what's going on, I put it to use."
                    "She lets out a yelp of surprise as I push head home."
                    show bree doggy dildoin ahegao
                    $ bree.sub += 1
                    "And then I begin to work it deep into her pussy."
                    "Soon the yelps are replaced by moans of submission."
                    "And I can feel that [bree.name]'s getting close to her limit."
                "Pull her hair":
                    "Invigorated by the sight of the toys, I make a grab for [bree.name]'s hair."
                    "With a good handful in my hand, I start to pound her harder than ever."
                    "If anything, the sensation of me pulling on her hair seems to turn [bree.name] on even more."
                    show bree doggy pull ahegao
                    $ bree.sub += 2
                    "She gasps and moans with pleasure the whole time."
                    "And when she has the chance to move her head she does so."
                    "Nodding almost desperately for more of the same treatment."
                "Stay simple":
                    "But I choose to ignore all of those things and keep right on going."
                    "I don't need toys, battery-operated or otherwise, to get the job done."
                    "And the evidence of that is written all over [bree.name]'s face right now!"
                    "She's nodding, moaning and panting for more."
                    $ bree.love += 2
                    show bree doggy ahegao
                    "So I redouble my efforts, giving her all that I can possibly give."
            bree.say "Oh..."
            bree.say "Oh fuck..."
            show bree doggy scream
            bree.say "I can't...can't take it!"
            "As soon as the words are out of [bree.name]'s mouth, I breathe a sigh of relief."
            "Because I'm pretty much in the same place she is right now as well!"
            "So I don't feel any shame in the act of letting myself go."
            call cum_reaction (bree, 'anal', sexperience_min) from _call_cum_reaction_62
            if _return == 'anal_inside':
                "It's now that I'm thankful I decided to fuck [bree.name]'s ass."
                "Because it means there's no need to bother thinking it out."
                "I can just keep right on going until the very end."
                show bree doggy cuminass ahegao with hpunch
                $ bree.love += 1
                "And that's just what I do, enjoying every second of my orgasm."
                with hpunch
                "Moments later I get a second helping of pleasure as [bree.name] cums too."
                with hpunch
                "The muscles inside her body squeezing my cock as she shudders from head to toe."
            elif _return == 'anal_outside':
                "I could just keep on going, but I feel the need to pull out before that happens."
                "And I manage to do that with a couple of seconds to spare."
                show bree doggy -anal cumshot ahegao with hpunch
                "I shoot my load over [bree.name]'s helpless form, showering her in cum."
                with hpunch
                pause 0.25
                with hpunch
                "Enjoying every second of my orgasm, I savour the sight."
                $ bree.sub += 1
                show bree doggy cumonass with hpunch
                "Moments later I get a second helping of pleasure as [bree.name] cums too."
                "The muscles inside her body making her shudder from head to toe."
            $ bree.flags.anal += 1
    if not bree_bj:
        "Thinking we're all done, I sink down onto the bed."
        "But then I see that [bree.name]'s very much awake."
        "And she's beckoning me to come forwards."
        "I move around so that I'm kneeling in front of [bree.name]."
        show bree doggy front -back -vaginal -anal -cumshot
        "And I pretty much shove my cock straight into her face."
        "[bree.name] smiles and nods."
        bree.say "Okay!"
        bree.say "A blowjob to finish things off!"
        "She licks her lips and leans forwards."
        "And at the same time, she takes hold of it with one hands."
        "[bree.name] closes her eyes as she parts her lips."
        show bree doggy suck normal
        "Which means she has to guide the tip into her mouth by feeling for it."
        "And I've got to admit I like the sight of her wrapping her lips around the head."
        "[bree.name] makes soft little moaning sounds as she starts to suck."
        "But these soon begin to increase in volume."
        "And at the same time, my feelings of pleasure increase too."
        show bree doggy scream
        "As [bree.name]'s head moves back and forth, it's my turn to get vocal."
        "I find that I can't keep from gasping as she works on me."
        "The fear of being discovered does nothing to silence me either."
        "[bree.name] begins to take my cock deeper into her mouth."
        show bree doggy normal
        "And I find myself wondering just how much she can take."
        menu:
            "Let's find out":
                "With that in mind, I lean forwards a little."
                "This doesn't seem to cause [bree.name] any problems."
                show bree doggy deep
                "She takes the extra length in with ease."
                "So I push further still, just to satisfy my curiosity."
                show bree doggy scream
                "This keeps on going until my cock is literally down [bree.name]'s throat."
                $ bree.sub += 1
                $ bree.love -= 1
                "She's giving me deep-throat, without any complaints too!"
            "Keep the pace":
                "I have no idea if [bree.name] can handle anything like deep-throat."
                "So I make doubly sure that she doesn't take it too deep."
                show bree doggy scream
                "That's not to say my cock isn't well in there."
                $ bree.love += 1
                "It's just not pushing down on [bree.name]'s tonsils, that's all!"
        "Suddenly I feel a change in the sensations from down there."
        "Before everything was building up."
        show bree doggy normal suck
        "But now I feel like it's going to explode!"
        menu:
            "Cum on her face":
                "Pulling my cock out of [bree.name]'s mouth, I take aim for her face."
                show bree doggy -suck
                "Which just so happens to have a look of genuine surprise on it."
                "And that makes what happens next all the more gratifying."
                show bree doggy ahegao cumshot with hpunch
                pause 0.25
                with hpunch
                "I shoot my load right at the target, spattering it all over [bree.name]'s face."
                with hpunch
                "Her mouth open, a good deal of it lands in her mouth too!"
                show bree doggy ahegao cumonface -cumshot
                "[bree.name] gasps and splutters as she struggles to swallow it down."
                "But I'm too busy smiling to be able to offer her any help."
            "Cum in her mouth":
                "I don't want to pull out, not when I'm so deep in [bree.name]'s mouth!"
                with hpunch
                "So I keep on going until I cum, shooting my load down her throat."
                with hpunch
                "[bree.name]'s eyes pop open, and she almost chokes on it."
                with hpunch
                "But through sheer force of will she makes herself swallow."
                show bree doggy cuminmouth ahegao
                "Though her eyes are watering from the effort, [bree.name] pulls it off."
                "And when she opens her mouth to gasp for air, there's no trace of it left."
    "Afterwards, I feel like I'm going to pass out from exhaustion."
    "But [bree.name] shoves my shoulder as she hops off the bed."
    scene bg bedroom3
    show bree normal blush naked
    with fade
    bree.say "What are you doing, [hero.name]?"
    bree.say "Did you forget where we are?!?"
    "Nodding as I remember that we were fucking in Sasha's room, I leap up."
    "Grabbing my clothes, I pull on as many as I can."
    "Then [bree.name] and I try to make Sasha's room look vaguely like it did when we found it."
    "That done we flee the scene of the crime, hoping that we evade detection."
    $ game.room = "bedroom3"
    scene bg black with dissolve
    return

label bree_zbox_penalty(sexperience_min=0):
    scene bg livingroom
    show bree b angry
    with fade
    bree.say "No!"
    bree.say "No way!"
    mike.say "Come on, [bree.name]..."
    mike.say "A deal's a deal."
    mike.say "We shook on it before we started playing!"
    mike.say "If you win, I buy you a takeout."
    mike.say "If I win, you put out for me."
    show bree b at startle
    "[bree.name] throws down her controller and it bounces off the living-room floor."
    show bree a
    "Then she crosses her arms over her chest and makes a pouting sound."
    show bree a annoyed
    bree.say "Okay, okay..."
    bree.say "Let's get it over with!"
    show bree evil blush topless with dissolve
    "Before I can say another word, [bree.name] starts pulling off her clothes."
    show bree naked with dissolve
    "Pretty soon she's naked and on her hands and knees in front of me."
    scene bree doggy
    show bree doggy livingroom noone
    with fade
    "[bree.name] looks over her shoulder at me, impatience written all over her face."
    bree.say "Well?"
    bree.say "What are you waiting for?"
    "I nod and hurry to strip off my own clothes too."
    "Luckily for us, Sasha's out for the rest of the day."
    "So this is my chance to make the most of my victory."
    "As soon as I'm naked, I shuffle up behind [bree.name]."
    show bree doggy -noone
    "I can already feel my cock getting hard."
    "So it looks like it's time to claim my winnings!"
    menu:
        "Fuck her ass" if bree.flags.anal >= 2 and hero.sexperience >= (sexperience_min + 5):
            "[bree.name]'s mood seems to improve somewhat as I put my hands on her waist."
            "I can hear her actually chuckling a little, and she even wiggles her butt!"
            "All of which makes me feel better about collecting on the bet we made."
            "It helps to get my cock all the way up too, meaning that I'm ready to go."
            "I start slow and gentle, just pushing my cock between [bree.name]'s thighs."
            "But as soon as it touches her lips a little, she giggles and shivers."
            bree.say "Ooh..."
            show bree doggy scream
            bree.say "That feels nice!"
            "But then I adjust my angle and change my target."
            "[bree.name] instantly seems to understand what's going on."
            bree.say "Hey!"
            show bree doggy anal normal
            bree.say "I didn't say you could do that!"
            bree.say "Get that thing away from my ass!"
            "It's already too late for her to do anything about it."
            "Even before [bree.name]'s finished protesting, I'm already in there."
            "And soon her expression changes as I sink into her ass."
            bree.say "Mmm..."
            bree.say "Oh, [hero.name]..."
            show bree doggy scream
            bree.say "That feels so good!"
            "[bree.name]'s going to the next level with her pleas."
            "And I feel the irresistible urge to do the same."
            "Pushing harder still, I feel her ass begin to open for me."
            bree.say "Yeah..."
            bree.say "Oh yeah..."
            bree.say "Go deeper - please!"
            "It's not like [bree.name] needs to ask."
            "Because nothing could hold me back from doing exactly that!"
            "The muscles of her ass are parting for me, so I'm going in!"
            "[bree.name]'s words turn into pure moans of pleasure as it happens."
            "And by the time I can go no deeper, she's lost the power of speech."
            "All she can do is moan and nod her head."
            "Like an animal begging for what she wants."
            "And even that begins to become impossible as I get into my stride."
            "By now I'm thrusting into [bree.name] for all I'm worth."
            show bree doggy normal speed
            "Gaining force and speed with each movement of my body."
            "I have to hold onto [bree.name]'s haunches as tightly as possible."
            "And I can see my fingers sinking into the soft flesh as I do so."
            "Because the way my thighs are slapping into her buttocks is rocking her body."
            "If I let go, I just know that she'd go flying forward and land on her face!"
            "But then I see [bree.name] has her hands clenched almost into fists."
            "She's grasping handfuls of the carpet."
            "And it's like she's holding on for dear life!"
            show bree doggy scream
            bree.say "H...h..."
            bree.say "Hard...harder..."
            bree.say "Fuck...me...harder!"
            "I don't know what takes me more by surprise."
            "The fact that [bree.name] actually managed to regain the power of speech."
            "Or that she did so to demand that I fuck her harder than I already am!"
            "Either way, I feel instantly compelled to do all I can to obey."
            "Which means almost throwing myself at her in an effort to make it happen."
            "[bree.name]'s howling by now, her entire body shaking too."
            "And the change in pace is enough to finish me off as well."
            call cum_reaction (bree, 'anal', sexperience_min) from _call_cum_reaction_63
            if _return == "anal_inside":
                "There's no need to stop what I'm doing."
                "And that's the massive bonus of putting it in [bree.name]'s ass."
                "I'm at the end of one of those huge thrusts when it happens."
                show bree doggy cuminass ahegao with hpunch
                $ bree.love += 1
                "So I shoot my load as deep into [bree.name] as possible."
                with hpunch
                "This seems to have an instant effect, making her begin to cum too."
                with hpunch
                "[bree.name] bucks and twists on the end of my cock."
                "And once it's all over, she slides off me and collapses onto the ground."
            elif _return == "anal_outside":
                "I want to pull out of [bree.name] before I lose it."
                show bree doggy -anal cumshot ahegao
                "Just for the sake of being able to mark my territory."
                "So after one last thrust, I drag myself out of her."
                "This seems to have an instant effect, making her begin to cum too."
                $ bree.sub += 1
                show bree doggy cumonass with hpunch
                pause 0.15
                with hpunch
                pause 0.20
                with hpunch
                "[bree.name] bucks and twists on the end of my cock while I shoot my load over her back."
                "And once it's all over, she slides off me and collapses onto the ground."
            $ bree.flags.anal += 1
        "Fuck her pussy":
            "[bree.name]'s mood seems to improve somewhat as I put my hands on her waist."
            "I can hear her actually chuckling a little, and she even wiggles her butt!"
            "All of which makes me feel better about collecting on the bet we made."
            "It helps to get my cock all the way up too, meaning that I'm ready to go."
            call check_condom_usage (bree) from _call_check_condom_usage_29
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show bree doggy condom
            "I start slow and gentle, just pushing my cock between [bree.name]'s thighs."
            "But as soon as it touches her lips a little, she giggles and shivers."
            bree.say "Ooh..."
            bree.say "That feels nice!"
            "I step things up a little, stroking the head up and down."
            "As I do so, I can feel [bree.name]'s pussy beginning to get wet."
            "The sensation serves to turn me on even more, making me push harder."
            bree.say "Mmm..."
            bree.say "Oh, [hero.name]..."
            bree.say "Stop teasing me!"
            "[bree.name]'s going to the next level with her pleas."
            "And I feel the irresistible urge to do the same."
            "Pushing harder still, I feel her pussy begin to open for me."
            bree.say "Yeah..."
            show bree doggy vaginal scream
            bree.say "Oh yeah..."
            bree.say "Put it in me - please!"
            "It's not like [bree.name] needs to ask."
            "Because nothing could hold me back from doing exactly that!"
            "The lips of her pussy are parting for me, so I'm going in!"
            "[bree.name]'s words turn into pure moans of pleasure as it happens."
            "And by the time I can go no deeper, she's lost the power of speech."
            "All she can do is moan and nod her head."
            show bree doggy normal
            "Like an animal begging for what she wants."
            "And even that begins to become impossible as I get into my stride."
            "By now I'm thrusting into [bree.name] for all I'm worth."
            "Gaining force and speed with each movement of my body."
            "I have to hold onto [bree.name]'s haunches as tightly as possible."
            "And I can see my fingers sinking into the soft flesh as I do so."
            "Because the way my thighs are slapping into her buttocks is rocking her body."
            "If I let go, I just know that she'd go flying forward and land on her face!"
            "But then I see [bree.name] has her hands clenched almost into fists."
            "She's grasping handfuls of the carpet."
            "And it's like she's holding on for dear life!"
            show bree doggy scream
            bree.say "H...h..."
            bree.say "Hard...harder..."
            bree.say "Fuck...me...harder!"
            "I don't know what takes me more by surprise."
            "The fact that [bree.name] actually managed to regain the power of speech."
            "Or that she did so to demand that I fuck her harder than I already am!"
            "Either way, I feel instantly compelled to do all I can to obey."
            "Which means almost throwing myself at her in an effort to make it happen."
            "[bree.name]'s howling by now, her entire body shaking too."
            "And the change in pace is enough to finish me off as well."
            call cum_reaction (bree, 'vaginal', 1) from _call_cum_reaction_64
            if _return == "vaginal_condom":
                "There's no need to stop what I'm doing."
                "And that's because we remembered to use a condom."
                "I'm at the end of one of those huge thrusts when it happens."
                with hpunch
                "So I shoot my load as deep into [bree.name] as possible."
                $ bree.love += 1
                with hpunch
                "This seems to have an instant effect, making her begin to cum too."
                show bree doggy ahegao with hpunch
                "[bree.name] bucks and twists on the end of my cock."
                "And once it's all over, she slides off me and collapses onto the ground."
            elif _return == "vaginal_outside":
                "I need to pull out of [bree.name] before I lose it."
                "And that's because we didn't bother to use a condom."
                show bree doggy -vaginal
                "So after one last thrust, I drag myself out of her."
                "This seems to have an instant effect, making her begin to cum too."
                show bree doggy cumshot ahegao with hpunch
                $ bree.love += 1
                pause 0.15
                with hpunch
                pause 0.25
                with hpunch
                "[bree.name] bucks and twists on the end of my cock while I shoot my load over her back."
                show bree doggy cumonass -cumshot
                "And once it's all over, she slides off me and collapses onto the ground."
            elif _return == "vaginal_inside_pill":
                bree.say "Don't stop..."
                bree.say "I'm on the pill!"
                "I silently thank [bree.name] for the timely reminder."
                "I'm at the end of one of those huge thrusts when it happens."
                with hpunch
                "So I shoot my load as deep into [bree.name] as possible."
                show bree doggy cuminpussy ahegao with hpunch
                "This seems to have an instant effect, making her begin to cum too."
                with hpunch
                "[bree.name] bucks and twists on the end of my cock."
                $ bree.love += 2
                "And once it's all over, she slides off me and collapses onto the ground."
            elif _return == "vaginal_inside_pregnant":
                bree.say "Don't stop..."
                bree.say "I'm already pregnant!"
                "I silently thank [bree.name] for the timely reminder."
                "I'm at the end of one of those huge thrusts when it happens."
                with hpunch
                "So I shoot my load as deep into [bree.name] as possible."
                with hpunch
                "This seems to have an instant effect, making her begin to cum too."
                show bree doggy cuminpussy ahegao with hpunch
                "[bree.name] bucks and twists on the end of my cock."
                $ bree.love += 2
                "And once it's all over, she slides off me and collapses onto the ground."
            elif _return == "vaginal_inside_mad":
                bree.say "Please stop..."
                bree.say "Don't come in me!"
                "[bree.name]'s sudden demand takes me completely by surprise."
                "I'm at the end of one of those huge thrusts when it happens."
                with hpunch
                "So I shoot my load as deep into [bree.name] as possible."
                show bree doggy cuminpussy ahegao with hpunch
                "This seems to have an instant effect, making her begin to cum too."
                with hpunch
                "[bree.name] bucks and twists on the end of my cock."
                $ bree.love -= 5
                $ bree.impregnate()
                "And once it's all over, she slides off me and collapses onto the ground."
                "Which leaves me to begin fretting over what we just did."
            elif _return == "vaginal_inside_happy":
                bree.say "Don't stop..."
                bree.say "Please come in me!"
                "[bree.name]'s sudden demand takes me completely by surprise."
                "I'm at the end of one of those huge thrusts when it happens."
                with hpunch
                "So I shoot my load as deep into [bree.name] as possible."
                show bree doggy cuminpussy ahegao with hpunch
                "This seems to have an instant effect, making her begin to cum too."
                with hpunch
                "[bree.name] bucks and twists on the end of my cock."
                $ bree.love += 5
                $ bree.impregnate()
                "And once it's all over, she slides off me and collapses onto the ground."
                "Which leaves me to begin fretting over what we just did."
    $ bree.sexperience += 1
    return

label get_bree_lapdance:
    $ game.room = "stripclub"
    scene bree lapdance
    show bree lapdance nonpc
    with fade
    "The strip club is normally one of those places where I go on my own and in secret."
    "Or else I'm there with a bunch of like-minded guys that aren't going to judge me."
    "But tonight I'm here with something that feels pretty different in mind."
    "And I'm sitting alone in one of the private booths, waiting for a lap-dance to begin."
    "I know that sounds like a great position to be in, right?"
    "And yeah, I'm super excited about what's about to happen."
    "But there's also a part of me that can't help being nervous too."
    "Because all the other times I've been here, I never knew the girl that was giving me a dance."
    "Sure, maybe someone told me their name or we swapped a couple of words in a bar here or there."
    "But this time it's different."
    "This time the girl in question is someone that I know well."
    "And after this, I don't know if I'll ever be able to look at her the same way again."
    $ game.play_music("music/roa_music/city_nights.ogg")
    "Suddenly music begins to play, making me look up."
    "It's a tune that I vaguely recognise, but can't put a name to."
    "Mainly because all of my attention is focussed right in front of me."
    bree.say "Hi, [hero.name]..."
    bree.say "Are you ready for your private dance?"
    "All I can do is nod, my voice dying in my throat."
    "[bree.name]'s only got her head and one arm through the curtains."
    "But she's already leaving me speechless at the mere sight of her."
    "She seems to notice the effect she's having on me."
    "And she giggles, then slides a leg through the curtains too."
    bree.say "Oh my!"
    bree.say "I'll take that as a yes..."
    scene bg black
    show bree lapdance
    with fade
    "With that, she slides through the curtains and into the booth."
    "And sure, I've lived in the same house as [bree.name] for a while now."
    "And she's been slobbing around the place in a T-shirt and underwear in the past."
    "But I don't think that I've ever seen her like this in all that time."
    "My eyes follow [bree.name] as though they're on strings tied to her body."
    "But almost no other part of me seems to be able to move at the same time."
    "All I can do is sit there and watch as [bree.name]'s body moves like a dream."
    "Her breasts bounce and her buttocks bob as she turns."
    "But I swear that my eyes are on her face as often as her curves."
    "There's just something different about those familiar features."
    "Something that I've never seen expressed on them before now."
    "A quality that's only coming out now that she's dancing for me."
    "And I think that [bree.name]'s aware of it too."
    "Her smile is knowing and she has a twinkle in her eye."
    "Like she knows that I'm helpless in the palm of her hand right now."
    "[bree.name] comes closer, leaning over me as she moves."
    "Her body is now close enough for me to touch."
    "And more than once I think she's going to brush my face."
    "But every time she turns away and twists out of reach."
    "By now my hands are clenched on the arms of my chair."
    "I can imagine my nails gouging into the material."
    "But I know how these places work, that it's look and don't touch."
    "The state of my nerves must be pretty obvious though."
    "As [bree.name] cocks her head on one side as she regards me."
    bree.say "Why so tense, [hero.name]?"
    bree.say "You almost look like you're afraid of me!"
    bree.say "Oh...I think I see the problem."
    "[bree.name] chuckles as she leans over me."
    "She takes hold of my wrists, pulling them off the arms of the chair."
    bree.say "Touching here is strictly at the discretion of the dancers."
    bree.say "And you certainly get a pass when it comes to me!"
    show bree lapdance grope
    "That said, [bree.name] places my hands on her body."
    "Touching her skin feels almost electric to me."
    "Like I'm getting little shocks all the time we're in contact."
    "And the smile that spreads across her face as I touch her..."
    "Oh man...I can feel that making me harder by the second!"
    "All the time that my hands are on her, [bree.name] keeps dancing."
    "Moving so that they pass over different parts of her body."
    "Until finally she turns her back to me."
    "Then she sits down on my lap."
    show bree lapdance finger
    "[bree.name] makes sure my arms are around her waist."
    "And then she grinds her ass down into my lap."
    show bree lapdance pleasure
    bree.say "Oh my!"
    bree.say "Aren't you a big boy?"
    bree.say "And that's all because of me?"
    bree.say "Oh, [hero.name], I had no idea you felt that way!"
    "[bree.name] giggles and proceeds to wiggle her ass even more."
    "And there's nothing I can do to prevent what happens next."
    "Because it'd take an army of men to drag her off me."
    with vpunch
    mike.say "Oh fuck..."
    with vpunch
    mike.say "[bree.name]!"
    with vpunch
    "[bree.name] must know that she's made me cum in my shorts."
    "I have no idea if she can feel anything but my movements."
    "Though she must be able to guess what those mean."
    bree.say "Oh dear!"
    bree.say "Did I make you have a little accident?"
    bree.say "Well don't worry, [hero.name]."
    bree.say "There are wet-wipes over there."
    bree.say "So you can get yourself all cleaned up!"
    $ bree.sub -= 1
    "With that she hops off my lap and onto her feet."
    "[bree.name] pauses long enough to blow me a kiss."
    show bree lapdance nonpc with dissolve
    "And then she disappears through the curtains again."
    scene bg stripclub with fade
    "Once I'm alone, I sink down into the chair."
    "My arms fall to my sides and my head rolls to one side."
    "I know that I should take [bree.name]'s advice."
    "That I should pull myself together and get cleaned up."
    "But the problem is that she's just pretty much blown my mind!"
    "And another thing - how in the hell am I supposed to face her when we both get back home!"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
