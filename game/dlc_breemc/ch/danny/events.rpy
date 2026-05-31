init python:
    Event(**{
    "name": "danny_female_event_01",
    "label": "danny_female_event_01",
    "duration": 1,
    "conditions": [
        HeroTarget(
            IsGender("female"),
            HasRoomTag("pub"),
            ),
        PersonTarget(lexi,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 30),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "danny_female_event_02",
    "label": "danny_female_event_02",
    "duration": 1,
    "conditions": [
        IsDone("danny_female_event_01"),
        IsHour(22, 4),
        HeroTarget(
            IsGender("female"),
            HasRoomTag("park"),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "danny_female_event_03",
    "label": "danny_female_event_03",
    "duration": 1,
    "conditions": [
        IsDone("danny_female_event_02"),
        HeroTarget(
            IsGender("female"),
            IsRoom("date_nightclub"),
            ),
        PersonTarget(mike,
            OnDate()
            ),
        PersonTarget(danny,
            IsRoom("alley", "nightclub", "nightclubbar"),
            Not(IsHidden()),
            MinStat("love", 20),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "danny_female_event_04",
    "label": "danny_female_event_04",
    "duration": 1,
    "conditions": [
        IsDone("danny_female_event_03"),
        IsHour(12, 18),
        HeroTarget(
            IsGender("female"),
            IsRoom("mall1"),
            ),
        PersonTarget(danny,
            MinStat("love", 40),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "danny_female_event_05",
    "label": "danny_female_event_05",
    "duration": 1,
    "conditions": [
        IsDone("danny_female_event_04"),
        IsHour(18, 22),
        HeroTarget(
            IsGender("female"),
            HasRoomTag("home"),
            ),
        PersonTarget(danny,
            MinStat("love", 60),
            ),
        ],
    "do_once": True,
    })


label danny_female_event_01:
    scene bg pub
    "I'm normally not one for people watching."
    "Well, no more than anyone else."
    "But tonight it feels like I just can't help myself."
    "The Winchester is pretty full for this time of week."
    "Which means nobody can see me doing it either."
    "So I've been taking the chance to watch Lexi."
    show lexi casual at left4 with dissolve
    "She's on the other side of the pub from me."
    "And it looks like she's talking to some people she knows."
    "I have no idea who they are to her."
    "But one of them keeps grabbing my attention."
    show danny at mostleft5 with dissolve
    "He's a tall, dark-haired and kinda handsome guy that looks to be Latino."
    "Though that's not what keeps making me steal glances in his direction."
    "That's got more to do with the fact that he's pretty much a stereotypical bad boy."
    "Black T-shirt, tight jeans and a shit-kicker's moustache."
    "And I bet that he rode here tonight on a huge motorbike too!"
    if hero.morality >= 0:
        "I can almost feel a tingle of fear when I look at him."
        "Like he's the exact kind of guy my daddy warned me about."
        "Yet somehow I can't make myself look away from him!"
    else:
        "Oh yeah, that's the kind of guy a girl dreams about in secret."
        "The kind of guy that always knows how to show her a good time!"
        "The kind of guy that's hot because he's dangerous!"
    "I do the best I can to keep from being seen while I watch him."
    "Sure, he glances over this way a couple of times."
    "But he seems to be too intent on talking to Lexi to notice me."
    "Whatever they're discussing must be pretty important."
    "Because they both seem to be getting animated over it!"
    "Eventually the conversation seems to come to a natural end."
    "I think that I see the guy palm something to Lexi."
    "Something that she shoves into her bra."
    "But that could just be my imagination."
    hide danny with easeoutright
    "The hot guy heads out of the door, and Lexi comes in my direction."
    "She elbows her way through the crowd until she sees me."
    show lexi at center with ease
    "And then she makes a bee-line for where I'm sitting."
    lexi.say "It is you, [hero.name]!"
    show lexi happy
    lexi.say "I thought I saw you from over there by the door."
    "All of a sudden I feel a cold jab of fear."
    "They did see me from the other side of the pub!"
    "What if they figured out I was staring at them too?"
    "But then I force myself to get a grip and stop panicking."
    "So what if they did see me?"
    "At the very worst Lexi and her friend saw me checking him out."
    "And that's not exactly a crime, now is it?"
    bree.say "Ah..."
    bree.say "Yeah, Lexi."
    bree.say "I spotted you too."
    bree.say "And that guy you were with..."
    "I only meant to say that in passing."
    "Yet somehow Lexi leaps on it the moment the words are out of my mouth."
    show lexi normal
    lexi.say "Oh, you mean Danny?"
    lexi.say "I didn't know you were into that kind of guy, [hero.name]!"
    menu:
        "He's kind of... hot":
            "Urgh..."
            "So much for keeping my cards to my chest!"
            "I should have figured that Lexi's good at spotting stuff like that."
            "I might as well come out and admit the truth."
            "At least that way I'll probably get a straight answer out of her."
            if hero.morality >= 0:
                bree.say "Okay, okay..."
                bree.say "I admit it, Lexi."
                bree.say "He is pretty hot!"
            else:
                bree.say "You got me, Lexi."
                bree.say "He really got my motor running."
                bree.say "If you know what I mean!"
            show lexi happy at startle
            "Lexi laughs and shakes her head."
            $ lexi.love += 2
            lexi.say "HA!"
            lexi.say "I fucking knew it!"
            lexi.say "But I know the effect Danny has on girls like you."
            show lexi normal
            lexi.say "He's like catnip for your type!"
        "I'm just curious":
            "How did Lexi guess that I was checking him out?"
            "All I did was mention that I saw the guy!"
            if hero.morality >= 0:
                bree.say "What are you talking about, Lexi?"
                bree.say "I'm not into him at all!"
                bree.say "I was just curious about your friends, that's all."
            else:
                bree.say "Who mentioned me being into him, Lexi?"
                bree.say "I mean sure, he's kind of hot."
                bree.say "And I wouldn't turn down a chance to fuck him!"
                bree.say "But I never said I was into him."
            show lexi happy at startle
            "Lexi laughs and shakes her head."
            $ lexi.sub += 1
            lexi.say "You can deny it all you want, [hero.name]."
            lexi.say "But I know the effect Danny has on girls like you."
            show lexi normal
            lexi.say "He's like catnip for your type!"
    bree.say "Hey!"
    bree.say "What's that supposed to mean?"
    "I can't keep the tone of annoyance out of my voice."
    "I know full well that Lexi's seen a lot more of life than I have."
    "In fact, compared to her, I've led a pretty sheltered existence."
    "But it still makes me prickly when she condescends to me like that."
    "Though even when I show how mad it makes me, that seems to have no effect."
    "Lexi still waves away my words like they're nothing."
    lexi.say "Ah, come on, [hero.name]."
    lexi.say "You're practically a cheerleader compared to Danny."
    show lexi wink
    lexi.say "An angel, even!"
    bree.say "Oh come on, Lexi."
    bree.say "I'm only asking to know a little about the guy."
    bree.say "It's not like I'm thinking about proposing to him!"
    bree.say "So tell me already - who is he?"
    show lexi normal
    if lexi.love <= 35:
        lexi.say "Fine, [hero.name]..."
        lexi.say "If you want to know the truth, Danny's just a friend of mine."
        lexi.say "He used to be more than that."
        $ lexi.love += 2
        lexi.say "But we've both moved on since then."
        $ danny.flags.lexi_relation = "friend"
    else:
        lexi.say "Cards on the table, [hero.name]..."
        lexi.say "Danny's my pimp."
        "I find myself blinking in surprise."
        "Like I can't actually believe what I just heard."
        bree.say "You're serious?!?"
        "Lexi nods."
        lexi.say "Totally."
        lexi.say "He sets me up with clients and takes a cut."
        show lexi annoyed
        lexi.say "More than I'd like, I gotta admit."
        lexi.say "But he brings me regular business."
        lexi.say "And if anyone messes me around..."
        show lexi normal
        lexi.say "Well, let's just say he's good at fucking their shit up!"
        if hero.morality >= 0:
            bree.say "Oh my goodness!"
            $ lexi.love += 2
            bree.say "That sounds so scary, Lexi!"
        else:
            bree.say "Wow, Lexi..."
            $ lexi.sub += 1
            bree.say "That sounds SO hot!"
        $ danny.flags.lexi_relation = "pimp"
    show lexi annoyed
    "I watch as Lexi rolls her eyes at me."
    lexi.say "Like I said, [hero.name]..."
    lexi.say "Danny's a serious guy."
    lexi.say "And he can be real hard to handle."
    show lexi normal
    lexi.say "I just want you to be sure you know what you're getting into."
    menu:
        "I'll be careful":
            "I guess that I really should swallow my pride and listen to Lexi."
            "After all, she knows this Danny guy far better than I do."
            bree.say "Okay, Lexi..."
            bree.say "I hear what you're saying."
            bree.say "I'll be careful around him."
            show lexi annoyed
            "Lexi nods."
            show lexi normal
            lexi.say "You do that, [hero.name]."
            lexi.say "A guy like Danny could eat you alive!"
            $ lexi.love += 2
            "I nod and smile."
            "But at the same time I remind myself of something."
            "I said I'd be careful around Danny, sure."
            "But I never actually said I was going to avoid him altogether."
        "Thanks for the advice":
            "I don't know if it's Lexi's attitude that makes me do it."
            "But I suddenly feel the urge to stand up for myself against her."
            show lexi surprised
            bree.say "Oh stop trying to treat me like a kid, Lexi!"
            bree.say "I'm a grown woman, and I can look after myself."
            bree.say "So I'll be the one that chooses who I do and don't get involved with."
            "I'm fully expecting Lexi to get angry and fire back at me."
            show lexi normal
            "But instead she just shrugs and shakes her head."
            lexi.say "Whatever, [hero.name]."
            lexi.say "Like you said, you're an adult."
            lexi.say "So it's your funeral."
            $ lexi.sub += 1
            hide lexi with easeoutright
            "And with that, she turns and walks away."
    scene bg black with dissolve
    return

label danny_female_event_02:
    scene bg park
    "I hate getting caught in the park at night, and usually I'll do anything to avoid it."
    "But it's just my luck that I'd get stuck walking through it as it's getting dark today."
    "I left it too late setting off back home, and now I'm watching the lights come on."
    "I really should know better than this, and I keep promising myself it won't happen again."
    "But no amount of rationalising seems to be enough to ease my mind."
    "I keep jumping at the lengthening shadows, eyeing everyone I see with suspicion."
    "Most of them are just innocent passers-by that return my gaze and then hurry on their way."
    show danny at left, dark with dissolve
    "It's only when I see a face I recognise that things change."
    "And it's a face that actually makes me stop in my tracks too."
    "Is that..."
    "It can't be..."
    "It is!"
    "That's Danny, the guy I saw with Lexi the other day."
    "He's standing just off the path, in the shadows."
    show shawn casual at mostleft5, blacker with dissolve
    "It looks like he's talking to someone that I definitely don't recognise."
    "Someone that's far more scruffy and shifty-looking then he is."
    "As I watch, I see the second guy produce a handful of banknotes."
    "That makes me stare even harder."
    "Because it's far more money than I'd expect a guy like that to have on him."
    "Well...unless..."
    "Danny takes the money and passes something to the other guy in return."
    "It's far smaller and he palms it to the scruffy guy in a really slick way."
    "Just like I saw him do with Lexi in the pub the other day."
    hide shawn
    show danny at mostleft5, dark, dark
    with easeoutleft
    "The other guy hurries away, and Danny slips back into the shadows."
    "Is he...selling drugs?"
    "In the park?"
    "That must be what Lexi meant when she said he was a bad guy!"
    menu:
        "Walk over him":
            $ danny.unhide()
            "This is one of those moments when I know what the right thing would be."
            "Right now it'd be to turn around and hurry away before Danny spots me."
            "But somehow I find myself turning in his direction and walking over."
            if hero.morality >= 0:
                "All the time I'm doing it, part of my brain is screaming at me."
                "But I just keep right on going, like someone reaching out to touch a flame."
            else:
                "Sometimes you have to tell that little voice in your head to shut the hell up."
                "Because if you don't, then you're always going to on the boring path in life."
            "As I get closer to him, I see Danny look up."
            hide danny
            show danny at center, zoomAt(1.25, (640, 940))
            with dissolve
            "He doesn't make eye-contact, just turns in my direction."
            "I guess he's not going to acknowledge me until he knows I want to speak to him."
            "That's probably the way he tries to tell a customer from a passer-by."
            show danny
            danny.say "Hey there, little lady..."
            danny.say "Is there something I can help you with?"
            if hero.morality >= 0:
                "Danny's voice is deep and rough."
                "And if I'm honest, more than a little scary!"
            else:
                "Danny's voice is gravelly in the best way possible."
                "Deep and sexy, sending a thrill through me as I hear it for the first time."
            "But I do the best I can to ignore that as I approach him."
            if hero.morality >= 0:
                bree.say "Erm..."
                bree.say "You're Danny, right?"
            else:
                bree.say "Hi there..."
                bree.say "You have to be Danny!"
            "At the mention of his name, Danny's eyes narrow."
            "And he uses them to look me up and down."
            danny.say "I might be."
            danny.say "Depends who's asking."
            if hero.morality >= 0:
                bree.say "Oh..."
                bree.say "My name's [hero.name]."
                bree.say "We have a mutual friend in Lexi."
            else:
                bree.say "You can call me [hero.name]."
                bree.say "Well, actually you can call me anything you like."
                bree.say "Or any time you like too!"
                bree.say "Because Lexi told me all about you."
            show danny smile
            "Danny nods and smiles as I throw Lexi into the conversation."
            danny.say "So you know, Lexi, do you?"
            danny.say "What did that bitch tell you about me?"
            danny.say "She'd better hope it was all good!"
            if danny.flags.lexi_relation == 'friend':
                "I feel like I need to stick up for Lexi."
                "Unfortunately that means standing up to Danny too."
                "So I take a deep breath and look him in the eye."
                if hero.morality >= 0:
                    bree.say "Hey!"
                    bree.say "There's no need to be rude about her."
                    bree.say "Lexi was just honest about you."
                    bree.say "She told me to be careful, that you were pretty real!"
                else:
                    bree.say "Don't worry, Danny."
                    bree.say "Lexi didn't tell me all of your secrets."
                    bree.say "She just told me to be careful around you."
                    bree.say "You know, on account of you being such a bad boy?"
                show danny sneaky at startle
                "Danny laughs and shakes his head."
                show danny smile
                "But I can see the way he's looking at me change."
                "Before he was suspicious."
                "Now he seems to be looking at me with a kind of respect."
                "So maybe standing up to him was the best idea."
                danny.say "Heh..."
                danny.say "I gotta admit, Lexi's got some balls on her."
                $ danny.love += 2
                danny.say "And it looks like you do too, [hero.name]!"
            else:
                "I feel like I need to score some points with Danny."
                "And unfortunately, Lexi's the easiest way to do that."
                "I comfort myself with the thought that she's a tough one."
                "So she should be able to cope with the fallout."
                if hero.morality >= 0:
                    bree.say "Well..."
                    bree.say "She kind of told me you were from the wrong side of the tracks."
                    bree.say "If you know what I mean?"
                else:
                    bree.say "She told me you were a bad guy, Danny."
                    bree.say "And that I should stay away from you!"
                show danny sneaky at startle
                "Danny laughs and shakes his head."
                "But I can see the way he's looking at me change."
                "Before he was suspicious, but now he looks almost...hungry!"
                danny.say "Ha!"
                danny.say "She told you that..."
                $ danny.sub -= 1
                danny.say "And yet here you are, checking me out for yourself!"
            show danny smile
            "Now that he's relaxed a little, Danny leans against the lamp-post."
            "And I get the feeling that he's shifting into business mode."
            danny.say "So, [hero.name]..."
            danny.say "What can I do you for?"
            danny.say "Are you after some of the good stuff?"
            danny.say "Or just the chance to bathe in my scintillating presence?"
            bree.say "Huh?"
            bree.say "What sort of stuff?"
            danny.say "Shit, powder, a hit, something for the weekend!"
            danny.say "Drugs of the illegal variety, [hero.name]!"
            danny.say "Would you like to purchase some or not?"
            menu:
                "What do you offer?":
                    "I was expecting to feel outraged at the suggestion."
                    "But somehow, coming from Danny, it doesn't have that effect on me."
                    "Instead I find myself nodding."
                    "Because I can buy the drugs from him."
                    "But that doesn't mean that I have to actually take them."
                    if hero.morality >= 0:
                        bree.say "That's right, Danny..."
                        bree.say "I want to buy some drugs."
                        bree.say "And I don't mean aspirin!"
                    else:
                        bree.say "Sure, Danny..."
                        bree.say "I could go for that."
                        bree.say "What are you selling?"
                    show danny sneaky
                    "Danny gives me that hungry smile of his again."
                    "And he opens up his jacket to show off his wares."
                    danny.say "I got uppers and downers."
                    danny.say "I got pills and powders too."
                    danny.say "Take your pick!"
                    if hero.morality >= 0:
                        bree.say "Erm..."
                        bree.say "Is...is that cannabis?"
                    else:
                        bree.say "Ooh..."
                        bree.say "So much choice!"
                        bree.say "Is that weed?"
                    "Danny holds up a baggie full of dark green stuff."
                    "For all I know, it could be supermarket oregano."
                    show danny smile
                    danny.say "Sure it is, [hero.name]..."
                    danny.say "Best that money can buy."
                    danny.say "I normally charge one hundred bucks for this much."
                    danny.say "But seeing as I like you, I'll take fifty."
                    menu:
                        "Pay 50$" if hero.money >= 50:
                            "I blink in surprise at the price."
                            "I know that I don't usually do this kind of thing."
                            "But I was expecting it to be much more than that."
                            bree.say "Is that all?"
                            bree.say "Okay, Danny..."
                            bree.say "Here you go."
                            "I hand over the money without hesitation."
                            "And Danny pauses before he takes it."
                            $ hero.money -= 50
                            $ hero.gain_item("weed")
                            "My guess is that he's regretting selling it to me so cheap."
                            "Especially now he's seen how quickly was willing to hand over the cash."
                            "But he already agreed the price with me, so he can't change his mind now."
                            "Not unless he wants to come over as a completely untrustworthy jerk!"
                            danny.say "Ah..."
                            danny.say "Okay, [hero.name]..."
                            danny.say "Pleasure doing business with you!"
                            $ danny.love += 2
                            "Danny hands me the baggie and I put it straight into my pocket."
                            bree.say "Thanks, Danny..."
                            bree.say "Maybe we could meet up again, in less risky circumstances?"
                            danny.say "Suits me fine, [hero.name]..."
                            danny.say "I get the feeling you're gonna be seeing more of me anyway!"
                            hide danny with dissolve
                            "I force a smile onto my face as I walk away from Danny."
                            "And I do the best I can not to break into a run until I'm out of sight."
                            "My belly filled with a strange mixture of excitement and fear."
                        "Negotiate":
                            "I shake my head as soon as Danny tells me the price."
                            "I know that I don't usually do this kind of thing."
                            "But I was expecting it to be much less than that."
                            if hero.morality >= 0:
                                bree.say "Oh dear..."
                                bree.say "I had no idea it was so expensive!"
                                bree.say "Is there any other way I could pay you?"
                            else:
                                bree.say "Oh no, no, no..."
                                bree.say "I'm not going to pay that much!"
                                bree.say "Surely there's some other way I can pay?"
                            show danny normal
                            "Danny crosses his arms over his chest and cradles his chin in his hand."
                            "He seems to be trying to look thoughtful, but comes across as an act."
                            danny.say "Not willing to stump up the cash, huh?"
                            danny.say "Well, well, well..."
                            danny.say "I do accept alternative forms of currency!"
                            "To make his meaning clear, Danny reaches down and unzips his flies."
                            "Then he gives me a lascivious wink."
                            menu:
                                "A blowjob, I can manage":
                                    "My eyes go wide as I watch what Danny's doing."
                                    "But then I remember just how much he makes my pulse race."
                                    "And suddenly the idea of doing it doesn't seem so bad at all."
                                    "I nod, unable to keep from licking my lips at the prospect."
                                    "The sight of which makes Danny cackle with laughter."
                                    danny.say "Come on, [hero.name]..."
                                    danny.say "Let's take a few steps over this way."
                                    danny.say "I know a spot where nobody's gonna see us."
                                    "I follow on Danny's heels, almost bumping into him when he stops."
                                    "And as soon as we're there, I get down on my knees to be ready."
                                    scene bg black
                                    show danny blowjob surprised park
                                    with fade
                                    "Danny nods, pleased to see my enthusiasm for the task at hand."
                                    danny.say "Here you go, [hero.name]..."
                                    danny.say "Show me how much you want that weed!"
                                    "I only half hear what Danny's saying."
                                    show danny blowjob hard
                                    "As that's the moment he actually pulls it out of his pants."
                                    "And as soon as I see it, I don't have to pretend any longer."
                                    "Because what emerges from his flies is impressive in the extreme."
                                    show danny blowjob opened
                                    "I can't take my eyes off it, staring harder as it gets bigger by the second."
                                    "Pure instinct takes over as I reach out for it."
                                    "And the moment I have it in my hands, there's no stopping me."
                                    show danny blowjob licking
                                    "My lips go straight to the base of the shaft."
                                    "They part to let my tongue get in on the action."
                                    "And then together they begin to caress Danny's manhood."
                                    show danny blowjob closed suck
                                    "I take it slow, more through desire than design."
                                    "Inching my way upwards, a little at a time."
                                    "This means that no part is forgotten or ignored."
                                    "I can hear Danny chuckling with delight as I work on him."
                                    "But as I go higher and it gets more intense, that slowly changes."
                                    show danny blowjob opened
                                    "His laughter becomes mixed with grunts and groans."
                                    "And before long, he's practically moaning from what I'm doing to him."
                                    "Though he's not the only one feeling things getting more intense."
                                    "By the time I reach the head of his cock, I'm feeling the same way too."
                                    "I'm totally into the flow of the oral I'm giving Danny."
                                    "And I'm getting almost as much out of it as he is."
                                    show danny blowjob closed deepthroat
                                    show sexinserts head bree zorder 1 at center, zoomAt(1, (720, 810))
                                    "That means I don't hesitate to take it as deep into my mouth as I can."
                                    "I wasn't kidding when I said that Danny's a big boy down there."
                                    "And I struggle to get it as far in as I'd like at first."
                                    show danny blowjob opened
                                    "But somehow I manage to clear my mind and focus."
                                    "Which seems to do the trick, letting the muscles of my throat relax."
                                    "Once they do so, I can finally take him in deeper still."
                                    "Normally I'd go into something like this with a game-plan."
                                    "Or at least a vague idea of how long I wanted to make it last."
                                    "The problem here is that I just jumped straight into this thing."
                                    "And I feel like I'm getting swept along with it as much as Danny."
                                    "I could have been at it for half an hour."
                                    "Or else I could just have begun five minutes ago."
                                    "That's how it feels to me."
                                    "It's only when I begin to feel Danny twitch and stiffen that changes."
                                    "Because I know it means he's close to losing it, so the end is getting near."
                                    "Looks like I have a decision to make."
                                    "And not much time to make it in."
                                    menu:
                                        "Swallow":
                                            "I do all that I can to be ready for the moment when it happens."
                                            show danny blowjob cum surprised
                                            show sexinserts head bree cum zorder 1 at center, zoomAt(1, (720, 810))
                                            with vpunch
                                            "So as Danny lets go and shoots his load, I try to swallow it whole."
                                            with vpunch
                                            "For a few seconds I think I won't make it, that I'll end up gagging."
                                            show danny blowjob closed suck with vpunch
                                            "But then I dig down deep and push on through, my eyes watering with the effort."
                                            "And I don't stop until Danny's completely spent."
                                        "Pull his cock out":
                                            show danny blowjob lick pullout
                                            hide sexinserts
                                            "I make sure to slide Danny's cock out of my mouth before it happens."
                                            show danny blowjob hard licking cum closed with vpunch
                                            "He moans at the sensation, then gasps as he starts to shoot his load."
                                            "As he does so, his cock is bobbing in front of my face."
                                            show danny blowjob normal facecum -cum
                                            "So there's nowhere else for it to go, and I take it right on the nose."
                                            show danny blowjob opened
                                            "And I make sure to open my mouth as cum spatters my face."
                                    hide sexinserts
                                    scene bg park
                                    show danny smile
                                    with fade
                                    "Afterwards I clean myself up and get back to my feet."
                                    "But to my surprise, I find that Danny's not gloating."
                                    "Instead he looks exhausted, almost weak at the knees."
                                    bree.say "Danny?"
                                    if hero.morality >= -10:
                                        bree.say "Are you okay?"
                                    else:
                                        bree.say "Was I too much for you?"
                                    "Danny moves his head in an odd way that could be either a nod or a shake."
                                    "And at the same time he holds out the baggie containing the weed."
                                    danny.say "T...take it..."
                                    $ hero.gain_item("weed")
                                    danny.say "You...earned...it..."
                                    bree.say "Ah...Danny?"
                                    bree.say "Maybe we could meet up again, in less risky circumstances?"
                                    danny.say "S...suits me..."
                                    danny.say "F...fine, [hero.name]..."
                                    danny.say "Want to...see more of...you too..."
                                    hide danny with dissolve
                                    "I force a smile onto my face as I walk away from Danny."
                                    "And I do the best I can not to break into a run until I'm out of sight."
                                    "My belly filled with a strange mixture of excitement and fear."
                                    $ danny.love += 4
                                "A blowjob ?!?":
                                    hide danny
                                    show danny
                                    "I take a step back in disgust."
                                    "And I shake my head in shock."
                                    bree.say "Eww!"
                                    bree.say "Forget it, Danny..."
                                    bree.say "I don't want the drugs that badly!"
                                    "Danny reacts more calmly than I was expecting."
                                    "He just shrugs and drops the baggie back into his pocket."
                                    danny.say "Suit yourself, [hero.name]."
                                    danny.say "No blow-job equals no blow!"
                                    "I give him a puzzled look."
                                    show danny annoyed
                                    "And suddenly he seems a little embarrassed."
                                    danny.say "Okay, okay..."
                                    danny.say "I know that wasn't blow."
                                    danny.say "But I didn't have a weed-related pun ready to go!"
                                    "I think for a moment."
                                    "And then I respond."
                                    bree.say "You could have said 'That kicked it into the tall grass'."
                                    danny.say "Erm...I guess..."
                                    bree.say "Or 'You cannabis serious?!?'."
                                    show danny smile
                                    danny.say "I get it, I get it!"
                                    bree.say "Maybe even 'I need to weed out a better offer'."
                                    danny.say "Just stop it with the puns, okay?!?"
                                    bree.say "It's fine - that was my last one anyway."
                                    bree.say "Ah...Danny?"
                                    bree.say "Maybe we could meet up again, in less risky circumstances?"
                                    danny.say "Suits me fine, [hero.name]..."
                                    danny.say "I get the feeling you're gonna be seeing more of me anyway!"
                                    hide danny with dissolve
                                    "I force a smile onto my face as I walk away from Danny."
                                    "And I do the best I can not to break into a run until I'm out of sight."
                                    "My belly filled with a strange mixture of excitement and fear."
                                    $ danny.love += 1
                "Who do you think I am ???":
                    "The very suggestion of buying drugs from Danny comes as a shock."
                    hide danny
                    show danny
                    "I shake my head and take a step backwards."
                    with vpunch
                    bree.say "WHAT?!?"
                    bree.say "Of course not!"
                    bree.say "Do I look like some kind of junkie to you?!?"
                    "I raise my voice as I'm saying all of this."
                    show danny annoyed
                    "And Danny instantly waves his hands at me."
                    danny.say "Jesus Christ!"
                    danny.say "Will you shut the hell up?"
                    danny.say "I'm trying to keep a low profile here!"
                    "I'm about to start yelling at Danny again."
                    "But then the point he's trying to make sinks in."
                    bree.say "Okay, okay..."
                    bree.say "Sorry, Danny."
                    bree.say "I'm just not used to this kind of thing."
                    show danny normal
                    danny.say "Yeah, no kidding!"
                    danny.say "Anyway, [hero.name]..."
                    danny.say "You shouldn't be so judgemental, you know?"
                    danny.say "Not all of my customers look like junkies."
                    danny.say "Some of them look a lot like you!"
                    bree.say "What's that supposed to mean?"
                    danny.say "It could mean a lot of things."
                    danny.say "It could also explain why I might think you wanted to buy drugs!"
                    "I can't help feeling a little embarrassed by what Danny just said."
                    "I mean, I was the one that walked up to him in a park at dusk."
                    bree.say "Point taken, Danny."
                    bree.say "Look, I think we got off on the wrong foot here."
                    bree.say "Maybe we could try again, in better circumstances?"
                    danny.say "Suits me fine, [hero.name]..."
                    danny.say "I get the feeling you're gonna be seeing more of me anyway!"
                    "I force a smile onto my face as I walk away from Danny."
                    hide danny with dissolve
                    "And I do the best I can not to break into a run until I'm out of sight."
                    "My belly filled with a strange mixture of excitement and fear."
                    $ danny.love -= 2
        "Hurry back home":
            "This is exactly why I don't want to be in the park after sunset!"
            "No matter how cute Danny is, I don't want him to see me here."
            "And I'm definitely not going over there to strike up a conversation!"
            hide danny with dissolve
            "Instead I put my head down and hurry on my way, not looking back."
            "All the way to the gates of the park I'm waiting to hear him call my name."
            "Or to feel the sensation of a hand on my shoulder."
            show bg street with fade
            "It's only when I'm out of there that I realise I've been holding my breath."
            "Let it out with a gasp of relief."
            "But I don't stop for a moment."
            "Not until I make it all the way back home."
            $ game.room = "street"
            $ hero.cancel_event()
    return

label danny_female_event_03:
    scene bg nightclub
    show mike date
    with fade
    "I'm seriously glad that [mike.name] suggested we go out to a nightclub to end the day."
    "I've been feeling kind of edgy for the past couple of day, weirdly unsettled."
    "And this is just the sort of thing that I needed to be able to shake it off."
    "All the noise and the pushing of the people means that my minds occupied the whole time."
    "So there's no chance for me to overthink stuff and dwell on it like I usually would."
    show mike date shout
    mike.say "[hero.name]..."
    mike.say "You ... a ....k?"
    "I can see [mike.name] looking straight at me, his lips moving."
    show mike normal
    "But the music in here is so loud that I have no idea what he's saying."
    bree.say "What?"
    bree.say "I can't hear you over the music?"
    show mike shout at center, zoomAt(1.25, (640, 880))
    mike.say "H...?"
    mike.say "I d... thi... ... can ... me ... ... ...sic!"
    show mike normal
    bree.say "What?"
    "[mike.name] stops trying to make himself heard."
    "Instead he holds up a hand and leans in close."
    "So close in fact that he's practically speaking into my ear."
    show mike shout at center, zoomAt(1.5, (640, 1040))
    mike.say "I was asking if you wanted a drink?"
    show mike normal at center, zoomAt(1.25, (640, 880))
    "He leans back and I make sure that he sees me nodding."
    show mike normal at center, zoomAt(1.5, (640, 1040))
    "Then he leans in for a second time."
    show mike shout
    mike.say "Okay..."
    mike.say "I'll go to the bar."
    mike.say "If we get separated, I'll find you on the dance-floor."
    show mike normal at center, zoomAt(1.25, (640, 880))
    "I have no concept of how [mike.name] plans to pull that off."
    "But he seems pretty confident, so I just nod again."
    hide mike with easeoutleft
    "He nods in return and turns to go, shouldering his way through the crowd."
    danny.say "Geez..."
    danny.say "I thought that guy'd never leave!"
    bree.say "Argh!"
    bree.say "What the..."
    "I leap up and then forwards at the sound of another voice in my ear."
    "Well, that and the sensation of a hand copping a feel of my ass."
    show danny at center, zoomAt(1.5, (640, 1040)) with hpunch
    "Acting on sheer instinct, I swing my arm around and slap the culprit."
    play sound spank
    pause 0.2
    with screenshot
    show danny scared at center, traveling(1.4, 0.1, (600, 1000))
    "And as the palm of my hand makes contact, only then do I see that it's Danny!"
    show danny normal at center, traveling(1.5, 0.2, (640, 1040))
    "His head turns a little at the impact, but then he looks me straight in the eye."
    if hero.morality >= 0:
        bree.say "I...I'm sorry, Danny..."
        bree.say "But you shouldn't do stuff like that!"
    else:
        bree.say "You deserved that, Danny..."
        bree.say "You can touch my ass any time you like."
        bree.say "So long as you ask first!"
    show danny smile
    "Danny rubs his cheek with one hand."
    "But I see that he's smiling too."
    danny.say "Nah..."
    danny.say "It's okay, [hero.name]..."
    danny.say "Your ass is worth getting slapped for!"
    "I shake my head, trying to hide that I'm kind of amused."
    "Yeah, I know - I should be fuming mad at Danny right now."
    "But he's one of those bad boys that kind of disarm me."
    if hero.morality >= 0:
        bree.say "Okay, Danny - you've had your fun."
        bree.say "Now tell me what you're doing here?"
    else:
        bree.say "Cut the crap, Danny..."
        bree.say "You're here for more than a the chance to touch my butt!"
    "Danny shakes his head and laughs."
    danny.say "What are you trying to imply, [hero.name]?"
    danny.say "That I followed you here or something?"
    danny.say "Last time I checked, anyone could walk in here."
    bree.say "Okay, Danny, let's pretend I believe your bullshit."
    bree.say "That doesn't explain why you're over here feeling me up!"
    show danny annoyed
    "Danny does his best to look offended."
    show danny sneaky
    danny.say "Since when was it a crime to say hi to a friend?"
    danny.say "And in a noisy place like this, you have to improvise!"
    danny.say "Anyway, enough with the small-talk."
    danny.say "Are we going to go someplace else and have fun, or what?"
    menu:
        "Follow Danny to \"have fun\"":
            if danny.love.max <= 40:
                $ danny.love.max = 40
            "I think about what Danny's proposing for a moment."
            "Then I take a quick glance around, seeing no sign of [mike.name]."
            "You know what, I bet I could go off with Danny."
            "And I could be back before [mike.name] knew a thing about it."
            if hero.morality >= 0:
                bree.say "Okay, Danny..."
                bree.say "But we have to be quick."
            else:
                bree.say "Why the hell not?"
                bree.say "Come on, Danny - let's go have some fun!"
            "Danny's face breaks into a smug grin as he takes my hand."
            "And then he doesn't hesitate to lead me away from the crowd."
            "I'm also not surprised when he heads straight for the bathroom."
            "But I already agreed to go with him, so I follow without question."
            scene bg publicbathroom
            show danny
            with fade
            "Inside he goes straight into the first vacant stall."
            "And then he locks the door behind us for good measure."
            danny.say "Now then, [hero.name]..."
            danny.say "I've got something for you right here!"
            scene bg black
            show danny blowjob limp publicbathroom
            with fade
            "I watch as Danny reaches down and unzips his flies."
            "And there's no doubt in my mind as to what he wants from me."
            if hero.morality >= 0:
                "I watch as he pulls out his manhood."
                "And I can't help my eyes going wide at the sight of it."
            else:
                "I'm smiling, filled with anticipation as he pulls out his cock."
                "And my smile becomes even wider at the actual sight of it."
            "Without needing to be told, I get down on my knees."
            "And I reach out for it with both hands."
            "I can hear Danny chuckling to himself as I set to work."
            "And I can imagine the look on his face, picture him nodding in approval."
            "He's only half-way hard to begin with, a little limp in my hands."
            "But at the touch of my fingers I can feel him begin to stir."
            show danny blowjob hard
            "Soon enough his cock is rising up in front of my face."
            "And by the time I open my lips to kiss the tip, it's good and hard."
            show danny blowjob closed suck
            "I close my eyes and part my lips, taking him straight into my mouth."
            "Another time I might have put more effort into other stuff first."
            "But we're doing this on the sly in a nightclub bathroom."
            "So I kind of feel justified in cutting to the chase."
            "Not that Danny seems to mind me dispensing with the fancy stuff."
            show danny blowjob opened
            "From the moment I'm licking and caressing, he can't keep quiet."
            "I can hear him moaning and groaning with pleasure as my head moves back and forth."
            "Sure, it's kind of flattering - but is he actually trying to get us caught?"
            "This sparks a fear in me of being discovered."
            show danny blowjob deepthroat
            "And I quicken my pace as a result."
            "Luckily for me, Danny's too distracted to realise I'm doing this."
            "Hell, if he notices any change he probably just thinks I'm trying harder to please him!"
            show danny blowjob closed suck
            pause 0.2
            show danny blowjob deepthroat
            pause 0.2
            show danny blowjob suck
            pause 0.2
            show danny blowjob deepthroat
            pause 0.2
            show danny blowjob suck
            pause 0.2
            show danny blowjob deepthroat
            "By now I'm going as fast and hard as I dare."
            "Taking him ever deeper into my mouth to make things more intense."
            show danny blowjob opened
            "I can't help flinching as Danny slams his hands against the walls of the cubicle."
            "I know that he's only bracing himself so that he can keep on his feet."
            show danny blowjob closed suck
            pause 0.2
            show danny blowjob deepthroat
            pause 0.2
            show danny blowjob suck
            pause 0.2
            show danny blowjob deepthroat
            pause 0.2
            show danny blowjob suck
            pause 0.2
            show danny blowjob deepthroat
            "But it puts me on edge again, making me want to through this without being interrupted."
            "To that end, I reach down and take hold of Danny's balls."
            "And then I begin to squeeze them pretty hard."
            "That seems to do the trick, to be enough to push him over the edge."
            show danny blowjob suck opened
            pause 0.2
            show danny blowjob deepthroat
            pause 0.2
            show danny blowjob suck
            pause 0.2
            show danny blowjob deepthroat
            pause 0.2
            show danny blowjob suck
            pause 0.2
            show danny blowjob deepthroat
            "I know for certain that he's going to cum in the next few seconds."
            "And I just have enough time left to decide how I'm going to finish this."
            menu:
                "Swallow":
                    show danny blowjob suck
                    "I let Danny's cock slip a little way back."
                    "Just enough to give me the space I'm going to need."
                    "And then I wait for it to happen."
                    show danny blowjob cum closed with vpunch
                    "As soon as he looses it, I start to swallow."
                    with vpunch
                    "The fact that I'm prepared means it goes without a hitch."
                    show danny blowjob lick pullout with vpunch
                    "I'm able to handle everything Danny can throw at me with relative ease."
                    show danny blowjob licking hard opened bodycum -cum
                    "So things come to a smooth and satisfying end."
                "Pull his cock out":
                    show danny blowjob lick pullout
                    "I let Danny's cock slide all the way out of my mouth."
                    "And then I wait patiently as it bobs in front of my face."
                    show danny blowjob closed hard licking
                    "Closing my eyes, I don't see the it as it happens."
                    show danny blowjob cum with vpunch
                    "Instead I feel the spattering of cum on my face."
                    with vpunch
                    "It's warm and sticky, covering my nose and cheeks."
                    show danny blowjob facecum bodycum opened -cum with vpunch
                    "Some of it even lands on my lips, letting me taste it too."
            "Danny's still leant against the wall of the cubicle when I'm done."
            "And he doesn't recover the power of speech until I'm all cleaned up."
            scene bg publicbathroom
            show danny
            with fade
            danny.say "God damn it..."
            $ danny.love += 4
            danny.say "That was fucking fantastic!"
            if hero.morality >= 0:
                bree.say "Thanks, Danny..."
                bree.say "[mike.name]'s going to be looking for me."
            else:
                bree.say "Just a little something to keep me on your mind!"
                bree.say "Now I have to go, or else [mike.name]'ll get suspicious."
            danny.say "What?"
            danny.say "You're still gonna go find him?"
            danny.say "Even after what we just did?!?"
            if hero.morality >= 0:
                "Let me worry about [mike.name]."
                "I know him far better then you do!"
            else:
                bree.say "Oh, grow up, Danny!"
                bree.say "What [mike.name] doesn't know can't hurt him."
            "With that I walk out of the bathroom to find [mike.name]."
            "All the time telling myself that I can handle this."
            "I can live with what just happened behind his back."
            "Or at least I hope I can."
            $ mike.love -= 2
            $ game.active_date.score -= 10
            $ game.active_date.stay = False
        "Stay with [mike.name]":
            "By way of answer, I give Danny a snarky smile."
            "Then I turn my back on him and walk into the crowd."
            hide danny with dissolve
            danny.say "Hey!"
            danny.say "Where are you going?"
            danny.say "I'm not done talking to you!"
            "But as far as I'm concerned, he is."
            "And I'm already searching the crowd for sight of [mike.name]."
            "I came here with him and I have no intention of ditching him."
            "Especially so that I can go running off with Danny."
            danny.say "[hero.name]..."
            danny.say "Get back here!"
            "The sound of Danny's voice makes me look back over my shoulder."
            show danny angry at center, zoomAt(1.25, (640, 880)) with dissolve
            "And I see him pushing his way after me, an angry look on his face."
            "I feel a genuine pang of fear at the notion of Danny being mad with me."
            "But help comes in the form of a guy that Danny tries to shove aside."
            "I don't see much, but I can tell he's as big as Danny, maybe even bigger."
            "And the two of them are exchanging pushes and cross words."
            hide danny with dissolve
            "Taking the chance to escape, I go deeper into the crowd."
            "And I don't stop until I literally bump into [mike.name]."
            show mike date happy at center, zoomAt(1.5, (640, 1040)) with hpunch
            mike.say "Whoa..."
            mike.say "Hey, [hero.name] - looks like you found me!"
            show mike normal
            "[mike.name]'s face falls as he notices that I'm a little shaken-up."
            show mike shout
            mike.say "Hey..."
            mike.say "What's the matter?"
            show mike normal
            bree.say "It's nothing..."
            bree.say "I just bumped into a guy that wouldn't take no for an answer!"
            show mike shout
            mike.say "That doesn't sound like nothing to me!"
            mike.say "You want me to go tell security, [hero.name]?"
            show mike normal
            bree.say "No, [mike.name]..."
            bree.say "I'm sure I lost him in the crowd."
            "[mike.name] doesn't look convinced."
            "But he lets it go like I asked."
            "And pretty soon we're dancing like nothing happened."
            "That is until [mike.name] gets roughly shoved into his ass!"
            show danny at center, zoomAt(1.5, (540, 1040)) with easeinleft
            hide mike surprised at center, zoomAt(1.5, (940, 1040)) with easeoutright
            show danny at center, zoomAt(1.5, (440, 1040)) with ease
            mike.say "Wha..."
            mike.say "Urgh!"
            danny.say "Mind if I cut in on this one?"
            danny.say "Hah - like you've got a choice!"
            show danny at center, zoomAt(1.5, (340, 1040))
            show mike date angry at center, zoomAt(1.5, (940, 1040))
            with easeinright
            "Before I can do anything to stop it, [mike.name] springs to his feet."
            "He comes at Danny, but the other guy's more then ready for him."
            "In seconds, fists are flying and blows are connecting."
            hide danny
            hide mike
            show danny fight win at center, zoomAt(1.85, (740, 1280))
            pause 0.2
            with hpunch
            "But it's not like [mike.name] every really stood a chance."
            "I watch in fascinated horror as Danny takes him to pieces."
            "And by the time the bouncers arrive to pull them apart, [mike.name] can barely stand without help."
            "What follows is a confused scuffle as both of them are tossed out of the place."
            "All I can do is follow along as it happens."
            scene bg alley
            show mike annoyed date
            with fade
            "But once we're outside, [mike.name]'s recovered enough to speak."
            mike.say "Urgh..."
            mike.say "Come on, [hero.name]..."
            show mike shout
            mike.say "Let's jump in that taxi."
            show mike angry
            mike.say "Anything to get away from this psycho!"
            "His words instantly set Danny off again."
            show mike at right4 with ease
            show danny at left with easeinleft
            "And he makes to close the distance between us."
            show danny angry
            danny.say "You're really gonna slink off with this pussy, [hero.name]?"
            danny.say "Even after I just stomped his ass flat to get to you?!?"
            show danny sneaky
            danny.say "Let him crawl off and lick his wounds."
            danny.say "And you can lick something of mine instead!"
            menu:
                "Go home with [mike.name]":
                    $ mike.love += 2
                    "I shoot Danny one last venomous look."
                    scene bg taxi night car open with fade
                    show mike date at left with easeinleft
                    "And then I bundle [mike.name] into the taxi."
                    hide mike with dissolve
                    "As I climb in after him, I make a point of not glancing in Danny's direction."
                    play sound car_door
                    scene bg taxi night car closed with dissolve
                    "In fact I don't even speak a word until the taxi's well away from the nightclub."
                    scene bg street night zorder 1 at center, zoomAt (1.5, (540, 420))
                    show dwayne limo as taxi zorder 2 at center, zoomAt(1.75, (420, 1220))
                    show mike date zorder 3 at center, zoomAt(1.65, (820, 1140))
                    with fade
                    if hero.morality >= 0:
                        bree.say "Oh, [mike.name]!"
                        bree.say "I'm so sorry!"
                        bree.say "What did that animal do to you?"
                    else:
                        bree.say "Wow, [mike.name]..."
                        bree.say "I never knew you could take that much punishment!"
                        bree.say "You must be SO rugged!"
                    show mike annoyed
                    mike.say "Ah..."
                    mike.say "He kicked my ass, [hero.name]!"
                    mike.say "Where in the hell did you meet a bastard like him?!?"
                    "I can feel my cheeks beginning to burn with shame."
                    "Because I was getting a cheap thrill from associating with Danny."
                    "And now it's resulted in [mike.name] getting hurt."
                    "It seems like the least I can do is be honest with him."
                    bree.say "His name's Danny..."
                    bree.say "He's one of Lexi's...friends."
                    mike.say "Huh!"
                    mike.say "That figures - Lexi knows all kinds of scumbags."
                    "I feel [mike.name] take hold of my hand."
                    mike.say "I just wanted to say, [hero.name]..."
                    show mike happy
                    mike.say "Thanks for staying with me."
                    if hero.morality >= 0:
                        bree.say "I could never abandon you, [mike.name]."
                        bree.say "Seeing you hurt like that..."
                        bree.say "Well, it reminded me of how much I'm into you!"
                    else:
                        bree.say "Are you kidding, [mike.name]?"
                        bree.say "The fight's not important."
                        bree.say "You were defending your woman - and that's SO hot!"
                    hide mike
                    show mike kiss date zorder 3 at flip
                    with fade
                    $ mike.flags.kiss += 1
                    "The next thing I know, [mike.name] and I are wrapped in each other's arms."
                    "We're kissing with a genuine passion, and we all but fall out of the taxi."
                    scene bg livingroom
                    show mike kiss date
                    with fade
                    "From there we hurry inside, still in a tangle of limbs."
                    show bg bedroom1 with dissolve
                    "Somehow we find our way to [mike.name]'s bedroom."
                    "And once there we don't hesitate to tear off each other's clothes."
                    "Neither of us speaks while all of this is happening."
                    "And that's not just because we're kissing the whole time."
                    "I honestly believe that it's because we've said all we can say."
                    "Now the only way left to prove that we meant all of those words is physical."
                    "[mike.name] and I care connecting on a totally different level now."
                    "And desperate, almost animalistic sex is the next logical step."
                    "Of course I'm thinking all of this in the privacy of my own head."
                    "But [mike.name]'s doing everything right to convince me that we're thinking alike."
                    show mike kiss naked with dissolve
                    "As his clothes start to come off though, I see something that makes me pause."
                    "Here and there, bruises are already starting to discolour [mike.name]'s skin."
                    "And they can only be from where Danny hit him earlier."
                    "[mike.name] winces when I touch one of them, and so I instinctively pull back."
                    "But his instant reaction is to take hold of my hands."
                    "Then he puts them right back where they were a moment before."
                    "The message is clear as it can be."
                    "He won't let what happened at the nightclub come between us."
                    "As gently as I'm able, I push [mike.name] down onto the bed."
                    scene bg black
                    show mike cowgirl bedroom1
                    with fade
                    "By now we're both naked, and so I make to straddle his thighs."
                    "The care I'm taking means that it's a slow process."
                    "But it also means that he's treated to a great view of me as I do so."
                    "And by the time I'm in position, I can see that he's more than ready for me."
                    "I reach down and take a firm hold of his now hard cock."
                    "As I do so, I say a little silent thank you that was spared in the fight."
                    "[mike.name] sighs as I stroke up and down the shaft."
                    show mike cowgirl out
                    "Then he groans with pleasure as I press it against the lips of my pussy."
                    "It doesn't take long for my body to warm up to the idea of him inside me."
                    "So the natural resistance fades a little more with each passing second."
                    show mike cowgirl vaginal
                    "Until the moment when I push and there's nothing to resist at all."
                    "[mike.name]'s cock begins to inch its way into me."
                    "And I use my weight to press down, guiding it home."
                    "Then I make sure not to stop until it can go no further."
                    "What follows is a text-book example of slow, sensual love-making."
                    "Every move I make is thought out and controlled."
                    "But that does nothing to rob it of intensity and passion."
                    "In fact it only serves to make the whole thing that much more intense."
                    "Each and every time I move, the sensations we share are incredible."
                    "They seem to stretch on, beyond mere seconds and minutes."
                    "As if they're entering a kind of time that's elastic in nature."
                    "I have my hands pressed on [mike.name]'s belly, holding myself up."
                    "And the only part of me moving at all is my hips."
                    "His hands are under my arms, holding me up at the same time."
                    "At some point I seem to forget all about the need to treat him gently."
                    "Because everything else has been subsumed in the desire to keep things slow."
                    "That's why it comes as a shock when [mike.name] suddenly stiffens."
                    "It's the first quick and unexpected motion either of us has made."
                    show mike cowgirl creampie with vpunch
                    "But I discover the reason a moment later, when he erupts inside of me."
                    with vpunch
                    "My thighs clench and bear down on him, holding me in place."
                    with vpunch
                    "And it doesn't take long for my own climax to cum on the heels of his."
                    "With an almost agonising slowness, I lower myself down onto him."
                    "Then I stay there, laid upon his chest as it takes me over."
                    $ mike.sexperience += 1
                    $ danny.set_gone_forever()
                    $ hero.replace_activity()
                    $ game.active_date.stay = False
                    $ game.room = "bedroom1"
                    $ game.pass_time()
                "Go off with Danny":
                    if danny.love.max <= 40:
                        $ danny.love.max = 40
                    "Part of me can't quite believe I'm doing this."
                    scene bg taxi night car open with fade
                    show mike date at left with easeinleft
                    "But all the same, I bundle [mike.name] into the taxi alone."
                    mike.say "[hero.name]..."
                    mike.say "Aren't you coming with me?"
                    bree.say "No, [mike.name]."
                    bree.say "Someone needs to put this guy in his place."
                    bree.say "And that someone's going to be me!"
                    hide mike with dissolve
                    pause 0.2
                    play sound car_door
                    scene bg taxi night car closed with dissolve
                    "As the taxi pulls away, I turn to face Danny."
                    scene bg alley
                    show danny smile
                    with fade
                    bree.say "And as for you..."
                    "My hand shoots out and grabs him by the wrist."
                    bree.say "You're coming with me!"
                    "Danny seems too shocked by my actions to be able to resist."
                    "I have no trouble dragging him away from the nightclub and into a nearby alley."
                    "As soon as we're out of sight, I make my move."
                    danny.say "[hero.name]..."
                    danny.say "What the hell..."
                    hide danny
                    show danny kiss
                    with hpunch
                    $ danny.flags.kiss += 1
                    danny.say "Mmmph..."
                    "My lips clamp down over his, and I pull him down to my level."
                    "The kiss is long and passionate, involving more than just lips."
                    "When Danny finally breaks away, he staggers backwards."
                    "And all that stops him landing on his ass is him backing up into the wall."
                    hide danny
                    show danny smile at center, zoomAt(1.5, (640, 1040))
                    with vpunch
                    danny.say "Whoa..."
                    danny.say "Where did that come from, [hero.name]?"
                    danny.say "I...I thought you were gonna put me in my place!"
                    if hero.morality >= 0:
                        bree.say "I can't help it, Danny."
                        bree.say "You just do something to me."
                        bree.say "I know that it's wrong - but I can't help it!"
                    else:
                        bree.say "I had to say that to get rid of [mike.name]'s loser ass."
                        bree.say "After I saw the way you put him down back there..."
                        bree.say "That was SO manly!"
                    show danny normal
                    "Danny just stares at me blankly for a couple of seconds."
                    "It's almost like he's gotten so used to women rejecting his bad-boy image."
                    "So used to it that he doesn't know what to do when one of them actually goes for it!"
                    "But little by little I can see the fog in his brain starting to clear."
                    "The lascivious twinkle comes back into his eyes, and his lips curl into a smile."
                    show danny smile
                    danny.say "So you just couldn't resist me, eh?"
                    danny.say "Can't say that I blame you!"
                    with vpunch
                    danny.say "Urgh..."
                    "Danny lets out a grunt as I push him back against the wall."
                    show danny surprised
                    "And then he looks down in surprise as I start unzipping his flies."
                    danny.say "Hey!"
                    danny.say "Who said you could touch that?!?"
                    "I look up at him in sheer amazement."
                    bree.say "Really, Danny?"
                    bree.say "Are you being serious right now?"
                    danny.say "I...I dunno, [hero.name]..."
                    danny.say "Sometimes it's nice to ask first, you know?"
                    "I shake my head and get back to the task at hand."
                    "And a few moments later, I have Danny's cock out of his pants."
                    if hero.morality >= 0:
                        bree.say "No more bullshit now, Danny."
                        bree.say "Because I really need this, okay?"
                    else:
                        bree.say "Eyes on the prize now, Danny."
                        bree.say "Because you'd better deliver on fucking me!"
                    show danny smile
                    "Danny nods, as if finally realising that I'm the one in charge here."
                    "And I almost breath a sigh of relief as he springs into action."
                    "I feel his hand under my skirt, roughly pulling down my panties."
                    scene bg black
                    show danny stand fingering alley eyes_closed
                    with fade
                    "And just like that his fingers are between my legs."
                    "They're hard and rough, but they feel incredible against my pussy."
                    "Danny strokes my a little, the pushes one of them a little way inside."
                    danny.say "Mmm..."
                    danny.say "Feels like you're gettin wet down there, [hero.name]!"
                    danny.say "Like you're wanting something, and wanting it badly!"
                    show danny stand mouth_pleasure
                    if hero.morality >= 0:
                        bree.say "Oh..."
                        bree.say "Oh yeah..."
                        show danny stand eyes_scared
                        bree.say "I want it, Danny!"
                    else:
                        bree.say "Oh fuck..."
                        bree.say "Don't tease me, Danny..."
                        show danny stand eyes_scared
                        bree.say "I want you in me!"
                    "Danny grabs my ass with both hands, then he lifts me off the ground."
                    "At the same time her turns around, pinning me up against the wall."
                    show danny stand fuck
                    danny.say "Oh, you're gonna get it..."
                    danny.say "You're gonna get all of it!"
                    "Without warning, Danny pulls me down and onto his cock."
                    "By now it's standing proud, hard as it can get."
                    "And I'm practically begging for him, almost desperate."
                    show danny stand mouth_hurt eyes_closed
                    "There's a moment of resistance, but only a moment."
                    show danny stand vaginal
                    "Then I feel myself opening up to him, muscles parting slowly."
                    "But things don't stay slow, instead they begin to pick up speed."
                    show danny stand mouth_dazed
                    "Like a ball rolling downhill, momentum builds as Danny enters me."
                    "And he can't be more than halfway inside when he starts to move."
                    "There's no chance for him to fill me gradually."
                    "Instead he goes all the way in, then back and forth like a piston."
                    "I find myself clinging onto him, afraid to let go."
                    show danny stand mouth_pleasure eyes_dazed
                    "But I soon find out that Danny doesn't just look like he's built."
                    "Those muscles are for real, and he more than lives up to my expectations."
                    "There's no time for anything but a desperate coupling in the alleyway."
                    "Yet every moment that it lasts is more than memorable for me."
                    "Danny makes love like he's desperate, like a man on the run."
                    "It's like any second he expects something to come between us."
                    "And he's determined to have his way with me before it does."
                    "I know that I should be pissed at him for this."
                    "That I should demand more care and compassion."
                    "But that's just not the kind of guy he is."
                    "It's certainly not where the thrill of being with him lies either."
                    "And I can say for certain that I'm being thrilled right now."
                    "Every time Danny thrusts into me, I feel myself thrown against the wall."
                    "But all that does is make me want more!"
                    show danny stand mouth_hurt
                    if hero.morality >= 0:
                        bree.say "Oh, Danny..."
                        bree.say "I...I can't hold on..."
                        bree.say "You're going to...make me cum!"
                    else:
                        bree.say "Harder, Danny..."
                        bree.say "Fuck...me...harder!"
                        bree.say "Make me...cum!"
                    show danny stand eyes_closed
                    "My desperate pleas seem to have the desired effect."
                    "I feel Danny redouble his efforts, going faster and harder than before."
                    show danny stand mouth_dazed eyes_ahegao cum with hpunch
                    $ danny.love += 5
                    $ danny.impregnate()
                    "There's no way to tell which one of us actually cums first."
                    with hpunch
                    "He seems to lose it the exact same moment my pussy begins to squeeze him."
                    with hpunch
                    "And it's then that I'm grateful for the wall behind me."
                    "Because I can feel Danny's muscles starting to quiver."
                    show danny stand eyes_closed out vaginaldrip -cum

                    "Neither of us says a word, we just stand there and stare at each other."
                    "But then Danny smiles and begins to push his cock back into his pants."
                    scene bg alley
                    show danny casual smile
                    with fade
                    danny.say "Thanks, [hero.name]..."
                    danny.say "That was just what I needed!"
                    hide danny with fade
                    "With that, he turns and walks away."
                    "Which leaves me to make myself decent."
                    "That and wonder just what I'm getting myself into with Danny."
                    $ danny.sexperience += 1
                    $ hero.cancel_activity()
                    $ game.active_date.stay = False
    return

label danny_female_event_04:

    $ danny.flags.nokiss = False
    $ danny.flags.nodate = False
    scene bg mall1
    "It's not like I came to the mall for anything specific today."
    "Sure there are a couple of things that I could take the time to pick up."
    "But the main reason for me coming here was more to get out of the house."
    "I feel like there's been a lot going on in my life recently."
    "And I could really use the chance to just chill."
    "So the mall is the perfect place to stroll around at my own leisure."
    "It seems to be working too."
    "I wander from one unit to the next window-shopping."
    "My brain switching off as I do so, my thoughts becoming calmer."
    "That means when I hear someone calling my name, I'm totally distracted."
    danny.say "Hey, [hero.name]!"
    danny.say "Over here!"
    show danny zorder 2 at center, dark, zoomAt(1.0, (1500, 740))
    show danny at center, zoomAt(1.0, (1140, 740)) with ease
    "I turn in the direction of the call."
    "Just like almost everyone else that hears it does too."
    "But unlike them, I soon figure out that the call is for me alone."
    show danny at center, brighter, zoomAt(1.0, (1140, 740)) with dissolve
    show danny at right5 with ease
    "It's Danny, waving to me from a couple of stores away."
    "As I watch, he puts his fingers in his mouth and whistles."
    show fx exclamation zorder 2 at right5
    "Then he shouts again."
    show danny at startle
    danny.say "Come on, [hero.name]..."
    danny.say "I know you see me over there!"
    menu:
        "Walk over to see what Danny wants":
            if danny.love.max <= 60:
                $ danny.love.max = 60
            if hero.morality >= 25:
                "I shake my head at the sight of Danny."
                "But I guess I'd better go see what he wants."
                "If I don't, he'll probably make a scene."
            elif hero.morality <= -25:
                "I feel a smile creeping onto my face at the sight of Danny."
                "Maybe a bad boy like him is what I need to clear my head?"
                "So with that in mind, I start walking towards him."
            "It's not until I get closer that I see he's not alone."
            show scottie b casual zorder 1 at flip, blacker, center, zoomAt (1, (760, 800)) with dissolve
            show dwayne zorder 1 at flip, blacker, center, zoomAt (1, (930, 820)) with dissolve
            show ryan zorder 1 at flip, blacker, center, zoomAt (1, (1100, 800)) with dissolve
            show danny at left4 with ease
            "Danny's got a group of guys standing and by him."
            if hero.morality >= 25:
                "And every one of them looks just as dodgy as he does."
                "Are these what he calls his friends?"
                "I wouldn't trust a single one of them!"
            elif hero.morality <= -25:
                "Every one of them looks almost as dangerous and exciting as Danny."
                "These must be his friends, the guys he hangs out with."
                "I bet they all know how to have a good time!"
            danny.say "Come meet the gang, [hero.name]..."
            show danny smile
            danny.say "These are some of my very best buddies."
            "I do the best I can to smile as they look me up and down."
            "And all the time I just know that they're undressing me with their eyes."
            if hero.morality >= 25:
                bree.say "Erm..."
                bree.say "Hello, I guess..."
            elif hero.morality <= -25:
                bree.say "Hi there, boys!"
                bree.say "Any friend of Danny's is a friend of mine!"
            danny.say "This is the one I was telling you about, yeah?"
            danny.say "The one that I hooked up with the other day."
            danny.say "You remember - the one that gives crazy good head?"
            menu:
                "Be offended":
                    "For a moment I can't actually believe what I'm hearing."
                    show scottie b casual zorder 1 at blacker, center, zoomAt (1, (760, 800)), startle(0.1,-20)
                    show dwayne zorder 1 at blacker, center, zoomAt (1, (930, 820)), startle(0.14,-20)
                    show ryan zorder 1 at blacker, center, zoomAt (1, (1100, 800)), startle(0.12,-20)
                    pause 0.2
                    show scottie b casual zorder 1 at blacker, center, zoomAt (1, (760, 800)), startle(0.1,-20)
                    show dwayne zorder 1 at blacker, center, zoomAt (1, (930, 820)), startle(0.14,-20)
                    show ryan zorder 1 at blacker, center, zoomAt (1, (1100, 800)), startle(0.12,-20)
                    pause 0.2
                    show scottie b casual zorder 1 at blacker, center, zoomAt (1, (760, 800)), startle(0.1,-20)
                    show dwayne zorder 1 at blacker, center, zoomAt (1, (930, 820)), startle(0.14,-20)
                    show ryan zorder 1 at blacker, center, zoomAt (1, (1100, 800)), startle(0.12,-20)
                    "But then Danny's friends begin to laugh and jeer at me."
                    "Which is more than enough to shake me back to reality."
                    bree.say "Danny!"
                    bree.say "I can't believe you just did that!"
                    show danny normal
                    danny.say "Did what?!?"
                    danny.say "I dunno what you're talking about!"
                    bree.say "You think it's okay to tell them that?"
                    bree.say "To tell them stuff that personal and private?"
                    show fx question zorder 2 at left4
                    "Danny looks genuinely puzzled by my outburst."
                    danny.say "It was supposed to be a compliment, [hero.name]!"
                    danny.say "These guys appreciate a broad with skills like that."
                    show bg mall1 at center, zoomAt (1, (640, 740))
                    show bg mall1 at center, traveling(1.1, 0.2, (640, 740))
                    show scottie b casual at blacker, center, traveling (1, 0.2, (780, 820))
                    show dwayne at blacker, center, traveling (1, 0.2, (950, 840))
                    show ryan at blacker, center, traveling (1, 0.2, (1120, 820))
                    show danny at center, traveling(1.25, 0.2, (600, 880))
                    play sound spank
                    pause 0.2
                    with screenshot
                    show danny scared at hshake
                    "Danny doesn't see the slap coming."
                    "And the blow makes his head spin around."
                    "But I don't hang around to see his reaction."
                    scene bg mall1 with dissolve
                    "I just turn and walk away."
                    "I can hear him shouting after me, and so I quicken my pace."
                    "But he doesn't try to come after me."
                    "Or if he does, I make it to the exit before he can reach me."
                    scene bg street with fade
                    "As I walk out of the mall, I have no idea where I'm headed."
                    "Just that I need it to be somewhere he's not."
                    $ danny.love -= 2
                    $ hero.morality += 5
                    $ game.room = "street"
                "Be flattered":
                    "I feel a smile creeping onto my face as Danny bigs me up."
                    "And it only gets bigger when they all start to nod and laugh."
                    show scottie b casual zorder 1 at blacker, center, zoomAt (1, (760, 800)), startle(0.1,-20)
                    show dwayne zorder 1 at blacker, center, zoomAt (1, (930, 820)), startle(0.14,-20)
                    show ryan zorder 1 at blacker, center, zoomAt (1, (1100, 800)), startle(0.12,-20)
                    pause 0.2
                    show scottie b casual zorder 1 at blacker, center, zoomAt (1, (760, 800)), startle(0.1,-20)
                    show dwayne zorder 1 at blacker, center, zoomAt (1, (930, 820)), startle(0.14,-20)
                    show ryan zorder 1 at blacker, center, zoomAt (1, (1100, 800)), startle(0.12,-20)
                    pause 0.2
                    show scottie b casual zorder 1 at blacker, center, zoomAt (1, (760, 800)), startle(0.1,-20)
                    show dwayne zorder 1 at blacker, center, zoomAt (1, (930, 820)), startle(0.14,-20)
                    show ryan zorder 1 at blacker, center, zoomAt (1, (1100, 800)), startle(0.12,-20)
                    "Looks like Danny's been telling them all how great I am!"
                    bree.say "I see my reputation proceeds me!"
                    bree.say "But they'd better not go getting any ideas."
                    bree.say "Because my services aren't for sale!"
                    "It takes a moment for Danny's friends to get their head around this."
                    show scottie b casual zorder 1 at blacker, center, zoomAt (1, (760, 800)), startle(0.1,-20)
                    show dwayne zorder 1 at blacker, center, zoomAt (1, (930, 820)), startle(0.14,-20)
                    show ryan zorder 1 at blacker, center, zoomAt (1, (1100, 800)), startle(0.12,-20)
                    pause 0.2
                    show scottie b casual zorder 1 at blacker, center, zoomAt (1, (760, 800)), startle(0.1,-20)
                    show dwayne zorder 1 at blacker, center, zoomAt (1, (930, 820)), startle(0.14,-20)
                    show ryan zorder 1 at blacker, center, zoomAt (1, (1100, 800)), startle(0.12,-20)
                    pause 0.2
                    show scottie b casual zorder 1 at blacker, center, zoomAt (1, (760, 800)), startle(0.1,-20)
                    show dwayne zorder 1 at blacker, center, zoomAt (1, (930, 820)), startle(0.14,-20)
                    show ryan zorder 1 at blacker, center, zoomAt (1, (1100, 800)), startle(0.12,-20)
                    "At first they keep on laughing like before."
                    show scottie b casual zorder 1 at blacker, center, zoomAt (1, (760, 800)), stepback(0.1, 10, 0)
                    show dwayne zorder 1 at blacker, center, zoomAt (1, (930, 820)), stepback(0.13, -10, 0)
                    show ryan zorder 1 at blacker, center, zoomAt (1, (1100, 800)), stepback(0.16, 5, 0)
                    pause 0.64
                    show scottie b casual zorder 1 at blacker, center, zoomAt (1, (760, 800)), stepback(0.16, -5, 0)
                    show dwayne zorder 1 at blacker, center, zoomAt (1, (930, 820)), stepback(0.1, -10, 0)
                    show ryan zorder 1 at blacker, center, zoomAt (1, (1100, 800)), stepback(0.13, 5, 0)
                    pause 0.64
                    show scottie b casual zorder 1 at blacker, center, zoomAt (1, (760, 800)), stepback(0.13, -5, 0)
                    show dwayne zorder 1 at blacker, center, zoomAt (1, (930, 820)), stepback(0.16, 10, 0)
                    show ryan zorder 1 at blacker, center, zoomAt (1, (1100, 800)), stepback(0.1, 5, 0)
                    "But as they realise what it means, they begin to moan instead."
                    show danny annoyed
                    show fx anger zorder 2 at left4
                    "Danny doesn't seem to like the sound of their complaints."
                    "And he rounds on them in front of me."
                    danny.say "Hey, you creeps..."
                    show danny at left5 with MoveTransition(0.2)
                    show danny at center with MoveTransition(0.1)
                    show scottie b casual zorder 1 at blacker, center, zoomAt (1, (760, 800)), stepback(0.1, 20, -40)
                    show dwayne zorder 1 at blacker, center, zoomAt (1, (930, 820)), stepback(0.13, 20, -40)
                    show ryan zorder 1 at blacker, center, zoomAt (1, (1100, 800)), stepback(0.16, 20, -40)
                    show danny at left4 with ease
                    danny.say "Don't go getting any ideas, okay?"
                    show danny normal
                    danny.say "I was just showing [hero.name] off to you."
                    danny.say "I'm not gonna be handing her round like a goddamn party favour!"
                    "Danny's friends keep right on moaning and complaining."
                    "But I note that they turn away from him and refuse to meet his eye too."
                    danny.say "Sorry about that, [hero.name]."
                    danny.say "You gotta remind these guys of their place every one in a while."
                    danny.say "If you don't, they start getting out of hand."
                    bree.say "It's okay, Danny..."
                    bree.say "Looks like you handled it."
                    bree.say "So you can handle me the next time we hook up!"
                    "With that, I smile and turn to walk away."
                    hide ryan zorder 1 at blacker
                    hide dwayne zorder 1 at blacker
                    hide scottie b casual zorder 1 at blacker
                    with dissolve
                    hide danny with dissolve
                    play sound spank
                    pause 0.2
                    with vpunch
                    "Danny grins and gives my ass a hard slap."
                    "I squeal in surprise, but I keep on walking all the same."
                    "The whole time filled with the thrill of being around such a dangerous guy."
                    $ hero.morality -= 5
                    $ danny.love += 4
        "Walk away":
            "Urgh..."
            "Danny's the last thing I need right now."
            "But luckily for me, it doesn't look like he's coming any closer."
            "So I don't feel any guilt in turning my back on him and walking away."
            hide danny with dissolve
            "I can hear him shouting after me, and so I quicken my pace."
            "But he doesn't try to come after me."
            "Or if he does, I make it to the exit before he can reach me."
            scene bg street with fade
            "As I walk out of the mall, I have no idea where I'm headed."
            "Just that I need it to be somewhere he's not."
            $ game.room = "street"
            $ danny.love -= 2
            $ hero.cancel_event()
    return

label danny_female_event_05:
    if danny.love.max < 80:
        $ danny.love.max = 80
    "Dating a guy like Danny, you kind of get used to expecting the unexpected."
    "Like getting taken along to a sleazy bar when you were expecting a nice restaurant."
    "Or ducking behind a wall to avoid being seen by the cops like a normal guy would his ex."
    play sound cell_vibrate
    "So when I get a text message from Danny before I go to meet him, I'm expecting the worst."
    $ nvl_mode = "phone"
    nvl clear
    danny_nvl "Hey, babe..."
    danny_nvl "Can't wait to see you later."
    danny_nvl "And don't forget to dress sexy too!"
    "I can't help smiling at Danny's message, as it's not as bad as it could have been."
    "And I make sure to send him a message in return before I start to get ready."
    if hero.morality >= 25:
        mchero_nvl "Now, now - you'd better behave yourself!"
    elif hero.morality <= -25:
        mchero_nvl "Oh just you wait, Danny - I'm gonna blow your mind!"
    else:
        mchero_nvl "Well you'll just have to wait and see what I turn up in, won't you?"
    scene bg street at center, zoomAt(1.1, (640, 750)) with fade
    "As soon as I'm satisfied that I'm ready, I head straight out of the house."
    "And I make my way to the spot where Danny and I agreed to meet up."
    "It's a street corner down town, a spot that I know really well."
    "One that's within walking distance of more than a few decent bars and restaurants."
    "A fact that makes me hopeful Danny's going to announce that that's where we're headed."
    show danny at center, zoomAt(1.1, (640, 750)) with dissolve
    "Once I make it there, I see he's already there and waiting for me."
    show danny shout at startle(0.1, 5)
    danny.say "Hey, [hero.name]..."
    danny.say "You are looking divine today!"
    danny.say "Good thing you took my advice."
    show danny smile
    pause 0.2
    show danny at startle(0.1, 5)
    show bg street at startle(0.1, 5)
    if hero.morality >= 25:
        bree.say "Thank you for the compliment, Danny..."
        bree.say "It's nice that you'd notice."
    elif hero.morality <= -25:
        bree.say "Hah - it's nothing compared what I've got on underneath!"
        bree.say "But if you wan to see that, you'd better be taking me somewhere nice."
    else:
        bree.say "Flattery will get you everywhere, Danny!"
        bree.say "Now hurry up and tell me where were headed already."
    show danny joke at vshake
    "Danny plants his balled fists on his hips and laughs out loud."
    show danny shout at startle(0.1, 5)
    danny.say "Hah!"
    danny.say "Just take my arm and walk this way."
    show danny smile at traveling(1.2, 0.2, (640, 800))
    show bg street at traveling(1.1, 0.7, (600, 720))
    "Intrigued, I do as he says, wrapping my arm in his."
    show danny smile at startle(0.1, 5)
    show bg street at traveling(1.2, 1, (550, 720))
    "And then Danny starts leading me a little way down the street."
    show bg alley at zoomAt(1.1, (640, 720)) with dissolve
    "But a moment later he surprises me by suddenly turning down an alleyway."
    show danny at startle(0.1, 5)
    show bg alley at startle(0.1, 5)
    bree.say "Erm, Danny..."
    bree.say "What's down here?"
    bree.say "Is it some kind of new, cool bar?"
    bree.say "You know, one that's hidden away and a well-kept secret?"
    show danny normal at stepback(0.1, 3,0)
    pause 0.3
    show danny normal at stepback(0.1, 3,0)
    pause 0.3
    "Danny shakes his head and chuckles as I ask the question."
    show danny shout at startle(0.1, 5)
    danny.say "Oh, hell no, [hero.name]..."
    danny.say "I just got some business to take care of down here."
    danny.say "And I figure bringing you along is good for my image."
    danny.say "That you add a bit of glamour, you know?"
    show danny joke
    pause 0.2
    show danny at startle(0.1, 5)
    show bg alley at startle(0.1, 5)
    if hero.morality >= 25:
        bree.say "That...that doesn't sound very romantic."
        bree.say "In fact, it sounds more than a little scary!"
    elif hero.morality <= -25:
        bree.say "I can think of fun business to conduct down an alleyway."
        bree.say "But I don't think you mean the romantic kind!"
    else:
        bree.say "I can guess the kind of business you mean."
        bree.say "And it's not sounding very romantic!"
    show danny shout at startle(0.1, 5)
    danny.say "Ah, relax, [hero.name]..."
    danny.say "Think of this as romance 'Danny Style'!"
    show danny normal
    menu:
        "Agree to accompany Danny to his business meeting":
            "I know how dodgy all of this sounds."
            "And I'm aware of just how dangerous it could be too."
            "Meeting some stranger down a dark alley-way."
            "It has to be something that could land us both in serious trouble."
            "But the problem is that I'm already kind of addicted to the excitement of it all."
            "The thrill of danger that being a part of Danny's life offers me."
            "Part of me wants to say no and turn away."
            "But that's not the part of me that speaks up."
            show danny at startle(0.1, 5)
            show bg alley at startle(0.1, 5)
            if hero.morality >= 25:
                bree.say "Erm...okay, Danny..."
                bree.say "If you're sure it'll be okay?"
            elif hero.morality <= -25:
                bree.say "Sure thing, Danny, you got it."
                bree.say "But you'd better make it worth my while!"
            else:
                bree.say "Okay, Danny, I'm cool with it."
                bree.say "But don't make a habit out of this, yeah?"
            show danny joke at startle
            pause 0.4
            show bg alley at traveling(1.3, 1, (640, 720))
            "Danny gives me a wolfish grin as he walk further down the alley-way."
            show ryan at blacker, left, zoomAt(0.8, (50, 720)) with dissolve
            "And then he stops as a shadowy figure steps out from behind a dumpster."
            show danny shout at startle(0.1, 5)
            danny.say "Wait here, okay..."
            danny.say "This won't take long."
            show ryan at blacker, traveling(0.8, 1, (0, 720))
            show danny normal at traveling(0.9, 1, (100, 750))
            "Danny walks the rest of the way over to the mysterious figure."
            "And as he's standing in front of them, I can't make out much."
            "Only the occasional sight of them stealing a glance in my direction over Danny's shoulder."
            "But whenever that happens, I can feel their gaze upon me, like it's a physical sensation."
            "And though it's not the most pleasant of things, it does give me a genuine thrill all the same."
            show danny at startle(0.1, 5)
            "Danny pulls something out of his pocket and shows it to the stranger."
            show danny at startle(0.1, 5)
            "And the guy seems pleased with what he's seeing, as he accepts it a moment later."
            show danny smile at startle(0.1, 5)
            "Then he pulls out something else and hands it to Danny."
            show ryan at blacker, traveling(0.8, 0.4, (-200, 720))
            show danny smile at traveling(1.1, 1, (640, 750))
            "The next thing I know, he steps back into the shadows and Danny returns to my side."
            show danny shout at startle(0.1, 5)
            danny.say "Another satisfied customer!"
            danny.say "Well done, [hero.name]..."
            danny.say "He was so busy staring at you, he never knew I was cheating his ass!"
            show danny joke at vshake
            pause 0.5
            show danny at traveling(1.2, 0.8, (640, 800))
            "Danny lets out a barking laugh as I take his arm again."
            show bg street with dissolve
            "And then he leads me back out of the alley-way."
            "All the time causing me a strange mixture of emotions."
            "Like I feel at once filthy and exhilarated."
            "Scared of what I was just a part of."
            "Yet hoping for the chance to do it all over again."
            $ hero.morality -= 3
            $ danny.love += 3
        "Refuse to accompany Danny to his business meeting":
            "Before now I was more than a little intrigued to see where this was going."
            "Hoping that Danny had something exciting and mysterious planned for me."
            "But the idea of him dragging me along on one of his dodgy dealings..."
            "Well, it's just too much for me to take."
            "So digging my heels in and forcing him to stop, I pull away."
            show danny at traveling (1, 0.5, (640, 750))
            show bg alley at traveling (1, 0.5, (640, 720))
            pause 0.3
            show danny annoyed at startle(0.1, 5)
            show bg alley at startle(0.1, 5)
            if hero.morality >= 25:
                bree.say "Are you out of your mind?"
                bree.say "There's no way I'm getting involved in something illegal."
            elif hero.morality <= -25:
                bree.say "Okay, Danny, I get the impression this isn't about anything raunchy."
                bree.say "And I'm not into doing the straight-up illegal stuff with you."
            else:
                bree.say "Look, Danny, I like it when we do the rebellious stuff together."
                bree.say "But I'm not getting in on the really bad stuff."
            "Danny turns to face me, looking less than impressed."
            show danny shout at startle(0.1, 5)
            danny.say "Ah, quit being such a stuck-up bitch, [hero.name]."
            danny.say "I need you to smile and look pretty while I conduct my business."
            danny.say "If you can't do that, you're no use to me!"
            show danny psycho
            show danny at startle(0.1, 5)
            show bg alley at startle(0.1, 5)
            bree.say "Well if that's how you see me, Danny..."
            bree.say "I'm happy to disappoint you!"
            show danny angry with dissolve
            "With that I turn my back on Danny and walk away."
            "Leaving him standing alone in the empty alley-way."
            $ hero.morality += 3
            $ danny.love -= 3
    return


label danny_birthday_date_female:
    $ DONE["danny_birthday_date_female"] = game.days_played
    $ game.active_date.clothes = "date"
    scene bg street with fade
    "It took me a hell of a lot of coaxing to get the date of Danny's birthday out of him."
    "I don't think he liked the idea of me knowing exactly how old he actually is."
    "I guess he sees it as being at odds with his whole tough guy persona, or something like that."
    "But after a good amount of badgering on my part, he finally gave up and told me the date."
    "Or I suppose he could have just made it up."
    "But let's not worry about that possibility."
    "Because the date he gave me is today, and I'm taking him out on a date to celebrate!"
    "At least I should be."
    scene bg door restaurant with fade
    "Right now I'm standing outside the restaurant where I booked us a table."
    "And it's a good fifteen minutes after the time that I told Danny to be here for."
    "But he's nowhere to be seen!"
    "Did he forget the time and place?"
    "Or even the actual day we were supposed to be doing this on?"
    "I'm trying to keep myself calm and not assume that I've been stood up."
    "And my phone is in my hand, ready to call him."
    show danny date at center, zoomAt (0.9, (640, 740)) with dissolve
    "But at that very moment I catch sight of Danny."
    show danny at center, traveling(1.50, 3, (640, 1040))
    "He's walking down the street towards me, with that usual swagger of his."
    "And from the look on his face, he doesn't seem to have a care in the world!"
    danny.say "Hey, sweet-cheeks!"
    danny.say "You're looking particularly fine tonight!"
    danny.say "So..."
    danny.say "Are you ready for our date?"
    "I can't believe he's being so casual about this!"
    "We're already late for the reservation."
    "And he's not offered me a single word of apology or explanation!"
    menu:
        "Hide my annoyance":
            "My instinct is to tell Danny off for the way he's behaving."
            "But then I remember that it is his birthday we're celebrating."
            "And he's definitely not the type that's used to fancy restaurant dining."
            "So maybe I need to cut him some slack?"
            bree.say "We're running a little late."
            bree.say "So let's get inside already."
            bree.say "Maybe they'll have held the table for us."
            "Danny listens intently to all that I have to say."
            "And he nods a couple of times too."
            "Though I'm convinced he's not sure what I'm talking about."
            $ game.active_date.score += 20
            show danny smile
            danny.say "Yeah, [hero.name]..."
            danny.say "Sounds good to me, real good!"
            danny.say "So long as they got beer and a burger, I'm in heaven!"
        "Tell Danny off for being late":
            "I can't let him get away with this."
            "Danny needs to know that he's out of order."
            bree.say "I've been ready for the past twenty minutes, Danny!"
            bree.say "That was the time I told you to get here for, remember?"
            "Danny lets out a laugh and shakes his head."
            "But then he sees the look on my face."
            "And he seems to finally realise that I'm serious."
            $ game.active_date.score -= 10
            show danny annoyed
            danny.say "Geez..."
            danny.say "Lighten up a little, [hero.name]!"
            danny.say "I can't have fun if you're acting all serious."
            danny.say "So pull that pole out of your ass already!"
            bree.say "Whatever, Danny..."
            bree.say "Let's just get inside."
            bree.say "If we're lucky, they won't have given our table away."
    scene bg restaurant with fade
    "The moment we get inside the place, I walk up to the waiter."
    bree.say "We have a reservation?"
    bree.say "Sorry, but we're running a little late."
    "Waiter" "Oh course, madam..."
    "Waiter" "You are in luck."
    "Waiter" "We still have your table for you."
    "Waiter" "This way please..."
    "I make to follow, but then I realise Danny's not at my side."
    show danny date at center, zoomAt (1, (1200, 740)) with dissolve
    "Looking around, I'm surprised to see him skulking in the doorway."
    bree.say "Come on, Danny..."
    bree.say "The table's this way."
    danny.say "I...I dunno, [hero.name]."
    danny.say "You said this place was fancy."
    danny.say "But I didn't think it was this fancy!"
    bree.say "Danny..."
    bree.say "Are you actually scared of this place?"
    show danny at startle
    danny.say "WHAT?!?"
    show danny at mostright5 with ease
    danny.say "Don't talk crazy, [hero.name]!"
    danny.say "I just..."
    show danny at right with ease
    danny.say "I just feel like everyone's staring at me, that's all."
    menu:
        "Reassure Danny":
            "I smile at Danny and take hold of his hand."
            bree.say "That's because you're a big, scary tough guy!"
            bree.say "They're staring at you because they're scared, Danny!"
            "Danny looks around the restaurant as I say this."
            danny.say "You sure, [hero.name]?"
            danny.say "You think that's really it?"
            bree.say "I'm sure of it."
            scene bg black
            show restaurant meal danny nomeals with fade
            "Danny nods and allows me to steer him towards the table."
            "We sit down and I make a point of trying to hold his attention."
            "I figure that if he's looking at me, he won't see who's looking at him."
            "But then a woman at the next table happens to make eye-contact with Danny."
            "As soon as it happens, she jumps in her seat and looks away again."
            bree.say "You see, Danny?"
            bree.say "Scared out of their wits!"
            show restaurant meal danny date dannyhappy
            "Danny nods and smiles, seeming to cheer-up a little."
            $ game.active_date.score += 20
            danny.say "HA!"
            danny.say "You're right, [hero.name]."
            danny.say "I must look pretty bad-ass sitting here."
            show restaurant meal danny date -dannyhappy
        "Tell Danny to man-up":
            "I look at Danny in sheer amazement."
            bree.say "I thought you were a real tough guy, Danny?"
            bree.say "You know, a dangerous type from the mean streets?"
            bree.say "Now you tell me you're scared of people looking at you?"
            "Danny actually looks embarrassed as I tell him off."
            "He shakes his head and hold up his hands."
            "But now he's backing away from me too!"
            $ game.active_date.score -= 10
            show danny annoyed
            show fx exclamation at right
            danny.say "No, [hero.name]!"
            danny.say "That's not it at all."
            show danny normal
            danny.say "I just...I might have mugged someone in here in the past."
            danny.say "And if they recognise me, then I'm screwed!"
            show danny at center with ease
            "I grab hold of Danny's wrist and haul him towards the table."
            "And much to my surprise, he lets me do it!"
            bree.say "Don't be stupid, Danny."
            bree.say "This is a restaurant, not a police line-up!"
            bree.say "If anyone recognises you, they're going to be scared shitless!"
            scene bg black
            show restaurant meal danny nomeals with fade
            "Danny allows me to push him down into his seat."
            "But he's still glancing around nervously all the same."
    show restaurant_meal_waiter_pose01 as waiter zorder 1 with easeinleft
    if hero.knowledge >= 20:
        "Despite my reassurances, Danny still seems a little nervous."
        "So when the waiter comes over to take our orders, I ask him straight out."
        bree.say "Excuse me..."
        bree.say "Does this place have a dress-code?"
        show restaurant meal danny date dannyembarrassed
        danny.say "[hero.name]!"
        show fx drop at right
        danny.say "What are you doing?!?"
        bree.say "Leave it to me, Danny..."
        bree.say "I know what I'm doing!"
        show restaurant meal danny date -dannyembarrassed
        "Waiter" "Well..."
        "Waiter" "Not as such."
        "Waiter" "But we do reserve the right to eject those whom we find to be..."
        "Waiter" "Shall we say, unsuitably dressed?"
        if hero.knowledge >= 40:
            bree.say "But you don't state that anywhere in the restaurant?"
            bree.say "And it's not in any of your branding either?"
            "The waiter's expression becomes a little pained at this."
            show restaurant_meal_waiter_pose01 as waiter zorder 1 at stepback(0.1, 10, 0)
            "Waiter" "No, madam..."
            show restaurant_meal_waiter_pose01 as waiter zorder 1 at stepback(0.1, -10, 0)
            "Waiter" "But..."
            "I hold up a hand, silencing him."
            bree.say "Take my companion here."
            bree.say "His clothes are clean and in good repair."
            bree.say "So would you eject him just based on their style?"
            "Waiter" "We have in the past, madam."
            bree.say "Yet you choose not to make potential customers aware of that?"
            bree.say "Hmm..."
            bree.say "That sounds very much like discrimination to me."
            bree.say "Based on nothing more than choice of clothing."
            "Waiter" "I..."
            show restaurant_meal_waiter_pose01 as waiter zorder 1 at stepback(0.1, 10, 0)
            "Waiter" "Wait a minute..."
            show restaurant_meal_waiter_pose01 as waiter zorder 1 at stepback(0.1, -10, 0)
            "Waiter" "I suppose it does!"
            bree.say "That would look very bad for the place."
            bree.say "Don't you think?"
            "I lean over to Danny and whisper so as not to let the waiter hear."
            bree.say "Don't worry about it, Danny."
            bree.say "They're going to be too scared to even think about kicking you out now!"
            $ game.active_date.score += 15
        else:
            bree.say "Erm..."
            bree.say "Right..."
            bree.say "That does sound like they could kick you out, Danny!"
            bree.say "So you'd better be on your best behaviour!"
            "The waiter nods and makes a sniffy sound."
            "This makes Danny lean in close and hiss into my ear."
            show restaurant meal danny date dannybored
            danny.say "What in the hell was that about?"
            danny.say "Are you trying to get them to throw me out or something?!?"
            bree.say "Sorry!"
            bree.say "I thought that I could argue my way around it."
            bree.say "Look, let's just order and be nice, okay?"
            "Danny shoots me a withering look."
            "And then we come out of our huddle."
            "Both with fake smiles on our faces."
            show restaurant meal danny date -dannybored
            $ game.active_date.score -= 5
    "The waiter holds up his notepad, signalling that he's ready to begin."
    show restaurant_meal_waiter_pose01 as waiter zorder 1 at stepback(0.1, 10, 0)
    "Waiter" "Can I get you anything to drink?"
    "At the mere mention of alcohol, Danny perks up."
    "And a huge, genuine grin spreads across his face."
    danny.say "Oh yeah!"
    danny.say "Now you're talking my language!"
    danny.say "I gotta get a beer before I die of thirst!"
    "The waiter raises his eyebrows at this."
    "And then he looks at me with a loaded expression."
    "Danny seems to pick up on the fact that there's something wrong."
    "But it's obvious that he has no reason what it is."
    danny.say "Huh?"
    danny.say "What's wrong?"
    danny.say "Don't they serve booze in this place?"
    menu:
        "Back Danny up":
            bree.say "Of course they serve alcohol, Danny."
            bree.say "It's just that most people aren't confident enough to order beer."
            bree.say "And so they get really snobby about it when people do!"
            "Danny looks at me in amazement."
            danny.say "Huh?"
            show restaurant meal danny date dannyhappy
            danny.say "You gotta be fucking with me!"
            bree.say "Uh-uh..."
            bree.say "Waiter..."
            bree.say "You have beer, right?"
            "The waiter looks unsure of himself."
            "My revelation to Danny seems to have thrown him off."
            show restaurant meal danny date -dannyhappy
            show restaurant_meal_waiter_pose01 as waiter zorder 1 at stepback(0.1, 10, 0)
            "Waiter" "Y...yes, of course..."
            show restaurant_meal_waiter_pose01 as waiter zorder 1 at stepback(0.1, -10, 0)
            "Waiter" "But..."
            "I cut him off before he can answer."
            bree.say "Did I ask you for your opinion?"
            bree.say "I don't think so."
            bree.say "So just go get our drinks."
            bree.say "Then come back and take our food orders."
            "Waiter" "Y...yes, madam."
            hide restaurant_meal_waiter_pose01 as waiter zorder 1 with easeoutleft
            "The waiter hurries off to do as he's told."
            show restaurant meal danny date dannyhappy
            "And Danny looks at me with renewed respect."
            danny.say "Whoa..."
            danny.say "You really showed him!"
            show restaurant meal danny date -dannyhappy
            bree.say "It's nothing really."
            bree.say "You just have to know how to talk to these people."
            $ game.active_date.score += 20
        "Say Danny he should drink wine instead":
            bree.say "Of course they serve alcohol, Danny."
            bree.say "It's just that most people aren't uncouth enough to order beer!"
            "Danny looks amazed at this revelation."
            show restaurant meal danny date dannyembarrassed
            danny.say "You're serious?"
            danny.say "Then what in the hell do they drink?"
            danny.say "You can't go straight to whiskey from beer!"
            "I shoot Danny a disapproving look."
            show restaurant meal danny date dannybored -dannyembarrassed
            bree.say "They drink wine, you oaf!"
            bree.say "And they savour the taste too."
            bree.say "They don't swig it back like you do with beer!"
            "Danny rolls his eyes and mutters under his breath."
            "I don't hear what he's actually saying."
            "But maybe that's for the best."
            danny.say "Urgh..."
            danny.say "Order damn wine then!"
            danny.say "Anything to get you off my back..."
            hide restaurant_meal_waiter_pose01 as waiter zorder 1 with easeoutleft
            show restaurant meal danny date -dannybored
            $ game.active_date.score -= 10
    show restaurant meal danny date dannysad
    show restaurant meal danny date order with dissolve
    "Danny seems to be studying the menu very intently."
    "Almost like it was the instructions to assemble a particle accelerator."
    "And the ones that he's been given are also in Japanese!"
    bree.say "What's the problem, Danny?"
    bree.say "Don't see anything you like on there?"
    danny.say "Huh?"
    danny.say "Oh no, [hero.name]..."
    show restaurant meal danny date dannybored -dannysad
    danny.say "I see lots of stuff, just nothing I can make sense of..."
    show fx drop at right
    danny.say "It's all foreign or something!"
    "I frown and look down at my menu."
    "Sure, the language is a bit fancy and flowery."
    "But it's still written in intelligible English."
    menu:
        "Help Danny to order":
            "I shake my head and smile at Danny."
            bree.say "I know it's a little weird."
            bree.say "You just have to know what kind of terms they use, that's all."
            show restaurant meal danny date dannyembarrassed -dannybored
            bree.say "It's kind of a mixture of English and French."
            "If anything, this seems to make Danny more confused."
            danny.say "But I don't speak French!"
            danny.say "I'm a normal kind of guy!"
            "I can't help giggling at Danny's distress."
            "But all the same I do what I can to help him."
            show restaurant meal danny date -dannyembarrassed
            bree.say "Okay, Danny..."
            bree.say "What kind of thing would you like to order?"
            "Danny shrugs and seems to think about it for a second."
            danny.say "Erm..."
            danny.say "I could go for a steak right about now?"
            bree.say "Okay..."
            bree.say "That's a steak, right there."
            danny.say "It is?"
            bree.say "Just order that, okay?"
            show restaurant meal danny date dannyhappy
            danny.say "Thanks, [hero.name]..."
            danny.say "You really helped me out there!"
            show restaurant meal danny date -dannyhappy
            $ game.active_date.score += 20
        "Shame Danny for not being able to order":
            "I frown and shake my head at Danny."
            bree.say "Really, Danny!"
            bree.say "The menu is in plain English."
            bree.say "What more do you want?"
            show restaurant meal danny date dannysad -dannybored
            "Danny looks at me with a helpless expression on his face."
            "Which is pretty different from his usual bad-ass one."
            danny.say "But, [hero.name]..."
            danny.say "I dunno what any of this stuff is!"
            bree.say "For god's sake, Danny..."
            bree.say "That's a steak, right there."
            "I jab my finger at the appropriate dish."
            "Danny nods and cringes in his seat."
            "Clearly embarrassed to need my help."
            show restaurant meal danny date -dannysad
            $ game.active_date.score -= 10
    show restaurant_meal_waiter_pose01 as waiter zorder 1 with easeinleft
    show restaurant meal danny date -order with dissolve
    "Pretty soon we've ordered our food and it's arrived."
    show restaurant meal danny date -nomeals with fade
    hide restaurant_meal_waiter_pose01 as waiter zorder 1 with easeoutleft
    "Everything looks really appetising to me, and I can't wait to get started."
    show restaurant meal danny date dannysad
    "But I can see that Danny's looking more than a little worried about his meal."
    "I guess it's way fancier than what he's used to."
    "But all the same, he picks up his knife and fork."
    "And he does the best he can to tuck into his steak."
    if hero.charm >= 20:
        show restaurant meal danny date dannybored dannyembarrassed -dannysad
        danny.say "Eurgh!"
        danny.say "Ah man..."
        show fx anger at right
        danny.say "What the fuck!"
        "I look up as Danny cries out in surprise."
        "But I can't tell what's making him freak out."
        bree.say "What's the matter, Danny?"
        bree.say "Doesn't it taste good?"
        "Danny holds up a forkful of steak."
        "And I can see that it's glistening red in the light."
        danny.say "It's fucking raw, [hero.name]!"
        danny.say "They didn't cook this shit right!"
        if hero.charm >= 40:
            bree.say "Oh yeah, Danny..."
            bree.say "It's called medium-rare."
            bree.say "They do that kind of thing in places like this!"
            danny.say "Urgh..."
            danny.say "I can't eat this!"
            bree.say "Don't worry."
            bree.say "I'll handle it..."
            show restaurant meal danny date -dannysad
            "I turn and wave the waiter over."
            show fx question at right
            show restaurant meal danny date dannyembarrassed
            danny.say "[hero.name], what are you doing?!?"
            show restaurant_meal_waiter_pose01 as waiter zorder 1 with easeinleft
            "Waiter" "Yes, madam?"
            show restaurant_meal_waiter_pose01 as waiter zorder 1 at stepback(0.1, -5, 0)
            "Waiter" "Is there something I can help you with?"
            "I smile and point to Danny's steak."
            bree.say "My friend's steak is medium-rare."
            bree.say "And he'd prefer it well-done, please."
            "Waiter" "Well, that's hardly our problem, madam."
            show restaurant_meal_waiter_pose01 as waiter zorder 1 at stepback(0.1, 5, 0)
            "Waiter" "We can't be held accountable for a diner's ignorance."
            "I raise an eyebrow at this."
            bree.say "Oh really?"
            bree.say "I think you'll find that my friend wasn't asked his preference."
            bree.say "Which means it was your mistake, not his."
            "The expression on the waiter's face changes as he realises that I'm right."
            "Waiter" "Oh..."
            show restaurant_meal_waiter_pose01 as waiter zorder 1 at stepback(0.1, -5, 0)
            "Waiter" "Of course..."
            "Waiter" "Let me take care of that for you."
            show restaurant_meal_waiter_pose01 as waiter zorder 1 at stepback(0.1, 10, 0)
            "Waiter" "And my apologies..."
            show restaurant meal danny nomeals with dissolve
            hide restaurant_meal_waiter_pose01 as waiter zorder 1 with easeoutleft
            "The waiter scoops up the plate and hurries away."
            show restaurant meal danny date dannyhappy -dannyembarrassed
            "And Danny stares at me in amazement."
            danny.say "Huh!"
            danny.say "You sure told him, [hero.name]!"
            show restaurant_meal_waiter_pose01 as waiter zorder 1 with easeinleft
            show restaurant meal danny date -nomeals with dissolve
            hide restaurant_meal_waiter_pose01 as waiter zorder 1 with easeoutleft
            "Soon after the food is back."
            show restaurant meal danny date -dannyhappy
            $ game.active_date.score += 15
        else:
            bree.say "Oh for god's sake, Danny!"
            bree.say "It's cooked medium rare, that's all!"
            "I roll my eyes and make a point of laughing."
            "And at the same time, I wave the waiter over."
            show restaurant meal danny date dannybored -dannyembarrassed
            danny.say "Urgh..."
            danny.say "[hero.name], what are you doing?!?"
            show restaurant_meal_waiter_pose01 as waiter zorder 1 with easeinleft
            "Waiter" "Yes, madam?"
            show restaurant_meal_waiter_pose01 as waiter zorder 1 at stepback(0.1, -5, 0)
            "Waiter" "Is there something I can help you with?"
            "I smile and point to Danny's steak."
            bree.say "My friend here doesn't understand cooking a steak rare."
            bree.say "So would you take it back and cook it until it's well-done?"
            show restaurant_meal_waiter_pose01 as waiter zorder 1 at stepback(0.1, 5, 0)
            "Waiter" "Well, that's hardly our problem, madam."
            show restaurant_meal_waiter_pose01 as waiter zorder 1 at stepback(0.1, 10, 0)
            "Waiter" "We can't be held accountable for a diner's ignorance."
            "Waiter" "Pardon me while I get this burnt to charcoal blocks."
            hide restaurant_meal_waiter_pose01 as waiter zorder 1 with easeoutleft
            "With that, the waiter turns on his heel and walks away."
            show restaurant meal danny date dannysad -dannybored -dannyembarrassed
            danny.say "[hero.name]!"
            danny.say "You made me look like an ass!"
            show restaurant meal danny date -dannysad
            $ game.active_date.score -= 5
    show restaurant meal danny date dannybored dannyembarrassed -dannysad
    danny.say "Urngh..."
    danny.say "Oh man..."
    "I look up from my food at the sounds Danny's making."
    "And I'm surprised to see him hacking away at his steak."
    bree.say "What's the matter, Danny?"
    bree.say "Is your steak a little too tough?"
    danny.say "Nah, [hero.name]..."
    show fx anger at right
    danny.say "I think the cutlery is fucking blunt!"
    "Danny stops what he's doing, holding up the utensils in his hands."
    "And I can instantly see the problem."
    "He's trying to cut his steak with a fish knife!"
    menu:
        "Explain cutlery to Danny":
            bree.say "That's a fish knife, Danny."
            bree.say "It's not meant to cut steak!"
            "Danny stares a the knife in surprise."
            "And she shakes his head."
            show restaurant meal danny date -dannybored
            danny.say "What the fuck?"
            danny.say "I ordered steak, not fish."
            danny.say "Why'd they give me this thing?"
            bree.say "They put all the cutlery out."
            bree.say "And they assume you'll know what's for what."
            "Danny frowns and puts the knife down."
            danny.say "Are they trying to make me look stupid, or what?"
            bree.say "It's okay, Danny..."
            bree.say "I'll explain it to you."
            bree.say "You have to start from the outside and work in..."
            "I give Danny a quick crash-course in cutlery etiquette."
            show restaurant meal danny date dannyhappy -dannyembarrassed
            "And afterwards he seems to be more confident."
            danny.say "Geez, [hero.name]..."
            danny.say "Why don't they tell you this shit before you eat?"
            danny.say "Lucky for me I have you to explain it all."
            show restaurant meal danny nomeals with dissolve
            show restaurant meal danny date -dannyhappy
            $ game.active_date.score += 20
        "Highlight Danny's incompetence":
            bree.say "Danny, you dumb-ass!"
            bree.say "That's a fish knife!"
            "Danny stares a the knife in surprise."
            "And she shakes his head."
            show restaurant meal danny date -dannybored
            danny.say "What the fuck?"
            danny.say "I ordered steak, not fish."
            danny.say "Why'd they give me this thing?"
            bree.say "They put all the cutlery out."
            bree.say "You just need to know what's for what."
            bree.say "You want me to..."
            "Danny shoots me a frown."
            "Then he shakes his head a second time."
            danny.say "What, so you can make me look dumb again?"
            danny.say "No way, [hero.name]."
            show fx anger at right
            danny.say "I'll manage!"
            "And with that, Danny goes back to his meal."
            "Grunting and swearing as he hacks away with his fish knife."
            show restaurant meal danny date -dannyembarrassed
            show restaurant meal danny nomeals with dissolve
            $ game.active_date.score -= 10
    "Once we're done eating, Danny and I have the chance to chat."
    "He keeps it pretty generic in terms of subject."
    "But I get the feeling he's trying to move the conversation in a specific direction."
    danny.say "So..."
    danny.say "You got a little something for me?"
    danny.say "Huh, [hero.name]?"
    if not hero.has_gifts:
        "I suddenly realise that Danny's fishing for a birthday gift."
        "Which is kind of a problem - because I didn't get him one!"
        "I'm just going to have to play it dumb and hope for the best."
        bree.say "You mean a birthday present?"
        show restaurant meal danny date dannyhappy
        danny.say "I sure do, [hero.name]!"
        danny.say "So gimmie what you got for me!"
        bree.say "Well..."
        bree.say "This date IS your present, Danny!"
        show restaurant meal danny date -dannyhappy
        danny.say "Whu...whadda ya mean?"
        bree.say "The gift of being exposed to new experiences, yeah?"
        bree.say "The chance to broaden your horizons!"
        show restaurant meal danny date dannybored
        show fx drop at right
        danny.say "Urgh..."
        danny.say "You're serious, aren't you?"
        bree.say "I sure am!"
        danny.say "Ah shit!"
        $ game.active_date.score -= 20
        show restaurant meal danny date -dannybored
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift_19
        if _return != "done":
            if _return not in ["None", "exit"]:
                "What better time to produce the gift that I have for Danny?"
                "So I whip it out and hand it over, much to his evident delight."
                bree.say "Happy birthday, Danny!"
                danny.say "Ah yeah..."
                danny.say "This is more like it!"
                danny.say "Gimmie that thing..."
                play sound [paper_ripping_1, paper_ripping_2]
                "Danny eagerly tears into the wrapping paper and opens the box inside."
                if _return:
                    show restaurant meal danny date dannyhappy
                    "But as soon as he sees what's inside, Danny's face lights up."
                    danny.say "Oh my god!"
                    danny.say "Oh my fucking Christ!"
                    bree.say "Erm..."
                    bree.say "What's the matter, Danny?"
                    danny.say "This gift, [hero.name]..."
                    danny.say "It's goddamn amazing!"
                    $ game.active_date.score += 20
                    bree.say "It is?"
                    danny.say "You bet it is!"
                    show restaurant meal danny date dannyblush -dannyhappy
                    danny.say "This is like, probably the best gift I ever got!"
                    danny.say "At least the best that I didn't have to steal myself..."
                    show restaurant meal danny date dannyhappy -dannyblush
                    bree.say "Th...thanks, Danny!"
                    bree.say "I think..."
                    show restaurant meal danny date -dannyhappy
                else:
                    "But as soon as he sees what's inside, Danny's face falls."
                    bree.say "Erm..."
                    bree.say "What's the matter, Danny?"
                    show restaurant meal danny date dannybored
                    danny.say "This gift, [hero.name]..."
                    show fx drop at right
                    danny.say "It's kinda lame!"
                    bree.say "It is?"
                    danny.say "Yeah, it really sucks."
                    bree.say "Well thanks for telling me that, Danny."
                    bree.say "Otherwise I might have thought you liked it!"
                    danny.say "No worries, [hero.name]."
                    show restaurant meal danny date -dannybored
                    $ game.active_date.score -= 10
            else:
                "I suddenly realise that Danny's fishing for a birthday gift."
                "Which is kind of a problem - because I didn't get him one!"
                "I'm just going to have to play it dumb and hope for the best."
                bree.say "You mean a birthday present?"
                show restaurant meal danny date dannyhappy
                danny.say "I sure do, [hero.name]!"
                danny.say "So gimmie what you got for me!"
                bree.say "Well..."
                bree.say "This date IS your present, Danny!"
                show restaurant meal danny date -dannyhappy
                danny.say "Whu...whadda ya mean?"
                bree.say "The gift of being exposed to new experiences, yeah?"
                bree.say "The chance to broaden your horizons!"
                show restaurant meal danny date dannybored
                show fx drop at right
                danny.say "Urgh..."
                danny.say "You're serious, aren't you?"
                bree.say "I sure am!"
                danny.say "Ah shit!"
                $ game.active_date.score -= 20
                show restaurant meal danny date -dannybored
    "The meal comes to an end and I ask for the bill."
    show restaurant_meal_waiter_pose02 as waiter zorder 1 with easeinright
    "Noting at the same time Danny making no attempt to split it with me."
    show restaurant meal danny date pay
    "Ah well, I guess I did promise to take him out for his birthday."
    show restaurant meal danny date -pay
    hide restaurant_meal_waiter_pose02 as waiter zorder 1 with easeoutright
    "The staff seem more than keen to usher him out of the door."
    scene bg street
    show danny date at center, zoomAt (1.5, (640, 1040))
    with fade
    "And so we soon find ourselves standing on the pavement outside."
    bree.say "I had a nice time tonight, Danny."
    bree.say "Are you ready to go home yet?"
    bree.say "Because I could stay out a little longer..."
    if game.active_date.score >= 100:
        show danny date smile at hshake
        danny.say "Hell yeah!"
        danny.say "The night isn't over yet, sweet-cheeks!"
        danny.say "We need to keep right on partying."
        danny.say "And I know just the place!"
        bree.say "You do?"
        danny.say "Oh yeah!"
        danny.say "It's a private little place."
        danny.say "Even has its own pool!"
        "I can't believe what I'm hearing."
        "Part of me was expecting Danny to offer me a grope down a back-alley."
        "Or at the most a trip with him to the nearest strip-club."
        "Maybe there is a more romantic side to him after all?"
        bree.say "What are we waiting for?"
        bree.say "Let's go!"
        call danny_birthday_sex_female from _call_danny_birthday_sex_female
    else:
        show danny date upset
        danny.say "Nah..."
        danny.say "I'm good, [hero.name]."
        bree.say "Oh..."
        bree.say "Are you sure?"
        danny.say "Yeah, yeah..."
        danny.say "I ate and drank a hell of a lot tonight."
        danny.say "So I'm gonna need to let all of that out."
        show danny date angry
        danny.say "If you know what I mean?"
        "I nod as a mental image fills my mind."
        "One that I have no desire to see become a reality."
        show danny date upset
        bree.say "Okay, Danny..."
        bree.say "See you soon, I guess?"
        show danny date sneaky
        danny.say "If you're lucky!"
        "With that, Danny turns on his heel and walks away down the street."
        hide danny date with dissolve
        "Leaving me to watch him disappear from sight."
    return

label danny_birthday_sex_female:
    scene bg trailer
    "I honestly don't know what I was expecting from Danny."
    show danny date smile at center, zoomAt(1.0, (-220, 740))
    show danny at center, zoomAt(1.0, (640, 740)) with ease
    "When he said he knew a private little place, I think I got carried away."
    "I was expecting some apartment that he'd got hidden away."
    "Maybe even a cabin in the woods where he hid out when the heat was on."
    "But I definitely wasn't expecting him to take me to a trailer park!"
    show danny at startle
    danny.say "Ta da!"
    danny.say "Wadda ya think, sweet-cheeks?"
    "Danny's pointing at a particularly scummy-looking trailer."
    "One that I could easily have believed was totally abandoned."
    bree.say "This is it?!?"
    bree.say "This is where we're going?"
    danny.say "It's just like I said, [hero.name]..."
    danny.say "A little place out of the way."
    show danny at stepback(0.1, -10, 0)
    danny.say "Even has it's own pool, see?"
    bree.say "Are you kidding?"
    bree.say "That's an inflatable paddling pool!"
    "Danny rolls his eyes and waves away my protests."
    scene bg trailerinside with fade
    "Then he pushes the door of the trailer open and walks inside."
    "Realising that I can either stand there or follow him, I choose the latter."
    "And once I'm inside too, I see that it's not as bad as I'd expected."
    "I mean sure, it's pretty low-rent - but at least it's clean."
    show danny date smile with dissolve
    danny.say "You can't look a gift horse in the mouth, [hero.name]."
    danny.say "I know the broad that lives here pretty well."
    danny.say "And she's not the kind to go running her mouth."
    danny.say "So this is a great place to kick back in private."
    bree.say "Wait a minute..."
    bree.say "Somebody actually lives here?"
    bree.say "I thought it was abandoned or something!"
    "Danny rubs the back of his neck as he looks around."
    show danny annoyed
    danny.say "Ah, yeah..."
    danny.say "I guess you have higher standards than she does, [hero.name]!"
    danny.say "But don't worry about that bitch."
    danny.say "She won't be home until long after we're gone."
    show danny normal
    "My first instinct is to tell Danny that I'm leaving."
    "That he's crazy to want to get it on in someone else's trailer."
    "But then I start to think about the girl who must live here."
    "Specifically about how exciting living like that must be."
    "And I can't keep my eyes from drifting to the bed in the corner."
    "Wondering what crazy things must have gone down on it in the past."
    bree.say "So..."
    bree.say "The girl that lives here..."
    bree.say "I bet she's pretty wild, yeah?"
    show danny smile at startle
    "Danny nods and lets out a filthy chuckle."
    danny.say "Oh, you bet!"
    danny.say "You have no idea, [hero.name]!"
    bree.say "Is that a challenge, Danny?"
    show danny surprised
    danny.say "What?"
    danny.say "No, I..."
    bree.say "You think I can't compete with her?"
    bree.say "Is that it?"
    show danny smile
    danny.say "Nah, [hero.name]..."
    danny.say "You're putting word in my mouth!"
    danny.say "It's just...you're a pretty nice girl, you know?"
    "I shrug as I walk over to the bed."
    "And I make sure that I do it in a slow, suggestive manner."
    bree.say "I think you're wrong, Danny."
    bree.say "I don't think you know how bad I can be..."
    "With that, I turn my back on him and climb onto the bed."
    "It doesn't take me long to strip off my clothes."
    "I toss them on the floor one by one."
    "And the whole time I can feel Danny's eyes on me."
    "He's staring in silence, eyes getting wider the whole time."
    "Once I'm naked, I get up on all fours."
    scene danny doggy
    show danny doggy trailer nonpc pleasure
    with fade
    "And I look back over my shoulder at him."
    bree.say "What about it, Danny?"
    bree.say "You wanna help me be bad?"
    danny.say "Urgh..."
    danny.say "Ah shit, [hero.name]..."
    danny.say "Wadda ya trying to do to me?!?"
    "Even as he's saying all of this, Danny's already stripping off."
    "And he's closing the short distance between us too."
    "Somehow he manages to get naked over those few short feet."
    "Which is a pretty impressive achievement in its own right!"
    show danny doggy trailer -nonpc
    "And by the time he reaches the bed, he's more than ready to go."
    "I only catch a brief glimpse of his cock as he leaps up behind me."
    "But like the rest of him, it looks excited, hard and ready for business!"
    "I can't help letting out a little yelp as I feel him grab hold of me."
    "Danny's hands are large and rough, taking a firm grip."
    "But I keep telling myself that this is what I wanted."
    "This is what I was trying to goad him into doing."
    "I just hope that I can handle what I'm asking for!"
    "Suddenly there doesn't seem to be room for thinking anymore."
    "Because I feel the sensation of something between my legs."
    "At first I think it must be Danny's cock."
    "But then I feel myself being touched in more than one place."
    "It's one of his hands!"
    "I shudder as Danny strokes and caresses me down there."
    "His fingertips trace the lines of my lips, exploring the folds."
    "And every movement makes me looser and wetter than the last."
    "My head nods without any conscious thought."
    "Because he seems to know exactly what he's doing down there."
    "In what feels like no time at all, I know that my body's surrendering to him."
    "Part of me expects Danny to push further, to put his fingers inside of me."
    show danny doggy hurt rolled vaginal
    "But then my head comes up and my eyes pop open."
    "Because instead he chooses that moment to get his cock involved."
    show danny doggy pleasure
    "I gasp as I feel him pushing into me."
    "He's not taking it slowly either."
    "Danny thrusts himself into me in one go."
    "He doesn't pause or hesitate, just keeps right on going."
    show danny doggy normal
    "I can feel every inch of him entering me, parting the walls of my pussy."
    "For a moment I actually think that he might never stop."
    "But eventually he does, stopping only when he can't go any further."
    danny.say "How's that feel, [hero.name]?"
    danny.say "You like that, huh?"
    bree.say "Y...yeah..."
    bree.say "I...I like it..."
    "My panting and gasping for breath is only in part from what I'm feeling right now."
    "A lot of it is actually because of the anticipation I have for what's coming next."
    danny.say "Then let's see how you like this!"
    show danny doggy hurt rolled speed with hpunch
    "That's the only warning I get before Danny leaps into action."
    "And before I know what's happening, he's moving inside of me."
    show danny doggy speed at startle(0.05,-10)
    pause 0.2
    show danny doggy -speed
    "There's no slow build, no chance for me to get up to speed."
    "Instead Danny just kicks into high gear goes for it."
    show danny doggy speed at startle(0.05,-10)
    pause 0.2
    show danny doggy -speed
    "I can hear someone moaning and crying out in the room."
    "But it takes me a few moments to realise that it's me!"
    show danny doggy speed at startle(0.05,-10)
    pause 0.2
    show danny doggy -speed
    "Sure, Danny's grunting with the effort as he pounds away."
    "But those other sounds can only be coming from me."
    show danny doggy speed at startle(0.05,-10)
    pause 0.2
    show danny doggy -speed
    "I don't remember the last time I got fucked like this."
    "Or maybe I've never had it this hard and rough before."
    show danny doggy speed at startle(0.05,-10)
    pause 0.2
    show danny doggy -speed
    "With all that Danny's doing to me, it's hard to be sure."
    "I guess this is what I wanted."
    show danny doggy speed at startle(0.05,-10)
    pause 0.2
    show danny doggy -speed
    "To be made love to like he would with the girl that lives here."
    "If you could really call what we're doing making love, that is."
    show danny doggy speed at startle(0.05,-10)
    pause 0.2
    show danny doggy -speed
    "It kinda feels more like being humped in a mating frenzy!"
    "But the fact is that I'm taking all he can give me."
    "And I know that I want more!"
    show danny doggy down hurt with hpunch
    "Danny might be thrusting into me for all he's worth."
    "But I'm pushing back into him at the same time."
    "Arching my back to make sure the angle is just right."
    show danny doggy speed with hpunch
    pause 0.2
    show danny doggy -speed
    "I can feel the roughness of his hands."
    "And the way that his coiled muscles are working so hard."
    show danny doggy speed with hpunch
    pause 0.2
    show danny doggy -speed
    "Those aren't the kind that you get from working out at the gym either."
    "Just thinking about the fights and chases with the cops that must have built them."
    show danny doggy speed pleasure with hpunch
    pause 0.2
    show danny doggy -speed
    "Oh god..."
    "The simple thought of it sends a shudder of excitement through my entire body!"
    "I never really faced the danger that Danny embodies this honestly before now."
    show danny doggy speed with hpunch
    pause 0.2
    show danny doggy -speed
    "He's no pretend bad boy either - he's the genuine article!"
    show danny doggy speed with hpunch
    pause 0.2
    show danny doggy -speed
    bree.say "Danny..."
    bree.say "Oh fuck..."
    bree.say "I'm...I'm gonna cum!"
    danny.say "Sh...shit..."
    danny.say "I can feel it..."
    "The muscles in my pussy begin to clench and squeeze."
    "And I can hear Danny groaning as they clamp down on him."
    "He's going so fast and hard that there's no way he can pace himself."
    show danny doggy up with hpunch
    "And he begins to cum a moment later too."
    show danny doggy ahegao rolled with hpunch
    "All the same we both keep right on going until the end."
    "Keeping up the pace we've set and making the climax that much more intense."
    show danny doggy squirt creampie -speed with hpunch
    "I feel Danny explode inside of me."
    show danny doggy down rolled
    "And then everything seems to go dark as I slump onto the bed."
    "The last thing I feel is him falling down beside me like a felled tree."
    "I come round a little later, still dizzy and hazy."
    bree.say "Urgh..."
    bree.say "We made a hell of a mess, Danny!"
    bree.say "Maybe we should clean this place before your friend gets home?"
    danny.say "Nah, [hero.name]..."
    danny.say "There's no point."
    danny.say "Trust me, she won't even notice!"
    $ danny.sexperience += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
