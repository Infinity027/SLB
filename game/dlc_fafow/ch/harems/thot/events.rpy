init python:
    InteractEvent(**{
    "name": "thot_harem_event_01",
    "label": "thot_harem_event_01",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 0,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsRoom("date_mall1"),
            ),
        PersonTarget(reona,
            Not(IsHidden()),
            Or(
                HasRoomTag("mall_southside"),
                HasRoomTag("mall_northside"),
            ),
            MinStat("love", 40),
            ),
        PersonTarget(alexis,
            IsActive(),
            OnDate(),
            MinStat("love", 40),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "thot_harem_event_02",
    "label": "thot_harem_event_02",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 0,
    "conditions": [
        IsDone("thot_harem_event_01"),
        HeroTarget(
            IsGender("male"),
            IsFlag("thot_harem_delay", False)
            ),
        PersonTarget(reona,
            Not(IsHidden()),
            IsPresent(),
            MinStat("love", 100),
            ),
        PersonTarget(alexis,
            ContactKnown()
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "thot_harem_event_03",
    "label": "thot_harem_event_03",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 1,
    "conditions": [
        IsDone("thot_harem_event_02"),
        HeroTarget(
            IsGender("male"),
            IsFlag("thot_harem_delay", False),
            HasRoomTag("mall_northside"),
            ),
        PersonTarget(reona,
            Not(IsHidden()),
            HasRoomTag("mall_northside"),
            MinStat("love", 130),
            ),
        PersonTarget(alexis,
            Not(IsHidden()),
            MinStat("love", 130),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "thot_harem_event_04",
    "label": "thot_harem_event_04",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 1,
    "conditions": [
        IsDone("thot_harem_event_03"),
        IsSeason(0, 1),
        IsTimeOfDay("evening"),
        HeroTarget(
            IsGender("male"),
            IsFlag("thot_harem_delay", False),
            IsRoom("livingroom"),
            ),
        PersonTarget(reona,
            Not(IsHidden()),
            MinStat("love", 170),
            ),
        PersonTarget(alexis,
            Not(IsHidden()),
            MinStat("love", 170),
            ),
        Or(
            PersonTarget(bree, IsGone()),
            PersonTarget(bree, Or(IsHidden(), Not(HasRoomTag("home")))),
            ),
        Or(
            PersonTarget(sasha, IsGone()),
            PersonTarget(sasha, Or(IsHidden(), Not(HasRoomTag("home")))),
            ),
        ],
    "do_once": True,
    })

label thot_harem_event_01:
    show alexis
    "Alexis and I are chatting away merrily as we walk around the mall."
    "You know, just a guy and a girl on a date, enjoying each other's company..."
    "Aah...let's be honest - I'm following Alexis around like a lovestruck puppy!"
    "I can't take my eyes off of her, so much so that I keep on bumping into people."
    "And she's making a show of not noticing the attention I'm giving her."
    "But I know the kind of smile that she has on her face right now."
    "It's one that she uses when she wants to hide the fact that she's delighted."
    alexis.say "So, [hero.name]..."
    mike.say "Yeah..."
    alexis.say "I was thinking that we could maybe..."
    mike.say "Uh-huh..."
    show alexis a blush
    alexis.say "Possibly start thinking about..."
    mike.say "Yup..."
    show alexis a wink -blush
    alexis.say "Kind of moving in the direction of..."
    mike.say "WHOA!"
    show fx question
    show alexis b annoyed
    alexis.say "[hero.name]!"
    alexis.say "Are you even listening to me right now?!?"
    hide fx
    "I wrench my gaze away from the thing that's captured my interest."
    show alexis b upset at center, traveling(1.5, 0.25, (640, 1040))
    "And as soon as I do so, I see Alexis glaring at me."
    "Her hands are balled into fists and planted on her hips."
    "Plus she's leaning towards me, almost thrusting her nose against mine."
    mike.say "Erm..."
    mike.say "Sorry, Alexis..."
    mike.say "I was just a little distracted!"
    show alexis b annoyed
    alexis.say "I can see that!"
    alexis.say "What's so interesting that you'd totally ignore me, huh?"
    "As if on cue, the source of my distraction saunters into view."
    show alexis confused at center, traveling(1.0, 0.25, (840, 720))
    pause 0.25
    show reona leftback rightopen at left5
    with easeinleft
    reona.say "Oh..."
    reona.say "Hi there, [hero.name]."
    show reona leftnormal rightnormal
    reona.say "I thought it was you checking me out from over there."
    reona.say "But then fair's fair, as I was checking you out too!"
    "Now I really am in a jam - caught between a rock and a hard place."
    "I have Alexis practically oozing with jealousy at my attention being elsewhere."
    "And then there's Reona, who's always ready to flirt and loves all of the drama."
    show alexis angry
    alexis.say "And who the hell is this, [hero.name]?"
    alexis.say "She seems to think that you know her."
    show alexis upset
    mike.say "I...I do know her..."
    mike.say "This is..."
    show reona normal rightopen at left4 with ease
    "Before I can get the words out, Reona steps in and speaks up for herself."
    "Though I can't tell if she's doing it to help me out or stir things up even more."
    reona.say "Don't worry about it, [hero.name]."
    reona.say "I can speak for myself."
    show reona leftback rightnormal
    reona.say "My name's Reona, and we know each other from college."
    reona.say "[hero.name] and I are study buddies!"
    "I nod hastily, trying to play up the innocent nature of the connection."
    mike.say "That's right, Alexis..."
    mike.say "Ah, Reona...this is Alexis, by the way!"
    mike.say "I've been helping Reona here with her revision."
    show alexis confused
    "Alexis has an odd look on her face right now."
    "Almost like there's a conflict going on inside of her."
    "I can see that her instinct is to get territorial."
    "It's only natural that she would see Reona as a potential rival."
    show alexis normal
    "But there's something holding her back from going on the offensive."
    "Because I've seen her verbally rip other girls apart from much less."
    show alexis happy
    alexis.say "Well, I should think he'd be good at that."
    alexis.say "He was one of the smartest boys in our year."
    show alexis mean at right4
    show reona embarrassed righthold at left
    with ease
    alexis.say "You know, back when we were in high-school together?"
    "It's a fairly blatant attempt to trump Reona."
    "And that makes me even more sure Alexis is hiding something."
    "But just what could it be?"
    show reona happy leftnormal
    reona.say "Well, that sure is fascinating, Alexa..."
    reona.say "But I have somewhere I need to be."
    "With that, Reona turns her attention to me."
    show alexis confused
    show reona normal rightopen
    reona.say "See you soon, [hero.name]..."
    mike.say "Erm..."
    mike.say "You too, Reona!"
    show reona flirt rightpeace
    reona.say "Real soon, I hope!"
    hide reona with easeoutleft
    "Reona turns on her heel and walks away, not looking back once."
    "Alexis and I watch in silence until she's out of sight."
    show alexis at center with ease
    "And then I do all I can to prepare myself."
    "Because I just know a tirade is coming my way."
    show alexis angry
    alexis.say "Did you hear what she called me?!?"
    alexis.say "She called me 'Alexa'!"
    show alexis upset
    mike.say "Geez..."
    mike.say "She just met you, Alexis."
    mike.say "Maybe she just misheard your name?"
    show alexis angry
    alexis.say "No way - that was deliberate!"
    alexis.say "Where do you meet girls like that anyway?"
    mike.say "Girls like what?"
    alexis.say "You know what I mean!"
    alexis.say "Brazen hussies that show themselves off the whole time."
    alexis.say "That stand around wanting all eyes on them, twenty-four seven!"
    show alexis upset
    "For a moment I think about calling Alexis out on her blatant hypocrisy."
    "But then I stop myself, partly because I know it's a dumb move."
    "And partly because I'm beginning to see what the problem is here."
    "Maybe putting Reona in front of Alexis is like having her look into a mirror."
    "Alexis might not know that, but she's seeing the similarities between them."
    "And all of the criticism is nothing more than a smokescreen."
    show alexis confused
    mike.say "I get all of that, Alexis..."
    mike.say "But Reona's really been getting a lot out of studying with me."
    mike.say "And she's been on her best behaviour too."
    mike.say "So until that changes, I'll be seeing more of her."
    show alexis annoyed
    "Alexis makes a huffing sound and raises an eyebrow."
    alexis.say "Hmph..."
    show alexis upset
    alexis.say "Well maybe I'll have to sit in on one of these study sessions."
    alexis.say "Just to make sure that brazen tart doesn't forget herself."
    "I nod at this."
    "But I deliberately don't offer anything in the way of a response."
    "Maybe that really would be for the best, to have Alexis there too."
    "Or maybe it'd be like putting two strutting lionesses in the same room together!"
    "Come to think of it, that might be kind of fun."
    "Provided I don't get torn apart in the inevitable cat-fight."
    $ game.flags.thot_harem_delay = TemporaryFlag(True, 1)
    return

label thot_harem_event_02:
    show reona flirt leftpeace rightopen with easeinleft
    reona.say "[hero.name]…"
    reona.say "You have something I want!"
    show reona normal
    "By now I can almost tell what kind of mood Reona's in from the sound of her voice."
    "And from the way she just said all of that, I take it that she's in a particularly flirty mood."
    show reona at center, traveling (1.5, 3.0, (640, 1060))
    "So it's no wonder that my head snaps up a moment later and she has my complete attention."
    "All the same, I still feel the need to at least try to act cool."
    mike.say "Oh yeah?"
    mike.say "And just what would that be, Reona?"
    mike.say "Did you, ah...see something you like?"
    "I'm expecting Reona to respond in kind and keep up the attempt at flirting."
    "Or at least to smile and say that she finds my efforts cute, something like that."
    show reona happy at startle
    "But I'm not prepared for her to shake her head and burst out laughing."
    show reona devious
    reona.say "What?"
    reona.say "Oh, [hero.name]..."
    reona.say "You thought I was talking about you?!?"
    reona.say "Oh, that's so needy and pathetic!"
    show reona sadsmile
    reona.say "It's funny too, but it's mostly needy and pathetic."
    show reona normal
    "I think about trying to brush it off as a mere misunderstanding."
    "That maybe I could claim Reona's actually the one that's mistaken."
    "But then I see that it's too late for anything like that to work."
    "So I just let out a sigh and resign myself to the inevitable embarrassment."
    mike.say "Okay, okay..."
    mike.say "I totally misread the situation there."
    mike.say "Can we just forget about it and get to the point?"
    show reona happy
    "Reona seems happy to do just that."
    show reona normal leftback
    "And when she starts speaking again, it's like nothing happened."
    show reona pensive
    reona.say "So as I was saying..."
    reona.say "You have something that I want, yeah?"
    mike.say "Right..."
    mike.say "And we've already established that's not my firm, manly body."
    show reona flirt
    reona.say "Well, not right now, at least."
    mike.say "So what is it?"
    show reona pensive
    reona.say "I just wondered if you'd let me have Alexis's number, that's all."
    show reona normal
    "For all that I was trying to be casual about this, now I find myself dropping that."
    "Because how am I not going to be intrigued by a request like that?"
    "The girl I'm dating is asking for the number of the girl I'm holding a torch for!"
    mike.say "Alexis's number?"
    mike.say "You want me to give you Alexis's number?"
    show reona pensive
    reona.say "That's what I said, isn't it?"
    reona.say "Sounds like a pretty simple request to me."
    show reona normal
    "I can't help narrowing my eyes at Reona as she explains herself."
    "And that's not just because what she's asking is suspicious in of itself."
    "The way she's looking at me right now and the tone of her voice she's using."
    "Both of them are making me even more paranoid, because they're totally over the top."
    "It's like Reona's deliberately being mysterious while playing it down too."
    mike.say "I beg to differ, Reona!"
    mike.say "Like, what are you going to do when you get it, huh?"
    show reona pensive rightnormal
    reona.say "Oh, I don't know..."
    reona.say "Maybe sell her details to tele-marketers?"
    show reona devious
    mike.say "Reona, you fiend..."
    mike.say "You wouldn't stoop so low, would you?"
    show reona shy
    reona.say "No, you moron!"
    reona.say "I'm just going to call her up, that's all."
    show reona devious
    "I feel a momentary flood of relief."
    "But then I realise the implications of what Reona just said."
    mike.say "You want to speak to Alexis?"
    show reona shy
    reona.say "Yeah."
    show reona devious
    mike.say "Without me there or being able to hear what you say?"
    show reona shy
    reona.say "Pretty much."
    reona.say "And what if I say no?"
    show reona devious
    "Now Reona's attitude changes, becoming nonchalant."
    "She curls her lip and shrugs."
    show reona flirt leftnormal
    reona.say "I dunno..."
    reona.say "Maybe I go ask one of your friends for her number instead?"
    reona.say "Someone like Jack, or that guy who works at the electronics store."
    reona.say "One of them must have it."
    reona.say "And I'd be VERY grateful to them for giving it to me!"
    show reona devious
    "Suddenly I find myself between a rock and a hard space."
    "On the one hand I'm paranoid about Reona and Alexis getting together behind my back."
    "But on the other, I'm jealous of Reona doing stuff with one of my guy friends too."
    "And in the end, I'm more worried about the latter than the former."
    mike.say "Okay, fine..."
    mike.say "I'll let you have Alexis's number."
    mike.say "But promise me you won't do anything with her behind my back."
    show reona happy
    "I watch as the smile on Reona's face turns from sweet to saccharine."
    "And she shakes her head, chuckling softly to herself as she does so."
    show reona shy
    reona.say "Oh, [hero.name]..."
    show reona pensive
    reona.say "Thanks for the number."
    reona.say "But you know I can't do that."
    reona.say "Because I never make a promise that I can't keep!"
    hide reona with easeoutleft
    "With that, Reona leaves me wondering if I just did the right thing."
    "Or if I made a mistake that'll soon come back to haunt me."
    $ game.flags.thot_harem_delay = TemporaryFlag(True, 1)
    return

label thot_harem_event_03:
    scene bg mall2 with fade
    "I can't quite remember what it was that I came down to the mall for."
    "The place sometimes has that effect on me, making me become forgetful."
    "It must be something to do with the artificial light and the air from the AC units."
    "Before I know it, I'm kind of drifting off into a haze as I wander around the place."
    "I find myself window shopping and not really aware of where I'm going or why."
    "And it takes something pretty note-worthy to snap me back to reality again."
    show reona zorder 2 at center, zoomAt(1.0, (900, 720)), dark
    show alexis zorder 1 at center, zoomAt(1.0, (1100, 720)), dark
    with easeinright
    "But the sight of Reona and Alexis appearing out of a store together..."
    "Yeah, that'll do it!"
    "But it can't really be the two of them, can it?"
    "I shake my head, trying to clear out the mall-induced fog."
    hide reona
    hide alexis
    show reona zorder 2 at center, zoomAt(1.0, (900, 720))
    show alexis zorder 1 at center, zoomAt(1.0, (1100, 720))
    with dissolve
    "And when I've managed to regain my senses, I see that I wasn't mistaken."
    "It's definitely Reona and Alexis, both clutching an armful of shopping bags."
    show reona zorder 2 at center, traveling(1.1, 2.0, (860, 760))
    show alexis zorder 1 at center, traveling(1.1, 2.0, (1060, 760))
    "Not only that, they're walking along arm-in-arm too."
    "And they're chatting away like the oldest besties in the world!"
    "I'm standing there, my jaw hanging open as I stare in their direction."
    "But luckily for me, I happen to have stopped somewhere out of their line of sight."
    "Even so, I take a step backwards, just to make sure that I'm not spotted."
    hide reona
    hide alexis
    with easeoutright
    "That means I can watch in safety as they walk off towards another store."
    "Before my head was filled with cotton-wool from the atmosphere of the mall."
    "But now it's spinning as I try to make sense of what I've just seen."
    "I remember that Reona strong-armed Alexis's number out of me a little while back."
    "So it seems like this must have been what she had in mind when she asked for it."
    "And it should be a pretty innocent thing, right?"
    "I mean, all they seem to be doing is shopping together."
    "But somehow my mind can't stop spinning up wild theories about what's going on here."
    "If she just wanted to hook up with Alexis to go shopping, then why not tell me?"
    "What's the reason for keeping me out of the loop like that?"
    "More importantly, what am I going to do about it?"
    menu:
        "Follow them":
            "For a moment I wonder if the right thing to do would be to just walk the other way."
            "After all, I don't want to be accused of spying on Reona and Alexis."
            "But the fear of that just isn't enough to keep me from following them."
            "So I end up doing the best I can to shadow the pair as they walk through the mall."
            scene bg mall1
            show reona zorder 2 at center, zoomAt(1.25, (840, 880))
            show alexis zorder 1 at center, zoomAt(1.25, (1140, 880))
            with fade
            $ game.room = 'mall1'
            "The only problem is that I'm far from an expert when it comes to that kind of thing."
            "When Reona and Alexis stop to look in a window, I must be too close."
            show reona surprised at startle
            show alexis surprised at startle
            "Close enough for them to see my reflection in the glass!"
            show reona zorder 2 at center, traveling(1.25, 0.5, (440, 880))
            show alexis happy zorder 1 at center, traveling(1.25, 0.5, (840, 880))
            alexis.say "Well, well, well..."
            alexis.say "Will you look who it is!"
            show alexis normal
            show reona pensive
            reona.say "Hey there, [hero.name]…"
            reona.say "Aren't you going to come over and say hello?"
            show reona happy
            "The pair of them turn to face me."
            "Which, of course, means the game is up."
            mike.say "I..."
            mike.say "Erm..."
            mike.say "I was just going to say hi, honestly!"
            "I'm obviously embarrassed to have been caught in the act."
            "But I can see that Reona and Alexis aren't in the least bit upset."
            "In fact they seem more amused to see me than anything else."
            "A fact which I choose to take as a good omen for what lies ahead."
            show reona pensive
            reona.say "Of course you were."
            show reona normal
            show alexis wink
            alexis.say "Let me guess..."
            alexis.say "You were just choosing your moment?"
            show alexis normal
            mike.say "Something like that."
            mike.say "But that's enough about me."
            mike.say "What brings you ladies to the mall on this fine day?"
            show alexis annoyed
            show reona annoyed
            "Reona and Alexis exchange a knowing glance."
            "Then they hold up their numerous bags."
            show reona happy
            show alexis normal
            reona.say "Shopping spree, baby!"
            alexis.say "Yeah, [hero.name], this isn't just retail therapy."
            show alexis happy
            alexis.say "It's more like intensive care!"
            "When I first saw Reona and Alexis, I was amazed at the number of bags they have between them."
            "But now that I'm up close, I can see that, if anything, I underestimated just how many there are!"
            mike.say "So, Reona..."
            mike.say "This is what you wanted Alexis's number for?"
            mike.say "Someone to go shopping with?"
            "I thought that I'd nailed it with that one."
            "But much to my frustration, Reona chooses to non-sell the question."
            show reona normal
            reona.say "That's one of the things I wanted it for."
            reona.say "But it's not the only thing."
            show reona happy
            reona.say "Right, Alexis?"
            show alexis normal
            alexis.say "Spot on, Reona!"
            "I feel a moment of frustration as I fail to find out what's really going on here."
            "And then a new level of the same feeling as Reona adds another layer to the mystery."
            "But before I can ask another question, I find myself being cut off."
            reona.say "You do raise an interesting point though, [hero.name]."
            mike.say "Huh?"
            mike.say "I do?"
            show reona normal
            reona.say "Yeah..."
            reona.say "It's because of you that we're here on this shopping spree."
            reona.say "Like, you hooked us up."
            alexis.say "You know, that's true."
            mike.say "And what's that got to do with anything?"
            show reona guilty
            "Reona cocks her head on one side as she begins to explain herself."
            reona.say "Well..."
            show reona devious
            reona.say "That means you technically set all of this up."
            "Wherever Reona's going with this, Alexis seems to be on the same wavelength."
            "Because now she's nodding, like she's backing the other girl up."
            alexis.say "Not only that, it's for your benefit as well."
            show alexis flirt
            alexis.say "Because you'll get to see how good we look in all of this stuff!"
            mike.say "I don't think I like where this is going!"
            show reona happy
            reona.say "It's only fair, [hero.name]…"
            reona.say "Fair that you pick up the tab for all of this."
            menu:
                "Deal with that Prada devil" if hero.money >= 600:
                    "I'm about to ask Reona if she's lost her mind."
                    "But then I stop and actually think about it for a moment."
                    "Because maybe there's a way to turn this to my advantage."
                    mike.say "Okay, Reona..."
                    mike.say "You've got a deal."
                    show alexis surprised
                    show reona shock
                    "Reona and Alexis look more than a little surprised at my answer."
                    "But they soon manage to recover their cockiness and confidence."
                    show alexis happy
                    show reona happy
                    "That done, they begin clapping their hands in a little impromptu celebration."
                    mike.say "But..."
                    show reona embarrassed
                    show alexis annoyed
                    show fx question as reonafx at left
                    show fx question as alexisfx at right
                    "That one word brings a halt to those celebrations a moment later."
                    "As they stop and stare at me, waiting to hear what's coming next."
                    mike.say "Come on guys..."
                    mike.say "You know there had to be a but!"
                    show reona pensive
                    mike.say "And this one is that, if I was technically responsible for all of this..."
                    mike.say "And if I agree to pay for it all..."
                    mike.say "Then I also technically own all the stuff that you've bought."
                    show alexis confused
                    show reona sad
                    "Reona and Alexis exchange a puzzled glance."
                    "Then they look back at me, their confusion not stopping them from objecting."
                    alexis.say "But what do you want with them?!?"
                    reona.say "Yeah, it's not like we take the same size as you!"
                    mike.say "No, no, no..."
                    mike.say "I don't want to wear them myself!"
                    mike.say "The deal is you only get to wear them when you're with me."
                    mike.say "If you're going to look that good and I'm paying..."
                    mike.say "Then I'm going to be the one getting the benefits!"
                    show alexis annoyed
                    show reona pensive
                    "For a moment I think they're going to tell me to go to hell."
                    "But then I see Reona shrug."
                    show reona happy
                    reona.say "Whatever, [hero.name]."
                    reona.say "If it gets me cute clothes for free, you've got a deal."
                    "This seems to be enough to convince Alexis too."
                    "Because she nods and chimes up a second later."
                    show alexis normal
                    alexis.say "Me too..."
                    alexis.say "I'm cool with it."
                    "I nod and hold out my hands, which they both shake."
                    "And so, with the deal done, we set off to the next store."
                    "In the course of what follows, my wallet takes a proper pounding."
                    "But I keep remembering all the stuff that Reona and Alexis have bought."
                    "That's just about enough to keep me from freaking out as they ruin me."
                    with fade
                    "And when I stagger out of the mall, carrying their bags, I'm glad it's finally over."
                    "All I need do now is sit back and wait to reap the rewards of my generosity."
                    $ hero.money -= 600
                "Don't pay for what looks like 600$ worth of clothes":
                    "My reaction is instant and pretty strong."
                    "I take a step backwards, holding up my hands."
                    "And I'm shaking my head like crazy too."
                    show alexis annoyed
                    show reona shy
                    mike.say "Are you crazy?"
                    mike.say "I didn't tell the pair of you to come here."
                    mike.say "And I certainly didn't make you buy all of that shit either!"
                    "Needless to say, Reona and Alexis don't seem pleased with my answer."
                    show reona sad
                    reona.say "Oh come on, [hero.name]…"
                    reona.say "Now you're just being a tight-ass!"
                    show alexis confused
                    alexis.say "She's right, [hero.name]…"
                    alexis.say "You can afford to treat us, I know it!"
                    mike.say "Maybe I can, Alexis..."
                    mike.say "But that doesn't mean you can just make me!"
                    "I turn and wave at the pair of them."
                    "Intending to walk away before this situation gets even more insane."
                    show reona angry
                    $ reona.love -= 5
                    $ reona.sub -= 5
                    reona.say "Well don't think you're going to see me in any of this stuff, you miser!"
                    show alexis angry
                    $ alexis.love -= 5
                    $ alexis.sub -= 5
                    alexis.say "And you're going to kick yourself if you ever do, [hero.name]…"
                    alexis.say "Because we look hot as hell in what we bought!"
                    hide alexis
                    hide reona
                    with dissolve
                    "I'm still shaking my head as I walk away from Reona and Alexis."
                    "Because I simply can't believe the audacity of them."
                    "Actually suggesting that I should bankroll their spending!"
                    "Urgh..."
                    "I should never have given Reona that damn number."
                    "And I should have known they'd be a bad influence on each other two."
                    "It seems that Reona and Alexis bring out the worst in their respective characters."
                    "One exacerbating the other and then feeding off of the results."
                    "I don't know if this friendship's going to last or implode in spectacular fashion."
                    "But until I do know, I'm going to have to keep a close eye on those two."
        "Let them be and mind your own business":
            "I think about following them, to see where all of this is leading."
            "But then I stop myself, actually thinking about the consequences."
            "If they see me creeping about and spying on them, I'll be in big trouble."
            "So maybe the best thing is to just leave it alone and walk the other way?"
            "After all, I'm sure Reona and Alexis will tell me about it in good time."
            "Plus, this way I don't end up looking like some kind of crazed stalker."
            "My mind made up, I turn and walk off in the opposite direction."
            "All the time telling myself that I'm making the right decision."
    $ game.flags.thot_harem_delay = TemporaryFlag(True, 1)
    return

label thot_harem_event_04:
    if bree.is_gone_forever and sasha.is_gone_forever:
        "As usual, I'm home alone tonight."
    elif bree.is_gone_forever:
        "I'm home alone tonight, as Sasha is off doing her own thing."
        "And from what she told me, she is going to be back late."
    elif sasha.is_gone_forever:
        "I'm home alone tonight, as [bree.name] is off doing her own thing."
        "And from what she told me, she is going to be back late."
    else:
        "I'm home alone tonight, as [bree.name] and Sasha are both off doing their own thing."
        "And from what they've told me, neither of them is going to be back until late."
    "So I have the whole house to myself and nobody to stop me doing whatever the hell I want!"
    "But you know how it is when you find yourself in a situation like that, right?"
    "You always end up slumped on the sofa, flicking through the TV channels and bored to death."
    "It's almost like being free to do anything means you can't decide on anything too."
    "I keep glancing out of the window at the encroaching darkness, wishing for something to happen."
    if bree.is_gone_forever:
        "Maybe Sasha will have a bad date or start feeling ill."
        "Then she'd have to come home and I'd have someone to talk to!"
        "No, that's such a bloody selfish thing to wish for."
    elif sasha.is_gone_forever:
        "Maybe Bree will have a bad date or start feeling ill."
        "Then she'd have to come home and I'd have someone to talk to!"
        "No, that's such a bloody selfish thing to wish for."
    else:
        "Maybe one of the girls will have a bad date or start feeling ill."
        "Then they'd have to come home and I'd have someone to talk to!"
        "No, that's such a bloody selfish thing to wish for."
    "Surely I can hack one boring night in on my own?"
    "I'm just steeling myself for the challenge ahead."
    "Lying on the sofa and staring at the ceiling."
    "And that's when I hear it."
    "A sound coming from the back of the house, maybe in the garden."
    "Sitting up, I frown as I stare in the general direction of the noise."
    "But then I just dismiss it as the wind blowing something over out there."
    "Or maybe a cat doing the same as it darts through the back garden."
    "Hell, we've even has foxes trying their best to get into the garbage."
    "So I just assume that it's nothing to worry about and lie back down on the sofa."
    "But a moment later I hear another sound, louder and closer this time."
    "And I swear that it's followed by muffled voices too!"
    "Okay, now I'm starting to get a little worried."
    "I drag myself up from the sofa and start walking to the back of the house."
    "All the time I keep on telling myself that I was probably right the first time."
    "Most likely there's nothing out there to worry about."
    "But all the same, it makes sense to at least check it out."
    "And no, I'm not even thinking about calling the police right now."
    "Because if it does turn out to be something trying to eat the trash..."
    "Well then I'm going to look like a complete fool when officers turn up to investigate."
    "So for now I'll just creep up to the window and take a look into the garden."
    "It looks like the curtains are open and the lights are on out there."
    if bree.is_gone_forever:
        "This is probably the first time I've been glad of Sasha leaving them on."
        "Normally I'd be lecturing her about wasting power and hiking up the household bills."
        "But right now her laziness means I can see out into the garden with ease."
    elif sasha.is_gone_forever:
        "This is probably the first time I've been glad of [bree.name] leaving them on."
        "Normally I'd be lecturing her about wasting power and hiking up the household bills."
        "But right now her laziness means I can see out into the garden with ease."
    else:
        "This is probably the first time I've been glad of [bree.name] and Sasha leaving them on."
        "Normally I'd be lecturing them about wasting power and hiking up the household bills."
        "But right now their laziness means I can see out into the garden with ease."
    "I'm creeping up on the window though, trying to keep from being seen."
    scene bg pool at dark, blur(5) with fade
    "And I manage to make it all the way up to the glass without noticing anything suspicious."
    "That is until the moment my nose is a literal inch from the window pane."
    "Because that's when someone pops up on the other side!"
    show reona swimsuit happy at center, zoomAt(1.5, (640, 1040)), dark with vpunch
    reona.say "SURPRISE!"
    with vpunch
    mike.say "AAARGH!"
    show reona surprised with vpunch
    reona.say "WAAAH!"
    "In the confusion that follows, everything seems to happen at once."
    hide reona
    show reona swimsuit surprised at center, zoomAt(1.5, (640, 1040))
    with dissolve
    "I realise that the person on the other side of the window is Reona."
    show reona swimsuit surprised at center, traveling(1.25, 0.5, (640, 880))
    "But even as my brain is trying to make sense of it all, she's already staggering backwards."
    "And as there's a window between the two of us, I can't stop her before it's too late."
    "Which means that Reona goes tumbling backwards and straight into the pool."
    reona.say "Aargh!"
    show reona shock
    reona.say "Help me!"
    hide reona with easeoutbottom
    pause 0.2
    play sound water_splash
    "I hurry to open the door and rush to the side of the pool."
    scene bg pool with fade
    pause 0.3
    show alexis swimsuit surprised at center, zoomAt(1.0, (740, 720)) with easeinright
    "But before I can get there, I see a familiar face has beaten me to it."
    show alexis angry
    alexis.say "What the hell's going on, [hero.name]?!?"
    alexis.say "Have you gone crazy or something?"
    show alexis upset
    "In slow my pace a little as Alexis appears out of the shadows."
    show reona swimsuit shock at center, zoomAt(1.0, (540, 720)) with easeinbottom
    "And I watch as she helps to haul a gasping Reona out of the pool."
    mike.say "Have I gone crazy?"
    mike.say "I'm not the one sneaking around in someone else's garden at night!"
    reona.say "It was..."
    show reona sadfrustrated
    reona.say "Urgh..."
    reona.say "Supposed to be...a surprise..."
    show alexis normal
    alexis.say "Yeah, [hero.name]..."
    alexis.say "A surprise pool party!"
    "It's only now that I notice Alexis and Reona are wearing swimsuits."
    "How on earth did I not see that before?"
    mike.say "A surprise pool party?"
    show alexis angry
    alexis.say "Yeah, you dope!"
    alexis.say "We were just going to drop in and see if you wanted to hang out."
    alexis.say "But then we saw your housemates leaving."
    show alexis upset
    show reona shout
    reona.say "And we thought we'd do something nice to for you!"
    show reona normal
    "I'd be feeling like a total fool right now."
    "But what's stopping that is the strangeness of it all."
    mike.say "And what..."
    mike.say "You just happened to have swimsuits with you?"
    "Alexis and Reona nod at this."
    show alexis normal
    alexis.say "Okay, I know that sounds totally random."
    show reona shout
    reona.say "But it's the truth, [hero.name]!"
    reona.say "We just wanted to hang-out and have some fun."
    show alexis annoyed
    alexis.say "But we'll get out of your hair, if that's what you want?"
    "Alexis asks the question in that knowing way girls have."
    "When they're making sure your eyes are totally fixed on them."
    "And they just know you're going to give them the answer they want."
    mike.say "Oh, no way..."
    mike.say "You can totally stay and hang-out with me!"
    mike.say "Actually, a surprise pool party sounds like a great idea."
    show alexis wink
    show reona normal
    "Alexis shoots Reona a knowing glance."
    "Which I guess means that they've got me totally where they want me."
    "But you really think I'm going to complain about that?"
    "I get to trade in a boring evening alone for time in the pool with the both of them!"
    mike.say "Just make yourselves comfortable, okay?"
    mike.say "I need to nip inside and change into something more appropriate!"
    scene bg livingroom with fade
    "I hurry back into the house and rush to my room."
    scene bg bedroom1 with fade
    "And once there, I tear off my clothes so I can pull on my trunks."
    "Then I dash back to the side of the pool, ready to have fun in the water."
    "When I arrive, Alexis and Reona are lounging around as they wait for me."
    scene bg pool
    show alexis swimsuit at center, zoomAt(1.0, (840, 720))
    show reona swimsuit shout at center, zoomAt(1.0, (440, 720))
    with fade
    reona.say "Now that's more like it!"
    show reona happy
    show alexis happy
    alexis.say "Yeah, [hero.name]..."
    alexis.say "This is starting to feel like a real party!"
    show alexis normal at center, traveling(1.25, 0.3, (840, 880))
    show reona shout at center, traveling(1.25, 0.3, (440, 880))
    "Alexis crawls over to me on one side, Reona on the other."
    show alexis at center, traveling(1.5, 0.3, (940, 1040))
    show reona shout at center, traveling(1.5, 0.3, (340, 1040))
    "Then they reach up and take hold of my hands, pulling me down towards them."
    "I'm more than happy to let them have their way."
    "So I'm soon sitting on the poolside tiles between them."
    "And they're crouching to either side, hands all over me."
    mike.say "So..."
    mike.say "What kind of games are we going to play at this party of ours?"
    show alexis happy
    show reona happy
    "Alexis and Reona share a chuckle at the question."
    "And I can already feel their hands moving downwards."
    alexis.say "Oh, lot's of fun games."
    alexis.say "More fun than you can handle!"
    show alexis normal
    show reona shout
    reona.say "But the problem is that you kind of got the dress-code wrong..."
    reona.say "And you're wearing far too much for this kind of party!"
    show reona happy
    call thot_harem_pool_fuck from _call_thot_harem_pool_fuck
    scene bg pool
    show alexis swimsuit happy at center, zoomAt(1.5, (840, 1040))
    show reona swimsuit happy at center, zoomAt(1.5, (440, 1040))
    with fade
    "As soon as we're able, we snatch up our swimming costumes and get dressed again."
    "And as we do so, reality slowly begins to dawn on me as to what we've been doing."
    "Where before I couldn't have cared less, now I'm wondering if the neighbours heard us."
    "So as the impromptu pool party comes to an end, I'm already feeling a little paranoid."
    "But the same can't be said for Alexis and Reona, who just look rather pleased with themselves."
    "Just to be clear, it's not that I regret doing this."
    "And I'd probably be up for doing it again in the future."
    "Just maybe at one of the girl's places, rather than mine!"
    $ game.flags.thot_harem_delay = TemporaryFlag(True, 1)
    $ Harem.join_by_name("thot", "alexis", "reona")
    return

label missed_thot_harem_event_05(from_cancel=False):
    if not from_cancel:
        "Shit, I missed my date. Alexis and Reona are going to be mad."
        $ alexis.love -= 10
        $ reona.love -= 10
    return

label thot_harem_event_05(appointment=None):
    $ DONE["thot_harem_event_05"] = game.days_played
    scene bg street with fade
    "It's pretty obvious that Alexis and Reona have more than hit it off since they met."
    "And rather than try to keep the two of them apart, I've decided to do the opposite."
    "Firstly because I figure that discouraging their friendship will just make it stronger."
    "And secondly because what kind of an idiot would I be not to want them to get along?"
    "Alexis and Reona are wanting to spend more time together, for sure."
    "But they're also keen on including me in whatever they're doing as well."
    "And what sane guy doesn't want to hang-out with two hot girls at once?"
    "So that's why I've invited them both along to a nightclub this evening."
    "I figure it's the perfect place for us to have a good time together."
    "A few drinks, some intimate conversation and plenty of up-close dancing."
    "That sounds like the recipe for a great night out."
    "And maybe even the first step along the way to something a little more exciting too!"
    "At least it will be if Alexis and Reona ever bother to show up tonight."
    "I made sure that I got here on time, but there's no sign of them."
    "Already in the queue for the nightclub, I'm starting to get worried."
    "And I'm just about to pull out my phone to call them..."
    alexis.say "Hey, [hero.name]..."
    "But before I can do so, there's the sound of Alexis's voice."
    show alexis sexydate at center, zoomAt(1.0, (1100, 720)) with easeinright
    "Which makes me look up and in her direction."
    reona.say "Hi, [hero.name]..."
    show reona sexydate at center, zoomAt(1.0, (140, 720)) with easeinleft
    "A second later I hear Reona calling to me as well."
    "This means that my head is turning this way and that."
    show alexis at center, traveling(1.25, 0.5, (840, 880))
    show reona at center, traveling(1.25, 0.5, (440, 880))
    "So it's not until they're both standing in front of me that I manage to concentrate."
    "And that's the very moment that I get to see what the two of them are wearing for the first time."
    mike.say "Whoa..."
    mike.say "I mean, whoa..."
    "Alexis and Reona must have planned this between them."
    "Because they're both wearing outfits that leave nothing to the imagination."
    "And somehow they seem to have managed to coordinate them as well."
    "So they also complement each other almost perfectly too."
    show alexis talkative
    alexis.say "What's gotten into you, [hero.name]?"
    show alexis normal
    show reona shout
    reona.say "Yeah..."
    reona.say "Is there something wrong?"
    show reona normal
    $ renpy.dynamic(alexis_score=0, reona_score=0)
    menu:
        "Sorry, I was just stunned by how good looking you are":
            "The questions seems to help shake me out of my confusion."
            "I find myself shaking my head, more to regain my senses than anything else."
            mike.say "Something wrong?"
            mike.say "Are you kidding?"
            mike.say "With you guys looking so good, how could anything be wrong?!?"
            "Reona's look of confusion quickly turns into one of beaming pride."
            "And she exchanges a knowing glance with Alexis."
            show reona shout
            reona.say "Did you hear that?"
            reona.say "Sounds like we got the seal of approval for our outfits!"
            show reona normal
            show alexis talkative
            alexis.say "Well, I can't say that I blame him, Reona..."
            alexis.say "We are looking totally stunning tonight."
            show alexis normal
            "I make room so that Alexis and Reona can join me in the queue."
            "But all the time I'm doing so, I can't stop staring at them."
            "The only thing that stops me is when Reona glances around."
            "And I see that she has a slightly nervous look on her face."
            show reona shout
            reona.say "Hey..."
            reona.say "You don't think we've overdone it, do you?"
            show reona normal
            mike.say "What makes you say that?"
            show reona shout
            reona.say "Well, people are kinda staring at us!"
            show reona normal
            show alexis annoyed
            "Alexis lets out a snort and shakes her head."
            alexis.say "Hmpf..."
            show alexis talkative
            alexis.say "Of course they are, Reona..."
            alexis.say "We already established that we look crazily hot!"
            show alexis normal
            mike.say "Alexis is right, Reona..."
            mike.say "People are just checking you out, that's all."
            "Reona nods, seemingly reassured by my explanation."
            $ alexis_score += 1
            $ reona_score += 1
        "Yeah, coming naked would have been the same thing...":
            "The questions seems to help shake me out of my confusion."
            "I find myself shaking my head, more to regain my senses than anything else."
            mike.say "You bet there's something wrong!"
            mike.say "Could you guys have worn anything more revealing?"
            show alexis annoyed
            show reona guilty
            "Alexis and Reona are instantly taken aback by the question."
            "I can see frowns forming on faces and arms being crossed."
            show alexis whining
            alexis.say "We're going to a night-club, for god's sake..."
            alexis.say "Not a damn funeral!"
            show alexis annoyed
            show reona angry
            reona.say "Why are you being like this, [hero.name]?"
            reona.say "You don't normally complain when I dress like this."
            show reona normal
            "I look around, becoming aware of all the eyes that are on us."
            "And I can imagine every guy here leering at Alexis and Reona."
            "Hell, most of the girls are probably doing the same thing too!"
            mike.say "I don't complain when it's me getting to see it, Reona."
            mike.say "But right now you're on display for everyone in the queue."
            mike.say "People are going to be hitting on you all night!"
            "Alexis rolls her eyes and turns to Reona."
            show alexis whining
            alexis.say "That sounds like a you problem, [hero.name]."
            alexis.say "Isn't that right, Reona?"
            show alexis annoyed
            show reona shout
            reona.say "Now that you mention it, Alexis..."
            reona.say "It really does!"
            show reona normal
            "With that they join the queue, leaving me to follow on their heels."
            "And all the time I can feel the eyes of the other clubbers on me."
            "Almost like they're sensing me being undermined a little more each passing moment."
            $ alexis_score -= 1
            $ reona_score -= 1
    scene bg alley
    show alexis sexydate at center, zoomAt(1.25, (840, 880))
    show reona sexydate at center, zoomAt(1.25, (440, 880))
    with fade
    "Luckily for us, the queue seems to be moving pretty quickly tonight."
    "Which means that it's not long before we're getting to the front of the line."
    "But when there's only a couple of people in front of us, I spot something worrying."
    mike.say "Ah..."
    mike.say "I think we're in trouble!"
    show reona shout
    reona.say "Huh?"
    show reona normal
    show alexis whining
    alexis.say "What's the problem?"
    show alexis sadsmile
    mike.say "They're taking people's names."
    mike.say "I think this is the VIP line or something."
    "All three of us are staring at the length of the line behind us."
    "And at what we're only now figuring out is the general admission line."
    "So nobody's actually paying attention to where we are in the queue."
    show dwayne as doorman zorder 4 at center, zoomAt(1.5, (1160, 1000)), blacker with dissolve
    "Doorman" "What name is it?"
    "All three of us turn around as one."
    "But I manage to make sure I'm the one that speaks up for us."
    if hero.charm >= 90:
        "Sure, there's a lot of potential pressure building up here."
        "But all that means is there's the need for someone to diffuse it."
        "With that in mind, I step up to talk to the doorman."
        mike.say "Yeah, we're not on the list..."
        mike.say "But I've been here a hundred times before."
        mike.say "Just let us in and we'll go straight to the main bar."
        "The doorman looks at me with obvious irritation."
        show dwayne as doorman at center, zoomAt(1.5, (1160, 1000)), startle
        "Doorman" "I don't think so, buddy."
        "Doorman" "I need you to go join the other queue."
        "I put a smile on my face as I follow his gaze."
        mike.say "Actually, I think what you need is to get this queue moving."
        mike.say "People don't like paying VIP rates to stand in line like schmucks."
        mike.say "Be quicker to just trust me and let it go, don't you think?"
        "For a moment I think the guy's going to stick to his guns."
        "But then I swear I see his left eye twitch."
        "And the next thing I know, he nods his head."
        show dwayne as doorman at center, zoomAt(1.5, (1160, 1000)), startle
        "Doorman" "Okay, get your asses inside."
        "Doorman" "But if I catch you in the VIP section..."
        "He lets the threat hang in the air as we scuttle inside."
        "But it soon fades from my mind when I see the impressed looks I'm getting from the girls."
        "I guess I managed to handle that pretty smoothly!"
    else:
        "I can already feel the pressure beginning to build up."
        "And I guess it must be making me a little edgy."
        "Because I really can't think of anything to do here."
        "Anything other than throwing myself on the doorman's mercy."
        mike.say "We're not on the list!"
        mike.say "We just joined the wrong queue by mistake."
        mike.say "Could you maybe..."
        mike.say "Just let us in this way?"
        "The doorman looks unimpressed with my begging."
        "And he doesn't even make eye-contact as he waves me away."
        show dwayne as doorman at center, zoomAt(1.5, (1160, 1000)), startle
        "Doorman" "Look, that's not my problem, buddy."
        "Doorman" "I got a long line of people behind you."
        "Doorman" "People smart enough to check what line they're in."
        "Doorman" "So get the hell out of my face already."
        "After that all I can do is turn and slink away."
        "And even as I do so, I can feel Alexis and Reona staring at me."
        "Their eyes bore into the back of my head as we walk to the correct queue."
        "And the stony silence endures as we begin to stand in line all over again."
        $ alexis_score -= 1
        $ reona_score -= 1
    scene bg nightclub
    show alexis sexydate at center, zoomAt(1.25, (840, 880))
    show reona sexydate at center, zoomAt(1.25, (440, 880))
    with fade
    "Once we're actually through the doors and inside the nightclub, I feel my spirits start to rise."
    "Because it's just like I hoped it would be in here, with a lively, practically buzzing atmosphere."
    "And I can see that Alexis and Reona are feeling it too, starting to forget the pains of the queue."
    mike.say "Okay, guys..."
    mike.say "What should we do first?"
    mike.say "Grab a drink or hit the dance-floor?"
    show reona shout
    reona.say "I'd kinda like to get a drink."
    show reona normal
    show alexis talkative
    alexis.say "Huh..."
    alexis.say "I wanted to dance first!"
    show alexis normal
    "I open my mouth to speak."
    "Preparing to step in before they start an argument."
    "But someone else beats me to the punch."
    audrey.say "Just make [hero.name] here get the drinks."
    audrey.say "Then have him bring them to you by the dance-floor."
    show alexis sexydate zorder 1 at center, traveling(1.0, 0.3, (640, 720))
    show reona sexydate zorder 2 at center, traveling(1.0, 0.3, (340, 720))
    show audrey sexydate zorder 3 at center, zoomAt(1.0, (940, 720)) with easeinright
    "Alexis and Reona both turn to look at the new arrival."
    "Probably wondering how some random girl in the club knows my name."
    "But I don't need to see her face to be able to place that voice."
    mike.say "Audrey..."
    mike.say "What an unexpected pleasure!"
    "If Audrey senses the sarcasm in my voice, she chooses to ignore it."
    show alexis sexydate zorder 2 at center, traveling(1.0, 0.3, (940, 720))
    show audrey sexydate zorder 3 at center, traveling(1.25, 0.3, (640, 880))
    "And instead she places herself right between me and the girls."
    show audrey joke
    audrey.say "That's my name, don't wear it out!"
    show audrey mock
    audrey.say "And who are your friends over here?"
    show audrey normal
    "I can see that Alexis and Reona are looking at me with interest."
    show alexis sexydate zorder 1 at center, traveling(1.15, 0.3, (940, 800))
    show reona sexydate zorder 2 at center, traveling(1.15, 0.3, (340, 800))
    show audrey sexydate zorder 3 at center, traveling(1.15, 0.3, (640, 800))
    "Obviously seen to see who this rather forward girl might be."
    mike.say "This is Alexis and Reona."
    mike.say "Guys, this is Audrey."
    show audrey joke
    audrey.say "I work under him..."
    audrey.say "If you know what I mean!"
    show audrey normal
    "Alexis and Reona seem to pick up on a joke that flies over my head."
    show reona happy at startle
    show alexis happy at startle
    "Because suddenly they're both laughing away merrily."
    show reona normal
    show alexis normal
    mike.say "Audrey's one of the admin people at my office."
    mike.say "She works under a lot of other people too!"
    "This explanation doesn't seem to help much, as they only laugh even louder."
    "Plus now Audrey's joining in too, which makes matters that much worse."
    show alexis talkative
    alexis.say "I know just what you mean, Audrey!"
    show alexis smile
    show reona shout
    reona.say "Me too, me too..."
    reona.say "You should come have a dance with us."
    show reona devious
    show alexis talkative
    alexis.say "And tell us more about what [hero.name] gets up to at work!"
    show alexis smile
    "By now all three of them are looking straight at me."
    "And the smiles on their faces are oddly disconcerting."
    "It's about then that a sinister thought begins to occur to me."
    mike.say "Wait a minute..."
    mike.say "You guys didn't, like..."
    mike.say "You didn't plan this, did you?"
    show audrey stuned
    show alexis stuned
    show reona surprised
    "Now they're all looking at each other in surprise."
    "Like they can't believe what I'm suggesting."
    show audrey surprised
    audrey.say "Oh come on, [hero.name]..."
    audrey.say "I never met these guys until a couple of minutes ago!"
    show audrey sadsmile
    show alexis surprised
    alexis.say "You really think we'd plan something like this?"
    alexis.say "With a random girl from your work?"
    show alexis sadsmile
    show reona surprised
    reona.say "That's totally crazy, [hero.name]!"
    show reona sadsmile
    "I can't help narrowing my eyes as they dismiss my concerns."
    "Not satisfied with their flat denials of a conspiracy."
    "Maybe Alexis and Reona are totally innocent."
    "But I wouldn't put it past Audrey to have been watching us and planning this!"
    "The problem is that it looks like there's been some kind of unconscious decision here."
    "That totally without asking my permission, the girls have added Audrey to our number."
    "I mean I could insist that she makes herself scarce or something."
    "But I get the feeling that wouldn't make me very popular."
    "So it looks like she's sticking with us."
    "At least for the time being."
    show audrey talkative
    audrey.say "Anyway..."
    audrey.say "We have some dancing to do, don't we, girls?"
    audrey.say "And you'd better see to getting those drinks!"
    show audrey normal
    show reona normal
    show alexis normal
    $ renpy.dynamic(audrey_score=0)
    menu:
        "Alright, I'll get you some drinks":
            "Okay, okay..."
            "I have to take a moment to get my head straight here."
            "I know Audrey better than most."
            "And I know that what she likes is drama."
            "So the best way to keep her in line is to defuse things before they get out of hand."
            "With that in mind, I put a smile on my face."
            mike.say "Okay..."
            mike.say "I'll get this round in."
            hide reona
            hide alexis
            hide audrey
            with easeoutright
            "While the three of them hurry off to dance, I head to the bar."
            "And by the time I have everyone's drinks, they're dancing away merrily."
            "The fact I'm not with them means they have a lot of male attention out there."
            "But I take comfort from the fact they're dancing in a tight little circle."
            show alexis sexydate zorder 1 at center, zoomAt(1.15, (940, 800))
            show reona sexydate zorder 2 at center, zoomAt(1.15, (340, 800))
            show audrey sexydate zorder 3 at center, zoomAt(1.15, (640, 800))
            with easeinright
            "And when one of them spots me, they hurry over."
            show alexis talkative
            alexis.say "Oh, thanks, [hero.name]."
            show alexis normal
            show reona shout
            reona.say "You remembered my order!"
            show reona normal
            show audrey talkative
            audrey.say "Bottoms up!"
            show audrey normal
            mike.say "So..."
            mike.say "You guys seem to be getting on pretty well?"
            show alexis happy at startle
            show audrey happy at startle
            show reona happy at startle
            "The question gets me a round of wicked giggles."
            show reona shout
            reona.say "Audrey is so mean!"
            reona.say "Funny with it, but mean."
            show reona normal
            show alexis talkative
            alexis.say "She already told us some great stories about you!"
            show alexis normal
            show audrey talkative
            audrey.say "Hey..."
            show audrey mock
            audrey.say "Every word was the truth!"
            show audrey normal
            "I could be pissed at Audrey gossiping about me."
            "But they all seem to be getting on so well."
            "So instead I choose to brush it off."
            mike.say "I have nothing to hide!"
            show alexis happy at startle
            show audrey happy at startle
            show reona happy at startle
            "This earns me three knowing looks, and then even more giggles."
            $ alexis_score += 1
            $ audrey_score += 1
            $ reona_score += 1
        "If you want drinks go get them, I'll be on the dance floor":
            "If Audrey wanted to win me over to the idea of her coming along with us, then she's not making a good start."
            "Because now she's ordering me around like I'm her personal cocktail waiter!"
            mike.say "You want drinks before we dance?"
            mike.say "Then why don't you get them yourselves?!?"
            "With that, I turn my back and walk towards the dance-floor."
            with fade
            "Audrey, Alexis and Reona are soon following my lead."
            "But almost as soon as we're out there, I sense that I've made them mad."
            show alexis upset zorder 1 at center, zoomAt(1.15, (900, 800))
            show reona sadangry zorder 2 at center, zoomAt(1.15, (380, 800))
            show audrey upset zorder 3 at center, zoomAt(1.15, (640, 800))
            with ease
            "Because they almost immediately form into a tight little knot."
            "And somehow they manage to keep me from breaking into it."
            show alexis normal
            show reona normal
            show audrey normal
            "Yet they also find a way to make it look like they're not keeping me out too!"
            "In the end I have to settle for orbiting around the three of them."
            "And that makes it look like I'm here on my own."
            "So pretty soon they have loads of other guys paying them attention."
            "While I'm just stuck on the edges, trying in vain to get noticed."
            $ alexis_score -= 1
            $ audrey_score -= 1
            $ reona_score -= 1
    show alexis normal zorder 1 at center, zoomAt(1.15, (940, 800))
    show reona normal zorder 2 at center, zoomAt(1.15, (340, 800))
    show audrey normal zorder 3 at center, zoomAt(1.15, (640, 800))
    with fade
    "As the night begins to wear on, one thing is becoming very clear to me."
    "Alexis and Reona aren't just accepting Audrey into our former threesome."
    "They're getting on so well that it's threatening to turn into a foursome!"
    "The more that we all talk, joke and share stories, the more obvious it becomes."
    "Somehow Audrey seems to be just the right shape to plug right in there."
    "Even over the constant noise in the club, we keep on talking most of the night."
    "Occupying a booth in the corner of the place, stubbornly refuse to move."
    "Only occasionally sending someone out for more drinks."
    if hero.energy < 5:
        "At first I really don't notice how late it's getting."
        "Or how tired I'm starting to feel."
        "But then I feel my head dip and my eyes close."
        "And a second later I jolt back awake again."
        "Oh man..."
        "I almost fell asleep!"
        if hero.has_skill("no_sleep"):
            "I make a concerted effort to snap out of it."
            "Doing the best I can to keep myself awake."
            "And by some minor miracle, I manage to pull it off."
            "I keep my eyes open and my head nodding the whole time."
            "That is until Alexis opens her mouth and lets out the biggest yawn possible."
            show alexis surprised
            alexis.say "Eeeurgh!"
            show alexis whining
            alexis.say "Oh wow..."
            alexis.say "Sorry!"
            show alexis sadsmile
            "It only takes seconds for the effect of the yawn to spread."
            "And then the others are all doing it too."
            show reona shout
            reona.say "Oooh..."
            reona.say "Alexis..."
            reona.say "Now you've set me off too!"
            show reona normal
            "I can see that Audrey's doing all she can to fight it."
            "But at the end of the day, she's only human."
            show audrey whining
            audrey.say "Urgh..."
            audrey.say "This is all your fault, [hero.name]..."
            audrey.say "For working me so hard in the office!"
            show audrey normal
            "All I can so is shrug and shake my head."
            mike.say "I don't know what's gotten into you guys."
            mike.say "I could keep this up all night!"
        else:
            "I make a concerted effort to snap out of it."
            "Doing the best I can to keep myself awake."
            "But it's no use, as I feel my eyes closing again."
            "I must fall asleep and wake up a good few times."
            "At least that's what it feels like from my perspective."
            "Until I finally flake out and my head lands on the table."
            "The girls all jump back in surprise."
            "But it's the sound of Reona yelping that wakes me up."
            reona.say "Waaagh!"
            mike.say "Uurgh!"
            mike.say "What the..."
            "I stare at the girls with bleary eyes."
            "But I can still see that they're frowning at me."
            show alexis whining
            alexis.say "What was that all about?"
            show alexis sad
            show reona annoyed
            reona.say "You almost gave me a heart-attack!"
            show reona sad
            show audrey whining
            audrey.say "He fell asleep!"
            audrey.say "Guess he's bored of our company."
            show audrey upset
            "I shake my head desperately."
            "Partly to disagree with Audrey's claims, and partly to try to wake myself up more."
            "But it seems like the damage has already been done."
            $ alexis_score -= 1
            $ audrey_score -= 1
            $ reona_score -= 1
    else:
        "As far as I can see, gossip is being exchanged at an alarming rate right now."
        "Alexis and Reona have begun to bombard Audrey with all that they can think of."
        "She's soaking it all up too, as well as giving as much as she possibly can in return."
        "In fact it's almost making my head spin trying to keep up with it all."
        "That is until the call of nature has to be answered."
        show audrey whining
        audrey.say "Oops..."
        audrey.say "I got to go use the little girl's room!"
        show audrey talkative
        audrey.say "Be right back."
        show alexis normal zorder 1 at center, zoomAt(1.15, (840, 800))
        show reona normal zorder 2 at center, zoomAt(1.15, (440, 800))
        hide audrey
        with easeoutleft
        "Almost as soon as Audrey's out of earshot, Alexis and Reona turn to me."
        show alexis talkative
        alexis.say "Okay, [hero.name]..."
        alexis.say "Make with the dirt on Audrey!"
        show alexis normal
        show reona shout
        reona.say "We want to know it all..."
        reona.say "Every last little detail!"
        show reona normal
        menu:
            "There's a ton to say!":
                "I can't keep a smile from creeping across my face."
                "Because a moment ago they were acting like lifelong friends."
                "And now they're ready to ask for the dirtiest dirt on Audrey."
                "Plus it's a chance for me to get a little revenge on her too!"
                mike.say "Okay..."
                mike.say "I'm going to have to make this quick."
                mike.say "So listen closely..."
                show alexis normal zorder 1 at center, traveling(1.25, 0.3, (840, 880))
                show reona normal zorder 2 at center, traveling(1.25, 0.3, (440, 880))
                "Alexis and Reona lean in close as I begin to spill my guts."
                "And pretty soon they're listening intently as I recount everything."
                "By which I do mean everything."
                "I reel off every single piece of gossip that I can remember."
                "Every time Audrey screwed up at work."
                "Every time she misspoke at a meeting."
                "Even the slightest scrap of humiliating information."
                "I whisper it all into their eagerly listening ears."
                "This earns me a round of nodding heads and disbelieving gasps."
                show alexis normal zorder 2 at center, traveling(1.15, 0.3, (940, 800))
                show reona normal zorder 3 at center, traveling(1.15, 0.3, (340, 800))
                show audrey sexydate zorder 1 at center, zoomAt(1.15, (640, 800)) with easeinleft
                "All of which stops the moment Audrey arrives back from the bathroom."
                show audrey talkative
                audrey.say "Okay..."
                audrey.say "What did I miss?"
                show audrey normal
                show alexis talkative
                alexis.say "Oh, nothing!"
                show alexis normal
                show reona shout
                reona.say "Nothing at all!"
                show reona normal
                $ alexis_score += 1
                $ audrey_score -= 1
                $ reona_score += 1
            "I don't really want to speak badly behind Audrey's back":
                "I can't help frowning at the pair of them."
                "Even shaking my head a little too."
                "As I'm totally amazed by what they're asking of me."
                mike.say "You want me to feed you sensitive facts info on Audrey?"
                mike.say "Like, tell you all of her hidden weaknesses?!?"
                mike.say "I thought you guys were getting on great!"
                show alexis talkative
                alexis.say "It's not like that, [hero.name]!"
                show alexis normal
                show reona shout
                reona.say "Yeah, you make it sound so..."
                reona.say "So..."
                show reona normal
                mike.say "So under-handed?"
                mike.say "It sounds like that because it is!"
                show alexis annoyed
                show reona annoyed
                "Alexis and Reona are really starting to look annoyed with me."
                "Like I'm the one that's in the wrong here!"
                show alexis whining
                alexis.say "It's perfectly normal to want to know this kind of stuff."
                show alexis normal
                show reona shout
                reona.say "You just ask any girl, [hero.name]!"
                show reona normal
                mike.say "So I should ask Audrey when she gets back?"
                "This earns me a round of shaking heads and waving hands."
                show alexis normal zorder 2 at center, traveling(1.15, 0.3, (940, 800))
                show reona normal zorder 3 at center, traveling(1.15, 0.3, (340, 800))
                show audrey sexydate zorder 1 at center, zoomAt(1.15, (640, 800)) with easeinleft
                "Which is just as well, because that's the moment Audrey arrives back from the bathroom."
                show audrey talkative
                audrey.say "Okay..."
                audrey.say "What did I miss?"
                show audrey normal
                show alexis talkative
                alexis.say "Oh, nothing!"
                show alexis normal
                show reona shout
                reona.say "Nothing at all!"
                show reona normal
                $ alexis_score -= 1
                $ audrey_score += 1
                $ reona_score -= 1
    with fade
    "By now it's getting pretty late and everyone's starting to look tired."
    "Sure, they do the best they can to cover it up and act all lively."
    "But the signs are all there and I guess that soon we'll have to call it a night."
    "So with that in mind, I nod towards the dance-floor."
    mike.say "How about one last turn out there?"
    mike.say "You know, to round out the night?"
    "This seems to be just what the girls were wanting to hear."
    "And soon enough I find myself being dragged out onto the dance-floor."
    show audrey talkative
    audrey.say "Great idea!"
    show audrey normal
    show alexis talkative
    alexis.say "Count me in!"
    show alexis normal
    show reona shout
    reona.say "Me too!"
    show reona normal
    "The dance-floor is pretty packed, as everyone seems to have the same idea."
    "But we manage to find ourselves a spot and claim it, dancing in a tight circle."
    if hero.fitness < 80:
        "Now that we're out here, I sense that the time is right."
        "This is the perfect chance for me to bust out my best moves."
        "Something that's sure to wow the girls."
        if hero.has_skill("dance"):
            "I wait for the right moment, and then I make my first move."
            "Which involves me leaping into the middle of the girls."
            "And then I do a kind of twirly, stretchy thing."
            "Which I pull off so well that all of their eyes are on me."
            show alexis surprised
            alexis.say "WOW..."
            show alexis talkative
            alexis.say "Nice moves!"
            show alexis normal
            show reona shout
            reona.say "Way to go, [hero.name]!"
            show reona normal
            show audrey talkative
            audrey.say "Damn it..."
            audrey.say "Where did you learn to do that?!?"
            show audrey normal
            "I can already feel the sensation of my head beginning to swell."
            "Because the praise that I'm getting right now is pretty sweet."
            "So I keep on dancing, piling on the great moves."
            "And it doesn't take long for them to join in too."
            "All three of them are doing the best they can to match my movements."
            "But despite their efforts, none of them are able to keep up with me."
            "Which means that I walk off the dance-floor feeling like a conquering hero."
            $ alexis_score += 1
            $ audrey_score += 1
            $ reona_score += 1
        else:
            "I wait for the right moment, and then I make my first move."
            "Which should involve me leaping into the middle of the girls."
            "And then the plan is to do a kind of twirly, stretchy thing."
            "It should look really impressive and get all of their eyes on me."
            "But the best I can say is that it definitely achieves the latter."
            "Instead one of my legs shoots out in front of me."
            "And at the same time the other slides out behind."
            with vpunch
            "This means that I end up hitting the floor."
            "But it also comes along with the sound of something tearing."
            "I don't know if it's my pants or something more personal."
            "Only that whatever's torn, I'm in a lot of pain!"
            mike.say "Aargh!"
            mike.say "Oh god!"
            show audrey whining
            audrey.say "Whoops..."
            audrey.say "That's torn it!"
            show audrey sad
            show reona shout
            reona.say "Oh no!"
            show reona sad
            show alexis whining
            alexis.say "Come on, you guys..."
            alexis.say "Help me get him off the dance-floor!"
            show alexis sadsmile
            "All I can do is wince in pain as they all take hold of me."
            "Then I suffer the humiliation of being carried off the dance-floor."
            "And even when I'm off it, the best I can manage is a weak limp."
    else:
        "We haven't been dancing long when I feel someone pushing into me."
        "And by the time I manage to look around, it's too late."
        "Because a bunch of guys have already pushed their way into our circle."
        "And now they're doing all they can to shove me out of it!"
        if hero.fitness >= 100:
            "Before now I was starting to feel tired and ready to call it quits."
            "But the idea of these guys trying to cut in on our space seems to wake me up again."
            "Suddenly I find a hidden reserve of energy, and I devote it to dealing with them."
            "It means that I have to keep moving most of the time I'm doing it."
            "But I somehow manage to be everywhere they try to break in."
            "And each time they try, I block their efforts and push them back."
            "I have to admit that they're persistent, at least at first."
            "Yet I still manage to outlast them, keeping them out until they give up."
            "All the time this is going on, the girls are watching my efforts."
            "And I can see that they're more than a little impressed."
            "Once we're done and leaving the dance-floor, they leave with me."
            "All three of them draped over my shoulders and hanging off my arms."
            audrey.say "Mmm..."
            show audrey joke
            audrey.say "There was some prime manhood on show back there!"
            show audrey normal
            show alexis talkative
            alexis.say "Yeah, but someone kept them all at bay."
            show alexis normal
            show reona shout
            reona.say "[hero.name] was totally the alpha male!"
            show reona normal
            "I can see all of them stealing glances at me as they talk about it."
            "Almost like they're expecting me to object."
            "But instead I keep quiet."
            "Because I'm secure in the knowledge that I saw off a genuine threat back there."
            $ alexis_score += 1
            $ audrey_score += 1
            $ reona_score += 1
        else:
            "Normally I'd be the first to push back and defend my territory."
            "But it's already late and I'm feeling more than a little tired."
            "Plus I'm pretty sure that I already have a deep connection with the girls."
            "So I'm not worried about a bunch of jerks trying to cut in."
            "Instead of pushing them out, I make room and just keep on dancing."
            "Sure, this earns me a few odd looks from Audrey, Alexis and Reona."
            "But eventually they seem to catch onto the fact I'm not feeling threatened."
            "And so they just accept the situation and keep on dancing too."
            "I'm not even concerned when some of them actually respond to the guys."
            "Because I know that they're only flirting, nothing more."
            "And once we're done dancing, the girls leave the floor with me."
            audrey.say "Mmm..."
            show audrey joke
            audrey.say "There was some prime manhood on show back there!"
            show audrey normal
            show alexis talkative
            alexis.say "I guess those guys were pretty cute."
            show alexis normal
            show reona shout
            reona.say "I thought so too!"
            show reona normal
            "I can see all of them stealing glances at me as they talk about it."
            "Almost like they're expecting me to object."
            "But instead I keep quiet."
            "Because I'm secure in the knowledge those guys were no threat to me."
            $ alexis_score -= 1
            $ audrey_score -= 1
            $ reona_score -= 1
    show bg alley with fade
    "As we leave the club, the next issue starts to play on my mind."
    "Like, are we calling it a night here, or going on somewhere else?"
    "And if we are going somewhere else, then where is it going to be?"
    mike.say "So what's it going to be?"
    mike.say "Are we hailing one taxi or four?"
    "The girls suddenly begin to huddle together, heads down."
    "And I really wish that I could hear what they're saying."
    "But every time I try to move closer, they shuffle further away!"
    "Which means that I have to wait until they're done huddling."
    "Then stand there with baited breath to hear what they have to say."
    if all(score >= 2 for score in (alexis_score, audrey_score, reona_score)):
        show audrey talkative
        audrey.say "Make it one taxi, [hero.name]!"
        show audrey normal
        show alexis talkative
        alexis.say "Yeah, we're having a great time with you!"
        show alexis normal
        show reona shout
        reona.say "And we don't want it to end yet either!"
        show reona normal
        "I'm obviously pleased to hear their answer."
        "And I'm about to say something in return."
        show bg taxi car with fade
        "But they're already flagging down a cab."
        "And none of them hesitate to leap inside, pulling me after them."
        $ Harem.join_by_name("thot", "audrey")
        $ DONE["thot_harem_event_06"] = game.days_played
        call thot_harem_event_06 from _call_thot_harem_event_06
    else:
        show audrey whining
        audrey.say "Let's make it two taxis, [hero.name]!"
        show audrey sad
        show alexis whining
        alexis.say "That is one for the three of us."
        show alexis sad
        show reona shout
        reona.say "And a different one for you!"
        show reona normal
        "I stand there dumbstruck for a moment."
        "Totally not understanding what they mean."
        mike.say "Wha..."
        mike.say "What are you..."
        show bg taxi car with fade
        "As I'm stuttering and stammering, they're already flagging down a cab."
        "And none of them hesitate to leap inside, closing the doors behind them."
        show audrey mock
        audrey.say "Sorry, [hero.name]..."
        audrey.say "But we're ditching your sorry ass..."
        audrey.say "Because we can have more fun without you!"
        show audrey upset
        "Audrey shouts this out the window as the cab pulls away."
        "Leaving me standing on the street, alone and more than a little pissed off."
    return

label thot_harem_event_06:
    "The taxi ride home from the club is nothing but fun and laughter for all four of us."
    scene bg house
    show alexis sexydate zorder 2 at center, zoomAt(1.15, (940, 800))
    show reona sexydate zorder 3 at center, zoomAt(1.15, (340, 800))
    show audrey sexydate zorder 1 at center, zoomAt(1.15, (640, 800))
    with fade
    "But almost the moment the cab pulls up outside my place, realisation begins to dawn on me."
    "Because now I somehow have to get three less than sober girls into the house and to my bedroom!"
    "Normally I'd be trying to shush them all and keep things quiet, but I don't think that'll work."
    "The only other thing I can think of is to take the complete opposite approach."
    "So as soon as we're standing on the pavement, I give the signal for them to follow me."
    mike.say "Come on guys..."
    mike.say "Last one inside and to my room!"
    "Without another word of explanation, I turn on my heel and make a dash for the porch."
    "And once I get to the front door, I have a mere fraction of a second to unlock it."
    show bg livingroom with fade
    "Because Audrey, Alexis and Reona are all right behind me, racing to keep up."
    "Stepping neatly to one side, I point them in the direction of my room."
    "Then I close the door, making sure it's locked before I hurry after them."
    show bg bedroom1 with fade
    "I arrive just in time to follow the last of them into the room as the door closes."
    "And only when it's firmly shut do I allow myself the chance to actually relax."
    "Or at least I would have done, if the three of them didn't choose that moment to pounce!"
    show alexis sexydate zorder 2 at center, zoomAt(1.25, (940, 880))
    show reona sexydate zorder 3 at center, zoomAt(1.25, (340, 880))
    show audrey sexydate zorder 1 at center, zoomAt(1.25, (640, 880))
    with hpunch
    "Before I know what's happening, three pairs of hands have a firm hold on me."
    "And there's nothing I can do to keep from being dragged towards the bed."
    show audrey talkative
    audrey.say "That's right..."
    audrey.say "Toss him on the bed!"
    show audrey normal
    show alexis talkative
    alexis.say "I'll take his shirt..."
    alexis.say "Reona, you handle his pants!"
    show alexis normal
    show reona shout
    reona.say "I'm on it!"
    show reona normal
    "I'd say that I'm fighting and struggling for all that I'm worth right now."
    "But who am I trying to kid?"
    "Three hot girls want to jump me, pin me to a bed and strip me naked."
    "And you think I'm dumb enough to actually try and stop them?"
    "I offer up no resistance whatsoever as I'm manhandled onto the bed."
    "And in less than a minute, I'm stripped down to my skin."
    "But that doesn't mean that all three of them are working on me at once."
    "Looking up I can see that they're taking it in turns to stop holding onto me."
    "And the one of them that's freed up takes the chance to strip off themselves."
    show audrey naked with dissolve
    "First Audrey pulls off her clothes, then she swaps with Alexis."
    show alexis naked with dissolve
    "And as soon as she's naked too, she makes the swap with Reona."
    show reona naked with dissolve
    "Soon enough I find myself staring up at three totally naked girls."
    "Well, if I'm honest, mainly staring at the six breasts that are hanging over me!"
    mike.say "Whoa..."
    mike.say "Did I die on the way home from the club?"
    mike.say "Because I'm in heaven right now, and surrounded by angels!"
    "It's a really cheesy line, I know it."
    "And the girls can't help rolling their eyes."
    "But I can see that they appreciate the sentiment."
    show alexis smile
    show reona happy
    "At least Alexis and Reona are smiling sweetly down at me."
    show audrey mock
    "Though the smile on Audrey's face looks different, more like a wicked grin."
    "Concentrating on her face, I have no chance of seeing what her hands are doing."
    call thot_harem_foursome_fuck from _call_thot_harem_foursome_fuck
    with fade
    if renpy.has_label("thot_harem_achievement_5") and not game.flags.cheat:
        call thot_harem_achievement_5 from _call_thot_harem_achievement_5
    "There's no chance of us doing anything more once the fun is finally over."
    "The most that I'm capable of is falling back onto the pillows and closing my eyes."
    "And one by one, I feel the girls doing the same thing, nestling up against me."
    "It's a cramped affair, all four of us on the one bed."
    "But I'm not going to complain about the lack of space."
    "The most I can do is take one last look at Audrey, Alexis and Reona."
    "And then close my eyes for the final time, sure that they look satisfied."
    "With that knowledge, I can fall asleep without any serious worries."
    $ alexis.sexperience += 1
    $ audrey.sexperience += 1
    $ reona.sexperience += 1
    return

label thot_harem_pool_fuck_intro(appointment=None):
    scene bg pool
    show alexis swimsuit happy at center, zoomAt(1.5, (840, 1040))
    show reona swimsuit happy at center, zoomAt(1.5, (440, 1040))
    with fade
    "The three of us are enjoying our time by the pool."
    "It's a really sunny day. And really hot too."
    "At least, this time, the girls gave a nearly perfect excuse before reaching for my trunks."
    call thot_harem_pool_fuck from _call_thot_harem_pool_fuck_1
    return

label thot_harem_pool_fuck:
    "I don't offer a hint of resistance as they start to pull down my trunks."
    "Instead I decide to get on the same page and speed things up."
    "So I begin pulling down the straps of their swimsuits too."
    "Of course this means that we're all naked in a mere matter of seconds."
    "And then the real fun begins, as my cock bobs up from between my thighs."
    "I was already good and hard from seeing the girls in their swimsuits."
    "But now that they've stripped me off and gotten naked themselves..."
    "Well, I'm as stiff as a board and raring to go!"
    "And the girls certainly seem to appreciate that fact."
    "Alexis and Reona coo and gasp at the sight of it standing to attention."
    "In fact they don't seem to be able to tear their eyes away from it!"
    "I sit back, happily letting them reach out and touch it."
    "Enjoying the sensation of them beginning to stroke and caress my manhood."
    scene bg black
    show thot 3some handjob pool
    with fade
    "Pretty soon they both have one hand on it, and they're working away nicely."
    "And I find myself looking up at them as they do so."
    show thot 3some handjob pool reonadown alexisdown
    "Alexis and Reona are no more than a few inches apart by now."
    show thot 3some handjob pool reonaup alexisup
    "Their heads almost touch, cheeks brushing as they move."
    "Then it happens, one of them move a little..."
    show thot 3some handjob pool reonadown alexisdown
    "And their lips meet!"
    "Without a word passing between them, they lock lips and begin to kiss!"
    "Now I feel like I'm looking up at a real show unfolding before me."
    "Alexis and Reona kiss with a genuine passion, eyes firmly closed."
    show thot 3some handjob pool reonaup alexisup
    "But there's no way I could close mine, not with what I'm seeing."
    "That combined with the sensation of them rubbing my cock is crazily intense."
    "So much so that I don't feel like I can hold on for much longer."
    show thot 3some handjob pool reonadown alexisdown
    "If I don't make a move soon, I'm going to shoot my load."
    "And I feel that it's way too early in the proceedings for that to happen."
    show thot 3some handjob pool reonaup alexisup
    "But here's the dilemma - where am I going to put it?"
    menu:
        "Fuck Alexis":
            "I hastily reach out and take hold of Alexis with both hands."
            "It's enough to make the girls break off their kiss."
            "And they also both let go of my cock at the same time."
            "Which helps me out, as I can steer it in the right direction."
            "I'm relieved that Alexis doesn't resist my efforts to hold onto her."
            "Instead she allows me to lay her down to my side and spread her legs."
            "She even lifts her right leg as she's spread apart, making my task easier still."
            scene bg black
            show thot 3some fuckalexis pool
            with fade
            "Reona doesn't protest at my choosing Alexis either."
            "Instead she scoots closer to the other girl, supporting her from behind."
            "But there's no time for me to pay attention to what Reona's doing."
            "As I need to make an important decision right now!"
            menu:
                "Fuck her pussy":
                    "By now I have Alexis's right leg slung over my left shoulder."
                    "So it's an easy task to point the head of my cock right at her pussy."
                    "And it only takes me leaning forwards just a little way to get things moving."
                    show thot 3some fuckalexis alexisclosed
                    alexis.say "Mmm..."
                    alexis.say "Oh man..."
                    alexis.say "That feels so good!"
                    "I can tell that Alexis isn't faking it thanks to the way it feel to me right now."
                    "Her pussy is already slippery and wet, making the head of my cock slide around."
                    "But that's not going to be enough to keep me from getting where I want to go."
                    "So I take a firmer hold of Alexis, and I begin to push harder than before."
                    show thot 3some fuckalexis vaginal
                    "Almost immediately I can feel a change start to come over her down there."
                    "Every pass that I make, the resistance seems to weaken just a little."
                    "And every time it does, I'm spurred on to try again and harder."
                    show thot 3some fuckalexis alexisopened
                    "All the while the changes in Alexis's body are reflected in her reactions."
                    "She seems to be lying back, almost helpless in Reona's arms."
                    "But the moment the last of the resistance vanishes, she really is helpless."
                    "As I feel myself sinking into Alexis, she collapses onto Reona."
                    "And to her credit, the other girl keeps right on holding her up."
                    "Even as I begin to give in to the moment, Reona never falters."
                    "Which is a damn good thing, because I'm now hammering away at Alexis."
                    "Every thrust I make goes as deep as I can possibly reach."
                    "And I feel like I'm filling her each time too."
                    "All the strength of my body is going into the effort."
                    "The force that I'm using makes Alexis's breast jiggle and her thighs shake."
                    "I don't let the fact that we're out the back of the house stop me for a moment."
                    "Alexis could be howling at the moon like a crazed wolf right now."
                    show thot 3some fuckalexis alexisclosed
                    "And it wouldn't keep me from ploughing into her with all my strength."
                    "All of my attention is focussed on the task at hand."
                    "I feel sure that nothing could distract me from what I'm doing."
                    "That is until I hear the familiar sound of Reona moaning with pleasure."
                    "Looking up, I see that Alexis is now holding onto the other girl."
                    "But more than that, her hands are all over Reona's body."
                    "And her lips are caressing one of the nipples hanging over her head!"
                    "If I thought that I was as turned-on and aroused as I could get, I was dead wrong."
                    "Watching them become entwined while I'm inside of Alexis simply blows my mind."
                    "And it comes as no surprise to me that I soon feel something else about to blow too!"
                    menu:
                        "Pull out":
                            "I almost don't have time for what I want to do."
                            "But at the very last moment, I pull out of Alexis."
                            show thot 3some fuckalexis -vaginal alexisahegao
                            "Alexis's head snaps back, releasing Reona's nipple and she gasps."
                            with hpunch
                            "I can feel the effect that it's having on her, the beginnings of her own orgasm."
                            show thot 3some fuckalexis cumshot with hpunch
                            "The next second I'm shooting my load over Alexis's belly."
                            with hpunch
                            "All of this while Reona and I hold her gently in place."
                            $ alexis.sub += 1
                        "Cum inside":
                            "All I can do is hold on for dear life, my fingers sinking into Alexis's thighs."
                            with hpunch
                            "Then with one last thrust, I lost it, shooting my entire load deep into her."
                            show thot 3some fuckalexis creampie with hpunch
                            "Alexis's head snaps back, releasing Reona's nipple and she gasps."
                            show thot 3some fuckalexis alexisahegao with hpunch
                            "I can feel the effect that it's having on her, the beginnings of her own orgasm."
                            "All of this while Reona and I hold her gently in place."
                            $ alexis.love += 2
                        "Cum on their faces":
                            call thot_harem_pool_double_oral_finish from _call_thot_harem_pool_double_oral_finish
                "Fuck her ass":
                    "By now I have Alexis's right leg slung over my left shoulder."
                    "So it's an easy task to point the head of my cock right at her rear hole."
                    "And it only takes me leaning forwards just a little way to get things moving."
                    show thot 3some fuckalexis alexisclosed
                    alexis.say "Mmm..."
                    alexis.say "Oh man..."
                    alexis.say "That feels so good!"
                    "I can tell that Alexis isn't faking it thanks to the way it feel to me right now."
                    "Her ass is already slippery and wet, making the head of my cock slide around."
                    "But that's not going to be enough to keep me from getting where I want to go."
                    "So I take a firmer hold of Alexis, and I begin to push harder than before."
                    show thot 3some fuckalexis anal
                    "Almost immediately I can feel a change start to come over her down there."
                    "Every pass that I make, the resistance seems to weaken just a little."
                    "And every time it does, I'm spurred on to try again and harder."
                    show thot 3some fuckalexis alexisopened
                    "All the while the changes in Alexis's body are reflected in her reactions."
                    "She seems to be lying back, almost helpless in Reona's arms."
                    "But the moment the last of the resistance vanishes, she really is helpless."
                    "As I feel myself sinking into Alexis, she collapses onto Reona."
                    "And to her credit, the other girl keeps right on holding her up."
                    "Even as I begin to give in to the moment, Reona never falters."
                    "Which is a damn good thing, because I'm now hammering away at Alexis."
                    "Every thrust I make goes as deep as I can possibly reach."
                    "And I feel like I'm filling her each time too."
                    "All the strength of my body is going into the effort."
                    "The force that I'm using makes Alexis's breast jiggle and her thighs shake."
                    "I don't let the fact that we're out the back of the house stop me for a moment."
                    "Alexis could be howling at the moon like a crazed wolf right now."
                    show thot 3some fuckalexis alexisclosed
                    "And it wouldn't keep me from ploughing into her with all my strength."
                    "All of my attention is focussed on the task at hand."
                    "I feel sure that nothing could distract me from what I'm doing."
                    "That is until I hear the familiar sound of Reona moaning with pleasure."
                    "Looking up, I see that Alexis is now holding onto the other girl."
                    "But more than that, her hands are all over Reona's body."
                    "And her lips are caressing one of the nipples hanging over her head!"
                    "If I thought that I was as turned-on and aroused as I could get, I was dead wrong."
                    "Watching them become entwined while I'm inside of Alexis simply blows my mind."
                    "And it comes as no surprise to me that I soon feel something else about to blow too!"
                    menu:
                        "Pull out":
                            "I almost don't have time for what I want to do."
                            "But at the very last moment, I pull out of Alexis."
                            show thot 3some fuckalexis -anal alexisahegao
                            "Alexis's head snaps back, releasing Reona's nipple and she gasps."
                            with hpunch
                            "I can feel the effect that it's having on her, the beginnings of her own orgasm."
                            show thot 3some fuckalexis cumshot with hpunch
                            "The next second I'm shooting my load over Alexis's belly."
                            with hpunch
                            "All of this while Reona and I hold her gently in place."
                            $ alexis.sub += 1
                        "Cum inside":
                            "All I can do is hold on for dear life, my fingers sinking into Alexis's thighs."
                            with hpunch
                            "Then with one last thrust, I lost it, shooting my entire load deep into her."
                            show thot 3some fuckalexis creampie with hpunch
                            "Alexis's head snaps back, releasing Reona's nipple and she gasps."
                            show thot 3some fuckalexis alexisahegao with hpunch
                            "I can feel the effect that it's having on her, the beginnings of her own orgasm."
                            "All of this while Reona and I hold her gently in place."
                            $ alexis.love += 2
                        "Cum on their faces":
                            call thot_harem_pool_double_oral_finish from _call_thot_harem_pool_double_oral_finish_1
        "Fuck Reona":
            "I make a hasty grab for Reona, just managing to get my hands on her."
            "But in doing so, I have to throw most of my weight forwards."
            "And this means that as soon as I have Reona, I start to fall backwards."
            "This makes her flail around as my weight shifts around."
            "And in falling back I almost shove Alexis straight into the pool!"
            alexis.say "Hey..."
            alexis.say "Watch out!"
            "At the same time as Alexis is trying to keep from falling in, Reona's righting herself."
            "Finally she manages to spread her legs and get herself stable."
            scene bg black
            show thot 3some fuckreona pool
            "And when she does so, Reona just so happens to be straddling my thighs."
            "Her back is turned to me, but I'm not going to pass up a chance like this."
            "So I push my groin upwards and pull Reona down at the same time."
            "All the while aiming the head of my cock at the intended target."
            menu:
                "Fuck her pussy":
                    "At times like this, I always think it's important to keep things simple."
                    "Which is why I make sure to go straight for Reona's pussy the first chance I get."
                    "Getting things lined up just right means that I hit the spot as well."
                    "The very first time that Reona comes down, I feel the lips of her pussy."
                    "And as soon as I do, I get irrefutable proof that she's feeling it too."
                    show thot 3some fuckreona reonaclosed
                    reona.say "Oh fuck..."
                    reona.say "That's it..."
                    reona.say "That's what I'm talking about!"
                    "Now that she has her balance back, Reona doesn't choose to sit back either."
                    "Because now I can feel her pressing down on me with all of her weight."
                    show thot 3some fuckreona vaginal
                    "Fighting to overcome the natural resistance her body's offering as much as I am!"
                    "The sensation takes me by surprise at first, making what I'm feeling even more intense."
                    "And it takes me a couple of seconds to be able to recover and get back into it."
                    mike.say "Shit..."
                    mike.say "Hell, Reona..."
                    mike.say "Careful you don't snap it!"
                    show thot 3some fuckreona reonaback
                    reona.say "Huh?"
                    reona.say "What?!?"
                    reona.say "Just shut up and fuck me already!"
                    "Spurred on by Reona's demands, I get right on it."
                    "I redouble my efforts, pushing harder than ever."
                    "And it doesn't take long for see results."
                    "All at once, Reona sinks down again as the lips of her pussy finally part."
                    show thot 3some fuckreona reonaopened
                    "Plus the fact she's using all of her weight to push down means that it happens fast."
                    "In a mere few seconds, every inch of my cock disappears inside of her."
                    "But once it's all the way in, Reona doesn't pause or hesitate."
                    "Instead she launches herself into bouncing up and down on it."
                    "I'm doing the best that I can to keep up with her as she does so."
                    "Trying to match my speed to hers and move in sympathy."
                    "In fact I'm concentrating so hard that I totally forget about Alexis."
                    "Well, that is until she literally sits on my face!"
                    alexis.say "Hey, [hero.name]..."
                    alexis.say "Think quickly!"
                    mike.say "Wha..."
                    mike.say "Mmm..."
                    mike.say "Mmmph..."
                    "That's all the warning I get before my head is between Alexis's thighs."
                    "And she wastes no time on making sure that her lips are touching mine too."
                    "Okay, I'm pretty sure that she has no actual intention of smothering me."
                    "But I'm not about to take the chance by refusing to do a damn good job."
                    "Which is why I get straight down to business, parting my lips and deploying my tongue."
                    "Soon enough it's exploring the folds around the edges of Alexis's pussy."
                    show thot 3some fuckreona alexisclosed
                    "I make sure to probe deeply and work my way inwards the whole time too."
                    "This means that by the time the tip of my tongue is inside, she's totally at my mercy."
                    show thot 3some fuckreona reonapleasure
                    "But all the while this has been going on, Reona's not been idle either."
                    "And I feel her push down one last time, as if to squeeze the life out of me."
                    "That's what does it in the end, what pushes me over the edge."
                    show thot 3some fuckreona reonaclosed alexispleasure
                    "I'm going to cum, and it's going to happen any second now!"
                    menu:
                        "Pull out":
                            "I decide that I want to pull out before it's too late."
                            "Don't ask me what my reasons are for wanting to do that."
                            "I just do what feels natural."
                            "But that means I have to wriggle my way out from under Alexis first."
                            show thot 3some fuckreona squirt with vpunch
                            "Which almost takes too long, and I only just manage to get it done."
                            show thot 3some fuckreona -vaginal cumshot with vpunch
                            "I gasp and pant as my cock pops out of Reona, shooting hot, sticky cum up her back."
                            $ reona.sub += 1
                        "Cum inside":
                            "I decide to just stay put and let nature take it's course."
                            "But then with someone sitting on my face, what choice do I have?"
                            show thot 3some fuckreona squirt with vpunch
                            "So I keep right on going, feeling myself lose it deep inside of Reona."
                            show thot 3some fuckreona creampie with vpunch
                            "Pinned down by the weight of both girls atop me."
                            $ reona.love += 2
                        "Cum on their faces":
                            call thot_harem_pool_double_oral_finish from _call_thot_harem_pool_double_oral_finish_2
                "Fuck her ass":
                    "At times like this, I always think it's important to embrace the unusual."
                    "Which is why I make sure to go straight for Reona's ass the first chance I get."
                    "Getting things lined up just right means that I hit the spot as well."
                    "The very first time that Reona comes down, I feel the edges of her hole."
                    "And as soon as I do, I get irrefutable proof that she's feeling it too."
                    show thot 3some fuckreona reonaclosed
                    reona.say "Oh fuck..."
                    reona.say "That's it..."
                    reona.say "That's what I'm talking about!"
                    "Now that she has her balance back, Reona doesn't choose to sit back either."
                    "Because now I can feel her pressing down on me with all of her weight."
                    show thot 3some fuckreona anal
                    "Fighting to overcome the natural resistance her body's offering as much as I am!"
                    "The sensation takes me by surprise at first, making what I'm feeling even more intense."
                    "And it takes me a couple of seconds to be able to recover and get back into it."
                    mike.say "Shit..."
                    mike.say "Hell, Reona..."
                    mike.say "Careful you don't snap it!"
                    show thot 3some fuckreona reonaback
                    reona.say "Huh?"
                    reona.say "What?!?"
                    reona.say "Just shut up and fuck me already!"
                    "Spurred on by Reona's demands, I get right on it."
                    "I redouble my efforts, pushing harder than ever."
                    "And it doesn't take long for see results."
                    "All at once, Reona sinks down again as the muscles of her ass finally begin to relax."
                    show thot 3some fuckreona reonaopened
                    "Plus the fact she's using all of her weight to push down means that it happens fast."
                    "In a mere few seconds, every inch of my cock disappears inside of her."
                    "But once it's all the way in, Reona doesn't pause or hesitate."
                    "Instead she launches herself into bouncing up and down on it."
                    "I'm doing the best that I can to keep up with her as she does so."
                    "Trying to match my speed to hers and move in sympathy."
                    "In fact I'm concentrating so hard that I totally forget about Alexis."
                    "Well, that is until she literally sits on my face!"
                    alexis.say "Hey, [hero.name]..."
                    alexis.say "Think quickly!"
                    mike.say "Wha..."
                    mike.say "Mmm..."
                    mike.say "Mmmph..."
                    "That's all the warning I get before my head is between Alexis's thighs."
                    "And she wastes no time on making sure that her lips are touching mine too."
                    "Okay, I'm pretty sure that she has no actual intention of smothering me."
                    "But I'm not about to take the chance by refusing to do a damn good job."
                    "Which is why I get straight down to business, parting my lips and deploying my tongue."
                    "Soon enough it's exploring the folds around the edges of Alexis's pussy."
                    show thot 3some fuckreona alexisclosed
                    "I make sure to probe deeply and work my way inwards the whole time too."
                    "This means that by the time the tip of my tongue is inside, she's totally at my mercy."
                    show thot 3some fuckreona reonapleasure
                    "But all the while this has been going on, Reona's not been idle either."
                    "And I feel her push down one last time, as if to squeeze the life out of me."
                    "That's what does it in the end, what pushes me over the edge."
                    show thot 3some fuckreona reonaclosed alexispleasure
                    "I'm going to cum, and it's going to happen any second now!"
                    menu:
                        "Pull out":
                            "I decide that I want to pull out before it's too late."
                            "Don't ask me what my reasons are for wanting to do that."
                            "I just do what feels natural."
                            "But that means I have to wriggle my way out from under Alexis first."
                            show thot 3some fuckreona squirt with vpunch
                            "Which almost takes too long, and I only just manage to get it done."
                            show thot 3some fuckreona -anal cumshot with vpunch
                            "I gasp and pant as my cock pops out of Reona, shooting hot, sticky cum up her back."
                            $ reona.sub += 1
                        "Cum inside":
                            "I decide to just stay put and let nature take it's course."
                            "But then with someone sitting on my face, what choice do I have?"
                            show thot 3some fuckreona squirt with vpunch
                            "So I keep right on going, feeling myself lose it deep inside of Reona."
                            show thot 3some fuckreona creampie with vpunch
                            "Pinned down by the weight of both girls atop me."
                            $ reona.love += 2
                        "Cum on their faces":
                            call thot_harem_pool_double_oral_finish from _call_thot_harem_pool_double_oral_finish_3
    $ alexis.sexperience += 1
    $ reona.sexperience += 1
    if renpy.has_label("thot_harem_achievement_2") and not game.flags.cheat:
        call thot_harem_achievement_2 from _call_thot_harem_achievement_2
    return


label thot_harem_pool_double_oral_finish:
    "I feel like I'm about to blow any moment."
    "But then I feel Alexis and Reona starting to move."
    "And they're moving with a purpose too."
    "At first they crawl out of my reach."
    scene bg black
    show thot 3some blowjob pool
    with fade
    "Then they come closer again, one on each side."
    "Leaning in, they begin to open their mouths."
    show thot 3some blowjob pool rlickdick
    "And their tongues dart out, touching the tip of my cock."
    show thot 3some blowjob pool alickdick
    "That's the only part of this whole thing where it goes slowly."
    "Time seems to crawl for a moment as I wait with baited breath."
    show thot 3some blowjob pool rblowjob alickdick
    "Then they move, and everything speeds up again."
    show thot 3some blowjob pool rlickdick alickdick
    pause 0.25
    show thot 3some blowjob pool ablowjob rlickdick closed
    "I hear myself gasping as they get to work on me."
    show thot 3some blowjob pool rlickdick alickdick
    pause 0.25
    show thot 3some blowjob pool rblowjob alickdick
    "Lips, tongues and even teeth all at once."
    show thot 3some blowjob pool rlickdick alickdick
    pause 0.25
    show thot 3some blowjob pool ablowjob rlickdick
    "I can hardly see what they're doing, as their heads are in the way."
    show thot 3some blowjob pool rlickdick alickdick
    pause 0.25
    show thot 3some blowjob pool rblowjob alickdick
    "But as they bob up and down, I can certainly feel the effect it's having on me."
    show thot 3some blowjob pool rlickdick alickdick normal
    pause 0.25
    show thot 3some blowjob pool ablowjob rlickdick
    "I was sure that I'd cum at any moment before they began."
    show thot 3some blowjob pool rlickdick alickdick
    pause 0.25
    show thot 3some blowjob pool rblowjob alickdick
    "Yet somehow this new surge of pleasure doesn't make that happen."
    show thot 3some blowjob pool rlickdick alickdick closed
    pause 0.25
    show thot 3some blowjob pool ablowjob rlickdick
    "It's as if a new kind of sensation has baffled my body."
    show thot 3some blowjob pool rlickdick alickdick
    pause 0.25
    show thot 3some blowjob pool rblowjob alickdick
    "And it has to make sense of what I'm feeling before it can react."
    show thot 3some blowjob pool rlickdick alickdick
    pause 0.25
    show thot 3some blowjob pool ablowjob rlickdick normal
    "I don't know how long that process actually takes."
    show thot 3some blowjob pool rlickdick alickdick
    pause 0.25
    show thot 3some blowjob pool rblowjob alickdick
    "To me it feels like an eternity that Alexis and Reona are going down on me."
    show thot 3some blowjob pool rlickdick alickdick
    pause 0.25
    show thot 3some blowjob pool ablowjob rlickdick
    "But in reality it can't be more than a few minutes of total bliss."
    show thot 3some blowjob pool rlickdick alickdick
    pause 0.25
    show thot 3some blowjob pool rblowjob alickdick surprised
    "Because all too soon I feel the urge to let go returning."
    show thot 3some blowjob pool rlickdick alickdick
    pause 0.25
    show thot 3some blowjob pool ablowjob rlickdick
    "And this time there's no way that I'm going to be able to resist."
    show thot 3some blowjob pool alickdick rlickdick
    "Alexis and Reona seem to feel it too, as they stop what they're doing."
    "Both of them sit back on their haunches, like they're waiting to be rewarded."
    show thot 3some blowjob pool alickdick rlickdick cumshot with vpunch
    "And a few seconds later it happens, I shoot my load."
    show thot 3some blowjob pool alickdick rlickdick cum onface with vpunch
    "It spatters straight over their faces, painting them in sticky stripes."
    show thot 3some blowjob pool alickdick rlickdick cum onface -cumshot dickcum with vpunch
    "But from the looks of delight on their faces, that's exactly what they wanted."
    return

label thot_harem_foursome_intro(appointment=None):
    "Once in my bedroom, all of us eagerly stripping off our clothes."
    "I'm struggling with my sock."
    "When undressing in a hurry, there's always a piece of clothes stuck. Always... "
    call thot_harem_foursome_fuck from _call_thot_harem_foursome_fuck_1
    return

label thot_harem_foursome_fuck:
    scene bg black
    show thot 4some foreplay audrey
    with fade
    "So when one of them shoots out and grabs hold of my cock, it comes as a complete surprise!"
    mike.say "Urgh..."
    mike.say "H...hey, Audrey..."
    mike.say "Be careful with that thing, yeah?"
    mike.say "It's the only one I've got!"
    show thot 4some foreplay audrey audreyhand_up
    pause 0.25
    show thot 4some foreplay audrey audreyhand_down
    audrey.say "That's a shame, [hero.name]..."
    show thot 4some foreplay audrey audreyhand_up
    pause 0.25
    show thot 4some foreplay audrey audreyhand_down
    audrey.say "Because I'm going to give it a run for it's money tonight."
    show thot 4some foreplay audrey audreyhand_up
    pause 0.25
    show thot 4some foreplay audrey audreyhand_down
    audrey.say "Really push it to the limit!"
    show thot 4some foreplay audrey audreyhand_up
    pause 0.15
    show thot 4some foreplay audrey audreyhand_down with vpunch
    "Audrey gives my cock a hard squeeze to underline her point."
    "And I suddenly feel like my eyes are bulging out of their sockets."
    mike.say "Hhnngh!"
    show thot 4some foreplay audrey alexis
    alexis.say "Don't worry, [hero.name]..."
    alexis.say "We won't let her break you."
    show thot 4some foreplay audrey alexis reona
    reona.say "Well, at least not completely."
    reona.say "It'd be nice if there was something left of you for the next time!"
    show thot 4some foreplay audrey alexis reona alexishand reonahand audreyhand_up
    "By now all three of them have their hands on my cock."
    "And I kind of feel like I'm being eyed up by hungry she-wolves!"
    "Then it dawns on me that I'm going to have to assert myself a little here."
    "At least take back enough control to decide where this thing is going."
    "Because if I don't, then these girls are going to eat me alive."
    menu:
        "Fuck Alexis":
            "I figure that the best choice would be to opt for Alexis or Reona."
            "Mainly seeing as how neither of them seems to want to break my cock in half!"
            "With that in mind, I make my move."
            "Luckily for me, all three of them have been lulled into letting their guards down."
            show thot 4some fuckalexis with fade
            "And so there's nothing to stop me shaking them off and making a grab for Alexis."
            "I could as easily have gone for Reona, because she equally close by."
            "But there's just something that makes me choose Alexis at the last moment."
            "Maybe it's the fact that I've known her the longest out of the three."
            "Or maybe it's just because she's the first one that I set eyes on."
            "Whatever the reason, my choice doesn't seem to bother her in the slightest."
            "Because Alexis eagerly allows me to put my hands on her."
            "And then she obediently goes wherever I direct her."
            "Which in this case is up and onto the bed, straddling my waist."
            "Once I have Alexis sitting atop me cowgirl style, I'm ready to go."
            menu:
                "Fuck her pussy":
                    alexis.say "Don't be jealous, girls..."
                    alexis.say "I'm sure you'll both get your turns, eventually!"
                    "Alexis chuckles as she rubs the fact I chose her in their faces."
                    "From where I'm laid right now, I can't see Audrey and Reona's faces."
                    "But a moment later I hear them laughing instead."
                    "And that's because I pull Alexis down hard, right onto my cock."
                    "It's as hard as it can possibly be by now, all ready to go."
                    "Though I can tell from the way Alexis feels down there she still has a way to go."
                    "The lips of her pussy are working hard to keep me out of there."
                    "Moving up and down beneath her, I begin to work away at her resistance."
                    "Feeling her begin to loosen just a little with each pass I make."
                    "From the way things feel, I'm going to have to work hard for this."
                    "But that's something I'm more than willing to do."
                    audrey.say "What's wrong, Alexis?"
                    audrey.say "You need some help to loosen up?"
                    show thot 4some fuckalexis audrey with fade
                    "I watch as Audrey leans into view, reaching for Alexis."
                    "As the other girl is pretty much helpless right now, there's nothing to stop her."
                    "Soon Audrey's hands are all over Alexis, stroking and caressing her body."
                    audrey.say "Don't just sit there, Reona..."
                    audrey.say "Give me a hand - or two!"
                    "That's all it takes for Reona to lean in from the other side too."
                    "And now both of them are exploring Alexis's naked form!"
                    "The sight is more than enough to get me working harder."
                    "And their efforts seem to be having a similar effect on Alexis too."
                    "Because all of a sudden I feel something change down below."
                    "Slowly at first, but then with ever greater speed, she starts to open up."
                    "The lips of her pussy finally parting to let me in."
                    show thot 4some fuckalexis vaginal closed at startle(0.05,-10)
                    "At the same time, Alexis sinks down and onto me."
                    "Inch by inch, she swallows the length of my cock into her."
                    show thot 4some fuckalexis open
                    "And by the time I can't go any deeper, there's no more holding back."
                    "Gripping Alexis tighter than ever, I launch into the act."
                    "Where before everything had been waiting, now it's all about movement."
                    show thot 4some fuckalexis closed at startle(0.05,-10)
                    "I'm thrusting myself in and out of her like an unstoppable piston."
                    show thot 4some fuckalexis at startle(0.05,-10)
                    "And the motion soon renders her all but helpless."
                    "Rather than playing with her, Audrey and Reona are now holding her up."
                    show thot 4some fuckalexis at startle(0.05,-10)
                    "Because I genuinely think Alexis would collapse without their support!"
                    "There's no way she could make flippant comments now, even if she tried."
                    show thot 4some fuckalexis open at startle(0.05,-10)
                    "Her head is swaying this way and that like she's delirious."
                    "And I swear that her eyes are rolling back into her head!"
                    show thot 4some fuckalexis at startle(0.05,-10)
                    "I'm also glad that the others are hanging onto Alexis for another reason."
                    show thot 4some fuckalexis at startle(0.05,-10)
                    "And that reason is the fact that I know I can't keep this pace up much longer."
                    show thot 4some fuckalexis closed at startle(0.05,-10)
                    "I'm about to lose it, and I can only wait and see what effect that has on her!"
                    menu:
                        "Cum inside":
                            "With Alexis held in place, I decide to go right ahead and do it."
                            show thot 4some fuckalexis at startle(0.05,-10)
                            "So with no thought of pulling out, I just let myself go."
                            show thot 4some fuckalexis cum with vpunch
                            "Buried deep inside of her, I shoot my load."
                            with vpunch
                            "And what happens next is explosive in nature."
                            with vpunch
                            "Alexis bucks and twists in Audrey and Reona's grasp."
                            "I can feel that I've pushed her over the edge, made her cum too."
                            "And it's all they can do to hold onto her body as it moves."
                            "Whereas I simply fall back onto the mattress, utterly spent."
                        "Pull out":
                            "Knowing that Alexis is secure, I make the decision to pull out."
                            "Just before I feel myself starting to cum, I slide backwards."
                            show thot 4some fuckalexis out at startle(0.05,-10)
                            "And as my cock pulls out of her, Alexis bucks and twists in Audrey and Reona's grasp."
                            "I can feel that I've pushed her over the edge, made her cum too."
                            "And it's all they can do to hold onto her body as it moves."
                            show thot 4some fuckalexis cum with vpunch
                            "At the same time my cock bobs up, and I shoot my load."
                            show thot 4some fuckalexis cum bodycum with vpunch
                            "It spatters over Alexis's belly, then runs down over her thighs."
                            show thot 4some fuckalexis -cum bodycum with vpunch
                            "Then I fall back onto the mattress, utterly spent."
                        "Endure a bit more":
                            call thot_harem_foursome_cumshare from _call_thot_harem_event_06_cumshare
                "Fuck her ass":
                    alexis.say "Don't be jealous, girls..."
                    alexis.say "I'm sure you'll both get your turns, eventually!"
                    "Alexis chuckles as she rubs the fact I chose her in their faces."
                    "From where I'm laid right now, I can't see Audrey and Reona's faces."
                    "But a moment later I hear them laughing instead."
                    "And that's because I pull Alexis down hard, right onto my cock."
                    "It's as hard as it can possibly be by now, all ready to go."
                    "Though I can tell from the way Alexis feels down there she still has a way to go."
                    "The muscles of her ass working hard to keep me out of there."
                    "Moving up and down beneath her, I begin to work away at her resistance."
                    "Feeling her begin to loosen just a little with each pass I make."
                    "From the way things feel, I'm going to have to work hard for this."
                    "But that's something I'm more than willing to do."
                    audrey.say "What's wrong, Alexis?"
                    audrey.say "You need some help to loosen up?"
                    show thot 4some fuckalexis audrey with fade
                    "I watch as Audrey leans into view, reaching for Alexis."
                    "As the other girl is pretty much helpless right now, there's nothing to stop her."
                    "Soon Audrey's hands are all over Alexis, stroking and caressing her body."
                    audrey.say "Don't just sit there, Reona..."
                    audrey.say "Give me a hand - or two!"
                    "That's all it takes for Reona to lean in from the other side too."
                    "And now both of them are exploring Alexis's naked form!"
                    "The sight is more than enough to get me working harder."
                    "And their efforts seem to be having a similar effect on Alexis too."
                    "Because all of a sudden I feel something change down below."
                    "Slowly at first, but then with ever greater speed, she starts to open up."
                    show thot 4some fuckalexis anal closed at startle(0.05,-10)
                    "At the same time, Alexis sinks down and onto me."
                    "Inch by inch, she swallows the length of my cock into her."
                    show thot 4some fuckalexis open
                    "And by the time I can't go any deeper, there's no more holding back."
                    "Gripping Alexis tighter than ever, I launch into the act."
                    "Where before everything had been waiting, now it's all about movement."
                    show thot 4some fuckalexis closed at startle(0.05,-10)
                    "I'm thrusting myself in and out of her like an unstoppable piston."
                    show thot 4some fuckalexis at startle(0.05,-10)
                    "And the motion soon renders her all but helpless."
                    "Rather than playing with her, Audrey and Reona are now holding her up."
                    show thot 4some fuckalexis at startle(0.05,-10)
                    "Because I genuinely think Alexis would collapse without their support!"
                    "There's no way she could make flippant comments now, even if she tried."
                    show thot 4some fuckalexis open at startle(0.05,-10)
                    "Her head is swaying this way and that like she's delirious."
                    "And I swear that her eyes are rolling back into her head!"
                    show thot 4some fuckalexis at startle(0.05,-10)
                    "I'm also glad that the others are hanging onto Alexis for another reason."
                    show thot 4some fuckalexis at startle(0.05,-10)
                    "And that reason is the fact that I know I can't keep this pace up much longer."
                    show thot 4some fuckalexis closed at startle(0.05,-10)
                    "I'm about to lose it, and I can only wait and see what effect that has on her!"
                    menu:
                        "Cum inside":
                            "With Alexis held in place, I decide to go right ahead and do it."
                            show thot 4some fuckalexis at startle(0.05,-10)
                            "So with no thought of pulling out, I just let myself go."
                            show thot 4some fuckalexis cum with vpunch
                            "Buried deep inside of her, I shoot my load."
                            with vpunch
                            "And what happens next is explosive in nature."
                            with vpunch
                            "Alexis bucks and twists in Audrey and Reona's grasp."
                            "I can feel that I've pushed her over the edge, made her cum too."
                            "And it's all they can do to hold onto her body as it moves."
                            "Whereas I simply fall back onto the mattress, utterly spent."
                        "Pull out":
                            "Knowing that Alexis is secure, I make the decision to pull out."
                            "Just before I feel myself starting to cum, I slide backwards."
                            show thot 4some fuckalexis out at startle(0.05,-10)
                            "And as my cock pulls out of her, Alexis bucks and twists in Audrey and Reona's grasp."
                            "I can feel that I've pushed her over the edge, made her cum too."
                            "And it's all they can do to hold onto her body as it moves."
                            show thot 4some fuckalexis cum with vpunch
                            "At the same time my cock bobs up, and I shoot my load."
                            show thot 4some fuckalexis cum bodycum with vpunch
                            "It spatters over Alexis's belly, then runs down over her thighs."
                            show thot 4some fuckalexis -cum bodycum with vpunch
                            "Then I fall back onto the mattress, utterly spent."
                        "Endure a bit more":
                            call thot_harem_foursome_cumshare from _call_thot_harem_event_06_cumshare_1
        "Fuck Reona":
            "I figure that the best choice would be to opt for Alexis or Reona."
            "Mainly seeing as how neither of them seems to want to break my cock in half!"
            "With that in mind, I make my move."
            "Luckily for me, all three of them have been lulled into letting their guards down."
            show thot 4some fuckreona with fade
            "And so there's nothing to stop me shaking them off and making a grab for Reona."
            "I could as easily have gone for Alexis, because she equally close by."
            "But there's just something that makes me choose Reona at the last moment."
            "Maybe it's that I feel like, out of the pair, Alexis is vibing with Audrey more."
            "You know, kind of tuning into her provocative way of getting what she wants?"
            "Whereas Reona seems to be more swept along with it, instead of taking the lead."
            "Whatever the reason, Reona offers me no resistance as I take hold of her."
            "And she eagerly nods as I push her down and onto the mattress before me."
            "Far from being annoyed at my choosing Reona over them, the others seem delighted."
            show thot 4some fuckreona audrey alexis with fade
            "Audrey and Alexis follow Reona down onto the bed, flanking her on either side."
            "Hell, they even help me to part her thighs as I kneel down in front of her."
            show thot 4some fuckreona mike with fade
            mike.say "Well, well, well..."
            mike.say "What do we have here?"
            mike.say "Looks like you've been hiding away a sweet little treasure down there!"
            "Reona doesn't say a word as I look down at her."
            "But I can already see the anticipation in her eyes."
            "Like she's desperately waiting to see what I do next."
            menu:
                "Fuck her pussy":
                    "For all of the amusement that was in my voice just now, I'm still getting amazingly excited."
                    "Because the very thought of what we're about to do is more than enough to make me almost crazy."
                    "Reona's laid there, spread out before me and not offering a single iota of resistance."
                    "Which is something that I intend to take full advantage of right now."
                    "But as I aim my cock straight at Reona's pussy, Audrey suddenly leans into view."
                    "And she boldly grasps the shaft with one hand."
                    audrey.say "Mmm..."
                    show thot 4some fuckreona audrey_mouth_scream
                    audrey.say "Let me give you a hand with that!"
                    show thot 4some fuckreona audrey_mouth_normal
                    "I'm about to open my mouth and tell her that I don't need any help."
                    "But then I get a hint of just how good the sensation of her fingers feel down there."
                    "And instead I just give her a nod and a knowing grin."
                    "This seems to please Audrey no end, and she starts to guide my cock home."
                    "At the same time she's using the fingers of her free hand to play with Reona's pussy."
                    "And once they come together, she starts to rub the head up and down Roena's lips."
                    "Looking up, I see that Alexis has got in on the act too."
                    "But where Audrey's at work below the waist, she's chosen to stay well above it."
                    "This means that she has Reona's breasts all to herself."
                    "And now she's making the most of being able to caress them at her leisure."
                    "All of this means that Reona's being almost overloaded with pleasure."
                    "Before she was laid back on the bed willingly, letting all of this happen to her."
                    "But now I suspect that she couldn't move even if she were to try."
                    "The feeling of my cock rubbing against her pussy is already pretty intense."
                    "Though not so much so that I can't tear my attention away to watch what the girls are up to."
                    "Yet all of that changes a moment later, when I feel a change taking place down there."
                    "The sensation is slow and gradual, yet there's no way I can hope to resist it."
                    "Of course it's the feeling of Reona finally opening up to me."
                    show thot 4some fuckreona vaginal reona_eyes_closed reona_mouth_pleasure
                    "And once she does, I no longer need Audrey's help and guidance."
                    "In the same way that my attention is drawn to Reona, my actions change focus too."
                    "Now it seems that the only thing on my mind is beginning to push my way deeper inside."
                    "Once I'm as deep as I can go, that urge instantly changes into a need to move."
                    "I pause maybe only as much as a few seconds, and then I launch into it."
                    show thot 4some fuckreona reona_mouth_open at startle(0.05,-10)
                    "Thrusting back and forth, going faster with each passing moment, I start to pound away."
                    "And the effect on Reona is both instant and dramatic in nature."
                    "Before she was laid back, quietly helpless to resist."
                    show thot 4some fuckreona reona_eyes_closed at startle(0.05,-10)
                    "But now she begins to move in sympathy to my own motions, as though she has no choice."
                    "I feel the urge to go faster and harder, pushing myself towards the limit."
                    show thot 4some fuckreona reona_eyes_open reona_mouth_open at startle(0.05,-10)
                    "And of course this means that Reona is taken along for the ride."
                    "Her head falls back onto the mattress, eyes rolling in their sockets."
                    show thot 4some fuckreona reona_eyes_closed at startle(0.05,-10)
                    "At the same time her breasts bounce and jiggle with each thrust."
                    "Audrey and Alexis are still playing with her, but I doubt she can even feel it."
                    show thot 4some fuckreona reona_eyes_open at startle(0.05,-10)
                    "Because I know that there's only one thing on my mind right now."
                    "And I guess it must be the same for Reona too."
                    show thot 4some fuckreona reona_eyes_closed reona_mouth_pleasure at startle(0.05,-10)
                    "I know that I'm going to lose it soon."
                    "That I have to decide how I want it to end."
                    menu:
                        "Cum inside":
                            show thot 4some fuckreona at startle(0.05,-10)
                            "Trusting Audrey and Alexis to hold Reona down, I keep on going."
                            "Thrusting in and out of her until the final moment comes."
                            with vpunch
                            "Only then do I stop, once I'm as deep inside of Reona as I can go."
                            show thot 4some fuckreona reona_eyes_ahegao reona_mouth_open cum with vpunch
                            "And when I shoot my load into her, I feel her lose it too."
                            with vpunch
                            "Her muscles clamp onto me, squeezing hard, and writhes on the bed in helpless pleasure."
                        "Pull out":
                            show thot 4some fuckreona at startle(0.05,-10)
                            "Trusting Audrey and Alexis to hold Reona down, I make to pull out."
                            show thot 4some fuckreona out at startle(0.05,-10)
                            "In one smooth motion I slide out of there before the final moment comes."
                            show thot 4some fuckreona cum with vpunch
                            "Only then do I stop, once I'm free and able to shoot my load over her."
                            show thot 4some fuckreona reona_eyes_ahegao reona_mouth_open with vpunch
                            "And when I do, I see Reona begin to lose it too."
                            show thot 4some fuckreona -cum bodycum with vpunch
                            "I spatter her belly and thighs as she writhes on the bed in helpless pleasure."
                        "Endure a bit more":
                            call thot_harem_foursome_cumshare from _call_thot_harem_event_06_cumshare_2
                "Fuck her ass":
                    "For all of the amusement that was in my voice just now, I'm still getting amazingly excited."
                    "Because the very thought of what we're about to do is more than enough to make me almost crazy."
                    "Reona's laid there, spread out before me and not offering a single iota of resistance."
                    "Which is something that I intend to take full advantage of right now."
                    "But as I aim my cock straight at Reona's ass, Audrey suddenly leans into view."
                    "And she boldly grasps the shaft with one hand."
                    audrey.say "Mmm..."
                    show thot 4some fuckreona audrey_mouth_scream
                    audrey.say "Let me give you a hand with that!"
                    show thot 4some fuckreona audrey_mouth_normal
                    "I'm about to open my mouth and tell her that I don't need any help."
                    "But then I get a hint of just how good the sensation of her fingers feel down there."
                    "And instead I just give her a nod and a knowing grin."
                    "This seems to please Audrey no end, and she starts to guide my cock home."
                    "At the same time she's using the fingers of her free hand to play with Reona's ass."
                    "And once they come together, she starts to rub the head around Roena's hole."
                    "Looking up, I see that Alexis has got in on the act too."
                    "But where Audrey's at work below the waist, she's chosen to stay well above it."
                    "This means that she has Reona's breasts all to herself."
                    "And now she's making the most of being able to caress them at her leisure."
                    "All of this means that Reona's being almost overloaded with pleasure."
                    "Before she was laid back on the bed willingly, letting all of this happen to her."
                    "But now I suspect that she couldn't move even if she were to try."
                    "The feeling of my cock rubbing against her ass is already pretty intense."
                    "Though not so much so that I can't tear my attention away to watch what the girls are up to."
                    "Yet all of that changes a moment later, when I feel a change taking place down there."
                    "The sensation is slow and gradual, yet there's no way I can hope to resist it."
                    "Of course it's the feeling of Reona finally opening up to me."
                    show thot 4some fuckreona anal reona_eyes_closed reona_mouth_pleasure
                    "And once she does, I no longer need Audrey's help and guidance."
                    "In the same way that my attention is drawn to Reona, my actions change focus too."
                    "Now it seems that the only thing on my mind is beginning to push my way deeper inside."
                    "Once I'm as deep as I can go, that urge instantly changes into a need to move."
                    "I pause maybe only as much as a few seconds, and then I launch into it."
                    show thot 4some fuckreona reona_mouth_open at startle(0.05,-10)
                    "Thrusting back and forth, going faster with each passing moment, I start to pound away."
                    "And the effect on Reona is both instant and dramatic in nature."
                    "Before she was laid back, quietly helpless to resist."
                    show thot 4some fuckreona reona_eyes_closed at startle(0.05,-10)
                    "But now she begins to move in sympathy to my own motions, as though she has no choice."
                    "I feel the urge to go faster and harder, pushing myself towards the limit."
                    show thot 4some fuckreona reona_eyes_open reona_mouth_open at startle(0.05,-10)
                    "And of course this means that Reona is taken along for the ride."
                    "Her head falls back onto the mattress, eyes rolling in their sockets."
                    show thot 4some fuckreona reona_eyes_closed at startle(0.05,-10)
                    "At the same time her breasts bounce and jiggle with each thrust."
                    "Audrey and Alexis are still playing with her, but I doubt she can even feel it."
                    show thot 4some fuckreona reona_eyes_open at startle(0.05,-10)
                    "Because I know that there's only one thing on my mind right now."
                    "And I guess it must be the same for Reona too."
                    show thot 4some fuckreona reona_eyes_closed reona_mouth_pleasure at startle(0.05,-10)
                    "I know that I'm going to lose it soon."
                    "That I have to decide how I want it to end."
                    menu:
                        "Cum inside":
                            show thot 4some fuckreona at startle(0.05,-10)
                            "Trusting Audrey and Alexis to hold Reona down, I keep on going."
                            "Thrusting in and out of her until the final moment comes."
                            with vpunch
                            "Only then do I stop, once I'm as deep inside of Reona as I can go."
                            show thot 4some fuckreona reona_eyes_ahegao reona_mouth_open cum with vpunch
                            "And when I shoot my load into her, I feel her lose it too."
                            with vpunch
                            "Her muscles clamp onto me, squeezing hard, and writhes on the bed in helpless pleasure."
                        "Pull out":
                            show thot 4some fuckreona at startle(0.05,-10)
                            "Trusting Audrey and Alexis to hold Reona down, I make to pull out."
                            show thot 4some fuckreona out at startle(0.05,-10)
                            "In one smooth motion I slide out of there before the final moment comes."
                            show thot 4some fuckreona cum with vpunch
                            "Only then do I stop, once I'm free and able to shoot my load over her."
                            show thot 4some fuckreona reona_eyes_ahegao reona_mouth_open with vpunch
                            "And when I do, I see Reona begin to lose it too."
                            show thot 4some fuckreona -cum bodycum with vpunch
                            "I spatter her belly and thighs as she writhes on the bed in helpless pleasure."
                        "Endure a bit more":
                            call thot_harem_foursome_cumshare from _call_thot_harem_event_06_cumshare_3
        "Fuck Audrey":
            "I feel like Audrey's fast becoming the ring-leader of a little gang here."
            "Sure, it's probably the hottest and most desirable gang I've ever come across."
            "But I still feel like I need to make a show of my authority right about now."
            "Not in the manner of showing the girls that I'm the boss or anything like that."
            "More in the sense of making sure the balance of power between myself and the girls is equal."
            "But in order to do that, I feel like I'm going to have to be a little underhanded."
            mike.say "You know what, guys..."
            mike.say "All three of you are just so hot, so mind-blowingly beautiful and sexy..."
            mike.say "It's almost impossible for me to choose between you!"
            "Of course, this earns me a round of giggles and hard stares."
            alexis.say "Flattery will get you everywhere!"
            reona.say "Oh come on, you know you like me the best!"
            audrey.say "No getting out of it, [hero.name]..."
            audrey.say "You have to choose one of us!"
            "I pretend to think about it for a moment."
            "And then I make like I just had a revelation."
            mike.say "I bet the only part of you guys I can't tell belongs to who would be your butts!"
            mike.say "So if you line them up in front of me, I'd just have to go with the cutest one, right?"
            "I can see that this amuses the girls greatly, which was the entire point."
            "And much to my delight, they oblige me by turning their backs on me."
            "I make sure to close my eyes as they decide where put themselves."
            show thot 4some fuckaudrey reona alexis lookfront with fade
            "Then I open them to be presented with the sight of three amazing asses in a row."
            mike.say "Oh my goodness..."
            mike.say "What perfect posteriors!"
            mike.say "How will I ever be able to choose between them?"
            "I can hear the girls giggling away as I say all of this."
            "But the joke's on them, because I'd know their butts anywhere."
            "What can I say?"
            "I'm an aficionado of asses!"
            "Which means I know Audrey's right in the middle."
            "Alexis and Reona are flanking her on either side."
            "So I know exactly what my next move is going to be."
            menu:
                "Fuck her pussy":
                    "Quick as a flash, I slide my legs between Audrey's."
                    "And at the same time I grab as much of her ass as I can."
                    "Before she can even react, my groin is level with her buttocks."
                    "And I'm pulling her down and onto me in one smooth motion."
                    show thot 4some fuckaudrey lookback
                    audrey.say "Wha..."
                    audrey.say "What the..."
                    mike.say "Congratulations, Audrey..."
                    mike.say "I choose you!"
                    "I make sure to aim my cock straight at Audrey's pussy as I say this."
                    show thot 4some fuckaudrey vaginal
                    "Pulling her down as I thrust upwards so they meet somewhere in the middle."
                    "And as soon as that happens, all of Audrey's confusion seems to disappear."
                    audrey.say "Oh..."
                    audrey.say "Oh yeah..."
                    audrey.say "Please, don't...don't stop!"
                    "I'm glad to hear Audrey asking for more of the same."
                    "Because I don't think I could stop now if I tried!"
                    "I can already feel the sensation of her getting slicker and wetter down there."
                    "And every pass I make sees me come closer to the moment when she opens up to me."
                    "So I blank out everything else in order to focus on the task at hand."
                    "First there's a slight change, the smallest hint of things relaxing."
                    "Then all of a sudden momentum seems to build, and the pace quickens."
                    "After that, all it takes is a couple more passes."
                    "And then Audrey's lips part, just enough for me to get inside."
                    show thot 4some fuckaudrey vaginal righthand_hold lefthand_hold with vpunch
                    "But the change comes without warning, meaning that I push as hard as ever."
                    "That sees me plunge into her, rather than sinking in gently."
                    "And the both of us feel the sudden change as a rush of sensation."
                    mike.say "Ah..."
                    audrey.say "Oh fuck..."
                    mike.say "Oh god..."
                    "I'm about to say something similar to my last line."
                    "But that's when Audrey looks back over her shoulder at me."
                    audrey.say "Well?"
                    audrey.say "Are you going to fuck me, or what?!?"
                    "That question is all I need to hear."
                    "And a moment later I feel myself leaping into action."
                    show thot 4some fuckaudrey at startle(0.05, -10)
                    "My first thrust makes Audrey close her eyes."
                    show thot 4some fuckaudrey at startle(0.05, -10)
                    "The second sees her turn her head back around."
                    show thot 4some fuckaudrey at startle(0.05, -10)
                    "And by the time I'm into the third, she's totally swept along."
                    "From that point on my whole body seem to be on autopilot."
                    show thot 4some fuckaudrey speed lookfront
                    pause 0.15
                    show thot 4some fuckaudrey -speed at startle(0.05, -10)
                    "I just keep going faster and harder, pushing myself to the limit."
                    "And of course that means I'm pushing Audrey too."
                    show thot 4some fuckaudrey speed
                    pause 0.15
                    show thot 4some fuckaudrey -speed at startle(0.05, -10)
                    "She rides me like her life depends on it, holding on as best she can."
                    show thot 4some fuckaudrey speed
                    pause 0.15
                    show thot 4some fuckaudrey -speed at startle(0.05, -10)
                    "All the while her body bounces up and down, all the good parts swaying too!"
                    "I hardly notice myself letting go of her waist."
                    show thot 4some fuckaudrey righthand_finger lefthand_finger lookback
                    "And I unconsciously reach out towards the two asses flanking her."
                    "Up until now, Alexis and Reona have just been watching the action."
                    "Totally wrapped up in what Audrey and I are getting up to."
                    "Which means they don't notice as I begin to stroke their exposed pussys."
                    show thot 4some fuckaudrey alexis_eyes_closed
                    alexis.say "Ah!"
                    show thot 4some fuckaudrey reona_eyes_closed
                    reona.say "Ooh!"
                    "They're already pretty wet down there."
                    "Which means I don't have too much work to do."
                    "And within what feels like seconds, my fingers are slipping inside of them."
                    show thot 4some fuckaudrey speed
                    pause 0.15
                    show thot 4some fuckaudrey -speed at startle(0.05, -10)
                    "So with my cock in Audrey and fingers in Alexis and Reona, I make one final push."
                    "Using the last of the energy left in me, I do all that I can to pleasure them."
                    show thot 4some fuckaudrey speed
                    pause 0.15
                    show thot 4some fuckaudrey -speed at startle(0.05, -10)
                    "Because I can already feel the sensation of my orgasm taking over."
                    menu:
                        "Cum inside":
                            show thot 4some fuckaudrey speed
                            pause 0.15
                            show thot 4some fuckaudrey -speed at startle(0.05, -10)
                            "Keeping my cock, as well as my fingers, exactly where they are, I keep on going."
                            show thot 4some fuckaudrey speed
                            pause 0.15
                            show thot 4some fuckaudrey -speed with vpunch
                            "And I make sure that I'm as deep into all three of them as I can be when it happens."
                            "But I think the effect on Audrey is the most dramatic of all."
                            "Sure, Alexis and Reona keep on moaning and panting the whole time."
                            show thot 4some fuckaudrey speed
                            pause 0.15
                            show thot 4some fuckaudrey -speed cum ahegao with vpunch
                            "But as soon as I feel myself filling Audrey, she starts to quake and quiver too."
                            with vpunch
                            "All of which tells me that she's cumming at the same time, helpless to resist."
                        "Pull out":
                            show thot 4some fuckaudrey speed
                            pause 0.15
                            show thot 4some fuckaudrey -speed out -righthand_finger -lefthand_finger at startle(0.05, -10)
                            "I pull everything out at the exact same moment, cock and fingers alike."
                            "Trying to make sure that everything happens at once for all three of them."
                            "But I think the effect on Audrey is the most dramatic of all."
                            "Sure, Alexis and Reona keep on moaning and panting as I pull my fingers out."
                            show thot 4some fuckaudrey ahegao with vpunch
                            "But as soon as I feel myself sliding out Audrey, she starts to quake and quiver too."
                            show thot 4some fuckaudrey cum with vpunch
                            "All of which tells me that she's cumming at the same time, helpless to resist."
                            show thot 4some fuckaudrey -cum bodycum with vpunch
                            "So the sensation of shooting my load over her buttocks is that much sweeter as a result."
                        "Endure a bit more":
                            call thot_harem_foursome_cumshare from _call_thot_harem_event_06_cumshare_4
                "Fuck her ass":
                    "Quick as a flash, I slide my legs between Audrey's."
                    "And at the same time I grab as much of her ass as I can."
                    "Before she can even react, my groin is level with her buttocks."
                    "And I'm pulling her down and onto me in one smooth motion."
                    audrey.say "Wha..."
                    audrey.say "What the..."
                    mike.say "Congratulations, Audrey..."
                    mike.say "I choose you!"
                    "I make sure to aim my cock straight at Audrey's hole as I say this."
                    show thot 4some fuckaudrey anal
                    "Pulling her down as I thrust upwards so they meet somewhere in the middle."
                    "And as soon as that happens, all of Audrey's confusion seems to disappear."
                    audrey.say "Oh..."
                    audrey.say "Oh yeah..."
                    audrey.say "Please, don't...don't stop!"
                    "I'm glad to hear Audrey asking for more of the same."
                    "Because I don't think I could stop now if I tried!"
                    "I can already feel the sensation of her getting slicker and wetter down there."
                    "And every pass I make sees me come closer to the moment when she opens up to me."
                    "So I blank out everything else in order to focus on the task at hand."
                    "First there's a slight change, the smallest hint of muscles relaxing."
                    "Then all of a sudden momentum seems to build, and the pace quickens."
                    "After that, all it takes is a couple more passes."
                    "And then Audrey's hole opens, just enough for me to get inside."
                    show thot 4some fuckaudrey anal righthand_hold lefthand_hold with vpunch
                    "But the change comes without warning, meaning that I push as hard as ever."
                    "That sees me plunge into her, rather than sinking in gently."
                    "And the both of us feel the sudden change as a rush of sensation."
                    mike.say "Ah..."
                    audrey.say "Oh fuck..."
                    mike.say "Oh god..."
                    "I'm about to say something similar to my last line."
                    "But that's when Audrey looks back over her shoulder at me."
                    audrey.say "Well?"
                    audrey.say "Are you going to fuck me, or what?!?"
                    "That question is all I need to hear."
                    "And a moment later I feel myself leaping into action."
                    show thot 4some fuckaudrey at startle(0.05, -10)
                    "My first thrust makes Audrey close her eyes."
                    show thot 4some fuckaudrey at startle(0.05, -10)
                    "The second sees her turn her head back around."
                    show thot 4some fuckaudrey at startle(0.05, -10)
                    "And by the time I'm into the third, she's totally swept along."
                    "From that point on my whole body seem to be on autopilot."
                    show thot 4some fuckaudrey speed lookfront
                    pause 0.15
                    show thot 4some fuckaudrey -speed at startle(0.05, -10)
                    "I just keep going faster and harder, pushing myself to the limit."
                    "And of course that means I'm pushing Audrey too."
                    show thot 4some fuckaudrey speed lookfront
                    pause 0.15
                    show thot 4some fuckaudrey -speed at startle(0.05, -10)
                    "She rides me like her life depends on it, holding on as best she can."
                    show thot 4some fuckaudrey speed lookfront
                    pause 0.15
                    show thot 4some fuckaudrey -speed at startle(0.05, -10)
                    "All the while her body bounces up and down, all the good parts swaying too!"
                    "I hardly notice myself letting go of her waist."
                    show thot 4some fuckaudrey righthand_finger lefthand_finger lookback
                    "And I unconsciously reach out towards the two asses flanking her."
                    "Up until now, Alexis and Reona have just been watching the action."
                    "Totally wrapped up in what Audrey and I are getting up to."
                    "Which means they don't notice as I begin to stroke their exposed holes."
                    show thot 4some fuckaudrey alexis_eyes_closed
                    alexis.say "Ah!"
                    show thot 4some fuckaudrey reona_eyes_closed
                    reona.say "Ooh!"
                    "They're already pretty wet down there."
                    "Which means I don't have too much work to do."
                    "And within what feels like seconds, my fingers are slipping inside of them."
                    "Probing and exploring their asses while they're helpless to resist."
                    show thot 4some fuckaudrey speed
                    pause 0.15
                    show thot 4some fuckaudrey -speed at startle(0.05, -10)
                    "So with my cock in Audrey and fingers in Alexis and Reona, I make one final push."
                    "Using the last of the energy left in me, I do all that I can to pleasure them."
                    show thot 4some fuckaudrey speed
                    pause 0.15
                    show thot 4some fuckaudrey -speed at startle(0.05, -10)
                    "Because I can already feel the sensation of my orgasm taking over."
                    menu:
                        "Cum inside":
                            show thot 4some fuckaudrey speed
                            pause 0.15
                            show thot 4some fuckaudrey -speed at startle(0.05, -10)
                            "Keeping my cock, as well as my fingers, exactly where they are, I keep on going."
                            show thot 4some fuckaudrey speed
                            pause 0.15
                            show thot 4some fuckaudrey -speed with vpunch
                            "And I make sure that I'm as deep into all three of them as I can be when it happens."
                            "But I think the effect on Audrey is the most dramatic of all."
                            "Sure, Alexis and Reona keep on moaning and panting the whole time."
                            show thot 4some fuckaudrey speed
                            pause 0.15
                            show thot 4some fuckaudrey -speed cum ahegao with vpunch
                            "But as soon as I feel myself filling Audrey, she starts to quake and quiver too."
                            with vpunch
                            "All of which tells me that she's cumming at the same time, helpless to resist."
                        "Pull out":
                            show thot 4some fuckaudrey speed
                            pause 0.15
                            show thot 4some fuckaudrey -speed out -righthand_finger -lefthand_finger at startle(0.05, -10)
                            "I pull everything out at the exact same moment, cock and fingers alike."
                            "Trying to make sure that everything happens at once for all three of them."
                            "But I think the effect on Audrey is the most dramatic of all."
                            "Sure, Alexis and Reona keep on moaning and panting as I pull my fingers out."
                            show thot 4some fuckaudrey ahegao with vpunch
                            "But as soon as I feel myself sliding out Audrey, she starts to quake and quiver too."
                            show thot 4some fuckaudrey cum with vpunch
                            "All of which tells me that she's cumming at the same time, helpless to resist."
                            show thot 4some fuckaudrey -cum bodycum with vpunch
                            "So the sensation of shooting my load over her buttocks is that much sweeter as a result."
                        "Endure a bit more":
                            call thot_harem_foursome_cumshare from _call_thot_harem_event_06_cumshare_5
    return

label thot_harem_foursome_cumshare:
    "I feel like I'm going to lose it any moment."
    "Like there's no way I can possibly hold on."
    "But that's when I feel movement down below."
    "And opening my eyes, I see that the girls are in motion."
    "Audrey, Alexis and Reona are all moving with apparent purpose."
    "And as soon as they realise I'm watching them, they move even faster."
    show thot 4some bj with fade
    "All of a sudden, they're kneeling in front of me."
    "Then Audrey reaches out and takes hold of my cock."
    audrey.say "Uh, uh..."
    audrey.say "Not just yet!"
    "I gasp as Audrey squeezes the base of my shaft."
    "And I have no idea how she does it, but I feel the urge to cum ease off."
    "It doesn't vanish completely, but more fades and becomes less urgent."
    "Which comes as a relief when I realise what exactly the girls have in mind."
    "As one they begin to lean in and focus all their attention on my cock."
    "Lips, tongues and teeth all come into play as they give me a three-way blow-job."
    show thot 4some bj audrey_suck
    "Audrey seems to be the one taking the lead, showing the others where to go and what to do."
    "And they follow in her wake, picking up where she leaves off as she flits here and there."
    show thot 4some bj out
    pause 0.3
    show thot 4some bj alexis_suck
    "Alexis rushes to take up what Audrey moves on from."
    show thot 4some bj out
    pause 0.3
    show thot 4some bj reona_suck
    "And then when she moves on again, Reona pick up from Audrey."
    "This means that head, shaft and balls are always being attended to."
    show thot 4some bj out
    pause 0.3
    show thot 4some bj alexis_suck
    "And for the entirety of the blow-job I'm being pleasured from three sides too!"
    show thot 4some bj out
    pause 0.3
    show thot 4some bj audrey_suck
    "I don't know if Audrey's deliberately pushing me as hard as she can right now."
    "Or else what she's doing is so intense that I can't hope to hold on for long."
    show thot 4some bj out
    pause 0.3
    show thot 4some bj reona_suck
    "But either way, I know that I'm getting ready to lose it again."
    show thot 4some bj out
    "Which means that I need to decide where it's going to go!"
    menu:
        "Cum in Audrey mouth":
            show thot 4some bj audrey_suck
            "Since she took lead, it seems appropriate that Audrey gets to finish off too."
            "And with that in mind, I use the last of my energy to hold off just long enough."
            show thot 4some bj audrey_suck cum with vpunch
            "Then as soon as my cock's back in her mouth, I let go."
            with vpunch
            "Luckily, Audrey seems to sense this coming and reacts in time."
            show thot 4some bj -cum out mouthcum_audrey with vpunch
            "Managing to gulp down every last drop, she takes it in her stride."
            "Much to the amazement of myself and the other girls."
        "Cum in Alexis mouth":
            show thot 4some bj alexis_suck
            "Since she did so well following Audrey's lead, it seems appropriate that Alexis gets to finish off."
            "And with that in mind, I use the last of my energy to hold off just long enough."
            show thot 4some bj alexis_suck cum with vpunch
            "Then as soon as my cock's back in her mouth, I let go."
            with vpunch
            "Luckily, Alexis seems to sense this coming and reacts in time."
            show thot 4some bj -cum out mouthcum_alexis with vpunch
            "Managing to gulp down every last drop, she takes it in her stride."
            "Much to the amazement of myself and the other girls."
        "Cum in Reona mouth":
            show thot 4some bj reona_suck
            "Since I don't want her to feel like she's losing out, it seems appropriate that Reona gets to finish off."
            show thot 4some bj reona_suck cum with vpunch
            "And with that in mind, I use the last of my energy to hold off just long enough."
            "Then as soon as my cock's back in her mouth, I let go."
            with vpunch
            "Luckily, Reona seems to sense this coming and reacts in time."
            show thot 4some bj -cum out mouthcum_reona with vpunch
            "Managing to gulp down every last drop, she takes it in her stride."
            "Much to the amazement of myself and the other girls."
        "Facial them all":
            show thot 4some bj out mikehand
            "Deliberately pulling back from the girls, I get ready to shoot my load."
            "And luckily for me, they seem to figure out what I have in mind."
            with vpunch
            "All three of them sit back, patiently waiting for what's coming next."
            show thot 4some bj cum with vpunch
            "Which, of course, is me firing everything I have straight into their faces!"
            show thot 4some bj facecum_audrey facecum_alexis facecum_reona with vpunch
            "Every one of them gets hit by the strings of hot, sticky cum as it flies."
            "And they all have a smile on their faces as it happens too."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
