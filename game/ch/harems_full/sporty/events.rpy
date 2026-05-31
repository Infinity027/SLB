init python:
    Event(**{
    "name": "ayesha_hanna_showdown",
    "priority": 500,
    "label": "ayesha_hanna_showdown",
    "conditions": [
        HeroTarget(
            Not(OnDate()),
            HasRoomTag("gym"),
            ),
        PersonTarget(ayesha,
            Not(IsHidden()),
            HasRoomTag("gym"),
            ),
        PersonTarget(hanna,
            Not(IsHidden()),
            HasRoomTag("gym"),
            ),
        "Person.showdown(ayesha, hanna)"
        ],
    "do_once": True,
    })

    Event(**{
    "name": "sporty_harem_event_01",
    "priority": 500,
    "label": "sporty_harem_event_01",
    "conditions": [
        TogetherInHarem('sporty', 'ayesha', 'hanna'),
        HeroTarget(
            IsRoom("date_mall1"),
            ),
        PersonTarget(ayesha,
            Not(IsHidden()),
            HasRoomTag("mall_southside"),
            MinStat("love", 150),
            ),
        PersonTarget(hanna,
            Not(IsHidden()),
            OnDate(),
            MinStat("love", 150),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "sporty_harem_event_02",
    "priority": 500,
    "label": "sporty_harem_event_02",
    "conditions": [
        TogetherInHarem('sporty', 'ayesha', 'hanna'),
        HeroTarget(
            Not(OnDate()),
            HasRoomTag("gym"),
            IsFlag("sporty_delay", False),
            ),
        PersonTarget(ayesha,
            Not(IsHidden()),
            HasRoomTag("gym"),
            ),
        PersonTarget(hanna,
            Not(IsHidden()),
            HasRoomTag("gym"),
            ),
        ],
    "do_once": True,
    })

label ayesha_hanna_showdown:
    scene bg gym
    "I pride myself on being able to see trouble when it appears on the horizon."
    "That and having the brains to get the hell out of the way before it reaches me too!"
    "And it's pretty easy to spot trouble when it comes in the form of Ayesha."
    show ayesha a angry at right with dissolve
    "She towers over almost everybody, man and woman alike."
    show ayesha a angry at right4 with move
    "So when she shows up with a face like thunder, I know it's time to make myself scarce."
    "The only problem is that as soon as I turn to go, I find my path blocked."
    hide ayesha
    show hanna angry at center, zoomAt(1.5, (540, 1040))
    with hpunch
    "Hanna's standing in the way, hands planted firmly on her hips as she glares at me."
    "And the look on her face is only a little less scary than the one on Ayesha's!"
    "I look over Hanna's left shoulder and then her right, still trying to make my exit."
    show hanna at center, zoomAt(1.5, (640, 1040)) with move
    "But she moves to block me no matter what direction I try to take."
    hanna.say "Hey, [hero.name]..."
    hanna.say "Where are you going in such a hurry?"
    mike.say "Erm..."
    mike.say "Nowhere, Hanna, nowhere..."
    mike.say "But I do kind of need to be there fast!"
    show hanna annoyed
    hanna.say "Is that so?"
    hanna.say "Maybe you should ask for directions?"
    hanna.say "I know, let's ask Ayesha if she knows a short-cut!"
    show hanna angry
    "I feel a genuine sense of fear in the pit of my stomach as Hanna gazes over my shoulder."
    "And then I feel the actual weight of Ayesha's hand landing on my shoulder."
    "Before I can say a word, she spins me around on the spot."
    show hanna at center, zoomAt(1.5, (340, 1040))
    show ayesha a angry at center, zoomAt(1.5, (940, 1040))
    with moveinright
    ayesha.say "There you are, you little worm!"
    ayesha.say "You pencil-necked geek!"
    ayesha.say "You shit-arsed jobber!"
    "I recoil from Ayesha's tirade like she was coming at me with clenched fists."
    "I've seen her in the wrestling ring, even sparred with her on the mat."
    "But I've never seen her this angry for real!"
    "In desperation I turn one way and then the other."
    "But there's an angry-looking girl in each direction!"
    mike.say "Hanna..."
    mike.say "Ayesha..."
    mike.say "I can explain!"
    show hanna happy
    "Hanna laughs at my plea and shakes her head."
    "Ayesha just lets out a low, menacing growl."
    show fx question at left
    hanna.say "Really, [hero.name]?"
    show hanna angry
    hanna.say "You're going to explain how Ayesha and I were comparing notes just now?"
    ayesha.say "And you're going to explain how we've both been seeing this great guy?"
    hanna.say "How about we start comparing notes on him?"
    ayesha.say "Then how we then start noticing these two guys sound a lot alike?"
    hanna.say "How they both work out at our gym?"
    ayesha.say "And how they both have the same name?"
    if ayesha.is_visibly_pregnant and hanna.is_visibly_pregnant:
        "Ayesha and Hanna both point to their swollen bellies at the same time."
        ayesha.say "The father of my child is a cheating rat!"
        hanna.say "You knocked me up while you were sleeping around!"
    elif ayesha.is_visibly_pregnant:
        "Ayesha points to her already swollen belly."
        ayesha.say "The father of my child is a cheating rat!"
    elif hanna.is_visibly_pregnant:
        "Hanna points to her visibly swollen belly."
        hanna.say "You knocked me up while you were sleeping around!"
    else:
        ayesha.say "I'm just glad I made you use protection!"
        hanna.say "Yeah, that makes two of us!"
    "I guess this is the danger of trying to juggle two girls at once."
    "It was all fun and games when I was getting away with it."
    "But now I've been caught out, and it's time to pay the price."
    mike.say "Okay, okay..."
    mike.say "You got me bang to rights."
    mike.say "One amazing girl should have been enough for me."
    mike.say "I guess the chance to be with two just blew my mind!"
    "Yeah, I know that I'm trying to be humble and charm them at the same time."
    "But as I see it, there's no way out of this situation where I end up looking good."
    "So I might as well put myself totally at their mercy."
    show hanna annoyed
    "And I can already see that Hanna's warming to the compliment just a little."
    "Like she could totally buy a guy being overwhelmed by just how hot she is!"
    "But I should have known Ayesha would be a harder sell."
    "She's spent most of her life being self-conscious thanks to her size."
    "So she's that much better at sniffing out bullshit!"
    hanna.say "Well..."
    show hanna normal
    hanna.say "You DO kind of have a point!"
    ayesha.say "What are you saying, Hanna?"
    show fx exclamation at right
    ayesha.say "This guy cheated on us!"
    ayesha.say "He's been fucking each of us behind the other's back!"
    "I sense the chance to capitalise on the schism between them."
    "And so I grab it with both hands and try to hold on for dear life!"
    mike.say "I know, Ayesha, and I don't expect you to forgive me."
    mike.say "But I am sorry, you have to believe that!"
    mike.say "There's just something about the gym, you know?"
    mike.say "We're all there in the same place."
    mike.say "We're in super-tight clothes."
    mike.say "We're working out together, sweating together..."
    mike.say "It's almost like I'm breathing in your pheromones the whole time!"
    show ayesha normal
    "Both of the girls listen to what I say in silence."
    "They seem to be weighing it up for themselves."
    "Then they exchange a meaningful look."
    "And I can almost feel them coming to a final decision."
    if all([person.love >= 160 and person.lesbian >= 9 for person in [ayesha, hanna]]):
        "Ayesha and Hanna shake their heads at each other."
        "And then they shrug their shoulders, laughing as they do so."
        hanna.say "You're sure lucky that we're such great girls, [hero.name]."
        hanna.say "Because most women in our position wouldn't be so understanding!"
        ayesha.say "But you get one thing into your head, okay?"
        ayesha.say "This thing stays between the three of us!"
        "I look from Ayesha to Hanna and back again."
        mike.say "You..."
        mike.say "You mean..."
        mike.say "Actually, what do you mean?!?"
        "As one, Ayesha and Hanna lean in and kiss me on either cheek."
        hanna.say "We mean that you're off the hook, [hero.name]."
        show hanna blush
        ayesha.say "And that you get to keep both of us."
        show ayesha blush
        ayesha.say "But no more going behind our backs!"
        hanna.say "Yeah, [hero.name]!"
        hanna.say "We're all in this together now, yeah?"
        "I can only blink in surprise."
        "Like it's taking my brain an age to catch up."
        mike.say "You mean..."
        mike.say "We're like..."
        mike.say "We're a threesome now?"
        hanna.say "That's right, [hero.name]!"
        ayesha.say "Aww, bless him!"
        ayesha.say "He got there in the end!"
        "I'm still speechless now that I know this is for real."
        "But now it's more on account of me considering the possibilities."
        "And there certainly are a lot of those!"
        $ Harem.join_by_name("sporty", "ayesha", "hanna")
        $ game.flags.sporty_delay = TemporaryFlag(True, 1)
    elif (hanna.love < 160 or hanna.lesbian < 9) and (ayesha.love >= 160 and ayesha.lesbian >= 9):
        ayesha.say "I..."
        ayesha.say "I guess I can understand that, [hero.name]."
        ayesha.say "I mean...I do think the gym can be kind of a sexy place."
        ayesha.say "And we all like to check out a tight body every now and then!"
        "I nod and smile, eager to encourage Ayesha down that avenue of thought."
        "But at the same time I can see that Hanna's not about to join her."
        show hanna annoyed
        hanna.say "Yeah, that's not going to work for me."
        hanna.say "I practically run the gym, and I have to be a professional."
        hanna.say "I can't spend all day staring longingly at people's asses!"
        mike.say "What are you saying, Hanna?"
        mike.say "That you want out of our relationship?"
        show hanna sad
        "Hanna sighs and shakes her head."
        hanna.say "Yeah, but it's more than that."
        hanna.say "I've been feeling like I need a change for a while now."
        hanna.say "Like I should branch out on my own."
        hanna.say "Maybe start over in a new city."
        hanna.say "Even start a gym of my own."
        hanna.say "Because I think you two are going to be happy together without me!"
        "I look at Ayesha, and she nods."
        "And at the same time she squeezes my hand."
        mike.say "You know what, Hanna..."
        show ayesha blush
        mike.say "I think you're right!"
        $ hanna.set_gone_forever()
    elif (ayesha.love < 160 or ayesha.lesbian < 9) and (hanna.love >= 160 and hanna.lesbian >= 9):
        hanna.say "Yeah, well..."
        hanna.say "You're only human, [hero.name]!"
        hanna.say "I guess most of the guys I teach must have a crush on me!"
        hanna.say "So I can't be mad at you for being human!"
        "Ayesha snorts in derision at this, shaking her head."
        "It's pretty clear that she doesn't agree with Hanna's sentiment."
        ayesha.say "I can't believe I'm hearing this!"
        show ayesha angry
        ayesha.say "He cheated on us both and you're talking about forgiving him?"
        ayesha.say "I don't care what perverted stuff you're prepared to put up with, Hanna!"
        ayesha.say "I'm dumping his sorry ass!"
        "Hanna looks instantly offended at the accusation."
        "She fixes Ayesha with a serious stare."
        hanna.say "Hey!"
        show hanna angry
        hanna.say "Who are you calling a pervert?!?"
        hanna.say "I'm still kind of your boss, you know?"
        ayesha.say "Yeah, well..."
        ayesha.say "I can soon fix that, Hanna."
        ayesha.say "Because I quit!"
        ayesha.say "You can keep this guy and shove your job!"
        "As Ayesha storms away, I feel Hanna take hold of my hand."
        hide ayesha with moveoutright
        "She gives it a squeeze and leans into my shoulder."
        hanna.say "Don't worry about her, [hero.name]."
        show hanna blush
        hanna.say "She was always too uptight anyway."
        hanna.say "And I'll be more than enough woman for you - I promise!"
        $ ayesha.set_gone_forever()
    else:
        play sound punch_hard
        pause 0.2
        with hpunch
        "Ayesha and Hanna turn almost as one and slap me in the face."
        "One of them gets me from each side, snapping my head around as they do so."
        "Once they're done, I'm left dazed, my head spinning and my eyes blurred."
        mike.say "Wha..."
        mike.say "Huh..."
        show hanna angry
        hanna.say "Oh, stop feeling sorry for yourself!"
        hanna.say "You deserve more than a little slap!"
        show ayesha a angry
        ayesha.say "Yeah, you prick!"
        ayesha.say "I should stretch you until you break!"
        "I shake my head groggily."
        "And I manage to shake off some of the disorientation too."
        mike.say "Ah, come on, girls!"
        mike.say "Give me a chance to make it up to you!"
        show hanna annoyed
        "Hanna lets out a disdainful chuckle."
        "And Ayesha lets out a low growl."
        hanna.say "I've been feeling like I need a change for a while now."
        hanna.say "Like I should branch out on my own."
        hanna.say "Maybe start over in a new city."
        hanna.say "Even start a gym of my own."
        hanna.say "How about you, Ayesha?"
        hanna.say "You want to come work for me?"
        show ayesha annoyed
        "Ayesha nods, turning her back on me as she does so."
        ayesha.say "I might take you up on that offer, Hanna."
        ayesha.say "This place is starting to get old."
        ayesha.say "You know, like it's full of trash?"
        "I open my mouth to protest."
        show hanna angry
        show ayesha angry
        "But then I see the pair of them staring at me over their shoulders."
        "And the glare of sheer hatred in those eyes stops me dead."
        hide ayesha
        hide hanna
        with moveoutleft
        "So all I can do is stand there in silence."
        "Just stand there and watch them walk away."
        $ hanna.set_gone_forever()
        $ ayesha.set_gone_forever()
    return

label sporty_harem_event_01:
    scene expression f"bg {game.room}"
    show hanna casual
    "You know when people say that they just had a funny feeling about something they were about to do?"
    "That little doubt that just won't stop nagging at them, no matter how much they try to ignore it?"
    "Yeah, well, just to be clear - I have nothing like that when Hanna and I turn up at the Mall."
    "After all, this is just supposed to be a normal, run-of-the-mill date."
    "Nothing particularly fancy and certainly nothing heavy either."
    "And at least to begin with, that's just the way it plays out."
    "We wander from one place to another, dodging the crowds as best we can."
    "We chat about nothing in particular, and yet manage to mention everything in the process."
    "We discuss whether we should get ice-cream, but then settle for grabbing a coffee instead."
    "But it's while we're waiting in line to grab out espressos, latte's or whatever the hell we ordered."
    "That's when I just so happen to glance around and see a familiar face in one of the stores across the way."
    "It's a pretty modern and impressive store that sells sports-wear and all the stuff that comes along with it."
    "And while I was initially gazing at the expensive sneakers in the window, someone inside catches my eye."
    "Tall and built like a Greek goddess, it can only be Ayesha."
    "She's half turned away from me, but I can still see that she's dressed mostly in figure-hugging spandex."
    "Look, I know what you're thinking right now, okay?"
    "I get to stare at Ayesha's astonishing body all the time at the gym."
    "And I am out on a date with Hanna right now, so the rules say that I should only have eyes for her."
    "But it's not like I was looking to check out another girl, and I am just looking."
    hanna.say "Hey, [hero.name]."
    show hanna annoyed
    hanna.say "What's caught your eye, huh?"
    "Ah, shit - busted!"
    "Instinctively, I try to play if off as nothing at all."
    "Maybe if I play innocent, Hanna will just buy it and we can get on with our date?"
    mike.say "Ah, nothing's up, Hanna - nothing at all!"
    mike.say "I was...I was just..."
    mike.say "Checking out the shoes in that window...the ones over there."
    mike.say "Don't you think I could use some new sneakers?"
    "Hanna fixes me with an amused stare, cocking her head on one side with a crooked grin."
    "Every part of her is screaming bullshit right now."
    "Telling me that she sees straight through my lame excuses."
    show hanna normal
    hanna.say "Aw, come on, [hero.name]."
    hanna.say "You were checking something out."
    hanna.say "But it wasn't the shoes!"
    "As we grab our drinks and walk out of the coffee shop, Hanna's not about to let it drop."
    "I can tell that she's enjoying the chance to watch me squirm."
    "And so the best I can hope is to be apologetic and ride it out."
    "Maybe throw in some ashamed compliments along the way to salve Hanna's pretty large ego too."
    "But then Hanna stops in her tracks, pointing into the store in question."
    show hanna annoyed
    hanna.say "Wait a minute, is that who you were eyeballing just now?"
    mike.say "Erm...I'm not sure, Hanna..."
    mike.say "I didn't really see their face..."
    hanna.say "No way, that's Ayesha, I know it is!"
    "She turns her gaze on me, and I can see the jealousy flashing in her eyes as she does so."
    hanna.say "You were eyeing up that lumbering moose?!?"
    mike.say "Hanna, please..."
    "Before I can stop her, Hanna's marching towards the sports store."
    "I hurry after her, still hoping that I can somehow avert the impending confrontation."
    "Once inside, Hanna walks straight up to Ayesha, who still has her back turned to us."
    "Putting a hand on the other girl's shoulder (which is something I note she has to reach up do), she spins her around."
    show hanna normal at right5
    show ayesha casual annoyed at left5
    with dissolve
    ayesha.say "Hey...what the hell?!?"
    ayesha.say "Oh, Hanna, it's you - what's up?"
    show ayesha normal
    "As Hanna opens her mouth, undoubtedly to say something hostile, I manage to impose myself between them."
    mike.say "Hi, Ayesha."
    mike.say "We were just passing and happened to see you in here."
    mike.say "Seemed rude not to take a second out to say hello."
    "I see recognition dawn on Ayesha, as her brain makes sense of what's happening to her."
    "Rather than her boss striding up to her out of the blue, it now looks like what it is."
    "And that's just some people she knows bumping into her randomly at the Mall."
    ayesha.say "Oh, sure..."
    ayesha.say "Nice to see you guys."
    "She gestures around where she's standing, an awkward smile on her face as she does so."
    show ayesha blush
    ayesha.say "I was just, you know - shopping for a couple of things..."
    "For the first time it dawns on me just why Ayesha is so uncomfortable."
    "She's standing in front of us, dressed just in spandex and running shoes."
    "Sure, she might do the same at the gym, but that's what she does for a living."
    "Here she seems so much more shy and aware of just how exposed she is."
    "My heart kind of goes out to her in that moment."
    "But I'm also a little guilty at how hot Ayesha's shyness makes her seem..."
    hanna.say "Must be hard, you know?"
    show hanna annoyed
    hanna.say "Trying to find all of this stuff in men's sizes?"
    "The comment is delivered in a catty, mean manner and changes the mood of the encounter entirely."
    show ayesha angry
    ayesha.say "I'm sorry, but WHAT did you just say?!?"
    hanna.say "You heard me, Ayesha."
    hanna.say "I mean sure, this stuff stretches."
    hanna.say "But there's a limit to how much testosterone it can hide!"
    ayesha.say "Why you...you skinny little bitch!"
    ayesha.say "If I didn't need that lousy job so much, I'd..."
    hanna.say "You'd what, Ayesha?"
    show hanna angry
    hanna.say "Say it, and I promise that I won't make Daddy fire you."
    "This is getting quickly out of hand."
    "And I'm worried that they'll actually come to blows in the middle of the store."
    mike.say "Girls, this is stupid."
    mike.say "What are you even arguing about?"
    hanna.say "We're arguing about why anyone would even look twice at this heifer, that's what!"
    ayesha.say "Oh, so that's what this is all about, is it?"
    ayesha.say "[hero.name] looked my way and you're scared he wants a woman with more substance than skank!"
    hanna.say "Ooh, you bitch!"
    hanna.say "That's it, there's only one way to settle this!"
    mike.say "Erm...there is?"
    hanna.say "We both buy swimsuits, and we let [hero.name] decide who he likes best!"
    ayesha.say "Challenge accepted!"
    mike.say "Huh...wait...what?!?"
    "Before I as much as raise any objections that I might have, they're both striding off the swimwear aisle."
    "And all I can do is follow in their wake, wondering how the situation managed to escalate so quickly."
    "It's not until a little while later that a rather obvious realisation starts to dawn on me."
    "Which is that if I play this thing right, it could turn out to be a hell of a lot of fun for me..."
    $ hero.replace_activity()
    $ game.active_date.score = 50
    $ game.active_date.stay = False
    $ game.room = "bedroom1"
    call sporty_harem_swimsuit_contest from _call_sporty_harem_swimsuit_contest
    return

label sporty_harem_swimsuit_contest:
    show bg bedroom1
    "It's a pretty weird feeling, watching Ayesha and Hanna as they jealously stalk the racks for a new swimsuit each."
    "And then being hustled back to my place so that they can put them on and make a contest out of parading around in them."
    "Even as I'm practically driven down the stairs and into my bedroom, it all still feels rather strange and surreal."
    show hanna casual at top_mostright
    show ayesha casual at center
    with dissolve
    "Under normal circumstances, just the thought of seeing either of them in a swimsuit would be enough to get me hot."
    "But somehow the fact that it's all been turned into an impromptu competition makes it hard for the reality to sink in."
    show hanna casual at right5
    show ayesha casual at left4
    with ease
    "Hanna closes the door behind us and leans on it too for good measure."
    "At the same time, Ayesha marches me to the bed and forces me to sit down on it."
    ayesha.say "Park your ass right there, mister."
    ayesha.say "And don't even think of moving until we've got this over with!"
    "Despite the fact that they seem to be bitter enemies at this moment in time, Hanna nods in agreement."
    hanna.say "Yeah, [hero.name] - you do that."
    hanna.say "After all, we're not doing this for your benefit, you know?"
    "Seriously?!?"
    "They're two grown women that are about to put on swimsuits and strut up and down in front of me."
    "And after that, they expect me to tell them which one looks better than the other."
    "I can't begin to imagine the hell else this could benefit..."
    "But not wanting to ruin the prospect of the show I've been promised, I'm sure to play along."
    "So I nod to each of them in turn."
    mike.say "Okay, Hanna."
    mike.say "Okay, Ayesha."
    mike.say "I'll do my best not to enjoy myself..."
    "Luckily for me, that seems to do the trick, and neither of them notices the growing amusement in my voice."
    "Maybe because neither of them is really paying that much attention to what I said after agreeing with them."
    "And so I end up sitting there on the bed, watching in sheer amazement as they get started."
    "Both Ayesha and Hanna waste no time in thrusting a hand into the bags that hold their newly purchased swimsuits."
    "But then, almost as one, they look up and glare at me, as if I've managed to screw up just sitting in silence."
    hanna.say "No peeking, [hero.name]!"
    ayesha.say "Yeah, shut your eyes until we tell you to open them again!"
    "Part of me wants to protest."
    "Yet I also don't want to break the spell and make them come to their senses."
    scene bg bedroom1 at blur(8), dark, dark with wipedown
    "And so I make a show of closing my eyes, acting like it's the last thing in the world I want to do."
    "Well, it's not a complete act, as I'd like to watch Ayesha and Hanna undress."
    "But I want to see them strutting their stuff once they're dressed even more!"
    hanna.say "Urgh...really?"
    ayesha.say "What's wrong now, Hanna?"
    hanna.say "Why are you watching me get undressed, you perv?"
    ayesha.say "I am NOT watching you!"
    ayesha.say "I'm just...checking you don't cheat, that's all."
    hanna.say "How am I going to cheat, Ayesha - use a body double or something?!?"
    "I try as best I can to keep a straight face as the two of them bicker and squabble."
    "But despite my best efforts, I guess that a smirk must have sneaked its way onto my lips."
    hanna.say "Hey, [hero.name], what gives?"
    ayesha.say "Is he...is he laughing at us?!?"
    "Thinking that I've been rumbled and it might be wise to apologise, I sneak one eye open."
    scene bg bedroom1
    show ayesha angry sexyswimsuit zorder 2 at left4
    show hanna a angry sexyswimsuit zorder 1 at right5
    with wipeup
    "And the moment that I see what's standing before me, I open the other as well to get a better look."
    "Ayesha and Hanna were as good as their word, both standing before me in their swimsuits."
    "They have disapproving looks on their faces, Hanna's hands on her hips and Ayesha's crossed over her chest."
    "But none of that can disguise the fact that they look simply stunning as they stand there."
    "I shake my head and rub my eyes in order to make sure that I'm seeing this as best I can."
    ayesha.say "What's the matter, [hero.name]?"
    hanna.say "Is...is there something wrong?"
    "Shake my head hastily, trying to assure them that everything's just fine."
    mike.say "No, no..."
    mike.say "You both look so..."
    mike.say "So amazing!"
    show ayesha blush
    "I see Ayesha instantly blush and turn away from me, as if she can't handle the compliment."
    show hanna happy
    "In contrast, Hanna seems to positively light up at the very same sentiment, smiling happily."
    hanna.say "Aww, that's so sweet of you to say, [hero.name]!"
    hanna.say "This is just something I grabbed off of the rack at random..."
    ayesha.say "You...you really mean that, [hero.name]?"
    ayesha.say "You think I look good in this?"
    "Not for the first time, I'm struck my the difference between these two girls."
    "The one soaking up praise like a sponge and the other bashful beyond belief."
    mike.say "I don't think I can go through with the competition, you guys."
    mike.say "Because I won't be able to choose between you!"
    "I fully expect Hanna to be the first one to speak up."
    "But when Ayesha opens her mouth to speak, we're all pretty surprised."
    "And from the look on her face as she does so, not least Ayesha herself!"
    ayesha.say "You...you don't have to - choose, that is..."
    ayesha.say "Maybe you could...have us...both?"
    show hanna mindless at startle
    "Hanna stares at Ayesha, her mouth hanging open in shock."
    "She looks to me and then back to Ayesha again, waiting for one of us to speak."
    ayesha.say "Well, it just seems dumb to keep fighting like this."
    ayesha.say "I'm cool with sharing - if you two are?"
    show hanna annoyed
    "I can't believe my luck right now - this just keeps getting better and better!"
    "But I sense the need to play it cool, or else I could scare both Ayesha and Hanna off."
    "And so I nod slowly, making it look as much as I can like I need to think it over."
    "Even though I've already screamed yes a hundred times inside of my head!"
    mike.say "I'm cool with that, Ayesha."
    mike.say "So long as Hanna is too?"
    "Even as I say this, I can see the possibilities dawning on Hanna too."
    "Sure, she looks a little nervous, but I know that she's an exhibitionist at heart."
    "And this is just the kind of thing that'll make her feel daring and dangerous."
    "So it comes as no real surprise when she cocks her head on one side, trying to look nonchalant as she answers."
    show hanna flirt
    hanna.say "Yeah, sure."
    hanna.say "I mean, if that's what you guys are into."
    hanna.say "I was gonna suggest it myself anyway!"
    "I think that Ayesha and I both know she's bullshitting us."
    "But it's a welcome alternative to some stupid competition between them."
    mike.say "I'm sure this'll be great."
    mike.say "There's nothing we can't do, so long as we put our heads together."
    hanna.say "Speaking of head, that gives me an idea!"
    show hanna at center with ease
    "Hanna leans in to whisper something into Ayesha's ear, covering her mouth with her hand."
    "I can't tell what she's saying, but I see a grin form on the larger girl's face all the same."
    "Finally, Ayesha nods, and they seem to be ready to put into motion whatever plan they're been discussing."
    hanna.say "Take it all off, [hero.name], and then lie back."
    ayesha.say "We're the ones in charge from here, okay?"
    "I nod hastily, already tugging off my clothes as instructed."
    "My eagerness to obey earns nods and smiles from Ayesha and Hanna."
    show hanna topless at right4 with ease
    show ayesha topless
    "And they reward me a moment later by stripping off their swimsuits."
    show hanna naked
    show ayesha naked
    "They stand before me, naked looking like a couple of horny goddesses."
    "Then they get down on their hands and knees, beginning to crawl towards the foot of the bed."
    "Of course I immediately strain to see them as best I can, still trying to keep put as I was told to."
    "But when they're close enough to climb up and join me, Ayesha and Hanna suddenly throw me a curve ball."
    "Ayesha holds up the bedclothes so that Hanna can slip under them, and then follows herself."
    "This sends me scuttling back to the top of the bed, feeling those same sheets as I search for them."
    "I slide under the covers, just in time to feel two pairs of hands take hold of my heels."
    "Laid on my back, I lift the covers, just in time to see Ayesha and Hanna literally climbing up my body."
    "And it's not only their hands that I can feel now, as they lick, kiss and caress as they come."
    "Needless to say, by the time that they reach my waist I have an almost painful erection."
    "Which feels like a tent-pole, holding up the sheets until they shoulder up to it."
    "I can see both Ayesha and Hanna eyeing it with a real look of hunger in their eyes."
    scene sporty blowjob with fade
    if renpy.has_label("sporty_harem_achievement_2") and not game.flags.cheat:
        call sporty_harem_achievement_2 from _call_sporty_harem_achievement_2
    "And for a moment, I wonder if the apparent truce between the two girls will hold up to this."
    "But they surprise me once again, as Ayesha begins to kiss and suck at my balls."
    "Hanna leaves her to it, tracing a line up the shaft of my cock with her tongue instead."
    "The feeling of what they're doing to me is pretty amazing, as you can imagine."
    "And it's made that much more intense and memorable by the sight of them working together to pleasure me."
    show sporty blowjob hannabj
    "By the time Hanna's lips are wrapped around the head of my cock, she's practically salivating at the prospect."
    "The second it slides into her mouth, Ayesha sucks as hard as she can, taking my balls between her lips too."
    mike.say "Ah, shit..."
    mike.say "That feels..."
    mike.say "Ah..."
    "There's no way that I can get out the words that are on the tip of my tongue."
    show sporty blowjob hannabj hannacloseeyes
    "Being double-teamed by Ayesha and Hanna is just too much for my brain to handle!"
    "By now, Hanna's head is bobbing up and down with a vengeance."
    "And Ayesha's playing my balls like a finely-tuned musical instrument too!"
    "But then I feel the larger girl begin to use her lips to climb the shaft of my cock."
    "When she reaches the top, I fully expect Hanna to stay right where she is."
    "But, much to my surprise, she willingly releases me from her mouth and makes way for Ayesha instead."
    "Indeed, they switch positions and roles so smoothly that I hardly notice the change of pace!"
    show sporty blowjob ayeshabj hannaopeneyes
    "Now it's Ayesha that's taking my cock deep into her mouth."
    "And Hanna begins to make her way back down towards my balls, licking all the way."
    "I feel kind of bad for the fact that I'm almost ready to cum as soon as Ayesha's working my cock."
    show sporty blowjob ayeshabj ayeshacloseeyes
    "I don't know if Hanna was on the brink of getting me off before they swapped."
    "Or if Ayesha just managed to do something that pushed me over the edge that quickly."
    "But either way, I'm going to cum in the blink of an eye..."
    show sporty blowjob ayeshaopeneyes
    menu:
        "Cum in Ayesha's mouth":
            "I figure that it'll perhaps be some kind of consolation for not getting much time on my cock."
            "And so I keep myself right where I am as my orgasm finally overtakes me."
            with vpunch
            "This means that I cum straight into Ayesha's mouth, almost down the back of her throat."
            show sporty blowjob cum ayeshaopeneyes with vpunch
            "Not prepared in the slightest for me to be over so quickly, she gags and chokes on the mouthful."
            with vpunch
            "But all the same, she somehow manages to keep from succumbing to a coughing fit."
            show sporty blowjob cum ayeshasquirt
            "And she gamely gulps down each and every spurt of semen that pumps out of me."
            "Only when I'm done and my slackening cock slides out of her mouth does she hack and cough."
            "By which time I'm almost too far gone to be able to do anything about it."
        "Cum in Hanna's mouth":
            "I don't know what possesses me to do so, but for some reason I want to cum inside of Hanna's mouth alone."
            show sporty blowjob hannabj
            "And so, taking hold of Ayesha's head, I pull my cock out of her mouth and hastily thrust it towards the other girl."
            "Whether Hanna's on board with it or just opening her mouth to ask what's happening, I have no idea."
            "But either way, the outcome is the same, as its pushed straight back between her lips."
            with vpunch
            "Then end result is that I cum straight into Hanna's mouth, right down the back of her throat."
            show sporty blowjob cum hannaopeneyes with vpunch
            "Not prepared in the slightest, she gags and chokes on the mouthful of cum."
            with vpunch
            "Yet somehow she manages to keep from having a coughing fit as she does so."
            "Hanna swallows every spurt that comes shooting out of me."
            "And only when I'm spent and my cock slips out of her mouth does give in and actually start to cough."
            show sporty blowjob cum hannasquirt
            "By which time I'm almost too far gone to be able to do anything about it."
        "Cum on their faces":
            "This started as a competition and they're now getting on so well together."
            "So it seems crazy to do anything that would ruin that change of heart now."
            "Which is why I pull my cock out of Ayesha's mouth just before I actually cum."
            show sporty blowjob -ayeshabj cumshot with vpunch
            "My instant reward is their two faces, both looking up in evident surprise."
            with vpunch
            "And that means I can let myself go without any hint of concern for someone being left out!"
            with vpunch
            "When the semen comes shooting out of my cock, it spatters over both of them at the same time."
            "Ayesha and Hanna let out squeals of alarm as it splashes across their noses and cheeks."
            show sporty blowjob -cumshot dickcum
            "But that also means that they get a good portion of it in their open mouths as well."
            "Each seems as hungry for their share as the other, licking what's left off of my cock too."
            "And all of this happens as I sag back onto the bed, gasping with exhaustion."
    $ ayesha.sexperience += 1
    $ hanna.sexperience += 1
    $ ayesha.love += 2
    $ hanna.love += 2
    $ game.pass_time(2)
    return


label sporty_harem_event_02:
    scene bg gym
    "So, Ayesha and Hanna have agreed that we're going to be doing the threesome thing."
    "That means my life just got a whole lot simpler and much more fun, right?"
    "Well that's where you'd be wrong."
    "You see we agreed to get into a three-way relationship together."
    "But we never actually sat down and thrashed out how it was going to work."
    "Add into the equation the fact that Ayesha and Hanna are very different girls."
    "One of them is practically an exhibitionist."
    "And the other's painfully shy outside of a wrestling ring!"
    "On top of that, they also work in the same place on a daily basis."
    "And Hanna's the daughter of the owner, so she's technically Ayesha's boss!"
    "I'm sure that having two girlfriends instead of one isn't supposed to be like this."
    "None of the movies that I've seen on the subject dwell on the problems it causes!"
    "Like the first time that I head down to the gym after we've made it official."
    "All I want to do is have my usual work-out, that's all."
    "But the moment that I'm changed and on the gym floor, I start to get twitchy."
    "It's almost like I can sense there's something up, but I don't know just what."
    "But then I see Hanna."
    "And almost instantly I begin to figure out what's going on."
    show hanna at right with dissolve
    hanna.say "Hey there, handsome!"
    hanna.say "You here to work on those guns of yours, huh?"
    "For a moment I find it hard to look Hanna in the eye, let alone answer her question."
    "And that's not because I can't bring myself to look at her."
    "More like I can't tear my eyes away from what I see below her neck!"
    "I'll level with you here."
    "Hanna's always wearing something tight."
    "Or something revealing."
    "Or more likely both at once."
    "But right now she has on gym gear that would struggle to pass as a bikini!"
    mike.say "Y...yeah, Hanna..."
    mike.say "Something like that!"
    show hanna happy at center with ease
    "She smiles and starts to walk towards me."
    "But she does so in a manner that puts me in mind of a big cat stalking its prey."
    hanna.say "Why don't you come join my class?"
    hanna.say "I don't have any other people signed up yet."
    hanna.say "We could turn it into a special, private session!"
    ayesha.say "You're only thinking about working out one part of his body, Hanna!"
    ayesha.say "Forget her, [hero.name]."
    ayesha.say "I'll give you a class that'll work out your whole body!"
    hide hanna
    show ayesha
    with fade
    "At the sound of Ayesha's voice, I turn around to see her standing behind me."
    "And as soon as I see her, I'm as amazed as I was to see Hanna a moment before."
    "Ayesha's also wearing barely enough lycra to be considered fully dressed."
    "Her muscles bugle with every move she makes, and her breasts heave."
    "It's like an even bigger cat just showed up to challenge the first one!"
    mike.say "Girls..."
    mike.say "Girls, please..."
    show ayesha at left
    show hanna at right
    with moveinright
    mike.say "I'm just here for my usual work-out, that's all!"
    show hanna annoyed
    show ayesha annoyed
    "Both Hanna and Ayesha look instantly annoyed."
    "I think each of them was thinking I'd ditch them for the other."
    "So turning them both down is a serious swerve!"
    hanna.say "Whatever, [hero.name]!"
    show hanna annoyed
    hanna.say "You go play with yourself if that's what you want!"
    ayesha.say "Yeah, [hero.name]."
    show ayesha annoyed
    ayesha.say "I know when I'm not wanted!"
    hide ayesha at top_mostleft
    hide hanna at top_mostright
    with move
    "I shake my head as they turn and storm off in opposite directions."
    hide ayesha with moveoutleft
    hide hanna with moveoutright
    "They're probably going to make me pay for that later."
    "But I really do want to work-out in peace."
    "Luckily for me the gym is pretty quiet."
    "In fact, as I get into my work-out routine, I realise it's practically dead!"
    "No matter."
    "That just means that I don't have to wait for any of the machines!"
    "I get into my routine and pretty soon I'm zoning out as usual."
    "In fact, when I get on the treadmill, I actually close my eyes."
    "The only problem is that I can't stop thinking about Hanna and Ayesha."
    "Those outfits they had on - they looked so hot!"
    "I can feel my cock getting hard as I think about them."
    "If only I could stop running and do something about it."
    "It's then that I feel a spare hand slipping into my shorts."
    "A second later it's joined by another."
    "They start rubbing and stroking my cock."
    "But then my eyes pop open as I realise something."
    "I know where my hands are - so the ones in my shorts aren't mine!"
    mike.say "Hey?!?"
    mike.say "What the hell?!?"
    show hanna blush at center, zoomAt(1.5, (340, 1040)) with dissolve
    "I glance to the left and see Hanna."
    show ayesha blush at center, zoomAt(1.5, (940, 1040)) with dissolve
    "Then I glance to the right and see Ayesha."
    hanna.say "Calm down, [hero.name]."
    ayesha.say "Yeah, we've got everything in hand!"
    mike.say "Oh ha ha, very funny!"
    mike.say "What if somebody walks in on us, huh?"
    hanna.say "Don't worry, I closed the gym early."
    ayesha.say "The three of us are the only ones here."
    "I reach up and turn the treadmill off, but they don't let go of my cock."
    "To be honest, I'm glad they don't, as it's starting to feel really good."
    "Plus they're still in those hot outfits, and if we are actually alone..."
    mike.say "So what happened to change your moods?"
    mike.say "Just a couple of minutes ago you were ready to fight over me."
    hanna.say "Oh, forget about that."
    hanna.say "We were just being silly."
    ayesha.say "We realised that we needed to work together."
    ayesha.say "That way we're sure to get what we want."
    "Together they lead me off the treadmill by the cock."
    "And then they work in tandem to strip me off while undressing themselves too."
    scene bg black
    show sporty blowjob gym with fade
    "Soon enough I find myself sitting on the floor, flanked on either side."
    "Ayesha and Hanna get onto their hands and knees."
    "They lean over me, still working away at my cock."
    "But now they start to bring their mouths into play too."
    "I lean back against a conveniently placed yoga ball."
    "And I let them alone while they get to work."
    "It seems that Ayesha and Hanna really have agreed to cooperate."
    "They take it in turns swapping between sucking my balls and licking my shaft."
    "And they do so so smoothly that I have to be looking down to know who's doing what!"
    show sporty blowjob ayeshabj
    "It's Ayesha that takes it into her mouth first, making me gasp with pleasure."
    "She's doing so well that I'm almost disappointed when she hands over to Hanna."
    show sporty blowjob hannabj
    "But I soon find that the competitive urge hasn't vanished completely."
    "As Hanna does the best she can to out-perform Ayesha."
    show sporty blowjob ayeshabj
    "This little rivalry continues, but it doesn't seem to be getting out of hand."
    "So I'm happy to just lie back and reap the benefits for myself!"
    "It's about then that my eyes stray to Hanna's ass."
    "I watch as it wiggles from her head going up and down."
    show sporty blowjob hannabj
    "A quick glance in the opposite direction shows Ayesha's doing the same."
    show sporty blowjob hannafinger ayeshafinger
    "Intrigued I reach out a hand towards each."
    "At first I just stroke their buttocks and give then a little squeeze."
    "But the reaction from them both is so intense that I have to go further."
    show sporty blowjob ayeshabj ayeshacloseeyes
    "Ayesha and Hanna both nod and make almost desperate sounds at my touch."
    "They also seem to redouble their efforts."
    "Without pausing to think about it, I feel between their thighs."
    "And then I start to stroke their pussy."
    show sporty blowjob hannabj ayeshacloseeyes hannacloseeyes
    "Almost as one, Ayesha and Hanna begin to moan and pant."
    "Even with my cock in their mouths, I can still hear them!"
    "And as soon as one them passes it to the other, I hear them urging me on."
    show sporty blowjob hannabj sweat
    ayesha.say "Mmm..."
    ayesha.say "Oh yeah..."
    ayesha.say "Don't stop, [hero.name]..."
    show sporty blowjob ayeshabj
    hanna.say "That's right..."
    hanna.say "Oh fuck..."
    hanna.say "Make me cum..."
    "I smile at Hanna's last words."
    "That's the kind of challenge I like!"
    "But then I realise that she might have to wait in line."
    "Because I can feel myself starting to lose it!"
    menu:
        "Cum in Ayesha's mouth":
            with vpunch
            "My cock just happens to be inside of Ayesha's mouth when I cum."
            show sporty blowjob cum ayeshaopeneyes with vpunch
            "I see her eyes go wide with surprise, but there's no time to pull out."
            with vpunch
            "Ayesha coughs and splutters, but then I see determination flare in her eyes."
            show sporty blowjob cum ayeshasquirt
            "Somehow she masters the situation and swallows every drop I have to give."
            "Ayesha gulps down the semen without stopping until I'm totally spent."
            "Then she releases my cock, panting and gasping for breath."
        "Cum in Hanna's mouth":
            show sporty blowjob hannabj with vpunch
            "My cock just happens to be inside of Hanna's mouth when I cum."
            with vpunch
            "I see her eyes go wide with surprise, but there's no time to pull out."
            show sporty blowjob cum hannaopeneyes with vpunch
            "Hanna coughs and splutters, but I know that this isn't her first rodeo."
            show sporty blowjob cum hannasquirt
            "Soon enough she recovers to the point where she's swallowing hard."
            "Hanna doesn't spill a single drop as she gulps it down."
            "Then she releases my cock, panting and gasping for breath."
        "Double facial":
            "At the very moment my cock's about to pass from Ayesha to Hanna, it happens."
            show sporty blowjob -ayeshabj cumshot with vpunch
            "And as it's between them, both the girls get an equal share of the inevitable shower."
            with vpunch
            "Ayesha and Hanna cry out in alarm, raising their hands to shield their faces."
            show sporty blowjob -cumshot dickcum
            "But it's too little too late, as the warm, sticky cum stripes their cheeks."
            "Still reclining on the yoga ball, I smile as I watch it run downwards."
            "It reaches their lips and then dribbles from their chins."
            "Their faces still frozen in expressions of genuine surprise."
    "Afterwards everyone begins to gather up their clothes."
    scene bg gym
    show hanna naked sweat blush at right5
    show ayesha naked blush at left5
    with fade
    "I feel like I'm bathed in sweat, desperate for a shower."
    "And both the girls are positively glistening under the lights."
    mike.say "Well, I'm going to go hit the showers."
    mike.say "Shall I meet you guys out front when I'm done?"
    hanna.say "Why wait until then?"
    hanna.say "We could just shower together."
    mike.say "Erm..."
    mike.say "Don't you have male and female locker-rooms here?"
    hanna.say "Only when the place is full of customers."
    ayesha.say "And after what we just did, well..."
    ayesha.say "Showering together is nothing!"
    $ ayesha.sexperience += 1
    $ hanna.sexperience += 1
    $ ayesha.love += 2
    $ hanna.love += 2
    return

label ayesha_hanna_propose_male:
    "I kind of feel like I've been dating Ayesha and Hanna for that certain period of time."
    "Like when you know for sure you're well out of the first tentative stages of a relationship."
    "But you're also having a lot of fun, and it's not starting to feel old at all."
    "To me that's a great sign, like you've really managed to hit a sweet spot."
    "And that's exactly where I feel I am with Ayesha and Hanna right now."
    "Sure, there are the occasional moments when we don't see eye to eye."
    "But most of the time we spend together is pretty much the most fun I've ever had."
    "And believe me, I need to keep up my schedule at the gym."
    "Because they're two of the fittest girls imaginable too."
    "And as such, it takes a hell of a lot of stamina to keep them happy!"
    "In fact, our relationship is going so well that I want to make it official."
    "Not just because of the fact I could die a happy man in the bedroom with those two."
    "But also on account of the way that I find myself feeling whenever we're all together."
    "It just feels...right, that's all."
    "There's no other way that I can put it."
    "Which is why I have two matching rings in my pocket."
    "Now all I need is to choose the perfect moment to pop the question..."
    show ayesha angry at left5
    ayesha.say "Hanna!"
    ayesha.say "Will you please stop that?"
    show hanna at right5, startle
    show fx question at right5
    hanna.say "Huh?"
    hanna.say "Stop what?"
    hide fx
    ayesha.say "You know damn well what!"
    ayesha.say "Comparing the size of your butt to mine!"
    show hanna flirt
    hanna.say "I was not!"
    ayesha.say "Yes you were!"
    mike.say "Ahem..."
    show ayesha normal
    show hanna normal
    "As one, Ayesha and Hanna turn towards me."
    "And then they look down to see me kneeling in front of them."
    "Before they can open their mouths to speak, I do it."
    mike.say "Ayesha..."
    mike.say "Hanna..."
    mike.say "Will you marry me?"
    if ayesha.love >= 195 and hanna.love >= 195:
        show ayesha mindless at startle
        show hanna mindless at startle
        show fx exclamation as exclaleft at left5
        show fx exclamation as exclaright at right5
        "The pair of them have looks of complete surprise on their faces."
        "And I can't help thinking that they're going to keep me waiting for an answer."
        show ayesha happy
        show hanna happy
        "But much to my surprise, those expressions suddenly turn into beaming smiles."
        hanna.say "WOW!"
        hanna.say "[hero.name] - I thought you'd never ask!"
        show hanna flirt
        hanna.say "Way to keep a girl hanging on!"
        ayesha.say "Are you kidding, [hero.name]?!?"
        ayesha.say "Of course I will!"
        ayesha.say "I'd love to marry you!"
        "Now they're both thrusting their hands at me."
        "So I hurry to slide the rings onto their fingers."
        "Getting back to my feet, I can hardly believe what's happening."
        mike.say "Oh man..."
        mike.say "You both said yes!"
        mike.say "You really want to marry me!"
        show hanna happy
        "Ayesha and Hanna share a smile and a shake of the head."
        "Then they grab me in a pretty ferocious bear-hug."
        "Which only serves to make me feel even happier than before."
        $ ayesha.set_fiance()
        $ hanna.set_fiance()
    elif ayesha.love >= 195 and hanna.love < 195:
        show ayesha happy
        ayesha.say "Are you kidding, [hero.name]?!?"
        ayesha.say "Of course I will!"
        ayesha.say "I'd love to marry you!"
        show hanna sad
        hanna.say "Oh god..."
        hanna.say "Why did you have to ask me that, [hero.name]?"
        hanna.say "I can't marry you - I have the gym to manage!"
        "For a moment, Ayesha and I are all smiles and happiness."
        show ayesha sad
        "But then the reality of what Hanna just said sinks in."
        mike.say "Are you serious, Hanna?"
        mike.say "You can't handle the gym and being married to us?"
        ayesha.say "Yeah, Hanna - what's the problem?"
        ayesha.say "[hero.name] and I can help to make it work."
        "Hanna listens to our arguments."
        "But then she shakes her head."
        hanna.say "Thanks, but no thanks."
        hanna.say "I need to focus on one thing."
        hanna.say "In fact, right now I feel like I need some space to think."
        hide hanna with moveoutright
        "Ayesha and I watch as Hanna turns and walks away."
        "I have no idea where we go from here."
        show ayesha normal
        "But it's a great comfort to feel Ayesha hugging me as we watch her go."
        $ ayesha.set_fiance()
        $ hanna.love -= 25
        $ hanna.sub -= 25
    elif ayesha.love < 195 and hanna.love >= 195:
        show hanna happy
        hanna.say "WOW!"
        hanna.say "[hero.name] - I thought you'd never ask!"
        show hanna flirt
        hanna.say "Way to keep a girl hanging on!"
        show ayesha sad
        ayesha.say "Oh, [hero.name]..."
        ayesha.say "I'm flattered, but I can't get married."
        ayesha.say "Not when my fighting career's in full swing!"
        "For a moment, Hanna and I are all smiles and happiness."
        show hanna sad
        "But then the reality of what Ayesha just said sinks in."
        mike.say "Are you serious, Ayesha?"
        mike.say "You can't handle your career and being married to us?"
        hanna.say "Yeah, Ayesha - what's the problem?"
        hanna.say "[hero.name] and I are always going to be in your corner."
        "Ayesha listens to our arguments."
        "But then she shakes her head."
        ayesha.say "Thanks, but no thanks."
        ayesha.say "I need to focus on my fighting spirit."
        ayesha.say "In fact, right now I feel like I need some space to think."
        hide ayesha with moveoutleft
        "Hanna and I watch as Ayesha turns and walks away."
        "I have no idea where we go from here."
        show hanna normal
        "But it's a great comfort to feel Hanna hugging me as we watch her go."
        $ hanna.set_fiance()
        $ ayesha.love -= 25
        $ ayesha.sub -= 25
    elif ayesha.love < 195 and hanna.love < 195:
        show fx exclamation at left
        show fx exclamation at right
        "Ayesha and Hanna stare at me in complete amazement."
        "But then I notice that they're both shaking their heads."
        show ayesha sad
        show hanna sad
        "And that can't be a good thing."
        hanna.say "Oh god..."
        hanna.say "Why did you have to ask me that, [hero.name]?"
        hanna.say "I can't marry you - I have the gym to manage!"
        ayesha.say "Oh, [hero.name]..."
        ayesha.say "I'm flattered, but I can't get married."
        ayesha.say "Not when my fighting career's in full swing!"
        "Suddenly I feel like I've been slapped in the face."
        "Well, that and as if my guts have been ripped out too."
        "Slowly I put the rings away and get back to my feet."
        mike.say "Oh..."
        mike.say "Okay..."
        mike.say "I guess it was a dumb idea anyway!"
        show ayesha normal
        show hanna normal
        "Ayesha and Hanna both smile and nod."
        "I know they're trying to make me feel better about being rejected."
        "But I think it's going to take time for these wounds to heal."
        $ ayesha.love -= 25
        $ ayesha.sub -= 25
        $ hanna.love -= 25
        $ hanna.sub -= 25
    return

label ayesha_hanna_male_ending:

    if renpy.has_label("sporty_harem_achievement_3") and not game.flags.cheat:
        call sporty_harem_achievement_3 from _call_sporty_harem_achievement_3
    $ game.hour = 16
    $ game.room = "church"
    scene bg church wedding with fade
    "I've got to admit something before we get into this."
    "I've pretty much lived in the gym in the weeks before the wedding!"
    "And I even chose a suit for the big day that shows off my efforts."
    "But can you really blame me for wanting to look good on the big day?"
    "Especially when I'm marrying a pair of girls like Ayesha and Hanna!"
    "I mean, they practically live in the gym."
    "So I feel like I'd be letting them down if I wasn't in prime condition too."
    "And well...maybe I want to be getting some of the admiring looks for a change!"
    "So that's why I'm standing at the altar, feeling pretty weird about the whole thing."
    "I keep on looking over my shoulder at the assembled guests too."
    "Of course I recognise all of my own friends and family."
    "But there's a whole bunch of people I don't as well."
    "And it feels like all of them are buff and glowing with health!"
    "I guess most of Hanna's guests are members of her gym too."
    "And Ayesha must have invited more than a few of her wrestling buddies as well!"
    "Suddenly the chapel fills with music and the mood instantly changes."
    "Now everyone's looking over their shoulders too."
    "All of us craning our necks to catch a glimpse of Ayesha and Hanna."
    show ayesha happy wedding at left5
    show hanna happy wedding at right5
    with dissolve
    "Then I see them!"
    "And it was worth the wait."
    "I know that Hanna's always been fond of having all eyes on her."
    "But right now I don't see how anyone could possibly be looking elsewhere."
    "Every move she makes sends a shiver through me, she looks so good."
    "Her dress is perfect too, accentuating her body in a subtle manner."
    if hanna.is_visibly_pregnant:
        "And even her pregnant belly looks amazing."
        "Somehow fitting in with her stunning form."
    "Then I manage to tear my eyes away from Hanna and check out my other bride."
    "And Ayesha takes my breath away in equal measures."
    "Where Hanna's fit, Ayesha's statuesque, a real Amazonian goddess!"
    "I'm so used to seeing her in spandex, that this is almost like a revelation."
    "And she's walking with utter confidence, striding down the aisle."
    if ayesha.is_visibly_pregnant:
        "It almost makes sense to glance down and see that Ayesha's pregnant too."
        "Like she's a goddess of fertility or something crazy like that!"
    "I must be grinning like a fool when they reach the altar."
    show ayesha happy at zoomAt (1.8, (350, 1275))
    show hanna happy at zoomAt (1.8, (1000, 1275))
    "Because I can see Ayesha and Hanna giggling as they exchange glances."
    show hanna blush
    hanna.say "Like what you see, honey?"
    ayesha.say "Because you can see even more later!"
    "Priest" "Ahem..."
    show ayesha normal
    show hanna normal
    "It's my turn to crack a wry grin as the priest coughs."
    "Ayesha and Hanna look mortified as he does so."
    "And they both hurry to take up their respective positions."
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To join these three people in the bonds of holy matrimony..."
    "We must have walked through the ceremony a hundred times."
    "So I'm almost on auto-pilot as we finally do it for real."
    "The only thing that stands out to me is when we exchange vows."
    "Priest" "Do you, Ayesha..."
    "Priest" "Take these people..."
    "Priest" "To be your lawful, wedded partners?"
    show ayesha happy
    ayesha.say "I do."
    "Priest" "And do you, Hanna..."
    "Priest" "Take these people..."
    "Priest" "To be your lawful, wedded partners?"
    show hanna happy
    hanna.say "I do."
    "Priest" "And finally, do you, [hero.name]..."
    "Priest" "Take these people..."
    "Priest" "To be your lawful, wedded partners?"
    mike.say "I do."
    "The priest nods and looks to the assembled guests."
    "Priest" "I call upon those here present..."
    "Priest" "That if they know of any reason why these people should not be married..."
    "Priest" "Speak now, or forever hold your peace."
    show ayesha normal
    show hanna normal
    "There's the usual awkward silence and laughter."
    "And I make a point of looking at Ayesha's wrestling buddies."
    "Because if anyone's going to pull some weird, theatrical bullshit, it's them!"
    "But thankfully, everyone behaves themselves."
    "Priest" "Very well."
    "Priest" "It is my great pleasure to declare you married."
    "Priest" "You may show your affection for each other in a manner of your choosing."
    show ayesha happy
    show hanna happy
    "Ayesha and Hanna don't hold back for a moment."
    hide ayesha
    hide hanna
    show ayesha kiss wedding
    with fade
    $ ayesha.flags.kiss += 1
    "And I find myself wrapped in their arms."
    "There are kisses and hands everywhere."
    "Some of them even squeezing my ass!"
    hide ayesha
    show hanna kiss wedding
    with fade
    $ hanna.flags.kiss += 1
    "But that's not something I'm going to complain about."
    "Because I just married the two most beautiful girls in the world."
    "And out life together starts right here and now."

    show sporty harem ending with fade
    hanna.say "So how is this supposed to work?"
    hanna.say "We just talk about what it's like living with [hero.name]?"
    ayesha.say "I guess so, Hanna."
    ayesha.say "We should probably try to be honest too."
    ayesha.say "You know, not sound like we're sugar-coating things?"
    hanna.say "Oh, don't worry about that."
    hanna.say "We've been putting up with him way too long!"
    ayesha.say "Yeah, yeah..."
    ayesha.say "But don't make it sound like he's a nightmare either."
    ayesha.say "I've got a lot of good things to say about him."
    ayesha.say "Like he was one of the few guys that was into me for me, you know?"
    ayesha.say "He wasn't put off by me being taller and more ripped than him."
    hanna.say "Ha!"
    hanna.say "That wouldn't have been hard before he stated working out at my gym!"
    ayesha.say "I'm serious, Hanna!"
    ayesha.say "All my life I had guys either scared off by my size."
    ayesha.say "Or else they were just creeps that wanted me to stretch them!"
    hanna.say "Urgh..."
    hanna.say "Don't start on the creeps!"
    hanna.say "So many of those at the gym."
    hanna.say "It's so hard to get them to stop looking at you."
    hanna.say "And to get the right guys doing it instead."
    ayesha.say "Like [hero.name]?"
    hanna.say "Well...yeah, Ayesha."
    hanna.say "I always wanted to keep fit and look good."
    hanna.say "And I like it when that gets me attention."
    hanna.say "But I always felt like [hero.name] saw more than that."
    ayesha.say "I don't think how good you looked ever put him off!"
    hanna.say "Of course not!"
    hanna.say "It's just that I never felt like I had to flaunt myself for him."
    hanna.say "You know what I mean?"
    ayesha.say "I do, I do..."
    ayesha.say "It's like he gives us space to be who we want to be."






    if not hanna.flags.gymSolution == "sell":
        hanna.say "I hear you, Ayesha."
        hanna.say "Like how he was behind me when I decided to keep working at the gym."
        ayesha.say "That's it exactly, Hanna."
        ayesha.say "He respected your decision and backed you up."

















    hanna.say "I suppose it is pretty weird though."
    hanna.say "You know, how things have turned out for us?"
    ayesha.say "Hmm..."
    ayesha.say "I certainly never thought I'd meet my life-partners at work!"
    ayesha.say "But I guess you just can't predict stuff like that."
    if not ayesha.is_visibly_pregnant and not hanna.is_visibly_pregnant:
        hanna.say "Hey, you know what...!"
        hanna.say "We're a family now."
        hanna.say "So maybe we should think about some new additions?"
        ayesha.say "Strange you should mention that, Hanna."
        ayesha.say "I was thinking the same thing."
        ayesha.say "We should talk to, [hero.name] about it."
        hanna.say "Or we could just surprise him!"
    if ayesha.is_visibly_pregnant:
        ayesha.say "Because I know that I couldn't have predicted being a mom!"
        ayesha.say "And I never thought my kid would be as perfect as Abigail is."
        hanna.say "You can say that again, Ayesha."
        hanna.say "She's a total delight!"
    if hanna.is_visibly_pregnant:
        hanna.say "[hero.name] Junior certainly took me by surprise."
        hanna.say "And he's never let me catch a breath since he was born!"
        ayesha.say "You can say that again, Hanna!"
        ayesha.say "He's a little tearaway!"
    ayesha.say "I think we can both admit that we got lucky."
    ayesha.say "That [hero.name]'s a pretty great husband."
    hanna.say "Yeah, I guess so."
    hanna.say "But don't go telling him that!"
    ayesha.say "Don't worry - I won't!"
    scene bg black with dissolve
    pause 1.0
    $ game.set_new_game_plus()
    $ renpy.full_restart()
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
