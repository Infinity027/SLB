init python:
    Event(**{
    "name": "harmony_hottub_sex_male",
    "label": "harmony_hottub_sex_male",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("date_hot_tub_home")),
        PersonTarget(harmony,
            OnDate(),
            MinStat("love", 100),
            MinStat("sexperience", 1),
            MaxStat("purity", 59),
            ),
        ],
    "priority": 500,
    "do_once": False,
    "once_day": True,
    "duration": 1,
    })



label harmony_fuck_date_male(location="hero"):
    $ game.play_music("music/roa_music/city_nights.ogg")
    $ prel = False
    show bg bedroom1
    $ game.room = "bedroom1"


    call harmony_fuck_date_intro_male (location) from _call_harmony_fuck_date_intro_male


    call harmony_dick_reactions from _call_harmony_dick_reactions_2


    call harmony_fuck_date_foreplay_male from _call_harmony_fuck_date_foreplay_male


    $ skip_to_sleep = _return

    scene bg bedroom1
    show harmony naked blush
    with fade

    if not skip_to_sleep:

        call harmony_fuck_date_choices_male from _call_harmony_fuck_date_choices_male


    call handle_npc_leaving (harmony, _return) from _call_handle_npc_leaving_9
    if _return:
        return


    hide harmony
    call harmony_sleep_date_fuck (location) from _call_harmony_sleep_date_fuck
    return


label harmony_fuck_date_intro_male(location="hero"):
    if not harmony.sexperience:
        show harmony sad
        "It's only when we're finally standing in the doorway of my room that I feel Harmony stiffen and stop."
        "I've been holding her hand the whole time, leading her through the house every step of the way."
        "But until now, she's managed to hide just how nervous she is under a cover of nods and smiles."
        "I turn around, the surprise at this written all over my face and quickly becoming genuine concern."
        mike.say "Harmony..."
        mike.say "What is it?"
        mike.say "Are you okay?"
        "Still holding my hand with her left, I see Harmony cover her mouth with her right."
        "Her eyes are wide, and she seems to be staring at the room beyond the doorway in actual fear."
        "And then it hits me - what are the chances that this is Harmony's first time with a guy?"
        "She hardly comes over as the type to have a long history on that side of things."
        "And it's a subject that's never come up before now - virgin territory, if you'll pardon the pun!"
        "I thought we were making progress in getting over Harmony's hang-ups as we were becoming more intimate."
        "But perhaps this is just too big of a leap for that to make any kind of difference."
        harmony.say "I...I'm just a little scared, [hero.name]."
        harmony.say "I've never done...this..."
        harmony.say "I've never been with a man before..."
        "Good god - how can a girl this beautiful be such a genuine innocent?"
        "Part of me thinks I should leave her that way, that I shouldn't soil her with my touch."
        "But another part of me thinks that I'll go insane if I don't have her, and soon!"
        "And I bet you can guess which part of me is going to win the debate too..."
        mike.say "I understand, Harmony."
        mike.say "And it's okay, trust me."
        mike.say "I'm not going to make you do anything you don't want to."
        show harmony normal
        "Hey, hey - wait a minute before you accuse me of being lame here!"
        "Haven't you ever heard of the softly, softly approach?"
        "My tactic seems to work, as Harmony nods slowly and then allows me to lead her into the room."
        "I give her what I hope is a warm, reassuring smile as I lead her towards the bed."
    else:
        "I can almost sense the vibes coming from Harmony as we make it back to my place."
        "She's been flirtatious and physical with me all night, touching me whenever she has the chance."
        "And on the ride home, her hands start to roam with a definite desire in mind."
        "Which means that once we walk through my bedroom door, we both know just what we want."
        "And sure enough, Harmony all but pounces on me the moment the door's closed behind us!"
    if game.days_played % 2 == 0:
        harmony.say "Mmm..."
        harmony.say "I've been waiting all night to get you alone, [hero.name]."
        if harmony.purity <= VLP:
            harmony.say "I want to feel your cock inside of me!"
        elif harmony.purity <= LP:
            harmony.say "I want to feel your hands all over me!"
        else:
            harmony.say "Come on - let's have some real fun!"
        mike.say "Sure thing, Harmony."
        mike.say "It's like you read my mind!"
        "Harmony and I both start to strip off at the same time."
        "And maybe we could have made an effort to put on a show for each other."
        "But the reality is that we're too busy checking out what's on show for that!"
        show harmony underwear with dissolve
        "Every time Harmony peels off another item of clothing, I get more excited."
        "And I hear a giggle of delight from her whenever I do the same thing too."
        show harmony naked with dissolve
        "Once we're naked, we make straight for the bed."
        "Harmony was closer to begin with, so she makes it there first."
        "I watch as she climbs onto the mattress, getting onto all fours."
    else:
        if harmony.purity >= HP:
            "Harmony returns my smile, letting me know that she's placing her trust in me to keep my word."
            "And so it's with the upmost care that I gently smooth her hair behind her ear and kiss her lips."
            hide harmony
            show harmony kiss
            with fade
            $ harmony.flags.kiss += 1
            "I figure that if we take slow, easy steps of increasing intimacy, we can ease into this thing."
            "I'm relieved to feel Harmony respond in kind to the kiss, even the tip of her tongue against mine."
            "We've already kissed many times before, and she always seems to warm to the idea quite quickly."
            "As the kiss becomes steadily more intense, I can feel the same thing happening to me too."
            "The enforced need to keep it slow makes me all the more needy for all I can get from Harmony."
            "And so a gentle kiss is intensified almost tenfold, almost making me scared to imagine what sex will feel like!"
            "When the kiss is finally over, we begin to undress each other."
            hide harmony kiss
            show harmony underwear
            with fade
            "There's no tearing off of the clothes, rather a slow and careful stripping off."
            "But with every new inch of Harmony that's revealed, I can feel my sense of anticipation growing."
            "I see her looking at me in what I hope is a similar manner too, blushing as I catch her in the act."
            show harmony naked with dissolve
            "Now that we're both naked, Harmony makes an effort to cover herself with her hands."
            call harmony_dick_reactions from _call_harmony_dick_reactions
            "I take hold of them gently, keeping her from concealing her body from me."
            mike.say "You don't have to hide from me, Harmony."
            mike.say "This is where we share ourselves with each other."
            mike.say "There's nothing to be ashamed of..."
            "Harmony nods, and then gingerly allows me to see her naked body."
            harmony.say "I'm scared, [hero.name]."
            harmony.say "Scared you'll think I'm too fat!"
            mike.say "Harmony, what are you talking about?"
            mike.say "Every inch of you is beautiful."
            "She blushes at this, unable to meet my eye."
            harmony.say "You're...you're sweet, [hero.name]."
            harmony.say "But you don't have to lie to me..."
            mike.say "Harmony, just look at what you're doing to me right now!"
            "I gesture down to where my cock is already standing to attention, hard as a rock."
            mike.say "That part of me can't lie."
            "It's a gamble, I know, what with her being so innocent and all."
            "But we're supposed to be letting our guard down and getting more intimate than ever before."
            "Harmony's eyes go wide at the sight of my stiff member, and she covers her mouth with one hand."
            harmony.say "Oh, my goodness!"
            harmony.say "You mean...I did...that?!?"
        elif harmony.purity <= VLP:
            "Do you ever get the feeling that you might have been had?"
            hide harmony
            show harmony kiss
            with fade
            $ harmony.flags.kiss += 1
            "Almost the very same moment that Harmony and I sit down on the bed, she leans forward and kisses me."
            "Not some chaste peck on the lips or honestly passionate meeting of mouths here."
            "She practically forces her tongue between my lips."
            "And it feels like the thing is an eel with a mind of it's own!"
            "Eventually, I manage to pull away for long enough to speak a couple of words."
            hide harmony kiss
            show harmony
            with fade
            mike.say "Whoa...okay, Harmony."
            mike.say "Time-out...time-out!"
            "Harmony obliges me by backing off just a little."
            show harmony sad
            "But I can see from the look on her face that she resents doing so."
            harmony.say "What's the problem, [hero.name]?"
            harmony.say "I thought guys liked a girl that's up for it?"
            mike.say "Yeah, well..."
            if not harmony.sexperience:
                mike.say "Maybe that's more true when you don't think the girl's a virgin!"
            else:
                mike.say "Maybe it helps when you don't think she wants you to go easy on her!"
            show harmony happy
            "Harmony's lips curl into a smirk at this, and she shakes her head at me."
            harmony.say "Jesus, [hero.name]."
            harmony.say "Don't let that stop you having your fun."
            harmony.say "Because I won't let it stop me having mine!"
            "What more invitation do I really need after that?"
            "I make an effort to show that I'm willing by starting to strip off my clothes."
            "At which Harmony lets out a filthy laugh, and follows my lead."
            show harmony -happy naked
        elif harmony.purity <= LP:
            "To begin with, I can still feel the nervous energy that Harmony's giving off."
            "But as we sit down and begin to move closer together, her demeanour changes."
            "It's almost as though the more intimate we get, the less shy and demure she becomes as a result."
            "Don't get me wrong here - I'm not suggesting that she was making a show of acting the innocent before."
            "But she gains in confidence and becomes so forward in that short time that I'm forced to wonder."
            hide harmony
            show harmony kiss
            with fade
            $ harmony.flags.kiss += 1
            "Harmony kisses me full on the lips, sighing with satisfaction as she does so."
            "And at the same time, I can feel her beginning to pull off my clothes."
            "Managing to partially free my lips from her all-consuming kiss, I stammer a couple of words."
            mike.say "Whoa...Harmony!"
            mike.say "Settle down already!"
            "She breaks the kiss in response to this, pausing in the act of pulling off her dress."
            hide harmony kiss
            show harmony underwear
            with fade
            harmony.say "What's the matter, [hero.name]?"
            harmony.say "Did I do something wrong?"
            mike.say "Ah, no...no."
            mike.say "You just took me a little by surprise, that's all!"
            if not harmony.sexperience:
                show harmony blush
                "At this, Harmony arches an eyebrow."
                harmony.say "Isn't that a guy's ultimate fantasy?"
                harmony.say "To fuck a dirty little virgin?"
                harmony.say "To give her what she REALLY wants?"
            else:
                "At this, Harmony pouts a little."
                harmony.say "I guess I just remembered that we've done this before."
                harmony.say "So I really don't need to be bashful - do I?"
            mike.say "Well, when you put it like that..."
            show harmony normal naked
        else:
            "Harmony smiles awkwardly as we sit together on the bed, and I return the gesture."
            "But then it occurs to me that I'm technically the one hosting her tonight."
            "And so it's up to me to do all that I can to reassure her that things are going to be okay."
            mike.say "I think we're both a little over-dressed for what we've got in mind."
            mike.say "So what if I go first and take something off, then you?"
            "Harmony blushes a little and smiles at the notion of making a game out of stripping off."
            "But she nods all the same, and I can see that I've managed to break the ice a little."
            "True to my word, I strip off my top and then gesture that it's her turn."
            "Harmony pauses, but then follows suit."
            show harmony happy with dissolve
            "Pretty soon we're stripped down to almost nothing, both fighting off the giggles."
            show harmony sad
            "But then, all of a sudden, Harmony stops laughing."
            "She looks down at herself, now dressed only in her underwear."
            "And then she covers up as best she can with only her hands."
            mike.say "Harmony, what's up?"
            harmony.say "I...I don't want you to look at me."
            mike.say "What the..."
            mike.say "Why would you say that?"
            harmony.say "Oh come on, [hero.name] - because I'm so fat!"
            "For a moment, I simply don't know what to say."
            "But then I shake my head in genuine disbelief."
            mike.say "Harmony, that's crazy talk!"
            mike.say "The only time you look more beautiful than with clothes is when you're naked."
            "She begins to shake her head, trying to dismiss my words."
            "But then I point to my groin, where my cock is already straining the elastic of my shorts."
            mike.say "If that's not the truth - then what's going on down here?!?"
            harmony.say "Oh...oh my!"
            harmony.say "Did I...did I do...that?"
            "I nod, still trying to convince her that she's mistaken when it comes to her appearance."
            mike.say "Yeah, you kinda did!"
            mike.say "And I'd kinda like to do something to you too..."
            show harmony naked with dissolve
    return

label harmony_fuck_date_foreplay_male:
    if harmony.sub >= 50:
        if not harmony.flags.titjob:
            call harmony_fuck_titjob from _call_harmony_fuck_titjob
            $ harmony.flags.titjob = True
        elif not harmony.flags.blowjob and harmony.purity <= 50:
            call harmony_fuck_blowjob from _call_harmony_fuck_blowjob
            $ harmony.flags.blowjob = True
        elif not harmony.flags.cunnilingus and harmony.purity <= 65:
            call harmony_fuck_cunnilingus from _call_harmony_fuck_cunnilingus
            $ harmony.flags.cunnilingus = True
        elif (harmony.flags.titjob or harmony.flags.titjob or harmony.flags.cunnilingus):
            menu:
                "Ask for a titjob" if harmony.flags.titjob:
                    $ prel = True
                    call harmony_fuck_titjob from _call_harmony_fuck_titjob_1
                    $ harmony.sub += 2
                "Give her a cunnilingus" if harmony.flags.cunnilingus:
                    $ prel = True
                    call harmony_fuck_cunnilingus from _call_harmony_fuck_cunnilingus_1
                    $ harmony.sub += 2
                "Ask for a blowjob" if harmony.flags.blowjob:
                    $ prel = True
                    call harmony_fuck_blowjob from _call_harmony_fuck_blowjob_1
                    $ harmony.sub += 2
                "Don't ask for anything":
                    pass
        if prel and hero.sexperience < 20:
            return "skip_to_sleep"
    call stop_all_sfx from _call_stop_all_sfx_17

    return _return

label harmony_fuck_date_choices_male:
    menu:
        "Missionary":
            call harmony_fuck_missionary (0) from _call_harmony_fuck_missionary
        "Doggy" if hero.sexperience >= 10:
            call harmony_fuck_doggy (10) from _call_harmony_fuck_doggy
    call stop_all_sfx from _call_stop_all_sfx_18

    return _return

label harmony_fuck_blowjob:
    $ game.play_music("music/roa_music/city_nights.ogg")
    if not harmony.flags.blowjob:
        mike.say "Harmony - you remember the last time we fooled around together?"
        mike.say "Remember how you used your breasts to get me off?"
        show harmony blush
        "The instant that I mention it, Harmony's cheeks flush bright red and she can't meet my eye."
        "If it were another girl, I'd be sure that she was too embarrassed for me to go on."
        "But I know that she's just so humble and sheltered that she can't help reacting like this."
        "And to be honest, it's one of the things about her that really turns me on!"
        if harmony.purity >= AP:
            harmony.say "Ah, yeah..."
            harmony.say "How could I forget something like that!"
        elif harmony.purity >= LP:
            harmony.say "Of course I do, [hero.name]."
            harmony.say "That was so naughty!"
        elif harmony.purity <= VLP:
            harmony.say "Ooh, yeah..."
            harmony.say "I can still remember what your cock felt like between my tits!"
        mike.say "Well..."
        mike.say "I think we're ready to take it to the next level."
        show harmony normal
        "Only now does Harmony look me in the eye once more."
        "And I can see that there's trepidation in her own eyes, but more than a little intrigue as well."
        show fx question
        harmony.say "The next level?"
        harmony.say "What does that mean, [hero.name]?"
        "I take a deep breath and just say it, figuring that the worst she can say is no."
        "Although I'm seriously hoping that she doesn't!"
        hide fx
        mike.say "How about you try giving me a blowjob, Harmony?"
        mike.say "Don't worry, I'll tell you what to do, like before!"
        mike.say "But I'm sure you'd be great at it, if you'd only try."
        if harmony.purity >= AP:
            harmony.say "A blowjob?!?"
            harmony.say "Oh, my...I should say no."
            harmony.say "But I felt the same way about the boob-job too - and that was okay in the end."
            show harmony happy
            harmony.say "So I guess I should give this a chance like I did with that."
        elif harmony.purity >= LP:
            harmony.say "Mmm..."
            show harmony happy
            harmony.say "I like the sound of that, [hero.name]!"
            harmony.say "Let's do it!"
        elif harmony.purity <= VLP:
            show harmony happy
            harmony.say "Oh yes..."
            harmony.say "Oh hell yes!"
            show harmony blush
            harmony.say "I've always wondered what cock tasted like!"
        "I try not to let my relief show, not wanting to look too desperate in front of Harmony."
        "But all the same, I can feel my heart leap in my chest almost as soon as she says yes."
        mike.say "That's great, Harmony."
        mike.say "Don't worry, we'll take it slow, okay?"
        show harmony normal
    else:
        mike.say "Ah, Harmony?"
        harmony.say "Yeah, [hero.name]?"
        mike.say "You remember what we did the last time?"
        mike.say "When you...used your mouth?"
        "Harmony flushes a little at the memory."
        show harmony happy
        "But she smiles all the same."
        "So maybe that means she's up for it?"
        harmony.say "You mean a blowjob?"
        show harmony normal
        harmony.say "Y...you want me to do it again?"
        mike.say "Yeah, Harmony - it was really great."
        mike.say "Would you do that for me?"
        show harmony blush
        harmony.say "Okay, if that's what you want - let's do it!"
    show harmony naked with dissolve
    if harmony.purity >= AP:
        harmony.say "Whoa..."
        harmony.say "I guess you really are looking forward to this, huh?"
        "Both now naked, I lead Harmony to the bed and guide onto the mattress."
        "She sits facing me on all fours, looking up expectantly."
        "Her face is so cute and innocent."
        "Her breasts are so huge!"
        harmony.say "Sh...should I put it in my mouth now?"
    elif harmony.purity >= LP:
        harmony.say "Whoo..."
        harmony.say "It looks even bigger than before!"
        "Both now naked, I lead Harmony to the bed and guide onto the mattress."
        "She sits facing me on all fours, looking up expectantly."
        "Her face is so cute and innocent."
        "Her breasts are so huge!"
        harmony.say "You want to put it in my mouth now?"
    elif harmony.purity <= VLP:
        harmony.say "WOW!"
        harmony.say "I can't wait to get my lips round that!"
        "Both now naked, I lead Harmony to the bed and guide onto the mattress."
        "She sits facing me on all fours, looking up expectantly."
        "Her face is so cute and innocent."
        "Her breasts are so huge!"
        harmony.say "I want it right now - come to mama!"
    show harmony bj with fade
    mike.say "No, Harmony - just try kissing and licking it first, okay?"
    "Harmony nods, and then does as she's told."
    "Understandably, she starts out slowly and with some hesitance."
    "She pecks at the very tip of my cock, like she's giving it a chaste kiss."
    "And then the smallest glimpse of her tongue can be seen as she licks at it too."
    "All the while, Harmony keeps on glancing up at me, eyes wide and seeking approval."
    "As much as she's going slow, I'm getting a thrill out of watching her every move."
    "So I'm sure to nod and smile, encouraging her efforts and urging her on."
    "This seems to have the desired effect, as Harmony steadily takes more of me into her mouth."
    "As her confidence grows, it's like watching her try some new, exotic food for the very first time."
    "And with each second that passes, I get the impression that she's realising that she loves the taste!"
    show harmony bj suck
    show sexinserts head harmony zorder 1 at center, zoomAt(1, (720, 760))
    "Harmony closes her eyes as she swallows my cock ever deeper into her mouth."
    "Her head is bobbing up and down now, and the noises that she's making are of pure pleasure."
    "Sure, a blowjob from any girl that really knows what she's doing is great."
    "But Harmony's feeling her way here, and it seems like she's a natural too!"
    "Knowing that she's never done this before makes that much hotter."
    "It's like she never knew how much she liked the taste of cock until she got some of mine."
    show harmony bj blush
    "Then she takes me by complete surprise, swallowing me almost balls-deep!"
    "Harmony gags a little, evidently surprising herself too."
    "But she quickly recovers and keeps right on going."
    "She's deep-throating me without even knowing what that is!"
    "It's getting too much for me to keep a hold of myself."
    "I know that I'm going to lose it any moment now..."
    mike.say "Oh fuck..."
    mike.say "Harmony!"
    if harmony.purity >= AP:
        show harmony bj cum
        show sexinserts head harmony cum zorder 1 at center, zoomAt(1, (720, 760))
        with hpunch
        "Before Harmony can tell what's wrong, I shoot my load down the back of her throat."
        show harmony bj done choke with hpunch
        "And this time she really does begin to gag, dragging my cock out of her mouth before she chokes on it."
        "All I can do is watch, gasping for breath as she spits as much of the cum as possible onto the floor."
        hide sexinserts
        show cuddle harmony with fade
        "Utterly spent, I collapse onto the bed beside her."
        "I wrap my arms around Harmony and pull her close to me, feeling her return the gesture."
        mike.say "That was amazing, Harmony."
        mike.say "I think you're a natural when it comes to this kind of thing!"
        harmony.say "I don't know about that, [hero.name]."
        harmony.say "But I'm sure glad to have someone like you to teach me!"
    elif harmony.purity >= LP:
        show harmony bj cum
        show sexinserts head harmony cum zorder 1 at center, zoomAt(1, (720, 760))
        with hpunch
        "Before Harmony can tell what's wrong, I shoot my load down the back of her throat."
        show harmony bj done surprised with hpunch
        "But somehow she seems to be ready for it, swallowing desperately as it pumps out of me."
        "I watch her drink every last drop, gasping for breath as she greedily sates her thirst."
        hide sexinserts
        show cuddle harmony with fade
        "Utterly spent, I collapse onto the bed beside her."
        "I wrap my arms around Harmony and pull her close to me, feeling her return the gesture."
        mike.say "That was amazing, Harmony."
        mike.say "I think you're a natural when it comes to this kind of thing!"
        harmony.say "Thanks, [hero.name]."
        harmony.say "Having a guy like you to practice on sure helps too!"
    elif harmony.purity <= VLP:
        hide sexinserts
        show harmony bj -suck
        with hpunch
        "Before I can shoot my load down the back of her throat, Harmony drags my cock out of her mouth."
        "Panting desperately, she works the shaft with her hand while pointing the tip squarely into her face."
        with hpunch
        "I lose it a second later, and she's showered with sticky streamers of cum across her cheeks and nose."
        "Harmony giggles with delight as it runs down her face, licking eagerly where it comes within reach of her tongue."
        show cuddle harmony with fade
        "Utterly spent, I collapse onto the bed beside her."
        "I wrap my arms around Harmony and pull her close to me, feeling her return the gesture."
        mike.say "That was amazing, Harmony."
        mike.say "I think you're a natural when it comes to this kind of thing!"
        harmony.say "You bet I'm a natural, [hero.name]."
        harmony.say "Your cock's like a drug!"
        harmony.say "I want it inside of me all the time!"
    return

label harmony_fuck_titjob:
    $ game.play_music("music/roa_music/city_nights.ogg")
    if not harmony.flags.titjob:
        "It's been a great night so far, and I'm sure that both of us have had some serious fun."
        if harmony.purity >= HP:
            "Though I have to choose my next move carefully with Harmony."
            "I don't want to come on too strong and scare her off."
        elif harmony.purity >= AP:
            "She seems to be pretty up for doing something intimate."
            "Though I'm not sure if she'd go all the way tonight."
        else:
            "Harmony looks like she's up for absolutely anything I might suggest."
            "So why not take the chance to do something a little different?"
        mike.say "Harmony?"
        harmony.say "Yes, [hero.name]?"
        mike.say "Do you know what a boob-job is?"
        show harmony sad
        show fx question
        "Harmony looks confused for a moment."
        "She glances down at her more than ample chest and then back up at me."
        hide fx
        show harmony normal
        show fx question
        harmony.say "Wha...what are you trying to say, [hero.name]?"
        harmony.say "Do you think my chest is too small?!?"
        "I shake my head, realising that my choice of words was pretty poor."
        hide fx
        mike.say "No, Harmony, no - that's not what I meant!"
        mike.say "I mean like a hand-job, but using your breasts."
        mike.say "Some people call it a titty-fuck..."
        show harmony at center, vshake
        "Harmony looks a little shocked at his, her cheeks flushing red."
        "She looks down at her breasts again, as if she never thought such a thing possible."
        "And then she looks me straight in the eye."
        if harmony.purity >= HP:
            harmony.say "Is...is that kind of thing okay?"
            harmony.say "I thought masturbation was a sin?"
            mike.say "I don't think the bible mentions titty-fucks specifically, Harmony."
            mike.say "So it's technically okay."
        elif harmony.purity >= AP:
            harmony.say "Really, [hero.name]?"
            harmony.say "You wouldn't rather I used my hand instead?"
            mike.say "Oh no, Harmony - I'd LOVE it!"
        else:
            harmony.say "Hee, hee..."
            show harmony happy
            harmony.say "That sounds like SO much fun, [hero.name]!"
        show harmony happy
        "I can sense that she's still nervous, no matter how she tries to hide it."
        "And so I make sure to be as encouraging and supportive as possible."
        show harmony blush naked with dissolve
        "Which isn't exactly hard when I see her breasts fall out of the bra she's wearing underneath!"
        mike.say "Wow, Harmony!"
        mike.say "Those things look so soft and welcoming."
        mike.say "I bet they're a dream to fall asleep on!"
        if harmony.purity >= HP:
            harmony.say "Aw, [hero.name]!"
            harmony.say "Maybe you can do that later?"
        elif harmony.purity >= AP:
            harmony.say "Well, you're about to find out just how soft they really are!"
        else:
            harmony.say "Hey - no falling asleep until after we're done!"
        "Harmony reaches out and gingerly starts to undo my flies."
        "She keeps glancing up at me, as if seeking my approval."
        "And so I nod and smile at her, which seems to do the trick."
    else:
        mike.say "Ah, Harmony?"
        harmony.say "Yeah, [hero.name]?"
        mike.say "You remember what we did the last time?"
        mike.say "When you...used your breasts?"
        "Harmony flushes a little at the memory."
        "But she smiles all the same."
        "So maybe that means she's up for it?"
        harmony.say "You mean a boob-job?"
        harmony.say "Y...you want me to do it again?"
        mike.say "Yeah, Harmony - it was really great."
        mike.say "Would you do that for me?"
        harmony.say "Okay, if that's what you want - let's do it!"
        show harmony happy
        mike.say "I don't think I will ever get tired of that view."
        if harmony.purity >= HP:
            harmony.say "Aw, [hero.name]!"
            harmony.say "Thank you."
        elif harmony.purity >= AP:
            harmony.say "Look to your heart's content then."
        else:
            harmony.say "They are yours to use as you please."
        "Harmony reaches out and gingerly starts to undo my flies."
    "A couple of moments later, she has my cock out and is holding it in her hand."
    if harmony.purity >= HP:
        harmony.say "Oh...om my..."
        harmony.say "It's...so BIG!"
    elif harmony.purity >= AP:
        harmony.say "Mmm..."
        harmony.say "Looks like someone's excited!"
    else:
        harmony.say "Well hello, big boy!"
        harmony.say "Come to mama!"
    hide harmony
    show harmony titjob with fade
    "Harmony carefully guides my cock between her breasts, biting her lip as she does so."
    "I keep up the nods and encouraging words the whole time, eager to have this thing happen."
    "And the moment that I feel it slide into the middle of them, I know this is going to be something else!"
    show harmony titjob smile
    "Harmony's breasts are huge and heavy, like a couple of massive pillows."
    "They're also warm and soft, and they almost over my cock as they embrace it."
    "I'm not exaggerating either - all I can see is the tip!"
    "Slowly and with infinite care, Harmony presses her breasts together."
    "She catches my eye as she does this, and I nod my head almost desperately."
    mike.say "That's right, Harmony - just like that!"
    "She smiles, happy with the praise I'm giving her."
    mike.say "Now, up and down, yeah?"
    mike.say "Like your breasts are stroking it!"
    show harmony down
    "Now it's Harmony's turn to nod, as gets on with the task I've set her."
    "She bites her lip as she concentrates."
    "Which only serves to make her look that much cuter."
    "And thanks to the size of her breasts and the infinite care she's taking..."
    "Well, it goes without saying that the sensation is just incredible."
    mike.say "Harmony..."
    mike.say "That feels..."
    mike.say "So good!"
    show harmony titjob blush with dissolve
    "Harmony practically beams at my words."
    "And then she seems to redouble her efforts to please me."
    if harmony.purity >= HP:
        harmony.say "Really, [hero.name]?"
        harmony.say "Am I really doing it right?"
    elif harmony.purity >= AP:
        show harmony titjob lick
        show sexinserts head harmony zorder 1 at center, zoomAt(1, (720, 960))
        harmony.say "You like it that much?"
        harmony.say "I must really be getting the hang of it!"
    else:
        show harmony titjob lick
        show sexinserts head harmony zorder 1 at center, zoomAt(1, (720, 960))
        harmony.say "Mmm...hmm...hmm..."
        harmony.say "Your cock feels pretty good too, [hero.name]!"
    "By now, my cock is thrusting up from between Harmony's breasts like a piston."
    "She looks down and seems to notice just how close it is to her face for the first time."
    "I see a puzzled expression come over her face as she stares at it."
    "Almost as if she's thought of something for the very first time."
    harmony.say "Ah, [hero.name]..."
    harmony.say "What exactly happens when you..."
    harmony.say "When you...you know...when you..."
    "As if in answer to her question, I feel myself starting to cum."
    show harmony titjob cumshot with vpunch
    "And a moment later, I let go with a spurt of hot semen."
    show harmony titjob cum face
    show sexinserts head harmony cum zorder 1 at center, zoomAt(1, (720, 960))
    with vpunch
    "Which of course, sprays straight into Harmony's unsuspecting face."
    with vpunch
    harmony.say "Ah...oh..."
    harmony.say "Oh my goodness..."
    harmony.say "It's in my eye!"
    harmony.say "Gah...it's in my mouth!"
    show harmony titjob cum tits -cumshot
    "A girl with smaller breasts might have been able to release me in time."
    "But I'm pinned between Harmony's massive tits."
    "Which means there's no escape for her."
    "And by the time I'm finished cumming, she has what looks like a mask of cum!"
    "She looks at me, her eyes wide with shock."
    "But all I can think to do is offer her yet more praise."
    mike.say "That was amazing, Harmony."
    harmony.say "R...really?"
    harmony.say "I did well?"
    mike.say "You're the best!"
    "Harmony smiles at me through the cum that's still running down her cheeks and dripping off of her chin."
    "Luckily for me, she seems to have forgotten all about it in order to soak up the praise!"
    hide sexinserts
    return

label harmony_fuck_cunnilingus:
    if harmony.purity <= VLP:
        harmony.say "My pussy's aching for some cock, [hero.name]!"
        harmony.say "So you'd better fuck me nice and hard!"
    elif harmony.purity <= LP:
        harmony.say "I'm feeling SO horny right now, [hero.name]!"
        harmony.say "I can't wait to have some fun!"
    else:
        harmony.say "Oh...I'm so excited, [hero.name]!"
        harmony.say "It's so much fun when we make love, so special too!"
    if not harmony.flags.cunnilingus:
        mike.say "Actually, Harmony..."
        mike.say "I wondered if we could try something else tonight?"
        show harmony sad
        "Harmony instantly looks disappointed, her face falling."
        "So I hurry to reassure her that she's not about to lose out."
        mike.say "Don't worry, Harmony."
        mike.say "What I have in mind is still sex."
        mike.say "Just a slightly different kind, that's all!"
        show harmony normal
        "At the mention of the word sex, Harmony seems to regain hope."
        "But I can see that she's not yet convinced."
        harmony.say "What do you mean, [hero.name]?"
        show fx question
        harmony.say "How can it be as good as regular sex?"
        "I smile, trying to be as reassuring as I can."
        "Sometimes I forget just how innocent Harmony actually is."
        "She may have grown a great deal in terms of experience since we started dating."
        "But she still needs me to take her by the hand when we're trying something new."
        mike.say "Trust me, Harmony."
        mike.say "Oral can be as good as regular sex."
        show fx exclamation
        "At the mere mention of the word, Harmony's eyes go wide."
        harmony.say "You...you mean you want me to suck it?"
        harmony.say "I have to put your cock in my mouth?!?"
        mike.say "No, Harmony."
        mike.say "I'd be the one going down on you!"
        "Harmony instantly flushes a very fetching shade of red."
        show harmony blush
        "But I note with interest that she doesn't dismiss the notion."
        "In fact, she looks more than a little intrigued."
        if harmony.purity <= VLP:
            harmony.say "Mmm..."
            harmony.say "It's like I can feel you licking my pussy already!"
            harmony.say "What are we waiting for?"
        elif harmony.purity <= LP:
            harmony.say "I like the sound of that, [hero.name]."
            harmony.say "Let's do it!"
        else:
            harmony.say "That sounds...nice."
            harmony.say "I think I'd like to give it a try."
        "I give Harmony an encouraging nod and take her by the hand."
    else:
        mike.say "Ah, Harmony?"
        harmony.say "Yeah, [hero.name]?"
        mike.say "You remember what we did the last time?"
        mike.say "When I...went down on you?"
        "Harmony flushes a little at the memory."
        "But she smiles all the same."
        "So maybe that means she's up for it?"
        harmony.say "Y...you want to do it again?"
        mike.say "Yeah, Harmony - it was really great."
        mike.say "Are you okay with that?"
        harmony.say "Yes, if that's what you want - let's do it!"
    show harmony normal
    "She follows willingly as I lead her over to the bed and lie down."
    "Still holding her hand, I pat my chest lightly."
    mike.say "I want you to sit right here, Harmony."
    mike.say "One leg on either side and facing towards me, okay?"
    show harmony sad
    harmony.say "Are you sure about this, [hero.name]?"
    harmony.say "I don't want to keep you from breathing!"
    "I appreciate Harmony's concern, and she is a curvy girl."
    "But there's really no need for her to worry about crushing me."
    mike.say "It's okay, Harmony."
    show harmony normal
    mike.say "Just keep your weight on your knees the whole time."
    show harmony cunnilingus handjob with fade
    "Harmony nods and lets me guide her into position."
    "Which means I get a fantastic view of her naked body as she does so."
    "Seriously, when she's in place, I can't see her face for her breasts!"
    harmony.say "Did I do it right, [hero.name]?"
    harmony.say "Can you still breathe?"
    show harmony cunnilingus hurt
    harmony.say "Oh...oooh..."
    harmony.say "Oh god!"
    "Harmony moans as I begin to explore the folds of her pussy with my tongue."
    "And this practical demonstration of what I'm going to do to her seems to work."
    "Because she makes no effort to pull away from me the whole time."
    show harmony cunnilingus pleasure
    "Instead she quivers and quakes, letting me have my way with her."
    "In fact more than once I have to keep Harmony from going too far."
    "As she literally tries to push her pussy into my face!"



    "I know that Harmony's enjoying it as I begin to move inwards with my tongue."
    if not harmony.flags.cunnilingus:
        "But this is still her first time being eaten out, and I want to play it safe."
        "Sure, there's any number of things I could do to spice it up a little."
        "But I want to keep it simple and just let her enjoy this new experience."
        "That's why I keep things slow and steady, working from the outside in."
    show harmony cunnilingus pray
    "Harmony's pussy opens up for me like a flower as I go."
    "And she's getting wetter with every second that passes too!"
    "My head is sandwiched between her soft, rounded thighs."
    "My hands are clutching her buttocks, and they feel like a couple of pillows."
    "The first chance I get, I steal a glance upwards."
    "And I'm amazed to see that Harmony's hands are pressed together."
    "Tucked beneath her breasts, they make it look like she's actually praying!"
    "It's hard to hear anything with my ears covered by her thighs."
    "But I could swear that she's muttering something under her breath."
    "Maybe this is a genuine revelation for Harmony?"
    "A moment of religious and spiritual enlightenment?"
    "It certainly is for me."
    "As I can honestly say that I need to do this to her again."
    "And I feel like it could help me achieve nirvana!"
    "The sight only serves to push me onwards."
    "And soon enough, my tongue is as deep inside as it can go."
    show harmony cunnilingus ahegao
    "Harmony's hands are clasped together now, fingers intertwined."
    "The muttering that she was making before has been replaced too."
    "Now she's crying out, loud and clear."
    harmony.say "Ah..."
    harmony.say "Oh my..."
    harmony.say "What are you..."
    harmony.say "What are you doing to me?!?"
    show harmony cunnilingus squirt
    "Harmony gets her answer a few moments later."
    "She tosses her head this way and that, crying out as she cums."



















































































































































    show harmony cunnilingus pleasure blush -squirt
    "Harmony collapses into a heap atop me, panting and gasping for breath."
    "She doesn't seem to have the strength left to say as much as a single word."
    "But she wraps herself around me, still quivering from her orgasm."
    "And that lets me know that she's more than satisfied."
    return

label harmony_fuck_missionary(sexperience_min):
    if harmony.purity >= HP:
        "I take her by the hand guiding her down onto the bed."
        show harmony missionary with fade
        "This seems easier than I expected, most likely as Harmony's still stunned at the sight of my cock."
        mike.say "It's all perfectly normal, Harmony."
        mike.say "My natural reaction to seeing you like this."
        mike.say "Now trust me, I'm not going to do anything freaky to you, okay?"
        "Harmony nods, but all the same, I see her biting on her lip as I lay her down."
        mike.say "What is it, Harmony?"
        harmony.say "I...wanted to ask if you'd..."
        harmony.say "If you'd have sex with me up my bottom..."
        "I stop dead in my tracks at this, totally blind-sided by the unexpected nature of the request."
        harmony.say "That way, I'd still be a virgin."
        harmony.say "Technically, at least..."
        "I nod, still trying to wrap my head what Harmony wants me to do to her."
        mike.say "Ah...okay, Harmony."
        mike.say "If that's really what you want..."
        show harmony missionary mike
        "Harmony smiles and allows me to lay her flat upon her back."
        "Now that the matter's settled, she's clearly happy to let me get on with the proceedings."
        show harmony missionary anal orgasm
        "I return her smile as I climb atop her and begin to push the head of my cock between her buttocks."
        "I go as slowly and gently as I can, afraid of being too rough with her."
        "My guess is that Harmony's as much a virgin when it comes to her ass as she is in terms of her pussy."
        "Her face looks uncomfortable and a little pained as I find the hole that I'm looking for."
        show harmony missionary normal
        "But she keeps on smiling in approval the whole time, save for the occasional grimace."
        "The going is hard at first, Harmony's natural resistance making me battle to gain purchase."
        "And for a long while I think that this can only end in disaster and disappointment."
        show harmony missionary player
        "But then I see an odd transformation taking place, as her expression changes before my eyes."
        "The pain that was there before seems to become more intense for a moment, and is then transmuted into pleasure."
        show harmony missionary speed
        "This comes along with a sudden relaxing of her muscles, allowing me to begin thrusting in and out of her too."
        "Harmony's reaction reminds me of pictures I've seen of martyrs from the bible and other religious texts."
        "Someone that's endured great pain and emerged from the other side into divine ecstasy."
        show harmony missionary orgasm
        "She begins to writhe and wriggle beneath me, moaning from the pleasure that she's experiencing."
        "And believe me, the sight of Harmony awash with sensual delight is something that sticks in the memory!"
        "She hugs herself unconsciously, pushing her massive breasts together and almost into my face."
        "Which is altogether too much for me to be able to handle and keep going at this pace."
        call cum_reaction (harmony, 'anal', sexperience_min) from _call_cum_reaction_193
        if _return == 'anal_inside':
            "I'm buried as deep inside of Harmony's ass as I can get when I finally cum."
            show harmony missionary ahegao -speed with hpunch
            "And the moment that I do, her eyes pop open, an expression of shock on her face."
            harmony.say "Ooooh..."
            with hpunch
            harmony.say "What...what was that?!?"
            with hpunch
            mike.say "It...it was my orgasm, Harmony."
            mike.say "You made me cum inside of you."
            show harmony missionary blush player
            "She flushes a deep, beetroot red as the implications of this sink in."
            mike.say "Harmony...are you okay?"
            "She nods quickly, as if ashamed to admit something."
            "But then she speaks, in a small, meek voice."
            harmony.say "It...it felt nice."
            harmony.say "Very nice..."
        elif _return == 'anal_outside':
            "Aware of the fact this is Harmony's first time, I feel like I have to pull out before the end."
            show harmony missionary outside
            "But it only occurs to me as I yank my cock out of her ass that this might not be the less traumatic of the two options..."
            show harmony missionary cumshot with hpunch
            "I hear Harmony moan at the sensation of what I'm doing, and then squeal in genuine alarm."
            show harmony missionary cumbody with hpunch
            "Looking down, I watch as streamers of cum stripe her belly and breasts."
            show harmony missionary player -cumshot with hpunch
            harmony.say "Eww...[hero.name]!"
            harmony.say "Is this what's supposed to happen at the end?"
            "Harmony looks surprised, but not freaked out enough to make me worried that she'll be turned off sex for life."
            mike.say "Well, it's either that, or it all comes out while I'm up your butt!"
            "Harmony's mouth drops wide open in shock."
            harmony.say "NO!"
            "I nod, smiling at her innocence."
            "Harmony shakes her head in disbelief."
            "But I can already see her turning over the possibilities in her mind."
        $ harmony.flags.anal += 1
    elif harmony.purity <= VLP:
        "Pretty soon we're both naked and rolling on the bed."
        "The only thought on my mind being where I'm going to put it..."
        show harmony missionary
        menu:
            "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
                "It's only now that I realise just how much Harmony's talking dirty has gotten to me."
                show harmony missionary mike
                "And the more I think about it, the more I want to do something to match it."
                "So that's why I push my cock down a little lower than usual, making for her ass."
                "The first thing that Harmony knows about it is the sensation on my cock between her buttocks."
                "She lets out a loud yelp, instinctively raising her backside a little."
                "Which is ironic, because that helps me to get just the right angle."
                "And when she comes back down, she does so straight onto my waiting cock."
                show harmony missionary anal
                harmony.say "Whoa..."
                harmony.say "Hello there, big boy!"
                harmony.say "I hear yah knocking - you wanna come in?"
                "The tone of Harmony's voice and the look on her face make me want her all the more."
                "And so I grab her by the hips, almost forcing my cock into her ass."
                "Almost the very same instant that I push into her, she stops talking."
                show harmony missionary orgasm
                "Instead beginning to make sounds of pleasure almost animal in nature."
                "Harmony gasps and pants with each and every inch I make it inside of her."
                "And the sound makes the sensations I'm feeling that much more intense as a result."
                "Once I'm finally balls deep in her ass, I stay there, as still as I can manage."
                "I can feel Harmony starting to quiver around me, as if it's turning her muscles to jelly."
                harmony.say "Please, [hero.name]..."
                harmony.say "Please..."
                "The words sound like they taxed Harmony to speak them out loud."
                "And though I can't be sure what she wants, I take it as my cue to start moving again."
                "I start off slow, forcing the muscles of her ass to part for me as I do so."
                show harmony missionary speed
                "My speed begins to increase as those strained fibres obey me."
                "Pretty soon I'm thrusting in and out of Harmony's ass nice and smoothly."
                "Which is a shame, because I can soon feel myself starting to cum..."
                call cum_reaction (harmony, 'anal', sexperience_min) from _call_cum_reaction_194
                if _return == 'anal_inside':
                    "It's taken a hell of a lot of work for me to get my cock in there."
                    "And so there's no way I'm going to go pulling out at this point."
                    "I have no idea if Harmony even knows what's coming."
                    "But I thrust into her as far as possible all the same."
                    show harmony missionary ahegao
                    "It's only when she feels the sensation of me filling her that she reacts."
                    "Harmony's eyes pop open and her mouth stretches in a silent cry of surprise."
                    "I can only hope that she got all she wanted out of that."
                    "Because I known that I certainly did."
                elif _return == 'anal_outside':
                    "There's only one thing that I can imagine as more satisfying than cumming in Harmony's ass."
                    "And that would be the chance to cum all over those incredible breasts of hers."
                    show harmony missionary outside
                    "So I make the effort to pull my cock out of her ass in the moments before I cum."
                    "But as I manage to get it pointed in the right direction, Harmony almost leaps up at me."
                    show harmony missionary normal
                    "For a second, I have no idea what's going on."
                    "But then she snatches my cock in one hand and starts jacking me off with astonishing speed."
                    "Using her other arm, she presses her tits together and points my dick at the middle of the target."
                    show harmony missionary cumshot ahegao with hpunch
                    "Then the inevitable happens - I cum right in between her swelling mounds."
                    show harmony missionary cumbody with hpunch
                    "She makes satisfied moaning sounds as I do so, gasping as each new splash paints her chest."
                    show harmony missionary -cumshot player with hpunch
                    "And then she lets me go, licking her hand clean and smiling in satisfaction."
                    "Somehow, I can't shake the image of a self-satisfied cat that's got the cream..."
                $ harmony.flags.anal += 1
            "Fuck her pussy":
                "This is no time to get fancy - Harmony wants an express delivery of hard cock."
                "And I very much want to be the one to give it to her!"
                "She can sense it as well, smiling up at me as she feels me climbing atop her."
                call check_condom_usage (harmony, 150) from _call_check_condom_usage_58
                if _return == False:
                    call sleep from _call_sleep_55
                    return

                if CONDOM:
                    show harmony missionary condom
                show harmony missionary mike
                "The tip of my cock begins to rub against Harmony's lips."
                "And I can feel just how slick and ready for it she is right now."
                if not harmony.sexperience:
                    mike.say "This might hurt a little at first, Harmony."
                    mike.say "But that's natural, and it won't last long - okay?"
                    "Harmony nods and smiles, but bites her lip in anticipation."
                    "As gently as I can manage, I begin to push into her."
                    "I feel the resistance that I'd been expecting, and the sound of Harmony yelp a little."
                    "But then there's a tearing sensation, as she gives way to me."
                    "And even more relieving is the sound of Harmony's yelp turning into an unmistakable moan of pleasure."
                "This makes me all the more eager to get inside of her."
                show harmony missionary vaginal
                "And so I waste no more time in easing my cock into Harmony's pussy."
                "The feeling is just incredible, and I find myself moaning in the same way as she is."
                "My plan had been to take things slow and build up to a climax."
                show harmony missionary speed
                "But I can feel my pace quickening almost unconsciously with each second that passes."
                "Luckily for me, I can feel Harmony matching me as I do this."
                show harmony missionary orgasm
                "Which gives me the confidence of knowing that she's into it too."
                "With this in mind, I let go of any such restraints."
                "If it's going to be quick and passionate instead of slow and sensuous, then so be it!"
                "Pretty soon the pair of us are sweating like a couple of race-horses."
                "Not to mention the fact that we're snorting like them too."
                "No matter how much force I put into it as I thrust into Harmony, she takes all I have to give."
                "Almost as much of a thrill as being inside of her is the way this makes her body move."
                "Harmony's pretty much composed of generous, feminine curves."
                "And they jiggle along with my movements in the most fantastic ways possible."
                "But of course, the crowning glory is her breasts."
                "Large and yet perfectly in scale with the rest of her body, they bounce like water-balloons."
                "I had thought that they were hypnotic when she walked."
                "But they're simply spell-binding when she's on her back!"
                "Perhaps it's watching them so intently that finally makes me cum."
                "Though whatever the reason, it's going to happen in the next couple of seconds!"
                call cum_reaction (harmony, 'vaginal', sexperience_min) from _call_cum_reaction_195
                if _return == 'vaginal_condom':
                    "Those few seconds to put on a condom are paying off right now."
                    "Meaning that I can concentrate on giving Harmony all I have to give."
                    show harmony missionary -speed with hpunch
                    "And that's just what I do, making her moan as I finish inside of her."
                    with hpunch
                    "Afterwards there's no need to break the silence."
                    "We simply lie there, still entwined together and enjoying the moment."
                    "I'm totally satisfied."
                    "And I like to think that Harmony's silence means she is too."
                    $ harmony.love += 1
                elif _return == 'vaginal_outside':
                    "Even knowing that she can be as wild as they come, I still want to take care of Harmony."
                    show harmony missionary outside
                    "That's why I make damn sure that I can pull my cock out of her in time."
                    "Despite this, she still moans in disappointment at the sensation."
                    show harmony missionary cumbody normal with hpunch
                    "But then I hear her yelp in surprise, and I look down at her."
                    with hpunch
                    "Harmony's soft belly and massive breasts are streaked with lines of glistening cum."
                    show harmony missionary blush
                    "She smiles while her cheeks are flushed a bright shade of red."
                    "And I don't know if she's too surprised or too satiated to speak."
                    $ harmony.sub += 1
                    $ harmony.purity -= 2
                elif _return == 'vaginal_inside_pill':
                    harmony.say "Don't...stop...please!"
                    harmony.say "Pill...remember the pill!"
                    "I nod hastily, altering my plans to pull out before I fill her."
                    with hpunch
                    "And the very next second, I do just that."
                    show harmony missionary creampie normal with hpunch
                    "Harmony lets out a sensual whimper, holding on tight the whole time."
                    show harmony missionary blush with hpunch
                    "She smiles up at me, enjoying the sensation for as long as it lasts."
                    $ harmony.love += 2
                    $ harmony.purity -= 1
                elif _return == 'vaginal_inside_pregnant':
                    "Harmony might be the size of a cow right now, and making similar sounds."
                    "But I like to think that's where the comparison ends!"
                    "For one thing, no cow ever looked that good with a big, swollen belly."
                    show harmony missionary creampie normal with hpunch
                    "And that belly also means that I can take my time and finish inside of her."
                    show harmony missionary blush with hpunch
                    "Harmony moans as I do so, making me smile once more at the bovine comparison."
                    with hpunch
                    "Which is something I think I'll keep to myself..."
                    $ harmony.love += 3
                elif _return == 'vaginal_inside_happy':
                    "This is it - I need to pull out now, before it's too late!"
                    "But then I feel Harmony, clinging to me and making that all but impossible."
                    harmony.say "Oh no you don't, [hero.name]!"
                    harmony.say "I want to be your cum-bucket!"
                    "I stare at Harmony, truly baffled by her actions."
                    show harmony missionary creampie normal with hpunch
                    $ harmony.impregnate()
                    "And that's all the time it takes..."
                    with hpunch
                    harmony.say "Oh...oh fuck...[hero.name]!"
                    show harmony missionary blush with hpunch
                    harmony.say "Fill me up...fill me up!"
                    $ harmony.love += 5
                elif _return == 'vaginal_inside_mad':
                    show harmony missionary creampie normal with hpunch
                    $ harmony.impregnate()
                    "All that's on my mind is the need to shoot my load inside of Harmony."
                    with hpunch
                    "And all she seems to care about is letting me do it."
                    with hpunch
                    "But suddenly she seems to snap out of it."
                    hide harmony
                    show harmony naked angry
                    $ harmony.love -= 20
                    harmony.say "Oh fuck..."
                    harmony.say "Oh fuck, fuck, FUCK!!!"
                    harmony.say "[hero.name] - you came in me!"
                    harmony.say "You fucking came in me..."
                    "I stare at her in disbelief, still panting and sweating."
                    "But of course, she's right - we just made a big mistake!"
    elif harmony.purity <= LP:
        "With that, Harmony smiles as I push her gently down onto the bed."
        show harmony missionary
        call check_condom_usage (harmony, 150) from _call_check_condom_usage_59
        if _return == False:
            call sleep from _call_sleep_56
            return
        "Before this moment, I was only aware of just how much I wanted this."
        if CONDOM:
            show harmony missionary condom
        show harmony missionary mike
        "But it doesn't take more than a gentle stroke of Harmony's pussy for me to realise I'm not alone."
        "Her lips are already slick and more than ready for what lies ahead."
        "Though her own giggling and the nervous look on her face tells me that may not be true of the rest of her!"
        if not harmony.sexperience:
            harmony.say "Well, what are you waiting for?!?"
            harmony.say "Isn't there something that you're supposed to be stealing from me?"
            "For a moment, I can't believe what I'm hearing."
            "Is she actually trying to goad me into taking her virginity?"
        "I try the best I can to ignore it, and just get on with the task at hand."
        "Lowering myself down onto her, I begin to ease my cock into Harmony."
        if not harmony.sexperience:
            mike.say "This might hurt a little at first, Harmony."
            mike.say "But that's natural, and it won't last long - okay?"
            "Harmony nods and smiles, but bites her lip in anticipation."
            "As gently as I can manage, I begin to push into her."
            "I feel the resistance that I'd been expecting, and the sound of Harmony yelp a little."
            "But then there's a tearing sensation, as she gives way to me."
            "And even more relieving is the sound of Harmony's yelp turning into an unmistakable moan of pleasure."
        show harmony missionary vaginal
        "The sounds that she makes as I push the entire length of my cock into her are a massive turn-on."
        "And pretty soon I can't think of anything else, save for the act itself."
        show harmony missionary speed
        "My speed begins to increase as this happens, ensuring that the feelings get more intense the whole time."
        "By now, Harmony isn't making any kind of sound that could be mistaken for actual words."
        show harmony missionary orgasm
        "Instead she lets out only moans and cries of acute pleasure."
        "And her entire body moves in time with my thrusting in and out of her."
        "But most impressive of all is the way that her huge breasts jiggle and bounce."
        "I swear that they'd be enough to get me hard and bring me off on my own."
        "And as just one part of the whole package that is Harmony, they're enough to tip me over the edge..."
        call cum_reaction (harmony, 'vaginal', sexperience_min) from _call_cum_reaction_196
        if _return == 'vaginal_condom':
            "Remembering to use protection means that I can make sure I last until the very end."
            "And though she's incapable of speech right now, I think that's something Harmony's thankful for!"
            show harmony missionary -speed
            "At least she seems to writhe and wriggle on the end of my cock as I finish inside of her."
            "Even afterwards I'm still left in the dark, as she fails to regain the power of speech."
            "Instead she simply lies there, as if there's no way she could even try to get up."
            "I keep my mouth shut as well, just letting her recover in silence."
            "But still, I can't suppress a smirk as I think Harmony got just what she asked for."
            $ harmony.love += 1
        elif _return == 'vaginal_outside':
            "Maybe it's the extra care that a girl like Harmony needs to be treated properly."
            "Or maybe I'm just far more paranoid about that kind of thing than I realised."
            show harmony missionary outside cumshot with hpunch
            "Either way, I just manage to pull my cock out of Harmony before it's too late."
            with hpunch
            "I hear her yelp in surprise at the sensation, and then again a moment later."
            with hpunch
            "Looking down, I see the result of what I've just done."
            show harmony missionary -cumshot cumbody
            "Harmony's soft belly and massive breasts are streaked with lines of glistening cum."
            "She smiles while her cheeks are flushed a bright shade of red."
            "And I don't know if she's too surprised or too satiated to speak."
            $ harmony.sub += 1
            $ harmony.purity -= 2
        elif _return == 'vaginal_inside_pill':
            harmony.say "Don't...stop...please!"
            harmony.say "Pill...remember the pill!"
            show harmony missionary -speed creampie ahegao with hpunch
            "I nod hastily, scrapping my plans to pull out before I cum."
            with hpunch
            "And a moment later I let myself go while thrusting into Harmony."
            with hpunch
            "She lets out a long, deep whimper as I do so, clinging to me tightly."
            "But luckily I soon see that it was a desperate whimper of pleasure."
            "And I see her smiling up at me, clearly delighted with what just happened to her."
            $ harmony.love += 2
            $ harmony.purity -= 1
        elif _return == 'vaginal_inside_pregnant':
            "Harmony's moans become even louder as I feel myself losing it, deep inside of her."
            "Her belly's a constant reminder of the fact that we're fast becoming more than just a couple."
            show harmony missionary -speed creampie ahegao with hpunch
            "Unconsciously she cradles her swollen belly as she begins to feel the start of her own climax."
            with hpunch
            "And I enjoy the last few seconds of my own as I watch this show of maternal protection."
            with hpunch
            "All I can think at that moment is how she couldn't be more perfect."
            $ harmony.love += 3
        elif _return == 'vaginal_inside_happy':
            "If I don't pull out now, then I'm never going to!"
            "But before I can do a thing about it, I feel Harmony clinging onto me."
            harmony.say "[hero.name], don't you dare!"
            harmony.say "I want all of it - everything that you've got to give!"
            "I'm thrown by Harmony's words and actions."
            show harmony missionary -speed creampie ahegao with hpunch
            "Not for long, but for long enough."
            $ harmony.impregnate()
            with hpunch
            harmony.say "Oh...oh shit...[hero.name]!"
            harmony.say "It's like I can already feel our kid, growing inside of me!"
            $ harmony.love += 5
        elif _return == 'vaginal_inside_mad':
            show harmony missionary -speed creampie ahegao with hpunch
            $ harmony.impregnate()
            "I'm so wrapped up in the moment that nothing else can penetrate my brain."
            with hpunch
            "And Harmony begins to cum too, putting her in the same spot."
            with hpunch
            "But then she suddenly stiffens and I hear her wail."
            hide harmony
            show harmony naked angry
            harmony.say "Oh shit..."
            harmony.say "Oh bugger, wank, fuck!"
            harmony.say "[hero.name] - you just came inside of me!"
            "I look at her, shocked and stunned into silence."
            "I know that she's right - we just screwed up, real bad!"
            $ harmony.love -= 20
    else:
        if harmony.sexperience:
            "Still blushing, Harmony nods and crawls backwards onto the bed."
        else:
            "Harmony nods and lets me lay her down on the bed."
            harmony.say "Just promise that you'll be gentle, [hero.name]?"
            harmony.say "That thing looks very big!"
            "I give Harmony a reassuring nod, while her words give my ego a polish at the same time."
        show harmony missionary with fade
        call check_condom_usage (harmony, 150) from _call_check_condom_usage_60
        if _return == False:
            call sleep from _call_sleep_57
            return
        if CONDOM:
            show harmony missionary condom
        show harmony missionary mike
        "I smile at Harmony in what I hope is a reassuring manner, and then get down to it."
        if not harmony.sexperience:
            mike.say "This might hurt a little at first, Harmony."
            mike.say "But that's natural, and it won't last long - okay?"
            "Harmony nods and smiles, but bites her lip in anticipation."
            show harmony missionary vaginal
            "As gently as I can manage, I begin to push into her."
            "I feel the resistance that I'd been expecting, and the sound of Harmony yelp a little."
            "But then there's a tearing sensation, as she gives way to me."
            "And even more relieving is the sound of Harmony's yelp turning into an unmistakable moan of pleasure."
        else:
            show harmony missionary vaginal
            "I feel myself slide into her as the lips of her pussy part and allow me entry."
            "The first thrust in is more of a long, satisfying slide until I can go no further."
            "And I remain as deep as I can reach into Harmony for a long time."
            "All the while I hold her eye, studying the expression on her face."
            "Her features wear a fascinating mixture of disbelief and utter ecstasy."
            "As if a part of her cannot believe she could feel this way."
            "And another is realising that she wants to feel this way all of the time."
        show harmony missionary speed
        "I can't help smiling a little as I begin to move in and out of her."
        "And that's because I know just how much the sensation is going to start to build in intensity."
        "Sure enough, Harmony's eyes seem to become wider and her cries louder with every thrust."
        show harmony missionary orgasm
        "Pretty soon she's writhing around beneath me, bathed in sweat."
        "She hugs her huge breasts tightly, as if doing so will help to dull the sensations she's feeling."
        "But in truth, all it does is turn me on even more."
        "And I can feel myself beginning to cum a moment later..."
        call cum_reaction (harmony, 'vaginal', sexperience_min) from _call_cum_reaction_197
        if _return == 'vaginal_condom':
            "It's times like this that I'm truly glad to have taken the time to wear protection."
            "Not having to worry about pulling out means that I can keep things smooth as I cum."
            with hpunch
            "And so I do just that, finishing inside of Harmony and making sure it's a delight for her."
            with hpunch
            "I'm sure to linger afterwards too, keeping up the same pace until she follows my lead."
            show harmony missionary -speed ahegao with hpunch
            "And when she does cum beneath me, it's a moment that I'll always remember."
            "I'd be afraid to ask her as much, but I'm pretty sure I just gave Harmony her first orgasm too!"
            $ harmony.love += 1
        elif _return == 'vaginal_outside':
            "I hate to do this to her, but I have no choice other than to pull out at the very last moment."
            "Harmony gasps in surprise at the sensation, and then again as I cum over her belly and breasts."
            "She looks up at me as the cum covers her in sticky, white stripes, eyes wide with amazement."
            "All I can do is stare right back at her, as I try to slow my breathing down."
            "And despite the shock of me cumming all over her, Harmony doesn't look all that upset with how things turned out."
            "As I watch, she begins to blush and then smile."
            "I'm not a gambling man, but I'd bet that she rather enjoyed that."
            $ harmony.sub += 1
            $ harmony.purity -= 2
        elif _return == 'vaginal_inside_pill':
            harmony.say "Don't...stop...please!"
            harmony.say "Pill...remember the pill!"
            "I nod hastily, scrapping my plans to pull out before I cum."
            show harmony missionary -speed creampie ahegao with hpunch
            "And a moment later I let myself go while thrusting into Harmony."
            with hpunch
            "She lets out a long, deep whimper as I do so, clinging to me tightly."
            "But luckily I soon see that it was a desperate whimper of pleasure."
            "And I see her smiling up at me, clearly delighted with what just happened to her."
            $ harmony.love += 2
            $ harmony.purity -= 1
        elif _return == 'vaginal_inside_pregnant':
            show harmony missionary -speed creampie ahegao with hpunch
            "Harmony smiles up at me as I feel myself losing it, deep inside of her."
            with hpunch
            "There's no way that either of us can fail to be reminded of the life we've created together at this moment."
            with hpunch
            "She cradles her swollen belly as she begins to feel the start of her own climax."
            "And I enjoy the last few seconds of my own as I watch her do so."
            "My only thought as our intimacy comes to an end is of how perfectly beautiful she looks."
            $ harmony.love += 3
        elif _return == 'vaginal_inside_happy':
            "I don't want to do it, but I have to pull out right now."
            "But the moment that I make to do so, Harmony grabs my arms and holds me tight."
            harmony.say "[hero.name], no!"
            harmony.say "We can't stop now - it's like this is God's plan for us!"
            show harmony missionary -speed creampie ahegao with hpunch
            "I'm so taken aback by what she's saying that I forget what I was doing."
            with hpunch
            "And then I feel myself cumming, filling Harmony with all that I have."
            $ harmony.impregnate()
            with hpunch
            harmony.say "Oh...[hero.name]!"
            harmony.say "We're going to be a family!"
            $ harmony.love += 5
        elif _return == 'vaginal_inside_mad':
            show harmony missionary -speed creampie ahegao with hpunch
            "There's nothing at all on my mind in that moment, save for my own pleasure."
            with hpunch
            "Harmony too seems completely wrapped up in the sensations of her own orgasm."
            $ harmony.impregnate()
            with hpunch
            "But in the few seconds that follow, I feel her stiffen beneath me."
            hide harmony
            show harmony naked sad
            with fade
            $ harmony.love -= 20
            harmony.say "Oh God..."
            harmony.say "Oh Jesus, Mary and Joseph too!"
            harmony.say "[hero.name] - what have we done?!?"
            "I look at her, wide-eyed and totally unable to summon a response."
            "But she's right - what have we done?"
    return

label harmony_fuck_doggy(sexperience_min):
    show harmony naked with dissolve
    harmony.say "Ooh..."
    harmony.say "I feel so horny, [hero.name]!"
    show harmony doggy with fade
    if harmony.purity <= VLP:
        harmony.say "Come fuck me like an animal!"
    elif harmony.purity <= LP:
        harmony.say "Come and stick it in me!"
    else:
        harmony.say "Come over here and get me!"
    "I nod eagerly, hurrying over to do as I'm told."
    "I can feel my cock getting stiffer by the second."
    "And by the time I make it over to Harmony, it's hard as a rock."
    "I see her eyeing it over her shoulder, almost licking her lips."
    if harmony.purity <= VLP:
        harmony.say "My pussy's aching for it, [hero.name] - give it to me!"
    elif harmony.purity <= LP:
        harmony.say "Mmm...that's going to feel so good!"
    else:
        harmony.say "Ooh...I want you so badly, [hero.name]!"
    "The moment I climb up on the bed behind Harmony, she leans backwards."
    show harmony doggy out pov with fade
    "And when she pushes her ass hard up against me."
    "I can feel how hot and wet she is right now, how much she wants it!"
    "I need to make a decision as to where I'm going to put it."
    "Or else she'll make me cum just by rubbing her buttocks on my cock!"
    menu:
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            "As much as I could let myself be drawn towards Harmony's pussy, I don't go there."
            "Because with all of her wriggling, she's shoved my cock between the cheeks of her ass."
            "And I can practically feel the head being pulled into it already."
            "So why not just go with it?"
            "Putting my thumbs between her buttocks, I part Harmony's ass."
            show harmony doggy anal surprised
            "And then I push my cock straight into her."
            harmony.say "Wha..."
            harmony.say "What are you..."
            show harmony doggy hurt
            "With one more shove, I'm inside of it."
            "And I can feel the muscles of her ass trying to resist."
            if harmony.purity <= VLP:
                harmony.say "Ah...ah...oh yes...my ass!"
                show harmony doggy bounce pleasure -pov
                "I push as hard as I can, not holding anything back."
                "And I moan as I feel myself sinking ever deeper into Harmony."
                harmony.say "Harder, [hero.name], harder!"
                harmony.say "Please fuck my ass harder!"
            elif harmony.purity <= LP:
                harmony.say "Oooh...my asshole!"
                show harmony doggy bounce pleasure -pov
                "I push as hard as I can, not holding anything back."
                "And I moan as I feel myself sinking ever deeper into Harmony."
                harmony.say "Oh yeah..."
                harmony.say "I love it!"
            else:
                harmony.say "Oh...oh, my ass!"
                show harmony doggy bounce pleasure -pov
                "I push as hard as I can, not holding anything back."
                "And I moan as I feel myself sinking ever deeper into Harmony."
                harmony.say "That...that's good!"
                harmony.say "I like it!"
            "I don't think I've ever been so eager to do as I was told!"
            "That's why I don't waste any time starting to pound Harmony."
            "And believe me when I say, this is where a sturdy girl comes into her own!"
            "There's nothing wrong with a slender or petite girl, of course."
            "But the way that Harmony's built means she absorbs everything I have to give."
            "Her ass swallows my cock whole, muscles flexing and squeezing the whole time."
            "Her buttocks absorb the impact of my thighs slapping against them with ease."
            "Harmony's cute little belly feels so good in my hands."
            "And her breasts, I swear I can sense the weight of them as they sway back and forth."
            "The whole time that I'm fucking her, Harmony is moaning and wailing."
            "It's like my cock is touching parts of her even she didn't know were there!"
            "We're both slick with sweat by now, heat rolling off us in waves."
            "It feels like every inch of Harmony's skin is glistening with perspiration."
            "My hands are struggling to gain purchase on her."
            "But her ass keeps a hold of my cock as if her life depends on it."
            "And I know that she's not going to let me go until she's had her fill."
            "She squeezes me tighter than ever, making me groan."
            "Then I can feel it happening."
            "And there's nothing I can do to stop myself from cumming!"
            call cum_reaction (harmony, 'anal', sexperience_min) from _call_cum_reaction_198
            if _return == 'anal_inside':
                "Harmony has such a tight hold on me that I'm not going anywhere."
                show harmony doggy pov ahegao creampie -bounce with hpunch
                $ harmony.sub += 2
                $ harmony.purity -= 3
                "So all I can do is hold on to the end, losing it deep inside of her."
                with hpunch
                "She shudders as I let go, her entire body shaking at the sensation."
                show harmony doggy -pov with hpunch
                if harmony.purity <= VLP:
                    harmony.say "Oh fucking hell...fucking hell..."
                elif harmony.purity <= LP:
                    harmony.say "Oh Christ...oh Christ..."
                else:
                    harmony.say "Oh god...oh god..."
                "As soon as I'm spent, Harmony's muscles turn to water."
                "She collapses forwards, sliding off my cock."
                "And then she lays there, exhausted and bathed in sweat."
                "Cum seeping out of her ass and down the inside of her thighs."
            elif _return == 'anal_outside':
                "Somehow I manage to take a firm hold of Harmony's slippery ass."
                show harmony doggy pov out ahegao -bounce
                "And I drag my cock out of her in one smooth motion."
                "She shudders as I do so, her entire body shaking at the sensation."
                if harmony.purity <= VLP:
                    harmony.say "Oh fucking hell...fucking hell..."
                elif harmony.purity <= LP:
                    harmony.say "Oh Christ...oh Christ..."
                else:
                    harmony.say "Oh god...oh god..."
                "As soon as I'm out of her, Harmony's muscles turn to water."
                "She collapses forwards, exhausted and bathed in sweat."
                show harmony doggy cumshot cum onbody with hpunch
                $ harmony.sub += 1
                $ harmony.purity -= 2
                "A second later I shoot my load over her."
                with hpunch
                "Cum spatters her buttocks and thighs, running down the inside of her legs."
            $ harmony.flags.anal += 1
        "Fuck her pussy":
            "There's no resisting Harmony when she knows what she wants."
            "Because she makes me want it just as badly as she does!"
            "I can already imagine my cock sliding into her pussy."
            "So it's time to make that a reality..."
            call check_condom_usage (harmony, 150) from _call_check_condom_usage_61
            if _return == False:
                call sleep from _call_sleep_58
                return
            if CONDOM:
                show harmony doggy condom
            show harmony doggy vaginaltip
            "All it takes is a little push forwards, just a little."
            show harmony doggy vaginal surprised
            "And I can feel myself pushing into Harmony."
            show harmony doggy hurt
            "As well as hear the effect it's having on her too!"
            if harmony.purity <= VLP:
                harmony.say "Ah shit...that's it..."
                harmony.say "I love your cock...love it inside of me!"
            elif harmony.purity <= LP:
                harmony.say "Oh yeah..."
                harmony.say "I like it...I want more!"
            else:
                harmony.say "Mmm..."
                harmony.say "That feels so good!"
            "It's not like I need to hear Harmony tell me that this feels good."
            "I know that from the sensation of being inside of her."
            "All the same, it spurs me on to give her all I've got."
            "Harmony's haunches are already slippery with sweat."
            "But luckily for me, she's no frail little waif."
            "Which means I can take a good hold of her."
            "And then I can kick it into a higher gear."
            show harmony doggy bounce pleasure -pov
            "Pretty soon I'm pounding Harmony for all I'm worth."
            "My thighs are slapping against her buttocks."
            "And her heavy breasts are swinging back and forth in sympathy."
            if harmony.purity <= VLP:
                harmony.say "Fuck yes..."
                harmony.say "I want it harder...harder!"
            elif harmony.purity <= LP:
                harmony.say "That's right..."
                harmony.say "More...more...harder!"
            else:
                harmony.say "Oh yes..."
                harmony.say "Please..."
            "I'm breathing heavily by now, my heart pounding in my chest."
            "And Harmony is glistening with perspiration too."
            "My hands slide all over her body."
            "Breasts, belly and buttocks all slip through my fingers."
            "The only place that I seem to be safe is her pussy."
            "There she has a hold of my cock and she's not letting go!"
            "And I know that she's not going to let me go until she's had her fill."
            "She squeezes me tighter than ever, making me groan."
            "Then I can feel it happening."
            "And there's nothing I can do to stop myself from cumming!"
            call cum_reaction (harmony, 'vaginal', sexperience_min) from _call_cum_reaction_199
            if _return == 'vaginal_condom':
                "Harmony has such a tight hold on me that I'm not going anywhere."
                show harmony doggy ahegao pov -bounce with hpunch
                $ harmony.love += 1
                "So all I can do is hold on to the end, losing it deep inside of her."
                with hpunch
                "But we don't have to worry, as we used protection."
                with hpunch
                "She shudders as I let go, her entire body shaking at the sensation."
                if harmony.purity <= VLP:
                    harmony.say "Oh fucking hell...fucking hell..."
                elif harmony.purity <= LP:
                    harmony.say "Oh Christ...oh Christ..."
                else:
                    harmony.say "Oh god...oh god..."
                "As soon as I'm spent, Harmony's muscles turn to water."
                show harmony doggy vaginaltip creampie
                "She collapses forwards, sliding off my cock."
                "And then she lays there, exhausted and bathed in sweat."
                "Cum seeping out of her pussy and down the inside of her thighs."
            elif _return == 'vaginal_outside':
                "Somehow I manage to take a firm hold of Harmony's slippery ass."
                show harmony doggy ahegao out pov -bounce
                "And I drag my cock out of her in one smooth motion."
                "She shudders as I do so, her entire body shaking at the sensation."
                if harmony.purity <= VLP:
                    harmony.say "Oh fucking hell...fucking hell..."
                elif harmony.purity <= LP:
                    harmony.say "Oh Christ...oh Christ..."
                else:
                    harmony.say "Oh god...oh god..."
                "As soon as I'm out of her, Harmony's muscles turn to water."
                "She collapses forwards, exhausted and bathed in sweat."
                show harmony doggy cumshot cum onbody with hpunch
                $ harmony.sub += 1
                $ harmony.purity -= 2
                "A second later I shoot my load over her."
                with hpunch
                "Cum spatters her buttocks and thighs, running down the inside of her legs."
            elif _return == 'vaginal_inside_pill':
                harmony.say "Just do it - I'm on the pill!"
                "Harmony has such a tight hold on me that I'm not going anywhere."
                show harmony doggy pov ahegao creampie -bounce with hpunch
                $ harmony.love += 2
                $ harmony.purity -= 1
                "So I do as she says, losing it deep inside of her."
                with hpunch
                "She shudders as I let go, her entire body shaking at the sensation."
                with hpunch
                if harmony.purity <= VLP:
                    harmony.say "Oh fucking hell...fucking hell..."
                elif harmony.purity <= LP:
                    harmony.say "Oh Christ...oh Christ..."
                else:
                    harmony.say "Oh god...oh god..."
                "As soon as I'm spent, Harmony's muscles turn to water."
                show harmony doggy vaginaltip
                "She collapses forwards, sliding off my cock."
                "And then she lays there, exhausted and bathed in sweat."
                "Cum seeping out of her pussy and down the inside of her thighs."
            elif _return == 'vaginal_inside_pregnant':
                "Harmony has such a tight hold on me that I'm not going anywhere."
                show harmony doggy pov ahegao creampie -bounce with hpunch
                $ harmony.love += 3
                "So all I can do is hold on to the end, losing it deep inside of her."
                with hpunch
                "But we don't have to worry, thanks to the curve of her pregnant belly."
                with hpunch
                "She shudders as I let go, her entire body shaking at the sensation."
                if harmony.purity <= VLP:
                    harmony.say "Oh fucking hell...fucking hell..."
                elif harmony.purity <= LP:
                    harmony.say "Oh Christ...oh Christ..."
                else:
                    harmony.say "Oh god...oh god..."
                "As soon as I'm spent, Harmony's muscles turn to water."
                show harmony doggy vaginaltip
                "She collapses forwards, sliding off my cock."
                "And then she lays there, exhausted and bathed in sweat."
                "Cum seeping out of her pussy and down the inside of her thighs."
            elif _return == 'vaginal_inside_happy':
                harmony.say "Don't pull out!"
                harmony.say "Don't you dare!"
                "Harmony has such a tight hold on me that I'm not going anywhere."
                show harmony doggy pov ahegao creampie -bounce with hpunch
                $ harmony.love += 5
                "So all I can do is hold on to the end, losing it deep inside of her."
                with hpunch
                "She shudders as I let go, her entire body shaking at the sensation."
                with hpunch
                if harmony.purity <= VLP:
                    harmony.say "Oh fucking hell...fucking hell..."
                elif harmony.purity <= LP:
                    harmony.say "Oh Christ...oh Christ..."
                else:
                    harmony.say "Oh god...oh god..."
                "As soon as I'm spent, Harmony's muscles turn to water."
                show harmony doggy vaginaltip
                "She collapses forwards, sliding off my cock."
                "And then she lays there, exhausted and bathed in sweat."
                "I stare down at her in horror as she chuckles to herself."
                "Cum seeping out of her pussy and down the inside of her thighs."
                $ harmony.impregnate()
            elif _return == 'vaginal_inside_mad':
                harmony.say "Pull out!"
                harmony.say "Pull out, now!"
                "Harmony has such a tight hold on me that I'm not going anywhere."
                show harmony doggy pov surprised creampie -bounce with hpunch
                $ harmony.love -= 20
                "So all I can do is hold on to the end, losing it deep inside of her."
                with hpunch
                "She shudders as I let go, her entire body shaking at the sensation."
                with hpunch
                if harmony.purity <= VLP:
                    harmony.say "Oh fucking hell...fucking hell..."
                elif harmony.purity <= LP:
                    harmony.say "Oh Christ...oh Christ..."
                else:
                    harmony.say "Oh god...oh god..."
                "As soon as I'm spent, Harmony's muscles turn to water."
                show harmony doggy hurt vaginaltip
                "She collapses forwards, sliding off my cock."
                "And then she lays there, exhausted and bathed in sweat."
                "Harmony stares up at me in horror."
                "Cum seeping out of her pussy and down the inside of her thighs."
                $ harmony.impregnate()
    return

label harmony_sleep_date_fuck(location="hero"):
    if game.hour > 19 or game.hour < 6:
        scene bg bedroom1
        show harmony naked
        if harmony.is_sex_slave:
            harmony.say "May I share your bed tonight, Master?"
        else:
            harmony.say "Mmm...you cool with me spending the night here?"
        menu:
            "No":
                mike.say "No...I have to be up really early in the morning."
                "The sex was beyond incredible, but now I want to be alone."
                "Harmony frowns in disappointment, clearly trying to shrug off the sense of rejection."
                harmony.say "Okay...sleep well, I guess."
                "She shakes her head as she collects her things and leaves my bedroom."
                $ harmony.love -= 3
                call sleep from _call_sleep_28
                $ game.room = "bedroom1"
            "Yes":
                mike.say "YES...I mean, yes...if you want to!"
                "I try to keep from sounding too desperate and needy, but I'm not sure I manage it."
                show cuddle harmony
                "Harmony curling up against me beneath the covers is almost as good as the sex - almost..."
                if harmony.is_sex_slave:
                    harmony.say "Sweet dreams, Master..."
                else:
                    harmony.say "Sweet dreams, [hero.name]..."
                mike.say "You too, Harmony..."
                $ harmony.love += 3
                call sleep ("harmony") from _call_sleep_11
                $ game.room = "bedroom1"
    return

label harmony_hottub_sex_male:
    $ game.active_date.clothes = "swimsuit"
    $ CONDOM = False
    scene bg pool
    "I've been waiting to get Harmony into the hot-tub almost since the moment that we started to get serious."
    "Just the thought of that body in a tight, revealing swimsuit is enough to get me almost as hot as the water!"
    show harmony swimsuit with moveinleft
    "And so when she emerges from the house, still wrapped in a towel, I can feel my cock already starting to get hard."
    "Harmony seems to pick up on the vibes that I'm giving out too, a coy smile on her face as she walks over."
    "Her cheeks flush a little as she begins to remove the towel, and she lets out a nervous giggle."
    if harmony.purity > LP:
        show harmony blush
        harmony.say "Stop it, [hero.name]."
        harmony.say "Don't look at me like that!"
        harmony.say "You're making me blush!"
    else:
        show harmony happy
        harmony.say "I see you, [hero.name]."
        harmony.say "And I know what you're thinking too!"
        harmony.say "I'm thinking the same thing..."
    show harmony normal
    "Harmony finally lets the towel fall to the ground and steps into the tub."
    "I can't help staring at the way her body moves as she does so."
    "Her curves are almost hypnotic, swaying and swinging as she comes."
    "But her smile is the hottest thing of all."
    "That and the promise that I can see in her eyes as she gazes down at me."
    "Harmony lowers herself into the water, clearly enjoying the experience."
    show hottub harmony with fade
    "She closes her eyes for a moment, just enjoying the sensation of the heat and the bubbles."
    harmony.say "Mmm..."
    harmony.say "That's really nice!"
    harmony.say "It's like I can feel my muscles loosening."
    harmony.say "I had no idea I felt so stiff..."
    "I have no idea if her choice of words was deliberate or not."
    "But she's certainly having the opposite effect on me that the water is on her!"
    mike.say "Ah..."
    mike.say "That's great, Harmony."
    mike.say "You just lie back and relax..."
    "At the sound of my voice, Harmony opens one eye and then the other."
    "She regards me with a knowing expression on her face, smiling the whole time."
    if harmony.purity > LP:
        harmony.say "Are you sure that's all you want me to do?"
        harmony.say "Just lie here and chill out?"
    else:
        harmony.say "No way, [hero.name]."
        harmony.say "I was just loosening up a little."
        harmony.say "Now we can have some real fun!"
    "With that, Harmony glides over to where I'm sitting in the tub."
    "She wraps her arms around my neck, pulling herself close."
    "Harmony's body feels incredible as she snuggles against me."
    "It's so soft and welcoming, impossible to ignore."
    "I can't help but return the embrace and pull her in for a kiss."
    "As soon as our lips touch, I feel Harmony come alive with desire."
    "She moans and pants, even while we kiss."
    "And I can almost sense how much she wants me inside of her!"
    "I feel her hand tugging down my trunks and then grabbing my cock."
    call harmony_dick_reactions from _call_harmony_dick_reactions_1
    "Harmony rubs the shaft as she parts her own legs in anticipation."
    "But it's not like I need to be encouraged, and I soon respond in kind."
    show hottub sex male harmony outside with fade
    "I lift one of Harmony's legs, spreading her pussy as I do so."
    "And then I waste no time in rubbing the head of my cock against her lips."
    if harmony.purity > LP:
        harmony.say "Oh..."
        harmony.say "Oh, [hero.name]..."
        harmony.say "Don't tease me like that!"
    else:
        harmony.say "Oh fuck..."
        harmony.say "What are you waiting for?"
        harmony.say "Stick your cock in me!"
    "I hurry to do as I'm told, thrusting my cock forwards."
    "Harmony is already wet from the water and slick from excitement."
    "Which means that there's no more than a few seconds of resistance."
    show hottub sex male harmony inside
    "And then she surrenders to me, letting it sink into her in one smooth motion."
    "Harmony's mouth opens wide as she moans from the sensation."
    "She looks up at me, her eyes half-closed."
    "But her head is nodding as she shows an almost desperate need for more."
    "I begin to thrust in and out of her then, faster with every passing moment."
    "Normally I might have been more gentle, built up speed slowly at first."
    "But there's just something so sturdy and satisfying about pounding Harmony."
    "No matter how hard I push into her, she takes it and asks for more!"
    "And then there's the way that her entire body shakes and jiggles too."
    "Breasts, belly thighs and buttocks, all swaying and swinging."
    "She takes every ounce of energy that I put into her."
    "And then she transforms it into hypnotic motion that makes me want more!"
    "When she's not holding on for dear life, Harmony keeps her hands busy."
    "She squeezes her breasts and rubs at her clit, adding to her pleasure."
    "It seems like there's not enough that she can do to satisfy herself."
    "But the sight of it all and the feel of being inside her is more than enough for me."
    "And I can feel myself on the brink of cumming..."
    menu:
        "Cum inside":
            "I hold onto Harmony as tightly as I can, pushing into her as deeply as possible."
            show hottub sex male harmony cumshot with hpunch
            "And then I shoot all that I have straight into her, losing myself completely."
            with hpunch
            "She lets out a cry as I fill her pussy, shaking the whole time."
            show hottub sex male harmony ahegao with hpunch
            if harmony.purity > LP:
                harmony.say "Oh god..."
                harmony.say "I'm cumming!"
            else:
                harmony.say "Shit..."
                harmony.say "I...I love it..."
                harmony.say "I love it when you cum in me!"
            $ harmony.love += 1
            "Cum is already leaking our of Harmony as she succumbs to her own orgasm."
            "And I hold her up in the water while it takes hold."
        "Pull out":
            show hottub sex male harmony outside
            "I yank my cock out of Harmony in the last few seconds before I cum."
            "She moans at the sensation, shaking her head the whole time."
            if harmony.purity > LP:
                harmony.say "Ah..."
                harmony.say "What are you..."
            else:
                harmony.say "No...no..."
                harmony.say "I want it..."
                harmony.say "Cum in me - please!"
            $ harmony.sub += 1
            show hottub sex male harmony cumshot with hpunch
            "But by now it's too late, as I'm already shooting my load over Harmony."
            with hpunch
            "It rains down on her breasts and belly."
            with hpunch
            "And there it mixes with the droplets of water on her skin."
            "Her hands are all over her body a moment later."
            "Rubbing as much as she can into her breasts and pussy."
    hide hottub
    show hottub harmony
    with fade
    "Once it's over, Harmony collapses into the water, panting heavily."
    "I slip around behind her and take her in my arms."
    "She feels so soft and reassuring as I hold her close."
    "I really feel like I could close my eyes and drift off to sleep."
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ harmony.sexperience += 1
    $ game.active_date.clothes = None
    return

label get_harmony_lapdance:
    scene harmony lapdance
    show harmony lapdance nonpc
    with fade
    "Normally I'd be sitting here in the strip-club filled with excitement."
    "Just waiting for some smoking-hot girl to come over and give me a personal dance."
    "But this time it's a little different, as I already know the girl in question."
    "In fact, I know her well enough to consider her a friend."
    "Perhaps even more than that!"
    "Though it's not a surprise that she'd be into something like this."
    "Since I first met Harmony at the church, she's been on a kind of journey of self-discovery."
    "One that's seen her go from a pure, innocent, maybe even virginal girl to a..."
    "Well, to a girl that the furthest thing from innocent!"
    "And now she's gone so far as to get a gig here at the strip-club."
    "Suddenly suggestive music starts to play."
    "I look up, just in time to see Harmony peeking into the booth."
    harmony.say "Hey, [hero.name]..."
    harmony.say "Are you ready for me yet?"
    "I swallow audibly as I look Harmony in the eye."
    "And I'm so nervous that I nod without a single conscious thought."
    "Harmony nods in response and adds a mischievous giggle for good measure."
    "Then she slips into the booth and I get a look at what she's wearing."
    "And in that moment I know that I'm totally at her mercy."
    show harmony lapdance -nonpc with fade
    "Harmony's wearing something it'd be a stretch to even call underwear!"
    "Which means that her voluptuous figure is completely on show."
    "And I don't know what your opinion is of larger girls."
    "But frankly I don't really care."
    "Because Harmony looks like a goddess right now."
    "One of those ancient earth-mother types they always dig up statues of."
    "Her body is one hundred percent feminine and irresistible."
    "Oh, and did I mention the fact that she's insanely beautiful too?"
    "I'm hard before Harmony even closes the few feet between us."
    "And by that I mean painfully hard."
    "Like it's straining to get out of my pants."
    mike.say "Y...yeah, Harmony..."
    mike.say "Of course I'm ready!"
    "If Harmony detects the fake bravado in my voice, she doesn't show it."
    "Instead she gets straight down to business."
    "I look up as she stands over me."
    "And I can hardly see her face for her breasts."
    "Then my eyes are drawn downwards as she starts to move."
    "I might have been staring at Harmony's breasts just now."
    "But now I see her belly and thighs begin to move."
    "And nothing else seems to matter while they're in motion."
    "Harmony makes sure to turn as she moves too."
    "Which means the twin spheres of her buttocks are soon added to the mix."
    "They're even more compelling than what came before."
    "My eyes follow every move that they make without fail."
    "And each one seems to make my cock twinge."
    "If not my whole body twitch with desire for her."
    harmony.say "Like what you see, huh?"
    harmony.say "Well get an eyeful of this!"
    "Now Harmony begins to bend over as she dances before me."
    "Her pendulous breasts swaying in front of my face."
    "I could reach out and touch them with relative ease."
    "But I keep reminding myself of the rules in a place like this."
    "Sure, I know Harmony pretty well."
    "But touching her now could get my ass thrown out of here."
    "The thing is, I don't think Harmony got the memo on that one."
    "Because she seems to take my refusal to touch her personally."
    "You know, like it's some kind of insult to her dancing?"
    "Her answer is to turn her back on me, like she's annoyed."
    "But then she actually backs up her momentous ass."
    "And she sits down on me without warning."
    "That doesn't mean that Harmony stops moving though."
    "Instead she keep on wriggling and twisting on my lap."
    "The effect is instant and dramatic for me."
    "Before I was straining not to touch Harmony."
    "Now I'm battling to keep myself from losing it."
    "Sure, I have pants on right now."
    "But Harmony's ass is so big and heavy that it doesn't seem to matter."
    "Her buttocks are rubbing against my cock, massaging it pretty hard."
    "I don't know if Harmony is aware of what she's doing."
    "All I know is that she's rubbing herself back and forth in time to the music."
    "And if she doesn't stop soon..."
    "Oh shit..."
    "Too late!"
    "All it takes is one more pass from Harmony."
    "Her buttocks press down on my cock one more time."
    with vpunch
    "And that's it, I feel myself letting go, helpless to resist."
    with vpunch
    mike.say "Oh..."
    with vpunch
    mike.say "Oh fuck..."
    mike.say "Harmony!"
    "Harmony looks back over her shoulder as I buckle beneath her."
    "And the expression on her face answers my question once and for all."
    "She's grinning from ear-to-ear, fully aware of what she's done to me."
    show harmony lapdance worried
    harmony.say "Aww, [hero.name]!"
    harmony.say "Did you have a little accident?"
    show harmony lapdance normal
    harmony.say "Maybe pop into the bathroom and clean yourself up?"
    "With that, Harmony gets to her feet."
    "She hurries to the curtains of the booth."
    "And there she pauses just long enough to blow me a kiss."
    "Then she's gone, leaving me to sort myself out."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
