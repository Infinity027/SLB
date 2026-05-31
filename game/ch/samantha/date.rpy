label samantha_date_intro_valentine_male:
    if samantha.flags.nickname == "cupcake":
        mike.say "Happy Valentine's day, Cupcake."
    else:
        mike.say "Happy Valentine's day, Sam."
    mike.say "You don't know how much this means to me."
    mike.say "To finally be able to call you my valentine!"
    "Sam smiles and shakes her head."
    samantha.say "Oh, I think I can imagine, [hero.name]."
    samantha.say "It probably means as much as knowing you're mine means to me!"
    return

label samantha_date_intro_halloween_male:
    if samantha.flags.nickname == "cupcake":
        mike.say "Hey, Cupcake, looking good tonight!"
    else:
        mike.say "Hey, Sam, looking good tonight!"
    "Sam giggles and gives me one of her trademark smiles."
    samantha.say "Thanks, [hero.name]."
    samantha.say "But, no costume tonight?"
    samantha.say "After all, it is Halloween."
    "I slap my forehead and groan."
    mike.say "Oh man, I totally forgot!"
    samantha.say "Don't worry about it, [hero.name]."
    samantha.say "We can still have a great time on our date."
    return

label samantha_date_intro_christmas_male:
    samantha.say "Happy Christmas, [hero.name]!"
    samantha.say "I'm really looking forward to this - a Christmas together."
    samantha.say "Just you and me!"
    "My heart leaps at the way Sam says those words."
    if samantha.flags.nickname == "cupcake":
        mike.say "Me too, Cupcake, me too."
    else:
        mike.say "Me too, Sam, me too."
    mike.say "I can't imagine anyone else I'd rather spend it with!"
    return

label samantha_date_intro_birthday_male:
    if samantha.flags.nickname == "cupcake":
        mike.say "Happy birthday, Cupcake!"
    else:
        mike.say "Happy birthday, Sam!"
    mike.say "And to celebrate, I'm going to make our date extra special too!"
    samantha.say "Oh, [hero.name]!"
    samantha.say "You remembered my birthday?"
    samantha.say "You never did that before now."
    if samantha.flags.nickname == "cupcake":
        mike.say "Well, Cupcake...we weren't dating back then!"
    else:
        mike.say "Well, Sam...we weren't dating back then!"
    mike.say "And now you're always on my mind..."
    return

label samantha_date_intro_mc_birthday_male:
    samantha.say "Happy birthday, [hero.name]!"
    if samantha.flags.nickname == "cupcake":
        mike.say "Wow, Cupcake - you remembered my birthday?"
    else:
        mike.say "Wow, Sam - you remembered my birthday?"
    samantha.say "You sound like you're surprised!"
    samantha.say "Didn't I always remember it before we started dating?"
    mike.say "Yeah, I guess so..."
    mike.say "But it just seems to mean more now, you know?"
    samantha.say "Oh, [hero.name]!"
    samantha.say "Let's just get on with our date and have a good time, okay?"
    return

label samantha_date_eat_a_burger:
    "Sam must have been pretty hungry, as she seems glad to see her burger arrive."
    "Without waiting for an invitation, she begins to devour it immediately."
    "And the appreciative sounds she makes at the same time certainly make me feel oddly hungry too."
    return

label samantha_date_buy_drink:
    if samantha.is_visibly_pregnant:
        show samantha angry
        $ samantha.love -= 10
        samantha.say "Grow up, [hero.name]!"
        samantha.say "I'm pregnant, remember?"
        if not samantha.flags.NPCpregnancy:
            samantha.say "Something you had a hand in too, I seem to recall!"
        $ hero.cancel_activity()
        hide samantha
    else:
        "Sam sips her drink through a straw, visibly savouring it as she does so."
        "Somehow she manages to make sucking up alcohol like that look very, very good."
        "Even when she gets to the bottom of the glass and makes sucking noises among the ice-cubes."
    return

label samantha_date_play_darts:
    "Almost as soon as we start playing darts, Sam undergoes a pretty scary transformation."
    "Gone is the sweet, charming girl that I know, replaced with an angry, highly competitive harpy."
    "She swears loudly when she misses her intended target and yells at me for cheating when I hit mine!"
    return

label samantha_date_pub_play_pool:
    "Sam agrees to a game of pool, but I can tell instantly that it's not her game."
    "She spends the entire time standing by the table, a passive smile fixed upon her face."
    "Win or lose, it seems to make no difference to her."
    return

label samantha_date_buy_a_round:
    if samantha.is_visibly_pregnant:
        show samantha angry
        $ samantha.love -= 10
        samantha.say "Grow up, [hero.name]!"
        samantha.say "I'm pregnant, remember?"
        if not samantha.flags.NPCpregnancy:
            samantha.say "Something you had a hand in too, I seem to recall!"
        $ hero.cancel_activity()
    elif (hero.charm >= 60 - samantha.love and samantha.flags.drinks < 2):
        show drink samantha
        "Sam just nods and smiles when I say that the next round's on me."
        "I guess she's not that bothered about downing another drink."
        "Or maybe she thinks that's what a guy's supposed to do on a date?"
        $ game.active_date.score += 5
        if "rebel" in samantha.traits:
            $ game.active_date.score += 5
        $ samantha.set_flag("drinks", 1, "day", mod="+")
        hide drink
    else:
        "I want to pay a round of beers to the whole pub."
        "But Samantha doesn't seem to want to drink, so I refrain from doing so."
        $ hero.cancel_activity()
    return

label samantha_dance_with:
    "Sam leads me onto the dance-floor and wraps her arms around me in a traditional manner."
    "The dance is slow and almost sedate in nature, never picking up pace or getting any more intense."
    "But yet I still spend the whole time looking into her eyes, entranced by their depth and beauty."
    return

label samantha_date_play_arcade_intro_male:
    samantha.say "Are you sure about this, [hero.name]?"
    samantha.say "There are a lot of kids in here."
    samantha.say "Don't you want to do something a bit more adult?"
    "I can't help shaking my head and smiling at Sam."
    "I guess she's just not used to visiting an arcade."
    "So she's not tuned into the magic of the place."
    if samantha.flags.nickname == "cupcake":
        mike.say "That's just because videogames are so magical, Cupcake."
    else:
        mike.say "That's just because videogames are so magical, Sam."
    mike.say "People of all ages love them!"
    "Sam doesn't even dignify that with a response."
    "Instead she just smirks and looks at me sideways."
    "And it's that look which spurs me into action."
    "Because it's a challenge for me to prove myself."
    if samantha.flags.nickname == "cupcake":
        mike.say "It's true, Cupcake!"
    else:
        mike.say "It's true, Sam!"
    mike.say "There's a videogame for everyone."
    mike.say "Like...what about this one?"
    "I lead Sam over to a vintage arcade cabinet."
    samantha.say "What's this, [hero.name]?"
    samantha.say "'Barmaid Blues'?"
    if samantha.flags.nickname == "cupcake":
        mike.say "Yeah, Cupcake - it's a classic!"
    else:
        mike.say "Yeah, Sam - it's a classic!"
    mike.say "You have to serve all the customers beer as fast as you can."
    mike.say "I mean, you like going to the pub, right?"
    "Sam still looks less than convinced, but she nods all the same."
    "Which I take as permission to start pumping coins into the slot."
    return

label samantha_date_play_arcade_win_male:
    "It's an old game, and one that I've played a lot in the past."
    "Which means that I don't have any trouble racking up a high score."
    "But the same doesn't seem to be true for Sam."
    samantha.say "Whoa..."
    samantha.say "This game is so fast!"
    samantha.say "I...I can't keep up!"
    if samantha.flags.nickname == "cupcake":
        mike.say "It's all about the rhythm, Cupcake."
    else:
        mike.say "It's all about the rhythm, Sam."
    mike.say "If you can get that, you're laughing."
    "I don't know if Sam even hears my advice."
    "Because nothing seems to change as we keep on playing."
    "She curses under her breath as she falls behind me."
    "And by the time we've used up our credits, it's too late."
    samantha.say "I...I don't think this is it, [hero.name]."
    samantha.say "I don't think this is the game for me!"
    if samantha.flags.nickname == "cupcake":
        mike.say "Ah, yeah, Cupcake..."
    else:
        mike.say "Ah, yeah, Sam..."
    mike.say "Maybe we should try another game?"
    "Sam's eyes go wide at my suggestion."
    "And she shakes her head vigorously."
    samantha.say "No, [hero.name], I don't."
    samantha.say "I think we should go to a real bar."
    samantha.say "And that we should down some real beers!"
    return

label samantha_date_play_arcade_lose_male:
    "It's an old game, and one that's pretty simple to master."
    "Which means I was right to pick it for Sam, as she does just that."
    "But it sucks to be right when it means I end up getting my ass kicked!"
    samantha.say "Ha..."
    samantha.say "I don't believe it, [hero.name]!"
    samantha.say "This really is fun!"
    if samantha.flags.nickname == "cupcake":
        mike.say "What did I tell you, Cupcake!"
    else:
        mike.say "What did I tell you, Sam!"
    mike.say "I knew you'd like it if you gave it a chance."
    mike.say "But maybe let me win a little, yeah?"
    "I don't know if Sam hears my desperate plea."
    "Because nothing seems to change as we keep on playing."
    "I keep on cursing under my breath as I fall behind."
    "And by the time we've used up our credits, it's too late."
    samantha.say "Wow..."
    samantha.say "This is it, [hero.name]."
    samantha.say "This is the game for me!"
    if samantha.flags.nickname == "cupcake":
        mike.say "Ah, yeah, Cupcake..."
    else:
        mike.say "Ah, yeah, Sam..."
    mike.say "Maybe we should try another game?"
    "Sam's eyes go wide at my suggestion."
    "And she shakes her head vigorously."
    samantha.say "No, [hero.name], I want to play this one again."
    if samantha.flags.nickname == "cupcake":
        mike.say "I don't think I can take it anymore, Cupcake!"
    else:
        mike.say "I don't think I can take it anymore, Sam!"
    mike.say "I think we should go to a real bar."
    mike.say "And that we should down some real beers!"
    return

label samantha_dick_reactions:
    if not samantha.flags.seendick:
        $ samantha.flags.seendick = 1
        if hero.has_skill("hung"):
            show dick reactions samantha smile
            samantha.say "Oh geez..."
            samantha.say "Was this ever worth waiting for!"
            mike.say "Y...you're serious?!?"
            samantha.say "Oh yeah - I always knew you'd be hung like this."
            show dick reactions samantha tasty
            samantha.say "I always wondered what one this big would taste like!"
            $ samantha.sub += 10
            $ samantha.love += 10
        elif hero.has_skill("smalldick"):
            show dick reactions samantha mock
            samantha.say "Oh...oh well..."
            if samantha.flags.nickname == "cupcake":
                mike.say "Wha...what's the matter, Cupcake?"
            else:
                mike.say "Wha...what's the matter, Sam?"
            mike.say "It's because it's so small, isn't it?"
            show dick reactions samantha smile
            samantha.say "Oh, [hero.name] - it's still bigger than Ryan's!"
            mike.say "Okay...maybe that's not so bad!"
            $ samantha.sub -= 10
            $ samantha.love -= 10
        hide dick reactions
    return

label samantha_peeping_scene_male:
    "Normally I'd just hear the sound of water running in the bathroom and walk straight by the door."
    "I mean, there's nothing unusual about hearing one of your housemates taking a shower, is there?"
    "And even when you're the only guy in the house, you kind of get used to the idea it's a girl in there."
    "Yeah, of course I'm being serious - you think I go around thinking perverted thoughts my every waking moment?"
    "In fact, don't answer that."
    "I don't think I'd like the answer..."
    "No, what makes me stop and take a second look this time is the fact that the bathroom door's open."
    "Not wide open, but left ajar, open just enough to see in through the crack."
    "I turn my head this way and that, checking that there's nobody else around."
    "And then I sneak over, keeping as quiet as I can the whole time."
    "Maybe someone left the shower running and forgot about it?"
    "Or maybe they forgot to close the door behind them?"
    "Either way, I really should check it out."
    "And if I see anything that I shouldn't..."
    "Well, it'd be a total accident - not me peeping on my housemates at all!"
    "Reaching the door to the bathroom, I lean in close to get a better look."
    "There's a lot of steam coming from the shower cubicle."
    "But all the same, I can make out an unmistakably feminine shape in there!"
    "The moment that I lay eyes on this, I'm hooked and I can't look away."
    "As the steam clears a little, I can make out the finer details too."
    "It's Sam!"
    "That's who I can see in there."
    "That's who those amazing curves belong to!"
    return

label samantha_peeping_reactions_male:
    if (samantha.love >= 150 or samantha.sub >= 50) and samantha.sexperience:
        show samantha naked
        "And it's all but confirmed when she turns her head in my direction."
        "But it takes me a moment longer to realise that she's looking straight at me!"
        show samantha happy
        samantha.say "Hey, [hero.name]..."
        samantha.say "I know you're there!"
        samantha.say "And I know that you're watching me..."
        "I open my mouth to protest."
        "But the words die in my throat."
        "What kind of a moron denies he's there by speaking up!"
        "There's that, but there's also the way Sam's looking right now."
        "It's almost like she's not mad that I'm here!"
        "Before now, Sam seemed to have just been washing herself."
        "You know - doing all the stuff you do in the shower?"
        "But now I see her begin to slow down and even show off."
        "She traces the lines of her body with both hands."
        "Lingering on her breasts, belly and then her ass."
        "All the time she's breathing heavily too."
        "In fact it's more than that - she's actually moaning!"
        "I watch, transfixed as Sam caresses herself from head to toe."
        "My eyes follow the progression of her hands the whole time."
        "And I can feel my cock getting stiffer with each second that passes."
        show samantha close
        "Finally, Sam looks up and fixes me with her gaze."
        $ samantha.love += 1
        $ samantha.sub += 1
        samantha.say "Mmm..."
        samantha.say "I bet you're good and hard by now."
        samantha.say "Huh, [hero.name]?"
        "I stand up and almost stumble backwards."
        "Afraid of being caught with my cock in my hand, I scurry off to my bedroom."
        "And I do so with the sound of Sam's laughter ringing in my ears too!"
    else:
        show samantha naked angry
        samantha.say "Hey!"
        samantha.say "Who's there?"
        samantha.say "[hero.name], is that you?!?"
        "I could make a run for it."
        "But that'd involve making some serious noise."
        "And Sam could get to the bathroom door before I could reach my bedroom."
        "Maybe I can talk my way out of this instead?"
        if samantha.flags.nickname == "cupcake":
            mike.say "Ah...hey, Cupcake."
        else:
            mike.say "Ah...hey, Sam."
        mike.say "This isn't what it looks like!"
        show samantha close
        $ samantha.love -= 20
        $ samantha.sub -= 10
        samantha.say "Urgh!"
        samantha.say "I knew I should have checked the damn door!"
        samantha.say "You guys - you're all the same."
        "I can hear the disappointment in Sam's voice."
        "Sure, it's under a layer of anger."
        "But it's still there, and it makes me feel ashamed of myself."
        samantha.say "Just you wait until I get out of here, [hero.name]."
        samantha.say "Then we're going to have a little chat about boundaries!"
        "I take that as my being dismissed and creep away to my room."
        "Which is appropriate, as I feel like a real creep right now too."
    return

label samantha_halloween_invitation:
    show samantha
    "It's not hard for me to decide who I want to invite to the Halloween party as my date."
    "Sam's name springs instantly to mind, and I spring the question the first chance I get."
    "I don't even consider the fact that she might not be into the idea or already have plans."
    "I just come straight out with it..."
    if samantha.flags.nickname == "cupcake":
        mike.say "Hey, Cupcake..."
    else:
        mike.say "Hey, Sam..."
    mike.say "Are you free on Halloween?"
    "Sam shakes her head."
    samantha.say "Ah...yeah, I think so."
    samantha.say "Why do you ask?"
    mike.say "We're having a Halloween party at my place."
    mike.say "Well...what used to be your place too!"
    show samantha surprised
    "I see the light of recognition in Sam's eyes."
    "She nods, and at first I think she's saying yes to the invite."
    samantha.say "Wow, that takes me back."
    show samantha happy
    samantha.say "You remember the parties we always used to have there?"
    samantha.say "There was that year Ryan pranked you with a monster mask."
    samantha.say "We honestly thought you'd pissed your..."
    "I wave my hands in the air, trying to cut Sam off before she can say anymore."
    "There are some memories that I don't need to be reminded of - and I mean ever!"
    mike.say "Anyway..."
    show samantha normal
    mike.say "And I wondered if you wanted to come along?"
    mike.say "You know...kind of as my date?"
    if samantha.love >= 100 and samantha.flags.engaged:
        show samantha happy
        "Sam nods her head happily at the invitation."
        "And I can feel my heart leap in my chest."
        samantha.say "Okay, [hero.name], that sounds great."
        samantha.say "Ryan and I could really use a night out!"
        "And just like that, my heart sinks again."
        "Did Sam not hear me ask her to be my date?"
        mike.say "Ah..."
        mike.say "You AND Ryan?"
        show samantha normal
        samantha.say "Well, I just kind of assumed..."
        samantha.say "We all used to live here together."
        show samantha sad
        samantha.say "Is...is there a problem with him coming?"
        mike.say "NO...no..."
        if samantha.flags.nickname == "cupcake":
            mike.say "Of course not, Cupcake."
        else:
            mike.say "Of course not, Sam."
        mike.say "You should totally bring Ryan along."
        mike.say "It'll be like old times!"
        show samantha normal
        "Sam doesn't seem to notice the look of disappointment on my face."
        "Instead she's already getting wrapped up in the possibilities."
        samantha.say "I'm guessing it's a costume party, right?"
        show samantha happy
        samantha.say "That means Ryan and I are going to have to think of what to wear!"
        "Yay...I can't wait to see what he comes up with."
        "Somebody kill me now, and spare me this torture!"
        $ game.flags.halloween_girl = "samantha"
    elif samantha.love >= 100 or Harem.together(bree, sasha, samantha, name='home'):
        "Sam cocks her head on one side, weighing up the offer."
        "And then she nods, making my heart leap inside of my chest."
        samantha.say "You know what, that sounds like fun."
        show samantha happy
        $ samantha.love += 1
        samantha.say "Okay, [hero.name], I'll come along."
        if samantha.flags.nickname == "cupcake":
            mike.say "That's great, Cupcake."
        else:
            mike.say "That's great, Sam."
        mike.say "You're going to have a hell of a time - I promise!"
        show samantha normal
        samantha.say "I'm sure I will, [hero.name]."
        samantha.say "In fact, it'll be nice to party at the house again."
        if samantha.flags.divorced:
            show samantha happy
            samantha.say "But without a certain someone there - if you know what I mean?"
            "I nod eagerly and give Sam a smile of my own."
            "We both know that she's talking about Ryan."
            "So there's no need to say his name again."
        mike.say "Oh, and before I forget..."
        mike.say "It's a costume party too."
        mike.say "So you might want to think about what you're going to come as."
        show samantha normal
        samantha.say "Don't worry, [hero.name], I have some ideas already."
        show samantha blush
        samantha.say "And I promise you won't be disappointed!"
        "The grin on my face must be a foot wide by now."
        "But how am I supposed to hide my enthusiasm for something like that?"
        $ game.flags.halloween_girl = "samantha"
    else:
        show samantha sad
        "Sam shakes her head almost as soon as I've said my piece."
        "And I know that she's about to let me down."
        samantha.say "I'd have been up for a Halloween party, [hero.name]."
        samantha.say "But I already made plans."
        samantha.say "And I can't cancel at such short notice."
        if samantha.flags.nickname == "cupcake":
            mike.say "Aw, that sucks, Cupcake."
        else:
            mike.say "Aw, that sucks, Sam."
        mike.say "Are you sure there's no way you could?"
        "Sam looks pained, but she shakes her head again."
        samantha.say "Any other time and I would have, [hero.name]."
        samantha.say "I just can't cancel what I have on that night."
        samantha.say "I'm sorry!"
        if samantha.flags.nickname == "cupcake":
            mike.say "It's okay, Cupcake."
        else:
            mike.say "It's okay, Sam."
        mike.say "I understand."
        show samantha normal
        "Sam gives me a helpless smile."
        samantha.say "I really am Sorry, [hero.name]."
        samantha.say "I'll make it up to you, I promise."
        "I nod, wondering just what she means by that."
    return

label samantha_halloween_arrival:
    scene bg house with wiperight
    if samantha.flags.engaged and not game.flags.ryandead:
        "Opening the door, I guess I should have been more cautious."
        "Especially after the incidents with Jack's sword and Scottie's trident."
        show ryan halloween smile at right5
        show samantha halloween at left5
        with dissolve
        "But I get caught out again as someone jumps out in front of me."
        mike.say "Aargh!"
        mike.say "What the hell?!?"
        ryan.say "It's just your friendly neighbourhood spidermen!"
        show samantha annoyed
        samantha.say "Ah..."
        show samantha normal
        samantha.say "Shouldn't that be spiderpeople, Ryan?"
        "It's only now that I can make sense of it all."
        "I see two figures clad in skin-tight Lycra jumpsuits."
        "One's obviously male, dressed as Spiderdude."
        "The other is equally clear as being female and Spider Cutey."
        "Both pull of their hoods a second apart."
        "Which reveals them to be Ryan and Gwen, respectively."
        show ryan halloween annoyed
        ryan.say "What was that, dear?"
        show ryan halloween smile
        ryan.say "Never mind, anyway."
        ryan.say "[hero.name] finally answered the door!"
        mike.say "Erm..."
        if samantha.flags.nickname == "cupcake":
            mike.say "Hey, Ryan...Cupcake."
        else:
            mike.say "Hey, Ryan...Sam."
        ryan.say "What do you think, [hero.name]?"
        ryan.say "Sam told me she was coming as SpiderMILF."
        ryan.say "So I came as Spiderdude to match!"
        menu:
            "Compliment him":
                "Urgh..."
                "He hasn't got a clue!"
                "Sam's dressed as Spider Cutey, not SpiderMILF."
                "And she's from an alternate Earth."
                "One where Peter Poker became the Chameleon, not Spiderdude!"
                "But I'd better humour him, for Sam's sake."
                mike.say "Yeah, Ryan."
                mike.say "That's great!"
                ryan.say "Now, where are these new room-mates of yours?"
                ryan.say "I'm dying to meet them!"
                hide ryan
                show samantha halloween annoyed
                with dissolve
                "Ryan shoulders his way past me and into the house."
                "But Sam holds back a moment, a pained look on her face."
                samantha.say "Thanks for that, [hero.name]."
                samantha.say "I told him all of that, because I remembered you telling me."
                samantha.say "But I don't think he heard a word of it."
                hide samantha with dissolve
                "Wait a minute - did she actually just say that?"
                "Sam remembers something that random about me?"
                "That has to be a good thing - doesn't it?"
                $ samantha.love += 5
            "Criticize him":
                "Urgh..."
                "I haven't missed Ryan being a prick since he and Sam moved out."
                "And I'm not in the mood to let him pick up where he left off, either."
                mike.say "She's actually Spider Cutey, Ryan."
                mike.say "Not SpiderMILF."
                show ryan halloween annoyed
                ryan.say "Well, I..."
                mike.say "And Spider Cutey comes from an alternate Earth."
                mike.say "One where there was no Spiderdude, and Peter Poker was the Chameleon."
                mike.say "So no, you don't actually match."
                "Ryan snorts at this, shaking his head."
                ryan.say "Whatever, [hero.name]."
                ryan.say "I see you're still a massive nerd!"
                show ryan halloween smile
                ryan.say "Now, where are these new room-mates of yours?"
                ryan.say "I'm dying to meet them!"
                hide ryan
                show samantha halloween annoyed
                with dissolve
                "Ryan shoulders his way past me and into the house."
                "But Sam holds back a moment, a pained look on her face."
                samantha.say "Might have been better to humour him, [hero.name]."
                samantha.say "He's in one of his arrogant moods tonight!"
                $ samantha.sub += 5
    elif Harem.together(bree, sasha, samantha, name='home'):
        "I stare at the door for a moment longer, and then I strike myself on the forehead."
        "Of course, Sam lives here too."
        "So my date's already in the house!"
        "Geez, I must have scrambled my brain putting so much effort into the party."
        scene bg livingroom
        show samantha halloween
        with fade
        "But the same can't be said for Sam, as she looks at me expectantly."
        samantha.say "Well, [hero.name], I'm waiting."
        samantha.say "What do you think of my costume?"
        "I look Samantha up and down one last time."
        "And then I take a deep breath."
        "All in preparation to tell her exactly what I think."
        menu:
            "Compliment":
                if samantha.flags.nickname == "cupcake":
                    mike.say "It's great, Cupcake."
                else:
                    mike.say "It's great, Sam."
                mike.say "Kind of like a dream come true."
                show samantha happy
                $ samantha.love += 1
                "Sam's cheeks flush at the compliment."
                "But she looks a little confused too."
                samantha.say "Thanks, [hero.name]."
                show samantha normal
                show fx question
                samantha.say "A dream come true?"
                "Now I'm the one starting to blush."
                mike.say "Well, back when you were with Ryan..."
                mike.say "I used to imagine what it'd be like to be with you."
                mike.say "So it is like that, you see?"
                show samantha happy
                "Sam smiles at this."
                samantha.say "Oh, [hero.name]."
                samantha.say "That's kind of sweet."
                show samantha normal
                samantha.say "I mean, it's needy and sad too."
                show samantha happy
                samantha.say "But still sweet!"
            "Criticise":
                if samantha.flags.nickname == "cupcake":
                    mike.say "It's great, Cupcake."
                else:
                    mike.say "It's great, Sam."
                mike.say "But did you have to wear something so..."
                mike.say "Well, so tight?"
                show samantha annoyed
                $ samantha.love -= 2
                if hero.charm >= samantha.sub and hero.knowledge >= samantha.sub:
                    $ samantha.sub -= 5
                "Sam shoots me a puzzled look."
                "And she crosses her arms over her chest."
                samantha.say "Hey!"
                samantha.say "Since when have you been such a prude?"
                samantha.say "You never objected when I dressed like this in the past?"
                "There's no real way get around it."
                "And so I decide to just come out and say it."
                if samantha.flags.nickname == "cupcake":
                    mike.say "I...I guess I'm just jealous, Cupcake."
                else:
                    mike.say "I...I guess I'm just jealous, Sam."
                samantha.say "You're jealous?"
                samantha.say "Of what, exactly?"
                if samantha.flags.nickname == "cupcake":
                    mike.say "Of other guys looking at you, Cupcake."
                else:
                    mike.say "Of other guys looking at you, Sam."
                mike.say "Of them trying to take you away from me."
                show samantha normal
                $ samantha.love += 1
                "Sam rolls her eyes at this."
                samantha.say "Oh, [hero.name]."
                samantha.say "That's kind of sweet."
                samantha.say "I mean, it's needy and sad too."
                samantha.say "But still sweet!"
                samantha.say "Trust me, you've got nothing to worry about!"
                "I nod, trying to find reassurance in her promise."
    else:
        "Opening the door, I guess I should have been more cautious."
        "Especially after the incidents with Jack's sword and Scottie's trident."
        show samantha halloween with dissolve
        "But I get caught out again as I see a figure in a full bodysuit."
        mike.say "Whoa!"
        show samantha happy
        samantha.say "Just me - your friendly neighbourhood Spider Cutey!"
        "With that, the figure pulls back its hood to reveal Sam's face."
        "It takes me a moment to realise what I'm seeing."
        "Sam, covered from head to toe in skin-tight spandex."
        "The sight is enough to leave me stunned and speechless."
        show samantha normal
        samantha.say "Well, [hero.name], I'm waiting."
        samantha.say "What do you think of my costume?"
        "I look Samantha up and down one last time."
        "And then I take a deep breath."
        "All in preparation to tell her exactly what I think."
        menu:
            "Compliment":
                if samantha.flags.nickname == "cupcake":
                    mike.say "It's great, Cupcake."
                else:
                    mike.say "It's great, Sam."
                mike.say "Kind of like a dream come true."
                show samantha happy
                $ samantha.love += 1
                "Sam's cheeks flush at the compliment."
                "But she looks a little confused too."
                samantha.say "Thanks, [hero.name]."
                show samantha normal
                show fx question
                samantha.say "A dream come true?"
                "Now I'm the one starting to blush."
                mike.say "Well, back when you were with Ryan..."
                mike.say "I used to imagine what it'd be like to be with you."
                mike.say "So it is like that, you see?"
                show samantha happy
                "Sam smiles at this."
                samantha.say "Oh, [hero.name]."
                samantha.say "That's kind of sweet."
                show samantha normal
                samantha.say "I mean, it's needy and sad too."
                show samantha happy
                samantha.say "But still sweet!"
            "Criticise":
                if samantha.flags.nickname == "cupcake":
                    mike.say "It's great, Cupcake."
                else:
                    mike.say "It's great, Sam."
                mike.say "But did you have to wear something so..."
                mike.say "Well, so tight?"
                show samantha annoyed
                $ samantha.love -= 2
                if hero.charm >= samantha.sub and hero.knowledge >= samantha.sub:
                    $ samantha.sub -= 5
                "Sam shoots me a puzzled look."
                "And she crosses her arms over her chest."
                samantha.say "Hey!"
                samantha.say "Since when have you been such a prude?"
                samantha.say "You never objected when I dressed like this in the past?"
                "There's no real way get around it."
                "And so I decide to just come out and say it."
                if samantha.flags.nickname == "cupcake":
                    mike.say "I...I guess I'm just jealous, Cupcake."
                else:
                    mike.say "I...I guess I'm just jealous, Sam."
                samantha.say "You're jealous?"
                samantha.say "Of what, exactly?"
                if samantha.flags.nickname == "cupcake":
                    mike.say "Of other guys looking at you, Cupcake."
                else:
                    mike.say "Of other guys looking at you, Sam."
                mike.say "Of them trying to take you away from me."
                show samantha normal
                $ samantha.love += 1
                "Sam rolls her eyes at this."
                samantha.say "Oh, [hero.name]."
                samantha.say "That's kind of sweet."
                samantha.say "I mean, it's needy and sad too."
                samantha.say "But still sweet!"
                samantha.say "Trust me, you've got nothing to worry about!"
                "I nod, trying to find reassurance in her promise."
    scene bg black with dissolve
    pause 1
    return

label samantha_halloween_party:
    $ game.pass_time(2)
    if samantha.flags.engaged:
        scene bg livingroom
        show ryan halloween smile at left5
        show samantha halloween at right5
        with fade
        ryan.say "Wow!"
        ryan.say "You made some improvements since we moved out!"
        "I follow Ryan's gaze and see where he's looking."
        "And I'm shocked to see that it's straight at [bree.name] and Sasha!"
        "He's checking them out as though nobody knows what he's doing."
        "I glance quickly at Sam, worried at how she might react."
        "But she doesn't seem to have noticed."
        "Either that or she's deliberately ignoring him."
        ryan.say "You know what I mean, [hero.name]?"
        menu:
            "Disagree":
                mike.say "I don't know, Ryan."
                mike.say "I liked some of the original features."
                show samantha surprised
                "I make a point of looking Sam in the eye as I say this."
                show samantha normal
                $ samantha.love += 2
                "And she seems to get the point that I'm trying to make."
                "Sam flashes me a smile that Ryan doesn't seem to notice."
                show ryan halloween annoyed
                ryan.say "Nah, I disagree."
                ryan.say "You can't live in the past."
                "I shake my head."
                mike.say "Maybe so."
                mike.say "But you have to remember it."
                mike.say "Or else you might forget what made it special."
                "Sam looks away as I say this, blushing a little."
                "She has to know that I'm talking about her, right?"
            "Agree":
                mike.say "Yeah, I know what you mean, Ryan."
                mike.say "There are some definite perks to living here!"
                show samantha surprised
                "Sam catches my eye as I say this."
                show samantha annoyed
                $ samantha.love -= 2
                "And I can see a look of disappointment in them."
                "Damn it - I don't want to exchange banter with Ryan."
                "But what else am I supposed to do?"
                "I can't slap the taste out of his mouth, can I?!?"
                ryan.say "I agree, [hero.name]."
                ryan.say "You can't live in the past."
                "Sam looks away as I say this, shaking her head."
                "She has to know that I'm just humouring him, right?"
    else:
        scene bg livingroom
        show samantha halloween
        with fade
        samantha.say "Wow..."
        samantha.say "This place brings back so many memories!"
        "Sam seems to be in a world of her own as the party goes on around her."
        "All she talks about is what we used to get up to when she lived here the last time."
        "And unfortunately for me, that involves Ryan's name being mentioned a lot."
        show samantha sad
        samantha.say "Are..."
        samantha.say "Are you okay, [hero.name]?"
        samantha.say "You've been quiet since I got here!"
        "I take a deep breath and prepare to answer."
        menu:
            "Compliment":
                mike.say "Maybe we should stop talking about the past?"
                mike.say "And try to work on making some new memories, huh?"
                "Sam looks at me in silence for a moment."
                "And I think she's going to tell me off."
                show samantha normal
                $ samantha.love += 2
                "But then I see her nod and smile."
                samantha.say "You're right."
                samantha.say "No more living in the past."
                show samantha happy
                samantha.say "We should be enjoying ourselves right now!"
                "Sam takes hold of my hand and looks me straight in the eye."
                "For the first time tonight I feel like I'm the centre of her attention."
                "And the sensation is enough to lift my mood and make me smile again."
            "Complain":
                if samantha.flags.nickname == "cupcake":
                    mike.say "I kind of feel a bit left out, Cupcake."
                else:
                    mike.say "I kind of feel a bit left out, Sam."
                mike.say "You're supposed to be my date tonight."
                mike.say "But all you've done is talk about Ryan!"
                show samantha surprised
                "Sam looks at me in surprise."
                show samantha annoyed
                $ samantha.love -= 2
                "But then she shrugs it off, becoming defensive."
                samantha.say "Well you can hardly blame me."
                samantha.say "We lived here together before you even moved in!"
                samantha.say "Maybe you should try to get in on the conversation?"
                samantha.say "Rather than leave me to do all the talking!"
                "I can feel my cheeks start to flush as Sam chides me."
                "She's right, I've been a lousy host."
                "Too bust sulking at her mentioning Ryan than paying her attention."
    scene bg black with dissolve
    pause 1
    return

label samantha_halloween_dance:
    $ game.pass_time(2)
    if samantha.flags.engaged and not game.flags.ryandead:
        scene bg livingroom
        with fade
        "I can't help watching as Sam follows Ryan around during the party."
        "More often than not, he seems to be ignoring her, or at least pretending to."
        "Instead of paying her attention, Ryan chats to [bree.name] and Sasha."
        "Neither of them seem impressed, but that doesn't phase him either."
        show samantha halloween sad at left5
        show ryan halloween smile at right5
        with fade
        "Finally, Sam manages to get him alone by the makeshift dance-floor."
        samantha.say "Ah..."
        samantha.say "You want to dance with me, honey?"
        show ryan halloween annoyed
        ryan.say "What?"
        ryan.say "Oh, no, dear - not now."
        hide ryan
        show samantha halloween sad at center
        with moveoutright
        "With that he drifts off to pay attention to someone else."
        "Left standing on her own, Sam seems to notice me looking at her."
        menu:
            "Go over" if hero.charm >= 25:
                "Without thinking of the consequences, I walk over."
                "Sam's mood seems to lift almost as soon as I reach her."
                if samantha.flags.nickname == "cupcake":
                    mike.say "Hey, Cupcake."
                else:
                    mike.say "Hey, Sam."
                mike.say "Are you okay?"
                samantha.say "I know I'm supposed to say that I am."
                samantha.say "But I'm really not!"
                "I nod and offer her an awkward smile."
                mike.say "I kind of heard what just happened."
                mike.say "And...well..."
                mike.say "I could dance with you - if you'd like?"
                samantha.say "You know what, [hero.name]..."
                show samantha normal
                $ samantha.love += 2
                samantha.say "I think I'd like that!"
                hide samantha
                show dance samantha halloween
                with dissolve
                "Sam lets me lead her onto the dance-floor."
                "The song that starts playing is a slow one."
                "And so we end up dancing equally slowly."
                "Slowly and very close together."
                "Neither of us speaks the whole time."
                "Which is a relief to me."
                "As it means I can just enjoy being close to Sam."
                "She looks amazing in her costume, more beautiful than ever."
                "And it baffles me how Ryan can stand to be apart from her."
                "There's nowhere else I want to be right now."
                "And when the song ends, I don't want the dance to as well."
                "All I want is an excuse to keep on holding Sam close to me."
            "Stay away":
                "Part of me wants to go over and comfort her."
                "But I know the dangers of getting between a couple."
                "Before you know it, they're forgetting their quarrel."
                "And that's only because they're both turning on you!"
                "So I just offer Sam a sympathetic smile and a shrug."
                show samantha annoyed
                $ samantha.love -= 2
                "She doesn't seem to appreciate the gesture."
                "Instead she rolls her eyes and turns her back on me."
                hide samantha with dissolve
                "I guess she was hoping for something more."
                "Maybe a show of physical support?"
                "But it's too late now."
                "Anything more would look like it was done out of pity."
    else:
        scene bg livingroom
        show samantha halloween
        with fade
        "I must have been talking for a couple of minutes straight."
        "And in all that time, I hadn't noticed once that Sam wasn't listening."
        "But when I do, I stop in the middle of what I was trying to say."
        "She's staring at the makeshift dance-floor, ignoring me completely."
        if samantha.flags.nickname == "cupcake":
            mike.say "Ah, Cupcake..."
        else:
            mike.say "Ah, Sam..."
        mike.say "Are you okay?"
        show samantha surprised
        samantha.say "What...oh..."
        show samantha sad
        samantha.say "Sorry, [hero.name]."
        samantha.say "I was miles away."
        show samantha normal
        samantha.say "Just remembering when I lived here with Ryan."
        "Almost as soon as she mentions Ryan's name, Sam shudders."
        "It's like she's trying to shake off the memories of her past."
        samantha.say "But screw that guy, right?"
        samantha.say "We should go dance!"
        menu:
            "Accept":
                if samantha.flags.nickname == "cupcake":
                    mike.say "Of course, Cupcake."
                else:
                    mike.say "Of course, Sam."
                mike.say "I'd love to dance with you."
                show samantha happy
                $ samantha.love += 2
                "Sam smiles at this, nodding eagerly."
                "All thought of the past now seems forgotten."
                hide samantha
                show dance samantha halloween
                with dissolve
                "Sam lets me lead her onto the dance-floor."
                "The song that starts playing is a slow one."
                "And so we end up dancing equally slowly."
                "Slowly and very close together."
                "Neither of us speaks the whole time."
                "Which is a relief to me."
                "As it means I can just enjoy being close to Sam."
                "She looks amazing in her costume, more beautiful than ever."
                "I can't understand how Ryan let her slip away from him."
                "And I promise myself in that moment I won't make the same mistake."
            "Refuse":
                if samantha.flags.nickname == "cupcake":
                    mike.say "Nah, Cupcake."
                else:
                    mike.say "Nah, Sam."
                mike.say "I'm just not feeling it right now."
                show samantha sad
                $ samantha.love -= 2
                "Sam's expression changes suddenly."
                "She looks sad, almost disappointed."
                samantha.say "Yeah...yeah..."
                samantha.say "That's just what Ryan always said!"
                hide samantha with dissolve
                "And with that, she turns and walks away."
                "All I can do is watch her go while cursing myself."
                "The last thing I need to do is act like Ryan used to."
                "He lost Sam by neglecting her needs."
                "And I don't want to do the same thing myself!"
    scene bg black with dissolve
    pause 1
    return

label samantha_halloween_sex:

    if samantha.flags.engaged and ("samantha_event_A01" in DONE or "samantha_event_D03" in DONE or "samantha_event_C03" in DONE):
        scene bg livingroom with fade
        "It's getting pretty late by now and the party seems to be winding down."
        "Almost everyone is either drunk, tired or both and so the house is quiet."
        scene bg secondfloor with fade
        "I'm wandering down the corridor past the girl's bedrooms when I hear it."
        "The sound of someone snoring behind the door to Sasha's room."
        "Normally I'd just have a chuckle at how loud she was."
        "Maybe even go find [bree.name] so that she could have a listen too."
        "But tonight it occurs to me that it might not be Sasha in there at all."
        "What if someone's wandered into her room by mistake and fallen asleep?"
        "I should really check to see."
        "And so I sneak up to the door and open it just a little."
        "All I need to do is stick my head inside and take a look..."
        scene bg bedroom3
        show samantha halloween surprised
        show fx exclamation
        with fade
        samantha.say "Who's there?!?"
        "Sam hisses the question at me almost as soon as I can see into the room."
        mike.say "Whoa!"
        if samantha.flags.nickname == "cupcake":
            mike.say "Cupcake?!?"
        else:
            mike.say "Sam?!?"
        mike.say "What are you doing in Sasha's room?"
        "Sam wastes no time in hauling me in through the door."
        "And then she closes it behind me, leaning her back against it."
        show samantha normal
        samantha.say "It was my room before it was hers."
        samantha.say "You remember?"
        if samantha.flags.nickname == "cupcake":
            mike.say "Well...yeah, Cupcake."
        else:
            mike.say "Well...yeah, Sam."
        mike.say "Of course I do."
        mike.say "But that doesn't mean you can just walk in here like it's still yours!"
        "Sam shakes her head and points towards a chair in the corner of the room."
        "And it's then I see Ryan, slumped in the chair and apparently fast asleep."
        "Which explains the source of the snoring, but not why they're in here."
        samantha.say "He insisted that we come in here and check it out."
        samantha.say "Said he wanted to see what the 'hot goth chick' had done with it!"
        show samantha annoyed
        samantha.say "And then he went and passed out, leaving me here stuck in here."
        mike.say "Ah..."
        mike.say "You want me to help you carry him downstairs?"
        "Sam puts a hand to her forehead and sighs."
        show samantha normal
        "Then she shakes her head and turns to look me in the eye."
        samantha.say "No, [hero.name], he can stay where he is."
        show samantha annoyed
        samantha.say "He's been ignoring me most of the night."
        show samantha angry
        samantha.say "And when he's paid me any attention at all he's made me feel like trash."
        show samantha normal
        samantha.say "You're the only guy that's made me feel like a human being."
        "As she's saying all this, I notice Sam getting closer to me."
        if samantha.flags.nickname == "cupcake":
            mike.say "I...I'm just trying to be a good friend, Cupcake!"
        else:
            mike.say "I...I'm just trying to be a good friend, Sam!"
        samantha.say "I know, [hero.name], I know."
        samantha.say "I want to be a good friend to you too."
        show samantha blush
        samantha.say "And I think I know how we can be good to each other."
        samantha.say "That and pay Ryan back at the same time..."
        show samantha kiss halloween with fade
        $ samantha.flags.kiss += 1
        "Sam pulls me in close and plants her lips on mine."
        "My eyes dart to Ryan's comatose form for a moment."
        "And part of me wants to say that this isn't the time or the place."
        "But another part of me seems to be in charge."
        "Before I know what's happening, I'm kissing her back."
        "And Sam's walking backwards, leading me towards Sasha's bed."
        "She takes hold of my hands, guiding them to her costume's zipper."


        "We collapse onto the bed in a tangle of limbs."
        show samantha reverse halloween down with fade
        "And I can feel my cock pressing against her pussy even before we're naked."
        "There's no need for talk or foreplay between us."
        "I think both Sam and I have imagined this moment in our minds."
        "At least I know that I have!"
        show samantha reverse up
        "And so I'm just acting out the fantasy, making it a reality."
        "Sam moans as I push the head of my cock against her lips."
        show samantha reverse vaginal pleasure
        "They resist only for a few seconds, and then I'm inside of her."
        "I know that her idea was to cuck Ryan for revenge."
        "To do it in the room they once shared under this roof too."
        "But Ryan could be a million miles from here for all I care."
        show samantha reverse down orgasm
        "Sam's the only person on my mind, the only one I care about."
        "I can feel the pleasure she's getting from doing this."
        "It's almost like I can sense the frustration coming out of her."
        "In contrast, all I can feel is the desire that I've always had for her."
        show samantha reverse vaginal up
        pause 0.4
        show samantha reverse vaginal down at startle(0.05,-10)
        pause 0.4
        show samantha reverse vaginal up
        pause 0.4
        show samantha reverse vaginal down at startle(0.05,-10)
        pause 0.4
        show samantha reverse vaginal up
        pause 0.4
        show samantha reverse vaginal down at startle(0.05,-10)
        "That's what pushes me on and makes me pound her without mercy."
        "I want to tell her that's how I feel."
        show samantha reverse vaginal up
        pause 0.2
        show samantha reverse vaginal down at startle(0.05,-10)
        pause 0.3
        show samantha reverse vaginal up
        pause 0.2
        show samantha reverse vaginal down at startle(0.05,-10)
        pause 0.3
        show samantha reverse vaginal up
        pause 0.3
        show samantha reverse vaginal down at startle(0.05,-10)
        "I want to make her see that I'm not doing this to cuck Ryan."
        "I might hate the jerk, but I love Sam so much more!"
        show samantha reverse vaginal up orgasm
        pause 0.2
        show samantha reverse vaginal down at startle(0.05,-10)
        pause 0.3
        show samantha reverse vaginal up
        pause 0.2
        show samantha reverse vaginal down at startle(0.05,-10)
        pause 0.3
        show samantha reverse vaginal up
        pause 0.3
        show samantha reverse vaginal down at startle(0.05,-10)
        samantha.say "That's right, [hero.name]."
        samantha.say "This is what he's missing."
        samantha.say "I'm giving it all to you!"
        show samantha reverse up
        "I try to block out Sam's words."
        "Instead I keep my eyes focused on her body."
        show samantha reverse vaginal up
        pause 0.2
        show samantha reverse vaginal down at startle(0.05,-10)
        pause 0.3
        show samantha reverse vaginal up
        pause 0.2
        show samantha reverse vaginal down at startle(0.05,-10)
        pause 0.3
        show samantha reverse vaginal up
        pause 0.3
        show samantha reverse vaginal down at startle(0.05,-10)
        "I watch her breasts as they bounce and her belly as she curls beneath me."
        "I don't know if she keep on talking after that."
        show samantha reverse vaginal up
        pause 0.2
        show samantha reverse vaginal down at startle(0.05,-10)
        pause 0.3
        show samantha reverse vaginal up
        pause 0.2
        show samantha reverse vaginal down at startle(0.05,-10)
        pause 0.3
        show samantha reverse vaginal up
        pause 0.3
        show samantha reverse vaginal down at startle(0.05,-10)
        "Just that I'm going to cum any moment!"
        "Sam holds onto me tightly, keeping me form pulling out."
        show samantha reverse vaginal up
        pause 0.2
        show samantha reverse vaginal down at startle(0.05,-10)
        pause 0.3
        show samantha reverse vaginal up
        pause 0.2
        show samantha reverse vaginal down at startle(0.05,-10)
        pause 0.3
        show samantha reverse vaginal up
        pause 0.3
        show samantha reverse vaginal down creampie ahegao with vpunch
        "And so, when the time comes, I shoot my load into her."
        with vpunch
        samantha.say "Oh...god..."
        with vpunch
        samantha.say "That's...so...good..."
        samantha.say "Thank you...thank you!"
        "I smile, trying to keep my mind on the sensations of making love to Sam."
        "Yet I can't help gazing at Ryan, still comatose and snoring across the room."
        "Sure, helping Sam get a measure of revenge on him was fun."
        "But I want more than that - I want him gone and Sam all to myself!"
        $ samantha.sexperience += 1
        $ game.pass_time(1)
    else:
        scene bg livingroom
        with fade
        "By now it's getting late, almost midnight by my estimation."
        "The party's started to wind down and the house is getting quieter."
        "Almost everyone is either tired, drunk or both."
        "And this means that my skills as a host aren't in demand."
        scene bg secondfloor
        show samantha halloween
        with fade
        "So Sam and I have the chance to steal some time away from the guests."
        samantha.say "I still think of this place how it was before, you know?"
        samantha.say "Back when it was you, me and Ryan living here?"
        "Sam's tone gets a little sad as she brings up the past."
        "And I can see that she's in danger of becoming melancholy."
        if samantha.flags.nickname == "cupcake":
            mike.say "Me too, Cupcake."
        else:
            mike.say "Me too, Sam."
        mike.say "But I think I like it better now."
        show samantha surprised
        if Harem.together(bree, sasha, samantha, name='home'):
            samantha.say "You mean since my marriage broke down?!?"
            if samantha.flags.nickname == "cupcake":
                mike.say "You know what I mean, Cupcake!"
            else:
                mike.say "You know what I mean, Sam!"
            mike.say "Since you moved back in!"
        else:
            samantha.say "You mean since I moved out?!?"
            mike.say "No - of course not!"
            mike.say "I meant since we got together!"
        show samantha normal
        "Sam nods at this, seemingly placated."
        "She nods to the nearest door."
        samantha.say "This used to be my room."
        samantha.say "Well...mine and Ryan's."
        mike.say "Yeah, but since Sasha moved in..."
        mike.say "Let's just say the decor's changed a little!"
        show fx question
        "Suddenly I see a look of mischief appear on Sam's face."
        "She puts her hand on the door handle and looks me in the eye."
        samantha.say "Oh yeah?"
        samantha.say "This I have to see!"
        "With that, Sam opens the door and walks into Sasha's bedroom."
        if samantha.flags.nickname == "cupcake":
            mike.say "Cupcake, no!"
        else:
            mike.say "Sam, no!"
        mike.say "What if Sasha's in there?"
        mike.say "What if she's got company?!?"
        "I hurry after Sam, fearing the worst."
        scene bg bedroom3
        show samantha halloween
        with fade
        "But once I make it through the door, I breathe a sigh of relief."
        show samantha happy
        samantha.say "See, [hero.name]?"
        samantha.say "There's nobody in here."
        show samantha normal
        samantha.say "Ooh...look at this place."
        samantha.say "I had no idea there were so many shades of black!"
        if samantha.flags.nickname == "cupcake":
            mike.say "Okay, great, Cupcake."
        else:
            mike.say "Okay, great, Sam."
        mike.say "We've seen what we came to see."
        mike.say "How about we get out of here, huh?"
        "But Sam doesn't seem to hear me."
        "Instead she walks over to the side of Sasha's bed."
        "Or else she does and just chooses to ignore me."
        samantha.say "She put her bed right where ours was too!"
        samantha.say "I used to sleep on this side, you know?"
        show samantha blush
        samantha.say "I'd get undressed on this very spot, every night."





        "I can't move as she lays down on the bed and stretches out like a cat."
        samantha.say "You know something, [hero.name]."
        samantha.say "Towards the end, I'd lie right here and pleasure myself."
        samantha.say "I'd rub my pussy and think of other guys to get off."
        samantha.say "And more than once, I thought of you..."
        "I swallow audibly as I see Sam's hand slip between her thighs."
        samantha.say "Did you ever jerk off over me, [hero.name]?"
        samantha.say "Just imagine if we'd been doing at the same time, under the same roof!"
        "Almost on autopilot, I find myself walking over to the bed."
        "And before I know it, I'm stripping off my costume too."
        samantha.say "Let's do it, [hero.name]!"
        samantha.say "Let's make our fantasies a reality!"
        "I don't need any more convincing than that."
        show samantha reverse halloween up pleasure with fade
        "A moment later I all but pounce on Sam."
        "She squeals in delight as the bed groans under our weight."
        "But all I'm thinking about is getting my cock inside of her."
        "What follows is more of a desperate fumbling than romantic consummation."
        show samantha reverse vaginal orgasm
        "But the second I feel myself sliding into her, nothing else matters."
        "Sam's moans urge me on, and she clings to me desperately."
        "Somehow she ends up atop me, reverse cowgirl style."
        show samantha reverse vaginal up
        pause 0.4
        show samantha reverse vaginal down at startle(0.05,-10)
        pause 0.4
        show samantha reverse vaginal up
        pause 0.4
        show samantha reverse vaginal down at startle(0.05,-10)
        pause 0.4
        show samantha reverse vaginal up
        pause 0.4
        show samantha reverse vaginal down at startle(0.05,-10)
        "And in no time I'm pounding her like my life depends on it."
        samantha.say "Oh fuck..."
        samantha.say "It's better..."
        show samantha reverse vaginal up pleasure
        pause 0.4
        show samantha reverse vaginal down at startle(0.05,-10)
        pause 0.4
        show samantha reverse vaginal up
        pause 0.4
        show samantha reverse vaginal down at startle(0.05,-10)
        pause 0.4
        show samantha reverse vaginal up
        pause 0.4
        show samantha reverse vaginal down at startle(0.05,-10)
        samantha.say "Better than I imagined..."
        "She's right about that."
        "I must have thought of Sam a thousand time when I jerked off."
        "But the reality of being with her is something else entirely."
        "Every move I make feels like heaven, every moment I'm inside of her."
        show samantha reverse vaginal up orgasm
        pause 0.2
        show samantha reverse vaginal down at startle(0.05,-10)
        pause 0.3
        show samantha reverse vaginal up
        pause 0.2
        show samantha reverse vaginal down at startle(0.05,-10)
        pause 0.3
        show samantha reverse vaginal up
        pause 0.3
        show samantha reverse vaginal down at startle(0.05,-10)
        "The pleasure on her face pushes me on even, making me give all I have."
        "This is what I wanted when she was living here the first time."
        show samantha reverse vaginal up
        pause 0.2
        show samantha reverse vaginal down at startle(0.05,-10)
        pause 0.3
        show samantha reverse vaginal up
        pause 0.2
        show samantha reverse vaginal down at startle(0.05,-10)
        pause 0.3
        show samantha reverse vaginal up
        pause 0.3
        show samantha reverse vaginal down at startle(0.05,-10)
        "I wanted to be with her, but Ryan was always in the way."
        "And now I feel the need to make up for lost time."
        show samantha reverse vaginal up
        pause 0.2
        show samantha reverse vaginal down at startle(0.05,-10)
        pause 0.3
        show samantha reverse vaginal up
        pause 0.2
        show samantha reverse vaginal down at startle(0.05,-10)
        pause 0.3
        show samantha reverse vaginal up
        pause 0.3
        show samantha reverse vaginal down at startle(0.05,-10)
        "Sam nods desperately as I increase my speed and pound her harder."
        "Her breasts bounce above me and her belly curls."
        show samantha reverse vaginal up
        pause 0.2
        show samantha reverse vaginal down at startle(0.05,-10)
        pause 0.3
        show samantha reverse vaginal up
        pause 0.2
        show samantha reverse vaginal down at startle(0.05,-10)
        pause 0.3
        show samantha reverse vaginal up
        pause 0.3
        show samantha reverse vaginal down at startle(0.05,-10)
        "I hardly notice the sound of Sasha's bed as it hammers against the wall."
        samantha.say "Oh god..."
        samantha.say "[hero.name]..."
        samantha.say "You're going to make me..."
        show samantha reverse vaginal up ahegao
        pause 0.2
        show samantha reverse vaginal down at startle(0.05,-10)
        pause 0.3
        show samantha reverse vaginal up
        pause 0.2
        show samantha reverse vaginal down at startle(0.05,-10)
        pause 0.3
        show samantha reverse vaginal up
        pause 0.3
        show samantha reverse vaginal down with vpunch
        "Sam cries out as she cums, pushing herself down and onto."
        with vpunch
        "I feel the muscles of her pussy squeeze my cock."
        show samantha reverse creampie with vpunch
        "And I lose it a second later, shooting my load into her."
        "We stay entangled as the aftershocks flow through us."
        "But neither of us speaks the whole time."
        "It feels like what we just did doesn't need words."
        "Just time to hold onto each other and savour it."
        $ samantha.sexperience += 1
        $ game.pass_time(1)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
