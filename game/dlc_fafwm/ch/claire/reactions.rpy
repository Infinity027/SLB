label claire_ice_cream_reaction_male:
    "I'm already feeling the heat of the day as we stroll along together."
    "But if I'm honest, at least some of that might be on account of my companion."
    "Because every glance I manage to steal in Claire's direction makes me feel hotter still."
    "She's just so damn sexy, and it's getting to the point where I need a distraction!"
    "And glancing around, I think I've seen just the thing."
    mike.say "Hey, Claire..."
    mike.say "It's crazy hot today, right?"
    mike.say "You want to grab an ice-cream from over there?"
    "Claire follows my gaze as I look over towards the ice-cream stand."
    "And then she nods, a charming smile spreading across her face as she does so."
    claire.say "That sounds really good, [hero.name]."
    claire.say "I can't remember the last time I had an ice-cream while I was on a date!"
    "I'm nodding and leading the way over to the stand as she says all of this."
    "But my head's already spinning on account of the fact Claire just called this a date!"
    "Once we make it to the ice-cream stand, I buy us one each."
    "And then I get to look on in awe and unbridled desire, as Claire licks her ice-cream."
    "Only snapping out if it when I feel the cold sensation of my own, melting onto my hand."
    "It snaps me back to reality, and I hurry to lick at it."
    "Trying to make it look like I wasn't just staring at Claire with my tongue hanging out."
    return

label claire_ask_phone_male:
    "I feel like Claire and I are really hitting it off, you know?"
    "Like she's genuinely starting to see me as one of her own friends."
    "Rather than just as someone her stepson used to know as a kid."
    "But to take things to the next stage, I need to be able to contact her myself."
    "I need that passport to a personal relationship that is a girl's phone-number."
    "So I put on the best nonchalant, casual tone that I can."
    mike.say "Claire, I just realised..."
    mike.say "I wanted to call you, but I don't have your number!"
    mike.say "How crazy is that?"
    if hero.charm >= 20 - claire.love:
        $ hero.smartphone_contacts.append("claire")
        "Claire looks up the moment I start to speak, interest written all over her face."
        "That's got to be a good sign, that she's genuinely surprised by the news."
        "And I also note that she's reaching for her phone at the same time."
        "Which has to be an almost concrete guarantee that she's about to give me what I want."
        claire.say "You don't already have it?"
        claire.say "Well then you should have told me earlier!"
        claire.say "Here you go, [hero.name]..."
        "I hurry to copy Claire's number into my phone."
        "And as I do so, she leans in to say more."
        claire.say "And don't worry about using it either."
        claire.say "You can call me any time - day or night!"
    else:
        $ claire.love -= 1
        $ claire.sub -= 1
        "Claire looks up the moment I start to speak, a frown on her face."
        "Which isn't something likely to fill me with hope of getting my way."
        "And I note that she also makes no effort to reach for her phone."
        claire.say "Well, I don't just go around giving it to everyone I meet!"
        claire.say "Is there any particular reason you should have it?"
        claire.say "Can't you just get Adam to pass on a message for you?"
        "She's got me there, because if she's just a friend's stepmom, then there really isn't."
        "So all I can do is nod and force an uncomfortable smile onto my face."
        "Who knows, maybe I can try again when I've managed to ingratiate myself more?"
    return

label claire_ask_birthday_male:
    "I feel like I need to do all that I can to ingratiate myself with Claire."
    "Anything that will make me feel more like a totally mature adult friend to her."
    "That and less like one of Adam's spotty old friends that happens to have made it to adulthood."
    "And I figure one way to do that would be to get to know when her birthday is."
    "That way I can arrange nice gifts and maybe even ask her out for a fancy meal somewhere."
    "But first I have to get that information out of her somehow."
    mike.say "Ah..."
    mike.say "Hey, Claire..."
    mike.say "When is your birthday?"
    "Okay, okay...I know that's not a very clever gambit."
    "But I'm kind of under pressure here, so cut me some slack."
    show claire stuned
    if hero.charm >= 40 - claire.love:
        $ claire.flags.birthdayknown = True
        "Claire hears my question and then gets one of those quizzical looks on her face."
        "Like her ears have perked up at hearing it, but she's also a little surprised too."
        show claire surprised
        claire.say "You don't know when it is?"
        claire.say "Huh...I assumed that you already did!"
        show claire happy
        claire.say "No bother - here it is..."
        "I make sure to note the date so that I won't forget it."
        "My brain already thinking of ways that I can use it to my advantage."
    else:
        "Claire hears my question and raises her eyebrows at it."
        "Then she shakes her head, like she disapproves somehow."
        show claire surprised
        claire.say "Don't you know that you should never ask a woman that?"
        show claire talkative
        mike.say "Erm..."
        mike.say "I thought you were never supposed to ask her age?"
        show claire talkative
        claire.say "Yes, but if you know the date of her birth..."
        claire.say "Then you can use that to work out her age!"
        show claire sad
        "All I can do is nod as Claire deftly dodges the question."
    return

label claire_offer_a_drink_male:
    "I drain the last dregs out of my glass and then make sure to put it down in a noisy manner."
    "Then I stand up, sure that Claire's attention is now focussed solely on me."
    mike.say "Okay, time for another one!"
    mike.say "You want me to grab one for you too, Claire?"
    if claire.is_visibly_pregnant:
        $ claire.love -= 10
        "Claire's face instantly changes to show a look of amazement and disbelief."
        "At the same time her hands close around her belly in a protective gesture."
        show claire whining
        claire.say "I'm sorry, [hero.name]..."
        claire.say "But did you forget that someone's pregnant?!?"
        show claire sadsmile
        mike.say "Oh...oh yeah...sorry!"
        $ hero.cancel_activity()
    else:
        show claire happy
        "Claire's face lights up as soon as I make the offer."
        "And she nods her head eagerly, making the gesture worthwhile."
        claire.say "That's so kind of you, [hero.name]..."
        claire.say "I'll have the same again, please."
        show claire happy
        mike.say "Coming right up!"
        if claire.love <= 25:
            $ claire.love += 1
        elif date_girl == claire and game.active_date:
            $ game.active_date.score += 5
        call expression claire.get_chat from _call_expression_539
        $ claire.set_flag("drinks", 1, "day", mod="+")
    return

label claire_slap_ass_intro_male:
    "Ever since I got reacquainted with Claire, I've been obsessed with her ass."
    "Oh, who am I trying to kid - I've always been obsessed with that woman's rear end!"
    "Even back when I was living at home, it caught my eye and haunted my dreams."
    "And since then, it just seems to have gotten better with time."
    "So now that I find myself in such close proximity to it, I'm being tortured."
    "Whenever Claire stands up, sits down or just walks past me - there it is."
    "That perfect pair of cheeks, like a gigantic peach, hovering in front of me!"
    "Before I know what's happening, my arm is moving, almost of it's own accord."
    play sound spank
    "And then there's the sound of a sharp clap, as the palm of my hand connects."
    "Of course, Claire leaps forwards and lets out a yelp of genuine alarm."
    claire.say "Ouch!"
    claire.say "Who did that?"
    claire.say "Who just slapped my arse?!?"
    "I look left and right, then back at Claire, not seeing any other possible culprits."
    "So the only thing I can think to do is just come clean."
    mike.say "Ah...yeah, it was me, I guess!"
    return

label claire_slap_ass_happy_male:
    "Almost as soon as the admission is out of my mouth, Claire's whole demeanour changes."
    "Where before she seemed to be shocked and then seriously pissed, now she's actually smiling."
    "And she also makes a point of waving a hand in the air too, like she's dismissing it all."
    claire.say "Oh well, if it's YOU that did it, [hero.name]..."
    claire.say "Then that's fine with me!"
    "As she says this, Claire seems to realise just how odd it sounds."
    claire.say "I...I mean it's not totally fine."
    claire.say "But it's better that you're the one doing it, rather than a total stranger."
    claire.say "You know what I mean?"
    "I nod, enjoying the look of embarrassment on Claire's face and the blush spreading over her cheeks."
    return

label claire_slap_ass_angry_male:
    "As soon as the admission is out of my mouth, Claire's attention is focussed on me like a laser-beam."
    "And I instantly regret everything - the actual slap and also the dumb idea of owning up to it."
    claire.say "How dare you do that to me?!?"
    claire.say "Weren't you raised with any kind of manners?"
    claire.say "Only a complete and utter animal puts his hands on a woman like that!"
    "All I can do is stand there and take it as Claire verbally lays into me."
    "Suffering her wrath and the consequences of my insatiable hunger for her ass."
    return

label claire_breakup_male:
    "Part of me can't believe that I'm actually doing what I'm about to do."
    "But then it's hard enough to believe that I ever managed to get involved with Claire in the first place."
    "So the act of breaking up with her is something that I could never have even imagined having to do."
    "The problem is that all of this stuff used to exist solely inside of my own head."
    "While ever it was there, Claire could remain the perfect woman and my ideal partner."
    "But in the real world, you quickly get too know how a person truly is."
    "And it pains me to say that Claire's fallen short of my expectations by quite a distance."
    "So sure, this is going to be painful, but there's no way around it."
    mike.say "Claire, there's no easy way to say this..."
    mike.say "I don't think this is working out."
    mike.say "You know - you and me being an item?"
    show claire stuned
    "Claire looks at me with wide eyes and an open mouth."
    "And for a moment it looks like she's going to argue with me."
    show claire sad
    "But then I see something change in her eyes, and she nods her head."
    show claire whining
    claire.say "I...I know what you mean, [hero.name]."
    claire.say "It's been fun, getting the chance to be with you."
    claire.say "And I don't think I'd change anything, if it all happened again."
    claire.say "But maybe it was never meant to be more than that - more than a little fling?"
    show claire sad
    "I nod my head, already knowing that she's trying her best to soften the impact."
    "That Claire's doing all she can to minimise the damage this is going to cause us both."
    "So instead of saying anything more, I just take her hand in mine."
    "Then I raise it to my lips, gently kissing her knuckles."
    "Which I hope she takes as a simple gesture of parting."
    return

label claire_go_steady_intro_male:
    "I feel like Claire and I have really been going places recently."
    "And I don't mean literally going out on dates either!"
    "We've been connecting on so many levels and getting so much closer."
    "All of which means I feel that we need to make it official."
    "Claire and I need to acknowledge that our relationship has matured."
    mike.say "Claire..."
    mike.say "I wanted to ask you something."
    show claire happy
    claire.say "Oh...what's that?"
    show claire normal
    mike.say "Well, I like you and you like me, that's obvious."
    mike.say "So why don't we make it official?"
    mike.say "Like, admit that we're a proper couple?"
    return

label claire_go_steady_yes_male:
    show claire surprised
    "Claire's eyes seem to flare with light and enthusiasm as I make my pitch."
    "And even before I'm finished saying my piece, she's nodding her head."
    show claire happy
    claire.say "Oh, [hero.name]..."
    claire.say "Why didn't I think of that myself?"
    claire.say "Of course we should do that - consider us officially dating!"
    return

label claire_go_steady_no_male:
    show claire surprised
    "Claire's brow furrows and her eyes narrow as I make my pitch."
    "And even before I'm finished saying my piece, she's shaking her head."
    show claire whining
    claire.say "Oh no, [hero.name]..."
    claire.say "I've done that kind of thing so many times already."
    claire.say "What I want now is to just keep things simple."
    show claire sadsmile
    return

label claire_pet_intro_male:
    "I've always had a thing for Claire, I think that's pretty obvious by now."
    "But what's less obvious is the fact that I always wanted to pet her on the head."
    "Yeah, I know it's a pretty weird thing to admit, but I just can't explain it."
    "She's just so cute and perky, I get the urge to pet her on the head, like a dog!"
    "And now that I'm spending more time around her, it's getting harder to resist."
    "Not least because of he way she's proved she likes the idea of me touching her."
    "So in the end, I find that there's nothing I can do to hold back the temptation."
    "As I walk past where Claire's sitting, I reach out and pat her on top of the head."
    "The fact that I'm standing and she's sitting makes pulling it off that much easier."
    "And it means that she's more than a little confused as to what just happened too."
    "Though that doesn't stop her from jumping up and looking around as soon as it's over."
    claire.say "Hey..."
    claire.say "What the hell was that?!?"
    "There's nobody else within reach of Claire right now."
    "So it's not going to take her long to figure out who the culprit is."
    "And I figure it's better to confess now and see what the consequences are for my actions."
    mike.say "Ah...it was me, Claire."
    mike.say "I just patted you on the head, that's all!"
    return

label claire_pet_happy_male:
    show claire stuned
    "As soon as she realises that I just owned up, Claire seems to stop in her tracks."
    "And for a moment she just stands there, like she's totally confused and flustered."
    "But soon enough she regains enough composure to put a smile on her face and shake her head."
    "Then it looks like all of the anger she was just showing has drained away."
    show claire surprised blush
    claire.say "Oh...well...that's alright then."
    claire.say "I...I mean technically it's not alright."
    claire.say "You shouldn't go around patting people on the head like that."
    claire.say "But what I meant was...it's better that you did it to me, [hero.name]..."
    claire.say "You and not some random stranger."
    show claire happy
    "I nod, trying to make it seem like I get what Claire's trying to say."
    "But the truth is that I'm not sure she knows that herself!"
    "Though I do note that her cheeks are flushing red and she can't quite look me in the eye."
    "So maybe she wasn't as upset with what I did as she was trying to make out."
    return

label claire_pet_annoyed_male:
    show claire stuned
    "As soon as she realises that I just owned up, Claire seems to stop in her tracks."
    "And for a moment she just stands there, like she's totally confused and flustered."
    "But soon enough she regains enough composure to put a formidable frown on her face."
    "Plus she wags a finger about an inch from my nose as well!"
    show claire surprised
    claire.say "That is not how you're supposed to behave, [hero.name]!"
    claire.say "You shouldn't go around patting people on the head like that."
    claire.say "It's totally demeaning, and it makes them feel like an animal."
    claire.say "And I can't believe it's something you'd be capable of!"
    show claire annoyed
    "I nod all the while that Claire's ranting and raving at me."
    "Doing the best I can to make it look like I'm ashamed of myself."
    "But the truth is that the telling off was totally worth it."
    "Because I felt a genuine thrill when I patted her on the head just now."
    "One that was only made that much better by her confused reaction to it."
    "And now all I want is to be able to do it all over again."
    return

label claire_massage_intro_male:
    "I can't help flinching in sympathy as I see Claire twitch and grimace."
    "Because it looks like she's pulled a muscle somewhere on her body."
    "And now she's paying the price for even the smallest of movements."
    show claire whining
    claire.say "OUCH!"
    show claire sadsmile
    mike.say "Ooh...that looks painful, Claire!"
    mike.say "Do you want me to take a look at it?"
    mike.say "Maybe give you a rub-down or something?"
    mike.say "I've been told that I give a pretty good massage!"
    return

label claire_massage_accept_male:
    show claire normal
    "Still clutching at the offending muscle, Claire nods eagerly."
    "But doing so only seems to make the matter that much worse."
    show claire happy
    claire.say "That sounds..."
    claire.say "AARGH!"
    claire.say "Damn it - that sounds like a great idea, [hero.name]!"
    show claire normal
    mike.say "Okay, okay..."
    mike.say "Let's get you laid down, then we can start the massage."
    return

label claire_massage_refuse_male:
    show claire sad
    "Still clutching at the offending muscle, Claire shakes her head."
    "But doing so only seems to make the matter that much worse."
    show claire talkative
    claire.say "No, thank you..."
    claire.say "AARGH!"
    claire.say "Damn it - I really need to see a professional!"
    show claire sadsmile
    mike.say "Okay, Claire, if you think that's for the best."
    mike.say "I certainly don't want to make things worse!"
    return

label claire_piercing_nipples_reaction_male:
    claire.say "[hero.name]..."
    claire.say "Come and look at this!"
    "Claire whips up her top before I can say a word in response."
    "And my eyes go wide as I'm presented with a view of her freshly-pierced nipples!"
    mike.say "WHOA!"
    mike.say "When did you get those done?!?"
    claire.say "Just this morning."
    claire.say "Aren't they great?"
    claire.say "I always wanted them done..."
    claire.say "But I never had the courage - not until I met you!"
    return

label claire_piercing_navel_reaction_male:
    claire.say "[hero.name]..."
    claire.say "Come and look at this!"
    "Claire whips up her top before I can say a word in response."
    "And my eyes go wide as I'm presented with a view of her freshly-pierced navel!"
    mike.say "WHOA!"
    mike.say "When did you get that done?!?"
    claire.say "Just this morning."
    claire.say "Isn't it great?"
    claire.say "I always wanted it done..."
    claire.say "But I never had the courage - not until I met you!"
    return

label claire_piercing_clit_reaction_male:
    claire.say "[hero.name]..."
    claire.say "Come and look at this!"
    "Claire yanks her waistband out before I can say a word in response."
    "And my eyes go wide as I'm presented with a view of her freshly-pierced pussy!"
    mike.say "WHOA!"
    mike.say "When did you get that done?!?"
    claire.say "Just this morning."
    claire.say "Isn't it great?"
    claire.say "I always wanted it done..."
    claire.say "But I never had the courage - not until I met you!"
    return

label claire_piercing_nose_reaction_male:
    claire.say "[hero.name]..."
    claire.say "Come and look at this!"
    "Claire pushes her face into mine before I can say a word in response."
    "And my eyes go wide as I'm presented with a view of her freshly-pierced nose!"
    mike.say "WHOA!"
    mike.say "When did you get that done?!?"
    claire.say "Just this morning."
    claire.say "Isn't it great?"
    claire.say "I always wanted it done..."
    claire.say "But I never had the courage - not until I met you!"
    return

label claire_piercing_head_reaction_male:
    claire.say "[hero.name]..."
    claire.say "Come and look at this!"
    "Claire pushes her face into mine before I can say a word in response."
    "And my eyes go wide as I'm presented with a view of her freshly-pierced septum!"
    mike.say "WHOA!"
    mike.say "When did you get that done?!?"
    claire.say "Just this morning."
    claire.say "Isn't it great?"
    claire.say "I always wanted it done..."
    claire.say "But I never had the courage - not until I met you!"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
