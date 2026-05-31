label mike_date_eat_a_burger:
    "[mike.name] doesn't hold back when his burger arrives, taking a huge bite straight away."
    "I guess he must have been hungry, or skipped lunch maybe."
    "Because the thing doesn't last long."
    return

label mike_date_buy_drink:
    "[mike.name] accepts the drink happily enough, for sure."
    "But he sips it slow and sparingly."
    "Perhaps he's just not a big drinker?"
    return

label mike_date_play_darts:
    "I don't have to twist [mike.name]'s arm for a game of darts."
    "He's up and ready to go almost the moment I suggest it."
    "And I soon find out the reason - he's pretty damn good too!"
    return

label mike_date_pub_play_pool:
    "I make the mistake of letting [mike.name] break, thinking that I'm being kind."
    "But I catch the twinkle in his eye as he winks at me."
    "And the trick-shot he pulls off afterwards confirms my worst fears!"
    return

label mike_date_buy_a_round:
    "Ask [mike.name] if he wants anything from the bar, and he shrugs, then nods."
    "He mutters that he'll get the next round in after this one."
    "So he's happy to let me stand a round, but will return the favour."
    "I guess that means he's a pretty modern kind of guy."
    return













label mike_halloween_invitation_female:
    show mike
    "Almost the moment I agreed to the Halloween party, I knew who I wanted to invite."
    "I might have been joking about Sasha and [mike.name] getting together when they pitched the party."
    "But that really was nothing more than a joke, because it's [mike.name] I want to be my date!"
    "Though I couldn't just come out and ask him there, right in front of Sasha."
    "No, I needed to be able to regroup and start making plans on where and when to ask him."
    "And that's just what I do, choosing my moment carefully so as to maximise my chances of success."
    "Don't get me wrong, I'm pretty sure [mike.name] will want to be my date."
    "But there's nothing wrong with stacking the deck in my favour, now is there?"
    "So when I think that the time is just right, I bring it up with [mike.name]."
    bree.say "[mike.name]..."
    bree.say "Have you thought about inviting anyone to the Halloween party?"
    bree.say "I'm just curious, because I had someone in mind myself."
    show mike surprised
    "[mike.name] looks up, genuine surprise on his face."
    mike.say "Oh no..."
    mike.say "I totally forgot, [hero.name]!"
    show mike normal
    mike.say "I guess I'll probably invite some of my friends."
    mike.say "You know, like Jack and Shawn?"
    "I nod and smile, trying to hide my instant reaction to those two guys."
    "I mean, I know that I kinda like nerds."
    "But they're some kind of super-nerd!"
    bree.say "Well..."
    bree.say "I was going to ask you to come."
    show mike surprised
    "Now [mike.name] really does look confused."
    mike.say "But I'm already coming, [hero.name]..."
    mike.say "We all are, remember?"
    mike.say "Because we're organising the party!"
    "I try to keep from rolling my eyes at his cluelessness."
    bree.say "I know that, [mike.name]!"
    bree.say "I meant ask you to be my date, yeah?"
    "Now I see [mike.name]'s eyes go wide as he finally understands."
    show mike normal
    mike.say "Oh..."
    mike.say "Oh yeah..."
    mike.say "Now I get you, [hero.name]!"
    bree.say "Well?"
    bree.say "Are you going to give me an answer this century?"
    if mike.love >= 100:

        "[mike.name] begins nodding almost as soon as the words are out of my mouth."
        "And he doesn't stop while he's answering me either."
        show mike happy
        mike.say "Of course I will, [hero.name]!"
        mike.say "I'd love for us to kind of be an item at the party."
        mike.say "Actually...I was going to ask you the same thing."
        $ mike.love += 1
        "The admission comes as a genuine surprise."
        "So much so that I have to ask for confirmation."
        bree.say "You were?"
        show mike down
        "[mike.name] shrugs and begins to look a little sheepish."
        mike.say "Well...I was thinking about it."
        mike.say "But I couldn't think of a way to ask you."
        bree.say "You could have just come out and done it."
        bree.say "You know, like I did?"
        show mike normal
        "[mike.name] nods and offers me a shrug by way of explanation."
        mike.say "You make it sound so simple, [hero.name]!"
        mike.say "I'd have had to pluck up the courage."
        mike.say "And then there's the fear you'd say no!"
        bree.say "Well you don't have to worry about that now."
        bree.say "You channel all your energy into your costume instead."
        bree.say "Which, by the way, had better be impressive!"
        show mike happy
        mike.say "Oh, don't worry, [hero.name]..."
        mike.say "It will!"
        $ game.flags.halloween_girl = "mike"
    else:

        "[mike.name] begins shaking his head almost as soon as the words are out of my mouth."
        "And he doesn't stop while he's answering me either."
        mike.say "We can't do that, [hero.name]!"
        mike.say "We're supposed to be the one's hosting the party."
        mike.say "If we have dates of our own, then we'll just get distracted."
        "Of course I feel an instant sense of disappointment."
        "But I'm not ready to give up just yet."
        bree.say "We don't have to make a big deal out of it, [mike.name]."
        bree.say "In fact, we could just keep it between us."
        bree.say "How about that?"
        "[mike.name] shakes his head again, dismissing my suggestion."
        mike.say "We'd still know, [hero.name]!"
        mike.say "And what about poor Sasha?"
        mike.say "We'd be leaving her out."
        mike.say "No, I'm sorry..."
        mike.say "It just wouldn't work."
        "I'm about to try another argument on [mike.name]."
        "But he ends the discussion by hurrying away."
        "I could follow him and keep things going."
        "But I don't think it's make any difference."
        "So I just have to accept that he's not going to be my date after all."
    return

label mike_halloween_arrival_female:
    scene bg house
    "Sasha heads into the hallway to see if any of the guests have arrived."
    "For a moment I think about calling out to her and asking why she'd bother."
    "Because the moment they arrive, the guests are bound to ring the doorbell or knock."
    "But then a thought occurs to me and I hold my tongue, shooting a glance at [mike.name]."
    scene bg livingroom
    show mike halloween
    with fade
    "This might well be the last chance that we have to talk in private tonight."
    "And seeing as he's my date, I want to exchange a few words while we still can."
    "So I sidle over to where he's standing and land a soft punch on his arm."
    show mike surprised
    mike.say "Wha..."
    show mike normal
    mike.say "Oh, hey, [hero.name]."
    mike.say "What's up?"
    bree.say "I just wanted to say that I think tonight's going to be fun."
    bree.say "But I'd still rather it was just the two of us having fun together."
    show mike happy
    "The smile that spreads across [mike.name]'s face makes me crack one too."
    "But I manage to resist the urge to nod my head up and down like a Jack-in-the-Box!"
    "That's something I leave up to him."
    mike.say "Me too, [hero.name]!"
    show mike normal
    mike.say "Hey, now that Sasha's not here..."
    mike.say "What do you really think of my costume?"
    menu:
        "Compliment":
            "I don't even have to think about my response to the question."
            "Nodding my head, I lean in closer to [mike.name]."
            "Which is pretty pointless as we're the only ones within earshot."
            "But somehow doing so makes me feel safer saying this anyway."
            bree.say "Don't worry about what Sasha thinks."
            bree.say "She might pretend to get nerd stuff."
            bree.say "But we both know most of it goes over her head."
            show mike happy
            $ mike.love += 1
            "A look of hope blossoms on [mike.name]'s face as he hears this."
            "And he's nodding like crazy again."
            mike.say "You really mean that, [hero.name]?"
            mike.say "You like my costume?"
            bree.say "What's not to like, [mike.name]!"
            "[mike.name] opens his mouth to say more."
            "But at that very moment I hear the sound of a knock at the door."
            "So I hold up a hand as I make for the hallway too."
            bree.say "Hold that thought, [mike.name]..."
            bree.say "We have guests to entertain!"
        "Criticize":
            "I think about lying to [mike.name] for the sake of his ego."
            "But as I take a second look at his costume, I just can't."
            "I feel like it's important for us to be honest with each other."
            "So I take a deep breath and then let him have it."
            bree.say "Urgh..."
            bree.say "It is kind of dated, [mike.name]."
            mike.say "I think the word you're looking for is 'retro', [hero.name]!"
            mike.say "You know, the fusion of the nostalgic and the current?"
            mike.say "Coming together to make something cooler than both?"
            bree.say "Or in this case, lamer than both!"
            show mike annoyed
            $ mike.love -= 4
            "[mike.name] opens his mouth to argue."
            play sound door_knock
            "But at that very moment I hear the sound of a knock at the door."
            "So I hold up a hand as I make for the hallway too."
            bree.say "Hold that thought, [mike.name]..."
            bree.say "We have guests to entertain!"
    scene bg black with dissolve
    pause 1
    return


label mike_halloween_party_female:
    $ game.pass_time(2)
    scene bg livingroom
    show mike halloween at left5
    show jack halloween normal at right5
    with dissolve
    mike.say "Ah...yeah, Jack."
    mike.say "That's really fascinating!"
    mike.say "I never thought that way about D&D!"
    jack.say "I know, right?"
    jack.say "And you'll freak when you hear this!"
    "I turn around to see that Jack has [mike.name] cornered."
    "He's in full-on geek mode, talking constantly."
    "And from the look on [mike.name]'s face, he needs rescuing."
    "Because Jack's in danger of waking up his inner-geek."
    "And if that happens, I'll lose him to nerd chat all night!"
    "I lean in closer, inserting myself into the conversation."
    menu:
        "Save [mike.name]":
            bree.say "Urgh..."
            bree.say "Come on, Jack!"
            bree.say "We're all nerds here."
            bree.say "But there's a time and a place, yeah?"
            show jack sad
            "Jack looks suddenly bashful."
            "And he finally stops talking."
            mike.say "She's right, Jack."
            mike.say "We can chat about D&D anytime."
            mike.say "You should really try to mingle a little."
            jack.say "Erm...okay..."
            jack.say "I'll give it a try."
            hide jack with easeoutright
            $ jack.love -= 2
            "With that, Jack wanders off to bother someone else."
            show mike happy
            mike.say "Ah..."
            $ mike.love += 2
            mike.say "Thanks, [hero.name]..."
            mike.say "You saved me from getting drawn into the geek vortex!"
        "Back up Jack":
            bree.say "I'm going to have to stop you there, Jack!"
            "At the sound of my voice, both [mike.name] and Jack look around."
            "Jack looks confused, but [mike.name] seems to think he's been saved."
            bree.say "Because you've left out an important point."
            bree.say "That rule WAS included in second edition!"
            $ mike.love -= 2
            $ jack.love += 2
            show jack happy
            "Jack looks instantly intrigued."
            show mike down
            "But [mike.name]'s face falls."
            mike.say "Erm..."
            mike.say "You really want to talk D&D too, [hero.name]?"
            "I ignore [mike.name] and launch into my speech about rules minutiae."
            "Jack listens with great interest as I go on."
            "And [mike.name] has no choice but to stand there and endure it."
    scene bg black with dissolve
    pause 1
    return

label mike_halloween_dance_female:
    $ game.pass_time(2)
    scene bg livingroom
    show mike halloween
    with dissolve
    mike.say "Aw, come on, [hero.name]..."
    mike.say "Don't you want to dance?"
    mike.say "What are we waiting for?"
    "[mike.name] won't seem to shut up about wanting to dance with me."
    "But none of the songs on the playlist make me want to do it."
    "After all, we picked them for a Halloween Party."
    "Not to create a romantic atmosphere on the dancefloor!"
    "I've been passing on every song that starts playing for ages now."
    "Pretty soon I'm going to have to say yes to something."
    "Or else tell [mike.name] I'm just not in the mood tonight."
    menu:
        "Accept":
            bree.say "You know what, [mike.name] - you're right."
            bree.say "This is a party."
            bree.say "And we're supposed to be having fun!"
            show mike happy
            $ mike.love += 2
            "[mike.name] beams with delight as I let him lead me onto the dance-floor."
            hide mike
            show dance mike halloween
            "And as soon as we start dancing, the music doesn't seem to matter."
            "All that does is the fact we're together and having a good time."
            "I'd have been cool with keeping things light and fun."
            "But [mike.name] seems to have other things in mind!"
            "He dances as close to me as he can."
            "But he still keeps from overstepping the line."
            "That is until I begin to dance even closer to him."
            "Letting him know that I'm into that too."
            "In fact, I can soon feel just how excited [mike.name]'s getting."
            "He knows that I know too, his face flushing red."
            mike.say "I..."
            mike.say "Erm..."
            bree.say "It's okay, [mike.name]..."
            bree.say "I'll take it as a compliment!"
        "Refuse":
            bree.say "No, [mike.name]..."
            bree.say "I really want to dance to the right song."
            bree.say "Let's just wait for it to come along, okay?"
            show mike annoyed
            $ mike.love -= 1
            "[mike.name] shakes his head and lets out a groan."
            mike.say "Urgh..."
            mike.say "What's up with you tonight?"
            mike.say "You're no fun!"
            mike.say "Maybe I should just do me!"
            "With that, [mike.name] walks away from me."
            "I watch as he strides out onto the dance-floor alone."
            "But it doesn't take long for him to attract company."
            "Sasha and Lexi are there in the blink of an eye."
            "Both of them dancing for all they're worth."
            "All I can do is watch as [mike.name] laughs and flirts with them."
            "And all the time he's making sure that I can see it too!"
    scene bg black with dissolve
    pause 1
    return

label mike_halloween_sex_female:
    scene bg livingroom
    show mike halloween
    with dissolve
    "It's getting pretty late by now and the party's starting to wind down."
    "Everyone's either tired, drunk or both and wanting to chill out."
    "And I know that I'm feeling the same way after playing host all night."
    "[mike.name] looks like she's exhausted too, but his eyes are still bright."
    "You know that look he sometimes gets?"
    "Like a kid that's been promised a treat if he behaves himself?"
    mike.say "I think we did pretty well tonight, [hero.name]."
    mike.say "We turned out to be good hosts after all!"
    bree.say "Yeah, [mike.name]."
    bree.say "Everyone seemed to have a good time."
    show mike happy
    "[mike.name] nods, smiling happily."
    mike.say "In fact, I think we did so well we deserve a reward."
    mike.say "Maybe a little celebration for just the two of us?"
    "There you go!"
    "You see that?"
    "I got him bang to rights!"
    "But it's only now that I realise we're standing outside [mike.name]'s bedroom door."
    "He leans against it and gives me a suggestive wink."
    "But then what am I complaining about, exactly?"
    "Everything he's said is the truth, and he is my date tonight."
    "Plus he looks really cute in his costume too!"
    bree.say "Sounds good to me, [mike.name]."
    bree.say "We worked our asses of tonight."
    bree.say "But...are you thinking what I think you're thinking?"
    "By way of answer, [mike.name] gives me what I think he imagines is a seductive wink."
    scene bg bedroom1
    show mike halloween blush
    with fade
    "And then he opens the door to his room, gesturing for me to step inside."
    "There's nothing more that either of us needs to say."
    "Inside and with the door closed, he begins to strip off his clothes."
    "That shouldn't be such a strange thing for either of us to be doing."
    "But as we're both still dressed in our costumes, it feels pretty weird."
    show mike naked with dissolve
    "[mike.name] finishes first, and chuckles as I struggle to free myself."
    show mike naked at center, zoomAt (1.5, (640, 1040))
    "He walks over and stops me to get totally reed of my costume."
    "And then he takes my hand, leading me over to his bed."
    "[mike.name] doesn't make any demands of me."
    "I don't think he'd dare to be so presumptuous."
    "But he doesn't know how much I want him right now."
    "So it seems to surprise him when I lie down on the bed and beckon to him."
    "[mike.name] hurries to join me, lying at my side."
    show mike cowgirl halloween with fade
    "And he offers no resistance as I roll him onto his back."
    "I can feel the fatigue melt away as I straddle his thighs."
    show mike cowgirl out
    "It's still there in the background."
    "But I know that I have enough energy in reserve for this."
    "Enough to make sure that this is a memorable end to the night."
    "I can already see [mike.name]'s cock beginning to get nice and hard."
    "He nods, encouraging me without the need for words."
    "The head of his cock brushes against the lips of my pussy."
    show mike cowgirl blush
    "And he closes his eyes, moaning with the anticipation of pleasure."
    show mike cowgirl pleasure vaginal
    "I go slowly, coaxing his cock inside of me, rather than teasing."
    "And [mike.name] nods all the more, urging me on."
    show mike cowgirl smile
    "I can feel myself opening, slowly but surely, like a flower parting its petals."
    "I sink into him with the same slow progress until I can go no further."
    "It's like I can feel the fatigue in [mike.name]'s body."
    "I can sense the way that it's being burnt away."
    "My movements are still slow and deliberate."
    show mike cowgirl pleasure
    "But I can already feel that [mike.name] wants more from me."
    "It's not enough to simply end the night with a lazy fuck."
    "He wants to use up every last ounce of his strength."
    "That and then to fall asleep satisfied and sated."
    "My speed is picking up now, adrenaline masking my exhaustion."
    "I can feel the sweat running down the length of my spine."
    "But still I keep on pushing myself harder."
    "[mike.name] begins to gasp beneath me, a deep and helpless sound."
    show mike cowgirl up
    "I'm panting, struggling to fill my lungs with each breath."
    "And yet I keep on going, by now riding [mike.name] has hard and fast as I can."
    "I can see that he's grabbing handfuls of the bedclothes."
    "Almost like he's holding on for dear life!"
    "My guess is that he doesn't have the energy to do anything more."
    "And finally I can feel the night catching up with me."
    "I know that I've used up the very last of my strength."
    "So there's nothing I can do to hold on when the end comes."
    show mike cowgirl ahegao with vpunch
    "My body stiffens as I cum, all of my muscles clamping down on his cock."
    with vpunch
    "And he quivers, taking it all without hesitation."
    show mike cowgirl creampie with vpunch
    "Then [mike.name] lets go too, and I feel him explode, deep inside me."
    show mike cowgirl resting dickcum cum onpussy
    "With that, I feel my muscles turn to water."
    "I collapse, almost unable to move."
    show mike cowgirl down
    "And he clings onto me, riding out the last moments of his orgasm."
    "His face is the last thing I see before my eyes close."
    "Then I'm asleep and probably snoring too!"
    $ mike.sexperience += 1
    $ game.pass_time(1)
    return


label mike_after_dance_success_with_female:
    show mike smile
    "I finish dancing and the world around me comes back into focus."
    "That's because I always kind of zone out whenever I bust a move."
    "But this time it happens, the first thing I see is [mike.name]."
    "So I make a point of waving and hurrying over to him."
    bree.say "Hey, [mike.name]..."
    bree.say "Did you see me dancing just now?"
    "The moment I ask the question, [mike.name] starts nodding."
    "Almost like he's been bursting to talk about it for ages."
    show mike happy
    mike.say "Did I see it?"
    mike.say "I couldn't take my eyes off you!"
    show mike smile
    "I blink in surprise at [mike.name]'s answer."
    "More than a little amazed by his enthusiasm."
    bree.say "You couldn't?"
    "[mike.name] shakes his head."
    show mike happy
    mike.say "I was watching you the whole time, [hero.name]."
    mike.say "And I never knew you could dance like that."
    show mike smile
    bree.say "That's...kind of you to say."
    bree.say "You want to dance with me some time?"
    show mike happy
    mike.say "I'd love to, [hero.name]!"
    mike.say "So long as you teach me some of your moves."
    show mike normal
    return

label mike_after_dance_failure_with_female:
    show mike annoyed
    "I finish dancing and the world around me comes back into focus."
    "That's because I always kind of zone out whenever I bust a move."
    "But this time it happens, the first thing I see is [mike.name]."
    "So I make a point of waving and hurrying over to him."
    bree.say "Hey, [mike.name]..."
    bree.say "Did you see me dancing just now?"
    "The moment I ask the question, [mike.name] seems to wince."
    "It's almost like the words cause him physical pain."
    show mike shout
    mike.say "Yeah..."
    mike.say "I kind of did!"
    show mike sad
    "I can't help frowning in confusion."
    bree.say "What's that supposed to mean?"
    bree.say "You make it sound like it was painful!"
    "[mike.name] looks around, as if to make sure nobody else is listening."
    "Then he lean in closer and gives me an answer."
    show mike shout
    mike.say "Thing is, [hero.name]..."
    mike.say "It kind of was!"
    show mike down
    bree.say "WHAT?!?"
    "[mike.name] waves his hands in front of me."
    "Obviously trying to get me to be quiet."
    show mike shout
    mike.say "Sorry to have to be the one to tell you this, [hero.name]..."
    mike.say "But you're like, a really bad dancer!"
    show mike normal
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
