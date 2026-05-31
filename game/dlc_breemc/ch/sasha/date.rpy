label sasha_date_intro_halloween_female:



label sasha_halloween_invitation_female:
    show sasha
    "Almost the moment I agreed to the Halloween party, I knew who I wanted to invite."
    "I might have been joking about Sasha and [mike.name] getting together when they pitched the party."
    "But that really was nothing more than a joke, because it's Sasha I want to be my date!"
    "Though I couldn't just come out and ask her there, right in front of [mike.name]."
    "No, I needed to be able to regroup and start making plans on where and when to ask him."
    "And that's just what I do, choosing my moment carefully so as to maximise my chances of success."
    "Don't get me wrong, I'm pretty sure Sasha will want to be my date."
    "But there's nothing wrong with stacking the deck in my favour, now is there?"
    "So when I think that the time is just right, I bring it up with Sasha."
    bree.say "Sasha..."
    bree.say "Have you thought about inviting anyone to the Halloween party?"
    bree.say "I'm just curious, because I had someone in mind myself."
    "Sasha looks up at me with genuine interest in her eyes."
    sasha.say "Huh..."
    sasha.say "You know what, [hero.name]..."
    sasha.say "I've been so wrapped up in organising the party, it totally slipped my mind!"
    "I can't help but leap on the opportunity Sasha just handed me."
    "But I at least try to sound casual as I make my pitch."
    bree.say "Well, Sasha..."
    bree.say "What if I were to tell you that I have the perfect solution?"
    "Sasha narrows her eyes at this."
    "But I can see that she's interested in what I have to say."
    sasha.say "Well you have to tell me what it is now, [hero.name]!"
    sasha.say "You can't leave me hanging like that."
    bree.say "Okay, Sasha..."
    bree.say "How about you come to the party as my date?"
    bree.say "It's a simple and elegant solution."
    bree.say "Like killing two birds with one stone!"
    "Sasha raises a single eyebrow and lets out a wry chuckle."
    sasha.say "Interesting choice of metaphor there, [hero.name]!"
    "I can't help blushing a little."
    "But I do the best I can to ignore it and push for an answer."
    bree.say "Whatever, Sasha..."
    bree.say "So, what do you say?"
    if sasha.love >= 100:

        sasha.say "You know what, [hero.name]..."
        sasha.say "That's a really great idea!"
        "I can feel my mood begin to rise as Sasha warms to the idea."
        "She's nodding and smiling, really seeming to go for it."
        bree.say "You really think so?"
        bree.say "That's great, Sasha!"
        sasha.say "Sure I do."
        sasha.say "This is going to be the best of both worlds."
        sasha.say "Now we both know who we're taking to the party."
        sasha.say "So that's sorted and we can both concentrate on making it perfect."
        sasha.say "Then we can have a great time on the actual night!"
        "Part of me can't believe that Sasha actually said yes."
        "And I'm about to blurt out words to that effect."
        "But then I realise that I should probably try to play it cool."
        "Or at least not look totally needy in front of her."
        bree.say "So it's agreed then?"
        bree.say "And we can get started making this the best party ever?"
        sasha.say "It is, and we totally can!"
        $ game.flags.halloween_girl = "sasha"
    else:


        sasha.say "I don't think so, [hero.name]..."
        sasha.say "At least not this time."
        "I can feel my mood begin to plummet as Sasha rejects the idea."
        "Which makes me begin to shake my head and argue my point."
        bree.say "But why, Sasha?"
        bree.say "Isn't it a neat solution?"
        sasha.say "Nah..."
        sasha.say "It'll just make things too complicated on the night."
        sasha.say "But that doesn't mean we can't get together another time."
        sasha.say "Maybe after the Halloween party, yeah?"
        "I open my mouth to keep on arguing my point."
        "But I can see from the look on Sasha's face that it's too late."
        "She's already made up her mind and there's going to be no changing it."
        "So all I can do is force a smile onto my face and nod."
        "Which Sasha takes as me agreeing to everything she's said."
    return

label sasha_halloween_arrival_female:
    scene bg house
    "I stand staring at the front door for a moment."
    "And then I roll my eyes at my own forgetfulness."
    "Of course, Sasha's not coming in through the front door."
    "My date's already in the house!"
    "I feel like preparing for the party's turned my brain to mush."
    "But the same can't be said for Sasha."
    "As I turn to see her looking at me expectantly."
    sasha.say "Well, [hero.name], I'm waiting."
    sasha.say "What do you think of my costume?"
    "I look Sasha up and down, not for the first time this evening."
    "And then I take a deep breath."
    "All in preparation to tell her exactly what I think."
    menu:
        "Compliment":
            bree.say "I didn't feel comfortable saying this in front of [mike.name]."
            bree.say "But I love it, Sasha."
            bree.say "You look crazily hot!"
            show sasha happy
            "Sasha smiles at this, clearly liking the praise."
            sasha.say "Thanks, [hero.name]!"
            sasha.say "That's just the answer I was looking for."
            sasha.say "I know we're supposed to be the hosts tonight."
            sasha.say "But that doesn't mean we can't find time for each other."
            sasha.say "Time to have fun, you know?"
            "I nod eagerly at this."
            "My head already filling with the possibilities."
            bree.say "You bet, Sasha."
            mike.say "But I'll be staring at you all night."
            mike.say "I just know I won't be able to stop!"
        "Criticize":
            bree.say "Erm..."
            bree.say "I dunno, Sasha."
            bree.say "It looks like you worked really hard on it!"
            "Sasha cocks her head on one side and narrows her eyes."
            "It looks like she doesn't know what to make of my answer."
            sasha.say "Erm..."
            sasha.say "Thanks...I guess!"
            sasha.say "I thought you might have been more into it than that!"
            "I can't help wrinkling up my nose as Sasha says this."
            "Doesn't she appreciate me being honest?"
            "Even if it hurts her feelings just a little?"
            bree.say "It's not really the costume, Sasha."
            bree.say "It's fine."
            sasha.say "Then what in the hell is it?!?"
            bree.say "I just like you better as a rock-chick, Sasha."
            bree.say "You know, the whole goth thing?"
            bree.say "Well...it doesn't work for you!"
            "Sasha rolls her eyes and lets out a sigh."
            sasha.say "At least you're honest, [hero.name]."
            sasha.say "But that's kind of put a dampener on things for me!"
    scene bg black with dissolve
    pause 1
    return

label sasha_halloween_party_female:
    $ game.pass_time(2)
    scene bg livingroom
    show sasha halloween dazed at left5
    show scottie halloween normal at right5
    with dissolve
    scottie.say "Whoa..."
    scottie.say "Sasha - you look SO hot!"
    sasha.say "Ah..."
    sasha.say "Thanks, Scottie, I guess..."
    "I turn around to see Scottie leaning in close to Sasha."
    "She has an awkward smile on her face."
    "And I can see that she's uncomfortable with the attention."
    scottie.say "No, seriously, Sasha."
    scottie.say "That's a real sexy look."
    scottie.say "Makes me sit up and pay attention!"
    "Sasha glances back over her shoulder at me."
    "And I guess she wants me to step in and rescue her."
    menu:
        "Defend Sasha":
            bree.say "That's close enough, Scottie."
            bree.say "Sasha doesn't need you drooling on her costume!"
            scottie.say "Wha...what?"
            scottie.say "I wasn't drooling - was I, Sasha?"
            scottie.say "We were just chatting, that's all."
            "I step forwards, putting myself between Scottie and Sasha."
            "I try not to make it an aggressive move."
            "And all the time I'm aware of how much bigger he is than me."
            "But he still seems to get the message."
            sasha.say "She's right, Scottie."
            sasha.say "I don't need to be able to smell your armpits!"
            "Scottie opens his mouth to say something."
            "But then he nods and turns to walk away."
        "Defend Scottie":
            bree.say "Give the guy a break, Sasha."
            bree.say "He's just trying to pay you a compliment."
            bree.say "I mean, you two used to be an item, right?"
            scottie.say "Yeah..."
            scottie.say "Yeah, that's right!"
            "Sasha takes a step backwards."
            "She shakes her head like she can't understand my actions."
            sasha.say "Y...you're fucking with me, right?"
            sasha.say "You have to be fucking with me!"
            bree.say "Geez, Sasha - lighten up."
            bree.say "This is supposed to be a party."
            bree.say "Don't take it so seriously!"
            "Sasha doesn't say anything."
            "She just shakes her head and turns away from me."
    scene bg black with dissolve
    pause 1
    return

label sasha_halloween_dance_female:
    $ game.pass_time(2)
    scene bg livingroom
    show sasha halloween
    with dissolve
    scottie.say "Come on, Sasha..."
    scottie.say "One dance - for old time's sake?"
    scottie.say "Wadda ya say?"
    "Neither of us saw Scottie walk up to where Sasha I are standing."
    "So the sound of his voice makes us both jump a little."
    "But it's not like he even seems to notice."
    "Sasha is already backing off from him, trying to put me between them."
    sasha.say "No, Scottie."
    sasha.say "I don't feel like dancing with you."
    sasha.say "I want to hang out with [hero.name] tonight!"
    "Sasha looks at me for support."
    "But at the same time, Scottie does the same."
    "And he's looming over me, starting to look a little pissed!"
    menu:
        "Side with Sasha":
            bree.say "Sasha said no, Scottie."
            bree.say "That's your answer, right there."
            "Scottie opens his mouth to protest."
            "But I take a step forward, shaking my head."
            "Scottie seems surprised to be confronted by another girl."
            "But despite that, he apparently gets the message, and backs off."
            scottie.say "Okay, okay!"
            scottie.say "I don't need to be told twice!"
            "With that, he turns on his heel and walks off."
            "Which prompts Sasha to turn to me, a look of relief on her face."
            sasha.say "Thanks for that, [hero.name]..."
            sasha.say "I owe you one!"
            bree.say "How about you pay me back with a dance?"
            "Sasha gives me a smile and a nod."
            "And as soon as a song she likes comes on, we hit the dance-floor."
            "Sasha shows none of the reluctance to me that she had for Scottie."
            "She moves in time to the music, never more than an inch from me!"
            "And I move in time with Sasha, all of my attention focused on her."
            "She really wasn't kidding when she said she wanted to be with me!"
        "Side with Scottie":
            bree.say "Don't be so mean, Sasha."
            bree.say "We've got all night to talk."
            bree.say "And Scottie did say he only wanted one dance."
            "Sasha's eyes go wide at this."
            "She clearly wasn't expecting that answer."
            sasha.say "I...I don't..."
            scottie.say "You see, Sasha?"
            scottie.say "I told you it was no biggie!"
            "I watch as Scottie bundles her onto the makeshift dance-floor."
            "And it's only then that I begin to wonder of I made a mistake."
            "Sasha keeps on glancing at me the whole time."
            "And I can tell she has a pleading look in her eyes."
            "She tries as best she can to keep her distance."
            "But Scottie seems determined to invade her personal space."
            "And when they're done, she storms away from him."
            "But she doesn't come back over to stand with me either."
            "She seems to be pretty angry with Scottie after all that."
            "But I get the feeling she's going to be more irate with me!"
    scene bg black with dissolve
    pause 1
    return


label sasha_halloween_sex_female:
    scene bg livingroom
    show sasha halloween
    with fade
    "It's getting pretty late by now and the party seems to be winding down too."
    "Everyone that's still here is either drunk, tired or both."
    "So the need for Sasha and I to play host is pretty much over for the night."
    "Which is great, because I feel like I spent the last of my energy already."
    "And all of it went on making sure that our guests had the best time possible."
    bree.say "Phew, Sasha..."
    bree.say "I'm totally exhausted!"
    "I was expecting Sasha to say the same."
    show sasha joke
    "But then I see she has a look of mischief in her eye."
    sasha.say "Oh no, [hero.name] - you're not off duty yet."
    sasha.say "There's one more person you have to entertain."
    bree.say "What are you talking about, Sasha?"
    mike.say "Looks to me like everyone's worn out too!"
    sasha.say "Not everyone, [hero.name]..."
    show sasha flirt
    sasha.say "I've still got a little life left in me!"
    "With that, Sasha takes hold of my wrist."
    "She drags me after her without asking permission."

    bree.say "Okay, Sasha..."
    bree.say "I think I have enough energy left for that!"
    "Sasha gives me a wicked smile as she opens a door and slips inside."
    scene bg bedroom1
    show sasha halloween
    with fade
    "But it's only when I follow her through that I see why she's grinning."
    bree.say "W...wait a minute, Sasha..."
    bree.say "This is [mike.name]'s room!"
    show sasha surprised
    "At this, Sasha claps her hands on her cheeks in mock horror."
    sasha.say "Oh no, how did we end up in here?!?"
    show sasha joke
    sasha.say "Come on, [hero.name], lighten up!"
    sasha.say "It's Halloween, so let's have fun."
    show sasha flirt
    sasha.say "Let's mess around on [mike.name]'s bed!"
    bree.say "B...but why?!?"
    show sasha joke at center, zoomAt (1.5, (640, 1040))
    "By way of answer, Sasha presses herself against me."
    "She's not shy about putting her hands in sensitive places either."
    "And I can already feel myself getting flustered at her efforts."
    sasha.say "Because I want to live dangerously, [hero.name]."
    show sasha flirt
    sasha.say "Come on, come on - I'm REALLY horny right now!"
    "I hardly notice that Sasha's already started stripping."
    "By now she's naked to the waist and starting to undress me too."
    "Part of my mind's still trying to tell me this is a bad idea."
    "But my hands are ignoring it, tugging at what remains of Sasha's costume."
    scene bg black
    show sasha fingering halloween bedroom1 with fade
    "We're standing in front of the full-length mirror in [mike.name]'s room."
    "And I'm still not sure this is a good idea."
    show sasha fingering sasha_arm
    "Or at least I am until I feel Sasha's hand on my pussy."
    "From then I seem to be on autopilot, one thing alone on my mind."
    sasha.say "Oh yeah..."
    sasha.say "Please..."
    sasha.say "Please play with me!"
    "Like I was ever going to do something else!"
    "Sasha's already setting a pretty good example for me to follow."
    "And it doesn't take long for me to slide a hand between her legs too."
    "We both moan and gasp almost as one, beginning to stoke each other."
    "Sasha leans back against me the whole time, making me support her weight."
    "I only spend a few moments looking down over her shoulder."
    "Because after that, I remember that we're standing in front of the mirror."
    "As soon as I look up, I'm treated to a full-frontal view of Sasha and I."
    "There are hands wandering everywhere, limbs moving slowly and sensually."
    "I can't help swallowing and letting out a gasp of amazement."
    sasha.say "Mmm..."
    sasha.say "We look pretty good together..."
    sasha.say "Don't we?"
    "I can't seem to find the words to express myself."
    "And my mind is totally blank as Sasha asks the question."
    "The best I can manage is to nod dumbly, eyes still wide."
    "But what does happen is that my hand begins to move faster."
    "My fingers sliding around Sasha's pussy like never before."
    "Soon enough they're actually starting to sink into the too."
    "And the effect this has on her is both instant and visible."
    show sasha fingering sashaahegao
    "Sasha leans back into me like never before."
    "Her head is almost resting on my shoulder by now."
    "And she's practically helpless in my arms."
    "All that it seems she can do is vaguely nod her head."
    "Letting me know that she approves of what I'm doing."
    "That and making it obvious that she wants more of the same."
    show sasha fingering breeahegao
    "Finally I see movement start to spread through Sasha's body."
    "And she manages to find the will to speak."
    sasha.say "Oh fuck..."
    sasha.say "That's so fucking good..."
    sasha.say "You're gonna make me cum!"
    with vpunch
    "She's not lying either, as I feel her pussy clenching around my fingers."
    bree.say "Oh...oh god..."
    show sasha fingering squirt with vpunch
    bree.say "[mike.name!u]!"
    "Sasha and I both lose it a moment later."
    show sasha fingering -squirt
    "But the look on her face is less than pleased as we do so."
    sasha.say "Y...you bitch!"
    sasha.say "You...said..."
    sasha.say "You said someone else's name!"
    bree.say "N...no, Sasha..."
    bree.say "I mean...[mike.name]'s here!"
    scene bg bedroom1
    show sasha halloween surprised at flip, center, zoomAt(1.5, (540, 1040))
    show mike halloween surprised at top_mostright
    with fade
    "We both look round to see [mike.name] standing in the open doorway."
    "His mouth hanging open and his eyes as wide as saucers."
    mike.say "Whoa!"
    mike.say "You did it - in my room?!?"
    bree.say "Ah...I guess so, [mike.name]!"
    show sasha annoyed
    sasha.say "Would you believe we got lost on the way to my room?"
    mike.say "Well, I certainly know where your room is, [hero.name]."
    mike.say "And that's where I'll be sleeping until you clean this place up!"
    hide mike with moveoutright
    show sasha surprised at center, zoomAt(1.5, (640, 1040)) with ease
    "And with that, [mike.name] turns on his heel and storms off."
    show sasha happy at startle
    "Sasha bursts out laughing, and for a moment I feel like telling her off."
    "But then the urge passes, and I find myself seeing the funny side."
    "[mike.name]'ll get over it in time."
    "And it was worth it to see the look on his face."
    "Well, that and the chance to fool around with Sasha too!"
    $ sasha.sexperience += 1
    $ game.pass_time(1)
    return

label sasha_after_dance_success_with_female:
    show sasha shy
    "I know that Sasha's watching me as I dance, and that pushes me to try harder than normal."
    "Because I obviously want to impress her with the brilliance of my moves, you know?"
    "And when I get a good look at her face, I'm pretty sure she's smiling!"
    "So as soon as I'm done dancing, I hurry over there."
    bree.say "Sasha..."
    bree.say "Were you..."
    bree.say "Were you watching me dance?"
    "Now that I'm up close, I can see that Sasha really is smiling."
    "And I can also see that it's a knowing, flirty smile too!"
    show sasha joke
    sasha.say "I might have been."
    sasha.say "Who wants to know?"
    show sasha embarrassed
    "Normally I'd be giving as good as I'm getting."
    "But right now I'm too interested in getting a confession out of Sasha for that."
    bree.say "Don't be like that, Sasha!"
    bree.say "You were watching me dance..."
    bree.say "I saw you!"
    show sasha happy
    "Sasha lets out a sigh of defeat."
    "And then she nods her head."
    show sasha shout
    sasha.say "Urgh..."
    sasha.say "Okay, [hero.name], okay..."
    sasha.say "I was watching you."
    sasha.say "And for the record, you're a pretty good dancer."
    show sasha shy
    "It's only a small admission."
    "But coming from Sasha, it feels like a major victory."
    show sasha normal
    return

label sasha_after_dance_failure_with_female:
    show sasha sad
    "I know that Sasha's watching me as I dance, and that pushes me to try harder than normal."
    "Because I obviously want to impress her with the brilliance of my moves, you know?"
    "But when I get a good look at her face, I could swear that she's actually wincing!"
    "So as soon as I'm done dancing, I hurry over there."
    bree.say "Sasha, are you okay?"
    bree.say "You looked like you were in pain or something!"
    show sasha annoyed
    "Sasha doesn't seem to look as pained now."
    "In fact she looks more like she's feeling awkward."
    show sasha shout
    sasha.say "Nah, [hero.name]..."
    sasha.say "It was nothing."
    show sasha normal
    "I note that saying it was nothing isn't the same as saying it didn't happen."
    "So I decide to keep on pressing Sasha, trying to get to the bottom of it."
    bree.say "Come on, Sasha..."
    bree.say "Tell me what the problem is, yeah?"
    bree.say "If you don't, I'll just keep on bugging you!"
    show sasha whining
    sasha.say "Please, [hero.name]..."
    sasha.say "I'd rather not say."
    show sasha sad
    bree.say "No way, I'm not giving up!"
    "Sasha sighs and shakes her head."
    show sasha whining
    sasha.say "Urgh..."
    sasha.say "Okay, [hero.name] - I was cringing at your dancing."
    show sasha sad
    "I stare at Sasha for a moment, not able to believe what I'm hearing."
    bree.say "Are you serious?!?"
    show sasha whining
    sasha.say "Ah, yeah, [hero.name]..."
    sasha.say "I told you that I'd rather not say!"
    show sasha normal
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
