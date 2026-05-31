init python:
    Event(**{
    "name": "bree_kat_threesome",
    "label": "bree_kat_threesome",
    "conditions": [
        IsDayOfWeek("67"),
        IsHour(10, 18),
        GameTarget(
            Not(IsFlag("gaming_delay")),
            ),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom"),
            Not(OnDate()),
            HasStamina(),
            ),
        PersonTarget("bree",
            Not(IsHidden()),
            HasRoomTag("home"),
            IsFlag("befriendKat", True),
            MinStat("sub", 50),
            MinStat("sexperience", 5),
            Or(
                InHarem('home'),
                MinStat("lesbian", 10),
                ),
            ),
        Or(
            "'fafow' not in DLCS",
            And("'fafow' in DLCS",
                IsDone("gaming_harem_event_02"),
                PersonTarget("kat",
                    Not(IsHidden()),
                    InHarem('gaming'),
                    MinStat("love", 130),
                    MinStat("sexperience", 3),
                    Not(IsDatePlanned()),
                    ),
                ),
            ),
        ],
    "music": "music/roa_music/juice.ogg",
    "do_once": True,
    }
    )



label bree_kat_threesome:
    scene bg livingroom
    show bree evil
    with fade
    "I look up from the stack of games in front of me as [bree.name] hurries into the sitting room."
    "She has a serious look on her face, almost as serious as the one that I have on mine right now."
    mike.say "We're all set, [bree.name]?"
    mike.say "Ready to go?"
    "[bree.name] nods stiffly, almost like she's standing to attention and saluting me."
    show bree happy
    bree.say "Absolutely, [hero.name]!"
    bree.say "We're one hundred percent prepared."
    bree.say "Everything's been taken care of!"
    show bree normal
    "I narrow my eyes at this, trying to look straight into [bree.name]'s soul."
    mike.say "You sure, [bree.name]?"
    mike.say "Are all the doors locked?"
    show bree wink
    bree.say "Locked AND bolted."
    mike.say "Is your mobile turned off?"
    show bree normal
    bree.say "Dead as a fossilised brick."
    mike.say "We have snacks sufficient to last?"
    show bree happy
    bree.say "Enough chips and pizza to give us terminal acne!"
    mike.say "And you're SURE Sasha's out of the house?"
    show bree normal
    bree.say "She has band practice and then the pub."
    bree.say "So she'll pass out under a table before she gets home!"
    "I nod, satisfied at last that everything really has been taken care of."
    mike.say "Okay, okay..."
    mike.say "NOW we can start playing some serious video games!"
    show bree happy at startle
    bree.say "YAY!"
    "[bree.name] hops up and down on the spot, clapping her hands."
    show play console bree with fade
    "Then she hurries over and grabs a joypad."
    "Sitting down on the floor besides me, she cracks her knuckles noisily."
    bree.say "I'm ready, [hero.name]."
    bree.say "Let's do this thing!"
    "What can I say?"
    "[bree.name] and I take our gaming seriously!"
    "Sure, we might play casually when we feel like it."
    "But this is a serious gaming session, one that's been in the diary for ages."
    "And that means [bree.name] and I are going to give it one hundred percent of our attention."
    "With that in mind, we exchange a silent nod."
    "And then we get into it!"
    mike.say "I hope you're ready for an ass-kicking, [bree.name]!"
    bree.say "Oh yeah?"
    bree.say "We'll see who's butt takes a pounding, [hero.name]!"
    "At this point we're literally staring each other down."
    "Both wired and ready to get it on!"
    "Geez...is there always this much sexual tension when other people game together?"
    play sound door_knock
    "And it's at that very moment a knock at the door cuts through it all."
    hide play
    show bree angry
    if 'fafow' in DLCS:
        "[bree.name] shoots a venomous look in the direction of the front door."
    else:
        "As one, [bree.name] and I shoot venomous glances in the direction of the front door."
    bree.say "Who in the hell could that be?"
    mike.say "I have no idea!"
    if 'fafow' in DLCS:
        "The reality is that I know exactly who it is."
        "Because I invited them over myself."
        "The person at the door is Kat."
        "But in a moment of horror, I realise I forgot to clue [bree.name] in on all of this."
        "And what's worse, I also forgot to tell her that what Kat wants is a threesome with us!"
    show bree annoyed
    bree.say "Hmm..."
    bree.say "Maybe if we just ignore them they'll get tired and go away?"
    mike.say "Nah...they could just come back and try again later."
    mike.say "Let's just go see who it is and get rid of them."
    show bree annoyed a at mostright5 with move
    "[bree.name] nods and we both get up to answer the door."
    "In the hallway I swing the front door open."
    "[bree.name] stands to my side, arms crossed over her chest."
    "And the way she looks right now, I wouldn't want to mess with her!"
    scene bg house
    show kat
    with wiperight
    if 'fafow' in DLCS:
        "But when she sees who's there, [bree.name] can't help looking surprised."
    else:
        "But when we see who's there, neither of us can help looking surprised."
    kat.say "Erm..."
    kat.say "Hey guys!"
    kat.say "It's me, Kat - you remember me, right?"
    if 'fafow' in DLCS:
        "[bree.name] gives me a puzzled glance, then looks back at our unexpected guest."
    else:
        "[bree.name] and I exchange a puzzled glance, then look back at our unexpected guest."
    "There's no way to miss the violet hair and the kind of surly expression."
    if 'fafow' in DLCS:
        "[bree.name] definitely recognises Kat, the girl she went up against in the gaming tournament."
        "In the moment that [bree.name]'s looking at neither of us, Kat winks at me."
        "Reminding me of the plan that we hatched together."
    else:
        "It's definitely Kat, the girl [bree.name] went up against in the gaming tournament."
    mike.say "Yeah, of course..."
    show bree normal at mostleft4 with moveinleft
    show fx drop at mostleft4
    bree.say "Hey, Kat..."
    bree.say "Fancy seeing you here!"
    hide fx
    if 'fafow' in DLCS:
        bree.say "Was there anything you wanted?"
        bree.say "Or are you selling stuff door-to-door now?"
    else:
        mike.say "Was there anything you wanted?"
        mike.say "Or are you selling stuff door-to-door now?"
    "Kat blushes a little, looking even more awkward than usual."
    if 'fafow' in DLCS:
        "She glances at me, as if she expects me to come to her rescue."
        mike.say "Okay, [bree.name]..."
        mike.say "Cards on the table."
        mike.say "Kat asked me if she could join our gaming session."
        mike.say "And I said yes, meaning to clear it with you later."
        mike.say "But I went and forgot."
        kat.say "So what do you say, [bree.name]?"
        kat.say "Mind me jumping in too?"
    else:
        "But somehow she manages to pluck up the courage to explain herself."
        kat.say "I...I just saw that you guys were playing videogames."
        kat.say "And I wondered if you'd mind me jumping in too?"
        "I can't help frowning and glancing around."
        mike.say "Huh?!?"
        mike.say "How did you know that?"
        mike.say "Have you been spying on us?!?"
        "Kat shakes her head and holds up her mobile."
        kat.say "No!"
        kat.say "Of course not!"
        kat.say "You just signed into the Zbox Network, that's all..."
        show bree surprised at mostleft4, vshake
        "[bree.name] slaps her forehead and lets out a groan."
        bree.say "Urgh..."
        bree.say "Of course, that's the one thing we forgot!"
        mike.say "Shit..."
        mike.say "Anyone else on there can see what we're playing!"
        "Kat nods at all of this, a nervous smile on her face."
        kat.say "So..."
        kat.say "What do you say?"
    show kat at right4
    hide bree
    show bree close annoyed
    "[bree.name] shrugs her shoulders and turns to face me."
    bree.say "I guess we could squeeze her in?"
    if 'fafow' in DLCS:
        bree.say "But I'm not happy with you, [hero.name]!"
        mike.say "I'm sorry, [bree.name]..."
        mike.say "I'll make it up to you, okay?"
        mike.say "And it's not like I invited a noob along, is it?"
        mike.say "You know how good Kat is already."
        call gaming_harem_event_03_fuck from _call_gaming_harem_event_03_fuck
        $ game.flags.gaming_delay = TemporaryFlag(True, 1)
        return
    else:
        bree.say "What do you think, [hero.name]?"
    menu:
        "Refuse":
            mike.say "Hmm..."
            mike.say "I don't really like the idea of her stalking us on the Zbox Network, [bree.name]!"
            mike.say "Maybe we could let her in on the next session that we do."
            mike.say "But right now I'm only in the mood to play with you!"
            show bree normal
            "[bree.name] nods at this."
            show bree -close at left
            "But then she turns and shakes her head at Kat."
            bree.say "Sorry, Kat - but you heard the man!"
            bree.say "Hit us up next time, okay?"
            "Kat's expression returns to it's normal position of apathy."
            "And she nods her head with what looks like resigned disappointment."
            kat.say "Oh...okay, I guess..."
            "Kat lingers on the doorstep for a moment."
            "Maybe she's waiting to see if we'll change our minds."
            "But if that's the case, then she's out of luck."
            "Because all that happens is the pair of us waving and stepping back inside."
            scene bg livingroom
            play sound door_slam
            show bree at right
            "And it's actually [bree.name] that pretty much slams the door in her face!"
            show bree happy at center with move
            bree.say "Okay, [hero.name]..."
            bree.say "Let's get it on!"
            "With [bree.name] making so little of leaving Kat out in the cold, my own guilt just melts away."
            "And I simply nod my head as I follow her back into the sitting room to start gaming in earnest."
        "Accept":
            mike.say "Hmm..."
            mike.say "I guess we WERE dumb enough to sign into the Zbox Network, [bree.name]."
            mike.say "And we'd never have known it if Kat didn't tell us too."
            mike.say "So the least we can do to say thanks is let her join us."
            label gaming_harem_event_03_fuck:
                show bree normal
                "[bree.name] nods at this."
                show kat at right4
                show bree -close at left4
                "Then she turns her head and nods at Kat too."
                bree.say "Okay, Kat - you're in!"
                show bree wink
                bree.say "Come on in and we'll bust out the spare controller."
                "Kat's normally downcast expression changes to one I've never seen on it before."
                "I can't be sure, but I think it's something approaching actual delight!"
                kat.say "Really?"
                kat.say "No way!"
                show bree happy at mostleft4 with move
                "[bree.name] and I step aside to let Kat come inside."
                hide bree
                hide kat
                with moveoutleft
                "Then the girls go ahead into the living room while I lock the door again."
                scene bg livingroom
                show bree normal at right5
                show kat at center
                with fade
                "When I catch up to them, [bree.name]'s already handed Kat the third controller."
                "And wasting no more time, we get down to a seriously intense gaming session."
                "All the time I've got one eye on Kat, expecting to regret letting her in on it."
                "I mean, after her performance at the tournament, who'd want to trust her, right?"
                "But, much to my surprise, she doesn't try to pull any shit."
                "And stranger still, she actually seems to fit in pretty well."
                "In fact, by the time we take a break, we're all laughing and joking like old friends."
                kat.say "Phew..."
                kat.say "I wish I knew how you guys do that!"
                show bree annoyed
                show fx question at right5
                bree.say "Huh?"
                bree.say "Do what?"
                hide fx
                show bree normal
                if 'fafow' in DLCS:
                    "I know where Kat's trying to take the conversation."
                    "But for now, I decide to play dumb."
                mike.say "Yeah, Kat..."
                mike.say "What is it that we're doing?"
                mike.say "I thought we were just playing videogames!"
                "Kat shakes her head at this."
                kat.say "Oh no - that's not all you're doing."
                kat.say "It's like you two are on the same wavelength or something."
                kat.say "I just wonder, is it because..."
                kat.say "Well...because you're together?"
                show bree surprised
                if 'fafow' in DLCS:
                    "[bree.name] shoots me a surprised glance."
                else:
                    "[bree.name] and I exchange a surprised glance."
                bree.say "You know...I never thought of it like that."
                mike.say "Yeah - maybe there is something to that idea."
                show bree normal
                "We both turn to look at Kat again."
                "And she's glancing away, visibly blushing."
                kat.say "I...I don't suppose..."
                kat.say "That you'd...let me in on it too?"
                show bree surprised at right5, startle
                show fx exclamation at right5
                "[bree.name]'s eyes go wide at this."
                bree.say "Kat!"
                bree.say "Did you just...proposition us?!?"
                hide fx
                "Kat waggles her head from side to side."
                kat.say "Pretty much, [bree.name]!"
                kat.say "So...what do you say?"
                show bree happy
                "[bree.name] bursts into a flurry of giggles."
                bree.say "Sounds good to me, Kat!"
                show bree normal
                bree.say "How about you, [hero.name]?"
                show bree flirt
                bree.say "Should we play Kat instead of the Zbox?"
                if 'fafow' in DLCS:
                    "I can feel a genuine surge of relief as [bree.name] asks me the question."
                    "Because it plays right into the plan I've been trying to stick to this whole time."
                    "All I need to do now is make it sound like I'm coming round to the idea like she is."
                    "And then everything should fall into place just like I wanted it to."
                else:
                    "I have to admit that Kat's been growing on me this whole time."
                    "And I don't mean that she's just turned out to be less of a bitch than I thought either."
                    "I've started to notice that she's actually quite pretty under all of that attitude."
                    "That and the fact she's hiding a hot little body under the baggy stuff she likes to wear."
                mike.say "Well, we already let her in on the videogames."
                mike.say "So why not let her in on the other games we play too?"
                "As one, [bree.name] and I once more turn our gazes towards Kat."
                "And in response, she manages a smile, but she still looks nervous."
                bree.say "Aw, don't look so scared, Kat!"
                show bree wink
                bree.say "We'll be gentle, okay?"
                bree.say "I promise we'll treat you like a vintage console!"
                "[bree.name] winks at me as she scoots towards Kat across the floor."
                "The other girl still looks nervous, but she doesn't shy away."
                "I choose to hold back a little, letting [bree.name] take the lead."
                show bree flirt underwear with dissolve
                "And she doesn't shirk the duty, already stripping off her own clothes."
                "[bree.name] doesn't go all the way though, and instead turns her attention to Kat."
                show bree at center
                show kat at left4
                with ease
                "This way she takes off an item of her own clothing, then one of Kat's."
                "I'm not sitting idle while all of this is going on either."
                "I'm removing my clothes too, just at a much slower pace."
                "And that's because I'm enjoying the show."
                show bree topless with dissolve
                "As both of them get progressively more naked, a change comes over Kat."
                "It's slow at first, almost impossible to perceive."
                "But before too long, the smile on her face is starting to grow wider."
                "Kat's actually warming up the longer [bree.name] handles her."
                "And the change is affecting me too."
                "Before Kat came across as painfully awkward and even a little cold."
                "Now she's starting to come alive, the charms of her face clear to see."
                "It's a pretty sexy thing to watch, and I can feel myself getting harder by the second!"
                "[bree.name] seems to be the first to notice."
                "As she smiles and beckons me over."
                if Person.find("kat") and kat.sexperience < 1:
                    show bree blush
                    bree.say "Ooh..."
                    bree.say "Look at that, Kat!"
                    bree.say "[hero.name]'s joystick is ready for us to play with!"
                    kat.say "Whoa..."
                    "I see Kat's eyes go wide at the sight of my cock."
                    mike.say "Erm..."
                    mike.say "Is there something the matter, Kat?"
                    kat.say "Oh...erm...no!"
                    kat.say "I just..."
                    if hero.has_skill("smalldick"):
                        kat.say "I just never saw one that cute, okay!"
                    elif hero.has_skill("hung"):
                        kat.say "I just never saw one that big, okay!"
                    else:
                        kat.say "I just never saw one that hard, okay!"
                    "For a moment I can't process what Kat just said."
                    "It's like it takes me that long to figure out it's actually a compliment!"
                    bree.say "Don't worry, Kat."
                    bree.say "You just have to know how to handle it!"
                call gaming_harem_threesome_fuck from _call_gaming_harem_threesome_fuck
                if renpy.has_label("gaming_harem_achievement_2") and not game.flags.cheat:
                    call gaming_harem_achievement_2 from _call_gaming_harem_achievement_2
                "Afterwards, we're left a pile of tangled limbs and sweaty bodies."
                "There are clothes and joypads scattered across the sitting-room floor."
                "But in the middle of the chaos, we're all exchanging smiles and even blushing a little."
                "Kat's the first to start gathering up her clothes and getting dressed."
                "But as she does so, she stops to gently kiss [bree.name] and myself in turn."
                "Once she's done, [bree.name] and I share a knowing glance of our own."
                "Soon enough, we're all dressed and there's no trace of what just happened."
                "Only the fading afterglow and the memories that should last a whole lot longer."
                kat.say "Th...thank you, guys!"
                kat.say "I really think you helped with my game."
                kat.say "You want to do this again some time, maybe?"
                bree.say "Oh yeah, Kat!"
                if 'fafow' in DLCS:
                    $ Harem.join_by_name("gaming", "bree")
                bree.say "I'd love to have you again!"
                bree.say "I mean...I'd love to have you over to play games again..."
                "I can't help chuckling as [bree.name] struggles to correct herself."
                mike.say "Me too, Kat."
                mike.say "I think you really clicked with us today."
                mike.say "Maybe we could turn our gaming partnership into a threesome?"
                "Now it's [bree.name] and Kat's turn to giggle."
                "And from the way they're nodding, I think this thing could have potential!"
                scene bg black with dissolve
    return

label gaming_harem_threesome_intro(appointment=None):
    scene bg bedroom1
    show bree normal at right5
    show kat at center
    "We all know why we're here, in my room."
    "No need for foreplay or chitchat, we only have one thing in mind."
    call gaming_harem_threesome_fuck from _call_gaming_harem_threesome_fuck_1
    return

label gaming_harem_threesome_fuck:
    menu:
        "Fuck [bree.name]":
            "I take that as [bree.name]'s way of saying that she wants to take the lead."
            "Which makes perfect sense to me, as Kat does seem more than a little nervous."
            hide bree
            show kat zorder 1 at center, zoomAt(1.5, (540, 1040))
            show bree underwear topless zorder 2 at center, zoomAt(2, (740, 1340))
            "So as soon as I'm naked, I make straight for [bree.name]."
            "And she seems to pick up on my intentions without needing to be told."
            "In fact, [bree.name] plants a hand on my shoulder as I reach her."
            "And then she starts pushing me down onto my back."
            hide bree
            hide kat
            show bree kat cowgirl
            with fade
            bree.say "Not so fast, [hero.name]."
            bree.say "THIS is the only bit of you I want sitting up!"
            "To make her point, [bree.name] grabs hold of my cock."
            "And if there was any confusion remaining, she gives it a squeeze, just for good measure!"
            mike.say "Ah..."
            mike.say "Okay, [bree.name], Okay!"
            mike.say "I get it - you're the boss!"
            "Chuckle as [bree.name] nods, then straddles my waist."
            "Kat appears, looking over [bree.name]'s right shoulder."
            "She looks very interested in what's about to go down."
            "Interested enough to overcome her previous inhibitions too!"
            bree.say "Hey, [hero.name]!"
            bree.say "Eyes on the girl you're actually fucking, please!"
            "I smile and give [bree.name] a nod."
            "Then I take hold of her haunches."
            "And I pull her sharply downwards."
            "At the same time, I thrust my groin upwards too."
            menu:
                "Fuck her pussy":
                    "We're kind of initiating Kat into this kind of thing."
                    "So there's no sense in complicating matters more then we need to."
                    "That's why I make sure to angle my cock a little higher."
                    "Just high enough to ensure that it hits [bree.name]'s pussy on the way down."
                    "The moment the head of my cock slides along her lips, I know where this is going."
                    "Because [bree.name] gasps in the most sensual way imaginable."
                    bree.say "Mmm..."
                    bree.say "Oh, [hero.name]..."
                    bree.say "That feels SO good!"
                    "I nod as I push a little harder, loving the sensation too."
                    "And I can already feel the lips of [bree.name]'s pussy beginning to part."
                    show bree kat cowgirl orgasm vaginal
                    "As my cock sinks into her, [bree.name] inches her way down its length."
                    "She seems to gasp more with every inch along the way too!"
                    "[bree.name]'s hands are roaming all over herself this whole time."
                    "She seems to be tracing the shape of her entire body."
                    "Pausing to pay particular attention to sensual parts, [bree.name] captivates my eye."
                    show bree kat cowgirl pleasure
                    "She squeezes her naked breasts, pinching the nipples pretty hard."
                    "Then on of her hands slides down, over her belly and to her pussy."
                    "I manage to tear my eyes away from what [bree.name]'s doing for a moment."
                    "Which allows me to see that Kat's fascinated too."
                    "She's leaning in so close that her chin is almost on [bree.name]'s shoulder."
                    "And as I watch, she seems to overcome her shyness and reach out."
                    "It doesn't take long for Kat's hands to begin caressing [bree.name]'s body too."
                    "Soon enough four arms are roaming all over the place."
                    "And it makes [bree.name] look like a multi-limbed goddess in the throes of passion!"
                    bree.say "That's nice, Kat!"
                    bree.say "Please keep touching me?"
                    "[bree.name] has her eyes tightly shut by now."
                    "But I guess that Kat doesn't notice, as she nods eagerly."
                    "Her hand finds its way to [bree.name]'s pussy, rubbing at her clit."
                    "Which puts it right above my cock, thrusting in and out of her at the same time."
                    "Kat leans in ever closer, her head next to [bree.name]'s."
                    "And in the next moment their lips touch."
                    "At first it's nothing but a brief contact, them brushing together."
                    show bree kat cowgirl orgasm
                    "But then [bree.name] opens her mouth with a loud sigh."
                    "And the moment she does so, Kat kisses her with a passion."
                    "I watch as the kiss becomes more intense with each passing second."
                    "And it keeps on going, making me feel ever hotter."
                    "That is until [bree.name] breaks it off, panting desperately."
                    bree.say "Oh fuck..."
                    bree.say "I can't hold on..."
                    bree.say "I'm gonna cum!"
                    menu:
                        "Cum inside":
                            "I tighten my grip on [bree.name], feeling myself losing it as she does."
                            "When it happens, there's no way for her to escape."
                            show bree kat cowgirl creampie with vpunch
                            "I fill [bree.name] with everything that I have to give."
                            with vpunch
                            "She twitches atop me, helpless to resist."
                            show bree kat cowgirl pleasure with vpunch
                            "And then she falls back into Kat's open arms, utterly spent."
                        "Pull out":
                            "I tighten my grip on [bree.name], feeling myself starting to lose it as she does."
                            show bree kat cowgirl pleasure out
                            "There's barely enough time for me to pull my cock out of her before it happens."
                            show bree kat cowgirl cumshot with vpunch
                            "Then I shoot my load over [bree.name]'s belly and breasts."
                            with vpunch
                            "She twitches atop me, helpless to resist."
                            show bree kat cowgirl bodycum -cumshot with vpunch
                            "And then she falls back into Kat's open arms, utterly spent."
                "Fuck her ass":
                    "The whole idea of what we're doing here is pretty wild."
                    "And that's something Kat's going to have to cope with if she wants in."
                    "So I see no point in holding back in any way, shape or form."
                    "That's why I angle my cock further forward than usual."
                    "Just far enough to make sure the head of my cock hits [bree.name]'s asshole."
                    bree.say "Wha..."
                    bree.say "Oh, [hero.name]..."
                    bree.say "You bad, bad boy!"
                    "I smile, noting that [bree.name] never once told me to stop."
                    "So I take that as my permission to keep right on going."
                    show bree kat cowgirl anal orgasm
                    "And I start to pull her downwards."
                    bree.say "Mmm..."
                    bree.say "Oh, [hero.name]..."
                    bree.say "That feels SO good!"
                    "I nod as I push a little harder, loving the sensation too."
                    "And I can already feel [bree.name]'s ass beginning to surrender."
                    "As my cock sinks into her, [bree.name] inches her way down its length."
                    "She seems to gasp more with every inch along the way too!"
                    "[bree.name]'s hands are roaming all over herself this whole time."
                    "She seems to be tracing the shape of her entire body."
                    show bree kat cowgirl pleasure
                    "Pausing to pay particular attention to sensual parts, [bree.name] captivates my eye."
                    "She squeezes her naked breasts, pinching the nipples pretty hard."
                    "Then on of her hands slides down, over her belly and to her pussy."
                    "I manage to tear my eyes away from what [bree.name]'s doing for a moment."
                    "Which allows me to see that Kat's fascinated too."
                    "She's leaning in so close that her chin is almost on [bree.name]'s shoulder."
                    "And as I watch, she seems to overcome her shyness and reach out."
                    "It doesn't take long for Kat's hands to begin caressing [bree.name]'s body too."
                    "Soon enough four arms are roaming all over the place."
                    "And it makes [bree.name] look like a multi-limbed goddess in the throes of passion!"
                    bree.say "That's nice, Kat!"
                    bree.say "Please keep touching me?"
                    "[bree.name] has her eyes tightly shut by now."
                    "But I guess that Kat doesn't notice, as she nods eagerly."
                    "Her hand finds its way to [bree.name]'s pussy, rubbing at her clit."
                    "Which means [bree.name]'s getting action from both sides at once!"
                    "Kat leans in ever closer, her head next to [bree.name]'s."
                    "And in the next moment their lips touch."
                    "At first it's nothing but a brief contact, them brushing together."
                    show bree kat cowgirl orgasm
                    "But then [bree.name] opens her mouth with a loud sigh."
                    "And the moment she does so, Kat kisses her with a passion."
                    "I watch as the kiss becomes more intense with each passing second."
                    "And it keeps on going, making me feel ever hotter."
                    "That is until [bree.name] breaks it off, panting desperately."
                    bree.say "Oh fuck..."
                    bree.say "I can't hold on..."
                    bree.say "I'm gonna cum!"
                    menu:
                        "Cum inside":
                            "I tighten my grip on [bree.name], feeling myself losing it as she does."
                            "When it happens, there's no way for her to escape."
                            show bree kat cowgirl creampie with vpunch
                            "I fill [bree.name] with everything that I have to give."
                            with vpunch
                            "She twitches atop me, helpless to resist."
                            show bree kat cowgirl pleasure with vpunch
                            "And then she falls back into Kat's open arms, utterly spent."
                        "Pull out":
                            "I tighten my grip on [bree.name], feeling myself starting to lose it as she does."
                            show bree kat cowgirl pleasure out
                            "There's barely enough time for me to pull my cock out of her before it happens."
                            show bree kat cowgirl cumshot with vpunch
                            "Then I shoot my load over [bree.name]'s belly and breasts."
                            with vpunch
                            "She twitches atop me, helpless to resist."
                            show bree kat cowgirl bodycum -cumshot with vpunch
                            "And then she falls back into Kat's open arms, utterly spent."
                    $ bree.flags.anal += 1
        "Fuck Kat":
            "[bree.name] winks at me over Kat's shoulder as she says all of this."
            "And I take that to mean her telling me that I need to be ready."
            hide kat
            scene bg black
            show bree kat rev cowgirl
            with fade
            "I'm proven right as [bree.name] gently but firmly pushed the other girl backwards."
            "So I make sure that I'm there to close my arms around Kat as she moves."
            "Feeling the sensation of my cock against her ass, Kat yelps in surprise."
            kat.say "Whoa!"
            kat.say "Be nice to me, you guys, please!"
            kat.say "This is my first time with you!"
            bree.say "Don't worry, Kat."
            bree.say "Just trust us, okay?"
            "I hold my hands up as [bree.name] says this."
            "Just to show Kat that she's speaking for both of us."
            mike.say "Nice and gentle, Kat."
            mike.say "I promise."
            "Kat nods slowly, seeming to be mollified by our promises."
            "But as soon as she's reassured, [bree.name] gives my shoulder a shove."
            bree.say "Not so fast, [hero.name]."
            bree.say "THIS is the only bit of you I want sitting up!"
            "To make her point, [bree.name] grabs hold of my cock."
            "And if there was any confusion remaining, she gives it a squeeze, just for good measure!"
            mike.say "Ah..."
            mike.say "Okay, [bree.name], Okay!"
            mike.say "I get it - you're the boss!"
            "[bree.name] nods and smiles as she guides Kat to straddle me backwards."
            "And then she starts to lower the other girl down towards my waiting cock."
            "Sure, [bree.name] might be able to put herself firmly in charge up there."
            "But down here, it's a different story."
            "Down here, I'm the one that can see where everything is headed..."
            menu:
                "Fuck her pussy":
                    "But that doesn't mean that I'm going to be taking advantage of Kat."
                    "After all, this is her first time doing this kind of stuff with us."
                    "The last thing I want to do is act like a jerk and ruin it for her."
                    "Which is why I reach up and gently part Kat's pert little buttocks."
                    show bree kat rev cowgirl pleasure
                    "She lets out a pleasing little squeal as I do so."
                    show bree kat rev cowgirl normal
                    "And maybe she looks back over her shoulder to see what's going on."
                    "But if she does, I don't notice, as I'm too busy staring at what I've just discovered."
                    "There's her neat, inviting little pussy, right in front of me!"
                    show bree kat rev cowgirl vaginal pleasure
                    "And I don't hesitate to thrust my pelvis upwards to take advantage."
                    kat.say "Oh...oh my..."
                    kat.say "That feels SO good!"
                    "I nod eagerly at Kat's words, because it feels pretty good to me too."
                    "Every time I stroke the head of my cock along her lips I shudder."
                    "It feels so slick and warm, making me want to be in there like crazy."
                    bree.say "You're ready for it, Kat?"
                    bree.say "You can feel your pussy melting down there?"
                    show bree kat rev cowgirl normal
                    "I look up to see [bree.name] leaning in close, face-to-face with Kat."
                    "In fact, they're so close together that they must be touching."
                    "I can't see it, but I can imagine their breasts pressing together."
                    "I can picture their nipples rubbing against each other - getting hard!"
                    show bree kat rev cowgirl pleasure
                    "Without waiting for permission, I pull Kat firmly down."
                    "She yelps in surprise and there's a moment of resistance."
                    "But then she surrenders to me, and I almost plunge into her!"
                    kat.say "Ah...ah..."
                    kat.say "Ugh...oh fuck!"
                    show bree kat rev cowgirl normal
                    kat.say "Y...yeah..."
                    "From that moment on I'm not satisfied to simply lie back and watch."
                    "My cock is as deep into Kat as it'll go, and I'm coming alive."
                    "Any hesitation in me seems to vanish, and I'm only interested in fucking her."
                    "Kat is taken by surprise, the sensation of me thrusting into her taking over."
                    "And [bree.name] seems to be taken aback, thrown off by me asserting myself."
                    show bree kat rev cowgirl pleasure
                    "Kat bounces up and down on my cock, her buttocks slapping down on my stomach."
                    "And it's all that [bree.name] can do to keep squeezing and caressing the other girl."
                    kat.say "F...fuck..."
                    kat.say "S...so...big..."
                    show bree kat rev cowgirl normal
                    kat.say "Please...fuck me...harder!"
                    "I don't know if it's sympathy, jealousy or arousal that makes [bree.name] do it."
                    "But whatever the reason, she leans in as kisses Kat."
                    "And I don't mean that she plants a peck on her cheek either."
                    "[bree.name] opens her mouth and passionately kisses Kat."
                    "Unable to resist, Kat melts into the kiss too."
                    "I can see tongues writhing between their lips."
                    "And the air is filled with the desperate sound of their panting."
                    "In fact, I'm so enthralled by the sight that I don't realise what's happening to me."
                    "I can't hold on any longer - I'm going to cum!"
                    menu:
                        "Cum inside":
                            show bree kat rev cowgirl pleasure
                            "I make sure to keep a firm hold on Kat as I reach my climax."
                            "Sure, she squirms and wriggles in my grasp, but she's not going anywhere."
                            "And the sounds that she's making let me know that she's enjoying it too."
                            show bree kat rev cowgirl creampie with vpunch
                            "Kat gasps and wails as I shoot my entire load into her, deep and hard."
                            with vpunch
                            "And pretty soon I'm holding her up, rather than holding her in place."
                            show bree kat rev cowgirl normal with vpunch
                            "As she slumps forwards and onto [bree.name], utterly spent."
                        "Pull out":
                            show bree kat rev cowgirl pleasure
                            "I make sure to keep a firm hold on Kat as I reach my climax."
                            "Sure, she squirms and wriggles in my grasp, but she's not going anywhere."
                            "And the sounds that she's making let me know that she's enjoying it too."
                            "But at the last possible moment, I change the nature of the game."
                            show bree kat rev cowgirl out normal cumshot with vpunch
                            "I pull out of Kat, making her wail as I then shoot my load over her."
                            with vpunch
                            "It spatters over her back and then runs down onto her buttocks."
                            show bree kat rev cowgirl bodycum -cumshot with vpunch
                            "And she slumps forwards and onto [bree.name], utterly spent."
                "Fuck her ass":
                    "I could take the easy route here, play it safe for Kat's sake."
                    "But we're not messing around here - this is a damn threesome!"
                    "If she can't handle the stuff that comes along with that, we're wasting our time."
                    "Kat needs to learn if she can hang, or this is going to suck for all three of us!"
                    "With that in mind, I reach up and part her buttocks."
                    "She lets out a pleasing little squeal as I do so."
                    "And maybe she looks back over her shoulder to see what's going on."
                    "But if she does, I don't notice, as I'm too busy staring at what I've just discovered."
                    "There's her neat, inviting little ass, right in front of me!"
                    show bree kat rev cowgirl anal pleasure
                    "And I don't hesitate to thrust my pelvis upwards to take advantage."
                    kat.say "Oh...oh my..."
                    show bree kat rev cowgirl normal
                    kat.say "That's...that's my ass!"
                    "I can hear what Kat's saying, but I press on."
                    "Because by now the head of my cock is squeezing into her ass."
                    bree.say "You're ready for it, Kat?"
                    bree.say "You can feel your ass melting down there?"
                    "I silently thank [bree.name] for choosing that moment to get involved."
                    "Looking up, I see her leaning in close, face-to-face with Kat."
                    "In fact, they're so close together that they must be touching."
                    "I can't see it, but I can imagine their breasts pressing together."
                    "I can picture their nipples rubbing against each other - getting hard!"
                    show bree kat rev cowgirl pleasure
                    "Without waiting for permission, I pull Kat firmly down."
                    "She yelps in surprise and there's a moment of resistance."
                    "But then she surrenders to me, and I almost plunge into her!"
                    kat.say "Ah...ah..."
                    kat.say "Ugh...oh fuck!"
                    show bree kat rev cowgirl normal
                    kat.say "Y...yeah..."
                    kat.say "You're in my ass!"
                    "From that moment on I'm not satisfied to simply lie back and watch."
                    "My cock is as deep into Kat as it'll go, and I'm coming alive."
                    "Any hesitation in me seems to vanish, and I'm only interested in fucking her."
                    "Kat is taken by surprise, the sensation of me thrusting into her taking over."
                    "And [bree.name] seems to be taken aback, thrown off by me asserting myself."
                    show bree kat rev cowgirl pleasure
                    "Kat bounces up and down on my cock, her buttocks slapping down on my stomach."
                    "And it's all that [bree.name] can do to keep squeezing and caressing the other girl."
                    kat.say "F...fuck..."
                    kat.say "S...so...big..."
                    show bree kat rev cowgirl normal
                    kat.say "Please...fuck me...harder!"
                    "I don't know if it's sympathy, jealousy or arousal that makes [bree.name] do it."
                    "But whatever the reason, she leans in as kisses Kat."
                    "And I don't mean that she plants a peck on her cheek either."
                    "[bree.name] opens her mouth and passionately kisses Kat."
                    "Unable to resist, Kat melts into the kiss too."
                    "I can see tongues writhing between their lips."
                    "And the air is filled with the desperate sound of their panting."
                    "In fact, I'm so enthralled by the sight that I don't realise what's happening to me."
                    "I can't hold on any longer - I'm going to cum!"
                    menu:
                        "Cum inside":
                            show bree kat rev cowgirl pleasure
                            "I make sure to keep a firm hold on Kat as I reach my climax."
                            "Sure, she squirms and wriggles in my grasp, but she's not going anywhere."
                            "And the sounds that she's making let me know that she's enjoying it too."
                            show bree kat rev cowgirl creampie with vpunch
                            "Kat gasps and wails as I shoot my entire load into her, deep and hard."
                            with vpunch
                            "And pretty soon I'm holding her up, rather than holding her in place."
                            show bree kat rev cowgirl normal with vpunch
                            "As she slumps forwards and onto [bree.name], utterly spent."
                        "Pull out":
                            show bree kat rev cowgirl pleasure
                            "I make sure to keep a firm hold on Kat as I reach my climax."
                            "Sure, she squirms and wriggles in my grasp, but she's not going anywhere."
                            "And the sounds that she's making let me know that she's enjoying it too."
                            "But at the last possible moment, I change the nature of the game."
                            show bree kat rev cowgirl out normal cumshot with vpunch
                            "I pull out of Kat, making her wail as I then shoot my load over her."
                            with vpunch
                            "It spatters over her back and then runs down onto her buttocks."
                            show bree kat rev cowgirl bodycum -cumshot with vpunch
                            "And she slumps forwards and onto [bree.name], utterly spent."
    $ bree.sexperience += 1
    if Person.find("kat"):
        $ kat.sexperience += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
