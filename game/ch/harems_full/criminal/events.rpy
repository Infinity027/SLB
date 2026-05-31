init python:
    Event(**{
    "name": "criminal_harem_event_01",
    "label": "criminal_harem_event_01",
    "priority": 500,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsFlag("CriminalRequest", 0),
            ),
        IsTimeOfDay("morning"),
        "Person.showdown(camila, lexi)",
        PersonTarget(camila,
            Not(IsPresent()),
            Not(IsHidden()),
            ),
        PersonTarget(lexi,
            Not(IsPresent()),
            Not(IsHidden()),
            ),
        ],
    "music": "music/roa_music/alley.ogg",
    "do_once": False,
    "once_month": True,
    })

    InteractEvent(**{
    "name": "criminal_harem_event_02",
    "label": "criminal_harem_event_02",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsFlag("CriminalRequest", 1),
            ),
        PersonTarget(camila,
            IsActive(),
            ),
        ],
    "music": "music/roa_music/hero.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "criminal_harem_event_03",
    "label": "criminal_harem_event_03",
    "priority": 500,
    "conditions": [
        TogetherInHarem('criminal', 'camila', 'lexi'),
        IsHour(2, 4),
        HeroTarget(
            IsGender("male"),
            IsFlag("CriminalRequest", 2),
            IsRoom("date_nightclub"),
            ),
        PersonTarget(camila,
            Not(IsPresent()),
            Not(IsHidden()),
            ),
        PersonTarget(lexi,
            OnDate(),
            ),
        ],
    "music": "music/roa_music/alley.ogg",
    "do_once": False,
    "once_month": True,
    })

label criminal_harem_event_01:
    play sound cell_vibrate loop
    "I pick up my phone as soon as I hear it ring."
    "But I make sure to check the caller ID before I accept it."
    "I see that it's Lexi's name that's popped up."
    stop sound
    $ result = renpy.call_screen("smartphone_choice", "Lexi")
    if not result:
        $ hero.cancel_event()
        return
    "And that's all the motivation I need to answer it."
    "Because when Lexi calls me, it's usually worth the effort."
    "More often than not, it's a not so subtle invitation to have some serious fun!"
    mike.say "Hey, Lexi!"
    mike.say "What's up?"
    lexi.say "Ah...hey, [hero.name]."
    lexi.say "I...kinda need your help, yeah?"
    "I'm already intrigued as to what Lexi could need from me."
    "But I do my best to keep my tone level and appear receptive."
    "Though my mind's racing the whole time as to the possibilities."
    mike.say "Sure, Lexi."
    mike.say "What can I do you for?"
    mike.say "I mean what can I do FOR you!"
    lexi.say "Just shut up and listen, [hero.name]..."
    lexi.say "I need you to come down the station."
    lexi.say "You've got money, right?"
    lexi.say "You can bail me out?"
    "Suddenly the conversation seems to have taken a dark turn."
    "All thought of flirting and innuendo disappears from my mind."
    mike.say "You mean station as in police station?!?"
    lexi.say "No, [hero.name], I mean the fire station."
    lexi.say "Of course I mean the fucking police station!"
    mike.say "You mean you got arrested?"
    mike.say "What in the hell did you do, Lexi?!?"
    "Lexi dismisses the question with a snort."
    "To her it seems that the details aren't important."
    lexi.say "What does that matter?"
    lexi.say "You know how cops are."
    lexi.say "Always cooking up some bullshit to hassle people like me!"
    mike.say "Ah..."
    mike.say "I'm not sure that's strictly true..."
    "Lexi cuts me off with another snort."
    "And then she's back to what's important to her."
    lexi.say "Blah, blah, blah...whatever, [hero.name]."
    lexi.say "You can bail me out, yeah?"
    lexi.say "It's only like a thousand dollars."
    lexi.say "You must have that in loose change!"
    menu:
        "Agree" if hero.money >= 1000:
            "Yeah, I know what most of you are thinking."
            "I should tell her where to get off and end the call."
            "But maybe that's the very reason that Lexi ends up in situations like this."
            "She doesn't have anyone to turn to when it really matters."
            "Of course, the alternative is a lot less appealing."
            "Because it means I'm just the latest in a long line of suckers."
            "Another naive guy that Lexi's able to wrap around her little finger."
            "Then again, maybe it's worth being a sucker for a girl like Lexi?"
            mike.say "Okay, Lexi, just sit tight."
            mike.say "I'm on my way over there now."
            $ lexi.love += 10
            lexi.say "I knew I could count on you, [hero.name]!"
            lexi.say "Hurry up and get your ass over here."
            lexi.say "I'm feeling better already."
            lexi.say "In fact, I'm feeling VERY generous..."
            "I try as best I can to keep my mind on the subject at hand."
            "But Lexi's words are already conjuring images in my imagination."
            mike.say "Just sit tight, Lexi."
            mike.say "I'm coming to get you."
            lexi.say "I'll be waiting!"
        "Refuse":
            "Bail her out for a thousand dollars!"
            "What the hell does she think I am?"
            "Some kind of walking ATM?!?"
            mike.say "I don't think so, Lexi."
            mike.say "You're going to have to call someone else."
            lexi.say "Huh?"
            lexi.say "What the fuck?!?"
            lexi.say "You can't just leave me here!"
            mike.say "I think you'll find that I can, Lexi."
            mike.say "You're a big girl, and you can look after yourself."
            "I hear Lexi cursing on the other end of the line."
            "But I just hold the phone away from my ear until the swearing stops."
            $ lexi.love -= 50
            lexi.say "Urgh..."
            lexi.say "I can't believe you're gonna leave me high and dry like this!"
            lexi.say "Some friend you are!"
            "And with that, she slams down the phone."
            "I feel instantly guilty for not stepping in to help."
            "But I keep telling myself that Lexi's wrong."
            "By doing this, I am being a friend to her."
            "I'm making her deal with the consequences of her actions."
            "And who knows, maybe a night in the cells is just what she needs?"
            "Better for her to cool off in there than explode in front of me too!"
            return
    scene bg black with timelaps
    scene bg policestation with timelaps
    "I arrive at the police station trying as best I can not to look furtive or suspicious."
    "All of which goes out the window the moment that I walk up to the front desk."
    lexi.say "Hey, [hero.name]!"
    lexi.say "Over here!"
    show lexi date with dissolve
    "My head snaps around to see Lexi standing by the desk."
    "By her side is a harassed-looking cop with a handful of paperwork."
    "And as I hurry over, he looks almost as relieved to see me as Lexi herself!"
    mike.say "Ah...hey, Lexi."
    mike.say "I'd have been here sooner."
    mike.say "But I needed to pick up the money for your bail."
    show lexi happy close
    lexi.say "Aww, my knight in shining armour!"
    lexi.say "I don't know what I'd do without you!"
    mike.say "Maybe spend the night in jail?"
    "I mutter these last words, so Lexi doesn't hear them."
    show lexi surprised -close
    lexi.say "Huh?"
    lexi.say "Did you say something?"
    mike.say "No..."
    mike.say "I didn't say anything at all!"
    $ hero.money -= 1000
    show lexi normal
    "I hand over the money and sign all the relevant paperwork."
    "And just like that, Lexi is out of the collective hair of the police."
    if "criminal_harem_event_01" not in DONE:
        $ game.flags.CriminalRequest = 1
        "But now I guess she's technically my responsibility instead."
        "Realising this, I waste no time in steering her towards the exit."
        "But before I can shove Lexi through the doors, I hear a familiar voice."
        show lexi annoyed at left
        show camila work wink at right
        with moveinright
        camila.say "Well, well, well..."
        camila.say "Look what the cat stepped in!"
        "For a moment, I can't figure out what Camila means."
        "But then I realise that she's talking to Lexi, and not me."
        "In fact, I don't think she's even seen me yet."
        show lexi normal
        lexi.say "Aw, hey - it's Dirty Harriet!"
        lexi.say "Still busy planting evidence and harassing folks, huh?"
        show camila angry
        "I can see that Camila's about to fire back at Lexi."
        "But then she stops, her mouth hanging open."
        "And I know that she's finally spotted me."
        show camila annoyed
        camila.say "Wha...what are you doing here, [hero.name]?"
        camila.say "Wait a minute..."
        camila.say "Do you two...know each other?!?"
        "I look from Camila to Lexi and then back again."
        "Camila looks shocked, like she has no idea what's going on."
        show lexi happy
        "But a wicked smile is already spreading across Lexi's face."
        lexi.say "Oh yeah - didn't you know?"
        show lexi wink
        lexi.say "[hero.name] and I are old friends."
        lexi.say "We're really tight too."
        lexi.say "I called him to bail me out."
        lexi.say "And he just came running!"
        show lexi normal
        mike.say "Well...running is a bit strong!"
        mike.say "Sure, we're friends - but old friends?"
        mike.say "I don't know if I'd go that far!"
        mike.say "I'm just trying to help out, that's all."
        show camila weird zorder 1 at right
        "Camila's expression is one that I'm not used to seeing on her face."
        "She looks unsure of herself."
        "But worse, she also looks like she's unsure of me too."
        camila.say "I...I had no idea."
        camila.say "No idea at all..."
        "I have no idea either - no idea of how to salvage the situation."
        "Lexi's not going to stop gloating while Camila's in front of her."
        "But this is Camila's place of work, and she's a cop."
        "She can't afford to be humiliated in front of her colleagues."
        "The only answer seems to be to get Lexi out of here."
        "And so I grab her by the hand and head for the door."
        show lexi surprised zorder 2 at center, zoomAt(1.5, (540, 1040)), hshake
        lexi.say "Wha..."
        lexi.say "Hey!"
        mike.say "Come on, Lexi - we're leaving."
        mike.say "I'm sure Camila's too busy to stand around chatting!"
        "With that, I hustle Lexi out of the doors and down the stairs."
        "The whole time, I don't hear Camila say a single word."
        "She just stands there, watching us leave in an awkward silence."
    return

label criminal_harem_event_02:
    show camila annoyed
    camila.say "Ah, [hero.name]..."
    camila.say "It's none of my business what you do with your own money."
    camila.say "But I wouldn't suggest spending it on bailing out certain people."
    show camila angry
    camila.say "And Lexi's definitely one of them!"
    show camila annoyed
    "There's an awkward moment of silence."
    "And all I can do is nod, then agree."
    mike.say "I...I know what you mean, Camila."
    mike.say "But like I said - I was just trying to help out!"
    show camila angry
    camila.say "Yeah..."
    camila.say "About that..."
    camila.say "I'm pretty good at spotting a liar, [hero.name]."
    camila.say "It kind of helps out in a job like mine."
    show camila annoyed
    "Camila doesn't come right out and call me on my bullshit."
    "But then she doesn't actually need to."
    "The only question is, do I come clean now?"
    "Or do I double down on what I told her the last time?"
    menu:
        "Lie":
            $ game.flags.CriminalRequest = "lie"
            mike.say "Well, don't shoot the messenger, Camila."
            mike.say "But I think your instincts are wrong on this one."
            "Camila raises an eyebrow at this."
            "And she looks far from convinced."
            show camila normal
            camila.say "Really, [hero.name]?"
            camila.say "Because if you're lying to me..."
            "I shake my head and roll my eyes."
            "Doing all I can to convince Camila."
            mike.say "You said you knew Lexi pretty well, didn't you?"
            mike.say "Then you have to know that she's full of shit, right?"
            camila.say "I...I guess so."
            mike.say "Camila, she was playing you."
            mike.say "She figured out we knew each other."
            mike.say "And she took the chance to wind you up, that's all."
            show camila annoyed
            "Camila looks like she's starting to question herself."
            "Which is all the encouragement I need to pile on the pressure."
            mike.say "At the most she's a friend of a friend."
            mike.say "I was bailing her out as a favour to someone."
            $ camila.love -= 50
            show camila normal
            camila.say "Okay, [hero.name], I believe you."
            camila.say "But you'd better not be feeding me a line!"
            "I smile and shake my head."
            "But I can't help worrying about what might happen if I get found out!"
        "Tell the truth":
            mike.say "I don't know how to tell you this, Camila."
            mike.say "But you're right - I have been lying to you about Lexi."
            "Camila reacts the moment that the words have been spoken."
            "But the nature of that reaction takes me by surprise."
            "She clenches her fist and shakes it triumphantly."
            show camila happy
            camila.say "YES!"
            camila.say "I KNEW it!"
            camila.say "I knew my instincts were on the money!"
            "Suddenly, Camila sees the surprise on my face."
            "And she makes a visual effort to appear more serious."
            if camila.sub >= 75 and camila.lesbian >= 9:
                $ game.flags.CriminalRequest = 2
                mike.say "I...I get it if we're over, Camila."
                mike.say "You're a cop and she's a felon."
                mike.say "So I understand..."
                show camila close annoyed
                "Camila begins to shake her head as I say this."
                "And she leans in a little closer."
                "Almost like she doesn't want to be overheard."
                show camila normal
                camila.say "No, no, no..."
                camila.say "You told me the truth, [hero.name]."
                camila.say "Now I'm gonna do the same in return!"
                "I can only blink in confusion at this."
                "As I have no idea what Camila means."
                camila.say "I kind of didn't believe you anyway."
                camila.say "And I couldn't get it out of my head."
                camila.say "I just kept thinking about you and her together!"
                mike.say "What - Lexi and me?!?"
                "Camila nods almost desperately."
                show camila blush
                "And I can see she's getting hot and bothered."
                "Flustered just thanks to talking about Lexi and I."
                camila.say "Yeah..."
                camila.say "She's just so...filthy!"
                camila.say "So bad, you know?"
                camila.say "I always kinda wanted to be like her..."
                camila.say "But I have to be the good cop."
                camila.say "I could never ask her to...to teach me."
                "Camila looks me in the eyes."
                "And I've never seen such desire her gaze."
                camila.say "But maybe you could..."
                camila.say "Maybe together, the three of us could..."
                "I nod as understanding dawns on me."
                mike.say "I know what you're asking, Camila."
                mike.say "And don't worry."
                mike.say "I'm sure I can convince Lexi."
                $ camila.love += 5
                $ camila.sub += 1
                "Camila's cheeks flush red all of a sudden."
                "And I'm sure it's as much from desire as relief."
                $ Harem.join_by_name("criminal", "camila", "lexi")
            else:
                show camila sad
                camila.say "I mean...that's not cool, [hero.name]."
                camila.say "You lied to me, abused my trust."
                camila.say "But worse than that - you did it with a known felon too!"
                show camila annoyed
                "I shrug helplessly at this."
                "There's really nothing I can say to defend myself."
                mike.say "I'm sorry, Camila."
                mike.say "I know that's not going to change anything."
                mike.say "But I am."
                "She nods at this."
                "But then she lets out a sigh of frustration."
                show camila sad
                camila.say "So am I, [hero.name]."
                camila.say "Because it means we can't keep on seeing each other."
                camila.say "I'm sorry because this means we're over."
                "I open my mouth to protest."
                "But Camila holds up a hand to silence me."
                "And then she walks away."
                "Which leaves me alone and regretting the bad choices I've made."
                $ camila.set_gone_forever()
    return

label criminal_harem_event_03:
    $ game.room = "alley"
    $ game.flags.CriminalRequest = 3
    scene bg alley
    show lexi date
    with fade
    "Lexi and I have just decided that it's time to bring our date to an end and head home."
    "Not because it's been a bust or anything like, in fact it's been a great night."
    "It's just that I have work in the morning, so I need to get my head down for a little sleep."
    "And Lexi...erm...well, I don't know exactly what Lexi's doing tomorrow."
    "But I'm guessing that she probably needs to sleep in order to have the energy too!"
    mike.say "Ah..."
    mike.say "Maybe we should call a taxi?"
    mike.say "This way leads to a pretty sketchy neighbourhood!"
    show lexi annoyed
    "Lexi looks at me like I have steaming turds hanging out of my mouth."
    show lexi happy at startle
    "Then she bursts out into spluttering laughter."
    lexi.say "Ppfft..."
    show lexi normal
    lexi.say "I'm sorry, but what did you just say?"
    lexi.say "You think that's a sketchy neighbourhood?"
    show lexi wink
    lexi.say "Please - I used to pull shit around there when I was just a little kid!"
    show lexi at center, zoomAt(1.5, (640, 1040))
    "As if to make her point, Lexi grabs hold of my hand."
    "And then she drags me after her as she walks towards the bad neighbourhood."
    show lexi happy
    lexi.say "If anyone messes with us, they'll be sorry!"
    "I can feel a nervous smile spreading across my face."
    "And on the inside, I'm trying to buy into what Lexi's saying."
    "I mean, she IS a pretty tough girl."
    "So it'll be okay to walk straight through there, right?"
    "Oh god - how did it come to this?"
    "I'm relying on my date to keep me safe from muggers and creeps!"
    "We're probably about halfway through the bad area."
    "And I'm actually starting to think this might work out."
    "But that's when I hear a stern, forceful voice behind us."
    show lexi surprised at startle
    show fx exclamation
    "???" "Stop right there!"
    "???" "Well, well, well...what do we have here?"
    "???" "Another dirty little whore and her latest customer, I'll bet!"
    hide fx
    show lexi annoyed
    "Lexi rolls her eyes, clearly used to being spoken to like that."
    "But there's something familiar about the voice."
    "I can't help turning around to get a look at who it belongs to."
    hide lexi
    show lexi date annoyed at left
    show camila work at right
    with fade
    "And there's Camila, in full uniform and with a pistol on her hip!"
    mike.say "CAMILA?!?"
    show camila surprised
    camila.say "[hero.name!u]?!?"
    show lexi normal
    lexi.say "Oh..."
    lexi.say "Hey, Camila!"
    lexi.say "Small world, huh?"
    lexi.say "Been a long time since I was busted by you!"
    "I look at Lexi in amazement."
    "Then I turn to Camila, still confused."
    mike.say "Busted?"
    mike.say "What do you mean 'busted'?!?"
    mike.say "We weren't doing anything - just walking down the street!"
    show lexi wink
    "Lexi leans in and winks at me in a conspiratorial manner."
    lexi.say "Good thinking, [hero.name]."
    lexi.say "That's what I always used to tell the cops!"
    mike.say "What the hell does that mean, Lexi?"
    mike.say "We were just walking home from our date!"
    "When she first pounced on us, Camila looks as surprised as me."
    show camila flirt
    "But when Lexi started talking, she suddenly became amused."
    "Yet at the mere mention of a date, she seems to change mood again."
    "Now she looks annoyed, almost like she's jealous."
    camila.say "You know what, Lexi..."
    camila.say "I really should bust your ass for bringing poor [hero.name] through here!"
    show lexi angry
    "Lexi can't help bristling at the criticism."
    lexi.say "What's that supposed to mean, huh?"
    lexi.say "He's safer here with me than he'd ever be with you!"
    show camila angry
    "Camila scoffs and shakes her head."
    camila.say "You're just a cheap little tart, Lexi."
    camila.say "I know these streets better than you ever will!"
    lexi.say "Oh yeah?!?"
    camila.say "YEAH?!?"
    mike.say "Erm..."
    mike.say "Guys?"
    show lexi at zoomAt(1.8, (350, 1275))
    show camila at zoomAt(1.8, (1000, 1275))
    with hpunch
    "Both Camila and Lexi turn to glare at me in the same instance."
    "And from the look in their eyes, I find myself taking a step backwards."
    mike.say "Do we have to do this here in the street?"
    show lexi annoyed
    show camila normal
    "To my surprise, Camila and Lexi nod."
    camila.say "You're right, [hero.name]."
    mike.say "I am?"
    show lexi normal
    lexi.say "Yeah - we should settle this down that alleyway!"
    "Before I can protest, each of them grabs one of my wrists." with hpunch
    "And then they drag me down the alleyway after them."
    "Once we're out of sight, they stop and let go of me."
    hide lexi
    hide camila
    show lexi date at left5
    show camila work at right5
    with vpunch
    "Which sees me slumping against the wall."
    camila.say "Okay, so how are we going to settle this?"
    lexi.say "Hmm..."
    show lexi flirt
    lexi.say "Duelling blowjobs?"
    show camila flirt
    camila.say "You're on!"
    show lexi at zoomAt(1.8, (350, 1275))
    show camila at zoomAt(1.8, (1000, 1275))
    "As one, Camila and Lexi advance on me."
    mike.say "Wait a minute..."
    mike.say "What are you..."
    "Before I can finish, they haul down my pants and shorts." with vpunch
    "Then they kneel down in front of me, one to either side."
    "Camila's hands shoot out and unzip my flies in the blink of an eye."
    "And once they're open, Lexi shoves one of hers into my pants!"
    lexi.say "Oh...oh..."
    lexi.say "I got it!"
    show criminal harem bj with vpunch
    "I gasp as Lexi hauls my cock out of my pants."
    "Before I can say a word, Camila grabs it too."
    mike.say "Urgh..."
    mike.say "Ouch!"
    "No matter what sounds come out of my mouth, it doesn't seem to matter."
    "Camila and Lexi are totally ignoring me as they pursue this weird vendetta of theirs."
    show criminal harem bj handjob
    "Both of them are stroking the shaft of my cock now."
    "And I guess they're trying to be sensual and arousing."
    "But I feel more like they're bruising me badly in the effort!"
    "It's only when they begin to push and shove each other than things change."
    "Camila and Lexi are only slapping and squabbling."
    "But the sight of them doing that is hot in a very weird way."
    "And I can't help the way it's making me get hard either!"
    camila.say "Look!"
    camila.say "It's working!"
    lexi.say "You mean I'm making it work!"
    "As soon as my cock is halfway to being hard, they pounce on it."
    show criminal harem bj camlick lexlick -handjob
    "Camila and Lexi both lean in, their mouths open and tongues out."
    "But there's no way they can occupy the same space."
    show criminal harem bj camnormal
    "So their heads crack together!" with hpunch
    camila.say "Ouch!"
    lexi.say "Ooh - looks like my head's harder!"
    "Lexi leaps on the chance to get there first, wrapping her lips around the head."
    "She does all that she can to make it a pleasurable experience for me."
    "But she only has a couple of seconds before Camila drags her off again!"
    show criminal harem bj lexnormal camlick
    "Tossing Lexi aside, Camila dives in to take her place."
    show criminal harem bj camsuck
    "And just like that, she's the one sucking and licking like her life depends on it!"
    show criminal harem bj
    "Time and again the girls dislodge each other, until one goes high and one low."
    "Suddenly the experience becomes so much more enjoyable for me."
    "Once of them is working the head and the other the shaft."
    "And I feel myself leaning back against the wall as it gets better."
    "Somehow the lack of fighting also seems to calm the girls down too."
    show criminal harem bj lexnormal camnormal
    "I'm amazed to see them change places more than once."
    show criminal harem bj lexsuck
    "They do so smoothly and without conflict too!"
    "All I can do is lie back and stare down at them in amazement."
    "It's like someone cast a spell over them or something."
    "Tongues, lips and teeth are doing a dance around my cock."
    "And it's getting better with each moment that passes too."
    mike.say "Oh..."
    mike.say "Oh shit..."
    show criminal harem bj lexnormal camnormal
    "I don't know if it's my faltering words that tip the girls off."
    "Or if they can feel what's happening in the movements of my body."
    show criminal harem bj lexlick camlick
    "But either way, they seem to know that I'm cumming before I do."
    if camila.sub > lexi.sub:
        "For a moment I think they're going to cooperate until the end."
        show criminal harem bj lexnormal
        "But then Camila elbows Lexi in the ribs and pushes her out of the way." with hpunch
        show criminal harem bj camsuck
        "Then she pounces on my cock, taking it into her mouth."
        show criminal harem bj cum
        "I shoot my load as soon as she's wrapped her lips around it."
        "And Camila swallows everything I have to give without hesitation."
        lexi.say "Urgh..."
        lexi.say "Typical cop - rotten to the core!"
    elif lexi.sub > camila.sub:
        "For a moment I think they're going to cooperate until the end."
        show criminal harem bj camnormal
        "But then Lexi elbows Camila in the ribs and pushes her out of the way." with hpunch
        show criminal harem bj lexsuck
        "Then she pounces on my cock, taking it into her mouth."
        show criminal harem bj cum with vpunch
        "I shoot my load as soon as she's wrapped her lips around it."
        with vpunch
        "And Lexi swallows everything I have to give without hesitation."
        camila.say "Urgh..."
        camila.say "You never change, Lexi..."
        camila.say "Once a crook, always a crook!"
    else:
        "Camila and Lexi kneel in front of me, side by side."
        "Apparently the truce between them is still holding."
        show criminal harem bj lexnormal camnormal cum with vpunch
        "And it lasts even as I shoot my load over them."
        show criminal harem bj facecum dickcum -cum with vpunch
        "Both of their smiling faces are spattered with cum."
        "Lines of it pass over one and then the other."
        show criminal harem bj flacid
        "Which means strands drip between them too."
        camila.say "Urgh..."
        camila.say "I needed that!"
        lexi.say "See, [hero.name]?"
        lexi.say "I told you this wasn't such a bad part of town!"
    $ hero.replace_activity()
    if game.active_date:
        $ game.active_date.stay = False
    "Camila and Lexi left me alone in the middle of the alley."
    "So I head back home and went to bed"
    $ game.room = "bedroom1"
    call sleep from _call_sleep_82
    return

label missed_criminal_harem_event_04(from_cancel=False):
label missed_criminal_harem_date(from_cancel=False):
    if not from_cancel:
        "Shit, I missed my date. Lexi and Camila are going to be mad."
        $ lexi.love -= 10
        $ camila.love -= 10
    return

label criminal_harem_event_04(appointment=None):
    $ renpy.dynamic(lexi_score=0, camila_score=0)
    scene bg door restaurant with fade
    "I'm standing on the street outside the restaurant."
    "And I'm checking the time what feels like every few seconds."
    "But all I can think of is one of those documentaries about negotiating a ceasefire to end a war."
    "Yeah, I know - that's a pretty weird thing to have on my mind when I'm supposed to be on a date."
    "Yet it feels really familiar when I remember what I had to go through to organise all of this."
    "I mean, Camila and Lexi aren't a couple of warring nations."
    "But there are a lot of similarities from my point of view."
    "I must have suggested a hundred different things we could do on a double-date together."
    "And I also watched as ninety nine of them were shot down in flames too."
    "Lexi won't go bowling because the shoes they make you wear are disgusting."
    "Camila won't do go-karting because it could give her flashbacks to car chases at work."
    "And on and on, until I just suggested that we go for a meal at a nice restaurant."
    "I was expecting them both to reject it as a lame idea."
    "But to my surprise, they both agreed to it!"
    "Only now they're both late, and I'm starting to get worried..."
    show lexi happy date nophone at center, zoomAt(1.5, (640, 1040)) with hpunch
    lexi.say "Hiya, [hero.name]!"
    with vpunch
    mike.say "Wha..."
    "Yeah, I know - it's not too manly to yelp and jump three feet into the air."
    "But Lexi just pretty much sneaked up on me and spoke straight into my ear!"
    show lexi annoyed date
    lexi.say "Geez..."
    lexi.say "What's gotten you so jumpy?"
    mike.say "I don't know, Lexi..."
    mike.say "How about people showing up late?"
    mike.say "And making me jump out of my skin too!"
    "Lexi rolls her eyes and waves away my concern."
    hide lexi
    show lexi annoyed date nophone
    with fade
    "Effectively letting me know she couldn't give a damn."
    lexi.say "Whatever, [hero.name]."
    show lexi normal
    lexi.say "I'm not THAT late!"
    lexi.say "And anyway, I don't see Dirty Harriet anywhere around here!"
    "I frown as I have to admit that Lexi's right."
    "She might be late, but she's here before Camila."
    mike.say "I don't know, Lexi."
    mike.say "She hasn't called or anything either."
    lexi.say "Well I'm starving!"
    lexi.say "Let's get in there already, yeah?"
    lexi.say "She can catch up when she gets her ass here!"
    menu:
        "We're waiting Camila":
            mike.say "We can't go inside without Camila."
            mike.say "So we're just going to have to wait here for her."
            show lexi annoyed
            "I can see that this idea instantly displeases Lexi."
            "But I chose not to phrase it as a question."
            "And I don't give her the chance to object."
            "Instead I keep from making eye-contact with her."
            "And I scan the street until I finally see Camila approaching."
            show camila surprised date at top_mostright with easeinright
            camila.say "What are you guys doing standing around out here?"
            mike.say "Erm..."
            mike.say "We're waiting for you, Camila!"
            lexi.say "Yeah, what the hell does it look like?"
            show camila normal
            camila.say "Why didn't you wait inside?"
            camila.say "Maybe at the bar?"
            show lexi angry
            lexi.say "That's what I said!"
            show lexi annoyed
            mike.say "Lexi, that's a lie!"
            mike.say "You wanted to eat without her!"
            show camila annoyed at right4
            show lexi at left5
            with ease
            "Camila steps between Lexi and I as we begin to squabble."
            "And she holds up a hand to silence us both."
            show camila bored
            camila.say "Urgh..."
            camila.say "Will you two stop it?"
            camila.say "I had a hard day and I am not in the mood!"
            "Muttering under our breath and casting accusing glances, Lexi and I do as we're told."
            "Then we all walk into the restaurant together, already feeling awkward and annoyed."
            $ lexi_score -= 1
            $ camila_score += 1
        "Let's grab a drink while we wait for her":
            "Suddenly I remember something about the restaurant."
            "It has a small bar for just this kind of situation."
            "Not big enough to spend the night drinking in."
            "But the perfect size to wait for a dining companion running late."
            mike.say "How about we compromise, Lexi?"
            mike.say "Get a drink and wait in the bar?"
            show lexi annoyed
            "Lexi looks like she's about to object on principle."
            "Then, as she actually thinks it over, her expression changes."
            show lexi wink
            lexi.say "Sure - why not?"
            scene bg restaurant
            show lexi normal date nophone
            with fade
            "We head inside and order a couple of drinks at the bar."
            show camila date sad at right with easeinright
            "And soon enough, Camila walks in a little later."
            camila.say "Sorry I'm late."
            camila.say "I got tied up at the end of my shift."
            show lexi wink
            lexi.say "I hope you mean that literally!"
            mike.say "No worries, Camila."
            mike.say "Let me get you something to drink."
            mike.say "Then we can get to the table..."
            show camila happy
            "Camila seems happy with the arrangement."
            "And the alcohol seems to have taken the edge off of Lexi's mood too."
            "So that's a small victory at least."
            $ lexi_score += 1
            $ camila_score += 1
        "Let's seat":
            mike.say "You know what, Lexi - you're right!"
            show lexi surprised at startle
            lexi.say "I am?!?"
            mike.say "Sure you are."
            mike.say "Camila could have called ahead and told me she was going to be late."
            mike.say "So it serves her right if we start without her."
            show lexi happy
            "Lexi looks pleased as hell with my decision."
            "And she wraps her arm in mine as I lead the way inside."
            scene bg restaurant
            show lexi happy date nophone zorder 2 at center, zoomAt(1.5, (640, 1140))
            with fade
            "Soon enough we're sat at the table, reading the menu."
            "Which is the precise moment Camila walks in too."
            show camila annoyed date zorder 1 at right with easeinright
            camila.say "What are you guys doing?"
            show lexi normal
            mike.say "Erm..."
            mike.say "We're sitting down for a meal, Camila!"
            lexi.say "Yeah, what the hell does it look like?"
            camila.say "Why didn't you wait for me?"
            show camila angry
            camila.say "Maybe at the bar?"
            mike.say "You didn't call to tell us you were running late, Camila."
            lexi.say "So we started without you!"
            "Camila holds up a hand to silence us both."
            camila.say "Urgh..."
            camila.say "Will you two stop it?"
            show camila annoyed
            camila.say "I had a hard day and I am not in the mood!"
            show lexi date at center, zoomAt(1.5, (340, 1140))
            show camila date at center, zoomAt(1.5, (940, 1040))
            with fade
            show camila at center, zoomAt(1.5, (940, 1140)) with ease
            "She sits down at the table, clearly not pleased with Lexi and me."
            "Which makes for an awkward start to the date."
            $ lexi_score += 1
            $ camila_score -= 1
        "Grab us seats, I'll wait Camila at the bar":
            "Suddenly I remember something about the restaurant."
            "It has a small bar for just this kind of situation."
            "Not big enough to spend the night drinking in."
            "But the perfect size to wait for a dining companion running late."
            mike.say "I'm going to wait for Camila at the bar."
            mike.say "You want to come join me?"
            show lexi at startle
            "Lexi snorts and shakes her head."
            lexi.say "Hah!"
            show lexi annoyed
            lexi.say "Do I fuck!"
            lexi.say "You do what you like - I'm going to the table."
            hide lexi with easeoutleft
            "I shake my head as Lexi strides off on her own."
            scene bg restaurant with fade
            "Then I head to the bar and order a drink for myself."
            "And soon enough, Camila walks in a little later."
            show camila sad date at right with easeinright
            camila.say "Sorry I'm late."
            show camila normal date
            camila.say "I got tied up at the end of my shift."
            mike.say "I hope you don't mean literally!"
            mike.say "Let me get you something to drink."
            mike.say "Then we can get to the table..."
            show camila surprised
            "Camila nods and then looks around with a puzzled expression."
            camila.say "Is Lexi not here yet?"
            mike.say "Yeah, but she went straight to the table."
            show camila normal
            "Camila rolls her eyes and shakes her head."
            camila.say "Typical!"
            show camila annoyed at center with ease
            "We walk over to the table as soon as Camila has her drink."
            "And she's clearly not pleased with Lexi."
            "Which makes for an awkward start to the date."
            "But at least she's not mad at me!"
            $ lexi_score += 1
            $ camila_score += 1
    scene bg restaurant
    show lexi normal date nophone at center, zoomAt(1.5, (340, 1140))
    show camila normal date at center, zoomAt(1.5, (940, 1140))
    with fade
    "Now that everyone's sitting around the table, we can get our date started."
    "So I give Camila and Lexi what I hope is one of my best smiles."
    mike.say "I hope you guys like this place."
    mike.say "I've heard a lot of good things about it!"
    "I'm expecting at least one of the girls to respond."
    "But it looks like they're just staring at each other."
    lexi.say "I'm up for having a good time, [hero.name]."
    show lexi happy
    lexi.say "Like, I was the one that actually got here on time!"
    show camila annoyed
    camila.say "I already explained that, Lexi."
    camila.say "I was busy working."
    show camila happy
    camila.say "Probably busting some of your closest friends!"
    show lexi angry
    lexi.say "What did you just say?!?"
    lexi.say "Most of my friends from back in the day were bent cops!"
    show camila angry
    "Suddenly both of them look like they're spoiling for a fight."
    "And I know that I have to do something before it actually comes to one!"
    menu:
        "Scold Lexi":
            "Normally I can just ignore most of the stuff Lexi comes out with."
            "But for some reason her digging at Camila right now gets under my skin."
            mike.say "You really shouldn't talk about Camila's work like that, Lexi."
            mike.say "She's out there almost every single day, keeping the streets safe."
            mike.say "And it's not like you had a great time with the people she's arresting."
            mike.say "I mean, don't tell me that ape Danny never treated you badly!"
            show lexi surprised
            show camila normal
            "Lexi's face is a picture of amazement as I fire back at her."
            "But all too soon it turns into one of embarrassment."
            lexi.say "Okay, okay..."
            show lexi annoyed
            lexi.say "I get the message!"
            lexi.say "No need to throw it in my face..."
            "I feel a pang of regret at having done that to Lexi."
            "But then I remind myself that it did the trick all the same."
            "She's dropped the subject now."
            "And hopefully that's the end of it for tonight."
            $ lexi_score -= 1
            $ camila_score += 1
        "Scold Camila":
            "I know that Lexi's got a pretty chequered past."
            "And Camila's all about treading a moral path in life."
            "But I just don't like the way she keeps talking to Lexi like that."
            mike.say "Okay, Camila, we get it."
            mike.say "Lexi has a dodgy past."
            mike.say "And you're a big, bad cop that won't let her forget it."
            mike.say "You think we can leave it alone long enough to eat?"
            show camila surprised
            show lexi normal
            "Camila's face is a picture of amazement as I fire back at her."
            "But all too soon it turns into one of embarrassment."
            camila.say "I...I didn't know you felt like that, [hero.name]."
            show camila annoyed
            camila.say "If you feel so strongly, I'll stop it, okay?"
            camila.say "Just don't keep on rubbing my face in it..."
            "I feel a pang of regret at having done that to Camila."
            "But then I remind myself that it did the trick all the same."
            "She's dropped the subject now."
            "And hopefully that's the end of it for tonight."
            $ lexi_score += 1
            $ camila_score -= 1
        "Scold both":
            "Urgh..."
            "Why does it always have to be like this with these two?"
            "Can't we have one date when they're not squabbling?"
            mike.say "Okay, that's enough!"
            mike.say "Will you two stop arguing already?"
            show lexi surprised at center, zoomAt(1.0, (340, 1140)), startle
            show camila surprised at center, zoomAt(1.0, (940, 1140)), startle
            "Camila and Lexi turn to look at me as one."
            "And they both look surprised at me stepping into the argument."
            camila.say "B...but..."
            camila.say "She started it!"
            lexi.say "You lying cow!"
            lexi.say "I did not!"
            mike.say "I don't give a shit."
            mike.say "Just drop it, okay?"
            show lexi annoyed
            show camila annoyed
            "The pair of them nod and then look down at the table."
            "I feel a pang of regret at having done that to them."
            "But then I remind myself that it did the trick all the same."
            "They've dropped the subject now."
            "And hopefully that's the end of it for tonight."
            $ lexi_score -= 1
            $ camila_score -= 1
        "Try a more subtle approach" if hero.charm >= 60:
            "I really don't want to take sides here."
            "But I feel like I have to do something to stop them arguing."
            "I'm racking my brain for a solution, and then it hits me."
            mike.say "You know something..."
            mike.say "You two are like two halves of a complete person!"
            show lexi surprised at center, zoomAt(1.0, (340, 1140)), startle
            show camila surprised at center, zoomAt(1.0, (940, 1140)), startle
            "Camila and Lexi turn to look at me as one."
            "And they both look surprised as hell by what I just said."
            camila.say "What on earth is that supposed to mean?"
            show camila angry
            lexi.say "Yeah, we've got nothing in common at all!"
            show lexi angry
            mike.say "Exactly, Lexi - that's what I mean!"
            mike.say "You're two tough chicks."
            mike.say "But one's on the side of good and the other the side of evil!"
            camila.say "Wait..."
            show camila normal
            camila.say "I think I see what you mean!"
            lexi.say "Me too..."
            show lexi normal
            lexi.say "Like, Camila's evil because she's a cop?"
            camila.say "Hey - that's not what he means!"
            "I can't help chuckling at the fact they're still squabbling."
            mike.say "You two should write a book together."
            mike.say "At least start a podcast!"
            "It was a pretty risky gamble, but it did the trick all the same."
            "They've dropped the subject and their talking about something else now."
            "And hopefully that's the end of the arguing for tonight."
            $ lexi_score += 1
            $ camila_score += 1
    show lexi normal
    show camila normal
    "At last we're all studying the menu's like our lives depend on it."
    "And it's not before time, as I can almost hear my stomach growling!"
    $ date_event = randint(0, 2)
    if date_event == 0:
        "Suddenly Lexi looks up from her menu."
        "And she has an expression of serious concern on her face."
        lexi.say "Hey, you guys..."
        show lexi annoyed
        lexi.say "I just thought of something serious!"
        lexi.say "Who's paying for all of this?"
        "Camila looks at her sideways."
        show camila surprised
        "Her own expression one of puzzlement."
        camila.say "Huh?"
        camila.say "I just assumed we were splitting it!"
        lexi.say "That's easy for you to say..."
        lexi.say "What with that fat cop salary of yours!"
        lexi.say "Some of us aren't so flush with cash."
        camila.say "What's the problem, Lexi?"
        show camila angry
        camila.say "Didn't you lift enough wallets this month?"
        show lexi angry
        "Here we go again!"
        "Looks like I'm going to have to step in before a second time."
        menu:
            "Camila will pay":
                mike.say "You're not going to like this, Camila..."
                mike.say "But Lexi does kind of have a point."
                mike.say "Out of all of us, you probably make the most!"
                show camila angry
                show lexi normal
                "Camila shoots me a look that could curdle milk."
                camila.say "Well what if I do?"
                camila.say "My job's a hundred times more dangerous than yours!"
                camila.say "And since when did Lexi even have a real job?"
                show camila annoyed
                lexi.say "Real is such a limiting term!"
                lexi.say "I prefer to think of myself as versatile..."
                mike.say "Yeah, Camila..."
                mike.say "I get all of that."
                mike.say "But aren't you paid by the government?"
                mike.say "And doesn't that money come out of my taxes?"
                "For a moment I think Camila's actually going to slap me."
                "But then she seems to reign in her rage."
                show camila angry
                camila.say "We're splitting the bill, okay?"
                camila.say "And that's all there is to it!"
                $ lexi_score += 1
                $ camila_score -= 1
            "Lexi will pay":
                mike.say "You're not going to like this, Lexi..."
                mike.say "But Camila does kind of have a point."
                mike.say "You always like to brag about how much money your schemes make."
                mike.say "But you never seem to have any of it to spread around!"
                "I try to put a smile on my face as I say this."
                show lexi angry
                show camila normal
                "But I can see that Lexi's looking daggers at me."
                lexi.say "That's none of your business, [hero.name]."
                lexi.say "And even if I do make a ton of money..."
                lexi.say "Wouldn't that mean you were benefiting from the profits of crime?"
                show lexi annoyed
                camila.say "Yeah..."
                camila.say "She's kind of got a point there!"
                mike.say "But on the other hand, Lexi..."
                mike.say "We could have reported you to the authorities already."
                mike.say "So you do kind of owe us for our continued silence!"
                "For a moment I think Lexi's actually going to slap me."
                "But then she seems to reign in her rage."
                show lexi angry
                lexi.say "We're splitting the bill, okay?"
                lexi.say "And that's all there is to it!"
                $ lexi_score -= 1
                $ camila_score += 1
            "I'll pay":
                mike.say "Well..."
                mike.say "I was the one that suggested we do this."
                mike.say "So I guess I could foot the bill this once."
                mike.say "You know, make it my treat?"
                "I'm expecting Camila and Lexi to thank me instantly."
                "But instead I find them both glaring at me instead."
                show lexi annoyed
                show camila annoyed
                camila.say "You think I can't pay my way?"
                camila.say "That I need you to bail me out?"
                lexi.say "I gotta say, [hero.name]..."
                lexi.say "That's pretty sexist of you!"
                mike.say "What are you talking about?"
                mike.say "I was just trying to be a gentleman!"
                lexi.say "What do you think this is, the past?"
                lexi.say "Next thing you'll be putting your coat over puddles!"
                camila.say "Keep your patriarchal oppression to yourself, [hero.name]."
                mike.say "Okay, okay..."
                mike.say "We'll split the damn bill!"
                $ lexi_score -= 1
                $ camila_score -= 1
            "Let's split" if hero.charm >= 75:
                mike.say "Sorry, guys..."
                mike.say "I kind of just assumed we'd be splitting the bill three ways!"
                "I was hoping this would be enough to settle the matter."
                "But Camila and Lexi both look less than happy with me."
                show lexi annoyed
                show camila annoyed
                camila.say "Oh no, I've been on nights out with the department."
                camila.say "I know how this goes!"
                lexi.say "There's always someone that says we're splitting the bill."
                lexi.say "And then they go and order really expensive shit!"
                lexi.say "All while you're trying to reign it in!"
                show camila surprised
                "Camila looks at Lexi in surprise."
                camila.say "Erm..."
                camila.say "That's pretty much exactly what I was going to say."
                show camila annoyed
                lexi.say "Weird!"
                lexi.say "Maybe cops and crooks aren't that different after all?"
                mike.say "Look..."
                mike.say "I have an app on my phone for this."
                mike.say "We all put in what we order and how much it costs."
                mike.say "Then at the end of the meal it tells us exactly what we each owe."
                show camila normal
                camila.say "Hmm..."
                camila.say "I can live with that."
                show lexi normal
                lexi.say "Me too."
                mike.say "Great, guys..."
                mike.say "That's all settled then!"
                $ lexi_score += 1
                $ camila_score += 1
    elif date_event == 1:
        lexi.say "Geez..."
        show lexi annoyed
        lexi.say "There's some really weird shit on here!"
        "I glance up in time to see Lexi shaking her head."
        mike.say "What are you talking about, Lexi?"
        mike.say "I don't see anything out of the ordinary."
        "Just then Camila chimes up from the other side of the table."
        camila.say "She's not wrong, [hero.name]."
        show camila annoyed
        camila.say "I mean look..."
        "Camila jabs a finger at the menu."
        camila.say "They have something called gravel on the menu!"
        show camila normal
        "I look over to see where she's pointing."
        "And I actually have to stop myself from laughing."
        "Camila's got it pretty wrong on that one."
        lexi.say "Oh yeah!"
        show lexi normal
        lexi.say "I see what you mean."
        "Oh no - now Lexi's doing it too!"
        menu:
            "Correct Camila":
                "I shake my head and let out a chuckle."
                mike.say "Not gravel, Camila..."
                mike.say "Gravlax!"
                "Camila frowns at my laughter."
                show camila annoyed
                "And she instantly becomes defensive."
                camila.say "Oh yeah..."
                camila.say "Because that explains what the hell it actually is!"
                mike.say "It's a Scandinavian dish, Camila."
                mike.say "Salmon pickled in salt and sugar."
                "Lexi grimaces as I describe the dish."
                lexi.say "Eww!"
                show lexi annoyed
                lexi.say "No wonder they had to come up with a dumb name for it!"
                lexi.say "That sounds gross!"
                mike.say "It's actually a delicacy."
                mike.say "But maybe a cheeseburger would be a safer bet, Camila?"
                show lexi happy at center, zoomAt(1.0, (340, 1140)), vshake
                "Lexi laughs at the suggestion."
                "But I can see that Camila's less than impressed."
                $ lexi_score += 1
                $ camila_score -= 1
            "Correct Lexi":
                "I shake my head and let out a chuckle."
                mike.say "Not gravel, Lexi..."
                mike.say "Gravlax!"
                "Lexi frowns at my laughter."
                show lexi annoyed
                "And she instantly becomes defensive."
                lexi.say "Hey!"
                lexi.say "What are you picking on me for?"
                lexi.say "Camila's the one that thought it was gravel!"
                mike.say "It's a Scandinavian dish, Lexi."
                mike.say "Salmon pickled in salt and sugar."
                mike.say "But at least Camila admitted she didn't know what it was."
                "Camila grimaces as I describe the dish."
                camila.say "That does not sound good!"
                show camila annoyed
                camila.say "I wish you'd never explained it to me!"
                lexi.say "That sounds gross!"
                mike.say "It's actually a delicacy."
                mike.say "But maybe a safer bet would be a sloppy joe, Lexi"
                show camila happy at center, zoomAt(1.0, (940, 1140)), vshake
                "Camila laughs at the suggestion."
                "But I can see that Lexi's less than impressed."
                $ lexi_score -= 1
                $ camila_score += 1
            "Correct Camila and Lexi":
                "I shake my head and let out a chuckle."
                mike.say "Not gravel, you pair of dummies..."
                mike.say "Gravlax!"
                "Camila and Lexi frown at my laughter."
                show lexi annoyed
                show camila annoyed
                "And they instantly become defensive."
                camila.say "Oh yeah..."
                camila.say "Because that explains what the hell it actually is!"
                lexi.say "Hey!"
                lexi.say "What are you picking on me for?"
                lexi.say "Camila's the one that thought it was gravel!"
                mike.say "It's a Scandinavian dish."
                mike.say "Salmon pickled in salt and sugar."
                mike.say "It's actually a delicacy."
                mike.say "But maybe a couple of cheeseburgers would be a safer bet?"
                mike.say "At least for the pair of you!"
                "I laugh at my own suggestion."
                "But I can see that Camila and Lexi are less then impressed."
                $ lexi_score -= 1
                $ camila_score -= 1
            "Fun facts about 'Gravlax'" if hero.has_skill("foodie") or hero.has_skill("cooking") or hero.knowledge >= 75:
                "I nod and make a point of smiling as I begin to explain."
                mike.say "It's a pretty weird one, right?"
                mike.say "They call it Gravlax, and it's from Scandinavia."
                mike.say "You pickle salmon in salt, sugar and dill."
                "Camila and Lexi frown at my description."
                show lexi annoyed
                show camila annoyed
                lexi.say "That sounds gross!"
                camila.say "Yeah...that does not sound good!"
                camila.say "I wish you'd never explained it to me!"
                mike.say "Some people actually consider it a delicacy."
                mike.say "But I can understand why it sound unappealing."
                "Camila and Lexi share a nod."
                "And they look more than a little relieved."
                show lexi normal
                show camila normal
                camila.say "Good thing we have you here, [hero.name]."
                camila.say "Otherwise we'd never have known what we were getting!"
                lexi.say "Damn right!"
                lexi.say "I could have ended up with sweet and sour aardvark!"
                show camila happy
                show lexi happy
                with vpunch
                "We share a knowing laugh and then get back to the menus."
                "And I feel more than a little proud of myself."
                "Because I managed to share some knowledge with the girls."
                "But I also did it in a way that didn't piss anyone off too."
                $ lexi_score += 1
                $ camila_score += 1
    else:

        "Pretty soon after we order, the food arrives."
        "And nobody stands on ceremony, beginning to eat straight away."
        "In fact everyone's pretty intent on their meals."
        "So much so that it goes quiet around the table."
        "Which is fine with me, as I'm practically ravenous."
        "That is until I hear the sound of someone sighing."
        camila.say "Phew..."
        show camila happy
        camila.say "I think that's me done!"
        "I glance up to see Camila pushing away her plate."
        "And then I see Lexi doing the same."
        lexi.say "That's what too many donuts will do to ya!"
        show lexi happy
        lexi.say "But yeah, I'm done too!"
        "I can't help staring at their plates in amazement."
        "Neither of them is even close to finishing off their portions!"
        mike.say "Are you guys serious?"
        mike.say "You're really going to leave all of that?!?"
        "Camila and Lexi stare at me in sheer amazement."
        camila.say "I'm totally full, [hero.name]!"
        show camila normal
        camila.say "Aren't you?"
        lexi.say "Yeah, [hero.name]..."
        show lexi normal
        lexi.say "You practically licked your plate clean already!"
        menu:
            "Camila, will you finish your plate?":
                mike.say "Yeah, I know..."
                mike.say "But I still need to fill in the corners!"
                "I feel the need to under line my point."
                "So I gesture to Camila's plate with my fork."
                mike.say "Camila..."
                mike.say "Are you going to eat that?"
                "Camila shakes her head in amazement."
                show camila annoyed
                camila.say "No, I guess not..."
                mike.say "Then pass it this way!"
                "I reach over and take the plate."
                "And then I proceed to demolish Camila's leftovers."
                "But as I do so, I can see her starting to blush."
                show camila sad
                "For a moment I wonder if I'm embarrassing her."
                "Then I tell myself it's more likely she's ashamed of herself."
                "I mean, imagine paying all that money for a meal you can't finish!"
                $ lexi_score += 1
                $ camila_score -= 1
            "Lexi, will you finish your plate?":
                mike.say "Yeah, I know..."
                mike.say "But I still need to fill in the corners!"
                "I feel the need to under line my point."
                "So I gesture to Lexi's plate with my fork."
                mike.say "Lexi..."
                mike.say "Are you going to eat that?"
                "lexi shakes her head with a frown."
                show lexi annoyed
                lexi.say "Nah, I couldn't eat another mouthful!"
                mike.say "Then pass it this way!"
                "I reach over and take the plate."
                "And then I proceed to demolish Lexis's leftovers."
                "But as I do so, I can see her starting to blush."
                show lexi sad
                "For a moment I wonder if I'm embarrassing her."
                "Then I tell myself it's more likely she's ashamed of herself."
                "I mean, imagine paying all that money for a meal you can't finish!"
                $ lexi_score -= 1
                $ camila_score += 1
            "You won't finish your plates, won't you?":
                mike.say "Yeah, I know..."
                mike.say "But I still need to fill in the corners!"
                "I feel the need to under line my point."
                "So I gesture to Camila and Lexi's plates with my fork."
                mike.say "Are you going to eat that?"
                "Camila shakes her head in amazement."
                show camila annoyed
                camila.say "No, I guess not..."
                "lexi shakes her head with a frown."
                lexi.say "Nah, I couldn't eat another mouthful!"
                show lexi annoyed
                mike.say "Then pass it this way!"
                "I reach over and take the plates."
                "And then I proceed to demolish Camila and Lexis's leftovers."
                "But as I do so, I can see them starting to blush."
                show lexi sad
                show camila sad
                "For a moment I wonder if I'm embarrassing the girls."
                "Then I tell myself it's more likely they're ashamed of themselves."
                "I mean, imagine paying all that money for a meal you can't finish!"
                $ lexi_score -= 1
                $ camila_score -= 1
            "Ask for a doggy bag" if hero.has_skill("iron_stomach"):
                mike.say "I'm not hungry right now."
                mike.say "But would you mind if I asked the waiter for a doggy-bag?"
                mike.say "This food is so expensive."
                mike.say "It'd be a shame to let it go to waste!"
                "I'm honestly expecting Camila and Lexi to object."
                "But instead they seem to come round to the idea as they think about it."
                show lexi happy
                show camila happy
                camila.say "Why not, [hero.name]."
                camila.say "I was worried about the expense."
                camila.say "But knowing it's going to get eaten kinda helps with that."
                "Lexi nods as she chimes in too."
                lexi.say "Nothing wrong with a doggy bag."
                lexi.say "Being thrifty never goes out of fashion!"
                "I nod and call the waiter over."
                "Then I whisper my request into his ear."
                "The guy nods and begins to clear the plates away."
                "That done, he hurries off to do as I asked."
                $ lexi_score += 1
                $ camila_score += 1
    show lexi normal
    show camila normal
    with fade
    "Now that the meal's over, the waiter brings over the bill."
    "It comes in one of those leather folders so that the total is hidden."
    "And we each take turns in looking it over and grimacing."
    show camila annoyed
    camila.say "Ouch!"
    camila.say "I'm glad we don't do this too often."
    camila.say "Otherwise I'd have to start taking bribes to pay for my share!"
    show lexi surprised
    lexi.say "Oooh..."
    lexi.say "I don't suppose you guys are up for a dine and dash?"
    "This earns Lexi a couple of hard stares from Camila and me."
    show lexi wink
    lexi.say "Joking!"
    show lexi annoyed
    lexi.say "I was only joking!"
    mike.say "Look, I know that it seems like a lot."
    mike.say "But this is kind of a special date."
    mike.say "And the food was great."
    mike.say "So we're going to tip what, twenty five percent?"
    "I hear an intake of breath from Camila and Lexi."
    "Then I see they're both shaking their heads."
    lexi.say "Sure, we've got to leave a tip."
    show lexi normal
    lexi.say "But ten percent's more than enough."
    camila.say "What are you talking about?"
    camila.say "We're going to pay the bill."
    show camila normal
    camila.say "So why should we have to leave a tip?"
    menu:
        "25%%":
            mike.say "Twenty five percent is pretty standard, guys."
            mike.say "It's about what waiting staff need to earn decent amount."
            mike.say "So if you're not going to tip that much, I'll do it myself."
            "I can tell that this doesn't make me popular with Camila and Lexi."
            "But I cross my arms over my chest, letting them know that I won't be moved."
            "And in the end, Camila's the first to crack."
            camila.say "Okay, you twisted my arm - but just this once!"
            show camila annoyed
            camila.say "Imagine if I asked for a tip before arresting someone, for god's sake!"
            "Camila breaking seems to weaken Lexi's will too."
            "And soon enough she surrenders."
            lexi.say "Fine, fine..."
            show lexi annoyed
            lexi.say "But this is daylight robbery!"
            "I choose to ignore the irony of what Lexi's saying."
            "And instead I get on with paying the bill."
            $ lexi_score -= 1
            $ camila_score -= 1
        "10%%":
            mike.say "Twenty five percent is pretty standard, guys."
            mike.say "It's about what waiting staff need to earn decent amount."
            mike.say "But just for the sake of peace and harmony - let's tip to ten percent instead."
            "I can tell that this doesn't make me popular with Camila."
            "But Lexi leaps in before she can object."
            lexi.say "Done!"
            show lexi happy
            lexi.say "Come on, Camila - pay up!"
            camila.say "Okay, you twisted my arm - but just this once!"
            show camila annoyed
            camila.say "Imagine if I asked for a tip before arresting someone, for god's sake!"
            "I choose to ignore the silliness of what Camila's saying."
            "And instead I get on with paying the bill."
            $ lexi_score += 1
            $ camila_score -= 1
        "No tip":
            mike.say "Twenty five percent is pretty standard, guys."
            mike.say "It's about what waiting staff need to earn decent amount."
            mike.say "But just for the sake of peace and harmony..."
            mike.say "Let's just forget about the tip this one time."
            "I can tell that this doesn't make me popular with Lexi."
            "But Camila leaps in before she can object."
            camila.say "Agreed!"
            show camila happy
            camila.say "Two to one, Lexi."
            camila.say "You're outvoted!"
            lexi.say "Fine, fine..."
            show lexi annoyed
            lexi.say "But you're robbing that poor waiter!"
            "I choose to ignore the irony of what Lexi's saying."
            "And instead I get on with paying the bill."
            $ lexi_score -= 1
            $ camila_score += 1
        "Find a diplomatic solution" if hero.charm + hero.knowledge >= 150:
            mike.say "Twenty five percent is pretty standard, guys."
            mike.say "It's about what waiting staff need to earn decent amount."
            mike.say "But just for the sake of peace and harmony - let's tip to ten percent instead."
            mike.say "And you can not contribute to the tip at all, Camila."
            mike.say "If that's what you want?"
            "I can see that neither Camila nor Lexi is totally happy."
            show lexi normal
            show camila normal
            "But they seem to be sucking it up all the same."
            camila.say "Don't try to make me feel guilty."
            camila.say "Imagine if I asked for a tip before arresting someone, for god's sake!"
            lexi.say "Fine, fine..."
            lexi.say "But you're robbing that poor waiter!"
            "I choose to ignore what the girls are saying."
            "And instead I get on with paying the bill."
            "Making sure to up the tip to twenty five percent."
            "But I do it out of my own pocket and when they're not looking too."
            $ lexi_score += 1
            $ camila_score += 1
    show camila normal
    show lexi normal
    "I hand the bill back to the waiter, expecting him to walk off with it."
    "But instead he pauses and makes a slight coughing sound behind his hand."
    "Waiter" "Can I get you anything else, sir?"
    "Waiter" "Tea?"
    "Waiter" "Coffee?"
    "Waiter" "Maybe even a shot of something a little stronger?"
    "I shoot a glance to Camila and Lexi."
    mike.say "What do you guys think?"
    mike.say "I could go for a coffee."
    "Lexi claps her hands together in delight."
    lexi.say "Screw the coffee."
    show lexi happy
    lexi.say "I like the sound of something stronger!"
    "But Camila shakes her head."
    camila.say "We already settled the bill."
    show camila happy
    camila.say "Let's get out of here before they make us spend more!"
    menu:
        "I'd like a coffee":
            "I could be swayed to agree with one of the girls."
            "But the allure of a nice coffee is too much to resist."
            mike.say "Spirits or nothing sounds like a choice between extremes!"
            mike.say "But I think a couple of cups of coffee is a good compromise."
            "Camila and Lexi shake their heads, not pleased with my decision."
            show camila annoyed
            show lexi annoyed
            camila.say "This is just a waste of money, [hero.name]."
            camila.say "We could just go someplace cheaper!"
            lexi.say "Oh man..."
            lexi.say "You guys are SO boring!"
            "I do the best I can to ignore then as I order the coffee."
            "And I tell myself that they'll thank me when it arrives."
            $ lexi_score -= 1
            $ camila_score -= 1
        "Something stronger":
            "As soon as Lexi mentions something stronger, I change my mind."
            "A shot of something strong would be the perfect end to the meal."
            mike.say "Lexi's got a point, Camila."
            mike.say "We're out to enjoy ourselves tonight."
            mike.say "So let's live a little!"
            show camila annoyed
            "Camila shakes her head, not pleased with my decision."
            camila.say "This is just a waste of money, [hero.name]."
            camila.say "We could just go someplace cheaper!"
            "But I can see from the look on Lexi's face that she approves."
            $ lexi_score += 1
            $ camila_score -= 1
        "We should leave":
            "As soon as Camila mentions the cost, I change my mind."
            "It's almost like I can feel the strain being put on my wallet!"
            mike.say "Camila's got a point, Lexi."
            mike.say "We did spend a lot already."
            mike.say "And we can always go someplace cheaper for a drink."
            "Lexi curls her lip, not pleased with my decision."
            show lexi annoyed
            lexi.say "Oh man..."
            lexi.say "You guys are SO boring!"
            "But I can see from the look on Camila's face that she approves."
            $ lexi_score -= 1
            $ camila_score += 1
        "Let's go somewhere else":
            "Suddenly I remember that this place has a pretty nice bar."
            mike.say "Okay, how about this..."
            mike.say "We stop off at the bar on the way out of here?"
            mike.say "That way we can each order what we want."
            mike.say "Or nothing at all, yeah?"
            "I watch as Camila and Lexi think it over."
            show lexi normal
            show camila normal
            "And I breathe a sigh of relief as they both nod."
            camila.say "So long as nobody judges me for not indulging."
            lexi.say "Or me for wanting something with a kick to it!"
            $ lexi_score += 1
            $ camila_score += 1
    scene bg street
    show lexi date normal at left5
    show camila date normal at right5
    with fade
    "As we leave the restaurant, my mind starts to turn to what happens next."
    "And as we stand on the street outside, I try to casually pose the question."
    mike.say "So..."
    mike.say "Are we all ready to call it a night?"
    mike.say "Or do you want to maybe do something else?"
    if camila_score >= 4 and lexi_score >= 4:
        camila.say "I'm up for doing something else."
        show camila happy
        camila.say "What did you have in mind?"
        lexi.say "Me too!"
        show lexi happy
        lexi.say "Let's go do something fun!"
        "I can't help smiling."
        "I was hoping that at least one of them would be up for it."
        "But both of them wanting to keep the date going..."
        "Well that's a total win for me!"
        call camila_lexi_threesome from _call_camila_lexi_threesome
    elif camila_score >= 4:
        lexi.say "I have to be up in the morning."
        lexi.say "So it's home for me!"
        camila.say "I'm up for doing something else."
        show camila happy
        camila.say "What did you have in mind?"
        hide lexi with dissolve
        "Lexi heads off in search of a taxi."
        "While Camila and I discuss what to do next."
        "And I keep telling myself that one girl is better than none."
        call camila_fuck_date_male from _call_camila_fuck_date_male
    elif lexi_score >= 4:
        camila.say "I'm still beat from work, [hero.name]."
        camila.say "So I'm going to call it a day."
        lexi.say "Not me!"
        show lexi happy
        lexi.say "I'm up for going someplace else."
        hide camila with dissolve
        "Camila heads off in search of a taxi."
        "While Lexi and I discuss what to do next."
        "And I keep telling myself that one girl is better than none."
        call lexi_fuck_date_male from _call_lexi_fuck_date_male
    else:
        camila.say "I'm still beat from work, [hero.name]."
        camila.say "So I'm going to call it a day."
        lexi.say "I have to be up in the morning."
        lexi.say "So it's home for me!"
        "I nod and do the best I can to look happy."
        hide lexi
        hide camila
        with dissolve
        "But as the girls go off in search of taxis, I wonder if I should have tried harder."
        $ game.pass_time(2)
    $ hero.replace_activity()
    if game.active_date:
        $ game.active_date.stay = False
    return

label camila_lexi_threesome:
    "Part of me can't actually believe that we made it this far."
    "The idea of being on a date with Camila and Lexi is a pretty crazy one to begin with."
    "To have made it through that without anyone causing a scene in public is one thing."
    "But for it to have gone so well that everyone's on the same page afterwards..."
    "Well, that's almost too much for me to be able to process!"
    "And yet here we are, all three of us stepping out of a taxi back at my place."
    scene bg livingroom with fade
    "Everyone's laughing and joking as we walk up to the front door and I let us in."
    $ game.room = "bedroom1"
    scene bg bedroom1 with fade
    "Nobody even questions it when I lead the way straight to my bedroom too."
    show camila date zorder 1 at left5
    show lexi date nophone zorder 2 at right5
    with easeinright
    "All it takes is for me to open the door, Camila and Lexi just walk right in!"
    "As I follow them and close the door behind me, I'm starting to get a swagger in my step."
    "I kind of feel like a wizard, one that can cast a spell over a girl!"
    "But the moment I turn around, I see something that bursts my bubble."
    "I see the girls standing by my bed, one on either side."
    "It's not that Camila and Lexi say anything."
    "In fact they're already starting to strip off their clothes."
    show camila naked
    show lexi naked
    with dissolve
    "So I should be extra excited right now."
    "It's just that there's something in the way they're looking at me."
    "Something that reminds me of those big-cats you see on nature documentaries."
    "They way they look at the poor, defenceless animal they're about to feast on!"
    mike.say "Erm..."
    mike.say "So..."
    mike.say "Here we are..."
    mike.say "All three of us!"
    "Camila and Lexi exchange a knowing glance."
    "And then Camila beckons me over with one crooked finger."
    "At the same time, Lexi sits down on the bed and pats the spot beside her."
    lexi.say "We're both over here, [hero.name]."
    show lexi wink
    lexi.say "So why don't you come join us?"
    camila.say "Yeah, [hero.name]..."
    show camila wink
    camila.say "What are you waiting for?"
    "This is totally crazy."
    show lexi normal
    show camila normal
    "I should be rushing over there and jumping onto the bed."
    "But all I can manage is a slow shuffle in that general direction."
    "Camila and Lexi are totally naked by now."
    "And it's hard to describe just how good the pair of them look."
    "I've spent so long trying to encourage them to get on too."
    "But now that they're on the same page, it's really kinda scary!"
    "All the energy that was going into then squabbling and sniping is being redirected."
    "Like it's going into a united effort to put me right where they want me."
    "Camila and Lexi are looking at me like they know just what I'm thinking too."
    show lexi happy
    show camila happy
    "They keep giggling and shaking their heads as I get ever closer."
    "Smiling as I take off one piece of clothing after another."
    camila.say "Come on, [hero.name]..."
    show camila normal
    camila.say "We won't bite - unless that's what you're into!"
    show lexi surprised
    lexi.say "Ooh!"
    show lexi normal
    lexi.say "What about your handcuffs, Camila?"
    lexi.say "We could do some bondage stuff with him!"
    with vpunch
    mike.say "H...handcuffs?"
    mike.say "Are you serious?!?"
    "I start to take a step backwards out of sheer instinct."
    "But Camila and Lexi have already waited this long."
    "And they're not about to let me spin things out any longer."
    show lexi at center, zoomAt(1.5, (840, 1040))
    "First Lexi leaps forwards and grabs hold of an arm."
    show camila at center, zoomAt(1.5, (440, 1040))
    "Then Camila realises what she's doing and lunges to grab the other."
    "Together they pull me down onto the bed, clambering all over me."
    camila.say "Hah!"
    camila.say "Who needs handcuffs?"
    lexi.say "Yeah, we can handle this guy ourselves!"
    "Okay, now I'm starting to wonder what I was actually afraid of."
    "After all, who wouldn't want to be manhandled by two beautiful women?"
    "Especially when you know just what they have in mind too!"
    "So I just decide to lie back and let them have their way with me."
    "This seems to do the trick for a short while."
    "I have the pleasure of their hands and lips all over my body."
    "But pretty soon I get the feeling that it's not going to be enough."
    "It's clear that Camila and Lexi are waiting for me to do something."
    "They're waiting for me to make a choice as to where this thing is going."
    "So it looks like I'm going to have to leap one way or the other."
    call camila_lexi_threesome_fuck from _call_camila_lexi_threesome_fuck
    return

label criminal_harem_fuck_date(appointment=None):
    if game.week_day % 2 == 0:
        "Part of me can't actually believe that we made it this far."
        "The idea of being on a date with Camila and Lexi is a pretty crazy one to begin with."
        "To have made it through that without anyone causing a scene in public is one thing."
        "But for it to have gone so well that everyone's on the same page afterwards..."
        "Well, that's almost too much for me to be able to process!"
        "And yet here we are, all three of us stepping out of a taxi back at my place."
        scene bg livingroom with fade
        "Everyone's laughing and joking as we walk up to the front door and I let us in."
        $ game.room = "bedroom1"
        scene bg bedroom1 with fade
        "Nobody even questions it when I lead the way straight to my bedroom too."
        show camila date zorder 1 at left5
        show lexi date nophone zorder 2 at right5
        with easeinright
        "All it takes is for me to open the door, Camila and Lexi just walk right in!"
        "As I follow them and close the door behind me, I'm starting to get a swagger in my step."
        "I kind of feel like a wizard, one that can cast a spell over a girl!"
        "But the moment I turn around, I see something that bursts my bubble."
        "I see the girls standing by my bed, one on either side."
        "It's not that Camila and Lexi say anything."
        "In fact they're already starting to strip off their clothes."
        show camila naked
        show lexi naked
        with dissolve
        "So I should be extra excited right now."
        "It's just that there's something in the way they're looking at me."
        "Something that reminds me of those big-cats you see on nature documentaries."
        "They way they look at the poor, defenceless animal they're about to feast on!"
        mike.say "Erm..."
        mike.say "So..."
        mike.say "Here we are..."
        mike.say "All three of us!"
        show camila flirt
        show lexi flirt
        "Camila and Lexi exchange a knowing glance."
        "And then Camila beckons me over with one crooked finger."
        "At the same time, Lexi sits down on the bed and pats the spot beside her."
        lexi.say "We're both over here, [hero.name]."
        show lexi wink
        lexi.say "So why don't you come join us?"
        camila.say "Yeah, [hero.name]..."
        show camila wink
        camila.say "What are you waiting for?"
        "This is totally crazy."
        show lexi normal
        show camila normal
        "I should be rushing over there and jumping onto the bed."
        "But all I can manage is a slow shuffle in that general direction."
        "Camila and Lexi are totally naked by now."
        "And it's hard to describe just how good the pair of them look."
        "I've spent so long trying to encourage them to get on too."
        "But now that they're on the same page, it's really kinda scary!"
        "All the energy that was going into then squabbling and sniping is being redirected."
        "Like it's going into a united effort to put me right where they want me."
        "Camila and Lexi are looking at me like they know just what I'm thinking too."
        show lexi happy
        show camila happy
        "They keep giggling and shaking their heads as I get ever closer."
        "Smiling as I take off one piece of clothing after another."
        camila.say "Come on, [hero.name]..."
        show camila normal
        camila.say "We won't bite - unless that's what you're into!"
        show lexi surprised
        lexi.say "Ooh!"
        show lexi normal
        lexi.say "What about your handcuffs, Camila?"
        lexi.say "We could do some bondage stuff with him!"
        with vpunch
        mike.say "H...handcuffs?"
        mike.say "Are you serious?!?"
        "I start to take a step backwards out of sheer instinct."
        "But Camila and Lexi have already waited this long."
        "And they're not about to let me spin things out any longer."
        show lexi at center, zoomAt(1.5, (840, 1040))
        "First Lexi leaps forwards and grabs hold of an arm."
        show camila at center, zoomAt(1.5, (440, 1040))
        "Then Camila realises what she's doing and lunges to grab the other."
        "Together they pull me down onto the bed, clambering all over me."
        camila.say "Hah!"
        camila.say "Who needs handcuffs?"
        lexi.say "Yeah, we can handle this guy ourselves!"
        "Okay, now I'm starting to wonder what I was actually afraid of."
        "After all, who wouldn't want to be manhandled by two beautiful women?"
        "Especially when you know just what they have in mind too!"
        "So I just decide to lie back and let them have their way with me."
        "This seems to do the trick for a short while."
        "I have the pleasure of their hands and lips all over my body."
        "But pretty soon I get the feeling that it's not going to be enough."
        "It's clear that Camila and Lexi are waiting for me to do something."
        "They're waiting for me to make a choice as to where this thing is going."
        "So it looks like I'm going to have to leap one way or the other."
    else:
        "My date with Camila and Lexi just came to a natural end."
        "But none of us seem ready to actually call it a night just yet."
        "Which is why I asked both of them back to my place."
        "And much to my delight, the answer was yes from the girls."
        scene bg livingroom with fade
        "As we're walking into the house on to my bedroom, I can't help chuckling."
        $ game.room = "bedroom1"
        scene bg bedroom1 with fade
        show camila date zorder 1 at left5
        show lexi date nophone annoyed zorder 2 at right5
        with easeinright
        lexi.say "Hey, [hero.name]!"
        lexi.say "What's so damn funny, huh?"
        show camila date annoyed
        camila.say "Yeah, [hero.name]..."
        camila.say "Are we amusing you or something?"
        "I hold my hands up in surrender as I walk through the door."
        "Shaking my head in the hope of defusing the situation."
        mike.say "Guys, guys..."
        mike.say "Chill out, okay?"
        mike.say "I was just laughing at you two."
        mike.say "You've been chatting away like old buddies all night!"
        show lexi angry
        "Lexi puts her hands on her hips and glares at me."
        show camila angry
        "Camila crosses her arms over her chest and does the same."
        camila.say "And just what's wrong with that?"
        lexi.say "Yeah, what's wrong with it?"
        lexi.say "You're always nagging us to get along better."
        camila.say "Sheesh - you got that right, Lexi!"
        camila.say "Nagging like an old woman!"
        mike.say "No, no, no..."
        mike.say "You're taking it the wrong way."
        mike.say "I think it's great you're getting along."
        mike.say "It's just hard to believe it's actually happening, that's all!"
        show camila flirt
        show lexi flirt
        "Camila and Lexi exchange a knowing glance."
        "Then, as one, they nod."
        "And it's one of those moments when it sucks to be a guy."
        "Because I get the feeling any woman alive would have read its meaning."
        "But as a man, I'm left clueless as to what just passed between them."
        show lexi at center, zoomAt(1.5, (440, 1040))
        show camila at center, zoomAt(1.5, (840, 1040))
        with fade
        "The girls advance on me, Camila to my left and Lexi to my right."
        "Instinctively I back away from them."
        "But I don't see the bed as it comes up behind me."
        mike.say "Whoa..."
        with vpunch
        "I topple over backwards, landing hard on the mattress."
        "And that's the moment that Camila and Lexi pounce."
        "Camila pins me to the mattress, keeping me from moving."
        "She must be using some kind of restraining technique too."
        "Because I can't shake her off or get up from the bed!"
        "This leaves Lexi free to begin stripping off my clothes."
        "And she does that with ruthless efficiency."
        "Everything I have on is torn off and thrown aside."
        "So that in less than a minute, I'm totally naked!"
        mike.say "What..."
        mike.say "What are you doing?!?"
        camila.say "We're showing you how well we can work together, [hero.name]."
        lexi.say "Isn't that what you wanted, huh?"
        "I watch in stunned silence as Camila and Lexi release me."
        "Then they start to take off their own clothes in front of me too!"
        "Instead of getting up, I just lie back and watch the show."
        "Because I'm beginning to think this might not be so bad after all."
        "I mean, why am I even bothering to struggle?"
        "The fact that I've stopped resisting seems to affect the girls too."
        "They slow things down a little and start to put on a show for me."
        "And I can see that they're enjoying the chance to have my eyes on them."
        show camila naked
        show lexi naked
        with dissolve
        "Soon enough, Camila and Lexi are both naked."
        "One stands on either side of the bed, looking down at me."
        "My eyes keep darting between them."
        "I'm waiting with baited breath to see what happens next."
        "Still keeping it slow, they crawl onto the bed."
        "All the time their eyes are fixed on my groin."
        "My own eyes are still looking from one side to the other."
        "But I keep catching passing glimpses of my cock too."
        "It's getting harder by the second as they inch towards it."
        "And by the time they reach their destination, it's standing upright."
        "Camila and Lexi get to work then, not speaking a single word."
        "They seem to know on instinct what the other is going to do."
    call criminal_harem_blowjob from _call_criminal_harem_blowjob
    call camila_lexi_threesome_fuck from _call_camila_lexi_threesome_fuck_1
    return

label criminal_harem_blowjob:
    "So they twist in and out, then around each other without a problem."
    "This means that all I have to do is lie there and surrender myself."
    scene bg black
    show criminal harem bj bedroom1 naked
    with fade
    "Lexi begins to work the shaft and Camila my balls."
    "It starts out with fingers, caressing and squeezing."
    show sexinserts head lexi zorder 1 at center, zoomAt(1, (-120, 810))
    show sexinserts head camila as extrabj zorder 2 at center, zoomAt(1, (720, 810))
    "Then they slowly start to make use of their lips."
    "Feather-light kisses turn into longer, lingering passes."
    show criminal harem bj lexlick lexdown
    pause 0.1
    show criminal harem bj lexhalfdown
    pause 0.1
    show criminal harem bj lexmid
    pause 0.1
    show criminal harem bj lexup
    pause 0.2
    show criminal harem bj lexlick lexdown
    pause 0.1
    show criminal harem bj lexhalfdown
    pause 0.1
    show criminal harem bj lexmid
    pause 0.1
    show criminal harem bj lexup
    "Tongues emerge from these next, teasing at what might be ahead."
    show criminal harem bj camlick camdown lexnormal
    pause 0.1
    show criminal harem bj camhalfdown
    pause 0.1
    show criminal harem bj cammid
    pause 0.1
    show criminal harem bj camup
    pause 0.2
    show criminal harem bj camlick camdown
    pause 0.1
    show criminal harem bj camhalfdown
    pause 0.1
    show criminal harem bj cammid
    pause 0.1
    show criminal harem bj camup
    "But as soon as the tongues become a part of this, so do the teeth!"
    "Camila and Lexi are switching places the whole time too."
    "So I can never be sure who's doing what to me from one moment to the next."
    show criminal harem bj lexsuck camnormal
    "All the same, I swear it's Lexi that takes it all the way in first."
    "Her eyes closed, Lexi's head bobs up and down."
    "And the sensation is the best thing they've done to me yet."
    show criminal harem bj lexlick lexdown
    pause 0.1
    show criminal harem bj lexhalfdown
    pause 0.1
    show criminal harem bj lexmid
    pause 0.1
    show criminal harem bj lexup
    "She doesn't linger over it too long though."
    show criminal harem bj camsuck lexnormal
    "Instead she releases me and lets Camila take over."
    "And the effort that she puts in seems to be better still."
    "It doesn't take genius to figure out that they're trying to outdo each other."
    "Sure, Camila and Lexi have put their former differences behind them."
    show criminal harem bj camlick camdown
    pause 0.1
    show criminal harem bj camhalfdown
    pause 0.1
    show criminal harem bj cammid
    pause 0.1
    show criminal harem bj camup
    "But this is a more friendly kind of competition, a rivalry if you will."
    show criminal harem bj lexsuck
    "They trade places working the head of my cock."
    "And the one that's really reaping the rewards is me!"
    show criminal harem bj camsuck lexnormal
    "Because this thing just keeps on getting better and better!"
    "The only problem is that it's now that much more intense too."
    show criminal harem bj lexsuck camnormal
    "So pretty soon the inevitable happens."
    mike.say "Urgh..."
    show criminal harem bj camlick camdown lexnormal
    pause 0.1
    show criminal harem bj camhalfdown lexlick lexdown
    pause 0.1
    show criminal harem bj cammid lexhalfdown
    pause 0.1
    show criminal harem bj camup lexmid
    pause 0.1
    show criminal harem bj lexup
    mike.say "Camila..."
    show criminal harem bj camlick camdown lexnormal
    pause 0.1
    show criminal harem bj camhalfdown lexlick lexdown
    pause 0.1
    show criminal harem bj cammid lexhalfdown
    pause 0.1
    show criminal harem bj camup lexmid
    pause 0.1
    show criminal harem bj lexup
    mike.say "Lexi..."
    show criminal harem bj camlick camdown lexnormal
    pause 0.1
    show criminal harem bj camhalfdown lexlick lexdown
    pause 0.1
    show criminal harem bj cammid lexhalfdown
    pause 0.1
    show criminal harem bj camup lexmid
    pause 0.1
    show criminal harem bj lexup
    mike.say "I'm going to...to cum!"
    menu:
        "Cum in Camila's mouth":
            "I honestly think this is going to end in perfect harmony."
            show criminal harem bj lexnormal camnormal
            "But at the last moment, Camila elbows Lexi out of the way."
            "Then she pounces on my cock, hungrily swallowing it."
            show sexinserts head camila cum as extrabj zorder 2 at center, zoomAt(1, (720, 810))
            show criminal harem bj camsuck
            with vpunch
            "This means that I shoot my load into her mouth."
            show criminal harem bj cum with vpunch
            "And Camila swallows it without hesitation."
            with vpunch
            lexi.say "Hey!"
            lexi.say "No fair!"
            lexi.say "What happened to working together?!?"
            "But neither of us can answer the question."
            "As I'm totally out of it."
            "And Camila has her mouth full."
            $ camila.love += 3
        "Cum in Lexi's mouth":
            "I honestly think this is going to end in perfect harmony."
            show criminal harem bj camnormal lexnormal
            "But at the last moment, Lexi elbows Camila out of the way."
            "Then she pounces on my cock, hungrily swallowing it."
            show criminal harem bj lexsuck
            show sexinserts head lexi cum zorder 1 at center, zoomAt(1, (-120, 810))
            with vpunch
            "This means that I shoot my load into her mouth."
            show criminal harem bj cum with vpunch
            "And Lexi swallows it without hesitation."
            with vpunch
            camila.say "Hey!"
            camila.say "Thanks a bunch, Lexi!"
            camila.say "Way to go into business for yourself!"
            "But neither of us can answer the question."
            "As I'm totally out of it."
            "And Lexi has her mouth full."
            $ lexi.love += 3
        "Cum on their faces":
            "Still working together in perfect harmony, Camila and Lexi stop what they're doing."
            "Then they wait patiently, staring at my cock as if hypnotised by the sight of it."
            show sexinserts head lexi cum zorder 1 at center, zoomAt(1, (-120, 810))
            show sexinserts head camila cum as extrabj zorder 2 at center, zoomAt(1, (720, 810))
            show criminal harem bj lexnormal camnormal cum
            with vpunch
            "And when I shoot my load, they take it straight in the face without flinching."
            with vpunch
            "Cum spatters across their features, landing in sticky lines."
            "Then it starts to run down their cheeks and over their lips."
            show criminal harem bj facecum dickcum -cum with vpunch
            "Camila and Lexi lap it up, swallowing as much as they possibly can."
            "But all I can do is lie back and watch, panting from sheer exhaustion."
            $ camila.love += 2
            $ lexi.love += 2
    hide sexinserts
    hide extrabj
    return

label camila_lexi_threesome_fuck:
    menu:
        "Fuck Camila":
            "I don't know what it is that makes up my mind in the end."
            "But without as much as a conscious thought, I find myself reaching out."
            "And there's no confusing the fact that it's Camila I'm making a grab for."
            "Of course, she offers up no resistance, smiling as my hands seize her."
            "And it's a relief to see that Lexi seems to take my choice in her stride too."
            "Rather than being jealous, the other girl seems interested so see where this is going."
            "With Camila's back against my chest, I guide her to the exact spot where I want her."
            "Which is straddling my thighs backwards as I lie down on the bed."
            "At first, Camila looks back over her shoulder at me."
            scene criminal harem threesome camilafuck with fade
            "And I can see that there's confusion on her face."
            "Like she wonders why I've turned her away from me."
            "I can tell you that it's not from a desire to miss out on her stunning features."
            "But the actual reason become apparent to Camila a moment later."
            "Precisely when she turns her head back to see where Lexi's gotten to."
            "If anything, Camila looks even more surprised when their lips meet."
            "Lexi's kneeling right in front of Camila, just waiting for her chance!"
            "It only takes a moment for Camila to surrender to Lexi's attentions."
            "And I get to watch as they start to make out in front of me."
            "As Camila's attention seems to be elsewhere, I decide to take the initiative."
            "I'm sure she won't mind if I get things started!"
            menu:
                "Fuck her pussy":
                    "I can't be sure that Camila's even aware of what I'm doing."
                    "But that doesn't stop me from aiming for what's between her thighs."
                    "I can practically smell her pussy from here, and that's my intended target."
                    $ CONDOM = False
                    if not (camila.flags.pregnant or camila.flags.pill or camila.flags.pregrequest):
                        menu:
                            "Use protection" if hero.has_condom():
                                $ CONDOM = hero.use_condom()
                                "But in that same moment I remember something important."
                                mike.say "Whoa..."
                                mike.say "We need to use a condom!"
                                "The sound of my voice is enough to get Camila's attention."
                                "She breaks away from Lexi and looks back over her shoulder."
                                camila.say "You bet we should!"
                                camila.say "Is that one right there?"
                                "I nod as Camila reaches over to the bedside table."
                                "Mere moments later she has the condom out of the packet."
                                "And a few seconds after that it's on my cock."
                                "So now we really are ready to go."
                            "Do not use protection":
                                if camila.force_condom_use(love=160, drinks=1, sub=None):
                                    "Suddenly Camila pulls away from Lexi."
                                    "Then she looks back over her shoulder at me."
                                    camila.say "Wait a minute..."
                                    camila.say "We need to use a condom!"
                                    if camila.love >= 160 - int(160 * .15):
                                        camila.say "And I have one right here..."
                                        "I nod as Camila reaches over to where she has the protection stashed."
                                        "Mere moments later she has the condom out of the packet."
                                        "And a few seconds after that it's on my cock."
                                        "So now we really are ready to go."
                                        $ CONDOM = True
                                    else:
                                        mike.say "Come on, Camila."
                                        mike.say "Let's just get on with it already!"
                                        mike.say "Forget about the condom, okay?"
                                        "Camila shakes her head as she climbs off me and then off the bed."
                                        "And much to my dismay, Lexi follows her example a moment later."
                                        camila.say "Come on, Lexi..."
                                        camila.say "That's our cue to get out of here."
                                        lexi.say "Yeah, Camila..."
                                        lexi.say "Maybe we can still find a real man to have some fun with."
                                        mike.say "Girls, please!"
                                        mike.say "This is all just a misunderstanding."
                                        mike.say "Can't we talk about it?"
                                        "But no matter what I say, it doesn't change their minds."
                                        "As soon as they're dressed, Camila and Lexi walk out."
                                        "Which leaves me alone and very much unfulfilled."
                                        hide criminal harem threesome camilafuck
                                        return "leave_without_gain"
                    if CONDOM:
                        show criminal harem threesome camilafuck condom
                    "Using both hands, I raise Camila up until she's in just the right position."
                    "I know that it's the right position because I can feel the lips of her pussy."
                    "They're getting slicker by the second as they rub against the head of my cock."
                    "Camila lets out a moan, even as Lexi keeps on kissing her with the same level of passion."
                    "And I can see that she's nodding eagerly, urging me to keep on going."
                    "Spurred on by this, I begin to pull her downwards with more force than before."
                    "At first there's resistance strong enough to keep her right where she is."
                    "But with each second that passes, I can feel it beginning to ebb away."
                    "For her own part, Camila writhes and wriggles in my grasp."
                    "And I can tell from her movements that she's not trying to escape."
                    "But rather she's doing all she can to speed up the process."
                    show criminal harem threesome camilafuck vaginal up
                    "Her efforts seem to be having an effect too."
                    "Soon I feel the last resistance fade to nothing."
                    "Once it's gone, Camila doesn't sink down as slowly as before."
                    "Instead she drops almost onto my lap on one smooth movement."
                    "One moment I can feel the head of my cock sinking into her."
                    "And the next I'm as far into her as I can possibly get."
                    show criminal harem threesome camilafuck camilaclose
                    "Camila sits there for a few seconds, as if savouring the sensation."
                    "Then she begins to ride my cock for all she's worth."
                    show criminal harem threesome camilafuck camilaopen
                    "My hands are still holding onto her haunches, sinking into her skin."
                    "And I do all that I can to add to the motion that's passing between us."
                    "But pretty soon it becomes apparent to me that I'm just whistling into the wind."
                    "Camila's the one that's riding me, harder and faster all the time."
                    "I might as well accept that fact and just enjoy the experience!"
                    "Well, that and the pretty spectacular show Camila and Lexi are putting on for me too."
                    show criminal harem threesome camilafuck camilaclose
                    "Because all the while that I've been fucking the former, the latter's been playing with her."
                    "Lexi's hands are all over Camila, exploring every inch of her body that they can reach."
                    "And I can only imagine how much that attention is heightening the experience for her."
                    "It's certainly enough to make me stare and struggle to get a better view of the action."
                    show criminal harem threesome camilafuck speed with vpunch
                    "Suddenly all of my efforts are interrupted by a change in what I'm feeling."
                    show criminal harem threesome camilafuck speed at startle(0.05,-10)
                    "Camila doesn't stop or even slow down for a second."
                    show criminal harem threesome camilafuck speed at startle(0.05,-10)
                    "But the grip that she has on me intensifies greatly."
                    show criminal harem threesome camilafuck speed at startle(0.05,-10)
                    "She's squeezing me so hard that I think I'm going to pass out!"
                    show criminal harem threesome camilafuck speed at startle(0.05,-10)
                    "But somehow I manage to keep a clear head."
                    show criminal harem threesome camilafuck speed at startle(0.05,-10)
                    "Which is what lets me figure out that she must be cumming."
                    show criminal harem threesome camilafuck up camilaopen at startle(0.05,-10)
                    call cum_reaction (camila, 'vaginal', 0) from _call_cum_reaction_209
                    if _return == "vaginal_outside":
                        "Camila seems too caught up in the moment to be able to take charge."
                        "So it's lucky for the both of us that I'm able to do so myself."
                        "At what feels like the last possible moment, I pull out."
                        show criminal harem threesome camilafuck -vaginal
                        "Camila breaks off her kiss with Lexi as my cock pops out of her."
                        show criminal harem threesome camilafuck up cumshot with vpunch
                        "The both of us climaxing at the same time and with dramatic effect too."
                        $ camila.sub += 1
                    elif _return == "vaginal_condom":
                        "Luckily for me, we remembered to use a condom."
                        "So there's no problem when Camila begins to make me cum too."
                        "All I need to do is hold on a little tighter and let it happen."
                        with vpunch
                        "Camila breaks off her kiss with Lexi as I lose it inside of her."
                        with vpunch
                        "The both of us climaxing at the same time and with dramatic effect too."
                        $ camila.love += 1
                    elif _return == "vaginal_inside_pill":
                        "Luckily for me, I know that Camila's on the pill."
                        show criminal harem threesome camilafuck down
                        "So there's no problem when she begins to make me cum too."
                        "All I need to do is hold on a little tighter and let it happen."
                        with vpunch
                        "Camila breaks off her kiss with Lexi as I lose it inside of her."
                        show criminal harem threesome camilafuck creampie with vpunch
                        "The both of us climaxing at the same time and with dramatic effect too."
                        $ camila.love += 1
                    elif _return == "vaginal_inside_pregnant":
                        "Luckily for me, Camila's already pregnant."
                        show criminal harem threesome camilafuck down
                        "So there's no problem when she begins to make me cum too."
                        "All I need to do is hold on a little tighter and let it happen."
                        with vpunch
                        "Camila breaks off her kiss with Lexi as I lose it inside of her."
                        show criminal harem threesome camilafuck creampie with vpunch
                        "The both of us climaxing at the same time and with dramatic effect too."
                        $ camila.love += 1
                    elif _return == "vaginal_inside_mad":
                        lexi.say "[hero.name]!"
                        show criminal harem threesome camilafuck down
                        lexi.say "What are you doing?!?"
                        lexi.say "You have to pull out - now!"
                        "Lexi's words come too late to snap me out of it."
                        with vpunch
                        "Which means that I realise what's happening as I shoot my load into Camila."
                        show criminal harem threesome camilafuck creampie with vpunch
                        $ camila.impregnate()
                        "She gasps and looks over her shoulder at me, a look of shock on her face."
                        "But there's nothing either of us can do to change what just happened."
                        $ camila.love -= 5
                    elif _return == "vaginal_inside_happy":
                        lexi.say "[hero.name]!"
                        show criminal harem threesome camilafuck down
                        lexi.say "What are you doing?!?"
                        lexi.say "You have to pull out - now!"
                        camila.say "Oh no..."
                        camila.say "Don't you dare!"
                        "Lexi's words come too late to snap me out of it."
                        with vpunch
                        "Which means that I realise what's happening as I shoot my load into Camila."
                        show criminal harem threesome camilafuck creampie with vpunch
                        $ camila.impregnate()
                        "She gasps and looks over her shoulder at me, a look of triumph on her face."
                        "I have no idea why she's looking at me like that."
                        "Like this is what she wanted to happen all along!"
                        $ camila.love += 5
                "Fuck her ass" if hero.sexperience >= 5:
                    "I can't be sure that Camila's even aware of what I'm doing."
                    "But that doesn't stop me from aiming for what's between her buttocks."
                    "I can imagine the feel of her ass already, and that's my intended target."
                    "Using both hands, I raise Camila up until she's in just the right position."
                    "I know that it's the right position because I can feel the entrance to her ass."
                    "It's getting wider by the moment as it rubs against the head of my cock."
                    "Camila lets out a moan, even as Lexi keeps on kissing her with the same level of passion."
                    "And I can see that she's nodding eagerly, urging me to keep on going."
                    "Spurred on by this, I begin to pull her downwards with more force than before."
                    "At first there's resistance strong enough to keep her right where she is."
                    "But with each second that passes, I can feel it beginning to ebb away."
                    "For her own part, Camila writhes and wriggles in my grasp."
                    "And I can tell from her movements that she's not trying to escape."
                    "But rather she's doing all she can to speed up the process."
                    show criminal harem threesome camilafuck anal
                    "Her efforts seem to be having an effect too."
                    "Soon I feel the last resistance fade to nothing."
                    "Once it's gone, Camila doesn't sink down as slowly as before."
                    "Instead she drops almost onto my lap on one smooth movement."
                    "One moment I can feel the head of my cock sinking into her."
                    "And the next I'm as far into her as I can possibly get."
                    show criminal harem threesome camilafuck camilaclose
                    "Camila sits there for a few seconds, as if savouring the sensation."
                    "Then she begins to ride my cock for all she's worth."
                    show criminal harem threesome camilafuck camilaopen
                    "My hands are still holding onto her haunches, sinking into her skin."
                    "And I do all that I can to add to the motion that's passing between us."
                    "But pretty soon it becomes apparent to me that I'm just whistling into the wind."
                    "Camila's the one that's riding me, harder and faster all the time."
                    "I might as well accept that fact and just enjoy the experience!"
                    "Well, that and the pretty spectacular show Camila and Lexi are putting on for me too."
                    show criminal harem threesome camilafuck camilaclose
                    "Because all the while that I've been fucking the former, the latter's been playing with her."
                    "Lexi's hands are all over Camila, exploring every inch of her body that they can reach."
                    "And I can only imagine how much that attention is heightening the experience for her."
                    "It's certainly enough to make me stare and struggle to get a better view of the action."
                    show criminal harem threesome camilafuck speed with vpunch
                    "Suddenly all of my efforts are interrupted by a change in what I'm feeling."
                    show criminal harem threesome camilafuck speed at startle(0.05,-10)
                    "Camila doesn't stop or even slow down for a second."
                    show criminal harem threesome camilafuck speed at startle(0.05,-10)
                    "But the grip that she has on me intensifies greatly."
                    show criminal harem threesome camilafuck speed at startle(0.05,-10)
                    "She's squeezing me so hard that I think I'm going to pass out!"
                    show criminal harem threesome camilafuck speed at startle(0.05,-10)
                    "But somehow I manage to keep a clear head."
                    show criminal harem threesome camilafuck speed at startle(0.05,-10)
                    "Which is what lets me figure out that she must be cumming."
                    show criminal harem threesome camilafuck camilaopen at startle(0.05,-10)
                    call cum_reaction (camila, 'anal', 0) from _call_cum_reaction_210
                    if _return == 'anal_inside':
                        "Luckily for me, I chose to use the back door tonight."
                        "So there's no problem when Camila begins to make me cum too."
                        "All I need to do is hold on a little tighter and let it happen."
                        with vpunch
                        "Camila breaks off her kiss with Lexi as I lose it inside of her."
                        show criminal harem threesome camilafuck creampie with vpunch
                        "The both of us climaxing at the same time and with dramatic effect too."
                        $ camila.love += 2
                    elif _return == 'anal_outside':
                        "Camila seems too caught up in the moment to be able to take charge."
                        "So it's lucky for the both of us that I'm able to do so myself."
                        show criminal harem threesome camilafuck -anal
                        "At what feels like the last possible moment, I pull out."
                        show criminal harem threesome camilafuck cumshot with vpunch
                        "Camila breaks off her kiss with Lexi as my cock pops out of her."
                        $ camila.sub += 2
                    $ camila.flags.anal += 1
        "Fuck Lexi":
            "There's no conscious choice involved in my decision."
            "I don't even stop to think about what I'm doing."
            "Instead I find myself reaching out and taking Lexi into my arms."
            "Much to my relief, she responds instantly, eager to come to me."
            "And maybe even more of a relief is the fact that Camila doesn't protest."
            "As Lexi crawls atop me, the other girl just sits back and watches."
            scene criminal harem threesome lexifuck with fade
            "All of my attention should be on Lexi right now."
            "I can feel the entire length of her body as she spreads herself over me."
            "Breasts, belly and thighs, all of them are there to be savoured."
            "But somehow my eye keeps being drawn to Camila as she watches in silence."
            "That is until I feel the sting of something striking my cheek."
            "I look up in surprise to see Lexi waving a hand in my face."
            "The same hand that she just used to slap me!"
            lexi.say "Don't look at her..."
            lexi.say "Look at me!"
            lexi.say "I'm the one you're supposed to be fucking!"
            "I can tell from the tone of Lexi's voice that she's amused, rather than mad."
            "But I make a point of nodding all the same."
            "And as I reach up to take hold of her, I can hear Camila chuckling too."
            "Because now I have no excuse but to devote all of my attention to Lexi."
            "Which means that she's free to do exactly as she pleases."
            menu:
                "Fuck her pussy":
                    "I push Lexi gently upwards, and she seems to take the hint."
                    "Sitting up she straddles my thighs and leans backwards."
                    "This let's her see my cock standing up before her."
                    "And the smile that spreads across her face is as wide as it could be."
                    lexi.say "Oh..."
                    lexi.say "Is all of that for me?"
                    mike.say "It is, Lexi..."
                    mike.say "If you think you can handle it?"
                    $ CONDOM = False
                    if not (lexi.flags.pregnant or lexi.flags.pill or lexi.flags.pregrequest):
                        menu:
                            "Use protection" if hero.has_condom():
                                $ CONDOM = hero.use_condom()
                                "Before Lexi can answer, a thought occurs to me."
                                mike.say "Wait a minute..."
                                mike.say "We really should use some protection."
                                "Lexi looks surprised for a moment."
                                "But then she seems to realise what I just said."
                                "And she nods in agreement."
                                lexi.say "I guess you're right, [hero.name]."
                                lexi.say "You've got one around here, right?"
                                mike.say "On the bedside table."
                                camila.say "I'm already on it!"
                                "Camila grabs a condom and tears open the packet."
                                "And between the two of them, they have it on in a matter of seconds."
                                "Which means that we're ready to go."
                            "Do not use protection":
                                if lexi.force_condom_use(love=180, drinks=1, sub=None):
                                    "Before I can make another move, Lexi holds up a hand."
                                    lexi.say "Whoa!"
                                    lexi.say "What about a condom?"
                                    if lexi.love >= 180 - int(180 * .15):
                                        lexi.say "Don't worry, [hero.name]..."
                                        lexi.say "I got one in my pocket."
                                        lexi.say "Right over there..."
                                        camila.say "I'm already on it!"
                                        "Camila grabs a condom and tears open the packet."
                                        "And between the two of them, they have it on in a matter of seconds."
                                        "Which means that we're ready to go."
                                        $ CONDOM = True
                                    else:
                                        mike.say "Come on, Lexi."
                                        mike.say "Let's just get on with it already!"
                                        mike.say "Forget about the condom, okay?"
                                        "Lexi shakes her head as she climbs off me and then off the bed."
                                        "And much to my dismay, Camila follows her example a moment later."
                                        camila.say "Come on, Lexi..."
                                        camila.say "That's our cue to get out of here."
                                        lexi.say "Yeah, Camila..."
                                        lexi.say "Maybe we can still find a real man to have some fun with."
                                        mike.say "Girls, please!"
                                        mike.say "This is all just a misunderstanding."
                                        mike.say "Can't we talk about it?"
                                        "But no matter what I say, it doesn't change their minds."
                                        "As soon as they're dressed, Camila and Lexi walk out."
                                        "Which leaves me alone and very much unfulfilled."
                                        hide criminal harem threesome lexifuck
                                        return "leave_without_gain"
                    if CONDOM:
                        show criminal harem threesome lexifuck condom
                    "Lexi reaches out and takes hold of my cock a moment later."
                    "And when I say that, I mean she actually grabs it and squeezes!"
                    "Not hard enough to make me cry out in pain."
                    "But definitely hard enough to make sure she has my undivided attention."
                    "Then the begins to move up and down, rubbing it against the lips of her pussy."
                    "She's smiling the whole time, that knowing smile that always turns me on."
                    "I'm so busy staring at Lexi's face that I don't notice what's happening elsewhere."
                    "So it comes as a surprise to feel Lexi's body surrendering to me."
                    show criminal harem threesome lexifuck vaginal
                    "But what I can see is the expression on her face as it's happening."
                    "I watch as Lexi's smile is replaced by a look of helpless pleasure."
                    show criminal harem threesome lexifuck pleasure
                    "Her eyes lose their focus and she seems to be staring into space."
                    "At the same time she leans backwards, resting on her haunches."
                    "The unconscious nature of what's happening between us continues as I begin to move."
                    "Without needing to be told, I start to thrust in and out of Lexi."
                    "The effect this has on her is instantly visible."
                    "Now her eyes seem to totally glaze over."
                    "And the only sound coming from her is a helpless moan."
                    "That's the exact moment Camila chooses to make her move."
                    "With Lexi helpless and totally tied up, she can do as she likes."
                    "And what Camila chooses to do is lie down atop me."
                    "Lexi might be taking up the room below my waist."
                    "But that doesn't stop Camila from draping her torso over mine."
                    "Her belly is laid atop my stomach, her breasts on my chest."
                    "And when my lips are within reach, she kisses me with genuine passion."
                    show criminal harem threesome lexifuck speed with vpunch
                    "Just like it was with Lexi, my hands move without a conscious thought."
                    show criminal harem threesome lexifuck speed at startle(0.05,-10)
                    "They explore every inch of Camila's body that they can reach."
                    show criminal harem threesome lexifuck speed at startle(0.05,-10)
                    "But they linger longest over the soft curves of her ass."
                    show criminal harem threesome lexifuck speed at startle(0.05,-10)
                    "And they spend maybe even a little more time massaging her breasts."
                    show criminal harem threesome lexifuck speed at startle(0.05,-10)
                    "We're all in this thing together, of course."
                    show criminal harem threesome lexifuck speed at startle(0.05,-10)
                    "But what Camila and I are doing right now still feels exciting."
                    show criminal harem threesome lexifuck speed at startle(0.05,-10)
                    "Almost like we're doing it while Lexi's looking the other way."
                    show criminal harem threesome lexifuck speed at startle(0.05,-10)
                    "The combination of the excitement and the pleasure is a heady cocktail."
                    show criminal harem threesome lexifuck speed at startle(0.05,-10)
                    "And I suddenly realise that I'm not going to be able to hold on much longer!"
                    if game.days_played % 4 == 0 and not CONDOM:
                        call criminal_harem_threesome_facial_ending from _call_criminal_harem_threesome_facial_ending
                    else:
                        call cum_reaction (lexi, 'vaginal', 0) from _call_cum_reaction_211
                        if _return == "vaginal_outside":
                            "I remember in good time that we didn't bother with a condom."
                            "So I make a point of pulling out before it's too late."
                            show criminal harem threesome lexifuck -vaginal
                            "That means I can keep right on kissing and caressing Camila the whole time it's happening."
                            show criminal harem threesome lexifuck cumshot with vpunch
                            "And that's just what I do, enjoying the sensation of release."
                            with vpunch
                            "From the sounds that she's making, my guess is that Lexi's cumming too."
                            with vpunch
                            "But my senses are filled with the sounds of Camila as she moans with pleasure."
                            $ lexi.sub += 1
                        elif _return == "vaginal_condom":
                            "The fact we remembered to use a condom means there nothing to worry about."
                            "I can keep right on kissing and caressing Camila the whole time it's happening."
                            with vpunch
                            "And that's just what I do, enjoying the sensation of what they're both doing to me."
                            with vpunch
                            "From the sounds that she's making, my guess is that Lexi's cumming too."
                            with vpunch
                            "But my senses are filled with the sounds of Camila as she moans with pleasure."
                            $ lexi.love += 1
                        elif _return == "vaginal_inside_pill":
                            "Camila breaks away from the kiss for a moment."
                            camila.say "What are you waiting for?"
                            camila.say "She's on the pill!"
                            "Camila's right, I can keep on going without having to worry about the consequences."
                            with vpunch
                            "And that's just what I do, enjoying the sensation of what they're both doing to me."
                            show criminal harem threesome lexifuck creampie with vpunch
                            "From the sounds that she's making, my guess is that Lexi's cumming too."
                            with vpunch
                            "But my senses are filled with the sounds of Camila as she moans with pleasure."
                            $ lexi.love += 1
                        elif _return == "vaginal_inside_pregnant":
                            "Camila breaks away from the kiss for a moment."
                            camila.say "What are you waiting for?"
                            camila.say "You already got her pregnant!"
                            "Camila's right, I can keep on going without having to worry about the consequences."
                            with vpunch
                            "And that's just what I do, enjoying the sensation of what they're both doing to me."
                            show criminal harem threesome lexifuck creampie with vpunch
                            "From the sounds that she's making, my guess is that Lexi's cumming too."
                            with vpunch
                            "But my senses are filled with the sounds of Camila as she moans with pleasure."
                            $ lexi.love += 1
                        elif _return == "vaginal_inside_mad":
                            "Camila breaks away from the kiss for a moment."
                            camila.say "What are you doing?"
                            camila.say "You need to pull out now!"
                            "Camila's right, but her warning catches me totally off-guard."
                            with vpunch
                            "So there's no way that I can stop myself losing it inside of Lexi."
                            show criminal harem threesome lexifuck creampie with vpunch
                            $ lexi.impregnate()
                            lexi.say "Oh god!"
                            with vpunch
                            lexi.say "What's happening?!?"
                            "There's no way I can answer Lexi."
                            "But I think she already knows the answer."
                            "And nobody seems happy about it either."
                            $ lexi.love -= 5
                        elif _return == "vaginal_inside_happy":
                            "Camila breaks away from the kiss for a moment."
                            camila.say "What are you doing?"
                            camila.say "You need to pull out now!"
                            "I make to do as Camila says, trying to pull out of Lexi."
                            "But then I feel her doing all she can to stop that happening."
                            lexi.say "No..."
                            lexi.say "No way..."
                            lexi.say "You stay right there!"
                            "Lexi's demand catches me totally off-guard."
                            with vpunch
                            "So there's no way that I can stop myself losing it inside of her."
                            show criminal harem threesome lexifuck creampie with vpunch
                            $ lexi.impregnate()
                            "Camila and I are exchanging looks of genuine horror."
                            "But Lexi looks bizarrely pleased with this turn of events."
                            $ lexi.love += 5
                "Fuck her ass" if hero.sexperience >= 5:
                    "I push Lexi gently upwards, and she seems to take the hint."
                    "Sitting up she straddles my thighs and leans backwards."
                    "This let's her see my cock standing up before her."
                    "And the smile that spreads across her face is as wide as it could be."
                    lexi.say "Oh..."
                    lexi.say "Is all of that for me?"
                    mike.say "It is, Lexi..."
                    mike.say "If you think you can handle it?"
                    "Lexi reaches out and takes hold of my cock a moment later."
                    "And when I say that, I mean she actually grabs it and squeezes!"
                    "Not hard enough to make me cry out in pain."
                    "But definitely hard enough to make sure she has my undivided attention."
                    "Then the begins to move up and down, rubbing it between the cheeks of her ass."
                    "She's smiling the whole time, that knowing smile that always turns me on."
                    "I'm so busy staring at Lexi's face that I don't notice what's happening elsewhere."
                    "So it comes as a surprise to feel Lexi's body surrendering to me."
                    show criminal harem threesome lexifuck anal
                    "But what I can see is the expression on her face as it's happening."
                    "I watch as Lexi's smile is replaced by a look of helpless pleasure."
                    show criminal harem threesome lexifuck pleasure
                    "Her eyes lose their focus and she seems to be staring into space."
                    "At the same time she leans backwards, resting on her haunches."
                    "The unconscious nature of what's happening between us continues as I begin to move."
                    "Without needing to be told, I start to thrust in and out of Lexi."
                    "The effect this has on her is instantly visible."
                    "Now her eyes seem to totally glaze over."
                    "And the only sound coming from her is a helpless moan."
                    "That's the exact moment Camila chooses to make her move."
                    "With Lexi helpless and totally tied up, she can do as she likes."
                    "And what Camila chooses to do is lie down atop me."
                    "Lexi might be taking up the room below my waist."
                    "But that doesn't stop Camila from draping her torso over mine."
                    "Her belly is laid atop my stomach, her breasts on my chest."
                    "And when my lips are within reach, she kisses me with genuine passion."
                    show criminal harem threesome lexifuck speed with vpunch
                    "Just like it was with Lexi, my hands move without a conscious thought."
                    show criminal harem threesome lexifuck speed at startle(0.05,-10)
                    "They explore every inch of Camila's body that they can reach."
                    show criminal harem threesome lexifuck speed at startle(0.05,-10)
                    "But they linger longest over the soft curves of her ass."
                    show criminal harem threesome lexifuck speed at startle(0.05,-10)
                    "And they spend maybe even a little more time massaging her breasts."
                    show criminal harem threesome lexifuck speed at startle(0.05,-10)
                    "We're all in this thing together, of course."
                    show criminal harem threesome lexifuck speed at startle(0.05,-10)
                    "But what Camila and I are doing right now still feels exciting."
                    show criminal harem threesome lexifuck speed at startle(0.05,-10)
                    "Almost like we're doing it while Lexi's looking the other way."
                    show criminal harem threesome lexifuck speed at startle(0.05,-10)
                    "The combination of the excitement and the pleasure is a heady cocktail."
                    show criminal harem threesome lexifuck speed at startle(0.05,-10)
                    "And I suddenly realise that I'm not going to be able to hold on much longer!"
                    if game.days_played % 4 == 0:
                        call criminal_harem_threesome_facial_ending from _call_criminal_harem_threesome_facial_ending_1
                    else:
                        call cum_reaction (lexi, 'anal', 0) from _call_cum_reaction_212
                        if _return == 'anal_inside':
                            "The fact that I chose to fuck Lexi's ass means there nothing to worry about."
                            "I can keep right on kissing and caressing Camila the whole time it's happening."
                            with vpunch
                            "And that's just what I do, enjoying the sensation of what they're both doing to me."
                            show criminal harem threesome lexifuck creampie with vpunch
                            "From the sounds that she's making, my guess is that Lexi's cumming too."
                            with vpunch
                            "But my senses are filled with the sounds of Camila as she moans with pleasure."
                            $ lexi.love += 2
                        elif _return == 'anal_outside':
                            "I remember in good time that I wanted to pull out before the end."
                            show criminal harem threesome lexifuck -anal
                            "So I make a point of doing so before it's too late."
                            "That means I can keep right on kissing and caressing Camila the whole time it's happening."
                            show criminal harem threesome lexifuck cumshot with vpunch
                            "And that's just what I do, enjoying the sensation of release."
                            with vpunch
                            "From the sounds that she's making, my guess is that Lexi's cuming too."
                            with vpunch
                            "But my senses are filled with the sounds of Camila as she moans with pleasure."
                            $ lexi.sub += 2
                    $ lexi.flags.anal += 1
    $ lexi.sexperience += 1
    $ camila.sexperience += 1
    if renpy.has_label("criminal_harem_achievement_2") and not game.flags.cheat:
        call criminal_harem_achievement_2 from _call_criminal_harem_achievement_2
    return

label criminal_harem_threesome_facial_ending:
    "I'm ready to let it go and shoot my load."
    "In fact I'm expecting it to happen any moment now."
    "But all of a sudden, Camila and Lexi decide to change things up."
    "Both of them slide off of me, meaning my cock is free a second later."
    "And even as I sit up and start to ask what's happening, they're already a step ahead of me."
    show criminal harem bj with fade
    "Lowering their heads towards my groin, I can see what they have in mind."
    show sexinserts head lexi zorder 1 at center, zoomAt(1, (-120, 810))
    show sexinserts head camila as extrabj zorder 2 at center, zoomAt(1, (720, 810))
    "So I just sit back and let them have their way with me."
    show criminal harem bj camsuck lexlick
    "Camila is the first one to take the head of my cock into her mouth."
    "And as she does so, Lexi turns her attention to my balls."
    "Without a word spoken between them, they somehow work in perfect harmony."
    "The sensations that I'm feeling are enough to almost overwhelm me."
    "So I take the chance to close my eyes and simply enjoy the moment."
    "But as soon as I open them again, I blink in surprise."
    show criminal harem bj lexsuck camlick
    "Now Lexi's the one with my cock in her mouth."
    "And Camila's the one working on my balls!"
    "Somehow they managed to swap places without me noticing."
    "I don't know if it's the surprise that does it."
    "Or else the simple fact that they're doing such a good job."
    "Either way, I can feel myself starting to cum again."
    show criminal harem bj lexlick camlick
    "And this time I know it's going to be for real!"
    menu:
        "Cum in Camila's mouth":
            "That's why I do the best I can to wait until the right moment."
            show criminal harem bj lexnormal
            "And let go as soon as my cock is firmly in Camila's mouth."
            show criminal harem bj camsuck
            "She seems surprised to be thrust into the position of swallowing."
            show sexinserts head camila cum as extrabj zorder 2 at center, zoomAt(1, (720, 810))
            with vpunch
            "But she recovers just in time to avoid disaster."
            with vpunch
            "Camila takes everything I can throw at her after that."
            show criminal harem bj cum with vpunch
            "Gulping it down without pause or hesitation."
            $ camila.love += 3
        "Cum in Lexi's mouth":
            "That's why I do the best I can to wait until the right moment."
            show criminal harem bj camnormal
            "And let go as soon as my cock is firmly in Lexi's mouth."
            show criminal harem bj lexsuck
            "She seems surprised to be thrust into the position of swallowing."
            show sexinserts head lexi cum zorder 1 at center, zoomAt(1, (-120, 810))
            with vpunch
            "But she recovers just in time to avoid disaster."
            with vpunch
            "Lexi takes everything I can throw at her after that."
            show criminal harem bj cum with vpunch
            "Gulping it down without pause or hesitation."
            $ lexi.love += 3
        "Cum on their faces":
            "That's why I wait to act until the perfect moment."
            "Which is just when my cock is being passed between them."
            "I let go just as that happens, catching them both off-guard."
            "Camila and Lexi are just waiting there, mouths wide open."
            show criminal harem bj lexnormal camnormal cum
            show sexinserts head lexi cum zorder 1 at center, zoomAt(1, (-120, 810))
            show sexinserts head camila cum as extrabj zorder 2 at center, zoomAt(1, (720, 810))
            with vpunch
            "And that means they take everything I have to give, square in the face."
            with vpunch
            "Lines of sticky, white cum spatter from one to the other."
            show criminal harem bj facecum dickcum -cum with vpunch
            "Running down their noses and cheeks, and dripping from their chins."
            $ camila.love += 2
            $ lexi.love += 2
    hide sexinserts
    hide extrabj
    return

label camila_lexi_propose_male:
    "It still feels kind of weird that I'm dating two girls as different as Camila and Lexi."
    "I mean one's a cop and the other's a...well, the kind of person who gets into trouble with cops!"
    "On paper it shouldn't work, Camila and Lexi shouldn't be able to stand each other's company."
    "But somehow it's different when the three of us are all together."
    "I kinda feel like I'm the one that makes the difference somehow."
    "Like the fact they both want to be with me makes them behave themselves."
    "And I've got to say that when they are, Camila and Lexi are a hell of a lot of fun!"
    "In fact, they're the most fun girls I've ever dated."
    "Which is why I feel like I want to make the whole thing official."
    "All I need to do that is a couple of rings and the perfect moment."
    "And when it comes, I get down on one knee and clear my throat..."
    show lexi casual normal b zorder 2 at right4
    show camila casual normal zorder 1 at left4
    mike.say "Ahem..."
    show lexi annoyed b
    lexi.say "I thought you always went down for that one?"
    show camila bored
    camila.say "Not always, Lexi."
    camila.say "There's a couple of loopholes in the law."
    show camila angry
    camila.say "Wait a minute - why am I even telling you that?!?"
    mike.say "I said - AHEM!"
    show camila normal
    show lexi normal
    "Camila and Lexi stop as one."
    "Then they finally look down at me."
    "And for once I have the pleasure of knowing I've left them speechless."
    "So before they can regain their composure, I decide it's time to pop the question."
    mike.say "Camila..."
    mike.say "Lexi..."
    mike.say "Will you marry me?"
    show lexi surprised
    show camila weird
    "Camila's shaking her head like she can't believe what's happening."
    "But Lexi seems more interested in checking out the rings."
    camila.say "Are you serious?"
    lexi.say "Ooh!"
    lexi.say "Those look fancy!"
    lexi.say "Did you get them off of a fence?"
    mike.say "What?!?"
    mike.say "Of course I'm serious!"
    mike.say "And no, I bought them from a jewellery store!"
    mike.say "Am I going to get an answer or what?"
    show camila normal
    show lexi normal
    if camila.love >= 195 and lexi.love >= 195:
        show lexi normal
        show camila normal
        "Camila and Lexi exchange a long and lingering look into each other's eyes."
        "And all the time I'm watching them, I'm expecting them to both say no."
        camila.say "You know what..."
        camila.say "Before we all got together, I'd have said no way."
        camila.say "I'd have said I was married to the force."
        show camila happy
        camila.say "But I dunno...this just feels right."
        lexi.say "Believe me, I never thought I'd get married."
        lexi.say "But then I never thought I'd date a cop either."
        show lexi happy
        lexi.say "So you can count me in!"
        show lexi b at center, zoomAt (1.5, (840, 1040))
        show camila a at center, zoomAt (1.5, (440, 1040))
        "They thrust their hands towards me."
        "And I hurry to slide the rings onto their fingers."
        show lexi b wink
        show camila a flirt
        mike.say "Phew..."
        mike.say "I was so nervous just now."
        mike.say "I was sure it was going to be a no!"
        show camila happy
        camila.say "Hey, when I commit to something, I really commit to it!"
        show lexi happy
        lexi.say "Yeah - what she said!"
        $ camila.set_fiance()
        $ lexi.set_fiance()
    elif camila.love < 195 and lexi.love < 195:
        "Camila and Lexi seem to suddenly snap back to reality."
        "It's like they're only now realising that I've actually proposed."
        "And now they're shaking their heads at me and frowning."
        show camila annoyed
        camila.say "Are you insane, [hero.name]?"
        camila.say "Marry you - maybe."
        show camila angry
        camila.say "Marry a known criminal - no way!"
        show lexi angry
        lexi.say "HEY!"
        show lexi annoyed
        lexi.say "Who are you calling a criminal?"
        show camila bored
        camila.say "Oh please, Lexi."
        camila.say "You have a record a mile long!"
        "I get hastily back to my feet, shoving the rings into my pocket."
        "And all the time I'm trying to make peace between the two of them."
        mike.say "Come on, guys!"
        mike.say "What's with all the fighting?"
        mike.say "Can't we just get on like we normally do?"
        "In the storm of argument that follows, the proposal is soon forgotten."
        "Which is kind of a relief to me, as it seemed to be the cause of the conflict."
        $ camila.love -= 25
        $ camila.sub -= 25
        $ lexi.love -= 25
        $ lexi.sub -= 25
    elif camila.love >= 195 and lexi.love < 195:
        "Camila and Lexi exchange a long and lingering look into each other's eyes."
        "And all the time I'm watching them, I'm expecting them to both say no."
        camila.say "You know what..."
        camila.say "Before we all got together, I'd have said no way."
        camila.say "I'd have said I was married to the force."
        show camila happy
        camila.say "But I dunno...this just feels right."
        camila.say "Even if one of us has got a questionable past!"
        lexi.say "HEY!"
        show lexi angry
        lexi.say "Who are you calling a criminal?"
        camila.say "Oh please, Lexi."
        show camila normal
        camila.say "You have a record a mile long!"
        "I get hastily back to my feet, shoving the rings into my pocket."
        "And all the time I'm trying to make peace between the two of them."
        mike.say "Come on, guys!"
        mike.say "What's with all the fighting?"
        mike.say "Can't we just get on like we normally do?"
        lexi.say "I'm not playing nice with some that talks to me like that!"
        "Lexi turns her back on Camila and I, then she stomps off."
        hide lexi
        show camila happy at center
        with moveoutright
        "Before I can go after her, Camila slips her finger through one of the rings."
        "Which leaves me happy, but still confused as to where we go from here."
        $ camila.set_fiance()
        $ lexi.love -= 25
        $ lexi.sub -= 25
    elif camila.love < 195 and lexi.love >= 195:
        lexi.say "Believe me, I never thought I'd get married."
        lexi.say "But then I never thought I'd date a cop either."
        show lexi happy
        lexi.say "So you can count me in!"
        camila.say "Are you insane, [hero.name]?"
        camila.say "Marry you - maybe."
        show camila angry
        camila.say "Marry a known criminal - no way!"
        lexi.say "HEY!"
        show lexi angry
        lexi.say "Who are you calling a criminal?"
        show camila bored
        camila.say "Oh please, Lexi."
        camila.say "You have a record a mile long!"
        "I get hastily back to my feet, shoving the rings into my pocket."
        "And all the time I'm trying to make peace between the two of them."
        mike.say "Come on, guys!"
        mike.say "What's with all the fighting?"
        mike.say "Can't we just get on like we normally do?"
        show camila angry
        camila.say "Forget it!"
        show camila annoyed
        camila.say "I'm not marrying that felonious slut!"
        "Camila turns her back on Lexi and I, then she stomps off."
        hide camila
        show lexi happy at center
        with moveoutleft
        "Before I can go after her, Lexi slips her finger through one of the rings."
        "Which leaves me happy, but still confused as to where we go from here."
        $ lexi.set_fiance()
        $ camila.love -= 25
        $ camila.sub -= 25
    return

label camila_lexi_male_ending:

    if renpy.has_label("criminal_harem_achievement_3") and not game.flags.cheat:
        call criminal_harem_achievement_3 from _call_criminal_harem_achievement_3
    $ game.hour = 16
    $ game.room = "church"
    scene bg church wedding
    "I always knew that dating two girls as different as Camila and Lexi was going to be a challenge."
    "But they're kind of like flavours that contrast yet somehow go really well together."
    "On the one hand you have the tough, unflinching cop."
    "On the other, the streetwise, edgy bad girl."
    "When it works, Camila straightens Lexi out just enough for it to be fun."
    "And Lexi gets under Camila's skin, making her lighten up in turn."
    "But now I've gone and asked them both to marry me - and they said yes!"
    "So here I am, standing at the altar in a suit, waiting for them to arrive."
    "And I can't help stealing the occasional look over my shoulder at the guests."
    "Sure, all of my own friends and family are there."
    "But what's making me sweat is the distinctly different crowd here for Camila and Lexi."
    "Seriously, on the one side of the chapel we have a bunch of hard-looking cops."
    "All of them seem to have just come off the beat, and could be packing heat."
    "And on the other all I can see are the kind of people I'd cross the street to avoid."
    "I can't see one of Lexi's guests that would look out of place in a police line-up!"
    "What's worse is that both sides of the chapel have realised the same thing too."
    "The cops and the crooks are eyeing each other up across the aisle."
    "And I'm worried that a gun-fight is about to break out back there!"
    "Luckily for me, music fills the chapel a few seconds later."
    "This seems to be enough to distract them all."
    "And I silently thank my brides for choosing that moment to come to my aid."
    "I almost don't hear the sound of the music they chose to come down the aisle to."
    "Because I'm far too busy staring in amazement at my brides to be."
    show camila wedding a happy at left5
    "Camila normally looks tough and uncompromising."
    "But the dress she's in somehow reveals her true beauty."
    "And I don't think I've ever seen her looking so good."
    if camila.is_visibly_pregnant:
        "She's practically glowing too."
        "Holding her swelling belly with pride."
        "Almost like she's challenging anyone to say they have a problem with it."
    show lexi wedding b bubblegum at right5
    "Lexi is a picture in her dress, but still manages to look cocky as ever."
    "Is she...is she...she is!"
    "She's actually chewing gum and blowing bubbles as she walks down the aisle!"
    if lexi.is_visibly_pregnant:
        "She also doesn't seem to be hiding the fact that she's pregnant either."
        "Her dress seems to celebrate the fact, rather than conceal it."
        "And somehow, it just looks right on her!"
    "I turn to face Camila and Lexi as they reach the altar."
    "And I'm about to make a joke when I find myself being interrupted."
    "Priest" "Ahem..."
    "Priest" "Shall we get started?"
    "This seems to be enough to silence all three of us."
    show camila normal
    show lexi normal
    "Camila, Lexi and I all nod and take our places."
    "And with that, the ceremony is underway."
    "Most of it's a blur to me, just words and nodding heads."
    "It only seems to become real when we get to the point of exchanging vows."
    "Priest" "Do you, Camila..."
    "Priest" "Take these two people..."
    "Priest" "To be your lawful, wedded partners?"
    show camila happy
    camila.say "I do."
    "Priest" "And do you, Lexi..."
    "Priest" "Take these two people..."
    "Priest" "To be your lawful, wedded partners?"
    show lexi happy
    lexi.say "Sure thing!"
    "The priest raises any eyebrow at Lexi's choice of words."
    "But then he seems to shake it off as he turns his attention to me."
    "Priest" "And finally, do you, [hero.name]..."
    "Priest" "Take these two people..."
    "Priest" "To be your lawful, wedded partners?"
    mike.say "I do."
    "The priest nods and then turns to the assembled guests."
    "Priest" "I call upon those here present..."
    "Priest" "That if they know of any lawful reason these three may not be wed..."
    "Priest" "Speak now, or forever hold your peace!"
    "Normally this is the point where everyone shares a knowing chuckle."
    "But I'm genuinely worried that it'll be a flash-point."
    "I can see one of the cops standing up and reading off Lexi's list of crimes."
    "Or one of the crooks revealing that Camila sent his brother to the electric chair!"
    "Then one of them will whip out a gun and start shooting the place up!"
    "Priest" "Very well."
    "Priest" "I now pronounce you married."
    "Priest" "You may kiss your partners."
    "And just like that, my fears vanish."
    "There are no objections and no gun-shots."
    "Just Camila and Lexi smiling up at me."
    show lexi wedding c at center, zoomAt (1.5, (840, 1040))
    show camila wedding a at center, zoomAt (1.5, (440, 1040))
    "Not waiting for me to make the first move, they embrace me from either side."
    "And the kisses that we exchange wash away the last of my worries."
    "I did it!"
    "I married Camila and Lexi!"
    "And I couldn't be happier right now."

    scene criminal harem ending
    with fade
    camila.say "So..."
    camila.say "We're supposed to tell everyone how great living with, [hero.name] is?"
    camila.say "Hmm...are we under oath or anything?"
    lexi.say "Ah, don't be so serious, Camila!"
    lexi.say "All we gotta do is talk about the guy."
    lexi.say "And what's not to like about it, huh?"
    camila.say "Yeah...I suppose you're right, Lexi."
    camila.say "Being married to [hero.name] is pretty sweet."
    lexi.say "Of course it is, Camila!"
    lexi.say "It meant that I could finally move out of the trailer park."
    lexi.say "And it's not like he makes me pimp myself out like Danny used to."
    camila.say "Yeah, Lexi..."
    camila.say "Because he knows what I'd do to him if he even suggested it!"
    lexi.say "Aw, thanks, Camila!"
    lexi.say "Living with you is pretty great too."
    lexi.say "Even if you ARE a cop..."
    lexi.say "And you gotta admit, [hero.name] was cool with that."
    lexi.say "Like, he didn't try to stop you from staying on the force."
    camila.say "That was my decision to make!"
    camila.say "But yeah, I am glad he didn't hassle me over it."
    camila.say "Once a cop, always a cop, Lexi."
    camila.say "You can't just walk away from the job!"
    lexi.say "Yeah..."
    lexi.say "But we're married now, right?"
    lexi.say "I mean, you wouldn't shop me or [hero.name], would you?"
    camila.say "Oh, wouldn't you like to know, Lexi!"
    lexi.say "No way, Camila!"
    lexi.say "That's not fair!"
    camila.say "Anyway..."
    camila.say "I'm kind of glad that I ended up with you and [hero.name]."
    camila.say "Because all of my friends were cops before that."
    lexi.say "I know what you mean, Camila."
    lexi.say "All of my friends were..."
    lexi.say "Well, they were..."
    camila.say "Crooks?"
    lexi.say "Urgh..."
    lexi.say "I guess so!"
    camila.say "Let's just say [hero.name] introduced us both to new people, yeah?"
    lexi.say "He did more than that."
    lexi.say "He made us into a family!"
    if (camila.is_visibly_pregnant or camila.flags.mikeBabies >= 1) and (lexi.is_visibly_pregnant or lexi.flags.mikeBabies >= 1):
        camila.say "You can say that again!"
        camila.say "What are the chances of us BOTH having twins?"
        lexi.say "I know!"
        lexi.say "First you dropped Nova and Seren."
        lexi.say "Then I had Chantel and Tyrone!"
        camila.say "At least we know that [hero.name]'s not firing blanks!"
        lexi.say "Yeah, but he can put a muzzle on it."
        lexi.say "Or else he's not using that thing on me in future!"
    elif (camila.is_visibly_pregnant or camila.flags.mikeBabies >= 1):
        camila.say "You can say that again!"
        camila.say "What are the chances of me having twins?"
        lexi.say "I know!"
        lexi.say "You dropped Nova and Seren out of nowhere!"
        camila.say "At least we know that [hero.name]'s not firing blanks!"
        lexi.say "Yeah, but he can put a muzzle on it."
        lexi.say "Or else he's not using that thing on me in future!"
    elif (lexi.is_visibly_pregnant or lexi.flags.mikeBabies >= 1):
        camila.say "You can say that again!"
        camila.say "What are the chances of you having twins?"
        lexi.say "I know!"
        lexi.say "I dropped Chantel and Tyrone out of nowhere!"
        camila.say "At least we know that [hero.name]'s not firing blanks!"
        lexi.say "Yeah, but he can put a muzzle on it."
        lexi.say "Or else he's not using that thing on me in future!"
    else:
        camila.say "Yeah, but we're not a real family yet..."
        lexi.say "Oh, I see!"
        lexi.say "You want to get banged up!"
        camila.say "What I mean is that I want to have kids, Lexi!"
        camila.say "Isn't that something you want too?"
        camila.say "I'd like to know that [hero.name]'s not firing blanks!"
        lexi.say "Yeah, don't let him put a muzzle on it either!"
        lexi.say "Oh, I should say - twins are really common in my family."
        camila.say "How weird - mine too!"
    lexi.say "So everything worked out in the end, right?"
    lexi.say "[hero.name] saved me from having to live at the trailer park."
    lexi.say "And he saved you from being just a tight-ass cop too!"
    camila.say "HEY!"
    camila.say "I don't need anyone to save me!"
    lexi.say "Ooh..."
    lexi.say "So you admit that you're a tight-ass?"
    camila.say "What the..."
    camila.say "Shut up, Lexi!"
    lexi.say "Ha, ha!"
    lexi.say "Come on, Camila!"
    lexi.say "You know you love me really!"
    $ game.set_new_game_plus()
    $ renpy.full_restart()
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
