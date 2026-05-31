label shawn_after_dance_success_with_female:
    show shawn normal
    "I'm having so much fun dancing that I almost forget to look out for Shawn."
    "But when I do finally spot him, I can't help staring in surprise."
    "And that's because he's already staring at me, wide-eyed with amazement."
    "He keeps staring too, right up until I'm done with the dancing."
    "Then he hurries over to catch me before I can catch a breath!"
    show shawn surprised
    shawn.say "[hero.name]..."
    shawn.say "Why didn't you tell me you could dance like that?"
    show shawn normal
    bree.say "Like what?"
    "Shawn gives me a knowing look."
    show shawn happy
    shawn.say "Oh come on, [hero.name]..."
    shawn.say "Now you're just trying to be modest!"
    shawn.say "I mean, I'm no expert on the whole dancing thing."
    shawn.say "But even I know that was totally off the charts!"
    show shawn normal
    "I look around, hoping that nobody else heard Shawn while he was gushing."
    "But deep down I'm obviously pretty pleased with the way he's going on about it."
    "Though I still feel like I have to act like it's nothing."
    bree.say "Oh, Shawn..."
    bree.say "That's so nice of you to say."
    bree.say "But don't go on about it too much."
    bree.say "Because I don't like to show off!"
    show shawn normal
    return

label shawn_after_dance_failure_with_female:
    show shawn sad
    "I was hoping that I could impress Shawn with my dancing."
    "Maybe even convince him to come and join me too."
    show shawn embarrassed
    "But every time I get a glimpse of him, he looks annoyed."
    "Like he's getting ever more irritated as time passes."
    "So when I'm done dancing, I walk over to see what's up."
    bree.say "Hey, Shawn..."
    bree.say "Is everything okay?"
    "Shawn doesn't answer me straight away."
    "Instead he leans in and hisses into my ear."
    show shawn sadsmile
    shawn.say "Do you really have to do that?"
    show shawn sad
    "Puzzled I pull back a little."
    "And I can't help shaking my head in confusion."
    bree.say "What are you talking about?"
    bree.say "The dancing?"
    show shawn complain
    shawn.say "If that's what you want to call it."
    shawn.say "I'd have called it an embarrassment!"
    show shawn sad
    "I can't quite believe what I'm hearing."
    "I might not be a trained, professional dancer."
    "But I never thought I was that bad!"
    bree.say "Are you serious?"
    bree.say "You're saying that I embarrassed you?"
    show shawn normal
    shawn.say "Of course you did, [hero.name]..."
    shawn.say "You looked like you were having some kind of fit out there!"
    show shawn normal
    return

label shawn_halloween_invitation_female:
    show shawn
    "Almost the moment I agreed to the Halloween party, I knew who I wanted to invite."
    "Ever since I met him and we started to get closer, I've been trying to work on Shawn."
    "He's so hard to coax out of his shell in social situations, so awkward."
    "But the party should be the perfect chance for him to chill out and socialise."
    "It's happening at the house, which is pretty much a safe space."
    "Well, at least most of the time..."
    "And there's going to be lots of people he knows coming to the party too."
    "So I raise the subject with him the first chance I get."
    bree.say "Shawn..."
    bree.say "What are you doing on Halloween?"
    "Shawn looks up and makes one of those odd, non-committal sounds."
    show shawn talkative at center, zoomAt(1.5, (640, 1040)) with fade
    shawn.say "Hmm..."
    shawn.say "What am I doing on Halloween?"
    shawn.say "Well, I normally stay in."
    shawn.say "With all the lights turned off too!"
    show shawn normal
    "I can't help blinking in genuine surprise."
    bree.say "You do?"
    bree.say "Why is that?"
    show shawn talkative
    shawn.say "The whole holiday's a scam, [hero.name]!"
    shawn.say "It legitimises being extorted in your own home!"
    shawn.say "To it being laid siege by juvenile delinquents!"
    show shawn normal
    bree.say "Are you talking about trick or treaters?"
    show shawn talkative
    shawn.say "The very same!"
    show shawn normal
    bree.say "Erm...okay, Shawn..."
    bree.say "Why not come to my Halloween party instead?"
    bree.say "You know, as my date?"
    if shawn.love >= 100:

        "As soon as I mention the party, Shawn's whole attitude changes."
        "It's like the words flipped a switch in his head."
        "And now he's all sunshine and rainbows."
        show shawn happy
        shawn.say "You want me to come to a party?"
        shawn.say "With you?!?"
        shawn.say "Of course I'll come, [hero.name]!"
        "I can't help smiling as I get the answer I was hoping for."
        "And I try to do the best I can to make sure I seal the deal too."
        bree.say "Awesome!"
        bree.say "The party's at my place on Halloween night."
        bree.say "And it's a costume party too."
        bree.say "So you'd better start thinking about what you're coming as."
        "Shawn nods eagerly."
        shawn.say "Oh, I will, [hero.name]..."
        shawn.say "This is going to be the best Halloween ever."
        shawn.say "I can already feel it!"
        $ game.flags.halloween_girl = "shawn"
    else:

        "As soon as I mention the party, Shawn's attention shifts."
        "Before he seemed to be directing his rage against trick or treaters."
        "But now I can feel it turning in my own direction."
        shawn.say "Is this party happening at your house, [hero.name]?"
        bree.say "Erm..."
        bree.say "Yeah, Shawn..."
        bree.say "Where else would I be having it?"
        "Shawn lets out a triumphant laugh."
        "Like I just revealed a massive secret."
        show shawn sadsmile
        shawn.say "Aha!"
        shawn.say "The same house where my so-called friend [mike.name] just so happens to reside!"
        bree.say "I don't see where this is going, Shawn..."
        bree.say "What's [mike.name] got to do with me inviting you to the party?"
        show shawn complain
        shawn.say "Oh come on, [hero.name]!"
        shawn.say "The same [mike.name] that's been interfering in my private life since we first met?"
        shawn.say "The same [mike.name] that's convinced I'm a social pariah?"
        shawn.say "He asked you to invite me, didn't he?"
        show shawn normal
        bree.say "No, Shawn - I asked you because I kind of like you."
        bree.say "Though I am starting to question that decision a little..."
        show shawn vangry
        shawn.say "Hah!"
        shawn.say "A likely story!"
        shawn.say "You can tell [mike.name] that I'll be at home on Halloween night."
        shawn.say "Keeping quiet in the dark as usual!"
        show shawn angry
        "With that, Shawn turns on his heel and strides away."
        "Leaving me to wonder why I was so set on inviting him in the first place."
    return

label shawn_halloween_arrival_female:
    scene bg house
    "I open the door, eager to see who's out there and what they're wearing."
    show shawn halloween at swing(1.0, 0.8, 1.0, -0.7, 0.6), center, zoomAt(1.05, (640, 930))
    show shawn at swing(1.0, 0.8, 1.0, -0.7, 0.6), center, traveling(1.5, 10.0, (640, 1250))
    "And I'm greeted by the sight of a rotting corpse stumbling towards me!"
    "I take an unconscious step backwards as it's arms reach out."
    "The stiff, claw-like fingers of it's hands grasping the air in front of me."


    shawn.say "Urgh..."


    shawn.say "Urgngh..."
    bree.say "Oh fuck!"
    bree.say "It's actually happening!"
    bree.say "The zombie apocalypse is here!"
    "As soon as the words are out of my mouth, the zombie stops dead in it's tracks."
    "Instead of reaching out to grab me, it adopts a far more relaxed pose."
    "In fact, it even looks kind of pleased with itself!"
    shawn.say "So I take it the costume's pretty decent then?"
    "At the sound of the familiar voice, I squint and look closer."
    bree.say "Shawn?"
    bree.say "Is that really you?"
    shawn.say "Ta da!"
    shawn.say "Pretty good, huh?"
    shawn.say "This took bloody ages to get right."
    shawn.say "And I've already had a couple of people try to kill me on the way over here too..."
    menu:
        "Compliment":
            "I'm still shaking my head in amazement at Shawn's costume."
            "The make-up looks like something straight out of a horror movie."
            bree.say "I can see why, Shawn."
            bree.say "It looks so realistic!"
            "I can see that Shawn's eagerly soaking up the praise."
            "Even under all that make-up he still manages to look smug."
            shawn.say "Yeah, well..."
            shawn.say "I studied special effects at uni, you know?"
            shawn.say "So I'm kind of a whizz at this stuff."
            shawn.say "The electrical store is just something I do to pay the bills."
            "I'm still nodding as I step aside and usher Shawn into the house."
            "And he keeps on talking about it as I close the door behind him."
            "In fact, I'm starting to wonder if he's ever going to shut up about it!"
            "Maybe a beer or two will quieten him down..."
        "Criticise":
            "I can't help frowning at the sight of Shawn under all that make-up."
            "I mean, if he fooled me, then he's going to fool everyone else too."
            "So I can see myself having to make the save over and over again tonight."
            bree.say "It's impressive and all, Shawn..."
            bree.say "But don't you think it's..."
            bree.say "Well, maybe a little much?"
            bree.say "Most people are just going to be in store-bought costumes."
            "Shawn frowns and shakes his head."
            shawn.say "What are you saying, [hero.name]?"
            shawn.say "That I have to come in a shit costume..."
            shawn.say "Just because everyone else had a shit costume?"
            shawn.say "Bollocks to that!"
            "Shawn makes to stride into the hallway."
            "And so I jump to one side, letting him in."
            "He seems pretty pissed at what I just said to him."
            "But maybe a beer or two will settle him down again..."
    scene bg black with dissolve
    $ renpy.pause(1)
    return

label shawn_halloween_party_female:
    $ game.pass_time(2)
    scene bg livingroom
    "I'm just grabbing a refill from the punchbowl for the Shawn and myself."
    "Which means my attention is totally focussed on the cup and ladle."
    "But I can hear the sound of Shawn's voice long before I get back with the drinks."
    shawn.say "Are you taking the piss or what?!?"
    show shawn halloween at right5
    show scottie halloween surprised at left5
    with dissolve
    scottie.say "Whoa..."
    scottie.say "Why are you getting mad with me, dude?"
    scottie.say "I was just trying to be nice!"
    "I arrive on the scene just in time to see Shawn's face turning red with anger."
    "As well as Scottie backing off, a look of total confusion on his face."
    "So I make a point of putting myself between them as I hand Shawn his drink."
    bree.say "Erm..."
    bree.say "What's going on here, guys?"
    scottie.say "Nothing, [hero.name] - I swear!"
    scottie.say "I was just saying that it's cool you invited a homeless guy, that's all!"
    shawn.say "What is the matter with you?"
    shawn.say "Are you hard of hearing or wrong in the head?!?"
    shawn.say "For the last time, I am not a tramp."
    shawn.say "I am dressed as a bloody zombie!"
    bree.say "Wait a minute..."
    bree.say "He thought you were a homeless guy?"
    shawn.say "Apparently so!"
    scottie.say "You mean...he's not?!?"
    menu:
        "Defend Shawn":
            bree.say "No, you total moron - he's not!"
            bree.say "It's just make-up."
            bree.say "He's supposed to be a zombie!"
            "Scottie looks genuinely surprised."
            scottie.say "Oops..."
            scottie.say "Sorry, dude!"
            bree.say "Seriously, Scottie..."
            bree.say "Try growing a brain!"
            show scottie embarrassed
            "Scottie suddenly seems unable to look me in the eye."
            "He turns on his heel and scuttles away a moment later."
            hide scottie with easeoutright
            show shawn at center, zoomAt(1.5, (640, 1040)) with fade
            shawn.say "Seriously, [hero.name]..."
            shawn.say "Can you believe that?"
            show shawn normal
            "I wave a hand in the air, dismissing Shawn's concern."
            bree.say "Ah, forget about him."
            bree.say "The guy's a total idiot."
            bree.say "Let's have ourselves a good time instead."
        "Defend Scottie":
            "No matter how hard I try, I can't keep from laughing."
            bree.say "No, Scottie..."
            bree.say "It's just make-up."
            bree.say "He's supposed to be a zombie!"
            show scottie surprised
            "Scottie looks genuinely surprised."
            scottie.say "Oops..."
            scottie.say "Sorry, dude!"
            "And with that, he scuttles away."
            hide scottie with easeoutright
            shawn.say "I don't see what's so funny, [hero.name]!"
            bree.say "Oh come on, Shawn..."
            bree.say "You have to admit it's pretty funny."
            bree.say "Your make-up's so good and he's such a moron!"
            "Shawn makes a huffing sound."
            shawn.say "Well you are right, [hero.name]."
            shawn.say "But I still don't think it's funny."
    scene bg black with dissolve
    $ renpy.pause(1)
    return

label shawn_halloween_dance_female:
    $ game.pass_time(2)
    scene bg livingroom
    show shawn halloween
    with dissolve
    "As soon as the song I've been waiting for starts, I grab Shawn's hand."
    "And then I begin to pull him towards the dancefloor without waiting for permission."
    "But a moment later I fell him pull in the opposite direction, freeing his hand."
    "As I turn to look at him, Shawn tries to make it look like he didn't just pull away."
    "I mean he actually uses the offending hand to kind of fiddle with his hair."
    "And he only adds to the situation by refusing to look me in the eye too."
    shawn.say "Whoa..."
    shawn.say "What just happened there, [hero.name]?"
    bree.say "Erm..."
    bree.say "I just wanted to dance with you, Shawn..."
    bree.say "That's all, I promise!"
    shawn.say "Ah..."
    shawn.say "Well..."
    shawn.say "You could have, I dunno..."
    shawn.say "Maybe asked me first?"
    menu:
        "Let Shawn off dancing":
            "I realise that I was coming on pretty strong just now."
            "So I hold up my hands in a show of surrender."
            "And I take a step backwards."
            bree.say "Okay, Shawn..."
            bree.say "Point taken."
            bree.say "I'll be back soon!"
            "With that, I turn and head out onto the dancefloor alone."
            shawn.say "[hero.name]..."
            shawn.say "Wait..."
            shawn.say "I didn't say that I didn't want to dance!"
            "I think I hear Shawn trying to say something to me."
            "But I'm already mingling with the other dancers."
            "And so I decide to let it go for the sake of enjoying myself."
            "Whatever it was, I'm sure he can tell me later."
        "Insist that Shawn dance with you":
            "Urgh..."
            "Shawn can be such a stick-in-the-mud sometimes!"
            "Well he's not going to get away with it tonight."
            "This time I grab him by both wrists."
            "And I pretty much fling him onto the dancefloor."
            shawn.say "Aargh!"
            shawn.say "What are you..."
            "Shawn wails and protests just like before."
            "But the difference is that this time, I'm not listening."
            hide shawn
            show dance shawn halloween
            "Soon enough we're both mingling with the other dancers."
            "And he has no choice but to move along with them too."
            "Call me cruel if you like."
            "But I enjoy watching him wriggle and squirm."
            "For once forced out of his comfort zone."
    scene bg black with dissolve
    $ renpy.pause(1)
    return

label shawn_halloween_sex_female:
    scene bg livingroom with dissolve
    "The party's been going a good few hours now, and the atmosphere is better than it's ever been."
    "We're well past the point where I have to worry about things not working out or going wrong."
    "All of the guests seem to be in a good mood, and the general vibe is moving towards chilled."
    "So now would be a good time to sit back and just enjoy the fruits of my labour."
    "But that's when I feel someone tapping me on the shoulder."
    "Taken by surprise, I spin around to see who it could be."
    show shawn halloween
    "And I'm presented with the sight of Shawn, looking more than a little awkward."
    shawn.say "Oh..."
    shawn.say "Hi, [hero.name]..."
    shawn.say "I didn't mean to make you jump!"
    bree.say "It's okay, Shawn."
    bree.say "I was miles away."
    bree.say "Tonight seems to have gone so fast, you know?"
    "Shawn rubs the back of his neck with one hand."
    "And he has an uncomfortable smile on his face."
    "Like he wants to say something, but thinks it might make him look rude."
    shawn.say "Yeah..."
    shawn.say "About that..."
    shawn.say "The party's kind of winding down."
    shawn.say "So..."
    "I think I know exactly what he's going to say next."
    "So I don't hesitate to jump in and fill in the blanks."
    bree.say "Take the chance to hang-out together?"
    bree.say "Just you and me?"
    "Shawn's eyes go wide at this, and his eyebrows rise too."
    shawn.say "Ah..."
    shawn.say "I was going to say you probably want me out from under your feet!"
    shawn.say "Like, you know - want me to go home?"
    shawn.say "But if you want me to stay, that's fine by me!"
    "I can't help blinking and shaking my head at Shawn's words."
    "Is his self-confidence so low he'd really think I want him to leave?"
    bree.say "Of course I want you to stay, Shawn."
    bree.say "I asked you to be my date for the party."
    bree.say "Plus I feel like I've been neglecting you all night."
    bree.say "And now I want to make it up to you..."
    "Without saying another word, I take hold of Shawn's hand."
    scene bg secondfloor
    show shawn halloween
    with fade
    "And then I lead him up the stairs and to the door of my bedroom."
    "He still seems more than a little stunned as I open it and usher him inside."
    scene bg bedroom4
    show shawn halloween
    with fade
    "Like I'm going to stop at any given moment and tell him it's all a joke."
    "I wonder if that's one of the things I like about him?"
    "The way that he's kind of grateful and needy?"
    "And I wonder what that says about me in turn!"
    "Anyway...this is no time for philosophising."
    "I've finally managed to coax Shawn into my room, and we're standing by the bed."
    "Seeing as how he's so easily tongue-tied, I decide to take a more direct approach."
    play sexsfx1 pants_unzip
    "Which is to slowly start stripping off the elements of his costume."
    "Luckily for me, the standard attire for a zombie is basically tattered clothes and rags."
    "So the process doesn't take me too long to complete."
    "All the time I'm undressing him, Shawn stays as still as a statue."
    "Almost as if he's afraid that moving will offend me."
    "Or that all of this is a dream and he'll wake up any moment."
    "Once he's finally naked, I reach out and take hold of his hands."
    "Then I put them on my shoulders, encouraging him to return the favour."
    "At first I think it's not going to work, that I'll have to do it myself."
    "But slowly and surely, Shawn starts to perform the task I've set him."
    "He's tentative at first, fumbling and fiddling."
    "Yet it doesn't take long for his confidence to grow."
    "By the time he's down to my underwear, he's well into his stride."
    "And with the last item of my clothing coming off, he's like a different guy."
    "This version of Shawn is kind of a revelation to me."
    "Because he's the one to take hold of my hand, leading me to the bed."
    "I let him guide me down onto the mattress, intrigued to see where this is going."
    "And I feel a genuine thrill as he climbs atop me, confidence showing in his eyes."
    "The same feelings must be playing out on a physical level for me too."
    "Because I can already feel what's almost like a longing from down there."
    "You know, as if my pussy is intrigued to see where this is going too?"
    "And it looks like I won't have to wait long to find out either."
    "Because a quick glance downwards shows me that Shawn's body is ready too!"
    "The same confidence that saw me laid down on the bed persists in him now."
    "He doesn't wait to ask for permission, and he doesn't need to on my part."
    scene shawn missionary
    show shawn missionary halloween pleasure
    "Because I'm already reaching up for him, pulling him down and onto me."
    "Still Shawn needs to earn it, using the head of his cock to tease and stroke."
    "Each and every time he makes a pass, I hope this will be the one."
    "That this time I'll be able to open up to him."
    "But when it finally happens, everything else fades into the background."
    "Little by little, I feel Shawn sinking into me."
    show shawn missionary halloween vaginal -pleasure opened
    play sexsfx1 slide_in
    "The sensation makes my eyes go wide, my breath catch in my throat."
    "For a moment it seems to do the same to Shawn as well."
    "And the confidence in his manner disappears, replaced by helpless amazement."
    "I think that he's going to lose his stride, to stop dead in his tracks."
    "But luckily for me, he seems to shake it off a few seconds later."
    "The surety returns to his eyes, and he begins to move in earnest."
    play sexsfx1 fuck_calm loop
    "What follows is a blur of sensation and pleasure."
    "Everything that my body cries out for, Shawn manages to give me."
    "It feels like all I have to do is think of it, and he senses my needs."
    "And as his confidence grows, so too does his ability to please me."
    "I can't help thinking that this is the person buried deep inside of him."
    "This is kind of like the ideal version of Shawn that's trying to get out."
    "The one that's buried under some of his quirks and silly hang-ups."
    "Maybe it had something to do with the way in which we're connecting."
    "A deep, physical connection that goes beyond the mundane and normal."
    "Hell, maybe it's just thanks to the fact he can't use his mouth to talk!"
    play sexsfx1 fuck_moderate loop
    show shawn missionary halloween vaginal speed pleasure wide
    "Whatever the reason, I can feel him burning through the last of my energy."
    "And as it ebbs away, my body seems to want to mark the moment."
    "All of a sudden I feel myself starting to cum, helpless to resist."
    "It sweeps over me like a wave, then carries me along with it."
    "I can't tell what effect it's having on my body."
    "But something must be affecting Shawn too, as he's swept along for the ride."
    play sexsfx1 final_thrust
    show shawn missionary halloween vaginal -speed creampie ahegao
    with hpunch
    "The feeling of him losing it inside of me only serves to make it that much more intense."
    "And I swear that the effect on my thoughts doesn't subside as we begin to fall asleep."
    "In fact, I barely feel Shawn as he slides off me and collapses at my side."
    "The urge to sleep is too strong to resist, especially after what we just did together."
    stop sexsfx1 fadeout 1.0
    scene bg black with dissolve
    $ shawn.sexperience += 1
    $ game.pass_time(1)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
