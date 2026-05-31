init python:
    Event(**{
    "name": "sasha_nightclub_showdown",
    "label": "sasha_nightclub_showdown",
    "duration": 1,
    "music": "music/roa_music/smile_for_me.ogg",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsRoom("date_nightclub")),
        PersonTarget(sasha,
            OnDate(),
            MinStat("sexperience", 1),
            MaxStat("sub", 75),
            ),
        PersonTarget(audrey,
            Not(IsHidden()),
            IsRoom("nightclub", "nightclubbar"),
            MinStat("sexperience", 1),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "jealous_harem_01",
    "label": "jealous_request",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsDone("sasha_nightclub_showdown"),
        HeroTarget(IsActivity("work", "workhard", "work_personal", "workhard_personal")),
        PersonTarget(sasha,
            Not(IsHidden()),
            IsFlag("cheated_too_much", False),
            IsFlag("showdownDelay", False)),
        PersonTarget(audrey,
            Not(IsHidden()),
            IsRoom("office"),
            MinStat("love", 100),
            MinStat("lesbian", MIN_LES_GIRL_SEX),
            ),
        ],
    "do_once": True,
    })

    SpecificTalkSubject(**{
    "name": "jealous_harem_02",
    "display_name": "Suggest a threesome to Sasha",
    "label": "jealous_proposal",
    "conditions": [
        IsDone("jealous_harem_01"),
        PersonTarget(sasha,
            IsActive(),
            Not(IsHidden()),
            Not(HasCheated()),
            IsFlag("requestDelay", False),
            IsFlag("audreythreesome", 1),
            ),
        ],
    "do_once": True,
    "icon": "button_audrey",
    })

    SpecificTalkSubject(**{
    "name": "jealous_harem_03",
    "display_name": "Tell Audrey that Sasha wants a threesome",
    "label": "jealous_arrangement",
    "conditions": [
        IsDone("jealous_harem_02"),
        HeroTarget(IsRoom("office")),
        PersonTarget(sasha,
            Not(IsHidden()),
            IsFlag("proposalDelay", False),
            IsFlag("audreythreesome", 2),
            ),
        PersonTarget(audrey,
            IsActive(),
            ),
        ],
    "do_once": True,
    "icon": "button_sasha",
    })


label sasha_nightclub_showdown:
    "Despite my nerves, the night seems to be going pretty well, what with this being the first time that Sasha and I have hit a nightclub together as an official item."
    "We found a club where the music was agreeable to the both of us, grabbed a couple of drinks and just took it from there."
    "Maybe it's the fact that the sheer volume of the place makes holding a conversation almost impossible, meaning I can't put my foot in it that way."
    "But then again, perhaps I'm just being too pessimistic, and we're actually getting along so well because we have genuine chemistry."
    "Eventually a track that Sasha can't resist gets played, and she drags me onto the dance-floor, refusing to take no for an answer."
    "I try not to look as though my protests are too phoney as I allow myself to be pulled along in her wake."
    "But all the while I'm eager to spend any amount of time pressed up close to Sasha while she gets hot and sweaty..."
    "Before too long, I can feel a willing body pressed against me, fulfilling the possibilities that are filling my mind."
    show sasha angry zorder 1 at right with dissolve
    "The only problem is that it takes me almost a full minute to realise that Sasha is still standing a little way off, her mouth hanging open in surprise."
    "Trying to shake myself back into awareness, I look down and see Audrey, a broad smile on her face as she grinds herself against me."
    show audrey zorder 2 at center, zoomAt(1.65, (640, 1140)) with dissolve
    audrey.say "Hey there - I didn't know you were a regular here!"
    "You know those times when you really do wish that the ground would open under your feet and swallow you up?"
    show sasha vangry
    "Before I even manage to even think about reacting, Sasha's expression has already turned dark and thunderous."
    "She shakes her head in apparent disgust, turns around and then storms off the dance-floor without as much as a single word."
    hide sasha with moveoutright
    show audrey frown
    "At the same time, Audrey has begun to frown at my frigid reaction to her attentions."
    "And why wouldn't she?"
    "Especially when I was so eager to return them the last time we met!"
    "But as I keep looking after Sasha and trying to escape her grip, she soon figures out what's going on."
    hide audrey
    show audrey annoyed at flip, zoomAt(1.65, (640, 540))
    audrey.say "Don't tell me - you were here with that other girl over there?"
    "I nod desperately, still trying to free myself from her grasp."
    show audrey mock
    audrey.say "Ooh...awkward!"
    show audrey joke
    audrey.say "Well, don't mind me - I think you've already got enough problems on your hands!"
    hide audrey with moveoutleft
    "With that, she steps to one side, allowing me to hurry after Sasha."
    "Part of me wants to say something sarcastic in response."
    "But I'm too desperate to catch up to Sasha for my brain to fire anything off quickly enough without making myself look even more stupid than I already do right now."
    "Of course, I was also pretty damn stupid to think that I could have some fun with Audrey behind Sasha's back without her finding out."
    show sasha annoyed at center with dissolve
    "I manage to catch up to her just before she reaches the exit."
    mike.say "Sasha...wait...please!"
    show sasha angry at center, zoomAt(1.5, (640, 1040)) with hpunch
    "I grab hold of her arm, more out of sheer desperation than any desire to manhandle her."
    with hpunch
    "Sasha spins around and twists her way out of my grip, her face still showing her evident distaste for my presence."
    "At the sight of our struggle, one of the doormen starts to walk over."
    "But Sasha shakes her head in his direction, causing him to shrug and turn away again."
    mike.say "Sasha...that wasn't what it looked like!"
    mike.say "I can explain..."
    show sasha vangry
    sasha.say "Can you really?"
    sasha.say "Because right now, all I hear are bullshit cliches!"
    show sasha angry
    menu:
        "Admit cheating":
            $ sasha.love -= 10
            "Maybe the only way that I can hope to make this right is to tell Sasha the truth?"
            "Honesty might show her that I'm seriously sorry for going behind her back."
            "But even if it doesn't, she's still too special for me to want to lie to her..."
            mike.say "Yes...that was what it looked like."
            mike.say "We hooked up once, back when you and I got together."
            mike.say "I didn't tell you at the time, because I didn't know if we'd get serious."
            show sasha wtf
            "At this last admission, her eyes go wide with irritation."
            mike.say "I...I know that was a mistake now."
            mike.say "I'm sorry, Sasha - really I am."
            show sasha angry
            "For a while, she says nothing, just stares at me in silence."
            "I can see that she's sizing up my explanation, dissecting it for what it's worth."
            show sasha vangry
            sasha.say "What were you doing?"
            sasha.say "Hedging your bets, huh?"
            show sasha angry
            mike.say "No, Sasha - it wasn't like that at all!"
            mike.say "You have to believe me!"
            "Sasha snorted and shook her head in apparent disbelief."
            show sasha annoyed
            sasha.say "No, [hero.name], I think you'll find that I don't."
            sasha.say "In fact, I think that if you want me to buy your story, then you're the one that's got to convince me."
            hide sasha with moveoutright
            "And with that, she turns her back on me for a second time and walks out of the nightclub."
            "But this time, I make no effort to follow."
            "Instead I just stand there, cursing myself for a fool and trying to think up some way to win her over once again."
        "Deny cheating":
            $ sasha.love -= 20
            "I want to be honest with Sasha, really I do."
            "But there's such a thing as too much honesty."
            "If she knew every grisly detail about my life, I'm sure Sasha would never be able to look me in the face again!"
            mike.say "Okay, okay...I do know that girl."
            mike.say "But she's an old flame, back from well before we were ever an item."
            "Sasha narrows her eyes, scrutinising my words for all they're worth."
            "But all the same, I can see a glimmer in her eyes that I choose to interpret as her wanting to believe me."
            "Whether my hunch right or not, I choose to seize on the one chance that I can see before me right now."
            show sasha annoyed
            sasha.say "You really mean that?"
            sasha.say "Because she seemed REALLY familiar with you?"
            "I can feel a cold sweat running down the back of my neck as she waits for my answer."
            "But I've committed myself to the lie, and I can't take it back now."
            mike.say "Of course I do, Sasha!"
            mike.say "Didn't you hear how surprised she was to see me here?"
            mike.say "I don't think I've seen her since we were last together."
            mike.say "And well...we kind of never broke it off - at least not formally."
            "Sasha nods slowly, as though she's not totally satisfied with this explanation, but willing to buy it all the same."
            show sasha normal
            sasha.say "Okay...well...I'm going home now."
            sasha.say "I don't feel like doing this anymore tonight."
            sasha.say "Would you mind getting a taxi home without me?"
            sasha.say "I need some time to think..."
            hide sasha with moveoutright
            "And with that, she turns her back on me for a second time and walks out of the nightclub."
            "But this time, I make no effort to follow."
            "Instead I just stand there, cursing myself for a fool and trying to think up some way to win her over once again."
    $ sasha.flags.nodate = True
    $ sasha.flags.nokiss = True
    $ sasha.flags.cheated = True
    $ hero.cancel_activity()
    $ game.active_date.stay = False
    $ sasha.flags.showdownDelay = TemporaryFlag(True, 3)

    if "followsamadvice" in DONE:
        $ sasha.flags.cheated_too_much = True
    return

label jealous_request:
    $ sasha.flags.audreythreesome = 0
    "It's not that I've been avoiding Audrey as such, just making an extra effort not to come into contact with her."
    "In the aftermath of the unpleasant encounter that Sasha and I had with her in the nightclub, it just seemed the best idea."
    "Not that Audrey seemed to find the whole thing unpleasant herself, judging by her behavior towards me since then."
    "Even when I've not come into direct contact with her, we still work in the same office."
    "So it's pretty much impossible not to keep from at least seeing her in passing most days of the week."
    "And whenever she manages to make eye contact, I get a knowing smile and a little wave from her."
    "I know that she's doing it deliberately, and getting off on torturing me as well."
    "But what with the fallout that I've already had from Sasha, I'm not about to confront Audrey any time soon."
    "It's a cowardly plan of action (or more appropriately inaction) I admit."
    "But it's one that I'm perfectly happy with for the foreseeable future."
    "The only problem with that being Audrey doesn't seem to feel the same way."
    scene bg office
    show audrey work normal at right
    with fade
    "She keeps on trying to corner me, despite my best efforts."
    scene bg breakroom
    show audrey work at left5
    with fade
    "And when she does, I can always see that she's about to engage me in conversation."
    "No prizes for guessing just what she wants to talk to me about either!"
    scene bg personal with fade
    show audrey work at left with moveinleft
    "In the end and despite my best efforts, she finally outwits me."
    "Backed into a corner and with no visible means of escape, I'm well and truly trapped."
    show audrey work normal at center with move
    audrey.say "Ah, [hero.name], finally!"
    audrey.say "I've been wanting to catch you to chat for so long."
    show audrey annoyed
    audrey.say "And if I didn't know better, I might think that you'd been avoiding me..."
    mike.say "Erm...no way, Audrey."
    mike.say "Whatever gave you that impression?"
    audrey.say "Oh, I don't know..."
    show audrey frown
    audrey.say "Maybe the way you keep darting through doors and down corridors the moment you see me?"
    audrey.say "Or perhaps the fact that you're already breaking out in a cold sweat at my being this close?"
    "I look this way and that, wondering if anyone else is within earshot of hearing us."
    mike.say "Is that what it looked like, Audrey?"
    mike.say "Geez, I'm so sorry!"
    show audrey mock
    "Audrey regards me with a sideways glance, clearly far from convinced by this explanation."
    "But she also looks far too amused by my excuses to call me on my bullshit just yet."
    audrey.say "Okay then, [hero.name], if you say so."
    audrey.say "So, why have you REALLY been avoiding me, huh?"
    "Come on brain, don't fail me now!"
    mike.say "Well, I was worried that you might be embarrassed."
    show audrey happy
    "Audrey doesn't even try to stifle the laugh that bursts from her lips."
    audrey.say "Embarrassed?"
    audrey.say "Me?"
    show audrey mock
    audrey.say "Oh, hell no!"
    "Audrey shakes her head, totally dismissing my suggestion."
    "Which I suppose serves me right for projecting my own feelings onto her."
    show audrey normal
    audrey.say "I really enjoyed meeting Sasha."
    audrey.say "She seems like a really great girl."
    mike.say "She does..."
    mike.say "I mean she is!"
    audrey.say "That's actually what I wanted to talk to you about, [hero.name]."
    "With this, Audrey leans in a little closer than before."
    "Not enough to be inappropriate should anyone see us."
    "But definitely closer than I'd have liked in my current state of paranoia."
    audrey.say "I think I know you pretty well by now, [hero.name]."
    audrey.say "And you seem like the kind of guy that knows how to have fun."
    audrey.say "Am I right?"
    "I can sense that we're fast getting into dangerous territory here."
    "But a part of me is still curious to see just what where Audrey's going with this."
    mike.say "I guess you could say that, yeah."
    show audrey blush
    audrey.say "Well, how would you feel about us having some fun together?"
    audrey.say "And by us, I mean you, me and your friend Sasha?"
    mike.say "Wait, what..."
    mike.say "You mean like...like a threesome?!?"
    audrey.say "Yeah, [hero.name], I do."
    audrey.say "I mean something so like a threesome that it's actually a threesome!"
    menu:
        "I'll see if Sasha is interested.":
            "For a moment I just stand there, fully expecting Audrey to start laughing and call the whole thing a joke."
            show audrey normal
            "But instead, she keeps right on looking me in the eye, clearly waiting for an answer."
            mike.say "Y...you mean it?"
            mike.say "You're actually serious?"
            "Audrey leans in a little closer and begins to smile a little wider."
            audrey.say "I mean it."
            audrey.say "I never joke about something as serious as a threesome."
            mike.say "Oh...wow..."
            mike.say "Ahem...I mean, sure thing, Audrey."
            mike.say "I just had to be sure you weren't pranking me, that's all."
            "Only now does Audrey lean back, scrutinizing me as she does so."
            audrey.say "So you'll ask her then?"
            audrey.say "You'll ask Sasha if she's up for it?"
            "I try to make my nod as casual and nonchalant as possible."
            "But I only succeed in making myself look like a moron as I bob my head up and down."
            mike.say "I'll run it by her, sure."
            mike.say "Don't worry, she's a pretty broad-minded girl."
            show audrey happy
            "Audrey gives me a mischievous giggle and turns to walk away."
            audrey.say "I hope you're right, [hero.name]."
            audrey.say "Because this could be a whole lot of fun."
            audrey.say "Fun for all three of us!"
            hide audrey
            $ sasha.flags.audreythreesome = 1
            $ sasha.flags.requestDelay = TemporaryFlag(True, 1)
            return
        "I could never ask Sasha for that!":
            "What in the actual fuck?!?"
            "I barely got out of that nightclub with my balls still attached."
            "How stupid would I have to be to go back to Sasha with an offer like that?"
            mike.say "I...I can't do that, Audrey."
            mike.say "I'm in a relationship with Sasha."
            mike.say "And I don't want to screw that up."
            show audrey angry
            "Audrey leans back, crossing her arms over her chest."
            "The look on her face becomes instantly darker and she narrows her eyes."
            audrey.say "Oh come on, [hero.name], get real!"
            audrey.say "Stop playing the faithful boyfriend - it doesn't suit you."
            "I shake my head at Audrey, trying to insist that it's no act."
            mike.say "I mean it, Audrey."
            mike.say "Sasha's the only girl that I'm interested in right now."
            show audrey frown
            audrey.say "Yeah, right, pull the other one."
            audrey.say "You're a guy, and guys think with their dicks."
            audrey.say "All us girls know what you're thinking about when you look at me."
            audrey.say "The difference between me and most girls is that I can admit it!"
            "I swallow hard as Audrey lays her metaphorical cards on the table."
            "But no matter what she says or what she offers me, I'm determined to keep my resolve."
            mike.say "I'm sorry, Audrey."
            mike.say "But the answer's still no."
            "Audrey tuts at this, shaking her head as she turns to walk away."
            audrey.say "I always had you pegged for a sleaze, [hero.name]."
            audrey.say "But I never thought that you were such a loser!"
            hide audrey
            $ sasha.flags.audreythreesome = 0
            return

label jealous_proposal:
    "It's all well and good me agreeing to Audrey's offer of a threesome."
    "But that's still only two out of the three people on board."
    "And now I have to somehow convince Sasha that it's a good idea too!"
    "I can hardly imagine being able to sell her on me having sex with another girl."
    "So how am I ever going to manage that and having her get involved too?"
    "I keep on telling myself that Sasha's not exactly a saint herself."
    "That she enjoys some pretty wild stuff behind closed doors too."
    "But I still can't quite make myself believe that will be enough."
    "That for all of her kinks, she'll be into the idea of a threesome."
    "In the end, I decide that the best thing is to just come straight out and ask her."
    "Better that and a quick refusal than waiting and giving myself an ulcer from worrying."
    "So as soon as we're alone together, I take the plunge..."
    show sasha normal with dissolve
    mike.say "Ah, Sasha..."
    sasha.say "Yeah, [hero.name] - what's up?"
    mike.say "Well, you remember that thing that happened in the nightclub?"
    show sasha annoyed
    sasha.say "Hmm, let's see, shall we?"
    sasha.say "Would that happen to be the incident with Audrey, would it?"
    show sasha vangry
    sasha.say "The one where the little slut walked up and planted a kiss on you?"
    mike.say "Erm...yeah, that's the one."
    show sasha annoyed
    sasha.say "Yes, [hero.name], I think it's pretty much etched in my memory!"
    "Already feeling myself beginning to sweat, I try to push on as quickly as I can."
    mike.say "Well, you'll never believe what happened the other day."
    sasha.say "Oh no?"
    sasha.say "Why don't you try me?"
    mike.say "Okay, okay...just hear me out."
    mike.say "Audrey was telling me how much she...liked you."
    sasha.say "So she likes me - what's that got to do with anything?"
    mike.say "She liked you a lot, Sasha."
    mike.say "So much so that she asked me if we'd be up for..."
    mike.say "Up for letting her in on what we have going between us."
    show sasha shocked
    "Sasha looks at me blankly for a moment."
    "But then I see the light of recognition in her eyes."
    show sasha surprised
    sasha.say "You mean..."
    mike.say "Yeah, Sasha."
    mike.say "Audrey asked me if we were up for a threesome..."
    if (sasha.lesbian >= MIN_LES_GIRL_SEX and sasha.love >= 100 and sasha.sub >= 75):
        "I watch as a change comes over Sasha's face in response to this revelation."
        "A change that I can only describe as surprise leading to intrigue and interest."
        show sasha annoyed
        sasha.say "A threesome?"
        sasha.say "Really?"
        "I give the question a hurried nod."
        mike.say "Really, Sasha."
        mike.say "And I know that she's not the kind of girl to joke about something like that."
        "Sasha looks like she's battling with something inside of herself for a moment."
        show sasha normal
        "And then she finally seems to come to a conclusion about whatever's bothering her."
        sasha.say "I...I suppose I should be flattered."
        sasha.say "She was quite pretty."
        sasha.say "And sexy too..."
        "I nod again, all the time trying not to look too eager."
        mike.say "She said all of the same stuff about you too, Sasha."
        mike.say "But you shouldn't feel pressured into anything."
        mike.say "Not because she flattered you..."
        "Sasha shakes her head, dismissing my advice."
        sasha.say "It's okay, [hero.name]."
        sasha.say "I'm a grown woman, you know?"
        sasha.say "And it takes more than a compliment to get into my panties."
        "She pauses, cocking her head on one side."
        sasha.say "But then again, I'm also a modern woman too."
        show sasha flirt
        sasha.say "And that means I'm mature enough to handle something like this."
        "I'm nodding again, now eager to push Sasha down the path to saying yes."
        mike.say "And if you think about it, we'd kind of have her at a disadvantage."
        show sasha annoyed
        sasha.say "How so?"
        mike.say "Well, she'd be the new addition to the picture, wouldn't she?"
        mike.say "It's almost like we're doing her a favor by letting her into what we already have."
        show sasha normal
        "Sasha raises an eyebrow at this, clearly intrigued by the notion of Audrey in an inferior position."
        show sasha happy
        sasha.say "Okay, I say we go for it."
        mike.say "That's great, Sasha."
        mike.say "I'll let her know when I next see her."
        "I think I almost manage not to sound too triumphant as I say this."
        "And I also manage to keep from punching the air too..."
        hide sasha
        $ sasha.flags.audreythreesome = 2
        $ sasha.flags.proposalDelay = TemporaryFlag(True, 1)
        return
    else:
        "I watch as a change comes over Sasha's face in response to this revelation."
        show sasha wtf
        "A change that I can only compare to someone realising the taste in their mouth is foul beyond belief."
        sasha.say "And you told her to fuck off, right?"
        "When I don't give her the answer that she's looking for, Sasha begins to shake her head at me."
        show sasha vangry
        sasha.say "[hero.name], please tell me that you told her to fuck off!"
        mike.say "Ah, no, Sasha."
        mike.say "I kind of told her I'd ask you..."
        show sasha annoyed
        "Sasha rolls her eyes and let's out a grunt of frustration and annoyance."
        "The kind of noise that women have been making at the stupidity of men since the dawn of time."
        show sasha vangry
        sasha.say "Oh, you did, did you?"
        sasha.say "Well you can march right back to that filthy little bitch and tell her no way!"
        sasha.say "And while you're doing it, maybe take the time to think about what the hell you want from me!"
        sasha.say "Because I've always been enough for most of the guys that I've dated, [hero.name]!"
        show sasha angry
        "I can already feel my cheeks flushing red as Sasha shames me for my actions."
        "How could I have misjudged her feelings this badly?"
        "I guess the fantasy of a threesome with her and Audrey must have blinded me to the truth."
        mike.say "O...okay, Sasha."
        mike.say "I'm sorry..."
        mike.say "I don't know what I was thinking..."
        show sasha sad
        "Sasha frowns at this, instinctively rejecting my clumsy attempt at an apology."
        "But then I see a glimmer of regret in her eyes, and she shakes her head ruefully."
        sasha.say "Why don't you ask your cock, [hero.name]?"
        sasha.say "And maybe don't let it think for you in future?"
        sasha.say "Now get lost - I think I want to be alone for a while..."
        "Well, I sure managed to go and fuck that one up in spectacular fashion."
        "But Sasha didn't out and out say that she was dumping me over it."
        "So at least there's the hope of salvaging something from this mess..."
        hide sasha
        $ sasha.flags.audreythreesome = 0
        return

label jealous_arrangement:
    "It's weird that I was going out of my way to avoid bumping into Audrey only the other day."
    "And now here I am, actually waiting for a chance to hurry over to her and talk."
    "But then I guess the circumstances are pretty different this time around."
    "And yet for someone that always seems to be hanging around, she's nowhere to be seen."
    "No matter how often I glance at the time or will her to appear, Audrey refuses to appear."
    "This means that when she finally does turn up, I'm so eager to speak to her that I kind of forget myself."
    "And I end up almost pouncing on her as I leap out in front of her."
    mike.say "Audrey!"
    show audrey scared at center, vshake
    audrey.say "Arrgh!"
    audrey.say "What the hell?!?"
    "Audrey almost jumps out of her skin, leaping back in surprise."
    "She has one hand on her chest and the other held out in front of her."
    mike.say "Oops..."
    mike.say "Sorry about that, Audrey."
    mike.say "I've just been waiting to catch you for a while, that's all."
    "Audrey shakes her head as she sucks in a couple of deep breaths."
    show audrey angry
    audrey.say "Yeah, well..."
    audrey.say "I appreciate the enthusiasm, [hero.name]."
    audrey.say "But I can't hear what you have to say if you give me a heart attack!"
    "I can only give an embarrassed shrug in response."
    show audrey normal
    "But I can see that Audrey's already well on the way to recovery."
    "That and the fact she's most likely just remembered why I'm so keen to talk to her too."
    show audrey mock
    audrey.say "Well, now that we're having this little chat, let's hear it."
    audrey.say "Just what could be so urgent, huh?"
    audrey.say "As if I didn't know..."
    "I gulp at this, suddenly aware of being put on the spot."
    mike.say "Ah...I...I spoke to Sasha."
    mike.say "I spoke to Sasha, just like you asked me to, Audrey."
    "Audrey nods, clearly trying to remain patient with me."
    audrey.say "And?"
    mike.say "Oh...yes...Sasha said yes."
    show audrey blush
    "The smile that spreads across Audrey's face puts me in mind of something distinctly feline."
    "I'm sure I've seen a similar look on the face of a big cat about to pounce on its prey."
    audrey.say "Of course she said yes, [hero.name]."
    audrey.say "It's not the kind of offer that comes along every day, after all!"
    show audrey at center, zoomAt(1.5, (640, 1040))
    "Audrey steps forward, closing the distance between us."
    "She leans in towards me, placing a single finger upon my chest."
    "And then traces a pattern with the tip as she speaks."
    show audrey flirt
    audrey.say "So, where are we going to get together?"
    audrey.say "You know, the three of us."
    audrey.say "You, Sasha and me..."
    show audrey at center, zoomAt(2.0, (640, 1340))
    "She's leaning in so close now that her voice is all I can hear."
    "The scent of her is all that I can smell."
    "And the shape of her body is all I can see."
    mike.say "M...my place?"
    mike.say "Should we do it at my place?"
    mike.say "I mean, get it on at my place?"
    mike.say "I mean..."
    "Audrey puts a fingertip to my lips, instantly stopping my tongue."
    audrey.say "Okay, okay."
    audrey.say "Slow down before you give yourself an aneurysm!"
    audrey.say "You guys live under the same roof, don't you?"
    "All I can do is nod in agreement."
    audrey.say "So that makes sense - your place it is then."
    audrey.say "Is Saturday okay for you?"
    mike.say "Sure thing, Audrey!"
    audrey.say "Then it's a date, [hero.name]!"
    audrey.say "See you then..."
    "And with that, Audrey saunters off, leaving me alone again."
    "I know that I should be either elated or downright terrified."
    "But right now, all I can do is watch Audrey's curves as she walks away."
    "For better or worse, this is going to be something that I remember for a long time to come!"
    hide audrey
    $ hero.calendar.add(game.calendar.get_next_day_of_week("saturday"), LabelAppointment(14, ["audrey", "sasha"], "Threesome (Audrey,Sasha)", "jealous_threesome", "missed_jealous_threesome"))
    return

label missed_jealous_threesome:
    "Shit I missed my date with Audrey and Sasha."
    $ audrey.love -= 10
    $ sasha.love -= 10
    $ hero.calendar.add(game.calendar.get_next_day_of_week("saturday"), LabelAppointment(14, ["audrey", "sasha"], "Threesome (Audrey,Sasha)", "jealous_threesome", "missed_jealous_threesome"))
    return

label jealous_threesome(appointment=None):
    scene bg black with dissolve
    pause 1.0
    scene bg livingroom with dissolve
    "When Saturday finally comes around, I find myself reduced to a bag of nerves."
    "I flit between looking down at my mobile and then glancing up towards the hallway."
    "There's nothing that I can do to occupy my mind while I wait for Audrey to arrive."
    "Occasionally I might manage to steal a quick glance at Sasha as she waits beside me."
    "But there's no help from that direction, as she seems to be totally unaffected by my own anxiety."
    "Instead, Sasha is just sitting there in silence, happily playing with her phone as if nothing's amiss."
    mike.say "Ah..."
    mike.say "Where in the hell is she?"
    show sasha normal
    "Sasha glances up from her phone, a quizzical look on her face."
    show sasha talkative
    sasha.say "Sorry, do you want me to actually answer that question?"
    show sasha normal
    "I look at her for a second, my puzzlement apparently all too clear to see."
    show sasha talkative
    sasha.say "I mean - are you really asking me if I know when she's going to get here?"
    sasha.say "Or was that just one of those rhetorical questions?"
    sasha.say "You know, the kind that's just for the sake of making a noise?"
    show sasha normal
    "I let out a long breath, and then nod heavily."
    mike.say "The last one."
    show sasha joke
    "Sasha gives me a little smile and a chuckle."
    "And it seems like she's about to say something."
    play sound door_bell
    "But just then, the sound of the doorbell interrupts her."
    "In the blink of an eye, I'm up and into the hallway."
    "Sasha doesn't even have time to follow me before I have the front door open."
    hide sasha
    show bg house
    show audrey normal
    with wiperight
    show audrey talkative
    audrey.say "Hey, [hero.name]."
    audrey.say "Sorry I'm a little later than we agreed."
    audrey.say "But some things are worth waiting for - I hope!"
    show audrey normal
    "I open my mouth to make what was probably going to be a lame comment."
    "But now it's my turn to be the one left hanging."
    sasha.say "That's what we're about to find out, isn't it!"
    show audrey at right4
    show sasha at left
    with moveinleft
    "I instinctively stand aside at this, turning to see Sasha behind me."
    "She leans against the wall, regarding Audrey with a laconic gaze."
    "For a moment, the two girls seem to size each other up like rival female predators."
    "But then the tension between them breaks as they exchange nods."
    show audrey happy
    audrey.say "Good to see you again, Sasha."
    audrey.say "Really good to see you..."
    show sasha happy
    sasha.say "Likewise, Audrey."
    show audrey blush
    show sasha blush
    "And then their gazes fall on me, like I'm a particularly intriguing morsel."
    "One that's giving them an appetite and making their stomachs grumble in anticipation..."
    show sasha talkative
    sasha.say "Where are your manners, [hero.name]?"
    show sasha normal
    mike.say "Huh?!?"
    show sasha talkative
    sasha.say "Are you just going to leave our guest on the doorstep or what?"
    hide audrey
    hide sasha
    with moveoutleft
    "Audrey give me an evil-sounding chuckle, as she breezes past me into the hall."
    show bg livingroom
    show audrey at right4
    show sasha at left4
    with fade
    show audrey talkative
    audrey.say "Typical guy, wouldn't you say?"
    audrey.say "Needs a woman to show him how it's done!"
    audrey.say "Speaking of which..."
    show audrey normal
    "And with that, she walks over to where Sasha's standing."
    show audrey blush at center with move
    show sasha shocked
    "As soon as they're face to face, Audrey leans forward and kisses her, full on the lips."
    "All I can do is stand there, stunned into silence as she pushes her tongue into Sasha's mouth."
    "But then it's Sasha's turn to surprise me, as she remains stiff with shock for only a couple of seconds."
    show sasha flirt
    "Then I see her eyes close as she melts into the kiss, showing almost as much passion as Audrey herself."
    "The kiss goes on for what feels like forever, until Audrey breaks away."
    show audrey at right with move
    "At first I think it was her that ended the kiss."
    "But then I see that Sasha has hold of Audrey's hand."
    show sasha normal
    show audrey normal
    "And without another word passing between them, she leads the other girl into the sitting room."
    "I follow in their wake, wondering if either of them even remembers that I'm here at all."
    "Almost as soon as they're in the sitting room, Sasha begins to strip off Audrey's clothes."
    show audrey underwear
    "No resistance is offered as this happens, and soon Audrey starts to return the favor."
    show sasha underwear
    "Any irritation that I felt at being snubbed by the two girls quickly fades away."
    "In fact, it seems to lessen with each and every item of clothing that they strip off of each other."
    show sasha blush
    show audrey blush
    "Pretty soon both of them are standing there, naked save for their underwear."
    "This they slow down and take more time over, as if savoring the task."
    "I guess that after doing the job myself, this is the next best thing I can imagine."
    show sasha naked
    show audrey naked
    "Now that they're stripped down to the skin, the dynamic seems to change."
    "It was Sasha that lead Audrey into the sitting room a moment before."
    "But the roles are reversed as Sasha now finds herself being pulled down onto the sofa."
    "She holds Audrey's eye the entire time, almost as if hypnotized."
    hide audrey
    hide sasha
    with moveoutright
    show jealous missionary kiss normal with fade
    $ renpy.music.set_pan(pan=-0.3,delay=0,channel="sexsfx1")
    $ renpy.music.set_pan(pan=+0.3,delay=0,channel="sexsfx2")
    play sexsfx1 audrey_moans_breathing_slow loop
    "And soon Audrey is laid upon her back, Sasha lowers herself down and begins kissing her."
    "I can see that Audrey has her hand raised to meet the other girl."
    play sexsfx2 sasha_moans_hard_low loop volume 15
    "And then I hear Sasha let out a gentle moan as it reaches between her open thighs."
    "With a skill that almost makes me blush, I watch Audrey stroke the lips of Sasha's pussy."
    "The pale girl grits her teeth, and then bites her lip, as if trying to resist."
    show jealous missionary -kiss
    "But then she begins to cast her head this way and that, tossing her hair as she does so."
    play sexsfx2 sasha_moans_hard_medium loop volume 15
    "Sasha's moans are becoming ever louder, and the smile on Audrey's face more wicked by the moment."
    show jealous missionary squirt ahegao with hpunch
    play sexsfx2 sasha_moans_hard_orgasm volume 15
    "Perhaps in desperation, or perhaps as a kind of retaliation, I see Sasha's hands move quickly."
    "They take hold of Audrey's sizable breasts, massaging and pinching her already erect nipples."
    show jealous missionary kiss closed with dissolve
    play sexsfx1 audrey_moans_discreet_medium loop
    "Now it's Audrey's turn to start moaning, and she does so without restraint."
    "My mouth feels dry as I stand and watch this incredible display being put on before me."
    "And I don't know if I'm dizzy from trying to make myself believe that it's really happening."
    "Or else my head is feeling light on account of the blood running to my cock."
    show jealous missionary -kiss -closed normal with dissolve
    play sexsfx1 audrey_moans_breathing_slow
    play sexsfx2 sasha_breathing volume 15
    "It's only then that I actually notice that, although they're pleasuring each other, their eyes are on me!"
    "Both Sasha and Audrey are staring straight at me, gazes full of almost desperate desire."
    "So they haven't been ignoring me this whole time."
    "Instead they've been doing their best to outdo each other and impress me!"
    "I can almost feel my mood changing from downcast to excited as I watch them."
    "And the change makes me feel like paying them back a little too."
    "So I take my time stripping off my own clothes, and then walk casually over to the sofa."
    scene jealous bj with fade
    stop sexsfx1 fadeout 1
    stop sexsfx2 fadeout 1
    "Sasha and Audrey are soon on their hands and knees, making space for me between them."
    "I sit down with one of them to either side of me, still not favoring one over the other."
    "By now my cock is well and truly standing to attention, and both of them eye it hungrily."
    "Slowly, I glance from one to the other, as if trying to make up my mind."
    "And then I reach out to put my hand on the back of a certain neck..."
    menu:
        "Have Audrey give me a blowjob":
            show jealous bj audreysuck
            play sexsfx1 audrey_moans_blowjob_low loop
            play sexsfx2 sasha_breathing loop volume 15
            "With my hand holding Audrey's head, I push her firmly down and towards my cock."
            "But it only takes the most gentle touch for her to get the picture."
            "And then she eagerly buries her head in my lap, all of her attention on the task ahead."
            show jealous bj audreysuck sashalick
            "Even as I can feel Audrey begin to wrap her lips around the tip, I see the disappointment on Sasha's face."
            "I make to say something that I hope will be of comfort or consolation."
            "But my words are stifled by the sensation of Audrey taking my cock into her mouth."
            "I gasp as she does so, feeling like I'm being swallowed whole."
            play sexsfx1 audrey_moans_blowjob_medium loop
            "Within mere seconds, she seems to have more than half of it in there."
            "The sheer force with which Audrey goes at it takes me by surprise."
            "Her head bobs up and down with an almost frantic motion, making some serious sucking sounds."
            "And yet she shows no sign of being lost for breath or gagging."
            show jealous bj audreysuck audreyclosed
            play sexsfx1 audrey_moans_blowjob_high loop
            "Normally I'd rate a girl's technique on more than one aspect of the blowjob."
            "But as Audrey devotes herself solely to sucking and swallowing, I can't do that."
            "Instead I'm left to simply cling onto the sofa for dear life as she goes at it."
            show jealous bj audreysuck sashanormal
            "For a moment I even manage to forget that Sasha's there at all."
            "The only thing that seems to exist beyond my own body is Audrey's tongue and lips."
            "And with the pace that she's setting, it's not long before I can feel myself cumming..."
            play sexsfx2 sasha_moans_discreet_medium loop volume 15
            menu:
                "Cum in Audrey's mouth":
                    "Before now, I hadn't realized how closely I was keeping pace with Audrey."
                    "Which means that I cum at the same pace too."
                    show jealous bj audreysuck audreyahegao cum with vpunch
                    play sexsfx1 audrey_moans_blowjob_swallow
                    "Without as much as a thought of pulling out, I shoot all I have into her open mouth."
                    with vpunch
                    "Only now does Audrey actually begin to cough and gag."
                    with vpunch
                    "But as my cock is still inside of her mouth, she can't spit it out either."
                    "Instead, she swallows every drop while struggling to keep on breathing around it."
                    show jealous bj -audreysuck audreyclosed
                    "As my cock slides out of her mouth, Audrey begins to take deep, rasping breaths."
                    play sexsfx1 audrey_moans_breathing_fast
                    "And these are almost, but not quite loud enough to conceal Sasha's giggles."
                    pass
                "Cum on Audrey's face" if hero.sexperience >= 10:
                    "Maybe it's the fact that Audrey almost pounced on me that inspires me to do it."
                    "Or maybe I just choose to do it on a sudden whim that comes out of nothing."
                    show jealous bj -audreysuck audreynormal
                    play sexsfx1 audrey_moans_breathing_fast
                    "Either way, I give Audrey no warning as I suddenly yank my cock out of her mouth."
                    "She makes a strangled gagging sound, her face looking stunned as her jaw hangs open."
                    "But there's only a mere matter of seconds before I finally lose it."
                    show jealous bj audreyclosed cum with vpunch
                    play sexsfx1 audrey_generic_oh_2
                    "The streamers of cum that burst out of my cock have nowhere else to go."
                    with vpunch
                    "Each successive one hits Audrey square in the face, until she's literally dripping with the stuff."
                    with vpunch
                    "It hits her forehead, eyes and nose, dripping down as more splashes her features."
                    with vpunch
                    "Some even lands inside of her open mouth, making her swallow on instinct alone."
                    "And all the time this happens, the only sound I can hear is that of Sasha giggling in the background."
                    pass
        "Have Sasha give me a blowjob":
            show jealous bj sashasuck
            play sexsfx2 sasha_blowjob_low volume 10
            play sexsfx1 audrey_moans_breathing_slow
            "With my hand holding Sasha's head, I push her firmly down and towards my cock."
            "I don't honestly know why I've chosen her over Audrey."
            "Maybe it's for the sake of letting her get the upper hand on home turf?"
            "Whatever the reason, Sasha doesn't need any serious convincing."
            "She offers no resistance as I guide her lips towards the head of my cock."
            show jealous bj sashasuck audreylick
            play sexsfx2 sasha_blowjob_medium volume 10
            "Audrey watches with an ironic grin on her face, as if she knows what game I'm playing."
            "But before I can hope to say a single word, I feel Sasha begin to lick at the shaft."
            "I gasp in surprise as she kisses and her way upwards, hands squeezing my balls."
            "And then she takes the head slowly into her mouth, making every small movement feel like she's starting anew."
            "All I can do is close my eyes and hold onto the sofa as Sasha begins to quicken her pace."
            show jealous bj sashasuck sashaclosed
            play sexsfx2 sasha_blowjob_high volume 10
            "Pretty soon I can feel her lips as they travel up and down the shaft."
            "And the tip of my cock almost touches the back of her throat."
            "Sasha's never been a slouch when it comes to giving head."
            "And yet right now, in front of Audrey, she seems to be pulling out all the stops."
            show jealous bj sashasuck audreynormal
            "Part of me wishes that I could see the other girl's face as she watches."
            "But all I can do is remain as still as a statue, letting her go to work on me."
            "And with treatment the likes of this, it's no surprise that I can already feel myself cumming..."
            menu:
                "Cum in Sasha's mouth":
                    "I'm still holding my eyes firmly closed as I lose it inside of Sasha's mouth."
                    "Though she's lucky that my cock isn't that deep when it actually happens."
                    show jealous bj sashasuck sashaahegao cum with vpunch
                    play sexsfx2 sasha_blowjob_swallow volume 10
                    "Instinctively, she wraps her lips around it as the cum fills her mouth."
                    with vpunch
                    "But for all her efforts, some still manages to hit the back of her throat."
                    with vpunch
                    "This makes Sasha gag a little, and swallow the mouthful of cum before she's ready."
                    show jealous bj -sashasuck sashaclosed
                    stop sexsfx2
                    "She pulls up her head, letting my cock drop out of her mouth."
                    "This leaves me almost breathless myself, and feeling more than a little exposed."
                    "I glance up at the sound of chuckling, and see Audrey smiling back at me."
                    "Maybe that look on her face means she's changed her mind about being left out?"
                    pass
                "Cum on Sasha's face" if hero.sexperience >= 10:
                    show jealous bj -sashasuck sashanormal
                    play sexsfx2 sasha_breathing volume 15
                    "I don't know how I manage to do it, but somehow I pull my cock out of Sasha's mouth with mere moments to spare."
                    "But of course, this leaves Sasha with her mouth wide open and no more than an inch from the tip."
                    "So when I cum, she takes the whole thing straight in the face."
                    show jealous bj sashaclosed cum with vpunch
                    play sexsfx1 audrey_generic_oh_2
                    "All that she manages to do is squeeze her eyes shut as the cum hits her."
                    with vpunch
                    "This means that she gets a sizable amount between her lips, as well as over her entire face."
                    "This sets Sasha off coughing for a second time, trying to clear her throat."
                    "I glance up at the sound of chuckling, and see Audrey smiling back at me."
                    "Maybe that look on her face means she's changed her mind about being left out?"
                    pass
    stop sexsfx1 fadeout 1
    stop sexsfx2 fadeout 1
    "Still panting and out of breath from the exertions that came along with the blowjob, I lie back on the sofa."
    "But all it takes is a quick glance from Sasha to Audrey for me to realize that they're not about to call it quits!"
    "I guess that I should have known as much - a threesome seems to involve three times as much work..."
    menu:
        "Fuck Audrey":
            $ renpy.music.set_pan(pan=+0.2,delay=0,channel="sexsfx1")
            $ renpy.music.set_pan(pan=+0.3,delay=0,channel="sexsfx2")
            "I shouldn't really complain, as this is most guy's idea of a dream come true."
            "And maybe it's because all of this is new territory for me that I find myself reaching for Audrey."
            "It's no slight to Sasha, but she's the least familiar thing about this threesome."
            scene jealous cowgirl
            with fade
            "She's not slow to accept the invitation either, coming eagerly into my arms."
            "In fact, she's on me so fast and with such enthusiasm that I'm taken by surprise."
            "Which means I have no time to console Sasha or explain my choice in the matter."
            menu:
                "Fuck Audrey up the ass" if hero.sexperience >= 20:
                    "But for all that I feel the urge to make Audrey the one I take, I'm not totally motivated by desire."
                    "Another part of me thinks that she needs to be taken down a peg or two."
                    "And as I take a hold of her rounded buttocks, the perfect method comes to mind."
                    play sound spank
                    play sexsfx1 audrey_generic_ah_4
                    show jealous cowgirl audreyclosed with hpunch
                    show jealous cowgirl audreyahegao
                    "Remembering Audrey's fondness for being spanked, I quickly slap a hand across her ass."
                    "She immediately jumps and lets out a genuine yelp of surprise."
                    "This makes Sasha flinch in sympathy, and she gives me a questioning look."
                    play sound spank
                    play sexsfx1 audrey_generic_ah_5
                    show jealous cowgirl audreyclosed with hpunch
                    show jealous cowgirl audreyahegao
                    "I shake my head at her as I give Audrey's ass a second slap."
                    "And then she sees the look of helpless ecstasy on the other girl's face."
                    "This seems to be enough to clue her in on the fact that it's a fetish."
                    "And she holds back from stopping me landing the third blow."
                    "But even so, I doubt she realizes that this is only a means to an end."
                    show jealous cowgirl sashasuck
                    play sexsfx2 sasha_blowjob_medium loop volume 10
                    pause 0.7
                    play sound spank
                    play sexsfx1 audrey_generic_ah_5
                    with vpunch
                    "Instead, Sasha consoles herself by licking at my cock as I spank Audrey."
                    "The feeling's so good that on any other occasion, I could have just let her finish me off."
                    "But there's no room for that right now."
                    "Because as soon as the spanking has reduced Audrey to an almost passive state, I make my move."
                    "Firmly parting her buttocks, I find the hole between them with the tip of my cock."
                    show jealous cowgirl anal -sashasuck audreyclosed
                    play sexsfx2 sasha_breathing volume 15
                    play sexsfx1 audrey_moans_pained_low loop
                    "And then I push myself firmly into her, not stopping until I'm already inches deep."
                    "Rather than squealing in pain or making any kind of protest, Audrey simply takes what she's given."
                    "A resigned moan emerges from her lips as I continue to push into her."
                    "It's as if the spanking has softened her up, made her willing and pliable too."
                    "Only when I'm in as deep as I can go does Audrey begin to quiver a little."
                    play sexsfx1 audrey_moans_pained_medium loop
                    "Intrigued, I keep my cock buried in her, pressing my weight up into her the whole time."
                    show jealous cowgirl audreyahegao
                    "Slowly the sound coming out of Audrey and the shaking of her body begin to intensify."
                    play sexsfx1 audrey_moans_pained_high loop
                    "And before too long she's shaking and moaning without me moving a muscle."
                    "I just stay right where I am, letting her motions massage my cock."
                    "This means that by the time Audrey is on the brink of losing it, so am I..."
                    menu:
                        "Cum inside Audrey's ass":
                            "Using the last of my energy, I shove my cock as deep into Audrey's ass as it'll go."
                            show jealous cowgirl audreyahegao cum with hpunch
                            play sexsfx1 audrey_moans_pained_orgasm_1
                            "She moans like a wounded animal as I fill what little space remains with cum."
                            with hpunch
                            "Audrey's stopped even trying to hold herself up by now, her limbs turning to jelly."
                            "And so she's pushed down into the cushions of the sofa as I finish her off."
                            "Sasha watches the whole thing in silence, without saying a word."
                            "I don't know if she's jealous of me fucking Audrey in front of her."
                            "But I think I can see genuine arousal in her eyes as she gazes on the other girl's state of disarray."
                            pass
                        "Cum in Sasha's mouth":
                            "Fucking her up the ass may well have put Audrey in her place."
                            "But I still feel that she needs a little reminder of who's the boss here."
                            show jealous cowgirl -anal
                            "And so I yank my cock out of her ass at the last possible moment."
                            show jealous cowgirl sashasuck
                            play sexsfx2 sasha_blowjob_high volume 10
                            "Audrey groans in surprise, and so does Sasha as I push it into her open mouth."
                            show jealous cowgirl cum sashaahegao with hpunch
                            play sexsfx2 sasha_blowjob_swallow volume 10
                            "Or at least she tries to, as I cum the very second my cock's between her lips."
                            with hpunch
                            "Sasha coughs and gags on the cum as it hits the back of her unsuspecting throat."
                            "And Audrey looks up at me, utterly humiliated at the way I've treated her."
                            "But I know her too well to be fooled, and I can tell just how much she got off on what I just did."
                            return
                        "Cum outside":
                            "I'm torn between shooting my load into Audrey's ass or Sasha's mouth."
                            "So in the end, I decide to choose neither."
                            show jealous cowgirl -anal
                            "I yank my cock out of Audrey's ass at the last possible moment."
                            "She groans in surprise as her hole yawns without its presence."
                            show jealous cowgirl cum sashaahegao with hpunch
                            play sexsfx1 audrey_moans_pained_orgasm_2
                            "But her groan turns into a yelp of shock as she feels the first shot hit the bottom of her chin."
                            "And what's left spatters down onto Audrey's breasts and belly."
                            pass
                    $ audrey.flags.anal += 1
                "Fuck Audrey in the pussy":
                    "There's more to this than simply wanting to fuck Audrey senseless."
                    "I also want to assert myself in this threesome as well."
                    "Just then, my hand happens to make contact with her backside."
                    show jealous cowgirl audreyahegao with fade
                    "She jumps and yelps, the sound betraying a genuine thrill."
                    "It's then that I remember how much Audrey's into that kind of thing."
                    play sound spank
                    play sexsfx1 audrey_generic_ah_5
                    show jealous cowgirl audreyclosed with hpunch
                    show jealous cowgirl audreyahegao
                    "I give her ass a real slap, hearing her yelp over the cracking sound."
                    "Sasha seems to catch on quickly, letting me spank Audrey without question."
                    show jealous cowgirl sashasuck
                    play sexsfx2 sasha_blowjob_medium loop volume 10
                    "Instead she starts to suck on my cock again, gazing at the other girl's dripping pussy the whole time."
                    "As much as Audrey's getting off on the slaps, Sasha seems equally turned-on by watching."
                    show jealous cowgirl audreyclosed
                    "By the time I've spanked her maybe half a dozen times, Audrey's panting and helpless."
                    show jealous cowgirl -sashasuck
                    play sexsfx2 sasha_breathing volume 15
                    "Sasha reluctantly surrenders my cock, and I waste no time in finding what I'm looking for."
                    "Audrey offers no sign of resistance as I line myself up."
                    show jealous cowgirl vaginal audreynormal
                    play sexsfx1 audrey_moans_discreet_medium loop
                    "As I suspected, Audrey's pussy is wet and slick enough for me to push right on in there."
                    "And so that's exactly what I do, not stopping until I'm in up to my balls."
                    play sexsfx1 audrey_moans_happy_medium loop
                    "Audrey quivers and lets out a series of low cries as I begin to move in and out."
                    "But not once does she try to stop me, simply taking what she's given."
                    "Pretty soon I'm pounding her with all the strength I can summon."
                    show jealous cowgirl audreyahegao
                    play sexsfx1 audrey_moans_happy_high loop
                    "And those low cries have turned into loud, helpless sounds that are almost screams."
                    "I can feel Audrey's limbs beginning to wobble and shake above me."
                    "Which makes me wonder how much longer she can keep up this kind of pace."
                    "She's also sweating so much that it's getting hard for me to keep her upright."
                    "But far from being worried about her collapsing, I'm more concerned with my urgent need to cum."
                    "At this rate, she could actually end up sliding off of my cock before I do so."
                    "That means that I have to make a decision as to how I use the last of my strength."
                    "And I have to make it right now!"
                    menu:
                        "Cum inside Audrey's pussy":
                            "I use the very last of my energy for one final push into Audrey's pussy."
                            show jealous cowgirl audreyahegao
                            "She cries out, louder than before, as all that I have fills her."
                            show jealous cowgirl cum with hpunch
                            play sexsfx1 audrey_moans_happy_orgasm_1
                            "Audrey cums as I do this, her tortured muscles seeming to give up the fight."
                            "She slides off of my cock and collapses into a sweaty heap on the sofa."
                            "Sasha holds her tongue throughout the whole thing, not saying a word."
                            "If she's at all jealous of me choosing Audrey over her, she's hiding it well."
                            "And I can see from the look in her eyes that she got off on watching it too."
                            pass
                        "Cum in Sasha's mouth":
                            "There's no way that pounding Audrey into submission with my cock is enough."
                            "Even with the humiliation of the spanking, it's still basically what she wants."
                            show jealous cowgirl -vaginal outside
                            "That's why I pull out of her pussy at the very last moment."
                            "I hear Audrey groan in surprise and disappointment."
                            show jealous cowgirl sashasuck -outside
                            play sexsfx2 sasha_blowjob_high volume 10
                            "And maybe Sasha tries to say something too, but then she finds my cock between her lips."
                            show jealous cowgirl cum sashaahegao with hpunch
                            play sexsfx2 sasha_blowjob_swallow
                            "All she has time to do is cough and splutter as she's forced to swallow my entire load."
                            "I see Audrey glance down as the other girl does this."
                            "And I wonder if she's more humiliated or turned-on by the sight."
                            pass
                        "Cum outside":
                            "I feel like I have to choose between which of the two girls I leave out at the end."
                            "But then a thought occurs to me - do I really have to choose?"
                            show jealous cowgirl -vaginal
                            queue sexsfx1 audrey_generic_oh_1
                            "At the very last moment, I pull my cock out of Audrey's pussy."
                            "I hear her groan in surprise and disappointment at the sensation."
                            show jealous cowgirl cum sashaahegao with hpunch
                            play sexsfx1 audrey_generic_oh_5
                            "But her groan turns into a yelp of shock as she feels the first shot hit the bottom of her chin."
                            "And what's left spatters down onto Audrey's breasts and belly."
                            pass
        "Fuck Sasha":
            "Man, why am I even complaining?"
            "This is most guy's idea of a dream come true."
            "The chance the spice things up with two girls and a whole new experience."
            scene jealous doggy
            show jealous doggy audrey sasha mike
            with fade
            "Still, I find myself reaching for Sasha first."
            "Maybe because of the fact that she's the most familiar of the two."
            "And she doesn't need to be encouraged either."
            scene jealous doggy
            show jealous doggy mike audreyfinger
            "Taking the chance to get one over on Audrey in an instant."
            scene jealous doggy
            show jealous doggy audreyfinger outside with dissolve
            "Which means I have no time to explain my choice to either of them."
            menu:
                "Fuck Sasha up the ass" if hero.sexperience >= 20:
                    "But just because I've chosen to fuck Sasha, that doesn't mean I'm keeping everything familiar."
                    "The sight of her tight little ass is just too much temptation, and I can't resist."
                    "I hear Sasha yelp in surprise as I take a firm hold of her buttocks."
                    scene jealous doggy
                    show jealous doggy mike anal audreyfinger sashaclosed
                    "And I see her bite down on her lip as I begin to push the head of my cock straight up there."
                    "The natural resistance of her muscles makes the process slow and gradual."
                    "But for me, that just means that there's so much more time to enjoy the sensation."
                    "By now, I can't see the expression on Sasha's face, only hear her moans."
                    "Audrey, on the other hand, makes a point of watching the other girl's features intently."
                    "In this way, the arousal that Audrey begins to show acts almost like a mirror for me."
                    "The more delight and fascination that she shows, the more I know that Sasha's feeling it too."
                    "In fact, pretty soon I'm getting as turned-on by Audrey's face as I am by Sasha's ass."
                    "I watch as she licks her lips, hands creeping towards her own pussy."
                    "Shit - even watching her get turned-on is a massive turn-on!"
                    scene jealous doggy
                    show jealous doggy mike outside sashaahegao with dissolve
                    "Unable to keep my eyes off of Audrey, I find myself pulling out of Sasha's ass."
                    "She moans at the sensation, legs quivering as her muscles do the same."
                    "Seeing this, Audrey's eyes home in on my freed cock."
                    scene jealous doggy
                    show jealous doggy mike audreysuck audreyclosed with dissolve
                    play sexsfx1 audrey_moans_blowjob_medium loop
                    "And then she's on it before I can say as much as a single word."
                    "The fact it's just been up Sasha's ass only seems to make Audrey all the more eager."
                    scene jealous doggy
                    show jealous doggy mike audreysuck audreyahegao
                    "She licks and sucks away as if her very life depended on it."
                    "In fact, Audrey's going at it with such gusto that I can already feel myself losing it!"
                    "If she keeps this up for too much longer, there's nothing I can do to keep a lid on."
                    "I need to make up my mind, right here and now."
                    "Who's getting this one, and where!"
                    play sexsfx1 audrey_moans_blowjob_high loop
                    menu:
                        "Cum in Sasha's ass":
                            "I don't know why, but I feel like I have to finish what I already started."
                            scene jealous doggy
                            show jealous doggy mike outside
                            play sexsfx1 audrey_moans_breathing_fast
                            "And so now it's Audrey's turn to be suddenly deprived of my cock."
                            "She gasps and begins to cough as I pull it straight out of her mouth."
                            "Luckily for me, the muscles of Sasha's ass haven't had time to recover."
                            scene jealous doggy
                            show jealous doggy mike anal sashaahegao
                            play sexsfx2 sasha_moans_hard_high
                            "This means that I can force my way back up there without too much effort."
                            play sexsfx2 sasha_moans_hard_orgasm volume 10
                            scene jealous doggy
                            show jealous doggy mike anal cum with vpunch
                            "She moans once more as I'm back inside of her, and then again when I come a moment later."
                            "Audrey watches the whole thing, a mixture of disappointment and arousal painted on her face."
                            pass
                        "Cum in Audrey's mouth":
                            "It's no good."
                            "Well, actually it's too good."
                            "And that's the problem!"
                            "There's just no way that I can bring myself to stop what Audrey's doing to me."
                            scene jealous doggy
                            show jealous doggy mike audreysuck cum sashaclosed with vpunch
                            play sexsfx1 audrey_moans_blowjob_swallow
                            "So I end up cumming straight into her mouth as she blows me."
                            "I almost expect her to choke on it, but somehow she seems more than ready."
                            "Audrey finishes me off like a pro, as Sasha looks on helpless to intervene."
                            pass
                        "Cum over Sasha and Audrey":
                            "How can I possibly choose between Audrey's mouth and Sasha's ass?"
                            "That's why, in the end, I decide not to."
                            scene jealous doggy
                            show jealous doggy mike outside audreyfinger audreyahegao sashaclosed
                            play sexsfx1 audrey_moans_breathing_fast
                            play sexsfx2 sasha_breathing volume 15
                            "I pull my cock out of Audrey's mouth just in time."
                            scene jealous doggy
                            show jealous doggy cum sashaahegao
                            with vpunch
                            pause 0.5
                            scene jealous doggy
                            show jealous doggy mike audreyfinger onbody audreyclosed sashaclosed
                            with vpunch
                            "And a second later, I cum over the pair of them."
                            "Sasha's buttocks takes the most of it, covering her in a sticky glaze."
                            "But enough spatters into Audrey's mouth to make her cry out in surprise."
                            pass
                    $ sasha.flags.anal += 1
                "Fuck Sasha in the pussy":
                    "Maybe it's the fact that so much of this situation is new that makes me choose to fuck Sasha."
                    "And maybe it's the same reason that I find myself beating a path to her pussy as well."
                    "Whatever the reason, there's something wonderful about the familiar feeling of it."
                    "Sasha's pussy just feels so right, and I already know that she fits me like a glove."
                    scene jealous doggy
                    show jealous doggy mike vaginal audreyfinger
                    play sexsfx2 sasha_moans_light_low loop volume 10
                    "Almost as soon as she feels the sensation of my cock against her lips, I hear her moan."
                    "And then she wriggles herself backwards, meaning that most of the work is done for me."
                    "My cock slides straight between Sasha's already slick lips."
                    "I begin to thrust in and out of her almost without thinking."
                    "And she responds by tossing her head this way and that, showing how much she enjoys being ridden."
                    "This display of mutual arousal seems to be going down well with Audrey too."
                    "I hear her making similarly pleasant sounds, and glance up to see for myself."
                    "When my eyes settle on her, I can see that Audrey has one hand on her own pussy."
                    "She strokes herself almost to the same rhythm with which I'm fucking Sasha."
                    "But when she notices me watching her, Audrey lifts her fingers to her mouth."
                    "And then she starts to lick them in the most provocative manner possible."
                    scene jealous doggy
                    show jealous doggy mike outside audreyfinger sashaahegao with dissolve
                    play sexsfx2 sasha_breathing volume 15
                    "Intrigued, I find myself pulling my cock out of Sasha and pointing it towards Audrey."
                    scene jealous doggy
                    show jealous doggy mike audreysuck audreyclosed
                    play sexsfx1 audrey_moans_blowjob_high
                    "Not needing to be invited, she immediately bends down and wraps her lips around the head."
                    scene jealous doggy
                    show jealous doggy mike audreysuck sashaclosed
                    "I only half hear the disappointed sound that Sasha makes as she sees what I just did."
                    "But even if I wanted to, there's no way I could switch back to her again."
                    scene jealous doggy
                    show jealous doggy mike audreysuck audreyahegao sashaclosed
                    "By now, Audrey has my cock so deep into her mouth that she's practically deep-throating me."
                    "Given the chance to upstage Sasha so late into the game, she seems determined to play for the win."
                    "Whatever I end up deciding to do, I'm going to have to make a decision soon."
                    "As I can already feel myself beginning to cum!"
                    menu:
                        "Cum in Sasha's pussy":
                            "Suddenly I have the urge to finish this thing the way I started it."
                            scene jealous doggy
                            show jealous doggy mike outside
                            "So this time, I yank my cock out of Audrey's mouth."
                            "She gasps and coughs as I do this, taken completely by surprise."
                            "Luckily for me, Sasha's pussy is still as slick as ever."
                            scene jealous doggy
                            show jealous doggy mike vaginal sashaclosed
                            "And I slide back in there as smoothly as the first time."
                            scene jealous doggy
                            show jealous doggy mike vaginal sashaahegao cum with vpunch
                            play sexsfx2 sasha_moans_hard_orgasm volume 10
                            "Her moans resume the moment that I do so, getting even louder as I cum inside of her."
                            "Audrey watches the whole thing, a mixture of disappointment and arousal painted on her face."
                            pass
                        "Cum in Audrey's mouth":
                            "There's no time to even think of pulling my cock out of Audrey's mouth."
                            "It's in too deep and I'm already starting to cum a couple of seconds later."
                            "All I can hope to do is hang on in there and ride it out!"
                            scene jealous doggy
                            show jealous doggy mike audreysuck cum audreyahegao sashaclosed
                            with vpunch
                            "Audrey doesn't as much as gag once as I almost shoot my load straight down her throat."
                            play sexsfx2 audrey_moans_blowjob_swallow
                            "Instead, she swallows every last drop that I have to give her."
                            "And that leaves Sasha to just sit there, watching the whole thing."
                            "She smiles, though I can see the disappointment she's hiding in her eyes."
                            pass
                        "Cum over Sasha and Audrey":
                            "How can I possibly choose between Audrey's mouth and Sasha's pussy?"
                            "And so, in the end, I decide that I won't."
                            scene jealous doggy
                            show jealous doggy mike outside audreyfinger
                            "I manage to get my cock out of Audrey's mouth a moment before I cum."
                            scene jealous doggy
                            show jealous doggy mike outside cum audreyfinger sashanormal audreynormal
                            play sexsfx1 audrey_generic_oh_2
                            with vpunch
                            pause 0.5
                            scene jealous doggy
                            show jealous doggy mike outside onbody
                            with vpunch
                            "So both of them have a look of surprise on their faces as I lost it."
                            "Sasha takes the lion's share, covering her ass."
                            "And enough splashes into Audrey's mouth to make her yelp and twitch."
                            pass
    call stop_all_sfx from _call_stop_all_sfx_16
    $ renpy.music.set_pan(pan=0,delay=0,channel="sexsfx1")
    $ renpy.music.set_pan(pan=0,delay=0,channel="sexsfx2")
    $ sasha.sexperience += 1
    $ audrey.sexperience += 1
    $ game.pass_time(4)
    $ Harem.join_by_name("jealous", "audrey", "sasha")
    if renpy.has_label("jealous_harem_achievement_2") and not game.flags.cheat:
        call jealous_harem_achievement_2 from _call_jealous_harem_achievement_2
    return

label audrey_sasha_propose_male:
    "Being faced with the task of choosing the right moment to propose to either Audrey or Sasha."
    "Now that would be a major challenge for a guy to pull off without ending up in a serious mess!"
    "Both of those girls are a handful in their own right."
    "On the one hand you have Audrey, a minx that likes nothing more than creating chaos for its own sake."
    "And on the other there's Sasha, a cocksure rock-chick that isn't afraid to stand up to anyone."
    "So spare a thought for me, because I'm the guy that's going to have to propose to them both."
    "At the same time too!"
    "I've thought about times and places, as well as what I should do and say."
    "But no matter what I come up with that'll work for one, it just won't for the other."
    "So after spending what feels like an age racking my brain, there's only one solution."
    "I have to keep it simple and I have to strike as fast as lightning too."
    "And don't be alarmed if this is sounding more like a commando raid than a proposal."
    "That's just the kind of girls I'm dealing with here!"
    show sasha casual annoyed at right5 with dissolve
    sasha.say "The jerk did what?!?"
    show audrey casual normal at left5 with dissolve
    audrey.say "Propositioned me - right there by the photocopier!"
    show sasha normal
    sasha.say "I hope you put him right in his place, Audrey!"
    audrey.say "Oh yeah, you're gonna love this."
    show audrey joke
    audrey.say "I reached down and grabbed his balls."
    show sasha normal
    sasha.say "Yeah, yeah?"
    audrey.say "And then I said..."
    show audrey surprised at startle
    audrey.say "[hero.name], what the fuck are you doing?!?"
    show fx question at right5
    sasha.say "Huh?"
    show sasha annoyed
    sasha.say "I thought you said this Dwayne creep was your boss?"
    audrey.say "No, no, no!"
    audrey.say "Check this shit out down here!"
    "In the time that Audrey and Sasha have been talking, I've gone down on one knee."
    show audrey normal
    show sasha normal
    "Now I find myself looking up at them, with the rings I picked out in my hand."
    "And it doesn't help that they're both looking at me like I've lost my mind."
    "But I guess the only thing I can do now is press on."
    "So I hold up the rings and put on what I hope is a winning smile."
    mike.say "Erm..."
    mike.say "Audrey..."
    mike.say "Sasha..."
    mike.say "Will you marry me?"
    "I don't know what I was expecting to happen after I popped the question."
    show sasha happy at startle
    show audrey happy at startle
    "But it definitely wasn't for Audrey and Sasha to burst out laughing!"
    show sasha joke
    sasha.say "Oh man..."
    sasha.say "That's a good one, [hero.name]!"
    show audrey joke
    audrey.say "Yeah..."
    audrey.say "You almost had me convinced you were serious!"
    "I can only guess that the pair of them see the pain in my eyes a moment later."
    show sasha sad
    show audrey sad
    "Because they exchange a worried glance and then look back to me."
    show audrey surprised
    audrey.say "Oh shit..."
    audrey.say "You are serious, aren't you!"
    mike.say "Erm...yeah."
    mike.say "I kind of am!"
    if audrey.love >= 195 and sasha.love >= 195:
        audrey.say "You are?"
        show audrey normal
        audrey.say "You really are?"
        audrey.say "In that case, my answer's yes!"
        show audrey happy
        audrey.say "Yes, I will marry you!"
        show sasha surprised
        "Sasha seems as surprised as me by Audrey's sudden change in tone."
        show sasha normal
        "But it only takes her a few seconds to recover and speak up for herself."
        sasha.say "Why didn't you say that from the start?"
        sasha.say "Of course I'll marry you, [hero.name]!"
        show sasha happy
        sasha.say "I was starting to think you'd never ask."
        "The flood of relief that sweeps over me is pretty strong."
        show audrey normal
        show sasha normal
        "So strong in fact that I feel a little dizzy as I get to my feet."
        "And I need a little help to slide the rings onto their fingers too."
        mike.say "Phew..."
        mike.say "That's a relief."
        mike.say "I was afraid you were going to say no!"
        show audrey happy at startle
        show sasha happy at startle
        "Audrey and Sasha laugh again."
        "But this time I feel like I'm in on the joke."
        show audrey normal
        audrey.say "What, you think I'm ever going to find anyone else like you?"
        audrey.say "Someone that's prepared to put up with my level of bullshit?"
        show sasha normal
        sasha.say "You were my best friend before we got together, [hero.name]."
        sasha.say "And we've only grown closer since then."
        sasha.say "There's nobody else I'd rather spend my life with."
        $ audrey.set_fiance()
        $ sasha.set_fiance()
    elif audrey.love >= 195 and sasha.love < 195:
        audrey.say "You are?"
        show audrey normal
        audrey.say "You really are?"
        audrey.say "In that case, my answer's yes!"
        show audrey happy
        audrey.say "Yes, I will marry you!"
        show sasha surprised
        "Sasha seems as surprised as me by Audrey's sudden change in tone."
        show sasha sad
        "But it only takes her a few seconds to recover and speak up for herself."
        sasha.say "Oh, [hero.name]!"
        show sasha normal
        sasha.say "What did you have to go and do that for?"
        sasha.say "I don't want to get married."
        show audrey normal
        show sasha annoyed
        sasha.say "I have the band and a hundred other things going on right now!"
        "I spent all of my time worrying about them both saying no."
        "I never thought of what would happen if only one of them did!"
        "My head's spinning as I get to my feet."
        "And I have no idea what to do next."
        mike.say "Aren't we a good match, Sasha?"
        mike.say "Don't we work as a threesome?"
        sasha.say "Face it, [hero.name] - it'd never work."
        show sasha sad
        sasha.say "We're just way too different people."
        audrey.say "I want to marry you, [hero.name]."
        show audrey happy
        show sasha normal
        audrey.say "What, you think I'm ever going to find anyone else like you?"
        audrey.say "Someone that's prepared to put up with my level of bullshit?"
        "Audrey smiles as I slide the ring onto her finger."
        show sasha annoyed
        "But Sasha looks on with a frown on her face."
        "I don't know where this leaves us with Sasha."
        "And I don't know where this leaves us as a threesome either."
        $ audrey.set_fiance()
        $ sasha.love -= 25
        $ sasha.sub -= 25
    elif sasha.love >= 195 and audrey.love < 195:
        audrey.say "You are?"
        show audrey normal
        audrey.say "You really are?"
        audrey.say "Oops!"
        show audrey frown
        audrey.say "You kinda made a fool of yourself - because the answer's no!"
        "Sasha seems to take a few more seconds to recover then Audrey."
        "But as soon as she does, she speaks up for herself."
        sasha.say "Why didn't you say that from the start?"
        show sasha normal
        sasha.say "Of course I'll marry you, [hero.name]!"
        show sasha happy
        show audrey normal
        sasha.say "I was starting to think you'd never ask."
        "I spent all of my time worrying about them both saying no."
        "I never thought of what would happen if only one of them did!"
        "My head's spinning as I get to my feet."
        "And I have no idea what to do next."
        show sasha normal
        mike.say "Aren't we a good match, Audrey?"
        mike.say "Don't we work as a threesome?"
        audrey.say "We work as a threesome, yeah."
        show audrey annoyed
        audrey.say "But not as a three-way marriage!"
        sasha.say "I want to marry you, [hero.name]."
        sasha.say "You were my best friend before we got together, [hero.name]."
        show sasha happy
        sasha.say "And we've only grown closer since then."
        sasha.say "There's nobody else I'd rather spend my life with."
        "Sasha smiles as I slide the ring onto her finger."
        "But Audrey looks on with a frown on her face."
        "I don't know where this leaves us with Audrey."
        "And I don't know where this leaves us as a threesome either."
        $ sasha.set_fiance()
        $ audrey.love -= 25
        $ audrey.sub -= 25
    else:
        audrey.say "You are?"
        show audrey normal
        audrey.say "You really are?"
        audrey.say "Oops!"
        show audrey frown
        audrey.say "You kinda made a fool of yourself - because the answer's no!"
        "Sasha seems to take a few more seconds to recover than Audrey."
        "But as soon as she does, she speaks up for herself."
        sasha.say "Oh, [hero.name]!"
        show sasha sad
        sasha.say "What did you have to go and do that for?"
        sasha.say "I don't want to get married."
        show sasha annoyed
        sasha.say "I have the band and a hundred other things going on right now!"
        "I know that I spent so much time worrying about this very thing happening."
        "But even so, it does nothing to lessen the effect their answer has on me."
        "As I get to my feet, I feel like I've been punched in the gut."
        "Like my heart's been ripped right out of my chest."
        mike.say "I..."
        mike.say "I thought one of you might say yes!"
        mike.say "Aren't we a good match?"
        mike.say "Don't we work as a threesome?"
        show audrey at startle
        show sasha at startle
        "Audrey and Sasha shake their heads."
        audrey.say "We work as a threesome, yeah."
        show audrey annoyed
        audrey.say "But not as a three-way marriage!"
        sasha.say "Face it, [hero.name] - it'd never work."
        show sasha sad
        sasha.say "We're just way too different people."
        $ audrey.love -= 25
        $ audrey.sub -= 25
        $ sasha.love -= 25
        $ sasha.sub -= 25
    return

label audrey_sasha_male_ending:

    if renpy.has_label("jealous_harem_achievement_3") and not game.flags.cheat:
        call jealous_harem_achievement_3 from _call_jealous_harem_achievement_3
    $ game.hour = 16
    $ game.room = "church"
    scene bg church wedding with fade
    "Part of me can't actually believe that we've made it this far."
    "But turning my head allows me to see the chapel behind me."
    "It's packed to the rafters with guests and the atmosphere's electric."
    "So I guess that I'm not dreaming after all."
    "It's really happening - I'm marrying Audrey and Sasha!"
    "I turn my head back, feeling how tight the collar of my shirt is."
    "Damn it - this thing was supposed to be tailored for me to wear!"
    "But it feels like it's choking the life out of me right now."
    "Maybe that's just the nerves..."
    "Just then the sound of music fill the chapel, snapping me out of it."
    "The entire crowd turns their heads as one, gazing at the doors."
    "And I do the same, straining to see the moment my brides walk in."
    show audrey wedding happy at left4
    show sasha wedding happy at right4
    with dissolve
    "Of course, Audrey and Sasha stride into the chapel side by side."
    "Neither of them was ever going to let the other one take the lead."
    "But I soon forget all about the rivalry that exists between them."
    "And that's simply because they both look so stunningly beautiful."
    "Audrey's still got that smirking look of mischief on her face."
    "The same one she had the first day I met her at work."
    "And she's walking with that same confidence too."
    "Almost like she's challenging everyone that makes eye-contact."
    "Even her wedding dress can't hide her true nature as a trouble-maker!"
    if audrey.is_visibly_pregnant:
        "And that's made all the more true thanks to her swelling belly."
        "Audrey makes no effort to hide the fact she's pregnant."
        "Turning that into a challenge for the onlookers too."
    "Sasha is another story entirely, looking like a goth-metal princess!"
    "Every move she makes reminds me of the times I've seen her on stage."
    "And she swaggers like this is just another gig with an audience to entertain."
    if sasha.is_visibly_pregnant:
        "I almost have to remind myself that she's pregnant."
        "But then I see Sasha's hand resting on her belly."
        "And I smile as I remember all the fun we had getting her there!"
    "The smile on my face must be like a mile wide."
    "Because by the time they make it to the alter, Audrey and Sasha are sniggering at me."
    audrey.say "Wow, [hero.name]..."
    show audrey joke
    audrey.say "You look like you just told one of your lamest jokes!"
    sasha.say "Oh, man!"
    show sasha joke
    sasha.say "You are kinda grinning like a fool!"
    "I open my mouth to say something in response."
    "And I'm sure it would have been witty in the extreme."
    "Just the kind of comeback to put Audrey and Sasha in their places."
    "But I get interrupted before I can actually come out with it."
    "Priest" "Ahem..."
    "At the sound of the priest's cough, Sasha and I stand to attention."
    "Hell, even Audrey seems to forget about wise-cracking for a moment!"
    show audrey normal
    show sasha normal
    "Priest" "Shall we begin?"
    "This gets a round of nods, to which the priest adds his own."
    "Priest" "Very good..."
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To join together these three people..."
    "Priest" "In the bounds of holy matrimony."
    "You know how the rest of the ceremony goes."
    "Nothing really interesting happens until we get to the vows."
    "Priest" "Do you, Sasha..."
    "Priest" "Take these two people..."
    "Priest" "To be your lawful, wedded partners?"
    show sasha happy
    sasha.say "I do."
    "Priest" "Very good."
    "Priest" "Do you, Audrey..."
    "Priest" "Take these two people..."
    "Priest" "To be your lawful, wedded partners?"
    show audrey happy
    audrey.say "I do."
    "Priest" "And do you, [hero.name]..."
    "Priest" "Take these two people..."
    "Priest" "To be your lawful, wedded partners?"
    mike.say "I do."
    "Priest" "I call upon all those here present..."
    "Priest" "That if you know of any lawful reason..."
    "Priest" "Why these three may not be married..."
    "Priest" "Speak now, or forever hold your peace!"
    "The guests look around, the usual ripple of laughter filling the chapel."
    "And I just keep on smiling as the customary pause continues."
    "Because this should just be a formality, you know?"
    "There's nobody that I can think of who'd want to crash the wedding."
    "And I'm proved right a few moments later."
    "Priest" "Very well."
    "Priest" "It is therefore my pleasure to pronounce you married."
    "Priest" "You may celebrate in a way that you find fitting."
    "I'm expecting us to have a restrained little kiss."
    "Something respectful so that we can save the real action for later."
    "You know, when the three of us are alone?"
    show audrey at center, zoomAt(2, (440, 1380))
    show sasha at center, zoomAt(2, (840, 1380))
    with hpunch
    "But Audrey and Sasha pretty much pounce on me!"
    "They must have planned this out ahead of time."
    "Because they move almost as one, catching me off-guard."
    "But that doesn't mean I'm complaining about what happens next."
    "Audrey and Sasha wrap themselves around me, hugging me tightly."
    "Then they take turns kissing me and each other."
    "And while all that's happening, I honestly forget where I am."
    "So it's a genuine shock to see the guests looking on when it's over."

    scene bg park
    show audrey casual at left5
    with fade
    audrey.say "No worries, Sasha..."
    audrey.say "I can handle this on my own."
    sasha.say "Whoa!"
    show sasha casual annoyed at right5
    sasha.say "I don't think so, Audrey!"
    sasha.say "You're not sneaking this one past me."
    audrey.say "Ah, whatever..."
    show audrey joke
    audrey.say "But you can't blame a girl for trying!"
    sasha.say "Yeah...you're pretty trying, Audrey!"
    audrey.say "Ouch!"
    show audrey mock
    audrey.say "Touche, Sasha - you're getting better at this!"
    sasha.say "I have a pretty good teacher, Audrey!"
    show sasha joke
    sasha.say "Huh?"
    show audrey normal
    sasha.say "What's up, Audrey?"
    sasha.say "You look like you were waiting for something back there!"
    audrey.say "Oh yeah..."
    audrey.say "I was just waiting for [hero.name] to jump in, you know?"
    show sasha normal
    sasha.say "Actually, I do."
    sasha.say "This is where he'd be getting in-between us."
    sasha.say "Keeping the peace and trying to get us to play nice!"
    audrey.say "Aww..."
    show audrey annoyed
    audrey.say "I kinda wish he was here right now."
    show sasha annoyed
    sasha.say "Yeah, it's not the same without him around."
    audrey.say "Not the same?"
    show audrey normal
    audrey.say "Face it, Sasha - this thing wouldn't work without him!"
    audrey.say "I mean, we're not exactly compatible on paper."
    show sasha normal
    sasha.say "You can say that again, Audrey!"
    sasha.say "But somehow [hero.name] seems to make it work."
    audrey.say "Yeah..."
    audrey.say "But we don't have to tell him that!"
    sasha.say "Oh hell no!"
    show sasha happy
    sasha.say "He is a pretty cool husband though."
    if audrey.sub == sasha.sub:
        audrey.say "He'd have to be to let us both stay home while he works!"
        sasha.say "Hmm..."
        sasha.say "Some guys would really get off on that, you know?"
        show audrey happy
        audrey.say "Yeah, but you know [hero.name]'s not one of them."
        audrey.say "I feel like he'd have been cool with us keeping our jobs."
        audrey.say "Even getting new jobs if the right ones came along."
    elif audrey.sub > sasha.sub:
        audrey.say "I gotta say it was cool of him to let me quit work."
        show audrey happy
        audrey.say "I never really liked that place, and it was really getting to me."
        audrey.say "Don't know if I want to be a housewife forever though."
        audrey.say "Maybe just until the right job comes along?"
        sasha.say "I'd have put my foot down if he'd wanted me to quit the band."
        sasha.say "But he's been so supportive, coming along to my gigs and everything."
        sasha.say "It's almost like my husband is also my biggest fan!"
    else:
        audrey.say "Sure he is."
        show audrey happy
        audrey.say "He was totally cool with me keeping my career."
        audrey.say "I know a lot of guys that would have made me quit."
        audrey.say "Like having a wife that works makes them less of a man!"
        sasha.say "I expected him to argue with me when I said I wanted to take a break."
        sasha.say "[hero.name]'s like the biggest fan of my band, you know?"
        sasha.say "But he was totally fine with it."
        sasha.say "Just told me to take all the time I needed."

    show audrey annoyed
    audrey.say "Urgh..."
    audrey.say "We're being so nice to him."
    audrey.say "It just doesn't feel right somehow!"
    show sasha joke
    sasha.say "Well you're not going to like what I'm about to say next then!"
    sasha.say "[hero.name]'s really made us feel like a family."
    sasha.say "Not just a threesome that tied the knot - a real family unit."
    audrey.say "Argh!"
    audrey.say "Stop it, Sasha!"
    show audrey normal
    audrey.say "Stop saying things I have to agree with!"
    if (audrey.is_visibly_pregnant or audrey.flags.mikeBabies >= 1) or (sasha.is_visibly_pregnant or sasha.flags.mikeBabies >= 1):
        if audrey.is_visibly_pregnant or audrey.flags.mikeBabies >= 1:
            audrey.say "Well, I guess [hero.name] is a good father."
            audrey.say "And little Tommy adores his daddy."
        if sasha.is_visibly_pregnant or sasha.flags.mikeBabies >= 1:
            sasha.say "I used to think that boys were easier to raise than girls."
            show sasha happy
            sasha.say "But wow, did Billy cure me of that one pretty quickly!"
    else:
        audrey.say "Sasha..."
        audrey.say "Do you..."
        show sasha normal
        sasha.say "Do I what, Audrey?"
        audrey.say "Do you kind of think about having kids with him?"
        sasha.say "Well you obviously do!"
        sasha.say "But yeah, I do all the time."
    audrey.say "This is crazy, Sasha."
    show audrey normal
    audrey.say "It sounds like we're living in a fairy-tale!"
    sasha.say "I know, I know - and we're not!"
    show sasha normal
    sasha.say "[hero.name]'s still a typical guy."
    sasha.say "Smelly, messy and gross!"
    show audrey annoyed
    audrey.say "Yeah, and he still thinks with his dick!"
    audrey.say "But the weird thing is..."
    show audrey normal
    audrey.say "I wouldn't change him, you know?"
    sasha.say "Well..."
    show sasha joke
    sasha.say "Maybe I'd make him fart a little less, you think?"
    audrey.say "Oh yeah!"
    show audrey joke
    audrey.say "That's the exception to the rule!"
    $ game.set_new_game_plus()
    $ renpy.full_restart()
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
