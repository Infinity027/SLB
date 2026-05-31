label harmony_date_intro_valentine_male:
    mike.say "Happy Valentine's day, Harmony!"
    mike.say "I'm so glad that you're my date tonight."
    mike.say "Because I couldn't imagine a more perfect valentine than you!"
    if harmony.purity >= HP:
        show harmony happy
        harmony.say "Aww...that's so sweet, [hero.name]!"
        harmony.say "I feel the exact same way about you too."
    elif harmony.purity < VLP:
        harmony.say "Keep talking to me like that, [hero.name]."
        show harmony blush
        harmony.say "You're making me feel SO horny!"
    else:
        harmony.say "I feel that way too, [hero.name]."
        show harmony happy
        harmony.say "Tonight's going to be so much fun!"
    return

label harmony_date_intro_halloween_male:
    mike.say "Hey, Harmony - I was wondering if you'd dress up for Halloween."
    mike.say "You know, maybe wear something spooky and sexy for me?"
    "Harmony looks surprised by my question, like she'd forgotten all about it."
    if harmony.purity >= HP:
        show harmony annoyed
        harmony.say "I would never do a thing like that, [hero.name]."
        harmony.say "Halloween is a wicked, pagan festival!"
    elif harmony.purity < VLP:
        show harmony annoyed
        harmony.say "Oh damn it - I totally forgot!"
        show harmony happy
        harmony.say "Don't worry, [hero.name] - I'll wear something extra sexy next year!"
    else:
        harmony.say "Maybe next year, [hero.name]."
        harmony.say "Let's just have a good time on our date, okay?"
    "I nod, agreeing with Harmony's sentiment."
    "And it's also the best way to keep our date on course!"
    mike.say "That sounds great, Harmony."
    mike.say "Let's get going."
    return

label harmony_date_intro_christmas_male:
    mike.say "Happy Christmas, Harmony!"
    mike.say "Are you ready for our date?"
    show harmony happy
    "Harmony nods and smiles at this."
    if harmony.purity >= HP:
        harmony.say "So long as you keep the true meaning of Christmas in your heart, [hero.name]."
        harmony.say "Remember - it's all about celebrating the birth of Jesus!"
    elif harmony.purity < VLP:
        harmony.say "You bet I am, [hero.name]!"
        harmony.say "I'm sick of this 'real meaning of Christmas' bullshit."
        harmony.say "I want to party!"
    else:
        harmony.say "Yeah, [hero.name] - I need a chance to relax and have some fun!"
    return

label harmony_date_intro_birthday_male:
    mike.say "Happy birthday, Harmony!"
    mike.say "And because it's your birthday, I want to make our date super-special too!"
    if harmony.purity >= HP:
        show harmony happy
        harmony.say "Bless you, [hero.name]!"
        harmony.say "And let's have some good, clean fun together."
    elif harmony.purity < VLP:
        show harmony happy
        harmony.say "Oooh...that sounds SO intriguing!"
        show harmony blush
        harmony.say "I hope it involved getting naked and doing it like animals!"
    else:
        harmony.say "Wow, [hero.name] - you remembered!"
        show harmony happy
        harmony.say "I thought guys weren't supposed to do that?"
    return

label harmony_date_intro_mc_birthday_male:
    mike.say "You ready for our date, Harmony?"
    if harmony.purity >= HP:
        harmony.say "First things first, [hero.name]..."
        show harmony happy
        harmony.say "Happy birthday to you!"
    if harmony.purity < VLP:
        harmony.say "Not until I wish you a happy birthday, [hero.name]."
        show harmony blush
        harmony.say "I want a LONG birthday kiss too - with lost of tongues!"
    else:
        harmony.say "Yeah, [hero.name]..."
        show harmony happy
        harmony.say "But I wanted to wish you a happy birthday first!"
    mike.say "Aw...thanks, Harmony!"
    mike.say "It's so great that you remembered."
    return

label harmony_date_eat_a_burger:
    if harmony.purity >= HP:
        "Almost as soon as the food arrives, I can see the look on Harmony's face and know that I've made a mistake here."
        "She eyes the burger like it was a thing of the devil, sent from hell itself to torment her."
        "At the very most, she awkwardly nibbles the edge of the bun and maybe a little of the garnish, but nothing else."
    elif harmony.purity < VLP:
        "At the sight of the burger being placed before her, Harmony's eyes practically light up."
        "Not waiting for me to start eating, she positively tears into the burger and devours it as though she were starving."
        "Harmony polishes off her food long before I do, and licks her fingers with a look of extreme satisfaction on her face."
    else:
        "Harmony seems to welcome the arrival of her food, smiling and making all the signs that she's hungry."
        "She eats with an appetite, but the burger never really takes up all of her attention as she does so."
        "In the end, she leaves a little of the food, yet seems to have been satisfied with what she did eat."
    return

label harmony_date_buy_drink:
    if harmony.is_visibly_pregnant:
        show harmony angry
        $ harmony.love -= 10
        harmony.say "What, and hurt the child growing inside of me?!?"
        harmony.say "Have you gone mad, [hero.name]?"
        harmony.say "Are you possessed by spirits of a demonic kind?!?"
        $ hero.cancel_activity()
        hide harmony
    else:
        if harmony.purity >= HP:
            "At the very mention of drinking alcohol, Harmony turns her nose up and shakes her head."
            "She mutters something about it being the root of all evil and shakes her head for a second time."
            "In the end, she makes me feel awkward holding my own drink too."
        elif harmony.purity < VLP:
            "Whatever I'm having, Harmony seems to want the same - and in equal measures too!"
            "She doesn't hold back once the glass is in her hand, draining it with some considerable speed too."
            "It's all that I can do to keep up with her as she finishes her drink off and looks to where the next is coming from."
        else:
            "Harmony accepts the offer of a drink, but settles for a small measure of something not too strong."
            "She sips this drink sparingly, seeming to be making it last as long as possible."
            "Though whether she's aware of doing this or not, I really can't tell."
    return

label harmony_date_play_darts:
    if harmony.purity >= LP:
        "Harmony looks at the darts in her hand as though they're bloodied knives I've just pulled out of something dead and bleeding."
        "She tosses them away in the same fashion as well, chucking them in the vague direction of the board."
        "More often then not, they bounce off the wall, almost hitting an innocent bystander."
    else:
        "Harmony opines that she has no idea how to play a game of darts, but that she's willing to be taught."
        "This means that I have to lean in close behind and talk her through every single stage of the process."
        "Though I'm not sure how much leaning backwards and grinding her backside into my groin actually helps her game..."
    return

label harmony_date_pub_play_pool:
    if harmony.purity >= LP:
        "Harmony grudgingly agrees to play a game of pool, but she puts no visible effort into it."
        "Most of the time she just seems barely hit the cue ball, let alone anything else."
        "Before too long, I'm happy to pot my own balls, one after another, just to get it over with."
    else:
        "While Harmony claims to be completely hopeless at pool, she certainly leaps at the chance of a little tuition."
        "And the result is that I find it hard to concentrate on the game myself."
        "Who wouldn't, pressed so close behind her as she bends over the table and spreads her legs for each and every shot?"
    return

label harmony_date_buy_a_round:
    if harmony.is_visibly_pregnant:
        show harmony angry
        $ harmony.love -= 10
        harmony.say "What, and hurt the child growing inside of me?!?"
        harmony.say "Have you gone mad, [hero.name]?"
        harmony.say "Are you possessed by spirits of a demonic kind?!?"
        $ hero.cancel_activity()
    elif (hero.charm >= 60 - harmony.love and harmony.flags.drinks < 2):
        show drink harmony
        if harmony.purity >= HP:
            "Harmony takes almost no notice of me as I get up and announce my intention to buy another round."
            "And when I specifically ask her what she'd like to drink, she actually ignores me and looks the other way."
            "I guess I should have been better at picking up the signals that she's giving out!"
        elif harmony.purity > LP:
            "Harmony smiles sweetly and thanks me for the offer of another drink, requesting the same again."
            "She takes the glass and we return to our previous conversation, just where we left off."
            "It seems she's grateful for my buying her a drink, but not about to drop her panties over it!"
        else:
            "Harmony nods enthusiastically as I get up to fetch another round, fixing me with her huge eyes and wide smile."
            "She seems to be well-oiled already, but she's a big girl, and should know her own limits."
            "Almost as soon as she has the drink in her hands, she's draining it and looking at me with almost hungry eyes!"
        $ game.active_date.score += 5
        if "rebel" in harmony.traits:
            $ game.active_date.score += 5
        $ harmony.set_flag("drinks", 1, "day", mod="+")
        hide drink
    else:
        "I want to pay a round of beers to the whole pub."
        "But Harmony doesn't seem to want to drink, so I refrain from doing so."
        $ hero.cancel_activity()
    return

label harmony_dance_with:
    if harmony.purity >= LP:
        "Harmony is reluctant at first, but eventually I talk her round into dancing with me."
        "She's shy as we take a spot and begin to move to the music, blushing all the time."
        "But that just makes the experience of dancing with her all the more sweet and enjoyable for me!"
    else:
        "Almost as soon as she's on the dance-floor, Harmony becomes like a woman possessed."
        "No matter what track the DJ chooses to play, she presses herself against me, grinding without mercy."
        "In the end, it's me that has the trouble moving, thanks to the effect she's having on my manhood!"
    return

label harmony_date_play_arcade_intro_male:
    if harmony.purity >= LP:
        harmony.say "I'm not sure about this, [hero.name]."
        harmony.say "Places like this are pretty sinful!"
    else:
        harmony.say "This is going to be boring, [hero.name]."
        harmony.say "Can't we go do something a bit more fun?"
    "I knew that it was a gamble inviting Harmony along to the arcade."
    "She's never shown much interest in videogames before."
    "But this is something that I love, and I wanted to share it with her."
    "I suppose I was hoping that there'd be something to pique her interest."
    mike.say "Just give it a chance, Harmony."
    mike.say "That's all I'm asking, yeah?"
    mike.say "Let's play a couple of games and see how it goes."
    mike.say "If you're not having fun after that, then we'll leave."
    harmony.say "Okay, [hero.name]."
    harmony.say "I'll try my best..."
    "I look around, searching for a likely game to try out."
    "And then my eyes settle on one that should do the trick."
    mike.say "How about this one, Harmony?"
    mike.say "'Nosferatu Nite'?"
    if harmony.purity >= LP:
        harmony.say "Vampires?"
        harmony.say "Those lustful minions of the Devil?!?"
    else:
        harmony.say "Urgh...vampires?"
        harmony.say "They're so not as hot as they used to be!"
    mike.say "You don't play a vampire in this game, Harmony."
    mike.say "You play a vampire slayer!"
    if harmony.purity >= LP:
        harmony.say "A holy warrior?"
        harmony.say "That's so cool!"
    else:
        harmony.say "I get to kill them?"
        harmony.say "I can make them bleed?!?"
    "I nod eagerly as I pump coins into the slot."
    "Best to jump on the chance to play while Harmony still seems interested."
    return

label harmony_date_play_arcade_win_male:
    "Almost as soon as we start playing the game, Harmony looks flustered."
    "And when the action begins to heat up, it only gets worse!"
    harmony.say "Argh!"
    harmony.say "What's that?!?"
    harmony.say "Help me, [hero.name] - shoot it!"
    mike.say "Your gun works too, Harmony."
    mike.say "We could kill it quicker if we both shoot it!"
    "What follows is an agonising game where I do most of the work."
    "Harmony flinches from every jump-scare."
    "And she shoots in the wrong direction most of the time too."
    "By the time our credits have run out, she's a nervous wreck."
    "Which is reflected in the scores."
    mike.say "Ah...you can open your eyes now, Harmony."
    mike.say "The game's over, and there are no more vampires."
    harmony.say "You promise, [hero.name]?"
    mike.say "I promise, Harmony."
    harmony.say "So...can we go now?"
    mike.say "Yes, Harmony, we can go."
    mike.say "I think we really should try something else..."
    return

label harmony_date_play_arcade_lose_male:
    "Almost the moment we start playing, Harmony undergoes a transformation."
    "Where before she was unsure and intimidated, now she's surging with confidence."
    harmony.say "Take that, minion of evil!"
    harmony.say "My bullets are going to end you!"
    harmony.say "Come on, [hero.name] - we've got vampires to slay!"
    mike.say "Whoa..."
    mike.say "Slow down, Harmony!"
    mike.say "Leave some of them for me!"
    "What follows is a complete slaughter."
    "Harmony guns down everything in her path."
    "And all I can do is follow in her wake."
    "By the time we're done, she's left me in the dust."
    mike.say "Ah...you can stop shooting now, Harmony."
    mike.say "The game's over, and there are no more vampires."
    harmony.say "Aw..."
    harmony.say "And I was having so much fun!"
    harmony.say "So...we have to go now?"
    mike.say "Yes, Harmony, we do."
    mike.say "I think we really should try something else..."
    return

label harmony_dick_reactions:
    if not harmony.flags.seendick:
        $ harmony.flags.seendick = 1
        if hero.has_skill("hung"):
            show dick reactions harmony scared
            harmony.say "Oh, good lord!"
            harmony.say "I never thought one could be THAT big!"
            mike.say "Hah...yeah...it is kind of big, I guess!"
            harmony.say "B...but still, it's a part of God's miracle."
            show dick reactions harmony smile
            harmony.say "And so I...I should be thankful for it..."
            $ harmony.sub += 10
            $ harmony.purity -= 10
        elif hero.has_skill("smalldick"):
            show dick reactions harmony smile
            harmony.say "My goodness - it's so tiny!"
            mike.say "Hey - that's not something a guy likes to hear!"
            harmony.say "No, I mean it's small - but it's perfectly formed."
            harmony.say "It's like God made a little work of art!"
            mike.say "Thanks...I guess..."
            $ harmony.sub -= 10
        hide dick reactions
    return

label harmony_halloween_invitation:
    show harmony
    "I knew that Harmony was the girl that I wanted to invite to the Halloween party from the start."
    "There was no need to sit down and ponder my options, as she's almost always on my mind anyway!"
    "The only problem is that I have to be really careful about how I choose to ask her."
    "She's the sensitive type, and I don't want to say something that sinks my chances."
    "That's why I try to mention it in passing, not just come right out and say it."
    mike.say "Wow..."
    mike.say "Can you believe it's that time of year already?"
    show fx question
    harmony.say "Hmm..."
    harmony.say "What, you mean that it's Autumn?"
    mike.say "That's right, Harmony."
    mike.say "That's exactly what I mean."
    show harmony happy
    "Harmony treats me to a broad, genuine smile."
    "And she nods her head happily."
    harmony.say "I know what you mean, [hero.name]."
    harmony.say "I love this time of year too."
    harmony.say "The leaves turning to flame."
    harmony.say "The nights drawing in."
    show harmony normal
    "Then she blushes a little before going on."
    harmony.say "Snuggling up with someone special!"
    "Wow..."
    "That's a nice mental image!"
    "But what was I supposed to be talking about?"
    "Oh yeah - Halloween!"
    mike.say "And Halloween, Harmony."
    mike.say "Don't forget Halloween!"
    show harmony sad
    harmony.say "Oh..."
    harmony.say "Of course not."
    mike.say "Talking of Halloween..."
    mike.say "We're having a party at my place."
    mike.say "And I was wondering if you wanted to come?"
    mike.say "You know - as my date?"
    if harmony.purity < HP and harmony.purity >= LP and (harmony.love >= 100 or harmony.sub >= 40):
        "Harmony looks a little awkward, maybe even embarrassed."
        harmony.say "I...I think I'd like that, [hero.name]."
        harmony.say "It's just...well..."
        harmony.say "I've never been to a Halloween party before."
        mike.say "You're kidding, right?!?"
        show harmony normal
        "Harmony blushes at my amazement."
        harmony.say "My parents were very strict, [hero.name]."
        harmony.say "Especially when it came to religion."
        harmony.say "They believed that celebrating Halloween was like worshipping the devil!"
        mike.say "Wow, Harmony!"
        mike.say "Look, I can promise you it's not going to be like that."
        mike.say "There's only going to be evil spirits if someone spikes the punch."
        show harmony happy
        "Harmony nods and treats me to a smile."
        harmony.say "I'll be okay, [hero.name]."
        harmony.say "So long as you promise to look after me."
        mike.say "Of course I will, Harmony."
        mike.say "And trust me - you'll have a great time!"
        $ game.flags.halloween_girl = "harmony"
    elif harmony.purity < LP:
        show harmony mean
        "The grin that spreads across Harmony's face is instant."
        "In fact, it's more than a little scary too!"
        harmony.say "Are you talking about a real Halloween party, [hero.name]?"
        harmony.say "Naughty costumes?"
        harmony.say "Spiked punch?"
        harmony.say "Maybe even Ouija boards?!?"
        mike.say "Ah..."
        mike.say "I...I don't know about all of that, Harmony!"
        mike.say "It's just a chance for a bunch of us to get together, you know?"
        mike.say "Have a few drinks, play some games, have a good time."
        show harmony happy
        $ harmony.love += 1
        $ harmony.purity -= 1
        "Harmony nods eagerly."
        harmony.say "I am so up for that!"
        show harmony normal
        harmony.say "My parents were real hard-asses - so uptight."
        harmony.say "They never let me do anything sinful when I was a kid."
        mike.say "Yeah, I might be realising why they did that..."
        harmony.say "Huh?"
        harmony.say "What was that?"
        mike.say "Oh, nothing..."
        mike.say "So I can put you down on the guest-list then?"
        show harmony happy
        harmony.say "Of course..."
        show harmony blush
        harmony.say "And I know just the costume to wear too!"
        "Well, that went well."
        "But why does part of me feel a little scared right now?"
        $ game.flags.halloween_girl = "harmony"
    else:
        show harmony angry
        $ harmony.love -= 1
        "Harmony pulls away from me suddenly."
        "She shakes her head and waggles a finger at me."
        harmony.say "How can you have a party to celebrate Halloween, [hero.name]?"
        harmony.say "Don't you know that's the night Satan and his demons walk the earth?!?"
        mike.say "B...b...but Harmony!"
        mike.say "It's just a party - a harmless bit of fun!"
        harmony.say "No, [hero.name], it's a gateway to worshipping the Devil!"
        harmony.say "I'll be doing what I always do that night."
        mike.say "And that is...what, exactly?"
        harmony.say "Taking part in a prayer vigil at church of course!"
        show harmony normal
        harmony.say "And you should join me too."
        mike.say "Ah...let me get back to you on that one, Harmony."
        mike.say "It sounds like you're too wild for me!"
    return

label harmony_halloween_arrival:
    scene bg house
    with wiperight
    "Opening the door, I guess I should have been more cautious."
    "Especially after the incidents with Jack's sword and Scottie's trident."
    show harmony close halloween down at cleavage with hpunch
    "But I get caught out again as something big and soft hits me in the face."
    mike.say "Mmmm..."
    mike.say "Mmmh..."
    mike.say "Can't...breathe!"
    harmony.say "Oops..."
    harmony.say "Sorry about that [hero.name]!"
    hide harmony
    show harmony halloween down
    with hpunch
    "It's only when Harmony takes a step back that I see what was smothering me."
    "And even when I do, I still can't summon the power of speech."
    "All I can do is stare at the dress that's clinging to Harmony's body."
    "It's red and shows off every curve, paired with long, purple opera gloves."
    "Her hair is dyed red and combed over one eye that's heavily made-up."
    mike.say "J...Jessica..."
    mike.say "Jessica Bunny!"
    harmony.say "What do you think, [hero.name]?"
    harmony.say "I'm not bad...I'm just dressed that way!"
    menu:
        "Compliment":
            mike.say "Wow..."
            mike.say "Harmony...you look..."
            mike.say "Amazing...you look amazing!"
            show harmony happy
            $ harmony.love += 1
            "Harmony smiles and lets out a happy giggle."
            "And that in turn makes her chest jiggle in sympathy."
            harmony.say "I'm so glad you like it, [hero.name]."
            "All I can do is nod in stunned silence."
            "I want to shove my head straight back between her breasts!"
            mike.say "Y...yeah, Harmony."
            mike.say "I love it."
            show harmony normal
            harmony.say "Great...that's great."
            harmony.say "Ah..."
            harmony.say "Should we not go inside?"
            harmony.say "I mean, like sometime tonight?"
            "I finally manage to snap myself out of it."
            mike.say "Oh...yeah..."
            mike.say "Where are my manners!"
            mike.say "Come on in, Harmony."
        "Criticize":
            mike.say "Ah..."
            mike.say "It's a bit much, Harmony."
            show harmony sad
            "As what I'm saying sinks in, I see Harmony frown."
            "She shakes her head as she questions my reaction."
            harmony.say "I don't understand, [hero.name]."
            harmony.say "I thought that you like this kind of thing?"
            harmony.say "You always encourage me to dress provocatively."
            mike.say "Maybe when we're going out to a club or for a meal."
            mike.say "But this is just a house-party."
            mike.say "I don't want all of my friends staring at you."
            show harmony angry
            $ harmony.love -= 4
            "Harmony becomes defensive at this."
            "She crosses her arms over her chest."
            harmony.say "Oh, I get it now."
            harmony.say "It's okay for you to stare at me."
            harmony.say "But not anyone else, right?"
            harmony.say "You're jealous I'll get other guys looking at me!"
            mike.say "Yes..."
            mike.say "I mean no..."
            mike.say "Ah...let's talk about it later."
            mike.say "You're here now, so that's that."
    scene bg black with dissolve
    pause 1
    return

label harmony_halloween_party:
    $ game.pass_time(2)
    scene bg livingroom
    show harmony halloween down at right5
    show scottie halloween perv at left5
    with fade
    scottie.say "Whoa..."
    scottie.say "How much to those things weigh?!?"
    harmony.say "Oh my..."
    harmony.say "Are you talking to little old me?"
    "I turn around to see Scottie talking to Harmony."
    "His eyes are almost bursting out of his head."
    "And I can hardly blame him."
    "Harmony's an impressive sight in that dress."
    "But she's my date tonight."
    "And she's not exactly acting like it!"
    menu:
        "Play along":
            mike.say "They're something else."
            mike.say "Huh, Scottie?"
            show scottie -perv
            scottie.say "Y...yeah, dude!"
            mike.say "But they're all mine."
            mike.say "So you need to find some puppies of your own!"
            "I put an arm around Harmony, pulling her close to me."
            show harmony happy
            $ harmony.love += 2
            "She giggles and presses herself against my side."
            "And Scottie shakes himself, like he just snapped out of it."
            scottie.say "Uh...yeah..."
            scottie.say "Sure thing, dude."
            show scottie blush
            scottie.say "I was just looking - that's all!"
            "I nod at this."
            mike.say "Look all you like, Scottie."
            mike.say "But only I get to touch!"
        "Protest":
            mike.say "Hey, Scottie - back off!"
            mike.say "Harmony's my date tonight."
            mike.say "And I don't appreciate you hitting on her!"
            show scottie -perv
            "And Scottie shakes himself, like he just snapped out of it."
            scottie.say "Uh...yeah..."
            scottie.say "Sure thing, dude."
            show scottie blush
            scottie.say "I was just looking - that's all!"
            "I nod at this."
            mike.say "Look all you like, Scottie."
            mike.say "But only I get to touch!"
            hide scottie
            show harmony halloween down angry at center
            with moveoutleft
            $ harmony.love -= 2
            "Harmony lets out a huff as Scottie hurries away."
            harmony.say "I was just flirting, [hero.name]."
            harmony.say "No need to be such a killjoy!"
    scene bg black with dissolve
    pause 1
    return

label harmony_halloween_dance:
    $ game.pass_time(2)
    scene bg livingroom
    show harmony halloween down
    with fade
    harmony.say "Hey, [hero.name]."
    harmony.say "We should get on the dance-floor!"
    "Harmony sounds like she's not going to take no for an answer."
    mike.say "Ah..."
    mike.say "Why, Harmony?"
    mike.say "Is this a song you like?"
    show harmony happy
    "Harmony lets out a giggle and shakes her head."
    harmony.say "What?"
    harmony.say "Oh no, I never heard it before."
    show harmony normal
    harmony.say "I just feel like I want to dance!"
    menu:
        "Accept":
            "I've already seen Harmony eyeing up Jack and Scottie."
            "And I know that they've noticed her too."
            "But what good is trying to keep her under wraps going to do?"
            "Maybe the opposite approach is the way to go?"
            mike.say "Sure, Harmony."
            mike.say "Let's go dance!"
            show harmony happy
            $ harmony.love += 2
            "Harmony claps her hands together in delight."
            hide harmony with dissolve
            "And I lead her out onto the makeshift dance-floor."
            "Harmony makes her intentions clear from the start."
            show dance harmony halloween with fade
            "She presses herself up against me, holding me tight."
            "I do the same, feeling the inviting softness of her body."
            "I can't help letting out all the air in my lungs."
            mike.say "Phew..."
            mike.say "You feel so soft, Harmony!"
            harmony.say "Mmm..."
            harmony.say "You feel good too, [hero.name]."
            $ harmony.sub += 1
            $ harmony.purity -= 1
            harmony.say "Nice and hard!"
            "Harmony giggles as I realise she's right."
            "Now I need to keep a hold of her for another reason."
            "And that's to hide how hard she's making me!"
            "Needless to say, the dance that follows isn't all that wild."
            "As I spend the whole time embracing Harmony, holding her close."
        "Refuse":
            "I can't help raising my eyebrows at this."
            "Harmony's already made me suspicious of her motives."
            "She pretty much eyed up Jack and Scottie right in front of me."
            "So the last thing I want to do is let her flaunt herself."
            mike.say "I don't think so, Harmony."
            show harmony sad
            harmony.say "Aww..."
            harmony.say "Why not?"
            mike.say "I want to wait for the right song."
            mike.say "Don't worry - I'll tell you as soon as I hear it."
            $ harmony.love -= 2
            "Harmony crosses her arms over her chest."
            "Which in the dress she's wearing is no mean feat."
            harmony.say "Huh..."
            harmony.say "You're no fun!"
    scene bg black with dissolve
    pause 1
    return

label harmony_halloween_sex:
    if harmony.purity < VLP:
        scene bg livingroom with timelaps
        "It's getting late by now, and while the party's not over it is winding down."
        "Everyone's either drunk, tired or both and happy to relax, rather than live it up."
        show harmony halloween down with dissolve
        "But all it takes is one glance at Harmony to tell that she's the exception."
        "Sure, she might look as calm and sedate as anyone else that's still here."
        "But I can tell from the look in her eyes that she's got a reserve of energy left."
        "And as soon as it looks like we're alone, she springs into action."
        harmony.say "Hey, [hero.name]!"
        mike.say "Ah, yeah, Harmony?"
        harmony.say "Where's one of your housemates' bedrooms?"
        "The question is so strange that I can't answer it at first."
        "I just end up shaking my head and looking baffled."
        mike.say "What?"
        mike.say "It's up the stairs on the left."
        mike.say "Do...do you want to go to sleep?!?"
        show harmony mean
        "Harmony laughs at the suggestion, shaking her head."
        "She still has that eager, slightly crazy look in her eye."
        harmony.say "No, no, no!"
        harmony.say "I want you to fuck me in there."
        "Again I'm left blinking and confused."
        "Harmony's so blunt and matter-of-fact."
        "It takes me a moment to get what she actually just said."
        mike.say "You want to have sex - in my housemate's bed?"
        "Harmony nods."
        mike.say "But...why don't we just use my bed?"
        mike.say "It's actually closer - and it'd be more comfortable."
        show harmony sad
        harmony.say "That's no fun, [hero.name]!"
        show harmony mean
        harmony.say "This is a party."
        harmony.say "And people sneak off to fuck at parties!"
        mike.say "I guess so, Harmony..."
        "Before I can say another word, Harmony grabs my wrist."
        scene bg secondfloor with fade
        "And then she's dragging me off in the direction of Sasha's bedroom."
        "Sure, I could put my foot down."
        "I could insist that it's my room or nothing."
        "But if Harmony wants to fuck in somebody else's, that's fine by me."
        "After all, it adds more than a little kink and thrill."
        "Harmony doesn't waste any time once she finds Sasha's bedroom."
        scene bg bedroom3 with fade
        "She opens the door and practically shoves me inside."
        "I stumble in, almost tripping over Sasha's bass on its stand."
        show harmony halloween down mean with dissolve
        "But before I can fall over, she's on me!"
        play sound door_slam
        "Harmony slams the door behind her and pounces."
        "I feel her body slam into mine, her arms wraps around me."
        "Her breasts and thighs are soft and warm, her lips too."
        "And it doesn't take me long to forget my discomfort."





        show harmony blush
        harmony.say "Mmm..."
        harmony.say "I've been waiting for this all night."
        harmony.say "My pussy's so wet..."
        harmony.say "It wants your cock..."
        show harmony missionary halloween mike with fade
        "We tumble onto the bed, Harmony landing on her back and me atop her."
        "I don't need to hear Harmony beg for it."
        "All it takes is a firm thrust, forwards and up..."
        show harmony missionary vaginal orgasm
        harmony.say "Oh fuck..."
        harmony.say "That's it..."
        show harmony missionary player blush
        harmony.say "Fuck me, [hero.name]...fuck me hard!"
        "Sliding into Harmony feels like nothing else in the world."
        "She's as soft and welcoming on the inside as she is on the outside."
        show harmony missionary orgasm
        "I enjoy pushing as deep into her as I can possibly go."
        "And every inch of the way I hear her moan in delight."
        "Turning the tables on Harmony, I pin down on the mattress."
        show harmony missionary speed with hpunch
        "And then I start to pick up speed, pounding her ever harder."
        "She takes everything that I have to give, wrapping her legs around me."
        "Her curves are more than able to handle it, absorbing my thrusts with ease."
        "I can hear myself panting and straining as I fuck Harmony."
        "And there's no way to ignore the pounding of my heart too."
        "I guess I must have had more energy in reserve than I thought."
        "Which is a good thing, because Harmony wants everything I have!"
        "By now her dress has slipped down to reveal her breasts."
        "And I can't keep from pushing my face between them."
        "It's only this close you see how big they really are."
        "I'm sure that I could suffocate in Harmony's cleavage."
        "And those nipples - stiff and standing to attention."
        "Before I know it, one of them is in my mouth."
        "And I'm sucking on it for all I'm worth!"
        harmony.say "Oh..."
        harmony.say "Oh god..."
        harmony.say "I'm gonna cum!"
        with hpunch
        "Harmony squeezes me with her thighs."
        show harmony missionary ahegao creampie with hpunch
        "And her pussy clenches my cock like a fist."
        with hpunch
        "I'm not sure, but I think we come at the same time."
        "And I'm more than a little amazed that we don't break Sasha's bed in the act."
        $ harmony.sexperience += 1
        $ game.pass_time(1)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
