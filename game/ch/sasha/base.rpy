init python:
    Activity(**{
    "name": "watch_tv_with_sasha",
    "duration": 2,
    "fun": 3,
    "icon": "tv",
    "display_name": "Watch TV with Sasha",
    "max_girls": 1,
    "rooms": "livingroom",
    "conditions": [
        HeroTarget(MinStat("fun", 0)),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(HasCheated()),
            ),
        InvalidActivities(
            "watch_tv_with_everyone_male",
            "watch_tv_with_everyone_female",
            ),
        ],
    "label": "sasha_tv",
    })

    Activity(**{
    "name": "play_in_the_pool_with_sasha",
    "fun": 3,
    "icon": "playpool",
    "display_name": "Play with Sasha",
    "rooms": "pool",
    "conditions": [
        HeroTarget(IsGender("male")),
        IsSeason(0, 1),
        InInventory("swimsuit"),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(HasCheated()),
            MinStat("love", 10),
            ),
        PersonTarget(bree,
            Not(IsPresent())
            ),
        ],
    "once_day": True,
    "label": "sasha_play_pool",
    })

    Event(**{
    "name": "sasha_give_phone_number",
    "label": "give_phone_number",
    "girl": "sasha",
    "conditions": [
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(ContactKnown()),
            Not(IsActivity("sleep")),
            MinStat("love", 40),
            ),
        ],
    "chances": 25,
    "do_once": True,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "sasha_send_text",
    "label": "send_text",
    "priority": 100,
    "conditions": [
        IsHour(18, 19),
        HeroTarget(
            Not(OnDate()),
            IsActivity("None"),
            ),
        GameTarget(IsFlag("noTexting", False)),
        PersonTarget(sasha,
            Not(IsPresent()),
            Not(IsHidden()),
            ContactKnown(),
            Not(IsActivity("sleep")),
            Not(HasCheated()),
            MinStat("love", 50),
            ),
        ],
    "fun": 1,
    "girl": "sasha",
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "sasha_auto_greet",
    "label": "auto_greet",
    "priority": 100,
    "conditions": [
        HeroTarget(IsActivity("None")),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            IsFlag("greeted", False),
            Not(HasCheated()),
            MinStat("love", 50),
            ),
        ],
    "girl": "sasha",
    "chances": 50,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "sasha_auto_chat",
    "label": "auto_chat",
    "priority": 100,
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            Not(HasCheated()),
            MinStat("love", 50),
            ),
        ],
    "girl": "sasha",
    "chances": 10,
    "do_once": False,
    "once_day": True,
    })

    Event(**{
    "name": "sasha_are_you_sick",
    "label": "are_you_sick",
    "priority": 100,
    "girl": "sasha",
    "conditions": [
        HeroTarget(
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            Not(HasCheated()),
            ),
        ],
    "chances": (sasha, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "sasha_ask_out",
    "label": "ask_out",
    "priority": 100,
    "girl": "sasha",
    "conditions": [
        HeroTarget(Not(IsActivity("ask_date"))),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            Not(IsDatePlanned()),
            IsFlag("nodate", False),
            IsFlag("noaskout", False),
            Not(HasCheated()),
            MinStat("love", 100),
            ),
        ],
    "chances": 5,
    "do_once": False,
    "once_day": True,
    })

    Event(**{
    "name": "sasha_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "sasha",
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(sasha,
            IsPresent(),
            Not(IsHidden()),
            IsDateTime(),
            Not(HasCheated()),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

    Event(**{
    "name": "sasha_masturbation",
    "priority": 500,
    "label": "sasha_masturbation",
    "duration": 1,
    "fun": 2,
    "conditions": [
        IsHour(20, 3),
        HeroTarget(
            IsGender("male"),
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

    Event(**{
    "name": "sasha_tv_footjob",
    "label": "sasha_tv_footjob",
    "conditions": [
        IsTimeOfDay("evening"),
        HeroTarget(
            IsGender("male"),
            IsActivity("watch_tv"),
            IsRoom("livingroom"),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            HasRoomTag("home"),
            IsFlag("footjob", True),
            Not(IsActivity("sleep"))
            ),
        ],
    "duration": 1,
    "do_once": False,
    "once_month": True,
    })

label sasha_masturbation:
    $ hero.cancel_activity()
    "I'm not normally the kind of guy to be caught sneaking around for the sake of looking through a keyhole in the hope of being able to see something that's supposed to be strictly private."
    "But I'm also only human, and living with a couple of female housemates as cute as [bree.name] and Sasha means that there are times when I just can't help myself and the normal rules go straight out the window."
    "I don't wander around the house, waiting for such an opportunity to arise like a raving pervert."
    "They just seem to happen when you least expect it, and before I can reign myself in, I'm utterly, helplessly hooked."
    "This is a good example of what I mean - all I intended to do was walk back downstairs from the bathroom to my own room."
    "There was the addition of a stop in the kitchen to make a snack, but that was it."
    "It's just that halfway across the upstairs corridor; I hear a sound coming from behind the door to Sasha's bedroom."
    "So what, you might say - surely there are sounds coming from both of the girls' bedrooms most of the time they're in there?"
    "But you see, the thing is that these are the kind of intriguing sounds capable of stopping most people in their tracks."
    "I can hear deep, breathy series of sighs and moans that just keeps on getting louder and louder by the second."
    "Thinking that I'll just listen for a moment or two, long enough to confirm my suspicions as to what's going on in there, I walk as quietly as I can over to Sasha's door."
    "Before I can put my ear to the door, I see a chink of light emerging from the keyhole."
    "Again, I swear that I don't make a conscious decision to crouch down and squint through the hole - I just kind of find myself doing it."
    "But almost as soon as my eye adjusts to the light coming from the keyhole, any thought of the morality of what I'm doing is utterly forgotten."
    "Instead I find myself rooted to the spot, straining to get a better view of what I can see inside."
    show sasha mast
    "Upon the bed, laid on her stomach and with her backside up in the air is Sasha."
    "Utterly naked, her normally pale skin is flushed with a rosy shade of pink and positively glistening with perspiration."
    "Her head is turned so that I can make out the almost dazed expression she wears upon her face, and her mouth hangs open as she pants and moans."
    "As if I needed any further explanation of just what she's in the middle of doing to herself, I see sex-toys and lubed-up dildos strewn on the bed around her."
    "Sasha's left arm is stretched behind her, spreading her buttocks as wide as she can manage."
    "At the same time, the right is reaching under her belly and between her thighs, stroking fervently at her exposed pussy."
    "Even if I could get my head straight and think about how much of an intimate moment I'm peeping in on here, I don't think that I could tear myself away from the keyhole."
    "A part of me is disappointed to have missed the sight of Sasha getting those sex-toys into such a wonderfully filthy state."
    "But what could be better than actually getting to see the moment where she's stroking herself towards cumming with such obvious and audible passion?"
    "I watch with rapt attention as Sasha's fingers perform a dexterous dance over the lips and folds of her pussy."
    "Each touch seems to send shivers of pleasure shooting through her already aroused body, as if she were electrifying every inch of her skin."
    "Her task is made that much easier by the combination of lube and natural juices that I can see making her pussy as slick as can be."
    "Even the insides of her thighs seem to be as well-oiled, as rivulets of the same viscous fluid run down towards the bedclothes below."
    "Part of me is watching simply for the voyeuristic pleasure of seeing Sasha pleasure herself without fear of being disturbed."
    "But another is trying to make mental note of where she touches her pussy and how."
    "I'm not clueless when it comes to the ways in which most women like to be touched down there."
    "But tell me how often a guy gets a chance to see for himself just what turns a particular girl on?"
    "And think of the kudos that kind of knowledge could earn when put to good use with the girl herself..."
    "I watch as Sasha sinks two of her fingers slowly into her pussy, working them in and out, the speed increasing as she goes."
    "At the same time her thumb begins to press down on her clit, massaging the sensitive spot without mercy."
    "Just when I think that I can see what's finally going to bring her off, the fingers of the hand spreading her buttocks begin to move as well."
    show sasha mast ass
    "Reaching down, Sasha feels for her anus and then pushes a finger in so deep that it almost disappears from view up to the knuckle."
    "Working herself up with both holes at once, her cries seem to reach a peak in very short order."
    "My own cock has been hard almost since the moment that I started watching through the keyhole."
    "But now I can't keep from rubbing at it through my pants as I watch Sasha begin to cum at her own hand."
    "While the sight of what she's doing to herself is unbelievable, it's the expression on her face in that moment that really turns me on."
    "I guess I'm used to seeing her with a knowing grin or rolling her eyes at something dumb that came tumbling out of my mouth."
    "To see her features almost rendered insensible by the pleasure that she's experiencing is something I don't think I'll ever forget."
    "It's all that I can do to keep my hand from creeping into my own pants and following her example."
    "And that's something which almost becomes a battle as Sasha tosses her head back and starts to yelp at the arrival of her climax."
    "Laid there, with her ass in the air and her pussy exposed, she cums more like an animal in heat than a girl bringing herself off."
    "Sasha's eyes glaze over and her tongue begins to lol out of her mouth, the first hints of drool escaping from the corner of her mouth as it does so."
    "Finally, her legs begin to wobble from exhaustion, and she literally collapses onto the bedclothes, adding to the dark patches that she's already dropped beforehand."
    "Though her eyes are closed, I have no way of knowing if Sasha's asleep or just momentarily unable to summon the strength to open her eyes."
    "Not wanting to be caught out either way, I clamber to my feet and continue on my way back to my room, trying to hide my painful erection as I go."
    "All thought of visiting the kitchen for a snack is forgotten as I struggle to keep the images of what I've just witnessed fresh in my mind."
    "I wouldn't tell her as much, but Sasha's not going to be the only person that she managed to make cum in this house tonight."
    hide sasha
    return

label sasha_propose_male:
    show sasha
    "I really want to keep as far away from the traditional trappings of a proposal as I can for this, as I'm not exactly asking a traditional girl to marry me."
    "But despite the effort that I've gone to in order to avoid all of the cliches, it's more than worth it for the sake of making the proposal unique."
    "And that's because Sasha's pretty damn unique herself - and it's one of the things that makes me love her the way that I do..."
    "This means that I don't plan a huge gesture or go down on one knee in public with all eyes upon me."
    "Instead, I pick a quiet, intimate moment and pull out the ring without a great deal of ceremony."
    mike.say "Sasha, I have something I've been meaning to ask you..."
    if sasha.love < 195:
        show sasha sad
        "Much to my distress, the look of surprise in Sasha's eyes soon turns to agonised discomfort."
        sasha.say "Oh, [hero.name] - why'd you have to go and do a silly thing like that?"
        sasha.say "I was happy with things just the way they were."
        sasha.say "But this pretty much tells me you're not..."
        "I honestly don't know what to say."
        "How could I have misjudged the situation so badly?"
        $ sasha.love -= 25
        $ sasha.sub -= 25
    else:
        show sasha happy
        "At the sight of the ring, Sasha's eyes light up with what looks like genuine happiness."
        sasha.say "Oh, [hero.name] - are you asking me to marry you?!?"
        mike.say "Y...yes...yes I am, Sasha."
        mike.say "And...is that a yes?"
        sasha.say "Yes, of course it is!"
        sasha.say "I always dreamed of marrying my best friend - and now that dream's coming true!"
        $ sasha.set_fiance()
    hide sasha
    return

label sasha_cheated(action, cheat_npc=None):
    show sasha
    if sasha.is_sex_slave:
        $ sasha.sub += 1
    elif cheat_npc and Harem.together(sasha, cheat_npc):
        sasha.say "Give me back my toy!"
        show sasha kiss
        $ sasha.flags.kiss += 1
        "And without warning Sasha kisses me."
        $ sasha.love += 1
        hide sasha kiss
    else:
        show sasha wtf
        show fx anger
        if cheat_npc:
            $ sasha.flags.cheatedby = cheat_npc.id
        $ loss = 5
        if sasha.flags.girlfriend or sasha.flags.fiance:
            $ loss += 5
        $ sasha.love -= loss
        sasha.say "What the fuck do you think you are doing you moronic ape?"
    hide sasha
    return

label sasha_play_pool:
    "I splash some water towards Sasha."
    sasha.say "Dimwit! You'll regret that!"
    show playing water pool sasha
    "After that she retaliates and we play in the water for a while..."
    sasha.say "That was fun!"
    mike.say "It sure was."
    $ sasha.love += 1
    $ sasha.flags.greeted = TemporaryFlag(True, 1)
    return

label sasha_tv:
    call sasha_greet from _call_sasha_greet
    if hero.charm >= 40 - sasha.love or sasha.activity_name == "tv":
        call watch_tv_with (sasha) from _call_watch_tv_with_5
    else:
        show sasha
        sasha.say "Sorry, I don't have time right now."
        $ hero.cancel_activity()
        hide sasha
    return

label sasha_tv_reaction:
    sasha.say "Ok."
    return

label sasha_tv_bj:
    show couch fun sasha
    "Sasha wraps her fingers around my shaft and rolls her tongue out, licking up along my length."
    mike.say "O... oh wow..."
    mike.say "It feels so good."
    sasha.say "I kind of knew this would please you..."
    if sasha.flags.mikeNickname:
        sasha.say "...[hero.name]."
    "Again, she licks up my shaft, up over the glans and over the tip."
    "What did I do to deserve the greatest roommate in the world?"
    "I wonder this as the excitement of her actions tingles up through my body."
    show couch fun sasha cumshot
    "I can't hold back and, with a groan, I release, shooting up onto her."
    "Cum sprays up onto her face, getting her nice and covered by my jizz."
    hide couch
    show couch fun sasha facial
    "Sasha smiles up at me, batting her half-lidded eyes up in my direction."
    sasha.say "Enjoy this view, [hero.name]."
    "Sasha takes a finger and slips a drop of my cum off of her face."
    "She then wraps her lips around my cock, moaning in delight at the taste."
    hide couch
    $ sasha.flags.couchbj = True
    return

label sasha_zombietalk:
    mike.say "Okay, in no way is this movie based on a true story."
    sasha.say "It's a future true story."
    sasha.say "A zombie apocalypse is going to happen."
    sasha.say "I mean, studies show only one of us would survive."
    sasha.say "The question is, which one? Depends on survival strategy, you know?"
    sasha.say "Are we talking strength to fight them or ability to blend in and live amongst them?"
    sasha.say "All right, if we're gonna do ability to blend in, l say you."
    sasha.say "You are basically a zombie."
    sasha.say "Wake up at 7:00, shower, eat."
    sasha.say "Eh And, like a zombie, you don't really have any hopes or dreams."
    mike.say "I have dreams."
    sasha.say "Really?"
    $ result = renpy.display_menu([("Finding love", 1), ("Becoming rich", 2), ("Banging a lot of women", 3)])
    if result == 1:
        mike.say "Look, l'm looking for the love of my life."
        $ sasha.love -= 1
    elif result ==2:
        mike.say "Look, l'm going to be filthy rich."
        $ sasha.love += 1
    else:
        mike.say "Look, I'll fuck every woman I can."
    sasha.say "Oh, yeah, you seem to be doing just fine."
    mike.say "I can tell you who would die first in a zombie attack."
    mike.say "I mean, it's obviously you."
    mike.say "You are out of shape, have no marketable talents, and no survival skills."
    sasha.say "There are things in this world that you love."
    sasha.say "That slows people down."
    sasha.say "My cold, black heart and living without attachments to anyone or anything, that's my greatest asset right there."
    $ sasha.flags.zombietalk = True
    return

label sasha_tv_footrub_1:
    "I'm trying to finally turn my brain off after a particularly stressful day at work by bombarding it into submission with mindless TV shows, when Sasha walks into the room."
    "She makes a show of flopping down on the opposite end of the sofa from where I'm sitting, pulling her legs up onto the cushions as she does so."
    "When she doesn't as much as say a word, I feel like I'm being baited into breaking the silence, but do so just to stop it from getting too weird."
    mike.say "Hey, Sasha - how was your day?"
    "She sighs with a little too much of a practised sound to it for me to believe that she's being totally genuine, before she answers me."
    sasha.say "Ah, pretty tough, you know - really tiring too!"
    "I nod in genuine sympathy."
    mike.say "Me too - had to deal with this really awkward case where..."
    sasha.say "You know what, [hero.name] - I'm just too frazzled to be a good listener tonight, yeah?"
    "I shrug off the way that Sasha just shut me down, willing to accept that she's not in the mood to exchange stories about our mutually shitty day."
    mike.say "Okay...you just want to lounge around here with me tonight, watch some garbage TV?"
    "At this, Sasha makes an odd sort of non-committal sound, as though she wants something more, but won't straight out ask for it."
    "I notice that she's stretching her legs out now, frowning a little as she does so, as if to suggest there's pain involved in the movements."
    "As is her habit when she's lounging around the house with nothing better to do, Sasha's wearing shorts right now."
    "And this means that I'm getting a rather spectacular view of her long, shapely legs as she inches her feet ever closer to me."
    sasha.say "Well, [hero.name], I've been on my feet all day at work."
    sasha.say "And I was going to ask if..."
    "Sasha pushes her bare feet the last couple of inches needed to close the distance between us, and plants them in my lap."
    sasha.say "If you'd be a babe and give me a little bit of a foot rub?"
    "I look down at her pale, delicate feet as they're resting on my lap."
    "And then up at Sasha's endearing smile - a smile that seems to say what she's asking for is as innocent as passing her the remote or telling her the time of day."
    "I can't help gulping as I ponder my options."
    menu:
        "Do it":
            $ sasha.sub -= 1
            $ sasha.love += 1
            "It's a simple choice, really - sit here and watch TV that's slowly melting my brain, or do the same whilst getting my hands on Sasha's feet."
            "Come to think of it, is there really any choice at all?"
            mike.say "I'm no professional masseur, Sasha - but I'll gladly give it my best shot."
            "Sasha smiles at this and sinks down lower on the sofa, only stopping when she's practically horizontal and I can easily get at the soles of her feet."
            sasha.say "Oh, [hero.name] - you're a godsend!"
            sasha.say "I don't need my Chakras rearranged, just some life rubbing back into them!"
            show sasha foot massage
            "I nod as I make sure my palms aren't sweaty, and then gently take hold of her right foot."
            "When I told Sasha that I wasn't a masseur, it was the honest truth."
            "And so the best that I can do is go on feeling and instinct, then keep an eye on how she reacts to what I'm doing."
            "I begin by using my thumbs to rub around the heel of her foot, working my way slowly upwards as I go."
            "Sasha's feet are as tight and tense as she claimed, but they soon start to loosen up under the firm but gentle pressure I'm applying."
            "As my thumbs move further up the sole of her foot, I start to apply the balls of my thumbs to the parts that I've already been over."
            "And soon I'm massaging as much of her foot as possible all at once."
            "I'm hardly looking down at my efforts as I switch to Sasha's left foot and repeat the process."
            "The sight of her sighing and beginning to breathe more deeply in response to the massage is far more compelling of a thing to watch."
            "Getting the same treatment as the right foot, her left is soon as relaxed and supple too."
            "From there, I switch to rubbing her toes, taking each one individually and never hurrying to move on to the next."
            "Soon, Sasha's eyes are closed and she's paying no attention whatsoever to the TV."
            "The expression on her face is almost enough to make me get hard myself, and I think I'm beginning to gain a certain sympathy for foot fetishists too!"
            "When she finally opens her eyes once more and nods in satisfaction, I feel lost at the massage coming to an end."
            sasha.say "Aww...thanks, [hero.name], that really did the trick!"
            sasha.say "Hopefully I can sleep now."
            "I shrug off her thanks and smile sheepishly, not knowing if I'll be able to do the same myself."
            $ sasha.flags.footrub += 1
            hide sasha foot
        "Don't do it":
            $ sasha.sub += 1
            $ sasha.love -= 1
            mike.say "Normally I would, Sasha, honestly."
            mike.say "But I've got just the same problem with my hands."
            "Sasha raises an eyebrow as she looks at me with visible disbelief."
            mike.say "No, seriously - I spend all day typing away at a computer."
            mike.say "So by the time evening comes around, my fingers are just as screwed-up as your feet must me right now!"
            "Sasha rolls her eyes and shakes her head at this."
            mike.say "It's the truth, Sasha - I'd be afraid of doing more harm than good..."
            "She snorts in derision and drags her legs back over to her own side of the sofa."
            "After that, we continue to watch TV while an awkward silence prevails."
    return

label sasha_tv_footrub_2:
    $ sasha.flags.footrub -= 3
    if sasha.flags.footrub < 0:
        $ sasha.flags.footrub = 0
    $ sasha.sub -= 5
    $ sasha.love += 5




    "I can't quite put my finger on it, but there's an odd cast in Sasha's eyes whenever she looks over in my direction."
    "It's not hostile in any way, just enough to make me feel a little nervous."
    "I feel as if she's watching me, waiting for the right moment to spring an unexpected surprise."
    "My legs are stretched out in front of me as I recline on the sofa, but Sasha's are laid across the length of it."
    "She has her head propped up on cushions at the other end and her bare feet resting idly in my lap."
    "They've been still and unmoving for a while now, but then I feel movement and look down at them."
    "Sasha's begun the rotate her feet, stretching them as she clenches and unclenches her toes."
    hide sasha
    show sasha foot massage
    "Almost absent-mindedly, I take hold of her left foot and begin to massage the sole with my thumbs."
    "I should say that I'm not any kind of serous foot fetishist, but also that I'm not phobic of them either."
    "And Sasha does have one of the nicer pairs of feet that I've ever had the privilege of handling in this manner."
    "I'm also not a professional masseur, but it's almost impossible not to get a positive reaction from giving a foot-rub unless you're absolutely clueless."
    "Sasha begins to make appreciative sounds almost immediately, though she doesn't take her attention off of the TV show she's assiduously not watching."
    "That's fine by me, as it's enough to know that she appreciates my efforts, no matter how small."
    "I move on from the left foot to the right, repeating the same process and taking an equal amount of time and care."
    "It's only when I finish my massage on the second foot that I actually look up and realise that Sasha's no longer pretending to watch the TV."
    "Instead she's watching me, her face reminding me of a satisfied cat."
    "Or maybe one that's just woken from its nap and finds itself feeling a little frisky."
    sasha.say "You know, [hero.name], you're pretty good with your hands."
    mike.say "Th...thanks, Sasha!"
    "I hope that my eager grin at her praise doesn't make me look too goofy."
    sasha.say "But I tell you what...I bet I'm better."
    sasha.say "In fact, I bet you that I'm even better with my feet!"
    "What does she mean by that?"
    "Is she about to walk all over me, like they do in those oriental massage parlours?"
    "While I kind of enjoy her doing it in a metaphorical sense, I don't know if I'm up for Sasha doing it in a literal one too!"
    sasha.say "Open your flies, [hero.name]."
    "It's not a request, nor even really a command."
    "More of a statement of what's going to happen without the thought of it being objected to."
    "Even so, I find myself hurrying to do as I'm told, already intrigued to see exactly what Sasha has in mind."
    sasha.say "Good...now get your dick out."
    "Again I follow her instructions, pulling my cock out of my pants and allowing it to flop into my lap and onto Sasha's naked feet."
    show sasha foot footjob blush
    "Sasha smiles indulgently at me as she begins to move her toes, causing my cock to bounce up and down as they do so."
    "She tries to catch it between her feet, clumsily at first, but then slowly getting the hang of it a little at a time."
    "I can already feel my cock beginning to get hard, which serves to make her job that much easier as it rises of its own accord."
    "Though I can't be sure if the erection's more on account of what she's doing with her feet now or the thought of what might come next."
    "I've heard of foot-jobs, but I've never actually had one before now."
    "They're not on my regular list of preferences for porn viewing either, so this could be a true voyage of discovery for me."
    "Once my cock is as stiff as it's going to get, Sasha starts to rub the soles of her feet up and down its length."
    "All the time she does her best to keep it held between them, so that I feel the touch of her soles as they work my shaft."
    "The clumsiness of her feet means that she has to go slowly and carefully, making the whole experience that much more sensual and involved for me."
    "While I might miss the delicate touch of more dexterous fingers or a tongue, the fact that Sasha's feet are larger means that I can feel more of my cock being caressed."
    "She varies her technique then, using the sole of one foot to press my dick against the other."
    "Her left foot is above and the right below, so that I'm pressed into the former by the latter."
    "Soon Sasha seems to have become comfortable enough to settle into a routine of switching between these two positions."
    "One moment she uses both feet on me, and the next she changes so that one holds me while the other rubs against it."
    "Again the care required of her and the size of her soles ensure that I find the whole experience exquisite in the extreme."
    "I honestly think that Sasha could have brought me off doing just that if she had been of a mind to."
    "But I can see, from the amused look on her face as she watches me gasp from her efforts, that she already has something else in mind."
    "It's then that Sasha begins to use her toes to grip and squeeze the sensitive skin of my cock."
    "If I thought that the soles of her feet were good to feel against my dick, then I was in no way prepared for the sensation of the muscular balls of her feet."
    "I feel as though I'm being seized and massaged by miniature and yet strong hands."
    "Sasha uses both feet to clutch me close to the head of my cock, and then starts to work the shaft almost as if giving me a hand-job."
    "Only now does she start to go faster, perhaps sensing that this is a more familiar technique and feeling more comfortable as a result."
    show sasha foot footjob orgasm
    "The effect on me is pretty much the same - I quickly go from feeling relaxed and like I'm being eased towards an orgasm to the urgency of the thing taking over completely."
    "Her toes are digging into me now, the motion of her feet needing the entirety of her legs to move in order to keep up the pace."
    "I hadn't noticed before, but my own hands are clutching handfuls of the sofa cushions and my toes are gripping the pile of the carpet as if they fear to let go."
    "Sasha shifts her feet slightly, so that they're clasping my cock between them now."
    "She continues to massage with her toes, but now most of the motion is coming from her legs and she reminds me of a cricket using it's limbs like a fiddle."
    show sasha foot footjob cum
    "Faced with all of this sensation and the strength of Sasha's entire lower half, I can already feel myself cumming."
    "Moments later, I see the evidence of this as it's forced from between her clenching toes and begins to run down the tops of her feet."
    "As I pant from my exertions and my cock starts to go flaccid again, Sasha makes no effort to remove her feet."
    "Instead she keeps them right where they are, still enjoying the feeling of massaging the softening length of my cock now that she has my cum between her toes and on the soles of her feet."
    "I should try to get up and clean myself off, definitely change my pants."
    "But for the moment, all I can do is lie slumped upon the sofa, staring at the satisfied and triumphant look on Sasha's face."
    $ sasha.flags.footjob = True
    hide sasha foot
    return

label sasha_tv_footrub_3:
    "To a casual observer, it might appear that there's absolutely nothing going on in the living room apart from what can be seen with the naked eye."
    "There's just Sasha and myself, sitting on either ends of the sofa with the TV blaring out the standard fare that we like to unwind to when we have the time."
    "But we both know full well that there's an unspoken agenda here."
    "One that she's just keeping me in a state of suspense over, and enjoying every minute of it too."
    "Neither of us says a word, only casting the occasional furtive glance in the direction of the other."
    "Whenever my own eye catches Sasha's, I can't help but look away quickly as she smiles in plain amusement at my discomfort."
    "Eventually, just when I think that I'm about to snap from the tension, I feel the sensation of something landing upon my lap."
    "Even though it's exactly what I've been expecting to happen sooner or later, I still can't help jumping a little in surprise."
    "This earns me a laugh from Sasha, and it's all the sound that she needs to make, as I know exactly what's expected of me in this situation."
    hide sasha
    show sasha foot massage
    "Without a moment of pause or hesitation, I take Sasha's bare foot in both hands and begin to work away at the sole with my thumbs."
    "This isn't the first time that she's demanded such treatment from me, and I know the drill pretty well by now."
    "Hell, I've even been watching videos online to pick up some hints and tips on how to make my foot rubs something special, for her sake alone."
    "I can soon hear the evidence of this paying off too, as Sasha begins to make appreciative noises and recline on the sofa."
    "A chance moment of glancing upwards from my task shows me that she's closed her eyes in order to better savour the effects of the massage as well."
    "This means that I can watch freely as she succumbs to the pressure that I'm applying in all of the right amounts and in all of the right places."
    "Sure, it might look like Sasha's the boss in our relationship and that I'm afraid to step a foot (if you'll pardon the pun) out of line with her."
    "But the truth is that I actually enjoy being able to please her like this, and it makes me know that she needs me too."
    "I know that she's not just walking all over me (again with the puns, sorry) right now."
    "What I'm doing shows her just how much I care."
    "It shows that she can ask anything of me and I'll always rise to the challenge."
    "As far as she's concerned, nothing's too much trouble - and I mean that."
    sasha.say "Mmm...[hero.name]...that feels SO good!"
    sasha.say "But you know what - I think it'd feel much better if you used your tongue instead..."
    menu:
        "Don't do it":
            $ sasha.flags.footrub = 0
            $ sasha.sub += 1
            $ sasha.love -= 1
            "Feel better for who, exactly?!?"
            "I mean, as much as I like giving Sasha a massage like this, that's asking too much!"
            mike.say "I hear what you're saying, Sasha."
            mike.say "But I don't think I'm up for doing that right now."
            mike.say "Have you even washed your feet today?"
            "Sasha, of course, looks instantly annoyed."
            "But I can't tell if it's more on account of my refusal to do what she wants or my suggesting that her feet might be less than squeaky clean."
            "Either way, she doesn't say a single word in response, only yanks her foot out of my grasp and then turns her back on me in a huff."
        "Do it":
            $ sasha.flags.footrub += 1
            $ sasha.sub -= 5
            $ sasha.love += 5
            "What the hell?"
            "It's not like I haven't licked other parts of Sasha's body in the past, now is it?"
            "And the look on her face is telling me that she's already pretty into the idea of me doing it to her."
            "So what have I got to lose?"
            "I shrug and give Sasha a smile as I nod to show my assent."
            mike.say "Sure, why not?"
            mike.say "If I have to kiss someone's feet, why not yours?!?"
            "Sasha returns my smile, looking all the while like the cat that got the cream."
            "Who would have thought all you needed to do to keep such an amazing girl happy was keep on giving her whatever she wants?"
            "It's just so simple - why did I never hit upon the idea before now!"
            hide sasha
            show sasha foot lick
            "I lift Sasha's foot up a little, just enough so that I can lean forward and reach it with my lips."
            "The truth is that, up this close, it doesn't really smell all that bad."
            "There's just the lingering scent of her socks and shoes, but nothing that could put me off."
            "I'm not sure of just where to begin, so I fall back on the basics, kissing the sole at first."
            "The skin is softer than I expected it to be, and I'm thankful for the fact that Sasha has such healthy and pristine feet like never before!"
            "She giggles and flinches a little in response, betraying just how ticklish she actually is."
            "Of course the laughter only serves to begin to turn me on, and I respond by taking my first actual lick at her foot."
            "Sure, it tastes a little bitter against my tongue - but what's that compared to how weird an actual pussy tastes?"
            "And anyway, I soon forget about all of that when I hear the reaction that it gets out of Sasha."
            "After that there's no stopping me, and I find myself licking the entire length of the sole, over and again."
            "I try to trace the lines and curves of her muscles, just like I would with my fingers."
            "But my tongue doesn't seem to have the same amount of stamina, and I soon have to limit myself to gentle, sensual passes instead."
            "I work my way vaguely upwards, starting each new lick from a higher point, until I finally reach Sasha's toes."
            "Then I work inwards from the smallest, liking around the bottom of them and then sucking them into my mouth one by one."
            "While I might not hear any evidence of Sasha being on the brink of cumming from what I'm doing to her, she keeps up the moans and sighs the whole time I'm at it."
            "And when I'm finally finished, she looks almost as relaxed and satisfied as I do exhausted and tongue-tied."
            $ sasha.flags.footlick = True
    return

label sasha_tv_footjob:
    scene bg livingroom
    "I've pretty much given up on putting any effort into the rest of the day by the time that I flop onto the sofa in the living room."
    "All I want to do is lie down and maybe binge watch a couple of episodes of a series before I feel the need to turn in for the night."
    "At the sound of someone padding into the room on bare feet, I glance up in time to see Sasha as she sits down on the other end of the sofa."
    show sasha sleep
    "She gives me what I guess is supposed to be an innocent smile, and I return the gesture, neither of us saying a single word."
    "But I can see instantly that she's very much awake and not in the mood to just vegetate, no matter how much she's trying to hide the fact."
    "I've almost gotten used to the way that Sasha likes to wander around the house in nothing but tight little shorts and a t-shirt of an evening."
    "At first it was a constant distraction, but now it just causes a gentle stirring in my shorts most of the time."
    "I do wonder if Sasha dresses like that for the sake of getting just such a reaction out of me."
    "And if so, then the way in which I've become used to her semi-naked lounging around the place might go some way to explaining what she does next."
    "I can see that she's trying to steal glances at me, as if gauging just how passive I am right now and planning her next move accordingly."
    "Slowly, ever so slowly, Sasha begins to pull her legs up onto the sofa and then push them towards me."
    "Soon her feet are between my own legs, moving inch by inch closer to my knees and then they're between my thighs."
    hide sasha
    scene sasha foot
    "It's the big toe of her right foot that makes the first tentative move to touch my groin, stroking gently to see what my reaction will be."
    "As Sasha begins to rub more intensely with both feet, I glance down at what she's doing for the first time."
    "I look up and raise my eyebrows, not urging her on and yet not telling her to stop either, but instead showing that I'm curious to see where this is going."
    "As if she's eager to gain my approval, Sasha now begins to massage me through the front of my pants with the soles of both feet at once."
    "For all that I'm trying to play it cool right now, she's not really having any trouble rousing life in my cock."
    "I don't know if she can feel the way that it's starting to swell in size, but at this rate, it won't be long before I'm fully erect."
    "On the other hand, as my cock grows, I can feel ever more sensations of what she'd doing with every second that passes."
    "Assuming that if I objected to what she's doing in any way then I would have said so by now, Sasha seems to become emboldened."
    "She leans forwards with a mischievous grin spreading across her face as she undoes my flies and reaches inside."
    show sasha foot footjob
    "Pulling my now fully erect cock out, she leans back and begins to grasp it between the soles of her feet."
    "And there I was thinking that all I had left in me was the energy required to slob on the sofa tonight!"
    "Almost as soon as my cock comes alive with the sensation of being held and massaged between the soles of Sasha's feet, I can feel myself stirring too."
    "She caresses the head with her toes gently, and then squeezes it harder for a moment until she sees me react visibly to her attentions."
    "Somehow the fact that when using her feet, Sasha is so much clumsier than she would be with her hands, makes the sensations all the more intense."
    show sasha foot footjob blush
    "Next she uses her left foot to press my cock against the sole of her right, rubbing up and down with the latter."
    "The entire length of the shaft is treated to the feeling of her clenched toes as they travel slowly up and down."
    "By now, I have my head propped on the arm of the sofa, unable to pretend like I'm not totally enraptured by what Sasha is doing to me."
    "The fact that she knows this is plain to see in her eyes, which glimmer with amusement as she aims to see just how much of this I can take."
    "Sasha begins to use both feet now, gripping either side of my cock with her toes and moving them vigorously up and down."
    "This is the closest that she's come to doing something that even resembles a conventional hand-job, and yet it feels that much rougher and more intense to me."
    "I honestly don't know if it's the foot-job alone that's making me feel like I'm going to cum at any moment."
    show sasha foot footjob orgasm
    "Either that or the fact that I'm looking over my own cock at Sasha's face as she's giving it to me."
    "The sheer amount of wicked amusement and pleasure that can be seen in her expression makes the whole thing so much more intense."
    "As she goes ever faster, I can't help feeling as though she's using her feet to literally drag the fast approaching climax out of me."
    show sasha foot footjob cum
    "But the moment that I do start to cum, she surprises me by instantly grabbing the head of my cock with the toes of her right foot."
    "I watch as the cum seeps through the gaps between her toes, and she squeezes them together to make it practically ooze forth."
    "Sasha giggles as the stuff runs down the back of her foot and between the sole and the shaft of my cock."
    "All I can do is lie back and watch as she releases me, wiping the mess off of her foot and into the leg of my pants."
    $ sasha.sub -= 5
    $ sasha.love += 5
    return

label sasha_bye(bye_outfit=None):
    call npc_bye_outfit (npc=sasha, bye_outfit=bye_outfit) from _call_npc_bye_outfit_19
    $ (day, h, activity, bye_outfit) = _return
    if not activity == sasha.activity:
        if day != game.week_day:
            $ sasha.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ sasha.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"sasha {bye_outfit}")
        if activity["activity"] == "sleep":
            sasha.say "I am smashed, I should go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            sasha.say "I'll go clean myself up now, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            sasha.say "I've got to run or I'll be late for work, bye."
        elif activity["activity"] in ["meal"]:
            sasha.say "I am starving, I'll go grab a bite!"
        elif activity["activity"] in ["tv"]:
            sasha.say "I am bored, I'll watch some tv I think."
        elif activity["activity"] in ["drink"]:
            sasha.say "I'll go to the pub and have a drink, see you around."
        elif activity["activity"] in ["sunbath"]:
            sasha.say "It's sunny today, I think I'll go laze around near the pool."
        elif activity["activity"] in ["shop"]:
            sasha.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            sasha.say "I'll go read a book now, that's how bored I am."
        elif activity["activity"] in ["dance"]:
            sasha.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            sasha.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            sasha.say "I'll go get dressed up."
        hide sasha
    return

label sasha_greet:
    $ renpy.log(f"sasha_greet ")
    if renpy.has_label(f"sasha_greet_dialogues_{hero.gender}") and not sasha.flags.greeted:
        scene expression f"bg {game.room}"
        show sasha
        $ sasha.flags.greeted = TemporaryFlag(True, 1)
        $ result = randint(1, 3)
        if result == 1:
            sasha.say "Hello."
        elif result == 2:
            sasha.say "Hi, [hero.name]."
        else:
            if game.hour < 6:
                sasha.say "Hello [hero.name]."
            elif game.hour < 12:
                sasha.say "Good morning [hero.name]."
            elif game.hour < 19:
                sasha.say "Good afternoon [hero.name]."
            else:
                sasha.say "Good evening [hero.name]."
        call expression f"sasha_greet_dialogues_{hero.gender}" from _call_expression_263
        if sasha.flags.submissive_interact:
            sasha.say "I like my music, [hero.name] - but nothing rocks me like your cock!"
        hide sasha
    return

label sasha_greet_dialogues_male:
    if sasha.flags.mikeNickname:
        if game.hour < 6:
            mike.say "Hello my slave."
        elif game.hour < 12:
            mike.say "Good morning my slave."
        elif game.hour < 19:
            mike.say "Good afternoon my slave."
        else:
            mike.say "Good evening my slave."
    else:
        $ result = randint(1, 3)
        if result == 1:
            mike.say "Hello, Sasha."
        elif result == 2:
            mike.say "Hi."
        else:
            if game.hour < 6:
                mike.say "Hello."
            elif game.hour < 12:
                mike.say "Good morning Sasha."
            elif game.hour < 19:
                mike.say "Good afternoon Sasha."
            else:
                mike.say "Good evening Sasha."
    return

label sasha_kiss_reaction_male:
    if sasha.lesbian > MAX_LES_GUY_SEX:
        $ sasha.lesbian -= 1
    return

label sasha_kiss_male:
    scene expression f"bg {game.room}"
    if sasha.love < 25 and not sasha.is_girlfriend and not game.active_date.score >= 75:
        show sasha
        "It can be hard to read Sasha from one moment to the next."
        "Sometimes she's upbeat and fun, other times she can be pretty dark and even angry."
        "But I know that I've misjudged her mood the moment that I make a move to kiss her."
        "And worse still, it seems that I've done so pretty badly too."
        "My reward for this is Sasha yanking her head away from me almost violently."
        "That and a look that could curdle milk from across a room, if not kill me outright!"
        sasha.say "Try that again and I'll cut your balls off."
        $ sasha.love -= 5
        $ sasha.sub -= 5
        hide sasha
    elif not sasha.flags.kiss:
        hide sasha
        $ sasha.love += 5
        call sasha_kiss_reaction_male from _call_expression_265
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
        call sasha_kiss_reaction_male from _call_expression_266
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

label sasha_ask_date_male:
    if Harem.find_by_name("band") and Harem.find_by_name("band").is_active(sasha):
        menu:
            "Ask Sasha on a date":
                call sasha_ask_date_alone_male from _call_sasha_ask_date_alone_male
            "Meet Kleio, Anna and Sasha for a 'hot coffee'" if Harem.together(anna, kleio, sasha, name="band"):
                mike.say "Do you want to get together with Anna and Sasha and have some fun?"
                sasha.say "I'd love to."
                call select_date_time from _call_select_date_time_11
                $ (day, hour, say_string) = _return
                if day == "cancel":
                    return
                $ mike.say(say_string)
                menu:
                    "See you in your room":
                        if day == "now":
                            call kleioannafoursome from _call_kleioannafoursome_2
                        else:
                            $ hero.calendar.add(day, HaremAppointment(hour, "band", ["kleio", "anna", "sasha"], "kleioannafoursome"))
                    "Let's meet in my room" if "kleioannafoursome2" in DONE:
                        if day == "now":
                            call kleioannafoursome2 from _call_kleioannafoursome2_3
                        else:
                            $ hero.calendar.add(day, HaremAppointment(hour, "band", ["kleio", "anna", "sasha"], "kleioannafoursome2"))
                return
    else:
        call sasha_ask_date_alone_male from _call_sasha_ask_date_alone_male_1
    return _return

label sasha_ask_date_alone_male:
    mike.say "Sasha, would you like to go on a date with me?"
    if sasha.love < 50 or sasha.flags.nodate:
        sasha.say "I'm sorry [hero.name], I don't see you that way."
        $ date_choice = False
    else:
        sasha.say "Sure, it might be fun, when do you want us to go?"
        $ date_choice = True
    return date_choice

label sasha_walk_outside:
    scene bg livingroom
    mike.say "Okay, let's get you a little fresh air."
    "Sasha look at me in confusion as I stand up."
    "But a gentle yet firm tug on her lead convinces her to follow suit."
    show sasha naked leash
    "I walk her to the front door and open it wide, then gesture for her to step outside."
    menu:
        "Take her out in the garden.":
            call sasha_walk_outside_garden from _call_sasha_walk_outside_garden
        "Take her to the park.":
            call sasha_walk_outside_park from _call_sasha_walk_outside_park
    $ game.pass_time(1)
    return

label sasha_walk_outside_garden:
    scene bg livingroom
    show sasha naked
    show hand sasha
    mike.say "There you go - what are you waiting for?"
    "Sasha raises a tentative hand."
    mike.say "Speak."
    sasha.say "Please, [hero.name]...I don't understand..."
    mike.say "What's not to understand?"
    mike.say "You're my bitch, you're wearing collar, and you need the bathroom."
    "I see recognition appear in Sasha's eyes."
    "Without needing to be told, she drops onto all fours and pulls eagerly on her leash, whining to be allowed outside."
    hide sasha
    hide hand
    scene petplay
    show petplay walk sasha leash
    "Not willing to be outdone by her, I walk the Sasha out of the front door into the garden."
    "Luckily for us, there aren't many lights on the neighborhood windows."
    "That means that only I get to see the spectacle of Sasha hunting on her hands and knees for an agreeable spot amongst the flowerbeds."
    "Sasha quickly relieve herself too."
    show petplay stand sashapee sashacloseeyes sasha
    mike.say "Finished?"
    show petplay stand -sashapee sashaopeneyes sasha
    "Sasha nod happily, not fazed in the least by the experience."
    "Shaking my head, and more than a little turned-on, I lead her back along the street to the house, usher her inside and lock the door."
    return

label sasha_walk_outside_park:
    scene bg house
    show sasha naked leash
    "She eagerly walks out onto the sidewalk on all fours, and I almost forget to scan the street for signs of anyone watching."
    scene bg street
    show sasha naked leash
    "So hypnotic is the sight of her naked backside in motion and the occasional hint of breasts, swaying from side to side."
    hide sasha
    scene petplay
    show petplay walk sasha leash
    "Several times before we reach the gates of the park, I'm almost half sure that I can see hints of light as people jerk curtains."
    "It's the way I can't be sure if we're being watched or not that makes the thought so thrilling for me."
    "But if anyone is peeping through their drapes at me walking my most unusual pet tonight, they're not making a point of coming out to confront me about it."
    "It's too late for mundane dog-walkers as we finally walk off of the street and into the park."
    "Though I can hear the occasional noise that I'm sure can't be an animal every now and then."
    "There are no street lights in the park, and we seem to be insulated in our own little world of darkness as we find our way to a stand of trees."
    "Just then I hear the unmistakable sound of footsteps approaching quickly."
    "I glance over my shoulder in time to see a jogger pounding her way up the path towards where I'm standing."
    "I step neatly out of the way as she passes, giving her a polite smile."
    "But all the time I'm silently panicking, trying to resist the urge to glance over at Sasha for fear of drawing the eye of the jogger as well."
    "She gives me a brief glance and a smile, before she passes me and jogs off until she's out of sight."
    "Finally I can breathe out and look over towards where I last saw my bitch."
    "Shaken by the experience, but not wanting to show it to Sasha, I walk into the stand of trees and call for her to come to me."
    "She obey eagerly, making me think that either she missed the passing of the jogger entirely, or else did not and enjoyed the thrill of coming so close to being seen."
    show petplay stand sasha
    "It's then that I look up to see that she has a hand raised, asking permission to speak."
    mike.say "Alright, Sasha - what do you have to say?"
    sasha.say "Now that we've had our exercise and fun..."
    sasha.say "Would [hero.name] allow me to do something nice and fun for him?"
    "I look at Sasha's smile and her wide, innocent-seeming eyes."
    "Why shouldn't I indulge her?"
    "We've only seen one other person the entire time we've been out here, and now we're well and truly standing in amongst the trees."
    "Also, my nerves are getting pretty frayed around the edges."
    "I could do with something enjoyable to calm me down before we head back home."
    "I smile indulgently at Sasha and nod my assent."
    "In response, she claps her hands together and happily shuffles forwards until she's kneeling before me."
    show petplay stand sasha sashabj
    "Sasha sets about unzipping my flies and pulling out my cock, making small, excited noise as she does so."
    "It's cold in the spot where we're standing, and that sashaze returns now with a vengeance."
    show petplay stand sasha sashabj inside hold -sashatongueout
    "But as if she can sense the way in which the cold is making me a little uncomfortable, Sasha wastes no time in wrapping her lips around my dick."
    "I'm not yet fully aroused, but the wet, warm sensation of her tongue soon fixes that problem."
    "Watching Sasha's face as she literally coaxes my cock to being fully erect is an experience in and of itself."
    show petplay sashacloseeyes
    "As it grows, she's forced to maneuver around it and struggle to keep the entire thing inside of her mouth as much as possible."
    "Her almost stubborn determination to keep it from escaping her is almost as arousing as the feeling of the blowjob she's giving me at the same time."
    "Indeed, Sasha whines and pines whenever it looks like my dick is going to slip from between her lips."
    show petplay cumshot
    "I lose myself in Sasha's mouth, a trickle of my cum begins to seep from the corner of her mouth."
    show petplay stand sasha -sashabj sashaopeneyes sashaopeneyes sashatongueout nohold outside
    "I stand still and allow Sasha to push my cock back into my pants."
    show petplay walk sashahappy -cum
    "With her lead firmly back in my hand, I give her a firm but gentle tug, making her trot along almost perfectly at heel."
    "It doesn't take us long to walk the short distance back home, and there are even fewer signs of life along the way than there were earlier in the evening."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
