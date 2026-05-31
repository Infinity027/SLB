
label ryan_belly_interaction_female:
    $ ryan.set_flag("interact", 1, 1, "+")
    show ryan at center, zoomAt(1.5, (640, 1040))

    menu:
        "Kiss my belly":
            call ryan_belly_kiss_female from _call_ryan_belly_kiss_female_1
        "Caress my belly":
            call ryan_belly_caress_female from _call_ryan_belly_caress_female_1
        "Listen to the baby":
            call ryan_belly_listen_female from _call_ryan_belly_listen_female_1
        "Never mind":
            pass
    return

label ryan_belly_caress_female:
    show ryan normal at center, zoomAt(1.5, (640, 1040))
    "I'm just engaged in an act that feels like it's becoming all to common these days."
    "And that's the act of trying to haul my huge belly along with me and not look like a whale."
    "So who absolutely has to show up at this exact moment in time?"
    "You want to take a guess?"
    show ryan smile
    ryan.say "Good morning, [hero.name]..."
    ryan.say "You're looking positively vibrant today."
    show ryan normal
    "The very sound of Ryan's voice is enough to make me want to groan out loud."
    "Because I can almost feel him starting to judge me before I've even set eyes on him."
    "But all I can do is take a deep breath, hold it for a moment, and then let it out."
    "Preparing myself for the task of dealing with his bullshit."
    bree.say "Aaah..."
    bree.say "Hey there, Ryan..."
    bree.say "Nice to see you too."
    bree.say "And you can save the niceties too, because I know how I look, okay?"
    show ryan blank
    "Ryan frowns at me, like he has no idea what I'm talking about."
    show ryan whining
    ryan.say "I really don't understand, [hero.name]..."
    ryan.say "Whatever are you talking about?"
    show ryan normal
    bree.say "Oh come on, Ryan..."
    bree.say "I'm bloated, sore and cranky!"
    show ryan smile
    "Ryan chuckles and shakes his head, dismissing my words at a stroke."
    "And I'm right on the verge of telling him to shove it."
    "But that's when he does that thing he does."
    "This time it involves leaning in and putting a hand on my belly."
    "He doesn't ask for permission, oh no - he just puts it right there."
    "And then he proceeds to stroke my belly and smile at me."
    show ryan smile
    ryan.say "Oh, [hero.name]..."
    ryan.say "That's such a load of nonsense!"
    ryan.say "You look beautiful right now, glowing with health."
    ryan.say "Pregnancy really suits you, I hope you realise that?"
    ryan.say "In fact, I don't think you've ever looked so good."
    show ryan normal
    "Urrgh...he's doing it again."
    "Being so charming and nice, even when I know it's all his patter."
    "But I don't know if Ryan's just that good at winning women over."
    "Or else I'm in a more vulnerable state on account of being full of hormones."
    "Either way, I find my mood totally changing."
    "Just like that, I'm smiling and fluttering my eyelids."
    "Completely falling for Ryan's charms again."
    "Man, I swear that this guy is the devil himself!"
    $ ryan.love += 2
    return

label ryan_belly_kiss_female:
    show ryan smile at center, zoomAt(1.5, (640, 1040))
    ryan.say "[hero.name]..."
    ryan.say "Would you do me the honour of letting me kiss you?"
    show ryan normal
    "Ryan's question comes as a bit of a surprise."
    "And that's because I'm not used to being asked for a kiss in such a manner."
    "Sure, it's polite and even a little charming."
    "But it's also so formal and practiced."
    "Which is something that always seems to set off alarm bells in my head."
    bree.say "I guess so, Ryan..."
    bree.say "Since you asked so nicely."
    show ryan smile
    "Ryan nods and smiles at this."
    "Then he walks over to me, and I prepare myself for a passionate kiss."
    "But just as I have my lips all puckered up and ready for him, Ryan throws me a curveball."
    show ryan at center, traveling(2.5, 0.3, (640, 1940))
    "And that's because he suddenly kneels down in front of me."
    "And before I can say a word, he lifts up my top."
    "The next thing I know, his lips are planted on my belly."
    "I open my mouth, meaning to tell him off."
    "Or at the very least to demand that he tell me what he thinks he's doing."
    "But the words die in my throat as I feel the sensation of it spreading trough me."
    "Ryan's lips are so soft, his touch so gentle..."
    "Damn it, I feel like I'm being lifted off my feet and into the air!"
    "That's why I find myself unable to do anything but simply stand there."
    "And it's not like Ryan just plants a couple of pecks on there and then calls it day."
    "Oh no, he makes it his task to kiss every inch of my belly while he's down there."
    "Something that makes me begin to feel like a queen being adored upon her throne."
    "Before I was going to tell him that I wanted him to stop."
    "But now I'm on the verge of telling him off if her misses a spot."
    "Then demanding that he goes around again to make up for the error."
    "And all the time I'm also thinking that this is how I got here in the first place."
    "I'm pregnant and swelling to the size of a whale because of this same guy."
    "Yet here he is, wrapping me around his little finger all over again."
    "But all I can do is stand here, sighing and enjoying the sensations."
    "Unable to muster the strength to say no."
    $ ryan.love += 3
    return

label ryan_belly_listen_female:
    show ryan normal at center, zoomAt(1.5, (640, 1040))
    bree.say "Ooh..."
    bree.say "Hello..."
    bree.say "Someone's a bit lively today!"
    "I'm holding onto my belly and looking down at it as I say all of this."
    "So when I look up, I can't help jumping a little, as Ryan's suddenly right there."
    show ryan smile
    ryan.say "You mean the baby, right?"
    ryan.say "They're moving around more than usual?"
    show ryan normal
    "I can't help backing off a little, just enough to feel comfortable."
    "And only then do I feel like I can answer Ryan's questions."
    bree.say "Erm..."
    bree.say "Yeah, Ryan..."
    bree.say "They're really going for it today!"
    "Ryan nods, looking at my belly with obvious interest."
    show ryan smile
    ryan.say "You mind if I take a listen myself?"
    ryan.say "I've always been curious as to what you can hear."
    ryan.say "And this seems like the perfect chance to do it."
    show ryan normal
    "I think about it for a moment."
    "But there doesn't seem to be anything wrong with the idea."
    "So I shrug and pull up my top."
    bree.say "Sure thing, Ryan..."
    bree.say "Here you go."
    "Ryan only pauses long enough to give me a nod."
    show ryan at center, traveling(2.5, 0.3, (640, 1940))
    "And then he leans in close to my belly, putting an ear to the curve."
    "At first he seems to be frowning a lot, and moving his ear around too."
    "So much so that I think he's going to call it quits any moment."
    "But then the expression on his face changes, and his mood seems to improve."
    show ryan smile
    ryan.say "There you are!"
    ryan.say "[hero.name], I found the little bugger!"
    show ryan normal
    "I lean as far forwards as I can, straining to see what Ryan's doing."
    "And I make sure to keep quiet too, as he's already relating all of it to me."
    "In the end, it's nothing that's going to change the world for the better."
    "Just his random observations and attempts to interpret what he's hearing."
    "But on a deeper level, this all feels quite important."
    "Because it's the first time that we've all interacted as a unit."
    "Ryan listening to the baby and me hearing all that he has to say."
    "An it might sound silly, but I choose to take that as the start of something."
    "Something that's big and will soon come to have a real meaning for us all."
    $ ryan.love += 4
    return

label ryan_ice_cream_reaction_female:
    "We're walking along, enjoying a moment of comfortable silence."
    "And that's when I spot the ice-cream stand up ahead."
    if hero.morality >= 25:
        bree.say "Ooh, Ryan...would you like an ice-cream?"
    elif hero.morality <= -25:
        bree.say "Mmm...I want to lick something tasty in public - like an ice-cream!"
    else:
        bree.say "I don't know about you, Ryan, but I sure could go for an ice-cream."
    "The suggestion seems to catch Ryan a little off-guard."
    "Like the thought never occurred to him until I mentioned it."
    if ryan.sub >= 50:
        ryan.say "Oh yeah, [hero.name] - that's a great idea!"
    elif ryan.sub <= -50:
        ryan.say "So long as you choose a low-fat one, [hero.name] - a second on the lips, but a lifetime on the hips!"
    else:
        ryan.say "Yeah, [hero.name] - I could go for one of those."
    "Keen to capitalise on his enthusiasm, I steer Ryan over to the ice-cream stand."
    "And within no more than few minutes, we're happily licking away."
    "At the ice-creams - obviously I mean we're licking at the ice-creams!"
    return

label ryan_ask_phone_female:
    "I really want to make sure that I get Ryan's phone number before he leaves."
    "Because once I have it, then I can get hold of him any time that I please."
    "But the problem is that I have to make the whole thing look totally innocent."
    "After all, I don't want anyone to suspect there's something going on between us."
    if hero.morality >= 25:
        bree.say "Oh, Ryan, I wanted to send you a message about something!"
        bree.say "But I remembered that I don't have your number - so could I get it?"
    elif hero.morality <= -25:
        bree.say "Hey, Ryan - could I get your number?"
        bree.say "Sam wanted me too clue you in on a position she's into!"
    else:
        bree.say "I'd like to call you about something, Ryan..."
        bree.say "But I don't have your number - so what is it?"
    if hero.charm >= 20 - ryan.love:
        $ hero.smartphone_contacts.append("ryan")
        "Ryan looks surprised at the question, already pulling out his phone."
        "As if he's going to tell me his number without any more prompting."
        "And as he does so, I do the best I can to hide my enthusiasm."
        if ryan.sub >= 50:
            ryan.say "Of course you can have it, [hero.name]..."
            ryan.say "Here you go!"
        elif ryan.sub <= -50:
            ryan.say "You can have my number, [hero.name]..."
            ryan.say "But it's probably best if I call you."
        else:
            ryan.say "You mean you don't have it already?"
            ryan.say "Well we can soon fix that!"
    else:
        $ ryan.love -= 1
        $ ryan.sub -= 1
        "Ryan looks like the question is something that he was expecting."
        "And I note, with much disappointment, that he doesn't take out his phone."
        "Both of which are probably bad signs from my perspective."
        if ryan.sub >= 50:
            ryan.say "Oh no, [hero.name], I can't let you have it."
            ryan.say "People might get the wrong idea about us!"
        elif ryan.sub <= -50:
            ryan.say "Nice try, [hero.name]!"
            ryan.say "But you're not the first girl to want my number, and you won't be the last."
        else:
            ryan.say "I don't think so, [hero.name]..."
            ryan.say "There's really nothing you need to call me about."
    return

label ryan_ask_birthday_female:
    "I want to start getting to know Ryan better, getting to know more things about him."
    "And where better to start than by knowing the date of his birthday?"
    "That's the kind of thing a person's friends almost always know about them."
    "And it could be the first step on the path to knowing a whole lot more too."
    if hero.morality >= 25:
        bree.say "Ryan, I was just wondering..."
        bree.say "When is your birthday?"
    elif hero.morality <= -25:
        bree.say "You just have to be a Scorpio, right?"
        bree.say "Like, totally passionate and hot-blooded!"
    else:
        bree.say "Oh yeah, Ryan, I meant to ask..."
        bree.say "When is your birthday?"
    if ryan.love >= 50:
        "Ryan looks like the question's totally thrown him for a moment."
        "But at the same time I can see that he's flattered by the attention."
        "Which means I'm almost certainly going to get an answer out of him."
        if ryan.sub >= 50:
            ryan.say "What the...didn't I tell you already?"
            ryan.say "I'm sorry, [hero.name] - here's the date."
        elif ryan.sub <= -50:
            ryan.say "Huh, you really want to know that badly?"
            ryan.say "Here you go, [hero.name]."
        else:
            ryan.say "If you want to know that badly, [hero.name]..."
            ryan.say "Here's the date."
        $ ryan.flags.birthdayknown = True
        $ ryan.love += 1
    else:
        "Ryan looks a little surprised to hear me ask the question out of nowhere."
        "But the surprise on his face is soon replaced by a knowing smile."
        "And when he shakes his head too, I know that I'm not getting the answer I wanted."
        if ryan.sub >= 50:
            "Oh no, [hero.name] - I can't tell you that."
            ryan.say "That's sensitive personal information!"
        elif ryan.sub <= -50:
            ryan.say "I don't think I'll be telling you that, [hero.name]."
            ryan.say "I like to keep my personal information just that - personal!"
        else:
            ryan.say "Nice try, [hero.name], but I'm not telling."
            ryan.say "A guy's got to keep some mystery about him!"
        $ ryan.love -= 1
    return

label ryan_offer_a_drink_female:
    "I stand up, waving my glass in the air to show that it's empty."
    if hero.morality >= 25:
        bree.say "Looks like it's my turn to but the drinks."
        bree.say "Can I get you one too, Ryan?"
    elif hero.morality <= -25:
        bree.say "I'm off to the bar - so can I get you one too, Ryan?"
        bree.say "And before you ask, yes, I am trying to get you drunk!"
    else:
        bree.say "I'm gonna get myself another one of these."
        bree.say "You ready for another one too, Ryan?"
    if bree.is_visibly_pregnant:
        "Ryan looks at me wit horror written all over his face."
        "And he shakes his head just to underline his disapproval too."
        if ryan.sub >= 50:
            ryan.say "Oh no, [hero.name] - not while you're pregnant!"
        elif ryan.sub <= -50:
            ryan.say "[hero.name], I am seriously disappointed in you!"
        else:
            ryan.say "Is that a good idea in your condition?"
        bree.say "Oh...oh yeah...there is that!"
        $ hero.cancel_activity()
    elif (hero.charm >= 60 - ryan.love and ryan.flags.drinks < 2) or date_girl == ryan:
        "Ryan looks at his own empty glass and then back up at me."
        "And he nods happily, letting me know that he appreciates the offer."
        if ryan.sub >= 50:
            ryan.say "Sure thing, [hero.name] - that's so kind of you!"
        elif ryan.sub <= -50:
            ryan.say "I suppose I can let you get me a round in, just this once."
        else:
            ryan.say "Okay, [hero.name] - so long as you let me get the next one!"
        hide ryan
        show drink ryan
        if ryan.love <= 25:
            $ ryan.love += 1
        elif date_girl == ryan and game.active_date:
            $ game.active_date.score += 5
        call expression ryan.get_chat from _call_expression_534
        hide drink ryan
        $ ryan.set_flag("drinks", 1, "day", mod="+")
        if hero.morality >= -25:
            $ hero.morality -= 1
    else:
        show ryan annoyed
        ryan.say "No thanks, [hero.name]."
        $ hero.cancel_activity()
        hide ryan
    return

label ryan_slap_ass_intro_female:
    "Part of me wants to play it really cool around Ryan, to impress him with my charms."
    "But every time he walks past me I get a good look at that tight ass of his."
    "And I can hardly keep myself from reaching out and squeezing those firm buttocks!"
    "So is it any surprise that I finally end up snapping, and then slapping?"
    "The sound of my hand making contact with them is like the crack of a whip."
    "And Ryan leaps a good half-foot into the air in surprise too."
    if ryan.sub >= 50:
        ryan.say "Who...who did that?!?"
    elif ryan.sub <= -50:
        ryan.say "Whoa...that is NOT cool - who slapped my ass?!?"
    else:
        ryan.say "Hey, who slapped my ass?!?"
    "There's no use hiding, so I decide to face the music."
    if hero.morality >= 25:
        bree.say "I'm sorry, Ryan - it was me."
    elif hero.morality <= -25:
        bree.say "It was me - but your ass is just such a peach!"
    else:
        bree.say "Sorry, Ryan - I just couldn't resist."
    return

label ryan_slap_ass_happy_female:
    "Almost as soon as he sees that it's me making the confession, Ryan's expression changes."
    "Where before he looked seriously irritated and annoyed, now he seems to be all smiles."
    "And he practically beams at me as he wags his finger at me in an exaggerated motion."
    if ryan.sub >= 50:
        ryan.say "I should have know it was you, [hero.name]!"
        ryan.say "Would you like another one for free?"
    elif ryan.sub <= -50:
        ryan.say "Okay, [hero.name], you need to ask my permission next time."
        ryan.say "But I'll let you off, just this once."
    else:
        ryan.say "If it were anyone else, I'd be very cross right now!"
        ryan.say "Just give me a little more notice next time, okay?"
    return

label ryan_slap_ass_angry_female:
    "My confession doesn't seem to have the desired effect on Ryan."
    "As, if anything, he seems even more annoyed than he was before."
    "And now I'm beginning to regret telling him it was me in the first place."
    if ryan.sub >= 50:
        ryan.say "That's not fair, [hero.name]..."
        ryan.say "It's like...like you're bullying me!"
    elif ryan.sub <= -50:
        ryan.say "You'd better not do that again, [hero.name]."
        ryan.say "Or else I will not allow you in the vicinity of my ass!"
    else:
        ryan.say "That is so not cool, [hero.name]."
        ryan.say "Not to do it to a woman or a man!"
    return

label ryan_breakup_female:
    "Believe me, this is the last thing that I wanted to have to do today."
    "But I've thought about it from every possible angle I can conceive of."
    "And there's no other way out of this, so I have to go through with it."
    bree.say "Ryan, I have to tell you something..."
    if hero.morality >= 25:
        bree.say "This thing between us, it has to end."
    elif hero.morality <= -25:
        bree.say "It's been fun, but we have to end it."
    else:
        bree.say "We can't keep on seeing each other."
    "Ryan looks at me like he doesn't quite understand what I'm saying."
    "I can't tell if he's just shocked to be hearing me say it's over."
    "Or else he's not used to being told that kind of thing by a woman."
    if ryan.sub >= 50:
        ryan.say "You...you can't mean that, [hero.name]!"
    elif ryan.sub <= -50:
        ryan.say "Whoa...who are you to say it's over?!?"
    else:
        ryan.say "Is this some kind of a joke?"
    "I do the best I can to ignore what Ryan's saying to me."
    "And instead I press on to get it over and done with."
    if hero.morality >= 25:
        bree.say "I meant what I said, Ryan..."
    elif hero.morality <= -25:
        bree.say "What, you want me to spell it out with naked semaphore?!?"
    else:
        bree.say "I think you heard me clearly, Ryan..."
    bree.say "It's over, Ryan - we're over!"
    "I make a point of turning on my heel and walking away as quickly as I can."
    "Putting distance between us before Ryan can object or put a hand on my shoulder."
    "And sure, it feels bad - but not as bas as looking him in the eye would have done."
    return

label ryan_go_steady_intro_female:
    "There's never going to be a better time to ask than right now."
    "So I take a deep breath, hold it for a second, then let it out."
    "And I go right ahead with asking the question that's been on my lips for so long."
    if hero.morality >= 25:
        bree.say "Ryan, I wondered if...maybe you'd like to..."
        bree.say "Well, you know...perhaps...go steady?"
    elif hero.morality <= -25:
        bree.say "Ryan, I am SO fucking hot for you!"
        bree.say "What do you say we make it official between us?"
    else:
        bree.say "We've been getting on great recently, don't you think?"
        bree.say "So well that we could maybe...make it official?"
    return

label ryan_go_steady_yes_female:
    "At first Ryan looks more than a little surprised to hear the question."
    "Almost like he's amazed that he didn't think of it himself."
    "But it doesn't take long for him to break into a smile and start nodding."
    if ryan.sub >= 50:
        ryan.say "That's such a great idea, [hero.name]..."
        ryan.say "I don't know why we didn't do it sooner!"
    elif ryan.sub <= -50:
        ryan.say "Funny thing, [hero.name] - I was thinking of asking you the same thing."
        ryan.say "So by asking me, you kind of answered my own question for me!"
    else:
        ryan.say "You know what, [hero.name] - I was about to ask you the same thing!"
        ryan.say "We should totally do that."
    return

label ryan_go_steady_no_female:
    "At first Ryan looks more than a little surprised to hear the question."
    "But then he seems to recover some of his composure, and he shakes his head."
    "Which kind of forewarns me about what he's going to day next."
    if ryan.sub >= 50:
        ryan.say "Oh no, [hero.name], I couldn't do that - at least not yet."
        ryan.say "I haven't proven myself worthy enough to be with you!"
    elif ryan.sub <= -50:
        ryan.say "Oh, I don't think we're there yet, [hero.name]."
        ryan.say "But don't worry, I'll tell you when we make it."
    else:
        ryan.say "Thanks for the offer, [hero.name] - but we're not quite there yet."
        ryan.say "Don't get me wrong, we're close though, and I'll tell you when we get there."
    return

label ryan_pet_intro_female:
    "Look, I know that Ryan's not a cute pussy cat or an adorable puppy."
    "But he's still pretty irresistible and so that makes me want to pet him!"
    "And if that makes me a bad person, then so be it!"
    "All of which is a roundabout way of explaining why I'm doing what I'm about to do."
    "Specifically reaching out and patting the top of his head."
    if ryan.sub >= 50:
        ryan.say "Wha...who did that?"
    elif ryan.sub <= -50:
        ryan.say "Okay, that is NOT cool - who did that?"
    else:
        ryan.say "Did...did someone just pat me on the head?"
    if hero.morality >= 25:
        bree.say "Erm...it was me, Ryan!"
    elif hero.morality <= -25:
        bree.say "Geez, Ryan, I was only trying to be friendly!"
    else:
        bree.say "Calm down, fella - it was only me!"
    return

label ryan_pet_happy_female:
    "Almost as soon as he hears me speak up, Ryan's whole attitude changes."
    "Where before he looked annoyed and irritable, now he's all smiles."
    "Waving it off like there's no problem at all."
    if ryan.sub >= 50:
        ryan.say "Oh, if YOU did it, [hero.name], that's totally fine!"
    elif ryan.sub <= -50:
        ryan.say "You're fine, [hero.name] - just give me some kind of warning next time, okay?"
    else:
        ryan.say "Ah, I didn't know it was you, [hero.name] - no worries."
    return

label ryan_pet_annoyed_female:
    "As soon as I make the admission, I know that it was a mistake."
    "Ryan's attention focusses in on me like a bloody laser beam."
    "And I can feel myself shrinking away from his gaze."
    if ryan.sub >= 50:
        ryan.say "[hero.name], I feel violated - how could you do that to me?"
    elif ryan.sub <= -50:
        ryan.say "Okay, [hero.name], I'm going to have to insist that you ask permission before touching me in future!"
    else:
        ryan.say "Not cool, [hero.name], not cool at all!"
    return

label ryan_massage_intro_female:
    if ryan.sub >= 50:
        ryan.say "Ouch...ooh, I think I pulled something!"
    elif ryan.sub <= -50:
        ryan.say "Damn it - I pulled a muscle working out!"
    else:
        ryan.say "Urgh...I went and pulled a damn muscle!"
    "I can't help wincing in sympathy as Ryan twitches and twinges."
    "Because it's clear that he's genuinely in pain."
    "So my instinct is to do everything I can to help."
    if hero.morality >= 25:
        bree.say "Maybe I could take a look at it for you?"
    elif hero.morality <= -25:
        bree.say "Let me see - I got the magic touch!"
    else:
        bree.say "Want me to give you a massage?"
    return

label ryan_massage_accept_female:
    "Ryan looks reluctant for a moment, as if anticipating more pain."
    "But then he seems to feel one more twinge from his tortured muscles."
    "And the look of pain on his face is enough to make me cringe in sympathy."
    "Hell, even the nod he gives me looks like it costs him dearly."
    if ryan.sub >= 50:
        ryan.say "Yes...yes please, bree!"
    elif ryan.sub <= -50:
        ryan.say "Okay, [hero.name] - but I'm trusting you, so don't let me down!"
    else:
        ryan.say "Sure, [hero.name] - I'll try anything!"
    return

label ryan_massage_refuse_female:
    "For a moment I think that Ryan's going to be forced to say yes."
    "He's obviously in a great deal of pain, that's plain to see."
    "But then he seems to find some hidden reserve of stubbornness."
    "Because he shakes his head, even though the move looks to cause him pain."
    if ryan.sub >= 50:
        ryan.say "No, [hero.name] - I can't bear the thought of you making it worse!"
    elif ryan.sub <= -50:
        ryan.say "No, [hero.name] - I need to trust this to a professional."
    else:
        ryan.say "No, [hero.name] - if you make it worse, I'll go crazy!"
    return

label ryan_piercing_nipples_reaction_female:
    ryan.say "[hero.name], check this out..."
    ryan.say "I went and did something pretty wild!"
    "Before I can fully react to his words, Ryan whips up his top."
    "Giving me an eyeful of his newly pierced nipples!"
    bree.say "Whoa..."
    bree.say "That's...that's totally crazy, Ryan!"
    bree.say "I'm glad you like it."
    return

label ryan_piercing_navel_reaction_female:
    ryan.say "[hero.name], check this out..."
    ryan.say "I went and did something pretty wild!"
    "Before I can fully react to his words, Ryan whips up his top."
    "Giving me an eyeful of his newly pierced navel!"
    bree.say "Whoa..."
    bree.say "That's...that's totally crazy, Ryan!"
    bree.say "I'm glad you like it."
    return

label ryan_piercing_dick_reaction_female:
    ryan.say "[hero.name], check this out..."
    ryan.say "I went and did something pretty wild!"
    "Before I can fully react to his words, Ryan pulls out his waistband."
    "Giving me an eyeful of his newly pierced dick!"
    bree.say "Whoa..."
    bree.say "That's...that's totally crazy, Ryan!"
    bree.say "I'm glad you like it."
    return

label ryan_piercing_head_reaction_female:
    ryan.say "[hero.name], check this out..."
    ryan.say "I went and did something pretty wild!"
    "Before I can fully react to his words, Ryan opens his mouth."
    "Giving me an eyeful of his newly pierced tongue!"
    bree.say "Whoa..."
    bree.say "That's...that's totally crazy, Ryan!"
    bree.say "I'm glad you like it."
    return

label ryan_piercing_nose_reaction_female:
    ryan.say "[hero.name], check this out..."
    ryan.say "I went and did something pretty wild!"
    "Before I can fully react to his words, Ryan shoves his face towards mine."
    "Giving me an eyeful of his newly pierced nose!"
    bree.say "Whoa..."
    bree.say "That's...that's totally crazy, Ryan!"
    bree.say "I'm glad you like it."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
