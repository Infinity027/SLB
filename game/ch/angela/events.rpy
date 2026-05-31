init python:
    Event(**{
    "name": "angela_bj_bruce",
    "label": "angela_bj_bruce",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDone("angela_visit"),
        Or(
            IsDone("bree_event_12"),   
            IsDone("bree_event_14b"),  
            ),
        HeroTarget(
            IsGender("male"),
            IsRoom("date_restaurant")),
        Or(
            PersonTarget(bree,
                OnDate(),
                IsFlag("breedelay", False),
                MinStat("love", 170),
                ),
            PersonTarget(minami,
                OnDate(),
                IsFlag("sisconDelay", False),
                MinStat("love", 180),
                ),
            ),
        MinDateScore(20),
        ],
    "do_once": True,
    "quit": False,
    })

label angela_bj_bruce:
    scene bg restaurant
    "Everything seems to be going well as we're shown to our table at the restaurant."
    if game.active_date.on_date(bree):
        $ game.flags.angelablow_datinggirl = "bree"
        show bree date
        "[bree.name] sits down and eagerly accepts a menu from the waiter."
        bree.say "Boy am I hungry, [hero.name]."
        bree.say "I feel like I could eat a horse!"
        show bree surprised
    elif game.active_date.on_date(minami):
        $ game.flags.angelablow_datinggirl = "minami"
        show minami date
        "Minami happily lets the waiter pull out her seat and accepts a menu."
        minami.say "Ooh..."
        minami.say "This place is pretty fancy, big bro!"
        show minami hunt
    show fx exclamation
    "But then I see her eyes go wide with surprise."
    "And she holds the menu up to cover her face."
    mike.say "Huh?!?"
    mike.say "What's the matter?"
    if game.active_date.on_date(bree):
        bree.say "Over there - in the corner."
        bree.say "It's my Dad!"
    elif game.active_date.on_date(minami):
        minami.say "Over there, in the corner."
        show minami annoyed
        minami.say "It's Mom - and she's with some guy that's not Dad!"
    "I know that I should be showing the same discretion as she is right now."
    "But you know how it is - the second I hear those words, my head turns around."
    "I see the table in question and the two people sitting at it."
    "And I can't help being surprised too."
    mike.say "Wait a minute..."
    if game.active_date.on_date(bree):
        mike.say "That's my Mom!"
        bree.say "What's she doing on a date with my Dad?!?"
    elif game.active_date.on_date(minami):
        mike.say "That's [bree.name]'s dad!"
        minami.say "What's he doing on a date with our Mom?!?"
    "I shake my head, trying to make sense of what I'm seeing."
    "Sure, it looks pretty suspicious from where we're sitting."
    "But for all we know, there could be a perfectly innocent explanation."
    mike.say "We...we don't know they're on a date, right?"
    mike.say "I mean, they could be having a business meeting."
    mike.say "They could just be old friends without either of us knowing."
    "As if in answer to my question, the waiter walks over to their table."
    "He then proceeds to light a candle and pour them each a glass of wine."
    "And as soon as he's gone, they lean in closer, holding hands and smiling at each other."
    mike.say "Okay, okay..."
    mike.say "So they ARE on a date!"
    if game.active_date.on_date(bree):
        show bree sad
        bree.say "But why, [hero.name]?"
        bree.say "How did they even meet up?"
    elif game.active_date.on_date(minami):
        show minami scared
        minami.say "But why, [hero.name]?"
        minami.say "Oh no - does this mean Mom and Dad are getting a divorce?!?"
    mike.say "How should I know?"
    mike.say "Look, let's just keep an eye on them, see what happens."
    if game.active_date.on_date(bree):
        show bree angry
        "[bree.name] sets her face in a serious expression and nods."
        "Then she returns to hiding behind her menu."
    elif game.active_date.on_date(minami):
        show minami normal
        "Minami nods and tries her best to look serious."
        "But I can easily tell that she's still anxious."
    "For a while we manage to stick to the plan."
    "We order our meals and try to look natural."
    "But neither of us can help stealing glances in my Mom and Bruce's direction."
    "Nothing seems to chance until my Mom gets up from her seat and walks away."
    "No need to panic though, as it looks like she's just going to the bathroom."
    if game.active_date.on_date(bree):
        show bree surprised
        bree.say "Huh!"
        bree.say "Looks like my Dad needs to pee too!"
    elif game.active_date.on_date(minami):
        show minami hunt
        minami.say "Huh!"
        minami.say "Look's like [bree.name]'s dad needs to pee too!"
    "I glance up to see Bruce getting out of his chair too."
    "But as he reaches the door to the men's room, he changes direction."
    "I see him slip into the ladies room without anyone else seeming to notice!"
    menu:
        "Follow them":
            "Almost the same second the door closes behind Bruce, I'm on my feet."
            mike.say "Come on - what are you waiting for?"
            if game.active_date.on_date(bree):
                bree.say "Y...you want to follow them?!?"
            elif game.active_date.on_date(minami):
                minami.say "Y...you want to follow them?!?"
            mike.say "Of course I want to follow them!"
            mike.say "They could be getting up to anything in there."
            mike.say "I mean, it's not like the men's room is out of order!"
            "Her eyes go wide with surprise as I say this."
            if game.active_date.on_date(bree):
                show bree sad
                bree.say "You don't mean..."
            elif game.active_date.on_date(minami):
                show minami scared
                minami.say "Eww!"
                minami.say "Mom would never..."
            mike.say "Why else would he go in there?!?"
            if game.active_date.on_date(bree):
                hide bree
                "[bree.name] hops out of her seat and follows me to the ladies room."
            elif game.active_date.on_date(minami):
                hide minami
                "Minami hops out of her seat and follows me to the ladies room."
            "I lead the way, sneaking inside as quietly as I can."
            "The whole time I'm praying that nobody's seen us."
            "Once we're inside, I notice only one cubicle's occupied."
            "Together we tiptoe to the cubicle next door and stand on the toilet."
            "From there we get a perfect view into the occupied cubicle."
            "And we see a scene that'll be forever burned into my memory."
            scene angela breedad bj
            show angela breedad bj mike closed blowjob
            if game.active_date.on_date(bree):
                show angela breedad bj bree
            elif game.active_date.on_date(minami):
                show angela breedad bj minami
            "Bruce is standing there, pants down around his ankles."
            "My Mom is on her knees in front of him."
            "And she's in the middle of giving him a pretty intense blowjob!"
            if game.active_date.on_date(bree):
                "Almost without thinking, I clap a hand over [bree.name]'s mouth."
            elif game.active_date.on_date(minami):
                "Almost without thinking, I clap a hand over Minami's mouth."
            "This means that she only manages to make a few muffled sounds of alarm."
            "And luckily for us, Bruce and my Mom are seriously distracted right now!"
            "Trying to keep from making a sound, we retreat back to our table."
            $ game.flags.angelaBlow = True
        "Don't follow them":
            if game.active_date.on_date(bree):
                show bree angry
                bree.say "Come on, [hero.name]."
                bree.say "We gotta follow them!"
            elif game.active_date.on_date(minami):
                show minami normal
                minami.say "Come on, big bro."
                minami.say "We gotta follow them!"
            "She's already halfway out of her seat as she says this."
            "But I reach out and put my hand on her wrist."
            show fx question
            "She turns her head in my direction, looking puzzled."
            mike.say "We can't follow them."
            mike.say "One guy going into the ladies room looks dodgy."
            mike.say "But two will look like we're stating an orgy in there!"
            "Her eyes go wide with surprise as I say this."
            if game.active_date.on_date(bree):
                show bree sad
                bree.say "You don't mean..."
            elif game.active_date.on_date(minami):
                show minami scared
                minami.say "Eww!"
                minami.say "Mom would never..."
            mike.say "Why else would he go in there?!?"
            mike.say "It's not like there's a queue for the men's room!"
    scene bg restaurant
    if game.active_date.on_date(bree):
        show bree date normal
    elif game.active_date.on_date(minami):
        show minami date normal
    "We do the best we can to get back to our meal."
    "But by now we're both more interested in Bruce and my Mom."
    "After a while, Bruce slips out of the ladies room and back to his seat."
    "My Mom appears a few minutes later, looking a little dishevelled."
    "They seem to have lost their appetites, or maybe sated them."
    "As they ask for the bill and leave pretty quickly."
    "Once they're gone, we hunch together over the table."
    mike.say "We need to get to the bottom of this, yeah?"
    if game.active_date.on_date(bree):
        show bree normal
        bree.say "Agreed."
    elif game.active_date.on_date(minami):
        show minami normal
        minami.say "You got it, big bro!"
    "We nod to each other, sealing the deal."
    "But I can't help wondering just what we're going to discover."
    return

init python:
    InteractEvent(**{
    "name": "ask_bruce_number",
    "label": "ask_bruce_number",
    "priority": 500,
    "duration": 1,
    "conditions": [
        IsDone("angela_bj_bruce"),
        GameTarget(IsFlag("angelaBlow", True)),
        HeroTarget(
            IsGender("male"),
            Not(OnDate())),
        PersonTarget(bree,
            IsActive(),
            ),
        ],
    "quit": False,
    })

label ask_bruce_number:
    "Sure, I can call my Mom and question her about what I saw at the restaurant the other night."
    "But maybe the person I should really be calling about this is [bree.name]'s dad himself?"
    "After all, it might help to hear both sides of the story before I decide who's to blame."
    "The only problem is that I obviously don't have Bruce's number."
    "And the only person that I can ask for it is [bree.name]."
    if game.flags.angelablow_datinggirl == "bree":
        "So I figure I'd better just come out and ask."
        mike.say "[bree.name], can I get your Dad's number?"
        show bree dazed
        bree.say "You mean you want to call him about what we saw?"
        bree.say "Don't you think I should be the one to do that?"
        mike.say "No, [bree.name] - I want to ask him myself, man to man."
        "[bree.name] frowns at me, raising one eyebrow."
        "She doesn't look very convinced."
        bree.say "You sure you want to do this, [hero.name]?"
        bree.say "I didn't think you guys got on that well!"
        mike.say "No way, [bree.name]!"
        mike.say "That's all just guy stuff, pretending not to like each other!"
        "[bree.name] looks as though she's going to say no."
        show bree normal
        "But then she shrugs and shakes her head."
        bree.say "Whatever you say, [hero.name]."
        bree.say "Here you go..."
        $ game.flags.bruceNumber = True
    else:
        "I figure I'd better just come out and ask."
        mike.say "Ah, [bree.name]..."
        bree.say "Huh?"
        bree.say "What's up, [hero.name]?"
        mike.say "Could I get your dad's number?"
        show bree annoyed
        "[bree.name] frowns at me, raising one eyebrow."
        bree.say "What the hell for?"
        bree.say "I didn't think you guys got on that well!"
        mike.say "No way, [bree.name]!"
        mike.say "That's all just guy stuff, pretending not to like each other!"
        if hero.charm >= 60:
            "[bree.name] looks as though she's going to say no."
            show bree normal
            "But then she shrugs and shakes her head."
            bree.say "Whatever you say, [hero.name]."
            bree.say "Here you go..."
            $ game.flags.bruceNumber = True
        else:
            "[bree.name] thinks about it for a moment."
            "Then she shakes her head."
            bree.say "I don't think so, [hero.name]."
            bree.say "He'll kick your ass - and I don't want that on my conscience!"
    return

label angela_afterblow_call:
    "I don't leave it too long before I pick up the phone and call my Mom."
    "I mean, not the very moment that we left the restaurant where we saw her."
    "Just long enough for me to clear my head and figure what I want to ask her."
    "And maybe long enough for her to think that she got away with the whole thing too."
    "As usual, it doesn't take long for her to pick up when I call."
    mike.say "Hey, Mom..."
    angela.say "Hi there, sweetie!"
    angela.say "How nice of you to call me."
    angela.say "Was there something you needed?"
    angela.say "Or did you just want to talk to your mom?"
    "I take a deep breath, steeling myself for what's coming next."
    "There's no point in beating about the bush."
    "So I just come straight out and ask the question."
    mike.say "Well...there was one thing, Mom."
    mike.say "I was eating out the other night."
    mike.say "And I saw you there - eating someone out."
    mike.say "I mean eating out with someone!"
    "There's a pause on the other end of the line."
    "And I can almost hear my Mom's mind racing."
    "But when she finally speaks, I'm taken by surprise."
    angela.say "Oh, no - that couldn't have been me, sweetie."
    angela.say "I wasn't at any restaurant."
    angela.say "I was right here, at home with your father."
    mike.say "Huh?"
    mike.say "I never said it was at a restaurant, Mom!"
    mike.say "We could have been at a cafe, a hotdog stand, even grabbing a burger at the pub."
    mike.say "Why would you mention a restaurant?"
    angela.say "Oh...no reason, sweetie."
    angela.say "It's just like a turn of phrase - you know?"
    angela.say "Anyway, it doesn't really matter, does it?"
    angela.say "Because I already told you I wasn't there."
    angela.say "I wasn't there, wherever there is, okay?"
    "My Mom's explanation leaves me far from convinced."
    "Either Bruce was getting a blowjob from her long-lost twin sister."
    "Or else she's lying like crazy in an effort to cover her tracks."
    "But if she's not going to admit it, then what can I do?"
    "I don't want to come out and accuse her of being a cheat and a liar."
    "So for the time being, I decide to play along."
    mike.say "Okay, Mom."
    mike.say "If that's your story, then I believe you."
    mike.say "I didn't think it was you."
    mike.say "But I just wanted to be sure."
    angela.say "Of course, Sweetie."
    angela.say "You can call me up anytime, remember that!"
    mike.say "Sure thing, Mom."
    "I end the call and can't help shaking my head in confusion."
    "That call was supposed to clear things up for me, to explain what's going on."
    "But now I have more questions than I did when I started down this rabbit-hole!"
    $ game.flags.angelaBlow = False
    $ angela.flags.complete = True
    return

label angela_afterblow_dad_call:
    "I don't want to have to do it, but I don't see how I can avoid it either."
    "That's why I end up calling my Dad after seeing my Mom and Bruce at the restaurant."
    "I have no idea how he's going to react to the news."
    "But he's got a right to know what's going on behind his back."
    mike.say "Ah..."
    mike.say "Hey, Dad!"
    "Dad" "Hey there, son!"
    "Dad" "To what do I owe this honour?"
    "Dad" "You only usually call me when you need something!"
    "I can't help letting out a nervous laugh at this."
    "And my Dad seems to take that as confirmation of his suspicions."
    "Dad" "Hah - I knew it!"
    "Dad" "Come on, [hero.name] - out with it."
    "Dad" "I'm always going to be there to help out my only son!"
    mike.say "No, Dad..."
    mike.say "It's not like that, honestly."
    mike.say "I have something to tell you, something you need to know."
    "My Dad goes quiet for a moment."
    "And when he speaks, his voice has taken on a more serious tone."
    "In fact it's one that I remember well from when I was a kid!"
    "Dad" "Well that's different, son."
    "Dad" "What do you need to tell me?"
    mike.say "I...I was at a restaurant the other night, Dad."
    mike.say "And Mom was there too...with another guy!"
    "I hear my Dad let out a sigh on the other end of the line."
    "Which is weird, as I was expecting him to get mad any moment."
    "Dad" "Yeah, son..."
    "Dad" "I know about all of that."
    "For a moment I can't actually process what he just said."
    "It's like closing your eyes, expecting to be slapped in the face."
    "And then experimentally opening them again when the blow doesn't land."
    mike.say "Huh?"
    mike.say "What do you mean you already know?!?"
    "Dad" "Your mom already told me, son."
    "Dad" "She confessed and I forgave her."
    mike.say "But, Dad..."
    mike.say "She was on a date with my housemate's dad!"
    mike.say "They went into the bathroom together and..."
    "Dad" "Okay, son, okay!"
    "Dad" "I know all the details already!"
    "I hear my Dad sigh again."
    "And I can picture him shaking his head as he does so."
    "Dad" "Look, son, it's really not that serious."
    "Dad" "Your mom apologised and we're working it through."
    "Dad" "We've been together a long time, and occasionally you mess up."
    "Dad" "Nobody's perfect, but our relationship's stronger than this, okay?"
    mike.say "If you say so, Dad."
    mike.say "I was worried, that's all."
    "Dad" "Well don't be."
    "Dad" "Just remember that your mom and I love you."
    "Dad" "And we love each other too."
    "I wrap up the call with my Dad, trying to sound reassured."
    "But something still keeps nagging at the back of my mind."
    "I push it away as best I can, hoping that I'm wrong and he's right."
    $ game.flags.angelaBlow = False
    $ angela.flags.complete = True
    return

label angela_afterblow_bruce_call:
    "As soon as I'm alone, I make the call."
    "The phone rings a few times, then he picks up."
    breesdad "I don't recognise this number!"
    breesdad "Who in the hell's calling me?"
    mike.say "Ah, hey, Bruce - it's [hero.name] here."
    breesdad "[hero.name] who?"
    breesdad "I don't know any fucking [hero.name]!"
    mike.say "I'm [bree.name]'s housemate - remember?"
    breesdad "Oh, THAT [hero.name]!"
    breesdad "So what do you want?"
    breesdad "And now that I think about it - who gave you my damn number?"
    "I try to ignore the threatening tone of voice Bruce is using."
    "And instead I focus on the real reason for calling him."
    mike.say "I saw you at the restaurant the other night, Bruce."
    mike.say "I saw you there with my Mom!"
    if hero.charm >= 80:
        breesdad "You got a lot of nerve calling me, kid."
        breesdad "Especially after what your crazy mom did to me!"
        "That wasn't the answer I was expecting."
        "And it throws me off balance."
        mike.say "Wh...what do you mean?"
        mike.say "My Mom's not crazy!"
        "I hear Bruce laugh on the other end of the line."
        breesdad "Sounds like you don't know the half of it!"
        breesdad "Okay, buddy, I'll level with you."
        breesdad "Sure, I took your mom out on a date."
        breesdad "I mean, why wouldn't I?"
        breesdad "She's pretty hot!"
        breesdad "But she called it off the next day - dumped me by text message!"
        "I can't help letting out a sigh of relief at this news."
        "And unfortunately, Bruce hears it too."
        breesdad "Yeah, yeah - laugh it up kid."
        breesdad "She was bad company anyway."
        breesdad "All she wanted to do was pump me for info on [bree.name] too!"
        "For the second time I'm surprised to hear what Bruce has to say."
        mike.say "She was asking you about [bree.name]?"
        mike.say "Why would she do that?"
        breesdad "Beats me, kid!"
        breesdad "She kept on asking though!"
        breesdad "Said something about needing to know if she was 'wife material' for you!"
        breesdad "Like my little girl could ever be right for a loser like you!"
        mike.say "Ah, yeah...thanks, Bruce."
        "I end the call there, as Bruce doesn't offer up anything else."
        "And I already have enough info to make my mind race at the possibilities."
        "Why would my Mom go behind my Dad's back and then dump Bruce the next day?"
        "Did she realise that she'd done something wrong and have an attack of the guilts?"
        "And then there's the matter of her quizzing the guy about [bree.name]."
        "Why would she be so interested in whether one of my housemates would make a good wife?"
    else:
        "Before I can say another word, Bruce cuts me off."
        breesdad "Aw no, no way!"
        breesdad "I already had my fill of your crazy mom."
        breesdad "You can both keep the hell away from me!"
        "And with that, he ends the call."
        "Which leaves me with more questions than before!"
    $ game.flags.angelaBlow = False
    $ angela.flags.complete = True
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
