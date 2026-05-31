
label cherie_date_eat_a_burger:
    "I'm kind of worried about how Cherie's going to react to the burger when it arrives."
    "I mean, she's such a refined and sophisticated woman - has she even eaten a burger before now?"
    if cherie.sub >= 66:
        cherie.say "Oh my goodness, it's so big!"
    else:
        cherie.say "Oh my goodness, this looks so wonderful!"
    "Before I can say a word, Cherie picks up her burger and begins to tuck into it."
    "And so it's with a genuine sense of relief that I feel myself relax and then do the same."
    return

label cherie_date_buy_drink:
    mike.say "Hey, Cherie..."
    mike.say "I'm going to grab another drink."
    mike.say "You want me to get one for you too?"
    if cherie.is_visibly_pregnant:
        "Cherie looks at me with a scandalised expression."
        if cherie.sub >= 66:
            "Cherie puts her hands on her belly, looking sad all of a sudden."
            cherie.say "I don't want to sound ungrateful, [hero.name]..."
            cherie.say "But aren't you forgetting something?"
        else:
            "And at the same time she places her hands on her belly in a defensive manner."
            cherie.say "[hero.name], you know that I'm pregnant!"
            cherie.say "How could you even suggest such a thing?!?"
        mike.say "Oh yeah...my bad!"
        $ hero.cancel_activity()
    else:
        "Cherie holds up her empty glass, shaking it so that the ice inside tinkles around."
        if cherie.sub >= 66:
            cherie.say "If you think I could handle another one, [hero.name]?"
            cherie.say "But only if you approve."
        else:
            cherie.say "Oh, how thoughtful of you!"
            cherie.say "I will have the same again, please."
            cherie.say "And don't be too shy with the measures either!"
        $ game.active_date.score += 5
        $ cherie.set_flag("drinks", 1, "day", mod="+")
    return

label cherie_date_play_darts:
    "Cherie looks at the darts when I hand them to her, almost like she doesn't know what to do with them."
    if cherie.sub >= 66:
        cherie.say "Oh my - I do not think that I can do this!"
    else:
        cherie.say "Oh my goodness - these look dangerous!"
    mike.say "Don't worry about it, Cherie, it's just an innocent game, yeah?"
    "Cherie nods as she turns to face the dartboard, preparing herself to play."
    "But despite her best efforts, Cherie misses the board more than she hits it."
    return

label cherie_date_pub_play_pool:
    "Cherie takes the pool-cue from me, weighing it in her hands."
    if cherie.sub >= 66:
        cherie.say "Are you sure that you want to play this game, [hero.name]?"
        cherie.say "I feel that you should know I am rather good at it."
    else:
        cherie.say "Hmm...not the best one I've ever used, but not the worst either."
        cherie.say "Very good, {i}mon ami{/i} - I will break."
    "I get the impression that this is not a question, but more a statement of fact."
    "So I nod my head and resign myself to what proves to be a tough game of pool."
    return

label cherie_date_buy_a_round:
    "Knocking back the last of my drink, I slam the empty glass down and stand up."
    mike.say "Okay, I think it's my round."
    mike.say "Are you up for one too, Cherie?"
    if cherie.is_visibly_pregnant:
        if cherie.sub >= 66:
            show cherie sad
            "Cherie puts her hands on her belly, looking sad all of a sudden."
            cherie.say "I don't want to sound ungrateful, [hero.name]..."
            cherie.say "But aren't you forgetting something?"
        else:
            "Cherie looks at me with a scandalised expression."
            "And at the same time she places her hands on her belly in a defensive manner."
            cherie.say "[hero.name], you know that I'm pregnant!"
            cherie.say "How could you even suggest such a thing?!?"
        mike.say "Oh yeah...my bad!"
        $ hero.cancel_activity()
    else:
        "Cherie holds up her empty glass, shaking it so that the ice inside tinkles around."
        if cherie.sub >= 66:
            cherie.say "If you think I could handle another one, [hero.name]?"
            cherie.say "But only if you approve."
        else:
            cherie.say "Oh, how thoughtful of you!"
            cherie.say "I will have the same again, please."
            cherie.say "And don't be too shy with the measures either!"
        $ game.active_date.score += 5
        $ cherie.set_flag("drinks", 1, "day", mod="+")
    return

label cherie_dance_with:
    mike.say "Come on, Cherie..."
    mike.say "Let's hit the dance-floor, yeah?"
    "I reach out my hand and Cherie takes hold of it without hesitation."
    "And within a mere matter of seconds we're on the dance-floor, moving in time to the music."
    "Cherie laughing as she presses her body close to mine, losing herself in the act of dancing."
    return

label cherie_date_play_arcade_intro:
    "I can see that there's a new arcade machine over in the corner."
    "And no matter how hard I try, the thing keeps calling out to me."
    "So in the end I feel like I have to do something about it."
    mike.say "You want to come play the new machine, Cherie?"
    mike.say "It looks like a really good one."
    "Cherie glances over at the machine, flashing away in the corner."
    "And I can see that she's not instantly sold on the idea."
    if cherie.sub >= 66:
        cherie.say "Oh, I am not very good at such things!"
        cherie.say "Maybe I could just watch you play instead?"
    else:
        cherie.say "Are you sure that's a good idea, [hero.name]?"
        cherie.say "I'm not so good at that kind of thing."
    mike.say "No need to worry, Cherie - I'll teach you how."
    return

label cherie_date_play_arcade_win:
    "Cherie seems to be humouring me, walking over to the machine so we can start playing."
    "I pump some coins into the slot, and the screen comes to life as the game begins."
    cherie.say "Oh dear..."
    cherie.say "I don't...I don't know what's happening!"
    mike.say "Don't worry, Cherie..."
    mike.say "Just do what I'm doing, okay?"
    "But no matter what I say, Cherie's performance doesn't improve."
    "And by the time the game is over, I'm the clear winner."
    cherie.say "Okay, can we do something else now?"
    mike.say "Erm...I guess so."
    return

label cherie_date_play_arcade_lose:
    "Cherie seems to be humouring me, walking over to the machine so we can start playing."
    "I pump some coins into the slot, and the screen comes to life as the game begins."
    cherie.say "Oh dear..."
    cherie.say "I don't...I don't know what's happening!"
    mike.say "Don't worry, Cherie..."
    mike.say "Just do what I'm doing, okay?"
    "My words seem to do the trick, as Cherie's performance seems to get steadily better."
    "Soon she's catching me up, and then pulling ahead, leaving me in her wake."
    "By the time the game is over, Cherie's the clear winner."
    cherie.say "This game is actually not bad - shall we play again?"
    mike.say "Erm...maybe we could do something else instead?"
    return

label cherie_dick_reactions:
    if not cherie.flags.seendick:
        $ cherie.flags.seendick = 1
        "I'm feeling nervous as I finally get to show Cherie what I have in my pants."
        "Laying it all out before her and waiting to see what she has to say."
        show cherie normal
        if hero.has_skill("hung"):
            show cherie surprised
            "Cherie's eyes bulge in their sockets as she stares at my manhood."
            show dick reactions cherie scared
            cherie.say "Oh my goodness!"
            mike.say "You...you don't like it, Cherie?"
            mike.say "You think it's too big?"
            "Cherie shakes her head as she keeps on staring at it."
            show dick reactions cherie smile
            if cherie.sub >= 66:
                cherie.say "Oh no, {i}mon ami{/i}- I am just amazed at the size of it."
                cherie.say "Please, promise to be gentle with me?"
            else:
                cherie.say "I did not say that it was too big, {i}mon ami{/i}..."
                cherie.say "I am just amazed by the size of it, of how it will feel inside of me!"
            $ cherie.sub += 10
        elif hero.has_skill("smalldick"):
            show dick reactions cherie mock
            "Cherie looks instantly disappointed, her expression downcast."
            if cherie.sub >= 66:
                cherie.say "Oh dear..."
                cherie.say "I mean...oh heavens!"
                mike.say "You...you mean it's too small?"
                show dick reactions cherie smile
                cherie.say "No, of course not!"
                show dick reactions cherie mock
                cherie.say "It is...a masterpiece in miniature, yes?"
            else:
                cherie.say "Oh..."
                cherie.say "Ah well, one cannot ask for everything."
                mike.say "You...you mean it's too small?"
                show dick reactions cherie smile
                cherie.say "Well, maybe smaller than I would have liked."
                cherie.say "But therein lies the challenge - prove to me that it doesn't matter, yes?"
                show dick reactions cherie mock
                cherie.say "Show me that it's how you use it that counts!"
            $ cherie.sub -= 10
        hide dick reactions
    return

label cherie_date_intro_valentine_male:
    mike.say "Happy Valentine's day, Cherie!"
    mike.say "And I'm so glad that you're my valentine."
    show cherie b stuned blush
    "Much to my surprise, Cherie blushes and looks away."
    "Not what I was expecting from a mature, dignified woman."
    mike.say "Cherie, are you okay?"
    show cherie b talkative
    cherie.say "Oh, I'm sorry, [hero.name]."
    show cherie b whining
    cherie.say "It's been so long since someone called me their valentine."
    show cherie a happy
    cherie.say "I think I'm going to have some real fun with you tonight!"
    show cherie a normal -blush
    return

label cherie_date_intro_halloween_male:
    mike.say "Hey, Cherie - you still up for our date tonight?"
    mike.say "Or would you rather forget about all that and go trick or treating instead?"
    show cherie a smile
    "Cherie chuckles at the suggestion, but waves it away all the same."
    show cherie a happy
    cherie.say "Oh, [hero.name], that's so funny!"
    cherie.say "Imagine, trick or treating at my age..."
    show cherie a amused
    mike.say "Well, Cherie, you're only as young as you feel."
    mike.say "And it might be fun..."
    show cherie a talkative
    cherie.say "Seriously though, let's drop the idea."
    show cherie a smile
    cherie.say "Unless you want to spend the evening trick or treating on your own..."
    show cherie a normal
    return

label cherie_date_intro_christmas_male:
    mike.say "Happy Christmas, Cherie."
    mike.say "And can I just say, you look amazing!"
    mike.say "I can't imagine a better gift than a date with you."
    show cherie b stuned blush
    "Cherie blushes at my compliment, clearly enjoying being flattered."
    show cherie b surprised
    cherie.say "Oh, [hero.name], you're so charming!"
    show cherie b happy
    cherie.say "It's so exciting to be the one getting spoilt at Christmas!"
    show cherie a normal -blush
    return

label cherie_date_intro_birthday_male:
    mike.say "Happy birthday, Cherie!"
    mike.say "I've got some serious fun planned for our date."
    mike.say "So I hope you'll enjoy it all."
    show cherie b happy blush
    cherie.say "Oh, [hero.name] - you're so thoughtful!"
    show cherie b talkative
    cherie.say "And so discreet too."
    show cherie b wink
    cherie.say "A less sensitive man might have mentioned my actual age..."
    show cherie a normal blush
    return

label cherie_date_intro_mc_birthday_male:
    show cherie a happy
    cherie.say "Happy birthday, [hero.name]!"
    cherie.say "Let's celebrate by having a great date, okay?"
    show cherie a normal
    mike.say "Oh...thanks, Cherie."
    mike.say "I'm really flattered that you remembered."
    show cherie a talkative
    cherie.say "Well, Dwayne was never one for keeping track of the finer details."
    cherie.say "So it kind of became a habit of mine to do all of that."
    show cherie a happy
    cherie.say "But enough about him - let's talk about us instead!"
    show cherie a normal
    return

label cherie_date_amusement_park_male:
    scene bg amusement
    show cherie
    with fade
    "I thought that bringing Cherie to the Amusement Park was a sure-fire win."
    "I mean, she's spent so much time being a wife and mother to Dwayne and Cassidy respectively."
    "And this is a chance for her to just forget all of that, kick back and have some fun."
    "Maybe even start a new chapter of her life with me, one that's all about the good times."
    "But as we're walking towards the entrance, she doesn't seem that excited by the prospect."
    "Don't get me wrong, she's not looking like she hates it."
    "Yet she's not exactly eager to get in there either."
    mike.say "Erm..."
    mike.say "Cherie..."
    mike.say "Are you okay right now?"
    show cherie stuned
    "Cherie looks at me in surprise."
    "Like the question totally caught her off-guard."
    show cherie surprised
    cherie.say "I'm fine, [hero.name]…"
    cherie.say "Why do you ask?"
    show cherie stuned
    mike.say "Well..."
    mike.say "This is an Amusement Park."
    mike.say "And they're supposed to be exciting..."
    show cherie normal
    "Cherie seems to catch my meaning before I can finish what I'm saying."
    show cherie happy
    cherie.say "Oh, I see!"
    cherie.say "I'm just not very into this kind of thing."
    cherie.say "It's more like I enjoy seeing them make other people happy."
    show cherie normal
    "I nod, pretending to accept Cherie's explanation at face value."
    "But the truth is that it's made me more determined than ever to ensure she enjoys herself."
    "Because that explanation sounded just like what I'd expect her to say to Dwayne or Cassidy."
    "And I'm determined for her relationship with me to be very different indeed."
    return

label cherie_date_ferris_wheel_male:
    "As soon as I see the Ferris Wheel, I know that we have to ride it."
    "It's a classic ride, and the perfect way to ease Cherie into things."
    "So I make sure to steer us towards it as the wheel looms above."
    cherie.say "So..."
    cherie.say "I'm guessing you want to go on the Ferris Wheel!"
    "There doesn't seem to be any point in denying it."
    "So I just shrug and steer Cherie towards the back of the queue."
    mike.say "Come on, Cherie..."
    mike.say "Everyone likes the Ferris Wheel, right?"
    "Cherie doesn't dignify that with an answer."
    "Instead she stands in line with me, waiting for our turn to come round."
    "And when it does, we step into one of the gondolas."
    "The safety bar comes down, making sure we stay in our seats."
    "And then the ride starts, raising us up into the air."
    "Cherie and I stay silent as we climb ever higher."
    "But I keep stealing a glance in her direction."
    "I'm waiting for the view from up here to have an effect on her."
    "Yet we make it all the way to the top of the wheel without any noticeable change."
    cherie.say "Are you planning on staring at me the whole time we're up here?"
    "I can't help jumping in my seat as Cherie notices me watching her."
    mike.say "Sorry, Cherie..."
    mike.say "I was just expecting you to enjoy the view or something."
    cherie.say "Ah..."
    cherie.say "It's okay, I guess."
    cherie.say "But I've seen better."
    cherie.say "To be honest, it's more than a little boring!"
    "I decide to leave it alone after that, keeping quiet for the rest of the ride."
    $ cherie.love -= 2
    $ game.active_date.score -= 20
    return

label cherie_date_merry_go_round_male:
    mike.say "Shall we ride the Merry-Go-Round, Cherie?"
    mike.say "That's even more of a classic than the Ferris Wheel!"
    "Cherie looks over at the ride in question."
    "Then she gives me a non-committal nod."
    cherie.say "If you like, [hero.name]."
    cherie.say "The queue does look shorter than most of the others."
    "Not exactly the level of enthusiasm I'd been hoping for."
    "But I'm not going to pass up on it all the same."
    "I lead Cherie over to where we can join the back of the queue."
    "And then we stand patiently in line until we get to the front."
    "Pretty soon we're sitting on the actual Merry-Go-Round."
    "And it begins to move, picking up speed as it goes."
    "Despite this being a pretty tame ride, I find myself enjoying it."
    "But when I glance around at Cherie, her face is kind of neutral."
    mike.say "What's the matter, Cherie?"
    mike.say "No fast enough for you?"
    "Cherie shrugs at this, giving me a little shake of the head."
    cherie.say "Well..."
    cherie.say "You get on and it goes round and round."
    cherie.say "That's really all there is to it."
    cherie.say "Not much to get excited about if you ask me."
    "I nod and turn my attention back to the ride."
    "But in my head I'm taking note of everything Cherie says."
    "So this one's too slow and sedate."
    "Point taken!"
    "I'll be sure to pick a more exciting ride next time."
    $ cherie.love -= 1
    $ game.active_date.score -= 10
    return

label cherie_date_haunted_house_male:
    "Seeing the Haunted House looming up ahead, I make straight for it."
    "It's one of my favourite attractions at the park, one I always try to do."
    "But as I push my way through the crowd, I feel Cherie holding back."
    mike.say "What's the problem, Cherie?"
    mike.say "I just want to do the Haunted House."
    mike.say "It's kind of a tradition for me!"
    "Cherie looks more than a little hesitant."
    "But then she seems to steel herself and conquer her misgivings."
    cherie.say "Okay, [hero.name]…"
    cherie.say "If it means that much to you, let's do it."
    cherie.say "But you have to promise to stick by me the whole time."
    cherie.say "Promise me?"
    "I nod, letting Cherie know that I'll do as she asks."
    "Then we join the queue and make our way into the Haunted House."
    "Almost as soon as we're in there, I discover Cherie wasn't pretending to be afraid."
    "The very first jump-scare makes her shriek out loud and scamper behind me."
    "But rather than being an annoyance, that actually makes things more enjoyable for me."
    "And that's because Cherie spends the entire time we're in there clinging to my side."
    "Every time she's scared, she yelps and presses herself into my chest."
    "And believe me when I say that she's scared almost all the time!"
    "Which means that I get to play the part of her protector the whole way round the place."
    "As well as feeling the pleasant sensation of her body close to mine."
    $ cherie.love += 2
    $ game.active_date.score += 20
    return

label cherie_date_love_boat_male:
    mike.say "Shall we take a ride on the Love Boat, Cherie?"
    mike.say "A nice, relaxing cruise on water might be just what we need."
    "Cherie smiles as I make the seemingly innocent suggestion."
    "And I know that she's not been fooled for an instant."
    cherie.say "Okay, [hero.name]…"
    cherie.say "But just you behave yourself."
    cherie.say "No turning into a randy octopus once we're on the water!"
    "I hold up my hands, trying to show that I understand."
    "But I still can't help feeling a little disappointed."
    "The idea of a few minutes in total privacy with Cherie will do that to a guy."
    "So I guess I'll just have to do all I can to restrain myself."
    "The queue for such a sedate ride is always one of the smaller ones."
    "And that means it doesn't take us long to make it to the front."
    "Soon enough we're hopping into our own boat."
    "Then we sail off into the darkness of the tunnel."
    "At first I feel a little hesitant to make my move."
    "But eventually I decide to throw caution to the wind."
    "I slide my arm around Cherie's shoulder."
    "And then I hold my breath, waiting to see what her reaction will be."
    "Much to my relief, I feel her lean into me."
    show cherie kiss with fade
    "And things progress naturally from there."
    "We kiss and cuddle the whole length of the ride."
    "But I keep my promise, and don't push my luck any further."
    "Though that doesn't mean I'm spared a painfully hard erection by the time it's over."
    $ cherie.love += 2
    $ game.active_date.score += 20
    return

label cherie_date_hedge_maze_male:
    mike.say "You want to try the Hedge Maze, Cherie?"
    cherie.say "A maze?"
    cherie.say "You're serious?"
    "I shrug, trying to ignore Cherie's lack of enthusiasm."
    mike.say "I don't know..."
    mike.say "It could be fun."
    "Now it's Cherie's turn to shrug."
    "But she adds a nod as well, letting me know she doesn't object."
    cherie.say "Let's give it a try."
    cherie.say "But if we get lost and have to be rescued..."
    cherie.say "Then I'm blaming you!"
    "Once we're inside the maze, it doesn't take long for me to begin enjoying myself."
    "There's just something compelling about a puzzle big enough for you to be inside of."
    "So I set off, leading us down the corridors of hedges and around one corner after another."
    "More than once I find myself standing still and wondering where the hell we should go."
    "Each time I catch Cherie looking my way, as if reminding me of her previous threat."
    "But luckily inspiration always seems to strike before it's too late."
    "And I manage to lead us back onto the right path."
    "Which eventually culminates in me leading us out of the exit and completing the maze."
    mike.say "There, Cherie..."
    mike.say "I did it!"
    cherie.say "Well done, [hero.name]…"
    cherie.say "Now don't ever ask me to do that again!"
    $ cherie.love -= 2
    $ game.active_date.score -= 20
    return

label cherie_date_amusement_ice_cream_male:
    cherie.say "Oh, look..."
    cherie.say "Don't those ice-creams look good, [hero.name]?"
    "I turn to look in the direction Cherie's pointing."
    "And the moment I do, I'm greeted with the sight of some pretty sweet looking ice-creams."
    "But I can also see that there are a lot of equally pretty girls licking at them too."
    "Which of course makes me take a look back at Cherie."
    mike.say "Oh..."
    mike.say "Oh yeah, Cherie..."
    mike.say "I can take a hint!"
    mike.say "Let me get you one of those bad boys..."
    "Cherie smiles happily as I hold out my arm for her to take."
    "And then we thread our way through the crowds towards the ice-cream stand."
    "Once we're there, we wait in line while Cherie studies the menu."
    cherie.say "Ooh..."
    cherie.say "I think I would like one of those, [hero.name]..."
    cherie.say "And maybe with a cherry on top?"
    "Cherie somehow manages to say all of that in a really suggestive manner."
    "Or at least in a way that my brain instantly decides to take in that way."
    "And I happily hand over the money, taking the ice-cream as soon as it's ready."
    "Then I hand it to Cherie and watch with anticipation as she takes her first lick."
    cherie.say "Mmm..."
    cherie.say "That is really nice, [hero.name]..."
    cherie.say "So tasty and so sweet!"
    mike.say "I know you are..."
    mike.say "I...I mean..."
    mike.say "I mean I know IT is!"
    $ cherie.love += 2
    $ game.active_date.score += 20
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
