label lexi_greet_dialogues_female:
    $ result = randint(1, 3)
    if result == 1:
        bree.say "Hello, Lexi."
    elif result == 2:
        bree.say "Hi."
    else:
        if game.hour < 6:
            bree.say "Hello Lexi."
        elif game.hour < 12:
            bree.say "Good morning Lexi."
        elif game.hour < 19:
            bree.say "Good afternoon Lexi."
        else:
            bree.say "Good evening Lexi."
    return

label lexi_kiss_reaction_female:
    if lexi.lesbian < MIN_LES_GIRL_SEX:
        $ lexi.lesbian += 1
    return


label lexi_kiss_female:
    scene expression f"bg {game.room}"
    if lexi.love + hero.charm < 80 and not lexi.is_girlfriend and not game.active_date.score >= 75:
        show lexi
        "I leaned in to kiss Lexi, not sure what I was expecting to happen but as soon as she caught wind of this, Lexi pushed me away forcefully."
        "As I recover my balance back I met with a very upset gaze from Lexi."
        lexi.say "[hero.name], just what the fuck you think you're doing?"
        "I stop their dumbfounded, clearly I was reading the situation wrong, but seeing my confusion Lexi took a deep breath and calmed down."
        lexi.say "Look... I like you, but not that much... not yet, just... let take things slow alright? I'm not a cheap slut you know..."
        "I smile nervously back at her and reply."
        bree.say "Y-Yeah...sorry, I don't know what I was thinking heh..."
        "Better luck next time."
        $ lexi.love -= 1
        hide lexi
    elif not lexi.flags.kiss:
        "Something just came over me, one moment I was looking at Lexi talking, her golden hair, her smile, her....everything."
        "She was talking to me and yet all I can focus on was her lips..."
        "And how I wanted them pressed against mine, before I knew it I was leaning in close."
        hide lexi
        call lexi_kiss_reaction_female from _call_lexi_kiss_reaction_female
        show lexi kiss
        "Taking her by surprise I kissed her with all the passion I could muster, Lexi's eyes are wide open but slowly she leans in and kiss me back."
        "And to my surprise, she didn't resist, kissing me back with a burning passion as she slid her tongue into my mouth."
        "I held her closer, her soft breast pressed against mine as we shared.. our first passionate kiss together."
        "We both broke the kiss together, longing for more, I wanted to say something but before I could this sexy Minx beat me to it."
        hide lexi kiss
        show lexi
        lexi.say "Heh...took you long enough babe..."
        "I smile back, this was one of many mores to come."
        $ lexi.flags.kiss += 1
        $ lexi.love += 5
    else:
        "It was just an ordinary day, me and Lexi were just chilling and in each other's embrace."
        "I felt her warmth as her hand interlocked with mine, while her other hand was playfully scratching my hips."
        hide lexi
        call lexi_kiss_reaction_female from _call_lexi_kiss_reaction_female_1
        show lexi kiss
        "I buried my face in her neck, planting small and quick kisses, making her giggle, fuck I love her laugh..."
        "Then I started feeling a bit adventurous, I pulled her in closer, as my lips slowly moved up with the kisses from her neck to her soft cheeks."
        "As I turn her face to look at mine, I see this beautiful girl smiling back at me, something tells me she already know whats coming, and she's all for it."
        "Not a word is said, as I lean in to kiss those lips, her soft, tender beautiful lips."
        "Lexi doesn't spare any passion and invite her tongue into my mouth as I do the same, both of us lost in the moment and even more in the passion we have for each other."
        "I close my eyes and let her take the lead, but not without giving her exactly what she wants from me, as we devour each other in a passionate, hot kiss."
        "None of us wants to break the kiss but eventually I pull back, her taste still linger on my lips as we smile to each other and enjoying our time together."
        $ lexi.love += 2
        $ lexi.flags.kiss += 1
    return

label lexi_ask_date_female:



    call lexi_ask_date_alone_female from _call_lexi_ask_date_alone_female
    return _return

label lexi_ask_date_alone_female:
    bree.say "Ah..."
    bree.say "Lexi..."
    bree.say "You maybe want to..."
    bree.say "I don't know..."
    lexi.say "What are you talking about, [hero.name]?"
    lexi.say "Spit it out already!"
    bree.say "You wanna go on a date with me?!?"
    bree.say "Urgh..."
    bree.say "There...I said it!"
    if lexi.love < 50 or lexi.flags.nodate:
        lexi.say "Erm...no."
        lexi.say "I think we need to keep things casual, [hero.name]."
        lexi.say "Otherwise things are going to get messy."
        $ date_choice = False
    else:
        lexi.say "Oh wow... yeah, [hero.name]..."
        lexi.say "We should definitely do that!"
        lexi.say "What a great idea!"
        $ date_choice = True
    return date_choice

label lexi_pregnancy_congratulations:
    "Lexi seems to notice the difference in me straight away."
    "And true to form, she's not exactly shy about admitting it either!"
    show lexi surprised
    lexi.say "Oops!"
    show lexi wink
    lexi.say "Looks like someone had an accident, [hero.name]!"
    lexi.say "What happened - condom tear on you?"
    "I do the best I can to put a smile on my face."
    "But I'm not used to someone asking me that kind of question."
    bree.say "Ah..."
    bree.say "Not exactly, Lexi..."
    show lexi normal
    "Lexi seems to sense the effect her question's had on me."
    "And her attitude softens as a result."
    lexi.say "What I meant to say was congratulations!"
    show lexi happy
    lexi.say "Obviously..."
    lexi.say "Nearly been there myself more than once."
    lexi.say "But with me, it really was an accident!"
    bree.say "Erm..."
    bree.say "Thanks, Lexi."
    bree.say "I think..."
    $ lexi.love += 1
    return

label lexi_propose_female:
    show lexi a
    "You know I never really saw myself as the goodie goodie type of girl."
    "Sure, I kept mainly to the rules when I was younger."
    "But then my dad was always a real hard-ass, so what choice did I have?"
    "Yet I still did all the little things that made me feel rebellious."
    "I smoked a few cigarettes, and then moved on to smoking other stuff..."
    "And I kind of flattered myself that I was a bad girl in all the ways that mattered."
    show lexi a bubblegum
    "But that was before I met Lexi and she became a part of my life."
    "When that happened, I had a rude awakening."
    "Because I found out what a bad girl looked like for real!"
    "And what's even weirder is that I found I didn't want to be one."
    "What I actually wanted was to be with one!"
    show lexi a -bubblegum
    "At first I thought that I was just enjoying the chance to hang out with Lexi."
    "Then I realised that when we weren't together, I was thinking about her."
    "Thinking about the next time that we could be together."
    "Luckily for me, I soon discovered that Lexi fells the same way too."
    show lexi a bubblegum
    "At least I think she does."
    "What scares me is that she might just think that what we have is casual."
    "That it's just a little fun between two girls that are more than friends."
    show lexi a -bubblegum
    "So there's two reasons that I'm about to ask her the question."
    "On the one hand, I need to know if she feels the same way as me."
    "And on the other, I want to take our relationship to the next level."
    "Whatever happens and whatever her answer is, I just have to know."
    show lexi nophone at center, zoomAt(1.5, (640, 1040)) with fade
    "So as soon as the chance presents itself, I jump on it."
    lexi.say "What's bugging you, [hero.name]?"
    show lexi wink
    lexi.say "You look like me trying to do hard maths in my head!"
    show lexi normal
    bree.say "Oh..."
    bree.say "Yeah, Lexi..."
    bree.say "I have got something on my mind right now."
    lexi.say "Well what are you waiting for?"
    lexi.say "A problem shared is a problem halved."
    show lexi happy
    lexi.say "Isn't that what they say?"
    "I nod and do the best I can to smile."
    show lexi normal
    "But the truth is that I can feel my guts tying themselves in knots."
    "Okay, here goes..."
    bree.say "Lexi..."
    bree.say "I always have the best time when we're together."
    bree.say "Like, you're the most amazing girl that I've ever dated."
    show lexi yawn blush
    lexi.say "Aww..."
    show lexi happy
    lexi.say "Thanks, [hero.name]!"
    show lexi wink
    lexi.say "You're not too bad yourself."
    show lexi normal -blush
    bree.say "But what I'm trying to say is that..."
    bree.say "I...want more, Lexi!"
    show lexi flirt
    "Lexi grins and jabs me in the ribs with her elbow."
    lexi.say "Oh-oh!"
    lexi.say "You wanna spice things up, huh?"
    lexi.say "What did you have in mind, you little minx?"
    lexi.say "Toys?"
    lexi.say "Ropes?"
    lexi.say "More bodies?"
    "I can feel my cheeks flushing more with each suggestion."
    "And I'm afraid that Lexi's steering the conversation away from my intended goal."
    "In the heat of the moment, all I can think to do is blurt it out."
    show lexi normal
    bree.say "Lexi..."
    show lexi surprised
    bree.say "Will you marry me?"
    if lexi.love < 195:

        show lexi happy at startle
        lexi.say "Ha ha!"
        lexi.say "Good one, [hero.name]."
        lexi.say "You almost had me going for a minute there!"
        "I'm too ramped up on nervous energy to really get what Lexi means at first."
        "Instead I just end up staring at her without saying a word in response."
        show lexi normal
        "Luckily for me, she seems to take this as me being offended at her reaction."
        show lexi yawn
        lexi.say "Oops..."
        show lexi sad
        lexi.say "You're not joking, are you?"
        bree.say "Nope..."
        bree.say "More like opening up my heart, Lexi!"
        "My words really seem to have an effect on Lexi."
        "Which isn't the reaction that I was expecting."
        "Normally she'd be dismissive of another person's feelings."
        "But this time she seems to get the sincerity behind what I just said."
        lexi.say "Urgh..."
        lexi.say "Well this is fucking awkward."
        bree.say "Yeah..."
        bree.say "You could say that."
        lexi.say "Look, [hero.name]..."
        lexi.say "I'm sorry, okay?"
        lexi.say "I shouldn't have said all of that shit."
        lexi.say "But I think it means we're pretty far apart on that issue."
        "I want to argue with what Lexi's saying."
        "To tell her that she's wrong and we can make it work."
        "But I know that she's just being honest."
        "So I don't have any choice but to do the same."
        bree.say "I guess so, Lexi."
        bree.say "We've got some stuff to work out between us."
        lexi.say "We sure do."
        $ lexi.love -= 25
    else:

        lexi.say "[hero.name]..."
        lexi.say "Are you fucking joking with me?"
        "I blink in surprise at Lexi's response."
        "And the only thing that I can think to do is shake my head at first."
        "But then I find my voice too."
        bree.say "No!"
        bree.say "Of course not, Lexi..."
        bree.say "I'm opening up my heart to you right now!"
        lexi.say "Oh..."
        show lexi happy blush
        show fx heart
        lexi.say "In that case, yeah."
        "I'm too ramped up on nervous energy to really get what Lexi means at first."
        "Instead I just end up staring at her without saying a word in response."
        show lexi normal
        lexi.say "Hey, [hero.name]!"
        lexi.say "Did you hear me?"
        lexi.say "I said yes!"
        "Suddenly I snap out of it."
        "All of that nervous energy is transformed into elation."
        "And I feel like I'm going to pass out from the excitement."
        bree.say "Oh fuck!"
        bree.say "You said yes!"
        show lexi happy
        lexi.say "That's right, [hero.name]."
        show lexi normal
        lexi.say "And it sounds like this is going to be a riot."
        lexi.say "You know that I never married a girl before?"
        show lexi annoyed
        lexi.say "Well...at least not that I know of!"
        bree.say "Huh..."
        bree.say "What was that, Lexi?"
        show lexi happy
        lexi.say "Ah, never mind, [hero.name]!"
        lexi.say "Come on, we've got a wedding to plan!"
        $ lexi.set_fiance()
    hide lexi
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
