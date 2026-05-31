label alexis_date_intro_valentine_male:
    mike.say "Happy Valentine's day, Alexis!"
    mike.say "You were the best valentine back in high school."
    mike.say "And I'm so glad you're still my valentine tonight!"
    "Alexis's cheeks flush and she smiles sweetly."
    alexis.say "Oh, [hero.name]..."
    alexis.say "I'm so happy you're still my valentine too!"
    return

label alexis_date_intro_halloween_male:
    mike.say "Aww, Alexis!"
    mike.say "You didn't dress up as something scary for Halloween?"
    "Alexis looks confused at this, frowning and shaking her head."
    alexis.say "Huh?"
    alexis.say "I thought we were going on a date, not trick or treating!"
    "I hold up a hand, letting Alexis know that I was just kidding."
    mike.say "I'm kidding, Alexis, I'm kidding."
    mike.say "I just remember you wearing some pretty hot Halloween costumes back in high school."
    alexis.say "They must have been something if you remember them after all this time!"
    alexis.say "But how about we make some new Halloween memories tonight?"
    return

label alexis_date_intro_christmas_male:
    alexis.say "Merry Christmas, [hero.name]!"
    alexis.say "I hope you're ready for our date - because I know I am!"
    "I can't help smiling as Alexis's enthusiasm starts to infect me too."
    mike.say "I was totally ready, Alexis."
    mike.say "But now you've made me even more excited!"
    return

label alexis_date_intro_birthday_male:
    mike.say "Happy birthday, Alexis!"
    mike.say "Geez...saying that takes me back to high-school."
    mike.say "Only I didn't get you a cake with candles this time!"
    alexis.say "Oh, don't worry about that, [hero.name]."
    alexis.say "We might not have cake and balloons like we did when we were kids."
    alexis.say "But now that we're all grown up, we can play party-games that are SO much more fun!"
    return

label alexis_date_intro_mc_birthday_male:
    mike.say "Hey, Alexis..."
    mike.say "Time for our date!"
    alexis.say "Okay, [hero.name]..."
    alexis.say "But first - happy birthday!"
    mike.say "Aw...thanks, Alexis - you remembered!"
    alexis.say "Sure I did, [hero.name]."
    alexis.say "We've known each other since forever!"
    return

label alexis_date_eat_a_burger:
    "I get the distinct impression that Alexis is used to better than a burger in a bar."
    "She obliges by eating her food when it turns up."
    "But the whole time she looks as though she's choking it down, and quite resentfully too!"
    $ game.active_date.score -= 5
    return

label alexis_date_buy_drink:
    if alexis.is_visibly_pregnant:
        show alexis angry
        $ alexis.love -= 10
        alexis.say "[hero.name]!"
        alexis.say "Are you serious?!?"
        alexis.say "You know I can't drink in my condition!"
        $ hero.cancel_activity()
        hide alexis
    else:
        "Alexis's face practically lights up at the sight of the drink that she ordered."
        "She lifts it to her lips and takes a generous sip whilst smiling the whole time."
        "Maybe the way to her heart is actually through her penchant for alcohol?"
        $ game.active_date.score += 5
    return

label alexis_date_play_darts:
    "The moment I suggest playing darts, Alexis frowns and crosses her arms in irritation."
    "She obliges me by playing a couple of games anyway."
    "But she makes a point of being awkward and uncooperative the whole time, and so the whole experience is ruined."
    return

label alexis_date_pub_play_pool:
    "Alexis practically strides to the pool-table, taking me by surprise with her enthusiasm for a game."
    "Though as we begin to play, I do have to wonder if it's actually genuine."
    "As she seems to spend more time draping herself on the table and wiggling her ass as she shoots."
    "In fact, she pays more attention to the attention being paid to her than the balls on the table."
    return

label alexis_date_buy_a_round:
    if alexis.is_visibly_pregnant:
        show alexis angry
        $ alexis.love -= 10
        alexis.say "[hero.name]!"
        alexis.say "Are you serious?!?"
        alexis.say "You know I can't drink in my condition!"
        $ hero.cancel_activity()
    elif (hero.charm >= 60 - alexis.love and alexis.flags.drinks < 2):
        show drink alexis
        "Alexis smiles broadly and flutters her eyelids at me when I offer to buy the next round."
        "The effect is such that I totally forget if it's actually my round at all."
        "Come to think of it - has she bought a single drink all night?"
        $ game.active_date.score += 5
        if "rebel" in alexis.traits:
            $ game.active_date.score += 5
        $ alexis.set_flag("drinks", 1, "day", mod="+")
        hide drink
    else:
        "I want to pay a round of beers to the whole pub."
        "But Alexis doesn't seem to want to drink, so I refrain from doing so."
        $ hero.cancel_activity()
    return

label alexis_dance_with:
    "I barely remember dancing with Alexis when we were last together, as other things stick in my mind more."
    "But stepping onto the dance-floor with her now, I find that she's all about the intimate and slow moves."
    "She fixes me with those huge eyes and puts a hand on my cheek, and I'm all but entranced from that moment on."
    return

label alexis_date_play_arcade_intro_male:
    alexis.say "Do we really have to do this, [hero.name]?"
    alexis.say "I mean, I was never into arcades when we were in school."
    alexis.say "So what makes you think that changed?"
    "I've been trying to ignore Alexis's complaints about the arcade."
    "I mean, yeah, it was my idea to come here and spend some time."
    "And I had been hoping that she might be more up for it."
    "But it's not like I've refused to do things she wanted to in the past."
    "So she could at least try to suck it up and return the favour!"
    mike.say "Just play one game with me, okay?"
    mike.say "That's all I'm asking for, Alexis."
    mike.say "And then if you're still not feeling it..."
    mike.say "Well we can go do something else, yeah?"
    "Alexis rolls her eyes and let's out a sigh."
    "But she nods all the same."
    alexis.say "Okay, [hero.name], fine."
    alexis.say "We play ONE game."
    alexis.say "Then we go do something adult!"
    "I nod, glancing around for a game we can play."
    "And then my eyes settle on a possible candidate."
    mike.say "How about 'Adolescent Anthropoid Assassin Alligators'?"
    alexis.say "Hey, wait a minute..."
    alexis.say "I remember that show!"
    alexis.say "I could never get the theme tune out of my head!"
    "We walk over to the arcade cabinet and I pump coins into the slot."
    mike.say "You be Mona Lisa, and I'll be Venus de Milo."
    return

label alexis_date_play_arcade_win_male:
    "Alexis's initial burst of enthusiasm is short-lived."
    "And that might have a lot to do with her skills at the game."
    "Because to put it bluntly, she sucks!"
    alexis.say "Hey!"
    alexis.say "How am I supposed to..."
    alexis.say "No fair - they're beating me up!"
    mike.say "Ah...this IS a beat-em-up, Alexis."
    mike.say "You have to get them before they get you!"
    "Together we sweat our way through a stack of coins."
    "And by the end of it all, Alexis is pretty fried."
    mike.say "Erm..."
    mike.say "How was it for you, Alexis?"
    mike.say "Did you have a nice trip down memory lane?"
    "Alexis shoots me a withering look."
    "And I can already see our time in the arcade is over."
    alexis.say "It reminded me that videogames suck."
    alexis.say "Is that what you mean?"
    mike.say "Okay, Alexis, okay."
    mike.say "Lets go do something else..."
    return

label alexis_date_play_arcade_lose_male:
    "Alexis's initial burst of enthusiasm refuses to die."
    "And that might have a lot to do with the fact that she's a natural!"
    "Somehow it just seems to come to her as she plays the game."
    alexis.say "HAH!"
    alexis.say "Did you see that, [hero.name]?"
    alexis.say "I totally wiped that guy out!"
    mike.say "Hey, Alexis!"
    mike.say "Leave some of them for me!"
    "Together we sweat our way through a stack of coins."
    "And by the end of it all, I'm feeling pretty fried."
    "But Alexis seems to be buzzing."
    alexis.say "That was great, [hero.name]."
    alexis.say "Just like being inside of the cartoon!"
    alexis.say "We should do this more often."
    mike.say "You really think so, Alexis?"
    "She nods and lets out a giggle."
    alexis.say "Oh yeah, [hero.name]."
    alexis.say "You could use the practice!"
    return

label alexis_dick_reactions:
    if not alexis.flags.seendick:
        $ alexis.flags.seendick = 1
        if hero.has_skill("hung"):
            show dick reactions alexis scared
            alexis.say "Whoa!"
            mike.say "What's up, Alexis?"
            mike.say "It's not like you never saw it before now!"
            show dick reactions alexis smile
            alexis.say "I...I know..."
            alexis.say "I just never remembered it being THAT big!"
            $ alexis.sub += 10
            $ alexis.love += 10
        elif hero.has_skill("smalldick"):
            show dick reactions alexis disgusted
            alexis.say "Oh my god!"
            mike.say "What's up, Alexis?"
            mike.say "It's not like you never saw it before now!"
            alexis.say "I...I know..."
            alexis.say "I just remembered it being bigger, that's all."
            show dick reactions alexis mock
            alexis.say "Did you have surgery to make it smaller or something?"
            $ alexis.sub -= 10
            $ alexis.love -= 10
        hide dick reactions
    return

label alexis_halloween_invitation:
    show alexis
    "The more I think about it, the more sure I am that Alexis is the perfect girl to invite to the Halloween party."
    "She's fun, up for a good time and she's always wanting to meet new people when we're out together."
    "So this is a great chance to introduce her to my room-mates, as well as my male friends too!"
    "In fact, now that I've thought it through - what could possibly go wrong?"
    "That's why I don't beat about the bush the next time that I get to see Alexis."
    "I just come straight out and ask her."
    mike.say "Alexis..."
    mike.say "We're having a Halloween party at my place this year."
    mike.say "And I was wondering if you wanted to come along?"
    "Alexis raises her eyebrows at the mention of a party."
    "And I can see that I've piqued her interest."
    alexis.say "Ooo..."
    alexis.say "It's been a while since I went to a Halloween party."
    alexis.say "What's the plan - just a bunch of friends hanging out?"
    "I shake my head."
    mike.say "Oh, no way, Alexis."
    mike.say "We're going to have all sorts of spooky stuff going on."
    mike.say "It's a costume party too, so you should think of something to come as."
    "I pause for a moment, taking a deep breath."
    mike.say "And I kind of wanted to ask if you'd come with me."
    mike.say "You know...as my date?"
    if alexis.love >= 100:
        "Alexis smiles at my awkward invitation."
        "And I can see that she's flattered by the attention too."
        alexis.say "Well, I was going to say no."
        alexis.say "But seeing as it's you asking."
        $ alexis.love += 1
        alexis.say "I can make an exception!"
        "I can't keep my face from breaking into an instant smile."
        "Sure, maybe it makes me look like I was desperate."
        "But it worked - Alexis is coming to the Halloween party!"
        mike.say "That's great, Alexis!"
        mike.say "At least it will be now you're coming."
        show alexis happy
        "Alexis smiles, like a cat that's got the cream."
        "Yeah, I know that I'm stroking her ego right now."
        "But can you blame me?"
        "I have my date for the party."
        "An she's going to the hottest girl there!"
        show alexis normal
        alexis.say "Oh..."
        alexis.say "I have the perfect idea for my costume."
        show alexis flirt
        alexis.say "Just wait until you see it."
        alexis.say "I promise you won't be disappointed!"
        "I nod and smile, resisting the temptation to ask for a preview."
        "That way it'll be a bigger surprise on the actual night of the party."
        $ game.flags.halloween_girl = "alexis"
    else:
        show alexis confused
        "Alexis frowns a little at this."
        "Like she just remembered something important."
        alexis.say "Yeah, [hero.name]..."
        alexis.say "I don't know about that."
        mike.say "What do you mean, Alexis?"
        mike.say "You sounded like you were into the idea just now."
        mike.say "Don't you want to be my date?"
        alexis.say "Aw, no, [hero.name] - that's not it."
        alexis.say "It's just that I haven't been to one because..."
        alexis.say "Because they're not really my kind of thing."
        alexis.say "You know what I mean?"
        "I don't know what she means."
        "And I can't keep it from showing as I answer her."
        mike.say "Ah, no, Alexis - not really."
        show alexis normal
        alexis.say "I just think it might be more fun to do something else."
        alexis.say "Like maybe go see a scary movie?"
        alexis.say "Or go to a nightclub maybe?"
        "All I can do is shrug in confusion."
        "If Alexis doesn't want to go to the party, I can't force her."
        mike.say "Okay, Alexis."
        mike.say "I'll cross your name off the guest-list."
    return

label alexis_halloween_arrival:
    scene bg house
    "Opening the door, I guess I should have been more cautious."
    "Especially after the incidents with Jack's sword and Scottie's trident."
    "But this time it's not a weapon that stops me in my tracks."
    "Though it's still a pair of guns!"
    show alexis halloween
    alexis.say "Hey, [hero.name]."
    alexis.say "I'm not too early - am I?"
    mike.say "Ah..."
    mike.say "N...no, Alexis...you're perfect."
    mike.say "I mean your timing's perfect!"
    "Alexis is standing there dressed as an angel."
    "Harp, halo, wings - all the stuff you'd expect."
    "But no angel I ever saw had a body like that!"
    "She really does look like a little piece of paradise."
    alexis.say "Oh...that's good."
    alexis.say "Well - do you like my costume?"
    menu:
        "Compliment":
            "I can't help smiling."
            "Grinning at Alexis like a fool."
            alexis.say "Hey!"
            alexis.say "What's with that smile?"
            mike.say "Good choice of costume, Alexis."
            mike.say "Because you look heavenly!"
            show alexis blush
            $ alexis.love += 1
            "Alexis looks away, her cheeks flushing red."
            alexis.say "Do...do you really mean that?"
            mike.say "Of course I do, Alexis."
            mike.say "I don't think you've ever looked more beautiful!"
            "Clutching her harp in one hand, Alexis steps into the hallway."
            "With the other she takes a firm hold of my wrist."
            show alexis -blush
            alexis.say "Come on, let's get mingling."
            alexis.say "That way you can show me off to all your friends!"
            "I nod as Alexis drags me along in her wake."
            "I mean, who wouldn't want to be seen with her?"
        "Criticize":
            "When I think about the implications, I can't help smiling."
            "Alexis picks up on this, and her smile turns into a frown."
            alexis.say "Hey!"
            alexis.say "What's so funny?"
            mike.say "Well, it's just...an angel?"
            mike.say "Really, Alexis?"
            mike.say "Is that supposed to be ironic or something?"
            show alexis confused
            alexis.say "What do you mean?"
            mike.say "Come on, Alexis - you're hardly pure and innocent!"
            show alexis angry
            $ alexis.love -= 4
            "Alexis balls her fists and clutches at her harp."
            "And for a moment I actually think she's going to hit me with it."
            alexis.say "Okay, [hero.name], I'm going to forget you said that."
            alexis.say "You've got one more chance to be nice to me."
            alexis.say "So you'd better be on your best behaviour from now on!"
            "I nod my head, but keep the smirk on my face as I do so."
            mike.say "Okay, Alexis, okay."
            mike.say "I'll be good - I promise!"
    scene bg black with dissolve
    pause 1
    return

label alexis_halloween_party:
    $ game.pass_time(2)
    scene bg livingroom
    show alexis halloween
    with dissolve
    alexis.say "Hmm..."
    alexis.say "There's more girls here than guys."
    mike.say "Huh..."
    mike.say "What was that, Alexis?"
    alexis.say "I said you invited more girls than guys."
    "Alexis nods towards Jack and Scottie."
    "But then I see her smile as she studies them."
    alexis.say "I gotta say - they're pretty cute though!"
    "What the hell?"
    "Is she actually checking them out in front of me?"
    "Alexis is supposed to be my date tonight!"
    menu:
        "Ignore it":
            "Wait a minute - what am I even thinking?"
            "What happened in the past is in the past."
            "Of course Alexis isn't going to cheat on me."
            "She's just complimenting Jack and Scottie, that's all."
            mike.say "Yeah, but you're the lucky one tonight."
            show fx question
            alexis.say "Ah...why's that?"
            mike.say "Because your date's cuter than the pair of them - right?"
            show alexis confused
            "For a moment Alexis looks confused."
            show alexis happy
            $ alexis.love += 2
            "But then she shakes her head and smiles."
            alexis.say "Oh, yeah...I get it!"
            show alexis normal
            alexis.say "And don't be so vain, [hero.name]!"
            "She slaps me playfully on the shoulder."
            "And I choose to take that as a good sign."
        "Call her out":
            "How can she be doing this again?"
            "After what she did to me back in high-school?!?"
            mike.say "Ah, Alexis..."
            mike.say "That's really not cool, you know?"
            show alexis confused
            "Alexis looks confused."
            alexis.say "What do you mean, [hero.name]?"
            alexis.say "Did I do something wrong?"
            "I can feel my cheeks flushing."
            "But I was the one that brought it up."
            "So I have no choice but to push on."
            mike.say "I...I don't like you checking out other guys, Alexis."
            mike.say "It makes me feel nervous."
            show alexis angry
            $ alexis.love -= 2
            alexis.say "Geez, [hero.name] - I was just being honest."
            alexis.say "I'm not going to throw myself at them!"
            "Ah well - looks like I managed to make this awkward..."
    scene bg black with dissolve
    pause 1
    return

label alexis_halloween_dance:
    $ game.pass_time(2)
    scene bg livingroom
    show alexis halloween
    with dissolve
    alexis.say "Have we actually danced together since high-school?"
    alexis.say "Because I don't think we have!"
    alexis.say "Come to think of it, did we even dance back then?"
    mike.say "Well, we can do something about that tonight, Alexis."
    mike.say "If you'd do me the honour of joining me?"
    "Alexis smiles and lets me take her hand."
    hide alexis with dissolve
    "We hurry over to the makeshift dance-floor."
    show dance alexis halloween with dissolve
    "And soon enough we're moving in time to the music."
    "Well, at least I thought I was moving in time."
    alexis.say "Oh, god - now I remember why we never danced."
    alexis.say "Your moves suck, [hero.name]!"
    "I see Alexis glance over at Jack and Scottie."
    alexis.say "Now there's a couple of guys that can dance!"
    menu:
        "React meekly":
            hide dance
            show alexis halloween sad with fade
            mike.say "Hey, Alexis - stop looking at those other guys!"
            alexis.say "I...I was only..."
            mike.say "Never mind that."
            mike.say "You're my date, and I want your eyes on me."
            "Alexis looks at me oddly for a moment."
            "And I honestly think she's about to tell me off."
            show alexis normal
            $ alexis.sub += 2
            "But then her expression softens and she nods her head."
            alexis.say "Okay, [hero.name], okay."
            alexis.say "Point taken."
            hide alexis
            show dance alexis halloween
            with fade
            "What follows is a pretty memorable slow dance."
            "Alexis holds herself against me the whole time."
            "And she never takes her eyes away from mine."
            "Instead she stares deep into them from start to finish."
            "This means that I soon lose all track of time."
            "Instead all I can do is enjoy the experience."
            "And when you're dancing with a girl this special..."
            "Well, can you really blame me for getting a little jealous?"
            "Because I want her eyes on me every second we're together!"
        "React strongly":
            hide dance
            show alexis halloween confused with fade
            mike.say "Oh yeah, Alexis?"
            mike.say "Then why don't you go dance with them, huh?"
            "Alexis takes a step backwards from me."
            "Clearly she wasn't expecting my outburst."
            alexis.say "Hey, [hero.name]!"
            alexis.say "I was just saying..."
            "But I'm not in any mood for Alexis's excuses."
            mike.say "Save it, Alexis."
            mike.say "You've been eyeing up other guys all night."
            mike.say "And I'm starting to get tired of it."
            hide alexis with dissolve
            $ alexis.love -= 2
            "With that, I turn on my heel and walk away."
            "I can hear Alexis calling after me."
            "But I don't want to answer her."
            "I'm afraid that if I do, everyone at the party will hear me."
    scene bg black with dissolve
    pause 1
    return

label alexis_halloween_sex:
    if alexis.flags.story in [1, 3] and not game.flags.ryandead:
        scene bg livingroom with dissolve
        "The idea was to spend tonight with my date, but things just seem to keep popping up."
        "And I have to apologise to Alexis while I hurry off to take care of them as quickly as I can."
        "Fixing the music, refreshing the snacks and even dealing with trick or treaters."
        "Where are [bree.name] and Sasha while all of this is going on, huh?"
        "It's starting to feel like I'm running this party all on my own!"
        "Finally I get a chance to break off and hurry back to Alexis."
        "But I can't seem to find her anywhere."
        "And so I start to search the house for her in earnest."
        "There's no sign of her until I get to my own bedroom door."
        "So either she has to be in there or else she's gone home."
        "I don't even want to think about the latter possibility."
        "But the former would almost make up for her disappearing on me."
        "Maybe Alexis snuck up here to wait for me?"
        "Maybe she's in there right now, ready to have some fun?"
        "It's only as I put my hand on the door handle that I hear it."
        "The unmistakable sound of voices coming from inside the room."
        "Well, I say voices - but there are audible words in what I hear."
        "Slowly and with infinite care, I open the door just wide enough."
        "And then I peer inside to see what's going on in my bedroom."
        show alexis halloween ntr foursome with fade
        "The sight that greets me is hard to process at first."
        "All I can make out is a mass of limbs with perhaps four heads."
        "But it soon resolves itself into four human bodies."
        "Four human bodies that are intertwined on my bed!"
        "I recognise Alexis first, naked and in the middle of it all."
        "She's sitting atop a guy that can only be Jack."
        "And his cock is thrusting in and out of her ass."
        "Scottie stands over her, his groin between her spread legs."
        "His cock is deep inside of Alexis's pussy."
        "Last of all I see Ryan, kneeling on the bed beside her."
        "Alexis is licking at this last cock, taking it into her mouth."
        "For a moment I'm too stunned to even think."
        "All I can do is keep right on staring at the four-way orgy happening right in front of me."
        "But then it dawns on me that I have to do something, that I can't just let it happen."
        menu:
            "Watch":
                "Somehow I just can't find the courage to do anything other than watch."
                "And so that's exactly what I do, silently and without moving a muscle."
                "I keep on peeping through the gap in the door as they all fuck Alexis."
                "The sound of their grunting with effort fills my ears."
                "That and the way in which she moans and groans the whole time."
                "I don't know why I do it, why I don't burst in and stop it."
                "I should be mad at what she's doing right now."
                "With guys that I know, under my roof and on my own bed!"
                "But there's a weird fascination that takes hold as well."
                "I remember when Alexis cheated on me in the past."
                "And I always wondered what the actual act looked like."
                "So maybe that's why I can't keep from watching in silence now?"
                menu:
                    "Masturbate":
                        "I hardly notice that I've unzipped my pants and pulled out my cock."
                        "It's already rock-hard in my hand, and I start masturbating a second later."
                        "Now my own heavy breathing is added to the sounds reaching my ears."
                        "I swallow hard, and then keep on panting as I watch Alexis get fucked."
                        "Am I actually getting off on the way she's humiliating me?"
                        "I don't want to contemplate what that says about me."
                        "And so I push it out of my mind, concentrating on the here and now."
                        "Alexis is getting close to cumming now, I can see the tell-tale signs."
                        "Jack, Scottie and Ryan look like they're going to lose it too."
                        show alexis halloween ntr foursome cum ahegao
                        "I can't tell who goes off first, but the effect is spectacular."
                        "Alexis dances on two cocks while a third spatters cum on her face."
                        "I feel the warmth of my own cum between my fingers a moment later."
                        "Still panting and trying to shove my cock into my pants, I hurry off."
                        "The shame of what I just saw and my reaction are already starting to hit home."
                    "Just watch":
                        "Am I actually getting off on the way she's humiliating me?"
                        "I don't want to contemplate what that says about me."
                        "And so I push it out of my mind, concentrating on the here and now."
                        "Alexis is getting close to cumming now, I can see the tell-tale signs."
                        "Jack, Scottie and Ryan look like they're going to lose it too."
                        show alexis halloween ntr foursome cum ahegao
                        "I can't tell who goes off first, but the effect is spectacular."
                        "Alexis dances on two cocks while a third spatters cum on her face."
                        "I hurry off, the shame of the whole thing starting to dawn on me."
                $ game.pass_time(1)
            "Interfere":
                "There's just no way I can sit back and let this happen."
                "Alexis made a fool of me once before."
                "But I can't let her do the same thing to me again."
                "Before I can lose the courage to do what needs to be done, I make my move."
                scene bg bedroom1 with hpunch
                "Throwing the door open, I storm straight into my bedroom."
                mike.say "Alexis!"
                mike.say "Just what the FUCK are you doing?!?"
                show alexis naked surprised
                "Alexis tries to let out a shriek of surprise."
                "But it's stifled thanks to her having Ryan's cock jammed in her mouth."
                hide alexis
                show ryan halloween annoyed at mostleft4
                "He jumps backwards a second later, solving the problem at a stroke."
                "Scottie jumps out of his skin at the sound of my voice."
                show scottie halloween at right4
                "And he pulls his cock out of Alexis's pussy as he does so."
                "But it's Jack's efforts to see what's going on that seal her fate."
                show jack halloween normal at mostright4
                "When he tries to move, the motion sends Alexis tumbling off of him."
                "She lets out another shriek as she falls onto the mattress."
                "Then she bounces once before landing noisily on the floor."
                show alexis naked sad at left4
                alexis.say "Ouch!"
                alexis.say "Jeez, that really hurt!"
                mike.say "You really expect me to give a shit, Alexis?"
                mike.say "Then maybe you shouldn't have been fucking these guys!"
                show scottie angry
                scottie.say "Whoa, dude - wait a minute!"
                scottie.say "She told us you had, like an open relationship or something?"
                show scottie normal
                jack.say "Erm...yeah, [hero.name], that's right."
                jack.say "I'd never have gotten involved otherwise!"
                show ryan halloween smile
                ryan.say "Oops...this is a little awkward."
                ryan.say "Looks like they have one of those special kind of open relationships."
                ryan.say "The kind where the other one doesn't know about it!"
                "I round on Ryan suddenly, tired of his mocking."
                show ryan halloween annoyed
                mike.say "Fuck you, Ryan!"
                mike.say "Who even invited you anyway?"
                show ryan halloween smile
                ryan.say "Nobody did."
                ryan.say "I just dropped by on my way to meet Sam at another party, that's all!"
                "The casual way he talks about it makes me want to punch him in the face."
                "How can he just shrug off his infidelities like that?"
                "But then I shake off the anger I feel for Ryan."
                "Sure, he's a cheating piece of shit."
                "But Alexis is the one that really betrayed me."
                hide ryan
                hide scottie
                hide jack
                hide alexis
                show alexis naked sad
                with fade
                "All three of the other guys get dressed and hurry out."
                "Leaving me staring at Alexis."
                show alexis normal
                alexis.say "Aw, come on, [hero.name] - lighten up!"
                alexis.say "This is supposed to be a party and I was getting bored, that's all."
                show alexis confused
                mike.say "Yeah, well...you're not the only one that's getting bored, Alexis."
                mike.say "I'm getting pretty tired of putting up with your shit too!"
                "And with that, I turn my back on her and walk out of the room."
                $ alexis.love -= 20
                $ alexis.flags.story = 2
                $ DONE["alexis_ntr_conversation"] = game.days_played
    else:
        scene bg livingroom
        show alexis halloween
        with dissolve
        "It's getting pretty close to midnight by now, the party winding down as the night draws on."
        "Almost everyone is either tired, drunk or a mixture of both and wants to chill out."
        "In fact, that's exactly what I think Alexis has in mind when I see her slipping upstairs."
        "She pauses for a moment and beckons for me to follow her, a conspiratorial grin on her face."
        "Of course, I hurry to follow her up the stairs and onto the landing."
        "I'm not about to pass up the chance to do something fun with Alexis."
        "Or even better, the chance to make out with her where nobody can see!"
        scene bg secondfloor
        show alexis halloween
        with fade





        alexis.say "What are you waiting for, [hero.name]?"
        show alexis flirt
        alexis.say "Get your ass in here with me!"
        mike.say "Alexis - what are you doing?!?"
        alexis.say "What does it look like?"
        alexis.say "I'm luring you to your doom!"
        show alexis normal
        alexis.say "Doesn't that sound like fun?"
        hide alexis
        "I hurry over to the bedroom door, shaking my head."
        "All I can think of is what happens if someone sees her."
        mike.say "You have to get out of there, Alexis!"
        mike.say "I've got a house full of people..."
        scene bg bedroom2
        show alexis halloween
        with fade
        "Alexis cuts me off by grabbing me and pulling me into the room."
        "I really should have known better than to get so close."
        "Alexis is drunk and dead-set on having a good time."
        "What else was she going to do?"
        "I stagger into the bedroom, almost losing my balance."
        "And while I'm regaining it, Alexis is already going to work."
        "She has most of my costume off before I know it."
        show alexis kiss halloween with fade
        $ alexis.flags.kiss += 1
        "Her lips are pressed against mine the whole time."
        "And then I feel her hand grab hold of my cock too."
        "That's what decides it for me, what changes my mind."
        "We're well and truly doing this thing now."
        "And if we do get caught, there's only two explanations."
        "One is that I stumbled in with my clothes on and thrashed around like a clown."
        "Or the other is that I agreed to come out here and fuck Alexis in [bree.name]'s bedroom."
        "I don't know about you, but I prefer the latter option!"
        show alexis cowgirl halloween hard with fade
        "Without hesitation, I pull Alexis onto the bed atop me."




        "It only takes a couple of seconds for me to find what I'm looking for."
        show alexis cowgirl vaginal
        "And when I do, I push my now hard cock straight into it."
        alexis.say "Oh..."
        alexis.say "Oh yeah..."
        alexis.say "That's what I need!"
        "Alexis sinks slowly down and onto my cock."
        "Her expression melts into one of sheer pleasure."
        "And I feel her surrender to me in that moment too."
        "I take it slow, thrusting in and out with care."
        "All the time I savour the feeling, and the sight of Alexis too."
        "She sits on top of me, almost helpless as I fuck her."
        "Her eyes are half closed and her mouth hangs open."
        "The motion of my cock is making her breasts sway in sympathy."
        "And I can't keep from reaching out to caress them."
        alexis.say "Mmm..."
        alexis.say "That feels good..."
        alexis.say "Play with me more..."
        "I do as she asks, squeezing and pinching."
        "Alexis moans as I tease her nipples."
        "And I feel her pussy quiver as I push her breasts together."
        "By now I'm past caring if someone sees what we're doing."
        "All I can think about is watching Alexis ride my cock."
        "And she seems to be in another world entirely."
        "In fact, I think I'm the only thing keeping her upright!"
        show alexis cowgirl creampie ahegao with vpunch
        "So when I feel myself cumming, I make sure to hold her tight."
        with vpunch
        "Alexis's eyes almost roll into her head when it happens."
        with vpunch
        "And she suddenly clings to me as I lose it inside of her."
        show alexis cowgirl -vaginal limp -creampie drip
        show pussy_insert alexis cum zorder 1 at zoomAt(0.75, (40, 200))
        "Her head is on my shoulder, and she's panting into my ear."
        "Tangled into a knot of limbs, we float together on [bree.name]'s bed."
        hide pussy_insert
        $ alexis.sexperience += 1
        $ game.pass_time(1)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
