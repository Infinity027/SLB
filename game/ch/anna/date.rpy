label anna_date_intro_valentine_male:
    anna.say "Hey there, valentine!"
    anna.say "Are you glad to see me?"
    "I can't help beaming as Anna bounces up to me."
    "She just looks so cute and full of life tonight."
    mike.say "You bet I am, Anna!"
    mike.say "And I'm SO glad you're my valentine!"
    anna.say "Me too!"
    anna.say "So what are we waiting for?"
    anna.say "Let's go have some fun!"
    return

label anna_date_intro_halloween_male:
    anna.say "Hey, [hero.name] - trick or treat?"
    "I turn to see Anna standing before me, beaming and waving."
    mike.say "Wow, Anna - you definitely look like a treat to me!"
    "Anna's smile only grows as I compliment her, and she blushes a little too."
    anna.say "Oh, stop it, [hero.name], you're embarrassing me!"
    anna.say "Actually...don't stop - I like it when you talk like that!"
    "Anna hurries over to where I'm standing and grabs my hand."
    "She squeezes it tightly and leans against me, nestling into my side."
    anna.say "Come on, we're supposed to be going on a date."
    anna.say "And I'm gonna make sure it's a treat for you!"
    return

label anna_date_intro_christmas_male:
    anna.say "Hey, [hero.name] - merry Christmas!"
    anna.say "What present did you get for me, huh?"
    "I smile and shake my head, unable to resist Anna's positivity."
    mike.say "You'll just have to wait and see, Anna."
    mike.say "Maybe that depends on how good you are while we're on our date!"
    "Anna giggles and takes hold of my hand."
    anna.say "Oh, don't worry, I'll be SO good you'll give me anything I want!"
    return

label anna_date_intro_birthday_male:
    mike.say "Happy birthday, Anna!"
    mike.say "And may I say, you're looking particularly hot tonight!"
    mike.say "You're making me feel like I'm the one getting the birthday treat here."
    anna.say "Aw, [hero.name]...stop it!"
    anna.say "Actually, no - don't stop it!"
    anna.say "You're getting me all hot and bothered already..."
    return

label anna_date_intro_mc_birthday_male:
    anna.say "Hey, [hero.name] - I'm over here!"
    anna.say "Happy birthday, to the best boyfriend in the world!"
    mike.say "Hey, Anna..."
    mike.say "You remembered my birthday?"
    mike.say "I'm impressed!"
    anna.say "I'm not a total scatter-brain, [hero.name]!"
    anna.say "And it's easy to remember things when it's all about you!"
    return

label anna_date_eat_a_burger:
    "As soon as Anna gets her hands on her burger, she begins to eat like she's starving."
    "It's amazing to see that she actually manages to smile broadly while cramming food into her mouth."
    "In fact, watching her is starting to make me feel hungry too..."
    return

label anna_date_buy_drink:
    if anna.is_visibly_pregnant:
        show anna angry
        $ anna.love -= 10
        anna.say "Seriously, [hero.name]?"
        anna.say "Did you forget that you got me pregnant?!?"
        anna.say "I can't drink while I'm like this!"
        $ hero.cancel_activity()
        hide anna
    else:
        "Petite as she is, there's nothing dainty about the way Anna knocks back her drink."
        "At times I even find it hard to keep up with her."
        "The glass in her hand seems to empty at an alarming rate!"
    return

label anna_date_play_darts:
    "Anna jumps at the chance to play, hurrying to the oche while clutching her darts."
    "She surprises me by being a pretty darn good player too."
    "I'd have to be lucky to pull off some of the shots she makes as well."
    return

label anna_date_pub_play_pool:
    "When I suggest a game of pool, Anna doesn't say no."
    "But I can see that she's less than enthusiastic."
    "This only makes sense when I see her struggling to make a shot."
    "Pool, it seems, is not the ideal game for someone of below average height."
    return

label anna_date_buy_a_round:
    if anna.is_visibly_pregnant:
        show anna angry
        $ anna.love -= 10
        anna.say "Seriously, [hero.name]?"
        anna.say "Did you forget that you got me pregnant?!?"
        anna.say "I can't drink while I'm like this!"
        $ hero.cancel_activity()
    elif (hero.charm >= 60 - anna.love and anna.flags.drinks < 2):
        show drink anna
        "Anna nods happily when I say that the next round is on me."
        "She thanks me, and then says that she'll get the next one herself."
        "Which means I'm on a date with a thoroughly modern girl."
        $ game.active_date.score += 5
        if "rebel" in anna.traits:
            $ game.active_date.score += 5
        $ anna.set_flag("drinks", 1, "day", mod="+")
        hide drink
    else:
        "I want to pay a round of beers to the whole pub."
        "But Anna doesn't seem to want to drink, so I refrain from doing so."
        $ hero.cancel_activity()
    return

label anna_dance_with:
    "Anna rushes onto the dance-floor like an eager puppy, pulling me after her."
    "Once there, she bounces eagerly through song after song."
    "I'm soon exhausted, but the pleasure I'm getting from being close to her is more than enough to keep me going."
    return

label anna_date_play_arcade_intro_male:
    anna.say "Ooh..."
    anna.say "Look at all the shiny things!"
    anna.say "And listen to the cool sounds too..."
    anna.say "This is going to be great, [hero.name]!"
    "I can't help smiling at Anna's enthusiasm at being asked to the arcade."
    "Unless you know they're a devoted gamer, it's always a gamble with a girl."
    "But so for, this seems to be going better than I could have hoped!"
    mike.say "Oh yeah, Anna."
    mike.say "I come here all the time."
    mike.say "It helps me to relax and unwind."
    "Even as I say this, I can see that's not what's happening with Anna."
    "Instead it seems like every new sight and sound makes her more excited."
    anna.say "Oh, that one looks like fun!"
    anna.say "No, this one's got cooler graphics!"
    anna.say "Wait...what's that over there?!?"
    mike.say "Ah, Anna..."
    mike.say "Maybe we should start with a classic?"
    mike.say "They have a really nice copy of \"Snackman\" over here..."
    "Anna's eyes light up and she giggles like a kid on a sugar rush."
    anna.say "Okay, [hero.name], that sounds great!"
    anna.say "Show me, show me!"
    "I hurry over to the arcade cabinet and begin pumping in the coins."
    "And all the while, Anna stands next to me, almost bouncing on the spot!"
    return

label anna_date_play_arcade_win_male:
    "Anna's not too shabby at the game, I have to admit."
    "But she's so excited that she's not really paying attention."
    "And so it doesn't take long for her to lose her lives."
    anna.say "Aww..."
    anna.say "That sucks, [hero.name]!"
    anna.say "The ghouls got me."
    anna.say "And I was just about to get the pow pill too!"
    mike.say "That's tough, Anna."
    mike.say "Let's see if I can do any better..."
    "I don't want to sound like I'm bigging myself up here."
    "But I soon manage to rack up a higher score than Anna."
    "And she watches in amazement as I leave her way behind."
    anna.say "Hey!"
    anna.say "What gives, [hero.name]?"
    anna.say "I think this game likes you better than me!"
    "Soon enough, all our coins have been spent."
    "And it looks like I'm the clear winner."
    mike.say "So, Anna..."
    mike.say "You had a good time?"
    anna.say "Yeah, I suppose so, [hero.name]."
    anna.say "But it'd have been better if I'd won!"
    return

label anna_date_play_arcade_lose_male:
    "I was expecting Anna's manic energy to get in the way."
    "That she wouldn't be able to pay attention to the game."
    "But the opposite seems to be true, as she plays like a demon!"
    anna.say "YES!"
    anna.say "Take that, you rotten ghouls!"
    anna.say "That pow pill is mine - and now you're gonna pay!"
    mike.say "Whoa..."
    mike.say "What's gotten into you, Anna?"
    mike.say "You're unstoppable!"
    "All I can do is stand there and watch."
    "Watch as Anna leaves me behind."
    "And when it's my turn, I can't hope to catch up."
    anna.say "Oh dear, [hero.name]..."
    anna.say "I think this game likes me better than you!"
    "Soon enough, all our coins have been spent."
    "And Anna's the clear winner."
    mike.say "So, Anna..."
    mike.say "You had a good time?"
    anna.say "I had a GREAT time, [hero.name]."
    anna.say "And don't feel down."
    anna.say "Because next time, I might let you win!"
    return

label anna_dick_reactions:
    if not anna.flags.seendick:
        $ anna.flags.seendick = 1
        if hero.has_skill("hung"):
            show dick reactions anna scared
            anna.say "WOW!"
            anna.say "That thing's SO big!"
            mike.say "Is...is that a problem?"
            show dick reactions smile
            anna.say "Oh no - don't worry about it."
            show dick reactions tasty
            anna.say "I'll find room for it somehow!"
            $ anna.sub += 10
        elif hero.has_skill("smalldick"):
            show dick reactions mock
            anna.say "Oooh!"
            mike.say "Is...is there a problem, Anna?"
            show dick reactions smile
            anna.say "No, no - it's all good."
            anna.say "It's what you do with it that counts!"
            $ anna.sub -= 10
        hide dick reactions
    return

label anna_halloween_invitation:
    show anna
    "Of course I want to ask Anna to come to the Halloween party."
    "Who else would I want to have there as my date?"
    "And so I take the first chance that presents itself to ask."
    "In fact, I'm so eager to ask that I just come out with it."
    "Which seems to catch Anna completely off guard."
    mike.say "Hey, Anna..."
    mike.say "We're having a Halloween party at my place this year."
    mike.say "And you should totally come along, yeah?"
    show anna surprised
    "Anna's eyes go wide at the mention of the party."
    "And she looks totally unprepared for the invitation."
    anna.say "A...a Halloween party?"
    anna.say "At your house?"
    mike.say "Yeah, Anna - that's what I said!"
    mike.say "You're going to come, right?"
    "Anna blinks, rather than offering me an answer."
    "And I'm starting to wonder what that answer will be."
    "Does she really not want to come to the party?"
    "I hadn't thought about what I'd do if that's the case."
    if anna.love >= 100 or anna.sub >= 40:
        $ anna.love += 1
        show anna normal
        anna.say "Ooh..."
        anna.say "That sounds great, [hero.name]."
        show anna wink
        anna.say "And I have just the costume in mind too!"
        "It takes a moment for it to sink in that Anna actually said yes."
        "But then I begin to nod my head with enthusiasm."
        mike.say "That's great, Anna!"
        mike.say "I'll let you know the time as soon as I can."
        mike.say "And I can't wait to see what costume you come up with too!"
        show anna annoyed
        "Anna holds up a hand to get my attention."
        "And I have to force myself to stop talking."
        "Which takes some serious effort."
        "As I was babbling thanks to my excitement."
        anna.say "But you have to promise me one thing, yeah?"
        mike.say "Anything, Anna."
        anna.say "You can't forget about me at the party."
        mike.say "Anna, I could never..."
        show anna angry
        anna.say "Of yes you could, [hero.name]!"
        anna.say "You don't know what it's like being short."
        anna.say "People forget you're even there!"
        show anna cry
        anna.say "And you and Sasha will be so busy with the party!"
        "Now it's my turn to hold up my hand."
        show anna surprised
        "And that stops Anna from babbling in turn."
        mike.say "I promise that won't happen, Anna."
        mike.say "You'll be the centre of my attention all night."
        show anna happy
        "Anna smiles at this."
        anna.say "I will when you see my costume!"
        $ game.flags.halloween_girl = "anna"
    else:
        show anna annoyed
        anna.say "Mmm..."
        anna.say "I don't know if I want to, [hero.name]!"
        "It takes me a moment to realise that Anna actually said no."
        "But then I shake my head in disbelief."
        mike.say "Y...you don't?"
        mike.say "But why, Anna?"
        mike.say "It's a costume party too."
        mike.say "I thought we could have some serious fun together!"
        "Anna looks uncomfortable as she tries to explain herself."
        "And she can hardly hold my eye for more than a second at a time."
        anna.say "It sounds like fun, [hero.name]."
        anna.say "But I won't know anyone there!"
        anna.say "You and Sasha will be busy all night."
        anna.say "And I'll just end up on my own in a corner!"
        "I shake my head, wanting to change Anna's mind."
        mike.say "Don't be silly, Anna!"
        mike.say "That's not going to happen."
        anna.say "Everyone says that, [hero.name]."
        anna.say "But it's different when you're short."
        anna.say "You get lost in the crowd."
        anna.say "People forget you're even there!"
        show anna normal
        anna.say "Can't we do something else - just you and me?"
        mike.say "I guess so, Anna."
        mike.say "Maybe the night after the party..."
        "I try to change the subject, finally accepting that as a no."
    return

label anna_halloween_arrival:
    scene bg house
    "I open the door while still more than a little distracted."
    "Which means I almost take a boot to the face a second later."
    "Jumping backwards, I barely avoid landing on my ass."
    anna.say "Hi-ya!"
    show anna halloween evil with dissolve
    anna.say "Ooh - nice reflexes, [hero.name]!"
    "Shaking myself back to awareness, I see Anna standing on the doorstep."
    "She's pulling a pose that looks like something out of a kung-fu movie."
    "And she has on a costume that's mostly black spandex."
    "Apart from her arms, which are supposed to look like metal."
    "She smiles eagerly at me as I try to put it all together."
    mike.say "A... A.I. Lita..."
    mike.say "Battle Angle A.I. Lita?"
    show anna happy
    "Anna's grin becomes wider still."
    "She claps her hands together in obvious delight."
    anna.say "That's right, [hero.name]!"
    anna.say "It's one of my favourite anime."
    show anna normal
    anna.say "You remember?"
    "Anna practically beams at me as she waits for an answer."
    "And I have to admit - she makes one hot cyborg!"
    menu:
        "Compliment":
            "Any thought of her almost kicking me in the face vanishes in an instant."
            "And instead all I can do is stare at Anna as she stands there in her costume."
            "My mind is too full of intriguing possibilities to think of anything else."
            mike.say "Wow, Anna...just, wow!"
            mike.say "It's my favourite anime too - as of right now!"
            $ anna.love += 1
            show anna blush
            "Anna blushes and bites her lips at the compliment."
            "She cocks her head on one side, regarding me shyly."
            anna.say "You...you really think so?"
            anna.say "I was worried my boobs would be too big!"
            "I shake my head, dismissing her concerns."
            mike.say "They're perfect, Anna."
            mike.say "I wouldn't change a thing."
            mike.say "Are...are you programmed for..."
            mike.say "Well, you know..."
            show anna evil
            "Anna's bashfulness vanishes in the blink of an eye."
            "Now she looks more like she's the one sizing me up!"
            anna.say "Oh, don't worry about that, [hero.name]."
            anna.say "I'm programmed in multiple techniques."
            show anna wink
            anna.say "And my cybernetic implants are top of the line too!"
        "Criticize":
            "But my pride is still more than a little hurt right now."
            "I mean, she nearly kicked me in the face!"
            mike.say "The costume's great, Anna."
            mike.say "But I don't appreciate the high kick."
            mike.say "You could have broken my damn nose!"
            $ anna.love -= 2
            show anna cry
            "Anna looks instantly crestfallen at my words."
            "She gazes down at her feet, wringing her hands together."
            anna.say "I...I'm sorry, [hero.name]."
            anna.say "I guess I didn't think."
            anna.say "I'm amazed I could kick so high!"
            "It's hard to stay mad at Anna."
            "Especially when she looks so sorry."
            mike.say "Apology accepted, Anna."
            mike.say "What do you say we try to forget about it?"
            mike.say "Come inside and let's have some fun."
            show anna normal
            "Anna's mood picks up instantly."
            "And she nods as she steps through the door."
            anna.say "Sure thing, [hero.name]."
            anna.say "Let's party!"
    scene bg black with dissolve
    pause 1
    return

label anna_halloween_party:
    $ game.pass_time(2)
    scene bg livingroom
    with fade
    jack.say "Ooh..."
    jack.say "As a serious Otaku, that's painful to see!"
    "I hear the sound of Jack's voice and the mention of anime terminology."
    "And it takes no more than a second for me to know who he's talking to."
    show anna halloween annoyed at right
    show jack halloween normal at left
    with dissolve
    "So it's no surprise when I turn around and see him looming over Anna."
    anna.say "Erm..."
    anna.say "What are you talking about?"
    anna.say "Don't you like my costume?"
    "Jack tuts and shakes his head."
    "And I know that Anna's in for a lecture."
    jack.say "Oh, don't get me wrong."
    jack.say "I like the IDEA of it."
    show jack halloween perv
    jack.say "But I can see so many places where you've got it wrong!"
    "Anna looks this way and that as Jack prepares to deliver his lecture."
    "Someone needs to step in here."
    "And that someone has to be me!"
    menu:
        "Defend Anna":
            mike.say "What's up, Jack?"
            mike.say "I don't see anything wrong with Anna's costume."
            show jack halloween normal
            "Jack takes a step back, amazement written all over his face."
            "It's like he can't understand the words coming out of my mouth."
            jack.say "But, but, but..."
            jack.say "It's not faithful to the original anime!"
            jack.say "It's more like the..."
            mike.say "Like the movie?"
            mike.say "Yeah, because that's what it's supposed to be, dummy!"
            show anna normal
            "Jack's mouth moves, but no words come out."
            mike.say "Anna and I watched that film together."
            mike.say "Didn't we, Anna?"
            show anna happy
            anna.say "Yeah, we did!"
            mike.say "And I remember loving it."
            $ anna.love += 2
            mike.say "So I love Anna's costume too!"
            jack.say "Arrgh!"
            jack.say "You've changed, man!"
            jack.say "But you won't infect me with your disease!"
            hide jack
            show anna at center
            "With that, Jack hurries off."
            "Which leaves me and Anna alone."
            "She hugs me tightly, letting me know I did the right thing."
        "Side with Jack":
            mike.say "I didn't want to be the one to say this, Anna."
            mike.say "But I know exactly what Jack means."
            show anna surprised
            "Anna's expression turns from hope to confusion."
            "She obviously thought I was stepping in to save her."
            "But when it comes to anime, being right is what really matters!"
            anna.say "W...what do you mean?"
            mike.say "Your costume, Anna."
            mike.say "It's based more on the movie than the anime."
            anna.say "Is that..."
            anna.say "Is that important?"
            show jack halloween normal
            "Jack brays with laughter and shakes his own head."
            "All I can do is roll my eyes in amazement."
            jack.say "Of course it is!"
            jack.say "Everyone knows the film's lame!"
            $ anna.love -= 2
            show anna cry
            anna.say "Oh...I see..."
            anna.say "I'm sorry, [hero.name]."
            anna.say "I had no idea..."
            "Sure, Anna looks a little upset right now."
            "But she's been put to rights."
            "And that's what really matters."
    scene bg black with dissolve
    pause 1
    return

label anna_halloween_dance:
    $ game.pass_time(2)
    scene bg livingroom
    show anna halloween happy
    with fade
    anna.say "Come on, [hero.name]..."
    anna.say "Let's dance!"
    "Before I know what's happening, Anna has a hold of my hand."
    "And she's tugging me onto the makeshift dance-floor."
    "I resist, more out of surprise than reluctance."
    mike.say "Whoa, Anna!"
    mike.say "What's the rush?"
    mike.say "You don't even like this song!"
    show anna blush
    "Anna's cheeks flush red."
    "And for a moment she won't meet my gaze."
    anna.say "Okay, I'll tell you why now."
    anna.say "But you can't laugh at me, yeah?"
    mike.say "I promise I won't laugh, Anna."
    "Anna lets out a sigh."
    anna.say "I...I want to dance now so Sasha can see us."
    anna.say "Because I want her to see me dancing with a hot guy!"
    menu:
        "Don't laugh":
            mike.say "Okay, Anna."
            show anna surprised
            mike.say "But I'm only doing it so Sasha can see me with a hot girl."
            "Anna looks puzzled for a moment."
            $ anna.love += 2
            show anna blush
            "But then realisation dawns on her."
            "And she blushes an even deeper shade of red."
            anna.say "Aww..."
            anna.say "You mean me!"
            show anna annoyed
            anna.say "Wait...you DO mean me, don't you?!?"
            mike.say "Yes, Anna - of course I mean you!"
            show anna happy
            "Anna giggles with delight and clings to my arm."
            hide anna
            show dance anna halloween
            "And with that, we hit the dance-floor together."
            "But if Sasha actually sees either of us, I have no way of knowing."
            "Because all I end up doing is gazing at Anna the whole time we're dancing."
        "Laugh anyway":
            "I know that I just made a promise."
            "But I can't keep from laughing out loud."
            mike.say "Oh, Anna..."
            mike.say "That's so funny!"
            show anna angry
            anna.say "Hey!"
            anna.say "No fair, [hero.name]!"
            anna.say "You promised you wouldn't laugh at me!"
            "I shake my head, trying to make an apology out of it."
            "But I still can't stop laughing."
            mike.say "Geez, Anna - what are you, like twelve years old?!?"
            $ anna.love -= 4
            hide anna
            "Anna storms off, all thought of our dancing together forgotten."
            "And I follow in her wake, trying to think of how I can make it up to her."
    scene bg black with dissolve
    pause 1
    return

label anna_halloween_sex:
    scene bg livingroom
    show anna halloween
    with fade
    "I haven't been able to tear my eyes away from Anna all night."
    "Every time I look in her direction, I can feel myself getting hard."
    "I always had a thing for A.I. Lita in the original anime back in the day."
    "And so seeing Anna dressed up as her now is almost too much."
    "I mean, Anna's hot anyway - but that costume just puts it over the top!"
    "Even better, I can tell that Anna's been enjoying having me watch her too."
    "All night I've been getting coy little smiles from her."
    "She's raised her eyebrows and blown me kisses too."
    "And more than once she's dropped something and bent to pick it up."
    "All the while making sure that I can see how her costume clings to her body!"
    scene bg bedroom1
    show anna halloween normal
    with fade
    "So by the time we finally make it to my bedroom, I'm a complete mess."
    show anna happy
    "Anna giggles as I close the door behind us."
    anna.say "Ooh..."
    anna.say "I've been waiting for this all night."
    show anna wink
    anna.say "Come on and catch me, [hero.name]!"
    hide anna
    "With that, she turns and skips over to my bed."
    "And then she clambers onto the mattress, still giggling away."
    mike.say "Hey!"
    mike.say "Where do you think you're going?"
    "Anna's giggles are replaced by a yelp of excitement as I run after her."
    "She back's away from me on her ass, pretending to be intent on escaping."
    show anna halloween blush
    "But her back hits the wall just as I make it to the edge of the bed."
    anna.say "Oh no!"
    anna.say "Looks like I can't get away!"
    "I've been stripping off my clothes as I crossed the room."
    show anna missionary halloween with fade
    "And by now I'm completely naked, climbing onto the bed."
    "Anna glances down at my cock and lets out another yelp."
    anna.say "Oh, [hero.name]!"
    anna.say "Even A.I. Lita can't defeat a weapon that mighty!"
    "I all but pounce on Anna a moment later."
    "I'm just that desperate to have her in my arms."
    "She allows herself to be caught, but makes a show of it."
    show anna missionary lookup
    "Anna wriggles in my grasp, pressing herself against me."
    "Which means I can feel the sensation of her spandex costume against my skin."
    "And even better, the warmth of Anna's own skin underneath it."
    "Neither of us is talking anymore."



    "Anna's breasts are suddenly in my face."
    "And I swear I can catch the scent of her pussy too!"
    show anna missionary lookdown
    "Anna grabs hold of my cock and thrusts it between her legs."
    "Of course, I have no choice but to follow."
    "She rubs it hard against the outer folds, gasping as she does so."
    anna.say "Mmm..."
    anna.say "I need this, [hero.name]..."
    anna.say "I need it inside of me now!"
    show anna missionary vaginal
    "With that, she pushes the head into the lips of her pussy."
    "All it takes from me is the slightest of pushes..."
    show anna missionary pleasure
    "And I hear Anna's gasp turn into a deep moan."
    "I use my arms to push her thighs wide apart."
    "Then I devote all of my efforts to giving her what she wants."
    "Not that it's a chore in any sense."
    "Sinking into Anna feels like heaven."
    "A feeling that I wish could go on forever."
    "And it's almost a shame to have to start moving again."
    show anna missionary lookup
    "But I have a job to do and a hot girl to please."
    "Anna nods desperately as I move in and out of her."
    "Eyes wide and mouth hanging open, she urges me on."
    "All of the remaining energy I have goes into it."
    show anna missionary ahegao
    "And then I add to that as much adrenaline as I can summon too."
    "It seems to pay off, as I see Anna's eyes begin to glaze over."
    "I know that I've done it for sure when they roll upwards too!"
    "She's still moaning as I use up all that I have in her."
    show anna missionary creampie with hpunch
    "And the sound becomes louder still when I shoot my load."
    with hpunch
    "Anna takes everything that I have left in one go."
    with hpunch
    "I keep on thrusting with all my remaining might as I fill her too."
    "Then she finally collapses onto the pillows."
    "There she writhes helplessly as she cums too."
    "But all I can do is watch in silent exhaustion."
    "My breath coming in ragged gasps as my heart hammers in my chest."
    $ anna.sexperience += 1
    $ game.pass_time(1)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
