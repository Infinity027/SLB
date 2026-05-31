label reona_ice_cream_reaction_male:
    "Wow..."
    "Reona looks SO good in her swimsuit!"
    "I can't tear my eyes away from her, no matter how hard I try."
    "In fact, I think my tongue is actually hanging out!"
    reona.say "You look like you could use an ice-cream, [hero.name]!"
    mike.say "Huh?"
    mike.say "Why's that, Reona?"
    reona.say "You're panting like a dog!"
    reona.say "You must be way too hot right now."
    mike.say "Somebody's too hot, that's for sure!"
    reona.say "What was that?"
    mike.say "Nothing..."
    mike.say "Now, about that ice-cream..."
    "Thankful for the distraction, I hurry towards the ice-cream stand."
    "Reona claps her hands in glee and anticipation as I order for us both."
    "And she instantly starts to lick her ice-cream as soon as I hand it to her."
    reona.say "Mmm..."
    reona.say "So good!"
    "I nod, only vaguely tasting my own ice-cream."
    "Because I'm back where I began."
    "Staring at Reona as she licks and slurps away."
    return

label reona_ask_phone_male:
    mike.say "I don't want to have to call Jack to get a message to you, Reona."
    "I try to emphasize how much of a pain that would be."
    "For both myself and Reona alike."
    mike.say "So do you think that I could get your number?"
    "I add a smile that I hope will seal the deal, just for good measure."
    if hero.charm >= 20 - reona.love:
        $ hero.smartphone_contacts.append("reona")
        "Reona smiles and nods, already getting her phone out."
        reona.say "Sure thing, [hero.name]."
        reona.say "I should've given it to you already."
        reona.say "Here you go..."
        reona.say "Last thing we want is Jack knowing what we're talking about, yeah?"
    else:
        $ reona.love -= 1
        $ reona.sub -= 1
        "Reona wrinkles her nose up, like the idea stinks."
        reona.say "I don't think so, [hero.name]."
        reona.say "I'm very careful about giving out my number."
        reona.say "You never know when someone's really a weirdo."
        reona.say "And you could still be one of those!"
    return

label reona_ask_birthday_male:
    mike.say "I'm just checking my calendar and I realised..."
    mike.say "You never told me the date of your birthday, Reona!"
    mike.say "I'd hate to forget it and piss you off."
    "Reona looks a little surprised at the revelation."
    "But then a smile spreads across her face."
    if hero.charm >= 40 - reona.love:
        $ reona.flags.birthdayknown = True
        reona.say "I didn't?"
        reona.say "Well, we can soon change that!"
        "Reona surprises me by pulling out her phone."
        "Does she actually need that to remember her own birthday?"
        reona.say "It's Fall 10."
    else:
        $ reona.sub -= 1
        $ reona.love -= 1
        reona.say "Yeah, I know."
        reona.say "Thing is, that's because I don't want you to know."
        reona.say "I'm really careful about who I tell that kind of stuff too."
        "Reona shrugs and shakes her head."
        reona.say "You're just not in my circle of trust yet!"
    return

label reona_offer_a_drink_male:
    mike.say "I'm on the way to the bar, Reona."
    mike.say "You want me to grab you one while I'm there?"
    mike.say "It's no trouble!"
    if reona.is_visibly_pregnant:
        "Reona looks like she's about to nod."
        "But then she gazes down at her swollen belly."
        reona.say "Oh yeah, I'm pregnant, aren't I?"
        $ reona.love -= 10
        reona.say "Dammit, I could have used a cold one!"
        $ hero.cancel_activity()
        hide reona
    elif (hero.charm >= 60 - reona.love and reona.flags.drinks < 2) or date_girl == reona:
        "Reona nods happily."
        reona.say "You read my mind, [hero.name]!"
        reona.say "Make mine a cold one."
        reona.say "And be quick about it!"
        "Reona even adds a wink to sweeten the deal."
        hide reona
        show drink reona
        if reona.love <= 25:
            $ reona.love += 1
        elif date_girl == reona and game.active_date:
            $ game.active_date.score += 5
        call expression reona.get_chat from _call_expression_481
        hide drink reona
        $ reona.set_flag("drinks", 1, "day", mod="+")
    else:
        reona.say "Sorry, I don't feel like drinking."
        $ hero.cancel_activity()
    return

label reona_slap_ass_intro_male:
    "Reona keeps on walking past me, drawing my gaze after her."
    "And I swear that she's doing it on purpose, just to bait me."
    "I mean, does she always wiggle her ass like that?"
    "Surely not, it kind of looks like it defies the laws of physics!"
    "In fact, it's almost hypnotic."
    "I feel like it's taking me over."
    "Making me stretch out my hand..."
    return

label reona_slap_ass_happy_male:
    reona.say "OUCH!"
    reona.say "Hey!"
    reona.say "Did you..."
    reona.say "Did you just slap me on the ass?!?"
    mike.say "Erm, yeah..."
    mike.say "I guess I did!"
    "Reona frowns and shakes her head."
    "But a moment later her face breaks into a smile."
    reona.say "Well..."
    reona.say "Give me a little notice next time, okay?"
    reona.say "Or at least wait until we're alone!"
    "I nod, returning the smile."
    "Partly because I managed to get away with it."
    "And partly because I now know Reona liked it."
    return

label reona_slap_ass_angry_male:
    reona.say "OUCH!"
    reona.say "Hey!"
    reona.say "Did you..."
    reona.say "Did you just slap me on the ass?!?"
    mike.say "Erm, yeah..."
    mike.say "I guess I did!"
    "Reona frowns and shakes her head."
    reona.say "It's not bad enough I gotta put up with your staring at it."
    reona.say "Now you're putting your hands on it too?"
    "I find myself looking at the ground."
    "Almost too ashamed to meet her eye."
    mike.say "Sorry, Reona..."
    mike.say "I couldn't help myself."
    reona.say "Well you'd better try harder next time."
    reona.say "Or you'll be getting a slap in return!"
    return

label reona_breakup_male:
    "I take a deep breath, preparing myself for what lies ahead."
    "I wish there was some way out of this, some other answer."
    "But I've already been over it a thousand times in my head."
    "And this is the only solution that makes any sense."
    mike.say "Reona..."
    mike.say "I have something to tell you."
    mike.say "And I don't think you're going to like it!"
    "Reona looks at me in surprise."
    "But I can see the expression on her face slowly changing."
    "So I guess she's sensed the mood I'm in and knows I mean it."
    reona.say "What is it, [hero.name]?"
    mike.say "It's us, Reona..."
    mike.say "I think we should stop seeing each other."
    "Reona now looks stunned."
    "She shakes her head in disbelief."
    reona.say "Wait a second..."
    reona.say "That's not how it works!"
    reona.say "I dump guys, they don't dump me!"
    mike.say "Well that's what's happening, Reona."
    mike.say "I suggest you find a way to deal with it."
    "Reona narrows her eyes, and I can sense anger welling up inside her."
    "But much to my surprise, she simply turns her back and walks away."
    "I was genuinely expecting her to go ballistic at me."
    "So that leaves me standing in stunned silence."
    return

label reona_go_steady_intro_male:
    "I can feel the nerves making my guts churn as I get ready to ask the question."
    "But this thing's gotten so bad that it'd almost be worse not to go through with it."
    "I'd be stuck in this awful state of limbo, never knowing what the answer would have been."
    mike.say "Ah, Reona..."
    mike.say "There's something I wanted to ask you."
    reona.say "Huh?"
    reona.say "What's that?"
    mike.say "Well, we get on pretty well, right?"
    reona.say "Right."
    mike.say "So how about we make it official?"
    mike.say "How about we go steady?"
    return

label reona_go_steady_yes_male:
    reona.say "You know what, [hero.name]..."
    reona.say "That's a pretty good idea!"
    reona.say "Yeah, sure thing we should go steady!"
    "I feel a flood of relief surging through me."
    "And for the first time in what feels like forever, I can breathe freely!"
    mike.say "That's great, reona!"
    mike.say "Really great!"
    return

label reona_go_steady_no_male:
    reona.say "Nah."
    "Reona shakes her head, like it's nothing."
    "I wait for a few moments, looking at her expectantly."
    "But it seems that's all she has to say on the matter."
    mike.say "So..."
    mike.say "Is that no, as in not yet?"
    mike.say "Or no, as in we need to talk it through?"
    reona.say "It's no as in no."
    reona.say "What more do you want me to say?!?"
    return

label reona_pet_intro_male:
    "Reona's one of those girls that you think is a real handful when you meet her."
    "But as you really get to know her, you realise that's just the impression she puts out."
    "In reality, she can be sweet and adorable in a way that catches you off-guard."
    "And it kind of makes me want to pet her like a cat too!"
    "Don't ask my why, I just can't seem to help myself..."
    reona.say "HEY!"
    reona.say "What was that?!?"
    reona.say "Did you just pat me on the head?"
    mike.say "Erm..."
    mike.say "Yeah, Reona!"
    mike.say "I kinda did..."
    return

label reona_pet_happy_male:
    reona.say "Oh..."
    reona.say "Okay, [hero.name]..."
    reona.say "So long as it was you!"
    "Reona smiles and gives me a knowing wink."
    reona.say "Anyone else, and I'd have smacked them!"
    reona.say "Smacked them up the side of the head!"
    return

label reona_pet_annoyed:
    reona.say "Well how'd you like me to slap you, huh?"
    reona.say "Slap you real hard up the side of yours?!?"
    "I instinctively leap backwards as Reona threatens me."
    mike.say "WHOA!"
    mike.say "Settle down, Reona!"
    mike.say "It was just a show of affection!"
    reona.say "Yeah?"
    reona.say "Well what I said was just a statement of fact!"
    return

label reona_massage_intro:
    reona.say "Ouch, ouch, ouch!"
    reona.say "Dammit!"
    reona.say "That really hurts!"
    mike.say "Ooh..."
    mike.say "I felt that too, Reona!"
    mike.say "You pulled a muscle?"
    reona.say "Yeah, [hero.name]..."
    reona.say "And I'm in SOOO much pain!"
    mike.say "You want me to take a look at it?"
    mike.say "I'm told I give a pretty good massage!"
    return

label reona_massage_accept:
    "Reona nods and hurries over to me."
    "And she even adds a pretty cute pout too!"
    reona.say "Oh yeah, [hero.name]..."
    reona.say "If you can make it better."
    reona.say "I'm up for giving anything a try!"
    return

label reona_massage_refuse:
    "Reona shakes her head and backs off."
    "Even if the motions seems to cause her even more pain."
    reona.say "Oh no, [hero.name]!"
    reona.say "I don't want to make it worse."
    reona.say "I really think I need to see a doctor or something."
    return

label reona_piercing_nipples_reaction:
    reona.say "Hey, [hero.name]..."
    reona.say "Guess what I got!"
    "I glance up just in time for Reona to thrust her chest into my face."
    "And based on the small amount of clothing she wears, it's plain to see!"
    mike.say "You had your nipples pierced?"
    reona.say "You bet I did!"
    reona.say "It looks super hot!"
    reona.say "And it feels even better..."
    return

label reona_piercing_navel_reaction:
    reona.say "Hey, [hero.name]..."
    reona.say "Guess what I got!"
    "I glance up just in time for Reona to thrust her belly into my face."
    "And based on the small amount of clothing she wears, it's plain to see!"
    mike.say "You had your navel pierced?"
    reona.say "You bet I did!"
    reona.say "It looks super hot!"
    reona.say "And it feels even better..."
    return

label reona_piercing_clit_reaction:
    reona.say "Hey, [hero.name]..."
    reona.say "Guess what I got!"
    "I glance up just in time for Reona to thrust her groin into my face."
    "Even with the revealing clothes that she wears, I still can't see it."
    "But I do know Reona well enough to be able to guess."
    mike.say "You had your clit pierced?"
    reona.say "You bet I did!"
    reona.say "It looks super hot!"
    reona.say "And it feels even better..."
    return

label reona_piercing_head_reaction:
    reona.say "Hey, [hero.name]..."
    reona.say "Guess what I got!"
    "I glance up just in time for Reona to thrust her tongue into my face."
    "And there's nothing to stop me seeing exactly what she's talking about."
    mike.say "You had your tongue pierced?"
    reona.say "You bet I did!"
    reona.say "It looks super hot!"
    reona.say "And it feels even better..."
    return

label reona_piercing_nose_reaction:
    reona.say "Hey, [hero.name]..."
    reona.say "Guess what I got!"
    "I glance up just in time for Reona to thrust her nose into my face."
    "And there's nothing to stop me seeing exactly what she's talking about."
    mike.say "You had your nose pierced?"
    reona.say "You bet I did!"
    reona.say "It looks super hot!"
    reona.say "And it feels even better..."
    return

label reona_belly_kiss_male:
    show reona normal at center, zoomAt(1.25, (640, 880))
    pause 0.1
    show reona at center, traveling(1.5, 1.0, (640, 1040))
    "I'm already reaching out with my hands to touch Reona's belly."
    "And now that she's used to me touching it, she reacts instinctively."
    show reona normal
    "Reona lifts her top, allowing me to see the naked curve of her belly."
    show reona at center, traveling(2.0, 1.0, (640, 980))
    "But instead of just touching it, I lean in closer still."
    "And then I proceed to put my lips against it, kissing her skin."
    show reona surprised
    reona.say "Oh..."
    reona.say "Oooh..."
    "Reona flinches a little at first, as she's taken by surprise."
    "But there's no sign of her pulling away from me."
    "Which I choose to take as a good sign, even permission to go further."
    "Moving here and there, I plant random kisses on Reona's belly."
    "There's no clear plan to what I'm doing and I don't know where it's going."
    "Just that I'm enjoying the act and Reona seems to be liking it too."
    show reona happy
    "I can hear her cooing and letting out pleasant little sighs."
    "Even the occasional word of encouragement that reaches my ears."
    show reona flirt
    reona.say "[hero.name]…"
    reona.say "That feels so nice!"
    "Rather than stopping to reply, I choose to keep on going."
    "Reasoning that I don't need to bask in the praise I'm getting."
    "As it's more than enough to know that she likes it."
    "And I'm getting a lot out of this too, so I don't want to stop."
    "Though by the time I've covered every inch, I'm feeling a little tired."
    "So it feels like the right time to bring the thing to an end."
    return

label reona_belly_caress_male:
    show reona normal at center, zoomAt(1.25, (640, 880))
    "It was bad enough back when Reona wasn't pregnant."
    "Because I couldn't keep my hands off her even then."
    "But now that she's really starting to show, it's gotten ten times worse."
    "I can't keep my eyes off of her, as she's really starting to glow."
    "And she's not the kind of girl that would fail to notice a thing like that."
    show reona talkative
    reona.say "[hero.name]…"
    reona.say "I was just wondering..."
    show reona devious
    mike.say "Erm..."
    mike.say "About what, Reona?"
    "There's nothing I can do to hide the trepidation in my voice."
    "Because I'm worried that Reona's about to call me out on my staring."
    show reona flirt
    reona.say "About when you're going to ask me, of course!"
    reona.say "When you're going to pluck up the courage to ask to touch my belly!"
    show reona devious
    "The knowing smile on Reona's face comes as a sudden relief to me."
    show reona at center, traveling(1.5, 0.3, (640, 1040))
    "That and the way she thrusts her belly towards me at the same time."
    "Because there's no way she'd be smiling like that if she disapproved."
    mike.say "You mean..."
    mike.say "You're okay with me..."
    show reona interested
    "Reona answers the half-formed questions by pushing herself against me."
    "And the fact I instinctively raise my hands as she does so seals the deal."
    "As it means that her belly is pressed against my palms a moment later."
    show reona happy
    "Reona's smile begins to truly beam as I move my hands over it too."
    reona.say "So, [hero.name]…"
    reona.say "How does it feel?"
    "I shake my head, almost unable to put the feeling into words."
    mike.say "Amazing, Reona..."
    mike.say "Totally amazing!"
    return

label reona_belly_listen_male:
    show reona normal at center, zoomAt(1.25, (640, 880))
    "When Reona thrusts her belly towards me, I kind of go into autopilot."
    "Because I'm used to either stroking it or laying kisses down when she does so."
    show reona interested at center, traveling(1.5, 0.3, (640, 1040))
    "But this time she shakes her head as I reach out for it."
    "Which of course means that I stop in my tracks, wondering what's up."
    mike.say "What's the matter, Reona?"
    mike.say "Did you change your mind?"
    "Reona shakes her head for a second time."
    show reona talkative
    reona.say "Oh no, [hero.name]…"
    reona.say "I just want you to do something a little different this time."
    show reona devious
    "Intrigued to find out what this could be, I nod eagerly."
    mike.say "Sure thing, Reona."
    mike.say "What did you have in mind?"
    show reona shy
    reona.say "I wondered if you'd listen to the baby?"
    reona.say "Just put your ear to my belly and tell me what you hear."
    show reona devious
    "I look at Reona for a moment, kind of thrown by her request."
    mike.say "Of course I will."
    mike.say "But I'm not sure what I'll be able to hear."
    mike.say "I mean, they use one of those ultra-sound thingies to do it in the hospital."
    mike.say "And I'll just be using my plain old human ear!"
    show reona embarrassed blush
    "Reona flushes a little, looking embarrassed."
    show reona talkative
    reona.say "I know that!"
    reona.say "I just want to know what you can hear - even if it's just impressions."
    reona.say "Somehow knowing that you can hear the baby..."
    reona.say "It'd just make me feel...kind of happy."
    show reona interested
    "I can tell that this is really important to Reona."
    "And do I decide that it's time to drop any hesitation on my part."
    "Because if it's going to make her happy, then why wouldn't I do it?"
    show reona at center, traveling(2.0, 1.0, (640, 980))
    "So pressing an ear to her belly, I do the best I can to listen."
    "And it doesn't take long for my efforts to be rewarded."
    mike.say "Whoa..."
    mike.say "I can hear them, Reona!"
    mike.say "It's like the sounds that you hear underwater."
    mike.say "Weird sounds, but really chill, you know?"
    show reona happy
    "I look up to see Reona nodding happily."
    "And from the smile on her face, I know that I've done the right thing."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
