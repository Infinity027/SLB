init python:
    Event(**{
    "name": "morgan_give_a_gift",
    "label": "npc_give_a_gift",
    "conditions": [
        Or(
            HeroTarget(IsBirthday()),
            IsSpecialDate("christmas"),
            IsSpecialDate("valentine"),
            ),
        PersonTarget(morgan,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "girl": "morgan",
    "once_day": True,
    "do_once": False,
    "quit": False,
    }
    )

label morgan_give_male:
    if "cool_sunglasses" not in hero.inventory:
        $ gift = "cool_sunglasses"
        "She hands me a small box."
        mike.say "Wow!\nThose glasses looks great!"
        mike.say "Thank you so much."
    elif morgan.love >= 25 and "military_boots" not in hero.inventory:
        $ gift = "military_boots"
        "She hands me a pair of boots."
        mike.say "They look fantastic."
        morgan.say "You're welcome [hero.name]."
    else:
        $ gift = "cake"
        "She hands me a box, obviously from a pastry shop."
        mike.say "Thanks."
    $ hero.gain_item(gift)
    return

label morgan_give_valentine_male:
    "Morgan walks hesitantly towards me."
    call morgan_greet from _call_morgan_greet_7
    show morgan
    morgan.say "Happy valentine's day [hero.name]..."
    "Morgan throws a box of chocolates towards me."
    mike.say "Thank you, Morgan."
    $ hero.gain_item("valentine_chocolates")
    return

label morgan_give_birthday_male:
    "Morgan walks towards me."
    call morgan_greet from _call_morgan_greet_8
    show morgan happy
    morgan.say "Happy birthday [hero.name]!"
    call morgan_give_male from _call_morgan_give_male
    return

label morgan_give_christmas_male:
    "Morgan walks towards me."
    call morgan_greet from _call_morgan_greet_9
    show morgan happy
    morgan.say "Merry Christmas [hero.name]."
    call morgan_give_male from _call_morgan_give_male_1
    return

label morgan_birthday_gift_male:
    show morgan
    if morgan.flags.birthdayknown:
        mike.say "Happy birthday Morgan."
        morgan.say "How sweet, you remembered my birthday!"
    else:
        morgan.say "How do you know my birthday?"
        mike.say "I didn't, it's just pure luck."
        $ morgan.flags.birthdayknown = True
    return

label morgan_gift_swimsuit_male:
    show morgan happy
    morgan.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy swimsuit."
    if morgan.male < 40 and morgan.sub >= 60:
        show morgan blush
        morgan.say "Thank you [hero.name]."
        $ morgan.flags.sexyswimsuit = True
    else:
        show morgan angry
        morgan.say "Thanks but no thanks [hero.name], it's objectifying..."
        morgan.say "Even worse than being naked..."
        $ hero.cancel_activity()
    return

label morgan_gift_cute_plushie_male:
    $ morgan.male -= 5
    return

label morgan_gift_collar_male:
    show morgan
    morgan.say "Well, someone sure took their vitamins this morning!"
    morgan.say "Did you say your prayers too?"
    "Ignoring the gentle gibe and eighties pop-culture reference, I'm already reaching into my pocket as I reply."
    mike.say "Very funny, Morgan."
    mike.say "Well, you remember how I was guilty of having made that little mistake about you, back when we were in high school?"
    show morgan happy at startle
    "Morgan shakes her head and snorts a quick laugh at my expense."
    show morgan normal
    morgan.say "[hero.name], how could I ever forget that you thought I was a guy for all that time?!?"
    morgan.say "But I thought we cleared all of that up before now?"
    morgan.say "God knows we've gotten up to things that should have proven I'm a girl since then!"
    show morgan wink
    "She leans in closer and treats me to a lascivious wink to make her point."
    "I frown in a good-natured way and make a wave to dismiss her comments in an amiable manner."
    show morgan normal
    mike.say "Thanks very much for stating the obvious, Morgan!"
    mike.say "No, this is more of a gesture to kind of say that's all behind us."
    mike.say "Maybe to say where we're going from here on as well..."
    "I can see that I've got her hooked by now, the intrigue written plainly on her angular little face."
    morgan.say "Come on, [hero.name] - don't leave a girl hanging!"
    "I oblige by holding up what I have in my hand, watching Morgan's expression intently as I do so."
    "At first, I honestly think that she mistakes it for a necklace or choker of some kind."
    "But then she looks a little more closely and realises that it's actually a blue leather dog-collar."
    "The only thing that marks it out as exceptional is the addition of a bronze pendant in the shape of a Venus symbol hanging from it."
    show morgan surprised
    "Morgan looks up at me, puzzlement written all over her face."
    morgan.say "[hero.name], is that...is that a dog-collar?"
    "I shake my head as I try to explain."
    mike.say "Well, you could put it on a dog, certainly."
    mike.say "But this is really a collar for you, Morgan."
    mike.say "What's the matter, don't you like it?"
    "She still looks puzzled, as though my words haven't cleared the matter up for her."
    morgan.say "But...why would you want to put a collar on me?"
    mike.say "The pendant's one reason - to let everyone know that you're a girl."
    mike.say "But the main reason would be to let people know that you're mine, Morgan - that you're my little pet bitch!"
    "I hold out the collar, gesturing for her to take it."
    if morgan.sub < 90:
        show morgan angry
        "Her bemusement soon turns into visible annoyance and then anger."
        "Morgan slaps my hand away, sending the collar flying at the same time."
        "She rounds on me then, shoving a finger up and into my face."
        if morgan.male >= 75:
            morgan.say "So that's your perverted little thing, is it?"
            morgan.say "Well let me tell you something, mister - you're not man enough to put a collar on THIS little bitch!"
            "Her eyes are wide and her nostrils flaring as she glowers at me from below."
            "I've never seen Morgan as mad as this, and if I'm honest, it's really kind of scary."
            morgan.say "Why don't you take your damn collar and shove it up your ass, before I do it for you?!?"
        elif morgan.male >= 25:
            morgan.say "Let me get this right, [hero.name]..."
            morgan.say "You expect me to put on a dog-collar and let you treat me like a pet?"
            "Morgan shakes her head and turns away from me for a moment, as if she needs to not see me right there and then."
            "She rounds on me a moment later, disappointment replacing puzzlement on her face."
            morgan.say "I really don't know whether to be more disgusted or disappointed, I honestly don't!"
        else:
            morgan.say "Eww...you want me to wear a creepy collar and pretend to be a dog?!?"
            morgan.say "[hero.name], I never knew you were secretly such a creep!"
            "Morgan recoils from me, as if she's afraid that touching me will pass on some unpleasant kind of contagion."
            morgan.say "I can't believe you'd think I'm THAT kind of girl!"
        $ morgan.love -= 20
        $ morgan.sub -= 10
        $ hero.cancel_activity()
    else:
        show morgan blush
        "I can see that I've piqued Morgan's curiosity, as she begins to eye the collar with visible anticipation."
        "Taking a gamble that I'm reading her mood correctly, I lean down and lift the collar to her throat."
        "She makes no effort to stop me, and so I fasten it in place, just tight enough so that she knows it's there."
        $ morgan.set_sex_slave()
        hide morgan
        show morgan flirt
        if morgan.male >= 75:
            "I can hear Morgan's breathing become that much heavier as I finish fastening the collar in place."
            "She keeps glancing at me sideways, almost like she wants me to see her."
            "But at the same time, she seems not to want to be seen to want it either."
            "She puts her hands up to feel at the collar, almost pulling on the leather strap for the sake of feeling the sensation it causes."
            "Morgan is silent the whole time, but I swear I can almost feel the heat coming off of her."
        elif morgan.male >= 25:
            "I hear the fluttering of Morgan's breath as the collar is finally in place and I remove my hands."
            "She reaches for it almost instantly with one hand, her fingers closing around the leather tightly."
            "At the same time, I see her other hand go unconsciously first to her breasts and then to her groin."
            "It's almost as though she's forgotten that there are other people present in her fascination with the collar."
            "Or else it's somehow made her not care in the slightest that they can see her becoming noticeably aroused..."
        else:
            "Morgan can hardly keep herself still as I fasten the collar and step back to admire my handiwork."
            "She bounces on the spot and flaps her hands in sheer excitement, not seeming to care that people are watching her the whole time."
            "When she turns to face me, she has a huge grin on her face and looks delighted with the course of events."
            "Even I have to admit to being surprised when she lolls her tongue out and holds up her hands beneath her chin."
            "I realise a moment later, when she makes a barking sound, that she's actually imitating a dog!"
        $ morgan.sub += 10
        "Finally relieved of the burden of carrying the collar around in my pocket, I feel like I can relax."
        "For better or worse, Morgan knows all about it now."
        "And I have the feeling that it's going to change our relationship to quite some degree."
    return

label morgan_gift_sexy_dress_male:
    "I feel a little nervous holding the box containing my gift for Morgan behind my back."
    "It's not that I never bought a girl something to wear before now, because I certainly have."
    "It's more the fact that Morgan's one of those people who has a very distinctive style."
    "She's always been like that, with a look that's all her own, you know?"
    "So the idea of buying something that was my choice and asking her to wear it..."
    "Well, let's just say that it's more than a little bit intimidating!"
    "But when I saw it, I just knew that I had to see Morgan wearing the thing."
    "So I'm just going to give it to her and hope for the best..."
    mike.say "Ah, Morgan..."
    show morgan normal
    morgan.say "Huh?"
    morgan.say "What's up, [hero.name]?"
    mike.say "I...I just got a little something for you, that's all!"
    "I must have the world's most nervous smile on my face right now."
    "And I swear I can see my hand shaking as I pull out the box."
    "But Morgan's smile is one of genuine surprise and joy."
    show morgan happy
    morgan.say "Oh wow!"
    morgan.say "That's more than a little something."
    morgan.say "Thank you so much, [hero.name]!"
    "I hand the box to Morgan and watch as she unwraps it."
    "Then she pulls out the contents and studies them intently."
    mike.say "I...I know it's like a dress, Morgan."
    mike.say "The kind of thing that women wear."
    mike.say "And I know you're kind of picky when it comes to things like that..."
    "I'm babbling almost the whole time that Morgan is studying the dress."
    "And I'm not sure that she's even hearing me as I keep on talking nonsense."
    show morgan normal
    "In the end she looks up and the expression on her face stops me dead."
    mike.say "Well, Morgan..."
    mike.say "What do you think?"
    if morgan.sub >= 30:
        "Morgan shakes her head as she holds the dress against herself."
        "Then she looks down at it, a smile spreading across her face."
        morgan.say "[hero.name]..."
        show morgan happy
        morgan.say "I had no idea you saw me in something like this!"
        if morgan.male >= 75:
            morgan.say "You know, I don't usually go in for this kind of shit."
            morgan.say "But for something this fucking kinky..."
            morgan.say "I think I could make an exception!"
        elif morgan.male >= 25:
            morgan.say "It's a bit of a shock, you know?"
            morgan.say "But...I kinda like it!"
            morgan.say "And I like the idea of you liking me in it too!"
        else:
            morgan.say "Who knew you were this naughty?"
            morgan.say "It's so exciting to find that out!"
            morgan.say "Makes me wonder what else you're hiding, [hero.name]!"
        "I feel a flood of relief sweep over me at Morgan's words."
        "And I almost droop from the tension that's released in that moment."
        mike.say "Oh, Morgan..."
        mike.say "I'm so glad you like it!"
        "Morgan's smile grows wider still."
        show morgan wink
        "And she adds a wink for good measure."
        morgan.say "I think you'll be even happier when you see me in it for the first time!"
        $ morgan.flags.sexydate = True
        $ morgan.flags.sluttydate = False
    else:
        "Morgan shakes her head as she hands the dress back to me."
        "And I take it without question, already feeling my mood sink."
        show morgan annoyed
        morgan.say "Yeah, I think I'll pass, [hero.name]!"
        if morgan.male >= 75:
            morgan.say "If I ever wear a fucking dress again, it won't be one like that!"
            morgan.say "What do you think I am, a fashion doll that's turned to prostitution?"
        elif morgan.male >= 25:
            morgan.say "I don't think you know the difference between subtly sexy and slutty!"
            morgan.say "So maybe in future, leave the fashion choices to me, yeah?"
        else:
            morgan.say "Eww...where did you even find something like that?"
            morgan.say "It looks like underwear - and really nasty underwear too!"
        "I look at the dress and then back up at Morgan."
        "I'm already starting to feel deeply embarrassed at my mistake."
        "And so I hastily stuff the dress back into its box."
        mike.say "Ah..."
        mike.say "Yeah, Morgan..."
        mike.say "You're right...of course you're right."
        mike.say "I honestly don't know what I was thinking!"
        "Maybe this isn't as bad as it seem on the surface?"
        "Maybe Morgan really does think that I just screwed up?"
        "Maybe I can return the dress and get my money back?"
        $ morgan.love -= 4
        $ hero.cancel_activity()
    return

label morgan_gift_slutty_dress_male:
    "Part of me is still adjusting to the mind-blowing revelation that Morgan is actually a girl."
    "Seeing her strutting around in girl's clothes and behaving in a distinctly more feminine manner."
    "And so maybe that's one of the reasons that I felt compelled to buy her what's in the box."
    "The one that I'm currently doing the best I can to hide behind my back and keep her from seeing."
    "Not that my efforts seem to be all that successful, as she's already trying to sneak a peak at it."
    show morgan talkative
    if morgan.male >= 75:
        morgan.say "What'ya got there, huh?"
    elif morgan.male >= 25:
        morgan.say "Well, well, well - what you got there?"
    else:
        morgan.say "[hero.name], what have you got there?"
    show morgan normal
    "I do the best I can to twist and turn as Morgan tries to see behind my back."
    "Admittedly enjoying the playful experience of it all."
    "But in the end I decide to just present her with the box."
    "As it was always intended to be a gift for her anyway."
    mike.say "Okay, Morgan..."
    mike.say "I admit it - this is for you."
    "Morgan grins as I pull out the box and hand it over to her."
    show morgan happy
    morgan.say "Thanks, [hero.name]…"
    morgan.say "I can't wait to see what you got me!"
    show morgan normal
    play sound [paper_ripping_1, paper_ripping_2]
    "As Morgan begins to tear at the wrapping-paper, I can feel my anxiety returning."
    "And it seems to spike as she reaches into the box and pulls out what's inside."
    "The dress that I picked out for her unfurling and it opens out to its full length."
    show morgan surprised
    "I watch as Morgan's eyes go wide with surprise and she stares at the garment."
    "And she has every reason to stare as well, based on the kind of girl she is."
    "Because I've never seen her in something as boldly feminine as that dress."
    "And definitely nothing as risqué and revealing either."
    mike.say "Erm..."
    mike.say "Okay, Morgan..."
    mike.say "I know this is a little out of your comfort zone."
    mike.say "But I think it could really work, if you give it a chance."
    show morgan normal
    if morgan.sub >= 70:
        "Morgan keeps me in suspense for a few more long, agonising moments."
        "Her eyes travelling up and down the length of the dress the whole time."
        "And when she finally looks up at me, I can't help wincing in anticipation of what she's about to say."
        if morgan.male >= 75:
            show morgan talkative
            morgan.say "There's no way that I'm going to wear this in public!"
            morgan.say "But that doesn't mean that I want you to return it."
            show morgan flirt
            morgan.say "Because I'm going to wear it for you, in private!"
        elif morgan.male >= 25:
            show morgan talkative
            morgan.say "You know, I used to be totally against this kind of thing?"
            morgan.say "But since we got together, I've really learned to loosen up."
            show morgan flirt
            morgan.say "So maybe wearing stuff like this isn't such a big deal after all?"
        else:
            show morgan blushhappy
            morgan.say "You are SO right, [hero.name]…"
            morgan.say "It's about time I started really embracing my feminine side."
            morgan.say "And this dress is a great way to do that."
        show morgan blush
        "The feeling that washes over me is a mixture of relief and excitement."
        "Making me flush and smile, as well as feeling more than a little dizzy too."
        mike.say "Really?!?"
        mike.say "That's great, Morgan..."
        mike.say "But...erm..."
        mike.say "Exactly when are you thinking of wearing it?"
        "Morgan smiles and shakes her head as she folds the dress and puts it back into the box."
        "Clearly enjoying the chance to keep me in a state of suspense."
        $ morgan.flags.sluttydate = True
        $ morgan.flags.sexydate = False
    else:
        "Morgan doesn't keep me waiting long before giving me an answer."
        "Already folding up the dress and shoving it back into the box."
        "Before roughly thrusting the whole thing at me a moment later."
        show morgan angry
        if morgan.male >= 75:
            morgan.say "You can shove that right up your ass."
            morgan.say "I mean, do you see me dressing like a slut?"
            morgan.say "Nope - you're just totally clueless!"
        elif morgan.male >= 25:
            morgan.say "Yeah, there's no way I'm wearing that!"
            morgan.say "And I can't believe you thought that I would either."
            morgan.say "Don't you know me better than that?"
        else:
            morgan.say "Eww!"
            morgan.say "How could you buy me something so slutty?!?"
            morgan.say "Is that how you really see me?"
        show morgan upset
        "I'm already shaking my head and trying to excuse my mistake."
        "Withering under the verbal tirade that Morgan's delivering."
        mike.say "I..."
        mike.say "I'm sorry, Morgan..."
        mike.say "I don't know what I was thinking."
        $ hero.cancel_activity()
    return

label morgan_gift_butt_plug_male:
    show morgan happy
    morgan.say "Oh, [hero.name], is it for me?"
    "She unwraps the butt plug."
    if morgan.sub <= 50 or morgan.male <= 66 or not morgan.sexperience:
        show morgan annoyed
        morgan.say "..."
        morgan.say "Keep it... I don't want it so keep it."
        morgan.say "I'm sure you'll have a better use of it than me."
        $ hero.cancel_activity()
    else:
        morgan.say "It's perfect!"
        show morgan flirt
        morgan.say "Thanks [hero.name], I'll make a good use of it."
        $ morgan.flags.buttplug = True
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
