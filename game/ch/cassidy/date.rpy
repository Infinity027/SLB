label cassidy_date_intro_valentine_male:
    cassidy.say "Hey there, [hero.name]..."
    cassidy.say "Are you ready to be my valentine?"
    "I swallow nervously as I nod my head."
    "And can you blame me - Cassidy looks stunning!"
    mike.say "Oh yeah, Cassidy!"
    mike.say "I'm ready for this!"
    "Cassidy smiles and gives me a nod of approval."
    "And just like that, we're off on our date."
    return

label cassidy_date_intro_halloween_male:
    mike.say "Hey, Cassidy - looking extra spooky tonight!"
    mike.say "I like it!"
    "Cassidy frowns at this, wrinkling her nose a little."
    cassidy.say "Wh...what do you mean, [hero.name]?"
    cassidy.say "I'm not spooky - goths are spooky!"
    mike.say "Erm...it's Halloween, Cassidy - I was just paying you a compliment!"
    "Cassidy's face lights up as she finally understands my meaning."
    cassidy.say "Oh...that's okay then!"
    cassidy.say "So long as spooky on Halloween is the same as cute the rest of the year."
    return

label cassidy_date_intro_christmas_male:
    mike.say "Merry Christmas, Cassidy!"
    mike.say "Ready for our date?"
    "Cassidy's positively beaming as she nods her head."
    cassidy.say "You bet I am, [hero.name]."
    cassidy.say "I love this time of year - it's just so magical!"
    cassidy.say "Mommy and daddy always made it special for me."
    cassidy.say "And now you're making it extra special too!"
    return

label cassidy_date_intro_birthday_male:
    mike.say "Happy birthday, Cassidy!"
    mike.say "I hope you're ready for some fun."
    mike.say "Because I'm going to make this date super-fun!"
    cassidy.say "Thanks, [hero.name] - I'm sure it'll be great."
    cassidy.say "Maybe not as lavish as the parties Daddy throws for me."
    cassidy.say "But with your touch, it's sure to be sweet all the same..."
    return

label cassidy_date_intro_mc_birthday_male:
    mike.say "Hey, Cassidy..."
    mike.say "Are you ready for our date?"
    cassidy.say "Wait a minute, [hero.name]..."
    cassidy.say "Isn't today your birthday?"
    mike.say "Erm...yeah, it is."
    cassidy.say "So why didn't you tell me?"
    mike.say "I dunno, Cassidy - I guess it's not a big deal to me."
    cassidy.say "WHAT?!?"
    cassidy.say "Birthdays are too a big deal!"
    cassidy.say "I'd be SO mad if someone forgot mine!"
    return

label cassidy_date_eat_a_burger:
    "From the moment that her burger shows up, Cassidy turns up her nose."
    "She looks positively disgusted at the prospect of touching it, let alone putting it in her mouth."
    "In the end, I'm not sure if she actually eats a single bite of it."
    return

label cassidy_date_buy_drink:
    if cassidy.is_visibly_pregnant:
        show cassidy angry
        $ cassidy.love -= 10
        cassidy.say "[hero.name], you...you beast!"
        cassidy.say "First you get me pregnant."
        cassidy.say "And then you put our child in danger by offering me alcohol!"
        $ hero.cancel_activity()
        hide cassidy
    else:
        "When her drink arrives, Cassidy plucks it up almost without acknowledging where it came from."
        "She holds it in her hand and takes the occasional sip, almost like it's an accessory."
        "Part of me wonders if she knows what she's actually drinking at all."
    return

label cassidy_date_play_darts:
    "Cassidy moans and groans at the prospect of playing darts."
    "So much so that I honestly think she's going to toss the darts over her shoulder in a huff."
    "Even though she doesn't, none of her throws actually hit the board."
    return

label cassidy_date_pub_play_pool:
    "Sulking as she stands by the pool-table, Cassidy seems to resent being asked to play a game with me."
    "In the end, she fouls the ball so many times and comes so close to tearing the felt that I call an end to it."
    "Bad enough to play with her in that mood, let alone pay for the damage she causes as well."
    return

label cassidy_date_buy_a_round:
    if cassidy.is_visibly_pregnant:
        show cassidy angry
        $ cassidy.love -= 10
        cassidy.say "[hero.name], you...you beast!"
        cassidy.say "First you get me pregnant."
        cassidy.say "And then you put our child in danger by offering me alcohol!"
        $ hero.cancel_activity()
    elif (hero.charm >= 60 - cassidy.love and cassidy.flags.drinks < 2):
        show drink cassidy
        "Cassidy simply nods in a nonchalant fashion at me offering to buy a round."
        "She's so entitled that she seems to think it's just a given thing."
        "I seriously doubt she'll return the favour next time round."
        $ game.active_date.score += 5
        if "rebel" in cassidy.traits:
            $ game.active_date.score += 5
        $ cassidy.set_flag("drinks", 1, "day", mod="+")
        hide drink
    else:
        "I want to pay a round of beers to the whole pub."
        "But Cassidy doesn't seem to want to drink, so I refrain from doing so."
        $ hero.cancel_activity()
    return

label cassidy_dance_with:
    "Though she's pretty demure and chaste in the way that she moves her body, Cassidy's eyes tell a different story."
    "They almost burn with barely suppressed desire as we're on the dance-floor."
    "It's as if she knows something I don't, and is weighing up whether or not to enlighten me..."
    return

label cassidy_date_play_arcade_intro_male:
    cassidy.say "Eww!"
    cassidy.say "This place smells funky!"
    cassidy.say "And my feet are sticking to the carpet too!"
    "I turn around and try to keep from frowning at Cassidy."
    "It was a challenge to get her to come to the arcade in the first place."
    "But now that we're here, all she seems to want to do is complain!"
    mike.say "It's not about the interior decor, Cassidy."
    mike.say "It's about tuning into the games."
    mike.say "They're a gateway to another world."
    mike.say "A world of fantasy and adventure!"
    "Cassidy rolls her eyes at this."
    cassidy.say "Who wants to come to a stinky place like this?"
    cassidy.say "Especially when you can play better games on your phone!"
    "I look around desperately for something I can throw back at Cassidy."
    "And then my eyes settle on a row of classic games."
    mike.say "Not these, Cassidy."
    mike.say "These are vintage arcade titles."
    mike.say "Classics that never got ported to a phone or a console."
    cassidy.say "Really?"
    mike.say "Really."
    cassidy.say "So if I put up a selfie of myself playing them on social media..."
    mike.say "It'd be pretty unique, maybe even totally original."
    cassidy.say "Okay, [hero.name], okay."
    cassidy.say "Let's play...this one!"
    mike.say "Ooh, good choice - that's called 'Rampant'."
    mike.say "You play a huge monster that's wrecking the city!"
    cassidy.say "Well put the money in then, [hero.name]!"
    cassidy.say "I'll be the scaly, lizard thing."
    cassidy.say "And you can be the big, hairy ape!"
    return

label cassidy_date_play_arcade_win_male:
    "My dad had a retro console when I was a kid, with this as one of the games."
    "And I must have spent hours playing the shit out of that thing."
    "Which means that I'm an expert at this game."
    cassidy.say "Hey, no fair!"
    cassidy.say "I was going to smash that building, [hero.name]!"
    cassidy.say "And you've grabbed more damsels in distress than me too!"
    mike.say "You need to pay more attention to the game, Cassidy."
    mike.say "Complaining's not going to win you more points!"
    "Cassidy makes a huffing noise and we get on with the game."
    "But she doesn't seem to take my advice to heart."
    "I dominate the whole time we're playing."
    "And once we've run out of credits, I'm way ahead of her."
    cassidy.say "Urgh..."
    cassidy.say "I'm glad that's over!"
    cassidy.say "Now, about that selfie..."
    cassidy.say "I'll just say that your score's mine, okay?"
    mike.say "Whatever you want, Cassidy."
    mike.say "So long as you're happy."
    return

label cassidy_date_play_arcade_lose_male:
    "My dad had a retro console when I was a kid, with this as one of the games."
    "And as soon as we start playing, I wish I'd spent more time on it!"
    "Because my skills are as basic as Cassidy's - we're both rank amateurs."
    mike.say "H...hey, what happened there?"
    mike.say "Cassidy, I was going to smash that building!"
    mike.say "And I was going to grab that damsel in distress too!"
    cassidy.say "Ah, get over it, [hero.name]."
    cassidy.say "You had your chance."
    cassidy.say "You know what - this is a really fun game!"
    "I try not to sulk as Cassidy continues to dominate the game."
    "It's uncanny, like she has a natural talent for it or something."
    "No matter what I try, I just can't catch up to her."
    "And by the time we've run out of credits, she's way ahead of me!"
    mike.say "Urgh..."
    mike.say "Is it finally over?"
    cassidy.say "Stop moaning, [hero.name]."
    cassidy.say "Now, let's get that selfie..."
    mike.say "Ah, Cassidy..."
    mike.say "I don't suppose you'd pretend your score is mine?"
    return

label cassidy_dick_reactions:
    if not cassidy.flags.seendick:
        $ cassidy.flags.seendick = 1
        if hero.has_skill("hung"):
            show dick reactions cassidy tasty
            cassidy.say "That's a pretty impressive size!"
            mike.say "Ah...thanks for the compliment."
            show dick reactions cassidy smile
            cassidy.say "Don't mention it, [hero.name]."
            cassidy.say "Just get over here and give me some of that thing!"
            $ cassidy.sub += 10
        elif hero.has_skill("smalldick"):
            show dick reactions cassidy mock
            cassidy.say "Aw...I was expecting it to be bigger!"
            mike.say "Ah...sorry to disappoint you, Cassidy!"
            cassidy.say "Ah well..."
            show dick reactions cassidy smile
            cassidy.say "I guess I'll just have to make the best of it!"
            $ cassidy.sub -= 10
        hide dick reactions
    return

label cassidy_halloween_invitation:
    show cassidy
    "I know as soon as we decide to throw the Halloween party that I want to invite Cassidy."
    "In an ideal world, I'd just walk up to her and pop the question without even thinking."
    "But she's one of those girls that you just don't do that with."
    "And that's because she..."
    "Well, let's be honest - it's because she can be a little spoilt at times!"
    "Okay, okay...she can be VERY spoilt at times."
    "But I'm sure that if I approach this in just the right way, I can pull it off."
    "All I need to do is find the right angle and pitch it in just such a way..."
    mike.say "Hey, Cassidy..."
    mike.say "You wanna come to a Halloween party at my place?"
    "Arrgh!"
    "What in the hell did I just do?!?"
    "The words came out of my mouth before I had time to think!"
    "And I can see the immediate effect they have on Cassidy in real time."
    cassidy.say "What was that, [hero.name]?"
    cassidy.say "Did you really just invite me to a Halloween party?"
    cassidy.say "One that's happening at that dump you live in too?"
    "Every word makes me want to wince out loud."
    "They hit me like blows to the stomach landed by a professional boxer."
    "I've only spoken two lines, and already Cassidy's got me on the ropes!"
    mike.say "Ah...ha ha!"
    mike.say "Yeah, you got me bang to rights!"
    mike.say "But it's so lame that it has to be cool, right?"
    mike.say "Kind of in an ironic way?"
    "Cassidy rolls her eyes at me and tuts in disapproval."
    if cassidy.love >= 100 or cassidy.is_sex_slave:
        cassidy.say "Wait a minute..."
        cassidy.say "Your housemates are all girls - aren't they?"
        mike.say "I...I guess so, Cassidy."
        "With that, Cassidy falls silent for a moment."
        "But I can see that her mind is racing the whole time."
        cassidy.say "And this party you're having..."
        cassidy.say "Is it a costume party too?"
        mike.say "Oh yeah, it is."
        mike.say "I meant to mention that!"
        show cassidy happy
        "A smile spreads slowly across Cassidy's face."
        "And I want to say that reassures me instantly."
        "But it's one of those smiles that makes me nervous."
        cassidy.say "Okay, [hero.name]."
        $ cassidy.sub += 1
        cassidy.say "I'll come to your little party."
        show cassidy normal
        cassidy.say "And I'll wear something that'll blow you away."
        cassidy.say "Something that'll put your little housemates to shame too!"
        mike.say "Y...yeah, Cassidy."
        mike.say "That sounds great!"
        $ game.flags.halloween_girl = "cassidy"
    else:
        $ cassidy.sub -= 1
        show cassidy sad
        cassidy.say "Urgh..."
        cassidy.say "I'm going to pretend you didn't say that, [hero.name]!"
        show cassidy normal
        cassidy.say "And then we can rewind this conversation, okay?"
        "I nod gingerly, feeling like I've been trodden on."
        mike.say "Ah..."
        mike.say "Okay, Cassidy."
        mike.say "Erm...thanks...I guess?"
        "Cassidy just makes another tutting sound."
        "And then she shakes her head."
        "Which seems to mean that we've officially moved on."
        cassidy.say "You have my permission to try again, [hero.name]."
        cassidy.say "So you might want to try harder next time."
        show cassidy happy
        cassidy.say "Otherwise you'll be spending Halloween without me."
        cassidy.say "Which is worse than spending it alone!"
    return

label cassidy_halloween_arrival:
    scene bg house
    "My head's still spinning from the demands of hosting the party."
    "Which means that I'm not fully tuned into what I'm doing as I open the door."
    show cassidy halloween
    "But what greets me on the other side is enough to stop me in my tracks."
    "And all I can do is stand there, eyes wide and mouth hanging open."
    cassidy.say "Hi, [hero.name]."
    cassidy.say "Aren't you a little short to be my date?"
    "Suddenly every embarrassing moment of my formative years comes surging back."
    "The same image burned into the mind of every guy that watched Return of the Jeudi."
    "The metal bikini."
    "The huge expanses of naked skin."
    mike.say "Princess..."
    mike.say "Leila..."
    "Cassidy lets out a giggle as she turns on the spot."
    "It's like she's reached into my soul and seized my inner geek."
    show cassidy happy
    cassidy.say "Yeah, that's right."
    cassidy.say "I kinda figured you'd be into it!"
    show cassidy normal
    cassidy.say "Well - are you going to let me in anytime soon?"
    cassidy.say "This costume isn't exactly the warmest thing to be wearing!"
    menu:
        "Step aside":
            "All of a sudden my mental block is broken."
            "I step aside and motion for Cassidy to come inside."
            mike.say "Sure, Cassidy, sure."
            mike.say "Come in before you freeze to death!"
            "Cassidy smiles as I make my show of deference."
            "Then she strides into the house like a true princess."
            "The whole time she's clearly enjoying my reaction to her costume."
            "And I'm powerless to resist, following in her wake."
            $ cassidy.love += 1
            $ cassidy.sub += 1
            cassidy.say "Ooh, the way you're looking at me!"
            cassidy.say "It reminds me of the movie, you know?"
            mike.say "What..."
            mike.say "Like I remind you of Han Alone coming to the rescue?"
            cassidy.say "Nah, I wasn't thinking of that guy."
            cassidy.say "More like the big slug thing licking his lips!"
            mike.say "Hey!"
            mike.say "I resent being compared to Djoba the Hung!"
        "Slap ass":
            "I manage to regain control of myself."
            "And I motion for Cassidy to step inside."
            "But there's just something about the way she moves."
            "The way that costume accentuates her body..."
            "I just can't help myself."
            $ cassidy.love -= 2
            $ cassidy.sub += 2
            "My hand slaps her ass as she passes me in the doorway."
            "And the sound is almost like the cracking of a whip."
            cassidy.say "Ouch!"
            cassidy.say "HEY!"
            cassidy.say "You can't do that to me - I'm a princess!"
            "I shake my head and let out a chuckle."
            "Cassidy looks really cute when she's angry!"
            mike.say "Yeah, but you've got to be faithful to the movie, Cassidy."
            mike.say "And Leila was a captive of Djoba the Hung when she wore that costume."
            mike.say "Which means that I get to treat you like my prisoner tonight."
            "Cassidy curls her lip at me."
            show cassidy normal
            "But then she raises one eyebrow as a thought occurs to her."
            cassidy.say "So that'd make you Djoba, right?"
            mike.say "Hey!"
            mike.say "I resent being compared to Djoba the Hung!"
    scene bg black with dissolve
    pause 1
    return

label cassidy_halloween_party:
    $ game.pass_time(2)
    scene bg livingroom
    with fade
    jack.say "Princess...Leila..."
    scottie.say "Metal...bikini..."
    cassidy.say "Argh!"
    cassidy.say "ZOMBIES!"
    cassidy.say "Save me, [hero.name]!"
    "I turn around to see what's gotten Cassidy so worked up."
    show cassidy halloween sad
    show scottie halloween perv at left
    show jack halloween perv at right
    with fade
    "And that's when I see Jack and Scottie shuffling towards her."
    "Their mouths hang open and their eyes are glazed over."
    "Both of them moan as they reach out in her general direction."
    "Cassidy darts behind me as they get closer."
    "Then she peeks over my shoulder, her face a picture of fear."
    cassidy.say "Don't let them get me."
    cassidy.say "Don't let them eat my brains!"
    "Of course, they're not really zombies."
    "The pair of them are just under the spell of Cassidy's costume!"
    menu:
        "Defend Cassidy":
            mike.say "Stand back, Cassidy."
            mike.say "I'll handle these mindless fiends!"
            hide cassidy
            "I step forwards and snap my fingers in front of their faces."
            show jack halloween normal
            show scottie normal
            "First Jack and then Scottie responds to the gesture."
            "They shake off the stupor they were in and look around in confusion."
            jack.say "Hey - where'd the princess go?"
            show scottie angry
            scottie.say "Yeah, where are the titties?!?"
            mike.say "I think I'm looking at the biggest pair of tits here tonight!"
            mike.say "Can't you two keep your adolescent fantasies under control?"
            jack.say "Ah...sorry, man."
            show scottie sad
            scottie.say "Our bad, dude."
            hide scottie
            hide jack
            "Jack and Scottie slope off, muttering their disappointment."
            $ cassidy.love += 2
            show cassidy halloween happy
            "But Cassidy emerges from behind me, looking pleased with my actions."
            cassidy.say "You really showed them, [hero.name]!"
            cassidy.say "You can be my Jeudi Knight in shining armour as a reward."
        "Defend Jack and Scottie":
            mike.say "Don't be silly, Cassidy."
            mike.say "Those guys aren't real zombies."
            mike.say "Their brains are just scrambled from ogling you in that costume!"
            hide cassidy
            "I step forwards and snap my fingers in front of their faces."
            show jack halloween normal
            show scottie normal
            "First Jack and then Scottie responds to the gesture."
            "They shake off the stupor they were in and look around in confusion."
            jack.say "Hey - where'd the princess go?"
            show scottie angry
            scottie.say "Yeah, where are the titties?!?"
            mike.say "You guys need to back off, okay?"
            mike.say "Cassidy's my date tonight."
            hide jack
            hide scottie
            "Jack and Scottie slope off, muttering their disappointment."
            $ cassidy.love -= 2
            show cassidy halloween angry
            "But Cassidy doesn't seem to happy with the way I handled things either."
    scene bg black with dissolve
    pause 1
    return

label cassidy_halloween_dance:
    $ game.pass_time(2)
    scene bg livingroom
    show bree halloween
    with fade
    bree.say "Hey, [hero.name]."
    bree.say "I know you love this song."
    show bree happy
    bree.say "Come dance with me!"
    "I look around and see [bree.name], calling me from the dance-floor."
    "The song that's playing is from a game we both really like."
    "I'd normally jump at the chance to dance with [bree.name]."
    "But Cassidy just slipped away to use the bathroom."
    "And I don't think she'd be happy to find me dancing with another girl."
    menu:
        "Refuse":
            mike.say "I'd love to, bree."
            mike.say "But I'm waiting for Cassidy."
            show bree annoyed
            "[bree.name] puts on an exaggerated pout at being turned down."
            show bree normal
            "But she shrugs, letting me know there are no hard feelings."
            bree.say "Your loss!"
            hide bree with dissolve
            "And with that, she turns away to dance alone."
            show cassidy halloween angry with fade
            "A moment later, Cassidy appears at my side."
            cassidy.say "What's up with Blondie, huh?"
            cassidy.say "Was she hitting on my date?"
            mike.say "No way, Cassidy!"
            mike.say "[bree.name] just wanted to ask me to dance."
            cassidy.say "Oh, did she now!"
            mike.say "Don't worry, I told her I was waiting for you."
            $ cassidy.love += 2
            show cassidy normal
            "At this, Cassidy nods and makes triumphant sound."
            cassidy.say "That deserves a reward."
            hide cassidy
            show dance cassidy halloween
            with fade
            "Cassidy drags me onto the dance-floor."
            "And then she sticks to me like glue."
            "The whole time she's staring at [bree.name]."
            "Like she's marking me out as belonging to her."
            "You might think that sounds weird."
            "But for me it's kind of sexy."
            "Like she wants me so badly!"
        "Accept":
            mike.say "Sure thing, [bree.name]."
            mike.say "Cassidy can join us when she's back too."
            $ bree.love += 2
            hide bree
            show dance bree halloween
            with fade
            "I hurry onto the dance-floor to join [bree.name]."
            "And I forget myself for the duration of the song."
            "Nothing scandalous happens."
            "We're just a couple of friends dancing together."
            "But once the song ends, I see Cassidy staring at me."
            "And she looks pissed!"
            hide dance
            show cassidy halloween angry
            with fade
            "I hurry over to Cassidy."
            mike.say "Cassidy - there you are!"
            mike.say "Why didn't you come and join us?"
            cassidy.say "You looked like you were doing okay without me!"
            mike.say "Don't be like that, Cassidy."
            mike.say "[bree.name]'s just my friend, that's all."
            cassidy.say "Yeah, [hero.name]?"
            $ cassidy.love -= 2
            cassidy.say "Well that's not what it looked like!"
            "I try to ignore what Cassidy just said."
            "She's overreacting, nothing more."
            "So I change the subject and put it out of my mind."
    scene bg black with dissolve
    pause 1
    return

label cassidy_halloween_sex:
    scene bg bedroom1
    show cassidy halloween
    with fade
    "I know that you sit down to watch a movie in order to escape from reality."
    "But sometimes, on a rare occasion, reality is better than fiction could ever be."
    "And right now, as I follow Cassidy into my bedroom, is one of those times."
    "Sure, that was one great movie, one of the best ever made."
    "But nobody got to enjoy some intimate time with Leila while she was in THAT outfit."
    "And Cassidy wears it like the princess she thinks of herself as too!"
    cassidy.say "Mmm..."
    cassidy.say "I've been so cold in this get-up all night."
    cassidy.say "The only thing keeping me warm is how hot it's made you!"
    cassidy.say "Isn't that right, [hero.name]?"
    "I swallow audibly and nod in agreement."
    "There's no way I can hide how I'm feeling right now."
    "Cassidy looks so hot in that costume it's impossible to deny."
    mike.say "Y...yeah, Cassidy."
    mike.say "I was going to say something clever."
    mike.say "Like a line from Han Alone, you know?"
    mike.say "But you're making my brain overload!"
    show cassidy happy
    "Cassidy gives me a satisfied smile and a seductive chuckle."
    "I can see that she's getting off on how entranced I am."
    cassidy.say "Aww..."
    cassidy.say "It's sweet that you're so honest, [hero.name]."
    show cassidy normal
    cassidy.say "And it also means that you deserve a reward too..."
    "With that, Cassidy turns her back on me."
    "She begins to walk towards the bed."
    "But the word walk doesn't do justice to the way she moves."
    "Cassidy sashays over to the bed, hips moving in a hypnotic manner."



    "The flimsy skirts hanging from her waist part to reveal her naked ass."
    "And I see that she must have slipped her panties off too!"
    "Cassidy looks back over her shoulder at me."
    cassidy.say "Well?"
    cassidy.say "What are you waiting for?"
    cassidy.say "Get over here, you scruffy-looking Nerf Herder!"
    "I don't need to be called that twice!"
    "And so I hurry to tear off my clothes and make it to the bed."
    show cassidy doggy halloween with fade
    "I all but pounce on Cassidy as I leap onto the mattress."
    "My cock's already good and hard from the mere sight of her."
    "But once I have my hand on her, there's no holding back."
    "If Cassidy had been hoping to give orders, she's out of luck."
    "As I waste no time in parting her buttocks with my hands."
    "She yelps in surprise, but I hardly hear the sound."
    "And that's because my eyes are fixated on the folds of her pussy."
    "Like me, Cassidy seems to already be pretty excited."
    "Her lips are glistening in the light, slick and supple."
    show cassidy doggy pleasure
    "And her yelps turn into hungry moans a moment later."
    "She does this as I rub the head of my cock along her pussy."
    show cassidy doggy normal
    "Cassidy looks back over her shoulder, nodding desperately."
    "I take this as my invitation, and push harder than before."
    show cassidy doggy vaginal
    "She parts slowly, letting me inch inside of her."
    "Every fraction of an inch feels better than the last."
    "Cassidy's tight, her muscles squeezing my cock."
    show cassidy doggy pleasure
    "My thrusts are sudden and powerful as a result."
    "She moans and pants with each one too, adding to the thrill."
    "But I still want to get deeper inside of her."
    show cassidy doggy blush
    "Without hesitating, I reach forwards."
    "And then I put my hands under Cassidy's chin."
    "This means that I can pull her back and onto be."
    show cassidy doggy ahegao
    "Cassidy bends like a bow, whimpering with pleasure."
    "I see her tongue begin to hang out of her mouth."
    "And I know that she's about to cum on the end of my cock."
    "The thought is more than enough to finish me off too."
    show cassidy doggy creampie
    "A moment later I lose it, as deep inside of Cassidy as I can go."
    "She cries out as I fill her, shuddering as her orgasm hits too."
    show cassidy doggy -creampie -vaginal pleasure
    "Afterwards, Cassidy slides off of my cock and onto the bed."
    show cassidy doggy cumshot with hpunch
    "As she does so, the last spurts of cum spurt out of me."
    show cassidy doggy -cumshot dickcum with hpunch
    "White spots rain down on her costume, soaking into the material."
    show cassidy doggy normal -blush
    "Cassidy looks around at me, a frown on her face."
    cassidy.say "Eww!"
    cassidy.say "Did you have to do that?!?"
    cassidy.say "Now I'll never get my deposit back on this thing!"
    $ cassidy.sexperience += 1
    $ game.pass_time(1)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
