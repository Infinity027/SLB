label lavish_date_intro_valentine_male:
    lavish.say "Happy Valentine's day, [hero.name]."
    lavish.say "I'm so looking forward to our date tonight!"
    "I nod eagerly, wanting to show Lavish that I feel the same way."
    mike.say "Me too, Lavish!"
    mike.say "I've been waiting for tonight a long time."
    mike.say "I want everything to be perfect."
    return

label lavish_date_intro_halloween_male:
    mike.say "You look amazing tonight, Lavish!"
    mike.say "I was going to ask if you wanted to get dressed-up for Halloween."
    mike.say "But now that I've seen what you're wearing...wow!"
    "Lavish smiles demurely, but I can see she's pleased with my flattery."
    lavish.say "Oh, dressing-up in costumes might have been fun."
    lavish.say "But I think I prefer to be dressed-up like this!"
    "All I can do is nod in agreement."
    mike.say "I can't argue with that, Lavish!"
    return

label lavish_date_intro_christmas_male:
    mike.say "Happy Christmas, Lavish!"
    mike.say "I'm really looking forward to our date."
    "Lavish smiles sweetly at this, but I can see the fatigue on her face."
    mike.say "Are...are you okay, Lavish?"
    lavish.say "Oh, I'll be fine, [hero.name]."
    lavish.say "I've just been working extra hard recently."
    mike.say "Oh, I see..."
    mike.say "Just relax tonight, Lavish - I'll take care of everything."
    return

label lavish_date_intro_birthday_male:
    mike.say "Happy birthday, Lavish!"
    lavish.say "Oh my...you remembered the date?"
    mike.say "Erm...yeah, Lavish."
    mike.say "Is that not a good thing?"
    lavish.say "No, no, no...it's fantastic."
    lavish.say "I just never thought you were so...organised, that's all!"
    return

label lavish_date_intro_mc_birthday_male:
    mike.say "Hey, Lavish - you ready for our date?"
    lavish.say "Sure, [hero.name], sure."
    lavish.say "But isn't today your birthday?"
    mike.say "Erm, yeah, it is."
    mike.say "Thanks for remembering, Lavish."
    lavish.say "Don't mention it, [hero.name]."
    lavish.say "I kind of pride myself on remembering stuff like that."
    return

label lavish_date_eat_a_burger:
    "Lavish seems happy with the burger from the moment that it arrives."
    "She eats delicately, but with a visible appetite."
    "And when she's done eating, she dabs the corners of her mouth with a napkin."
    return

label lavish_date_buy_drink:
    if lavish.is_visibly_pregnant:
        show lavish angry
        $ lavish.love -= 10
        lavish.say "Have you forgotten that one of us is pregnant, [hero.name]?!?"
        lavish.say "It wouldn't have slipped your mind if YOU were the one carrying our child!"
        $ hero.cancel_activity()
        hide lavish
    else:
        "Lavish accepts her drink gratefully and places it down next to her."
        "She traced the rim of the glass with and idle finger."
        "The whole time she smiles, and coyly averts her eyes."
    return

label lavish_date_play_darts:
    "Lavish looks at the darts that I've just handed her with something approaching actual fear."
    "She can't seem to tear her eyes away from the points."
    "And as a result, she tosses them without paying attention, sending her darts here and there, causing utter chaos."
    return

label lavish_date_pub_play_pool:
    "Although she doesn't look like a natural when it comes to holding a cue, Lavish seems to enjoy playing pool."
    "Unfortunately, she proves to also have no hidden talent for the game either."
    "But she perseveres any way, jumping up and down on the spot and clapping her hands when she finally manages to sink a ball."
    return

label lavish_date_buy_a_round:
    if lavish.is_visibly_pregnant:
        show lavish angry
        $ lavish.love -= 10
        lavish.say "Have you forgotten that one of us is pregnant, [hero.name]?!?"
        lavish.say "It wouldn't have slipped your mind if YOU were the one carrying our child!"
        $ hero.cancel_activity()
    elif (hero.charm >= 60 - lavish.love and lavish.flags.drinks < 2):
        show drink lavish
        "I get up and offer to buy the next round, and get a short nod in return."
        "I was expecting more enthusiasm, maybe a bit of thanks."
        "But then maybe Lavish is just too much of a modern girl to be impressed by that kind of thing?"
        $ game.active_date.score += 5
        if "rebel" in lavish.traits:
            $ game.active_date.score += 5
        $ lavish.set_flag("drinks", 1, "day", mod="+")
        hide drink
    else:
        "I want to pay a round of beers to the whole pub."
        "But Lavish doesn't seem to want to drink, so I refrain from doing so."
        $ hero.cancel_activity()
    return

label lavish_dance_with:
    "Lavish laughs and giggles the entire time that we're on the dance-floor together."
    "But far from being annoying, it only serves to make me aware of how much fun she's having."
    "Not that having her pressed so close to me in that kind of mood isn't fun for me too!"
    return

label lavish_date_play_arcade_intro_male:
    lavish.say "Do we really have to spend time here, [hero.name]?"
    lavish.say "I mean, videogames?"
    lavish.say "It's all a bit childish, isn't it?"
    "Lavish's words distract me from the lights and sounds of the arcade."
    "It's hard for me to believe that anyone wouldn't love this place."
    "Maybe what she needs is to find the right game for her?"
    mike.say "Most of these games are classics, Lavish."
    mike.say "Just like a book or a film."
    mike.say "Playing them is kind of a cultural experience!"
    "Lavish gives this a weak smile."
    "But it's clear to see that she's not convinced."
    lavish.say "Okay, [hero.name], okay."
    lavish.say "I did agree to come here."
    lavish.say "So let's get it over with!"
    mike.say "How about this one, Lavish?"
    mike.say "It's called 'Admin Girl'."
    mike.say "You have to navigate the office, filing stuff as you go."
    mike.say "But the whole time you have to avoid things that try to get you."
    mike.say "Like the possessed fax machine and the office pervert!"
    "This last comment seems to make an impression on Lavish."
    "She raises an eyebrow and looks sideways at me."
    lavish.say "Sounds oddly familiar..."
    "I should really ask Lavish what she means by that."
    "But I'm too busy pumping coins into the slot..."
    return

label lavish_date_play_arcade_win_male:
    "The game might feel familiar to Lavish, but that doesn't help her out."
    "And soon enough her lack of experience and enthusiasm starts to show."
    lavish.say "Oh dear..."
    lavish.say "Is that supposed to happen?"
    lavish.say "I don't know how anyone gets a thing done in this office!"
    lavish.say "It's like everything's out to get me!"
    mike.say "It's not supposed to be a real office, Lavish!"
    mike.say "Ooh...keep an eye on the pervert!"
    lavish.say "Which one?!?"
    "Things don't seem to get much better as the game progresses."
    "I've played it so many times that it's a breeze."
    "And once our last credits have been spent, I've racked up quite a score."
    "But Lavish hasn't even managed to come close."
    lavish.say "A game that's just like my real job."
    lavish.say "What a stupid idea!"
    mike.say "So..."
    mike.say "I take it that didn't change your mind about videogames?"
    lavish.say "No, [hero.name], it didn't!"
    lavish.say "Now you have to keep your side of the deal."
    lavish.say "Let's go do something else, okay?"
    return

label lavish_date_play_arcade_lose_male:
    "Maybe it's the familiar nature of the game's setting that does it."
    "Or maybe she just has an undiscovered natural talent for gaming."
    "Either way, Lavish takes to the game like a duck to water."
    lavish.say "Huh, this is just like the real thing!"
    lavish.say "You just need to know how to handle the workload, that's all."
    lavish.say "I deal with worse than this before my first coffee break most days!"
    mike.say "Wow!"
    mike.say "You're really getting the hang of this, Lavish!"
    mike.say "Are you sure you never played it before?"
    "Things just seem to get better for Lavish as time goes on."
    "And it should be pretty easy for me too."
    "As I've played this game a hell of a lot in the past."
    "But even so, I just can't seem to catch her up!"
    "soon enough the last of our credits has been spent."
    "And Lavish has racked up an epic score."
    lavish.say "I have to admit, [hero.name], that was pretty fun!"
    lavish.say "And it did kind of remind me of the real thing too."
    lavish.say "Especially the office pervert."
    lavish.say "Just like a guy I know!"
    mike.say "Really, Lavish?"
    mike.say "That's great - I'm so glad you had a good time."
    mike.say "And don't tell me who the pervert reminds you of either."
    mike.say "I want to guess for myself!"
    lavish.say "Okay, [hero.name], whatever you say..."
    return

label lavish_dick_reactions:
    if not lavish.flags.seendick:
        $ lavish.flags.seendick = 1
        if hero.has_skill("hung"):
            show dick reactions lavish smile
            lavish.say "You certainly are big down there!"
            mike.say "That's not a problem - is it?"
            lavish.say "Oh no...not at all."
            show dick reactions lavish tasty
            lavish.say "I just hope I can find room for it, that's all!"
            $ lavish.sub += 10
        elif hero.has_skill("smalldick"):
            show dick reactions lavish mock
            lavish.say "Is that as big as it's going to get?"
            mike.say "Uhm...yeah."
            mike.say "That's not a problem - is it?"
            show dick reactions lavish smile
            lavish.say "Oh no...not at all."
            lavish.say "There'll be plenty of room for it!"
            $ lavish.sub -= 10
        hide dick reactions
    return

label lavish_halloween_invitation:
    show lavish
    "Almost as soon as it's decided we're throwing a Halloween party, my mind is onto other things."
    "Specifically who I'm going to ask to come along as my date on the night."
    "And it doesn't take me long to decide that Lavish is the girl I want there with me."
    "So as soon as the chance comes around, I ask the question."
    mike.say "Hey, Lavish..."
    mike.say "I wondered if you were free on Halloween?"
    "Lavish looks at me with interest."
    "Her head cocked on one side as she does so."
    lavish.say "Oh..."
    lavish.say "Erm, no...I haven't made any solid plans yet."
    lavish.say "Why - do you have something in mind?"
    "You bet I do, Lavish!"
    "At least that's what I'm thinking as she poses the question."
    "Somehow I manage to keep my actual reply a little more restrained."
    mike.say "Well..."
    mike.say "My housemates and I are throwing a Halloween party."
    mike.say "It's not a massive thing, just a house-party, you know?"
    show lavish flirt
    "Lavish raises her eyebrows, evidently interested."
    lavish.say "And were you going to invite me?"
    mike.say "Y...yeah, Lavish!"
    mike.say "Of course I was!"
    mike.say "If you want to come, that is?"
    mike.say "Do you want to come?"
    "Lavish lets out a little giggle at my reaction."
    "Which only serves to make me that much more flustered."
    show lavish normal
    if lavish.love >= 100:
        "It's only then that I notice the smile on Lavish's face."
        "It's impish and more than a little mischievous."
        lavish.say "You already said it's a Halloween party."
        lavish.say "But is it a costume party too?"
        "I can't believe my luck."
        "I've been handed the perfect chance to swing this my way!"
        mike.say "Yeah, Lavish!"
        mike.say "Didn't I mention it before?"
        mike.say "No admittance on the night without a costume!"
        show lavish happy
        "I like the look on Lavish's face when she hears this."
        "It's almost like I can see her warming to the idea as I speak."
        "If only I'd started with the costume part."
        "This would have been so much easier!"
        lavish.say "Oh, that sounds like so much fun!"
        lavish.say "I hardly ever get the chance to dress up."
        show lavish flirt
        lavish.say "And I have just the costume in mind too."
        mike.say "So that's a yes?"
        mike.say "You'll come to the party?"
        $ lavish.love += 1
        show lavish normal
        "Lavish nods eagerly."
        "And I have to try hard not to punch the air in celebration."
        $ game.flags.halloween_girl = "lavish"
    else:
        "It's only then that I notice the smile on Lavish's face."
        "It's sad and very indulgent, which means I know what's coming next."
        lavish.say "I'm sorry, [hero.name]."
        lavish.say "But that doesn't sound like my kind of thing."
        "I start shaking my head even before Lavish is done talking."
        mike.say "How can it not be your kind of thing, Lavish?"
        mike.say "It's a party!"
        mike.say "Everyone likes a party, don't they?"
        "Lavish is still killing me with that smile."
        "It's so pleasant and reasonable."
        "And she looks so cute as she beams at me too!"
        lavish.say "Sure I like parties, [hero.name]."
        show lavish annoyed
        lavish.say "But all of your friends will be there."
        lavish.say "And I don't think I have too much in common with them."
        lavish.say "I'd just be in the way when you wanted to talk about that dungeon thing you play!"
        "Curse my geekiness!"
        "It's ruined my chances to bring a hot date to the party!"
        "But there's nothing I can do about it."
        "Not unless I want to look completely pathetic and desperate."
    return

label lavish_halloween_arrival:
    scene bg house
    "I open the door on autopilot, my mind still dwelling on the party."
    "Which means that I'm totally unprepared for what greets me once it's open."
    play sound woosh_punch
    "Quick as a flash, I see claws reaching out for me."
    with vpunch
    "And I take a jump back, trying to get out of their range."
    mike.say "Argh!"
    mike.say "What the hell?!?"
    show lavish halloween flirt with hpunch
    lavish.say "Meow..."
    lavish.say "Hiss!"
    "I manage to pull myself back together."
    "And that means I can finally make sense of what's going on."
    "The first thing I see is Lavish, standing on the doorstep."
    "But then I realise there's more too it than that - much more."
    "Because Lavish isn't normally dressed in tight, shiny latex!"
    mike.say "Y...you're..."
    mike.say "Felinelady..."
    mike.say "With the claws and the whip and the rubber..."
    show lavish normal
    "Lavish grins at this, clearly enjoying my reaction."
    lavish.say "What do you think, [hero.name]?"
    show lavish flirt
    lavish.say "Are you going to invite me in for a saucer of milk?"
    "She leans against the door frame, pretending to lick her hands."
    "Then she rubs them against her cheeks, like a cat would clean itself."
    menu:
        "Compliment":
            "Who cares if she made me jump when I opened the door?"
            "I'd have to be insane to hold a grudge about something so petty."
            "Especially when my date's all wrapped up in rubber like that!"
            mike.say "Wow, Lavish - pass the catnip!"
            mike.say "Seriously, you look amazing!"
            $ lavish.love += 1
            show lavish happy
            "Lavish gives me an approving smile."
            "And then she pushes herself forwards."
            "She rubs against me, pressing as close as possible."
            "The whole time she's purring like a cat too!"
            lavish.say "Purr...purr...purr..."
            lavish.say "That's earned you the chance to stroke me!"
            show lavish flirt
            lavish.say "If you want to stroke me, that is?"
            "I'm already flushing red."
            "And I can feel the effect Lavish is having on me in my shorts as well!"
            "I waste no time in hurrying her inside and closing the door behind us."
        "Criticize":
            "I want to gush over Lavish's costume."
            "Well, to be honest, I want to do far more than that!"
            "But the fact she almost pounced on me just now."
            "It's kind of taken the edge off of the surprise."
            mike.say "You really shouldn't jump out on a guy like that, Lavish."
            mike.say "That's a sure way for a cat to get declawed!"
            $ lavish.love -= 2
            show lavish annoyed
            "Lavish shakes her head and rolls her eyes."
            "And she lets out a groan."
            lavish.say "Urgh..."
            lavish.say "You sure know how bring a girl down, [hero.name]!"
            show lavish angry
            lavish.say "Do you know how hard it was to get into this thing?!?"
            "I hold my hands up in a gesture of surrender."
            "The last thing I want is Lavish to turn around and leave."
            mike.say "Okay, Lavish."
            mike.say "I'm sorry."
            mike.say "The costume is super hot."
            show lavish annoyed
            "Lavish looks at me sideways as she walks into the house."
            "And I know instantly that I'm not off the hook just yet."
    scene bg black with dissolve
    pause 1
    return

label lavish_halloween_party:
    $ game.pass_time(2)
    scene bg livingroom
    with fade
    sasha.say "Geez, that's one lame costume."
    sasha.say "Like zero imagination went into that one."
    show lavish halloween angry at left5
    show sasha halloween joke at right5
    with dissolve
    "I turn around just in time to see the expression on Lavish's face change."
    "Her smile turns into a frown as she looks at Sasha."
    lavish.say "I'm sorry?"
    lavish.say "What the hell is that supposed to mean?!?"
    "Sasha greets the question with a knowing smile."
    "And I can tell from her stance that she's spoiling for a fight!"
    sasha.say "Everyone knows that Felinelady's just boil-in-the-bag perversion!"
    sasha.say "The kind of thing boring people think is really naughty."
    lavish.say "So let me get this straight."
    lavish.say "You're saying I'm not a real pervert?"
    lavish.say "Which means that YOU are, yes?"
    show sasha angry
    "Oh dear - that escalated quickly!"
    "I need to step in before things get out of hand..."
    menu:
        "Defend Lavish":
            mike.say "You really have to make everything about sex, Sasha?"
            mike.say "Sounds like a shrink would have a field day on you!"
            $ sasha.love -= 2
            $ lavish.love += 2
            show lavish normal
            show sasha annoyed
            "Both of the girls turn to face me at once."
            "Lavish begins to look smug and confident as she realises what I'm saying."
            "But Sasha looks surprised and like she's getting more unsure."
            sasha.say "Ah..."
            sasha.say "You know what I mean, [hero.name]!"
            mike.say "No, I don't think I do, Sasha!"
            mike.say "Even Freud himself said 'sometimes a cigar is just a cigar'!"
            sasha.say "I...I have to go..."
            sasha.say "I need to check on the penis..."
            show sasha surprised
            sasha.say "I mean punch...I need to check on the punch!"
            hide sasha
            show lavish at center
            with easeoutright
            "Sasha hurries away, leaving Lavish and I me alone."
            lavish.say "Thanks for the save, [hero.name]."
            show lavish happy
            lavish.say "But I have to admit - I really do think this costume is naughty!"
            mike.say "Me too, Lavish, me too!"
        "Defend Sasha":
            mike.say "Come on, Lavish."
            mike.say "You have to admit that Sasha's got a point!"
            $ lavish.love -= 2
            $ sasha.love += 2
            show lavish annoyed
            show sasha normal
            "Both of the girls turn to face me at once."
            "Sasha looks smug and confident at my intervention."
            "But Lavish looks surprised and more than a little unsure."
            lavish.say "Wh...what do you mean, [hero.name]?"
            lavish.say "I thought you liked my costume?"
            mike.say "I do, Lavish, I do."
            mike.say "But you say bondage, and Felinelady IS what most people think of."
            mike.say "She kind of like the acceptable face of kinkiness in modern society!"
            show sasha happy
            "Sasha jumps on my words, eager to win the argument."
            sasha.say "That's it, [hero.name]!"
            sasha.say "You get it!"
            hide sasha
            show lavish at center
            with easeoutright
            "Sasha shoots Lavish a victorious look as she walks away."
            "For her part, Lavish seems to have gone quiet."
            "But I'm left wondering if I did the right thing just now..."
    scene bg black with dissolve
    pause 1
    return

label lavish_halloween_dance:
    $ game.pass_time(2)
    scene bg livingroom
    show lavish halloween
    with fade
    "Lavish and I have been making small-talk for a while now."
    "But I can't help glancing over to the makeshift dance-floor."
    lavish.say "Are you okay, [hero.name]?"
    lavish.say "You seem a little distracted!"
    mike.say "Huh?"
    mike.say "Oh...sorry, Lavish."
    mike.say "I was wondering if you wanted to dance?"
    "Lavish doesn't say yes right away."
    "But she doesn't say no either."
    lavish.say "I...I might!"
    menu:
        "Press on":
            "Lavish may not have said yes."
            "But she didn't say no either."
            "And that's good enough for me!"
            hide lavish
            show dance lavish halloween
            with fade
            "Grabbing her hand, I make for the dance-floor."
            "Lavish holds back for a second."
            "And then she gives in, following in my wake."
            "Once we're out there, she seems to relax."
            "Her demeanour changes subtly."
            $ lavish.love += 2
            $ lavish.sub += 1
            "And she lets me take charge."
            "What follows is a pretty slow, memorable dance."
            "We keep quiet the whole time."
            "And I savour the sensation of holding Lavish close."
            "Her body pressed against mine."
            "And I swear I her heart beating."
            "Even over the music."
            "It's like we're connecting on a whole new level."
        "Back down":
            "I nod and give Lavish a shrug."
            "If she wanted to dance, she would have said so."
            "I don't want to make her something she's not into."
            "So I just let the matter drop."
            mike.say "We don't have to dance if you don't want to, Lavish."
            mike.say "I'm fine with that."
            $ lavish.sub -= 2
            show lavish annoyed
            "Lavish narrows her eyes at this."
            "And for a moment I think she's going to tell me I got it wrong."
            show lavish normal
            "But then she just smiles and shakes her head."
            lavish.say "Okay, [hero.name]."
            "And she seems to be happy to let it drop too."
    scene bg black with dissolve
    pause 1
    return

label lavish_halloween_sex:
    scene bg livingroom
    show lavish halloween flirt
    with fade
    "Lavish's been playing up the sexiness of her costume all night."
    "Purring and stretching herself out like a cat whenever the opportunity arises."
    "And I've been having the time of my life playing along with her too!"
    "I mean, who wouldn't?"
    "But as the night draws on, Lavish starts to succumb to the effects of the punch."
    "And this means that her performance takes on a distinctly adult tone."
    "She's not so much acting like a flirty version of Felinelady anymore."
    "It's more like she's quickly turning into an actual cat on heat!"
    "Which is why I hustle her off to my bedroom the first chance I get."
    scene bg bedroom1
    show lavish halloween flirt
    with fade
    "Lavish doesn't seem to object to this in the slightest."
    "Instead she saunters into the room as I close the door behind us."
    lavish.say "Mmm..."
    lavish.say "Alone at last!"
    "I turn around just in time to see Lavish walk over to the side of the bed."
    "But then walk is hardly the right word to describe her motion right now."
    "She somehow manages to make every movement overtly sensual and sexual."
    "I stare at the shape of her legs, the curves of her buttocks and the sway of her shoulders."
    "And she strokes the sides of her body with her hands too, smiling the whole time."
    lavish.say "I can't tell you how hard it's been tonight, [hero.name]."
    lavish.say "Having all those other people around us."
    lavish.say "And wanting you to touch me the whole time!"
    hide lavish
    "As if to emphasize her point, Lavish sinks down onto her knees."
    show lavish doggy halloween with fade
    "She rests her elbows on the bed and props her head up on her hands."
    lavish.say "It was all I could do to keep my hands off of myself."
    lavish.say "So many times I wanted to stroke my pussy."
    lavish.say "Or pinch my nipples - they were so hard!"
    "I can hear my own breathing now, heavy and ragged."
    "But all I can see is Lavish's hand between her thighs."
    lavish.say "I'm so hot and wet down there, [hero.name]!"
    lavish.say "Can you help me out?"
    "I must have stripped my clothes off without a conscious thought."
    show lavish doggy mike lust
    "Because a moment later I find myself almost pouncing on Lavish."
    "And I'm completely naked too!"
    "She feels warm through the rubber of her costume."
    "And that same material makes her so tactile that I can't help myself."
    show lavish doggy torn
    lavish.say "Oh, [hero.name]!"
    show lavish doggy happy
    lavish.say "That's right...that's what I want!"
    "I don't know if I manage to find an opening in Lavish's costume."
    "Or else I might simply have torn a hole to get to my prize."
    "Either way I catch a glimpse of the delicate folds between her thighs."
    "I swear that I can feel the heat radiating from Lavish's pussy."
    "That and the scent of her makes it seem like she really is in heat!"
    "But then I'm not thinking clearly or rationally either."
    "And so I simply aim my already stiff cock at its target."
    "At first there's a delightful moment of resistance."
    "And the moan that Lavish lets out makes it all the more enjoyable."
    show lavish doggy vaginal pleasure
    "Then she surrenders, and I sink slowly into her."
    "I keep it steady at first, filling her as much as I can."
    "But the sounds that Lavish makes are too compelling to hold back."
    "She groans and pouts, at times sounding like a purring cat."
    "And she feels to good around my cock that I can't help myself."
    "Before I know it I'm practically hammering away at Lavish."
    "And every thrust that I make feels so much better than the last."
    "I'm worried that she'll complain or tell me to lighten up."
    "But instead she seems to rise to the occasion."
    "The harder that I fuck her, the more Lavish nods and moans."
    "Like an alley cat, she noise she makes gets ever louder too!"
    "Soon it begins to feel like I'm having to hold Lavish down."
    "She wriggles and squirms on the end of my cock."
    "And she's moving with the same intensity as I am."
    "I don't know how much stamina I have left right now."
    "But I do know that I can't keep getting worked both ways like this!"
    "And in the blink of an eye, the inevitable happens."
    show lavish doggy ahegao creampie with hpunch
    "I cum all at once, thrusting myself as deep into Lavish as I can go."
    with hpunch
    "She takes all of it without breaking her stride."
    with hpunch
    "But she almost yowls as I fill her."
    "And then Lavish subsides into satisfied purrs."
    "Her pussy still quivering as my cum starts to seep out around my cock."
    $ lavish.sexperience += 1
    $ game.pass_time(1)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
