init python:
    def emma_too_small(size_limit):
        if hero.has_skill("hung"):
            size_limit += 5
        elif hero.has_skill("smalldick"):
            size_limit -= 5
        return (emma.sexperience + emma.flags.loose) < size_limit

    Event(**{
    "name": "emma_hottub_sex_male",
    "label": "emma_hottub_sex_male",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("date_hot_tub_home")),
        PersonTarget(emma,
            OnDate(),
            MinStat("love", 100),
            MinStat("sexperience", 1),
            ),
        ],
    "priority": 500,
    "do_once": False,
    "once_day": True,
    "duration": 1,
    })

    InteractActivity(**{
    "name": "fuck_emma",
    "display_name": "Fuck",
    "label": "emma_fuck_ROOM",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            HasStamina(),
            ),
        PersonTarget(emma,
            IsActive(),
            MinStat("love", 150),
            MinStat("sexperience", 5),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })


label emma_fuck_date_male(location="hero"):
    $ game.play_music("music/roa_music/city_nights.ogg")
    scene bg street
    show emma
    if not "emma_fuck_date_first" in DONE:
        call emma_fuck_date_first from _call_emma_fuck_date_first
    elif not emma.flags.benjibinge:
        call emma_fuck_date_binge_or_else from _emma_fuck_date_binge_or_else
    elif not "emma_fuck_date_second" in DONE or emma.love < 140:
        call emma_fuck_date_second from _call_emma_fuck_date_second
    elif not "emma_fuck_date_third" in DONE:
        call emma_fuck_date_third from _call_emma_fuck_date_third
    elif not "emma_fuck_date_fourth" in DONE:
        call emma_fuck_date_fourth from _call_emma_fuck_date_fourth
    elif not "emma_fuck_date_fifth" in DONE:
        call emma_fuck_date_fifth from _call_emma_fuck_date_fifth
    elif not "emma_fuck_date_sixth" in DONE:
        call emma_fuck_date_sixth from _call_emma_fuck_date_sixth
    elif not "emma_fuck_date_seventh" in DONE:
        call emma_fuck_date_seventh from _call_emma_fuck_date_seventh
    elif not "emma_fuck_date_eighth" in DONE:
        call emma_fuck_date_eighth from _call_emma_fuck_date_eighth
    elif not "emma_fuck_date_ninth" in DONE:
        call emma_fuck_date_ninth from _call_emma_fuck_date_ninth
    else:
        call emma_fuck_date_loop from _call_emma_fuck_date_loop
    return

label emma_fuck_date_first:
    $ game.play_music("music/roa_music/city_nights.ogg")
    $ DONE["emma_fuck_date_first"] = game.days_played
    scene bg house
    show emma
    with fade
    emma.say "Wow, I didn't think I'd be this nervous!"
    mike.say "Why are you nervous?"
    emma.say "Well, you know, coming to a strange man's house and, um. Whatever! You know?"
    mike.say "Are you saying I'm a strange man?"
    emma.say "Have you met you?"
    mike.say "Not formally."
    emma.say "Perhaps you should, then."
    "I laugh, while we continue into the house."
    scene bg livingroom
    show emma
    with fade
    mike.say "Besides, you've already had a sleepover here. And I hear it was pretty exciting for you!"
    show emma blush
    emma.say "Yeah, but you were in the other room!"
    mike.say "See, I was able to excite you from halfway across the house!"
    show emma blush ahoge
    emma.say "Stop!"
    mike.say "Stop what?"
    emma.say "Stop being...you!"
    mike.say "Okay, who should I be?"
    emma.say "Benji!"
    mike.say "Bah. Nobody needs Benji."
    show emma happy
    emma.say "For one that's a lie, and for two he's super cute!"
    mike.say "For an anime character, I suppose."
    emma.say "You {b}suppose{/b}?!?"
    mike.say "Well, I'm not really a judge."
    emma.say "That's it, if we're going to do this, then we need to cuddle up and binge the next eight or so episodes!"
    menu:
        "Sounds awesome!":
            jump emma_fuck_date_binge
        "I'd rather do something else":
            mike.say "I'd rather do...something else."
            show emma sad
            $ emma.love -= 5
            emma.say "Like what?"
            mike.say "Maybe a little hanky panky?"
            show emma blush with vpunch
            emma.say "Oh! I, uh. I don't...no I'm not. It's too soon, I mean it's...we're."
            emma.say "Oh! I'm sorry, I'm having tr--"
            "And then she gets up and runs out."
            hide emma with moveoutright
            "Yikes. Maybe I need to be a bit more careful next time. Hopefully there will be a next time!"
    return

label emma_fuck_date_binge:
    mike.say "That sounds like a great way to spend the rest of the evening!"
    $ emma.flags.benjibinge = True
    $ emma.love += 5
    "Once we agreed to the binge-watching, Emma's nervousness melted away and transformed into boundless excitement."
    "After I set up {i}No need for Benji{/i} on the TV, she pats the spot next to her on the couch. I oblige and sit next to her."
    "She presses herself against me and we settle in to watch."
    $ game.pass_time(1, needs=True)
    scene bg livingroom with fade
    "After the first couple of episodes, Emma's excitement has settled in, and she is happy to cuddle with me on the couch."
    "I really like having her next to me, sharing the personal space. True, I'm also horny and would like to get some, but she's still nervous about that."
    "So I'm content to wait."
    $ game.pass_time(1, needs=True)
    scene bg livingroom with fade
    "After two more episodes, Emma seems to be getting pretty sleepy. But we go straight into the next episode anyway; she doesn't want to stop."
    $ game.pass_time(1, needs=True)
    scene bg livingroom with fade
    "As I'm watching the closing credits on the...what, eighth episode, I start to ask her if she's done."
    "...and she's fast asleep, with her head resting on my shoulder. She's drooling on me, just slightly."
    "I very carefully separate myself from her, and she doesn't wake up."
    "So I get a pillow and a blanket, tuck her in and give her a kiss on the forehead."
    "As I do so, she opens her eyes and gives me a happy, sleepy smile."
    mike.say "Good night, Emma."
    emma.say "G'ni--"
    "And she's back to sleep."
    "And then I head off to my own bed."
    $ hero.fun += 4
    $ game.room = "livingroom"
    call sleep from _emma_fuck_date_first
    return

label emma_fuck_date_binge_or_else:
    scene bg house
    show emma
    emma.say "So, [hero.name], you ready for that Benji binge?"
    menu:
        "Sure!":
            jump emma_fuck_date_binge
        "Do I have to?":
            show emma sad
            emma.say "Is it...really such a...I mean I thought you liked. I mean didn't we..."
            show emma angry
            "Her expression turns sour and her speech speeds up, like she's hurrying to get the words out before she loses track of them."
            emma.say "I mean, I thought we had-a-connection-but-I-guess-I-was-just-imagining--"
            menu:
                "I'm just kidding, I didn't mean to upset you" if hero.charm > 60:
                    "I put one hand up and interrupt her, trying to show as disarming of a smile as I can muster."
                    mike.say "I'm sorry, Emma, that was a really poorly timed joke. I didn't mean to upset you!"
                    $ emma.love -= 2
                    emma.say "Really?"
                    mike.say "Look, I can be an idiot sometimes!"
                    emma.say "So you do want to binge Benji with me or not?"
                    jump emma_fuck_date_binge
                "I'm not as into anime as you are":
                    mike.say "Emma! I'm sorry, I didn't, I guess I'm just not into anime as you are."
                    show emma sad
                    emma.say "Oh. I...yeah. I better go."
                    mike.say "No, wait!"
                    emma.say "No! It's okay if you don't actually like it, but I feel kind of...like you lied. That's not okay!"
                    "She turns away from me and heads for the door."
                    mike.say "Emma, I--"
                    emma.say "Stop! Just stop digging deeper."
                    "And with that, she disappears."
                    $ emma.flags.nodate = True
                    $ emma.flags.nokiss = True
                    $ emma.flags.noanime = True
                    if emma.love.max < 100:
                        $ emma.love.max = 100
                    hide emma
                "I guess we don't":
                    mike.say "I guess we don't have a connection after all. Maybe the dreams were just...some kind of illusion."
                    hide emma
                    "Emma bursts into tears and runs out without another word."
                    $ emma.flags.nodate = True
                    $ emma.flags.nokiss = True
                    $ emma.flags.noanime = True
                    $ emma.flags.noconnection = True
                    $ emma.set_gone_forever()
        "No":
            mike.say "No, I'd rather do something else."
            show emma sad
            emma.say "Oh. I guess I should have--you know what, I just remember, I have, um. Stuff. Some stuff I have to take care of."
            mike.say "Stuff, really?"
            emma.say "Well, I mean. I just...yeah. I have to watch some anime. Alone."
            mike.say "Emma, wait--"
            emma.say "No! It's okay if you don't actually like it, but I feel kind of...like you lied. That's not okay!"
            "She turns away from me and heads for the door."
            mike.say "Emma, I--"
            emma.say "Stop! Just stop digging deeper."
            "And with that, she disappears."
            $ emma.flags.nodate = True
            $ emma.flags.nokiss = True
            $ emma.flags.noanime = True
            if emma.love.max < 100:
                $ emma.love.max = 100
            hide emma
    return

label emma_fuck_date_second:
    $ game.play_music("music/roa_music/city_nights.ogg")
    $ renpy.dynamic("girl", "partners", "girlfriends")
    $ partners = hero.get_partners(defaults={"alexis"}, ignore=["emma"])
    $ girlfriends = hero.get_girlfriends(ignore=["emma", "samantha"])
    scene bg livingroom
    show emma date blazer happy
    with fade


    if "emma_fuck_date_second" not in DONE:
        "Emma looks just about as happy as I've ever seen her, and her mood is infectious. I have to admit, she's making me really want some sexy time."
        "But I've learned that pushing her on that is a bad idea. It's gotten more clear that it's not really about me."
        "Something must have happened to her, somewhere, somewhen."
        "But still..."
        menu:
            "Do you want to have some sexy time?":
                mike.say "So, Emma, do you want to, you know. Have some sexy time?"
                show emma angry
                emma.say "Is that really what you want, [heroname] [hero.family_name]?"
                "Oh crap, my full name? Clearly that was the wrong call."
                mike.say "No! I mean yes, I have to be honest, that is something I want, but it's not {b}all{/b} I want!"
                "She frowns."
                emma.say "Do you think I'm some kind of slut?"
                mike.say "No! I'd never say that about you!"
                emma.say "Oh? So you'd say that about someone else?"
                mike.say "What? No!"
                show emma happy
                "Emma suddenly starts laughing."
                emma.say "Oh my God, [hero.name], you should see the look on your face right now."
                mike.say "What!?"
                show emma normal
                emma.say "What if I were a slut?"
                mike.say "I don't...I honestly don't know how to answer that."
                emma.say "No? Would it matter to you if I'd had sex with a hundred guys?"
                mike.say "Well I don't know, I guess."
                "I had to think about that. My co-worker Audrey's clearly been around the block a few...hundred times. Do I care about that?"
                "Or heck, Sasha's certainly had her share of partners. She can be pretty slutty. Do I care?"
                mike.say "No, it wouldn't matter."
                emma.say "Oh yeah? So would you like me more slutty? You want a girl that has gotten around?"
                mike.say "I--well, um. Is this a trap?"
                emma.say "Not at all. Be honest."
                mike.say "I guess, experience counts for something. But so is exploring and learning? I don't honestly know."
                emma.say "How about you. Are you...experienced?"
                if len(partners) > 4:
                    mike.say "I've...been with a few girls, yeah."
                elif len(partners) > 2:
                    mike.say "I guess I've been with a couple of girls. Is that experienced?"
                elif len(partners) == 2:
                    mike.say "Just two."
                else:
                    mike.say "Just the one girl from my past, honestly."
                emma.say "What if I told you I didn't care?"
                mike.say "Then why did you ask?"
                emma.say "To make you squirm."
                mike.say "And why don't you care?"
                emma.say "It doesn't matter to me what was in your past. Only what's in your present."
                emma.say "Well. Unless you've hurt or killed people in your past. That would matter."
                mike.say "I've never done that!"
                show emma happy
                "She gives me a big, happy Emma smile."
                emma.say "I know! I would never have gotten close to you if you had that kind of past."
                show emma normal
                emma.say "But about your present. Do you have a girlfriend?"
                if len(girlfriends) > 0:
                    "Tricky. How will she take the truth? Can she trust me if I tell her I have a girlfriend? Will she trust me if she figures out I lied?"
                    menu:
                        "Yes":
                            "I figure it's better to be open. Our relationship is a little unusual, and she doesn't trust easily."

                            mike.say "Yes, I have a girlfriend of sorts."
                            emma.say "Just one girl? Not counting me, of course."
                            if len(girlfriends) > 1:
                                mike.say "Fine, yes, there's more than one girl."
                            else:
                                mike.say "No, just the one."
                            emma.say "Well. I'm glad you didn't lie about it. But -- look, you're asking me for sexy time when you've got a girlfriend."
                            if len(girlfriends) > 1:
                                emma.say "Is that really fair to them?"
                            else:
                                emma.say "Is that really fair to her, though?"


                            if len(girlfriends.difference({'palla', 'lexi', 'audrey'})):
                                mike.say "Truthfully? Our relationship is open. So yeah, it's fair."
                                emma.say "Oh. Oh! That's...girls really do that?"
                                mike.say "Well. Some do. I hope that's not a problem for you?"
                                "Emma looks at me and thinks about it."
                                emma.say "What is really the question is...if you and I were to be...a thing. Would {b}I{/b} be okay with that?"
                                mike.say "That is a very important question."
                                emma.say "I don't know the answer to that."
                                mike.say "That's probably for another time, then."
                            else:
                                mike.say "I don't have a good answer for that."
                                emma.say "Maybe I should go."
                                mike.say "Wait! No, look. It's, it's complicated okay?"
                                emma.say "Yes, everything about you and everything about this is complicated."
                                $ emma.flags.admittedgirlfriend = True
                                emma.say "Fine. I'll stay, but there's limits to what I'll do until you resolve this."
                                mike.say "What do you mean?"
                                show emma angry
                                emma.say "What I mean is that if you hurt anyone for my sake, I'll destroy you."
                                "Whoa. That got intense really fast."
                                show emma normal
                                emma.say "So make sure you know what you're doing."
                                mike.say "Yes, ma'am!"
                                emma.say "But. You told me the truth. I appreciate that. So..."
                        "[[LIE] No":
                            mike.say "Nope. I'm single! Completely available."
                            "Emma gives me a long stare."
                            emma.say "You're a pretty good liar, [hero.name], but not that good."
                            mike.say "What do you mean?"
                            emma.say "Please, it's not like I didn't do my research on you."
                            "Oh shit."
                            mike.say "Then you must've done the wr--"
                            emma.say "Stop right there."
                            show emma angry
                            "Emma gathers her things while she speaks."
                            emma.say "I had a speech about being fair all ready in my head, and what you needed to do. And I was ready, even knowing what I know about you."
                            emma.say "But you lied to me."
                            emma.say "How can I ever trust you?"
                            $ emma.flags.nodate = True
                            $ emma.flags.nokiss = True
                            $ emma.flags.noanime = True
                            $ emma.flags.noconnection = True
                            $ emma.set_gone_forever()
                            mike.say "Emma..."
                            hide emma with moveoutright
                            "But she doesn't listen to anything I might have to say as she walks out."
                            return
                else:
                    mike.say "Nope, no one. Just you, if I'm lucky."
                    emma.say "Oh really? So you're saying you hope you get lucky tonight?"
                    mike.say "Tonight? Tomorrow night? Sometime? Every moment I spend with you is lucky."
                    show emma blush
                    emma.say "I...wow!"
            "We're out of Benji episodes, what next?":

                mike.say "We're out of Benji episodes. What should we do next?"
                emma.say "Oh, you sweet summer child. That was just the OVAs! We still have {i}Benji Forever{/i}, {i}Benji in Kyoto{/i}, {i}Benji across the World{/i}, {i}Benji in Space{/i}, and {i}Benji Benji Benji{/i}!"
                mike.say "Really? There's one called {i}Benji Benji Benji{/i}?"
                emma.say "Yeah. It's kind of terrible honestly. It's this weird thing where he gets cursed and people can say his name three times and summon him."
                mike.say "That...could be funny, I guess?"
                emma.say "It should be, but...enh. Anyway I liked Benji Forever well enough, though it's not quite in the same canon. Benji in Kyoto is a proper sequel and we should definitely watch that."
                mike.say "Let's do it!"
                emma.say "But tonight I have another idea."
                mike.say "What do you have in mind?"
    "Without warning, Emma throws her arms around me and envelops me with a kiss."
    show emma kiss date with fade
    $ emma.flags.kiss += 1
    "Her eyes close and her lips press against mine. It feels as though the air is sucked out of the room as our bodies press against each other."
    "And it's not a brief kiss, either."
    "Instead, she takes her time, alternately exploring, then pressing harder against me, then exploring again."
    "I'm not sure if time stops or flies by. Everything is gone except for her."
    show emma ahoge date blazer with fade
    mike.say "Wow. That was...really nice. I--"
    emma.say "Not done yet, Mister. Shut up."
    mike.say "I..."
    "No, she said shut up. I do so, to see what else she has in mind."
    emma.say "Take your clothes off and sit down."
    mike.say "Really?"
    emma.say "Do you want me to do this or not, Mister?"
    mike.say "On it."
    "I do as instructed, quickly removing my clothing and tossing them aside without much care. Then I sit."
    show emma hj livingroom with fade
    "Emma sits beside me and wraps her fingers around my member. The look on her face would best be described as not quite sure what to do."
    call emma_dick_reactions from _emma_fuck_date_second_dick_reaction
    mike.say "Oh. Oh! This is what you--"
    emma.say "No talking!"
    mike.say "Fine I--"
    emma.say "You do know what 'No talking' means, right?"
    "I open my mouth to say yes, then close it and nod."
    "She looks back at my cock, which even with just that simple touch is fully awake and ready to go."
    show emma hj at startle(0.05, -10)
    "She strokes up and down...somewhat awkwardly and not entirely gently. It's pretty clear she doesn't know what to do."
    "I'm going to be honest. This feels good, mostly. But her lack of experience also adds some discomfort."
    "I must have winced, because she looks at me with concern."
    emma.say "[hero.name]? Did I hurt you?"
    mike.say "No, just. I...can I show you?"
    "She looks at me a bit wide-eyed, then nods."
    "So I put my hand over hers, and show her where to put her fingers. Without talking--she did ask me not to talk--I try to show her how much pressure to use."
    show emma hj at startle(0.05, -10)
    pause 0.2
    show emma hj at startle(0.05, -10)
    "Then I guide her hand up and down for several strokes."
    "And holy shit, the skin of her fingertips is soft, and sensuous. That doesn't take very long."
    show emma hj at startle(0.05, -10)
    pause 0.2
    show emma hj at startle(0.05, -10)
    "Then I move my hand away, and let her continue."
    emma.say "Slower? Faster?"
    mike.say "Just like that. Maybe...speed up a tiny bit as we OH! Oh!"
    show emma hj
    "As she gets better, precum starts to dribble out and flows down my cock, adding lubrication to the mix."
    show emma hj at startle(0.05, -10)
    pause 0.2
    show emma hj at startle(0.05, -10)
    "I let myself go to just feel the sensation. My hips start to move, and she times her strokes with my hips."
    show emma hj surprised cum with vpunch
    "After a few more moments, white, sticky semen spews forth from my cock."
    show emma hj hand_shoulder with vpunch
    emma.say "Oh! Oh my God!"
    show emma hj -cum with vpunch
    emma.say "Holy shit, [hero.name], you're covered with it!"
    mike.say "Hm, yeah. Guess I'm going to need a shower. Unless..."
    show emma hj normal
    emma.say "Stop it right there, Mister. You can clean that mess up by yourself."
    show emma hj hand_leg
    mike.say "Aww. You don't want to help?"
    emma.say "Not...this time. Maybe another time."

    if len(girlfriends) == 1:
        emma.say "If, of course, you deal with your girlfriend first."
    elif len(girlfriends) > 1:
        emma.say "If, of course, you deal with your girlfriends first."
    mike.say "Mmm."
    emma.say "Mind if I sleep on your couch?"
    mike.say "Yeah. I mean no, I don't mind. Yeah, sleep here."
    emma.say "Good. Go clean up!"
    hide emma hj
    show bg bathroom
    with fade
    "I go and take a quick shower, washing myself off while I enjoy the afterglow."
    $ hero.grooming += 8
    show bg livingroom with fade
    "By the time I'm done, she's already fast asleep on the couch. She's smiling in her sleep while her eyes shift. I imagine she's dreaming about me."
    show bg bedroom1 with fade
    "And then I head off to sleep myself."
    $ game.room = "bedroom1"
    $ DONE["emma_fuck_date_second"] = game.days_played
    call sleep from _emma_fuck_date_second
    return

label emma_fuck_date_third:
    $ game.play_music("music/roa_music/city_nights.ogg")
    $ DONE["emma_fuck_date_third"] = game.days_played
    scene bg livingroom
    show emma date blazer happy
    with fade
    emma.say "So, [hero.name], I've been thinking..."
    mike.say "Oh? What about?"
    emma.say "Well. What if...I mean, you know how much I love Benji, right?"
    mike.say "Oh yes, he's almost an obsession!"
    show emma blush
    emma.say "Obsession! I don't--well. Maybe. Anyway, I was thinking, what if..."
    mike.say "Yes?"
    emma.say "What if you...I mean, let's say you pre--I mean,I pre--Oh, no, I'm screwing this all up, aren't I?"
    mike.say "No, but you do need to spit it out. I'm getting really confused."
    emma.say "Well, yeah you're right. Okay. Here goes..."
    "She closes her eyes and takes a deep breath."
    emma.say "What if you pretend to be Benji and I pretend to be Princess Akari, and we, um. We...you know."
    mike.say "No, I don't know."
    emma.say "Um. Have sex!"
    "If she could blush any brighter, she would be doing so."
    mike.say "Oh! Oh wow. Wait, did Benji and Akari ever actually have sex?"
    emma.say "Well, no, but Akari always wanted him, right from the beginning. And there was one story where they almost did, and..."
    mike.say "Okay! I got you. Look, are you sure? I know that sex has been kind of weird for you."
    "Her voice takes on a bit of a higher class accent."
    emma.say "Shut up and take me to your bedroom...{i}Benji{/i}."
    mike.say "Yes, ma'am!"
    show emma angry
    emma.say "No! Not like that! The way Benji would say it!"
    mike.say "Oh! Right. Yes...Your Highness?"
    show emma happy
    emma.say "That's better!"
    mike.say "Uh, right this way, Princess!"
    show bg bedroom1
    show emma date blazer happy
    with fade
    emma.say "Oh...oh Benji! I can't believe I finally get -- I mean, we finally get to do this!"
    mike.say "Oh, well, Princess, you know you've always been my favorite, of, um. Wait what are they called again?"
    emma.say "The Junmai!"
    mike.say "Yes! My favorite of the Junmai!"
    emma.say "And you're my favorite of...everyone in the whole galaxy, Benji!"
    mike.say "Aww, shucks, Princess, I'm just a --"
    show emma blush
    emma.say "Shut up, Benji, and take your clothes off!"
    mike.say "Yes, my Princess!"
    "I take my clothes off, while Emma watches me hungrily. When I called her \"my Princess\", I could really see how aroused that made her."
    mike.say "There. Your turn...{i}my Princess!{/i}."
    "Emma looks thoughtful for a moment, then strips out of most of her clothes."
    show emma blush -blazer with dissolve
    emma.say "Like this, Benji?"
    mike.say "Oh Princess, that's...more, please!"
    show emma blush naked with dissolve
    emma.say "So more like this, my Benji?"
    mike.say "Oh. Oh my yes, Princess."
    emma.say "What...what should I do now, Benji?"
    mike.say "Lie back on the bed."
    show emma missionary with fade
    "Emma lays on the bed, spreading her legs wide and giving me a fantastic view of...well, everything."
    show emma missionary mike
    "As soon as I see her, open and inviting like that, my cock stiffens."

    emma.say "Oh my God, [hero.name] -- I mean Benji! That's...so big!"
    mike.say "I know, it's a burden, but I will bear it, my Princess!"
    "As I take a step toward her, she starts to look concerned. Even a little frightened."
    emma.say "Nonono, no! That's...no! It won't fit!"
    mike.say "Nonsense! It's not {b}that{/b} big!"
    emma.say "No! Maybe it's not but ... I'm not ... I can't!"
    emma.say "Don't you dare put that in me! Use...use your tongue instead!"
    menu:
        "Oh no, I've waited forever for this...":
            "Seeing her spread like that, open and waiting, I'm {b}ready{/b}."
            mike.say "Oh no, Princess Akari, I've wanted this forever!"
            "As I move forward to try and insert myself into her, Emma screams at the top of her lungs, flying off the bed faster than I thought she could move."
            show emma naked angry with hpunch
            emma.say "Holy shit, [hero.name], I never thought you would...you could!"
            emma.say "How {b}dare{/b} you treat someone that way!"
            emma.say "I {b}never{/b} want to see you again!"
            mike.say "Emma! I'm sorry, I thought it was part of the game!"
            "She quickly grabs her clothes and runs out of the house."
            hide emma with moveoutright
            $ emma.set_gone_forever()
            "Damn. That was...really fast. Did I fuck that up that badly?"
            "I think I did."
            $ game.room = "bedroom1"
            return
        "As you wish, my Princess!":
            mike.say "As you wish, my Princess!"
            hide emma miss
            show emma lick
            with fade
            $ emma.flags.loose += 1
            "I get down on my knees and put my face between her thighs. They close around me, pressing lightly on my cheeks."
            "I use my tongue on her; she is incredibly wet, and moans almost every time I brush across her clit."
            "Bringing one hand up, first I stroke between her labia, and then I press one finger in."
            "Except she's so tight, it won't go past the first knuckle. Not even my finger."
            "That means she's right -- if I can't get my finger in there while she's this wet, I'd never have gotten my dick inside her."
            "I try not to think about that just now; I've got a job to do, and I'm here to do it."
            "It doesn't take long..."
            show emma lick pleasure
            emma.say "Oh! Oh god. Oh...Oh Benji! Oh [hero.name]! I--I'm coming!"
            "My face is absolutely flooded with her juices when it happens."
            hide emma lick
    show cuddle emma
    with fade
    "I crawl up beside her, and she leans her head on my shoulder. Her voice sounds content...and maybe a little bit sleepy."
    emma.say "Oh, [hero.name]! That was...fucking amazing!"
    mike.say "Benji!"
    emma.say "Oh right. I mean...Benji, my hero! You've saved everyone again!"
    mike.say "Anything for you, my Princess!"
    emma.say "Thank you. I'm...sorry I flipped out about...how, um. How big you are."
    mike.say "I admit, I was a bit upset about it at first -- but...you're special, Emma. I never want to hurt you."
    mike.say "And then I tried to push a finger in, and I couldn't even do that."
    "She gives me a sleepy smile, then gives my shoulder a kiss."
    emma.say "If you want to...I mean. The...my doctor says that I'll have to work on it."
    mike.say "Is there something...wrong? I mean, I've never heard of something like this."
    emma.say "It's...a condition. It's called vaginismus. My vaginal muscles are very strong, and very very tight."
    emma.say "There's some exercises I can do, maybe. I've always been afraid to. They hurt."
    emma.say "I might...might be willing to. For you."
    mike.say "That's sweet, Emma!"
    emma.say "If...if..."
    mike.say "If what?"
    emma.say "If you'll...oh God I'm sorry, I always start tripping over myself when I try to talk, don't I?"
    mike.say "But you eventually get it out. It's okay."
    "She takes a deep breath."
    emma.say "Be my boyfriend! Be my Benji, [hero.name]! I want that."
    "Oh. I guess I should have known, but I wasn't expecting it...now!"
    menu:
        "Yes":
            mike.say "Yes, of course, {b}my Princess!{/b}"
            "Emma's eyes widen."
            emma.say "Really? You mean it? You and me?"
            mike.say "Just so."
            emma.say "Oh I can't, I thought...I was so..."
            "She envelops me in as big a hug as her petit body can manage."
            emma.say "I look forward to...exploring this with you."
            mike.say "Me too!"
            emma.say "Just...be patient with me, okay?"
            mike.say "Of course!"
            "Then she kisses my shoulder, and fades off into sleep."
            $ hero.fun += 4
            if emma.love.max < 160:
                $ emma.love.max = 160
            $ emma.love += 10
            $ emma.set_girlfriend()
            $ game.room = "bedroom1"
            $ emma.flags.emmadelay = TemporaryFlag(True, 1)
            call sleep ("emma") from _call_sleep_52
        "I can't":
            mike.say "I...can't do that, Emma."
            emma.say "Oh."
            "I admit, I expected...more of a response than that. So I wait a moment or two."
            "But she doesn't move, doesn't react in any other way."
            mike.say "Are you okay?"
            "More silence."
            mike.say "Emma?"
            emma.say "Just...just go to sleep, [hero.name]."
            "I can't really sleep, though. Not like that."
            $ game.pass_time(1)
            hide emma
            $ emma.set_gone_forever()
            "Apparently I can, though, because I closed my eyes once, and when I opened them again, she's gone."
            call sleep from _emma_fuck_date_third
    return

label emma_fuck_date_fourth:
    $ DONE["emma_fuck_date_fourth"] = game.days_played
    $ game.play_music("music/roa_music/city_nights.ogg")
    $ game.room = "bedroom1"
    scene bg bedroom1
    show emma date blazer happy
    with fade
    emma.say "So, [hero.name], what would you like to do?"
    mike.say "How goes your...er, exercises?"
    emma.say "Oh! They're, um. Going okay."
    mike.say "Are they doing any good?"
    emma.say "I guess...I mean. Not yet."
    mike.say "Oh. That's kind of disappointing."
    emma.say "I can...um. Give you a handy, if you want?"
    menu:
        "Hand job":
            call emma_fuck_date_handjob from _call_emma_fuck_date_handjob
        "Lick":
            show emma lick with fade
            $ emma.flags.loose += 1
            "I get down on my knees and put my face between her thighs. They close around me, pressing lightly on my cheeks."
            "I use my tongue on her; she is incredibly wet, and moans almost every time I brush across her clit."
            "I use my fingers, caressing the outside of her labia while my tongue massages her clit."
            emma.say "Oh! Oh god! Oh my God! Oh Benji!"
            "It doesn't take her very long..."
            show emma lick pleasure
            emma.say "Oh! Oh god. Oh...Oh Benji! Oh [hero.name]! I--I'm coming!"
            "My face is absolutely flooded with her juices when it happens."
    show cuddle emma with fade
    "Emma mumbles into my ear about how absolutely amazing that was, before we drift off to sleep."

    call sleep ("emma") from _emma_fuck_date_fourth
    $ game.room = "bedroom1"
    return

label emma_fuck_date_fifth:
    $ game.play_music("music/roa_music/city_nights.ogg")
    $ game.room = "bedroom1"
    scene bg bedroom1
    show emma date blazer
    with fade
    "I was worried that tonight might be too much for Emma to handle."
    "I think she might just be the shyest girl that I've ever met."
    "And she's for sure the shyest one that I've ever dated!"
    "But she took me by complete surprise and handled it like a pro."
    "Maybe it was because we were alone, with nobody else butting in."
    "But whatever the reason, Emma and I ended up having a great time."
    "So much so that she never even questioned the idea of coming back to my place."
    show emma annoyed
    "It's only as I close the door behind us that she seems to change her tune."
    "Maybe because the reality of what we're about to do is finally sinking in..."
    mike.say "Hey, Emma..."
    mike.say "Are you okay?"
    mike.say "You look a little nervous there!"
    "Who am I trying to kid?"
    "She looks fucking terrified!"
    show emma normal
    emma.say "N...no..."
    emma.say "I'm not nervous..."
    emma.say "Not me, [hero.name]!"
    show emma happy
    emma.say "I'm just fine and dandy!"
    show emma annoyed
    "I can tell from the tone of Emma's voice that she's not telling the truth."
    "And the fact that she's pretty much babbling is a dead giveaway too."
    "I take a deep breath, hold it for a moment and then let it out."
    mike.say "I had a great time tonight, Emma."
    mike.say "And I'm not going to lie to you."
    mike.say "I'm really in the mood to fool around a little."
    mike.say "Are you okay with that?"
    show emma normal
    emma.say "I...had a great time too, [hero.name]."
    emma.say "And...I...I want to..."
    emma.say "Really, I do!"
    show emma annoyed
    "She's all but saying that this is a decision I'm going to have to make."
    "But how should I go about handling this?"
    menu:
        "Suggest a BJ":
            "This isn't going to be easy."
            "But maybe the answer isn't me getting what I want."
            "Maybe it's more about me making sure Emma gets what she wants."
            mike.say "It's okay, Emma."
            mike.say "I'm a little nervous too!"
            show emma normal
            "Emma's expression changes from anxious to surprised."
            "It's as if she can't believe what she's hearing."
            emma.say "You are?!?"
            emma.say "B...but why?"
            emma.say "You must have lots of..."
            emma.say "Well...lots of experience, right?"
            mike.say "I've had some, Emma."
            mike.say "But that's not what I meant."
            mike.say "I'm nervous because I want you to enjoy this."
            mike.say "And I won't be happy if you don't, even if you tell me you do!"
            show emma annoyed
            "Emma nods slowly, considering my words."
            "And it seems that I've gotten through to her."
            show emma normal
            emma.say "W...we could take it slow?"
            emma.say "If you like?"
            mike.say "I would, Emma."
            mike.say "How about a blowjob?"
            mike.say "Or else you could just touch it?"
            "Emma shakes her head all of a sudden."
            "And I can see that she's gathering up her courage."
            emma.say "No, [hero.name], it's okay."
            $ emma.sub += 1
            call emma_fuck_date_bj from _call_emma_fuck_date_bj
            $ game.pass_time(1)
        "Insist on sex":

            "Ah...this is tough."
            "I know what I want."
            "But how am I supposed to know what Emma wants too?"
            "Maybe she's just waiting for me to assert myself?"
            "If I do that, perhaps she'll forget about her nerves."
            mike.say "That's great, Emma."
            mike.say "So let's keep on having a good time."
            mike.say "Let's fuck!"
            show emma angry
            $ emma.love -= 10
            "The look on Emma's is clear as day."
            "She looks horrified at the mere mention of the word!"
            emma.say "No...no...no..."
            emma.say "What if it's too big?"
            emma.say "What if it doesn't fit?"
            "She shakes her head and puts her hands over her ears."
            "All of which means I can't even try to talk her round."
            show emma sad
            emma.say "I...I have to go!"
            emma.say "I have to go right now!"
            hide emma with moveoutright
            "And with that, Emma scurries to the door."
            "She opens it, and in the next second she's gone."
            "I find myself staring at the open doorway."
            "And all I can do is shake my head, cursing internally."
            "What in the hell was I thinking?!?"
            "And how am I ever going to come back from this with Emma?"
            return
    $ DONE["emma_fuck_date_fifth"] = game.days_played
    call sleep ("emma") from _emma_fuck_date_bj
    return

label emma_fuck_date_bj:
    emma.say "I think I'd like to try a blowjob!"
    "I nod and give Emma what I hope is an encouraging smile."
    "She lets me lead her over to the bed, and we perch on the edge."
    show emma bj with fade
    "Slowly and with great care, we undress each other."
    show emma bj chub
    "I hear Emma gulp at her first sight of my cock."
    show emma bj hard lookup blush
    call emma_dick_reactions from _emma_fuck_date_bj_dick_reaction
    "It's already good and hard, standing to attention."
    "But it's not like I can help it, sitting next to her."
    "Emma's so cute and her body's so sexy..."
    show emma bj handjob
    "Suddenly I snap out of it as I feel her touch it."
    "She's tentative at first, as if scared that it'll bite."
    "But little by little, Emma gains in confidence."
    show emma bj speed
    "Before I know it, she's stroking it faster and faster."
    show emma bj smile
    "And I swear that I can see a hunger building in her eyes."
    show emma bj chub lookdown
    "Emma licks her lips, and I sense she's almost ready."
    emma.say "I never thought it'd be this big!"
    emma.say "And my mouth is so small..."
    mike.say "You don't have to swallow it whole, Emma."
    show emma bj lookup
    mike.say "Just do what feels good to begin with."
    mike.say "And most important of all - remember that blowjob's just a figure of speech!"
    "Emma giggles at this, her cheeks flushing a little."
    show emma bj lookdown
    "Then she seems to take this as a good omen, leaning forward and opening her mouth..."
    show emma bj blowjob -speed
    show mouth_insert emma zorder 1 at zoomAt(1, (40, 160))
    "What follows is a blowjob like nothing I've had before."
    "It's not mind-blowing and it's certainly not awful."
    "But it feels like Emma's taking me along on her journey."
    "She starts as timidly as I'd expected, barely kissing the tip."
    "And then she sticks out the tip of her tongue to lick at it."
    "But nothing that she experiences seems to put her off."
    "Quite the opposite, she becomes bolder with each second that passes."
    "Soon enough, Emma has the head of my cock in her mouth."
    "She moans in between the gentle sucking and caressing."
    "And I can see that she's starting to enjoy it more too."
    "Emma takes a little more of the length into her mouth at a time."
    "Soon enough she's swallowing almost half of my length."
    "She could probably take more of it without a problem."
    "But this isn't the time to force deep-throat on her!"
    "And so I just leave it to her, letting her find her way."
    "Emma's cheeks are an even deeper shade of red by now."
    show emma bj lookup
    "And when she sneaks a glance up at me, her eyes are full of emotion."
    "Sure, there's a measure of shame in there at what she's doing."
    "But I can also see that she's massively turned-on too."
    "And that most of the shame is her actually getting off on it."
    "As meek as she might be, Emma's clearly enjoying sucking my cock!"
    "That knowledge is as much of a turn-on for me as the blowjob itself!"
    "Knowing that she's conquering her natural fears for my sake."
    "That she's trying so hard to please me."
    "Well, it makes the whole thing that much more special."
    show emma bj lookdown speed
    "Emma rubs her hand up and down my shaft."
    show emma bj lookup
    "And at the same time her head bobs back and forth."
    "To say this is her first time, she's doing a damn good job!"
    "In fact, I think..."
    "No, I know that she's about to make me cum!"
    menu:
        "Swallow":
            "I have no idea if Emma knows what's about to happen."
            "And the moment I open my mouth to tell her, it does!"
            show emma bj -speed shocked creampie
            show mouth_insert emma cum
            with hpunch
            "I see her eyes go wide as I lose it."
            with hpunch
            "She coughs and chokes, struggling to handle it."
            show emma bj -handjob scare closed hard dickcum with hpunch
            "Emma might have wanted to spit it out."
            "But all she can do is desperately swallow!"
            $ emma.sub += 1
            $ emma.love += 1
            show emma bj lookup ahegao cum onmouth limp
            hide mouth_insert
        "Facial" if emma.sub >= 50:
            "I don't want to have Emma choke on her first attempt."
            show emma bj -speed -handjob shocked hard surprised
            hide mouth_insert
            "And so I pull my cock out of her mouth before it's too late."
            "She looks up at me with a puzzled expression."
            "My guess is that Emma thinks she did something wrong."
            show emma bj chub
            "But there's no time to put her right."
            show emma bj cumshot closed ahegao with hpunch
            "And that's because I shoot my load into her face a second later."
            show emma bj -cumshot cum onface onmouth limp with hpunch
            "Emma squeals in alarm as the cum stripes her red cheeks."
            with hpunch
            "She squeezes her eyes shut as tightly as she can."
            "But the fact that she's yelping means her mouth is open."
            show emma bj -onmouth scare
            "I don't know how big of a mouthful she gets."
            "Though it's enough to make her cough and gag as she swallows it down."
            $ emma.sub += 2
            show emma bj lookup
    "Afterwards she looks up at me, her eyes watering."
    "But she has a look on her face that tells me she's seeking approval."
    emma.say "D...did I..."
    emma.say "Did I do it right?"
    "I try to ignore the cum that's dripping from her lips."
    "And instead I nod and give her what I hope is a reassuring smile."
    mike.say "That was amazing, Emma!"
    mike.say "You did great."
    return

label emma_fuck_date_sixth(loop=False):
    $ game.play_music("music/roa_music/city_nights.ogg")
    $ game.room = "bedroom1"
    scene bg bedroom1
    show emma date blazer
    with fade
    "I've been looking forward to getting Emma alone all evening."
    "In fact, it's been the only thing on my mind the whole time."
    "But on the way back to my place she started to go quiet."
    "And by the time we're in my bedroom, I can see she's preoccupied too."
    "Only I'm not sure that she's obsessing about what happens now for the same reason!"
    mike.say "Ah, Emma..."
    mike.say "Are you feeling okay?"
    show fx exclamation
    "Emma all but jumps at the sound of my voice."
    "It's as if the question's exposed her nerves all at once."
    emma.say "What...I..."
    show emma annoyed
    emma.say "N...no, [hero.name]..."
    emma.say "I'm fine!"
    if emma.flags.sixth_gone_ahead == False:
        mike.say "Well..."
        mike.say "You don't look fine, Emma."
        mike.say "In fact, you look scared stiff!"
        show emma normal
        "Emma's smile is pained."
        "But it also looks genuine."
        emma.say "I...I guess I'm a little nervous."
        emma.say "This is kind of a big deal for me!"
        emma.say "And...and what if it IS too big for me!"
        show emma annoyed
        emma.say "I suppose that sounds silly to you?"
        "I shake my head, eager to allay Emma's fears."
        mike.say "No, Emma, it doesn't."
        mike.say "I'm a little nervous too!"
        "Emma's eyes go wide at this and she shakes her head."
        show emma normal
        emma.say "Really?!?"
        emma.say "I thought you did this kind of thing all the time?"
        mike.say "This isn't my first time, Emma."
        mike.say "But I'm not exactly a Casanova either!"
        show emma blush
        "Emma chuckles at this, her cheeks flushing a little."
        "But all that does is make her look that much sexier!"
        emma.say "You're such a liar, [hero.name]!"
        emma.say "But I trust you all the same."
    show emma normal
    emma.say "Just...be gentle with me, okay?"
    "I nod and begin to strip off my clothes as I walk to the bed."
    "Emma follows behind me, doing the same thing at a slower pace."
    show emma naked with dissolve
    "And by the time I'm naked, she's pulling off her last item of clothing."
    "She stays silent as I guide her down onto the bed."
    if emma_too_small(10):
        "I can't help but wonder if I should do this. I don't know if her exercises have progressed to a point where she's ready to take this step."
        menu:
            "Go ahead":
                pass
            "Suggest something else":
                mike.say "We don't have to go all the way tonight."
                call emma_fuck_date_too_small from _emma_fuck_date_sixth_offer
                if not loop:
                    $ game.pass_time(1)
                    call sleep ("emma") from _emma_fuck_date_sixth_offer_sleep
                return
    if loop:
        return
    $ emma.flags.sixth_gone_ahead = True
    call emma_fuck_date_missionary (0) from _emma_fuck_date_sixth_missionary
    if _return == "too_small":
        call emma_fuck_date_too_small from _emma_fuck_date_sixth_too_small
    $ DONE["emma_fuck_date_sixth"] = game.days_played
    $ game.pass_time(1)
    call sleep ("emma") from _emma_fuck_date_sixth_sleep
    return

label emma_fuck_date_missionary(sexperience_min):
    show emma missionary with fade
    "All the time those big, green eyes are staring up at me."
    "They're full of trepidation, but also with trust."
    "Which almost gets me harder than the sight of her naked body."
    show emma missionary mike mikehand
    "I lower myself down, Lifting Emma's legs as I do so."
    "And once I'm atop her, I look her in the eye and nod."
    call emma_dick_reactions from _emma_fuck_date_missionary_dick_reaction
    "Still smiling nervously, she nods in return."
    show emma missionary pleasure
    "Well, here goes nothing."
    "But wait a minute - where is it actually going?"
    menu:
        "Fuck her ass" if hero.sexperience >= 20 and emma.sub >= 50:
            "I know that Emma's worried about me being too big for her."
            "So maybe I need to think outside of the box on this one."
            "While it might be tighter at first, her ass could maybe take more."
            "And the more I think about it, the more I come to like the idea."
            "Sure, it might sound crazy with how nervous Emma is right now."
            "But maybe doing something this outrageous will help her get over it?"
            mike.say "Emma, you're going to have to trust me, okay?"
            emma.say "Wh...what's that?"
            emma.say "What do you mean?!?"
            "Before she can get cold feet, I make my move."
            "I already have Emma's legs in the air."
            "So her ass is presenting a pretty sweet target."
            show emma missionary anal
            "Without hesitation, I push the head of my cock between her buttocks."
            "Her ass is as tight as I expected, but I push on regardless."
            emma.say "Ooh..."
            emma.say "Oh god..."
            emma.say "That's...that's my butt!"
            "I can hear the trepidation in Emma's voice."
            "But I do my best to ignore it as I force my way into her."
            show emma missionary normal
            emma.say "Oh...oh...oooh..."
            emma.say "Mmm..."
            show emma missionary pleasure
            emma.say "Oh god...what are you doing to me!"
            "I can hear the change in Emma's voice as I sink deeper in."
            "And much to my relief, the alarm simply melts away."
            "In it's place I can hear a growing sense of intrigue."
            "Intrigue that quickly transforms into delight."
            show emma missionary normal
            "Emma gazes up at me, her eyes wide with amazement."
            "And with each subsequent thrust, they glaze over a little more."
            "Pretty soon she's totally lost, overtaken by the sensations."
            "As soon as I realise that, I feel a sense of relief flood my body."
            "But that only lasts for a couple of seconds."
            show emma missionary pleasure
            "And then I can feel my desire for Emma take over!"
            "It's like all the care that I've taken finally paid off."
            "I've got past the nerves and the shyness that she had."
            "So now there's nothing to keep me from indulging myself!"
            "And that's just what I do."
            "Emma's ass is incredibly tight around my cock."
            "That and her reaction tell me she's never done this before."
            "But from the look on her face, my bet is that she'll want it again!"
            "Her entire body is moving in time with my thrusts."
            "Head swaying back and forth, breasts bouncing on her chest."
            "And all that makes me want to do is fuck her even harder."
            "I lean forwards, pushing down on Emma's thighs."
            "This is almost enough to fold her in half."
            "And it means that all of my weight is behind my cock too!"
            show emma missionary ahegao
            "I see Emma's eyes begin to roll back into her head."
            "She starts to twitch, letting me know that she's about to cum."
            "And the muscles of her ass are squeezing my cock like crazy."
            "Which means I'm going to do the same!"
            call cum_reaction (emma, 'anal', sexperience_min) from _call_cum_reaction_182
            if _return == 'anal_inside':
                "I don't know if I could pull out of Emma if I wanted to."
                show emma missionary creampie with vpunch
                $ emma.sub += 2
                "And in the end it doesn't matter, as I shoot my load into her."
                with vpunch
                "She whines and wriggles the whole time she's taking it."
                show emma missionary pleasure with vpunch
                "And for a moment I'm sure that she must have actually passed out!"
                "But then I hear her begin to mumble something."
                "And I strain to listen..."
                emma.say "Y...you came..."
                emma.say "You came...in my ass..."
                emma.say "And I loved it!"
            elif _return == 'anal_outside':
                show emma missionary -anal
                show chest_insert emma zorder 1 at zoomAt(1, (860, 100))
                show belly_insert emma zorder 2 at zoomAt(1, (0, 380))
                "I have no idea how I manage to pull out in time."
                show emma missionary cumshot with vpunch
                "But that's just what I do before I shoot my load."
                with vpunch
                "Emma whines and wriggles as I yank my cock out of her ass."
                if not CONDOM:
                    show emma missionary -cumshot dickcum cumbody
                    show chest_insert emma cum
                    show belly_insert emma cum
                    $ emma.sub += 1
                    with vpunch
                    "And then she yelps as the sticky streamers of cum spatter her breasts and belly."
                "I hear her begin to mumble something."
                "And I strain to listen..."
                emma.say "Y...you came..."
                if not CONDOM:
                    emma.say "You came...all over me..."
                    emma.say "But I loved it!"
                hide chest_insert
                hide belly_insert
            $ emma.flags.anal += 1
        "Fuck her pussy":
            "I know that I need to be careful here, to take thing slow."
            "So I set my sights on Emma's neat little pussy."
            "Sure, it looks pretty tiny from this angle."
            "But somethings really are bigger on the inside..."
            show emma missionary normal
            call check_condom_usage (emma, 180) from _call_check_condom_usage_37
            if _return == False:
                return
            if CONDOM:
                show emma missionary condom
            "At first I just tease Emma's lips with the head of my cock."
            "The idea was to get her used to the feeling and relax her a little."
            show emma missionary pleasure
            "But the way that she wriggles and squirms at the sensation."
            "And the squeals of delight that she lets out too..."
            "Seriously - I want her so badly right now!"
            "How can a girl this sexy be so bashful?"
            "In fact, I'm so wrapped up in her that I don't notice what I'm doing."
            show emma missionary vaginal
            "And in a moment more, the head of my cock slips inside of her."
            "The feeling takes me by complete surprise, making me gasp."
            "Emma's so neat and so tight down there."
            "All I want to do is sink deeper into her."
            show emma missionary normal
            if emma_too_small(10):
                emma.say "Ow...ow...ow..."
                emma.say "Please, [hero.name]..."
                emma.say "You're hurting me!"
                "I can't be more than an inch into Emma's pussy by now."
                "But I can see from the look on her face that she's serious."
                "And as much as I want this, it's not worth hurting her to get it."
                hide emma
                show emma naked
                with fade
                "Which is why I pull out of her as quickly as I can."
                mike.say "I...I'm sorry, Emma."
                mike.say "Are you okay?"
                "Emma still looks more than a little pained."
                "And yet she forces a smile onto her face all the same."
                emma.say "No, I'm sorry, [hero.name]."
                emma.say "You're just so...large!"
                emma.say "I don't think this is going to work..."
                "I'm disappointed to say the least."
                "But I force a smile onto my face too."
                mike.say "Don't worry about it, Emma."
                mike.say "We'll figure something out."
                mike.say "We don't have to do this tonight. Maybe you'd like to do something else instead?"
                $ emma.love -= 10
                $ emma.sub -= 10
                return "too_small"
            else:
                emma.say "Oh...oh god..."
                emma.say "That feels...SO good!"
                if renpy.has_label("emma_achievement_5") and not game.flags.cheat:
                    call emma_achievement_5 from _call_emma_achievement_5
                show emma missionary pleasure
                emma.say "Please - do it some more!"
                "I wasn't expecting to feel the relief that those words inspire in me."
                "But hearing that Emma's actually liking what I'm doing to her..."
                "Well, it's almost more of a turn on than the sensation of being inside her!"
                "It's all that I can do to keep myself from going to fast."
                "But I summon all of my willpower and manage to hold back."
                "I need to take this slowly, give her a little at a time."
                "Too much right now would be as bad as being too big for her!"
                show emma missionary normal
                "And I don't have to wait long to see that I was right."
                "Emma's eyes become wider with each motion of my body."
                "She gasps and pants with more intensity too."
                "And I can almost see her pupils beginning to dilate."
                "Her eyes glazing over as the sensations overtake her."
                "I'm picking up speed more rapidly now."
                "Thrusting in and out of Emma faster with each passing second."
                "We're way past the limits of her anxiety and nerves holding her back."
                show emma missionary pleasure
                "And she's beginning to show what lies beyond them too."
                "Gone is the fear and trepidation that she showed before."
                "And in it's place is an appetite that takes me by surprise."
                "Pretty soon I'm the one that's starting to feel the effects."
                "I'm panting and I can feel the sweat running down my spine."
                "But still Emma takes all that I have to give."
                "And she shows no sign of stopping either!"
                "Her eyes are closed now, her mouth hanging open."
                "Her petite breasts bouncing like crazy on her chest."
                "She starts to twitch, letting me know that she's about to cum."
                "And the muscles of her pussy are squeezing my cock like crazy."
                "Which means I'm going to do the same!"
                call cum_reaction (emma, 'vaginal', sexperience_min, love_min=200) from _call_cum_reaction_183
                if _return == "vaginal_outside":
                    show emma missionary -vaginal
                    show chest_insert emma zorder 1 at zoomAt(1, (860, 100))
                    show belly_insert emma zorder 2 at zoomAt(1, (0, 380))
                    "I have no idea how I manage to pull out in time."
                    show emma missionary cumshot with vpunch
                    "But that's just what I do before I shoot my load."
                    with vpunch
                    "Emma whines and wriggles as I yank my cock out of her pussy."
                    if not CONDOM:
                        show emma missionary -cumshot dickcum cumbody
                        show chest_insert emma cum
                        show belly_insert emma cum
                        $ emma.love += 1
                        with vpunch
                        "And then she yelps as the sticky streamers of cum spatter her breasts and belly."
                    "I hear her begin to mumble something."
                    "And I strain to listen..."
                    emma.say "Y...you came..."
                    if not CONDOM:
                        emma.say "You came...all over me..."
                        emma.say "But I loved it!"
                    hide chest_insert
                    hide chest_insert
                elif _return == "vaginal_condom":
                    "I don't know if I could pull out of Emma if I wanted to."
                    show emma missionary creampie with vpunch
                    "And in the end it doesn't matter, as I shoot my load into her."
                    with vpunch
                    "She whines and wriggles the whole time she's taking it."
                    with vpunch
                    "And for a moment I'm sure that she must have actually passed out!"
                    "But then I hear her begin to mumble something."
                    "And I strain to listen..."
                    emma.say "Y...you came..."
                    emma.say "You came...in my pussy..."
                    emma.say "And I loved it!"
                elif _return == "vaginal_inside_pill":
                    emma.say "I'm on the...pill..."
                    emma.say "Remember?"
                    show emma missionary creampie with vpunch
                    $ emma.love += 2
                    "I'm grateful for the reminder as I shoot my load into Emma."
                    with vpunch
                    "She gasps and wriggles the whole time."
                    with vpunch
                    "And for a moment I think she's passed out!"
                    "But then I hear her, speaking softly."
                    "And I strain to listen..."
                    emma.say "You did it..."
                    emma.say "You came...in my pussy..."
                    emma.say "It was amazing!"
                elif _return == "vaginal_inside_pregnant":
                    emma.say "You already came inside of me once, remember?"
                    emma.say "That's how I ended up with this massive belly!"
                    show emma missionary creampie with vpunch
                    $ emma.love += 3
                    "I almost laugh as I shoot my load into Emma."
                    with vpunch
                    "She gasps and wriggles the whole time, giggling too."
                    with vpunch
                    "Emma falls silent as I feel my orgasm come to an end."
                    "But then I hear her, speaking softly."
                    "And I strain to listen..."
                    emma.say "You did it again."
                    emma.say "It was amazing!"
                elif _return == "vaginal_inside_mad":
                    show emma missionary normal
                    emma.say "Oh no..."
                    emma.say "You have to pull out - now!"
                    "It's too late to stop now."
                    show emma missionary creampie pleasure with vpunch
                    $ emma.love -= 5
                    $ emma.impregnate()
                    "And a second later I shoot my load into her."
                    with vpunch
                    emma.say "Ah..."
                    show emma missionary normal with vpunch
                    emma.say "Oh god...oh god..."
                    emma.say "You came in me..."
                    emma.say "You can't have come in me!"
                    "But I hardly hear what she's saying."
                    "As my mind is still reeling from what just happened."
                elif _return == "vaginal_inside_happy":
                    "I realise at the last moment that I need to act now."
                    "But when I go to pull out, Emma holds me tight."
                    mike.say "Emma - what are you..."
                    "It's too late to stop now."
                    show emma missionary creampie ahegao with vpunch
                    $ emma.love += 5
                    $ emma.impregnate()
                    "And a second later I shoot my load into her."
                    with vpunch
                    emma.say "Ah..."
                    with vpunch
                    emma.say "Oh god...oh god..."
                    emma.say "You came in me, and it feels SO good!"
                    "But I hardly hear what she's saying."
                    "As my mind is still reeling from what she just did."
                    "From what she just made me do!"
    $ emma.sexperience += 1
    return

label emma_fuck_date_seventh(loop=False):
    $ game.play_music("music/roa_music/city_nights.ogg")
    $ game.room = "bedroom1"
    scene bg bedroom1
    show emma date blazer
    with fade
    "Emma's been keeping me entertained most of the night, chatting and joking the whole time."
    "But as soon as we get back to my place, I sense a change in her mood."
    "All of a sudden she clams up and seems to become shy again, like she's had an attack of nerves."
    "If I didn't know her better, I might have thought that she really didn't want to be here."
    "But my guess is that she's waiting for me to take the lead, rather than looking for a way out."
    "So as soon as we're alone in my bedroom, I do the best I can to ease Emma's nerves."
    mike.say "I had a great time tonight, Emma."
    mike.say "It was a lot of fun!"
    show fx exclamation
    "The compliment seems to catch Emma off guard."
    "And she blushes, genuinely smiling at the compliment."
    emma.say "R...really, [hero.name]?"
    emma.say "I was a little nervous."
    emma.say "And when I get nervous I tend to babble."
    emma.say "I just start talking and talking and then I can't stop..."
    show fx exclamation
    "Emma's cheeks turn an even deeper shade of red."
    "And she covers her mouth with her hands."
    emma.say "Oops..."
    emma.say "There I go again!"
    emma.say "I'm sorry, [hero.name]."
    "I wave away her apology and shake my head."
    "I can't help chuckling at her little habits and foibles."
    "In fact, they're one of the things that's endearing me to her."
    "Those quirks make me more fond of Emma every time we meet."
    "Well...that and the fact that she's so cute too!"
    mike.say "It's not a problem, Emma."
    mike.say "I could listen to you talk all night."
    mike.say "Unless you feel like doing something else instead?"
    show emma annoyed
    "I nod in the direction of my bed, trying to keep it casual."
    "Sure, I want to get my hands on Emma in a big way right now."
    "But I don't want to come over like a sex-crazed sleaze either."
    show emma normal
    emma.say "Oh...yeah..."
    emma.say "Of course, [hero.name]!"
    emma.say "Just promise me that you'll be gentle, okay?"
    "I nod and reach out to take Emma by the hand."
    "And then she allows me to lead her over to the bed."
    "Neither of us speaks a word as we begin to undress each other."
    "At first I'm worried that this will make things awkward."
    "But the silence means that it's that much more intense."
    "I can feel the trust that Emma's placing in my every time I touch her."
    "And whenever she touches me in return, I feel her confidence growing."
    show emma naked with dissolve
    "The moment that we're both naked, she makes to lie down on the bed."
    if emma_too_small(15):
        "This isn't a new experience, even with her hesitance. That said, I've come to care a lot about this petite woman, and the idea of hurting her is off-putting."
        "I'm still unsure if her exercises have been enough."
        menu:
            "Go ahead":
                pass
            "Suggest something else":
                mike.say "We don't have to go all the way tonight."
                call emma_fuck_date_too_small from _emma_fuck_date_seventh_offer
                if not loop:
                    $ game.pass_time(1)
                    call sleep ("emma") from _emma_fuck_date_seventh_offer_sleep
                return
    if loop:
        return
    call emma_fuck_date_cowgirl (15) from _emma_fuck_date_seventh_cow_girl
    if _return == "too_small":
        call emma_fuck_date_too_small from _emma_fuck_date_seventh_too_small
    $ DONE["emma_fuck_date_seventh"] = game.days_played
    $ game.pass_time(1)
    call sleep ("emma") from _emma_fuck_date_seventh_sleep
    return

label emma_fuck_date_cowgirl(sexperience_min):
    mike.say "I thought you could go on top tonight."
    mike.say "That way you're the one in control!"
    "For a moment I think that Emma's going to flatly refuse."
    "Or at least that she'll come up with an excuse."
    show emma blush
    "So it comes as a surprise when she nods in agreement."
    emma.say "O...okay, [hero.name]."
    emma.say "I'll give it a try!"
    show emma cowgirl hand_shy with fade
    "Before Emma can change her mind, I lie down on the bed."
    "She holds my hands as she clambers atop me, straddling my midriff."
    "Emma wobbles a little, but then seems to find her balance."
    call emma_dick_reactions from _emma_fuck_date_cowgirl_dick_reaction
    "Then she nods, letting me know that she's as ready as she'll ever be."
    menu:
        "Fuck her ass" if hero.sexperience >= 20 and emma.sub >= 50:
            "I know that I said I was putting Emma in control tonight."
            "But in reality, that's only partly true."
            "A fact that she discovers as soon as we get down to it."
            "Putting my hands firmly upon her waist, I pull her downwards."
            "And at the same time, I aim my cock in a particular direction..."
            emma.say "Whoa..."
            emma.say "What are you..."
            show emma cowgirl anal eyes_close mouth_pleasure
            "Before she can even speak the words, I hit the target."
            "And the head of my cock begins to push into Emma's ass."
            emma.say "Oh god..."
            emma.say "That's my...that's my butt!"
            emma.say "That feels..."
            show emma cowgirl eyes_ahegao
            emma.say "Oh...that feels SO good!"
            "Emma's cheeks are burning like never before as she says this."
            "Her eyes are wide as she sinks down onto my cock."
            "And I watch as they seem to glaze over and roll back into her head."
            "I know this is a big gamble on my part, well out of Emma's comfort zone."
            "But so far the signs are good, and I think this could pay off big time."
            "If I can just push her horizons a little, everything should be fine."
            show emma cowgirl eyes_close -hand_shy at center, stepback(speed=0.1, h=-5, v=-30)
            "And so I begin to move inside of her as gently as I can manage."
            "Slowly and with infinite care, I keep a close eye on how she reacts."
            "My efforts are soon rewarded as Emma seems to lose the power of speech."
            "Instead she's reduced to moaning and sighing as I push into her."
            show emma cowgirl at stepback(speed=0.1, h=-10, v=-20)
            pause 0.3
            show emma cowgirl at stepback(speed=0.1, h=-10, v=-20)
            "Her head flops forwards and back as she rides my cock."
            "And more than once I think that she's going to collapse atop me."
            "But each time Emma seems to save herself at the very last moment."
            "She's like a drunk that's staggering the whole time."
            "And yet is saved from disaster by some weird quirk of gravity!"
            "All of this only serves to make the experience that much better for me."
            show emma cowgirl speed tongueout at stepback(speed=0.1, h=-10, v=-20)
            pause 0.2
            show emma cowgirl at stepback(speed=0.1, h=-10, v=-20)
            "Emma's ass is incredibly tight, squeezing my cock as I fuck her."
            "And the way that she's rocking and swaying above me redoubles the sensation."
            show emma cowgirl at stepback(speed=0.1, h=-10, v=-20)
            pause 0.2
            show emma cowgirl at stepback(speed=0.1, h=-10, v=-20)
            "I feel like Emma's giving me a private pole-dance."
            "Only the poll that she's using is the one between my legs!"
            "I vaguely remember trying to start out slow."
            show emma cowgirl at stepback(speed=0.1, h=-10, v=-20)
            pause 0.2
            show emma cowgirl at stepback(speed=0.1, h=-10, v=-20)
            "But by now, I seem to have picked up speed without noticing."
            "I can feel the perspiration standing out on my forehead."
            show emma cowgirl at stepback(speed=0.1, h=-10, v=-20)
            pause 0.2
            show emma cowgirl at stepback(speed=0.1, h=-10, v=-20)
            "I'm gasping as my heart pounds in my chest."
            "Yet none of that stops me from pounding away at Emma."
            show emma cowgirl at stepback(speed=0.1, h=-10, v=-20)
            pause 0.2
            show emma cowgirl eyes_open with vpunch
            "That is until the moment that she cries out and clings onto me."
            "At the same time her muscles contract around my cock."
            "And the pressure is more than I can bear."
            "All at once, I can feel myself about to cum!"
            call cum_reaction (emma, 'anal', sexperience_min) from _call_cum_reaction_184
            if _return == 'anal_inside':
                "There's no reason to stop now, and so I keep right on going."
                show emma cowgirl eyes_ahegao cum -speed with vpunch
                $ emma.sub += 2
                "I shoot my load into Emma, holding nothing back as I do so."
                with vpunch
                "The muscles of her ass quiver and she moans the whole time."
                "And then she finally collapses forwards, lying atop me in a heap."
            elif _return == 'anal_outside':
                show emma cowgirl out -tongueout -speed
                show chest_insert emma zorder 1 at zoomAt(1, (840, 40))
                show belly_insert emma zorder 2 at zoomAt(1, (20, 420))
                "I take hold of Emma and pull my cock out of her before it's too late."
                "It pops out of her ass with an audible, almost comical sound."
                "Emma moans at the sensation, almost tumbling off of me."
                show emma cowgirl eyes_close cum with vpunch
                "But a second later, I shoot my load all over her."
                show chest_insert emma cum
                show belly_insert emma cum
                with vpunch
                $ emma.sub += 1
                "And then she yelps as the cum spatters over her breasts and belly."
                hide chest_insert
                hide belly_insert
            $ emma.flags.anal += 1
        "Fuck her pussy":
            "I want to keep things simple, as I already gave Emma a challenge."
            "And so just lie back and let her take the lead."
            "She reaches out and gingerly touches my cock."
            "But then she pauses and looks me straight in the eye."
            "I nod eagerly, urging her on and trying to show her that it's okay."
            "And my reward is the sensation of her taking a firmer hold of my cock."
            call check_condom_usage (emma, 180) from _call_check_condom_usage_38
            if _return == False:
                return
            if CONDOM:
                show emma cowgirl condom
            "Emma's hand is on my cock in almost the next breath."
            show emma cowgirl vaginal eyes_close mouth_pleasure
            "And I watch in silence as she steers it between her legs."
            "I feel rather than see it rub against her lips."
            "And that's because I'm too busy watching the expression on her face."
            "It betrays a mixture of excitement and trepidation."
            "But as I feel myself sink into her, it soon changes..."
            if emma_too_small(15):
                show emma cowgirl eyes_open mouth_shy -hand_shy
                emma.say "Ooh...ooh...ooh..."
                emma.say "Oh no, [hero.name]..."
                emma.say "You're really hurting me!"
                "My cock's no more than an inch into Emma's pussy at this point."
                "But the look on her face and the tone of her voice tell me she's serious."
                "I might be up for this, but it seems like her body's not."
                hide emma
                show emma naked annoyed
                with fade
                "And so I pull my cock out of her as soon as I can."
                mike.say "Geez...I'm really sorry, Emma."
                mike.say "Are you going to be okay?"
                "Emma still has a look of discomfort on her face."
                "And the smile manages a moment later looks forced."
                emma.say "It's not you, [hero.name], it's me."
                emma.say "I'm just too small for you."
                emma.say "I can't handle it..."
                "I do the best I can to hide my disappointment."
                "After all, it's not Emma's fault."
                mike.say "No worries, Emma."
                mike.say "We don't have to do this tonight. Maybe you'd like to do something else instead?"
                $ emma.love -= 10
                $ emma.sub -= 10
                return "too_small"
            else:
                show emma cowgirl eyes_open mouth_pleasure
                emma.say "Oh wow..."
                emma.say "Oh wow..."
                mike.say "Ah..."
                mike.say "Is that wow as in good or bad?"
                show emma cowgirl eyes_close -hand_shy
                "As if to answer the question, Emma makes a sudden move."
                "And that's to push herself downwards with all at once."
                if renpy.has_label("emma_achievement_5") and not game.flags.cheat:
                    call emma_achievement_5 from _call_emma_achievement_5_1
                mike.say "Oh wow..."
                mike.say "Oh wow...wow...wow!"
                "Emma's actions answer my question better than words ever could."
                "And they don't stop letting me know how she feels afterwards either."
                "I almost find myself lying back and letting her take the lead."
                "She pushes down as far as she can go and then begins to ride me."
                "But I can't keep my hands off of her."
                "And I can't keep still either."
                "I take a hold of Emma at the waist."
                show emma cowgirl speed at stepback(speed=0.1, h=-10, v=-20)
                "And then I begin to move beneath her."
                show emma cowgirl at stepback(speed=0.1, h=-10, v=-20)
                pause 0.3
                show emma cowgirl at stepback(speed=0.1, h=-10, v=-20)
                "I try as best I can to match the rhythm she's setting."
                "The effort seems to pay off almost as soon as I get started."
                "Emma lets me know this by squeezing me with her thighs."
                "It's like she's clinging onto me, unable to let go."
                show emma cowgirl at stepback(speed=0.1, h=-10, v=-20)
                pause 0.3
                show emma cowgirl at stepback(speed=0.1, h=-10, v=-20)
                "Every part of her is moving now, dancing to the same rhythm."
                "Her breasts are bouncing up and down above me."
                "Her head is swaying from side to side."
                show emma cowgirl at stepback(speed=0.1, h=-10, v=-20)
                pause 0.3
                show emma cowgirl at stepback(speed=0.1, h=-10, v=-20)
                "And her thighs are slapping noisily against mine."
                show emma cowgirl mouth_shy eyes_ahegao
                emma.say "Oh...oh....oh...."
                emma.say "Oh god..."
                emma.say "I think...I think I'm going to cum!"
                show emma cowgirl at stepback(speed=0.1, h=-10, v=-20)
                pause 0.2
                show emma cowgirl at stepback(speed=0.1, h=-10, v=-20)
                "Almost the same moment that she says this, it happens."
                "Right before my eyes, Emma's orgasm hits."
                show emma cowgirl at stepback(speed=0.1, h=-10, v=-20)
                pause 0.2
                show emma cowgirl at stepback(speed=0.1, h=-10, v=-20)
                "And sure, she might have looked like she was having a good time before."
                show emma cowgirl eyes_close
                "But now she looks like she's been taken on a one way trip to heaven."
                show emma cowgirl at stepback(speed=0.1, h=-10, v=-20)
                pause 0.2
                show emma cowgirl at stepback(speed=0.1, h=-10, v=-20)
                "Emma grinds herself against me as she cums."
                "And it doesn't take long for her to push me over the edge too!"
                call cum_reaction (emma, 'vaginal', sexperience_min, love_min=200) from _call_cum_reaction_185
                if _return == "vaginal_condom":
                    "There's no reason to stop now, and so I keep right on going."
                    with vpunch
                    "I shoot my load into Emma, holding nothing back as I do so."
                    with vpunch
                    "The muscles of her pussy quiver and she moans the whole time."
                    show emma cowgirl mouth_pleasure -speed with vpunch
                    "And then she finally collapses forwards, lying atop me in a heap."
                    emma.say "You did it..."
                    emma.say "You came...in my pussy..."
                    emma.say "It was amazing!"
                elif _return == "vaginal_outside":
                    show emma cowgirl out -speed
                    show chest_insert emma zorder 1 at zoomAt(1, (840, 40))
                    show belly_insert emma zorder 2 at zoomAt(1, (20, 420))
                    "I take hold of Emma and pull my cock out of her before it's too late."
                    "It pops out of her pussy with an audible, almost comical sound."
                    "Emma moans at the sensation, almost tumbling off of me."
                    show emma cowgirl eyes_close cum with vpunch
                    "But a second later, I shoot my load all over her."
                    show chest_insert emma cum
                    show belly_insert emma cum
                    with vpunch
                    $ emma.love += 1
                    "And then she yelps as the cum spatters over her breasts and belly."
                    with vpunch
                    emma.say "You did it..."
                    emma.say "You came...all over me..."
                    emma.say "It was amazing!"
                    show chest_insert
                    show belly_insert
                elif _return == "vaginal_inside_pill":
                    emma.say "Oh...Oh...I'm on the pill..."
                    "I silently thank Emma for the reminder."
                    "And then I take full advantage of the situation."
                    show emma cowgirl eyes_ahegao mouth_pleasure tongueout cum -speed with vpunch
                    $ emma.love += 2
                    "She gasps and moans as I shoot my load into her."
                    show emma cowgirl eyes_close -tongueout with vpunch
                    "Then I hear her gasping breathlessly."
                    with vpunch
                    emma.say "You did it..."
                    emma.say "You came...in my pussy..."
                    emma.say "It was amazing!"
                elif _return == "vaginal_inside_pregnant":
                    emma.say "You already came in me, remember?"
                    emma.say "That's how I got this big!"
                    with vpunch
                    "I almost laugh as I lose it."
                    with vpunch
                    "And she laughs too as it happens."
                    show emma cowgirl eyes_ahegao mouth_pleasure tongueout cum -speed with vpunch
                    $ emma.love += 3
                    "Emma falls silent as I feel my orgasm come to an end."
                    show emma cowgirl eyes_close -tongueout
                    "Then I hear her gasping breathlessly."
                    emma.say "You did it again."
                    emma.say "It was amazing!"
                elif _return == "vaginal_inside_happy":
                    show emma cowgirl eyes_ahegao mouth_pleasure tongueout cum -speed with vpunch
                    $ emma.love += 5
                    $ emma.impregnate()
                    emma.say "Ah..."
                    with vpunch
                    emma.say "Oh god...oh god..."
                    with vpunch
                    show emma cowgirl eyes_close -tongueout
                    emma.say "You came in me, and it feels SO good!"
                    "I hardly hear what Emma's saying."
                    "As I'm only just realising what just happened."
                    "I came inside her, without protection!"
                elif _return == "vaginal_inside_mad":
                    show emma cowgirl eyes_open mouth_pleasure with vpunch
                    emma.say "Oh god..."
                    with vpunch
                    emma.say "Pull out - NOW!"
                    "I only hear Emma's warning when it's too late."
                    show emma cowgirl eyes_ahegao tongueout cum -speed with vpunch
                    $ emma.love -= 5
                    $ emma.impregnate()
                    "And that's a split-second before I cum!"
                    show emma cowgirl eyes_close mouth_shy -tongueout
                    emma.say "Oh god..."
                    emma.say "You came in me..."
                    emma.say "You shouldn't have come in me!"
    $ emma.sexperience += 1
    return

label emma_fuck_date_eighth(loop=False):
    scene bg bedroom1 with fade
    "It's easy to forget that Emma can be pretty shy at the best of times."
    "Especially when we're alone together in my bedroom and about to get it on!"
    "Normally I'd find it easier to keep in mind her quirks and foibles."
    "But that's pretty hard when you're alone with her and there's one thing on your mind..."
    "I guess the date going well made me forget about anything else."
    "Anything apart from getting Emma back to my place!"
    show emma annoyed with dissolve
    "It's only when I see how nervous she looks that I snap out of it."
    "After all, I don't want her to think that's all I see in her."
    mike.say "Are you okay, Emma?"
    mike.say "You've gone a little quiet since we got out of the taxi."
    show emma normal
    "Emma looks up at me, her eyes wide open."
    "And I notice that she has her hands clasped tightly together."
    emma.say "Oh...I...I have?"
    emma.say "I'm sorry, [hero.name]."
    emma.say "I think I'm still a bit on edge."
    emma.say "Or maybe I'm a little drunk..."
    emma.say "I don't know which would be better!"
    "I rub the back of my neck, smiling awkwardly."
    mike.say "Ah..."
    mike.say "I'm not sure if I know the answer to that one either!"
    mike.say "But we don't have to do anything you don't want to, Emma."
    "Suddenly the expression on Emma's face changes dramatically."
    "She goes from looking unsure to concerned, shaking her head."
    show emma annoyed
    emma.say "Oh no, [hero.name]!"
    emma.say "Please don't think that!"
    emma.say "I want to...to do...you know what."
    emma.say "I'm just nervous - that's all!"
    "I nod, trying my best to be the good guy I know I should be."
    mike.say "Okay, Emma."
    mike.say "But you're in control, remember?"
    mike.say "I won't be mad if you say not at any time."
    show emma happy
    "Emma nods and smiles, visibly trying to reassure me."
    "And you know what - it works."
    "Seeing the determination in her eyes as she tries to conquer her fears."
    "Well, it makes me see just how much she's wanting this thing to happen."
    "What more can a guy ask of a girl than that?"
    "Emma walks over to the edge of the bed and turns her back to me."
    show emma topless with dissolve
    "Then she slowly begins to strip off her clothes."
    "I do the same on the other side of the bed, occasionally glancing in her direction."
    "At first I wonder if she'll baulk at me watching her undress."
    "But when she catches my eye, all that happens is her cheeks flushing red."
    "The fact that Emma's still smiling the whole time tells me she actually likes it!"
    show emma naked with dissolve
    "Emma finishes undressing first and climbs onto the bed."
    "And then she playfully pats the mattress beside her."
    emma.say "W...why don't you come over here?"
    emma.say "I mean, if you want to?"
    "As soon as I'm done stripping off, I hurry to join Emma."
    mike.say "Of course I want to, Emma!"
    if emma_too_small(15):
        "This isn't a new experience, even with her hesitance. That said, I've come to care a lot about this petite woman, and the idea of hurting her is off-putting."
        "I'm still unsure if her exercises have been enough."
        menu:
            "Go ahead":
                pass
            "Suggest something else":
                mike.say "We don't have to go all the way tonight."
                call emma_fuck_date_too_small from _emma_fuck_date_eighth_offer
                if not loop:
                    $ game.pass_time(1)
                    call sleep ("emma") from _emma_fuck_date_eighth_offer_sleep
                return
    if loop:
        return
    call emma_fuck_date_reverse_cowgirl (25) from _emma_fuck_date_eighth_reverse_cowgirl
    if _return == "too_small":
        call emma_fuck_date_too_small from _emma_fuck_date_eighth_too_small
    $ DONE["emma_fuck_date_eighth"] = game.days_played
    $ game.pass_time(1)
    call sleep ("emma") from _emma_fuck_date_eighth_sleep
    return

label emma_fuck_date_reverse_cowgirl(sexperience_min):
    mike.say "I've been thinking about this moment all night!"
    show emma blush
    "Emma's cheeks visibly darken at this."
    "I can genuinely see them go from red to crimson."
    "And for a moment I think that I might have said the wrong thing."
    emma.say "M...me too!"
    emma.say "I'm really excited!"
    "Emma takes me completely by surprise, planting a kiss on my lips."
    "But the surprise only lasts for a few seconds before I return it."
    "We end up in a tangle of limbs as we kiss, wrapped together."
    scene emma reverse with fade
    "And it's almost by accident that Emma ends up atop me."
    "Atop me and facing away, so that she has to look back over her shoulder."
    "Or at least she would, it my cock didn't choose that exact moment to pop up."
    "Emma literally jumps, letting out a cry of surprise and alarm."
    emma.say "Ah!"
    emma.say "Oh god!"
    emma.say "I...I didn't know they did that!"
    call emma_dick_reactions from _emma_fuck_date_reverse_cowgirl_dick_reaction
    "I shake my head and chuckle in amusement."
    "And then I gently take hold of Emma by the haunches."
    "She doesn't stop me as I slowly guide her towards it."
    "But she can't see just where it's headed..."
    menu:
        "Fuck her ass" if hero.sexperience >= 30 and emma.sub >= 50:
            "I feel like Emma's putting herself into my hands."
            "And I guess she is quite literally as well."
            "And so I take a chance and put that trust to the test."
            "I guide Emma down onto my cock."
            "But it's not aimed at the hole she thinks I'm interested in..."
            show emma reverse anal
            emma.say "Oooh..."
            emma.say "You're going to..."
            "Emma squeals as I push onwards, ignoring her words."
            "By now my cock is already inching into her."
            show emma reverse anal down
            emma.say "Oh, [hero.name]..."
            emma.say "You...you're in my ass!"
            emma.say "Mmm..."
            emma.say "Oh...please..."
            emma.say "Don't stop now!"
            show emma reverse anal pleasure
            "Emma has her back to me as she says this."
            "And her head is already drooping forwards too."
            "All I can see of her face is the curve of her cheek."
            "But this is already flushed from the sensations that she's feeling."
            "I take the pleas she's making and her physical reaction as a good sign."
            show emma reverse up
            "And I slowly begin to move inside of her ass."
            "Emma responds almost as soon as I do this."
            "She braces herself with one hand placed on my thigh."
            "And the other she keeps free to explore her own body."
            "All I can see of this is the position of her elbow."
            show emma reverse down
            "So I have to guess what that hand is doing."
            "But it's not hard to figure out that it goes straight to her chest."
            show emma reverse up
            pause 0.35
            show emma reverse down
            "Emma sighs and gasps as she rides my cock."
            "And I imagine that she's pinching at her nipples too."
            show emma reverse up
            pause 0.35
            show emma reverse down
            "Squeezing them between finger and thumb, desperate for release."
            "Part of me wishes that I could see the look on Emma's face."
            show emma reverse up
            pause 0.35
            show emma reverse down
            "And I wouldn't mind watching what she's doing with her hands either!"
            show emma reverse up
            pause 0.25
            show emma reverse fast
            pause 0.15
            show emma reverse down
            "But instead I concentrate on keeping up a steady rhythm."
            "My speed increases almost without my knowing it."
            show emma reverse up
            pause 0.25
            show emma reverse fast
            pause 0.15
            show emma reverse down
            "I only realise that I'm going faster as Emma reacts in kind."
            show emma reverse up
            pause 0.2
            show emma reverse fast
            pause 0.1
            show emma reverse down at startle(0.05,-10)
            "Her gasps become that much more pronounced."
            "And I see her hand creeping downwards from her breasts."
            "It disappears between her thighs, rubbing desperately."
            show emma reverse up
            pause 0.2
            show emma reverse fast
            pause 0.1
            show emma reverse down at startle(0.05,-10)
            "Emma begins to wriggle on my cock as she plays with herself."
            show emma reverse up
            pause 0.2
            show emma reverse fast
            pause 0.1
            show emma reverse down anal ahegao at startle(0.05,-10)
            emma.say "Ah..."
            emma.say "I...I can't take it!"
            emma.say "Please...do it!"
            show emma reverse up
            pause 0.2
            show emma reverse fast
            pause 0.1
            show emma reverse down at startle(0.05,-10)
            pause 0.2
            show emma reverse up
            pause 0.2
            show emma reverse fast
            pause 0.1
            show emma reverse down at startle(0.05,-10)
            "With Emma begging me to cum, I feel my body respond."
            "I hold onto her more firmly as begin to cum."
            call cum_reaction (emma, 'anal', sexperience_min) from _call_cum_reaction_186
            if _return == 'anal_inside':
                show emma reverse up
                pause 0.2
                show emma reverse fast
                pause 0.1
                show emma reverse down at startle(0.05,-10)
                pause 0.2
                show emma reverse up
                pause 0.2
                show emma reverse fast
                pause 0.1
                show emma reverse down with vpunch
                pause 0.2
                show emma reverse up creampie
                $ emma.sub += 2
                "I shoot my load into Emma without a moment of hesitation."
                with vpunch
                "And I swear my hands are the only thing keeping her in place!"
                with vpunch
                "Emma's entire body bucks and twists in my grip."
                "But I hold her down the entire time, letting her ride it out."
                "Only then do I lower her gently onto the bed."
                "And she lies there, panting and squirming still."
            elif _return == 'anal_outside':
                show emma reverse up
                pause 0.2
                show emma reverse fast
                pause 0.1
                show emma reverse down at startle(0.05,-10)
                pause 0.2
                show emma reverse up
                pause 0.2
                show emma reverse fast
                pause 0.1
                show emma reverse up -anal pleasure
                "At the last moment I hoist Emma up into the air."
                "She yelps in surprise as my cock pops out of her ass."
                "Then she yelps again, but this time in alarm."
                show emma reverse pleasure cumshot with vpunch
                "And she cries out in surprise as I shoot my load over her."
                show emma reverse bodycum with vpunch
                "The cum spatters Emma's back and buttocks, striping them white."
                show emma reverse -cumshot with vpunch
                $ emma.sub += 1
                "Then she collapses onto the mattress beside me."
            $ emma.flags.anal += 1
        "Fuck her pussy":
            "Emma gazes down at my cock, as if entranced by the sight of it."
            "She bites her lip, and then reaches out to take a gentle hold."
            "And even though her touch is light, it sends a jolt of excitement through me."
            "That's because I know just what it takes for her to be so bold."
            "I almost find myself holding my breath as I wait for what comes next."
            "As Emma raises herself up just enough to aim my cock at her pussy..."
            call check_condom_usage (emma, 180) from _call_check_condom_usage_39
            if _return == False:
                return
            if CONDOM:
                show emma reverse condom
            "Emma raises herself up again."
            "And then she lowers herself slowly down."
            "I feel the head of my cock press against her lips."
            show emma reverse vaginal
            "And then it pushes inside of her."
            "Emma moans at the sensation."
            "And I can't help making a similar sound too."
            if emma_too_small(15):
                emma.say "Ouch...ouch...ouch..."
                emma.say "Ooh, [hero.name]..."
                emma.say "That hurts so bad!"
                "I'm hardly even inside Emma's pussy."
                "But she looks over her shoulder at me in alarm."
                "And I instantly know that it's not going to happen tonight."
                hide emma
                show emma naked annoyed
                with fade
                "Which means I have to pull out of her as gently as I can."
                mike.say "Sorry, Emma."
                mike.say "I...I didn't mean to hurt you."
                "Emma smiles through the pain she's feeling."
                "And she manages to shake her head."
                emma.say "It's okay...it's okay..."
                emma.say "I just can't handle something so big."
                emma.say "I'm sorry too, [hero.name]."
                "I force a smile onto my face."
                "Sure, I'm disappointed with how this played out."
                "But Emma doesn't deserve to take the blame."
                mike.say "Don't apologise, Emma."
                mike.say "It's not your fault."
                $ emma.love -= 10
                $ emma.sub -= 10
                return "too_small"
            else:
                emma.say "Oh my..."
                emma.say "Oh my oh my..."
                "I'm about to ask Emma if she's enjoying herself."
                "But then she sits down on me with all of her weight."
                if renpy.has_label("emma_achievement_5") and not game.flags.cheat:
                    call emma_achievement_5 from _call_emma_achievement_5_2
                show emma reverse down pleasure
                "I hear her buttocks slap against my belly."
                "And I feel the way her tight little pussy is squeezing me too."
                show emma reverse up
                pause 0.35
                show emma reverse down
                "But I only have a fraction of a second to savour it."
                show emma reverse up
                pause 0.25
                show emma reverse fast
                pause 0.15
                show emma reverse down
                "That's because Emma begins riding me furiously a moment later!"
                "All I can do is hold onto her for dear life."
                show emma reverse up
                pause 0.2
                show emma reverse fast
                pause 0.1
                show emma reverse down at startle(0.05,-10)
                "Her petit little body goes up and down like a jackhammer."
                show emma reverse up
                pause 0.2
                show emma reverse fast
                pause 0.1
                show emma reverse down at startle(0.05,-10)
                "And somehow her sparse weight is enough to pin me down."
                show emma reverse up
                pause 0.2
                show emma reverse fast
                pause 0.1
                show emma reverse down at startle(0.05,-10)
                "Emma's well and truly taking the lead here."
                "But that's not to say that I'm complaining."
                "I simply lie back and let her have her way."
                show emma reverse up
                pause 0.2
                show emma reverse fast
                pause 0.1
                show emma reverse down at startle(0.05,-10)
                pause 0.2
                show emma reverse up
                pause 0.2
                show emma reverse fast
                pause 0.1
                show emma reverse down at startle(0.05,-10)
                "The whole time enjoying her sensual side as it emerges."
                "Once she forgets herself, Emma seems to be transformed."
                "That shy little thing is gone."
                "And in it's place is a lusty imp."
                "One that's got a massive itch to scratch too!"
                show emma reverse up
                pause 0.2
                show emma reverse fast
                pause 0.1
                show emma reverse down at startle(0.05,-10)
                pause 0.2
                show emma reverse up
                pause 0.2
                show emma reverse fast
                pause 0.1
                show emma reverse down at startle(0.05,-10)
                "Emma's hands roam all over her body as she rides me."
                "One moment she's massaging her breasts, pinching her nipples."
                "The next she's tracing the shape of her torso or thighs."
                "And finally her fingers descend below her waist."
                "Once there, they begin to play with her pussy."
                "Emma rubs her fingertips between the folds."
                show emma reverse up
                pause 0.2
                show emma reverse fast
                pause 0.1
                show emma reverse down at startle(0.05,-10)
                pause 0.2
                show emma reverse up
                pause 0.2
                show emma reverse fast
                pause 0.1
                show emma reverse down at startle(0.05,-10)
                "And she does the same to her clit too."
                emma.say "Ah..."
                emma.say "Ah shit..."
                "My eyes open wide at the sound of Emma swearing."
                "She's normally anything but foul-mouthed."
                "And so I know now that she must be worked up to a crazy degree."
                "But rather than put me off, it just serves to make me more excited."
                show emma reverse up
                pause 0.2
                show emma reverse fast
                pause 0.1
                show emma reverse down at startle(0.05,-10)
                pause 0.2
                show emma reverse up
                pause 0.2
                show emma reverse fast
                pause 0.1
                show emma reverse down at startle(0.05,-10)
                "I begin thrusting up and into Emma like never before."
                "And it's not long before my efforts have an audible effect."
                emma.say "F...fuck..."
                emma.say "I'm going to..."
                emma.say "Going to fucking cum!"
                show emma reverse up
                pause 0.2
                show emma reverse fast
                pause 0.1
                show emma reverse down at startle(0.05,-10)
                pause 0.2
                show emma reverse up
                pause 0.2
                show emma reverse fast
                pause 0.1
                show emma reverse down ahegao at startle(0.05,-10)
                "As if they were a magic spell or a firm command, Emma's words affect me too."
                "And I feel myself cumming at the same time..."
                call cum_reaction (emma, 'vaginal', sexperience_min, love_min=200) from _call_cum_reaction_187
                if _return == "vaginal_condom":
                    "Because we took precautions beforehand, I can keep on going."
                    show emma reverse up
                    pause 0.2
                    show emma reverse fast
                    pause 0.1
                    show emma reverse down at startle(0.05,-10)
                    pause 0.2
                    show emma reverse up
                    pause 0.2
                    show emma reverse fast
                    pause 0.1
                    show emma reverse down with vpunch
                    "Emma bucks and sways as I lost it inside of her."
                    with vpunch
                    "Then she topples off of my cock."
                    show emma reverse pleasure with vpunch
                    "And she collapses onto the bed beside me."
                    emma.say "Mmm..."
                    emma.say "That felt so good..."
                    emma.say "I love it when you cum inside of me like that!"
                elif _return == "vaginal_outside":
                    show emma reverse up
                    pause 0.2
                    show emma reverse fast
                    pause 0.1
                    show emma reverse down at startle(0.05,-10)
                    pause 0.2
                    show emma reverse up
                    pause 0.2
                    show emma reverse fast
                    pause 0.1
                    show emma reverse up -vaginal
                    "I need to take control now, before it's too late!"
                    "But in the end I have to all but tear Emma off of me!"
                    "My cock comes out of her with an audible pop."
                    show emma reverse pleasure cumshot with vpunch
                    "And she cries out in surprise as I shoot my load over her."
                    show emma reverse bodycum with vpunch
                    "The cum spatters Emma's back and buttocks, striping them white."
                    show emma reverse -cumshot with vpunch
                    $ emma.love += 1
                    emma.say "Mmm..."
                    emma.say "That feels so warm..."
                    emma.say "So good against my skin!"
                elif _return == "vaginal_inside_pill":
                    emma.say "Oh..."
                    emma.say "Cum in me..."
                    emma.say "I'm on the pill!"
                    "I hadn't forgotten this fact."
                    "But it's nice to have Emma give me permission."
                    show emma reverse up
                    pause 0.2
                    show emma reverse fast
                    pause 0.1
                    show emma reverse down at startle(0.05,-10)
                    pause 0.2
                    show emma reverse up
                    pause 0.2
                    show emma reverse fast
                    pause 0.1
                    show emma reverse down with vpunch
                    pause 0.2
                    show emma reverse up creampie
                    $ emma.love += 2
                    "Emma bucks and sways as I lost it inside of her."
                    with vpunch
                    "Then she topples off of my cock."
                    show emma reverse pleasure with vpunch
                    "And she collapses onto the bed beside me."
                    emma.say "Mmm..."
                    emma.say "That felt so good..."
                    emma.say "I love it when you cum inside of me like that!"
                elif _return == "vaginal_inside_pregnant":
                    emma.say "It's okay..."
                    emma.say "Do it!"
                    emma.say "I'm as pregnant as I can get!"
                    "I smile at the memory of getting Emma pregnant."
                    show emma reverse up
                    pause 0.2
                    show emma reverse fast
                    pause 0.1
                    show emma reverse down at startle(0.05,-10)
                    pause 0.2
                    show emma reverse up
                    pause 0.2
                    show emma reverse fast
                    pause 0.1
                    show emma reverse down with vpunch
                    pause 0.2
                    show emma reverse up creampie
                    $ emma.love += 3
                    "And then I lose it inside of her again."
                    show emma reverse pleasure with vpunch
                    emma.say "Mmm..."
                    emma.say "That felt so good..."
                    emma.say "I love it when you cum inside of me like that!"
                elif _return == "vaginal_inside_happy":
                    show emma reverse up
                    pause 0.2
                    show emma reverse fast
                    pause 0.1
                    show emma reverse down at startle(0.05,-10)
                    pause 0.2
                    show emma reverse up
                    pause 0.2
                    show emma reverse fast
                    pause 0.1
                    show emma reverse down with vpunch
                    pause 0.2
                    show emma reverse up creampie
                    $ emma.love += 5
                    $ emma.impregnate()
                    emma.say "Oh..."
                    with vpunch
                    emma.say "Oh shit...oh shit..."
                    with vpunch
                    emma.say "You came in me - and I love it!"
                    "Suddenly I realise what Emma's actually saying."
                    "And then the reality of what's just happened dawns on me."
                    "I came inside her, and we weren't using a condom!"
                elif _return == "vaginal_inside_mad":
                    show emma reverse pleasure
                    emma.say "Oh..."
                    emma.say "Oh shit...oh shit..."
                    emma.say "You came in me - you can't do that!"
                    "Emma's warning comes too late."
                    show emma reverse up
                    pause 0.2
                    show emma reverse fast
                    pause 0.1
                    show emma reverse down at startle(0.05,-10)
                    pause 0.2
                    show emma reverse up
                    pause 0.2
                    show emma reverse fast
                    pause 0.1
                    show emma reverse down with vpunch
                    pause 0.2
                    show emma reverse up creampie
                    $ emma.love -= 5
                    $ emma.impregnate()
                    "And there's nothing I can do to stop it happening."
                    with vpunch
                    emma.say "Oh no..."
                    emma.say "You did it..."
                    emma.say "You came inside of me!"
    $ emma.sexperience += 1
    return

label emma_fuck_date_ninth(loop=False):
    "Emma keeps pretty quiet on the ride back to my place, not saying much at all."
    "But I can see from the looks that she keeps giving me she's in a good place right now."
    scene bg livingroom
    show emma date
    with fade
    "And even better, she lets me lead her into the house and to my room without protest."
    "Then she hurries through the door as I open it and then follow her in."
    show bg bedroom1
    show emma happy
    with fade
    emma.say "Hurry up, [hero.name]!"
    emma.say "Close the door and get over here already!"
    "It takes me a moment to process what Emma just said to me."
    "She's normally so quiet and shy, needing me to take the lead."
    "And I know she's not actually tearing my clothes off at this point."
    "But trust me, for her, this is pretty forward!"
    mike.say "Oh...okay, Emma."
    mike.say "I'll be right there!"
    "Emma smiles at my obvious enthusiasm, nodding eagerly herself."
    "She claps her hands together and giggles, bouncing on the edge of my bed."
    "By now I'm pretty sure that I'm about to get some action."
    "And so I start stripping off as I walk over to the bed."
    "This seems to strike a chord with Emma too, as she follows my lead."
    "I make it to the bed just as she's pulling off her top."
    "And I catch hold of it just as her head's halfway out of the neck hole."
    show emma normal
    emma.say "Huh..."
    emma.say "Wha...what are you..."
    hide emma
    show emma kiss
    with fade
    $ emma.flags.kiss += 1
    "Without stopping to explain myself, I kiss Emma full on the lips."
    "It only takes a moment for her to realise what's happening."
    "And then she returns the gesture with rapidly increasing passion."
    "As my tongue slips between Emma's lips, I finally pull off her top."
    "By now she's totally absorbed in the act of kissing me."
    "And she hardly seems to notice that she's been released at all!"
    "Emma pretty much clings onto me as I roll on the bed."
    hide emma kiss
    show emma kiss naked
    with dissolve
    $ emma.flags.kiss += 1
    "Somehow we manage to remove the last of each others clothes."
    hide emma
    show emma blush naked
    with dissolve
    "The kiss is broken to the sound of us both panting and gasping."
    "I end up kneeling on the bed."
    if emma_too_small(20):
        "This isn't a new experience, even with her hesitance. That said, I've come to care a lot about this petite woman, and the idea of hurting her is off-putting."
        "I'm still unsure if her exercises have been enough."
        menu:
            "Go ahead":
                pass
            "Suggest something else":
                mike.say "We don't have to go all the way tonight."
                call emma_fuck_date_too_small from _emma_fuck_date_ninth_offer
                if not loop:
                    $ game.pass_time(1)
                    call sleep ("emma") from _emma_fuck_date_ninth_offer_sleep
                return
    if loop:
        return
    call emma_fuck_date_doggy (35) from _emma_fuck_date_ninth_doggy
    if _return == "too_small":
        call emma_fuck_date_too_small from _emma_fuck_date_ninth_too_small
    $ DONE["emma_fuck_date_ninth"] = game.days_played
    $ game.pass_time(1)
    call sleep ("emma") from _emma_fuck_date_ninth_sleep
    return

label emma_fuck_date_doggy(sexperience_min):
    "Emma is half laid, half sprawled in front of me."
    call emma_dick_reactions from _emma_fuck_date_doggy_dick_reaction
    "She makes to get up, lifting herself onto her hands and knees."
    "But I step in before she can go any further."
    show emma doggy noacc with fade
    "Place my hands firmly on her haunches, pushing myself against her."
    emma.say "Oh..."
    emma.say "I...I've never done it this way before!"
    "Emma looks back over her shoulder at me."
    emma.say "You...you promise to be gentle with me?"
    "I nod at this, trying to look as serious and sensitive as I can."
    "But the truth is that I'm itching to get inside of Emma right now!"
    mike.say "Of course, Emma."
    mike.say "I promise you won't feel a thing!"
    mike.say "Well...no...that's not right."
    mike.say "I promise that you WILL feel something."
    mike.say "But it'll be all good!"
    "Emma looks at me with a confused expression on her face."
    "And I know that I have to move things on before it's too late!"
    menu:
        "Fuck her ass" if hero.sexperience >= 40 and emma.sub >= 50:
            "I know it sounds a little strange, but I decide to aim for Emma's ass."
            "I don't know what makes me choose it over her pussy."
            "It just feels like things might go a little easier from this angle."
            "And so I gently part her buttocks and begin to explore between them."
            emma.say "Ooh..."
            emma.say "I think you got a little lost back there!"
            emma.say "Didn't you, [hero.name]?"
            show emma doggy ahegao
            "By way of answer, I push the head of my cock deeper into Emma's ass."
            "There's a pleasant sensation as her muscles try to resist."
            "But then I feel them giving way and I sink further in."
            emma.say "Oh dear..."
            emma.say "That's...that's not an accident!"
            show emma doggy smile
            emma.say "You really are inside of my ass!"
            "I know Emma well enough to gauge the tone of her voice."
            "And right now she sounds like she's actually enjoying herself."
            show emma doggy pleasure
            "I take opportunity to push even further into her."
            "Listening the whole time to make sure Emma's okay."
            "But I don't have to wait long for her to let me know."
            emma.say "Oh god..."
            emma.say "It's SO big..."
            emma.say "And it feels SO good!"
            "Somehow just hearing those words makes it feel that much better."
            "I mean, being inside of Emma's ass felt amazing to begin with."
            "But knowing that she's getting off on it takes things to another level."
            show emma doggy bounce speed
            "I start to pick up speed, slowly at first and then gradually faster."
            "And Emma keeps pace with me as things begin to get more intense."
            "She's grabbing handfuls of the bedclothes and pushing backwards."
            "Her head nods up and down almost in time with my thrusts too."
            emma.say "Yeah...yeah..."
            show emma doggy squirt
            emma.say "Keep going, [hero.name]..."
            emma.say "Faster...harder...please!"
            "Take it from me, I like doing it this way."
            "I mean, I like it a lot!"
            "But it's so much better when I know the other person is too."
            "When you really know that they're loving every single moment."
            "I tighten my grip around Emma's waist."
            "And I pull her towards me with all my strength."
            "She moans with pleasure, getting louder with every passing second."
            "The sound is all that I can hear."
            "It almost drowns out everything else."
            "Making me forget that I'm about to cum!"
            call cum_reaction (emma, 'anal', sexperience_min) from _call_cum_reaction_188
            if _return == 'anal_inside':
                "There's no chance of stopping before I lose it."
                "And neither of us seems to be in the least bit concerned either."
                show emma doggy cum ahegao -speed -bounce saliva with hpunch
                $ emma.sub += 2
                "I keep on going as I shoot my load into Emma."
                with hpunch
                "And she rides my cock the whole time, loving every second."
                show emma doggy limp pleasure -saliva with hpunch
                "Afterwards, she slides off of me and collapses onto the bed."
                "I feel my own legs give out, and I fall onto the mattress beside her."
            elif _return == 'anal_outside':
                "I really don't know how I manage to do it, but I pull out before the end."
                "Emma moans and quakes as she feels my cock being dragged out of her ass."
                show emma doggy cumshot -speed -bounce with hpunch
                $ emma.sub += 1
                "And a moment later I shoot my load over her buttocks."
                with hpunch
                "She cries out as the warm cum spatters over her ass and runs down her legs."
                with hpunch
                "Then she collapses onto the bed, lying still and utterly spent."
                "I feel my own legs give out, and I fall onto the mattress beside her."
            $ emma.flags.anal += 1
        "Fuck her pussy":
            "When in doubt, keep things simple."
            "It's with that in mind I aim for Emma's pussy."
            "But of course, simple doesn't mean boring."
            "As soon as she feels my cock between her legs, Emma lets out a squeak."
            emma.say "Ooh..."
            emma.say "There you are, [hero.name]!"
            call check_condom_usage (emma, 180) from _call_check_condom_usage_40
            if _return == False:
                return
            "I rub the head of my cock against the lips of Emma's pussy."
            "The sensation is incredible, soft, warm and welcoming."
            "And the cooing sound she makes as I do so is almost a bigger turn on."
            "I'm sure that Emma wasn't lying about being nervous."
            "But her body seems to be well ahead of her mind right now."
            "Because her pussy is already pretty slick, wet with anticipation."
            show emma doggy pleasure
            "And she actually gasps as I begin to push my way inside of her."
            if emma_too_small(20):
                emma.say "Ow, ow, ow!"
                emma.say "It REALLY hurts!"
                emma.say "Seriously, [hero.name] - please stop it!"
                "I'm not going to ignore a request like that."
                "And Emma doesn't have to ask twice for me to stop."
                hide emma
                show emma naked annoyed
                with fade
                "I pull my cock out of her pussy as quickly as I can."
                "But even so, she still winces as I do so."
                mike.say "I'm sorry, Emma."
                mike.say "Are you going to be okay?"
                "Emma gives me what I think is supposed to be a reassuring smile."
                "But I can still see the pain in her eyes as she tries to sit comfortably."
                emma.say "I'll be fine, [hero.name], don't worry."
                emma.say "Thanks for listening to me back there."
                emma.say "I guess you're just too much for me to handle right now!"
                $ emma.love -= 10
                $ emma.sub -= 10
                return "too_small"
            else:
                "The sounds that Emma's making are affecting me on two levels."
                "One is that I can hear how much she's enjoying herself right now."
                "And the other is getting me hotter by the second as I listen to her!"
                "At first I find myself holding back all the same."
                "I have the fear of something going wrong, of Emma being in pain."
                "But it doesn't take long for her to cure me of that fear."
                emma.say "Oh...oh god!"
                show emma doggy smile
                emma.say "Your cock...it's so big!"
                emma.say "And it feels SO good!"
                "With those words, Emma effectively lets me off the hook."
                "Now I know that she's loving this as much as I am."
                "And I can begin to give her all that I've got."
                if renpy.has_label("emma_achievement_5") and not game.flags.cheat:
                    call emma_achievement_5 from _call_emma_achievement_5_3
                show emma doggy pleasure speed bounce
                "Without needing to think, I start to pick up speed."
                "My cock thrusts in and out of her, faster each time."
                "And Emma seems to love every moment of it too."
                "She lowers herself down, almost onto the mattress."
                "And she pushes her backside hard against me."
                "I am just seeing the back of her head as she nods desperately."
                emma.say "Oh yeah...yeah..."
                show emma doggy squirt
                emma.say "Keep going, [hero.name], don't stop now..."
                emma.say "Fuck me harder...harder...please!"
                "Emma grabs handfuls of the sheets as she begs for more."
                "And I swear that I can feel every muscle in her body squeezing at once."
                "I redouble my efforts, trying to give Emma all that she could want."
                "But the more I give the more she seems to demand!"
                "The demure girl that asked me to be gentle seems to be long gone."
                "And in her place is a horny little bitch that can't be satisfied!"
                "I tighten my grip around Emma's waist."
                "And I pull her towards me with all my strength."
                "She moans with pleasure, getting louder with every passing second."
                "The sound is all that I can hear."
                "It almost drowns out everything else."
                "Making me forget that I'm about to cum!"
                call cum_reaction (emma, 'vaginal', sexperience_min, love_min=200) from _call_cum_reaction_189
                if _return == "vaginal_condom":
                    "There's no chance of stopping before I lose it."
                    "But as we took precautions, it really doesn't."
                    show emma doggy -speed -bounce with hpunch
                    "I keep on going as I shoot my load into Emma."
                    with hpunch
                    "And she rides my cock the whole time, loving every second."
                    with hpunch
                    "Afterwards, she slides off of me and collapses onto the bed."
                    "I feel my own legs give out, and I fall onto the mattress beside her."
                elif _return == "vaginal_outside":
                    "I really don't know how I manage to do it, but I pull out before the end."
                    "Emma moans and quakes as she feels my cock being dragged out of her pussy."
                    show emma doggy cumshot -speed -bounce with hpunch
                    $ emma.love += 1
                    "And a moment later I shoot my load over her buttocks."
                    with hpunch
                    "She cries out as the warm cum spatters over her ass and runs down her legs."
                    with hpunch
                    "Then she collapses onto the bed, lying still and utterly spent."
                    "I feel my own legs give out, and I fall onto the mattress beside her."
                elif _return == "vaginal_inside_pill":
                    emma.say "Don't stop now!"
                    emma.say "I'm on the pill, remember?!?"
                    "I don't know if I could have pulled out in time."
                    "But Emma's timely reminder means that I don't have to."
                    show emma doggy ahegao cum -speed -bounce saliva with hpunch
                    $ emma.love += 2
                    "I keep on going as I shoot my load into Emma."
                    with hpunch
                    "And she rides my cock the whole time, loving every second."
                    show emma doggy pleasure limp -saliva with hpunch
                    "Afterwards, she slides off of me and collapses onto the bed."
                    "I feel my own legs give out, and I fall onto the mattress beside her."
                elif _return == "vaginal_inside_pregnant":
                    emma.say "Don't stop now!"
                    emma.say "I'm already pregnant, remember?!?"
                    "As if I could forget something like that!"
                    "But I am grateful Emma's timely reminder."
                    "As it means that I don't have to worry about pulling out."
                    show emma doggy ahegao cum -speed -bounce saliva with hpunch
                    $ emma.love += 3
                    "I keep on going as I shoot my load into Emma."
                    with hpunch
                    "And she rides my cock the whole time, loving every second."
                    show emma doggy pleasure limp -saliva with hpunch
                    "Afterwards, she slides off of me and collapses onto the bed."
                    "I feel my own legs give out, and I fall onto the mattress beside her."
                elif _return == "vaginal_inside_happy":
                    emma.say "Wait..."
                    emma.say "Don't do it..."
                    emma.say "Don't pull out!"
                    "I'm about to pull out of Emma when she says it."
                    "And her words catch me off guard, stopping me in my tracks."
                    show emma doggy ahegao cum -speed -bounce saliva with hpunch
                    $ emma.love += 5
                    $ emma.impregnate()
                    "But a moment later, I shoot my load."
                    with hpunch
                    "She cries out as I do so, in a mixture of arousal and alarm."
                    show emma doggy -saliva smile limp with hpunch
                    "But she looks back over her shoulder at me a moment later."
                    "Her eyes full of delight and her mouth twisting into a smile."
                    emma.say "You...you did it!"
                    emma.say "You came in me!"
                elif _return == "vaginal_inside_mad":
                    emma.say "Wait..."
                    emma.say "You have to..."
                    emma.say "You have to pull out!"
                    show emma doggy ahegao cum -speed -bounce with hpunch
                    $ emma.love -= 5
                    $ emma.impregnate()
                    "Almost the same second that Emma opens her mouth to say it, I shoot my load."
                    with hpunch
                    "She cries out as I do so, in a mixture of arousal and alarm."
                    show emma doggy pleasure limp with hpunch
                    "But she looks back over her shoulder at me a moment later."
                    "Her eyes full of shock and her mouth hanging open."
                    emma.say "You...you did it!"
                    emma.say "You came in me!"
    $ emma.sexperience += 1
    return

label emma_fuck_date_handjob:
    $ emma.sub += 1
    show emma hj with fade
    "Emma sits beside me and wraps her fingers around my member. Some experience with this has improved her technique."
    "She looks back at my cock, which even with just that simple touch is fully awake and ready to go."
    call emma_dick_reactions from _emma_fuck_date_handjob_dick_reaction
    show emma hj at startle(0.05, -10)
    pause 0.3
    show emma hj at startle(0.05, -10)
    "She strokes up and down...using a motion that she's practiced, and with a gentle, erotic touch."
    show emma hj at startle(0.05, -10)
    pause 0.2
    show emma hj at startle(0.05, -10)
    "My hips move toward her nearly of their own accord. Precum starts to dribble out and flows down my cock, adding lubrication to the mix."
    show emma hj surprised cum with vpunch
    "After a few more moments, white, sticky semen spews forth from my cock."
    show emma hj hand_shoulder with vpunch
    emma.say "Oh! Oh my God!"
    show emma hj normal -cum with vpunch
    mike.say "Oh, oh Emma! That was fantastic!"
    $ emma.sub += 1
    return

label emma_fuck_date_loop:

    if game.week_day % 2 == 0:
        call emma_fuck_date_sixth (True) from _call_emma_fuck_date_sixth_1
    else:
        call emma_fuck_date_seventh (True) from _call_emma_fuck_date_seventh_1


    menu:
        "Propose handjob":
            call emma_fuck_date_handjob from _call_emma_fuck_date_handjob_1
        "Propose blowjob" if emma.sub >= 25:
            call emma_fuck_date_bj from _call_emma_fuck_date_bj_1
        "Offer cunnilingus" if hero.sexperience >= 10:
            call emma_fuck_date_cunni from _call_emma_fuck_date_cunni
        "Skip foreplay":
            pass


    menu:
        "Missionary":
            call emma_fuck_date_missionary (0) from _call_emma_fuck_date_missionary
        "Cowgirl" if hero.sexperience >= 15:
            call emma_fuck_date_cowgirl (15) from _call_emma_fuck_date_cowgirl
        "Reverse Cowgirl" if hero.sexperience >= 25:
            call emma_fuck_date_reverse_cowgirl (25) from _call_emma_fuck_date_reverse_cowgirl
        "Doggy" if hero.sexperience >= 35:
            call emma_fuck_date_doggy (35) from _call_emma_fuck_date_doggy

    if _return == "too_small":
        call emma_fuck_date_too_small from _emma_fuck_date_loop
    $ game.pass_time(1)
    call sleep ("emma") from _emma_fuck_date_loop_sleep
    return

label emma_fuck_date_too_small:
    menu:
        "Propose handjob":
            call emma_fuck_date_handjob from _call_emma_fuck_date_handjob_2
        "Propose blowjob" if emma.sub >= 25:
            call emma_fuck_date_bj from _call_emma_fuck_date_bj_2
        "Offer cunnilingus" if hero.sexperience >= 10:
            call emma_fuck_date_cunni from _call_emma_fuck_date_cunni_1
        "Missionary" if not emma_too_small(10):
            call emma_fuck_date_missionary (0) from _call_emma_fuck_date_missionary_1
        "Cowgirl" if not emma_too_small(15) and hero.sexperience >= 15:
            call emma_fuck_date_cowgirl (15) from _call_emma_fuck_date_cowgirl_1
        "Reverse Cowgirl" if not emma_too_small(15) and hero.sexperience >= 25:
            call emma_fuck_date_reverse_cowgirl (25) from _call_emma_fuck_date_reverse_cowgirl_1
    return

label emma_fuck_date_cunni:
    $ emma.flags.loose += 1
    show emma lick with fade
    "I get down on my knees and put my face between her thighs. They close around me, pressing lightly on my cheeks."
    "I use my tongue on her; she is incredibly wet, and moans almost every time I brush across her clit."
    "Bringing one hand up, first I stroke between her labia, and then I press one finger in."
    if emma_too_small(10):
        "Except she's so tight, it won't go past the first knuckle. Not even my finger."
        "That means she's right -- if I can't get my finger in there while she's this wet, I'd never have gotten my dick inside her."
        "I try not to think about that just now; I've got a job to do, and I'm here to do it."
    else:
        "I move that finger up, then down, and that breath releases with a high pitched, squeal, like a balloon that's just let the air out."
        emma.say "Oh, [hero.name]!"
        "She puts her hand on the back of my head and pulls me toward her. My face dives in and I don't think, I just act."
        "I use my tongue, I use my fingers. She responds to everything, breathing faster with every touch, moaning aloud."
    "It doesn't take long..."
    show emma lick pleasure
    $ emma.love += 1
    emma.say "Oh! Oh god. Oh... Oh [hero.name]! I--I'm coming!"
    "My face is absolutely flooded with her juices when it happens."
    hide emma lick
    return

label emma_hottub_sex_male:
    $ game.active_date.clothes = "swimsuit"
    $ CONDOM = False
    show bg pool
    "I can't help looking down at my wrist out of sheer habit, only to realise that I don't have my watch on."
    "But then I'm sitting in the hot-tub out the back of my house, so why would I be wearing it?"
    "I let out a weary sigh, aware that I'm getting distracted by how long I've been waiting now."
    "Not for the first time, I crane my head around to see into the house."
    mike.say "Emma?"
    mike.say "Are you okay?"
    mike.say "You don't need any help?"
    "My questions are met with silence at first, wonder about calling out a second time."
    "But then I realise that it would actually be the third or maybe fourth time I've done so."
    "And so I make to get out of the tub and head inside to see what's holding Emma up."
    emma.say "Ah...no, [hero.name]."
    emma.say "I'm okay..."
    emma.say "I'll be there in a second, okay?"
    "I can't help frowning at the sound of Emma's voice when I hear it."
    "She sounds so nervous, almost like she's afraid of something."
    "I know she's a pretty shy kind of girl."
    "But it's not like I had to twist her arm to agree to a dip in the hot-tub with me."
    "Now I'm starting to get worried she agreed to it because she felt pressured somehow."
    "And that's really not the way I like to get a girl into the water with me!"
    show emma swimsuit with dissolve
    "That's why I try to give Emma a reassuring smile as soon as she emerges from the house."
    "Now that I see her, wrapped up tightly in a towel, I can see that she does look nervous."
    emma.say "Sorry, [hero.name]."
    emma.say "It took me a while to get changed!"
    mike.say "No worries, Emma."
    mike.say "I'm not mad at you."
    mike.say "I was just worried, that's all."
    emma.say "Oh, I was just being silly."
    emma.say "Worrying about you seeing me in my swimsuit."
    emma.say "Pretty dumb of me, huh?"
    mike.say "I understand if you're shy, Emma."
    mike.say "Look, you don't have to come in here if you don't want to."
    mike.say "I can get out - we can just sit and chat, if that's what you want?"
    "Emma shakes her head at this, starting to slip off her towel."
    "She walks the last few feet to the edge of the tub as she does so."
    emma.say "No, no..."
    emma.say "It's fine, [hero.name]..."
    "As she reveals her body for the first time, Emma's word trail off."
    "And that's because she notices the way that I'm staring at her."
    mike.say "Emma..."
    mike.say "You look amazing!"
    show hottub emma with fade
    "Emma blushes and looks away as she lowers herself into the water."
    "She even tries to cover her chest with her arms as she does so."
    "But that can't hide the fact that she's hot as hell!"
    emma.say "Oh, [hero.name]!"
    emma.say "You don't have to be nice just because of what I said!"
    mike.say "No, Emma, I wouldn't do that!"
    mike.say "I mean, I wouldn't just say you looked good without meaning it!"
    "Getting flustered, I look down at my trunks."
    "Noticing for the first time how hard Emma's got me right now."
    "She follows my gaze, and I hear her gasp in surprise."
    call emma_dick_reactions from _emma_hottub_sex_male_dick_reactions
    if emma_too_small(5):
        mike.say "Well..."
        mike.say "You don't look fine, Emma."
        mike.say "In fact, you look scared stiff!"
        "Emma's smile is pained."
        "But it also looks genuine."
        emma.say "I...I guess I'm a little nervous."
        emma.say "This is kind of a big deal for me!"
        emma.say "And...and what if it IS too big for me!"
        emma.say "I suppose that sounds silly to you?"
        "I shake my head, eager to allay Emma's fears."
        mike.say "No, Emma, it doesn't."
        mike.say "I'm a little nervous too!"
        "Emma's eyes go wide at this and she shakes her head."
        emma.say "Really?!?"
        emma.say "I thought you did this kind of thing all the time?"
        mike.say "This isn't my first time, Emma."
        mike.say "But I'm not exactly a Casanova either!"
        "Emma chuckles at this, her cheeks flushing a little."
        "But all that does is make her look that much sexier!"
        emma.say "You're such a liar, [hero.name]!"
        emma.say "But I trust you all the same."
    else:
        emma.say "Oh, wow!"
        emma.say "Did I..."
        emma.say "Is that for me?!?"
        mike.say "Erm...yeah, Emma."
        mike.say "You kind of have that effect on me!"
    "Emma reaches out then, almost touching it through my trunks."
    "But then she pulls her hand back at the last moment and looks me in the eye."
    emma.say "Can I...touch it?"
    mike.say "Sure Emma, if you want."
    "She gives me a nervous smile and reaches out again."
    "This time she actually strokes it with the tips of her fingers."
    "And even though she only brushes it, I feel a tingle pass through me."
    "Emma seems to notice this, looking me in the eye again."
    emma.say "Did that feel good?"
    mike.say "Yeah, Emma - it felt really good!"
    "Emma's smile grows wider and her cheeks begin to flush with colour."
    emma.say "W...would you like to..."
    emma.say "To put it inside of me?"
    emma.say "To see how it'd feel?"
    show hottub sex male emma outside with fade
    "By way of answer, I pull down my trunks and place Emma's hand on my cock."
    "She finches for a moment, but then takes a firmer hold."
    "I pull her closer, holding her gently as I do so."
    "And then I kiss her, full on the lips, feeling her resistance melt away."
    "The effect seems to take hold of Emma in a dramatic fashion."
    "She clings onto me with one hand and holds my cock with the other."
    "And when the time comes to guide it between her legs, she doesn't hesitate."
    "Emma perches on the edge of the tub as it pushes aside the lips of her pussy."
    show hottub sex male inside
    if emma_too_small(5):
        emma.say "Ow...ow...ow..."
        emma.say "Please, [hero.name]..."
        emma.say "You're hurting me!"
        "I can't be more than an inch into Emma's pussy by now."
        "But I can see from the look on her face that she's serious."
        "And as much as I want this, it's not worth hurting her to get it."
        hide hottub
        show emma swimsuit
        with fade
        "Which is why I pull out of her as quickly as I can."
        mike.say "I...I'm sorry, Emma."
        mike.say "Are you okay?"
        "Emma still looks more than a little pained."
        "And yet she forces a smile onto her face all the same."
        emma.say "No, I'm sorry, [hero.name]."
        emma.say "You're just so...large!"
        emma.say "I don't think this is going to work..."
        "I'm disappointed to say the least."
        "But I force a smile onto my face too."
        mike.say "Don't worry about it, Emma."
        mike.say "We'll figure something out."
        $ emma.love -= 10
        $ emma.sub -= 10
        return
    "Then she slides down onto it, a little at a time."
    "She gasps more with each inch that slips into her."
    if renpy.has_label("emma_achievement_5") and not game.flags.cheat:
        call emma_achievement_5 from _call_emma_achievement_5_4
    "Once I'm all the way in, I start to move as gently as I can."
    "Emma seems to appreciate this, sighing and cooing as I move back and forth."
    "Almost immediately I feel the urge to go faster, the need to push harder."
    "But I reign it in, not wanting to do anything that might upset Emma."
    "And so I keep on going with all of my efforts focused on that goal."
    "At first it feels a little frustrating, like I'm giving without getting."
    "But soon enough I begin to sense just how completely I have her in my power."
    "I realise that it's only through my exertions that Emma's enjoying this at all!"
    "And I'm damn sure she is enjoying it too."
    "Emma's clinging onto me for dear life by now."
    "I can feel her entire body quivering from the sensations she's feeling."
    "For her to go from feeling self-conscious to this!"
    "The way that she's taking all that I have to give..."
    "Well, it's only now that I can actually feel that she is giving back in return."
    "Because the feeling building up inside of me is telling me one thing."
    "It's telling me that I'm about to cum!"
    call cum_reaction (emma, 'vaginal', 1) from _call_cum_reaction_190
    if _return == "vaginal_outside":
        "I make a special effort to be ready as I feel the moment getting closer."
        "And just before it happens, I manage to gently pull out of Emma before it's too late."
        "Normally I'd be less worried about it, but she's too sensitive to leave it to chance."
        show hottub sex male outside
        "Emma's eyes open wide at the sensation of my cock pulling out of her pussy."
        show hottub sex male cumshot with vpunch
        $ emma.sub += 1
        "But they become wider still when she sees me shoot my load over her a moment later!"
        with vpunch
        "She jumps in surprise and shock as the cum lands on her breasts and belly."
    else:
        "Part of me feels like I should be trying to pull out of Emma before it's too late."
        "But another tells me that all I'd be doing is ruining the work I've already done."
        "And in the end, the latter wins out, as I keep up the same pace to the very end."
        show hottub sex male cumshot with vpunch
        $ emma.love += 1
        "Emma moans and bites her lip as I cum inside of her, but she doesn't seem upset."
        show hottub sex male ahegao with vpunch
        "Quite the opposite as she wears a broad smile the whole time."
    hide hottub sex male
    show hottub emma
    with fade
    "Afterwards, Emma looks exhausted and more than a little shaky."
    "But she smiles warmly at me and allows me to guide her down into the water at my side."
    "She seems more relaxed and at ease than I can remember, more comfortable in her skin."
    "I just hope that I've done the right thing and that she'll be more confident the next time!"
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ emma.sexperience += 1
    $ game.active_date.clothes = None
    return

label emma_fuck_date_nudistbeach:
label emma_fuck_date_beach:
label emma_fuck_beach:
    $ game.play_music("music/roa_music/tiny_love.ogg")
    scene bg beach
    show emma
    with fade
    "Part of me's amazed that Emma agreed to a date at the beach in the first place."
    "Sure, she's a lot of fun - but Emma's also pretty shy too."
    "I was worried that the idea of being around so many people might put her off."
    "That and the fact that we'd be in our swimming costumes the whole time too!"
    "But here we are, and the only thing that I can think about now is Emma herself."
    "Specifically the sight of her in the costume that she's chosen to wear today."
    "It's a one-piece, rather than something more adventurous like a bikini."
    "But she wears it so well, showing off the curves of her figure to perfection."
    "I can't stop stealing glances at her the whole time we're looking for a spot to settle."
    "And it doesn't take long for Emma to notice and her cheeks to flush red."
    show emma angry
    emma.say "Hey!"
    emma.say "Will you cut it out already?"
    "I shake my head, trying to play the innocent."
    mike.say "What do you mean, Emma?"
    show emma annoyed
    emma.say "You know what I mean, [hero.name]."
    emma.say "Stop staring at me like that!"
    "I shrug and let out a sigh."
    mike.say "It's the beach, Emma."
    mike.say "Everyone's looking at everyone!"
    emma.say "I...I know that, [hero.name]."
    show emma normal
    emma.say "But when you do it's...it's different!"
    "Well now, there's an intriguing admission!"
    "I stop and look around."
    "There's nobody else in sight and no chance of us being overheard."
    "So what better time and place to try and dig a little deeper?"
    mike.say "How is it different, Emma?"
    show emma annoyed
    emma.say "Well...when you look at me..."
    emma.say "I...I kind of don't mind it!"
    show emma happy
    emma.say "I mean, I like you looking at me!"
    mike.say "But if you like it, why tell me to stop?"
    show emma normal
    "Emma's cheeks are practically blazing red by now."
    "And she checks to see that we're alone before speaking too."
    emma.say "Because it makes me feel...frisky!"
    emma.say "That's why!"
    "I've never heard it called that before."
    "And so it takes me a moment to understand what Emma's saying."
    mike.say "You...you mean it's a turn-on?"
    show emma blush
    emma.say "Yes - of course it is!"
    mike.say "You mean you're turned-on right now?!?"
    emma.say "Oh god, yes!"
    mike.say "Then let's just do it - here and now!"
    show emma annoyed
    "Emma looks around again, as if she needs to be sure we're alone."
    "She bites her lips, clearly struggling with the idea and her own shyness."
    show emma normal
    emma.say "I...I suppose we could..."
    "That's a good enough answer for me."
    "And so I get right to work, spreading a towel on the sand."
    "Emma sits down and watches me intently, a hand held to her mouth."
    "But when I finish up and come to join her, she doesn't recoil for a moment."
    "Instead she shuffles close to me and points towards the sea."
    show emma happy
    emma.say "Look at the view, [hero.name]."
    emma.say "Isn't it amazing?"
    mike.say "It sure is, Emma."
    mike.say "Why not look out there and leave the rest to me?"
    show emma normal
    emma.say "Oh...okay."
    emma.say "Just...be gentle with me, alright?"
    mike.say "Don't worry, Emma."
    mike.say "You're in safe hands!"
    "I nod and take hold of Emma's hand, guiding her into position."
    "She straddles my thighs, gazing back over her shoulder as she does so."
    show emma reverse beach with fade
    "And then, with a quick nod, she turns to look out over the crashing waves."
    menu:
        "Fuck her ass" if hero.sexperience >= 20 and emma.sub >= 50:
            "I know that Emma's pretty nervous about doing this in a public place."
            "And I should be doing everything I can to soothe those nerves too."
            "But I can't shake the notion that I should really push her a bit."
            "You know what I mean, just challenge her boundaries a little."
            "Which is why I make a decision as I reach between her thighs."
            "I already have my own shorts down, and I pull her swimsuit aside too."
            "But then I aim the head of my cock between her buttocks."
            "And I pull Emma's ass down onto me!"
            emma.say "Oooh..."
            emma.say "That feels funny..."
            emma.say "What are you doing to me?"
            "I could stop and explain myself to Emma."
            "But that would be almost as good as giving up right now."
            show emma reverse anal pleasure
            "And so I press on regardless, pushing my cock into her."
            "And almost instantly I begin to hear a change in Emma's tone."
            "Before she was moaning and yelping in surprise."
            "But now she starts to sigh and let out gasps of pleasure."
            "Her body is doing the same thing too."
            "I can feel the resistance melt away as I go deeper still."
            show emma reverse down ahegao
            "And Emma sinks down onto my cock in a smooth motion."
            emma.say "Oh my..."
            emma.say "Your cock..."
            emma.say "It's in my ass!"
            "Emma looks back over her shoulder at me as she says this."
            "And I can see that she's more flushed and flustered than ever."
            show emma reverse pleasure
            emma.say "I...I never thought it'd fit in there."
            emma.say "But it feels...really nice!"
            "I nod, happy to see that Emma's enjoying herself."
            "But in truth I'm also relieved that my gamble paid off."
            show emma reverse up
            pause 0.35
            show emma reverse down
            "I begin to move slowly inside of Emma."
            "All the time I'm taking care to be gentle and attentive."
            show emma reverse up
            pause 0.35
            show emma reverse down
            "She seems to appreciate the effort I'm going to as well."
            "Emma nods her head and closes her eyes, enjoying the sensation."
            show emma reverse up
            pause 0.35
            show emma reverse down
            "I have to fight the urge to speed up my pace."
            "Being inside of her like this feels amazing."
            "But I need to make sure she's okay before I indulge myself."
            "This means that the act becomes ever more intense for me."
            show emma reverse up
            pause 0.35
            show emma reverse down
            "I want to let go and ride Emma with wild abandon."
            "And yet I keep on struggling to control that urge."
            show emma reverse up
            pause 0.35
            show emma reverse down
            "Every movement I make is drawn out, the sensations exaggerated."
            "Soon enough I'm panting from frustration, rather than exhaustion!"
            "Emma seems to sense this, and she speaks up a moment later."
            show emma reverse up
            pause 0.35
            show emma reverse down
            emma.say "You can go a little faster, if that's what you'd like?"
            emma.say "I'm not made of glass, [hero.name]."
            emma.say "And I trust you not to break me!"
            "Sure, Emma just gave me permission to kick it up a gear."
            "But that doesn't mean I'm going to go crazy the very next second."
            show emma reverse up
            pause 0.25
            show emma reverse fast
            pause 0.15
            show emma reverse down
            "Instead I respond by gradually picking up speed."
            show emma reverse up
            pause 0.2
            show emma reverse fast
            pause 0.1
            show emma reverse down at startle(0.05,-10)
            "Soon enough I can feel my momentum building."
            "And I'm sure that Emma can too!"
            show emma reverse up
            pause 0.2
            show emma reverse fast
            pause 0.1
            show emma reverse down at startle(0.05,-10)
            "She responds by soaking up all that I have to give."
            "Before she was riding me gently, pacing herself."
            show emma reverse up
            pause 0.2
            show emma reverse fast
            pause 0.1
            show emma reverse down at startle(0.05,-10)
            pause 0.2
            show emma reverse up
            pause 0.2
            show emma reverse fast
            pause 0.1
            show emma reverse down at startle(0.05,-10)
            "But now she becomes like a rider in a rodeo, holding on for dear life."
            show emma reverse up ahegao
            pause 0.2
            show emma reverse fast
            pause 0.1
            show emma reverse down at startle(0.05,-10)
            pause 0.2
            show emma reverse up
            pause 0.2
            show emma reverse fast
            pause 0.1
            show emma reverse down at startle(0.05,-10)
            "Emma's eyes roll back into her head and her tongue flops out between her lips."
            "She speaks, but her words are slurred, like she's drunk or high."
            show emma reverse up
            pause 0.2
            show emma reverse fast
            pause 0.1
            show emma reverse down at startle(0.05,-10)
            pause 0.2
            show emma reverse up
            pause 0.2
            show emma reverse fast
            pause 0.1
            show emma reverse down at startle(0.05,-10)
            emma.say "I...I'm..."
            emma.say "I'm...gonna..."
            emma.say "I'm...gonna...cum!"
            "What a coincidence - so am I!"
            call cum_reaction (emma, 'anal', 5) from _call_cum_reaction_191
            if _return == 'anal_inside':
                show emma reverse up
                pause 0.2
                show emma reverse fast
                pause 0.1
                show emma reverse down at startle(0.05,-10)
                pause 0.2
                show emma reverse up
                pause 0.2
                show emma reverse fast
                pause 0.1
                show emma reverse down with vpunch
                pause 0.2
                show emma reverse up creampie
                "I hold onto Emma as best I can as I feel myself losing it."
                with vpunch
                "And she's already in the throes of her orgasm as I do so."
                with vpunch
                "The sensation of me cumming inside of her has an instant effect."
                $ emma.sub += 2
                with vpunch
                "It makes Emma quiver and shake atop me."
                "Her muscles squeezing my cock until I'm completely spent."
                "And then I feel her go limp in my grasp."
                show emma reverse pleasure dickcum -anal
                "She slides off my cock and onto the towel beside me."
            elif _return == 'anal_outside':
                "I could keep right on going without any danger."
                "But for some reason I get the urge to pull out."
                show emma reverse up
                pause 0.2
                show emma reverse fast
                pause 0.1
                show emma reverse down at startle(0.05,-10)
                pause 0.2
                show emma reverse up
                pause 0.2
                show emma reverse fast
                pause 0.1
                show emma reverse up -anal
                "My cock slides out of Emma with an audible pop."
                "And the sensation has an instant effect."
                $ emma.sub += 1
                "She shakes and quivers atop me, like she's cumming a second time."
                show emma reverse cumshot with vpunch
                "I cum a moment later, shooting my load over Emma's buttocks."
                with vpunch
                "And then I feel her go limp in my grasp."
                show emma reverse -cumshot dickcum bodycum with vpunch
                "She slides off my lap and onto the towel beside me."
            $ emma.flags.anal += 1
        "Fuck her pussy":
            "I want to make this as pleasant of an experience as possible for Emma."
            "And so I set my sights firmly on what's hidden between her legs."
            "I already have my own shorts down, and I pull her swimsuit aside too."
            call check_condom_usage (emma, 180) from _call_check_condom_usage_41
            if _return == False:
                return
            if CONDOM:
                show emma reverse condom
            "Emma nods as I pull her downwards, wriggling her ass into my lap."
            "She seems to be more ready for it than she was before, more prepared."
            "And I nod too as I feel my cock pressing against the lips of her pussy."
            "I hold my breath as it pushes slowly inside..."
            show emma reverse vaginal pleasure
            if emma_too_small(15):
                "I realise that I've made a mistake a few seconds later."
                "Emma's yelps of surprise turn into cries of pain."
                "And she begs me to stop what I'm doing."
                emma.say "Ah..."
                emma.say "Please, [hero.name], don't do it!"
                emma.say "It's too big - you're hurting me!"
                hide emma
                show emma swimsuit annoyed
                with fade
                "I pull my cock out of Emma as quickly as I can."
                "But it's too late, the damage is already done."
                "She rolls off of me and onto the towel, still panting and in pain."
                mike.say "Are you okay, Emma?"
                mike.say "I never meant to..."
                emma.say "I...I'll be fine, honestly!"
                emma.say "Just promise that you'll warn me in future, okay?"
                "I nod and we both stare out at the sea, trying to move on."
                "But I get the feeling I just turned things sour."
                "And I'm already dreading the rest of the date ahead of us."
                $ emma.love -= 10
                $ emma.sub -= 10
                return "too_small"
            else:
                emma.say "Mmm..."
                emma.say "Oh, [hero.name]..."
                emma.say "That feels amazing!"
                "I have to agree with Emma."
                "It feels pretty amazing as I slide into her a little at a time."
                "Her pussy is nice and tight, squeezing my cock like a hand."
                if renpy.has_label("emma_achievement_5") and not game.flags.cheat:
                    call emma_achievement_5 from _call_emma_achievement_5_5
                show emma reverse down
                "But it's yielding more with every inch I get inside of her."
                "Emma's tone melts into moans and gasps of pleasure."
                "And her body does the same thing to."
                "She surrenders to me more with each second that passes."
                "But I still force myself to hold back a little."
                show emma reverse up
                "I want to be gentle with her, to take things slowly."
                "After all, I know how shy and delicate Emma can be."
                show emma reverse down
                "The last thing I want is to go too hard and actually hurt her."
                "Emma seems to appreciate my efforts too."
                show emma reverse up
                pause 0.35
                show emma reverse down
                "She rides my cock smoothly, matching my own motions."
                "Emma steals a look back over her shoulder."
                "And I can see that she's looking more flushed and flustered than ever!"
                show emma reverse up
                pause 0.35
                show emma reverse down
                emma.say "Your cock...it's SO big!"
                emma.say "I...I never thought it'd fit in there."
                emma.say "But it feels...really nice!"
                "Emma's words make me want to go hard and fast."
                show emma reverse up
                pause 0.35
                show emma reverse down
                "But I'm still holding myself back for her sake."
                "This means that as I move inside her, I have to suppress the urge."
                "Every moment becomes more tense for me as I do this."
                show emma reverse up
                pause 0.35
                show emma reverse down
                "And I swear that I'm going to explode from the pressure!"
                "Emma seems to notice this, and comes to my rescue."
                show emma reverse up
                pause 0.35
                show emma reverse down
                emma.say "Would you like to go a little faster, [hero.name]?"
                emma.say "I'm not made of glass, you know."
                emma.say "And you're not going to break me!"
                "Emma giggles as I feel myself set free by her words."
                "But still I don't go crazy as soon as she lets me off the hook."
                show emma reverse up pleasure
                pause 0.25
                show emma reverse fast
                pause 0.15
                show emma reverse down
                "Instead I begin to pick up speed gradually, pacing myself."
                show emma reverse up
                pause 0.2
                show emma reverse fast
                pause 0.1
                show emma reverse down at startle(0.05,-10)
                "And pretty soon I see the effect that this is having on her too."
                "Before she was riding me gently, letting me do most of the work."
                "But soon enough, Emma's acting like she's riding in a wild rodeo."
                show emma reverse up
                pause 0.2
                show emma reverse fast
                pause 0.1
                show emma reverse down at startle(0.05,-10)
                "She grinds herself into my lap, pushing down with all her weight."
                "And her demure moans become almost desperate gasps of pleasure."
                show emma reverse up ahegao
                pause 0.2
                show emma reverse fast
                pause 0.1
                show emma reverse down at startle(0.05,-10)
                pause 0.2
                show emma reverse up
                pause 0.2
                show emma reverse fast
                pause 0.1
                show emma reverse down at startle(0.05,-10)
                "Emma's eyes roll back into her head and her tongue flops out between her lips."
                show emma reverse up
                pause 0.2
                show emma reverse fast
                pause 0.1
                show emma reverse down at startle(0.05,-10)
                pause 0.2
                show emma reverse up
                pause 0.2
                show emma reverse fast
                pause 0.1
                show emma reverse down at startle(0.05,-10)
                "She speaks, but her words are slurred, like she's drunk or high."
                emma.say "I...I'm..."
                emma.say "I'm...gonna..."
                emma.say "I'm...gonna...cum!"
                "What a coincidence - so am I!"
                call cum_reaction (emma, 'vaginal', 5, love_min=200) from _call_cum_reaction_192
                if _return == "vaginal_condom":
                    show emma reverse up pleasure
                    pause 0.2
                    show emma reverse fast
                    pause 0.1
                    show emma reverse down at startle(0.05,-10)
                    pause 0.2
                    show emma reverse up
                    pause 0.2
                    show emma reverse fast
                    pause 0.1
                    show emma reverse down with vpunch
                    "I hold onto Emma as best I can as I feel myself losing it."
                    with vpunch
                    "And she's already in the throes of her orgasm as I do so."
                    with vpunch
                    "But as we used a condom, we can enjoy the moment."
                    with vpunch
                    "The sensation of me cumming inside of her has an instant effect."
                    "It makes Emma quiver and shake atop me."
                    "Her muscles squeezing my cock until I'm completely spent."
                    "And then I feel her go limp in my grasp."
                    show emma reverse up cumshot -vaginal
                    "She slides off my cock and onto the towel beside me."
                elif _return == "vaginal_outside":
                    "I can't keep on going without it getting dangerous."
                    "And for that reason alone I make to pull out before it's too late."
                    show emma reverse up
                    pause 0.2
                    show emma reverse fast
                    pause 0.1
                    show emma reverse down at startle(0.05,-10)
                    pause 0.2
                    show emma reverse up
                    pause 0.2
                    show emma reverse fast
                    pause 0.1
                    show emma reverse up -vaginal
                    "My cock slides out of Emma with an audible pop."
                    "And the sensation has an instant effect."
                    $ emma.love += 1
                    "She shakes and quivers atop me, like she's cumming a second time."
                    show emma reverse cumshot with vpunch
                    if CONDOM:
                        "I cum a moment later."
                    else:
                        "I cum a moment later, shooting my load over Emma's buttocks."
                    "And then I feel her go limp in my grasp."
                    if not CONDOM:
                        show emma reverse -cumshot dickcum bodycum with vpunch
                    with vpunch
                    "She slides off my lap and onto the towel beside me."
                elif _return == "vaginal_inside_pill":
                    "I hold onto Emma as best I can as I feel myself losing it."
                    "And she's already in the throes of her orgasm as I do so."
                    emma.say "It's...okay..."
                    emma.say "Pill...remember?"
                    emma.say "I'm...on the...pill!"
                    "I silently thank Emma for that timely reminder."
                    show emma reverse up
                    pause 0.2
                    show emma reverse fast
                    pause 0.1
                    show emma reverse down at startle(0.05,-10)
                    pause 0.2
                    show emma reverse up
                    pause 0.2
                    show emma reverse fast
                    pause 0.1
                    show emma reverse down with vpunch
                    pause 0.2
                    show emma reverse up creampie
                    "The sensation of me cumming inside of her has an instant effect."
                    $ emma.love += 2
                    with vpunch
                    "It makes Emma quiver and shake atop me."
                    with vpunch
                    "Her muscles squeezing my cock until I'm completely spent."
                    "And then I feel her go limp in my grasp."
                    show emma reverse pleasure dickcum -vaginal
                    "She slides off my cock and onto the towel beside me."
                elif _return == "vaginal_inside_pregnant":
                    "I hold onto Emma as best I can as I feel myself losing it."
                    "And she's already in the throes of her orgasm as I do so."
                    emma.say "It's...okay..."
                    emma.say "I'm pregnant...remember?"
                    emma.say "I'm...already...pregnant!"
                    "I silently thank Emma for that timely reminder."
                    show emma reverse up
                    pause 0.2
                    show emma reverse fast
                    pause 0.1
                    show emma reverse down at startle(0.05,-10)
                    pause 0.2
                    show emma reverse up
                    pause 0.2
                    show emma reverse fast
                    pause 0.1
                    show emma reverse down with vpunch
                    pause 0.2
                    show emma reverse up creampie
                    "The sensation of me cumming inside of her has an instant effect."
                    $ emma.love += 3
                    with vpunch
                    "It makes Emma quiver and shake atop me."
                    with vpunch
                    "Her muscles squeezing my cock until I'm completely spent."
                    "And then I feel her go limp in my grasp."
                    show emma reverse pleasure dickcum -vaginal
                    "She slides off my cock and onto the towel beside me."
                elif _return == "vaginal_inside_happy":
                    "I know that I have to pull out now, before it's too late."
                    "But as I try to move, Emma pushes down on me with all her weight."
                    emma.say "No!"
                    emma.say "No, no, no!"
                    emma.say "You HAVE to cum in me!"
                    "Normally I could heave Emma off my lap with ease."
                    "But her words catch me totally off-guard."
                    "And those few seconds are all it takes for disaster to strike."
                    show emma reverse up
                    pause 0.2
                    show emma reverse fast
                    pause 0.1
                    show emma reverse down at startle(0.05,-10)
                    pause 0.2
                    show emma reverse up
                    pause 0.2
                    show emma reverse fast
                    pause 0.1
                    show emma reverse down with vpunch
                    pause 0.2
                    show emma reverse up creampie
                    $ emma.impregnate()
                    "The sensation of me cumming inside of her has an instant effect."
                    $ emma.love += 5
                    with vpunch
                    "It makes Emma quiver and shake atop me."
                    with vpunch
                    "Her muscles squeezing my cock until I'm completely spent."
                    "Then I feel her go limp in my grasp."
                    show emma reverse pleasure dickcum -vaginal
                    "She slides off my cock and onto the towel beside me."
                    "And I stare at her in horror, still baffled by what she just did."
                    "She slides off my cock and onto the towel beside me."
                elif _return == "vaginal_inside_mad":
                    emma.say "No!"
                    emma.say "No, no, no!"
                    emma.say "You HAVE to pull out of me!"
                    "Normally I could have responded to Emma's frantic warning."
                    "But her words catch me totally off-guard."
                    "And those few seconds are all it takes for disaster to strike."
                    show emma reverse up pleasure
                    pause 0.2
                    show emma reverse fast
                    pause 0.1
                    show emma reverse down at startle(0.05,-10)
                    pause 0.2
                    show emma reverse up
                    pause 0.2
                    show emma reverse fast
                    pause 0.1
                    show emma reverse down with vpunch
                    pause 0.2
                    show emma reverse up creampie
                    $ emma.impregnate()
                    "The sensation of me cumming inside of her has an instant effect."
                    with vpunch
                    "It makes Emma quiver and shake atop me."
                    with vpunch
                    "Her muscles squeezing my cock until I'm completely spent."
                    "Then I feel her go limp in my grasp."
                    show emma reverse dickcum -vaginal
                    "She slides off my cock and onto the towel beside me."
                    $ emma.love -= 5
                    "And we stare at each other in horror, stunned and silent after what just happened."
    scene bg beach with fade
    "Afterwards, Emma lays herself against me and nestles into my side."
    "All I can hear is the sound of the waves and her gentle breathing."
    "She doesn't say anything, and I don't feel like spoiling the silence."
    "So we simply lie there, listening to the lapping of the water."
    "Because what could be better after the fun we just had together?"
    $ emma.sexperience += 1
    hide emma
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
