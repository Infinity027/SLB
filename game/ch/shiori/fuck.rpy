init python:
    InteractActivity(**{
    "name": "fuck_shiori",
    "display_name": "Fuck",
    "label": "shiori_fuck_ROOM",
    "conditions": [
        HeroTarget(
            Not(HasRoomTag("mcoffice")),
            HasStamina(),
            ),
        PersonTarget(shiori,
            IsActive(),
            Not(IsActivity("sleep")),
            MinStat("love", 125),
            MinStat("sexperience", 1),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })

    InteractActivity(**{
    "name": "fuck_shiori_personal",
    "display_name": "Fuck",
    "label": "shiori_fuck_mc_office",
    "conditions": [
        IsDone("shiori_show_off_3"),
        HeroTarget(
            HasRoomTag("mcoffice"),
            HasStamina(),
            ),
        PersonTarget(shiori,
            IsActive(),
            Not(IsActivity("sleep")),
            MinStat("love", 125),
            MinStat("sexperience", 1),
            ),
        ],
    "once_day": "ACTIVE",
    "icon": "fuck",
    })

    Event(**{
    "name": "shiori_hottub_sex_male",
    "label": "shiori_hottub_sex_male",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("date_hot_tub_home")
            ),
        PersonTarget(shiori,
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

label shiori_fuck_date_nudistbeach:
label shiori_fuck_date_beach:
label shiori_fuck_beach:
    $ game.play_music("music/roa_music/city_nights.ogg")
    scene bg beach
    show shiori
    with fade
    shiori.say "Hey, [hero.name] - are you okay?"
    mike.say "Ah, yeah...sure."
    mike.say "I'm fine, Shiori."
    mike.say "I'm just not used to being out of the office like this!"
    show shiori happy at startle
    "Shiori giggles, putting a hand to her mouth like a naughty school-girl cutting class."
    shiori.say "I know what you mean, [hero.name]."
    shiori.say "I feel like I should be answering the phone or making coffee!"
    "At this, Shiori lies down on her towel, spreading herself out beside me."
    shiori.say "After all, we shouldn't be behaving like this is still the office - should we?"
    "Her grin is wide and the look in Shiori's eyes unmistakable."
    "I swallow dryly as the true implications of her words sink in."
    "Shiori watches happily as my eyes travel slowly over the entire length of her body."
    "Her swimsuit clings to her form so tightly that nothing is left to the imagination."
    "Indeed, at some particularly impressive points, it struggles to contain what it can't hope to conceal."
    show shiori blush at center, zoomAt(1.5, (640, 1040))
    shiori.say "Ah, [hero.name]..."
    shiori.say "I watch you at the office every single day."
    shiori.say "And I see you working so, so hard."
    shiori.say "The sad thing is that there, I can't do enough to relieve your stress."
    shiori.say "But here...well, it's a different story altogether..."
    "It's only now that I look up and see just how far off the beaten track the spot we've chosen actually is."
    "Did we really pick this place out at random, or was there more thought involved, at least on Shiori's part?"
    "My attention is dragged back to the here and now as I hear Shiori let out a giggle."
    "I look down and see that she's staring at my shorts, eyeing the ever-growing bulge now visible beneath them."
    mike.say "I...ah..."
    show shiori happy at startle
    "Shiori giggles again, rubbing her hand up and down my thigh in a suggestive manner."
    shiori.say "Would you like some help with that, [hero.name]?"
    shiori.say "I know somewhere that you could put it..."
    hide shiori
    show shiori doggy swimsuit beach nomike normal
    with fade
    "At this, Shiori rolls onto her belly and then raises her backside into the air."
    "She pulls aside the gusset of her swimsuit with one hand, exposing herself to me."
    shiori.say "It's okay - no one will see us!"
    "For god's sake - what am I waiting for?!?"
    "Tearing off my shorts, I all but pounce on Shiori's ass."
    "She lets out a little yelp of surprise at the speed with which I move."
    hide shiori
    show shiori doggy swimsuit beach out normal
    "And then she lets out another as I aim my cock straight between her buttocks."
    "All I can say is that I can't have been the only one with this on my mind as we sized each other up just now."
    hide shiori
    show shiori doggy swimsuit beach vaginal normal
    "Shiori's lips are already slick and slippery as the head of my cock rubs against them."
    "She gasps at the sensation, but then this turns into a long moan as I go further."
    "I guess it only takes a moment or two for my cock to slip into her and keep right on going."
    "And that's just what I do, pushing on until I'm balls deep inside of Shiori's pussy."
    "My weight presses her down into the sand, and I can already see her breasts making depressions of their own."
    "Shiori's fingers dig down, as if she hopes to find something to cling onto amongst the shifting grains."
    show shiori doggy speed with vpunch
    "But all that happens is she gets shoved ever more firmly against the sand as I pound away at her."
    "Still gasping for breath, Shiori looks back at me, her head jostled by my own movements."
    show shiori doggy pleasure
    "Her mouth hangs open and her eyes are wide, almost glazed in their appearance."
    "Part of me can't help seeing her as being reduced almost to the state of an animal as I fuck her."
    "The absent look in her eyes and the base, almost bestial noises that she's making right now."
    "But I suppose that makes me an animal too, as all I can think of is doing more of the same."
    show shiori doggy orgasm
    "By now the sound of my thighs slapping against Shiori's buttocks is louder than both our cries."
    "And I know that I can't go on at this pace for much longer."
    "When I cum, I have no way of knowing if Shiori could have sensed it coming."
    show shiori doggy out
    "But from the way she yelps and cries as I yank my cock out of her pussy at the last moment, my guess would be that she didn't."
    show shiori doggy cumshot with vpunch
    "My cum spurts an impressive distance, reaching as high as the back of Shiori's neck."
    hide shiori
    show shiori doggy swimsuit beach done cumshot with vpunch
    "Where it touches her swimsuit, it sinks in, leaving dark patches."
    with vpunch
    "And where it hits her skin, it runs down her sides as gravity has its say."
    "Shiori closes her eyes and lets her head sink down onto her crossed arms."
    "She looks satisfied and almost serene as she lies there in complete silence."
    "And I have to admit that she was right."
    "She really has done more to help my stress here than she ever managed to do back in the office."
    return

label shiori_hottub_sex_male:
    $ game.active_date.clothes = "swimsuit"
    $ CONDOM = False
    show bg pool
    "Normally the invitation to hop into a hot-tub is one that a girl can't resist, as sure thing."
    "But then Shiori's not like most girls, she's more than a little meek and shy."
    "And that means that it takes a lot of coaxing and reassurance from me to convince her."
    "In the end, Shiori gets changed out of sight, unwilling to let me watch."
    "She sticks her head around the door, her cheeks already beginning to flush red."
    mike.say "Hey, Shiori."
    mike.say "Come on in - the water's perfect!"
    if shiori.is_collared:
        shiori.say "I...I'm ready, Master."
    elif shiori.sub >= 25:
        shiori.say "I...I'm ready, Sir."
    else:
        shiori.say "I...I'm ready, [hero.name]."
    shiori.say "I'm going to come out there now!"
    mike.say "Okay, Shiori."
    mike.say "That's great!"
    show shiori swimsuit at left with easeinleft
    "Shiori emerges from the house, wrapped up tightly in a towel."
    show shiori swimsuit at center with ease
    "I'm already sitting in the hot-tub, waiting for her and trying to look reassuring."
    "I watch as she gingerly sticks a toe into the bubbling water, and then a foot."
    "Shiori waits until the very last moment possible to shed her towel."
    hide shiori
    show hottub shiori
    with fade
    "And for a moment, I actually think she's going to sit down in the water before she does so."
    "This means that I only get the briefest glimpse of her body in those few seconds."
    "But what I do manage to see is more than enough to start my cock stiffening!"
    "Shiori's hot little body is all soft curves, enough to make anyone sweat at the sight of them."
    "And when that already hot package is wrapped up in a tight, stretchy swimsuit..."
    "Well, let's just say I feel like the water in the hot-tub right now!"
    if shiori. is_collared:
        shiori.say "Are...are you okay, Master."
    elif shiori.sub >= 25:
        shiori.say "Are...are you okay, Sir."
    else:
        shiori.say "Are...are you okay, [hero.name]?"
    shiori.say "Did I do something wrong?"
    mike.say "Huh..."
    mike.say "What do you mean, Shiori?"
    shiori.say "Well..."
    shiori.say "You're staring at me..."
    "I realise that Shiori's right, I have been staring at her."
    "But not for the reason that she's thinking!"
    "I shake my head, to regain my senses as much as dismiss her concerns."
    mike.say "No, Shiori, of course not!"
    mike.say "I...I just can't stop looking at you, that's all."
    "Shiori lets out a nervous giggle and looks away from me."
    "Her cheeks are burning for real now, and she's come over all bashful."
    "Which, of course, only makes her that much cuter and more desirable in my eyes."
    if shiori. is_collared:
        shiori.say "Oh, stop it, Master."
    elif shiori.sub >= 25:
        shiori.say "Oh, stop it, Sir."
    else:
        shiori.say "Oh, stop it, [hero.name]!"
    shiori.say "I know this swimsuit make me look fat."
    shiori.say "I must look like a tubby little seal right now!"
    mike.say "Seriously, Shiori - if that's what a seal looks like..."
    mike.say "I'd be stiff as a rock watching a nature show about them!"
    "Shiori lets out another giggle, but she's holding my eye this time."
    "She still looks shy, but she pushes herself through the water towards me all the same."
    if shiori. is_collared:
        shiori.say "I...I could be your little seal, Master."
    elif shiori.sub >= 25:
        shiori.say "I...I could be your little seal, Sir."
    else:
        shiori.say "I...I could be your little seal, [hero.name]."
    shiori.say "Y...you could teach me all kinds of tricks."
    shiori.say "And I'd be very good, just to get a reward..."
    "Shiori's breasts bob and float in the water like beach-balls."
    "And they reach me a little before the rest of her does."
    "They press softly against my chest as Shiori pulls me into her embrace."
    "I find myself peeling the straps of her swimsuit down almost as soon as she kisses me."
    "And Shiori offers no resistance whatsoever, surrendering herself to me in that moment."
    "By the time she slips her tongue between my lips, I'm slipping the suit down to her waist."
    "I can feel the sensation of Shiori's nipples as they stiffen against my chest."
    "She sighs through the kiss, helping to pull down her swimsuit."
    "And at the same time, she's tugging down my own trunks."
    "My cock rubs against Shiori's belly and I know that I can't wait any longer."
    show hottub sex male shiori outside
    call shiori_dick_reactions from _call_shiori_dick_reactions_1
    with fade
    "Without waiting for permission, I turn her around and pull her onto my lap."
    "Shiori lets out a yelp of surprise, but she offers no resistance."
    "And the way she wriggles against me is almost too much to bear!"
    "I can't wait any longer, and so pull her hastily onto me."
    "Shiori yelps again as her pussy holds out for a brief moment."
    show hottub sex male shiori inside
    "And then her yelp turns into a sensual moan as her body surrenders to me."
    "She sinks slowly down as my cock pushes its way into her."
    "Every fraction of an inch feels incredible as she does so."
    "I wait until I'm as deep in her as I can possibly go."
    "And only then do I start to thrust in and out of her."
    "Every motion sends Shiori's full, heavy breasts jiggling and bouncing."
    "The water is beading on them, dripping from her stiff nipples the whole time."
    "They seem to hypnotise me then, moving in a way that's impossible to ignore."
    "And so I lean my head around and catch one in my mouth."
    shiori.say "Oooh!"
    shiori.say "Mmmm..."
    "If anything, this makes Shiori even more excited than before."
    "She's riding my cock now like her life depends on it!"
    "I have my hands under her thighs, lifting her up to make each thrust more intense."
    "Another time I might have been worried about her cries attracting unwanted attention."
    "But here and now, all I can think about is keeping right on pounding her as hard as possible!"
    menu:
        "Cum inside":
            "Made slippery by the water, Shiori shifts and slides in my hands."
            "And for a moment I think that she's about to slide right off of my cock!"
            "Not about to let such a thing happen, I make a desperate grab for her."
            "But even then I can still feel Shiori slipping away from me."
            "And so rather than just holding onto her, I almost squeeze her against me!"
            "Shiori squeals as I do so, all of her weight pressing down on my cock."
            "The sensation is more than enough to push me over the edge."
            show hottub sex male shiori cumshot
            $ shiori.love += 1
            "And I lose it there and then, shooting my load deep into Shiori as I cum."
            "I hold her tightly as her squeals fade into satisfied moans."
            show hottub sex male shiori ahegao
            "She squirms in my grasp, riding out the last of her own orgasm on my cock."
        "Pull out":
            "Made slippery by the water, Shiori shifts and slips out of my grasp for a moment."
            show hottub sex male shiori outside
            "It's only a couple of seconds, but long enough for my cock to pop out of her pussy."
            "She yelps and squeals at the sensation, taken completely by surprise."
            "And instinctively, she clamps her thighs around my cock."
            "The feel of Shiori's thick haunches is enough to push me over the edge."
            $ shiori.sub += 1
            show hottub sex male shiori cumshot
            "Which means that I cum mere seconds later between her thighs."
            "Shiori gasps as the sticky, white streamers spatter against her breasts."
            "And without thinking, she begins to massage them as she cums herself."
            "She kneads and squeezes away, rubbing the cum into her pale skin."
    hide hottub
    show hottub shiori
    with fade
    "Afterwards, Shiori sinks back into my arms."
    "She's panting lightly, exhausted and utterly spent."
    "But she seems perfectly happy as she leans back against me."
    "She doesn't even seem concerned that she's bare-chested."
    "Which means that I can admire the view I have of her breasts as we bask in the after-glow."
    $ hero.replace_activity()
    $ game.active_date.score += 20
    $ shiori.sexperience += 1
    $ game.active_date.clothes = None
    return

label shiori_fuck_date_male(location="hero"):
    $ game.play_music("music/roa_music/city_nights.ogg")
    $ game.room = "livingroom"
    scene bg livingroom
    show shiori


    call shiori_fuck_date_intro_male (location) from _call_shiori_fuck_date_intro_male


    call shiori_dick_reactions from _call_shiori_dick_reactions


    if shiori.sub >= 25:
        call shiori_fuck_date_foreplay_male from _call_shiori_fuck_date_foreplay_male

        call handle_npc_leaving (shiori, _return, from_foreplay=True) from _call_handle_npc_leaving_25
        if _return:
            return


    scene bg bedroom1
    show shiori naked blush
    "Shiori glances down at my still stiff cock and her expression becomes one of mock horror."
    shiori.say "You wouldn't...you wouldn't...put it inside of me...would you?"
    "Shiori begins to back away slowly, covering her crotch with one hand and her backside with the other, as if afraid that I'll stick it in her at any moment."
    "Sensing the way she wants this to go, and not being at all adverse to a little roleplay myself, I advance on her equally slowly."
    shiori.say "Oh please...please don't!"
    "She's almost to the bed now."
    shiori.say "It's so big...there won't be room!"
    if not shiori.is_visibly_pregnant:
        "Shiori bumps into the bed and pantomimes falling over and scrambling onto it."
        shiori.say "Please...please...I'll be good - just don't put it inside of me!"
        "She's on all fours now, her naked ass wriggling as she clambers across the bed, being sure not to go too fast."
    else:
        "Shiori bumps into the bed, her rounded belly making her movements clumsy and causing her to collapse onto it."
        shiori.say "Please...please...I'll be good - just don't put it inside of me!"
        "She's on all fours now, her naked ass wriggling and huge belly keeping her from moving at more than a crawl."
    mike.say "It's too late for that now, Shiori!"
    mike.say "You've been a very bad girl - the worst of all!"
    "Shiori yelps and looks back over her shoulder as I begin to climb onto the bed and crawl after her."
    "She may be doing a good job of keeping up the act, but I can still see the glimmer of anticipation in her eyes as I draw ever closer."
    "It's probably out of the feeling that I'm disciplining her that I can't resist slapping Shiori's backside as I draw close enough."
    "I give her a swift, sharp crack across the right buttock, and then follow it up with one to the left for good measure."
    mike.say "That's far enough, Shiori - stop running away from me now, or I'll start to get really mad with you."
    "She stops, biting her lip in sheer anticipation as she looks back over her shoulder at me."
    mike.say "It's time that you held still and took the punishment that you deserve!"


    call shiori_fuck_date_choices_male from _call_shiori_fuck_date_choices_male


    call handle_npc_leaving (shiori, _return) from _call_handle_npc_leaving_26
    if _return:
        return


    hide shiori
    call shiori_sleep_date_fuck (location) from _call_shiori_sleep_date_fuck
    return

label shiori_fuck_date_intro_male(location="hero"):
    if not shiori.sexperience:
        "As soon as we're back at my place, Shiori lets me lead her down the stairs and into my bedroom."
        $ game.room = "bedroom1"
        show bg bedroom1
        "There's no need to chat or offer her a drink before we get down to business, she simply does as she's told."
        "Even though she's more than enough to get me excited merely based off of her looks and the shape of her body."
        "Shiori keeps looking at me with sideways glances and then down at the floor, her cheeks flushing red at the same time."
        "She seems so shy and filled with anticipation at finally doing more than kissing, that it's quite an ego rub for me."
        "Normally a girl would strip herself off at this point, probably make a show of it too."
        "But Shiori just stands there by the bed, biting her lip and looking at me shyly."
        "IS she really this bashful, or is it another one of her manipulative tricks intended to get her just what she wants from me?"
        "Either way, I'm too deeply taken in by her shyness now to be discouraged from taking her by the hand."
        "I take the short, tight dress that she's wearing by the hem and then proceed to almost peel it off of her."
        "Shiori lifts her arms to aid me, and I see her breasts fall free of the dress even before her head is revealed."
        show shiori naked with dissolve
        "She hasn't been wearing a bra all night, instead relying upon he stretchy material of her dress to support them."
        "They're simply huge for her petite build, but they seem to be totally natural, only adding to the amazing shape of her body."
        "A moment later, her head pops free of the dress, her dark hair dropping around her face like a black mane."
        "Shiori sees the way that I'm looking at her breasts, and a truly delighted smile spreads across her features."
        shiori.say "Do you like them?"
        "As if to prejudice the answer, she puts her hands behind her back, swaying from side to side so that her breasts follow suit."
        "I can only nod a little at first, the sight of this making my mouth go suddenly dry."
        "Shiori giggles happily at my silent answer."
        shiori.say "You can touch them...if you like!"
        if not shiori.piercings.nipples.worn:
            "Eagerly I reach out and take a breast in each hand, feeling their significant weight as I do so."
            "Shiori's breasts are as incredible to touch as they are to gaze at - warm and soft like giant balls of pale dough."
            "I begin to stroke at her nipples, when I hear her sigh, almost ruefully."
        else:
            "Eagerly I reach out and take a breast in each hand, feeling their significant weight as I do so."
            "Shiori's breasts are as incredible to touch as they are to gaze at - warm and soft like giant balls of pale dough."
            "I tug at the rings that pierce her nipples, gently at first and then ever harder as she cries out in delighted pain at the sensation."
        shiori.say "Oh, darn it...I went and did it again!"
        "I look up at her, unsure of just what she can mean by that."
        shiori.say "I used my titties to lure you in, just like a naughty girl would!"
        shiori.say "You should punish me for being so bad..."
        "With that, she looks down at her nipples, and then back up at me with raised eyebrows, her expression mournful."
        "So it's punishment that she wants, is it?"
        "I take her nipples between forefinger and thumb, gently at first, but then rolling and squeezing them with increasing force."
        "Shiori moans with sudden pleasure, almost seeming to melt with the sensations she must be feeling."
        "The expression on her face is ecstatic, and she shakes with barely suppressed desire as I continue to squash and abuse her nipples."
        "I have to confess that, by now, I'm already painfully erect myself."
        "Shiori presses herself against me then, stroking the bulge in my pants as though she's hungry for more than just being roughly fondled."
        shiori.say "Maybe I could strip you...and then you could punish me some more?"
        "I nod again, wondering if I'm ever going to manage to actually get a word out of my mouth tonight."
        "She takes her time about the task, seeming to enjoy being able to do little things that I'd normally think nothing of doing myself."
        "Most girls would be outraged that a guy would even think of asking them to do stuff like this."
        "But Shiori seems to revel in the fact that it makes her seem subservient and even a little cowed."
        if not hero.has_skill("hung") and not hero.has_skill("smalldick"):
            "One she has me fully naked, she stares at my cock with wide-eyed amazement."
            shiori.say "Mmm...I'd like to see how this feels in my mouth."
            "She licks her lips slowly and makes a satisfied sound."
            shiori.say "But maybe it's just too big..."
    else:
        if game.week_day % 2 == 0:
            $ game.room = "bedroom1"
            show bg bedroom1
            "Shiori scuttles into the bedroom just ahead of me, glancing over her shoulder, as if afraid that I might not be following."
            "Her eyes are wide and she has a finger pressed to her lips, making her look all the more innocent and unsure of herself."
            "How can she still be so hesitant and insecure, even when we're alone like this?"
            "We both know where this is going, and neither of us is calling for an end to it or making for the door!"
            "But then I guess that's just part of Shiori's nature, she's almost totally convinced that she's never going to be good enough."
            "In truth, it's one of the things that I find most attractive about her."
            "Not the fact that she'd probably let someone walk all over her if the urge took them."
            "Rather the way that she's so humble and unaware of just how beautiful she actually is."
            "All that being said, it doesn't mean I'm about to hold back from having some serious fun with her..."
            mike.say "Take off your clothes, Shiori."
            mike.say "I want to watch you strip."
            "Shiori giggles and looks away, unable to hold my eye as her cheeks flush red at the very suggestion."
            shiori.say "[hero.name]!"
            shiori.say "You're making me blush!"
            "I sit down on the bed and give her what I hope is a reassuring smile."
            mike.say "Well, you're making me hard, Shiori!"
            mike.say "So don't go acting all innocent on me now."
            "Shiori covers her mouth in shock at the suggestion of the effect that she's having upon me."
            "But all the same, I can see that she's more intrigued than outraged."
            shiori.say "I...I suppose I could..."
            "Even as she falters towards doing as I ask, her hands are already starting the task."
            show shiori embarrassed topless with dissolve
            "As though her body is two steps ahead of her brain, Shiori slowly begins to strip off her clothes."
            "There's no practiced art to it, but that almost makes the act of watching her all the more arousing."
            "Her brief glances in my direction as she bashfully takes off one item of clothing after another are so full of genuine emotion."
            "It's almost like I can feel the trepidation and thrills that are battling it out inside of her right now."
            "Even the way she tries to cover herself once she's finally naked is adorable."
            "Shiori's delicate little hands could never hope to conceal her huge, heavy breasts, let alone the rest of her body too."
            show shiori embarrassed naked with dissolve
            "But still she tries, moving her hands from one spot to another and biting her lip as she does so."
            mike.say "Now you've done it, Shiori!"
            shiori.say "Oh no - what is it?"
            show shiori surprised
            shiori.say "What did I do wrong?"
            mike.say "You've made me so hard that I've got no other choice."
            mike.say "I'm going to have to put my cock inside of you!"
            show shiori happy
            shiori.say "Oh, [hero.name]..."
        else:
            $ game.room = "bedroom1"
            show bg bedroom1
            show shiori happy with fade
            "I can't stop smiling like a fool as I lead Shiori into the house and then to my bedroom."
            "And she's smiling back at me in the exact same way as she squeezes my hand too!"
            "The reason we're both so happy is because our date went so well tonight."
            "In fact, it went pretty much perfectly!"
            "Shiori finally seems to be getting over her shyness around me."
            "That means we've been able to talk honestly and openly for the first time."
            "And doing that's revealed to me just how amazing she truly is!"
            "Shiori's sweet, kind and quite smart, despite her kind of ditzy personality."
            "When we first started dating, I was worried that all wanted was her body."
            "But now I'm genuinely falling in love with her personality as well."
            "Though I do have to admit - her curves will always drive me crazy!"
            "Shiori stops just short of my bed and lets go of my hand."
            "Then she wrings hers together as she look at me adoringly."
            show shiori happy
            shiori.say "Oh, [hero.name]..."
            shiori.say "I can't remember when I last had so much fun."
            shiori.say "I really don't want tonight to end!"
            "I can't help letting out a little chuckle and shaking my head."
            mike.say "I wasn't planning on ending it yet, Shiori!"
            mike.say "Why else did you think I wanted to bring you back here?"
            show shiori embarrassed
            "I see Shiori's cheeks flush red."
            "And she turns her eyes away from me."
            "As if she's suddenly too embarrassed to look me in the eye."
            shiori.say "Oh..."
            shiori.say "I...I thought you might want to..."
            shiori.say "You know...do that sort of thing..."
            shiori.say "But I was afraid to assume you'd ask."
            shiori.say "Just in case...you didn't ask...you know?"
            "Oh man..."
            "How can she look like that and yet be so damn innocent?"
            "It's breaking my heart just to hear her talking like that!"
            "I step forward and cradle Shiori's chin in my hand."
            "She gasps at the gesture, but lets me turn her head to face me."
            mike.say "Shiori..."
            mike.say "I'm asking you right now."
            mike.say "Would you like to spend the night with me?"
            mike.say "Because there's nobody else I'd rather be with besides you."
            show shiori surprised
            "Shiori's eyes become wide, almost glistening with happiness."
            "And she nods her head eagerly."
            show shiori happy
            shiori.say "Oh..."
            shiori.say "Yes!"
            shiori.say "Of course I will!"
            "Shiori stands on her tip-toes as I lean forwards."
            show shiori kiss with fade
            $ shiori.flags.kiss += 1
            "And we share a deep, sensual kiss."
            "A kiss that's more than enough to make me start getting hard."
            hide shiori kiss
            show shiori topless embarrassed
            with fade
            "After that, Shiori and I undress each other slowly."
            "She's still more than a little shy, blushing as we do so."
            "But I can feel the warmth of affection building in her."
            show shiori naked with dissolve
            "So that by the time we're finally naked, it feels perfectly natural."
            "I can almost feel the desire in Shiori's body for me to touch her."
            "Because it's the perfect reflection of what I'm feeling for her right now."
    return

label shiori_fuck_date_foreplay_male:
    menu:
        "Tell her to suck you" if shiori.sub >= 25:
            call shiori_fuck_date_bj from _call_shiori_fuck_date_bj
        "Tell her to give you a titty fuck" if shiori.sub >= 50:
            call shiori_fuck_date_titfuck from _call_shiori_fuck_date_titfuck
        "Just fuck her":
            return
    call stop_all_sfx from _call_stop_all_sfx_40

    return _return

label shiori_fuck_date_choices_male:
    menu:
        "Reverse cowgirl":
            call shiori_fuck_date_reverse_cowgirl (0) from _call_shiori_fuck_date_reverse_cowgirl
        "Doggy" if hero.sexperience >= 5:
            call shiori_fuck_date_doggy (5) from _call_shiori_fuck_date_doggy
        "Missionary" if hero.sexperience >= 10 and not Room.has_tag(game.room,"work"):
            call shiori_fuck_date_missionary (10) from _call_shiori_fuck_date_missionary
        "Piledriver" if hero.sexperience >= 15 and not Room.has_tag(game.room,"work"):
            call shiori_fuck_date_piledriver (15) from _call_shiori_fuck_date_piledriver
    call stop_all_sfx from _call_stop_all_sfx_41

    return _return

label shiori_sleep_date_fuck(location="hero"):
    if game.hour > 19 or game.hour < 6:
        show cuddle shiori
        "Afterwards, Shiori clings to me like a small, frightened animal, silent and meek once more."
        "I can't help but feel that we've gone so far tonight that there's no chance of things going back to the way they used to be."
        "For better or worse, I've succeeded in turning sweet, innocent little Shiori into a very dirty girl."
        hide shiori
        call sleep ("shiori") from _call_sleep_31
        $ game.room = "bedroom1"
    return

label shiori_fuck_date_bj:
    mike.say "Get started with your mouth."
    "She starts stroking my dick with her fingers, almost ticking under the head."
    "I'm so excited by now that I can't even think of stopping to ask Shiori to do what I want or else waiting patiently to see if she has the same thing in mind."
    show shiori bj smile with fade
    "Instead I simply thrust my cock forwards while she's still making an act out of teasing me, her mouth mere inches from the tip."
    show shiori bj suck
    "My guess is that Shiori would have made some squeak of protest, but having an erect cock stuffed into her mouth means all I hear is a muffled yelp."
    "But much to my surprise, she only protests until what I've done becomes clear to her."
    "And then she seems to recover quickly, as if resigning herself to doing what I want without objection."
    "Though her technique leaves a lot to be desired, Shiori more than makes up for it in sheer enthusiasm for the task at hand."
    "She sucks and licks away with such dedication that I can't help but soon find myself breathing heavily in response."
    "As I already said, it's not as if Shiori has any kind of technique that I can describe."
    "But she looks up at me with those huge eyes, watching me as my cock fills her mouth and threatens to push right down her throat..."
    "The whole experience is enough to make me almost lose control of myself in record time..."
    menu:
        "Cum in her mouth":
            show sexinserts head shiori zorder 1 at center, zoomAt(1, (640, 870))
            "There's no way I can hold back from cumming now, and I just hope that Shiori's ready for it!"
            "I let out an agonised groan and lose myself while my cock is as deep in her mouth as it'll go."
            show sexinserts head shiori cum zorder 1 at center, zoomAt(1, (640, 870))
            show shiori bj suck cumshot
            with hpunch
            "Shiori's eyes go wide, and I can hear her almost choking as the cum hits the back of her throat."
            with hpunch
            "I try to pull out, but the chaos of her coughing around my cock makes it hard to know what the best thing to do would be."
            show shiori bj tongue -cumshot -suck
            "Eventually, with her eyes watering, she manages to regain her breath enough for me to slide quickly out of her mouth."
            "This leaves her gasping for air, but not looking as though she's about to die of suffocation."
            if not hero.sexperience >= 15:
                $ shiori.love -= 5
                return 'leave_without_gain'
            else:
                $ shiori.love += 1
        "Cum on her face" if shiori.sub >= 50:
            "I might not be able to hold back from cumming, but that doesn't mean I can't pull out in time."
            "The mere thought of doing so is enough to give me the presence of mind when the moment comes."
            hide shiori
            show shiori bj smile
            "Before Shiori truly knows what's happening, my cock is out of her mouth and already twitching before her face."
            show shiori bj cumshot with hpunch
            "A moment later, the first streamer of cum splashes up across her cheek and over her forehead."
            with hpunch
            "Another and then another follow in quick succession, and Shiori yelps in alarm with each one that hits her."
            hide shiori
            show shiori bj smile facial
            with hpunch
            "The sight of that innocent, trusting face marred in that way is something that will stick with me for a long time to come."
            if not hero.sexperience >= 15:
                $ shiori.love -= 5
                return 'leave_without_gain'
            else:
                $ shiori.sub += 1
        "Hold back" if hero.sexperience >= 10:
            "Somehow, the notion of holding back and saving myself for doing something far more memorable to Shiori keeps me from losing it."
            "I take hold of the back of her head with one hand, and carefully part her lips with the other."
            "She looks surprised and disappointed at my actions, which makes me all the more determined to make what I do to her next sufficient compensation."
    return

label shiori_fuck_date_titfuck:
    show shiori bj smile boobs
    "As much as her mouth looks inviting, it's Shiori's huge breasts that are calling out to me tonight."
    "I reach out and take her by the shoulders, pulling her forward until my cock is wedged into her cleavage."
    "At first she looks a little baffled, and I realise that she's far more innocent than the average girl I've screwed around with in the past."
    "Gently taking her hands in mine, I guide them to the sides of her breasts and press them against the fleshy orbs."
    $ shiori.sub += 1
    "After moving them up and down a couple of times, I see realisation dawn in Shiori's eyes."
    "And from that point on, she no longer needs to be told what to do."
    "The sheer weight and size of her breasts means that the sensation is incredible from the start."
    "And Shiori soon begins to perspire from the effort, making her cleavage all the more slick as time goes on."
    if shiori.piercings.nipples.worn:
        "I can't keep myself from hooking my fingers into the rings that pierce Shiori's nipples as she keeps up an impressive pace."
        "She moans and bites at her lower lip in response to the exquisite pain this causes her."
    else:
        "I find that I can't resist the temptation to reach out and pinch at Shiori's nipples as she massages my cock."
        "Her cheeks redden and she groans with pleasure at my touch, making me feel all the more aroused in response."
    "I know that if this goes on for too much longer, I won't have a choice in the matter."
    "I'll cum from what she's doing to me without any trouble whatsoever."
    menu:
        "Cum on her face":
            show shiori bj smile
            "As my cock comes up from between Shiori's breasts, I stiffen my pose and do all that I can to keep it there."
            show shiori bj smile cumshot with hpunch
            "A moment later, the first streamer of cum splashes up across her cheek and over her forehead."
            show shiori bj boobs facial with hpunch
            "Another and then another follow in quick succession, and Shiori yelps in alarm with each one that hits her."
            with hpunch
            "The sight of that innocent, trusting face marred in that way is something that will stick wit me for a long time to come."
            if not hero.sexperience >= 20:
                $ shiori.love -= 5
                return 'leave_without_gain'
            else:
                $ shiori.sub += 1
        "Hold back" if hero.sexperience >= 15:
            "Somehow, the notion of holding back and saving myself for doing something far more memorable to Shiori keeps me from losing it."
            "I take hold of the back of her head with one hand, and carefully part her lips with the other."
            "She looks surprised and disappointed at my actions, which makes me all the more determined to make what I do to her next sufficient compensation."
    return

label shiori_fuck_date_doggy(sexperience_min):
    mike.say "I can't promise that I'll be gentle, Shiori."
    mike.say "But you have my word that I'll make sure you enjoy what I'm going to do to you..."
    if "shiori_event_06" in DONE and game.week_day % 2 == 0:
        $ shiori_fall = True
        "Shiori hurries to step over the bed."
        "But as she does so, one foot gets in the way of the other."
        "I can't tell if it's because of how much she's had to drink tonight."
        "Or if she genuinely trips up on account of her nerves."
        "But either way, the end result is the same."
        "Shiori topples over, landing flat on her face on the bed!"
        scene shiori fall
        show shiori fall bedroom closed naked
        with vpunch
        shiori.say "Aargh!"
        shiori.say "Ooh...ouch!"
        "Shiori looks up at me, embarrassment and shame written all over her face."
        show shiori fall open
        "I suspect that most of the impact was actually absorbed by her unfeasibly huge chest."
        "But it looks like the damage done was mostly to her ego anyway."
        shiori.say "Oh, [hero.name]!"
        shiori.say "I'm such a stupid clutz!"
        shiori.say "Please...don't look at me!"
        menu:
            "Comfort her":
                "The sight of Shiori in such a state makes my heart ache for her."
                "And I can't stand the thought of someone actually laughing at her either!"
                "Hurrying over to where she's laid, I start to help her up."
                mike.say "Don't say things like that about yourself, Shiori!"
                mike.say "You just tripped, that's all."
                mike.say "Just remember I'm always here to help pick you up again!"
                "I hope that my words have had a positive effect of Shiori."
                shiori.say "Oh, [hero.name]..."
                shiori.say "I love you!"
                $ shiori.love += 1
            "LOL!":
                "I can't help bursting into peals of laughter."
                "Shiori just looks so ridiculous down there on the floor!"
                mike.say "Ah, Shiori..."
                mike.say "You're such a clown!"
                "At first it looks like my words hurt Shiori."
                "But then she forces a smile onto her face and nods."
                shiori.say "Ha, ha..."
                shiori.say "That's me, [hero.name]!"
                shiori.say "Just a silly clown!"
                $ shiori.sub += 1
    else:
        $ shiori_fall = False
        "She nods weakly, still not offering any resistance as I guide her down and onto all-fours on the bed."
        "Shiori glances over her shoulder at me as I climb up behind her."
        "The look on her face is equal parts expectation and trepidation."
        show shiori doggy out
    "Shiori lies before me, on her elbows and knees, her face and heavy breasts pressing into the pillows."
    "She's totally exposed, with nothing to hide what's between her buttocks from my hands as I gently part them."
    "For all of her professed shyness, I can see instantly that Shiori's every bit as excited as I am."
    "I could easily make a play for Shiori's sweet little asshole right now."
    "It looks very tight and ever so inviting, nestled there between her buttocks."
    show shiori doggy out
    menu:
        "Fuck her ass" if shiori.flags.anal and hero.sexperience >= (sexperience_min + 5):
            "I'm pretty sure that, in her relative state of innocence, Shiori expects me to make straight for her pussy."
            "So maybe that's why I find the sight of her tight little asshole so irresistible."
            if shiori_fall and shiori.flags.buttplug:
                "Parting her buttocks as wide as I can, I pull of her plug and let the head of my cock rub against her ass a little."
            else:
                "Parting her buttocks as wide as I can, I let the head of my cock rub against it a little."
            "Shiori twitches in evident surprise and lets out a yelp to go with it."
            shiori.say "Uhm, [hero.name], did you get lost back there or something!"
            "Although she's trying to make a joke out of it, I can hear the trepidation in her voice."
            "The effect of this is to make her seem like a frightened little mouse caught in a trap."
            "And that's something that I just can't resist."
            hide shiori
            show shiori doggy anal
            "Without warning, I thrust myself into Shiori's ass."
            "Her yelp turns into a genuine cry as I push past the initial resistance of her muscles."
            show shiori doggy pleasure
            shiori.say "Ooh...ooh god!"
            shiori.say "I can feel you in my ass!"
            shiori.say "I can feel your cock going up there!"
            "It's a turn-on to hear her say as much, even if it is kind of stating the obvious."
            "Pinned to the bed by my weight, she wriggles beneath me in a vain attempt to get free."
            "But this only serves to make my job easier as she works my cock ever deeper into herself."
            "And then there comes a point where the resistance of her muscles seems to at last give out."
            "At that moment, a change comes over Shiori, and as her body gives up the fight, so does she."
            "All at once she melts beneath me, all show of resistance fading away into a supple form of helplessness."
            "Her cries change too, going from an expression of almost desperate pain to moans of defeated acceptance."
            "Shiori lies there, with my cock buried as deep as it can go inside of her."
            "I can feel the muscles, still quivering around me as I push in and out in a gentle rhythm."
            "The fact that she's stopped fighting and surrendered her body to me makes the sensation all the more enjoyable."
            "It feels like I've broken something inside of her, in a metaphorical sense."
            "And as bad as that sounds, I get the impression that Shiori somehow wanted it this way."
            "In fact, I feel so relaxed and satisfied as I fuck her ass, that I almost don't realise I'm about to cum."
            call cum_reaction (shiori, 'anal', sexperience_min) from _call_cum_reaction_168
            if _return == "anal_outside":
                show shiori doggy out
                "Shaking off the haze that seemed to have settled over me, I hastily pull out of Shiori's ass."
                "She moans in a mixture of disappointment and renewed pain as her muscles pucker and shrink in my absence."
                show shiori doggy cumshot with vpunch
                "But then she sighs and looks over her shoulder as the first spurts of cum start to rain down on her."
                with vpunch
                "The warm mess spatters over her back, buttocks and thighs, as though I'm marking my territory."
                $ shiori.sub += 1
                show shiori doggy done with vpunch
                "All that Shiori can do is look at me with distant eyes, as she's showered."
                "And I can't help but see that as an implicit acceptance that she really is mine now."
                "Mine to do with as I please..."
            elif _return == "anal_inside":
                "I could pull out, but that would mean stopping before I've completely conquered Shiori in this way."
                "So instead I keep on pounding away at her buttocks until the very last moment."
                show shiori doggy cumshot with vpunch
                "I cum as deep inside of her as possible, and then feel her collapse onto the bed beneath me."
                with vpunch
                "As she does so, Shiori slides off of my cock, trailing coils of cum from her ass that are still dripping from it."
                $ shiori.sub += 2
                show shiori doggy done gape cumshot with vpunch
                "I watch her crawl around aimlessly atop the sheets, making little sounds, almost like she's mewling to herself."
                "And I can't help but see that as an implicit acceptance that she really is mine now."
                "Mine to do with as I please..."
            $ shiori.flags.anal += 1
        "Fuck her pussy":
            call check_condom_usage (shiori, 120) from _call_check_condom_usage_107
            if _return == False:
                return

            if CONDOM:
                show shiori doggy condom

            "Deep down I know that the only thing that'll satisfy me is getting deep down in her pussy."
            "I lean forward, just enough to let the head of my cock brush at the bottom of Shiori's lips."
            "Instantly she shudders and lets out a gasp of anticipation that makes me want her all the more desperately."
            shiori.say "Oh, [hero.name]..."
            shiori.say "You can...put it inside...if you want to!"
            shiori.say "I want you..."
            "Does she really need to ask if I want to?"
            "Without another moment of hesitation, I change the angle of my cock."
            show shiori doggy vaginal pleasure
            "The head pushes between the already slick lips of Shiori's pussy with ease."
            "I hear her gasp as I do this, but I don't even think of stopping for a second."
            "Instead I thrust into her, not stopping until I can go no further and my balls hit her buttocks."
            "My reward, apart from the amazing sensation being inside of her, is the way her gasp changes the deeper I go."
            "It transforms from a low hiss and into a long, deep moan as she takes every inch of my cock."
            show shiori doggy speed
            "I hold myself still once I've reached my limit, enjoying the feeling of her as she begins to quiver around me."
            "Only then do I start to move slowly back and forth, keeping as much pressure on her as I can manage."
            "Even without her having to move an inch, I can already see the toll this is taking on Shiori."
            "Her hair is starting to become wet with sweat."
            "And not all of the dampness I feel on the inside of her thighs can have dripped from her pussy."
            "From the way her moans are getting louder too, I don't think it'll be too long before Shiori cums."
            "The thought spurs me on, making me want to do the same as close to her climax as possible."
            "I grasp her buttocks with both hands, getting ready for the inevitable to happen..."
            call cum_reaction (shiori, "vaginal", sexperience_min) from _call_cum_reaction_169
            if _return == "vaginal_outside":
                show shiori doggy out
                "At the very last moment, I drag myself out of Shiori's pussy."
                show shiori doggy cumshot
                if not CONDOM:
                    $ shiori.love += 1
                    with vpunch
                    "A second later I shoot my load across her still twitching buttocks."
                    show shiori doggy done with vpunch
                    "Strings of warm cum spatter over her ass and the lips of her pussy as her own orgasm takes her."
                    with vpunch
                    "Utterly spent, Shiori collapses onto the bed as her own sweat and my cum cool upon her skin."
                else:
                    with vpunch
                    "A second later I shoot my load."
                    with vpunch
                    "Utterly spent, Shiori collapses onto the bed as her own sweat cool upon her skin."
            elif _return == "vaginal_condom":
                with vpunch
                "Safe in the knowledge that I've already taken precautions, I keep on pounding Shiori until the very last moment."
                with vpunch
                "This makes certain that we cum together, each one pushing the other onwards to the end."
                with vpunch
                "We both collapse onto the bed, exhausted and yet completely satisfied."
                "Shiori wears a weak and yet blissful smile as I feel my cock finally slither out of her."
            elif _return == "vaginal_inside_pill":
                "I make to pull out, but then I feel Shiori reach back and grab my wrist."
                shiori.say "It's okay...I'm...I'm on the pill!"
                shiori.say "Please...keep going!"
                $ shiori.love += 2
                show shiori doggy cumshot with vpunch
                "I don't need any more motivation to do as she says, and so I keep on thrusting into Shiori until I finally lose it."
                with vpunch
                "This makes certain that we cum together, each one pushing the other onwards to the end."
                with vpunch
                "We both collapse onto the bed, exhausted and yet completely satisfied."
                "Shiori wears a weak and yet blissful smile as I feel my cock finally slither out of her."
            elif _return == "vaginal_inside_pregnant":
                "There's nothing to keep me from keeping right on, as I've already made Shiori pregnant before now."
                "Indeed, it's the weight of her growing belly and the amount by which her breasts have grown that's making this so memorable."
                "It's weird - I never thought I'd be turned on by a pregnant woman's body."
                "But with Shiori, it makes me desire her all the more, so maybe it's different when you're the one responsible?"
                $ shiori.love += 3
                show shiori doggy cumshot with vpunch
                "And that's it - with my head full of Shiori's swollen belly and breasts, I cum inside of her."
                with vpunch
                "Her legs buckle and she collapses onto the bed."
                "But I'm there to catch her, and guide her gently down, holding her in my arms the whole time."
            elif _return == "vaginal_inside_mad":
                "I might well have managed to forget the fact that I'm not wearing any protection."
                "But as she realises I'm about to cum, Shiori certainly shows that she hasn't."
                "Suddenly I feel her start to move beneath me, trying to crawl forwards and off of my cock."
                $ shiori.love -= 5
                show shiori doggy cumshot with vpunch
                $ shiori.impregnate()
                "But before I can even make a move to help her, I lose myself inside of her."
                with vpunch
                "Shiori sinks onto the bed, sobbing at the realisation of what we've done..."
                shiori.say "I can't get pregnant...I can't!"
            elif _return == "vaginal_inside_happy":
                "At the very last moment, I remember that I'm not wearing a condom."
                "But as I begin to make an effort to pull out before it's too late, I feel Shiori reach back and grab my wrist."
                shiori.say "Don't...please!"
                "I look at her wide-eyed, a puzzled expression on my face."
                "The last thing most girls want is for you to shoot your load inside of them with no protection!"
                shiori.say "I don't care...if I get pregnant, [hero.name]."
                shiori.say "I...love you..."
                shiori.say "I'll love our baby too!"
                $ shiori.love += 5
                show shiori doggy cumshot orgasm with vpunch
                $ shiori.impregnate()
                "In the end, there's no time for me to pull out, and I lose it deep inside of Shiori."
                with vpunch
                "She looks blissfully happy as I fill her, the sensation tipping her into an orgasm of her own."
                "I should be feeling the same way too."
                "But I just can't be sure if I kept from pulling out because I wanted to, or because Shiori distracted me on purpose..."
    return

label shiori_fuck_date_reverse_cowgirl(sexperience_min):
    "At that, I sit down on the bed and pull her backwards onto my lap."
    show shiori reverse out with fade
    "I slide my arms under her knees, and then wrap my hands around the back of her neck, pinning her in place."
    menu:
        "Fuck her pussy":
            "Shiori's wide open to me now, meaning that I can have my pick of just where I want to take things."
            "Her ass feels very inviting indeed, but then I notice that her neat little pussy feels so exposed and inviting that I can't resist."
            "Shiori's lips look so perfect and petite that for a moment I wonder if she was actually play-acting when she said I wouldn't fit."
            "But there's only one way to find out the truth."
            call check_condom_usage (shiori, 120) from _call_check_condom_usage_108
            if _return == False:
                return

            show shiori reverse vaginal
            if CONDOM:
                show shiori reverse vaginal condom
            with fade
            "Shiori begins to moan, even before the head of my dick actually makes contact with her lips."
            "This means that when I finally do slide my cock along the length of her pussy, she draws in several short, sharp breaths at the sensation."
            "She's already warm and slick, but I was right to have guessed that she was going to be tight."
            "As I push my way inside of her, the walls of Shiori's pussy squeeze me so much that I gasp myself."
            shiori.say "Oh, [hero.name]...I can feel you inside of me!"
            shiori.say "You're so big!"
            "The mixture of astonishment and arousal in Shiori's voice makes the sensation of pushing into her all the more intense and enjoyable."
            "For every inch that I make it further into her, there's a sigh or a sudden panting."
            "At first I'm afraid that I'm going to cum before I'm even all of the way into her."
            "Finally, when I'm as far into her as I can go, I just stay there and enjoy the feeling of Shiori's reactions."
            shiori.say "Mmm...[hero.name]...you've filled me up!"
            shiori.say "There's no more room left inside!"
            "I begin to thrust in and out of her then, slowly at first, but then ever faster."
            "If Shiori moaned and sighed when I was just inside of her and still, she's soon crying and almost wailing now that I'm moving."
            mike.say "No more spankings for you, Shiori!"
            mike.say "This is the kind of punishment that you deserve."
            mike.say "And from now on, I'm going to see that you get it!"
            "Her whole body is trembling now, her large breasts swinging back and forth in sympathy with my thrusts."
            "Shiori's cries are getting louder now, growing in volume until I'm worried that she'll soon be genuinely screaming."
            "Perhaps she's just a screamer, but part of me can't help thinking this is all of her repressed, submissive feelings suddenly finding an outlet all at once."
            show shiori reverse milk
            "It's then I notice that her breasts have begun to weep milk, and it's seeping down her body and over me too."
            "Being this deep inside of an ecstatic banshee is almost too much for me."
            "And I can already feel myself beginning to cum."
            call cum_reaction (shiori, "vaginal", sexperience_min) from _call_cum_reaction_170
            if _return == "vaginal_outside":
                "I don't know how I have the presence of mind to do it, but I wrench myself out of Shiori mere seconds before I cum."
                show shiori reverse milk out
                "As intense as the sensation of yanking myself out of her tight little pussy is for me, it must be even more so for her."
                "Shiori actually lets out a scream and then a little burst of sobs as I leave her empty."
                $ shiori.love += 1
                show sexinserts chest shiori cum zorder 1 at center, zoomAt(1, (720, 820))
                show sexinserts belly shiori cum as bellycum zorder 2 at center, zoomAt(1, (-140, 1020))
                show shiori reverse milk out cumshot
                with vpunch
                "My cum rains down on her body, even as I see her thrust one hand towards her pussy."
                with vpunch
                "The cum mingles with the milk now almost squirting from Shiori's breasts as she brings herself off."
                hide shiori
                show shiori out reverse milk body
                with vpunch
                "Before the rolling white droplets on her skin have had time to cool, she brings herself off in a flurry of moaning and twitching."
                hide sexinserts
                hide bellycum
            elif _return == "vaginal_condom":
                "The last thing on my mind right now is doing anything other than riding out every last second of my climax inside of Shiori."
                "As I feel it take over, I push myself as far into her as I can possibly go."
                shiori.say "Ah...[hero.name]...you're going to...make me..."
                show shiori reverse milk cum with vpunch
                "And then she follows my lead, cumming with me so deep within her that I can feel every single moment of her climax."
                with vpunch
                "The milk that was leaking from her breasts before this is almost squirting forth now."
                with vpunch
                "If anything, she becomes even tighter, clutching me like a fist and ensuring that I spend all of myself inside her."
            else:
                "I'm just seconds away from cumming now, and it's in this instant that Shiori seems to recall that I'm inside of her without any protection."
                "Part of me expects her to freak out and scream for me to pull out before I cum."
                "But instead she seems to be enjoying the experience all the more."
                show shiori reverse milk ahegao
                shiori.say "Oh, [hero.name]...I can feel you so deep!"
                shiori.say "Punish me some more - cum inside of me...please!"
                with vpunch
                "That's it, I can't hold on any longer."
                with vpunch
                "My orgasm sends me even deeper into Shiori, pushing her into her own, so that she writhes in my lap."
                hide shiori
                show shiori reverse milk pussy nodick


                with vpunch
                $ shiori.love += 3
                if not shiori.flags.pill and not shiori.is_visibly_pregnant:
                    $ shiori.impregnate()
                "When I finally pull out she let a faint whimper escape her throat as my cum seep out of her pussy."
                "The milk from her breasts is almost squirting now as she cums, making us both slick with pale white fluids."

        "Fuck her ass" if shiori.flags.anal and hero.sexperience >= (sexperience_min + 5):
            "Shiori's neat little pussy looks very inviting, but I'm so into this idea of role-playing her punishment, that I focus on her ass instead."
            mike.say "I'm afraid a simple spanking's not going to cut it this time, Shiori."
            mike.say "You've been so bad, I need to do something far worse to you!"
            "Shiori gasps suddenly, the sound of it very different from the playfully afraid noises she's made before this moment."
            shiori.say "Are you really going to..."
            "She gulps audibly, clearly imagining what I'm about to do to her."
            shiori.say "I've...I've never had it up my bottom before!"
            mike.say "Well, I've never taken you up the ass before, Shiori."
            mike.say "So this is a new experience for the both of us!"
            "I hear Shiori audibly gulp and begin to whimper in anticipation."
            "Taking one of her milky-white buttocks in each hand, I part them a little roughly pull her backwards."
            "I pass my arms under Shiori's thighs and then knot my hands behind her head."
            "The head of my cock presses against Shiori's exposed back-passage, and she whines again at the sensation."
            show shiori reverse anal pain with fade
            "As I begin to push myself inside of her, the progress is slow thanks to the fact that she's tense and resisting."
            "But that just makes the whole thing so much more enjoyable, claiming her an inch at a time and listening to her shrill cries as I do so."
            "When I'm finally into her as deep as I can possibly go, I stay there without moving a muscle, simply enjoying the feel of her body as she shudders in response."
            "In between her desperate gasps, Shiori finally manages to speak."
            show shiori reverse anal normal
            shiori.say "Oh, [hero.name]...you're...you're inside of me so deep!"
            "I begin to move in and out of her, returning her almost instantly to a state of helpless moaning."
            "The more that I pound away on her ass, the more Shiori's muscles contract and squeeze me inside of her."
            "Almost every time she cries out, I feel it translated into a contraction around by dick."
            "I can only describe it as a combination of the tightest hole I've ever fucked and the most aggressive hand-job I can imagine."
            "As if sensing what's about to happen, Shiori lets out a desperate wail."
            shiori.say "Ah...ah...you're going to cum...in my ass!"
            show shiori reverse anal normal milk
            "I see with some surprise, that this exclamation is accompanied by her breasts beginning to leak a constant stream of milk."
            call cum_reaction (shiori, "anal", sexperience_min) from _call_cum_reaction_171
            if _return == "anal_outside":
                "Cumming inside of Shiori would be worth it, even if just for the sake of seeing the look on her face."
                "But I'm so into the swing of the idea that I'm punishing her by now, that I want to humiliate her some more."
                show shiori reverse milk out
                "Moments before I reach my climax, I begin to pull myself out of Shiori's ass."
                "The intensity of the act and her reaction to it is almost enough to bring me off on its own."
                $ shiori.sub += 1
                show sexinserts chest shiori cum zorder 1 at center, zoomAt(1, (720, 820))
                show sexinserts belly shiori cum as bellycum zorder 2 at center, zoomAt(1, (-140, 1020))
                show shiori reverse milk out cumshot
                with vpunch
                "And it means that a few seconds after I finally get my cock out of her ass, I cum."
                hide shiori
                show shiori reverse milk out body milk
                with vpunch
                "Shiori moans and whimpers meekly as the warm liquid rains down on her belly and then her breasts."
                with vpunch
                "But she makes no complaint, her cheeks burning with shame as it begins to run down."
                "Almost as if in sympathy, her nipples are now practically squirting milk in quick gushes."
                hide sexinserts
                hide bellycum
            elif _return == "anal_inside":
                "Although the idea of cumming all over Shiori's body is very appealing."
                "I'm getting off far too much on being inside of her ass to be able to even think about pulling out now."
                with vpunch
                "I keep on pushing myself into Shiori, as far as I can go, and hearing the moans she makes in response."
                with vpunch
                "She must know by now what I'm planning to do, aware of how much I'm using her as something to cum in and humiliating her."
                $ shiori.sub += 2
                show shiori reverse anal with vpunch
                "Shiori screams when I finally cum, as though everything that came before was just a game, and now she's crossed an unspoken line with her desire to be degraded."
                shiori.say "Oh, [hero.name]...you...you came inside of me...inside of my ass..."
                shiori.say "I feel so filthy...so dirty that I'll never be clean again!"
                "As if to further compound her shame, Shiori's breasts continue to spurt milk as she pants with sheer exhaustion."
            $ shiori.flags.anal += 1
    return

label shiori_fuck_date_missionary(sexperience_min):
    if game.week_day % 2 == 0:
        "The moment she feels my cock between her thighs, those eyes go wider still."
        "But Shiori bites her lip and nods, letting me know that she's ready for what lies ahead."
        show shiori missionary with fade
        menu:
            "Fuck her ass" if shiori.flags.anal and hero.sexperience >= (sexperience_min + 5):
                "As crazy as it might sound, I get the idea that I should take Shiori up the ass."
                "Because if I can do that and make her enjoy it, then it proves she's capable of anything."
                "And so I aim my cock a little lower, angling it in just such a way..."
                shiori.say "Oh..."
                shiori.say "Oooh, [hero.name]..."
                shiori.say "I...I think you missed the spot!"
                "I give Shiori what I hope is a reassuring smile."
                "And I press on at the same time."
                mike.say "Don't worry, Shiori."
                mike.say "I know what I'm doing."
                mike.say "Trust me - you're going to love this..."
                "Shiori looks less than convinced, but she nods all the same."
                "By now I can feel the tight little hole that I'm looking for."
                "It's doing everything in it's power to resist me."
                "But that's just another part of the thrill!"
                "Shiori moans as I push my cock into her ass."
                shiori.say "Mmm..."
                shiori.say "[hero.name]..."
                shiori.say "It...it hurts!"
                "I almost stop, worrying that the pain is too much for Shiori."
                "And a moment later, her moans are transformed into gasps of pleasure."
                "That's the moment that her muscles stop trying to resist me."
                "The moment when I can finally sink all the way into her."
                show shiori missionary pleasure
                shiori.say "Oh...oh shit!"
                shiori.say "That feels so good!"
                "I nod and smile down at Shiori, relieved that the brief moment of pain is passed."
                "Now all that she's feeling is the pure delight of me moving inside of her."
                "She nods back at me, urging me to go faster and fuck her harder."
                show shiori missionary speed with hpunch
                "And it's not like I need to be encouraged either!"
                "Within mere seconds I'm riding Shiori like my life depends on it."
                "I thrust in and out of her as fast as I can possibly go, panting with the effort."
                "But there's no chance of me slowing down or stopping."
                "Not while Shiori's loving every second of it!"
                "In fact, the only thing that could stop me now is my own climax."
                "And when that comes, there's no holding back!"
                call cum_reaction (shiori, "anal", sexperience_min) from _call_cum_reaction_172
                if _return == "anal_inside":
                    "I'm so deep inside of Shiori's ass right now."
                    "I don't think there's any way I could pull out, even if I wanted to!"
                    $ shiori.sub += 2
                    show shiori missionary ahegao -speed with hpunch
                    "So I just hold on tight and push into her with one final thrust."
                    with hpunch
                    "Shiori moans and writhes beneath me as I shoot my load in her."
                    with hpunch
                    "I hold her close to me the whole time, not wanting it to end."
                    "But when it does, I lay her gently down on the bed, still enjoying the feel of her beneath me."
                elif _return == "anal_outside":
                    "It takes the very last of my strength, but somehow I manage to pull out of Shiori."
                    "She cries out in surprise at the sensation of my cock popping out of her ass."
                    $ shiori.sub += 1
                    show shiori missionary ahegao -speed with hpunch
                    "And then she yelps a second time as I shower her breasts and belly with cum."
                    with hpunch
                    "Shiori stares up at me the whole time, eyes wide with surprise."
                    with hpunch
                    "I'm panting by now, exhausted from my efforts, but smiling all the same."
                    "And when Shiori smiles back up at me, it feels almost as good as the orgasm!"
                $ shiori.flags.anal += 1
            "Fuck her pussy":
                "I move forward just a little."
                "Enough for the head of my cock to stroke the lips of Shiori's pussy."
                "She gasps and nods even more eagerly than before."
                call check_condom_usage (shiori, 120) from _call_check_condom_usage_109
                if _return == False:
                    return
                show shiori missionary vaginal
                if CONDOM:
                    show shiori missionary vaginal condom
                "Feeling more confident that she's into it, I push a little harder down there."
                "And I'm instantly rewarded when Shiori lets out a peal of giggling laughter."
                "It's totally spontaneous and seems to come from the delight she's feeling right now."
                "It lights up her face and sends a shudder through my entire body too."
                "And all I want to do is get inside of her as soon as possible!"
                "All it takes is one more thrust, and I know how much Shiori wants it too."
                "She resists for no more than a second before her lips part."
                "I can't hold back for a moment longer, and I sink straight into her in one motion."
                "Even when I'm as deep into Shiori as I can go, I want to go further."
                "And I stay buried in her for what feels like forever before I begin to move again."
                "But when I do, the reward is well worth the effort."
                "Shiori moans and mewls beneath me, clinging on for dear life."
                "Everything that I give her, she takes with what feels almost like desperation."
                "Her entire body is shaking as I thrust in and out of her."
                "And I feel like I'm touching her from head to toe."
                if CONDOM:
                    show shiori missionary pleasure condom
                else:
                    show shiori missionary pleasure
                shiori.say "Mmm..."
                shiori.say "Oh, [hero.name]..."
                shiori.say "You feel so good..."
                shiori.say "So good inside of me..."
                "With every motion of her body and every word she speaks, Shiori draws me further in."
                "It's weird that this shy, passive girl is inspiring such passion in me right now."
                "But all that I want is to please her, to make her blissfully happy."
                "Maybe it's because I want to protect Shiori."
                "Maybe it's because she's really a beast underneath it all."
                if CONDOM:
                    show shiori missionary speed condom
                else:
                    show shiori missionary speed
                with hpunch
                "But whatever the reason, I redouble my efforts once more."
                "By now I'm all but pounding away at Shiori, unable to slow down for a moment."
                "And she takes everything that I have to give without protest."
                "Her petite, curvaceous little body soaks up every ounce of my effort."
                "Shiori's slick with sweat by now, her breasts bouncing up and down on her chest."
                "I wish I could go on like this forever."
                "But I can already feel myself cumming..."
                call cum_reaction (shiori, "vaginal", sexperience_min) from _call_cum_reaction_173
                if _return == "vaginal_condom":
                    "I'm buried deep inside of Shiori's pussy right now."
                    "So pulling out in time is pretty much out of the question."
                    show shiori missionary cum condom with hpunch
                    "And with one final thrust, I shoot my load into her."
                    with hpunch
                    "Shiori writhes on the end of my cock, safe thanks to us taking precautions."
                    with hpunch
                    "I hold gently against me, letting her ride it out to the end."
                    "Afterwards I lay her down on the bed, enjoying the feeling of her beneath me."
                elif _return == "vaginal_outside":
                    "It takes all the strength I have left to pull out of Shiori."
                    "And she cries out in surprise as my cock slides out of her."
                    $ shiori.love += 1
                    with hpunch
                    "Those cries become louder as I spatter her with my cum a moment later."
                    with hpunch
                    "White striped paint Shiori's breasts and belly."
                    with hpunch
                    "She stares down at the sight, eyes as wide as ever."
                    "But when she looks back up at me with a smile, I feel like I came all over again!"
                elif _return == "vaginal_inside_pill":
                    shiori.say "Please, [hero.name]..."
                    shiori.say "Cum in me..."
                    shiori.say "I'm...on...the...pill!"
                    $ shiori.love += 2
                    show shiori missionary cum ahegao with hpunch
                    "Almost the second that she says this, I lose it inside of Shiori."
                    with hpunch
                    "She clings onto me tightly as I fill her, gasping with pleasure."
                    with hpunch
                    "Shiori rides me to the very end, and then collapses onto the bed."
                    "And I fall down beside her, panting and utterly spent."
                elif _return == "vaginal_inside_pregnant":
                    "Shiori smiles up at me as she cradles her swollen belly."
                    "We both know that it means there's no need for me to stop."
                    "And I don't, keeping on until the very last moment."
                    $ shiori.love += 3
                    show shiori missionary cum ahegao with hpunch
                    "Shiori moans as I shoot my load inside of her."
                    with hpunch
                    "And I gasp as I fill her too."
                    with hpunch
                    "Shiori rides me to the very end."
                    "And then we collapse onto the bed, panting and utterly spent."
                elif _return == "vaginal_inside_mad":
                    shiori.say "Oh...oh...[hero.name]!"
                    shiori.say "You can't..."
                    shiori.say "We didn't use a condom!"
                    "The very second Shiori gasps out her warning, it happens."
                    $ shiori.love -= 5
                    show shiori missionary cum normal with hpunch
                    $ shiori.impregnate()
                    "I shoot my load while I'm as deep inside of her as I can go."
                    with hpunch
                    "She looks up at me in horror as I fill her."
                    "And all I can do is mirror her reaction in my own expression."
                    "Oh shit - what have we done?!?"
                elif _return == "vaginal_inside_happy":
                    shiori.say "Mmm..."
                    shiori.say "Do it, [hero.name]..."
                    shiori.say "Cum inside me..."
                    shiori.say "I want your babies!"
                    "As soon as Shiori utters those last words, it happens."
                    $ shiori.love += 5
                    show shiori missionary cum ahegao with hpunch
                    $ shiori.impregnate()
                    "I cum as deep inside of her as possible, filling her in the blink of an eye."
                    with hpunch
                    "She clings onto me the whole time, a look of utter ecstasy on her face."
                    with hpunch
                    "But all I can do is shake my head, not really aware of what just happened."
                    "Did I really just cum inside of her?"
                    "Without protection?"
                    "Shit - what have I done?!?"
    else:
        "Shiori sighs with anticipation as I guide her gently down onto the bed."
        "And she stares longingly into my eyes as I then lie down atop her."
        scene shiori missionary2
        show shiori missionary2 bedroom
        with fade
        menu:
            "Fuck her ass" if shiori.flags.anal and hero.sexperience >= (sexperience_min + 5):
                "It doesn't take me long to realise that Shiori's not going to make any demands of me here."
                "Instead she seems happy to put herself totally in my hands, trusting me implicitly."
                "And that trust is something that means a hell of a lot to me."
                "So I'm not going to do anything that might damage it."
                "I give Shiori what I hope is a reassuring smile as I lie atop her."
                "And she smiles back at me, but the nerves she's feeling are still visible."
                "That's why I go as slowly and gently as I possibly can."
                "At first all I do is brush the soft folds between Shiori's thighs."
                "This is still enough to make her gasp and bite her lip."
                "Then I slide the entire length of my cock over her pussy."
                "And Shiori's lips part with a moan of sheer, helpless pleasure."
                shiori.say "Oh, [hero.name]..."
                shiori.say "I...I've waited for this SO long!"
                shiori.say "I've dreamed of what it would feel like..."
                shiori.say "Having you inside of me!"
                "As Shiori's saying all of this, my body seems to be on autopilot."
                "I'm hearing her words and the emotions they express are affecting my mind."
                "But my body is acting on some unconscious, almost animal instinct at the same time."
                "This means that as Shiori is speaking, things are still happening to her."
                "And her words melt seamlessly into moans as the inevitable happens."
                show shiori missionary2 anal
                "Before I know what's going on myself, my cock is sinking into her ass!"
                "Ah shit - I wanted to make sure I it was her pussy this time!"
                mike.say "Oh fuck..."
                mike.say "Shiori..."
                mike.say "I'm so sorry!"
                "But to my surprise, Shiori doesn't seem the least bit concerned."
                shiori.say "[hero.name]!"
                shiori.say "Oh my..."
                shiori.say "I had no idea you were so adventurous!"
                shiori.say "But if that's what you like, I like it too.!"
                shiori.say "And you're SO big!"
                show shiori missionary2 pleasure
                shiori.say "Nobody...nobody ever filled me up like this before!"
                "I can feel myself nodding and smiling at Shiori's comments."
                "Already I'm getting an eager desire to please her as much as possible."
                "Oh man - does she already have that much of a hold on me?"
                show shiori missionary2 normal
                "I shake my head, trying to concentrate on the matter at hand."
                "My pace is instinctively slow and gentle to begin with."
                "Because I'm afraid of pushing to hard and fast."
                "Shiori seems to appreciate my efforts, nodding and gasping."
                "But at this rate we're going to be here all night before one of us cums!"
                show shiori missionary2 speed bounce with vpunch
                "So I decide to experiment with going a little faster."
                "And as I begin to pick up speed, I see Shiori note the change."
                "Her arms and legs begin to wrap around me."
                "And soon she's nodding faster too."
                mike.say "Shiori..."
                mike.say "You want more?"
                shiori.say "Oh yes..."
                show shiori missionary2 pleasure
                shiori.say "Please!"
                "Now I'm the one nodding as I pick up speed."
                "Shiori might be meek and demure in terms of her personality."
                "But her body is made of curves and cushions."
                "So it's more than able to stand up to what I'm giving her."
                "In fact, it's starting to feel like it's eating me up!"
                "The more I give Shiori, the more she takes."
                "And pretty soon I'm beginning to pant, sweat beading on my forehead."
                "But she's still not showing any sign of slowing down!"
                "Is this what's really hiding under that shy little smile?"
                "An insatiable appetite for sex?"
                "And the sturdy body to handle it all too?"
                "All the time, Shiori's gazing up at me."
                "There's a look of sheer bliss and satisfaction on her face."
                "Is this for real?"
                "Can she actually be that happy to be with me?"
                "Suddenly Shiori's eyes flare with something from deep down inside."
                show shiori missionary2 pleasure -speed -bounce
                "And in the same moment I feel myself starting to cum."
                "Did she know it was coming?"
                call cum_reaction (shiori, "anal", sexperience_min) from _call_cum_reaction_174
                if _return == "anal_inside":
                    "Still going as fast as I dare, I push on at the very end."
                    "There's no danger in doing so, because I'm doing her up the ass."
                    "And Shiori seems to appreciate me doing so no end."
                    $ shiori.sub += 2
                    show shiori missionary2 ahegao creampie with vpunch
                    "She begins to cum almost the same moment I lose it inside of her."
                    with vpunch
                    "And she clings to me the whole time, sighing with delight."
                elif _return == "anal_outside":
                    "I'd like to have been able to stay inside of Shiori until the end."
                    "But I'm worried about hurting her, so I decide to pull out."
                    $ shiori.sub += 1
                    show sexinserts chest shiori zorder 1 at center, zoomAt(1, (720, 820))
                    show sexinserts belly shiori as bellycum zorder 2 at center, zoomAt(1, (-140, 1020))
                    show shiori missionary2 -anal
                    "And when I do so, the sensation seems to push Shiori over the edge too."
                    $ shiori.sub += 1
                    show sexinserts chest shiori cum zorder 1 at center, zoomAt(1, (720, 820))
                    show sexinserts belly shiori cum as bellycum zorder 2 at center, zoomAt(1, (-140, 1020))
                    show shiori missionary2 cumshot ahegao
                    with vpunch
                    "She wriggles and moans as I shoot my load over her belly."
                    with vpunch
                    "And I can tell that those are sounds of pure delight."
                    hide sexinserts
                    hide bellycum
                $ shiori.flags.anal += 1
            "Fuck her pussy":
                "It doesn't take me long to realise that Shiori's not going to make any demands of me here."
                "Instead she seems happy to put herself totally in my hands, trusting me implicitly."
                "And that trust is something that means a hell of a lot to me."
                "So I'm not going to do anything that might damage it."
                call check_condom_usage (shiori, 120) from _call_check_condom_usage_110
                if _return == False:
                    return
                show shiori missionary2
                if CONDOM:
                    show shiori missionary2 condom
                "I give Shiori what I hope is a reassuring smile as I lie atop her."
                "And she smiles back at me, but the nerves she's feeling are still visible."
                "That's why I go as slowly and gently as I possibly can."
                "At first all I do is brush the soft folds between Shiori's thighs."
                "This is still enough to make her gasp and bite her lip."
                "Then I slide the entire length of my cock over her pussy."
                show shiori missionary2 vaginal
                "And Shiori's lips part with a moan of sheer, helpless pleasure."
                shiori.say "Oh, [hero.name]..."
                shiori.say "I...I've waited for this SO long!"
                shiori.say "I've dreamed of what it would feel like..."
                shiori.say "Having you inside of me!"
                "As Shiori's saying all of this, my body seems to be on autopilot."
                "I'm hearing her words and the emotions they express are affecting my mind."
                "But my body is acting on some unconscious, almost animal instinct at the same time."
                "This means that as Shiori is speaking, things are still happening to her."
                "And her words melt seamlessly into moans as the inevitable happens."
                "Before I know what's going on myself, my cock is sinking into her pussy."
                mike.say "Oh fuck..."
                mike.say "Shiori..."
                shiori.say "[hero.name]!"
                shiori.say "Oh my..."
                show shiori missionary2 pleasure
                shiori.say "You're SO big!"
                shiori.say "Nobody...nobody ever filled me up like this before!"
                "I can feel myself nodding and smiling at Shiori's comments."
                "Already I'm getting an eager desire to please her as much as possible."
                "Oh man - does she already have that much of a hold on me?"
                "I shake my head, trying to concentrate on the matter at hand."
                "My pace is instinctively slow and gentle to begin with."
                show shiori missionary2 normal
                "Because I'm afraid of pushing to hard and fast."
                "Shiori seems to appreciate my efforts, nodding and gasping."
                "But at this rate we're going to be here all night before one of us cums!"
                "So I decide to experiment with going a little faster."
                show shiori missionary2 speed bounce with vpunch
                "And as I begin to pick up speed, I see Shiori note the change."
                "Her arms and legs begin to wrap around me."
                "And soon she's nodding faster too."
                mike.say "Shiori..."
                mike.say "You want more?"
                shiori.say "Oh yes..."
                show shiori missionary2 pleasure
                shiori.say "Please!"
                "Now I'm the one nodding as I pick up speed."
                "Shiori might be meek and demure in terms of her personality."
                "But her body is made of curves and cushions."
                "So it's more than able to stand up to what I'm giving her."
                "In fact, it's starting to feel like it's eating me up!"
                "The more I give Shiori, the more she takes."
                "And pretty soon I'm beginning to pant, sweat beading on my forehead."
                "But she's still not showing any sign of slowing down!"
                "Is this what's really hiding under that shy little smile?"
                "An insatiable appetite for sex?"
                "And the sturdy body to handle it all too?"
                "All the time, Shiori's gazing up at me."
                "There's a look of sheer bliss and satisfaction on her face."
                "Is this for real?"
                "Can she actually be that happy to be with me?"
                "Suddenly Shiori's eyes flare with something from deep down inside."
                "And in the same moment I feel myself starting to cum."
                "Did she know it was coming?"
                show shiori missionary2 pleasure -speed -bounce
                call cum_reaction (shiori, "vaginal", sexperience_min) from _call_cum_reaction_175
                if _return == "vaginal_condom":
                    "Still going as fast as I dare, I push on at the very end."
                    "We remembered to use a condom, so there's no danger involved."
                    show shiori missionary2 creampie with vpunch
                    "And Shiori seems to appreciate me doing so no end."
                    with vpunch
                    "She begins to cum almost the same moment I lose it inside of her."
                    with vpunch
                    "And she clings to me the whole time, sighing with delight."
                elif _return == "vaginal_outside":
                    "I'd like to have been able to stay inside of Shiori until the end."
                    show sexinserts chest shiori zorder 1 at center, zoomAt(1, (720, 820))
                    show sexinserts belly shiori as bellycum zorder 2 at center, zoomAt(1, (-140, 1020))
                    show shiori missionary2 -vaginal
                    with vpunch
                    "But the fact we didn't use a condom means that I have to pull out."
                    "And when I do so, the sensation seems to push Shiori over the edge too."
                    show sexinserts chest shiori cum zorder 1 at center, zoomAt(1, (720, 820))
                    show sexinserts belly shiori cum as bellycum zorder 2 at center, zoomAt(1, (-140, 1020))
                    show shiori missionary2 cumshot
                    with vpunch
                    "She wriggles and moans as I shoot my load over her belly."
                    with vpunch
                    "And I can tell that those are sounds of pure delight."
                    hide sexinserts
                    hide bellycum
                elif _return == "vaginal_inside_pill":
                    mike.say "Shiori..."
                    mike.say "You're on the pill..."
                    mike.say "Right?"
                    shiori.say "Y...yes!"
                    "Still going as fast as I dare, I push on at the very end."
                    "All because I now know there's no danger in doing so."
                    $ shiori.love += 2
                    show shiori missionary2 creampie ahegao with vpunch
                    "And Shiori seems to appreciate me doing so no end."
                    with vpunch
                    "She begins to cum almost the same moment I lose it inside of her."
                    with vpunch
                    "And she clings to me the whole time, sighing with delight."
                elif _return == "vaginal_inside_pregnant":
                    "Still going as fast as I dare, I push on at the very end."
                    "Shiori's belly is a reminder of the fact she's already pregnant."
                    "So there's no danger in me not pulling out."
                    $ shiori.love += 3
                    show shiori missionary2 creampie ahegao with vpunch
                    "And Shiori seems to appreciate me doing so no end."
                    with vpunch
                    "She begins to cum almost the same moment I lose it inside of her."
                    with vpunch
                    "And she clings to me the whole time, sighing with delight."
                elif _return == "vaginal_inside_mad":
                    shiori.say "Please..."
                    shiori.say "Don't cum in me!"
                    shiori.say "I can't get pregnant again!"
                    "Shiori's demands take me completely by surprise."
                    "And in that moment of shock, it's too late to pull out."
                    show shiori missionary2 creampie normal with vpunch
                    $ shiori.impregnate()
                    $ shiori.love -= 5
                    "So I end up shooting my load inside of her."
                    with vpunch
                    "She begins to cum almost the same moment I lose it inside of her."
                    with vpunch
                    "Shiori tries to pull away from me, but she can't escape in time."
                    "Which leaves us both reeling from the shock of what just happened."
                elif _return == "vaginal_inside_happy":
                    shiori.say "Please..."
                    shiori.say "Please cum in me!"
                    shiori.say "I want to have your babies!"
                    "Shiori's demands take me completely by surprise."
                    "And in that moment of shock, it's too late to pull out."
                    show shiori missionary2 creampie ahegao with vpunch
                    $ shiori.impregnate()
                    $ shiori.love += 5
                    "So I end up shooting my load inside of her."
                    with vpunch
                    "And Shiori seems to appreciate me doing so no end."
                    with vpunch
                    "She begins to cum almost the same moment I lose it inside of her."
                    "And she clings to me the whole time, sighing with delight."
                    "But I'm still reeling from the shock of what just happened."
    return

label shiori_fuck_date_piledriver(sexperience_min):
    "Shiori half trips and tumbles onto her back, the mattress breaking her fall."
    "But I'm atop her before she can even begin to recover."
    "She squeals in mock-alarm as I push her thighs downwards, pressing her into the bedclothes."
    "This exposes her to me completely, and I pause to take it all in."
    scene bg black
    show shiori piledriver
    with fade
    "Shiori's pussy and ass are there for the taking."
    "The former looks like it's already getting slick as she imagines what's coming next."
    "But the latter's just there, peeking at me from between her buttocks and ripe for the taking."
    "I don't waste any time making my choice."
    "And a moment later, I'm aiming my cock straight at the one that I want!"
    menu:
        "Fuck her ass":
            show shiori piledriver anal
            "Maybe what Shiori needs is to be shown what she's actually capable of?"
            "To be taken out of her comfort zone and on a journey of discovery?"
            "That's why I part her buttocks wider than before and aim my cock for her ass."
            "I see Shiori's eyes widen as she realises what I have in mind."
            "She squirms a little, but not enough to be trying to escape my hold on her."
            shiori.say "Ah..."
            shiori.say "[hero.name]..."
            shiori.say "My ass!"
            "By now I have the head of my cock in there, pushing against the muscles of her ass."
            "They resist out of sheer instinct, but I keep right on forcing myself in there."
            show shiori piledriver inside
            "And soon enough I can feel my cock sinking inevitably into her."
            shiori.say "Mmm..."
            shiori.say "It's so big!"
            shiori.say "You're filling me up inside!"
            $ dildo = False
            if hero.has_item("dildo"):
                menu:
                    "Use the dildo" if hero.has_item("dildo"):
                        $ dildo = True
                        "I smile down at Shiori, trying to keep my intentions under wraps."
                        "This means that the first thing she sees of the vibrator is when it appears in my hand."
                        "I'd stashed it under the bedclothes for just this kind of situation."
                        "And now is the perfect time to actually use it."
                        show shiori piledriver dildo
                        "Shiori watches in wide-eyed silence as I turn the thing on."
                        "It hums and judders in my hand."
                        "But the sound becomes muffled when I begin to rub it against Shiori's pussy."
                        "Even before I push it inside of her, Shiori closes her eyes tight."
                        show shiori piledriver dildovibes
                        "She moans and pants the whole time, squirming as I work it into her."
                        show shiori piledriver pleasure blush
                        "I keep on thrusting in and out of her ass at the same time."
                        "And now that I'm working her from both sides, Shiori is effectively helpless!"
                    "No vibrator":
                        "I'm sure that Shiori's not just trying to stroke my ego right now."
                        "As her ass feels wonderfully tight around the shaft of my cock."
                        "And it continues to squeeze and press at me as I thrust in and out of her too!"
                        "In fact, I can feel the speed I'm going at pick up with each second that goes by."
                        "It's like running downhill, like I can't stop gaining momentum!"
                        show shiori piledriver pleasure blush
                        "Shiori's stopped talking by now, her eyes closing as I pound away."
                        "All she can do is surrender to the sensation of my cock in her ass."
                        "Bent double as she is, all of my weight is pressing down upon her."
                        "She's pinned to the bed, unable to do anything but take what she's given."
            else:
                "I'm sure that Shiori's not just trying to stroke my ego right now."
                "As her ass feels wonderfully tight around the shaft of my cock."
                "And it continues to squeeze and press at me as I thrust in and out of her too!"
                "In fact, I can feel the speed I'm going at pick up with each second that goes by."
                "It's like running downhill, like I can't stop gaining momentum!"
                show shiori piledriver pleasure blush
                "Shiori's stopped talking by now, her eyes closing as I pound away."
                "All she can do is surrender to the sensation of my cock in her ass."
                "Bent double as she is, all of my weight is pressing down upon her."
                "She's pinned to the bed, unable to do anything but take what she's given."
            "But I can't keep on like this forever."
            "And all too soon I feel myself starting to cum!"
            call cum_reaction (shiori, "anal", sexperience_min) from _call_cum_reaction_176
            if _return == "anal_inside":
                "I keep right on pressing down on Shiori, pushing as deep as I can."
                $ shiori.sub += 2
                show shiori piledriver cumshot with hpunch
                "And by now there's nowhere to go but forwards as I shoot my load."
                show shiori piledriver ahegao with hpunch
                "Shiori cries out as I lose myself inside of her."
                with hpunch
                "And I tumble forwards a moment later, utterly spent and exhausted."
            elif _return == "anal_outside":
                "I pull my cock out of Shiori's ass at the very last moment, almost tumbling over as I do so."
                $ shiori.sub += 1
                show shiori piledriver cumshot outside ahegao with hpunch
                "She cries out at the sudden sensation, her own orgasm seeming to hit at the same time."
                with hpunch
                "Shiori is left panting and helpless as I shoot my load over her from above."
                show shiori piledriver bodycum -cumshot with hpunch
                "And it spatters down over her belly, breasts and face."
            $ shiori.flags.anal += 1
        "Fuck her pussy":
            "I focus all of my attention on Shiori's exposed pussy."
            "All the time she's watching me too."
            "And I swear I can see it begin to glisten all the more."
            call check_condom_usage (shiori, 120) from _call_check_condom_usage_111
            if _return == False:
                return
            if CONDOM:
                show shiori piledriver condom
            "The angle I have Shiori at means that it's an easy task to slip inside of her."
            "All I need to do is push downwards, and my cock sinks between her lips."
            "By now, Shiori's so worked up that there's no resistance whatsoever."
            show shiori piledriver inside
            "Her pussy parts without protest, and I go as deep as I can in one motion."
            shiori.say "Oh, [hero.name]..."
            shiori.say "It's just so big..."
            shiori.say "You've filled me up!"
            "If it were any other girl, I'd be sure they were flattering me."
            "But Shiori's not the kind to say something that she doesn't mean."
            "And she's always at her most honest and intimate at the same time."
            "I try not to let the compliment go straight to my head."
            "Instead I channel the thrill that it give me into my efforts."
            "And pretty soon, I'm thrusting in and out of Shiori like a piston."
            "Her body may well be petite, but she's built out of curves."
            "So everything that I put into my thrusts, she absorbs it with ease."
            "Shiori's thighs quake and her breasts bounce in time with my motions."
            "And I can see the effect that it's having on her too."
            "Her eyes are almost rolling back into her head right now."
            "Shiori's mouth is also hanging open as she pants in sympathy."
            "By now she's almost folded in half beneath me, pressed down into the mattress."
            "But neither of us is about to quit before we see this thing through to the end!"
            "I push on, giving all that I have in an effort to tip Shiori over the edge."
            "And just as I can feel myself on the verge of cumming, I see something change."
            "All of a sudden, Shiori's eyes pop open."
            "It looks like she's about to cum too!"
            call cum_reaction (shiori, "vaginal", sexperience_min) from _call_cum_reaction_177
            if _return == "vaginal_condom":
                "The fact that we took precautions means there's no need to stop."
                with hpunch
                "And so I keep right on until the very moment that I shoot my load."
                with hpunch
                "Shiori seems to climax at the same second too, moaning with the sensation."
                with hpunch
                "Afterwards I collapse into a heap, pulling Shiori over with me."
            elif _return == "vaginal_outside":
                "At the very last moment I take a firm hold of Shiori and yank myself out of her."
                show shiori piledriver outside
                "The sudden motion seems to push her over the edge, and she cums as my cock pops out."
                show shiori piledriver cumshot ahegao with hpunch
                if not CONDOM:
                    "I shoot my load almost as soon as it's free, sending it spattering down onto her."
                    $ shiori.love += 1
                    show shiori piledriver bodycum -cumshot with hpunch
                    "The cum hits Shiori on the belly and chest, but a lot hits her face too."
                    with hpunch
                    "She's panting with her lips parted, and so her tongue gets a portion of it too!"
                else:
                    "I shoot my load almost as soon as it's free."
            elif _return == "vaginal_inside_pill":
                shiori.say "Don't stop, [hero.name]..."
                shiori.say "I'm on the pill!"
                "Shiori's warning is all the permission I need."
                show shiori piledriver cumshot with hpunch
                "I keep right on until the very moment that I cum."
                $ shiori.love += 2
                show shiori piledriver ahegao squirt with hpunch
                "And she cums a second later, crying out at the sensation."
                with hpunch
                "Afterwards I collapse into a heap, pulling Shiori over with me."
            elif _return == "vaginal_inside_pregnant":
                "All the while I've been careful to protect Shiori's swollen belly."
                "But it also means that there's no need to stop what I'm doing."
                show shiori piledriver cumshot with hpunch
                "And so I keep right on going until I shoot my load inside of her."
                $ shiori.love += 3
                show shiori piledriver ahegao squirt with hpunch
                "Shiori moans as I fill her, riding me to the very end."
                with hpunch
                "And then we collapse onto the bed, panting and utterly spent."
            elif _return == "vaginal_inside_mad":
                shiori.say "[hero.name]!"
                shiori.say "The condom..."
                shiori.say "We didn't use one!"
                "Almost as soon as Shiori speaks the words, it's too late."
                show shiori piledriver cumshot with hpunch
                $ shiori.impregnate()
                "I cum while my cocks as deep in her as it'll go."
                $ shiori.love -= 5
                with hpunch
                "Shiori looks at me in horror as I fill her."
                "And I look back with the same expression on my face too."
            elif _return == "vaginal_inside_happy":
                shiori.say "Oh god..."
                shiori.say "Please, [hero.name]..."
                shiori.say "Cum in me..."
                shiori.say "I want it so much!"
                "Shiori's words take be completely by surprise."
                "And that split-second is all it takes."
                $ shiori.love += 5
                show shiori piledriver cumshot ahegao squirt with hpunch
                $ shiori.impregnate()
                "I shoot my load inside of her, much to her apparent delight."
                with hpunch
                "Though what I'm feeling is more like shock and horror!"
    return

label shiori_fuck_mc_office:
    $ game.play_music("music/roa_music/city_nights.ogg")
    shiori.say "What is it, [hero.name]?"
    call office_harem_fuck_choices ('shiori') from _call_office_harem_fuck_choices_3
    return

label shiori_fuck_office_choices:
    menu:
        "Get me a coffee." if "shiori_coffee_2" in DONE:
            call shiori_fuck_office_milk from _call_shiori_fuck_office_milk
        "Give me a blowjob" if "shiori_office_bj" in DONE:
            call shiori_fuck_office_BJ from _call_shiori_fuck_office_BJ
        "Fuck her doggystyle" if "shiori_show_off_3" in DONE:
            call shiori_fuck_office_doggy from _call_shiori_fuck_office_doggy
        "Fuck her missionary style" if hero.sexperience >= 5:
            call shiori_fuck_office_missionary (5) from _call_shiori_fuck_office_missionary
        "Fuck her reverse cowgirl style" if hero.sexperience >= 10:
            call shiori_fuck_office_reverse (10) from _call_shiori_fuck_office_reverse
        "Don't you think you need to be punished" if "shiori_scold_5" in DONE:
            if "lavish_spanking_start" not in DONE and "lavish_spanking_alternate_start" not in DONE and not lavish.hidden and Room.has_tag(lavish.room, "work") and lavish.love >= 90 and lavish.sub >= 25:
                call lavish_spanking_start from _call_lavish_spanking_start
            else:
                call shiori_fuck_office_spank from _call_shiori_fuck_office_spank
        "Forget it":
            shiori.say "Yes [hero.name]."
            $ hero.cancel_activity()
    return

label shiori_fuck_office_BJ:
    show shiori
    shiori.say "How can I be of service?"
    mike.say "I'm feeling a little bit stressed today, Shiori."
    mike.say "And I know that's not really something that's your problem..."
    "The moment that I say those words, I see Shiori's expression change."
    "She shakes her head, instantly dismissing my concerns."
    show shiori happy
    shiori.say "Oh no, [hero.name], it's okay."
    shiori.say "I want to do anything I can to relieve your stress."
    shiori.say "After all, a happy boss is a good boss!"
    "Shiori smiles sweetly as she puts down her pad and pen."
    "Then she starts to walk around to my side of the desk."
    shiori.say "Are you feeling tense at all?"
    if not "shiori_fuck_office_BJ" in DONE:
        shiori.say "Would a massage help?"
        mike.say "Well..."
        mike.say "I was thinking something like that, Shiori."
        mike.say "But maybe more delicate?"
        "I push my chair back and little and gesture downwards."
        "And this stops Shiori in her tracks, eyes wide in surprise."
        show shiori close
        shiori.say "Oh, [hero.name]!"
        shiori.say "Are...are you saying what I think you're saying?"
        shiori.say "You want me to touch you...down there?!?"
        "I nod, trying as best I can to seem calm and reasonable."
        "If I can act like it's not a big deal, maybe I can convince Shiori too."
        mike.say "I know it's a little outside of your job description, Shiori."
        mike.say "But you'd really be helping me out, you know - doing the boss a solid?"
        "Shiori glances at the door and then back at my crotch."
        "Then she bites her lip and looks me in the eye."
        shiori.say "Y...you promise that nobody will ever know?"
        shiori.say "That this will just be between us, [hero.name]?"
        mike.say "Of course, Shiori, of course!"
        mike.say "I won't tell a soul, I promise."
        mike.say "And I'll be eternally grateful too!"
        "Shiori wrings her hands together, looking nervous."
        "But then she seems to steel herself, nodding boldly."
        shiori.say "Okay, [hero.name]."
    else:
        shiori.say "Would it help that if I sucked your dick?"
        mike.say "That would be perfect Shiori."
    hide shiori
    show shiori bj office outfit smile
    with fade
    "I make room for Shiori as she gets down on her hands and knees."
    "Then she shuffles awkwardly under the desk and between my legs."
    "She bangs her head on the underside of the desk more than once."
    "But then I feel her unzipping my flies and reaching inside."
    shiori.say "Oh..."
    shiori.say "I...I found it, [hero.name]!"
    "Of course I knew that before Shiori even opened her mouth."
    "She is handling a rather sensitive part of my anatomy right now!"
    "But I keep my response calm and positive."
    "As the last thing I want to do is put her off."
    mike.say "That's great, Shiori."
    mike.say "You know what to do, yeah?"
    if not "shiori_fuck_office_BJ" in DONE:
        shiori.say "Y...yes, [hero.name]."
        shiori.say "Kanta's daddy seemed to like this kind of thing too."
        shiori.say "So I'll try to remember what I did with his one, okay?"
        mike.say "That sounds perfect, Shiori!"
        mike.say "You go ahead and do that."
        shiori.say "Ooh...it's already so big and hard!"
        shiori.say "I'm...I'm going to put it in my mouth now, okay?"
        mike.say "Okay, Shiori, okay!"
        show shiori bj suck office outfit
        "Mercifully the fact she now has a cock in her mouth keep Shiori from talking."
        "And it doesn't take long for me to realise that she's putting it to better use."
        "Shiori must have had some practice, because what she's doing feels amazing."
    else:
        show shiori bj suck office outfit
        "As usual Shiori's skill is amazing."
    "Right from the start I have to brace myself, holding onto the arms of my chair."
    "For all of her innocence and trepidation, Shiori gives really good head!"
    "She doesn't shy away from swallowing as much of my cock as she can."
    "But at the same time, she's not taking in too much either."
    "And as she works away under the desk, I can feel myself relaxing."
    "The sensation of her lips and tongue are already melting away my stress."
    "I glance down, watching Shiori's head bobbing away between my legs."
    "She has her eyes closed and a look of determination on her face."
    show shiori bj speed with vpunch
    "I shake my head as I realise she's giving it her all down there."
    "Shiori's trying to be efficient, as she always does..."
    "And she's much better at this than at her actual job!"
    python:
        entering_persons = [person.id for person in [aletta, audrey, lavish] if not person.hidden]
        if not game.flags.dwaynedead:
            entering_persons += ["dwayne"]
    if entering_persons:
        $ entering_person = randchoice(entering_persons)
        hide shiori bj with fade
        "I'm just about to lean back in my chair and leave her to it."
        play sound door_knock
        "But then there's a sudden knock at the door."
        "And before I can blink, the person on the other side lets themselves in!"
        if entering_person == "aletta":
            show aletta at top_mostleft with easeinleft
            aletta.say "[hero.name], are you in there?"
            aletta.say "I need your input on this, right now!"
            show aletta at center with ease
            "Aletta comes storming into my office in her usual manner."
            "No asking for permission, no apologies and no pause for breath."
            "Luckily for me she seems to misread the shock on my face."
            "Most likely she takes it for surprise at the interruption."
            mike.say "Ah...uh..."
            mike.say "Aletta...I...I..."
            show aletta surprised
            aletta.say "What's the matter with you, [hero.name]?"
            aletta.say "You sound like you're high or something!"
            mike.say "N...no, Aletta..."
            mike.say "It's just..."
            show aletta normal
            "Aletta frowns at me and crosses her arms over her chest."
            aletta.say "Do you have a migraine, [hero.name]?"
            show aletta sad
            aletta.say "Because I used to get those too."
            aletta.say "And they always made me slur my speech."
            show aletta normal
            "Sensing a chance of redemption, I nod my head."
            mike.say "Y...yeah, Aletta..."
            mike.say "That's it...a migraine!"
            show aletta flirt
            aletta.say "Hmm..."
            aletta.say "Well, you should ease of a little, get some rest."
            aletta.say "I'll come back when you're feeling better, okay?"
            hide aletta with easeoutleft
            "With that, Aletta turns on her heel and walks out."
            "And I let out a sigh of genuine relief."
        elif entering_person == "audrey":
            show audrey angry at left with easeinleft
            audrey.say "Have you seen Shiori around here?"
            audrey.say "That dumb little cow's hiding from me, I know it!"
            show audrey angry at center with ease
            "Audrey storms straight into my office, fuming with rage."
            "I can only assume that she reads my shock as being her own doing."
            "Because she just keeps on talking at me the whole time."
            audrey.say "She was supposed to be helping me out with something."
            audrey.say "But she's gone and done a disappearing act on me!"
            "It doesn't take a genius to figure out what's happened here."
            "Shiori promised to help Audrey out, but then I called her in here."
            "And of course she came running to help her boss."
            "Which means she forgot all about Audrey."
            if audrey.flags.nickname == "toy":
                mike.say "N...no, Toy..."
            else:
                mike.say "N...no, Audrey..."
            mike.say "I haven't seen her all morning!"
            show audrey at center, zoomAt(1.5, (640, 1040))
            "Suddenly I see Audrey's eyes narrow, and she leans towards me."
            "It's like she's zeroing in on something that's suspicious."
            "And that something just so happens to be me!"
            show audrey mock
            audrey.say "Wait a minute..."
            audrey.say "Are you...are you covering for her?!?"
            show audrey angry
            audrey.say "Because if you are, then you're on my shit-list too!"
            "Part of me wants to chew Audrey out for talking to me like that."
            "But I know that I have to let it go while Shiori's actually chewing on my junk!"
            if audrey.flags.nickname == "toy":
                mike.say "I haven't seen her, Toy - I swear!"
            else:
                mike.say "I haven't seen her, Audrey - I swear!"
            mike.say "But I'll let her know you're looking for her if I do, okay?"
            audrey.say "You be sure to do that!"
            hide audrey with easeoutleft
            "With that, Audrey turns on her heel and storms out."
            "And I let out a sigh of genuine relief."
        elif entering_person == "dwayne":
            show dwayne at top_mostleft with easeinleft
            dwayne.say "Hey there!"
            dwayne.say "How's my number one employee, huh?"
            show dwayne smile at left with ease
            "Dwayne swaggers his way into my office without stopping to ask for permission."
            "But then he seems to think that as CEO, he has the right to go where he pleases."
            "Luckily for me, his ego is as huge as his manners are bad."
            show dwayne at center with ease
            "And so he seems to think that his surprise visit is the cause of my alarm."
            show dwayne normal
            dwayne.say "Whoa!"
            dwayne.say "You look like you've seen a ghost, [hero.name]!"
            "But then Dwayne narrows his eyes and scrutinises me closely."
            "He smiles and gives me what he thinks is a conspiratorial wink."
            dwayne.say "Wait a minute..."
            show dwayne smile
            dwayne.say "You're hungover, aren't you?"
            dwayne.say "You were out partying last night, weren't you?"
            dwayne.say "That's my man!"
            show dwayne normal
            "I nod and smile, trying to jump on the chance Dwayne just gave me."
            mike.say "Y...yeah, Dwayne..."
            mike.say "That's right..."
            mike.say "You know me...I'm a party animal!"
            show dwayne smile
            "Dwayne flashes me a smile that shows off his expensive-looking teeth."
            "And he points a finger in my direction, waggling it knowingly."
            dwayne.say "If I were you, I'd get one of those hotties out there to come in here."
            dwayne.say "Then I'd have her give me some executive relief, if you know what I mean!"
            show dwayne at startle
            "Dwayne lets out a manly laugh and his smile becomes wolfish as he does so."
            mike.say "I...I'll keep that in mind, Dwayne!"
            mike.say "D...did you need something?"
            show dwayne normal
            "Dwayne makes a dismissive gesture with one hand."
            dwayne.say "Nah, it can wait until you're sober."
            dwayne.say "Catch you later, [hero.name]."
            hide dwayne with easeoutleft
            "With that, Dwayne turns on his heel and strides out."
            "And I let out a sigh of genuine relief."
        elif entering_person == "lavish":
            show lavish at top_mostleft with easeinleft
            lavish.say "I'm sorry to bother you, [hero.name]."
            lavish.say "But this is REALLY important!"
            show lavish at center with ease
            "Lavish hurries into my office, not stopping to ask permission."
            "And she's blurting out her reasons as she does so."
            "I guess that's why she doesn't notice my surprise."
            "Or maybe she just takes it as being on account of her bursting in."
            show lavish annoyed
            lavish.say "I wouldn't have come barging in normally."
            lavish.say "But I'm looking for Shiori."
            show lavish angry
            lavish.say "She was supposed to be helping me with something important!"
            "It doesn't take a genius to figure out what's happened here."
            "Shiori promised to help Lavish out, but then I called her in here."
            "And of course she came running to help her boss."
            "Which means she forgot all about poor Lavish."
            mike.say "I...I haven't seen her..."
            mike.say "Not in a while, Lavish..."
            mike.say "But...I'll tell her...when...I...do!"
            show lavish normal
            "Lavish nods her head at this, but she still looks worried."
            "I feel a genuine pang of sympathy for her in that moment."
            "Because all she's trying to do is be good at her job."
            "But I can't come out and admit that it's all my fault."
            "That she's been let down because I asked Shiori to blow me!"
            lavish.say "Okay, [hero.name]."
            lavish.say "And sorry for barging in here again!"
            hide lavish with easeoutleft
            "With that, lavish turns on her heel and hurries out."
            "And I let out a sigh of genuine relief."
        $ shiori.sub += 1
        show shiori bj suck speed office outfit with fade
        "It's only then that I realise Shiori never once stopped."
        "All the time there was someone else in the room she kept on going."
        "So she either didn't hear them, or else simply chose to ignore them!"
        "I wonder if I should try to ask her which of the two it is."
        "But one glance under the desk tells me that she's ignore me too."
    "Shiori's head is moving back and forth as fast as it can go."
    "And she's making a moaning sound as she sucks on my cock."
    "The sensation of it mixes with the adrenaline already in my system."
    "And I know that I'm not going to be able to hold on much longer."
    "Which means I have to make a decision about how this is going to end!"
    menu:
        "Cum on her face" if shiori.sub >= 50:
            $ facial = True
            "Just as I feel myself beginning to cum, I make my move."
            show sexinserts head shiori zorder 1 at center, zoomAt(1.0, (680, 870))
            show shiori bj smile -suck
            "I pull back my chair, dragging my cock out of Shiori's mouth."
            "There's a sucking sound as she lets it go."
            "And her eyes open in surprise."
            $ shiori.sub += 1
            show shiori bj cumshot with vpunch
            "But the first thing she see's is me cum in her face."
            show shiori bj -cumshot facial with vpunch
            "White strings of semen spurt out and spatter her cheeks."
            show sexinserts head shiori cum zorder 1 at center, zoomAt(1.0, (680, 870))
            show shiori bj tongue
            with vpunch
            "Shiori yelps in alarms as this happens, opening her mouth wide."
            "Which means that a good amount lands on her tongue too."
            show sexinserts head shiori -cum zorder 1 at center, zoomAt(1.0, (680, 870))
            show shiori bj smile
            "And she has no choice but to swallow it with an alarmed look on her face."
        "Cum in her mouth":
            $ facial = False
            "Just as I feel myself beginning to cum, I make my move."
            show sexinserts head shiori zorder 1 at center, zoomAt(1.0, (680, 870))
            "I push my chair forwards, pushing my cock deeper into Shiori's mouth."
            "Her eyes pop open and she makes a gurgling sound."
            $ shiori.love += 1
            show sexinserts head shiori cum zorder 1 at center, zoomAt(1.0, (680, 870))
            show shiori bj cumshot
            with vpunch
            "And then I shoot my load straight down her throat."
            with vpunch
            "Shiori gulps and gasps, swallowing every last drop."
            show shiori bj tongue -suck
            with vpunch
            "Then she lets me drag my cock out of her mouth."
            show sexinserts head shiori -cum zorder 1 at center, zoomAt(1.0, (680, 870))
            show shiori bj smile -cumshot
            "A string of cum and spit trailing from the tip."
    hide sexinserts
    mike.say "Whoa..."
    mike.say "Thanks, Shiori - that really did the trick!"
    "Shiori looks up from where she's kneeling under the desk."
    "She's trying to clean herself up as best she can."
    "But I see that she's beaming with happiness all the same."
    shiori.say "Do you mean that, [hero.name]?"
    shiori.say "Did I really do well?"
    shiori.say "Oh, that makes me so happy!"
    hide shiori bj
    show shiori blush happy close
    if facial:
        show shiori cumface
    with fade
    "Shiori gets to her feet, still smiling with delight."
    show shiori -close -blush
    "And she almost skips out of my office, waving as she goes."
    hide shiori with easeoutleft
    "I shake my head as the door closes behind her."
    "And I make a mental note to do this more often."
    return

label shiori_fuck_office_missionary(sexperience_min):
    shiori.say "How can I help, [hero.name]?"
    "I give Shiori a smile, which I can't help making a little wolfish."
    "And I think she picks up on the nature of my interest in her too."
    show shiori blush
    "Because she takes a half step backwards, blushing ever so slightly."
    mike.say "You won't need the pen and paper for what I have in mind, Shiori."
    mike.say "I'm just going to need you to lie down on the sofa over there."
    "Shiori follows my gaze over to the sofa in the corner of the room."
    "And then she looks back at me, her eyes growing wider by the second."
    shiori.say "You...you don't want to dictate anything?"
    mike.say "Hmm..."
    mike.say "More of the 'dick' and less of the 'tate', Shiori."
    mike.say "Oh, and I'll need you to take off your clothes too."
    show shiori surprised at startle
    "Reality finally dawns on Shiori, and it's a wonderful sight."
    "Her cheeks flush red and her mouth drops open in surprise."
    shiori.say "You...you mean..."
    mike.say "Yeah, Shiori, I do."
    mike.say "I want you to hop on the sofa and let me fuck you!"
    "For a moment, I think that Shiori might actually say no."
    "Or that she might be thinking of a way to turn this to her advantage."
    show shiori normal
    "But then she nods her head and lowers her eyes, showing her submission."
    shiori.say "If...if that's what you want, [hero.name]."
    "I watch as Shiori does what she's been told."
    "She walks slowly over to the sofa, beginning to strip as she goes."
    "Shiori undresses in a deliberate and careful manner."
    "And she keeps on glancing up at me the whole time."
    "It's like she's looking for my approval."
    "And so I'm sure to nod as I get up and walk over to her."
    show shiori naked with dissolve
    "I make a show of taking off my own clothes at the same time."
    "So when I reach the sofa, I'm pretty much naked as well."
    scene shiori missionary2
    show shiori missionary2 office naked blush
    with fade
    "I can see Shiori's eyes widen even more as she glances at my cock."
    "It's good and hard now, thanks to the sight of her naked body."
    "And she backs onto the sofa, almost like she's retreating from it."
    shiori.say "I...I'm ready for you, [hero.name]."
    shiori.say "Please be gentle with me!"
    menu:
        "Fuck her ass" if shiori.flags.anal and hero.sexperience >= (sexperience_min + 5):
            "The moment those words are out of Shiori's mouth, I can't help myself."
            "If this were a cartoon, I'd suddenly have little devil horns sprout from my forehead."
            "All I want to do now is make Shiori squeal while I have my way with her."
            "Don't get me wrong, I'm not talking about doing anything sadistic."
            "Just making her squirm a little along the way."
            "That's why I spread her thighs nice and wide as I lay atop her."
            "And aim the head of my cock straight between her buttocks."
            show shiori missionary2 pleasure -blush
            shiori.say "Oh..."
            shiori.say "[hero.name]..."
            shiori.say "That feels a little strange!"
            "I can't help smirking to myself as Shiori says this."
            "Her surprise and mounting alarm make it that much more enjoyable."
            show shiori missionary2 ahegao anal
            "And with one firm thrust, I begin to push into her ass."
            shiori.say "Oh...oh god..."
            shiori.say "My ass...that's my ass!"
            "Shiori clings to me in desperation as I sink deeper into her."
            "She moans the whole time too, the sound turning me on all the more."
            "Because it's the perfect embodiment of the sensation she must be feeling right now."
            "And I listen as it turns into the sound of her being pleasured more with each passing second."
            shiori.say "Oh...yes..."
            show shiori missionary2 pleasure
            shiori.say "Please, [hero.name]..."
            shiori.say "Please fuck my ass harder?"
            "I let out a burst of laughter that turns into a grunt of effort."
            "Shiori had me at 'fuck my ass'."
            "But if she wants more, then she's going to get it."
            "In fact, she's going to get all that she can handle!"
            show shiori missionary2 speed with vpunch
            "I can feel Shiori's ass echoing her words."
            "Her muscles are squeezing my cock like a fist."
            "But they're pulling it deeper, rather than pushing it out."
            "And I begin to move in sympathy with that motion as well."
            "I can feel Shiori trying to draw me in, so I feed that desire."
            "She whimpers as I do so, nodding desperately."
            show shiori missionary2 bounce
            "The pace I set is gradually getting faster, a little at a time."
            "And every time I pick up speed, Shiori matches me perfectly."
            show shiori missionary2 blush
            shiori.say "Oh, [hero.name]..."
            shiori.say "You're SO big..."
            shiori.say "I can't take it any more..."
            "Shiori's voice is rising with every word she gasps out."
            "And she's starting to get louder with her cries of pleasure too!"
            "I steal a glance at the door, worried someone will hear her."
            "Maybe it's the sense of urgency that pushes me over the edge."
            "Or the thrill of being caught in the act that does it."
            "Either way I feel myself cumming, and there's no way I can stop it!"
            call cum_reaction (shiori, "anal", sexperience_min) from _call_cum_reaction_178
            if _return == "anal_inside":
                show shiori missionary2 creampie ahegao -speed -bounce with vpunch
                "I clap a hand over Shiori's mouth as I shoot my load."
                with vpunch
                "Not hard enough to keep her from breathing, of course."
                with vpunch
                "Just enough to muffle the noise she makes as I cum in her ass."
                "Shiori squeaks and squeals under me as I fill her up."
                $ shiori.sub += 2
                "She clings onto me until it's over, twitching around my cock."
                "And then her head falls back onto the sofa and she flops like a ragdoll."
            elif _return == "anal_outside":
                show shiori missionary2 -speed -bounce
                "I clap a hand over Shiori's mouth the moment before I shoot my load."
                "Not hard enough to keep her from breathing, of course."
                show sexinserts chest shiori zorder 1 at center, zoomAt(1, (720, 820))
                show sexinserts belly shiori as bellycum zorder 2 at center, zoomAt(1, (-140, 1020))
                show shiori missionary2 outside
                with vpunch
                "Just enough to muffle the noise she makes as I pull my cock out of her ass."
                show sexinserts chest shiori cum zorder 1 at center, zoomAt(1, (720, 820))
                show sexinserts belly shiori cum as bellycum zorder 2 at center, zoomAt(1, (-140, 1020))
                show shiori missionary2 cumshot
                with vpunch
                "Shiori squeaks and squeals under me as I spatter cum over her breasts and belly."
                $ shiori.sub += 1
                with vpunch
                "She clings onto me until it's over, twitching as she cums too."
                "And then her head falls back onto the sofa and she flops like a ragdoll."
            $ shiori.flags.anal += 1
        "Fuck her pussy":
            "I nod at this, wanting to make Shiori as comfortable as I possibly can."
            "And to that end, I part her legs and lower myself down atop her slowly."
            "The tip of my cock brushes the lips of her pussy, making her gasp."
            "But I hold back from pushing it any further, keeping my desires under control."
            call check_condom_usage (shiori, 120) from _call_check_condom_usage_112
            if CONDOM:
                show shiori missionary2 condom
            "Shiori bites her lip as I stroke her pussy with the had of my cock."
            show shiori missionary2 -blush
            "And the moment I see her nod, I make a subtle movement and push."
            show shiori missionary2 pleasure vaginal
            "That's all it takes for me to slip inside of her, sinking deep inside."
            "For all of her apparent nerves, Shiori's as slick as can be down there."
            "I guess she's getting off on the thrill of what we're doing as much as I am!"
            shiori.say "Mmm..."
            shiori.say "Oh, [hero.name]..."
            shiori.say "You're just SO big!"
            shiori.say "I've never felt this full before!"
            "I don't know if Shiori's talking me up for the sake of it."
            "Or if she's being totally honest with me right now."
            "But the truth is that it doesn't really matter."
            "My cock is as deep inside of her as it's possible to get."
            "And it feels incredible, so good I never want it to stop!"
            "I know that I should hold back, at least a little."
            "That I should do it for the sake of keeping Shiori comfortable."
            "And also to prolong the experience for as long as possible."
            "But the sense of release that I'm feeling is just too great."
            show shiori missionary2 speed with vpunch
            "I feel myself moving ever faster, unable to stop myself."
            "Soon enough I'm hammering away at Shiori without mercy."
            "My cock thrusting in and out of her as fast as I can go."
            "But the reaction this causes in her is not what I was expecting."
            "Shiori isn't overwhelmed and she doesn't beg for me to stop."
            "Instead it seems to awaken something deep inside of her."
            "Something that's hungry and desperate to be satisfied."
            show shiori missionary2 blush
            shiori.say "Urgh..."
            shiori.say "Please, [hero.name]..."
            shiori.say "Don't stop...fuck me..."
            shiori.say "Fuck me harder...harder, please..."
            shiori.say "I love your cock...inside me...love it!"
            show shiori missionary2 bounce
            "There's no room in my mind to overthink what Shiori's saying anymore."
            "I'm so lost in the moment and so into her that I just don't care."
            "As far as I'm concerned, she thinks my cock is the best thing in the world."
            "And I'm going to do everything I can to prove that she's right!"
            "My ears are filled with the sound of her begging for more."
            shiori.say "Oh, [hero.name]..."
            shiori.say "You're SO big..."
            shiori.say "I can't take it any more..."
            "Shiori's voice is rising with every word she gasps out."
            "And she's starting to get louder with her cries of pleasure too!"
            "I steal a glance at the door, worried someone will hear her."
            "Maybe it's the sense of urgency that pushes me over the edge."
            "Or the thrill of being caught in the act that does it."
            "Either way I feel myself cumming, and there's no way I can stop it!"
            call cum_reaction (shiori, "vaginal", sexperience_min) from _call_cum_reaction_179
            if _return == "vaginal_condom":
                show shiori missionary2 -speed - bounce with vpunch
                "I clap a hand over Shiori's mouth as I shoot my load."
                with vpunch
                "Not hard enough to keep her from breathing, of course."
                with vpunch
                "Just enough to muffle the noise she makes as I cum in her pussy."
                "The protection we used earlier means there's no danger in doing this."
                "Shiori squeaks and squeals under me as I fill her up."
                "She clings onto me until it's over, twitching around my cock."
                "And then her head falls back onto the sofa and she flops like a ragdoll."
            elif _return == "vaginal_outside":
                "I clap a hand over Shiori's mouth the moment before I shoot my load."
                "Not hard enough to keep her from breathing, of course."
                show sexinserts chest shiori zorder 1 at center, zoomAt(1, (720, 820))
                show sexinserts belly shiori as bellycum zorder 2 at center, zoomAt(1, (-140, 1020))
                show shiori missionary2 outside -speed -bounce
                with vpunch
                "Just enough to muffle the noise she makes as I pull my cock out of her pussy."
                show sexinserts chest shiori cum zorder 1 at center, zoomAt(1, (720, 820))
                show sexinserts belly shiori cum as bellycum zorder 2 at center, zoomAt(1, (-140, 1020))
                show shiori missionary2 cumshot -condom
                with vpunch
                "Shiori squeaks and squeals under me as I spatter cum over her breasts and belly."
                $ shiori.love += 1
                with vpunch
                "She clings onto me until it's over, twitching as she cums too."
                "And then her head falls back onto the sofa and she flops like a ragdoll."
            elif _return == "vaginal_inside_pill":
                shiori.say "Do it, [hero.name], please?"
                shiori.say "I'm on the pill, remember?"
                show shiori missionary2 ahegao creampie -bounce -speed with vpunch
                "I clap a hand over Shiori's mouth as I shoot my load."
                with vpunch
                "Not hard enough to keep her from breathing, of course."
                with vpunch
                "Just enough to muffle the noise she makes as I cum in her pussy."
                "She just reminded me she's on the pill, so there's no danger in doing this."
                $ shiori.love += 2
                "Shiori squeaks and squeals under me as I fill her up."
                "She clings onto me until it's over, twitching around my cock."
                "And then her head falls back onto the sofa and she flops like a ragdoll."
            elif _return == "vaginal_inside_pregnant":
                shiori.say "Do it, [hero.name], please?"
                shiori.say "You already got me pregnant!"
                "I clap a hand over Shiori's mouth as I shoot my load."
                "Not hard enough to keep her from breathing, of course."
                show shiori missionary2 ahegao creampie -bounce -speed with vpunch
                "Just enough to muffle the noise she makes as I cum in her pussy."
                with vpunch
                "She just reminded me she's pregnant, so there's no danger in doing this."
                with vpunch
                $ shiori.love += 3
                "Shiori squeaks and squeals under me as I fill her up."
                "She clings onto me until it's over, twitching around my cock."
                "And then her head falls back onto the sofa and she flops like a ragdoll."
            elif _return == "vaginal_inside_happy":
                shiori.say "Oh, [hero.name]..."
                shiori.say "I want to have your babies!"
                shiori.say "Fill me up...PLEASE?!?"
                "Shiori totally catches me off-guard with her sudden demand."
                show shiori missionary2 ahegao creampie -bounce -speed with vpunch
                $ shiori.impregnate()
                "Which means that I'm distracted at the very moment I cum."
                $ shiori.love += 5
                with vpunch
                "Shiori squeaks and squeals under me as I fill her up."
                with vpunch
                "She clings onto me until it's over, twitching around my cock."
                "And then her head falls back onto the sofa and she flops like a ragdoll."
                "She giggles happily the whole time, while I look on in horror."
            elif _return == "vaginal_inside_mad":
                shiori.say "Oh, [hero.name]..."
                shiori.say "I can't have you cum in me!"
                shiori.say "Pull out...PLEASE?!?"
                "Shiori totally catches me off-guard with her sudden demand."
                show shiori missionary2 ahegao creampie -bounce -speed with vpunch
                $ shiori.impregnate()
                "Which means that I'm distracted at the very moment I cum."
                with vpunch
                $ shiori.love -= 5
                "Shiori squeaks and squeals under me as I fill her up."
                with vpunch
                "She clings onto me until it's over, twitching around my cock."
                "And then her head falls back onto the sofa and she flops like a ragdoll."
                "The both of us staring at each other in horror."
    "Once she's recovered enough to speak, Shiori begins to clean herself up."
    hide sexinserts
    hide bellycum
    hide shiori
    show shiori work
    with fade
    "Then we both hurriedly pull our clothes back on and try to look presentable."
    "Shiori smiles at me as she picks up her pad and pen, getting ready to leave."
    shiori.say "Will there be anything else, [hero.name]?"
    "I note the glow that she has about her, and it makes me smile too."
    mike.say "No, Shiori, not right now."
    mike.say "I think you took care of all my needs already!"
    $ shiori.sexperience += 1
    return

label shiori_fuck_office_reverse(sexperience_min):
    mike.say "There's something I need your help with."
    show shiori happy
    "Shiori's face lights up at the mere mention of me needing her."
    shiori.say "Oh...of course, [hero.name]."
    shiori.say "You know that I'd do anything for you!"
    "I can't help smiling as Shiori makes this so easy for me."
    "I motion towards the desk."
    mike.say "You'd like to join me?"
    "I make a point of raising my eyebrows and smiling."
    "Which means that it's impossible for Shiori to misunderstand me."
    show shiori surprised blush
    "Her eyes go wide as the reality dawns upon her, and he cheeks flush red."
    shiori.say "Oh dear!"
    shiori.say "You mean that you want to..."
    shiori.say "On the desk...with me?"
    mike.say "Well...you did say you'd do anything for me, Shiori."
    mike.say "Or were you just saying that to impress me?"
    show shiori sad
    "Caught out by her own words, Shiori gazes down at her feet."
    "She bites her lip, realising that there's no way out of this."
    shiori.say "I...I did say that, [hero.name]."
    show shiori normal
    shiori.say "So if that's what you want..."
    shiori.say "Just promise that you'll be gentle with me?"
    mike.say "Of course, Shiori."
    mike.say "I can't promise you won't feel a thing."
    mike.say "But I can promise you everything you feel will be amazing!"
    "Shiori lets me take her by the hand and lead her to my desk."
    show shiori topless sadsmile with dissolve
    "Once there she begins to strip off her clothes in a demure fashion."
    "Somehow the subdued nature of her movements is still a big turn-on."
    "And when she steals a glance at me, she looks away again quickly."
    shiori.say "Oh, [hero.name]..."
    shiori.say "I feel so funny!"
    mike.say "Why so, Shiori?"
    shiori.say "B...because I kind of like you watching me!"
    shiori.say "It's strange - I know that I shouldn't."
    shiori.say "But I can't help it!"
    "I know exactly what she means, because I'm feeling it too!"
    "Shiori's an odd mixture of demure innocence and undeniable sexiness."
    "And it's making my cock so hard that it actually hurts!"
    "As if to illustrate my point, I pull down my pants."
    show shiori surprised at startle
    "Shiori gasps out loud at the sight of my manhood."
    shiori.say "Oh, [hero.name]!"
    shiori.say "Did I do that to you?"
    show shiori normal
    shiori.say "Is...is that for me?"
    "The look of sudden hunger in Shiori's eyes is almost scary."
    show shiori naked with dissolve
    "She pulls off the last of her clothes and begins to tug at mine."
    "And before I know it, we're tumbling onto the desk."
    hide shiori
    show shiori reverse office with fade
    "We land in a tangle of limbs, Shiori straddling me backwards."
    "I know that she's about to come down on my cock."
    "And I have a split-second to decide what part of her hits the target!"
    menu:
        "Fuck her ass" if shiori.flags.anal and hero.sexperience >= (sexperience_min + 5):
            "I clap my hands onto Shiori's haunches, where there's plenty to grab hold of."
            "And I make sure that she lands in just such a way."
            "This pushes the head of my cock between her buttocks."
            show shiori reverse anal pain
            "And I feel it begin to sink into her ass."
            shiori.say "Oooh!"
            shiori.say "Oh god..."
            shiori.say "[hero.name], you're in my bottom!"
            shiori.say "Your cock, it's going up my bottom!"
            "I don't dignify that with an answer."
            show shiori reverse ahegao
            "Instead I pull Shiori down with more force."
            "Not enough to cause her pain, but enough to push deeper inside."
            "She wriggles and squirms in my grasp, yelping in alarm."
            show shiori reverse normal
            "But then I sense a change in her motions and the sounds she's making."
            "All of a sudden, Shiori's no longer struggling."
            "Instead she's deliberately trying to work herself downwards."
            "Every move she makes lets my cock deeper inside of her."
            "And her yelps have turned into moans of pleasure."
            shiori.say "Mmm..."
            shiori.say "[hero.name]!"
            shiori.say "What are you doing to me?!?"
            shiori.say "Please...please, don't stop!"
            "Well, what the lady wants, the lady gets!"
            show shiori reverse ahegao
            "Keeping a firm hold on Shiori, I start to move inside of her."
            "She nods desperately from the first moment that I do so."
            "I can feel the muscles of her ass melting around me."
            "And the weight of her body atop me makes it all the more intense."
            "As she rides my cock, every curve and line of Shiori moves in sympathy."
            "Her buttocks are squashed against me like soft cushions."
            "And her breasts bounce up and down on her chest the whole time."
            "The only thing turning me on more is the look on her face."
            "Shiori glances back over her shoulder at me."
            "Cheeks flushed red and her mouth in a helpless pout."
            "She nods desperately, telling me that she wants more."
            "And I find myself leaping to give it to her without question."
            show shiori reverse wet
            "Now I'm pounding away at Shiori faster and harder than ever."
            "I'm doing it with a reserve of strength and stamina."
            "One that I didn't know I possessed until this very moment."
            "But somehow it's still not enough to satisfy her!"
            "Shiori's eyes plead with me for more, and her body demands it."
            "She pushes herself down, squeezing everything out of me."
            "And I can't hold on any longer."
            "A moment later I feel myself starting to cum!"
            call cum_reaction (shiori, "anal", sexperience_min) from _call_cum_reaction_180
            if _return == "anal_inside":
                "I sink my fingers even deeper into Shiori's soft thighs."
                "And at the same time I pull her down like never before."
                "She gasps in surprise, but then nods her approval."
                with vpunch
                "Or at least she does until I shoot my load into her."
                show shiori reverse squirt with vpunch
                $ shiori.sub += 2
                "Then she begins to buck and squirm on my cock."
                with vpunch
                "And it's all I can do to keep a hold of her while I cum."
                show shiori reverse nodick cum ass -squirt -milk
                "By the time she slides off my cock, Shiori seems exhausted."
                "Panting and slick with sweat, she falls onto her face on the desk."
            elif _return == "anal_outside":
                "I sink my fingers even deeper into Shiori's soft thighs."
                show sexinserts chest shiori zorder 1 at center, zoomAt(1, (720, 820))
                show sexinserts belly shiori as bellycum zorder 2 at center, zoomAt(1, (-140, 1020))
                show shiori reverse out -wet
                "And at the same time I pull my cock out of her."
                "Shiori gasps in surprise, looking back over her shoulder."
                show sexinserts chest shiori cum zorder 1 at center, zoomAt(1, (720, 820))
                show sexinserts belly shiori cum as bellycum zorder 2 at center, zoomAt(1, (-140, 1020))
                show shiori reverse cumshot
                with vpunch
                $ shiori.sub += 1
                "But that doesn't stop me shooting my load all over her."
                show shiori reverse body cum -cumshot with vpunch
                "Streamers of cum rain down on her back and buttocks."
                with vpunch
                "It mixes with the sweat already covering her skin."
                show shiori reverse normal
                "Before I'm done, Shiori falls onto her face on the desk."
                "And she lies there, gasping for breath, utterly exhausted."
                hide sexinserts
                hide bellycum
            $ shiori.flags.anal += 1
        "Fuck her pussy":
            "I clap my hands onto Shiori's haunches, where there's plenty to grab hold of."
            "And I make sure that she lands in just such a way."
            "The lips of her pussy slide along the length of my cock."
            "And I can instantly feel just how slick she is down there."
            "Which means I want to get inside of her as soon as I possibly can!"
            call check_condom_usage (shiori, 120) from _call_check_condom_usage_113
            if _return == False:
                return
            "When the moment comes and I pull Shiori downwards, it's as smooth as can be."
            "All of her weight is behind her and she's more than ready for me too."
            if CONDOM:
                show shiori reverse condom pain
            show shiori reverse vaginal pain
            "Which means that after a few seconds of resistance, I slide right into her."
            "The feeling is like nothing I can describe, but I'll try all the same!"
            "And Shiori makes it that much better by letting me know she's enjoying it too."
            shiori.say "Oh..."
            shiori.say "Oh, [hero.name]..."
            shiori.say "You're SO big!"
            shiori.say "How can it fit inside of me?!?"
            "I don't know if Shiori's trying to talk me up right now."
            "Or if she's genuinely blown away by my size."
            "But it hardly matters, as her words have the desired effect on me."
            "All that I can think of is showing her the best time possible."
            "I want to live up to her expectations of me."
            "And I devote all of my strength to making that happen."
            "I sink my fingers even deeper into Shiori's soft thighs."
            show shiori reverse wet
            "And I slowly begin to pick up speed as I thrust in and out of her."
            "I had meant to keep things under control as I do this."
            "But Shiori seems to somehow take over, making me follow her lead."
            "The moment I give her more, she takes it without pause or question."
            "Her small yet sturdy little frame eats it up in the blink of an eye."
            show shiori reverse ahegao
            "And then she demands more, riding my cock like she's desperate."
            shiori.say "Mmm..."
            shiori.say "Oh god..."
            shiori.say "You feel so good inside of me, [hero.name]!"
            shiori.say "I want to...to have your cock in me forever!"
            "How is she doing this?"
            "How is she turning the tables on me?!?"
            "This was supposed to be me getting Shiori to do what I wanted."
            "And now she's got me eating out of her hand!"
            "Anything she says or asks for, I can't help but give it to her."
            "But then if being Shiori's slave feels this good..."
            "I'm not sure that I want to be anything else!"
            "Shiori's buttocks are pressed against me like pillows."
            "Her breasts are bouncing up and down on her chest."
            "And she looks back at me over her shoulder, cheeks flushed red."
            "Shiori nods, letting me know that I'm giving her all she desires."
            "And that's all it takes to push me over the edge."
            "No matter what Shiori might want, I'm about to cum!"
            call cum_reaction (shiori, "vaginal", sexperience_min) from _call_cum_reaction_181
            if _return == "vaginal_condom":
                "I sink my fingers even deeper into Shiori's soft thighs."
                "And at the same time I pull her down like never before."
                "She gasps in surprise, but then nods her approval."
                with vpunch
                "Or at least she does until I shoot my load into her."
                show shiori reverse milk with vpunch
                "Then she begins to buck and squirm on my cock."
                with vpunch
                "And it's all I can do to keep a hold of her while I cum."
                show shiori reverse normal -milk -cum
                "By the time she slides off my cock, Shiori seems exhausted."
                "Panting and slick with sweat, she falls onto her face on the desk."
            elif _return == "vaginal_outside":
                "I sink my fingers even deeper into Shiori's soft thighs."
                show sexinserts chest shiori zorder 1 at center, zoomAt(1, (720, 820))
                show sexinserts belly shiori as bellycum zorder 2 at center, zoomAt(1, (-140, 1020))
                show shiori reverse out -wet -condom
                "And at the same time I pull my cock out of her."
                "Shiori gasps in surprise, looking back over her shoulder."
                show sexinserts chest shiori cum zorder 1 at center, zoomAt(1, (720, 820))
                show sexinserts belly shiori cum as bellycum zorder 2 at center, zoomAt(1, (-140, 1020))
                show shiori reverse cumshot
                with vpunch
                "But that doesn't stop me shooting my load all over her."
                show shiori reverse cum body -cumshot with vpunch
                $ shiori.love += 1
                "Streamers of cum rain down on her back and buttocks."
                with vpunch
                "It mixes with the sweat already covering her skin."
                show shiori reverse normal
                "Before I'm done, Shiori falls onto her face on the desk."
                "And she lies there, gasping for breath, utterly exhausted."
                hide sexinserts
                hide bellycum
            elif _return == "vaginal_inside_pill":
                shiori.say "Please cum inside me, [hero.name], please!"
                shiori.say "I'm on the pill, remember?"
                "I mentally thank Shiori for the timely reminder."
                "And at the same time I pull her down like never before."
                "She gasps in surprise, but then nods her approval."
                "Or at least she does until I shoot my load into her."
                show shiori reverse milk cum with vpunch
                $ shiori.love += 2
                "Then she begins to buck and squirm on my cock."
                with vpunch
                "And it's all I can do to keep a hold of her while I cum."
                show shiori reverse nodick cum pussy -milk with vpunch
                "By the time she slides off my cock, Shiori seems exhausted."
                "Panting and slick with sweat, she falls onto her face on the desk."
            elif _return == "vaginal_inside_pregnant":
                shiori.say "Please cum inside me, [hero.name], please!"
                shiori.say "Like you did before, remember?"
                shiori.say "Like the time you got me pregnant!"
                "I mentally thank Shiori for the timely reminder."
                "And at the same time I pull her down like never before."
                "She gasps in surprise, but then nods her approval."
                "Or at least she does until I shoot my load into her."
                show shiori reverse milk cum with vpunch
                $ shiori.love += 3
                "Then she begins to buck and squirm on my cock."
                with vpunch
                "And it's all I can do to keep a hold of her while I cum."
                show shiori reverse nodick cum pussy -milk with vpunch
                "By the time she slides off my cock, Shiori seems exhausted."
                "Panting and slick with sweat, she falls onto her face on the desk."
            elif _return == "vaginal_inside_happy":
                shiori.say "Keep going, [hero.name], please!"
                shiori.say "I want to feel you cum inside of me!"
                "Shiori catches me off guard, making me forget myself."
                "And that's all the time needed for it to happen."
                show shiori reverse milk cum with vpunch
                $ shiori.impregnate()
                "I shoot my load into her while Shiori squirms on my cock."
                show shiori reverse out cumshot -wet -cum with vpunch
                "I pull out the moment I regain control."
                "But by then it's too late."
                show shiori reverse cum body -milk -cumshot
                $ shiori.love += 5
                "Shiori smiles back at me as she slides off my cock."
                "And all I can do is shake my head in shock."
            elif _return == "vaginal_inside_mad":
                shiori.say "[hero.name], you have to pull out!"
                shiori.say "You can't cum inside me!"
                "Shiori catches me off guard, making me forget myself."
                "And that's all the time needed for it to happen."
                show shiori reverse milk cum with vpunch
                $ shiori.impregnate()
                "I shoot my load into her while Shiori squirms on my cock."
                show shiori reverse out cumshot -wet -cum with vpunch
                "I pull out the moment I regain control."
                "But by then it's too late."
                show shiori reverse pain body -milk -cumshot
                $ shiori.love -= 5
                "Shiori drags herself off my cock, a look of horror on her face."
                "And all I can do is shake my head in shock."
    "Shiori cleans herself up and then begins to get dressed."
    hide shiori
    show shiori work blush
    with fade
    "And I follow her lead, still exhausted from my efforts."
    "She's blushing and trying to avoid meeting my eye."
    "But I can see that Shiori's also smiling."
    "In fact, she's practically glowing."
    shiori.say "W...will that be all, [hero.name]?"
    mike.say "Ah...yeah, Shiori."
    mike.say "That'll be all for now!"
    $ shiori.sexperience += 1
    return

label shiori_fuck_office_doggy:
    shiori.say "Where do you want me?"
    "What is she trying to do - kill me with innuendos?"
    mike.say "Just over here by the desk, Shiori."
    mike.say "That'll do fine...for now."
    "If Shiori notices the tone of my voice or the way I'm looking at her, she doesn't show it."
    "Instead she simply walks over and stands in the appointed spot."
    "She smiles obligingly as I get up and walk over to stand behind her."
    mike.say "Have you got that thing in?"
    mike.say "Is it up your ass?"
    "Shiori looks confused for a moment as she glances back over her shoulder at me."
    "But then the realisation seems to dawn on her as to just what I'm talking about."
    "Her cheeks flush red in an instant, and she starts to mutter a stream of excuses."
    shiori.say "I don't...I don't..."
    shiori.say "Oh, [hero.name] - what on earth can you mean?"
    "I lean in a little closer."
    mike.say "Don't play dumb with me, Shiori."
    mike.say "You've got that thing up there right now - haven't you?"
    "She looks away, as if ashamed to admit the truth."
    "And then she nods quickly, confirming my suspicions."
    shiori.say "Yes..."
    shiori.say "Yes, it's in me..."
    "As she says this, her breathing is becoming heavier by the second."
    shiori.say "I put it up there every day that I come into work."
    shiori.say "To remind me of you, [hero.name]."
    shiori.say "Because...because it makes me think of you being inside of me!"
    "Now I'm the one to begin breathing heavily, my heart beating like a drum in my chest."
    "I can feel my cock in my shorts, getting as stiff as a board at her admission."
    mike.say "There's no need to wander around like that, Shiori."
    mike.say "Why settle for a substitute, when you can have the real thing in its place?"
    "I hear Shiori gasp as I push my groin against her backside, pressing her against the edge of the desk."
    "But she makes no effort to object or pull away as I do so."
    "I use one hand to push Shiori on the desk and the other to yank up her skirt."
    hide shiori
    show shiori doggy office work buttplug nomike with fade
    "Once the rounded shape of her buttocks are exposed, I pull down her tights and panties in one go."
    "Shiori doesn't struggle for a moment."
    "Instead I feel her kicking off her shoes and pulling at her own underwear too."
    "And it's a second later that I see it, the green shape of the butt-plug."
    "There it is, nestled between Shiori's buttocks like an invitation to me."
    "I don't hesitate to reach down and grab hold of it, yanking it straight out of her butt."
    hide shiori
    show shiori doggy office work pleasure nomike gape
    "The sound of it popping out is almost forgettable alongside the one Shiori makes in the same moment."
    "Her sigh is so deep and intense, that part of me thinks she might actually start to deflate any second!"
    shiori.say "Oooh..."
    shiori.say "[hero.name]..."
    shiori.say "I feel so empty now..."
    shiori.say "Won't you fill me up again?"
    "Without another moment's hesitation, I push Shiori forwards until she's forced to clamber onto the table."
    "Down on all fours and with her thighs spread apart, she waits for me to make my next move."
    "And so I hastily strip off my pants and free my cock from my shorts a second later."
    hide shiori
    show shiori doggy office work normal out
    "The butt-plug has left Shiori's ass wide open and more than slick enough for me."
    "I'm more than willing to take the act of stripping her off and pulling out the plug as foreplay enough."
    "So I don't waste any more time in aiming my cock between her buttocks and climbing onto the desk after her."
    show shiori doggy office work pleasure anal
    "The muscles of Shiori's ass are just beginning to recover as I push into her."
    "Still quivering and trying to tighten up again, they naturally melt as I frustrate their efforts."
    "This translates into Shiori herself shaking and moaning as I keep on until I can go no further."
    mike.say "How's that, Shiori?"
    mike.say "How does it feel?"
    mike.say "Is that better than the butt-plug?"
    shiori.say "Ah...yes...yes it is!"
    shiori.say "Oh, [hero.name]..."
    shiori.say "Your cock feels so much better in my ass!"
    shiori.say "I want it inside of me all the time!"
    "Shiori's words are enough to turn me on even more."
    "I grab her by the thighs and begin to thrust in and out as hard as I'm able."
    show shiori doggy speed with vpunch
    "Soon her words are replaced by a desperate groaning and moaning."
    "This isn't some elegant and romantic union of two kindred spirits."
    "It's just me, desperately fucking Shiori's ass as hard as I possibly can."
    "And it's her riding my cock, desperately wanting all that I can give her."
    show shiori doggy cumshot with vpunch
    "When I cum, all I can hear is Shiori as she buries her head into her arms, trying to muffle her cries."
    with vpunch
    "Well, that and the sound of my thighs slapping against her buttocks."
    show shiori doggy done gape
    "Afterwards, Shiori slithers off of my cock, gasping the whole time."
    hide shiori
    show shiori
    with fade
    "As we get dressed again, neither of us says a word."
    "But as she turns to go, I see Shiori clutching the butt-plug in one hand."
    "And she has a satisfied, almost blissful look on her face."
    $ shiori.sexperience += 1
    $ shiori.flags.anal += 1
    return

label shiori_fuck_office_milk:
    shiori.say "Of course, [hero.name]!"
    "Shiori storms out and come back a few minutes later."
    shiori.say "Your coffee, [hero.name]."
    call shiori_coffee_choice from _call_shiori_coffee_choice_1
    return

label shiori_fuck_office_spank:
    if game.week_day % 2 == 0:
        show shiori embarrassed
        "I point to my desk, and she sighs, sliding over it."
        "I don't really know why she needs to be punished. But it looks like she does."
        hide shiori
        show shiori spanking
        show shiori spanking botpantiesdown
        with fade
        "I grab her skirt, hiking it up and showing off her panties."
        "I then trace my fingers down along the white fabric before I gripped at them and tugged them down, exposing her before me."
        show shiori spanking botpantiesdown hand
        mike.say "A bare butt... that's the only way to cure you."
        show shiori spanking botpantiesdown done mark pain foot
        play sound spank
        with hpunch
        "I slap her square in the center, lower than normal, getting close to her exposed pussy."
        hide shiori
        show shiori spanking botpantiesdown hand normal
        "She yelps, her tongue rolling out from that hit."
        show shiori spanking botpantiesdown done mark pain
        play sound spank
        with hpunch
        shiori.say "Aaaagh! Boss, I'll do better, I promise!"
        hide shiori
        show shiori spanking botpantiesdown hand normal
        mike.say "No more games from now on!"
        show shiori spanking botpantiesdown blur
        "I said, slapping her on one cheek, and then the other."
        show shiori spanking botpantiesdown done mark pain
        play sound spank
        with hpunch
        "She grips the desk, shuddering violently as she groans out from my slaps."
        hide shiori
        show shiori spanking botpantiesdown hand normal
        shiori.say "B... Boooosss!"
        show shiori spanking botpantiesdown blur
        mike.say "From now on, if you want to be punished, you do a GOOD job. That's because you want this so much."
        show shiori spanking botpantiesdown done mark pain foot
        play sound spank
        with hpunch
        shiori.say "Aaah, r-right boss!"
        hide shiori
        show shiori spanking botpantiesdown hand normal
        shiori.say "I'm so sorry boss..."
        show shiori spanking botpantiesdown blur
        "I give her a triple slap."
        show shiori spanking botpantiesdown done mark pain foot
        play sound spank
        with hpunch
        "One cheek, the other, and then in between."
        hide shiori
        show shiori spanking botpantiesdown e pain
        "She pants, leaning over the desk, groaning as her butt shines red with my hand prints."
        show shiori spanking botpantiesdown e normal
        "She sighs, closing her eyes and smiling."
        mike.say "Shiori, you can take care of this, but... leave your panties here when you go back to your desk."
        hide shiori
        show shiori blush
        with fade
        "She squeaks and pushes herself up, pulling down her skirt and running off towards the room."
        hide shiori
    else:
        mike.say "Shiori, you understand that I need coffee to function, right?"
        show shiori embarrassed
        shiori.say "Erm...yes, I guess so."
        mike.say "And right now my cup is half-full and stone cold!"
        shiori.say "I...I'm sorry!"
        shiori.say "Would you like me to make you a fresh cup?"
        mike.say "Yes, Shiori."
        mike.say "But first I want you to come over here."
        "I push my chair back from the desk and gesture to my lap."
        show shiori annoyed
        "Shiori glances back over her shoulder at the door."
        "And for a moment I think she's going to defy me."
        show shiori embarrassed
        "But then she scuttles around the side of the desk."
        shiori.say "Y...you want me to sit there?"
        shiori.say "On your knee?!?"
        mike.say "No, Shiori."
        mike.say "I want you to lie across me."
        show shiori surprised
        "She nods slowly, eyes wide as saucers."
        "Slowly, Shiori does as she's told, lowering herself over my knees."
        hide shiori
        show spank shiori
        with fade
        "I feel the weight of her body push the chair down."
        "And I enjoy the sensation of her curvy shape against my legs."
        shiori.say "Wh...what now, [hero.name]?"
        mike.say "Now I have to punish you, Shiori."
        mike.say "Punish you for letting my coffee go cold!"
        "Shiori lets out a little whimper as I lift her skirt."
        "But once her shapely ass is revealed, I don't waste anymore time."
        "The first slap is louder than I expected, and it makes Shiori yelp."
        show spank shiori spank surprised
        play sound spank
        with hpunch
        "But as one slap follows another, she begins to bite her lip instead."
        "This means that she's making whimpering sounds the whole time."
        "And she's wriggling around in my lap too, trying to endure her punishment."
        show spank shiori up pleasure
        mike.say "You've been a bad girl, Shiori."
        shiori.say "Y...yes, Sir!"
        show spank shiori spank
        play sound spank
        with hpunch
        mike.say "So you deserve to be punished."
        shiori.say "Oh yes!"
        show spank shiori up
        mike.say "You're a bad, naughty girl!"
        shiori.say "Yes...yes I am!"
        show spank shiori spank marks
        play sound spank
        with hpunch
        "I don't know if Shiori can feel it from where she's laid."
        show spank shiori ready
        "But my cock is hard as a rock right now!"
        "And if I keep this up much longer, I'm going to lose it!"
        mike.say "Ah...ahem..."
        mike.say "I think that's enough for now, Shiori."
        scene expression f"bg {game.room}"
        show shiori embarrassed
        with fade
        "Shiori scrambles up from my lap, pulling down her skirt as she does so."
        shiori.say "Y...yes, [hero.name]."
        hide shiori
    $ shiori.sub += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
