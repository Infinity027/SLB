label morgan_ice_cream_reaction_male:
    mike.say "Wow, I need to cool down, Morgan - what do you say we grab an ice cream?"
    if morgan.male >= 66:
        morgan.say "Yeah, I could go for one right now!"
    elif morgan.male >= 33:
        morgan.say "Phew, I sure could use one!"
    else:
        morgan.say "Oh dear, I definitely need one!"
    "At the ice cream stall, I buy myself a cone with a couple of different scoops."
    "Morgan chooses an ice lolly, a deep, dark red that glistens in the sun."
    mike.say "Ooh...those things always give me brain-freeze!"
    if morgan.male >= 66:
        morgan.say "Not me - I must be made of tougher stuff!"
    elif morgan.male >= 33:
        morgan.say "Not me - I love them!"
    else:
        morgan.say "Aw, poor you - but I love them!"
    "She proceeds to lick at the ice lolly, winking as she does so."
    "And for once it's not the coldness of the ice that makes my brain-freeze."
    "Instead it's the irresistible sight of Morgan licking away eagerly that does it!"
    return

label morgan_ask_phone_male:
    mike.say "Can I have your number, Morgan?"
    mike.say "We didn't swap them yet!"
    if hero.charm >= 20 - morgan.love:
        show morgan happy
        $ hero.smartphone_contacts.append("morgan")
        morgan.say "We didn't?"
        morgan.say "Then we really should!"
        morgan.say "There you go, [hero.name]."
    else:
        show morgan annoyed
        $ morgan.love -= 1
        $ morgan.sub -= 1
        morgan.say "I know, [hero.name], I know."
        morgan.say "I just don't think we're ready for that yet."
        morgan.say "Almost, but not quite."
    return

label morgan_ask_birthday_male:
    mike.say "When is it your birthday, Morgan?"
    mike.say "I can't remember the date!"
    if hero.charm >= 40 - morgan.love:
        show morgan happy
        $ morgan.flags.birthdayknown = True
        morgan.say "Wow, [hero.name], your brain's like Swiss Cheese!"
        morgan.say "It's Winter 15, remember?"
    else:
        show morgan annoyed
        $ morgan.sub -= 1
        $ morgan.love -= 1
        morgan.say "Wow, [hero.name], you never did pay any attention to me back in the day!"
        morgan.say "So you can forget me telling you all that stuff now!"
    return

label morgan_offer_a_drink_male:
    mike.say "Morgan, I'm headed to the bar."
    mike.say "Would you like me to get you something to drink?"
    "Almost the second the words are out of my mouth, Morgan turns to face me."
    if morgan.is_visibly_pregnant:
        show morgan angry
        $ morgan.love -= 10
        if morgan.male <= 33:
            morgan.say "Oh no, [hero.name]!"
            morgan.say "Won't you please think of the baby?!?"
        elif morgan.male <= 66:
            morgan.say "Ah, did you forget that I'm pregnant?"
            morgan.say "Urgh...you're so irresponsible sometimes!"
        else:
            morgan.say "What the fuck?"
            morgan.say "Did you forget I was pregnant, asshole?!?"
        $ hero.cancel_activity()
        hide morgan
    elif (hero.charm >= 60 - morgan.love and morgan.flags.drinks < 2) or date_girl == morgan:
        show morgan happy
        if morgan.male <= 33:
            morgan.say "Oh, that's be sweet of you, [hero.name]!"
            morgan.say "Could I get a white wine, please?"
        elif morgan.male <= 66:
            morgan.say "Oh, yeah, [hero.name], that's cool."
            morgan.say "Can I get a beer?"
        else:
            morgan.say "Sweet, [hero.name]."
            morgan.say "Mine's a vodka and tonic, yeah?"
        hide morgan
        show drink morgan
        if morgan.love <= 25:
            $ morgan.love += 1
        elif date_girl == morgan and game.active_date:
            $ game.active_date.score += 5
        call expression morgan.get_chat from _call_expression_257
        hide drink morgan
        $ morgan.set_flag("drinks", 1, "day", mod="+")
    else:
        show morgan annoyed
        if morgan.male <= 33:
            morgan.say "Oh no, no way!"
            morgan.say "You're trying to get me drunk!"
        elif morgan.male <= 66:
            morgan.say "Ah, no, [hero.name]."
            morgan.say "I'm cool."
        else:
            morgan.say "What the fuck?"
            morgan.say "Since when did I need YOU to buy ME a drink?"
        $ hero.cancel_activity()
        hide morgan
    return

label morgan_slap_ass_intro_male:
    "Morgan might be on the shorter side, but she's perfectly in scale."
    "That petite body's tight and hot as hell, moving like a dream."
    "And her ass - I could write a book about that thing!"
    "But right now, I just can't resist slapping it!"
    return

label morgan_slap_ass_happy_male:
    "Morgan jumps at the sensation and cries out in surprise."
    if morgan.male <= 33:
        morgan.say "Oh my goodness!"
    elif morgan.male <= 66:
        morgan.say "Whoa..."
    else:
        morgan.say "What the hell?!?"
    morgan.say "[hero.name], did you just slap my butt?!?"
    "I shrug and nod by way of an answer."
    if morgan.male <= 33:
        morgan.say "Well..."
        morgan.say "I guess it IS a compliment!"
    elif morgan.male <= 66:
        morgan.say "You cheeky bastard!"
        morgan.say "I kind of like it!"
    else:
        morgan.say "It's cool, [hero.name]."
        morgan.say "So long as I get to do the same to you!"
    return

label morgan_slap_ass_angry_male:
    "Morgan jumps at the sensation and cries out in surprise."
    if morgan.male <= 33:
        morgan.say "Oh my goodness!"
    elif morgan.male <= 66:
        morgan.say "Whoa..."
    else:
        morgan.say "What the hell?!?"
    morgan.say "[hero.name], did you just slap my butt?!?"
    "I shrug and nod by way of an answer."
    if morgan.male <= 33:
        morgan.say "Ooh..."
        morgan.say "How dare you!"
    elif morgan.male <= 66:
        morgan.say "Urgh..."
        morgan.say "That's kind of demeaning, you know?"
    else:
        morgan.say "Don't do that again."
        morgan.say "Unless you want a broken arm!"
    return

label morgan_breakup_male:
    show morgan
    "It's like tearing off a plaster when you just know that it's going to hurt."
    "You have to do it eventually, and it gets harder the longer you put it off."
    "So in the end, you just have to grit your teeth and get on with it..."
    mike.say "Morgan..."
    mike.say "I've been thinking lately..."
    "Morgan turns to me with a smile on her face."
    "She doesn't seem to have picked up on the seriousness of my tone."
    morgan.say "Well, there's a first time for everything!"
    "But the moment she sees the look on my face, her own drops too."
    morgan.say "Oh no..."
    morgan.say "I think I can guess what you're thinking, [hero.name]!"
    "I can feel the conversation slipping away from me."
    "And I know that if it does, I can't get my message over."
    "So I rush to speak before it's too late."
    mike.say "I...I just think it's not working out, Morgan."
    mike.say "It's been great hanging out with you so much."
    mike.say "But maybe that's because we're supposed to be friends, you know?"
    mike.say "Close friends for sure, but still just friends."
    show morgan annoyed
    "Morgan frowns and furrows her brow at this."
    "She looks like she's getting mad, but keeping a lid on it somehow."
    morgan.say "How can you say something like that, [hero.name]?"
    morgan.say "Last time we were just friends, you didn't notice me at all."
    morgan.say "Hell, you even thought I was a guy!"
    morgan.say "I can't go back to being just a friend to you."
    morgan.say "Not after how much us being together changed me!"
    mike.say "Problem is, Morgan, it's the changes that scare me."
    mike.say "I'm worried that it's just the novelty of it all that's got me hooked!"
    "Morgan takes a step back and shakes her head at me."
    "And I can see the beginnings of tears welling in her eyes."
    show morgan sad
    morgan.say "Wow, [hero.name], just wow!"
    morgan.say "I thought I was more to you than that."
    morgan.say "I thought we'd connected."
    morgan.say "That you'd become the guy I always wanted you to be!"
    morgan.say "But you're not - you're still a selfish little prick!"
    morgan.say "So do me a favour and go back to forgetting all about me."
    return

label morgan_go_steady_intro_male:
    mike.say "I feel like we're really going somewhere, Morgan."
    mike.say "Like this relationship is growing into something bigger."
    mike.say "And I think we should go steady because of that too."
    return

label morgan_go_steady_yes_male:
    if morgan.male >= 66:
        morgan.say "I was gonna say the same thing."
        morgan.say "But you beat me to it!"
    elif morgan.male >= 33:
        morgan.say "You're right, [hero.name]."
        morgan.say "I couldn't have said it better myself!"
    else:
        morgan.say "Ooh yes, [hero.name]!"
        morgan.say "We should totally do that!"
    return

label morgan_go_steady_no_male:
    if morgan.male >= 66:
        morgan.say "Nah, I don't think so."
        morgan.say "I'm cool as we are, [hero.name]."
    elif morgan.male >= 33:
        morgan.say "Hmm...I don't think so, [hero.name]."
        morgan.say "We're not there yet."
    else:
        morgan.say "Oh no, [hero.name]!"
        morgan.say "I'm SO not ready for that yet."
    return

label morgan_pet_intro_male:
    "Without thinking, I reach out and pat Morgan on the head."
    "As soon as I realise what I'm doing, I regret it."
    "I mean, how is any modern girl going to like me doing that?"
    return

label morgan_pet_happy_male:
    if morgan.male >= 66:
        morgan.say "Whoa..."
        morgan.say "If you do that to me, I get to slap your ass!"
    elif morgan.male >= 33:
        morgan.say "Wha..."
        morgan.say "I...I guess I should be flattered!"
    else:
        morgan.say "Ooh..."
        morgan.say "Ha ha...thank you, [hero.name]!"
    return

label morgan_pet_annoyed_male:
    if morgan.male >= 66:
        morgan.say "You EVER do that again, [hero.name]..."
        morgan.say "Well, you'll regret it, you know?"
    elif morgan.male >= 33:
        morgan.say "I'll let you off this time, [hero.name]."
        morgan.say "But you NEVER do that to me again!"
    else:
        morgan.say "Oh...oh dear..."
        morgan.say "You'd better not do that again, [hero.name]!"
    return

label morgan_massage_intro_male:
    mike.say "You seem kind of tense, Morgan."
    mike.say "Would you like me to help you out?"
    mike.say "You know, give you a quick massage?"
    return

label morgan_massage_accept_male:
    if morgan.male >= 66:
        morgan.say "Urgh...yeah!"
        morgan.say "Please, [hero.name] - but don't go holding back!"
    elif morgan.male >= 33:
        morgan.say "You know what, [hero.name]..."
        morgan.say "That sounds like a great idea!"
    else:
        morgan.say "Ooh...ouch!"
        morgan.say "Yes please, [hero.name]!"
    return

label morgan_massage_refuse_male:
    if morgan.male >= 66:
        morgan.say "Urgh...no way!"
        morgan.say "I can cope, [hero.name]."
    elif morgan.male >= 33:
        morgan.say "You know what, [hero.name]..."
        morgan.say "I don't want anyone touching me right now!"
    else:
        morgan.say "Ooh...ouch!"
        morgan.say "No, no, no, [hero.name] - you'll make it worse!"
    return

label morgan_piercing_nipples_reaction_male:
    if morgan.male >= 66:
        morgan.say "Huh!"
        morgan.say "I should have done this ages ago!"
        morgan.say "Piercing my nipples makes me feel so frikin hot!"
    elif morgan.male >= 33:
        morgan.say "This actually feel really good, [hero.name]."
        morgan.say "And I love how they make my nipples look too!"
        morgan.say "Thanks for talking me into doing this."
    else:
        morgan.say "Oh, wow!"
        morgan.say "It looks SO cute!"
        morgan.say "Thank you SO much for convincing me to have my nipples pierced!"
    return

label morgan_piercing_navel_reaction_male:
    if morgan.male >= 66:
        morgan.say "Wow...check it out, [hero.name]!"
        morgan.say "This thing is awesome, right?"
        morgan.say "I'm so stoked you talked me into getting it done!"
    elif morgan.male >= 33:
        morgan.say "Wow...it looks so cool!"
        morgan.say "And it makes me love my belly-button even more!"
        morgan.say "Thanks for suggesting it, [hero.name]."
    else:
        morgan.say "Wow...it looks SO cute!"
        morgan.say "I LOVE it, [hero.name]!"
        morgan.say "And I love YOU for convincing me to get it done too."
    return

label morgan_piercing_clit_reaction_male:
    if morgan.male >= 66:
        morgan.say "Whoa...this feels SO intense!"
        morgan.say "Like my pussy's come to life!"
        morgan.say "Good call, [hero.name], good call."
    elif morgan.male >= 33:
        morgan.say "Whoa...I never thought it'd feel like this!"
        morgan.say "If I'd known, I'd have done this years ago!"
        morgan.say "Thanks for encouraging me, [hero.name]."
    else:
        morgan.say "Whoo...it feels SO weird!"
        morgan.say "But, like good weird, you know?"
        morgan.say "This was such a great idea, [hero.name]!"
    return

label morgan_piercing_head_reaction_male:
    if morgan.male >= 66:
        morgan.say "Ha...this thing is great!"
        morgan.say "I can feel it whenever I open my mouth."
        morgan.say "Great idea, [hero.name]!"
    elif morgan.male >= 33:
        morgan.say "Ha...it feels so weird when I talk!"
        morgan.say "But I think I'm getting used to it."
        morgan.say "Thanks for suggesting this, [hero.name]."
    else:
        morgan.say "Oh my...I can feel it when I talk!"
        morgan.say "But it feels good when I do."
        morgan.say "This is going to be fun, [hero.name]!"
    return

label morgan_piercing_nose_reaction_male:
    if morgan.male >= 66:
        morgan.say "This looks so cool!"
        morgan.say "Like I'm a biker or something!"
        morgan.say "Thanks for suggesting it, [hero.name]."
    elif morgan.male >= 33:
        morgan.say "I wasn't sure at first."
        morgan.say "But I'm really starting to like it!"
        morgan.say "Thanks for convincing me, [hero.name]."
    else:
        morgan.say "Oooh...I just love it!"
        morgan.say "It's SO pretty!"
        morgan.say "Thank you, [hero.name]!"
    return

label morgan_movie_disliked_reaction_male:
    if morgan.male >= 66:
        morgan.say "Ouch - that was a massive pile of shit!"
    elif morgan.male >= 33:
        morgan.say "Yeah...I didn't like that at all!"
    else:
        morgan.say "Hmm...I don't think I liked that movie!"
    return

label morgan_movie_indifferent_reaction_male:
    if morgan.male >= 66:
        morgan.say "Ah...that was fucking boring as hell!"
    elif morgan.male >= 33:
        morgan.say "Meh...that was a load of nothing!"
    else:
        morgan.say "Oh dear...I almost fell asleep in there!"
    return

label morgan_movie_liked_reaction_male:
    if morgan.male >= 66:
        morgan.say "That kicked some serious ass!"
    elif morgan.male >= 33:
        morgan.say "Wow...that was a seriously great movie!"
    else:
        morgan.say "Yay...I loved that movie - it was great!"
    return

label morgan_belly_kiss_male:
    show morgan normal at center, zoomAt(1.25, (640, 880))
    mike.say "Morgan..."
    mike.say "I was just wondering if..."
    mike.say "You'd mind me..."
    mike.say "But if not, it's like, totally cool..."
    show morgan annoyed
    "Morgan waves a hand in my direction as I'm saying all of this."
    "And she shakes her head too, just to get the point across."
    show morgan annoyed
    morgan.say "Whoa, whoa, whoa..."
    morgan.say "Slow down, [hero.name]!"
    morgan.say "You sound like you're having a conversation with yourself!"
    show morgan sadsmile
    "I take a deep breath and nod my head."
    "Partly because I know that she's right."
    "And partly because I'm afraid of asking her for what I really want."
    mike.say "Okay, okay..."
    mike.say "I wanted to ask you something."
    mike.say "But I'm afraid you'll say no."
    show morgan normal
    "Morgan looks at me with renewed interest."
    "And she crosses her arms over her bump too."
    show morgan talkative
    morgan.say "Is that so?"
    morgan.say "Too afraid to want to know the actual answer?"
    show morgan normal
    "I nod my head, acknowledging that she's got me there."
    mike.say "Okay, I wanted to ask if..."
    mike.say "If I could kiss your belly?"
    show morgan stuned
    "Morgan raises an eyebrow at this."
    show morgan happy
    "And her smile is slow to spread across her face."
    show morgan talkative
    if morgan.male >= 66:
        morgan.say "Heh..."
        morgan.say "That's less weird than having a foot fetish!"
        morgan.say "So yeah, you can kiss it."
    elif morgan.male >= 33:
        morgan.say "That's not totally weird, [hero.name]…"
        morgan.say "Sure you can kiss it."
    else:
        morgan.say "That sounds cute, [hero.name]…"
        morgan.say "I'd love you to kiss it!"
    show morgan normal
    "Morgan sticks out her belly as an invitation."
    show morgan a at center, traveling(2.0, 1.0, (640, 980))
    "And I get down on my knees, then lean forwards."
    "I kiss it gently and with some real reverence too."
    "But the experience is pretty sweet, making me feel warm inside."
    "Morgan gazes down at me the whole time, an approving smile on her face."
    "And with every kiss that I place on her belly, I feel myself falling for her all the more."
    return

label morgan_belly_caress_male:
    show morgan normal at center, zoomAt(1.25, (640, 880))
    "Nobody ever sits you down and tells you all about the etiquette of pregnant bellies."
    "And it's ten times as bad when the belly in question is attached to your significant other."
    "Because you kind of feel possessive towards it, as you helped to make the kid inside there."
    "But it's still part of another person's body, so you can't just go helping yourself either."
    "All of this means that I find myself reaching out to touch Morgan's belly."
    "Then I remember myself and pull my hand back, hoping she didn't see me."
    "And at the same time wondering why I can't pluck up the courage to just ask her."
    show morgan annoyed
    morgan.say "[hero.name]…"
    morgan.say "What are you doing?"
    show morgan normal
    "Oh no, caught in the act!"
    "Morgan spotted me, and now she wants an explanation."
    mike.say "I...I..."
    mike.say "I just wanted to..."
    mike.say "To touch your bump, Morgan."
    show morgan happy
    "The moment that I make the admission, Morgan's face lights up."
    show morgan at center, traveling(1.5, 0.3, (640, 1040))
    "And she reaches out, grabbing hold of my wrist."
    show morgan talkative
    if morgan.male >= 66:
        morgan.say "Here you go, [hero.name]…"
        morgan.say "It's weird, but in a cool kind of way!"
    elif morgan.male >= 33:
        morgan.say "Sure you can, [hero.name]…"
        morgan.say "You only had to ask!"
    else:
        morgan.say "Oh, [hero.name]…"
        morgan.say "I thought you'd never ask!"
    show morgan normal
    "A moment later I find the palm of my hand pressed against Morgan's belly."
    "I'm staring down at it, almost like I can't believe this is really happening."
    "And straight away I feel a sense of joy rising inside of me."
    "I look up and straight into Morgan's eyes, and it's there too."
    "The exact same feeling is beaming out of her."
    show morgan talkative
    morgan.say "You see what I mean?"
    show morgan happy
    morgan.say "Pretty cool, huh?"
    show morgan normal
    "I'm nodding helplessly, almost unable to form the words to answer her."
    mike.say "Y...yeah, Morgan..."
    mike.say "It'd the coolest thing ever."
    mike.say "In fact, it's totally awesome!"
    return

label morgan_belly_listen_male:
    show morgan surprised at center, zoomAt(1.25, (640, 880))
    morgan.say "Ooh..."
    morgan.say "You little rascal!"
    morgan.say "Will you settle down in there already?"
    show morgan upset
    "Right now all it takes is the slightest moan or gasp from Morgan."
    show morgan at center, traveling(1.5, 0.3, (640, 1040))
    "The result of which will be me rushing to her side in a flood of concern."
    "As well as with the hospital on speed-dial!"
    mike.say "Morgan, are you okay?"
    mike.say "Is there something wrong with the baby?!?"
    show morgan normal
    "Morgan shakes her head at this."
    "As I guess she's already used to me being overly protective."
    show morgan talkative
    morgan.say "Everything's fine, [hero.name]…"
    morgan.say "It's just..."
    show morgan surprised
    morgan.say "Whoa!"
    show morgan talkative
    morgan.say "It's just weird, you know?"
    morgan.say "Having a tiny person moving around inside of you?"
    show morgan normal
    "All I can do is nod at this."
    "Because I can't begin to imagine what that must be like."
    mike.say "Is there anything I can do?"
    mike.say "You want me to listen to your bump?"
    show morgan stuned
    "Morgan looks at me with a quizzically raised eyebrow."
    show morgan surprised
    morgan.say "And that will achieve what, exactly?"
    show morgan normal
    mike.say "Erm..."
    mike.say "I dunno, Morgan."
    mike.say "But it's better than doing nothing, right?"
    show morgan annoyed
    if morgan.male >= 66:
        morgan.say "You really do talk crap sometimes..."
    elif morgan.male >= 33:
        morgan.say "If it'll make you feel better..."
    else:
        morgan.say "I have no idea if you're right..."
    morgan.say "But here you go!"
    show morgan normal at center, traveling(2.0, 1.0, (640, 980))
    "I nod eagerly as I lean in to listen."
    "Putting an ear against Morgan's belly, I try to blot everything else out."
    "And soon enough I can hear the baby moving around in there."
    "Obviously I can't make anything out other than movement in liquid."
    "It's like the sound of someone swimming underwater."
    "But the fact that's my kid in there makes it sound amazing and magical."
    mike.say "Wow..."
    mike.say "Morgan, I can hear them..."
    mike.say "And they're really going for it too!"
    if morgan.male >= 66:
        show morgan annoyed
        morgan.say "You think I can't feel that too?!?"
    elif morgan.male >= 33:
        show morgan happy
        morgan.say "That's great, [hero.name]!"
    else:
        show morgan happy
        morgan.say "Oh, I wish I could hear them too!"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
