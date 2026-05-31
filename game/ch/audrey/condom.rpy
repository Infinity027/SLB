label audrey_use_condom:
    $ result = randint(1, 5)
    if game.room == "audreybedroom":
        mike.say "Stay right where you are, Audrey."
        "Audrey's eyes are already beginning to glow with anticipation as she waits for what's coming next."
        "But the moment I mention anything other than getting straight down to it, she looks puzzled."
        audrey.say "Huh?"
        audrey.say "What's the matter, [hero.name]?"
        audrey.say "Did I do something wrong?"
        "I'm shaking my head as I climb off the and head towards my bedside table."
        mike.say "Oh, no way, Audrey..."
        mike.say "Just trust me, this won't take a second."
        "With that I hurry over to the pile of my clothes on the floor by the bed."
        "And when I turn back around, she can clearly see that condom I'm holding in my hand."
        audrey.say "Oh yes..."
        audrey.say "That's such a good idea!"
        "I nod my head at the way Audrey's suddenly changed her tune."
        "And I hurry to get back to the bed, as I want to get down to it too."
        "Together we open the packet, putting it on as quickly as we're able."
        "Then we're ready to get started for real."
    elif result == 1 and game.room == "bedroom1":
        "I ignore Audrey's words for a moment, as I reach onto the bedside table."
        "And when she twists her face into an irritated expression, I hold up a condom as way of explanation."
        "She shrugs in response and nods, admitting that I'm in the right for once."
        "And then she lies back and waits, as I put the thing on."
    elif result == 2 and game.room == "bedroom1":
        "And I decide that I'm going to give her just what she wanted, but on my own terms."
        "But that's still no excuse not to take the necessary precautions first."
        "And so, with my free hand, I reach for one of the condoms on the bedside table."
        "If she even notices the time it takes me to do this and put it on, Audrey doesn't say so."
    elif result == 3 and game.room == "bedroom1":
        "I hold up a hand, letting her know that I need her to hold on a second."
        "And then I reach for the bedside table, grabbing a condom."
        "Audrey looks annoyed at the hold-up, but nods all the same."
        "I waste not time in putting it on, eager to get things started."
    elif result == 4 and game.room == "bedroom1":
        "But then something important occurs to me."
        mike.say "Hold on a second, Audrey."
        mike.say "We should really use a condom!"
        audrey.say "Oh shit!"
        audrey.say "You're right, [hero.name]!"
        audrey.say "You've got one, right?"
        "I reach for the bedside table, finding one with relative ease."
        mike.say "There you go, Audrey."
        "Audrey takes the condom and tears it open without hesitation."
        "Then she smooths it down over my cock."
        audrey.say "Okay, we're all set!"
    else:
        "But the one thing I always do is play it safe."
        "And so I hold a hand up to stop Audrey in her tracks."
        "Of course, she instantly looks more than a little annoyed."
        "But then she sees me wave a condom in front of her face."
        "And she nods hastily, urging me to get on with it."
        "All that takes is a couple of seconds, and we're ready to go!"
    return

label audrey_intro_condom:
    $ result = randint(1, 4)
    if result == 1:
        "I push myself forwards, more suddenly and with more force than she could have anticipated."
        "I confess that this is to give her something else to think about."
        "Something other than another round of cutting comments."
    elif result == 2:
        "And I decide that I'm going to give her just what she wanted, but on my own terms."
    elif result == 3:
        "I'm not in the mood to play around here."
        "And from the look on her face, neither is Audrey."
        "So I fix my attention on what's between her legs."
        "And I get ready to dive down there for some action."
    else:
        "I feel Audrey inching forwards, sliding her pussy towards my cock."
        "I can hardly wait until the moment they come together and we can get started."
    return

label audrey_warn_condom:
    $ result = randint(1, 5)
    if result == 1:
        "But before I can get down to business, I hear Audrey speak up all of a sudden."
        audrey.say "Sorry to spoil the mood, [hero.name]."
        audrey.say "But don't you need a little something, down there?"
    elif result == 2:
        "But then Audrey holds up a hand, stopping me in my tracks."
        audrey.say "Slow down there, [hero.name]."
        audrey.say "Aren't you forgetting something?"
    elif result == 3:
        audrey.say "Whoa there, [hero.name]!"
        audrey.say "We almost forgot the condom!"
        "I stop dead in my tracks, realising that Audrey's serious."
        "She won't go a step further until someone whips one out."
    elif result == 4:
        "But just as I'm about to get things moving, Audrey wriggles out from under me."
        mike.say "What the..."
        mike.say "Audrey..."
        mike.say "What are you doing?!?"
        "Audrey points directly at my bobbing cock."
        audrey.say "Just a moment, [hero.name]..."
        audrey.say "We need to use some protection!"
    else:
        "But then Audrey holds up her hand."
        audrey.say "Whoa..."
        audrey.say "We forgot the condom!"
    return

label audrey_force_condom:
    $ result = randint(1, 6)
    if game.room == "audreybedroom":
        "I can't help blinking as I shake my head in surprise."
        "But Audrey seems to be way ahead of me."
        audrey.say "Don't worry..."
        audrey.say "I've got a condom in the drawer of my bedside table."
        "With that she hurries over her side of the bed."
        "And within a few seconds she's holding her prize up for me to see."
        audrey.say "Got it!"
        "I nod as she turns back over, already tearing open the packet."
        "Together we put it on as quickly as we can, and then we're ready to go."
    elif result == 1:
        "Before I can act on her invitation, Audrey wriggles her way out of reach."
        "When my face twists into an irritated expression, she holds up a condom as way of explanation."
        "I shrug in response and nod, admitting that she's in the right on this one."
        "I take the condom, and she lies back and waits as I put the thing on."
    elif result == 2:
        audrey.say "In my purse."
        audrey.say "I think I threw it somewhere near the door!"
        "I hurry to find the condom and then waste no time in putting it on."
        "Then I resume my previous position, taking hold of Audrey's hair as if nothing happened."
    elif result == 3:
        audrey.say "Grab a condom out of my pocket."
        audrey.say "Just there, on the floor by the bed!"
        "I nod grudgingly, accepting that I really should do as I'm told."
        "But I put the thing on as quickly as I can, eager to get back to it."
    elif result == 4:
        audrey.say "Lucky for you, I always come prepared!"
        "Much to my relief, Audrey waves a condom in my face."
        "I nod hastily, grabbing it from her and opening the packet."
        "A couple of seconds later it's on, and we're ready to go!"
    elif result == 5:
        "I can't help blinking as I shake my head in surprise."
        "But Audrey seems to be way ahead of me."
        audrey.say "Don't worry..."
        audrey.say "I've got a condom in my pocket."
        "With that she hurries over to the pile of her clothes on the floor by the bed."
        "And within a few seconds she's holding her prize up for me to see."
        audrey.say "Got it!"
        "I nod as she walks back over, already tearing open the packet."
        "Together we put it on as quickly as we can, and then we're ready to go."
    else:
        audrey.say "Lucky for you, I thought ahead!"
        "Audrey hops off the bed and rummages around in her clothes."
        "Then she gets back into position, the condom in one hand."
        "Audrey takes the condom and tears it open without hesitation."
        "Then she smooths it down over my cock."
        audrey.say "Okay, we're all set!"
    return

label audrey_mad_condom:
    $ result = randint(1, 6)
    if game.room == "audreybedroom":
        "I shake my head, unable to believe what I'm hearing."
        mike.say "You can't be serious?"
        mike.say "A second ago you were practically begging for it!"
        mike.say "Just forget the condom this one time, okay?"
        "Much to my dismay, Audrey takes a step backwards and away from me."
        "And the look on her face tells me that she's less than impressed."
        audrey.say "Oh, [hero.name]!"
        audrey.say "How could you be so thoughtless?!?"
        "I take a stumbling step towards her, trying to explain myself."
        mike.say "No..."
        mike.say "Audrey, wait!"
        "But Audrey's already pointing stubbornly in the direction of her bedroom's door."
        audrey.say "No, [mike.name]..."
        audrey.say "I'm not in the mood anymore."
        audrey.say "So leave me alone please."
        audrey.say "And you can kick yourself out."
        "I'm about to argue, but then I realise it is to late."
        "And once I manage to get enough clothes on to be decent, I leave her apartment."
    elif result == 1:
        audrey.say "But not without protection!"
        "I stop in my tracks, shaking my head in disbelief."
        mike.say "What?!?"
        mike.say "You're getting all preachy and puritanical on me now?"
        "Audrey crosses her arms over her chest, a look of outrage on her face."
        audrey.say "What did you think - that I was going to let you knock me up?"
        audrey.say "You must be fucking crazy!"
        "And with that, she pulls on her clothes and storms out of the room."
    elif result == 2:
        if audrey.flags.nickname == "toy":
            mike.say "Really, little Toy?"
        else:
            mike.say "Really, Audrey?"
        mike.say "I thought you were into the whole danger thing?"
        audrey.say "Yeah, well - I'm certainly not into the whole knocked-up thing!"
        "With that, she slaps my hand away from her hair and climbs off the bed."
        "As she pulls on her clothes, my chances of scoring tonight disappear."
        "Almost as fast as my cock shrinks."
    elif result == 3:
        if audrey.flags.nickname == "toy":
            mike.say "What the hell, Toy?"
        else:
            mike.say "What the hell, Audrey?"
        mike.say "You really want to stop now?"
        audrey.say "[hero.name], you're not putting that thing in me without a condom."
        audrey.say "So it looks like you're not putting it in me at all tonight!"
        "With that, Audrey climbs off of me and starts to get dressed."
        "And all I can do is watch her as she gets ready to leave."
        "All the time cursing myself for not using protection."
    elif result == 4:
        if audrey.flags.nickname == "toy":
            mike.say "Seriously, Toy?"
        else:
            mike.say "Seriously, Audrey?"
        mike.say "I didn't think you were that kind of girl?"
        "Audrey sneers and fixes me with harsh stare."
        audrey.say "What the fuck does that mean?"
        audrey.say "You think I'm some kind of slut?!?"
        mike.say "No..."
        if audrey.flags.nickname == "toy":
            mike.say "Little toy, I..."
        else:
            mike.say "Audrey, I..."
        audrey.say "Oh, shut up."
        audrey.say "I'm out of here!"
        "Audrey shoves me off of her and gets up from the sofa."
        "She dresses in record time, then storms out of my office."
        "Which leaves me alone and even more frustrated than before."
    elif result == 5:
        "I shake my head, unable to believe what I'm hearing."
        mike.say "You can't be serious?"
        mike.say "A second ago you were practically begging for it!"
        mike.say "Just forget the condom this one time, okay?"
        "Much to my dismay, Audrey takes a step backwards and away from me."
        "And the look on her face tells me that she's less than impressed."
        audrey.say "Oh, [mike.name]!"
        audrey.say "How could you be so thoughtless?!?"
        "I take a stumbling step towards her, trying to explain myself."
        mike.say "No..."
        mike.say "Audrey, wait!"
        "But Audrey's already turned her back to me and started to pick up her clothes."
        "Then she starts to put them back on as she heads for my bedroom door."
        audrey.say "No, [mike.name]..."
        audrey.say "I'm not in the mood anymore."
        audrey.say "So I'm going to be heading home."
        audrey.say "And don't worry, I'll see myself out."
        "I'm about to chase after Audrey, but then I realise I'm still naked."
        "And by the time I manage to get enough clothes on to be decent, it's too late."
        "She's long gone and I'm left all alone."
    else:
        mike.say "Forget about that, Audrey."
        mike.say "Let's just do it unprotected this time."
        "Audrey's face falls at the mere mention of the idea."
        "Then she climbs off me and rolls to the edge of the bed."
        audrey.say "I'll tell you something you can forget about, [hero.name]."
        audrey.say "Having sex with me anytime soon!"
        "With that, she starts pulling on her clothes."
        "Leaving me to watch my cock droop with disappointment."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
