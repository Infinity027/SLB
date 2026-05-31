label shawn_use_condom:
    $ result = randint(0, 3)
    if result == 0:
        "But then I remember that there's something else we needed to do."
        "Something that's essential to take care of before we get down to it."
        bree.say "Wait a second..."
        bree.say "I need to grab something!"
        "Shawn looks at me in amazement and I wriggle out from under him."
        shawn.say "Huh?"
        shawn.say "What's the matter?"
        "But when he sees me returning with a condom, he nods eagerly."
        shawn.say "Oh yeah..."
        shawn.say "Good call, [hero.name]!"
        "All it takes is a couple of seconds to fumble around down there."
        "Then we're all ready to go."

    elif result == 1:
        "I almost ignore Shawn's complaints, as something else had occurred to me."
        "And it's enough to make me swing my leg back over him and hop off the bed."
        bree.say "Hold that thought, Shawn..."
        bree.say "I just remembered something important."
        "Shawn looks at me in total surprise."
        "Like he's expecting me to leap out of the window or something crazy like that."
        shawn.say "Huh?"
        shawn.say "What are you talking about, [hero.name]?"
        "By way of an answer, I hold up what I was looking for."
        "And the moment he sees it, recognition is visible in Shawn's eyes."
        shawn.say "A condom?"
        shawn.say "Oh right...I see!"
        "All it takes is a minute to open the packet and get it on."
        "Then I'm back in position and we're the ones ready to get it on!"

    elif result == 2:
        "It seems like Shawn's ready for it too."
        "As I feel him stir the moment I make my move."
        "But there's just one thing I need to handle first."
        bree.say "Just a second, Shawn..."
        bree.say "We need to put something on."
        "Shawn looks puzzled, glancing at the clothes we already stripped off."
        shawn.say "What's that, [hero.name]?"
        shawn.say "I thought the idea was to take stuff off..."
        shawn.say "Not to put it back on again!"
        "I chuckle and shake my head as I slip off the bed."
        bree.say "I mean a condom, silly!"
        bree.say "Got one right here..."
        "Shawn looks relieved as I grab the condom and tear open the packet."
        "Then he holds still as I slide it onto his waiting manhood."
        "That done, I hop back onto the bed and onto all-fours."
    else:

        "But it's just as he's beginning to get hot that I remember something."
        "Something so important that I put things on hold while I handle it."
        "Which involves letting go of Shawn's cock and leaping off the bed."
        "As I do so, Shawn sits up, a look of genuine surprise on his face."
        shawn.say "Erm..."
        shawn.say "[hero.name]..."
        shawn.say "Is there something wrong?"
        "I don't bother to turn my head as I answer the question."
        "Instead I just keep on searching to make things quicker."
        bree.say "Nothing's wrong, Shawn..."
        bree.say "I just remembered we needed one of these!"
        "I turn around and begin to make my way back to the bed."
        "And I make sure to hold up the condom in my hand for him to see."
        "Thankfully this turns the look of surprise into one of understanding."
        "Which means that I only have to hop back into position and tear open the package."
        "After that it takes a couple of seconds to het get everything sorted."
        "And then we're all good to go."
    return









label shawn_warn_condom:
    $ result = randint(0, 3)
    if result == 0:
        "But then Shawn seems to remember something."
        "And he starts to climb off the bed."
        bree.say "Huh?"
        bree.say "Where are you going?"
        shawn.say "We need a condom, [hero.name]!"

    elif result == 1:
        "At first I think that Shawn's just joking around."
        "But then I see he's looking pretty serious."
        shawn.say "[hero.name]..."
        shawn.say "You just reminded me..."
        shawn.say "We really should use a condom!"

    elif result == 2:
        "I'm expecting Shawn to leap straight into action."
        "But to my surprise, he seems to be holding back."
        "So much so that I find myself bumping my ass into him."
        "As well as looking back over my shoulder to see what's up."
        bree.say "Shawn..."
        bree.say "What gives?"
        bree.say "I thought you were well up for this?"
        "Shawn shakes his head."
    else:

        "But then I hear something that I wasn't expecting."
        "And definitely something I never thought I'd hear from Shawn."
        shawn.say "Erm..."
        shawn.say "[hero.name]..."
        shawn.say "We need to stop!"
        bree.say "Huh?"
        bree.say "What are you talking about, Shawn?!?"
        shawn.say "Don't panic, okay?"
        shawn.say "I just remembered that we should use a condom, that's all."
    return

label shawn_force_condom:
    $ result = randint(0, 3)
    if result == 0:
        "I watch as Shawn quickly retrieves a condom from his pocket."
        "Then he climbs back onto the bed, handing it to me."
        "All it takes is a couple of seconds to fumble around down there."
        "Then we're all ready to go."

    elif result == 1:
        "I'm about to speak up when Shawn ushers me off his lap."
        "And then he hops off the bed, heading to his discarded pants."
        shawn.say "Don't worry, [hero.name]..."
        shawn.say "I got one right here."
        "Shawn holds up the condom for me to see."
        "All it takes is a minute to open the packet and get it on."
        "Then I'm back in position and we're the ones ready to get it on!"

    elif result == 2:
        shawn.say "Oh, I'm up for it, [hero.name]..."
        shawn.say "We just need to use some protection, that's all."
        "I watch as Shawn hops neatly off the bed and retrieves the condom."
        "Her hands it to me, and I tear open the packet."
        "Then he holds still as I slide it onto his waiting manhood."
        "That done, I hop back onto the bed and onto all-fours."
    else:

        "I blink in amazement as Shawn slides out from under me."
        "And then I watch as he walks over to his clothes."
        "It only takes him a moment to rummage through the pockets of his pants."
        "Then he's on his way back to me, holding up the condom for me to see."
        "As soon as he gets back into position, he hands it to me."
        "And then I eagerly tear open the package."
        "After that it takes a couple of seconds to het get everything sorted."
        "And then we're all good to go."
    return

label shawn_mad_condom:
    show shawn angry at center, zoomAt(1.5, (640, 1040)) with fade
    $ result = randint(0, 3)
    if result == 0:
        "I can't actually believe what I'm hearing right now."
        bree.say "Are you kidding me?"
        bree.say "Forget the damn condom, Shawn..."
        bree.say "Just get on with it already!"
        "Shawn looks at me like I'm crazy."
        "Then he shakes his head and starts to pick up his clothes."
        shawn.say "What the hell, [hero.name]?"
        shawn.say "You think I'm desperate enough to do something stupid?"
        shawn.say "I'm not having sex without protection!"
        "After that there's nothing I can do to talk him round."
        "Shawn just puts on his clothes and lets himself out."
        "Leaving me alone and frustrated on the bed."
        "Not to mention feeling like a total idiot too."

    elif result == 1:
        "For some reason my head's just not processing what Shawn's saying."
        "And all I can see his words as are a barrier to me getting what I want."
        bree.say "Forget the condom, Shawn..."
        bree.say "Just make with the cock!"
        "Shawn looks horrified at this, and instantly ushers me off his lap."
        "Then I'm forced to watch as he starts to get dressed."
        shawn.say "Really, [hero.name]..."
        shawn.say "I thought you were smarter than that."
        shawn.say "And don't try to stop me either..."
        shawn.say "Because you've totally killed the mood!"
        "All I can do is watch in helpless silence as Shawn walks out the door."
        "Leaving me alone and frustrated, all for the sake of a single, lousy condom."

    elif result == 2:
        shawn.say "Oh, I'm up for it, [hero.name]..."
        shawn.say "We just need to use some protection, that's all."
        "He looks at me while he's saying all of this."
        "And I get the impression he's expecting me to produce one."
        "Like I can magic the thing out of thin air somehow!"
        bree.say "Oh come on, Shawn..."
        bree.say "Just forget about it this once, yeah?"
        bree.say "Let's live dangerously!"
        "Shawn's face drops as soon as the words are out of my mouth."
        "And I swear his cock starts to droop in the same moment too."
        "I watch as he gets off the bed and begins to get dressed."
        shawn.say "Sorry, [hero.name]..."
        shawn.say "You just killed the mood for me."
        shawn.say "Let's try this again another time."
        shawn.say "Maybe when you've not lost your mind?"
        "I'm left utterly speechless and unable to respond."
        "All I can do is watch as Shawn finishes dressing and walks out of my bedroom."
        "And I guess he's right, I must have lost my mind."
        "Because I just blew a sure thing, and now I'm not getting any tonight."
    else:

        "I look at Shawn like he's not making any sense."
        "And then I let out a snort of laughter and shake my head."
        bree.say "Are you serious?"
        bree.say "You total and utter nerd!"
        bree.say "Like you're gonna turn down actual sex with a girl?!?"
        bree.say "I don't think so!"
        "A moment later the look of amusement on my face disappears."
        "And it's replaced with one of genuine amazement."
        "Because Shawn literally pushes me off of him."
        "I land in a tangled heap on the bed as he leaps up."
        "And I'm forced to watch in shocked silence as he gets dressed."
        shawn.say "You can call me a nerd all you like, [hero.name]..."
        shawn.say "You think I never heard that before?"
        shawn.say "But one thing you're never going to make me do is be that stupid!"
        "With that, Shawn turns his back on me and lets himself out of my room."
        "Which leaves me sprawled out on the bed, still hardly able to believe what just happened."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
