init python:
    Event(**{
    "name": "sasha_masturbation_female",
    "priority": 500,
    "label": "sasha_masturbation_female",
    "duration": 1,
    "conditions": [
        IsHour(20, 3),
        HeroTarget(
            IsGender("female"),
            IsActivity("knock_bedroom3")),
        PersonTarget(sasha,
            Not(IsHidden()),
            IsRoom("bedroom3"),
            ),
        ],
    "chances": 25,
    "do_once": False,
    "once_day": True,
    })

    Activity(**{
    "name": "play_in_the_pool_with_sasha_female",
    "fun": 3,
    "icon": "playpool",
    "display_name": "Play with Sasha",
    "rooms": "pool",
    "conditions": [
        HeroTarget(IsGender("female")),
        IsSeason(0, 1),
        InInventory("swimsuit"),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(HasCheated()),
            MinStat("love", 10),
            ),
        PersonTarget(mike,
            Not(IsPresent())
            ),
        ],
    "once_day": True,
    "label": "sasha_play_pool_female",
    })

label sasha_masturbation_female:
    $ hero.cancel_activity()
    "Everyone walks around with their unconscious ear for interesting sounds turned on, don't they?"
    "I mean, I'm no different from the next girl when it comes to that kind of thing, not at all."
    "It's not like I snoop around the house the whole time, trying to find stuff to eavesdrop on - honestly, it's not!"
    "But I'm only human, and so when I hear something that intrigues me, how can I help turning an ear towards?"
    "That's natural curiosity, not any kind of perviness on my part...right?"
    "Anyway, that's how I end up looking in through the keyhole of Sasha's bedroom door."
    "I just happen to be wandering past, and I hear the most worrying sounds coming from inside of there."
    "Unable to guess just what's going on, and worried that poor Sasha might be in some kind of terrible pain, I rush over and put my eye to the keyhole."
    "Obviously I can't just knock on the door, as she might be perfectly fine in there, which would be embarrassing for the both of us."
    "No - much better to take a quick peak through the keyhole and make sure that she's actually in need of my help first."
    show sasha mast
    "At first, all I can see is Sasha herself, spread out on the bed, naked as the day she was born."
    "And bless her, the poor thing does seem to be in the throes of agony, casting her head about and moaning terribly."
    "But then I see the various phallic-shaped objects that are scattered on the bed around her."
    "And I begin to think that I might have made slight error in my guess at just what Sasha's been up to!"
    menu:
        "Stop watching":
            "Oh...my...god!"
            "She's masturbating, right there in front of me!"
            "Well...I suppose she's actually doing it in the privacy of her own room and behind a closed door..."
            "But still - she's masturbating!"
            "I feel instantly dirty and wretched as I tear my eye away from the keyhole, wishing that I'd never taken a peak to begin with."
            "Urgh...that image is going to be seared into my memory forever!"
            "I retreat to the safety and sanctuary of my own room, terrified that I might get the urge to copy what I've seen."
            "Or worse - that I might do it while still thinking about Sasha!"
            "Eww...why do I have to have such a dirty little bitch for a housemate?"
            hide sasha
            return
        "Keep watching" if hero.morality >= 0:
            "Oh...I see - she's not in THAT kind of pain!"
            "I guess that I should have noticed sooner just where Sasha's hands were."
            "And the fact that the toys on the bed are all visibly slick with a fresh application of lube."
            "Look, I know that this is the point where I should get all embarrassed and maybe even puritanically squeamish."
            "But there's always been that little bit of curiosity in the back of my mind when it comes to this kind of thing."
            "I might not be ready to give up on guys altogether, but the thought of watching another girl is kind of intriguing."
            "And it's not like I'm sneaking into some stranger's home to do it, right?"
            "Sasha and I have been living under the same roof for long enough by now."
            "Both of us have seen the other in our bikinis and running here and there in nothing but underwear."
            "So that unspoken barrier has already been broken..."
            "Anyway, it's not like I'm planning to make a habit of this!"
            "I'll watch this one time...just to see what happens."
        "Keep watching" if hero.morality < 0:
            "Oh wow - this is the chance of a lifetime!"
            "Sasha's actually pleasuring herself in there, right now."
            "And it looks like I might just have stumbled upon her as she's getting to the best part!"
            "I press my eye closer to the keyhole, straining to get the best view as possible."
            "As I do so, I can't help wondering if Sasha knows that someone could be watching her right now."
            "Perhaps she does, and that's all part of the thrill for her?"
            "I mean, if she wants to do something like that in privacy, why wouldn't she have kept the noise down?"
            "The walls around here aren't paper thin, but all the same, noise still carries."
            "Come to think of it, Sasha might have done everything in her power to tip off [mike.name] and me to the fact that she's doing this."
            "So it'd be pretty rude to ignore the show she's putting on for our benefit."
            "Not to mention prudish to be offended or outraged too!"
    if hero.morality >= -25:
        $ hero.morality -= 1
    "I don't think I've ever seen Sasha looking more worked up than she does right now."
    "Her normally pale, milky skin is suffused with a rosy, pink flush that's most intense in her cheeks."
    "And she's almost glistening with perspiration, as she pants with her tongue almost hanging out of her mouth the whole time."
    "By now she's laid on her belly, with her head against the pillows and her backside hoisted in the air."
    "I can see her little round breasts hanging down beneath her, swaying in time with the way she's moving."
    "Sasha has her left hand reaching around to part her buttocks and encourage the lips of her pussy to spread in sympathy."
    "The right hand is doing a pretty good job of parting them the rest of the way."
    "As well as rubbing frantically at the sensitive, exposed flesh within."
    "I can't honestly tell if the glistening slickness of Sasha's pussy is from the lube on the toys or a natural consequence of what she's doing to herself."
    "But either way, the intensity of the act is causing it to slide down the inside of her legs in rivulets."
    "It's a tough decision whether to watch Sasha's face as she pants and moans, or her hands as they make her do the same."
    "As my eyes dart between the two, I can feel myself getting hotter and more excited in sympathy."
    "I can already feel that tell-tale tingling between my own legs that's telling me I'm being turned on, whether I like it or not."
    "Unconsciously, my hand drifts towards the exact same spot, pushing under the waistband of my panties before I truly know what it's doing down there."
    "It's then that Sasha either saves me from myself or ruins my fun, based on your point of view."
    "She begins to literally push two of her fingers inside of herself, at the same time stroking at her clit with her thumb."
    "This is enough to start her on the inevitable path towards her climax, as her panting and moaning increase noticeably as she does so."
    "In sympathy, Sasha's body twitches and jerks like never before."
    "She arches her back, pushing her head into the pillows at the top of the bed."
    "Whether she does this for relief or in the hope of stifling her cries of pleasure, it seems to achieve neither."
    "Sasha cums then, collapsing into a sweaty heap of limbs as her muscles finally betray her and turn to water."
    "I watch as she writhes helplessly on the bed, wrapping herself in the bedclothes before finally curling up into a foetal position."
    "After that, Sasha doesn't move for the whole while that I stay there, still peeping through the keyhole."
    "She could be awake, sleeping or unconscious for all I can tell."
    "Soon enough I'm skulking off back to my own room, already wondering what I'm going to do about the head-full of images I now possess."
    "I might sleep in tomorrow morning, or at least wait until Sasha goes out for the day before showing my face."
    "I'm just not sure that I can stomach looking at her over the breakfast table for a while."
    hide sasha
    return

label sasha_play_pool_female:
    "I splash some water towards Sasha."
    sasha.say "Dimwit! You'll regret that!"
    show playing water pool sasha
    "After that she retaliates and we play in the water for a while..."
    sasha.say "That was fun!"
    bree.say "It sure was."
    $ sasha.love += 1
    $ sasha.flags.greeted = TemporaryFlag(True, 1)
    return

label sasha_greet_dialogues_female:
    if sasha.flags.mikeNickname:
        if game.hour < 6:
            bree.say "Hello my slave."
        elif game.hour < 12:
            bree.say "Good morning my slave."
        elif game.hour < 19:
            bree.say "Good afternoon my slave."
        else:
            bree.say "Good evening my slave."
    else:
        $ result = randint(1, 3)
        if result == 1:
            bree.say "Hello, Sasha."
        elif result == 2:
            bree.say "Hi."
        else:
            if game.hour < 6:
                bree.say "Hello."
            elif game.hour < 12:
                bree.say "Good morning Sasha."
            elif game.hour < 19:
                bree.say "Good afternoon Sasha."
            else:
                bree.say "Good evening Sasha."
    return

label sasha_greet_dialogues_2_female:

    return

label sasha_kiss_reaction_female:
    if sasha.lesbian < MIN_LES_GIRL_SEX:
        $ sasha.lesbian += 1
    return

label sasha_kiss_female:
    scene expression f"bg {game.room}"
    if sasha.love < 25 and not sasha.is_girlfriend and not game.active_date.score >= 75:
        show sasha
        "It can be hard to read Sasha from one moment to the next."
        "Sometimes she's upbeat and fun, other times she can be pretty dark and even angry."
        "But I know that I've misjudged her mood the moment that I make a move to kiss her."
        "And worse still, it seems that I've done so pretty badly too."
        "My reward for this is Sasha yanking her head away from me almost violently."
        "That and a look that could curdle milk from across a room, if not kill me outright!"
        sasha.say "Try that again and I'll cut your tits off."
        $ sasha.love -= 5
        $ sasha.sub -= 5
        hide sasha
    elif not sasha.flags.kiss:
        hide sasha
        $ sasha.love += 5
        call sasha_kiss_reaction_female from _call_sasha_kiss_reaction_female
        show sasha kiss
        "Sasha seems, for the most part, to work more on instinct than conscious thought."
        "And being around her, it kind of starts to rub off on you too."
        "That's why I hardly give it a second thought when I make to kiss her."
        "It's pure whim and a spur of the moment thing, no conscious thought involved."
        "I guess I'm lucky that she's taken by surprise in a pleasant way, and lets me do so without objection."
        "And when she leans into it and begins to return the kiss too, I know that my instincts were right on the mark."
        hide sasha kiss
        $ sasha.flags.kiss += 1
    else:
        hide sasha
        $ sasha.love += 2
        call sasha_kiss_reaction_female from _call_sasha_kiss_reaction_female_1
        show sasha kiss
        "Sasha's quick to steal a kiss where and whenever the mood takes her."
        "But once she's sneaked what was supposed to be a small show of affection, it never seems to be enough."
        "She almost always lingers longer than she intends, drawing it out for as long as possible."
        "In this way her kisses feel like they smoulder, enduring like the coals of a fire."
        "Even when the memory of the heat and the intensity that they began with have long since past."
        "And yes, her kisses are good enough to need me to get all poetic about them."
        hide sasha kiss
        $ sasha.flags.kiss += 1
    return

label sasha_ask_date_female:



    call sasha_ask_date_alone_female from _call_sasha_ask_date_alone_female
    return _return

label sasha_ask_date_alone_female:
    bree.say "Erm..."
    bree.say "Sasha..."
    bree.say "We've been getting on great recently, yeah?"
    bree.say "Having a good time together?"
    sasha.say "Yeah, [hero.name] - I guess so."
    bree.say "So...I was thinking..."
    bree.say "Would you like to go on a date?"
    bree.say "Like an official date?"
    if sasha.love < 50 or sasha.flags.nodate:
        sasha.say "Geez, [hero.name] - you took your time to get there!"
        sasha.say "And for the record, no - I don't think we should."
        sasha.say "If we call it a date, then we're giving it a name."
        sasha.say "And I don't think we're there yet!"
        $ date_choice = False
    else:
        sasha.say "Geez, [hero.name] - there's no need to beat around the bush like that!"
        sasha.say "Of course I would."
        sasha.say "I kinda thought we were already dating, you know?"
        sasha.say "But if you want to make it formal, then I'm cool with that."
        $ date_choice = True
    return date_choice

label sasha_pregnancy_congratulations:
    "Sasha's looking at me in a pretty odd way."
    "Like she just figured something out for the first time."
    "And I'm pretty sure it can only be one thing."
    show sasha annoyed
    sasha.say "[hero.name]..."
    sasha.say "When were you gonna tell me you were pregnant?"
    sasha.say "When your belly was huge?"
    show sasha normal
    sasha.say "Or when you actually had the kid?!?"
    bree.say "Of course I was going to tell you, Sasha!"
    bree.say "I was just waiting for the right time, that's all."
    "The admission seems to be enough to change Sasha's mood."
    show sasha happy
    "And now her expression is all happy and positive vibes."
    sasha.say "Sure, [hero.name], sure..."
    sasha.say "Anyway, congratulations!"
    sasha.say "You're going to be a mommy!"
    sasha.say "And I'm going to be 'Auntie Sasha'!"
    $ sasha.love += 1
    return

label sasha_propose_female:
    show sasha
    "Back when I was in college, I pretty much only had one rule."
    "Those are supposed to be the years when you get to be crazy, right?"
    "So anything was on the table as far as partying and having a good time."
    "All except for fooling around with your mates - room, house or whatever."
    "No matter who it was or what excuses they used, it always ended in a mess."
    "And I managed to keep to that rule for a good long time too."
    "That was until I happened to move into my current house and met Sasha."
    show sasha happy
    "I didn't see the danger at first, because we were just friends."
    "Normally I can feel an attraction to a guy or girl I'm compatible with."
    "But in Sasha's case, it just felt like we were going to be friends, nothing more."
    "Sure, we got on - but there was no spark that I could sense."
    "And I guess that was how she managed to sneak under my radar."
    "That meant that by the time I finally realised I had feelings for her, it was too late."
    "We started getting closer in a natural way."
    "At first we were just friends, hanging around the house together."
    "Then we started going down to the pub and swapping stories about our day."
    "Before I knew it we were going out to see movies together and all that stuff."
    "Basically doing all the stuff a couple would be doing without the extra benefits."
    "Eventually we finally came clean and admitted that we had feelings for each other."
    "And from there it just kept on getting better still."
    "We transitioned into dating in what felt like the blink of an eye."
    "But now I know that I can't just keep on the way we are."
    "I've grown to need Sasha like nobody else I've ever known."
    "And I need to do something to make sure that I don't lose her."
    "Which is why I'm getting ready to pop the question."
    "To ask her to marry me."
    "I know that I have to pick the exact right moment to do this."
    "And I feel like I planned out every single thing that I could."
    "But the truth is that I'm still terrified as I get ready to do it."
    "So in the end, all I can do is just take a deep breath and ask."
    bree.say "Sasha..."
    bree.say "I wanted to ask you something..."
    show sasha normal at center, zoomAt(1.5, (640, 1040))
    "As soon as the words are out of my mouth, I have Sasha's undivided attention."
    "She's looking at me like she knows that something is afoot."
    "That the question I mentioned isn't going to be something simple or mundane."
    show sasha annoyed
    sasha.say "Oh..."
    sasha.say "Okay!"
    sasha.say "I recognise that tone."
    show sasha joke
    sasha.say "Be honest, [hero.name] - is this going to be a scary kind of question?"
    "I can tell from the tone of Sasha's voice that she's being playful."
    "That she's only trying to defuse things with humour, like she always does."
    "But the question still somehow manages to send me into a spin."
    show sasha normal
    bree.say "Well..."
    bree.say "I suppose it is a scary question..."
    bree.say "But you shouldn't really be scared of it!"
    bree.say "Oh god...I don't know what I'm even saying..."
    bree.say "I'll just...just ask it!"
    bree.say "Sasha, will you...will you marry me?"
    if sasha.love < 195:

        "When it comes to giving me her answer, Sasha doesn't hesitate for a moment."
        show sasha happy at startle
        "She just shakes her head and starts laughing."
        show sasha joke
        sasha.say "Oh come on, [hero.name]..."
        sasha.say "You're joking, right?"
        sasha.say "You have to be!"
        show sasha happy at startle
        "I can feel myself going weak at the knees as Sasha laughs."
        "I tried as best I could to prepare myself for her saying no."
        "But I had no idea she'd be laughing at me too."
        show sasha normal
        bree.say "Erm..."
        bree.say "No, Sasha..."
        bree.say "I'm really not!"
        "Even as I'm admitting that I'm sincere, Sasha's reaction doesn't change."
        "Rather she actually doubles down on her previous stance."
        "Shaking her head to underline the fact that she really means it."
        show sasha joke
        sasha.say "We're a couple of hot, young bitches, [hero.name]."
        sasha.say "We're having a good time together - living the rock and roll lifestyle!"
        sasha.say "The last thing we should be thinking about is getting married."
        bree.say "I guess that's a no then, Sasha?"
        bree.say "If I heard you right?"
        sasha.say "You bet it's a no, [hero.name]!"
        sasha.say "Ask me again when we're both old and grey."
        "Much as it hurts to do so, I feel like all I can do is nod."
        "That and let the matter drop, regretting just how much I misread the situation."
        $ sasha.love -= 25
    else:

        "When it comes to giving me her answer, Sasha doesn't hesitate for a moment."
        show sasha happy at startle
        "She just nods her head and starts laughing."
        show sasha normal
        sasha.say "Get married?!?"
        sasha.say "That's a great idea, [hero.name]!"
        sasha.say "I'd have never thought of it myself."
        show sasha happy at startle
        "I can feel myself going weak at the knees as Sasha laughs."
        "I don't know why that's happening to me."
        "This is exactly what I wanted, the answer I was hoping for."
        "I thought I'd be jumping for joy, not shaking and nervous."
        bree.say "Are..."
        bree.say "Are you serious, Sasha?"
        bree.say "Did you just agree to marry me?"
        show sasha dazed
        "Sasha looks at me, clearly puzzled at the question."
        show sasha shy
        sasha.say "That's what I said, isn't it?"
        sasha.say "And you do want to marry me too?"
        sasha.say "Don't you?"
        show sasha blush at center, zoomAt(1.75, (640, 1190)) with vpunch
        "Rather than answering yes, I throw myself at Sasha."
        "And I have her wrapped in my arms before she knows what's happening."
        "I squeeze her, apparently with a strength I didn't know I had."
        "Because almost instantly, she starts struggling and wailing."
        sasha.say "[hero.name[0]]...[hero.name]!"
        sasha.say "You're...crushing...me!"
        show sasha shy
        "Hearing the desperation in her pleas, I loosen my hold."
        "And that done, we sink into a more genuine, gentle hug."
        "I know I have to let go sooner or later."
        "But right now I'm not letting anyone or anything take her away from me."
        $ sasha.set_fiance()
    hide sasha
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
