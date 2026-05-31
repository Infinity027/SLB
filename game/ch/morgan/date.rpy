label morgan_date_intro_valentine_male:
    mike.say "Happy Valentine's day, Morgan."
    mike.say "Are you ready for our date?"
    mike.say "Because I can't wait to spend some quality time with my valentine!"
    if morgan.male >= 66:
        morgan.say "Ah, don't be such a sap, [hero.name]!"
        morgan.say "Just lighten up and have a good time already."
    elif morgan.male >= 33:
        morgan.say "Me too, [hero.name]!"
        morgan.say "I've been counting the days!"
    else:
        morgan.say "You bet I have, [hero.name]!"
        morgan.say "I can't wait to be with my valentine either!"
    return

label morgan_date_intro_halloween_male:
    mike.say "You ready to go, Morgan?"
    mike.say "Tonight should be fun, what with it being Halloween!"
    if morgan.male >= 66:
        morgan.say "So long as we don't have to dress-up in silly costumes!"
    elif morgan.male >= 33:
        morgan.say "Damn it - we should have worn some fun costumes!"
    else:
        morgan.say "Oh no - I could have worn a really cute costume tonight!"
    mike.say "Don't worry about it, Morgan."
    mike.say "We can still have fun without costumes."
    mike.say "And we can always plan ahead for Halloween next year."
    return

label morgan_date_intro_christmas_male:
    mike.say "Happy Christmas, Morgan!"
    mike.say "Hope you're full of festive cheer for our date!"
    if morgan.male >= 66:
        morgan.say "Hah...I'm more in it for the fun parts."
        morgan.say "Like your hot buns, [hero.name]!"
    elif morgan.male >= 33:
        morgan.say "I don't know about that, [hero.name]."
        morgan.say "I'm more interested in hanging out with you!"
    else:
        morgan.say "Of course, [hero.name]."
        morgan.say "I really love this time of year!"
    return

label morgan_date_intro_birthday_male:
    mike.say "Happy birthday, Morgan!"
    mike.say "And don't worry about anything."
    mike.say "I have an extra special birthday plan for us!"
    if morgan.male >= 66:
        morgan.say "Oh yeah?"
        morgan.say "This should be worth the admission fee!"
    elif morgan.male >= 33:
        morgan.say "You actually remembered?"
        morgan.say "That's so great, [hero.name]!"
    else:
        morgan.say "Aw, [hero.name] - that's so sweet of you!"
        morgan.say "I feel like such a lucky girl!"
    return

label morgan_date_intro_mc_birthday_male:
    mike.say "Ready to have some fun on our date, Morgan?"
    if morgan.male >= 66:
        morgan.say "Wait a minute, [hero.name]."
        morgan.say "You're not getting away with it this year!"
    if morgan.male >= 33:
        morgan.say "Oh no you don't, [hero.name]!"
        morgan.say "Aren't you forgetting something?"
    else:
        morgan.say "Don't be silly, [hero.name]!"
        morgan.say "You didn't think I'd forgotten, did you?"
    morgan.say "Happy birthday!"
    mike.say "Aw...thanks, Morgan!"
    mike.say "I should have known you'd remember."
    return

label morgan_date_eat_a_burger:
    "For some reason, eating a burger seems to have tickled Morgan's sense of humour."
    "She sits and eats quite happily, but can't keep from giggling every now and then."
    "I have no idea what she finds so funny, and it doesn't look like she's about to clue me in either."
    return

label morgan_date_buy_drink:
    if morgan.is_visibly_pregnant:
        show morgan angry
        $ morgan.love -= 10
        if morgan.male <= 33:
            morgan.say "Oh no, [hero.name]!"
            morgan.say "Won't you please think of the baby?!?"
        elif morgan.male <= 66:
            morgan.say "Ah, did you forget that I'm pregnant?"
            morgan.say "Urgh...you're so irresponsible sometimes!"
        else:
            morgan.say "What the fuck?"
            morgan.say "Did you forget I was pregnant, asshole?!?"
        $ hero.cancel_activity()
        hide morgan
    else:
        "Getting her hands on a drink really seems to help Morgan to loosen up and start enjoying herself."
        "Not that I'm trying to say that she's dependent on the booze, you understand?"
        "Just that it looks like it's helping her to just be herself around me."
    return

label morgan_date_play_darts:
    "I think I might have made a mistake in casually challenging Morgan to a game of darts."
    "She doesn't brag before we start, but it soon becomes clear that she's one mean darts player."
    "In the end, it's me that's struggling to keep up with her."
    return

label morgan_date_pub_play_pool:
    "Morgan grabs a cue and strides confidently over to the pool table."
    "Without asking, she racks up the balls and puts the cue ball in the D."
    "I take a deep breath, already wondering what I've let myself in for!"
    return

label morgan_date_buy_a_round:
    if morgan.is_visibly_pregnant:
        show morgan angry
        $ morgan.love -= 10
        if morgan.male <= 33:
            morgan.say "Oh no, [hero.name]!"
            morgan.say "Won't you please think of the baby?!?"
        elif morgan.male <= 66:
            morgan.say "Ah, did you forget that I'm pregnant?"
            morgan.say "Urgh...you're so irresponsible sometimes!"
        else:
            morgan.say "What the fuck?"
            morgan.say "Did you forget I was pregnant, asshole?!?"
        $ hero.cancel_activity()
    elif (hero.charm >= 60 - morgan.love and morgan.flags.drinks < 2):
        show drink morgan
        "When I offer to get the next round in, Morgan just shrugs and nods."
        "I guess that she's pretty much just expecting us to trade rounds anyway."
        "Which means she's a thoroughly modern girl."
        $ game.active_date.score += 5
        if "rebel" in morgan.traits:
            $ game.active_date.score += 5
        $ morgan.set_flag("drinks", 1, "day", mod="+")
        hide drink
    else:
        "I want to pay a round of beers to the whole pub."
        "But Morgan doesn't seem to want to drink, so I refrain from doing so."
        $ hero.cancel_activity()
    return

label morgan_date_play_arcade_intro_male:
    if morgan.male >= 66:
        morgan.say "Urgh..."
        morgan.say "Are you actually serious, [hero.name]?"
    elif morgan.male >= 33:
        morgan.say "Do we really have to do this, [hero.name]?"
        morgan.say "Seriously?"
    else:
        morgan.say "Eww..."
        morgan.say "This place is all sticky - and stinky too!"
    "I turn to face Morgan, tearing my attention away from the games around me."
    "I was expecting her to be more enthusiastic about coming to the arcade."
    "It's kind of hard to understand, since I love it here so much."
    mike.say "Give it a chance, Morgan."
    mike.say "There's like a hundred different games in here."
    mike.say "I'm sure we can find one that you'll like!"
    "Morgan looks less than convinced."
    "But she nods all the same."
    "I take this as permission to start hunting for a game."
    "And it doesn't take long for me to find one."
    mike.say "How about this one, Morgan?"
    mike.say "It's called 'Wonder Trio'."
    mike.say "And even better, it has three games."
    mike.say "So you can choose the one that you like the best!"
    if morgan.male >= 66:
        morgan.say "Okay, [hero.name] - let's try the shoot-em-up."
    elif morgan.male >= 33:
        morgan.say "Okay, [hero.name] - let's try the platformer."
    else:
        morgan.say "Ooh, the puzzle-game looks like fun!"
    "I nod eagerly, stuffing coins into the slot."
    return

label morgan_date_play_arcade_win_male:
    "Maybe I should have told Morgan that I'm pretty good at this game."
    "Because it doesn't take long for it to show."
    "I start pulling ahead as she struggles with the unfamiliar game."
    if morgan.male >= 66:
        morgan.say "Dammit..."
        morgan.say "This is REALLY tough!"
    elif morgan.male >= 33:
        morgan.say "Geez, [hero.name]..."
        morgan.say "This is really hard!"
    else:
        morgan.say "Oh dear..."
        morgan.say "I don't think I can do this!"
    mike.say "Just follow my lead, Morgan."
    mike.say "It's not as hard as it looks!"
    "My advice doesn't seem to sink in."
    "And even if it does, Morgan doesn't reap the benefits."
    "Which means that when we've used up all our credits, I'm way ahead of her."
    mike.say "Well done, Morgan."
    mike.say "You played pretty well!"
    if morgan.male >= 66:
        morgan.say "Don't patronise me, [hero.name]!"
        morgan.say "I suck at this game!"
    elif morgan.male >= 33:
        morgan.say "You don't have to patronise me, [hero.name]."
        morgan.say "I know I'm no good at this kind of thing!"
    else:
        morgan.say "Aw, thanks, [hero.name]!"
        morgan.say "You really think so?"
    morgan.say "But anyway..."
    morgan.say "We played the game, so can we go now?"
    return

label morgan_date_play_arcade_lose_male:
    "Maybe I should have picked another game to play with Morgan?"
    "Because the truth is that I'm really not very good at this one!"
    "Morgan starts to pull away almost from the start."
    if morgan.male >= 66:
        morgan.say "Oh yeah..."
        morgan.say "This is pretty fun, [hero.name]!"
    elif morgan.male >= 33:
        morgan.say "Wow..."
        morgan.say "This is actually a lot of fun!"
    else:
        morgan.say "Oh wow..."
        morgan.say "I can actually do this!"
    mike.say "W...wait a minute, Morgan..."
    mike.say "This was my idea, remember!"
    "My pleas don't seem to reach Morgan's ears."
    "Or if they do, she chooses to ignore them."
    "This means that she's way ahead of me once we're out of credits."
    mike.say "Wow, Morgan..."
    mike.say "You played so well!"
    if morgan.male >= 66:
        morgan.say "You'd better believe it, [hero.name]!"
    elif morgan.male >= 33:
        morgan.say "Yeah - I surprised myself!"
    else:
        morgan.say "Aw, thanks [hero.name]!"
    mike.say "So I guess you want to go somewhere else now?"
    morgan.say "Oh no, [hero.name]."
    morgan.say "I want to play again!"
    return

label morgan_dick_reactions:
    if not morgan.flags.seendick:
        $ morgan.flags.seendick = 1
        if hero.has_skill("hung"):
            show dick reactions morgan scared
            morgan.say "Gee, [hero.name]..."
            morgan.say "You sure grew up big down there!"
            mike.say "Is...that a problem, Morgan?"
            morgan.say "I...I don't really know!"
            morgan.say "Just promise you'll be gentle, okay?"
            $ morgan.sub += 10
        elif hero.has_skill("smalldick"):
            show dick reactions morgan tasty
            morgan.say "Mmm..."
            morgan.say "Pocket rocket!"
            mike.say "Is...that a problem, Morgan?"
            show dick reactions morgan smile
            morgan.say "No way!"
            morgan.say "I don't need a monster cock to get me off."
            morgan.say "All I need is to want the guy attached to it!"
            $ morgan.sub -= 10
        hide dick reactions
    return

label morgan_halloween_invitation:
    show morgan
    "I know from the start that there's only one girl I want to invite to the Halloween party."
    "And that's Morgan, because having her there just feels like it'd make the party that much more special."
    "So all I have to do now is choose the right moment to actually ask her to come along."
    "That shouldn't be too hard, right?"
    "I mean, who doesn't want to get an invite to a fun costume party on Halloween?"
    mike.say "Hey, Morgan..."
    mike.say "My housemates and I are throwing a Halloween party."
    mike.say "Do you want to come along?"
    mike.say "You know...kind of as my date?"
    show morgan surprised
    "Morgan's eyebrows raise at the mere mention of the party."
    "Which means that I know her interest has been piqued too."
    morgan.say "A house party?"
    show morgan normal
    morgan.say "I haven't been to one of those on Halloween for years!"
    "I sense a chance to sell the idea to Morgan."
    "And I immediately double down on my sales pitch."
    mike.say "It's going to be great, Morgan."
    mike.say "There'll be music and we're decorating the entire house."
    mike.say "Oh...and it's a costume party too!"
    "Morgan goes quiet for a moment."
    "And I can see that she's thinking about it."
    "Then she opens her mouth, about to give me an answer."
    if morgan.love >= 100:
        $ morgan.love += 1
        show morgan happy
        morgan.say "You know what, that sounds like fun!"
        "I can't keep from smiling."
        "That answer's as good as a yes!"
        mike.say "So you'll come to the party?"
        if morgan.male > 75:
            show morgan normal
            "Morgan nods and lets out an affirmative grunt."
            morgan.say "Sure I will."
            morgan.say "Sounds like a chance to hang out and party!"
            show morgan happy
            morgan.say "Of course I'm up for that."
            "I nod enthusiastically."
            "The last thing I want to do is dampen Morgan's spirits."
            mike.say "So, have you got any idea what costume you'll wear?"
            show morgan normal
            morgan.say "Nah, I haven't got a clue!"
            morgan.say "But I'll think of something before then."
            mike.say "That's great, Morgan."
            mike.say "I can't wait to see what you come up with!"
        if morgan.male < 40:
            "Morgan nods and lets out a squeal of delight."
            morgan.say "You bet I will, [hero.name]!"
            morgan.say "I get to dress up, dance and party!"
            morgan.say "It sounds like a crazy amount of fun."
            "I nod enthusiastically."
            "The last thing I want to do is dampen Morgan's spirits."
            mike.say "So, have you got any idea what costume you'll wear?"
            show morgan blush
            morgan.say "Ooh..."
            morgan.say "I don't know!"
            show morgan normal
            morgan.say "But I'll think of something before then."
            mike.say "That's great, Morgan."
            mike.say "I can't wait to see what you come up with!"
        else:
            show morgan normal
            "Morgan nods and gives me a smile."
            morgan.say "Yeah, [hero.name], I will."
            morgan.say "Like I said, I haven't been to a Halloween party in years."
            morgan.say "It'll be like we're all kids again!"
            "I nod enthusiastically."
            "The last thing I want to do is dampen Morgan's spirits."
            mike.say "So, have you got any idea what costume you'll wear?"
            morgan.say "No, you only just invited me - remember?!?"
            morgan.say "But I'll think of something before then."
            mike.say "That's great, Morgan."
            mike.say "I can't wait to see what you come up with!"
        $ game.flags.halloween_girl = "morgan"
    else:
        morgan.say "Nah, I think I'll give it a hard pass."
        "I blink in confusion and surprise."
        "Did Morgan actually say no?"
        mike.say "B...but why, Morgan?"
        if morgan.male > 75:
            "Morgan shrugs and lets out an apathetic grunt."
            morgan.say "I dunno, [hero.name]."
            $ morgan.sub -= 1
            morgan.say "It just sounds lame, that's all."
            morgan.say "I can think of a dozen things I'd rather do."
            "I nod slowly, trying to look like I understand."
            "Morgan just dismissed the idea so casually."
            "I'm afraid that if I show how disappointed I am..."
            "Well, that she'll treat my feelings the same way!"
            mike.say "Okay, Morgan."
            mike.say "If that's how you feel..."
            morgan.say "It is - that's exactly how I feel!"
        if morgan.male < 40:
            "Morgan shrugs and lets out a long sigh."
            morgan.say "Oh, [hero.name]..."
            $ morgan.love -= 1
            morgan.say "It just sounds so BORING!"
            morgan.say "I want to have fun on Halloween."
            morgan.say "Not be put to sleep!"
            "I nod slowly, trying to look like I understand."
            "Morgan just dismissed the idea so completely."
            "And she did it with such melodrama too!"
            "There's no way I want to get drawn into more of that."
            mike.say "Okay, Morgan."
            mike.say "If that's how you feel..."
            morgan.say "It is!"
            morgan.say "Now, let's talk about something else..."
        else:
            "Morgan shrugs and lets out a sigh."
            morgan.say "It's nothing personal, [hero.name]."
            morgan.say "I just feel like I've grown out of it, that's all."
            morgan.say "It's what we'd have done back when we were kids."
            "I nod slowly, trying to make it clear that I understand."
            "Morgan just gave me a pretty good reason for her answer."
            "I should show her the same respect in return."
            mike.say "Okay, Morgan."
            mike.say "If that's how you feel..."
            $ morgan.love += 1
            morgan.say "Thanks for understanding, [hero.name]."
            morgan.say "It means a lot to know that you do!"
    return

label morgan_halloween_arrival:
    scene bg house with wiperight
    "I open the door with my head still somewhere else."
    "The stress of organising the party occupying my mind."
    "But I snap out of it at the sight of a furry, brown tail."
    "A tail which belongs to an equally furry figure with its back to me."
    mike.say "Morgan?"
    mike.say "Is that you?"
    "The figure jumps a little at the sound of my voice."
    show morgan halloween with dissolve
    "But then it turns around to reveal that my suspicions were correct."
    "Morgan's wearing a onesie made of brown fur."
    "And the ears atop the hood make it clear she's supposed to be a bear."
    morgan.say "Hey, [hero.name]."
    morgan.say "How do you like my costume?"
    if morgan.male > 75:
        mike.say "You're a teddy bear?!?"
        show morgan angry
        "Morgan bristles at the mere mention of the term."
        show morgan a
        "She crosses her arms over her chest in a show of defiance."
        morgan.say "Who said anything about me being a teddy bear?"
        morgan.say "Why does everyone keep saying that?!?"
        morgan.say "I'm just a bear, dammit!"
    elif morgan.male < 40:
        show morgan happy
        morgan.say "I'm a teddy bear!"
        morgan.say "And I'm here for cuddles!"
    menu:
        "Agree" if morgan.male > 75:
            "I hold my hands up in a gesture of surrender."
            "At times like this, it's best to just go with it!"
            mike.say "Okay, Morgan, okay."
            mike.say "You're a big, tough bear."
            mike.say "And I'm really scared of you!"
            "For a moment it looks like Morgan is going to protest again."
            show morgan normal
            "But then I see the annoyance drain out of her expression."
            show morgan happy
            "She laughs and shakes her head."
            morgan.say "Maybe asked for it, dressing up like this."
            show morgan normal
            morgan.say "Next time I guess I should put more effort in."
            mike.say "I don't know, Morgan."
            mike.say "Being a bear kind of suits you."
            mike.say "And you look really cute with a fluffy tail!"
            $ morgan.love += 1
            show morgan happy
            "Morgan aims a punch at my arm for my troubles."
            "But she laughs again and then pushes her way into the house."
        "Disagree" if morgan.male > 75:
            "I cradle my chin in the palm of my hand."
            "And then I stand back to study Morgan more closely."
            mike.say "Hmm..."
            mike.say "You're short, furry and oh so adorable."
            mike.say "All the signs say that you're a cute little teddy bear!"
            "Morgan is positively quaking with rage by now."
            "She plants her hands on her hips and squares up to me."
            $ morgan.love -= 2
            show morgan angry at center, vshake
            show fx exclamation
            morgan.say "I AM NOT A TEDDY BEAR!!!"
            "It's no good trying to hold it in any longer."
            "And I burst out laughing a moment later."
            "For a second Morgan looks like she's about to explode."
            show morgan normal
            "But then I see the annoyance drain out of her expression."
            show morgan happy
            "She laughs and shakes her head."
            morgan.say "Maybe asked for it, dressing up like this."
            morgan.say "Next time I guess I should put more effort in."
            mike.say "I don't know, Morgan."
            mike.say "Being a bear kind of suits you."
            mike.say "And you look really cute with a fluffy tail!"
            "Morgan aims a punch at my arm for my troubles."
            "But she laughs again and then pushes her way into the house."
        "Compliment" if morgan.male <= 75:
            "I can't help smiling at the sight of Morgan in the costume."
            "She looks so cute and adorable, not to mention sexy!"
            "And the way she blushes as I'm checking her out."
            "She's suddenly all I can think about!"
            mike.say "You look amazing, Morgan."
            mike.say "You're the cutest bear I ever saw!"
            if morgan.male < 40:
                $ morgan.love += 2
                show morgan normal
                "Morgan smiles like she's lighting up."
                "She clasps her hands under her chin."
                "And for a moment I think she's going to explode with joy."
                show morgan blush
                morgan.say "Y...you really mean that?"
                show morgan blushhappy
                morgan.say "Aw, you made me so happy!"
                morgan.say "I want to be your teddy bear, [hero.name]."
                morgan.say "You can cuddle me all night!"
                "I smile and usher Morgan into the house."
                "All the time trying to hide just how hard I am right now!"
            else:
                $ morgan.love += 1
                $ morgan.male -= 1
                show morgan blush
                "Morgan wrinkles her nose and looks away for a second."
                "She tries hard to make it look like she hates the attention."
                "But I know her well enough not to be fooled."
                "Deep down she loves the compliments."
                morgan.say "Ah, shut up!"
                morgan.say "This is no big deal."
                morgan.say "Just something I threw on at the last minute."
                mike.say "Whatever you say, Morgan."
                mike.say "So long as you're my teddy bear tonight!"
                show morgan blushhappy
                "Morgan's cheeks flush red at this."
                "But she clings to me all the same."
        "Criticize" if morgan.male <= 75:
            mike.say "Ah..."
            mike.say "I don't know, Morgan."
            show morgan angry
            "Morgan's brow furrows at this."
            "And she frowns, cocking her head on one side."
            morgan.say "What's that supposed to mean?"
            "I shrug and shake my head."
            mike.say "I guess I just don't see you as a teddy bear."
            mike.say "It's cute and all that."
            if morgan.male < 40:
                mike.say "But I'm not into soft and fluffy!"
            else:
                mike.say "But I never thought of you as soft and fluffy!"
            $ morgan.love -= 4
            "Morgan plants her hands on her hips."
            "Then she lets out a huff of frustration."
            if morgan.male < 40:
                morgan.say "Well that's just perfect, [hero.name]!"
                morgan.say "I go to all this trouble to dress up for you."
                morgan.say "And you can't even pretend to like it!"
            else:
                $ morgan.male += 1
                morgan.say "Who said that I was supposed to be a teddy bear, huh?"
                morgan.say "For all you know, I could be a damn grizzly!"
            "I can't help chuckling at Morgan's show of defiance."
            "Which of course does nothing to soften her mood."
            if morgan.male < 40:
                mike.say "Okay, okay - I'm sorry, Morgan."
                mike.say "Come on in and who knows."
                mike.say "Maybe it'll start to grow on me."
            else:
                mike.say "Okay, okay - I get it!"
                mike.say "You're just going to have to prove it to me."
                mike.say "Show me how much of a grizzly you really are!"
    scene bg black with dissolve
    pause 1
    return

label morgan_halloween_party:
    $ game.pass_time(2)
    scene bg livingroom
    with dissolve
    scottie.say "Oh wow - a teddy bear!"
    scottie.say "And a real cute one too!"
    scottie.say "How about cuddling up with me, baby?"
    "The moment I hear Scottie's voice I know what's happening."
    "From what he just said, he can only be hitting on Morgan!"
    show scottie halloween perv at left5
    show morgan halloween annoyed at right5
    with dissolve
    "I turn around to see that I'm right."
    "He's leaning over her, almost drooling at what he sees."
    if morgan.male > 75:
        show morgan angry
        morgan.say "Hey!"
        morgan.say "Who are you calling cute?!?"
    elif morgan.male < 40:
        show morgan blush
        morgan.say "Oh no!"
        morgan.say "I'm not that kind of bear!"
    else:
        show morgan annoyed
        morgan.say "Urgh..."
        morgan.say "What if I say no?"
    "Looks like I need to step in here."
    "And I should do it before things get out of hand too!"
    menu:
        "Defend Morgan":
            mike.say "Hey, Scottie."
            mike.say "Cuddling bears without their consent is not cool!"
            show scottie sad
            "Scottie looks surprised to see me."
            "And he struggles to explain himself."
            scottie.say "I didn't..."
            scottie.say "I wasn't..."
            scottie.say "I wouldn't..."
            hide scottie
            show morgan normal at center
            with moveoutleft
            "He scuttles off, still muttering nervously."
            "Which leaves me alone to face Morgan."
            if morgan.male > 75:
                show morgan angry
                morgan.say "I could have handled him on my own, you know!"
                $ morgan.male -= 1
                show morgan normal
                morgan.say "But thanks for the help."
                morgan.say "And for not calling me a teddy bear too!"
            elif morgan.male < 40:
                $ morgan.love += 2
                $ morgan.sub += 1
                show morgan happy
                morgan.say "Oh, thank you, [hero.name]!"
                morgan.say "There was no way I wanted that guy cuddling me!"
                show morgan blush
                morgan.say "But you can have all the cuddles you like..."
            else:
                $ morgan.love += 1
                show morgan normal
                morgan.say "I was about to tell him to get lost."
                morgan.say "But thanks for helping me out all the same."
        "Defend Scottie":
            mike.say "Hey, Morgan."
            mike.say "You should really lighten up!"
            mike.say "You can't blame the guy for reacting like that."
            show scottie normal
            show morgan angry
            "Scottie looks surprised to see me."
            "But then relief shows on his face."
            "Morgan, on the other hand, looks less than impressed."
            if morgan.male > 75:
                $ morgan.love -= 4
                morgan.say "I don't need you to tell me what to do!"
                morgan.say "And I don't need this jerk hitting on me either!"
            elif morgan.male < 40:
                $ morgan.love -= 2
                $ morgan.sub -= 1
                morgan.say "It's not okay, [hero.name]."
                morgan.say "I was scared without you there to save me!"
            else:
                $ morgan.male += 1
                morgan.say "Seriously, [hero.name]..."
                morgan.say "I don't like being hit on like this!"
            "I shake my head and roll my eyes, not sympathising with her in the least."
            hide scottie
            show morgan at center
            with moveoutleft
            "Scottie takes the chance to slink away, leaving me to face Morgan alone."
            "And I don't think I've impressed her with my handling of the situation either!"
    scene bg black with dissolve
    pause 1
    return

label morgan_halloween_dance:
    $ game.pass_time(2)
    scene bg livingroom
    show morgan halloween
    with fade
    morgan.say "Ah..."
    morgan.say "Everyone seems to be up and dancing!"
    morgan.say "Do you think that we should too?"
    "Normally I'd jump at the chance to hit the dance-floor with Morgan."
    "But there's just something a little weird about the tone of her voice."
    "It's almost like she's forcing herself to ask the question."
    "And I don't know if she wants me to encourage her to dance."
    "Or if she wants me to let her off the hook and say that I don't feel like it."
    "But she's looking at me like she wants an answer."
    "So I have to jump one way or the other..."
    menu:
        "Insist on dancing":
            mike.say "Yeah, Morgan - we should."
            mike.say "Let's get in on the action!"
            "Before Morgan has the chance to object, I take hold of her hand."
            hide morgan
            show dance morgan halloween
            with dissolve
            "And within a few mere moments, we're on the dance-floor together."
            if morgan.male > 75:
                "Almost as soon as we're dancing, Morgan stiffens up."
                $ morgan.love -= 2
                "She hardly moves at all, like she's rooted to the spot!"
                "And the look on her face tells me that she's not happy."
                "But it's too late to back out now."
                "We're up and dancing, so we'll have to tough it out."
                "What follows is one of the most painful few minutes of my life."
                "I have to keep on smiling as I die a little on the inside."
                "And when it's all over, things don't improve either."
                "I can practically feel how annoyed Morgan is with me."
            elif morgan.male < 40:
                "Almost as soon as we're dancing, I know I made the right decision."
                $ morgan.love += 2
                "Morgan comes alive on the dance-floor, turning into a ball of energy."
                "With every song that ends, I can feel myself getting more tired."
                "But all they seem to do is reinvigorate her all over again!"
                "Of course, the consolation is that she clings to me the whole time."
                "And having Morgan pressed so close to me makes it worth the effort."
                "Let's just say that I get some serious skin to fur contact."
                "I remember having a teddy bear when I was a kid."
                "But cuddling it never got me hard the way Morgan does!"
            else:
                "As soon as we start dancing, Morgan seems to loosen up."
                $ morgan.love += 1
                $ morgan.male -= 1
                "Where before she was stiff and nervous, now she relaxes."
                "Soon enough we're strutting our not so funky stuff."
                "And all thought of keeping away from the dance-floor is forgotten."
                "I guess that what Morgan really needed was a gentle push."
                "Or maybe she needed to know that I'd be with her the whole time."
                "Either way she becomes the only thing on my mind."
                "And let's just say that I get some serious skin to fur contact."
                "I remember having a teddy bear when I was a kid."
                "But cuddling it never got me hard the way Morgan does!"
        "Pass on dancing":
            mike.say "Yeah, Morgan - we could."
            mike.say "But I'm just not feeling it right now."
            mike.say "Maybe we wait until later?"
            "I raise my eyebrow, waiting for her response."
            if morgan.male > 75:
                $ morgan.love += 2
                show morgan happy
                "Almost as soon as the words are out of my mouth, I see Morgan relax."
                "She let's out a sigh of obvious relief and almost slumps against me."
                morgan.say "Phew..."
                morgan.say "Thank god for that!"
                morgan.say "I HATE dancing when I'm not in the mood!"
                "I can't keep from nodding as soon as I hear this."
                mike.say "Me too!"
                mike.say "Like I just don't need the pressure!"
                "Morgan smiles at my admission."
                "And I can't help thinking I just scored a few points with her!"
            elif morgan.male < 40:
                $ morgan.love -= 1
                $ morgan.sub -= 2
                "Almost as soon as the words are out of my mouth, I see Morgan begin to pout."
                show morgan a annoyed
                "She crosses her arms over her chest and makes a huffing sound."
                morgan.say "Humph..."
                morgan.say "That's not what you were supposed to say!"
                "Puzzled, I shake my head."
                mike.say "What do you mean, Morgan?"
                mike.say "You asked me a question and I gave you an answer!"
                show morgan angry
                morgan.say "But it wasn't the one I wanted!"
                morgan.say "You're supposed to know what I mean!"
                mike.say "What - even when you don't say what you mean?"
                morgan.say "Especially when I don't say what I mean!"
            else:
                "Morgan nods in a nonchalant manner, accepting my suggestion."
                "But there's a slight undertone that betrays her apparent relief."
                $ morgan.love += 1
                morgan.say "That's fine, [hero.name]."
                morgan.say "I wasn't really feeling it anyway."
                "I nod too, hoping that Morgan's telling the truth."
                "And that she's not just telling me what I want to hear."
                mike.say "We've still got all night to dance."
                mike.say "I just don't like being forced when I'm not in the mood."
                morgan.say "It's okay - me neither."
    scene bg black with dissolve
    pause 1
    return

label morgan_halloween_sex:
    scene black with timelaps
    scene bg livingroom
    show morgan halloween happy at center, zoomAt(1.5, (640, 1040))
    with timelaps
    "I've been finding it hard to keep my hands off of Morgan all night."
    "There's just something irresistible about her in that bear costume."
    "She's cute as hell to begin with, but wrap her up in all that fake fur..."
    "And well, all I want to do is stroke and squeeze her every chance I get!"
    "At first she takes it in her stride, laughing my attentions off."
    "But as it gets later and she's had more to drink, things start to change."
    "Morgan begins cuddling up to me more, giggling at the attention she's getting."
    "And she the more I stroke her, the more she seems to want to be stroked!"
    scene bg bedroom1
    show morgan halloween angry at center, zoomAt(1.5, (640, 1040))
    with fade
    "By the time we make it to my bedroom at the end of the night, she's actually growling!"
    show morgan halloween happy
    "I mean, not in a threatening way like a real bear would."
    "More like the cute kind of sounds you'd expect a teddy bear to make."
    show morgan halloween angry
    morgan.say "Grrr..."
    if morgan.male > 75:
        morgan.say "I'm a savage little bear!"
    elif morgan.male < 40:
        morgan.say "I'm a little teddy bear!"
    else:
        morgan.say "I'm a little bear!"
    "She makes a point of clawing the air with her hands."
    "And she stalks over to the bed, looking back over her shoulder at me."
    "I follow behind her, already getting turned on."
    mike.say "What, like the little bear in the fairy tale?"
    mike.say "The one that had his porridge eaten by Goldie Locks?"
    morgan.say "No way!"
    if morgan.male > 75:
        morgan.say "I'd have eaten her all up if she tried that with me!"
    elif morgan.male < 40:
        morgan.say "That mean old Goldie Locks wouldn't dare!"
    else:
        morgan.say "Forget the porridge - wouldn't you rather eat me?"
    "Morgan crawls onto the bed and stands on her hands and knees."
    "She claws the air again."
    show morgan flirt
    "But this time she adds a quick shake of her ass too."
    morgan.say "Mmm..."
    morgan.say "You might want to get over here, [hero.name]."
    morgan.say "Before I get the urge to hibernate!"
    "I nod at this, understanding the nature of the invitation."
    "It takes me less than a minute to strip off my clothes."
    "And then I leap onto the bed behind Morgan."
    hide morgan
    show morgan doggy halloween
    with fade
    "She giggles and shakes her ass again, pushing it against my groin."
    "I respond in the only way that makes sense, grabbing it with both hands."
    "Morgan begins to slowly unzip her costume."
    "Which reveals first her small, pert breasts and then her belly."
    "At the same time she uses her other hand to grab my cock."
    "I gasp in surprise as she guides it roughly between her thighs."
    "And the moment that it touches the folds of her pussy, I know what she wants."
    "Morgan's already wet, slippery and ready for me down there."
    "All it takes is a moment to get things in the right position..."
    show morgan doggy pleasure vaginal
    if persistent.xray:
        show morgan doggy xray
    "And then I'm inside of her, sinking all the way in."
    "I gasp at the sense of sudden release."
    "Morgan does the same, nodding eagerly for more."
    "And I'm happy to give her just what she wants."
    "I start slowly, moving in and out at a steady pace."
    "But it doesn't take long for me to pick up speed."
    "As soon as I do so, Morgan matches me, keeping pace and demanding more."
    "We go on like this until I'm working like a piston."
    "My thighs slap against Morgan's own like the crack of a whip."
    "And yet still she seems to want me to go faster."
    show morgan doggy normal tongueout
    "Morgan looks back at me over her shoulder, eyes pleading."
    "I redouble my efforts, feeling the fatigue of the day for the first time."
    "There's no way that I'm going to stop before I have to."
    "I just hope I can hold on long enough to give Morgan what she wants!"
    show morgan doggy spit pleasure
    "The cries that are coming out of her mouth say that could be on the cards."
    "Morgan's yelping and crying with every thrust I make inside of her now."
    "And she's almost bent double as she rides my cock."
    show morgan doggy ahegao creampie smile with hpunch
    "Her back arches just as I feel myself cumming."
    with hpunch
    "At that same moment, the cries come to an end."
    with hpunch
    "Instead, Morgan holds her breath, gasping as she cums too."
    "I hold onto her tightly as we feel the aftershocks pass through out bodies."
    "And then we collapse onto the bed, still entwined in one another."
    $ morgan.sexperience += 1
    $ game.pass_time(1)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
