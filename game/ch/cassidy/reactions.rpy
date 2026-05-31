label cassidy_ice_cream_reaction_male:
    mike.say "It's so hot today, Cassidy - we need some ice cream!"
    cassidy.say "Yay - I LOVE ice cream!"
    "At the ice cream stall, I buy myself a cone with a couple of different scoops."
    "But Cassidy orders herself a pretty fancy sundae that comes with a long spoon."
    mike.say "Whoa, Cassidy - that thing looks pretty amazing!"
    cassidy.say "When I eat an ice cream, I'm not messing around!"
    "Cassidy looks at me sideways as she spoons ice cream into her mouth."
    "And my own cone sits untouched in my hand as she hold me spellbound."
    "I only actually remember it's there when I feel it begin to melt, running over my fingers!"
    return

label cassidy_ask_phone_male:
    mike.say "Hey, Cassidy..."
    mike.say "We should really swap numbers."
    if hero.charm >= 20 - cassidy.love:
        show cassidy happy
        $ hero.smartphone_contacts.append("cassidy")
        cassidy.say "That's a great idea, [hero.name]!"
        cassidy.say "I know just the ringtone for your number too!"
    else:
        show cassidy annoyed
        $ cassidy.love -= 1
        $ cassidy.sub -= 1
        cassidy.say "I don't think so, [hero.name]."
        cassidy.say "I'm not ready to share my number with you."
        cassidy.say "Not yet, anyway."
    return

label cassidy_ask_birthday_male:
    mike.say "Hey, Cassidy..."
    mike.say "When's your birthday?"
    if hero.charm >= 40 - cassidy.love:
        show cassidy happy
        $ cassidy.flags.birthdayknown = True
        cassidy.say "Oh, that's something you really should know."
        cassidy.say "That way you have no excuse for forgetting it!"
        cassidy.say "It's Spring 9."
    else:
        show cassidy annoyed
        $ cassidy.sub -= 1
        $ cassidy.love -= 1
        cassidy.say "Why would you ask me that, [hero.name]?"
        cassidy.say "I'm old enough to do smoke, drink AND drive!"
    return

label cassidy_offer_a_drink_male:
    mike.say "Would you like a drink, Cassidy?"
    mike.say "Because I was just thinking of going to the bar."
    "Almost the second the words are out of my mouth, Cassidy turns to face me."
    if cassidy.is_visibly_pregnant:
        show cassidy angry
        $ cassidy.love -= 10
        cassidy.say "[hero.name], you...you beast!"
        cassidy.say "First you get me pregnant."
        cassidy.say "And then you put our child in danger by offering me alcohol!"
        $ hero.cancel_activity()
        hide cassidy
    elif (hero.charm >= 60 - cassidy.love and cassidy.flags.drinks < 2) or date_girl == cassidy:
        show cassidy happy
        cassidy.say "So nice of you to ask, [hero.name]."
        cassidy.say "I'll have one of those fancy cocktails, thank you!"
        hide cassidy
        show drink cassidy
        if cassidy.love <= 25:
            $ cassidy.love += 1
        elif date_girl == cassidy and game.active_date:
            $ game.active_date.score += 5
        call expression cassidy.get_chat from _call_expression_223
        hide drink cassidy
        $ cassidy.set_flag("drinks", 1, "day", mod="+")
    else:
        show cassidy annoyed
        cassidy.say "Don't bother, [hero.name]."
        cassidy.say "You probably couldn't afford what I want anyway!"
        $ hero.cancel_activity()
        hide cassidy
    return

label cassidy_slap_ass_intro_male:
    "Cassidy sashays along at my side, without a care in the world."
    "And the whole time her ass is moving too, making its own rhythm."
    "I can't take my eyes off it, no matter how hard I try."
    "And before too long, I get the urge to slap it."
    "Nothing too hard - just a little tap, that's all..."
    return

label cassidy_slap_ass_happy_male:
    "Cassidy makes a little leap into the air."
    "And she lets out a yelp of surprise at the same time."
    cassidy.say "Ow..."
    cassidy.say "What was that?!?"
    "She rubs her ass as she looks at me."
    "And it doesn't take long for her to figure it out."
    cassidy.say "Just couldn't contain yourself, huh?"
    cassidy.say "If you want to touch me, [hero.name]..."
    cassidy.say "All you have to do is ask!"
    return

label cassidy_slap_ass_angry_male:
    "Cassidy makes a little leap into the air."
    "And she lets out a yelp of surprise at the same time."
    cassidy.say "Ow..."
    cassidy.say "What was that?!?"
    "She rubs her ass as she looks at me."
    "And it doesn't take long for her to figure it out."
    cassidy.say "You know that's shitty, [hero.name]!"
    cassidy.say "I might have let you touch me."
    cassidy.say "If only you had the manners to ask first!"
    return

label cassidy_breakup_male:
    show cassidy
    "I guess that it's kind of like pulling teeth, you know?"
    "You really would rather not do it at all."
    "You know that it's going to hurt like hell."
    "But you also know that you can't just leave it to fester either."
    "So in the end, you just have to get on with it..."
    mike.say "Cassidy..."
    mike.say "I've been thinking..."
    mike.say "Thinking about us, you know?"
    "Cassidy regards me with a strange expression on her face."
    "It looks a lot like concern, but a lot like confusion too."
    "It's almost like she's experiencing something for the very first time."
    cassidy.say "Huh?"
    cassidy.say "What's that supposed to mean, [hero.name]?"
    cassidy.say "I think about us all the time - so what?"
    "I try to keep my voice even as I explain myself."
    "Right now I don't know if Cassidy is playing dumb."
    "Or else she might actually not know what I mean."
    mike.say "I mean us, Cassidy - our relationship."
    mike.say "I don't think it's working out between us."
    show cassidy annoyed
    "Cassidy pulls her head back, like she's been stung."
    "Then she shakes it, letting me know that she's still not getting it."
    show cassidy angry
    cassidy.say "Wait a minute..."
    cassidy.say "Are you actually saying that you..."
    cassidy.say "You're DUMPING me?!?"
    cassidy.say "Nobody's ever dumped me before!"
    cassidy.say "I'm the one that does the dumping!"
    "I can honestly say that it doesn't feel good."
    "There's no pride in being the first person to dump Cassidy!"
    "In fact, it kind of makes the whole thing that much more awkward."
    mike.say "I'm sorry, Cassidy."
    mike.say "But that's just the way I feel."
    mike.say "I'm sure you'll get over it...eventually!"
    "Cassidy narrows her eyes and fixes me with a hard stare."
    "And I can almost feel myself begin to squirm under her gaze."
    cassidy.say "Oh, I'll get over it alright, [hero.name]."
    cassidy.say "In fact, I'm already over it - SO over it!"
    cassidy.say "You're the one that's never going to forget me!"
    return

label cassidy_go_steady_intro_male:
    mike.say "We're going strong, right, Cassidy?"
    mike.say "So we should make it official."
    mike.say "You know, go steady?"
    return

label cassidy_go_steady_yes_male:
    cassidy.say "Hmm..."
    cassidy.say "I guess that's right, [hero.name]."
    cassidy.say "We really should go steady!"
    "Cassidy smiles and leans in to kiss my cheek."
    "Which instantly makes a smile spread across my face."
    return

label cassidy_go_steady_no_male:
    if game.week_day % 2 == 0:
        cassidy.say "Hmm..."
        cassidy.say "I don't think that's going to happen, [hero.name]."
        cassidy.say "At least not right now."
    else:
        mike.say "I would like us to be an official couple, you know 'go steady' as they say."
        cassidy.say "Don't be silly, that doesn't make sense given the arrangement we have."
    return

label cassidy_pet_intro_male:
    "I suddenly feel a rush of affection for Cassidy."
    "So much so that I can't help myself."
    "I just reach out and pat her on the head."
    return

label cassidy_pet_happy_male:
    cassidy.say "Ooh..."
    cassidy.say "Th...thank you, [hero.name]."
    cassidy.say "He he...I guess that means I'm a good girl!"
    return

label cassidy_pet_annoyed_male:
    cassidy.say "Hey!"
    cassidy.say "Where do you get off patting me like that?!?"
    cassidy.say "I'm not a dog, you know!"
    return

label cassidy_massage_intro_male:
    mike.say "You've got a lot of tension in your shoulders, Cassidy."
    mike.say "Would you like me to give you a massage?"
    mike.say "I've been told I have magic fingers!"
    return

label cassidy_massage_accept_male:
    cassidy.say "Well, I normally get a massage from Andre at the country club."
    cassidy.say "But I am feeling pretty tense right now."
    cassidy.say "So I guess it couldn't hurt..."
    return

label cassidy_massage_refuse_male:
    cassidy.say "I have to say no, [hero.name]."
    cassidy.say "I only ever get a massage from Andre at the country club."
    cassidy.say "So I have very high expectations!"
    return

label cassidy_piercing_nipples_reaction_male:
    if not game.flags.dwaynedead:
        cassidy.say "Daddy always hated the idea of me getting my nipples pierced."
        cassidy.say "But what in the hell would he know about it, right?"
        cassidy.say "I should SO listen to you instead of him, [hero.name]!"
    else:
        cassidy.say "Daddy always hated the idea of me getting my nipples pierced."
        cassidy.say "But he's dead now, so what can he do about it, right?"
        cassidy.say "I'm SO glad you're not like he was, [hero.name]!"
    return

label cassidy_piercing_navel_reaction_male:
    if not game.flags.dwaynedead:
        cassidy.say "Oh, this is going to look SO cute when I wear my swimsuit!"
        cassidy.say "And I can't wait to wear it for you, [hero.name]!"
        cassidy.say "Can you wait to see it?"
    else:
        cassidy.say "Oh, this is going to look SO cute when I wear my swimsuit!"
        cassidy.say "And I can't wait to wear it for you, [hero.name]!"
        cassidy.say "I can just imagine Daddy, turning in his grave!"
    return

label cassidy_piercing_clit_reaction_male:
    if not game.flags.dwaynedead:
        cassidy.say "Daddy would freak out and die if he knew I got my clit pierced!"
        cassidy.say "But that just makes it so much better, [hero.name]!"
        cassidy.say "This can be our little secret, right?"
    else:
        cassidy.say "Daddy would have freaked out if he knew I got my clit pierced!"
        cassidy.say "But he's dead and gone, what who cares, [hero.name]!"
        cassidy.say "This can be our little secret, right?"
    return

label cassidy_piercing_head_reaction_male:
    if not game.flags.dwaynedead:
        cassidy.say "Thanks for putting the idea to get this into my head, [hero.name]."
        cassidy.say "I'll have to keep it a secret from Daddy though."
        cassidy.say "But it'll be so hard to resist sticking my tongue out at him from now on!"
    else:
        cassidy.say "Thanks for putting the idea to get this into my head, [hero.name]."
        cassidy.say "I'll have to keep it a secret from Mommy though."
        cassidy.say "But it'll be so hard to resist sticking my tongue out at her from now on!"
    return

label cassidy_piercing_nose_reaction_male:
    if not game.flags.dwaynedead:
        cassidy.say "I guess this officially makes me a rebel, huh, [hero.name]?"
        cassidy.say "I'm breaking the rules and I don't care who knows it!"
        cassidy.say "God, you really bring out the bad girl in me!"
    else:
        cassidy.say "I guess this officially makes me a rebel, huh, [hero.name]?"
        cassidy.say "I'm breaking the rules and I don't care who knows it!"
        cassidy.say "Daddy's dead and I'm not Mommy's little girl anymore!"
        cassidy.say "God, you really bring out the bad girl in me!"
    return

label cassidy_movie_disliked_reaction_male:
    cassidy.say "Urgh...that movie sucked - what a waste of my time!"
    return

label cassidy_movie_indifferent_reaction_male:
    cassidy.say "I was SO bored in there - I was on my phone almost the whole time!"
    return

label cassidy_movie_liked_reaction_male:
    cassidy.say "Oh my god - that was so great, it makes me want to cry just remembering it!"
    return

label cassidy_belly_kiss_male:
    show cassidy at center, zoomAt(1.25, (640, 880))
    "I keep sneaking a look at Cassidy's belly whenever I get the chance."
    "And whenever I do, I feel a sensation of excitement deep inside of me."
    "Like a little jolt of electricity in my belly inspired by what it means."
    "The craziness of the idea that we're going to be parents!"
    show cassidy annoyed
    cassidy.say "[hero.name]…"
    cassidy.say "What are you looking at?"
    show cassidy sad
    "Cassidy's question catches me off-guard."
    "And so I look up at her with a confused expression on my face."
    "The surprise ensuring that my answer is totally honest."
    mike.say "Oh..."
    mike.say "I was just thinking about how good you look, Cassidy."
    mike.say "So good that I really want to kiss you!"
    show cassidy normal
    "Obviously, the admission delights Cassidy."
    "Her face lights up and she almost claps her hands at the idea."
    show cassidy happy
    cassidy.say "Well what are you waiting for, [hero.name]?"
    cassidy.say "After all, you already got me pregnant."
    cassidy.say "So it's not like you need permission to kiss me!"
    show cassidy normal
    "I nod in agreement, already preparing myself to do the honours."
    show cassidy at center, traveling(2.0, 0.5, (640, 980))
    "And as I lean in closer, Cassidy purses her lips and closes her eyes."
    "But when I get on a level with her mouth, I keep right on going."
    "Cassidy opens one eye, clearly wondering what in the hell is happening."
    show cassidy at center, traveling(2.0, 0.5, (640, 980))
    "Which means that she's just in time to see me planting my lips on the curve of her belly."
    show cassidy angry
    cassidy.say "[hero.name]…"
    cassidy.say "What are you doing down there?!?"
    cassidy.say "You know very well that my lips are up here!"
    "I keep on kissing Cassidy's belly all the time she's saying this."
    "And once I'm done, I sit up again, shrugging my shoulders."
    mike.say "I'm sorry, Cassidy..."
    mike.say "Your bump just looks so damn good."
    mike.say "I want to kiss it all the time!"
    show cassidy normal
    "Cassidy frowns and crosses her arms over her belly."
    "And as crazy as it sounds, she really does seem to be jealous of it!"
    cassidy.say "You're supposed to be paying attention to me, [hero.name]!"
    cassidy.say "I'm the one that you got into this state to begin with."
    cassidy.say "So I think it's the very least that you could do!"
    "Shake my head and smile, unable to believe Cassidy could be so jealous."
    "But then I lean in again, and this time I really do plant a kiss on her lips."
    "Because there's no sense in upsetting her."
    "Not when she's already carrying my baby."
    return

label cassidy_belly_caress_male:
    show cassidy at center, zoomAt(1.25, (640, 880))
    "I can hear Cassidy approaching long before I actually see her, the sound carrying way ahead of her."
    "It's a constant stream of gasps, sighs and even the occasional bout of moaning and cursing."
    "And so when she finally comes into view, it's no surprise to see that her face is red and frowning."
    "All it takes is a quick glance down at Cassidy's belly for me to be able to see what the problem is too."
    show cassidy annoyed
    cassidy.say "Urgh..."
    cassidy.say "Phew..."
    show cassidy angry
    cassidy.say "Damn it!"
    show cassidy upset
    "I mean, it's not the biggest bump that I've ever seen a pregnant woman carrying."
    "But from the way that Cassidy's holding her belly and hauling it around..."
    "Well you'd get the impression that it weighed a hundred pounds or more!"
    mike.say "Erm..."
    mike.say "Are you okay, Cassidy?"
    mike.say "You look like you could do with sitting down, or something."
    show cassidy sadsmile
    "At the sound of my voice, Cassidy suddenly looks up."
    "And it seems like she's almost embarrassed to that I can see her."
    "Because I swear she almost turns on her heel and runs away."
    "But I manage to take hold of her hand, preventing her from doing so."
    show cassidy surprised
    cassidy.say "Oh, [hero.name]…"
    cassidy.say "I really don't like you seeing me like this."
    show cassidy annoyed
    cassidy.say "It's so undignified!"
    show cassidy sadsmile at center, traveling(1.5, 0.5, (640, 1040))
    "I shake my head, already reaching out to put a hand on Cassidy's belly."
    mike.say "Don't say that, Cassidy."
    mike.say "There's nothing at all wrong with the way you look."
    mike.say "It's perfectly natural for a pregnant woman."
    mike.say "And I happen to think it looks pretty damn sexy!"
    "I make a point of caressing Cassidy's belly as I say all of this."
    "Stroking the curve with the palm of my hand and enjoying the warmth of it."
    "And I'm not just saying this for the sake of making her feel better either."
    "To me she really does look amazing right now, beautiful and full of life."
    show cassidy normal at center, zoomAt(1.5, (640, 1040))
    "Much to my relief, Cassidy's mood seems to improve a little."
    show cassidy happy
    "Because she smiles and shakes her head, giggling at my words."
    show cassidy normal
    cassidy.say "Oh, [hero.name]..."
    show cassidy happy
    cassidy.say "I never thought you were that kind of guy!"
    show cassidy normal
    "I can't help frowning as Cassidy says this."
    "Wondering what on earth she can mean."
    mike.say "Ah..."
    mike.say "What kind of guy, Cassidy?"
    mike.say "I thought I was just the regular kind."
    mike.say "Maybe with a little more going on than the average?"
    show cassidy happy at center, traveling(1.5, 0.5, (640, 1040))
    "Cassidy giggles again and pushes her belly towards me."
    cassidy.say "It's okay, [hero.name]..."
    cassidy.say "Lot's of guys like big girls!"
    show cassidy normal
    mike.say "Wha...what?!?"
    mike.say "I don't like big girls!"
    mike.say "I...I mean I have nothing against them."
    mike.say "I just don't like them more then other sizes of girl!"
    show cassidy wink
    "Cassidy nods and gives me a wink."
    cassidy.say "Of course not..."
    cassidy.say "Your secret's safe with me!"
    show cassidy normal
    mike.say "What secret?"
    mike.say "There isn't any secret!"
    "But no matter what I do, Cassidy just nods and smiles."
    return

label cassidy_belly_listen_male:
    show cassidy sad at center, zoomAt(1.25, (640, 880))
    mike.say "Cassidy..."
    mike.say "Would you come over here?"
    show cassidy normal
    "As soon as she hears me saying her name, Cassidy's mood picks up."
    show cassidy at center, traveling(1.5, 0.5, (640, 1040))
    "A smile spreads across her face as she hurries to do as I ask."
    show cassidy happy
    cassidy.say "Here I am, [hero.name]…"
    cassidy.say "What was it that you wanted?"
    show cassidy normal
    "It takes a moment for me to adjust myself to the way Cassidy's behaving."
    "And that's just because I'm not used to her being so eager to please."
    "Normally she's the one that's demanding attention."
    "And she's used to getting it too!"
    "I guess she must be feeling like the baby is getting more attention than she is."
    "But if that's the case, then I'm going to have to add to Cassidy's disappointment."
    mike.say "Just stand right there, Cassidy..."
    mike.say "Maybe stick your belly out a bit too?"
    show cassidy surprised
    "Cassidy looks more than a little puzzled."
    "But she does as I ask anyway."
    "Probably not wanting to pass up the chance for any attention she can get."
    show cassidy normal
    cassidy.say "Okay, [hero.name]..."
    cassidy.say "But why?"
    show cassidy at center, traveling(2.0, 0.5, (640, 980))
    "I'm already getting down onto one knee as she asks the question."
    "So I'm a little distracted as I offer an answer."
    "Because I'm more interested in putting my ear to her belly."
    mike.say "Oh, I want to listen to the baby, Cassidy."
    mike.say "You know, see if I can hear them moving around in there?"
    "Cassidy crosses her arms over her bump and frowns down at me."
    show cassidy angry
    cassidy.say "Oh, [hero.name]..."
    cassidy.say "I thought you wanted to shower me with attention for a change!"
    "All I can manage to do in way of a reply is to vaguely wave my hand in the air."
    "Because all of my attention is currently focussed on the task at hand."
    mike.say "Shhh!"
    cassidy.say "Hey!"
    cassidy.say "Don't you dare shush me!"
    cassidy.say "I'm not used to being talked to like..."
    cassidy.say "Wait a minute...why are you...can you..."
    show cassidy surprised
    cassidy.say "Can you actually hear something?"
    "I nod eagerly, already feeling totally energised by what my ears are picking up."
    mike.say "I totally can, Cassidy..."
    show cassidy normal
    mike.say "They're moving around in there..."
    mike.say "Swimming, I guess!"
    cassidy.say "Really?"
    cassidy.say "Aww..."
    show cassidy annoyed
    cassidy.say "I wish I could hear it too!"
    "I feel a sense of relief as Cassidy seems to get swept up in the moment too."
    show cassidy normal
    "A little but because it means that she's finally off my back."
    "But even more so because it shows that she's more interested in the baby than herself."
    "Which is a fact that gives me great hope for the future."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
