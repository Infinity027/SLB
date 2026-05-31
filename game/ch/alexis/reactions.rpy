label alexis_ice_cream_reaction_male:
    mike.say "Phew...it's crazy hot today, Alexis - let's get ice cream!"
    alexis.say "Yeah, I could really use something to cool me down!"
    "At the ice cream stall, I buy myself a cone with a couple of different scoops."
    "But Alexis orders herself a pretty fancy sundae that comes with a long spoon."
    mike.say "Huh...you're not messing around, Alexis!"
    alexis.say "Well, why not, [hero.name]?"
    alexis.say "Even eating an ice cream can be memorable experience!"
    "I watch, my mouth hanging open as Alexis begins to spoon ice cream into her mouth."
    "And I don't know what I'm more fascinated by."
    "The ice cream itself, or the way Alexis is eating it!"
    return

label alexis_ask_phone_male:
    mike.say "Oh, Alexis, I was gonna ask..."
    mike.say "Could I get your number?"
    alexis.say "Didn't I give it to you already?"
    if hero.charm >= 20 - alexis.love:
        show alexis happy
        $ hero.smartphone_contacts.append("alexis")
        alexis.say "Sure, [hero.name], of course you can have it!"
    else:
        show alexis annoyed
        $ alexis.love -= 1
        $ alexis.sub -= 1
        alexis.say "Hmm..."
        alexis.say "That must mean it doesn't feel like I'm ready to let you have it!"
    return

label alexis_ask_birthday_male:
    mike.say "Hey, Alexis..."
    mike.say "Remind me - when is your birthday?"
    if hero.charm >= 40 - alexis.love:
        show alexis happy
        $ alexis.flags.birthdayknown = True
        alexis.say "Really, [hero.name]?"
        alexis.say "How could you forget something like that?!?"
        alexis.say "It's Fall 1, just for the record."
    else:
        show alexis annoyed
        $ alexis.sub -= 1
        $ alexis.love -= 1
        alexis.say "Really, [hero.name]!"
        alexis.say "How long have we known each other?!?"
        alexis.say "If you can't be bothered to remember, then I can't be bothered to remind you!"
    return

label alexis_offer_a_drink_male:
    mike.say "I'm just going to the bar, Alexis."
    mike.say "You want a drink?"
    "Almost the second the words are out of my mouth, Alexis turns to face me."
    if alexis.is_visibly_pregnant:
        show alexis angry
        $ alexis.love -= 10
        alexis.say "[hero.name]!"
        alexis.say "Are you serious?!?"
        alexis.say "You know I can't drink in my condition!"
        $ hero.cancel_activity()
        hide alexis
    elif (hero.charm >= 60 - alexis.love and alexis.flags.drinks < 2) or date_girl == alexis:
        show alexis happy
        alexis.say "Oh, sure, [hero.name]."
        alexis.say "You mind grabbing me a craft beer?"
        hide alexis
        show drink alexis
        if alexis.love <= 25:
            $ alexis.love += 1
        elif date_girl == alexis and game.active_date:
            $ game.active_date.score += 5
        call expression alexis.get_chat from _call_expression_207
        hide drink alexis
        $ alexis.set_flag("drinks", 1, "day", mod="+")
    else:
        show alexis annoyed
        alexis.say "Nah, I'm fine right now."
        alexis.say "Wait a minute..."
        alexis.say "Are you trying to get me drunk?"
        $ hero.cancel_activity()
        hide alexis
    return

label alexis_slap_ass_intro_male:
    "Okay, I try to be a pretty cool, modern guy."
    "But sometimes I just can't help myself."
    "And one of those times is right now."
    "Specifically as I'm watching Alexis's ass!"
    "It's just so perfect in every possible way."
    "I've slapped it before I know what I'm doing!"
    return

label alexis_slap_ass_happy_male:
    "Alexis stops dead in her tracks."
    "And her jaw drops in sheer amazement."
    alexis.say "Did you just..."
    alexis.say "You did!"
    "She shakes her head, eyes wide as she does so."
    "But she also cracks a smile and then shoots me a wink."
    "So I guess that means she liked it!"
    return

label alexis_slap_ass_angry_male:
    "Alexis stops dead in her tracks."
    "And her jaw drops in sheer amazement."
    alexis.say "Did you just..."
    alexis.say "You did!"
    alexis.say "What are you, [hero.name]?"
    alexis.say "Some kind of Neanderthal?!?"
    "Alexis shakes her head as she walks off."
    "Leaving me with no delusions as to the fact she's not happy."
    return

label alexis_breakup_male:
    show alexis
    "I can feel my nerve threatening to break even as I open my mouth to speak."
    "But I already talked myself into doing this here and now."
    "So it's too late to back down - I have to go through with it..."
    mike.say "Alexis..."
    mike.say "There's something I need to tell you..."
    "Alexis turns to face me, her expression changing before my eyes."
    "Before she looked happy and carefree."
    "But now worry spreads across her features."
    alexis.say "[hero.name]..."
    alexis.say "I don't like the sound of this..."
    "I hate the sound in Alexis's voice as she says this."
    "It's a mixture of fear, and worse, resignation."
    "Like she always knew this was going to happen."
    mike.say "It's about us, Alexis."
    mike.say "I'm sorry."
    mike.say "But I think we should break it off."
    show alexis sad
    "For a moment I think Alexis is going to burst into tears."
    show alexis angry
    "But then she seems to stiffen, like she's taking a hold of herself."
    alexis.say "You never really forgave me, did you?"
    alexis.say "You said what happened in high school was behind us."
    alexis.say "You told me that it didn't matter anymore."
    alexis.say "But you never really believed that."
    alexis.say "And I was a fool to believe that you did!"
    mike.say "No, Alexis!"
    mike.say "It's not like that, I promise!"
    "At this, Alexis rounds on me."
    "I can see the anger in her eyes as she stares me down."
    alexis.say "You mean there's something else?!?"
    alexis.say "Something worse that stopped you wanting me?"
    alexis.say "Then I guess I'm never going to be good enough for you!"
    "Alexis turns on her heel and begins to walk away."
    "I have no idea what to say to her right now."
    "What words can I possibly utter that won't make it worse?"
    "But still, I feel like I have to try."
    mike.say "Alexis..."
    mike.say "Alexis, wait!"
    alexis.say "Shut up, [hero.name] - just stop talking!"
    alexis.say "I don't ever want to hear your voice or see your face again!"
    return

label alexis_go_steady_intro_male:
    mike.say "I was going to ask you something, Alexis..."
    mike.say "Things are going pretty well for us right now, yeah?"
    mike.say "So maybe we could say we're going steady?"
    return

label alexis_go_steady_yes_male:
    alexis.say "Of course we can, [hero.name]!"
    alexis.say "I mean...I kind of thought we already were..."
    alexis.say "But if you want to make it official, then okay!"
    hide alexis
    show alexis kiss
    $ alexis.flags.kiss += 1
    "Alexis leans in and kisses me on the lips."
    "It takes me by surprise for a moment."
    "But then I return the favour with genuine enthusiasm."
    return

label alexis_go_steady_no_male:
    alexis.say "Ah..."
    alexis.say "I'm not ready for that yet, [hero.name]."
    alexis.say "I'd rather not rush into anything, okay?"
    return

label alexis_pet_intro_male:
    "Without thinking, I reach out and pat Alexis on the head."
    "I meant it as a show of affection and nothing more."
    "But now I realise I have no idea how she'll react..."
    return

label alexis_pet_happy_male:
    alexis.say "Oh..."
    alexis.say "You...you never did that before, [hero.name]!"
    alexis.say "But it made me feel all fuzzy inside!"
    return

label alexis_pet_annoyed_male:
    alexis.say "W...wait a minute, [hero.name]!"
    alexis.say "What the hell was that?"
    alexis.say "Since when did you pat me on the head like a dog?!?"
    return

label alexis_massage_intro_male:
    mike.say "You're really tense today, Alexis."
    mike.say "Would you like me to give you a massage?"
    mike.say "It always helps me to loosen up!"
    return

label alexis_massage_accept_male:
    alexis.say "Huh..."
    alexis.say "You must have read my mind, [hero.name]!"
    alexis.say "A massage sounds like a great idea right now."
    return

label alexis_massage_refuse_male:
    alexis.say "Huh?"
    alexis.say "Oh no, [hero.name], not now."
    alexis.say "I'm not in the mood for someone's hands all over me."
    return

label alexis_piercing_nipples_reaction_male:
    alexis.say "How did I get all the way through high-school without getting these things pierced?"
    alexis.say "Especially when it feels this good!"
    alexis.say "You should have convinced me to do it years ago!"
    return

label alexis_piercing_navel_reaction_male:
    alexis.say "Wow..."
    alexis.say "I just can't get over how good my belly-button looks!"
    alexis.say "Thanks for talking me into getting it done."
    return

label alexis_piercing_clit_reaction_male:
    alexis.say "I love the way it feels, [hero.name]!"
    alexis.say "And I love that nobody else knows it's down there too!"
    alexis.say "This was such a great idea."
    return

label alexis_piercing_head_reaction_male:
    alexis.say "Mmm..."
    alexis.say "This thing feels really good against my tongue."
    alexis.say "Imagine how good it'll feel when I use it on you!"
    return

label alexis_piercing_nose_reaction_male:
    alexis.say "Huh...I really wasn't sure about getting this done."
    alexis.say "But now that I have..."
    alexis.say "Well, I really like the look of it!"
    return

label alexis_movie_disliked_reaction_male:
    alexis.say "Well, that's two hours of my life I'm never getting back!"
    return

label alexis_movie_indifferent_reaction_male:
    alexis.say "Urgh...don't you think a boring movie sucks even worse than a bad one?"
    return

label alexis_movie_liked_reaction_male:
    alexis.say "I'm SO glad we did this - that was an amazing film!"
    return

label alexis_belly_kiss_male:
    show alexis whining at center, zoomAt(1.25, (640, 880))
    alexis.say "Urgh..."
    alexis.say "Phew..."
    alexis.say "I can't get used to hauling this huge belly around!"
    show alexis annoyed
    "I look up to see Alexis puffing and panting, her hands on her stomach."
    "And naturally I hurry to do all that I can to help."
    "Because I'm more than eager to be a good partner and prospective father."
    mike.say "You want to sit down, Alexis?"
    mike.say "Put your feet up for a while?"
    mike.say "Or maybe a warm bath would help?"
    show alexis sadsmile
    "Alexis looks at me helplessly."
    "And for a moment I think that she's actually about to burst into tears."
    "Which would make sense, as her hormones must be going crazy right now."
    show alexis talkative
    alexis.say "Oh, [hero.name]..."
    alexis.say "I'm so glad I didn't look like this when we first met!"
    show alexis sadsmile
    mike.say "What's that supposed to mean, Alexis?"
    mike.say "We were just kids back then."
    mike.say "So that would have been pretty weird!"
    show alexis whining
    alexis.say "You know what I mean!"
    alexis.say "You'd never have fallen for me if I was this fat."
    show alexis sad
    "I instantly start shaking my head."
    mike.say "You're not fat, Alexis..."
    mike.say "You're glowing, and you're beautiful!"
    show alexis annoyed
    "Alexis looks like she's about to shoot me down."
    show alexis stuned at center, traveling(1.75, 1.0, (640, 880))
    "But then she stops in her tracks, as I'm already kneeling down."
    show alexis surprised
    alexis.say "[hero.name]..."
    alexis.say "What are you doing?"
    show alexis stuned
    "By now I've lifted her top and begun to plant kisses on her belly."
    "And I only explain myself between placing them and moving on to the next spot."
    mike.say "I'm kissing something beautiful, Alexis."
    mike.say "Because I like to kiss beautiful things."
    mike.say "I think they deserve to be kissed."
    "I don't look up at Alexis as I say all of this."
    show alexis smile
    "But I take her silence as a good sign, that I'm winning her over."
    "And when I feel her begin to stroke my hair, I know that it's working."
    "Though it's the long sigh of relief and satisfaction a moment later that confirms it."
    "That lets me know I've managed to reach her in the way I intended."
    return

label alexis_belly_caress_male:
    show alexis at center, zoomAt(1.25, (640, 880))
    "I feel the sensation of Alexis beside me, which is nothing unusual."
    "The weight of her leaning against me is familiar and comforting."
    show alexis at center, traveling(1.5, 1.0, (640, 1040))
    "But then I feel something being pushed forcibly into my side."
    "And I look down to see that it's the curve of her swelling belly."
    mike.say "Hey, Alexis..."
    mike.say "What are you doing?"
    mike.say "Trying to use that thing to barge me out of the way?"
    "The moment the words are out of my mouth, I know I made a mistake."
    show alexis upset
    "Because Alexis gives me a hurt frown, and furrows her brow."
    show alexis angry
    alexis.say "Really, [hero.name]?"
    alexis.say "I'm just trying to get some affection out of you."
    alexis.say "I feel like every part of me is swollen and sore right now."
    alexis.say "And you're fifty percent responsible for all that discomfort!"
    show alexis upset
    "I make an effort to change my attitude as soon as I hear this."
    "Because I had no idea Alexis was in such an emotional state."
    "Or that she was feeling so needy!"
    mike.say "Ah..."
    mike.say "Sorry, Alexis..."
    mike.say "I see how that could have sounded insensitive."
    show alexis sadsmile at center, traveling(1.75, 1.0, (640, 880))
    "As I'm saying all of this, I'm reaching out to touch Alexis's belly."
    "And the apology, along with the human contact, seems to do the trick."
    show alexis normal
    "Because Alexis lets out a sigh and instantly starts to relax."
    "She leans even more of her weight against me, sagging as she does so."
    "And for once it begins to feel like there's no need for words."
    "I can pretty much tell what she wants simply by listening."
    "So that's just what I do, responding to Alexis's cues."
    show alexis happy
    "Soon enough it feels like the stress and irritation is long gone."
    "And all of the anger that Alexis was feeling simply melts away."
    "All of which leaves me wondering if everything in life could be so simple."
    "If we could defuse other problems simply by gently stroking a needy belly."
    return

label alexis_belly_listen_male:
    show alexis surprised at center, zoomAt(1.25, (640, 880))
    alexis.say "[hero.name]..."
    alexis.say "Get over here..."
    alexis.say "Quickly!"
    show alexis smile
    "I'm already in a state of heightened alert for Alexis needing me."
    "The pregnancy is something that'll put you on constant alert."
    show alexis at center, traveling(1.75, 1.0, (640, 880))
    "So I make it over to her in record time, ready to lend assistance."
    mike.say "I'm here, Alexis..."
    mike.say "What's the problem?"
    mike.say "Whatever you need, just say it!"
    "Instead of speaking up, Alexis pulls up her top."
    "Which of course reveals the huge curve of her belly."
    "My eyes go wide and I look her in the face."
    "All the while expecting some dramatic proclamation to follow."
    "But much to my surprise, Alexis proceeds to grab hold of my head."
    show alexis normal at center, traveling(2.0, 0.5, (640, 980))
    "With one hand on either side of it, she suddenly pulls me downwards."
    "And a moment later I find my ear pressed hard against her stomach."
    mike.say "Wha..."
    mike.say "What are you..."
    show alexis wink
    alexis.say "SSSHHH!"
    show alexis talkative
    alexis.say "Shut up and listen..."
    alexis.say "The baby's moving!"
    show alexis smile
    "I'm about to tear myself free of Alexis's grasp."
    "That and to tell her off for manhandling me in such a fashion."
    "But then I hear the odd, underwater sound coming from inside her belly."
    "It's vague and weird in the extreme, but it undeniably something moving."
    "Which has to mean that I'm listening to the sound of our baby in there!"
    mike.say "Alexis..."
    mike.say "I can hear the baby..."
    mike.say "It's moving in there!"
    show alexis mean
    alexis.say "Well, duh!"
    alexis.say "Isn't that what I just said?"
    show alexis happy
    "Even though Alexis is kind of telling me off, I recognise something in her voice."
    "It's a sense of pride and happiness that she can't hope to hide under sarcasm."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
