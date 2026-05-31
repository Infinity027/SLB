
label master_after_dance_success_with_female:
    show master happy
    master.say "Hey!"
    master.say "Hey there!"
    show master normal
    "I hear the familiar sound of the Master bellowing orders at me."
    "And so I reluctantly stop dancing and walk over to where he's standing."
    "But it's only as I get closer that it becomes clear he's jumping on the spot."
    "That and waving his hands like he's desperate to get my attention."
    bree.say "Erm..."
    bree.say "Is there something wrong, Master?"
    "The Master shakes his head."
    "At the same time he's grinning at me eagerly."
    show master happy
    master.say "No problem, my dear, no problem at all."
    master.say "I'm just happy to see my lessons being put to good use!"
    show master normal
    bree.say "Your lessons?"
    bree.say "What do you mean?"
    show master happy
    master.say "Your dancing, my dear."
    master.say "Why, it could only be so good on account of my teachings!"
    show master normal
    "I feel like asking the old man what in the hell he's talking about."
    "But he just looks so happy right now that it's easier to nod and smile."
    bree.say "Oh..."
    bree.say "Yes, Master..."
    bree.say "I couldn't have done it without you!"
    return

label master_after_dance_failure_with_female:
    show master angry
    master.say "No, no, no!"
    master.say "Come over here, right now!"
    show master upset
    "I hear the familiar sound of the Master bellowing orders at me."
    "And so I reluctantly stop dancing and walk over to where he's standing."
    "But it's only when I do so that I realise he's standing with his arms crossed over his chest."
    "Plus I can see that he has a stern look on his face too."
    bree.say "Erm..."
    bree.say "Is there something wrong, Master?"
    "The Master nods and then points away from where the dancing is going on."
    show master angry
    master.say "As your teacher, I am hereby banning you from dancing."
    master.say "At least until we can teach you to do it properly."
    show master upset
    "I can't quite believe what I'm hearing."
    bree.say "What?"
    bree.say "You can't ban me from dancing!"
    show master angry
    master.say "I can and I am."
    master.say "As my pupil, you reflect upon me."
    master.say "And I will not have people thinking that I have two left feet!"
    show master upset
    "I open my mouth to argue with the old man."
    "But then he does something with his eyebrows and forehead."
    "Somehow making his stare harder than stone."
    "And I feel my will to argue draining away."
    bree.say "Yes, Master..."
    "I hang my head as I do as I'm told."
    "Already feeling totally embarrassed and humiliated."
    show master normal
    return

label master_halloween_invitation_female:
    show master
    "Almost the moment I agreed to the Halloween party, I knew who I wanted to invite."
    "I've spent so long learning the martial arts at the feet of my Master so far."
    "So much so that we've become far more than just master and student."
    "That's why I want to bring him along to the Halloween party as my date."
    "I'm sure he'll have plenty of wisdom to bestow on the actual night."
    "And with his martial arts mastery, he'll be a natural at all the party games too!"
    "So the next time I'm in his presence, I take a deep breath to cleanse myself."
    "Then I let it out and prepare to ask the question."
    "But before I can speak, the Master raises his hand to stop me."
    master.say "Hmm..."
    show master talkative
    master.say "I sense that you have a question, my dear."
    show master normal
    "I wonder just how he can manage to do stuff like that."
    "I mean, a normal human being might have guessed it from my body language or something like that."
    "But in the case of the Master, I'm sure that he must be tapping into my aura or reading my thoughts."
    bree.say "Yes, master..."
    bree.say "Halloween is coming up soon..."
    show master talkative
    master.say "And you are planning to celebrate, yes?"
    show master normal
    "He just did it again!"
    bree.say "Yes, that's it exactly!"
    show master talkative
    master.say "Would your celebrations happen to be taking the form of a party?"
    show master normal
    "Wow...this is getting uncanny!"
    "I mean, I know most people have a party on Halloween."
    "But that doesn't mean he's not using his mystical powers right now."
    bree.say "Right again, master."
    bree.say "And I was going to invite you too."
    bree.say "Would you like to come?"
    bree.say "As my date?"
    if master.love >= 100:

        "I don't have to wait long for an answer."
        "The old man starts nodding eagerly."
        "His head bobbing up and down on his scrawny neck."
        show master talkative
        master.say "Yes, yes..."
        master.say "That sounds like a most agreeable idea."
        master.say "I would be very happy to accompany you, my dear."
        show master normal
        "I can't keep from smiling as I hear the answer I wanted."
        "And pretty soon I'm nodding my head too."
        bree.say "That's great!"
        bree.say "I'll let you know the time and date as soon as I can."
        bree.say "Oh, and one more thing..."
        show master talkative
        master.say "Eh?"
        master.say "What might that be?"
        show master normal
        bree.say "It's a costume party."
        bree.say "So you're going to need to fix yourself up a costume!"
        "The old man looks more than a little perplexed at this news."
        "And I'm worried that it could be enough to make him change his mind."
        bree.say "I could help you pick one out, if you like?"
        "At this, the Master stiffens and shakes his head."
        show master talkative
        master.say "No need, no need..."
        master.say "I will rise to the challenge like I always do!"
        show master normal
        "I nod, deciding to leave the matter well enough alone."
        $ game.flags.halloween_girl = "master"
    else:

        "I don't have to wait long for an answer."
        "The old man starts shaking his head."
        "His head turning from side to side atop his scrawny neck."
        show master talkative
        master.say "No, no..."
        master.say "I couldn't possibly do something like that."
        master.say "I will be spending the time meditating on matters spiritual."
        show master normal
        "I can't keep from frowning as I hear the answer that I didn't want."
        "But that's still not enough to keep me from trying again."
        bree.say "Surely you can spare me a few hours, master?"
        bree.say "The party won't be going on all night."
        "The old man keeps on shaking his head."
        "And he refuses to be moved."
        show master talkative
        master.say "It is not the place of the student to argue with the master."
        master.say "My word should be sufficient for you."
        show master normal
        bree.say "Urgh..."
        bree.say "Yes, master."
        bree.say "I suppose you're right."
    return

label master_halloween_arrival_female:
    scene bg black with dissolve
    pause 0.1
    scene bg house with wiperight
    "I open the door, eager to see who's out there and what they're wearing."
    play sound woosh_punch
    with hpunch
    "And as soon as I open it, I find myself having to duck backwards into the house."
    "Because a wrinkled, green foot passes right in front of my face!"
    master.say "Plowabundle, rube!"
    "Recovering my balance, I take a second look out of the door."
    show master halloween with dissolve
    "I certainly recognise the voice, although I'm not sure what it's saying!"
    "But then I see the familiar face of the Master grinning at me."
    "And I realise that it's green too!"
    "It's only when I see the mask tied over his eyes and the shell on his back that everything makes sense."
    bree.say "Oh, Master..."
    bree.say "You came as a ninja tortoise?"
    "The old man nods his head eagerly."
    show master talkative
    master.say "Of course, my dear."
    master.say "It's the perfect combination."
    master.say "On the one hand, it acknowledges my mastery of the martial arts."
    master.say "And on the other it shows that I'm still hip and with it."
    master.say "That I have my finger on what all the kids think is cool."
    master.say "Isn't that right?"
    show master normal
    menu:
        "Compliment":
            "I have to bite my lip to stop myself giggling."
            "Because the Master's so old and wrinkly already."
            "He kind of looks like a tortoise to begin with!"
            "But somehow I manage to keep myself under control."
            "Which means that I can protect his dignity."
            bree.say "Yes, Master..."
            bree.say "I'm sure everyone will be impressed."
            show master happy
            "This seems to please the old man."
            "And he smiles, secure in his belief that he's still in touch."
            show master talkative
            master.say "Well?"
            master.say "Aren't you going to invite me inside?"
            show master normal
            bree.say "Oh..."
            bree.say "Of course!"
            "I step aside and usher him inside the house."
            "All the time trying not to laugh at the sight of him."
            "Though I have no idea if the other guests will be as kind."
        "Criticise":
            "I'm doing the best I can to keep from laughing."
            "Because the truth is that the Master looks pretty funny."
            "I mean sure, the idea of him dressing as a ninja tortoise is silly enough."
            "But the fact he's so old and wrinkly just makes him look even more like real tortoise!"
            bree.say "Are you sure anyone's going to notice that you dressed up, Master?"
            show master surprised
            master.say "Eh?"
            master.say "What do you mean?"
            show master stuned
            bree.say "Well..."
            bree.say "You pretty much look like a tortoise most of the time!"
            show master upset
            "The old man frowns and stamps his foot on the ground."
            show master angry
            master.say "Hah!"
            master.say "Look this good when you are eighty, you will not!"
            master.say "And are you forgetting that I painted myself green?!?"
            show master upset
            "The Master barges past me and into the house, still muttering under his breath."
            "I do the best I can to close the door behind him and follow on his heels."
            "But the truth is that I'm almost doubled over with laughter."
            "I know that I'll have to try and make it up to him soon."
            "Just not right now, as I can't stop giggling at him!"
    scene bg black with dissolve
    $ renpy.pause(1)
    return

label master_halloween_party_female:
    $ game.pass_time(2)
    scene bg livingroom
    show master halloween at right5
    show jack halloween embarrassed at left5
    with dissolve
    "I'm just grabbing a refill from the punchbowl for the Master and myself."
    "Which means my attention is totally focussed on the cup and ladle."
    "But I can hear the altercation going on long before I get back with the drinks."
    "And as I do the source of all the noise becomes painfully apparent."
    "Jack's pretty much cowering away from the Master."
    "All while the older man pokes him in his not inconsiderable belly!"
    master.say "Hmm..."
    show master talkative
    master.say "You're a very doughy young man."
    master.say "You could use some toughening up!"
    show master whining
    jack.say "Ouch!"
    jack.say "Hey..."
    jack.say "Stop it..."
    show jack annoyed
    "Jack looks around, obviously searching for help."
    show jack normal
    "And that's when his gaze settled on me."
    show master whining
    jack.say "[hero.name]..."
    jack.say "Save me!"
    show jack sadsmile
    "I put the drinks down and then walk over."
    "At the sight of me, the Master stops prodding Jack."
    "And his hapless victim retreats, putting be between them."
    bree.say "What's going on here?"
    show jack worried
    jack.say "Your crazy old boyfriend attacked me!"
    show jack annoyed
    show master talkative
    master.say "Nonsense!"
    master.say "I was just showing this young man how fat and slow he is."
    master.say "He could really stand to lose some of that blubber!"
    show master normal
    menu:
        "Defend the Master":
            "I have to admit that the old man's not wrong."
            "Jack's more than a little pudgy!"
            "And he's way too thin-skinned too."
            show jack surprised
            bree.say "Lighten up, Jack."
            bree.say "Oops..."
            bree.say "I meant your mood, not your weight!"
            show jack embarrassed
            show master happy
            "The Master cackles with laughter."
            "Nodding his head atop his thin neck as he does so."
            show master talkative
            master.say "Oh my goodness..."
            master.say "That's a funny..."
            master.say "Because of how fat he is!"
            show master normal at center
            hide jack
            with easeoutleft
            "Jack shakes his head and turns to walk away."
            "But I don't really see him go."
            "As I'm too busy laughing."
            bree.say "Oh dear..."
            bree.say "I think we offended him."
            show master talkative
            master.say "No need to worry, my dear."
            master.say "He's headed in the direction of the buffet."
            master.say "No doubt he will find comfort there!"
            show master normal
        "Defend Jack":
            "I have to admit that the old man's not wrong."
            "Jack's more than a little pudgy!"
            "But that doesn't mean it's okay to mock him."
            bree.say "You shouldn't do that, Master."
            bree.say "It's called 'fat-shaming'."
            bree.say "And it's not very nice."
            show master stuned
            "The Master looks more than a little confused."
            "But Jack takes the chance to lean around me and tell him off."
            show jack worried
            jack.say "You heard her, you crazy old coot!"
            jack.say "It's not nice."
            show jack normal
            "The Master shakes his head as Jack scuttles off."
            show master talkative
            master.say "I don't understand, my dear."
            master.say "I was simply telling the truth."
            master.say "That boy is quite fat!"
            show master normal
            bree.say "He is, Master."
            bree.say "But sometimes the truth can be hurtful."
            bree.say "And remember, this isn't one of your lessons."
            bree.say "It's a party, and it's supposed to be fun."
            "The old man nods and accepts his drink."
            "He looks thoughtful, and I hope that I've given him food for thought."
            "Rather than just offending him."
    scene bg black with dissolve
    $ renpy.pause(1)
    return

label master_halloween_dance_female:
    $ game.pass_time(2)
    scene bg livingroom
    show master halloween
    with dissolve
    "As soon as the song I've been waiting for starts, I grab the Master's hand."
    with hpunch
    "And then I begin to pull him towards the dancefloor without waiting for permission."
    "But a moment later, I hear him protesting and crying out in pain."
    show master whining
    master.say "Oooh!"
    master.say "Ouch..."
    master.say "The pain, the pain!"
    show master sad
    "I turn around to see the old man almost on his knees before me."
    "Making it look like the grip I have on him is crippling him."
    bree.say "Erm..."
    bree.say "I only wanted to dance!"
    show master whining
    master.say "You must respect the age of my body, my dear."
    master.say "I didn't get to be this old by leaping up to dance at a second's notice!"
    show master sad
    menu:
        "Respect the Master's age":
            "I narrow my eyes a little as I listen to his excuse."
            "Not least because I remember all of the lessons he's given me."
            "And the way he leaps into action at the prospect of indulging himself too!"
            "But the last thing that I want is to have him break a hip."
            "Plus it'd look really bad for me to be seen dragging an old man around the place."
            bree.say "Of course, master."
            bree.say "I'll go and dance by myself."
            "The old man opens his mouth to say something."
            "But I don't hear it as I'm already on my way to the dancefloor."
            "All the while I'm up there, I see him struggling to watch."
            "Probably regretting the fact he refused to come dance too."
            "What with all of the young, female bodies bobbing around."
            "Well, he only has himself to blame for that!"
        "Call the Master's bluff":
            "Is the old duffer for real?!?"
            "He's always showing off his moves in our lessons."
            "Plus he boasts about his physical prowess all the time!"
            "Determined to call him out, I tighten my grip on his hand."
            hide master
            show dance master halloween
            with hpunch
            "And then I pull him bodily onto the dancefloor."
            master.say "Argh..."
            master.say "What are you doing?"
            master.say "Unhand me this instant, do you hear?"
            master.say "Oh..."
            master.say "Oh my..."
            master.say "So many female bodies, moving in such intriguing ways!"
            "Before too long, the Master seems to forget all about his misgivings."
            "And instead he spends his time moving in vague time with the music."
            "All while his eyes almost pop out of his head at the sights which surround him."
    scene bg black with dissolve
    $ renpy.pause(1)
    return

label master_halloween_sex_female:
    scene bg livingroom with fade
    "The party's been going a good few hours now, and the atmosphere is better than it's ever been."
    "We're well past the point where I have to worry about things not working out or going wrong."
    "All of the guests seem to be in a good mood, and the general vibe is moving towards chilled."
    "So now would be a good time to sit back and just enjoy the fruits of my labour."
    show master halloween with dissolve
    "And that's when I spot the Master, still hovering around the table with the food on it."
    "Most of the plates have been picked over, but that's not stopping him."
    "As he seems determined to polish off the last morsels of everything."
    bree.say "Erm..."
    bree.say "Are you really still hungry?"
    bree.say "Because I could order a pizza or something?"
    show master stuned
    "The old man jumps a little at the sound of my voice."
    "And he spins around, hiding his plate behind his back."
    show master surprised
    master.say "Eh..."
    master.say "What..."
    show master talkative
    master.say "Oh no, no need for that."
    master.say "My diet is a matter of precise balance and the purest of foods."
    master.say "I assure you that I'm totally free from the burden of hunger."
    show master normal
    "I can't help raising an eyebrow at this."
    "As I swear I saw him eating all sorts of junk earlier in the night."
    "But I decide to leave it alone for the sake of keeping the peace."
    "Not least because I think I just figured out what I need to round out the night."
    "The perfect thing to use up the last of my energy and help me to sleep as well."
    bree.say "Whatever you say, Master."
    bree.say "Perhaps you'd like to come see where I meditate around here?"
    bree.say "The sanctuary that I've made for myself to be able to practice your teachings?"
    "The Master doesn't seem overly enthused with the notion."
    "In fact he appears to be more interested in checking out the other female party-goers."
    "But when I hold out my hand for him to take it, he realises that he doesn't have a choice."
    show master talkative
    master.say "Very well, my dear..."
    master.say "If you insist."
    master.say "But once you've seen one of those things, you've seen them all!"
    show master normal
    "The Master keeps on muttering and complaining under his breath."
    scene bg secondfloor
    show master halloween
    with fade
    "But I just ignore him as I lead the way upstairs and to my bedroom."
    "And I can see his expression changing as we get closer to our destination."
    scene bg bedroom4
    show master halloween
    with fade
    "Opening the door, I usher him inside, then close it behind us."
    "Turning the catch on the lock, I turn around to see him inspecting the room."
    show master talkative
    master.say "So this is where you masturbate..."
    master.say "Erm...I mean meditate!"
    master.say "Very impressive indeed."
    show master normal
    bree.say "Oh, it's nothing special, Master."
    bree.say "But it is my little sanctuary away from the chaos of modern life."
    "I say all of this as I'm walking over to the bed."
    "And once I'm sitting down on it, I pat the mattress at my side."
    "The Master doesn't need any more invitation than that."
    "He instantly scuttles across the room and sits down beside me."
    show master talkative
    master.say "So..."
    master.say "What kind of techniques have you been practising?"
    show master normal
    bree.say "Well, Master..."
    bree.say "Let me give you a little demonstration."
    "With that, I turn and push hard on the Master's shoulders."
    "And for all of his supposed martial arts skills, he's taken by complete surprise."
    "The Master falls backwards onto the bed, letting me pounce on him a moment later."
    "He doesn't even have the time to say a single word before I'm pulling off his costume."
    "In fact he seems to be helpless to stop me doing whatever I want."
    show master talkative
    master.say "Oh..."
    master.say "I...I recognise this technique..."
    master.say "It's very...very effective!"
    show master normal

    scene bg black
    show master cowgirl halloween
    with fade

    "And I use my weight to pin him down."
    "By the time I'm done, he's as hard as a rock, standing to attention before me."
    "So I don't hesitate to reach out and grab hold of his cock."
    show master cowgirl halloween at startle(0.05, -10)
    "He gasps and lets out a moan as I push it between my thighs."
    "But I note that he's nodding desperately the whole time."
    show master cowgirl halloween at startle(0.05, -10)
    "And his head begins to bob even faster as I lower myself onto him."
    "The Master seems to be happy to let me do most of the work."
    "Which means that I'm also going to be the one taking the lead too."
    "Raising and lowering myself, I stroke his cock against my pussy."
    "And with every repetition, I feel myself loosening just a little."
    "That is until the moment something inside of me sees fit to relax."
    "Not a lot, but just enough."
    "That's the moment that I press down with all of my weight."
    "That little opening begins to grow as the head of his cock enters it."
    "And the momentum starts to build from there, growing all the time."
    "Inch by inch, I sink downwards as he slides into me."
    "And once he's all the way in, I lean back and enjoy the sensation."
    "The Master seems to be frozen beneath me."
    "His face a mask of helpless pleasure."
    "I know that I could stay like this for the longest time."
    "Just enjoying the feeling of it and seeing how much he can take."
    show master cowgirl halloween at startle(0.05, -10)
    pause 0.2
    show master cowgirl halloween at startle(0.05, -10)
    "But I can already feel my body beginning to move."
    "As though it were an unconscious thing, I start to ride him."
    show master cowgirl halloween at startle(0.05, -10)
    pause 0.2
    show master cowgirl halloween at startle(0.05, -10)
    "Slowly at first, and then ever faster as the sensations build."
    "Before I even know it, I'm in full motion."
    show master cowgirl halloween at startle(0.05, -10)
    pause 0.2
    show master cowgirl halloween at startle(0.05, -10)
    "My buttocks are all but slamming down onto him."
    "Almost like I'm trying to drive him through the mattress."
    "All the while, the Master remains unmoving beneath me."
    show master cowgirl halloween at startle(0.05, -10)
    pause 0.2
    show master cowgirl halloween at startle(0.05, -10)
    "His eyes are wide open and glassy, staring up at the ceiling."
    "But I can hardly spare a moment to think about him or anything else."
    "The only thing that matters to me is seeing it through to the end."
    show master cowgirl halloween at startle(0.05, -10)
    pause 0.2
    show master cowgirl halloween at startle(0.05, -10)
    "This level of distraction means that my orgasm takes me by surprise."
    "It hits out of nowhere, doubling me over with irresistible pleasure."
    with vpunch
    "I'm pressing down so hard on the Master that he's swept along with me."
    with vpunch
    "And I feel him explode inside of me a moment later."
    with vpunch
    "I all but fall off of him, rolling around on the bed until it's over."
    "Afterwards I have to hold a mirror over his mouth to check that he's still breathing."
    "And that done, I finally feel able to lie down and sleep too."
    $ master.sexperience += 1
    $ game.pass_time(1)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
