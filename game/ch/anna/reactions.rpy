label anna_ice_cream_reaction_male:
    mike.say "I feel like I'm melting here - let's grab an ice cream!"
    anna.say "Oh yeah, that sounds good to me!"
    "At the ice cream stall, I buy myself a cone with a couple of different scoops."
    "Anna chooses a cone too, but she has hers filled with sweet-looking, pink ice cream."
    mike.say "Hey, Anna - is that supposed to match your hair?"
    anna.say "Oh, I see what you mean - I never thought of that!"
    "Anna giggles and then begins to lick at her cone."
    "And all I can do is stand there and watch as her tongue goes to work."
    "I don't know which looks sweeter and more appetising."
    "The ice cream cone or Anna herself!"
    return

label anna_study_with_intro_male:
    "Anna comes bustling into the room with an armful of books, huffing as she does so."
    "Without pausing to ask permission, she pushes my stuff roughly aside."
    "And then she proceeds to drop her own load right in front of me."
    mike.say "Wha...what the hell?!?"
    mike.say "Anna, what are you doing?"
    anna.say "Oh, [hero.name], you've forgotten, haven't you?"
    anna.say "You said that you'd help me study, remember?"
    "I can't help slapping myself on the forehead as I recall that she's right."
    "Anna's seemed preoccupied recently and more than a little bit stressed out."
    "When I quizzed her on what was up, she told me that she finding it hard to study."
    "And so, being the good guy that I am, I volunteered to help her out."
    "I mean, I know that she's studying biology at a pretty high level."
    "But that's just basically stuff about nature and the human body, right?"
    "And I've had a human body my whole life, which should make me and expert!"
    mike.say "Oh...yeah!"
    mike.say "Sorry, Anna!"
    mike.say "Sure, sure...let's get down to it."
    "Anna smiles at this, clearly grateful for the help that I'm offering."
    "But I can see in her eyes that she's less than convinced I know what I'm doing."
    "So it's time for me get this big brain of mine in gear."
    "I really need to impress her with my smarts!"
    anna.say "Okay, [hero.name]."
    anna.say "Let's start out slow and see how we go."
    anna.say "This stuff can get pretty complicated and confusing!"
    mike.say "Don't worry, Anna - I can handle it!"
    anna.say "If you say so..."
    anna.say "This module is all about genetics."
    anna.say "Specifically haemochromatosis, yeah?"
    anna.say "And it's instances in individuals of European, particularly Celtic descent?"
    "For a moment I can't help staring at Anna as if she's speaking a foreign language."
    "But then I realise that's not going to help me impress her one bit!"
    "So I rack my brain, thinking of something intelligent to say..."
    return

label anna_study_with_success_male:
    mike.say "Hmm..."
    mike.say "I never heard that term before, Anna!"
    "I can see Anna beginning to roll her eyes in frustration."
    "And so I start to think out loud in the hope of proving myself."
    mike.say "But 'hemo' reminds me of 'haemophilia'."
    mike.say "So it must have something to do with blood."
    mike.say "And 'mitosis' is something to do with cells, right?"
    "Anna's expression changes as I say all of this."
    "She goes from looking annoyed to intrigued."
    anna.say "Kind of, [hero.name]..."
    anna.say "It's a genetic condition that affects some people."
    anna.say "It makes them absorb too much iron..."
    "From there, Anna launches into an explanation of the condition."
    "I can't claim to understand everything that she tells me."
    "But I can see that the process of explaining seems to help her."
    "It's like by educating me, she's reinforcing her own knowledge."
    "Pretty soon Anna's talking confidently about the subject."
    "And I can see that her smile is genuine, her nods for real."
    anna.say "And that's just about all there is to say!"
    anna.say "Wow...I think I could give a lecture on this stuff now!"
    mike.say "Well, I could maybe answer a question about it in the pub quiz!"
    anna.say "Seriously though, [hero.name]..."
    anna.say "Thanks for doing this - it really helped me out!"
    mike.say "No worries, Anna."
    mike.say "I'm just glad that I could do you a favour!"
    "Anna gathers up her books and prepares to leave."
    "But not before she leans in close and plants a kiss on my cheek."
    "It's brief and unexpected, but it makes the whole thing worthwhile."
    return

label anna_study_with_failure_male:
    mike.say "Uh..."
    mike.say "What's that, Anna?"
    mike.say "Did you say ham and cheese toasties?"
    "Anna rolls her eyes and lets out a long sigh."
    "She shakes her head, already beginning to gather up her books."
    anna.say "I knew this wasn't a good idea, [hero.name]."
    anna.say "It was a sweet thing to offer to help."
    anna.say "But...well...you're just too dumb to be of any use!"
    mike.say "Aw, come on, Anna!"
    mike.say "That was just a rookie mistake - I promise!"
    "Anna's smile looks pained."
    "And she shakes her head a second time."
    anna.say "No, I mean it, [hero.name]."
    anna.say "This module is really important - I have to pass it."
    anna.say "Maybe you could help me out on another one?"
    anna.say "Like...maybe if there's one about lifting heavy objects or something?"
    "With that, Anna gives me another indulgent smile."
    "You know the kind - the ones that you give to a dull kid that's trying their best."
    "And then she walks out, leaving me feeling dumber than a box of rocks."
    return

label anna_ask_phone_male:
    mike.say "Hey, Anna..."
    mike.say "How about we swap numbers?"
    if hero.charm >= 20 - anna.love:
        show anna happy
        $ hero.smartphone_contacts.append("anna")
        anna.say "Oh...sure thing, [hero.name]!"
        anna.say "I'd love to let you have my number!"
        anna.say "But you'd better call me soon."
    else:
        show anna annoyed
        $ anna.love -= 1
        $ anna.sub -= 1
        anna.say "Oh...I don't know about that, [hero.name]."
        anna.say "That's kind of personal information!"
    return

label anna_ask_birthday_male:
    mike.say "Ah, Anna..."
    mike.say "Your birthday is when, exactly?"
    if hero.charm >= 40 - anna.love:
        show anna happy
        $ anna.flags.birthdayknown = True
        anna.say "Oops!"
        anna.say "Did I not tell you yet?"
        anna.say "I can be SO forgetful sometimes!"
        anna.say "It's Summer 26, okay?"
    else:
        show anna annoyed
        $ anna.sub -= 1
        $ anna.love -= 1
        anna.say "Oh, [hero.name]!"
        anna.say "I know I told you that already."
        anna.say "And I'm not telling you again!"
    return

label anna_offer_a_drink_male:
    mike.say "You ready for a drink, Anna?"
    mike.say "Because I'm just heading to the bar."
    "Almost the second the words are out of my mouth, Anna turns to face me."
    if anna.is_visibly_pregnant:
        show anna angry
        $ anna.love -= 10
        anna.say "Seriously, [hero.name]?"
        anna.say "Did you forget that you got me pregnant?!?"
        anna.say "I can't drink while I'm like this!"
        $ hero.cancel_activity()
        hide anna
    elif (hero.charm >= 60 - anna.love and anna.flags.drinks < 2) or date_girl == anna:
        show anna happy
        anna.say "Ooh..."
        anna.say "Yes please!"
        anna.say "I'll have my usual - if you remember what that is!"
        hide anna
        show drink anna
        if anna.love <= 25:
            $ anna.love += 1
        elif date_girl == anna and game.active_date:
            $ game.active_date.score += 5
        call expression anna.get_chat from _call_expression_209
        hide drink anna
        $ anna.set_flag("drinks", 1, "day", mod="+")
    else:
        show anna annoyed
        anna.say "Hey!"
        anna.say "I know where the bar is in here."
        anna.say "This better not be some joke about me being to short to see over it!"
        $ hero.cancel_activity()
        hide anna
    return

label anna_slap_ass_intro_male:
    "I keep on sneaking a peak at Anna's ass as we walk."
    "I even speed up to make her run as she tries to catch me."
    "The whole time her pert little buttocks are moving."
    "And they're like poetry in motion!"
    "Then something takes over, something I can't control."
    "And I can't keep myself from slapping Anna's ass!"
    return

label anna_slap_ass_happy_male:
    "Anna makes a little leap into the air."
    "And she lets out a yelp of alarm."
    anna.say "Hey!"
    anna.say "What the hell?!?"
    "She blushes as the reality dawns on her."
    anna.say "Hey, [hero.name]!"
    anna.say "No slapping my ass without asking first!"
    "Anna tries to make her tone sound disapproving."
    "But I can see the truth in the look on her face."
    "She loved every moment of it!"
    return

label anna_slap_ass_angry_male:
    "Anna makes a little leap into the air."
    "And she lets out a yelp of alarm."
    anna.say "Hey!"
    anna.say "What the hell?!?"
    "She blushes as the reality dawns on her."
    anna.say "Hey, [hero.name]!"
    anna.say "Don't you EVER do that again!"
    "Now I'm the one blushing and looking away in shame."
    "The look on Anna's face tells me that she's serious!"
    return

label anna_breakup_male:
    show anna
    "There's no good way to do this kind of thing."
    "So in the end, I just have to come out and say it."
    mike.say "Anna..."
    mike.say "We need to talk..."
    "The moment the words are out of my mouth, Anna's mood changes."
    "Before she was chatting and laughing like she didn't have care in the world."
    show anna cry
    "But now her face drops and I swear I can see her eyes getting bigger too!"
    anna.say "Oh..."
    anna.say "Oh no..."
    anna.say "I'm not dumb, [hero.name] - I know what that means!"
    "I can almost feel the situation slipping out of my control."
    "I need to make my point now, before Anna gets hysterical!"
    mike.say "I...I think we need to call it quits, Anna."
    mike.say "And if we do it now, then we can still stay friends - right?"
    "Just like that, Anna's mood changes for a second time."
    "Now she seems to be getting angry with me."
    "And at record speed too!"
    show anna angry
    anna.say "What the hell, [hero.name]?"
    anna.say "You're the one doing the dumping."
    anna.say "And you want to stay friends?"
    anna.say "Why don't you ask to keep fucking me on the side too?!?"
    "I have to admit, this last statement catches me off-guard."
    "Which is why I inevitably end up saying something really stupid."
    mike.say "Would you like to do that, Anna?"
    mike.say "Because we could..."
    "Anna explodes a second later."
    "She goes off like a petite nuclear weapon."
    anna.say "Of course not, [hero.name]!"
    anna.say "I was being sarcastic, you moron!"
    "Anna throws her arms up in the air."
    "And she sounds like she's actually grinding her teeth right now too."
    anna.say "Urgh..."
    anna.say "Why did I ever start dating guys again?"
    anna.say "Sure, the sex is fun - but they're all a bunch of shits!"
    anna.say "Like you, [hero.name] - you're the biggest shit of all!"
    return

label anna_go_steady_intro_male:
    mike.say "You and me, Anna..."
    mike.say "We're having some serious fun, right?"
    mike.say "So how about we make it official and go steady?"
    return

label anna_go_steady_yes_male:
    anna.say "Oh..."
    anna.say "I mean, sure, [hero.name]!"
    anna.say "That sounds like a great idea!"
    hide anna
    show anna kiss
    $ anna.flags.kiss += 1
    "Anna half leaps up and half pulls me down."
    "And she does so to plant a kiss on my lips."
    "Which I return without a second's pause."
    return

label anna_go_steady_no_male:
    anna.say "Oh..."
    anna.say "I don't know, [hero.name]..."
    anna.say "Can we wait a little longer?"
    return

label anna_pet_intro_male:
    "I can't resist the urge to pat Anna on the head."
    "She's just so cute and adorable, I have to do it."
    "But I don't know if she'll feel the same way..."
    return

label anna_pet_happy_male:
    anna.say "Ooh..."
    anna.say "I didn't know you were going to do that!"
    anna.say "But you can do it again, [hero.name]!"
    return

label anna_pet_annoyed_male:
    anna.say "Hey!"
    anna.say "What was that for?"
    anna.say "Since when was it okay to pet me like puppy?!?"
    return

label anna_massage_intro_male:
    mike.say "You seem a little wound-up, Anna."
    mike.say "You know, really tense?"
    mike.say "Like you could use a massage from yours truly!"
    return

label anna_massage_accept_male:
    anna.say "Hey, you're right, [hero.name]!"
    anna.say "I am kinda cranky today!"
    anna.say "And I'm always up for a massage from you..."
    return

label anna_massage_refuse_male:
    anna.say "Ooh..."
    anna.say "No way, [hero.name]!"
    anna.say "I'm WAY too cranky for that!"
    anna.say "I just want to be left alone, okay?"
    return

label anna_piercing_nipples_reaction_male:
    anna.say "Oh...I love it, [hero.name]!"
    anna.say "It looks so cute...and it feels REALLY sexy too!"
    anna.say "Thanks SO much for suggesting I pierce my nipples."
    return

label anna_piercing_navel_reaction_male:
    anna.say "I LOVE it, [hero.name]!"
    anna.say "But...I...I can't see it for my breasts!"
    anna.say "It looks cute though, yeah?"
    return

label anna_piercing_clit_reaction_male:
    anna.say "Oh wow...I love the way it feels!"
    anna.say "I can feel it whenever I'm walking around too..."
    anna.say "It's making me feel so hot!"
    return

label anna_piercing_head_reaction_male:
    anna.say "Ooh...I'm feeling a little tongue-tied right now."
    anna.say "But that's normal, right - when you just had it pierced?"
    anna.say "Whatever...I love this thing!"
    return

label anna_piercing_nose_reaction_male:
    anna.say "I LOVE IT, [hero.name]!"
    anna.say "It's perfect - just like I imagined it would be!"
    anna.say "Thanks for convincing me to get it."
    return

label anna_movie_disliked_reaction_male:
    anna.say "Eww...that movie was a massive stinker - I hated it!"
    return

label anna_movie_indifferent_reaction_male:
    anna.say "Meh...I was so bored I almost fell asleep in there!"
    return

label anna_movie_liked_reaction_male:
    anna.say "Oh wow - that movie was SO great...we HAVE to see it again!"
    return

label anna_belly_kiss_male:
    show anna b evil at center, zoomAt(1.25, (640, 880))
    anna.say "Hey, [hero.name]…"
    anna.say "Caught you staring at my belly!"
    show anna b normal
    "I feel my cheeks flushing with colour as Anna catches me in the act."
    "And it's not like I can really hide the fact, as her belly is huge!"
    mike.say "Yeah, Anna..."
    mike.say "I just can't get enough of that thing!"
    mike.say "Sometimes I just want to cover it in kisses..."
    mike.say "Which is crazy..."
    mike.say "I mean, it is crazy, right?"
    "With any other girl I'd have been waiting with baited breath for an answer."
    "Because this is one of those things that you can never predict with a pregnant woman."
    "Sometimes they want all the attention and affection in the world on their bump."
    "And sometimes they want to keep themselves from being the centre of attention."
    "But I think that I know what kind of a girl Anna is."
    "And my assumption is confirmed as she now goes all starry-eyed."
    show anna b surprised
    anna.say "You do?"
    show anna b talkative
    anna.say "Then why aren't you kissing it?"
    show anna b happy
    anna.say "In fact, why aren't you kissing it right now?!?"
    show anna b evil at center, traveling(2.0, 0.5, (640, 980))
    "Anna practically barges her belly into me as she says all of this."
    "Which leaves me no choice but to put my money where my mouth is."
    "Or to be more accurate, put my lips where her bump is."
    "And once I start kissing it, I find that it's hard to stop!"
    "All the time Anna's looking down at me, approval written all over her face."
    return

label anna_belly_caress_male:
    show anna b evil at center, zoomAt(1.25, (640, 880))
    "I have to admit that I was a little worried when Anna started to show."
    "My worry was that being pregnant would change her body in a dramatic way."
    "Even that it'd make me find her less attractive."
    "But if anything, the amount I want her has grown at the same rate as her belly!"
    "I can't keep my eyes off the thing."
    "And that's probably because I can't help wanting to touch it."
    "Though I'm afraid Anna might think that's weird, you know?"
    "So I just keep trying to sneak a look now and then."
    "Hoping that..."
    show anna b evil
    anna.say "Hey..."
    anna.say "Are you staring at my belly?!?"
    show anna b normal
    "Oh shit..."
    "Looks like I got caught in the act."
    "So I'd best come clean and face the consequences."
    mike.say "Ah..."
    mike.say "Yeah, Anna..."
    mike.say "I kind of can't help myself!"
    show anna b happy at center, traveling(1.75, 1.0, (640, 880))
    "Much to my surprise, Anna shakes her head while she beams at me."
    "Then she shoves her belly right up against me, chuckling away merrily."
    show anna b evil
    anna.say "Well here you go..."
    anna.say "Help yourself!"
    show anna b happy
    "Already reaching out to touch it, I still feel the need to ask."
    mike.say "Are you sure?"
    anna.say "Of course I am, [hero.name]."
    anna.say "You're as much responsible for it as I am!"
    "I nod as I put my hands on Anna's belly."
    "And when I feel the first movement, I look up."
    "That means I look straight into her eyes."
    "The exchange between us is totally silent."
    "But it makes me feel a love for her that's so strong."
    "One that I can't remember feeling before this moment."
    return

label anna_belly_listen_male:
    show anna b surprised at center, zoomAt(1.25, (640, 880))
    anna.say "[hero.name]..."
    anna.say "[hero.name]..."
    show anna b normal
    "At the sound of Anna's shouting my name, I turn around."
    mike.say "Yeah, Anna..."
    mike.say "What is it?"
    show anna normal
    "But before I can say another word, she has hold of me."
    "And then she's pulling my head downwards."
    show anna b talkative
    anna.say "You have to check this out..."
    anna.say "Trust me, you're gonna love it!"
    show anna b normal
    "Anna's not exactly hurting me right now."
    "And she's stronger than she looks."
    "So I decide to play along for the moment."
    show anna normal at center, traveling(2.0, 0.5, (640, 980))
    "Which is how I find my ear jammed against the curve of her belly."
    "I'm about to say something, when I feel the baby move against the side of my head."
    "But I also hear something at the same time, and that's what stops me in my tracks."
    "It's weird, like the vague sound of something moving, deep underwater."
    "Yet there's no mistaking the fact that it's source is the baby's movements."
    "Looking up at Anna, I must look as amazed and excited as she does."
    mike.say "Was that..."
    show anna happy
    anna.say "Yeah!"
    mike.say "You mean that..."
    anna.say "Yeah!"
    mike.say "I just heard the baby?!?"
    anna.say "Yeah!"
    "There's nothing else that I can hope to do in that moment."
    "So I leap up and throw my arms around Anna, pulling her close."
    "She returns the gesture, making allowances for her belly."
    "And we share a deep, meaningful moment that we'll always remember."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
