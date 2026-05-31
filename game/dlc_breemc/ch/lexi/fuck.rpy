init python:
    Event(**{
    "name": "lexi_hottub_sex_female",
    "label": "lexi_hottub_sex_female",
    "conditions": [
        HeroTarget(
            IsGender("female"),
            IsActivity("date_hot_tub_home")),
        PersonTarget(lexi,
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

label lexi_hottub_sex_female:
    scene bg pool with fade
    "I've been wanting to do this for a hell of a long time."
    "Wanting to ask Lexi over to spend a little time in the hot-tub."
    "With me, obviously - to spend some time in the tub with me!"
    "But it's kind of hard for me to be confident about it."
    "For some reason, girls like Lexi always scare me a little."
    "It's not because she's got such big boobs or she's so pretty."
    "I'm not hung up on something that stupid - mainly because I'm not a guy!"
    "It's more that she's kind of a bad girl, you know?"
    "Like she's from the wrong side of the tracks."
    "And it's not that I'm scared she's going to rob me either!"
    "I know Lexi's not like that."
    "I guess she kind of makes me feel pretty straight-laced."
    "Like I've lived a sheltered life, unlike the one she's had."
    "Urgh...I'm babbling here!"
    "Look, I'll just come out and say it - I'm worried she'll think I'm pathetic."
    "That she'll think I'm some silly little daddy's girl trying to be rebellious!"
    "I've been trying to keep all of that out of my head as I got the place ready."
    if game.calendar.get_time_of_day() == "evening":
        $ renpy.show(f"hottub_bg_night_left")
    else:
        $ renpy.show(f"hottub_bg_{game.calendar.season_name}_left")
    $ renpy.show("hottub_fg_valentine_left", tag="romantic")
    with fade
    "The lighting is subdued."
    "There are candles dotted around the edge of the tub."
    "I've picked out a nice bottle of wine and put out two glasses."
    "I even went to the trouble of scattering rose petals all over the place."
    "The only problem is that now I'm worried that it's too much!"
    "Should I leave it?"
    "Or should I try to make it less...well, less romantic?"
    lexi.say "Whoa!"
    lexi.say "Will you check this out?"
    lexi.say "Looks pretty fancy, [hero.name]!"
    scene bg pool
    show lexi casual happy at center, zoomAt(1.5, (640, 1040))
    with hpunch
    "At the sound of Lexi's voice, I spin around."
    "And I can't help letting out a yelp of surprise too."
    bree.say "Argh!"
    show lexi surprised at startle
    lexi.say "Argh!"
    hide lexi
    show lexi casual surprised at center, zoomAt(1.15, (640, 800))
    with vpunch
    "Lexi mirrors my cry, and we leap apart."
    lexi.say "What the fuck, [hero.name]?"
    show lexi normal
    lexi.say "I didn't think I was that scary!"
    "I shake my head, trying to get a hold on myself at the same time."
    bree.say "Sorry, Lexi, sorry..."
    bree.say "I was just in a world of my own."
    bree.say "I didn't hear you walk up on me."
    "Lexi seems to understand what I mean."
    show lexi annoyed
    "And she even looks a little ashamed of herself too."
    lexi.say "Ah, yeah..."
    lexi.say "Maybe I should have knocked or something..."
    lexi.say "Not just walked into your yard unannounced!"
    "Oh shit, this is already going south!"
    "I can't have Lexi feeling like she's not welcome around here."
    bree.say "No, Lexi..."
    bree.say "It's okay, really."
    bree.say "I'm just a little nervous, you know?"
    show lexi normal
    "Just as quickly as Lexi's expression changed to one of shame, it changes again."
    "But this time it's to one of genuine amusement, as if I just said something hilarious."
    show lexi happy
    lexi.say "You're nervous, [hero.name]?"
    lexi.say "About little old me?"
    "I get the impression that Lexi's about to burst out laughing."
    "And in that moment I can feel a sense of immense pressure."
    "It's like something's building up inside of me."
    "And I just know that I won't be able to take her laughing at me."
    "So in order to stop that happening, I do something pretty rash."
    hide lexi
    show lexi kiss casual
    with dissolve
    $ lexi.flags.kiss += 1
    "I lean forwards and kiss Lexi."
    "I kiss her full on the lips, with no warning."
    lexi.say "Wha..."
    lexi.say "Mmm..."
    "I know that my body's pretty tense right now."
    "And I can feel that Lexi's is exactly the same."
    "That fills me with doubt, making me think I just did the wrong thing."
    "But a moment later I'm relieved to feel her begin to relax."
    "Even more so, I start to feel Lexi returning the kiss a few seconds later."
    "In fact it doesn't take me long to realise that she's really getting into it."
    "Lexi's hands are wandering all over my body right now."
    "And I can feel her sticking her tongue between my lips."
    "So I guess this thing is really happening!"
    "But I'm surprised when Lexi suddenly breaks away from me, ending the kiss."
    hide lexi kiss
    show lexi flirt at center, zoomAt(1.5, (640, 1040))
    with dissolve
    "I stand there frozen in the same pose, thinking I must look pretty stupid."
    "Yet one glance at Lexi is enough to tell me that she didn't have that in mind."
    lexi.say "C'mon, [hero.name]..."
    lexi.say "What are you waiting for?"
    hide lexi
    show lexi flirt
    with dissolve
    "I watch as Lexi strips of the few clothes that she's wearing."
    "She tosses them aside, not seeming to care where they land."
    $ game.active_date.clothes = "swimsuit"
    show lexi swimsuit with dissolve
    "And I can see that underneath she's wearing a skimpy swimsuit."
    hide lexi with moveoutright
    "Without waiting to see what I'm doing, Lexi then jumps into the hot-tub."
    play sound water_splash
    lexi.say "Bombs away!"
    lexi.say "Ha, ha!"
    "I take an involuntary step backwards as water surges out of the tub."
    "It knocks over most of the candles, extinguishing them in an instant."
    "But none of that seems to bother Lexi in the slightest."
    "Because she ignores the chaos she's causing and makes a grab for the wine."
    show hottub lexi valentine nomc with fade
    lexi.say "Come on, [hero.name]..."
    lexi.say "Get your ass in here too!"
    lexi.say "And maybe get some ice for this booze, yeah?"
    "Part of me wants to tell Lexi off for ruining my carefully planned decor."
    "But a larger part of me is too thrilled by her actions to think of anything else."
    "And that's the part of me that wins out, as I hastily strip off my clothes too."
    "I think about jumping into the hot-tub like Lexi just did."
    "Though in the end common-sense wins out, and I climb in carefully instead."
    show hottub lexi valentine -nomc with dissolve
    "Lexi doesn't seem to appreciate my efforts."
    "She shoots me a raised eyebrow and slides straight over to me in the water."
    "I find a glass of wine, full to the brim, being shoved into my hand."
    lexi.say "Ah, [hero.name]..."
    lexi.say "Don't tell me that one kiss was it!"
    lexi.say "Is that really all that you had in you?"
    "Lexi's getting closer to me all the time as she says this."
    "She's pressing her body against mine."
    "Wrapping my arms and legs with her own too."
    "I try to take a sip of my wine, hoping it might calm my nerves."
    "But Lexi's closeness means that I fumble in my efforts."
    "Instead of a sip, I end up with a mouthful that I swallow straight down."
    "Lexi seems to misread this, assuming that I'm doing it out of bravado."
    "And she takes an equally huge swig of her own wine so as not to be out-done."
    bree.say "Urgh..."
    bree.say "Oh...oh man..."
    bree.say "That's gone straight to my head!"
    lexi.say "Yeah, I know..."
    lexi.say "This is some real good shit, [hero.name]!"
    lexi.say "You really know how to party!"
    "The compliment's pretty crude and Lexi totally misses the point."
    "Yet knowing that she's praising me has a really weird effect."
    "It's like the strength of the alcohol goes through the roof."
    "Or else my own judgement just disappears completely."
    "Oh fuck..."
    "Is this what it feels like to be a guy?"
    "Like you can only think with your pussy like they do with their dicks?"
    "I was supposed to be getting over my issues with Lexi."
    "I was supposed to be getting in control of the situation."
    "But she just makes me want to act on pure, unadulterated impulse."
    bree.say "I'll show you how I party, Lexi..."
    bree.say "Now give me some more of that sugar!"
    "Both our wine glasses clatter onto the decking around the tub."
    "Any other time I'd have been worried about them breaking."
    "But the only thing on my mind right now it getting hold of Lexi."
    "What's really amazing is that I seem to take Lexi by surprise."
    "I'd have thought that this would be pretty normal for her."
    "But maybe she'd already written me off as being shy and passive."
    "This means I end up practically pinning Lexi to the side of the tub."
    "And I don't know if it happens by accident or design on my part."
    "But a moment later, Lexi's swimsuit is pulled down."
    "Which means that her impressive chest is suddenly released."
    "Seriously, I'm not kidding when I say this - they almost slap me in the face!"
    "Lexi's breasts bounce around, and my head's pretty much pushed between them."
    "Though I'm not about to let any of that stop me."
    "Instead I take hold of Lexi's swimsuit, pulling it down further still."
    "At the same time I lean forwards and start to nuzzle at her breasts."
    show hottub sex female lexi with fade
    "Lexi whimpers with pleasure, still too dazed to do anything in return."
    "The most she manages is to begin tugging at the material of my own swimsuit in return."
    "I help her out with this, beginning to shoulder out of it myself."
    "All the while I have one of Lexi's nipples in my mouth."
    "And I'm teasing it with lips, tongue and teeth alike."
    "Pretty soon we're both naked, clinging to each other in the water."
    "But I'm sure that Lexi's the first one to reach down below the waist."
    "The moment I feel the tips of her fingers down there, everything changes."
    "Now I'm no longer the one in charge, as Lexi explores those hidden folds."
    "My lips release her nipple, and suddenly I'm the one gasping with pleasure."
    "I make sure to nod eagerly as Lexi looks me in the eye."
    "Because I'm desperate for her to keep right on with what she's doing to me."
    "Lexi nods too, pulling me in closer, until we're locked together."
    "One of her legs slides between mine, and I feel our lips touch."
    "But this time it's not a kiss, if you know what I mean!"
    "Sensations explode inside of me as Lexi's pussy meets mine."
    "We're both still moving and fingers are everywhere down there."
    "I'm kind of amazed that the result is a steadily building certainty."
    "The sure and unshakable knowledge that I'm about to lose my mind."
    with hpunch
    "And when I finally do cum, I cling to Lexi for all I'm worth."
    with hpunch
    "It's a small relief to see that the same thing is happening to her at the same time."
    with hpunch
    "Together we thrash about in the water, barely keeping each other above the surface."
    "And when it's over, we cling to the side of the tub, exhausted and utterly spent."
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ lexi.sexperience += 1
    $ game.active_date.clothes = None
    scene bg black with dissolve
    return


label lexi_fuck_date_female(location="hero"):
    $ game.room = "bedroom4"
    $ game.play_music("music/roa_music/smile_for_me.ogg")
    call lexi_fuck_date_intro_female (location) from _call_lexi_fuck_date_intro_female
    menu:
        "Go down on her":
            call lexi_fuck_date_bree_cunnilingus (0) from _call_lexi_fuck_date_bree_cunnilingus
        "Let her go down":
            call lexi_fuck_date_lexi_cunnilingus (0) from _call_lexi_fuck_date_lexi_cunnilingus
        "Lick her right here" if hero.sexperience >= 5:
            call lexi_fuck_date_bree_standing_cunnilingus (5) from _call_lexi_fuck_date_bree_standing_cunnilingus
        "Let her take the lead" if hero.sexperience >= 5:
            call bree_licking_lexi (5) from _call_bree_licking_lexi
        "Let her surprise me" if hero.sexperience >= 10:
            call lexi_fingering_bree (10) from _call_lexi_fingering_bree

    if _return == "leave_without_gain":
        return
    $ lexi.sexperience += 1
    if _return == "leave_with_gain":
        return
    hide lexi
    call lexi_sleep_date_fuck_female (location) from _call_lexi_sleep_date_fuck_female
    return

label lexi_fuck_date_intro_female(location="hero"):
    $ result = game.days_played % 2
    if result == 0:
        show bg livingroom
        show lexi smile blush nophone
        with fade
        "The moment Lexi and I make it back to the house, we both know what we want."
        "And there's no need for either of us to speak as much as a single word."
        "I just take hold of her hand and lead her upstairs to my bedroom."
        scene bg bedroom4 with fade
        pause 0.3
        show lexi smile a blush nophone at center, zoomAt(1.0, (840, 720)) with easeinright
        "Lexi keeps a silent look-out as I open the door, and then we slip inside."
        show lexi a at center, traveling(1.5, 0.5, (640, 1040))
        "And once it's closed, we leap into action!"
        "Seriously, it's like someone throws a switch."
        "I pretty much pounce on Lexi, and she's ready to catch me too."
        hide lexi
        show lexi kiss
        with fade
        $ lexi.flags.kiss += 1
        "Our lips meet at the same moment we wrap our arms around each other."
        "And the first chance I get, I slip my tongue into Lexi's mouth."
        "I can feel her hands all over me, just squeezing and caressing at first."
        "But then she starts to pull at my clothes, trying to undress me."
        "It's a clumsy effort, as she can't see what she's doing and she's already distracted."
        "Yet that doesn't stop me from starting to do the same thing in return."
        show lexi kiss underwear with hpunch
        "This strange dance continues, and more than once we almost topple over."
        "But somehow we manage to strip each other down to our underwear."
        show lexi kiss naked with hpunch
        "Finally, Lexi almost tears my bra off me, spilling my breasts."
        "And I haul down her panties, revealing her already wet slit!"
        hide lexi kiss
        show lexi a naked flirt nophone at center, zoomAt(1.5, (640, 1040))
        with fade
        "Both of us step back, breaking the kiss as we pant for breath."
        show lexi c flirt
        "I can see the way Lexi's looking at me right now."
        "Like she's starving and I'm the meal that could save her life!"
        "And I've got to admit, the way I'm staring at her is pretty much the same."
        "Her eyes follow my breasts as they sway from side to side."
        show lexi c normal blush
        lexi.say "W...well..."
        lexi.say "Are we going to do it?"
        lexi.say "Or what?"
        show lexi c smile
        "The sound of forced bravado in Lexi's voice makes me smile."
        "But I keep myself from laughing, instead nodding my head."
        bree.say "Oh yeah, Lexi."
        bree.say "Don't you worry."
        bree.say "We're going to get it on!"
        "I take a step backwards as I pull down my panties."
        "Turning my back on Lexi, I toss them straight at her."
        show lexi a at startle
        "She flinches, but still manages to catch them."
    else:
        show bg livingroom
        show lexi a smile blush nophone at center, zoomAt(1.0, (640, 720))
        with fade
        "I'm pretty eager to get into the house and up the stairs to my bedroom right now."
        "After all, Lexi and I just had a great time together on our date."
        "And neither of us is ready for it to come to an end just yet."
        show lexi a at center, traveling(1.5, 0.5, (640, 1040))
        "But all the same, I'm struggling to keep up with Lexi as she pulls me along."
        show lexi a normal
        lexi.say "Come on, [hero.name]..."
        lexi.say "What's keeping you?"
        show lexi a smile
        "Right now Lexi has hold of my wrist, and she's pulling me after her."
        "And it's not like I'm trying to hold back or dragging my heels."
        "It's just that she's somehow moving faster than I can manage."
        bree.say "N...nothing, Lexi..."
        bree.say "I'm coming as fast as I can!"
        "Luckily for me, Lexi seems to remember which door leads to my bedroom."
        show bg bedroom4 with fade
        "So we end up barrelling into mine, rather than Sasha or [mike.name]'s!"
        "But the moment that we're through the door, she's on me again."
        show lexi a normal blush
        lexi.say "Hurry up, [hero.name]..."
        lexi.say "You need to get naked!"
        show lexi a smile
        "Lexi's hands are all over me, even before I have the door closed behind us."
        "And somehow she's already managed to take off half of the things I'm wearing!"
        if hero.morality >= 25:
            bree.say "Oh my goodness, Lexi..."
            bree.say "Will you slow down just a little?"
        elif hero.morality <= -25:
            bree.say "Good job, Lexi..."
            bree.say "Make sure you take off the rest too!"
        else:
            bree.say "Bloody hell, Lexi..."
            bree.say "You're unstoppable tonight!"
        "I do all that I can to help Lexi pull off the rest of my clothes."
        show lexi naked with dissolve
        "And then I return the favour, stripping her naked as well."
        "But the moment I open my mouth to say something, Lexi takes hold of my hand again."
        "Though this time she's dragging me across the room and towards my bed."
        "The distance is much shorter, and now I'm totally on the same page."
        "So we make it there in mere seconds, Lexi pushing me down onto the mattress."
        "I'm expecting her to keep going, to have me lie down so that she can climb on top."
    return

label lexi_fuck_date_bree_cunnilingus(sexperience_min):
    bree.say "Lexi...Honey, I want you to lean on the bed."
    show lexi surprised blush
    lexi.say "W-what?"
    bree.say "Do you trust me?"
    show lexi normal
    lexi.say "Y-yeah, what's this about [hero.name]?"
    show lexi smile
    bree.say "I'm going to show you I'm serious about this... and that I want it just as much as you do."
    $ lexi.love += 1
    "I give her a smile."
    bree.say "Now be the adorable good girl that you are, and lean on the bed."
    show lexi normal
    lexi.say "Yes... baby."
    scene bree cunnilingus lexi
    show bree cunnilingus lexi nomc
    with fade
    "Lexi obeys and sit on the poolside again, her wet naked body is just everything I want right now, seeing those huge naked breasts of hers, her beautiful butt and that wet... Focus [hero.name]!"
    bree.say "Spread your legs, show me that beautiful pussy..."
    "Lexi smiles seductively and opens up her legs, showing me all of herself. She's so beautiful. She's so sexy..."
    show bree cunnilingus lexi suck -nomc with fade
    "And she's mine. I smile back up at her before going down to do my work. Gently I kiss along on the sides, slowly making my way lower from her leg towards that sexy shaved entrance."
    show bree cunnilingus lexi lick with fade
    "She's moaning slightly, letting them escape every few seconds. Finally reaching her prize, I kiss her lips over and over, licking, probing at the entrance."
    show bree cunnilingus lexi lick down backward
    pause 0.1
    show bree cunnilingus lexi lick middle
    pause 0.1
    show bree cunnilingus lexi lick up
    "She is beginning to shake and shudder. I reach up, and interlock her hand with mine; she knows I'm with her, she knows I'm there to love her."
    $ lexi.love += 1
    show bree cunnilingus lexi lick middle
    pause 0.2
    show bree cunnilingus lexi lick down
    pause 0.1
    show bree cunnilingus lexi lick middle
    pause 0.1
    show bree cunnilingus lexi lick up pleasure
    lexi.say "Ohhhh.... Ahhhh... [hero.name].... D-Don't... stop... don't you dare stop"
    show bree cunnilingus lexi lick middle
    pause 0.2
    show bree cunnilingus lexi lick down
    pause 0.1
    show bree cunnilingus lexi lick middle
    pause 0.1
    show bree cunnilingus lexi lick up
    "It's all I need to hear, I pick up the pace and lick her more, letting my tongue slip inside before pushing two of my fingers inside gently. Thank God I did my nails before!"
    show bree cunnilingus lexi lick middle
    lexi.say "AHHHH, yes! I love this! [hero.name] I love it so much!"
    show bree cunnilingus lexi lick middle
    pause 0.2
    show bree cunnilingus lexi lick down
    pause 0.1
    show bree cunnilingus lexi lick middle
    pause 0.1
    show bree cunnilingus lexi lick up normal
    "Lexi looks at me and I meet her gaze as well, while her pussy is still in my mouth, I kiss her down there a few more times before stopping, and smiling at her."
    show bree cunnilingus lexi lick middle
    pause 0.2
    show bree cunnilingus lexi lick down
    pause 0.1
    show bree cunnilingus lexi lick middle
    pause 0.1
    show bree cunnilingus lexi lick up
    pause 0.1
    show bree cunnilingus lexi lick -up
    bree.say "Still think you're forcing anything?"
    show bree cunnilingus lexi lick middle
    pause 0.2
    show bree cunnilingus lexi lick down
    pause 0.1
    show bree cunnilingus lexi lick middle
    pause 0.1
    show bree cunnilingus lexi lick up
    lexi.say "No babe... B-But I do want more."
    show bree cunnilingus lexi lick -up
    bree.say "Coming right up~"
    lexi.say "You have no idea how... AIIIEEE!!!"
    show bree cunnilingus lexi lick down pleasure
    pause 0.1
    show bree cunnilingus lexi lick middle
    pause 0.1
    show bree cunnilingus lexi lick up at startle(0.05,-10)
    "Without much of a warning I pick back up where I left off, picking up the pace while I'm at it."
    show bree cunnilingus lexi lick middle
    pause 0.2
    show bree cunnilingus lexi lick down
    pause 0.1
    show bree cunnilingus lexi lick middle
    pause 0.1
    show bree cunnilingus lexi lick up at startle(0.05,-10)
    "My tongue traces over her folds, my fingers go back and forth. Lexi is just laying back as her whole body is twitching, I can tell she's close..."
    show bree cunnilingus lexi lick middle
    pause 0.2
    show bree cunnilingus lexi lick down
    pause 0.1
    show bree cunnilingus lexi lick middle
    pause 0.1
    show bree cunnilingus lexi lick up frontward ahegao with vpunch
    lexi.say "[hero.name] I-....I'm CUMMING!"
    show bree cunnilingus lexi lick middle
    pause 0.2
    show bree cunnilingus lexi lick down
    pause 0.1
    show bree cunnilingus lexi lick middle
    pause 0.1
    show bree cunnilingus lexi lick up with vpunch
    "I give her a thumbs up with my free hand and giving her the one final show to send her to a galaxy far far away. She jolts upright, grabbing the back of my head and pushing me deeper into her pussy and between her legs."
    show bree cunnilingus lexi lick middle back
    pause 0.2
    show bree cunnilingus lexi lick down
    pause 0.1
    show bree cunnilingus lexi lick middle
    pause 0.1
    show bree cunnilingus lexi lick up with vpunch
    "With a yelp and a moan, she releases all over my mouth. Laying back down on the sheets of the bed, panting and trying to regain her breath."
    show bree cunnilingus lexi suck front frontward pleasure with fade
    "I climb and lay next to her, and then over her. Rubbing my body against hers, pressing myself on top of her, I lean in to kiss her, my mouth is dripping with her fluids. The kiss deepens for a moment, and then I break away."
    lexi.say "T-that...was..."
    bree.say "Me too~"
    scene bg bedroom4
    show lexi normal blush naked nophone at center, zoomAt (2.0, (640, 1300))
    with fade
    lexi.say "C-can I...?"
    bree.say "You always can, besides... you're gonna return the favor in the shower~"
    show lexi surprised
    bree.say "Yeah I can tease back too."
    show lexi happy
    lexi.say "For you babe... Any time and always."
    show lexi smile
    "I smile gently, leaning in for another kiss."
    return

label lexi_fuck_date_bree_standing_cunnilingus(sexperience_min):
    "Lexi doesn't hesitate, she leans forwards and kisses me."
    hide lexi
    show lexi kiss naked at flip
    with fade
    $ lexi.flags.kiss += 1
    "And I don't mean she pecks me on the cheek."
    "She full-on plants her lips on mine!"
    "My eyes are wide open with the shock of it."
    "And I know just what I have to do next."
    "The sensation of Lexi kissing me just feels so right."
    "It's like it answers all of my questions at once."
    "I part my lips and feel her tongue dart into my mouth."
    "And then I'm kissing her back, with just as much passion."
    "Lexi's hands are all over me, stroking and caressing."
    "Soon enough I'm returning the favour, exploring her body too."
    "When I touch her below the waist, she breaks off the kiss."
    hide lexi
    show lexi a nophone smile blush naked at center, zoomAt (2.0, (640, 1300))
    with fade
    "I hear her panting, almost desperate for my touch."
    show lexi a sadsmile
    lexi.say "Oh shit...[hero.name]..."
    lexi.say "You're so fucking hot..."
    lexi.say "I'm SO wet for you!"
    show lexi a smile
    "Now all I can think about is what lies between Lexi's legs!"
    show lexi a at center, zoomAt (2.0, (840, 1300)) with ease
    "And so I push her gently up against the wall."
    hide lexi
    show bree lick lexi naked mc_naked bedroom
    with fade
    "Then I kneel down in front of her."
    "I feel like I have no control over my actions."
    "Like I couldn't stop myself, even if I tried."
    "Lexi gasps, but she makes no attempt to stop me."
    "The scent of her pussy fills my senses."
    "It's musky and sweet, impossible to resist."
    "I close my eyes before the tip of my tongue touches her."
    "So all I have to go on is touch and taste."
    "That and the sounds that Lexi makes as I begin to lick at her."
    "They're not words exactly, more like whimpering sounds."
    "And they urge me on, mingling with the taste of her on my tongue."
    "I don't take my time, I can't as we're in a public place."
    "So I lap and lick at Lexi with a desperation and hunger."
    "I can't resolve the unspoken attraction between us with words."
    "But I seem to be able to use my tongue in another way entirely."
    "And it's already getting me results!"
    "Lexi is having to hold herself up against the wall."
    "She's breathing like she just ran a marathon too."
    "I admit I'm not an expert when it comes to this kind of thing."
    "So I simply try to do to Lexi what I'd like to experience in her position."
    "Almost the same moment I plunge my tongue into her pussy, she starts to quiver."
    lexi.say "F...fuck..."
    lexi.say "[hero.name[0]]...[hero.name]..."
    lexi.say "Where'd you learn to do that?!?"
    hide bree
    show lexi c nophone normal blush naked at center, zoomAt (2.0, (640, 1300))
    with fade
    "I stand up and lean in close, helping Lexi make herself decent."
    "Her hands are shaking, and she's still gasping for breath."
    bree.say "Aw...I can't share all my secrets with you, Lexi."
    bree.say "That'd spoil the fun of trying them out on you!"
    return

label lexi_fuck_date_lexi_cunnilingus(sexperience_min):
    scene bg black
    show lexi cunnilingus bree back
    with fade
    "But instead Lexi keeps me sitting up, then slides around behind me."
    lexi.say "Oh no..."
    lexi.say "No laying down on the job for you!"
    "Lexi's leaning over my shoulder as she says this, looking me in the eye."
    "Which means that all of my attention is on her in that moment."
    "So I don't see that she's reaching around with her arms at the same time."
    show lexi cunnilingus bree chest
    "In fact the first thing that I know about it is when she takes hold of my breasts!"
    bree.say "Wha..."
    bree.say "Huh..."
    bree.say "Oh..."
    "Don't get me wrong, this is far from the first time someone touched my boobs!"
    "But in the past I've been more used to people making a dash for me during foreplay."
    "And some folks seem to forget that they're not just a pair of fun-bags to be squeezed."
    "But Lexi instead treats them with respect, remembering they're a part of my body."
    "She caresses and massages them, not gently, but in a way that feels so good."
    "And she only begins to tease at the nipples once she feels me relax in her arms."
    "That sense of release seems to be something that she recognises for what it is."
    "Because from that point on, I feel like I'm totally surrendering."
    "Like I'm putting myself totally in Lexi's hands, to do with as she likes."
    "Which is why I offer not a hint of resistance as one of her hands moves downwards."
    "I feel that hand travel over the curve of my belly, then over my thigh."
    "From there it slides between my legs, seeking for a certain something."
    show lexi cunnilingus bree finger
    if hero.morality >= 25:
        bree.say "Oh, Lexi!"
    elif hero.morality <= -25:
        bree.say "Fuck yeah..."
    else:
        bree.say "Mmm...oh yeah!"
    "A moment later, Lexi's fingers are tickling and teasing the edges of my pussy."
    show lexi cunnilingus bree suck
    "And even her touching so gently beside it is enough to send shivers through me."
    "But still, Lexi keeps things moving slowly, moving inwards a little at a time."
    "That way she makes sure that I'm totally at her mercy, by fractions of an inch."
    "I can't help squeezing my eyes tightly shut as she begins to move inwards."
    "And little by little, the tips of her fingers find their way inside of me."
    show lexi cunnilingus bree smile
    lexi.say "Oh, [hero.name]..."
    lexi.say "This little pussy of yours..."
    lexi.say "It's so hungry, like it's trying to pull me inside!"
    "There's no way I can hope to offer any words in response."
    "As I still have my eyes closed and my senses are being overwhelmed."
    "The best I can manage is to nod my head and give a helpless whimper."
    "All of which seems to be more than enough to satisfy Lexi."
    lexi.say "You know what..."
    lexi.say "It looks as good as your mouth, [hero.name]."
    lexi.say "Good enough for me to want to kiss it too!"
    "I feel Lexi begin to move, and at the same time my eyes pop open."
    "So the first thing I see is her slithering around my side."
    "And by that I mean she moves almost like a snake."
    show lexi cunnilingus bree front with fade
    "One moment Lexi's behind me and the next she's crouched in front."
    "I'm way too disoriented and drunk on pleasure to know how she did it too."
    "All I know is that her head is now descending between my thighs."
    "And I barely have enough time to realise what that means."
    show lexi cunnilingus bree closed
    "Barely enough time to realise before a new wave of pleasure hits me."
    "When this one washes over me, I almost topple onto my back too."
    "For a few confused seconds I'm not sure what Lexi's doing to my down there."
    "I know that she must be using her tongue and lips."
    "But I swear it feels like there's an amorous squid on the loose between my legs."
    show lexi cunnilingus bree opened
    "And even when I do look down, all that I can see is the top of Lexi's head."
    "That leaves me unable to say a word or move from the spot."
    "All of my efforts go into holding myself up in a sitting position."
    "Perhaps it'd be a relief to collapse onto my back."
    "But my fear is that doing so would make Lexi stop what she's doing."
    "And the moment the thought pops into my head, I feel her tongue go deeper than ever."
    "Which makes me dismiss the notion totally, steeling myself to hang on to the end."
    "The only problem is that I'm not sure when that will come."
    "In fact I'm not sure how long we've been going either."
    show lexi cunnilingus bree closed at startle(0.05,-10)
    "Time seems to lose all meaning, replaced by constant pleasure."
    "Lexi turns my body into one giant knot of delightful tension."
    show lexi cunnilingus bree at startle(0.05,-10)
    "Getting tighter and tighter the whole time."
    "Until there's just no way that I can take any more."
    show lexi cunnilingus bree opened at startle(0.05,-10)
    "Finally the dam breaks and I feel myself losing it."
    show lexi cunnilingus bree closed with vpunch
    "And when that happens the last of my strength disappears too."
    "My arms can no longer hold me up, and so I collapse backwards."
    show lexi cunnilingus bree opened with vpunch
    "But even when I land on the mattress, Lexi still doesn't stop."
    "Helpless and unable to speak, I have to lie there as she presses on."
    show lexi cunnilingus bree closed with vpunch
    "Before she's satisfied, I swear that Lexi makes me climax at least twice more."
    "So that when she finally lifts her head, I look like I've been knocked-out."
    show lexi cunnilingus bree opened
    "I can hear her saying something to me, even see her looming over me too."
    "But there's nothing I can do to respond or even acknowledge her."
    show lexi cunnilingus bree closed
    "All I'm capable of doing is lying there, waiting to recover."
    "That and hoping Lexi's still waiting for me when I do."
    return

label bree_licking_lexi(sexperience_min):
    "Lexi's one of those girls who always seems to be wearing next to nothing."
    "So much so that I thought I'd already seen it all before she stripped off."
    "And sure, the process of her doing so is over in the blink of an eye."
    "But the moment that she's standing unclothed before me, I realise that I was dead wrong."
    "Because the sight of her naked body is more than enough to make my eyes go wide."
    "As well as rendering me totally speechless too."
    show lexi normal
    lexi.say "Ha!"
    lexi.say "I know that look, [hero.name]..."
    lexi.say "I've seen it before enough times."
    show lexi happy
    lexi.say "That's the look of someone that likes what they're seeing!"
    show lexi smile
    "I was in the process of taking off my own clothes as Lexi started to strip-off."
    "But it's only now that I realise I've stopped, just over halfway through the process."
    "And all that I can manage to do in response to what Lexi's saying is slowly nod my head."
    "Though, all the same, that seems to be more than enough to please her."
    "Because she closes the short distance between us and begins to help me out."
    "Tugging at the last of my clothes until they're strewn around me on the floor."
    show lexi normal
    lexi.say "There you go, [hero.name]..."
    lexi.say "Now we're a matching pair!"
    lexi.say "And talking about pairs..."
    show lexi smile
    "I blush as Lexi reaches up an starts to touch my breasts without asking for permission."
    "But the sensation of her touch is more than enough to keep me from being able to protest."
    "Not that I think I would have done, as my entire body begins to quiver in response."
    "And Lexi seems to know exactly what she's doing, caressing my nipples as they quickly harden."
    show lexi normal
    lexi.say "You know, [hero.name]..."
    lexi.say "It's totally fine if you want to keep quiet all the way through."
    lexi.say "But I'm not gonna let you get away with not using your mouth at all."
    show lexi smile
    "I can't help blinking as I stare at Lexi, wondering what she can mean by that."
    "She seems to be able to read the expression on my face perfectly though."
    "As a moment later, I feel one of her hands leave my breasts."
    "It slides down, over the flat plane of my stomach and then below my waist."
    "And I let out a gasp of surprise as its fingers begin to stroke between my thighs."
    bree.say "Ah..."
    bree.say "Mmm…"
    show lexi normal
    lexi.say "Oh yeah, [hero.name]..."
    lexi.say "I think you get what I mean, don't you?"
    show lexi smile
    "I'm biting my lip as I nod, letting Lexi know that I'm on the same page as her."
    "And when she puts a hand on my shoulder, I let myself be pushed downwards."
    scene bree licking lexi with fade
    "Not stopping until I've sunk all the way down and onto my knees before her."
    "It's kind of crazy that things are happening this way."
    "That I'm letting Lexi all but point me in the direction of what she wants."
    "Though maybe a large part of that is because I'm realising it's what I want too."
    "Because I can already catch the scent of Lexi's pussy as I lean in towards it."
    "And I can see the way that the light is making the folds of it glisten too."
    "All of which means that she's more than ready for what I'm about to do to her."
    "The thought of her wanting it really makes me want it too, spurring me into action."
    "My own lips part and the tip of my tongue emerges from between them."
    "And I start to kiss at Lexi's pussy, as if I was kissing her mouth."
    "Gently at first, not using anything more than lips and the tip of my tongue."
    "I plant gently pecks here and there, exploring her more than anything."
    "This close the scent of her is almost intoxicating, musky and sweet."
    "Wherever my tongue touches, I taste her too, and it makes me shudder."
    "That odd combination of sourness and compelling delight, like liking a battery and feeling a jolt."
    "Above me, I can hear Lexi starting to gasp and moan as I go further and probe deeper."
    show bree licking lexi closed with dissolve
    "To me it sounds like she's trying her best to remain in control."
    "But already I can feel her pressing herself forwards in an effort to push onwards."
    "And the knowledge that she's beginning to melt at my touch instils me with confidence."
    "Pushing my tongue out further, I circle Lexi's pussy and move inwards at the same time."
    "Doing the best I can to describe a spiral into the soft hold before me."
    "Lexi's really moaning now, propping herself against the wall with one hand as she leans over me."
    "And I see that the other hand is clutching at one of her breasts too."
    "Out of the corner of my eye, I watch as it cups the heavy orb."
    "Her fingers pinching at the already stiff nipple, as if seeking release."
    "By now my tongue is almost as deep into Lexi's pussy as I can get it."
    "Man, what I wouldn't give for the kind that a frog has right now."
    "Just to be able to spool it out until I was all the way inside of her."
    "But I figure that there's still more that I can do to push Lexi further."
    "And with that in mind, I reach up and take hold of her other breast."
    "Lexi nods desperately as I start to squeeze and massage it in the palm of my hand."
    "All the while I'm still licking away at her for all I'm worth."
    "My tongue is going in and out now, curling like a snake."
    "So one moment it's all the way inside of Lexi's pussy."
    "And the next it's folded in my mouth, lapping at her clit."
    show bree licking lexi normal
    lexi.say "B...[hero.name]..." with hpunch
    lexi.say "Please..."
    lexi.say "I can't...can't take it!"
    "I can't describe how hearing Lexi stutter out those words makes me feel."
    "I know that she's been everywhere and done everything when it comes to the bedroom."
    "So the know that I've managed to get her into such a state is totally mind-blowing."
    show bree licking lexi pleasure
    "Finally Lexi throws her head back and lets out a cry of sheer ecstasy." with hpunch
    "Letting me know that she's reached the limit of her stamina." with hpunch
    "And that I've gotten the job done down here too." with hpunch
    return

label lexi_fingering_bree(sexperience_min):
    "Truth be told, I'm still more than a little scared at being alone with Lexi like this."
    "It's not that I don't trust her as a person or that I think she'll do anything bad to me."
    "More that I know she's seen and done things that I probably couldn't even imagine in the bedroom."
    "Hell, I bet that Lexi's done it in place that I wouldn't think it was physically possible!"
    "And I guess I'm worried that she's going to do something that totally takes me by surprise."
    "Which she then proceeds to do, no more than a second later."
    "Lexi's one of those girls who always seems to be wearing next to nothing."
    "So much so that I thought I'd already seen it all before she stripped off."
    "And sure, the process of her doing so is over in the blink of an eye."
    "But the moment that she's standing unclothed before me, I realise that I was dead wrong."
    "Because the sight of her naked body is more than enough to make my eyes go wide."
    "As well as rendering me totally speechless too."
    show lexi normal
    lexi.say "Ha!"
    lexi.say "I know that look, Bree..."
    lexi.say "I've seen it before enough times."
    show lexi happy
    lexi.say "That's the look of someone that likes what they're seeing!"
    show lexi smile
    "I was in the process of taking off my own clothes as Lexi started to strip-off."
    "But it's only now that I realise I've stopped, just over halfway through the process."
    "And all that I can manage to do in response to what Lexi's saying is slowly nod my head."
    "Though, all the same, that seems to be more than enough to please her."
    "Because she closes the short distance between us and begins to help me out."
    "Tugging at the last of my clothes until they're strewn around me on the floor."
    show lexi normal
    lexi.say "There you go, Bree..."
    lexi.say "Now we're a matching pair!"
    lexi.say "And talking about pairs..."
    show lexi smile
    "I blush as Lexi reaches up an starts to touch my breasts without asking for permission."
    "But the sensation of her touch is more than enough to keep me from being able to protest."
    "Not that I think I would have done, as my entire body begins to quiver in response."
    "And Lexi seems to know exactly what she's doing, caressing my nipples as they quickly harden."
    show lexi normal
    lexi.say "You know, Bree..."
    lexi.say "It's totally fine if you want to keep quiet all the way through."
    lexi.say "Just lie back and put yourself in the palm of my hand, okay?"
    show lexi smile
    "I can't help blinking as I stare at Lexi, wondering what she can mean by that."
    "She seems to be able to read the expression on my face perfectly though."
    "At a moment later, I feel one of her hands leave my breasts."
    "It slides down, over the flat plane of my stomach and then below my waist."
    "And I let out a gasp of surprise as its fingers begin to stroke between my thighs."
    bree.say "Ah..."
    bree.say "Mmm…"
    show lexi normal
    lexi.say "Oh yeah, Bree..."
    lexi.say "I think you get what I mean, don't you?"
    show lexi smile
    "I'm biting my lip as I nod, letting Lexi know that I'm on the same page as her."
    scene lexi fingering bree with fade
    "Because I can now feel the sensation of her fingers, slowly circling my pussy!"
    "My instinct is to move backwards, either out of fear or sheer sensual overload."
    "But the moment I take a step away from Lexi, my back is flat against the door."
    "And she follows me, a knowing smile spreading across her face as she does so."
    lexi.say "Uh, uh, uh..."
    lexi.say "No getting away from me that easily!"
    bree.say "I..."
    bree.say "I wasn't trying to..."
    show lexi fingering bree closed with hpunch
    bree.say "Urgh!"
    "Lexi stifles my attempts to protest my innocence with a single finger."
    "Pushing it deeper than before, and all the way into my now willing pussy."
    "Because while my brain might be holding back, my body is in a state of total surrender."
    "Which means that I feel Lexi's finger slide smoothly into me."
    "Pushing my lips aside and pressing against the walls of my pussy."
    "Now I really am glad to have the door against my back."
    "And that's because it means I have something to hold me up."
    "Lexi doesn't let up either, but instead presses on with what she's doing."
    "The finger already inside of me begins to move back and forth."
    "Like it's crooking and beckoning inside of me to some unseen party."
    "At the same time her other fingers are teasing the folds on the outside."
    "Slipping and sliding around as I get ever more wet and slick."
    "What she's doing to me seems to manifest itself in my senses as a series of waves."
    "Each emanating out from the centre of my body and moving outwards to swamp me."
    "When it reaches the limits of my perceptions, it doesn't fade into nothingness."
    "Instead the remnants of it fall back in on me, colliding with the next wave going out."
    "Thus I soon feel like I'm caught in the middle of a tidal plane of sheer pleasure."
    "At first I could guess what fingers Lexi was using and where they were going."
    "But now I just feel like the whole of my pussy is turning into putty."
    "And that her deft digits are melting into my as they stroke and massage."
    "When I look up and meet Lexi's eye, she seems to be able to see straight into me."
    "To read the thoughts that are bouncing around inside of my head."
    "Maybe it's that feeling that pushes me over the edge."
    "Or maybe Lexi starts to do something new that I totally fail to notice."
    "But either way, the waves of pleasure I'm feeling are now more like a tsunami."
    bree.say "L...Lexi..." with hpunch
    bree.say "I'm going to..."
    lexi.say "To cum?"
    lexi.say "Of course you are..."
    lexi.say "That's the whole idea!"
    show lexi fingering bree closed with hpunch
    "I all but collapse against the door as my climax begins to take hold."
    show lexi fingering bree pleasure with hpunch
    "And for the first time, I think I understand why some call it 'the little death'."
    show lexi fingering bree ahegao with hpunch
    "Because it feels like everything else in the world is on hold while it takes me."
    "Like the waves before, it begins between my thighs and spreads quickly outwards."
    "But this is more like the blast of an atomic bomb, flattening everything in its path."
    "And once it's done, I feel pretty much devastated too!"
    "So much so that Lexi has to help to hold me up, or else I'd be in a heap on the floor."
    "A fact that she seems to derive much amusement and pleasure from too!"
    return


label lexi_sleep_date_fuck_female(location="hero"):
    if game.hour > 19 or game.hour < 6:
        scene bg bedroom4
        show lexi a naked nophone
        with fade
        if lexi.is_sex_slave:
            lexi.say "May I share your bed tonight, Master?"
        else:
            lexi.say "Mmm...you cool with me spending the night here?"
        menu:
            "No":
                bree.say "No...I have to be up really early in the morning."
                "The sex was beyond incredible, but now I want to be alone."
                show lexi a sad
                "Lexi frowns in disappointment, clearly trying to shrug off the sense of rejection."
                show lexi a sadsmile
                lexi.say "Okay...sleep well, I guess."
                hide lexi with easeoutright
                "She shakes her head as she collects her things and leaves my bedroom."
                $ lexi.love -= 3
                call sleep from _call_sleep_109
                $ game.room = "bedroom4"
            "Yes":
                bree.say "YES...I mean, yes...if you want to!"
                "I try to keep from sounding too desperate and needy, but I'm not sure I manage it."
                show cuddle lexi with fade
                "Lexi curling up against me beneath the covers is almost as good as the sex - almost..."
                if lexi.is_sex_slave:
                    lexi.say "Sweet dreams, Master..."
                else:
                    lexi.say "Sweet dreams, [hero.name]..."
                bree.say "You too, Lexi..."
                $ lexi.love += 3
                call sleep ("lexi") from _call_sleep_110
                $ game.room = "bedroom4"

    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
