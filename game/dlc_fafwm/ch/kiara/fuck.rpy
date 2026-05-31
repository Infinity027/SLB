init python:
    InteractActivity(**{
    "name": "fuck_kiara",
    "display_name": "Fuck",
    "label": "ACTIVE_GIRL_fuck_ROOM",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            HasStamina(),
            ),
        PersonTarget(kiara,
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
    "name": "kiara_hottub_sex_male",
    "label": "kiara_hottub_sex_male",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            HasStamina(),
            IsActivity("date_hot_tub_home")),
        PersonTarget(kiara,
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


label kiara_hottub_sex_male:
    $ game.active_date.clothes = "swimsuit"
    $ CONDOM = False
    "When I invited Kiara to come around for a dip in the hot-tub, I was only really half serious about it."
    "Because like, sure I want her to come over to my place and strut around in her swimming-costume."
    "But part of me is always convinced something like is only ever going to be a fantasy I dreamed up."
    "So when she casually said yes, I smiled and nodded calmly, telling her a date and a time to come over."
    "And all the while I was going into a crazy spin inside of my own head at the mere thought of it."
    "Which is how I came to be here, having shooed my housemates out of the door and done the best I can to clean up."
    play sound door_knock
    "When I hear the sound of a knock at the door, I hastily toss the dust-pan and brush aside."
    play sound door_open
    "Then dash into the hallway, wearing nothing but my swimming trunks, and open the door."
    scene bg house
    show kiara d
    with fade
    mike.say "Hey, Kiara..."
    mike.say "I'm so glad that you could make it!"
    mike.say "Come in, come in."
    "In contrast to my state of agitation, Kiara's her usual cool and controlled self."
    "Looking me up and down with a knowing smile on her pretty face."
    show kiara a surprised
    kiara.say "Oh my, [hero.name]…"
    kiara.say "How handsome you look in your little shorts!"
    kiara.say "It is lucky that I was the one at the door and not the man with the mail."
    show kiara d normal
    "Kiara walks into the hallway as I step aside to make room for her."
    "And I do the best I can to smile and shrug off her playful comments."
    "But the fact is that I'm already aware of the way she's eyeing me up."
    scene bg livingroom with fade
    show kiara with easeinleft
    mike.say "Erm..."
    mike.say "The hot-tub is on the back porch, Kiara..."
    mike.say "So if you want to follow me?"
    show kiara a talkative
    kiara.say "But of course I do."
    kiara.say "Otherwise I might get lost!"
    show kiara normal
    "Kiara follows close on my heels as I lead her the short distance to the back of the house."
    "Hoping all the time that her eyes are on me and not the humble nature of my home."
    scene bg pool at center, zoomAt(1.2, (640, 820)) with fade
    show kiara at center, zoomAt(1.4, (640, 920)) with easeinleft
    "We emerge onto the back porch, with me hoping that my efforts to make it nice are obvious."
    "And I take heart from the fact that the smile stays on Kiara's face as she surveys the scene."
    mike.say "I've made sure the water's the perfect temperature."
    mike.say "So if you want to maybe slip inside and change?"
    "Kiara doesn't dignify the question with an answer that involves words."
    "Instead she drops all the stuff she's carrying onto a nearby chair and kicks off her shoes."
    "Then she kind of fiddles with the dress she's wearing, doing something I don't quite understand."
    "And once she removes her hand, the whole thing drops off of her."
    "I mean that literally - it just falls to the groups like a discarded towel."
    "For a moment I think that I'm going to see Kiara in her underwear - or even naked!"
    "But when my eyes manage to focus on her form again, sanity seems to have returned."
    show kiara swimsuit
    "Because now I can see that Kiara was wearing her swimming-costume under her dress."
    "And though that's less outrageous than her being naked, it's not at all demure."
    show bg pool at center, traveling(1.2, 1, (640, 720))
    show kiara flirt at center, traveling(1.4, 1, (640, 720))
    pause 2
    kiara.say "Oh..."
    kiara.say "I see that you approve of my bathing-suit, [hero.name]?"
    show bg pool at center, traveling(1.2, 1, (640, 820))
    show kiara at center, traveling(1.4, 1, (640, 920))
    pause 2
    kiara.say "Because you certainly seem to be unable to tear your eyes away from it!"
    show kiara normal
    "At first all I can do is nod in a stupefied silence, and who could blame me?"
    "Kiara's wearing a strapless one-piece affair in shade of red."
    "The cut of which accentuates every curve of her body."
    "And the colour perfectly compliments her eyes too."
    mike.say "Of course not, Kiara..."
    mike.say "You look totally amazing!"
    mike.say "I...I mean not that you don't usually look amazing..."
    mike.say "You just look even more amazing now than you usually do!"
    "Kiara chuckles and shakes her head."
    show kiara flirt
    kiara.say "Oh, [hero.name]..."
    kiara.say "You are so adorable when you are reduced to a babbling mess!"
    show kiara normal
    "Without another word, Kiara takes hold of my hand and turns towards the hot-tub."
    "Part of me thinks that, as this is my place, I should be the one making all the moves."
    "But somehow I don't seem to be able to resist letting her lead me into the bubbling water."
    show hottub kiara swimsuit with fade
    "Kiara and I sit down in the tub, the water coming up to our waists."
    "The distance between us enough to be comfortable, but not so much as to be awkward."
    kiara.say "Mmm..."
    kiara.say "You were not lying, [hero.name]..."
    kiara.say "The water is just right for relaxing."
    mike.say "Yeah, I never lived anywhere that had one of these before I moved in here."
    mike.say "But now I couldn't imagine not being able to come out here and jump in it."
    mike.say "I guess it's funny how you get used to these things so easily."
    "Kiara's lips curve into a slow, seductive smile as she listens to me."
    "And she spreads her arms out along the edge of the tub, letting herself float in the water."
    kiara.say "I certainly did not have anything like this when I was growing up."
    kiara.say "But in the old country, we had hot springs that occurred naturally."
    kiara.say "And everyone would swim in those whenever the chance arose."
    "As soon as Kiara starts talking about her homeland, my ears prick up."
    "Because she's usually quite guarded about her past and the secrets it holds."
    "Maybe the chance to relax and unwind is loosening her tongue?"
    mike.say "Whoa..."
    mike.say "You mean, like, volcanic springs?"
    mike.say "The kind that bubble and all that?"
    "Kiara cocks her head on one side, as if considering my questions."
    "And thinking up an answer based on relaxed whimsy."
    kiara.say "Hmm..."
    kiara.say "I think that is what you would call them."
    kiara.say "They were so beautiful - the water a pure, azure colour."
    mike.say "Yeah, Kiara..."
    mike.say "That does sound totally amazing."
    mike.say "Much more amazing than my little hot-tub in the garden!"
    kiara.say "Oh, I do not know about that..."
    kiara.say "Some would say that it was the company one keeps that makes a thing special."
    "The tone of Kiara's voice has suddenly turned quite intense, almost sensual."
    "So much so that I can't help but turn to look in her direction as soon as I hear it."
    "And when I do, I see that she's staring straight at me, gazing into my very soul!"
    kiara.say "Would you like me to show you what we used to do in those pools, [hero.name]?"
    kiara.say "What we would do when there were only two of us bathing together?"
    mike.say "Erm..."
    mike.say "Y...yeah, Kiara..."
    mike.say "I think I'd like that more than anything!"
    "Kiara nods her head as she pushes herself off the edge of the tub."
    "The water isn't deep enough to actually swim, not by a long way."
    "But she still manages to propel herself through it in one smooth motion."
    "Gracefully turning her back to me as she comes and floating into my arms."
    "And I feel the sensation of her buttocks bumping into my groin."
    "Kiara reaches back and takes hold of my wrist, then pulls my hand underwater."
    "Not hesitating to guide it between her thighs and place my fingers on her most intimate parts."
    "Kiara's literally been leading me by the hand up to this point."
    "But now it feels like I know exactly what she wants, and I can take over."
    "So I begin to stroke gently, going up and down the length of her sex."
    "Almost instantly she starts to moan at the sensation, nodding her head."
    "And then she leans back into me, pressing her back into my chest."
    "I choose to take this as Kiara giving me her approval, her permission to take it to the next level."
    "So my fingers pluck at the material of her swimming-costume, pulling it aside."
    "And as soon as the tips touch the bare lips of her pussy, she gasps and moans."
    kiara.say "Ah..."
    kiara.say "Oh yes..."
    kiara.say "Touch me there - please?"
    "Man, is it ever easy to give a girl what she wants when it's the exact same thing you do!"
    "I mean, it's not like Kiara would really have to beg me to play with her pussy, now is it?"
    "But almost as soon as my fingers start tracing the lines of her lower lips, I know it won't be enough."
    "Every touch seems to make Kiara quiver and quake in my arms, to make her sigh and moan gasp even more."
    "And I can already feel the sensation of my cock as it strains against the waistband of my shorts."
    "Luckily for me, it seems that Kiara can feel it from where she's sitting too."
    kiara.say "Urgh..."
    kiara.say "I...I need more, [hero.name]…"
    kiara.say "I must have you...inside of me!"
    "I nod, tyring to make it look like I'm selflessly doing all I can to satisfy Kiara."
    "When the reality is that I want to be inching into her more than anything right now."
    "And so I pull the gusset of her swimming-costume aside with one hand."
    "While clumsily pulling down my own trunks with the other."
    show hottub sex male kiara outside with fade
    "As soon as it's free, my cock bobs up in the water, breaking the surface."
    "And it the tip brushes against the exposed lips of Kiara's pussy."
    "Instantly she tries as best she can to sit down on it."
    "Which gives me no more than a split second to decide where I want it to go."
    menu:
        "Fuck her pussy":
            "And there's no mystery about that, now is there?"
            "I want to feel myself sinking into Kiara's pussy."
            "So all I need to do is make sure that's where it goes."
            "A little at a time, Kiara lowers herself onto me."
            "The head pressing against her lips for a prolonged moment as they resist."
            "But then gravity and the sheer need between us becomes too much."
            "Kiara lets out a little cry and clings onto me as they begin to part."
            "And I do the same, gasping and holding her tightly as we come together."
            "She sinks down a fraction of an inch at a time, prolonging the experience."
            show hottub sex male kiara inside with dissolve
            "Which means that by the time I can go no further, we're both totally flustered."
            "There's no sudden and explosive thrusting going on here."
            "Instead Kiara moves slowly in my arms, and I move in sympathy with her."
            "Using the side of the tub to prop myself up, I make love to her gently."
            "And she lets the water bear her weight, allowing me to slide back and forth."
            "Knowing that I can still hold her up, I begin to let my hands roam."
            "They travel over the curves of Kiara's body, stroking and caressing her."
            "The feel of the swimming-costume stretched over her contrasting with her naked skin."
            "But as soon as they settle on her chest, I feel something stirring inside of me."
            "And instead of gentle caresses, I squeeze and massage her breasts like never before."
            "In the blink of an eye, I've pulled down the front of Kiara's swimming-costume."
            "Freeing her breasts and spilling them onto her chest, bare and exposed."
            "At the same time my pace quickens below, pushing into her harder than before."
            "Kiara responds in kind, pushing down and griding herself into me."
            "Of course her enthusiasm only serves to make me try harder still."
            "And soon enough I can feel the sensation of her pussy beginning to squeeze me."
            "A moment later Kiara's entire body stiffens and she bears down on me like never before."
            "Her orgasm is so intense that it gives me no chance to prepare myself."
            "And I know that I'm going to be swept away any second."
            call cum_reaction (kiara, 'vaginal', 1) from _call_cum_reaction_326
            if _return == "vaginal_outside":
                "Holding onto Kiara more tightly than ever, I pull myself downwards."
                show hottub sex male outside ahegao
                "And at the same time I lift her up and off of me in one smooth motion."
                show hottub cumshot with vpunch
                $ kiara.sub += 1
                "This means that my cock slides out of her just before I explode."
                with vpunch
                "Making her arch her back and cry out, before slumping back against me."
                "Cum spattering down on her exposed buttocks."
            else:
                "Holding onto Kiara more tightly than ever, I pull her downwards."
                "And at the same time I thrust myself up from below."
                show hottub cumshot ahegao with vpunch
                $ kiara.love += 1
                "This means that I'm as deep into her as possible when I explode."
                with vpunch
                "Making her arch her back and cry out, before slumping back against me."
        "Fuck her ass":
            "But the twist is that I want very badly to put it in the other hole."
            "I want to feel myself sinking into Kiara's beautifully tight ass."
            "So all I need to do is make sure that's where it goes."
            "A little at a time, Kiara lowers herself onto me."
            "The head pressing between her buttocks and wedging against the edge of her hole."
            "But then gravity and the sheer need between us becomes too much."
            "Kiara lets out a little cry and clings onto me as her muscles begin to relax."
            "And I do the same, gasping and holding her tightly as we come together."
            "She sinks down a fraction of an inch at a time, prolonging the experience."
            show hottub sex male kiara inside with dissolve
            "Which means that by the time I can go no further, we're both totally flustered."
            "There's no sudden and explosive thrusting going on here."
            "Instead Kiara moves slowly in my arms, and I move in sympathy with her."
            "Using the side of the tub to prop myself up, I make love to her gently."
            "And she lets the water bear her weight, allowing me to slide back and forth."
            "Knowing that I can still hold her up, I begin to let my hands roam."
            "They travel over the curves of Kiara's body, stroking and caressing her."
            "The feel of the swimming-costume stretched over her contrasting with her naked skin."
            "But as soon as they settle on her chest, I feel something stirring inside of me."
            "And instead of gentle caresses, I squeeze and massage her breasts like never before."
            "In the blink of an eye, I've pulled down the front of Kiara's swimming-costume."
            "Freeing her breasts and spilling them onto her chest, bare and exposed."
            "At the same time my pace quickens below, pushing into her harder than before."
            "Kiara responds in kind, pushing down and griding herself into me."
            "Of course her enthusiasm only serves to make me try harder still."
            "And soon enough I can feel the sensation of her muscles beginning to squeeze me."
            "A moment later Kiara's entire body stiffens and she bears down on me like never before."
            "Her orgasm is so intense that it gives me no chance to prepare myself."
            "And I know that I'm going to be swept away any second."
            call cum_reaction (kiara, 'anal', 1) from _call_cum_reaction_327
            if _return == "anal_outside":
                "Holding onto Kiara more tightly than ever, I pull myself downwards."
                show hottub sex male outside
                "And at the same time I lift her up and off of me in one smooth motion."
                show hottub cumshot ahegao with vpunch
                $ kiara.sub += 1
                "This means that my cock slides out of her ass just before I explode."
                with vpunch
                "Making her arch her back and cry out, before slumping back against me."
                "Cum spattering down on her exposed buttocks."
            else:
                "Holding onto Kiara more tightly than ever, I pull her downwards."
                "And at the same time I thrust myself up from below."
                show hottub cumshot ahegao with vpunch
                $ kiara.love += 1
                "This means that I'm as deep into her ass as possible when I explode."
                with vpunch
                "Making her arch her back and cry out, before slumping back against me."
    "Once we're both spent, Kiara lets herself go limp in my arms."
    "And she floats in the water, head resting on my shoulder."
    kiara.say "Oh yes..."
    kiara.say "That is exactly what we used to do in those pools back home!"
    kiara.say "Who knows, [hero.name]…"
    kiara.say "One day I may take you there, and we can do it for real."
    kiara.say "How does that sound to you?"
    mike.say "It sounds great, Kiara..."
    mike.say "It sounds pretty damn great!"
    call stop_all_sfx from _call_stop_all_sfx_74
    show bg black with fade
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ kiara.sexperience += 1
    $ game.active_date.clothes = None
    return


label kiara_fuck_date_male(location="hero"):
    $ renpy.dynamic(skip_foreplay=False, cum_foreplay=False)
    $ game.play_music("music/roa_music/city_nights.ogg")
    scene bg street
    show kiara


    call kiara_fuck_date_intro_male (location) from _call_kiara_fuck_date_intro


    call kiara_dick_reactions_male from _call_kiara_dick_reactions


    call kiara_fuck_date_foreplay_male from _call_kiara_fuck_date_foreplay_male


    if skip_foreplay:
        pass
    elif cum_foreplay:
        if hero.sexperience >= 20:
            "For a moment I wonder if I'm going to have the energy to keep on going."
            "But then I take one look at Kiara, as she's stretching on the bed before me."
            "And I know that I'm more than ready for whatever's coming next."
        else:
            "I haul myself up, trying to summon my strength for what's coming next."
            "But then I feel myself collapsing onto the bed in front of Kiara."
            "The truth is that I'm totally exhausted, and my eyes are getting heavy."
            "But before they close, I see a look of annoyance on Kiara's face."
            "Then I'm gone, fallen asleep and probably snoring loudly too."
            $ kiara.love -= 20
            $ kiara.sub -= 5
            hide kiara
            call sleep from _call_sleep_131
            return


    call kiara_fuck_date_choices_male from _call_kiara_fuck_date_choices_male


    call handle_npc_leaving (kiara, _return) from _call_handle_npc_leaving_32
    if _return:
        return


    hide kiara
    call kiara_fuck_date_sleep (location="hero") from _call_kiara_fuck_date_sleep
    return

label kiara_fuck_date_intro_male(location="hero"):
    if kiara.sexperience == 0:
        scene bg house
        show kiara at center, zoomAt(1.25, (640, 880))
        with fade
        "It's only as we're getting out of the taxi and walking up to the front door that I feel the nerves really start to kick in."
        "Because up to now I've been too caught up in the excitement of Kiara agreeing to come back to my place to actually think straight."
        "And the moment that my thoughts clear, I realise that I'm about to bring a sophisticated woman back to my humble little house."
        "Or to be more specific, a house that I share with a bunch of typically lazy and messy girls!"
        "But the problem is that we're already stepping onto the porch and approaching the front-door."
        "There's no way that I can just ask Kiara to wait out here while I hurry inside and try to tidy the place up!"
        "So instead I have to make to with looking back over my shoulder as I open the door."
        "And putting what I hope is a nonchalant face on as I do so."
        mike.say "So, here we are..."
        mike.say "Welcome to Casa [hero.name]!"
        mike.say "It might be quite humble, but I like to feel it's also homely."
        "Kiara raises a single eyebrow as she regards me, a languid smile on her face."
        "And part of me is sure that she's more than able to see through my bullshit."
        "But the hope is that she's finding it amusing, maybe even endearing, rather than tedious and annoying."
        show kiara talkative
        if kiara.sub >= 25:
            kiara.say "I'm sure that it's a very fine house, [hero.name]…"
            kiara.say "But I'd know for sure if you were to invite me inside."
        elif kiara.sub < -25:
            kiara.say "How am I ever going to know if that's the truth, [hero.name]?"
            kiara.say "Unless you're planning on inviting me inside?"
        else:
            kiara.say "Well all I can see of it at the moment is the outside."
            kiara.say "How am I supposed to make up my mind without seeing inside?"
        show kiara normal
        "I'm nodding as I open the door and begin to usher Kiara inside."
        "But I pause as my hand is halfway to the light-switch, remembering my fears about the mess."
        mike.say "Well, let's do something about that, shall we?"
        mike.say "Only thing is, I'm gonna keep the lighting subdued."
        mike.say "That way we can...preserve the mood."
        show kiara smile at startle
        pause 0.3
        show kiara normal at center, traveling(1.5, 0.5, (640, 1040))
        "Kiara chuckles and shakes her head as she steps into the hallway."
        "But I note that she doesn't object to me keeping the lights low."
        "Instead she reaches out, offering me her hand to take."
        scene bg livingroom at dark, dark with fade
        pause 0.3
        show kiara normal at dark, center, zoomAt(1.5, (640, 1040)) with easeinright
        "And I do so, wasting no time in beginning to lead her through the house."
        "Every step of the way I'm conscious of the danger that I might slip or trip over something half-seen in the gloom."
        "On top of that there's the constant fear of bumping into one of my housemates going to the bathroom or getting a midnight snack."
        scene bg bedroom1 with fade
        pause 0.3
        show kiara normal at center, zoomAt(1.5, (940, 1040)) with easeinright
        "So it comes as a genuine relief when I manage to steer Kiara to the door of my bedroom without incident."
        "And once we're there, I turn the handle and almost drag her inside, before shutting it behind us."
        show kiara fantasize at center, traveling(1.25, 0.5, (540, 880))
        "Once I've made sure the door is firmly closed, I turn around to see Kiara inspecting the décor of my room."
        "Normally I'd be very defensive of the sci-fi posters and collectibles that I've amassed over the years."
        "But there's just something so refined and sophisticated about her that I don't feel like doing so."
        mike.say "Erm..."
        mike.say "Sorry if the décor's not up to your standards, Kiara."
        mike.say "I guess it's kind of a single-guy thing, you know?"
        show kiara flirt at center, zoomAt(1.25, (640, 880)) with ease
        "Kiara turns slowly to regard me, the same languid smile still on her face as she does so."
        show kiara talkative
        if kiara.sub >= 25:
            kiara.say "This is your home, [hero.name]…"
            kiara.say "You must know that I would never judge your taste!"
        elif kiara.sub < -25:
            kiara.say "Oh, [hero.name]…"
            kiara.say "You are worried that I will find your tastes childish?"
        else:
            kiara.say "You are afraid that I find all of these things childish, yes?"
            kiara.say "That I think a real man would have long ago lost interest in them?"
        show kiara normal
        mike.say "I..."
        mike.say "I guess so."
        show kiara smile at startle
        "Kiara gives me another one of those irresistible little chuckles of hers."
        "The kind that are more like sexual signals than expressions of actual amusement."
        show kiara talkative
        if kiara.sub >= 25:
            kiara.say "In fact, I find all of this very inspiring."
            kiara.say "It tells me you are a man of great imagination."
            kiara.say "And maybe, if I am lucky, you will use some of that imagination to pleasure me!"
        elif kiara.sub < -25:
            kiara.say "Quite the contrary, [hero.name]…"
            kiara.say "You have your toys and I now have a new one of my own - you, to be precise."
            kiara.say "And now I intend to play with you until I am totally satisfied!"
        else:
            kiara.say "Well, I do not."
            kiara.say "To me, these things say that you are a man with an open mind, with imagination."
            kiara.say "And imagination is one of the most exciting things that a man can have in the bedroom!"
        show kiara flirt at center, traveling(1.5, 1.0, (640, 1040))
        "Kiara closes the distance between us as she says this."
        show kiara underwear
        "And it's hard to miss the fact that she's fiddling with her clothes as she does so."
        "Honestly, I have no idea how she manages to pull this off, none at all."
        "But by the time she's standing in front of me, her clothes fall off."
        "And I really mean that, they just drop off of her and land in a pile on the ground."
        "One minute Kiara's fully clothed, and the next she's standing in front of me in her underwear!"
        mike.say "Whoa..."
        mike.say "What the hell?"
        mike.say "How did you do that?!?"
        show kiara talkative
        if kiara.sub >= 25:
            kiara.say "Just a little trick I picked up along the way."
            kiara.say "But there are more pressing matters at hand."
            kiara.say "Like your unleashing all of that imagination upon me!"
        elif kiara.sub < -25:
            kiara.say "I don't remember giving my little toy permission to talk back!"
            kiara.say "But I do remember telling you to unleash your imagination."
            kiara.say "So what are you waiting for?"
        else:
            kiara.say "The how does not matter, [hero.name]…"
            kiara.say "What matters is the way you choose to respond."
            kiara.say "How you choose to express that imagination of yours to me now."
        show kiara normal
        "I feel like I'm beginning to get what Kiara's saying to me."
        "That I understand she wants me to be impulsive and to express myself."
        "Which is why I choose to answer her with actions, rather than words."
        hide kiara
        show kiara kiss underwear
        with fade
        "Specifically I lean forwards and place my lips against hers."
        "And the moment that we touch, I feel a genuine spark."
        "One that spurs me on to wrap my arms around Kiara and pull her in close."
        "All the while the kiss is becoming even more intense, and I feel her pulling at my clothes."
        "Soon enough my tongue is exploring as Kiara's wraps around it inside of her mouth."
        "And I'm stripped down to my underwear, feeling her pulling at the waistband of my shorts."
    else:
        scene bg house
        show kiara at center, zoomAt(1.25, (640, 880))
        with fade
        "I feel like I've gotten to know Kiara so well by now that I don't have anything to hide from her."
        "In fact it seems pretty strange to me that I was nervous the first time I brought her back to my place."
        "But now all of that feels so silly - like she was really going to judge me for living where I do!"
        "In fact, she seems to treat coming to my place like a break from the world that she's used to."
        "Normally Kiara's all cool, calm and sophisticated, projecting her image of total control."
        "But once we're out of the taxi and through my front-door, she seems to be able to let her guard down."
        scene bg bedroom1 with fade
        pause 0.3
        show kiara mischievous at center, zoomAt(1.5, (940, 1040)) with easeinright
        "And the playful, almost mischievous version of Kiara that pops out as soon as I close the door to my room..."
        "Well that's what really makes the whole thing extra-special!"
        "Already peeling my clothes off me as I make sure the door's closed, Kiara seems as impatient as usual."
        show kiara talkative
        if kiara.sub >= 25:
            kiara.say "May we get started, [hero.name]?"
            kiara.say "I feel like I've waited forever for you to hold me!"
        elif kiara.sub < -25:
            kiara.say "No time for idle chit-chat, [hero.name]…"
            kiara.say "I want you, and I am not prepared to wait any longer!"
        else:
            kiara.say "Come on, [hero.name]…"
            kiara.say "I am surrounded by your posters and books about fantastical things."
            kiara.say "And you know what that does to me, how it makes me want to sample the fruits of your imagination!"
        show kiara normal
        mike.say "Okay, Kiara, okay..."
        mike.say "I'm coming as fast as I can!"
        show kiara talkative
        if kiara.sub >= 25:
            kiara.say "But, [hero.name]…"
            kiara.say "It is my job to make you cum!"
        elif kiara.sub < -25:
            kiara.say "Oh no, [hero.name]…"
            kiara.say "Not before you have made me cum first!"
        else:
            kiara.say "Oh no, [hero.name]…"
            kiara.say "I want it to be a long time before you cum!"
        show kiara flirt naked with fade
        "It takes no more than a few seconds for us to tear each other's clothes off."
        "And all the time we're no more than a few inches apart, kissing and caressing."
    $ game.room = "bedroom1"
    return

label kiara_fuck_date_foreplay_male:
    hide kiara
    show kiara flirt naked at center, zoomAt(1.5, (640, 1040))
    with fade
    "As soon as the last item of clothing comes off and is tossed away, I see Kiara eyeing me hungrily."
    "At times like this, she always reminds me of a female big-cat that's about to pounce on its prey."
    "And so the sensations that the looks stirs in me are a strange mix of fear and arousal."
    show kiara talkative
    if kiara.sub >= 25:
        kiara.say "I await your command, [hero.name]…"
        kiara.say "What is it that you desire of me?"
    elif kiara.sub < -25:
        kiara.say "Be quick now, [hero.name]…"
        kiara.say "Tell me what you desire!"
    else:
        kiara.say "So, [hero.name]…"
        kiara.say "What is your pleasure?"
    show kiara flirt
    mike.say "You're..."
    mike.say "You're letting me choose?"
    show kiara mischievous
    "Kiara nods slowly as she looks me up and down."
    "All the time looking like she's choosing which part of me she wants to devour first."
    show kiara talkative
    if kiara.sub >= 25:
        kiara.say "Of course!"
        kiara.say "Your pleasure is my pleasure."
    elif kiara.sub < -25:
        kiara.say "Only because it amuses me."
        kiara.say "And I reserve the right to overrule you, should you choose badly!"
    else:
        kiara.say "But of course..."
        kiara.say "Just say the word, and your pleasure will become mine too!"
    show kiara flirt
    menu:
        "Suggest a blowjob" if kiara.sub >= 10:
            call kiara_fuck_date_blowjob from _call_kiara_fuck_date_blowjob
        "Ask for a sixty-nine" if kiara.sub >= 25:
            call kiara_fuck_date_sixty_nine from _call_kiara_fuck_date_sixty_nine
        "Eat her pussy" if hero.sexperience >= 5:
            call kiara_fuck_date_cunnilingus from _call_kiara_fuck_date_cunnilingus
        "Fuck her right now":
            $ skip_foreplay = True
    call stop_all_sfx from _call_stop_all_sfx_65

    return _return

label kiara_fuck_date_choices_male:
    menu:
        "Cowgirl":
            call kiara_fuck_date_cowgirl (0) from _call_kiara_fuck_date_cowgirl
        "Missionary" if hero.sexperience >= 5:
            call kiara_fuck_date_missionary (5) from _call_kiara_fuck_date_missionary
        "Standing" if hero.sexperience >= 10:
            call kiara_fuck_date_standing (10) from _call_kiara_fuck_date_standing
    call stop_all_sfx from _call_stop_all_sfx_66

    return _return

label kiara_fuck_date_sleep(location="hero"):
    scene bg bedroom1
    if game.hour > 19 or game.hour < 6:
        show kiara naked talkative at center, zoomAt(1.25, (640, 880))
        if kiara.is_sex_slave:
            kiara.say "May I share your bed tonight, Master?"
        else:
            kiara.say "[hero.name], can I spend the night the night here?"
        show kiara normal
        menu:
            "No":
                mike.say "No...I have to be up really early in the morning."
                "The sex was beyond incredible, but now I want to be alone."
                "Kiara frowns in disappointment, clearly trying to shrug off the sense of rejection."
                show kiara whining
                kiara.say "Okay...sleep well."
                show kiara sad
                "She shakes her head as she collects her things and leaves my bedroom."
                $ kiara.love -= 3
                call sleep from _call_sleep_132
            "Yes":
                mike.say "YES...I mean, of course you can!"
                "I try to keep from sounding too desperate and needy, but I'm not sure I manage it."
                show cuddle kiara
                "Kiara curling up against me beneath the covers is almost as good as the sex - almost..."
                if kiara.is_sex_slave:
                    kiara.say "Sweet dreams, Master..."
                else:
                    kiara.say "Sweet dreams, [hero.name]..."
                mike.say "You too, Kiara..."
                $ kiara.love += 3
                call sleep ("kiara") from _call_sleep_133
    return

label kiara_fuck_date_blowjob:
    "I can see the way that Kiara's eyes are lingering on my manhood."
    "The way that they seem to almost flare with naked desire for it."
    "And the result is that I can already feel it beginning to stiffen and rise."
    "Hell, it would have been hard soon enough with me simply staring at her naked body."
    "But with her looking at me like that, it's going to take mere seconds."
    "And now I'm more than intrigued to see what she wants to do with it."
    mike.say "Well, maybe you could..."
    mike.say "I dunno...give me a BJ?"
    mike.say "You know, if it's not too much trouble?"
    "Before I said that I could see a flare of desire in Kiara's eyes."
    "But now they seem to burst into a veritable blaze of naked lust."
    "And without another word, she stretches out one arm."
    show kiara naked evil at center, zoomAt(1.25, (640, 880)) with hpunch
    "Kiara's open palm slaps into my chest, and then she gives me a shove."
    "It's hard and totally unexpected, which means I'm instantly pushed backwards."
    with hpunch
    "I bump into the shelves I was standing in front of, shaking them and their contents."
    mike.say "Wha…"
    mike.say "Urgh..."
    "Kiara doesn't seem in the least bit concerned by the sounds that I'm making."
    "Even less so if any of he valuable collectables on the shelves are dislodged."
    "In fact I doubt that she's even aware of the shelf being there at all."
    hide kiara with easeoutbottom
    "Because she's already crouching down in front of me."
    scene bg black
    show kiara bj happy
    with fade
    "Kiara wastes no time in lowering herself until her head is level with my groin."
    "Reaching out with one hand, she gently takes hold of my cock."
    "Her fingers wrap around the base of the shaft, giving it a light squeeze."
    mike.say "Ah..."
    "Even something so soft is enough to make me gasp at the sensation."
    "And I swear that I see the corner of Kiara's mouth twist into a smile."
    "But there's no time to wonder if she's getting a kick out of my reaction."
    show kiara bj blowjob
    "Because the very next moment, her lips part and her tongue darts out."
    "And the second it makes contact with the tip of my cock, that's it."
    "All I can do is flatten myself against the shelves, almost like I'm clinging on for dear life."
    play sexsfx1 bj_openmouth
    show kiara bj at stepback(0.09, 10, 0)
    "Kiara takes it inside of her mouth a little at a time, upping the stakes with aching slowness."
    "As my cock travels deeper into Kiara's mouth, her hand moves up the shaft."
    "It's not like she's really working it with her fingers, at least not like a genuine hand-job."
    "More like her hand is serving to steer her efforts and keep everything in place."
    "But once her lips and fingertips meet, Kiara's hand falls away, leaving it to her mouth."
    "And that's when things seem to change into a whole different gear for me."
    "Now she uses her hands to hold onto my legs, bracing herself against my calves."
    "And I can feel the soft pressure of her breasts against me as she leans into it."
    play sexsfx1 bj_sucking loop
    show kiara bj at stepback(0.07, 10, 0)
    pause 0.2
    show kiara bj at stepback(0.07, 10, 0)
    "Kiara's head moves back and forth, working away at my cock inside of her mouth."
    "From the outside, it might not look like there's much going into the effort."
    "But I can feel everything that's happening inside of there, and it's pretty crazy."
    "From the way my cock is being caressed, I'd swear Kiara had more than one tongue!"
    show kiara bj at stepback(0.07, 10, 0)
    pause 0.2
    show kiara bj at stepback(0.07, 10, 0)
    "And part of me is sure that it's already starting to reach all the way into her throat."
    "Until now, she's had her eyes firmly closed, as if totally devoted to the act."
    "So it almost makes me jump in surprise when they suddenly open again."
    "My own eyes must be wide with amazement as I gaze into Kiara's."
    "But that doesn't last long, as I soon see the way she's looking at me."
    show kiara bj pleasure at stepback(0.07, 10, 0)
    pause 0.2
    show kiara bj at stepback(0.07, 10, 0)
    "Kiara's eyes are languid, almost sleepy as he stares upwards."
    "And yet it's plain to see that it's on account of enjoying what she's doing."
    show kiara bj at stepback(0.07, 10, 0)
    pause 0.2
    show kiara bj at stepback(0.07, 10, 0)
    "Kiara looks almost blissed-out to be working away on my cock."
    "And the realisation makes me swell up inside, wanting her all the more."
    show kiara bj at stepback(0.07, 10, 0)
    pause 0.2
    show kiara bj at stepback(0.07, 10, 0)
    "But then it seems to make me swell up for real, and feel like I'm going to burst!"
    menu:
        "Facial":
            "Almost too deeply into what's happening to talk, I still need to communicate with Kiara."
            "But my instinct is just to pull back and attempt to drag myself out of her mouth before it's too late."
            "The only problem is that, in my haste, I seem to have forgotten the shelves behind me."
            "Which means that I bump into them, sending books and action figures falling onto the floor."
            play sexsfx1 slide_out
            show kiara bj happy with hpunch
            "Luckily for me, Kiara seems to catch onto what I'm trying to do, and she soon releases me."
            "Pulling her head back, she sits patiently in front of me, waiting for the inevitable to happen."
            play sexsfx1 cum_outside
            show kiara bj cum closed hurt with hpunch
            pause 0.3
            show kiara bj bodycum pleasure happy
            "And when it does, I shoot my load straight into her face, painting her cheeks with white stripes."
            $ cum_foreplay = True
        "Swallow":
            "There's nothing that I could do to tell Kiara if I was of a mind to pull out before the end."
            "And so I just resign myself to riding it out and letting nature take it's course."
            "Luckily for me it seems that she's well aware of what's going on inside of her mouth."
            "Meaning that she keeps right on going, making subtle preparations for the inevitable."
            show kiara bj cum blowjob with hpunch
            "All of this means that, when I finally shoot my load, Kiara's more than ready to handle it."
            play sexsfx1 bj_gulp
            show kiara bj with hpunch
            "Without missing a beat she swallows everything that I have to give, keeping pace with me perfectly."
            show kiara bj closed -cum with hpunch
            "I watch as she closes her eyes, pacing herself and holding me in place until it's all over."
            $ cum_foreplay = True
        "Hold it in" if hero.sexperience >= 10:
            "Somehow I manage to find a reserve of willpower, which I use to hold on for dear life."
            "But my instinct is just to pull back and attempt to drag myself out of her mouth to be sure."
            show kiara bj wide with hpunch
            "The only problem is that, in my haste, I seem to have forgotten the shelves behind me."
            "Which means that I bump into them, sending books and action figures falling onto the floor."
            play sexsfx1 slide_out
            show kiara bj happy with hpunch
            "Luckily for me, Kiara seems to catch onto what I'm trying to do, and she soon releases me."
            "Pulling her head back, she sits patiently in front of me, waiting to see what comes next."
    pause 0.5
    return

label kiara_fuck_date_sixty_nine:
    "I can see the way that Kiara's eyes are lingering on my manhood."
    "The way that they seem to almost flare with naked desire for it."
    "And the result is that I can already feel it beginning to stiffen and rise."
    "Hell, it would have been hard soon enough with me simply staring at her naked body."
    "But with her looking at me like that, it's going to take mere seconds."
    "And now I'm more than intrigued to see what she wants to do with it."
    mike.say "Well, maybe you could..."
    mike.say "I dunno...give me a BJ?"
    mike.say "You know, if it's not too much trouble?"
    "Before I said that I could see a flare of desire in Kiara's eyes."
    "But now they seem to burst into a veritable blaze of naked lust."
    "Though I guess that I'm doing the exact same thing too."
    "Because my eyes keep being drawn back to the same spot on Kiara's body."
    "And if she's wanting my cock, I'm wanting her pussy just as badly."
    mike.say "And maybe I could..."
    mike.say "I dunno...give give you oral?"
    mike.say "You know, like, at the same time?"
    show kiara mischievous
    "Before I said that I could see desire in Kiara's eyes."
    "But now they seem to burst with what can only be described as naked lust!"
    show kiara talkative
    if kiara.sub >= 25:
        kiara.say "Are you sure that's what you want?"
        kiara.say "Because that sounds like the best of both worlds!"
    elif kiara.sub < -25:
        kiara.say "So you want to get down on your knees and pleasure me at the same time as I pleasure you?"
        kiara.say "How could I possibly say not to that?!?"
    else:
        kiara.say "[hero.name], are you serious?"
        kiara.say "I would love to have you lick my pussy at the same time!"
    show kiara smile
    "Kiara smiles as she turns to walk the short distance to the bed."
    "And she doesn't even need to bother beckoning for me to follow her."
    "Because I hurry along, as if she has me on an invisible leash."
    hide kiara
    show kiara cowgirl
    with fade
    "Once there she crawls onto the mattress, turning over as she mounts it."
    "Then she plants herself down, spreading her thighs wide as she does so."
    "Kiara doesn't say a word, just leans back on her palms of her hands."
    "But again, she doesn't need to tell me a thing, or hint at what to do next."
    "And that's because by now I can see what's waiting for me between those legs."
    "Kiara's pussy is right there, exposed as she parts her thighs."
    "It's neat, beautiful to look at, and I can see it's already glistening in the light!"
    if kiara.sub >= 25:
        kiara.say "There you go, [hero.name]…"
        kiara.say "I'm all yours!"
    elif kiara.sub < -25:
        kiara.say "Now then, [hero.name]…"
        kiara.say "Are you going to take care of me like you promised?"
    else:
        kiara.say "What are you waiting for, [hero.name]?"
        kiara.say "Come over here and take it!"
    scene bg black
    show kiara sixtynine
    with fade
    "I nod as I climb onto the bed, my eyes already fixated on Kiara's pussy."
    "The only problem is that as I go for my prize, she seems to have the same idea."
    "I was aiming to end up on top of Kiara, with her beneath me."
    "But in making to grab my cock, she scuttles onto her side, eluding me."
    "All that I can do is follow, already starting to tie myself up in knots."
    "In the end she makes what looks almost like a dive for it."
    "And in the confusion, I find myself doing the same thing too."
    "Together we go almost into a roll, me ending up on the bottom and Kiara on the top."
    "I'm about to say something about the whole mess, to suggest we try again."
    "But then she almost literally sits on my face, which kind of settles the matter."
    mike.say "Wha…"
    mike.say "Mmmph!"
    "Just like that, any thought of stopping to complain vanishes from my head."
    "And the only thing that I can think about is pleasuring Kiara as best I can."
    show kiara sixtynine lick
    "My lips part and my tongue shoots out, going straight to work on what's before me."
    "Which just so happens to be the rather delectable pussy I was already so keen on."
    "Soon enough, the tip of my tongue is in amongst those soft folds."
    "And it's intent on going far deeper still, not stopping to take its time."
    "I'm so intent on my task that at first I hardly notice Kiara's reaction."
    play sexsfx1 bj_sucking
    show kiara sixtynine blowjob
    "It's only when she returns the favour that anything cuts through to my senses."
    "And let's just say that she's not being subtle about it at the other end either."
    show kiara sixtynine closed
    "From what I can feel, Kiara seems to have all but pounced on my cock."
    "Swallowing it as deep as she possibly can and then working it hard."
    show kiara sixtynine pleasure
    "Normally I know that I'd be trying my hardest to be elegant and refined with my technique."
    "And I get the feeling that Kaira would be doing the exact same thing on her end too."
    show kiara sixtynine closed
    "But the tumble and scramble seems to have left the pair of us in kind of a jumbled state."
    "Now the only thing that matters is going hard at the object of our respective attentions."
    show kiara sixtynine pleasure
    "And this frantic sexual energy is only feeding back again into what we're doing to each other."
    show kiara sixtynine closed
    "The more I pleasure Kiara, the more she pleasures me, and vice-versa."
    "Each of us pushing the other to go further and harder, then doing the same in return."
    "But there's no way something like this can go on forever."
    "I know it because I can feel the pressure building up inside of me."
    "And from the way she's starting to move, I think the same is true of Kiara."
    "Any moment, one of us is going to blow!"
    menu:
        "Facial":
            "Almost too deeply into what's happening to talk, I still need to communicate with Kiara."
            "But my instinct is just to pull back and attempt to drag myself out of her mouth before it's too late."
            play sexsfx1 slide_out
            show kiara sixtynine pleasure happy
            "Luckily for me, Kiara seems to catch onto what I'm trying to do, and she soon releases me."
            "Pulling her head back, she doesn't have to wait long for the inevitable to happen."
            play sexsfx1 cum_outside
            show kiara sixtynine closed hurt cum with vpunch
            "And when it does, I shoot my load straight into her face, painting her cheeks with white stripes."
            $ cum_foreplay = True
        "Swallow":
            "There's nothing that I could do to tell Kiara if I was of a mind to pull out before the end."
            "And so I just resign myself to riding it out and letting nature take it's course."
            "Luckily for me it seems that she's well aware of what's going on inside of her mouth."
            "Meaning that she keeps right on going, making subtle preparations for the inevitable."
            play sexsfx1 bj_gulp
            show kiara sixtynine wide blowjob cum with vpunch
            "All of this means that, when I finally shoot my load, Kiara's more than ready to handle it."
            with vpunch
            "Without missing a beat she swallows everything that I have to give, keeping pace with me perfectly."
            show kiara sixtynine closed blowjob -cum
            "I watch as she closes her eyes, pacing herself and holding me in place until it's all over."
            $ cum_foreplay = True
        "Hold it in" if hero.sexperience >= 10:
            "Somehow I manage to find a reserve of willpower, which I use to hold on for dear life."
            "But my instinct is just to pull back and attempt to drag myself out of her mouth to be sure."
            play sexsfx1 slide_out
            show kiara sixtynine pleasure happy
            "Luckily for me, Kiara seems to catch onto what I'm trying to do, and she soon releases me."
            "Pulling her head back, she sits patiently in front of me, waiting to see what comes next."
    return

label kiara_fuck_date_cunnilingus:
    "I can see the way that Kiara's looking hungrily at my naked body."
    "Or to be more precise, how she's eyeing up my cock right now!"
    "And, of course, that's only making it start to harden."
    "But I guess that I'm doing the exact same thing too."
    "Because my eyes keep being drawn back to the same spot on Kiara's body."
    "And if she's wanting my cock, I'm wanting her pussy just as badly."
    mike.say "Well, maybe I could..."
    mike.say "I dunno...give give you oral?"
    mike.say "You know, if it's not too much trouble?"
    "Before I said that I could see desire in Kiara's eyes."
    "But now they seem to burst with what can only be described as naked lust!"
    show kiara talkative
    if kiara.sub >= 25:
        kiara.say "Are you sure that's what you want?"
        kiara.say "Because if you are, then I am all yours!"
    elif kiara.sub < -25:
        kiara.say "So you want to get down on your knees and pleasure me?"
        kiara.say "How could I possibly say not to that?!?"
    else:
        kiara.say "[hero.name], are you serious?"
        kiara.say "I would love to have you lick my pussy!"
    show kiara flirt
    "Kiara smiles as she turns to walk the short distance to the bed."
    "And she doesn't even need to bother beckoning for me to follow her."
    "Because I hurry along, as if she has me on an invisible leash."
    hide kiara
    show kiara cowgirl
    with fade
    "Once there she crawls onto the mattress, turning over as she mounts it."
    "Then she plants herself down, spreading her thighs wide as she does so."
    "Kiara doesn't say a word, just leans back on her palms of her hands."
    "But again, she doesn't need to tell me a thing, or hint at what to do next."
    "And that's because by now I can see what's waiting for me between those legs."
    "Kiara's pussy is right there, exposed as she parts her thighs."
    "It's neat, beautiful to look at, and I can see it's already glistening in the light!"
    if kiara.sub >= 25:
        kiara.say "There you go, [hero.name]…"
        kiara.say "I'm all yours!"
    elif kiara.sub < -25:
        kiara.say "Now then, [hero.name]…"
        kiara.say "Are you going to take care of me like you promised?"
    else:
        kiara.say "What are you waiting for, [hero.name]?"
        kiara.say "Come over here and take it!"
    scene bg black
    show kiara oral
    with fade
    "I'm already lowering myself onto my knees as Kiara says all of this."
    "And it's just a lucky thing that the bed happens to be so close to me."
    "Because otherwise I'd have ended up crawling towards her on my hands and knees!"
    "I'm nodding my head the whole time that it takes me to reach her."
    "Mainly because I can't tear my eyes away from my prize."
    "And as I get ever closer to it, there's less chance of me being able to form actual words too."
    "Putting my hands on Kiara's thighs, I lower my head until it's between them."
    "As I get within touching distance, I also begin to catch the scent of it."
    "And I swear there's a hint of pepper and spice in there."
    "Though I couldn't say if it's natural or from Kiara's perfume."
    "Closing my eyes, I lean in the last few inches and begin to lick gently."
    "First I make sure to trace the outer edges, exploring the soft folds."
    "As soon as I do so the taste of her sends a tingle through me."
    "And at the same moment, Kiara moans and shudders too."
    "I feel her lie back, reclining onto the pillows behind her."
    "I raise her left leg as she does so, giving me better access."
    "And then I start to push my tongue further into her, going deeper each time."
    show kiara oral closed
    "Soon all of Kiara's poise and elegance are gone, replaced by sheer, unadulterated need."
    "The more I plunge my tongue into her, the more she seems to urge me on with her cries."
    "I can feel the sensation of her body quivering at my attentions, which thrills me in turn."
    "So I resolve to kiss the lips of her pussy just like I would those of her mouth."
    "For her part, Kiara can't help thrusting herself forwards, pushing herself onto me."
    "Which only serves to make my tongue reach deeper still."
    show kiara oral happy
    if kiara.sub >= 25:
        kiara.say "Oh...oh, [hero.name]…"
        kiara.say "You are going to...to make me..."
    elif kiara.sub < -25:
        kiara.say "Yes...[hero.name]…"
        kiara.say "Just like...just like that!"
    else:
        kiara.say "Y...yes..."
        kiara.say "Please...don't...stop!"
    show kiara oral pleasure hurt
    "Kiara's words are all I need to know that I'm on the right track."
    "And they also serve as a rallying call to make me redouble my efforts."
    "Pushing my tongue deeper than ever before, I try my best to make what comes next even more intense."
    show kiara oral pleasure ahegao with vpunch
    "Kiara reacts by almost collapsing backwards and onto the pile of pillows."
    with vpunch
    "At the same time I can feel her thighs clamping down on me to either side."
    with vpunch
    "But her cries as she cums are muffled by the way her legs are covering my ears."
    return

label kiara_fuck_date_cowgirl(sexperience_min):
    hide kiara
    show kiara naked normal at center, zoomAt(1.5, (640, 1040))
    with fade
    "Kiara stands in front of me, looking me straight in the eye."
    "There's something about her stance that's defiant, almost challenging."
    "As if she's just waiting to see if I have the balls to take charge."
    "But the very moment that I begin to open my mouth, I see her move."
    mike.say "Kiara..."
    mike.say "What are you..."
    "Before I can get the words out, she plants a hand flat on my chest."
    show kiara naked evil at center, zoomAt(1.25, (640, 880)) with vpunch
    "And she uses my surprise to be able to shove me over backwards."
    mike.say "WHOAH!"
    "I find myself tumbling backwards, arms flailing in a vain attempt to stop myself."
    "But I should have remembered that, from where she's standing, Kiara can see behind me."
    "As I soon find my fall interrupted by my back making contact with the mattress!"
    mike.say "What the..."
    scene bg black
    show kiara cowgirl out
    with vpunch
    "I maybe have time to bounce once before I feel something heavy land atop me."
    "Looking up, I'm not surprised to see Kiara staring down at me from above."
    "And she's not wasting any time either, as she quickly straddles my thighs."
    "Then, once she has me pinned down to the bed, she leans in closer still."
    show kiara cowgirl happy
    if kiara.sub >= 25:
        kiara.say "So, [hero.name], now you've got me…"
        kiara.say "Where would you like to put it?"
    elif kiara.sub < -25:
        kiara.say "Time to make up your mind, [hero.name], now you've got me…"
        kiara.say "Where is it going to go?"
        kiara.say "And make up your mind quickly, or I'll have to do it for you!"
    else:
        kiara.say "So, now you've got me, are you going to tell me where it's going?"
        kiara.say "Or are you going to surprise me?"
    "For a moment I think about pointing out that it seems to be Kiara that's got me."
    "But this doesn't seem like the time or the place to be getting pedantic."
    "So instead I devote myself to pondering the question that she's asked."
    "And it doesn't take me long to make up my mind."
    menu:
        "Fuck her pussy":
            "The slightest glimpse of Kiara's pussy is all that I need to know that I want it."
            "One glance at the neat pink folds between her thighs and I'm sold."
            "I can already feel my cock getting harder at the mere thought of it."
            "And all I need to do is pull her forwards just a little more..."
            call check_condom_usage (kiara) from _call_check_condom_usage_167
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show kiara cowgirl condom out
            show kiara cowgirl out
            with fade
            "Kiara looks down at me, fully knowing that I'm ready to go."
            "And I can see anticipation in her eyes as she does so."
            "Almost like she knows exactly how this thing is going to go."
            "And she's waiting to see what kind of an effect she'll have on me."
            "The truth is that she's probably right to be looking down on me like that."
            "Because I can't remember the last time I saw something that turned me on as much."
            "Every inch of Kiara's beautiful body is hanging over me, there for the taking."
            "But for some reason I feel myself pause, like I can't quite believe it."
            "That's when she reaches down with one hand, taking hold of my right wrist."
            "I offer no resistance as Kiara runs it over her flat belly and then up to her left breast."
            "All of my attention is focussed on what she's doing, that and beginning to squeeze what's in the palm of my hand."
            "And so I'm taken totally by surprised when Kiara's other hand reaches down to grab the shaft of my cock."
            mike.say "Urgh..."
            mike.say "Kiara..."
            mike.say "Please...be gentle?"
            "My pleas seem to amuse Kiara, a wicked smile spreading across her face."
            "But she at least bothers to nod curtly as she begins to stroke me."
            "At the same time she shuffles herself forwards, angling her crotch over mine."
            "And then I feel her begin to rub my cock against the lips of her pussy."
            "By now there's no way that I can manage to form a single coherent word."
            "The sensations that she's sending through my body are just too much."
            "And so the best I can do is let my head fall back onto the bed."
            "That and surrender myself to Kiara, letting her have her way with me."
            "In that position of almost total surrender, I watch as she works diligently."
            "Moving her body up and down atop me, so that her lips kiss the shaft of my cock."
            "I swear that with each pass she makes I can feel her pussy begin to relax."
            "And each time she lowers herself, I almost hold my breath, waiting for the moment when it happens."
            "But anticipation can't hope to compare to the actual reality."
            show kiara cowgirl vaginal -out at startle(0.05,-10)
            "So when those lips finally part, what I feel in the instant blows everything before it away."
            "My eye go wide and my mouth drops open, as if I'm letting out a silent cry."
            "At the same time Kiara moans, pushing down so that my cock is forced into her."
            "But the moan that she lets out isn't one of helpless surrender like mine."
            "Instead it sounds to me more like a triumphant cry of victory."
            show kiara cowgirl at startle(0.07,-15)
            play sexsfx1 fuck_calm loop
            "And it's not like Kiara stops moving once she's got me inside of her, oh no."
            "As soon as I'm all the way into her, I see her muscles tense in anticipation."
            show kiara cowgirl at startle(0.07,-15)
            pause 0.2
            show kiara cowgirl at startle(0.07,-15)
            "Then she starts to move again, this time up and down in a careful rhythm."
            "And before I know it, she's riding me as skilfully as any jockey I ever saw in the saddle!"
            "But let me tell you, no horse ever got as much pleasure from being ridden as I am right now."
            show kiara cowgirl at startle(0.07,-15)
            pause 0.2
            show kiara cowgirl at startle(0.07,-15)
            "Kiara's using every ounce of her strength to ride my cock, and it feels incredible."
            "Pinned beneath her, I do all that I can to move in sympathy with her body."
            "Trying to heighten the effect that she's having on me and double the pleasure for us both."









            "I shake my head to focus my thoughts, doing the best I can to keep my mind on the task at hand."
            show kiara cowgirl at startle(0.07,-15)
            pause 0.2
            show kiara cowgirl at startle(0.07,-15)
            "Soon enough we seem to reach a peak, to be in perfect balance with each other."
            "And from there I feel like I've finally climbed to the peak of a metaphorical mountain."
            "But the problem it that from there, we're soon tumbling down the other side of it!"
            play sexsfx1 fuck_moderate loop
            show kiara cowgirl at startle(0.05,-10)
            pause 0.2
            show kiara cowgirl at startle(0.05,-10)
            "Out momentum just seems to increase, as we go ever faster and harder."
            "Kiara seems to be holding onto me for dear life, pinning me to the bed."
            "At the same time I'm desperately pushing upwards, gripping her tightly."




            play sexsfx1 fuck_sprint loop
            show kiara cowgirl at startle(0.04,-10)
            pause 0.15
            show kiara cowgirl at startle(0.04,-10)
            "Knowing that any moment one of us is going to be pushed over the edge."
            "In the end it's Kiara that succumbs first, muscles tensing and squeezing me hard."
            show kiara cowgirl at startle(0.04,-10)
            pause 0.15
            show kiara cowgirl at startle(0.04,-10)
            "But the sensation is too much for me to be able to resist, and I feel myself losing it too."
            call cum_reaction (kiara, 'vaginal', sexperience_min) from _call_cum_reaction_301
            if _return == "vaginal_condom":
                "Safe in the knowledge that we took precautions and used a condom, I choose to keep going."
                with vpunch
                "Putting all of my energies into one last effort to please Kiara as I cum myself."
                play sexsfx1 final_thrust
                show kiara cowgirl pleasure ahegao with vpunch
                "This means that I shoot my load while I'm as deep inside of her as it's possible to be."
                with vpunch
                "Making one last thrust as I let go and fill her completely, cum seeping out around me."
            elif _return in ["vaginal_inside_happy", "vaginal_inside_mad"]:
                "Faced with the choice of pulling out or keeping going, I choose to keep going."
                with vpunch
                "Putting all of my energies into one last effort to please Kiara as I cum myself."
                $ kiara.impregnate()
                play sexsfx1 final_thrust
                show kiara cowgirl pleasure ahegao cum with vpunch
                "This means that I shoot my load while I'm as deep inside of her as it's possible to be."
                with vpunch
                "Making one last thrust as I let go and fill her completely, cum seeping out around me."
            elif _return == "vaginal_inside_pregnant":
                kiara.say "It's okay..."
                kiara.say "I'm pregnant - remember?"
                "I'm thankful for the reminder from Kiara, but the size of her belly means I hardly needed it!"
                with vpunch
                "Putting all of my energies into one last effort to please Kiara as I cum myself."
                play sexsfx1 final_thrust
                show kiara cowgirl pleasure ahegao cum with vpunch
                "This means that I shoot my load while I'm as deep inside of her as it's possible to be."
                with vpunch
                "Making one last thrust as I let go and fill her completely, cum seeping out around me."
            elif _return == "vaginal_inside_pill":
                kiara.say "It's okay..."
                kiara.say "I'm on the Pill - remember?"
                "I'm thankful for the reminder from Kiara, because it leaves me free to do what comes naturally."
                with vpunch
                "Putting all of my energies into one last effort to please Kiara as I cum myself."
                play sexsfx1 final_thrust
                show kiara cowgirl pleasure ahegao cum with vpunch
                "This means that I shoot my load while I'm as deep inside of her as it's possible to be."
                with vpunch
                "Making one last thrust as I let go and fill her completely, cum seeping out around me."
            elif _return == "vaginal_outside":
                menu:
                    "Cum on her body":
                        "Remembering that we didn't bother to use any protection, I get ready to pull out before it's too late."
                        "And so I use the last of my energy to brace my hands against the mattress and slide backwards."
                        play sexsfx1 slide_out
                        show kiara cowgirl out
                        "Pulling myself all the way out of Kiara in one smooth, uninterrupted motion."
                        play sexsfx1 cum_outside
                        show kiara cowgirl out cum with vpunch
                        "Almost the same moment that my cock emerges from her, I feel myself starting to lose it."
                        show kiara cowgirl out bodycum
                        "Spattering her belly and thighs with warm, sticky droplets of cum."
                    "Cum on her face":
                        play sexsfx1 slide_out
                        show kiara cowgirl out -vaginal
                        "And then I pull her to her feet too, making her kneel on the floor in front of me."
                        "To her credit, Kiara seems to know exactly what's happening, and plays along."
                        hide kiara
                        show kiara bj happy
                        with fade
                        "She kneels in front of me, patiently waiting for the inevitable to happen."
                        "Wanting to do more than just cum inside or over Kiara, I pull out in one smooth motion."
                        play sexsfx1 cum_outside
                        show kiara bj cum closed hurt with hpunch
                        pause 0.3
                        show kiara bj bodycum pleasure happy
                        "And when it does, she smiles as I paint her face with lines of sticky, white cum."
                    "Cum in her mouth":
                        play sexsfx1 slide_out
                        show kiara cowgirl out -vaginal
                        "Wanting to do more than just cum inside or over Kiara, I pull out in one smooth motion."
                        "And then I pull her to her feet too, making her kneel on the floor in front of me."
                        "To her credit, Kiara seems to know exactly what's happening, and plays along."
                        hide kiara
                        show kiara bj happy
                        with fade
                        "She kneels in front of me and then opens her mouth as I take a step forwards."
                        play sexsfx1 bj_gulp
                        show kiara bj blowjob cum with hpunch
                        "Taking my cock into her mouth, Kiara swallows everything that I have to give."
                        "Making sure not to lose a drop as she drinks the whole thing down."
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "The slightest glimpse of Kiara's butt is all that I need to know that I want it."
            "One glance at the perfectly rounded curve of her buttocks and I'm sold."
            "I can already feel my cock getting harder at the mere thought of it."
            "And all I need to do is pull her forwards just a little more..."
            show kiara cowgirl out with fade
            "Kiara looks down at me, fully knowing that I'm ready to go."
            "And I can see anticipation in her eyes as she does so."
            "Almost like she knows exactly how this thing is going to go."
            "And she's waiting to see what kind of an effect she'll have on me."
            "The truth is that she's probably right to be looking down on me like that."
            "Because I can't remember the last time I saw something that turned me on as much."
            "Every inch of Kiara's beautiful body is hanging over me, there for the taking."
            "But for some reason I feel myself pause, like I can't quite believe it."
            "That's when she reaches down with one hand, taking hold of my right wrist."
            "I offer no resistance as Kiara runs it over her flat belly and then up to her left breast."
            "All of my attention is focussed on what she's doing, that and beginning to squeeze what's in the palm of my hand."
            "And so I'm taken totally by surprised when Kiara's other hand reaches down to grab the shaft of my cock."
            mike.say "Urgh..."
            mike.say "Kiara..."
            mike.say "Please...put it in your butt?"
            "My pleas seem to amuse Kiara, a wicked smile spreading across her face."
            "But she at least bothers to nod curtly as she begins to stroke me."
            "At the same time she shuffles herself forwards, angling her crotch over mine."
            "And then I feel her begin to rub my cock between her buttocks."
            "By now there's no way that I can manage to form a single coherent word."
            "The sensations that she's sending through my body are just too much."
            "And so the best I can do is let my head fall back onto the bed."
            "That and surrender myself to Kiara, letting her have her way with me."
            "In that position of almost total surrender, I watch as she works diligently."
            "Moving her body up and down atop me, so that her buttocks the shaft of my cock."
            "I swear that with each pass she makes I can feel her hole begin to relax."
            "And each time she lowers herself, I almost hold my breath, waiting for the moment when it happens."
            "But anticipation can't hope to compare to the actual reality."
            play sexsfx1 slide_in
            show kiara cowgirl vaginal -out closed hurt at startle(0.05,-10)
            "So when those lips finally part, what I feel in the instant blows everything before it away."
            "My eye go wide and my mouth drops open, as if I'm letting out a silent cry."
            show kiara cowgirl pleasure happy
            "At the same time Kiara moans, pushing down so that my cock is forced into her."
            "But the moan that she lets out isn't one of helpless surrender like mine."
            "Instead it sounds to me more like a triumphant cry of victory."
            show kiara cowgirl at startle(0.07,-15)
            play sexsfx1 fuck_calm loop
            "And it's not like Kiara stops moving once she's got me inside of her, oh no."
            "As soon as I'm all the way into her, I see her muscles tense in anticipation."
            show kiara cowgirl at startle(0.07,-15)
            pause 0.2
            show kiara cowgirl at startle(0.07,-15)
            "Then she starts to move again, this time up and down in a careful rhythm."
            "And before I know it, she's riding me as skilfully as any jockey I ever saw in the saddle!"
            "But let me tell you, no horse ever got as much pleasure from being ridden as I am right now."
            show kiara cowgirl at startle(0.07,-15)
            pause 0.2
            show kiara cowgirl at startle(0.07,-15)
            "Kiara's using every ounce of her strength to ride my cock, and it feels incredible."
            "Pinned beneath her, I do all that I can to move in sympathy with her body."
            "Trying to heighten the effect that she's having on me and double the pleasure for us both."









            "I shake my head to focus my thoughts, doing the best I can to keep my mind on the task at hand."
            show kiara cowgirl at startle(0.07,-15)
            pause 0.2
            show kiara cowgirl at startle(0.07,-15)
            "Soon enough we seem to reach a peak, to be in perfect balance with each other."
            "And from there I feel like I've finally climbed to the peak of a metaphorical mountain."
            "But the problem it that from there, we're soon tumbling down the other side of it!"
            play sexsfx1 fuck_moderate loop
            show kiara cowgirl at startle(0.05,-10)
            pause 0.2
            show kiara cowgirl at startle(0.05,-10)
            "Out momentum just seems to increase, as we go ever faster and harder."
            "Kiara seems to be holding onto me for dear life, pinning me to the bed."
            "At the same time I'm desperately pushing upwards, gripping her tightly."




            play sexsfx1 fuck_sprint loop
            show kiara cowgirl at startle(0.04,-10)
            pause 0.15
            show kiara cowgirl at startle(0.04,-10)
            "Knowing that any moment one of us is going to be pushed over the edge."
            "In the end it's Kiara that succumbs first, muscles tensing and squeezing me hard."
            show kiara cowgirl at startle(0.04,-10)
            pause 0.15
            show kiara cowgirl at startle(0.04,-10)
            "But the sensation is too much for me to be able to resist, and I feel myself losing it too."
            call cum_reaction (kiara, 'anal', sexperience_min) from _call_cum_reaction_302
            if _return == "anal_inside":
                "Faced with the choice of pulling out or keeping going, I choose to keep going."
                with vpunch
                "Putting all of my energies into one last effort to please Kiara as I cum myself."
                play sexsfx1 cum_inside
                show kiara cowgirl pleasure ahegao with vpunch
                "This means that I shoot my load while I'm as deep inside of her ass as it's possible to be."
                with vpunch
                "Making one last thrust as I let go and fill her completely, cum seeping out around me."
            elif _return == "anal_outside":
                menu:
                    "Cum on her body":
                        "For some reason I feel the need to mark my territory, to christen Kiara with my own juices."
                        "And so I use the last of my energy to brace my hands against the mattress and slide backwards."
                        play sexsfx1 pop_out
                        show kiara cowgirl out -vaginal
                        "Pulling myself all the way out of Kiara's ass in one smooth, uninterrupted motion."
                        play sexsfx1 cum_outside
                        show kiara cowgirl cum with vpunch
                        "Almost the same moment that my cock emerges from her, I feel myself starting to lose it."
                        show kiara cowgirl bodycum
                        "Spattering her belly and thighs with warm, sticky droplets of cum."
                    "Cum on her face":
                        play sexsfx1 pop_out
                        show kiara cowgirl out -vaginal
                        "Wanting to do more than just cum inside or over Kiara, I pull out of her ass in one smooth motion."
                        "And then I pull her to her feet too, making her kneel on the floor in front of me."
                        "To her credit, Kiara seems to know exactly what's happening, and plays along."
                        hide kiara
                        show kiara bj happy
                        with fade
                        "She kneels in front of me, patiently waiting for the inevitable to happen."
                        play sexsfx1 cum_outside
                        show kiara bj cum closed hurt with hpunch
                        pause 0.3
                        show kiara bj bodycum pleasure happy
                        "And when it does, she smiles as I paint her face with lines of sticky, white cum."
                    "Cum in her mouth":
                        play sexsfx1 pop_out
                        show kiara cowgirl out -vaginal
                        "Wanting to do more than just cum inside or over Kiara, I pull out of her ass in one smooth motion."
                        "And then I pull her to her feet too, making her kneel on the floor in front of me."
                        "To her credit, Kiara seems to know exactly what's happening, and plays along."
                        hide kiara
                        show kiara bj happy
                        with fade
                        "She kneels in front of me and then opens her mouth as I take a step forwards."
                        play sexsfx1 bj_gulp
                        show kiara bj blowjob cum with hpunch
                        "Taking my cock into her mouth, Kiara swallows everything that I have to give."
                        "Making sure not to lose a drop as she drinks the whole thing down."
    return

label kiara_fuck_date_missionary(sexperience_min):
    hide kiara
    show kiara naked normal at center, zoomAt(1.5, (640, 1040))
    with fade
    "Kiara plants her hands firmly on my hips, getting a good grip on my waist."
    "And then the walks backwards, pulling me with her the short distance to the bed."
    "I follow without question, looking her in the eye the whole time."
    scene bg black
    show kiara missionary out
    with fade
    "Even when she crawls onto the bed, I still keep it up, climbing on after her."
    "At the same time Kiara's lowering herself onto her back as she goes."
    "This means that I'm doing the same thing too, as if I'm magnetically drawn towards her."
    "As our bodies come closer together, Kiara's hands move upwards from my waist."
    "Soon enough they're moving all over my back and chest, stroking and caressing."
    "And I'm returning the favour with my lips, planting kisses here and there as I go."
    "But when I reach her head and make to kiss her on the lips, Kiara holds up a single finger."
    "She presses this against my own pursed lips, stopping me while she asks a question."
    if kiara.sub >= 25:
        kiara.say "So, [hero.name]…"
        kiara.say "Where would you like to put it?"
    elif kiara.sub < -25:
        kiara.say "Time to make up your mind, [hero.name]…"
        kiara.say "Where is it going to go?"
        kiara.say "And make up your mind quickly, or I'll have to do it for you!"
    else:
        kiara.say "So, are you going to tell me where it's going?"
        kiara.say "Or are you going to surprise me?"
    "Kiara's question makes me stop in my tracks and think for a moment."
    "But once I do that, it takes me no more than a couple of seconds to decide."
    menu:
        "Fuck her pussy":
            "The slightest glimpse of Kiara's pussy is all that I need to know."
            "One glance at the neat pink folds between her thighs and I'm sold."
            "I can already feel my cock getting harder at the thought of it."
            "And all I need to do is lower myself down just a little more..."
            call check_condom_usage (kiara) from _call_check_condom_usage_168
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show kiara missionary condom out
            show kiara missionary out
            with fade
            "Kiara seems to be every bit as much into the idea as I am."
            "Because she doesn't hesitate to open her legs wide for me."
            "Hell, she even reaches up and grabs hold of her own ankles."
            "Which means that I can practically climb atop her!"
            "As soon as the tip of my cock touches the lips of her pussy, I know that I made the right choice."
            "I can almost feel the need inside of Kiara as it builds with every passing second."
            "And the way it begins to slide and slip lets me know that she's more than ready for me."
            "In fact the sensation of my cock against her is so pleasant that it's totally distracting."
            "My body just seems to go into an automatic loop as the pleasure occupies my mind."
            "And so I'm taken by surprise when there's suddenly no resistance whatsoever."
            "I was prepared for the efforts to get inside lasting longer, to have to work harder."
            "Which wouldn't have been a bad thing, as I don't mind working for my reward."
            "But it seems that Kiara's keener to get things moving than I thought."
            "Suddenly I'm snapped back to reality as I feel myself sinking into her."
            show kiara missionary -out vaginal at startle(0.05,-10)
            "The lips of Kiara's pussy part with almost no effort on my part."
            "And now all of my weight is behind me too, ensuring that I go all the way."
            "In one smooth motion I fill Kiara, not stopping until I can go no further."
            "She's nodding the whole time, silently urging me on."
            "But she doesn't say a word as she's also biting her lip."
            "Almost as if the pleasure that she's feeling is simply too much."
            "Of course by now my body is on auto-pilot, and I begin to move inside of her."
            show kiara missionary at startle(0.07,-15)
            play sexsfx1 fuck_calm loop
            "Slowly at first, I go back and forth, moving in and out of Kiara."
            "But there's no way I can keep myself from picking up the pace."
            play sexsfx1 fuck_moderate loop
            show kiara missionary pleasure at startle(0.05,-10)
            pause 0.2
            show kiara missionary at startle(0.05,-10)
            "And soon enough I'm going as fast as I can, unable to even think of slowing down."
            "Kiara responds in kind, taking everything that I have to give."
            "All the while the nodding of her head continues."
            show kiara missionary at startle(0.05,-10)
            pause 0.2
            show kiara missionary at startle(0.05,-10)
            "Though I can't be sure if it's still a conscious gesture."
            "Or else her head is simply nodding from the motion of her entire body."










            "I shake my own head, doing the best I can to keep my mind on the task at hand."
            play sexsfx1 fuck_sprint loop
            show kiara missionary at startle(0.04,-10)
            pause 0.15
            show kiara missionary at startle(0.04,-10)
            "Kiara has spent most of her time lying still beneath me so far."
            "But now I feel the sensation of her legs closing around me."
            "Looking up I see her arms doing the same, so her hands pull at her ankles."
            show kiara missionary at startle(0.04,-10)
            pause 0.15
            show kiara missionary at startle(0.04,-10)
            "All in all, it feels like I'm being cocooned by her limbs."
            "At the same time there's a squeezing around my cock that makes my eyes bulge in their sockets."
            show kiara missionary closed hurt
            "And one glance down at Kiara beneath me is all that I need to be able to guess the reason why."
            "Her eyes are closed and her face is twisted into an expression of helpless ecstasy."
            "She's right on the verge of cumming, and it happens as I'm gazing down at her."




            "I'm literally watching her orgasm take hold in real time."
            "Kiara lets out a long moan, almost a keening of pure release as she's swept away."
            "And the effect is so powerful that I know I'm going to be carried along with her."
            "So I have no more than a few seconds to decide where I want to be when it happens."
            call cum_reaction (kiara, 'vaginal', sexperience_min) from _call_cum_reaction_303
            if _return == "vaginal_condom":
                "Safe in the knowledge that we took precautions and used a condom, I choose to keep going."
                with vpunch
                "Putting all of my energies into one last effort to please Kiara as I cum myself."
                play sexsfx1 final_thrust
                show kiara cowgirl pleasure ahegao with vpunch
                "This means that I shoot my load while I'm as deep inside of her as it's possible to be."
                with vpunch
                "Making one last thrust as I let go and fill her completely, cum seeping out around me."
            elif _return in ["vaginal_inside_happy", "vaginal_inside_mad"]:
                "Faced with the choice of pulling out or keeping going, I choose to keep going."
                with vpunch
                "Putting all of my energies into one last effort to please Kiara as I cum myself."
                $ kiara.impregnate()
                play sexsfx1 final_thrust
                show kiara missionary pleasure ahegao cum with vpunch
                "This means that I shoot my load while I'm as deep inside of her as it's possible to be."
                with vpunch
                "Making one last thrust as I let go and fill her completely, cum seeping out around me."
            elif _return == "vaginal_inside_pregnant":
                kiara.say "It's okay..."
                kiara.say "I'm pregnant - remember?"
                "I'm thankful for the reminder from Kiara, but the size of her belly means I hardly needed it!"
                with vpunch
                "Putting all of my energies into one last effort to please Kiara as I cum myself."
                play sexsfx1 final_thrust
                show kiara missionary pleasure ahegao cum with vpunch
                "This means that I shoot my load while I'm as deep inside of her as it's possible to be."
                with vpunch
                "Making one last thrust as I let go and fill her completely, cum seeping out around me."
            elif _return == "vaginal_inside_pill":
                kiara.say "It's okay..."
                kiara.say "I'm on the Pill - remember?"
                "I'm thankful for the reminder from Kiara, because it leaves me free to do what comes naturally."
                with vpunch
                "Putting all of my energies into one last effort to please Kiara as I cum myself."
                play sexsfx1 final_thrust
                show kiara missionary pleasure ahegao cum with vpunch
                "This means that I shoot my load while I'm as deep inside of her as it's possible to be."
                with vpunch
                "Making one last thrust as I let go and fill her completely, cum seeping out around me."
            elif _return == "vaginal_outside":
                menu:
                    "Cum on her body":
                        "Remembering that we didn't bother to use any protection, I get ready to pull out before it's too late."
                        "And so I use the last of my energy to brace my hands against the mattress and slide backwards."
                        play sexsfx1 slide_out
                        show kiara missionary out -vaginal
                        "Pulling myself all the way out of Kiara in one smooth, uninterrupted motion."
                        play sexsfx1 cum_outside
                        show kiara missionary cum with vpunch
                        "Almost the same moment that my cock emerges from her, I feel myself starting to lose it."
                        show kiara missionary bodycum
                        "Spattering her belly and thighs with warm, sticky droplets of cum."
                    "Cum on her face":
                        "Wanting to do more than just cum inside or over Kiara, I pull out in one smooth motion."
                        play sexsfx1 slide_out
                        show kiara missionary out -vaginal
                        "And then I pull her to her feet too, making her kneel on the floor in front of me."
                        "To her credit, Kiara seems to know exactly what's happening, and plays along."
                        hide kiara
                        show kiara bj happy
                        with fade
                        "She kneels in front of me, patiently waiting for the inevitable to happen."
                        play sexsfx1 cum_outside
                        show kiara bj cum closed hurt with hpunch
                        pause 0.3
                        show kiara bj bodycum pleasure happy
                        "And when it does, she smiles as I paint her face with lines of sticky, white cum."
                    "Cum in her mouth":
                        play sexsfx1 slide_out
                        show kiara missionary out -vaginal
                        "Wanting to do more than just cum inside or over Kiara, I pull out in one smooth motion."
                        "And then I pull her to her feet too, making her kneel on the floor in front of me."
                        "To her credit, Kiara seems to know exactly what's happening, and plays along."
                        hide kiara
                        show kiara bj happy
                        with fade
                        "She kneels in front of me and then opens her mouth as I take a step forwards."
                        play sexsfx1 bj_gulp
                        show kiara bj blowjob cum with hpunch
                        "Taking my cock into her mouth, Kiara swallows everything that I have to give."
                        "Making sure not to lose a drop as she drinks the whole thing down."
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "The slightest glimpse of Kiara's cheeks down there is all I is all that I need to know."
            "One glance at the rounded shape of her buttoks and I'm sold."
            "I can already feel my cock getting harder at the thought of it."
            "And all I need to do is lower myself down just a little more..."
            show kiara missionary out with fade
            "Kiara seems to be every bit as much into the idea as I am."
            "Because she doesn't hesitate to open her legs wide for me."
            "Hell, she even reaches up and grabs hold of her own ankles."
            "Which means that I can practically climb atop her!"
            "As soon as the tip of my cock touches the edge of her hole, I know that I made the right choice."
            "I can almost feel the need inside of Kiara as it builds with every passing second."
            "And the way it begins to slide and slip lets me know that she's more than ready for me."
            "In fact the sensation of my cock against her is so pleasant that it's totally distracting."
            "My body just seems to go into an automatic loop as the pleasure occupies my mind."
            "And so I'm taken by surprise when there's suddenly no resistance whatsoever."
            "I was prepared for the efforts to get inside lasting longer, to have to work harder."
            "Which wouldn't have been a bad thing, as I don't mind working for my reward."
            "But it seems that Kiara's keener to get things moving than I thought."
            "Suddenly I'm snapped back to reality as I feel myself sinking into her."
            show kiara missionary -out vaginal closed hurt at startle(0.05,-10)
            "The muscles of Kiara's ass relax with almost no effort on my part."
            "And now all of my weight is behind me too, ensuring that I go all the way."
            "In one smooth motion I fill Kiara, not stopping until I can go no further."
            show kiara missionary pleasure happy
            "She's nodding the whole time, silently urging me on."
            "But she doesn't say a word as she's also biting her lip."
            "Almost as if the pleasure that she's feeling is simply too much."
            "Of course by now my body is on auto-pilot, and I begin to move inside of her."
            show kiara missionary at startle(0.07,-15)
            play sexsfx1 fuck_calm loop
            "Slowly at first, I go back and forth, moving in and out of Kiara."
            "But there's no way I can keep myself from picking up the pace."
            play sexsfx1 fuck_moderate loop
            show kiara missionary pleasure at startle(0.05,-10)
            pause 0.2
            show kiara missionary at startle(0.05,-10)
            "And soon enough I'm going as fast as I can, unable to even think of slowing down."
            "Kiara responds in kind, taking everything that I have to give."
            "All the while the nodding of her head continues."
            show kiara missionary at startle(0.05,-10)
            pause 0.2
            show kiara missionary at startle(0.05,-10)
            "Though I can't be sure if it's still a conscious gesture."
            "Or else her head is simply nodding from the motion of her entire body."










            "I shake my own head, doing the best I can to keep my mind on the task at hand."
            play sexsfx1 fuck_sprint loop
            show kiara missionary at startle(0.04,-10)
            pause 0.15
            show kiara missionary at startle(0.04,-10)
            "Kiara has spent most of her time lying still beneath me so far."
            "But now I feel the sensation of her legs closing around me."
            "Looking up I see her arms doing the same, so her hands pull at her ankles."
            show kiara missionary at startle(0.04,-10)
            pause 0.15
            show kiara missionary at startle(0.04,-10)
            "All in all, it feels like I'm being cocooned by her limbs."
            "At the same time there's a squeezing around my cock that makes my eyes bulge in their sockets."
            show kiara missionary closed hurt
            "And one glance down at Kiara beneath me is all that I need to be able to guess the reason why."
            "Her eyes are closed and her face is twisted into an expression of helpless ecstasy."
            "She's right on the verge of cuming, and it happens as I'm gazing down at her."




            "I'm literally watching her orgasm take hold in real time."
            "Kiara lets out a long moan, almost a keening of pure release as she's swept away."
            "And the effect is so powerful that I know I'm going to be carried along with her."
            "So I have no more than a few seconds to decide where I want to be when it happens."
            call cum_reaction (kiara, 'anal', sexperience_min) from _call_cum_reaction_304
            if _return == "anal_inside":
                "Faced with the choice of pulling out or keeping going, I choose to keep going."
                with vpunch
                "Putting all of my energies into one last effort to please Kiara as I cum myself."
                play sexsfx1 cum_inside
                show kiara missionary pleasure ahegao with vpunch
                "This means that I shoot my load while I'm as deep inside of her ass as it's possible to be."
                with vpunch
                "Making one last thrust as I let go and fill her completely, cum seeping out around me."
            elif _return == "anal_outside":
                menu:
                    "Cum on her body":
                        "For some reason I feel the need to mark my territory, to christen Kiara with my own juices."
                        "And so I use the last of my energy to brace my hands against the mattress and slide backwards."
                        play sexsfx1 pop_out
                        show kiara missionary out -vaginal
                        "Pulling myself all the way out of Kiara's ass in one smooth, uninterrupted motion."
                        play sexsfx1 cum_outside
                        show kiara missionary cum with vpunch
                        "Almost the same moment that my cock emerges from her, I feel myself starting to lose it."
                        show kiara cowgirl bodycum
                        "Spattering her belly and thighs with warm, sticky droplets of cum."
                    "Cum on her face":
                        play sexsfx1 pop_out
                        show kiara missionary out -vaginal
                        "Wanting to do more than just cum inside or over Kiara, I pull out of her ass in one smooth motion."
                        "And then I pull her to her feet too, making her kneel on the floor in front of me."
                        "To her credit, Kiara seems to know exactly what's happening, and plays along."
                        hide kiara
                        show kiara bj happy
                        with fade
                        "She kneels in front of me, patiently waiting for the inevitable to happen."
                        play sexsfx1 cum_outside
                        show kiara bj cum closed hurt with hpunch
                        pause 0.3
                        show kiara bj bodycum pleasure happy
                        "And when it does, she smiles as I paint her face with lines of sticky, white cum."
                    "Cum in her mouth":
                        play sexsfx1 pop_out
                        show kiara missionary out -vaginal
                        "Wanting to do more than just cum inside or over Kiara, I pull out of her ass in one smooth motion."
                        "And then I pull her to her feet too, making her kneel on the floor in front of me."
                        "To her credit, Kiara seems to know exactly what's happening, and plays along."
                        hide kiara
                        show kiara bj happy
                        with fade
                        "She kneels in front of me and then opens her mouth as I take a step forwards."
                        play sexsfx1 bj_gulp
                        show kiara bj blowjob cum with hpunch
                        "Taking my cock into her mouth, Kiara swallows everything that I have to give."
                        "Making sure not to lose a drop as she drinks the whole thing down."
    return

label kiara_fuck_date_standing(sexperience_min):
    hide kiara
    show kiara naked normal at center, zoomAt(1.5, (640, 1040))
    with fade
    "Kiara holds my eye as she closes the short space between us."
    "And she holds me almost spellbound as she does so."
    "Man, and I thought that she looked stunning with her clothes on!"
    "But now that she's standing in front of me totally naked..."
    "I give up, because there's no way I can describe how hot she is."
    "And from the smile on her face right now, she knows just what I'm thinking."
    "Kiara reaches up with one hand, placing it upon my chest."
    "The other she uses to stroke her breasts and perfectly flat stomach."
    show kiara talkative
    if kiara.sub >= 25:
        kiara.say "So, [hero.name], now you've got me…"
        kiara.say "Where would you like to put it?"
    elif kiara.sub < -25:
        kiara.say "Time to make up your mind, [hero.name], now you've got me…"
        kiara.say "Where is it going to go?"
        kiara.say "And make up your mind quickly, or I'll have to do it for you!"
    else:
        kiara.say "So, now you've got me, are you going to tell me where it's going?"
        kiara.say "Or are you going to surprise me?"
    show kiara flirt
    "There's no way that I can even think of getting Kiara onto the bed."
    "It doesn't matter that the thing is no more than a couple of feet away."
    "My poor, overloaded brain just can't handle the idea of moving that far."
    "Because the only thing it can process right now is my desire for her."
    hide kiara
    show kiara kiss naked
    with fade
    "And so I do the best I can to express myself by leaning in and kissing Kiara."
    "She readily acquiesces to the idea, knotting her hands behind my head."
    "Then she pulls me down to her level, kissing me full on the lips."
    "It lasts for a good long while too, tongues intertwining and exploring."
    scene bg black
    show kiara stand out
    with fade
    "And when it finally comes to a natural end, we both let out a sigh as we gasp for breath."
    kiara.say "Phew..."
    kiara.say "Okay, [hero.name]…"
    kiara.say "We do it right here, yes?"
    "I start nodding almost as soon as Kiara makes the suggestion."
    "But I should point out that she's also stroking my cock with one hand."
    "And I can already feel the sensation of it stiffening and starting to rise."
    menu:
        "Fuck her pussy":
            "Maybe it means that I'm obsessed with what's right in front of me."
            "But right now I can't think of anything apart from Kiara's sweet little pussy."
            "And I want to make straight for it, forgetting about absolutely everything else."
            call check_condom_usage (kiara) from _call_check_condom_usage_169
            if _return == False:
                return "leave_without_gain"
            if CONDOM:
                show kiara stand condom
            "Now that all the pieces are in place, I feel like we're ready to go."
            "And so I get ready to make the first move, to take the lead."
            "But it seems like Kiara has exactly the same thing in mind."
            "And she manages to beat me to the punch too."
            "Putting her hands on my shoulders, she leaps into the air."
            "And I'm forced to react on instinct, reaching out to catch her."
            "But when I do so, Kiara's jumped so high that my arms are actually under her thighs!"
            "Her legs come down on either side of me as her hands knot behind my head."
            "And my own hands end up on her shoulders as I do all I can to brace myself."
            mike.say "Whoa..."
            mike.say "Kiara..."
            mike.say "What are you doing?!?"
            kiara.say "Just hold on, [hero.name]…"
            kiara.say "And I promise you this will be worth the effort!"
            "As if to make good on her promise, Kiara lowers herself in my arms."
            "Which means that she pretty much comes down right on my cock."
            "The entire weight of her body is behind her as she does so."
            "And that's more than enough to make the inevitable begin to happen."
            "There's a few short moments of resistance, while Kiara's pussy doesn't get the memo."
            play sexsfx1 slide_in
            show kiara stand vaginal closed hurt at stepback(speed=0.1, h=-10, v=-10)
            "But soon enough I hear the sound of her beginning to moan, right into my ear."
            "And at the same time I can feel the sensation of her lips parting."
            "At first she slips down quite a way, taking almost half of it inside."
            "But then I tighten my hold on Kiara and her limbs stiffen too."
            "This means that we can slow things down and really start to enjoy ourselves."
            "And together we make sure the rest of her descent is controlled and satisfying."
            "By the time I'm as deep into her as I can go, Kiara's literally clinging onto me."
            play sexsfx1 fuck_calm loop
            show kiara stand vaginal pleasure happy at stepback(speed=0.1, h=-10, v=-10)
            "Which means that I'm the one who has to set the pace for what lies ahead."
            "I do that by gently lifting her upwards and then letting her fall again."
            "At the same time angling myself so that there's as much movement as possible."
            "This seems to do the trick, and soon enough I feel Kiara going limp in my arms."
            "In fact she seems content to simply hold on and let me have my way with her."
            play sexsfx1 fuck_moderate loop
            show kiara stand at stepback(speed=0.7, h=-10, v=-10)
            pause 0.2
            show kiara stand at stepback(speed=0.7, h=-10, v=-10)
            "Soon I settle into a rhythm that suits us both, and one that I can easily keep up."









            "And I focus all of my efforts on the task of staying vertical."
            show kiara stand at stepback(speed=0.7, h=-10, v=-10)
            pause 0.2
            show kiara stand closed at stepback(speed=0.7, h=-10, v=-10)
            "By now Kiara's bouncing up and down in my arms, totally lost to the moment."
            "Her eyes are closed and her mouth is kind of hanging open too."
            "All of which makes me think that she's off with the fairies."
            show kiara stand at stepback(speed=0.7, h=-10, v=-10)
            pause 0.2
            show kiara stand at stepback(speed=0.7, h=-10, v=-10)
            "But the only thing stopping me from being the same way is the need to concentrate."
            "On the one hand my brain is doing all it can to keep me on my feet."
            "Yet all the while I'm almost reeling from the pleasure that I'm feeling too."
            show kiara stand at stepback(speed=0.7, h=-10, v=-10)
            pause 0.2
            show kiara stand at stepback(speed=0.7, h=-10, v=-10)
            "And I can already feel the sensation of my climax creeping up on me."




            "Something that's made all the more pressing as I feel Kiara begin to cum herself."
            play sexsfx1 fuck_sprint loop
            show kiara stand at stepback(speed=0.5, h=-10, v=-10)
            pause 0.15
            show kiara stand at stepback(speed=0.5, h=-10, v=-10)
            "Curling up and clinging onto me more tightly than ever, she seems to tense her entire body."
            "Which also means that she's putting more pressure on my cock, deep inside of her."
            "And finally there's no way that I can hold on any longer."
            call cum_reaction (kiara, 'vaginal', sexperience_min) from _call_cum_reaction_305
            if _return == "vaginal_condom":
                "Safe in the knowledge that we took precautions and used a condom, I choose to keep going."
                play sexsfx1 final_thrust
                with vpunch
                "Putting all of my energies into one last effort to please Kiara as I cum myself."
                show kiara stand pleasure ahegao with vpunch
                "This means that I shoot my load while I'm as deep inside of her as it's possible to be."
                with vpunch
                "Making one last thrust as I let go and fill her completely, cum seeping out around me."
            elif _return in ["vaginal_inside_happy", "vaginal_inside_mad"]:
                "Faced with the choice of pulling out or keeping going, I choose to keep going."
                with vpunch
                "Putting all of my energies into one last effort to please Kiara as I cum myself."
                if _return == "vaginal_inside_happy":
                    $ claire.love += 5
                else:
                    $ claire.love -= 5
                $ kiara.impregnate()
                play sexsfx1 final_thrust
                show kiara stand pleasure ahegao cum with vpunch
                "This means that I shoot my load while I'm as deep inside of her as it's possible to be."
                with vpunch
                "Making one last thrust as I let go and fill her completely, cum seeping out around me."
            elif _return == "vaginal_inside_pregnant":
                kiara.say "It's okay..."
                kiara.say "I'm pregnant - remember?"
                "I'm thankful for the reminder from Kiara, but the size of her belly means I hardly needed it!"
                with vpunch
                "Putting all of my energies into one last effort to please Kiara as I cum myself."
                $ kiara.love += 3
                play sexsfx1 final_thrust
                show kiara stand pleasure ahegao cum with vpunch
                "This means that I shoot my load while I'm as deep inside of her as it's possible to be."
                with vpunch
                "Making one last thrust as I let go and fill her completely, cum seeping out around me."
            elif _return == "vaginal_inside_pill":
                kiara.say "It's okay..."
                kiara.say "I'm on the Pill - remember?"
                "I'm thankful for the reminder from Kiara, because it leaves me free to do what comes naturally."
                with vpunch
                "Putting all of my energies into one last effort to please Kiara as I cum myself."
                $ kiara.love += 2
                play sexsfx1 final_thrust
                show kiara stand pleasure ahegao cum with vpunch
                "This means that I shoot my load while I'm as deep inside of her as it's possible to be."
                with vpunch
                "Making one last thrust as I let go and fill her completely, cum seeping out around me."
            elif _return == "vaginal_outside":
                menu:
                    "Cum on her body":
                        "Remembering that we didn't bother to use any protection, I get ready to pull out before it's too late."
                        "And so I use the last of my energy to brace my hands against her and slide backwards."
                        play sexsfx1 slide_out
                        show kiara stand out
                        "Pulling myself all the way out of Kiara in one smooth, uninterrupted motion."
                        play sexsfx1 cum_outside
                        show kiara stand out cum with vpunch
                        "Almost the same moment that my cock emerges from her, I feel myself starting to lose it."
                        show kiara cowgirl out bodycum
                        "Spattering her belly and thighs with warm, sticky droplets of cum."
                    "Cum on her face":
                        play sexsfx1 slide_out
                        show kiara stand out
                        "Wanting to do more than just cum inside or over Kiara, I pull out in one smooth motion."
                        "And then I place her onto her feet too, making her kneel on the floor in front of me."
                        "To her credit, Kiara seems to know exactly what's happening, and plays along."
                        hide kiara
                        show kiara bj happy
                        with fade
                        "She kneels in front of me, patiently waiting for the inevitable to happen."
                        "Wanting to do more than just cum inside or over Kiara, I pull out in one smooth motion."
                        play sexsfx1 cum_outside
                        show kiara bj cum closed hurt with hpunch
                        pause 0.3
                        show kiara bj bodycum pleasure happy
                        "And when it does, she smiles as I paint her face with lines of sticky, white cum."
                    "Cum in her mouth":
                        play sexsfx1 slide_out
                        show kiara stand out
                        "Wanting to do more than just cum inside or over Kiara, I pull out in one smooth motion."
                        "And then I place her onto her feet too, making her kneel on the floor in front of me."
                        "To her credit, Kiara seems to know exactly what's happening, and plays along."
                        hide kiara
                        show kiara bj happy
                        with fade
                        "She kneels in front of me and then opens her mouth as I take a step forwards."
                        play sexsfx1 bj_gulp
                        show kiara bj blowjob cum with hpunch
                        "Taking my cock into her mouth, Kiara swallows everything that I have to give."
                        "Making sure not to lose a drop as she drinks the whole thing down."
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "Maybe it means that I'm obsessed with what's hidden from me."
            "But right now I can't think of anything apart from Kiara's sweet little ass."
            "And I want to make straight for it, forgetting about absolutely everything else."
            "Now that all the pieces are in place, I feel like we're ready to go."
            "And so I get ready to make the first move, to take the lead."
            "But it seems like Kiara has exactly the same thing in mind."
            "And she manages to beat me to the punch too."
            "Putting her hands on my shoulders, she leaps into the air."
            "And I'm forced to react on instinct, reaching out to catch her."
            "But when I do so, Kiara's jumped so high that my arms are actually under her thighs!"
            "Her legs come down on either side of me as her hands knot behind my head."
            "And my own hands end up on her shoulders as I do all I can to brace myself."
            mike.say "Whoa..."
            mike.say "Kiara..."
            mike.say "What are you doing?!?"
            kiara.say "Just hold on, [hero.name]…"
            kiara.say "And I promise you this will be worth the effort!"
            mike.say "The ass, Kiara..."
            mike.say "I'm aiming for the ass!"
            kiara.say "Don't worry, I've got this!"
            "As if to make good on her promise, Kiara lowers herself in my arms."
            "Which means that she pretty much comes down right on my cock."
            "The entire weight of her body is behind her as she does so."
            "And that's more than enough to make the inevitable begin to happen."
            "There's a few short moments of resistance, while Kiara's hole doesn't get the memo."
            play sexsfx1 slide_in
            show kiara stand anal closed hurt at stepback(speed=0.1, h=-10, v=-10)
            "But soon enough I hear the sound of her beginning to moan, right into my ear."
            "And at the same time I can feel the sensation of her muscles relaxing."
            "At first she slips down quite a way, taking almost half of it inside."
            "But then I tighten my hold on Kiara and her limbs stiffen too."
            "This means that we can slow things down and really start to enjoy ourselves."
            "And together we make sure the rest of her descent is controlled and satisfying."
            "By the time I'm as deep into her as I can go, Kiara's literally clinging onto me."
            play sexsfx1 fuck_calm loop
            show kiara stand pleasure happy at stepback(speed=0.1, h=-10, v=-10)
            "Which means that I'm the one who has to set the pace for what lies ahead."
            "I do that by gently lifting her upwards and then letting her fall again."
            "At the same time angling myself so that there's as much movement as possible."
            "This seems to do the trick, and soon enough I feel Kiara going limp in my arms."
            "In fact she seems content to simply hold on and let me have my way with her."
            play sexsfx1 fuck_moderate loop
            show kiara stand at stepback(speed=0.7, h=-10, v=-10)
            pause 0.2
            show kiara stand at stepback(speed=0.7, h=-10, v=-10)
            "Soon I settle into a rhythm that suits us both, and one that I can easily keep up."









            "And I focus all of my efforts on the task of staying vertical."
            show kiara stand at stepback(speed=0.7, h=-10, v=-10)
            pause 0.2
            show kiara stand closed at stepback(speed=0.7, h=-10, v=-10)
            "By now Kiara's bouncing up and down in my arms, totally lost to the moment."
            "Her eyes are closed and her mouth is kind of hanging open too."
            "All of which makes me think that she's off with the fairies."
            show kiara stand at stepback(speed=0.7, h=-10, v=-10)
            pause 0.2
            show kiara stand at stepback(speed=0.7, h=-10, v=-10)
            "But the only thing stopping me from being the same way is the need to concentrate."
            "On the one hand my brain is doing all it can to keep me on my feet."
            "Yet all the while I'm almost reeling from the pleasure that I'm feeling too."
            show kiara stand at stepback(speed=0.7, h=-10, v=-10)
            pause 0.2
            show kiara stand at stepback(speed=0.7, h=-10, v=-10)
            "And I can already feel the sensation of my climax creeping up on me."




            "Something that's made all the more pressing as I feel Kiara begin to cum herself."
            play sexsfx1 fuck_sprint loop
            pause 0.15
            show kiara stand at stepback(speed=0.5, h=-10, v=-10)
            "Curling up and clinging onto me more tightly than ever, she seems to tense her entire body."
            "Which also means that she's putting more pressure on my cock, deep inside of her."
            "And finally there's no way that I can hold on any longer."
            call cum_reaction (kiara, 'anal', sexperience_min) from _call_cum_reaction_306
            if _return == "anal_inside":
                "Faced with the choice of pulling out or keeping going, I choose to keep going."
                with vpunch
                "Putting all of my energies into one last effort to please Kiara as I cum myself."
                play sexsfx1 final_thrust
                show kiara stand pleasure ahegao cum with vpunch
                "This means that I shoot my load while I'm as deep inside of her as it's possible to be."
                with vpunch
                "Making one last thrust as I let go and fill her completely, cum seeping out around me."
            elif _return == "anal_outside":
                menu:
                    "Cum on her body":
                        "Feeling the need to mark my territory, I get ready to pull out before it's too late."
                        "And so I use the last of my energy to brace my hands against her and slide backwards."
                        play sexsfx1 pop_out
                        show kiara stand out
                        "Pulling myself all the way out of Kiara in one smooth, uninterrupted motion."
                        play sexsfx1 cum_outside
                        show kiara stand out cum with vpunch
                        "Almost the same moment that my cock emerges from her, I feel myself starting to lose it."
                        show kiara cowgirl out bodycum
                        "Spattering her belly and thighs with warm, sticky droplets of cum."
                    "Cum on her face":
                        play sexsfx1 pop_out
                        show kiara stand out
                        "Wanting to do more than just cum inside or over Kiara, I pull out in one smooth motion."
                        "And then I place her onto her feet too, making her kneel on the floor in front of me."
                        "To her credit, Kiara seems to know exactly what's happening, and plays along."
                        hide kiara
                        show kiara bj happy
                        with fade
                        "She kneels in front of me, patiently waiting for the inevitable to happen."
                        play sexsfx1 cum_outside
                        show kiara bj cum closed hurt with hpunch
                        pause 0.3
                        show kiara bj bodycum pleasure happy
                        "And when it does, she smiles as I paint her face with lines of sticky, white cum."
                    "Cum in her mouth":
                        play sexsfx1 pop_out
                        show kiara stand out
                        "Wanting to do more than just cum inside or over Kiara, I pull out in one smooth motion."
                        "And then I place her onto her feet too, making her kneel on the floor in front of me."
                        "To her credit, Kiara seems to know exactly what's happening, and plays along."
                        hide kiara
                        show kiara bj happy
                        with fade
                        "She kneels in front of me and then opens her mouth as I take a step forwards."
                        play sexsfx1 bj_gulp
                        show kiara bj blowjob cum with hpunch
                        "Taking my cock into her mouth, Kiara swallows everything that I have to give."
                        "Making sure not to lose a drop as she drinks the whole thing down."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
