init python:
    Activity(**{
    "name": "best_customer_service",
    "display_name": "Sasha won a contest",
    "label": "best_customer_service",
    "music": "music/roa_music/smile_for_me.ogg",
    "conditions": [
        IsDone("palla_event_03b"),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            HasRoomTag("home"),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            Not(HasCheated()),
            IsRoom("clothesshop"),
            MinStat("love", 50),
            ),
        PersonTarget(palla,
            Not(IsHidden()),
            ),
        "Person.showdown(sasha, palla)",
        ],
    "do_once": True,
    "icon": "sasha",
    })

label best_customer_service:
    "You know how it is - you're scrolling through endless posts on social media just to pass the time."
    "All you're seeing are pictures of other people's lunch and the most obvious kinds of clickbait out there."
    "But then you read something that makes you raise your eyebrows in surprise and want to read more."
    "Right now it's the name of a store at the mall that's caught my attention."
    "It's won some kind of award for customer service, but that's not what interests me."
    "What does interest me is the fact that I know the name of the store."
    "It's the one where Sasha works part-time."
    "Intrigued, I scroll down to where the article has some quotes from the people that voted for the store."
    "And my eyebrows climb even further up my forehead as I realise that most of them are praising Sasha!"
    "Someone called SecretArchangel says 'Sasha wins, not even a question!'"
    "Kisser-K is practically gushing in their praise \"Sasha's in a different class, and I think the poll will reflect that!\""
    "And John Tuggson adds 'Sasha is my favourite character, by a wide margin!'"
    "I can't help frowning a little at the last quote."
    "Do they mean they like her personality or what?"
    "I mean, it's not like Sasha's a character in a game or something."
    "What do they think, that there's some guy sitting around typing up lines for her to recite?!?"
    "But whatever - the important thing is that all of these people really like Sasha."
    "Which is only right, because she's a strong, independent woman that takes no shit!"
    "And well...she's pretty fucking hot too!"
    "Just don't tell her I said that..."
    "I finish reading the article and it leaves me feeling full of admiration for Sasha."
    "Maybe I should get off of my ass and do something to show her that I appreciate her too?"
    menu:
        "Better not interfere":
            "I glance at the time, and then I realise that Sasha's at work right now."
            "I could go down to the mall and say hi before the end of her shift."
            "But how's that going to look, especially when she's supposed to be so professional?"
            "She can't serve her customers and make a good impression if I'm distracting her."
            "I nod to myself, deciding that it's better for all concerned if I stay away."
            "And with that, I get back to the important task of scrolling through social media."
            "Which means that I forget all about Sasha and her customer service skills a few moments later."
            return
        "Praise Sasha when she gets home":
            "I glance at the time, and then I realise that Sasha's at work right now."
            "I could go down to the mall and say hi before the end of her shift."
            "But how's that going to look, especially when she's supposed to be so professional?"
            "She can't serve her customers and make a good impression if I'm distracting her."
            "It'd be far better to wait for her to get home and compliment her then."
            scene bg black with timelaps
            $ game.pass_time(1)
            show bg livingroom with timelaps
            "And so that's exactly what I do, going about my business until Sasha walks through the front door."
            show bg livingroom
            show sasha
            with dissolve
            mike.say "Hey, Sasha..."
            mike.say "Wow - you look beat!"
            "Sasha looks a little distracted at first."
            "Like her body's at home, but her head's still at work."
            "But then she seems to shake it off and gives me a tired smile."
            show sasha happy
            sasha.say "Oh...yeah, [hero.name]!"
            sasha.say "Work was super busy today."
            sasha.say "It went crazy for some reason and I was run off my feet!"
            "I smile and nod, amused at how humble Sasha's being."
            "Of course her shop was busy, it just won an award."
            "And it sounds like she was the main reason for that happening."
            mike.say "I guess everyone wanted a little bit of the Sasha experience for themselves?"
            mike.say "I mean, when I read all about it, I know I did!"
            show sasha blush
            "Sasha's cheeks instantly flush red with embarrassment."
            "But she still manages a shy smile at me bringing up the competition."
            show fx question
            sasha.say "What?!?"
            hide fx
            sasha.say "That silly competition?"
            sasha.say "You know those things don't mean anything, [hero.name]!"
            show sasha normal
            sasha.say "And anyway, the whole store won it - not just me!"
            mike.say "Not for the comments I read, Sasha!"
            mike.say "Anyway, I'm not trying to tease you about it."
            mike.say "I just wanted to congratulate you, that's all."
            mike.say "You work really hard, and it's good to see people notice that."
            show sasha happy
            "Sasha's smile becomes broader as she hears what I have to say about her."
            "But if anything, she's now blushing even more than she was to begin with!"
            sasha.say "Thanks, [hero.name]!"
            sasha.say "It's great having customers give you compliments."
            sasha.say "And I'm so lucky to have so many great people vote for me too."
            show sasha flirt
            sasha.say "Oh, and it's nice to get a compliment from you too!"
            $ sasha.love += 3
            show sasha at center, zoomAt(2, (640, 1380))
            "Sasha leans in to place a kiss on my cheek."
            "And then she hurries off to get changed out of her work things."
            hide sasha with moveoutright
            "It's only when she's gone that I get to thinking about what she just said."
            "Wait a minute...does that mean she likes the people that voted for her more than me?!?"
            "I shake my head, beginning to feel more than a little jealous!"
            return
        "Head down to the mall":
            "I glance at the time, and then I realise that Sasha's at work right now."
            "I could go down to the mall and say hi before the end of her shift."
            "That's a great idea - I can tell her how great she is in person!"
            "I'm up and out of the door no more than a few minutes later."
            show bg mall1 with fade
            "And I make it to the mall in record time too."
            "I walk up to the store where Sasha works, expecting to be greeted by crowds of shoppers."
            "After all, the place just won a competition and everyone was bigging it up online."
            show bg clothesshop with fade
            "But as I walk inside, I'm surprised to find that there's nobody around."
            "In fact the place is deserted, no customers or staff in sight!"
            "Puzzled by all of this, I make a quick circuit of the store."
            "I don't happen across anyone hiding in the corners."
            "And there's nobody crouched down behind the counter either."
            "It's only when I pass the door to the back of the store that I find any evidence of human life."
            "And that's what sounds like the raised voices of two women, yelling back a forth at each other."
            "For a moment I think about opening the door to see what the commotion's all about."
            "But the sign attached to it clearly reads 'Staff Only'."
            "So maybe that's not the best idea?"
    menu:
        "Ignore the voices":
            "Yeah, I think discretion really is the better part of valour."
            "Especially when it comes to walking in on two women fighting."
            "I mean, I'm not even supposed to go back there to begin with."
            "And are the pair of them going to do when they set eyes on me?"
            "Nothing apart from turning all of their attentions in my direction!"
            "I shake my head and turn towards the entrance of the store."
            "I can always congratulate Sasha when she gets home."
            "And that way there's no chance of me getting into trouble either."
            "So I hurry out of the store and into the mall, not stopping to look back."
            $ game.room = "mall1"
        "Investigate the voices":
            "I think about it for a moment, and then I resolutely shake my head."
            "I really should check it out, even if only for Sasha's sake."
            "At the very least I could end up getting told off for walking into the back of the store."
            "But the worst scenario might actually involve Sasha or one of her co-workers being in trouble."
            "And what kind of an asshole would walk away from that kind of a situation?"
            "So I take a deep breath and turn the door-handle as quietly as I can."
            "Then I inch the door open and step through it..."
            if not hero.has_skill("sneaky") and hero.fitness < 50:
                "I try my best to be quiet, but I guess I don't manage to pull it off."
                "That's because, almost the same moment I open the door, the voices fall silent."
                "And before I can as much as peer around the edge of the door, Sasha appears."
                show sasha surprised
                "In fact she almost pushes the door into my face, she appears so suddenly!"
                mike.say "Whoa, Sasha!"
                mike.say "It's only me!"
                show fx exclamation
                sasha.say "[hero.name]!"
                hide fx
                show sasha annoyed
                sasha.say "What in the hell?"
                sasha.say "Why are you even here?!?"
                "I hold my hands up in a gesture of surrender."
                "And I instinctively back away from Sasha as I do so."
                "She instantly follows me into the store, closing the door behind her."
                mike.say "Erm...this is a store, Sasha."
                mike.say "And the sign in the window says it's open too."
                mike.say "I didn't know I needed permission to come inside!"
                "I can see now that Sasha's a bit of a mess."
                "Her clothes are in a state of disarray and she's sweating too."
                "She seems confused and angry, far more than the circumstances justify."
                show sasha normal
                sasha.say "I...I guess you're right..."
                sasha.say "But I was busy back there just now!"
                sasha.say "You can't just walk into staff only parts of the store!"
                "I can't help looking over her shoulder at the door to the back of the store."
                "What on earth could she have been doing back there to get her this worked-up?"
                mike.say "Sasha..."
                mike.say "Are they working you too hard?"
                mike.say "I mean...I wanted to say how great you getting that award is."
                mike.say "But it's not worth it if you're going to collapse from exhaustion!"
                "Sasha looks at me for a moment like she has no idea what I'm talking about."
                "But then recognition dawns on her face and she shakes her head."
                sasha.say "No, [hero.name]..."
                sasha.say "It's okay, really it is."
                show sasha annoyed
                sasha.say "I was just dealing with a customer just now."
                sasha.say "One that's REALLY demanding, you know?"
                "I can't help nodding, as I've worked in retail myself."
                "And I know how that kind of customer can be."
                mike.say "Okay, Sasha, okay."
                mike.say "I see now that this isn't a good time."
                mike.say "We can chat about it when you get off your shift."
                show sasha happy
                sasha.say "Thanks for understanding, [hero.name]."
                sasha.say "I'll see you when I get home tonight."
                "I give Sasha a smile and a wave, then she shows me out of the store."
                hide sasha
                show bg mall1
                with fade
                "I watch as she lowers the shutters, looking furtively this way and that."
                "And then I walk out of the mall and begin to make my way home."
                "Boy, I sure hope those guys know how lucky they are to have a girl like Sasha."
                "She'd practically bend over backwards to please her customers!"
                $ game.room = "livingroom"
            else:
                $ sasha.flags.strapon_known = True
                "I must have passed the skill check when it comes to my ninja powers."
                "Because I manage to open the door and sneak through without being heard."
                "The two female voices keep right on yelling at each other as I sneak closer."
                "Positioning myself behind a convenient pile of boxes, I crane my neck to see them."
                "And when I finally do, I have to stifle a cry of sheer amazement."
                "I don't know what I'd been expecting to find back here."
                "But I know it wasn't Sasha standing there naked."
                "Well, naked save for a pretty impressive strap-on around her waist!"
                "And I certainly wasn't prepared for the second girl to be taking it up the ass!"
                "I lean in closer, trying to get a better look at the other woman involved."
                "It's...it's Palla!"
                "She's on her hands and knees."
                "She's totally naked."
                show fashion doggy pleasure with fade
                "And she's being fucked up the ass by Sasha!"
                "As I listen, what I heard through the door begins to make more sense."
                palla.say "Urgh..."
                show fashion doggy -pleasure
                palla.say "Harder, you minimum-wage whore!"
                palla.say "Fuck me HARDER - or I'm going to get you FUCKING FIRED!"
                show fashion doggy pleasure
                sasha.say "Hah..."
                sasha.say "That gets you wet, doesn't it?"
                sasha.say "You entitled, spoilt little bitch!"
                sasha.say "You get off on treating people like SHIT!"
                show fashion doggy close
                "Whoa...this is pretty intense stuff!"
                "Normally you'd have to pay good money to watch something like this."
                "But I'm getting a front-row seat to watch the entire show."
                show fashion doggy -close
                "Is this what they mean by customer service?"
                "If so, then it's no wonder Sasha's so popular!"
                "I watch for a few more seconds, but then a thought occurs to me."
                "Should I keep quiet back here and just see how this all plays out?"
                "Or should I take a gamble and see if this is a public affair?"
                menu:
                    "Keep quiet and watch":
                        "I've done pretty well to sneak in here without being caught."
                        "So maybe I shouldn't push my luck any further, just in case it runs out."
                        "With that in mind, I hunker down behind the boxes and keep watching."
                        "And it doesn't take long for my patience to be rewarded either."
                        show fashion doggy close
                        "Sasha's pounding away on Palla like she means it."
                        "I swear I can see all the suppressed rage of a retail worker in her thrusts."
                        "Every minute of the day she's spent dealing with boring tasks and idiot customers."
                        show fashion doggy -close
                        "All of it's going into the effort she's making to fuck Palla's ass."
                        sasha.say "How does that feel, Madam?"
                        sasha.say "Does it fit, huh?"
                        sasha.say "Is there enough room with your head already jammed up there?!?"
                        "For a moment I don't think she's going to get an answer out of Palla."
                        show fashion doggy ahegao close
                        "The other girl seems to busy moaning and groaning as her ass is pounded."
                        "But Palla's the other side of the coin to Sasha's exploited retail drone."
                        "What Palla personifies is every stuck-up, entitled cow that ever walked into a store."
                        "Every unreasonable customer that looked down at the staff and demanded to see the manager."
                        palla.say "Can't you fuck me any harder than that?"
                        palla.say "Seriously, you worthless flake!"
                        palla.say "This is NOT how to service a customer!"
                        show fashion doggy normal -close
                        sasha.say "Oh yeah?!?"
                        sasha.say "Then why don't you show me?"
                        sasha.say "Put your money where your nasty mouth is!"
                        "Palla instantly rises to the challenge."
                        "She pulls herself off the dildo with an amusing pop."
                        "And then she rounds on Sasha, still on her knees."
                        palla.say "Urgh..."
                        palla.say "Your pussy smells as cheap as it looks!"
                        palla.say "I bet you taste of rotten junk food!"
                        sasha.say "See for yourself, bitch!"
                        show fashion licking with fade
                        "With that, Sasha pushes Palla's face into her pussy."
                        "Instantly, Palla begins to lick at Sasha's lips as if her life depends on it."
                        show fashion licking up pleasure
                        "Sasha moans with pleasure, fingering her own nipples as she does so."
                        "For all of the insults the pair have traded, they seems to be getting off pretty well."
                        show fashion licking down
                        "Sasha's panting like a dog on heat, and Palla's eating her out like she's starving!"
                        "One of them has her face buried in the other's pussy."
                        show fashion licking up
                        "And the one being liked out is losing the power of speech."
                        "But somehow that still doesn't stop them trying to trade insults."
                        show fashion licking down
                        "I have to stifle a laugh as I hear Sasha and Palla mumbling away to each other."
                        "I can't make out what they're saying, so it just sounds utterly ridiculous!"
                        show fashion licking middle climax squirt
                        "It's only when I see signs of Sasha being about to come that I snap back to reality."
                        "I really shouldn't be anywhere near here once those two are done!"
                        "Using my sneaking skills again, I retrace my steps backwards."
                        $ palla.lesbian += 1
                        $ sasha.lesbian += 1
                        hide fashion with fade
                        "And as soon as I'm on the other side of the door, I make a run for it."
                        "All the way home I have the image of what I just saw replaying in my head."
                        "That and the sound of all those insults they traded in my ears too!"
                        "Say what you want about Sasha - she sure worked hard for the reputation she has with her customers!"
                        $ game.room = "mall1"
                    "Get involved":
                        "I can't just sit back and watch all of this."
                        "Not without at least trying to get involved."
                        "I mean, how often does a chance like this present itself?"
                        "So I stand up slowly and make a point of coughing loudly."
                        "Both Sasha and Palla stop dead, neither of them moving or seeming to breathe."
                        "Suddenly the room is so silent that you could actually hear a pin drop."
                        mike.say "Ahem..."
                        mike.say "Ladies..."
                        if hero.charm < 60:
                            "Before I can say another word, Palla lets out an ear-piercing scream."
                            "Sasha seems shocked too, but her expression soon turns into one of murderous rage."
                            "In fact, it's so scary that I almost miss the sound of the dildo popping out of Palla's ass!"
                            hide fashion
                            show palla naked blush at left5, vshake
                            show sasha strapon surprised at right5
                            palla.say "What the hell?!?"
                            show palla angry
                            palla.say "I thought you said there was nobody else in the store?!?"
                            show sasha vangry
                            sasha.say "There wasn't - I checked!"
                            sasha.say "And there soon won't be again."
                            show fx anger at right5
                            sasha.say "Because this limp-dick is leaving - NOW!"
                            hide fx
                            "I hold my hands up in a gesture of surrender."
                            "And I instinctively back away from Sasha as I do so."
                            mike.say "Okay, okay!"
                            mike.say "I'm gone!"
                            $ palla.love -= 3
                            $ sasha.love -= 3
                            $ palla.lesbian += 1
                            $ sasha.lesbian += 1
                            hide palla
                            hide sasha
                            show bg mall1
                            with fade
                            "I turn and literally run through the door to the store."
                            "And then I keep on running out of the entrance and then the mall."
                            "Say what you want about Sasha - she sure worked hard for the reputation she has with her customers!"
                            $ game.room = "mall1"
                        else:
                            mike.say "It appears you're having a dispute of a professional nature."
                            show fashion doggy normal
                            if renpy.has_label("fashion_harem_achievement_2") and not game.flags.cheat:
                                call fashion_harem_achievement_2 from _call_fashion_harem_achievement_2
                            mike.say "So perhaps what you need is a neutral, third party to arbitrate?"
                            mike.say "And might I offer myself to serve in just such a capacity?"
                            "I add what I hope is a roguish smile as my pitch comes to an end."
                            "For a moment, neither of the girls says a single word."
                            "They just stare at me in stunned silence."
                            "And all the while I try to ignore the fact that the dildo is still in a certain hole the whole time."
                            "But then Palla looks around to Sasha and a moment of silent communication seems to occur."
                            sasha.say "I...I guess we could use a hand..."
                            sasha.say "I was just trying to...satisfy this difficult customer!"
                            palla.say "I'm not apologising for being hard to please."
                            palla.say "After all, I DO have standards to maintain!"
                            "I take a step forwards, walking around the boxes between us."
                            "And I'm unzipping my flies as I do so."
                            "But I'm also praying that I've read the situation correctly too!"
                            mike.say "My assessment would be that you're doing fine at that end."
                            "I point to where Sasha is standing, with the strap-on inside of Palla."
                            show fashion doggy mike
                            mike.say "But there needs to be more done over here."
                            "I use my now erect cock to point towards Palla's open mouth."
                            mike.say "Maybe this would help?"
                            show fashion doggy -mike bj
                            "Without hesitating, I shove my cock into between Palla's lips."
                            "Instantly her eyes go wide with surprise."
                            "But they take on a more submissive, satisfied glaze."
                            "And Palla begins to lick and suck without any need to be prompted."
                            "I guess it's like when you put a toffee in some people's mouth."
                            "They just can't help chewing!"
                            "Sasha soon picks up where she left off, thrusting into Palla."
                            "Which means that she's being worked from both ends at once."
                            "The sight of Palla sucking my cock seems to excite Sasha."
                            "And she redoubles her efforts, making Palla whimper in response."
                            show fashion doggy bj pleasure close
                            "This in turn ensures that Palla works even harder to please me."
                            "She has my cock deep in her throat, head moving back and forth."
                            "It's like an unbroken chain, one person pleasures another."
                            "That turns on the next person and they try that much harder too."
                            "And before we know it, it's almost too much to handle."
                            "I can feel myself cumming, and so I have to decide what happens next..."
                            menu:
                                "Swallow":
                                    "I keep my cock firmly in Palla's mouth as I'm losing it."
                                    show fashion doggy bj cuminside with hpunch
                                    "This means that it hits the back of her throat a moment later."
                                    "She coughs and gags, but somehow manages to swallow it down."
                                    show fashion doggy -bj cum cumonpalla mouth
                                "Facial":
                                    show fashion doggy -bj mike
                                    "I take a step backwards, pulling my cock out of Palla's mouth."
                                    "She gags and coughs a little, but that's all she has time for."
                                    show fashion doggy cumshot ahegao with hpunch
                                    "Because I shoot my load into her face a moment later."
                                    show fashion doggy -cumshot cum cumonpalla facial
                                    "Palla gasps in surprise as the streamers of hot, sticky cum paint her face."
                            show fashion doggy mike -cuminside cum ahegao
                            "While Palla's still gasping from aftermath of sucking my cock, Sasha pulls out too."
                            "The strap-on pops out of Palla's ass with a comical sound."
                            "And she moans at the sensation, settling onto her haunches."
                            mike.say "Well, it looks like we managed to satisfy the customer's complaint."
                            mike.say "Because she's stopped making her demands, you see?"
                            "Sasha nods, a satisfied smile spreading across her face."
                            "Palla, on the other hand, looks up at us with an uncertain expression."
                            mike.say "Perhaps it's time the customer addressed your issues?"
                            mike.say "She could put her mouth to good use again?"
                            "Palla seems to understand what I'm getting at, as she nods eagerly."
                            show fashion licking with fade
                            "A moment later, she practically lunges for Sasha's exposed pussy."
                            "Sasha gasps in surprise and arousal as Palla's tongue darts between her lips."
                            show fashion licking pleasure up
                            "Her eyes roll back into her head, and I'm worried that she might fall over any moment!"
                            "That's why I step in to help, taking a firm hold of Sasha with both hands."
                            show fashion licking mike down
                            "I suppose it can't be helped that I miss my mark and end up holding onto her breasts."
                            "But I just have to make the best of the situation, caressing them eagerly."
                            show fashion licking up
                            "I feel Sasha's nipples stiffen between my fingers as I play with them."
                            "And she moans, leaning in closer to kiss me full on the lips."
                            show fashion licking down
                            "Sasha's tongue slips straight into my mouth like a lustful snake."
                            "And I wonder if this is what she's feeling in her pussy right now."
                            show fashion licking up
                            "She still moans while she kisses me, almost mewling with pleasure."
                            "Suddenly, Sasha starts to twitch and wriggle in my grasp."
                            show fashion licking down
                            "Her moans become sharp yelps as she begins to cum too."
                            "But none of that stops Palla for as much as a second."
                            show fashion licking up
                            "She keeps right on exploring Sasha's pussy with her tongue."
                            "And she seems to be going deeper still, even as Sasha loses it."
                            show fashion licking middle squirt
                            "It's only when Sasha almost collapses into my arms that Palla actually stops."
                            "And then all I can hear is the sound of us all panting for breath."
                            "Nobody speaks as we clean up and begin to get dressed."
                            "It seems that all of this is going to be one of those unspoken secrets."
                            $ palla.love += 2
                            $ palla.sub += 2
                            $ sasha.love += 2
                            $ palla.lesbian += 1
                            $ sasha.lesbian += 1
                            "The kind of thing we can't speak about to anyone that wasn't involved."
                            "It only occurs to me later to wonder about something."
                            "When I've left the shop and the mall, and I'm on my way home again."
                            "Only then do I start to wonder if the shop had CCTV in the back room..."
                            $ game.room = "livingroom"
                            $ Harem.join_by_name("fashion", "palla", "sasha")
    return

label palla_sasha_propose_male:
    "I'm trying to act as calm and nonchalant as I possibly can."
    "You know, so normal that nobody would ever suspect a thing?"
    "And of course the result is the exact opposite of what I intended."
    show palla annoyed at left5
    show sasha annoyed at right5
    "I'm acting so weird that Palla and Sasha are instantly suspicious."
    "They keep on staring at me and whispering to each other."
    "Which makes the situation that mush worse!"
    "Finally, they seem to decide that enough is enough."
    show palla blank
    palla.say "[hero.name]!"
    palla.say "Just what do you think you're doing?"
    show sasha annoyed
    sasha.say "Yeah, [hero.name]..."
    sasha.say "You're acting pretty weird right now."
    sasha.say "And I mean pretty weird even for you!"
    "I have no way to answer that question without letting on what I'm doing."
    "So the only solution that I can think of is to go ahead with it right now."
    "Sure, it's not ideal."
    "But the surprise might be enough to see me through."
    "So without another word, I get down on one knee."
    "And then I whip out the two little boxes in my pocket."
    show palla surprised
    show sasha surprised
    "Once these are open, the girls can finally see the rings."
    "Which does seem to change things a little."
    show palla at startle
    palla.say "Are you..."
    show sasha at startle
    sasha.say "Are those..."
    mike.say "Palla..."
    mike.say "Sasha..."
    mike.say "Will you marry me?"
    "Palla and Sasha manage to tear their eyes away from the rings for a moment."
    "Just long enough for them to look at each other in complete surprise."
    "Then they look back at me."
    "And I brace myself to hear their answers."
    if palla.love >= 195 and sasha.love >= 195:
        show palla happy
        palla.say "Oh my god, [hero.name]!"
        palla.say "I never thought you had such good taste."
        palla.say "That ring is SO on trend!"
        palla.say "How could I say no to it?!?"
        show sasha happy
        sasha.say "Of course I'll marry you, [hero.name]!"
        sasha.say "What took you so long to ask?"
        sasha.say "I feel like I've been waiting forever!"
        "I have to admit that I'm more than a little stunned."
        "Sure, I wanted them both to say yes."
        "But the reality of it's kind of hit me hard!"
        "Still I manage to get to my feet without fainting."
        show palla at center, zoomAt(1.5, (340, 1040))
        show sasha at center, zoomAt(1.5, (940, 1040))
        "And then I push the rings onto their fingers."
        mike.say "Erm, yeah..."
        mike.say "So sorry I was acting weird back there."
        mike.say "At least now you know why!"
        "Palla and Sasha nod and smile at this."
        "But I get the impression they're more interested in their rings."
        "Which is fine by me, as it gives me a chance to recover!"
        $ palla.set_fiance()
        $ sasha.set_fiance()
    elif palla.love < 195 and sasha.love < 195:
        palla.say "Oh my god, [hero.name]!"
        show palla annoyed
        palla.say "That ring is SO out of style!"
        palla.say "How could I ever marry someone with such bad taste?!?"
        show sasha annoyed
        sasha.say "Ah shit, [hero.name]!"
        sasha.say "Why'd you have to go and do that?"
        sasha.say "We had a pretty good thing going here."
        sasha.say "Now you've ruined it!"
        "I have to admit that I'm more than a little stunned."
        "Sure, I tried to prepare myself for them saying no."
        "But the reality of it's kind of hit me hard!"
        "Still I manage to get to my feet without fainting."
        mike.say "Erm, yeah..."
        mike.say "So that didn't go quite how I hoped it would!"
        "If I was expecting sympathy from Palla and Sasha, I was wrong."
        "Because both of them give me pretty hard stares."
        palla.say "That's hardly our fault, [hero.name]!"
        show palla angry
        palla.say "This was all your idea."
        sasha.say "Yeah, [hero.name]..."
        show sasha angry
        sasha.say "You rolled the dice and you lost - deal with it!"
        $ palla.love -= 25
        $ palla.sub -= 25
        $ sasha.love -= 25
        $ sasha.sub -= 25
    elif sasha.love < 195:
        palla.say "Oh my god, [hero.name]!"
        show palla happy
        palla.say "I never thought you had such good taste."
        palla.say "That ring is SO on trend!"
        palla.say "How could I say no to it?!?"
        show sasha annoyed
        sasha.say "Ah shit, [hero.name]!"
        sasha.say "Why'd you have to go and do that?"
        sasha.say "We had a pretty good thing going here."
        sasha.say "Now you've ruined it!"
        "I have to admit that I'm more than a little stunned."
        "Sure, I wanted them both to say yes."
        "But I never figured one would say yes and the other say no!"
        "Still I manage to get to my feet without fainting."
        mike.say "Erm..."
        mike.say "This is a little awkward!"
        show palla normal
        palla.say "Wait a minute, Sasha..."
        palla.say "That means you don't want to marry me either!"
        sasha.say "Well yeah, Palla..."
        sasha.say "I don't want to marry anyone right now!"
        "Palla makes a huffing sound and turns her back on Sasha."
        palla.say "Hmmpf..."
        palla.say "Forget her, [hero.name]."
        show palla happy
        palla.say "We can still get married."
        "Before I can object, Palla grabs my hand and leads me away."
        "And I look back over my shoulder at Sasha, not knowing what to do next."
        $ sasha.love -= 25
        $ sasha.sub -= 25
        $ palla.set_fiance()
    elif palla.love < 195:
        palla.say "Oh my god, [hero.name]!"
        show palla annoyed
        palla.say "That ring is SO out of style!"
        palla.say "How could I ever marry someone with such bad taste?!?"
        sasha.say "Of course I'll marry you, [hero.name]!"
        show sasha happy
        sasha.say "What took you so long to ask?"
        sasha.say "I feel like I've been waiting forever!"
        "I have to admit that I'm more than a little stunned."
        "Sure, I wanted them both to say yes."
        "But I never figured one would say yes and the other say no!"
        "Still I manage to get to my feet without fainting."
        mike.say "Erm..."
        mike.say "This is a little awkward!"
        show sasha normal
        sasha.say "Wait a minute, Palla..."
        sasha.say "That means you don't want to marry me either!"
        palla.say "Of course not, Sasha..."
        palla.say "If anything, you have even worse taste!"
        "Sasha narrows her eyes and turns her back on Palla."
        sasha.say "Forget that bitch, [hero.name]."
        show sasha happy
        sasha.say "We can still get married."
        "Before I can object, Sasha grabs my hand and leads me away."
        "And I look back over my shoulder at Palla, not knowing what to do next."
        $ palla.love -= 25
        $ palla.sub -= 25
        $ sasha.set_fiance()
    return

label palla_sasha_male_ending:

    if renpy.has_label("fashion_harem_achievement_3") and not game.flags.cheat:
        call fashion_harem_achievement_3 from _call_fashion_harem_achievement_3
    $ game.hour = 16
    $ game.room = "church"
    scene bg church wedding with fade
    "I feel like a bag of nerves right now, and I'm surprised that I'm not actually shaking."
    "Plus being trussed up in a restrictive suit and on display in front of an audience doesn't help."
    "I had thought that after all the stress of organising today, the actual wedding would be a breeze."
    "But it seems like I was wrong, my nerves are even worse now than they were in the run up."
    "Maybe that's because of the contrasting personalities of my two brides."
    "On the one hand, you have Palla."
    "For her everything has to be precise and planned out ahead of time."
    "And on the other, you have Sasha."
    "Who likes to fly by the seat of her pants and say fuck the details."
    "Then there's me, caught in the middle and trying to keep them both happy!"
    "I look over my shoulder and I see the same thing reflected in their respective guests."
    "Palla's friends from the fashion scene are all immaculate and stylish."
    "I swear not one of them has a hair out of place."
    "Then you have Sasha's friends from the metal scene, all in torn denim and black leather."
    "Jesus - some of them are even have profanities on their T-shirts!"
    "And yes, they are wearing T-shirts to a wedding!"
    "Before I can give myself an ulcer, I hear music begin to play."
    show sasha wedding zorder 2 at center, zoomAt (1.0, (880, 740))
    show palla wedding zorder 1 at center, zoomAt (1.0, (400, 740))
    with fade
    "Then the doors open and my brides walk into the chapel."
    show sasha at center, traveling (1.25, 5.0, (860, 900))
    show palla at center, traveling (1.25, 5.0, (420, 900))
    "They stride down the aisle side by side."
    "Because I know that neither of them is going to walk behind the other!"
    "And they look so different it's almost insane."
    "Of course Palla looks the image of perfection."
    "Her dress, hair and make-up have been styled with a cutting-edge vision."
    "So she looks like she could be walking down a catwalk right now."
    if palla.is_visibly_pregnant:
        "Somehow they even managed to make the dress sympathetic to her belly."
        "You can't hide the fact she's pregnant, but the dress makes it seem inconsequential."
    "Sasha's the perfect counter to Palla's perfection."
    "Pale skin and dark hair make her look like a Goth princess."
    "And she walks with a swagger no model ever possessed too."
    if sasha.is_visibly_pregnant:
        "She even carries her belly with a defiant pride."
        "Like she's challenging anyone to have a problem with her being pregnant."
    show sasha at center, traveling (1.75, 5.0, (840, 1200))
    show palla at center, traveling (1.75, 5.0, (440, 1200))
    "By the time Palla and Sasha reach the altar, I'm entranced."
    "And they end up waving their hands in front of my face to snap me out of it."
    show palla annoyed
    palla.say "Hello?"
    show sasha annoyed
    sasha.say "Hey, [hero.name]!"
    mike.say "Wha..."
    mike.say "Oh..."
    mike.say "Hey, guys!"
    "Priest" "Ahem..."
    "The sound of the priest coughing makes us all stand to attention."
    show palla normal
    show sasha normal
    "Even Palla and Sasha seem to be chastened by the sound."
    "Priest" "Shall we begin?"
    "We all nod."
    "Then the priest nods."
    "And we get this show on the road."
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To join these three people..."
    "Priest" "In the bonds of holy matrimony."
    "The rest is routine stuff."
    "Nothing really happens until it's time for the vows."
    "Priest" "Do you, Palla..."
    "Priest" "Take these two people..."
    "Priest" "To be your lawful, wedded partners?"
    show palla happy at startle
    palla.say "I do."
    "Priest" "Very good."
    "Priest" "Do you, Sasha..."
    "Priest" "Take these two people..."
    "Priest" "To be your lawful, wedded partners?"
    show sasha happy at startle
    sasha.say "I do."
    "Priest" "And do you, [hero.name]..."
    "Priest" "Take these two people..."
    "Priest" "To be your lawful, wedded partners?"
    mike.say "I do."
    "Priest" "I call upon all those here present..."
    "Priest" "That if you know of any lawful reason..."
    "Priest" "Why these three may not be married..."
    "Priest" "Speak now, or forever hold your peace!"
    "Part of me thinks that one of Palla's friends will brand me too unfashionable."
    "Or that one of Sasha's will accuse me of being a closet fan of K-Pop!"
    "But luckily for me, they all keep their mouths shut."
    "Priest" "Very well."
    "Priest" "It is therefore my pleasure to pronounce you married."
    "Priest" "You may celebrate in a way that you find fitting."
    show sasha happy zorder 2 at center, zoomAt (2.0, (820, 1340))
    show palla happy zorder 1 at center, zoomAt (2.0, (460, 1340))
    with hpunch
    "Palla, Sasha and I come together in a three-way embrace."
    "Then we share a kiss that's slow and sensual to begin with."
    "But which becomes ever more passionate with each second that passes."
    "Sure, we've got the rest of our lives together to do things like this."
    "But when you're married to two girls like these, why would you waste any time?"

    $ game.room = "park"
    scene bg park
    show palla blank
    with fade
    palla.say "What do you mean we should wait for Sasha to get here?"
    palla.say "I already told you that she was otherwise engaged."
    show palla normal
    palla.say "And she's fine for me to handle this on my own, okay?"
    show sasha annoyed at right with easeinright
    show palla surprised at startle
    sasha.say "Hey!"
    sasha.say "What the hell are you doing, Palla?"
    show palla annoyed
    show sasha at right5 with ease
    sasha.say "I had to run all the way here!"
    show sasha normal
    sasha.say "I almost didn't make it..."
    show palla at left5 with ease
    palla.say "Erm...okay..."
    palla.say "Change of plan - Sasha and I are going to do this together!"
    show sasha annoyed at startle
    sasha.say "What?"
    sasha.say "Weren't we always?!?"
    show palla normal
    palla.say "Never mind about that, Sasha."
    palla.say "We're supposed to be talking about what life's like living with [hero.name]!"
    show sasha normal
    sasha.say "Oh yeah..."
    sasha.say "Well...he's not the one that's hard to live with, Palla."
    sasha.say "That would be you!"
    show palla annoyed at startle
    palla.say "I beg your pardon?!?"
    sasha.say "Ah, come on, Palla!"
    sasha.say "[hero.name] and me are pretty laid back."
    sasha.say "You're the one that's always got to have things just so!"
    show palla blank
    palla.say "Well can you blame me?"
    palla.say "The two of you want to live like a couple of barbarians!"
    palla.say "I've never know such slobs in all my life!"
    sasha.say "Yeah, but [hero.name]'s worse than me, right?"
    show palla joke
    palla.say "Hmm..."
    palla.say "I suppose you're right."
    palla.say "At least you don't slob around the house in your shorts!"
    sasha.say "Oh no!"
    show sasha happy
    sasha.say "I know well enough to at least wear a robe over my underwear!"
    sasha.say "But you've got to admit, Palla..."
    sasha.say "He's a pretty fun guy to live with, right?"
    palla.say "I suppose so."
    show palla happy
    palla.say "He's certainly never tried to upstage me, that's for sure!"
    sasha.say "You'd better hope he's never tried on any of your stuff, Palla."
    show sasha joke
    sasha.say "You know, like when you're out of the house?"
    show palla surprised
    palla.say "What are you saying, Sasha?"
    palla.say "He wouldn't...would he?!?"
    sasha.say "Ha, ha!"
    show sasha happy
    sasha.say "The look on your face, Palla!"
    sasha.say "Come on, you know you love us really!"
    show palla joke
    palla.say "Yeah, yeah..."
    palla.say "I'm living the dream!"
    show palla normal
    palla.say "Okay, Sasha, I admit it."
    palla.say "I never thought this thing could work between the three of us."
    palla.say "But somehow it does."
    show sasha normal
    sasha.say "I mean, it's a shame that [bree.name] had to move out of the house."
    palla.say "Don't be silly, Sasha - there was no room for her and us!"
    palla.say "What with my hectic schedule at work, you know?"
    show palla blank
    palla.say "The life of a model is a hectic one!"
    sasha.say "Yeah - I never knew being a clotheshorse was so hard!"
    show palla annoyed
    palla.say "Hey!"
    show palla joke
    sasha.say "I guess you're right, Palla."
    show palla normal
    show sasha normal
    sasha.say "I'm always in and out with the band."
    palla.say "Oh yeah..."
    show palla joke
    palla.say "Have you actually learned to play in tune yet?"
    show sasha angry at startle
    sasha.say "Palla!"























    show sasha normal
    sasha.say "Jesus - look at us!"
    sasha.say "We're setting up house together."
    show palla normal
    palla.say "More than that, Sasha."
    palla.say "We're creating a home!"
    if (palla.is_visibly_pregnant or palla.flags.mikeBabies >= 1) and (sasha.is_visibly_pregnant or sasha.flags.mikeBabies >= 1):
        palla.say "I certainly wouldn't have had Mary without [hero.name]."
        show palla happy
        palla.say "And she means so much more to me than my career ever did."
        sasha.say "I used to think that boys were easier to raise than girls."
        show sasha happy
        sasha.say "But wow, did Tommy cure me of that one pretty quickly!"
    elif palla.is_visibly_pregnant or palla.flags.mikeBabies >= 1:
        palla.say "I certainly wouldn't have had Mary without [hero.name]."
        show palla happy
        palla.say "And she means so much more to me than my career ever did."
    elif sasha.is_visibly_pregnant or sasha.flags.mikeBabies >= 1:
        sasha.say "I used to think that boys were easier to raise than girls."
        show sasha happy
        sasha.say "But wow, did Tommy cure me of that one pretty quickly!"
    else:
        palla.say "And there might be other people to fit in down the line too."
        show sasha annoyed
        sasha.say "Huh?"
        sasha.say "Who's gonna be moving in with us?"
        palla.say "No, Sasha - new additions to the family!"
        show sasha normal
        sasha.say "OH!"
        sasha.say "Yeah...that could be a thing."
    show sasha normal
    show palla normal
    sasha.say "So all in all, things are pretty good, right?"
    palla.say "I'd say so."
    palla.say "But we don't need to tell [hero.name] that."
    show palla happy
    palla.say "At least not in so many words."
    show sasha happy at startle
    sasha.say "Ha!"
    sasha.say "You got that right, Palla."
    sasha.say "It's our duty to keep him on his toes!"
    scene bg black with dissolve
    pause 2.0
    $ game.set_new_game_plus()
    $ renpy.full_restart()
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
