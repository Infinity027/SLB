init python:
    Event(**{
    "name": "samantha_hottub_sex_male",
    "label": "samantha_hottub_sex_male",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("date_hot_tub_home")),
        PersonTarget(samantha,
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
    "name": "fuck_samantha",
    "display_name": "Fuck",
    "label": "ACTIVE_GIRL_fuck_ROOM",
    "conditions": [
        IsTimeOfDay("evening"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            HasStamina(),
            ),
        PersonTarget(samantha,
            IsActive(),
            InHarem('home'),
            MinStat("love", 150),
            MinStat("sexperience", 2),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })

    InteractActivity(**{
    "name": "fuck_samantha_beach",
    "display_name": "Fuck",
    "label": "ACTIVE_GIRL_fuck_ROOM",
    "duration": 1,
    "conditions": [
        IsHour(14, 18),
        HeroTarget(
            IsGender("male"),
            IsRoom("beach", "date_beach", "date_nudistbeach"),
            HasStamina(),
            ),
        PersonTarget(samantha,
            IsActive(),
            MinStat("love", 150),
            MinStat("sexperience", 2),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })

label samantha_hottub_sex_male:
    $ game.active_date.clothes = "swimsuit"
    $ CONDOM = False
    scene bg pool
    "I have to admit that getting Sam into the hot-tub with me was one of those things on my bucket list."
    "Well, maybe that's an overstatement, but in all the time we lived together, we never took a dip together."
    "I'd see her in there on her own and want to suggest that I join her, yet not be able to summon the courage."
    "Or worse still, I'd see her in there with Ryan and feel a surge of jealousy at the look on his smug face."
    show samantha swimsuit at left with easeinleft
    "But now there's nothing to stop us relaxing in the luxurious, bubbling water of the tub together."
    "And when I suggest as much to her, Sam seems up for it too!"
    show samantha at center with ease
    "So that's how I find myself sitting in the hot-tub, trying to look casual and innocent."
    "Which is hard when you also have to watch Sam lowering herself into the water at your side."
    "Do I even have to mention that she looks like a million dollars in her swimsuit?"
    hide samantha
    show hottub samantha
    with fade
    "By the time she's sitting down, a certain part of my anatomy is sitting up!"
    samantha.say "Mmm..."
    samantha.say "I really missed this when I moved out!"
    samantha.say "We talked about getting one."
    samantha.say "But there just wasn't room at the new place..."
    "Sam trails off as she sees the expression on my face."
    "I guess I can't help looking awkward when she talks about her and Ryan."
    "It's dumb of me, I know, but there it is."
    samantha.say "Oh, I'm sorry, [hero.name]."
    samantha.say "I guess I'm so used to thinking of this place..."
    samantha.say "Well, you know what I mean, right?"
    if samantha.flags.nickname == "cupcake":
        mike.say "It's okay, Cupcake, really."
    else:
        mike.say "It's okay, Sam, really."
    mike.say "I need to get over it, you know?"
    mike.say "We can't erase the past."
    if samantha.flags.engaged or "samantha_event_B01" not in DONE:
        menu:
            "Let's not talk about him right now.":
                mike.say "Let's not talk about him right now."
                samantha.say "Okay. New topic."
            "Tell me you're sure about this." if hero.charm >= 50:
                mike.say "Tell me you're sure about this."
                if samantha.flags.engaged:
                    samantha.say "I'm sure. I know what this means."
                else:
                    samantha.say "I'm sure. I want this."
                $ samantha.love += 1
    "Sam smiles at this and nods with a little sadness."
    "But then her smile seems to become more hopeful."
    "She reaches out and puts her hands atop mine."
    samantha.say "Sure, [hero.name]."
    samantha.say "But that doesn't mean we can't make new memories."
    samantha.say "Better ones too!"
    "I can't help returning the smile as Sam edges closer to me."
    "Soon she's nestled against my side, leaning in to whisper in my ear."
    samantha.say "You know, [hero.name]."
    samantha.say "There's one thing I never did in here..."
    if samantha.flags.nickname == "cupcake":
        mike.say "What was that, Cupcake?"
    else:
        mike.say "What was that, Sam?"
    "Then I feel her hand slipping into my trunks."
    mike.say "Oh..."
    mike.say "Oh, I get it!"
    menu:
        "Say 'please'." if samantha.sub >= 25:
            mike.say "Say 'please'."
            if samantha.sub >= 50:
                samantha.say "Please."
                $ samantha.sub += 1
            else:
                samantha.say "Don't push your luck."
                $ samantha.love -= 2
        "Tell me how you want it.":
            mike.say "Tell me how you want it."
            if samantha.sub <= 20:
                samantha.say "Close. Gentle. I want to feel you."
            else:
                samantha.say "Deep. Hard. Make me remember."
        "Turn around.":
            mike.say "Turn around."
            if samantha.sub >= 50:
                samantha.say "Yes."
                $ samantha.love += 1
            elif samantha.sub <= 25:
                samantha.say "Don't push your luck."
                $ samantha.love -= 1
            else:
                samantha.say "Bossy. I like it."
    show hottub sex male samantha outside with fade
    call samantha_dick_reactions from _call_samantha_dick_reactions
    "Holding onto my already hard cock, Sam turns her back to me."
    "She leans against the side of the tub, lifting her ass out of the water."
    "And then she shakes it in a way that says more than words ever could."
    "I don't need to be told what to do next, especially since she still has a hold of me!"
    "I follow Sam's lead, instinctively reaching out to grab hold of her at the waist."
    "She pushes her ass into me then, grinding it into my groin."
    samantha.say "Like I said, [hero.name], we're making memories."
    samantha.say "So you better fuck me hard, yeah?"
    samantha.say "Hard enough that I can't forget the feeling!"
    "By now I'm getting so excited that all I can do is nod."
    "And my hand is already exploring between Sam's thighs."
    "She giggles as I use the other hand to pull down my trunks."
    show hottub sex male samantha inside
    "A few seconds later, the giggles turn into a sensual sigh."
    "I can't help letting out a moan too, as I feel myself pushing into her."
    "Sam's at that halfway point as I part the lips of her pussy."
    "She's willing to be persuaded, but not surrendering without a fight."
    "Which means that every inch I gain comes with an intense sensation."
    "Sam seems to urge me on without saying a word."
    "She nods as she gazes back over her shoulder."
    "The look in her eyes telling me that she's loving it as much as I am."
    if samantha.sub >=50:
        mike.say "Good girl."
        samantha.say "Don't stop."
        $ samantha.sub += 1
    elif samantha.sub >=25:
        mike.say "You feel unbelievable."
        samantha.say "Keep going."
    "Knowing that Sam's getting off on my efforts only makes me try harder."
    "And soon enough she's practically forced up against the edge of the tub."
    "All that's keeping her from falling out is the fact that I'm so deep into her."
    "I don't want to push too hard or too far."
    "But at the same time I'm determined to make this a moment Sam will never forget."
    "And so all I can do is listen as closely as possible to the sounds she makes."
    "That and trust to the fact that I know her well enough to pull it off."
    "Sam certainly seems to like what I'm doing to her."
    "She's moving in time with me, riding my cock like a jockey on a horse!"
    if samantha.flags.toldpreg:
        "Her free hand drifts to her belly for a heartbeat; the sight makes something fierce and protective flare in my chest."
    elif samantha.flags.NPCpregnancy == "ryan":
        "Her free hand drifts to her belly for a heartbeat."
    "In fact, I think I can feel her starting to twitch on the end of it."
    "I think we're both about to cum!"
    call cum_reaction (samantha, 'vaginal', 1) from _call_cum_reaction_150
    if _return == "vaginal_outside":
        show hottub sex male outside
        if game.days_played%2 == 1:
            "I drag in a breath and yank myself free just in time, hot slickness striping her lower back."
        else:
            "I mean to hold on a second longer, but the wave crests and I spill across her back in shuddering pulses."
        show hottub sex male cumshot with hpunch
        $ samantha.sub += 1
        with hpunch
        "And she seems to cum at the same time, shuddering as the sensation overtakes her."
    else:
        "I'm so deep inside of Sam now, and she's pressed so hard against the edge of the tub."
        "There's no way I can do anything other than keep right on going to the end."
        show hottub sex male cumshot with hpunch
        $ samantha.love += 1
        "That means I cum inside of Sam with all of the force I've been using to fuck her."
        show hottub sex male ahegao with hpunch
        "And the sensation of me bursting deep in her pushes her over the edge too."
        with hpunch
        "She cums almost a second after me, release coming for us both at the same time."
    hide hottub
    show hottub samantha
    with fade
    "Sam clings to me in the moments afterwards, shivering as the aftershocks hit her."
    "She chuckles to herself a little, nestling her head against my chest."
    if samantha.flags.toldpreg:
        "She touches her baby bump."
        samantha.say "That's ours."
        if samantha.sub >= 50:
            mike.say "Mine."
            samantha.say "Yours."
            $ samantha.sub += 1
        else:
            mike.say "Ours."
            $ samantha.love += 1
    elif samantha.flags.NPCpregnancy == "ryan":
        samantha.say "Hold me a second longer."
        mike.say "I've got you."
    else:
        if samantha.flags.nickname == "cupcake":
            mike.say "Hey, Cupcake."
        else:
            mike.say "Hey, Sam."
    mike.say "What's so funny?"
    samantha.say "Oh, nothing much."
    samantha.say "Just that I'll never be able to look at this tub the same way again!"
    samantha.say "Or without thinking of having you inside of me..."
    if "samantha_event_B01" not in DONE:
        menu:
            "We shouldn't make a habit of this.":
                mike.say "We shouldn't make a habit of this."
                samantha.say "I know."
                $ samantha.love += 1
            "Tell me you'll call me.":
                mike.say "Tell me you'll call me."
                samantha.say "I will."
    elif samantha.flags.engaged:
        menu:
            "Are you okay with this?":
                mike.say "Are you okay with this?"
                samantha.say "Right now? Yes."
                $ samantha.love += 1
            "Let’s keep this our secret.":
                mike.say "Let’s keep this our secret."
                samantha.say "Our secret."
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ samantha.sexperience += 1
    $ game.active_date.clothes = None
    return

label samantha_fuck_livingroom:
label samantha_fuck_kitchen:
label samantha_fuck_pool:
label samantha_fuck_bedroom1:
label samantha_fuck_bedroom2:
label samantha_fuck_bedroom3:
label samantha_fuck_bedroom4:
label samantha_fuck_bedroom5:
label samantha_fuck_bedroom6:
label samantha_fuck_secondfloor:
label samantha_fuck_home:
    $ game.play_music("music/roa_music/city_nights.ogg")
    show samantha
    mike.say "Hey, wanna come and have fun?"
    samantha.say "Sure."


    if samantha.is_visibly_pregnant:
        mike.say "Let's take it slow tonight."
        samantha.say "I like that."
    elif samantha.sub >= 50:
        mike.say "You know who's in charge tonight."
        samantha.say "Yes."
        $ samantha.sub += 1
    elif samantha.flags.engaged:
        mike.say "Keep this just between us."
        samantha.say "We shouldn't make a habit of it."
    if Harem.find(samantha, name='home'):
        call home_harem_fuck_choices ('samantha') from _call_home_harem_fuck_choice_3
    else:
        call samantha_fuck_date_male from _call_samantha_fuck_date_4
    return

label samantha_fuck_date_male(location="hero"):
    $ game.play_music("music/roa_music/city_nights.ogg")
    $ FACIAL = ""
    $ game.room = "livingroom"
    scene bg livingroom
    show samantha
    play music "music/roa_music/the_one.ogg" loop fadeout .5 fadein .5


    if game.week_day % 3 == 0 and hero.sexperience >= 20 and samantha.sexperience >= 1:
        call samantha_fuck_date_cunnilingus_intro from _call_samantha_fuck_date_cunnilingus_intro
        call samantha_fuck_date_cunnilingus from _call_samantha_fuck_date_cunnilingus
        "Now I need more."
    else:
        call samantha_fuck_date_intro_male (location) from _call_samantha_fuck_date_intro_male


    call samantha_dick_reactions from _call_samantha_dick_reactions_5


    call samantha_fuck_date_foreplay_male from _call_samantha_fuck_date_foreplay_male

    $ skip_to_sleep = _return




    if not skip_to_sleep:
        call samantha_fuck_date_choices_male from _call_samantha_fuck_date_choices_male


        call handle_npc_leaving (samantha, _return) from _call_handle_npc_leaving_22
        if _return:
            return

        scene bg bedroom1
        show samantha naked
        with fade
        if samantha.flags.engaged:
            "Her engagement ring throws a sharp little star on the wall whenever she moves her hand; she twists it without thinking, breath still ragged."
        "Both of us lay collapsed upon the bed, an entire session where I was in full control spending both of us."
        if samantha.is_visibly_pregnant and not samantha.flags.NPCpregnancy == "ryan":
            "She guides my hand to her belly and smiles, breath still shaky; the soft curve rises and falls under my fingers."
            samantha.say "Ours."
            mike.say "Ours."
            $ samantha.love += 1
        elif samantha.flags.NPCpregnancy == "ryan":
            "She exhales and squeezes my fingers, protective and warm, her palm lingering over the gentle swell of her stomach."
            samantha.say "Hold me a second longer."
            mike.say "I've got you."
        if randint(1, 100) <= 25:
            "She smiles as she turns towards me, and gives me a great hug, pressing her chest up against my body."
            show samantha close naked
            if samantha.flags.engaged:
                "Her wedding ring presses lightly into my shoulder—tiny, cool, real."
            samantha.say "Oh, did you enjoy yourself?"
            menu:
                "You were great.":
                    mike.say "You bet, I did! You were great!"
                    samantha.say "Oh, you're so wonderful. Thank you."
                    "She says, sighing, nuzzling up to me and just enjoying our time together."
                    $ samantha.love += 1
                "Be honest; we can do better.":
                    mike.say "Actually, it wasn't all that good, really."
                    show samantha surprised
                    samantha.say "W... what?"
                    mike.say "Yeah, you were just so bland, not wanting to please yourself, just wanting to please me."
                    mike.say "Where's the spirit?"
                    samantha.say "I..."
                    show samantha sad
                    "She goes silent."
                    mike.say "Well, that's that, I guess, unless you want to do something else...?"
                    samantha.say "I'm... I'm going to have to think about it."
                    "She turns away, curling up in my bed."
                    $ samantha.love -= 5
    hide samantha
    call samantha_sleep_date_fuck (location) from _call_samantha_sleep_date_fuck_2
    return

label samantha_fuck_date_intro_male(location="hero"):
    if not samantha.sexperience:
        "Sam smiles with a sort of nostalgic whimsy as she casually strolls around my room."
        "Her hands behind her back, humming to herself a little."
        if samantha.flags.engaged:
            "When she lifts her hand to tuck her hair, a wedding ring flashes, habit makes her thumb worry the band for a heartbeat before she lets her hand fall."
        samantha.say "Oh, [hero.name], it's like I never even moved. This room is just like before."

        if "luxury_bed" in hero.inventory:
            mike.say "Hey, I got a new bed!"
            "She giggles."
            samantha.say "Oh, silly, I meant just how you decorated. You haven't changed one bit."
            mike.say "I thought that's one reason you decided to go out with me."
            "She nods at that, her smile warm and genuine."
            samantha.say "Well, you aren't wrong."
            samantha.say "But I also chose you because you are a solid foundation in this crazy world."
            samantha.say "And you know what?"
            samantha.say "I think you need a nice reward for being there for me during the tough times."

        if samantha.flags.nickname == "cupcake":
            mike.say "Well, Cupcake, we're here. What would you like to do?"
        else:
            mike.say "Well, Sam, we're here. What would you like to do?"
        samantha.say "Oh, [hero.name]."
        samantha.say "Such a gentleman."
        samantha.say "But we're in your house, so we get to do what you want."
        samantha.say "Though... let me give you something to think about first."
        show samantha naked
        if samantha.flags.engaged:
            "Her wedding band stays on as she undresses; the slim circle of gold gleams against her skin, a pale indentation beneath it betraying how rarely she takes it off."
        if samantha.is_visibly_pregnant:
            "Her belly is round and warm beneath my gaze, a faint line running from her navel downward; she cradles it as if the gesture is instinct."

        if samantha.flags.engaged:
            "She pauses; for a heartbeat, guilt and hunger flicker across her face."
            menu:
                "Tell me you're sure about this.":
                    mike.say "Tell me you're sure about this."
                    samantha.say "I'm sure."
                "Let's keep us separate from the rest.":
                    mike.say "Let's keep us separate from the rest."
                    samantha.say "Then take me and don't look back."
        if samantha.is_visibly_pregnant and not samantha.flags.NPCpregnancy == "ryan":
            "She draws my palm to her belly and kisses my wrist."
            samantha.say "This is ours."
        if game.days_played % 2 == 1:
            menu:
                "I want to be gentle with you.":
                    mike.say "I want to be gentle with you."
                    samantha.say "Then be gentle with me."
                    $ samantha.love += 1
                "I want you, all of you.":
                    mike.say "I want you, all of you."
                    samantha.say "Then take me."
                    $ samantha.sub += 1
        samantha.say "Sorry if the piercings look tacky..."
        samantha.say "Ryan... he had me get them."
        "Having lived with her for a bit, I could get glimpses here and there if I wanted, but to be the reason she undresses, hands behind her back to keep her arms from obstructing my view, that is a new feeling..."
        menu:
            "I like them.":
                mike.say "I like them."
                samantha.say "Oh, I'm so glad you like them!"
                "She says, bouncing gently, which causes those wonderful breasts to jiggle delightfully."
                $ samantha.love += 1
            "Lose them for me.":
                mike.say "Yeah, maybe you should get rid of them."
                mike.say "Start fresh. Don't worry, though, I'll be gentle around there."
                samantha.say "Okay, [hero.name]. For you, I'll get rid of them."
                python:
                    for k,v in samantha.piercings.items():
                        if v.worn:
                            v.worm = False
        "I get undressed myself, knowing we won't be needing clothes where we're going."
        call samantha_dick_reactions from _call_samantha_dick_reactions_1
        samantha.say "Just let me know what you want, and I'll do it for you."
        mike.say "Come here. Let's see you use that mouth for something else other than praising me."
        "I lay back on the bed, my hands behind my head as I watch her."
        mike.say "Come and get my cock."
        hide samantha
        show samantha bj open
        with fade
        "She brushes her fingers gently up along my thighs. Her large breasts squish against the mattress."
        "As she looks down over my already hardened shaft, ready to take her mouth."
        "But as she smiles down at it, she then looks up to me, the face she makes showing how her shy side melts away to a look of pure excitement and joy."
        samantha.say "[hero.name], let's make this a little more interesting than a simple little blowjob."
        "Just as she says this, she lifts up a bit, cupping her hands under her motherly breasts and sliding my cock in between those warm and soft tits of hers."
        if samantha.flags.engaged:
            "Her wedding ring shines every time her hands squeeze together around me, a tiny strobe of light that shouldn't be this hot."
        if samantha.is_visibly_pregnant:
            "A soft bead of milk pearls at one nipple when the pressure shifts; she blushes, then breathes out when I don't stop her."
        samantha.say "How does this feel? Do you like it?"
        "As she squeezes herself, the swollen and filled jugs swish around my cock with a heavier weight."
    else:
        $ res = game.days_played % 6
        if res == 0:
            $ game.room = "bedroom1"
            scene bg bedroom1
            show samantha
            with fade
            if samantha.flags.nickname == "cupcake":
                mike.say "Well, Cupcake, we're here. What would you like to do?"
            else:
                mike.say "Well, Sam, we're here. What would you like to do?"
            samantha.say "Oh, [hero.name]."
            samantha.say "Such a gentleman."
            samantha.say "But we're in your house, so we get to do what you want."
            samantha.say "Though... let me give you something to think about first."
            show samantha naked
            if samantha.is_visibly_pregnant:
                "Samantha's already bountiful breasts swell with the burden of motherhood."
                "The round, pregnant shape of her belly is almost enough to make me realize how amazing she looks."
                if samantha.flags.engaged:
                    "She braces on the mattress; the band on her finger taps the headboard with a tiny click before she steadies herself."
                samantha.say "You like it, [hero.name]?"
                samantha.say "This is all for you and all because of you."
                "She caresses her stomach, looking downward over her body."
                samantha.say "I'll be a perfect mother, if that is what you want me to be, but for now, I'll be your pregnancy fetish."
                "Well, then! I can't say no to that. Let's get going!"
                $ samantha.love += 1
                menu:
                    "Kiss her belly.":
                        mike.say "Come here."
                        "I kneel and kiss the soft curve of her stomach."
                        samantha.say "Do that again."
                        $ samantha.love += 1
                    "Eyes up here.":
                        mike.say "Eyes up here."
                        samantha.say "Then earn it."
            "I get undressed myself, knowing we won't be needing clothes where we're going."
            call samantha_dick_reactions from _call_samantha_dick_reactions_2
            samantha.say "Just let me know what you want, and I'll do it for you."
            mike.say "Come here. Let's see you use that mouth for something else other than praising me."
            "I lay back on the bed, my hands behind my head as I watch her."
            mike.say "Come and get my cock."
            hide samantha
            show samantha bj open
            with fade
            if samantha.is_visibly_pregnant:
                "Samantha takes a deep breath and slides down in between my legs, going a little slowly as she carefully tries to keep her baby safe from any harm."
            "She brushes her fingers gently up along my thighs. Her large breasts squish against the mattress."
            "As she looks down over my already hardened shaft, ready to take her mouth."
            "But as she smiles down at it, she then looks up to me, the face she makes showing how her shy side melts away to a look of pure excitement and joy."
            samantha.say "[hero.name], let's make this a little more interesting than a simple little blowjob."
            "Just as she says this, she lifts up a bit, cupping her hands under her motherly breasts and sliding my cock in between those warm and soft tits of hers."
            if samantha.flags.engaged:
                "Her wedding ring glints each time her hands press together around me; it's distracting in exactly the right way."
            "As she squeezes herself, the swollen and filled jugs swish around my cock with a heavier weight."
            if samantha.is_visibly_pregnant:
                "From her actions, little trickles of milk roll down, glistening her body and making a wet and sticky mess of my crotch."
        elif res == 1:
            "I'm practically bursting with excitement and anticipation as Sam and I make it back to my place."
            "I mean, can you really blame me?"
            "I held a torch for Sam all the time that I was living with her and Ryan."
            "And now I'm actually getting the chance to be with her myself."
            "Our date went really great too, which means I might just be in luck!"
            mike.say "Ah..."
            if samantha.flags.nickname == "cupcake":
                mike.say "Cupcake..."
            else:
                mike.say "Sam..."
            show samantha flirt
            "Sam gives me a knowing smile."
            "As if she can read my mind."
            samantha.say "Yeah, [hero.name]?"
            samantha.say "You got something to ask me?"
            mike.say "I...I was wondering if..."
            mike.say "Well...if you wanted to come to my room?"
            mike.say "I mean...you don't have to if you don't want to!"
            mike.say "We could just watch TV on the sofa or whatever..."
            "Sam reaches up and puts a single finger to my lips."
            if samantha.flags.engaged:
                "The wedding ring is cool against my mouth for a second before she pulls her hand away."
            show samantha normal
            samantha.say "Shut up, [hero.name]."
            samantha.say "You're babbling!"
            "The next thing I know, she's taken hold of my hand."
            "And she's leading me through the house towards my bedroom."
            "Of course, she knows the way."
            "And I'm more than happy to follow in her wake."
            "Sam pauses once she reaches my bedroom door."
            "Then she opens it and pulls me inside."
            $ game.room = "bedroom1"
            scene bg bedroom1
            show samantha
            with fade
            samantha.say "Mmm..."
            samantha.say "You know what..."
            samantha.say "I always had a little fantasy about this room."
            "As Sam closes the door behind me, I gape at what she's saying."
            mike.say "Y...you did?"
            mike.say "A fantasy about my room?!?"
            show samantha flirt
            "Sam gives me the most seductive smile imaginable."
            "One that's made all the more alluring by the look in her eyes."
            "A look that's pretty much smouldering with desire!"
            samantha.say "Oh yeah."
            samantha.say "It went a little like this..."
            "Sam turns her back on me and starts to walk towards the bed."
            show samantha normal
            "I hurry to follow, eager to hear all about this fantasy of hers."
            samantha.say "I used to wonder if I could slip out of bed while Ryan was sleeping."
            samantha.say "Then sneak all the way down here and into this room without waking you."
            samantha.say "You'd be laid on the bed, asleep and naked."
            "Sam pushes me towards the bed, catching me off-guard."
            "This means that I fall backwards onto the mattress."
            mike.say "Whoa!"
            samantha.say "Then I'd creep over to the bed and take off my clothes too..."
            "I stare up at Sam as she starts to strip off in front of me."
            show samantha topless with dissolve
            if samantha.flags.engaged:
                "Her wedding ring is the last thing to leave her before the rest does; she slides it onto the nightstand with a soft clink, eyes never leaving mine."
            "By now I'm pretty sure of where this is going."
            "So I start to strip-off too, trying to watch her at the same time."
            "Sam takes off one item of clothing at a time, tossing them to the floor."
            show samantha naked with dissolve
            "Needless to say I'm hard as a rock before she's finally naked."
            samantha.say "And I'd climb onto the bed..."
            "I hold my breath as Sam does just that."
            "She crawls on her hands and knees until she's atop me."
            "Then she straddles my thighs, leaning back and looking down."
            samantha.say "Then I'd take a hold of your cock, like this..."
            call samantha_dick_reactions from _call_samantha_dick_reactions_3
            show samantha flirt
            "The sensation of Sam grabbing me breaks the spell holding me still and silent."
            "I gasp as she squeezes the shaft, nodding my head with desperation."
            mike.say "Oh god!"
            "Sam laughs and smiles, clearly approving of my reaction."
            samantha.say "You like my little fantasy too, huh?"
            show samantha happy
            if samantha.flags.nickname == "cupcake":
                mike.say "Y...yeah, Cupcake!"
            else:
                mike.say "Y...yeah, Sam!"
            mike.say "I love it!"
        elif res == 2:
            "Sometimes I don't even need to say a word to Sam, I can just sense the mood she's in."
            "Like right now, we've just made it home from a date that went really well."
            "And she doesn't let go of my hand from the moment we step out of the taxi."
            "Instead she leads me into the house and makes straight for my bedroom!"
            $ game.room = "bedroom1"
            scene bg bedroom1
            show samantha
            with fade
            "Yeah, I know - it's not a very subtle signal!"
            "But there's no mistaking what she wants from me."
            "And I'm in as much of a hurry as she is to give it to her!"
            samantha.say "Come on, [hero.name]!"
            samantha.say "What are you waiting for?"
            show samantha flirt
            samantha.say "A written invitation?!?"
            if samantha.flags.nickname == "cupcake":
                mike.say "Okay, Cupcake, okay!"
            else:
                mike.say "Okay, Sam, okay!"
            mike.say "I'm going as fast as I can!"
            "Sam all but pushes me through the door and into my bedroom."
            "And the moment it closes, she hurries over to the bed."
            "At the same time she's already tearing off her clothes too!"
            show samantha naked with dissolve
            if samantha.flags.engaged:
                "She hesitates half a breath at her left hand, then keeps the wedding ring on; the band gives a tiny bright kiss of light each time her fingers move."
            "I hurry to follow, afraid that she'll get impatient with me."
            "Fucking hell - I don't think I've ever seen Sam this horny before!"
            samantha.say "Get over here!"
            samantha.say "I want you inside me!"
            if samantha.flags.nickname == "cupcake":
                mike.say "I'm coming, Cupcake..."
            else:
                mike.say "I'm coming, Sam..."
            mike.say "I just need to..."
            mike.say "WHOA..."
            "Before I can pull off the last of my clothes, Sam pounces."
            "She grabs hold of me, pulling me down onto the bed."
            "Then she shows surprising strength as she pins me down."
            samantha.say "I'm not playing, [hero.name]!"
            samantha.say "I want it!"
        elif res == 3:
            "I feel like I've hit a higher plane of being tonight, my date with Sam's gone that well."
            "Every place I've taken her, every joke I've cracked - hell almost every time I've opened my mouth!"
            "Sam's loved each and every one, hanging on the next word I say like she's sure it'll be pure gold!"
            "I don't even have to hint at her coming back to my place either, Sam practically insists on it."
            "At the end of the night we make it back home and she hustles me to my bedroom."
            "Sam all but shoves me through the door and slams it closed behind her too!"
            $ game.room = "bedroom1"
            scene bg bedroom1
            show samantha
            with fade
            if samantha.flags.nickname == "cupcake":
                mike.say "Whoa, Cupcake!"
            else:
                mike.say "Whoa, Sam!"
            mike.say "Slow down a little, yeah?"
            mike.say "We're not on a timer here!"
            show samantha happy
            "Sam laughs and shakes her head at this."
            "And then she starts pushing me backwards towards my bed."
            samantha.say "Oh no...no way!"
            samantha.say "I only need one more thing to make tonight perfect, [hero.name]."
            show samantha flirt
            samantha.say "And that's to have your cock inside of me!"
            "I can't believe what I'm hearing."
            "And that's the only reason I keep on resisting for a moment longer."
            mike.say "Wha...what did you say?!?"
            samantha.say "Urgh..."
            show samantha annoyed
            samantha.say "What's the problem here, [hero.name]?"
            samantha.say "You normally have sex on the brain."
            show samantha flirt
            samantha.say "Why won't you throw me down on the bed and fuck me?!?"
            "Only now does my brain-fog begin to clear."
            "And I realise it's not some kind of cunning trick."
            "Sam really is begging me to fuck her!"
            mike.say "Oh..."
            mike.say "Oh yeah..."
            if samantha.flags.nickname == "cupcake":
                mike.say "Sure, Cupcake, sure!"
            else:
                mike.say "Sure, Sam, sure!"
            "Sam rolls her eyes at me as I begin to undress in earnest."
            show samantha underwear with dissolve
            "But then she begins to do the same thing too."
            "Pretty soon we're both naked."
            show samantha naked with dissolve
            call samantha_dick_reactions from _call_samantha_dick_reactions_4
            "And then our hands are all over each other."
            "We don't so much lie down on the bed as topple onto it."
        elif res == 4:
            $ game.room = "bedroom1"
            scene bg bedroom1
            show samantha at center, zoomAt(1.25, (640, 880))
            with fade
            "I can vividly remember the first time that Sam and I hurried into my room like this."
            "Back then I was a bag of nerves, all of my issues around her filling my head."
            "But now that we've had time to come to terms with our relationship, it's different."
            "I mean sure, I'm still a little nervous at the thought of being intimate with Sam."
            show samantha flirt blush at center, traveling(1.5, 1.0, (640, 1040))
            "Hell, I get goosebumps just from being in the same room as her!"
            "But now I know that we're an item, the nerves are more of thrill than anxiety."
            hide samantha
            show samantha kiss
            with fade
            "And without saying a word, she leans in to press her lips against mine."
            "The kiss that follows is long, lingering and passionate."
            "And even better, it serves to silence my worries, putting me in the right place for what lies ahead."
            "Sam and I might be in the middle of a pretty intense kiss right now."
            "But that doesn't mean we're just lying still on my bed while it happens."
            "Almost as soon as our lips touch, I feel her hands all over my body."
            "At first I think she's just checking out my gym-hardened physique."
            "But then I realise that Sam's actually popping buttons and undoing zips."
            "She's engaged in the task of stripping me off - and she's not taking it slowly either!"
            "Seriously, I'm more than half naked before I get my arse into gear start doing the same to her."
            "And in rushing to catch up, I can't help getting a lot more touchy than she did with me."
            "Thankfully Sam seems to be in a particularly tactile mood today."
            "The sensation of my hands clumsily removing her clothes doesn't result in me being told off."
            show samantha kiss naked with dissolve
            "Quite the opposite in fact, as I feel her rise to my touch and hear her moan with pleasure."
            hide samantha kiss
            show samantha naked flirt blush
            with fade
            "So by the time I'm sliding off Sam's panties, she's pulling me towards the bed."
            "Holding my hand, Sam leads me over to my bed and together we lie down on the mattress."
            "And even I can tell that she's more than ready for what's coming next!"
        else:
            "Sam hurries into my bedroom ahead of me, looking back over her shoulder as she does so."
            "And it's not like she even needs to speak a single word to make sure that I'm following."
            "I mean, I'd follow Sam anywhere she went!"
            "But with the look she has in her eye right now..."
            "Hell, it's impossible for me to even think straight!"
            $ game.room = "bedroom1"
            scene bg bedroom1
            show samantha
            with fade
            mike.say "Hey!"
            if samantha.flags.nickname == "cupcake":
                mike.say "Cupcake!"
            else:
                mike.say "Sam!"
            mike.say "Wait for me!"
            "I'm fumbling to shut the door as I'm blurting all of this out."
            "Which means I have my back turned for a couple of seconds."
            "And when I turn around again, what I see hits me like a physical blow."
            "I stop dead, making a sound that would be in keeping with being punched in the gut."
            mike.say "Urgh..."
            mike.say "Whoa!"
            samantha.say "Oh..."
            samantha.say "So you like what you see?"
            samantha.say "Huh, [hero.name]?"
            show samantha topless
            "I'm nodding with a big, dumb smile on my face."
            "Because I'm staring at Sam as she's pulling off her top."
            "This means that her breasts are just popping out, free to move naturally."
            "And boy, is that a sight to see!"
            if samantha.flags.nickname == "cupcake":
                mike.say "Oh yeah, Cupcake!"
            else:
                mike.say "Oh yeah, Sam!"
            mike.say "I like it a lot!"
            "Sam smiles and begins to take off the rest of her clothes."
            "She drops them in a pile at her feet, one after another."
            show samantha naked
            if samantha.is_visibly_pregnant:
                "Her belly rounds beautifully when she straightens; she strokes the curve like it's second nature."
            "And once she's finally naked, she turns her back to me."
    return

label samantha_fuck_date_foreplay_male:
    menu:
        "Let her suck you off":
            call samantha_fuck_date_bj from _call_samantha_fuck_date_bj
        "Fuck her tits":
            call samantha_fuck_date_titjob from _call_samantha_fuck_date_titjob
        "I want to eat something sweet":
            "She understood the meaning of my words as i laid her back on the bed."
            "She starts jiggling while i put my face between her breasts and slowly move to her lower body."
            call samantha_fuck_date_cunnilingus from _call_samantha_fuck_date_cunnilingus_1
            "Now I need more."
        "Just fuck her":
            return
    if hero.fitness < 50 and not _return:
        $ samantha.love -= 5
        $ samantha.sub -= 5
        return "skip_to_sleep"
    else:
        $ samantha.sub += 1
    call stop_all_sfx from _call_stop_all_sfx_34

    return _return

label samantha_fuck_date_choices_male:
    menu:
        "Doggy":
            call samantha_fuck_date_doggy (0) from _call_samantha_fuck_date_doggy
        "Cowgirl" if hero.sexperience >= 5:
            call samantha_fuck_date_cowgirl (5) from _call_samantha_fuck_date_cowgirl
        "Missionary" if hero.sexperience >= 10:
            call samantha_fuck_date_missionary (10) from _call_samantha_fuck_date_missionary
        "Flat doggy" if hero.sexperience >= 15:
            call samantha_fuck_flat_doggy (15) from _call_samantha_fuck_flat_doggy
        "Reverse cowgirl" if hero.sexperience >= 20:
            call samantha_fuck_date_reverse_cowgirl (20) from _call_samantha_fuck_date_reverse_cowgirl
    call stop_all_sfx from _call_stop_all_sfx_35

    return _return


label samantha_fuck_date_bj:
    if game.days_played % 2 == 1:
        mike.say "I want your mouth."
        "She giggles."
        if samantha.is_sex_slave and randint(0, 1):
            samantha.say "Your slave will swallow it all."
        elif samantha.sub >= 70 and randint(0, 1):
            samantha.say "Please fuck my mouth."
        else:
            samantha.say "Oh, I'm so glad to hear that!"
        if samantha.is_visibly_pregnant and randint(0, 1):
            "She shifts her weight and props herself comfortably before she starts, one hand absently smoothing her belly."
        elif samantha.flags.engaged and randint(0, 1):
            "When her fingers wrap around me, the wedding ring throws a tiny spark of light; it keeps catching my eye as she moves."
        "Then she sets off to work."
        "As she rubs her breasts up and down along my shaft, the hunger in her eyes is almost too much to bear."
        if samantha.piercings.nipples.worn and randint(0, 1):
            "Her nipple piercings kiss my skin each stroke; the cool tug makes her gasp against me."
        show samantha bj closed suck with fade
        "She's a thirsty girl, and she lets her tongue lick over my head."
        if samantha.piercings.tongue.worn and randint(0, 1):
            "The little stud taps my crown before she seals her lips, a faint click that shoots straight through me."
        "She swirls over it a moment, getting the head nice and wet before she kisses me with those wonderful and soft lips of hers."
        if samantha.piercings.navel.worn and randint(0, 1):
            "When she arches, her navel jewel gleams up at me like a tiny lighthouse."
        "All the while as she does this, she glances up at me, making sure that I'm having a good time."
        "All the while, she lets out those loud and thirsty grunts, accenting each action with a louder, perhaps performance, moan."
        "Perhaps she is making sure I have a good time."
        "I am sure to let her know I am, and that only makes her go faster, to try harder."
        "Soon, a simple suckle goes into a full-blown suck as her cheeks collapse in from the vacuum pressure of her blowjob."
        "I groan, lifting my hips a bit as she quickens the pace of her tits, fucking my cock with her wonderful bouncy chest."
        "Soon, her focus becomes so powerful that she hungrily sucks me off as she squishes her body up against my own, her own growls and grunts rising up."
        if samantha.is_visibly_pregnant and randint(0, 1):
            "Her tits make a mess of my bed as she fondles herself, not seeming to care about all that she spills out."
        if samantha.flags.engaged and randint(0, 1):
            "The wedding ring flashes again when she strokes faster, a tiny crown of light at the base of my shaft."
        if samantha.piercings.clit.worn and randint(0, 1):
            "When she spreads her knees for balance, a cool piercing peeks between her folds for a heartbeat."
        menu:
            "Stop her":
                mike.say "He... Hey!"
                mike.say "Slow down a bit. I'm not done with you, yet!"
                hide samantha
                show samantha bj open
                "She pulls her lips away with a smack and smiles, licking them as she pushes herself up."
                if samantha.is_visibly_pregnant and randint(0, 1):
                    "She gives her sensitive breasts one last rub as she stands there."
                if samantha.flags.engaged and randint(0, 1):
                    "She wipes her mouth with the back of her hand; the band catches on her lip for a second and she laughs."
                samantha.say "Alright then. What do you want to do next? I'm ready to please!"
                return "stopped"
            "Don't stop her":
                menu:
                    "Cum in her mouth":
                        "She just can't be satisfied until my cock unleashes its cumload inside her throat, and I'm not one to displease such a lady."
                        show sexinserts head samantha cum zorder 1
                        show samantha bj suck cumshot both
                        with vpunch
                        if randint(0, 1):
                            "She seals deep and hums around me, gurgling once before swallowing hard."
                        else:
                            "She holds, then opens wide to show me the creamy pool on her tongue before gulping it down."
                        show sexinserts head samantha -cum zorder 1
                        "Soon, she pulls away, a sticky trail between my head and her lips as she shudders, wiping the remainder off of her chin."
                        if samantha.flags.engaged and randint(0, 1):
                            "She cleans the corner of her mouth with a thumb; the wedding ring flashes as she swallows."
                        samantha.say "Wow... [hero.name], you must have loved it! I'm so glad to make you happy!"
                        hide sexinserts
                    "Cum on her face":
                        "I reach for her hair, stroking her head tenderly."
                        mike.say "H.. Hey... get some air, already!"
                        "She obeys, pulling her mouth back with a pop."
                        "But what's done is done, and I can't hold back."
                        hide samantha
                        show samantha bj cumshot surprise with vpunch
                        "Suddenly, ropey white strands of cum shoot out from my cock and over her face, staining her cheeks, nose, and lips."
                        hide samantha
                        show samantha bj cumface
                        if samantha.flags.engaged and randint(0, 1):
                            "She wipes a little line off her cheek with her knuckle; the wedding band gleams bright against the mess."
                        if randint(0, 1):
                            "A stray cum slips past her chin to her throat; she chases it with two fingers and sucks them clean."
                        samantha.say "Do you like seeing me like this [hero.name]? Well, I'm glad I could make you finish!"
                        mike.say "You look wonderful."
                        samantha.say "As long as you like it, I'd be happy to look like that. Alright?"
                        "I chuckle."
                        $ FACIAL = " facial "
                hide samantha with fade
    else:
        "Sam kneels down in front of me."
        if samantha.is_visibly_pregnant and randint(0, 1):
            "She eases to her knees with a little care, one hand braced on the mattress before she reaches for me."
        show samantha bj4 lick rest up smile with fade
        if samantha.is_sex_slave and randint(0, 1):
            samantha.say "Your slave will drink it all."
        elif samantha.sub >= 70 and randint(0, 1):
            samantha.say "Hold my hair."
        elif samantha.sub >= 30 and randint(0, 1):
            samantha.say "I'll be gentle… then hungry."
        "Then she looks up at me, still smiling."
        "But I can't help gasping, as her hands are on my cock!"
        if samantha.flags.engaged and randint(0, 1):
            "The wedding band on her finger brushes my skin when she closes her grip; it sends a small shiver through me."
        "Still holding my eye, Sam leans in closer."
        show samantha bj4 lick rest down shut
        "Then she starts to caress the very tip with her lips."
        "The sensation is light and gentle in the extreme."
        "Yet somehow it's more than enough to make me gasp in surprise."
        "And I wonder if any girl but Sam would have had that effect on me."
        "Somehow knowing how long I've waited for this to become a reality..."
        "That serves to make everything she does so much more intense."
        show samantha bj4 lick rest down openmouth
        "So when she parts her lips and sticks out her tongue I'm helpless."
        if samantha.piercings.tongue.worn and randint(0, 1):
            "Her stud draws a lazy figure-eight on my tip before she dips lower."
        "Sam keeps it subtle and simple, licking and teasing, tip to tip."
        "But I can feel that she's also building up slowly."
        "She's letting things grow naturally."
        "Following her instincts and reading my reactions alike."
        "This means that when she opens her mouth wider, the time is just right."
        "My cock slides into Sam's mouth easily, without a second's pause."
        "But still she doesn't rush things, or take it all the way in."
        "Instead, Sam swallows a little at a time."
        show samantha bj4 deep deepup
        "Pausing to keep on teasing and hinting as she does so."
        "The touch of her lips, teeth and tongue are subtle."
        "But at the same time so well chosen that I feel every move she makes."
        show samantha bj4 deep deepclosed
        "I'm gasping by now, not from being exhausted or overwhelmed."
        "But rather from the intensity of my questions being answered."
        show samantha bj4 deep deepup
        "I always dreamed of what Sam would be like in a situation like this."
        "Yet my wildest imaginings don't seem close to the reality."
        "She's better than I could have imagined."
        show samantha bj4 deep deepclosed
        "And what she's doing feels so good I wish it could go on forever."
        "But it's just too good for that to be possible."
        "I'm going to lose it any moment!"
        menu:
            "Cum on her face":
                "Sam seems to be fully aware of what's going on."
                show samantha bj4 lick down
                "And she pulls her head back, letting my cock fall out of her mouth."
                show samantha bj4 up
                with vpunch
                "She's looking up at me when I finally lose it."
                show samantha bj4 lick face closed with vpunch
                "And I'm staring at that perfect face as I shoot my load."
                with vpunch
                "Lines of sticky white cum stripe Sam's face."
                if samantha.flags.engaged and randint(0, 1):
                    "She drags a finger through it with a little laugh; the wedding ring gleams at me through the mess."
                if randint(0, 1):
                    "A warm thread runs past her jaw onto her chest; she smears it into her skin and licks her palm clean."
                if samantha.is_visibly_pregnant and randint(0, 1):
                    "Another drop trails lower; she traces it toward the curve of her belly with a soft, wondering smile."
                "And she doesn't stop smiling the whole time it's happening either!"
                $ FACIAL = " facial "
            "Cum in her mouth":
                "I don't know if Sam's aware of what's happening."
                "And for a moment I'm worried about cumming in her mouth."
                "But the second I do, she shows me that she's ready."
                show sexinserts head samantha cum zorder 1
                with vpunch
                "Sam seems to brace herself as I shoot my load."
                with vpunch
                "And somehow she's ready to handle it."
                show sexinserts head samantha -cum zorder 1
                show samantha bj4 deepup
                with vpunch
                if randint(0, 1):
                    "She holds me hilt-deep and swallows in two slow pulses, humming like she's tasting wine."
                elif randint(0, 1):
                    "She lets it pool on her tongue, shows me with a naughty little grin, then gulps it down and chases the last with a lick."
                else:
                    "Sam swallows all that I have to give without incident."
                show samantha bj4 lick mouth
                if samantha.flags.engaged and randint(0, 1):
                    "She licks a last pearly thread from her lip with a slow sweep of her tongue; her wedding band flashes when she wipes her mouth."
                else:
                    "Only releasing my cock once I'm done, and gasping with satisfaction as well!"
                hide sexinserts
        show samantha bj4 down
        if samantha.flags.nickname == "cupcake":
            mike.say "Cupcake..."
        else:
            mike.say "Sam..."
        mike.say "That was..."
        mike.say "I mean it felt..."
        show samantha bj4 up smile
        "Sam smiles up at me, clearly pleased with herself and my reaction."
        samantha.say "Thank you, [hero.name]!"
        if randint(0, 1):
            samantha.say "Next time, I want to see how far I can take you without using my hands."
        else:
            samantha.say "I love the taste of you."
        show samantha bj4 lick closed
        samantha.say "And now that we're together..."
        samantha.say "There's going to be a lot more where that came from!"
        hide samantha with fade
    return

label samantha_fuck_date_titjob:
    "Laying back on the bed, I give her but one simple request."
    mike.say "I want to keep fucking them wonderful tits of yours."
    samantha.say "Oh, you really like these tits, don't you [hero.name]?"
    samantha.say "Is this what you really want?"
    if samantha.is_visibly_pregnant and randint(0, 1):
        if samantha.flags.NPCpregnancy == "ryan":
            samantha.say "You think Ryan would believe these got bigger just from swims at the pool?"
        else:
            samantha.say "Is this why you knocked me up—so you'd have even more to worship?"
    if samantha.is_visibly_pregnant and not samantha.flags.NPCpregnancy:
        samantha.say "Is this why you got me pregnant? You just wanted me to get larger and lactate, is that right?"
        mike.say "Well, it's certainly not something I dislike about knocking you up!"
        samantha.say "Then, I'm happy to give it to you. Oh, so very happy!"
    if samantha.flags.engaged and randint(0, 1):
        "When she climbs over me, her wedding ring flashes once, cold light, hot promise."
    elif randint(0, 1):
        "As she leans in, a little sparkle at her navel catches my eye—her belly jewel glitters before her breasts swallow my view."
    "Samantha scoots in, her large breasts squishing up against my body."
    hide samantha
    show samantha bj
    with fade
    if samantha.is_visibly_pregnant:
        "Little squirts of milk rolling down her chest as she settles in, making sure not to harm the baby as she gets up against the bed."
        if randint(0, 1):
            "Tiny barbells tug at her nipples; the metal gleams, halos of milk beading where the jewelry presses her soft skin."
        "She slides her hands over to the sides of her wondrous mounds, squeezing the soft and supple flesh, wincing slightly as those sore and swollen mounds are played with, and lining up both sides to wrap around my hardened pole."
        "Her breasts are warm and soft and nearly envelope my entire shaft, but they feel so wonderful having become so heavy with mother's milk."
        "She shifts and rolls those beauties with her fingers, groping herself in the process, spreading the staining milk over her body as she lets her skin slide up and down along my own."
    else:
        "She slides her hands over to the sides of her wondrous mounds, squeezing the soft and supple flesh, and lining up both sides to wrap around my hardened pole."
        "The pressure of the weighted breasts only add to my pleasure, and they nearly envelope my whole cock, but she keeps the head poking out, perhaps as a tease."
        if randint(0, 1):
            "She flicks her tongue over my tip; the little stud clicks faintly against me before she traps my shaft between her breasts again."
        "She shifts and rolls those beauties with her fingers, groping herself in the process."
    if samantha.piercings.clit.worn and randint(0, 1):
        "When she adjusts her knees, a tiny flash of metal between her folds betrays a secret piercing I’ve only barely seen."
    elif samantha.is_visibly_pregnant and randint(0, 1):
        if samantha.flags.NPCpregnancy == "ryan":
            samantha.say "Gentle… I still want to feel everything."
        else:
            samantha.say "Easy… remember—our baby’s listening."
    samantha.say "You feel so wonderful, [hero.name]. I'm so happy I get to please you with these!"
    menu:
        "Don't stop her":
            "There's no way a guy like me could ever compete with tits like those."
            "Try as I might, she's just too wonderful, running those amazing breasts up and down my meat, showing off the kinkiness of her lactating beauties."
            "What else would happen but me erupting all over her!?"
            hide samantha
            show samantha bj cumshot
            show sexinserts head samantha cum zorder 1
            show sexinserts chest samantha cum as chestcum zorder 2 at center, zoomAt(1, (670, 970))
            with vpunch
            "My cum spurts up all over her face and covers between her tits, but despite all that, she doesn't get mad."
            show samantha bj cumface cumchest with vpunch
            if randint(0, 1):
                if samantha.flags.engaged:
                    "She swipes a streak from her cheek with her wedding ring hand; the band smears a shining line across her skin."
                if samantha.is_visibly_pregnant and randint(0, 1) and samantha.piercings.nipples.worn:
                    "White on white—my spend and her milk gleam together over the metal at her nipples."
            elif randint(0, 1) and samantha.piercings.tongue:
                "Her tongue stud peeks as she tastes me off her lip, the little bead tapping her teeth."
            "She gasps, then she smiles, and she pulls away."
            hide sexinserts
            hide chestcum
            hide samantha bj
            show samantha naked blush cum
            samantha.say "I'm so happy I could make you enjoy that, [hero.name]."
            $ FACIAL = " facial "
        "Stop her":
            if samantha.flags.nickname == "cupcake":
                mike.say "Cupcake... you're wonderful. Just... please, hold back a moment."
            else:
                mike.say "Samantha... you're wonderful. Just... please, hold back a moment."
            hide samantha bj
            show samantha naked annoyed
            "Samantha frowns, pulling her wonderful breasts away from my body."
            samantha.say "Aw, [hero.name], did I... did I disappoint?"
            mike.say "No! Not at all! Just that. I want to do so much more with you!"
            show samantha normal blush
            samantha.say "W... what? Oh my! Of course! What though?"
            return "stopped"
    return

label samantha_fuck_date_cunnilingus_intro:
    $ game.play_music("music/roa_music/city_nights.ogg")
    scene bg bedroom1 with fade
    "I can hardly wait to get Sam up the stairs and into my bedroom, almost holding my breath until it happens."
    "Sam begins to strip almost as soon as the door is closed, and I follow her lead without question."
    show samantha naked happy with dissolve
    if samantha.flags.engaged and randint(0, 1) and samantha.piercings.nipples.worn:
        "When she tosses her top aside, her nipples piercings catches the lamp—little starbursts dance over the wall."
    elif samantha.is_visibly_pregnant and randint(0, 1):
        "Her belly rises and falls when she breathes in; she strokes it once, an unconscious, tender habit."
    elif randint(0, 1) and samantha.piercings.navel.worn:
        "As she steps out of her skirt, a tiny sparkle at her navel glints at me before she climbs onto the bed."
    "Before too long, we're both naked and my eyes are fixed on the shape of her body."
    "She's so beautiful - I still can't believe that she feels the same way about me as I do about her!"
    "She can't help but see how excited I am to have her in my room, it's pretty obvious in the way that she can't stop smiling."
    "Sam shakes her head as she saunters over to the bed, chuckling to herself at the sight of my enthusiasm."
    samantha.say "Aww, [hero.name]."
    samantha.say "You look like a kid on Christmas morning!"
    "I shrug, feeling embarrassed at the way she's looking at me."
    if samantha.flags.nickname == "cupcake":
        mike.say "Can you blame me, Cupcake?"
    else:
        mike.say "Can you blame me, Sam?"
    mike.say "Being with you's like the gift that keeps on giving!"
    "Sam shakes her head for a second time, rolling her eyes at the corny line."
    samantha.say "Whatever you say..."
    samantha.say "Hey, you know what - why don't you give me a gift?"
    "Sam takes hold of my hands and leads me the last few feet to the edge of the bed."
    "I follow eagerly, liking the way that this is going."
    if samantha.flags.nickname == "cupcake":
        mike.say "Yeah, Cupcake..."
    else:
        mike.say "Yeah, Sam..."
    mike.say "Whatever you want!"
    "Sam glances at me sideways, a coy look in her eyes."
    samantha.say "Well, you're always calling me your cupcake, right?"
    "I nod at this, imagining the dumb look that must be on my face right now."
    samantha.say "So did you ever wonder what that cake tastes like?"
    "Sam guides my hands towards her waist and then a little below."
    "She smiles as she does so, pressing herself against me in a very suggestive manner."
    show samantha cunnilingus with fade
    "With that, Sam lowers herself onto the bed backwards, going slow so I can follow."
    "Her hands remain holding mine, our fingers entwined."
    "And so she's pulling me down atop her at the same time."
    if randint(0, 1) and samantha.piercings.clit.worn:
        "When her thighs part, a tiny flash of metal glimmers between her folds for just a heartbeat."
    "Sam lets me lie atop her for a moment, smiling up at me the whole time."
    "I enjoy the sensation of her body, soft beneath me while it lasts."
    "Until she puts her hands on my shoulders and pushes me down towards her nether."
    samantha.say "Come on, [hero.name]."
    samantha.say "Time to pay up!"
    "I put up a token of resistance, just enough to make it fun."
    "And the upside is that I get to linger for a moment, my face between her breasts."
    if randint(0, 1) and samantha.piercings.nipples.worn:
        "Her nipple barbells brush my cheek as I kiss down; the cool metal makes her gasp."
    mike.say "Okay, Okay..."
    mike.say "You win!"
    mike.say "This elevator is going down."
    mike.say "Belly buttons, women's underwear and oral pleasure!"
    return

label samantha_fuck_date_cunnilingus:
    $ game.play_music("music/roa_music/city_nights.ogg")
    show samantha cunnilingus notongue
    "Sam bursts out laughing as my head sinks between her thighs."
    "I swear I can still feel her laughter as I begin to kiss and lick at her pussy."
    show samantha cunnilingus up
    if randint(0, 1) and samantha.piercings.clit.worn:
        "When I flatten my tongue, her own stud taps my lip as she gasps, the little bead trembling against me."
    "But as the attention that I'm giving to her gets more intense, she soon stops."
    show samantha cunnilingus middle
    "And the laughter is replaced by noises of an altogether more appreciative kind."
    show samantha cunnilingus down
    "It's not like I need any encouragement of that kind."
    show samantha cunnilingus up
    "As soon as I'm into it, all I want to do is lick Sam all the more."
    show samantha cunnilingus middle
    "Joking aside, this cupcake really does taste amazing!"
    show samantha cunnilingus down
    if randint(0, 1) and samantha.piercings.clit.worn:
        "A cool kiss of metal greets the tip of my tongue—her hood piercing answers every flick with a tiny chiming pressure."
    show samantha cunnilingus up
    "I switch between using the whole of my tongue and just the tip as I explore."
    show samantha cunnilingus middle
    "At first I'm just tracing the shape of Sam's outer folds."
    show samantha cunnilingus down
    if randint(0, 1) and samantha.flags.engaged:
        "Her wedding ring presses into my fingers when she squeezes my hand; I feel the circle bite sweetly as she pulls me closer."
    show samantha cunnilingus up
    "But I'm also beginning to work my way inwards too, spiralling ever deeper into her."
    show samantha cunnilingus middle
    samantha.say "Shit..."
    show samantha cunnilingus down
    samantha.say "That's good..."
    show samantha cunnilingus up
    samantha.say "That's REALLY good!"
    show samantha cunnilingus down
    menu:
        "Use my tongue":
            show samantha cunnilingus up
            "Keen to give Sam more of what she's liking, I redouble my efforts."
            show samantha cunnilingus middle
            "Now my tongue isn't just licking at her pussy like it was before."
            if samantha.piercings.clit.worn and randint(0, 1):
                "A cool kiss of metal greets my tongue—her hood piercing answers every flick with a tiny pulse of pressure."
            elif samantha.is_visibly_pregnant and randint(0, 1):
                "I keep my shoulders snug between her knees so nothing presses her belly; she exhales a grateful, shivery yes."
            show samantha cunnilingus down
            "Instead I'm lapping away, doing all I can to touch as much of her as possible."
            show samantha cunnilingus up
            "My tongue starts to travel deeper and deeper into her folds."
            if samantha.piercings.navel.worn and randint(0, 1):
                "When her abs tense, the little jewel in her navel twinkles at me between breaths."
            elif samantha.flags.engaged and randint(0, 1):
                "Her wedding ring flashes as she clutches the sheets, a bright spark every time I hit the spot."
            show samantha cunnilingus middle
            "Sam's all that I can taste and all that I can smell."
            show samantha cunnilingus down
            "I've long since closed my eyes to concentrate on the task at hand."
            if samantha.piercings.nipples.worn and randint(0, 1):
                "Her nipple barbells graze my cheek when I kiss up her inner thigh; the cool metal makes her gasp."
            show samantha cunnilingus up
            "Which means that Sam's filling all of my remaining senses."
            show samantha cunnilingus middle
            "I wonder just how far I can reach with my tongue."
            show samantha cunnilingus down
            "How far inside of her can it go before I have to stop?"
            show samantha cunnilingus up
            "And more importantly, how far can I go before Sam cums?"
            show samantha cunnilingus middle
            show samantha cunnilingus blush
            "It's not like I need to listen out for the first signs of that either."
            show samantha cunnilingus down
            "And that's because I feel Sam's legs wrap themselves around me."
            show samantha cunnilingus up wet
            "She's crushing me with her thighs a moment later."
            show samantha cunnilingus down
            "As if she can squeeze the effort out of my body and into her own!"
            if samantha.piercings.tongue.worn and randint(0, 1):
                "When she moans, her tongue stud clicks faintly against her teeth; the sound spikes my pulse."
            show samantha cunnilingus middle
            "I struggle to keep on doing what I'm doing right to the end."
            show samantha cunnilingus down
            "But it's a battle to make sure I manage it without being smothered for my troubles!"
        "Finger her ass" if hero.sexperience >= 30:
            show samantha cunnilingus up
            "I'm doing my best to keep on giving Sam more of what she likes."
            show samantha cunnilingus middle
            "But she starts to buck and twitch under the attention of my tongue."
            show samantha cunnilingus down
            "At first I just take hold of her ass to keep from being smothered by her pussy!"
            if samantha.is_visibly_pregnant and randint(0, 1):
                "I angle my wrist carefully, keeping her hips cushioned so we don't jostle her belly."
            show samantha cunnilingus up
            show samantha cunnilingus fingerass
            "So that's why I take a finger and stick it straight up there."
            if samantha.flags.engaged and randint(0, 1):
                "Her wedding ring bites my palm when she squeezes my hand, dragging me closer."
            elif samantha.piercings.navel.worn and randint(0, 1):
                "Her tummy tightens; the navel jewel gives a quick glitter between breaths."
            show samantha cunnilingus middle
            samantha.say "Wow..."
            show samantha cunnilingus down
            samantha.say "What are you..."
            show samantha cunnilingus up
            samantha.say "Oooh...that feels incredible!"
            show samantha cunnilingus middle wet
            "I can feel Sam's ass melting from the sensation of my finger being up there."
            show samantha cunnilingus down
            "And now I can make her dance between that one finger and my tongue."
            show samantha cunnilingus up
            "I swear I can almost feel the way her muscles are moving on account of one with the other."
            show samantha cunnilingus middle
            "Like my tongue can tell where my finger is and my finger can do the same."
            show samantha cunnilingus down
            "I don't know whether it's on account of my finger or Sam's doing it herself."
            show samantha cunnilingus up
            "But her pelvis starts to rise up from the mattress and press into my face."
            show samantha cunnilingus middle
            "Rather than feeling like I'm going to be smothered again, I embrace it eagerly."
            "If she's so desperate for more of the same, then I'm going to give it to her!"
            show samantha cunnilingus down
            "And based on the effort that I'm having to put in, she can't take much more of this..."
        "Use the vibrator" if hero.has_item("vibrator"):
            show samantha cunnilingus up
            "I pause in my efforts, just enough to be able to speak and be heard."
            show samantha cunnilingus middle
            if samantha.flags.nickname == "cupcake":
                mike.say "Sure it's good, Cupcake."
            else:
                mike.say "Sure it's good, Sam."
            show samantha cunnilingus down
            mike.say "But it's not good enough to fill you all the way..."
            show samantha cunnilingus up
            "I make to reach for something that I know is under the bed, just within reach."
            show samantha cunnilingus middle
            "Sam moves to stop me, and I know that she's already missing my attentions."
            show samantha cunnilingus down
            samantha.say "No, [hero.name]..."
            show samantha cunnilingus up
            samantha.say "You don't need to..."
            show samantha cunnilingus middle
            "But by then I already have the vibrator that was stashed under the bed in my hand."
            show samantha cunnilingus down
            "I make sure that Sam gets only the merest glimpse of it as I steer it between her thighs."
            if samantha.piercings.clit.worn and randint(0, 1):
                "The toy nudges her hood piercing and she jolts; that tiny tap turns her sigh into a hungry gasp."
            show samantha cunnilingus -up -middle -down -notongue vibratorpussy
            "She's still glistening from my tongue, and so it slides into her without any trouble."
            samantha.say "Oh..."
            samantha.say "Oooh..."
            show samantha cunnilingus wet
            samantha.say "Fuck...that feels SO good!"
            "Sure, using a toy on Sam might not be as intimate as using my tongue."
            show samantha cunnilingus vibrate
            "Yet I enjoy the feeling of being in control of just what she experiences all the same."
            if samantha.flags.engaged and randint(0, 1):
                "Her wedding ring scrapes the sheet as she fists it tight, flashing with each shiver."
            "I think about licking around the edges of her pussy at the same time."
            "But the chance to watch as she wriggles and writhes on the end of the vibrator is just too much."
            "She looks so wanton and helpless as she lies there, totally in the power of her own pleasure."
            "God, I hope she cums soon."
            "Because I don't think my cock can get any harder!"
        "Use vibrator and my finger." if hero.has_item("vibrator") and hero.sexperience >= 30:
            show samantha cunnilingus up
            "I stop what I'm doing for a moment, smiling down at Sam."
            show samantha cunnilingus middle
            if samantha.flags.nickname == "cupcake":
                mike.say "It's good, Cupcake."
            else:
                mike.say "It's good, Sam."
            show samantha cunnilingus down
            mike.say "But it's not the best that I can do..."
            show samantha cunnilingus up
            "With that, I reach under the bed, searching for something that I know is at hand."
            show samantha cunnilingus middle
            "Sam tries to stop me, instinctively desiring more of my attention."
            show samantha cunnilingus down
            samantha.say "No, [hero.name]..."
            show samantha cunnilingus up
            samantha.say "Please don't stop..."
            show samantha cunnilingus middle
            "I already have the vibrator in my hand, even as she reaches out to me."
            show samantha cunnilingus down
            "Sam hardly gets to see it as I lower it between her legs."
            show samantha cunnilingus -up -middle -down -notongue vibratorpussy
            "The first she knows about it is the sensation of it sinking into her pussy."
            "And she's already wet enough to make that happen with no resistance whatsoever."
            samantha.say "Ah..."
            samantha.say "Aaah..."
            show samantha cunnilingus vibrate
            samantha.say "Shit...that feels SO good!"
            "Sam soon starts to buck and twitch under the attention of the toy."
            if samantha.piercings.clit.worn and randint(0, 1):
                "Every pulse of the toy tugs faintly at her hood ring; the extra spark makes her hips chase the vibration."
            "At first I just take hold of her ass with my free hand to keep her still."
            show samantha cunnilingus fingerass
            "But it's not long before I give in to temptation and stick a finger up there too."
            if samantha.flags.engaged and randint(0, 1):
                "She laces her fingers with mine; the wedding ring presses into my knuckle while she rides the toy."
            if samantha.is_visibly_pregnant and randint(0, 1):
                "I keep my palm under her hip so she can move without straining; she melts into the support."
            samantha.say "Whoa..."
            samantha.say "What's that..."
            samantha.say "Mmm...oh man..."
            "Sam's ass melts in mere seconds, the muscles surrendering to my finger."
            "And now I can make her dance between that one finger and the vibrator."
            "I swear I can almost feel the way her muscles are moving on account of one with the other."
            show samantha cunnilingus wet
            "Like my finger can feel where her muscles are contracting from the vibrator."
            "I don't know whether it's on account of my finger or Sam's doing it herself."
            "But her pelvis starts to rise up from the mattress."
            "If she's so desperate for more of the same, then I'm going to give it to her!"
            "And based on the effort that I'm having to put in, she can't take much more of this..."
            show samantha cunnilingus down
    show samantha cunnilingus ahegao -up -middle -down -notongue -fingerass
    "When Sam finally cums, it's like something erupting from a volcano."
    "Her entire body shakes so much that she has me worried for a moment."
    "Every muscle in her body seems to tense, knotting up from the pressure she's under."
    show samantha cunnilingus squirt
    "And then, just like that, it's released with a groan that comes from the very core of her being."
    "Sam collapses back onto the mattress, like her body's become limp and lifeless."
    "All she can do is pant, her chest rising and falling as her heart pounds inside of it."
    "Her eyes are glazed over, impossible to read in the afterglow of her orgasm."
    "But all the same, I can see that her lips are curled into a smile of pure satisfaction."
    "And that's more than enough for me to know that it was a job well done."
    return

label samantha_date_fuck_blindfold:
    $ game.play_music("music/roa_music/city_nights.ogg")
    mike.say "I want to try something a little different now, too. Take a look at this!"
    "With that, I reach over towards my drawer, pulling out a blindfold."
    if samantha.flags.engaged and randint(0, 1):
        "Her wedding ring flashes when she lifts her hand to her mouth."
    "Samantha bites her lip at the sight of it."
    if samantha.piercings.tongue.worn and randint(0, 1):
        "She wets her lips; the little stud clicks faintly against her teeth."
    samantha.say "You want to blind me, [hero.name]?"
    mike.say "It'll heighten your pleasure and I'll get to do whatever I want without you seeing what it is."
    if samantha.sub >= 10:
        if samantha.is_visibly_pregnant and randint(0, 1):
            "I steady her by the hips so nothing presses her belly."
        elif samantha.piercings.nipples.worn and randint(0, 1):
            "When I reach around, the cloth brushes her barbells and she shivers."
        samantha.say "Oh, oh my..."
        "I reach around her head, putting the cloth over her face. She sighs as I tie it around the back of her head."
        if samantha.piercings.navel.worn and randint(0, 1):
            "As she breathes in, her navel jewel gives a twinkle."
        elif samantha.piercings.clit.worn and randint(0, 1):
            "When she shifts her thighs, a quick sparkle betrays a hidden piercing."
        mike.say "There you go, can you see?"
        samantha.say "Nothing at all!"
        $ samantha.sub += 1
        $ BLINDFOLD = " blind "
    else:
        samantha.say "Maybe some other time."
    return

label samantha_date_fuck_beads:
    $ game.play_music("music/roa_music/city_nights.ogg")
    "I clamber away, pulling out the set of anal beads from my drawer."
    if samantha.flags.engaged and randint(0, 1):
        "Her wedding ring leaves a little comet of light across the sheet as she adjusts."
    "Samantha lets a curious coo out as I tell her my plan."
    if samantha.sub >= 20:
        mike.say "Spread your legs. Your ass, too."
        "She spreads apart, reaching down over her thighs, her fingers digging into her cheeks."
        if samantha.piercings.clit.worn and randint(0, 1):
            "A tiny flicker between her folds betrays a hood piercing when she parts herself."
        "She pulls them apart, showing off her puckered pink star."
        if samantha.is_visibly_pregnant and randint(0, 1):
            "She props a cushion under her hips and nods for me to continue."
        samantha.say "H-here it is, [hero.name]. I hope its not too terrible for you."
        mike.say "Oh, it's perfect."
        "I pour the lube over the beads, making them glisten."
        if samantha.piercings.navel.worn and randint(0, 1):
            "The shine in my palm mirrors the sparkle at her navel."
        mike.say "Just keep holding on. I'm coming in."
        "The beads glisten in my hand as I get down in front of the bed."
        "Samantha breathes steadily, waiting for what is to come."
        "First comes the smallest bead, which meets resistance."
        "Samantha gasps, her toes curling, her body shuddering."
        "I roll the bead around her hole a moment before I push in."
        "Her ass swallows it, and she tilts her head back, sighing happily."
        if samantha.flags.engaged and randint(0, 1):
            "She fists the sheet; her wedding ring bites the fabric as she squeezes."
        samantha.say "[hero.name], it's inside., I-"
        "I push the next one up against her hole, larger than the first."
        "She bites her lip and squeals as she feels it forcing its way inside, but after a moment of coaxing, Samantha swallows it up."
        if samantha.is_visibly_pregnant and randint(0, 1):
            "I keep my free hand cradling her belly while I feed the next bead home."
        samantha.say "Do... do you like seeing my ass take your beads, [hero.name]?"
        "I answer her by adding in the next one."
        "One after another, larger and larger beads make their way inside her body."
        if samantha.piercings.nipples.worn and randint(0, 1):
            "Her nipples piercings stand taut as she groans into the mattress."
        "Her mouth hangs open as she takes in those beads, until finally, we are done, leaving her with a trail of beads sticking out of her ass."
        $ samantha.sub += 1
        $ BEADS = " beads "
    else:
        samantha.say "Maybe some other time."
    return

label samantha_fuck_date_doggy(sexperience_min):
    $ BLINDFOLD = ""
    $ BEADS = ""
    $ DILDO = ""
    $ CONDOM = False
    "I push myself up, sitting on the bed on my knees."
    mike.say "Come over here. Crawl up on the bed."
    samantha.say "Oooh, yes, sir, [hero.name]!"
    show expression f"samantha doggy nomike {FACIAL}" with fade
    if FACIAL and randint(0, 1):
        "Shiny streaks of cum cling to her cheek; she drags her tongue across her lip and smiles."
        if samantha.piercings.tongue.worn and randint(0, 1):
            "Her stud taps her teeth as she tastes me."
        if samantha.flags.engaged and randint(0, 1):
            "She wipes a line with the back of her hand; the wedding ring smears a bright trail."
    "Samantha says, making her way to the middle of the mattress, palms running along the sides of the bed to get her bearings..."
    if samantha.flags.engaged and randint(0, 1):
        "Her wedding ring ticks softly on the headboard when she braces."
    samantha.say "I can guess what we're doing now!"
    if samantha.is_visibly_pregnant:
        "The way her belly and her tits accent her profile makes the submissive position all the more hot."
        if samantha.piercings.navel.worn and randint(0, 1):
            "Her navel jewel glints when she arches."
    if "anal_beads" in hero.inventory or "dildo" in hero.inventory or "blindfold" in hero.inventory:
        menu:
            "Use some toy":
                menu:
                    "Anal beads" if "anal_beads" in hero.inventory:
                        call samantha_date_fuck_beads from _call_samantha_date_fuck_beads
                    "Dildo" if "dildo" in hero.inventory:
                        call samantha_date_fuck_dildo from _call_samantha_date_fuck_dildo
                    "Blindfold" if "blindfold" in hero.inventory:
                        call samantha_date_fuck_blindfold from _call_samantha_date_fuck_blindfold
            "Don't use toys":
                mike.say "You're probably right."
    else:
        mike.say "You're probably right."
    show expression f"samantha doggy out {FACIAL} {BEADS} {BLINDFOLD} {DILDO}" with fade
    "I shuffle around her and soon face her from behind."
    mike.say "Always want to do it doggy style. You ever done it before?"
    samantha.say "For you, I'll do anything!"
    "She looks over her shoulder with that devoted smile she always has and nods quickly, grabbing the covers in her anticipation."
    "So, I go in, looming over her, my arms wrapping around her body."
    if samantha.is_visibly_pregnant:
        "I grab onto her tits, fondling them, squeezing them, letting the milk spill out and roll over my fingers and over her skin."
        if samantha.piercings.nipples.worn and randint(0, 1):
            "The nipples piercings press into my palms; milk beads around cool steel."
        "She gasps, pushing her chest out, her nipples hardening under my palms as I work my way over her."
        samantha.say "Aah, [hero.name] milk me... I'm so swollen!"
        "Once I am done with her tits, I slide my sticky and wet hand downward, drying myself off over her smooth and supple skin."
        "Soon, my palm finds its way over her pregnant body, and I swirl my hand over the mound I had made within her."
        "New life, created by me!"
        "The perfect biological achievement a man can accomplish, and within a mother who would do anything for me."
    menu:
        "Fuck her ass" if not BEADS:
            "My cock rests between her asscheeks before I slide the length down between that crack of hers."
            show expression f"samantha doggy anal {FACIAL} {BLINDFOLD} {DILDO}" with fade
            "She squeaks as my cock presses itself up against her hole."
            if samantha.flags.engaged and randint(0, 1):
                "Her wedding ring digs into the sheet when she clutches at it."
            samantha.say "Ah, [hero.name], my ass?"
            mike.say "Your ass is mine."
            samantha.say "Mmm, yes, you're right. It is yours. All of my body is. All for your pleasure!"
            "I take that pleasure, thrusting inside of her, spreading her apart as I fill her forbidden hole."
            if DILDO:
                menu:
                    "Take the vibrator out":
                        call samantha_date_fuck_dildo_out from _call_samantha_date_fuck_dildo_out
                    "Don't":
                        pass
            show expression f"samantha doggy anal {FACIAL} {BLINDFOLD} {DILDO}" with fade
            "I press up against her naked back, our bodies heated in our animalistic fucking."
            "This is for my own pleasure, but her groans underneath of my body prove that she too loves taking it up the ass, even if it is for my own desires."
            "She lifts her hips up, begging for more, and I give it, plunging deeper into her."
            call cum_reaction (samantha , 'anal', sexperience_min) from _call_cum_reaction_151
            if _return == "anal_inside":
                $ samantha.love += 1
                "With a few more thrusts, I soon find myself slamming up into her."
                if samantha.flags.nickname == "cupcake":
                    mike.say "I'm going to cum now, Cupcake."
                else:
                    mike.say "I'm going to cum now, Samantha."
                samantha.say "Oh, [hero.name], please!"
                show expression f"samantha doggy cumshot anal {FACIAL} {BLINDFOLD} {DILDO}"
                "With a gasp, I soon find myself releasing, spurting out into her as I hold her down."
                "She's mine now, and she smiles, her cheek against the bed, drooling."
                "I pull out, her hole filled with my creamy goodness as I look over my conquest with a satisfied grin."
                show expression f"samantha doggy nomike{FACIAL} {BLINDFOLD} {DILDO}"
            elif _return == "anal_outside":
                $ samantha.sub += 1
                show expression f"samantha doggy cumshot out {FACIAL} {BLINDFOLD} {DILDO}"
                "Finding myself ready, I pull myself out, but I don't leave her with nothing."
                "When I release, I shoot off onto her lower back and her butt, making her glisten with my expulsions."
                if samantha.is_visibly_pregnant:
                    "After all, I've already conquered her inside, why not mark her outside?"
                show expression f"samantha doggy nomike asscum bodycum{FACIAL} {BLINDFOLD} {DILDO}"
            $ samantha.flags.anal += 1
        "Fuck her pussy" if not DILDO:
            call check_condom_usage (samantha) from _call_check_condom_usage_97
            if _return == False:
                return
            "Meanwhile, my cock rests between her asscheeks."
            if CONDOM:
                show expression f"samantha doggy {FACIAL} {BEADS} {BLINDFOLD} condom"
            else:
                show expression f"samantha doggy {FACIAL} {BEADS} {BLINDFOLD}"
            if samantha.piercings.clit.worn and randint(0, 1):
                "When I slide lower, a cool piercing kisses the crown of my cock and she jolts."
                "I slide the length down between those wonderful curves, soon finding her womanhood."
            "With a thrust, I take her, and she squeaks as I penetrate."
            "My chest presses up against her naked back, our bodies warming each other as I rut away like a wild animal."
            if BEADS:
                menu:
                    "Take the beads out":
                        call samantha_date_fuck_beads_out from _call_samantha_date_fuck_beads_out
                    "Don't":
                        pass
            if CONDOM:
                show expression f"samantha doggy {FACIAL} {BEADS} {BLINDFOLD} condom"
            else:
                show expression f"samantha doggy {FACIAL} {BEADS} {BLINDFOLD}"
            if samantha.flags.engaged and randint(0, 1):
                "Her wedding ring ticks against the sheet when she braces, flashing each time I drive in."
            elif samantha.piercings.navel.worn and randint(0, 1):
                "When her core tightens, the little jewel at her navel gives a quick twinkle."
            elif samantha.piercings.clit.worn and randint(0, 1):
                "A cool kiss of metal grazes my crown on every pass; she jolts and pushes back harder."
            elif samantha.piercings.nipples.worn and randint(0, 1):
                "Her nipple piercings sway when her breasts drag on the mattress; she gasps and arches."
            elif samantha.piercings.tongue.worn and randint(0, 1):
                "Her moan breaks on a soft click of her tongue piercing."

            "She lifts her hips against my body, grinding away as if she is in heat herself, and perhaps, in a way we are."
            if samantha.is_visibly_pregnant:
                "Which, for a pregnant woman, would make her quite the insatiable monster!"
            if samantha.is_visibly_pregnant and randint(0, 1):
                "I keep one palm under her belly when she rocks back; she melts into the support."
            "It has been a long time coming, and I'm glad I get to have her."
            call cum_reaction (samantha, 'vaginal', sexperience_min) from _call_cum_reaction_152
            if _return == "vaginal_condom":
                "With a few more thrusts, I soon find myself slamming up into her."
                if samantha.flags.nickname == "cupcake":
                    mike.say "I'm going to cum now, Cupcake."
                else:
                    mike.say "I'm going to cum now, Samantha."
                samantha.say "Oh, [hero.name], please!"
                show expression f"samantha doggy cumshot {FACIAL} {BEADS} {BLINDFOLD} condom"
                "With a gasp, I soon find myself releasing, spurting out into the condom as I hold her down."
                if samantha.flags.engaged and randint(0, 1):
                    "Her wedding ring digs into the sheet as she clutches it through the aftershocks."
                "She's mine now, and she smiles, her cheek against the bed, drooling."
                "I pull out, the rubber filled with my creamy goodness as I look over my conquest with a satisfied grin."
                show expression f"samantha doggy nomike {FACIAL} {BEADS} {BLINDFOLD}"
            elif _return == "vaginal_outside":
                if CONDOM:
                    show expression f"samantha doggy cumshot out {FACIAL} {BEADS} {BLINDFOLD} condom"
                else:
                    show expression f"samantha doggy cumshot out {FACIAL} {BEADS} {BLINDFOLD}"
                "Finding myself ready, I pull myself out, but I don't leave her with nothing."
                "When I release, I shoot off onto her lower back and her butt, making her glisten with my expulsions."
                if FACIAL and randint(0, 1):
                    "Her cheek is still glossy from earlier; the new streaks make a wicked contrast with the shine on her face."
                elif samantha.flags.engaged and randint(0, 1):
                    "She wipes a line with the back of her hand; the wedding ring smears a pearly trail over her skin."
                if samantha.is_visibly_pregnant:
                    "After all, I've already conquered her inside, why not mark her outside?"
                show expression f"samantha doggy nomike asscum bodycum {FACIAL} {BEADS} {BLINDFOLD}"
            elif _return == "vaginal_inside_pill":
                "With a few more thrusts, I soon find myself slamming up into her."
                if samantha.flags.nickname == "cupcake":
                    mike.say "I'm going to cum now, Cupcake."
                else:
                    mike.say "I'm going to cum now, Samantha."
                samantha.say "Oh, [hero.name], please!"
                show expression f"samantha doggy cumshot {FACIAL} {BEADS} {BLINDFOLD}"
                "With a gasp, I soon find myself releasing, spurting out into her as I hold her down."
                if samantha.piercings.clit.worn and randint(0, 1):
                    "She shudders when the last pulse brushes her hood ring."
                "She's mine now, and she smiles, her cheek against the bed, drooling."
                "I pull out, her hole filled with my creamy goodness as I look over my conquest with a satisfied grin."
                show expression f"samantha doggy nomike {FACIAL} {BEADS} {BLINDFOLD}"
            elif _return == "vaginal_inside_pregnant":
                "With a few more thrusts, I soon find myself slamming up into her."
                if samantha.flags.nickname == "cupcake":
                    mike.say "I'm going to cum now, Cupcake."
                else:
                    mike.say "I'm going to cum now, Samantha."
                samantha.say "Oh, [hero.name], please!"
                show expression f"samantha doggy cumshot {FACIAL} {BEADS} {BLINDFOLD}"
                "With a gasp, I soon find myself releasing, spurting out into her as I hold her down."
                if samantha.is_visibly_pregnant and not samantha.flags.NPCpregnancy == "ryan" and randint(0, 1):
                    "I press my palm to her belly for a heartbeat; ours."
                elif samantha.flags.NPCpregnancy == "ryan" and randint(0, 1):
                    "She breathes, 'steady,' and I keep her hips cradled until the tremor fades."
                "She's mine now, and she smiles, her cheek against the bed, drooling."
                "I pull out, her hole filled with my creamy goodness as I look over my conquest with a satisfied grin."
                show expression f"samantha doggy nomike {FACIAL} {BEADS} {BLINDFOLD}"
            elif _return == "vaginal_inside_mad":
                "With a few more thrusts, I soon find myself slamming up into her."
                if samantha.flags.nickname == "cupcake":
                    mike.say "I'm going to cum now, Cupcake."
                else:
                    mike.say "I'm going to cum now, Samantha."
                samantha.say "Oh, [hero.name], please!"
                $ samantha.love -= 20
                show expression f"samantha doggy cumshot {FACIAL} {BEADS} {BLINDFOLD}"
                samantha.say "Ugh...ugh...you...you came in me!"
                samantha.say "...you came inside of me!"
                $ samantha.impregnate()
                "I'm still in her when she says this."
                mike.say "What can I say...I wanted you to have something to remember me by!"
                "Sam surprises me by giving me a swift slap across the face and dragging herself out from under me."
                samantha.say "Asshole - it'd serve you right if you got me pregnant!"
                show expression f"samantha doggy nomike {FACIAL} {BEADS} {BLINDFOLD}"
            elif _return == "vaginal_inside_happy":
                "With a few more thrusts, I soon find myself slamming up into her."
                if samantha.flags.nickname == "cupcake":
                    mike.say "I'm going to cum now, Cupcake."
                else:
                    mike.say "I'm going to cum now, Samantha."
                samantha.say "Oh, [hero.name], please!"
                show expression f"samantha doggy cumshot {FACIAL} {BEADS} {BLINDFOLD}"
                "With a gasp, I soon find myself releasing, spurting out into her as I hold her down."
                if samantha.piercings.nipples.worn and randint(0, 1):
                    "Her piercings stand tight when she moans into the pillow."
                $ samantha.impregnate()
                "I pull out, her hole filled with my creamy goodness as I look over my conquest with a satisfied grin."
                show expression f"samantha doggy nomike {FACIAL} {BEADS} {BLINDFOLD}"
    "After holding onto her a bit, I whisper into her ear."
    mike.say "You like it when I take control?"
    samantha.say "Oh, I like it when you're happy!"
    return

label samantha_fuck_date_reverse_cowgirl(sexperience_min):
    scene samantha reverse with fade
    "Sam straddles my thighs, her back to me."
    "I think they call the position reverse cowgirl."
    "But I don't have the headspace to be sure of that."
    "All I know is that Sam has a hold of my cock."
    "And she's already stroking the shaft like she means business!"
    if samantha.flags.engaged and randint(0, 1):
        "Her wedding ring shimmers as she pumps me; every flash sends a hot little jolt through me."
    elif samantha.piercings.navel.worn and randint(0, 1):
        "When she leans forward to guide me, her navel jewel gives a wicked gleam."
    elif FACIAL and randint(0, 1):
        "A glossy sheen still clings to her cheek; she drags her tongue over her lip and grins."
    elif samantha.is_visibly_pregnant and randint(0, 1):
        "Her belly rises and falls; she places my hand where she wants support before she sits deeper."
    elif samantha.piercings.tongue.worn and randint(0, 1):
        "She steals a quick lick along my tip; the stud clicks softly, then she settles back onto me."
    if samantha.is_sex_slave and randint(0, 1):
        samantha.say "Your slave is ready. Use me."
    elif samantha.sub >= 70 and randint(0, 1):
        samantha.say "Tell me how you want me."
    elif samantha.sub < 30 and randint(0, 1):
        samantha.say "Go easy… at least at first."
    menu:
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "Sam might be doing all she can to take control of the situation."
            "But that doesn't mean I have to sit back and surrender it to her."
            "With that in mind, I reach out and take a firm hold of her around the waist."
            "And then I angle myself in just such a way..."
            samantha.say "Wha..."
            samantha.say "What are you..."
            samantha.say "Oh...oh fuck!"
            show samantha reversecowgirl anal with fade
            "Caught off-guard, there's nothing that Sam can do to stop me."
            "Before she even knows what's happening, I have my cock in her ass."
            if samantha.is_visibly_pregnant and randint(0, 1):
                "I keep one hand braced beneath her belly while I guide her down, steady and sure."
            "Her muscles instinctively tense, trying to keep me out."
            "But I have gravity and her own weight on my side."
            "Which means that she begins to sink down and onto me."
            samantha.say "My..."
            samantha.say "My ass..."
            samantha.say "You're in my ass!"
            "I can't help chuckling at the sheer surprise in Sam's voice."
            "It's almost like she can't actually believe what's happening to her!"
            "But then I remember that I'm right in the middle of something here."
            "There will be plenty of time to pat myself on the back later."
            "Right now I need to focus on the task at hand."
            if samantha.flags.nickname == "cupcake":
                mike.say "How does that feel, Cupcake?"
            else:
                mike.say "How does that feel, Sam?"
            mike.say "You liking having me inside you?"
            "Sam looks back over her shoulder as I say this."
            "Her eyes are more than a little glazed over."
            "And her mouth is hanging open as she gasps for breath."
            "But all the same, I see her nod."
            if samantha.sub >= 70 and randint(0, 1):
                samantha.say "Yes. Take what you want."
            elif samantha.is_sex_slave and randint(0, 1):
                samantha.say "I'm yours to use."
            "That's all the permission I need to step things up."
            "A moment later I'm thrusting in and out of her."
            "Sure, the going's a little slower than it would be with her pussy."
            show samantha reversecowgirl speed at startle(0.05,-10)
            "But that extra bit of squeezing from her muscles feels incredible."
            if samantha.piercings.nipples.worn and randint(0, 1):
                "Her nipple piercings tug and sway when her hands clamp over her breasts."
            elif samantha.piercings.clit.worn and randint(0, 1):
                "Her fingers find the cool piercings between her folds; every brush sends a shock through her."
            "It doesn't take long for Sam's head to sag forwards."
            "And I can see that she's playing with herself too."
            "One hand is pinching at her erect nipples, the other stroking between her thighs."
            "It's as if she's desperately trying to find release for the sensations she's feeling."
            "And she's not the only one that's in need of release."
            "My heart is pounding in my chest right now."
            "My breathing is getting ever more laboured."
            "And I can feel the last of my energy ebbing away."
            "Which is why the sensation of being about to come is so welcome."
            call cum_reaction (samantha, 'anal', sexperience_min) from _call_cum_reaction_153
            if _return == 'anal_inside':
                "Neither of us is going to stop before we're done."
                "Which makes me glad that I chose to use this hole!"
                show samantha reversecowgirl impact creampie orgasm with vpunch
                "I keep a firm hold on Sam as I shoot my load."
                show samantha reversecowgirl -speed -impact with vpunch
                "And she arches her back as I do so."
                if samantha.flags.engaged and randint(0, 1):
                    "Her wedding ring digs into her thigh as she clenches and moans."
                "From the sounds that she's making, I know that she's enjoying it."
                "Maybe even as much as I am!"
                $ samantha.love += 2
                $ samantha.sub += 1
            elif _return == 'anal_outside':
                "I'd love nothing more than to just keep right on going."
                "But I feel like I need to mark my territory."
                "I make sure that I have a firm grip on Sam."
                show samantha reversecowgirl -speed -anal
                "And then I pull out before it's too late."
                "Sam arches her back as I do so, moaning at the sensation."
                show samantha reversecowgirl cumshot orgasm cum onbody with vpunch
                "Then I shoot my load, spattering her backside with cum."
                if FACIAL and randint(0, 1):
                    "A few stray drops cross her shoulder; the shine on her cheek makes the contrast even filthier."
                $ samantha.sub += 2
                $ samantha.love += 1
            $ samantha.flags.anal += 1
        "Fuck her pussy":

            "Sam teases me by rubbing the head of my cock against the lips of her pussy."
            if samantha.piercings.clit.worn and randint(0, 1):
                "The crown kisses a cool ring; she jolts and then aims me again with a hungry little noise."
            "And there's nothing more I want right now than to push it right in there."
            call check_condom_usage (samantha) from _call_check_condom_usage_98
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show samantha reverse condom
            "Sam doesn't waste any time."
            "She knows what she wants and she's going to get it."
            "I feel her pressing herself down, using all of her weight."
            "And at the same time she's aiming my cock just so..."
            show samantha reverse vaginal up
            "There's a few short moments of resistance, but that's all."
            "Then I feel the sensation of her body surrendering to me."
            samantha.say "Oh..."
            show samantha reverse vaginal down
            samantha.say "Oh yeah..."
            if samantha.flags.engaged and randint(0, 1):
                "Her wedding ring flashes when she braces on my knees and rides me down."
            elif samantha.piercings.navel.worn and randint(0, 1):
                "Her belly jewel blink with every inch she claims."
            if samantha.is_sex_slave and randint(0, 1):
                samantha.say "Command me. I'll ride until you say stop."
            elif samantha.sub >= 70 and randint(0, 1):
                samantha.say "Hold me down and make me take it."
            "Sam could be speaking for the both of us right now."
            "Because what I'm feeling is so good it's leaving me speechless!"
            "She slowly inches her way down, taking my cock into her as she goes."
            "Every little bit of it that slides into her makes the sensation more intense."
            "And even when I'm as deep into her as I can go, Sam doesn't stop."
            "Instead she begins to move up and down, riding my cock."
            "At first I'm happy to just lie back and leave her to it."
            show samantha reverse vaginal up
            pause 0.4
            show samantha reverse vaginal down at startle(0.05,-10)
            pause 0.4
            show samantha reverse vaginal up
            pause 0.4
            show samantha reverse vaginal down at startle(0.05,-10)
            pause 0.4
            show samantha reverse vaginal up
            pause 0.4
            show samantha reverse vaginal down at startle(0.05,-10)
            "I can see her ass going up and down in front of me."
            "And I catch glimpses of her breasts swaying too."
            if samantha.piercings.nipples.worn and randint(0, 1):
                "Her nipple barbells bounce and tug with every drop; she moans when they pull."
            "But I know that it's not going to be enough."
            "I can't just let Sam fuck me."
            "I have to fuck her too!"
            "Without a conscious thought, my hands reach out."
            "Sam yelps as I grab her around the waist."
            show samantha reverse vaginal up
            pause 0.2
            show samantha reverse vaginal down at startle(0.05,-10)
            pause 0.3
            show samantha reverse vaginal up
            pause 0.2
            show samantha reverse vaginal down at startle(0.05,-10)
            pause 0.3
            show samantha reverse vaginal up
            pause 0.3
            show samantha reverse vaginal down at startle(0.05,-10)
            "But then the sound turns into a moan as I begin to move too."
            "I know that Sam's loving this, so I don't waste any time either."
            "My first thrust into her goes all the way."
            "I literally push as deep as I can get."
            show samantha reverse vaginal up
            pause 0.2
            show samantha reverse vaginal down at startle(0.05,-10)
            pause 0.3
            show samantha reverse vaginal up
            pause 0.2
            show samantha reverse vaginal down at startle(0.05,-10)
            pause 0.3
            show samantha reverse vaginal up
            pause 0.3
            show samantha reverse vaginal down at startle(0.05,-10)
            "And that's the way I keep it with every one that follows."
            samantha.say "Fuck..."
            show samantha reverse vaginal up smile
            samantha.say "That's so good..."
            samantha.say "Keep doing that!"
            if samantha.is_visibly_pregnant and randint(0, 1):
                "I guide her hips to keep the bounce smooth; she melts into the rhythm and pushes harder."
            "It's not like I need the encouragement!"
            show samantha reverse vaginal up
            pause 0.2
            show samantha reverse vaginal down at startle(0.05,-10)
            pause 0.3
            show samantha reverse vaginal up
            pause 0.2
            show samantha reverse vaginal down at startle(0.05,-10)
            pause 0.3
            show samantha reverse vaginal up
            pause 0.3
            show samantha reverse vaginal down at startle(0.05,-10)
            "Each thrust feels better than the last."
            "Like I'm going deeper than ever before."
            "And before too long I can feel Sam starting to twitch in my grasp."
            show samantha reverse vaginal down pleasure
            "It feels like she's about to cum."
            show samantha reverse vaginal up
            pause 0.2
            show samantha reverse vaginal down at startle(0.05,-10)
            pause 0.3
            show samantha reverse vaginal up
            pause 0.2
            show samantha reverse vaginal down at startle(0.05,-10)
            pause 0.3
            show samantha reverse vaginal up
            pause 0.3
            show samantha reverse vaginal down with vpunch
            "And then she does, gasping and pushing down harder than ever."
            "That's more than enough for her to take me with her too!"
            call cum_reaction (samantha, 'vaginal', sexperience_min) from _call_cum_reaction_154
            if _return == "vaginal_outside":
                "I'd love nothing more than to just keep right on going."
                "But as we didn't use a condom, I have no choice."
                "I make sure that I have a firm grip on Sam."
                show samantha reverse -vaginal up
                pause 0.3
                show sexinserts samantha belly zorder 1 at center, zoomAt(1, (-120, 970))
                show samantha reverse down
                with vpunch
                "And then I pull out before it's too late."
                "Sam arches her back as I do so, moaning at the sensation."
                show sexinserts samantha belly cum zorder 1 at center, zoomAt(1, (-120, 970))
                show samantha reverse cumshot
                with vpunch
                "Then I shoot my load, spattering her belly with cum."
                if FACIAL and randint(0, 1):
                    "She wipes a stripe off her cheek with the back of her hand; now her stomach matches her face."
                hide sexinserts
                $ samantha.sub += 1
            elif _return == "vaginal_condom":
                "Neither of us is going to stop before we're done."
                "Which makes me glad that we remembered to use a condom!"
                "I keep a firm hold on Sam as I shoot my load."
                show samantha reverse vaginal up
                pause 0.3
                show samantha reverse vaginal down creampie with vpunch
                "And she arches her back as I do so."
                show samantha reverse vaginal orgasm with vpunch
                if samantha.flags.engaged and randint(0, 1):
                    "Her wedding ring flashes as she clenches my knees and rides the aftershocks."
                "From the sounds that she's making, I know that she's enjoying it."
                "Maybe even as much as I am!"
                $ samantha.love += 1
            elif _return == "vaginal_inside_pill":
                samantha.say "Keep going..."
                samantha.say "I'm on...the pill!"
                "I silently thank Sam for reminding me."
                show samantha reverse vaginal up
                pause 0.3
                show samantha reverse vaginal down creampie with vpunch
                "And I keep a firm hold on her as I shoot my load."
                show samantha reverse vaginal creampie with vpunch
                "And she arches her back as I do so."
                show samantha reverse vaginal ahegao with vpunch
                if samantha.piercings.nipples.worn and randint(0, 1):
                    "Her nipple piercing stand tight when the climax hits."
                "From the sounds that she's making, I know that she's enjoying it."
                "Maybe even as much as I am!"
                $ samantha.love += 2
            elif _return == "vaginal_inside_pregnant":
                samantha.say "Keep going..."
                samantha.say "I'm...pregnant..."
                samantha.say "Remember?"
                "I shake my head, wondering how Sam could imagine I'd forget."
                show samantha reverse vaginal up
                pause 0.3
                show samantha reverse vaginal down creampie with vpunch
                "And I keep a firm hold on her as I shoot my load."
                show samantha reverse vaginal creampie with vpunch
                "And she arches her back as I do so."
                show samantha reverse vaginal ahegao with vpunch
                if samantha.flags.toldpreg and randint(0, 1):
                    "I brush her belly with my fingertips for a heartbeat; ours."
                elif samantha.flags.NPCpregnancy == "ryan" and randint(0, 1):
                    "She whispers 'steady' and I keep her hips cradled until her breathing slows."
                "From the sounds that she's making, I know that she's enjoying it."
                "Maybe even as much as I am!"
                $ samantha.love += 2
            elif _return == "vaginal_inside_mad":
                samantha.say "Stop it..."
                samantha.say "You have to pull out..."
                samantha.say "NOW!"
                "It's just then that I remember we didn't use protection."
                "I try to pull out and Sam tries to clamber off me."
                show samantha reverse vaginal up
                pause 0.3
                show samantha reverse vaginal down creampie with vpunch
                "But it's too late, as I'm already shooting my load."
                show samantha reverse vaginal creampie with vpunch
                $ samantha.impregnate()
                "Sam arches her back as I do so."
                "And from the sounds that she's making, I know she's as horrified as me!"
                $ samantha.love -= 5
            elif _return == "vaginal_inside_happy":
                samantha.say "Keep going..."
                samantha.say "Don't stop..."
                samantha.say "I won't let you!"
                "It's just then that I remember we didn't use protection."
                "I try to pull out, but Sam presses down with all her weight."
                show samantha reverse vaginal up
                pause 0.3
                show samantha reverse vaginal down creampie with vpunch
                "And she holds me there as I shoot my load."
                show samantha reverse vaginal creampie with vpunch
                $ samantha.impregnate()
                "Sam arches her back as I do so."
                "From the sounds that she's making, I know that she's enjoying it."
                show samantha reverse vaginal ahegao
                if FACIAL and randint(0, 1):
                    "Her face is still glazed; she grins over her shoulder while my spend warms her deep inside."
                "But I'm horrified by what just happened."
                $ samantha.love += 5
    return

label samantha_fuck_date_cowgirl(sexperience_min):
    scene samantha cowgirl with fade
    samantha.say "You want me to show you what happens next?"
    if samantha.flags.nickname == "cupcake":
        mike.say "Please, Cupcake!"
    else:
        mike.say "Please, Sam!"
    mike.say "You have to show me!"
    if samantha.flags.engaged and randint(0, 1):
        "Her wedding ring flashes as she poises over me; every little shine makes my pulse jump."
    elif samantha.piercings.navel.worn and randint(0, 1):
        "When she leans forward, the jewel in her navel gives a wicked gleam."
    elif FACIAL and randint(0, 1):
        "A glossy sheen still clings to her cheek; she licks a stripe from her lip and smirks."
    if samantha.is_visibly_pregnant and randint(0, 1):
        "Her belly rises and falls; she sets my hands where she wants support before she sinks down."
    if samantha.is_sex_slave and randint(0, 1):
        samantha.say "Your slave will ride however you command."
    elif samantha.sub >= 70 and randint(0, 1):
        samantha.say "Tell me what to do."
    elif samantha.sub < 30 and randint(0, 1):
        samantha.say "Let's start slow... then ruin me."
    samantha.say "Okay, [hero.name], okay."
    samantha.say "What happens next is that you wake up."
    samantha.say "And you tell me where you want me to put it!"
    menu:
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "I'm still nodding like a fool as Sam squeezes my cock again."
            "In fact I'm enjoying the feeling so much that I almost forget her question."
            "I guess that's why she gives it another squeeze, extra hard this time!"
            mike.say "Urgh..."
            mike.say "Ass!"
            mike.say "I want it in your ass!"
            "Sam's eyes go wide as she hears what I just said."
            samantha.say "Whoa...that never happened in my fantasy!"
            samantha.say "But sure thing, [hero.name]."
            samantha.say "We can do that!"
            "Sam lifts herself up, spreading her thighs a little wider apart."
            show samantha cowgirl up with fade
            if samantha.piercings.clit.worn and randint(0, 1):
                "When she reaches back to guide me, a cool piercing kisses my crown and she jolts."
            "And then she guides my cock back there, lowering her ass as she does so."
            samantha.say "Mmm..."
            samantha.say "We're going to have to take this slow, okay?"
            if samantha.flags.nickname == "cupcake":
                mike.say "Sure thing, Cupcake!"
            else:
                mike.say "Sure thing, Sam!"
            mike.say "Whatever you say."
            "Sam nods, and then closes her eyes."
            if samantha.is_visibly_pregnant and randint(0, 1):
                "I steady her with one palm beneath her belly while she settles."
            "That done, she begins to push my cock between her buttocks."
            "Not only do I feel everything that follows..."
            "I'm also treated to the expression on Sam's face."
            "As well as the sounds that she makes as she sinks down onto me."
            show samantha cowgirl down anal
            "I see a little trepidation and a tiny amount of pain at first."
            "But that's just in the first few moments as Sam's body resists."
            "Soon enough her muscles surrender to the inevitable."
            show samantha cowgirl up
            "And the look on her face becomes one of blissful acceptance."
            "At the same time, she slides down my cock, swallowing it whole."
            samantha.say "Oh fuck..."
            samantha.say "That feels..."
            show samantha cowgirl pleasure
            samantha.say "So good!"
            if samantha.flags.engaged and randint(0, 1):
                "Her wedding ring bites her palm when she grips my chest for balance."
            elif samantha.piercings.nipples.worn and randint(0, 1):
                "Her nipples piercings tug and sway when her hands clamp over her breasts."
            "I feel Sam almost quivering as my cock fills her ass."
            "And I get the urge to take matters into my own hands."
            "After all, she already said this wasn't part of her fantasy."
            "So I guess that means I'm the one in charge of where this goes from here."
            show samantha cowgirl down
            "I reach up, placing my hands on Sam's breasts."
            if samantha.sub >= 70 and randint(0, 1):
                samantha.say "Hold me down—I'll take it."
            elif samantha.sub < 30 and randint(0, 1):
                samantha.say "Easy… then harder. Please."
            "And without asking for permission, I start to move inside her."
            show samantha cowgirl up
            pause 0.4
            show samantha cowgirl down
            pause 0.4
            show samantha cowgirl up
            pause 0.4
            show samantha cowgirl down
            pause 0.4
            show samantha cowgirl up
            pause 0.4
            show samantha cowgirl down
            "I go slowly at first, watching how she reacts."
            "But it doesn't take long for Sam to begin moaning."
            show samantha cowgirl up
            pause 0.4
            show samantha cowgirl down at startle(0.05,-10)
            pause 0.4
            show samantha cowgirl up
            pause 0.4
            show samantha cowgirl down at startle(0.05,-10)
            pause 0.4
            show samantha cowgirl up
            pause 0.4
            show samantha cowgirl down at startle(0.05,-10)
            "Her head falls forwards, making me think she's about to collapse."
            "Then she braces herself and I see that she's actually nodding."
            "I don't need any clearer signal than that."
            show samantha cowgirl up speed
            pause 0.2
            show samantha cowgirl down at startle(0.05,-10)
            pause 0.3
            show samantha cowgirl up
            pause 0.2
            show samantha cowgirl down at startle(0.05,-10)
            pause 0.3
            show samantha cowgirl up
            pause 0.2
            show samantha cowgirl down at startle(0.05,-10)
            "So I begin to pick up speed and thrust harder than before."
            "Sam keeps on nodding as I start to really pound away at her."
            "Before I was worried that this would be too much."
            "But she's taking all that I have to give."
            show samantha cowgirl up speed
            pause 0.2
            show samantha cowgirl down at startle(0.05,-10)
            pause 0.3
            show samantha cowgirl up
            pause 0.2
            show samantha cowgirl down at startle(0.05,-10)
            pause 0.3
            show samantha cowgirl up
            pause 0.2
            show samantha cowgirl down at startle(0.05,-10)
            "And from the looks of it, she's actually asking for more!"
            "Pretty soon I'm going as hard and fast as I possibly can."
            show samantha cowgirl up speed
            pause 0.2
            show samantha cowgirl down at startle(0.05,-10)
            pause 0.3
            show samantha cowgirl up
            pause 0.2
            show samantha cowgirl down at startle(0.05,-10)
            pause 0.3
            show samantha cowgirl up
            pause 0.2
            show samantha cowgirl down at startle(0.05,-10)
            "Yet Sam is still keeping pace and nodding her head."
            "And I'm starting to worry that she's going to be the one to wear me out!"
            "In fact..."
            show samantha cowgirl down
            "Yeah, I'm going to..."
            if samantha.flags.nickname == "cupcake":
                mike.say "Cupcake..."
            else:
                mike.say "Sam..."
            mike.say "I'm gonna cum!"
            call cum_reaction (samantha, 'anal', sexperience_min) from _call_cum_reaction_155
            if _return == 'anal_inside':
                "I have no idea if Sam even heard what I just said."
                show samantha cowgirl up speed
                pause 0.2
                show samantha cowgirl down at startle(0.05,-10)
                pause 0.3
                show samantha cowgirl up
                pause 0.2
                show samantha cowgirl down at startle(0.05,-10)
                pause 0.3
                show samantha cowgirl up
                pause 0.2
                show samantha cowgirl down -speed with vpunch
                "Because she doesn't stop for a moment, just keeps on going."
                "A few seconds later I feel myself losing it."
                show samantha cowgirl creampie with vpunch
                "As my cocks as deep into her as it can go, I shoot my load."
                show samantha cowgirl orgasm with vpunch
                if samantha.flags.engaged and randint(0, 1):
                    "Her wedding ring digs into my shoulder as she clutches me through the tremors."
                "Now Sam reacts, tossing back her head and wailing."
                "I think she's cumming too, her entire body shaking and quivering."
                $ samantha.love += 2
                $ samantha.sub += 1
            elif _return == 'anal_outside':
                "Not waiting for permission from Sam, I lift her up."
                "And at the same time I pull my cock out of her too."
                show samantha cowgirl up -anal orgasm
                pause 0.2
                show sexinserts samantha chest zorder 1 at center, zoomAt(1, (670, 870))
                show sexinserts samantha belly as bellycum zorder 2 at center, zoomAt(1, (-120, 1010))
                show samantha cowgirl down
                with vpunch
                "Now Sam reacts, tossing back her head and wailing."
                "I think she's cumming too, her entire body shaking and quivering."
                show samantha cowgirl cumshot with vpunch
                "A few seconds later I feel myself losing it."
                show sexinserts samantha chest cum zorder 1 at center, zoomAt(1, (670, 870))
                show sexinserts samantha belly cum as bellycum zorder 2 at center, zoomAt(1, (-120, 1010))
                show samantha cowgirl -cumshot cum onbody -speed
                with vpunch
                "And I shoot my load over Sam's exposed belly."
                if FACIAL and randint(0, 1):
                    "She wipes a finger along her cheek and laughs—now her stomach matches her face."
                hide sexinserts
                hide bellycum
                $ samantha.sub += 2
                $ samantha.love += 1
            $ samantha.flags.anal += 1
        "Fuck her pussy":
            "I'm still nodding like a fool as Sam squeezes my cock again."
            "In fact I'm enjoying the feeling so much that I almost forget her question."
            "I guess that's why she gives it another squeeze, extra hard this time!"
            mike.say "Urgh..."
            mike.say "Pussy!"
            mike.say "I want it in your pussy!"
            "Sam laughs with evident delight."
            samantha.say "Sure thing, [hero.name]."
            samantha.say "We can do that!"
            call check_condom_usage (samantha) from _call_check_condom_usage_99
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show samantha cowgirl condom
            "Sam raises herself up and pulls my cock towards her at the same time."
            "And I find myself gasping again as she rubs it against the lips of her pussy."
            if samantha.piercings.clit.worn and randint(0, 1):
                "The crown taps a cool piecing; she shivers and lines me up again."
            mike.say "Oh fuck..."
            show samantha cowgirl up
            if samantha.flags.nickname == "cupcake":
                mike.say "Cupcake..."
            else:
                mike.say "Sam..."
            if samantha.flags.engaged and randint(0, 1):
                "Her wedding ring flashes when she braces on my chest to sink down."
            samantha.say "Save a little something for later, [hero.name]."
            samantha.say "You haven't seen anything yet!"
            "Without waiting a second longer, Sam pushes herself down."
            show samantha cowgirl down vaginal
            if samantha.is_visibly_pregnant and randint(0, 1):
                "I steady her hips so the motion stays smooth; she melts into the support."
            elif samantha.piercings.navel.worn and randint(0, 1):
                "Her navel jewel glints as she swallows me inch by inch."
            elif FACIAL and randint(0, 1):
                "A pearly sheen on her cheek catches the light when she throws her head back."
            "Somehow she's managed to get herself into the perfect position."
            "And I only feel the weight of her body pressing down on me for a moment."
            "Because a second later I feel myself sinking into her."
            "Sam closes her eyes and opens her mouth as it happens."
            "Which means I can see what she's feeling written all over her face."
            samantha.say "Oh yeah..."
            show samantha cowgirl up pleasure
            samantha.say "That's...that's it..."
            samantha.say "I...I always hoped..."
            if samantha.flags.nickname == "cupcake":
                mike.say "Cupcake..."
            else:
                mike.say "Sam..."
            mike.say "Is it like you thought it'd be?"
            mike.say "Like in your fantasy?"
            show samantha cowgirl down
            "Sam shakes her head, still holding her eyes closed."
            samantha.say "No..."
            samantha.say "It's..."
            show samantha cowgirl up
            samantha.say "Better!"
            if samantha.is_sex_slave and randint(0, 1):
                samantha.say "Use your slave's body. Make it real."
            "As if to underline the point, Sam begins to grind on me."
            "Slowly at first, she works herself up and down on my cock."
            show samantha cowgirl up
            pause 0.4
            show samantha cowgirl down
            pause 0.4
            show samantha cowgirl up
            pause 0.4
            show samantha cowgirl down
            pause 0.4
            show samantha cowgirl up
            pause 0.4
            show samantha cowgirl down
            "It feels incredible, making me want to lie back and leave her to it."
            "But then I feel her hands grabbing my wrists."
            "Sam pulls my arms up, pressing my hands against her breasts."
            if samantha.piercings.nipples.worn and randint(0, 1):
                "Her nipples piercings press into my palms; the tug makes her gasp."
            show samantha cowgirl up
            samantha.say "[hero.name]..."
            samantha.say "Make the fantasy come true..."
            samantha.say "Fuck me hard!"
            samantha.say "And make me cum!"
            show samantha cowgirl up
            pause 0.4
            show samantha cowgirl down at startle(0.05,-10)
            pause 0.4
            show samantha cowgirl up
            pause 0.4
            show samantha cowgirl down at startle(0.05,-10)
            pause 0.4
            show samantha cowgirl up
            pause 0.4
            show samantha cowgirl down at startle(0.05,-10)
            "Before I was ready to let Sam do all the hard work."
            "But her words are like a command that I can't ignore."
            "And I find myself springing into life."
            "My hands move over her body until they rest on her waist."
            "Then I tighten my grip, holding her firmly."
            show samantha cowgirl up speed
            pause 0.2
            show samantha cowgirl down at startle(0.05,-10)
            pause 0.3
            show samantha cowgirl up
            pause 0.2
            show samantha cowgirl down at startle(0.05,-10)
            pause 0.3
            show samantha cowgirl up
            pause 0.2
            show samantha cowgirl down at startle(0.05,-10)
            "That done, I begin to thrust upwards and into her."
            "The moment I do that, it's Sam's turn to start gasping."
            "And at the same time I can see that she's also nodding."
            "In fact she's moving her head in an almost desperate manner."
            "Part of me still can't believe this is happening."
            "Was she telling me the truth just now?"
            show samantha cowgirl up speed
            pause 0.2
            show samantha cowgirl down at startle(0.05,-10)
            pause 0.3
            show samantha cowgirl up
            pause 0.2
            show samantha cowgirl down at startle(0.05,-10)
            pause 0.3
            show samantha cowgirl up
            pause 0.2
            show samantha cowgirl down at startle(0.05,-10)
            "Is this really a fantasy for Sam as much as it is for me?"
            "All I can say is that it feels so right."
            "So much better than I ever imagined it could."
            show samantha cowgirl up speed
            pause 0.2
            show samantha cowgirl down at startle(0.05,-10)
            pause 0.3
            show samantha cowgirl up
            pause 0.2
            show samantha cowgirl down at startle(0.05,-10)
            pause 0.3
            show samantha cowgirl up
            pause 0.2
            show samantha cowgirl down at startle(0.05,-10)
            "The faster I go and the more effort I put in, the better it gets too."
            "Sam doesn't hesitate for a moment either."
            "She takes everything that I have to give her."
            show samantha cowgirl up speed
            pause 0.2
            show samantha cowgirl down at startle(0.05,-10)
            pause 0.3
            show samantha cowgirl up
            pause 0.2
            show samantha cowgirl down at startle(0.05,-10)
            pause 0.3
            show samantha cowgirl up
            pause 0.2
            show samantha cowgirl down at startle(0.05,-10)
            if samantha.flags.engaged and randint(0, 1):
                "Her wedding ring flashes each time she plants her hands on my chest."
            "Time seems to lose all meaning as we go at it."
            "And part of me wishes that this could last forever."
            "But then I feel Sam stiffen, and she gasps out the words..."
            samantha.say "Ah..."
            samantha.say "I..."
            samantha.say "I'm going to..."
            show samantha cowgirl up speed pleasure
            pause 0.2
            show samantha cowgirl down at startle(0.05,-10)
            pause 0.3
            show samantha cowgirl up
            pause 0.2
            show samantha cowgirl down at startle(0.05,-10)
            pause 0.3
            show samantha cowgirl up
            pause 0.2
            show samantha cowgirl down at startle(0.05,-10)
            "Sam cums before she can finish speaking."
            "She bears down on me as she does so, taking me with her."
            call cum_reaction (samantha, 'vaginal', sexperience_min) from _call_cum_reaction_156
            if _return == "vaginal_outside":
                "What I really want to do is keep right on going."
                "But we didn't bother to use any kind of protection."
                "So I use the last of my strength to lift Sam off me."
                show samantha cowgirl up -vaginal orgasm
                pause 0.2
                show sexinserts samantha chest zorder 1 at center, zoomAt(1, (670, 870))
                show sexinserts samantha belly as bellycum zorder 2 at center, zoomAt(1, (-120, 1010))
                show samantha cowgirl down with vpunch
                "She moans and protests as I pull my cock out of her."
                show samantha cowgirl -vaginal cumshot with vpunch
                pause 0.4
                show sexinserts samantha chest cum zorder 1 at center, zoomAt(1, (670, 870))
                show sexinserts samantha belly cum as bellycum zorder 2 at center, zoomAt(1, (-120, 1010))
                show samantha cowgirl -cumshot cum onbody -speed
                with vpunch
                "And when I cum a moment later, it spatters over her belly."
                if FACIAL and randint(0, 1):
                    "She drags a finger across her cheek and then down her stomach, smiling at the matching shine."
                "Then she collapses atop me, panting and spent."
                $ samantha.sub += 1
                hide sexinserts
                hide bellycum
            elif _return == "vaginal_condom":
                "Luckily for me, we remembered to use a condom."
                "So all I have to do is hold on and ride it out."
                show samantha cowgirl up speed
                pause 0.2
                show samantha cowgirl down at startle(0.05,-10)
                pause 0.3
                show samantha cowgirl up
                pause 0.2
                show samantha cowgirl down at startle(0.05,-10)
                pause 0.3
                show samantha cowgirl up
                pause 0.2
                show samantha cowgirl down with vpunch
                "Even with the protection, Sam still feels the sensation."
                show samantha cowgirl orgasm -speed with vpunch
                if samantha.flags.engaged and randint(0, 1):
                    "Her wedding ring flashes as she clutches my wrists and rides the aftershocks."
                "She moans and twitches as she rides me until the end."
                with vpunch
                "Breathing hard, she stays astride and reaches down to the base."
                "Two fingers pinch the rim and she eases the condom off my cock, careful not to spill."
                if samantha.piercings.tongue.worn and randint(0, 1):
                    "She teases the latex with her tongue stud, tasting the slick before bringing it to her mouth."
                "She lifts the heavy tip to her lips and sucks it clean, eyes on mine as she swallows."
                if randint(0, 1):
                    "A last pearly string clings to the rim; she purses her mouth and drains the rest."
                "Then she collapses atop me, panting and spent."
                $ samantha.love += 1
            elif _return == "vaginal_inside_pill":
                samantha.say "Don't stop!"
                show samantha cowgirl orgasm
                samantha.say "I'm on the pill!"
                "I silently thank Sam for the timely reminder."
                "Now all I have to do is hold on and ride it out."
                show samantha cowgirl up speed
                pause 0.2
                show samantha cowgirl down at startle(0.05,-10)
                pause 0.3
                show samantha cowgirl up
                pause 0.2
                show samantha cowgirl down at startle(0.05,-10)
                pause 0.3
                show samantha cowgirl up
                pause 0.2
                show samantha cowgirl down creampie -speed with vpunch
                if samantha.piercings.nipples.worn and randint(0, 1):
                    "Her nipples piercings stand taut when the climax breaks over her."
                "She moans and twitches as she rides me until the end."
                with vpunch
                "Then she collapses atop me, panting and spent."
                $ samantha.love += 2
            elif _return == "vaginal_inside_pregnant":
                samantha.say "Don't stop!"
                show samantha cowgirl orgasm
                samantha.say "I'm pregnant, remember!"
                "I silently thank Sam for the timely reminder."
                "Now all I have to do is hold on and ride it out."
                show samantha cowgirl up speed
                pause 0.2
                show samantha cowgirl down at startle(0.05,-10)
                pause 0.3
                show samantha cowgirl up
                pause 0.2
                show samantha cowgirl down at startle(0.05,-10)
                pause 0.3
                show samantha cowgirl up
                pause 0.2
                show samantha cowgirl down creampie -speed with vpunch
                if randint(0, 1):
                    "I brush her belly with my fingertips for a heartbeat and she smiles through a gasp."
                "She moans and twitches as she rides me until the end."
                with vpunch
                "Then she collapses atop me, panting and spent."
                $ samantha.love += 2
            elif _return == "vaginal_inside_mad":
                samantha.say "Stop!"
                show samantha cowgirl normal
                samantha.say "You can't cum inside me!"
                "Suddenly I remember that we're not using a condom."
                "I try to pull out, and Sam tries to scramble off me."
                "But it's already to late to stop it happening."
                show samantha cowgirl up speed orgasm
                pause 0.2
                show samantha cowgirl down at startle(0.05,-10)
                pause 0.3
                show samantha cowgirl up
                pause 0.2
                show samantha cowgirl down at startle(0.05,-10)
                pause 0.3
                show samantha cowgirl up
                pause 0.2
                show samantha cowgirl down creampie -speed with vpunch
                "Sam moans and twitches as she I shoot my load into her."
                with vpunch
                $ samantha.impregnate()
                "Then she collapses atop me, panting and spent."
                "Our eyes meet and we exchange a glance of sheer horror."
                "Neither of us can actually believe what just happened!"
                $ samantha.love -= 5
            elif _return == "vaginal_inside_happy":
                samantha.say "Don't stop!"
                show samantha cowgirl orgasm
                samantha.say "Keep going!"
                "Suddenly I remember that we're not using a condom."
                "I try to pull out, but Sam clings to me for all she's worth."
                show samantha cowgirl up speed
                pause 0.2
                show samantha cowgirl down at startle(0.05,-10)
                pause 0.3
                show samantha cowgirl up
                pause 0.2
                show samantha cowgirl down at startle(0.05,-10)
                pause 0.3
                show samantha cowgirl up
                pause 0.2
                show samantha cowgirl down creampie -speed with vpunch
                "She moans and twitches as she rides me until the end."
                with vpunch
                $ samantha.impregnate()
                "Then she collapses atop me, panting and spent."
                with vpunch
                if FACIAL and randint(0, 1):
                    "She cups her cum glazed face, grinning, while warmth spreads inside her."
                "She laughs like she's happy with what just happened."
                "But I can't believe what she just did!"
                $ samantha.love += 5
    return

label samantha_fuck_date_missionary(sexperience_min):
    $ result = randint(1, 2)
    if result == 1:
        call check_condom_usage (samantha) from _call_check_condom_usage_100
        if _return == False:
            return
        if not CONDOM:
            show samantha missionary pussy
        else:
            show samantha missionary condom
        if FACIAL:
            show samantha missionary cumface
        with fade
        if samantha.flags.engaged and randint(0, 1):
            "Her wedding ring flashes beside my cheek when she cups my face."
        elif FACIAL and randint(0, 1):
            "A glossy sheen still clings to her cheek; she licks a streak from her lip and smiles."
        if samantha.is_sex_slave and randint(0, 1):
            samantha.say "Your slave is open. Take me."
        elif samantha.sub >= 70 and randint(0, 1):
            samantha.say "Tell me how you want it."
        elif samantha.sub >= 30 and randint(0, 1):
            samantha.say "Slow… I want to feel every inch."
        "When I push myself into Sam, it's slowly and gently, so that I can feel every moment of the experience."
        if samantha.piercings.clit.worn and randint(0, 1):
            "A cool kiss of metal at her hood greets my first slide; she shivers and clutches my back."
        elif samantha.is_visibly_pregnant and randint(0, 1):
            "I cradle the curve of her belly with my palm so the motion stays smooth; she exhales a grateful yes."
        "Looking down on her as I do so, I can see the sensations spreading through her entire body at the same time."
        "My thrusts and motions are not translated into painful or taxing pangs, but rather they seem to create sympathetic ripples in her."
        "Sam moves beneath me in harmony, enjoying every moment of my presence inside of her."
        "At one moment her eyes are closed in seeming bliss, the next they open slowly and regard me with an almost sleepy delight."
        "As beautiful as I thought she was before this, she becomes even more so as she betrays her intimate pleasure through the expression upon her face."
        "Sam begins to massage her breasts again, reminding me of the sensation this gave me, even whilst my cock is deep inside of her."
        if samantha.piercings.nipples.worn and randint(0, 1):
            "Her nipples piercings press into my fingers when I cover her hands; the tug makes her gasp and arch."
        show samantha missionary closedeyes
        "She's panting now, building steadily in terms of her own pleasure."
        "Locks of her dirty-blonde hair begin to fall across her face as she rolls her head."
        "I can see sweat standing out on her forehead, neck and chest - a bead rolling over the curve of her belly."
        if samantha.piercings.navel.worn and randint(0, 1):
            "When her abs tense, the jewel in her navel twinkles up at me."
        elif samantha.flags.engaged and randint(0, 1):
            "Her wedding ring taps my shoulder when she clutches at me, a bright spark each time I bottom out."
        "Suddenly, all of these elements come together, and I see Sam in her entirety, become aware of how deep I am and how desperate she makes me."
        "That's it - I can't hold back any longer!"
        call cum_reaction (samantha, 'vaginal', sexperience_min) from _call_cum_reaction_157
        if _return == "vaginal_condom":
            "That little bit of foresight now means that I can stay right where I am as I finally cum."
            "My muscles jerk and buck, translating the physical manifestation of my orgasm into yet more pleasure for Sam."
            "She feels every last moment of my climax, clinging tightly to me as I try to push yet further into her."
            if samantha.flags.engaged and randint(0, 1):
                "Her wedding ring flashes when she wraps her arms around my neck and rides the aftershocks."
            "I'm flattered and delighted in equal measure when she begins to cum herself."
            if randint(0, 1):
                "Breathing hard, she pinches the rim and eases the condom off me, careful not to spill, then lifts the heavy tip to her lips and drinks it down with a satisfied swallow."
                if samantha.piercings.tongue.worn and randint(0, 1):
                    "Her tongue stud clicks faintly against the latex as she drains the last pearly thread."
            "We end together, slick with each other's sweat and still entangled in every way possible for two human bodies to be united as one."
            $ samantha.love += 1
        elif _return == "vaginal_outside":
            "Somehow, despite the chaos going on inside of my head, I manage to remember to pull out before I cum."
            show samantha missionary dickout
            "Sam writhes and moans in disappointment as I do so, her hands instinctively flying to her pussy to keep herself going."
            show samantha missionary normaleyes outside with vpunch
            "All I can do now is kneel over her and watch as my cum spatters down and over her."
            if FACIAL and randint(0, 1):
                "A new streak crosses the shine already glazing her cheek; she laughs and rubs it in with two fingers."
            elif samantha.flags.engaged and randint(0, 1):
                "She wipes a line with the back of her hand; the wedding ring smears a bright trail over her skin."
            show samantha missionary normaleyes outside2 with vpunch
            "Belly, breasts and face all get their fair share of the droplets, and Sam yelps in surprise as she's showered."
            if samantha.piercings.nipples.worn and randint(0, 1):
                "Pearls cling to the metal at her nipples before sliding down her curves."
            "But she soon recovers her composure, wiping the cum over her breasts and belly with one hand, even as she brings herself off with the other."
            $ samantha.sub += 1
        elif _return == "vaginal_inside_pill":
            "I can sense from Sam's body language that she's suddenly aware of the fact that I'm on the brink and inside of her without protection."
            "She begins to wriggle and squirm beneath me, as if trying to separate herself from me before I can lose it."
            "But by this time she's so entangled with me that she simply can't manage to escape of her own volition."
            "And I'm not about to oblige her by stopping what I'm doing in order to climb off of her either."
            samantha.say "Ah...ah...you're going to...cum inside of me..."
            "The desperation in her voice means that her words have the opposite effect to what she intended."
            with vpunch
            "A second later, I lose myself in her."
            show samantha missionary cumeyes inside with vpunch
            if samantha.flags.engaged and randint(0, 1):
                "Her wedding ring digs into my back as she clings and shakes."
            elif samantha.piercings.nipples.worn and randint(0, 1):
                "Her barbells stand taut under my thumbs when the climax breaks over her."
            samantha.say "OH FUCK!"
            samantha.say "OH YES...FUCK ME...PLEASE!!!"
            with vpunch
            "Funny, that's what I thought I'd been doing!"
            "By now I'm almost pushing Sam back into the pillows and the headboard, starting to feel fatigue creeping into my limbs."
            "Luckily, she's almost there, and just needs that last push over the edge."
            show samantha missionary ahegao
            "She cums with her head half-buried in the heaped pillows so that her cries are almost muffled and lost beneath them."
            $ samantha.love += 2
        elif _return in ["vaginal_inside_pregnant", "vaginal_inside_happy"]:
            "I can sense from Sam's body language that she's suddenly aware of the fact that I'm on the brink and inside of her without protection."
            "She begins to wriggle and squirm beneath me, as if trying to separate herself from me before I can lose it."
            "But by this time she's so entangled with me that she simply can't manage to escape of her own volition."
            "And I'm not about to oblige her by stopping what I'm doing in order to climb off of her either."
            samantha.say "Ah...ah...you're going to...cum inside of me..."
            "The desperation in her voice means that her words have the opposite effect to what she intended."
            with vpunch
            "A second later, I lose myself in her."
            $ samantha.impregnate()
            show samantha missionary cumeyes inside with vpunch
            if samantha.is_visibly_pregnant and randint(0, 1):
                "I press my palm to the curve of her belly for a heartbeat; she smiles through a gasp."
            samantha.say "OH FUCK!"
            samantha.say "OH YES...FUCK ME...PLEASE!!!"
            with vpunch
            "Funny, that's what I thought I'd been doing!"
            "Far from being mad at me for cumming inside of her unprotected, Sam seems to be swept away by the feeling."
            "She's kneading her breasts like they were balls of dough."
            "And her legs are wrapped around me so tight that it's actually getting a little hard to breathe."
            if samantha.is_sex_slave and randint(0, 1):
                samantha.say "Keep your seed in your slave."
            elif samantha.sub >= 70 and randint(0, 1):
                samantha.say "Don't you dare pull out."
            "She's not going to let go or stop demanding to be pleasured until she cums herself."
            "So I hurry to oblige."
            "By now I'm almost pushing Sam back into the pillows and the headboard, starting to feel fatigue creeping into my limbs."
            "Luckily, she's almost there, and just needs that last push over the edge."
            show samantha missionary ahegao
            "She cums with her head half-buried in the heaped pillows so that her cries are almost muffled and lost beneath them."
            $ samantha.love += 5
        elif _return == "vaginal_inside_mad":
            "I can sense from Sam's body language that she's suddenly aware of the fact that I'm on the brink and inside of her without protection."
            "She begins to wriggle and squirm beneath me, as if trying to separate herself from me before I can lose it."
            "But by this time she's so entangled with me that she simply can't manage to escape of her own volition."
            "And I'm not about to oblige her by stopping what I'm doing in order to climb off of her either."
            samantha.say "Ah...ah...you're going to...cum inside of me..."
            "The desperation in her voice means that her words have the opposite effect to what she intended."
            with vpunch
            "A second later, I lose myself in her."
            $ samantha.love -= 20
            $ samantha.impregnate()
            with vpunch
            if samantha.flags.engaged and randint(0, 1):
                "Her wedding ring flashes as her palm cracks across my cheek."
            samantha.say "Ugh...ugh...you...you came in me!"
            samantha.say "...you came inside of me!"
            "I'm still in her when she says this."
            mike.say "What can I say...I wanted you to have something to remember me by!"
            "Sam surprises me by giving me a swift slap across the face and dragging herself out from under me."
            samantha.say "Asshole - it'd serve you right if you got me pregnant!"
    else:

        scene bg black
        show samantha missionary at center, zoomAt(1.3, (640, 930))
        "she's laid out on her back."
        if samantha.sub >= 50:
            samantha.say "Oh, [hero.name] - please, be gentle?"
        else:
            samantha.say "[hero.name], I want you inside of me!"
        menu:
            "Fuck her pussy":
                "It's at times like this that I have to kind of mentally slap myself."
                "Because there's a part of me that would just stay right where I am."
                "Starting down at the sight of Sam, laid out naked in front of me."
                "Unable to actually believe that this is happening, that I get to do this with her!"
                "But that's not the kind of thinking that gets the job done."
                "So I direct my gaze downwards, glancing between Sam's thighs."
                "And the moment I do that, what I see does the trick."
                "That neat, perfect little pussy - that's what I want!"
                call check_condom_usage (samantha) from _call_check_condom_usage_158
                if _return == False:
                    return
                "Sam seals the deal a moment later, when she draws up her legs so that they part."
                "And at the same time she extends her arms, beckoning me to come to her."
                "Of course there's nothing that I want more in the world right now than to do that."
                "But I have to battle against my instinct to just thrown myself at her."
                "Because I don't want to come across as desperate - or to flatten her!"
                "And so I force myself to lie down slowly and gently atop her instead."
                show samantha missionary closedeyes
                "As I do so, Sam wraps her arms around me, pulling me closer still."
                "Somehow, while my mind is all over the place, we manage to pull it off perfectly."
                "By which I mean that we come together like two halves of a puzzle to form a whole."
                "Her limbs fold around me, and I wrap myself up in her too."
                "At the same time I can feel my manhood pressing against the lips of her sex."
                "Everything happening between us seems to be totally natural and instinctive."
                show samantha missionary normaleyes at center, traveling(1.0, 1.0, (640, 720))
                "And so when I begin to move, she matches my motions."
                "The head of my cock is already pressing against the lips of her pussy."
                "Every movement I make causing Sam to gasp at the sensation."
                "But there's no sense of me fumbling or struggling to know what to do next."
                "Instead I feel like I'm walking a linear, logical path that leads straight ahead."
                "With each pass, Sam yields a little more, relaxes just a fraction."
                "And I have to fight to keep from holding my breath every time."
                "Wondering if this is going to be the one that sees her open herself to me."
                "Soon the rhythm begins to take over, and I tune out just a little."
                "All of which means that when it does finally happen, I'm taken by surprise."
                hide samantha
                show samantha missionary cumeyes
                samantha.say "Oh..."
                samantha.say "Oh, [hero.name]..."
                mike.say "What the..."
                mike.say "Oh...oh fuck!"
                if CONDOM:
                    show samantha missionary condom
                else:
                    show samantha missionary pussy
                show samantha missionary closedeyes at startle(0.05,-10)
                "My eyes are wide and my mouth hanging open as I sink into Sam."
                "And I'm so shocked that I must he half the way into her before I regain my senses."
                "Which is easier said than done, as what I'm feeling is almost overwhelming."
                "Suddenly I'm filling her up more with each passing second."
                "Feeling everything that I wanted being thrust upon me all at once."
                "Thankfully I'm soon as deep as I can possibly go."
                "That means I can stop and take stock of the situation."
                "But again my unconscious mind seems to be in a position to take over."
                "Because as soon as I pause, it rebels against me."
                "The animal in me doesn't want to stop and think - all it wants is Sam."
                "And now that I'm buried inside of her, it's not going to be denied!"
                "All of a sudden my muscles tense and my limbs start to move."
                show samantha missionary at startle(0.05,-10)
                "I rise up and then sink down again, repeating the action as soon as it's done."
                show samantha missionary at startle(0.05,-10)
                pause 0.2
                show samantha missionary at startle(0.05,-10)
                "And I'm picking up speed too, going faster with each passing second."
                "Sam doesn't seem to be aware of the fact that I've totally lost control of myself."
                show samantha missionary at startle(0.05,-10)
                pause 0.2
                show samantha missionary at startle(0.05,-10)
                "She just clings onto me the whole time, likely overwhelmed by what I'm doing."
                "I have no idea of just how long I'm capable of keeping up this kind of pace."
                show samantha missionary at startle(0.05,-10)
                pause 0.2
                show samantha missionary at startle(0.05,-10)
                "And I can't seem to keep track of how long I've already been at it either."
                "There's nothing but the act of making love to Sam, nothing else matters."
                show samantha missionary at startle(0.05,-10)
                pause 0.2
                show samantha missionary at startle(0.05,-10)
                "So I keep on going, pounding away until the pressure builds to breaking point."
                "Only then do I remember what comes next."
                show samantha missionary at startle(0.05,-10)
                pause 0.2
                show samantha missionary at startle(0.05,-10)
                mike.say "Oh shit..."
                mike.say "I'm...I'm gonna cum!"
                call cum_reaction (samantha, 'vaginal', sexperience_min) from _call_cum_reaction_293
                if _return == "vaginal_outside":
                    "I need to make sure I don't let go inside of Sam."
                    "It's a pain, but we didn't bother to use a condom."
                    show samantha missionary dickout
                    "So I make sure to do it before the inevitable happens."
                    show samantha missionary cumeyes cumshot ahegao with vpunch
                    "Sam and I cum almost at the same moment, each affecting the other."
                    show samantha missionary outside2 with vpunch
                    "I feel her squeezing me tightly as I pull out of her."
                    show samantha missionary outside with vpunch
                    "And she's in the grips of her orgasm as I shoot my load over her belly."
                    if FACIAL and randint(0, 1):
                        show samantha missionary cumface
                        "A stray arc lands across her cheek; she rubs it in with two fingers and licks them clean."
                    show samantha missionary closedeyes with vpunch
                    "Luckily we're both laid down on the bed."
                    "So we can easily collapse into a heap afterwards."
                    $ samantha.sub += 1
                elif _return == "vaginal_condom":
                    "Thankfully we took time to use a condom, so there's no need to worry."
                    with vpunch
                    "And that's all for the good, because a second later, my orgasm hits like a tidal wave!"
                    with vpunch
                    "My whole body stiffens and I make one final thrust into Sam, shooting my load as I do so."
                    show samantha missionary cumeyes ahegao with vpunch
                    "The sensation seems to be more than enough to make her cum too, clinging onto me tighter than before."
                    show samantha missionary closedeyes
                    "But once it's over, both of us seem to flop at the exact same moment."
                    "Collapsing into a helpless pile of sweaty limbs, chests heaving and hearts pounding."
                    $ samantha.love += 1
                elif _return == "vaginal_inside_pregnant":
                    samantha.say "It's okay..."
                    samantha.say "I'm pregnant...remember?"
                    "I get the urge to ask how in the hell I could ever forget!"
                    with vpunch
                    "But a second later, my orgasm hits like a tidal wave!"
                    with vpunch
                    "My whole body stiffens and I make one final thrust into Sam, shooting my load as I do so."
                    show samantha missionary cumeyes ahegao inside with vpunch
                    "The sensation seems to be more than enough to make her cum too, clinging onto me tighter than before."
                    show samantha missionary closedeyes
                    "But once it's over, both of us seem to flop at the exact same moment."
                    "Collapsing into a helpless pile of sweaty limbs, chests heaving and hearts pounding."
                elif _return == "vaginal_inside_pill":
                    samantha.say "It's okay..."
                    samantha.say "I'm on the Pill...remember?"
                    "I get the urge to thank Sam for reminding me in time."
                    with vpunch
                    "But a second later, my orgasm hits like a tidal wave!"
                    with vpunch
                    "My whole body stiffens and I make one final thrust into Sam, shooting my load as I do so."
                    show samantha missionary cumeyes ahegao inside with vpunch
                    "The sensation seems to be more than enough to make her cum too, clinging onto me tighter than before."
                    show samantha missionary closedeyes
                    "But once it's over, both of us seem to flop at the exact same moment."
                    "Collapsing into a helpless pile of sweaty limbs, chests heaving and hearts pounding."
                elif _return == "vaginal_inside_mad":
                    samantha.say "Pull out - quickly!"
                    samantha.say "No condom, remember?!?"
                    with vpunch
                    "I make to do as Sam says, but a second later, my orgasm hits like a tidal wave!"
                    show samantha missionary cumeyes ahegao inside with vpunch
                    "My whole body stiffens and I make one final thrust into Sam, shooting my load as I do so."
                    with vpunch
                    "The sensation seems to be more than enough to make her cum too, clinging onto me tighter than before."
                    "But once it's over, both of us seem to flop at the exact same moment."
                    "Collapsing into a helpless pile of sweaty limbs, chests heaving and hearts pounding."
                    play sound spank
                    scene bg bedroom1
                    show samantha naked angry at center, zoomAt(1.5, (640, 1040))
                    with hpunch
                    $ samantha.love -= 20
                    $ samantha.impregnate()
                    "That is until Sam hauls herself up and swings her hand, slapping me across the face."
                    samantha.say "You careless moron, [hero.name]..."
                    samantha.say "It'd serve you right if I do end up getting pregnant!"
                elif _return == "vaginal_inside_happy":
                    mike.say "Oh shit...I need to pull out!"
                    mike.say "No condom, remember?!?"
                    "I make to pull out of Sam, but to my surprise, she clings onto me."
                    with vpunch
                    "A second later, my orgasm hits like a tidal wave!"
                    show samantha missionary cumeyes ahegao inside with vpunch
                    "My whole body stiffens and I make one final thrust into Sam, shooting my load as I do so."
                    with vpunch
                    "The sensation seems to be more than enough to make her cum too, clinging onto me tighter than before."
                    "But once it's over, both of us seem to flop at the exact same moment."
                    show samantha missionary closedeyes
                    "Collapsing into a helpless pile of sweaty limbs, chests heaving and hearts pounding."
                    "That is until Sam hauls herself up, a smile on her face."
                    $ samantha.impregnate()
                    mike.say "Why...why did you do that?"
                    mike.say "Are you totally crazy?!?"
                    show samantha missionary normaleyes
                    samantha.say "Mmm...I can feel your seed inside of me, [hero.name]..."
                    samantha.say "With any luck, you just got me pregnant!"
                    $ samantha.love += 5
            "Fuck her ass":
                "It's at times like this that I have to kind of mentally slap myself."
                "Because there's a part of me that would just stay right where I am."
                "Starting down at the sight of Sam, laid out naked in front of me."
                "Unable to actually believe that this is happening, that I get to do this with her!"
                "But that's not the kind of thinking that gets the job done."
                "So I direct my gaze downwards, glancing between Sam's thighs."
                "And the moment I do that, what I see does the trick."
                "That neat, perfect little ass - that's what I want!"
                "Sam seals the deal a moment later, when she draws up her legs so that they part."
                "And at the same time she extends her arms, beckoning me to come to her."
                "Of course there's nothing that I want more in the world right now than to do that."
                "But I have to battle against my instinct to just thrown myself at her."
                "Because I don't want to come across as desperate - or to flatten her!"
                "And so I force myself to lie down slowly and gently atop her instead."
                show samantha missionary closedeyes
                "As I do so, Sam wraps her arms around me, pulling me closer still."
                "Somehow, while my mind is all over the place, we manage to pull it off perfectly."
                "By which I mean that we come together like two halves of a puzzle to form a whole."
                "Her limbs fold around me, and I wrap myself up in her too."
                "At the same time I can feel my manhood pressing against the edge of her hole."
                "Everything happening between us seems to be totally natural and instinctive."
                show samantha missionary normaleyes at startle(0.05,-10)
                "And so when I begin to move, she matches my motions."
                "The head of my cock is already pressing against the muscles of her ass."
                "Every movement I make causing Sam to gasp at the sensation."
                "But there's no sense of me fumbling or struggling to know what to do next."
                "Instead I feel like I'm walking a linear, logical path that leads straight ahead."
                "With each pass, Sam yields a little more, relaxes just a fraction."
                "And I have to fight to keep from holding my breath every time."
                "Wondering if this is going to be the one that sees her open herself to me."
                "Soon the rhythm begins to take over, and I tune out just a little."
                "All of which means that when it does finally happen, I'm taken by surprise."
                show samantha missionary cumeyes
                samantha.say "Oh..."
                samantha.say "Oh, [hero.name]..."
                mike.say "What the..."
                mike.say "Oh...oh fuck!"
                show samantha missionary closedeyes anal at center, traveling(1.1, 1.0, (640, 760))
                "My eyes are wide and my mouth hanging open as I sink into Sam."
                "And I'm so shocked that I must he half the way into her before I regain my senses."
                "Which is easier said than done, as what I'm feeling is almost overwhelming."
                "Suddenly I'm filling her up more with each passing second."
                "Feeling everything that I wanted being thrust upon me all at once."
                "Thankfully I'm soon as deep as I can possibly go."
                "That means I can stop and take stock of the situation."
                "But again my unconscious mind seems to be in a position to take over."
                "Because as soon as I pause, it rebels against me."
                "The animal in me doesn't want to stop and think - all it wants is Sam."
                "And now that I'm buried inside of her, it's not going to be denied!"
                "All of a sudden my muscles tense and my limbs start to move."
                show samantha missionary at startle(0.05,-10)
                "I rise up and then sink down again, repeating the action as soon as it's done."
                show samantha missionary at startle(0.05,-10)
                pause 0.2
                show samantha missionary at startle(0.05,-10)
                "And I'm picking up speed too, going faster with each passing second."
                "Sam doesn't seem to be aware of the fact that I've totally lost control of myself."
                show samantha missionary at startle(0.05,-10)
                pause 0.2
                show samantha missionary at startle(0.05,-10)
                "She just clings onto me the whole time, likely overwhelmed by what I'm doing."
                "I have no idea of just how long I'm capable of keeping up this kind of pace."
                show samantha missionary at startle(0.05,-10)
                pause 0.2
                show samantha missionary at startle(0.05,-10)
                "And I can't seem to keep track of how long I've already been at it either."
                "There's nothing but the act of making love to Sam, nothing else matters."
                show samantha missionary at startle(0.05,-10)
                pause 0.2
                show samantha missionary at startle(0.05,-10)
                "So I keep on going, pounding away until the pressure builds to breaking point."
                "Only then do I remember what comes next."
                show samantha missionary at startle(0.05,-10)
                pause 0.2
                show samantha missionary at startle(0.05,-10)
                mike.say "Oh shit..."
                mike.say "I'm...I'm gonna cum!"
                menu:
                    "Cum in her ass":
                        "Thankfully I chose to take Sam up the ass, so there's no need to worry about losing it inside of her."
                        show samantha missionary cumeyes ahegao with vpunch
                        "And that's all for the good, because a second later, my orgasm hits like a tidal wave!"
                        with vpunch
                        "My whole body stiffens and I make one final thrust into Sam, shooting my load as I do so."
                        with vpunch
                        "The sensation seems to be more than enough to make her cum too, clinging onto me tighter than before."
                        show samantha missionary closedeyes with vpunch
                        "But once it's over, both of us seem to flop at the exact same moment."
                        "Collapsing into a helpless pile of sweaty limbs, chests heaving and hearts pounding."
                        $ samantha.love += 2
                        $ samantha.sub += 1
                    "Pull out of her ass":
                        show samantha missionary dickout at center, zoomAt(1.0, (640, 720)) with vpunch
                        "It takes the last of my energy to manage to haul myself out of Sam's ass."
                        show samantha missionary cumeyes cumshot ahegao with vpunch
                        "And that's all for the good, because a second later, my orgasm hits like a tidal wave!"
                        show samantha missionary outside2 with vpunch
                        "My whole body stiffens and then releases, shooting my load over Sam as it does so."
                        show samantha missionary outside with vpunch
                        "The sensation seems to be more than enough to make her cum too, clinging onto me tighter than before."
                        show samantha missionary closedeyes with vpunch
                        "But once it's over, both of us seem to flop at the exact same moment."
                        "Collapsing into a helpless pile of sweaty limbs, chests heaving and hearts pounding."
                        $ samantha.sub += 2
                        $ samantha.love += 1
                $ samantha.flags.anal += 1
    return

label samantha_fuck_flat_doggy(sexperience_min):
    if game.days_played % 2 == 0:
        "Sam lands on her belly and I fall on top of her."
        scene bg black
        show samantha flat doggy bedroom
        with fade
        "This means my already stiffening cock is shoved between her buttocks."
        if samantha.flags.engaged and randint(0, 1):
            "Her wedding ring ticks the sheet when she braces under me."
        elif samantha.is_visibly_pregnant and randint(0, 1):
            "I cradle her belly with one palm so the slide stays smooth; she exhales a grateful yes."
        elif FACIAL and randint(0, 1):
            "A glossy sheen still clings to her cheek; she grins when I press close."
        "It's not exactly the most romantic methods of choosing where to put it."
        "But the yelp and the moan that follow it from Sam are more than enough for me."
        "And I try to make it look like that was my intent all along."
        show samantha flat doggy pleasure
        samantha.say "Oh...oh wow!"
        show samantha flat doggy normal
        samantha.say "I...I didn't know you were that kinky!"
        samantha.say "But if you insist..."
        "Sam obligingly raises her ass in the air as I probe for the right hole."
        if samantha.piercings.clit.worn and randint(0, 1):
            "A cool piercing kisses my crown when I slide lower; she jolts and pushes back harder."
        "And the moment she does so, we manage to meet in the middle."
        "This means that she's pushing up as I'm pushing down."
        "I'm pressing into her ass as she's wriggling herself onto my cock."
        show samantha flat doggy pleasure
        samantha.say "Yeah...yeah..."
        samantha.say "That feels good...really good!"
        show samantha flat doggy normal
        samantha.say "You can do that to me all night!"
        "I don't know if I can promise Sam to keep it up so long."
        "But I'll certainly do my best to make this a night she won't soon forget."
        "Sam's ass tries to resist me, going against the wishes of her head."
        "Her muscles contract, trying to keep my cock from getting any further."
        "But all that does is make me all the more determined to succeed."
        show samantha flat doggy anal
        "I push onwards, feeling those same muscles do all they can to resist."
        if samantha.piercings.nipples.worn and randint(0, 1):
            "Her nipples piercings press into my knuckles when I slide my hands under her chest; she gasps and arches."
        "And then I feel their resolve waver for a moment."
        "That's when I put in an extra ounce of effort."
        "And that's enough to see them quiver and then surrender."
        "I push my cock slowly but surely on, all the way into Sam's ass."
        "To me it feels incredible, like sinking into the very core of her."
        "But I can't even begin to imagine what Sam's feeling right now."
        "She squirms under me, almost like she's trying in vain to crawl away."
        "Her hands grasp at the bedclothes, like she's going to tear them the shreds."
        "Any other time and place, that all could have been taken for distress."
        show samantha flat doggy pleasure
        "But the moans that Sam's letting out and the way she's nodding her head..."
        "All of that speaks to the fact that she's overwhelmed with pleasure!"
        if samantha.is_sex_slave and randint(0, 1):
            samantha.say "Your slave is open... take everything."
        elif samantha.sub >= 70 and randint(0, 1):
            samantha.say "Hold me down. Use me."
        elif samantha.sub >= 30 and randint(0, 1):
            samantha.say "Start steady… then ruin me."
        "I can't hope to go as fast and hard as I could if I were fucking Sam's pussy."
        "Instead all of my energy goes into keeping up a steady pace."
        "The whole time I'm still fighting against the pressure of her muscles."
        "They may have surrendered enough to let me in."
        "But that doesn't mean they've completely given up the fight."
        "Every thrust that I make into Sam, they resist just a little."
        "Eating up another small amount of my reserves and making me tire a little more."
        "I try to ignore the sweat that's starting to run down my spine."
        "And instead I focus on what each and every thrust had on Sam."
        "Because the muscles of her ass are the only part of her still resisting me."
        "The rest of her body seem to have become limp."
        "She lies spread upon the bed beneath me, helpless and totally in my power."
        "Sam's not even able to nod anymore, her eyes beginning to roll back into her head."
        "Her mouth hangs open and her tongue is lolling out too."
        if samantha.piercings.tongue.worn and randint(0, 1):
            "Her tongue stud flashes when she moans into the pillow."
        "In fact I can't help wondering if she's even conscious!"
        "But that mystery is put to rest a moment later."
        "I can feel myself beginning to lose it, starting to cum."
        "I don't know why I feel compelled to warn Sam."
        "I mean, it's not like she can get pregnant with me fucking her ass, is it?"
        "But for whatever reason, I end up gasping out the words all the same."
        if samantha.flags.nickname == "cupcake":
            mike.say "C...Cupcake..."
        else:
            mike.say "S...Sam..."
        mike.say "Here...here it comes!"
        show samantha flat doggy ahegao
        "At the sound of my voice, Sam's head shoots up."
        "She looks over her shoulder at me, eyes still vacant."
        "And the look on her face is more one of confusion than recognition."
        "But there's no time for me to offer a better explanation..."
        menu:
            "Cum inside":
                show samantha flat doggy cum pleasure with hpunch
                "And that's because I shoot my load into her ass a moment later."
                with hpunch
                "If I wasn't as deep as I could get already, I am as I thrust forwards."
                show samantha flat doggy cum ahegao with hpunch
                "With my cock buried inside of her, Sam's helpless as I fill her to the brim."
                "All she can do is wriggle and squirm as her ass twitches around me."
                "There's cum dripping out of her before I'm done."
                if randint(0, 1):
                    "She reaches back, scoops what leaks onto her fingers, and brings it to her mouth with a hungry little swallow."
                "And when I finally pull my cock out of her, it trails from the tip."
                $ samantha.love += 1
            "Pull out":
                "Sam's eyes flare back to life a moment later."
                show samantha flat doggy normal out
                "And that's because I pull my cock straight out of her ass."
                "But the effect is only temporary, as she slumps down onto the bed."
                with hpunch
                "All she can do is lie there, panting and gasping as I let myself go."
                show samantha flat doggy ahegao cumshot with hpunch
                "Sam only manages the faintest gasps as I spatter her buttocks with cum."
                if randint(0, 1):
                    "She drags two fingers through the mess, smears it on her cheek, then licks them clean with a grin."
                elif FACIAL and randint(0, 1):
                    "The fresh streaks shine next to the glaze already on her face."
                with hpunch
                "But my own gasps are loud, ragged and utterly exhausted."
                $ samantha.sub += 1
        $ samantha.flags.anal += 1
    else:
        scene samantha flat doggy
        show samantha flat doggy bedroom
        with fade
        "Still holding my eye over her shoulder, Sam lowers herself onto my bed."
        "I watch spellbound as her ass rises up and wiggles right in front of me."
        if samantha.flags.engaged and randint(0, 1):
            "Her wedding ring flashes when she plants her hand for balance."
        elif samantha.is_visibly_pregnant and randint(0, 1):
            "She pats her belly and smiles; I nod and steady her hips as I climb behind."
        samantha.say "Well..."
        samantha.say "If you like it so much..."
        samantha.say "Why don't you come and get it?"
        "As if she needs to underline the point, Sam shakes her ass at me."
        "Those perfectly round buttocks seems to hypnotise me in that instant."
        "And I don't have a conscious thought in my head as I begin to move."
        "I'm nodding and automatically pulling off my clothes."
        "At the same time I'm walking towards the bed."
        "This means that I'm naked and climbing up behind Sam."
        "And I don't know what it would take to stop me getting to her right now."
        "Because there's nothing else in my head, other than grabbing that ass!"
        samantha.say "Mmm..."
        samantha.say "I've been waiting for this all night."
        samantha.say "Waiting to have your hands all over me!"
        "I don't need to say how much I've been waiting for this."
        "Or how excited I am to be getting my hands on Sam."
        "Because we can both feel just how hard my cock is!"
        "Sam lowers her belly down until she's laid on it."
        if samantha.piercings.navel.worn and randint(0, 1):
            "Her navel jewel shines when she settles flat."
        "And this means her ass rises up to meet me."
        samantha.say "What are you waiting for?"
        samantha.say "Come on and fuck me already!"
        menu:
            "Fuck her pussy":
                "I try not to throw myself too hastily onto Sam."
                "For one thing I'm worried about hurting her."
                "And for another I don't want to break my own bed!"
                "But even so, I still end up clambering atop her within seconds."
                "Much to her evident amusement and delight."
                show samantha flat doggy pleasure
                samantha.say "Oh oh!"
                show samantha flat doggy normal
                samantha.say "Someone's keen tonight!"
                call check_condom_usage (samantha) from _call_check_condom_usage_139
                if _return == False:
                    return
                if CONDOM:
                    show samantha flat doggy condom
                if samantha.piercings.clit.worn and randint(0, 1):
                    "The crown kisses a cool piercing as I line up; she shivers and pushes back."
                mike.say "With an ass like that..."
                mike.say "Can you blame me?!?"
                "Sam giggles and gives me a shake of her ass as a reward."
                "But she's not laughing for long, as I'm more than ready to go."
                "Instead, Sam begins to moan and gasp as I push between her legs."
                "She still has her ass raised in the air, so there's easy access."
                "And I can feel from the first moment of contact that she's ready for me."
                "In fact, Sam's so slick down there that my cock slides off her lips!"
                samantha.say "Oh no you don't!"
                "Now it's my turn to gasp in surprise."
                "Because Sam grabs hold of the shaft without warning."
                "And then she pushes it hard against the lips of her pussy."
                show samantha flat doggy vaginal
                "This is at the same time as I'm pushing to get in there as well."
                "So it doesn't take long for the inevitable to happen."
                show samantha flat doggy pleasure
                samantha.say "Ah..."
                samantha.say "Oh yeah..."
                samantha.say "Just...like...that!"
                if samantha.is_sex_slave and randint(0, 1):
                    samantha.say "Use your slave... deeper."
                elif samantha.sub >= 70 and randint(0, 1):
                    samantha.say "Hold my hips. Make me take it."
                elif samantha.sub < 30 and randint(0, 1):
                    samantha.say "Steady first… then harder."
                mike.say "Oh shit!"
                "Samantha opens for me like a flower."
                "My cock doesn't go all the way in, not at first."
                "Instead it sinks into her, inch by inch."
                "And every moment that it's happening is better than the last."
                if samantha.is_visibly_pregnant and randint(0, 1):
                    "I keep one hand under her belly so the rhythm stays smooth; she melts into the support."
                samantha.say "Mmm..."
                samantha.say "Don't...don't hold back..."
                samantha.say "I...I want it...hard!"
                "I'm nodding eagerly as Sam says all of this."
                "And I can already feel my body obeying her commands."
                "I don't honestly know if I could make myself hold back."
                "But that's not a on my mind as I want the exact same thing."
                "Almost desperate to please Sam, I begin to move ever faster."
                "From a standing start, I'm soon thrusting into her at speed."
                "And it feels almost as good as sinking in there slowly too!"
                show samantha flat doggy normal
                "For her part, Sam seems to know exactly what she wants."
                "As she happily takes everything that I have to give."
                "In fact, from the way she's nodding her head, I think she actually wants more!"
                show samantha flat doggy pleasure
                "Sam grabs handfuls of the bedclothes, like she's hanging on for dear life."
                "And I can feel her legs thumping the mattress behind me too."
                "Now I'm worried about her breaking the bed, rather than me!"
                "But that's not going to stop me from fucking her as hard as I can."
                "By now Sam seems to be groaning and gasping with every thrust I make."
                show samantha flat doggy ahegao
                "And when I catch a glimpse of her eyes, they're starting to glaze over."
                "I can feel her pussy starting to quiver around me too."
                "So my guess is that she's about to cum!"
                show samantha flat doggy pleasure
                "And I know that I can time my orgasm to hit when hers does."
                "If I can just push a little harder..."
                call cum_reaction (samantha, 'vaginal', sexperience_min) from _call_cum_reaction_263
                if _return == "vaginal_outside":
                    "I need to make sure I don't let go inside of Sam."
                    "It's a pain, but we didn't bother to use a condom."
                    show samantha flat doggy out
                    "So I make sure to do it before the inevitable happens."
                    "Sam and I cum almost at the same moment, each affecting the other."
                    with hpunch
                    "I feel her squeezing me tightly as I pull out of her."
                    show samantha flat doggy cumshot ahegao with hpunch
                    "And she's in the grips of her orgasm as I shoot my load over her buttocks."
                    if FACIAL and randint(0, 1):
                        "A stray arc lands across her cheek; she rubs it in with two fingers and licks them clean."
                    with hpunch
                    "Luckily we're both laid down on the bed."
                    "So we can easily collapse into a heap afterwards."
                    $ samantha.sub += 1
                elif _return == "vaginal_condom":
                    "I don't need to worry about letting go inside of Sam."
                    "Because we remembered to use protection before getting started."
                    "So all I have to do is let nature take it's course."
                    show samantha flat doggy ahegao with hpunch
                    "Sam and I cum almost at the same moment, each affecting the other."
                    with hpunch
                    "I feel her squeezing me tightly as I let go inside of her."
                    show samantha flat doggy out cum with hpunch
                    if randint(0, 1):
                        "Breathing hard, she pinches the rim and eases the condom off me, careful not to spill, then lifts the tip to her mouth and drinks it down, swallowing with a satisfied hum."
                        if samantha.piercings.tongue.worn and randint(0, 1):
                            "Her tongue stud clicks faintly on the latex as she drains the last pearly thread."
                    "Luckily we're both laid down on the bed."
                    "So we can easily collapse into a heap afterwards."
                    $ samantha.love += 1
                elif _return == "vaginal_inside_pill":
                    "I don't need to worry about letting go inside of Sam."
                    "Because she already told me she was on the pill."
                    "So all I have to do is let nature take it's course."
                    show samantha flat doggy cum ahegao with hpunch
                    "Sam and I cum almost at the same moment, each affecting the other."
                    with hpunch
                    "I feel her squeezing me tightly as I let go inside of her."
                    if samantha.flags.engaged and randint(0, 1):
                        "Her wedding ring digs into the sheet when she clutches it through the tremors."
                    with hpunch
                    "Luckily we're both laid down on the bed."
                    "So we can easily collapse into a heap afterwards."
                    $ samantha.love += 2
                elif _return == "vaginal_inside_pregnant":
                    "I don't need to worry about letting go inside of Sam."
                    "Because her belly keeps on reminding me she's already pregnant."
                    "So all I have to do is let nature take it's course."
                    show samantha flat doggy ahegao with hpunch
                    "Sam and I cum almost at the same moment, each affecting the other."
                    show samantha flat doggy cum with hpunch
                    "I feel her squeezing me tightly as I let go inside of her."
                    if randint(0, 1):
                        "I stroke the curve of her belly for a heartbeat; she smiles into the pillow."
                    with hpunch
                    "Luckily we're both laid down on the bed."
                    "So we can easily collapse into a heap afterwards."
                    $ samantha.love += 2
                elif _return == "vaginal_inside_mad":
                    show samantha flat doggy ahegao
                    samantha.say "NO!"
                    samantha.say "Pull out!"
                    samantha.say "You can't cum in me!"
                    "I'm so shocked by what Sam just said that I freeze in place."
                    "And in that short space of time, nature takes it's course."
                    with hpunch
                    "Sam and I cum almost at the same moment, each affecting the other."
                    show samantha flat doggy cum with hpunch
                    "I feel her squeezing me tightly as I let go inside of her."
                    with hpunch
                    $ samantha.impregnate()
                    mike.say "Oh shit..."
                    mike.say "What have we done?!?"
                    samantha.say "We...we fucked up!"
                    samantha.say "That's what we did!"
                    $ samantha.love -= 5
                elif _return == "vaginal_inside_happy":
                    "I need to make sure I don't let go inside of Sam."
                    "It's a pain, but we didn't bother to use a condom."
                    "So I make sure to do it before the inevitable happens."
                    show samantha flat doggy ahegao
                    samantha.say "NO!"
                    samantha.say "Don't pull out!"
                    samantha.say "I want you to cum in me!"
                    "I'm so shocked by what Sam just said that I freeze in place."
                    "And in that short space of time, nature takes it's course."
                    with hpunch
                    "Sam and I cum almost at the same moment, each affecting the other."
                    show samantha flat doggy cum with hpunch
                    "I feel her squeezing me tightly as I let go inside of her."
                    if FACIAL and randint(0, 1):
                        "She smears a fresh stripe from her cheek down to her lips and sucks it from her fingers."
                    with hpunch
                    $ samantha.impregnate()
                    mike.say "Oh shit..."
                    mike.say "What have we done?!?"
                    $ samantha.love += 5
            "Fuck her ass":
                "I try not to throw myself too hastily onto Sam."
                "For one thing I'm worried about hurting her."
                "And for another I don't want to break my own bed!"
                "But even so, I still end up clambering atop her within seconds."
                "Much to her evident amusement and delight."
                samantha.say "Oh oh!"
                samantha.say "Someone's keen tonight!"
                mike.say "With an ass like that..."
                mike.say "Can you blame me?!?"
                samantha.say "Well..."
                samantha.say "If you like it so much..."
                samantha.say "Why don't you fuck it?"
                "Sam giggles and gives me a shake of her ass as a reward."
                "But she's not laughing for long, as I'm more than ready to go."
                "Instead, Sam begins to moan and gasp as I push between her legs."
                "She still has her ass raised in the air, so there's easy access."
                "And I can feel from the first moment of contact that she's ready for me."
                "But when I push my cock against her hole, there's natural resistance."
                samantha.say "Oh no you don't!"
                "Now it's my turn to gasp in surprise."
                "Because Sam grabs hold of the shaft without warning."
                "And then she pushes it hard against her hole."
                if samantha.piercings.clit.worn and randint(0, 1):
                    "Her fingers brush the cool piercing between her folds as she guides me; she shivers and presses back."
                "This is at the same time as I'm pushing to get in there as well."
                "So it doesn't take long for the inevitable to happen."
                show samantha flat doggy pleasure
                samantha.say "Ah..."
                samantha.say "Oh yeah..."
                samantha.say "Just...like...that!"
                mike.say "Oh shit!"
                "Samantha opens for me like a flower."
                "My cock doesn't go all the way in, not at first."
                show samantha flat doggy anal
                "Instead it sinks into her, inch by inch."
                "And every moment that it's happening is better than the last."
                if samantha.is_sex_slave and randint(0, 1):
                    samantha.say "Your slave's hole... take it."
                elif samantha.sub >= 70 and randint(0, 1):
                    samantha.say "Deeper. Use my ass."
                elif samantha.sub < 30 and randint(0, 1):
                    samantha.say "Fill me… but go steady."
                samantha.say "Mmm..."
                samantha.say "Don't...don't hold back..."
                show samantha flat doggy normal
                samantha.say "I...I want it...hard!"
                "I'm nodding eagerly as Sam says all of this."
                "And I can already feel my body obeying her commands."
                "I don't honestly know if I could make myself hold back."
                "But that's not a on my mind as I want the exact same thing."
                "Almost desperate to please Sam, I begin to move ever faster."
                "From a standing start, I'm soon thrusting into her at speed."
                "And it feels almost as good as sinking in there slowly too!"
                "For her part, Sam seems to know exactly what she wants."
                "As she happily takes everything that I have to give."
                show samantha flat doggy pleasure
                "In fact, from the way she's nodding her head, I think she actually wants more!"
                "Sam grabs handfuls of the bedclothes, like she's hanging on for dear life."
                "And I can feel her legs thumping the mattress behind me too."
                "Now I'm worried about her breaking the bed, rather than me!"
                "But that's not going to stop me from fucking her as hard as I can."
                show samantha flat doggy ahegao
                "By now Sam seems to be groaning and gasping with every thrust I make."
                "And when I catch a glimpse of her eyes, they're starting to glaze over."
                "I can feel her ass starting to quiver around me too."
                "So my guess is that she's about to cum!"
                "And I know that I can time my orgasm to hit when hers does."
                "If I can just push a little harder..."
                call cum_reaction (samantha, 'anal', sexperience_min) from _call_cum_reaction_264
                if _return == 'anal_inside':
                    show samantha flat doggy pleasure
                    "I don't need to worry about letting go inside of Sam."
                    "And that's one of the perks of doing her up the ass."
                    "So all I have to do is let nature take it's course."
                    show samantha flat doggy cum ahegao with hpunch
                    "Sam and I cum almost at the same moment, each affecting the other."
                    with hpunch
                    "I feel her squeezing me tightly as I let go inside of her."
                    if randint(0, 1):
                        "When it leaks, she catches it on her fingers and sucks them clean without looking back."
                    with hpunch
                    "Luckily we're both laid down on the bed."
                    "So we can easily collapse into a heap afterwards."
                    $ samantha.love += 2
                    $ samantha.sub += 1
                elif _return == 'anal_outside':
                    show samantha flat doggy pleasure
                    "I don't know why, but I get the urge to pull out."
                    "So I make sure to do it before the inevitable happens."
                    show samantha flat doggy ahegao with hpunch
                    "Sam and I cum almost at the same moment, each affecting the other."
                    show samantha flat doggy out with hpunch
                    "I feel her squeezing me tightly as I pull out of her."
                    show samantha flat doggy ahegao cumshot with hpunch
                    "And she's in the grips of her orgasm as I shoot my load over her buttocks."
                    if FACIAL and randint(0, 1):
                        "She smears a line from her cheek to her lips and gurgles it down, eyes half-lidded."
                    "Luckily we're both laid down on the bed."
                    "So we can easily collapse into a heap afterwards."
                    $ samantha.sub += 2
                    $ samantha.love += 1
                $ samantha.flags.anal += 1
    return

label samantha_date_fuck_beads_out:
    $ game.play_music("music/roa_music/city_nights.ogg")
    "It's time to take the beads out, I think, so I grab hold and prepare for extraction."
    if samantha.flags.engaged and randint(0, 1):
        "Her wedding ring flashes as she clutches the sheet, the band biting into the fabric."
    elif samantha.is_visibly_pregnant and randint(0, 1):
        "I keep one palm under her belly so the angle stays gentle while I work."

    menu:
        "Rough":
            "With a tug, I yank the beads back."
            "Multiple little balls plop out in quick succession."
            "Samantha screams as she feels her body expel the little spheres and then she falls to the bed, her hands gripping the sheets."
            if samantha.is_sex_slave and randint(0, 1):
                samantha.say "Your slave empties for you…"
            elif samantha.sub >= 70 and randint(0, 1):
                samantha.say "Yes... take it from me. All of it."
            elif samantha.sub >= 30 and randint(0, 1):
                samantha.say "God—okay—breathe—do that again… slower next time."
            if randint(0, 1) and samantha.sub >= 50:
                "She catches the last slick bead against her tongue, sucks it clean, and grins up at me."
            samantha.say "O... oh fuck! [hero.name] so rough!"
            $ samantha.sub += 1
        "Gentle":
            "One at a time, I pull the beads out."
            "Just like when it took them in, Samantha's exit spreads, letting the shining bead spit out of it."
            if samantha.piercings.nipples.worn and randint(0, 1):
                "Her nipples piercings stand taut when she exhales, a soft gasp trapped behind her teeth."
            "I pull gently once the first one exits, but each successive one comes out easier and easier, until finally, I pull out the final one, placing the beads aside and getting a nice look at Samantha's open hole."
            if randint(0, 1) and samantha.sub >= 50:
                "She brings the last bead to her mouth, kisses it, and laps the shine away before letting it fall to the sheet."
            elif samantha.flags.engaged and randint(0, 1):
                "Her wedding ring gleams when she strokes her lips, cheeks flushed."
            samantha.say "Ah... [hero.name] that was so nice..."
            $ samantha.love += 1
    $ BEADS = ""
    return

label samantha_date_fuck_dildo:
    $ game.play_music("music/roa_music/city_nights.ogg")
    mike.say "Spread your legs."
    "She does as I command."
    if samantha.is_sex_slave and randint(0, 1):
        samantha.say "Your slave opens for your toy."
    elif samantha.sub >= 70 and randint(0, 1):
        samantha.say "Yes, Sir."
    elif samantha.sub >= 30 and randint(0, 1):
        samantha.say "Show me… but be nice."
    mike.say "Let me see how much you want me."
    "She understands me, her fingers pressing against her moistened lips, spreading them apart and giving me a view of her wanting womanhood."
    if samantha.piercings.clit.worn and randint(0, 1):
        "A tiny glint flashes when she parts herself; her belly flutters."
    elif samantha.piercings.navel.worn and randint(0, 1):
        "Her navel jewel sparkles when she tilts her hips to frame the view."
    mike.say "Amazing."
    samantha.say "[hero.name], This is just for you, as long as you want it."
    mike.say "Oh, I want it, alright."
    if randint(0, 1):
        "She leans up and licks the tip, lubing it with a hungry little hum."
        if samantha.piercings.tongue.worn and randint(0, 1):
            "Her tongue stud taps the toy—ting—before she sits back open and ready."
    else:
        "I say, pouring a little bit of lube over the massive plastic dong."
    mike.say "But I'm not going to take it, not yet."
    "She shudders at that, feeling the ominous air around her over the vibrator."
    "I soon take it, pressing the tip into her wanting warmth."
    "It eagerly swallows it up, her walls stretching to accommodate its amazing size."
    "With a cry, she reaches down, wrapping her hands around it."
    samantha.say "Aah, [hero.name]!"
    "Go ahead, put it in... keep it in, but first..."
    "I flip the switch, and the buzzing fills the air of my room."
    "Immediately, Samantha squirms around under the shock of the intense stimulation."
    if samantha.is_visibly_pregnant and randint(0, 1):
        "I keep my palm under her belly while she rides the pulse, breath catching."
    elif samantha.flags.engaged and randint(0, 1):
        "Her wedding ring flashes as her fingers clutch the sheets."
    mike.say "And you're going to keep it inside you until I tell you to pull it out. Got it."
    samantha.say "Y... yes, [hero.name]!"
    $ samantha.sub += 1
    $ DILDO = " dildo "
    return

label samantha_date_fuck_dildo_out:
    $ game.play_music("music/roa_music/city_nights.ogg")
    if samantha.flags.nickname == "cupcake":
        mike.say "Cupcake, it's time to pull it out."
    else:
        mike.say "Samantha, it's time to pull it out."
    samantha.say "Ah.. Ah, thank you. I don't... mmm, I don't think I could have lasted much longer."
    "Samantha reaches down with one hand, gripping onto the soaked, humming plastic."
    if samantha.flags.engaged and randint(0, 1):
        "Her wedding ring bites the base as she twists the toy free."
    if randint(0, 1):
        "With a final loud gasp, she pulls it free."
        "She lowers her mouth to the dripping tip, sucks it clean, and swallows loudly, eyes never leaving mine."
        if samantha.piercings.tongue.worn and randint(0, 1):
            "The stud traces a slow circle before she lets the toy fall away."
    else:
        "With a final loud gasp, she pulls it free, letting it roll and clatter to the floor, a sloppy mess."
    "This leaves Samantha there, panting heavily, her tongue out, looking like a horny animal."
    samantha.say "Ah... ah.... J... just for.... For you...!"
    $ DILDO = ""
    return

label samantha_sleep_date_fuck(location="hero"):
    if game.hour > 19 or game.hour < 6:
        scene bg bedroom1
        if not samantha.get_counters('pregnant') > 6 or samantha.flags.tellpregnant:
            show samantha naked
            if samantha.is_visibly_pregnant and randint(0, 1):
                "She rubs the curve of her belly, then tugs me close to feel the warmth together."
            elif FACIAL and randint(0, 1):
                "A soft sheen still glazes her cheek; she kisses my chin and giggles."
            elif samantha.flags.engaged and randint(0, 1):
                "Her wedding ring shimmers when she hooks a finger in my waistband."
            samantha.say "Mm.. want me to spend the night?"
            menu:
                "No":
                    $ r = False
                    mike.say "No, you shouldn't; I have to get up early tomorrow."
                    "The sex was beyond incredible."
                    "Frowning a little, Samantha straightens and shrugs, then goes to collect her robe from where she'd let it fall earlier."
                    samantha.say "Alright. Sleep well."
                    "She then heads up the stairs."
                    $ samantha.love -= 3
                    call sleep from _call_sleep_39
                "Yes":
                    $ r = True
                    mike.say "Absolutely."
                    "I say, my voice a little shaky."
                    "I pull out with a reluctant sigh, then turn toward the bed."
                    "We curl up spooning together in bed, drifting toward sleep."
                    if samantha.is_sex_slave and randint(0, 1):
                        samantha.say "Your slave stays warm for you."
                    elif samantha.sub >= 70 and randint(0, 1):
                        samantha.say "Hold me down if I move... I sleep better when you restrain me."
                    elif samantha.sub < 30 and randint(0, 1):
                        samantha.say "Stay right here… I like feeling you on my back."
                    show cuddle samantha with fade
                    samantha.say "Sweet dreams."
                    mike.say "You too."
                    $ samantha.love += 3
                    call sleep ("samantha") from _call_sleep_40
            $ game.room = "bedroom1"
        else:
            call sleep ("samantha") from _call_sleep_41
            $ game.room = "bedroom1"
            "When I come to, my head feels heavy."
            "The soft sheets underneath me slowly bring my sleep addled mind forward."
            "I open my eyes, blinking rapidly and see the ceiling of my room."
            "When did I fall asleep?"
            show cuddle samantha with fade
            "A body shifts next to me- Samantha."
            "She ended up curled into my side, gripping my arm."
            "She must have fallen asleep too."
            "Seems like she's waking up."
            samantha.say "[hero.name]?"
            mike.say "Hmm...?"
            "All I can do it grunt in response while trying to rev up the motor to my mouth."
            "She shakes me."
            samantha.say "[hero.name]?"
            mike.say "Yeah? What?"
            "I rub a hand across my eyes, then the rest of my face, forcing myself to wake up."
            if FACIAL and randint(0, 1):
                "Some dried cum still marks her cheek; she notices my stare and smirks."
            samantha.say "I have to go to work in a few minutes."
            "The bed shifts and she slips off the side, raising her arms above her head in a stretch."
            scene bg bedroom1
            show samantha naked
            with fade
            if samantha.flags.engaged and randint(0, 1):
                "Her wedding ring flashes when she tucks a strand of hair behind her ear."
            samantha.say "Thanks for letting me stay over."
            "I sit up."
            mike.say "Yeah, no problem."
            show samantha
            "Sam shoves on her shirt and starts to look for her bag."
            if samantha.piercings.navel.worn and randint(0, 1):
                "Her navel jewel peeks above the waistband before the fabric falls."
            mike.say "It's by the door."
            samantha.say "Oh! Thanks!"
            "She picks it up and slings it over her shoulder. I guess it's time to start the day. Unfortunately. I move to get to the bathroom, wanting to get in before Sasha."
            samantha.say "Hey... [hero.name]?"
            "I look over at Sam who's hesitating by the door. She's having trouble looking me in the eye."
            mike.say "What's up?"
            samantha.say "How do you feel about... kids?"
            menu:
                "They're okay":
                    "That's a weird question. But..."
                    mike.say "They're alright. It's not like I know any?"
                    samantha.say "Oh..."
                    show samantha happy
                    "She suddenly smiles, looking much more confident."
                    samantha.say "That's not what I meant but... I'm glad to hear that."
                    "With that, she opens the door and leaves."
                    mike.say "... Okay?"
                    $ samantha.flags.tellpregnant = 1
                    $ samantha.love += 1
                "I love them":
                    "That's a weird question. But..."
                    mike.say "I love kids."
                    samantha.say "Great!"
                    show samantha happy
                    "She suddenly smiles, looking much more confident."
                    samantha.say "I'm glad to hear that."
                    "With that, she opens the door and leaves."
                    mike.say "... Okay?"
                    $ samantha.flags.tellpregnant = 1
                    $ samantha.love += 5
                "I can't stand kids.":
                    $ samantha.love -= 10
                    mike.say "Kids are... not my thing. I can't really stand them."
                    "Samantha's lips purse. Otherwise I can't read her expression, but her tone gives it away."
                    show samantha angry
                    samantha.say "Oh... okay then."
                    "She makes a move to leave, but I stop her."
                    mike.say "Wait! What's wrong?"
                    "She lets her bag drop back to the ground and crosses her arms. This can't be good."
                    samantha.say "You know I want kids... someday... right?"
                    "Oh yeah. I think she mentioned that at some point. Maybe when she was still with Ryan? And she's always wanted to be a children's book author too."
                    mike.say "We can... figure something else out."
                    samantha.say "What?!"
                    "I wince when she raises her voice. Her eyes look sad and her eyebrows are angry."
                    samantha.say "Are you serious?! What does that even mean?"
                    mike.say "What?"
                    samantha.say "'Figuring something else out'. What is that supposed to mean?"
                    "She makes air quotes with her fingers as she repeats what I said."
                    mike.say "Well... ya know. We could always get a dog. Or a cat?"
                    "This just seems to upset her more."
                    samantha.say "A dog is not the same thing as a baby!"
                    mike.say "You're right. A dog is a lot quieter."
                    "Her mouth falls open, as if she's offended."
                    samantha.say "I can't believe you right now!"
                    if samantha.flags.nickname == "cupcake":
                        mike.say "I'm sorry, Cupcake. I just don't want kids. Is that so bad?"
                    else:
                        mike.say "I'm sorry, Sam. I just don't want kids. Is that so bad?"
                    samantha.say "I'm pregnant!"
                    "Her shout cuts through the tense room air. What?"
                    mike.say "You're what?"
                    "Samantha angrily picks up her bag and forcefully opens it. She digs around for a moment before pulling something out and throwing it at me. It hits me in the chest."
                    samantha.say "I think I need some space."
                    "Samantha mutters before leaving. I don't stop her this time."
                    "Numbly, my fingers reach for the white stick she threw at me. I instantly know what it is."
                    "I quickly turn over the pregnancy test and my heart falls through my chest."
                    "Two stripes."
                    $ samantha.flags.tellpregnant = 2
    return

label samantha_fuck_bathroom:
    $ game.play_music("music/roa_music/city_nights.ogg")
    scene bg bathroom
    show samantha underwear
    with fade
    "Sam has a tight hold of my hand as she leads me into the bathroom."
    "She also has a mischievous smile on her face that I just can't ignore."
    if samantha.flags.engaged and randint(0, 1):
        "Her wedding ring flashes when she pulls me over the tiles, a tiny comet of light in the steam."
    "Both mean that I can't help but follow wherever she wants to lead me."
    "And yet I still feel more than a little nervous about what she has in mind."
    if samantha.flags.nickname == "cupcake":
        mike.say "Ah, Cupcake..."
    else:
        mike.say "Ah, Sam..."
    mike.say "Are you sure this is a good idea?"
    "Sam shakes her head, as if the question isn't even worth answering."
    mike.say "I mean...we might get caught!"
    "Sam's already slammed the door behind us by now."
    "She lets go of my hand so that she can hurry over and turn on the shower."
    play sound shower loop
    samantha.say "Of course we could, [hero.name]."
    samantha.say "That's what makes it so exciting!"
    if samantha.is_sex_slave and randint(0, 1):
        samantha.say "Your slave will take you... Here, now."
    elif samantha.sub >= 70 and randint(0, 1):
        samantha.say "Tell me what to do."
    elif samantha.sub >= 30 and randint(0, 1):
        samantha.say "Then make it quick... and make it good."
    "I make to say something more, opening my mouth to speak."
    "But the words don't come to me and I stand there in stunned silence."
    show samantha naked with dissolve
    if samantha.piercings.nipples.worn and randint(0, 1):
        "Water pearls on her nipple piercings before streaking down her curves."
    elif samantha.piercings.navel.worn and randint(0, 1):
        "Her navel jewel gleams once and disappears beneath the running water."
    "Sam's already all but naked before me, making no effort to cover herself."
    "And with that one move, she's defeated any arguments I might have had!"
    "She steps backwards into the shower."
    "The water soaks her hair and then runs down over her body."
    "Sam beckons for me to join her."
    mike.say "Well..."
    mike.say "When you put it like that..."
    "I hardly remember stripping off my own clothes."
    "And getting into the shower is likewise a blur."
    "The next thing I know, I have Sam in my arms."
    "Water cascades down over us as she clings to me."
    "She feels slippery and slick as I try to keep a hold of her."
    "And I can feel a genuine hunger in the way that she's kissing me."
    if samantha.piercings.tongue.worn and randint(0, 1):
        "Her tongue stud clicks softly against her teeth; she moans into my mouth."
    "The moment that my tongue is in her mouth, she almost shudders."
    "It's then I know that she wants me inside of her that badly!"
    "Sam twists in my grasp, breaking off the kiss."
    scene samantha showersex
    show samantha showersex outside
    with fade
    "She turns her back to me then, pushing her ass against me."
    "I don't need to be told what she wants me to do next."
    if samantha.is_visibly_pregnant and randint(0, 1):
        "I slide one hand beneath the soft swell of her belly to steady her as she sets her feet."
    "Needless to say, I'm already hard."
    "And I want the exact same thing..."
    menu:
        "Fuck her ass":
            "Sam's grinding her ass into my groin by now."
            "And so it's almost too easy to take advantage."
            "All I need to do is point my cock just so..."
            samantha.say "Ah..."
            samantha.say "Oh, [hero.name]!"
            samantha.say "Look who's full of surprises..."
            "Sam looks back over her shoulder as she giggles at me."
            "But that only lasts for a couple of seconds."
            show samantha showersex anal -outside
            "As the head of my cock pushes into her ass, she gasps."
            if samantha.flags.engaged and randint(0, 1):
                "Her wedding ring scrapes the rail when she grips it, flashing with every breath."
            "And then I see the way her eyes begin to glaze over."
            "She can't help but surrender to the sensations that she's feeling."
            "I watch with fascination as I push deeper still."
            "It's almost like every inch I get inside has a visible effect."
            "Like it makes Sam less able to focus, less able to form words."
            "Like fucking her ass is slowly reducing her to the state of an animal."
            show samantha showersex pleasure
            "Sam clings to the shower fittings as I make it all the way inside of her."
            "Her head hangs down and her back is almost horizontal."
            "It's clear that she wants as much of me in her as possible."
            if samantha.is_sex_slave and randint(0, 1):
                samantha.say "Your slave's hole is yours."
            elif samantha.sub >= 70 and randint(0, 1):
                samantha.say "Deeper. Use me."
            elif samantha.sub < 30 and randint(0, 1):
                samantha.say "Keep it steady… then harder."
            "And it's now that I begin to fuck her for real."
            "The muscles of Sam's ass quiver and protest as I do so."
            "But neither of us seems inclined to listen to their protests."
            "Instead I thrust in and out with all the speed I can muster."
            "And Sam urges me on with the almost feral moans she lets out."
            samantha.say "Aaah..."
            samantha.say "Mmm..."
            samantha.say "Yeah...fuck me..."
            samantha.say "Fuck me...hard..."
            "Every word that Sam manages to spit out makes me work that much harder."
            "Part of me can't believe that this is the girl I call my cupcake."
            "That she's begging me to pound her ass harder and harder!"
            "I'm so lost in the effort to do so that I lose track of myself."
            "And before I know it, I'm about to cum!"
            menu:
                "Cum inside":
                    "All of my effort is going into pushing forwards, not holding back."
                    "And so there's nothing I can do to keep it from happening."
                    show samantha showersex anal creampie with hpunch
                    "I lose it when I'm as deep inside of Sam as I can possibly go."
                    show samantha showersex ahegao with hpunch
                    "I feel her shudder as she takes it, groaning and tossing her head."
                    with hpunch
                    "The muscles of her ass keep on squeezing my cock the whole time."
                    if randint(0, 1):
                        "When it leaks, she catches a milky thread on her fingers and licks them clean, sighing like it's dessert."
                    "And afterwards, all I can hear is the sound of us both gasping with exhaustion."
                    "That and the water still raining down on us from above."
                    $ samantha.love += 1
                "Pull out":
                    "Sam begins to protest almost as soon as I start to pull out."
                    show samantha showersex outside -anal
                    "But I keep on going all the same, my cock sliding free just in time."
                    show samantha showersex ahegao with hpunch
                    "She moans and shudders as her muscles quiver from the release."
                    show samantha showersex outside creampie with hpunch
                    "And then I shoot my load over her buttocks and onto her back."
                    if randint(0, 1):
                        "She turns her head, cups the runoff with one hand, and drinks from her palm, eyes fluttering shut."
                    with hpunch
                    "Sam stares back at me over her shoulder, eyes wide and intense."
                    "I swear I can see the animal in them fading as she comes back to reality."
                    "But the power of speech still seems to be lost to her."
                    $ samantha.sub += 1
            $ samantha.flags.anal += 1
        "Fuck her pussy":
            "Sam's nice and wet down there, of course because of the water."
            "But I'd like to think that she's also more than a little slick thanks to my efforts too!"
            "All of that means it's easy as hell to get inside of her pussy."
            if samantha.piercings.clit.worn and randint(0, 1):
                "The crown brushes a cool piercing as I line up; she jolts and breathes my name."
            "The moment that she feels the head of my cock against her lips, Sam quivers all over."
            samantha.say "Mmm..."
            samantha.say "Oh, [hero.name]..."
            samantha.say "That's what I want!"
            samantha.say "I want you inside of me..."
            if samantha.is_visibly_pregnant and randint(0, 1):
                "I steady her hips and belly so the rhythm stays smooth in the spray."
            "It's not like I needed the encouragement to keep on going."
            "But just knowing that Sam want this so badly..."
            "That makes it all the more exciting as I begin to push into her."
            show samantha showersex vaginal -outside
            "There's only a few seconds of resistance before she gives way."
            "Which tells me that she was being honest about her wanting it."
            "Sam moans, deep and long as I sink my cock as deep into her as it'll go."
            "I only stop when I can't go any further, holding it inside of her."
            "She wriggles as quivers, clearly enjoying the sensation."
            if samantha.is_sex_slave and randint(0, 1):
                samantha.say "Let your slave milk you."
            elif samantha.sub >= 70 and randint(0, 1):
                samantha.say "Harder. Make me take all of it."
            elif samantha.sub >= 30 and randint(0, 1):
                samantha.say "Slow first… then ruin me."
            "And her delight only seems to mount as I begin to move a second later."
            "I start out slowly, only beginning to build speed a little at a time."
            "Sam doesn't complain, but rather matches me every step of the way."
            "Every time I kick the speed up a notch, she keeps pace."
            "Sam's ass bounces up and down as I pound away."
            "The sight is hypnotic, drawing my eye and holding it."
            "Pretty soon her buttocks are slapping against my thighs over and again."
            show samantha showersex pleasure
            "The sound is louder than the cries Sam's letting out."
            "Part of me wonders if anyone can hear her over the sound of the shower."
            "But even if they can, there's no way I'm stopping now!"
            "I don't think anything could tear me away from Sam."
            "Not before I finish what I started!"
            samantha.say "Do it, [hero.name]..."
            samantha.say "Make me cum..."
            samantha.say "Please!"
            "It's almost as if she's the one in control of my body right now."
            "I can already feel myself obeying Sam's command!"
            menu:
                "Cum inside":
                    "If Sam wants everything I have to give, then that's what she'll get."
                    show samantha showersex vaginal creampie with hpunch
                    "I hold nothing back as I shoot my load into her."
                    with hpunch
                    "I lose it when I'm as deep inside of Sam as I can possibly go."
                    show samantha showersex ahegao with hpunch
                    "She moans like an animal, tossing her head this way and that."
                    if randint(0, 1):
                        "She slips two fingers down to catch what spills and licks them clean, eyes hazy with satisfaction."
                    "I can feel the sensation of her cumming in the moments that follow."
                    "And then it's all over, and we're both gasping with exhaustion."
                    "Gasping as the water rains down on us from above."
                    $ samantha.love += 1
                "Pull out":
                    show samantha showersex outside -vaginal
                    "Sam moans in disappointment as I pull my cock out of her."
                    "But I can already feel the effect that it's having on her."
                    show samantha showersex ahegao with hpunch
                    "She quivers and moans as the release triggers her own orgasm."
                    show samantha showersex outside creampie with hpunch
                    "And then I shoot my load over her buttocks and onto her back."
                    if randint(0, 1):
                        "A hot stripe arcs around her hip onto her belly; she rubs it into the skin and sucks it from her fingers like it's a secret treat."
                        if samantha.is_visibly_pregnant and randint(0, 1):
                            "Watching it warm the curve of her belly makes my chest ache in a way I can't name."
                    with hpunch
                    "Sam gasps the whole time, still shuddering from her climax."
                    "And then it's all over, and we're both gasping with exhaustion."
                    "Gasping as the water rains down on us from above."
                    $ samantha.sub += 1
    stop sound fadeout 1.0
    $ samantha.flags.showersex = True
    $ samantha.sexperience += 1
    return

label samantha_fuck_date_nudistbeach:
label samantha_fuck_beach:
label samantha_fuck_date_beach:
    $ game.play_music("music/roa_music/city_nights.ogg")
    if game.week_day % 2 == 0:
        show samantha
        "Sometimes it's hard for me to actually believe that Sam and I are now an item, you know?"
        "I feel like I have to pinch myself to check that it's really happening, that I'm not dreaming."
        "As crazy as it sounds, that's just how much being with her means to me."
        "Take today as an example - all that we're doing is spending the day at the beach."
        "Nothing out of the ordinary or crazily romantic, you might think."
        show samantha happy at center, zoomAt(1.5, (640, 1100)) with fade
        if samantha.flags.engaged and randint(0, 1):
            "When she squeezes my hand, her wedding ring throws a tiny star across the sand."
        "But I can't stop staring at Sam, beaming with happiness at the thought that she's all mine."
        if samantha.is_visibly_pregnant and randint(0, 1):
            "She strokes the curve of her belly when the breeze lifts, smiling like the sun is only for us."
        elif samantha.piercings.navel.worn and randint(0, 1):
            "Her navel jewel glimmers each time the light dances on the waves."
        "And she seems to feel the same way too, holding my hand and returning my smiles the whole time."
        show samantha normal
        "The day passes far too quickly for my liking."
        "And the sun is beginning to sink towards the horizon."
        "My disappointment that this will all be over soon must show on my face."
        show fx question
        "As Sam cocks her head on one side as she looks at me."
        samantha.say "What's the matter, [hero.name]?"
        samantha.say "You've been so happy all day."
        samantha.say "What's happened to change your mood?"
        hide fx
        "I make a deliberate effort to perk myself up, smiling and shaking my head."
        if samantha.flags.nickname == "cupcake":
            mike.say "Oh, it's nothing really, Cupcake."
        else:
            mike.say "Oh, it's nothing really, Sam."
        mike.say "I've just had such a good time with you today."
        mike.say "I'm not ready for it to end, that's all."
        show samantha happy
        "Sam smiles at this, showing me that she's flattered by the sentiment."
        "But then she surprises me by getting to her feet and holding out her hands to me."
        samantha.say "Come on, [hero.name]."
        samantha.say "The day's not done with yet."
        samantha.say "What do you say we take a romantic sunset stroll?"
        if samantha.is_sex_slave and randint(0, 1):
            samantha.say "Your slave follows."
        elif samantha.sub >= 70 and randint(0, 1):
            samantha.say "Lead me. I'll go wherever you decide."
        "I nod eagerly as I hurry to get up and accept the invitation."
        show samantha normal
        "The beach has been pretty crowded all day."
        "And the chance to spend some time alone with Sam is more than enough to get me off of my ass!"
        "She clasps my hand in her own and leads me towards the point where the waves lap against the beach."
        "We talk as we walk, chatting about everything and nothing."
        "And I begin to feel like, as long as I'm with Sam, I don't have a care in the world."
        "That's why it surprises me when she finally stops and looks out to sea."
        "I realise that we've walked far further than I thought."
        "We're amongst the rocks on a remote part of the beach."
        "There's only the sound of the crashing waves, as we're also totally alone."
        samantha.say "You know what, [hero.name]."
        samantha.say "I just thought of the perfect way to end the perfect day."
        "Sam lets go of my hand and lowers herself down, onto the sand."
        hide samantha
        show beach cream samantha nomc
        with fade
        if samantha.is_visibly_pregnant and randint(0, 1):
            "She lies carefully, one hand caressing her belly as the evening air cools."
        "Her belly is almost flat to the ground."
        "But her makes sure to raise her exquisite ass in a provocative manner too."
        "Sam looks back over her shoulder at me, a wicked gleam in her eyes."
        samantha.say "I always wanted to do it as the sun goes down."
        samantha.say "So how about it?"
        samantha.say "You want to fuck me where the sun doesn't shine?"
        if not game.room == "date_nudistbeach":
            show beach cream samantha naked
            "As if there's any need to underline the point, Sam pulls her swimsuit away."
            if samantha.piercings.clit.worn and randint(0, 1):
                "A tiny cool piercing flashes as she parts herself for me."
            "This reveals her sweet, tight ass like an irresistible seashell upon the sand."
        "I nod, hastily pulling down my trunks as I check that there's no one around."
        "Sam sees my cock bobbing up and down as I do this and lets out a cute little laugh."
        if samantha.piercings.tongue.worn and randint(0, 1):
            "She leans, taps the tip with her stud, and then settles down again with a naughty smile."
        "Which, of course, only makes me want her all the more desperately!"
        hide beach cream samantha
        show samantha flat doggy
        with fade
        "Now freed of my trunks, I lower myself down atop Sam."
        "She obliges by wriggling her buttocks against me as I adjust my weight."
        "And the sensation of my cock slipping between them is almost too much to bear."
        if samantha.flags.engaged and randint(0, 1):
            "Her wedding ring scratches lightly through the sand when she plants her hand for leverage."
        samantha.say "Mmm..."
        samantha.say "I'm ready for you, [hero.name]."
        if samantha.is_sex_slave and randint(0, 1):
            samantha.say "Use your slave's body."
        elif samantha.sub >= 70 and randint(0, 1):
            samantha.say "Push... Make me take it."
        elif samantha.sub < 30 and randint(0, 1):
            samantha.say "Go slow… then don't stop."
        samantha.say "Stick it inside me already!"
        "I do as I'm told, soon finding that Sam wasn't lying."
        "The muscles of her ass are tight and feel incredible."
        show samantha flat doggy anal
        "But she doesn't make it hard for me to push myself into her either."
        "This means that I feel a combination of token resistance at first."
        "And then her ass seems to melt into submission, letting me sink right in up to my balls."
        "Sam looks back over her shoulder at me again."
        "Though this time I can see that her huge, expressive eyes are full of desire."
        "Her cheeks are flushed too, letting me know that she can feel me right to the core of her being."
        "I begin to move inside of her, feeling her body start to move in sympathy."
        "The sight of Sam in motion as she rides my cock is something else."
        show samantha flat doggy pleasure
        "The swaying of her breasts, the rise and fall of her ass."
        if samantha.piercings.nipples.worn and randint(0, 1):
            "Her nipple piercings tug and bounce with every shove, making her gasp."
        "It's almost as much of a turn-on as the feeling of actually being buried deep inside of her ass!"
        "I'm gasping and sweating now, throwing all that I have behind each thrust."
        "And Sam's taking every ounce of what I have to give too."
        "Her knees are buried in the sand from how hard I'm pounding her."
        "And I can see her hands almost clawing at it in desperation, like she's digging a hole for herself."
        "The sun's almost set by now, and the tide is creeping ever closer."
        samantha.say "Ah..."
        samantha.say "Make me cum..."
        samantha.say "Before the tide comes in!"
        "It's not like Sam has to worry about that."
        "Even as she says the words, I can feel myself starting to cum!"
        menu:
            "Cum inside":
                "I make one final push into Sam's ass, thrusting in as deep as I can go."
                show samantha flat doggy ahegao with hpunch
                "A second later I shoot everything that I have into her, holding nothing back."
                show samantha flat doggy cum with hpunch
                if randint(0, 1):
                    "She presses a finger to her hole as I slip free, scoops what leaks, and licks it from her knuckle with a greedy little hum."
                "I fill her completely, cum already seeping out of her and running down her thighs."
                with hpunch
                "She moans, digging deeper into the sand than ever before."
                "And I know from the way that she's shuddering around my cock that she's cumming too."
            "Cum on her back":
                "I yank my cock out of Sam's ass the moment before I actually lose it."
                "It comes out of her with an audible pop, and she moans in surprise at the same moment."
                show samantha flat doggy ahegao out with hpunch
                "And then I shoot my load over her back and buttocks, spattering her with cum."
                show samantha flat doggy cumshot with hpunch
                if randint(0, 1):
                    "A stripe curls around her hip and kisses her lower belly; she rubs it into her skin with two fingers and sucks them clean."
                    if samantha.is_visibly_pregnant and randint(0, 1):
                        "Watching it warm the soft curve of her belly stirs something fierce and tender in my chest."
                "She moans, digging deeper into the sand than ever before."
                with hpunch
                "And I know from the way she's shuddering that she's cumming too."
        hide samantha flat doggy
        show samantha naked flirt blush at center, zoomAt(1.5, (640, 1100))
        with fade
        "By now the tide is lapping around our ankles as we sit on the sand."
        if samantha.piercings.navel.worn and randint(0, 1):
            "Her navel jewel glitters through a last tiny rivulet before the water claims it."
        "And so we use it to clean ourselves up before starting out back the way we came."
        show samantha happy
        "Sam holds my hand tightly, leaning happily against my shoulder the whole way."
        if samantha.flags.engaged and randint(0, 1):
            "Her wedding ring is cool against my palm; she squeezes, and I squeeze back."
        "And I don't know which is more beautiful to my eyes."
        "The glow of the sunset on the horizon."
        "Or that of satisfaction on her cheeks."
    else:
        show samantha
        "It's days like this when it's really hard to be a guy."
        "When you really want to come across as the cool, caring type."
        "But fate just seems to conspire to stop that from happening."
        "And worse, it also tries to make you look like a total perv too!"
        "Take today for example, the perfect sunny day to go to the beach."
        "And Sam's the perfect companion to make it that much better."
        "The only problem is that she has to go and be hotter than the damn sun!"
        "I know that it's not her fault, she didn't ask to be the cutest girl I know."
        "And it's not like she can help looking so damn good in that swimsuit either."
        if samantha.piercings.navel.worn and randint(0, 1):
            "The tiny jewel at her navel catches the light and shoots it straight through me."
        "But seriously, it's like she doesn't even know what she's doing to me!"
        "I try as best I can to play down how Sam's making me feel."
        "Instead I concentrate all of my energies on finding us the perfect spot."
        "And once I find one that's hidden away and yet still in the sun, I claim it for us."
        show samantha happy at center, zoomAt(1.5, (640, 1100)) with fade
        "We throw towels down on the sand and settle on them."
        "Sam lies back, soaking up the sun without a care in the world."
        if samantha.is_visibly_pregnant and randint(0, 1):
            "She rests a hand on her belly and hums, eyes closed, peaceful as the tide."
        "And I lie next to her, trying to hide the fact she's making me hard as a rock!"
        "As time passes, I'm beginning to think that I can handle it."
        show samantha at center, zoomAt(1.5, (640, 1100)), top_to_bottom
        "I can keep stealing furtive glances at Sam as she lies there."
        "My eyes commit the curves of her body to memory as best they can."
        "And so when I'm forced to look away, they're still fresh in my mind."
        "But then I hear the sound of Sam stirring a little beside me."
        show samantha at center, zoomAt(1.5, (640, 1100)), bottom_to_top
        "Which makes me hold my breath, worried that I've been found out..."
        samantha.say "Mmm..."
        samantha.say "[hero.name]?"
        samantha.say "Are you awake?"
        "I've never been the best at faking it, so I admit the truth."
        mike.say "Uh..."
        if samantha.flags.nickname == "cupcake":
            mike.say "Yeah, Cupcake."
        else:
            mike.say "Yeah, Sam."
        mike.say "I'm awake."
        "Sam nods at this, still not opening her eyes."
        samantha.say "Good..."
        samantha.say "That means you can do me a favour."
        "Sam's been lying on her back this whole time."
        hide samantha
        if game.room == "date_nudistbeach":
            show beach cream samantha naked nomc
        else:
            show beach cream samantha nomc
        with fade
        "But now she rolls over until her belly's on the sand."
        if samantha.flags.engaged and randint(0, 1):
            "Her wedding ring leaves a tiny crescent in the sand when she props herself up."
        samantha.say "I have a kink somewhere in my back."
        samantha.say "Be a hero and see if you can work it out for me?"
        if samantha.flags.nickname == "cupcake":
            mike.say "S...sure thing, Cupcake."
        else:
            mike.say "S...sure thing, Sam."
        mike.say "Where exactly is it?"
        "Sam shakes her head as I lean over to begin my assigned task."
        "And she lets out a sigh that sounds almost as good as she looks."
        samantha.say "I don't know, [hero.name]."
        samantha.say "It's weird...keeps moving around."
        samantha.say "You'd best start by my shoulders and work your way down, okay?"
        if samantha.flags.nickname == "cupcake":
            mike.say "You got it, Cupcake!"
        else:
            mike.say "You got it, Sam!"
        show beach cream samantha -nomc
        "As my hands reach out towards Sam's shoulders, I try to keep focused."
        "I'm telling myself that this is just a back rub, nothing more than that."
        "I know that it can lead to all sorts of exciting stuff in other circumstances."
        "But this isn't one of them - it's JUST a back rub!"
        "Not that Sam seems to be interested in helping me stay on target."
        "Almost the same moment my hands touch her skin, Sam moans."
        "And I don't mean she just lets me know she approves."
        "I mean she lets out a sensual sound that's like torture to my ears!"
        samantha.say "Oh...mmm..."
        samantha.say "Yeah, [hero.name]..."
        samantha.say "That's really helping!"
        "Okay, I have to keep holding on here."
        "All Sam's doing is letting me know she likes it."
        "That's all she's doing."
        samantha.say "I think you should go lower."
        samantha.say "Maybe around the middle of my back?"
        "I do as I'm told, massaging with my hands the whole time."
        "Soon I reach the middle of Sam's back, like I've been told."
        if samantha.piercings.nipples.worn and randint(0, 1):
            "When she shifts, her barbells imprint two tiny dimples in the towel."
        samantha.say "You know what...that's not it!"
        samantha.say "Try going lower - try the small of my back."
        "Again I follow her instructions, heading downwards."
        "And so I find myself working at the knots just above Sam's ass."
        samantha.say "No, no, no..."
        samantha.say "Just a little lower!"
        if samantha.flags.nickname == "cupcake":
            mike.say "But, Cupcake..."
        else:
            mike.say "But, Sam..."
        mike.say "That's your ass!"
        "I hear Sam chuckle at this."
        "And she looks back over her shoulder at me."
        samantha.say "I know that, silly!"
        samantha.say "Your cock's been pressing into my leg this whole time."
        samantha.say "And it feels harder than your hands to me!"
        samantha.say "So why don't you use it instead?"
        if samantha.is_sex_slave and randint(0, 1):
            samantha.say "Your slave begs. Use her."
        elif samantha.sub >= 70 and randint(0, 1):
            samantha.say "Make me take you."
        mike.say "Wha...what?!?"
        mike.say "You want me to you know what?"
        mike.say "In your you know where?!?"
        samantha.say "Yeah, [hero.name], I do!"
        samantha.say "I've got an itch there and I want you to scratch it!"
        "As if she needed to make her point clear, Sam uses one hand to stroke my cock."
        if not game.room == "date_nudistbeach":
            show beach cream samantha naked
            "And at the same time, she uses the other to pull aside her swimsuit!"
            if samantha.piercings.clit.worn and randint(0, 1):
                "A cool little piercing winks at me when she parts herself."
        "I nod eagerly, any thought of keeping things clean vanishing from my mind."
        "It only takes me a moment to yank off my trunks."
        "And then I take advantage of the invitation Sam just made."
        hide beach cream samantha
        show samantha flat doggy naked
        with fade
        "I push my cock slowly between her buttocks, searching for my target."
        "When Sam gasps and begins to nod her head, I know that I've found it."
        "All it takes is one more firm push, and I'm inching into her ass."
        show samantha flat doggy anal
        "It's now that Sam seems to lose the power of speech."
        "Before she was the one giving instructions."
        "But now all she can do is moan as I sink my cock into her."
        "Every inch that her ass takes seems to make the sound more intense."
        "And I'm glad that I had the foresight to choose a spot like this."
        "The idea of getting caught might be a thrill to some people."
        "But it scares the living hell out of me!"
        "Sam's ass is tight, gripping me the whole time."
        show samantha flat doggy pleasure
        "This makes me go slowly, means that I take extra care."
        "And the upshot is that we both get to feel every second more intensely."
        "I might have been tempted to pound away at Sam's pussy."
        "But her ass slows me right down, enjoy every moment I'm inside of her."
        "My weight is pressing down on Sam too, pushing her into the sand."
        "She's leaning on her elbows, trying to stay upright."
        "This is because it means she can raise her ass into the air."
        "And then, in turn, I can push my cock deeper inside of her."
        "But I can already see her arms beginning to quake."
        "This means it comes as no surprise a moment later when they give out."
        "Sam collapses onto the sand, panting and helpless."
        "I don't even think of stopping."
        "I just keep right on going."
        "That's because I can see that she's nodding her head."
        "Letting me know that she wants me to finish this."
        "I can't read the expression on her face right now."
        show samantha flat doggy ahegao
        "And that's because Sam's eyes have rolled back into her head."
        "At the same time her tongue is lolling out of her open mouth."
        if samantha.piercings.tongue.worn and randint(0, 1):
            "Her stud glints when her tongue spills past her lips."
        "Every thrust that I make into Sam shoves her harder into the sand."
        "And I can see her breasts straining against her bikini top."
        "Any moment they could escape, rubbing Sam's nipples into the sand too!"
        "The thought is oddly exciting, and it spurs me on to push harder still."
        "With one last effort, I feel something burst inside of me."
        show samantha flat doggy cum ahegao with hpunch
        "And then I hear the sound of Sam wailing as I shoot my load inside her ass."
        with hpunch
        if randint(0, 1):
            "When I slide free, she reaches back, scoops a warm spill onto her fingers, and sucks it clean with a lazy smile."
        "Her entire body seems to quiver and shake, like she's cumming too."
        show samantha flat doggy pleasure with hpunch
        "Then the last of her strength evaporates and she collapses onto the sand."
        show samantha flat doggy out -cum
        "As gently as I can manage, I pull myself out of Sam's ass."
        "There's barely a sound as I do so, but she must feel it."
        "Because she rolls onto her back and looks up at me."
        show samantha flat doggy normal
        "Sam's eyes are still more than a little glazed over."
        "And she seems to be in the process of coming back down to earth."
        hide samantha flat doggy
        show samantha naked flirt blush at center, zoomAt(1.5, (640, 1100))
        with fade
        "But she has a smile on her face that let's me know she's satisfied."
        samantha.say "Whoo..."
        samantha.say "I feel kind of dizzy!"
        samantha.say "What did you do to me, [hero.name]?"
        "After all that, she actually has the cheek to blame me?"
        "I can't help chuckling and shaking my head as I reply."
        if samantha.flags.nickname == "cupcake":
            mike.say "Nothing you didn't as me to, Cupcake!"
        else:
            mike.say "Nothing you didn't as me to, Sam!"
        "Sam looks at me in confusion for a moment."
        "But then she nods in agreement."
        show samantha naked happy
        samantha.say "Fair...that's fair."
        samantha.say "But I need you to help me out with something else now."
        "I roll my eyes."
        if samantha.flags.nickname == "cupcake":
            mike.say "Really, Cupcake?"
        else:
            mike.say "Really, Sam?"
        mike.say "What is it now?"
        "Sam looks embarrassed, like she can't quite meet my eye."
        "But she manages to ask the question all the same."
        samantha.say "I...I think I got sand all up in my butt-crack!"
        show samantha naked flirt blush
        samantha.say "I don't suppose you'd help me get it out?"
    $ samantha.love += 2
    $ samantha.flags.anal += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
