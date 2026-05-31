label aletta_date_intro_valentine_male:
    mike.say "Happy Valentine's day, Aletta!"
    mike.say "I'm really looking forward to tonight!"
    "Aletta treats me to an approving smile."
    "And it's enough to make my heart beat faster than before."
    aletta.say "Thank you, [hero.name]."
    aletta.say "I'm looking forward to it too..."
    return

label aletta_date_intro_halloween_male:
    mike.say "You ready for our date, Aletta?"
    mike.say "Feeling extra spooky tonight?"
    "Aletta snorts at this, shaking her head."
    aletta.say "Since when have I been spooky, [hero.name]?"
    "I shrug, already getting worried that I said the wrong thing."
    mike.say "I dunno, Aletta - you do look good in black."
    mike.say "Like those leathers you wear when you're riding your bike."
    mike.say "In those you could give any goth girl a run for her money!"
    "Aletta seems to perk up at this, her mood getting better."
    aletta.say "Hmm...I have been told that I wear them well!"
    return

label aletta_date_intro_christmas_male:
    mike.say "Happy Christmas, Aletta!"
    mike.say "And I gotta say, I'm feeling festive today."
    mike.say "I hope there's some mistletoe around here!"
    "Aletta raises an eyebrow at this, regarding me with amusement."
    aletta.say "Seems to me that someone's being a tad presumptuous!"
    aletta.say "If you want a festive kiss, then you're going to have to earn it."
    return

label aletta_date_intro_birthday_male:
    mike.say "Happy birthday, Aletta!"
    mike.say "And since it is your birthday..."
    mike.say "I'm going to make this date extra special!"
    aletta.say "Ha, ha, ha..."
    aletta.say "Oh, [hero.name] - so sweet of you to remember."
    aletta.say "I never thought you were so organised!"
    aletta.say "Because you certainly aren't at work..."
    return

label aletta_date_intro_mc_birthday_male:
    mike.say "Hey, Aletta..."
    mike.say "Are you ready for our date?"
    aletta.say "Hmm..."
    aletta.say "Aren't you forgetting something?"
    mike.say "Erm...I don't think so..."
    aletta.say "Happy birthday, [hero.name]!"
    mike.say "Oh...oh yeah!"
    mike.say "You remembered?"
    aletta.say "Oh, [hero.name] - of course I did!"
    return

label aletta_date_eat_a_burger:
    "When her burger arrives, Aletta looks less than impressed."
    "She wraps it in a napkin, as if disgusted at the thought of touching it."
    "And then proceeds to nibble at it while looking daggers in my direction the whole time."
    $ game.active_date.score -= 5
    return

label aletta_date_buy_drink:
    if aletta.is_visibly_pregnant:
        show aletta angry
        $ aletta.love -= 10
        aletta.say "I'm going to pretend you didn't say that, [hero.name]."
        aletta.say "For your sake and the sake of our unborn child."
        aletta.say "But I won't forget a second time!"
        $ hero.cancel_activity()
        hide aletta
    else:
        "Aletta accepts her drink with a genuine smile."
        "She takes a sip and places it down before her."
        "Seems that it meets with her approval."
    return

label aletta_date_play_darts:
    "Aletta holds her darts a little awkwardly and throws them without much care."
    "It's almost as though she's trying to show willing."
    "But in reality she couldn't care less about our game."
    return

label aletta_date_pub_play_pool:
    "Almost as soon as she has the cue in her hand, Aletta becomes interested in the course of the game."
    "She's not a bad pool player, inexperienced for sure, but she learns quickly from her mistakes."
    "While I, on the other hand, make more as I get distracted from watching her as she leans over the table."
    $ game.active_date.score += 5
    return

label aletta_date_buy_a_round:
    if aletta.is_visibly_pregnant:
        show aletta angry
        $ aletta.love -= 10
        aletta.say "I'm going to pretend you didn't say that, [hero.name]."
        aletta.say "For your sake and the sake of our unborn child."
        aletta.say "But I won't forget a second time!"
        $ hero.cancel_activity()
    elif (hero.charm >= 60 - aletta.love and aletta.flags.drinks < 2):
        show drink aletta
        "When I announce that I'm going to the bar and this round's on me, Aletta makes no big fuss about the matter."
        "She just shrugs and nods, as if she has no problem with it, but doesn't expect it all the same."
        "I guess that just comes from being a hard-nosed woman in a man's world."
        $ game.active_date.score += 5
        if "rebel" in aletta.traits:
            $ game.active_date.score += 5
        $ aletta.set_flag("drinks", 1, "day", mod="+")
        hide drink
    else:
        "I want to pay a round of beers to the whole pub."
        "But Aletta doesn't seem to want to drink, so I refrain from doing so."
        $ hero.cancel_activity()
    return

label aletta_dance_with:
    "As soon as we're on the dance-floor, Aletta's face seems to light up."
    "She waltzes (if you'll pardon the pun) through the entire thing whilst beaming with happiness."
    "I don't know if it's being up there with me, or just the chance to show off in public."
    "But either way, she wows me with her moves."
    return

label aletta_date_play_arcade_intro_male:
    aletta.say "Urgh..."
    aletta.say "I can't believe you talked me into this, [hero.name]!"
    "I tear my attention away from the alluring lights and sounds of the arcade around me."
    "It takes me some effort, as I can see so many games that I'm just itching to play."
    "But somehow I manage to pay attention to Aletta as she's venting her frustrations."
    mike.say "Huh..."
    mike.say "What do you mean, Aletta?"
    mike.say "How can you not have fun in a place like this?!?"
    "Aletta rolls her eyes at me and makes a huffing sound."
    "She turns almost a complete circle as she looks around."
    aletta.say "I already told you, [hero.name] - I don't play games!"
    aletta.say "And all of these ones are of no interest to me at all."
    aletta.say "Alien invaders, zombies, superheroes - it's all so childish."
    "I cast my gaze around, following Aletta's as she takes the place in."
    "It can't he as hopeless as she's making it sound, surely?"
    "There must be something that she likes, something that she's into."
    "A moment later, my eyes settle on a possible candidate."
    mike.say "You like to go to the shooting range, right, Aletta?"
    mike.say "You know - practice your aim and all that?"
    "Aletta frowns at this, suspicion written all over her face."
    "She crosses her arms over her chest and raises an eyebrow too."
    aletta.say "Of course I do, [hero.name]."
    aletta.say "You know that I do."
    aletta.say "And we could have gone there instead of here!"
    mike.say "Why not do both, Aletta?"
    aletta.say "Huh?"
    aletta.say "What are you talking about?"
    "I lead Aletta over to a particular game."
    "It's a shooter, with a pair of light-guns attached."
    "And I pick one up, placing it into Aletta's hand."
    mike.say "There you go - 'Buck Hunt'."
    mike.say "This one's a classic."
    mike.say "Trust me, you'll love it!"
    "Aletta huffs and puffs a little longer."
    "But in the end she lets me pump coins into the machine, and we play a game."
    return

label aletta_date_play_arcade_win_male:
    "I can see from the way that Aletta holds her gun she means business."
    "But I also know that there's a difference between these and the real thing."
    "And it doesn't take long for Aletta's lack of experience to show."
    aletta.say "Argh..."
    aletta.say "There's no recoil on this thing!"
    mike.say "Of course not, Aletta."
    mike.say "You're not firing real bullets!"
    aletta.say "But I was factoring that into my aim!"
    aletta.say "And...dammit..."
    aletta.say "How do I reload this thing!"
    mike.say "Just shoot off-screen!"
    "By the time we're finished, my score is more than double Aletta's."
    "She slams her gun back into the holster on the machine, taking it badly."
    aletta.say "You see, [hero.name]?!?"
    aletta.say "I told you this was a lousy idea!"
    return

label aletta_date_play_arcade_lose_male:
    "I can see from the way that Aletta holds her gun she means business."
    "And that serves to put me off even before we've started shooting."
    "Aletta might be lacking in experience, but she's a crack shot!"
    aletta.say "Got him!"
    aletta.say "And another one!"
    aletta.say "This is FAR too easy!"
    mike.say "Whoa..."
    mike.say "Hang on, Aletta!"
    mike.say "Leave some of them for me!"
    aletta.say "Wait a minute..."
    aletta.say "How do I reload this thing?"
    mike.say "You..."
    mike.say "You just shoot off-screen!"
    aletta.say "Oh, I see!"
    "By the time we're finished, Aletta's score is more than double mine."
    "I slam the gun back into the holster on the machine, taking it badly."
    aletta.say "You see, [hero.name]?!?"
    aletta.say "I told you this was a lousy idea."
    aletta.say "Now it's making you miserable too!"
    return

label aletta_dick_reactions:
    if not aletta.flags.seendick:
        $ aletta.flags.seendick = 1
        if hero.has_skill("hung"):
            show dick reactions aletta tasty
            aletta.say "Hmm..."
            aletta.say "Now that's certainly not a disappointment!"
            mike.say "Like what you see, Aletta?"
            aletta.say "It's certainly more impressive than your CV!"
            $ aletta.sub += 10
        elif hero.has_skill("smalldick"):
            show dick reactions aletta mock
            aletta.say "Ah well..."
            mike.say "You...you sound disappointed, Aletta!"
            aletta.say "It's kind of like lying on your CV."
            aletta.say "And then getting the job anyway!"
            $ aletta.sub -= 10
        hide dick reactions
    return

label aletta_halloween_invitation:
    show aletta
    "I can't think of anyone I'd rather take to the Halloween party than Aletta."
    "But how do I go about asking her to be my date for the night?"
    "She's such a no-nonsense, hard-nosed kind of girl."
    "It's kind of hard to imagine her letting her hair down with my room-mates."
    "I guess that I'll just have to come out and ask her."
    "After all, the worst that can happen is her saying no, right?"
    "Best to make it all sound casual too."
    "Like I ask girls to this kind of thing all the time."
    mike.say "Hey, Aletta..."
    mike.say "Have you made any plans for Halloween yet?"
    "Aletta stares at me over her glasses, one eyebrow raised."
    "It looks like the question itself is what interests her."
    "Far more than the prospect of finding out what I have in mind."
    show aletta talkative
    aletta.say "Well, [hero.name], now that you ask..."
    aletta.say "I was planning to trick or treat around my neighbourhood."
    show aletta normal
    mike.say "Huh?"
    mike.say "Really?!?"
    show aletta embarrassed
    "Aletta rolls her eyes at me."
    show aletta talkative
    aletta.say "Of course not, [hero.name]!"
    aletta.say "I'm a grown woman."
    aletta.say "Why would I have plans for Halloween of all things?"
    show aletta normal
    "Well, that answer made me feel like a fool."
    "But there's no turning back now..."
    mike.say "Hah...well..."
    mike.say "We were...actually it was more my room-mates idea..."
    mike.say "We're having a Halloween party - just for fun."
    mike.say "And I wondered if you wanted to come along?"
    mike.say "Maybe...as my...you know...my date?"
    show aletta normal
    if aletta.love >= 100:
        "Aletta smiles, and for a moment I think she's just indulging me."
        "But then she nods her head and chuckles."
        show aletta talkative
        aletta.say "You know what, [hero.name]..."
        $ aletta.love += 1
        aletta.say "I think I'll take you up on that."
        show aletta normal
        "I shake my head in amazement."
        "Did she really say what I think she said?"
        mike.say "Y...you will?"
        mike.say "That's great, Aletta!"
        show aletta talkative
        aletta.say "Well, I have been working extra hard lately."
        aletta.say "I could use the chance to do something fun."
        aletta.say "Both as a reward to myself and a chance to relax."
        show aletta normal
        mike.say "Trust me, Aletta - you won't regret this."
        mike.say "We're going to have music and some fun games."
        mike.say "But you don't have to play them if you don't want to!"
        mike.say "Oh, and I almost forgot - it's a costume party too."
        show aletta dreamy
        "Aletta nods, beginning to look thoughtful."
        show aletta talkative
        aletta.say "Is it really?"
        aletta.say "Well, I'll have to get thinking about my costume."
        show aletta pain
        aletta.say "Won't I?"
        show aletta normal
        "All I can do is nod in turn."
        "As my head's already filling with possibilities."
        "Just what kind of costume could Aletta have in mind?"
        $ game.flags.halloween_girl = "aletta"
    else:
        "The smile that Aletta gives me is genuine, I'm sure of it."
        "But it's more indulgent and amused than anything else."
        show aletta whining
        aletta.say "Well, it's kind of you to ask, [hero.name] - but I can't."
        $ aletta.sub -= 1
        aletta.say "I have grown-up things to do that night."
        show aletta pain
        aletta.say "But don't let that stop you having fun with your friends."
        show aletta sadsmile
        "I can already feel my cheeks starting to burn."
        "But all I can do is stand there and take it."
        "Just stand there and let Aletta talk to me like a kid."
        "What was I thinking - inviting her to a dumb, immature party?"
        mike.say "Aw..."
        mike.say "That's a shame, Aletta."
        mike.say "I'm sure you'd have had a great time."
        show aletta talkative
        aletta.say "Oh, I don't need a party to have a great time, [hero.name]."
        aletta.say "There are far more fun things that adults can get up to."
        show aletta pain
        aletta.say "It's just a shame that you can't enjoy them with me!"
        show aletta normal
        "I swallow audibly and nod at this."
        "And all the time I'm wondering if the party is the best idea after all."
        "Maybe I could take a rain-check and do something with Aletta instead?"
    return

label aletta_halloween_arrival:
    scene bg house
    "Opening the door, I guess I should have been more cautious."
    "Especially after the incidents with Jack's sword and Scottie's trident."
    "But this time it's not a weapon that stops me in my tracks."
    "Though it's still a pair of guns."
    "But I'm not sure exactly which pair is more impressive!"
    show aletta halloween talkative
    aletta.say "Hello, [hero.name]."
    aletta.say "I trust that I'm on time?"
    show aletta normal
    "All I can do is nod in response, having lost the power of speech."
    "Aletta's standing there with a pair of pistols in her hands."
    "And her entire body is swathed in a black, skin-tight catsuit."
    mike.say "B...B...Bayoletta..."
    show aletta talkative
    aletta.say "That's right, I came as Bayoletta."
    aletta.say "I don't have time for videogames myself."
    aletta.say "But I did some research."
    aletta.say "And the hair seemed to speak to me."
    show aletta normal
    "Aletta stares at me, clearly waiting for a response."
    show aletta talkative
    aletta.say "Well, [hero.name]?"
    show aletta pain
    aletta.say "What do you think?"
    show aletta normal
    menu:
        "Compliment":
            mike.say "It's..."
            mike.say "It's amazing, Aletta!"
            mike.say "Absolutely amazing!"
            show aletta happy
            $ aletta.love += 1
            "I can see the effect my enthusiasm has on Aletta instantly."
            "She looked confident beforehand, like she could boss the whole room."
            "But now she looks like she's going to start purring like a cat."
            show aletta talkative
            aletta.say "Good, very good."
            aletta.say "That was the answer I wanted to hear!"
            show aletta normal
            "I nod silently, utterly entranced by the sight of Aletta's body."
            "And then I catch myself reaching out unconsciously to touch her."
            show aletta talkative
            aletta.say "Uh-uh, [hero.name]."
            show aletta pain
            aletta.say "There'll be plenty of time for that later."
            aletta.say "So long as you earn it!"
            show aletta wink
            "Aletta winks at me."
            "As if there's any need to explain just what she means by that!"
            "But all I can do is nod like an obedient dog."
            "That and take her hand as she strides into the house like a queen."
        "Criticize":
            mike.say "It's..."
            mike.say "It's too much, Aletta!"
            show aletta annoyed
            $ aletta.love -= 4
            "I can instantly see the effect my words have on Aletta."
            show aletta sad
            "The confidence seems to drain out of her face."
            "And her stance becomes defensive."
            "It's like she's trying to cover herself up."
            show aletta whining
            aletta.say "Wha...what do you mean?"
            aletta.say "I thought this was a party, [hero.name]?"
            aletta.say "A chance to let my hair down!"
            show aletta sadsmile
            mike.say "I'm sorry, Aletta."
            mike.say "But this just doesn't seem like the real you."
            mike.say "You're normally so dignified and reserved in the office."
            mike.say "I guess I thought you'd be the same out of it too."
            show aletta whining
            aletta.say "I...I don't know what to say!"
            show aletta sad
            mike.say "Urgh..."
            mike.say "Just come in and try to keep covered up, okay?"
            "God's sake - this is going to be awkward!"
    scene bg black with dissolve
    pause 1
    return

label aletta_halloween_party:
    $ game.pass_time(2)
    scene bg livingroom
    show aletta halloween flirt at left
    show bree halloween annoyed at right
    with fade
    aletta.say "Excuse me?"
    show aletta normal
    show fx question at right
    show bree surprised
    bree.say "Huh?"
    show bree stuned
    "I turn around to see Aletta confronting [bree.name]."
    show aletta angry
    aletta.say "Did I just hear you tutting at me?"
    show aletta upset
    show bree hesitating
    bree.say "No...I...well..."
    bree.say "I suppose so."
    show bree sadsmile
    show aletta angry
    aletta.say "And why, pray tell, was that?"
    show aletta upset
    "Aletta raises an eyebrow as she speaks."
    "And I know from experience that [bree.name]'s not getting away from this."
    show bree vangry
    bree.say "It's...it's just the guns, that's all."
    show bree angry
    aletta.say "Oh please - these are just toys!"
    show bree vangry
    bree.say "Well...my Dad's a gun-nut."
    bree.say "And I just don't like them!"
    show bree angry
    show aletta annoyed
    aletta.say "Hmm..."
    show aletta angry
    aletta.say "Doesn't sound to me like your father's the nut here..."
    show aletta annoyed
    menu:
        "Defend Aletta":
            mike.say "Aletta's right, [bree.name]."
            mike.say "You should try to lighten up."
            show bree surprised
            show aletta normal
            $ bree.love -= 2
            $ aletta.love += 2
            "[bree.name] looks surprised at my butting into the conversation."
            "And more than a little annoyed at my siding against her too."
            "But Aletta nods and smiles as I come to her aid."
            "I can practically feel the approval radiating from her."
            show bree vangry
            bree.say "Hey, [hero.name]."
            bree.say "Don't gang up on me!"
            bree.say "I can't help how I feel."
            show bree angry
            show aletta angry
            aletta.say "Maybe you should seek professional help?"
            show aletta upset
            show bree sad
            "[bree.name]'s mouth drops open at the suggestion."
            "And it looks like she's waiting for me to come to her aid."
            hide bree
            show aletta normal at center
            with easeoutright
            "But when that doesn't happen, she harumphs and storms off."
            show aletta flirt
            aletta.say "Really - what a silly little girl!"
        "Defend [bree.name]":
            mike.say "Don't you think that's a bit harsh, Aletta?"
            mike.say "[bree.name] can't help the way she feels."
            show bree normal
            $ aletta.love -= 2
            $ bree.love += 2
            "Aletta looks surprised at my butting into the conversation."
            "And more than a little annoyed at my siding against her too."
            "But [bree.name] looks relieved to have me come to her aid."
            show aletta angry
            aletta.say "Then maybe she should be seeking professional help?"
            show aletta flirt
            aletta.say "After all - I'm not the one that has the problem here."
            show bree vangry
            bree.say "No, you're the one that's making one!"
            show bree angry
            show aletta annoyed
            "Aletta's mouth drops open at [bree.name]'s statement."
            "I honestly don't think she expected the other girl to show her teeth."
            "Aletta looks at me, waiting for me to come to her aid."
            hide aletta
            show bree happy at center
            with easeoutleft
            "But when that doesn't happen, she harumphs and turns away."
            "[bree.name] turns and walks away too."
            hide bree with easeoutright
            "But not before she gives me a grateful smile."
            "One that I'm sure Aletta sees too."
    scene bg black with dissolve
    pause 1
    return

label aletta_halloween_dance:
    $ game.pass_time(2)
    scene bg livingroom
    show aletta halloween
    with dissolve
    "Aletta and I have been standing around chatting for a while now."
    "But the whole time, I've been tapping my foot to the music that's playing."
    "And I can't help glancing over to the makeshift dance-floor too."
    show aletta talkative
    aletta.say "Am I boring you, [hero.name]?"
    aletta.say "Because you seem a little distracted!"
    show aletta normal
    mike.say "Huh?"
    mike.say "Oh...sorry, Aletta."
    mike.say "I was wondering if you wanted to dance?"
    show aletta flirt
    "Aletta raises one eyebrow as she regards me."
    "I can see that she's more amused than intrigued by my offer."
    show aletta talkative
    aletta.say "Well, it looks like you want to dance."
    aletta.say "That's for sure!"
    show aletta normal
    menu:
        "Press on":
            "Aletta might not have said yes."
            "But she didn't say no either."
            "And that's all the permission I need."
            "Taking her by the hand, I make for the dance-floor."
            "There's only the slightest resistance from Aletta."
            hide aletta
            $ aletta.sub += 1
            "And then she seems to give in, following along after me."
            "It's when we're actually out there that she seems to relax."
            "Aletta's normally haughty demeanour changes subtly."
            "And it's as if she's resigned to me being the one in charge."
            show dance aletta halloween with fade
            "What follows is a pretty memorable slow-dance."
            "Neither of us feels the need to speak the entire time."
            "Instead I get to enjoy the sensation of being close to Aletta."
            "Her almost statuesque body close to mine."
            "And I swear that I can hear the sound of her heart beating."
            "Even over the music and the chatter of voices."
            "It's like we're making a connection on a whole other level."
        "Back down":
            "I take it that Aletta's making her feelings plain."
            "If she wanted to dance, she would have said so."
            "After all, she's not the kind of girl to beat around the bush."
            "So I decide to let the matter drop."
            mike.say "Only if you want to, Aletta."
            mike.say "I'm fine just the way we are."
            "Aletta narrows her eyes at this."
            "And for a moment I think she might actually say yes."
            show aletta annoyed
            $ aletta.sub -= 1
            "But then she blows air out of her nose and shakes her head."
            aletta.say "Hmm..."
            show aletta whining
            aletta.say "That's the matter settled then."
            show aletta sad
            "And we both remain standing right where we are."
    scene bg black with dissolve
    pause 1
    return

label aletta_halloween_sex:
    scene bg livingroom with fade
    "It's getting pretty late by now, and the party's beginning to wind down."
    "Everyone's either tired, drunk or both and seems to want to chill out."
    "And I was feeling the same, looking forward to not being the host much longer."
    "That is until I feel the sensation of something poking me in the small of the back."
    aletta.say "Hands up, [hero.name]!"
    mike.say "Wha..."
    mike.say "Aletta?"
    mike.say "Is that you?"
    show aletta halloween flirt with dissolve
    "It's Aletta alright."
    "And she's jabbing me in the back with her costume pistols!"
    aletta.say "No time for talk."
    aletta.say "Get moving!"
    "I hop to it, doing as Aletta tells me to."
    "In pretty short order, she marches me to the door of my bedroom."
    aletta.say "Inside - now!"
    scene bg bedroom1
    show aletta halloween flirt
    with fade
    "Aletta hustles me into the room and closes the door behind us."
    "Still brandishing her fake pistols, she nods towards the bed."
    aletta.say "Now strip!"
    "I can't help smiling at the situation I find myself in."
    "If Aletta wants to indulge in a little bit of roleplay, that's fine."
    "So long as it means I get my hands on her in that amazing outfit!"
    "I do as I'm told, hurrying to take off my clothes."
    "I try as best I can to play the part of someone being held at gunpoint."
    "But in that situation, I doubt most guys would have an erection quite as big as mine."
    "Aletta can't help notice the effect she's having on me."
    "And I see a smile spread across her face."
    "One that I'm sure is more to do with anticipation than amusement."
    "Or at least I hope that it is!"
    aletta.say "Very good."
    aletta.say "Now lie on the bed."
    aletta.say "And keep your hands where I can see them!"
    "I nod as I hurry over to the bed and do as she says."
    "And I can't help smiling too."
    "From here I have a perfect view of Aletta."
    show aletta doggy halloween glasses pleasure with fade
    "She's standing defiantly at the foot of the bed."
    "And her costume shows off every inch of her body."
    "Aletta doesn't issue any more orders."
    "Instead she tosses her pistols aside and puts her hands to better use."
    show aletta doggy -halloween hairdown
    "It doesn't take her long to strip off the tight spandex she's wearing."
    "But all the same, it's a memory that will stay with me for a very long time!"
    "Once she's completely naked, Aletta climbs onto the end of my bed."
    show aletta doggy mike
    "She crawls slowly towards me on all fours, taking her time."
    "Which means that I get to watch her body move, her heavy breasts sway."
    show aletta doggy hand
    "Without asking permission, I take hold of her ass."
    "And then she begins to squeeze my cock, stroking the shaft."
    "There's no need for either of us to speak at this point."
    "We're beyond the role playing that got us here."
    "There's only one thing that we want now."
    "Aletta pushes her ass backwards, pressing the head of my cock against her lips."
    show aletta doggy vaginal normal
    "And then she pushes herself onto me, using her weight to drive it home."
    "I gasp at the sensation, every slow second passing like an age."
    "By the time I'm as deep into Aletta as I can go, I realise I'm holding my breath."
    show aletta doggy pleasure
    "I only begin to feel that I can breathe again as she starts to ride my cock."
    "Aletta goes slowly at first, but soon builds up speed."
    "And I feel like all I can do is sit back and let her have her way."
    "The experience is amazing, watching her use me to pleasure herself."
    "The sensations that she stirs in me building with each second that passes."
    "Aletta looks back at me over her shoulder."
    "I don't know if she does this because she wants me to play with her breasts."
    "But it's not a chance that I'm going to let pass me by."
    "As soon as I begin to massage those huge, fleshy orbs, Aletta moans with pleasure."
    "She doesn't say a word, just nods to let me know what she wants more."
    "I oblige, squeezing her stiff nipples between my fingers and thumbs."
    show aletta doggy squirt ahegao with hpunch
    "Aletta throws her head back, and I can feel that she's about to cum."
    show aletta doggy creampie with hpunch
    "Which makes me lost it too, shooting my load into her."
    with hpunch
    "Aletta collapses onto the bed before me."
    "And we lie there as she rides out the last moment of her climax."
    "Her pussy twitching around my cock the whole time."
    $ aletta.sexperience += 1
    $ game.pass_time(1)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
