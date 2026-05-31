label ayesha_date_intro_valentine_male:
    ayesha.say "H...hello, [hero.name]!"
    ayesha.say "I'm...a little nervous about tonight."
    ayesha.say "I don't think I've ever been someone's valentine!"
    "The moment the words are out of Ayesha's mouth, my heart aches for her."
    "She just looks so vulnerable and right now, despite her Amazonian physique."
    mike.say "Don't worry, Ayesha, just follow my lead."
    mike.say "I wouldn't have anyone else for my valentine, not for the world!"
    return

label ayesha_date_intro_halloween_male:
    mike.say "Hey, Ayesha - you look great tonight!"
    "Ayesha blushes and smiles at my compliment."
    ayesha.say "Thanks, [hero.name] - you too."
    ayesha.say "I'm pretty excited about tonight."
    ayesha.say "I don't think I ever went on a Halloween date before!"
    "At the mention of Halloween, I slap my forehead."
    mike.say "It's Halloween, and I totally forgot!"
    mike.say "We should have gotten dressed up for the occasion."
    "Ayesha shakes her head at this."
    ayesha.say "Oh no, [hero.name] - I only dress up in strange costumes when I wrestle."
    return

label ayesha_date_intro_christmas_male:
    ayesha.say "Happy Christmas, [hero.name]!"
    ayesha.say "Are you ready for our date?"
    mike.say "Of course I am, Ayesha."
    mike.say "I've been looking forward to it all week!"
    "Ayesha's face lights up as she hears the excitement in my voice."
    ayesha.say "Come on then - let's go."
    ayesha.say "And the first sprig of mistletoe we see - I want a festive kiss!"
    return

label ayesha_date_intro_birthday_male:
    mike.say "Happy birthday, Ayesha!"
    ayesha.say "Y...you remembered?"
    ayesha.say "Oh, [hero.name] - nobody EVER remembers my birthday!"
    mike.say "Nobody but me, Ayesha."
    mike.say "You're so special to me that I wanted to make this special for you."
    ayesha.say "You already did, [hero.name], you already did!"
    return

label ayesha_date_intro_mc_birthday_male:
    mike.say "You ready for our date, Ayesha?"
    ayesha.say "I am, [hero.name], I am..."
    ayesha.say "Oh...I can't believe I almost forgot!"
    ayesha.say "Happy birthday, [hero.name]!"
    mike.say "Wow, Ayesha - thanks for remembering!"
    ayesha.say "Don't look at me like that, [hero.name]."
    ayesha.say "You're making me blush!"
    return

label ayesha_date_pub_male:
    show ayesha
    ayesha.say "So, this would be what...your local?"
    mike.say "Ah, yeah - why'd you ask?"
    ayesha.say "No reason..."
    ayesha.say "It's just interesting what it says about you, that's all..."
    hide ayesha
    return

label ayesha_date_cinema_male:
    show ayesha
    ayesha.say "The cinema sounds like a great idea."
    ayesha.say "So long as we don't have to see something violent and braindead!"
    hide ayesha
    return

label ayesha_date_familyrestaurant_male:
    show ayesha
    ayesha.say "Hmm..."
    mike.say "Ah, what's up, Ayesha?"
    ayesha.say "Oh, it's nothing really, just...there are a LOT of noisy kids in here!"
    hide ayesha
    return

label ayesha_date_restaurant_male:
    show ayesha
    ayesha.say "Wow, this place is NOT what I was expecting!"
    mike.say "Really?"
    mike.say "This is one of my favourite places to eat."
    ayesha.say "Well, [hero.name], I guess you have hidden depths!"
    hide ayesha
    return

label ayesha_date_amusmentpark_male:
    show ayesha
    ayesha.say "There's a lot of people in the crowd here, [hero.name]."
    ayesha.say "Don't you let go of my hand!"
    hide ayesha
    return

label ayesha_date_ride_the_ferris_wheel:
    show ayesha
    ayesha.say "Ah...I don't like the look of that Ferris Wheel."
    ayesha.say "If we ride it, I may have to hold onto you the whole time!"
    $ ayesha.love += 1
    hide ayesha
    return

label ayesha_date_waterpark_male:
    if not ayesha.flags.first_date_waterpark:
        hide ayesha
        show bg black with fade
        "When I made the suggestion, I kind of expected Ayesha to baulk at the idea of going to the waterpark with me."
        "I guess I was afraid that she'll see it as a pretty childish way to spend her time, and tell me that there was no way."
        "After all, she's pretty serious when it comes to physical discipline and keeping herself in shape."
        "And it's pretty hard to imagine her splashing around in a pool without a care in the world."
        "But when I actually call her up and ask, she manages to take me by surprise with her answer."
        ayesha.say "You know what, [hero.name] - that sounds like it could be fun."
        "For a moment I don't know what to say."
        "I had all of my arguments and alternatives lined up for when Ayesha said no."
        "The one thing I never counted on was for her to say yes right from the start!"
        mike.say "Well, I suppose if you don't want to, we could always..."
        mike.say "Wait...did you say yes?"
        ayesha.say "Erm, yeah, [hero.name]."
        ayesha.say "That's not a problem, is it?"
        ayesha.say "I mean, you suggested it..."
        mike.say "Ah, yes...of course I did!"
        mike.say "I just didn't know if you'd be into that kind of thing, Ayesha."
        ayesha.say "Why wouldn't I be?"
        ayesha.say "I like to have fun as much as anyone!"
        mike.say "Sure you do, Ayesha, sure you do."
        ayesha.say "Right, [hero.name] - glad we cleared that up!"
        mike.say "So...should I see you there?"
        mike.say "Say this afternoon?"
        ayesha.say "Sounds like a plan to me!"
        "And so that's how I come to be walking into the waterpark with Ayesha."
        "And then soon afterwards, walking out of our respective changing-rooms."
        "I'm ready a little before she is, and I find myself checking my reflection as I wait."
        "Call me vain if you like, but I've been working out a hell of a lot recently."
        "And I'm hoping that Ayesha will notice an improvement in what she sees."
        scene bg waterpark
        ayesha.say "Hey, [hero.name]."
        ayesha.say "Are you ready to hit the water?"
        show ayesha
        "But as I turn around at the sound of her voice, all thought of impressing her with my body vanishes in an instant."
        "Sure, I've seen Ayesha in spandex at the gym and in the wrestling ring."
        "Yet the sight of her, standing there in her bathing suit, stops me in my tracks."
        "Maybe it's just the cut of what she's wearing that makes the difference."
        "Or maybe it's the smiles that's on her face right now."
        "Either way, she looks amazing - and I can already see the admiring gazes that she's attracting."
        mike.say "Hey, Ayesha - you look great!"
        "I hurry over to her side as I say this, eager to let everyone know that this stunning Amazon is with me!"
        show ayesha happy
        ayesha.say "You...you really think so?"
        ayesha.say "I thought it might be too skimpy, you know?"
        show ayesha normal
        ayesha.say "That it showed off too much of my muscles?"
        "I shake my head as she wraps her arm around mine and we start to walk together."
        mike.say "No way, Ayesha."
        mike.say "You look like some kind of goddess in that thing!"
        "Ayesha shakes her head and looks away bashfully at my comment."
        "But underneath it all, I can see that she's practically beaming at the compliment."
        "I decide to start things off slow, and so we play around a little in one of the shallow pools."
        hide ayesha
        show playing water ayesha waterpark
        "At first, Ayesha seems reluctant to join in as I splash her with water and generally horse around."
        "But then, just as she begins to lighten up and starts splashing me back, a shout comes from behind us."
        "A Kid" "Hey, I recognise you!"
        "Another Kid" "Yeah, you're the baddie that beat up Cutie Kawasaki!"
        "As one, Ayesha and I turn around to see two very irate-looking boys standing a little way off."
        hide playing water ayesha
        show expression Placeholder("boy") as kid1 at mostright5
        show expression Placeholder("boy") as kid2 at right5
        "Neither of them can be as much as ten years old."
        "But they have their hands balled into fists and frowns on their faces."
        show ayesha annoyed at left
        ayesha.say "Ah...I think you've gotten me confused with someone else, boys."
        "A Kid" "No way, lady!"
        "Another Kid" "We're BIG wrestling fans."
        "A Kid" "And we know who you really are!"
        "Ayesha turns her head away from the boys and towards me."
        show ayesha normal
        "And I can see the silent appeal for help in her eyes..."
        menu:
            "Wrestling is fake!":
                "Who in the hell do these little punks think they're talking to?"
                "Ayesha and I were in the middle of what promised to be a really fun date."
                "And now they're about to ruin it because of some dumb wrestling match they saw her in?!?"
                "Well, that's what those snot-nosed shits think!"
                mike.say "Hey, you two!"
                "The boy's heads swivel atop their pencil-necks as they hear the sound of my voice."
                mike.say "Yeah, that's right - I'm talking to you!"
                mike.say "That's my date you're disrespecting, and I don't appreciate it."
                "A Kid" "She's a bad guy, mister!"
                "Another Kid" "Yeah, she's always cheating in the squared-circle!"
                "I glance around me, looking this way and that."
                mike.say "Funny, I don't see a wrestling ring anywhere around here."
                mike.say "And do you know why that is, huh?"
                "The boys look at me nervously, shaking their heads."
                mike.say "Because this is the REAL world, you morons."
                mike.say "Wrestling's fake, it's made up, and you dumbasses think it's real!"
                show expression Placeholder("boy") as kid1 at mostright5, hshake
                "A Kid" "Wha...what?!?"
                "Another Kid" "No, mister, it really is..."
                mike.say "It's fake, make-believe, a fantasy - like Santa Claus!"
                "I leave the two boys to digest this as I take Ayesha by the arm and walk her away from them."
                "A Kid" "It can't be!"
                hide kid1 with moveoutright
                "Another Kid" "Wait...what did the mean man say about Santa?!?"
                hide kid2 with moveoutright
                "Ayesha glances back over her shoulder as we leave them to wrestle with the truth."
                ayesha.say "You probably shouldn't have said that, you know?"
                show ayesha annoyed at center with move
                ayesha.say "What if they never go to another wrestling match after this?"
                mike.say "So what if they don't, Ayesha?"
                mike.say "Think of it as two less little bastards to hurl abuse at you while you're in there!"
                $ ayesha.sub += 1
            "I'm her tag-team partner":
                "I have to think up a way out of this, and I have to do it quickly."
                "But the problem is that I can't do something that would make them think wrestling isn't real."
                "And telling Ayesha to piledrive them into the bottom of the pool isn't going to cut it!"
                "Racking my brains, I try to think of some wrestling-related rule that could save her ass..."
                mike.say "Hey, you two!"
                "The boy's heads swivel atop their pencil-necks as they hear the sound of my voice."
                mike.say "Yeah, that's right - I'm talking to you!"
                mike.say "That's my tag-team partner you're disrespecting, and I don't appreciate it."
                "A Kid" "She's a bad guy, mister!"
                "Another Kid" "Yeah, she's always cheating in the squared-circle!"
                mike.say "Well, what are you gonna do about it, punks?"
                mike.say "You know full well the rules don't let a guy fight a girl."
                mike.say "So you'll have to take me on instead!"
                "I step between Ayesha and the boys, trying my best to pull off an intimidating pose as I do so."
                "A Kid" "Hey, I've never seen YOU in the ring before!"
                "Another Kid" "How do we know you're even a wrestler?"
                mike.say "Oh yeah?"
                mike.say "How about you step into the ring and challenge me, brother?"
                mike.say "Or are you afraid to let [hero.name]mania run wild all over you?!?"
                "A Kid" "I...I think he means it!"
                "Another Kid" "Screw this - I'm not doing a run-in to save you!"
                hide kid2 with moveoutright
                "And with that, they turn tail and run, leaving Ayesha and I alone once more."
                hide kid1 with moveoutright
                "I turn to face Ayesha, only now realising that I'm still pulling my best wrestling pose."
                show ayesha happy
                ayesha.say "Nicely done, [hero.name]."
                ayesha.say "You sure scared those primary-school kids!"
                "Dropping the pose and trying to shrug it off, I begin to apologise."
                mike.say "I'm sorry, Ayesha."
                mike.say "I was trying to keep, what is it...kayfabe?"
                "She laughs and shakes her head at me, her smile reassuring me that she's not really mad."
                ayesha.say "It's okay, [hero.name] - I know you meant well."
                show ayesha blush
                ayesha.say "I actually quite enjoyed being described as your tag-team partner."
                ayesha.say "It was sweet...maybe even romantic - in a geeky kind of way!"
                $ ayesha.love += 2
        "With the threat to our having fun dealt with, Ayesha and I do the best we can to pick up where we left off."
        show ayesha happy
        "It feels a little awkward and forced at first, but soon enough the mood begins to lighten up again."
        "Before too long it almost feels as if the incident hadn't happened at all, and we're enjoying ourselves once more."
        $ ayesha.flags.first_date_waterpark = game.days_played
        hide ayesha
    else:
        show ayesha
        ayesha.say "The...the waterpark?"
        ayesha.say "I...I guess I should find my swimming costume out!"
        hide ayesha
    return

label ayesha_date_park_male:
    if not ayesha.flags.first_date_park:
        "I swear that the reason I chose to take Ayesha for a stroll in the park today was totally based on the weather and nothing else."
        "All it took was a quick glance out of the window this morning to see that it was going to be a clear day, with cloudless blue skies."
        "What better time to spend a couple of hours walking around the park, enjoying the sights, sounds and scents of nature?"
        "It had nothing to do with the fact that I checked my bank balance before I looked out the window and nearly had a seizure."
        "Okay, okay - I admit that I might have been a little liberal with my spending recently."
        "But the fact that I need to tighten my belt until payday doesn't make the park a bad option."
        "A cheap one, maybe - but not a bad one!"
        "Anyway, it's not like Ayesha seems upset at the idea when I call her up and make the suggestion."
        show ayesha
        mike.say "Hey, Ayesha."
        ayesha.say "Hey, [hero.name]."
        ayesha.say "So, where are we going for our date today?"
        mike.say "I was thinking maybe we could take a walk in the park?"
        mike.say "I know it's not exactly a rollercoaster ride."
        mike.say "But the weather's pretty nice today, right?"
        show ayesha happy
        ayesha.say "Don't sweat it, [hero.name]."
        ayesha.say "A walk sounds nice."
        ayesha.say "We can spend some time in nature and get some exercise all at once."
        ayesha.say "Who knows, it might even be romantic!"
        "I end the call feeling pretty flushed at the idea of Ayesha finding my suggestion romantic."
        "It's dumb, I know - but the feeling that she's into it makes me so much more nervous than it should."
        "I've walked through the park with more than a couple of girls in the past and thought nothing of it."
        show ayesha normal
        "But somehow doing the same things with a girl like Ayesha makes it all seem new and a more than a little exciting too."
        "That's why I find myself hurrying to the park, eager to be there for the appointed time."
        "And in my haste, I end up getting there a little early and having to wait with only my own thoughts for company."
        "This sees me pacing up and down, just about to teeter over into believing that I'm being stood up."
        "But then I see Ayesha striding towards me, and I suddenly recall that I was early and she's right on time."
        "Smile as I walk towards her, but I can't help noticing that she's glancing around as I do so."
        mike.say "Ayesha - what's up?"
        mike.say "What are you looking for?"
        "Ayesha looks at me with mild surprise showing in her eyes."
        "It's like I've jogged her out of a thought and back to reality."
        ayesha.say "What..."
        ayesha.say "Oh, no...it's nothing, really."
        mike.say "Are you sure?"
        mike.say "Because we can always go somewhere else if you're having second thoughts about the venue."
        mike.say "Unless you're having second thoughts about spending time with me?"
        ayesha.say "No, [hero.name] - like I said, it's okay."
        show ayesha happy
        ayesha.say "I just haven't been here in a while."
        ayesha.say "And it looks like they changed some stuff since then."
        "I choose to accept Ayesha's explanation at face value, not wanting to delve any deeper."
        "Sure, it doesn't make that much sense, but it's better than being stood up, right?"
        "So I reach out to take hold of her hand, and we start off on our walk."
        "To my relief, Ayesha seems to shake off the strange mood she's in pretty quickly."
        show ayesha normal
        "The park is full of pleasant things to see and the buzz of the other people taking their leisure alongside us."
        "Even on the odd occasion that we have to dodge cyclists and joggers, we just laugh it off and go on our merry way."
        "It's only when we come to the point where the park is mostly expanses of grass that things begin to change."
        "At first I can only hear the vague sound of someone shouting a way off."
        "But it soon begins to get louder, as the source of the noise draws quickly closer to us."
        "Pretty soon I can make out just what's being bellowed, and it's the same word, over and over again."
        "Dog Owner" "CAESAR...CAESAR...CAESAR!!!"
        "At the very same moment, Ayesha and I look in the direction of the shouting."
        "And then we see it - a creature that looks more like a small pony than an actual dog."
        "It's eyes look wild and it's jowls are flapping in the wind as it bares down upon us."
        "Only the glimpse of a collar and name-tag convinces me this is an actual pet and not some hound from hell itself!"
        "Ayesha and I are frozen to the spot, mere moments away from the beast closing the dwindling distance between us."
        show ayesha annoyed
        "I know that I have to do something, and fast - but what?!?"
        if hero.has_skill("animalhated") or game.week_day % 2 == 0:
            mike.say "Arrgh!"
            with vpunch
            mike.say "Ayesha, save me!"
            "And with those utterly cowardly words escaping my mouth, I leap towards my date."
            "Taken completely by surprise, Ayesha catches me as I wrap my arms around her neck."
            "This means that when the bounding, slavering dog arrives on the scene, I'm cradled in her arms."
            "It proceeds to let out a series of rumbling barks and try to leap up at Ayesha."
            "All of which only serves to make me cling to her all the more tightly."
            "A moment later, the dog's apparent owner comes running in its massive wake."
            "Dog Owner" "Sorry, sorry."
            "Dog Owner" "He's harmless really."
            "Dog Owner" "Sorry he scared your son..."
            "The words peter off into nothing as it becomes apparent I'm not a child, but in fact a grown man."
            "Muttering something that I can't make out, the owner puts the dog back on the lead and hurries away."
            show ayesha normal
            ayesha.say "[hero.name]."
            mike.say "Yeah, Ayesha?"
            ayesha.say "The dog's gone now, okay?"
            mike.say "Yeah, Ayesha."
            show ayesha happy
            ayesha.say "So I'm going to put you down now, okay?"
            mike.say "Yeah, Ayesha."
            "Slowly and with infinite care, Ayesha puts me down on my feet in front of her."
            "But the best that I can do to explain myself is give her a stupid grin and then a shrug."
            mike.say "I...I've always been scared of dogs."
            mike.say "It's dumb, I know - but there it is."
            show ayesha normal
            ayesha.say "What, like all dogs?"
            mike.say "No, of course not - you really think I'm afraid of a Chihuahua?!?"
            ayesha.say "I don't know, [hero.name]."
            show ayesha happy
            ayesha.say "You were the one that just leap into my arms!"
            mike.say "Well, that thing was huge."
            mike.say "You could have put a saddle on it and passed it off as a horse!"
            "Ayesha shakes her head, clearly amused both at my performance and my excuses."
            ayesha.say "Okay, [hero.name], okay."
            ayesha.say "It doesn't make you any less of a man!"
            "We set off on our walk again, and as the subject changes, I begin to feel less embarrassed."
            "I suppose it was actually quite funny, a guy jumping into a girl's arms."
            "I just hope that it doesn't mean Ayesha's lost any respect for me that she might have had..."
            $ ayesha.love += 2
        else:
            "Without saying a word, I put myself between Ayesha and the fast approaching-dog."
            "I lower myself down until I have my legs spread apart and my arms outstretched to meet it."
            "This means that when the bounding, slavering dog arrives on the scene, I'm directly in its path."
            "It proceeds to let out a series of rumbling barks and leaps up at me."
            with vpunch
            "And the next thing I know, its colliding with me like a speeding freight train."
            "I feel the force of it lift me off of my feet and bare me to the ground beneath it."
            "Wrapping my arms around its barrel of a chest, I roll the dog over onto its back."
            "And then I come up again, raking its belly with both hands."
            ayesha.say "[hero.name]!"
            ayesha.say "Oh my god!"
            show ayesha angry
            ayesha.say "Someone help him!"
            "At the sound of her distress, I glance over at Ayesha."
            mike.say "Ah, it's okay, Ayesha."
            mike.say "He just wanted his belly tickling."
            show ayesha annoyed
            mike.say "You see?"
            "I nod my head down towards the dog, now laid on his back, paws in the air."
            "His tongue is hanging out and he's looking up at me in blissful happiness."
            "A moment later, the dog's apparent owner comes running in its massive wake."
            "Dog Owner" "Sorry, sorry."
            "Dog Owner" "He's harmless really."
            "I nod and smile as I get back to my feet."
            mike.say "Oh don't worry."
            mike.say "I grew up around mutts just like him."
            mike.say "Sure, they look scary - but they're just overgrown pups at heart!"
            "The owner nods gratefully, happy not to have been harangued for failing to keep the dog under control."
            "And as soon as the dog is back on its lead, he's hauled away with great effort on the part of his owner."
            "It's only then that I look at Ayesha, noticing the genuine look of fear in her eyes."
            mike.say "God, Ayesha..."
            mike.say "Are you okay?"
            "The thought had never occurred to me that someone as physically imposing as her could be afraid of dogs."
            "But as I hurry over to where she stands, I can see that she's actually shaking with fear."
            ayesha.say "I...I thought it was going to get me!"
            show ayesha blush
            ayesha.say "B..but you stopped it, [hero.name] - you saved me!"
            "I put a tentative arm around Ayesha, trying to comfort her as best I can."
            mike.say "Hey, hey, it's okay, Ayesha."
            mike.say "Sure, he looked scary - but he just wanted to play, that's all."
            "She nods, but I can see that she's not convinced."
            ayesha.say "There was a dog...back when I was a kid."
            ayesha.say "We walked past it, to and from school every day."
            ayesha.say "It'd go crazy, pulling at its chain."
            ayesha.say "And then one day, the chain broke."
            show ayesha sad
            ayesha.say "And...and it got to me..."
            ayesha.say "I tried to run...but it got to me..."
            "Without saying another word, I pull her as close to me as I can."
            "She returns the embrace, those strong arms feeling anything but in that moment."
            mike.say "Don't worry, Ayesha."
            mike.say "I won't let that happen to you."
            mike.say "Not while I'm with you."
            "Ayesha stays wrapped in my arms for a few minutes longer."
            "And then she seems to have recovered enough to continue our walk through the park."
            show ayesha normal
            "But the whole time she clings to my arm, almost resting her head on my shoulder."
            "Though I get the feeling it's not entirely out of fear of the same thing happening again."
            "I can't help thinking that some of it is on account of her now seeing me as a kind of guardian."
            "Perhaps even a living talisman against some of her worst fears too..."
            $ ayesha.sub += 2
        $ ayesha.flags.first_date_park = game.days_played
        hide ayesha
    else:
        show ayesha
        ayesha.say "You know, I haven't been here in a while."
        ayesha.say "Thanks, [hero.name], this was a really great idea."
        hide ayesha
    return

label ayesha_date_livingroom_male:
    if not ayesha.flags.first_date_home:
        "I know full well that inviting a girl over to your place is one of those things that you're just supposed to do."
        "It's such a cliche of modern relationships that most people wouldn't even think twice about suggesting it and then following through."
        "But me being me, I can't help overthinking the whole thing the moment after I suggest it to Ayesha and she agrees."
        "I try to calm myself down by rationalising it, boiling the evening down to just the essential elements."
        "All it really means is that Ayesha comes round here and we spend time together, watching whatever on the TV."
        "But then I realise that means she'll be walking into my home for the very first time."
        "What if she doesn't like what she sees?"
        "What if it starts her thinking that it's a reflection on me?"
        "No...I have to stop catastrophising about what's just supposed to be a chance to spend some time with Ayesha."
        "She'll come over, we'll lounge around on the sofa together and both of us will have a good time - that's all there is to it."
        "Needless to say, when open the doorstep, I feel like a jumble of nerves."
        "As I show her into the sitting room, I note Ayesha looking at her surroundings with interest."
        show ayesha
        ayesha.say "This is a pretty nice neighbourhood, [hero.name]."
        ayesha.say "It must be a quiet life living around here, huh?"
        "What does she mean by that?"
        "Is she trying to say that I'm boring?"
        "No, of course not - she's just saying what she means."
        "After all, this is a nice neighbourhood."
        mike.say "I guess so, Ayesha."
        mike.say "I never much thought about it."
        mike.say "The town I grew up in was pretty small, so most of it was kind of like this too."
        "Ayesha nods as we sit down on the sofa."
        ayesha.say "That sounds like the kind of place that'd be good to visit."
        ayesha.say "Who knows, maybe you can show me around some time?"
        ayesha.say "The neighbourhood I grew up in was a little rougher than that..."
        "For a moment I feel as though Ayesha is about to say more on the subject."
        "But then she smiles and shakes her head, closing the potential window into her past."
        ayesha.say "But you don't wanna talk about my childhood."
        show ayesha happy
        ayesha.say "Not when we're supposed to be having a pleasant time together!"
        "I consider telling Ayesha it's okay, pressing her to go on with what she was going to say."
        "But then I change my mind, thinking that I shouldn't pressure her to talk when she's already changed the subject."
        mike.say "Okay, Ayesha - whatever you say."
        mike.say "Now, where were we?"
        $ at_home = Room.find("livingroom").get_present_girls_ids_by_tag()
        if not at_home:
            ayesha.say "About to kick back and watch some TV?"
            "I nod in agreement, plucking the remote control off the arm of the sofa and flicking on the TV."
        elif {'bree', 'sasha'}.issubset(set(at_home)):

            show bree normal at right
            bree.say "Ooh, [hero.name] - who's this?!?"
            show sasha normal at mostright4
            sasha.say "Yeah, [hero.name] - you never told us you were having company over today!"
            show ayesha normal
            "Ayesha and I look around at the exact same moment, like guilty children caught raiding the biscuit tin."
            "And I'm not at all surprised to see [bree.name] and Sasha, their heads sticking around the edge of the doorway."
            mike.say "Ah, I'm almost one hundred percent certain that I did."
            mike.say "And I also seem to remember you telling me that you'd make yourselves scarce too!"
            "[bree.name] looks sideways at Sasha as they come slinking into the room."
            "Sasha just shrugs and shakes her head, dismissing my words completely."
            sasha.say "As I recall, we said we'd get out of your hair when she was HERE."
            bree.say "And here she is."
            sasha.say "And here we are, on our way out the door."
            show bree wink
            bree.say "Yeah, [hero.name] - we just happened to see her between here and there!"
            "Admitting defeat, I roll my eyes at the pair of them."
            mike.say "Urgh...okay, you win!"
            show bree normal
            if Harem.together(bree, sasha, name="home"):
                mike.say "Ayesha, meet [bree.name] and Sasha."
                mike.say "They're my housemates..."
                "At the mention of the word housemates, [bree.name] and Sasha burst out laughing."
                show bree happy
                show sasha happy
                "In fact, the fit of laughter seems to affect them so much that they collapse onto the sofa."
                "One ends up on either side of us."
                "And I see Ayesha recoil a little at the invasion of her personal space."
                show bree normal
                bree.say "Ah, he's just being modest, Ayesha."
                show sasha normal
                sasha.say "Yeah, he really is - because we're MUCH more than that!"
                show ayesha annoyed
                ayesha.say "Uh...wha...what do you mean?"
                bree.say "Well, you see we share everything in this house."
                sasha.say "The bills..."
                show bree happy
                bree.say "The shopping..."
                show sasha happy
                sasha.say "Each other..."
                "I see Ayesha's eyes go wide at this."
                "But she struggles to keep calm and not freak out."
                ayesha.say "Tha...that's really modern of you!"
                show ayesha blush
                ayesha.say "Real Bohemian, you know?"
                "[bree.name] and Sasha get up from the sofa, both smiling at Ayesha's discomfort."
                show ayesha normal
                show bree normal
                bree.say "Well, we should get going."
                show sasha normal
                sasha.say "Yeah, but remember, Ayesha - you're always welcome here!"
                hide bree with moveoutright
                hide sasha with moveoutright
                "And with that, they're gone, leaving me to deal with the fallout of what they just did."
                mike.say "I'm sorry, Ayesha - I should have told you that before now."
                mike.say "If this changes things between us...I understand."
                "To my surprise, Ayesha turns to me with a smile on her face, shaking her head."
                show ayesha happy
                ayesha.say "Hey, I've seen stranger in my time wrestling, believe me."
                ayesha.say "And if those little girls think they can scare me off, they're dead wrong!"
                "All I can do is nod, wondering if this means that Ayesha will be joining in with [bree.name], Sasha and I in the near future."
            else:
                mike.say "Ayesha, meet [bree.name] and Sasha."
                mike.say "They're my housemates - and the bane of my existence!"
                "Ayesha laughs at my evident irritation, slapping me playfully on the shoulder."
                show ayesha happy
                ayesha.say "It's okay, [hero.name]."
                ayesha.say "They're just interested in your love-life."
                ayesha.say "It's sweet - like you have a couple of sisters to look after you!"
                "I can feel myself starting to blush as [bree.name] and Sasha join in with the laughter."
                show bree happy
                show sasha happy
                bree.say "Yeah, [hero.name] - you should listen to your sisters!"
                bree.say "We know what's best for you!"
                sasha.say "Sure thing we do."
                sasha.say "And that goes for you too, sister!"
                "At this, Sasha turns her attention to Ayesha."
                show ayesha normal
                sasha.say "You be sure to look after our brother there."
                sasha.say "Or else there'll be hell to pay!"
                "As [bree.name] and Sasha finally make themselves disappear, Ayesha shakes her head."
                hide bree with moveoutright
                hide sasha with moveoutright
                ayesha.say "Am I hearing things, or was that kind of a threat?"
                mike.say "Why, Ayesha?"
                mike.say "Are you afraid of them?"
                mike.say "Just be nice to me, and you won't have to face the wrath of my sisters!"
        show ayesha normal
        "With the remote control in my hand, I scroll through what's on offer."
        "Nothing leaps out at us, and so in the end, we settle on something that we can just chill out to."
        "At first we're just sitting next to each other, our hips kind of the only things touching."
        "But as time passes, I can feel the atmosphere changing, as if it's hanging over the both of us."
        "We're sitting here alone, in an otherwise deserted house and with nothing at all to get in the way."
        "Someone needs to make a move soon, or it's going to become too much to bear!"
        menu:
            "Wait a little more":
                "I honestly don't know what it is that keeps me from making that first move."
                "But I feel like my limbs are suddenly frozen with the fear of taking a risk."
                "If I get this wrong, it could be the start of the end for us!"
                "And it's as I can feel my mind becoming trapped in such thoughts that it happens."
                "I feel hands grab the side of my head, turning it smartly around."
                "Before I know what's happening, I find myself looking Ayesha square in the face."
                ayesha.say "If you're not gonna do it, then I will!"
                hide ayesha
                show ayesha kiss
                $ ayesha.flags.kiss += 1
                "And with that, she presses her lips against mine."
                "I stiffen at first, which means that Ayesha has to practically force her tongue between my lips."
                "But she manages this with some ease, and a moment later, I feel myself melt into it."
                "There's something undeniably thrilling about the way she's taking control."
                "It's as if knowing that she wants me that desperately is a huge turn-on."
            "Go for it":
                "It's now or never, I tell myself as I turn to face Ayesha."
                "She looks around at me, waiting to see what I'll do next."
                "And without waiting for permission, I cup her cheeks in my hands."
                show ayesha kiss
                $ ayesha.flags.kiss += 1
                "Then I kiss her, full on the lips and with all of the passion that I can summon."
                "The kiss doesn't last too long, and I end it a moment later feeling full of trepidation."
                hide ayesha kiss
                show ayesha close blush
                "Ayesha remains in the same position as she was when I kissed her."
                "She stares at me, her eyes seemingly still somewhere else until they focus on me."
                ayesha.say "Oh, [hero.name]..."
                ayesha.say "Please - don't stop now!"
                "Her words and the look on her face mean that I don't need to be told twice."
                hide ayesha close
                show ayesha kiss
                "And a moment later, our lips are pressed together again."
                "But this time Ayesha is playing her part too, and so it's that much more enjoyable."
        hide ayesha kiss
        show ayesha blush
        "From that point on, it's like the floodgates have broken and there's nothing at all holding us back."
        "Ayesha and I become one jumble of entwined limbs and heaving body-parts on the sofa."
        "I forget everything in the world, save for the girl that's wrapped in my arms."
        "I want to feel every inch of Ayesha's body, with my hands and lips alike."
        "I've known women both thicc and thin, but never one that feels the way she does."
        "Ayesha's muscles don't make her hard like a rock, but rather lithe like a big cat."
        "And all I can think is that I want so badly to be hunted down by this apex predator in particular..."
        "By now, I have a rather massive and painful erection below the belt."
        "The only thing I want to do is introduce Ayesha to it as soon as I possibly can."
        "But then the sound of keys in a lock breaks the spell, and reality rushes back in."
        "For some reason, Ayesha and I fly apart, like guilty teenagers caught in the act."
        "All I can guess is that she was as into it as I was, her mind wandering in the same direction."
        "And being caught at it on the couch by [bree.name] or Sasha would have been pretty embarrassing."
        ayesha.say "Oh, wow..."
        show ayesha annoyed
        ayesha.say "Have you SEEN the time?"
        ayesha.say "I should really get going!"
        mike.say "Ah...okay, Ayesha."
        mike.say "If you say so..."
        show bg house
        show ayesha normal
        "As I walk Ayesha to the door, we still seem to be behaving like bashful teenagers, enslaved by our urges."
        ayesha.say "I had a really nice time, [hero.name]."
        mike.say "Me too!"
        mike.say "We should do this again, and soon."
        show ayesha happy
        ayesha.say "Yeah - I'd like that."
        "I pause for a moment, just as Ayesha is about to step out of the front door."
        mike.say "You don't have to go, Ayesha."
        mike.say "You could always...stay...with me."
        "She smiles at this, but still shakes her head."
        ayesha.say "Thanks for the offer, [hero.name]."
        ayesha.say "Maybe next time, yeah?"
        mike.say "Yeah, Ayesha...yeah."
        hide ayesha with moveoutleft
        "Ayesha turns and walks to the street, pausing to wave before she starts off on her way."
        "I stand in the doorway, watching her go until she's lost from sight."
        "But my mind is already imagining the possibilities should she keep her promise..."
        $ game.room = "house"
        $ game.active_date.stay = False
        $ game.active_date.score = 50
        $ ayesha.love += 5
        $ ayesha.flags.first_date_home = True
        $ game.pass_time()
    else:
        show ayesha
        "We decide to hang out at the house."
        hide ayesha
    return

label ayesha_date_nightclub_male:
    if not ayesha.flags.first_date_nightclub:
        "It took more than a little effort on my part to convince Ayesha that we should go clubbing for our latest date."
        "From the way she reacted to the suggestion, I could have believed that she'd never stepped foot inside a nightclub before."
        "And even though I managed to talk her around, I can still tell that's nervous as we stand in the queue waiting to get in."
        mike.say "Hey, Ayesha."
        show ayesha
        ayesha.say "Huh...what is it, [hero.name]?"
        mike.say "There's no need to be so jumpy."
        mike.say "It's just a nightclub, that's all."
        "Ayesha glances around at all of the people standing around us in the queue."
        "And she has a good view of them as well, standing a head taller than most."
        ayesha.say "You keep saying that, and I know you're right."
        show ayesha annoyed
        ayesha.say "But places like this, well..."
        ayesha.say "They make me feel self-conscious, okay?"
        "I find myself shaking my head as we move forwards with the queue."
        mike.say "But you're a wrestler, Ayesha."
        mike.say "You have people looking at you the whole time you're in the ring."
        ayesha.say "That's not the same thing, [hero.name]."
        ayesha.say "I'm playing a role then, portraying a character."
        ayesha.say "Other times I'm...just me."
        "I can't argue with something like that, or suggest anything that might make it better."
        "And so I have to fall back on the only comfort that I can offer."
        mike.say "'Just you' is still pretty amazing, Ayesha - trust me!"
        show ayesha normal
        "Ayesha gives me a smile that's weak, but still makes my heart flutter a little."
        mike.say "And don't worry about anything."
        mike.say "I'll be with you the whole time."
        mike.say "All we're here to do is have a couple of drinks and maybe a dance, okay?"
        "Ayesha nods, taking hold of my hand as we're finally ushered into the place by the bouncers."
        "Even with the noise and press of people inside the club, I can't help wondering at Ayesha."
        "It's such a strange contradiction that a girl so strong and imposing could also be so shy and awkward."
        "And even stranger is the fact that it's not a turn-off for me in the slightest."
        "If anything, it makes her that much more endearing and me more determined to protect her."
        "It's just my luck that the club is busier than normal on the very night I've chosen to bring Ayesha here."
        "Normally that'd be a good sign, meaning a better chance of there being a decent atmosphere in the place."
        "But right now, all it seems to mean is that Ayesha feels the need to cling ever closer to me as we push our way to the bar."
        "As we wait to be served, I think about making a quip about the advantages of her being so tall."
        "You know, something in passing about being able to use her as a landmark to navigate the crowd."
        "But then I stop myself just as the words are forming in the back of my throat."
        "Ayesha's self-conscious enough as it is."
        "The last thing that she needs is her own date making fun of her."
        "Instead, I hold my tongue until we're both holding our drinks."
        "And then I make a point of surveying the dance-floor."
        mike.say "I think there's some space just opened up out there, Ayesha."
        mike.say "Let's go and stake a claim, yeah?"
        "I see Ayesha open her mouth, and I'm prepared for her to say no."
        "But then she visibly stops herself, as if wrestling with her own nerves."
        ayesha.say "Sure...why not!"
        ayesha.say "You lead the way, [hero.name]."
        "I nod and smile, appreciating the fact that she's making an effort to leave her comfort zone behind."
        "And so taking hold of Ayesha's hand once more, I walk her to the space I spotted a moment before."
        "Even when we make it out there and begin to move in time to the music, Ayesha still looks nervous."
        hide ayesha
        show dance ayesha
        "I try as best I can to reassure her, making sure that her attention is focused on me."
        "But all too soon I begin to notice that she looks distracted."
        "Her gaze keeps drifting to the people dancing to either side of us, as if she's bothered by their presence."
        "This worries me, as I can't exactly tell them to back off on a crowded dance-floor."
        "It's only then that I take a closer look at the offending bodies and notice something for the first time."
        "They are actually getting closer to Ayesha and me, like they're trying to move in on us."
        "It's a couple of girls and guys that seem to be together in a group."
        "And it doesn't take me long to figure out that they're all casting admiring glances Ayesha's way too!"
        "Don't get me wrong - they're not being assholes about it or anything like that."
        "But they're definitely making her feel pretty uncomfortable..."
        menu:
            "We should join in":
                "I could cut them off, you know - keep them well away from Ayesha."
                "But would I really be doing her any favours?"
                "Maybe the best way for her to get over her fears is to face them?"
                "Or else be made to face them..."
                "I begin to make a little room between Ayesha and myself on the dance-floor."
                "Not a blatant invitation to the new-comers."
                "But still enough to let them know they're welcome to join us."
                "Ayesha sees what I'm doing."
                "And she immediately makes to grab my wrist, pulling me closer to her."
                "I give her what I hope is a reassuring smile, and shake my head."
                "But by this time, the other clubbers have already taken advantage of the space I've allowed them."
                "Now it's my turn to take Ayesha by the wrists, gently drawing her into the newly-formed circle around us."
                "She resists at first, but slowly relents, allowing me to have my way."
                "And pretty soon we're dancing in the middle of a like-minded huddle of bodies."
                "Ayesha follows my example, moving in sympathy to the people around her."
                "But the whole time that she does so, I can see that there's a pained smile on her face."
                "Almost as soon as the track that we've been dancing to ends, the group breaks up a little."
                "And that's when Ayesha seizes the chance to make good her escape."
                "I find myself being practically dragged off of the dance-floor, her grip like iron around my wrist."
                hide dance ayesha
                show ayesha normal
                "It takes me a couple of moments, but eventually I manage to make her slow down and stop."
                mike.say "Ayesha...hey, Ayesha!"
                mike.say "Are you okay?"
                ayesha.say "Ah...yeah, [hero.name] - I'm fine."
                show ayesha happy
                ayesha.say "That was...that was really fun..."
                "I nod and smile at this, trying to make it look like I'm convinced by her words."
                "But at the same time, I can't help beginning to think that I made a big mistake back there."
                $ ayesha.sub += 1
            "Stay close":
                "Okay, point number one - I don't want anyone ruining this for Ayesha."
                "It was a pretty big deal for her to even come here in the first place!"
                "And point number two, she's MY date."
                "Call me selfish if you like, but I'm not about to share her with anyone!"
                "Even as the newcomers draw closer to us, I move to close the gap between Ayesha and myself."
                "Without warning, I put my hands on her ass and pull her into a tight embrace."
                "She lets out a yelp of surprise as we come together, instinctively wrapping her arms around me."
                "I turn my back to the clubbers trying to cut in on our action, underlining the fact that they're not welcome."
                "And only then do I actually begin to feel the sensation of having Ayesha pressed so close to me."
                "Her body is an amazing combination of firm and yielding as she moves in my arms."
                "Her breathing is somehow louder in my ear than the music that's filling the club."
                "Almost as soon as the danger of us being interrupted is passed, I make to loosen my grip on Ayesha."
                hide dance ayesha
                show ayesha close normal
                "But much to my surprise, she instantly pulls me back into just as tight of an embrace as before."
                mike.say "I...I'm sorry, Ayesha."
                mike.say "I was just trying to..."
                ayesha.say "No..."
                show ayesha close happy
                ayesha.say "It's okay, [hero.name]."
                ayesha.say "It's...nice..."
                ayesha.say "Really nice..."
                "Seemingly assured that I won't try to pull away again, Ayesha relaxes her grip on me just a little."
                hide ayesha close
                show dance ayesha
                "But now that I know what's behind her clinging to me so closely, I'm keen to keep it up too."
                "Slowly and with a great deal of care, we start moving to the music once more."
                "The difference this time is that we're both on the same page."
                "And I'm enjoying the sensations of being so close to Ayesha more with each second that passes."
                "When the song ends, she remains pressed against me, as if unwilling to let go."
                hide dance ayesha
                "We then move off the dance-floor."
                $ ayesha.love += 2
        $ ayesha.flags.first_date_nightclub = True
        hide ayesha
    else:
        show ayesha
        "We go to the nightclub."
        hide ayesha
    return

label ayesha_date_eat_a_burger:
    "Ayesha picks up her burger, but then pauses as she realises I'm watching her."
    "And the bite that she takes out of it is amazingly delicate and demure."
    "I'll admit, I had been expecting her to devour it in two or three bites!"
    return

label ayesha_date_buy_drink:
    if ayesha.is_visibly_pregnant:
        show ayesha angry
        $ ayesha.love -= 10
        ayesha.say "You want me to drink?"
        ayesha.say "When I'm pregnant with your own child?!?"
        ayesha.say "Unbelievable!"
        $ hero.cancel_activity()
        hide ayesha
    else:
        "Ayesha smiles as I had her a drink, taking it readily."
        ayesha.say "Thanks, [hero.name]."
        ayesha.say "I'll get you one next time round."
    return

label ayesha_date_play_darts:
    "Ayesha shrugs at the invitation to play darts, but agrees anyway."
    "She manages to hit the board with almost all of her throws."
    "But I get the distinct impression that this isn't her game..."
    return

label ayesha_date_pub_play_pool:
    "Ayesha accepts the pool cue with a casual smile, chalking the tip with practised ease."
    "And I can almost feel my chances of winning evaporate in that same moment."
    "From there, Ayesha proceeds to trounce me with depressing ease."
    return

label ayesha_date_buy_a_round:
    if ayesha.is_visibly_pregnant:
        show ayesha angry
        $ ayesha.love -= 10
        ayesha.say "You want me to drink?"
        ayesha.say "When I'm pregnant with your own child?!?"
        ayesha.say "Unbelievable!"
        $ hero.cancel_activity()
    elif (hero.charm >= 60 - ayesha.love and ayesha.flags.drinks < 2):
        show drink ayesha
        mike.say "Time for another round?"
        ayesha.say "Sure, [hero.name]."
        ayesha.say "But you paid last time - isn't it my turn to get the drinks?"
        $ game.active_date.score += 5
        if "rebel" in ayesha.traits:
            $ game.active_date.score += 5
        $ ayesha.set_flag("drinks", 1, "day", mod="+")
        hide drink
    else:
        "I want to pay a round of beers to the whole pub."
        "But Ayesha doesn't seem to want to drink, so I refrain from doing so."
        $ hero.cancel_activity()
    return

label ayesha_dance_with:
    "I have to really work hard to get Ayesha onto the dance-floor with me."
    "She shakes her head, makes excuses and almost flatly refuses."
    "But in the end, she relents and lets me lead her out there."
    "Ayesha leans in close the whole time, as if she's afraid to let go of me for even a second."
    return

label ayesha_date_play_arcade_intro_male:
    ayesha.say "Ah..."
    ayesha.say "I don't know about this, [hero.name]."
    ayesha.say "I've never been one for videogames."
    "I can't help looking at Ayesha like a dog that's been shown a card trick."
    "It baffles me that anyone could not have fun in an arcade as cool as this one."
    "I mean, I'm almost dizzy from the sheer choice of amazing games there are to choose from!"
    mike.say "You can't be serious, Ayesha!"
    mike.say "I thought everyone played videogames as a kid?"
    mike.say "Are you telling me you didn't?"
    "Ayesha looks a little awkward as I ask the question."
    "I could almost swear that she's blushing a little too."
    ayesha.say "I...I was always more into books as a kid, [hero.name]!"
    ayesha.say "Sure, I was a geek, a massive one."
    ayesha.say "But not the kind of geek it's cool to be now, you know?"
    mike.say "I see what you're saying, Ayesha."
    mike.say "You mean that you missed out back in the day."
    mike.say "So now's the perfect time to catch up!"
    mike.say "And there's a game for everyone too - how about this one?"
    "At first, Ayesha doesn't look at all convinced."
    "But then I almost see her ears prick up."
    ayesha.say "Is that..."
    ayesha.say "Is that the Big Bosswoman's entrance theme?!?"
    mike.say "Well, yeah, Ayesha."
    mike.say "This is GGF Wrestlequest - it's a classic!"
    "Ayesha almost shoulders me aside in her eagerness to see the arcade cabinet."
    ayesha.say "The Ultimate Amazon, Andrea the Giantess...The Million-Dollar Lass!"
    ayesha.say "They're all here!"
    "Before I can say a word, she's pumping coins into the slot!"
    ayesha.say "Pick wrestler, [hero.name], quickly!"
    ayesha.say "We're going to enter the Regal Rumble!"
    return

label ayesha_date_play_arcade_win_male:
    "Ayesha might have all the enthusiasm in the world."
    "But unfortunately that doesn't translate into talent for the game."
    "And pretty soon she finds herself on the end of an ass-whipping."
    ayesha.say "What the hell?"
    ayesha.say "No way was that fair!"
    ayesha.say "You...you can't counter a leg-lock with a hip-toss!"
    "I keep on glancing sideways at Ayesha as we play."
    "And I swear I can see the veins standing out on her forehead."
    "That and hear the sound of her grinding her teeth!"
    mike.say "Ah, Ayesha..."
    mike.say "Are you feeling okay?"
    mike.say "You look a little stressed over there!"
    ayesha.say "What?"
    ayesha.say "Don't...don't distract me!"
    ayesha.say "NO...NO...NO, NO, NO!"
    "I watch as my wrestler downs Ayesha's on the screen."
    "And then the referee counts the pin - one, two, three."
    mike.say "Sorry, Ayesha!"
    mike.say "No hard feelings, yeah?"
    ayesha.say "Speak for yourself, [hero.name]."
    ayesha.say "I want a rematch - in the real world!"
    return

label ayesha_date_play_arcade_lose_male:
    "Ayesha just told me that she's never played videogames in her life."
    "But somehow she just seems to get the knack of the game straight away."
    "Maybe it's just luck, or maybe her experience as a wrestler helps."
    "Whatever it is, I'm getting my ass kicked!"
    mike.say "Hey..."
    mike.say "What the hell?"
    mike.say "Ayesha, how are you doing that?!?"
    "I keep glancing sideways at Ayesha as we play."
    "And I swear she's smirking at me the whole time."
    "Loving the fact that she's beating me hands down!"
    ayesha.say "Wow, [hero.name]..."
    ayesha.say "You're as bad at this as you'd be at the real thing!"
    ayesha.say "I really should put you out of your misery..."
    mike.say "What?"
    mike.say "NO...NO...NO, NO, NO!"
    "I watch as Ayesha's wrestler downs mine on the screen."
    "And then the referee counts the pin - one, two, three."
    ayesha.say "Sorry, [hero.name]."
    ayesha.say "No hard feelings, yeah?"
    mike.say "Speak for yourself, Ayesha."
    mike.say "I think you just KO'd my love of videogames!"
    mike.say "At least for a little while..."
    return

label ayesha_dick_reactions:
    if not ayesha.flags.seendick:
        $ ayesha.flags.seendick = 1
        if hero.has_skill("hung"):
            show dick reactions ayesha scared
            ayesha.say "Oh...oh my!"
            mike.say "What's the matter, Ayesha?"
            show dick reactions ayesha mock
            ayesha.say "Nothing...nothing..."
            ayesha.say "It's just...so big!"
            $ ayesha.sub += 10
        elif hero.has_skill("smalldick"):
            show dick reactions ayesha scared
            ayesha.say "Oh...oh my!"
            mike.say "What's the matter, Ayesha?"
            show dick reactions ayesha mock
            ayesha.say "Nothing...nothing..."
            ayesha.say "You wanna cuddle, maybe?"
            $ ayesha.sub -= 10
        hide dick reactions
    return

label ayesha_halloween_invitation:
    show ayesha
    "Almost as soon as we agreed to have a Halloween party, I knew who I wanted to invite."
    "We've been having such a great time together that Ayesha's the only girl it could be."
    "And by the time I get round to asking her, I'm already imagining the night with her there."
    "So now all I need to do is actually make the invitation."
    "Well, that and have her say yes!"
    show ayesha at center, zoomAt(1.5, (640, 1040)) with fade
    mike.say "Ayesha..."
    mike.say "I was just wondering..."
    show ayesha happy
    "Ayesha looks around at the sound of my voice."
    "Her mouth is curled into a knowing smile."
    "And her eyes have an interested, slightly amused look in them."
    ayesha.say "I know that tone of voice, [hero.name]!"
    ayesha.say "What are you after this time, huh?"
    mike.say "Wh...what do you mean?"
    ayesha.say "You always sound like that when you want something."
    ayesha.say "And you always get defensive too - just like that!"
    mike.say "Okay, Ayesha, okay."
    mike.say "You got me."
    "Ayesha nods, enjoying my admission of guilt."
    show ayesha normal
    ayesha.say "So come on - out with it!"
    mike.say "Well..."
    mike.say "We're having a Halloween party at my place."
    mike.say "And I wanted to ask if you'd be my date?"
    mike.say "It's a costume party too."
    mike.say "So you can dress up, just like you do in the wrestling ring!"
    if ayesha.love >= 100:
        show ayesha annoyed
        "Ayesha frowns and shakes her head."
        ayesha.say "It's nothing like what I do in the ring."
        ayesha.say "It's just for fun, that's all."
        ayesha.say "But I do have a costume I've wanted to wear for a while..."
        "Sensing a chance to influence Ayesha, I jump on it."
        mike.say "Well then, this is the perfect opportunity!"
        mike.say "You'll have a captive audience at my place."
        show ayesha normal
        "I can see that Ayesha's warming to the idea."
        "And with each second that passes, her smile widens."
        $ ayesha.love += 1
        ayesha.say "Okay, [hero.name], you win."
        ayesha.say "But only because I didn't already have plans."
        "I can see from the twinkle in Ayesha's eye that she's lying."
        "But if letting her save face gets me what I want, then so be it."
        mike.say "Lucky me then, getting in first."
        mike.say "I just hope I get lucky on the night too!"
        show ayesha happy
        ayesha.say "That remains to be seen!"
        $ game.flags.halloween_girl = "ayesha"
    else:
        show ayesha angry
        "Ayesha frowns and shakes her head."
        "And then she crossed her arms over her chest."
        "None of which can be taken as a good sign."
        ayesha.say "What?!?"
        ayesha.say "Professional wrestling is nothing like a costume party!"
        mike.say "I don't understand, Ayesha."
        mike.say "You put on crazy outfits."
        mike.say "You pretend to be someone else."
        mike.say "How are they any different?"
        $ ayesha.love -= 2
        show ayesha annoyed
        "Ayesha lets out a frustrated groan."
        "And I can see that I'm in danger of losing this one."
        ayesha.say "What I do in the ring is a performance art."
        ayesha.say "It takes athletic skill, years of training."
        ayesha.say "And you have to understand psychology too."
        show ayesha angry
        ayesha.say "How is that like dressing up for Halloween!"
        mike.say "I...I'm sorry, Ayesha."
        mike.say "You're right - it was a dumb thing to say!"
        show ayesha annoyed
        ayesha.say "That's right, [hero.name], it was."
        ayesha.say "You can think about that at your dumb party."
        ayesha.say "And you'll have time to do it too."
        ayesha.say "Because you won't have me there to distract you!"
    hide ayesha with fade
    return

label ayesha_halloween_arrival:
    scene bg house
    "I open the door, expecting to see my date standing there."
    show ayesha halloween angry
    "But instead I find a massive, imposing figure towering over me."
    "It's shadow covers me, and I can almost feel myself quaking."
    ayesha.say "Kneel before the prophet of the Great Kraken!"
    "Before I even know what I'm doing, I obey the command."
    "I actually get down on my knees in the hope of being shown mercy."
    "That's when the giant on my doorstep leans forwards."
    "And the aspect of it's features changes from stern to worried."
    show ayesha sad
    ayesha.say "Ah, [hero.name]..."
    ayesha.say "You don't actually have to do it!"
    mike.say "Ayesha?"
    mike.say "Oh...my...goddess!"
    mike.say "Is that you?!?"
    "She gazes down on me with her massive icon hoisted on her shoulder."
    "The costume is stop on, making her look like the priestess in the game."
    show ayesha blush
    "All of a sudden, Ayesha looks a little embarrassed."
    "She glances this way and that, as though she wants to come inside."
    ayesha.say "I...I almost didn't come as The Squid Priestess."
    ayesha.say "But she's my favourite character in the game!"
    ayesha.say "And now I'm staring to wonder if I made the right choice..."
    menu:
        "Compliment":
            "I can't begin to shake my head quickly enough."
            "And I get back to my feet as I do so."
            mike.say "Who cares what anyone else thinks, Ayesha?"
            mike.say "You're my date tonight."
            mike.say "And I think you look divine!"
            mike.say "If you'll pardon the pun..."
            show ayesha blush
            $ ayesha.love += 1
            "Ayesha can't help blushing as I gush over her."
            "She looks this way and that, checking we're alone."
            ayesha.say "Stop it, [hero.name]!"
            ayesha.say "Actually, don't stop it!"
            ayesha.say "You really like my costume?"
            "I nod eagerly."
            mike.say "Of course I do, Ayesha."
            mike.say "You've made her my favourite character too!"
        "Criticize":
            "Well, what on earth did she expect?"
            "Ayesha's practically a giant in her own right."
            "And dressing up as The Squid Priestess only adds to her stature."
            mike.say "You should have thought it through better, Ayesha."
            mike.say "Now you have to spend all night being the centre of attention!"
            $ ayesha.love -= 2
            show ayesha sad
            "Ayesha looks more than a little hurt by my answer."
            "She frowns and looks at her feet."
            ayesha.say "You didn't have to come right out and say it, [hero.name]."
            ayesha.say "Maybe you could have spared my feelings - just a little?"
            "I shrug it off and shake my head."
            "I really don't have time for this tonight."
            "The last thing I need is Ayesha laying a guilt-trip on me."
            mike.say "What can I say, Ayesha?"
            mike.say "I'm a modern guy - I say it how it is!"
            show ayesha annoyed
            "Ayesha frowns at me and curls her lip."
            "But she walks into the house all the same."
            "Though I think it'd be wise to be nice to her from now on."
            "After all, I don't want to be smited by her righteous fury!"
    scene bg black with dissolve
    pause 1
    return

label ayesha_halloween_party:
    $ game.pass_time(2)
    scene bg livingroom
    with dissolve
    ayesha.say "Back, foul heathen!"
    ayesha.say "Back I say!"
    ayesha.say "If I like something I take it, if I hate something I break it."
    ayesha.say "In the name of the Great Kraken, I smite thee!"
    "I recognise the sound of Ayesha's voice as soon as I hear it."
    "And at first I think she's just playing up to her costume."
    show ayesha halloween angry at right
    show jack halloween perv at left
    "But then I see that she has the huge icon that she carries held before her."
    "That and the fact that Jack's pretty much cowering before her!"
    jack.say "Smited by The Squid Priestess!"
    jack.say "Wow - what a way to go!"
    jack.say "I want that written on my tombstone!"
    "I hurry over as quickly as I can."
    "Determined to put myself between Jack and Ayesha's massive weapon."
    menu:
        "Defend Ayesha":
            mike.say "Whoa, whoa..."
            mike.say "What's going on, Ayesha?!?"
            mike.say "What did he do to you?"
            show ayesha annoyed
            "Ayesha lowers the blunt object."
            "But she keeps one eye on Jack all the same."
            ayesha.say "The little creep pinched my ass!"
            show jack sad
            jack.say "It was only a little pinch."
            jack.say "I couldn't help it - I was hypnotised!"
            "I turn to face Jack, frowning at his excuses."
            mike.say "You're lucky she didn't bash your brains out!"
            mike.say "Ayesha here could tie you up in knots without breaking a sweat."
            "That last comment was meant to scare Jack."
            show jack perv
            "But instead I see his eyes light up at the prospect."
            jack.say "She's welcome to try that on me anytime!"
            "Without thinking, I grab the icon out of Ayesha's hands."
            show jack halloween surprised
            "And then I use it to threaten Jack myself."
            "He lets out a yelp and scuttles off."
            hide jack
            show ayesha sad at center
            with easeoutleft
            "Which leaves Ayesha and me alone."
            ayesha.say "You wouldn't really have hit him, would you?"
            mike.say "I could ask you the same question, Ayesha!"
            $ ayesha.love += 2
            $ ayesha.sub -= 1
            show ayesha happy
            "Ayesha chuckles and shakes her head."
            "She leans to take the icon back and whispers in my ear."
            ayesha.say "You can touch my ass all you like, [hero.name]."
            ayesha.say "And I promise you'll enjoy me tying you up in knots too!"
        "Defend Jack":
            mike.say "Whoa, whoa..."
            mike.say "What's going on, Ayesha?!?"
            mike.say "You're not going to use that thing on him, are you?"
            show ayesha annoyed
            "Ayesha glowers at me, clearly still angry."
            "But she lowers the blunt object all the same."
            ayesha.say "I should brain him with it."
            ayesha.say "The little creep pinched my ass!"
            show jack sad
            jack.say "It was only a little pinch."
            jack.say "I couldn't help it - I was hypnotised!"
            mike.say "You could have just told me, Ayesha."
            mike.say "I'd have made sure it never happened again."
            $ ayesha.love -= 2
            $ ayesha.sub += 2
            hide jack
            show ayesha blush at center
            with easeoutleft
            "Jack takes the chance to slip away while I talk to Ayesha."
            "And she hardly seems to notice him leave."
            "She's too busy looking embarrassed and a little ashamed of herself."
            ayesha.say "I...I'm sorry, [hero.name]."
            ayesha.say "I didn't think!"
            mike.say "Well, try to do that next time, okay?"
    scene bg black with dissolve
    pause 1
    return

label ayesha_halloween_dance:
    $ game.pass_time(2)
    scene bg livingroom
    show ayesha halloween
    with dissolve
    "Ayesha's been eyeing up the dance-floor all night."
    "She keeps glancing at it and then at me."
    "But whenever I catch her doing it, she looks away again."
    "And when she does that, her face is full of guilt."
    "At first I can't figure out what's up with her."
    "But then it hits me."
    "Ayesha must be waiting for me to ask her to dance!"
    "She's obviously too shy to make the first move herself."
    mike.say "Hey, Ayesha..."
    mike.say "Do you want to dance with me?"
    show ayesha blush
    "I'd been expecting Ayesha's expression to change."
    "But now she looks even more nervous than before!"
    ayesha.say "I...I don't know..."
    ayesha.say "I guess we could - if that's what you want?"
    menu:
        "Dance":
            "I frown a little, puzzled by Ayesha's reluctance."
            "But then I shrug my shoulders and give her a smile."
            mike.say "Yeah, Ayesha - it's what I want."
            mike.say "So let's go dance!"
            hide ayesha
            show dance ayesha halloween
            "Ayesha offers no resistance as I lead her onto the dance-floor."
            "But she looks nervous the whole time, glancing this way and that."
            "I do the best I can to keep her attention on me."
            $ ayesha.love -= 2
            "And yet it doesn't seem to have any effect."
            "Ayesha remains stiff and awkward the whole time."
            hide dance
            "Then she makes her escape as soon as the song is over."
            "I follow in her wake, wondering if I just made a mistake."
        "Do not dance":
            "I frown a little, puzzled by Ayesha's reluctance."
            "But then I shake my head and give her a smile."
            mike.say "Not if it's not what YOU want, Ayesha."
            mike.say "And I don't think it is, yeah?"
            show ayesha happy
            "Only now does Ayesha's expression change."
            "She looks suddenly relieved."
            "Like a weight's been lifted off of her."
            ayesha.say "I always feel self-conscious when I dance."
            ayesha.say "And being all dressed up like this makes it worse!"
            mike.say "No problem, Ayesha."
            mike.say "Let's just grab another drink instead."
            $ ayesha.love += 2
            "Ayesha nods and smiles at this."
            "And I feel like I made the right decision."
    scene bg black with dissolve
    pause 1
    return

label ayesha_halloween_sex:
    scene bg bedroom1
    show ayesha halloween happy
    with dissolve
    "It's been hard to concentrate on anything apart from Ayesha all night."
    "She just looks so damn good in that costume of hers, I can't help it."
    "At first I thought she might get annoyed that I kept on staring at her."
    "But then I noticed that she was starting to grin and smirk whenever I looked her way."
    "What I didn't realise until later was that she's been hitting the punch pretty hard."
    "And so by the time the party is coming to an end, I'm dealing with a rather drunk Amazon!"
    ayesha.say "Come here, puny manthing!"
    ayesha.say "Let me grab you and take you!"
    "Ayesha grips my collar and tosses me into my bedroom with ease."
    with vpunch
    play sound door_slam
    "Then she slams the door behind her, crossing her arms over her chest."
    mike.say "Ah..."
    mike.say "Are you feeling okay, Ayesha?"
    mike.say "Your breath smells like I could light it on fire!"
    "Ayesha strides over to me and stops when we're almost nose to nose."
    "Then, without even stopping to ask permission, she starts tearing off my clothes."
    mike.say "Whoa!"
    mike.say "What the hell?!?"
    "Ayesha doesn't even look up from what she's doing."
    "Instead her pace quickens as she removes more of my clothes."
    show ayesha angry
    ayesha.say "Silence your prattle, manthing."
    show ayesha happy
    ayesha.say "I have needs that must be satisfied!"
    "Suddenly I find myself totally naked."
    "Ayesha stands back, nodding as she admires her work."
    ayesha.say "You will do - for now!"
    "Before I can protest, Ayesha places her hand flat on my chest."
    "And then she shoves me backwards, sending me sprawling onto the bed."
    "It's only when I hit the mattress that my thoughts seem to clear."
    "Ayesha hasn't taken a blow to the head and regressed to the mentality of cavewoman."
    "She's just managed to down enough alcohol to bypass her usual inhibitions."
    "And now she's playing out the character that she came to the party dressed as."
    "That means I have maybe two choices here."
    "I can go along with it and let her have her way."
    "Or I can step up to the challenge and give as good as I get."
    "I make my choice as soon as Ayesha lowers herself onto the bed."
    "She tries to lie down atop me, pinning me to the mattress."
    show ayesha angry
    "But I manage to slip out from beneath her at the last moment."
    "Normally, Ayesha's reactions are pretty fast."
    "But I have the booze to thank for making her a little sluggish."
    "She hits the bedclothes, then looks up in surprise."
    show ayesha doggy halloween
    ayesha.say "Manthing!"
    ayesha.say "Where did you go?!?"
    "I take this as my opportunity to pounce on Ayesha from behind."
    "She lets out a cry of alarm as I land on her back."
    "But I notice that her efforts to throw me off are less than effective."
    "For all that Ayesha makes a show of it, I see that she's not really trying."
    "Which tells me that she's actually enjoying the experience!"


    ayesha.say "Oh..."
    ayesha.say "Manthing - I am at your mercy!"
    "I'm already hard from being manhandled by Ayesha."
    "And so I don't need to worry about being ready for what comes next."
    "I aim my cock between Ayesha's buttocks."
    show ayesha doggy vaginal pleasure
    if persistent.xray:
        show ayesha doggy xray
    "Then I push with all my might."
    ayesha.say "Mmm..."
    ayesha.say "I am at your mercy..."
    ayesha.say "I am in your power..."
    ayesha.say "Do with me as you will!"
    "I don't need to be told what to do next."
    "As soon as I feel my cock inside of Ayesha, I give it all I've got."
    "Her pussy feels amazing around my cock, squeezing me hard."
    "And I start to pound away at her ass without mercy."
    "There are no more words from Ayesha now."
    "Instead she moans and gasps beneath me."
    "Where before she was the one dominating me, now she succumbs totally."
    "With each and every thrust, I feel her surrender more to me."
    "I feel like I'm taming her with my cock!"
    "All Ayesha can do is look back over her shoulder at me."
    "The expression on her face seeming to beg for more of the same."
    "I try as best I can to give her what she wants."
    "The last reserves of energy that I have go into my efforts."
    "Ayesha nods desperately as I push myself to the limit for her."
    "And she begins to let out cries of sheer pleasure too."
    "I don't know if it's me coming to the end of my endurance."
    "Or else the feeling of Ayesha beginning to cum beneath me."
    "But either way I can't keep this up any longer."
    show ayesha doggy -vaginal ahegao
    "At the very last moment, I pull my cock out of Ayesha."
    "She gasps in surprise, but before she can object, it happens."
    with hpunch
    "Ayesha let's out a deep moan, vocalising her orgasm."
    show ayesha doggy cumshot with hpunch
    "And I shoot my load over her back and buttocks."
    show ayesha doggy pleasure -cumshot dickcum cum onbody with hpunch
    "Then I slump down onto the bed beside her."
    "Neither of us seems able to move."
    "So there we stay, panting and slick with sweat."
    $ ayesha.sexperience += 1
    $ game.pass_time(1)
    return


label ayesha_date_forest_male:
    scene bg black with rtimelaps
    scene bg bedroom1 at sepia
    show flashback
    with rtimelaps
    "It's just by chance that I happen to be rooting through some of my stuff that I'd stashed at the back of my wardrobe."
    "I can't even remember what I started out looking for amongst things I haven't touched since I moved into the house."
    "Pulling something out from the bottom of the pile with all of my strength, I inevitably bring the whole lot tumbling down onto me."
    play sound body_fall
    pause 0.3
    with vpunch
    "And it's when I'm sitting, half buried under the avalanche of random crap, that I see it poking out of the mess."
    "A jumble of waterproof material, carbon poles and complex-looking ropes that end in metal pegs."
    "My tent, the one that always promised myself I'd get more use out of when I packed it along with the rest of my stuff!"
    "For a moment I feel the urge to go camping rise inside of me, and it sounds like a great idea."
    "The fact that I spent most of my time inside of the thing while I was doing various fun things at music festivals doesn't seem to matter."
    scene bg black with timelaps
    scene bg street
    show ayesha casual normal
    with timelaps
    mike.say "Hey, Ayesha."
    mike.say "You remember we were racking our brains to think of something to do this weekend?"
    show ayesha joke
    ayesha.say "Erm...I remember YOU were."
    ayesha.say "Didn't I say that we could just catch a film or whatever?"
    mike.say "Well, you don't have to worry about any of that, Ayesha."
    mike.say "Because I just decided that we're going camping!"
    show ayesha surprised
    "Ayesha looks at me with mild surprise showing in her eyes."
    "Which is not exactly the kind of response that I'd been hoping for."
    "But I try my best to ignore that and carry on undeterred."
    mike.say "It'll be great, Ayesha, trust me."
    mike.say "I've got a tent and I can get all the other stuff we'll need."
    mike.say "We can have a fire and roast marshmallows under the light of the stars."
    mike.say "Just you and me!"
    show ayesha happy
    ayesha.say "That does sound kind of nice, [hero.name]."
    show ayesha annoyed
    ayesha.say "But I don't know..."
    ayesha.say "I'm not really the outdoors type!"
    "For all that Ayesha's trying to give me a means to get out of this one, I'm simply not listening to her."
    "In my mind we're already sitting by that fire, snuggled together under a blanket."
    "And then there's the sleeping arrangements to think of too..."
    mike.say "So that's decided then?"
    mike.say "You, me and a tent, in the woods!"
    show ayesha normal
    ayesha.say "Ah...I guess so, [hero.name]."
    $ game.pass_time(3)
    scene bg black with timelaps
    scene bg forest
    show ayesha casual normal
    with timelaps
    "And as Ayesha and I hike into the forest, making for the spot that I've picked out for us to camp, she seems to feel it too."
    "For all that she's always told me she's a city girl at heart, being out in nature can't help but raise her mood."
    "So by the time we find the clearing I've chosen, both us are in pretty high spirits."
    mike.say "We're here, Ayesha."
    mike.say "This is the spot where we're going to pitch the tent."
    "Ayesha looks around before she turns her attention to me, taking in the surroundings."
    "And I swear that I see her close her eyes and breath in a lungful of the clean, pine-scented air."
    ayesha.say "You know, [hero.name], I was sure I'd hate this from the start."
    ayesha.say "But now I'm out here..."
    show ayesha happy
    ayesha.say "Well, let's just say I'm starting to feel glad you talked me around!"
    "I can't help smiling at this, feeling vindicated for ignoring her initial misgivings."
    "Opening my mouth to say something that would probably have been pretty smug, I'm cut off by a sudden, massive thunder-crack."
    play sound thunder_single
    pause 0.5
    show ayesha surprised with vpunch
    "Both of us jump at the sound, unable to control our reactions to such a show of raw, elemental power."
    play sfx1 thunder_deep
    "There's a second thunder-crack, this one low and rolling, ominous in the sound that it makes."


    show bg forest at dark with dissolve
    "And then the heavens open, and we're caught in a torrential downpour."
    show ayesha normal at center, zoomAt (1.65, (650, 1140))
    "Ayesha and I dash straight under the largest tree we can find."
    "In the confusion, neither of us spares as much as a thought for where the inevitable lightning might strike."
    "As we huddle there, staring out into the storm that's taken us completely by surprise, Ayesha jabs me in the ribs."
    with hpunch
    mike.say "Ow!"
    mike.say "Hey, Ayesha - that hurt!"
    show ayesha angry
    ayesha.say "Didn't you check the weather forecast?!?"
    show ayesha annoyed
    ayesha.say "Well?"
    ayesha.say "This was your idea, [hero.name] - so I'm waiting for you to fix it!"
    show ayesha normal
    if hero.knowledge < 50:
        "Of course I didn't check the weather forecast!"
        "What does she think I am - some kind of outdoors survivalist or doomsday prepper?!?"
        "All I wanted to do was pitch a tent and share a sleeping bag with Ayesha."
        "Not prove my credentials as a hunter-gatherer..."
        "But she's looking at me like she expects me to make it all work out."
        mike.say "Okay, Ayesha - I got this."
        hide ayesha with dissolve
        "And with that, I hurry out into the pouring rain, grappling with my backpack."
        "As I haul out the tent, already soaked to the bone, the pieces drop into the deepening mud."
        "What follows is a farce of epic proportions, as I struggle against the tent and the elements all at once."
        "I was banking on having time and space to pitch the tent, as I never bothered to read the damn instructions."
        $ game.pass_time(2)
        scene bg black with timelaps
        scene bg forest at dark
        show ayesha casual normal
        with timelaps
        "But the best I can manage is to fumble with the lining, shoving the poles in at random and hoping for the best."
        "Pretty soon I'm actually getting wrapped up inside of the tent, and losing the battle against it."
        "Ayesha watches from the poor shelter of the trees, probably feeling as embarrassed as I do right now."
        "And when I slip on the mud, falling in a chaotic pile of limbs and tent-parts, she calls time on the fight."
        show ayesha annoyed
        ayesha.say "[hero.name], for god's sake."
        ayesha.say "You're going to end up strangling yourself with that thing!"
        "Realising that she's right, I haul myself to my feet and slug it back over to where she's standing."
        "The going is tough, as I'm dragging the remains of the tent after me."
        "And so I arrive under the tree looking bedraggled and defeated."
        mike.say "I'm sorry, Ayesha."
        mike.say "I've taken us camping by accident..."
        show ayesha normal
        ayesha.say "It's okay, [hero.name] - at least you tried."
        ayesha.say "But what are we gonna do now, huh?"
        show ayesha sad
        ayesha.say "It's too late to set off back, and the rain isn't stopping."
        "With some difficulty, I manage to extricate myself from the tent and inspect the damage I've done."
        mike.say "You know what - the inside of this thing is still dry, and there's no mud in there either."
        mike.say "If we get inside of it and then into our sleeping bags, we might be okay..."
        show ayesha joke
        "Ayesha gives me a pained smile, and then shakes her head."
        ayesha.say "Well, it sounds pretty lame."
        ayesha.say "But it's better than what I got - which is precisely nothing!"
        $ ayesha.love -= 4
        "And so we set about putting my half-assed plan into action."
        "Once we're snuggled down inside of our makeshift shelter, I dig around in my backpack for something to eat."
        "All I can find that's safe to be eaten raw are a couple of chocolate bars."
        "So I hand one to Ayesha and keep the other for myself."
        show ayesha happy
        "As we lie there, huddled together for warmth, I hear the sound of soft laughter."
        mike.say "Ayesha...are you okay?"
        ayesha.say "Yeah, [hero.name], yeah."
        ayesha.say "I'm laid in a collapsed tent in the middle of the woods, eating chocolate in the pouring rain."
        show ayesha joke
        ayesha.say "I was just thinking - if this is camping, then I've really been missing out all these years!"
        "I start laughing too, feeling the sense of camaraderie growing between us."
    else:
        "When I said that I'd only ever camped at music festivals before now, I wasn't lying."
        "But no one ever binge-watched as many series on the Discovery Channel as I did!"
        "And it only takes a couple of seconds for my memory to come to the rescue."
        mike.say "Okay, Ayesha - I got this."
        "The survivalist and bush-craft shows that can help me come flooding back."
        hide ayesha with dissolve
        "And I stride confidently out into the clearing, my head held high and a purpose in my walk."
        "It doesn't take me long to identify the best spot for the tent, sheltered and away from any run-off too."
        "I clear the ground and set about pitching the tent, and pretty soon it's up and secure."
        "From there I stash our stuff inside and close the flap to keep it as dry as possible."
        "And then I set about collecting as much dry wood as I can scavenge and piling it up by the tent."
        "Next is a circle of stones to contain the fire and a makeshift shelter of ferns beside it."
        "By the time I'm making the sticks into a pyramid and striking sparks from my flint, I hear footsteps approaching."
        $ game.pass_time(3)
        scene bg black with timelaps
        scene bg forest
        show ayesha casual surprised
        with timelaps
        ayesha.say "Wow, [hero.name]!"
        show ayesha happy
        ayesha.say "Where did you learn to do stuff like this?!?"
        "She shakes her head as she surveys the neat, orderly camp I've constructed in such a short space of time."
        ayesha.say "I wouldn't know where to get started!"
        mike.say "Ah, it's nothing that amazing, Ayesha."
        mike.say "And I wouldn't have brought you out here if I didn't know what I was doing."
        "As the kindling smoulders and the fire begins to take, I hand her a marshmallow on the end of a stick."
        "Patting a spot on the log that I found to serve as a bench, I invite Ayesha to join me."
        show ayesha normal at center, zoomAt (1.65, (650, 1140))
        "The rain is still coming down, and it doesn't look likely to stop until morning."
        "But we can glimpse some of the night sky through the dark clouds."
        mike.say "What star-sign are you, Ayesha?"
        ayesha.say "I'm Taurus..."
        show ayesha annoyed
        ayesha.say "The bull..."
        "I choose to ignore the fact that she's clearly embarrassed by the connotations of the animal in question."
        "And instead I point to a group of stars, just visible between the clouds."
        mike.say "That's Taurus, right there."
        show ayesha surprised
        ayesha.say "No way!"
        $ ayesha.love += 4
        mike.say "No word of a lie, Ayesha - that's your star-sign up there!"
        show ayesha happy at startle
        "She laughs and leans against me, wrapping her arm in mine."
        ayesha.say "Okay, [hero.name], you got me."
        ayesha.say "I was sure this would be a bad idea, a sucky way to spend a date."
        ayesha.say "But it's nice, you know?"
        show ayesha blush
        ayesha.say "Kind of romantic, even..."
        "I don't say anything, but simply smile, enjoying the closeness growing between us."
    $ game.active_date.stay = False
    $ DONE["ayesha_date_forest"] = game.days_played
    stop sound fadeout 1.0
    scene bg forest
    call sleep (sleep_room="forest") from _call_sleep_66
    if game.hour <= 7:
        $ time_to_pass = 7 - game.hour
    else:
        $ time_to_pass = 7 + (24 - game.hour)
    $ game.pass_time(time_to_pass)
    $ game.room = "forest"
    scene bg forest with fade
    "In the morning, I rouse Ayesha gently and slip out of my sleeping-bag to begin breaking down the camp."
    show ayesha casual normal with dissolve
    "Neither of us says much while there's work to be done, but the pleasant feelings from last night still endure."
    "The walk back from the clearing and towards civilisation is more enjoyable than the one we took to get out there the previous day."
    "And all in all, I can't help thinking that Ayesha will remember her first camping trip for a long time to come."
    $ game.room = "street"
    scene bg street with fade
    return

label ayesha_date_aquarium_male:
    show ayesha casual
    "I only mentioned the idea of us going to the aquarium to Ayesha in passing, while I was plucking possible date locations out of the air."
    "But the moment that I speak the word to her, she seems to get pretty excited about the prospect."
    "And so, not wanting to look the proverbial gift horse in the mouth, I jump on the chance to take her somewhere she really wants to go."
    mike.say "So that's settled then, Ayesha?"
    mike.say "You really want to go to the aquarium for our..."
    mike.say "Our trip out together?"
    show ayesha happy at startle
    "Ayesha shakes her head as she starts to laugh."
    show ayesha normal
    ayesha.say "Oh, come on, [hero.name]!"
    ayesha.say "You can call it a date you know!"
    show ayesha joke
    ayesha.say "I don't bite...well, that's strictly true..."
    show ayesha normal
    mike.say "Ahem..."
    mike.say "The aquarium, Ayesha..."
    mike.say "We were talking about our...date?"
    show ayesha happy at startle
    "Ayesha laughs again, clearly enjoying the fact that she's managed to get me all flustered."
    show ayesha normal
    ayesha.say "Okay, [hero.name]."
    ayesha.say "The aquarium it is!"
    scene bg street with fade
    "For some reason, the idea of us actually being on official date together makes me far more nervous than it should."
    "And it's not anything to do with Ayesha's stature either, which is actually something I love about her."
    "Sure, she's incredibly hot - anyone can see that."
    "But there's just something about her that disarms me."
    "I can't quite put my finger on it, and I almost crave the chance to spend time with her so that I can discover more."
    scene bg aquarium at flip, center, zoomAt(1.65, (540, 840)), dark, blur(10)
    show ayesha b casual happy at center, zoomAt(1.65, (840, 1140))
    with fade
    pause 0.5
    show ayesha b at center, zoomAt(1.65, (640, 1140)) with ease
    "As we head over to buy our tickets, Ayesha takes hold of my hand."
    "She doesn't ask permission, and her grip is predictably strong."
    "My heart almost skips a beat at the sensation."
    "Which is crazy, as I must have held hands with dozens of other girls before now."
    "And yet I can't remember feeling that way with any of them!"
    show ayesha b normal
    ayesha.say "You know, it's crazy."
    ayesha.say "But I've lived in this city for a couple of years now."
    ayesha.say "And in all that time, I've never once thought of coming here!"
    mike.say "Really?"
    mike.say "Huh...I guess it's like people that live in New York, you know?"
    mike.say "They grow up there, and yet they've never been to see the Statue of Liberty."
    scene bg aquarium with fade
    show ayesha b casual happy at dark, center, zoomAt(1.65, (1040, 1140)) with easeinright
    "As we walk into the darkened interior of the aquarium, I see Ayesha almost in silhouette."
    show ayesha b at dark, center, zoomAt(1.65, (940, 1140)) with ease
    "But I can still make out the shape of her head as she nods in agreement."
    show ayesha b at dark, center, zoomAt(1.65, (800, 1140)) with ease
    ayesha.say "Sometimes you can't see what's right under your nose."
    show ayesha b at dark, center, zoomAt(1.65, (640, 1140)) with ease
    ayesha.say "No matter how amazing it might be..."
    hide ayesha
    show ayesha b casual happy at center, zoomAt(1.65, (640, 1140)) with dissolve
    "Suddenly, the light from the first of the tanks illuminates Ayesha's face."
    "And I can see that she's looking straight at me, a smile on her lips as she does so."
    "The weird, aquatic glow from the tank casts Ayesha's face in an ethereal manner."
    "She looks so good that I can feel that same nervous sensation rising in my chest again."
    mike.say "Ah, yeah..."
    mike.say "That'd...that'd really suck..."
    mike.say "Ooh, look - what an interesting fish!"
    "Without hesitation or turning her head away from the tank, Ayesha nods."
    ayesha.say "Pterois volitans, more commonly known as the 'Lionfish'."
    "I narrow my eyes in suspicion, and then glance down at the label next to the tank."
    mike.say "Lucky guess!"
    "Ayesha smiles at my disbelief, but shakes her head all the same."
    show ayesha b joke
    ayesha.say "You wish!"
    ayesha.say "Want to test me?"
    show ayesha b normal
    menu:
        "Continue the visit":
            "For some reason, I feel instantly intimidated by the idea of Ayesha being so knowledgeable."
            "I know it's stupid of me, but I guess I kind of like to be the one to dispense the info."
            "Ayesha might not intimidate me at all physically."
            "Yet she seems to be able to challenge my mental manhood all the same!"
            mike.say "No, Ayesha."
            mike.say "You don't need to prove yourself to me."
            mike.say "But I still think it was a lucky guess!"
            show ayesha a angry with hpunch
            "Ayesha frowns a little and punches me gently on the arm at this."
            "Well, I suppose she punches me in a way that she thinks is gentle."
            "Even so, I can feel my whole arm going numb from the blow."
            show ayesha a annoyed
            $ ayesha.love -= 2
            ayesha.say "Hey!"
            ayesha.say "I'm not some kind of muscle-bound dumbass, you know!"
            mike.say "No...of course not!"
            mike.say "That's not what I meant, Ayesha."
            show ayesha a normal
            "I see her frown ease a little at my reassurance."
            "But there's still the hint in her eyes that she feels slighted by what I just said."
            ayesha.say "Okay, [hero.name]."
            show ayesha a happy
            ayesha.say "Let's just forget about it and enjoy ourselves, yeah?"
            "I nod my agreement, eager to put the whole matter behind us."
            show ayesha a normal
            "We spend the rest of our visit to the aquarium in almost complete silence."
            "The only thing that makes either of us speaks is to point out something particularly colourful or interesting."
            "And as much as I try to forget my earlier faux pas, it hangs over us the entire time."
            "By the end of the date, I've already vowed to myself to be more sensitive with Ayesha in future."
            "That, and to get over my own hang-ups about dating an unexpectedly smart girl too!"
        "Why not":
            "I can't help smiling at the way Ayesha just seems to reel of the information."
            "It seems such a contrast to the image that she presents."
            "A wonderful revelation that casts her in an entirely new light."
            mike.say "You bet I do!"
            "Taking hold of Ayesha's hand, I almost pull her from one tank to the next."
            show ayesha b happy
            ayesha.say "Amphirion ocellaris - Clownfish."
            mike.say "Okay, that's a freebie."
            ayesha.say "Hippocampus erectus - Seahorse."
            mike.say "You sure you can't see these signs?"
            show ayesha b normal
            ayesha.say "Gymnothorax polyuranodon - Moray Eel."
            mike.say "Yeah...right again."
            "After what feels like the same process being repeated dozens of time, I can only admit defeat."
            mike.say "That's it, Ayesha."
            mike.say "You win!"
            show ayesha b happy
            $ ayesha.love += 2
            "I can't help but see the look of satisfaction on Ayesha's face at my admission."
            "But it's not just the gloating of the victor either, there's something else in her eyes too."
            "It's almost like she's basking in the way that I'm looking at her, realising how smart she actually is."
            mike.say "That's amazing, Ayesha."
            mike.say "It's like you know everything about everything!"
            ayesha.say "That's a bit much, [hero.name]."
            show ayesha b normal
            ayesha.say "Let's just say I know a hell of a lot about SOME things, yeah?"
            mike.say "I never would have thought..."
            show ayesha b joke
            ayesha.say "What - that I had a brain inside of my head?"
            "Suddenly I feel embarrassed and more than a little ashamed at what I just said."
            "How could I have let myself prejudge Ayesha like that?"
            "I'm supposed to be a modern, open-minded kind of guy."
            "Not some kind of jerk that's just assume she was a dumb muscle-freak!"
            mike.say "I'm sorry, Ayesha - I should have known better."
            mike.say "I guess you just surprised me, that's all."
            show ayesha b happy
            ayesha.say "Ah, it's okay, [hero.name]."
            show ayesha b normal
            ayesha.say "At least you said sorry - most guys never get that far!"
            ayesha.say "I wasn't born and raised inside of a gym."
            "I feel Ayesha squeeze my hand, reminding me that she's been holding my hand this whole time."
            show ayesha b happy
            ayesha.say "Anyway, weren't we supposed to be on a date?"
            "I nod at this, glad to be able to move on from what could have been a prickly subject."
            "With the air cleared, the rest of the visit to the aquarium goes more smoothly."
            "While Ayesha doesn't flinch from dispensing her knowledge, I also manage to score a couple of hits myself."
            "And by the end date, I can't help feeling that I've learned a great deal about Ayesha as a person."
            "As well as renewed respect for the incredible brain that she keeps inside of that astonishing body too..."
    scene bg black with dissolve
    $ game.active_date.score += 50
    $ DONE["ayesha_date_aquarium"] = game.days_played
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
