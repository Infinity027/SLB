init python:
    Consumable("kylie_cookies", display_name="Kylie's cookies", effects=[("fun", 1), ("hunger", 1)], frequency_limit="day", label="kylie_cookies")

    Event(**{
    "name": "kylie_give_a_gift",
    "label": "npc_give_a_gift",
    "conditions": [
        Or(
            HeroTarget(IsBirthday()),
            IsSpecialDate("christmas"),
            IsSpecialDate("valentine"),
            ),
        PersonTarget(kylie,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "girl": "kylie",
    "once_day": True,
    "do_once": False,
    "quit": False,
    }
    )

    Event(**{
    "name": "kylie_give_christmas_murder",
    "label": "kylie_give_christmas_murder",
    "conditions": [
        IsSpecialDate("christmas"),
        IsHour(6, 12),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home")),
        PersonTarget(kylie,
            Not(IsHidden()),
            MinStat("love", 50),
            MinStat("yandere", 90),
            Not(IsFlag("target", False)),
            Not(IsFlag("schedule", "jail")),
            ),
        ],
    "once_day": True,
    "music": "music/darren_curtis/come_out_and_play.ogg",
    "do_once": False,
    "quit": False,
    })

label kylie_give_male:
    "Kylie gives me home made cookies."
    mike.say "Thank you, Kylie."
    $ hero.gain_item("kylie_cookies")
    hide kylie
    return

label kylie_give_valentine_male:
    "Kylie walks hesitantly towards me."
    call kylie_greet from _call_kylie_greet_7
    show kylie
    kylie.say "Happy valentine's day [hero.name]..."
    call kylie_give_male from _call_kylie_give_male
    return

label kylie_give_birthday_male:
    "Kylie walks towards me."
    call kylie_greet from _call_kylie_greet_8
    show kylie happy
    kylie.say "Happy birthday [hero.name]!"
    call kylie_give_male from _call_kylie_give_male_1
    return

label kylie_give_christmas_male:
    "Kylie walks towards me."
    call kylie_greet from _call_kylie_greet_9
    show kylie happy
    kylie.say "Merry Christmas [hero.name]."
    call kylie_give_male from _call_kylie_give_male_2
    return

label kylie_give_christmas_murder:
    scene bg livingroom
    "You may not be surprised to hear this, but as our house is basically three pretty casual friends under one roof, we don't really have any Christmas traditions as such."
    "Sure, we always talk vaguely about getting together to have a meal so that we can at least do something to mark the occasion and we always swap dumb little gifts."
    "But what usually happens is that we each end up partying on the night of Christmas Eve with our own friends and then crawling out of bed later in the day, still reeling from the night before."
    "Then the most that we can manage is to crash out on the sofas, find a takeaway that's delivering and stare at something vaguely seasonal in an amiable silence."
    "Not exactly everyone's ideal image of an average Christmas Day, I know."
    "But then we're not the average household either."
    "The reason that I'm telling you all of this is to explain why I'm so puzzled to hear someone knocking at the door on this particular Christmas Morning."
    "I glance at the clock on the bedside table, seeing that it's well before midday."
    "That's a small comfort at least, knowing that I haven't overslept."
    "While I'm congratulating myself on this achievement, the knocking at the door begins again."
    "Doesn't look like they're going to get tired of trying to raise an answer and just go away any time soon."
    "And so with a fuzzy head and the threat of a hangover looming, I crawl out of bed and pull on just enough clothes to qualify as decent."
    "On my way down to the front door, I can still hear the knocking as it continues on."
    mike.say "Alright, alright...I'm coming as fast as I can!"
    mike.say "Jesus - who's in this much of a hurry on a national fucking holiday!"
    scene bg house
    show kylie christmas happy
    "I'm greeted with the sight of an extremely perky Kylie, positively beaming with the spirit of the festive season."
    kylie.say "Surprise, [hero.name]!"
    kylie.say "Happy Christmas!"
    "I open my mouth to say something appropriate in response, but nothing comes out."
    "Despite the fact that it's damn cold outside and there's snow on the ground, Kylie's not exactly wrapped up against the Winter chill."
    "She has on one of those outfits that's a combination of red and white, showing off as much flesh as possible without being positively indecent."
    "I can't honestly tell if she's supposed to be Mrs Santa Claus reminding her husband that she's all woman, or some kind of over-sexed elf."
    "But either way, the effect is the same and it renders me utterly speechless."
    "Kylie giggles at my evident state of confusion, the sweetness of the sound only serving to make matters worse."
    kylie.say "Oh, [hero.name], what a reaction - I'm so flattered!"
    mike.say "Erm...yeah...you're welcome, I guess."
    kylie.say "Anyway, I suppose you're wondering why I'm here?"
    "I rub the back of my head and nod."
    mike.say "Well...the thought had crossed my mind..."
    "At this, Kylie cocks her head on one side and gives me one of those amused smiles people use when they think the other person isn't all together there."
    kylie.say "Can't you guess?"
    "I have to shake my head, admitting that I'm still stumped on that particular question."
    kylie.say "I came to give you your Christmas present, silly!"
    "As she turns to retrieve something from behind her, bending over to pick it up, the short skirt of her outfit rides up even further and I'm treated to quite a view."
    "Trying to cover up my amazement at Kylie who then proceeds to wiggle her backside as she stands back up, I blurt out the first thing that comes into my mind."
    hide kylie
    show kylie gift
    mike.say "You really shouldn't have, Kylie."
    mike.say "I feel really bad, because...because I don't have a gift to give you in return!"
    "Kylie waves away my apologies with one hand, using the other to clutch the box she just picked up."
    "It's maybe a foot on each side and wrapped in typically gaudy paper with a bow and label on top."
    kylie.say "Don't be ridiculous, [hero.name]."
    kylie.say "Knowing that you like my outfit was the best gift you could have given me!"
    kylie.say "Now don't keep me in suspense all morning - open your present!"
    "I nod, trying to shake off the funk that I'm in and focus on doing as she says."
    "The way I see it, that's the easiest way to get out of this rather awkward situation."
    "Whatever's inside the box is quite heavy, and seems to be loose in there, as I can feel it rolling around as I handle the parcel."
    "Trying to make a good show of it, I shake the thing, but no discernible sounds can be heard to reward my efforts."
    "Looks like there's nothing for it but to get on with it and actually open the thing."
    "Holding the box in the crook of one arm, I use my free hand to tear at the wrapping paper and start to pry open the lid."
    "It's at this point that I notice the bottom of the box feels oddly damp against the bare skin of my arm."
    "But then I remember that Kylie just plucked this thing off of the path, so no wonder it feels wet."
    "Struggling with the last of the paper around the lid, I give Kylie what I hope is a positive look, just to show I'm still doing as I'm told."
    "And in return, I get an excited smile and a flapping of her hands that I assume is meant to encourage me to go faster still."
    "When I finally tear away the last of the paper and open the top of the box, the first thing I see is what looks like hair."
    hide kylie
    $ renpy.show("kylie gift " + kylie.flags.target)
    "What in the hell did she get me - a damn wig?!?"
    "But then I remember the circumstances and that I need to be delighted with it, even if it's a box of roadkill."
    show kylie gift yandere
    "Grabbing a handful of the hair, I try to turn whatever it is over and get a better look."
    "There's a flash of something so pale that it's almost white."
    "And then I drop the box, almost tossing it away from me as I see something that stares back."
    "It's an eye, glassy and utterly dead."
    "I fall over my own feet and collapse onto my ass on the path, struggling ineptly to crawl away from the contents of the box."
    "My foot kicks out and sends it rolling out onto the virgin snow that covers the lawn."
    "All at once I get the answer to the two burning questions of the morning."
    $ target = Person.find(kylie.flags.target)
    "Now I know what was in the box and why [target.name] did not answer my call back home last night."
    "There on the lawn, staring up at the sky with dead eyes, is [target.name]'s severed head."
    "Her mouth is open, as if in some last terrible scream."
    "Her hair streaked and stained with blood from the ragged stump of her neck."
    "I can't make sense of what I'm seeing, as if my mind refuses to process the evidence of my eyes as it knows what the consequences of doing so will be."
    "Part of me can't understand why someone would put [target.name]'s head in a box and give it to Kylie."
    "Another is worried that [target.name]'s going to come home any moment and be horrified to see her own head tossed out on the lawn like garbage."
    "My mouth starts to work silently, trying to ask Kylie if she knows what's going on."
    hide kylie
    show kylie christmas yandere
    kylie.say "Hey there, hey now!"
    "I feel the sensation of her sitting down behind me, cradling my body against her own."
    kylie.say "It's okay, everything's okay."
    "Still in a state of hopeless confusion, I can't help being comforted by her words and the feeling of her pulling me close."
    kylie.say "This wasn't what I wanted - you know that, right?"
    kylie.say "I love you, [hero.name], and I always will, no matter what."
    kylie.say "But she was in the way, so she had to go - that's all there is to it!"
    "I make an effort to move, the implications of what Kylie's telling me only now starting to sink in."
    kylie.say "Uh-uh, no struggling now."
    kylie.say "You'll ruin this perfect moment!"
    if renpy.has_label("kylie_achievement_4") and not game.flags.cheat:
        call kylie_achievement_4 from _call_kylie_achievement_4
    if renpy.has_label("kylie_achievement_8") and not game.flags.cheat and game.week_day == 5 and game.day == 13:
        call kylie_achievement_8 from _call_kylie_achievement_8_1
    show kylie a christmas blush knife
    "I don't feel the blade that she uses to slice open my throat, only hear the gasping sound of air escaping from the gaping hole."
    "My body begins to twitch and spasm, but Kylie clutches me to her all the same."
    show kylie a christmas happy knife bloodyknife bloodyface
    kylie.say "You see, after I killed her, I had what you might call an epiphany of sorts."
    kylie.say "I realised that the thing that's kept us apart was never you or me - it was other women, always trying to come between us."
    kylie.say "The only way we can ever be together is if there's no other women to do that."
    kylie.say "But I can't kill every other woman on the face of the Earth."
    scene bg house at blood
    show kylie a christmas happy knife bloodyknife bloodyface at center, blood
    with dissolve
    kylie.say "Believe me - I would if I could, [hero.name], and all for you!"
    kylie.say "So I decided to do the only other thing that would work, and kill you instead."
    kylie.say "That way you'll always be perfect, just how I remember you."
    kylie.say "And always be mine, because I'll be the last person to hold you close, keep you warm and tell you that I'll always love you..."
    "She keeps on talking, telling me things that I can't hear and wouldn't matter to me even if I could."
    scene bg house at blur(8), blood
    show kylie a christmas happy knife bloodyknife bloodyface at center, blur(8), blood
    with dissolve
    "I'm dying in her arms, getting colder and farther away from the world with every second that passes."
    "Soon there's nothing but blurred colours and incoherent sounds, my own thoughts also losing all meaning."
    "Then there's just a confused mass of sensations that have no beginning or end."
    "And then there's nothing..."
    scene bg black with dissolve
    pause 1.0
    $ renpy.full_restart()
    return

label kylie_birthday_gift_male:
    show kylie
    if kylie.flags.birthdayknown:
        mike.say "Happy birthday Kylie."
        kylie.say "How sweet, you remembered my birthday!"
    else:
        kylie.say "How do you know my birthday?"
        mike.say "I didn't, it's just pure luck."
        $ kylie.flags.birthdayknown = True
    return

label kylie_gift_swimsuit_male:
    show kylie happy
    kylie.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy swimsuit."
    if kylie.sub >= 60:
        show kylie blush
        kylie.say "It's so pretty, thank you [hero.name]."
        $ kylie.flags.sexyswimsuit = True
    else:
        show kylie angry
        $ kylie.love -= 4
        kylie.say "Thanks but no thanks [hero.name]."
        kylie.say "You think I would wear that?"
        $ hero.cancel_activity()
    return

label kylie_gift_sexy_dress_male:
    show kylie happy
    kylie.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy dress."
    if kylie.sub >= 30:
        show kylie blush
        kylie.say "Thank you [hero.name]."
        $ kylie.flags.sexydate = True
        $ kylie.flags.sluttydate = False
    else:
        show kylie angry
        $ kylie.love -= 4
        kylie.say "Thanks but no thanks [hero.name], I would feel very awkward with that..."
        $ hero.cancel_activity()
    return

label kylie_gift_slutty_dress_male:
    "There's no way of avoiding the fact that Kylie's in possession of an impressive figure."
    "At times she reminds me of one of those ancient idols of the Earth Mother archaeologists dig up."
    "All curves and bulges, with no straight lines or hard edges in sight."
    "And so I naturally feel the urge to make the absolute most of that same figure."
    "So, to that end, when I saw something that would achieve my goal, I just had to buy it."
    "Now I'm waiting for the right moment to offer it up as a tribute to my own personal goddess."
    "I just hope that she looks on it with divine favour, rather than heavenly wrath!"
    mike.say "Kylie..."
    mike.say "I know it's not a special occasion or anything like that..."
    mike.say "But I went ahead and got you a little something."
    "I pull the box out from behind my back and offer it to Kylie."
    "Who seems delighted with the idea of me giving her a gift."
    "But oddly, not nearly as surprised as I was expecting her to be."
    show kylie talkative
    kylie.say "[hero.name]…"
    kylie.say "You shouldn't have!"
    kylie.say "I've been wondering what this was..."
    kylie.say "Ever since I saw you sneaking it home the other night."
    show kylie normal
    "I'm feeling more than a little discombobulated by the whole affair of giving Kylie the gift."
    "And so I must not be hearing what she's saying correctly."
    mike.say "Huh?"
    mike.say "What was that?"
    show kylie talkative
    kylie.say "Oh..."
    kylie.say "I mean...since I saw it poking out from behind your back just now!"
    show kylie normal
    "That seems to make sense and explain things enough for my already addled brain."
    "And so I choose to forget about it and just focus on what's really important."
    "Which is making sure that Kylie likes her gift."
    mike.say "Well..."
    mike.say "Are you going to open it?"
    show kylie smile
    play sound [paper_ripping_1, paper_ripping_2]
    "Kylie smiles and proceeds to tear off the wrapping-paper."
    "Then she opens the box and pulls out the contents."
    "And I can't help grinning as I see the stunning dress I picked out for her unfold."
    "Or I should say, the stunning and very daring dress that I fantasised about seeing her in."
    mike.say "What do you think, Kylie?"
    mike.say "Is that a conversation-stopper, or what?"
    if kylie.sub >= 70:
        "I see Kylie's eyes scan the dress, looking it up and down."
        "But the weird thing is that she doesn't react like I expected her to."
        "Because there's no sign of an emotional reaction in her eyes."
        "I was prepared for her to love or hate the dress."
        "Instead she seems to be looking at me now, more than at it."
        show kylie talkative
        kylie.say "So..."
        kylie.say "You...like this dress?"
        show kylie normal
        mike.say "Yeah, Kylie - very much so!"
        mike.say "And I think it'd look great on you."
        show kylie shy
        "Almost as soon as I explain my feelings, Kylie seems to come alive."
        "Her face lights up and she gives me a huge, delighted smile."
        kylie.say "Then I love it too."
        kylie.say "And I can't wait to wear if for you!"
        show kylie smile
        "I feel a little thrown by Kylie's odd reaction to all of this."
        "But I choose to put that down to the pressure she must have been under just now."
        "Like, I was a bag of nerves giving the dress to her myself."
        "So she must have been in just the same state receiving it."
        "Most likely she just didn't know how to react when put on the spot."
        "And my worries soon begin to fade as I think about the promise she just made."
        "Because the thought of that figure in that dress..."
        "Well that is a thing worth bowing down and worshipping!"
        $ kylie.flags.sluttydate = True
        $ kylie.flags.sexydate = False
    else:
        "I see Kylie's eyes scan the dress, looking it up and down."
        "But the weird thing is that she doesn't react like I expected her to."
        "She's shaking her head, rather than nodding it and smiling."
        show kylie vangry
        kylie.say "No, no, no..."
        kylie.say "This isn't how it's supposed to be."
        kylie.say "This is all wrong!"
        show kylie angry
        mike.say "What do you mean, Kylie?"
        mike.say "I bought you the dress as a surprise..."
        mike.say "So how can it be wrong?"
        "Still shaking her head, Kylie thrusts the dress back into my open hands."
        show kylie vangry
        kylie.say "I've seen how this is supposed to go, [hero.name]..."
        kylie.say "And it's really important that we get it right, you and me."
        kylie.say "But don't worry, because I'm going to give you another chance."
        kylie.say "Just...make sure you get it right this time."
        show kylie angry
        "Kylie phrases that last bit as a statement, rather than a question."
        "And before I can ask her what the hell she means, she turns on her heel."
        "Then she walks away, leaving me holding the dress and feeling totally clueless."
        $ kylie.love -= 10
        $ hero.cancel_activity()
    return

label kylie_gift_collar_male:
    show kylie happy
    kylie.say "Oh, hey, [hero.name]."
    "Kylie gives me a smile of her own, one that barely manages to keep from becoming a rictus thanks to her insatiable curiosity."
    "It's when my hand reaches into my pocket and I see Kylie begin to absently play with the ring finger of her left hand that everything finally begins to make sense."
    "She thinks that I'm going to produce a ring and propose to her!"
    "Well, I suppose this is what you get for jumping to conclusions like that..."
    mike.say "Okay, Kylie, no more beating about the bush."
    mike.say "I really wanted to ask you something."
    "By this time, I can see that Kylie's eyes are almost burning with a manic intensity, as she leans forward to hear what I have to say next."
    mike.say "Since we first got reacquainted with each other, you've made me very happy, Kylie."
    mike.say "But I've always felt like there was something missing between us."
    mike.say "That you were almost crying out for some kind of gesture from me, some kind of commitment."
    mike.say "And not something shallow or frivolous either - a serious commitment, one that would fill a gaping void that you have inside of yourself."
    "While I'm apparently in the act of pouring my heart out to her, Kylie nods faster and with more intensity with each passing second."
    "And after all, why the hell not - I'm telling her everything that I'm sure she wants to hear from me."
    mike.say "So that's why I went out and had this made, especially for you."
    mike.say "And I'd be honoured if you'd wear it, day and night, together and apart, as a symbol of my feelings for you?"
    "I choose that moment to finally whip out what's been concealed in my pocket and dangle it in front of Kylie's wide, almost glazed over eyes."
    kylie.say "Oh, [hero.name], I've dreamed of this day ever since I was a girl!"

    kylie.say "You just can't imagine how many times I've pictured the day that you ask me to wear your...DOG COLLAR?!?"
    "See, I told you that I had a surprise in store for her, even if it wasn't the kind she was expecting."
    "I continue to ignore the flabbergasted look on Kylie's face and push straight on with my patter."
    mike.say "Let's face it, Kylie - you're more than a little wild at times!"
    mike.say "Well...if I'm honest, you're seriously wild most of the time!"
    mike.say "But don't get me wrong - I'm really into that craziness."
    mike.say "I just think that, if you're honest, what you're actually crying out for is someone to put a leash on you, figuratively and literally."
    "Kylie's eyes keep darting from my face and down to the collar, where the tag clearly reads 'CRAZY'."
    mike.say "Like I already said, Kylie - I want to make a commitment to you."
    mike.say "And I think I can do that best if you'll consent to take me as your master and be my bitch."
    mike.say "So what do you say?"
    "Kylie says nothing at first, and at the same time her face is almost impossible to read."
    "But the way her eyes are darting here and there and the time she's taking makes me certain that she's weighing up her options and considering all of the angles."
    "We both know that she wanted a marriage proposal and a ring from me, but essentially what she wants is to have me commit myself to her."
    "And what I'm offering does just that, even if it's not strictly in the way that she anticipated."
    show kylie happy
    kylie.say "If it means that I get to be with you, [hero.name], then I'll be whatever you want me to be."
    "Kylie smiles as she lifts her hair and lets me fasten the collar around her neck."
    $ kylie.set_sex_slave()
    hide kylie
    show kylie blush
    "And when it's in place, I can't help but think that it actually looks really good, like it's the missing part of her personality."
    "On another girl, a more normal and well-balanced type of girl, it would probably look downright weird."
    "But somehow it just works as an early warning that Kylie's quirky and more than a little crazy - but of course, in a good way!"
    kylie.say "So, when do we get to start the obedience training?"
    mike.say "Hold on there, girl!"
    mike.say "You're getting a bit ahead of yourself there."
    mike.say "We need to teach you to walk to heel before we get into any of that!"
    "I can see Kylie warming to idea more as each second passes and her mind considers the possibilities."
    "And a part of me wonders how responsive she'll be to obedience training after all."
    return

label kylie_gift_butt_plug_male:
    show kylie happy
    kylie.say "Oh, [hero.name], is it for me?"
    "She unwraps the butt plug."
    if kylie.sub <= 50 or not kylie.sexperience:
        show kylie annoyed
        kylie.say "..."
        kylie.say "Keep it... I don't want it so keep it."
        kylie.say "I'm sure you'll have a better use of it than me."
        $ hero.cancel_activity()
    else:
        show kylie blush
        kylie.say "It's perfect!"
        kylie.say "Thanks [hero.name], I'll make a good use of it."
        $ kylie.flags.buttplug = True
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
