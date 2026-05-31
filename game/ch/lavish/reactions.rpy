label lavish_ice_cream_reaction_male:
    mike.say "I'm WAY too hot, Lavish - let's grab an ice cream!"
    lavish.say "Mmm...okay - that sounds nice!"
    "At the ice cream stall, I buy myself a cone with a couple of different scoops."
    "Lavish chooses the same thing, but with her own combination of flavours."
    lavish.say "Oh...oh dear..."
    lavish.say "My...my ice cream's getting away!"
    "As Lavish tries to lick her cone, one of the scoops slips off."
    "It runs down her arm and she chases it with her tongue, licking desperately."
    "I can't take my eyes off her as she does this, watching her cheeks flush red with embarrassment."
    "And all I can think of is Lavish using her tongue like that in an intimate situation!"
    return

label lavish_ask_phone_male:
    mike.say "I wanted to ask for your number, Lavish."
    mike.say "If you'd let me have it?"
    if hero.charm >= 20 - lavish.love:
        show lavish happy
        $ hero.smartphone_contacts.append("lavish")
        lavish.say "Of course you can have my number, [hero.name]!"
        lavish.say "I was waiting for you to ask!"
    else:
        show lavish annoyed
        $ lavish.love -= 1
        $ lavish.sub -= 1
        lavish.say "Hmm..."
        lavish.say "I don't think now is the right time, [hero.name]."
        lavish.say "We're not there yet."
    return

label lavish_ask_birthday_male:
    mike.say "I was wondering about something, Lavish."
    mike.say "When's your birthday, huh?"
    if hero.charm >= 40 - lavish.love:
        show lavish happy
        $ lavish.flags.birthdayknown = True
        lavish.say "Oh, it's no secret, [hero.name]."
        lavish.say "It's on Spring 3."
        lavish.say "Thanks for taking an interest!"
    else:
        show lavish annoyed
        $ lavish.sub -= 1
        $ lavish.love -= 1
        lavish.say "That's kind of a personal question, [hero.name]."
        lavish.say "Not a professional one."
        lavish.say "And not one that I'm going to answer, either!"
    return

label lavish_offer_a_drink_male:
    mike.say "Can I get you a drink from the bar, Lavish?"
    mike.say "I was just about to get a round in."
    "Almost the second the words are out of my mouth, Lavish turns to face me."
    if lavish.is_visibly_pregnant:
        show lavish angry
        $ lavish.love -= 10
        lavish.say "Have you forgotten that one of us is pregnant, [hero.name]?!?"
        lavish.say "It wouldn't have slipped your mind if YOU were the one carrying our child!"
        $ hero.cancel_activity()
        hide lavish
    elif (hero.charm >= 60 - lavish.love and lavish.flags.drinks < 2) or date_girl == lavish:
        show lavish happy
        lavish.say "Aw..."
        lavish.say "That's so kind of you, [hero.name]."
        lavish.say "Could I get a white wine please?"
        hide lavish
        show drink lavish
        if lavish.love <= 25:
            $ lavish.love += 1
        elif date_girl == lavish and game.active_date:
            $ game.active_date.score += 5
        call expression lavish.get_chat from _call_expression_247
        hide drink lavish
        $ lavish.set_flag("drinks", 1, "day", mod="+")
    else:
        show lavish annoyed
        lavish.say "I'd rather buy my own drinks, [hero.name]."
        lavish.say "It's easier to stay in control that way."
        $ hero.cancel_activity()
        hide lavish
    return

label lavish_slap_ass_intro_male:
    "I love being seen with Lavish - she's stunning and so poised."
    "Even the way she walks speaks volumes about how elegant she is."
    "But her ass is another matter entirely, and it speaks a different language."
    "It affects me on an almost animal level."
    "Which is why I can't resist slapping it..."
    return

label lavish_slap_ass_happy_male:
    "The moment my hand connects with her buttock, Lavish stops dead."
    "She remains frozen for what feels like forever."
    "But then she turns her head to stare at me."
    lavish.say "[hero.name]..."
    lavish.say "Am I imagining things."
    lavish.say "Or did you actually just slap my ass?"
    "All I can do is give her a helpless nod."
    "In response to which, Lavish gives me an enigmatic smile."
    lavish.say "Okay..."
    lavish.say "Just don't make a habit of it!"
    return

label lavish_slap_ass_angry_male:
    "The moment my hand connects with her buttock, Lavish stops dead."
    "She remains frozen for what feels like forever."
    "But then she turns her head to stare at me."
    lavish.say "[hero.name]..."
    lavish.say "Am I imagining things."
    lavish.say "Or did you actually just slap my ass?"
    "All I can do is give her a helpless nod."
    "In response to which, Lavish gives me a cross frown."
    lavish.say "Urgh..."
    lavish.say "I'll let you off this once."
    lavish.say "But next time I won't be so generous!"
    return

label lavish_breakup_male:
    show lavish
    "I can't even look Lavish in the eyes when the time comes to say my piece."
    "It's never been easy for me to tell a girl that I want to break up with her."
    "And maybe that's because I remember how it feels to be dumped myself."
    "But all the same, I can't keep putting it off..."
    mike.say "Hey, Lavish..."
    mike.say "We need to talk..."
    "I can see that Lavish is tuned into me the moment she looks around."
    "She already has a look of concern growing on her face as she does so."
    "What else was I expecting?"
    "She's one of the smartest girls I've ever dated."
    "So she was always going to be able to cut to the chase."
    lavish.say "Oh dear, [hero.name]."
    lavish.say "Does that mean what I think it means?"
    "What other choice do I have but to push on?"
    "I can't backtrack now, Lavish would never believe me."
    mike.say "I'm sorry, Lavish."
    mike.say "It's been fun, the time we've had together."
    mike.say "But I don't think we're going anywhere."
    mike.say "So we'd best end it now."
    mike.say "You know - while we just have the good memories?"
    show lavish annoyed
    "Lavish actually snorts at this."
    "And then she shakes her head."
    lavish.say "Well, this isn't going to be a good memory, [hero.name]."
    lavish.say "So you kind of shot that one down yourself!"
    mike.say "Come on, Lavish!"
    mike.say "Don't be like that!"
    lavish.say "I don't think you get it, [hero.name]."
    lavish.say "I never dated anyone in the workplace before you."
    lavish.say "I always kept my work life and my social life apart."
    lavish.say "But I broke that rule for you."
    lavish.say "And now I have to see you in the office every damn day!"
    mike.say "It doesn't have to be awkward, Lavish."
    mike.say "We can still be friends, as well as colleagues!"
    lavish.say "No, [hero.name], we can't."
    lavish.say "I see now that I was wrong to break my own rules."
    lavish.say "Just make sure you keep out of my way in the office."
    lavish.say "Because I'll be doing all I can to avoid you!"
    return

label lavish_go_steady_intro_male:
    mike.say "I was thinking, Lavish..."
    mike.say "We're getting on like a house on fire."
    mike.say "I think we should make it official."
    return

label lavish_go_steady_yes_male:
    lavish.say "You mean go steady, [hero.name]?"
    lavish.say "That's a great idea."
    lavish.say "I'd love to."
    "Lavish plants a neat little kiss on my cheek."
    "But I feel it far more deeply."
    "And it seems to touch every part of my body."
    return

label lavish_go_steady_no_male:
    lavish.say "Hmm..."
    lavish.say "I like you a lot, [hero.name]."
    lavish.say "But I'm not quite there yet."
    lavish.say "So I'll pass."
    return

label lavish_pet_intro_male:
    "Without thinking, I pat Lavish on the head."
    "And the moment I do so, I know I've taken a risk."
    "Because there's no way of knowing how she'll react."
    return

label lavish_pet_happy_male:
    lavish.say "Oh my..."
    lavish.say "Did you just..."
    lavish.say "I should be mad at you, [hero.name]."
    lavish.say "And I don't know why, but I'm not!"
    return

label lavish_pet_annoyed_male:
    lavish.say "Oh no..."
    lavish.say "You did NOT just pat me on the head, [hero.name]."
    lavish.say "We're going to pretend that you didn't, anyway!"
    return

label lavish_massage_intro_male:
    mike.say "You seem tense today, Lavish."
    mike.say "Like you're shoulders are knotted up."
    mike.say "Would you like me to rub them for you?"
    mike.say "Maybe even give you a massage?"
    return

label lavish_massage_accept_male:
    lavish.say "Hmm..."
    lavish.say "I am in a lot of pain, [hero.name]."
    lavish.say "It's kind of you to notice and offer to help."
    lavish.say "Yes...I think I would like a massage."
    return

label lavish_massage_refuse_male:
    lavish.say "Urgh..."
    lavish.say "No thanks, [hero.name]."
    lavish.say "The last thing I want right now is anyone touching me!"
    return

label lavish_piercing_nipples_reaction_male:
    lavish.say "I...I never thought about getting my nipples pierced before now."
    lavish.say "I thought it was...you know...unprofessional!"
    lavish.say "But now that you talked me into it...I really like it!"
    return

label lavish_piercing_navel_reaction_male:
    lavish.say "Hmm..."
    lavish.say "I was worried that a belly-button piercing might look trashy."
    lavish.say "But I like it, and nobody can see it under my clothes too."
    return

label lavish_piercing_clit_reaction_male:
    lavish.say "You...you can't let anyone else know this, [hero.name]."
    lavish.say "But I LOVE the feeling of having this thing down there!"
    lavish.say "I just hope I can keep my mind off of it at work!"
    return

label lavish_piercing_head_reaction_male:
    lavish.say "Mmm...I'm going to have to keep my mouth closed at work!"
    lavish.say "But that doesn't mean literally, [hero.name]!"
    lavish.say "Anyway...I do actually like the feel of this thing..."
    return

label lavish_piercing_nose_reaction_male:
    lavish.say "I like the look of this, [hero.name]!"
    lavish.say "It makes me feel pretty exotic..."
    lavish.say "But you have to promise to make sure it's okay at work!"
    lavish.say "I don't want it to get in the way of my career!"
    return

label lavish_movie_disliked_reaction_male:
    lavish.say "Ah...I really didn't connect with that film, I just didn't like it at all."
    return

label lavish_movie_indifferent_reaction_male:
    lavish.say "I thought that was pretty boring - not my kind of thing really."
    return

label lavish_movie_liked_reaction_male:
    lavish.say "I have to say that I LOVED that film - instant favourite for me!"
    return

label lavish_call_in:
    "I'm just looking at my coffee cup, thinking that I need a refill."
    "But then it dawns on me that I feel like I need something a little stronger."
    "With that in mind, I pick up the phone on my desk and dial a certain number."
    lavish.say "Hello..."
    lavish.say "Lavish here!"
    mike.say "Hey, Lavish, it's me..."
    mike.say "Would you mind stepping into my office for a moment?"
    lavish.say "No problem - I'll be right there!"
    "I put down the phone and glance at the door."
    "Within literally twenty seconds there's an efficient knock."
    mike.say "Come in, Lavish."
    "The door opens and Lavish walks in, notepad in hand."
    "She closes the door behind her and strides over to my desk."
    show lavish
    lavish.say "Here I am, [hero.name]."
    lavish.say "What can I do for you?"
    return

label lavish_belly_kiss_male:
    show lavish at center, zoomAt(1.25, (640, 880))
    mike.say "Erm..."
    mike.say "Lavish..."
    "As if she can sense my emotions from the tone of my voice, Lavish begins to chuckle."
    "And she looks at me with those beguiling eyes of hers, amused to hear what I have to say."
    show lavish talkative
    lavish.say "Yes, [hero.name]…"
    lavish.say "Was there something you wanted to ask me?"
    show lavish normal
    "How does she do that?"
    "Look at me in that way and instantly make me start to sweat!"
    mike.say "Well, I was just thinking..."
    mike.say "It's been a while since..."
    mike.say "Since we last...kissed!"
    show lavish at center, traveling(1.5, 0.5, (640, 1040))
    "Lavish nods as she walks over to me and leans in closer."
    "And I can already see her closing her eyes as she does so."
    show lavish flirt
    lavish.say "You're right..."
    lavish.say "It has!"
    hide lavish
    show lavish kiss
    with fade
    "The kiss is everything I was hoping for."
    "It's long, lingering and very passionate."
    "But when it ends, I realise that Lavish's belly is pressed against me."
    hide lavish kiss
    show lavish a flirt at center, zoomAt(1.5, (640, 1040))
    with fade
    "And that's when instinct seems to take over."
    show lavish a at center, traveling(2.0, 1.0, (640, 980))
    "Because I find myself getting down on my knees in front of her."
    "The next thing I know, I'm lifting up her top."
    "Then I'm placing my lips against the curve of her belly."
    "And planting kisses all over it, trying to cover every inch."
    show lavish embarrassed
    "Lavish seems totally taken aback by what I'm doing."
    "She looks down at me, eyes wide with amazement."
    "But every time I sneak a glance up at her, I notice something."
    show lavish pleased
    "And that's the smile on her face getting ever wider."
    "Soon enough, Lavish is practically beaming at me."
    "Seeming to love the attention that I'm bestowing on her."
    return

label lavish_belly_caress_male:
    show lavish at center, zoomAt(1.25, (640, 880))
    "I've always thought of Lavish as being one of the most beautiful girls I've ever seen."
    "And that's not just me gushing on account of her being my girlfriend too."
    "But since she got pregnant, I don't know how to even begin explaining it."
    "It's like she's just started to get more beautiful as she's gotten bigger!"
    "Now she seems to have some kind of glow about her, almost like you can actually see it."
    "And I can't stop looking at her, as well as wanting to touch her all the time!"
    show lavish whining
    lavish.say "[hero.name]…"
    lavish.say "Will you please stop staring at me like that?"
    lavish.say "I know that I've put on some weight recently, okay?"
    show lavish sad
    "At first I can't actually make sense of what Lavish is saying."
    "I feel like I've missed out on the first part of the conversation."
    "And then it suddenly dawns on me that she thinks I'm disapproving of her weight."
    "That I'm staring at her because she thinks that I think she's fat!"
    mike.say "Are you crazy, Lavish?!?"
    mike.say "I'm not staring at you because you got fat."
    mike.say "Which, by the way, you are not!"
    mike.say "I'm staring at you because you're frikin beautiful!"
    show lavish stuned
    "Lavish stares at me with a stunned look on her face."
    "Like that was the last thing she expected to hear me say."
    show lavish surprised
    lavish.say "You're serious?"
    lavish.say "You...you really mean that?"
    show lavish a normal at center, traveling(1.5, 0.3, (640, 1040))
    "I hurry over to Lavish and reach out to touch the curve of her belly."
    "And the moment it's in my hands, I can't keep from smiling like a fool."
    mike.say "Oh, Lavish..."
    mike.say "You are SO hot right now."
    mike.say "So hot I can't keep my hands off of you!"
    show lavish a pleased
    "Lavish smiles and puts a hand atop mike as I caress her belly."
    "Then I feel her leaning into me, putting her head on my shoulder."
    "And I hope that I've managed to convince her of my feelings."
    "Because this is perhaps one of the times I've been the most honest in my life."
    "Admitting the truth I didn't think was even possible before now."
    "That there was anything in the world that could make Lavish more beautiful than before."
    return

label lavish_belly_listen_male:
    show lavish at center, zoomAt(1.25, (640, 880))
    pause 0.1
    show lavish a normal at center, traveling(1.5, 0.3, (640, 1040))
    mike.say "Hold still, Lavish..."
    mike.say "I want to try something out..."
    "I already have my hands on Lavish's belly as I'm saying all of this."
    "And I'm in the act of kneeling down in front of her too."
    show lavish stuned
    "Lavish's first instinct is to pull back a little."
    "Which is understandable, as she has no idea what I'm trying to do."
    show lavish surprised
    lavish.say "Hey!"
    lavish.say "What are you..."
    show lavish a at center, traveling(2.0, 1.0, (640, 980))
    "But then I guess that Lavish sees me putting an ear to her belly."
    "And that must be enough to pique her interest."
    "As she stops pulling away and lets me get on with it."
    show lavish a talkative
    lavish.say "Ah..."
    lavish.say "You mind if I ask something, [hero.name]?"
    show lavish a normal
    mike.say "No, Lavish..."
    mike.say "Ask away..."
    show lavish a talkative
    lavish.say "Okay, here goes..."
    lavish.say "You mind telling me what in the hell you're doing?"
    show lavish a embarrassed
    "The question strikes me as more than a little redundant."
    "But as I want to be able to keep on going, I decide to humour her."
    mike.say "I'm listening to the baby, of course."
    mike.say "What else would I be doing down here?"
    show lavish a talkative
    lavish.say "Oh, of course..."
    lavish.say "How silly of me not to get that!"
    lavish.say "So..."
    lavish.say "What can you hear down there?"
    show lavish a normal
    mike.say "It's pretty wild, Lavish..."
    mike.say "Like listening to one of those chill-out tracks."
    mike.say "You know, the one's with the whale sounds in them?"
    show lavish a talkative
    lavish.say "Hey, you should know better than that!"
    show lavish a wink
    lavish.say "Don't go mentioning whales around me..."
    lavish.say "Not when it was you that got me into this state in the first place!"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
