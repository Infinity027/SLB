init python:
    InteractActivity(**{
    "name": "fuck_minami",
    "display_name": "Fuck",
    "label": "ACTIVE_GIRL_fuck_ROOM",
    "conditions": [
        IsTimeOfDay("evening"),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home"),
            HasStamina(),
            ),
        PersonTarget(minami,
            IsActive(),
            MinStat("love", 150),
            MinStat("sexperience", 2),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })

    InteractActivity(**{
    "name": "fuck_minami_beach",
    "display_name": "Fuck",
    "label": "ACTIVE_GIRL_fuck_ROOM",
    "conditions": [
        IsHour(14, 18),
        HeroTarget(
            IsGender("male"),
            IsRoom("beach", "date_beach", "date_nudistbeach"),
            HasStamina(),
            ),
        PersonTarget(minami,
            IsActive(),
            MinStat("love", 150),
            MinStat("sexperience", 2),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })

    Event(**{
    "name": "minami_hottub_sex_male",
    "label": "minami_hottub_sex_male",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("date_hot_tub_home")),
        PersonTarget(minami,
            OnDate(),
            MinStat("love", 100),
            MinStat("sexperience", 1),
            ),
        ],
    "priority": 500,
    "do_once": False,
    "once_day": True,
    "duration": 1,
    })

label minami_fuck_date_nudistbeach:
label minami_fuck_beach:
label minami_fuck_date_beach:
    $ game.play_music("music/roa_music/new_days.ogg")
    show minami
    "I love the chance to leave all my worries behind and just spend a couple of hours at the beach."
    "Somehow everything seems better when I'm there, the bad stuff smaller and the good stuff even better still."
    "But what makes it even more amazing is when I get to go to the beach with a really hot girl!"
    if game.room != "date_nudistbeach":
        "And right now, I can't imagine anything hotter than Minami!"
    else:
        "And right now, I can't imagine anything hotter than Minami in her swimsuit!"
    show minami b at left5 with ease
    "All we're supposed to be doing is soaking up some sun, and she's making that into genuine torture."
    "You see that's the only problem with coming to the beach along with a hot girl."
    show minami b at right4 with ease
    "They make it impossible for you to just kick back and relax."
    show minami a at center with ease
    "Literally all I can think about right now is Minami and how sexy she looks!"
    show minami happy b at center, zoomAt(1.5, (640, 1040)), top_to_bottom
    "I keep stealing glances at her whenever I think I can get away with it."
    "But I end up staring longer than I intend at her pert little breasts."
    "Then I eye up the cute curve of her tight stomach."
    "And my gaze lingers on just how good her butt looks today too!"
    "So in the end, she can't help but notice the attention I'm giving her."
    hide minami
    show minami hunt a at center, zoomAt(1.5, (640, 1040))
    with vpunch
    minami.say "Ah, big bro..."
    minami.say "Are you okay?"
    mike.say "Erm..."
    mike.say "Yeah, Minami..."
    mike.say "Why do you ask?"
    "I keep on trying to play dumb."
    "Even though I'm sure Minami can see right through me."
    show minami blush
    minami.say "It's just..."
    minami.say "Well...you keep staring at me all the time!"
    mike.say "I was?!?"
    mike.say "Oh...I'm sorry, Minami."
    if game.room == 'date_nudistbeach':
        mike.say "I was just admiring you, that's all!"
    else:
        mike.say "I was just admiring your swimsuit, that's all!"
        "Yeah, more like admiring everything that it doesn't cover up!"
        "It really leaves nothing to the imagination at all."
    show minami -close
    minami.say "Oh, thanks, big bro!"
    if not game.room == 'date_nudistbeach':
        minami.say "I'm glad that you like it."
        minami.say "I was worried you might think it was too..."
        minami.say "You know, too revealing!"
        mike.say "No way, Minami!"
        mike.say "I love how revealing it is!"
        "Way to go there, Mister Tactless!"
        "I shake my head desperately, trying to take it back."
        mike.say "I...I didn't mean it like that, Minami!"
        mike.say "I meant it...it complements your figure..."
        mike.say "I mean...it's very flattering!"
    "Minami giggles, clearly enjoying how tongue-tied she's making me."
    "She rolls onto her side, deliberately showing herself off even more."
    minami.say "Aww...that's so sweet, big bro!"
    if not game.room == 'date_nudistbeach':
        minami.say "I wore this for you - you know that?"
        minami.say "Because I thought you'd like it."
        minami.say "AND like to fuck me in it too..."
    hide minami
    show minami doggy beach
    with fade
    "Without another word, Minami gets onto her hands and knees."
    "My cock's hard before she's halfway done."
    "And I know that she can see the bulge in my shorts too!"
    minami.say "Come on, big bro - what are you waiting for?"
    minami.say "Nobody's around to see us."
    minami.say "I don't just want your eyes on me."
    minami.say "I want you inside of me too!"
    "Well, that does it for lying around, just relaxing on the beach!"
    if not game.room == 'date_nudistbeach':
        "Before I know it, I'm up and yanking off my shorts too."
    show minami doggy mike
    "Minami giggles and shakes her ass as I crawl over to her."
    "Looking back over her shoulder with a grin on her face."
    "That grin changes to a look of surprise a moment later."
    "Because I grab her by the buttocks and pull her backwards."
    show minami doggy inside closed
    "Minami squeals as I push myself forward at the same time."
    "As soon as my cock slips between her thighs, I can't help smiling."
    "She's already as slick as can be down there, like she's ready for me."
    "And that can only mean she was getting turned-on before we decided to fuck."
    "Minami must have been worked up by the way I was looking at her just now."
    "All of which means it's that much easier to push inside of her too."
    minami.say "Mmm..."
    minami.say "That's it, big bro..."
    minami.say "Just like that!"
    "I smile as I sink all the way into Minami."
    "Because I can feel her body echoing her words."
    "Minami's pussy is nice and tight, squeezing me the whole time."
    "But she's also yielding to me more with each passing second."
    "I want to make the sensation last as long as possible."
    "Yet I can also feel myself picking up speed too."
    "It's like my body won't listen to what me head wants."
    "Or, more honestly, like my cock is the part of me that's in charge right now!"
    "None of this seems to matter to Minami though."
    "As she nods her head desperately as I thrust in and out of her ever faster."
    "There's nothing to be done for it now, I'm already committed to the act."
    "So I resolve to get the most I can out of fucking Minami before it's over."
    "I still have hold of Minami's haunches, and I tighten my grip on them."
    "As I thrust forwards I also pull her backwards like I did to enter her."
    "But now it becomes something I do constantly, smacking my thighs against her ass."
    "Minami starts to cry out whenever our bodies slap together."
    "And the rest of the time she moans with pleasure too."
    "She's hardly having to move a muscle by now, as I'm doing all the work."
    "Her petite breasts are jiggling with the motion of her body."
    "And when she looks back over her shoulder, her eyes are glazed over."
    $ minami.love += 1
    show minami doggy ahegao
    minami.say "Ah...ah..."
    minami.say "Big bro..."
    minami.say "You're gonna make me cum!"
    "Minami's words turn into a helpless cry even as their prediction comes true."
    "I can feel every single twitch and twinge of the orgasm she's having."
    with hpunch
    "And the sensation is more than enough to ensure she takes me along with her!"
    with hpunch
    "Before she can come down again, I fill Minami's pussy with all that I have."
    with hpunch
    "Just like that she's right back where she started, cumming all over again!"
    "And I find that I have to hold her up as her arms and legs start to buckle."
    "I guide Minami down onto the ground, slipping out of her as I do so."
    "She sighs and twitches from the aftershocks of her orgasm."
    "But she eagerly nestles herself against me at the same time."
    "Neither of us feels the need to speak as we lie there together."
    "And maybe now we can just relax and do nothing other than soak up the sun."
    return

label minami_fuck_livingroom:
label minami_fuck_kitchen:
label minami_fuck_pool:
label minami_fuck_bedroom1:
label minami_fuck_bedroom2:
label minami_fuck_bedroom3:
label minami_fuck_bedroom4:
label minami_fuck_bedroom5:
label minami_fuck_bedroom6:
label minami_fuck_secondfloor:
label minami_fuck_house:
label minami_fuck_home:
    $ game.play_music("music/roa_music/new_days.ogg")
    show minami
    mike.say "Hey, wanna come and have fun in my bedroom?"
    minami.say "Sure."
    if Harem.find(minami, name='home'):
        call home_harem_fuck_choices ('minami') from _call_home_harem_fuck_choice
    else:
        call minami_fuck_date_male (called_from_date=False) from _call_minami_fuck_date_3
    return

label minami_fuck_date_male(location="hero", called_from_date=True):
    $ game.room = "bedroom1"
    $ game.play_music("music/roa_music/new_days.ogg")
    $ minami.flags.handcuffs = False
    show bg livingroom
    show minami


    call minami_fuck_date_intro_male (location, called_from_date) from _call_minami_fuck_date_intro_male


    call minami_dick_reactions from _call_minami_dick_reactions_3

    scene bg bedroom1
    show minami naked
    with fade


    call minami_fuck_date_foreplay_male from _call_minami_fuck_date_foreplay_male




    call minami_fuck_date_choices_male from _call_minami_fuck_date_choices_male

    $ minami.flags.handcuffs = False

    call handle_npc_leaving (minami, _return) from _call_handle_npc_leaving_15
    if _return:
        return


    hide minami
    call minami_sleep_date_fuck (location) from _call_minami_sleep_date_fuck
    return

label minami_fuck_date_intro_male(location="hero", called_from_date=True):
    $ intro = minami.flags.sexperience % 5
    if intro == 0:
        if called_from_date:
            "After the date is over and we make it back to the house, Minami never lets go of my hand as we let ourselves in and go down the stairs."
            "And there's never as much as the slightest hint of her making for the stairs that would lead to the attic and her bedroom."
        show bg bedroom1
        show minami
        with fade
        "Instead she leads me straight towards the door to my own bedroom, and I make no effort to resist as she does so."
        "Neither of us feels the need to say as much as a single word, both knowing what this means and what we want."
        "Minami simply looks back over her shoulder at me, grinning from ear to ear in anticipation."
        "Almost as soon as I close the door behind us, I glance round to see her stripping off her clothes."
        "She does this with that same exuberance and enthusiasm that's always been one of her most defining qualities."
        show minami naked with dissolve
        "So before I've even had the chance to cross the room and begin to take off my own clothes, Minami's already naked."
        minami.say "Come on, slow coach!"
        minami.say "What are you waiting for?!?"
        show minami hunt at center, zoomAt(1.5, (640, 1040)) with vpunch
        "As if to underline the statement, Minami clambers onto the bed before me."
        "She makes sure that I get a good, long look at her as she does so too."
        "Shaking her petite breasts and then wiggling her ass to show off what I'm missing out on."
        "I can't help smiling and shaking my head as I get undressed at her command."
        "All of that manic, sexual energy that used to go into getting me hot under the collar is still there."
        "But now that our relationship's evolved, it's devoted to making me want her all the more."
        "Don't misunderstand - that same energy that used to make me think I was losing my mind still makes me go crazy."
        "The difference is that now I can channel all of it into giving Minami what she wants."
        "Or to be more precise - what we both want."
        mike.say "You might want to save your breath while you still can, Minami."
        mike.say "Because as soon as I get my hands on you, I'm gonna take it away!"
        hide minami
        show minami naked happy
        "Minami lets out a burst of giggles, clapping her hands together in anticipation."
        minami.say "Big talk, big bro!"
        minami.say "You better be able to deliver..."
        "By the time she says this, I'm already climbing onto the bed after her."
        "I don't bother to think up another witty comeback."
        call minami_dick_reactions from _call_minami_dick_reactions
    elif intro == 1:
        if called_from_date:
            show bg livingroom
            show minami
            with fade
            "There's just something about spending time with Minami, something that makes me almost giddy inside."
            "I mean, she's always been a pretty fun person to be around, when we were growing up together."
            "She could be annoying, sure - but we were just a couple of kids back then."
            "And yeah, I know that things have changed now we've admitted that we're something more to each other than before."
            "But she still makes me feel alive and excited at the prospect of simply being with her."
            "It's like she makes everything new, like we're discovering a whole new world together."
        call minami_fuck_date_oral_intro from _call_minami_fuck_date_oral_intro
        call minami_fuck_date_oral from _call_minami_fuck_date_oral
        $ minami_cunni = True
    elif intro == 2:
        show bg bedroom1
        show minami hunt
        with fade
        "I know that I'm in for a treat as soon as Minami and I walk in through the front door."
        "It's pretty obvious what she has in mind too, as Minami's got a room of her own."
        "But she steers me straight towards the door to my room, not stopping for a moment."
        "Once we're inside, there's no reason to pretend what we're up to anymore."
        "There's only the two of us in here, and we both know what we want right now!"
        minami.say "Oh, big bro!"
        minami.say "I thought we'd never make it back here!"
        minami.say "I've wanted you SO bad all night!"
        show minami kiss with fade
        $ minami.flags.kiss += 1
        "Minami literally pounces on me a moment later, leaping into my arms."
        "I only just manage to catch her, staggering across the room as I do so."
        "Minami wraps her legs and arms around me, clinging to me tightly."
        "And she starts to kiss me at the same time, all around my face and on my neck."
        "When her lips aren't pressed against my skin, she sighs into my ear."
        minami.say "Ah..."
        minami.say "You HAVE to fuck me, big bro!"
        minami.say "All I can think about is having you inside of me!"
    elif intro == 3:
        show bg bedroom1
        "There's no mad, passionate rush to tear off each other's clothes as Minami and I slip quietly into my bedroom."
        "All the same, I can almost feel the electricity between us right now, hear it in the prevailing silence."
        "So much of what we're about to do might seem wrong on the surface of things, to be a taboo."
        "But I can say with complete certainty that I don't care what anyone else might happen to think."
        "I know that I want this, more than anything else."
        show minami hunt
        "And the look on Minami's face tells me she feels the same way too."
        "Slowly and with infinite care, we begin to undress each other."
        "And with every piece of clothing that's dropped to the floor, I become more sure of myself."
        show minami a naked blush with dissolve
        "Once we're naked, we simply stand there for a moment, eyes devouring the sight before us."
        call minami_dick_reactions from _call_minami_dick_reactions_1
        "In the end, it's Minami that steps forward first, pressing herself gently against me."
        "Her body is so soft and petite, feeling warm and inviting as she wraps her arms around my waist."
        "Well, at least that's what she does with one of them."
        "I feel her free hand begin to stroke my already stirring cock, and I can't help gasping at the sensation."
        "Minami giggles at this, a delightful little trill of pure and infectious delight."
    else:
        if called_from_date:
            scene bg house
            show minami happy
            with fade
            "Minami hasn't stopped giggling since we piled into the taxi home after our date tonight."
            "At first I thought she was just laughing at the quality of the jokes I was coming out with."
            "Because I'm a funny guy, right?"
            "But she keeps on giggling and chuckling to herself, even when I've run out of material."
        scene bg bedroom1
        show minami hunt
        with fade
        if called_from_date:
            "And she only stops once we're finally alone in my bedroom."
            "In fact not only does Minami stop giggling, her whole demeanour changes too."
            "I mean, it's not like she suddenly turns evil or anything that dramatic."
            "More like she gets a mischievous look on her face, one that makes her look impish."
        play sound door_slam
        "She leans her back against the door, slamming it closed in the process."
        "And all the time her gaze is focused on a point just below my waist."
        "Or to be more specific, she's staring straight at my cock!"
        "Minami doesn't even need to tell me what she's thinking right now."
        "Just the sight of her sizing me up like this is enough to get the message across."
        "And I can already feel my cock starting to get hard inside of my shorts!"
        "Suddenly Minami clasps her hands behind her back and licks her lips."
        if called_from_date:
            minami.say "Mmm..."
            minami.say "I thought I was full from dinner, big bro."
            minami.say "But now I realise I'm still hungry!"
            "Minami pouts as she says all of this, turning down the corners of her mouth."
        "This serves to make her look irresistibly cute."
        "As well as far more innocent than she is in reality too!"
        "She begins to walk slowly towards me, still pouting as she comes."
        "And without thinking, I walk backwards to keep the distance between us."
        "Part of me doesn't know why I even do it."
        "I'm not afraid of Minami in the slightest."
        "And I really want to see what kind of fun she has in mind here."
        "But still I feel compelled to play along as she advances on me."
        "Soon enough I feel the edge of the bed against the back of my legs."
        "I half sit and half fall down onto the mattress."
        hide minami
        show minami hunt at center, zoomAt(1.5, (640, 1040))
        with vpunch
        "And it's then that Minami pounces on me."
        mike.say "Whoa!"
        minami.say "Don't worry, big bro!"
        minami.say "I've got you!"
        "Minami reaches out and pulls me upright."
        "But she also guides my hands over her body as she does so too."
        show minami normal
        "And the moment that I touch her, it's like tapping into an electric current."
        "I swear that I can feel all of the desire in Minami's body, the pent up energy."
        "Before I know that it's happening, we're pulling at each others clothes."
        "Minami nods and pants desperately as I struggle to undress her."
        "A task made that much harder on account of the fact she's doing the same to me!"
        show minami naked with dissolve
        "Somehow we manage to tear off the last of our clothes and toss them aside."
        hide minami
        show minami naked
        with fade
        "I've made it to my feet a moment later, caressing Minami's body as I do so."
    return

label minami_fuck_date_foreplay_male:
    $ minami_bj = False
    $ minami_cunni = False
    $ minami_spank = False
    $ minami_kiss = False
    $ go_on = False
    while ((not minami_bj and hero.sexperience >= 20) or (not minami_cunni and hero.sexperience >= 15) or (not minami_kiss and hero.fun >= 5) or (not minami_spank and minami.sub >= 50) or (minami.sub >= 60 and "handcuffs" in hero.inventory)) and not go_on:
        menu:
            "Propose to use handcuffs" if minami.sub >= 60 and "handcuffs" in hero.inventory and not minami.flags.handcuffs:
                call minami_fuck_date_handcuffs from _call_minami_fuck_date_handcuffs
            "Kiss her" if hero.fun >= 5 and not minami_kiss:
                $ minami_kiss = True
                call minami_fuck_date_kiss from _call_minami_fuck_date_kiss
            "Spank her" if not minami_spank and minami.sub >= 50:
                $ minami_spank = True
                call minami_fuck_date_spank from _call_minami_fuck_date_spank
            "Give her oral" if not minami_cunni and hero.sexperience >= 15:
                $ minami_cunni = True
                call minami_fuck_date_oral from _call_minami_fuck_date_oral_1
            "Let her suck you off" if not minami_bj and hero.sexperience >= 20:
                $ minami_bj = True
                call minami_fuck_date_bj from _call_minami_fuck_date_bj
            "Fuck her":
                $ go_on = True
    call stop_all_sfx from _call_stop_all_sfx_27

    return _return

label minami_fuck_date_choices_male:
    menu:
        "Reverse cowgirl":
            call minami_fuck_date_cowgirl (0) from _call_minami_fuck_date_cowgirl
        "Missionary" if hero.sexperience >= 5:
            call minami_fuck_date_missionary (5) from _call_minami_fuck_date_missionary
        "Doggy" if hero.sexperience >= 10:
            call minami_fuck_date_doggy (10) from _call_minami_fuck_date_doggy
    call stop_all_sfx from _call_stop_all_sfx_28

    return _return

label minami_fuck_date_kiss:
    "I know what I want from Minami, the way my cock's getting hard is proof of that."
    "But I also know that I need to keep myself from just pouncing on her."
    show minami kiss naked with fade
    $ minami.flags.kiss += 1
    $ minami.love += 1
    "And so I take a firm hold of my desires as I begin to kiss her gently on the lips."
    "The reward for this is the feeling of Minami rising to the kiss herself."
    "Believe me, the kiss really is gentle, as tender as I can make it."
    "But Minami seems to react in the opposite way as she returns the gesture."
    "She's getting more forward by the second, pushing her tongue between my lips."
    "I swear I can almost feel her whole body starting to quiver too!"
    "Before I know it, Minami's doing more than just kissing me with a passion."
    "She's pressing herself against me too, like she needs to get ever closer."
    "And when I feel her hand groping for my cock, I know where this is going!"
    hide minami kiss
    show minami naked
    with fade
    return

label minami_fuck_date_doggy(sexperience_min):
    minami.say "Come on, big bro!"
    minami.say "What are you waiting for?"
    minami.say "I'm getting SO wet down there - just for you!"
    mike.say "I...I'm coming, Minami!"
    mike.say "Just wait a second..."
    "It doesn't take me long to strip off my clothes."
    "And Minami does the same, hastily tossing her own things aside."
    "The moment she sets eyes on my cock, she gasps in amazement."
    minami.say "Is all of that for me?"
    minami.say "Mmm..."
    minami.say "You really are BIG bro!"
    "I can't wait a second longer, I want Minami that badly!"
    "So I all but leap onto the bed, clutching at her as I do so."
    "Minami wails in surprise and tries to scuttle out of reach."
    "But it's pretty obvious that she's not really trying to escape."
    "A moment later I've got my hands on her."
    "And I pull her roughly towards my swaying cock..."
    menu:
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            hide minami
            show minami doggy blush mike
            with fade
            "I catch a glimpse between Minami's buttocks as she wriggles them in anticipation."
            "And from that second on, I can't think of putting it anywhere else."
            "All it takes is a motion of my hands to part those pert like cheeks."
            "Then I aim the head of my cock towards my prize and push as hard as I can."
            show minami doggy pain closed inside
            minami.say "Oh...oh..."
            show minami doggy normal
            minami.say "Oooh...oh god!"
            minami.say "You're in my butt, big bro!"
            show minami doggy open
            "Minami squirms and twists in my hands, waggling her ass."
            "But all she manages to do is work my cock even deeper into her."
            "And as she does so, I can hear the tone of her voice begin to change."
            minami.say "Oh...oooh..."
            minami.say "My butt...it's melting!"
            minami.say "Don't...don't stop, big bro!"
            "I do as she says, pushing myself into her as deep as I can go."
            "And with every inch that squeezes inside her ass, Minami moans all the more."
            "By now she's still squirming and wriggling like crazy."
            "But the difference is that Minami's going in the opposite direction."
            "She's trying to push my cock deeper into her all the time!"
            "Not only does this make my job that much easier, it feels amazing too."
            "Minami's ass is incredibly tight, squeezing me the whole time."
            "Which means that every movement I make is its own reward."
            "And even with Minami doing so much of the work, I don't let up for a moment."
            "My cock moves in and out of her as fast as I can go."
            "All of my energy goes into pounding Minami's ass harder and harder."
            "To begin with she was moaning as I moved more slowly."
            "But now that I'm going as fast as I can, Minami's getting louder too."
            "She yelps and cries out with unashamed pleasure, holding nothing back."
            "Every time I feel my thighs slap into her buttocks, Minami makes that same sound."
            "To my ears, it's an intoxicating mixture of satisfaction and the desire for more."
            "It thrills me to my core and makes me redouble my efforts at the same time."
            "Minami looks back over her shoulder at me, her mouth hanging open."
            "All that she can manage to do is nod desperately, urging me on."
            "I can already feel the muscles inside of her beginning to twitch."
            "And from the look on her face, she's on the edge of cumming!"
            "I don't know it it's just a coincidence, that we're so well attuned to each other."
            "Or else that knowing Minami's about to cum is enough to set me off too."
            "But either way, I suddenly know that I'm going to lose it too!"
            call cum_reaction (minami, 'anal', sexperience_min) from _call_cum_reaction_125
            if _return == "anal_inside":
                "I have my cock so far inside of Minami right now it's almost impossible to pull out."
                "And I don't think she'd be inclined to let me do that, even if I wanted to!"
                "So instead I don't stop for a moment, pushing into Minami until it happens."
                $ minami.love += 2
                $ minami.sub += 2
                show minami doggy ahegao with hpunch
                "She cries out as I shoot my load into her ass, surrendering to her own orgasm too."
                with hpunch
                "I don't know which of us is holding the other up as we cum in the same second."
                with hpunch
                "But as soon as we're both spent, Minami sinks onto the bed and I fall on top of her."
            elif _return == "anal_outside":
                "I don't honestly know how I manage to pull out of Minami before I shoot my load."
                "One moment I'm as deep inside of her as I can go, and the next my cock pops out of her ass."
                "This seems to be all she needs to lose it, and I watch as she cries out, her body shaking."
                $ minami.sub += 4
                show minami doggy -inside cumshot with hpunch
                "I feel the same kind of sensations as I spatter her ass with cum a few seconds later."
                show minami doggy -inside cum bodycum -cumshot with hpunch
                "We must have been holding each other up, as Minami sinks onto the bed before me."
                with hpunch
                "She's down before the cum can even begin to run down her legs."
                "And I fall on top of her a moment later, my muscles finally giving up on me."
            $ minami.flags.anal += 1
        "Fuck her pussy":
            hide minami
            show minami doggy blush
            with fade
            "The moment that Minami waggles her ass at me, I only have one thing on my mind."
            "I want to get my hands on what's hiding between her thighs, and I want to do it now."
            "Or to be more precise, I want to get my cock inside of it in record time!"
            call check_condom_usage (minami) from _call_check_condom_usage_84
            if _return == False:
                return "leave_without_gain"
            show minami doggy mike
            "I take a firm hold of Minami's haunches, pulling her towards me."
            "But it's not like I have to try all that hard to grab her."
            "As she's already pushing her ass backwards, almost grinding it against me!"
            "And it's while we're pushing from opposite directions I feel it happening."
            show minami doggy inside
            "The head of my cock slides along the length of Minami's lips."
            "I hear her moan at the sensation, and then myself joining in too."
            "Because, in that same moment, I slip inside of her."
            "My cock sinks slowly into Minami's pussy, and every second feels amazing."
            "I don't stop until I'm as deep as I can possibly go."
            "And then I hold still, almost holding my breath too."
            minami.say "Oh..."
            minami.say "Oh wow..."
            minami.say "That feels so good, big bro!"
            "Without warning, Minami starts to move back and forth."
            "While I stay still, she works herself on my cock."
            "It's like she can't resist the urge to feel it moving inside of her."
            "The feeling for me is something else, intense and pleasurable in equal measures."
            "But watching Minami as she uses me to get herself off is pretty hot too!"
            "Part of me wants to just kneel there and let her do what she needs to do."
            "And I have no doubt that she could easily bring the both of us off in the end."
            "But then Minami looks back over her shoulder at me."
            "Her mouth hangs open as she pants."
            "And the look in her eyes is almost pleading."
            show minami doggy inside ahegao
            minami.say "Ah..."
            minami.say "P...please, big bro..."
            minami.say "Fuck me...fuck me harder!"
            "I don't hesitate to do as I'm told, as though hypnotised by her gaze."
            "I nod hastily and strengthen my grip on Minami's waist."
            "There's no time to build up speed gradually."
            "I feel like I have to give her what she wants right away."
            "And so I begin to pound away at Minami as fast as I possibly can."
            "At first I'm worried that it's going to be too much for Minami to take."
            "But she soon proves me wrong, taking everything that I have to give."
            "Not only that, she nods her head desperately as I thrust into her."
            "And I don't need to be told that she's demanding more!"
            "By now I'm panting, gasping for breath and sweating like crazy."
            "Minami's slick with perspiration too, slick in my grasp."
            "And when I feel myself cumming, I'm afraid that she might slip out of my hands!"
            call cum_reaction (minami, 'vaginal', sexperience_min) from _call_cum_reaction_126
            if _return == "vaginal_condom":
                "I have my cock so far inside of Minami right now it's almost impossible to pull out."
                "And I don't think she'd be inclined to let me do that, even if I wanted to!"
                "So instead I don't stop for a moment, pushing into Minami until it happens."
                "We remembered to use a condom, so there's no danger of an accident either."
                with hpunch
                "She cries out as I shoot my load into her, surrendering to her own orgasm too."
                with hpunch
                "I don't know which of us is holding the other up as we cum in the same second."
                with hpunch
                "But as soon as we're both spent, Minami sinks onto the bed and I fall on top of her."
            elif _return == "vaginal_outside":
                "I don't honestly know how I manage to pull out of Minami before I shoot my load."
                "One moment I'm as deep inside of her as I can go, and the next my cock pops out of her pussy."
                "This seems to be all she needs to lose it, and I watch as she cries out, her body shaking."
                $ minami.sub += 2
                show minami doggy -inside cumshot with hpunch
                "I feel the same kind of sensations as I spatter her ass with cum a few seconds later."
                show minami doggy -inside cum bodycum -cumshot with hpunch
                "We must have been holding each other up, as Minami sinks onto the bed before me."
                with hpunch
                "She's down before the cum can even begin to run down her legs."
                "And I fall on top of her a moment later, my muscles finally giving up on me."
            elif _return == "vaginal_inside_pill":
                minami.say "I'm on the pill, big bro..."
                minami.say "Don't stop now!"
                "Minami's reminder comes as a great relief."
                "I have my cock so far inside of her right now it's almost impossible to pull out."
                "And I don't think she'd be inclined to let me do that, even if I wanted to!"
                "So instead I don't stop for a moment, pushing into Minami until it happens."
                $ minami.love += 2
                with hpunch
                "She cries out as I shoot my load into her, surrendering to her own orgasm too."
                with hpunch
                "I don't know which of us is holding the other up as we cum in the same second."
                with hpunch
                "But as soon as we're both spent, Minami sinks onto the bed and I fall on top of her."
            elif _return == "vaginal_inside_pregnant":
                minami.say "I'm already pregnant, remember?"
                minami.say "So you'd better not pull out yet!"
                "Minami's reminder comes as a great relief."
                "I have my cock so far inside of her right now it's almost impossible to pull out."
                "And I don't think she'd be inclined to let me do that, even if I wanted to!"
                "So instead I don't stop for a moment, pushing into Minami until it happens."
                $ minami.love += 2
                with hpunch
                "She cries out as I shoot my load into her, surrendering to her own orgasm too."
                with hpunch
                "I don't know which of us is holding the other up as we cum in the same second."
                with hpunch
                "But as soon as we're both spent, Minami sinks onto the bed and I fall on top of her."
            elif _return == "vaginal_inside_mad":
                minami.say "Big bro..."
                minami.say "You have to pull out - NOW!"
                "Minami's words take me by surprise and it's that which leads to disaster."
                "That and the fact she tries to pull herself off of me at the same time."
                "All that does is get in the way of me getting my cock out of her before it's too late."
                with hpunch
                "She cries out as I shoot my load into her, surrendering to her own orgasm too."
                $ minami.impregnate()
                $ minami.love -= 25
                $ minami.sub += 5
                with hpunch
                "I don't know which of us is holding the other up as we cum in the same second."
                with hpunch
                "But as soon as we're both spent, Minami sinks onto the bed and I fall on top of her."
                "All we can do is stare at each other, shocked and confused by what just happened."
            elif _return == "vaginal_inside_happy":
                "I suddenly remember that we didn't use a condom."
                "And so I begin to pull out of Minami before it's too late."
                minami.say "Oh no you don't!"
                minami.say "You're not going anywhere, big bro!"
                "Minami's words take me by surprise and it's that which leads to disaster."
                "Sure, she holds onto me, but it's more my confusion that makes it happen."
                with hpunch
                $ minami.love += 5
                $ minami.impregnate()
                "She cries out as I shoot my load into her, surrendering to her own orgasm too."
                with hpunch
                "I don't know which of us is holding the other up as we cum in the same second."
                with hpunch
                "But as soon as we're both spent, Minami sinks onto the bed and I fall on top of her."
                "She looks happy and satisfied, but I'm still shocked and confused by what just happened."
    hide minami with fade
    "Once her orgasm has faded, Minami cuddles herself up against me."
    "She lays her head on my chest and I can hear her breathing begin to change."
    "Soon enough it turns into gentle snoring as she falls asleep."
    "The sound soothes me, making me relax in turn."
    "And before too long, I slip into a deep sleep as well."
    return

label minami_fuck_date_spank:
    "Once Minami's naked, I can't take my eyes off of her for even a moment."
    "And as soon as she see's this, she begins to blush and giggle at the attention."
    "Which, of course, only makes me want to get my hands on her all the more."
    "And it's then I get an idea into my head, one that just won't quit."
    "So I sit down on the bed and beckon for Minami to come join me."
    mike.say "Hey, Minami..."
    mike.say "You've been a REALLY naughty girl."
    mike.say "And I think you deserve to be punished!"
    "I pat my thighs, letting her know that I want her right there."
    "Minami's walking over to me slowly, but she stops when she see this."
    "She has her hands behind her back and she's biting her lip."
    "Wow - she looks even hotter when she's nervous!"
    if minami.sub >= 55 and not minami.flags.spanked:
        $ minami.flags.spanked = True
        "For a moment I think Minami's going to refuse."
        "But then I see a twinkle in her eye as she looks at me."
        show minami tehe
        "And an impish smile slowly spreads across her face."
        minami.say "Oh, big bro..."
        minami.say "Have I really been so bad?"
        minami.say "Then I guess you just HAVE to punish me!"
        "With that, she lets out a mischievous giggle."
        "And then comes running towards me."
    elif minami.sub >= 25:
        "For a moment I think Minami's going to refuse."
        "Like she didn't enjoy it the last time I spanked her."
        "But then I see a twinkle in her eye as she looks at me."
        show minami tehe
        "And an impish smile slowly spreads across her face."
        minami.say "Oh, big bro..."
        minami.say "I loved it when you spanked me before."
        minami.say "And I've been trying to be bad ever since!"
        minami.say "Just so that you'd HAVE to punish me!"
        "With that, she lets out a mischievous giggle."
        "And then comes running towards me."
    else:
        $ minami.sub -= 5
        show minami annoyed
        minami.say "Ah..."
        minami.say "Big bro..."
        minami.say "Can we leave off the spanking this time?"
        minami.say "I kinda don't feel like having my ass slapped tonight!"
        "I'm disappointed to hear that Minami's not up for it."
        "But knowing that the other person's not into it is a turn-off anyway."
        "So I do the best I can to sound upbeat and nod in agreement."
        mike.say "Okay, Minami, no worries."
        mike.say "We can do something else instead."
        return
    $ minami.sub += 1
    show minami spank bedroom naked mikenaked
    "Minami obediently lays herself over my thighs as soon as she reaches the bed."
    "And I can feel myself getting stiff almost the same moment she's laid down too."
    "The sensation of her weight feels good, pressing down on me the whole time."
    "Every inch of her body is spread out before me, ripe for the taking."
    "But we've already decided on the particular game we're going to play."
    mike.say "I have to do this, Minami."
    mike.say "It's for your own good."
    mike.say "And it hurts me more than you!"
    show minami spank down surprise
    play sound spank
    with hpunch
    "The first blow is fairly light, but still sounds crazily loud."
    "And Minami lets out a yelp as soon as it lands across her buttocks."
    "But the sounds is more from surprise than pain."
    show minami spank middle pleasure
    minami.say "Ooh...ouch!"
    minami.say "I...I understand, big bro."
    minami.say "I'm such a bad girl...and I deserve this!"
    show minami spank up
    "I can hear the effect this is having on Minami, just listening to her voice."
    "There's a tremble of excitement in there, and a hint of arousal too."
    show minami spank down pain
    play sound spank
    with hpunch
    "And so the second slap comes close on the heels of the first."
    show minami spank pleasure
    "This one is harder and sharper, the sound louder as a result."
    show minami spank up
    "Minami yelps again and squirms around in my lap."
    "All of which makes me even more eager to land a third blow."
    "And that comes before Minami can even manage to say a word."
    show minami spank down pain
    play sound spank
    with hpunch
    "With that I'm well and truly away, spanking like my life depends on it."
    show minami spank up pleasure
    "Minami doesn't complain for a moment either."
    show minami spank down pain
    play sound spank
    with hpunch
    "In fact she soaks it up as fast as I can dish it out!"
    show minami spank up pleasure
    "The more I spank her buttocks, the more she seems to like it."
    show minami spank down pain
    play sound spank
    with hpunch
    "Soon enough, the cheeks on her face are as red as the ones on her ass!"
    show minami spank up pleasure
    "But still she's not asking me to stop, just nodding for more."
    show minami spank marks
    minami.say "Ah...ah..."
    minami.say "Yes...please..."
    minami.say "I'll be good, big bro...I promise!"
    show minami spank down pain
    play sound spank
    with hpunch
    "I can't keep this up much longer."
    show minami spank up pleasure
    "I'm scared that I'll leave a permanent mark on Minami's ass!"
    show minami spank down pain
    play sound spank
    with hpunch
    "Plus my hand is starting to lose all feeling too."
    show minami spank up pleasure
    "Not to mention what the weight of her is doing to my cock!"
    show minami spank down pain
    play sound spank
    with hpunch
    "At this rate, I'll end up cumming in my shorts."
    show minami spank up pleasure
    "So I slowly ease off on the spanking, a little at a time."
    show minami spank down pain
    play sound spank
    with hpunch
    "And as I do so, Minami's groans and pants slow down too."
    show minami spank up pleasure
    "But even when I come to a halt, she's still gasping for breath."
    show minami spank down pain
    play sound spank
    with hpunch
    "And her buttocks are practically glowing red!"
    return

label minami_fuck_date_handcuffs:
    $ minami.flags.handcuffs = True
    if not minami.flags.already_did_handcuffs:
        $ minami.flags.already_did_handcuffs = True
        "I can already feel my cheeks starting to burn as I open my mouth to speak."
        "But I'm committed now, so I have to see it through to the bitter end."
        mike.say "Ah, Minami..."
        minami.say "Hmm..."
        minami.say "Yeah, big bro?"
        mike.say "How do you feel about...handcuffs?"
        "Minami cocks her head on one side, looking a little confused."
        minami.say "Handcuffs?!?"
        mike.say "You know...like in the bedroom?"
        hide minami
        show minami naked surprised
        "At this, Minami's eyes go wide."
        minami.say "You mean like...like bondage and stuff?!?"
        "Well, I'm one hundred percent committed now!"
        mike.say "Yeah, Minami - I wondered if we could try it out?"
        mike.say "But obviously, if you're not into that kind of thing..."
        show minami hunt
        minami.say "Okay, big bro - you can slap the cuffs on me, and we can get kinky!"
        mike.say "Y...you mean that's a yes?!?"
        show minami tehe
        minami.say "Of course, big bro - it sounds like fun!"
    else:
        mike.say "Wanna play with the handcuffs again?"
        hide minami
        show minami naked hunt
        minami.say "Okay, big bro - you can slap the cuffs on me, and we can get kinky!"
    return

label minami_fuck_date_missionary(sexperience_min):
    $ game.play_music("music/roa_music/new_days.ogg")
    $ game.room = "bedroom1"
    "I smile too, and put my own arms around her, leading her towards the bed."
    "As soon as her legs touch the side of the mattress, Minami turns and scrambles onto it."
    "She goes backwards, her eyes fixed on mine as she does so, almost pulling me after her."
    "And I do follow, perhaps a step behind Minami, enjoying the sight of her spread out before me."
    "She tries to keep on looking me in the eye as I start to climb up the length of her body."
    "But I see her gaze flitting down to where my cock is rubbing against her thighs."
    "And I see the anticipation in them too, as well as a little genuine fear."
    mike.say "Don't worry about a thing, Minami."
    mike.say "This is going to be as special as the first time - trust me."
    "Minami nods as she looks up at me."
    "And the genuine trust in her eyes almost makes my heart skip a beat."
    minami.say "Oh, big bro..."
    minami.say "It could only ever BE special with you!"
    "I take a deep breath then, preparing myself for what lies ahead."
    "After all, this isn't just sex with any random girl that I could have in the course of my normal, everyday life."
    "This is Minami, the adopted sister that I grew up with and only recently discovered has been in love with me forever."
    "And even more amazing is the fact that I'm quickly discovering that I feel the same way too!"
    menu:
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            hide minami
            scene minami missionary
            with fade
            "It's then that a thought occurs to me - do I actually want to do this the normal way?"
            "I mean, we're not exactly the most conventional of couples, are we."
            "So why not keep mixing things up and experiment a little?"
            "That's why I angle my cock a little lower than normal, aiming straight for Minami's ass..."
            if not minami.flags.anal:
                minami.say "Ooh!"
                minami.say "Big bro, what are you..."
            else:
                minami.say "Whoa..."
                minami.say "Big bro, you naughty boy!"
                minami.say "Putting something that big up my poor, little ass!"
            "And that's all that Minami has the chance to say before my cock hits the target."
            "I see Minami's eyes go suddenly wide and then roll back into her head."
            "All of this is accompanied by the sensation of my cock pushing slowly but surely up her ass."
            "Minami's arms are thrust out to either side of her body."
            "Her hands clutching at the bedclothes as if holding on for dear life."
            "And all the time I'm still sinking into her, lowering myself as she takes the entire length of my cock."
            "Only when I've buried myself as deep into Minami as I can do I begin to move again."
            "Slowly at first, I start to rise and fall above her."
            "The muscles of her ass are incredibly tight, making it all the more pleasurable for me."
            "For a moment, I don't think I'll actually be able to move at all."
            "I expect her ass to hold me so tight that I'll be all but trapped."
            "Then, with almost infinite slowness, I start to move."
            "Each and every second that I do so seems to make Minami wriggle and writhe."
            show minami missionary speed
            "Her petite body is literally shaking from what I'm doing to her right now."
            "I don't think she could form a single word, even if she were of a mind to do so."
            "Instead she pants and moans, vocalising the sensations of having my cock so deep inside of her."
            "All I can do is marvel at the sight of her, spread out before me."
            show minami missionary closed
            "It baffles me now how I could ever have thought of Minami as merely a little sister."
            "If we were blood relatives, things would be different."
            "But we're not, and I make a vow, right there and then, that I'll never think of her that way again."
            "After all, I could never have done what I'm about to do to my own sister!"
            call cum_reaction (minami, 'anal', sexperience_min) from _call_cum_reaction_127
            if _return == "anal_inside":
                "I could pull out of her before I actually cum, but something stops me from doing so."
                "Perhaps it's the need to go all the way, to finish this inside of Minami."
                "Or maybe I'm just enjoying myself too much to even think of stopping now!"
                "Either way, I keep right on until the very last moment."
                "I thrust my cock in and out of Minami, making her gasp with each motion."
                show minami missionary ahegao with hpunch
                "And then I push with all my might, cumming inside of her as I do so."
                with hpunch
                "Minami actually cries out when I do so, wrapping herself around me and clinging on."
                with hpunch
                "Utterly spent, I sink down atop her, pulling her as close as I possibly can."
                "And in a tangle of sweaty limbs, we lie together, panting and exhausted."
            elif _return == "anal_outside":
                "Just before I cum, I somehow manage to pull my cock out of Minami's tight little ass."
                "She lets out a sudden moan at the sensation, arching her back as she does so."
                show sexinserts chest minami
                "This means that she spreads her petite, perfectly rounded breasts, presenting them as an easy target."
                show sexinserts chest minami cum
                with hpunch
                "The streamers of sticky, white semen rain down on them a moment later."
                with hpunch
                "Minami looks on in surprise, eyes wide as she watches the shower."
                show sexinserts belly minami cum -chest
                with hpunch
                "Soon the cum begins to run down, over her belly and towards her groin."
                "I watch as it flows, silent save for the sound of my own exhausted panting."
                "In fact, I can't tear my eyes away from the sight of Minami as she lies there."
                "Flushed red, slick with sweat and painted with cum."
                "I've never seen her look more beautiful than she does right now."
            $ minami.flags.anal += 1
        "Fuck her pussy":
            "I can already feel the state of Minami's pussy as my cock rubs between her thighs."
            "She's getting wet enough down there to make it pretty hard to think about much else!"
            "But then, I guess there's nothing wrong with keeping things simple."
            call check_condom_usage (minami) from _call_check_condom_usage_85
            if _return == False:
                return "leave_without_gain"
            hide minami
            scene minami missionary
            with fade
            "Even with only the very tip of my cock against Minami's lips, I can already feel it pushing inside of her."
            "It won't be long before every inch of it is sliding in there as slick as can be."
            "Where she was nervous and afraid the first time that we made love, Minami shows none of those fears now."
            "Instead she smiles in anticipation as I push my cock into her, and then moans deeply as I sink further in."
            "Once I'm in all the way, I pause for a moment, enjoying the feeling of her tight pussy around me."
            "Minami chuckles at me, clearly pleased with the delight that I'm taking from our coupling."
            minami.say "Mmm..."
            minami.say "It feels SO good to have you back inside of me, big bro!"
            "Encouraged by Minami's words, I begin to move in and out of her."
            "I go slowly at first, building up more speed as I go and hearing her respond to my attentions."
            "I do this because I want to be as gentle as I can with Minami, as caring as possible."
            "But it doesn't take long for me to see that I've been way too cautious with her."
            show minami missionary speed
            "Where I thought that she'd need to be coaxed into letting herself go, she soon proves not to need my help."
            "Whatever I give her, Minami takes without as much as a pause or hesitation."
            show minami missionary closed
            "And every ounce of stimulation and pleasure I give her only seems to make her hungry for more."
            "Pretty soon I feel like I'm the one being pushed to the limit, struggling to keep up."
            "Minami's small, supple body is like a sponge, absorbing all of the energy that I have to give."
            minami.say "Ah..."
            minami.say "Yeah, please..."
            minami.say "Don't stop now, big bro..."
            minami.say "I want your cock inside of me forever!"
            "That might be asking a bit too much, but I'm determined to do my best to satisfy her all the same."
            "I redouble my efforts, by now almost pounding Minami hard enough to drive her into the mattress below us."
            "But no matter how much I give her, it seems like it's not enough to satiate Minami's desire!"
            show minami missionary ahegao
            minami.say "Oh fuck..."
            minami.say "Oh...fuck..."
            minami.say "I think I'm cumming!"
            "Minami's sudden announcement takes me completely by surprise."
            "I was sure that she'd end up wearing me out, but now she's telling me that she's ready to blow!"
            "The revelation is all that I need to feel myself losing it too..."
            call cum_reaction (minami, 'vaginal', sexperience_min) from _call_cum_reaction_128
            if _return == "vaginal_condom":
                with hpunch
                "Minami gasps and moans as I put all of my remaining strength into one last push."
                with hpunch
                "And then she rides my cock as I lose myself inside of her."
                $ minami.love += 1
                with hpunch
                "I can't be sure in the confusion, but I think we actually came together."
                "I stay inside of her afterwards, enjoying the sensation of her muscles twitching around me."
                "And Minami clings to me too, as if determined to stay as close to me as possible for as long as she can manage."
            elif _return == "vaginal_outside":
                "Just before I cum, I somehow manage to pull my cock out of Minami's tight little pussy."
                "She lets out a sudden moan at the sensation, arching her back as she does so."
                show sexinserts chest minami
                "This means that she spreads her petite, perfectly rounded breasts, presenting them as an easy target."
                show sexinserts chest minami cum
                with hpunch
                "The streamers of sticky, white semen rain down on them a moment later."
                with hpunch
                "Minami looks on in surprise, eyes wide as she watches the shower."
                show sexinserts belly -chest minami cum
                with hpunch
                "Soon the cum begins to run down, over her belly and towards her groin."
                "I watch as it flows, silent save for the sound of my own exhausted panting."
                "In fact, I can't tear my eyes away from the sight of Minami as she lies there."
                "Flushed red, slick with sweat and painted with cum."
                "I've never seen her look more beautiful than she does right now."
            elif _return == "vaginal_inside_pill":
                minami.say "It's okay, big bro..."
                minami.say "I'm on the pill..."
                minami.say "Cum in me all you like!"
                $ minami.love += 2
                "Minami whispers those words into my ear a mere second before I lose myself inside of her."
                "She rides my cock on delight as I do so, enjoying every last moment before it's all over."
                "Afterwards, she slides happily off of my cock, the cum already starting to leak out of her."
            elif _return == "vaginal_inside_pregnant":
                "Minami laughs and smiles up at me as she cradles her growing belly."
                "And I return her smile, safe in the knowledge that we both want the same thing."
                $ minami.love += 2
                "She rides my cock on delight as I do so, enjoying every last moment before it's all over."
                "Afterwards, she slides happily off of my cock, the cum already starting to leak out of her."
            elif _return == "vaginal_inside_mad":
                minami.say "Wait..."
                minami.say "You can't..."
                $ minami.love -= 25
                $ minami.impregnate()
                with hpunch
                "Minami hisses those words into my ear a mere second before I lose myself inside of her."
                with hpunch
                minami.say "You did..."
                minami.say "You came inside of me!"
                "The look of horror and surprise on her face is matched only by my own."
                "Shit - what have we done?!?"
            elif _return == "vaginal_inside_happy":
                "I know full well that I can't let myself cum inside of Minami without protection."
                "So I make to pull out of her, but then feel that she's holding on, stopping me from doing so!"
                mike.say "Minami!"
                mike.say "What are you doing?!?"
                minami.say "It's okay, big bro."
                minami.say "This was always how it was supposed to happen!"
                with hpunch
                $ minami.love += 5
                $ minami.impregnate()
                "I'm still trying to make sense of the situation when I lose myself inside of her."
                with hpunch
                "Minami rides the whole thing out in delight, smiling as I fill her."
                "But all I can feel is fear and confusion, not knowing what's happening or why."
    return

label minami_fuck_date_cowgirl(sexperience_min):
    $ game.play_music("music/roa_music/new_days.ogg")
    $ game.room = "bedroom1"
    "Instead, I just reach out and grab hold of Minami, pulling her towards me."
    "She giggles again as she's drawn into my embrace, wriggling and pretending to fight."
    "But the moment that we're locked together, I hear her sigh deeply."
    hide minami
    show minami kiss naked
    with fade
    $ minami.flags.kiss += 1
    "I was making to kiss her, but she beats me to the punch, pressing her lips against mine."
    "Before I can return the gesture with all that I have, Minami's tongue darts into my open mouth."
    "She kisses me deeply and with a strength of passion that belies her petite frame."
    "And I swear that it's as much this kiss as the feel of her naked skin against mine that makes me get hard."
    "When she finally pulls away, breaking the kiss, I can hear Minami gasping for breath."
    hide minami
    show minami naked blush
    with fade
    minami.say "That's...what I want..."
    minami.say "How deep...I want you in me..."
    "And then she turns her back to me, almost teasing me with her ass."
    "I don't need to be given any more encouragement than that."
    "Pressing my belly against her back, I gently pull Minami towards me."
    menu:
        "Fuck her ass" if hero.sexperience >= (sexperience_min + 5):
            show minami cowgirl with fade
            "The first thing that I feel once we're pressed together is the sensation of Minami's ass in my lap."
            "It's so soft and perfectly rounded, the only possible counter-balance to her sweet little breasts."
            "As my cock starts to rub against her buttocks, it naturally finds its way between them."
            "But as soon as I hear Minami yelp and then giggle at the feeling, an idea forms in my mind."
            "Placing my hands on her haunches, I position myself in just the right way."
            "And then I pull her firmly backwards in one smooth motion..."
            show minami cowgirl anal surprised
            minami.say "WHOA!"
            minami.say "Big bro - what are you..."
            minami.say "Ahhh...."
            "I can feel every fraction of an inch as my cock pushes into Minami's ass."
            "Her muscles are tight, like a clenched fist as they try to resist my efforts."
            "But before too long they begin to surrender, and I slide ever deeper into her."
            minami.say "Mmm..."
            minami.say "Oh, fuck..."
            minami.say "That feels SO good, big bro..."
            minami.say "Don't stop - please, fuck my ass!"
            "It's not as if I needed the encouragement, as that was my plan all along!"
            show minami cowgirl speed
            "Starting out slow and gentle, I begin to move inside of Minami's ass."
            "She moans and sighs with even the smallest of motions, her head starting to toss this way and that."
            "Her body is so light and supple that I have no trouble thrusting into her."
            "And soon she's dancing like a puppet on my cock."
            if not minami.flags.handcuffs:
                show minami cowgirl up
                "Seeing her breasts bouncing up and down, I reach around and take them in my hands."
                "Minami's nipples are as stiff as can be, and I roll them between my fingers."
                "This only serves to add to the state that she's already worked herself into."
            show minami cowgirl orgasm
            "And she practically begins to leap in time to my efforts, gasping for breath."
            "In this way, the dynamic between us slowly begins to shift."
            "Pretty soon I feel like it's Minami's sitting on my cock that's pushing me towards the end."
            "Whereas when we started out, she was the one that simply taking it from me."
            "But it's not like I've completely surrendered all control."
            "I still have a say in just when and where I cum in the end..."
            show minami cowgirl -speed
            call cum_reaction (minami , 'anal', sexperience_min) from _call_cum_reaction_129
            if _return == "anal_inside":
                "That said, it's not like I'm eager to pull my cock out of Minami before it's all over."
                "So I keep on letting her ride me until the very last moment, her cries filling my ears the whole time."
                show minami cowgirl creampie with vpunch
                $ minami.love += 1
                "And those same cries only become louder once I lose myself inside of her."
                with vpunch
                "Minami bucks and writhes as I hold onto her, unwilling to let her slip out of my grasp."
                with vpunch
                "Only when I've shot my entire load do I finally loosen my grip, gently guiding her down onto the bed."
                "She lies there, panting in complete and utter exhaustion, my cum already starting to leak out of her."
                "But it's not like I'm in any better condition, only able to kneel there, trying to catch my breath."
            elif _return == "anal_outside":
                "Suddenly I feel the urge to pull my cock out of Minami before it's too late."
                "And so I half pull back and half lift her off of me in the last few moments left."
                with vpunch
                "I hear her moan at the sensation of my cock sliding out of her, the sound of pleasure tinged with disappointment."
                show minami cowgirl cumshot
                show sexinserts minami chest zorder 1
                show sexinserts minami belly as bellycum zorder 2 at center, zoomAt(1, (670, 970))
                with vpunch
                $ minami.sub += 2
                "But there's no more than a couple of seconds for her to dwell on that before I cum."
                show minami cowgirl dickcum
                show sexinserts minami chest cum zorder 1
                show sexinserts minami belly cum as bellycum zorder 2 at center, zoomAt(1, (670, 970))
                with vpunch
                "Standing up between Minami's thighs, my cock sprays her belly and breasts with stings of semen."
                show minami cowgirl -cumshot dickcum
                "She watches, eyes wide with amazement as it begins to run down her chest and over her stomach."
                "And the whole time, the only sound is that of us both panting in sheer exhaustion."
            $ minami.flags.anal += 1
        "Fuck her pussy":
            "As Minami's ass settles into my lap, I feel the wet warmth of her pussy against my cock."
            "She wriggles and giggles at the sensation, clearly excited at the prospect of what's coming next."
            "And once I know that's what she has on her mind, I can't help but start wanting the same thing too."
            call check_condom_usage (minami) from _call_check_condom_usage_86
            if _return == False:
                return "leave_without_gain"
            show minami cowgirl down
            if CONDOM:
                show minami cowgirl condom
            "Putting a hand on Minami's waist, I stroke my cock up and down a couple more times."
            if not minami.flags.handcuffs:
                show minami cowgirl up
                "As I do this, I reach around with the other hand, taking hold of one of her breasts."
                "With my fingers, I rub at her already stiff nipple, rolling it between them and squeezing gently."
            "I see Minami look down at what I'm doing, her gaze fixed on the actions of my hand."
            "And once I'm sure that she's truly distracted, I pull my cock back and aim it at her pussy."
            show minami cowgirl vaginal
            if hero.has_skill("hung"):
                show minami cowgirl hung
                $ minami.sub += 1
            "The state that she's already worked herself into means that there's almost no resistance whatsoever."
            "Minami might not be ready for it yet, but her pussy is more than willing."
            "I must be almost halfway into her before she realises what's going on."
            show minami cowgirl surprised
            if hero.has_skill("hung"):
                show minami cowgirl poke
                $ minami.sub += 1
            minami.say "Whoa..."
            minami.say "Wha..."
            minami.say "Oh shit...you're inside of me!"
            minami.say "Oh...that feels good, so good!"
            "It feels pretty good from where I'm sitting too."
            "Minami's pussy might have been soft on the outside, but the muscles inside are something else entirely."
            "They're almost unbelievably tight, squeezing on the head and shaft of my cock."
            "She fits like a glove and I feel the proverbial fingers inside of it too."
            "I like to flatter myself into thinking that I have a pretty big cock."
            show minami cowgirl orgasm
            "But this is one of those times that I actually worry it might be too much for Minami to handle."
            "Yet she swallows each and every inch that I push into her, sinking down onto me the whole time."
            "And almost the very same second that I feel like I can't go any deeper, she starts to ride me."
            show minami cowgirl speed
            "In this position, you really understand why girls of her size get called 'laptops'!"
            "Minami literally leaps up and down in my lap, making short, yelping sounds of pleasure."
            "Every move she makes is replayed in the way her hair tosses and her breasts bounce."
            "So much so that the sight of it is almost as big of a turn-on as being inside of her."
            minami.say "Mmm..."
            minami.say "Big bro..."
            minami.say "You're gonna make me...cum!"
            "The mere mention of Minami having an orgasm while on the end of my cock is enough to push me that far too."
            "And I can already feel the sensation building up inside of me..."
            show minami cowgirl down -speed
            call cum_reaction (minami, 'vaginal', sexperience_min) from _call_cum_reaction_130
            if _return == "vaginal_condom":
                "In the moment, I can't recall much, save for the fact we took precautions before we got started."
                "And it means that I don't have to worry about surrendering to the moment, so I do just that."
                $ minami.love += 1
                with vpunch
                "Minami's words trail away into incoherent moans as I let myself go inside of her."
                with vpunch
                "Her breath comes in ragged gasps, and I swear that I catch a glimpse of her eyes actually glazing over."
                with vpunch
                "And then she sags in my arms, like a puppet with severed strings."
                "I hold onto her until the last throes of my orgasm have passed, and then lay her gently down on the bed."
            elif _return == "vaginal_outside":
                "It'd be almost too easy to keep right on going and cum inside of Minami right now."
                "She's totally lost in the moment and probably doesn't even remember that we didn't use protection."
                "But the fact that I'm still aware enough to know that means the responsibility fall on me."
                "And as much as I don't want to, the risk of us having an accident is too great."
                show minami cowgirl outside
                show sexinserts minami chest zorder 1
                show sexinserts minami belly as bellycum zorder 2 at center, zoomAt(1, (670, 970))
                with vpunch
                "So in the last couple of seconds, I lift Minami off of my cock."
                with vpunch
                "She's light enough to make this possible, and though she protests, I ignore her and do what I must."
                show minami cowgirl cumshot
                show sexinserts minami chest cum
                show sexinserts minami belly cum as bellycum at center, zoomAt(1, (670, 970))
                with vpunch
                $ minami.sub += 1
                "Almost as soon as it's free, I cum without restraint, painting Minami's stomach and breasts with semen."
            elif _return == "vaginal_inside_pill":
                minami.say "Ah, big bro..."
                minami.say "Shoulda said..."
                minami.say "On...the...pill!"
                mike.say "Huh?!?"
                "Ironically, Minami's efforts to let me know it's okay to cum inside of her are what ensure that I actually do."
                $ minami.love += 2
                show minami cowgirl creampie ahegao with vpunch
                "Minami's words become nothing more than moans as I shoot my load into her."
                with vpunch
                "Her breath comes in ragged gasps, and then she sags in my arms, like a puppet with severed strings."
                with vpunch
                "As the last moments of my orgasm finally pass, I lay her on the bed as gently as I can manage."
            elif _return == "vaginal_inside_pregnant":
                "I have the constant reminder of Minami's rounded belly to let me know there's no need to pull out."
                "But the sight of it does mean that I try to cradle and support her that little bit more."
                $ minami.love += 2
                show minami cowgirl creampie ahegao with vpunch
                "Still she shudders and moans as I cum inside of her, making sounds that could never be mistaken for words."
                with vpunch
                "I keep a hold of her as the last throes of our orgasms pass away, almost reluctant to let her go once they have."
                with vpunch
                "Only when I'm sure that it's all over do I carefully lay Minami down on her side."
                "I watch her then, as she lays there, arms clutching her belly, unconsciously protecting what's growing inside."
            elif _return == "vaginal_inside_mad":
                minami.say "Ah, big bro..."
                minami.say "We didn't..."
                minami.say "Didn't use a condom!"
                mike.say "Wha?!?"
                show minami cowgirl creampie with vpunch
                $ minami.love -= 25
                $ minami.impregnate()
                "The true meaning of Minami's words only hits me in the same moment that I cum inside of her."
                with vpunch
                "Each and every thrust serves to hammer home the mistake that we've just made."
                with vpunch
                "Even though I whip my cock out of her a second later, the damage is already done."
                "We both stare in silence, watching the cum begin to drip out of her pussy and run down the inside of her thighs."
            elif _return == "vaginal_inside_happy":
                "At the last possible second, I remember that we didn't bother with a condom."
                "And so I instantly make to whip my cock out of Minami before it's too late."
                minami.say "Oh no you don't, big bro!"
                "I feel Minami wrapping herself around me, keeping me from pulling out of her."
                mike.say "Wha..."
                mike.say "What are you..."
                minami.say "Don't worry, big bro."
                minami.say "This is how it's supposed to be!"
                show minami cowgirl creampie ahegao with vpunch
                $ minami.love += 5
                $ minami.impregnate()
                "Then I cum inside of her, still stunned by what she just did and said."
                with vpunch
                "In fact, I'm so shocked that I hardly feel a thing."
                "And all I can hear is Minami, making sounds like those of a satisfied cat..."
    return

label minami_fuck_date_bj:
    show minami bj
    minami.say "Aw, big bro..."
    minami.say "You're always so good to me!"
    minami.say "I said I was hungry, and this is just what I need..."
    "With that, Minami leans forward and parts her lips."
    show minami bj lick out
    "She looks up at me as she sticks her tongue out."
    "Then she begins to lick at the very tip of my cock."
    "I want to say something witty in reply, to make Minami laugh."
    "But I'm frozen as I watch her begin to kiss and caress my cock."
    "So all I can do is jerk a quick nod, urging her to go further."
    "Minami doesn't nod in return."
    show minami bj close
    "Instead she closes her eyes and opens her mouth wider still."
    "And suddenly I have the urge to close my eyes too."
    "Seriously, the feeling is that intense!"
    "Minami doesn't give oral like she's read about it in some book."
    "And it doesn't feel like she's copying a porn film she's seen either."
    "What she's doing feels as if it's based on instinct and intuition."
    "Well, that and a whole lot of honest desire and physical need too!"
    "Minami does what feels right to her in the moment."
    "And she seems to be listening closely to my reactions too."
    "Because when I sigh or moan with pleasure, she takes note."
    "Then she either repeats the action or doubles down on it."
    show minami bj suck -out
    "Minami slowly takes ever more of my cock into her mouth."
    "She's not desperate to swallow me whole."
    "But rather she's feeling her way, a little at a time."
    "And for me the sensation of her doing do is crazily intense!"
    "The more she hits the spot, the more I can't help letting it show."
    "And the more I let it show, the better she seems to get."
    show minami bj blush
    "By now Minami has more than half of my length in her mouth."
    "Her head is moving back and forth as she works her lips and tongue."
    "And the only thing in the world I can think of is watching her."
    "Ah...I know how terrible this is going to sound..."
    "But she really does look beautiful while she's sucking away!"
    "I've seldom seen Minami look so peaceful and serene!"
    "She looks like an angel would if one ever gave someone oral!"
    "Suddenly my thoughts are interrupted by a spasm and a twitch."
    "So much for thinking about angels and heavenly images."
    "I'm about to do something that's one hundred percent grounded in reality!"
    menu:
        "Cum on her face":
            "If Minami senses the fact that I'm about to cum, she doesn't show it."
            show minami bj surprised open out -suck -blush
            "So my guess is that it comes as a surprise to her when I pull my cock out her mouth."
            "I'm just grateful that she opens her eyes and makes a muffled sound of confusion."
            "You know, rather than her biting down on sheer instinct?"
            "All of this means that Minami's staring, wide-eyed a moment later."
            show sexinserts minami head zorder 1
            show minami bj cumshot
            with vpunch
            "Which happens to be the very moment that I shoot my load into her face!"
            show minami bj facial close with vpunch
            $ minami.sub += 1
            "Stripes of white cum spatter across Minami's cheeks and nose."
            show sexinserts minami head cum zorder 1
            show minami bj -cumshot
            with vpunch
            "And as her mouth is as wide open as her eyes, it lands in there as well."
            show minami bj open -out
            "Minami coughs and splutters, blinking as she shakes her head from side to side."
        "Cum in her mouth":
            "If Minami senses the fact that I'm about to cum, she doesn't show it."
            "So my guess is that it comes as a surprise to her when she feels me start to cum!"
            show sexinserts minami head cum zorder 1
            show minami bj open cumshot -blush
            with vpunch
            "My suspicions are confirmed a few moments later as Minami's eyes snap open."
            with vpunch
            "And I'm worried that she's going to be overwhelmed, that she'll choke on it!"
            show minami bj close with vpunch
            $ minami.love += 1
            "But them it's my turn to be surprised, as Minami recovers before my eyes."
            "It's like she rises to the challenge, gulping down all that I have to give."
            show sexinserts minami head -cum zorder 1
            show minami bj -suck -cumshot swallow
            "Once done, she finally leans back, letting my cock slip out of her mouth."
            "Minami pants wearily, licking the last traces of cum from her lips."
    "I'm still gasping for air afterwards, trying to keep standing."
    show minami bj open lick
    "But I manage a smile as I look down at Minami, kneeling before me."
    minami.say "You filled me up nicely!"
    "Minami starts to giggle again as she looks up at me."
    "And I may well be exhausted right now, but one thing's for sure."
    "If she keep on doing that, I'm going to get a second wind!"
    hide sexinserts
    return

label minami_fuck_date_oral_intro:
    $ game.play_music("music/roa_music/new_days.ogg")
    scene bg bedroom1
    show minami
    with fade
    "Almost as soon as we're alone in my room, Minami leaps into my arms."
    "I catch her, but only just."
    "Which means that I'm treated to the sensation of her wrapping her legs and arms around me."
    show minami happy
    minami.say "Oh, big bro..."
    minami.say "I had SO much fun tonight!"
    minami.say "You know, big bro, I can still smell it on us both."
    minami.say "I can still taste everything too!"
    "I know that I should tell her to stop calling me that."
    "But the truth is I'm so used to it that I always forget to tell her so."
    "And I secretly love the way she now says something so familiar with such obvious desire."
    mike.say "Me too, Minami."
    mike.say "But the night's not over yet."
    mike.say "And I want to taste something else before it's done..."
    "With that, I start to walk towards the bed, still holding her against me."
    "Minami looks at me with a quizzical expression on her face."
    "It's one that reminds me that, for all her boldness, she's still quite innocent at times."
    "Only when I reach the edge of the bed does Minami look down and begin to understand."
    show minami blush
    minami.say "M...me?"
    minami.say "You want to taste me, big bro?"
    "I just nod in response, making sure that my smile is visibly wolfish as I do so."
    "Minami visibly flinches at the gesture, but I feel her clinging to me all the same."
    "And that's just the reaction I wanted to get out of her."
    "That moment where she's almost like a deer in the headlights."
    "But at the same time, I can feel the desire already building in her body."
    "Of course I want to taste that - it's the very essence of what makes her so desirable!"
    "Minami offers no resistance as I lay her gently down upon the bed."
    "Her eyes are wide and I can hear the sound of her breathing heavily."
    "Yet she makes no move to resist as I slowly and surely strip off her clothes."
    "I swear that I can already smell her scent as soon as she's naked."
    show minami cunnilingus hidden with fade
    "And I have to all but tear my eyes away from the glistening between her thighs."
    "She's already wet down there!"
    "Now it's my turn to strip off my clothes as Minami watches in rapt silence."
    "I try to make it a show for her without acting the fool and ruining the moment."
    show minami cunnilingus closed bite
    "But her eyes are wide, and she's biting her lip so hard that it's almost bleeding."
    "I don't think she'd be put off if I started doing some kind of dance routine!"
    if minami.flags.handcuffs:
        show minami cunnilingus come
    else:
        show minami cunnilingus open
    "By the time I'm naked too, Minami is waving at me with both hands."
    "She's actually beckoning me to come to her - almost begging!"
    "My instinct is to dive on her, right there and then."
    show minami cunnilingus mike nohead closed normal
    "But somehow I manage to hold back and keep up the illusion that I'm the one in control here."
    show minami cunnilingus lickpussy
    "Slowly and as subtly as I can, I begin to lower myself over Minami's naked form."
    "I know that her eyes are on me the whole time, and that makes it so much more thrilling."
    "And when I reach down to part her legs, my touch is as gentle as I can make it."
    show minami cunnilingus hidden
    "All the same, she lets out a little yelp of anticipation."
    "At the sound, I feel my already stiff cock twitch with desire."
    "Jesus Christ - I want her so much right now!"
    "Letting her thighs rest across my arms, I lay my head between them."
    "Minami's pussy is like her in every way possible."
    "Petite, neat and enough to make me fall in love with her all over again."
    "She smells incredible too - sweet and sensual."
    "I close my eyes to better enjoy the scent of her as I open my mouth."
    "And as soon as my tongue touches the folds of her pussy, I can taste her too!"
    "There's that almost indescribable mixture of sweet and sour, like licking a battery."
    "I feel like I can taste Minami's essence in there too, as crazy as that sounds."
    show minami cunnilingus closed
    "It's simple yet complex at the same time, and utterly addictive."
    return

label minami_fuck_date_oral:
    $ game.play_music("music/roa_music/new_days.ogg")
    show minami cunnilingus mike lickpussy hidden
    "Before I know it, I'm licking for all I'm worth, my tongue going ever deeper."
    "I barely hear Minami begin to gasp and moan at my efforts."
    "And the way her body twitches around me is nothing more than a faint distraction."
    minami.say "Oh shit..."
    minami.say "Big bro..."
    "All Minami's words do is make me more determined to push on."
    "And so I push my tongue still deeper into her pussy, feeling her part for me."
    "There are no more words from Minami now, just the sound of pure, unadulterated pleasure."
    menu:
        "Use my tongue":
            show minami cunnilingus closed
            "I could get fancier with what I'm doing."
            "Maybe play with Minami's ass or get toys involved too."
            "But all I want right now is to keep on exploring her with my tongue."
            "By now, Minami's thighs are almost resting on my shoulders."
            "My lips are pressed against the lips of her pussy."
            "She's all I can taste and all that I can smell too."
            "I can feel my tongue beginning to tire from the attention I'm giving her."
            "But it doesn't stop me for as much as a single second."
            show minami cunnilingus wet orgasm
            "Even if it goes numb and I lose all feeling in my entire face, I'll keep on going."
            "I vow to myself that I won't stop until I push Minami over the edge."
            "Perhaps that's helped by the way I can feel the sheets moving beneath me."
            "Minami's practically writhing now, grabbing handfuls of the bedclothes."
            "At this rate, she'll either cum soon or else roll straight off the bed!"
            $ minami.love += 1
        "Finger her ass" if hero.sexperience >= 30:
            "I can feel Minami moving beneath me as I work on her pussy."
            "Her ass is lifting off of the mattress each and every time too."
            "Which means that her pert little buttocks are raised just enough for me to..."
            show minami cunnilingus awkward
            minami.say "Wha..."
            minami.say "What are you..."
            show minami cunnilingus fingerass nohead
            "I can't blame Minami for the surprise in her voice as she comes back down."
            "After all, how could she have known there would be a finger waiting to sink into her ass?"
            show minami cunnilingus hidden wet normal
            minami.say "Mmm..."
            minami.say "Oooh..."
            "I feel the muscles of her ass quiver as they're forced to take my finger in."
            show minami cunnilingus lickpussy
            "The sensation of it spreads throughout the rest of Minami's body too."
            "I swear I can even feel it on the tip of my tongue!"
            show minami cunnilingus closed orgasm
            "And when she instinctively moves to raise herself, I press my tongue into her in response."
            "Soon she's trapped between the two, moving from one forcing her onto the other."
            "I can feel Minami getting close to the edge, getting ready to cum."
            "She has the bedclothes clenched in her hands."
            "And she's fighting just to keep her back on the mattress."
            $ minami.sub += 1
        "Use the dildo" if hero.has_item("dildo"):
            show minami cunnilingus lickpussy
            "It's only now that I recall where I dropped one of the sex toys that I own."
            "If my memory serves me right, it should be within easy reach."
            "I pause for a moment, feeling around with one hand."
            "And it's just as Minami seems to notice my distraction that my fingers close around it."
            minami.say "H...hey, big bro..."
            minami.say "What's up?"
            "Her expression was puzzled to begin with."
            "But when she sees the dildo that I have in my hand, Minami's eyes go wide."
            minami.say "Wha..."
            minami.say "What are you gonna do with that?!?"
            "I smile at what seems like such a dumb question, shaking my head a little."
            show minami cunnilingus dildopussy nohead
            "And then I give Minami her answer by stroking the dildo against the folds of her pussy."
            show minami cunnilingus awkward hidden
            "She yelps in barely suppressed arousal."
            "And I surprise her by pushing it inside a mere second later."
            show minami cunnilingus vibrate
            minami.say "Oooh..."
            minami.say "Mmm..."
            show minami cunnilingus orgasm closed
            "It only takes a moment for Minami's initial surprise to pass."
            show minami cunnilingus dildowet
            "And then she melts under the touch of the dildo as it fills her pussy."
            show minami cunnilingus lickpussy
            "I keep on licking at the edges of her lips as I work the thing in and out of her."
            "I can feel Minami getting close to the edge, getting ready to cum."
            "She has the bedclothes clenched in her hands."
            "And she's fighting just to keep her back on the mattress."
            $ minami.love += 1
            $ minami.sub += 1
        "Use dildo and my finger." if hero.has_item("dildo") and hero.sexperience >= 30:
            show minami cunnilingus lickpussy
            "Suddenly I remember what's lying under the bed."
            "I know just where it is and that it should be close to my hand."
            "I stop what I'm doing to grope around under the bed."
            "Minami seems to notice my distraction just as I lay my hand on it."
            minami.say "H...hey, big bro..."
            minami.say "What's up?"
            "Her expression is one of confusion at first."
            "But it becomes a picture of surprise at the sight of the dildo in my hand!"
            minami.say "Wha..."
            minami.say "What are you gonna do with that?!?"
            "I smile, shaking my head to let her know that I'm not going to answer that question."
            show minami cunnilingus dildopussy nohead
            "Instead I show her, by rubbing the toy against the lips of her pussy."
            show minami cunnilingus awkward hidden
            "She yelps in barely suppressed arousal."
            "And she keeps on making the same noise as I push it into her."
            show minami cunnilingus normal closed
            minami.say "Oooh..."
            minami.say "Mmm..."
            show minami cunnilingus vibrate
            "I can feel Minami moving as I work on her with the dildo."
            "She lifts her ass off of the mattress a little each time she moves."
            show minami cunnilingus closed
            "And that means her tight little buttocks are raised just enough for me to..."
            show minami cunnilingus awkward
            minami.say "Wha..."
            minami.say "What are you..."
            show minami cunnilingus fingerass hidden
            "Hard to blame Minami for sounding surprised as she comes back down."
            show minami cunnilingus dildowet
            "Especially as my finger is waiting to sink into her ass!"
            "I feel her muscles quiver and protest as it's taken in."
            show minami cunnilingus orgasm
            "Soon she's trapped between the finger and the dildo, moving from one forcing her onto the other."
            "I can feel Minami getting close to the edge, getting ready to cum."
            "She has the bedclothes clenched in her hands."
            "And she's fighting just to keep her back on the mattress."
            $ minami.love += 2
            $ minami.sub += 2
    show minami cunnilingus ahegao nohead sweat
    "When Minami finally loses it, I'm in a prime position to watch the show."
    "And it's a pretty impressive one too!"
    "It's almost like she's a sponge that's soaked up all it can."
    "And now she needs to be squeezed out, wrung until there's nothing left!"
    "I get to hold her through every single second of it too."
    show minami cunnilingus ahegao -fingerass -dildopussy -dildowet wet
    "Afterwards, she rests in my arms, slick with sweat and panting heavily."
    "I don't know if she's ever looked better than she does right now."
    mike.say "For the record, Minami - you taste great!"
    show minami cunnilingus normal
    "I see her cheeks flush redder than before."
    "But she's smiling at me, eyes full of affection."
    minami.say "Aww, big bro."
    minami.say "I love being your favourite flavour!"
    return

label minami_hottub_sex_male:
    $ game.active_date.clothes = "swimsuit"
    $ CONDOM = False
    show bg pool with fade
    "It's one of those days when there's nothing you want more than to sit back in the hot-tub and relax."
    "The sun is out, there's not a cloud in the sky and all I have to do is lie back enjoy it."
    "I close my eyes and just listen to the sounds of nature all around me."
    "Sounds that I don't usually notice, softened almost into melody by the distance..."
    show minami swimsuit with dissolve
    minami.say "Hey, big bro!"
    minami.say "Wake up already!"
    "The sound of Minami's voice is sudden and completely unexpected."
    "It jerks me out of my reverie and snaps me straight back to reality."
    "My eyes snap open and I sit straight up, already feeling annoyed."
    "I have my mouth open, ready to tell Minami off for disturbing me."
    "But then my gaze settled on her for the first time."
    "And suddenly all thought of dressing her down is gone."
    "Because she's pretty much undressed already!"
    "I almost gasp at the sight of Minami as she poses by the side of the hot-tub."
    "All she's wearing right now is a bathing suit and a smile."
    "The former shows off every inch of her petite, sexy little figure."
    "And the latter betrays the fact she's enjoying my reaction to the sight."
    show minami tehe
    minami.say "Like what you see, big bro?"
    minami.say "Want a closer look, huh?"
    "Minami gives me a cheeky wink as she starts to climb into the hot-tub."
    "She shoos me over to the other side so that there's enough space for her too."
    minami.say "Move over, big bro."
    minami.say "Make some room for little me!"
    hide minami
    show hottub minami
    with fade
    "It's then that she looks down and sees the effect she's already having on me."
    "Minami lets out a delighted little chuckle, which only seems to make it get harder!"
    minami.say "Ooh, look at that!"
    minami.say "There's hardly room for the both of us AND your cock!"
    "At the mention of my already stiff dick, I somehow snap out of it."
    "All thought of relaxing in the hot-tub simply vanishes from my mind."
    "Now there's nothing else in my thoughts but Minami."
    "Well, Minami and how much I want her right now..."
    mike.say "You think so, Minami?"
    mike.say "Well, I can think of somewhere else we could put it..."
    "Minami's eyes go wide with delight and her chuckles become distinctly dirty."
    "She bites her lip in anticipation as she closes the short distance between us."
    minami.say "Oh, big bro, you dirty boy!"
    minami.say "You want to park your submarine inside of me?"
    "I can only gasp in response, my own eyes going wide too."
    "And that's because Minami's reached under the water and grabbed me."
    "The sneaky little minx - she did that while I was distracted!"
    "My breathing becomes heavy and ragged as she rubs away eagerly."
    minami.say "Mmm..."
    minami.say "It's so big!"
    minami.say "You'll end up sinking me for sure."
    minami.say "But it'll be worth it!"
    "With that, Minami kisses me full on the lips."
    "Her tongue darts into my mouth, probing like an eel."
    "And all the time she's still massaging my painfully stiff cock."
    "She already has my trunks off when I decide I can't wait any longer."
    show hottub sex male minami outside with fade
    call minami_dick_reactions from _call_minami_dick_reactions_2
    "I have to get my cock as deep inside of Minami as I can and as soon as I can!"
    "My hands take hold of her and turn her around, pushing her against the side of the tub."
    "Minami yelps in surprise, but then sighs and lets me have my way with her."
    "My sense of urgency means I don't indulge in any kind of teasing."
    "Instead I simply begin to push my cock into Minami without delay."
    minami.say "Oh..."
    minami.say "Oh, big bro..."
    minami.say "Give it to me...please!"
    "The combination of Minami urging me on while her pussy resists turns me on even more."
    show hottub sex male minami inside
    "And it only takes me a couple more thrusts to push all the way inside of her."
    "Minami quivers and moans as I sink up to my balls, every inch of my cock in her pussy."
    "She looks back over her shoulder, eyes wide and head nodding almost desperately."
    "I begin to thrust in and out of her then, with the same haste and force."
    "But the look on Minami's face only becomes more needy as she takes all I have to give."
    "Her moans have given way to animal sounds of sheer passion by now."
    "She seems to purr as my cock pounds her to within an inch of her life."
    "And to think, all I wanted to do was lie on the hot-tub and relax!"
    call cum_reaction (minami, 'vaginal', 1) from _call_cum_reaction_131
    if _return == "vaginal_outside":
        show hottub sex male minami outside
        "All of a sudden, my cock pops out of Minami's pussy."
        "She jumps and lets out a cry of surprise at the unexpected sensation."
        "I gasp too, feeling that the motion has kicked something off inside of me."
        show hottub sex male minami cumshot with vpunch
        "And so it comes as no great shock to me that I shoot my load a second later."
        with vpunch
        "The cum spatters down on Minami's exposed ass."
        $ minami.sub += 1
        "It runs down her slick thighs and into the water below."
        with vpunch
        "Minami jumps as it hits her, beginning to cum as well."
        "And all I can do is watch as she desperately fingers her pussy."
        "Minami rubs my cum into the lips between her legs, panting the whole time."
        "She holds my eye while she brings herself off."
        "And I see the exact moment that she cums too."
        "Minami looks at me, a helpless expression in her eyes."
        "It's almost enough to make me cum again too!"
    else:
        "I have a firm hold on Minami right now."
        "And there's no way I'm letting go of her until it's over."
        "The sound of our wet skin slapping together is almost as loud as her cries."
        "And every time her buttocks hit my thighs, I grunt in passion too."
        minami.say "Oh..."
        minami.say "Oh shit..."
        minami.say "I'm...I'm gonna cum!"
        "Minami's not kidding either!"
        "Within seconds of gasping the words out, I can feel it beginning."
        "She writhes and wriggles on the end of my cock as her orgasm takes over."
        "But there's nowhere for her to go, so she can only ride it out to the end."
        "I push as hard as I can, trying to make it as intense as possible."
        show hottub sex male minami cumshot with hpunch
        "And in doing so, I lose it almost at the same moment."
        $ minami.love += 1
        with vpunch
        "Which means that we cum close on each other's heels."
        show hottub sex male minami ahegao with vpunch
        "I shoot my load into Minami as she shudders from head to toe."
        "And then all that I can hear is the sound of us both panting as we let go."
    hide hottub
    show hottub minami
    with fade
    "Afterwards, we sink into the water, utterly exhausted."
    "Minami cuddles herself into the crook of my arm without saying a word."
    "And only then do my thoughts turn back to the notion of relaxing."
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ minami.sexperience += 1
    $ game.active_date.clothes = None
    return

label minami_fuck_bathroom:
    $ game.play_music("music/roa_music/new_days.ogg")
    scene bg bathroom with fade
    "I never even realised I had a daily routine until I also realised that Minami was exploiting it."
    "But I guess I just settled into a convenient rhythm and kept it up from one day to the next."
    "It was what she started getting up to while I showered that tipped me off to Minami's scheme."
    "Every time I was in there, washing away the memory of the day, she'd always seem to turn up."
    "At first I just wrote it off as a coincidence, even though there were some pretty heavy hints."
    "Like the fact that she's never be fully dressed when she walked into the bathroom."
    "Or that she's suddenly need to stretch and bend over a hell of a lot too."
    "So eventually, I decided to call her on it..."
    show minami underwear with dissolve
    mike.say "Minami..."
    mike.say "Do you have to do that when I'm showering?"
    minami.say "What's the problem, big bro?"
    minami.say "It never bothered you when we were kids!"
    mike.say "Yeah, but we're not kids anymore - are we?"
    "I hear Minami chuckle at this."
    "And I can just make out her shaking her head through the steamy glass."
    "She's doing something else too, but I can't quite make it out."
    show minami tehe
    minami.say "No, big bro."
    minami.say "We're not kids anymore..."
    "As she says this, Minami opens the shower door."
    show minami naked hunt with dissolve
    "Even through the steam, I can see that she's now naked."
    "She smiles up at me, huge eyes wide and full of mischief."
    "I can see how much she's enjoying the surprise on my face right now."
    "But maybe not as much as I'm liking the look of her hot little body."
    mike.say "You're not wrong there, Minami."
    mike.say "Not wrong at all..."
    "I reach out of the shower cubicle, wrapping my arms around Minami."
    "Sure, she was trying to tease me into doing just that kind of thing."
    "But I move so quickly that she can't help jumping and squealing."
    minami.say "Ah..."
    minami.say "Oooh..."
    minami.say "Mmm...big bro!"
    "A moment later, Minami is in the shower with me."
    "Her neat little body is pressed against mine."
    "I can feel her stiffening nipples on my chest."
    "And my cock stiffens too as she begins to caress it gently."
    "There's no need to say a word."
    "We both know what we want and where this is going."
    "I slowly lower myself down and onto my back, until I'm laid flat."
    scene minami showersex
    show minami showersex outside
    with fade
    "And Minami follows me down, straddling me once I'm down there."
    "Her breasts are pressed into my face, and I take full advantage."
    "She moans as I begin to suck on them, nibbling at her nipples."
    minami.say "Mmm..."
    minami.say "Big bro..."
    minami.say "Put it inside me...please!"
    menu:
        "Fuck her ass":
            "Maybe it's just because we're doing this on the spur of the moment."
            "Or perhaps I just like the idea of making Minami squeal in surprise."
            "Either way, I take a firm hold of her buttocks and part them."
            "And then I push my cock firmly between them."
            minami.say "Oh..."
            minami.say "What are you..."
            "By the time Minami manages to get the words out, it's already too late."
            show minami showersex anal -outside
            "I'm a good inch inside of her and pushing hard to get deeper still."
            "Before she knows it, her muscles have surrendered to my efforts."
            "And they're pulling me in, rather than trying to push me out!"
            minami.say "Mmm..."
            minami.say "That's good, big bro..."
            minami.say "Don't stop now!"
            "As if I needed any encouragement, Minami pushes herself downwards."
            "This means that we're both pushing in the opposite direction."
            "My cock is as deep into her as it can go mere seconds later."
            "And then she starts to ride me like her life depends on it."
            "I hardly have to do any of the work, just lie back and take it."
            "Putting my hands firmly upon Minami's haunches, I do just that."
            "She bucks and sways above me, grinding this way and that."
            show minami showersex pleasure
            "The sight of her body moving, breasts bouncing..."
            "It's amazing - but not as amazing as how it feels."
            "Minami's muscles are squeezing me the whole time."
            "And slight as she is, her weight makes me feel every single movement."
            minami.say "Ah..."
            minami.say "Big bro..."
            minami.say "I'm gonna cum!"
            mike.say "Me..."
            mike.say "Me too!"
            menu:
                "Cum inside":
                    "There's no time to think of changing direction now."
                    "It's too late to do anything but keep right on going."
                    show minami showersex anal creampie with vpunch
                    "I shoot my load into Minami, holding her tight the whole time."
                    show minami showersex ahegao with vpunch
                    "She wriggles and writhes in my grasp, tossing her head this way and that."
                    with vpunch
                    "And then she lowers herself onto me, panting with exhaustion."
                    $ minami.love += 1
                "Pull out":
                    "I just have enough time to lift Minami up..."
                    show minami showersex outside -anal
                    "And that lets my cock pop out of her."
                    show minami showersex outside creampie ahegao with vpunch
                    "Her eyes go wide as I shoot my load on her back."
                    with vpunch
                    "But then she rubs it into her skin as she cums too."
                    with vpunch
                    "All I can do is watch in fascination and pant in exhaustion."
                    $ minami.sub += 1
            $ minami.flags.anal += 1
        "Fuck her pussy":
            "All it takes is a little rearranging down there..."
            "And just like that, I can feel myself pushing into Minami."
            "She's more than ready for me too, anticipating this moment."
            "Which means that there's almost no resistance as I enter her."
            minami.say "Mmm..."
            minami.say "That's right, big bro..."
            minami.say "That's what I want!"
            show minami showersex vaginal -outside
            "I have my hands on Minami's waist, guiding her onto me."
            "And all of a sudden I pull her down without warning."
            "She sinks straight onto my cock, which buries itself inside of her."
            minami.say "Ah..."
            minami.say "Yes...please..."
            minami.say "Fuck me, big bro - please fuck me!"
            show minami showersex pleasure
            "Now how can I resist a request like that?"
            "Still holding Minami tight, I give her what she wants."
            "Short, sharp thrusts from below soon have her moaning."
            "And she becomes almost passive as I begin to do all the work."
            "Minami's pert little breasts bounce and jiggle."
            "Her head flops from side to side too."
            "It's like she's been reduced to the state of a rag-doll."
            "And the only thing keeping her upright are my hands."
            "Well, that and the fact I have my cock buried deep inside of her too!"
            "Suddenly I hear Minami making a different kind of noise."
            "She's gasping, like she's trying to form words."
            minami.say "Ah..."
            minami.say "Big...bro..."
            minami.say "I'm...gonna...cum!"
            mike.say "Me too, Minami..."
            mike.say "Me too!"
            menu:
                "Cum inside":
                    "I don't even think about stopping for a moment."
                    "And Minami is clinging onto me like her life depends on it too."
                    show minami showersex vaginal creampie with vpunch
                    "I let go when I'm as deep inside of her as possible."
                    show minami showersex ahegao with vpunch
                    "And just like that, she tosses her head back and cries out."
                    with vpunch
                    "But then, just as quickly, she collapses onto my chest."
                    $ minami.love += 1
                "Pull out":
                    show minami showersex outside -vaginal
                    "I lift Minami up, letting my cock slip out of her."
                    show minami showersex ahegao with vpunch
                    "Her eyes go wide as her orgasm hits, making her moan at the release."
                    show minami showersex outside creampie with vpunch
                    "At the same time, I cum, shooting it over her back."
                    with vpunch
                    "Minami hovers above me for a moment, still feeling her climax."
                    "And then she collapses onto my chest."
                    $ minami.sub += 1
    $ minami.flags.showersex = True
    $ minami.sexperience += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
