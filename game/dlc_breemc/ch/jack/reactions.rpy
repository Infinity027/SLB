label jack_ice_cream_reaction_female:
    if game.week_day % 2 == 0:
        "It's a pretty hot day, and I'm feeling it more than usual."
        "I need a way to cool down, and I see one right on cue."
        bree.say "Hey, Jack..."
        bree.say "Let's go grab an ice cream!"
        jack.say "Wow, you read my mind!"
        "Pretty soon Jack and I are walking away from the ice cream stand."
        "Each of us is holding our choice of frozen treat in our hand."
        "It's about now that I notice Jack watching me eat mine."
        bree.say "Ah, Jack - what's up?"
        jack.say "Oh, nothing, [hero.name]!"
        jack.say "I was...just thinking your ice cream looked good, that's all!"
        "I nod and return to eating my ice cream, knowing full well Jack was watching me lick it."
        "Which I guess is fair enough, as I was doing the same thing to him too."
        "And imagining what else I could get him to do with that tongue!"
    else:
        jack.say "[hero.name]!"
        bree.say "What's up, Jack?"
        jack.say "We should get ice-cream!"
        bree.say "Yeah, we totally should!"
        "Jack and I hurry over to the ice-cream stand."
        "And we don't waste any time ordering what we want."
        "The moment I'm handed my ice-cream, I start licking at it."
        "But then I notice that Jack's not eating his own."
        "Instead he's staring at me as I get to work on mine."
        bree.say "Erm..."
        bree.say "Can I help you, Jack?"
        bree.say "Is there something wrong with your ice-cream?"
        "Jack stares for a moment longer, then shakes his head."
        "And he seems to snap back to reality as he does so."
        jack.say "N...no, [hero.name]..."
        jack.say "It's just that you look so good...so tasty!"
        jack.say "I...I mean your ICE-CREAM looks so good and tasty!"
        "I burst into laughter at Jack's unconscious admission."
        "He blushes a little, which makes me feel bad."
        "So I hurry to reassure him."
        bree.say "It's okay, Jack!"
        bree.say "I kinda like that you think I'm as tasty as ice-cream!"
    return

label jack_ask_phone_female:
    "I feel like Jack and I have been getting on pretty well."
    "And now would be a good time to take things to the next stage."
    "So I ask what I hope sounds like an innocent question."
    bree.say "Erm, Jack..."
    bree.say "Do you think I could get your number?"
    jack.say "Huh?"
    jack.say "Do you mean my phone number?"
    bree.say "No, I mean the size shoe you take!"
    bree.say "Of course I mean your phone number, dummy!"
    if hero.charm >= 20 - jack.love:
        $ hero.smartphone_contacts.append("jack")
        jack.say "Of course you can have my number, [hero.name]!"
        jack.say "I was waiting for you to ask!"
        "Jack hurriedly reels off his number."
        jack.say "Now call me - I want to check you got it right!"
        bree.say "Okay, Jack, okay..."
        "Well, I guess I should be pleased with his enthusiasm, right?"
    else:
        $ jack.love -= 1
        $ jack.sub -= 1
        jack.say "Ah...I don't think so, [hero.name]."
        bree.say "Wh...why not?"
        jack.say "I dunno..."
        jack.say "I just don't think we're at that point in our relationship yet."
        bree.say "Oh...okay, Jack."
        "Well, that told me!"
    return

label jack_ask_birthday_female:
    if game.week_day % 2 == 0:
        "It occurs to me that I have no idea when Jack's birthday is."
        "So I just come out and ask, thinking nothing of it."
        bree.say "Jack..."
        bree.say "When is your birthday?"
        "At first, Jack looks a little surprised by the question."
        "But then he comes out with an answer for me."
    else:
        bree.say "Jack..."
        bree.say "When's your birthday?"
        bree.say "I just realised that I have no idea of the date!"
    if hero.charm >= 40 - jack.love:
        $ jack.flags.birthdayknown = True
        if game.week_day % 2 == 0:
            jack.say "Oh, sure, [hero.name]!"
            jack.say "It's Summer 12."
            "I nod and file the date away for future reference."
            bree.say "Thanks, Jack."
            bree.say "Now I don't have an excuse not to remember it!"
        else:
            jack.say "Oh..."
            jack.say "It's Summer 12."
            jack.say "Thanks for showing an interest."
    else:
        if game.week_day % 2 == 0:
            jack.say "I'd really rather not say, [hero.name]!"
            "Now it's my turn to look surprised."
            bree.say "Seriously, Jack - you're not going to tell me?"
            jack.say "It's sensitive personal information, [hero.name]."
            jack.say "And I don't think we're at that point in our relationship yet."
            bree.say "Oh...okay, Jack."
            "Well, that told me!"
        else:
            jack.say "That's kind of a personal question, don't you think?"
            jack.say "If I wanted you to know, I'd have told you already."
            jack.say "Don't be so nosy, [hero.name]!"
        $ jack.sub -= 1
        $ jack.love -= 1
    return

label jack_offer_a_drink_female:
    if bree.is_visibly_pregnant:
        bree.say "I'm on the soft drinks tonight, Jack."
        bree.say "But I'm going to buy you a drink, okay?"
    else:
        bree.say "I'm going to grab a beer, Jack."
        bree.say "And I'm going to buy you a drink too, okay?"

    if (hero.charm >= 60 - jack.love and jack.flags.drinks < 2) or date_girl == jack:
        "Jack smiles and nods at the offer."
        jack.say "Oh yeah!"
        jack.say "Well spotted, [hero.name]."
        jack.say "I'll have the same again."
        jack.say "And thanks, I owe you one."
        show drink jack
        if jack.love <= 25:
            $ jack.love += 1
        elif date_girl == jack and game.active_date:
            $ game.active_date.score += 5
        call expression jack.get_chat from _call_expression_392
        hide drink jack
        $ jack.set_flag("drinks", 1, "day", mod="+")
        if hero.morality >= -25:
            $ hero.morality -= 1
    else:
        jack.say "Whoa..."
        jack.say "Slow down there, [hero.name]!"
        jack.say "It's not a drinking competition, you know?"
        jack.say "You really shouldn't be encouraging me to drink too much either."
        $ hero.cancel_activity()
        hide jack
    return

label jack_slap_ass_intro_female:
    if game.week_day % 2 == 0:
        "I know it's kind of a 'guy thing', but girls love asses too."
        "It's just that we don't go on about it in public as much as guys do!"
        "And it's not just skinny asses like boiled eggs in a handkerchief either."
        "Take Jack's ass for example - it's far more substantial than that."
        "But the sight of it moving inside of his jeans..."
        "Phew...it just does something to me!"
        "In fact, I can feel it doing something to me right now!"
        "I try as best I can to fight the urge."
        "But it's just too strong to resist!"
        "Before I know what I'm doing, I wind up and swing..."
        "Then there's an audible crack as my hand hits Jack's ass!"
    else:

        "Jack's wearing those pants again, the ones that make his ass look SO good!"
        "I can't keep my eyes off his buttocks, no matter how hard I try."
        "And the first chance I get, my arm swings back as far as it'll go."
        "Then it swings back in the opposite direction, until my hand makes contact."
        "There's an audible slapping sound as my palm hits Jack's butt-cheek."

    return

label jack_slap_ass_happy_female:
    if game.week_day % 2 == 0:
        jack.say "OW..."
        jack.say "Hey, [hero.name]!"
        jack.say "Did you..."
        jack.say "Did you actually just slap my ass?!?"
        bree.say "Erm...yeah, I guess so..."
        bree.say "I just couldn't help myself!"
        "I shrug and smile, hoping that Jack will laugh it off."
        "But instead he flushes red and looks embarrassed."
        jack.say "Th...thanks, [hero.name]!"
        jack.say "I have been trying to work it into shape."
        jack.say "So I guess I should be happy you noticed!"
        "I give Jack another smile, amused at his bashfulness."
        "I never knew he worked so hard to look good for me!"
    else:
        "And he makes a high-pitched, almost feminine yelping sound."
        jack.say "[hero.name]..."
        jack.say "Did you just..."
        jack.say "Did you slap my ass?!?"
        "I can feel my cheeks flushing red as Jack asks the question."
        "Which is a pretty good admission of guilt on my part."
        bree.say "Sorry, Jack..."
        bree.say "I couldn't help myself!"
        "To my great relief, I see that Jack's blushing too."
        jack.say "I...I guess I should be flattered, [hero.name]."
        jack.say "Nobody ever slapped my ass before!"
        jack.say "I kind of thought that it wasn't...well, slappable!"
    return

label jack_slap_ass_angry_female:
    if game.week_day % 2 == 0:
        jack.say "OW..."
        jack.say "Hey, [hero.name]!"
        jack.say "Did you..."
        jack.say "Did you actually just slap my ass?!?"
        bree.say "Erm...yeah, I guess so..."
        bree.say "I just couldn't help myself!"
        "I shrug and smile, hoping that Jack will laugh it off."
        "But instead he frowns and shakes his head at me."
        jack.say "That is NOT cool, [hero.name]."
        jack.say "I might be a straight guy."
        jack.say "But I am not a sex-object!"
        jack.say "Please don't do that again."
        "I nod and look at my feet, dying of embarrassment."
        "That sure put me in my place!"
    else:
        "And he makes a high-pitched, almost feminine yelping sound."
        jack.say "[hero.name]..."
        jack.say "Did you just..."
        jack.say "Did you slap my ass?!?"
        "I can feel my cheeks flushing red as Jack asks the question."
        "Which is a pretty good admission of guilt on my part."
        bree.say "Sorry, Jack..."
        bree.say "I couldn't help myself!"
        "Jack frowns and shakes his head."
        "Which only serves to make me feel more ashamed of myself."
        jack.say "[hero.name], do you even know how wrong that is?"
        jack.say "If I slapped your ass, I'd be dead meat!"
        jack.say "So it's totally not okay for you to do that to me!"
    return

label jack_breakup_female:
    if game.week_day % 2 == 0:
        "There's no easy way to do this and no way that's not going to be painful either."
        "But Jack's such a nice guy that I owe it to him to be straight up, not to string him along."
        "So I choose my moment and take a deep breath, already knowing this is going to suck..."
        bree.say "Jack..."
        bree.say "We need to talk..."
        jack.say "Huh?"
        jack.say "What about, [hero.name]?"
        "Oh shit, he's not getting it."
        "Either that or he's pretending not to get it."
        bree.say "Us, Jack."
        bree.say "We need to talk about us!"
        "I can see the change come over Jack's face as I say this."
        "And now I know that he wasn't pretending - he really didn't see this coming!"
        jack.say "Oh..."
        jack.say "I think I get it now!"
        jack.say "You're dumping me, aren't you?"
        bree.say "No, Jack - I'm not dumping you!"
        bree.say "I just...think we should maybe see other people, yeah?"
        jack.say "Yeah...that's just another way of saying I'm dumped, [hero.name]!"
        bree.say "I'm sorry, Jack..."
        jack.say "Not as sorry as I am!"
        bree.say "Don't be like that, Jack."
        bree.say "We can still be friends - like we were before!"
        jack.say "I don't think I want to be just your friend, [hero.name]!"
        "With that, Jack turns and starts to walk away."
        "I hold up a hand and begin to say something."
        "But then I stop, realising that I don't know what else to say."
        "So I guess that means that it's over."
    else:
        bree.say "Urgh..."
        bree.say "There's no easy way to say this, Jack..."
        bree.say "So I'm just going to come out and say it."
        "Jack looks at me, dread on his face and fear in his eyes."
        "He must have sensed what's coming from the tone of my voice."
        jack.say "This is going to be bad, isn't it?"
        bree.say "Yeah, Jack..."
        bree.say "It's us, Jack."
        bree.say "I don't think this thing is working out."
        bree.say "I think we should break up."
        "I don't think I've ever seen someone look so devastated."
        "In that moment, Jack looks just like a kicked puppy."
        "And I feel like the person that planted a foot in his ass."
        jack.say "Y...you do, [hero.name]?"
        jack.say "Oh...okay..."
        jack.say "I guess I should be grateful we dated at all..."
    return

label jack_go_steady_intro_female:
    if game.week_day % 2 == 0:
        "I feel like Jack and I have really clicked every time I've seen him."
        "And the dates we've been on together have all been really fun."
        "I find myself making any excuse to call him up on the phone too."
        "So it seems pretty obvious to me there's a real spark between us."
        "And I think we should take things to the next level."
        "So I pop the question the first chance I get."
        bree.say "Jack..."
        bree.say "We're having a good time together, right?"
        jack.say "A good time, [hero.name]?"
        jack.say "It's been like the best times ever!"
        "I can't help smiling as he gives us a golden review."
        "And it makes me all the more sure I'm doing the right thing."
        bree.say "So maybe we should make it more formal, yeah?"
        bree.say "You know, officially go steady?"
    else:
        bree.say "How many dates have we been on now, Jack?"
        "The question seems to catch Jack off-guard."
        "He frowns and looks thoughtful as he ponders it."
        jack.say "Oh, I don't know, [hero.name]..."
        jack.say "I didn't know I was supposed to keep count!"
        bree.say "Don't worry, Jack - it's not a test!"
        bree.say "I was just thinking that things are going great for us."
        bree.say "And I wondered if you wanted to kind of make it official?"
        "Realisation dawns in Jack's eyes."
        jack.say "You...you mean you want to go steady?"
        bree.say "Yeah, Jack - so how about it?"
    return

label jack_go_steady_yes_female:
    if game.week_day % 2 == 0:
        jack.say "Are...are you serious, [hero.name]?"
        bree.say "Ah...yeah, Jack."
        bree.say "Of course I'm serious!"
        bree.say "Why wouldn't I be?"
        "Jack shakes his head and shrugs off the question."
        jack.say "Oh, never mind..."
        jack.say "I just never had much luck with women in the past!"
        jack.say "But yeah - of course we should go steady!"
        jack.say "I'd love that!"
    else:
        jack.say "Well yeah, [hero.name]..."
        jack.say "I don't want to stop seeing you."
        jack.say "In fact, I want to see even more of you!"
        jack.say "So we should definitely do that!"
        bree.say "That's great!"
    return

label jack_go_steady_no_female:
    if game.week_day % 2 == 0:
        jack.say "Aw, [hero.name]..."
        jack.say "Why'd you have to go and do that?"
        "I shake my head, confused by Jack's reaction."
        bree.say "Do what, Jack?"
        bree.say "I don't understand?"
        jack.say "That's how you jinx something like this!"
        jack.say "When it's going well, you never SAY it's going well!"
        jack.say "That's like asking for it to go bad!"
        bree.say "Oh...sorry..."
        bree.say "Just for the record, you don't want to..."
        jack.say "No, [hero.name] - I don't want to go steady!"
        "Well, that told me!"
    else:
        jack.say "Urgh..."
        jack.say "Why'd you have to go and do a thing like that, [hero.name]?"
        jack.say "Things were going so well until you wanted to turn it into a relationship!"
        jack.say "Now it's like you're wanting us to get married or something!"
        bree.say "Oh...sorry...I guess..."
    return

label jack_pet_intro_female:
    if game.week_day % 2 == 0:
        "I can't help staring at Jack, smiling and thinking how cute he looks."
        "I mean sure, he's pretty darn handsome and manly, in his own special way."
        "But there's just something about him that makes me want to reach out and pet him!"
        "And that's just what I find myself doing, even before I'm aware of it."
        "My hand is stretched out, and I'm patting him on the head."
        "It's just what I'd be doing if he was a dog that deserved praise."
        bree.say "Good boy!"
        bree.say "Good boy!"
        "I cover my mouth with my hand as soon as I hear the words."
        "Did I really just say that out loud?!?"
        "Jack turns around to look at me, confusion on his face."
        jack.say "[hero.name], did you just..."
        jack.say "Did you pat me on the head?"
        bree.say "Ah...yeah - I guess so!"
    else:
        "I suddenly feel a surge of affection for Jack."
        "It's not like I can even explain where it comes from."
        "And maybe that's also something to do with what happens next."
        "Because I find myself reaching out without even thinking about it."
        "And then I pat him on top of the head, like he's a dog or something!"
        "The moment I do so, Jack looks up at me in surprise."
        jack.say "[hero.name]..."
        jack.say "Did you..."
        jack.say "Did you just pat me on the head?"
        bree.say "Erm...yeah, Jack."
        bree.say "I guess so!"
    return

label jack_pet_happy_female:
    if game.week_day % 2 == 0:
        "Jack looks puzzled, but he smiles all the same."
        jack.say "Weird..."
        jack.say "But acceptable!"
        jack.say "Should I expect more of the same?"
        bree.say "If you liked the first one?"
        "Jack smiles and nods."
        "Which gives me a funny, warm feeling inside."
    else:
        jack.say "Okay, [hero.name]..."
        jack.say "That's pretty weird!"
        jack.say "But I guess it's okay."
        jack.say "It's just a little quirky, you know?"
    return

label jack_pet_annoyed_female:
    if game.week_day % 2 == 0:
        "Jack frowns and shakes his head."
        jack.say "Please don't, [hero.name]!"
        jack.say "I'm not a dog, you know?"
        bree.say "Erm...okay, Jack - sorry!"
        "Well, that certainly told me!"
    else:
        jack.say "Urgh..."
        jack.say "Would you please not do that, [hero.name]?"
        jack.say "It's kind of humiliating, you know?"
        bree.say "Oh..."
        bree.say "Okay, Jack..."
    return

label jack_massage_intro_female:
    if game.week_day % 2 == 0:
        "The second that I see him, I just know that Jack is super tense."
        "I can see it in his body-language and hear it in his voice too."
        "And I instantly start thinking of ways that I could help him out."
        "I know what would work - a massage!"
        "And no, it's not just an excuse to get my hands on him!"
        bree.say "Jack..."
        bree.say "You look kind of tense!"
        jack.say "You noticed?"
        jack.say "Yeah...I am feeling a little knotted up!"
        bree.say "Would be giving you a massage help?"
        bree.say "Just a massage - I promise!"
    else:
        jack.say "Ouch..."
        jack.say "Oh man, I'm really feeling tender today!"
        bree.say "What's the matter, Jack?"
        bree.say "Did you overdo it at the gym or something?"
        jack.say "No, [hero.name]..."
        jack.say "I took a big swing at a troll when I was larping the other day!"
        bree.say "Ooh...that's live action roleplaying, right?"
        jack.say "Yeah...I'm breaking in a new battle-axe."
        jack.say "And it's still a little heavy for me!"
        bree.say "I could have a look at it if you want?"
        bree.say "Maybe give you a little massage to help with the pain?"
    return

label jack_massage_accept_female:
    if game.week_day % 2 == 0:
        "Jack's face becomes instantly brighter at the offer."
        "He nods, even though it seems to cause him pain!"
        jack.say "Would you, [hero.name]?"
        jack.say "That sounds great!"
        "I smile, happy to know that I can help."
        bree.say "It's no problem, Jack."
        bree.say "I've done it before."
        "I don't mention what happened to [mike.name] or Sasha the last time I gave a massage."
        "And anyway, I'm sure I know what went wrong on those occasions - pretty sure..."
    else:
        jack.say "Could you, [hero.name]?"
        jack.say "I'd be really grateful."
        bree.say "Sure thing, Jack!"
        bree.say "Come over here and let me take a look at you."
        jack.say "Thanks, [hero.name]..."
        jack.say "You're like my own personal cleric with your healing magic!"
    return

label jack_massage_refuse_female:
    if game.week_day % 2 == 0:
        "Jack's face tells me all I need to know."
        "He frowns and furrows his brow."
        jack.say "Ah...no, [hero.name]."
        jack.say "I think I'll pass!"
        bree.say "Really?"
        bree.say "I've done it before!"
        jack.say "No, no..."
        jack.say "The last thing I want right now is someone else touching me!"
        "That sounds pretty final, so I decide to let the matter drop."
    else:
        jack.say "Ah, no..."
        jack.say "I think I'll pass, [hero.name]."
        bree.say "Really, Jack?"
        bree.say "It's no trouble."
        jack.say "No, [hero.name]..."
        jack.say "I should really go see a professional about this."
    return

label jack_piercing_nipples_reaction_female:
    if game.week_day % 2 == 0:
        bree.say "How are the nipples feeling now, Jack?"
        jack.say "They're still a little sore, [hero.name]."
        jack.say "But they're looking great!"
        jack.say "Thanks for convincing me to get them done."
        bree.say "You're welcome, Jack!"
    else:
        "I can see that Jack looks a little uncomfortable."
        "It's like his shirt is itching him or something."
        bree.say "Are you okay, Jack?"
        bree.say "Because you look edgy!"
        jack.say "Ah...you noticed, [hero.name]?"
        jack.say "It's because of these..."
        "Jack lifts his shirt, showing me what's underneath."
        bree.say "Whoa, Jack!"
        bree.say "You got your nipples pierced?"
        jack.say "Yeah, [hero.name] - what do you think?"
        bree.say "It looks great, Jack."
        bree.say "Really hot!"
        "Jack smiles and blushes a little, clearly happy with my reaction."
    return

label jack_piercing_navel_reaction_female:
    if game.week_day % 2 == 0:
        bree.say "How's the belly-button feeling now, Jack?"
        jack.say "It's still a little sore, [hero.name]."
        jack.say "But it's looking great!"
        jack.say "Thanks for convincing me to get it done."
        bree.say "You're welcome, Jack!"
    else:
        "I can see that Jack looks a little uncomfortable."
        "It's like his shirt is itching him or something."
        bree.say "Are you okay, Jack?"
        bree.say "Because you look edgy!"
        jack.say "Ah...you noticed, [hero.name]?"
        jack.say "It's because of these..."
        "Jack lifts his shirt, showing me what's underneath."
        bree.say "Whoa, Jack!"
        bree.say "You got your belly button pierced?"
        jack.say "Yeah, [hero.name] - what do you think?"
        bree.say "It looks great, Jack."
        bree.say "Really hot!"
        "Jack smiles and blushes a little, clearly happy with my reaction."
    return

label jack_piercing_dick_reaction_female:
    if game.week_day % 2 == 0:
        bree.say "How's your manhood feeling now, Jack?"
        jack.say "It's still a little sore, [hero.name]."
        jack.say "But it's feeling great!"
        jack.say "Thanks for convincing me to get it done."
        bree.say "You're welcome, Jack!"
        bree.say "Can't wait to see how it feels from my perspective too!"
    else:
        "I can see that Jack looks a little uncomfortable."
        "It's like his pants are itching him or something."
        bree.say "Are you okay, Jack?"
        bree.say "Because you look edgy!"
        jack.say "Ah...you noticed, [hero.name]?"
        jack.say "It's because of something down there..."
        "Jack gestures below his waist."
        "Specifically around his groin."
        bree.say "Whoa, Jack!"
        bree.say "You got your manhood pierced?"
        jack.say "Yeah, [hero.name] - what do you think?"
        bree.say "It sounds great, Jack."
        bree.say "Really hot!"
        "Jack smiles and blushes a little, clearly happy with my reaction."
    return

label jack_piercing_head_reaction_female:
    if game.week_day % 2 == 0:
        bree.say "How's the piercing feeling now, Jack?"
        jack.say "It's still a little sore, [hero.name]."
        jack.say "But it's looking great!"
        jack.say "Thanks for convincing me to get it done."
        bree.say "You're welcome, Jack!"
        bree.say "Can't wait to see how it feels from my perspective too!"
    else:
        "I can see that Jack looks a little uncomfortable."
        "It's like something in his mouth is bugging him."
        bree.say "Are you okay, Jack?"
        bree.say "Because you look edgy!"
        jack.say "Ah...you noticed, [hero.name]?"
        jack.say "It's because of this..."
        "Something sounds a little off with Jack's voice."
        "And when he opens his mouth, sticking out his tongue, I see why."
        bree.say "Whoa, Jack!"
        bree.say "You got your tongue pierced?"
        jack.say "Yeah, [hero.name] - what do you think?"
        bree.say "It looks great, Jack."
        bree.say "Really hot!"
        "Jack smiles and blushes a little, clearly happy with my reaction."
    return

label jack_piercing_nose_reaction_female:
    bree.say "How's the nose feeling now, Jack?"
    jack.say "It's still a little sore, [hero.name]."
    jack.say "But it's looking great!"
    jack.say "Thanks for convincing me to get it done."
    bree.say "You're welcome, Jack!"
    return

label jack_movie_liked_reaction_female:
    bree.say "Wow...just WOW!"
    bree.say "Wasn't that like the best movie ever, Jack?"
    bree.say "Those effects totally blew my mind!"
    jack.say "I was just gonna say the same thing, [hero.name]!"
    jack.say "That was a great call on your part."
    jack.say "You've got a knack for picking them."
    return

label jack_movie_indifferent_reaction_female:
    bree.say "Wow...just WOW!"
    bree.say "Wasn't that like the best movie ever, Jack?"
    bree.say "Those effects totally blew my mind!"
    jack.say "Meh..."
    jack.say "I guess it was okay, [hero.name]."
    jack.say "But it wasn't that good!"
    return

label jack_movie_disliked_reaction_female:
    bree.say "Wow...just WOW!"
    bree.say "Wasn't that like the best movie ever, Jack?"
    bree.say "Those effects totally blew my mind!"
    jack.say "Were we even watching the same film, [hero.name]?"
    jack.say "I've never seen such a pile of flaming garbage!"
    jack.say "Next time you need to let me pick the movie we see."
    return

label jack_abortion_reaction_female:
    jack.say "[hero.name]..."
    jack.say "Erm, [hero.name]..."
    "I turn to see Jack looking in my direction."
    "He looks nervous, like he really wants to ask me something."
    "But he doesn't know how to go about actually doing it."
    bree.say "Yeah, Jack?"
    bree.say "You got something on your mind?"
    "Jack smiles and shakes his head."
    "And then just as quickly, he nods."
    jack.say "Yeah...kind of..."
    jack.say "I mean, maybe it's not any of my business..."
    jack.say "But you looked pregnant before."
    jack.say "And now you don't look pregnant anymore..."
    jack.say "So I was wondering if..."
    "I cut Jack off before he can finish."
    "As I'm getting a little tired of this by now."
    bree.say "Yes, Jack..."
    bree.say "I'm not pregnant anymore."
    bree.say "I had a termination."
    if (jack.flags.know_is_father and jack.love >= 150) or jack.love <= 150:
        "Suddenly Jack's whole demeanour changes."
        "Before he was passive and painfully shy."
        "But now he seems to grow a spine and stand up taller."
        "On top of that, he actually looks pretty pissed too!"
        jack.say "You killed the baby, [hero.name]!"
        jack.say "That's what you did!"
        "I take a step backwards, shaking my head."
        "I don't know what to do, as I've never seen Jack like this before."
        bree.say "No, Jack!"
        bree.say "That's not how it is."
        bree.say "You know it's not!"
        jack.say "Oh yeah?"
        jack.say "Then why didn't you ask me how I felt about it, huh?"
        jack.say "You didn't bother because you knew I'd try to stop you!"
        bree.say "Jack, please!"
        jack.say "Don't touch me!"
        jack.say "I can't even look at you right now!"
        "With that, Jack turns and hurries away."
    else:
        "Suddenly Jack's whole demeanour changes."
        "Before he was passive and painfully shy."
        "But now it's like someone took the weight of the world off his shoulders."
        jack.say "Oh my god, [hero.name]..."
        jack.say "I feel bad saying this..."
        jack.say "But I'm SO relieved you did that!"
        "I nod, happy that Jack agrees with my chosen course of action."
        "But at the same time, it was still a pretty painful affair for me."
        "So it's hard to be upbeat about it in any way."
        bree.say "To be honest, Jack..."
        bree.say "I was worried you'd hate me for doing that."
        "Jack shakes his head at this."
        jack.say "Oh no, [hero.name]."
        jack.say "You had to do what you had to do."
        jack.say "And I know it must have been hard."
        jack.say "Just let me know if there's anything I can do to help."
        bree.say "Thanks, Jack..."
        bree.say "You're a good friend."
    return


label jack_belly_interaction_female:
    $ jack.set_flag("interact", 1, 1, "+")
    show jack at center, zoomAt(1.5, (640, 1040))

    menu:
        "Kiss my belly":
            call jack_belly_kiss_female from _call_jack_belly_kiss_female_1
        "Caress my belly":
            call jack_belly_caress_female from _call_jack_belly_caress_female_1
        "Listen to the baby":
            call jack_belly_listen_female from _call_jack_belly_listen_female_1
        "Never mind":
            pass
    return

label jack_belly_caress_female:
    "I'm getting that weird feeling that someone is watching me."
    "You know, that odd sense of eyes being on you?"
    "And you can almost feel it, like a strange itch?"
    "So I look up, to either see who it is or put the notion to bed."
    show jack smile at center, zoomAt(1.5, (640, 1040))
    "Which is when I find myself staring straight into Jack's face."
    "Seriously, he's like no more than a couple of inches away from me."
    with vpunch
    bree.say "SHIT!"
    show jack surprised at startle
    jack.say "AARGH!"
    "At once I jump backwards as Jack does the exact same thing."
    jack.say "What is it, [hero.name]?"
    jack.say "What's the matter?"
    show jack sad
    bree.say "What do you think's the matter, Jack?"
    bree.say "Somebody just snuck up on me, you know?"
    bree.say "Scared me half to death!"
    "Jack looks around with concern on his face."
    show jack worried
    jack.say "They did?"
    jack.say "Where'd they go?"
    show jack whining
    jack.say "Did they...oh...oh I see!"
    show jack sadsmile
    "Jack looks suitably mollified as he realises I'm talking about him."
    show jack whining
    jack.say "I'm sorry, [hero.name]..."
    jack.say "I was just..."
    jack.say "I just wanted to ask if I could...touch your bump?"
    show jack sadsmile
    "Part of me wants to go off on Jack for what he just did."
    "To tell him never to do it again or else."
    "But the truth is that he already looks totally ashamed of himself."
    "So I just let out a sigh and then shove my belly in his general direction."
    bree.say "Urgh..."
    bree.say "Okay, Jack..."
    bree.say "There you go."
    show jack smile
    "Jack nods eagerly, already reaching out towards my belly."
    "And as soon as he has his hands on it, he seems to totally zone out."
    "I'm still feeling a little pissed as I watch him doing it."
    "But the enthusiasm he has is kind of infectious."
    "And it means that I can't stay mad at him for very long."
    "I mean, Jack's kind of like a big kid in his own right."
    "Which makes me wonder how he's going to cope when it comes to being a dad."
    "Is he going to rise to the occasion and become a more mature version of himself?"
    "Or am I going to end up feeling like I have two kids to take care of instead on one?"
    "I guess there's no way to answer that question at this point in time."
    "I just have to do the best I can and hope that things work out in the end."
    $ jack.love += 2
    return

label jack_belly_kiss_female:
    show jack happy at center, zoomAt(1.5, (640, 1040))
    jack.say "Hold still, [hero.name]..."
    jack.say "I want to kiss the baby!"
    show jack smile
    "I look down to see that Jack's taken hold of my belly."
    "He has a hand on either side of it, gripping it gently."
    "And he's already kneeling down on the ground in front of me."
    "I can't help frowning as I stare down at him."
    bree.say "Jack..."
    bree.say "How are you going to do that?"
    bree.say "The baby's still inside of my..."
    "Jack answers my question a moment later, when he lifts up my top."
    show jack at center, traveling(2.5, 0.3, (640, 1940))
    "Because he then leans forwards and plants a kiss on the curve of my belly."
    bree.say "Oh..."
    bree.say "Okay..."
    bree.say "I guess that kind of works."
    "I'm still watching as Jack starts to move from one spot to another."
    "And pretty soon he's planting kisses all over it."
    "Almost like he's doing his best to cover every inch with his lips."
    bree.say "Erm..."
    bree.say "That's okay, Jack..."
    bree.say "You just keep right on going, yeah?"
    bree.say "Like, there's no need to actually ask me if it's okay..."
    "I have no idea of Jack is even hearing what I'm saying right now."
    "But it feels like I have to keep talking, just for my own sake."
    "And to feel like I have some kind of say in the matter too!"
    "Not that what he's doing to me is in any way unpleasant."
    "In fact, the longer Jack keeps it up, the more I feel as though I like it."
    "After all, I'm the absolute centre of his attention."
    "And he's devoting himself to the task with some serious dedication too."
    "So in the end, I decide to just lie back and leave him to it."
    "Enjoying the sensation of Jack covering my belly in kisses."
    "And when he finally seems to be done, I feel like I'm being shaken awake."
    "I find myself blinking and looking around, almost like I'm disoriented."
    "As well as feeling like I miss all of the attention I was just getting."
    "The problem is that now I have to figure out some way of asking Jack to do it all again."
    "But in a way that makes it seem like I'm the one doing him a favour."
    $ jack.love += 3
    return

label jack_belly_listen_female:
    show jack normal at center, zoomAt(1.5, (640, 1040))
    bree.say "Oh wow..."
    bree.say "Oooh..."
    bree.say "Man, that feels so weird!"
    "I can see that Jack's watching me as I hold onto my belly."
    show jack surprised
    "His eyes are wide and his face full of interest in what's happening."
    show jack worried
    jack.say "Is..."
    jack.say "Is that the baby, [hero.name]?"
    jack.say "Is the baby moving around in there?"
    show jack normal
    "I know full well that this kind of thing has a weird effect on people."
    "But I still can't help putting an ironic smile on my face all the same."
    bree.say "I certainly hope it's the baby, Jack."
    bree.say "Because I don't think there should be anything else inside of me right now!"
    show jack embarrassed
    "Jack looks up at me, an sheepish expression on his face."
    show jack lying
    jack.say "Oh..."
    jack.say "Oh yeah, [hero.name]..."
    jack.say "I guess that makes sense!"
    show jack sadsmile
    "Jack goes kind of quiet after that, but he keeps on staring at my belly."
    "And it doesn't take a genius to work out that he has something else on his mind."
    "So I decide that I really should call him out on it."
    "Or else he'll be staring at me for the rest of the day."
    bree.say "Was there something else, Jack?"
    bree.say "Something that's still on your mind?"
    "And it's about then that the realisation hits me."
    bree.say "Jack..."
    bree.say "Would you like to listen to the baby?"
    show jack surprised
    "The moment the words are out of my mouth, Jack stands to attention."
    "And I can see the surprise written all over his face."
    jack.say "[hero.name]..."
    jack.say "How did you know I wanted to do that?"
    jack.say "Are you serious?"
    jack.say "Can I actually do it?!?"
    show jack sadsmile
    "Rather than replying with words, I pull up my top instead."
    "Then I gently pat my belly, inviting Jack to help himself."
    show jack smile at center, traveling(2.5, 0.3, (640, 1940))
    "He hurries to take my up on the offer, bending over to place an ear against the curve."
    "I just stand back and watch as he moves his ear here and there, following the sounds."
    "And all the time Jack has a look of sheer amazement and wonder on his face."
    "Like he's listening to something magical that he's never heard before."
    "More than once I think about asking him just what it is that he can hear."
    "But I decide to hold my tongue and just leave him to it."
    "Because he looks so happy right now."
    "And how would he even begin to describe it to me anyway?"
    $ jack.love += 4
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
