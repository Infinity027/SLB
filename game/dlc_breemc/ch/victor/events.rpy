init python:

    Event(**{
    "name": "victor_female_event_01",
    "label": "victor_female_event_01",
    "display_name": "Meet the bogeyman",
    "duration": 2,
    "conditions": [
        MinDaysPlayed(9),
        HeroTarget(
            IsGender("female"),
            IsRoom("nightclub", "nightclubbar")
            ),
        ],
    "music": "music/darren_curtis/feel_it_in_your_feet.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "victor_female_event_02",
    "label": "victor_female_event_02",
    "display_name": "Cleaning up the mess",
    "duration": 2,
    "conditions": [
        IsDone("victor_female_event_01"),
        HeroTarget(
            IsGender("female"),
            IsRoom("alley")
            ),
        ],
    "music": "music/darren_curtis/feel_it_in_your_feet.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "victor_female_event_03",
    "label": "victor_female_event_03",
    "display_name": "The Graveyard Shift",
    "duration": 2,
    "conditions": [
        IsDone("victor_female_event_02"),
        IsHour(22, 3),
        HeroTarget(
            IsGender("female"),
            IsRoom("cemetery")),
        PersonTarget(victor,
            MinStat("love", 40),
            IsFlag("delay", False),
            ),
        ],
    "music": "music/darren_curtis/feel_it_in_your_feet.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "victor_female_event_04",
    "label": "victor_female_event_04",
    "display_name": "Blood on your hands",
    "duration": 2,
    "conditions": [
        IsDone("victor_female_event_03"),
        IsTimeOfDay("evening", "night"),
        HeroTarget(
            IsGender("female"),
            HasRoomTag("street")
            ),
        PersonTarget(victor,
            MinStat("love", 60),
            IsFlag("delay", False),
            ),
        ],
    "music": "music/darren_curtis/feel_it_in_your_feet.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "victor_female_event_05",
    "label": "victor_female_event_05",
    "display_name": "Dinner with a killer",
    "duration": 2,
    "conditions": [
        IsDone("victor_female_event_04"),
        IsHour(20, 22),
        HeroTarget(
            IsGender("female"),
            HasRoomTag("street")
            ),
        PersonTarget(victor,
            MinStat("love", 80),
            IsFlag("delay", False),
            ),
        ],
    "music": "music/darren_curtis/feel_it_in_your_feet.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "victor_preg_talk",
    "label": "victor_preg_talk",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            Not(OnDate()),
            IsFlag("pregnancy_father", "victor"),
            Or(
                MinCounter("pregnant", 60),
                IsFlag("foundpreg"),
                ),
            ),
        PersonTarget(victor,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("toldpreg", False),
            MinStat("sexperience", 1),
            ),
        ],
    "do_once": False,
    })

    Event(**{
    "name": "victor_kiss_me_female",
    "label": "victor_kiss_me_female",
    "max_girls": 1,
    "conditions": [
        HeroTarget(IsGender("female")),
        PersonTarget(victor,
            Not(IsHidden()),
            IsPresent(),
            MinFlag("kiss", 1),
            MinStat("love", 150),
            ),
        ],
    "chances": 20,
    "once_day": True,
    "do_once": False,
    "quit": False,
    })

    Event(**{
    "name": "victor_find_out_pregnancy",
    "label": "victor_find_out_pregnancy",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            Not(OnDate()),
            MinCounter("pregnant", 30),
            CounterChanceChecker("pregnant", 50)
            ),
        PersonTarget(victor,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("toldpreg", False),
            MinStat("sexperience", 1),
            ),
        ],
    "do_once": False,
    })

label victor_preg_talk:
    $ victor.flags.toldpreg = True
    $ victor.flags.know_is_father = True
    show victor
    "It's not hard to find Victor when you know the kind of places that he likes to hang out."
    "Well, maybe haunt would be a better term than hang out, as they're always spooky spots."
    "All I have to do is check out the local graveyards and the creepy woods to root him out."
    "And sure enough, I quickly find the goth I'm looking for, lurking in the shadows."
    bree.say "Victor, I can see you in there."
    bree.say "Would you mind coming out into the light for a moment?"
    bree.say "We need to talk."
    "Victor does as I ask, sliding out of his hiding place."
    victor.say "Oh, hello, [hero.name]."
    victor.say "I'll come out to talk."
    victor.say "But not all the way into the light."
    victor.say "I didn't put sunscreen on today - so I might get sunburn!"
    "I can't help noting that it's hardly a sunny day."
    "And we are pretty much standing totally in the shade."
    "But I don't have time to argue with Victor over his strange habits."
    "So I shake it off and try to get down to business."
    bree.say "Whatever, Victor..."
    bree.say "Just shut up and listen to me, okay?"
    "Victor's eyes go even wider than usual at my commanding tone."
    "But he's never been a particularly assertive kind of guy."
    "So he can't help but slide closer, doing as he's told."
    victor.say "Okay, [hero.name]..."
    victor.say "Keep your hair on!"
    victor.say "I'm all ears."
    "I take a deep breath and prepare myself for what lies ahead."
    "There's no easy way to say something like this."
    "So I just go right ahead and say it."
    bree.say "Victor..."
    bree.say "I missed my last period."
    "At the mere mention of the word, Victor screws up his face in disgust."
    victor.say "Eww..."
    victor.say "Please don't mention periods, [hero.name]."
    victor.say "So much blood!"
    "I do the best I can to ignore Victor's prudish reaction."
    "I need to get this out, and I can't afford to be distracted."
    bree.say "Whatever, Victor..."
    bree.say "The point is that it got me worried."
    bree.say "So I took a pregnancy test."
    "Victor's eyes are so wide now they're almost popping out of their sockets."
    "And he's doing that thing where he creeps forwards, like something out of a horror film!"
    victor.say "What are you saying, [hero.name]?"
    victor.say "Are you saying what I think you're saying?"
    bree.say "I'm saying the test was positive, Victor."
    bree.say "I'm pregnant, and you're the father!"
    "Victor throws up his arms and leaps backwards."
    "He looks like something caught in the headlights of a car!"
    if victor.love >= 150:
        victor.say "Oh wow, [hero.name]!"
        victor.say "You mean I'm going to be a father?"
        victor.say "You're going to have a little Victor?"
        "I can't hide how surprised I am with Victor's response."
        "All I can do is nod in agreement."
        bree.say "Yeah, Victor..."
        bree.say "Or maybe a little Victoria!"
        bree.say "I have to say, you're handling this better than I expected!"
        "Victor recoils a little at this, his hand on his chest."
        victor.say "What are you saying, [hero.name]?"
        victor.say "Don't you think I'm the fatherly type?"
        victor.say "I think there's a lot I could teach the little chap!"
        bree.say "You mean like teaching them to ride a bike?"
        bree.say "Or playing football with them at the park?"
        "Victor takes a step backwards, like a vampire reacting to garlic."
        victor.say "Let's not lose our tiny little minds, [hero.name]!"
        victor.say "I was thinking more like passing on fashion tips, you know?"
        victor.say "Showing them how to apply eye-liner too!"
        victor.say "And obviously introducing them to Bauhaus nice and early."
        "I shake my head and let out a chuckle at Victor."
        "He seems puzzled by my amusement, as he's totally sincere."
        "But the truth is I'm feeling pretty relieved and happy right now."
        "Sure, he's not typical father material."
        "But I feel like Victor's heart is in the right place."
        "And that's got to count for a lot, right?"
        bree.say "If you say so, Victor."
        bree.say "But I think we can leave the goth culture until later."
        bree.say "We need to focus on stuff like nappies and prams for now!"
        victor.say "Ooh, we should get one of those Victorian baby carriages!"
        victor.say "Black on black, with black lace trimmings!"
    else:
        victor.say "[hero.name]!"
        victor.say "My barely adequate psychic defences are crumbling!"
        victor.say "Please tell me that this is some kind of sick joke!"
        "I roll my eyes at Victor's typically dramatic reaction to the news."
        "The last thing I need right now are his pretentious theatrics."
        bree.say "No, Victor."
        bree.say "This isn't a joke!"
        bree.say "I'm definitely pregnant - and it's yours!"
        "Victor keeps on reeling from my words."
        "I have to follow him as he retreats."
        "And the scene reminds me of a vampire running away from garlic!"
        victor.say "Oh no, [hero.name]!"
        victor.say "I couldn't possibly get involved in all of that."
        victor.say "It'll be pretty intense, all of it."
        victor.say "And there'll be bodily fluids spraying all over the place too!"
        bree.say "Victor!"
        bree.say "It's your fault I'm in this mess."
        bree.say "The least you could do is offer to help!"
        "My words don't seem to be having the desired effect on Victor."
        "In fact he's already starting to run away."
        "Which is pretty amazing, as I've never seen him move that fast before!"
        victor.say "I...I have to go, [hero.name]!"
        victor.say "I just remembered there's somewhere else I have to be..."
        victor.say "Let me know how the whole baby thing turns out, yeah?"
        victor.say "Like maybe in ten years time?"
        "With that he's gone, and I choose to let him go."
        "Because seriously, what good is chasing him down going to do me?"
        "The useless prat's obviously going to be no use as a father."
        "Better to forget all about him and make plans myself."
        $ victor.breakup()
    return


label victor_kiss_me_female:
    show victor
    "I turn around to see Victor looming over me."
    "He has his mouth open, letting me see his teeth."
    "I never noticed how white and sharp they look before now!"
    "And in that moment, all the horror films I've ever seen flash through my head."
    "He's a vampire!"
    "He's going to bite my neck!"
    "And then he's going to drink my blood!"
    "I'm about to scream, but then I feel Victor's lips pressed against my own."
    hide victor
    show victor kiss
    with fade
    $ victor.flags.kiss += 1
    "He...he's kissing me!"
    "And it feels...it feels amazing!"
    "Suddenly Victor changes from a monster to a hero in my mind."
    "He's like one of those romantic heroes in a gothic novel."
    "And he's kissing me!"
    "I feel myself swooning in Victor's arms."
    "I can't help it, I feel like he's melting me with this kiss!"
    hide victor kiss with fade
    return

label victor_find_out_pregnancy:
    $ victor.flags.toldpreg = True
    show victor
    "Victor's looking at me sideways and in a curious manner."
    "But that's nothing new, he's always sizing someone up."
    "What is different is when he sidles up to me a moment later."
    show victor at center, zoomAt(1.5, (640, 1040)) with fade
    "Then he leans in and asks me a pretty insightful question."
    victor.say "[hero.name]..."
    victor.say "Correct me if I'm wrong..."
    victor.say "But are you pregnant?"
    "I can't help blinking in surprise."
    "As I wouldn't have expected a guy to notice the subtle clues."
    "But then Victor isn't exactly an average guy."
    bree.say "Wow..."
    bree.say "How did you know?"
    bree.say "I am pregnant, Victor!"
    victor.say "Hmm..."
    victor.say "I thought so."
    bree.say "But that's not all, Victor."
    show victor joke
    victor.say "Oh!"
    victor.say "It's not?"
    victor.say "What else is there to tell, [hero.name]?"
    show victor normal
    bree.say "Okay, Victor - hold onto your goatee!"
    menu:
        "It's yours":
            $ victor.flags.know_is_father = True
            bree.say "I have to tell you..."
            bree.say "That you're the father of my baby!"
            show victor surprised
            "Victor's eyes go wide with surprise."
            hide victor
            show victor surprised
            "And he takes a dramatic step backwards."
            if victor.love >= 160:
                victor.say "Oh man - are you kidding?"
                victor.say "I'm gonna be a father!"
                victor.say "We're going to have a kid!"
                "I have a smile on my face as I hear what Victor's saying."
                "Because most of it sounds pretty positive to me."
                bree.say "Erm..."
                bree.say "Does that mean you're okay with it, Victor?"
                bree.say "Just with you, it's sometimes hard to tell!"
                show victor happy at center, zoomAt(1.5, (640, 1040))
                "Victor nods and clutches my hands in his own."
                victor.say "I'm better than okay with it, [hero.name]!"
                victor.say "This is great news!"
                victor.say "We're going to be hearing the sound of tiny little footsteps!"
                victor.say "And for once it won't be a dwarf hitman come to take me out!"
            else:
                victor.say "No way, [hero.name]!"
                victor.say "This can't be happening!"
                victor.say "I always assumed I was shooting blanks!"
                "I frown a little, trying to follow what he's saying."
                "But I take it as a positive that he's not running away!"
                bree.say "Erm..."
                bree.say "Does that mean you're okay with it, Victor?"
                bree.say "Just with you, it's sometimes hard to tell!"
                "Victor shakes his head and backs away from me."
                "He looks almost like he's afraid."
                if victor.love >= 150:
                    show victor pain
                    victor.say "Argh..."
                    victor.say "No, [hero.name]!"
                    victor.say "I'm definitely not okay with it!"
                    victor.say "I can't be a father."
                    victor.say "Baby puke doesn't wash out of black suits!"
                    hide victor with easeoutright
                    "With that, Victor turns on his heel and hurries away."
                    "And I decide to let him go."
                    "Because I'm thinking maybe I can talk him around in time."
                else:
                    show victor pain
                    victor.say "Argh..."
                    victor.say "No, [hero.name]!"
                    victor.say "I'm definitely not okay with it!"
                    victor.say "I can't be a father."
                    victor.say "And you can't make me be one either!"
                    bree.say "Victor..."
                    bree.say "What are you saying?!?"
                    show victor angry
                    victor.say "This relationship is over, [hero.name]!"
                    victor.say "And I never want to see you again!"
                    hide victor with easeoutright
                    "With that, Victor turns on his heel and hurries away."
                    "And it doesn't look like he's coming back."
                    $ victor.set_gone_forever()
        "It's not yours":
            bree.say "I have to tell you..."
            bree.say "That you're not the father of my baby!"
            show victor surprised
            "Victor's eyes go wide with surprise."
            hide victor
            show victor surprised
            "And he takes a dramatic step backwards."
            if jack.love >= 140:
                show victor pain
                victor.say "Oh, man!"
                victor.say "I knew I was shooting blanks!"
                victor.say "So the kid's not mine!"
                "I frown a little, trying to follow what he's saying."
                "From what I can understand, he could be going either way."
                bree.say "Erm..."
                bree.say "Does that mean you're okay with it, Victor?"
                bree.say "Just with you, it's sometimes hard to tell!"
                "Victor nods and clutches my hands in his own."
                victor.say "No, [hero.name]..."
                victor.say "I'm having an existential crisis right now!"
                victor.say "Can't you see that?"
                bree.say "Ah..."
                bree.say "No, Victor - you look like that most of the time!"
                bree.say "But are you okay with what I just told you?"
                bree.say "Because I could use your help!"
                menu:
                    "Ask Victor to help with the baby":
                        if victor.love >= 160:
                            "Victor lets out a deep, painful sigh."
                            victor.say "Hurmph..."
                            victor.say "I'm not my usual, happy-go-lucky self right now, [hero.name]!"
                            show victor normal
                            victor.say "But I've wrapped my head around stranger things than this."
                            "I feel a sudden surge of reassurance."
                            "Maybe this is going to be okay after all."
                            bree.say "So..."
                            bree.say "You'll help me?"
                            show victor happy
                            victor.say "Yes, [hero.name]."
                            show victor joke
                            victor.say "But no more going with other men, yeah?"
                            "I nod, eager to accept any conditions for the answer I wanted."
                        else:
                            "Victor lets out a deep, painful sigh."
                            victor.say "Hurmph..."
                            victor.say "I'm not my usual, happy-go-lucky self right now, [hero.name]!"
                            victor.say "But I do still love you."
                            "I feel a sudden surge of reassurance."
                            "Maybe this is going to be okay after all."
                            bree.say "So..."
                            bree.say "You'll help me?"
                            victor.say "No, [hero.name]."
                            victor.say "Baby puke doesn't wash out of black suits!"
                            bree.say "Victor..."
                            bree.say "You can't abandon me!"
                            victor.say "I'm not, [hero.name]."
                            victor.say "I just won't raise another man's child for him."
                            "I decide to leave it at that."
                            "Because I'm thinking maybe I can talk him around in time."
                            $ victor.breakup()
                    "I won't bother you about it":
                        pass
            else:
                victor.say "Urgh..."
                victor.say "No, [hero.name]!"
                victor.say "I'm definitely not okay with it!"
                victor.say "I can't be a father to another man's child."
                victor.say "Baby puke doesn't wash out of black suits!"
                bree.say "Victor..."
                bree.say "You can't abandon me!"
                bree.say "Not at a time like this!"
                show victor sad
                victor.say "I think you'll find I can, [hero.name]."
                victor.say "How can I ever trust you again?"
                victor.say "How can I ever think anything you say isn't a lie!"
                bree.say "Aren't you being just a little dramatic?"
                show victor surprised
                victor.say "Who, me?"
                show victor angry
                victor.say "No!"
                victor.say "Never!"
                show victor annoyed
                "Victor shakes his head and backs away from me."
                "He looks almost like he's afraid."
                hide victor with easeoutright
                "With that, Victor turns on his heel and hurries away."
                "And I decide to let him go."
                "Because maybe I don't need that kind of drama in my life."
                $ victor.set_gone_forever()
    hide victor with fade
    return

label victor_birthday_date_female:
    $ DONE["victor_birthday_date_female"] = game.days_played
    $ game.active_date.clothes = "casual"
    scene bg street with fade
    "Part of me can't actually believe that I got Victor to tell me the date of his birthday."
    "The guy's so private and protective of his personal details that I don't even know his surname!"
    "So when he coughed up the information, it made me want to do something special to say thanks."
    "That's why I'm waiting for him by the gates to the park, clutching a picnic hamper to my chest."
    "I figure that he'll appreciate the chance to do something as normal and relaxing as having a picnic."
    "We can slow things down a little, you know?"
    "Really have a chance to get to know each other better."
    "Or at least that's what I hope we're going to be able to do once he gets here."
    "Part of me is actually expecting him to be late, just because he's a guy!"
    play sound car_screeching_tires
    "I'm about to check my watch when I hear the sound of screeching tyres."
    with hpunch
    "Looking up, I just have time to leap backwards as two cars go shooting past."
    "They're careering around in the road like they're actually chasing each other."
    "And they almost lose control as they skid around the corner and out of sight."
    play sound bus_accident
    "Just as I think it's all over, there's the sound of an almighty collision."
    "Oh no - they must have crashed!"
    "It takes me a few moments for me to recover from the shock."
    "And then I begin to wonder if I should hurry over there to try and help."
    "But before I can make up my mind, I see Victor jogging towards me from the same direction."
    show victor with easeinleft
    victor.say "Uh..."
    show victor happy
    victor.say "Hi, [hero.name]."
    "I blink in genuine surprise, still stunned on account of what I just witnessed."
    "But Victor doesn't seem to be aware of what's behind my confusion."
    show victor surprised
    victor.say "What's the matter, [hero.name]?"
    victor.say "I'm not late, am I?"
    show victor normal
    "Snapping out of it a little, I check the time on my phone."
    "And I see that Victor's not late at all, in fact he's bang on time."
    "The only thing I could possibly fault him on is that he's a little dishevelled."
    "He kind of looks like he got ruffled up in his efforts to get here."
    menu:
        "Worried by Victor's appearance":
            "I hurry over to Victor, worried about the state he's in."
            "At first Victor flinches and takes a step back."
            "But then he seems to realise that I'm not trying to hurt him."
            "And so he stands still, letting me do the best I can to clean him up."
            show victor sad
            victor.say "Uh..."
            victor.say "Sorry, [hero.name]."
            victor.say "I kinda came here straight from work."
            victor.say "I had to chase someone down, and it got pretty intense!"
            bree.say "Don't worry about any of that, Victor."
            bree.say "I'm more worried about whether you're okay or not!"
            "Now Victor looks more than a little surprised by my concern."
            show victor happy
            "He nods slowly and a smile creeps onto his face."
            victor.say "Okay, [hero.name]..."
            victor.say "If you say so."
            victor.say "For the record, I think I'm going to be okay."
            $ game.active_date.score += 20
        "Complain about Victor's appearance":
            "I shake my head and roll my eyes at Victor."
            "And then I walk over and start trying to dust him off."
            bree.say "Sure, you're right on time."
            bree.say "But you might have made an effort to look presentable!"
            "At first Victor flinches and takes a step back."
            "But then he seems to realise that I'm not trying to hurt him."
            "And so he stands still, letting me do the best I can to clean him up."
            show victor sad
            victor.say "Uh..."
            victor.say "Sorry, [hero.name]."
            victor.say "I kinda came here straight from work."
            victor.say "I had to chase someone down, and it got pretty intense!"
            bree.say "Well, I guess that can't be helped, Victor."
            bree.say "But maybe try to get off work a little early next time?"
            "Victor nods, not looking too pleased with my suggestion."
            "I've got to admit that this isn't how I wanted our date to get started."
            "But maybe it'll pick up from here now we've got that out of the way."
            $ game.active_date.score -= 10
    scene bg park
    show victor normal
    with fade
    "Victor and I start to walk into the park together."
    "I managed to pick a pleasant day for our picnic."
    "The sun is shining and there's not a cloud in the sky."
    "Pretty soon we're chatting away like old friends."
    victor.say "So, [hero.name]..."
    victor.say "You know this place well?"
    bree.say "Oh yeah, Victor."
    bree.say "My dad used to..."
    bree.say "Ungh..."
    bree.say "Bring me here all the time..."
    bree.say "Phew..."
    bree.say "As a kid, you know?"
    show victor sad
    victor.say "Are you feeling okay?"
    "The truth is that the picnic hamper is starting to get pretty heavy."
    "It wasn't too bad when I first picked it up."
    "But now the weight is getting to be a little too much."
    "The only problem is that I'm not sure I want to let it show."
    "Because I'm worried Victor will think I'm a wimp if I ask him for help."
    menu:
        "Ask for Victor's help":
            "I force myself to swallow my pride."
            "Then I turn to Victor and admit the truth."
            show victor happy
            bree.say "Would you mind helping me out?"
            bree.say "This thing's starting to get a little heavy!"
            victor.say "Sure thing, [hero.name]..."
            victor.say "You want me to take it for you?"
            bree.say "No..."
            bree.say "Just grabbing one side would be great."
            "Victor nods as he hurries to do as I ask."
            "And a moment later we're sharing the burden together."
            "Having Victor's help makes things a whole lot easier."
            "We're able to pick up the pace as well."
            "So we get to the picnic spot that much quicker too."
            "Maybe that's the answer with Victor."
            "Not trying to look all big and macho."
            "But instead treating him as an equal."
            $ game.active_date.score += 20
        "Don't ask for Victor's help":
            "I make a massive effort to straighten myself up."
            "And in doing so I manage to almost trip over my own feet."
            "Staggering forwards, it's all I can do to keep from landing on my face."
            show victor surprised
            victor.say "Whoa, [hero.name]!"
            "Victor instinctively rushes to help me."
            "But once I've recovered, I all but push him away."
            bree.say "I don't need any help, thank you!"
            bree.say "I can cope perfectly fine on my own."
            "Victor instantly backs off, holding up his hands."
            show victor sad
            victor.say "Sure, sure..."
            victor.say "I didn't mean to patronise you."
            "The moment I hear the tone of his voice, I cringe inside."
            "All he was trying to do was help me out."
            "Just like any halfway-decent human being would have done."
            "But I threw it back in his face."
            "And for what?"
            "To prove that I'm big and tough?"
            "It hardly seems worth the effort."
            $ game.active_date.score -= 10
    show victor normal
    "It doesn't take us long to reach the spot that I'd picked out for the picnic."
    "It's a nice place where the grass begins to run into the woods by a stream."
    "And a big bonus is that it's a little way off the beaten path in the park."
    "So not only are we getting a beautiful view, but a measure of privacy too."
    bree.say "Here we are, Victor!"
    bree.say "Would you mind spreading the out the blanket?"
    victor.say "Sure thing, [hero.name]..."
    victor.say "Whoa!"
    "Victor catches the blanket with ease as I toss it to him."
    "But he's still looking around a moment later."
    "Call me paranoid, but I get the feeling he's checking the spot out."
    "And I don't mean that he's appreciating the aesthetics either."
    "He seems to be studying all the angles around us."
    "In fact, it's almost like he's looking for places someone could hide!"
    bree.say "Is everything okay, Victor?"
    bree.say "Almost nobody comes around here."
    bree.say "I guarantee it!"
    victor.say "Oh..."
    victor.say "Oh yeah...sorry."
    victor.say "It's just hard for me to switch off sometimes."
    "Victor shakes himself."
    "And then he gets on with spreading the blanket on the ground."
    "As soon as he's done, I start to unpack the picnic."
    show victor at center, zoomAt(1.5, (640, 1040)) with fade
    pause 0.5
    show victor at center, zoomAt(1.5, (640, 1140)) with ease
    "Victor settles on the blanket and watches me."
    "And I flatter myself that he's admiring the spread I've put on for us."
    if hero.has_skill("cooking") or hero.has_skill("iron_stomach") or hero.knowledge >= 100:
        menu:
            "Take out what you have prepared for the meal" if hero.has_skill("cooking"):
                show victor happy
                victor.say "All of this stuff looks great, [hero.name]."
                victor.say "I can't remember the last time someone made a meal for me!"
                bree.say "It's a pleasure, Victor."
                bree.say "And I can't remember that last time I had someone to cook for."
                bree.say "Well...at least someone that seemed to appreciate it!"
                "Victor waits patiently for permission to get stuck in."
                "Which I happily give him with a simple nod of the head."
                "That done, we both start eating."
                "I'm well into my second helping and enjoying my cooking."
                "That is until I happen to take a quick glance at Victor."
                "And I see that he's eating like his life depends on it!"
                bree.say "Erm..."
                bree.say "Victor..."
                bree.say "Is everything okay?"
                "At the sound of my voice, Victor stops what he's doing."
                "And he looks up at me with his mouth half full."
                victor.say "Uh..."
                show victor surprised
                victor.say "Sorry, [hero.name]..."
                victor.say "This is so good, so tasty, you know?"
                show victor happy
                victor.say "I kind of got carried away!"
                "I can't help cracking into a beaming smile at the compliment."
                "And I make sure to hold up another helping to Victor."
                bree.say "Aw!"
                bree.say "That's so sweet of you to say."
                bree.say "And here, help yourself to all you want."
                bree.say "After all, I did make this for you!"
                $ game.active_date.score += 20
            "Offer as a meal what you have bought before coming" if hero.has_skill("iron_stomach"):
                "Serving up the food means that I have to open the packets."
                "And I can't help blushing as Victor watches me doing so."
                bree.say "I'm sorry, Victor..."
                bree.say "I feel like this should all have been home-made food."
                bree.say "But I'm just not very good at that kind of thing!"
                show victor happy
                "Victor shrugs and gives me a smile."
                "Like it's nothing at all to worry about."
                victor.say "Ah, it's okay, [hero.name]."
                victor.say "I don't get time to cook either."
                victor.say "I like, microwave most of my meals."
                victor.say "So it's pretty special even to have someone else do that for me!"
                "I nod and smile, offering him a plate of food."
                "I'm sure it'll be okay, just like he says."
                "And I'm sure that I remembered to check the use by dates on all of this stuff."
                "[hero.name] manages to keep it down"
                "I make a point of tucking into my food with enthusiasm."
                "Because I want to show Victor that it's good to eat."
                "At least as good as it can be without being home-made."
                "But I happen to take a quick glance at Victor."
                "I can see that he's doing the very best he can to hide it."
                "But all the same, his eyes are bulging out of their sockets."
                "And he doesn't look like he's feeling too good."
                bree.say "What's the matter, Victor?"
                bree.say "You look like you're having trouble swallowing!"
                "Victor turns his back on me for a moment."
                "And I can hear him coughing something into a napkin."
                "When he turns back, his face is red and his eyes are watering."
                show victor shy
                victor.say "Uh..."
                victor.say "I think that stuff's a little off, [hero.name]."
                victor.say "Like past it's use by date?"
                "All I can do is shrug and take another bite of my own food."
                "I make a point of swallowing it too."
                bree.say "Hmm..."
                bree.say "Tastes fine to me!"
                show victor surprised
                victor.say "Wow, [hero.name]!"
                victor.say "You must have one tough stomach."
                $ game.active_date.score += 10
            "Notice that Victor seems to be interested in something other than the meal" if hero.knowledge >= 100:
                "As we're eating, I notice Victor staring at the trees around us."
                "At first I think he's just enjoying the view."
                "But then I notice that he's kind of frowning at stuff."
                "And I can't help feeling worried that he's not enjoying himself."
                bree.say "Is something wrong, Victor?"
                bree.say "It's just...you look a little cross."
                "Victor seems to snap out of it as soon as he hears my voice."
                "The expression on his face changes too, becoming softer."
                victor.say "Uh..."
                victor.say "Sorry, [hero.name]..."
                victor.say "This is going to sound dumb."
                victor.say "But I was just wishing I knew what all of these trees and plants were called."
                bree.say "You mean you don't?"
                bree.say "No, I never had a chance to find out."
                bree.say "And I always wanted to get closer to nature, you know?"
                "[hero.name] has the knowledge to help"
                "I frown at the confession."
                "And then I shrug my shoulders."
                bree.say "Well..."
                bree.say "What do you want to know?"
                show victor surprised
                "At first Victor seems surprised by the question."
                "Like he was sure that I wouldn't be able to help."
                "But then he points at some of the trees nearby."
                victor.say "Uh..."
                victor.say "Like, what are those ones?"
                victor.say "The ones over there?"
                bree.say "Most of them are oaks."
                bree.say "But that one on the left is a birch."
                "Victor narrows his eyes at this."
                "Almost like he doesn't believe me."
                victor.say "How can you even tell?"
                bree.say "Look at the leaves, Victor."
                bree.say "They're really different in shape."
                show victor happy
                "Victor begins to look and listen more closely."
                "And soon I've given him the basics on identifying a couple of trees."
                "It's not much in terms of knowledge, but he seems pleased with the results."
                "And I feel better for having been able to help him out."
                $ game.active_date.score += 20
    else:
        "I'm well into my second helping and enjoying my cooking."
        "That is until I happen to take a quick glance at Victor."
        "I can see that he's doing the very best he can to hide it."
        "But all the same, his eyes are bulging out of their sockets."
        "And he doesn't look like he's feeling too good."
        "I watch Victor turn his back on me so that I can't see what he's doing."
        "But I can still guess that he's coughing something into a napkin."
        bree.say "Erm..."
        bree.say "Victor..."
        bree.say "Is everything okay?"
        show victor shy
        victor.say "Urgh..."
        victor.say "Ack..."
        victor.say "Uh...yeah, [hero.name]..."
        victor.say "I think..."
        victor.say "I think something got stuck in my throat, that's all!"
        "I nod and smile, not wanting to get into the subject any deeper."
        "And I make a promise to myself that I'll brush up on my culinary skills in future."
        $ game.active_date.score -= 10
    hide victor
    show victor normal
    with fade
    "Once we've finished eating, Victor helps me to pack everything away."
    show victor at center, zoomAt(1.5, (640, 1040)) with fade
    pause 0.5
    show victor at center, zoomAt(1.5, (640, 1140)) with ease
    "And then we sit back on the blanket, just watching the sky for a while."
    "Victor seems happy to just relax, but I'm feeling a little restless."
    "It seems to me that we need to actually be doing something."
    "That we're just wasting time and the chance to do more by sitting here."
    bree.say "You know, Victor..."
    bree.say "There are some lovely walks you can take in the park."
    bree.say "It'd be a shame to miss out on them, right?"
    "Victor blinks and looks me in the eye."
    "And I can see that he does look a bit tired."
    victor.say "Is that what you'd like to do, [hero.name]?"
    victor.say "I'm happy just chilling here for a while."
    victor.say "But if you want to go for a walk, we can do that."
    menu:
        "Decide to let Victor rest":
            "My instinct is to jump up the moment Victor gives me the choice."
            "But then I remember that we're supposed to be here to celebrate his birthday."
            "So he should really be the one to make that decision."
            "And not let himself be run into the ground to please me."
            bree.say "That's cool, Victor."
            bree.say "I picked this spot for just that reason."
            bree.say "So we could chill out in peace."
            show victor joke
            "Victor gives me a nod and a smile."
            "But I can see that he's really a lot more grateful than that."
            "He's quite for a long while as we relax."
            "And my instinct is to fill the silence with chatter."
            "But instead I bite my tongue and just keep quiet."
            "A few minutes later I feel Victor taking hold of my hand."
            "He still doesn't say anything at all."
            "Though he makes a point of squeezing it."
            "And that gesture lets me know how much he appreciates the moment."
            $ game.active_date.score += 20
        "Insist on taking a stroll":
            "As soon as Victor gives me the choice, I nod my head."
            bree.say "Yes, Victor..."
            bree.say "That's what I want to do."
            "I get to my feet, pulling him up after me."
            bree.say "Trust me, you won't regret it."
            show victor pain at center, zoomAt(1.5, (640, 1040)) with ease
            "Victor allows himself to be pulled to his feet."
            "And he does the best he can to hide how tired he is."
            "Putting my arm in his, I lead him towards the nearest path."
            "From there I take him on the best routes that I know around the park."
            "And I make sure that we see all of the best sights on the way round."
            show victor sad
            "All the while I can see that Victor's doing the best he can."
            "But more than once I get the feeling that his mind is elsewhere."
            show victor sad at center, zoomAt(1.5, (640, 1040)) with fade
            pause 0.5
            show victor joke at center, zoomAt(1.5, (640, 1140)) with ease
            "And by the time we get back to the blanket, his eyes are half closed."
            "Sure, he's still smiling and nodding away as I chatter at him."
            "But I'm now sure that the better idea would have been to let him have his way."
            "Who knows, maybe I can get him a coffee on the way home."
            "That might be enough to wake him up again."
            $ game.active_date.score -= 10
    "I get the feeling that it's almost time for us to pack up and leave."
    "We've finished the picnic by now, enjoyed the sights and sounds of the park too."
    "Staying too long could be enough to spoil the good time we've already had here."
    "But when I make a move to collect my things, Victor puts a hand on my wrist."
    victor.say "Wait, [hero.name]..."
    victor.say "Where are you going?"
    bree.say "Oh..."
    bree.say "I was just going to get ready to leave, Victor."
    bree.say "I thought we were getting to that point, you know?"
    bree.say "But if you want to stay longer..."
    show victor sad
    "Victor has a sad smile on his face as I say all of this."
    victor.say "No, [hero.name]..."
    victor.say "It's okay."
    victor.say "It's just that I don't get to do this kind of thing often."
    victor.say "So it's a welcome change..."
    victor.say "Ouch!"
    "Victor winces all of a sudden, and rubs his shoulder."
    victor.say "Huh!"
    victor.say "You see what I mean?"
    victor.say "Life kind of kicks the shit out of me sometimes!"
    menu:
        "Offer Victor a massage":
            "I feel like I need to do something to help."
            "But I know that guys like Victor often find it hard to open up."
            "Hell, my own dad is a pretty good example!"
            "So instead I turn my attention to Victor's more visible source of pain."
            bree.say "You want me to take a look at that, Victor?"
            bree.say "I know how to give a pretty good massage."
            show victor joke
            "Victor looks relieved to be talking about a different subject."
            "And he nods eagerly at the offer."
            victor.say "Would you mind?"
            victor.say "The guy I normally go to can't see me right now."
            victor.say "He got a bad case of lead poisoning."
            "I nod and help Victor take off his jacket."
            "Then I do the best I can to work on his muscles."
            "Like I expected, it's tight and knotted as hell."
            "He groans at my efforts, but keeps on nodding the whole time."
            show victor happy
            bree.say "There you go."
            bree.say "It's not perfect, but it's the best I can do."
            victor.say "It feels great."
            victor.say "Thanks, [hero.name]."
            "I get the feeling that Victor's thanking me for more than the massage."
            "That he's also thanking me for respecting his privacy too."
            $ game.active_date.score += 20
        "Offer to talk to Victor about his problems":
            "I feel like I need to do something to help."
            "And the first thing that springs to mind is talking."
            "Maybe Victor doesn't have anyone else that he can open up to."
            bree.say "I'm always here for you, Victor."
            bree.say "And people tell me I'm a good listener."
            bree.say "So if there's anything you want to talk about..."
            show victor angry
            "Suddenly there's a change in Victor's demeanour."
            "Before he was all smiles and nods."
            "But now it's like a shutter's come down over his emotions."
            "His mouth becomes a hard line and he's almost frowning."
            victor.say "I don't think so, [hero.name]."
            victor.say "There are somethings in my life that I can't share with you."
            victor.say "Urgh...I know that's not cool, I really do."
            victor.say "But it's for your own good, okay?"
            "I nod slowly, feeling more than a little stunned."
            "All I was trying to do was help the guy!"
            "But if he's that determined to keep his secrets to himself, then so be it."
            $ game.active_date.score -= 10
    show victor at center, zoomAt(1.5, (640, 1140)) with fade
    pause 0.5
    show victor at center, zoomAt(1.5, (640, 1040)) with ease
    "With everything packed back into the hamper, we're ready to go."
    "As we start to walk, Victor gives me a sideways look."
    victor.say "So..."
    victor.say "Is that the only thing you got me for my birthday?"
    if not hero.has_gifts:
        "Oh no!"
        "I thought that I'd forgotten something!"
        bree.say "Oh damn it!"
        bree.say "I spent so much time on the picnic."
        bree.say "It must have slipped my mind!"
        show victor sad
        "Victor chuckles and shakes his head."
        victor.say "Don't worry about it, [hero.name]."
        victor.say "The picnic was a great gift."
        victor.say "It's better than anything you could have bought me."
        $ game.active_date.score -= 20
        $ victor.love -= 10
    else:
        call give_a_gift (from_birthday_date=True) from _call_give_a_gift_26
        if _return != "done":
            if _return not in ["None", "exit"]:
                "I slap my forehead and let out a gasp of irritation."
                bree.say "Oh man!"
                bree.say "I'm so forgetful."
                bree.say "I spent so much time on the picnic."
                bree.say "I totally forgot I had this for you!"
                show victor happy
                "I pull out the gift and hand it to Victor."
                victor.say "Wow!"
                victor.say "Thanks, [hero.name]."
                victor.say "You didn't have to do that."
                if _return:
                    "But as soon as he has the thing open, Victor looks amazed."
                    victor.say "Oh my god..."
                    victor.say "[hero.name], where did you find this?"
                    victor.say "How did you know I was looking for one?"
                    "I feel a warm sense of satisfaction at Victor's reaction."
                    bree.say "Oh, I just listened carefully, that's all."
                    $ game.active_date.score += 20
                else:
                    show victor sad
                    "But as soon as he has the thing open, Victor looks disappointed."
                    victor.say "Oh..."
                    victor.say "Oh yeah..."
                    bree.say "What's the matter, Victor?"
                    bree.say "Is everything okay?"
                    victor.say "Erm..."
                    victor.say "Yeah, [hero.name], yeah..."
                    victor.say "It's great, I guess..."
                    $ game.active_date.score -= 10
            else:
                "Oh no!"
                "I thought that I'd forgotten something!"
                bree.say "Oh damn it!"
                bree.say "I spent so much time on the picnic."
                bree.say "It must have slipped my mind!"
                show victor sad
                "Victor chuckles and shakes his head."
                victor.say "Don't worry about it, [hero.name]."
                victor.say "The picnic was a great gift."
                victor.say "It's better than anything you could have bought me."
                $ game.active_date.score -= 20
                $ victor.love -= 10
    show victor normal
    "By now we're getting pretty close to the entrance of the park."
    "And that should probably mean the date is coming to an end too."
    "But there's always the chance that Victor's not ready to end it yet."
    "I mean, I could stand to spend a little more time in his company too..."
    "But I don't want to seem too needy and just come out with it."
    bree.say "Looks like we're back where we started!"
    bree.say "So is this where we say goodbye?"
    show victor surprised
    "Victor looks surprised to see the entrance of the park."
    "Almost like he's not pleased at being snapped back to reality."
    show victor normal
    if game.active_date.score >= 80 and victor.sexperience >= 1:
        victor.say "Oh yeah..."
        victor.say "I had a great time today, [hero.name]."
        victor.say "But we don't have to end it yet - do we?"
        "I blink in surprise."
        "Even though this is the answer I wanted to hear."
        bree.say "Y...yeah..."
        bree.say "Of course we don't!"
        bree.say "We can do whatever you want!"
        bree.say "Well...you know what I mean."
        "Victor thinks for a moment."
        "And then he looks back over his shoulder."
        victor.say "You know, you never did show me all of those paths in the park."
        victor.say "I'll bet there are some really quiet ones, yeah?"
        victor.say "The kind that most people don't even know are there?"
        bree.say "Now you mention it, I do know a couple..."
        "Taking hold of Victor's arm, I lead him back into the park."
        "All the time trying to hide my enthusiasm for what we're doing."
        call victor_birthday_sex from _call_victor_birthday_sex
    else:
        victor.say "Oh yeah..."
        victor.say "I had a great time today, [hero.name]."
        victor.say "We should do it again some time."
        "I stand there in silence."
        "Waiting for Victor to say more."
        "Like suggest a time or place for another date."
        "Or to suggest that we go somewhere else."
        "But the silence stretches on."
        "And it becomes more strained with every moment that passes."
        bree.say "Okay..."
        bree.say "So maybe call me?"
        bree.say "Or not - it's totally up to you!"
        "With that, I turn on my heel and hurry away."
        "Because I have no idea how to handle the situation."
        "And I hate not knowing if he wants to see me again or not."
    return

label victor_birthday_sex:

    return

label victor_female_event_01:
    scene bg nightclub
    "I clocked the group of scary-looking guys in dark suits almost as soon as we were in the nightclub, filling most of the secluded booths in the VIP area."
    "They were all shaven heads and mean stares, as though they thought everyone in the place was trying to lean over their shoulders and hear their conversations."
    "But I've seen so many wannabe gangsters hanging around in clubs before that I just plain ignored them and got on with enjoying myself instead."
    "I figure that whatever they're up to, it's nothing at all to do with me, and if I leave them alone they should at least return the favour."
    "But as the night goes on, I can't help casting my glance over to them from the relative safety of the dance-floor."
    "And every time that I do so, it feels as if their numbers have increased since I last looked, like they keep multiplying the second that I look away again."
    "I try to push them out of my mind and just keep on dancing, but they're giving me such a creepy vibe that pretty soon I can't think of anything else."
    show victor at left with easeinleft
    "It's then that I see another guy in a suit across the dance-floor, one that stands out from the rest."
    "While they all look like Eastern European mobsters, this guy's got long black hair, a stubbly beard and cheekbones to die for."
    show victor at center with ease
    "I can feel my heart beating a little faster at the sight of him, he's just got such almost film-star looks."
    "His eyes are dark and intense, and he looks like he spends most of his time brooding over how much the world hurt him in the past..."
    show victor at right with ease
    "While I'm busy mooning over him, I hardly notice that he's walking intently towards the gangster-types in the VIP area."
    "They're already rising from their seats and some of them seem to be disappearing into the crowd at his approach."
    "I see the dark-haired guy's gaze flick left and right as he notes their movements, and his right hand slip under his jacket."
    "Oh fuck - surely not!"
    scene bg nightclub at center, zoomAt(1.5, (640, 1040)), blur(5)
    show victor_firefight_po_base at center, zoomAt(1.0, (1040, 720))
    with hpunch
    "Before I can see what he pulls out in his hand, I feel someone grab me from behind."
    with screenshot
    play sound gun
    pause 0.2
    with screenshot
    scene bg nightclub at dark, center, zoomAt(1.5, (640, 1040)), blur(5)
    show victor_firefight_po_base at center, zoomAt(1.0, (1040, 720))
    play sound gun
    "My scream isn't enough to cover the sound of guns being fired close by me."
    "And soon my scream is just one among many as panic spreads throughout the club at the sudden gunfight."
    show victor_firefight_po_base at center, zoomAt(1.0, (940, 720)) with move
    "I'm dragged roughly backwards, and all that I can see of the person holding me hostage are his arms."
    "One of his black suited wrapped around my neck, the other is holding a huge pistol out in front of me."
    "Apart from that, all I can gather of him is the smell of his cheap cologne and the sound of his rough voice as he curses in what sounds to me like Russian."
    show victor_firefight_po_base at center, zoomAt(1.0, (740, 720)) with move
    pause 0.2
    show victor_firefight_po_base at center, zoomAt(1.0, (880, 720)) with move
    "I'm jerked this way and that as he struggles to point his gun at the dark-haired man."
    "His target seems to never be still, constantly weaving here and there amongst the crowd."
    hide victor_firefight_po_base
    show bg nightclub at blur(5), center, zoomAt(1.5, (640, 1040))
    show victor firefight fire -po at center, zoomAt(1.35, (200, 720))
    play sound gun
    pause 0.2
    show bg nightclub at dark, blur(5), center, zoomAt(1.5, (640, 1040))
    show victor firefight -fire
    "I can see a gun in his hand too, and he's firing as though he never ran out of bullets."
    show bg nightclub at blur(5), center, zoomAt(1.5, (640, 1040))
    show victor firefight fire
    play sound gun
    pause 0.2
    show bg nightclub at dark, blur(5), center, zoomAt(1.5, (640, 1040))
    show victor firefight -fire
    "Every one of his shots seems to result in another gangster screaming in pain and falling to the floor at his feet."
    show bg nightclub at blur(5), center, zoomAt(1.5, (640, 1040))
    show victor firefight fire
    play sound gun
    pause 0.2
    show bg nightclub at dark, blur(5), center, zoomAt(1.5, (640, 1040))
    show victor firefight -fire
    "The guy holding me is swearing now, and firing almost desperately at the dark-haired man as he sees his friends being cut down one by one before his very eyes."
    show bg nightclub at blur(5), center, zoomAt(1.5, (640, 1040))
    show victor firefight fire
    play sound gun
    pause 0.2
    show bg nightclub at dark, blur(5), center, zoomAt(1.5, (640, 1040))
    show victor firefight -fire
    "Every time he pulls the trigger, the proximity of my head to his gun means that my ears ring and my vision swims from the explosive force of the shot."
    "Thus far, the dark-haired man seems to have been ignorant of my own captor."
    show bg nightclub at blur(5), center, zoomAt(1.5, (640, 1040))
    show victor firefight fire
    play sound gun
    pause 0.2
    show bg nightclub at dark, blur(5), center, zoomAt(1.5, (640, 1040))
    show victor firefight -fire
    "But now a shot from his gun almost finds its mark, clipping his ear and causing him to finally turn in our direction."
    "He seems to dive to one side and raise his own gun to fire back at the same time."
    scene bg nightclub at dark, blur(5), center, zoomAt(1.5, (640, 1040))
    show victor firefight po
    "I swear that I can see a small explosion of fire emerge from the barrel of his gun as the bullet intended for my captor emerges."
    show bg nightclub at blur(5), center, zoomAt(1.5, (640, 1040))
    show victor firefight fire po headshot
    play sound gun
    "Time seems to slow to a crawl as the bullet travels through the air towards me."
    "And I'm utterly convinced that it'll hit me, not the gangster using me as a human shield."
    "Then time returns to its normal flow, and I hear a sickening sound that I can only think is the bullet entering my skull and turning my brain instantly to a bloody pulp."
    "I feel no pain at all, but then that would probably make sense as I don't have time to do so."
    "Gravity pulls me down and I feel myself falling onto the nightclub floor, believing that the lights now above me are the last thing I'll ever see."
    "So I just lie there and wait for the inevitable to happen..."
    scene bg nightclub
    show victor gun at center, zoomAt(1.5, (640, 1040))
    with fade
    "But it doesn't - and then I see a face looming over me."
    show victor shout at startle(0.1, 5)
    "Handsome man" "Hey, are you okay?"
    show victor normal
    "It's the dark-haired man, looking down at me with concern written all over his face."
    "Wow - he's even cuter close up!"
    bree.say "You...you shot me!"
    show victor upset at slide(10, 0.25)
    pause 1
    show victor at center, zoomAt(1.5, (640, 1040))
    "He shakes his head."
    show victor shout
    "Handsome man" "Ahh...no, I was shooting at him."
    show victor annoyed
    "I follow the direction in which his finger is pointing, looking over my shoulder until I can see the man I'm currently laid atop."
    "It's the same guy that grabbed me, only now he has a bloody, smoking hole right between his eyes."
    show victor normal
    bree.say "Arrggh...shit!"
    with hpunch
    show victor shout at startle(0.1, 5)
    "Handsome man" "Erm...are you gonna be alright?"
    show victor normal
    "I'm laid on the corpse of a dead mobster in the middle the carnage caused by a full-scale nightclub shoot-out."
    "How in the hell am I supposed to ever be alright again?"
    "Somehow, when I look back at the dark-haired man with eyes like saucers and almost hyperventilating, he takes this as an affirmative answer."
    "Handsome man" "Okay, good - look, I have to get the hell out of here, like right now!"
    hide victor with easeoutleft
    "With that, he stands up and hurries to the closest fire exit, slipping out of the door and disappearing into the night."
    "I look after him for a moment, before realising that I'm still sitting on the other guy's rapidly cooling corpse."
    "Shrieking once more, I clamber off it and get as far away as I can."
    "All the time I'm wondering about the dark-haired stranger - just who he is and what his story could be."
    "Well, that and if I can ever take enough showers to feel clean again..."
    scene bg black with dissolve
    $ game.room = "alley"
    return

label victor_female_event_02:
    scene bg alley at center, zoomAt(1.1, (640, 720)) with fade
    "I virtually leap out of the emergency exit into the alleyway around the back of the nightclub."
    play sound heartbeat fadein 1.0
    "My heart is still beating like a drum, and I can feel the blood pounding in my ears too."
    "I stagger the few feet to the wall of the building opposite, leaning against it for fear of collapsing."
    "And then I look down at my feet, trying to remember all those breathing exercises I learnt over the years."
    stop sound fadeout 1.0
    show victor shout at center, zoomAt(1.1, (640, 780)) with easeinleft
    "Handsome man" "Ah..."
    "Handsome man" "Are you like...okay and stuff?"
    show victor normal
    "Okay, so I totally recognise the voice, and I know that he's probably trying to be nice to me right now."
    "But the problem is that I'm still so totally wound up and stressed, I can't possibly do anything but react naturally."
    "Which is to leap away from the guy and let out a genuinely terrified scream into the bargain."
    show bg alley at vshake
    show victor surprised at vshake
    bree.say "AAARGH!"
    show victor shout at startle(0.1, 5)
    "Handsome man" "Ah..."
    "Handsome man" "You need to calm down there."
    show victor normal
    "Is he for real?"
    "Is he really telling me to calm down?"
    show bg alley at startle(0.1, 5)
    show victor at startle(0.1, 5)
    bree.say "What..."
    bree.say "What are you doing?!?"
    show victor upset
    "The mysterious man looks at me with an incredulous expression on his face."
    "Like he really doesn't understand what I'm talking about."
    show victor shout at startle(0.1, 5)
    "Handsome man" "Ah..."
    "Handsome man" "What do you think I'm doing, miss?"
    "Handsome man" "I'm checking if you're okay."
    show victor normal
    "I can't help shaking my head at him, stunned at his answer."
    show bg alley at startle(0.1, 5)
    show victor at startle(0.1, 5)
    pause 0.1
    if hero.morality >= 25:
        bree.say "How can you be so calm?"
        show victor surprised with dissolve
        bree.say "You just went on a rampage back in there!"
    if hero.morality <= 25:
        bree.say "Geez, are you for real?"
        show victor surprised with dissolve
        bree.say "You shoot your load and you expect me to just shrug it off?!?"
    else:
        bree.say "Are you serious right now?"
        show victor surprised with dissolve
        bree.say "You just shot up an entire nightclub!"
    "The man looks surprised at the tone I'm taking with him."
    "As if it's totally unreasonable that I should be reacting in this manner."
    show victor shout at startle(0.1, 5)
    "Handsome man" "Ah..."
    "Handsome man" "Okay..."
    "Handsome man" "Emotions are running high right now."
    "Handsome man" "At times like this I find it helps to try meditating, and stuff."
    "Handsome man" "You can call me Victor if you like"
    "Handsome man" "But you need to understand that you saw nothing, okay?"
    "Handsome man" "And you tell no one!"
    show victor upset with dissolve
    "My head is still kind of spinning, so it takes me a moment to realise he's staring at me."
    "Which I guess means that he's expecting some kind of an answer."
    menu:
        "Thank Victor for saving me":
            "Okay, I know that it's totally not cool to go on a rampage and shoot a bunch of people."
            "But for all I know, those guys he wasted back in the club could have been a real bunch of assholes."
            "I don't know, maybe they really deserved what they got at his hands?"
            "And even if they didn't, Victor still managed not to put a single bullet into me."
            "So I should probably be thanking him."
            show bg alley at startle(0.1, 5)
            show victor normal at startle(0.1, 5)
            if hero.morality >= 25:
                bree.say "Of course, Victor..."
                bree.say "You're right, and thank you for saving me."
            elif hero.morality <= 25:
                bree.say "You got it, Victor..."
                bree.say "And just so you know - I am SO grateful!"
            else:
                bree.say "Sure thing, Victor..."
                bree.say "And please don't think I'm ungrateful - I know that you saved me back there."
            bree.say "My name is [hero.name]"
            show victor normal at startle(0.1, 5)
            "Victor nods his head quickly, like he's not really listening to me."
            show victor paranoid at startle(0.1, 5)
            victor.say "Ah..."
            victor.say "Yeah, [hero.name]..."
            show victor shout
            victor.say "Look, I'm gonna go this way."
            show victor normal
            "He points in one direction."
            show victor shout at startle(0.1, 5)
            victor.say "You wait, like a minute..."
            victor.say "Then run in the other direction, okay?"
            show victor normal at traveling(1.1, 0.8, (1500, 780)) with easeoutright
            "Before I can say another word, he turns on his heel and runs off."
            "Leaving me to hurry off in the other direction."
            $ hero.morality += 1
            $ victor.love += 3
        "Pull Victor up on his brutality":
            "Part of me is obviously grateful that I wasn't one of the people that Victor just shot."
            "But at the same time, that doesn't change the fact he just went on the rampage right in front of me."
            "And there is no way that kind of thing is acceptable behaviour!"
            show bg alley at startle(0.1, 5)
            show victor paranoid at startle(0.1, 5)
            if hero.morality >= 25:
                bree.say "Don't you tell me what to do you...you thug!"
                bree.say "You just shot a whole bunch of people in there."
            elif hero.morality <= 25:
                bree.say "Okay, Victor...are you trying to impress me by shooting the place up?"
                bree.say "Because that is not the way to get into my panties!"
            else:
                bree.say "You really need to get help, Victor."
                bree.say "Because that is NOT the way to solve your problems!"
            show victor upset
            "Victor fixes me with a pretty serious stare."
            "One that's enough to make me instantly regret taking that tone with him."
            show victor angry at traveling(1.3, 0.5, (640, 900))
            victor.say "Are you even listening to me?!?"
            victor.say "This is serious stuff, [hero.name]!"
            show victor upset
            pause 0.2
            show bg alley at startle(0.1, 5)
            show victor at startle(0.1, 5)
            bree.say "Erm..."
            bree.say "Okay, Victor...I guess."
            show victor shout at startle(0.1, 5)
            victor.say "Look, I'm gonna go this way."
            show victor normal
            "He points in one direction."
            show victor shout at startle(0.1, 5)
            victor.say "You wait, like a minute..."
            victor.say "Then run in the other direction, okay?"
            show victor normal at traveling(1.3, 0.8, (1500, 900)) with easeoutright
            "Before I can say another word, he turns on his heel and runs off."
            "Leaving me to hurry off in the other direction."
            $ hero.morality += 3
            $ victor.love -= 1
        "Press Victor for answers":
            "Just who the hell is this guy?"
            "And why is he shooting up nightclubs?"
            "This is crazy, like a scene from a gangster movie or something!"
            "Okay, I know that there's like, a whole bunch of dead bodies back in there..."
            "But I have to find out more about Victor!"
            show bg alley at startle(0.1, 5)
            show victor paranoid at startle(0.1, 5)
            if hero.morality >= 25:
                bree.say "I'll do whatever you say, Victor..."
                bree.say "So long as you tell me a little more about yourself?"
            elif hero.morality <= 25:
                bree.say "You know what, Victor..."
                bree.say "A mysterious guy like you is pretty hot."
                bree.say "But getting to know you would be even hotter!"
            else:
                bree.say "I'm not doing anything for you, Victor..."
                bree.say "At least not until you tell me more about yourself!"
            show victor normal
            "Victor fixes me with a pretty serious stare."
            "One that's enough to make me instantly regret taking that tone with him."
            show victor shout at traveling(1.3, 0.5, (640, 900))
            victor.say "Did you hear a word I just said, [hero.name]?!?"
            victor.say "There's no time for that kind of thing right now!"
            show bg alley at startle(0.1, 5)
            show victor normal at startle(0.1, 5)
            bree.say "Erm..."
            bree.say "Okay, Victor...I guess."
            show victor shout at startle(0.1, 5)
            victor.say "Look, I'm gonna go this way."
            show victor normal
            "He points in one direction."
            show victor shout at startle(0.1, 5)
            victor.say "You wait, like a minute..."
            victor.say "Then run in the other direction, okay?"
            show victor normal at traveling(1.3, 0.8, (1500, 900)) with easeoutright
            "Before I can say another word, he turns on his heel and runs off."
            "Leaving me to hurry off in the other direction."
            $ hero.morality -= 1
            $ victor.love += 1
    scene bg black with dissolve
    $ victor.flags.delay = TemporaryFlag(True, 2)
    $ Room.find("cemetery").unhide()
    $ victor.unhide()
    return

label victor_female_event_03:
    if victor.love.max < 60:
        $ victor.love.max = 60
    scene bg street at center, zoomAt(1.2, (680, 720)) with fade
    "I don't often use the cemetery as a short-cut, though I know a lot of people who do."
    "And no, it's not because I'm superstitious or scared of seeing a ghost or a zombie!"
    "It's more on account of the type of living weirdo that would want to hang out in there."
    "Personally I'd rather be a couple of minutes late than run into a death-obsessed psycho."
    "But today I find myself deciding to make an exception to my usual rule."
    "It's a particularly bright, sunny kind of day and the birds are singing in the trees."
    "Not the kind of weather that some edgy gloom-lord is going to want to turn out in."
    show bg cemetery at center, zoomAt(1.2, (600, 720)) with fade
    "So I take the chance and turn into the cemetery when I reach the gates."
    "And it doesn't take me long to realise that I might have been wrong about this place."
    "In the bright light of day, it actually looks quite pretty and pleasant."
    "I mean sure, I know that I'm currently surrounded by gravestones, tombs and all that stuff."
    "But if I do my best to forget the specifics and don't read the inscriptions, I could almost be in the park."
    show bg cemetery at traveling(1.2, 1, (680, 720))
    "Plus it looks like I was right about there not being any weirdos around in the sunshine."
    show victor at left, blacker, zoomAt(1, (320, 740)) with dissolve
    "In fact, as I stroll through the cemetery, I can only see one other person around."
    show victor sad at dark, traveling(1.1, 1, (320, 800))
    show bg cemetery at traveling(1.15, 1, (680, 720))
    "And maybe that's why I find myself looking at the guy so closely."
    "He's in a black suit, with hair almost the same colour."
    "Ooh...he's actually quite cute!"
    "But wait a minute...he's more than a little familiar too."
    show victor at dark, traveling(1.2, 1, (320, 850))
    show bg cemetery at traveling(1.1, 1, (680, 720))
    show flowers at center, zoomAt(0.7, (190, 700)) with dissolve
    "As I get closer, it becomes more obvious where I've seen the guy before."
    "That style, those chiseled looks and designer stubble - it can only be one person I know."
    show bg cemetery at startle(0.1, 5)
    show victor at startle(0.1, 5)
    show flowers at startle(0.1, 5)
    bree.say "Victor?"
    bree.say "What are you doing here?"
    "The moment the words are out of my mouth, I feel like kicking myself."
    show victor surprised
    "Because Victor's head instantly snaps around in my direction."
    "I mean seriously, this guy must have the sharpest ears going!"
    "And that's when I see that he has a bunch of flowers in his hand."
    "So well done, [hero.name], you really put your foot in it this time."
    "What else is the guy going to be doing in a cemetery with flowers, other than visiting someone's grave?"
    "And you just managed to crash his moment of quiet, contemplative grieving with a dumbass question."
    show victor shout at startle(0.1, 5)
    show flowers at startle(0.1, 5)
    victor.say "Ah..."
    victor.say "Hey, [hero.name]..."
    victor.say "I was just..."
    show victor paranoid with dissolve
    pause 1
    show victor sad
    "Victor looks down at the flowers in his hand, and then back up at me."
    show bg cemetery at startle(0.1, 5)
    show victor at startle(0.1, 5)
    bree.say "Paying your respects, I know."
    bree.say "Look, Victor, I'm sorry, okay?"
    bree.say "I was just surprised to see you, that's all."
    bree.say "I should...I should really get going."
    "I'm expecting Victor to nod and wait for me to scuttle away."
    "But instead he surprised me by shaking his head and gesturing for me to come closer."
    hide flowers with dissolve
    pause 0.2
    show victor at traveling(1.2, 1.2, (640, 850))
    pause 1.2
    show flowers at center, zoomAt(0.7, (470, 700)) with dissolve
    pause 0.2
    show victor shout at startle(0.1, 5)
    show flowers at startle(0.1, 5)
    victor.say "No way, [hero.name]..."
    victor.say "It's okay, really."
    victor.say "Actually, I'd kind of like it if you hung around a little."
    show victor sad
    "Okay, that kind of makes sense."
    "He's visiting the grave of someone he cares about and he wants some company."
    "I'm sure that I can spare the time to indulge him in that."
    "And plus, it's not like I'm not intrigued as to who those flowers are for."
    show bg cemetery at startle(0.1, 5)
    show victor at startle(0.1, 5)
    show flowers at startle(0.1, 5)
    if hero.morality >= 25:
        bree.say "Of course, Victor - if that's what you want."
        bree.say "Do you mind me asking who it is you're visiting today?"
    elif hero.morality <= 25:
        bree.say "Any excuse to spend time with you, Victor!"
        bree.say "So who are the flowers for?"
    else:
        bree.say "I can spare you a couple of minutes, Victor."
        bree.say "So long as you tell me who you're visiting?"
    "Victor looks visibly relieved as I walk over to join him."
    "And I get the impression he's struggling to keep a handle on his emotions right now."
    "Man, this guy really is a deep, dark well of mystery and intrigue!"
    show victor shout at startle(0.1, 5)
    show flowers at startle(0.1, 5)
    victor.say "Ah..."
    victor.say "This is Svetlana's grave, [hero.name]..."
    victor.say "She was my wife."
    show victor sad
    "I can't keep my eyes from going wide as Victor tells me we're standing by his wife's grave."
    "Because this guy's story just keeps getting deeper and more intense as he reveals it to me."
    "First I meet a dark, brooding and obviously handsome guy that guns people down like it's nothing."
    "And then I find him laying flowers on the grave of his tragically deceased wife."
    show bg cemetery at startle(0.1, 5)
    show victor at startle(0.1, 5)
    show flowers at startle(0.1, 5)
    bree.say "Oh, Victor..."
    bree.say "I'm so sorry!"
    hide flowers at traveling(0.7, 0.5, (190, 1000)) with dissolve
    "Victor nods as he steps forwards to place the flowers on the grave."
    "But I note that he also places a small figurine shaped like a cat on there too."
    "Which seems weird, but now's not really the time or place to ask why."
    show victor shout at startle(0.1, 5)
    victor.say "Thanks, [hero.name]."
    victor.say "And thanks for being here with me."
    victor.say "I think she'd be pleased to know I've made a friend."
    show bg cemetery at startle(0.2, 5)
    show victor sadsmile at startle(0.2, 5)
    "I'm nodding at what Victor just said."
    "But it still strikes me as a little odd."
    "Like, does he really not have any other friends to comfort him at times like this?"
    "After that he seems to fall silent, like he's wanting to be alone with his thoughts for a moment."
    "And I find myself feeling like I should be doing something to help cheer him up."
    menu:
        "Stand in silence":
            "But then I really take a moment to think about the guy and what he's doing."
            "And I get the distinct feeling that this is probably exactly what he needs."
            "Someone to stand by him and remind him that he's not alone anymore."
            "To allow him to embrace the silence without it being totally bleak and hopeless."
            "So that's exactly what I do - I keep my mouth shut and just wait."
            "And eventually Victor's the one to break the silence."
            show victor shout at startle(0.1, 5)
            victor.say "Ah..."
            victor.say "Thanks, [hero.name]..."
            victor.say "This is usually pretty hard for me to handle."
            victor.say "But having you here really helped."
            show victor normal
            $ hero.morality += 3
            $ victor.love += 1
        "Try to get Victor to talk about his wife":
            "It worries me that all Victor seems to do is brood."
            "Because that means he's keeping it all bottled up inside."
            "Maybe what he really needs is to talk about his feelings more?"
            show bg cemetery at startle(0.1, 5)
            show victor at startle(0.1, 5)
            bree.say "Victor..."
            if hero.morality >= 25:
                bree.say "Would you like to talk about her?"
                bree.say "About Svetlana?"
            elif hero.morality <= 25:
                bree.say "Sounds like your wife was from Eastern Europe, right?"
                bree.say "I hear women from there can be pretty fierce, huh?"
            else:
                bree.say "Tell me if I'm overstepping the mark here..."
                bree.say "But would it help to talk about your wife?"
            "At the sound of my voice, Victor seems to be jerked out of his reverie."
            "And I can't help noticing that he's now frowning ever more than usual."
            show victor shout at startle(0.1, 5)
            victor.say "I..."
            victor.say "I suppose so, [hero.name]."
            victor.say "I'm not used to talking when I come here."
            victor.say "So it's kind of strange to be asked questions, you know?"
            show victor normal
            $ hero.morality += 1
            $ victor.love += 1
        "Try to lighten the mood":
            "Man, this guy could brood for his country most of the time."
            "But right now it looks like he's going for the world record!"
            "And yeah, I know that we're standing by the grave of his dead wife."
            "But there is such a thing as black humour, you know?"
            "So maybe what I need to do is lighten the mood a little."
            show bg cemetery at startle(0.1, 5)
            show victor at startle(0.1, 5)
            if hero.morality >= 25:
                bree.say "Isn't it always the way with women, Victor?"
                bree.say "Even now she's dead, you're still standing around waiting for her!"
            elif hero.morality <= 25:
                bree.say "Should you really let her see us here together, Victor?"
                bree.say "I mean, was she the jealous type?"
                bree.say "Because I don't want to be haunted by a vengeful spirit!"
            else:
                bree.say "The flowers are a nice touch, Victor."
                bree.say "But you could have bought fake ones."
                bree.say "Because it's not like she's going to notice!"
            "At the sound of my voice, Victor seems to be jerked out of his reverie."
            "And I can't help noticing that he's now frowning ever more than usual."
            show victor shout at startle(0.1, 5)
            victor.say "I..."
            victor.say "I don't really know what you mean, [hero.name]."
            victor.say "Like, if you're serious or if you're joking, you know?"
            show victor normal
            $ hero.morality -= 3
            $ victor.love -= 3
    "I choose to focus on the fact that I've managed to get Victor talking again."
    "Ignoring all of the other awkwardness associated with being at the side of someone's grave."
    "But a quick glance at the time reminds me that I was supposed to be going somewhere."
    show bg cemetery at startle(0.1, 5)
    show victor at startle(0.1, 5)
    bree.say "Oops..."
    bree.say "I'm gonna have to run, Victor!"
    show victor at startle(0.1, 5)
    "Victor looks disappointed at the news, but nods his head all the same."
    show victor joke at startle(0.1, 5)
    victor.say "Okay, [hero.name]..."
    victor.say "But thanks for sparing me the time you did."
    victor.say "I'm sure Svetlana would have been happy to see you there with me."
    victor.say "She always said that life was precious, that we shouldn't waste a second of it."
    show bg cemetery at startle(0.1, 5)
    show victor normal at startle(0.1, 5)
    if hero.morality >= 25:
        bree.say "That sounds like good advice, Victor."
        bree.say "She must have been a very wise woman."
    elif hero.morality <= 25:
        bree.say "Man, that's so true!"
        bree.say "You should take her advice, Victor."
    else:
        bree.say "I can appreciate that, Victor..."
        bree.say "Sounds like she had a real love of life."
    show victor happy at startle(0.1, 5)
    "Victor nods and gives me one of his typically awkward smiles."
    show victor at traveling(1.2, 1.2, (1500, 850))
    "Then he turns on his heel and walks off in the opposite direction."
    "Leaving me to hurry towards my own destination, still wondering what other secrets he's hiding."
    scene bg black with dissolve
    $ victor.flags.delay = TemporaryFlag(True, 2)
    $ Room.find("cemetery").hide()
    return

label victor_female_event_04:
    if victor.love.max < 80:
        $ victor.love.max = 80
    "One moment I'm just happily getting on with my day."
    "You know, thinking about nothing but the usual boring, dumb stuff?"
    "But then I somehow manage to make a turn, without even realising it."
    "And that's when everything changes in an instant."
    "Suddenly the only thing that seems to exist is what I'm staring at."
    show bg black
    show victor fly wounded at center, zoomAt(2, (540, 820))
    with fade
    "The bright red shade of blood upon pale-skinned hands."
    bree.say "What the actual fuck?!?" with vpunch
    show victor at traveling(1.4, 1.5, (540, 970))
    pause 1.5
    show victor -fly
    show bg street
    with dissolve
    "At the sound of my voice, Victor looks up at me, eyes wide with surprise."
    "But at the same time he doesn't stop cleaning the blood off his hands."
    show victor shout at startle(0.1, 5)
    victor.say "[hero.name!u]!"
    victor.say "What the hell are you doing here?"
    show victor angry
    "I only half hear the question that Victor yells at me."
    "The shaking of my head being more on account of disbelief for what I'm seeing." with vpunch
    bree.say "I..."
    bree.say "I guess there's no chance of an innocent explanation?"
    bree.say "Like, you didn't cut yourself while you were shaving?"
    "I guess it must be the ridiculous nature of the question that gets to Victor."
    show victor annoyed with dissolve
    "Because a moment later I see the expression on his face visibly soften."
    show victor sad with dissolve
    "And when he speaks again, the tone of his voice is far more gentle than before."
    show victor shout at startle(0.1, 5)
    victor.say "Look, [hero.name]..."
    victor.say "This isn't the kind of world you want to be involved in."
    victor.say "Not at all!"
    show victor sad
    show bg street at sepia, blur(10) with dissolve
    "I can't help feeling like this is one of those crossroads in life."
    "Like Victor and I have come as far as we can without something changing."
    "And sure, on the surface of it all, he's saying this isn't for me."
    show bg street at center, zoomAt(1.6, (740, 1110))
    show victor at center, zoomAt(2, (640, 1380))
    with fade
    "But at the same time, I get the feeling he's waiting to see what I do next."
    "That whatever it is, my reaction will shape how he treats me from this point on."
    menu:
        "Show fear":
            "I know that this would be a really good time to stick out my chin and act all tough."
            "To show Victor once and for all that I'm able to take the sight of him with literal blood on his hands."
            "But the truth is that's only how this kind of thing plays out in the movies and on TV."
            "Right now I can almost feel my legs beginning to wobble and my knees knock together."
            "Because this really is some terrifying shit!"
            if hero.morality >= 25:
                bree.say "Okay, Victor - I'm totally terrified."
                bree.say "Is that what you wanted me to say?"
                bree.say "Because it's the truth!"
            elif hero.morality <= -25:
                bree.say "You know a guy that's dangerous can be a real turn-on."
                bree.say "But that's usually when the danger's just hinted at."
                bree.say "Whereas you...you have an actual body-count!"
            else:
                bree.say "I'm not going to lie, Victor..."
                bree.say "Seeing what you do scares the shit out of me."
                bree.say "And I don't know what to do about it."
            "Victor gives me a hard stare as he seems to consider what I just said."
            "And then he lets out a resigned sigh, shaking his head."
            show victor sadsmile with dissolve
            victor.say "That's a shame, [hero.name]."
            victor.say "Because this is a big part of who I am."
            victor.say "And it's not something I can change either."
            victor.say "Now hand me that soap!"
            show victor sad
            $ hero.flags.mentee += True
        "Show curiosity":
            "I can't lie and just say that the violence in Victor's life doesn't scare me."
            "But then there's the fact that it doesn't make me just turn and run away either."
            "Which has to mean that I'm more curious about it than I am afraid."
            "I just need to find a way to put that into words he'll understand."
            if hero.morality >= 25:
                bree.say "I have no idea how you're able to do all of this, Victor."
                bree.say "But people tell me I'm a good listener."
                bree.say "So if you want to talk about it, I'm always here."
            elif hero.morality <= -25:
                bree.say "You know how hot a man with a mysterious past is, right?"
                bree.say "Then on top of that you're totally dangerous too."
                bree.say "Can you blame me for wanting to know more?"
            else:
                bree.say "You keep telling me how dangerous all of this is, Victor."
                bree.say "But you never tell me to keep away from you either."
                bree.say "I think you're trying to draw me in without knowing it."
            "Victor listens to what I have to say in total silence."
            "His hard stare boring into me the whole time."
            "Then he furrows his brow and curls one corner of his mouth."
            show victor joke at startle(0.1, 5)
            victor.say "You'll need more to survive in my world than curiosity, [hero.name]."
            victor.say "But it's a better place to start your journey than being afraid."
            show victor shout at startle(0.1, 5)
            victor.say "Now hand me that soap!"
            show victor upset
            $ hero.flags.partner = True
        "Show defiance":
            "Part of me wants to burst into tears and run away from Victor right now."
            "But it's not as strong as the part of me that wants to stand up to him."
            "Sure, he's this strong, silent and steely hitman type of guy."
            "But where does he get off just expecting me to go along with it all?"
            "He's running around, shooting off guns and Kung-Fu fighting all the time."
            "And I seem to keep on getting pulled into the middle of it all."
            if hero.morality >= 25:
                bree.say "Or what, Victor?"
                bree.say "What'll happen if I don't do as you say?"
                bree.say "Will you kill me too?"
            elif hero.morality <= -25:
                bree.say "And what if I don't, Victor?"
                bree.say "What are you going to do the, huh?"
                bree.say "Hit me?"
                bree.say "Force yourself on me?"
                bree.say "Maybe even kill me too?"
            else:
                bree.say "You just expect me to do as you say?"
                bree.say "What if I choose to go to the police, huh?"
                bree.say "What then, Victor - will you kill me too?"
            "For the first time I can recall, Victor looks speechless."
            "He just seems to absorb all that I've said and then stare at me."
            "The power of speech only returns to him as he shakes his head."
            show victor shout at startle(0.1, 5)
            victor.say "Ah..."
            victor.say "Of course not, [hero.name]!"
            victor.say "I was just...just saying it's serious, you know?"
            victor.say "And would you mind...well...handing me that soap?"
            show victor upset
            $ hero.flags.foil = True
    $ victor.love += 5
    $ victor.flags.delay = TemporaryFlag(True, 2)
    return

label victor_female_event_05:
    if victor.love.max < 100:
        $ victor.love.max = 100
    scene bg victorquarters at center with fade
    "It's not like this is the first time a guy's invited me over to his place and promised to cook me dinner."
    "But whenever it happened in the past I was always going to a house or an apartment for the date."
    "Hell, once I even found myself knocking on the door of a trailer!"
    "Though I have to admit, this is the first time I ever got invited to a meal at someone's safehouse."
    "At least that's what Victor called the place when he gave me the address and told me the time."
    "And I have to admit that when I saw the part of town where he's living, I almost chickened out."
    "It's one of those neighbourhoods that's more warehouses and empty lots than nice, neat rows of suburban houses."
    show bg victorquarters at center, traveling(2, 1.5, (1280, 1020))
    "But not wanting to look like I'm intimidated, I steel myself and hurry as fast as I can to the correct address."
    "And once I'm there, I find myself standing in front of a door that looks like it could keep out a damn tank."
    "I raise my hand, meaning to hammer on the metal plating in the hope of someone inside hearing me."
    "But then I see that there's a sturdy-looking intercom set into the wall beside the door."
    "So instead I press the button and speak into the microphone."
    bree.say "Erm..."
    bree.say "Victor?"
    if hero.morality >= 25:
        bree.say "Let me in - it's scary out here!"
    elif hero.morality <= -25:
        bree.say "Let me in before someone thinks I'm a hooker!"
    else:
        bree.say "You are in there, right?"
    "There's a long pause, which seems to stretch on forever as I stand there waiting."
    "Then I jump a little as the intercom buzzes in response."
    victor.say "Ah..."
    victor.say "Hey, [hero.name]..."
    victor.say "Great to see you made it."
    victor.say "Let me get the door for you."
    bree.say "Okay, Victor."
    "I hear the sound of a dull, metallic thud coming from the door."
    "Then it swings inwards, which I take as my que to step inside."
    scene bg victorsafehouse at center with dissolve
    "And once I do, I have to say that I'm pleasantly surprised."
    "Part of me had been expecting to find myself inside a cavernous warehouse or loft."
    "Or else to find Victor living inside what amounted to a survivalist's bunker."
    "But I'd describe what I'm walking into right now as...well, as homely!"
    "Sure, it's a little more minimalist and masculine in décor that I might have liked."
    "And yet there's subtle signs here and there of a woman's lingering influence."
    show victor joke at right with easeinright
    victor.say "Welcome to my humble abode, [hero.name]!"
    show victor at right, traveling(2, 1.7, (740, 1320))
    victor.say "Oh, and let me take your coat too."
    show victor at startle(0.2,-5)
    pause 0.5
    hide victor with easeoutright
    "I can't help smiling as Victor greets me and begins to play the part of the gracious host."
    bree.say "That's a pretty impressive front door you've got there."
    bree.say "I'm amazed you knew that it was me wanting to be let in."
    "Victor's still smiling as he hangs up my coat."
    "Then he points to a bank of screens on the wall by the door."
    show victor joke at right with easeinright
    victor.say "Not so hard when you have as many cameras as I do."
    victor.say "You were being recorded most of the way here."
    show victor normal
    "Looking at the grainy, black and white screens, I see that he's right."
    "I can spot views of every street I walked down and corner I turned getting here."
    "I'm about to say something about feeling watched."
    "But then I remember the kind of stuff Victor does for a living."
    "And I figure that it's a good thing he's taking so many precautions."
    show victor joke
    victor.say "Come this way, [hero.name]..."
    victor.say "I'm still in the middle of cooking dinner."
    victor.say "Otherwise I'd have made it to the door sooner."
    show victor normal
    "I nod eagerly and do as Victor asks, because I can already smell something good."
    show bg victorsafehouse at center, traveling(1.4, 1, (640, 920))
    show victor at right, traveling(1, 1, (1080, 720))
    "And as he leads me the short distance to the kitchen, it only gets better too."
    "Once we're there, Victor gestures for me to sit down at the table."
    "As I do so, he returns to fussing over the pots and pans on the stove."
    "Which leaves me to look around, taking in the ambiance of his home."
    "Like I said before, it has the unmistakable touch of a woman about it."
    "And as I start to notice small details, I realise she must have been Victor's departed wife."
    "I see pictures of them in what were doubtless happier times, doing typical couple stuff."
    "Plus there are mementos dotted around the place that I can't hope to make sense of."
    "But which obviously must have important stories and tender memories attached to them."
    show victor joke at right, traveling(1.4, 1, (640, 970))
    victor.say "Ah..."
    victor.say "I should warn you before we eat..."
    victor.say "That I might have oversold my abilities as a chef!"
    show victor normal
    "I turn to face Victor as he speaks up, still a little distracted from looking around the place."
    "So I shake my head as much to clear it and focus as to dismiss his apology."
    if hero.morality >= 25:
        bree.say "No need to apologise, Victor..."
        bree.say "I'm sure whatever you've made will taste great."
    elif hero.morality <= -25:
        bree.say "Oh don't worry about it, Victor..."
        bree.say "It's only fuel for my engine, after all!"
    else:
        bree.say "I'll reserve judgement until I taste it, Victor."
        bree.say "After all, the proof of the pudding is in the eating!"
    "Victor nods and lets out a chuckle in response."
    "But it doesn't take a psychic to know that he's nervous."
    "Which when you consider what he does for a living, is pretty weird!"
    show victor joke
    victor.say "Ha..."
    victor.say "See what you say once you've tried it, [hero.name]."
    victor.say "I'm afraid I only know how to cook what I call comfort food."
    victor.say "Nothing fancy or complicated, or else I just burn it!"
    show victor normal
    "I watch with genuine interest as Victor begins to dish up the food."
    "And the smell as he does so just seems to get better and better."
    "Even more so when I actually get the chance to see it on the plate."
    if hero.morality >= 25:
        bree.say "Mmm..."
        bree.say "That looks even better than it smells!"
    elif hero.morality <= -25:
        bree.say "I hope this tastes as good as it looks, Victor..."
        bree.say "My mouth's already watering!"
    else:
        bree.say "Looking good there, Victor..."
        bree.say "I can't wait to taste this!"
    "Victor places a plate in front of me and then sits down with his own."
    "He grabs a fork and points towards the food, indicating that I should begin eating."
    "So I do as he says, filling my fork and shovelling it into my mouth."
    bree.say "MMMM..."
    bree.say "This is amazing!"
    show victor happy at startle(0.2, 5)
    "Victor nods and smiles, looking genuinely happy to have pleased me."
    "I'm expecting him to start telling me about the food, explaining the recipe."
    "Or maybe to begin regaling me with tales of his exploits as a hitman."
    "But instead he tucks into his food, eating with a very healthy appetite."
    "And once the initial surprise has passed, it occurs to me that maybe this exactly what he wants."
    "Maybe it's been so long since he had someone to sit down for a quiet meal with."
    "That now he's happy just to have the company of another human being."
    "And perhaps if I was a more humble kind of girl, I'd just enjoy the quiet company too."
    "But that's just not me."
    "No, I want to pump Victor for as much info on himself as I possibly can!"
    menu:
        "Compliment Victor on his cooking":
            "But no matter how hard I try to think up a subject to ask about, it's no use."
            "Because I just can't get past how damn good this meal tastes!"
            if hero.morality >= 25:
                bree.say "Mmm..."
                bree.say "I'm not just being kind, Victor..."
                bree.say "This really is that damn good!"
            elif hero.morality <= -25:
                bree.say "You know, Victor, they say the way to a man's heart is though his stomach."
                bree.say "But your cooking is so damn good it, it makes it true of a woman too!"
                bree.say "If you know what I mean?"
            else:
                bree.say "You have no right to be this good of a cook victor."
                bree.say "And you're a complete asshole for keeping it from me for so long!"
                bree.say "I am never cooking for you after this, and I mean it."
            "Victor chuckles and shakes his head, waving away my compliments."
            show victor joke
            victor.say "Ah, stop it with the flattery!"
            victor.say "All I know are the recipes that my handler taught me."
            victor.say "Although I have made a couple of improvements myself."
            show victor normal
            "I'm obviously wondering what he means by 'handler' when I'd been expecting him to say his mom taught him."
            show victor annoyed
            "But suddenly Victor seems to get an odd, faraway look in his eyes."
            show victor joke
            victor.say "You know, most people have something to pass on before they die."
            victor.say "Like, my handler taught me all of her recipes, made then a part of me."
            victor.say "But it makes me wonder if there's anything I have that's worth passing on."
            victor.say "All I know is how to put a bullet into someone, [hero.name]!"
            show victor normal
            "I can't help frowning at Victor as he reduces himself to that one thing."
            "Because from what I've seen of the guy, there's far more to him than that."
            bree.say "You know something, Victor..."
            bree.say "You can be a total dummy sometimes!"
            show victor surprised
            victor.say "Huh?"
            victor.say "What do you mean?"
            bree.say "Well at the very least you could do the same damn thing as your...handler."
            bree.say "You could teach them to cook as well as you do, you dummy!"
            show victor happy
            $ hero.morality += 1
            $ victor.love += 4
        "Ask about his past":
            "Somehow I manage to resist the temptation to bang on about how good the food tastes."
            "As well as to stifle my curiosity as to how a hitman ends up living in a place like this."
            "And instead I use the opportunity to ask Victor about his mysterious past."
            "Okay, I know everyone's past is mysterious until you get to know about it."
            "But give me a break - it's not every day you get to eat dinner with a guy like this one!"
            if hero.morality >= 25:
                bree.say "So, Victor..."
                bree.say "You invited me to your place and cooked me a nice meal."
                bree.say "Isn't it about time you told me a little bit about yourself?"
            elif hero.morality <= -25:
                bree.say "Hmm...there's only one way this thing is going, Victor..."
                bree.say "We both know it's going to get intimate, sooner or later."
                bree.say "So wouldn't you like to tell me all about yourself before that happens?"
            else:
                bree.say "Okay, Victor, let's check the list..."
                bree.say "Invited to your place, check..."
                bree.say "Cooked me a really nice meal, check..."
                bree.say "So the next thing on the list would be - telling me about yourself!"
            "Victor chuckles and shakes his head."
            show victor joke
            victor.say "If I told you that, you know that I'd have to kill you, right?"
            show victor normal
            "For a moment I find myself looking at Victor in sheer amazement."
            "Because I'm not sure whether he's being serious or not."
            bree.say "Wait..."
            bree.say "You have to be screwing with me, right?"
            "Victor waits just long enough for me to get flustered."
            "And only then does he laugh and shake his head."
            show victor surprised at startle(0.1, 5)
            victor.say "Oh man, [hero.name]..."
            victor.say "The look on your face!"
            show victor happy with dissolve
            victor.say "No, I wouldn't HAVE to kill you..."
            victor.say "But it'd be dangerous for you to know too much about my past."
            show victor upset
            victor.say "For now, let's just say that I didn't have a traditional upbringing."
            victor.say "And that I did a lot of bad things to bad people for other bad people."
            $ victor.sub -= 2
        "Tease him for being so domesticated":
            "But no matter how hard I try to think up a subject to ask about, it's no use."
            "Because I just can't get past how domesticated Victor looks and acts in this setting."
            if hero.morality >= 25:
                bree.say "Oh, boy..."
                bree.say "This is so weird."
                bree.say "Out there you're this cool, edgy hitman."
                bree.say "But in here, you're making house and cooking wholesome food!"
            elif hero.morality <= -25:
                bree.say "You know, I always had you down as the edgy type, Victor."
                bree.say "All dark and brooding, enough to make a girl swoon."
                bree.say "But it turns out you're...like, a total domesticated male."
                bree.say "Which is kind of hot in a totally different way!"
            else:
                bree.say "I have to say, Victor..."
                bree.say "This isn't what I was expecting your place to look like at all."
                bree.say "I was thinking every wall would be filled with gun-racks and, like, samurai swords."
                bree.say "But instead it's like a cute little homely house!"
            "Part of me is worried that Victor will take my teasing him the wrong way."
            "So it comes as a genuine relief when he chuckles and shakes his head."
            show victor surprised at startle(0.1, 5)
            victor.say "Ah..."
            victor.say "Yeah...what can I say?"
            victor.say "It was Svetlana that kinda introduced me to all this stuff."
            victor.say "You know, taught me to value the simple things in life?"
            victor.say "Before her, I wasn't much more than my job."
            show victor normal
            "I'm listening intently to what Victor has to say."
            show victor annoyed
            "But suddenly he seems to realise that he's talking about his wife to another woman."
            "And he makes an effort to change the subject."
            victor.say "I'm sorry, [hero.name]..."
            victor.say "Let's talk about something else, okay?"
            show bg victorsafehouse at startle(0.2, 5)
            show victor at startle(0.2, 5)
            "Not wanting to push him into uncomfortable territory, I nod in agreement."
            $ hero.morality -= 1
            $ victor.sub += 2
    "Well, that might not have been all that I wanted to get out of Victor tonight."
    "But by the time the meal is over, I still feel like we've made a real connection."
    "You know, like he trusts me more than he did before and we're making progress."
    "So when he calls me a taxi and sees me into it, I pause to give him a little peck on the cheek."
    "And as the taxi drives away, it's weird to see a genuine hitman blushing from my doing so."
    scene bg black with dissolve
    $ Room.find("victorsafehouse").unhide()
    $ victor.flags.delay = TemporaryFlag(True, 2)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
