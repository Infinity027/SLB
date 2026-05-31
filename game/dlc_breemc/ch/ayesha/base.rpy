label ayesha_greet_dialogues_female:
    $ result = randint(1, 3)
    if result == 1:
        bree.say "Hello, Ayesha."
    elif result == 2:
        bree.say "Hi."
    else:
        if game.hour < 6:
            bree.say "Hello Ayesha."
        elif game.hour < 12:
            bree.say "Good morning Ayesha."
        elif game.hour < 19:
            bree.say "Good afternoon Ayesha."
        else:
            bree.say "Good evening Ayesha."
    return

label ayesha_kiss_reaction_female:
    if ayesha.lesbian < MIN_LES_GIRL_SEX:
        $ ayesha.lesbian += 1
    return

label ayesha_ask_date_female:



    call ayesha_ask_date_alone_female from _call_ayesha_ask_date_alone_female
    return _return

label ayesha_kiss_female:
    scene expression f"bg {game.room}"
    if ayesha.love < 25 and not ayesha.is_girlfriend and not game.active_date.score >= 75:
        show ayesha
        "I feel like I have to summon all of my courage to make the first move."
        "But there's just no way that I can hold back any longer."
        "I have to try to kiss Ayesha - and it has to be now!"
        "But the moment I lean in to plant one on her lips, Ayesha spots me."
        show ayesha at startle
        "She jerks her head back, meaning that I miss my target and almost fall over!"
        "Ayesha recovers more quickly, making it look like nothing's amiss."
        "But I can already feel my cheeks starting to burn with embarrassment."
        "And that's nothing compared to the emotions churning away in my gut!"
        $ ayesha.love -= 5
        $ ayesha.sub -= 5
        hide ayesha
    elif not ayesha.flags.kiss:
        hide ayesha
        $ ayesha.love += 5
        call ayesha_kiss_reaction_female from _call_expression_451
        show ayesha kiss with dissolve
        "I can't hold back any longer, I feel like I'll go mad if I do!"
        "So I summon up all of my courage and lean in to kiss Ayesha."
        "I'm expecting her to pull away any moment, and she stiffens as our lips meet."
        "But that only lasts for a moment, and then I feel her resistance melt away."
        "Before I can get a handle on what's happening, Ayesha's kissing me back!"
        "I thought this would relieve the tension I've been feeling around her."
        "But now I can feel a whole new level of desire and need building inside of me!"
        "And I know that one kiss is never going to be enough!"
        hide ayesha kiss with dissolve
        $ ayesha.flags.kiss += 1
    else:
        hide ayesha
        $ ayesha.love += 2
        call ayesha_kiss_reaction_female from _call_expression_452
        show ayesha kiss with dissolve
        "Every time Ayesha kisses me, it feels even more natural than before."
        "It's not like being kissed by a man that towers over me."
        "Even though there is a thrill to being kissed by an Amazon!"
        "Ayesha kisses me with a tenderness that belies the size of her frame."
        "And I find myself falling into her arms more easily every time."
        "Pretty soon all she has to do is look at me in a certain way."
        "Or give me one of those smiles..."
        "And I'm like putty in her hands!"
        hide ayesha kiss with dissolve
        $ ayesha.flags.kiss += 1
    return

label ayesha_beats_ryan_female:
label ayesha_beats_scottie_female:
label ayesha_beats_jack_female:
label ayesha_beats_shawn_female:
label ayesha_beats_mike_female:
label ayesha_beats_danny_female:
label ayesha_beats_dwayne_female:
label ayesha_beats_victor_female:
label ayesha_beats_master_female:
    if randint(1, 100) <= 20:
        return "abort"
    "I can feel his lips against mine, his hands all over me."
    "I know that I should be stopping him, but it's so hard to resist!"
    ayesha.say "What the..."
    ayesha.say "Oh no, oh hell no!"
    scene bg black
    $ renpy.show(f"bg {game.room}")
    show ayesha casual angry zorder 10 at right5
    "At the sound of Ayesha's voice, he releases me from his grip."
    $ renpy.show(f"{active_girl.id} angry", at_list=[zoomAt(power=1, xypos=(-500, 0))])
    $ renpy.show(f"{active_girl.id} angry", at_list=[traveling (1.0, 0.5, (50, 0))])
    "I gasp and look around to see her standing there, visibly seething."
    bree.say "Ayesha, I..."
    "But before I can try to explain myself, Ayesha cuts me off."
    ayesha.say "No need to explain a thing, [hero.name]..."
    ayesha.say "Just leave this creep to me!"
    "I can't help gasping in surprise at Ayesha."
    "She looks steely, determined and downright manly right now!"
    "Well...I mean womanly, I guess..."
    "Call me shallow, but she's really impressing me!"
    if active_girl.id == "ryan":
        ryan.say "Who are you supposed to be, gigantor?"
        ryan.say "Andrea the Giant?!?"
    elif active_girl.id == "jack":
        jack.say "Whoa!"
        jack.say "Are you, like, a real wrestler?"
        jack.say "Or one of those pretend ones you see on TV?"
    elif active_girl.id == "shawn":
        shawn.say "Huh?"
        shawn.say "Where did she come from?"
        shawn.say "I should warn you, I will hit a girl in self-defence!"
    elif active_girl.id == "mike":
        mike.say "You're Ayesha!"
        mike.say "I know you from the gym..."
        mike.say "You know [hero.name] too, huh?"
    elif active_girl.id == "danny":
        danny.say "Oh man!"
        danny.say "You have to be the biggest chick I ever saw!"
        danny.say "Do you like, arm-wrestle and all that stuff?"
    elif active_girl.id == "scottie":
        scottie.say "Oh wow!"
        scottie.say "This chick's got muscles for miles!"
        scottie.say "Like, what do you bench?"
    elif active_girl.id == "dwayne":
        dwayne.say "Where in the hell did she come from?"
        dwayne.say "Am I going to have to kick her candy-ass?!?"
        ayesha.say "Huh..."
        ayesha.say "You look oddly familiar!"
    elif active_girl.id == "victor":
        victor.say "Uh..."
        victor.say "This is all, like, a misunderstanding, yeah?"
        victor.say "Why don't we just talk it through?"
    elif active_girl.id == "master":
        master.say "My, my...aren't you an impressive specimen!"
        master.say "You have the bearing of a natural warrior."
        master.say "We must pit our respective skills against each other, to see who is best."
        master.say "What do you say to that?"
    show ayesha at stepback(1.0, 20, 0)
    pause 0.7
    show ayesha at stepback(0.2, -200, -20)
    pause 0.2
    play sound spank
    $ renpy.show(f"{active_girl.id} angry", at_list=[hshake])
    "Ayesha answers the question by stepping up and punching him."
    "I mean it, she literally hits him square on the jaw!"
    "He staggers back, clutching his mouth."
    "But I don't know if it's from pain or sheer surprise that Ayesha hit him!"
    "Either way, he doesn't get a chance to respond."
    show ayesha at stepback(0.2, -200, -20)
    pause 0.2
    play sound spank
    $ renpy.show(f"{active_girl.id} angry", at_list=[hshake])
    "Ayesha throws herself at him, and the fight is on!"
    "Actually, it's Ayesha beating the living shit out of him."
    show ayesha at stepback(0.2, -200, -20)
    pause 0.2
    play sound spank
    $ renpy.show(f"{active_girl.id} angry", at_list=[hshake])
    "Because he doesn't even manage to get a single shot in!"
    "I watch as Ayesha manhandles him with shocking ease."
    "Tying his limbs in knots and stretching him in the most painful manner imaginable."
    $ renpy.hide(f"{active_girl.id}")
    hide ayesha
    $ renpy.show(f"ayesha beats {active_girl.id}")
    play sound punch_hard
    "Finally, Ayesha leaps into the air, hitting him in the face with a standing dropkick."
    "All of it connects, and he crumples to the floor in a helpless heap."
    if active_girl.id == "ryan":
        ryan.say "Aaargh..."
        ryan.say "My beautiful face!"
    elif active_girl.id == "jack":
        jack.say "Urgh..."
        jack.say "And down I go!"
    elif active_girl.id == "shawn":
        shawn.say "They lied to me!"
        shawn.say "Pro-wrestling is totally real..."
        shawn.say "And it hurts like hell too!"
    elif active_girl.id == "mike":
        mike.say "I surrender, I surrender!"
        mike.say "Please don't hurt me anymore!"
    elif active_girl.id == "danny":
        danny.say "[hero.name], help me!"
        danny.say "Make the giant chick stop kicking my ass!"
    elif active_girl.id == "scottie":
        scottie.say "Urgh..."
        scottie.say "I met the biggest chick in the world..."
        scottie.say "And she totally kicked my ass!"
    elif active_girl.id == "dwayne":
        dwayne.say "I can smell what this girl is cooking!"
        dwayne.say "And she just kicked MY candy-ass too!"
    elif active_girl.id == "victor":
        victor.say "Ah..."
        victor.say "Where am I?"
        victor.say "What did they do with my puppy?"
    elif active_girl.id == "master":
        master.say "If I die here, I want the world to know..."
        master.say "This is exactly how I wanted it to end!"
    ayesha.say "Take that, you asshole!"
    ayesha.say "That's what happens when you put your hands on a woman without their permission!"
    return

label ayesha_ask_date_alone_female:
    if not ayesha.flags.hadadate:
        bree.say "We've been getting on pretty well, haven't we, Ayesha?"
        ayesha.say "Yeah, [hero.name] - I always have a blast when I see you."
        bree.say "Well..."
        bree.say "I was wondering if you maybe wanted to hang-out?"
        bree.say "Just with me...like, at the pub or somewhere we could grab a bite to eat?"
        ayesha.say "Wait...you mean...like a date?"
        ayesha.say "You and me?"
        ayesha.say "On a date?"
        ayesha.say "Together?"
        bree.say "Well, yeah...I guess so!"
    else:
        bree.say "Hey Ayesha, wanna go on a date?"
    if ayesha.love < 50 or ayesha.flags.nodate:
        ayesha.say "I don't think so, [hero.name]."
        if not ayesha.flags.hadadate:
            ayesha.say "I mean, I like you as a friend."
            ayesha.say "But not anything more than that."
        $ date_choice = False
    else:
        ayesha.say "I'd love to, [hero.name]."
        ayesha.say "That's a great idea."
        ayesha.say "We should do it as soon as possible!"
        $ ayesha.flags.hadadate = True
        $ date_choice = True
    return date_choice

label ayesha_propose_female:
    show ayesha
    "There was a time in my life when I could never have imagined myself dating a girl like Ayesha."
    "In fact there was a time when I'd probably have run away from her, terrified of her muscle."
    "But of course that was before I actually met Ayesha and got to know the girl under all those muscles."
    "Now I know very well that the real Ayesha's strength lies elsewhere, in places harder to see."
    "As we've spent time together and grown to be more than friends, I've discovered that so much more about her."
    "Ayesha's intelligent, warm and most surprising of all, really sensitive!"
    "In fact, I've also discovered that I can't imagine her not being a part of my life."
    "Which is why I've resolved to do something about it."
    "I just know that I have to ask Ayesha to marry me."
    "I have no idea what her reaction to that is going to be."
    "Obviously I want her to say yes!"
    "But I still feel like I have to be prepared for the fact she might say no as well."
    "And if she does, that's going to be something that'll probably end up crushing me."
    "But I think it'd be far worse to never ask the question and go on wondering what might have been."
    show ayesha at center, zoomAt(1.5, (640, 1040)) with fade
    "So as soon as I feel that the time is right, I steel myself and prepare to ask the question."
    show ayesha b
    bree.say "Ayesha..."
    ayesha.say "Yeah, [hero.name]?"
    bree.say "I..."
    bree.say "I have to ask you something..."
    "I kind of start to go down on one knee."
    "But then I remember just how tall Ayesha is."
    "And the idea of doing that just seems utterly ridiculous."
    "So I reach out and take hold of her hands instead."
    show ayesha surprised
    ayesha.say "Oh..."
    show ayesha normal
    show fx question
    ayesha.say "What is it, [hero.name]?"
    bree.say "I've been so happy since we met, Ayesha."
    bree.say "And my life's become so much better since we became a couple too."
    bree.say "So much so that...that I want to marry you!"
    show ayesha surprised
    "I've never seen Ayesha's eyes go as wide as they go once I'm done talking."
    "Even when I've seen her in the wrestling ring, she never looked so animated."
    "But all I can do is hope that she soon regains the power of speech."
    "And that when she does, Ayesha says something that I want to hear too."
    if ayesha.love >= 195:

        "But the first thing that Ayesha does isn't to speak."
        "Instead she begins to nod her head."
        "And when she does so, I feel my heart start to beat faster."
        bree.say "Ayesha..."
        bree.say "Are you..."
        show ayesha happy at startle(0.05,-10)
        ayesha.say "Yes, [hero.name]..."
        show fx exclamation
        show ayesha at startle(0.05,-10)
        ayesha.say "Yes, I will marry you!"
        "As soon as I hear those words, I can't hold my emotions back any longer."
        "It's like a dam bursts inside of me and it all just comes flooding out."
        "I all but throw myself at Ayesha, wrapping my arms around her."
        "She's not ready for this, and it sends her staggering backwards."
        "But she soon recovers, and I feel her arms around me too."
        "Finally I pull away a little, just enough for us to look each other in the eye."
        bree.say "I can't believe it..."
        bree.say "We're engaged!"
        bree.say "We're going to get married!"
        bree.say "This is a whole different kind of ring for you, right?"
        "Ayesha winces and shakes her head."
        show ayesha a
        ayesha.say "Okay, [hero.name]..."
        ayesha.say "Here's the first condition I'm putting on you..."
        ayesha.say "No more terrible puns, not if you want this to work out between us!"
        $ ayesha.set_fiance()
    else:

        show ayesha sad
        "But as soon as I see Ayesha begin to shake her head, I know that's not going to happen."
        ayesha.say "I...I can't marry you, [hero.name]."
        ayesha.say "I'm sorry, but I just can't."
        bree.say "But why, Ayesha?"
        bree.say "We love each other, don't we?"
        bree.say "Isn't that enough?"
        hide ayesha
        show ayesha sad
        "Ayesha shakes her head as she takes a step backwards, putting herself out of my reach."
        "And that single movement almost hurts more than hearing her say no to marrying me."
        "Because it's an effort to put distance between us, rather than bring us closer together."
        show ayesha normal
        ayesha.say "Of course I love you, [hero.name]!"
        ayesha.say "But that's not what this is about."
        show fx drop
        ayesha.say "I'm just not ready to be that close to anyone."
        ayesha.say "Maybe one day I will be."
        ayesha.say "But here and now...there's just no way!"
        "I open my mouth, getting ready to argue my case."
        "But Ayesha holds up a hand to stop me."
        "She doesn't say a single word to silence me either."
        "But coming from her, the gesture is enough to stop me in my tracks."
        hide ayesha with easeoutright
        "And so I let her turn on her heel and walk away."
        "All the time this is happening, I'm hoping it's just because she needs time alone."
        "Time to think deeply and seriously about what I asked her and what lies in our future."
        "Rather than her just wanting to get as far away from me as possible."
        $ ayesha.love -= 25
    return

label ayesha_pregnancy_congratulations:
    show ayesha curious
    "Ayesha keeps on shooting me these odd looks."
    show ayesha normal
    "You know the kind I mean."
    show ayesha sad
    "When someone's looking at you while trying to seem like they're not."
    show ayesha curious
    "It's easy enough to spot with most people."
    show ayesha normal
    "So when Ayesha tries to pull it off, it's almost impossible to miss."
    bree.say "It's okay, Ayesha..."
    bree.say "You can ask me."
    show ayesha surprised
    ayesha.say "What?"
    ayesha.say "I don't know what you mean!"
    "I smile and give Ayesha a knowing look."
    show ayesha normal
    "And that seems to be enough to make her drop all pretence."
    ayesha.say "Am I really that obvious?"
    show ayesha sad
    ayesha.say "I guess so!"
    show ayesha curious
    ayesha.say "Okay, [hero.name]..."
    ayesha.say "You're pregnant, aren't you?"
    "I nod and smile, unconsciously holding my belly."
    bree.say "Yes I am!"
    show ayesha happy
    ayesha.say "That's great news, [hero.name]!"
    ayesha.say "Congratulations, and I'm sure you'll be a great mom!"
    $ ayesha.love += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
