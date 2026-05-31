init python:
    Event(**{
    "name": "palla_audrey_date",
    "label": "palla_audrey_date",
    "gallery": {"conditions": [IsDone("palla_audrey_date")], 'character':'palla', 'label':'palla_audrey_date', 'id':'Palla/Audrey', 'icon': 'bitchy threesome pallafuck', 'scene': 'restaurant'},
    "priority": 500,
    "conditions": [
        IsDone("palla_event_08"),
        HeroTarget(
            IsActivity("date_eat_restaurant"),
            IsRoom("date_restaurant"),
            HasStamina(),
            ),
        PersonTarget(palla,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("noaudrey", False),
            MinStat("love", 160),
            MinStat("lesbian", 10),
            ),
        PersonTarget(audrey,
            MinStat("love", 140),
            MinStat("lesbian", 10),
            MinStat("sexperience", 1),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "palla_audrey_date_areyoumad",
    "label": "palla_audrey_date_areyoumad",
    "priority": 500,
    "conditions": [
        IsDone("palla_audrey_date"),
        PersonTarget(palla,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("nothreesome"),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "palla_audrey_date_apology",
    "label": "palla_audrey_date_apology",
    "priority": 500,
    "conditions": [
        IsDone("palla_audrey_date"),
        PersonTarget(palla,
            IsPresent(),
            Not(IsHidden()),
            IsFlag("nothreesome", False),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "cassidy_audrey_showdown",
    "priority": 500,
    "label": "cassidy_audrey_showdown",
    "conditions": [
        'Harem.together("audrey", "palla", name="bitchy")',
        HeroTarget(
            Not(OnDate()),
            HasRoomTag("mcoffice"),
            ),
        PersonTarget(cassidy,
            Not(IsHidden()),
            HasRoomTag("work"),
            Not(IsFlag("status", "mistress")),
            ),
        PersonTarget(audrey,
            Not(IsHidden()),
            HasRoomTag("work"),
            ),
        "Person.showdown(cassidy, audrey)"
        ],
    "do_once": True,
    })

    Event(**{
    "name": "cassidy_palla_showdown",
    "priority": 500,
    "label": "cassidy_palla_showdown",
    "conditions": [
        'Harem.together("audrey", "palla", name="bitchy")',
        HeroTarget(
            IsRoom("date_nightclub"),
            ),
        PersonTarget(cassidy,
            OnDate(),
            ),
        PersonTarget(palla,
            Not(IsHidden()),
            ),
        "Person.showdown(cassidy, palla)"
        ],
    "do_once": True,
    })

    Event(**{
    "name": "cassidy_bitchy_harem",
    "priority": 1000,
    "label": "cassidy_bitchy_harem",
    "conditions": [
        IsDone("cassidy_audrey_showdown", "cassidy_palla_showdown"),
        PersonTarget(cassidy,
            Not(IsHidden()),
            IsFlag("audreyshowdown"),
            IsFlag("pallashowdown"),
            ),
        PersonTarget(audrey,
            Not(IsHidden()),
            ),
        PersonTarget(palla,
            Not(IsHidden()),
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "bitchy_harem_foursome_request",
    "priority": 500,
    "label": "bitchy_harem_foursome_request",
    "conditions": [
        'Harem.together("audrey", "cassidy", "palla", name="bitchy")',
        HeroTarget(
            Not(OnDate()),
            Or(
                IsRoom("nightclub", "nightclubbar"),
                HasRoomTag("mall_southside")
               ),
           ),
        PersonTarget(audrey,
            Not(IsHidden())
            ),
        PersonTarget(palla,
            Not(IsHidden())
            ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "bitchy_harem_foursome_ask_cassidy",
    "priority": 500,
    "label": "bitchy_harem_foursome_ask_cassidy",
    "conditions": [
        IsDone("bitchy_harem_foursome_request"),
        'Harem.together("audrey", "cassidy", "palla", name="bitchy")',
        HeroTarget(Not(OnDate())),
        PersonTarget(cassidy,
                     IsActive(),
                     ),
        ],
    "do_once": True,
    })

    Event(**{
    "name": "bitchy_harem_nightclub_encounter",
    "label": "bitchy_harem_nightclub_encounter",
    "priority": 500,
    "conditions": [
        HeroTarget(IsGender("male")),
        And(
            HeroTarget(
                IsActivity("dance_with"),
                OnDate()
                ),
            PersonTarget(cassidy,
                         IsActive(),
                         IsFlag("bitchyHaremAgree", True)
                         ),
            ),
        ],
    "do_once": True,
    })

label palla_audrey_date:
    scene bg restaurant
    show restaurant meal palla
    with fade
    "Palla and I casually chat while we wait for our food."
    "The food has just arrived when I realize something very odd. Palla hasn't said anything bitchy about me or the other patrons or the food or the restaurant even once."
    "She also hasn't been extra needy and clingy either, and those are the only two modes I'm used to seeing her in."
    show restaurant meal palla pallahappy
    "Instead, she's been sunshine and giggles."
    "And to be honest, it's great. When Palla smiles at me, it makes me feel like I'm the only person in the restaurant."
    show restaurant meal palla pallabored
    palla.say "[hero.name], are you even listening to me?"
    mike.say "Sort of, Palla. I mean yes, but I'm dazzled by your smile. I feel like I'm seeing a side of you I don't see a lot."
    show restaurant meal palla pallablush
    palla.say "Do you like it?"
    mike.say "I did say dazzled, right?"
    hide restaurant meal palla
    show palla normal date normal at center, zoomAt(1.5, (640, 1140))
    with fade
    palla.say "Well yes, but you're often at a loss for words because you're dim, not because I'm beautiful."
    "I purse my lips. I guess not being bitchy couldn't last. But before I can say anything she laughs."
    palla.say "Relax, [hero.name], I'm just teasing."
    "She puts her hand in my lap."
    palla.say "And you know what? I think I'm hungry but for something not on my plate here."
    mike.say "Oh. And you're hoping I'll feed you?"
    "Her eyes twinkle, and her voice is full of mischief."
    palla.say "Well, you wouldn't let a gorgeous redhead starve to death at the table, would you?"
    hide palla at zoomAt(1.5, (640, 1140)) with moveoutbottom
    "And with that she slips beneath the table. I get stiff before she even has a chance to unzip my fly."
    show palla restaurantbj with fade
    palla.say "Now don't let anyone know I'm down here!"
    show palla restaurantbj suckdick
    "She touches her lips to the tip of my head, which responds. My eyes go half-lidded while she works me."
    "She takes her time, too, caressing me gently with her tongue. So many times she just tries to get this kind of thing over with, but this time it's like she's worshipping my phallus, and it's fucking amazing."
    "...and then I see Audrey, walking right towards my table. Well, this is awkward."
    mike.say "Shit, Palla, don't move. Audrey is coming."
    hide palla restaurantbj suckdick
    show audrey date zorder 2 at center
    audrey.say "Hey [hero.name]! Fancy meeting you here! Do you mind if I join you?"
    "Holy crap, with Palla still wrapped around my cock, I'm not sure I can actually hold a conversation."
    mike.say "I, uh..."
    "She doesn't really wait for me to answer, and instead sits in Palla's seat."
    show audrey at zoomAt(1.5, (640, 1140)) with ease
    audrey.say "It's so funny to run into you here, [hero.name]! And here I was thinking I'd have to eat by myself tonight."
    mike.say "Yeah, uh, funny."
    "Palla, who'd managed to stay still up until this point, pulls my head deeper into her mouth, which makes me groan, just slightly."
    show audrey angry
    audrey.say "What's that about? Didn't you enjoy the present I gave you last time we ate together?"
    "So, I know Palla said it's okay that I date other people, but that doesn't mean she necessarily wants to hear about it. And this is her best friend. This is getting worse by the minute."
    mike.say "Oh, sorry no, I just...had some gas. It's not you."
    show audrey date normal
    audrey.say "Oh, that's okay then. Anyway, I was thinking this time instead of just giving you a handy I might use something else. I mean, you deserve the best, right? What do you think."
    "Palla's lips clamp down tight, and I can feel her teeth just barely dig into the very sensitive skin of my cock. Not enough to really hurt, but I definitely feel it."
    mike.say "I, uh. Maybe not right now?"
    "Audrey scoots toward me and puts her hand where she expects my dick to be."
    show audrey surprised at hshake
    pause 1
    show audrey angry
    if audrey.flags.mikeNickname:
        audrey.say "May I ask what is happening under the table [hero.name]?"
    else:
        audrey.say "What the fuck! What the fuck is going on here, [hero.name]!"
    show audrey frown
    "She looks under the table and sees the red hair that's in her hand. She scowls at me and pushes Palla down into my crotch, forcing her to take it all the way into her throat."
    "Palla makes a choking noise and tries to pull away, but Audrey doesn't release her head. With the table there, she doesn't have enough leverage to force herself away either."
    if audrey.flags.mikeNickname in nickname_master:
        audrey.say "Are you cheating with another slave Master?"
    else:
        audrey.say "Are you cheating on me, [hero.name]!"
    mike.say "Uh well it's not cheating exactly."
    show audrey angry
    audrey.say "And how is getting a blowjob under the table by my best friend not exactly cheating, huh?"
    "At this point other people in the restaurant are starting to look, and a murmur takes over the entire place. All of a sudden, Audrey and I are the center of everyone's attention."
    audrey.say "Well, what do you have to say for yourself?"
    show audrey frown
    mike.say "It's not like you're my girlfriend! We never said anything about being exclusive!"
    "My mind races, trying to think of a way to defuse this situation without getting my dick bitten off, and...not a single idea comes to me, good or bad."
    show audrey angry
    audrey.say "I'm not your girlfriend? Then what am I? Just some kind of side piece for you?"
    "She lets go of Palla's head, finally, who slips off my dick and gasps a couple of times."
    audrey.say "Besides, I wanted to be the one giving you head under the table."
    "Just then the maître d'hôtel appears."
    "Manager" "Excuse me, sir and madame, but is there a problem?"
    audrey.say "I'll say there's a problem!"
    show audrey frown
    "Manager" "Can you please keep it down? You're disturbing the other guests."
    show palla date zorder 1 at right
    show palla date angry at zoomAt(1.5, (1000, 2040))
    show palla at zoomAt(1.5, (1000, 1040)) with move
    "Palla chooses that moment to come up from under the table, taking one of the seats."
    "Manager" "Oh. Oh my. Sir, I think I'm going to have to ask you to leave now."
    show audrey angry
    audrey.say "What the hell? You're kicking us out?"
    show audrey frown
    "Manager" "I'm asking you to please be considerate of the other guests, who are having their meal spoiled by your shenanigans. Please leave. Now."
    "Audrey gets up and leaves, smacking the table loudly on the way out. Meanwhile, Palla gives me a death glare."
    scene bg street
    show audrey date frown at left5
    show palla date angry at right5
    with fade
    "As soon as we get outside, both girls start yelling at me at the same time. I can't make out any of the words, and they ignore my attempts to interrupt. So I'm forced to wait it out."
    "Finally, Audrey quiets down."
    palla.say "Well, [hero.name]? What the fuck is going on? What do you have to say for yourself."
    if audrey.flags.nickname == "toy":
        mike.say "Okay, first, little Toy, like I said, there were no promises. So yeah I guess that makes you just a side piece."
    else:
        mike.say "Okay, first, Audrey, like I said, there were no promises. So yeah I guess that makes you just a side piece."
    mike.say "But since you waste no opportunities to put your tits in my face in the office, that's clearly what you want."
    mike.say "And Palla, you said you {b}like{/b} it when I'm with other women!"
    palla.say "Yeah, [hero.name], but she's my best friend!"
    "Audrey's mask of anger cracks and she looks like she's about to laugh."
    palla.say "I told you that I was afraid of dating just one guy, that it was bad the last time I did it. And this is what you do?"
    mike.say "What the fuck, Palla? Do I need you to make a list of who's off-limits? Or is the only girl in the entire world who's off limits your best friend?"
    show audrey happy
    "Audrey starts laughing. It is completely incongruous with everything else that's gone on tonight."
    mike.say "Now what?"
    show audrey normal
    "Audrey stops laughing and tries to look angry again, but it's like she can't make her face do it."
    palla.say "The only one who is off-limits is my best friend. I thought that was obvious?"
    "I look between Audrey and Palla, and I start to wonder if this is all a setup."
    mike.say "No, Palla, it wasn't fucking obvious."
    audrey.say "Oh my God, Palla, do you see the look on his face right now? I mean, that deer-in-headlights thing is the best. Just the best."
    show palla normal
    palla.say "Really, Audrey?"
    audrey.say "So worth it. So very worth it."
    "I look between the two of them, Audrey laughing and Palla looking stern and bitchy."
    mike.say "This is a setup, isn't it?"
    audrey.say "No shit, Sherlock. Figure that out on your own, did you?"
    show palla happy
    palla.say "Oh, fine. It would've been nice if Audrey could keep character for more than 5 minutes!"
    audrey.say "Shut it, bitch."
    show palla normal
    palla.say "Don't be a cunt. And you didn't have to push my head down so hard! I almost threw up in his lap!"
    mike.say "Whoa. Whoa. What the hell?"
    "Palla and Audrey both shrug in unison. And then..."
    show audrey at zoomAt(1.65, (440, 1140))
    show palla at zoomAt(1.65, (840, 1140))
    with hpunch
    "Both women launch themselves at me simultaneously, and I wind up hugging them both, tightly."
    "Well that changed real fast. I can feel Palla's nipples hard against my chest. She is seriously turned on right now."
    audrey.say "You're not mad, are you [hero.name]?"
    mike.say "Not mad? Fuck yeah, I'm mad! You got us kicked out of the nicest restaurant in the city! I'll be embarrassed to ever even go back there!"
    palla.say "Oh don't be such a pussy, [hero.name]. You got a nice blowjob out of it."
    mike.say "You didn't even finish!"
    audrey.say "Well, that can be fixed."
    mike.say "After that? I'm humiliated!"
    audrey.say "You're right, we were bad girls. We deserve to be punished."
    "Palla whispers into my ear."
    palla.say "Yeah. You should punish us."
    "I have to admit, feeling four breasts smashed against my chest is going a long way toward easing my frustration over what just happened. Plus, okay, the idea of taking them both home and fucking the living crap out of them has some appeal."
    audrey.say "I promise I'll be a good girl."
    menu:
        "I'm out of here.":
            mike.say "Oh, no fucking way am I giving you what you want after what you pulled tonight. Fuck this shit, I'm going home."
            "As I walk away, both girls are only able to stare at me with open mouths. Audrey looks confused, Palla looks genuinely upset."
            "On the way, I think I hear Palla calling Audrey a fucking cunt."
            "She sure isn't wrong about that."
            $ game.room = "map"
            scene bg map
            $ palla.flags.nothreesome = True
            $ hero.replace_activity()
            if game.active_date:
                $ game.active_date.stay = False
            return
        "Yeah, these girls deserve a spanking.":
            "Her promises aren't worth crap, but I can have fun with this anyway..."
            $ game.active_date.score = 100
    call palla_and_audrey (None) from _call_palla_and_audrey
    return

label palla_and_audrey(appointment=None):
    "The three of us waste no time in getting to my room."
    call palla_audrey_date_threesome from _call_palla_audrey_date_threesome
    return

label palla_audrey_date_threesome:
    scene bg bedroom1
    show audrey date happy at left4
    show palla date happy at right4
    "We go back to my place, and both girls are, once again, all smiles. Palla might even be described as giddy. I rarely see her giddy."
    "Audrey steps behind Palla and reaches around her. In a few seconds, her elegant, probably expensive dress is on the floor."
    show palla normal underwear
    "While Palla stands still, Audrey's hands cup the redhead's breasts and display them to me. Her nipples harden visibly at the caress."
    show audrey normal
    audrey.say "You want some of this?"
    "Her hands go under Palla's bra, which is erotic but also hides my view of her nipples. But then one hand slips back out and down into Palla's crotch, while the other casually casts aside the bra."
    audrey.say "Or do you want some of this?"
    "Palla shivers exaggeratedly as two of Audrey's fingers disappear into her slit."
    show palla naked
    palla.say "Now now, Audrey. This isn't just about me."
    "Palla slips out of Audrey's embrace and turns around to face her."
    palla.say "And you, you deserve to be punished for that awful performance you put in."
    "While she speaks, Palla removes Audrey's dress."
    show audrey underwear topless
    palla.say "Not to mention, you were the one who couldn't keep it down. You weren't supposed to get us kicked out."
    "Audrey closes her eyes while Palla works; the model's hands caress Audrey's breasts, and her nipples are as hard as if we were inside a freezer."
    audrey.say "I know."
    palla.say "We were {b}supposed{/b} to give him a BJ together, but you couldn't control yourself."
    "Audrey shrieks as Palla tweaks the brunette's nipples."
    audrey.say "Ow! That fucking hurts!"
    palla.say "Good! It's supposed to!"
    "Palla does it again. Audrey's shriek is quieter this time, a little more guttural. And with almost a purr behind it. Audrey likes the pain."
    show audrey naked
    "Palla turns back toward me and presents Audrey, who stands there looking completely subservient."
    palla.say "So what do you want to do, [hero.name]?"
    call palla_audrey_date_loop from _call_palla_audrey_date_loop_2
    return

label palla_audrey_date_loop(palla_spanked=False, audrey_spanked=False):
    show audrey naked at left4
    show palla naked at right4
    menu:
        "Spank Audrey" if not audrey_spanked:
            mike.say "Audrey, bend over."
            "Audrey's eyes get wide. She's been wanting this, but now that she's presented with it, I think she's just a little bit afraid. But she does what she's told."
            show spank audrey bedroom naked up normal
            pause 0.3
            show spank audrey spank bedroom naked surprised
            play sound spank
            with hpunch
            "I raise my hand and bring it down on her cheeks. It makes a satisfying SLAP noise, and her ass jiggles a little when I make contact."
            show spank audrey bedroom naked up normal
            pause 0.3
            show spank audrey spank bedroom naked surprised
            play sound spank
            with hpunch
            "I do it again and this time she makes a soft \"Unf\" noise. Her eyes close."
            show spank audrey bedroom naked up normal
            pause 0.3
            show spank audrey spank bedroom naked marks surprised
            play sound spank
            with hpunch
            "I keep going, counting my way up to twenty smacks. None of them are very hard, but they do add up. By the time I'm done, her ass is as red as a cherry, and a single tear is coming from one eye."
            show spank audrey spank bedroom naked marks pleasure
            palla.say "Yeah, cunt. That's what you deserve!"
            "Audrey moans, a mix of pain and pleasure filling her throat."
            palla.say "Slap that bitch again."
            show spank audrey bedroom naked up pleasure
            pause 0.3
            show spank audrey spank bedroom naked surprised
            play sound spank
            with hpunch
            "SLAP!"
            show spank audrey bedroom naked marks pleasure
            audrey.say "MORE!"
            show spank audrey bedroom naked up
            pause 0.3
            show spank audrey spank bedroom naked surprised
            play sound spank
            with hpunch
            "SLAP!"
            show spank audrey bedroom naked up pleasure
            pause 0.3
            show spank audrey spank bedroom naked surprised
            play sound spank
            with hpunch
            "Another SLAP!"
            show spank audrey bedroom naked up pleasure
            pause 0.3
            show spank audrey spank bedroom naked marks surprised
            play sound spank
            with hpunch
            "One more SLAP!"
            show spank audrey spank bedroom naked marks pleasure
            audrey.say "Oh God!"
            mike.say "Okay, I think that's enough."
            "And if I might be worried about how much pain I'm inflicting, her pussy is completely wet and I think she'd orgasm now if I just touched it. But she has to wait for that. This {b}is{/b} punishment after all."
            $ audrey.sub += 10
            scene bg bedroom1
            call palla_audrey_date_loop (palla_spanked=palla_spanked, audrey_spanked=True) from _call_palla_audrey_date_loop
            return
        "Spank Palla" if not palla_spanked:
            if audrey_spanked:
                mike.say "Your turn, Palla!"
                palla.say "Oh, no, I think Audrey getting it is enough!"
            else:
                mike.say "You first, Palla!"
                palla.say "What?! Wait no, Audrey is the one who wants the spanking!"
            palla.say "I had...something else in mind."
            mike.say "Oh no, you set that up with her. I know she's the one who fucked it up, but now it's your turn. Bend over."
            if palla.sub == 100:
                "Palla walks up to me and comes close to whisper into my ear, presumably so Audrey doesn't hear."
                palla.say "Yes, Master, as you wish."
            else:
                "Palla looks at me with her big, blue eyes."
                palla.say "I...please, don't."
                mike.say "Get over here and give me your ass."
                if audrey_spanked:
                    mike.say "I promise I won't spank you as hard as Audrey got."
            "She looks at me, then at Audrey, who is just watching this whole exchange with a smile. Then she bends over, as instructed."
            show palla at middle
            show palla spank
            "Before I start, I caress her ass. I have to say, one advantage to her being a model is that she keeps her ass in perfect shape. It's fit and trim, not too big, not too small. I kind of want to fuck it rather than spank it."
            show palla spank hit impact surprised
            play sound spank
            with hpunch
            "SLAP!"
            show palla spank -impact
            "Palla shouts in pain."
            palla.say "Not so rough!"
            mike.say "I thought you liked it rough?"
            palla.say "Not like that!"
            show palla spank middle
            "Palla closes her eyes as I raise my hand."
            show palla spank hit impact
            play sound spank
            with hpunch
            "SLAP! Not so hard this time, though."
            show palla spank -impact
            audrey.say "Oh fuck."
            "I was so absorbed in what I was doing with Palla that I didn't notice Audrey. She's standing there with her hand between her legs, pleasuring herself."
            show palla spank middle
            audrey.say "Hit her again!"
            show palla spank speed
            palla.say "No!"
            show palla spank hit impact marks
            play sound spank
            with hpunch
            "SLAP!"
            show palla spank -impact
            "Palla shouts again. Audrey straight up has an orgasm, she's so turned on by this."
            palla.say "Please, Master, stop! I'll do anything!"
            mike.say "Anything?"
            show palla spank pleasure
            palla.say "Anything you want, Master. I'm yours. Fuck me. Fuck my ass, fuck my mouth."
            mike.say "Lick my cum out of your best friend's pussy? Let her fuck your cunt with a strapon while I fuck your ass?"
            $ palla.sub += 10
            palla.say "Yes, please! All of those things! Just...stop this!"
            mike.say "Okay, but you need to be a good girl or we'll finish this later."
            "She looks up at me, a tear running down one cheek."
            palla.say "Yes, Master! Thank you, Master!"
            scene bg bedroom1
            call palla_audrey_date_loop (audrey_spanked=audrey_spanked, palla_spanked=True) from _call_palla_audrey_date_loop_1
            return
        "Fuck them both":
            pass

    if palla_spanked and audrey_spanked:
        "I look at both girls with their red asses and admire my handiwork."
    "They're both ready, looking at me with smiles on their faces. Both of them have swollen cunt lips, ready for my cock. The question is, who should I satisfy first?"
    "And then I remember that Sasha has a huge box of toys in her room, and one of those would come in handy. I'm going to hope she's not home."
    mike.say "Wait here, you two. I'll be right back."
    scene bg secondfloor
    "I sneak up the stairs and peek into her door. She is home, but she's asleep. I just have to be quiet."
    scene bg bedroom3
    "Luckily, Sasha is a sound sleeper, and I'm able to sneak away with one of the half-dozen strap on dildos that Sasha keeps in her toybox. I hope she doesn't notice it missing!"
    scene bg bedroom1
    show audrey naked happy at left4
    show palla naked blush at right4, hshake
    "When I return I present the strapon to the two ladies. Palla looks honestly surprised, but Audrey looks absolutely delighted."
    audrey.say "Oh, you have the best ideas, [hero.name]!"
    "I pass the strapon to Audrey."
    mike.say "Put it on."
    show audrey strapon normal
    palla.say "Whoa, are you...is she going to use that on me?"
    mike.say "Well she's certainly not going to use it on {b}me{/b}."
    palla.say "Oh. Oh fuck me."
    mike.say "Yes, that's the idea. Audrey, you lay down on the bed. Palla, I want you to climb aboard."
    "Audrey obeys immediately. Palla is a little slower to move, but she does so."
    show bitchy threesome pallafuck strapon pallaclosed
    if renpy.has_label("bitchy_harem_achievement_2") and not game.flags.cheat:
        call bitchy_harem_achievement_2 from _call_bitchy_harem_achievement_2
    "Palla moans as she surrounds the dildo with her cunt, dropping her weight onto it and taking it all in one go. Any hesitation she had about this evaporated as soon as the toy entered her. Yeah, she is ready."
    show bitchy threesome pallafuck mike out
    "I climb up behind her and push her down so that her face is in Audrey's."
    show bitchy threesome pallafuck anal pallaopen
    "The two of them kiss while I enter Palla's anus from behind."
    "Palla's voice is muffled by Audrey, but despite her mouth being busy, her moans are loud and sensuous. Together, Audrey and I work Palla pretty hard."
    show bitchy threesome pallafuck pussyjuice
    "Audrey thrusts up while I thrust down, filling Palla up completely. Audrey holds onto Palla's head, not letting her pull away; all in all, Palla is completely trapped and doesn't have much choice about what happens to her."
    show bitchy threesome pallafuck cum
    "It doesn't take long before I spill my load into her ass."
    palla.say "Oh fuck, oh fuck, [hero.name] that was...that was amazing."
    audrey.say "My turn!"
    mike.say "I just unloaded, I don't think I can for a few minutes."
    mike.say "Nope, Audrey, that's your punishment. You want to finish, you gotta finish yourself."
    "Audrey scowls at me, but she can't hold it and cracks into a smile."
    audrey.say "It's okay, I came twice already anyway."
    hide bitchy threesome pallafuck
    show palla naked normal
    show audrey -strapon normal
    "Palla slides up and over, laying on my bed next to Audrey. She pats the bed between them."
    palla.say "Come here, my love."
    "I really should be taking charge, but...I'm spent, and it looks comfortable."
    "So I crawl up between them, and the two beautiful women snuggle up to me. Huddled in their warmth, I drift right to sleep."
    $ palla.flags.anal += 1
    $ palla.sexperience += 1
    $ audrey.sexperience += 1
    $ hero.replace_activity()
    if game.active_date:
        $ game.active_date.stay = False
    $ game.room = "bedroom1"
    call sleep from _palla_audrey_date
    return

label palla_audrey_date_areyoumad:
    show palla
    palla.say "Hey, [hero.name], are you mad?"
    mike.say "Mad about what?"
    "Don't get me wrong, I know perfectly well what she's asking about -- am I mad about that blown up date with Audrey -- but I'm still upset enough to not play nice with her."
    palla.say "About our date, and Audrey."
    mike.say "Oh, you mean that part where you set me up and got us kicked out of the nicest restaurant in the city? Gosh, why would I be mad about that?"
    "This is the part where I'd expect Palla to, normally, fly into a rage."
    "But she doesn't."
    show palla sad
    "Instead, she looks down at my feet."
    palla.say "[hero.name]...I don't know what to say. It wasn't supposed to go like that."
    mike.say "Oh, did I not get humiliated enough?"
    palla.say "You weren't supposed to get humiliated at all! It was supposed to be a fun show for you. Two hot girls, fighting over you, and eventually decided they didn't have to fight anymore, and could share."
    palla.say "Seriously, I thought that was every guy's dream. Isn't that like half the porn videos we watch at your place?"
    "I frown."
    mike.say "I want to believe you, Palla, I just don't see how it went from what you describe to what actually happened."
    "Palla sighs."
    show palla normal
    palla.say "The short answer is that Audrey's a stupid cunt."
    palla.say "The long answer is that...I set every bit of that up. I told her exactly what to do and how to do it. And she ignored me. She wasn't supposed to be so bitchy. Or loud. I trusted her, and I fucked up. Okay? That's on me."
    show palla annoyed
    palla.say "If she had done it right, we both would've been under the table."
    mike.say "Why should I believe you?"
    show palla angry
    palla.say "Fuck you, [hero.name]. When was the last time I apologized to you for anything?"
    if "palla_event_12" in DONE:
        mike.say "Well, you did apologize for lying to me about your career."
        show palla normal
        palla.say "Did you believe me then?"
        mike.say "Yes."
        palla.say "So how's this different?"
        mike.say "You're not crying your eyes out."
        palla.say "Would you like me to open up the water works? I can, if you want."
        mike.say "I'm not sure that would make me feel better."
    else:
        mike.say "Nothing comes to mind."
        show palla normal
        palla.say "I don't say I'm sorry lightly, at least not like this. I'm serious. I mean it."
    palla.say "Look. I'm sorry. I fucked this up, and I want to fix this."
    mike.say "How?"
    show palla at zoomAt(1.5, (640, 1040))
    "Palla steps up to me."
    palla.say "I can be...very accommodating."
    mike.say "Hey now, I'm still mad."
    palla.say "Do you want to go home and have angry sex?"
    mike.say "Right now?"
    palla.say "I'm not busy. Are you?"
    mike.say "I don't know..."
    palla.say "Wait, [hero.name], are you actually...turning down sex?"
    mike.say "I'm thinking about it."
    palla.say "What else can I do to make it up to you then?"
    mike.say "I'm not sure."
    palla.say "I still want that threesome with you and Audrey."
    mike.say "Why?"
    palla.say "Because the idea of you pounding her ass, I don't know. It turns me on so much. Is there something wrong with me? I know women are supposed to be jealous bitches, but I'm just not. At least the jealous part."
    mike.say "Well, it has its merits, for sure."
    palla.say "I want to watch while you punish her. I want to see you stick your cock all the way down her throat, and fill her up with your cum. And then me too."
    mike.say "So you really, for serious, were trying to set that up?"
    palla.say "Oh, fuck yes."
    mike.say "Wow."
    palla.say "I want to lick your cum out of her pussy."
    mike.say "Okay, okay, maybe I'm convinced."
    "In truth, there's no maybe about it. Just listening to her talk, and seeing the expression on her face is starting to turn me on."
    palla.say "So. Forgiven?"
    show palla at zoomAt(1.65, (640, 1140))
    "For emphasis, she presses her chest up against mine and wraps her arms around my waist."
    mike.say "No. But..."
    palla.say "But, what?"
    mike.say "But...maybe I'll let you earn it."
    palla.say "Okay. I deserve it. I will earn your forgiveness. And..."
    palla.say "Can we still have that threesome?"
    menu:
        "Sure, someday":
            mike.say "Sure, Palla. We can, someday."
            show palla happy
            $ Harem.join_by_name("bitchy", "audrey", "palla")
            "Palla gives me a big smile."
            palla.say "We'll set it up sometime, like a date."
            hide palla
            show palla kiss
            $ palla.flags.kiss += 1
            "And then she kisses me. I can't keep my anger in, not when I can smell her so close, taste her lips, her tongue."
            "By the time we're done kissing, I almost can't remember what I was angry about."
        "Not interested":
            mike.say "I know it sounds weird, because it's every guy's fantasy, but it's not mine. Sorry."
            show palla sad
            "Palla looks disappointed, but not upset."
            palla.say "Okay. But you still like me, right?"
            mike.say "Yes, Palla. I still like you."
            show palla happy
            "She smiles."
            palla.say "That's all that matters, then."
    $ palla.love += 5
    hide palla
    return

label palla_audrey_date_apology:
    show palla
    palla.say "Hey, [hero.name]. I just wanted to say...I'm really sorry about Audrey's behavior the other night. You know, when you punished us."
    mike.say "You two really deserved that!"
    palla.say "I know! It wasn't supposed to go like that. I mean, it ended up in a good place, but we weren't supposed to get kicked out."
    mike.say "I was humiliated!"
    show palla annoyed
    palla.say "I am so, so sorry about that. It wasn't supposed to go down like that. If Audrey wasn't such a stupid fucking cunt, it wouldn't have turned into such a clusterfuck."
    show palla normal
    palla.say "But that's my fault. I trusted her and I knew better. That's on me."
    "She flutters her eyelashes at me."
    palla.say "...and you can punish me again, if you want."
    mike.say "Well, it was a lot of fun punishing you last time."
    palla.say "God, I loved being between you two. It's like heaven."
    show palla at zoomAt(1.65, (640, 1140))
    "She walks up close and puts her arms around me, and whispers."
    palla.say "Thank you so much for being a good sport about it."
    mike.say "It was kind of fun!"
    palla.say "Want to do it again? I mean, not right this second, obviously, she's not here. But later?"
    menu:
        "Sure":
            mike.say "Sure, Palla. We can, someday."
            show palla happy
            $ Harem.join_by_name("bitchy", "audrey", "palla")
            "Palla gives me a big smile."
            palla.say "We'll set it up sometime, like a date."
            hide palla
            show palla kiss
            $ palla.flags.kiss += 1
            "And then she kisses me. I can't keep my anger in, not when I can smell her so close, taste her lips, her tongue."
            "By the time we're done kissing, I almost can't remember what I was angry about."
        "Not interested":
            mike.say "I know it sounds weird, because it's every guy's fantasy, but it's not mine. Sorry."
            show palla sad
            "Palla looks disappointed, but not upset."
            palla.say "Okay. But you still like me, right?"
            mike.say "Yes, Palla. I still like you."
            show palla happy
            "She smiles."
            palla.say "That's all that matters, then."
    $ palla.love += 5
    hide palla
    return

label cassidy_audrey_showdown:
    scene expression f"bg {game.room}"
    "I'm just sitting at my desk, trying to get some work done."
    "Pretty much like any random moment you might find me in the office."
    "But the sound of the door opening is enough to make me stop and look up."
    "I'm expecting to see Aletta, who's in the habit of just barging in."
    "Or else Shiori, looking embarrassed and apologetic after forgetting to knock."
    show cassidy b at top_mostleft with moveinleft
    "But one person I certainly wasn't expecting to see is Cassidy!"
    "She looks seriously hot and has a mischievous expression on her face."
    "I can't keep mine from lighting up at the mere sight of her."
    "Cassidy sees this instantly, and giggles."
    show cassidy b at left with move
    "Then she slips inside my office and closes the door behind her."
    show cassidy b at center with move
    cassidy.say "Hi, [hero.name]..."
    cassidy.say "You look pleased to see me!"
    "I nod eagerly, not trying to deny it."
    mike.say "Of course I am, Cassidy."
    if cassidy.flags.schedule == "default":
        mike.say "I'm surprised too."
        mike.say "What are you doing here?"
        hide cassidy
        show cassidy b at center, zoomAt(1.5, (640, 1040))
        "Cassidy shrugs and shakes her head as she walks over to my desk."
        cassidy.say "Oh..."
        cassidy.say "Let's say I wanted to see where you work."
        cassidy.say "How about that?"
        mike.say "Well, here I am, Cassidy."
        mike.say "And here's my office."
    else:
        mike.say "Come in."
    "Cassidy nods as she reaches my desk and walks around the side of it."
    "She's holding my eye the entire time, keeping me staring back at her."
    show fx question
    cassidy.say "And I bet you work hard too, yes?"
    cassidy.say "So hard that you're almost burned out?"
    mike.say "I..."
    mike.say "I don't know about that, Cassidy!"
    mike.say "But it can be tough going sometimes, for sure."
    "Cassidy's still nodding as she walks behind my desk."
    hide cassidy
    show cassidy b at center, zoomAt(2.0, (640, 1340))
    "She comes to a stop by my chair."
    "And I turn to face her, still looking up at her."
    cassidy.say "You shouldn't have to be worked so hard, [hero.name]."
    show cassidy happy
    cassidy.say "What you need is someone to relieve your stress..."
    "I'm still nodding silently as Cassidy sinks down to her knees."
    "And, of course, I don't try to stop her as she reaches out for my flies."
    scene bitchy blowjob
    show bitchy blowjob cassidyblow
    with fade
    "I just watch as she pulls my cock out of my pants."
    "Just the sight of her was already starting to make me get hard."
    "But she handles it expertly, making me stand to attention in no time at all."
    "Cassidy doesn't say another word, but that doesn't mean she's silent."
    "Instead she makes little sounds of delight and arousal."
    "Giggles and gasps as my cock comes to life in her hands."
    "She only stops when she finally leans in and begins to give me head."
    show bitchy blowjob blow
    "The sight of Cassidy and the sounds she was making are nothing compared to this."
    "She starts off slow, taking a little more at a time into her mouth."
    show bitchy blowjob tip
    "Cassidy's careful and attentive, eager to do her very best."
    "And soon enough I find myself leaning back in my chair."
    "It's all I can do as the sensations of what she's doing to me take over."
    show bitchy blowjob deep
    "I can't recall what I was doing the moment before Cassidy walked into my office."
    "In fact it's hard enough to remember that I'm in the office at all."
    "The only thing that seems real is the feeling of Cassidy's lips and tongue."
    show bitchy blowjob tip
    "I feel like Cassidy could make me cum at any moment."
    "But she's dragging it out for the sake of my enjoyment."
    show bitchy blowjob deep
    "Her head bobs up and down between my thighs."
    "And she presses on without any sign of tiring."
    scene expression f"bg {game.room}"
    audrey.say "Oh, [hero.name]!"
    audrey.say "I know you're in here..."
    audrey.say "You'd better be ready - because I want it!"
    show audrey happy zorder 1 at left with moveinleft
    audrey.say "I want you to give me a good, hard fucking!"
    "My eyes snap open and my head spins in the direction of the door."
    show cassidy annoyed zorder 2 at center
    show cassidy at zoomAt(1.5, (740, 2040))
    show cassidy at zoomAt(1.5, (740, 1340)) with move
    "At the same moment, Cassidy's own head pops up from between my thighs."
    "Both of us are looking straight at Audrey on the other side of the room."
    show audrey topless surprised a
    "She's halfway through stripping off her clothes."
    "And she has the same look of surprise on her face as Cassidy and I do."
    audrey.say "Whoa..."
    show audrey surprised
    audrey.say "What did I just walk in on?!?"
    cassidy.say "I...I..."
    show cassidy annoyed
    cassidy.say "I wasn't..."
    scene bitchy blowjob
    show bitchy blowjob cassidyblow blow
    "It's at that exact moment Cassidy chooses to look down at my cock."
    show bitchy blowjob cumshot with vpunch
    "And as fate would have it, the same moment I manage to shoot my load."
    "I don't know how it happens, but somehow it does."
    "Maybe it was just the timing, or maybe the surprise set me off."
    show bitchy blowjob -cumshot cum onface -blow swallow
    "Whatever the reason, Cassidy take it square in the face!"
    "She squeals and shakes her head as the cum spatters her."
    "But all that does is make sure more of her face is covered."
    "Forehead, nose, cheeks and mouth, all get a liberal striping."
    "A little even lands in her open mouth as she wails in alarm."
    audrey.say "Nice shooting, [hero.name]!"
    scene expression f"bg {game.room}"
    show audrey annoyed topless a at left
    show cassidy angry facecum a at center, zoomAt(1.5, (740, 1340))
    audrey.say "Right between the eyes!"
    "Before I can get it together to say a single word, Cassidy's on her feet."

    hide cassidy
    show cassidy angry facecum a at right
    if cassidy.flags.schedule == "default":
        cassidy.say "Who in the hell are you?!?"
        cassidy.say "What are doing walking straight in here?!?"
        cassidy.say "Have you never heard of knocking?!?"
        mike.say "Ah..."
        mike.say "Cassidy, this is Audrey."
        mike.say "She works here under me."
    else:
        cassidy.say "Audrey!!!"
        cassidy.say "What are doing walking straight in here?!?"
        cassidy.say "Have you never heard of knocking?!?"
        mike.say "Calm down Cassidy, Audrey works under me."
        mike.say "You know that."
    show cassidy normal
    "Cassidy seems to miss the unintentional yet obvious pun."
    show audrey normal
    "But Audrey can't help curling her lips into a cynical smile."
    if cassidy.flags.schedule == "default":
        mike.say "Audrey, this is Cassidy."
        mike.say "She's Dwayne's daughter."
    if all([person.love >= 160 and person.lesbian >= 9 for person in [audrey, cassidy]]):
        if cassidy.flags.schedule == "default":
            audrey.say "Is she now?"
            show audrey annoyed
            audrey.say "Is she really?"
        "There's a tense moment as Audrey walks across the room."
        show audrey at center with move
        "She closes the distance between Cassidy and herself."
        hide audrey
        hide cassidy
        show cassidy close a normal facecum at top_to_bottom
        "And then she makes a point of looking the other girl up and down."
        hide cassidy close
        show audrey annoyed topless a
        show cassidy a normal facecum at right
        "I hold my breath, waiting for Audrey to so something."
        "At the very least I think she's going to slap Cassidy in the face."
        "But then she reaches out and grabs her head with both hands."
        show audrey normal
        "As Cassidy's eyes go wide, Audrey kisses her full on the lips."
        "The kiss doesn't last long, but Audrey seems to savour it."
        "She breaks off, licking her lips with satisfaction."
        audrey.say "Mmm..."
        show audrey flirt
        audrey.say "You still taste good, [hero.name]!"
        audrey.say "Even when I'm licking you off of her lips!"
        "She then proceeds to lick every last drop of cum from Cassidy's face."
        "All I can do is watch in amazed silence as she does this."
        show cassidy -facecum
        "And Cassidy remains as still as a statue the whole time too."
        "As soon as she's done, Audrey strides over to my desk."
        "She shoves my paperwork aside and strips off the last of her clothes."
        show audrey naked a
        "And then she leans over the desk, looking back over her shoulder at me."
        show audrey frown
        audrey.say "Now it's my turn!"
        audrey.say "Well, what are you waiting for?"
        show audrey happy b
        audrey.say "Fuck me already!"
        mike.say "S...sure thing, Audrey!"
        mike.say "Whatever you say!"
        "Cassidy looks on in amazement as I obey Audrey's command."
        "Sure, I might have just shot my load over her a couple of minutes ago."
        "But the sight of Audrey stripping off and the way she's offering herself up..."
        "Well, let's just say that it's more than enough to give me a second wind!"
        scene audrey doggy with fade
        if game.room == 'ceo':
            show audrey doggy ceo -sexywork
        else:
            show audrey doggy -sexywork
        "My cock is just as hard as it was when Cassidy gave me head."
        "And I can already see that Audrey's nice and slick down there too!"
        "I grab hold of Audrey's haunches, not bothering to be gentle about it."
        "I know her well enough to be sure she'll want it hard and rough."
        "And as soon as I do, she confirms my suspicions."
        audrey.say "Oh yeah, that's it!"
        audrey.say "Grab me and don't let go!"
        audrey.say "I want it good and hard!"
        "I don't waste another second."
        "Instead I thrust myself forwards."
        "The head of my cock presses against Audrey's pussy for a moment."
        show audrey doggy inside
        "And then it surrenders to me, letting me push in all the way."
        "The sensation is incredible, making me gasp out loud."
        show audrey doggy pleasure inside
        audrey.say "Oh..."
        audrey.say "Oh fuck..."
        audrey.say "Mmm...fuck yeah!"
        "I don't go slowly or wait to build up momentum."
        "I just begin pounding Audrey with all my might."
        "I know it's what she wants, and I feel her body tell me I'm right."
        "Audrey groans and pants as I pound her as hard as I possibly can."
        "But I see that she's staring straight at Cassidy as she takes it."
        "I feel my eyes being drawn in the same direction too."
        "And it's not long before I'm staring at the other girl too."
        "Cassidy's eyes are as large as saucers."
        "It's obvious that she can't tear her gaze away from us."
        "Maybe the normal thing to feel right now would be shame or discomfort."
        "But I'm actually getting a thrill from having her watch us do it!"
        "A thrill that only becomes more intense when I see what Cassidy's doing with her hand."
        "I watch as it creeps between her thighs and she begins to stroke herself."
        "Pretty soon she's moaning too as she plays with her pussy."
        "Cassidy lets out little gasps of pleasure as she does so."
        "And it's soon more than I can take!"
        show audrey ahegao inside with hpunch
        "I hammer into Audrey's buttocks as I shoot my load into her."
        "She gasps, beginning to cum herself a moment later."
        "And the whole time, Cassidy holds her free hand over her mouth."
        "Trying to stifle her own gasps as she cums too."
        "Afterwards, a weird silence falls over all of us."
        scene expression f"bg {game.room}"
        show audrey work at left5
        show cassidy blush at right5
        with fade
        "We get dressed quickly and without comment."
        show audrey flirt
        "Audrey fixes Cassidy and me with a knowing stare."
        "Then she winks and slips out of my office."
        hide audrey with moveoutleft
        "I keep expecting Cassidy to say something to break the silence."
        "But instead she looks thoughtful and keeps her mouth shut."
        "All she does after that is place a kiss on my cheek."
        hide cassidy with moveoutleft
        "And then she's gone too, leaving me alone in my office."
        "I do the best I can to get my desk in order and get back to work."
        "But my mind keeps on going back to what just happened."
        "And I can't help wondering what it means."
        "That and where we go from here."
        $ audrey.sexperience += 1
        $ cassidy.sexperience += 1
        $ audrey.love += 2
        $ cassidy.love += 2
        $ cassidy.flags.audreyshowdown = True
    else:
        if cassidy.flags.schedule == "default":
            audrey.say "I don't care who's daughter she is."
            show audrey angry
            audrey.say "I'm the queen bitch in this office."
            audrey.say "And I don't like her muscling in on my turf!"
        show audrey frown
        "I don't think I've ever seen Audrey move so fast."
        "She's across the office in the blink of an eye."
        show cassidy angry a
        show audrey angry a at center with move
        "And she's on Cassidy before the other girl knows what's happening."
        "The fight that follows is a confused tangle of slapping and scratching."
        show cassidy at hshake
        with vpunch
        "Hair is pulled and screams fill the air as they brawl."
        show audrey at hshake
        "Audrey gets the upper hand to begin with."
        "But I soon see that was thanks to the element of surprise."
        show cassidy at hshake
        "Because Cassidy begins to give as good as she gets."
        with hpunch
        "In fact, it looks like they're pretty evenly matched."
        show cassidy at hshake
        show audrey at hshake
        "All I can do is stand back and watch as the girls fight."
        "Sure, I could step in and try to break it up."
        "But I feel like they need to settle this for themselves."
        "So I force myself to simply watch as they go at it."
        with vpunch
        "And it's torture, seeing two semi-naked women brawl."
        "Trust me, I'm not enjoying this at all..."
        if audrey.love > cassidy.love or (audrey.love == cassidy.love and randint(0, 1) == 0):
            "I honestly don't know which one of them is going to come out on top."
            "But that changes when I see Audrey grab hold of Cassidy with both hands."
            with hpunch
            "She lets out an almost feral roar, tossing the other girl across the room."
            show cassidy annoyed at zoomAt(1, (340, 940)) with move
            with vpunch
            "Cassidy flies through the air and lands heavily on her ass."
            "The sight and sound of it make me wince."
            "And it seems to knock the fight out of Cassidy too."
            show cassidy sad at left
            "She hurriedly gathers up her clothes and darts through the door."
            hide cassidy with moveoutleft
            "Cassidy doesn't even stop to check the coast is clear either!"
            "Audrey snorts in triumph and turns to face me."
            show audrey joke
            audrey.say "That told her!"
            "I nod eagerly, trying to hide my cock from sight."
            "Seeing Audrey fight like that really turned me on!"
            $ audrey.love += 3
            $ cassidy.set_gone_forever()
        else:
            "I honestly don't know which one of them is going to come out on top."
            "But that changes when I see Cassidy grab hold of Audrey with both hands."
            with hpunch
            "She lets out an almost feral roar, tossing the other girl across the room."
            show audrey surprised at zoomAt(1, (340, 940)) with move
            with vpunch
            "Audrey flies through the air and lands heavily on her ass."
            "The sight and sound of it make me wince."
            "And it seems to knock the fight out of Audrey too."
            show audrey sad at left
            "She hurriedly gathers up her clothes and darts through the door."
            hide audrey with moveoutleft
            "Audrey doesn't even stop to check the coast is clear either!"
            "Cassidy snorts in triumph and turns to face me."
            show cassidy normal
            cassidy.say "That told her!"
            "I nod eagerly, trying to hide my cock from sight."
            "Seeing Cassidy fight like that really turned me on!"
            $ cassidy.love += 3
            $ audrey.set_gone_forever()
    return


label cassidy_palla_showdown:
    scene expression f"bg {game.room}"
    show dance cassidy date
    "I've heard all the lines about how it's a scummy thing to cheat on a girl, every last one of them."
    "But you know what - I seem to be pulling it off pretty well right now!"
    "I mean, here I am, dancing away with Cassidy, not a care in the world."
    "And I know that I also have Palla in the palm of my hand too, ready and waiting for me!"
    "Neither of them knows that I'm seeing the other behind their back, so they're both happy."
    "Which means that I'm happy too - so where's the problem?"
    "And it's just as I'm getting through congratulating myself that I see her."
    "It's Palla, scanning the dance-floor with a look of pure rage on her face!"
    "I try to duck down and keep from being seen, but it's too late."
    "Palla's gaze locks onto me a second later."
    "I swear it feels like she's already grabbed hold of me!"
    hide dance
    show cassidy date at center, zoomAt (1.5, (640, 1040))
    with hpunch
    cassidy.say "Wha..."
    show fx exclamation
    cassidy.say "What's the matter, [hero.name]?!?"
    mike.say "No time to explain, Cassidy."
    mike.say "We have to get out of here!"
    mike.say "Is there a way out around the back?"
    show fx question
    cassidy.say "Huh?!?"
    cassidy.say "How would I know?"
    show palla date angry at left
    show cassidy at center, zoomAt (1.5, (940, 1040))
    with moveinleft
    palla.say "AHA!"
    palla.say "I thought so!"
    "Cassidy and I turn around to see Palla elbowing her way towards us."
    "If she looked scary across the dance-floor, then she looks terrifying up close!"
    cassidy.say "[hero.name]..."
    show cassidy angry
    cassidy.say "Who is that girl?"
    cassidy.say "And what does she want?"
    show palla at center, zoomAt (1.5, (340, 1040))
    show cassidy at center, zoomAt (1.5, (740, 1040)) with ease
    "Palla strides over to us while Cassidy clings to me."
    "I don't feel like I need Cassidy to protect me from Palla."
    "But she puts herself between us all the same."
    palla.say "What do I want?"
    show palla annoyed
    palla.say "Maybe we can start with who the hell are you?"
    palla.say "What are you doing with my boyfriend, you little slut?!?"
    "Cassidy bristles at the insult."
    "She's not used to being talked to like that."
    "And she's not the kind of girl to back down either."
    mike.say "Cassidy...Palla..."
    mike.say "There's no need for this!"
    hide cassidy
    show cassidy date angry at center, zoomAt (1.5, (740, 1040)), vshake
    cassidy.say "What did you call me?"
    cassidy.say "I should scratch your eyes out!"
    cassidy.say "You lying bitch!"
    cassidy.say "Tell her, [hero.name]!"
    show cassidy annoyed
    cassidy.say "Tell her you're my boyfriend, not hers!"
    show palla angry
    "Palla turns her gaze on me again."
    "And I feel like I'm shrivelling up under as she stares at me."
    palla.say "Yeah, [hero.name]."
    show palla annoyed
    palla.say "You tell her the truth - and me while you're at it!"
    mike.say "Well..."
    mike.say "You see..."
    mike.say "You're both kind of right!"
    show palla angry
    "Now I have both Cassidy and Palla staring at me."
    "And all I can do is shrug helplessly."
    "Then hold my breath and wait to see what happens next..."
    if all([person.love >= 160 and person.lesbian >= 9 for person in [cassidy, palla]]):
        palla.say "Well, I don't so much care that he's been cheating on me."
        show palla angry
        palla.say "Not as much as I hate that he chose to do it with the likes of you!"
        cassidy.say "Hah!"
        show cassidy angry
        cassidy.say "Take one look at me and then in the mirror!"
        cassidy.say "You know that he was slumming it with you!"
        "I look from Cassidy to Palla and back again."
        "And I can feel a glimmer of hope beginning to rise up inside of me."
        "If I can make this about them rather than me, maybe I can turn it around!"
        mike.say "Girls, girls..."
        mike.say "Don't say things like that about each other!"
        mike.say "You're both so amazing - I could never choose between you!"
        palla.say "Oh really?"
        show palla annoyed
        palla.say "Well, I'll show you why you should choose me over her!"
        with hpunch
        "Palla grabs me by the wrist and proceeds to haul into the middle of the dance-floor."
        "I don't even have time to resist, and so I'm dragged along in her wake."
        "But Cassidy is right on our heels."
        cassidy.say "Where do you think you're taking him?!?"
        show cassidy annoyed
        cassidy.say "And what are you going to do anyway?"
        cassidy.say "Whatever it is, I'll do a hundred time better!"
        hide cassidy
        hide palla
        show dance palla date
        "Before I know it, Palla's dancing with me like her life depends on it."
        "Well, I say she's dancing with me..."
        "It kind of feels more like she's using me as a pole to dance around!"
        "Cassidy crashes the party a moment later."
        hide dance palla
        show dance cassidy date with vpunch
        "She's pressing herself against me too, trying to shove Palla out of the way."
        "Normally this would be a dream come true for me."
        "But right now I feel like I'm a piece of meat being fought over!"
        hide dance cassidy
        show palla date at center, zoomAt (1.5, (440, 1040))
        show cassidy date at center, zoomAt (1.5, (840, 1040))
        with hpunch
        "I have Cassidy grinding against me on one side and Palla doing the same on the other."
        "And it doesn't take long for them to realise this isn't going to solve anything."
        "Palla suddenly takes hold of my hand again."
        with hpunch
        "This time she pulls me off the dance-floor."
        scene bg restroom
        show palla date at center, zoomAt (1.5, (440, 1040))
        with fade
        "Palla doesn't stop until she leads me into the bathroom."
        "And then she hustles me into one of the stalls."
        show cassidy date at center, zoomAt (1.5, (840, 1040)) with moveinright
        play sound door_slam
        "Cassidy follows, slamming the door behind us."
        mike.say "What's going on here?"
        palla.say "You just shut your mouth."
        show palla annoyed
        palla.say "And take what's coming, okay?"
        "With that, Palla unzips my pants and pulls them down."
        hide palla with moveoutbottom
        "She's on her knees before I even know what's happening to me."
        hide cassidy with moveoutbottom
        "And a moment later, Cassidy is right there beside her too!"
        cassidy.say "Hey!"
        cassidy.say "Move over, bitch!"
        "Cassidy shoulders her way in beside Palla."
        "And somehow it seems to be settled between them."
        "Without the need to say a word, they decide to give me a blowjob!"
        if cassidy.love >= palla.love:
            call cassidy_palla_showdown_cassidy_blows from _call_cassidy_palla_showdown_cassidy_blows
        else:
            call cassidy_palla_showdown_palla_blows from _call_cassidy_palla_showdown_palla_blows
        scene bg restroom
        show palla date blush at left4
        show cassidy date normal blush at right4
        with fade
        "I collapse against the wall of the cubicle, panting like I've run a marathon."
        "Cassidy and Palla seem to be just as exhausted by their efforts too."
        "Neither of them attacks the other, either physically or verbally."
        "In fact, they're not showing any signs of fighting at all, which is weird."
        "Once we're all cleaned up, they follow me out of the bathroom and then out of the club too."
        show bg street with fade
        "All thought of having me choose between them seems to have been forgotten."
        "But what they're thinking about instead is a mystery to me."
        $ palla.sexperience += 1
        $ cassidy.sexperience += 1
        $ palla.love += 2
        $ cassidy.love += 2
        $ cassidy.flags.pallashowdown = True
    else:
        "I swear that I don't actually see who lands the first blow."
        hide cassidy
        hide palla
        show palla date annoyed at left4
        show cassidy date angry a at right4
        with vpunch
        "But suddenly there are hands flying between Cassidy and Palla."
        show cassidy at hshake
        "They're slapping at each other and grabbing handfuls of hair."
        show palla at hshake
        "It's what you might call a cat-fight, without punches and kicks."
        "But that doesn't mean it's any less vicious and violent."
        show cassidy at hshake
        show palla at hshake
        "Cassidy and Palla are tearing into each other like they mean it."
        "And I can't help but wince at each and every blow that lands."
        with hpunch
        "They're twisting and turning on the dance-floor too."
        "People jump out of their path, narrowly avoiding being caught up in the fight."
        "But some aren't that lucky, and they get shoved roughly aside."
        "All I can do is follow in Cassidy and Palla's wake."
        "They don't seem to be in the mood to listen to reason."
        with vpunch
        "And there's no way I'm stepping in to break it up either."
        "Not when I'm the reason they're fighting in the first place!"
        if cassidy.love > palla.love or (palla.love == cassidy.love and randint(0, 1) == 0):
            "Palla takes a wild swing at Cassidy."
            "It misses and spins her off balance."
            with hpunch
            "Palla tumbles to the floor and Cassidy's on her in the blink of an eye."
            "The downed girl screams as Cassidy grabs at her hair."
            "And Palla's scream gets louder as Cassidy tears out a handful from her scalp."
            "Palla edges backwards on her ass, a look of disbelief on her face."
            "Cassidy stands over her, looking down in triumph."
            "And she waves the hair in Palla's face like a trophy."
            "Palla struggles to her feet and dashes towards the door."
            hide palla with moveoutleft
            "The crowd parts to let her go."
            "And Cassidy lets out a grim chuckle."
            cassidy.say "I'd better not have to do that to another bitch, [hero.name]."
            show cassidy normal at center with move
            cassidy.say "Because if I do, I'm going to tear something off of you too!"
            mike.say "Ah...no, Cassidy..."
            mike.say "I'll be good - I swear it!"
            $ cassidy.love += 3
            $ palla.set_gone_forever()
        else:
            "Cassidy takes a wild swing at Palla."
            "It misses and spins her off balance."
            with hpunch
            "Cassidy tumbles to the floor and Palla's on her in the blink of an eye."
            "The downed girl screams as Palla grabs at her hair."
            "And Cassidy's scream gets louder as Palla tears out a handful from her scalp."
            "Cassidy edges backwards on her ass, a look of disbelief on her face."
            "Palla stands over her, looking down in triumph."
            "And she waves the hair in Cassidy's face like a trophy."
            "Cassidy struggles to her feet and dashes towards the door."
            hide cassidy with moveoutright
            "The crowd parts to let her go."
            "And Palla lets out a grim chuckle."
            palla.say "I'd better not have to do that to another bitch, [hero.name]."
            show palla normal at center with move
            palla.say "Because if I do, I'm going to tear something off of you too!"
            mike.say "Ah...no, Palla..."
            mike.say "I'll be good - I swear it!"
            $ palla.love += 3
            $ cassidy.set_gone_forever()
    $ hero.cancel_activity()
    $ game.active_date.stay = False
    $ game.room = "street"
    $ game.pass_time(1)
    return

label cassidy_palla_showdown_cassidy_blows:
    scene bitchy blowjob
    show bitchy blowjob cassidyblow pallasuck restroom
    with fade
    "So I guess this is somehow supposed to settle the argument between them."
    "And if I'd been expecting this to degenerate into a cat-fight, boy was I wrong!"
    "Somehow Cassidy and Palla settle into an instinctive rhythm."
    "First one and then the other caresses my balls."
    show bitchy blowjob sucked
    "And the other licks at the base of my cock at the same time."
    "They wind their way ever higher, swaying like sexy serpents."
    show bitchy blowjob still blow
    "Tongues and lips find their way up my shaft with agonising slowness."
    "And it's not long before I begin to lose track of who is doing what."
    show bitchy blowjob tip sucked
    "Without any warning, Cassidy swallows my cock."
    "And I swear that sometimes I don't even feel the change!"
    "Every second it goes on making me gasp ever louder with pleasure."
    show bitchy blowjob deep
    "Maybe it's the fact that two girls are working on me at once."
    "Or maybe it's the sense of danger at this happening in a public place."
    "Either way, it's not long before I feel myself begin to cum."
    menu:
        "Cum on Cassidy's face":
            "My eyes open suddenly as I lose it."
            show bitchy blowjob tip
            "And I make sure my cock is aimed where I want it to be."
            show bitchy blowjob -tip cumshot still with vpunch
            "Which is squarely at Cassidy's face!"
            "She just has time to gasp in surprise."
            show bitchy blowjob -cumshot cum onface -blow swallow
            "Then I shoot my load right between her eyes."
            "Cassidy squeals as the cum paints her cheeks."
            "It runs down, reaching her lips and then her chin too."
        "Cum in Cassidy's mouth":
            "Somehow I just know where my cock is in that moment."
            "And I open my eyes to see that I was right."
            "It's deep inside of Cassidy's mouth!"
            show bitchy blowjob cheeks cum with vpunch
            "She just has time to let out a muffled gasp surprise."
            show bitchy blowjob mouth cum with vpunch
            "Then I shoot my load straight down her throat."
            "Cassidy's eyes go wide as she swallows it down."
            show bitchy blowjob -deep -blow swallow
            "And a little spills out of her mouth, running down her chin."
    return

label cassidy_palla_showdown_palla_blows:
    scene bitchy blowjob
    show bitchy blowjob pallablow cassidysuck restroom
    "So I guess this is somehow supposed to settle the argument between them."
    "And if I'd been expecting this to degenerate into a cat-fight, boy was I wrong!"
    "Somehow Cassidy and Palla settle into an instinctive rhythm."
    "First one and then the other caresses my balls."
    show bitchy blowjob sucked
    "And the other licks at the base of my cock at the same time."
    "They wind their way ever higher, swaying like sexy serpents."
    show bitchy blowjob still blow
    "Tongues and lips find their way up my shaft with agonising slowness."
    "And it's not long before I begin to lose track of who is doing what."
    show bitchy blowjob tip sucked
    "Without any warning, Cassidy swallows my cock."
    "And I swear that sometimes I don't even feel the change!"
    "Every second it goes on making me gasp ever louder with pleasure."
    show bitchy blowjob deep
    "Maybe it's the fact that two girls are working on me at once."
    "Or maybe it's the sense of danger at this happening in a public place."
    "Either way, it's not long before I feel myself begin to cum."
    menu:
        "Cum on Palla's face":
            "My eyes open suddenly as I lose it."
            show bitchy blowjob tip
            "And I make sure my cock is aimed where I want it to be."
            show bitchy blowjob -tip cumshot still with vpunch
            "Which is squarely at Palla's face!"
            "She just has time to gasp in surprise."
            show bitchy blowjob -cumshot cum onface -blow swallow
            "Then I shoot my load right between her eyes."
            "Palla squeals as the cum paints her cheeks."
            "It runs down, reaching her lips and then her chin too."
        "Cum in Palla's mouth":
            "Somehow I just know where my cock is in that moment."
            "And I open my eyes to see that I was right."
            "It's deep inside of Palla's mouth!"
            show bitchy blowjob cheeks cum with vpunch
            "She just has time to let out a muffled gasp surprise."
            show bitchy blowjob mouth cum with vpunch
            "Then I shoot my load straight down her throat."
            "Palla's eyes go wide as she swallows it down."
            show bitchy blowjob -blow swallow
            "And a little spills out of her mouth, running down her chin."
    return


label cassidy_bitchy_harem:
    $ Harem.join_by_name("bitchy", "cassidy")
    if renpy.has_label("bitchy_harem_achievement_4") and not game.flags.cheat:
        call bitchy_harem_achievement_4 from _call_bitchy_harem_achievement_4
    return


label bitchy_harem_foursome_request:
    scene expression f"bg {game.room}"
    "At the sound of approaching footsteps I look up to see who's headed my way."
    if game.room == "nightclub":
        show palla date at left5
        show audrey date at right5
        with dissolve
    else:
        show palla casual at left5
        show audrey casual at right5
        with dissolve
    "But my mood changes as soon as I see that it's Audrey and Palla together!"
    "One of them I could easily handle, no problem at all."
    "But the pair of them together?"
    "No way any guy could hope to do that!"
    mike.say "Ah..."
    mike.say "Hey, Audrey..."
    mike.say "Hey, Palla..."
    mike.say "What can I do for..."
    "Almost as one, they cut me off before I can finish speaking."
    audrey.say "Cassidy, [hero.name]."
    audrey.say "That's what you can do for us!"
    palla.say "Yeah, that uppity little bitch!"
    palla.say "We want to talk to you about her!"
    "Ah, shit - I should have seen this one coming."
    "Audrey and Palla both happened upon me with Cassidy recently."
    "The one walked in on me and her in my office at work."
    "The other crashed our date at the nightclub."
    "But I thought those incidents ended up working out okay."
    "Everyone seemed to walk away from them happy."
    "Or at least not wanting Cassidy's head on a platter!"
    mike.say "Yeah..."
    mike.say "I kinda thought we dealt with that, didn't we?"
    mike.say "I mean, everyone seemed to walk away happy!"
    show palla annoyed
    show audrey annoyed
    "Audrey and Palla exchange a meaningful look."
    "And I think I can see them trying to suppress smiles."
    show audrey normal
    show palla normal
    audrey.say "I think you've got the wrong idea, [hero.name]."
    audrey.say "We don't want to bust your balls about Cassidy."
    palla.say "No way - we wanted to tell you we kind of like her!"
    "I shake my head, unable to believe what I'm hearing."
    mike.say "Y...you do?!?"
    mike.say "That's great!"
    mike.say "I'm sure she'll be happy to hear that."
    show audrey normal
    audrey.say "That's the thing..."
    palla.say "We want you to tell her something."
    palla.say "But it's a little bit more than that."
    audrey.say "Actually, we want you to ask her something."
    show audrey flirt
    audrey.say "We want you to ask Cassidy if we can all get together."
    "I blink, still struggling to make sense of it all."
    mike.say "You two want to have a threesome?"
    mike.say "With Cassidy?!?"
    show audrey scared
    show palla angry
    audrey.say "No, stupid!"
    palla.say "We want to have a foursome!"
    palla.say "Otherwise we wouldn't be here asking you!"
    show palla normal
    show audrey normal
    audrey.say "Well, what do you say?"
    "I take a deep breath, hold it in for a moment and then let it out with a sigh."
    "I thought that I'd gotten away with seeing Cassidy behind Audrey and Palla's backs."
    "And when I did, I made a vow to myself that I'd keep things simpler in the future."
    menu:
        "Agree to ask Cassidy":
            "But that was before they both turned up and made me an offer I'd be insane to refuse!"
            mike.say "Of course I'll ask her!"
            mike.say "That sounds like a great idea!"
            mike.say "A chance for all four of us to have some serious fun!"
            show palla happy
            show audrey happy
            "Audrey and Palla exchange a knowing glance."
            "And I see the smugness in their smiles too."
            "They were sure that I'd leap at the chance they're offering me."
            "And it looks like they were right."
            audrey.say "That's good, [hero.name]."
            audrey.say "You get a hold of Cassidy as soon as you can."
            show palla normal
            show audrey normal
            palla.say "But you'd better be quick about it."
            palla.say "Because you don't want us to change our minds."
            palla.say "Do you?"
            "I shake my head, desperate to avoid that happening."
            "And in return I get a chorus of chuckles from Audrey and Palla."
            hide palla
            hide audrey
            with dissolve
            "They turn and begin to walk away together, chatting as they go."
            "But their voices are too low for me to hear what they're saying."
            "No doubt they're congratulating themselves."
            "That and joking about how easy it is to manipulate me!"
            "But who cares about any of that?"
            "I've got the offer of a foursome on the table."
            "And all I have to do now is get the last person in on it."
            "I mean, how hard can that be?"
            $ audrey.love += 2
            $ palla.love += 2
        "Refuse to ask Cassidy":
            "I still think that I need to keep that promise."
            mike.say "No..."
            mike.say "I don't think that's be a good idea."
            show audrey surprised
            show palla annoyed
            "Audrey and Palla look instantly shocked."
            "And can you really blame them?"
            "They already know that I'm sleeping around."
            "But now I'm suddenly showing a conscience?"
            audrey.say "Excuse me?"
            audrey.say "Did you just say no?!?"
            palla.say "Huh..."
            palla.say "I thought you were into living dangerously?"
            mike.say "Not anymore, guys."
            mike.say "I could do with a little less excitement in my life!"
            show audrey annoyed
            "Audrey and Palla look like they're going to argue."
            "But then they shake their heads in disappointment."
            show palla angry
            palla.say "Your loss, [hero.name]!"
            audrey.say "Yeah, and don't worry about excitement either."
            show audrey angry
            audrey.say "Because I know two girls that you aren't going to get any from for a while!"
            hide audrey
            hide palla
            with dissolve
            "All I can do is watch them leave in silence."
            "It sucks to have to say no to them."
            "But I still think I made the right decision."
            $ audrey.love -= 4
            $ palla.love -= 4
            $ Harem.leave_by_name("bitchy", "cassidy")
    return


label bitchy_harem_foursome_ask_cassidy:
    show cassidy a
    "So now I've agreed to have a foursome with two of the other people supposed to be in on it."
    "The only thing left to do is convince the fourth person to jump in there as well."
    "Yeah, because it's going to be as easy as that!"
    "I'm going to have to be smart about this, approach Cassidy with caution."
    "I honestly have no idea how she's going to react."
    "She might be intrigued by the notion of having a foursome."
    "Or else she could be outraged and take her fury out on me!"
    "But I'm committed now, so when the opportunity presents itself, I make my pitch..."
    mike.say "Ah, Cassidy..."
    show fx question
    cassidy.say "Hmm..."
    cassidy.say "Yeah, [hero.name]?"
    hide fx
    mike.say "You know how Palla turned up while we were in the nightclub?"
    cassidy.say "Of course I do!"
    cassidy.say "How could I forget something like that?"
    mike.say "And you remember that Audrey walked in on us in my office?"
    cassidy.say "Yeah, I remember that too."
    cassidy.say "Kind of hard to when it's burned into my memory!"
    "I smile and let out a nervous chuckle."
    mike.say "Well..."
    mike.say "Audrey and Palla came to see me the other day."
    cassidy.say "They did?"
    show cassidy happy a
    cassidy.say "Well, aren't you a lucky guy!"
    cassidy.say "What crazed acts of depravity did you get up to this time?"
    show cassidy normal a
    mike.say "That's the thing, Cassidy."
    mike.say "They DID want to get up to some pretty kinky stuff."
    mike.say "Stuff that they wanted me in on, yeah."
    mike.say "But they wanted you in on it too!"
    show cassidy annoyed b
    show fx exclamation
    "Cassidy looks instantly shocked and surprised."
    "But there's something else in her eyes too."
    hide fx
    "Is that curiosity I see in there?"
    "Maybe even a little excitement?"
    cassidy.say "ME?!?"
    cassidy.say "What could they possibly want with me?"
    mike.say "They want us all to get together and get it on, Cassidy."
    mike.say "They want us to have a foursome with them!"
    if cassidy.lesbian >= 9 and cassidy.love >= 160:
        show cassidy normal b
        "Cassidy goes quiet once I've finished delivering my news."
        "And she seems to be lost in thought, pondering what I just said."
        "That has to be a good sign, right?"
        "Surely she would have blown up in my face if she was just going to say no?"
        cassidy.say "I..."
        cassidy.say "I always wondered what it'd be like."
        cassidy.say "You know, to do something that outrageous?"
        mike.say "It's a thrill, Cassidy."
        mike.say "A really mind-blowing experience!"
        "I can see now that Cassidy's battling with herself."
        "Part of her wants to say yes."
        "But another part of her is scared."
        mike.say "I trust Audrey and Palla, if that helps."
        mike.say "And I won't let anything bad happen to you either."
        show cassidy blush b
        "Cassidy seems to brighten at this."
        "My words of reassurance seem to help."
        cassidy.say "You promise, [hero.name]?"
        cassidy.say "You'll keep me safe?"
        mike.say "I promise, Cassidy."
        show cassidy happy a
        cassidy.say "Then I'll do it!"
        "Of course I'm super happy to hear Cassidy say that."
        "But I try to keep a lid on my elation, just nodding and smiling."
        "I don't want to look too eager."
        "If I do, Cassidy might think I'm hiding something from her."
        "Instead I get myself ready to tell Audrey and Palla the good news."
        $ cassidy.flags.bitchyHaremAgree = True
    else:
        show cassidy angry a
        "Cassidy's answer comes more quickly than I could have anticipated."
        "And it comes with more force than I was prepared to handle too."
        cassidy.say "They're a couple of fucking perverts!"
        cassidy.say "There's no way I'm letting them touch me!"
        mike.say "So..."
        mike.say "I'll take that as a no?"
        show fx anger
        cassidy.say "You'll take it as a hell no!"
        cassidy.say "And you can tell them I never want to see them again too!"
        hide fx
        "All I can do is nod hastily, eager to show Cassidy that I understand."
        "Sure, I'm more than a little disappointed that the foursome's not going to happen."
        "But Cassidy's been pretty understanding already."
        "Two different girls crashed our time together."
        "And some pretty crazy stuff happened when they did."
        "I guess I'm lucky she's even talking to be after that!"
        "So I let the matter drop with Cassidy."
        "And I'm already thinking of what I'll say to Audrey and Palla when I tell them the bad news."
        $ Harem.leave_by_name("bitchy", "cassidy")
        $ cassidy.love -= 10
    return


label bitchy_harem_nightclub_encounter:
    scene bg nightclub
    show dance cassidy date
    with fade
    "Cassidy and I are having a great time at the nightclub, really making every moment count."
    "The music is perfect and somehow we get one of the best spots on the dance-floor too."
    "In fact, I'm having such a good time that I end up letting my guard down totally."
    "All I can see is Cassidy's face as she beams back at me."
    "Every other face around us is nothing more than a blur."
    "That is until we slow down a little and I see two pairs of eyes staring straight at me."
    "OH FUCK - it's Audrey and Palla!"
    "How in the hell did they know I was bringing Cassidy here tonight?!?"
    "For a moment I hope in vain that they haven't noticed me across the dance-floor."
    "But then I see them shaking their heads in unison, and I know my fate is sealed."
    hide dance
    show cassidy date
    show fx question
    cassidy.say "What's the matter, [hero.name]?"
    cassidy.say "You look like you've seen a ghost or something!"
    hide fx
    mike.say "Ah...not exactly a ghost, Cassidy."
    mike.say "But something just about as scary!"
    cassidy.say "Huh?"
    cassidy.say "What does that mean?"
    mike.say "Never mind..."
    mike.say "Just follow me - we have to get out of here!"
    show fx exclamation
    cassidy.say "Wha..."
    hide fx
    hide cassidy
    "Without waiting for Cassidy to agree with me, I take hold of her hand."
    "And then I lead the way off the dance-floor, pulling her after me."
    "I make a point of heading in the opposite direction to where I saw Audrey and Palla."
    "But of course neither of them is stupid, so I don't get very far..."
    show audrey date at left
    show palla date at left4
    with hpunch
    audrey.say "Hey, [hero.name]..."
    audrey.say "Fancy seeing you here!"
    palla.say "And you're not alone either."
    palla.say "In fact, I think I recognise your charming companion there too!"
    show cassidy date at mostright4
    cassidy.say "Oh..."
    cassidy.say "Hey, Palla!"
    cassidy.say "What are you doing here?"
    audrey.say "We were going to ask you the same thing!"
    if audrey.flags.bitchyFoursome or cassidy.flags.bitchyFoursome or palla.flags.bitchyFoursome:
        mike.say "There's no issue here, right?"
        mike.say "I mean we all got on great last time, didn't we?"
        cassidy.say "Oh yeah - the foursome!"
        cassidy.say "That was you two, wasn't it?"
        show palla angry
        show audrey surprised
        "Audrey and Palla look a little surprised at Cassidy's tone."
        "Like the fact we all hooked up that time should be a bigger deal."
        show audrey angry
        audrey.say "Yeah, that was us!"
        palla.say "We kind of thought you might remember!"
        show cassidy happy
        cassidy.say "Well, when you have a social calendar as full as mine..."
        cassidy.say "It's so easy to forget what you done and who you did it with!"
        "I feel the need to step in and ease the building tension."
        mike.say "None of that really matters."
        mike.say "What does matter is that we're all here together."
        mike.say "So we should be hanging out and having a good time!"
    else:
        "I'm about to open my mouth and start making excuses."
        "But Cassidy beats me to it."
        cassidy.say "Oh..."
        cassidy.say "Hey, Palla!"
        cassidy.say "Since when did they let you back in here?"
        show audrey frown
        show palla annoyed
        "Audrey frowns at this and turns her stare on Palla."
        "In turn the other girl looks more than a little uncomfortable."
        audrey.say "Wait a minute..."
        audrey.say "You two know each other?!?"
        palla.say "Well...yeah..."
        palla.say "Let's just say we move in the same circles, okay!"
        "While Audrey and Palla's attentions are divided, I sense my chance."
        "If I can just take advantage of this opening..."
        mike.say "Isn't that crazy?"
        mike.say "What a small world!"
        mike.say "You know what - we should all grab a drink and chat."
        mike.say "Maybe we'll find out we're all connected in crazy ways too!"
    show cassidy happy
    cassidy.say "That's a great idea!"
    cassidy.say "Let's grab that booth over there!"
    "Before Audrey and Palla can object, I put my hasty plan into motion."
    scene bg vip
    show audrey date at left
    show palla date at left4
    show cassidy date at mostright4
    "Soon enough we're all crammed into a booth, drinks in hand."
    cassidy.say "So were you two here looking for [hero.name]?"
    cassidy.say "Because you look kind of mad at him!"
    audrey.say "No, that's not it."
    palla.say "We were out anyway - we just happened to see you together."
    show audrey angry
    audrey.say "And we were mad that he didn't tell us!"
    show fx question at mostright4
    "Cassidy looks a little confused at this."
    cassidy.say "But he didn't know you were going to be here, right?"
    palla.say "Erm...no."
    cassidy.say "So you're mad at him for doing the same thing as you?"
    cassidy.say "Sounds to me like you're being a little unfair!"
    show palla annoyed
    show audrey annoyed
    "I nod eagerly, sensing that Cassidy's caught them out."
    mike.say "Look, guys..."
    mike.say "We're all adults here."
    mike.say "There's no need to go pointing fingers."
    mike.say "Not when we all want the same thing!"
    show palla normal
    show audrey normal
    "This gets me a round of shrugs and nods from the girls."
    "And I can see that they're coming round to my way of thinking."
    "Soon enough we're onto a second round of drinks, then a third."
    "And just like that, the whole thing is forgotten."
    show palla happy
    show audrey happy
    show cassidy happy
    "The four of us are getting on like a bunch of old friends."
    "In fact, things only come to an end when Cassidy stands up."
    "She sways on her feet, like she's going to fall over."
    "But then she grabs the edge of the table and steadies herself."
    cassidy.say "Come on, you guys..."
    cassidy.say "Let's go back to my place!"
    "And just like that, we're into a taxi and away."
    call bitchy_harem_foursome_nightclub_intro from _call_bitchy_harem_foursome_nightclub_intro
    return

label bitchy_harem_foursome_nightclub_intro:
    scene bg taxi at blur(8), dark with dissolve
    "We've sunk so many drinks by the time we leave the nightclub that everything's a blur."
    "It even takes me a while to remember where we're going and what we're supposed to be doing."
    scene bg mansionentrance at blur(4) with dissolve
    "But when we stumble out of the taxi I recognise Cassidy's seriously impressive pad."
    "And that's all I need for it all to come flooding back to me!"
    "We're here for a foursome, Cassidy, Audrey, Palla and me!"
    play sound door_lock
    scene bg door mansionentrance at blur(2) with dissolve
    "Everyone lines up behind Cassidy as she unlocks the door."
    "And when the door opens, we all spill into the hallway in a chaotic procession."
    scene bg mansion
    show cassidy date blush
    show audrey date surprised at left
    show palla date at right
    with fade
    if audrey.flags.bitchyFoursome or cassidy.flags.bitchyFoursome or palla.flags.bitchyFoursome:
        audrey.say "Is it just me..."
        audrey.say "Or did this place get fancier since last time?"
        palla.say "I don't think it changed at all, Audrey."
        show palla happy
        palla.say "So maybe it's you that's gotten cheaper?"
    else:
        audrey.say "Whoa..."
        audrey.say "This place is seriously fancy!"
        palla.say "Yeah..."
        palla.say "I could seriously see myself living like this."
        show audrey happy
        audrey.say "In your dreams, Palla!"
    mike.say "Ah, guys..."
    mike.say "You think we can call a truce here?"
    cassidy.say "What are you guys even talking about?"
    show audrey normal
    show palla normal
    cassidy.say "I already told you this isn't my place."
    cassidy.say "It belongs to my mom and dad!"
    "At the mere mention of Cassidy's parents, I feel my hair stand on end."
    "I can't help glancing this way and that, suddenly aware of where we are."
    mike.say "Ah, yeah..."
    if game.flags.dwaynedead:
        mike.say "About your mother, Cassidy..."
    else:
        mike.say "About your parents, Cassidy..."
    show cassidy happy
    "Cassidy lets out a peal of laughter and shakes her head."
    cassidy.say "Oh, don't be silly, [hero.name]!"
    if game.flags.dwaynedead:
        cassidy.say "She's not here!"
        show cassidy normal
        cassidy.say "If she was, then we wouldn't be!"
    else:
        cassidy.say "They're not here!"
        show cassidy normal
        cassidy.say "If they were, then we wouldn't be!"
    hide cassidy
    hide palla
    hide audrey
    with dissolve
    "Cassidy leads us into a pretty swanky-looking sitting room."
    "One that reminds me of the ones you see in expensive hotels."
    "I'm almost afraid to touch anything for fear of breaking it."
    "But Cassidy herself doesn't seem to have any such fears."
    "In fact, when I'm done looking around the room, I take a step back in surprise."
    show cassidy date topless
    show audrey date at left
    show palla date at right
    with dissolve
    "And that's because she's already more than half undressed!"
    "Audrey and Palla seem to have been watching Cassidy the whole time."
    show audrey topless
    show palla topless
    "As they don't look surprised and they're starting to follow her lead!"
    show palla happy
    palla.say "What's the matter, [hero.name]?"
    palla.say "You look a little shocked!"
    show audrey annoyed
    audrey.say "You do know that we have to be naked to do this thing, right?"
    audrey.say "We're not just going to rub against each other with out clothes on!"
    "I hurry to follow their lead, trying as best I can to catch up."
    show cassidy naked happy
    show audrey naked happy
    show palla naked
    "But despite my best efforts, I'm still the last to get naked."
    "Audrey, Cassidy and Palla are already getting intimate."
    "And I hastily inject myself into the proceedings, not wanting to miss out."
    "As you can imagine, hands lips and tongues are everywhere to begin with."
    "Everyone seems to be determined to explore everyone else."
    "And that's fine for some quick, simple fun."
    "But we're supposed to be making a foursome out of this."
    show audrey normal
    show cassidy normal
    show palla normal
    "So somebody's going to have to take control."

    call bitchy_harem_foursome from _call_bitchy_harem_foursome

    scene bg mansion with fade
    "Once it's over, everyone sits back, panting and gasping."
    "But it's Cassidy that snaps back to reality first."
    show cassidy naked angry with hpunch
    cassidy.say "You guys have to get dressed - NOW!"
    "She begins picking up random items of clothing and flinging them at us."
    show audrey sad naked at left
    show palla sad naked at right
    "Audrey and Palla seem more than a little annoyed by this."
    "But I can't help chuckling at Cassidy's apparent panic."
    audrey.say "Hey!"
    palla.say "Yeah, Cassidy - what the hell?!?"
    mike.say "What's the matter, Cassidy?"
    mike.say "You said your parents were away."
    cassidy.say "No, I said they weren't here now."
    cassidy.say "But they soon will be!"
    show audrey surprised
    show palla blush
    show expression "fx exclamation" at left
    show fx exclamation at right
    "That revelation is enough to get me up and moving."
    scene bg mansion
    "Within the blink of an eye, Audrey, Palla and I are dressed."
    scene bg mansionentrance with fade
    "Then we're out of the door and looking for a taxi in record time."
    "Sure, we had a great time tonight, and I'm still sore!"
    "But that's not going to stop me fleeing at the prospect of Cassidy's parents turning up!"
    scene bg black with dissolve
    $ hero.replace_activity()
    $ game.pass_time(2)
    $ audrey.flags.bitchyFoursome += 1
    $ cassidy.flags.bitchyFoursome += 1
    $ palla.flags.bitchyFoursome += 1
    return

label bitchy_harem_foursome_appointment_intro(appointment=None):
    scene bg street
    show audrey at left5
    show palla at right5
    with fade
    "When the appointed day for the foursome finally comes around, I meet up with Audrey and Palla."
    scene bg mansionentrance with fade
    "And then we make our way over to Cassidy's place together, turning up at the time she specified."
    scene bg mansion
    show audrey casual surprised at left5
    show palla casual at right5
    with fade
    audrey.say "Whoa..."
    audrey.say "This place is pretty fancy!"
    audrey.say "I never knew Cassidy's was THIS rich!"
    mike.say "You mean her family are rich, Audrey."
    mike.say "We both work for her dad's company, remember?"
    palla.say "Hmm..."
    palla.say "I could really see myself living in a place like this."
    show audrey happy
    audrey.say "Hah!"
    audrey.say "In your dreams, Palla!"
    show palla angry
    palla.say "Hey!"
    palla.say "What's that supposed to mean?!?"
    show cassidy casual happy
    show audrey at left
    show palla at right
    cassidy.say "Welcome to my humble abode!"
    cassidy.say "And thanks again for agreeing to do this thing here."
    "I shrug off the thanks."
    show audrey normal
    show palla normal
    mike.say "It's no problem, Cassidy."
    mike.say "Anything to make you feel more at ease."
    show audrey flirt
    audrey.say "Hey, I bet you've got a wine cellar here, right?"
    palla.say "A house like this, it's practically a given!"
    show cassidy annoyed
    "Cassidy looks a little nervous for a second."
    "As though Audrey and Palla are intimidating her with their presence."
    show cassidy normal
    "But then she seems to shake if off."
    "And a second later she's her usual, confident self again."
    show cassidy happy
    cassidy.say "Of course we have a wine cellar!"
    cassidy.say "Can you even call somewhere that doesn't a home?!?"
    cassidy.say "You guys take a seat in the lounge and I'll go raid the cellar, okay?"
    show cassidy normal
    "Cassidy points us in the direction of a predictably plush lounge."
    "And we do our best to make ourselves at home while she heads for the wine cellar."
    hide cassidy
    show audrey normal at left5
    show palla at right5
    mike.say "Hey guys..."
    mike.say "Go easy on the wine, okay?"
    mike.say "Cassidy's trying to impress you."
    mike.say "So we shouldn't take advantage of her!"
    show audrey happy
    audrey.say "Forget that, [hero.name]!"
    audrey.say "Company profits paid for all of this, yeah?"
    audrey.say "That means our hard work, so we own a piece of it too!"
    palla.say "Plus it's rude to refuse someone's hospitality."
    show palla happy
    palla.say "If Cassidy wants to shower you with booze, then you should let her!"
    mike.say "Hey!"
    mike.say "I'm not trying to be a party-pooper here."
    mike.say "I just don't think we should be going crazy!"
    show cassidy casual happy
    show palla at right
    show audrey at left
    "It's at that very moment Cassidy happens to come barging into the room."
    "And she kind of makes me look stupid thanks to the sheer number of bottles she's carrying."
    cassidy.say "Here you go, guys!"
    cassidy.say "There's glasses and a bottle-opener in the cabinet over there."
    show cassidy normal
    cassidy.say "[hero.name], would you do the honours?"
    "I stagger a little as Cassidy shoves most of the bottles into my arms."
    "And I struggle to do as I'm told, not wanting to ruin the mood."
    "Sure, I don't want to get Cassidy in trouble for raiding the wine cellar."
    "But I'm more keen on not sabotaging the foursome by behaving like I have a stick up my ass!"
    "By the time I've opened a bottle and poured four glasses, the others are all sat down."
    show audrey normal
    show palla normal
    "Well, I say sat down."
    "It's more like the three of them are sprawling across the couch."
    "They remind me of ancient Roman ladies reclining at a feast."
    "But the illusion is kind of spoiled by the way they're checking their phones."
    "I had a glass to each of them and find a place for myself on the couch."
    "Cassidy looks understandably nervous."
    "And she drinks her wine far faster than the rest of us."
    "But Audrey and Palla seem more confident."
    audrey.say "Slow down, Cassidy!"
    show audrey flirt
    audrey.say "At least taste the wine!"
    show palla happy
    palla.say "Yeah, Cassidy - relax!"
    palla.say "We're going to take this nice and slow, you'll see!"
    "Cassidy smiles at this, seemingly reassured."
    "The wine's surprisingly good, and it goes down with ease."
    scene bg mansion
    "I must have gone back two or three times to refill our glasses."
    "But on the last trip, I turn around to see that something's changed."
    show cassidy casual topless annoyed blush
    show audrey casual happy at left4
    show palla casual happy at right4
    "Cassidy is slowly being stripped off by Audrey and Palla."
    "I stand there and watch, unable to do anything else."
    "Cassidy looks nervous, her cheeks flushing red."
    "But that doesn't seem to stop Audrey and Palla."
    show cassidy naked
    "Soon she's stripped to her underwear, her eyes darting this way and that."
    show audrey topless flirt at left5
    show palla normal topless at right5
    "Audrey and Palla begin to strip off their own clothes too."
    "Without a conscious thought, I put the glasses down and copy them."
    show audrey naked
    show palla naked
    "It takes perhaps less than a minute for us all to be naked."
    "And then we stand there, exchanging glances."
    "Each one of us wondering who's going to make the first move..."

    call bitchy_harem_foursome from _call_bitchy_harem_foursome_1

    scene bg mansion
    show cassidy casual
    show audrey casual at left
    show palla casual at right
    with fade
    "Afterwards, everyone hurries to clean themselves up and get dressed."
    show cassidy happy
    "Cassidy assured us that we'd be alone for the duration, that there's no need to worry."
    "But for some reason, once the act is over, we all seem to want to flee the scene."
    show palla happy
    show audrey happy
    "As we leave, promises are made that we have to meet up and do it all over again."
    "And I have no doubt that we probably will, as everyone seems to have enjoyed themselves."
    "Three girls, all of whom I know can be bitches, are smiling like cats that got the cream!"
    $ hero.replace_activity()
    $ game.pass_time(2)
    $ audrey.flags.bitchyFoursome += 1
    $ cassidy.flags.bitchyFoursome += 1
    $ palla.flags.bitchyFoursome += 1
    return

label bitchy_harem_foursome:
    $ triple_blowjob = False
    menu:
        "Fuck Cassidy":
            "Cassidy was kind enough to invite us all back to her place after the nightclub."
            "So it seems right that she should be the one to get the lion's share of the attention."
            "And all it takes is for me to begin guiding her down onto the floor for my plan to swing into action."
            show bitchy foursome cassidyfuck
            "Audrey and Palla seem to sense exactly what I'm thinking and they come to my aid."
            "They wrap their arms around Cassidy's shoulders."
            "Then they guide the other girl down until she's laid flat on her back."
            "Cassidy's eyes dart between Audrey, Palla and where my cock's being steered."
            "And they seem to grow larger the closer she gets to her ultimate destination."
            cassidy.say "H...hey..."
            cassidy.say "Be gentle..."
            cassidy.say "Okay?"
            "Audrey and Palla break into wicked laughter at Cassidy's demand."
            "They shake their heads and keep right on going, as if not concerned in the slightest."
            "That leaves Cassidy staring up at my cock as it comes ever closer."
            "But it's not like I'm just sitting here, watching whatever those two get up to."
            "I'm not about to let them use me like some kind of dildo for their own amusement."
            "So as soon as Cassidy is within reach, I take a firm hold of her."
            "And then I put myself in the position where I need to be..."
            menu:
                "Fuck her ass":
                    "I want to make this memorable for Audrey and Palla, even if they're not the ones getting the action."
                    "And the fact that I know Cassidy's pretty innocent means I don't hesitate for a moment."
                    "I push her thighs apart and take aim for the target that I have in mind."
                    "But the first thing she knows about it is the sensation of my cock pressing against her ass."
                    cassidy.say "Wha..."
                    cassidy.say "What are you doing?"
                    cassidy.say "Are you going to fuck my..."
                    "Cassidy doesn't have the time to finish asking her question."
                    "And that's because I thrust with all my might a second later."
                    show bitchy foursome cassidyfuck anal closed
                    cassidy.say "Oh..."
                    cassidy.say "Ah..."
                    cassidy.say "Mmm..."
                    "I feel all of the sounds that Cassidy's making reflected in her body."
                    "In the way that her muscles twitch and try to resist me to begin with."
                    "Then in the way that they quiver and slowly begin to surrender."
                    "I keep sinking deeper into her, a little at a time."
                    "And the feeling just keeps on getting more intense."
                    "Once I'm as deep as I can go, I start to move inside Cassidy."
                    "Helpless to resist, all she can do is lie there and take it."
                    "I'm so engrossed in the task at hand that I almost forget we're not alone."
                    "I only remember that Audrey and Palla are still there when they get in on the act."
                    "Audrey leans over Cassidy, making the most of her helpless position."
                    show bitchy foursome cassidyfuck audrey
                    "She plays with the other girl's breasts, pinching and squeezing her nipples."
                    "But Palla surprises me by doing something even more bold."
                    "Straddling Cassidy's head, she lowers herself gently."
                    show bitchy foursome cassidyfuck palla
                    "Soon enough, her pussy is no more than an inch from Cassidy's face."
                    "Not needing any prompting, Cassidy leans back her head and opens her mouth."
                    "Palla moans as Cassidy begins to lick at her pussy with something like desperation."
                    show bitchy foursome cassidyfuck lick closed
                    "All the time I'm picking up speed, fucking her harder with each second that passes."
                    "The three of us are doing all that we can to drive Cassidy crazy, to push her over the edge."
                    mike.say "Oh shit..."
                    mike.say "I think I'm going to..."
                    mike.say "Yeah, I'm going to cum!"
                    "I can only see one of Cassidy's eyes as she licks away at Palla."
                    "But the fact that it's wide open and staring straight at me means something."
                    "It means that Cassidy heard every word I just said!"
                    menu:
                        "Cum inside":
                            "With Cassidy tied up from almost every angle, I can choose how this all ends."
                            "And that means I'm going to keep right on going until I have to stop."
                            "I make sure that I'm as deep inside of her as possible when it finally happens."
                            show bitchy foursome cassidyfuck ahegao creampie -lick with hpunch
                            $ cassidy.love += 4
                            "And I add one last thrust as I shoot my load into her."
                            "Cassidy moans and squirms on the floor, unable to move more than an inch."
                            show bitchy foursome cassidyfuck lick pallasquirt
                            $ palla.love += 2
                            "I don't move or make any attempt to pull out as she cums too."
                            "And I feel every twitch and spasm of her muscles."
                            $ audrey.love += 2
                        "Pull out":
                            if cassidy.sexperience % 3:
                                show bitchy foursome cassidyfuck out opened -lick
                                "With Cassidy tied up from almost every angle, there's nothing to stop me pulling out."
                                "And I make sure to do so before the last moment, saving myself as I do so."
                                "Cassidy moans and squirms as I pull my cock all the way out of her."
                                "The sensation seems to be enough to push her over the edge before me."
                                show bitchy foursome cassidyfuck closed cumshot with hpunch
                                $ cassidy.love += 2
                                "And she cums as I finally shoot my load over her belly and thighs."
                                "I don't move or make a sound, just watching the effects of her orgasm."
                                "And I swear I see every twitch and spasm of her muscles."
                                $ audrey.love += 1
                                $ palla.love += 1
                            else:
                                $ triple_blowjob = True
                    $ cassidy.flags.anal += 1
                "Fuck her pussy":
                    "I know that Cassidy's probably more wild than she seems."
                    "But right now I'm not in the mood to make things that complicated."
                    "Not when I can see her pussy glistening in the light right in front of me."
                    "And when I can smell the scent of it too!"
                    "That's why I don't hesitate to aim the head of my cock straight at it."
                    "Then I begin to push against her lips, savouring the sensation as I do so."
                    cassidy.say "Mmm..."
                    cassidy.say "Oh yeah..."
                    cassidy.say "That feels SO good!"
                    show bitchy foursome cassidyfuck vaginal closed
                    "I can't help smiling as I listen to Cassidy."
                    "Whatever she's feeling, it can't be as good for her as it is for me right now!"
                    "All I can think about is the sensation of her lips parting for me."
                    "And then the smooth, tight feeling of my cock sinking into her pussy."
                    "I make it as slow as I can, drawing things out so that I can savour it."
                    "This means that Cassidy is fed a little more of my cock with each second that passes."
                    "And it seem that the pace is almost enough to drive her crazy!"
                    cassidy.say "Please..."
                    cassidy.say "Don't stop..."
                    cassidy.say "I want more..."
                    cassidy.say "I want all of you inside me!"
                    "I'm more than willing to give Cassidy what she wants."
                    "But the fact that I've made her wait for it means the sensation is that much sweeter."
                    "Once I'm as deep inside of her as I can go, I wait to let her feel it filling her."
                    "And then I slowly begin to move inside her, picking up speed at a gradual pace."
                    "I'm so engrossed in the task at hand that I almost forget we're not alone."
                    "I only remember that Audrey and Palla are still there when they get in on the act."
                    "Audrey leans over Cassidy, making the most of her helpless position."
                    show bitchy foursome cassidyfuck audrey
                    "She plays with the other girl's breasts, pinching and squeezing her nipples."
                    "But Palla surprises me by doing something even more bold."
                    "Straddling Cassidy's head, she lowers herself gently."
                    "Soon enough, her pussy is no more than an inch from Cassidy's face."
                    show bitchy foursome cassidyfuck palla
                    "Not needing any prompting, Cassidy leans back her head and opens her mouth."
                    "Palla moans as Cassidy begins to lick at her pussy with something like desperation."
                    show bitchy foursome cassidyfuck lick closed
                    "All this time I've been marvelling at Audrey and Palla's antics."
                    "And that means I've also lost track of what I'm doing too."
                    "Instead of keeping my speed under control, I've just gone ever faster."
                    "Right now I'm practically pounding away at Cassidy's pussy."
                    "My cock's going in and out of her at a crazy rate of speed."
                    mike.say "Oh shit..."
                    mike.say "I think I'm going to..."
                    mike.say "Yeah, I'm going to cum!"
                    "I can only see one of Cassidy's eyes as she licks away at Palla."
                    "But the fact that it's wide open and staring straight at me means something."
                    "It means that Cassidy heard every word I just said!"
                    menu:
                        "Cum inside":
                            "With Cassidy tied up from almost every angle, I can choose how this all ends."
                            "And that means I'm going to keep right on going until I have to stop."
                            "I make sure that I'm as deep inside of her as possible when it finally happens."
                            show bitchy foursome cassidyfuck ahegao creampie -lick with hpunch
                            $ cassidy.love += 4
                            "And I add one last thrust as I shoot my load into her."
                            "Cassidy moans and squirms on the floor, unable to move more than an inch."
                            show bitchy foursome cassidyfuck lick pallasquirt
                            $ palla.love += 2
                            "I don't move or make any attempt to pull out as she cums too."
                            "And I feel every twitch and spasm of her muscles."
                            $ audrey.love += 2
                        "Pull out":
                            if cassidy.sexperience % 3:
                                show bitchy foursome cassidyfuck out opened -lick
                                "With Cassidy tied up from almost every angle, there's nothing to stop me pulling out."
                                "And I make sure to do so before the last moment, saving myself as I do so."
                                "Cassidy moans and squirms as I pull my cock all the way out of her."
                                "The sensation seems to be enough to push her over the edge before me."
                                show bitchy foursome cassidyfuck closed cumshot with hpunch
                                $ cassidy.love += 2
                                "And she cums as I finally shoot my load over her belly and thighs."
                                "I don't move or make a sound, just watching the effects of her orgasm."
                                "And I swear I see every twitch and spasm of her muscles."
                                $ audrey.love += 1
                                $ palla.love += 1
                            else:
                                $ triple_blowjob = True
            $ cassidy.sexperience += 1
        "Fuck Audrey":
            "I don't want to sound like I'm trying to punish Audrey here."
            "But out of everyone here, she's got the biggest mouth of all."
            "And she's never afraid to use it to cause conflict either."
            "So maybe it's time we did a little something to shut her up?"
            mike.say "Hey, Audrey..."
            mike.say "Get over here!"
            show audrey surprised
            show fx exclamation at left5
            audrey.say "Huh?"
            audrey.say "What did you say?"
            "The moment Audrey turns to face me, I make my move."
            "I take hold of her around the waist as firmly as I can."
            hide audrey
            hide fx
            show audrey kiss naked
            $ audrey.flags.kiss += 1
            "My mouth presses against hers, still open from asking her questions."
            "And as my tongue pushes between her lips, I stroke her lower lips too."
            "Audrey's eyes go wide and she makes mewling sounds as I kiss her."
            "But there's no way that she can resit as I guide her down onto the sofa."
            hide audrey kiss
            show bitchy foursome audreyfuck
            "Palla flanks Audrey, gently but firmly holding her in place."
            show bitchy foursome audreyfuck palla
            "And Cassidy does the same to me, stroking and toying in a distracting manner."
            show bitchy foursome audreyfuck cassidy
            "By now Audrey's been reduced to a state of complete helplessness."
            "All she seems to be able to do is stare up at me."
            "Her huge brown eyes almost asking me what's going to happen next."
            menu:
                "Fuck her ass":
                    "I have one hand between Audrey's thighs right now."
                    "So I can feel just how wet she's getting down there."
                    "But I guess there's just something a little perverse inside of me in that moment."
                    "Which is why I lift Audrey's right leg higher than she's expecting."
                    "Palla's been stroking my cock this whole time."
                    "And she seems to understand what I'm doing without needing to be told."
                    "She points the head straight towards Audrey's exposed ass."
                    "And then all I have to do is guide her down and onto it!"
                    audrey.say "Oh god..."
                    audrey.say "You're gonna..."
                    audrey.say "My ass...you're gonna fuck my ass!"
                    show bitchy foursome audreyfuck anal
                    "I nod at this, my smile becoming wolfish."
                    "And Audrey lets out an uncharacteristic squeal of trepidation."
                    "But all too soon that turns into a sound of desperate pleasure."
                    "The noises that she's making match what I'm feeling too."
                    "Audrey's muscles refuse to budge at first, resisting desperately."
                    "But gravity will always have its way, and she can't resist forever."
                    "Slowly but surely, she slips downwards a little at a time."
                    "And each time she does, my cock sinks deeper into her."
                    "Audrey's muscles still squeeze me, but now it's more like a massage."
                    "They work the shaft of my cock in a delightful manner."
                    "The sensation inspiring me to begin thrusting from beneath too."
                    show bitchy foursome audreyfuck pleasure
                    audrey.say "Mmm..."
                    audrey.say "Don't stop..."
                    audrey.say "Harder...please...harder!"
                    "Palla seems to be adding to Audrey's torment too."
                    "She's playing with the other girl's exposed breasts."
                    "Tweaking the nipples with undisguised delight."
                    "This makes Audrey squirm on my cock all the more."
                    "At the same time, Cassidy is still stroking me."
                    "The more I thrust into Audrey, the more she rubs and caresses!"
                    "Between the two of them, they're going to make Audrey and I cum!"
                    "And that's why I need to decide what I'm going to do when that happens..."
                    menu:
                        "Cum inside":
                            "There's just no way that Audrey can escape right now."
                            "My cock is buried too deep inside of her to make that possible!"
                            "And so all I have to do is make one last, deep thrust..."
                            audrey.say "Oh fuck..."
                            audrey.say "You're gonna make me..."
                            audrey.say "I am...I'm cumming!"
                            show bitchy foursome audreyfuck ahegao creampie with hpunch
                            $ audrey.love += 4
                            "Audrey rides my cock as I shoot my entire load into her."
                            "She wails and gasps, taking it all as she's helpless to resist."
                            "Almost as soon as I'm done, Audrey's muscles become slack."
                            "And she collapses against me, panting for breath."
                            $ cassidy.love += 2
                            $ palla.love += 2
                        "Pull out":
                            if audrey.sexperience % 3:
                                show bitchy foursome audreyfuck normal out
                                "I could just leave Audrey right where she is until the last moment."
                                "There's no way she can escape unless I let her do it."
                                "But then I remember the sensation of my cock sinking into her ass."
                                "And I can't help wondering what it'd feel like in reverse."
                                audrey.say "Oh fuck..."
                                audrey.say "What are you..."
                                audrey.say "You're gonna make me cum!"
                                "As quickly as I can, I begin to pull my cock out of Audrey's ass."
                                "She wails and gasps, helpless to resist."
                                "And she begins to cum before it's all the way out."
                                show bitchy foursome audreyfuck cumshot pleasure with hpunch
                                "I lose it the very second that it's free shooting my load as I do so."
                                show bitchy foursome audreyfuck dickcum bodycum
                                "Almost as soon as I'm done, Audrey's muscles become slack."
                                "She collapses against me, panting for breath."
                                "And I can feel my own cum between her ass and my lap."
                                $ cassidy.love += 1
                                $ palla.love += 1
                            else:
                                $ triple_blowjob = True
                    $ audrey.flags.anal += 1
                "Fuck her pussy":
                    "I can't deny it, I'm loving the chance to get Audrey in this position."
                    "Normally she's all cocky and full to the brim with attitude."
                    "But right now she's helpless, ready to be filled to the brim with something else!"
                    "And her pussy feels so slick as I stroke it too."
                    "Almost like I could waltz right in there with no resistance at all!"
                    "Cassidy seems to read my mind."
                    show bitchy foursome audreyfuck
                    "As I lift Audrey's right leg, she leaps into action."
                    "Cassidy aims the head of my cock straight at Audrey's pussy."
                    show bitchy foursome audreyfuck cassidy
                    "And she reacts as soon as it brushes her glistening lips."
                    audrey.say "Oh fuck..."
                    audrey.say "That feels SO good!"
                    audrey.say "Please...please don't tease me!"
                    "The sheer desperation in Audrey's voice is a massive turn-on."
                    "In fact it's almost enough to make me do the exact opposite of what she's asking."
                    "But Cassidy seems to have other ideas."
                    show bitchy foursome audreyfuck vaginal
                    "So I find my cock being pushed deeper into Audrey."
                    "And a moment or two later, it's too late to change direction!"
                    "Audrey slides onto my cock, smooth as silk."
                    "Her lips part almost without resistance."
                    "And then gravity takes over, doing the rest of the work."
                    "She sinks down onto me, until I can't go any deeper."
                    audrey.say "Oh..."
                    audrey.say "Oh...please..."
                    show bitchy foursome audreyfuck vaginal pleasure
                    audrey.say "Please fuck me, [hero.name]!"
                    audrey.say "I want it so bad!"
                    "I can't help letting out a chuckle as I begin to move inside Audrey."
                    "It's not like there's any reluctance on my part to give her what she wants."
                    "And every moment that I spend doing so is a sheer pleasure for me too!"
                    "At the same time as I'm thrusting in and out of Audrey, Palla and Cassidy aren't still either."
                    show bitchy foursome audreyfuck palla
                    "Palla leans in towards Audrey, a look of genuine fascination on her face."
                    "She's playing with the other girl's exposed breasts, pinching and squeezing."
                    "And there's nothing that Audrey can do to resist her attentions."
                    "But on the other side, Cassidy's equally enthralled with me too!"
                    "She busies herself playing with my balls and stroking the base of my cock."
                    "The sensation is almost enough to distract me from what I'm doing to Audrey!"
                    "Thanks to Cassidy and Palla, the both of us are being pushed even further."
                    "I thrust harder and faster into Audrey."
                    "And she rides my cock with what feels like sheer desperation!"
                    audrey.say "I..."
                    audrey.say "I can't take it..."
                    audrey.say "I'm gonna cum!"
                    mike.say "Tell me about it, Audrey!"
                    mike.say "Me too..."
                    menu:
                        "Cum inside":
                            "There's just no way that Audrey can escape right now."
                            "My cock is buried too deep inside of her to make that possible!"
                            "And so all I have to do is make one last, deep thrust..."
                            audrey.say "Oh fuck..."
                            audrey.say "You're gonna make me..."
                            show bitchy foursome audreyfuck ahegao creampie with hpunch
                            $ audrey.love += 4
                            audrey.say "I am...I'm cumming!"
                            with hpunch
                            "Audrey rides my cock as I shoot my entire load into her."
                            "She wails and gasps, taking it all as she's helpless to resist."
                            "Almost as soon as I'm done, Audrey's muscles become slack."
                            "And she collapses against me, panting for breath."
                            $ cassidy.love += 2
                            $ palla.love += 2
                        "Pull out":
                            if audrey.sexperience % 3:
                                "I could just leave Audrey right where she is until the last moment."
                                "There's no way she can escape unless I let her do it."
                                "But then I remember the sensation of my cock sinking into her pussy."
                                "And I can't help wondering what it'd feel like in reverse."
                                audrey.say "Oh fuck..."
                                audrey.say "What are you..."
                                audrey.say "You're gonna make me cum!"
                                show bitchy foursome audreyfuck normal out
                                "As quickly as I can, I begin to pull my cock out of Audrey's pussy."
                                "She wails and gasps, helpless to resist."
                                "And she begins to cum before it's all the way out."
                                show bitchy foursome audreyfuck cumshot pleasure with hpunch
                                $ audrey.love += 2
                                "I lose it the very second that it's free shooting my load as I do so."
                                "Almost as soon as I'm done, Audrey's muscles become slack."
                                "She collapses against me, panting for breath."
                                "And I can feel my own cum between her ass and my lap."
                                $ cassidy.love += 1
                                $ palla.love += 1
                            else:
                                $ triple_blowjob = True
            $ audrey.sexperience += 1
        "Fuck Palla":

            "Choosing between Cassidy, Audrey and Palla was never going to be easy."
            "Each of them would be an amazing prospect on their own."
            "But together it's almost impossible to pick one over the other two."
            "So instead I base my choice on confidence and experience."
            "Audrey's the one with the biggest mouth for sure."
            "But Palla's got her beaten in terms of sheer swagger."
            "And so she's the one that I choose."
            "I lie down on the floor and beckon for her to join me."
            show bitchy foursome pallafuck
            "Audrey appears behind Palla, taking hold of her shoulders."
            "She looks a little surprised at first, but then she goes with it."
            show bitchy foursome pallafuck audrey
            palla.say "Okay, okay..."
            palla.say "Have it your way!"
            palla.say "Just make sure that I enjoy it!"
            "Cassidy follows us down onto the floor without hesitation."
            show bitchy foursome pallafuck cassidy
            "But Cassidy holds back for a moment, then hurries to do the same."
            "Then she leans in to take a firm hold of my cock."
            show bitchy foursome pallafuck hand
            "They're surrounding Palla, front and back."
            "Almost like they think she might try to escape at any moment."
            "Not that I'm about to let anything like that happen."
            "My cock is rock-hard and I'm itching to get started."
            "And I can almost feel the heat from Palla's pussy too!"
            menu:
                "Fuck her ass":
                    "I could easily point the head of my cock at Palla's pussy."
                    "But where's the fun in playing it safe like that?"
                    "After all, we are supposed to be having a foursome here."
                    "And so it's probably better to be as daring as possible, right?"
                    "That's why I aim for the other hole down there."
                    "The first thing that Palla knows about it is when she feels my cock between her buttocks."
                    show bitchy foursome pallafuck anal
                    palla.say "Wh...wha..."
                    palla.say "You're in the wrong place!"
                    palla.say "That's my ass - not my pussy!"
                    audrey.say "Oh, I don't think so, Palla!"
                    cassidy.say "No - I think he's right on target!"
                    "Palla's eyes go wide as I push as hard as I dare."
                    "She squeals in alarm as I feel my cock begin to push into her ass."
                    "It's hard going at first, as her muscles are strong and they instinctively resist."
                    "But gravity and Audrey are both working against her."
                    "And slowly, little by little, Palla starts to sink downwards."
                    "With my hands on her haunches, I guide her as she does so."
                    "There's no point in pulling her down, as the work is being done for me."
                    "That and the fact I want Palla to enjoy this too."
                    "And by the time she's taken me as deep as she can, it sounds like that's how it is."
                    show bitchy foursome pallafuck pleasure
                    palla.say "Mmm..."
                    palla.say "I...I never knew..."
                    palla.say "Never knew it could feel like this!"
                    "I can't help smiling to myself as I begin to move inside Palla."
                    "She feels so tight and the sensation is so good around my cock."
                    "The sounds that she starts to make only add to the thrill for me."
                    "Pretty soon Palla's riding me like her life depends on it!"
                    "Audrey's still behind her, offering support."
                    "But at the same time she's also taking advantage of Palla's helplessness."
                    "I can see her hands all over the other girl's breasts, pinching and squeezing."
                    "At the same time Cassidy's doing similar things to me."
                    "I can feel her playing with my balls and stroking the base of my shaft."
                    "Try as I might, there's no way I can ignore what she's doing."
                    "Both Palla and I are being pushed ever onwards."
                    "It'd be enough to be buried inside of her."
                    "But Audrey and Cassidy are making sure we're pushed to the limit!"
                    palla.say "Oh..."
                    palla.say "Oh fuck..."
                    palla.say "I can't hold on!"
                    mike.say "Me..."
                    mike.say "Me neither..."
                    mike.say "Here it comes!"
                    menu:
                        "Cum inside":
                            "I don't know if I could pull out before it happens, even if I wanted to!"
                            "So instead I just tighten my grip on Palla and hold on until the very end."
                            with vpunch
                            "This means that I'm as deep as possible when I shoot my load."
                            with vpunch
                            "Palla wails as I fill her ass, the sticky cum already beginning to seep out."
                            show bitchy foursome pallafuck ahegao creampie with vpunch
                            $ palla.love += 4
                            "She wriggles and squirms as the last bursts are pumped into her."
                            "And she keeps on going afterwards too, her own orgasm taking over."
                            "I can feel my muscles turning to water after all that effort."
                            "And it takes Audrey and Cassidy to hold Palla up as I sag beneath her."
                            $ audrey.love += 2
                            $ cassidy.love += 2
                        "Pull out":
                            if palla.sexperience % 3:
                                "I don't think that I could have pulled out of Palla on my own."
                                "But Audrey seems to be able to read my mind in the last few moments."
                                show bitchy foursome pallafuck normal out
                                "She supports Palla as I desperately yank my cock out of her."
                                "Cassidy wriggles and squirms as the sensation makes her cum too."
                                show bitchy foursome pallafuck pleasure cumshot with vpunch
                                $ palla.love += 2
                                "And she gasps in surprise as I shoot my load all over her back."
                                "I can feel my muscles turning to water after all that effort."
                                show bitchy foursome pallafuck dickcum
                                "And it takes Audrey and Palla to hold Palla up as I sag beneath her."
                                $ audrey.love += 1
                                $ cassidy.love += 1
                            else:
                                $ triple_blowjob = True
                    $ palla.flags.anal += 1
                "Fuck her pussy":
                    "Don't think that I'm going all out to take advantage of Palla right now!"
                    "I'm not some kind of freaky sex monster!"
                    "That's why I make sure to aim my cock straight at her pussy."
                    "Keeping things familiar will help to ease her into this thing."
                    "As I guide Palla down and onto my cock, I sense something from Audrey and Cassidy."
                    "It's brief, lasting only for a moment."
                    "But I get the feeling that it's resistance to my plan."
                    "Maybe they're wanting to have a little more wild fun with Palla."
                    "But whatever the case, I'm not about to give in and let them take control."
                    "A moment later, the head of my cock presses against the lips of Palla's pussy."
                    show bitchy foursome pallafuck vaginal
                    palla.say "Oh wow..."
                    palla.say "Oh...it's...it's so big!"
                    palla.say "I want it...I want it inside of me!"
                    "I can't help smiling at Cassidy's pleas."
                    "Sure, she can be a brat some times."
                    "But indulging her is more fun than you can imagine!"
                    "I begin to pull Palla downwards, sinking into her."
                    "She yelps and then moans as her lips part."
                    "I can't help gasping myself."
                    "The sensation of pushing into her is so smooth."
                    "The muscles of her pussy are so tight."
                    "It's like nothing I can describe!"
                    "Before I know it, Palla's riding me like her life depends on it."
                    "I keep on thrusting upwards, but she's pushing downwards too!"
                    "I can't tell which one of us is doing the most work."
                    show bitchy foursome pallafuck pleasure
                    "All I can do is keep on going, holding onto her for all I'm worth."
                    "Audrey's right behind Palla, supporting her."
                    "But at the same time she's also taking advantage of the other girl's helplessness."
                    "Her hands are all over Palla's breasts, pinching and squeezing."
                    "At the same time Cassidy's doing similar things to me."
                    show bitchy foursome pallafuck hand
                    "I can feel her playing with my balls and stroking the base of my shaft."
                    "Try as I might, there's no way I can ignore what she's doing."
                    "Both Palla and I are being pushed ever onwards."
                    "It'd be enough to be buried inside of her."
                    "But Audrey and Cassidy are making sure we're pushed to the limit!"
                    palla.say "Ah..."
                    palla.say "Oh...oh god..."
                    palla.say "I'm...I'm gonna cum!"
                    mike.say "Me too..."
                    mike.say "Me too...Palla..."
                    mike.say "I can't hold on any longer!"
                    menu:
                        "Cum inside":
                            "I don't know if I could pull out before it happens, even if I wanted to!"
                            "So instead I just tighten my grip on Palla and hold on until the very end."
                            with vpunch
                            "This means that I'm as deep as possible when I shoot my load."
                            show bitchy foursome pallafuck ahegao creampie with vpunch
                            $ palla.love += 4
                            "Palla wails as I fill her pussy, the sticky cum already beginning to seep out."
                            "She wriggles and squirms as the last bursts are pumped into her."
                            "And she keeps on going afterwards too, her own orgasm taking over."
                            "I can feel my muscles turning to water after all that effort."
                            "And it takes Audrey and Cassidy to hold Palla up as I sag beneath her."
                            $ audrey.love += 2
                            $ cassidy.love += 2
                        "Pull out":
                            if palla.sexperience % 3:
                                "I don't think that I could have pulled out of Palla on my own."
                                "But Audrey seems to be able to read my mind in the last few moments."
                                show bitchy foursome pallafuck normal out
                                "She supports Palla as I desperately yank my cock out of her."
                                "Palla wriggles and squirms as the sensation makes her cum too."
                                show bitchy foursome pallafuck pleasure cumshot with vpunch
                                $ palla.love += 2
                                "And she gasps in surprise as I shoot my load all over her back."
                                "I can feel my muscles turning to water after all that effort."
                                show bitchy foursome pallafuck dickcum
                                "And it takes Audrey and Cassidy to hold Palla up as I sag beneath her."
                                $ audrey.love += 1
                                $ cassidy.love += 1
                            else:
                                $ triple_blowjob = True
            $ palla.sexperience += 1

    if triple_blowjob:
        if palla.sexperience % 3:
            "I'm just about to shoot my load, on the very edge of losing it."
            "But a moment later, Audrey, Cassidy and Palla spring into action."
            "Before I know what's happening, I find myself shoved into the sofa."
            show bitchy foursome cumshare palla cassidy audrey
            "And all three of them are kneeling in front of me."
            "Audrey's to my left, Cassidy to my right and Palla between them."
            "They all have an almost hungry look on their faces."
            "One that makes me feel a little uneasy!"
            "Then, almost as one, they pounce on my cock."
            "What follows is one of the most intricate and amazing blowjobs I've ever experienced."
            show bitchy foursome cumshare cassidysuck audreyballs cassidyclosed
            "Somehow, without a word between them, they work my cock like a team!"
            "It goes from Audrey's mouth to Palla's and then to Cassidy's."
            show bitchy foursome cumshare out audreymouth cassidyopened
            "Whoever has it kisses, sucks and licks."
            show bitchy foursome cumshare pallasuck pallaclosed
            "And at the same time, the other two stroke and caress."
            "The whole time they're looking up at me, as if for approval."
            show bitchy foursome cumshare out pallaopened
            "Three beautiful faces and three pairs of wide, sparkling eyes."
            show bitchy foursome cumshare audreysuck audreyclosed
            "The sight of them alone would be enough for me to get myself off."
            "But combined with what they're doing to me..."
            show bitchy foursome cumshare cassidysuck audreyballs cassidyclosed
            "It's all that I can do to hold on for more than a few minutes."
            show bitchy foursome cumshare out audreymouth cassidyopened
            "I've lost track of how many times they've swapped my cock between them."
            show bitchy foursome cumshare pallasuck pallaclosed
            "And I'm even a little hazy on who's sucking it when I lose control."
            show bitchy foursome cumshare out pallaopened cumshot with vpunch
            "But that hardly matters, as all three of them crowd in."
            show bitchy foursome cumshare dickcum audreyclosed cassidyclosed pallaclosed pallamouthcum audreymouthcum cassidymouthcum -cumshot with vpunch
            "Audrey, Cassidy and Palla giggle as I cum over them."
            show bitchy foursome cumshare limp share audreyopened cassidyopened pallaopened
            "They have their eyes closed and their mouths open."
            "And I watch as they try to catch as much as they can on their tongues too!"
        else:
            "Before I know what's happening, I feel my cock being pulled out."
            "It pops free with a comical sound, leaving me confused, even a little disoriented."
            show bitchy foursome cumshare palla cassidy audrey
            "Then I see Audrey and Palla kneeling before me."
            "They summon Cassidy over too, and then get down to business."
            show bitchy foursome cumshare cassidysuck audreyballs cassidyclosed
            "At first it's up to Audrey and Cassidy to take the lead."
            "They lick and suck at my cock with confidence."
            show bitchy foursome cumshare out audreymouth cassidyopened
            "And it doesn't take long for Palla to join in."
            show bitchy foursome cumshare pallasuck pallaclosed
            "Soon enough they swapping it around between them."
            "I have no idea without looking down exactly where it is!"
            show bitchy foursome cumshare out pallaopened
            "And when I do look down, I see three heads bobbing away."
            show bitchy foursome cumshare audreysuck audreyclosed
            "I was almost ready to cum before they started doing this."
            "So it doesn't take long for me to get to that point again."
            show bitchy foursome cumshare out audreyopened cumshot with vpunch
            "I shoot my load just as one of them is passing my cock to the next."
            with vpunch
            "It hangs in the air, still swaying from popping out of a mouth."
            show bitchy foursome cumshare dickcum audreyclosed cassidyclosed pallaclosed pallamouthcum audreymouthcum cassidymouthcum -cumshot with vpunch
            "This means that all three of them get a showering in short order!"
            "Cassidy, Audrey and Palla all have their faces striped with semen."
            show bitchy foursome cumshare limp share audreyopened cassidyopened pallaopened
            "And they have their eyes and mouths open too."
            "Which means that each of them gets a mouthful along the way."
        $ audrey.love += 3
        $ cassidy.love += 3
        $ palla.love += 3
    if renpy.has_label("bitchy_harem_achievement_5") and not game.flags.cheat:
        call bitchy_harem_achievement_5 from _call_bitchy_harem_achievement_5
    return


label audrey_cassidy_palla_propose_male:
    "Sometimes I really have to stop and pinch myself to check that I'm not dreaming."
    "I really am in a relationship with three girls at once, one hundred percent for real!"
    "And on top of that, somehow I've managed to balance Audrey, Cassidy and Palla."
    "A self-confessed bitch, a rich daddy's girl and an aspiring fashion icon."
    "Any one of them would be a challenge on their own, let alone all together!"
    "I dunno - maybe that's the reason that it works?"
    "All of those conflicts and potential arguments, all pulling in different directions."
    "Perhaps it's the tension that makes the relationship a success."
    "Whatever the reason, it's made me a happy guy."
    "And it's also inspired me to want to take things to the next level."
    "Even if that does mean I have to go out and buy THREE rings!"
    "Urgh...I hope they say yes when I pop the question."
    "And if not, I'd better keep a hold of the receipt..."
    show audrey casual annoyed at left
    audrey.say "Geez, Palla..."
    audrey.say "That outfit looks like underwear!"
    show cassidy casual annoyed
    cassidy.say "Yeah..."
    cassidy.say "My Daddy would NEVER let me wear something like that!"
    show palla casual annoyed at right
    palla.say "Hah!"
    palla.say "You two and your daddies are clueless."
    palla.say "This just so happens to be all the rage in Paris right now!"
    show audrey normal
    audrey.say "What do you think, [hero.name]?"
    show cassidy normal
    cassidy.say "Yeah, [hero.name]..."
    cassidy.say "Do you think Palla's outfit looks like underwear?"
    show palla normal
    "As one the three of them turn towards me."
    "And they all have the same look of surprise on their faces too."
    "Because they're having to look down at me kneeling in front of them."
    mike.say "Audrey..."
    mike.say "Cassidy..."
    mike.say "Palla..."
    mike.say "Will you marry me?"
    "Now they're not looking at me anymore."
    show audrey surprised
    show cassidy annoyed
    show palla annoyed
    "Instead they're exchanging glances between themselves."
    "And with every moment that passes, my anxiety grows."
    "Ah fuck...they'd better give me an answer soon."
    "Because I can't take much more of this!"
    if audrey.love >= 195 and cassidy.love >= 195 and palla.love >= 195:
        audrey.say "Wow!"
        show audrey normal
        audrey.say "Look at you with the surprise question!"
        audrey.say "Yeah, what the hell - I'll marry you."
        audrey.say "Because who else would?"
        cassidy.say "Oh yes, [hero.name]!"
        show cassidy normal
        cassidy.say "I REALLY want you to be my husband!"
        palla.say "Me too, [hero.name]."
        show palla normal
        palla.say "You're not the most stylish guy in the world."
        palla.say "But you clean up pretty nicely!"
        "Together they thrust their hands out towards me."
        "And I hurry to push the rings onto their fingers."
        "I feel like I'm dreaming all of this."
        "Like any moment I'll wake up and it won't be real."
        "As I get up, I can't help shaking my head."
        mike.say "Wow..."
        mike.say "You said yes!"
        mike.say "All three of you said yes!"
        "The girls are all knowing smiles and giggles by now."
        "Admiring their rings and waving away my amazement."
        cassidy.say "Of course we did, [hero.name]!"
        show cassidy happy
        cassidy.say "You're the only man who treats me more like a princess than my Daddy."
        cassidy.say "And when we're together, you make me feel like a queen too!"
        palla.say "Yeah, that's true."
        show palla happy
        palla.say "We look good together too."
        palla.say "Like, you dress far better now, thanks to me."
        palla.say "But you still don't look good enough to take the attention off of me."
        audrey.say "And you're my boss."
        show audrey happy
        audrey.say "So I kind of have to say yes."
        audrey.say "KIDDING!"
        "All I can do is laugh and shake my head."
        "Already wondering what I've let myself in for!"
        $ audrey.set_fiance()
        $ cassidy.set_fiance()
        $ palla.set_fiance()
    elif audrey.love >= 195 and cassidy.love >= 195 and palla.love < 195:
        audrey.say "Wow!"
        show audrey normal
        audrey.say "Look at you with the surprise question!"
        audrey.say "Yeah, what the hell - I'll marry you."
        audrey.say "Because who else would?"
        cassidy.say "Me too, [hero.name]!"
        show cassidy normal
        cassidy.say "I REALLY want you to be my husband!"
        palla.say "Oh come on!"
        show palla annoyed
        palla.say "You can't be serious?"
        palla.say "Can you?"
        mike.say "Erm..."
        mike.say "Yeah, Palla - I kinda was!"
        "Before I can say anything more, Audrey and Cassidy confront Palla."
        cassidy.say "What are you talking about, Palla?!?"
        audrey.say "Forget her, [hero.name]!"
        show audrey happy
        audrey.say "Looks like it's just you, me and Cassidy."
        "I give Palla a pleading look, hoping that she'll change her mind."
        "But instead she turns her back on me and starts walking away."
        hide palla
        "Which leaves me getting to my feet and staring after her."
        show cassidy happy at right4 with move
        show audrey happy at left4 with move
        "Audrey and Cassidy distract me by almost throwing themselves into my arms a moment later."
        "They hold up their hands, and I hastily slide the ring onto their fingers."
        "I have no idea where I go with Palla from this point on."
        "And for the moment, all I can do is hold Audrey and Cassidy close."
        $ audrey.set_fiance()
        $ cassidy.set_fiance()
        $ palla.love -= 25
        $ palla.sub -= 25
    elif audrey.love >= 195 and palla.love >= 195 and cassidy.love < 195:
        audrey.say "Wow!"
        show audrey normal
        audrey.say "Look at you with the surprise question!"
        audrey.say "Yeah, what the hell - I'll marry you."
        audrey.say "Because who else would?"
        palla.say "Me too, [hero.name]."
        show palla normal
        palla.say "You're not the most stylish guy in the world."
        palla.say "But you clean up pretty nicely!"
        cassidy.say "[hero.name], I'm too young to get married!"
        cassidy.say "That's something old people would do."
        cassidy.say "Like my parents!"
        show cassidy annoyed
        cassidy.say "You can't be serious?"
        cassidy.say "Can you?"
        mike.say "Erm..."
        mike.say "Yeah, Cassidy - I kinda was!"
        "Before I can say anything more, Audrey and Palla confront Cassidy."
        show palla annoyed
        palla.say "What are you talking about, Cassidy?!?"
        audrey.say "Forget her, [hero.name]!"
        show audrey happy
        audrey.say "Looks like it's just you, me and Palla."
        "I give Cassidy a pleading look, hoping that she'll change her mind."
        "But instead she turns her back on me and starts walking away."
        hide cassidy
        "Which leaves me getting to my feet and staring after her."
        show palla happy at right4 with move
        show audrey happy at left4 with move
        "Audrey and Palla distract me by almost throwing themselves into my arms a moment later."
        "They hold up their hands, and I hastily slide the ring onto their fingers."
        "I have no idea where I go with Palla from this point on."
        "And for the moment, all I can do is hold Audrey and Palla close."
        $ audrey.set_fiance()
        $ palla.set_fiance()
        $ cassidy.love -= 25
        $ cassidy.sub -= 25
    elif cassidy.love >= 195 and palla.love >= 195 and audrey.love < 195:
        palla.say "Of course I'll marry you, [hero.name]."
        show palla normal
        palla.say "Did you think I'd say no?"
        cassidy.say "Me too, [hero.name]!"
        show cassidy normal
        cassidy.say "I REALLY want you to be my husband!"
        audrey.say "Erm...no!"
        audrey.say "I don't think so."
        show audrey annoyed
        audrey.say "This whole thing here, it's fun."
        audrey.say "But it's not what I want to do with the rest of my life."
        "Before I can say anything more, Cassidy and Palla confront Audrey."
        show cassidy annoyed
        cassidy.say "What are you talking about, Audrey?!?"
        palla.say "Forget her, [hero.name]!"
        show palla happy
        palla.say "Looks like it's just you, me and Cassidy."
        "I give Audrey a pleading look, hoping that she'll change her mind."
        "But instead she turns her back on me and starts walking away."
        hide audrey
        "Which leaves me getting to my feet and staring after her."
        show cassidy happy at left4 with move
        show palla happy at right4 with move
        "Cassidy and Palla distract me by almost throwing themselves into my arms a moment later."
        "They hold up their hands, and I hastily slide the ring onto their fingers."
        "I have no idea where I go with Audrey from this point on."
        "And for the moment, all I can do is hold Cassidy and Palla close."
        $ cassidy.set_fiance()
        $ palla.set_fiance()
        $ audrey.love -= 25
        $ audrey.sub -= 25
    elif audrey.love >= 195 and cassidy.love < 195 and palla.love < 195:
        audrey.say "Wow!"
        show audrey normal
        audrey.say "Look at you with the surprise question!"
        audrey.say "Yeah, what the hell - I'll marry you."
        audrey.say "Because who else would?"
        palla.say "Oh come on!"
        show palla annoyed
        palla.say "You can't be serious?"
        palla.say "Can you?"
        mike.say "Erm..."
        mike.say "I kinda was!"
        cassidy.say "[hero.name], I'm too young to get married!"
        show cassidy annoyed
        cassidy.say "That's something old people would do."
        cassidy.say "Like my parents!"
        "Audrey snorts and shakes her head."
        "Then she steps over and pulls me to my feet."
        audrey.say "Forget them, [hero.name]!"
        show audrey happy
        audrey.say "Looks like it's just you and me."
        "Cassidy and Palla look like they're about to argue."
        "But then they shake their heads and turn on their heels."
        hide palla
        hide cassidy
        show audrey happy at center with move
        "Then they walk away, leaving me to slide the ring onto Audrey's finger."
        "I have no idea where I go with Cassidy and Palla from this point on."
        "And for the moment, all I can do is hold Audrey close."
        $ audrey.set_fiance()
        $ cassidy.love -= 25
        $ cassidy.sub -= 25
        $ palla.love -= 25
        $ palla.sub -= 25
    elif cassidy.love >= 195 and audrey.love < 195 and palla.love < 195:
        cassidy.say "Oh yes, [hero.name]!"
        show cassidy normal
        cassidy.say "I REALLY want you to be my husband!"
        audrey.say "Erm...no!"
        show audrey annoyed
        audrey.say "I don't think so."
        audrey.say "This whole thing here, it's fun."
        audrey.say "But it's not what I want to do with the rest of my life."
        palla.say "I can't be tied down to a relationship, [hero.name]."
        show palla annoyed
        palla.say "I have a career and a life of my own."
        palla.say "I'm not supposed to be someone's wife!"
        "Before I can say another word, Cassidy cuts jumps in."
        cassidy.say "What are you guys talking about?!?"
        show cassidy annoyed
        cassidy.say "I want to marry you, [hero.name]!"
        cassidy.say "You're the only man who treats me more like a princess than my Daddy."
        show cassidy happy
        cassidy.say "And when we're together, you make me feel like a queen too!"
        "I give Audrey and Palla a pleading look, hoping that they'll change their minds."
        "But instead they turn their backs on me and starts walking away."
        hide audrey
        hide palla
        show cassidy happy at center with move
        "Which leaves me getting to my feet and staring after them."
        "Cassidy distracts me by almost throwing herself into my arms a moment later."
        "She holds up her hand, and I hastily slide the ring onto her finger."
        "I have no idea where I go with Audrey and Palla from this point on."
        "And for the moment, all I can do is hold Cassidy close."
        $ cassidy.set_fiance()
        $ audrey.love -= 25
        $ audrey.sub -= 25
        $ palla.love -= 25
        $ palla.sub -= 25
    elif palla.love >= 195 and audrey.love < 195 and cassidy.love < 195:
        palla.say "Of course I'll marry you, [hero.name]."
        show palla normal
        palla.say "Did you think I'd say no?"
        audrey.say "Erm...no!"
        show audrey annoyed
        audrey.say "I don't think so."
        audrey.say "This whole thing here, it's fun."
        audrey.say "But it's not what I want to do with the rest of my life."
        cassidy.say "[hero.name], I'm too young to get married!"
        show cassidy annoyed
        cassidy.say "That's something old people would do."
        cassidy.say "Like my parents!"
        "Palla snorts and shakes her head."
        "Then she steps over the other girls and pulls me to my feet."
        palla.say "Forget them, [hero.name]!"
        show palla happy
        palla.say "Looks like it's just you and me."
        "Audrey and Cassidy look like they're about to argue."
        "But then they shake their heads and turn on their heels."
        hide audrey
        hide cassidy
        show palla happy at center with move
        "Then they walk away, leaving me to slide the ring onto Palla's finger."
        "I have no idea where I go with Audrey and Cassidy from this point on."
        "And for the moment, all I can do is hold Palla close."
        $ palla.set_fiance()
        $ audrey.love -= 25
        $ cassidy.sub -= 25
        $ cassidy.love -= 25
        $ cassidy.sub -= 25
    elif audrey.love < 195 and cassidy.love < 195 and palla.love < 195:
        audrey.say "Erm...no!"
        show audrey annoyed
        audrey.say "I don't think so."
        audrey.say "This whole thing here, it's fun."
        audrey.say "But it's not what I want to do with the rest of my life."
        palla.say "I can't be tied down to a relationship, [hero.name]."
        show palla annoyed
        palla.say "I have a career and a life of my own."
        palla.say "I'm not supposed to be someone's wife!"
        cassidy.say "[hero.name], I'm too young to get married!"
        show cassidy annoyed
        cassidy.say "That's something old people would do."
        cassidy.say "Like my parents!"
        "I try as best I can to force a smile onto my face."
        "Then I put the rings back into my pocket."
        "Slowly getting to my feet, I manage a weak laugh."
        mike.say "Ah...yeah..."
        mike.say "Good points and well made."
        mike.say "Maybe I can get a refund..."
        $ audrey.love -= 25
        $ audrey.sub -= 25
        $ cassidy.love -= 25
        $ cassidy.sub -= 25
        $ palla.love -= 25
        $ palla.sub -= 25
    return

label audrey_cassidy_propose_male:
    "Sometimes I'm surprised that Audrey and Cassidy can even be in the same room together."
    "A sarcastic bitch that likes to cause a scene and a spoilt little daddy's girl."
    "They should be like two elements that explode when you put them together."
    "But somehow they seem to be able to co-exist when we're hanging out as a threesome."
    "At first I wondered what was different, and then it struck me."
    "I must be the thing that's making the difference here!"
    "Yeah, I know - it sounds kind of egotistical for me to say it."
    "But somehow I make Audrey and Cassidy get along with one another."
    "And it's not like I have to battle to get it done either."
    "Sure, when we're together their usual bad habits are still there."
    "Audrey likes to poke and prod until she gets a reaction."
    "And Cassidy can be pig-headed, demanding her own way."
    "Yet each of them seems to know when to back down."
    "Which makes being with them both a lot of fun."
    "Because when their true personalities shine through, Audrey and Cassidy are amazing."
    "And that's why I raided my savings to buy the two matching rings I have in my pocket."
    "As soon as the right moment presents itself, I'm going to pop the question."
    "All I have to do is wait for it to come around..."
    show audrey casual annoyed at left5
    audrey.say "Have you ever paid for something yourself, Cassidy?"
    audrey.say "Or is it always daddy that pays for your shit?"
    show cassidy casual annoyed at right5
    cassidy.say "Urgh..."
    cassidy.say "You're like a snob, Audrey - but against rich people!"
    cassidy.say "Tell her, [hero.name] - make her shut up!"
    audrey.say "Erm, [hero.name]..."
    audrey.say "What are you doing?!?"
    "I hold up the two rings, one in each hand."
    "And I try to look confident as I shake my head."
    mike.say "What does it look like, Audrey?"
    mike.say "I'm trying to propose to the both of you!"
    show audrey normal
    show cassidy normal
    "For what feels like the first time, Audrey and Cassidy are both speechless."
    "All they seem to be able to do is stare at me in sheer amazement."
    mike.say "Well?"
    mike.say "Are you going to give me an answer?"
    if audrey.love >= 195 and cassidy.love >= 195:
        "I'm almost wincing as the girls open their mouths to speak."
        "Because part of me is sure that they're going to turn me down."
        audrey.say "Aww..."
        audrey.say "How can I say no to a face like that!"
        show audrey joke
        audrey.say "Seriously, [hero.name] - you look like a kicked puppy!"
        cassidy.say "Don't be mean, Audrey!"
        cassidy.say "Yes, [hero.name]!"
        show cassidy happy
        cassidy.say "Of course I want to marry you."
        cassidy.say "And so does she!"
        "It's almost too much for me to take."
        "And I'm shaking as I put the rings onto their fingers."
        "I try to get up too, but they have to give me a hand."
        mike.say "Whoa..."
        mike.say "I guess the nerves got to me a little!"
        cassidy.say "Don't worry, we're here to help you!"
        audrey.say "Yeah, [hero.name]..."
        show audrey happy
        audrey.say "We're gonna be getting married."
        audrey.say "So we kinda have to pick your sorry ass up!"
        "I laugh and shake my head."
        "Because I'm already wondering what I've let myself in for!"
        $ audrey.set_fiance()
        $ cassidy.set_fiance()
    elif audrey.love >= 195 and cassidy.love < 195:
        audrey.say "Aww..."
        audrey.say "How can I say no to a face like that!"
        show audrey joke
        audrey.say "Seriously, [hero.name] - you look like a kicked puppy!"
        cassidy.say "You have to be kidding!"
        cassidy.say "I can't get married."
        show cassidy annoyed
        cassidy.say "I'm too young and pretty!"
        "I start to get to my feet."
        "At the same time trying to appeal to Cassidy."
        "But Audrey beats me to it."
        audrey.say "Ah, forget about her, [hero.name]."
        show audrey happy
        audrey.say "You need a real woman as your wife."
        audrey.say "Not some spoilt little brat!"
        "Cassidy's face darkens at this."
        "And for a moment I think she's going to argue."
        "But then she turns her back on us and storms away."
        hide cassidy
        show audrey at center with move
        "At the same time, Audrey holds up her hand."
        "All I can think to do is slide the ring onto her finger."
        "As my head is still spinning from what just happened."
        $ audrey.set_fiance()
        $ cassidy.love -= 25
        $ cassidy.sub -= 25
    elif audrey.love < 195 and cassidy.love >= 195:
        audrey.say "Fuck off, [hero.name]!"
        show audrey frown
        audrey.say "I mean, you're kidding - right?"
        cassidy.say "Don't be mean, Audrey!"
        cassidy.say "Yes, [hero.name]!"
        show cassidy happy
        cassidy.say "Of course I want to marry you."
        "I start to get to my feet."
        "At the same time trying to appeal to Audrey."
        "But Cassidy beats me to it."
        cassidy.say "Ah, forget about her, [hero.name]."
        cassidy.say "You need someone that cares for you as your wife."
        cassidy.say "Not that spiteful bitch!"
        "Audrey's face darkens at this."
        "And for a moment I think she's going to argue."
        "But then she turns her back on us and storms away."
        hide audrey
        show cassidy at center with move
        "At the same time, Cassidy holds up her hand."
        "All I can think to do is slide the ring onto her finger."
        "As my head is still spinning from what just happened."
        $ cassidy.set_fiance()
        $ audrey.love -= 25
        $ audrey.sub -= 25
    elif audrey.love < 195 and cassidy.love < 195:
        "I'm almost wincing as the girls open their mouths to speak."
        "Because part of me is sure that they're going to turn me down."
        audrey.say "Fuck off, [hero.name]!"
        show audrey frown
        audrey.say "I mean, you're kidding - right?"
        cassidy.say "You have to be!"
        show cassidy angry
        cassidy.say "I can't get married."
        cassidy.say "I'm too young and pretty!"
        "Shoving the rings back into my pocket, I slowly get up."
        mike.say "Erm..."
        mike.say "Yeah, I kinda was!"
        show audrey mock
        "Audrey lets out a peal of laughter and shakes her head."
        "But Cassidy looks a little more concerned for me."
        show cassidy annoyed
        cassidy.say "Oh dear..."
        audrey.say "Don't sweat it, Cassidy."
        show audrey annoyed
        audrey.say "He'll get over it."
        audrey.say "Won't you?"
        "Unable to do anything else, I shrug and nod."
        mike.say "I...I guess so."
        $ audrey.love -= 25
        $ audrey.sub -= 25
        $ cassidy.love -= 25
        $ cassidy.sub -= 25
    return

label audrey_palla_propose_male:
    "Being with Audrey and Palla at the same time is kind of a challenge."
    "They're both girls that know exactly what they want and how to get it."
    "But while they have a lot in common, they're also very different too."
    "Like, Palla's a total poser, someone that loves to have all the attention."
    "And that's because she wants to show off her latest outfit to the world."
    "Audrey wants the attention too, but she's not interested in making a fashion statement."
    "Instead she thrives on the feeling she gets from causing a scene or provoking a reaction."
    "I often feel like I'm juggling with the pair of them."
    "Trying to keep them both happy at the same time."
    "And always in danger of messing up in some way or another."
    "I feel like I need something to change the game up a little."
    "But I think I might have the very thing."
    "All I need is two rings and the right moment..."
    show palla casual annoyed at left5
    palla.say "Erm, Audrey..."
    palla.say "Like, what are you looking at?"
    show audrey casual annoyed at right5
    audrey.say "Why don't you tell me, Palla?"
    audrey.say "You're the one that had the front to wear it!"
    palla.say "Why you..."
    show palla angry
    palla.say "[hero.name], what are you doing?"
    audrey.say "Huh?"
    show audrey surprised
    audrey.say "Oh yeah - what in the hell are you doing?"
    "I reach into my pocket and pull out the rings."
    "Then I hold them up, hoping that it's enough of an explanation."
    show audrey awkward
    audrey.say "Wait a minute..."
    audrey.say "Are those..."
    show palla normal
    palla.say "Engagement rings!"
    palla.say "Stylish, fashionable engagement rings!"
    "I hope the smile on my face is a confident one."
    "Because I have the worst case of butterflies in my stomach right now!"
    mike.say "Audrey..."
    show audrey normal
    mike.say "Palla..."
    show palla normal
    mike.say "Will you marry me?"
    "I feel like I'm holding my breath as I wait for an answer."
    "And I'm worried that I'll pass out before I get one!"
    if audrey.love >= 195 and palla.love >= 195:
        "Audrey and Palla share a wry smile with each other."
        "And in that moment they remind me of smug, superior cats."
        "But when they both nod a few seconds later, I feel a surge of relief."
        audrey.say "Wow!"
        audrey.say "Look at you with the surprise question!"
        show audrey flirt
        audrey.say "Yeah, what the hell - I'll marry you."
        audrey.say "Because who else would?"
        palla.say "Me too, [hero.name]."
        palla.say "You're not the most stylish guy in the world."
        show palla happy
        palla.say "But you clean up pretty nicely!"
        "I don't know if I'm reeling from them both saying yes."
        "Or else from the back-handed compliments."
        "But I press ahead regardless."
        "Because girls like these could always change their minds."
        "I slip the rings onto their fingers and stand up."
        show audrey happy
        "But for once Audrey and Palla seem to be lost for words."
        "And they both just stand there, admiring their rings in silence."
        $ audrey.set_fiance()
        $ palla.set_fiance()
    elif audrey.love >= 195 and palla.love < 195:
        "Audrey's the one that manages to speak up first."
        audrey.say "Wow!"
        audrey.say "Look at you with the surprise question!"
        show audrey flirt
        audrey.say "Yeah, what the hell - I'll marry you."
        audrey.say "Because who else would?"
        "But then I see Palla shaking her head."
        palla.say "I can't be tied down to a relationship, [hero.name]."
        show palla angry
        palla.say "I have a career and a life of my own."
        palla.say "I'm not supposed to be someone's wife!"
        "Audrey snorts and shakes her head."
        "Then she steps over and pulls me to my feet."
        audrey.say "Forget her, [hero.name]!"
        show audrey happy
        audrey.say "Looks like it's just you and me."
        "Palla looks like she's about to argue."
        "But then she shakes her head and turns on her heel."
        hide palla
        "Then she walks away, leaving me to slide the ring onto Audrey's finger."
        $ audrey.set_fiance()
        $ palla.love -= 25
        $ palla.sub -= 25
    elif audrey.love < 195 and palla.love >= 195:
        "Palla's the one that manages to speak up first."
        palla.say "Yeah, [hero.name] - I'll marry you."
        show palla happy
        palla.say "You're not the most stylish guy in the world."
        palla.say "But you clean up pretty nicely!"
        "But then I see Audrey shaking her head."
        audrey.say "Erm...no!"
        show audrey annoyed
        audrey.say "I don't think so."
        audrey.say "This whole thing here, it's fun."
        audrey.say "But it's not what I want to do with the rest of my life."
        "Palla snorts and shakes her head."
        "Then she steps over and pulls me to my feet."
        palla.say "Forget her, [hero.name]!"
        show palla happy
        palla.say "Looks like it's just you and me."
        "Audrey looks like she's about to argue."
        "But then she shakes her head and turns on her heel."
        hide audrey
        "Then she walks away, leaving me to slide the ring onto Palla's finger."
        $ palla.set_fiance()
        $ audrey.love -= 25
        $ audrey.sub -= 25
    elif audrey.love < 195 and palla.love < 195:
        "Audrey and Palla look each other in the eye."
        "And then they shake their heads as one."
        audrey.say "Erm...no!"
        show audrey annoyed
        audrey.say "I don't think so."
        audrey.say "This whole thing here, it's fun."
        audrey.say "But it's not what I want to do with the rest of my life."
        palla.say "I can't be tied down to a relationship, [hero.name]."
        show palla angry
        palla.say "I have a career and a life of my own."
        palla.say "I'm not supposed to be someone's wife!"
        "Feeling more than a little crushed, I put the rings away."
        "And then I get slowly to my feet."
        mike.say "Oh..."
        mike.say "Okay..."
        mike.say "I just thought it would be nice, you know?"
        audrey.say "Oh for fuck's sake, [hero.name]."
        audrey.say "Don't start sulking!"
        palla.say "Yeah..."
        palla.say "That's really unattractive!"
        "I nod, forcing a smile onto my face."
        "And all the time I'm trying to hide my disappointment."
        $ audrey.love -= 25
        $ audrey.sub -= 25
        $ palla.love -= 25
        $ palla.sub -= 25
    return

label cassidy_palla_propose_male:
    "Dating one girl that could be called high-maintenance is a pretty daunting prospect."
    "So imagine what it's like when you're in a relationship with two of them at the same time."
    "Being with Cassidy and Palla can be like tiptoeing across a minefield."
    "Juggling the affections of a rich daddy's girl and a haughty devotee of high-fashion."
    "It's kind of like riding around on the back of a tiger, you know?"
    "You look like the king of the world until you have to get off it's back safely!"
    "All that said, I just can't imagine my life without the pair of them."
    "So there's only one thing that I can think to do in order to make that happen."
    "I save up the money."
    "I pick out two rings that will come up to their exacting standards."
    "And then I wait for the perfect moment to present itself in which to pop the question."
    "But when it comes, I'm almost too nervous to do it."
    "I go down on one knee slowly."
    "And it almost looks like I'm tripping over in slow motion."
    show palla casual angry at left5
    palla.say "[hero.name]!"
    palla.say "What are you doing?"
    show cassidy casual angry at right5
    cassidy.say "Huh?"
    cassidy.say "Oh wow!"
    cassidy.say "Are you okay down there?"
    "I force a grin onto my face as I look up at them."
    "And at the same time I reach for the rings in my pocket."
    mike.say "Palla..."
    show palla normal
    mike.say "Cassidy..."
    show cassidy normal
    mike.say "I...I have something to ask you..."
    "I hold up the rings, making sure they're plainly visible."
    "And I watch as looks of surprise spread across their faces."
    "Which gives me confidence, as that's a rare thing to see."
    palla.say "Oh..."
    show palla blush
    palla.say "Oh my!"
    cassidy.say "[hero.name]..."
    show cassidy normal
    cassidy.say "Are you..."
    "I nod and hold the rings up higher."
    mike.say "Yeah, I guess I am!"
    mike.say "So what about it?"
    mike.say "Will you marry me?"
    "Palla and Cassidy exchange a wide-eyed glance."
    show palla normal
    "And then I get my answer."
    if cassidy.love >= 195 and palla.love >= 195:
        "I think this is the first time I've ever seen the girls stunned into silence."
        "They're staring into each other's eyes for so long I'm sure it must be bad news."
        "But then they smile and begin to nod."
        palla.say "Of course I'll marry you, [hero.name]."
        show palla blush
        palla.say "Did you think I'd say no?"
        cassidy.say "Me too, [hero.name]!"
        show cassidy happy
        cassidy.say "I REALLY want you to be my husband!"
        "Together they thrust their hands out towards me."
        "And I hurry to push the rings onto their fingers."
        "I feel like I'm dreaming all of this."
        "Like any moment I'll wake up and it won't be real."
        "As I get up, I can't help shaking my head."
        mike.say "Wow..."
        mike.say "You said yes!"
        mike.say "Both of you said yes!"
        "Palla and Cassidy share a knowing laugh."
        cassidy.say "Of course we did, [hero.name]!"
        show cassidy happy
        cassidy.say "You're the only man who treats me more like a princess than my Daddy."
        cassidy.say "And when we're together, you make me feel like a queen too!"
        palla.say "Yeah, that's true."
        show palla happy
        palla.say "We look good together too."
        palla.say "Like, you dress far better now, thanks to me."
        palla.say "But you still don't look good enough to take the attention off of me."
        mike.say "Erm..."
        mike.say "Thanks, Palla...I think..."
        "I smile and soon find myself forgetting the back-handed compliment."
        "And all I can think about is the fact that they said yes."
        "It's actually happening - we're getting married!"
        $ cassidy.set_fiance()
        $ palla.set_fiance()
    elif cassidy.love >= 195 and palla.love < 195:
        "Palla shakes her head and lets out a peal of laughter."
        palla.say "Oh come on!"
        show palla angry
        palla.say "You can't be serious?"
        palla.say "Can you?"
        mike.say "Erm..."
        mike.say "I kinda was!"
        "Before I can say another word, Cassidy cuts jumps in."
        cassidy.say "What are you talking about, Palla?!?"
        show cassidy angry
        cassidy.say "I want to marry you, [hero.name]!"
        show cassidy happy
        cassidy.say "You're the only man who treats me more like a princess than my Daddy."
        cassidy.say "And when we're together, you make me feel like a queen too!"
        "I give Palla a pleading look, hoping that she'll change her mind."
        "But instead she turns her back on me and starts walking away."
        hide palla
        show cassidy at center with move
        "Which leaves me getting to my feet and staring after her."
        "Cassidy distracts me by almost throwing herself into my arms a moment later."
        "She holds up her hand, and I hastily slide the ring onto her finger."
        "I have no idea where I go with Palla from this point on."
        "And for the moment, all I can do is hold Cassidy close."
        $ cassidy.set_fiance()
        $ palla.love -= 25
        $ palla.sub -= 25
    elif cassidy.love < 195 and palla.love >= 195:
        "Cassidy wrinkles her nose and shakes her head."
        cassidy.say "[hero.name], I'm too young to get married!"
        show cassidy angry
        cassidy.say "That's something old people would do."
        cassidy.say "Like my parents!"
        cassidy.say "You can't be serious?"
        cassidy.say "Can you?"
        mike.say "Erm..."
        mike.say "I kinda was!"
        "Before I can say another word, Palla cuts jumps in."
        palla.say "Well I do want to marry you, [hero.name]."
        show palla happy
        palla.say "We look good together."
        palla.say "Like, you dress far better now, thanks to me."
        palla.say "But you still don't look good enough to take the attention off of me."
        mike.say "Erm..."
        mike.say "Thanks, Palla...I think..."
        "I smile at the back-handed compliment."
        "I give Cassidy a pleading look, hoping that she'll change her mind."
        "But instead she turns her back on me and starts walking away."
        hide cassidy
        show palla at center with move
        "Which leaves me getting to my feet and staring after her."
        "Palla distracts me by wrapping her arms around me a moment later."
        "She holds up her hand, and I hastily slide the ring onto her finger."
        "I have no idea where I go with Cassidy from this point on."
        "And for the moment, all I can do is hold Palla close."
        $ palla.set_fiance()
        $ cassidy.love -= 25
        $ cassidy.sub -= 25
    elif cassidy.love < 195 and palla.love < 195:
        "As one, the girls shake their heads and laugh."
        show cassidy happy
        show palla happy
        "Which really isn't the kind of answer I wanted."
        "When she sees my disappointment, Cassidy seems a little concerned."
        "But Palla just rolls her eyes and lets out a snort of derision."
        palla.say "Oh come on!"
        show palla angry
        palla.say "You can't be serious?"
        palla.say "Can you?"
        mike.say "Erm..."
        mike.say "I kinda was!"
        cassidy.say "[hero.name], I'm too young to get married!"
        show cassidy angry
        cassidy.say "That's something old people would do."
        cassidy.say "Like my parents!"
        "I get slowly to my feet."
        "And I put the rings away as I do so."
        mike.say "I just thought we were getting on so well, you know?"
        mike.say "Like we could make it official?"
        "Palla and Cassidy shake their head again."
        mike.say "So I guess that's a no?"
        "This time they nod their heads."
        "And I get the feeling that the discussion is over."
        $ cassidy.love -= 25
        $ cassidy.sub -= 25
        $ palla.love -= 25
        $ palla.sub -= 25
    return

label audrey_cassidy_palla_male_ending:

    if renpy.has_label("bitchy_harem_achievement_6") and not game.flags.cheat:
        call bitchy_harem_achievement_6 from _call_bitchy_harem_achievement_6
    $ game.hour = 16
    $ game.room = "church"
    scene bg church wedding
    "I know what most guys are going to be thinking - I'm one lucky bastard, right?"
    "I mean, I'm dating Audrey, Cassidy and Palla all at once and they're loving it."
    "And what's even better, we're all about to tie the knot."
    "But sometimes I feel like I'm constantly spinning plates with the three of them."
    "Every one of them is pretty high-maintenance, demanding to be kept happy."
    "And as the only guy in the relationship, that duty tends to fall on me."
    "Oh, and then imagine all of that with a wedding on top!"
    "Every single aspect of the wedding has to be perfect."
    "And it has to satisfy three very different Bridezilla's too!"
    "So by the time I'm actually standing at the altar, my head is spinning."
    "In fact, I'm so amazed that we actually made it here I almost think I'm dreaming!"
    "I take a look back over my shoulder to ground myself in reality."
    "And I see my own friends and family sitting behind me."
    "They're about as numerous and typical as Audrey's guests."
    "But I can easily pick out Cassidy's guests."
    if not game.flags.dwaynedead:
        "I see Dwayne, her father and my own boss out there."
        "And beside him is Cherie, his wife and Cassidy's mother - who looks as hot as ever!"
    else:
        "I see Cherie, her mother - who looks as hot as ever!"
    "But it's Palla's guests that really stand out."
    "Fucking hell - they look like the crowd at Paris Fashion Week!"
    "And they're already making me feel shabby in comparison."
    "Unconsciously I start to smooth out my clothes."
    "But then the music begins to play and I snap out of it."
    show audrey wedding happy at left
    show cassidy wedding happy
    show palla wedding happy at right
    with dissolve
    "I watch as Audrey, Cassidy and Palla stride into the chapel."
    "And I can't help smiling as they walk three abreast too."
    "I should have known it."
    "None of them would ever let the others walk in front of them!"
    "I look at each of my brides in turn as they walk down the aisle."
    "There's Audrey, as wicked and spikey as the day I first met her at work."
    "And the dress she's wearing reminding me of all the physical charms she possesses too."
    if audrey.is_visibly_pregnant:
        "She even seem to be wearing her pregnant belly as a challenge."
        "Like she just doesn't care what anybody else thinks of her."
    "Cassidy looks more like a princess than ever right now."
    "Like she was born to be the centre of attention."
    if cassidy.is_visibly_pregnant:
        "And even the fact that she's visibly pregnant doesn't seem to bother her."
        "Instead she's taking it in her stride and smiling happily."
    "Of course Palla looks like she's striding down a catwalk."
    "Every step she takes oozes with confidence and her dress is sheer perfection."
    if palla.is_visibly_pregnant:
        "It's also cut in just such a way to accommodate her pregnant belly."
        "Not so as to hide it, just to make it less than instantly obvious."
    "Once they reach the altar, all we have time to do is smile at each other."
    "And that's because we're running on a tight schedule here."
    "After all, we are dealing with three brides!"
    "Priest" "Dearly beloved..."
    show audrey normal
    show cassidy normal
    show palla normal
    "Priest" "We are gathered here today..."
    "Priest" "To join these four people in the bonds of holy matrimony."
    "We've walked through the ceremony so many times I could do it backwards."
    "And all four of us instantly respond to the priest's opening words."
    "The ceremony seems to fly by, until we get to the vows."
    "Priest" "Do you, Audrey..."
    "Priest" "Take these people..."
    "Priest" "To be your lawful, wedded partners?"
    show audrey happy
    audrey.say "I do."
    "Priest" "Do you, Cassidy..."
    "Priest" "Take these people..."
    "Priest" "To be your lawful, wedded partners?"
    show cassidy happy
    cassidy.say "I do."
    "Priest" "And do you, Palla..."
    "Priest" "Take these people..."
    "Priest" "To be your lawful, wedded partners?"
    show palla happy
    palla.say "I do."
    "Priest" "And finally..."
    "Priest" "Do you, [hero.name]..."
    "Priest" "Take these people..."
    "Priest" "To be your lawful, wedded partners?"
    mike.say "I do."
    "Priest" "Phew..."
    "Priest" "I hereby declare you married."
    "Priest" "If anyone here present knows of any reason these people may not be married..."
    "Priest" "Speak now, or forever hold your peace!"
    "There's the customary pause and laughter from the assembled guests."
    "But part of me is actually worried someone might speak up."
    if not game.flags.dwaynedead:
        "And I feel my gaze being pulled towards where Dwayne is sitting."
        "Luckily for me though, he seems to be keeping his mouth shut."
    "Priest" "Very good."
    "Priest" "You may exchange kisses with your partners."
    show audrey wedding normal blush zorder 2 at center, zoomAt(1.5, (340, 1040))
    show cassidy wedding normal blush zorder 1 at center, zoomAt(1.5, (640, 1040))
    show palla wedding blush zorder 3 at center, zoomAt(1.5, (940, 1040))
    "We do as the priest says, embracing each other warmly."
    "For the moment, everyone seems happy and on the same page."
    "God knows how long it's going to last for."
    "But I'm going to enjoy every moment for as long as it does."

    scene bitchy harem ending
    show bitchy harem ending audrey cassidy palla
    with fade
    palla.say "There's really no need for you two to be here."
    palla.say "I think that I can speak for everyone involved."
    cassidy.say "Oh really, Palla?"
    cassidy.say "Just because you can handle a catwalk, doesn't mean you can handle this!"
    audrey.say "You think we should just leave it to you instead, Cassidy?"
    audrey.say "Because I don't!"
    cassidy.say "Okay, okay..."
    cassidy.say "Time out, guys!"
    cassidy.say "You wouldn't be doing this if [hero.name] were here..."
    palla.say "Urgh..."
    palla.say "I hate to admit it, Audrey."
    palla.say "But Cassidy's right."
    audrey.say "I know, I know..."
    audrey.say "It bugs the hell out of me too."
    audrey.say "How does he even do that?!?"
    cassidy.say "Isn't it obvious?"
    cassidy.say "He brings out the best in all of us!"
    cassidy.say "He's the glue that binds us all together!"
    audrey.say "Eww!"
    palla.say "She's right again, Audrey."
    palla.say "All I used to care about was making it as a model."
    palla.say "But with [hero.name] in my life, I see there's more to it than that."
    cassidy.say "Me too - he makes me think about all of you guys."
    cassidy.say "Like we're a real family!"
    audrey.say "Oh god..."
    audrey.say "I've become everything I used to hate!"
    audrey.say "I'm in a loving relationship, and it just gets better all the time!"
    cassidy.say "Ha, ha!"
    cassidy.say "You know that you love us, Audrey!"
    palla.say "Yeah!"
    palla.say "We're all stuck with each other now!"
    if audrey.is_visibly_pregnant or audrey.flags.mikeBabies >= 1:
        audrey.say "Well, I guess [hero.name] is a good father."
        audrey.say "And little Lee adores his daddy."
    if cassidy.is_visibly_pregnant or cassidy.flags.mikeBabies >= 1:
        cassidy.say "Sophia is so precious to [hero.name]."
        cassidy.say "He's such a good daddy to me..."
        cassidy.say "To them - I mean to them!"
    if palla.is_visibly_pregnant or palla.flags.mikeBabies >= 1:
        palla.say "I certainly wouldn't have had Mary without [hero.name]."
        palla.say "And she means so much more to me than my career ever did."
    cassidy.say "And let's face it, girls..."
    cassidy.say "[hero.name] needs us too!"
    audrey.say "Oh, you got that right!"
    audrey.say "He'd be a total mess without us to keep him on his toes."
    cassidy.say "Totally clueless, totally sloppy."
    cassidy.say "Sometimes I even have to pick out his clothes for him!"
    audrey.say "Let's face it, guys..."
    audrey.say "[hero.name]'s a pretty great guy."
    audrey.say "But he's lucky to have the three of us."
    audrey.say "Because we know what's good for him better than he does himself!"
    $ game.set_new_game_plus()
    $ renpy.full_restart()

label audrey_palla_male_ending:

    if renpy.has_label("bitchy_harem_achievement_3") and not game.flags.cheat:
        call bitchy_harem_achievement_3 from _call_bitchy_harem_achievement_3
    $ game.hour = 16
    $ game.room = "church"
    scene bg church wedding
    "It's weird how you can have two elements that are totally safe on their own."
    "But put them together, and you're going to have them blow up in your face!"
    "And that pretty much sums up Audrey and Palla alike!"
    "No, no...wait a minute, that's not right."
    "They're both pretty combustible in their own right!"
    "It's more like putting them together turns dynamite into an atomic bomb!"
    "Part of me never thought we'd make it this far."
    "That I'd actually be standing at the altar, waiting for them both."
    "And believe me, there was a lot of planning went into this."
    "Everything had to be just so for a girl as exacting as Palla."
    "And Audrey was there to snipe and provoke every step of the way too!"
    "But now the big days here, and I keep looking back over my shoulder."
    "I recognise my own friends and family sitting in the chapel."
    "There's a bunch of familiar faces from work too."
    "I guess all of the painfully fashionable people must be here for Palla."
    "As they all look like they take their dress-sense very seriously!"
    "I'm about to study one or two of them more closely."
    "But that's the moment at which the music begins to play."
    "And all heads turn towards the back of the chapel."
    show audrey wedding happy at left5
    "There's Audrey, as wicked and spikey as the day I first met her at work."
    "And the dress she's wearing reminding me of all the physical charms she possesses too."
    if audrey.is_visibly_pregnant:
        "She even seem to be wearing her pregnant belly as a challenge."
        "Like she just doesn't care what anybody else thinks of her."
    "Of course Palla looks like she's striding down a catwalk."
    show palla wedding happy at right5
    "Every step she takes oozes with confidence and her dress is sheer perfection."
    if palla.is_visibly_pregnant:
        "It's also cut in just such a way to accommodate her pregnant belly."
        "Not so as to hide it, just to make it less than instantly obvious."
    "Once they reach the altar, all we have time to do is smile at each other."
    "And that's because we're running on a tight schedule here."
    "After all, we are dealing with two brides!"
    "Priest" "Dearly beloved..."
    show audrey normal
    show palla normal
    "Priest" "We are gathered here today..."
    "Priest" "To join these three people in the bonds of holy matrimony."
    "We've walked through the ceremony so many times I could do it backwards."
    "And all three of us instantly respond to the priest's opening words."
    "The ceremony seems to fly by, until we get to the vows."
    "Priest" "Do you, Audrey..."
    "Priest" "Take these people..."
    "Priest" "To be your lawful, wedded partners?"
    audrey.say "I do."
    show audrey happy
    "Priest" "And do you, Palla..."
    "Priest" "Take these people..."
    "Priest" "To be your lawful, wedded partners?"
    palla.say "I do."
    show palla happy
    "Priest" "And finally..."
    "Priest" "Do you, [hero.name]..."
    "Priest" "Take these people..."
    "Priest" "To be your lawful, wedded partners?"
    mike.say "I do."
    "Priest" "I hereby declare you married."
    "Priest" "If anyone here present knows of any reason these people may not be married..."
    "Priest" "Speak now, or forever hold your peace!"
    "There's the customary pause and laughter from the assembled guests."
    "But part of me is actually worried someone might speak up."
    "Luckily for me though, everyone keeps their mouths shut."
    "Priest" "Very good."
    "Priest" "You may exchange kisses with your partners."
    show audrey wedding normal blush at center, zoomAt(1.5, (440, 1040))
    show palla wedding blush at center, zoomAt(1.5, (840, 1040))
    "We do as the priest says, embracing each other warmly."
    "For the moment, everyone seems happy and on the same page."
    "God knows how long it's going to last for."
    "But I'm going to enjoy every moment for as long as it does."

    scene bitchy harem ending
    show bitchy harem ending audrey palla
    with fade
    audrey.say "Nah, no need for you to get involved in this one, Palla."
    audrey.say "Just let me handle it, okay?"
    palla.say "What are you talking about, Audrey?"
    palla.say "This is supposed to be us talking about what it's like living with [hero.name]!"
    audrey.say "Yeah, I know..."
    audrey.say "But I'm the one that does most of the talking, right?"
    audrey.say "Whereas you're kind of a professional mannequin, aren't you?"
    audrey.say "You know, like a dummy?"
    palla.say "HEY!"
    palla.say "You promised you'd stop calling me that!"
    audrey.say "Whatever, Palla."
    audrey.say "But you've got to admit, what with you and [hero.name]..."
    audrey.say "I'm kinda the brains of the operation!"
    palla.say "More like the ass, Audrey!"
    audrey.say "Ouch!"
    audrey.say "Saucer of milk for you, Palla!"
    palla.say "Urgh..."
    palla.say "You're always like this when [hero.name]'s not here!"
    audrey.say "Speak for yourself!"
    palla.say "No, I mean it Audrey."
    palla.say "He kind of keeps us both in line - but in a good way!"
    audrey.say "Yeah, yeah..."
    audrey.say "You've got a point."
    audrey.say "I guess I do feel more chill when he's around."
    palla.say "It's like I said."
    palla.say "And I don't like admitting this either."
    palla.say "But he kind of makes us better."
    audrey.say "Yeah..."
    audrey.say "It's so annoying."
    audrey.say "I hate that about him!"
    palla.say "I definitely couldn't have imagined getting married before I met him."
    audrey.say "Nah, me neither."
    audrey.say "Especially not to someone like you!"
    palla.say "Thanks, Audrey - the feeling's mutual!"
    palla.say "But somehow he manages to make us a family."
    if audrey.is_visibly_pregnant or audrey.flags.mikeBabies >= 1:
        audrey.say "Well, I guess [hero.name] is a good father."
        audrey.say "And little Tommy adores his daddy."
    if palla.is_visibly_pregnant or palla.flags.mikeBabies >= 1:
        palla.say "I certainly wouldn't have had Mary without [hero.name]."
        palla.say "And she means so much more to me than my career ever did."
    if not audrey.is_visibly_pregnant and not audrey.flags.mikeBabies and not palla.is_visibly_pregnant and not palla.flags.mikeBabies:
        audrey.say "Palla..."
        audrey.say "Do you..."
        palla.say "Spit it out, Audrey!"
        audrey.say "Do you kind of think about having kids with him?"
        palla.say "You too, huh?"
        palla.say "Yeah, Audrey - all the time!"
    audrey.say "So we're agreed?"
    audrey.say "[hero.name]'s like the perfect husband."
    audrey.say "And he's made the pair of us disgustingly happy."
    palla.say "On hundred percent."
    palla.say "And one more thing - even more important."
    audrey.say "Yeah?"
    palla.say "Under no circumstances must he find that out."
    palla.say "Agreed?"
    audrey.say "Agreed!"
    $ game.set_new_game_plus()
    $ renpy.full_restart()
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
