label hanna_date_intro_valentine_male:
    mike.say "Wow, Hanna..."
    mike.say "I must have the best looking valentine ever!"
    mike.say "I just can't take my eyes off you."
    "Hanna smiles and waves away my compliments like they're nothing."
    "But I can see how happy they're making her, so happy she almost purrs like a cat."
    hanna.say "Oh, don't be silly, [hero.name]!"
    hanna.say "The only guy I want looking at me tonight is you..."
    return

label hanna_date_intro_halloween_male:
    mike.say "Hey, Hanna - we should have dressed up for Halloween."
    mike.say "You know, maybe gone a bit goth and spooky?"
    "Hanna raises an eyebrow, as if she's considering my point."
    hanna.say "Oh yeah, you're right, [hero.name]."
    hanna.say "Geez, we should have thought of that!"
    hanna.say "I could have worn something really tight and eye-catching, you know?"
    "Suddenly my mind is filled with possibilities."
    mike.say "That would have been great, Hanna!"
    mike.say "We should really try to remember next year."
    return

label hanna_date_intro_christmas_male:
    mike.say "Hey, Hanna - merry Christmas!"
    "Hanna makes a huffing noise and shakes her head."
    hanna.say "Whatever, [hero.name], whatever."
    hanna.say "Urgh...I just don't like the cold!"
    mike.say "You mean it makes you feel uncomfortable?"
    hanna.say "No...I don't like having to wrap up like this."
    hanna.say "It means nobody can see all the hard work I've been putting in at the gym!"
    return

label hanna_date_intro_birthday_male:
    mike.say "Happy birthday, Hanna!"
    mike.say "And may I say, you're looking particularly fantastic tonight."
    mike.say "You make me feel like I'm the one getting a birthday treat!"
    hanna.say "Aw, [hero.name]!"
    hanna.say "You can say that as much as you like."
    hanna.say "Because I never get tired of hearing it!"
    return

label hanna_date_intro_mc_birthday_male:
    mike.say "You ready for our date, Hanna?"
    hanna.say "I sure am, [hero.name]."
    hanna.say "But first things first - Happy birthday!"
    mike.say "Wow, Hanna!"
    mike.say "You remembered the date - that's pretty impressive."
    hanna.say "No, [hero.name], you dope!"
    hanna.say "You're signed up at my gym, remember?"
    hanna.say "I have all your details on file!"
    return

label hanna_date_pub_male:
    show hanna
    hanna.say "The Winchester?!?"
    hanna.say "I used to be in here watching sports all the time when I was at college!"
    hide hanna
    return

label hanna_date_cinema_male:
    show hanna
    hanna.say "Okay, but I usually watch films on TV."
    hanna.say "It's just so dark in the cinema - no one can see me."
    hanna.say "No, no - I mean I can't see anyone else, obviously..."
    hide hanna
    return

label hanna_date_familyrestaurant_male:
    show hanna
    hanna.say "Sure we can eat here, [hero.name]."
    hanna.say "As long as you don't mind all the parents."
    hanna.say "I mean, why do the dads all stare at me?"
    hanna.say "And the mom's - they all look like they want to kill me!"
    hide hanna
    return

label hanna_date_restaurant_male:
    show hanna
    hanna.say "Oh, wow - now this is a really classy joint."
    hanna.say "It's the kind of place you go to be SEEN!"
    hide hanna
    return

label hanna_date_amusmentpark_male:
    show hanna
    hanna.say "Places like this are always so full of life."
    hanna.say "So many people, and so many eyes all over you!"
    hide hanna
    return


label hanna_date_waterpark_male:
    show hanna
    hanna.say "The waterpark?"
    hanna.say "That's such a great idea - I just bought the cutest swimsuit!"
    hide hanna
    return

label hanna_date_park_male:
    show hanna
    hanna.say "Fresh air and a chance to stretch our legs with some exercise!"
    hanna.say "What's not to like about a walk in the park?"
    hide hanna
    return

label hanna_date_eat_a_burger:
    "Hanna almost begins to salivate at the sight of the burger."
    "She grabs hold of it with both hands, taking a huge bite and chewing with gusto."
    "I guess all the time she spends at the gym really works up an appetite!"
    return

label hanna_date_buy_drink:
    if hanna.is_visibly_pregnant:
        show hanna angry
        $ hanna.love -= 10
        hanna.say "Alcohol, [hero.name]?"
        hanna.say "Really?!?"
        hanna.say "Am I the only one looking out for this kid?"
        $ hero.cancel_activity()
        hide hanna
    else:
        "Hanna takes the drink I offer her and immediately swallows about half of it."
        "And I don't mean she sips it either - she knocks it back in one!"
        "Afterwards, Hanna smiles at me as she wipes the back of her hand across her lips."
    return

label hanna_date_play_darts:
    "Hanna almost leaps at the chance to play a round of darts with me."
    "And she doesn't take long to prove that she's way better at it than me as well."
    "She pretty much trounces me and doesn't hesitate to celebrate her victory either."
    return

label hanna_date_pub_play_pool:
    "Hanna accepts her cue like she's being offered a weapon to duel to the death."
    "And the game she plays is almost as ruthless and deadly too!"
    "In the end, it's all I can do to hold her to a draw."
    return

label hanna_date_buy_a_round:
    if hanna.is_visibly_pregnant:
        show hanna angry
        $ hanna.love -= 10
        hanna.say "Alcohol, [hero.name]?"
        hanna.say "Really?!?"
        hanna.say "Am I the only one looking out for this kid?"
        $ hero.cancel_activity()
    elif (hero.charm >= 60 - hanna.love and hanna.flags.drinks < 2):
        show drink hanna
        mike.say "Time for another?"
        hanna.say "Sure thing, [hero.name]."
        hanna.say "But sit down - it's my round!"
        $ game.active_date.score += 5
        if "rebel" in hanna.traits:
            $ game.active_date.score += 5
        $ hanna.set_flag("drinks", 1, "day", mod="+")
        hide drink
    else:
        "I want to pay a round of beers to the whole pub."
        "But Hanna doesn't seem to want to drink, so I refrain from doing so."
        $ hero.cancel_activity()
    return

label hanna_dance_with:
    "Hanna needs no convincing to get up and dance with me."
    "In fact, I have to chase after her in order to keep up!"
    "And when we get down to it, she dances up close and delightfully dirtily too..."
    return

label hanna_date_play_arcade_intro_male:
    hanna.say "Ah...this really isn't my kind of place, [hero.name]."
    hanna.say "I mean, sure, I'm into machines."
    hanna.say "But more the kind that you can work out on!"
    "It's hard for me to pay attention to Hanna in a place like this."
    "I love the arcade - it's one of my favourite spots to hang out."
    "But if she's not into it, then I owe it to Hanna to make the effort."
    mike.say "Yeah, Hanna, I know you're more the active type."
    mike.say "But videogames aren't just for fat slobs, you know?"
    mike.say "Some of these games you have to dance or run to play."
    mike.say "You always work up a sweat too!"
    "Hanna rolls her eyes at this."
    "And she lets out a sigh."
    hanna.say "Who wants to get hot and sweaty outside of the gym?"
    hanna.say "That just sounds really uncomfortable - disgusting too!"
    mike.say "But there are sports games too, Hanna!"
    mike.say "How about this one?"
    mike.say "'Crack and Peel' - that's all about athletics."
    "Hanna gazes over my shoulder at the arcade cabinet."
    "She frowns for a moment, but then nods her head."
    hanna.say "Hmm..."
    hanna.say "It does look pretty easy."
    hanna.say "If I play it, can we leave after?"
    mike.say "Sure thing, Hanna."
    mike.say "Just give it a chance."
    mike.say "And if you're still not having fun, we'll go someplace else."
    "That said, I start to pump coins into the slot."
    return

label hanna_date_play_arcade_win_male:
    "It's weird to watch Hanna trying to play the game."
    "I mean, she's normally pretty coordinated, graceful even."
    "And all you really need for this game is a little timing."
    "Well, that and the ability to pound the buttons like crazy!"
    "But for some reason, Hanna just can't seem to get the knack of it."
    hanna.say "Urgh..."
    hanna.say "Why is my guy running so slowly!"
    hanna.say "And why does he throw like a pussy?!?"
    mike.say "I honestly don't know, Hanna."
    mike.say "But you need to tone down the button bashing."
    mike.say "At this rate, you're going to break the game."
    mike.say "That or break your fingers!"
    "Soon enough the game is over and the dust settles."
    "And there's no disguising who's won the proverbial gold."
    "My score is way higher than Hanna's."
    hanna.say "There you go, [hero.name]."
    hanna.say "We played the dumb game."
    hanna.say "You won, I lost."
    hanna.say "Can we go now?"
    mike.say "I guess so, Hanna."
    mike.say "That was the deal..."
    "As we leave, I make a couple of mental notes."
    "The first is never to bring Hanna here again."
    "And the second is to remember that she's a really bad loser."
    return

label hanna_date_play_arcade_lose_male:
    "It's almost uncanny to watch Hanna as she plays the game."
    "But then all it really takes is a bit of basic timing."
    "Well, that and the ability to pound the buttons like crazy!"
    "It seems that Hanna's natural grace and coordination makes the difference."
    "Because she gets the knack of the game almost instantly."
    hanna.say "YES!"
    hanna.say "You can't catch me on the track!"
    hanna.say "And I just put that javelin into orbit!"
    mike.say "Slow down, Hanna!"
    mike.say "We're just playing a game, remember?"
    mike.say "At this rate I'm going to break the buttons."
    mike.say "That or my damn fingers!"
    "Soon enough the game is over and the dust settles."
    "And there's no disguising who's won the proverbial gold."
    "Hanna's score is way higher than mine."
    hanna.say "Woo!"
    hanna.say "She takes the winners podium."
    hanna.say "And the crowd goes wild!"
    hanna.say "Can you hear them chanting - 'Hanna...Hanna...Hanna'!"
    mike.say "Ah...okay, Hanna."
    mike.say "You won, but don't let it go to your head, yeah?"
    mike.say "Anyway...didn't you want to leave after we finished the game?"
    hanna.say "No way, [hero.name] - I want a rematch!"
    return

label hanna_dick_reactions:
    if not hanna.flags.seendick:
        $ hanna.flags.seendick = 1
        if hero.has_skill("hung"):
            show dick reactions hanna smile
            hanna.say "Mmm..."
            hanna.say "Hello - what have we here!"
            mike.say "Y...you like what you see, Hanna?"
            show dick reactions hanna tasty
            hanna.say "You bet, [hero.name]."
            hanna.say "Now let's see where we can put this monster!"
            $ hanna.sub += 10
        elif hero.has_skill("smalldick"):
            show dick reactions hanna smile
            hanna.say "Ah..."
            show dick reactions hanna mock
            hanna.say "Is that all that you got in there?"
            mike.say "Um...yeah, I guess so!"
            hanna.say "Well, I'm sure you can make up for it."
            show dick reactions hanna tasty
            hanna.say "You're just gonna have to work extra hard, okay?"
            $ hanna.sub -= 10
        hide dick reactions
    return

label hanna_halloween_invitation:
    show hanna
    "Of course there's only one girl that I want to invite to the Halloween party."
    "I can't imagine asking anyone but Hanna to be my date for the night."
    "And I'm pretty sure that she's going to say yes as soon as I ask her."
    "Because I know how much she likes to make an impression."
    "And what better place to do it than at a costume party?"
    "So as soon as the chance presents itself, I pop the question."
    mike.say "Hanna..."
    mike.say "Have you got any plans for Halloween?"
    show hanna surprised
    "Hanna looks around at the unexpected question."
    "Her expression one of genuine surprise and interest."
    hanna.say "Halloween..."
    hanna.say "Hmm..."
    show hanna normal
    hanna.say "I can't say that I do."
    mike.say "That's great news!"
    mike.say "Well...I don't mean it's great that you have no plans."
    mike.say "What I mean is it's great because we're having a party at my place."
    mike.say "And I wanted to ask if you'd come as my date?"
    "Hanna raises her eyebrows at this."
    hanna.say "A party at your place?"
    hanna.say "That sounds like it could be fun."
    "I nod eagerly, trying to urge Hanna to say more."
    "Though she sounds interested, I not that she hasn't actually said yes."
    mike.say "It'll be a blast, Hanna."
    mike.say "It's a costume party too."
    mike.say "So you'd have to come dressed up!"
    "This last detail seems to spark something in Hanna's mind."
    "And I can almost feel that I'm about to get an answer."
    if hanna.love >= 100:
        hanna.say "You know what, I was going to pass on the invite."
        hanna.say "But then you said it was a costume party."
        $ hanna.love += 1
        show hanna happy
        hanna.say "And I just LOVE the chance to get all dressed up!"
        "My head's nodding up and down more than ever by now."
        "And I'm grinning like an idiot too."
        mike.say "So you'll come, right?"
        mike.say "That's a yes?"
        hanna.say "Of course it's a yes, [hero.name]!"
        hanna.say "I wouldn't miss it."
        mike.say "Great, Hanna!"
        mike.say "That's just great!"
        "I pause for a moment as a thought occurs to me."
        "And when I go on, my tone changes as I try to sound nonchalant."
        mike.say "Say..."
        mike.say "What kind of a costume were you thinking of wearing?"
        mike.say "If you told me I could make sure nobody else thinks of it too..."
        show hanna normal
        "Hanna laughs and shakes her head."
        "And I know that she's seen straight through me."
        hanna.say "Nice try, [hero.name]!"
        hanna.say "You're just going to have to wait and see."
        show hanna flirt
        hanna.say "But I promise you won't be disappointed!"
        $ game.flags.halloween_girl = "hanna"
    else:
        $ hanna.sub -= 1
        show hanna annoyed
        hanna.say "You know what, I think I'll pass."
        "It takes me a moment to process what Hanna just said."
        "But then I shake my head, unable to believe that she said no."
        mike.say "B...but why, Hanna?"
        mike.say "We're going to have punch and music."
        mike.say "There's going to be a ton of people there too."
        mike.say "I swear on my life it won't be lame!"
        show hanna normal
        "Hanna gives me a condescending smile."
        "Which makes me feel like a kid having stuff explained to him by an adult."
        hanna.say "You're going to think I'm such a bitch, [hero.name]."
        hanna.say "But that's the kind of thing I used to do as a teenager."
        hanna.say "I'm not judging you or your friends."
        hanna.say "It's just that I prefer to act like an adult now that I am one!"
        "I open my mouth, preparing to argue the point with Hanna."
        "But then I shake my head and decide to let it go."
        "She's right, we're both adults."
        "So if she doesn't want to come to the party, that's the end of it."
        mike.say "Okay, Hanna."
        mike.say "If that's how you feel, no worries."
        "Hanna gives me another condescending smile."
        "And we move on to talk about something else instead."
    return

label hanna_halloween_arrival:
    scene bg house
    "I open the door, not really knowing what to expect."
    "I mean, I know that Hanna's something of an exhibitionist."
    "But does that really mean she's going to go over the top?"
    "It is just a Halloween party after all - a chance to have some fun."
    show hanna halloween
    hanna.say "Hi, [hero.name]!"
    hanna.say "I'm not late, am I?"
    "It takes me a moment to realise that Hanna actually asks a question."
    "And that's because my eyes are almost popping out of my head!"
    mike.say "N...no, Hanna..."
    mike.say "You're right on time!"
    show hanna flirt
    "Hanna seems to notice my state of amazement."
    "And her smile becomes even wider as a result."
    hanna.say "You like it, huh?"
    hanna.say "I just HAD to come as Rainbow Smash!"
    "Hanna has on dangerously short shorts and a vest."
    "Her hair is dyed a riot of different colours too."
    mike.say "What?"
    mike.say "Like the pony?"
    show hanna happy
    "Hanna nods her head happily."
    hanna.say "Yeah, that's right!"
    hanna.say "Isn't it great?"
    menu:
        "Compliment":
            "Of course it's great."
            "It means Hanna's turned up with everything on show."
            "And not in some dumb horse costume either!"
            mike.say "It's perfect, Hanna."
            mike.say "It says 'I'm a pony'."
            mike.say "But it doesn't saddle you with all the tackle!"
            show hanna annoyed
            "Hanna rolls her eyes at my deliberate puns."
            show hanna normal
            "But she seems inclined to let them go all the same."
            hanna.say "Well..."
            hanna.say "Maybe not all of the tackle..."
            "At this, my ears stand up."
            "Almost as high as the fake one's on Hanna's head."
            mike.say "Ah..."
            mike.say "What does that mean, Hanna?"
            hanna.say "Oh, you know..."
            $ hanna.love += 1
            show hanna flirt
            hanna.say "I like a chance to parade around."
            hanna.say "Maybe show off on the dance-floor."
            hanna.say "And I don't mind being ridden on occasion either..."
            mike.say "Huh..."
            mike.say "What was that last one?!?"
            show hanna normal
            "Hanna smiles as she breezes past me into the house."
            "And I follow, close on her heels."
        "Criticize":
            "I stand back a little and scrutinise Hanna's costume."
            "Then I shake my head, as I really don't get it."
            mike.say "How can you be Rainbow Smash, Hanna?"
            mike.say "You're just wearing some ears on your head."
            mike.say "I mean, where are you hooves and your tail?"
            $ hanna.love -= 2
            show hanna annoyed
            "Hanna looks at me with open amazement."
            "And she crosses her arms over her chest."
            hanna.say "I don't have to be an actual horse to be Rainbow Smash, [hero.name]!"
            hanna.say "They show up as humans all the time - everyone knows that!"
            "I frown at this, not convinced by Hanna's explanation."
            mike.say "If you say so, Hanna."
            mike.say "Call me old-fashioned if you like."
            mike.say "But I still think a pony needs hooves and a tail."
            hanna.say "Whatever, [hero.name], whatever."
            hanna.say "Can I just come inside?!?"
    scene bg black with dissolve
    pause 1
    return

label hanna_halloween_party:
    $ game.pass_time(2)
    scene bg livingroom
    with dissolve
    scottie.say "Whoa!"
    scottie.say "Now there's the kind of pony I can dig!"
    scottie.say "Are you giving out rides tonight or what?!?"
    "It takes me a moment to get my brain in gear."
    "But when I do, my head snaps around in Scottie's direction."
    "He's talking about ponies and rides in a lascivious manner."
    "And that means his attentions can only be focused on one guest at the party!"
    show scottie halloween perv at left5
    show hanna halloween flirt at right5
    hanna.say "Ha!"
    hanna.say "You think I could take your weight?"
    hanna.say "Maybe I'm not that kind of pony!"
    "I can tell from the tone of Hanna's voice that she's enjoying the chance to flirt."
    "And Scottie's not the kind to flinch at chatting up another guy's date."
    "I have to act fast if I want to avert potential disaster here."
    "But what can I do?!?"
    menu:
        "Outdo Scottie":
            mike.say "Hey, Scottie, back off."
            mike.say "This ride's already taken."
            mike.say "So you need to find one of your own!"
            $ hanna.sub += 2
            show hanna normal
            show scottie normal
            "Hanna and Scottie look around at me."
            "He looks surprised and a little embarrassed."
            "But Hanna's eyes light up at my words."
            "And I can see she's turned on too!"
            scottie.say "Oh...hey!"
            scottie.say "I didn't see you there, man."
            scottie.say "No worries - I was just joking around."
            "With that, Scottie nods his head."
            show hanna at center
            hide scottie
            with moveoutleft
            "And then he hurries off."
            mike.say "Sorry about that, Hanna."
            mike.say "Other guys can look all they want."
            mike.say "But nobody's riding you except me!"
            hanna.say "N...no worries, [hero.name]."
            hanna.say "It's all good."
            show hanna flirt
            hanna.say "So long as you make good on your promises!"
        "Tell Scottie and Hanna off":
            mike.say "Erm...hello!"
            mike.say "Do you two have no shame?"
            mike.say "I'm standing right here!"
            $ hanna.sub -= 1
            $ hanna.love -= 2
            show hanna annoyed
            show scottie normal
            "Hanna and Scottie look around at me."
            "He looks surprised and a little embarrassed."
            "But Hanna just glares at me with an annoyed expression."
            scottie.say "Oh...hey!"
            scottie.say "I didn't see you there, man."
            scottie.say "No worries - I was just joking around."
            "With that, Scottie nods his head."
            show hanna at center
            hide scottie
            with moveoutleft
            "And then he hurries off."
            hanna.say "Did you have to do that, [hero.name]?"
            hanna.say "The guy was just being nice!"
            "I look away, feeling like a petulant jerk."
            "And the best I can do is mutter something under my breath in way of an answer."
    scene bg black with dissolve
    pause 1
    return

label hanna_halloween_dance:
    $ game.pass_time(2)
    scene bg livingroom
    show hanna halloween annoyed
    with dissolve
    hanna.say "Come on, [hero.name]!"
    hanna.say "When are we going to dance!"
    "I can hear the impatience in Hanna's voice."
    "She's been eyeing up the makeshift dance-floor all night."
    "But somehow I don't feel the same urgency to get out there myself."
    "If only Hanna had been paying as much attention to me."
    "Then I might be able to say that I felt differently."
    hanna.say "Well?"
    hanna.say "Are you coming or not?!?"
    menu:
        "Dance":
            "So Hanna won't give me her attention, will she?"
            "In that case, I'm going to take it for myself!"
            show hanna normal
            mike.say "Sure thing, Hanna."
            mike.say "We should totally dance together."
            $ hanna.love += 2
            hide hanna
            show dance hanna halloween
            "Taking hold of Hanna's hand, I pull her onto the dance-floor."
            "From that moment on, I make her the centre of everything I do."
            "I watch her every move, matching it with my own."
            "I follow her wherever she goes, never taking my eyes off of her."
            "And, true to form, Hanna eats up the attention."
            "Everything she does, I let it wow me."
            "Making her feel like she's the only girl in the room."
            "It's like feeding a fire, then adding gasoline!"
            "We stay up for one song after another."
            "Hanna basking in my complete and unadulterated attention."
        "Do not dance":
            "It sounds like Hanna's going to dance whatever I say."
            "Which means that she can't care whether I join her or not!"
            mike.say "You know what, Hanna..."
            mike.say "I'm going to sit this one out."
            mike.say "But you feel free to..."
            "Before I can say the words, Hanna's off."
            "Like she doesn't even want my permission to leave me behind."
            hanna.say "Whatever, [hero.name]."
            hanna.say "Catch you later!"
            $ hanna.love -= 2
            hide hanna with moveoutleft
            "And just like that, she's gone."
            "I stand and watch as Hanna dances to one song after another."
            "First she dances with Jack."
            "Then she dances with Scottie."
            "Next she dances with Jack and Scottie at the same time."
            "And all I can do is keep telling myself that it's fine."
            "It's all fine, and I'm not in the slightest bit jealous..."
    scene bg black with dissolve
    pause 1
    return

label hanna_halloween_sex:
    scene bg livingroom
    show hanna halloween flirt zorder 3 at center
    show scottie halloween perv zorder 2 at left
    show jack halloween perv zorder 1 at right
    with dissolve
    "It's no secret that Hanna likes to have all the eyes in the room on her."
    "And she's done all she can tonight to make sure she was the centre of attention."
    "Hanna's been flirty and fun, the life and soul of the party."
    "Which means she's been admired both openly and from afar all evening."
    "Not that it really matters to me, or makes me crazily jealous."
    "Because most of her attention's been focused on me the whole time."
    "I see Jack and Scottie openly ogling Hanna more than once."
    "And all it does is make me feel that much luckier to have her as my date."
    "Plus I know that I'm the only one she's with once we make it to my bedroom."
    scene bg bedroom1
    show hanna halloween happy blush
    with dissolve
    "Hanna wastes no time now that we're finally alone."


    hanna.say "You've been a good boy, [hero.name]."
    show hanna flirt -blush
    hanna.say "And that means you get a reward!"
    "I nod eagerly, entranced by Hanna's gesture."

    "And I'm struggling to pay attention to her words."
    mike.say "Y..yeah, Hanna..."
    mike.say "Whatever you say!"
    "Hanna nods too, stopping as she reaches the foot of the bed."
    show hanna missionary halloween down with fade
    "She climbs backwards onto the mattress, pulling up her top."
    "This lets her breasts fall onto her chest, swaying with her motions."
    "And then she beckons me to come to her."
    hanna.say "You've been so good to me tonight."
    hanna.say "So you get to ride this little pony!"
    "As if to underline the point, Hanna spreads her legs apart."
    "She strokes the lips of her pussy with one hand."
    "And she crooks a finger with the other."
    "Maybe the most obvious invitation I've ever seen!"
    "I all but tear off the last of my clothes."
    "And then I'm on top of Hanna in a heartbeat."
    "She's already got me good and hard - how could she not?"
    "Which means it's a relief to feel how slippery she is too."
    "The head of my cock slithers along the lips of her pussy."
    show hanna missionary fuck pussy
    "And I'm inside of her before I know what's happening down there!"
    "Hanna moans deeply the moment I enter, pulling me closer."
    "I sink into her that much more quickly with her efforts."
    "My own gasp matching hers as I'm taken by surprise."
    show hanna missionary orgasm
    "Hanna's still nodding, letting me know that she wants more."
    "And so I shake myself back to reality and set about giving it to her."
    "I take Hanna's demands to mean that she wants it fast and hard."
    "She's held nothing back so far, and likely wants me to do the same."
    "If she wants to be ridden like a pony, the so be it!"
    "Standing at the foot of the bed, I take a firm hold of Hanna."
    show hanna missionary fuck
    "And then I begin to move back and forth."
    "In the space of a few moments, I'm going as fast as I can."
    "The last of my energy goes into pounding away at Hanna."
    "And she takes everything that I have left to give."
    "Her entire body is shaking, breasts bouncing and head bobbing."
    "Either that, or else she's nodding desperately, urging me on!"
    "I can hear myself panting with the effort this is taking."
    "My heart is beating like a jackhammer in my chest."
    "And still Hanna holds on in there, demanding that I give her more."
    "The sensation of being inside her like this is mind-blowing."
    "But it's been a long day, and I can't go on forever."
    "Where is she getting these reserves of energy from?"
    "Hanna's been drinking, dancing and partying all night, just like me."
    "She really does seem to have the stamina of an actual pony!"
    show hanna missionary blush
    "Just then, Hanna adds to the image of her equine nature by snorting."
    "She honestly lets out a sound like a whinnying horse."
    "And with a genuine sense of relief, I realise that she's about to cum!"
    "Feeling like I've been given permission, I let go too."
    show hanna missionary ahegao cum with vpunch
    "Hanna reaches her climax a moment later, her body tensing as it takes her."
    with vpunch
    "She wraps her legs around my waist and grabs me with her hands."
    with vpunch
    "Which means that I feel every twitch and spasm of her orgasm."
    "Once she's done, I pull my cock out of her and sit down on the bed."
    "Hanna curls up into a ball, making quiet, satisfied noises."
    "I wouldn't be surprised if she feel asleep in a few moments."
    "And I feel like I could join her soon afterwards."
    $ hanna.sexperience += 1
    $ game.pass_time(1)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
