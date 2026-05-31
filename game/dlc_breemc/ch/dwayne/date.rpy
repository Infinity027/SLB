label dwayne_after_dance_success_with_female:
    show dwayne normal
    "Once I'm done dancing, I'm feeling pretty pleased with myself."
    "That is until I look around and see Dwayne watching me closely."
    "At first I have no idea what his intentions are, and I'm worried he's unimpressed."
    "Then I see him begin to clap, slowly and without making a scene."
    "But clapping nonetheless."
    bree.say "Ah..."
    bree.say "You didn't happen to watch me dancing just now..."
    bree.say "Did you, Dwayne?"
    "Dwayne's expression doesn't change in the slightest."
    show dwayne therock
    "But I watch as he slowly raises a single eyebrow."
    show dwayne happy
    dwayne.say "I have to be honest with you, [hero.name]..."
    dwayne.say "I saw all of it, from start to finish."
    dwayne.say "I couldn't tear my eyes away for as much as a second."
    show dwayne normal
    "I find myself blinking and shaking my head in genuine surprise."
    bree.say "You really mean that?"
    bree.say "Then you liked my dance?"
    show dwayne smile
    "Dwayne gives me one firm nod of the head."
    show dwayne happy
    dwayne.say "[hero.name], I think you should seriously consider dancing more."
    dwayne.say "Preferably at places and occasions when I'm present."
    dwayne.say "As well as times when there's a chance people will connect us too."
    show dwayne normal
    return

label dwayne_after_dance_failure_with_female:
    show dwayne normal
    "Once I'm done dancing, I'm feeling pretty pleased with myself."
    "That is until I look around and see the expression on Dwayne's face."
    "He kind of looks like he just found his expensive suit is a fake."
    "Or that his hundred dollar stake is tough as an old boot!"
    bree.say "Ah..."
    bree.say "You didn't happen to watch me dancing just now..."
    bree.say "Did you, Dwayne?"
    "Dwayne's expression doesn't change in the slightest."
    show dwayne therock
    "But I watch as he slowly raises a single eyebrow."
    show dwayne shout
    dwayne.say "I have to be honest with you, [hero.name]..."
    dwayne.say "I saw all of it, from start to finish."
    dwayne.say "I watched every excruciating second."
    show dwayne normal
    "I feel myself swallowing nervously."
    bree.say "And you do mean excruciating?"
    bree.say "You didn't mean to say exciting, or exhilarating?"
    "Dwayne shakes his head at this, and I feel my heart sink."
    show dwayne shout
    dwayne.say "I think that you should refrain from dancing in future, [hero.name]."
    dwayne.say "At least at any time or place that I might happen to be present."
    dwayne.say "Or anywhere there's even the vaguest chance of someone realising we know each other."
    show dwayne normal
    return

label dwayne_halloween_invitation_female:
    show dwayne
    "Almost the moment I agreed to the Halloween party, I knew who I wanted to invite."
    "I can't think of anyone other than Dwayne that I want to be there as my date."
    "But that presents me with a couple of potential problems as well."
    "The first is that [mike.name] actually works for the guy."
    "So socialising with him too might be a little awkward for them both."
    "The second is that Dwayne's like a multi-billionaire or something!"
    "Well...maybe he's not that rich."
    "But he's definitely the richest guy that I've ever met."
    "So why would he want to come and hang out at a party we're throwing?"
    "It'd be like he was seriously slumming it!"
    "But who knows?"
    "Maybe I'm overthinking it."
    "Maybe Dwayne gets on well with all his employees."
    "And in turn that keeps him in touch with the common man."
    "So as soon as I feel like the time is right, I ask the question."
    bree.say "Dwayne..."
    bree.say "We're having a little get-together at my place."
    bree.say "It's happening on Halloween, kind of a party, yeah?"
    bree.say "And I wondered if you wanted to come?"
    "Dwayne stops what he's doing and turns all of his attention to me."
    "Plus he does that thing where he raises one eyebrow."
    "All of which makes me feel like I'm being put on the spot."
    bree.say "Erm..."
    bree.say "Well..."
    bree.say "What do you say, Dwayne?"
    bree.say "Are you coming or what?"
    if dwayne.love >= 100:

        dwayne.say "Settle down, [hero.name]..."
        dwayne.say "I heard you the first time."
        dwayne.say "And that sounds interesting."
        "I'm already nodding eagerly."
        "Doing all that I can to encourage him."
        bree.say "It does?"
        bree.say "So that means you'll come?"
        "Dwayne throws back his head and lets out a deep, booming laugh."
        "In fact it's so loud that I find myself taking a step backwards."
        dwayne.say "Of course I'll come, [hero.name]!"
        dwayne.say "It does me good to get out amongst the common people once in a while."
        dwayne.say "Reminds me of where I started out in life."
        dwayne.say "And why I worked so hard to get away from it!"
        "I'm not really listening to what Dwayne's saying by now."
        "Instead my mind's racing with thoughts of him coming to the party."
        bree.say "Brilliant, Danny..."
        bree.say "It's a costume party too."
        bree.say "So you might want to think about that."
        dwayne.say "Don't worry, [hero.name]..."
        dwayne.say "I have the perfect costume in mind."
        $ game.flags.halloween_girl = "dwayne"
    else:

        dwayne.say "I'm sorry, [hero.name]..."
        dwayne.say "But I'm already committed on Halloween."
        "I feel my mood spiralling downwards into a state of pure dejection."
        "Because I can tell from the tone of Dwayne's voice that this is a no."
        "And that he definitely isn't leaving any room for me to suggest an alternative."
        dwayne.say "You see, I've been invited to a Halloween ball."
        dwayne.say "Very high-class, high-society kind of thing."
        dwayne.say "In fact, I was going to ask you to come along..."
        "And just like that, my pit of despair becomes deeper still."
        "As Dwayne twists the knife that he's already thrust into my guts."
        dwayne.say "Ah well..."
        dwayne.say "I guess I'll just have to take Cherie with me instead!"
        "Oh man!"
        "And here I was thinking that it couldn't get any worse!"
        "Now he tells me that he's taking his wife with him."
        "The one who's back he's been seeing me behind."
        "I might have had the strength or will to argue before that."
        "But now I feel like I've had the stuffing knocked out of me."
        "So all I can do is just drop the subject and let it go."
    return

label dwayne_halloween_arrival_female:
    scene bg black with dissolve
    pause 0.1
    scene bg house at center, zoomAt(1.25, (640, 880))
    show dwayne halloween at center, zoomAt(2.0, (640, 1200))
    with wiperight
    "I open the door, eager to see who's out there and what they're wearing."
    "But instead of a face, I find myself staring into a huge pair of pecs."
    "They're smooth, tanned and practically bulging until they hit me in the face!"
    show bg house at center, traveling(1.0, 0.5, (640, 720))
    show dwayne at center, traveling(1.5, 0.5, (640, 1040))
    "I can't help taking a step backwards, eyes popping out in surprise."
    show dwayne happy
    dwayne.say "Can you smell what Dwayne is cooking?"
    dwayne.say "Dwayne says, good evening, [hero.name]!"
    show dwayne normal
    "I'm kind of puzzled as to why Dwayne's talking about himself in the third-person."
    "But the truth is that it actually helps me to get my head around what's happening."
    "I finally manage to take it all in, seeing that all he has on is a his underwear!"
    bree.say "Erm..."
    bree.say "Dwayne?"
    bree.say "Why are you in your underwear?"
    show dwayne therock
    "Dwayne responds by raising one eyebrow, staring at me pretty hard."
    show dwayne shout
    dwayne.say "It doesn't matter what you think!"
    show dwayne normal
    bree.say "I didn't say anything about what I think, Dwayne..."
    bree.say "I asked why you're wearing underpants and boots!"
    show dwayne annoyed
    "Dwayne rolls his eyes and shakes his head."
    show dwayne shout
    dwayne.say "I'm supposed to be that wrestler, [hero.name]!"
    dwayne.say "The one everybody says I look like."
    dwayne.say "Not that I see it myself - I think I'm much better looking!"
    show dwayne normal
    "Dwayne cradles his chin between his thumb and forefinger."
    "And at the same time he continues to pout and pose."
    "Then it hits me - he does look just like that wrestler."
    "You know the one that's in all the action movies?"
    "And Dwayne seems to notice it dawning on me too."
    show dwayne happy
    dwayne.say "Uh-huh?"
    dwayne.say "You starting to get it, [hero.name]?"
    show dwayne smile
    menu:
        "Compliment":
            "I can't help eyeing-up the sheer amount of Dwayne that's on show."
            "I've only ever seen him this scantily clad before when he was in the pool."
            "But here he is, walking around wearing just a sliver of spandex!"
            bree.say "It took some balls to come dressed like that, Dwayne!"
            bree.say "You'd better come in before you freeze to death."
            "I step aside to clear the way into the house."
            "And Dwayne nods his head as he strides into the hallway."
            dwayne.say "Part of me wishes I could dress like this all the time, [hero.name]."
            dwayne.say "After all, I spend so much time and money on perfecting my body."
            dwayne.say "It should be on show, like any other work of art!"
            "I'm nodding the whole time that Dwayne's saying all of this."
            "And the truth is that I can hardly hear a word of it."
            "All that's on my mind right now is getting my hands on those muscles."
            "That and keeping the other girls at the party away from them too!"
        "Criticize":
            "I can't help screwing up my face at what I see before me."
            bree.say "Don't you think it's a little bit on the nose, Dwayne?"
            bree.say "I mean, people tell you that you look like some wrestler."
            bree.say "And you just run off and dress up like him?"
            show dwayne upset
            "Dwayne's expression changes as he processes my response."
            "And I can already see he's not pleased with it."
            show dwayne shout
            dwayne.say "What are you trying to say, [hero.name]?"
            dwayne.say "What's wrong with that?"
            show dwayne upset
            "I shrug and let out a sigh."
            bree.say "Ah..."
            bree.say "I kind of thought you were more original than that."
            bree.say "Plus you're going to be freezing before the end of the night!"
            bree.say "Didn't you bring a coat or anything?"
            show dwayne shout
            dwayne.say "Well I'm gonna get cold standing here on the doorstep for sure!"
            dwayne.say "Are you going to invite me in, or what?!?"
            show dwayne shout
            "I step aside and Dwayne stalks into the hallway."
            "Closing the door, I can already feel this is going to be a long night."
    scene bg black with wiperight
    $ renpy.pause(1)
    return

label dwayne_halloween_party_female:
    $ game.pass_time(2)
    scene bg livingroom
    with dissolve
    "I'm just grabbing a refill from the punchbowl for Dwayne and myself."
    "Which means my attention is totally focussed on the cup and ladle."
    "But I can hear the altercation going on long before I get back with the drinks."
    "And as I do the source of all the noise becomes painfully apparent."
    show dwayne halloween upset at center, zoomAt(1.25, (400, 900))
    show scottie halloween upset at center, zoomAt(1.25, (880, 900))
    with dissolve
    "Dwayne is standing almost nose-to-nose with Scottie."
    "Both of them have their chests puffed out like strutting cocks."
    "And I already think I can guess the cause of the issue here."
    show dwayne angry
    dwayne.say "You need to learn some respect, little boy!"
    show dwayne upset
    show scottie angry
    scottie.say "Oh yeah?"
    scottie.say "And who's gonna teach it to me, old man?!?"
    show scottie upset
    "Putting the drinks down, I push my way between the two of them."
    show dwayne halloween upset at center, zoomAt(1.25, (340, 900))
    show scottie halloween upset at center, zoomAt(1.25, (940, 900))
    with ease
    "Which isn't easy when they're such a pair of beefcakes."
    "But luckily for me, they're also meat-heads."
    "So I can kind of take them by surprise."
    bree.say "Break it up, you two!"
    bree.say "This is a party, not a pose-down!"
    show dwayne annoyed
    show scottie annoyed
    "Dwayne and Scottie both back off at this."
    "And they at least have the character to look a little ashamed."
    bree.say "Okay..."
    bree.say "Now what's going on here?"
    show scottie angry
    scottie.say "He started it, [hero.name]!"
    scottie.say "He insulted my costume!"
    show scottie annoyed
    show dwayne vangry
    dwayne.say "Don't listen to this punk, [hero.name]..."
    dwayne.say "He's full of BS - and he's been making ageist comments!"
    show dwayne annoyed
    menu:
        "Defend Dwayne":
            "I can guess what happened here."
            "Dwayne and Scottie are both musclebound, egotistical jerks."
            "But only one of them is dumbass male bimbo with less brains than a squashed tomato!"
            bree.say "Are you for real, Scottie?"
            bree.say "Sasha only invited you out of pity."
            bree.say "And you repay her by starting a fight?!?"
            scottie.say "Huh?"
            scottie.say "What did you say about Sasha and pity?"
            dwayne.say "That's right, [hero.name]..."
            dwayne.say "You tell him!"
            bree.say "Shut up, Dwayne!"
            dwayne.say "Okay, [hero.name], okay!"
            bree.say "Now you listen to me, Scottie..."
            bree.say "And you listen good."
            bree.say "I don't want to hear another peep out of you tonight."
            bree.say "Because if I do, I'm going to go find Sasha."
            bree.say "And I'm going to tell her that you tried to touch my ass!"
            "A look of genuine fear appears on Scottie's face."
            scottie.say "You...you wouldn't?"
            bree.say "Try me!"
            scottie.say "But, but...Sasha would kick my ass!"
            bree.say "And I have the popcorn all ready to watch it!"
            "Scottie hurries off, shaking his head at the mere prospect."
            dwayne.say "Well done, [hero.name]..."
            dwayne.say "You sure told him!"
            bree.say "Do me a favour, Dwayne..."
            bree.say "Don't get into anymore fights tonight?"
        "Defend Scottie":
            "I can guess what happened here."
            "Dwayne and Scottie are both musclebound, egotistical jerks."
            "But only one of them is the CEO of a big company and supposedly a pillar of the community."
            "The other is a dumbass male bimbo with less brains than a squashed tomato!"
            bree.say "Are you for real, Dwayne?"
            bree.say "I leave you alone for five minutes."
            bree.say "And I come back to find you fighting with this cabbage?!?"
            scottie.say "Huh?"
            scottie.say "What did you call me?"
            bree.say "Shut up, Scottie!"
            scottie.say "Okay, [hero.name], okay!"
            dwayne.say "But, [hero.name]..."
            dwayne.say "He was the one that started it!"
            bree.say "A likely story, Dwayne!"
            bree.say "Urgh..."
            bree.say "I'm not letting you out of my sight for the rest of the night!"
            "Dwayne looks down at his feet and mutters something under his breath."
            "Great, so he's going to be sulking for the remainder of the party."
            "But at least that's better than him getting into fights with morons."
    scene bg black with dissolve
    $ renpy.pause(1)
    return

label dwayne_halloween_dance_female:
    $ game.pass_time(2)
    scene bg livingroom
    show dwayne halloween
    with dissolve
    "I feel Dwayne's hands on my hips before I hear his voice."
    "But when he speak, he's booming away right by my ear."
    "So it's impossible to hear what he's trying to say to me."
    dwayne.say "Come on, [hero.name]..."
    dwayne.say "They're playing my song!"
    dwayne.say "So it's time to dance."
    "Before I know what's happening, I'm being moved towards the dancefloor."
    "Dwayne's totally taken me by surprise, so I'm not really resisting."
    "And he's so strong that I'm almost being swept off of my feet!"
    "I mean, I don't even know if I want to dance at all."
    menu:
        "Accept":
            "I feel the instinct to struggle and dig in my heels."
            "Because who really wants to be man-handled like that?"
            "But then I remember that this is supposed to be a party."
            "And I decide that I should probably go along with it."
            bree.say "Okay, Dwayne, okay..."
            bree.say "You don't have to drag me!"
            dwayne.say "Huh?"
            dwayne.say "What was that, [hero.name]?"
            dwayne.say "I wasn't listening to you!"
            "I feel like I have to force a smile onto my face as Dwayne says this."
            "Because it kind of makes me feel like a fool for letting him have his way."
            "And all the time we're dancing, I can't help dwelling on that notion."
            "That I really should be standing up for myself in small ways like that."
            "Or else he's going to feel the need to listen to me less and less."
        "Refuse":
            "I feel the instinct to struggle and dig in my heels."
            "Because who really wants to be man-handled like that?"
            "Sure, I could just go along with it, as this is a party."
            "But I don't like Dwayne thinking he can just push me around like that."
            bree.say "Okay, Dwayne..."
            bree.say "Time to put on the brakes!"
            "I put all of my strength into resisting."
            "And even then I don't actually manage to stop Dwayne."
            "More like I put an obstacle in his path."
            "So he ends up stumbling over me instead."
            dwayne.say "Whoa..."
            dwayne.say "What's the matter, [hero.name]?"
            bree.say "You can't just pick me up whenever you feel like it, Dwayne."
            bree.say "Next time, I'd be grateful if you waited for an actual answer!"
            "Dwayne raises a single, quizzical eyebrow."
            "But he nods all the same."
            dwayne.say "Of course, [hero.name]..."
            dwayne.say "I just got carried away, that's all!"
            "I'm not totally sure I buy it."
            "But at least I made Dwayne stop and think about his actions."
    scene bg black with dissolve
    $ renpy.pause(1)
    return

label dwayne_halloween_sex_female:
    scene bg livingroom with dissolve
    "It's getting late by now, and the party seems to be winding down."
    "Most of the guests are tired and more than a little drunk."
    "And they seem more interested in chilling out than being wild."
    "I'm just about to take a break from my duties as host for the night."
    show bg livingroom at center, zoomAt(1.1, (640, 720))
    show dwayne halloween at center, zoomAt(2.0, (640, 1200))
    with hpunch
    "But as I turn around, I find myself staring into a wall of solid muscle."
    "And as it's happened to me before earlier in the night, I kind of take it in my stride."
    bree.say "Oh..."
    bree.say "Hi there, Dwayne."
    bree.say "For a moment, I thought you were the wall!"
    show dwayne at center, traveling(1.5, 0.5, (640, 1040))
    "Dwayne takes a step back so that I can actually see his face."
    "But he doesn't seem to be insulted in the slightest by what I just said to him."
    show dwayne shout
    dwayne.say "Ha!"
    show dwayne happy
    dwayne.say "I'm more a rock than a brick, [hero.name]."
    dwayne.say "But I do have a lot in common with a wall."
    dwayne.say "I'm totally solid and I hold up everything else around me!"
    show dwayne smile
    "I can't help shaking my head and rolling my eyes at this."
    "But I have to let out a giggle as well, because it's so corny."
    bree.say "Whatever, Dwayne..."
    bree.say "I think the party's coming to an end, you know?"
    bree.say "That's a relief for me - no more entertaining!"
    show dwayne therock
    "Dwayne raises a single eyebrow at this."
    "And then he leaps into action before I know what's happening."
    show dwayne at center, traveling(1.65, 0.2, (640, 1180))
    pause 0.2
    show bg livingroom at center, traveling(1.3, 0.3, (640, 940))
    show dwayne at center, traveling(2.5, 0.3, (640, 1740))
    with vpunch
    "In one move he reaches down, scooping me up and off my feet."
    bree.say "Whoa!"
    bree.say "Dwayne..."
    bree.say "What are you doing?"
    "Dwayne doesn't stop to provide me with an answer."
    "Instead he strides straight to the stairs and starts to climb them."
    show dwayne happy
    dwayne.say "You're right, [hero.name]..."
    dwayne.say "It's time for you to lie back and relax."
    dwayne.say "Now I'm going to be the one entertaining you!"
    show dwayne smile
    "I think about protesting, about demanding to be put down."
    show bg secondfloor with fade
    "But then I see that we're rapidly approaching the door of my bedroom."
    "And I wonder what in the hell I was thinking!"
    "Being carried in Dwayne's arms like this is pretty thrilling."
    "He's so big and powerful, handling me like it's no problem for him."
    "In fact, I'm already thinking about what he has in mind next."
    "And it's making me feel all tingly inside!"
    play sound door_slam
    show dwayne normal
    with hpunch
    "So instead I choose to keep my mouth shut as he kicks open my door."
    show bg bedroom4 with hpunch
    "Dwayne strides inside, swinging his leg backwards to close it again."
    "He makes it to the bed in two strides."
    "And I'm expecting him to lay me down gently."
    "Which is why it comes as a surprise a moment later when he swings me around."
    "Dwayne still has hold of my across my chest and under one arm."
    play sound bed_jump
    show dwayne_cowgirl_bg as bg zorder 1
    show dwayne zorder 2 at center, traveling(2.0, 0.1, (340, 1340))
    with vpunch
    "And he uses it to slam me down onto the mattress."
    bree.say "Aargh!"
    bree.say "What the hell?!?"
    show dwayne halloween happy
    dwayne.say "You survived the 'Dwayne Deadline', [hero.name]..."
    dwayne.say "But you won't shrug off the 'Boss's Elbow'!"
    play sound bed_jump
    show dwayne smile at center, traveling(2.5, 0.1, (640, 1640)) with ease
    "I only just manage to dart out of the way as Dwayne leaps into the air."
    show dwayne smile at center, traveling(2.5, 0.1, (640, 1640))
    with vpunch
    "And it feels like a miracle that my bed survives him landing bodily on it too!"
    with vpunch
    "The impact of Dwayne hitting the mattress beside me tosses me into the air as well."
    "But somehow he manages to land on his side, reclining on his elbow."
    show dwayne shout
    dwayne.say "What's the matter, [hero.name]?"
    dwayne.say "I'm just playing the part!"
    show dwayne smile
    "Dwayne gestures to his costume by way of explanation."
    "And I realise he's pulling off the moves of the wrestler he came to the party as."
    bree.say "Okay, okay..."
    bree.say "I get it now."
    bree.say "Can we please drop the wrestling moves?"
    dwayne.say "Fine, [hero.name]..."
    dwayne.say "Let's try a different kind of wrestling altogether!"
    scene bg black
    show dwayne cowgirl halloween
    with fade
    "Rather than saying anything in response, I let my actions speak for themselves."
    "As I reach out and start to pull down the tiny trunks that Dwayne's wearing."
    "This puts a smile on his face, and he scoots over, straddling me as he does so."
    "Undressing him only takes a matter of seconds, but I take a lot longer."
    "Because I'm wearing more than trunks and a pair of boots!"
    "But soon enough, I tear the last of my clothes off."
    "And once that's done, Dwayne doesn't waste another second."
    "I can't help gasping at the sight of his manhood as it descends upon me."
    "Sure, that's only going to help inflate his ego even more."
    "But there's just no way that I can be blase about it."
    "And I really do find myself wondering if it'll fit!"
    "Dwayne makes sure to tease me with the tip at first."
    "Stroking it up and down along the length of my lips."
    "I moan and sigh every time he does so."
    "And I can feel things loosening up down there with each pass."
    play sexsfx1 slide_in
    show dwayne cowgirl at startle(0.1,-20)
    "Finally he begins to sink inside, the lips beginning to part."
    "From there, Dwayne slowly presses down, inching his way inside."
    show dwayne cowgirl ahegao
    bree.say "Mmmh..."
    bree.say "Dwayne..."
    bree.say "Don't stop - fill me up!"
    "Dwayne's smile is broader than ever as he does just that."
    show dwayne cowgirl normal bulge
    "And once he can't go any deeper, he stays as still as a statue."
    "All the time I'm wriggling and writhing beneath him."
    "I'm so full that the sensation of it is overwhelming."
    "I think that he could stay right where he is, pinning me to the bed."
    "And the result would be the same as if he started to move too."
    "Sooner or later, I'd end up losing it, cumming all the same."
    "But there's a quality to Dwayne's smile that tells me it won't happen."
    play sexsfx1 fuck_calm
    show dwayne cowgirl at startle(0.1,-20)
    "He doesn't say a word, just begins to move inside me."
    "Slowly at first, but still with devastating effect."
    "Where before I was squirming from the sensation, now I'm paralysed."
    show dwayne cowgirl at startle(0.07,-15)
    "And as he starts to pick up speed, the effect only becomes more intense."
    "Like a rock rolling down a hill, Dwayne steadily picks up momentum."
    play sexsfx1 fuck_moderate loop
    show dwayne cowgirl speed at startle(0.05,-15)
    "Before too long he's moving with some serious speed too."
    "All of those muscles are working like organic jack-hammers."
    "And the thing they're hammering away at is me!"
    show dwayne cowgirl at startle(0.05,-15)
    "At times I actually think that the bed's not going to take it."
    "That Dwayne might actually break the frame."
    play sexsfx1 fuck_speed loop
    show dwayne cowgirl at startle(0.05,-15)
    "But still my body keep soaking up all he has to give."
    "And I feel my head nodding for more as I cling onto him."
    show dwayne cowgirl at startle(0.05,-15)
    "I feel like I could go on like this forever."
    "Just becoming ever more aroused and wanting more."
    show dwayne cowgirl at startle(0.05,-15)
    "But then I feel Dwayne stiffen, and he lets out a desperate grunt."
    "Part of me is about to complain that he's already spent."
    show dwayne cowgirl at startle(0.05,-15)
    "To demand that he keeps on going until I'm ready to cum too."
    "Though all of that changes the moment I feel him let go inside of me."
    play sexsfx1 final_thrust
    show dwayne cowgirl creampie with vpunch
    "That one last thrust and the feeling of him shooting his load."
    with vpunch
    "It pushes me higher than ever before, and I just can't hold on."
    show dwayne cowgirl squirt ahegao with vpunch
    "My orgasm hits a moment later, and that's all she wrote."
    "Dwayne collapses, face down on the mattress next to me."
    "And all I can do is lie there, helpless as my entire body quivers."
    scene bg black with dissolve
    "I can feel myself passing out and falling into a deep sleep."
    "It happens before it's all over too, which plunges me into strange dreams."
    "And the fact I'm utterly spent means that I won't be waking up for a long time too."
    $ dwayne.sexperience += 1
    $ game.pass_time(1)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
