init python:
    Item("dwayne_corpse", display_name="Dwayne's corpse")
    Item("aletta_gun", display_name="Aletta's gun")

    Activity(**{
    "name": "cherie_cold_call",
    "display_name": "Visit Cherie",
    "label": "cherie_cold_call",
    "duration": 0,
    "icon": "cherie",
    "conditions": [
        IsDone("cassidy_cherie_next_steps"),
        IsHour(11, 14),
        HeroTarget(
            Not(OnDate()),
            MinStat("charm", 75),
            ),
        ],
    "music": "music/roa_music/focus.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "cherie_dwayne_confrontation",
    "label": "cherie_dwayne_confrontation",
    "conditions": [
        IsDone("cassidy_chat_about_cherie", "aletta_chat_about_cherie"),
        HeroTarget(
            HasRoomTag("mcoffice"),
            IsFlag("cherie_dwayneconfrontation")
            ),
        PersonTarget(cassidy,
            Not(IsPresent()),
            Not(IsHidden()),
            ),
        ],
    "priority": 1000,
    "do_once": True,
    })

    Event(**{
    "name": "cherie_first_call",
    "label": "cherie_first_call",
    "conditions": [
        IsDone("cherie_dwayne_confrontation"),
        IsHour(10, 22),
        HeroTarget(
            Not(OnDate()),
            HasRoomTag("home"),
            IsFlag("cherie_cheriecall")
            ),
        ],
    "priority": 1000,
    "music": "music/roa_music/focus.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "cherie_second_meeting",
    "label": "cherie_second_meeting",
    "conditions": [
        IsDone("cassidy_chat_about_cherie2", "aletta_chat_about_cherie2"),
        IsHour(10, 22),
        HeroTarget(
            Not(OnDate()),
            ),
        ],
    "priority": 1000,
    "music": "music/roa_music/focus.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "cherie_vault",
    "label": "cherie_vault",
    "conditions": [
        IsHour(22, 0),
        HeroTarget(
            Not(OnDate()),
            IsFlag("cherie_vault")
            ),
        ],
    "duration": 1,
    "priority": 1000,
    "music": "music/roa_music/focus.ogg",
    "do_once": True,
    })

    Event(**{
    "name": "cherie_trigger_vault",
    "label": "cherie_trigger_vault",
    "conditions": [
        HeroTarget(
            IsFlag("cherie_helping")
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Activity(**{
    "name": "dump_dwayne_corpse_mansion",
    "display_name": "Dump Dwayne's corpse",
    "label": "dump_dwayne_corpse_mansion",
    "duration": 4,
    "rooms": "mansion",
    "conditions": [
        InInventory("dwayne_corpse"),
        HeroTarget(
            Not(OnDate()),
            IsGender("male"),
            ),
        ],
    "music": "music/roa_music/focus.ogg",
    "do_once": True,
    "icon": "dwayne",
    })

    Activity(**{
    "name": "dump_dwayne_corpse_beach",
    "display_name": "Dump Dwayne's corpse",
    "label": "dump_dwayne_corpse_beach",
    "duration": 4,
    "rooms": "beach",
    "conditions": [
        InInventory("dwayne_corpse"),
        IsHour(20, 6),
        HeroTarget(
            Not(OnDate()),
            IsGender("male"),
            ),
        ],
    "do_once": True,
    "icon": "dwayne",
    })

    Activity(**{
    "name": "dump_dwayne_corpse_forest",
    "display_name": "Dump Dwayne's corpse",
    "label": "dump_dwayne_corpse_forest",
    "duration": 4,
    "rooms": "forest",
    "conditions": [
        InInventory("dwayne_corpse"),
        IsHour(20, 6),
        HeroTarget(
            Not(OnDate()),
            IsGender("male"),
            ),
        ],
    "do_once": True,
    "icon": "dwayne",
    })

    Activity(**{
    "name": "dump_aletta_gun_mansion",
    "display_name": "Dump Aletta's gun",
    "label": "dump_aletta_gun_mansion",
    "duration": 1,
    "rooms": "mansion",
    "conditions": [
        InInventory("aletta_gun"),
        HeroTarget(
            Not(OnDate()),
            IsGender("male"),
            ),
        ],
    "do_once": True,
    "icon": "aletta",
    })

    Activity(**{
    "name": "dump_aletta_gun_beach",
    "display_name": "Dump Aletta's gun",
    "label": "dump_aletta_gun_beach",
    "duration": 1,
    "rooms": "beach",
    "conditions": [
        InInventory("aletta_gun"),
        IsHour(20, 6),
        HeroTarget(
            Not(OnDate()),
            IsGender("male"),
            ),
        ],
    "do_once": True,
    "icon": "aletta",
    })

    Activity(**{
    "name": "dump_aletta_gun_forest",
    "display_name": "Dump Aletta's gun",
    "label": "dump_aletta_gun_forest",
    "duration": 1,
    "rooms": "forest",
    "conditions": [
        InInventory("aletta_gun"),
        IsHour(20, 6),
        HeroTarget(
            Not(OnDate()),
            IsGender("male"),
            ),
        ],
    "do_once": True,
    "icon": "aletta",
    })

    Activity(**{
    "name": "dump_aletta_gun_alley",
    "display_name": "Dump Aletta's gun",
    "label": "dump_aletta_gun_alley",
    "duration": 1,
    "rooms": ("street", "street2"),
    "conditions": [
        InInventory("aletta_gun"),
        IsHour(20, 6),
        HeroTarget(
            Not(OnDate()),
            IsGender("male"),
            ),
        ],
    "do_once": True,
    "icon": "aletta",
    })

    Activity(**{
    "name": "dump_aletta_gun_pond",
    "display_name": "Dump Aletta's gun",
    "label": "dump_aletta_gun_pond",
    "duration": 1,
    "rooms": "pond",
    "conditions": [
        InInventory("aletta_gun"),
        IsHour(20, 6),
        IsSeason(0, 1, 2),
        HeroTarget(
            Not(OnDate()),
            IsGender("male"),
            ),
        ],
    "do_once": True,
    "icon": "aletta",
    })

    Event(**{
    "name": "dwayne_corpse_reminder",
    "label": "dwayne_corpse_reminder",
    "conditions": [
        "game.week_day % 3 == 0",
        IsDone("cherie_vault"),
        IsHour(8, 12),
        HeroTarget(
            InInventory("dwayne_corpse"),
            IsFlag("dwayne_corpse_discovery_delay", False),
            IsFlag("handle_gun_body"),
            ),
        ],
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "dwayne_corpse_discovery",
    "label": "dwayne_corpse_discovery",
    "conditions": [
        IsDone("cherie_vault"),
        HeroTarget(
            IsRoom("livingroom", "housemap"),
            IsFlag("hasworked"),
            IsFlag("dwayne_corpse_discovery_delay", False),
            IsFlag("dwayne_corpse", "mansion", "beach", "forest"),
            ),
        ],
    "duration": 1,
    "priority": 1000,
    "music": "music/roa_music/focus.ogg",
    "do_once": True,
    })

    WakeUpEvent(**{
    "name": "dwayne_murder_mike_arrest",
    "label": "dwayne_murder_mike_arrest",
    "conditions": [
        IsDone("cherie_vault"),
        IsHour(4),
        HeroTarget(
            IsRoom("bedroom1"),
            InInventory("dwayne_corpse"),
            IsFlag("dwayne_corpse_discovery_delay", False),
            ),
        ],
    "duration": 1,
    "priority": 4000,
    "music": "music/roa_music/focus.ogg",
    "do_once": True,
    })

label cherie_trigger_vault:
    $ game.flags.cherie_vaultdelay = TemporaryFlag(True, 7, hook=[hook_set_flag, {"girl": game, "flag": "cherie_vault", "value": True}])
    return

label cherie_first_meeting_appointment(appointment=None):
    $ DONE["cherie_first_meeting_appointment"] = game.days_played
    "It takes a bit of time to get myself dressed up. It's not that putting on a tuxedo is hard, but everything has to be just right. These people will know if I did anything wrong, and I need this little plan to work."
    $ game.room = "mansion"
    scene bg mansionentrance with fade
    "I decide to take a private car rather than drive. It's a bit more expensive, but looks more impressive to be dropped off."
    scene bg mansion with fade
    "When I arrive at the party, it's mostly people I don't recognize wearing outfits and jewelry that cost more than my annual salary. Dwayne's family sure does hobnob with the super-wealthy. I don't feel like I fit in at all."
    "I mingle amongst the crowd for a little while, making casual small talk with CEOs, heirs to billion dollar fortunes, low level politicians looking for campaign contributions and the like."
    "I tell people I'm an executive at Dwayne's company, which isn't too far from the truth, and I try to look like I know what they're talking about when they discuss their yachts, or their investment portfolios, or their golf club memberships."
    if hero.charm >= 80:
        "Nobody {b}seems{/b} to notice I don't fit in."
    else:
        "A few people give me strange looks, but nobody actually says anything. After that I decide I need to try keeping to myself a bit."
    "All the while, I'm keeping an eye out, trying to find Cherie."
    "I realize that Cassidy didn't really describe her to me, so all I know is that I'm looking for a lonely woman old enough to be Cassidy's step-mother."
    show cherie with dissolve
    "And then I realize that the incredibly attractive woman with the two-tone hair and the gorgeous red dress I'm talking to, telling me about her jewelry in intricate detail, is named Cherie."
    mike.say "Excuse me, but did you say you're Dwayne's wife?"
    show cherie sadsmile
    "Her expression falls at the mention of his name. That can only be her."
    show cherie talkative
    cherie.say "I did not say that, no."
    show cherie normal
    "She speaks with a mild French accent. It's just a little shift in the vowels that gives away her origins."
    mike.say "Sorry. I work for Dwayne, and he mentioned you."
    show cherie smile
    "Her expression perks up just a little."
    show cherie talkative
    cherie.say "He actually spoke of me?"
    show cherie normal
    mike.say "A little bit, yeah. Doesn't everyone talk about their wife?"
    show cherie talkative
    cherie.say "Dwayne does not usually tell people about me. He says I embarrass him."
    show cherie normal
    mike.say "That seems like a terrible thing to say!"
    show cherie talkative
    cherie.say "Yes, it does, but that is the life."
    show cherie normal
    if hero.charm > 80:
        mike.say "I don't see how you could possibly embarrass him. You're without a doubt the most beautiful person in the room."
        if Person.find("cherie"):
            $ cherie.love += 2
        "She looks around, almost as though looking to see if she thinks I'm being honest or just flattering her."
        show cherie talkative
        cherie.say "You flatter me, but no, my days of being the most beautiful woman in the room are behind me now."
        show cherie normal
        mike.say "Hardly. You can't be a day over twenty nine!"
        show cherie smile
        "Cherie laughs; it's a gentle, lilting sound. It doesn't quite have the full weight of humor behind it, but instead is a polite laugh to humor me."
        show cherie talkative
        cherie.say "Please, sir, now you are making a fool of yourself."
        show cherie normal
        mike.say "If you think that, you're the one fooling yourself. But if you'd rather not hear how lovely you are, I'll keep it to myself and simply admire your beauty in quiet."
        "Her laugh disappears and turns into a genuine-seeming smile."
        show cherie talkative
        cherie.say "Oh, sir, it is too much. But who am I to tell such a bold young man to stay quiet? You are, after all, the guest in my home. You may say what you like."
    mike.say "Why do you stay with someone who would say such things about you?"
    "She shrugs and casually waves."
    show cherie talkative
    cherie.say "Where else would I go? My home is here. At least this way I have something. Without him I have nothing."
    show cherie normal
    mike.say "I'm sure a woman such as yourself could choose any man and charm him until the end of time."
    show cherie talkative
    cherie.say "Ah yes, but alas, the charms wear off by midnight. Like Cinderella, only the prince is a tyrant. Oh, dear, I should not say such things."
    show cherie normal
    mike.say "It is your home, I believe you can say what you like."
    show cherie talkative
    cherie.say "Ah, but it is his home as well, and I should not speak ill of a man in his own home."
    show cherie normal
    mike.say "Perhaps we should go elsewhere?"
    show cherie talkative
    cherie.say "Oh, so that I may speak ill of my husband freely?"
    show cherie normal
    mike.say "So that you can speak of anything you like."
    show cherie talkative
    cherie.say "I do not think that would be good for you. The only time Dwayne pays attention to me is when another man is also paying attention to me. He is powerful and quick to anger."
    show cherie normal
    mike.say "I'm not afraid of Dwayne."
    show cherie talkative
    cherie.say "No? Then you are brave, and a fool."
    show cherie normal
    mike.say "For beauty such as yours, I will happily play the fool."
    "Cherie swirls the drink in her glass and looks at me as though it's the first time she has really seen me tonight."
    show cherie talkative
    cherie.say "I appreciate the flattery, sir, but you play a dangerous game. Dwayne does not pull punches."
    show cherie normal
    mike.say "Like I said, I'm not afraid of Dwayne."
    show cherie talkative
    cherie.say "Then it is best that I retire for the evening, before I am the cause of your downfall. I would hate to have another destroyed soul upon my conscience."
    show cherie normal
    "She tosses back the rest of her drink and turns away from me. She takes one step before looking back at me over her shoulder."
    show cherie talkative
    cherie.say "May I have your name?"
    show cherie normal
    mike.say "[heroname]. [heroname] [hero.family_name]."
    show cherie talkative
    cherie.say "[hero.name]. That is a good name. I hope your life treats you well."
    hide cherie with easeoutright
    "She turns and disappears, quickly going up the stairs and into the private parts of the house, ignoring my protestations that I wasn't done speaking with her."
    "I wait around for a little while longer, but she does not reappear. And when I see Cassidy by herself, that means Dwayne is no longer distracted by his little girl."
    "That means I need to get out of here before I run into him."
    "So I head home. That was kind of a failure, but she did ask my name. Maybe there's an opening, and I just need to find a way to try again."
    $ game.room = "livingroom"
    $ game.pass_time(3, needs=True)
    return

label cherie_first_meeting_appointment_missed:
    $ DONE["cherie_first_meeting_appointment_missed"] = game.days_played
    "Shit, I missed the party and my chance to see Cherie. This could be bad."
    $ game.flags.cherie_missed = True
    return

label cherie_cold_call:
    "I admit I'm nervous, but I need to go see Cherie. I'm just going to have to bluster my way through this and hope she likes me."
    $ game.room = "mansion"
    scene bg mansionentrance with fade
    pause 1.0
    play sound door_bell
    scene bg door mansionentrance with fade
    "I arrive at the mansion and ring the bell. I tell the butler who answers the door that I'm there to see Cherie. He asks, in a rather surly manner, if I have an appointment."
    "When I respond that no, I don't have an appointment, he gives me a highly disapproving look, but asks who is calling and says he'll check to see if she is available."
    "After what feels like an eternity, he returns to the door and informs me that he will show me to her."
    scene bg mansion
    show cherie
    with fade
    "At the party, Cherie was immaculate; her clothing and makeup were all perfect. Seeing her here, though, she is less perfect. She must have put makeup on in haste."
    "It's not badly done, but it's not the consummate perfection it was the last time I saw her."
    show cherie talkative
    cherie.say "Why, [heroname] [hero.family_name], this is a most unexpected surprise."
    show cherie normal
    mike.say "A pleasant surprise, I hope!"
    show cherie talkative
    cherie.say "That remains to be seen, I imagine."
    show cherie normal
    "I do my best to pour on the charm and I offer her a slight bow as I speak."
    mike.say "Then my mission is clear: to ensure this surprise is as pleasant as possible."
    show cherie talkative
    cherie.say "So what can I do for you, [hero.family_name]?"
    show cherie normal
    mike.say "I came by to see if you'd like to go out to lunch with me."
    show cherie talkative
    cherie.say "Are you asking me on a date?"
    show cherie normal
    mike.say "Certainly not! This is just a lunch with a gentleman and a beautiful woman."
    show cherie talkative
    cherie.say "Strange, that sounds very much like a date."
    show cherie normal
    mike.say "I would never have the audacity to ask a married woman on a date."
    show cherie talkative
    cherie.say "Needless to say, I cannot go with you."
    show cherie normal
    mike.say "That is very disappointing. I was really looking forward to lunch with you."
    show cherie talkative
    cherie.say "It's not that I won't have lunch with you, it's that lunch is about to be served here. I can have Manfred set another place. If that won't ruin your plan too much?"
    show cherie normal
    mike.say "I think that will do nicely."
    "Cherie claps her hands together and smiles."
    show cherie talkative
    cherie.say "Magnificent! Remain here for a moment."
    show cherie normal
    "Cherie disappears for several moments, and then reappears."
    "She leads me through several of the incredibly impressive rooms of the house, and then into a cozy little solarium where I guess Manfred has already set the table for two."
    "Manfred, who is already there waiting, asks me to sit down."
    "Once seated, Cherie sits across from me and offers a smile that is both sad and intrigued."
    show cherie talkative
    cherie.say "So, what should we talk about on our {i}not date?{/i}"
    show cherie normal
    mike.say "You could tell me how someone as lovely as you could end up ignored by someone as clearly horny as Dwayne."
    show cherie talkative
    cherie.say "Now why would you say that about him?"
    show cherie normal
    mike.say "Let's just say the office gossip has a lot to say on the topic."
    "Cherie chuckles."
    show cherie talkative
    cherie.say "Yes, I am certain word of his exploits travels far and wide. Still, I would not speak ill of the man in his own home."
    show cherie normal
    mike.say "Then don't speak ill of him, simply tell the truth."
    show cherie talkative
    cherie.say "They are one and the same, my friend."
    show cherie sad
    mike.say "If the truth speaks ill of him, then it is his own fault, not yours. You cannot wrong him with honesty any more than he could wrong you by being a loving husband."
    show cherie talkative
    cherie.say "Well..."
    show cherie sad
    "Cherie picks up a glass in front of her and takes a sip. Judging by the olive, I think it's a martini, and judging by her eyes it may not be her first one today."
    show cherie talkative
    cherie.say "I suppose. Once upon a time...what feels a lifetime ago, I was the light of Dwayne's life, the apple of his eye. Second only to that brat he spawned."
    cherie.say "But for family, I was content to be second, because it was a very good second."
    cherie.say "But I suppose I should have known. Dwayne does not have as long an attention span as I had hoped."
    cherie.say "I do not know if his love for me dwindled or if it was never truly love at all, but either way, what was twice a day became every other day, then once a week, and then...not for months."
    cherie.say "Do not get me wrong, my friend, he gives me an amazing life. I could not ask for more. But it is a life devoid of love and passion."
    cherie.say "Dwayne ignores me, his brat abhors me, and I am left with no one."
    show cherie sad
    "I am silent, thinking about this, while Manfred places a plate in front of each of us, starting with Cherie."
    "It appears to be some kind of fancy seafood, with 3 or 4 lumps of something that may be scallop and a piece of lobster?"
    "As he sets down the plate, Cherie tosses back the rest of her martini. Manfred takes the empty glass without a word and disappears. We eat while we speak."
    mike.say "It seems criminal that you are left without attention."
    show cherie talkative
    cherie.say "Oh, there is attention, but anyone who offers it becomes an enemy to my husband. And he always wins."
    cherie.say "But enough about me, surely you did not come here to be depressed by my circumstances. And truly, what have I to be sad about? Look at this place."
    cherie.say "I have the best of everything. The best food, the best drink, clothing, jewelry, fashion."
    cherie.say "What more could a woman like me ask for?"
    show cherie normal
    mike.say "A little love would not hurt."
    show cherie talkative
    cherie.say "I suppose. So tell me, [heroname] [hero.family_name], what of you? Here I have shared my deepest regrets and all I know about you is that you work for the man I am speaking ill of."
    cherie.say "Perhaps you are here to punish me?"
    show cherie normal
    mike.say "Hardly! I work for Dwayne, but I've no love for the man."
    show cherie talkative
    cherie.say "No loyalty?"
    show cherie normal
    mike.say "I'm loyal to my people and my family. I manage a small team, and they are the ones I am concerned for."
    show cherie talkative
    cherie.say "Then you are especially vulnerable to him."
    show cherie normal
    "Manfred returns and sets another martini in front of her, and one in front of me. I hadn't asked for it and he hadn't asked me. I have a feeling he doesn't really want me here."
    show cherie talkative
    cherie.say "Thank you, Manfred. You may go."
    show cherie normal
    "The butler departs without a word."
    show cherie talkative
    cherie.say "You should leave now. He is going to tell Dwayne about this, and then Dwayne will probably fire you."
    show cherie normal
    mike.say "Dwayne can't fire me, at least not right now."
    show cherie talkative
    cherie.say "No? Why is that, then?"
    show cherie normal
    mike.say "Let's just say I have some leverage over him."
    show cherie talkative
    cherie.say "Ah. I hope it is a great deal of leverage, then."
    show cherie normal
    mike.say "It is."
    "Cherie's face tightens a little, and she narrows her eyes just a little."
    show cherie talkative
    cherie.say "What do you want from me, [hero.name]? Why are you here?"
    show cherie normal
    mike.say "Is it not enough to seek the company of a beautiful, dangerous woman?"
    show cherie talkative
    cherie.say "Perhaps it should be, but it is not, not when I learn you have leverage over my husband."
    show cherie normal
    mike.say "That is all I have to offer, I'm afraid."
    "She looks at me dubiously, and takes another drink. She sure can put down the martinis."
    show cherie talkative
    cherie.say "Are you the reason that Cassidy has been out of the house? She said something about having a job, and that seemed particularly odd."
    if cassidy.status == 'pet':
        cherie.say "And Dwayne said something about her new boss taking advantage of her."
        show cherie normal
        mike.say "Yes, she works for me."
        show cherie talkative
        cherie.say "And just how have you been taking advantage of her then?"
        show cherie normal
        mike.say "I've been training her to be...a better person. She treated people pretty terribly when we first met, and I've been...showing her what that's like."
        show cherie talkative
        cherie.say "Oh, my. That sounds positively salacious."
        show cherie normal
        mike.say "It...might be."
        show cherie talkative
        cherie.say "Well, I am happy if anyone can put that brat in her place."
        show cherie normal
        if Person.find("cherie"):
            $ cherie.love += 3
    else:
        cherie.say "And Dwayne said something about her having a new pet."
        show cherie normal
        mike.say "Well, we do have a bit of an arrangement, but that's evolving over time. She is finally learning how the world actually works."
        show cherie talkative
        cherie.say "How is that working out for you?"
        show cherie normal
        mike.say "It's actually quite pleasant, and she has occasionally found kindness for others. It's a start."
        show cherie talkative
        cherie.say "It sounds as though you have a long way to go."
        show cherie normal
        mike.say "Yes, that is true."
    show cherie talkative
    cherie.say "You are very curious, [heroname] [hero.family_name]."
    show cherie normal
    mike.say "I hope that is a good thing."
    "She shrugs, but there is a small smile on her lips as she does so."
    show cherie talkative
    cherie.say "It is a thing."
    cherie.say "And now our lunch is over, my friend, and I must go. I have...things to do."
    show cherie normal
    mike.say "I see."
    show cherie talkative
    cherie.say "Manfred will show you out."
    show cherie normal
    mike.say "I hope that I may see you again?"
    show cherie talkative
    cherie.say "Ah, so you think we had a good {i}not date{/i}?"
    show cherie normal
    mike.say "Perhaps I just feel that is criminal that your loveliness lacks attention, and I'm not afraid of Dwayne."
    show cherie talkative
    cherie.say "Indeed, I think you take joy in poking the bear."
    show cherie normal
    mike.say "Perhaps I do."
    show cherie talkative
    cherie.say "Very well. But please, do not show up unannounced here again."
    show cherie normal
    mike.say "Then how shall I reach you?"

    show cherie talkative
    cherie.say "I will contact you when I am ready."
    show cherie normal
    mike.say "Soon, I hope?"
    show cherie talkative
    cherie.say "Patience is a virtue."
    show cherie normal
    "I have to laugh at that."
    mike.say "I never promised you virtue."
    "Her lips make a little O shape, and perhaps for the first time since I've known her, there is true delight on her face."
    if Person.find("cherie"):
        $ cherie.love += 2
    scene bg street with fade
    "On the way home, I have a lot to think about. I've managed to get another meeting with her, but I'm not really closer to getting what I actually need from her."
    "Plus, I may have promised her something of a relationship. Cassidy told me if I needed to I could, but she isn't going to be happy about it. This could get complicated."
    $ game.room = "livingroom"
    $ game.flags.cherie_dwaynedelay = TemporaryFlag(True, 7, hook=[hook_set_flag, {"girl": game, "flag": "cherie_dwayneconfrontation", "value": True}])
    return

label cherie_dwayne_confrontation:
    show dwayne with easeinleft
    "Before I can even sit down and get started working, Dwayne steps into my office."
    play sound door_slam
    "He doesn't exactly slam the door as he closes it, but...let's just say he closes the door with authority, and no small amount of noise."
    show dwayne shout
    dwayne.say "[hero.name]."
    show dwayne normal
    mike.say "Yes, Dwayne?"
    show dwayne shout
    "Dwayne carefully and slowly clasps his hands in front of him, moving deliberately to make a show of being patient or something."
    dwayne.say "I would like to know what you've been doing at my home."
    show dwayne normal
    mike.say "As the CEO, I don't see how that's any of your business."
    show dwayne shout
    dwayne.say "As the owner of the home, it is absolutely my business."
    show dwayne normal
    mike.say "Well, as the owner of the home, you should make an appointment with my secretary to discuss the issue."
    show dwayne shout
    "Dwayne slams his fist down onto my desk so hard that the door rattles."
    dwayne.say "Maybe I should make an appointment with your face?"
    show dwayne normal
    mike.say "Why, Dwayne, are you threatening me?"
    if cassidy.status in ["pet", "sex slave"]:
        mike.say "Because I wouldn't think that you, of all people, should be threatening me. Not unless you'd like certain...events to happen that could cost you, big time."
        show dwayne shout
        dwayne.say "Be careful, son. I've been doing this business a lot longer than you have, and that thing you think you've got on me isn't going to last much longer."
        dwayne.say "And I'm willing to let all that go, except..."
        show dwayne angry
        dwayne.say "Stay"
        dwayne.say "The fuck"
        dwayne.say "Away from my wife!"
        show dwayne upset
        mike.say "Honestly, Dwayne, why do you care? I thought you were done with her. It sounds like she hasn't had sex in months!"
        mike.say "And honestly, that woman? How can you not do the horizontal tango with her at least twice a week? My God she's hot!"
        show dwayne vangry
        "Dwayne's expression goes from \"angry\" to \"about to explode like an old pre World War 2 cartoon\"."
        dwayne.say "If you touch her, I will end you. I will destroy you so thoroughly that you'll wish for death. And then maybe I'll grant you your last wish."
    else:
        show dwayne shout
        dwayne.say "Damn straight I am threatening you."
        mike.say "I'm pretty sure that I could sue you blind for firing me over...what is it you're threatening me about again?"
        show dwayne shout
        dwayne.say "Whatever it is you're doing with my wife!"
        show dwayne normal
        mike.say "I'm not doing anything with her, {b}Dwayne{/b}! Cassidy decided she wants to have a better relationship with her step-mother."
        mike.say "And she asked me to help."
        mike.say "Honestly, I'd think you'd want something like that. Your family is awfully dysfunctional and those two really need to kiss and make up."
        show dwayne upset
        "Dwayne's expression goes from \"angry\" to \"about to explode like an old pre World War 2 cartoon\"."
        show dwayne vangry
        dwayne.say "You shut your damn mouth, punk."
        dwayne.say "If you keep this up, I will end you. I will destroy you so thoroughly that you'll wish for death. And then maybe I'll grant you your last wish."
    show dwayne upset
    mike.say "Wow, Dwayne. Maybe you need some therapy. You seem to have some anger management issues. How do you run a company like that?"
    "He thrusts one long, thick finger almost into my face. He has more muscles in that one finger than I have in my leg. Yikes."
    show dwayne shout
    dwayne.say "This is your only warning."
    show dwayne upset
    mike.say "Yeah, okay. If you're done, I have work to do. Assuming you still care about this company's success?"
    "I know I sound nonchalant here about this, but between you and me, I'm trying not to piss myself. I really hope he can't tell."
    hide dwayne with easeoutleft
    "With a guttural growl, he turns and exits my office. This time, he {b}does{/b} slam the door, hard enough that one of the hinges actually breaks."
    "I wait a good thirty seconds, to make sure he's really gone, and then I collapse into my chair."
    "Holy fuck. For a moment there, I was sure he was going to hit me."
    "I really, really start to wonder if I'm in over my head now."
    $ game.flags.cherie_cheriecalldelay = TemporaryFlag(True, 2, hook=[hook_set_flag, {"girl": game, "flag": "cherie_cheriecall", "value": True}])
    return

label cherie_first_call:
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice")
    if not result:
        $ hero.cancel_event()
        return
    "When my phone goes off, the number is blocked. Ordinarily I'd send that straight to voice mail, but there's an outside chance..."
    mike.say "Hello?"
    cherie.say "Hello, [heroname] [hero.family_name]. I bet you did not think I was going to call?"
    mike.say "Cherie, my friend, I did not doubt for a second you would call."
    cherie.say "I'm not sure if I should be offended that you think we're friends, or that you think so highly of yourself that I would be unable to resist your charms."
    mike.say "You don't think we're friends?"
    "The line is silent for a moment, just long enough to get me concerned."
    cherie.say "Very well, {i}mon ami{/i}. Friends."
    mike.say "{i}Mon ami{/i}? I like that."
    cherie.say "I notice, however, that you do not protest how highly you think of yourself."
    mike.say "Guilty as charged, madame. It gets me into trouble at times, I must admit."
    cherie.say "Like now, I should think."
    mike.say "What makes you say that?"
    cherie.say "I am wondering what you said to my husband?"
    mike.say "Oh, you know. Work stuff, mostly?"
    cherie.say "The tingling in my nether regions would beg to differ with you."
    mike.say "I beg your pardon?"
    cherie.say "Whatever it is you said to him, I have not been...handled...so hard, nor so long in years. He was like a piston, and I am sore all over."
    cherie.say "Top to bottom, you might say."
    "Words fail me as images of that man pounding away at her flood my mind."
    mike.say "I, uh..."
    cherie.say "So whatever it is you said to him, {i}mon ami{/i}, has him quite...no, I should say extremely angry."
    mike.say "I should think that I have been very successful, then. The thing that has pained me since the moment I met you seems lessened now."
    cherie.say "And why do you say that?"
    mike.say "I've said it before, your loveliness must not go unappreciated! I am happy that I have convinced him to render his appreciation appropriately."
    cherie.say "Perhaps, but...it will be fleeting. Anger is not love. As soon as you are gone, then I shall be alone again."
    mike.say "Then I must endeavor not to be gone."
    cherie.say "No, {i}mon ami{/i}. I cannot allow that. I will not let him destroy you. As tempting as it is, as charming as your company has been, I will not have that on my conscience."
    cherie.say "I'm afraid that I must end our -- what are they? -- {i}not dates{/i} at once."
    "Oh shit. If she hangs up, I'm screwed. I don't have a number to call her back on."
    mike.say "Wait! I think that would be a grave mistake on your part."
    cherie.say "Allowing you and your sweetness to come to harm for my benefit would be a grave mistake. That is too much."
    mike.say "No, look, the bear is already poked. There's no unpoking it. It doesn't matter if I never see you again, he's never going to trust it."
    mike.say "Whatever he's going to do, he's going to do anyway."
    cherie.say "Perhaps, but--"
    mike.say "What if I said I had a plan to get you away from him?"
    cherie.say "Oh? Are you trying to say you want me for yourself? That's quite...forward."
    mike.say "No! That's not--I mean, look. One thing at a time, all right?"
    cherie.say "What are you proposing?"
    mike.say "Not over the phone. Can we meet? I'll explain everything."
    cherie.say "That would not be practical."
    mike.say "Not now. Some time when he's not around."
    cherie.say "Manfred will know."
    mike.say "Make up an excuse and leave. Or send him away. He can't be there all the time, can he?"
    cherie.say "He can. Though perhaps..."
    mike.say "Yes?"
    cherie.say "I don't know. Listen, if I call, there will be a brief opportunity. Can you be ready at a moment's notice?"
    mike.say "I can."
    cherie.say "Hmm. Very well. No promises, but...I will try."
    mike.say "Then it's a date."
    cherie.say "A {i}not date{/i}."
    mike.say "As you say."
    cherie.say "You are a most...interesting person, [heroname] [hero.family_name]. Whatever happens, I've felt more alive recently than I have in a long time."
    cherie.say "I look forward to the next chapter of our little...misadventure."
    cherie.say "Au revoir, {i}mon ami{/i}!"
    "And without waiting for my response, she disconnects."
    return

label cherie_second_meeting:
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice")
    if not result:
        $ hero.cancel_event()
        return
    $ renpy.dynamic("score")
    $ score = 0
    "When my phone goes off and it's a blocked number, I find myself hoping very much that it's Cherie."
    cherie.say "Hello, {i}mon ami{/i}."
    "And it is!"
    mike.say "Hello, mon Cherie!"
    "Cherie giggles pleasantly."
    cherie.say "Oh, [heroname] [hero.family_name], so forward! I definitely do not think it is safe to say that."
    mike.say "No? I thought I would try it out, as I like the sound of it."
    cherie.say "As do I, {i}mon ami{/i}, but it is, how do you say, putting the cart before the horse, no?"
    mike.say "I guess?"
    cherie.say "In any case, while this is enjoyable, there is little time. If you wish to have that conversation, you must come immediately."
    mike.say "It's safe? You're alone?"
    cherie.say "Yes, but perhaps not for very long. Enough time for you to tell me of your intrigues."
    mike.say "Then I am on my way."
    cherie.say "I...look forward to seeing you again, {i}mon ami{/i}."
    mike.say "Me too..."
    "I leave the pause dangling for a beat too long, before I decide not to go with \"mon Cherie\" again. But she knows I'm thinking it."
    mike.say "...Cherie."
    "She giggles again, and then disconnects."
    scene bg mansionentrance with fade
    "I get myself as quickly as I can to the mansion that she calls home. Driving up to it, I never fail to be impressed by its sheer size and grandeur."
    scene bg mansion
    show cherie
    with fade
    "When I see her, this is the happiest she's been in any of our various meetings. That alone pleases me."
    show cherie talkative
    cherie.say "Hello again, {b}mon ami{/b}!"
    show cherie normal
    "Seeing her, I don't quite know the proper way to greet her. And my hesitation means she takes the lead."
    "She steps forward and touches her left cheek to mine, making a kissing noise, and then repeats it on the other cheek."
    mike.say "Oh, what is that?"
    show cherie talkative
    cherie.say "That is how we say hello where I grew up!"
    show cherie normal
    mike.say "Oh! Do you do that with everyone then?"
    show cherie talkative
    cherie.say "Not as much as I once did, no, but you have me feeling a little nostalgic."
    show cherie normal
    "I offer her a broad smile."
    mike.say "I shall take that as a compliment."
    show cherie talkative
    cherie.say "And indeed you should!"
    cherie.say "Now then, you must tell me all of your intrigues before Manfred returns."
    show cherie normal
    mike.say "I don't think I have time to tell you about all my intrigues, but--"
    show cherie talkative
    cherie.say "Oh, you have so many? Perhaps I am mistakenly getting acquainted with James Bond?"
    show cherie smile
    "I laugh aloud at that!"
    mike.say "Heavens no, but...there is a lot going on."
    show cherie talkative
    cherie.say "Very well. What do you have time to tell me?"
    show cherie normal
    mike.say "I have a plan that will put Dwayne in jail for the rest of his life. You'll be free of him. Free to pursue a life."
    show cherie talkative
    cherie.say "Ah, you wish to frame him?"
    show cherie normal
    mike.say "Absolutely not. He is one hundred percent guilty of the crimes he'll go to jail for."
    show cherie talkative
    cherie.say "I see."
    show cherie normal
    "There is a brief pause while she thinks about this."
    show cherie talkative
    cherie.say "The question remains, then, why are you speaking with me about it?"
    cherie.say "It seems to me that if you can put my husband in jail, and he is truly guilty and deserves to be there, this should already be done, no?"
    show cherie normal
    mike.say "There's the rub."
    show cherie talkative
    cherie.say "Ah, the other shoe. It is about to drop."
    show cherie normal
    mike.say "Well, I have almost everything I need, but there's one thing I do not have."
    "Her eyes narrow, and suspicion and mistrust cloud her face."
    show cherie talkative
    cherie.say "That would be?"
    show cherie normal
    mike.say "He keeps a second set of accounting ledgers that he needs to properly manage his wide array of illegal operations and embezzlement."
    "Cherie's expression falls. I can see in her face she knows where this is going."
    show cherie talkative
    cherie.say "And you want me to acquire this for you?"
    show cherie normal
    mike.say "No, but you can get me access to where it's kept."
    show cherie talkative
    cherie.say "Why do you think I would be able to do that?"
    show cherie normal
    mike.say "Because it's in his private vault in his office, and you have the combination."
    "Her eyebrows go up."
    show cherie talkative
    cherie.say "What would make you believe that I have that?"
    show cherie normal
    mike.say "Cassidy knows."
    show cherie talkative
    cherie.say "Ahh, so you are working with the brat as well? That is curious. Why would she work with you against her own father? She worships him."
    show cherie normal
    mike.say "There is no hate quite so strong as that of one who feels betrayed."
    show cherie talkative
    cherie.say "Oh, and what did my husband do to the delight of his eye? I think she is the only person in the world he truly cares about."
    show cherie normal
    mike.say "He lied to her about her mother."
    show cherie talkative
    cherie.say "So?"
    show cherie normal
    mike.say "He paid her to leave and never speak to Cassidy again. She is furious."
    show cherie talkative
    cherie.say "So let me get this straight."
    cherie.say "The brat with whom I've had to compete for his affection for the entirety of my marriage--and mind you, I've lost that competition every time--"
    cherie.say "She sent you to to charm me into betraying my husband, her father, to get secret information that could destroy him and lead to financial ruin."
    cherie.say "And I am expected to throw myself at your feet, grateful for the charming, smiling Mister [heroname] [hero.family_name] for saving me from my own loneliness?"
    show cherie normal
    mike.say "That's not it at all."
    show cherie talkative
    cherie.say "Oh, please, {b}mon ami{/b}, set me straight. I cannot wait to hear this."
    show cherie normal
    "The tone in her voice has turned bitter and dangerous. I can feel this spinning out of control."
    mike.say "She didn't send me, I came for myself. She did make it possible for me to come. And she is not the only one whose interests I'm working for here."
    mike.say "Your husband has forced my boss into a sexual relationship she doesn't want, and will destroy her life if she doesn't perform for him."
    show cherie talkative
    cherie.say "Hah! That's just like him, too."
    show cherie normal
    mike.say "And the company I work for? He's taking millions away from it every year that should be going toward the company."
    mike.say "And finally, he tried to set {b}me{/b} up as his patsy."
    show cherie talkative
    cherie.say "Ah, so it is revenge too?"
    show cherie sadsmile
    "She sighs."
    show cherie talkative
    cherie.say "I was foolish to think that your charms, so expertly aimed at me, were real."
    show cherie sadsmile
    menu:
        "Ma Cherie, They are real!":
            mike.say "Ma Cherie, They are real! Nothing I've said to you is untrue."
            "She scowls and points at me."
            show cherie talkative
            cherie.say "Do not call me that, not now."
            show cherie normal
            mike.say "I am sorry, but..."
            show cherie talkative
            cherie.say "Yes, you should be sorry. I should be sorry too, for daring to feel."
            show cherie normal
            mike.say "Cherie..."
        "Look, it's complicated":
            mike.say "Look, it's complicated. There's a lot going on. But I've been completely honest with you."
            show cherie talkative
            cherie.say "Honest? I don't know."
            show cherie normal
            mike.say "Tell me anything I've said that is wrong and I will correct the record immediately."
            show cherie talkative
            cherie.say "Perhaps...perhaps I've just been too eager to see something. You saw that I am lonely, and, yes, a little attention and I ate it up."
            show cherie normal
            mike.say "I could hardly ask you, straight away, for the combination to his secret vault."
            $ score += 1
    "She turns away from me and takes a step toward one of the hallways."
    show cherie talkative
    cherie.say "I need a drink."
    show cherie normal
    menu:
        "Stop her physically":
            "I step forward and put my hand on her wrist, pulling her arm toward me. As she takes a step this turns her entire body and suddenly she is facing me again."
            show cherie angry
            cherie.say "You dare lay a hand on me?"
            show cherie sad
            "This is a gamble, but Cassidy mentioned some of her sexual preferences. If she doesn't respond the way I think, I'm fucked, but..."
            "Still holding her wrist, I step up until I'm mere inches from her face, looking just a little down at her."
            mike.say "If you leave now, you'll be stuck in this emptiness forever. If you work with me, there is an escape."
            "Her nostrils flare. She's angry, but I believe she's aroused as well."
            show cherie talkative
            cherie.say "Alone with him and alone without him are very much the same, only one does not have my every need attended to."
            show cherie normal
            mike.say "Every need except the most important. And..."
            "I slip my hand from her wrist down, taking her hand in mine."
            mike.say "I do not think you'll be alone without him."
            show cherie talkative
            cherie.say "Do not make promises, {i}mon ami{/i}."
            show cherie sad
            menu:
                "I'll make sure you're not alone":
                    $ score += 1
                    mike.say "I'll make sure you're not alone."
                    show cherie sadsmile
                    "She squeezes my hand once, then pulls it away. I let her."
                    $ game.flags.cherie_promisednotalone = True
                "No promises, then":
                    mike.say "No promises, then. But don't sell yourself short."
                    mike.say "A woman as ravishingly beautiful as you won't be alone."
        "Ask her to wait":
            mike.say "Wait, Cherie. Please don't go yet."
            show cherie talkative
            cherie.say "Oh? Have you more lines to sell me?"
            show cherie normal
            mike.say "No, I don't want you to walk away from the rest of your life."
            show cherie talkative
            cherie.say "What rest of my life?"
            show cherie normal
            mike.say "The one that you're missing out on, {b}right now{/b}."
            "She closes her eyes, but she does pause."
            show cherie talkative
            cherie.say "You ask me to betray him for a small hope of freedom."
            show cherie normal
            mike.say "Not a small hope. A very large hope."
            show cherie talkative
            cherie.say "I am not a betrayer."
            show cherie normal
            mike.say "He has done nothing but betray you. Why should he deserve your loyalty?"
            show cherie talkative
            cherie.say "It's not about what is deserved."
            show cherie normal
            mike.say "He takes another woman against their will while you pine for even an acknowledgement."
            mike.say "What he deserves is not loyalty. He deserves prison."
            show cherie talkative
            cherie.say "And you're the man to put him there?"
            show cherie normal
            mike.say "With your help."
    "She looks up at me and all sorts of emotions flitter through her eyes. Fear, anger for sure. Perhaps desire. And a lot of weariness."
    show cherie talkative
    cherie.say "You should go now."
    show cherie normal
    mike.say "But..."
    show cherie talkative
    cherie.say "No buts. Go."
    show cherie normal
    mike.say "I need that--"
    show cherie talkative
    cherie.say "Shut up right this second. I might call you."
    show cherie normal
    mike.say "I--"
    show cherie talkative
    cherie.say "But only if you go. Right. Now."
    show cherie normal
    "Fuck, I don't know how to take that ultimatum."
    mike.say "Fine."
    "I turn and walk toward the door. Moving very slowly, giving myself time to think if there's one more thing I can say."
    show cherie talkative
    cherie.say "{i}Mon ami{/i}..."
    show cherie normal
    "I answer without turning back, just slightly hopeful."
    mike.say "Yes?"
    show cherie talkative
    cherie.say "If I ask you to take me to my bedroom and make passionate love to me, right now, will you?"
    show cherie normal
    menu:
        "Don't hesitate. Yes":
            $ game.flags.cherie_promisedsex = True
            "Without even thinking about it, I answer."
            mike.say "Yes."
            show cherie talkative
            cherie.say "Why?"
            show cherie normal
            mike.say "Because you are charming, and beautiful, and making love with you is a memory I would cherish forever."
            show cherie talkative
            cherie.say "I see."
            show cherie normal
        "Hesitate. Yes":
            $ game.flags.cherie_promisedsex = True
            $ score += 1
            "I think about my answer for a few seconds."
            mike.say "Yes, yes I will."
            show cherie talkative
            cherie.say "Why did you hesitate?"
            show cherie normal
            mike.say "Truly? I wasn't sure if you wanted me to say yes or not."
            show cherie talkative
            cherie.say "Oh, so you were thinking about what it is I want?"
            show cherie normal
            mike.say "Well, I know what I want."
            cherie.say "Mmm."
        "No":
            mike.say "No, I will not."
            show cherie talkative
            cherie.say "Why not?"
            show cherie normal
            mike.say "Because there is no time. Manfred will be back soon, and I would not want such an opportunity to be over so swiftly."
            show cherie talkative
            cherie.say "Ah. And if we have the time? Perhaps Manfred will not be back so soon as I led you to believe."
            show cherie normal
            mike.say "Is that what you want?"
            show cherie talkative
            cherie.say "What I want is for you to answer."
            show cherie normal
            menu:
                "Yes":
                    $ game.flags.cherie_promisedsex = True
                    mike.say "If there is time, then I am yours for the taking."
                    show cherie talkative
                    cherie.say "How very thoughtful of you."
                    show cherie normal
                "No":
                    $ score += 1
                    mike.say "I'm afraid the answer is still no."
                    show cherie talkative
                    cherie.say "Why not?"
                    show cherie normal
                    mike.say "Because if and when I do make love to you, I want it to be after your husband is no longer your husband."
                    mike.say "I want it to be after you are free to choose whomever you are with."
                    mike.say "Then--and only then--when you've freely chosen that you want to be with me, then I might say yes."
                    show cherie talkative
                    cherie.say "Oh. Oh my."
                    show cherie normal
    if score >= 2:
        $ game.flags.cherie_helping = True
        show cherie talkative
        cherie.say "Very well, {i}mon ami{/i}. I will call you. I will give you what it is you want. Everything."
        hide cherie with easeoutright
        "And with that, she quickly exits the room."
        show screen message(title="⚠️ WARNING ⚠️",what="Cherie's story may become a little challenging after this point.\nWe advise you to make a save before progressing further in her story.")
        pause
        hide screen message with dissolve
    else:
        show cherie talkative
        cherie.say "Good-bye, [heroname] [hero.family_name]. Manfred will be here in about five minutes. Be certain that you are not here when he arrives."
        hide cherie with easeoutright
        "And with that, she quickly exits the room. I'm left with a sinking feeling in my gut. I have failed here, and I don't know what to do next. Cassidy won't be pleased."
    $ game.room = "livingroom"
    $ game.pass_time(2, needs=True)
    return

label cherie_vault:
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice")
    if not result:
        $ hero.cancel_event()
        return
    "As soon as my phone rings and I see it's Cherie, I feel my heart flutter."
    "And I almost fumble and drop the thing as I hurry to answer the call."
    cherie.say "{i}Bonjour, mon ami{/i}!"
    "I find that my heart becomes even more aflutter as soon as I actually hear Cherie's voice."
    mike.say "It's so good to hear your voice, {i}ma Cherie{/i}!"
    "Cherie giggles at my attempt to speak a little of her native language."
    "And it's in a far more girlish fashion than I would have expected."
    cherie.say "{i}Ahh, mon ami{/i}..."
    cherie.say "You always make me feel so..."
    cherie.say "How do you say...young again!"
    "For a moment I think that's the way the call is going to go."
    "Just Cherie and I swapping pleasantries and flirting back and forth."
    "But then her tone changes in an instant."
    cherie.say "But!"
    cherie.say "Enough of these sweet nothings..."
    cherie.say "We have business to attend to, you and I!"
    "The sudden change kind of throws me off a little."
    "But I do the best I can to pretend like it's nothing."
    mike.say "Oh yeah?"
    cherie.say "Of course, oh yes!"
    cherie.say "My husband is not here."
    cherie.say "Now is your opportunity, {i}mon ami{/i}."
    cherie.say "As promised, I will reveal all of his secrets to you."
    cherie.say "But only if you come immediately!"
    "Now all pretence of hiding my reaction is gone."
    "Because Cherie's right, this is the chance I've been waiting for."
    mike.say "Of course, mon Cherie!"
    mike.say "I'm already on my way!"
    "Well, maybe that's not strictly true."
    "Because after she hangs up, I instantly text Cassidy and Aletta to clue them in too."
    scene bg mansionentrance with fade
    "Only then do I head over to Dwayne's mansion, as quickly as I possibly can."
    $ game.room = "mansion"
    scene bg mansion
    show cherie
    with fade
    "And it seems that Cherie's just as eager as I am."
    "Because when I arrive, she's already waiting to meet me."
    show cherie talkative
    cherie.say "Good, {i}mon ami{/i}, you came quickly."
    show cherie normal
    "I shrug, doing the best I can to make it look like nothing."
    mike.say "You called, I came."
    mike.say "That was the deal, right?"
    "Cherie looks me up and down, almost like she's seeing me in a new light."
    cherie.say "Mmm..."
    show cherie talkative
    cherie.say "Yes...yes it was."
    cherie.say "And a good deal for me, I think."
    show cherie normal
    "Cherie underlines the point by offering me a wink."
    "Which, in turn, gives me the confidence to answer her in kind."
    mike.say "Hello..."
    mike.say "Someone's feeling a little frisky!"
    "Cherie raises one eyebrow and gives me a shake of the head."
    "One of those expressions that only a French woman seems to be able to pull off."
    "One that at once says everything and nothing at all."
    show cherie talkative
    cherie.say "What can I say?"
    cherie.say "The excitement of this...what would you call it?"
    cherie.say "This caper?"
    cherie.say "Hmm...this does have the feel of a caper."
    show cherie normal
    "I'm not so sure I'd have chosen such a light-hearted term myself."
    "But I'm not about to argue semantics with Cherie right now."
    mike.say "Sure, mon Cherie..."
    mike.say "I guess you could call it that."
    show cherie talkative
    cherie.say "So..."
    show cherie normal
    "Cherie holds up a heavy, official-looking ledger."
    "One that's held closed by a pair of thick, decorative bands."
    "And I instantly know it's the kind of thing Dwayne would use to record everything."
    "All of his business dealings and dirty little secrets, all hidden in those pages."
    show cherie talkative
    cherie.say "I believe this is what you are looking for?"
    show cherie normal
    "My eyes are growing wider by the second as I stare at the ledger."
    show cherie talkative
    cherie.say "I..."
    cherie.say "I am still not certain I should be giving this to you!"
    cherie.say "Maybe I need a little more...convincing?"
    show cherie normal
    "Part of my brain is telling me that Cherie's dropping not so subtle hints right now."
    "But it's being ignored by the larger part making me salivate at the prospect of the ledger."
    mike.say "Is that it?"
    mike.say "Is that all there was in the vault?"
    "Cherie shrugs off the question."
    "Almost as if she's eager to avoid the issue."
    show cherie talkative
    cherie.say "It is everything that is relevant, everything that you need."
    cherie.say "There were...other things, of course."
    cherie.say "But are not a matter of concern for you."
    show cherie normal
    mike.say "I see..."
    show cherie talkative
    cherie.say "So..."
    cherie.say "What exactly do I get for this?"
    show cherie normal
    "The question seems to come out of nowhere."
    "And I have no time to think of a subtle or clever answer."
    "Which I suppose means the one I come out with must be an honest one."
    mike.say "Your freedom, I hope!"
    mike.say "That at the very least."
    "Cherie cocks her head on one side."
    "Clearly she's not satisfied with my answer."
    show cherie talkative
    cherie.say "Yes, yes..."
    cherie.say "But what about you?"
    cherie.say "What do {b}I{/b} get from {b}you{/b}?"
    show cherie normal
    "I can't help staring in silence at Cherie."
    "Again her question puts me on the spot."
    "And all I can do is offer an honest response."
    mike.say "I don't know, Cherie..."
    mike.say "What would you like?"
    "Cherie regards me for a time."
    "Almost like she's trying to look deeper than the surface."
    "Trying to see into my head, so she can understand what makes me tick."
    show cherie talkative
    cherie.say "What I would {b}like{/b}, {i}mon ami{/i}..."
    cherie.say "Is for you to take me to Dwayne's bed and fuck me like he does."
    cherie.say "Fuck me long, deep and hard!"
    show cherie normal
    menu:
        "Okay":
            "Oddly the frank and forward demand from Cherie doesn't confound me at all."
            "Unlike the supposedly less dramatic things she askes of me before now."
            "And all I do is nod my head, then gesture towards the palatial house."
            mike.say "If that's what you want, then let's go!"
            mike.say "Let's go it right now, Cherie."
            "Much to my disappointment, Cherie simply shakes her head."
            "And she gives me one of those enigmatic looks she's so good at."
            cherie.say "Hmm.."
            show cherie talkative
            cherie.say "I am delighted by your enthusiasm, {i}mon ami{/i}..."
            cherie.say "But that, I think, is not in the cards for tonight."
            show cherie normal
            "I shake my head in disbelief."
            mike.say "So what, Cherie?"
            mike.say "You were just teasing me?"
            "Now Cherie gives me a nod and an amused smile."
            show cherie talkative
            cherie.say "But of course, {i}mon ami{/i}..."
            cherie.say "Just like the way you tease me, every time I see you!"
            show cherie normal
        "That's not what you really want":
            if Person.find("cherie"):
                $ cherie.love += 3
            "I think of myself as being a pretty good judge of character, able to read the room."
            "And believe me, the idea of making love to Cherie is hard to shake."
            "But there's something about the way she said it that just doesn't feel right."
            mike.say "I...really like you, Cherie..."
            mike.say "But I don't think that's how you want it to be, not really."
            "I was expecting that to be an end to it."
            "But Cherie instead responds by raising her eyebrows."
            show cherie talkative
            cherie.say "Oh, is that so?"
            cherie.say "I don't really want you to make me feel like a wanted woman again?"
            cherie.say "Then tell me, [hero.name] - what do I really want?"
            show cherie normal
            "I've called Cherie on it now, so I can't back down."
            "What I need to do is match her boldness and confidence."
            mike.say "Oh don't get me wrong, Cherie..."
            mike.say "I think you want me to make long, passionate, earth-moving love to you."
            mike.say "But I don't think the time for that is right now."
            "For the first time since the subject came up, Cherie looks disappointed."
            show cherie talkative
            cherie.say "Why not?"
            cherie.say "I have not been able to think of anything but your handsome, smiling face for days!"
            show cherie normal
            "I can feel a smile spreading across my face."
            "My mood improving as Cherie shows her vulnerable side to me."
            mike.say "What I think is that you want a guarantee, Cherie..."
            mike.say "A promise that I'll still be here for you tomorrow."
            mike.say "And sure, you'd really like the sex too."
            mike.say "But what good is one fantastic night if I'm gone the next morning?"
            "Now Cherie really looks worried."
            show cherie talkative
            cherie.say "Are you..."
            cherie.say "Are you saying that you would make love to me and then leave?"
            show cherie normal
            "I shake my head, still smiling to myself."
            mike.say "No, Cherie, that's not what I'm saying."
            mike.say "When this is all over and you're a free woman..."
            mike.say "That's when I want to explore what our relationship could be."
            mike.say "Without your {b}husband{/b} in the equation at all."
            "Cherie stares deep into my eyes as I explain myself."
            "And soon enough, she's nodding with enthusiasm."
            show cherie talkative
            cherie.say "I have to admit, {i}mon ami{/i}..."
            cherie.say "That does sound...very pleasant, very pleasant indeed."
            show cherie normal
    "Cherie's hand reaches out, offering the ledger to me."
    show cherie talkative
    cherie.say "I think it is time for you to take this and go."
    cherie.say "To do what you must with it, and set me free."
    show cherie normal
    "I reach out to take the book, my fingers almost touching it."
    "But then I hear a door slam, and we both flinch in surprise."
    "Though the surprise turns to alarm for me, when I see Dwayne striding into the room!"
    play music "music/TeknoAXE/simple_metal.ogg" loop fadein .5
    show cherie surprised at right4
    show dwayne casual at left
    with moveinleft
    cherie.say "Dwayne! What are you doing here?"
    cherie.say "You told me that you were flying to New York!"
    show dwayne angry
    dwayne.say "What the actual fuck is going on here?!?"
    "Cherie looks from Dwayne to me and back again."
    cherie.say "It...this is not..."
    cherie.say "This is not what it looks like!"
    "Unfortunately for Cherie and me, there's precious little else this does look like."
    "And Dwayne's far from being an idiot, so it's not like she can pull the wool over his eyes either."
    dwayne.say "That's the ledger from the vault."
    dwayne.say "How in the hell did you get your hands on that?!?"
    show cherie sad
    "Cherie looks down at the ledger, still clutched in her hands."
    "Almost as if she's surprised to see it there."
    show cherie talkative
    cherie.say "Oh, this?"
    cherie.say "I...uh..."
    cherie.say "This is..."
    show cherie sad
    "Dwayne cuts Cherie off before she can cook up an explanation."
    dwayne.say "You lying, stealing, conniving bitch!"
    dwayne.say "Is this how you repay me for years of keeping you in the lap of luxury?"
    dwayne.say "You give my precious secrets away, and to a deadbeat asshole like this?!?"
    show cherie surprised
    cherie.say "Dwayne, no..."
    cherie.say "I..."
    play sound punch_hard
    pause 0.2
    play sound body_fall
    show dwayne at left4 with MoveTransition(0.1)
    hide cherie with easeoutbottom
    "Dwayne steps up and backhands Cherie with one powerful swing."
    "I'd be terrified of taking a blow like that from Dwayne myself."
    "And of course, Cherie doesn't stand a chance."
    "She spins away, immediately crumpling into a heap on the floor."
    show dwayne at center with ease
    "I want to rush over to Cherie, to check that she's okay."
    "But before I can make a move, Dwayne is standing in my way."
    dwayne.say "And you..."
    dwayne.say "First my company, then my daughter, and now this?"
    dwayne.say "This is the final straw - I've had it with you!"
    "Desperate to help Cherie, all I can think to do is point at her."
    "Trying to appeal to the part of Dwayne that might still love his wife."
    mike.say "Dwayne..."
    mike.say "What did you do?"
    mike.say "You could have killed her!"
    "Dwayne doesn't take his eyes off me for even a second."
    "And when he laughs, the sound chills me to my core."
    dwayne.say "Ha..."
    dwayne.say "Maybe I was trying to?"
    dwayne.say "But I promise I'll try harder with you!"
    "Dwayne lunges toward me, his huge hands thrusting out for my neck."
    "I know instinctively he's not trying to fight me."
    "All he wants to do is choke the life out of me!"
    hide dwayne
    show dwayne fight neck
    with hpunch
    dwayne.say "You ungrateful, miserable little shit!"
    dwayne.say "I'm going to enjoy snapping your pencil neck!"
    if not hero.has_skill("martial_arts"):
        "I struggle, trying as best I can to fight back, but it's no use."
        "Dwayne just seems to ignore everything I manage to do to him."
        "The guy's simply huge, dwarfing me physically."
        "And he's steaming mad too!"
        play sound punch_hard
        pause 0.2
        hide dwayne fight neck
        show dwayne fight win
        with hpunch
        "Dwayne has one massive hand around my neck, squeezing hard."
        "And he uses the other to pummel me in the face over and over again."
        "Soon my vision starts to blur, going fuzzy around the edges."
        "I try to speak, to beg for it all to stop."
        "But no sound comes out and I can taste blood."
        "Part of me wonders if my jaw's been broken in the one-sided struggle."
        play sound punch_hard
        pause 0.2
        with hpunch
        "As far as I can tell, Dwayne keeps on hitting me."
        "Though it's getting harder to tell one blow from the next."
        dwayne.say "I'm gonna end you, then dump your body where they'll never find it."
        dwayne.say "Then I'm gonna track down everyone you knew and ever loved."
        dwayne.say "And I'm gonna burn it all down to the ground - all of it!"
        dwayne.say "You're gonna be an example of what happens to whoever fucks with me!"
        play sound punch_hard
        pause 0.2
        with hpunch
        scene bg mansion at blood
        show dwayne fight win at blood
        with dissolve
        scene bg mansion at blur(8), blood
        show dwayne fight win at blur(8), blood
        with dissolve
        "Dwayne's fist connects with my face one last time."
        "And everything goes red."
        scene bg mansion at blur(16), dark, red
        show dwayne fight win at blur(16), dark, red
        with dissolve
        "Then black."
        scene bg black with dissolve
        pause 1.0
        $ renpy.full_restart()
    "Luckily for me, I've been keeping up to speed with my martial arts recently."
    "Even better, I never told Dwayne that I'd as much as watched a Kung Fu movie in all the time I've known him."
    "Instinct kicks in, and I instantly put Dwayne into a wrist-lock."
    "Even at an awkward angle like this, I can still force him to release me."
    "All it takes is a quick application of pressure in the right spot, and I'm free."
    play sound woosh_punch
    hide dwayne fight neck
    show dwayne casual angry
    with hpunch
    "From there it's just a matter of using Dwayne's size against him."
    "Moving his mass to propel myself to a safe distance from his grasping hands."
    "Of course, none of this goes down well with Dwayne himself."
    "He lets out a bestial roar, then lowers his head to charge at me."
    "I wait for the right moment, then lower my center of gravity and take a smooth step to one side."
    "All of this means Dwayne shoots straight past me."
    play sound punch_hard
    pause 0.2
    show dwayne close angry
    with hpunch
    with hpunch
    "But he's more nimble than he looks."
    "Somehow, Dwayne manages to turn and take a swipe at my head."
    "I do the best I can to block it, but he's just too strong."
    "Dwayne grazes me with the blow, the pain of the impact making me see stars."
    show dwayne fight win with hpunch
    call injured from _call_injured_6
    "Dwayne uses the chance to clamp a hand on my neck again."
    "Then he pulls back his fist to deliver another blow."
    play sound gun
    with screenshot
    hide dwayne fight win
    show dwayne fight shot
    "But the blow never comes."
    "Instead there's an ear-splitting bang."
    "And the next thing I know, Dwayne's grip loosens."
    "my neck freed from his grasp, I collapse to the floor, coughing and spluttering."
    "But when I look up, I see a confused look on Dwayne's face."
    "Perhaps on account of the blood that's currently spurting out of a hole in his forehead!"
    play sound body_fall
    hide dwayne fight shot
    show aletta casual pain
    with fade
    "Suddenly Dwayne's eyes roll upwards and into the top of their sockets."
    "He sways like a drunk, gravity getting a hold on him."
    "And then his massive body falls right down atop me."
    "Mercifully I'm only trapped beneath Dwayne's carcass for a few moments."
    "Then I hear grunting and cursing as someone pulls it off of me."
    "I look up, straight into Aletta's face."
    "She's gazing down at me, a serious expression on her features."
    show aletta angry
    aletta.say "Fucking hell, [hero.name]..."
    aletta.say "Are you okay?"
    show aletta sad
    "I'm about to say something cutting and sarcastic in response."
    "But then I realise it's a damn good question."
    "And a quick check clues me in on the fact that almost everything hurts right now."
    "But I'm alive, which is probably more than can be said for Dwayne!"
    mike.say "I'll live, Aletta..."
    mike.say "At least I think I will!"
    show aletta talkative
    aletta.say "You'd better, because you need to get on your feet."
    aletta.say "And we've got to get out of here!"
    show aletta normal
    mike.say "Aletta, wait..."
    mike.say "Where is she..."
    mike.say "Where's...Cherie!"
    scene bg mansion at center, zoomAt(2.5, (960, 840)), dark with fade
    "I glance around, searching for her."
    "And seeing her, I get up, ignoring all of the pain that flares as I hurry to her."
    "She's still laid where she fell, and to my horror, she's not moving."
    "An ugly purple bruise marks the side of her face where Dwayne hit her."
    "But I ignore it to put my hand on her neck and check her pulse."
    "Much to my relief, I feel it a moment later, which means she's still alive."
    mike.say "Cherie..."
    mike.say "Cherie, you have to wake up!"
    show cherie sad at center, zoomAt(1.5, (640, 1040)) with fade
    "Cherie slowly opens her eyes and looks up at me."
    "But the look in them is distant and her expression is disoriented."
    show cherie talkative
    cherie.say "What..."
    cherie.say "What happened?"
    show cherie sad
    mike.say "Dwayne happened!"
    mike.say "The bastard hit you."
    mike.say "Are you okay?"
    "Cherie puts an experimental hand to her bruised temple."
    "And she winces the moment that her fingers touch the purple skin."
    show cherie talkative
    cherie.say "Ah..."
    cherie.say "That...that really hurts."
    cherie.say "But I do not think anything is broken."
    show cherie sad
    "For the first time, Cherie's eyes seem to focus on my face."
    "And I can see a look of concern in them a moment later."
    show cherie talkative
    cherie.say "You don't look so good yourself, {i}mon ami{/i}!"
    cherie.say "What happened to you?"
    show cherie sad
    "I do the best I can to put a smile on my face."
    "That and to dismiss Cherie's concerns for me."
    mike.say "I...I'll live."
    "Cherie nods, but then a look of concern spreads over her face."
    show cherie talkative
    cherie.say "But..."
    cherie.say "But what about Dwayne?"
    show cherie sad
    "I look over at Dwayne, sure that she's following my gaze."
    "I'm no expert, but the blood was coming out of the front of his head."
    "So that probably means Aletta shot him in the back of the skull."
    "And no matter how big and tough Dwayne was, he couldn't survive that!"
    mike.say "Dwayne's dead, Cherie, Dwayne's dead!"
    scene bg mansion
    show aletta casual at left4
    with fade
    show cherie at center, zoomAt (1.0, (820, 940)) with easeinbottom
    "That seems to be what Cherie needed to jolt her back to reality."
    "She sits up and crawls towards the quicky cooling body."
    "Cherie reaches out for a moment, probably out of years of instinct."
    "But then she pulls her hand back, realising that it's far too late to help."
    show cherie talkative
    cherie.say "What?"
    cherie.say "How?"
    cherie.say "Where did you get a..."
    show cherie sad
    "Cherie falls silent for a moment as she sees we're not alone."
    "Only now does she notice Aletta, standing over Dwayne's body."
    "That and the fact she still has a smoking pistol in her hand."
    show cherie surprised
    cherie.say "You..."
    cherie.say "You shot him?"
    show aletta angry
    aletta.say "I sure did!"
    show aletta annoyed
    mike.say "And just in time too."
    mike.say "He was gonna kill me!"
    "By now Cherie is kneeling by Dwayne's body."
    "Her hands are clutched to her chest, and she's shaking her head."
    show cherie talkative
    cherie.say "Oh..."
    cherie.say "Oh Dwayne..."
    cherie.say "I did not want this - I did not want you dead!"
    cherie.say "You silly...terrible, horrible man."
    cherie.say "I wanted rid of you, but I did not want you dead."
    show cherie sad
    "I shuffle over to knell beside Cherie."
    "Then I reach out to put a hand on her shoulder."
    mike.say "That makes two of us, Cherie..."
    mike.say "This was never part of the plan."
    mike.say "I...I still don't get what he was doing here!"
    show cherie talkative
    cherie.say "Your guess is as good as mine, {i}mon ami{/i}!..."
    cherie.say "He told me he was flying to New York, on business."
    cherie.say "Perhaps he was suspicious of me?"
    cherie.say "Or maybe it was something as silly and simple as that he forgot something?"
    show cherie sad
    "Cherie lets out a long, tired sigh."
    show aletta at left5
    show cherie at center, zoomAt (1.0, (820, 740))
    with ease
    menu:
        "Step in":
            mike.say "Aletta..."
            mike.say "Give the gun to me."
            show aletta scared
            "As one, Aletta and Cherie turn to stare at me."
            "But it's the former that questions me first."
            aletta.say "Have you lost your mind?"
            aletta.say "That'll put your prints all over the thing!"
            show aletta sad
            show cherie talkative
            cherie.say "She's right, {i}mon ami{/i}!"
            show cherie sad
            "I nod my head, still holding out my hand to Aletta."
            mike.say "I know that, Aletta..."
            mike.say "But once I clean it, yours will be gone."
            show aletta stuned
            "This gets me another round of shaking heads and shocked looks."
            show aletta scared
            aletta.say "That's crazy, [hero.name]..."
            aletta.say "Are you trying to make it look like you shot Dwayne, or what?"
            show aletta sad
            mike.say "Of course not!"
            mike.say "I'm trying to start cleaning up this mess."
            "Cherie and Aletta exchange a look."
            "And then they're on me as a pair."
            show cherie talkative
            cherie.say "But it should be me that cleans things up!"
            cherie.say "Besides, I can claim that it was self defence."
            show cherie sad
            show aletta whining
            aletta.say "In the back of the head?"
            aletta.say "No one in their right mind will believe that!"
            show aletta upset
            "Cherie looks at Aletta with a coldness in her eyes that I've never seen before."
            "And I can't believe how calmly she's discussing the subject of Dwayne's death."
            show cherie talkative
            cherie.say "He thought I was dead."
            cherie.say "He was leaving to find the means to dispose of my body."
            cherie.say "But he was mistaken, and I shot him before he could finish the job."
            show cherie sad
            "It strikes me as an elaborate story to cook up in the current situation."
            "And I can't help wondering how much time Cherie's spent dwelling on this subject in the past."
            "But whatever the answer, neither of them are going to change my mind."
            mike.say "No..."
            mike.say "Give me the gun and make yourselves scarce."
            mike.say "Nobody's calling the police and nobody's taking the fall."
            mike.say "I'll dump the body and the gun."
            mike.say "Then I'll come back and clean up the scene too."
            "I can see that the two of them are about to start arguing again."
            play sound woosh_punch
            pause 0.1
            with hpunch
            "So I snatch the gun out of Aletta's hand, hoping to make my point."
            "Luckily for me, she's not holding onto it tightly, and I take it away from her."
            show aletta scared
            aletta.say "HEY!"
            show aletta upset
            mike.say "Too late, Aletta..."
            mike.say "Now my prints are on it too!"
            "Aletta scowls at me, but she also starts to pull Cherie to her feet."
            show aletta whining
            aletta.say "Come on, Cherie..."
            aletta.say "Let him martyr himself if that's what he wants!"
            show aletta upset
            "Cherie allows herself to be led out of the room."
            "But she looks back over her shoulder at the same time."
            "All I can do is give her what I hope is a reassuring smile."
            "And once I'm alone, the smile instantly vanishes."
            "I could never have predicted that things would play out like this."
            "But I guess that I have to look for the positives, even in this mess."
            "Though I can't help thinking we just traded one problem for another."
            "And perhaps more pressingly, I have to dispose of a gun and a dead body."
            "Not things that I have much experience of!"
            $ hero.gain_item("dwayne_corpse")
            $ hero.gain_item("aletta_gun")
            $ game.flags.handle_gun_body = True
        "Wait":
            "Then she turns to Aletta, reaching out with her hand."
            cherie.say "Give the gun to me."
            show aletta stuned
            "Aletta takes a step backwards, confusion written all over her face."
            show aletta scared
            aletta.say "What?!?"
            aletta.say "N...no...not a chance!"
            show aletta upset
            "But all this gets her in return is a steely stare from Cherie."
            show cherie talkative
            cherie.say "Do not be stupid!"
            cherie.say "Do you want to go to jail for killing Dwayne?"
            show cherie sad
            "Aletta looks to me, as if appealing for help."
            "But all I can do is offer a helpless shrug."
            "Which leaves her to turn back to Cherie."
            show aletta whining
            aletta.say "No..."
            aletta.say "But..."
            show aletta embarrassed
            show cherie talkative
            cherie.say "Then give me the gun - now!"
            show cherie sad
            "Aletta's still shaking her head."
            "Trying and failing to understand what's happening here."
            show aletta whining
            aletta.say "Why?"
            aletta.say "What difference will it make?"
            show aletta sad
            show cherie talkative
            cherie.say "Because I will tell the police that I shot him."
            cherie.say "Dwayne was my husband, after all."
            cherie.say "He got angry, hit me, and I shot him."
            cherie.say "They will think it was an act of self-defence."
            show cherie sad
            show aletta whining
            aletta.say "In the back of the head?"
            aletta.say "No one in their right mind will believe that!"
            show aletta upset
            "Cherie looks at Aletta with a coldness in her eyes that I've never seen before."
            "And I can't believe how calmly she's discussing the subject of Dwayne's death."
            show cherie talkative
            cherie.say "He thought I was dead."
            cherie.say "He was leaving to find the means to dispose of my body."
            cherie.say "But he was mistaken, and I shot him before he could finish the job."
            show cherie sad
            "It strikes me as an elaborate story to cook up in the current situation."
            "And I can't help wondering how much time Cherie's spent dwelling on this subject in the past."
            mike.say "I don't know, Cherie..."
            mike.say "Maybe you need help to..."
            "Cherie cuts me off before I can even finish what I was about to say."
            show cherie talkative
            cherie.say "Believe me, this is the best way."
            cherie.say "We must pretend that the two of you were never here."
            show cherie sad
            "Tears start to form at the corner of Cherie's eyes as she says this."
            "As if admitting that she has to face this challenge alone is too much."
            show aletta whining
            aletta.say "This is..."
            aletta.say "You don't have to..."
            show aletta embarrassed
            "Suddenly Cherie seems to snap under the pressure."
            "She thrusts out her hand again."
            "And her eyes are as intense as before."
            show cherie talkative
            cherie.say "Just give me the damn gun!"
            cherie.say "Give it to me and get out of here, before it's too late!"
            show cherie sad
            "The more I think about this, the more I think Cherie's right."
            "If the police do but that it's just a domestic violence call, it could work."
            "But with Aletta and I here, there would be too many questions to answer."
            mike.say "Okay, Cherie..."
            mike.say "You win..."
            mike.say " Aletta, give her the gun."
            show aletta stuned
            "Aletta is now looking at me in disbelief."
            show aletta scared
            aletta.say "What?!?"
            aletta.say "Have you lost your mind too?"
            show aletta sad
            mike.say "Think about it, Aletta..."
            mike.say "If the police investigate us, they're going to uncover everything that's been going on."
            mike.say "What Dwayne did to you, what I did to Dwayne..."
            mike.say "We could wind up in jail without even trying."
            mike.say "Even if they pin it on Cherie, she'll probably get off lightly."
            show aletta upset
            "I see anger flare in Aletta's eyes."
            "But I don't know if it's because she disagrees with me."
            "Or simply because she hates to be told what to do."
            show aletta angry
            aletta.say "No..."
            aletta.say "We should..."
            show aletta upset
            mike.say "ALETTA!"
            "I make myself sound as commanding and assertive as I dare."
            "But Aletta still narrows her eyes and glares at me."
            show aletta sadsmile
            "But then she pulls the gun back out of her purse."
            "And she thrusts it into Cherie's open hand."
            show cherie talkative
            cherie.say "Thank you."
            cherie.say "Now, both of you..."
            cherie.say "Go and get cleaned up."
            cherie.say "And remember - you were never here!"
            show cherie sad
            "Aletta does as she's told for a second time."
            "But she still can't resist saying more."
            show aletta whining
            aletta.say "Fine..."
            aletta.say "But this had better not go..."
            show aletta sad
            "Cherie snaps out a response, cutting Aletta off."
            show cherie talkative
            cherie.say "It's my life on the line now!"
            show cherie sad
            "This seems to be enough to shut Aletta up."
            show aletta whining
            aletta.say "Y...you're right..."
            aletta.say "I'm sorry, Cherie..."
            show aletta sad
            "I take hold of Aletta's hand and begin to lead her away from the scene of the crime."
            mike.say "Come on, let's go."
            hide aletta
            hide cherie
            with fade
            "We leave Cherie kneeling over Dwayne's fast-cooling body."
            "And I hear her begin to sob, a deep and painful sound."
            "I could never have predicted that things would play out like this."
            "But I guess that I have to look for the positives, even in this mess."
            "Though I can't help thinking we just traded one problem for another."
            $ game.flags.handle_gun_body = False
            $ game.room = "street"
    $ game.flags.cherie_ceooffer = TemporaryFlag(True, 7)
    $ game.flags.dwaynedead = True
    $ game.flags.dwayne_corpse_discovery_delay = TemporaryFlag(True, 7)
    return

label dwayne_corpse_reminder:
    "..."
    "Did I turn off the oven?"
    "Hmm..."
    "Yes. Yes, I did."
    "Maybe it’s just the fact that I still haven’t disposed of Dwayne’s body that’s weighing on my mind."
    "I should really take care of that when I have some time."
    return

label dump_dwayne_corpse_mansion:
    play music "<from 2 to 20>music/darren_curtis/into_oblivion.ogg" loop fadein 0.5 fadeout 5.0
    show dwayne_corpse at center, zoomAt(0.85, (640, 720)) with fade
    "As soon as I look down at Dwayne's body, I'm struck by just how big he actually was."
    "I mean sure, he was intimidating when he was alive and strutting around the place like he owned it."
    "Well...I guess in most cases he actually did!"
    "But now that he's dead and lying there motionless, he looks even bigger than ever."
    "In fact he reminds me of some huge slab of meat."
    "The kind you always see in the movies, hanging from hooks in freezers."
    "And that's when it hits me - maybe I can get rid of Dwayne in the very same way?"
    "I mean, this mansion of his is bloody vast, and it has every luxury imaginable."
    "I'm willing to bet that it has a massive freezer somewhere in the huge basement."
    "Leaving the body for a moment, I hurry off to search for the freezer."
    "And it doesn't take me long to find a huge, metal door in the cellar."
    mike.say "Oh man..."
    mike.say "This can't be what I think it is..."
    mike.say "Can it?"
    scene bg alley night winter at center, zoomAt(4.0, (2500, 2000)), blur(2) with fade
    "Pulling the handle on the door, I yank the thing open."
    "And the moment I do, I'm assaulted by a draft of cold air from inside."
    mike.say "Wow..."
    mike.say "It is!"
    "Turns out Dwayne doesn't just have a huge freezer down here."
    "He has an actual walk-in freezer!"
    "With those hooks hanging from the ceiling and shelves lining the walls too."
    "Leaving the door propped open, I hurry back to where I left the body."
    "There's no way that I can hope to lift Dwayne's carcass off the floor."
    "So I make do with grabbing his ankles and hauling him in the direction of the freezer."
    "But even doing it this way, he's still a massive weight to shift and it takes a while."
    "I have to make multiple stops along the way to catch my breath."
    "And more than once I accidentally bang his head on steps and doorframes."
    "So by the time I'm finally dragging Dwayne into the freezer, I'm exhausted."
    "Part of me is afraid of the door slamming shut while I'm in there."
    "And I've seen enough movies to know that these things can only be opened from the outside."
    "That means I hurry to shove him in there and then scuttle out as quickly as I can."
    "And no, I don't even think about sticking him on one of the meat-hooks either!"
    "Firstly I couldn't hope to lift him off the ground."
    "So getting him onto a hook would be totally impossible."
    "And secondly, I still have a modicum of respect for the guy."
    "All of this means that I just slam the door shut and close the latch."
    "Hoping, as I do so, that I've chosen the right place to stash the body."
    "As well as trying not to dwell on what happens if there's a power-cut!"
    $ hero.lose_item("dwayne_corpse")
    $ hero.flags.dwayne_corpse = "mansion"
    return

label dump_dwayne_corpse_beach:
    play music "<from 2 to 20>music/darren_curtis/into_oblivion.ogg" loop fadein 0.5 fadeout 5.0
    "It took a massive effort to drag Dwayne out of the mansion and into my car."
    "All the time I was sure that someone was going to see me dragging the body along."
    "But manhandling him into the trunk and driving away was even worse."
    "The drive to the seaside cliffs had never seemed this long in the past."
    "And I had to fight to keep from driving above the speed limit."
    "Luckily for me, I made it there without incident."
    "So the next task is to haul him out of the car again."
    show dwayne_corpse at center, zoomAt(0.85, (640, 720)) with fade
    "As soon as I look down at Dwayne's body, lying there on the ground, I'm struck by just how big he actually was."
    "I mean sure, he was intimidating when he was alive and strutting around the place like he owned it."
    "Well...I guess in most cases he actually did!"
    "But now that he's dead and lying there motionless, he looks even bigger than ever."
    "In fact he reminds me of some huge slab of meat."
    "As I grab his ankles again and begin dragging him towards the cliffs, that strikes me as a good thing."
    "Because maybe a hungry shark will catch the scent of him and come looking for the cadaver."
    "Knowing that he was safely in the belly of something with all those teeth would be a real comfort!"
    "By the time I reach the edge, I'm sweating and panting, totally exhausted."
    "This means that I have to take a moment to get my breath back."
    "As I'll need it to toss him over and into the sea."
    "The last thing I need is for the body to get snagged on something halfway down."
    "Or worse, to end up falling in after it!"
    "Taking a casual glance over the edge, I feel a rush of vertigo."
    "But that's okay, I can handle it."
    "It's not like I have to go down there myself, just toss him over."
    "Forcing myself to look, I note that the tide is well and truly in right now."
    "It's lashing against the bottom of the cliffs, probably a good few metres deep."
    "With luck, the undertow will get hold of him."
    "And that'll drag him far out to sea before he even surfaces again."
    "Deciding that I can't lift him even for a moment, I put a foot on Dwayne's body."
    hide dwayne_corpse with easeoutbottom
    "Then I shove it over the edge with a good, hard kick."
    "My weight shifts forward for a second, and I flail my arms."
    "Then I stagger backwards and away from the edge."
    "I don't wait any longer, turning the motion into a turn."
    "Running back towards the car, I don't turn around once."
    "I sprint back to the car and drive out of there."
    "All the time hoping that I've done enough to hide the body."
    "As well as that Dwayne doesn't turn up in some fishing boat's net tomorrow morning!"
    $ hero.lose_item("dwayne_corpse")
    $ hero.flags.dwayne_corpse = "beach"
    return

label dump_dwayne_corpse_forest:
    play music "<from 2 to 20>music/darren_curtis/into_oblivion.ogg" loop fadein 0.5 fadeout 5.0
    "It took a massive effort to drag Dwayne out of the mansion and into my car."
    "All the time I was sure that someone was going to see me dragging the body along."
    "But manhandling him into the trunk and driving away was even worse."
    "The drive to the forest had never seemed this long in the past."
    "And I had to fight to keep from driving above the speed limit."
    "Luckily for me, I made it there without incident."
    "So the next task is to haul him out of the car again."
    show dwayne_corpse at center, zoomAt(0.85, (640, 720)) with fade
    "As soon as I look down at Dwayne's body, lying there on the ground, I'm struck by just how big he actually was."
    "I mean sure, he was intimidating when he was alive and strutting around the place like he owned it."
    "Well...I guess in most cases he actually did!"
    "But now that he's dead and lying there motionless, he looks even bigger than ever."
    "In fact he reminds me of some huge slab of meat."
    "I glance around, my head suddenly filling with images of hungry carnivores."
    "A shudder of fear runs down my spine, and I hurry to grab Dwayne's ankles."
    "Dragging him to what looks like a decent spot, I run back to the car."
    "Then I grab the spade I've brought along and dash back again."
    play sound knife_stab
    pause 0.2
    with vpunch
    "Driving the spade into the ground, I feel it jar against my shoulder."
    "Ah shit..."
    "Why did the ground have to be as hard as concrete?"
    play sound hitting_bushes
    "Doing the best I can, I start to dig a hole for Dwayne."
    play sound knife_stab
    pause 0.5
    queue sound hitting_bushes
    "It's slow going, way harder than I ever imagined digging a grave would be."
    "But there's no other choice for me - I have to bury him here and now."
    play sound knife_stab
    pause 0.5
    queue sound hitting_bushes
    "So I carry on, my muscles burning with fatigue and seeming to jar the spade on every stone in the ground."
    "Eventually I stop and stand up, feeling my whole body aching as I stretch out my tortured limbs."
    "I'm expecting to find myself looking up and out of a suitably deep hole."
    "But instead I discover that it's barely deep enough to reach my knees!"
    mike.say "Oh come on!"
    mike.say "You have got to be kidding!"
    "Suddenly I realise that I'm bellowing into the deepest, darkest woods."
    "And that if anyone or anything heard me, then I'm probably in deep trouble!"
    play sound knife_stab
    pause 0.5
    queue sound hitting_bushes
    "I do the best I can to dig out a few more inches, then I climb out of the hole."
    "It looks way smaller than I'd hoped, but it'll have to do."
    play sound body_fall
    hide dwayne_corpse with easeoutbottom
    "Rolling Dwayne's body into the hole, I curse as he tumbles over the edge."
    "Somehow it manages to land head-down, with it's ass in the air."
    "Tentatively I stick out my foot and try to push him deeper into the hole."
    "But despite my efforts, the buttocks are still sticking out when I fill it in."
    "The best I can do is to pile the earth up on top of them, making a little mound."
    "Then I grab branches and other fallen debris, tossing them on top."
    "Glancing around, I leap on top of the whole thing."
    "And then I jump up and down, trying to flatten it all."
    "That done, I sprint back to the car and drive out of there."
    "All the time hoping that I've done enough to hide the body."
    "As well as that a bear or something similar doesn't dig him up for a midnight snack!"
    $ hero.lose_item("dwayne_corpse")
    $ hero.flags.dwayne_corpse = "forest"
    return

label dump_aletta_gun_mansion:
    play music "<from 2 to 20>music/darren_curtis/into_oblivion.ogg" loop fadein 0.5 fadeout 5.0
    "I've tried to think up a really clever way to dispose of the gun that Aletta used to shoot Dwayne."
    "But all I could seem to come up with was stuff like dissolving it in acid or melting it in a furnace."
    "Both of which are pretty far out ideas, even for me."
    "And I have no idea where I'd find the stuff I'd need to actually do it either!"
    "So I discard all of those crazy notions and do the best I can to clear my mind."
    "And instead I think of the most simple, practical place possible."
    "But even that doesn't seem to work, and I just end up getting tired."
    "I'm starting to wonder if I should just sleep on it and try again in the morning."
    "And that's when it hits me - I can stash the gun under Dwayne's bed!"
    "There's no way anyone would think I'd be dumb enough to hide it there."
    "Which makes actually doing it a stroke of genius, right?"
    if hero.flags.dwayne_corpse == "mansion" and (hero.knowledge >= 85 or hero.has_skill("investigator")):
        show black at opacity(0.25) with dissolve
        "But wait..."
        "Didn't I hide Dwayne's body here already?"
        "That might not be the wisest idea to also stash the gun here..."
        "But it's not like they'll find it anyway, right?"
        hide black with dissolve
        menu:
            "It will be fine":
                "Yeah, there's no chance they'll find the gun in this huge place."
            "Better find another place":
                "Yeah, what I was thinking..."
                "If either the body or gun is found, they will turn the entire place upside down to locate the other."
                return



    "Pulling the gun out, I lift the mattress and toss it underneath."
    play sound bed_jump
    "I drop it down again and flop onto the bed, bouncing up and down to see how it feels."
    "It's on the second bounce that I realise just how dumb what I'm doing actually is."
    "And so I stop dead, wincing as I expect to hear the sound of the gun going off."
    "Nothing seems to happen, and so I let out a sigh of relief."
    "Did I even bother to check if there were bullets left in the thing?"
    "Urgh..."
    "It must be the stress of the whole Dwayne being shot dead situation."
    "I'm so wound up that I'm not thinking straight!"
    "Even so I still don't bother to pull the gun out and check it."
    "The fact that it didn't go off is good enough for now."


    "That'll work, right?"
    $ hero.lose_item("aletta_gun")
    $ hero.flags.aletta_gun = "mansion"

    return

label dump_aletta_gun_beach:
    play music "<from 2 to 20>music/darren_curtis/into_oblivion.ogg" loop fadein 0.5 fadeout 5.0
    "I'd tried to think up a really clever way to dispose of the gun that Aletta used to shoot Dwayne."
    "But all I could seem to come up with was stuff like dissolving it in acid or melting it in a furnace."
    "Both of which are pretty far out ideas, even for me."
    "And I have no idea where I'd find the stuff I'd need to actually do it either!"
    "So I discarded all of those crazy notions and did the best I can to clear my mind."
    "And instead I thought of the most simple, practical place possible."
    "But even that didn't seem to work, and I just ended up getting tired."
    "I was starting to wonder if I should just go for a walk and clear my mind."
    "The cliffs by the sea are always a nice place to do that..."
    "And that's when it hit me - I could toss the gun into the sea!"
    "Then the water will wash it away for good."
    "Either that or it'll sink to the bottom and never be seen again."
    "With the gun stashed in my pocket, I hurried to leap into the car."
    "And then I drove straight to the coast, hoping that I was not followed."
    "I parked and started walking towards the cliffs, going as fast as I could."
    with fade
    "This means that I get to the edge in record time."
    "But as I do so I can feel the rush of vertigo induced by the heights."
    "So I close my eyes and do the best I can to regulate my breathing."
    "It's not like I have to actually dangle the gun over the edge or anything."
    "That would run the risk of it getting hooked on a branch or outcropping on the way down."
    "No, much better to wind up and toss it as far out as I possibly can."
    if hero.flags.dwayne_corpse == "beach"  and (hero.knowledge >= 85 or hero.has_skill("investigator")):
        show black at opacity(0.25) with dissolve
        "Wait..."
        "Didn't I hide Dwayne's body somewhere around here already?"
        "That might not be the wisest idea to also throw the gun here..."
        "But it's not like they'll find it anyway, right?"
        hide black with dissolve
        menu:
            "It will be fine":
                "Yeah, there's no chance they'll find the gun in this huge place."
            "Better find another place":
                return
    "So that's just what I do."
    "It's only as the gun leaves my hand that I think of something important."
    "Nothing seems to happen, and so I let out a sigh of relief."
    "Did I even bother to check if there were bullets left in the thing?"
    "And I'm just assuming that the damn gun is going to sink as it's made of metal."
    "For all I know, it could float like a duck!"
    "Urgh..."
    "It must be the stress of the whole Dwayne being shot dead situation."
    "I'm so wound up that I'm not thinking straight!"
    "But it's done now."
    "I've thrown it into the sea."
    "And that's the end of it."
    "Either it'll sink or the tide will take it so far out to sea it'll never be found."
    "So all that's left for me to do is turn on my heel and head back to the car."
    $ hero.lose_item("aletta_gun")
    $ hero.flags.aletta_gun = "beach"
    return

label dump_aletta_gun_forest:
    play music "<from 2 to 20>music/darren_curtis/into_oblivion.ogg" loop fadein 0.5 fadeout 5.0
    "I'd tried to think up a really clever way to dispose of the gun that Aletta used to shoot Dwayne."
    "But all I could seem to come up with was stuff like dissolving it in acid or melting it in a furnace."
    "Both of which are pretty far out ideas, even for me."
    "And I have no idea where I'd find the stuff I'd need to actually do it either!"
    "So I discarded all of those crazy notions and did the best I can to clear my mind."
    "And instead I thought of the most simple, practical place possible."
    "But even that didn't seem to work, and I just ended up getting tired."
    "I was starting to wonder if I should just go for a walk and clear my mind."
    "The woods are always a nice place to do that..."
    "And that's when it hit me - I can bury the gun in the woods!"
    "There are lots of places off the beaten path where I could bury it."
    "With the gun stashed in my pocket, I hurried to leap into the car."
    "And then I drove straight to the forest, hoping that I was not followed."
    "I parked and started walking into the trees, going as deep as I possibly can."
    with fade
    "It's only when I stop and look around that I realise something."
    "This is the perfect spot to dig a hole and bury the gun."
    "But I totally forgot to bring anything to dig with!"
    "Cursing my own stupidity, I glance around, looking for a solution."
    if hero.flags.dwayne_corpse == "forest"  and (hero.knowledge >= 85 or hero.has_skill("investigator")):
        show black at opacity(0.25) with dissolve
        "Wait..."
        "Didn't I hide Dwayne's body here already?"
        "That might not be the wisest idea to also stash the gun here..."
        "But it's not like they'll find it anyway, right?"
        hide black with dissolve
        menu:
            "It will be fine":
                "Yeah, there's no chance they'll find the gun in this huge place."
            "Better find another place":
                return
    "Soon my eyes settle on the roots of a nearby tree."
    "They're huge and gnarled, with lots of leaves and loose earth between them."
    "I dash over and get down on my knees, thrusting my hands into the earth."
    "And when my hands sink right in, I feel like my prayers have been answered."
    "Not wasting any more time, I dig away as much earth as I can."
    "Then I take out the gun, jamming it roughly into the hole I've made."
    "Scraping the earth back on top, I step back to admire my handiwork."
    "But I see that it's sticking out like a proverbial sore thumb."
    "So I take to stamping my foot on the mound of earth in an effort to flatten it down."
    "It's on the second or third stomp that I realise just how dumb what I'm doing actually is."
    "And so I stop dead, wincing as I expect to hear the sound of the gun going off."
    "Nothing seems to happen, and so I let out a sigh of relief."
    "Did I even bother to check if there were bullets left in the thing?"
    "Urgh..."
    "It must be the stress of the whole Dwayne being shot dead situation."
    "I'm so wound up that I'm not thinking straight!"
    "Even so I still don't bother to dig up the gun out and check it."
    "The fact that it didn't go off is good enough for now."
    "My fiddling with it won't help matters."
    "Instead I pile leaves and other debris on top, then retrace my steps to the car."
    $ hero.lose_item("aletta_gun")
    $ hero.flags.aletta_gun = "forest"
    return

label dump_aletta_gun_alley:
    play music "<from 2 to 20>music/darren_curtis/into_oblivion.ogg" loop fadein 0.5 fadeout 5.0
    "I'd tried to think up a really clever way to dispose of the gun that Aletta used to shoot Dwayne."
    "But all I could seem to come up with was stuff like dissolving it in acid or melting it in a furnace."
    "Both of which are pretty far out ideas, even for me."
    "And I have no idea where I'd find the stuff I'd need to actually do it either!"
    "So I discarded all of those crazy notions and did the best I can to clear my mind."
    "And instead I thought of the most simple, practical place possible."
    "But even that didn't seem to work, and I just ended up getting tired."
    "I was starting to wonder if I should just go for a walk and clear my mind."
    "Wandering in the various alleys of the city streets usually help me find peace and quiet."
    "Even though it can be noisy with all those cars and people, the lights of the street soothe my soul."
    "And that's when it hit me - I can just dump the gun here!"
    "Any random trash can will do!"
    "At first it might just sound like a really stupid idea, but that's exactly because it's so dumb that I'm sure it will work!"
    "It's brilliantly simple."
    "With the gun still stashed in my pocket, I try to find a discrete alley trash where I can hide it."
    scene bg alley with fade
    "It doesn't take me long to find what I'm looking for."
    "A large, overflowing trash can that smells like it hasn't been emptied in weeks."
    "I reach into my pocket and pull out the gun, then hesitate for a second."
    "If I just drop it on top, someone might see it."
    "So I take a deep breath and shove my hand deep into the garbage."
    "I bury the gun as deep as I can go, then pull my hand back."
    $ hero.grooming -= 10
    "The sticky and wet feeling on my skin gives me gastric reflux that I do my best to hold back..."
    "But it's done now. The gun is buried under a week's worth of rotting food and god knows what else."
    $ hero.lose_item("aletta_gun")
    $ hero.flags.aletta_gun = "alley"
    $ game.room = "alley"
    return

label dump_aletta_gun_pond:
    play music "<from 2 to 20>music/darren_curtis/into_oblivion.ogg" loop fadein 0.5 fadeout 5.0
    "I'd tried to think up a really clever way to dispose of the gun that Aletta used to shoot Dwayne."
    "But all I could seem to come up with was stuff like dissolving it in acid or melting it in a furnace."
    "Both of which are pretty far out ideas, even for me."
    "And I have no idea where I'd find the stuff I'd need to actually do it either!"
    "So I discarded all of those crazy notions and did the best I can to clear my mind."
    "And it's only when I passed nearby that I notice this perfect hiding spot."
    "The park's pond."
    "At this time the park is quiet, save for the gentle rustling of the leaves and the distant sound of city life."
    "The pond surface reflects the moonlight like a dark, polished mirror."
    "I reach into my pocket and feel the cold weight of the gun. My heart beats a little faster as I pull it out."
    "I take one last look around to make absolutely sure I'm alone."
    "Then, with a swift motion, I toss the gun as far as I can, aiming for the middle of the pond."
    "There's a soft {i}plop{/i} as it breaks the surface, followed by a series of concentric ripples that slowly fade away."
    "I watch for a moment, waiting for the water to settle back into its tranquil state."
    "I feel a weight lifting off my shoulders as I now know that it's now deep under the dark water, where hopefully no one will ever think to look."
    $ hero.lose_item("aletta_gun")
    $ hero.flags.aletta_gun = "pond"
    $ game.room = "pond"
    return


label dwayne_corpse_discovery:
    scene bg livingroom with fade
    "It's been another one of those days at the office, a real head-banger for me."
    "On top of the usual pile of work, I've got Aletta slowly coming apart at the seams."
    "Then there's Cherie, trying to take over the company and cover up Dwayne's murder at the same time."
    "And finally you have me, sandwiched in the middle of it all and with as much to lose as anyone."
    "Luckily for me, the house is dark and quiet when I walk in through the front door."
    if not sasha.hidden and not bree.hidden:
        mike.say "Sasha..? [bree.name]..?"
    elif not sasha.hidden:
        mike.say "Sasha..?"
    elif not bree.hidden:
        mike.say "[bree.name]..?"
    if not minami.hidden:
        mike.say "Minami..?"
    if Harem.together(samantha, name='home') and not samantha.hidden:
        if Harem.together(lexi, name='home') and not lexi.hidden:
            mike.say "Sam..? Lexi..?"
        else:
            mike.say "Sam..?"
    elif Harem.together(lexi, name='home') and not lexi.hidden:
        mike.say "Lexi..?"
    mike.say "Anyone home?"
    "There's no answer, and so I breathe a sigh of relief and make straight for the sitting-room."
    "Once there, I waste no time in kicking off my shoes and collapsing onto the sofa."
    "My hand finds the remote control without the need for a conscious thought."
    "And when I switch the TV on, it flickers to life showing one of the local news channels."
    "Anchor" "And now we go live to our reporter on the scene..."
    "Anchor" "So, what can you tell us about this developing story?"
    "I'm only half listening to what's being said and unaware of what's on the screen."
    "To my tired brain it sounds like any other supposedly important story on the news."
    if hero.flags.dwayne_corpse == "beach":
        show bg beach at police_lights
    elif hero.flags.dwayne_corpse == "forest":
        show bg forest at police_lights
    elif hero.flags.dwayne_corpse == "mansion":
        show bg mansionentrance at police_lights
    show concert_solo_npc_kleio at blacker, center, zoomAt(1.0, (940, 840))
    show concert_solo_nohaircut_kleio at blacker, center, zoomAt(1.0, (940, 840))
    show concert_solo_outfit_date_kleio at blacker, center, zoomAt(1.0, (940, 840))
    show tv overlay
    with fade
    "And my eyes are only vaguely registering the sight of a reporter talking to the camera."
    "Reporter" "Police are being careful as to what they tell us at the moment..."
    "Reporter" "But suffice to say, we have been told that the body's been identified."
    "Reporter" "And it is none other than missing business mogul and philanthropist, Dwayne Jackson!"
    "The reporter says the name in that serious, dramatic fashion that they use."
    "And that's the first thing that really cuts through the funk I'm in and reaches my brain."
    "Suddenly I'm wide awake, leaning forward in my seat and turning up the volume on the TV."

    if hero.flags.dwayne_corpse == "beach":
        "Reporter" "We understand that the body was found here, by a passerby…"
        "The reporter turns to gesture to the beach, stretching out behind them."
        "Reporter" "Wrapped in a fishing net and washed up with the tide."
        if hero.flags.aletta_gun == "beach":
            "Reporter" "A firearm was also recovered nearby, which is thought to be the murder weapon."
        "I feel like slapping myself as hard as I possibly can."
        "Why in the hell did I think tossing the body into the sea would work?"
        "I mean, shit washes up on the shore all the time."
        "So a shit the size and magnitude of Dwayne was sure to end up there in the end."
        if hero.flags.aletta_gun == "beach":
            "Not to mention the gun - why did I think it was a good idea to hide it in the same place?!?"

    elif hero.flags.dwayne_corpse == "forest":
        "Reporter" "We understand that the body was found here, by a passerby…"
        "The reporter turns to gesture to the trees, stretching out behind them."
        "Reporter" "Buried in a shallow grave and with signs of animal predation."
        if hero.flags.aletta_gun == "forest":
            "Reporter" "A firearm was also recovered nearby, which is thought to be the murder weapon."
        "I feel like slapping myself as hard as I possibly can."
        "Why in the hell did I think burying the body in the woods would work?"
        "I mean, you read about people walking their dogs there finding bodies all the time."
        "So how was this one going to be any different?"
        if hero.flags.aletta_gun == "forest":
            "Not to mention the gun - why did I think it was a good idea to hide it in the same place?!?"

    elif hero.flags.dwayne_corpse == "mansion":
        "Reporter" "We understand that the body was found here, by police..."
        "The reporter turns to gesture to the house behind them, cordoned off with police tape."
        "Reporter" "When police responded to reports of a rotten smell emanating from the basement."
        if hero.flags.aletta_gun == "mansion":
            "Reporter" "A firearm was also recovered nearby, which is thought to be the murder weapon."
        "I feel like slapping myself as hard as I possibly can."
        "Why in the hell didn't I make Cherie get rid of the damn body?"
        "I should have known that a shit the size and magnitude of Dwayne would stink."
        "More than enough for someone to smell it a mile off too."
        if hero.flags.aletta_gun == "mansion":
            "Not to mention the gun - why did I think it was a good idea to hide it in the same place?!?"
    "Reporter" "We are lead to understand that Cherie Jackson..."
    "Reporter" "Mister Jackson's wife...and widow..."
    "Reporter" "Reported her husband as missing to authorities when he failed to return from a business trip abroad."
    "Reporter" "But the discovery of his body now throws that narrative into question, suggesting he never left town."
    "I do the best I can to keep calm and listen to what the reporter's saying."
    "Trying to pick out the relevant information from the usual salacious gossip."
    "Aware that saving my ass and those of everyone involved could depend on it."
    "Reporter" "Of course, the police are being very tight-lipped and refusing to divulge many details."
    "Reporter" "But we understand that Mister Jackson's death is now officially being investigated as a homicide."
    "Reporter" "Though it is already a matter of public record that Jackson and his company were under scrutiny from financial authorities."
    "Reporter" "And on top of that, his personal life was the subject of much speculation and rumour."
    "Reporter" "So there is understandable speculation as to whether this could be a case of personal, or professional revenge."
    scene bg livingroom with fade
    "The report comes to an end, and that anchor starts talking about another story."
    "But there's no way I can even hope to make sense of what they're saying."
    "Because my mind is already going over everything that I heard again and again."
    "Analysing it in painfully minute detail as I begin to obsess on what it could mean."
    "The temptation is to pull out my phone and instantly call Cherie or Aletta."
    "But I stop myself by sheer force of will, because that would look pretty suspicious."
    "And who knows - the police might already have started watching all of the suspects."
    "Listening in to our phone calls and reading our emails."
    "No, I should wait and talk to them at the office tomorrow."
    "As there's less chance of us being overheard or spied on there."
    "Though I get the feeling I might have a long, sleepless night ahead of me before then."
    $ hero.fun -= 7
    return


label dwayne_murder_mike_arrest:
    scene bg bedroom1 at blur(16), dark, dark with fade
    "It seems to be the middle of the night when I wake up, alerted by intruders in my bedroom."
    scene bg bedroom1
    "At first I have a panic reaction, but when I see the police uniforms, I understand."
    "And I know what the reason must be even before I raise from my bed."
    "Because the truth is that I've been waiting for this moment to come."
    show inspector at center, zoomAt(1.0, (840, 720))
    show camila work at center, zoomAt(1.0, (440, 720))
    with dissolve
    show inspector at center, traveling(1.25, 0.5, (840, 900))
    show camila at center, traveling(1.25, 0.5, (440, 880))
    "So when I see Detective Michaels and Camila walking towards me, it comes as no surprise."
    "And the fact that they have grim determination written all over their faces just proves it."
    "The game is finally up, as they're here to arrest me."
    "I make a point of standing and holding out my hands as they reach my desk."
    "Hoping that they'll understand it means that I'm going to come quietly."
    show inspector at startle(0.1, -5)
    "Michaels" "[hero.name] [hero.family_name]…"
    "Michaels" "You are under arrest on suspicion of the murder of Dwayne Jackson."
    "Michaels" "You do not have to say anything..."
    "Michaels" "But it may harm your defence if you do not mention when questioned something which you later rely on in court."
    "Michaels" "Anything you do say may be given in evidence."
    "I keep my lips firmly closed all the time Michaels is reading me my rights."
    "And when he's done, the detective gives Camila a nod."
    show camila upset at center, traveling(1.5, 0.3, (540, 1040))
    "Then she steps forwards, pulling out her handcuffs and using them to bind my wrists."
    "But as she's doing so, we're close enough that nobody else can overhear us."
    show camila angry
    camila.say "The evidence we've got on you is air-tight."
    camila.say "What kind of maniac keeps his victim's corpse as a souvenir?!?."
    camila.say "I hope they lock you up and throw away the key!"
    show camila upset
    "I could say something in response to that."
    "But what good would it do me?"
    "If Camila's telling the truth, of course she's going to hate me."
    "No, better to hold my tongue and try to hold onto a shred of my dignity."
    show inspector at center, traveling(1.25, 0.3, (640, 900))
    show camila at center, traveling(1.25, 0.3, (340, 880))
    "I can hear my roomates voices echoing from elsewhere in the house, but I don't understand a single word."
    "Police officers must prevent them from interfering with my arrest."
    show bg livingroom with dissolve
    "But I'm already being led away as they lead me outside, and I can't look back."
    "So I guess that's the end of my story, at least as a free man."
    scene bg house at center, zoomAt(1.5, (640, 1040)), blur(5)
    show hypnosis arrest
    show layer master at police_lights
    with dissolve
    "Dwayne's dead, Aletta's free of his tentacles and Cherie gets the company."
    "And as for me, I suppose I get to take the blame for it all."
    "As well as a private cell in which to sit and dwell on where it all went wrong."
    scene bg black with dissolve
    pause 1.0
    $ renpy.full_restart()
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
