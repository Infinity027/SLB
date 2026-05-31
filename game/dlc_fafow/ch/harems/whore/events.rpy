init python:
    Event(**{
    "name": "whore_harem_event_01",
    "label": "whore_harem_event_01",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 0,
    "conditions": [
        MinDateScore(90),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_nightclub"),
            ),
        PersonTarget(reona,
            Not(IsHidden()),
            IsRoom("nightclub", "nightclubbar"),
            MinStat("love", 120),
            MinStat("sexperience", 2),
            ),
        PersonTarget(lexi,
            OnDate(),
            MinStat("love", 120),
            MinStat("sexperience", 2),
            ),
        ],
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "whore_harem_event_02",
    "label": "whore_harem_event_02",
    "display_name": "About Lexi",
    "duration": 0,
    "icon": "button_lexi",
    "conditions": [
        IsDone("whore_harem_event_01"),
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget(reona,
            IsActive(),
            MinStat("sub", 10),
            Or(
                IsFlag("cheating_agreement", "mc"),
                IsFlag("cheating_agreement", "both"),
                ),
            ),
        ],
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "whore_harem_event_03",
    "label": "whore_harem_event_03",
    "display_name": "About Reona",
    "duration": 0,
    "icon": "button_reona",
    "conditions": [
        IsDone("whore_harem_event_02"),
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget(lexi,
            IsActive(),
            MinStat("sub", 20),
            ),
        PersonTarget(reona,
            Not(IsHidden()),
            MinStat("love", 130),
            MinStat("sub", 20),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "whore_harem_event_04",
    "label": "whore_harem_event_04",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 0,
    "conditions": [
        IsDone("whore_harem_event_03"),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_pub"),
            ),
        PersonTarget(lexi,
            Not(IsHidden()),
            Or(
                IsFlag("sexydate"),
                IsFlag("sluttydate"),
                ),
            ),
        PersonTarget(reona,
            Not(IsHidden()),
            Or(
                IsFlag("sexydate"),
                IsFlag("sluttydate"),
                ),
            MinStat("sub", 50),
            ),
        Or(
            PersonTarget(lexi,
                OnDate(),
                ),
            PersonTarget(reona,
                OnDate(),
                ),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "whore_harem_event_05",
    "label": "whore_harem_event_05",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 0,
    "conditions": [
        IsDone("whore_harem_event_04"),
        IsSeason(0, 1),
        IsHour(9, 14),
        HeroTarget(
            IsGender("male"),
            IsActivity("None"),
            IsFlag("nudistBeach")
            ),
        PersonTarget(lexi,
            Not(IsHidden()),
            ),
        PersonTarget(reona,
            Not(IsHidden()),
            MinStat("sub", 70),
            MinStat("love", 140),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "whore_harem_event_06",
    "label": "whore_harem_event_06",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 0,
    "conditions": [
        IsDone("whore_harem_event_05"),
        HeroTarget(
            IsGender("male"),
            IsFlag("whore_nudist_beach")
            ),
        MinDateScore(50),
        PersonTarget(lexi,
            Not(IsHidden()),
            OnDate(),
            MinStat("sub", 80),
            MinStat("love", 160),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "whore_harem_event_07_text",
    "label": "whore_harem_event_07_text",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 0,
    "conditions": [
        IsDone("whore_harem_event_05"),
        IsNotDone("whore_harem_event_07"),
        HeroTarget(
            IsGender("male"),
            IsFlag("whore_nudist_beach")
            ),
        PersonTarget(reona,
            Not(IsHidden()),
            Not(IsPresent()),
            Not(IsActivity("None")),
            MinStat("sub", 80),
            MinStat("love", 160),
            ),
        ],
    "once_day": True,
    })

    Event(**{
    "name": "whore_harem_event_07",
    "label": "whore_harem_event_07",
    "priority": 500,
    "music": "music/roa_music/jump.ogg",
    "duration": 1,
    "conditions": [
        IsDone("whore_harem_event_07_text"),
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget(reona,
            Not(IsHidden()),
            IsActive(),
            MinStat("sub", 80),
            MinStat("love", 160),
            ),
        ],
    "do_once": True,
    })

label whore_harem_event_01:
    "When you're feeling stressed and strung out, there's no better way to relax than dancing your troubles away."
    show dance lexi with fade
    "And they're guaranteed to disappear that much more quickly if you make sure that Lexi's your dancing partner."
    "Before we came to the club tonight, my head was filled with nothing but worry and negative thoughts."
    "But now the only thing on my mind is the sight of Lexi, shaking her assets in front of me for all she's worth!"
    "Sure, she's never going to be able to help me with the deeper quandaries and philosophical problems in life."
    "Yet the way she's wiggling her ass and shaking her chest right now, I'm hardly too concerned!"
    hide dance
    show lexi b annoyed nophone at center, zoomAt(1.5, (640, 1040))
    with fade
    lexi.say "Are you gonna look me in the eyes even once tonight?"
    mike.say "Huh..."
    mike.say "What did you say, Lexi?"
    show lexi angry
    lexi.say "Ah, never mind."
    lexi.say "I ain't getting turned on by your face either!"
    "I'm about to ask Lexi just what she means by that."
    "But then I feel the sensation of someone tapping me on the shoulder."
    "On sheer instinct, I turn around to see who it could be."
    hide lexi
    if reona.flags.cheating_agreement in ["mc", "both"]:
        show reona leftback rightopen
        "I'm surprised to see Reona standing behind me."
        "From the look on her face, she's seen that I'm here with Lexi."
        "And she looks more than a little intrigued by that fact."
        reona.say "Hey there, [hero.name]..."
        show reona rightnormal leftnormal
        reona.say "Who's your friend?"
        show reona at left with ease
        show lexi at right5 with easeinright
        "I look from Reona to Lexi."
        "And I can see that the interest is definitely mutual."
        lexi.say "Oh my god..."
        lexi.say "I was gonna ask the same thing!"
        "From the way things are going, I need to make the introduction."
        "And quickly, before they decide too cut me out of the equation!"
        mike.say "Reona, this is Lexi."
        mike.say "Lexi, this is Reona."
        mike.say "I...she...we're..."
        show lexi happy
        show reona happy
        "As one, Reona and Lexi laugh at my being tongue-tied."
        show reona leftback
        reona.say "Oh, [hero.name]..."
        lexi.say "Tell me about it!"
        lexi.say "He can't even say the words."
        show reona rightopen
        reona.say "It's okay - we're both girls you're fucking at the same time."
        reona.say "Isn't that right, Lexi?"
        show lexi wink
        lexi.say "You know it is!"











        reona.say "Mmm..."
        reona.say "I would love to have a go at that!"
        hide reona with easeoutleft
        "With that, Reona turns on her heel and walks away."
        "As I watch her go, Lexi takes hold of my hand."
        show lexi at center with ease
        lexi.say "For the record, [hero.name]..."
        lexi.say "The feeling is mutual!"
    else:
        show reona sad leftback righthold
        "I'm surprised to see Reona standing behind me."
        "From the look on her face, she's seen that I'm here with Lexi."
        "And she certainly doesn't seem pleased about it."
        mike.say "Reona..."
        mike.say "I can explain..."
        play sound spank
        show reona rightopen at center, zoomAt(1.5, (640, 1040)) with hpunch
        "The slap connects before I can finish what I have to say."
        "And the way it spins my head around is more painful than the actual blow itself."
        mike.say "Urgh..."
        mike.say "Jesus, Reona!"
        show reona angry
        reona.say "Don't even try to explain, [hero.name]."
        reona.say "Not after what you just did to me!"
        show reona at center, traveling(1.0, 0.25, (340, 720))
        pause 0.25
        show reona at left with ease
        show lexi surprised with easeinright
        "By now Lexi's pretty much sized up the situation."
        "Yet she doesn't seem ready to step in and defend me one bit."
        "Instead she's looking Reona up and down."
        "And I can tell that she likes what she sees."
        lexi.say "Ouch!"
        show lexi normal
        lexi.say "Looks like someone's been a naughty boy!"
        mike.say "Lexi, please..."
        mike.say "Just stay out of this, okay?"
        show lexi surprised
        "Lexi throws up her hand in a gesture of surrender."
        "Happy to let me deal with the mess that I've made on my own."
        lexi.say "Whatever..."
        show reona righthold
        reona.say "I can't believe you're with another girl, [hero.name]."
        reona.say "Especially after you sold me that line of bullshit."
        if reona.flags.cheating_agreement == "neither":
            reona.say "After you told me you wanted to keep it exclusive!"
        mike.say "No, Reona..."
        mike.say "This isn't what it looks like."
        mike.say "Lexi's just...a friend!"
        show lexi happy
        "Lexi can't help giggling at the suggestion."
        "And she's so amused that she jumps back into the conversation too."
        lexi.say "HA!"
        lexi.say "Friend with benefits, more like!"
        show fx anger at left
        show reona devious
        "It doesn't help that I see an ironic smile on Reona's face."
        "Like she really appreciates Lexi's sentiment."
        reona.say "Oh man..."
        hide fx
        show reona angry
        reona.say "You suck SO much, [hero.name]."
        reona.say "If you'd only done things my way..."
        reona.say "We could have all had so much fun."
        show lexi normal
        lexi.say "She's got you there, [hero.name]!"
        mike.say "But, Reona..."
        mike.say "We can still try it your way!"
        show reona rightopen
        show lexi surprised
        reona.say "No we can't, [hero.name]."
        reona.say "Because I don't trust you anymore."
        reona.say "Consider yourself dumped."
        hide reona with easeoutleft
        "With that, Reona turns on her heel and walks away."
        show lexi happy
        "Leaving me to listen to the sound of Lexi's giggling."
        "Laughter that I know is totally at my expense."
        $ reona.set_gone_forever()
    return

label whore_harem_event_02:
    show reona happy leftback
    reona.say "So..."
    reona.say "I really liked meeting your little friend the other day."
    show reona normal
    "By now I'm more than used to the way that Reona likes to speak to me."
    "So I don't even bother to ask who she might happen to be talking about."
    "Instead I simply change the gear of my brain from casual conversation."
    "And I shift it straight over to thinly-veiled innuendo."
    mike.say "Oh really?"
    mike.say "Did you now, Reona?"
    show reona sadshock
    "Reona nods at this, her expression a becoming a tad confused."
    reona.say "Erm...yeah..."
    reona.say "I really took a liking to them."
    show reona interested
    mike.say "Well now..."
    mike.say "I'm sure we could arrange for you to meet him again."
    mike.say "And real soon too!"
    show reona shock
    "Now Reona really is looking at me in genuine confusion."
    reona.say "He?!?"
    reona.say "Wow, [hero.name]…"
    reona.say "I had no idea that Lexi was a guy..."
    show reona normal
    reona.say "That makes them so much more interesting!"
    "Now it's my turn to look confused."
    show reona embarrassed
    mike.say "What are you talking about, Reona?"
    mike.say "Lexi's not a guy!"
    mike.say "At least, I'm pretty sure she's not."
    show reona pensive
    reona.say "Wait a minute..."
    reona.say "I think we've got our wires crossed here..."
    show reona annoyed
    reona.say "I'm talking about the girl you introduced to me as Lexi."
    reona.say "Who on earth are you talking about?"
    "I think about denying it and spinning some kind of bullshit lie."
    "But then I realise that's only ever going to make the situation worse."
    "And so instead I decide to just come straight out and admit the truth."
    mike.say "Okay, okay..."
    show reona pensive
    mike.say "I thought you were talking about my...about my penis!"
    mike.say "You know 'my little friend' and all that?"
    "Another girl might have been offended by that admission."
    "They might even have given me a slap in the face for my trouble."
    show reona normal
    "But luckily for me, Reona's not that kind of girl."
    "Instead she just bursts out laughing and shakes her head."
    reona.say "Oh, [hero.name]..."
    reona.say "You really do think with your dick, don't you?"
    show reona flirt
    reona.say "But I'd never call you little in that department!"
    show reona happy
    reona.say "Seriously though, I was talking about Lexi."
    "I nod at this, keen to move on from me embarrassing myself."
    mike.say "Oh yeah, Reona..."
    mike.say "Lexi's a great girl."
    mike.say "Hot as they come, and really open-minded too."
    "All of a sudden, a thought occurs to me."
    "And without thinking, I throw it into the conversation."
    mike.say "You know, she kind of reminds me of you!"
    show reona interested leftnormal
    "Reona's interest seems to be piqued by this."
    "And she leans in closer, like she's pressing me for more."
    reona.say "She does?"
    reona.say "Like, how are we similar?"
    mike.say "Well..."
    mike.say "I mean the most obvious thing is that you're both gorgeous."
    mike.say "You know, like, totally smoking hot!"
    show reona happy
    "Reona nods at this."
    reona.say "Well clearly!"
    reona.say "But tell me more."
    mike.say "And you're both adventurous when it comes to sexy stuff too."
    mike.say "Like, there are times when Lexi will get all horny."
    mike.say "And she'll be all, like, 'fuck me in this alley, right now!'."
    mike.say "You know, even if it's up against a filthy dumpster or something?"
    show reona interested
    "By now I can see that Reona's eyes are getting wider."
    "Like she's hanging on my every word as I describe Lexi to her."
    "And the more lurid the details become, the more she likes it."
    show reona happy
    reona.say "Oh hell yeah!"
    reona.say "Sounds like we could practically be twins!"
    show reona normal
    "It's then that I remember the other side to Lexi's character."
    "The one that sometimes makes her dangerous."
    "Also the one that's almost always the source of all her problems."
    mike.say "I wouldn't go that far, Reona."
    mike.say "I don't think you come from the same background as Lexi."
    mike.say "When I say she's a bad girl, I kind of mean it literally."
    mike.say "She's always hanging around in seedy bars and associating with a bad crowd."
    mike.say "And I'm pretty sure she's been on the game in the past too!"
    "I meant to share all of this information with a specific goal in mind."
    "And that was to clue Reona in on the less desirable side of Lexi's character."
    "But it doesn't seem to be having the desired effect."
    show reona interested
    "If anything, Reona seems more intrigued now then ever."
    reona.say "Oh wow..."
    reona.say "You mean she's from the wrong side of the tracks?"
    show reona flirt
    reona.say "That is SO hot!"
    mike.say "Ah..."
    mike.say "No, Reona..."
    mike.say "That's not exactly what I meant!"
    "For all of my efforts to explain myself, nothing seems to work."
    "Reona just keeps on getting more swept up in her admiration for Lexi."
    show reona normal
    reona.say "You know that you have to let me hang out with her sometime, right?"
    reona.say "I think that the three of us could have some real fun together!"
    mike.say "Tell you what, Reona..."
    mike.say "I'll keep that in mind the next time I bump into Lexi."
    mike.say "And I'll be sure to ask her what she thinks of the idea."
    show reona happy leftback
    "Reona nods, clearly happy with the offer."
    "And as I think about it, I find I'm beginning to warm to the idea myself."
    "My initial surprise is probably what made me so reluctant at first."
    "But Reona's right that they have a lot in common."
    "Plus Lexi's been making a real effort to clean up her act recently."
    "So maybe the two of them would be good for each other?"
    "I can certainly see how it would be good for me!"
    "In fact, it's starting to sound like a win-win situation."
    "Two totally liberated girls that love sexual exploration with multiple partners."
    "I'd have to be crazy to say no to that!"
    return

label whore_harem_event_03:
    show lexi normal nophone
    "Lexi's got a huge grin on her face as she sidles her way towards me."
    show lexi at center, traveling(1.5, 1.0, (640, 1040))
    "And once she makes it over to where I'm standing, she leans in real close."
    "I'm smiling too, until I realise that she's grabbed me by the balls!"
    show lexi flirt with vpunch
    mike.say "Urgh..."
    mike.say "Lexi..."
    mike.say "What are you..."
    "It's not as if Lexi's actually trying to hurt me down there."
    "More like she's squeezing firmly for the sake of getting my attention."
    "But that doesn't seem to mean she's not enjoying it at the same time."
    show lexi normal
    lexi.say "What's the matter, [hero.name]?"
    lexi.say "Don't you like it when I play with them?"
    show lexi wink
    lexi.say "Or is that just for your new little friend?"
    lexi.say "The one you were with the last time?"
    mike.say "You..."
    mike.say "You mean Reona?!?"
    show lexi normal
    lexi.say "That's the one!"
    "Lexi seems to be pleased with my admission."
    "At least pleased enough to loosen her grip on my balls a little."
    mike.say "Phew..."
    mike.say "You know you could have just asked me about her, right?"
    mike.say "I'm not some pimp that's refusing to pay you for your services!"
    show lexi happy at startle
    "Lexi lets out a peal of laughter at this and shakes her head."
    "She plants a kiss on my cheek as she does so too."
    lexi.say "Oh, [hero.name]…"
    lexi.say "I'd never be so gentle with someone that owed me money!"
    show lexi normal
    lexi.say "But since you mentioned this Reona..."
    lexi.say "Let's have a little chat about her, yeah?"
    "Sure, my balls are feeling a bit sore after Lexi's done squeezing them."
    "But now I'm becoming more intrigued with just why she wants to talk about Reona."
    mike.say "So what's with your interest in Reona?"
    mike.say "I mean, she's not exactly the first of my female friends that you've met."
    mike.say "Why are you pumping me for more info on her?"
    mike.say "Normally you'd just tell me that you thought she was hot or something like that!"
    show lexi wink
    lexi.say "Oh, I think she's hot for sure."
    lexi.say "Like, super hot!"
    show lexi normal
    lexi.say "But there's something else about her too."
    lexi.say "Something about the aura she gives off, you know?"
    lexi.say "It's kind of familiar."
    "I can't help chuckling as Lexi ponders the feeling that she got off of Reona."
    show lexi surprised
    "And when she hears me laughing, Lexi doesn't seem very impressed."
    lexi.say "Hey!"
    show lexi angry
    lexi.say "What's so funny, you big jerk?"
    mike.say "Don't take it too hard, Lexi..."
    mike.say "But I think I know what you find familiar about Reona."
    show lexi surprised
    lexi.say "You do?"
    lexi.say "So what is it?"
    show lexi angry
    lexi.say "You'd better tell me, and fast!"
    "I hold up my hand to show Lexi that I'm going to do as she asks."
    "Though at the same time I'm thinking fast as to how I'm going to say this."
    "Because if I get it wrong, she could easily take offence."
    mike.say "Let's just say Reona's liberated in some of the same ways you are, Lexi."
    show lexi surprised
    mike.say "She's generous with her affections, if you know what I mean?"
    "Realisation seems to be dawning on Lexi as I explain."
    "And soon enough, she's nodding her head."
    lexi.say "Oh, I see!"
    show lexi happy
    lexi.say "Why didn't you just say that she love cock?"
    "Good old Lexi, always getting to the point."
    mike.say "You could put it that way, I guess."
    mike.say "I met Reona at college a little while back."
    mike.say "She was struggling with her course and needed some tuition."
    mike.say "So I offered to help her out with her studies."
    "The smile on Lexi's face becomes knowing at this."
    "And she nods, giving me a playful jab in the ribs."
    show lexi normal
    lexi.say "I get the picture, [hero.name]."
    lexi.say "You helped her out with that big old brain of yours."
    show lexi wink
    lexi.say "And she repaid you with those big titties of hers!"
    "I can't help flushing with colour as Lexi makes her accusation."
    "And a lot of that is because she's kind of hit the nail on the head."
    "Even if I'd argue it really didn't happen in exactly the way she's suggesting."
    show lexi surprised
    mike.say "Lexi!"
    mike.say "I didn't make Reona pay me with sex!"
    mike.say "I tutored her for free, and she passed her exams with my help."
    mike.say "We only started having sex after that - because we liked each other!"
    "Lexi's still giving me that knowing look, even now I've explained myself."
    "And something gives me the feeling that she's never going to be totally convinced."
    show lexi normal
    lexi.say "Whatever you say, [hero.name]."
    lexi.say "But I still like the sound of this girl."
    lexi.say "I like it a lot!"
    "Lexi seems to be satisfied with all that I've said."
    "And after that she lets the matter lie."
    "But I make sure to remember the interest that she's shown in Reona."
    "Just in case there's a chance of the two meeting in the future."
    "Because if that happens, I want to be there to reap any potential benefits."
    return

label whore_harem_event_04:
    $ renpy.dynamic(acting_stripper=None, available_strippers=[])
    if "bree_stripclub_intro" in DONE and bree.flags.work_stripclub:
        $ available_strippers.append("bree")
    if hanna.flags.schedule == "stripclub":
        $ available_strippers.append("hanna")
    if harmony.flags.schedule == "stripclub":
        $ available_strippers.append("harmony")
    if shiori.flags.schedule == "stripclub":
        $ available_strippers.append("shiori")
    if available_strippers:
        $ acting_stripper = renpy.random.choice(available_strippers)
    if date_girl == lexi:
        $ reona.set_room(game.room)
        scene bg street with fade
        "I've had a date in the diary to meet up with Lexi for a while now."
        "But it's been a busy week and so I've had no headspace to think of a plan."
        "So the best that I could come up with was the idea of inviting her to the pub."
        "And luckily for me, Lexi can often be a pretty cheap date - if you get my meaning?"
        "Which means she's perfectly happy to meet me down at The Winchester for a couple of pints."
        scene bg door pub with fade
        "So much so that when I walk in through the door, she's already waiting for me."
        scene bg pub with fade
        lexi.say "Hey, [hero.name]…"
        lexi.say "Over here!"
        scene bg black
        show drink lexi sexydate pub
        with fade
        "I see Lexi waving to me from a table that she's already claimed for herself."
        "And as I walk over there, I also see that she's bought a round of drinks too!"
        mike.say "Hey, Lexi..."
        mike.say "Wow..."
        mike.say "You already got me a round in?"
        "Lexi nods eagerly, pushing a pint of beer towards me as I sit down."
        lexi.say "Oh yeah, I already had a couple while I was waiting for you!"
        lexi.say "Come on, get drinking already..."
        lexi.say "You've got some catching up to do!"
        "Now that I'm sitting down with a drink in my hand, I get a closer look at Lexi."
        "And I can instantly see that she's not joking - she's already looks pretty drunk!"
        "So as I can't make her slow down, I guess the best thing is for me to speed up."
        "I down the pint she gave me as quickly as I can and then go grab another round."
        "But much to my dismay, Lexi's already polished off her own drink when I get back!"
        "At this rate she's going to drink me under the table."
        reona.say "Hey, you guys..."
        reona.say "Why didn't you tell me you were out drinking?!?"
        scene bg pub
        show reona sexydate normal at center, zoomAt(1.25, (940, 900))
        with fade
        "As one, Lexi and I turn around to see Reona standing behind us."
        "She has a drink in her hand too."
        "And from the way she's swaying, it's not her first of the night."
        "I open my mouth to speak, but Lexi jumps in first."
        lexi.say "REONA..."
        lexi.say "Get your ass over here!"
        "I look from Lexi to Reona and then back again."
        "And I start to remember the interest that they've been showing in each other."
        "Which makes me wonder just what would happen if I were to encourage that connection."
        "That and maybe pour some more alcohol into the mix..."
        mike.say "Oh totally..."
        mike.say "Reona, you should totally come and join us."
        show reona happy
        "Reona seems to be delighted by our enthusiasm, a smile spreading across her face."
        show reona at center, zoomAt(1.25, (640, 900)) with ease
        "And she hurries over to the table, sliding into an empty seat between Lexi and me."
        show reona pensive
        reona.say "Sure, sure..."
        reona.say "I'm here on my own anyway, and I could use the company."
    else:
        $ lexi.set_room(game.room)
        scene bg street with fade
        "I've had a date in the diary to meet up with Reona for a while now."
        "But it's been a busy week and so I've had no headspace to think of a plan."
        "So the best that I could come up with was the idea of inviting her to the pub."
        "And luckily for me, Reona can often be a pretty cheap date - if you get my meaning?"
        scene bg door pub with fade
        "Which means she's perfectly happy to meet me down at The Winchester for a couple of pints."
        scene bg pub with fade
        "So much so that when I walk in through the door, she's already waiting for me."
        reona.say "Hey, [hero.name]…"
        reona.say "Over here!"
        scene bg black
        show drink reona sexydate pub
        with fade
        "I see Reona waving to me from a table that she's already claimed for herself."
        "And as I walk over there, I also see that she's bought a round of drinks too!"
        mike.say "Hey, Reona..."
        mike.say "Wow..."
        mike.say "You already got me a round in?"
        "Reona nods eagerly, pushing a pint of beer towards me as I sit down."
        reona.say "Oh yeah, I already had a couple while I was waiting for you!"
        reona.say "Come on, get drinking already..."
        reona.say "You've got some catching up to do!"
        "Now that I'm sitting down with a drink in my hand, I get a closer look at Reona."
        "And I can instantly see that she's not joking - she's already looks pretty drunk!"
        "So as I can't make her slow down, I guess the best thing is for me to speed up."
        "I down the pint she gave me as quickly as I can and then go grab another round."
        "But much to my dismay, Reona's already polished off her own drink when I get back!"
        "At this rate she's going to drink me under the table."
        lexi.say "Hey, you guys..."
        lexi.say "Why didn't you tell me you were out drinking?!?"
        scene bg pub
        show lexi a sexydate normal nophone at center, zoomAt(1.25, (940, 900))
        with fade
        "As one, Reona and I turn around to see Lexi standing behind us."
        "She has a drink in her hand too."
        "And from the way she's swaying, it's not her first of the night."
        "I open my mouth to speak, but Reona jumps in first."
        reona.say "LEXI..."
        reona.say "Get your ass over here!"
        "I look from Reona to Lexi and then back again."
        "And I start to remember the interest that they've been showing in each other."
        "Which makes me wonder just what would happen if I were to encourage that connection."
        "That and maybe pour some more alcohol into the mix..."
        mike.say "Oh totally..."
        mike.say "Lexi, you should totally come and join us."
        show lexi a happy
        "Lexi seems to be delighted by our enthusiasm, a smile spreading across her face."
        show lexi a smile at center, zoomAt(1.25, (640, 900)) with ease
        "And she hurries over to the table, sliding into an empty seat between Reona and me."
        show lexi a normal
        lexi.say "Sure, sure..."
        lexi.say "I'm here on my own anyway, and I could use the company."
    scene drink_room_pub
    show reona sexydate at center, zoomAt(1.65, (340, 1040))
    show lexi a smile sexydate nophone at center, zoomAt(1.65, (940, 1040))
    show drink_table_pub_victor
    show drink_room_fg_pub
    with fade
    "I'm more than aware of the fact that the girls have a couple of drinks on me."
    "And they're not slowing down to let me catch up to them at all."
    "Which means that I have to up my own pace in the hope of not being left behind."
    "Pretty soon I can feel the effects of my efforts, as the room starts to sway."
    "But the problem is that I'm having such a good time with Lexi and Reona."
    "The last thing that I want to do is fall even further behind them."
    mike.say "Okay, okay..."
    mike.say "It's my round...I think!"
    show lexi a normal
    lexi.say "Is it?"
    lexi.say "I lost count already!"
    show lexi a smile
    show reona pensive
    reona.say "I think I bought the last one..."
    reona.say "Or was that the second to last one?"
    show reona normal
    "In the hope of breaking the deadlock, I make to stand up."
    "But my legs seem to have a very different plan in mind."
    "And the experience of standing up makes my head swirl."
    mike.say "I..."
    mike.say "Whoa..."
    mike.say "Who keeps shaking the pub?"
    mike.say "Tell them they need to stop!"
    scene bg pub
    show reona sexydate at center, zoomAt(1.5, (340, 1040))
    show lexi a smile sexydate nophone at center, zoomAt(1.5, (940, 1040))
    with fade
    "In the blink of an eye, Lexi and Reona are up and supporting me."
    "But I can see that they're not too steady on their feet either."
    show lexi a wow
    lexi.say "Whoops..."
    show lexi a normal
    lexi.say "I think we might have overdone it a little!"
    show lexi a smile
    show reona annoyed
    reona.say "Yeah, maybe you're right, Lexi..."
    show reona pensive
    reona.say "I think we should move on to someplace else."
    show reona happy
    "Before I have the chance to say another word, I feel them start to walk."
    hide reona
    hide lexi
    with easeoutright
    "And as they're still holding onto me, I have no choice but to go with them."
    scene bg street with fade
    pause 0.3
    show reona happy sexydate at center, zoomAt(1.5, (340, 1040))
    show lexi a smile sexydate nophone at center, zoomAt(1.5, (940, 1040))
    with easeinleft
    "We're soon out of the door and into the street."
    "Where the fresh air hits me like a slap to the face."
    mike.say "Wow..."
    mike.say "That's so much better."
    mike.say "I feel like my legs are working again!"
    show reona pensive
    reona.say "That's great news."
    reona.say "But where are we going to go now?"
    reona.say "I'm not ready to go home yet."
    show reona happy
    show lexi a normal
    lexi.say "Don't worry about it, guys..."
    lexi.say "I know the perfect place."
    lexi.say "Just follow me, okay?"
    show lexi a smile
    "Reona and I exchange a quick glance, and a shrug."
    "Then we fall in behind Lexi as she turn and walks away."
    "Reona and I follow on her heels, eager to see where she's taking us."
    "I'm sure that I'd be able to guess if I hadn't been drinking so much."
    "But as it is, I feel like we're being lead on a magical mystery tour."
    "And even when we get to the end of it, I'm still feeling kind of dazed."
    scene bg alley
    show reona happy sexydate at center, zoomAt(1.5, (340, 1040))
    show lexi a happy sexydate nophone at center, zoomAt(1.5, (940, 1040))
    with fade
    lexi.say "Ta da!"
    show lexi a normal
    lexi.say "Here we are, guys."
    show lexi a smile
    "Reona and I look up to see the frontage of a familiar establishment before us."
    mike.say "But, Lexi..."
    mike.say "This is the strip club!"
    show reona shock
    reona.say "Huh?"
    reona.say "I thought you were taking us to another bar?"
    show reona shy
    "Lexi waves away our questions, already walking towards the door."
    show lexi a normal
    lexi.say "Of course it's the strip club, [hero.name]."
    lexi.say "And for your information, Reona..."
    lexi.say "This place has a bar too!"
    show lexi a smile
    scene bg stripclub
    show reona normal sexydate at center, zoomAt(1.5, (340, 1040))
    show lexi a smile sexydate nophone at center, zoomAt(1.5, (940, 1040))
    with fade
    "Reona and I are quick to follow Lexi again as we walk into the strip club."
    mike.say "I should explain that I was just surprised that you chose this place."
    mike.say "It's not like I have anything against the strip club."
    reona.say "Me too..."
    show reona happy
    reona.say "I'm totally cool with this kind of thing."
    "It's reassuring that Reona makes the admission as we get into the place."
    scene bg black
    if acting_stripper:
        show expression f"poledance {acting_stripper} alone"
    else:
        show poledance shiori alone at dark, dark
    with fade
    "Because we walk straight into the middle of some girl's act!"
    "And all three of us are staring up at her as we take a seat."
    "Three pairs of eyes are fixated on her parts as she moves on the stage."
    "But there's something a little unusual about the girl up there."
    "Something that I can't quite put my finger on."
    mike.say "Huh..."
    mike.say "What is it that's bugging me about that girl?"
    scene bg stripclub
    show reona interested sexydate at center, zoomAt(1.5, (340, 1040))
    show lexi a smile sexydate nophone at center, zoomAt(1.5, (940, 1040))
    with fade
    reona.say "What do you mean, [hero.name]?"
    reona.say "She's dancing on the stage and getting naked."
    reona.say "Isn't that what the girls here are supposed to do?"
    show reona interested
    "I shake my head, dismissing Reona's attempt at an explanation."
    mike.say "I dunno, Reona..."
    show reona normal
    mike.say "There's just something off about it."
    mike.say "But I'm buggered if I can figure it out!"
    lexi.say "I think I can help you there, [hero.name]…"
    show lexi wink
    lexi.say "Look at the sign by the bar."
    "I look over to where Lexi's pointing, squinting to read the sign."
    mike.say "Open Pole Night!"
    mike.say "What...like an open mic night?"
    reona.say "So what..."
    show reona interested
    reona.say "Anyone can get up there and dance?"
    show lexi a happy
    "Lexi nods as a smile spreads across her face."
    show lexi a normal
    lexi.say "That's right, it's amateur night."
    show lexi a flirt
    lexi.say "And we just walked into the middle of it!"
    show lexi a smile
    "I can see from the glint in Lexi's eyes that's not the end of it."
    "She's not just stoked because we get to watch anyone that wants to get up there."
    "And as she looks Reona and me in the eye, I think I can guess what she's thinking."
    mike.say "Lexi..."
    show lexi a bored
    lexi.say "Oh come on!"
    show lexi a smile
    mike.say "You can't be serious?"
    show reona pensive
    reona.say "Serious about what?"
    show reona normal
    show lexi a normal
    lexi.say "Oh come on, you guys..."
    lexi.say "Why don't you try living a little?"
    show lexi a smile
    mike.say "I'm quite happy with the amount of living I'm doing right now!"
    show reona annoyed
    reona.say "What are you two even talking about?"
    "Lexi catches Reona's eye, rather than answering the question."
    "Then she draws her attention back to the stage and the amateur performer up there."
    "Or to be more precise, to the empty stage, as the girl's just finishing her dance."
    show reona surprised
    reona.say "Oh!"
    reona.say "You think we should get up and dance?"
    mike.say "Well that's what Lexi wants us to do."
    show reona normal
    hide lexi with easeoutright
    mike.say "But we haven't really thrashed it out yet..."
    mike.say "Have we, Lexi?"
    mike.say "Lexi?!?"
    "Not getting an answer, I turn around to find Lexi's seat empty."
    "And looking back the other way, I see her already halfway to the stage."
    "I assess the speed she's moving and the amount that I've had to drink."
    "Guessing that there's pretty much no chance of me being able to stop her."
    mike.say "Looks like we're going to get a special performance, Reona."
    show reona interested
    reona.say "Oh yeah?"
    reona.say "Is she good at this kind of thing?"
    mike.say "She's probably better when she hasn't had an absolute skin-full."
    mike.say "But I guess that we're going to find out pretty soon!"
    scene bg black
    show poledance lexi alone sexydate
    with fade
    "Almost as soon as Lexi strides onto the stage, the mood in the place changes."
    "And I can see that the amount she's had to drink isn't affecting her at all."
    "Instead she walks out there like she owns the place."
    "Standing in the middle of the stage, Lexi nods to the DJ."
    "Then the lighting goes down and spotlights point at her."
    "The next thing I know, Lexi is making love to the pole."
    "And she's stripping off her clothes with ease at the same time."
    "The rest of the patrons in the bar are already loving it."
    "They whoop and cheer as every piece of clothing comes off."
    show poledance lexi naked
    "And I find myself unable to tear my eyes away too."
    "Sure, it's pretty obvious that Lexi never took a dance class in her life."
    "But she more than makes up for it with raw passion, moving naturally."
    "And it looks like the knowledge she has an audience is fuelling her too."
    "Lexi doesn't seem to need to look at the crowd to know it either."
    "Almost like she can feel all of the eyes on her right now."
    "And the thrill of it is pushing her on to perform so well."
    "By the time the music comes to an end, Lexi must be totally exhausted."
    "Because I feel drained from just sitting here watching!"
    mike.say "WOW!"
    mike.say "What do you think of that, Reona?"
    scene bg stripclub with fade
    mike.say "Reona?!?"
    "Almost like a perfect replay of what happened before, I'm talking to empty space."
    "Because Reona's already out of her chair and hurrying towards the stage."
    scene bg black
    show poledance reona sexydate alone
    with fade
    "Even before Lexi's collected up her clothes, Reona takes her place."
    "And it looks like she's determined to show off her own skills up there too!"
    "I guess there's nothing I can do to keep Reona from doing a dance of her own."
    "Okay, okay...it's not like I'd have tried to stop her if I could!"
    "So now that we've got that out of the way, I'm going to sit back and watch."
    "Reona's dance begins in pretty much the same way Lexi's did."
    "Standing in the middle of the stage, she nods to the DJ."
    "But as soon as the music starts and she's moving, one difference is clear."
    "Lexi's moves were fuelled by sheer, instinctual sensuality."
    "Yet Reona's show me that she's at least had some dancing lessons in the past."
    "I admit that I don't have a clue what kind, as I'm not expert."
    "But she's moving and gyrating with a purpose and to a pattern."
    "And it's totally working for her too!"
    "Like she's taking inspiration from the music, Reona moves smoothly."
    "Not only that, she manages to work in enough sexiness to make it totally hot."
    "The audience are getting into it every bit as much as they did with Lexi."
    show poledance reona naked
    "And for my part, I'm not willing to stand up while this is going on."
    "Because what's going on in my shorts would make that pretty awkward!"
    "I do the best I can to keep my brain from being overloaded by what I'm seeing."
    "That and to ask Reona where she learnt to dance like that too!"
    "Once the music ends, Reona makes a move to leave the stage."
    scene bg stripclub
    show reona interested sexydate at center, zoomAt(1.0, (640, 740))
    show lexi a smile sexydate nophone at center, zoomAt(1.0, (940, 740))
    with fade
    "Lexi's waiting for her as well, just to one side."
    show reona surprised
    show lexi a surprised
    "But as they turn to leave, there's a chorus of boos from the crowd."
    "The girls turn as one, probably thinking they've done something wrong."
    "In doing so, they take a step back onto the stage."
    "And that's all it takes for the boos to turn into cheers."
    show reona happy
    show lexi a smile
    "As this happens, Lexi and Reona seem to realise what's happening."
    "Far from being upset, the crowd wants more!"
    "And so do I."
    "So I hammer my hands on the table and shout to encourage them."
    mike.say "Encore!"
    mike.say "You guys are the best!"
    mike.say "One more time for [hero.name]!"
    "Lexi and Reona seem to be warming up to the idea too."
    "As one they walk back onto the stage and turn to face the crowd."
    "This time the DJ doesn't need to be told what to do."
    "Again the lights go down and the spotlights come up."
    scene bg black
    show poledance lexi reona sexydate reona_sexydate alone forced
    with fade
    "And based on what I see next, I have no idea how they're doing it."
    "Like, I just said Lexi was acting on instinct and Reona had some training."
    "So neither of them can be coming from the same place as the other, right?"
    "But from the first moment they start to move, Lexi and Reona are working together."
    "Somehow the two different styles they possess begin to merge and compliment each other."
    "I don't know if Lexi's following Reona's more practiced moves."
    "Or if it's Reona that's using her skills to follow Lexi's natural ones."
    "But either way, the two of them are wrapping themselves around the pole - and each other!"
    "The crowd are lapping it up two, loving the way they're coming together."
    "And me?"
    "Well, what do you think this is doing to me?!?"
    "I've just sat through two of the sexiest moments of my entire life."
    "And now it's like they're being mashed together before my eyes!"
    "I can hear the people shouting, urging them on."
    show poledance lexi reona naked
    "But there's one loud-mouthed jackass that's louder than the rest."
    "Though I soon realise that it's me!"
    mike.say "WHOO!"
    mike.say "Now that's what I'm talking about!"
    mike.say "This is the greatest thing I've ever seen!"
    "I have no idea if Lexi and Reona can hear me over the rest of the crowd."
    "Though I have to say that I don't really care."
    "The only thing on my mind is watching them as closely as possible."
    "That and trying to burn the memory of what I'm seeing into my brain."
    "But all too soon the music stops and the lights come back up."
    "Which means that Lexi and Reona have to bring their dance to an end."
    "Though there's no booing as they collect their clothes and leave the stage this time."
    scene bg stripclub
    show reona happy sexydate at center, zoomAt(1.5, (340, 1040))
    show lexi a smile sexydate nophone at center, zoomAt(1.5, (940, 1040))
    with fade
    "And I can see all eyes in the place following them as they return to where I'm sitting."
    "Which is more than enough to make my head begin to swell with pride."
    mike.say "That was..."
    mike.say "I mean..."
    mike.say "Wow...just wow!"
    "Lexi and Reona are pulling on the last of their clothes as I stumble over my words."
    "I can see that they're both tired from their exploits on the stage."
    "But the smiles on their faces are totally genuine all the same."
    show lexi a wow
    lexi.say "Phew..."
    show lexi a happy
    lexi.say "That shit really takes it out of you!"
    show lexi a smile
    show reona pensive
    reona.say "You're telling me!"
    reona.say "I haven't danced like that in years."
    show reona happy
    mike.say "But you loved it, right?"
    mike.say "I mean..."
    mike.say "You could do it again, maybe?"
    mike.say "Like, quite soon?"
    "Lexi and Reona share a knowing glance and then a chuckle."
    show reona flirt
    reona.say "You hear that, Lexi?"
    reona.say "I think he wants an encore!"
    show lexi a flirt
    lexi.say "We can handle that, Reona..."
    lexi.say "But I say we make it a private show this time!"
    "All I can do is stare at them, mouth open and eyes wide."
    "Nodding my head like crazy as I begin to imagine the possibilities."
    return


label whore_harem_event_05:
    "My phone starts to vibrate, and I automatically pull it out of my pocket to see who's calling."
    "Normally I'm pretty much on autopilot when this happens, more than ready to let it got to voicemail."
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Reona")
    if not result:
        $ hero.cancel_event()
        $ reona.love -= 5
        return
    "But as soon as I see that it's a call from Reona, I snap out of it and instantly answer it."
    scene expression f"bg {game.room}" at blur(5), dark with dissolve
    "Because there's nothing I'm more interested in that hearing from a hot girl that's always a lot of fun!"
    mike.say "Hey, Reona..."
    mike.say "What can I do for you?!?"
    "I hear the sound of Reona chuckling to herself on the other end of the line."
    reona.say "Oh..."
    reona.say "Hello, [hero.name]…"
    reona.say "Sounds like someone's pleased to hear my voice!"
    "There's no way that I can play it down, so I just let out some laughter of my own."
    mike.say "Ha..."
    mike.say "Yeah, Reona..."
    mike.say "I guess that I just can't help it!"
    reona.say "That's okay, [hero.name]…"
    reona.say "It's super sweet that you're glad to hear from me."
    reona.say "But I do have something to ask you - so try to concentrate, yeah?"
    "I do as Reona says, clearing my mind of all irrelevant thoughts."
    "And instead I listen closely to what she's going to say next."
    mike.say "Okay, Reona..."
    mike.say "Lay it on me!"
    reona.say "Well, if you take a look outside, you'll see it's a nice day."
    reona.say "So I was going to ask if you wanted to come to the beach with me?"
    "Does she even have to ask?"
    "Of course I want to go to the beach with her!"
    mike.say "Sure I do!"
    mike.say "The beach is gonna be great on a day like this."
    mike.say "And I know the perfect spot where we can..."
    "Before I can finish what I was going to say, Reona cuts me off."
    reona.say "Erm..."
    reona.say "Not that beach, [hero.name]…"
    reona.say "I was talking about the OTHER beach, yeah?"
    reona.say "You know the one that I mean?"
    "I instantly get what Reona means, and I want to play it off smoothly."
    "But I guess my brain's just not in a smooth gear this morning."
    "Instead I blurt out the words before I can stop myself."
    mike.say "You..."
    mike.say "You mean the nudist beach?!?"
    "There's a pause again as I hear Reona chuckle for a second time."
    "Then she answers my question, taking advantage of how off-balance she's left me."
    reona.say "That's right - I mean the nudist beach!"
    reona.say "So what do you say, [hero.name]?"
    reona.say "Are you up for a little excitement, or what?"
    menu:
        "Refuse to go to the nudist beach":
            "The moment that Reona mentions the nudist beach, I feel my guts churn."
            "Understand that I have no problems with getting naked when I'm with a girl."
            "But there's no way I'm doing it in front of a bunch of strangers!"
            mike.say "Uh-uh, Reona..."
            mike.say "It's either the normal beach or nothing."
            reona.say "What?!?"
            reona.say "Are you actually serious?"
            mike.say "I'm being totally serious."
            mike.say "There's no way I'm going to the nudist beach."
            mike.say "Not with you or anyone else!"
            reona.say "Hurmph..."
            reona.say "Well screw you then!"
            reona.say "I'll just find somebody else to go with me."
            scene expression f"bg {game.room}" with dissolve
            "Reona ends the call before I can say anything more."
            "And part of me is worried that she wasn't just making an idle threat."
            "That she actually might end up going to the nudist beach with someone else."
            "But I keep telling myself that standing my ground is more important."
            "If I don't do that, Reona's never going to respect me."
            $ reona.love -= 10
            return
        "Agree to go to the nudist beach":
            "The moment Reona mentions the nudist beach, I feel like I must be dreaming."
            "I've spent ages wondering how I'd pitch a trip to the nudist beach to a girl."
            "And here she is, actually asking me if I want to go there with her!"
            mike.say "Are you kidding?!?"
            mike.say "Of course I want to go to the nudist beach with you!"
            mike.say "I can be meet you there as soon as I grab my stuff."
            reona.say "You can?"
            reona.say "That's great, [hero.name]…"
            reona.say "Get to the beach as soon as you can."
            scene expression f"bg {game.room}" with dissolve
            "As soon as the call ends, I rush around grabbing my stuff."
            "And then I head straight over to the beach."
            $ game.room = "beach"
            scene bg beach with fade
            "Once I get there, it doesn't take me long to spot Reona."
            "So I hurry over to where she's waiting."
            mike.say "Hey, Reona..."
            mike.say "I got here as soon as I could!"
            show reona swimsuit zorder 2 with dissolve
            "At the sound of my voice, Reona turns to look in my direction."
            show lexi a smile swimsuit nophone zorder 1 with dissolve
            pause 0.3
            show reona at left4
            show lexi a at right4
            with ease
            "And as she does so, I can see that she's not alone."
            mike.say "Lexi?"
            mike.say "What are you doing here?"
            "Lexi waves and gives me a smile."
            show lexi a nophone happy
            lexi.say "Hi, [hero.name]…"
            lexi.say "Reona invited me along too."
            show lexi a smile
            "I turn my gaze from Lexi to Reona, still looking a little puzzled."
            show reona pensive
            reona.say "You don't mind, do you?"
            reona.say "It's a nice surprise, right?"
            reona.say "And I thought this would be right up Lexi's street."
            show reona happy
            "I have a mind to mention that Lexi's more often to be found on street corners."
            "But I bite my tongue as I actually take a moment to think about it."
            "Which is when I realise that only a complete moron would object to Lexi coming along."
            "Why spend time at the nudist beach with one hot girl when you could be there with two?"
            "So I wave a hand in the air, dismissing Reona's concern."
            mike.say "Of course I don't mind."
            mike.say "Having Lexi along too will be great."
            "This earns me a round of smiles as we start to walk down to the beach."
            call whore_harem_beach_fuck from _call_whore_harem_beach_fuck
    scene bg beach with fade
    "Once it's all over, the three of us lie back on the sand."
    "We're totally exhausted, utterly spent and hopelessly worn-out."
    "All we want to do is spend the rest of our time on the beach recovering."
    "But even so, I swear that I can hear something as I lie there."
    "And I'm pretty sure that it's a round of applause."
    "One intended for Lexi, Reona and myself."
    "As a show of appreciation for the show we just put on."
    $ hero.flags.whore_nudist_beach = True
    $ lexi.sexperience += 1
    $ reona.sexperience += 1
    return

label whore_harem_event_06:
    show lexi
    "Lexi and I are just taking some time to hang-out together and chill."
    "No real agenda or anything that either of us really wants to do."
    "Simply taking the chance to enjoy each other's company for once."
    "And that's something that should be really nice, you know?"
    show lexi blank at center, zoomAt(1.5, (640, 1040)) with fade
    "But it doesn't take long for me to sense that there's something up."
    "Like, there's a metaphorical elephant in the room."
    show lexi sadsmile
    lexi.say "This is nice..."
    lexi.say "Right, [hero.name]?"
    show lexi blank
    mike.say "Erm..."
    mike.say "Yeah, Lexi..."
    mike.say "I'm really having a nice time."
    show lexi smile
    "I'm looking at Lexi as she asks me the question."
    "And I note that she smiles and starts nodding as soon as I answer her."
    "But it's not in the kind of natural way that I've come to expect of Lexi."
    "Normally she's pretty cocky and nonchalant in the way she behaves."
    "Yet right now she seems to be hanging on my every word."
    show lexi happy
    lexi.say "Me too..."
    show lexi normal
    lexi.say "A really nice time!"
    lexi.say "Almost as nice as the last time that we went out on a date."
    lexi.say "You remember that, right?"
    lexi.say "When we were out on a date with Reona?"
    show lexi smile
    "I can't help furrowing my brow and frowning as I listen to Lexi."
    "Because it's not like she's being subtle about anything she's saying."
    "I mean, she could be trying to - but she's failing badly!"
    mike.say "Lexi..."
    mike.say "I thought the point of today was for us to spend time together?"
    mike.say "You know, just you and me?"
    show lexi blank
    mike.say "But you're starting to make it sound like you'd rather be with Reona!"
    show lexi surprised
    "Lexi's eyes go wide at the accusation."
    "And she hurries to shake her head."
    show lexi wow
    lexi.say "No!"
    lexi.say "No, no, no!"
    show lexi sadsmile
    lexi.say "Well..."
    show lexi bored
    lexi.say "Maybe a little bit?"
    show lexi blank
    "The effect the admission has on me must be plain to see."
    "Because Lexi looks horrified as she reads the expression on my face."
    show lexi surprised
    lexi.say "But not like that!"
    lexi.say "I don't mean it like that!"
    show lexi sad
    "I let out a sight of genuine frustration and confusion."
    mike.say "Huh..."
    mike.say "Then how do you mean it, Lexi?"
    show lexi bored
    lexi.say "I don't mean I want Reona here instead of you, [hero.name]…"
    show lexi sadsmile
    lexi.say "What I mean is that I want her here as well as you!"
    show lexi normal
    lexi.say "Like, it's so much better when all three of us are together."
    show lexi blank
    "I find myself staring at Lexi as I try to make sense of what she's saying."
    mike.say "You know what, Lexi..."
    show lexi blank blush
    mike.say "It kind of sounds like you have feelings for Reona."
    mike.say "And I mean the serious kind of feelings!"
    "Lexi looks away from me for a moment, like she can't meet my eye."
    "But at the same time she nods her head."
    show lexi sadsmile
    lexi.say "Y...yeah..."
    lexi.say "I kinda feel the same way about her as I do about you, [hero.name]…"
    show lexi normal
    lexi.say "I think I'm in love with the both of you!"
    show lexi smile
    menu:
        "You know what? That goes the same about me." if "whore_harem_event_07" not in DONE or Harem.find("reona", "whore"):
            "The moment Lexi makes the admission, I feel a rush of excitement."
            "Because I've been feeling a growing affection for Reona too."
            "And I was dreading the moment when I was going to have to choose between them."
            "But now it looks like I might not have to make that decision!"
            show lexi blank -blush
            mike.say "That's amazing, Lexi!"
            show fx question
            "Lexi blinks in genuine surprise."
            lexi.say "It..."
            lexi.say "It is?"
            hide fx
            mike.say "Of course it is!"
            mike.say "I've been getting the same kind of feelings for Reona too."
            mike.say "But I was worried that you'd be jealous of her."
            show lexi happy at startle
            "Lexi shakes her head, beginning to laugh."
            show lexi normal
            lexi.say "You think I'm old-fashioned or something?"
            lexi.say "I can handle having the hots for both of you."
            show lexi wink
            lexi.say "So long as you're cool with it too?"
            show lexi smile
            mike.say "Oh yeah, Lexi..."
            mike.say "I'm totally cool with the whole idea!"
            show lexi normal
            $ lexi.love += 4
            "Lexi lets out a genuine sigh of relief."
            show lexi smile
            "And I can see that her whole demeanour changes."
            "Like a massive weight was just lifted off her shoulders."
            show lexi happy
            lexi.say "Well thank fuck for that!"
            show lexi normal
            lexi.say "Now we can keep on having fun together."
            show lexi wink
            lexi.say "And by fun, I obviously mean fucking, yeah?"
            show lexi smile
            mike.say "Yeah, Lexi..."
            mike.say "I kind of guessed that's what you meant."
            hide lexi
            show lexi
            with fade
            $ Harem.join_by_name("whore", "lexi")
        "What the... You can't! It's her or me, make a decision!":
            "The moment that Lexi makes the admission, I feel myself bristle."
            "Because it's basically an admission that she loves someone else."
            "And that means a hell of a lot of her affection is directed elsewhere!"
            show lexi blank -blush
            mike.say "What's that supposed to mean, Lexi?"
            show lexi surprised
            mike.say "That you're testing us both out?"
            mike.say "Seeing which one you like the best?!?"
            show lexi annoyed
            "Lexi frowns and shakes her head."
            "Clearly she wasn't expecting me to react in this way."
            show lexi wow
            lexi.say "What?!?"
            show lexi surprised
            lexi.say "No way, [hero.name]…"
            lexi.say "It means I love the pair of you the same!"
            show lexi sadsmile
            lexi.say "Don't we all get on together?"
            lexi.say "I thought we were having a fun time?"
            hide lexi
            show lexi sad
            with fade
            "I take a step backwards, putting space between Lexi and me."
            "And by now I'm shaking my head too."
            mike.say "That's just what it was, Lexi..."
            mike.say "It was fun, not a relationship!"
            mike.say "There's enough with two of us in this one."
            mike.say "At least there is for me!"
            show lexi sadsmile
            lexi.say "What are you saying, [hero.name]?"
            show lexi sad
            mike.say "That you need to decide, Lexi..."
            mike.say "I'm saying that you need to choose between me and Reona."
            mike.say "So how about you do that, and then call me when you have."
            $ lexi.love -= 10
            hide lexi with dissolve
            $ hero.cancel_activity()
            "With that I turn my back on Lexi and walk away."
            "Still fuming on the inside that I'm not enough for her."
    return

label whore_harem_event_07_text:
    play sound cell_vibrate
    pause 1.0
    "It's a text from Reona."
    $ result = renpy.display_menu([("Ignore it", 1), ("Read it", 2)])
    if result == 1:
        $ reona.love -= 2
        return
    $ nvl_mode = "phone"
    nvl clear
    reona_nvl "Hey [hero.name]."
    reona_nvl "I kinda want to talk to ya. Mind if we meet?"
    mike_nvl "Yeah sure. When?"
    reona_nvl "Just come to me whenever you want."
    return

label whore_harem_event_07:
    show reona
    "When Reona asked me to meet up with her, I thought that she had something exciting in mind."
    "You know, like maybe she was springing a surprise date on me or had some really hot gossip."
    "But the moment that she shows up, I can tell that it's not going to be anything that's as much fun."
    "Because she has a serious look on her face, the kind that you don't often see Reona wearing."
    "So from the very beginning, I'm caught totally off-balance as I have no idea what to make of it all."
    show reona sadsmile
    reona.say "Hey, [hero.name]…"
    reona.say "Thanks for coming to meet me."
    show reona normal
    "I shrug and shake my head at this."
    "Trying as best I can to look nonchalant."
    mike.say "Hi, Reona..."
    mike.say "And it's not a problem, you know?"
    mike.say "Any chance to see you is great news!"
    "Normally Reona's a bit of a sucker for compliments."
    "So I'm looking for a smile at the very least."
    "But what I get is barely a twitch of the lips."
    show reona sadsmile
    reona.say "Erm..."
    reona.say "Yeah, [hero.name]…"
    reona.say "You might want to hear what I have to say to you."
    reona.say "Like, before you go thinking it's all fun and games!"
    show reona normal
    "Okay, so now I really am starting to worry."
    "Because Reona's not the kind of girl to overthink things."
    "So if she has something to tell me, then it's probably going to be serious."
    "But there's no way out of this, or at least none that I can see."
    "So I take a deep breath and then let it out."
    mike.say "Urgh..."
    mike.say "Okay, Reona..."
    mike.say "Don't hold back, just hit me with it!"
    "Reona nods, not looking happy about the situation either."
    show reona normal
    reona.say "Here goes..."
    reona.say "Okay, the thing is..."
    reona.say "I think that I'm in love with someone else!"
    show reona normal
    "I thought that I was ready for whatever Reona was going to say to me."
    "Or at least I told myself that I was prepared to handle it."
    "But the news hits me hard, feeling like a genuine punch to the gut."
    mike.say "You..."
    mike.say "You're in love with someone else?"
    mike.say "Oh god, Reona..."
    mike.say "I...guess that I should have seen this coming."
    mike.say "A girl as hot as you, and a guy that looks like me..."
    show reona embarrassed
    mike.say "I should have known it wasn't meant to last!"
    "Reona listens to everything that I have to say."
    "But as I keep on talking, the expression on her face starts to change."
    "It goes from one of awkward concern to genuine confusion."
    "And by the time I'm done, she's shaking her head at me."
    show reona pensive
    reona.say "What in the hell are you even talking about?"
    show reona annoyed
    reona.say "I don't want to break up with you!"
    reona.say "Whatever made you think that?!?"
    show reona sad
    "For a moment I can't make sense of what Reona's saying to me."
    "My brain just won't process the meaning of her words."
    "But then something seems to click inside of my head."
    "And the question just comes popping out of me."
    mike.say "What am I talking about?"
    mike.say "What are YOU talking about?!?"
    mike.say "You just told me you don't love me anymore!"
    show reona guilty
    reona.say "No I did not!"
    show reona sad
    mike.say "Yes you did..."
    mike.say "You said you loved someone else!"
    show reona angry
    reona.say "But I never said that didn't still love you, dummy!"
    reona.say "I love you and I love Lexi too!"
    show reona surprised blush
    reona.say "Oops..."
    show reona embarrassed
    "Even when Reona was trying to explain herself to me, I never expected that."
    "I was waiting for her to tell me she was on love with some other guy besides me."
    mike.say "Lexi?"
    mike.say "You love Lexi?!?"
    show reona sadfrustrated
    reona.say "I..."
    reona.say "I think so..."
    show reona sadsmile
    reona.say "I love you both!"
    menu:
        "That's great news then!" if "whore_harem_event_07" not in DONE or Harem.find("lexi", "whore"):
            "The moment that the words are out of Reona's mouth, everything changes."
            "Before I was worried that she was trying to tell me that it was all over."
            "But now I realise that there's nothing at all to fear about her confession."
            mike.say "But, Reona..."
            mike.say "That's great news!"
            show reona shock -blush
            reona.say "It is?"
            "I'm nodding like crazy as Reona asks the question."
            "Eager to explain to her how I see things."
            mike.say "Of course it is..."
            mike.say "Don't you see?"
            show reona embarrassed
            mike.say "We've been having so much fun with Lexi recently."
            mike.say "But this means we can take things to the next level."
            "Reona looks relieved, but also a little puzzled."
            show reona sadshock
            reona.say "You really mean that?"
            show reona sadsmile
            reona.say "I was worried that you might get jealous or something."
            mike.say "Hell no!"
            mike.say "I'm all for it."
            mike.say "We need to call Lexi up right now..."
            mike.say "Let her know that we want to make this threesome a thing!"
            show reona normal
            $ reona.love += 4
            "I can see that my enthusiasm is starting to rub off on Reona."
            "She's smiling now, warming to the idea more with each passing second."
            "And I'm pretty sure that Lexi's going to have a similar reaction too."
            "So I can't wait for the chance to tell her."
            $ Harem.join_by_name("whore", "reona")
        "Tell me you're joking...":
            "I was expecting Reona's explanation to make things better."
            "But if anything, it manages to do the exact opposite."
            "Because it's bad enough that she loves someone else."
            "Yet even worse that the person in question happens to be Lexi!"
            show reona embarrassed -blush
            mike.say "That's not how these things work, Reona!"
            mike.say "Sure, we can fool around with Lexi and have some fun."
            mike.say "But there's no room in the relationship for her."
            "Reona seems to be puzzled by my reaction to the confession."
            "Almost like she was expecting me to love the idea."
            "To be eager to allow Lexi into the relationship with us."
            show reona sadshock
            reona.say "Why are you being like this, [hero.name]?"
            if cheating_agreement in ["mc", "neither"]:
                reona.say "I thought you were open-minded?"
                mike.say "And I thought that we already talked about all of this, Reona."
                mike.say "Weren't you supposed to be changing your ways?"
                mike.say "Not being so promiscuous?"
                show reona sadangry
                "Reona looks like she's starting to get mad now."
                "And that last question really seem to set her off."
                "I can see anger beginning to blaze in her eyes."
                "But I'm not about to hang around and take the brunt of it."
            mike.say "You need to decide, Reona..."
            mike.say "Which one of us do you want?"
            mike.say "Is it going to be Lexi, or me?"
            hide reona with dissolve
            $ reona.love -= 10
            "Before she can answer, I turn on my heel and walk away."
            "Because I figure that Reona needs time to think it over."
            "That and like I already said, I'm not in the mood for a tongue-lashing right now."
    return

label whore_harem_event_08(appointment=None):
    $ renpy.dynamic(reona_score=0, lexi_score=0)
    scene bg street with fade
    "I knew that I was taking a massive gamble when I decided to take Lexi and Reona out for a meal."
    "It's not that we haven't eaten out together in the past, so the experience isn't totally new."
    "But that was just stuff like grabbing a hotdog on the way to do something else, you know?"
    "At the most I think I might have been for a coffee with Lexi and Reona and included a donut."
    "So why I thought it'd be a good idea to take a quantum leap forward in culinary terms, I haven't a clue."
    "I mean, I'm assuming the girls have eaten in an actual restaurant before tonight."
    "But with characters like Lexi and Reona, you can never be too sure."
    "All of that means I'm going to have to be on high alert while we're eating."
    "Because I don't like the idea of them showing me up in front of the other diners."
    "But perhaps I should have been a little more specific about the etiquette of timing."
    "As I'm standing around outside the restaurant, and the girls are already late!"
    "I keep on looking at the time and wondering where they can be."
    "And it's while I have my eyes on the time that I hear someone calling me."
    reona.say "Hey, [hero.name]…"
    reona.say "Are we the first ones here?"
    show reona date normal at center, zoomAt(1.25, (640, 900)) with easeinright
    "I look up to see Reona's standing in front of me, a smile on her face."
    "But just as I'm about to open my mouth and say something, I hear another familiar voice."
    show reona at center, zoomAt(1.25, (340, 900))
    show lexi date at center, zoomAt(1.25, (940, 900))
    with easeinright
    lexi.say "Hi, guys..."
    lexi.say "Hope you've not been waiting long?"
    show lexi smile
    show reona shout
    reona.say "Nah..."
    reona.say "I just got here!"
    show reona happy
    "I turn my head from side to side as Lexi and Reona talk to each other and ignore me."
    "And I can already feel myself beginning to lose the hold I had on my temper too!"
    mike.say "Maybe you two just got here."
    show reona shock
    show lexi surprised
    mike.say "But I was the only one that actually turned up on time!"
    menu:
        "Temper yourself":
            "I might be feeling pretty pissed off right now."
            "But I'm determined to make sure tonight is a success."
            "So I do the best I can to let go of my annoyance."
            mike.say "Look, guys..."
            mike.say "Let's just forget about it and have a good time, okay?"
            mike.say "You weren't so late that it cost us the reservation."
            show reona guilty
            show lexi sad
            "Lexi and Reona seem to be mollified by my efforts at making peace."
            "So much so that they each take one of my arms."
            show lexi sadsmile
            lexi.say "So what are we waiting for?"
            show lexi wink
            lexi.say "Let's get in there!"
            show reona shout
            reona.say "I'm with her, [hero.name]…"
            reona.say "My stomach's growling like a wild animal!"
            show reona happy
            "I nod and begin walking into the restaurant."
            "Feeling like I've managed to avoid them both making a scene."
        "Scold them":
            mike.say "I went to a lot of trouble to arrange all of this for you guys."
            mike.say "The least you could do is get here for the time I booked the table."
            show reona guilty
            show lexi blank
            "Lexi and Reona both look pretty annoyed at my telling them off."
            "But I feel like it's important to let them know how pissed I am right now."
            show reona sadsmile
            reona.say "Okay, okay..."
            reona.say "I'm sorry!"
            show lexi bored
            show reona normal
            lexi.say "Me too, [hero.name]..."
            lexi.say "This isn't really my kind of thing!"
            show lexi blank
            "I roll my eyes and wave for them to follow me into the restaurant."
            mike.say "Look, let's just forget about it, yeah?"
            mike.say "And try to have a nice meal."
            $ reona_score += .5
            $ lexi_score += .5
        "Scold Reona":
            "After pointing that fact out, I turn my attention to Reona."
            mike.say "You only got here a few seconds before Lexi."
            mike.say "So don't act like you're any better than her."
            show reona sad
            show lexi yawn
            "Reona shoots me a pretty harsh glare."
            "But Lexi looks relieved the attention is on someone else."
            show lexi blank
            show reona angry
            reona.say "Hey!"
            reona.say "We were both late."
            reona.say "Why'd you have to pick on me more than her?"
            show reona sadangry
            "I roll my eyes and wave for them to follow me into the restaurant."
            mike.say "Look, let's just forget about it, yeah?"
            mike.say "And try to have a nice meal."
            $ lexi_score += 1
        "Scold Lexi":
            "After pointing that fact out, I turn my attention to Lexi."
            mike.say "But you were the latest of all, Lexi!"
            mike.say "I was worried you weren't going to turn up at all."
            show lexi annoyed
            show reona normal
            "Lexi shoots me a pretty harsh glare."
            "But Reona looks relieved the attention is on someone else."
            show lexi angry
            lexi.say "Hey!"
            lexi.say "We were both late."
            lexi.say "Why'd you have to pick on me more than her?"
            show lexi annoyed
            "I roll my eyes and wave for them to follow me into the restaurant."
            mike.say "Look, let's just forget about it, yeah?"
            mike.say "And try to have a nice meal."
            $ reona_score += 1
    scene bg restaurant
    show ryan at center, zoomAt(1.25, (440, 900)), blacker
    with fade
    pause 0.1
    show lexi a smile date nophone at center, zoomAt(1.25, (1040, 880))
    show reona date at center, zoomAt(1.25, (740, 880))
    with easeinright
    "Now that we're inside the restaurant, I feel like I can start to relax."
    "Or at least I have the illusion of that being the case for a few moments."
    "Because I can already see that the maître d'hotel has an odd look on his face."
    mike.say "Erm..."
    mike.say "Hey there, fella!"
    mike.say "We have a reservation?"
    mike.say "A table for three?"
    show ryan at center, zoomAt(1.0, (440, 900)), blacker, startle(0.05,-10)
    "Waiter" "Ah, yes..."
    "Waiter" "I'm afraid there's been a slight problem, sir."
    "I can already hear Lexi and Reona behind me."
    "Reacting with mock horror to the maître d's words."
    show lexi bored a
    lexi.say "Oh-oh!"
    show lexi blank
    show reona shout
    reona.say "That doesn't sound like good news!"
    show reona sad
    "I wave for the girls to keep quiet."
    mike.say "Will you guys shut up for a second?"
    "And then I turn my attention back to the maître d'hotel."
    mike.say "A problem?"
    mike.say "What kind of problem?"
    "Waiter" "There was an error with the reservation system earlier today."
    "Waiter" "Basically all of the information was lost."
    "Waiter" "We're still able to offer you one of our best tables."
    "Waiter" "But I'm afraid you will have to wait a little while longer."
    "I can't believe what I'm hearing."
    "After going to all the trouble of booking a table."
    "That and making sure that we got here in good time."
    "Now I'm being told that we're going to have to wait longer!"
    menu:
        "Try to get a table faster":
            "I'm about to say something I'll probably regret."
            "But then a thought occurs to me."
            mike.say "Wait a minute..."
            mike.say "If the reservations all got lost..."
            mike.say "Then you can just as easily skip us to the front of the queue, right?"
            show lexi smile
            show reona happy
            "Lexi and Reona are leaning in as I say all of this."
            "And they begin nodding as soon as they hear my argument."
            "Waiter" "I..."
            "Waiter" "I don't know about that..."
            if hero.charm >= 70:
                "The maître d'hotel looks like he's thinking about it."
                "And then he raises his eyebrows and shrugs."
                "Waiter" "I suppose you're right, sir..."
                "Waiter" "And the whole thing is also our fault."
                "Waiter" "Getting you seated as soon as possible is the least we can do."
                "Without another word, he motions for us to follow."
                "Then he leads us to what looks like a pretty good table."
                hide ryan at center, zoomAt(1.25, (440, 900)), blacker
                show lexi a smile at center, zoomAt(1.25, (840, 880))
                show reona happy at center, zoomAt(1.25, (540, 880))
                with easeoutleft
                "Once he leaves us to sit down, I can see Lexi and Reona are impressed."
                show reona shout
                reona.say "That was pretty smooth, [hero.name]."
                show reona happy
                show lexi normal
                lexi.say "Check out your silver tongue!"
                show lexi smile
                $ reona_score += 1
                $ lexi_score += 1
            else:
                "For a moment it looks like the maître d'hotel is going to concede defeat."
                "But then he shakes his head at me, and I can see he's not convinced."
                "Waiter" "I'm sorry, sir..."
                "Waiter" "But you're just going to have to wait like everyone else."
                "He motions towards some seats in the small lobby."
                "And the three of us have no choice but to do as he says."
                "So we trudge over to the seats and slump down."
                "Then we wait in silence to be called to our table."
        "Indignant yourself":
            mike.say "Are you serious?!?"
            "The maître d'hotel doesn't even dignify that with an answer."
            "Instead all he offers me is a shrug and a neutral smile."
            "But it's Lexi that chimes up first."
            show lexi normal
            lexi.say "Oh look, they've got a little bar over there!"
            lexi.say "We can grab a drink while we wait."
            show lexi smile
            show reona sad
            "As if doing so on purpose, Reona instantly disagrees."
            show reona shout
            reona.say "No way, Lexi..."
            reona.say "I'm way too hungry!"
            show reona sad
            menu:
                "Offer to go at the bar and get nibbles":
                    "I turn to the girls, eager to reassure them both."
                    mike.say "I don't think we'll be waiting long for the table."
                    mike.say "But in the meantime we can go sit at the bar."
                    mike.say "That way you can get a drink, Lexi."
                    mike.say "And I'm sure they'll have some snack or nibbles too."
                    mike.say "So that should take care of you as well, Reona."
                    show lexi smile
                    show reona happy
                    "The girls look at each other and then back at me."
                    "And much to my relief, they both nod in agreement."
                    show lexi normal
                    lexi.say "Sounds good!"
                    show lexi smile
                    show reona shout
                    reona.say "So let's go!"
                    show reona happy
                    "Now that everyone's happy, we can walk over to the bar."
                    "As I know that I'll feel better once I have a drink in my hand!"
                    $ reona_score += .5
                    $ lexi_score += .5
                "Offer to wait at the bar":
                    "I turn to Lexi, eager to reassure her."
                    mike.say "Don't worry, Lexi..."
                    mike.say "We can get go sit at the bar while we wait."
                    mike.say "And we can grab a couple of drinks over there."
                    "Lexi seems to be satisfied with this."
                    "As she nods and doesn't complain any more."
                    "But the same can't be said for Reona."
                    show reona shout
                    reona.say "That's fine for her..."
                    reona.say "But what about me?"
                    reona.say "I want something to eat!"
                    show reona sad
                    "I shake my head at this."
                    mike.say "God, Reona..."
                    mike.say "You can wait a couple of minutes, can't you?"
                    mike.say "It's not like you're going to starve, is it?"
                    "Reona doesn't reply to the question."
                    "Instead she mutters under her breath as we walk to the bar."
                    $ lexi_score += 1
                "Offer to get nibbles":
                    "I turn to Reona, eager to reassure her."
                    mike.say "Don't worry, Reona..."
                    mike.say "We can get them to bring us something while we wait."
                    mike.say "Maybe some breadsticks or a couple of rolls?"
                    show reona happy
                    show lexi sad
                    "Reona seems to be satisfied with this."
                    "As she nods and doesn't complain any more."
                    "But the same can't be said for Lexi."
                    show lexi bored
                    lexi.say "That's fine for her..."
                    lexi.say "But what about me?"
                    lexi.say "I want a damn drink!"
                    show lexi sad
                    "I shake my head at this."
                    mike.say "God, Lexi..."
                    mike.say "You can wait a couple of minutes, can't you?"
                    mike.say "Or are you an alcoholic?"
                    "Lexi doesn't reply to the question."
                    "Instead she mutters under her breath."
                    $ reona_score += 1
                "Stay put as long as you don't get a table":
                    "I hardly hear what the girls are saying."
                    "And that's because I'm still pissed at the restaurant losing our reservation."
                    mike.say "Oh no..."
                    mike.say "We're not going anywhere."
                    mike.say "Not until we get our table!"
                    "But the maître d'hotel doesn't seem to be at all impressed with my defiance."
                    "He just shakes his head, dismissing my efforts."
                    "Waiter" "I'm sorry, sir..."
                    "Waiter" "But you're just going to have to wait like everyone else."
                    "He motions towards some seats in the small lobby."
                    "And the three of us have no choice but to do as he says."
                    "So we trudge over to the seats and slump down."
                    "Then we wait in silence to be called to our table."
    scene restaurant_meal_bg_pose01
    show reona date at center, zoomAt(1.65, (340, 1040))
    show lexi a smile date nophone at center, zoomAt(1.65, (940, 1040))
    show drink_table_pub_victor
    show drink_room_fg_pub
    with fade
    "The maître d'hotel is at least true to his word, as we're soon seated"
    "And now that Lexi and Reona have menus in their hands, things can only get better."
    show lexi blank
    show reona sadsmile
    "But as they scan the list of dishes on offer, the girls start to look confused."
    show lexi surprised
    lexi.say "What is this, [hero.name]..."
    lexi.say "Some kind of a joke?"
    show lexi blank
    "The question seems so odd that I look up from my own menu instantly."
    mike.say "Huh?"
    mike.say "What's that supposed to mean?"
    show reona devious
    "Luckily for me, Reona steps in to explain the problem."
    "And she does so in a more diplomatic manner than Lexi would have too."
    show reona shout
    reona.say "Most of the menu is in French, [hero.name]."
    reona.say "So I'm finding it hard to understand too."
    show reona sadsmile
    menu:
        "Heureusement que je parle français !" if locale.getlocale()[0] and locale.getlocale()[0].startswith('fr'):
            "I wave a hand in the air to dismiss their concerns."
            mike.say "Don't worry about it..."
            mike.say "I speak fluent French!"
            show lexi surprised
            show reona surprised
            "Lexi and Reona both seem impressed by this revelation."
            "And they don't hesitate to tell me what they'd like to eat."
            show reona shout
            reona.say "I like the look of the muscles, yeah?"
            show reona happy
            show lexi blank
            lexi.say "Hmm..."
            show lexi normal
            lexi.say "I dunno about all this fancy shit!"
            lexi.say "So I'll just have some chicken."
            show lexi smile
            "I nod, scanning the menu for what the girls want."
            show restaurant_meal_waiter_pose01 as waiter zorder 1 at flip, center, zoomAt (1.3, (1040, 840)) with easeinright
            "Then I motion for the waiter and translate it as best I can."
            mike.say "The ladies would like this..."
            mike.say "And one of these..."
            mike.say "That one for me, okay?"
            "Waiter" "Very good, sir."
            "The waiter nods, collects the menus and then walks away."
            hide restaurant_meal_waiter_pose01 as waiter zorder 1 at flip with easeoutright
            "We chat for a while, talking about this and that."
            "And the food turns up surprisingly quickly."
            show lexi happy
            lexi.say "Oh man..."
            show lexi normal
            lexi.say "That looks good."
            show lexi smile
            show reona happy
            reona.say "Mmm..."
            show reona shout
            reona.say "It smells good too!"
            show reona happy
            "I'm sure that we're about to enjoy an exceptionally nice meal."
            "So I don't hesitate to dig into the contents of my plate."
            "And I see that the girls are doing the same thing."
            if hero.knowledge >= 70:
                "Lexi looks up from her plate, a look of amazement on her face."
                show lexi normal
                lexi.say "Fuck me..."
                lexi.say "This is amazing!"
                lexi.say "It's almost better than sex!"
                show lexi smile
                "Reona looks over at Lexi's plate with interest."
                "But I notice that she doesn't stop eating."
                show reona shout
                reona.say "You should try the muscles, Lexi..."
                reona.say "They're the best I've ever had!"
                show reona happy
                show lexi blank
                "Lexi looks at the shellfish with a frown on her face."
                "And I get the impression that she's not a fan of the stuff."
                show lexi normal
                lexi.say "Nah, you're okay."
                lexi.say "I'm not taking up space with anything else."
                lexi.say "Not while I have more of this on my plate!"
                show lexi smile
                "I'm listening in on the conversation with obvious interest."
                "Already congratulating myself on the quality of my choices."
                mike.say "So..."
                mike.say "You like what I chose for you?"
                "The question gets me a round of eager nods."
                "But not a single word of approval."
                "Because the girls are still eating their meals."
                "And they probably won't speak again until they're done."
                $ reona_score += 1
                $ lexi_score += 1
            else:
                show lexi blank
                "Lexi looks up from her plate, a frown on her face."
                show lexi bored
                lexi.say "Huh..."
                lexi.say "This chicken's weird."
                lexi.say "Like, it's kinda rubbery!"
                show lexi sad
                show reona embarrassed
                "Reona looks over Lexi's plate."
                "And as she does so, I notice she's pushing her own food about too."
                show reona sadfrustrated
                reona.say "Yeah, I see that..."
                reona.say "And the shells of these muscles are strange too."
                reona.say "They're in a spiral shape!"
                show reona sad
                "Lexi sticks her tongue out as she scans Reona's plate."
                show lexi surprised
                lexi.say "Eww!"
                lexi.say "Those are snails!"
                "Reona pushes the plate away from herself."
                show reona surprised
                reona.say "WHAT!"
                "She returns the favour, leaning over Lexi's plate."
                reona.say "Well those look like a frog's legs to me!"
                lexi.say "Oh man, I think I'm going to puke!"
                "I can feel myself beginning to blush."
                mike.say "Ah..."
                mike.say "I must have made a mistake when I read the menu!"
                show reona angry
                show lexi angry
                "I can almost feel the glares that Lexi and Reona throw my way."
                "And it's all I can do to look down at my own plate and keep on eating."
                "Which is a shame, because I seem to have managed to order myself something nice at least!"
        "We'll have to make it without speaking French...":
            "I'm guessing that Lexi and Reona don't speak French."
            "And I don't know much more than how to order a coffee myself."
            "So it looks like I'm going to have to come up with a solution."
            "One that I hope will satisfy everyone."
            menu:
                "Confess to the waiter you don't speak French":
                    "I figure that someone's got to throw themselves on the proverbial grenade here."
                    show restaurant_meal_waiter_pose01 as waiter zorder 1 at flip, center, zoomAt (1.3, (1040, 840)) with easeinright
                    "So I call the waiter over, putting a helpless smile on my face as I do so."
                    "Then I speak to him behind my hand, making it look like I don't want the girls to hear me."
                    mike.say "Erm..."
                    mike.say "Look, buddy..."
                    mike.say "I said I'd order for the ladies, chicken and the muscles, right?"
                    mike.say "But I can't make head nor tail of the menu!"
                    mike.say "Like, it's all Greek to me!"
                    "The waiter raises an eyebrows an snorts in amusement."
                    "Waiter" "I think you'll find that's French, sir!"
                    "Waiter" "Allow me..."
                    "The waiter seems to take great pleasure in pointing out the dishes."
                    hide restaurant_meal_waiter_pose01 as waiter zorder 1 at flip with easeoutright
                    "And then he disappears to take the orders to the kitchen."
                    "Sure, I feel kind of humiliated by the treatment."
                    "But it's worth it to see Lexi and Reona's faces light up when their food arrives."
                    "They both attack their meals, making me feel justified in playing dumb to make it happen."
                    $ reona_score += 1
                    $ lexi_score += 1
                "Order \"Coq au Vin\" for everyone":
                    show restaurant_meal_waiter_pose01 as waiter zorder 1 at flip, center, zoomAt (1.3, (1040, 840)) with easeinright
                    mike.say "All three of us will have that."
                    "Waiter" "Le \"Coq au Vin\" ?"
                    "Waiter" "An excellent choice, sir."
                    hide restaurant_meal_waiter_pose01 as waiter zorder 1 at flip with easeoutright
                    "With that he hurries away."
                    show reona angry
                    reona.say "Hey, I didn't want chicken!"
                    show reona sad
                    show lexi normal
                    lexi.say "Oh come on, reona..."
                    lexi.say "I bet you'll love them."
                    show lexi smile
                    "I figure that two out of three isn't that bad."
                    "So I try to make the most of the situation."
                    mike.say "Sorry, Reona..."
                    mike.say "Looks like we're all having chicken!"
                    "When the food arrives, I dig straight into it."
                    "Partly because it looks and smells great."
                    "But also as it gives me an excuse not to look up at Reona."
                    "Because she's glaring at me as she picks at her own plate."
                    $ lexi_score += 1
                "Order \"Moules à la provençale\" for everyone":
                    show restaurant_meal_waiter_pose01 as waiter zorder 1 at flip, center, zoomAt (1.3, (1040, 840)) with easeinright
                    mike.say "All three of us will have that."
                    "Waiter" "Les \"Moules à la provençale\" ?"
                    "Waiter" "An excellent choice, sir."
                    hide restaurant_meal_waiter_pose01 as waiter zorder 1 at flip with easeoutright
                    "With that he hurries away."
                    show lexi angry
                    lexi.say "Hey, I didn't want muscles!"
                    show lexi sad
                    show reona shout
                    reona.say "Oh come on, Lexi..."
                    reona.say "I bet you'll love them."
                    show reona happy
                    "I figure that two out of three isn't that bad."
                    "So I try to make the most of the situation."
                    mike.say "Sorry, Lexi..."
                    mike.say "Looks like we're all having muscles!"
                    "When the food arrives, I dig straight into it."
                    "Partly because it looks and smells great."
                    "But also as it gives me an excuse not to look up at Lexi."
                    "Because she's glaring at me as she picks at her own plate."
                    $ reona_score += 1
                "Order \"Bœuf bourguignon\" for everyone":
                    show restaurant_meal_waiter_pose01 as waiter zorder 1 at flip, center, zoomAt (1.3, (1040, 840)) with easeinright
                    mike.say "All three of us will have that."
                    "Waiter" "Le \"Boeuf bourguignon\" ?"
                    "Waiter" "An excellent choice, sir."
                    hide restaurant_meal_waiter_pose01 as waiter with easeoutright
                    "With that he hurries away."
                    show lexi angry
                    lexi.say "Hey, I didn't want steak!"
                    show lexi sad
                    show reona angry
                    reona.say "I wanted the muscles!"
                    show reona sad
                    mike.say "Sorry guys..."
                    mike.say "Looks like we're all having steak!"
                    "When the food arrives, I dig straight into it."
                    "Partly because it looks and smells great."
                    "But also as it gives me an excuse not to look up at Lexi and Reona."
                    "Because they're both glaring at me as they pick at their own plates."
    "As this is a more upmarket sort of establishment, I was expecting smaller portions."
    "But as I plough through my meal, I have to admit that it's becoming a challenge."
    "And the stingy git in me is starting to worry that I won't be able to finish it."
    "Normally I'd just give up and ask the waiter for a doggy-bag."
    "The only problem is that I'm worried that'll make him look down his nose at me."
    "I feel like the only answer is a final push to clean my plate."
    "One last, monumental effort to polish the lot off before I have to surrender."
    "So I get down to it, shovelling away as fast as I can."
    show reona shock
    reona.say "Whoa..."
    reona.say "Slow down, [hero.name]!"
    show lexi surprised
    lexi.say "Fucking hell..."
    lexi.say "He's really going for it!"
    if hero.hunger <= 4 or hero.has_skill("iron_stomach"):
        "I feel like I've set a genuine challenge for myself."
        "One that would be almost impossible for the unprepared."
        "Or maybe a lesser mortal than me!"
        "But I know that I can handle something like this."
        "So I steel myself and keep right on going."
        "Little by little the contents of my plate are thinned out."
        "And I can see the end of my task coming ever closer."
        "Sure, I feel like my eyes must be popping out of their sockets."
        "And it's as though I can count every drop of sweat squeezing out of my pores too!"
        "But at the same time I can also feel the reserves of stamina I still have left."
        "So it's these that I draw upon when the final push is upon me."
        "And before I know it, I'm finishing off the very last morsel."
        mike.say "Aaah..."
        mike.say "That's better..."
        mike.say "All finished!"
        "Lexi and Reona look at me with amazement in their eyes."
        reona.say "You must have hollow legs or something!"
        lexi.say "How'd you do that, [hero.name]?"
        lexi.say "I was sure you were gonna burst back there!"
        $ reona_score += .5
        $ lexi_score += .5
    else:
        "Lexi's right, I'm putting everything into this."
        "Trying as hard as I can to eat every last morsel of food."
        "But I'm already starting to feel the effects of the task."
        "I don't know what my face looks like right now."
        "But I feel like my eyes must be popping out of their sockets."
        "And it's as though I can count every drop of sweat squeezing out of my pores too!"
        "I do the best I can to dig down in the hope of finding a reserve of stamina."
        "Or even for the sheer force of will needed to make my body keep on going."
        "But it's no good, as I end up slumping in my seat."
        "In fact it's a minor miracle I don't end up face-down in my dinner."
        mike.say "Urgh..."
        mike.say "It's no good..."
        mike.say "I need a doggy-bag!"
        show lexi annoyed
        show reona annoyed
        "Lexi and Reona look at me with disapproval in their eyes."
        show reona shout
        reona.say "Then why not just ask for one?"
        show reona normal
        show lexi angry
        lexi.say "Urgh..."
        lexi.say "You'd better not puke on the table!"
        show lexi annoyed
    show reona normal
    show lexi smile
    with fade
    "Once the waiter takes away the empty plates, we have a chance to chat."
    "A few moments to catch our breath and enjoy each other's company."
    "And hopefully let the food we've just eaten digest properly too."
    if Harem.together("lexi", "reona", name='whore'):
        mike.say "We really should do this kind of thing more often, you know?"
        mike.say "Spending real quality time together, doing proper adult stuff."
        "Part of me is expecting this notion to be shot down in flames."
        "Maybe if not by Reona then definitely by Lexi."
        "As she's usually the one that wants to have outrageous fun."
        "And to hell with the consequences."
        "But instead they both start nodding eagerly."
        show reona shout
        reona.say "Makes sense to me."
        show reona happy
        show lexi normal
        lexi.say "Me too, you know..."
        lexi.say "Now that we're more serious?"
        show lexi smile
        "As soon as the words are out of her mouth, Lexi claps a hand over it."
        "And to make things even more suspicious, she shoots a glance at Reona."
        "Who rolls her eyes and then shakes her head."
        show reona shout
        reona.say "Way too go, Lexi..."
        reona.say "We kind of have to tell him now!"
        show reona happy
        mike.say "Tell me what?"
        mike.say "What's all this about?"
        show reona shout
        reona.say "Lexi knows that I told you I love you both."
        reona.say "And I know that she told you the same thing too."
        show reona normal
        show lexi normal
        lexi.say "But that's a good thing, right?"
        lexi.say "It means we're all on the same page."
        show lexi blank
        "My initial surprise is quickly fading as I get up to speed with the situation."
        "But as I do, I find myself nodding."
        mike.say "You're right, Lexi..."
        mike.say "It is a good thing."
        mike.say "Because it means that we're coming together as a trio."
        mike.say "And I have to say, I love both of you too!"
        show reona happy
        show lexi smile
        "Reona and Lexi are all smiles now."
        "And the next thing I know, we're all holding hands around the table."
        "Everyone's looking each other in the eye and beaming with happiness."
        "Because I guess we just kind of made it official without a formal declaration."
        "Lexi, Reona and I are in love with each other."
        "And it looks like we're going to see how far this we can take this thing."
        $ reona_score += 2
        $ lexi_score += 2
    else:
        "Our privacy is interrupted a moment later when the waiter returns."
        "But he only hangs around long enough to hand over the bill and then he leaves."
        "I open the fancy leather folder it's inside of, and then I let out a gasp."
        "One that's loud enough to get Lexi and Reona's attention."
        show reona annoyed
        reona.say "Oh no..."
        reona.say "That doesn't sound good!"
        show reona sad
        show lexi surprised
        lexi.say "Don't keep us in suspense, [hero.name]..."
        lexi.say "What's the damage?"
        show lexi sad
        "Rather than say it out loud, I hand over the bill."
        "And then it's their turn to whistle and stare."
        mike.say "Yeah..."
        mike.say "Now you get it!"
        show lexi surprised
        lexi.say "We just ate the food..."
        lexi.say "We didn't want to buy the whole restaurant!"
        show lexi sad
        show reona shock
        reona.say "Oh man..."
        reona.say "I had no idea it'd be that expensive!"
        show reona sadshock
        "I shrug and reach for my wallet."
        mike.say "I was the one that booked the table here."
        mike.say "So I should be the one to foot the bill."
        "Lexi and Reona both seem to be less than enthused with my suggestion."
        show reona angry
        reona.say "Don't you think that's a little old-fashioned?"
        reona.say "Like, we're supposed to be equals in this relationship!"
        show reona sadangry
        show lexi surprised
        lexi.say "What are you guys even talking about?"
        show lexi angry
        lexi.say "We need to stick it to these stuck-up pricks."
        lexi.say "Let's make a run for it!"
        show lexi smile
        "I can see that Reona's thrilled by Lexi's suggestion."
        "But it still looks like the final decision is going to come down to me."
        menu:
            "Lexi's right, let's run!":
                mike.say "Ah, fuck it..."
                mike.say "Let's live for once!"
                "I slowly stand up and push my chair back under the table."
                "First Lexi catches onto what I'm doing and copies me."
                "But it takes both of us gesturing to Reona for her to get it."
                "Though when she does, she almost blows it for us by leaping to her feet."
                lexi.say "Act casual!"
                reona.say "Oh..."
                reona.say "Okay, okay!"
                "As nonchalantly as possible, we start walking towards the door."
                "But once we're halfway there, something in me seems to snap."
                mike.say "Run for it!"
                "All of a sudden, we're racing towards the door."
                "Lexi, Reona and I scramble to get out of the place."
                scene bg street
                "And once we're in the street, we break into a run."
                "We don't stop until we're a safe distance from the restaurant."
                "Then we duck into an alley, panting for breath, still high on adrenaline."
                $ reona_score += .5
                $ lexi_score += .5
            "Reona's right, let's split the bill":
                mike.say "You're right, Reona..."
                mike.say "We should split the bill three ways."
                "Reona nods at this, happy to have been listened too."
                show lexi annoyed
                "But Lexi looks more than a little annoyed."
                "Nevertheless she still pays up her share."
                "And I can only hope that she realises this is for the best."
                "Because it's a chance for us all to behave like responsible adults."
                $ reona_score += 1
            "Let's pay only what's worth paying for":
                mike.say "I think Lexi's got a point..."
                mike.say "But maybe we can make it in a more subtle way?"
                show lexi smile
                "Lexi looks interested in what I have to say."
                "But Reona merely seems to be listening for the sake of it."
                lexi.say "What are you talking about?"
                mike.say "I say we pay what we feel the food was worth."
                lexi.say "That's a great idea..."
                lexi.say "We should do that!"
                "So that's exactly what we do."
                "This seems to make Lexi very happy."
                "But the same thing can't be said for Reona."
                "Though she chooses to keep her feelings on the matter to herself."
                $ lexi_score += 1
            "I'll pay for everything":
                "I shake my head and continue getting out my wallet."
                "Then I count out the correct amount to settle the bill."
                mike.say "No way, guys..."
                mike.say "I'm covering this, and that's all there is to it."
                show lexi blank
                show reona sadfrustrated
                "Lexi and Reona don't argue the point any further."
                "But I can tell neither of them is happy."
                "Still I feel justified in what I'm doing."
                "So I do the best I can to ignore their disapproval."
    scene bg street with fade
    show lexi a smile date at center, zoomAt(1.25, (840, 880))
    show reona happy date at center, zoomAt(1.25, (440, 880))
    with easeinleft
    "On the walk back from the restaurant, I feel the need to raise a certain subject."
    mike.say "So..."
    mike.say "I had a really great time tonight."
    mike.say "So good in fact, that I'm not ready to call it quits just yet."
    mike.say "How about you guys?"
    if reona_score >= lexi_score >= 3:
        show lexi normal
        lexi.say "I'm not quitting yet!"
        lexi.say "Let's go do something fun, yeah?"
        show lexi smile
        show reona shout
        reona.say "Me neither..."
        reona.say "We should go do something else."
        show reona happy
        "I feel a surge of positive energy as the girls answer me."
        "Both as it means we're not done for the night."
        "And that I've managed to show them both a good time tonight."
        "So just like before, I find them each taking one of my arms."
        "Then we walk on together, discussing what to do next."
        call whore_harem_event_08_sex from _call_whore_harem_event_08_sex
    elif lexi_score >= 3 > reona_score:
        show lexi normal
        lexi.say "I'm not quitting yet!"
        lexi.say "Let's go do something fun, yeah?"
        show lexi smile
        show reona shout
        reona.say "You know what..."
        reona.say "I'm feeling kind of tired."
        show reona sad
        "Reona gives Lexi and I a wave."
        hide reona with easeoutleft
        "And then she walks off."
        "Presumably starting on her way home."
        "So Lexi and I share a shrug."
        "And then we start trying to figure out what to do next."
    elif reona_score >= 3 > lexi_score:
        show reona shout
        reona.say "Me neither..."
        reona.say "We should go do something else."
        show reona sad
        show lexi sadsmile
        lexi.say "Nah..."
        lexi.say "I could do with getting some sleep!"
        show lexi blank
        "Lexi gives Reona and I a wave."
        hide lexi with easeoutleft
        "And then she walks off."
        "Presumably starting on her way home."
        "So Reona and I share a shrug."
        "And then we start trying to figure out what to do next."
    else:
        "Lexi and Reona share a look that seems to speak volumes."
        "Like they're both trying to be nice in order to spare my feelings."
        show reona shout
        reona.say "You know what..."
        reona.say "I'm feeling kind of tired."
        show reona sad
        show lexi bored
        lexi.say "Me too..."
        lexi.say "I could do with getting some sleep."
        show lexi blank
        "I feel like I'm being let down gently."
        "But there's really nothing I can do about it."
        mike.say "Oh..."
        mike.say "Okay, guys..."
        mike.say "I'll see you soon, I guess."
        hide lexi
        hide reona
        with easeoutleft
        "With that, we split up and go our separate ways."
        "And all the way home I'm trying to figure out what I did wrong."
    return

label whore_harem_event_08_sex:
    show lexi a smile date nophone at center, zoomAt(1.25, (840, 880))
    show reona happy date at center, zoomAt(1.25, (440, 880))
    "It doesn't take me long to figure out just what Lexi and Reona have in mind."
    show lexi a flirt at center, traveling(1.5, 1.0, (840, 1040))
    show reona flirt at center, traveling(1.5, 1.0, (440, 1040))
    "Almost as soon as we've made the decision to prolong the date, they start getting touchy feely with me."
    "With one of them on each arm, they lean in close and are soon running their hands over my body."
    "And I know that there's a million exciting or dangerous places that I could take them to make it happen."
    "But I guess my brain's on autopilot, overwhelmed with the notion of letting them have their way with me."
    "Because I hail a taxi and tell the driver to take us back to my place without even thinking."
    "That's how we come to be staggering up the path to the house, giggling and telling each other to be quiet."
    scene bg bedroom1
    with fade
    "I hastily let everyone in and usher them straight towards my bedroom door."
    "Because I have no idea if Bree and Sasha are in the house right now."
    "But I figure that if we start making a noise inside of my bedroom, then I at least have some kind of excuse."
    "As it means we'll be getting noisy behind a closed door."
    "Though Lexi and Reona seem determined to undermine my efforts every step of the way."
    mike.say "Shhh!"
    mike.say "You guys have to keep quiet."
    "I say this as I'm closing the door behind us."
    show lexi a smile date nophone at center, zoomAt(1.25, (840, 880))
    show reona happy date at center, zoomAt(1.25, (440, 880))
    with fade
    "And then I turn to see Lexi and Reona standing by my bed."
    show reona shout
    reona.say "Yeah..."
    reona.say "I don't think that's going to happen!"
    show reona happy
    show lexi normal
    lexi.say "She's right, [hero.name]..."
    lexi.say "I'm gonna scream for all I'm worth."
    lexi.say "And so are you!"
    show reona underwear
    show lexi a smile underwear
    with dissolve
    "As if to show that they're serious, Lexi and Reona begin to strip off their clothes."
    "But as they do so, they also make exaggerated gasping and moaning sounds too."
    "Every piece of clothing that comes off is accompanied by almost orgasmic noises."
    "And I'm sure that under any other circumstances, I'd be laughing my ass off."
    "Instead I find myself hurrying across the room, waving my arms at the pair of them."
    mike.say "Shhh!"
    mike.say "You're going to get us caught!"
    mike.say "Then nobody's going to get what they want!"
    show reona naked
    show lexi naked
    with dissolve
    "Now I should mention that neither Lexi nor Reona are wearing an overabundance of clothing tonight."
    "Which explains why they're both naked by the time I close the few metres of space between us."
    "It also helps to explain how they're more than ready for me too, and able to put their plan into action."
    "As I reach them, Lexi and Reona pounce on me from two sides, pulling at my clothes."
    mike.say "Hey..."
    mike.say "What are you..."
    mike.say "What are you doing?!?"
    show lexi normal
    lexi.say "Geez..."
    lexi.say "And you were telling us to be quiet!"
    show lexi smile
    show reona shout
    reona.say "Just relax, [hero.name]..."
    reona.say "We're only getting you naked too!"
    show reona happy
    "About halfway through the process of being stripped naked, I have a revelation."
    "I realise that I'm a complete moron for even trying to offer a shred of resistance."
    "And from that moment on, I simply stand there and let the girls have their way with me."
    "Soon enough I see the wisdom of my choice, as the last of my clothes are neatly removed."
    "And only then do I take the chance to make a move of my own."
    menu:
        "Fuck Lexi":
            "Taking advantage of the fact the girls are distracted, I reach out."
            hide reona
            hide lexi
            show lexi kiss naked
            with fade
            $ lexi.flags.kiss += 1
            "And I take a firm hold of Lexi, pulling her towards me and into my embrace."
            "She's taken totally by surprise, and so doesn't have any time to react."
            "But the only problem is that I've thrown all of my weight into catching her."
            "Which mean that I'm left totally off-balance, and in the process of toppling over!"
            show whore doggy bedroom with vpunch
            mike.say "Ah shit!"
            lexi.say "Whoa!"
            with vpunch
            "Lexi clings onto me as we both fall, pressing her body against mine."
            "Luckily it's the bed that breaks our fall, rather than the floor."
            "Lexi lands on her back with me atop her, but she doesn't break her hold."
            "Instead she clings onto me with even more determination than before."
            "I feel her legs wrapping around my waist, pulling me closer still."
            "And we've also managed to land in a very fortuitous position too."
            "At least in terms of what's going on below the waist."
            "Lexi wriggles and squirms beneath me as I lie atop her on the bed."
            "But there's no hint of her trying to get away."
            "Rather she's doing it in order to make me aware of where something is right now."
            "Something that's been getting bigger ever since we all started getting naked."
            "And now it's more than ready to do the business."
            lexi.say "Hello..."
            lexi.say "Is that someone knocking at the door?"
            lexi.say "You want to come inside?"
            show whore doggy vaginal onlexi at stepback(speed=0.1, h=-10, v=-5)
            "For all of Lexi's squirming, I'm moving atop her too."
            "Because I can already feel just how slick she is down there."
            "And so there's really no hope of me replying in a suave or nonchalant manner."
            mike.say "You bet I want to get in there, Lexi!"
            "Lexi giggles with glee at my enthusiasm, doing all that she can to make it happen."
            "But with no barriers of any kind between us, it really doesn't take all that long."
            "The token resistance that her pussy puts up soon begins to fade away to nothing."
            "Which means that I can start sinking slowly into her."
            show whore doggy vaginal onlexi at stepback(speed=0.1, h=-10, v=-5)
            "I push deeper with every passing second, not holding back at all."
            "And every inch of me that Lexi swallows seems to make her more determined still."
            "Once I'm as deep as I can go, I pause for a moment, enjoying the sensation."
            "Which is when Reona leans over from behind, planting he lips over Lexi's own."
            "They kiss right in front of me, with a genuine passion and hunger."
            "But far from making me envious, the sight is what starts me moving inside Lexi."
            "I feel a deep and irresistible passion building up in me."
            show whore doggy vaginal onlexi at stepback(speed=0.1, h=-10, v=-5)
            "And I can't hold back, moving ever faster with every breath I take."
            "This means that now Lexi is clinging onto me with her legs."
            "But she's also reaching out to hold onto Reona with her arms at the same time."
            "Not that the other girl is showing her any mercy."
            "Reona keeps on kissing Lexi, and her hands explore everywhere too."
            "I watch as she caresses Lexi's breasts, squeezing and pinching her nipples."
            "And I can feel the effect it's having on her body too."
            "As Reona plays with Lexi, the muscles of her pussy twitch."
            "They also contract around my cock, making me gasp at the sensation."
            show whore doggy at stepback(speed=0.1, h=-10, v=-5)
            pause 0.2
            show whore doggy at stepback(speed=0.1, h=-10, v=-5)
            pause 0.2
            show whore doggy at stepback(speed=0.1, h=-10, v=-5)
            "Once, twice, and then a third time I feel like I'm going to lose it."
            "Then I feel Lexi squeeze me like a fist, and I know that's going to do the job."
            "As though I'm being swept along by a massive wave, I feel myself starting to cum."
            menu:
                "Cum inside":
                    "Still tangled up in Lexi's legs, I simply keep on going."
                    "Thrusting in and out until the very last moment that I can."
                    with hpunch
                    "And then I let it happen, holding nothing back."
                    show whore doggy vaginal creampie with hpunch
                    "I fill Lexi with everything that I have to give."
                    show whore doggy closed with hpunch
                    "Her back bends and she begins cum too."
                    "But she's pinned down my Reona and myself."
                    "Which means that there's no escaping for even a moment."
                "Pull out":
                    "For the first time since this started, I struggle to free myself."
                    show whore doggy at stepback(speed=0.1, h=-10, v=-5)
                    "Not totally, but merely enough to be able to move a certain part of my body."
                    "And when I have the space I need, I don't hesitate to do so."
                    show whore doggy out at stepback(speed=0.1, h=-10, v=-5)
                    "I pull out of Lexi with a sudden jerk, making her arch her back beneath me."
                    show whore doggy out up
                    pause 0.2
                    show whore doggy down
                    pause 0.2
                    show whore doggy up
                    pause 0.2
                    show whore doggy down
                    "And from what I can see, she begins to cum almost the same moment it's done."
                    show whore doggy out down
                    pause 0.2
                    show whore doggy up
                    pause 0.2
                    show whore doggy down
                    pause 0.2
                    show whore doggy up
                    pause 0.2
                    show whore doggy down cumshot cum with hpunch
                    "Riding out her orgasm as I shoot my load over her exposed belly."
            $ lexi.sexperience += 1
        "Fuck Reona":
            "Taking advantage of the fact the girls are distracted, I reach out."
            hide lexi
            hide reona
            show reona kiss naked
            with fade
            $ reona.flags.kiss += 1
            "And I take a firm hold of Reona, pulling her towards me and into my embrace."
            "Part of me is expecting her to be taken by surprise."
            "Maybe even to fall over backwards and take me with her."
            "But to my surprise, Reona seems to anticipate the move."
            "Instead of being caught off-guard, she simply returns my embrace."
            "And then she allows herself to be slowly lowered down and onto the bed."
            "I follow her down every step of the way, matching her movements."
            "This means that our bodies come together in a graceful motion."
            "One that only comes to an end once we're laid on the bed."
            show whore reverse cowgirl raising up mike_bedroom with fade
            "And when we are, Reona looks up at me with a smile on her face."
            reona.say "So?"
            reona.say "What are you waiting for, a written invitation?"
            reona.say "Fuck me already!"
            "And just like that I'm snapped out of my romantic trance and back into reality!"
            "But that's not to say that Reona's demands are a mood-killer, not in the slightest."
            "Because my response is to line myself up and instantly get right down to business."
            "I've been getting steadily harder since the girls started undressing in front of me."
            "And now that I'm locked into Reona's embrace, I'm almost painfully erect."
            "So much so that I feel the overwhelming need to do something with it."
            "But as soon as I make contact down there, I know that Reona's in the same state too."
            "I begin to move back and forth, meaning to overcome her natural resistance slowly."
            "That is until another hand reaches in and starts to get involved."
            lexi.say "Come on, guys..."
            lexi.say "Let's get things moving, yeah?"
            "Before either of us can object, Lexi's hand is in the middle of everything."
            "One moment she's squeezing the shaft of my cock."
            show whore reverse cowgirl vaginal up
            "The next she's stroking the lips of Reona's pussy."
            "And the effect of her touch is so intense that neither of us can even try to object."
            show whore reverse cowgirl lying vaginal down with vpunch
            "A moment later I feel her pushing the head of my cock hard against Reona's pussy."
            "At the same time all of the resistance seems to melt away from her body."
            "Just like that I sink into her, unprepared for the way that it's happening."
            "Which means that I don't slow down or stop."
            "All of the effort I was using to get inside now sends me deep inside of Reona."
            "I don't stop until I'm all the way in there, until I can't go any further."
            "Lexi giggles with delight, and I hear Reona moaning too."
            "But I don't stop for a moment, instead I start to move inside of her."
            show whore reverse cowgirl raising up
            pause 0.2
            show whore reverse cowgirl raising down at startle(0.05,-10)
            pause 0.2
            show whore reverse cowgirl raising up
            pause 0.2
            show whore reverse cowgirl raising down at startle(0.05,-10)
            "Just like that I'm thrusting in and out of Reona, going as fast as I can."
            "I can feel her beneath me the whole time, sense the hunger in her as well."
            "As quickly as I can deliver it to her, Reona's body eats it up and demands more."
            show whore reverse cowgirl raising up
            pause 0.2
            show whore reverse cowgirl raising down at startle(0.05,-10)
            pause 0.2
            show whore reverse cowgirl raising up
            pause 0.2
            show whore reverse cowgirl raising down at startle(0.05,-10)
            "Which is a good thing, because I feel like I want to keep right on giving."
            "All the time we're making love at this manic pace, Lexi's watching."
            "She doesn't hold back either, putting her hands anywhere and everywhere she chooses."
            "And whenever her touch seems to set one of us off or make things more intense, I hear her laugh."
            "Then the capricious touching begins anew, adding to the thrill of what we're doing to each other."
            show whore reverse cowgirl raising up ahegao
            pause 0.2
            show whore reverse cowgirl raising down at startle(0.05,-10)
            pause 0.2
            show whore reverse cowgirl raising up
            pause 0.2
            show whore reverse cowgirl raising down at startle(0.05,-10)
            "In the end, I think it's Lexi's involvement that pushes me over the edge."
            "Because when she grabs my balls and squeezes them, I feel my entire body twinge."
            "The next thing I know, I can sense my climax approaching."
            "And there's nothing I can do to stop it, no hope of holding on any longer."
            menu:
                "Cum inside":
                    "Still laid atop Reona, I simply keep on going."
                    show whore reverse cowgirl raising up ahegao
                    pause 0.2
                    show whore reverse cowgirl raising down at startle(0.05,-10)
                    pause 0.2
                    show whore reverse cowgirl raising up
                    pause 0.2
                    show whore reverse cowgirl raising down at startle(0.05,-10)
                    "Thrusting in and out until the very last moment that I can."
                    "And then I let it happen, holding nothing back."
                    show whore reverse cowgirl raising up
                    pause 0.2
                    show whore reverse cowgirl raising down at startle(0.05,-10)
                    pause 0.2
                    show whore reverse cowgirl raising up cum
                    pause 0.2
                    show whore reverse cowgirl lying down -cum with vpunch
                    "I fill Reona with everything that I have to give."
                    show whore reverse cowgirl lying up cum
                    pause 0.2
                    show whore reverse cowgirl lying down -cum at startle(0.05,-10)
                    pause 0.2
                    show whore reverse cowgirl lying up cum
                    pause 0.2
                    show whore reverse cowgirl lying down -cum with vpunch
                    "Her back bends and she begins cum too."
                    show whore reverse cowgirl close with vpunch
                    "But she's pinned down my Lexi and myself."
                    "Which means that there's no escaping for even a moment."
                "Pull out":
                    "For the first time since this started, I struggle to free myself."
                    show whore reverse cowgirl raising up
                    pause 0.2
                    show whore reverse cowgirl raising down at startle(0.05,-10)
                    pause 0.2
                    show whore reverse cowgirl raising up
                    pause 0.2
                    show whore reverse cowgirl lying down at startle(0.05,-10)
                    "Not totally, but merely enough to be able to move a certain part of my body."
                    show whore reverse cowgirl raising up
                    pause 0.2
                    show whore reverse cowgirl raising down at startle(0.05,-10)
                    pause 0.2
                    show whore reverse cowgirl raising up
                    pause 0.2
                    show whore reverse cowgirl lying down at startle(0.05,-10)
                    "And when I have the space I need, I don't hesitate to do so."
                    show whore reverse cowgirl -vaginal with vpunch
                    "I pull out of Reona with a sudden jerk, making her arch her back beneath me."
                    show whore reverse cowgirl cumshot with vpunch
                    "And from what I can see, she begins to cum almost the same moment it's done."
                    "Riding out her orgasm as I shoot my load over her exposed belly."
            $ reona.sexperience += 1
    if renpy.has_label("whore_harem_achievement_2") and not game.flags.cheat:
        call whore_harem_achievement_2 from _call_whore_harem_achievement_2
    "Once we're done I feel an immense amount of satisfaction as I collapse onto the bed."
    "Lexi and Reona do the same, lying to either side of me and seeming to be as spent as I am too."
    "But at least we can fall asleep secure in the knowledge that we exhausted ourselves having fun."
    "And we did it without getting caught by my housemates too."
    return


label lexi_reona_propose_male:
    "My relationship with Lexi and Reona feels like one of the wildest things that I've ever been involved with."
    "It was crazy when it started out, and since then it only seems to have gotten more intense and passionate."
    "So what I'm about to do might seem like a pretty weird idea, as it's a totally normal and routine thing."
    "And that's because I have two rings in my pocket right now, and I'm getting ready to propose to Lexi and Reona."
    "But my reasoning is that they just passed laws to make polygamy legal, right?"
    "So my wanting to make things with the two of them official is part of the new normal, isn't it?"
    "At least that's the way I hope they're going to see it!"
    "All I have to do now is play it cool, just act like there's nothing at all going on here."
    "Which is something that I can easily pull off, because I'm a smart guy in control of my emotions."
    "Plus I know that Lexi and Reona are easily distracted, so they'll probably never notice anything's amiss."
    show lexi nophone at center, zoomAt(1.0, (740, 720))
    show reona at center, zoomAt(1.0, (440, 720))
    with dissolve
    lexi.say "Hey, Reona..."
    show lexi smile
    show reona shout
    reona.say "Yeah, Lexi?"
    show lexi normal
    lexi.say "You seen how shifty, [hero.name]'s being today?"
    show lexi smile
    "My head snaps around as soon as I overhear the conversation the girls are having."
    show reona pensive
    reona.say "Hell, yeah!"
    reona.say "And I was gonna say something too."
    show reona shout
    reona.say "But you beat me to it!"
    show reona normal
    show lexi normal
    lexi.say "Oh-oh..."
    show lexi sadsmile
    lexi.say "Looks like he's been snooping on our conversation too!"
    show lexi annoyed
    "I can already feel my cheeks flushing as the girls put me on the spot."
    "And I know that they're on the brink of blowing my entire plan."
    "So as far as I can see, I only have two choices."
    "The first is to abort the entire thing and make up some lame excuse."
    "Or the second, just say to hell with it, and plough on regardless."
    show lexi at center, traveling(1.5, 0.3, (840, 1040))
    show reona at center, traveling(1.5, 0.3, (440, 1040))
    "And I think you can guess which option I'm going to choose."
    mike.say "Actually, there was something I wanted to ask you guys..."
    "I'm getting down on one knee as I say this."
    "Looking from Lexi to Reona as I reach into my pocket."
    show reona surprised
    show lexi surprised
    "Luckily for me, this seems to be more than enough to change the balance of power."
    "In fact it seems to have totally tipped the scales in my favour."
    "Because the looks of amusement on their faces have suddenly vanished."
    "And in their place, Lexi and Reona wear puzzled expressions."
    lexi.say "What are you doing down there?"
    reona.say "[hero.name]…"
    show reona annoyed
    reona.say "You're being so weird right now!"
    show lexi normal
    lexi.say "Well, maybe weirder than usual!"
    show lexi smile
    "Hoping to make use of this temporary advantage, I hold up the rings."
    "And I offer one to each of the girls."
    mike.say "What I wanted to say is this..."
    show reona embarrassed
    show lexi blank
    mike.say "Ever since we all got together, things have just gotten better and better."
    mike.say "And I think that's because we have something really special, you know?"
    mike.say "Something that we should really make official."
    mike.say "What I'm trying to say is that I love you both, and I want to marry you!"
    if lexi.love >= 195 and reona.love >= 195:

        "I feel like I'm going to be left hanging, waiting for an answer."
        "But almost instantly, Lexi and Reona burst out with their replies."
        show reona surprised
        show lexi surprised
        lexi.say "Marry you?!?"
        show lexi happy
        lexi.say "Of course I'll fucking marry you!"
        show lexi smile
        show reona shout
        reona.say "Yes, yes, yes!"
        reona.say "I totally want to be your wife!"
        show reona happy
        "I feel a flood of relief wash over me when I realise they both said yes."
        "And it's soon joined by a feeling of excitement as I get to my feet and slide on the rings."
        "But then something else occurs to me."
        mike.say "Guys, I'm ecstatic that you both want to marry me."
        mike.say "But you do get that it means marrying each other too, right?"
        "I'm expecting Lexi and Reona to look at me like I'm stupid."
        "But instead they both seem to be more than a little struck by the reminder."
        show lexi normal
        lexi.say "Oh fuck..."
        lexi.say "He's right!"
        show lexi smile
        show reona shout
        reona.say "Well, I'm cool with marrying you, Lexi!"
        show reona happy
        show lexi happy
        lexi.say "Me too - it's just a crazy fun idea, you know?"
        show lexi smile
        "I feel that flood of relief renewed as the girls get into the idea."
        "And I know, deep down, that I made the right decision doing this."
        "So let's hope that things only get to be more fun from this point on!"
        $ lexi.set_fiance()
        $ reona.set_fiance()
    elif lexi.love >= 195:

        "I feel like I'm going to be left hanging, waiting for an answer."
        "But almost instantly, Lexi and Reona burst out with their replies."
        show lexi surprised
        lexi.say "Marry you?!?"
        show lexi happy
        lexi.say "Of course I'll fucking marry you!"
        show lexi smile
        show reona annoyed
        reona.say "I can't get married, [hero.name]…"
        reona.say "That's what ancient people do!"
        show reona sadsmile
        "I'm feeling a weird mix of emotions as I get up again."
        "On the one hand, I'm excited to slide a ring onto Lexi's finger."
        "But on the other, both of us are now looking awkwardly at Reona."
        show lexi annoyed
        lexi.say "What's the matter, Reona?"
        lexi.say "We're good enough to fuck..."
        lexi.say "But we're not marriage material?"
        show lexi sad
        show reona annoyed
        reona.say "Don't be like that, Lexi!"
        show reona sad
        "Lexi shakes her head and grabs hold of my arm."
        "Then she turns on her heel, dragging me away with her."
        hide reona
        show lexi normal at center, traveling(1.5, 0.3, (640, 1040))
        with fade
        lexi.say "Come on, future husband..."
        lexi.say "We don't need her kind of negativity in our lives."
        show lexi smile
        "I feel like I have no choice but to follow."
        "Glancing helplessly back over my shoulder at Reona as we go."
        $ lexi.set_fiance()
        $ reona.love -= 25
        $ reona.sub -= 25
    elif reona.love >= 195:

        "I feel like I'm going to be left hanging, waiting for an answer."
        "But almost instantly, Lexi and Reona burst out with their replies."
        show lexi surprised
        lexi.say "Marry you?!?"
        lexi.say "Are you fucking insane?"
        show lexi sad
        show reona shout
        reona.say "Yes, yes, yes!"
        reona.say "I totally want to be your wife!"
        show reona happy
        "I'm feeling a weird mix of emotions as I get up again."
        "On the one hand, I'm excited to slide a ring onto Reona's finger."
        "But on the other, both of us are now looking awkwardly at Lexi."
        show reona annoyed
        reona.say "What's the matter, Lexi?"
        reona.say "We're good enough to fuck..."
        reona.say "But we're not marriage material?"
        show reona sadangry
        show lexi sadsmile
        lexi.say "Don't be like that, Reona!"
        show lexi sad
        "Reona shakes her head and grabs hold of my arm."
        "Then she turns on her heel, dragging me away with her."
        hide lexi
        show reona shout at center, traveling(1.5, 0.3, (640, 1040))
        with fade
        reona.say "Come on, future husband..."
        reona.say "We don't need her kind of negativity in our lives."
        show reona happy
        "I feel like I have no choice but to follow."
        "Glancing helplessly back over my shoulder at Lexi as we go."
        $ reona.set_fiance()
        $ lexi.love -= 25
        $ lexi.sub -= 25
    else:

        "I feel like I'm going to be left hanging, waiting for an answer."
        "But almost instantly, Lexi and Reona burst out with their replies."
        show lexi surprised
        lexi.say "Marry you?!?"
        lexi.say "Are you fucking insane?"
        show lexi sad
        show reona annoyed
        reona.say "I can't get married, [hero.name]…"
        reona.say "That's what ancient people do!"
        show reona sadsmile
        "I can already feel my hopes and dreams being crushed by their answers."
        "So I get slowly to my feet, trying to look like it's no big deal."
        mike.say "Oh..."
        mike.say "Right..."
        mike.say "I don't know what I was even thinking!"
        "Lexi and Reona don't seem to pick up on just how disappointed I am."
        "Either that or they choose to ignore it for the sake of not embarrassing me further."
        show lexi sadsmile
        lexi.say "And we'd have been marrying each other too!"
        show reona annoyed
        reona.say "Oh yeah, we would!"
        reona.say "And I don't wanna marry you either, Lexi!"
        show reona sadsmile
        show lexi sadsmile
        lexi.say "Don't sweat it, Reona..."
        show lexi wink
        lexi.say "I feel the same way about you too!"
        show lexi sad
        "All I can do is keep the rigid smile on my face as they trample all over my dreams."
        "I just hope that this doesn't mean the end for the relationship as a whole."
        "Because that really would be too much for me to handle!"
        hide lexi
        hide reona
        $ lexi.love -= 25
        $ lexi.sub -= 25
        $ reona.love -= 25
        $ reona.sub -= 25
    return


label lexi_reona_male_ending:

    if renpy.has_label("whore_harem_achievement_3") and not game.flags.cheat:
        call whore_harem_achievement_3 from _call_whore_harem_achievement_3
    $ game.room = "church"
    scene bg church wedding with fade
    "There are some things that you never think are going to happen to you, not in a million years."
    "I'm talking about crazy stuff like winning the lottery or finding that you're the legitimate King of Spain."
    "But if you'd asked me if I ever thought I'd be getting married to not one, but two super-hot girls..."
    "Well, there's every chance that I'd have put it on the same list, something that only happens in the movies."
    "And yet here I am, standing at the altar in a chapel filled with guests and well-wishers."
    "Guests that are drawn from the friends and family of not two, but three different people."
    "Because today's the big day."
    "The day that I get to marry Lexi AND Reona!"
    "Sure, it was a long and winding road that brought us here."
    "And there were a lot of times when I thought I was going to go careening off of it and into a pile-up."
    "But somehow we manages to navigate all of those twists and turns along the way."
    "Now the only thing I have to do is not let my nerves get the better of me before the ceremony is over."
    "Something that'd be greatly helped if it were to actually get started soon."
    "I shoot a nervous glance at the priest standing in front of me."
    "But all he can do is offer me a shrug and a smile in the way of reassurance."
    "Not feeling like that makes any difference, I turn my head."
    "And it's while I'm staring back at the doors of the chapel that something finally changes."
    "All of a sudden there's the sound of music, and I recognise it instantly."
    "It's the track Lexi and Reona chose to come down the aisle to."
    "I feel a surge of relief, but only for a few mere seconds."
    "Because then the doors of the chapel swing open, and I see my brides for the first time today."
    show lexi wedding smile nophone at center, zoomAt(1.0, (840, 720))
    show reona wedding happy at center, zoomAt(1.0, (440, 720))
    with dissolve
    "Lexi and Reona made the choice to come down the aisle together."
    "And now that they're walking towards me, it makes perfect sense."
    "Side by side and hand in hand, they present an image of togetherness and equality."
    "Neither one is coming before or putting themselves above the other."
    "Lexi looks amazing in her wedding dress, such a contrast to her normal trashy style."
    "It highlights every bit of the natural beauty that she possesses."
    "Making me aware of just how special she truly is."
    if lexi.is_visibly_pregnant:
        "The cut of her dress compliments her curving belly, rather than trying to hide it."
        "And I know full well that there's no way Lexi would ever deny the fact she's pregnant."
        "Because I also know just how proud she is to be carrying our child."
    else:
        "But don't think that means I'll be trying to make Lexi into a proper lady."
        "I fell in love with her for who she is, not what I thought I could make her into."
    "Reona's as beautiful as she was the first day I met her at college."
    "And she's walking with the same confidence she had that day as well."
    "Like Lexi, I never want her to chance."
    "I'll always be perfectly happy with her as the person she is."
    if reona.is_visibly_pregnant:
        "And the fact that she's visibly pregnant is a part of that too."
        "I don't feel any shame as I gaze at Reona's belly."
        "On the contrary, I feel a thrill knowing she's expecting."
        "As well as the promise for the future that brings along with it."
    else:
        "Sometimes I wonder what would have happened if I hadn't talked to her that day."
        "If I'd refused to offer the help that she needed to get ahead in her studies."
    show lexi at center, traveling(1.5, 5.0, (840, 1040))
    show reona at center, traveling(1.5, 5.0, (440, 1040))
    "I'm staring at the girls so hard and thinking so deeply about them that I kind of zone out."
    "For a moment I almost forget where I am and what's happening right now."
    "So when they actually reach the altar, it snaps me right back to reality."
    show lexi normal
    lexi.say "Hey..."
    lexi.say "Earth to [hero.name]!"
    show lexi smile
    show reona shout
    reona.say "Wake up..."
    reona.say "You've got two girls to marry!"
    show reona happy
    mike.say "Oh..."
    mike.say "Oh yeah, sorry..."
    mike.say "This is all..."
    mike.say "It's just a lot, you know?"
    "Lexi and Reona nod, smiling with genuine amusement."
    "And we might have been able to share a little more banter."
    "But the priest seems to be eager to get things started."
    "Priest" "Ahem..."
    show lexi blank
    show reona normal
    "At the sound of his clearing his throat, everyone comes to attention."
    "And then we all hurry to get into our proper positions."
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To join these three people together..."
    "Priest" "In the bonds of holy matrimony."
    show lexi wink
    lexi.say "Bonds!"
    show lexi smile
    show reona shout
    reona.say "Yeah..."
    show reona devious
    reona.say "I like the sound of that!"
    mike.say "Shhh!"
    show lexi annoyed
    show reona annoyed
    "That pretty much sets the tone for the rest of the ceremony."
    "The priest goes through the motions, reciting the words."
    "While Lexi and Reona make smutty jokes every chance they get."
    show lexi flirt
    show reona devious
    "Luckily for me, they seem to get a little more serious when it comes to the actual vows."
    "Priest" "Do you, Lexi..."
    "Priest" "Take Reona and [hero.name]..."
    "Priest" "To be your lawful, wedded partners?"
    show lexi happy at startle
    lexi.say "You bet I do!"
    show lexi smile
    "Priest" "Do you, Reona..."
    show reona normal
    "Priest" "Take Lexi and [hero.name]..."
    "Priest" "To be your lawful, wedded partners?"
    show reona shout at startle
    reona.say "I sure do!"
    show reona happy
    "Priest" "And do you, [hero.name]..."
    "Priest" "Take Lexi and Reona..."
    "Priest" "To be your lawful, wedded partners?"
    mike.say "I do."
    "The priest seems to mutter this under his breath."
    "Which means I'm not sure what he actually said."
    "Priest" "God help you!"
    mike.say "Huh?"
    mike.say "What was that?"
    "Priest" "Oh..."
    "Priest" "I mean, very good!"
    "Priest" "I call upon all those here present..."
    "Priest" "That if you know of any lawful reason..."
    "Priest" "Why these three many not be married..."
    "Priest" "Speak now, or forever hold you peace!"
    "There's the customary pause as the guests chuckle to themselves."
    "But I'm actually starting to sweat as I wait for the moment to pass."
    "Because I'm afraid of that scumbag Danny showing his lousy face."
    "That or one of Reona's rotten ex-boyfriends showing up."
    "Luckily for me, none of those things happen."
    "And I breathe a sigh of relief as the priest gets going again."
    "Priest" "Very well..."
    "Priest" "By the power vested in me..."
    "Priest" "I now pronounce you married."
    "Priest" "You may celebrate in a manner you find fitting."
    "Of course that results in a three-way embrace."
    hide reona
    hide lexi
    show lexi kiss wedding
    with fade
    $ lexi.flags.kiss += 1
    "Followed by a hell of a lot of kissing!"
    hide lexi kiss
    show reona kiss wedding
    with fade
    $ reona.flags.kiss += 1
    "And why not?"
    hide reona kiss
    show lexi wedding happy at center, zoomAt(1.5, (840, 1040))
    show reona wedding happy at center, zoomAt(1.5, (440, 1040))
    with fade
    "We actually did it - we got married!"
    "Which has to be something worth celebrating."


    scene whore ending with fade
    reona.say "Are you guys sure you want us to do this?"
    reona.say "Because we usually let [hero.name] do all the talking."
    lexi.say "Yeah..."
    lexi.say "And not because we're all sexist or anything either."
    lexi.say "He's just like, better at that kind of stuff."
    reona.say "So you really want us to do it?"
    reona.say "Okay then..."
    reona.say "I guess we'll give it a go."
    lexi.say "Oh man, this is going to sound so lame!"
    lexi.say "But I gotta say it..."
    lexi.say "My life was so much worse before [hero.name] came along!"
    reona.say "How so, Lexi?"
    lexi.say "Well I obviously didn't think so at the time."
    lexi.say "I was living at the trailer-park with a trailer all of my own."
    lexi.say "And I was turning tricks on the street most nights."
    lexi.say "Making a lot of money too!"
    reona.say "There's a but coming, isn't there?"
    reona.say "I can always sense a but on the horizon!"
    lexi.say "Yeah, and it was a pretty fucking massive butt too."
    lexi.say "It was Danny, my pimp - and yeah, he was a total asshole!"
    lexi.say "At first I thought he was a cool guy, you know?"
    lexi.say "Like he was looking out for me and getting me work."
    lexi.say "But then I met [hero.name]."
    reona.say "Ah, enter the handsome prince!"
    lexi.say "Oh stop it!"
    lexi.say "But yeah, at first he seemed to be just another customer."
    lexi.say "Maybe even a rube that I could take to the cleaners with ease."
    lexi.say "But then the weirdest thing happened - he started being nice to me!"
    lexi.say "And that's when I started seeing that Danny was just using me."
    lexi.say "Without [hero.name] I'd never have realised."
    lexi.say "Plus he helped me to kick Danny to the kerb too!"
    reona.say "Hmm..."
    reona.say "With me it was kinda similar."
    reona.say "But nothing so dramatic as that."
    lexi.say "Oh yeah?"
    reona.say "Yeah..."
    reona.say "I was in a really bad place when we first met."
    reona.say "No self-esteem and trying to fill that hole with meaningless sex."
    lexi.say "Tell me about that place!"
    reona.say "It had almost become the whole of my personality."
    reona.say "And I saw [hero.name] as my latest conquest."
    reona.say "But he wouldn't go for it, no matter how hard I tried to tempt him!"
    lexi.say "That's a feat in itself, Reona..."
    lexi.say "Because you are one hot chick!"
    reona.say "Thanks, babe..."
    reona.say "I appreciate you."
    reona.say "Anyway..."
    reona.say "It wasn't that he wouldn't have sex with me."
    reona.say "More that he would, but he made me realise my own value."
    reona.say "You know what I mean?"
    lexi.say "I sure do, girlfriend!"
    reona.say "He showed me that I could be a sexual being."
    reona.say "And yet still be able to have worth as a person."
    reona.say "That I could find fulfilment in dedicating myself to just one man."
    lexi.say "And one other woman!"
    lexi.say "Don't think you're leaving me out of this wonderful story!"
    reona.say "Of course not, Lexi!"
    reona.say "When [hero.name] introduced us, I knew there was something special about you."
    lexi.say "I felt the same thing the moment we me!"
    lexi.say "But it was a little weird discovering I was in love with two people."
    reona.say "That did take a bit of getting my head around too."
    reona.say "But together we made it work."
    reona.say "You know I always thought I might be the kind of wife that stays at home."
    reona.say "The kind that waits for her successful husband to come home from the office."
    lexi.say "Yeah, but I bet you never imagined you'd be wearing a dog-collar when you did!"
    reona.say "Oh no..."
    reona.say "Or that we'd both be on our hands and knees behind the front-door!"
    lexi.say "Ha!"
    lexi.say "I love the look on his face when we pull stunts like that!"
    if (lexi.is_visibly_pregnant or lexi.flags.mikeBabies >= 1) and (reona.is_visibly_pregnant or reona.flags.mikeBabies >= 1):
        lexi.say "Though we get to do less of it now Chantel and Laurel are around."
        lexi.say "[hero.name]'s usually running around after them when he gets home."
        reona.say "Yeah, but he loves being a daddy."
        reona.say "And that's what makes it worthwhile."
    elif (lexi.is_visibly_pregnant or lexi.flags.mikeBabies >= 1):
        lexi.say "Though we get to do less of it now little Chantel's around."
        lexi.say "[hero.name]'s usually running around after her when he gets home."
        reona.say "Yeah, but he loves being a daddy."
        reona.say "And that's what makes it worthwhile."
    elif (reona.is_visibly_pregnant or reona.flags.mikeBabies >= 1):
        reona.say "Though we get to do less of it now little Laurel's around."
        reona.say "[hero.name]'s usually running around after her when he gets home."
        lexi.say "Yeah, but he loves being a daddy."
        lexi.say "And that's what makes it great."
    else:
        reona.say "We might want to make the most of it while we have the chance."
        lexi.say "Huh?"
        lexi.say "Wadda ya mean?"
        reona.say "Well, [hero.name] has the wives, the house and the job."
        reona.say "All he needs to complete the picture is a couple of kids."
        lexi.say "Oh, you think?"
        reona.say "I do think!"
        lexi.say "No worries, we'll both look cute with big, pregnant bellies."
        lexi.say "And we'll have some serious fun getting them too!"
    reona.say "So all in all, I think things turned out pretty well for us."
    lexi.say "Yeah, life's pretty darn sweet."
    lexi.say "And I kinda want to see where we end up, you know?"
    reona.say "I do, Lexi."
    reona.say "If it's as good in the future as it is right now."
    reona.say "Then I definitely can't wait to see what happens next."
    scene bg black with dissolve
    pause 0.5
    $ game.set_new_game_plus()
    $ renpy.full_restart()
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
