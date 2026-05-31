label minami_date_intro_valentine_male:
    minami.say "Hey, big bro..."
    minami.say "Is my valentine ready for our big date?"
    "I nod, unable to tear my eyes away from Minami."
    "She just looks so hot, I can't believe it."
    mike.say "Oh yeah, Minami!"
    mike.say "I've never been more ready for anything!"
    show minami happy
    "Minami giggles and claps her hands together in delight."
    return

label minami_date_intro_halloween_male:
    mike.say "Hey, Minami - why no costume this year?"
    mike.say "Haven't you got a bedroom full of them?"
    "Minami wrinkles her face, looking confused."
    minami.say "Why would I need a costume, big bro?"
    minami.say "We're going on a date!"
    mike.say "Well...it is Halloween."
    show minami surprised
    minami.say "It is?!?"
    show minami sad
    minami.say "Oh...I've been studying so hard that I totally forgot!"
    mike.say "No worries, Minami."
    show minami normal
    mike.say "We can still have a great time on our date."
    return

label minami_date_intro_christmas_male:
    show minami happy
    minami.say "Happy Christmas, big bro!"
    minami.say "Come on, we've got a date tonight!"
    "Minami grabs hold of my hand, pulling me along with her."
    "At times like this, it's impossible to resist her enthusiasm."
    show minami normal
    mike.say "Whoa...slow down there, Minami!"
    mike.say "I'm going as fast as I can!"
    return

label minami_date_intro_birthday_male:
    mike.say "Happy birthday, Minami!"
    mike.say "Bet you thought I was going to forget, huh?"
    show minami happy
    minami.say "Thanks, big bro."
    show minami normal
    minami.say "But I kinda knew you'd remember."
    minami.say "I mean, we were there for each other's birthdays as kids!"
    mike.say "Oh yeah - I guess so."
    return

label minami_date_intro_mc_birthday_male:
    minami.say "Happy birthday, big bro!"
    show minami tehe
    minami.say "And for your present - you get a super fantastic date with me!"
    mike.say "Thanks, Minami."
    mike.say "That sounds like the best present I could ask for!"
    mike.say "I should have known you'd never forget my birthday."
    show minami normal
    minami.say "What, big bro - like you forget mine?"
    return

label minami_date_pub_male:
    show minami
    minami.say "Urgh..."
    minami.say "Don't you think this place is kinda, well...boring?"
    hide minami
    return

label minami_date_cinema_male:
    show minami
    minami.say "I've been wanting to see this film since it came out."
    minami.say "So no talking and definitely NO SPOILERS!"
    hide minami
    return

label minami_date_familyrestaurant_male:
    show minami
    minami.say "Hmm..."
    minami.say "I guess this place is okay - but it's kinda like the places Mom and Dad used to take us."
    hide minami
    return

label minami_date_restaurant_male:
    show minami
    minami.say "Ooh, this place looks fancy!"
    minami.say "Let's order the most expensive thing on the menu - then do a runner!"
    hide minami
    return

label minami_date_amusmentpark_male:
    show minami
    minami.say "Ooh, I just LOVE amusement parks."
    minami.say "I want to ride that, and that...AND THAT RIGHT NOW!"
    hide minami
    return

label minami_date_ride_the_ferris_wheel:
    show minami
    minami.say "Sure, it moves kinda slow."
    minami.say "But we have the view all to ourselves..."
    $ minami.love += 1
    hide minami
    return

label minami_date_waterpark_male:
    show minami
    minami.say "Oh yay - the waterpark!"
    minami.say "You better get ready to get splashed!"
    hide minami
    return

label minami_date_park_male:
    show minami
    minami.say "Just a walk in the park...really?"
    minami.say "Erm...I guess that's okay..."
    hide minami
    return

label minami_date_eat_a_burger:
    "Minami smiles from ear to ear at the sight of the burger."
    "And the bites that she takes out of it are quite something too!"
    "I'd almost forgotten that she has a healthy appetite for such a petite girl."
    return

label minami_date_buy_drink:
    if minami.is_visibly_pregnant:
        show minami angry
        $ minami.love -= 10
        minami.say "You can't give me beer, big bro!"
        minami.say "It's bad for the baby."
        minami.say "We're going to be parents soon - you need to be more responsible!"
        $ hero.cancel_activity()
        hide minami
    else:
        "Minami doesn't even blink when I hand her the drink that she asked for."
        "She just takes hold of it and begins to sip happily at the contents."
        "I guess she's just used to getting what she wants!"
    return

label minami_date_play_darts:
    "Minami doesn't look too enthused at the idea of playing darts."
    "But she nods and forces a smile onto her face all the same."
    "In the end, I feel guilty as I beat her easily."
    return

label minami_date_pub_play_pool:
    "Minami takes hold of the cue, which is almost as tall as she is herself."
    "And she tries her best to play the game, really she does."
    "But I find myself distracted by the way her short skirt tends to ride up when she leans in to make a shot..."
    return

label minami_date_buy_a_round:
    if minami.is_visibly_pregnant:
        show minami angry
        $ minami.love -= 10
        minami.say "You can't give me beer, big bro!"
        minami.say "It's bad for the baby."
        minami.say "We're going to be parents soon - you need to be more responsible!"
        $ hero.cancel_activity()
    elif (hero.charm >= 60 - minami.love and minami.flags.drinks < 2):
        show drink minami
        "I stand up and offer to get the next round of drinks in."
        "But I pause out of habit, being used to my friends at least making a token gesture of objection."
        "But Minami just smiles and nods without a single word, reminding me that she can be more than a little spoiled at times..."
        $ game.active_date.score += 5
        if "rebel" in minami.traits:
            $ game.active_date.score += 5
        $ minami.set_flag("drinks", 1, "day", mod="+")
        hide drink
    else:
        "I want to pay a round of beers to the whole pub."
        "But Minami doesn't seem to want to drink, so I refrain from doing so."
        $ hero.cancel_activity()
    return

label minami_dance_with:
    "Minami all but jumps at the chance to get out onto the dance-floor with me."
    "She grabs my hand and practically drags me after her."
    "And then she dances as close as she possibly can, almost clinging to me the whole time!"
    return

label minami_date_play_arcade_intro_male:
    minami.say "OH...MY...GOD!"
    minami.say "Big bro, this place is incredible!"
    minami.say "How long were you going to wait show me it?!?"
    "I can't help smiling as Minami rushes into the arcade ahead of me."
    "She's like a kid in a candy store, flitting from one thing to the next."
    mike.say "I wasn't holding out on you, Minami."
    mike.say "This just seemed like the perfect chance to bring you here."
    mike.say "It kind of reminds me of the arcades we used to visit back home."
    "Minami takes me by the hand, pulling me in her wake."
    "Every turn she makes seems to put us in front of a familiar machine."
    minami.say "We used to play ALL of these back in the day!"
    minami.say "Oh damn it, big bro..."
    minami.say "How are we going to choose?"
    "I shrug and shake my head."
    "But then I spot one arcade cabinet in particular."
    mike.say "Hey, Minami..."
    mike.say "Isn't that 'Luna Mariner'?"
    mike.say "The one with the sailor suits?"
    minami.say "It is, big bro!"
    minami.say "Remember the copy the local arcade had?"
    minami.say "I think we wore it out!"
    "Neither of us needs to say another word."
    "We just exchange a certain look."
    "Then we rush over to the cabinet."
    "I pump coins into the slot."
    "And Minami wiggles her fingers in anticipation."
    return

label minami_date_play_arcade_win_male:
    "Almost as soon as we're in control of our short-skirted heroines, I know I'm good."
    "I've been coming to this arcade since long before Minami moved over here."
    "And this is one of the games that I can't help coming back to."
    minami.say "Hey, big bro!"
    minami.say "That power-up was mine!"
    mike.say "Too slow, Minami!"
    "Even though she plays her best, Minami can't match me."
    "I wonder if she's even played on this game since I left home?"
    "Pretty soon she's puffing and pouting as I pull ahead."
    minami.say "What gives, big bro?"
    minami.say "You were never this good before!"
    minami.say "Hey...go easy on me!"
    "Once we're out of credits and coins to buy more, the game comes to an end."
    "I can see that Minami's already falling into a sulk."
    "Because my score is way higher than hers."
    mike.say "Come on, Minami."
    mike.say "Don't be a bad loser, yeah?"
    "Minami frowns and then sticks her tongue out at me."
    minami.say "Humph..."
    minami.say "Well, I WAS going to let you see me in my new Luna Mariner costume, big bro."
    minami.say "But not now I know that you're a big, stinky jerk!"
    mike.say "Wait...what now?!?"
    mike.say "You have a Luna Mariner costume?!?"
    "Minami smiles, knowing that she's got me, hook, line and sinker."
    minami.say "Yeah, I do, big bro."
    minami.say "And if you DO want to see me in it..."
    minami.say "Well...you'd better let me win next time we play!"
    return

label minami_date_play_arcade_lose_male:
    "Almost as soon as we're in control of our short-skirted heroines, I know I'm in trouble."
    "I haven't been coming to the arcade as much as I used to back home."
    "And so my skills are more than a little rusty when it comes to this game."
    mike.say "Hey, Minami!"
    mike.say "That power-up was mine!"
    minami.say "Ha ha...you're too slow, big bro!"
    "Even though I'm giving it my best, I can't hold a torch to Minami."
    "She must have been practicing at this game after I left home."
    "Pretty soon I'm cursing under my breath as she leaves me behind."
    mike.say "What the hell, Minami?"
    mike.say "When did you get this good?!?"
    mike.say "Wait...be nice to me!"
    minami.say "I dunno, big bro."
    minami.say "I'm just SO into Mariner Luna right now."
    minami.say "I even got a new Mariner Luna costume..."
    "The words sink in just as I see a short skirt reveal a flash of underwear on the screen."
    "And suddenly all I can think of is Minami in the same kind of outfit!"
    mike.say "Wait...what now?!?"
    mike.say "You have a Luna Mariner costume?!?"
    "Minami smiles, knowing that she's got me, hook, line and sinker."
    minami.say "Yeah, I do, big bro."
    minami.say "And if you DO want to see me in it..."
    minami.say "Well, you'd better be real nice to me!"
    "Once we're out of credits and coins to buy more, the game comes to an end."
    "I try not to fall into a sulk, because Minami's score is way higher than mine."
    "Minami sticks her tongue out at me and then bursts out laughing."
    minami.say "Don't be a bad loser, big bro!"
    mike.say "Ah..."
    mike.say "Whatever, Minami!"
    mike.say "Now, about that costume you mentioned before..."
    return

label minami_dick_reactions:
    if not minami.flags.seendick:
        $ minami.flags.seendick = 1
        if hero.has_skill("hung"):
            show dick reactions minami scared
            minami.say "Whoa, big bro - you are seriously BIG!"
            minami.say "I mean, I've seen it before, but..."
            mike.say "Hey...what does that mean?"
            show dick reactions minami smile
            minami.say "Who cares - we're doing this thing now."
            minami.say "I waited long enough to get that thing inside of me already!"
            $ minami.sub += 10
        elif hero.has_skill("smalldick"):
            show dick reactions smile
            minami.say "Aww..."
            minami.say "Big bro and little bro!"
            mike.say "Hey!"
            minami.say "Don't worry about it, big bro."
            minami.say "He's just the right size for my little pussy!"
            show dick reactions minami tasty
            minami.say "Come and see for yourself..."
            $ minami.sub -= 10
        hide dick reactions
    return

label minami_peeping_scene_male:
    "I swear that all I was doing was walking past the bathroom on my way to somewhere else."
    "And the only reason that I stopped at all was the fact that the door was left ajar."
    "That and there was the sound of running water too, which caught my attention."
    "At most I thought that one of the girls had forgotten to close the door behind them."
    "Or else they'd jumped in the shower it had slipped their minds that it was open."
    "All I meant to do was quietly close it for them - honestly!"
    "But then I just can't fight the urge to take a quick peak around the door..."
    "And there she is - Minami, standing under the shower-head."
    "There's steam and condensation on the glass of the shower cubicle."
    "But that doesn't stop me seeing the outline of her body."
    "Petite and slight, yet unmistakably feminine too."
    "I sweat that I can even make out the shape of her breasts."
    "That I can see the water as it drips from her nipples..."
    "It's amazing to watch as it cascades over her."
    "More amazing than I could ever have imagined."
    "Almost amazing enough to make forget what I'm actually doing right now..."
    return

label minami_peeping_reactions_male:
    if (minami.love >= 150 or minami.sub >= 50) and minami.sexperience:
        show minami naked
        minami.say "Hey, big bro..."
        minami.say "I know you're there!"
        "I feel a chill down the length of my spine."
        "I've been busted, and now I'm going to get it!"
        show minami happy
        minami.say "I know that you're watching me right now."
        minami.say "And it's making me SO hot!"
        "Minami doesn't turn her head to the door as she says this."
        "Instead she reaches between her legs with one hand."
        "Is she..."
        "Is she really doing what I think she is?"
        minami.say "Mmm..."
        minami.say "I can see bits of me that you can't, big bro."
        minami.say "Parts of me that are getting wetter too!"
        "I almost fall head-first through the door."
        "Minami actually has her hand between her thighs."
        "And she looks like she's playing with herself!"
        minami.say "Ah..."
        minami.say "Oh...oh yeah..."
        minami.say "Makes me feel so hot..."
        minami.say "Knowing you're watching me, big bro..."
        "I can't help feeling my cock getting hard."
        "Watching Minami touching herself in the shower like this..."
        "What I wouldn't give to be in there with her right now!"
        $ minami.love += 1
        $ minami.siscon += 5
        $ minami.sub += 1
        minami.say "Oh...oh..."
        minami.say "Ah...big bro!"
        "I can't stop to watch Minami cum, or else I will too!"
        "Instead I creep away towards the safety of my bedroom."
        "And I'm bent double the whole way."
    else:
        show minami naked angry
        minami.say "HEY!"
        minami.say "BIG BRO - is that you?!?"
        "I stand up straight and begin to back off."
        "That tone in Minami's voice is more than a little familiar."
        "I remember hearing it back when we were kids together."
        "And then, as now, it never meant anything good was coming my way!"
        mike.say "Whoa...no need to get mad, Minami."
        mike.say "I was just checking to see if the bathroom was occupied."
        "Wrapped in a towel and still dripping from the shower, Minami confronts me."
        "She stands in the doorway, glaring up at me with murder in her eyes."
        minami.say "We're not at home anymore, big bro!"
        show fx anger
        minami.say "And that means no walking in on me or peeping - you got that?!?"
        mike.say "Of course I do, Minami, of course!"
        mike.say "Like I already said - this was just a misunderstanding, that's all."
        minami.say "Yeah, well..."
        minami.say "Anymore misunderstandings and you won't misunderstand what I do to you, big bro!"
        $ minami.siscon += 5
        $ minami.love -= 20
        $ minami.sub -= 5
        play sound door_slam
        pause 0.4
        scene bg door bathroom at center, zoomAt(1.25, (640, 880))
        with hpunch
        "With that, Minami slams the door in my face."
        "Which leaves me to scuttle off on my way."
    return

label minami_halloween_invitation:
    show minami
    "Almost as soon as [bree.name], Sasha and I agreed to hold the Halloween party, a thought occurred to me."
    "What about Minami?"
    "She's living here in the house with us now, so she deserves to know what we're planning."
    "But then a second thought occurs to me, more urgent than the first."
    "If Minami agrees to come to the party, then I want her there as my date."
    "Sure, part of that is because I still feel protective of her."
    "I don't like the thought of [bree.name] and Sasha's male friends flirting with Minami."
    "Or, come to think of it, any of the guys that I know either!"
    "But If I'm honest, it's for a far more selfish reason."
    "Because if anyone's going to hit on Minami in a cute costume - I want it to be me!"
    "As soon as I can get Minami alone, I hastily ask the question."
    mike.say "Minami..."
    mike.say "Have you made any plans for Halloween yet?"
    show fx question
    minami.say "Huh?"
    minami.say "I don't know, big bro."
    minami.say "Why?"
    show minami tehe
    minami.say "Do you wanna go trick or treating with me?"
    "Minami giggles and gives me a smile as she says this."
    "And it's the kind of smile that makes me know what treat I want from her!"
    mike.say "Not exactly, Minami."
    mike.say "It's just that [bree.name], Sasha and I were going to have a party."
    mike.say "You're invited - of course!"
    mike.say "And I wondered if you'd be my date?"
    if minami.love >= 100 or minami.siscon >= 60 or Harem.together(bree, sasha, minami, name='home'):
        show minami happy
        $ minami.love += 1
        "Minami's eyes light up at the invitation."
        "And instantly I can feel my heart thumping in my chest."
        "Because I know that expression from when we were kids."
        "It means she's super interested in coming to the party!"
        minami.say "Big bro, this is perfect!"
        mike.say "It...it is?"
        minami.say "Sure it is."
        show minami normal
        minami.say "I was going to do a livestream on Halloween."
        minami.say "To show off my latest cosplay creations to my audience."
        mike.say "And now...you're not?"
        show minami happy
        minami.say "Now I can get footage of me wearing one of them to an actual party."
        minami.say "That's much better than what I had in mind."
        mike.say "That's great, Minami."
        mike.say "But you are going to be my date, right?"
        show minami normal
        "Minami looks blankly at me for a moment."
        "But then she nods and smiles."
        minami.say "Sure, big bro, sure."
        show minami tehe
        minami.say "I can do both at once!"
        "I nod, realising that I really can't hope for anything more."
        hide minami
        "But when I open my mouth to ask what she's going as, Minami's already gone."
        "I look up to see her skipping away, no doubt thinking about her costume."
        "All I can do is sigh and shake my head."
        "At least I got myself a date to the party."
        "Even if she's likely to forget about that part!"
        $ game.flags.halloween_girl = "minami"
    else:
        show minami annoyed
        "Minami wrinkles her nose at the invitation."
        "And instantly I can feel my heart sink."
        "Because I know that expression from when we were kids."
        "It means she's about to turn me down!"
        minami.say "Aw, I'd love to, big bro."
        minami.say "But I'm doing a livestream on Halloween."
        minami.say "Showing off my latest cosplay creations."
        show minami sad
        minami.say "And I can't let my followers down!"
        mike.say "Ah...okay...I guess."
        mike.say "I wouldn't want that to happen..."
        show minami normal
        "All of a sudden, Minami's face is sweetness and light again."
        minami.say "Thanks for being so understanding."
        show minami tehe
        minami.say "You're the best, big bro!"
        mike.say "Yeah, that's me."
        mike.say "The best guy without a date!"
        hide minami
        "But Minami doesn't hear me."
        "As she's already skipped off, leaving me all alone."
    return

label minami_halloween_arrival:
    scene bg house
    "I stare at the door for a moment longer, and then I strike myself on the forehead."
    "Of course, Minami's living here, so my date's already in the house!"
    scene bg livingroom with fade
    "Geez, I must have scrambled my brain putting so much effort into the party."
    show minami halloween with dissolve
    "But the same can't be said for Minami, as she looks at me expectantly."
    minami.say "Well, big bro?"
    minami.say "What do you think?"
    "Ah, I get it now."
    "This is where I'm supposed to gush over her costume."
    "You know - tell her that she looks amazing?"
    menu:
        "Compliment":
            mike.say "Ah, Minami..."
            mike.say "I never got what was so popular about those sailor suits."
            mike.say "Well, not until I saw you in that one!"
            show minami happy
            $ minami.love += 1
            "Minami clasps her hands under her chin and jumps up and down."
            "Wow...she looks just like something out of a cutesy anime!"
            minami.say "Aww, thanks, big bro!"
            show minami tehe
            minami.say "I picked this outfit just for you."
            minami.say "It means so much to know that you like it."
            "I shake my head, unable to speak at first."
            mike.say "It's perfect, Minami."
            mike.say "I wish you could wear it all the time!"
            "Minami giggles at the compliment."
            minami.say "Oh, I couldn't wear it ALL the time, big bro."
            minami.say "You'd never be able to keep your hands off me!"
            hide minami with hpunch
            "Minami grabs hold of my hand and pulls me after her."
            "I almost trip over my own feet as she does so."
            "Because I'm too busy staring at her to do anything else."
        "Criticize":
            mike.say "Ah, Minami..."
            mike.say "Don't take this the wrong way."
            mike.say "But doesn't that outfit make you look...well, a little young?"
            show minami a annoyed
            $ minami.love -= 4
            "Minami frowns at me, planting her fists on her hips."
            "I can already see that this isn't going well."
            minami.say "It's a schoolgirl's uniform, big bro."
            minami.say "What else is it supposed to do?"
            mike.say "Yeah, I know that."
            mike.say "I just..."
            mike.say "I don't know if I want people to think we go that far back!"
            show minami surprised
            "Minami cocks her head on one side, clearly confused."
            minami.say "But...we go way back, big bro."
            minami.say "Back to when we were kids."
            mike.say "Yeah, but we weren't an item back then."
            mike.say "And they might think we were!"
            show minami tehe
            "Minami sticks out her tongue and blows a raspberry at this."
            "Which only serves to make her look younger than ever!"
            minami.say "Oh, stop being such a prude!"
            minami.say "You're going to spoil the party before it gets started."
            hide minami with hpunch
            "Minami grabs hold of my hand and pulls me after her."
            "But I can tell from the look on her face that she's still mad at me."
    scene bg black with dissolve
    pause 1
    return

label minami_halloween_party:
    $ game.pass_time(2)
    scene bg livingroom
    show minami halloween
    with dissolve
    minami.say "Hey, big bro - let's grab some punch!"
    "Without waiting for an answer Minami bounces over to the punch-bowl."
    "She reaches for a cup and the ladle, but then finds someone in her way."
    hide minami
    show minami halloween at right5
    show scottie halloween at left5
    with moveinleft
    scottie.say "Whoa there, little lady!"
    scottie.say "Are you even old enough to drink?"
    show minami annoyed
    "Minami's features instantly contort into a grimace."
    "And she pokes a finger in Scottie's face."
    minami.say "Of course I am!"
    minami.say "Tell him, big bro!"
    "I step in between them, trying to calm the situation."
    menu:
        "Tell off":
            mike.say "She's legal, Scottie."
            mike.say "Not that it's any of your business."
            "Scottie holds his hands up and backs off."
            show scottie angry
            scottie.say "Okay, dude, okay."
            scottie.say "I was just trying to be responsible - that's all!"
            mike.say "I get that, Scottie."
            mike.say "But Minami's already got me looking out for her."
            hide scottie
            show minami halloween at center
            with moveoutleft
            $ minami.sub += 1
            "With that, Scottie nods and slinks away."
            "Which leaves to bask in Minami's gratitude."
            show minami happy
            minami.say "Yeah, go, big bro!"
            minami.say "You told him where to get off!"
        "Laugh it off":
            mike.say "Heh..."
            mike.say "I know what you're thinking, Scottie."
            mike.say "She does look a little like jailbait, yeah?"
            $ minami.love -= 2
            "Scottie laughs and nods his head at this."
            show minami angry
            "But Minami becomes even more annoyed."
            scottie.say "Yeah, you can say that again, dude!"
            minami.say "Hey!"
            minami.say "What the hell, big bro?!?"
            "I ignore Minami's latest outburst."
            "And instead I keep talking to Scottie."
            mike.say "She's legal."
            mike.say "Take it from me, man."
            hide scottie
            show minami halloween angry
            with moveoutleft
            "Scottie nods and wanders off."
            "But I can see Minami scowling at me."
    scene bg black with dissolve
    pause 1
    return

label minami_halloween_dance:
    $ game.pass_time(2)
    scene bg livingroom
    show minami halloween
    with dissolve
    minami.say "Ooh..."
    minami.say "I love this song!"
    show minami happy
    minami.say "Big bro, we HAVE to dance to this - right now!"
    "Before I can even argue, Minami has a hold of my hand."
    "I'm actually a little frightened by the strength of her grip!"
    "She's hauling me towards the makeshift dance-floor."
    "And I can hear the sound of some awful bubblegum pop awaiting us."
    mike.say "Ah..."
    mike.say "I don't think I know this one, Minami!"
    show minami normal
    minami.say "Don't worry, big bro."
    minami.say "It'll be fun!"
    menu:
        "Accept":
            "It'd take all of my strength to resist."
            hide minami with dissolve
            "And so I allow myself to be pulled onto the dance-floor."
            "But it doesn't take long for me to realise I was wrong."
            "Because Minami doesn't bounce around for too long."
            show dance minami halloween with dissolve
            $ minami.love += 1
            $ minami.siscon += 2
            "Instead she wraps her arms around me and clings on."
            "And all of that energy goes into holding onto me."
            "It's not like one of those slow dances in the movies."
            "In fact, she reminds me a little of an excitable puppy."
            "But all of that intensity is directed at dancing with me."
            "And when I put my hands on her ass, Minami smiles up at me."
            minami.say "See, big bro?"
            minami.say "I told you it'd be fun!"
            "Minami puts her arms around my neck."
            hide dance
            show minami kiss halloween
            with dissolve
            $ minami.flags.kiss += 1
            "And then she pulls me down so she can kiss me."
            "It feels amazing, like she's charged with electricity."
            "I can almost feel her infectious energy passing into me."
            "The song must have ended some time ago, fading into the next."
            "But I don't even notice the change."
            "Minami's the only thing on my mind the whole time."
        "Refuse":
            "It takes all of my strength, but I manage to resist."
            "I keep myself from being dragged onto the dance-floor."
            show minami angry
            $ minami.love -= 1
            $ minami.siscon -= 2
            minami.say "Aw, big bro!"
            minami.say "You're no fun."
            hide minami
            show minami halloween angry at left5
            show jack halloween normal at right5
            with moveinright
            jack.say "You want to dance with me, Minami?"
            show minami normal
            show fx exclamation at left5
            "Both of our heads snap around at the sound of Jack's voice."
            "But Minami is the first one to respond to his offer."
            show minami tehe
            minami.say "Sure thing, Jack!"
            hide minami
            hide jack
            with dissolve
            "I'm forced to watch as they hurry off together."
            "And what follows is pretty torturous from my point of view."
            "I know that Jack's always admired Minami from afar."
            "And she's mad at me, so determined to make me jealous."
            "This means that Minami flirts outrageously with Jack."
            "She never goes too far, but she does everything else possible."
            "And all I can do is stand there and watch."
    scene bg black with dissolve
    pause 1
    return

label minami_halloween_sex:
    if minami.siscon >= 95:
        scene bg black with timelaps
        scene bg livingroom
        show minami halloween
        with timelaps
        "The party's been going on for a good few hours by now, and it's getting late."
        "Things have started to die down as people are becoming drunk and tired."
        "But the same thing can't be said for Minami, who still seems full of energy."
        "She looks left and right, like she's checking that the coast is clear."
        scene bg bedroom5
        show minami halloween tehe
        with fade
        "And then she grabs my hand, pulling me into her bedroom."
        mike.say "Whoa..."
        mike.say "What's the matter, Minami?"
        mike.say "There's no hurry, we have all night!"
        show minami hunt
        "Minami giggles and shakes her head."
        "And I see that she's locked the door behind us."
        minami.say "I'm not waiting any longer, big bro."
        minami.say "I'm desperate for you!"
        "I raise my eyebrows at this."
        "Sure, I'm surprised in that moment."
        "But it's definitely a pleasant surprise."
        "And one that I instantly want to make the most of."
        show minami c
        "Minami stands in front of me, a knowing smile on her face."
        "She has her hands clasped behind her back, leaning forwards."
        minami.say "I know that you've been looking at me all night, big bro."
        minami.say "And I know that you've been thinking I'm a naughty girl!"
        mike.say "I...I have?"
        "Minami giggles, shaking her head."
        minami.say "Of course you have."
        minami.say "You've been thinking that I skip school all the time."
        minami.say "That I skip school and do naughty things with guys like you."
        minami.say "Like I let them fuck me in my bedroom!"
        show minami a normal
        "I watch as Minami walks slowly over to the bed."
        "She holds my eye every step of the way."
        "And she moves like I've never seen her move before."
        "Her slight, petite form sways and swaggers."
        "And it's all I can do to keep my mouth from hanging open."
        "Minami seems to notice the effect that she's having on me."
        "Because she giggles again as she sits on the edge of the bed."
        "Looking back over her shoulder, she beckons me over."
        minami.say "Come on, big bro."
        minami.say "What are you waiting for?"
        show minami b hunt
        minami.say "You know how to deal with a naughty little girl like me!"
        "As if to underline the point, Minami shakes her ass from side to side."
        "I don't need anymore encouragement."
        show minami close
        "Closing the distance between us, I grab hold of her waist."
        "Minami squeals with delight as I do so, pushing her ass against me."

        "And I have my already hard cock out a moment later."
        "We tumble on the bed, a mass of limbs and libido."
        show minami cowgirl halloween with fade
        "And somehow Minami ends up atop me, reverse cowgirl style."
        "Slick and slippery against the tip, she doesn't need coaxing."
        show minami cowgirl vaginal
        "I slide all the way onto Minami in what feels like one motion."
        "The whole time I can see her face, glancing back over her shoulder."
        show minami cowgirl surprised
        if hero.has_skill("hung"):
            show minami cowgirl hung poke
        "Her eyes and her mouth are wide open as she takes it."
        mike.say "You like that?"
        mike.say "You like how that feels?"
        mike.say "Huh, you naughty little bitch?"
        show minami cowgirl orgasm
        minami.say "Uh..."
        minami.say "Oh god..."
        minami.say "I love it, big bro!"
        minami.say "Please...fuck me...hard!"
        "I don't hesitate to give Minami what she wants."
        "There's no gentle building up or gradually gaining speed."
        show minami cowgirl speed
        "I thrust into her as hard as I can manage right from the start."
        "Minami pants and moans the whole time she's riding my cock."
        "The bedspring starts to do horrible sounds."
        "And part of me is worried that it's going to break and we end up on the floor."
        "But the largest part of my brain couldn't care less if it does."
        "Because I'm having too much fun fucking Minami's brains out to care."
        "It feels like we've been at it forever."
        "But in truth I can't have been inside of her for that long."
        "Not before I feel myself starting to cum."
        "Minami senses it too, I can see it reflected in her face."
        minami.say "Y...yes..."
        minami.say "Do it...big bro..."
        minami.say "Cum in me!"
        with vpunch
        "I'm already there as Minami's saying the words."
        show minami cowgirl ahegao creampie -blur -speed with vpunch
        "She wriggles on the end of my cock as I shoot my load into her."
        with vpunch
        "And when I'm done, she flops forwards, falling onto the mattress."
        "All I can do is look down on her, panting and sweating."
        "I don't even know if she's just exhausted like I am."
        "That or if she's actually slumped over on the bed and passed out!"
        $ minami.sexperience += 1
        $ game.pass_time(1)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
