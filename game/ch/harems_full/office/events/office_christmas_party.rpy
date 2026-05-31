








init python:
    Event(**{
    "name": "christmas_invite",
    "label": "office_christmas_intro",
    "conditions": [
        IsDone("office_party"),
        IsNotDone("christmas_invite"),
        'game.calendar.get_future_previous_day_of_week(game.calendar.get_future_days_played("christmaseve"), "friday", force_previous_if_today=True) - 7 <= game.days_played < game.calendar.get_future_previous_day_of_week(game.calendar.get_future_days_played("christmaseve"), "friday", force_previous_if_today=True) - 1',
        HeroTarget(
            HasRoomTag("work"),
            IsFlag("fired", False),
            IsFlag("suspended", False),
            Or(
                IsFlag("isceo"),
                IsFlag("dwaynedead", False),
                ),
            ),
        PersonTarget(aletta,
            Not(IsHidden()),
            ),
        PersonTarget(audrey,
            Not(IsHidden()),
            ),
        PersonTarget(shiori,
            Not(IsHidden()),
            ),
        PersonTarget(lavish,
            Not(IsHidden()),
            ),
        PersonTarget(cassidy,
            Not(IsHidden()),
            ),
        ],
    "duration": 1,
    "do_once": False,
    "once_hour": False,
    "once_year": True,
    })

    Event(**{
    "name": "office_christmas_cancelled",
    "label": "office_christmas_cancelled",
    "conditions": [
        IsDone("christmas_invite"),
        HeroTarget(
            IsFlag("isceo", False),
            Or(
                IsFlag("fired"),
                IsFlag("suspended"),
                IsFlag("dwaynedead"),
                ),
            ),
        'game.days_played < game.calendar.get_future_previous_day_of_week(game.calendar.get_future_days_played("christmaseve"), "friday", force_previous_if_today=True)',
        ],
    "duration": 1,
    "do_once": False,
    })


label office_christmas_intro:
    if hero.flags.isceo or game.flags.dwaynedead:
        scene bg office
        show aletta work
        "With Aletta walking at my side, I stride into the office where I used to work."
        "I'm still not used to coming here in my new role as CEO of the entire company."
        "It feels like I should be going back to my old desk and just getting on with it."
        hide aletta
        show shiori work at left
        show audrey work at center
        show lavish work at right
        "And it gets strangers still when I see how my old colleagues respond to the sight of me."
        "One by one, Audrey, Lavish and Shiori look up from their work."
        show shiori surprised
        show audrey surprised
        show lavish surprised
        "Then their eyes go wide as they realise that the big boss just walked in."
        "They seem to be adjusting to the change in status between us pretty well."
        "So why is it so hard for me to do the same?"
        hide lavish
        hide shiori
        hide audrey
        show aletta work angry
        aletta.say "Ahem..."
        aletta.say "Could I have your attention please?"
        show aletta normal
        aletta.say "Mister [hero.family_name] has an announcement to make."
        "All eyes are suddenly on Aletta."
        "And I have to admit I admire her ability to phrase a demand as a question!"
        "Well used to being summoned by Aletta, the girls all get to their feet."
        hide aletta
        show shiori work at left
        show audrey work at center
        show lavish work at right
        "And once they're assembled before me, I guess it's my turn to speak."
        mike.say "Ah...hello..."
        mike.say "Just a quick visit to say we'll be closing the office early next Friday."
        "Instantly they girls begin glancing at each other."
        show shiori happy
        show audrey flirt
        show lavish happy
        "And a chatter of eager conversation spreads between them."
        "Oh shit!"
        "I see what's happening here."
        "They think I'm giving them the afternoon off!"
        "I can't blame them - it's what I would have assumed in their position too!"
        mike.say "Erm...closing it because we'll be having an office Christmas party!"
        show lavish normal
        show shiori embarrassed
        show audrey happy
        "Suddenly the delight turns to surprise."
        "Shiori looks worried and disappointed."
        "Lavish manages to keep her face pretty much neutral."
        "Audrey, in contrast, seems delighted."
        hide lavish
        hide shiori
        hide audrey
        show aletta work
        "I glance at Aletta, and she just shrugs."
        mike.say "Well..."
        hide aletta
        show shiori work embarrassed at left
        show audrey work happy at center
        show lavish work normal at right
        mike.say "Attendance isn't mandatory, I guess..."
        mike.say "But it'd be great if you could come along!"
        "I force a smile onto my face, hoping that I'm coming across as a good boss."
        "But inside I can't help feeling like I just died a little."
        "I was always the guy at the back of the office in this situation."
        "The one that muttered and rolled his eyes when the boss tried to be cool."
        "Now I just hope my underlings don't think the same of me!"
        "But I can already see that most of them think they have to come."
        show shiori work at left
        hide audrey
        show lavish work at right
        show aletta work happy at center
        "Aletta comes to my rescue."
        "She claps her hands and nods with authority."
        aletta.say "Well, I suppose that's official then."
        show aletta normal
        aletta.say "See you all at the party next week."
        hide aletta
        show shiori sad
        shiori.say "Ooh..."
        shiori.say "I hope I can find a babysitter for Kanta!"
        lavish.say "I was planning to work that afternoon anyway."
        lavish.say "So it's no big deal."
        show audrey work happy
        audrey.say "Geez - cheer up, you sad-sacks!"
        show audrey flirt
        audrey.say "Don't you know how much fun an office party can be?"
        audrey.say "Food, booze and plenty of dark corners to misbehave in!"
        "I keep on smiling, trying not to listen to what they all have to say."
        "Dwayne wouldn't have felt like this."
        "He'd have just strolled in and laid down the law."
        "But then I remember that Dwayne's dead."
        "And now I'm the guy trying to fill his shoes!"
    else:
        scene bg personal
        "I hear the sound of voices in the middle of the office."
        "And for once it doesn't sound like idle gossip either."
        "So I get up from my desk and drift over to see what's going on."
        scene bg office
        show lavish work at mostleft4
        show aletta work at mostright5
        show shiori work embarrassed at right4
        show audrey work annoyed at left4
        "I'm met by the sight of everyone congregating together."
        "I nod to Audrey, Lavish and Shiori."
        "But then I notice that Aletta's here too."
        hide lavish
        hide shiori
        hide audrey
        hide aletta
        show dwayne
        "And standing in the middle of it all is Dwayne."
        "So the big man's descended from his ivory tower to mix with the plebs!"
        "I wonder what the hell all of this is about?"
        show dwayne at left
        show aletta work angry at right
        aletta.say "Quiet down, all of you!"
        aletta.say "Mister Big has an announcement to make."
        dwayne.say "Thank you, Aletta."
        show aletta annoyed
        dwayne.say "But I can handle it from here!"
        "Aletta looks a little mollified."
        hide aletta
        show dwayne at center
        "But she nods and takes a step back all the same."
        dwayne.say "Don't worry guys, it's nothing sinister."
        dwayne.say "Quite the opposite, actually!"
        dwayne.say "We're going to be closing the office early next Friday."
        hide dwayne
        show lavish work at left
        show audrey work at center
        show shiori work at right
        "A ripple of delight spreads through everyone present."
        "Of course it does."
        "Who wouldn't want to get off work early during the festive season!"
        dwayne.say "And that's because we'll be throwing an office party!"
        show lavish surprised
        show audrey surprised
        show shiori surprised
        "Suddenly the delight turns to surprise."
        show lavish normal
        show audrey happy
        show shiori sad
        "Shiori looks worried and disappointed."
        "Lavish manages to keep her face pretty much neutral."
        "Audrey, in contrast, seems delighted."
        hide lavish
        hide audrey
        hide shiori
        show aletta work
        "I glance at Aletta, and she just shrugs."
        hide aletta
        show dwayne
        dwayne.say "Of course, attendance isn't mandatory."
        dwayne.say "I'm your boss, not your jailer."
        dwayne.say "But I do like to think that I'm a cool kind of guy."
        dwayne.say "The kind that you'd all like to party with, yeah?"
        "Urgh..."
        "I don't need somebody else to translate that one for me!"
        "Dwayne basically means that he can't force any of us to attend."
        "But he'll count it as a black mark against us if we go home instead!"
        "Dwayne underlines the point with one of his trademark grins."
        "And he makes me cringe by giving us a double thumbs-up to seal the deal."
        hide dwayne
        "With that, Dwayne turns and strides out of the office."
        show aletta work annoyed
        aletta.say "Well, I suppose that's official then."
        aletta.say "See you all at the party next week."
        hide aletta
        show lavish work at left
        show audrey work happy at center
        show shiori work sad at right
        shiori.say "Ooh..."
        shiori.say "I hope I can find a babysitter for Kanta!"
        lavish.say "I was planning to work that afternoon anyway."
        lavish.say "So it's no big deal."
        audrey.say "Geez - cheer up, you sad-sacks!"
        show audrey flirt
        audrey.say "Don't you know how much fun an office party can be?"
        audrey.say "Food, booze and plenty of dark corners to misbehave in!"
        "I laugh and shake my head."
        mike.say "I have a bad feeling about this!"
    $ renpy.dynamic("officechristmas", "appointment")
    $ officechristmas = game.calendar.get_future_previous_day_of_week(game.calendar.get_future_days_played("christmaseve"), "friday", force_previous_if_today=True)
    $ appointment = LabelAppointment((14, 18), ["aletta", "audrey", "cassidy", "lavish", "shiori"], "Office Christmas Party", "office_christmas_arrival", "office_christmas_missed")
    $ hero.calendar.add(officechristmas, appointment)
    $ game.notify("{image=gui/icons/icon_reminder.png}" + str(appointment.format(officechristmas)))
    return

label office_christmas_missed:
    "Shit, I missed the Christmas office party. Aletta is going to be mad."
    $ aletta.love -= 4
    call office_christmas_reset from _call_office_christmas_reset_1
    return

label office_christmas_cancelled:
    if game.flags.fired:
        "I don't work in the office anymore. I suppose."
    elif game.flags.suspended:
        "I've been suspended from work. No Christmas party for me this year."
    elif game.flags.dwaynedead:
        "Dwayne's dead. I guess there won't be a Christmas party this year."
    call office_christmas_reset from _call_office_christmas_reset_2
    $ hero.calendar.find_and_remove(label="office_christmas_arrival")
    return


label office_christmas_arrival(appointment=None):
    if renpy.has_label("christmas_achievement_2") and not game.flags.cheat:
        call christmas_achievement_2 from _call_christmas_achievement_2
    play music "music/roa_music/santas_nice_list.ogg" loop fadeout .5 fadein .5
    if not Room.has_tag(game.room, "work"):
        scene bg street
    if hero.flags.isceo or game.flags.dwaynedead:
        "Friday is finally here and it's time for the office Christmas Party to begin."
        "In past years I'd have just sloped along to the party when I felt like it."
        "My only concern was soaking up as much of the free booze as humanly possible."
        "Well, that and the chance to flirt with my female colleagues on company time!"
        "But this year, everything is different."
        "This year I'm the CEO of the company, which means I'm the host!"
        "That's also why I'm currently dressed as Santa Claus."
        "I know there's no specific rules about dressing up for the party."
        "But I feel like I need to set an example and put myself out there."
        "You know, show that I'm getting into the Christmas spirit?"
        "I keep on telling myself that as I walk into the party."
        scene bg breakroom
        mike.say "Ho, ho, ho!"
        mike.say "Merry Christmas, everyone!"
        show shiori work surprised at right4
        show lavish work happy at left4
        show aletta work happy at mostright5
        show audrey work surprised at mostleft4
        "As one, the entire room turns around to stare at me."
        "And in that instant I see I'm the only one that bothered to dress up!"
        audrey.say "Oh...my...god!"
        lavish.say "Ha, ha...hello, Santa!"
        shiori.say "Oh dear..."
        shiori.say "Were we supposed to dress up too?"
        aletta.say "Hmm..."
        aletta.say "I didn't know red was your colour, [hero.name]!"
        "I smile and rub the back of my neck, trying to look nonchalant."
        "But the truth is that I just had four hot girls giggling at me."
        "And that's not the ideal way to start a party, now is it?"
        "This would never have happened to Dwayne."
        "He'd have strode in and taken control of the entire room."
        "But that's the entire point, isn't it?"
        "Dwayne would also have gotten drunk, and loud too."
        "Then he'd have started hitting on all the girls at the party."
        "The point is that I'm not Dwayne."
        "And I want to show my employees that I'm not."
        "So who cares if they get a laugh out of my costume?"
        mike.say "Aw..."
        mike.say "Come on, you guys!"
        mike.say "It's Christmas, and this is supposed to be a party!"
        show shiori normal
        show lavish normal
        show aletta normal
        show audrey happy
        "One by one, the girls seem to warm to my pleas."
        audrey.say "Okay, [hero.name], okay."
        show audrey flirt
        audrey.say "I guess the booze will help!"
        lavish.say "You're right, [hero.name]."
        lavish.say "Happy Christmas!"
        shiori.say "I...I really like your costume, [hero.name]!"
        shiori.say "I was just too shy to say so..."
        aletta.say "I have to hand it to you, [hero.name]."
        aletta.say "You're really trying to lead by example."
        show aletta happy
        aletta.say "And I like that."
        "As people begin to mingle and chat, I feel my spirits lifting."
        "Maybe this is going to work out the way I hoped after all."
        "Maybe I can be my own kind of boss and step out of Dwayne's shadow."
        "But then I make a conscious effort to shake off those thoughts."
        "I should be enjoying the party like everyone else."
    else:
        "Friday's finally come around and it's time for the long-awaited office Christmas party."
        "In an effort to get into the spirit of things, I'm all ready and dressed up as Santa."
        "I know there was nothing in the specifics about appropriate seasonal costume."
        "But maybe some of my colleagues will have had the same idea as me."
        "And if not...well, at least I'm not going to be the one saying humbug to it all!"
        scene bg breakroom
        mike.say "Ho, ho, ho!"
        mike.say "Merry Christmas, everyone!"
        show shiori work surprised at right4
        show lavish work happy at left4
        show aletta work happy at mostright5
        show audrey work surprised at mostleft4
        "As one, the entire room turns around to stare at me."
        "And in that instant I see I'm the only one that bothered to dress up!"
        audrey.say "Oh...my...god!"
        lavish.say "Ha, ha...hello, Santa!"
        shiori.say "Oh dear..."
        shiori.say "Were we supposed to dress up too?"
        aletta.say "Hmm..."
        aletta.say "I didn't know red was your colour, [hero.name]!"
        "I smile and rub the back of my neck, trying to look nonchalant."
        "But the truth is that I just had four hot girls giggling at me."
        "And that's not the ideal way to start a party, now is it?"
        hide shiori
        hide lavish
        show aletta annoyed
        show audrey annoyed
        show dwayne
        dwayne.say "Hey, hey, hey!"
        dwayne.say "Now that's what I'm talking about!"
        "Just then, Dwayne comes shouldering through the girls."
        "He has a huge grin on his face and a drink in his hand."
        "From the look of him, it's not the first one he's had."
        "And from the smell of his breath, it's not fruit-juice either!"
        hide audrey
        hide aletta
        dwayne.say "I knew I could rely on you to get into the festive spirit, [hero.name]!"
        dwayne.say "Because you're that kind of guy, you know?"
        "Dwayne wraps one of his huge arms around my shoulder." with hpunch
        "And I swear I can feel the bones and tendons in my body contract as he does so."
        dwayne.say "I mean me - I'd never be able to dress up like a clown."
        dwayne.say "I have an image to maintain, yeah?"
        dwayne.say "But you, [hero.name] - you've got nothing to lose in those stakes!"
        mike.say "Ah..."
        mike.say "Thanks...I guess?"
        "With that, Dwayne seems to lose interest in me."
        hide dwayne
        "He wanders off, leaving me with a bruised shoulder and ego."
        "I don't think I've ever seen the guy that drunk before."
        "Maybe someone should keep an eye on him, you know?"
        "Make sure that he doesn't do anything stupid."
        "After all, you know what kind of stuff happens at office parties."
        "Especially when there's alcohol involved!"
        "But then again, Dwayne did just insult me in front of my colleagues."
        "So maybe he doesn't deserve to have someone looking out for him?"
        "Argh...I need to stop thinking about that jerk!"
        "It's Christmas and this is a party."
        "He's not the only person here."
        "And there are people I'd much rather spend some time with too!"
    scene bg black with dissolve
    pause 1
    $ game.pass_time(1)
    jump office_christmas_dancing


label office_christmas_dancing:
    play music "music/roa_music/santas_nice_list.ogg" loop fadeout .5 fadein .5
    scene bg breakroom with dissolve
    "I need to make the most of this chance to enjoy myself and mingle with my colleagues."
    "And seeing as how there's already some music playing, maybe a dance is in order."
    "But then who am I going to choose as a partner?"
    "Nobody else seems to be up and dancing just yet."
    "So I can have my pick of potential partners."


    $ christmas_girl = max([aletta, audrey, lavish, shiori], key=lambda p: p.love())

    if game.flags.dwaynedead and ("office_event_01" in DONE or "cherie_event_02" in DONE):
        menu:
            "Dance with Aletta" if christmas_girl == aletta:
                pass
            "Dance with Audrey" if christmas_girl == audrey:
                pass
            "Dance with Lavish" if christmas_girl == lavish:
                pass
            "Dance with Shiori" if christmas_girl == shiori:
                pass
            "Dance with Cherie" if not (Person.find("cherie") and cherie.flags.isceo):
                $ christmas_girl = "cherie"


    if christmas_girl == aletta:
        "But it's not like I need to really think about the person I want to dance with."
        show aletta work
        "That's why I walk straight over to Aletta and pop the question without hesitating."
        mike.say "Hey, Aletta..."
        mike.say "You want to dance?"
        show aletta flirt
        "Aletta turns to face me, looking a little surprised as she does so."
        "But it only takes a second for her to regain control of herself and look aloof."
        "She raises an eyebrow, as if the idea of dancing with me amuses her."
        aletta.say "What a quaint idea, [hero.name]!"
        aletta.say "Gyrating to holiday-themed popular music in front of people below my grade."
        aletta.say "Normally I'd say it was below my dignity and my pay grade."
        show aletta normal
        "Aletta pauses to let out a sigh."
        aletta.say "But..."
        aletta.say "As it's the season of goodwill, I'll make an exception."
        "That's good enough for me."
        hide aletta
        show dance aletta work
        "I take Aletta's hand and lead her to a space where we can dance."
        "And it doesn't take long for her to loosen up either."
        "When she cracks a smile, I know that it's a done deal."
        "She's enjoying herself, and even she can't hide it anymore!"
        "Aletta doesn't protest when I begin to move in closer."
        "In fact she positively encourages me with her wry expression."
        "Before I know it, we're wrapped in each other's arms."
        "And we spend the next few songs body-to-body."
        hide dance
        show aletta work happy
        "So much so that when it's over, I feel exhausted!"
        "And I have a serious case of stiffening in my underwear too..."


    elif christmas_girl == audrey:
        show audrey normal work
        "But as soon as my eyes fall on Audrey, I can't think of anyone else."
        "She sees me even before I make it across the room to where she's standing."
        "And she regards me with her arms crossed over her chest."
        show audrey flirt
        audrey.say "Well hello there..."
        audrey.say "To what do I owe this honour?"
        show audrey normal
        mike.say "Hey, Audrey..."
        mike.say "Do you want to dance?"
        "Audrey shakes her head at the request."
        show audrey flirt
        "And she lets out a typically filthy snort of laughter."
        audrey.say "Sure, [hero.name], why not."
        audrey.say "Anything to liven things up around here!"
        hide audrey
        show dance audrey work
        "Audrey grabs me by the hand and leads me to a space where we can dance."
        "And she keeps on taking the lead as soon as we get down to it too."
        "All I had in mind was some innocent dance moves."
        "Maybe a few goofy ones too, just to lighten the mood."
        "But Audrey starts as she means to go on, pressing herself against me."
        "What follows would have left me sweating and breathless in a dark nightclub."
        "So you can imagine the effect Audrey gyrating against me has in the office!"
        "I end up almost standing still as she basically uses me as a dancing pole."
        "Not that I'm complaining about the experience, you understand?"
        "It's just that I'm painfully aware of the fact we have an audience."
        "I can feel everyone's eyes on me the whole time."
        "But not as much as I can feel Audrey's body against mine!"
        "That and the sound of her heavy breathing in my ear."
        hide dance
        show audrey work flirt
        "When it's over, I feel exhausted!"
        "And I have a serious case of stiffening in my underwear too..."


    elif christmas_girl == lavish:
        "I don't have to think too long about exactly who I want to dance with."
        show lavish work
        "And I can't help smiling a the look Lavish gives me as I walk over to her."
        "She's so calm and confident, so self-possessed and poised."
        "She makes me want her just with the merest of glances!"
        mike.say "Hey, Lavish..."
        mike.say "Would you like to dance?"
        show lavish flirt
        "At this, there's a subtle change in Lavish's smile."
        "Slightly knowing and even a little mysterious."
        "All of which only serves to make me want her that much more!"
        lavish.say "I've got to admit, [hero.name]..."
        lavish.say "I was kind of hoping you might ask me that!"
        mike.say "So that's a yes?"
        "By way of answer, Lavish nods."
        "And then she offers me her hand."
        hide lavish
        show dance lavish work
        "I take it, and together we find a space where we can dance."
        "We keep it casual at first."
        "Staying close together, but not actually touching."
        "But at a certain point it feels like something clicks."
        "A switch is thrown in both our heads and things change."
        "I find my hands on Lavish's hips, pulling her close to me."
        "And hers reach for my shoulders, then wrap around my neck."
        "A moment later we're wrapped in each other's arms."
        "We spend the rest of our time dancing locked together like that."
        "And time seems to slow down to a crawl."
        hide dance
        show lavish work
        "When it's over, I feel exhausted!"
        "And I have a serious case of stiffening in my underwear too..."


    elif christmas_girl == shiori:
        show shiori work
        "The moment my eyes settle on Shiori, I feel a flutter in my chest."
        "And I don't even spare a moment to think as I walk over to her."
        show shiori surprised
        "She looks up in surprise, as if amazed that I noticed her at all."
        "Those eyes are so big and innocent, she almost breaks my heart!"
        mike.say "Hey, Shiori..."
        mike.say "Do you want to dance with me?"
        show shiori embarrassed
        "Shiori looks left and right, as if confused."
        "And then she points to herself."
        shiori.say "Wh...why do you want to dance with me?!?"
        shiori.say "There are so many other girls here at the party!"
        shiori.say "Surely you'd rather..."
        show shiori surprised
        mike.say "I don't want to dance with them, Shiori."
        mike.say "I want to dance with you!"
        show shiori normal
        shiori.say "R...really?!?"
        "I nod and smile as I take hold of Shiori's hand."
        hide shiori
        show dance shiori work
        "She offers no resistance as I lead her to a spot where we can dance."
        "At first Shiori's nerves seem to be getting the better of her."
        "She keeps her distance and refuses to even look me in the eye."
        "But the gentle touch seems to be working."
        "First she makes eye-contact, and then she smiles up at me."
        "I return the gesture, and watch as she takes a step closer."
        "And when she leans in close, laying her head against my chest..."
        "Well, it feels almost too good to put into words!"
        "We spend the rest of our time dancing locked in an embrace."
        "And I love the sensation of Shiori's body against mine."
        "Sure, she's built like a sexy little dream."
        "But it's more than that which is making this so special."
        hide dance
        show shiori work happy
        "When it's over, I feel almost exhausted!"
        "Like I'm emotionally drained."
        "And I have a serious case of stiffening in my underwear too..."


    elif christmas_girl == "cherie":
        "I'm scanning the room and looking for a likely dancing partner."
        "It's not like the office is short of girls that look great."
        "And one's that I wouldn't mind getting up close and personal with!"
        "But then I spot someone across the room that I never expected to see here."
        show cherie at center, zoomAt(1.0, (640, 720)) with dissolve
        "It's Cherie, Dwayne's wife - well, now I guess she's his widow!"
        "I make straight for her through the crowd of partygoers between us."
        mike.say "Hey, Cherie..."
        mike.say "I didn't expect to see you here!"
        show cherie smile
        "Cherie turns to face me, a smile on her face as she does so."
        "But it's not hard to see that the smile is kind of forced."
        "She looks good, but more than a little tired."
        "Which isn't surprising - she did just lose her husband."
        show cherie happy
        cherie.say "Oh..."
        cherie.say "Hello there!"
        show cherie normal
        "She shakes her head and gestures around the room."
        show cherie talkative
        cherie.say "I always had a standing invitation to these kind of things."
        cherie.say "I just never felt like coming along to any of them before now."
        show cherie happy
        cherie.say "And...well...I just wanted to get out of the house!"
        show cherie whining
        cherie.say "I hope that doesn't make me sound as awful as I think it does!"
        show cherie sadsmile
        "Now it's my turn to shake my head."
        "I'm more than eager to soothe Cherie's worries."
        mike.say "Of course not, Cherie!"
        mike.say "I think you're seriously brave to be here."
        mike.say "Especially after all you've been through."
        show cherie smile
        "Cherie smiles sweetly at my attempts to comfort her."
        "But then there's an awkward pause."
        "Neither of us seems to know what to do next."
        "And then it comes to me."
        mike.say "Hey..."
        mike.say "You want to dance?"
        show cherie stuned
        "Cherie looks at me in surprise for a moment."
        "But then she cracks a genuine smile and lets out a girlish giggle."
        show cherie happy
        cherie.say "You know...why the hell not!"
        cherie.say "Lead the way!"
        hide cherie
        show christmas dance cherie
        with fade
        "Cherie takes my arm and I lead her out onto the makeshift dance-floor."
        "I can feel the eyes of the other partygoers on us the whole time."
        "After all, I am dancing with the dead CEO's glamorous widow!"
        "But it doesn't take me long to forget all about them."
        "In fact, I soon forget everyone in the room, save for Cherie."
        "She presses herself close to me the whole time."
        "Her arms around me like she needs me to hold her up."
        "It's like I can feel the need in her."
        "The way she's been left all alone now that Dwayne's dead."
        hide dance with fade
        "When it's over, I feel almost exhausted!"
        "Like I'm emotionally drained."
        "And I have a serious case of stiffening in my underwear too..."
    scene bg black with dissolve
    pause 1
    $ game.pass_time(1)
    jump office_christmas_antics


label office_christmas_antics:
    play music "music/roa_music/santas_nice_list.ogg" loop fadeout .5 fadein .5
    scene bg breakroom with dissolve
    "By now the party's well and truly underway, with people laughing, joking and dancing."
    "It feels like everyone's guard has finally come down and they're getting into the festive spirit."
    "Well, maybe the festive spirits would be a better way of putting it."
    "Because a considerable amount of booze seems to have been consumed as well!"
    "More than a few people have pink noses and red cheeks from the alcohol."
    "And soon enough, talk begins to turn towards things of a risky nature..."
    show lavish work angry at right
    show audrey work angry at left
    audrey.say "All I'm saying is that it's a Christmas Party, Lavish!"
    audrey.say "People expect you do get drunk and do crazy stuff."
    lavish.say "They might expect you to do it, Audrey."
    lavish.say "But that's no reason to actually do it!"
    hide audrey
    hide lavish
    show shiori work surprised at left
    show aletta work sad at right
    shiori.say "Ooh..."
    shiori.say "It sounds scary!"
    aletta.say "Hmm..."
    aletta.say "What are you talking about?"
    show aletta annoyed
    aletta.say "Is somebody plotting to pull off a prank?"
    "I can't help being intrigued by the conversation the girls are having."
    "And so I sidle over to get involved in it as well."
    mike.say "Yeah, what are you talking about?"
    mike.say "Come on, spill it!"
    show shiori sad at mostleft4
    show aletta at mostright5
    show lavish work annoyed at right4
    show audrey work annoyed at left4
    "Suddenly I have all four of the girls looking straight at me."
    "And it's more than a little amusing to see the expressions on their faces."
    "All four of them, even Aletta, look like guilty school-girls right now!"
    aletta.say "We were just..."
    lavish.say "Just talking..."
    shiori.say "Talking about..."
    show shiori surprised
    show lavish surprised
    show aletta surprised
    show audrey angry
    audrey.say "Oh, come on, guys!"
    audrey.say "It's [hero.name] we're talking to here!"
    show shiori normal
    show lavish normal
    show aletta normal
    show audrey normal
    audrey.say "At heart, he's as big of a goof-off as anybody!"
    audrey.say "We were talking about pranks, [hero.name]."
    show audrey flirt
    audrey.say "Pranks at the Christmas party, you know?"
    "I nod slowly, then look over my shoulder at the photocopier."
    "All four of the girls follow my gaze too."
    mike.say "You mean the old classics, right?"
    mike.say "Like photocopying a certain part of your anatomy, for example?"
    show aletta annoyed
    aletta.say "Huh - so childish!"
    show lavish annoyed
    lavish.say "That's pretty unprofessional!"
    show shiori annoyed
    shiori.say "Not to mention unhygienic too!"
    show audrey happy
    audrey.say "Yeah, [hero.name] - that's a great idea!"
    "Well, it looks like at least one of them is up for it."
    "I wonder if I can talk the other three round?"


    $ christmas_girl = max([aletta, audrey, lavish, shiori], key=lambda p: p.sub())


    if christmas_girl == audrey and audrey.sub >= 25:
        "She seems eager to see the prank played out."
        "So it makes sense for Audrey to be the one to actually do it."
        "The one to put her ass on the line."
        "Or in this case, on the photocopier!"
        "So I walk over to it and lift the lid, patting the glass beneath."
        mike.say "Great, Audrey!"
        mike.say "Why don't you show us how it's done?"
        show shiori normal
        show audrey awkward
        "I see a sudden change in Audrey's expression."
        "Clearly she wasn't expecting me to call her bluff!"
        audrey.say "Wh...what?!"
        audrey.say "Why me?"
        aletta.say "Hmm..."
        aletta.say "How disappointing!"
        show lavish normal
        lavish.say "Yeah, Audrey - way to lead by example!"
        show shiori embarrassed
        shiori.say "Well, I'm not doing it if she won't!"
        "I look at Audrey with raised eyebrows."
        "And she makes an effort to look more confident."
        show audrey angry
        audrey.say "I never said I wouldn't do it!"
        audrey.say "I just wanted to know why it had to be me."
        audrey.say "And that's obviously because I'm the only one with the guts to do it!"
        hide aletta
        hide lavish
        hide shiori
        hide audrey
        show audrey close work normal
        "Audrey strides past the others and takes my hand."
        show audrey bottomless
        "Then she hikes up her skirts and clambers onto the photocopier."
        show audrey awkward
        "But as she wriggles her ass on top of it, there's a sickening crack!"
        audrey.say "Oh no - my ass!"
        show audrey -close
        "Audrey hops off of the photocopier again."
        "Which means I can see the cracked glass where she was just sat."
        mike.say "Wow, Audrey."
        mike.say "I never knew your ass was THAT heavy!"
        show audrey scared
        "Before I can say another word, Audrey thrusts her backside at me."
        audrey.say "Never mind that, [hero.name]!"
        audrey.say "Check out my ass!"
        show audrey close flirt
        "I dutifully do as I'm told, exploring Audrey's buttocks for damage."
        "Admittedly, I take longer than is strictly necessary."
        "But I feel the need to do a thorough job!"
        mike.say "Don't worry, everything's in order back here!"
        show audrey normal -close -bottomless
        "Audrey lets out an audible sigh of relief."
        "And the others enjoy a good laugh at her expense."


    elif christmas_girl == aletta and aletta.sub >= 25:
        "I smile broadly and look straight at Aletta."
        "Then I walk over to the photocopier."
        "Once there, I lift the lid and pat the glass beneath."
        mike.say "Why don't you hop on up here, Aletta?"
        show shiori normal
        show lavish normal
        show audrey normal
        "In response, Aletta lets out a snort of derision."
        aletta.say "And why, pray tell, would I do that?"
        "I shrug and twist my face into a frown."
        mike.say "Maybe because true management material leads by example?"
        mike.say "I mean, it's not like you're actually afraid, is it?"
        show audrey flirt
        audrey.say "I'd have done it without even thinking!"
        show lavish flirt
        lavish.say "Hmm..."
        lavish.say "It would show fearlessness in the face of a challenge."
        show shiori embarrassed
        shiori.say "Well, I'm not doing it if she won't."
        shiori.say "And that's that!"
        "I look at Aletta with raised eyebrows."
        show aletta normal
        "And she makes an effort to look more confident."
        aletta.say "I only refused before because I hadn't established the mood."
        aletta.say "And I have to say it's of a much lower standard than I'd hoped!"
        aletta.say "But if that's what it takes to show you animals who's the boss around here..."
        hide audrey
        hide shiori
        hide lavish
        hide aletta
        show aletta close work normal
        "Aletta strides past the others and takes my hand."
        show aletta bottomless
        "Then she hikes up her skirts and clambers onto the photocopier."
        show aletta surprised
        "But as she wriggles her ass on top of it, there's a sickening crack!"
        aletta.say "Oh lord!"
        aletta.say "Oh no!"
        show aletta -close
        "Aletta hops off of the photocopier again."
        "Which means I can see the cracked glass where she was just sat."
        mike.say "Wow, Aletta."
        mike.say "I never knew your ass was THAT heavy!"
        "Before I can say another word, Aletta thrusts her backside at me."
        show aletta pain
        aletta.say "Never mind that, [hero.name]!"
        aletta.say "Make yourself useful and check if my behind is okay!"
        show aletta close flirt
        "I dutifully do as I'm told, exploring Aletta's buttocks for damage."
        "Admittedly, I take longer than is strictly necessary."
        "But I feel the need to do a thorough job!"
        mike.say "Don't worry, everything's in order back here!"
        show aletta normal -close -bottomless
        "Aletta lets out an audible sigh of relief."
        "And the others enjoy a good laugh at her expense."


    elif christmas_girl == lavish and lavish.sub >= 25:
        "I smile broadly and look straight at Lavish."
        "Then I walk over to the photocopier."
        "Once there, I lift the lid and pat the glass beneath."
        mike.say "Why don't you hop on up here, Lavish?"
        show shiori normal
        show aletta normal
        show audrey happy
        show lavish surprised
        "Lavish's eyes go wide at the suggestion."
        "And she shakes her head in confusion."
        lavish.say "Wh...why me?"
        "I shrug and twist my face into a frown."
        mike.say "Maybe because true management material leads by example?"
        mike.say "I mean, it's not like you're actually afraid, is it?"
        show aletta flirt
        aletta.say "Hmm..."
        aletta.say "I would have put myself forward in an instant!"
        audrey.say "Ooh, she's terrified!"
        show audrey flirt
        audrey.say "Maybe you don't have the stones for this kind of thing, Lavish!"
        show shiori embarrassed
        shiori.say "Well, I'm not doing it if she won't."
        shiori.say "And that's that!"
        "I look at Lavish with raised eyebrows."
        show lavish normal
        "And she makes swallows, trying to overcome her fears."
        lavish.say "Well...when you put it like that!"
        lavish.say "You have to be able to see things like this as an opportunity!"
        lavish.say "When life gives you lemons, as they say..."
        hide audrey
        hide aletta
        hide shiori
        hide lavish
        show lavish close work normal
        "Lavish strides past the others and takes my hand."
        show lavish bottomless
        "Then she hikes up her skirts and clambers onto the photocopier."
        show lavish surprised
        "But as she wriggles her ass on top of it, there's a sickening crack!"
        lavish.say "Oh no!"
        lavish.say "What was that noise!"
        show lavish a -close
        show expression "lavish_bot_a_underwear"
        "Lavish hops off of the photocopier again."
        "Which means I can see the cracked glass where she was just sat."
        mike.say "Wow, Lavish."
        mike.say "I never knew your ass was THAT heavy!"
        "Before I can say another word, Lavish thrusts her backside at me."
        show lavish a angry
        lavish.say "[hero.name]!"
        lavish.say "Am I okay?"
        lavish.say "Check if I'm bleeding back there!"
        hide expression "lavish_bot_a_underwear"
        show lavish close sad
        "I dutifully do as I'm told, exploring Lavish's buttocks for damage."
        "Admittedly, I take longer than is strictly necessary."
        "But I feel the need to do a thorough job!"
        mike.say "Don't worry, everything's in order back here!"
        show lavish normal -close -bottomless
        "Lavish lets out an audible sigh of relief."
        "And the others enjoy a good laugh at her expense."


    elif christmas_girl == shiori and shiori.sub >= 25:
        "I smile broadly and look straight at Shiori."
        "Then I walk over to the photocopier."
        "Once there, I lift the lid and pat the glass beneath."
        mike.say "Why don't you hop on up here, Shiori?"
        show aletta normal
        show audrey normal
        show lavish normal
        show shiori surprised
        "Shiori looks instantly panicked by the mere suggestion."
        "She looks this way and that, hoping for some way out."
        show shiori embarrassed
        shiori.say "P...please, [hero.name]..."
        shiori.say "I don't really want to..."
        "With the same smile on my face, I pat the photocopier again."
        mike.say "Never mind what you want, Shiori."
        mike.say "I'm ordering you to do it!"
        aletta.say "Hmm..."
        aletta.say "I wonder if he has the authority to pull it off?"
        show audrey flirt
        audrey.say "I'd have done it without even thinking!"
        show lavish flirt
        lavish.say "Hmm..."
        lavish.say "It would show fearlessness in the face of a challenge."
        "I look at Shiori with raised eyebrows."
        hide audrey
        hide aletta
        hide lavish
        hide shiori
        show shiori close work embarrassed
        "She nods quickly and begins to scamper forwards."
        "But she still looks like she'd rather be somewhere else."
        "Anywhere else in the entire world right now."
        shiori.say "Y...yes, [hero.name]."
        shiori.say "Right away, [hero.name]!"
        show shiori bottomless
        "Then she hikes up her skirts and clambers onto the photocopier."
        show shiori surprised
        "But as she wriggles her ass on top of it, there's a sickening crack!"
        shiori.say "Oh my!"
        shiori.say "Oh my goodness!"
        show shiori -close
        "Shiori hops off of the photocopier again."
        "Which means I can see the cracked glass where she was just sat."
        mike.say "Wow, Shiori."
        mike.say "I never knew your ass was THAT heavy!"
        "Before I can say another word, Shiori thrusts her backside at me."
        show shiori embarrassed
        shiori.say "Oh, [hero.name]!"
        shiori.say "How bad is it?"
        shiori.say "Will I need to go to the hospital?!?"
        show shiori close
        "I dutifully do as I'm told, exploring Shiori's buttocks for damage."
        "Admittedly, I take longer than is strictly necessary."
        "But I feel the need to do a thorough job!"
        mike.say "Don't worry, everything's in order back here!"
        show shiori normal -close -bottomless
        "Shiori lets out an audible sigh of relief."
        "And the others enjoy a good laugh at her expense."
    else:


        show aletta normal
        aletta.say "Hmm..."
        aletta.say "How about you lead by example, [hero.name]?"
        show audrey normal
        show shiori normal
        show lavish normal
        "I frown at Aletta's suggestion."
        "I'm not sure what she means."
        "But I know that I don't like the sound of it!"
        audrey.say "Yeah, [hero.name]."
        audrey.say "You go first!"
        "Ah, I see."
        "Trust Audrey to cut to the chase!"
        lavish.say "I wonder if he will?"
        show shiori embarrassed
        shiori.say "Oh, [hero.name]!"
        shiori.say "Please be careful!"
        "I let out a snort of derision in response."
        "I'm not about to let them write me off as a coward!"
        mike.say "Sure, if that's what you girls want."
        mike.say "I'll be the one to go first."
        "I nod, trying to show that I'm confident."
        "But inside I'm already worried about going through with it!"
        "I pull down my pants and underwear."
        "At the same time making sure I don't flash them."
        "And then I hop onto the photocopier."
        show audrey surprised
        show lavish surprised
        show shiori surprised
        show aletta surprised
        "But no more than a second later, I hear a sickening crack!"
        mike.say "Oh shit!"
        mike.say "Oh shit, oh shit, oh shit!"
        "I hop off of the photocopier again."
        "And the girls hurry over to inspect the cracked glass where I just sat."
        show aletta annoyed
        aletta.say "Well that's not going to be cheap to fix!"
        show audrey happy
        audrey.say "Wow, [hero.name]."
        audrey.say "I never knew your ass was THAT heavy!"
        show lavish normal
        lavish.say "I'm glad you went first now!"
        show shiori sad
        shiori.say "[hero.name], are you okay?"
        shiori.say "Should I call you an ambulance?!?"
        mike.say "Never mind all that!"
        mike.say "How about checking if my ass is okay, huh?!?"
        show audrey happy
        show lavish happy
        show shiori happy
        show aletta happy
        "I bend over as they gather around to inspect my backside."
        "And I can feel my cheeks burning the whole time."
        "Not least because the whole process seems to take far too long!"
        mike.say "Hey - what's going on back there!"
        show aletta flirt
        aletta.say "Oh, pipe down!"
        show audrey flirt
        audrey.say "Yeah, we need to do a thorough job!"
        show lavish flirt
        lavish.say "We should make sure you're okay!"
        show shiori joke
        shiori.say "Oh, my poor [hero.name]!"
        show audrey happy
        show lavish happy
        show shiori happy
        show aletta happy
        "All I can do is stand there and let them have their fun."
        "Every laugh and giggle reminding me of my predicament."
        "And of just how dumb I was to agree to this in the first place too!"
    scene bg black with dissolve
    pause 1
    $ game.pass_time(1)
    jump office_christmas_mistletoe_kiss


label office_christmas_mistletoe_kiss:
    play music "music/roa_music/santas_nice_list.ogg" loop fadeout .5 fadein .5
    scene bg office with dissolve
    "All the time the party is going on, I keep glancing over at the mistletoe."
    "It's hanging down from the ceiling where most people don't seem to see it."
    "But I can't help feeling like it's almost mocking me whenever I glance at it."
    "People keep passing under it as I watch."
    "Yet it never seems to be the right person at the right time!"
    "Finally I see my chance, and I step up to meet the challenge."
    "As my intended target walks under the mistletoe, I ask the question..."


    $ christmas_girl = max([aletta, audrey, lavish, shiori], key=lambda p: p.flags.kiss)

    if game.flags.dwaynedead and ("office_event_01" in DONE or "cherie_event_02" in DONE):
        menu:
            "Kiss Aletta" if christmas_girl == aletta:
                pass
            "Kiss Audrey" if christmas_girl == audrey:
                pass
            "Kiss Lavish" if christmas_girl == lavish:
                pass
            "Kiss Shiori" if christmas_girl == shiori:
                pass
            "Kiss Cherie" if not (Person.find("cherie") and cherie.flags.isceo):
                $ christmas_girl = "cherie"


    if christmas_girl == aletta:
        mike.say "Erm, Aletta..."
        mike.say "Take a look up there!"
        show aletta normal work
        "Aletta stops dead in her tracks and frowns at me."
        "Then she sighs and does as I ask."
        aletta.say "I see the ceiling, [hero.name]."
        aletta.say "And I see a sorry-looking sprig of mistletoe!"
        "She returns her gaze to my level."
        "And now I see that she's wearing a wry grin."
        "Aletta adds to that with a raised eyebrow."
        show aletta annoyed
        aletta.say "And your point is?"
        mike.say "Well..."
        mike.say "There's kind of a tradition, isn't there?"
        mike.say "You know...this time of year?"
        "Aletta seems to be enjoying this."
        "Having me squirm on the spot as she drags it out of me."
        show aletta normal
        aletta.say "Oh, I see!"
        aletta.say "Normally I'm against fraternisation during work hours."
        aletta.say "But as this is a party..."
        "Aletta puts her hands on my cheeks and pulls me closer."
        hide aletta
        show aletta kiss work
        $ aletta.flags.kiss += 1
        "And then she plants her lips on mine."
        "I barely have time to react in kind."
        "Before I know it, her tongue is between my lips."
        "What Aletta gives me is no chaste festive kiss."
        "It's a full-on display of unbridled passion!"
        "And it goes on for what feels like forever too."
        "When she finally breaks it off, I'm left breathless and gasping."
        hide aletta kiss
        show aletta flirt work
        aletta.say "Merry Christmas, [hero.name]."
        aletta.say "And a very prosperous New year!"


    elif christmas_girl == audrey:
        mike.say "Erm, Audrey..."
        mike.say "You see what's up there?"
        show audrey normal work
        "Audrey looks surprised for a moment."
        "But then she follows my gaze upwards."
        "And the moment she sees the mistletoe, her mood changes."
        show audrey flirt
        "Audrey looks back down at me with a wicked smile on her face."
        audrey.say "How long have you been standing there, [hero.name]?"
        audrey.say "You've been waiting for me to walk under it - haven't you?"
        "I can't help swallowing nervously."
        "And I'm sure my cheeks are flushing red right now too!"
        mike.say "I..."
        mike.say "I might have been..."
        audrey.say "You've imagined every second of it too!"
        audrey.say "But the real thing is always so much better..."
        "Audrey underlines her point by leaning towards me."
        hide audrey
        show audrey kiss work
        $ audrey.flags.kiss += 1
        "And then she places her lips on mine."
        "She lingers there a while, pressing herself against me."
        "And only makes her next move once I put my hands on her hips."
        "At once she pulls them downwards so that I'm grabbing her ass."
        "Then she pushes her tongue deep into my open mouth."
        "Audrey wriggles and presses against me like a restless snake."
        "And her tongue does the same thing as her body."
        "I've never had a kiss under the mistletoe like this one."
        "One that feels so passionate and lingers so long."
        "And when she finally breaks it off, I'm left breathless and gasping."
        hide audrey kiss
        show audrey flirt work
        audrey.say "Mmm..."
        audrey.say "Merry Christmas, [hero.name]."


    elif christmas_girl == lavish:
        mike.say "Erm, Lavish..."
        mike.say "Look up there!"
        show lavish normal work
        "Lavish blinks in surprise, as if I've caught her off-guard."
        "But she can't help following my gaze upwards all the same."
        lavish.say "Oh..."
        lavish.say "Mistletoe!"
        "Lavish looks back down at me, blushing as she does so."
        "There's a knowing smile on her face."
        "But she seems a little bashful too."
        "And the combination really suits her, you know?"
        "It makes her look super cute!"
        show lavish flirt
        lavish.say "Are you..."
        lavish.say "Asking me for a Christmas kiss, [hero.name]?"
        mike.say "Y...yeah, Lavish."
        mike.say "I guess I am!"
        "Lavish beckons me closer."
        hide lavish
        show lavish kiss work
        $ lavish.flags.kiss += 1
        "And then she stands on her tip-toes to reach me."
        "At first she places her lips gently against mine."
        "The kiss is pretty chaste and innocent in nature."
        "But somehow it still gives me butterflies in my stomach."
        "And when I feel Lavish's tongue between my lips..."
        "Well, it's hard to describe how excited the sensation makes me feel!"
        "Lavish seems to feel the same way too."
        "I know this because of the way she ups the stakes."
        "Her arms are around my neck and mine around her waist."
        "And her tongue is exploring my mouth the whole time."
        "When Lavish finally breaks it off, I'm left breathless and gasping."
        hide lavish kiss
        show lavish flirt work
        lavish.say "Oh..."
        lavish.say "Oh my..."
        lavish.say "Merry Christmas, [hero.name]."


    elif christmas_girl == shiori:
        mike.say "Erm, Shiori..."
        mike.say "Look up!"
        show shiori normal work
        "Shiori stops dead the moment she hears my voice."
        "And she glances upwards just as quickly too."
        shiori.say "Wha..."
        shiori.say "Oh my!"
        shiori.say "Mistletoe!"
        show shiori flirt
        "The moment that Shiori looks down again, she blushes."
        "And she struggles to meet my eye as well!"
        mike.say "Shiori..."
        mike.say "Would you like a..."
        shiori.say "A kiss under the mistletoe!"
        shiori.say "Oh yes, [hero.name]!"
        shiori.say "I've been waiting for you to ask since the party started!"
        "I lean forwards and gently put my hands on Shiori's shoulders."
        "And she stands on her tip-toes, meeting me on the way down."
        hide shiori
        show shiori kiss work
        $ shiori.flags.kiss += 1
        "Our lips touch softly and gently at first."
        "And I can almost feel a tingle run through Shiori's body."
        "Her hands reach up and wrap around my neck."
        "It's then that I take a gamble."
        "I slip my tongue into Shiori's mouth."
        "And she moans, unable to hide her delight."
        "It only gets better when Shiori returns the gesture too."
        "Things seem to be heating up between us by the second."
        "And when Shiori finally lets go, I'm left breathless and gasping."
        hide shiori kiss
        show shiori flirt work
        shiori.say "Oh..."
        shiori.say "Oh, [hero.name]..."


    elif christmas_girl == "cherie":
        mike.say "Ah, Cherie..."
        mike.say "Look up there!"
        show cherie stuned
        "Cherie turns and then looks up in surprise."
        "It takes her a moment to see the sprig of mistletoe overhead."
        show cherie flirt
        "She looks back down at me, blushing a little as she does so."
        "Her reaction is so honest and unexpected, even a little vulnerable."
        "And it instantly tugs at my heart."
        show cherie happy
        cherie.say "Oh, I see..."
        cherie.say "Mistletoe!"
        show cherie normal
        mike.say "And...well..."
        mike.say "You know the tradition, right?"
        show cherie amused
        "Cherie pulls a mock frown and cocks her head on one side."
        show cherie talkative
        cherie.say "Wait a minute..."
        cherie.say "Are you asking me for a kiss?"
        show cherie amused
        mike.say "Not so much asking..."
        mike.say "Maybe more enquiring..."
        mike.say "Basically testing the water..."
        show cherie happy at startle
        "Cherie chuckles as she wraps her hands around my neck."
        hide cherie
        show cherie kiss santa
        with fade
        "And then she places her lips against mine."
        "Cherie kisses me gently at first."
        "But then I feel her begin to press her body into me."
        "And at the same time, she slowly pushes her tongue between my lips."
        "I respond in kind, pulling her ever closer."
        "This means that the kiss builds in intensity the whole time."
        "And before too long, she's almost panting in my arms."
        hide cherie
        show cherie flirt
        with fade
        "And when Cherie finally breaks it off, I'm left breathless and gasping."
        show cherie happy
        cherie.say "Oh..."
        cherie.say "Oh wow...I think I got a little carried away there!"
        cherie.say "Happy Christmas, [hero.name]!"
    scene bg black with dissolve
    pause 1
    $ game.pass_time(1)
    if not game.flags.dwaynedead:
        jump office_christmas_dwayne_antics
    else:
        jump office_christmas_sex


label office_christmas_dwayne_antics:
    play music "music/roa_music/santas_nice_list.ogg" loop fadeout .5 fadein .5
    scene bg office with dissolve
    $ ignore_dwayne_flags = False
    if not hero.flags.isceo:
        "The party's well underway by now, with people dancing and chatting happily."
        "And a lot of that good feeling is down to the generous supply of alcohol."
        "I have to admit that Dwayne's been generous with the budget this year."
        "But by the looks of him, he's not been shy of indulging himself either!"
        "I see him on the other side of the room, laughing and joking loudly."
        "He hides it well, but I know him well enough to tell that he's pretty drunk."
        "Suddenly he seems to spot something that takes his interest."
        "And he lurches off in the same direction without excusing himself."
        "Somehow, I can't help feeling this might spell trouble."
        "So I begin to follow Dwayne, making sure that he doesn't see me."
        "And soon enough, he leads me to what he's spotted."
        "Or to be more specific, to who..."


    $ christmas_girl = max([aletta, audrey, lavish, shiori], key=lambda p: p.sexperience)


    if christmas_girl == aletta:
        "As I watch his progress, Dwayne reaches Aletta."
        show dwayne
        dwayne.say "Hey, Aletta!"
        dwayne.say "It's cold outside."
        dwayne.say "But you're looking hot as usual!"
        show aletta work annoyed at right
        "Aletta rolls her eyes at the corny line."
        "But I can see she's trying to hide her revulsion."
        aletta.say "I think you've had one too many, Dwayne."
        aletta.say "Maybe you should eat something from the buffet?"
        aletta.say "It might soak up some of the booze."
        "Dwayne seems to find Aletta's comeback hilarious."
        "He bursts out laughing and shakes his head."
        "But then he leans in closer to Aletta than before."
        dwayne.say "You know what, Aletta."
        dwayne.say "I think you should take your own advice."
        dwayne.say "How about you come into my office for a while?"
        dwayne.say "I've got something really special for you to eat in there!"
        "Aletta looks this way and that."
        "It's obvious that she's searching for a way out."
        "And then her gaze falls on me."
        show aletta sad
        "Aletta's eyes widen as she silently appeals for help."
        menu:
            "Help Aletta":
                "I know Aletta's more than capable of handling herself."
                "So if she's appealing for help, that means it serious!"
                "I have no idea what I'm going to actually do or say."
                "But I hurry over all the same."
                mike.say "Hey, Dwayne!"
                mike.say "Did someone mention the buffet?!?"
                "Dwayne turns to face me, looking confused."
                dwayne.say "Huh?"
                mike.say "Aw, man - you've got to see it to believe it!"
                mike.say "Come on, I already saved you a plate."
                mike.say "Let's get you fed before it's all gone!"
                "Drunk as he is, Dwayne lets me lead him away from Aletta."
                "I mean, what's he going to do?"
                "Tell me off and demand I let him go back and keep on harassing her?"
                "I take a moment to glance back over my shoulder."
                show aletta happy
                $ game.flags.worksatisfaction -= 10
                $ game.flags.promoted -= 2
                "And I see a relieved Aletta mouth the words 'thank you'."
            "Ignore Aletta":
                "I'm not about to get involved in that little mess."
                "And Aletta's more than capable of looking after herself."
                "I look away as quickly as I can."
                "And I try to make it look like I didn't catch her intent."
                "The last thing I see as I walk away is the look on Aletta's face."
                "Despite my best efforts, she knows full well I just left her hanging."
                $ ignore_dwayne_flags = True
                $ aletta.love -= 10

    elif christmas_girl == audrey:
        "As I watch his progress, Dwayne reaches Audrey."
        show dwayne
        dwayne.say "Hey, Audrey!"
        dwayne.say "I've been watching you real closely."
        dwayne.say "And I see you're the kind of girl that likes to have fun, right?"
        show audrey work annoyed at right
        "Audrey regards Dwayne with barely suppressed disgust."
        "He might be closer to the truth about her than her realises."
        "But Audrey still has self-respect."
        "So of course she's insulted by his drunken advances."
        audrey.say "I think you're a little confused."
        audrey.say "Because I have no idea what you're talking about!"
        "Dwayne doesn't seem put off in the slightest by this."
        "In fact, he seems to see it as some kind of encouragement."
        dwayne.say "Aw, come on, Audrey."
        dwayne.say "I know an office bike when I see one!"
        dwayne.say "All I want is my turn to take you for a ride!"
        "Audrey looks this way and that."
        "It's obvious that she's searching for a way out."
        "And then her gaze falls on me."
        show audrey sad
        "Audrey's eyes widen as she silently appeals for help."
        menu:
            "Help Audrey" if hero.fitness >= 25 or hero.charm >= 25:
                "I know full well that Audrey's capable of looking after herself."
                "So if she's asking for help, then I know that she needs it badly."
                "I hurry over as fast as I can elbow through the crowd."
                "My mind racing until the very last moment to think up a plan."
                mike.say "Hey, Audrey!"
                mike.say "I found a stationary cupboard that's empty!"
                mike.say "We can go do..."
                mike.say "Oh...hey, Dwayne!"
                show audrey frown
                "Both Dwayne and Audrey look shocked and confused at my arrival."
                "But luckily for me, Audrey catches on more quickly."
                audrey.say "Oh...oh yeah!"
                audrey.say "The stationary cupboard!"
                "She winks at me in an obvious manner."
                "And I wink back."
                dwayne.say "Oh, I see what's going on here!"
                "Dwayne nods and smiles."
                dwayne.say "Sorry, [hero.name]."
                dwayne.say "Didn't know she was already taken!"
                "With that, he shoots me a cheesy grin and wanders off."
                hide dwayne
                show audrey normal at center with move
                $ game.flags.worksatisfaction -= 10
                $ game.flags.promoted -= 2
                "Which allows both Audrey and I to let out a sigh of relief."
                mike.say "Sorry about that, Audrey."
                mike.say "I had to think on my feet back there!"
                show audrey happy
                audrey.say "No worries, [hero.name]."
                audrey.say "There isn't really a stationary cupboard free, is there?"
                mike.say "Erm...no."
                audrey.say "Shame..."
            "Ignore Audrey":
                "If Audrey hadn't behaved like such a flirt around here..."
                "Well, maybe she wouldn't be in such a mess right now."
                "I look away as quickly as I can."
                "And I try to make it look like I didn't catch her intent."
                "The last thing I see as I walk away is the look on Audrey's face."
                $ audrey.love -= 10
                "Despite my best efforts, she knows full well I just left her hanging."
                $ ignore_dwayne_flags = True

    elif christmas_girl == lavish:
        "As I watch his progress, Dwayne reaches Lavish."
        show dwayne
        dwayne.say "Hey, Lavish!"
        dwayne.say "You've got some real career goals, right?"
        dwayne.say "I think we should discuss them in my office."
        show lavish work surprised at right
        "Lavish looks instantly shocked at Dwayne's approach."
        "He's leaning in close to her, invading her personal space."
        "And he's just behaviour just stinks of unprofessionalism."
        "All things that Lavish can't stand being exposed to."
        lavish.say "Mr Jackson..."
        lavish.say "I don't think this is the time or the place!"
        lavish.say "And your behaviour is inappropriate!"
        "Dwayne doesn't seem in the least bit put off by this."
        "In fact, he seems to see it as Lavish playing hard to get!"
        dwayne.say "Aw, come on, Lavish."
        dwayne.say "This is your chance to get ahead."
        dwayne.say "All you have to do is give me some head first!"
        "Lavish looks this way and that."
        "It's obvious that she's searching for a way out."
        "And then her gaze falls on me."
        show lavish sad
        "Lavish's eyes widen as she silently appeals for help."
        menu:
            "Help Lavish":
                "I know full well that Lavish's capable of looking after herself."
                "So if she's asking for help, then I know that she needs it badly."
                "I hurry over as fast as I can elbow through the crowd."
                "My mind racing until the very last moment to think up a plan."
                mike.say "Hey, Lavish!"
                mike.say "My friend looked up that lawyer you recommended."
                mike.say "And they really tore his boss a new asshole!"
                show lavish surprised
                "Both Dwayne and Lavish look shocked and confused at my arrival."
                "But luckily for me, Lavish catches on more quickly."
                show lavish normal
                lavish.say "Oh...oh yeah!"
                lavish.say "That guy's a real professional!"
                lavish.say "He eats inappropriate bosses alive!"
                "I look at Dwayne, trying to pretend I just noticed him."
                mike.say "Oh, hey, Dwayne!"
                mike.say "Sorry to talk about bosses getting taken to the cleaners just now."
                mike.say "But you're one of the good ones, aren't you?"
                mike.say "You don't have to worry about getting sued back to the stone age!"
                "Dwayne nods, seeming to sober up on the spot."
                dwayne.say "Y...yeah, of course!"
                dwayne.say "I'm not one of those sleazy assholes!"
                dwayne.say "No way!"
                "With that, he shoots me a pained smile and hurries off."
                hide dwayne
                show lavish normal at center with move
                $ game.flags.worksatisfaction -= 10
                $ game.flags.promoted -= 2
                "Which allows both Lavish and I to let out a sigh of relief."
                mike.say "Sorry about that, Lavish."
                mike.say "I had to think on my feet back there!"
                show lavish happy
                lavish.say "No worries, [hero.name]."
                lavish.say "I owe you one!"
            "Ignore Lavish":
                "If Lavish wants to make it to the top, she has to do it herself."
                "And part of that is always going to be dealing with stuff like this."
                "I look away as quickly as I can."
                "And I try to make it look like I didn't catch her intent."
                "The last thing I see as I walk away is the look on Lavish's face."
                "Despite my best efforts, she knows full well I just left her hanging."
                $ lavish.love -= 10



    elif christmas_girl == shiori:
        "As I watch his progress, Dwayne reaches Shiori."
        show dwayne
        dwayne.say "Hey, Shiori!"
        dwayne.say "You know what they say about Christmas, right?"
        dwayne.say "Goodwill to men and all that?"
        dwayne.say "Well your goods are making me feel pretty great right now!"
        show shiori work annoyed at right
        "Shiori literally jumps at the way Dwayne pops up before her."
        "He's looming over her like some ogre out of a fairy tale."
        "And she looks too scared to turn her back on him and escape."
        shiori.say "W...wh...what do you want, Mister Jackson?"
        shiori.say "I think this is above my pay-grade!"
        "Dwayne doesn't seem to hear the fear in Shiori's voice."
        "Instead of backing off, he leans in even closer than before."
        dwayne.say "Aw, don't worry about that, Shiori."
        dwayne.say "It's Christmas, and I'm playing Santa!"
        dwayne.say "Just come into my office and sit on my lap a while."
        dwayne.say "I got something for you in my sack!"
        "Shiori looks this way and that."
        "It's obvious that she's searching for a way out."
        "And then her gaze falls on me."
        show shiori sad
        "Shiori's eyes widen as she silently appeals for help."
        menu:
            "Help Shiori":
                "I know full well that Shiori's not capable of looking after herself."
                "She needs help in a situation like this, and I'm going to provide it."
                "I hurry over as fast as I can elbow through the crowd."
                "My mind racing until the very last moment to think up a plan."
                mike.say "Hey, Shiori!"
                mike.say "The school just called."
                mike.say "They said Kanta had a nose-bleed or something?"
                show shiori surprised
                "Both Dwayne and Shiori look shocked and confused at my arrival."
                "But luckily for me, Shiori catches on more quickly."
                show shiori normal
                shiori.say "Oh...oh yes, yes - he gets those!"
                shiori.say "But I should really speak to them myself."
                shiori.say "You know - check that he's not throwing up!"
                "All the talk of kids, blood and vomiting seems to sober Dwayne up."
                "He takes a step back from Shiori, looking a little green himself."
                mike.say "Oh, hey, Dwayne!"
                mike.say "I didn't see you there."
                mike.say "That must take you back to when Cassidy was a kid, huh?"
                mike.say "Always puking up her lunch, yeah?"
                mike.say "And all those stinky nappies too!"
                "Dwayne seems to break out in a sudden sweat."
                "Seriously, he doesn't look too good!"
                dwayne.say "Ah...right..."
                dwayne.say "Look, I gotta go to the bathroom."
                dwayne.say "Something's not sitting right..."
                hide dwayne
                show shiori normal at center with move
                $ game.flags.worksatisfaction -= 10
                $ game.flags.promoted -= 2
                "With that, he hurries off, leaving Shiori and I alone."
                mike.say "Sorry about that, Shiori."
                mike.say "I had to think on my feet back there!"
                show shiori happy
                shiori.say "Oh, thank you, [hero.name]."
                shiori.say "I'm ever so grateful for your help."
                shiori.say "Very grateful indeed!"
            "Ignore Shiori":
                "I'm not about to get involved in that little mess."
                "And it's time Shiori learned to stand up for herself."
                "I look away as quickly as I can."
                "And I try to make it look like I didn't catch her intent."
                "The last thing I see as I walk away is the look on Shiori's face."
                "Despite my best efforts, she knows full well I just left her hanging."
                $ shiori.love -= 10
                $ ignore_dwayne_flags = True
    scene bg black with dissolve
    pause 1
    $ game.pass_time(1)
    if ignore_dwayne_flags:
        call office_christmas_dwayne_sex from _call_office_christmas_dwayne_sex
    else:
        call office_christmas_sex from _call_office_christmas_sex
    return




label office_christmas_sex:
    play music "music/roa_music/santas_nice_list.ogg" loop fadeout .5 fadein .5
    scene bg breakroom with dissolve
    if any([g.sexperience for g in [aletta, audrey, lavish, shiori, cassidy]]) or (game.flags.dwaynedead and ("office_event_01" in DONE or "cherie_event_02" in DONE)):
        "I think it's time to actually have some real fun right about now."
        "So I scan the room for that certain special somebody."
        "And there she is, the girl that's been on my mind all day."
        menu:
            "Approach Aletta" if aletta.sexperience and aletta.love >= 50:
                "It's the perfect time to walk over there and make my intentions known."
                "So I do just that, whispering into her ear."
                mike.say "Follow me and don't ask any questions, yeah?"
                mike.say "I promise you this is going to be some serious fun!"
                play sound door_open
                scene bg personal with fade
                pause 0.3
                show aletta work normal at center, zoomAt(1.0, (640, 720))
                "Taking me by the hand, Aletta hurries into the empty office and closes the door behind us."
                queue sound door_close
                "Neither of us knows how long we have before somebody notices that we're gone."
                "But we're more than willing to try to sneak in as much fun as we can before they do!"
                "Luckily for us, the office that we've chosen has a sofa as well as a desk."
                "So at least we'll be comfortable for the amount of time we can steal for ourselves."
                "Aletta makes it to the sofa before me and sits down, patting the spot beside her."
                show aletta flirt work
                aletta.say "Come on, [hero.name]!"
                aletta.say "What are you waiting for?"
                "I'm trying to strip off my clothes as I follow behind her."
                "Tossing items of clothing aside as I get ever closer."
                mike.say "Give me a second, Aletta..."
                mike.say "I need to get out of this Santa costume!"
                mike.say "Don't you need to get undressed too?!?"
                show aletta topless with dissolve
                "By way of answer, Aletta un-buttons her top."
                "This allows her heavy breasts to spill out."
                "And they bounce invitingly upon her chest."
                "They're so hypnotic that I almost miss what she does next."
                show aletta naked with dissolve
                "Which is to pull down her panties and toss them at me!"
                aletta.say "You've worked hard this year."
                aletta.say "And I think you deserve a Christmas bonus!"
                aletta.say "Come and get it, [hero.name]!"
                "Right now it's something else that's good and hard."
                "Looking at Aletta, how could my cock not get stiff?"
                "I make to climb on top of her, but Aletta evades me."
                "And then she uses my confusion to her advantage."
                scene aletta cowgirl
                show aletta cowgirl office
                with fade
                "Before I know what's happening, I'm flat on my back."
                "And Aletta is clambering all over me!"
                "I look up at her face, amazed at what I see there."
                "The normally calm and aloof Aletta that I know is gone."
                "And in her place is someone that looks like her."
                "But her expression is all hunger and desire!"
                "As she pins me down and mounts me, Aletta slithers up my thigh."
                "At the same time, I can feel how wet she is down there."
                "She wants it as badly as I do - maybe more."
                "And she's going to make sure that she gets it too!"
                "All I can do is clap my hands on Aletta's haunches."
                "Then I hold on for dear life as she takes matters into her own hands."
                "I gasp as Aletta uses one hand to brace herself against me."
                "And with the other, she grabs hold of my cock."
                aletta.say "Mmm..."
                aletta.say "Good and hard - that's how I like it!"
                show aletta cowgirl vaginal
                "Then she pushes the head of my cock hard against her pussy."
                "I feel it slip and slide along her lips."
                play sexsfx1 slide_in
                show aletta cowgirl down
                "And then I gasp again, deeper this time, as it pushes inside of her."
                "But this time, Aletta gasps too."
                "Deeper and louder than me, becoming more intense with each passing second."
                "The further Aletta sinks down onto my cock, the more noise she makes."
                "By the time I'm as deep into her as I can go, she's almost crying out."
                "For a moment I'm genuinely worried that she'll attract unwanted attention."
                "That someone will hear her and come to investigate the noise."
                play sexsfx1 slide_out
                show aletta cowgirl raised
                pause 0.7
                play sexsfx1 slide_in
                show aletta cowgirl down
                "And so I begin thrusting in and out of her in earnest."
                play sexsfx1 slide_out
                show aletta cowgirl raised
                pause 0.7
                play sexsfx1 slide_in
                show aletta cowgirl down
                "To my relief, it seems to do the trick."
                play sexsfx1 slide_out
                show aletta cowgirl raised
                pause 0.7
                play sexsfx1 slide_in
                show aletta cowgirl down
                pause 0.7
                play sexsfx1 slide_out
                show aletta cowgirl raised
                pause 0.7
                play sexsfx1 slide_in
                show aletta cowgirl down
                "Aletta relaxes and settles into the rhythm I'm setting."
                "And at the same time, her cries turn into low moans."
                show aletta cowgirl pleasure
                aletta.say "Oh..."
                aletta.say "That's it..."
                aletta.say "Fuck me like that, [hero.name]!"
                aletta.say "Make me cum...please!"
                "Well, it is Christmas after all."
                "So I guess I should give Aletta exactly what she wants!"
                play sexsfx1 fuck_calm loop
                show aletta cowgirl raised
                pause 0.25
                show aletta cowgirl down at startle(0.05,-10)
                pause 0.25
                show aletta cowgirl raised
                pause 0.25
                show aletta cowgirl down at startle(0.05,-10)
                "I thrust upwards with renewed vigour and speed."
                show aletta cowgirl raised
                pause 0.25
                show aletta cowgirl down at startle(0.05,-10)
                pause 0.25
                show aletta cowgirl raised
                pause 0.25
                show aletta cowgirl down at startle(0.05,-10)
                "All the time holding Aletta tightly in my grip."
                show aletta cowgirl raised
                pause 0.25
                show aletta cowgirl down at startle(0.05,-10)
                pause 0.25
                show aletta cowgirl raised
                pause 0.25
                show aletta cowgirl down at startle(0.05,-10)
                "The effect is both instant and visible."
                play sexsfx1 fuck_moderate loop
                show aletta cowgirl raised ahegao
                pause 0.25
                show aletta cowgirl down bounce at startle(0.05,-10)
                pause 0.25
                show aletta cowgirl raised
                pause 0.25
                show aletta cowgirl down at startle(0.05,-10)
                pause 0.1
                show aletta cowgirl -bounce
                "Aletta's eyes roll back into her head."
                "Her tongue falls out of her mouth."
                "And her moans begin to sound almost delirious."
                "Well, that's what I see whenever I catch a brief glimpse of her face."
                "Because most of the time I'm in the shadow of Aletta's breasts!"
                show aletta cowgirl raised bounce
                pause 0.15
                show aletta cowgirl down at startle(0.05,-10)
                pause 0.15
                show aletta cowgirl raised
                pause 0.15
                show aletta cowgirl down at startle(0.05,-10)
                pause 0.15
                show aletta cowgirl raised
                pause 0.15
                show aletta cowgirl down at startle(0.05,-10)
                pause 0.1
                show aletta cowgirl -bounce
                "They bounce and sway above me the whole time."
                "And more than once they threaten to hit me square in the face!"
                "The sound of them is pretty impressive too."
                play sexsfx1 fuck_speed loop
                show aletta cowgirl raised bounce
                pause 0.15
                show aletta cowgirl down at startle(0.05,-10)
                pause 0.15
                show aletta cowgirl raised
                pause 0.15
                show aletta cowgirl down at startle(0.05,-10)
                pause 0.15
                show aletta cowgirl raised
                pause 0.15
                show aletta cowgirl down at startle(0.05,-10)
                pause 0.1
                show aletta cowgirl -bounce
                "Whenever they slap together, I hear a sound like someone clapping!"
                "By now it's not just me pulling Aletta onto myself."
                "She's pushing down onto me with all of her strength too."
                "Aletta grinds herself against me, almost desperately."
                show aletta cowgirl raised bounce
                pause 0.15
                show aletta cowgirl down at startle(0.05,-10)
                pause 0.15
                show aletta cowgirl raised
                pause 0.15
                show aletta cowgirl down at startle(0.05,-10)
                pause 0.15
                show aletta cowgirl raised
                pause 0.15
                show aletta cowgirl down at startle(0.05,-10)
                pause 0.1
                show aletta cowgirl -bounce
                "And I can tell that she's close to getting what she wants."
                "I don't know if it's just good timing."
                "Or if Aletta's pushing me over the edge too."
                play sexsfx1 fuck_sprint loop
                show aletta cowgirl raised bounce
                pause 0.15
                show aletta cowgirl down at startle(0.05,-10)
                pause 0.15
                show aletta cowgirl raised
                pause 0.15
                show aletta cowgirl down at startle(0.05,-10)
                pause 0.15
                show aletta cowgirl raised
                pause 0.15
                show aletta cowgirl down with vpunch
                pause 0.1
                show aletta cowgirl -bounce
                "But I can feel myself starting to cum as well!"
                "A few seconds later, Aletta goes stiff."
                "The expression on her face seems to freeze too."
                play sexsfx1 final_thrust
                show aletta cowgirl raised creampie cum with vpunch
                "And it's then that I shoot my load into her."
                with vpunch
                "The sound of Aletta's orgasm emerges from between gritted teeth."
                with vpunch
                "A gasping moan that comes out a little at a time."
                "She reminds me of a steam engine letting out pressure."
                "And I slow down at the same pace, feeling my muscles finally relax."
                aletta.say "Oh god..."
                aletta.say "Santa definitely came this year!"
                stop sexsfx1
                $ aletta.love += 2
                $ aletta.sexperience += 1

            "Approach Audrey" if audrey.sexperience and audrey.love >= 50:
                "It's the perfect time to walk over there and make my intentions known."
                "So I do just that, whispering into her ear."
                mike.say "Follow me and don't ask any questions, yeah?"
                mike.say "I promise you this is going to be some serious fun!"
                "As soon as she knows that we're going to sneak off and fool around, Audrey's onto it."
                play sound door_open
                scene bg personal with fade
                pause 0.3
                show audrey work normal at center, zoomAt(1.0, (640, 720))
                "She grabs me by the hand and leads the way to an empty office that's a little away from the party."
                queue sound door_close
                "There's barely enough time for me to slip in after her before she shuts the door tight."
                "And then I've barely turned around and she's already surveying the room for options!"
                show audrey normal work
                audrey.say "The desk's got WAY too much crap on it."
                audrey.say "And there's no way I'm doing it on the floor!"
                audrey.say "No, wait..."
                show audrey happy
                audrey.say "A sofa - perfect!"
                "Before I can utter as much as a single word, Audrey's off again."
                "And as she's still holding my hand, I have no choice but to follow in her wake."
                if audrey.flags.sexywork:
                    mike.say "Whoa..."
                    mike.say "Hold on a second, Audrey!"
                    mike.say "Don't we need to strip-off, first?"
                    "Audrey looks at me for a moment, and then she shakes her head."
                    "Her laughter isn't as cutting as I know she can make it sound."
                    "But I still get the impression that she's chiding me."
                    audrey.say "You might want to shed some of that Santa costume."
                    audrey.say "But I spent too much time on my outfit for that!"
                    scene audrey missionary
                    show audrey missionary office nomike
                    "As if to underline her point, Audrey lays back on the sofa."
                    "Then she spreads her thighs apart, showing off her panties."
                    "Holding my eye, she reaches down and tugs them aside."
                    "Not much, but just enough to let me see the lips of her pussy."
                    "And there's no mistaking the way they glisten in the light!"
                else:
                    "Tossing items of clothing aside as I get ever closer."
                    mike.say "Give me a second, Audrey..."
                    mike.say "I need to get out of this Santa costume!"
                    mike.say "Don't you need to get undressed too?!?"
                    show audrey topless
                    "By way of answer, Audrey un-buttons her top."
                    "This allows her heavy breasts to spill out."
                    "And they bounce invitingly upon her chest."
                    "They're so hypnotic that I almost miss what she does next."
                    "Which is to pull down her panties and lay back on the sofa."
                    scene audrey missionary
                    show audrey missionary office nomike naked
                audrey.say "Oh-ho!"
                audrey.say "I think he likes what he sees!"
                audrey.say "So how about it, [hero.name]?"
                audrey.say "If you want it for a Christmas present, then come get it!"
                "I only have the pants of my Santa costume off by now."
                "And I'm pretty sure this is the only way it could look more ridiculous."
                "But the sight of Audrey's pussy and the invitation she just gave me..."
                "Well, let's just say it's more than enough to make me forget about anything else!"
                "Within mere seconds I've all but pounced on Audrey."
                scene audrey missionary
                show audrey missionary office -nomike
                "I push her right leg down and her left leg up."
                "And then I waste no time in aiming my cock between them."
                "All the time I can hear Audrey laughing, urging me on."
                audrey.say "That's right..."
                audrey.say "That's what I want..."
                audrey.say "That's what I - oh god!"
                "Audrey's voice rises and then her words fade into moans."
                "Her body pushes upwards from the sofa beneath me."
                "And she pulls at the buttons of her top, freeing her breasts."
                show audrey missionary vaginal
                play sexsfx1 slide_in
                "All of this happens as I push my cock into her."
                "There's just the right amount of resistance as I do so."
                "Enough to make every moment feel intense and satisfying."
                "Once I can't go any deeper, I pause for a moment."
                "Audrey seems to feel it too, almost holding her breath in anticipation."
                "She nods, looking me straight in the eye as she does so."
                play sexsfx1 slide_out
                "Letting me know that she wants more of the same."
                play sexsfx1 slide_in
                "There's nothing slow or gentle about it from this point on."
                play sexsfx1 fuck_calm
                "The harder and faster I go, the more Audrey seems to like it."
                "And pretty soon I'm beginning to wonder if I can keep it up!"
                "But it's the I remember all the times that Audrey's teased me."
                "All the times that she taunted me to within an inch of losing it."
                "This is why she does it."
                "To make the moment of release that much sweeter!"
                play sexsfx1 fuck_moderate
                "Suddenly I feel a renewed surge of energy."
                "It flows through every inch of my body."
                "And Audrey seems to feel it too."
                "She nods, desperately this time."
                "But it's not like I need the encouragement."
                "I put every last drop of this unknown reserve into it."
                "Hammering away at Audrey like never before and not stopping for an instant."
                play sexsfx1 fuck_speed
                show audrey missionary pleasure
                "Soon enough, Audrey's moaning and crying out beneath me."
                "She's not begging for mercy or asking me to stop."
                "Instead the way she clings to me speaks only of need and desire."
                "We're both making enough noise to raise the dead by now."
                "But thankfully the sounds of the party are pretty loud too."
                "The music and laughter have only gotten louder as people get more drunk."
                "So we'd literally have to be smashing the place up to have a hope of being heard."
                play sexsfx1 fuck_sprint
                "Audrey looks up at me the whole time."
                "And I can see the look of defiance still in her eyes."
                "Even though she's the one getting pounded, she still keep it."
                "It's then that I get the notion to change things up a little."
                "To do something right at the end."
                "Something that'll wipe that look off of Audrey's face."
                "The moment that I feel myself starting to cum, I make my move."
                play sexsfx1 slide_out
                show audrey missionary -vaginal
                "Pulling my cock out of Audrey with no warning, I hear her gasp."
                "She starts to cum just a few seconds before I do."
                show audrey missionary cum with vpunch
                play sexsfx1 cum_outside
                "Which means that she's helpless as I shoot my load into her face."
                with vpunch
                "Eyes and mouth wide open, Audrey takes the whole thing."
                with vpunch
                "The streamers of semen stripe her forehead, cheeks and nose."
                "And not a small amount manages to land on her tongue too!"
                "Instinctively, Audrey closes her mouth and swallows."
                show audrey missionary -cumshot dickcum
                "Meaning that she also swallows what's on her tongue as well!"
                mike.say "Ha..."
                mike.say "Happy Christmas, Audrey..."
                mike.say "Hope you liked what was in Santa's sack this year!"
                stop sexsfx1
                $ audrey.love += 2
                $ audrey.sexperience += 1

            "Approach Lavish" if lavish.sexperience and lavish.love >= 50:
                "I walk over Lavish, whispering into her ear."
                mike.say "Follow me and don't ask any questions, yeah?"
                mike.say "I promise you this is going to be some serious fun!"
                "She nods and goes back to her previous occupation."
                "It takes a little while for Lavish to choose her moment, as she's networking as usual."
                "But eventually she manages to slip away from the hubbub of the party and take my hand."
                "Holding a finger to her lips with her free hand, she leads me towards an empty office."
                play sound door_open
                scene bg personal with fade
                pause 0.3
                show lavish work normal at center, zoomAt(1.0, (640, 720))
                "I follow eagerly, glancing back over my shoulder to make sure nobody sees where we're going."
                queue sound door_close
                "And a few moments later, the door closes, meaning that Lavish and I are alone at last."
                "I watch in anticipation as Lavish moans and stretches like a cat."
                "The motion shows off the shape of her body, displaying each and every curve."
                lavish.say "Mmm..."
                lavish.say "I thought we were never going to get away from the party!"
                "I can't help cocking my head on one side at this."
                "And Lavish seems to notice the question in my frown and furrowed brows before I say a word."
                mike.say "Huh?"
                mike.say "I thought you were having a great time?"
                mike.say "You looked like the life and soul of the party back there!"
                show lavish happy
                "Lavish smiles and shakes her head."
                "Then she lets out a little chuckle."
                lavish.say "Aw, [hero.name]!"
                lavish.say "That's just my business face."
                lavish.say "The one I put on when I need to be professional."
                lavish.say "Now this...this is my pleasure face!"
                show lavish flirt
                "I watch with fascination as a change comes over Lavish's face."
                "Her expression becomes suddenly more sultry and seductive."
                "I can't say exactly what she changes, but it has an instant effect."
                lavish.say "When I have my business face on, I'm all business."
                lavish.say "And when I have my pleasure face on..."
                lavish.say "Well, how about I show you?"
                "All I can do is nod like a fool at Lavish's suggestion."
                "Because I know that if I try to speak, I'll be lost for words."
                "But that seems to be more than enough for Lavish."
                "She lets out a little giggle and then takes my hand again."
                "This time she leads me over to the sofa in the corner of the office."
                "Once there, Lavish climbs onto it and kneels before me."
                "She looks up at me, her huge dark eyes staring into mine."
                "And slowly her mouth curls into a knowing smile."
                "All of which serves to distract me as she reaches for my waistline."
                "The first I know about Lavish's intentions comes when she pulls down my pants."
                "I'm still wearing my goofy Santa outfit, but that doesn't seem to bother her."
                "Lavish wastes no time in pushing my pants and shorts down to my ankles."
                "And then she turns her attention to what lies beneath."
                scene lavish bj
                show lavish bj office
                with fade
                lavish.say "Oh my!"
                lavish.say "Look what Santa brought me!"
                "I don't need to tell you that my cock's pretty hard by now."
                "And when Lavish reaches out to touch it, it gets harder still."
                "She begins to stroke the shaft, gently at first."
                "But then she leans in and starts to lick around my balls."
                "Before I know what's happening, Lavish is sucking on them too."
                "It tickles like crazy, but there's no way I'm telling her to stop!"
                "I can't help gasping as she wraps her tongue around them."
                "And for a moment, I feel like I might cum far too early."
                "As if sensing that it's too much for me, Lavish changes direction."
                "She lets my balls alone, instead kissing the base of my cock."
                "From there she climbs upwards, kissing and licking as she goes."
                "One of her hands still keeps my balls from feeling left out."
                "But now she caresses and plays with them almost as an afterthought."
                "And that's because she's paying so much attention to the shaft."
                "Lavish takes her time, inching ever upwards."
                "So by the time she gets to the top, I'm quivering with anticipation."
                "She makes sure to catch my eye before she goes any further."
                "And I can tell from the look she gives me that she knows."
                show lavish bj deep blow
                play sexsfx1 bj_sucking
                "She knows full well that she has me right in the palm of her hand."
                "A moment later, Lavish closes her eyes and swallows me whole."
                "And all I can do is stare at her as her head bobs up and down."
                "That and reach out with one hand, putting it behind Lavish's head."
                "I hold it more to support her than to offer encouragement."
                show lavish bj deep pleasure
                "As there's no sign of her losing enthusiasm any time soon!"
                "Lavish is taking me deep into her mouth every time."
                "And I can feel the sensation building inside of me."
                "One that tells me it won't be her that ends it."
                "Before I can get the words out to warn Lavish, it happens."
                show lavish bj deep creampie
                play sexsfx1 cum_inside
                "I shoot my load just as she takes me in deep."
                show lavish bj deep creampie pain
                "She has no time to react, only to rely on instinct."
                "Which means that Lavish struggles to swallow all that she can."
                "But all the same, she splutters and gasps."
                "And everything that she can't swallow seeps out from between her lips."
                stop sexsfx1
                mike.say "Whoa..."
                mike.say "Wow, Lavish..."
                mike.say "Everything in Santa's sack was for you!"
                $ lavish.love += 2

            "Approach Shiori" if shiori.sexperience and shiori.love >= 50:
                "I wait until the party is in full-swing to make my move, making sure that we won't be missed."
                "And then I hurry over to take Shiori by the hand, motioning for her to follow me and keep quiet."
                "Shiori looks this way and that, the familiar look of concern and worry spreading across her face."
                "But she makes no effort to resist as I lead her away from the party and towards an empty office."
                play sound door_open
                scene bg personal with fade
                pause 0.3
                show shiori work normal at center, zoomAt(1.0, (640, 720))
                "Shiori comes meekly after me, allowing herself to be ushered through the door without protest."
                queue sound door_close
                "And she waits patiently for me to close the door behind us once we're inside the office too."
                "I turn to face Shiori, finding her standing before me, wringing her hands."
                shiori.say "Oh, please, [hero.name]..."
                shiori.say "Couldn't this wait until after Christmas?"
                "I blink in surprise at the question."
                "I'm just not sure what Shiori means."
                "Or why she seems to scared right now either."
                mike.say "I'd rather not, Shiori."
                mike.say "I've been waiting all day to get you alone."
                mike.say "I don't know if I can wait until then!"
                "Shiori responds by clasping her hands and begging."
                "She looks up at me with genuine fear in her eyes."
                show shiori sad
                shiori.say "Don't just think of me."
                shiori.say "Think of Kanta too."
                shiori.say "Don't make his poor mother destitute at Christmas!"
                mike.say "Shiori..."
                mike.say "What in the hell are you talking about?!?"
                shiori.say "I...I thought..."
                shiori.say "When you wanted to talk in private..."
                shiori.say "That you were going to fire me or something like that!"
                mike.say "Oh god no!"
                mike.say "Shiori...no!"
                mike.say "I just wanted to fool around, you know?"
                mike.say "If you're up for it?"
                show shiori embarrassed
                "Suddenly I see Shiori's cheeks flush red."
                "And she puts her hand over her mouth as she gasps."
                shiori.say "Oh..."
                shiori.say "Oh dear..."
                "She swallows and looks away for a moment."
                "But then her head snaps back around and she looks me in the eye."
                show shiori normal
                shiori.say "Oh, [hero.name]."
                shiori.say "So long as you don't fire me."
                shiori.say "You can do anything you like to me."
                shiori.say "ANYTHING..."
                "Shiori's still blushing as I lead her over to the sofa."
                "And she lets me lay her down on her back with a smile."
                "I'm not about to let a chance like this pass me by."
                "So I waste no time in pulling off the pants of my Santa costume."
                "Sure, it feels a little weird getting down to it with the rest still on."
                "But my eyes are firmly focused on Shiori, rather than myself."
                scene shiori missionary2
                show shiori missionary2 office
                with fade
                "Shiori hastily pulls off her panties and spreads her legs."
                "All the time her eyes are fixed on my cock, wide with anticipation."
                "And she doesn't avert her gaze as I climb onto the sofa."
                "Instead she watches in fascination as it slips between her thighs."
                "Shiori only tears her eyes away a moment later."
                "Which is the precise second the head of my cock touches her pussy."
                "Then she looks up at me, two pairs of lips opening at the same time."
                shiori.say "Ah..."
                shiori.say "Yes...yes..."
                shiori.say "Please put your cock in me!"
                "Shiori's pussy is as pliant as the rest of her."
                show shiori missionary2 vaginal
                play sexsfx1 slide_in
                "And so it doesn't take long for me to give her what she wants."
                "But still I make sure to prolong the moment."
                "I push into Shiori an inch at a time, feeling each one as I go."
                "Shiori moans and whimpers at my efforts, nodding to urge me on."
                "And from the way she's biting her lip, I know they're sounds of pleasure."
                "Soon I'm as deep into Shiori as I can go."
                "I rest there for a few seconds, enjoying the sensation."
                "Shiori's pussy feels amazing as her muscles squeeze my cock."
                play sexsfx1 slide_out
                "And the feeling only gets better as I begin to move again."
                play sexsfx1 slide_in
                "Putting my hands on Shiori's thighs, I push down and into her."
                show shiori missionary2 pleasure
                "Shiori nods as I do this, almost desperate for more."
                play sexsfx1 fuck_moderate
                "She doesn't have to wait long, as I leap straight into it."
                "All of my weight is behind my cock as I pound Shiori."
                "And she takes everything that I have to give without complaint."
                "In fact, she soaks it up as quickly as I can provide it!"
                "Shiori keeps on nodding as I give it to her."
                "Letting me know that I can use her as I see fit."
                "Every part of her is moving now."
                "Her legs back and forth with my own motions."
                "And her heavy breasts bouncing around in sympathy too."
                play sexsfx1 fuck_speed
                shiori.say "Oh..."
                shiori.say "[hero.name]..."
                shiori.say "You're SO big!"
                shiori.say "You're going to make me..."
                show shiori missionary2 ahegao
                "Shiori cums a moment later, wriggling and writhing beneath me."
                "I don't know if it's the sight of her losing it."
                "Or whether the way her pussy squeezes me that does it."
                show shiori missionary2 creampie
                play sexsfx1 final_thrust
                "But either way I cum a second later, shooting my load into her."
                mike.say "Merry Christmas, Shiori."
                mike.say "You've been such a good girl."
                mike.say "Santa had to cum for you!"
                stop sexsfx1 fadeout 1
                $ shiori.love += 2
                $ shiori.sexperience += 1

            "Approach Cassidy" if cassidy.sexperience and cassidy.love >= 50:
                "The party's in full swing by the time Cassidy grabs a hold of my hand and pulls me away."
                "She takes me by surprise, and I stumble after her, bumping into a few bodies as I do so."
                "But by now there's been more than enough booze consumed for nobody to really care."
                "And enough to ensure that nobody notices us slipping away either."
                "Cassidy shows a surprising amount of knowledge as to how the place is laid out."
                "As she quickly and efficiently steers me towards an empty office that's nice and private."
                "So it seems Daddy's little princess was actually paying attention when she was last here."
                "And the whole show of huffing like a spoilt brat while staring at her phone was an act."
                play sound door_open
                scene bg personal with fade
                pause 0.3
                show cassidy b work normal at center, zoomAt(1.0, (640, 720))
                "Cassidy opens the door and hustles me into the empty office, closing the door behind us."
                queue sound door_close
                mike.say "Ah...what's the matter, Cassidy?"
                mike.say "Did you want to talk in private?"
                mike.say "Is there something on your mind?"
                "Of course I'm just trying to make myself look like good right now."
                "You know, like I care about her wellbeing and I'm not just a total perv?"
                "I know exactly what's on my mind."
                "And I'm hoping the same thing is on Cassidy's mind too!"
                show cassidy annoyed
                cassidy.say "Urgh!"
                cassidy.say "Don't give me that touchy feely crap!"
                cassidy.say "Not when I want it for real!"
                show cassidy a normal
                mike.say "Huh?"
                mike.say "What does that mean, Cassidy?"
                cassidy.say "Oh come on!"
                show cassidy wink
                pause 0.3
                show cassidy normal
                cassidy.say "You can't be that dumb!"
                show cassidy sadsmile
                cassidy.say "I mean that I want you to touch and feel me!"
                show cassidy at center, traveling(1.4, 1.0, (640, 960))
                "As if she needs to make her point even clearer, Cassidy grabs me by the collar."
                "And then she proceeds to yank me forwards until we're face to face."
                show cassidy kiss casual with dissolve
                "She plants her lips on mine, and I feel her tongue pushing into my mouth."
                "It's forward, aggressive and done totally without asking permission."
                "Cassidy's literally forcing herself onto me, which should be a bad thing."
                "But all I can think about is how hot she is and how much I want her right now!"
                "I grab hold of Cassidy's butt, pulling her hard against me."
                show cassidy a surprised
                play sound sasha_breathing loop volume 8
                "She breaks the kiss for a moment to let out a squeal of surprise."
                show cassidy wink
                pause 0.3
                show cassidy normal
                pause 0.5
                show cassidy kiss casual with dissolve
                "But then she instantly redoubles her efforts, grinding herself into me."
                "All I can think about is getting inside of her."
                "And if she keeps this up, I'm going to cum in my shorts!"
                "Luckily for me, it seems like Cassidy is thinking the same thing."
                show cassidy b normal
                stop sound fadeout 1.5
                "Because she breaks the kiss with a gasp of serious effort."
                "And then she grabs me by the collar for a second time."
                "But the difference is that now she's leading me towards the corner."
                "Towards the place where a couch is pushed up against the wall."
                show cassidy naked with dissolve
                "Once there, it only takes a few moments for us to undress."
                "And once we're finished tearing off our clothes, Cassidy takes over again."
                "She guides me down onto the sofa, firmly and brooking no argument."
                "And then she turns her back on me, looking at me over her shoulder."
                scene cassidy reverse cowgirl
                show cassidy reverse cowgirl office normal
                with fade
                cassidy.say "I know what goes on in an office, [hero.name]."
                cassidy.say "I know that people fuck each other all the time."
                cassidy.say "But I want you to remember fucking me here."
                cassidy.say "So I'm going to let you do something to me you'll never forget!"
                "With that, Cassidy bends over, pushing her ass towards me."
                play sound sasha_moans_light_low loop volume 8
                "She presses her buttocks together, moaning as she does so."
                "And then she lowers those magnificent cheeks until they're hovering over my cock."
                "Oh, maybe I should have mentioned that I have a raging boner right now."
                "But I guess I kind of thought that would be obvious!"
                "This means that there's not much distance separating the two to begin with."
                "And soon enough, the head of my cock is firmly sandwiched between Cassidy's buttocks."
                "She let's out a filthy giggle as she feels it, and begins to manoeuvre herself."
                "With a combination of sitting down and wriggling her ass, Cassidy takes control."
                "All I have to do is lie back and enjoy the show that she's putting on for me."
                stop sound fadeout 1.0
                play sexsfx1 slide_in
                show cassidy reverse cowgirl anal pleasure with dissolve
                "That and savour the sensation of my cock inching it's way into her ass."
                "Cassidy's incredibly tight down there, squeezing me mercilessly."
                play sexsfx1 slide_out
                "But that means it feels amazing as gravity wins out over her muscles."
                play sexsfx1 slide_in
                play sound sasha_moans_hard_low loop volume 10
                "Every inch that she sinks down, she lets out a deep, helpless moan."
                play sexsfx1 slide_out
                "And I swear that I can feel it in the way her ass quivers too."
                play sexsfx1 slide_in
                "As soon as I'm as deep into her as I can go, Cassidy sits down on me."
                play sexsfx1 fuck_calm loop
                "She raises her legs onto the sofa, and then begins to ride my cock."
                "I do all that I can to help, holding her up with both my hands."
                "But I have no idea if Cassidy even feels me doing this."
                "That's because she's already stopped looking back over her shoulder at me."
                show cassidy reverse cowgirl anal normal
                play sound sasha_moans_hard_medium loop volume 10
                play sexsfx1 fuck_moderate loop
                "And the only sounds coming out of her are helpless groans too!"
                "I keep on thinking that Cassidy's going to collapse onto me."
                "That the sensations she's feeling and the effort of it all will be too much."
                "But she proves me wrong by actually speeding up!"
                "I watch in disbelief as Cassidy begins to bob up and down, faster and faster."
                show cassidy reverse cowgirl anal pleasure
                play sexsfx1 fuck_speed loop
                "Her buttocks are slapping against my thighs, making an ever louder cracking sound."
                "And Cassidy's breasts are bouncing around like space-hoppers!"
                "If I didn't know we were so far away from the party, I'd be worried."
                "But the distance we put between them and us should be more than enough."
                show cassidy reverse cowgirl anal normal
                "So I don't hesitate to try and match Cassidy's efforts myself."
                "I thrust upwards with as much force as I can muster."
                "And she keeps on pushing down to meet me."
                "Cassidy really is moaning now, crying out as my cock probes her ass."
                show cassidy reverse cowgirl anal pleasure
                play sexsfx1 fuck_sprint loop
                play sound sasha_moans_hard_high loop volume 12
                cassidy.say "Oh..."
                cassidy.say "Oh fuck..."
                show cassidy reverse cowgirl anal ahegao
                cassidy.say "Give me an Xmas present, [hero.name]..."
                cassidy.say "Cum...inside of...my ass!"
                "Now, I ask you - how can I resist an invitation like that?"
                "Holding nothing back, I make one final push into Cassidy's ass."
                "And then I shoot my load, as deep in her as I can get."
                show cassidy reverse cowgirl anal creampie with vpunch
                play sexsfx1 final_thrust
                play sound sasha_moans_hard_orgasm loop volume 10
                "Cassidy's looking back at me in the same moment I cum."
                with vpunch
                "Which means I can see her eyes roll back into their sockets."
                with vpunch
                show cassidy reverse cowgirl anal normal
                "Cassidy's head lolls and sways as her body becomes limp."
                stop sound fadeout 2.0
                play sound sasha_breathing loop volume 6
                "Then she falls backwards like a rag-doll, landing atop me."
                "I do the best I can to guide her onto the couch."
                "She still tumbles over in a helpless tangle of limbs."
                "But at least I managed to keep her from landing on the floor."
                "Somewhere along the way, my cock pops out of Cassidy."
                "And she mumbles something unintelligible as she lies on the sofa."
                stop sound fadeout 3.0
                stop sexsfx1 fadeout 3.0
                "I leave her be for the moment, beginning to get dressed."
                "I just hope she can do the same when she finally recovers."
                $ cassidy.love += 2
                $ cassidy.sexperience += 1

            "Approach Cherie" if game.flags.dwaynedead and ("office_event_01" in DONE or "cherie_event_02" in DONE) and not (Person.find("cherie") and cherie.flags.isceo):
                "I've known that I wanted to do this almost from the first moment I realised Cherie was going to be at the party."
                "And since then I've been stuck waiting for my moment, just pretending to be having a good time."
                show cherie with dissolve
                "I've kept watching as she downs one drink after another, laughing at other people's terrible jokes."
                "And every look that Cherie's shot me across the room has been like torture for me to endure."
                "Because I know that look, it's the one she gives me when she's thinking about being alone with me."
                "She doesn't know she does it, and I'd never let on that I know she does it either."
                "But it lets me know that she's getting steadily more drunk and horny as the party progresses."
                "So when the time finally comes, I don't hesitate to seize the chance."
                "I walk over, taking Cherie by the hand, and then lead her towards a vacant office."
                "She follows without protest, but she doesn't seem to get the need to be discreet."
                play sound door_open
                scene bg personal with fade
                pause 0.3
                show cherie talkative at center, zoomAt(1.0, (640, 720))
                cherie.say "Oh..."
                cherie.say "There you are, [hero.name]..."
                cherie.say "I wanted to talk to you!"
                play sound door_close
                show cherie normal
                mike.say "Me too, Cherie, me too."
                mike.say "Let's go somewhere private - we can talk there, okay?"
                show cherie happy
                cherie.say "Ooh...that sounds good!"
                cherie.say "But if it's REALLY private, then we should fuck!"
                cherie.say "You do want to fuck me, don't you?"
                show cherie normal
                "I hustle Cherie into the empty office before I dare respond."
                "And only when I've managed to close the door behind us."
                mike.say "Of course I do, Cherie."
                mike.say "I've been waiting for the chance all night!"
                show cherie smile
                "Cherie practically beams at this admission."
                "She tries to look all sophisticated and seductive."
                "But the booze means that she just ends up looking comical instead."
                show cherie happy
                cherie.say "Oh dear..."
                cherie.say "I had a few small ones while I was waiting for you..."
                cherie.say "And I think I might be a tiny little bit drunk!"
                cherie.say "Are...are you going to take advantage of me?!?"
                show cherie smile
                "I open my mouth to reassure Cherie that my intentions are honourable."
                "But that's the very moment she chooses to stagger over to the desk."
                "Cherie tries to sit on it and cross her legs, hoping to entice me over."
                "Instead she ends up tripping and sprawling across the desk instead."
                "I rush to help as Cherie's dress rides up, showing off her ass."
                "The moment I lay my hands on her, it's clear she's misread my intentions."
                "Because she shoves her ass hard against me, grinding against my groin."
                show cherie happy
                cherie.say "I...I want to be taken advantage of..."
                cherie.say "Please, [hero.name]..."
                cherie.say "Take advantage of me?"
                show cherie flirt
                "It's only now that I look down and see Cherie's exposed pussy."
                "Either she was never wearing any panties to begin with."
                "Or else she somehow managed to slip them off as she staggered to the desk!"
                "I suppose how she did it isn't the important thing."
                "What holds me enthralled right now is the sight and scent of it."
                "I can see Cherie's lips glistening in the light."
                "And I can smell the musky perfume of it too."
                show cherie stand limp with fade
                "Before I have a chance to think about it, I have my cock out."
                "It feels like it's been hard for Cherie most of the night."
                show cherie stand -limp
                "And now it's like I'm finally unleashing it to find its prey!"
                "Ah...maybe that's too intense of an analogy..."
                "Let's just say that I'm finally giving it what it wants!"
                if renpy.has_label("cherie_achievement_0") and not game.flags.cheat:
                    call cherie_achievement_0 from _call_cherie_achievement_0
                show cherie stand vaginal opened
                play sexsfx1 slide_in
                "Cherie lets out an almost desperate whimper as I push it between her legs."
                "She nods, letting me lift one of her legs to spread her lips wider."
                "As ready as I am for Cherie, she's just as eager for me."
                "I feel only the tiniest hints of resistance as I tease her pussy."
                "And before I know it, my cock slips smoothly into her."
                "I don't stop until it's all the way in, as deep as I can go."
                show cherie stand closed
                "Cherie moans the whole time, nodding for me to keep going."
                "I stay there for as long as I can manage, just enjoying the sensation."
                "After waiting so long, I want to savour being inside of her."
                cherie.say "Mmm..."
                show cherie stand opened
                cherie.say "Oh, [hero.name]..."
                cherie.say "Your cock...it feels so good..."
                cherie.say "Fuck me...please?"
                play sexsfx1 slide_out
                "Slowly and surely, I start to move inside of Cherie."
                play sexsfx1 slide_in
                "I don't begin to pick up speed until she's already nodding again."
                "This time it's almost frantic, and it gets more intense the faster I go."
                show cherie stand closed
                play sexsfx1 fuck_moderate
                cherie.say "Oh fuck..."
                cherie.say "Oh fuck yes..."
                cherie.say "Harder...fuck me harder!"
                "There's no need for Cherie to ask."
                play sexsfx1 fuck_speed
                "I'm already dead set on fucking her brains out!"
                "And true to her being a cougar, she's almost clawing at the desk."
                "Cherie's nails scrape across the desktop, and I'm scared she'll gouge it too!"
                "But there's no way I'm stopping for the sake of office furniture."
                "Not when I'm this close to cumming!"
                "With one final thrust, I push all the way into Cherie's pussy."
                show cherie stand creampie with vpunch
                play sexsfx1 final_thrust
                "And then I lose it, letting go as I cum inside of her."
                with vpunch
                "Cherie groans and clings onto the desk as she begins to cum too."
                with vpunch
                "The muscles of her pussy twitch and contract around my cock."
                with vpunch
                "And it feels like she's trying to squeeze the last drop out of me."
                "When it's finally over, I notice that Cherie's still slumped over the desk."
                show cherie stand dickcum -vaginal -creampie
                play sexsfx1 slide_out
                "I pull my cock out of her hastily, afraid that she's passed out."
                "But then she groans and tries to bat away imaginary hands."
                "She may be the worse for all that she's drunk at the party."
                "But at least she's not fallen asleep while I was fucking her."
                "Because I don't know if my ego could have taken that blow!"
                stop sexsfx1
                if Person.find("cherie"):
                    $ cherie.love += 2
                    $ cherie.sexperience += 1
        scene bg black with dissolve
        pause 1
        $ game.pass_time(1)
    call office_christmas_conclusion from _call_office_christmas_conclusion
    return

label office_christmas_conclusion:
    scene bg breakroom
    "By the time we get back to the party, it seems to be winding down."
    "Everyone's either drunk too much, danced themselves out or both."
    "All that's left to do is wave a half-hearted goodbye to everyone still there."
    "And then I can phone a taxi to drive me back home, hopefully before I pass out."
    "Looking around at the state of the office, I don't envy the cleaners their task tomorrow morning."
    "But by then, I'll be too busy wrestling with my hangover to spare a thought for anyone else."
    call office_christmas_reset from _call_office_christmas_reset
    call sleep from _call_sleep_53
    $ game.room = "bedroom1"
    return

label office_christmas_reset:
    $ DONE.pop("christmas_invite", None)
    $ DONE.pop("office_christmas_arrival", None)
    return


label office_christmas_dwayne_sex:
    scene bg breakroom with dissolve

    if christmas_girl == aletta:
        "It's been a while since I saw Aletta getting hassled by Dwayne."
        "And there's no sign of her around the office as the party goes on."
        "I'm already feeling guilty that I didn't do anything to help her."
        "So I figure that the least I can do is look for her and make sure she's okay."
        "But I can't see Aletta anywhere and nobody seems to know where she went."
        "Well, they tell me they don't know, but they're being kind of weird about it too."
        "It's almost like they don't want to tell me everything they know."
        "I shake my head, realising that I can't see Dwayne either."
        "Maybe he knows where Aletta went?"
        "I decide to head to his office, thinking he might be there."
        "When I get to the door, I can hear noises coming from inside."
        "I almost turn to walk away, not wanting to disturb whoever's in there."
        "But the door's been left ajar, and I can't resist peaking through the gap."
        scene bg black
        show aletta ceofuck dwayne santa haircut noglasses vaginal
        with fade
        "And the moment I do so, I find out where both Aletta and Dwayne went."
        "She's sprawled on her back over the desk, legs spread apart."
        "He's leaning over her, the pants of his Santa costume down around his ankles."
        show aletta ceofuck dwayne at stepback(0.07, -10, 0)
        pause 0.2
        show aletta ceofuck dwayne at stepback(0.07, -10, 0)
        "I don't need to see Dwayne's ass moving back and forth to know what's going on!"
        "Aletta's the one facing me, and I can see that she's grimacing."
        "I don't know if she's in actual pain, but she's clearly not thrilled with this arrangement!"
        menu:
            "Walk away":
                "Part of me knows that I should barge in there and put a stop to it."
                "But I already chickened out of helping Aletta when Dwayne was hitting on her earlier."
                "And this is far more intense than that ever was!"
                "Plus, he's my boss - the CEO of the whole company too."
                "What choice do I really have?"
                scene bg breakroom with fade
                "So I creep backwards before Aletta can see me."
                "I guess I'll just have to live with the fact I'm that guy."
                "The one that saw it happen and didn't say a thing."
            "Step in":
                "This could be the end of my job here, even my whole career."
                "But I can't just stand back and watch this happen to Aletta!"
                "So I take a deep breath and walk into the office."
                mike.say "Hey, Dwayne..."
                mike.say "Everyone's looking for you, man!"
                "I hear Aletta cry out in horror at being seen in that position."
                "And Dwayne almost leaps away from her, cursing under his breath."
                scene bg ceo
                show aletta annoyed blush haircut noglasses naked at left
                show dwayne annoyed santa at right
                with hpunch
                mike.say "Oh shit..."
                mike.say "I'm so sorry, guys!"
                mike.say "I had no idea..."
                show dwayne shout
                dwayne.say "Nah, nah..."
                dwayne.say "It's okay, [hero.name]."
                dwayne.say "This isn't what it looks like, you understand?"
                show dwayne smile
                "I have no idea how it could be anything other than what it looks like."
                "But I nod all the same, thankful to have brought the whole thing to an end."
                $ aletta.sub += 5
                show dwayne annoyed
                hide aletta with easeoutleft
                "Aletta doesn't say a word, just grabs her things and hurries out of the office."
                "I don't think I've ever seen her look so vulnerable and ashamed of herself."
                "I follow her a moment later, not wanting to be alone with Dwayne a second longer."
                scene bg breakroom with fade
                "But once I'm outside in the corridor, Aletta's nowhere to be seen."
            "Watch":
                "Part of me knows that I should barge in there and put a stop to it."
                "But I already chickened out of helping Aletta when Dwayne was hitting on her earlier."
                "And this is far more intense than that ever was."
                "Plus, I can already feel myself getting hard as I watch!"
                "It's a mercy that I can't actually see Dwayne's manhood from this angle."
                "But as I'm almost looking over his shoulder, I've got a great view of Aletta!"
                "Her hair is loose, tumbling down her shoulders and over her chest."
                "And the latter is bare, thanks to her dress being pulled down too."
                show aletta ceofuck dwayne at stepback(0.07, -10, 0)
                pause 0.2
                show aletta ceofuck dwayne at stepback(0.07, -10, 0)
                "Aletta's breasts bounce and jiggle as Dwayne pounds her."
                "Her face is flushed red from a mixture of embarrassment and arousal."
                "I guess because she can't ignore the fact his cock is inside of her!"
                show aletta ceofuck dwayne at stepback(0.07, -10, 0)
                pause 0.2
                show aletta ceofuck dwayne at stepback(0.07, -10, 0)
                "I'm kind of disgusted with myself for keeping on watching."
                "But I've never seen Aletta in this kind of position before."
                "Normally she's a force around the office, arrogant and haughty."
                show aletta ceofuck dwayne pleasure at stepback(0.05, -10, 0)
                pause 0.15
                show aletta ceofuck dwayne at stepback(0.05, -10, 0)
                "Now she's been stripped of all that, totally humiliated."
                "I don't think I'll be able to look at her the same way again."
                show aletta ceofuck dwayne pleasure at stepback(0.05, -10, 0)
                pause 0.15
                show aletta ceofuck dwayne at stepback(0.05, -10, 0)
                "Dwayne doesn't slow down or stop for a moment."
                "He thrusts himself into Aletta without mercy."
                show aletta ceofuck dwayne pleasure at stepback(0.05, -10, 0)
                pause 0.15
                show aletta ceofuck dwayne at stepback(0.05, -10, 0)
                "She's moaning the whole time he's fucking her."
                "But when he looks like he's shooting his load, that changes."
                show aletta ceofuck dwayne pleasure at stepback(0.05, -10, 0)
                pause 0.15
                show aletta ceofuck dwayne santa creampie with hpunch
                "As Dwayne cums inside of her, Aletta begins to wail."
                show aletta ceofuck dwayne santa creampie ahegao with hpunch
                "She yelps and gasps, like she's cumming and can't do a thing about it."
                scene bg breakroom with fade
                "I choose that as my moment to retreat, fleeing before they're done."
                "The last thing I want is for either of them to see me!"

    elif christmas_girl == audrey:
        "I start to think that something's not right a little time after I saw Dwayne hitting on Audrey."
        "The both of them have vanished from sight and nobody seems to have any idea where they went."
        "With Dwayne I could just write it off as him not getting anywhere and moving onto his next target."
        "But in Audrey's case it raises a whole heap of questions, all of which are bugging me."
        "She's not the kind of girl to be embarrassed by what happened and sneak off home."
        "More likely she'd be making as much of it as she can, talking about suing and all that."
        "Actually, her getting lawyered up is a real possibility!"
        "I figure that I'd better find Dwayne and try to sober him up."
        "Don't get me wrong - I'm not taking his side over Audrey's in this."
        "I just don't want to lose my job over him getting too physical at an office party!"
        "The first place I think to check is Dwayne's office."
        "I know he keeps a flashy liquor cabinet in there, so maybe he's drowning his sorrows?"
        "Walking up to the open door, at first I think I'm right."
        "I can definitely hear the sound of someone inside."
        "But as I get closer, I can tell that it's not one person, but two."
        "Peeking through the crack in the door, I check out what's going on."
        "And I'm not prepared for the sight that greets me, not at all!"
        scene bg black
        show audrey missionary ceo dwayne santa vaginal
        with fade
        "Audrey lies on her back, sprawled over the desk."
        "Her clothes have been pulled at, exposing her breasts."
        "And her legs are spread apart, with Dwayne between them."
        "He has the pants of his Santa costume down around his ankles."
        show audrey missionary at stepback(0.07, -10, 0)
        pause 0.2
        show audrey missionary at stepback(0.07, -10, 0)
        "And he's busy pounding away at Audrey with all his might!"
        "I can't see Dwayne's face, which is a small mercy."
        show audrey missionary at stepback(0.07, -10, 0)
        pause 0.2
        show audrey missionary pleasure at stepback(0.07, -10, 0)
        "But the look on Audrey's is a mixture of shame and humiliation."
        menu:
            "Walk away":
                "I'm all set to barge into the office and tell Dwayne to back off."
                "But then I freeze on the spot, thinking about the consequences."
                "It's not just that Dwayne's my boss and the CEO of the company."
                "I had a chance to step in and try to save Audrey before, and I didn't."
                "Is she really going to thank me for doing it now?"
                "Especially after I've seen her with Dwayne's cock up her?"
                "No, the best thing is to just turn around and walk away."
                scene bg breakroom with fade
                "Which is just what I do, as quietly as possible."
                "I'm sure I can live with it - of course I can."
                "Stuff like this happens all the time."
                "And it's none of my business."
            "Step in":
                "Ah, fuck the consequences!"
                "I looked the other way before."
                "I'm not going to do it again."
                "Without giving myself time to think again, I walk into Dwayne's office."
                mike.say "Hey, Dwayne..."
                mike.say "Everyone's waiting for you to make a speech!"
                "Audrey lets out a cry at the sound of my voice."
                "But I'm sure I can hear a note of relief in there too."
                "But Dwayne almost leaps away from her, cursing under his breath."
                scene bg ceo
                show audrey naked stuned blush at left
                show dwayne annoyed santa at right
                with hpunch
                mike.say "Oh shit..."
                mike.say "I'm so sorry, guys!"
                mike.say "I had no idea..."
                show audrey shy
                show dwayne shout
                dwayne.say "Nah, nah..."
                dwayne.say "It's okay, [hero.name]."
                dwayne.say "This isn't what it looks like, you understand?"
                show dwayne smile
                "I have no idea how it could be anything other than what it looks like."
                "But I nod all the same, thankful to have brought the whole thing to an end."
                show audrey work with dissolve
                "Audrey's already up and making herself look decent."
                $ audrey.sub += 1
                show dwayne annoyed
                hide audrey with easeoutleft
                "She shoots Dwayne an evil glare and then hurries out of the door."
                "I give him an awkward nod and follow on her heels."
                "Outside, Audrey storms off and I make my way back at my own pace."
            "Watch":
                "If I were the hero of a movie, or even a videogame, I'd do something."
                "But I'm not - I'm just an average guy in an awkward situation right now!"
                "Well, maybe I'm more kind of a pervy guy."
                "Because I find that I can't stop myself from watching!"
                "It's not like I can see Dwyane's cock from here."
                "Which really helps!"
                "But I've got a pretty sweet view of Audrey on the desk."
                "I can see those thighs she likes to tease me with."
                "And her breasts, the ones she shows off like a pair of trophies."
                show audrey missionary at stepback(0.07, -10, 0)
                pause 0.2
                show audrey missionary at stepback(0.07, -10, 0)
                "They're bouncing up and down in time to Dwayne's thrusts."
                "Audrey has a look of helpless humiliation on her face too."
                "It's one I'm not used to seeing her pull, not at all."
                show audrey missionary at stepback(0.07, -10, 0)
                pause 0.2
                show audrey missionary at stepback(0.07, -10, 0)
                "Seeing her being the one that's embarrassed for a change."
                "For some reason that seems to get me excited."
                show audrey missionary at stepback(0.05, -10, 0)
                pause 0.15
                show audrey missionary humping at stepback(0.05, -10, 0)
                "Almost more excited than seeing her get fucked!"
                "I don't think I'll be able to look at her the same way again."
                show audrey missionary at stepback(0.05, -10, 0)
                pause 0.15
                show audrey missionary humping at stepback(0.05, -10, 0)
                "Dwayne doesn't slow down or stop for a moment."
                "He thrusts himself into Audrey without mercy."
                show audrey missionary at stepback(0.05, -10, 0)
                pause 0.15
                show audrey missionary humping at stepback(0.05, -10, 0)
                "She's moaning the whole time he's fucking her."
                show audrey missionary at stepback(0.05, -10, 0)
                pause 0.15
                show audrey missionary cum humping with hpunch
                "But when he looks like he's shooting his load, that changes."
                show audrey missionary ahegao with hpunch
                "As Dwayne cums inside of her, Audrey begins to wail."
                with hpunch
                "She yelps and gasps, like she's cumming and can't do a thing about it."
                scene bg breakroom with fade
                "I choose that as my moment to retreat, fleeing before they're done."
                "The last thing I want is for either of them to see me!"


























































































    elif christmas_girl == shiori:
        "I felt bad almost as soon as I turned my back and walked away from Shiori."
        "I shouldn't have left her to the mercy of a guy like Dwayne."
        "She looked like a cute little gazelle being stalked by a hungry lion!"
        "Hopefully Dwayne was just drunk and had forgotten about boundaries in the workplace."
        "All the same, I resolve to find Shiori and apologise, or at least check she's okay."
        "But that soon proves to be easier said than done, as I can't find her anywhere."
        "Everyone I ask hasn't seen her either, or else they have and won't tell me."
        "Because at the mention of the incident, some of the partygoers just clam up."
        "In the end I make the rounds of the office on my own, looking for Shiori."
        "Which is how I end up outside of Dwayne's office."
        "The door's ajar and I can hear noises coming from inside."
        "So I decide to see if the man himself is in there."
        "Maybe he'll know where Shiori's gotten to?"
        "Or maybe he'll have sobered up enough to be embarrassed by his behaviour?"
        "I look through the crack in the door."
        scene bg black
        show shiori missionary2 ceo dwayne christmas vaginal pleasure
        with fade
        "And I can't believe what I see inside!"
        "Dwayne's there alright, standing with his back to the door."
        "But the pants of his Santa costume are down around his ankles."
        "Shiori's in there too, sprawled across the desk on her back."
        "Her legs are spread apart and her breasts have popped out of her top."
        "Shiori's squealing and Dwayne's grunting."
        show shiori missionary2 speed bounce at startle(0.05,-10)
        pause 0.2
        show shiori missionary2 -speed -bounce at startle(0.05,-10)
        "And from the way they're moving, it's obvious what's going on."
        "Dwayne's fucking her, on his desk!"
        "No wonder nobody wanted to tell me what had happened to Shiori!"
        "They must have seen Dwayne getting his way with her!"
        menu:
            "Walk away":
                "If I felt bad for not helping Shiori out before, imagine how I feel now!"
                "She's ended up being a piece of meat for Dwayne to chew on!"
                "But what in the hell am I supposed to do about it?"
                "There's nothing technically wrong with two people fucking in an office?"
                "And all I'd be doing if I walked in there was humiliate Shiori even more!"
                "At least walking away means she can pretend like none of this ever happened."
                "It's not the best way this could end for anyone but Dwayne."
                "Yet that's the mess we've all ended up in."
                "And that's thanks to my not doing something when I could have."
                scene bg breakroom with fade
                "So I slowly turn and make my way back to the party."
                "Already wondering how I'm going to look Shiori in the face after this."
            "Step in":
                "Technically there's nothing wrong with two people fucking in an office."
                "And I know that I'm only doing this out of guilt for not stepping in earlier."
                "But that's how guy's like Dwayne get away with doing this shit."
                "They play on their authority and the fear of those beneath them."
                "And they'll always get away with it while people look the other way!"
                "Taking a deep breath, I push the door open and walk inside."
                "I can at least try to make it look like I walked in on them by accident."
                mike.say "Hey, Dwayne..."
                mike.say "You're needed back at the party."
                mike.say "It's time to make a speech..."
                "I let my words trail off, like I'm dumbstruck at what I'm seeing."
                scene bg ceo
                show shiori naked stuned blush at left
                show dwayne annoyed santa at right
                with hpunch
                "Dwayne lets out a curse under his breath and jumps back from the desk."
                "At the same time, Shiori gasps."
                "But I can't tell if it's from surprise or the sensation of him pulling out."
                mike.say "I'm so sorry, guys!"
                mike.say "I had no idea..."
                show shiori embarrassed
                show dwayne shout
                dwayne.say "Nah, nah..."
                dwayne.say "It's okay, [hero.name]."
                dwayne.say "This isn't what it looks like, you understand?"
                show dwayne smile
                "I have no idea how it could be anything other than what it looks like."
                "But I nod all the same, thankful to have brought the whole thing to an end."
                "Meanwhile, Shiori has clambered off the desk and tried to cover herself up."
                show dwayne annoyed
                $ shiori.sub += 1
                hide shiori with easeoutleft
                "She hurries out of the office and I follow her."
                "But not after I've given Dwayne a 'what the fuck?' stare."
                "Outside in the corridor, I look around for Shiori."
                "She's nowhere to be seen."
                "And I can't say that I blame her for disappearing."
            "Watch":
                "I know that the right thing to do would be to barge into the room."
                "Walk straight in there and make sure that Dwayne stops what he's doing."
                "But something stops me doing that and keeps me rooted to the spot."
                "Part of it could be nothing more than morbid fascination."
                "Or else me being enough of a closet pervert to get off on watching."
                show shiori missionary2 speed bounce fullbelly pock at startle(0.05,-10)
                pause 0.2
                show shiori missionary2 -speed -bounce -fullbelly -pock at startle(0.05,-10)
                "But there's also the sight of Shiori being humiliated right in front of me."
                "She's so meek and submissive around the office."
                "I've often caught myself wondering about that side of her."
                "About just how much she'd let me get away with if I tried it on."
                show shiori missionary2 speed bounce fullbelly pock at startle(0.05,-10)
                pause 0.2
                show shiori missionary2 -speed -bounce -fullbelly -pock at startle(0.05,-10)
                "I guess this is a pretty good measure of it!"
                "Luckily for me, with his back turned, I can't see Dwayne's face."
                "But I'm almost looking over his shoulder at Shiori as she sprawls on the desk."
                show shiori missionary2 speed bounce fullbelly pock at startle(0.05,-10)
                pause 0.2
                show shiori missionary2 -speed -bounce -fullbelly -pock at startle(0.05,-10)
                "Dwayne's pounding her mercilessly, making her jump with each thrust."
                "This in turn sends Shiori's huge breasts bouncing and jiggling."
                show shiori missionary2 speed bounce fullbelly pock at startle(0.05,-10)
                pause 0.2
                show shiori missionary2 -speed -bounce -fullbelly -pock at startle(0.05,-10)
                "I feel myself swallowing dryly as I stare at those fleshy globes."
                "I've eyed them up beneath Shiori's top so many time before now."
                show shiori missionary2 speed bounce fullbelly pock at startle(0.05,-10)
                pause 0.2
                show shiori missionary2 -speed -bounce -fullbelly -pock at startle(0.05,-10)
                "And seeing them on display like this is making me hard!"
                "Dwayne doesn't slow down or stop for a moment."
                show shiori missionary2 speed bounce fullbelly pock at startle(0.05,-10)
                pause 0.2
                show shiori missionary2 -speed -bounce -fullbelly -pock at startle(0.05,-10)
                "He thrusts himself into Shiori without mercy."
                "She's moaning the whole time he's fucking her."
                show shiori missionary2 speed bounce fullbelly pock at startle(0.05,-10)
                pause 0.2
                show shiori missionary2 -speed -bounce creampie with vpunch
                "But when he looks like he's shooting his load, that changes."
                show shiori missionary2 -pock ahegao with vpunch
                "As Dwayne cums inside of her, Shiori begins to wail."
                with vpunch
                "She yelps and gasps, like she's cuming and can't do a thing about it."
                scene bg breakroom with fade
                "I choose that as my moment to retreat, fleeing before they're done."
                "The last thing I want is for either of them to see me!"
    $ game.pass_time(1)
    scene bg breakroom with fade
    "By the time I get back to the party, it seems to be winding down."
    "Everyone's either drunk too much, danced themselves out or both."
    "All that's left to do is wave a half-hearted goodbye to everyone still there."
    "And then I can phone a taxi to drive me back home, hopefully before I pass out."
    "Looking around at the state of the office, I don't envy the cleaners their task tomorrow morning."
    "But by then, I'll be too busy wrestling with my hangover to spare a thought for anyone else."
    call office_christmas_reset from _call_office_christmas_reset_3
    call sleep from _call_sleep_121
    $ game.room = "bedroom1"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
