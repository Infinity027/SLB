init python:
    Consumable("shiori_milk", display_name="Shiori's milk", effects=[("energy", 1), ("hunger", 1)], frequency_limit="day")

    Event(**{
    "name": "shiori_give_a_gift",
    "label": "npc_give_a_gift",
    "conditions": [
        Or(
            HeroTarget(IsBirthday()),
            IsSpecialDate("christmas"),
            IsSpecialDate("valentine"),
            ),
        PersonTarget(shiori,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "girl": "shiori",
    "once_day": True,
    "do_once": False,
    "quit": False,
    }
    )

label shiori_give_christmas_male:
    "Shiori walks towards me."
    call shiori_greet from _call_shiori_greet_9
    show shiori happy
    shiori.say "Merry Christmas [hero.name]."
    call shiori_give_male from _call_shiori_give_male
    return

label shiori_give_birthday_male:
    "Shiori walks towards me."
    call shiori_greet from _call_shiori_greet_8
    show shiori happy
    shiori.say "Happy birthday [hero.name]!"
    call shiori_give_male from _call_shiori_give_male_1
    return

label shiori_give_valentine_male:
    "Shiori walks hesitantly towards me."
    call shiori_greet from _call_shiori_greet_7
    show shiori blush
    shiori.say "Happy valentine's day [hero.name]..."
    call shiori_give_male from _call_shiori_give_male_2
    return

label shiori_give_male:
    "She hands me a bottle of milk."
    mike.say "Thanks."
    $ hero.gain_item("shiori_milk")
    return

label shiori_birthday_gift_male:
    show shiori
    if shiori.flags.birthdayknown:
        mike.say "Happy birthday Shiori."
        shiori.say "How sweet, you remembered my birthday!"
    else:
        shiori.say "How do you know my birthday?"
        mike.say "I didn't, it's just pure luck."
        $ shiori.flags.birthdayknown = True
    return

label shiori_gift_collar_male:
    show shiori
    shiori.say "A gift, for me?!?"
    "I nod indulgently at her genuine enthusiasm, producing a small box from where I've had it concealed this whole time."
    mike.say "It's nothing much, I admit."
    mike.say "Really it's a token of my affection."
    mike.say "And let's just say it's also something to let people know that you're mine..."
    "Shiori's smile endures as she opens the wrapping and reaches inside the box."
    "But when she pulls out what's inside, it isn't replaced by a frown."
    "Rather a confused expression as she cocks her head on one side and holds it up to me."
    "Her mouth hangs open, as if silently asking for an explanation."
    "In Shiori's hand is a leather collar, patterned black and white like the coat of a Friesian cow."
    "The collar bears no tag or other means of identification save for a tin cattle bell, which dangles from the middle."
    "I meet Shiori's uncomprehending gaze with an indulgent smile, pointing at the collar in her hands."
    mike.say "When I saw that, Shiori, I just couldn't help instantly thinking of you."
    shiori.say "R...really?"
    shiori.say "This is like...like the kind of bell you'd put on a...a cow!"
    "I nod again, gesturing to her as I explain my thinking."
    mike.say "Sure, Shiori, it's exactly that."
    mike.say "And it suits you down to the ground, don't you think?"
    "Shiori blinks and stutters in response, as though she can't quite process what I'm saying."
    mike.say "Face it, Shiori - a cow is pretty much what people think of when they look at you."
    mike.say "You're sweet and docile, with your udders swaying as you chew the cud."
    mike.say "Sure, you can call them breasts and say that you work in an office for a living, but in the end it's pretty much the same thing."
    "Her cheeks redden noticeably, and she puts her hands over her breasts in an unconscious motion."
    mike.say "We both know you're no modern, independent career woman, Shiori."
    mike.say "What you really want in life is for someone to come along and make all of the decisions just disappear."
    mike.say "Someone to put a collar on you and lead you off like the cow you've always wanted to be."
    "At this, she looks up at me almost desperately."
    mike.say "Put that collar on, and that's just what'll happen."
    mike.say "You'll be my little pet cow..."
    if shiori.sub < 90:
        "Shiori nods her head slowly, holding my eye the entire time."
        "Her nervous smile puts me in mind of the way someone might look at a lunatic as they indulge them in the hope of escaping at the right moment."
        shiori.say "Thank you, [hero.name] - it's a very nice gift, very thoughtful..."
        shiori.say "If you don't mind though...I think I'll wait until I get home to try it on?"
        "I try to put a brave face on things, shrugging and acting as though it's no big deal."
        mike.say "Erm, yeah...whatever you think's best, Shiori!"
        "My smile must be turning into a rictus by now, and I'm wishing that the ground would open and swallow me up."
        "Shiori's trying her best to be polite with me now."
        "But I can already feel her looking for the first opportunity to make her excuses and leave."
        $ hero.cancel_activity()
    else:
        "Shiori, looks into my eyes for a long, lingering moment."
        "I can tell without the need for words that she's weighing up all that I've said, trying to come to a decision."
        "And then she raises the collar and proceeds to strap it in place around her neck."
        $ shiori.set_sex_slave()
        hide shiori
        show shiori
        "The blush that was on her cheeks before has become a riot of red by the time she looks up at me with the collar around her neck."
        "Shiori's hands linger around the bell for a couple of seconds, and then she clasps together tightly in her lap."
        "As strange as it might sound, somehow the collar and bell look just so natural on her."
        "In fact, they almost look like the missing element of her being that's been absent up to this point."
        "Reading the approval in my eyes, Shiori giggles suddenly and shakes her chest so that the bell clangs gently."
        shiori.say "I don't know if I should say 'moo'...or would that be just too silly?"
        mike.say "I think a moo from you would be a pretty sexy sound!"
        mike.say "Especially from such a hot little cow!"
        "At this, Shiori giggles again, putting a hand over her mouth."
        "She looks away for a moment, as if gathering her courage."
        shiori.say "M...M...Moo!"
        "I nod approvingly, and she gives me a coy, sideways glance."
        shiori.say "Mooooo!"
        mike.say "That's right, Shiori - you're my little pet now, so there's no need to worry any more."
        mike.say "You can even call me 'Master', from now on."
        "Something seems to spark in Shiori's eyes at the mention of the word."
        shiori.say "Oh, yes...M...Master!"
        $ shiori.sub += 10
    "Once Shiori's gone, taking the collar with her, I can finally breath a sigh of relief."
    "Just being able to present her with it feels like a load off of my mind."
    "And I really think that this is going to be the point at which I look back and remember when things changed for us in a very real way."
    return

label shiori_gift_swimsuit_male:
    show shiori happy
    shiori.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy swimsuit."
    if shiori.sub >= 60:
        show shiori blush
        shiori.say "Thank you [hero.name]."
        $ shiori.flags.sexyswimsuit = True
    else:
        show shiori sad
        shiori.say "I am sorry, I am not ready to wear that [hero.name]..."
        $ hero.cancel_activity()
    return

label shiori_gift_sexy_dress_male:
    show shiori happy
    shiori.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy dress."
    if shiori.love >= 100 or shiori.sub >= 50:
        show shiori blush
        shiori.say "Thank you [hero.name]."
        $ shiori.flags.sexydate = True
        $ shiori.flags.sluttydate = False
    else:
        show shiori sad
        shiori.say "I am sorry, I am not ready to wear that [hero.name]..."
        $ hero.cancel_activity()
    return

label shiori_gift_slutty_dress_male:
    "Okay, I know that Shiori's not exactly the most forward or flirtatious kind of girl."
    "But there's no way you can deny that she's in possession of a body that's pure dynamite."
    "The merest glance of her walking past always puts me in mind of milking cows, you know?"
    "And I can't help thinking that figure is just crying out for the chance to be made more of."
    "Which is why I decided to buy the dress that I'm currently hiding in a box behind my back."
    "Gambling on the notion that Shiori's conservative style of dress is on account of her shyness."
    "And that what she really needs is a gentle push towards wearing things with a little more...visual impact."
    show shiori talkative
    shiori.say "Oh..."
    shiori.say "Hello, [hero.name]…"
    shiori.say "It's so nice to see you!"
    show shiori smile
    "I can't help smiling in response to Shiori's own sweet smile."
    "Rubbing the back of my neck with one hand and feeling a little awkward."
    mike.say "Ah..."
    mike.say "Hey, Shiori..."
    mike.say "It's great to see you too!"
    "Shiori keeps on smiling and holds my eye."
    "But at the same time she leans over to the side, drawing my gaze downwards."
    "And she keeps on doing that until we're both looking straight at the gift-wrapped box."
    show shiori talkative
    shiori.say "Looks like some lucky person's in for a surprise!"
    show shiori smile
    mike.say "Oh..."
    mike.say "Yeah, Shiori..."
    mike.say "You got me!"
    "I pull out the box and hand it over to her, still rubbing the back of my neck."
    mike.say "I went and bought you a little something."
    mike.say "Hope you like it!"
    "Shiori takes the box from me, grinning from ear to ear as she does so."
    show shiori happy
    shiori.say "Oh, [hero.name], you're so kind."
    shiori.say "I'm sure whatever it is will be wonderful!"
    show shiori embarrassed
    play sound [paper_ripping_1, paper_ripping_2]
    "I watch with baited breath as Shiori carefully tears off the gift-wrap."
    "And then she opens the box, gently lifting out the dress inside of it."
    show shiori surprised
    shiori.say "Oh my goodness..."
    shiori.say "It looks like a dress."
    show shiori normal
    shiori.say "But where's the rest of it gotten to?"
    mike.say "Erm..."
    mike.say "No, Shiori - that's all of it!"
    mike.say "So you were saying...it's wonderful, right?"
    if shiori.sub >= 70:
        "Shiori holds up the dress, measuring it against herself."
        "Almost as if she can't believe that it will actually fit her."
        show shiori embarrassed
        shiori.say "You really want to see me in something like this?"
        show shiori normal
        mike.say "Oh yeah, Shiori..."
        mike.say "It's the kind of thing I dream about seeing you in!"
        show shiori embarrassed
        "Shiori looks more amazed than ever by my admission."
        "But the I see a new expression spreading across her face."
        "One that seems to show more confidence and conviction."
        show shiori happy
        shiori.say "Okay, [hero.name]…"
        shiori.say "If you want to see that, then you will!"
        show shiori flirt
        "I feel relief wash over me as Shiori commits to wearing the dress."
        "As well as a rising sense of arousal at the thought of her in it."
        "I think about asking her when she might put it on for me."
        "But then I decide that might be pushing her just a little too far."
        "And instead I choose to leave it alone for fear of tainting my victory."
        $ shiori.flags.sluttydate = True
        $ shiori.flags.sexydate = False
    else:
        "Shiori holds up the dress, measuring it against herself."
        "Almost as if she can't believe that it will actually fit her."
        show shiori embarrassed
        shiori.say "You really want to see me in something like this?"
        show shiori normal
        mike.say "Oh yeah, Shiori..."
        mike.say "It's the kind of thing I dream about seeing you in!"
        show shiori embarrassed
        "Shiori looks more amazed than ever by my admission."
        "But the I see a new expression spreading across her face."
        "One that seems to show more confidence and not a little defiance too."
        show shiori angry
        shiori.say "Well, if that's the case - then you really don't know me at all!"
        show shiori annoyed
        "Shiori balls the dress up in her hands and then thrusts it into mine."
        "And before I can think of anything to say, she turns on her heels and walks briskly away."
        "I go to follow her, but then decide it would be better to just let her go."
        "Because maybe after she's cooled down, I can talk to her and repair some of the damage I've done."
        $ shiori.love -= 10
        $ hero.cancel_activity()
    return

label shiori_gift_cosplay_male:
    show shiori happy
    shiori.say "Oh, [hero.name], is it for me?"
    "She unwraps the cowkini."
    if shiori.love >= 150 or shiori.sub >= 75:
        show shiori blush
        shiori.say "Thank you [hero.name]."
        $ shiori.flags.cowkini = True
    else:
        show shiori sad
        shiori.say "I am sorry, I am not ready to wear that [hero.name]..."
        $ hero.cancel_activity()
    return

label shiori_gift_butt_plug_male:
    show shiori
    "I've been hiding the box behind my back for so long that it feels like forever."
    "But I finally feel as though the right moment's come for me to whip it out."
    "Shiori's smiling and seems to be as happy as I've ever seen her right now."
    "So what better time to surprise her with an unexpected gift?"
    mike.say "Shiori, I have something for you."
    "Instantly, her face flushes as she's caught completely off-guard."
    shiori.say "Oh, [hero.name] - this is such a surprise!"
    "I hand the box to her, watching as she unties the bow and tears off the wrapping paper."
    "Shiori plunges her hand into the tissue-paper inside, and then pulls out what she finds."
    shiori.say "Oh my!"
    "Her eyes are as wide as saucers as she stares at the huge, black butt-plug clutched in her hand."
    "Shiori looks at the sex-toy."
    "Then at me."
    "Then back at the toy again."
    shiori.say "Oh, [hero.name] - I really don't know what to say!"
    mike.say "You don't have to say anything, Shiori."
    mike.say "Just let me watch whenever you use it when I'm around..."
    if shiori.sub <= 50 or not shiori.sexperience:
        show shiori angry
        "Shiori shoves the butt-plug, box and all into my stomach with all the force she can manage."
        "Winded, I gasp and groan as she waves a disapproving finger in my face."
        shiori.say "You think I'm going to USE this disgusting thing at all?"
        shiori.say "Let alone let you watch me?!?"
        shiori.say "What kind of a girl do you think I am?"
        shiori.say "You revolting pervert!"
        $ shiori.sub -= 10
        $ shiori.love -= 10
        "Unable to get a single word out, I'm forced to weather Shiori's rant."
        "I still can't stand up straight as she crosses her arms and turns her back on me."
        shiori.say "I'll say goodbye now, and thank you not to follow me!"
        "And with that, she walks away, leaving me to wheeze and cough all on my own."
        $ hero.cancel_activity()
    else:
        $ shiori.flags.buttplug = True
        $ shiori.flags.anal += 1
        "Shiori keeps right on looking startled for a moment."
        "But then I see her expression begin to change."
        "She looks up at me, her large, innocent eyes fixing on mine."
        $ shiori.sub += 5
        shiori.say "You...you want to watch me?"
        "I nod."
        shiori.say "Watch me while I use this?"
        "I nod again."
        shiori.say "While I use this...on myself?"
        "I nod for a third time."
        "At this, Shiori looks away, as if suddenly coming over all bashful."
        "But I note that she's also nodding her head as she does so."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
