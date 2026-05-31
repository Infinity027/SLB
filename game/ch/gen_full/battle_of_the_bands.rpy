init python:
    Activity(**{
    "name": "battle_of_the_bands_round_one",
    "duration": 4,
    "rooms": "studio",
    "conditions": [
        IsDone("first_gig"),
        MinDaysPlayed(45),
        IsDayOfWeek("5"),
        HeroTarget(
            MinStat("energy", 3),
            MinStat("hunger", 3),
            MinStat("grooming", 1),
            MinStat("fun", 0),
            MinFlag("band", 2),
            IsFlag("nextgig", False),
            ),
        PersonTarget(anna,
            Not(IsHidden()),
            ),
        PersonTarget(kleio,
            Not(IsHidden()),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            ),
        ],
    "icon": "guitar",
    "display_name": "Battle of the bands",
    "label": "battle_of_the_bands_round_one",
    "do_once": True,
    })

    Activity(**{
    "name": "battle_of_the_bands_round_two",
    "duration": 4,
    "rooms": "studio",
    "conditions": [
        IsDayOfWeek("5"),
        HeroTarget(
            MinStat("energy", 3),
            MinStat("hunger", 3),
            MinStat("grooming", 1),
            MinStat("fun", 0),
            MinFlag("band", 2),
            IsFlag("bobWon"),
            IsFlag("nextgig", False),
            ),
        PersonTarget(anna,
            Not(IsHidden()),
            ),
        PersonTarget(kleio,
            Not(IsHidden()),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            ),
        ],
    "icon": "guitar",
    "display_name": "Battle of the bands",
    "label": "battle_of_the_bands_round_two",
    "do_once": True,
    })

    Event(**{
    "name": "first_gig",
    "priority": 500,
    "label": "first_gig",
    "duration": 4,
    "conditions": [
        HeroTarget(
            IsActivity("practice_band"),
            IsFlag("gigready"),
            ),
        PersonTarget(anna,
            Not(IsHidden()),
            ),
        PersonTarget(kleio,
            Not(IsHidden()),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "battle_of_the_bands_lose",
    "priority": 1000,
    "label": "battle_of_the_bands_lose",
    "duration": 1,
    "conditions": [
        Or(
            IsDone("battle_of_the_bands_round_one"),
            IsDone("battle_of_the_bands_round_two")
            ),
        HeroTarget(
            IsFlag("bobWon", False),
            ),
        PersonTarget(anna,
            Not(IsHidden()),
            ),
        PersonTarget(kleio,
            Not(IsHidden()),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "battle_of_the_bands_win",
    "priority": 1000,
    "label": "battle_of_the_bands_win_restaurant",
    "duration": 1,
    "conditions": [
        IsDone("battle_of_the_bands_round_one", "battle_of_the_bands_round_two"),
        HeroTarget(
            IsFlag("bobWon"),
            ),
        PersonTarget(anna,
            Not(IsHidden()),
            ),
        PersonTarget(kleio,
            Not(IsHidden()),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    })

label battle_of_the_bands_lose:
    "No one spoke as much as a word after the contest was over and it was made official that the Deathless Harpies are among the losers."
    "Sasha, Anna, Kleio and I just trudged backstage and begin to pack up our gear, a cloud of disappointment hovering over us the whole time."
    "As hard as I try to keep from doing it, I can't help seeing and hearing the sound of the winners celebrating their victory as we left."
    "Afterwards, we loaded the van and drove to the Winchester, almost like we were all on autopilot."
    scene bg pub
    show kleio date sad at center, zoomAt(1.5, (300, 1040))
    show sasha date sad at center, zoomAt(1.5, (640, 1040))
    show anna b date dazed at center, zoomAt(1.5, (980, 1040))
    with dissolve
    "Sitting down at a vacant table, everyone exchanges glances that say more than words could hope to in that tense moment."
    "But then, one by one, everyone looks away, shaking their heads and muttering to themselves."
    show sasha normal
    "Only Sasha seems to be able to hold my eye for any longer, a helpless smile on her face as she does so."
    "Maybe it's because she's the one that I've known for the longest."
    "Or the one that I have the closest bond of friendship with thanks to us living together for."
    "Whatever the reason, when she shrugs, I feel oddly comforted by the gesture."
    "Once we've ordered a round of drinks with which to drown our sorrows, the air finally starts to clear."
    "But someone has to be the one to bite the bullet and break the silence."
    "And so we exchange furtive glances over the table, waiting to see who that will be..."
    if Harem.together(anna, sasha, kleio, name='band'):
        "But in the end, I just can't stand the dejected looks on the faces Sasha, Anna and Kleio."
        "They worked so hard and gave so much of themselves, it drives me crazy to see them like this."
        "And I realise that I feel so much love for them it's almost like my chest is going to burst."
        mike.say "This is going to sound like such a fucking cliche, I know it."
        mike.say "But you guys have got nothing to be ashamed of - nothing at all!"
        "Anna smiles sadly, cocking her head on one side."
        show anna happy
        anna.say "Aww...thanks, [hero.name]!"
        show kleio happy
        "But Kleio's own smile is by far more rueful and amused."
        kleio.say "That's sweet, Loverboy."
        show kleio annoyed
        show anna normal
        kleio.say "But it doesn't change the fact we lost!"
        "It's only now that Sasha chooses to throw herself into the conversation."
        sasha.say "No, Kleio - he's right."
        sasha.say "Sure, we all knew this was a big chance for the band."
        sasha.say "But it's not like we have to quit over losing."
        "I turn to look Kleio in the eye as Sasha makes her point."
        mike.say "You don't want to quit, do you, Kleio?"
        show anna surprised at vshake
        "At the mere mention of this, Anna pipes up in alarm."
        show fx question at right
        anna.say "What do you mean, [hero.name]?"
        anna.say "Kleio, you're not quitting, are you?!?"
        show anna cry
        anna.say "The band's not breaking up, is it?!?"
        "By now, Anna's practically wailing as she jumps to the worst possible conclusion."
        "And I have to admit that I feel a little guilty for kind of setting her on Kleio like that."
        "But I can already see the effect that it's having on her."
        show kleio angry
        kleio.say "No...no way, Anna!"
        show kleio normal
        kleio.say "I'm not quitting, okay?"
        sasha.say "Take a pill, Anna - the band's not splitting up."
        mike.say "We're stronger than this, guys."
        mike.say "And that's because we're more than just a band."
        show anna normal
        "I reach out and take hold of Anna and Kleio's hands as they're sitting to either side of me."
        "And taking the hint, they also join hands with Sasha too, linking us all in a circle."
        "Yeah, I know it's a pretty cheesy image."
        "But screw you, because it's just what we need right now."
        mike.say "Long live the Deathless Harpies!"
        show anna happy
        anna.say "Yay!"
        show kleio happy
        kleio.say "Fuck yeah!"
        show sasha happy
        sasha.say "Oh hell yeah!"
    elif Harem.together(anna, kleio, name='band') and not Harem.find(sasha, name='band'):
        "Sasha lets out a deep, rueful sigh as she takes a long pull on her drink."
        "She slams it back down onto the table, shaking her head as she does so."
        show sasha annoyed
        sasha.say "Damn it, guys."
        sasha.say "I was so sure we were gonna smash this thing."
        show anna annoyed
        anna.say "Yeah, Sasha, me too!"
        show kleio annoyed
        kleio.say "I don't get it either."
        kleio.say "I feel like would have wiped the floor with those guys a month back!"
        mike.say "Then what in the hell did we do wrong?"
        show sasha normal
        "Anna looks lost for an answer, and Kleio shakes her head too."
        "But it's then that I see a frown growing in Sasha's face."
        show sasha annoyed
        sasha.say "Maybe it wasn't something we did wrong."
        sasha.say "What if it was something that we changed?"
        "Anna and Kleio look up at Sasha, but then follow her gaze."
        "And as she's been looking at me the whole time, I find myself being scrutinised by all three at once."
        mike.say "What are you trying to say, Sasha?"
        mike.say "Are you saying that this was my fault?"
        show anna surprised
        anna.say "Sasha, is that really true?"
        kleio.say "Yeah, Sasha - what happened to us being a team, huh?!?"
        show sasha normal
        "Suddenly finding herself under attack, Sasha holds her hands up in a defensive gesture."
        sasha.say "I'm not blaming [hero.name], not specifically."
        sasha.say "But you've got to admit, the band's changed since he joined."
        sasha.say "I can't put my finger on just what it is."
        show sasha annoyed
        sasha.say "There's just something between the three of you."
        sasha.say "Like you're united against me, you know?"
        "There's no way to disguise the furtive glances that Anna, Kleio and I exchange at this."
        "But I guess it answers the question as to which is stronger - the band or our relationship with each other!"
        mike.say "I think you're just shaken up form us losing, Sasha."
        mike.say "It's making everything seem ten times worse!"
        kleio.say "Yeah, Sasha - we're all screwed up right now."
        anna.say "Maybe we should sleep together?"
        show anna blush at vshake
        anna.say "I mean sleep on it - maybe you should sleep on it!"
        show sasha shocked
        "Sasha looks puzzled at this, and Kleio glares daggers at Anna as she blushes."
        "Trying to avert complete disaster and the implosion of the band, I raise my glass."
        mike.say "Long live the Deathless Harpies!"
        show kleio normal
        show sasha dazed
        show anna normal
        "All three of them look at me, and then hastily raise their glasses too."
        show kleio annoyed
        show anna annoyed
        "But as we share the toast, all I can see is the guilt in Anna and Kleio's eyes."
        show sasha annoyed
        "And what I think is confusion turning into suspicion in Sasha's."
    elif sasha.is_girlfriend and not anna.is_girlfriend and not kleio.is_girlfriend:
        show kleio normal
        "Kleio smiles at me, raising her glass in a mocking salute."
        "I can see the look in her eyes, the one that tells me I'm about to get both barrels."
        kleio.say "Here's to you, Loverboy."
        kleio.say "At least there's one thing your right hand's still good for!"
        "I roll my eyes, more than used to being the target of Kleio's acid tongue."
        "I was already kind of expecting her to single me out as the problem."
        "As the newest member of the band and a guy to boot, it was probably inevitable."
        sasha.say "Look who's talking, Kleio."
        show sasha annoyed
        sasha.say "If you spent more time plucking your bass than your pussy, it might have turned out different!"
        "Sasha's retort is so sudden and unexpected that it takes me by completely by surprise."
        show anna surprised
        show kleio surprised
        "I can see that it's had pretty much the same effect on Anna and Kleio too!"
        anna.say "Sasha, did you just..."
        anna.say "Did you just say Kleio..."
        anna.say "That she plays with herself too much?!?"
        "Sasha doesn't take her eyes off of Kleio for as much as a second."
        "But she still nods in answer to Anna's question."
        show anna dazed
        sasha.say "Yeah, Anna - that's exactly what I did."
        sasha.say "I don't see where she gets off on blaming this all on [hero.name]."
        show kleio annoyed
        "I can already see Kleio getting ready to fire back and defend herself."
        "And while I appreciate Sasha being in my corner, I can't let the band fall apart over this."
        mike.say "Whoa, Sasha - just wait a minute."
        "Suddenly, all eyes are on me."
        "I swallow nervously, feeling like I'm being eyed up by a pride of angry lionesses."
        mike.say "Thanks for the vote of confidence, Sasha."
        mike.say "But Kleio has a right to be pissed off, we all do."
        mike.say "I just don't think that fighting and pointing the finger is going to help."
        mike.say "We're a band, aren't we?"
        mike.say "We either win or lose, but we do it together."
        mike.say "Otherwise, what's the damn point of it all?"
        show kleio sad
        show sasha sad
        "Sasha and Kleio fall silent at this, my words evidently sinking in."
        "They look awkwardly at each other for a moment, then both nod."
        kleio.say "Sorry, Loverboy."
        sasha.say "You're right - we need to stick together."
        "Anna makes the three of us jump a second later, raising her glass and cheering."
        show anna happy
        anna.say "Yay - Deathless Harpies forever!"
        mike.say "Long live the Deathless Harpies!"
        show kleio punk
        kleio.say "Fuck yeah!"
        show sasha happy
        sasha.say "Oh hell yeah!"
    elif anna.is_girlfriend and not sasha.is_girlfriend and not kleio.is_girlfriend:
        show kleio normal
        "Kleio smiles at me, raising her glass in a mocking salute."
        "I can see the look in her eyes, the one that tells me I'm about to be on the receiving end."
        kleio.say "Here's to you, Loverboy."
        kleio.say "At least there's one thing your right hand's still good for!"
        "I roll my eyes, more than used to being the target of Kleio's acid tongue."
        "I was already kind of expecting her to single me out as the problem."
        "As the newest member of the band and a guy to boot, it was probably inevitable."
        show anna angry
        anna.say "Oh, shut your fucking mouth, Kleio!"
        anna.say "You go around saying you hate everyone with a cock."
        anna.say "But you're still the biggest dick I've ever seen!"
        show anna annoyed
        "Anna's retort is so sudden and unexpected that it takes me by completely by surprise."
        "I can see that it's had pretty much the same effect on Sasha and Kleio too!"
        show kleio surprised
        show sasha surprised
        sasha.say "Whoa, Anna - don't spare her feelings!"
        "Anna doesn't take her eyes off of Kleio for as much as a second."
        "She only lets out a huffy snort in answer to Anna's question."
        show anna angry
        anna.say "She deserves it, Sasha."
        anna.say "She bangs on about solidarity and respect."
        anna.say "But she's always taking a shot at, [hero.name]."
        anna.say "It's not fair, and I'm sick of it!"
        show kleio angry
        show anna annoyed
        "I can already see Kleio getting ready to fire back and defend herself."
        "And while I appreciate Anna being in my corner, I can't let the band fall apart over this."
        mike.say "Whoa, Anna - just wait a minute."
        "Suddenly, all eyes are on me."
        "I swallow nervously, feeling like I'm being eyed up by a pride of angry lionesses."
        mike.say "Thanks for the vote of confidence, Anna."
        mike.say "But Kleio has a right to be pissed off, we all do."
        mike.say "I just don't think that fighting and calling each other names is going to help."
        mike.say "We're all members of this band, aren't we?"
        mike.say "Win or lose, we do it together."
        mike.say "If not, then there's no point, yeah?"
        "Anna and Kleio fall silent at this, my words evidently sinking in."
        "They look awkwardly at each other for a moment, then both nod."
        show kleio sad
        kleio.say "Sorry, Loverboy."
        show anna normal
        anna.say "You're right, [hero.name] - we should stick together."
        "Sasha makes the three of us jump a second later, raising her glass and offering a toast."
        show anna happy
        anna.say "Deathless Harpies forever!"
        mike.say "Long live the Deathless Harpies!"
        show kleio punk
        kleio.say "Fuck yeah!"
        show sasha happy
        sasha.say "Ooh, yay!"
    elif kleio.is_girlfriend and not anna.is_girlfriend and not sasha.is_girlfriend:
        show kleio normal
        "Before anyone else can get a word in edgeways, Kleio raises her glass."
        "She salutes the other two girls, but there's a crooked smile on her face."
        "And I recognise it instantly as the one that means they're in the firing line."
        show kleio annoyed
        kleio.say "Here's to my beloved bandmates - the millstones around my fucking neck!"
        "I was expecting Kleio to attack Sasha and Anna, but not to go straight for the jugular."
        "The other two girls look equally as shocked, staring at her in a stunned silence."
        "But even so, Kleio's not done yet!"
        show kleio angry
        kleio.say "Anna, buy some elevator shoes next time, you damn dwarf!"
        show anna surprised
        kleio.say "And you, Sasha, maybe you should stop it with the kinky shit, huh?"
        show sasha surprised
        kleio.say "All that getting tied up and whipped seems to be cutting off the oxygen to your brain!"
        "I grimace as Kleio spits her venom at Sasha and Anna, expecting my turn to come next."
        "But when it doesn't, I'm left wondering what the hell's going on."
        "As the newest member of the band, surely I'm the easiest target for her rage?"
        "It's only then that I realise what's really happening here."
        "Kleio's blistering the others to keep them from turning the blame on me!"
        "The revelation actually makes me feel pretty filled with adoration for her."
        show anna annoyed
        show sasha annoyed
        "But, as usual, it's an example of Kleio using a sledgehammer to crack a nut."
        "At this rate, she'll spilt the band up and lose her two best friends."
        "And all before we've even finished the first round of drinks too!"
        mike.say "Whoa, Kleio, hold on there!"
        mike.say "Emotions are running high right now."
        mike.say "Maybe this isn't the time to be handing out blame, huh?"
        show kleio sad
        "Kleio spins around to look me in the eye, and I can see the hurt she's feeling."
        "In her own way, she's trying to protect me."
        "And now it looks like I'm throwing her under the bus!"
        mike.say "Sure, you have a right to be pissed off, we all do."
        mike.say "I just don't think that attacking each other is going to solve anything."
        mike.say "Everyone here is a vital part of this band."
        mike.say "Win or lose, we do it together and we support each other whatever the result."
        mike.say "If we haven't got each other's backs, then what chance do we have?"
        show kleio annoyed
        "Kleio falls silent at this, my words evidently sinking in."
        show anna normal
        show sasha normal
        "Sasha and Anna look at me, the gratitude they're feeling for my efforts plain to see."
        "And after a moment of contemplative silence, Kleio looks their way again."
        show kleio sad
        kleio.say "Sorry, Sasha."
        kleio.say "Sorry, Anna."
        kleio.say "You're right, [hero.name] - we should stick together."
        sasha.say "It's okay, Kleio - I know how much you wanted to win this thing."
        anna.say "Yeah, Kleio, we all did!"
        show kleio normal
        "Kleio smiles at the reassurances of her friends and bandmates."
        "Then she raises her glass and offers up a toast."
        show kleio happy
        kleio.say "Deathless Harpies forever!"
        mike.say "Long live the Deathless Harpies!"
        show sasha happy
        sasha.say "Fuck yeah!"
        show anna happy
        anna.say "Ooh, yay!"
    else:
        show kleio normal
        "Kleio lifts her glass, making a salute while she smiles at me."
        "But there's a look in her eye that tells me her intentions are not so sincere."
        kleio.say "Here's to you, Loverboy."
        "I roll my eyes, more than used to being the target of Kleio's acid tongue."
        "Sasha lets out a rueful laugh for much the same reason, not willing to take the bait."
        "Anna, on the other hand, is a different matter altogether."
        show anna surprised
        anna.say "Kleio, are you saying it's [hero.name]'s fault we lost?"
        anna.say "Because if you are, that's really mean!"
        show kleio annoyed
        kleio.say "All I'm saying is that he's the only thing we changed recently."
        anna.say "No way, Kleio - [hero.name]'s like a lucky charm!"
        show kleio normal
        "Kleio lets out an evil chuckle at this, amused by the other girl's innocence."
        kleio.say "Yeah, sure thing Anna."
        kleio.say "Only thing is, the luck's the bad kind!"
        show anna angry
        anna.say "Hey, Kleio!"
        anna.say "Quit saying nasty stuff!"
        show sasha angry
        sasha.say "She's right, Kleio."
        sasha.say "We're a band, and that means we stick together."
        sasha.say "Either we win as a band or we lose as one."
        anna.say "Yeah, Sasha - one for all and all for one."
        anna.say "Say...wasn't that an Ozzy lyric or something?"
        show kleio annoyed
        "Kleio shakes her head, clearly not convinced by the lecture that's just been delivered."
        "But she finally seems to be willing to let the matter drop."
        show kleio normal
        "I can guess this from the fact that she doesn't snipe straight back."
        "That and the way she lets Anna's latest ditzy comment go without answer."
        mike.say "Erm..."
        mike.say "I appreciate you guys standing up for me, really I do."
        mike.say "And I think I understand why Kleio feels the way she does too."
        mike.say "But would you mind letting me speak for myself?"
        show anna normal
        show sasha normal
        "Kleio huffs at this, Anna looks surprised, and Sasha just waits for me to say my piece."
        mike.say "I think we're in danger of seeing this as a glass half empty situation, you know?"
        kleio.say "Glass brim-full of piss, more like!"
        anna.say "Yeah, [hero.name], we did lose."
        "Only Sasha holds her tongue."
        mike.say "Sure we lost, Anna."
        mike.say "But we still played well in front of a big crowd tonight."
        sasha.say "[hero.name]'s right, we should be thankful for the exposure we got."
        sasha.say "So we lost - so what?"
        sasha.say "Are you gonna call it quits?"
        show sasha happy
        sasha.say "Because I'm not, no way!"
        "Anna and Kleio are silent for a moment, but then they raise their glasses to Sasha."
        show anna happy
        anna.say "Not me!"
        show kleio happy
        kleio.say "Fuck no!"
        "All three of them look at me, and I hastily raise my own glass too."
        mike.say "Long live the Deathless Harpies!"
    return

label battle_of_the_bands_win_restaurant:
    $ game.room = "restaurant"
    scene bg street at blur(16), dark with dissolve
    "I know that it's just a local competition, a chance for bands that play on the side to show off their talent."
    "But from the very moment they announce us as the winners, I feel like we just came out on top of the entire world."
    "And I can tell that the others are feeling pretty much the same way too as we cheer, hug and congratulate ourselves."
    "What happens after the whole thing is over becomes a blur of being patted on the back as we pack up our gear."
    "Which means that I can hardly keep track of events, and soon find myself sitting in a restaurant, my head spinning."
    scene bg restaurant with dissolve
    "All I can remember is some vague mention of us all going out for a celebratory meal and nodding in agreement."
    "Truth be told, there's been more than one bottle passed around between us by now."
    "And I can already feel the effects on my empty, nerve-cramped stomach."
    "Normally I'd have tried to reign it in, to fill my stomach before drinking so much."
    "But the I'm still being carried along on a wave of positive emotion."
    "So there's no chance of me being able to snap out of it and start acting sensibly now."
    "Plus there's all of the chat and banter being exchanged around the table too."
    "That's more than enough to make me throw caution to the wind and just party like there's no tomorrow."
    "And any hope that I had of realising just how drunk I am disappears a moment later."
    "That's when Kleio makes a sound of disgust, tossing her menu down on the table."
    show kleio date at center, zoomAt(1.5, (300, 1040))
    show sasha date at center, zoomAt(1.5, (640, 1040))
    show anna b date at center, zoomAt(1.5, (980, 1040))
    with dissolve
    kleio.say "Urgh!"
    kleio.say "This shit's too fancy."
    kleio.say "We should have just grabbed a kebab and hit a club already!"
    show anna annoyed
    "Anna wrinkles her nose in obvious disgust at the suggestion."
    anna.say "Eww!"
    anna.say "I don't like those awful things."
    anna.say "Someone once told me they're made from an elephant's leg!"
    show kleio happy
    show sasha happy
    show anna dazed
    "Sasha and Kleio instantly burst into laughter at this, and I barely manage to keep from doing the same."
    anna.say "Hey, you guys - what's so funny?!?"
    show sasha normal
    sasha.say "It's just meat they scrape off of the carcass, Anna."
    sasha.say "That and a ton of fatty gristle."
    show kleio normal
    kleio.say "Yeah, dummy, elephants are like a seriously endangered species."
    kleio.say "You can't buy ivory - so how are kebab joints going to get an elephant's leg?!?"
    show anna annoyed
    "Anna scowls, crossing her arms over her chest."
    "I should probably step in to save her from the other girls."
    "But she's so tiny that her rage makes her look pretty funny."
    show anna angry
    anna.say "I never said that I believed it!"
    mike.say "Don't worry, Anna."
    mike.say "They're just fucking with you!"
    show anna surprised
    "Anna looks at me, the anger fading from her eyes to be replaced with surprise."
    anna.say "Really, [hero.name]?"
    "She turns to the others, giving them the same wide-eyed stare as she does so."
    anna.say "Is that true?"
    anna.say "Are you guys joking around?"
    show sasha happy
    sasha.say "Oh, Anna - you're so easy to wind-up!"
    show kleio happy
    kleio.say "Yeah - lighten up, dum-dum!"
    "Well, I suppose that's as close to an apology as you're likely to get from Kleio!"
    "Picking up my own menu, I clear my throat to get the attention of the others."
    mike.say "Ahem!"
    mike.say "Maybe we should just get on and order something?"
    mike.say "I'm starving right now, and the club's waiting!"
    show kleio normal
    show anna normal
    show sasha normal
    "This gets a round of nods from the girls."
    "And soon enough they're studying their menus in an intense, drunken silence."
    "The waiter stands there, taking our orders while trying not to look annoyed at just how drunk we are."
    "But even though we've finally managed to decide what we're eating, it's not as if we stop drinking."
    "Which means that almost as soon as the food arrives and we start to eat, it's cancelled out by more booze."
    if Harem.together(anna, sasha, kleio, name='band'):
        "I guess it was going to happen, sooner or later."
        "For one thing, we just won a major competition as a band."
        "And we're also kind of more than just bandmates too."
        "So what chance was there of us being able to keep our hands off of each other for too long?"
        "No one's crazy enough to do anything over the table."
        "But underneath is a different story altogether."
        "Before we're even halfway through our meals, we all have one hand under there."
        "And I can already feel at least one foot that's slipped out of its shoe and is massaging my groin."
        "It all seems to be going pretty well, everyone having fun and shooting knowing looks."
        "But then I walk my hand up Anna's thigh, getting dangerously close to her crotch."
        show anna surprised at vshake
        anna.say "OH SHIT!"
        "Her cry of surprise and alarm is enough to cut through the ambient noise of the restaurant."
        "And in that moment, everything seems to stop dead, all eyes falling on as one."
        "No one utters as much as a single word, all staring down at our plates."
        "Time seems to drag on forever, but eventually people begin to lose interest."
        "The sound of polite conversation fills the air once more."
        "At last, it looks like we're in the clear."
        show anna normal
        anna.say "Oops..."
        anna.say "Sorry, guys!"
        mike.say "I'm sorry too, Anna."
        mike.say "That was my hand!"
        show anna blush
        "Anna smiles and blushes at this admission."
        anna.say "I gotta say, I didn't shout out because I hated it, [hero.name]!"
        kleio.say "Thanks for that public service announcement, Anna!"
        sasha.say "Whatever, guys - I think we got off lightly there."
        show sasha flirt
        sasha.say "Maybe we should put a brake on things like that."
        sasha.say "At least until we're out of here?"
        "I nod, wanting the action to keep going, but afraid of causing a scene in the restaurant."
        mike.say "Sasha's right - we should finish off the meal and hit a club."
        "To my surprise, it's Anna that starts waving her hand to call for the bill."
        "I think the waiter just bites his tongue and smiles on through it all."
        "That said, he does seem to take great pleasure in slamming the door behind us."
        play sound door_slam
        "Not that anyone but me notices, as the girls are already noisily hailing a taxi across the street."
    elif Harem.together(anna, kleio, name='band') and not Harem.find(sasha, name='band'):
        "I've been aware the whole night that there are four of us in this band."
        "But also that only three of us are more than mere bandmates and friends."
        "And then there's the mood of celebration, coupled with the amount of booze we've already consumed."
        "I suppose it's inevitable that Anna, Kleio and I are going to turn our minds to it sooner or later."
        "First Anna and then Kleio turn their attention away from whatever Sasha is saying."
        show kleio seductive
        show anna wink
        "Both of them leaning in towards me, casting glances between themselves that are visibly lewd in nature."
        sasha.say "Ahem..."
        sasha.say "I know that [hero.name]'s the new face around here."
        show sasha annoyed
        sasha.say "But what the hell am I - chopped fucking liver?!?"
        "Almost as one, Anna, Kleio and I stop what we're doing and look at Sasha across the table."
        show anna normal
        anna.say "Huh...oh, sorry."
        mike.say "Ah, yeah...sorry about that, Sasha."
        show kleio normal
        kleio.say "Alright, alright - sorry, spoilsport!"
        "Sasha rolls her eyes at Kleio's backhanded apology."
        show sasha normal
        sasha.say "Spoilsport or not, Kleio - I'm a part of the band too."
        sasha.say "Aren't we supposed to be out celebrating something we just did together?"
        "I can feel the urge to play peacemaker growing inside of me."
        "Sasha's right, we just did something amazing."
        "So it'd be doubly crazy to let the band implode straight after that."
        mike.say "Sasha's right, guys."
        mike.say "We should be partying together, okay?"
        "Anna nods almost instantly."
        "But Kleio takes a couple more seconds before she gives a resentful nod of her own."
        "Sasha nods at this, mollified for the moment, but clearly still far from happy."
        sasha.say "Whatever - I'm going to use the bathroom."
        sasha.say "We should hit a club when I get back."
        sasha.say "Who knows, maybe a change of scene will do us all some good?"
        hide sasha with moveoutright
        "Almost as soon as she's out of earshot, I turn my attention to Anna and Kleio."
        mike.say "You guys, we really need to hold off getting hot and heavy while Sasha's here."
        mike.say "Just reign it in until we can all be alone together, okay?"
        mike.say "Then we can make up for it and really have a good time."
        anna.say "Okay, [hero.name], I'll try my best."
        show kleio annoyed
        kleio.say "Urgh..."
        kleio.say "Alright, alright - I'll just simmer away for the rest of the night!"
        show kleio normal
        "I nod as I call for the bill and we get up to leave."
        "Sasha comes back from the bathroom a moment later."
        "She walks straight outside and begins trying to hail a taxi."
        "But Anna and Kleio still keep a tight hold of my arms."
        "As if they're afraid of losing me before I can honour my side of the bargain..."
    elif sasha.is_girlfriend and not anna.is_girlfriend and not kleio.is_girlfriend:
        "It doesn't take me long to tune out whatever Anna and Kleio are talking about."
        "I'm not doing it to be rude, but in my drunken state, I only have eyes for Sasha."
        "And the feeling seems to be mutual, as she leans in close to me, ignoring them too."
        show sasha flirt
        sasha.say "You played your heart out tonight, [hero.name]."
        sasha.say "We couldn't have won this thing without you."
        "I shrug and shake my head, trying as best I can to look humble."
        "But the truth is that Sasha's compliments are going to my head almost as fast as the booze."
        mike.say "Nah, you'd have aced it, Sasha."
        mike.say "You're pretty amazing, even without me."
        "She smiles at this in the same way as I did when she complimented me just now."
        "And she giggles in that way she only does when seriously drunk."
        show sasha happy
        sasha.say "No, you're amazing."
        sasha.say "And playing guitar's not all that you're good at either."
        "By now, Sasha's almost whispering straight into my ear."
        sasha.say "But one thing I'm better at is giving head!"
        show sasha flirt
        sasha.say "And I could go under the table right now..."
        "Even as drunk as I am right now, I'm still pretty sure that's not a good idea!"
        mike.say "Ah, no, Sasha..."
        mike.say "You don't need to prove it - I believe you!"
        sasha.say "I mean it, [hero.name]."
        sasha.say "It's no trouble..."
        mike.say "How about this, Sasha - you show me later, when we're alone?"
        sasha.say "Hmm..."
        show sasha normal
        sasha.say "Okay, [hero.name] - but you have to promise!"
        "As soon as we're all finished eating, I call for the bill and we get up to leave."
        "Anna and Kleio begin noisily hailing a taxi."
        "But Sasha clings to my arm, as if she's afraid of losing me before she can fulfil her promise..."
    elif anna.is_girlfriend and not sasha.is_girlfriend and not kleio.is_girlfriend:
        "I don't know if we were all talking to each other before we started eating."
        "But soon enough I lose track of what Sasha and Kleio are saying as I tune into Anna alone."
        "She's pretty much ignoring the other two girls, giving me all of her attention."
        "And as I'm every bit as drunk as she is, I'm more than happy to let her."
        show anna dazed
        anna.say "Mmm..."
        anna.say "You were SO good out there tonight, [hero.name]."
        mike.say "Ah...thanks, Anna."
        mike.say "You were pretty hot on the drums too!"
        "Anna shakes her head at this, as if I'm not understanding her."
        "You know, that way a drunk can get hung up on the tiniest subtlety."
        anna.say "No, [hero.name]."
        anna.say "I mean you were REALLY GOOD to look at!"
        "Anna's voice drops down to what her intoxicated brain thinks is a hushed tone."
        "But when she next speaks, it's still loud enough to be heard without any serious effort."
        anna.say "I mean you looked HOT, [hero.name]!"
        anna.say "You made me hot too!"
        mike.say "Okay, okay, Anna!"
        mike.say "I hear what you're saying..."
        "I feel Anna's hand on my thigh, sliding up to my groin."
        "She squeezes my cock through the fabric of my jeans, making me yelp in surprise."
        show anna blush
        anna.say "I almost couldn't keep my mind on the drumming."
        anna.say "All the time I was thinking about having this inside of me!"
        anna.say "I still can't..."
        "Anna leans in closer still, and now she really is whispering into my ear."
        show anna dazed
        anna.say "[hero.name]..."
        anna.say "I want you to fuck me under the table!"
        "I may be pretty drunk right now, but I still know a bad idea when I hear one!"
        mike.say "Ah, no, Anna..."
        mike.say "Let's wait until later, when it's just us, okay?"
        anna.say "Aww..."
        show anna normal
        anna.say "Okay, [hero.name] - but you have to promise!"
        "As soon as we're all finished eating, I call for the bill and we get up to leave."
        "Sasha and Kleio begin noisily hailing a taxi."
        "But Anna clings to my arm, as if she's afraid of losing me before she can fulfil her promise..."
    elif kleio.is_girlfriend and not anna.is_girlfriend and not sasha.is_girlfriend:
        "Once we've started eating, the conversation is sporadic between mouthfuls."
        "But I'm pretty sure that it involves everyone around the table."
        "Well, that is we're all either chipping in with full mouths."
        "Or else we're nodding and then shaking our head in agreement with what's being said."
        "But soon enough, Sasha and Anna are locked in a conversation together."
        "Which leaves Kleio and myself to indulge our mutual affections without interruption."
        "She gives me a playful jab in the ribs with her elbow, pushing up against me as she does so."
        show kleio seductive
        kleio.say "You did good out there today, Loverboy."
        kleio.say "REAL good..."
        "I smile and let out a bashful chuckle, trying to sound humble."
        "Though the truth is that compliments for Kleio are pretty rare."
        "And she's got me hooked the very moment she starts to stroke my ego."
        mike.say "Ah...I tried my best, Kleio."
        mike.say "I think we just clicked as a band, you know?"
        show kleio blush
        kleio.say "Don't be shy, [hero.name]."
        kleio.say "You played with skills up there."
        kleio.say "All the time I wanted you to be playing me instead!"
        "It's now that I realise Kleio has her hand on my cock."
        "And she's stroking it in the most suggestive manner possible."
        show kleio seductive
        kleio.say "Say..."
        kleio.say "You wanna sneak off to the bathroom, or maybe the alley round back?"
        "I'm so close to saying yes that I can feel the words forming on my tongue..."
        show anna happy
        anna.say "All done - let's go hit a club!"
        show sasha happy
        sasha.say "Hell yeah, that sounds good!"
        show kleio annoyed -blush
        "Kleio rolls her eyes in frustration at her plans being foiled."
        mike.say "Don't worry about it, Kleio."
        mike.say "Let's wait until later, when it's just us, okay?"
        kleio.say "Okay, [hero.name] - but you better be as good as your word!"
        "I nod as I call for the bill and we get up to leave."
        "Sasha and Anna begin noisily hailing a taxi."
        "But Kleio keeps a tight hold of my arm."
        "And she clutches it if she's afraid of losing me before I can honour my side of the bargain..."
    else:
        "One by one, we all seem to forget how a knife and fork are supposed to work."
        "Whenever someone drops food onto the table or the floor, it's the funniest thing ever."
        "Soon enough, we're all trying to feed each other a little bit of this and that from our plates."
        "And one drunk trying to feed another from a wobbly fork is apparently more amusing by a factor of ten."
        show kleio normal blush
        show anna blush
        show sasha blush
        "On top of this, what do you think happens when a drunk laughs with a mouthful of food?"
        "I don't see who it is that sprays their meal over the table."
        "But it's not as though the identity of the culprit really matters that much."
        mike.say "Ah, guys."
        mike.say "I think we need to ask for the bill!"
        "As much as I try to keep my voice down, I still end up almost shouting the words."
        "And of course, as soon as I do, everyone gets furtive and looks over their shoulder at the waiter."
        show anna annoyed
        anna.say "Ooh...I hope they're not mad at us!"
        kleio.say "Ah, screw them - they're not the boss of us!"
        "Thankfully, Sasha seems to sense the seriousness of the situation."
        sasha.say "[hero.name]'s right, guys."
        sasha.say "Let's get out of here and go somewhere more fun!"
        "With that, we proceed to get up and begin to leave."
        "But for all I just said, we still manage to make enough noise to raise the dead."
        "And in the end, I think the waiter just bites his tongue and smiles on through it all."
        "That said, he does seem to take great pleasure in slamming the door behind us."
        play sound door_slam
        "Not that anyone but me notices, as the girls are already noisily hailing a taxi across the street."
    call battle_of_the_bands_win_nightclub from _call_battle_of_the_bands_win_nightclub
    return

label battle_of_the_bands_win_nightclub:
    scene bg taxi car with fade
    "Once the four of us have finally managed to find a taxi driver willing to have us in his cab, we clamber eagerly inside."
    "And when asked just where in the hell we're going, it shouldn't come as any surprise that we all demand the same thing at the same time."
    show bg street at dark
    show kleio date at center, zoomAt(1.5, (980, 1040))
    show anna b date at center, zoomAt(1.5, (640, 1040))
    show sasha b date at center, zoomAt(1.5, (300, 1040))
    with dissolve
    "Taxi driver" "So, where to?"
    show kleio annoyed
    kleio.say "Where do you think, dummy?"
    kleio.say "The fucking opera?!?"
    anna.say "Yeah, we wanna go somewhere that plays metal."
    show anna happy
    anna.say "Plays it loud enough to make your ears bleed!"
    show sasha happy
    sasha.say "Now that's what I'm talking about!"
    "Having had three girls bellowing in his face, the taxi driver looks at me with a pleading look on his face."
    "It's not like he's being sexist or anything, he just looks like he's hoping I might be a tad more sober."
    mike.say "Just take us to the club, okay?"
    "He nods, a look of genuine relief on his face at the prospect of an actual destination."
    "And also probably thanks to the fact he knows just how long it'll be until he's finally rid of us."
    scene black
    play sound car_door
    pause 0.4
    play sound car_door
    pause 0.2
    play sound car_door
    scene bg street with fade
    with vpunch
    "Pretty soon the taxi pulls up outside of the club and we pile out onto the pavement."
    "The driver takes the fare and drives off without delay."
    "And I wonder if it'll be enough to offset the fines he's going to get in the post."
    "Because he must have passed at least half-a-dozen speed cameras on the way here at well above the limit."
    show kleio date at left5
    show sasha date
    show anna date at right5
    with dissolve
    "As soon as we're in the queue, all thought of anything but the club is instantly forgotten."
    "It's as long as usual, and I hope that we don't actually sober up before we get into the place."
    "But then a thought occurs to me, and I start desperately rummaging in my pockets."
    sasha.say "Hey, [hero.name], stop that!"
    show sasha annoyed
    sasha.say "You really should have gone back at the restaurant, you know?"
    anna.say "Huh...what's up?"
    kleio.say "Whoa, looks like Loverboy's playing with himself in public!"
    "I look up at the three of them, confused and more than a little annoyed."
    mike.say "What the..."
    mike.say "No, I don't need to piss, damn it!"
    mike.say "We have VIP passes, remember?!?"
    show sasha happy
    "Sasha's the first one to get it, nodding with a smile on her face."
    sasha.say "Oh yeah - the goodies bags we got at the Battle of the Bands!"
    show anna happy
    anna.say "We have VIP passes - YAY!"
    show fx question at left5
    kleio.say "We do?"
    kleio.say "So why are we standing in line with these losers?!?"
    "I hear the chorus of objections Kleio's words cause, even if she doesn't."
    "And so brandishing the rather crumpled passes in one hand, I hastily push to the front of the queue."
    "It might be a pretty rude thing to do, but the sooner Kleio and her mouth are elsewhere, the better."
    scene bg vip with dissolve
    "Not only do the passes get us straight into the club, they also see us shown to a booth in the VIP section too."
    show kleio happy date at left
    show sasha happy date
    show anna happy date at right
    with dissolve
    mike.say "Wow - only the best for the Deathless Harpies."
    mike.say "I didn't know this place even HAD a VIP area!"
    show kleio happy
    "At this, Kleio laughs and shakes her head."
    kleio.say "Why in the hell would you, Loverboy?"
    kleio.say "It's not like you've ever been a VIP before now!"
    show anna annoyed
    anna.say "Hey, Kleio, don't be mean!"
    show sasha annoyed
    sasha.say "Yeah, Kleio, we're all getting the red card treatment for the first time."
    sasha.say "We won it as a band, so let's make the most of it as a band too, yeah?"
    "Kleio shrugs and rolls her eyes, but I can see in her eyes that she takes it on board."
    show kleio normal
    kleio.say "Okay, okay..."
    kleio.say "But promise me one thing, right?"
    "Everyone glances at Kleio, waiting for the condition that she's about to put on it."
    show kleio happy
    kleio.say "Promise me that we're going to party as a band too, really go crazy?"
    show sasha happy
    show anna happy
    "This gets a series of nods and affirmations, as much out of relief as agreement."
    anna.say "Oh yeah!"
    sasha.say "Oh hell yeah!"
    mike.say "Oh fucking hell yeah!"
    show kleio normal
    show sasha normal
    show anna normal
    "We must have only been sat in the booth for long enough to sip our first drinks before I'm dragged to my feet."
    "A song comes on makes the girls almost literally go wild with excitement."
    "And I just know that there's not going to be any chance of saying no to them."
    sasha.say "Fuck, I haven't heard this one in SO long!"
    kleio.say "Yeah, this is one of the songs that got me into metal in the first place!"
    anna.say "Wow..."
    anna.say "I used to have this girlfriend, and whenever this song played, she'd..."
    show anna blush
    "Anna stops in her tracks and turns a bright shade of red as she realises all eyes are now on her."
    anna.say "Ah...I..."
    show anna happy
    anna.say "LET'S GO DANCE!"
    "Under almost any other circumstances, Anna's attempt at a save just wouldn't have worked."
    "But by now, we're all so drunk and pumped up with adrenaline that what she was about to say is soon forgotten."
    scene bg nightclub
    show kleio happy date at left
    show sasha happy date
    show anna happy date at right
    if Harem.together(anna, sasha, kleio, name='band'):
        "Out on the dance-floor, I try to keep things civilised as best I can."
        "But it doesn't take long for all pretences to be dropped as we start to get physical with each other."
        show kleio normal at left5
        show sasha normal
        show anna normal at right5
        with move
        "Sasha, Anna and Kleio begin to pull into an ever tighter embrace."
        "And I'm drawn in too, aware of the surprised look that we're getting as a result."
        show kleio at center, zoomAt(1.5, (440, 1040))
        show sasha at center, zoomAt(1.5, (640, 1040))
        show anna a at center, zoomAt(1.5, (940, 1040))
        with dissolve
        "All I can do is shrug and allow myself to be wrapped up in the collection of limbs."
        "I don't honestly see why we should be embarrassed about the fact that we're more than just bandmates."
        "So it's only natural that we'd want to celebrate together at some point in the night."
        "This salves my conscience enough for me to get into dancing with Sasha, Anna and Kleio."
        "And pretty soon they've managed to make me all but forget about anything other than them."
        "I guess that winning the competition's really fired them up, made them feel proud of themselves."
        "Because they're dancing like women so sure of her powers that it's impossible for me to resist."
        "And all of that cocky confidence is making them all the more forward too."
        "Right now the excitement that I felt at winning seems to be taking a backseat in my mind."
        "I feel like I could toss it all aside for the sake of being here with Sasha, Anna and Kleio."
        "Every time their bodies are pressed against mine, I want them a little bit more."
        "And I can sense that the same feelings are building up inside of them too."
        "I've never been more aware of just how much dancing like this is a kind of foreplay."
        "So if I don't get to take it to the next logical step soon, I think I might go crazy."
        "And so I lean in close, trying to say what I have to say straight into their ears."
        mike.say "Sasha, Anna, Kleio, I need to get you alone!"
        "But the pounding of the music is just too much for them to hear me."
        kleio.say "Huh?"
        show fx question at left
        kleio.say "You...you wanna use my phone?!?"
        mike.say "No...I want to make love to you!"
        show anna surprised
        anna.say "What...you wanna fill a glove with glue?!?"
        mike.say "I...I think we should get it on!"
        show sasha annoyed
        sasha.say "Hey, who weighs a ton?!?"
        mike.say "No... I WANT TO FUCK YOU!!!"
        "Of course, this is the exact moment when the song ends and there's a moment of silence over the dance-floor."
        "Suddenly I'm aware of every eye in the place being on me."
        show kleio seductive
        show sasha flirt
        show anna dazed
        "But Sasha, Anna and Kleio just shake their heads, looking me in the eye without the merest hint of embarrassment."
        sasha.say "With smooth moves like that, how can us girls say no?"
        show sasha dazed
        kleio.say "Jesus, but you're a fuck-up, [hero.name]."
        show kleio happy
        kleio.say "But I love you for it!"
        anna.say "Yeah, Kleio, I know just what you mean."
        show anna blush
        anna.say "[hero.name], you're SO perfect - it's like you can read my mind!"
        "I shuffle off the dance-floor, still burning with shame."
        "Sasha, Anna and Kleio hold my hand the whole time, not letting me go until we're in the taxi and headed to my place."
        call kleioannafoursome2 from _call_kleioannafoursome2_1
    elif Harem.together(anna, kleio, name='band') and not Harem.find(sasha, name='band'):
        "Out on the dance-floor, I try to keep the band together as a foursome for as long as I can."
        "But it doesn't take long for Anna and Kleio to single me out and begin to wrap themselves around me."
        "I can see the surprised look on Sasha's face as this happens."
        "But all I can do is shrug helplessly as Anna and Kleio jealously pull me into an even tighter embrace."
        "For a moment I'm worried that the Sasha's going to be pissed off, even make a scene."
        "So I'm relieved when she shrugs and turns her attention to a more than willing guy close at hand."
        "It occurs to me that I really shouldn't be feeling guilty right now."
        "After all, it's becoming pretty obvious that the three of us are an item."
        "So it's only natural that we'd want to celebrate together at some point in the night."
        "This salves my conscience enough for me to get into dancing with Anna and Kleio."
        "And pretty soon they've managed to make me all but forget about anything other than them."
        "I guess that winning the competition's really fired them up, made them feel proud of themselves."
        "Because they're dancing like women so sure of her powers that it's impossible for me to resist."
        "And all of that cocky confidence is making them all the more forward too."
        "Right now the excitement that I felt at winning seems to be taking a backseat in my mind."
        "I feel like I could toss it all aside for the sake of being here with Anna and Kleio."
        "Every time their bodies are pressed against mine, I want them a little bit more."
        "And I can sense that the same feelings are building up inside of them too."
        "I've never been more aware of just how much dancing like this is a kind of foreplay."
        "So if I don't get to take it to the next logical step soon, I think I might go crazy."
        "And so I lean in close, trying to say what I have to say straight into their ears."
        mike.say "Anna, Kleio, I need to get you alone!"
        "But the pounding of the music is just too much for them to hear me."
        kleio.say "Huh?"
        show fx question at left
        kleio.say "You...you wanna use my phone?!?"
        mike.say "No...I want to make love to you!"
        show anna surprised
        anna.say "What...you wanna fill a glove with glue?!?"
        mike.say "No... I WANT TO FUCK YOU!!!"
        "Of course, this is the exact moment when the song ends and there's a moment of silence over the dance-floor."
        "Suddenly I'm aware of every eye in the place being on me."
        "Sasha's staring too, already smirking."
        show kleio seductive
        show sasha normal
        show anna dazed
        "But Anna and Kleio just shake their heads, looking me in the eye without the merest hint of embarrassment."
        kleio.say "Jesus, but you're a fuck-up, [hero.name]."
        show kleio happy
        kleio.say "But I love you for it!"
        anna.say "Yeah, Kleio, I know just what you mean."
        show anna blush
        anna.say "[hero.name], you're SO perfect - it's like you can read my mind!"
        "I shuffle off the dance-floor, still burning with shame."
        "Anna and Kleio hold my hand the whole time, not letting me go until we're in the taxi and headed to my place."
        call kleio_anna_threesome from _call_kleio_anna_threesome_2
    elif sasha.is_girlfriend and not anna.is_girlfriend and not kleio.is_girlfriend:
        "Out on the dance-floor, I try to keep the band together as a foursome for as long as I can."
        "But it doesn't take long for Sasha to single me out and begin to wrap herself around me."
        "I can see the surprised look on Anna's face and the knowing one on Kleio's."
        "And all I can do is shrug helplessly as Sasha jealously pulls me into an even tighter embrace."
        "For a moment I'm worried that the other two girls are going to be seriously pissed at us."
        "But the I see Kleio shrug too and pull Anna away to dance together."
        "And it occurs to me that they really can't hold it against Sasha and me."
        "After all, we've never made a secret of the fact we're together."
        "So it's only natural that we'd want to celebrate together at some point in the night."
        "This salves my conscience enough for me to get into dancing with Sasha."
        "And pretty soon she's managed to make me all but forget about anything other than her."
        "I guess that winning the competition's really fired her up, made her feel proud of herself."
        "Because she's dancing like a woman that's so sure of her powers that it's impossible to resist."
        "Right now the excitement that I felt at winning seems to be taking a backseat in my mind."
        "I feel like I could toss it all aside for the sake of being here with Sasha."
        "Every time her body is pressed against mine, I want her a little bit more."
        "And I can sense that the same feelings are building up inside of her too."
        "I've never been more aware of just how much dancing like this is a kind of foreplay."
        "So if I don't get to take it to the next logical step soon, I think I might go crazy."
        "And so I lean in close, trying to say what I have to say straight into Sasha's ear."
        mike.say "Sasha, I need to get you alone!"
        "But the pounding of the music is just too much for her to hear me."
        sasha.say "Huh?"
        show fx question
        sasha.say "You...you wanna use my phone?!?"
        mike.say "No...I want to make love to you!"
        sasha.say "What...you wanna fill a glove with glue?!?"
        mike.say "No... I WANT TO FUCK YOU!!!"
        "Of course, this is the exact moment when the song ends and there's a moment of silence over the dance-floor."
        "Suddenly I'm aware of every eye in the place being on me."
        "Anna and Kleio are staring too, the former with wide eyes and the latter already smirking."
        show kleio normal
        show anna normal
        show sasha flirt
        "But Sasha just shakes her head, looking me in the eye without the merest hint of embarrassment."
        show sasha dazed
        sasha.say "With smooth moves like that, how can I say no?"
        "I shuffle off the dance-floor, still burning with shame."
        "Sasha holds my hand the whole time, not letting me go until we're in the taxi and headed home."
        call sasha_fuck_date_male from _call_sasha_fuck_date
    elif anna.is_girlfriend and not sasha.is_girlfriend and not kleio.is_girlfriend:
        "Out on the dance-floor, I try to keep the band together as a foursome for as long as I can."
        "But it doesn't take long for Anna to single me out and begin to wrap herself around me."
        "I can see the knowing looks on from Sasha and Kleio."
        "And all I can do is shrug helplessly as Anna jealously pulls me into an even tighter embrace."
        "For a moment I'm worried that the other two girls are going to be seriously pissed at us."
        "But the I see Sasha shrug too and pull Kleio away to dance together."
        "And it occurs to me that they really can't hold it against Anna and me."
        "After all, we've never made a secret of the fact we're together."
        "So it's only natural that we'd want to celebrate together at some point in the night."
        "This salves my conscience enough for me to get into dancing with Anna."
        "And pretty soon she's managed to make me all but forget about anything other than her."
        "I guess that winning the competition's really fired her up, made her feel proud of herself."
        "Because she's dancing like a woman that's so sure of her powers that it's impossible to resist."
        "Her normally hesitant and ditzy manner thrown aside in favour of a newfound confidence."
        "Right now the excitement that I felt at winning seems to be taking a backseat in my mind."
        "I feel like I could toss it all aside for the sake of being here with Anna."
        "Every time her body is pressed against mine, I want her a little bit more."
        "And I can sense that the same feelings are building up inside of her too."
        "I've never been more aware of just how much dancing like this is a kind of foreplay."
        "So if I don't get to take it to the next logical step soon, I think I might go crazy."
        "And so I lean in close, trying to say what I have to say straight into Anna's ear."
        mike.say "Anna, I need to get you alone!"
        "But the pounding of the music is just too much for her to hear me."
        anna.say "Huh?"
        show fx question at right
        anna.say "You...you wanna use my phone?!?"
        mike.say "No...I want to make love to you!"
        anna.say "What...you wanna fill a glove with glue?!?"
        mike.say "No... I WANT TO FUCK YOU!!!"
        "Of course, this is the exact moment when the song ends and there's a moment of silence over the dance-floor."
        "Suddenly I'm aware of every eye in the place being on me."
        "Sasha and Kleio are staring too, both already smirking in amusement."
        show kleio normal
        show anna dazed
        show sasha normal
        "But Anna just shakes her head, looking me in the eye without the merest hint of embarrassment."
        anna.say "Mmm..."
        show anna blush
        anna.say "[hero.name], you're SO perfect - it's like you can read my mind!"
        "I shuffle off the dance-floor, still burning with shame."
        "Anna holds my hand the whole time, not letting me go until we're in the taxi and headed back to my place."
        call kleio_fuck_date_male from _call_kleio_fuck_date
    elif kleio.is_girlfriend and not anna.is_girlfriend and not sasha.is_girlfriend:
        "Out on the dance-floor, I try to keep the band together as a foursome for as long as I can."
        "But it doesn't take long for Kleio to single me out and begin to wrap herself around me."
        "I can see the surprised look on Anna's face and the knowing one on Sasha's."
        "And all I can do is shrug helplessly as Kleio jealously pulls me into an even tighter embrace."
        "For a moment I'm worried that the other two girls are going to be seriously pissed at us."
        "But the I see Sasha shrug too and pull Anna away to dance together."
        "And it occurs to me that they really can't hold it against Kleio and me."
        "After all, we've never made a secret of the fact we're together."
        "So it's only natural that we'd want to celebrate together at some point in the night."
        "This salves my conscience enough for me to get into dancing with Kleio."
        "And pretty soon she's managed to make me all but forget about anything other than her."
        "I guess that winning the competition's really fired her up, made her feel proud of herself."
        "Because she's dancing like a woman that's so sure of her powers that it's impossible to resist."
        "And all of that cocky confidence is making her all the more forward too."
        "Right now the excitement that I felt at winning seems to be taking a backseat in my mind."
        "I feel like I could toss it all aside for the sake of being here with Kleio."
        "Every time her body is pressed against mine, I want her a little bit more."
        "And I can sense that the same feelings are building up inside of her too."
        "I've never been more aware of just how much dancing like this is a kind of foreplay."
        "So if I don't get to take it to the next logical step soon, I think I might go crazy."
        "And so I lean in close, trying to say what I have to say straight into Kleio's ear."
        mike.say "Kleio, I need to get you alone!"
        "But the pounding of the music is just too much for her to hear me."
        kleio.say "Huh?"
        show fx question at left
        kleio.say "You...you wanna use my phone?!?"
        mike.say "No...I want to make love to you!"
        show kleio surprised
        kleio.say "What...you wanna fill a glove with glue?!?"
        mike.say "No... I WANT TO FUCK YOU!!!"
        "Of course, this is the exact moment when the song ends and there's a moment of silence over the dance-floor."
        "Suddenly I'm aware of every eye in the place being on me."
        "Anna and Sasha are staring too, the former with wide eyes and the latter already smirking."
        show kleio seductive
        show anna normal
        show sasha normal
        "But Kleio just shakes her head, looking me in the eye without the merest hint of embarrassment."
        kleio.say "Jesus, but you're a fuck-up, [hero.name]."
        show kleio blush
        kleio.say "But I love you for it!"
        "I shuffle off the dance-floor, still burning with shame."
        "Kleio holds my hand the whole time, not letting me go until we're in the taxi and headed to my place."
        call kleio_fuck_date_male from _call_kleio_fuck_date_1
    else:
        show kleio normal at left5
        show sasha normal
        show anna normal at right5
        with move
        "Out on the dance-floor, we instinctively stick together as a foursome."
        "There's nothing bonding us together beyond platonic friendship and camaraderie."
        show kleio happy at center, zoomAt(1.5, (340, 1040))
        show sasha b happy at center, zoomAt(1.5, (680, 1040))
        show anna a happy at center, zoomAt(1.5, (900, 1040))
        with dissolve
        "But all the same we manage to have some flirty fun and dance pretty close together."
        "More than once we each seem to have attracted the attention of a potential partner."
        "And yet there's just something so special about the bond between the four of us right now."
        "It means that we completely ignore even the most obvious approaches that are made towards us."
        "Almost as though what we've achieved as a band is sacred, and to let an outsider in would taint it."
        "And the strangest thing is that I'm totally okay with that."
        "I mean, I'm not losing interest in that kind of thing."
        "It's just that I've never had something like this with a bunch of girls before now."
        "Sasha, Anna and Kleio are all pretty hot in their own right."
        "But I love them as friends right now, not as potential conquests."
        "Who knows, that might chance in the future, it might not."
        "Right now, they're my bandmates and my friends, and that's enough for me."
        "The rest of the night is kind of a blur, with more drinks and even more dancing."
        scene bg taxi car at blur(8), dark, dark with dissolve
        "At some point we must stumble out of the place and into another taxi."
        scene bg bedroom1 at blur(8), dark with dissolve
        "And the last thing that I remember is being carried into my room by the girls."
        show sasha date at center with dissolve
        sasha.say "Get some sleep, [hero.name]."
        show anna date at right5 with dissolve
        anna.say "Ooh...he's gonna have one hell of a hangover in the morning!"
        show kleio date at left5 with dissolve
        kleio.say "Sleep tight, sweet prince!"
        scene bg bedroom1 at blur(8), dark, dark with dissolve
        "And so I pass out with the sound of their voices still ringing in my ears..."
        call sleep from _call_sleep_26
    return

label battle_of_the_bands_round_two:
    $ game.room = "nightclub"
    show bg nightclub
    $ BOB_SCORE = game.flags.bandpractice
    "We make it to the venue in record time."
    "Either more awake or just more belligerent than the rest of us, Kleio is the first to find the running order for the night."
    show kleio date angry at left with dissolve
    kleio.say "FUCK - they've only gone and put us on last!"
    show anna date at right with dissolve
    anna.say "Is that a good thing...or a bad thing?"
    show sasha date at center with dissolve
    sasha.say "It's just a thing - doesn't matter when we're on, just how well we play."
    show kleio date normal
    "I nod, adding something vague that I hope sounds affirmative enough, and am relieved to see it gets smiles all round."
    "The rest of the time passes like a race between a crippled slug and an arthritic tortoise."
    "Everyone nurses their heads and tries to look interested in the pounding music making them throb all the more terribly."
    "Finally, it seems just as we're preparing to go on stage, I can feel the hangover giving way to adrenalin and a positive buzz at what lies ahead."
    "Sasha nods, and one by one, we all nod in return, no one speaking as we stride out onto the stage."
    "I can't tell if the same faces are in the crowd as last night, but I try not to let it bother me."
    "I tell myself that what they got last night was just a flavour of the Deathless Harpies, and tonight is the full-on, balls-to-the-wall experience."
    stop music
    show concert stage anna kleio sasha with fade
    kleio.say "We are the Deathless Harpies, and we want to win this whole fucking thing!"
    kleio.say "But first, we gotta win over all of you mother-fuckers...so let's do this thing!"
    play music "music/deathless_harpies/Deathless_Harpies.ogg" loop
    show layer master at lparty
    "We launch into the set list, playing a couple of songs from last night to remind the crowd of who we are."
    scene bg black
    show concert solo anna date
    pause 2.0
    show concert solo sasha date
    pause 2.0
    show concert solo kleio date
    "But then we switch to different material, stuff we'd deliberately held back as our best."
    "Just in case we got this far and needed a final kick to the nuts to push it over the top."
    scene bg black
    show concert stage anna kleio sasha
    "We get to a critical point in one song where I'd been convinced we needed a guitar solo."
    "It was voted down in practice, two to one, with one abstention."
    "But now that we're onstage, I'm more sure we need it than ever, and no one can stop me from trying."
    scene bg black
    show concert solo mike date
    if game.flags.bandcrossdress:
        "I still have no clue as to whether the crowd think I'm a lanky girl or know I'm a guy in drag."
        "But either way, they're not ready for me to put one stockinged leg up on my speaker and grind out a solo of this sheer stature."
        "In that moment, I could believe that I've made everyone in the audience, male, female, straight, gay or bi want to fuck me."
        "Being in drag feels like the ultimate form of armour, a second skin that transforms me into a true star."
        $ BOB_SCORE += 10
    elif hero.charm >= 75:
        "At the moment when I'm supposed to stick to the script, I suddenly veer off into the dramatic solo."
        "I try to ignore the girls' reactions, concentrating solely on the music, channeling my instinct into pure sound."
        "Kleio compensates seamlessly, and I can only just hear the crowd's cheers soaring as I climb the stairway to metaphorical heaven."
        "As I wrap up the solo, I hope that my sighs are taken as triumph rather than sheer relief by all those watching."
        $ BOB_SCORE += 10
    else:
        "From the moment I leave the safety of the plan behind, I can almost feel things starting to go wrong."
        "What I'm improvising just won't fit with the rest of the sound, and it jars the girls off their own parts too."
        "In the end, to save face, I have to mime that I've broken a string or some such, and stop playing altogether."
        "As my cheeks burn with embarrassment, I can already hear the girls hissing their demands for an explanation at me."
        $ BOB_SCORE -= 10
    scene bg black
    show concert stage anna kleio sasha
    "As we're reaching the final few songs on the set list, I realise that I haven't seen one member of a single band crowdsurf tonight."
    "There's no way to tell the others what I'm planning to do, just keep on watching the crowd and pick my moment as best I can."
    scene bg black
    show concert solo mike date
    if game.flags.bandcrossdress:
        "I pick a pack of pretty buff looking crowd members and then my moment, diving out into the audience a second later."
        "Luckily enough of them see me coming, and I manage to keep hold of my guitar, playing while I surf the crowd."
        "My playing stumbles at one point, when I feel the unmistakable sensation of a hand going up my dress and copping a feel."
        "As much as the solo was a success, what'll stick in my mind is getting to know what it feels like to be a woman when roaming hands are about."
        $ BOB_SCORE += 10
    elif hero.fitness >= 75:
        "Launching myself into the air, still clutching my guitar, I pray that the couple of large guys I aimed for don't move."
        "At least one of them sees me coming, and I land on awaiting hands, the lead of my instrument miraculously reaching as well."
        "Bobbing on the heads of the crowd, I play out the remainder of the song with only the ceiling of the venue to look at."
        "But it's worth the discomfort, as the audience seem to really get off on the reckless abandon the move shows."
        $ BOB_SCORE += 10
    else:
        "I make a plea to whomever's listening that the big guys I aimed for don't move as I leap from the stage."
        "But my luck's out, as they get swept to one side and I end up on a trajectory for a knot of teenage girls instead."
        "Unaware of my imminent arrival and probably not up to catching me anyway, they instinctively scatter, and I crash unceremoniously to the ground."
        "The song finishes before I can limp to the barrier and sheepishly clamber back onto the stage, trying to avoid the murderous looks coming my way from both the crowd and the band."
        $ BOB_SCORE -= 10
    show concert solo sasha date
    pause 3.0
    show concert solo anna date
    pause 3.0
    show concert solo kleio date
    pause 3.0
    scene bg black
    show concert stage anna kleio sasha
    "Once the last song is over and the final notes have faded, we trudge offstage, truly exhausted, worn out and used up."
    "We're so tired and spent that we totally miss the results as they're announced to the crowd, one of the backstage staff having to relay them to us instead."
    scene bg nightclub with fade
    if BOB_SCORE >= 100:
        "It takes a while for what they're trying to tell us to actually sink in, we're so shell-shocked from the gig."
        show kleio date surprised at right
        show sasha date surprised at left
        show anna date surprised
        with dissolve
        pause 1
        show sasha happy
        sasha.say "What, wait...you mean we won this thing?"
        show kleio happy
        kleio.say "Well that's what they fucking well said, isn't it?"
        show anna happy
        anna.say "I think that's what I heard."
        mike.say "You heard right, Anna - we won the contest!"
        if renpy.has_label("battle_of_bands_achievement_1") and not game.flags.cheat:
            call battle_of_bands_achievement_1 from _call_battle_of_bands_achievement_1
        if game.flags.bandcrossdress:
            "While the most important thing seems to be that we have apparently won the contest, no one can mention it without adding how amazing it is that we're such an inclusive group."
            show anna annoyed
            anna.say "What do they mean by that?"
            show kleio punk
            kleio.say "They mean that dick-in-a-dress here is getting us over with the LGBTQ+ contingent."
            show sasha happy
            sasha.say "But that's great, right? That's what we wanted from the start?"
            mike.say "Screw you guys - it's great this thing paid off, but all you wanted to do was make me squirm!"
            show sasha happy
            show kleio happy
            show anna happy
            "I can't help grinning and then bursting into laughter at the confused looks on their faces, unsure as to whether they did something woke and PC on purpose or just pulled a puerile joke and got lucky."
        else:
            "Suddenly everyone is hugging and kissing everyone else, and there's danger of a band-wide orgy breaking out backstage."
    else:
        "What the staff member's saying to us doesn't make sense at first, but then I can almost feel the girls' hearts sink in their chests."
        show kleio date surprised at right
        show sasha date surprised at left
        show anna date surprised
        with dissolve
        pause 1
        show kleio angry
        kleio.say "This is bullshit, man - we played better than any of that other trash out there!"
        show sasha date angry
        sasha.say "Fuck me...after we got to the finals, I really thought we had this thing in the bag."
        show anna date cry
        anna.say "Ooh...did we not win, then?"
        mike.say "No, Anna...we didn't win."
        show kleio annoyed
        show sasha sad
        "I want to say something positive, something about the importance of taking part, or else hear one of the others say it."
        "But the truth is that I'm so physically tired and emotionally spent that I just can't manage it."
        $ game.flags.bobWon = False
    "Just like the night before, there's some kind of presentation onstage and an after-party."
    "The only problem is that we're so wired and exhausted that we make our collective excuses as soon as we can, and then leave."
    "I can't imagine what the consequences of tonight will be for the band and the four of us."
    "But one thing I can be sure of is that there's going to be changes on the horizon, for better or worse."
    return

label battle_of_the_bands_round_one:
    $ game.room = "pub"
    show bg pub
    "It feels like we've been slaving away in the practice room for a lifetime, but the day of the Battle of the Bands has now arrived."
    "All four of us are nervous, all hiding it in our own ways, be that by being surly, cheerful or just feigning indifference to the outcome."
    "As it's a Friday night, we arrive at the venue as early as possible and set about hauling our gear out of the back of the van."
    show kleio casual at right5
    show anna casual surprised
    show sasha casual at top_mostright
    with moveinright
    anna.say "Ooh, look at some of their shit...that stuff's real nice!"
    show anna normal
    show kleio at right4 with move
    kleio.say "Expensive toys are no substitute for actual fucking talent!"
    mike.say "Kleio's right, Anna - we're as good as any of them, and it's just one more gig, that's all."
    show sasha at right with move
    sasha.say "Two more, you mean."
    mike.say "What?!?"
    sasha.say "There's two rounds, semi-final tonight and grand final in 2 weeks."
    show sasha casual at right
    show anna casual surprised at vshake
    anna.say "Two whole gigs?!?"
    show kleio casual annoyed at left with move
    kleio.say "Geez, Sasha - you could have told us!"
    show sasha joke
    sasha.say "I thought I already did!"
    show kleio normal
    show anna normal
    show sasha normal
    "I can see that eyes are turning my way, looking for my input."
    $ BOB_SCORE = game.flags.bandpractice
    if game.flags.bandcrossdress:
        mike.say "I'm gonna take a wild stab in the dark and guess I forgot on account of having to wear make-up and a dress!"
        mike.say "If I can cope with that, the least you three can do is play two gigs with me while I do it!"
        show kleio casual annoyed
        show sasha casual annoyed
        show anna casual annoyed
        "All three of the girls snigger, the thought of me in drag taking their minds off of the task at hand."
        $ BOB_SCORE += 10
    else:
        menu:
            "Be positive":
                mike.say "Maybe she did mention it, but we've been in a buzz for ages now, so it probably didn't sink in."
                $ kleio.love -= 5
                show anna casual dazed
                anna.say "My head's still spinning!"
                show kleio casual annoyed
                kleio.say "Gah, whatever - we're ready for one gig or one hundred."
                $ BOB_SCORE += 10
            "Be negative":
                mike.say "Dunno...can't see that it matters."
                $ kleio.love -= 5
                $ sasha.love -= 5
                show kleio casual angry
                kleio.say "Jesus, could you be any more useless?"
                show sasha casual annoyed
                sasha.say "Whatever you guys think, it's still two gigs."
            "Be angry":
                mike.say "What happened to us being a damn band?!?"
                $ sasha.love -= 5
                $ anna.love -= 5
                show sasha casual vangry
                sasha.say "Fuck sake, I already said that I told you morons!"
                show anna casual dazed
                anna.say "Hey, you guys...I don't think we should be arguing right now."
                $ BOB_SCORE -= 10
    hide anna
    hide kleio
    hide sasha
    with moveoutleft
    "After that little distraction, we cram into the allotted dressing room and wait feverishly for our turn to be called."
    "No one seems to feel much like talking, and the sounds of the other bands playing are muffled to the point of being almost incomprehensible."
    "When the call comes, we almost sneak out onto the stage, blinded by the intensity of the lights and awed by the size of the crowd."
    stop music
    scene bg black
    show concert pub anna kleio sasha with fade
    kleio.say "We are the Deathless Harpies, and we're here to win this thing by winning you over first!"
    play music "music/deathless_harpies/Deathless_Harpies.ogg" loop
    show concert solo sasha casual pub
    pause 3.0
    show concert solo anna casual pub
    pause 3.0
    show concert solo kleio casual pub
    pause 3.0
    scene bg black
    show concert pub anna kleio sasha
    "And with that we're off, everyone seeming to forget their nerves and play their part."
    "I can feel myself getting swept away the atmosphere, and soon I'm trying to channel my inner rock god with some outrageous moves."
    if game.flags.bandcrossdress:
        scene bg black
        show concert solo mike casual pub
        "Somehow the dress and make-up only serve to make me surer of myself as I try to command the stage."
        "My height and the striking sight of me in the women's clothes mean I look so much more worthy of attention."
        "I have no clue as to whether the audience think I'm female or a guy in drag, but either way, they're popping for it big time."
        $ BOB_SCORE += 10
    elif hero.charm >= 50:
        scene bg black
        show concert solo mike casual pub
        "I unconsciously recall steps from Angus Young, Slash and maybe even Nigel Tufnel."
        "Retracing their moves and mixing in some of my own, I strut across the stage as I play."
        "Stopping to face the crowd, I can hear them reacting eagerly to my posturing with the guitar."
        $ BOB_SCORE += 10
    else:
        "I know what I want my feet to do while the rest of me goes on playing the guitar."
        "But it seems like they're just not getting the message, and doing something all of their own."
        "At one point I get my ankles wound up in cables, tumbling to the floor and only just managing to keep from screwing the song up completely."
        $ BOB_SCORE -= 10
    scene bg black
    show concert pub anna kleio sasha
    "The set list is being devoured as our time begins to run out, and we start playing the last number."
    scene bg black
    show concert solo anna casual pub
    pause 3.0
    show concert solo sasha casual pub
    "Everyone's playing their hearts out, but I can't help thinking that it needs something more."
    show concert solo kleio casual pub
    "So I step up to Kleio's mic and add my voice to hers as we go for the big finale."
    if game.flags.bandcrossdress:
        "I step up and impose myself on Kleio and her mic, accompanying her in singing the lyrics."
        "She looks surprised at first, but a second later the audience seem to buy into it and she recovers almost without letting her shock show."
        "I guess the contrast of a tall guy dressed as a woman and a smaller girl decked out as tough and spikily as Kleio just works."
        "Kleio owns the rest of the song, and I can't help admiring the strength and sexiness that she exudes as she does so."
        $ BOB_SCORE += 10
    if hero.charm >= 75:
        "Surprised by the unexpected move, Kleio nevertheless doesn't lose a beat as I step up beside her and start to sing."
        "Perhaps it's the ease of all that time in the practice room, or something more intimate altogether, but we gel almost instantly."
        "Kleio pushes herself to a new height as my own voice supports and adds to hers, and we finish the song locked in a vocal duel that crackles with sexual tension."
        $ BOB_SCORE += 10
    else:
        "Kleio is almost instantly wrong-footed by my hustling up and sharing her mic without warning."
        "She stumbles, losing her concentration and then elbows me savagely in the gut as she struggles to recover."
        "It's all that I can do to limp through the rest of the song, cursing myself for doing something that could have cost us the contest."
    scene bg black
    show concert pub anna kleio sasha
    "After the set, we wait impatiently for the last bands to play so that we can hear the results."
    "When the MC steps out onto stage, we hold out collective breath."
    if BOB_SCORE >= 75:
        "Over the noise of the crowd and the chattering of the other bands backstage, we hear the name Deathless Harpies included amongst those advancing to the final."
        "We did it, we're still in with a chance of winning the whole thing!"
        $ game.flags.bobWon = True
        $ game.flags.nextgig = TemporaryFlag(game.days_played + 14, 14)
    else:
        "We wait until the last band name has been read out, but there's no mention of the Deathless Harpies to be heard."
        "Look's like we just weren't good enough, and we're not coming back tomorrow night as a result."
    scene bg pub with fade
    "No one speaks as we walk out of the venue, the emotions and the adrenaline still in control."
    "I don't think any of us actually expected this to be the outcome, and no one knows what tomorrow will bring."
    return

label first_gig:
    $ hero.cancel_activity()
    $ game.set_flag("bandpractice", 5, mod="+")
    show kleio at left
    show anna at center
    "The Battle of the Bands was now literally a week away, and I thought things couldn't get any more tense."
    "But then, out of the blue, Sasha turned up at the practice room and dropped a bombshell."
    show sasha at right with moveinright
    sasha.say "Grab your shit, guys - we've got a gig!"
    show anna surprised at vshake
    anna.say "Huh?"
    show kleio surprised at vshake
    kleio.say "What the hell?!?"
    mike.say "Sasha, what on earth do you mean? An actual gig?"
    show sasha annoyed
    sasha.say "No, not a real gig, a pretend one in front of an audience of cardboard cut-outs!"
    show sasha joke
    sasha.say "Of course I mean a real one."
    show kleio punk at hshake
    "Kleio made enough noise as she stormed around the room to almost cover up her swearing."
    show anna dazed
    "Anna did the opposite, staying sat on her drum stool in silence, but her expression betrayed her trepidation at the thought of the surprise gig."
    show sasha normal
    sasha.say "Come on, people - this is the perfect opportunity to put all that practice into...well, practice!"
    sasha.say "If we can't play a gig now, then how can we play one in a week's time?"
    show kleio normal
    show anna normal
    "Sasha looks at me expectantly, as I realise Kleio and Anna are too."
    "I realise that, while Kleio's thrown her usual tantrum and Anna's gone characteristically quiet, I still haven't voiced my thoughts."
    if not game.flags.bandcrossdress:
        menu:
            "Try to be positive":
                mike.say "Sure it's a shock, but carpe diem, and all that shit - let's do it!"
                show sasha happy
                show kleio annoyed
                "Sasha seems glad to have my support, but Kleio and Anna still don't look convinced."
                mike.say "You two might not believe in yourselves, but I do - Kleio, Anna, you've aced everything we've practiced today."
                mike.say "I say we grab this gig by the scruff of the neck and shake it till it screams for mercy!"
                $ anna.love += 5
            "Try to remain neutral":
                mike.say "Honestly, Sasha, you dropping this on us kind of sucks."
                show sasha annoyed
                "Sasha looks a little wounded at the dig, clearly hoping for more support from me."
                mike.say "I'm not shitting on you, or the idea though - I think we can do it, and that we probably should."
                mike.say "I just wish we'd had some warning so that we could at least prepare."
                $ sasha.love += 5
            "Be negative":
                mike.say "Fuck sake, Sasha - as if we haven't got enough shit on our plates already?!?"
                show sasha surprised
                "Sasha looks surprised at the way I tear into her, and then her face darkens with her mood."
                show sasha annoyed
                mike.say "All of us are wrapped up in practicing, but now we've got to snap out of it and deal with a live audience too?"
                $ kleio.love += 5
    else:
        show kleio happy
        show anna wink
        "Suddenly Kleio and Anna stop their complaining and start to give me sly glances and knowing winks, laughing to each other."
        show sasha happy
        "Sasha's mood lightens too when she realises what's got them so amused."
        mike.say "Wait a minute - you don't seriously expect me to do the gig in drag?"
        show sasha joke
        sasha.say "It's supposed to be a dress rehearsal, [hero.name]."
        kleio.say "Yeah, so in your case, that makes it a drag rehearsal too!"
        "I'm already panicking about cross-dressing in front of complete strangers, but at least my discomfort seems to have smoothed things over with the girls for the moment."
        $ kleio.love += 5
        $ anna.love += 5
        $ sasha.love += 5
    show kleio normal
    show sasha normal
    show anna normal
    sasha.say "Whatever to all that, we need to get our shit downstairs and into the van - RIGHT NOW!"
    "For a moment, at least the nerves and recriminations are forgotten as we scurry around gathering up instruments and gear."
    "In less than fifteen minutes, we're packed, panting and sweating into the van with everything we need to play the gig."
    show sasha at top_mostright
    show anna at right4
    with move
    anna.say "Oh, Sasha - you didn't say where we're going."
    show sasha at right with move
    sasha.say "The Leadmill - some guy on my course knows the manager, and he was desperate for a band to fill in at short notice."
    show kleio annoyed
    kleio.say "Wow, tough crowd...I heard one band got their singer pulled off stage and roughed up by the crowd 'cos they thought he sucked."
    mike.say "WHAT?!?"
    show sasha
    sasha.say "Don't have a cow, [hero.name]...that's just an urban legend."
    if game.flags.bandcrossdress:
        mike.say "So you say, Sasha...but if they do that kind of thing to people that suck, what are they gonna do when they realise I'm a dude in pantyhose and a stuffed bra?"
        sasha.say "I already said don't worry about it, the lights will be so bright that even you'll look hot in a dress."
    scene black
    play sound car_door
    pause 0.4
    play sound car_door
    pause 0.2
    play sound car_door
    queue sound car_ignition
    scene bg street with fade
    with vpunch
    "With Kleio behind the wheel of the van, we make it to the venue with time to spare, almost as shaken from the journey as we were from the prospect of the surprise gig itself."
    "I have to change into my gig clothes in the back of the van during the journey, wrestling with my rock-chick outfit while tumbling around the loose equipment."
    stop sound
    scene bg door pub with fade
    "Mercifully, the venue has hired a couple of stagehands, and they unload our gear while we troop to a tiny dressing-room with our band's name written in marker-pen on what looks like a napkin and stuck to the door."
    scene bg pub with fade
    "A member of backstage staff clues us in that we're replacing the second support band for a group I've never heard of, but the girls seem to know, as they nod with enthusiasm."
    "Time seems to shoot by in a blur, and before I know it, we're standing in the wings, waiting to be ushered onstage."
    stop music
    if game.flags.bandcrossdress:
        show concert solo kleio casual pub
        kleio.say "Hello there...we are the Deathless Harpies, and we're gonna make your ears bleed!"
        play music "music/deathless_harpies/Deathless_Harpies.ogg" loop
        "Any lingering worries I have about being in drag are pushed aside as I start playing."
        show concert solo sasha casual pub
        pause 3.0
        show concert solo anna casual pub
        pause 3.0
        show concert solo mike pub
        "The urge to perform takes over, and somehow the clothes that I'm wearing start to feel weirdly liberating."
        "I have no clue if the audience knows I'm a man or a woman, and that ambiguity frees me to make the music do the talking."
        "My enthusiasm seems to spread to the girls as well, and they up their game accordingly, with audible results."
        "When we wrap up the set and step off stage, only then do I remember what I'm wearing and start to come back down to earth."
        if game.flags.bandpractice >= 50:
            $ a = 1
        elif game.flags.bandpractice >= 25:
            $ a = 2
        else:
            $ a = 3
    elif game.flags.bandpractice >= 50:
        $ a = 1
        show concert solo kleio casual pub
        kleio.say "Hello and how the hell are you doing?"
        kleio.say "We are the Deathless Harpies, and we're here to entertain you!"
        play music "music/deathless_harpies/Deathless_Harpies.ogg" loop
        "I don't know where Kleio's words come from, but they seem to set the audience off straight away."
        show concert solo sasha casual pub
        pause 3.0
        show concert solo anna casual pub
        pause 3.0
        show concert solo mike casual pub
        "The rest of the set is a haze, as everything just clicks, and we become a tight-knit unit, more than the sum of its parts."
        "Adrenaline takes over, and everyone plays like their lives depend upon it."
        "When we come off stage, we're soaked and exhausted, but grinning like four clowns at the cheers from the audience."
    elif game.flags.bandpractice >= 25:
        $ a = 2
        show concert solo kleio casual pub
        kleio.say "We are the Deathless Harpies, and...we...we're here to rock."
        play music "music/deathless_harpies/Deathless_Harpies.ogg" loop
        "Kleio stumbles a little as she introduces us, and her nerves quickly spread to the rest of us on stage."
        show concert solo sasha casual pub
        pause 3.0
        show concert solo anna casual pub
        pause 3.0
        show concert solo mike casual pub
        "We start off unsure of ourselves and it shows, but somehow the mixed reaction of the audience spurs us on."
        "Sasha, Kleio, Anna and I start to remember our cues, and our individual efforts inspire us to drag ourselves together as a band."
        "By the time the set ends and we troop off stage, we're not celebrating, but nods and smiles say we know that we salvaged something."
    else:
        $ a = 3
        show concert solo kleio casual pub
        kleio.say "Hello all of you bitches and male chauvinist pigs!"
        kleio.say "We are the Deathless Harpies, and we're the next big thing!"
        play music "music/deathless_harpies/Deathless_Harpies.ogg" loop
        "Kleio's words go down with the crowd like a lead balloon, earning us shocked stares and even hurled abuse before we even start to play."
        show concert solo sasha casual pub
        pause 3.0
        show concert solo anna casual pub
        pause 3.0
        show concert solo mike casual pub
        "The negative emotion infects the rest of us, and it's like we've somehow forgotten what our instruments are actually for."
        "Every song sees at least one of us fuck up, and by the end of the set we almost run off stage to keep from hearing the boos aimed at us."
    scene bg pub with fade
    "Everyone keeps quiet as we walk back to the dressing room and the stagehands load our gear back into the van."
    "We're all clearly wired from the gig, Sasha and Kleio looking like they want to share their opinions on how things went."
    scene black
    play sound car_door
    pause 0.4
    play sound car_door
    pause 0.2
    play sound car_door
    queue sound car_ignition
    scene bg street with fade
    with vpunch
    "But somehow we all keep up an unconscious silence until we're alone in the van and driving back to the practice room."
    if a == 1 and game.flags.bandcrossdress:
        show bg street at dark
        show kleio at center, zoomAt(1.5, (940, 1040))
        show anna b happy at center, zoomAt(1.4, (640, 1040))
        show sasha b at center, zoomAt(1.5, (340, 1040))
        with dissolve
        sasha.say "So, some good, some bad - plenty that we can work on in time for the competition."
        show kleio happy
        kleio.say "Way to ignore the elephant in the van, Sasha!"
        "I frown, not knowing what Kleio's talking about, but then I hear Anna giggling beside me."
        show anna wink
        anna.say "She means you, [hero.name]...you know that you forgot to get changed, right?"
        "I look down in genuine surprise, realising for the first time that I'm still dressed in drag."
        mike.say "Shit...I must have forgotten, you know - in the fuss after the gig!"
        show anna blush
        anna.say "Whatever you say - don't worry, I think you look adorable like that!"
        show kleio flirt
        kleio.say "Yeah, with a swamp-donkey like you around, we all look ten times better by default!"
        sasha.say "Don't listen to her...I think you pulled it off well, and it kinda added something to the band as well."
        $ kleio.love += 5
        $ anna.love += 5
        $ sasha.love += 5
    elif a == 1:
        show bg street at dark
        show kleio at center, zoomAt(1.5, (940, 1040))
        show anna b happy at center, zoomAt(1.4, (640, 1040))
        show sasha b at center, zoomAt(1.5, (340, 1040))
        with dissolve
        sasha.say "See, you guys - I told you we needed this!"
        show kleio annoyed
        kleio.say "Geez, Sasha...don't let it go to your head or anything!"
        show anna happy
        anna.say "Wow, Kleio's not going for the jugular - that means she thinks you're right, Sasha!"
        show kleio happy
        "I can't help but laugh at Anna's ability to interpret Kleio's rudeness and guess her deeper meaning."
        "In that moment, I feel a real fondness for all three of the girls, seeing their redeeming qualities shine through."
        mike.say "I'm just gonna come out and say it - you girls were amazing...I think we all were."
        $ kleio.love += 5
        $ anna.love += 5
        $ sasha.love += 5
    elif a == 2:
        show bg street at dark
        show kleio at center, zoomAt(1.5, (940, 1040))
        show anna b at center, zoomAt(1.4, (640, 1040))
        show sasha b at center, zoomAt(1.5, (340, 1040))
        with dissolve
        sasha.say "I can't say we couldn't have done better - but I think, on balance, it was more good than bad."
        kleio.say "Huh...well, yeah...I guess you're right."
        kleio.say "Just remember to warn us next time you do something like that, okay?"
        show anna happy
        anna.say "Ah well, back to the grind for us all!"
        "Everyone's tired, and there are some seriously bruised egos, but I can't help smiling at the fact we still managed to pull through in the end."
        $ kleio.love += 2
        $ anna.love += 2
        $ sasha.love += 2
    else:
        show bg street at dark
        show kleio at center, zoomAt(1.5, (940, 1040))
        show anna b at center, zoomAt(1.4, (640, 1040))
        show sasha b annoyed at center, zoomAt(1.5, (340, 1040))
        with dissolve
        sasha.say "I'm just gonna say it, Kleio - what the fuck was that shit about at the start of the set, huh?"
        show kleio annoyed
        kleio.say "Do I have to run everything I say past you now?"
        sasha.say "If you're gonna spout that kind of BS, then maybe you need to!"
        show anna happy
        anna.say "Well, I think that..."
        with vpunch
        show anna dazed
        show sasha vangry
        show kleio angry
        "Anna's words are lost in the mix, as Sasha and Kleio tear into each other over the disastrous gig."
        "I feel that I should jump in, defend Anna or at least plead for them to stop."
        "But I'm feeling so tired and down from the shitty performance, that I just end up staring out of the window at the passing streetlights."
    scene bg street with dissolve
    "An odd, tired silence falls over us all after that, and no one speaks until the van pulls up outside the practice room."
    "I guess we're all just mulling over our thoughts on the way the gig went, and what it'll mean when the day of the competition finally comes around."

    $ game.room = "pub"
    $ game.flags.nextgig = TemporaryFlag(game.days_played + 7, 7)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
