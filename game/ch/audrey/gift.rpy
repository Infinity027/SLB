init python:
    Event(**{
    "name": "audrey_give_a_gift",
    "label": "npc_give_a_gift",
    "conditions": [
        Or(
            HeroTarget(IsBirthday()),
            IsSpecialDate("christmas"),
            IsSpecialDate("valentine"),
            ),
        PersonTarget(audrey,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "girl": "audrey",
    "once_day": True,
    "do_once": False,
    "quit": False,
    }
    )

label audrey_give_male:
    audrey.say "What do you think about your present?"
    mike.say "What present?"
    audrey.say "The necklace I am wearing, silly."
    mike.say "!?"
    audrey.say "I bought it just so that you could see me wearing it..."
    return

label audrey_give_valentine_male:
    "Audrey walks hesitantly towards me."
    call audrey_greet from _call_audrey_greet_7
    show audrey blush
    audrey.say "Happy valentine's day [hero.name]..."
    "Audrey hands me a box of chocolates."
    mike.say "Thank you, Audrey."
    $ hero.gain_item("valentine_chocolates")
    return

label audrey_give_birthday_male:
    "Audrey walks towards me."
    call audrey_greet from _call_audrey_greet_8
    show audrey happy
    audrey.say "Happy birthday [hero.name]!"
    call audrey_give_male from _call_audrey_give_male
    return

label audrey_give_christmas_male:
    "Audrey walks towards me."
    call audrey_greet from _call_audrey_greet_9
    show audrey happy
    audrey.say "Merry Christmas [hero.name]."
    call audrey_give_male from _call_audrey_give_male_1
    return

label audrey_birthday_gift_male:
    show audrey
    if audrey.flags.birthdayknown:
        mike.say "Happy birthday Audrey."
        audrey.say "How sweet, you remembered my birthday!"
    else:
        audrey.say "How do you know my birthday?"
        mike.say "I didn't, it's just pure luck."
        $ audrey.flags.birthdayknown = True
    return

label audrey_gift_swimsuit_male:
    show audrey happy
    audrey.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy swimsuit."
    if audrey.sub >= 60:
        show audrey blush
        audrey.say "It's so pretty, thank you [hero.name]."
        $ audrey.flags.sexyswimsuit = True
    else:
        show audrey angry
        $ audrey.love -= 4
        audrey.say "Thanks but no thanks [hero.name]."
        audrey.say "You think I would wear that?"
        $ hero.cancel_activity()
    return

label audrey_gift_collar_male:
    show audrey
    "It's taken me a while to get used to Audrey's rather unique and spikey personality."
    "And in that time I've come to understand that there's far more to her than you might think."
    "I mean sure, at first you just think that she's acts like a jerk because she's a bitch."
    "But I know that all of that stuff is just what she chooses to show on the surface."
    "It's something that she gets off on, that she does for the thrill of it."
    "And I want to let her know that I get it - that I get her."
    "So I've been racking my brains for a way to do that."
    "And I think that I've come up with the perfect solution."
    "It's a little gift that Audrey should really love."
    "One that'll let her know how much I understand her."
    "So now all I have to do is wait for the perfect moment to give it to her."
    mike.say "Ah, audrey?"
    mike.say "I got you a little something."
    "Audrey's eyebrows shoot up as soon as I mention that I have something for her."
    "Of course she's naturally interested in the prospect of being given a gift."
    show audrey normal
    "But there's also that look of curiosity, almost suspicion in her eyes too."
    audrey.say "Hmm..."
    show audrey happy
    audrey.say "What's the occasion, [hero.name]?"
    audrey.say "It's not like it's my birthday yet!"
    show audrey normal
    "I shake my head and wave away Audrey's questions."
    mike.say "I know, Audrey, I know!"
    mike.say "But I don't need a reason to buy you something, do I?"
    mike.say "I just thought that I'd get you one to show how I feel."
    "Audrey looks suitably flattered as I produce the gift."
    "It's small enough for me to conceal it in my hands and prolong the mystery."
    "But of course it being so small doesn't mean that it's likely to be any less impressive."
    "Audrey cranes her neck, doing her best to see what I'm hiding from her."
    audrey.say "Aw, come on!"
    audrey.say "Stop it with the suspense already!"
    audrey.say "Let me see what you got me, [hero.name]!"
    "I hold out for a few more seconds, enjoying Audrey's frustration."
    "And then I open my hands to reveal what I'm holding."
    "It's a black leather collar, perhaps an inch in width."
    "The both edges are lined with a white frill."
    "And the metal tag at the front bears the word 'Toy', spelt out in capital letters."
    "Audrey's eyes go wider than ever at the sight of it."
    "She's shaking her head, like she doesn't know what to say."
    "So all I can do is keep right on smiling."
    "That and wait for her to recover the power of speech."
    if audrey.sub >= 90:
        show audrey blush
        "Audrey looks at the collar and then up at me."
        "There's something in her eyes that I can't quite read."
        "And for a moment I think that she's maybe going to tell me off."
        "Maybe that she's even going to slap me too!"
        "But then I realise that she's looking at me in disbelief."
        "It's like she simply can't believe the collar is real."
        mike.say "Audrey..."
        mike.say "Are you okay?"
        "My words seem to have the effect of snapping Audrey back to reality."
        "She shakes her head, as if clearing the mental cobwebs."
        "And then she nods with more enthusiasm."
        audrey.say "I...I'm fine, [hero.name]."
        audrey.say "I'm better than fine, actually!"
        "Without asking for permission, Audrey plucks the collar from my hands."
        "And then she begins to wrap it around her neck, so I hurry to help."
        "I'm eager to help fasten it in place, gratified that she likes it."
        $ audrey.set_sex_slave()
        hide audrey
        show audrey
        "As soon as the collar is in place, Audrey hurries to find a mirror or reflective surface."
        "In the end she settles for shooting herself with the camera on her phone, making faces as she does so."
        $ audrey.love += 5
        audrey.say "Oh...it's perfect!"
        audrey.say "I always wanted one of these, [hero.name]."
        audrey.say "But I felt like I couldn't buy one myself, you know?"
        audrey.say "I needed somebody else to get it and then get me one!"
        mike.say "I'm happy to be that guy, Audrey!"
        mike.say "And I'm happy that you like it too."
        "Audrey throws her arms around me, squeezing me tight."
        "She doesn't say anything more after that."
        "Not that it really matters."
        "As the collar around her neck seems to say it all anyway."
        $ audrey.flags.nickname = "toy"
    else:
        show audrey angry
        "It's probably because I'm waiting for her to speak that I'm so distracted."
        "And that's also why I don't even see the slap coming before it connects."
        $ audrey.love -= 20
        $ audrey.sub -= 10
        "Audrey's open palm cracks me on the cheek, turning my head to the side."
        "In the confusion, I drop the collar as I clutch at my stinging face."
        mike.say "Wha...what..."
        mike.say "What the hell..."
        mike.say "Audrey, what was that for?!?"
        "My words are awkward and stumbling."
        "But Audrey seems to have regained her own ability to speak."
        audrey.say "Like you don't know!"
        audrey.say "You fucking creep!"
        "I'm still shaking my head, unable to make sense of what's happening."
        "Audrey was supposed to love the collar, to be thanking me for it."
        "Did I really misread the signs with her that badly?"
        mike.say "I...I thought you'd be into it, Audrey!"
        audrey.say "I don't want to be something you own, [hero.name]!"
        audrey.say "Where's the fun in that?"
        audrey.say "I want to be one of the players - not the plaything!"
        "Audrey turns her back on me and storms away."
        "And she manages to do it before I can say another word too."
        "I think about following on her heels."
        "But then I dismiss the idea, as I don't want another tongue-lashing."
        "All I can do is bend down and pick up the collar from where it fell."
        "That and wonder how I managed to read the situation so badly."
        $ hero.cancel_activity()
    return

label audrey_gift_slutty_dress_male:
    "As soon as I have the chance, I pull out the package that contains the gift I have for Audrey."
    "I knew that I had to get it for her the very moment that I first laid eyes on it."
    "And it's all that I've been able to think about since I walked out of the shop with it too!"
    "I just hope that it's enough to cut through Audrey's usual layers of sarcasm and apathy."
    mike.say "Audrey...hey, Audrey!"
    mike.say "Have you got a minute to spare?"
    mike.say "I got something for you!"
    show audrey happy
    "Audrey lets out a snort of laughter as I hurry over to her."
    "And she shakes her head at my obvious enthusiasm."
    show audrey frown
    audrey.say "Yeah, I can see what you've got for me, [hero.name]."
    audrey.say "It's written all over your face!"
    show audrey normal
    "I try as best I can to ignore Audrey's words and just press on."
    "Thrusting the gift into her hands, I give her no choice but to take it from me."
    "Audrey lets out a sigh of resignation and takes the package from me."
    show audrey happy
    "It doesn't take long for her to tear open the wrapping paper and pull out what's inside."
    "She holds it up to the light, revealing an outfit that's skimpy and revealing in the extreme."
    "Even the sight of her holding it is enough to get me excited."
    "And I can already feel my cock getting hard at the thought of seeing her in it too!"
    mike.say "I just saw it and thought of you, Audrey."
    mike.say "Well, what do you think?"
    if audrey.sub >= 70:
        "Audrey looks up at me, an ironic smile on her face."
        show audrey normal
        audrey.say "Aww..."
        audrey.say "You thought of me, huh?"
        audrey.say "But I bet it was your dick doing the thinking, right?"
        "I can feel my cheeks beginning to flush."
        "Audrey just seems to be able to see right through me like that."
        mike.say "I...thought you'd look nice in it, Audrey!"
        audrey.say "Oh yeah, [hero.name], I bet!"
        show audrey flirt
        audrey.say "I bet you got a really good mental image of it too."
        audrey.say "In fact, I bet you can't think of anything else but me in this thing!"
        "Audrey laughs in sheer delight when I can't answer her."
        "Because she knows full well it's as good as an admission that she's right."
        audrey.say "Oh, [hero.name] - you're so predictable!"
        audrey.say "It'll be worth wearing this thing."
        audrey.say "Even if it's just to keep on living in your mind rent-free!"
        "All I can do is nod and laugh along with her."
        "Telling myself the whole time that it doesn't matter what she says to me."
        "Not so long as I get to see her in that outfit!"
        $ audrey.flags.sexydate = False
        $ audrey.flags.sluttydate = True
    else:
        "Audrey lets out a peal of derisive laughter and shakes her head."
        "Then she unceremoniously shoves the gift back into my hands."
        show audrey annoyed
        mike.say "Y...you don't like it?"
        mike.say "I thought you'd love this kind of thing!"
        "Audrey cocks her head on one side, the smile on her face becoming cruel as she does so."
        "I can see that she's getting a kick out of how awkward all of this is making me feel."
        "She's enjoying the chance to put me on the spot and really make me squirm."
        audrey.say "Nah, [hero.name] - that's not it."
        audrey.say "I've got tons of stuff like that in my wardrobe back home."
        show audrey angry
        audrey.say "It's more that I don't want to dress up as your pathetic little wank-fantasy!"
        audrey.say "But thanks for letting me know that you'll be tossing one off over me tonight..."
        "And with that, Audrey turns on her heel and walks away."
        "Which leaves me standing there, alone with only my humiliation for company."
        $ audrey.love -= 10
        $ hero.cancel_activity()
    return

label audrey_gift_sexy_dress_male:
    "I do the best I can to keep a smile on my face as I get Audrey's attention."
    "Sure, she's the kind of girl that can smell bullshit from a mile away."
    "But I'm hoping that the fact I have a gift for her will change her mood."
    "I mean, it has to count for something, right?"
    "Everyone likes to be surprised with a thoughtful present."
    mike.say "Ah, Audrey..."
    show audrey
    "At the sound of my voice, Audrey looks over."
    "She has a familiar expression on her face."
    "The one that's a mixture of interest and cruel amusement."
    audrey.say "Hey, [hero.name]!"
    show audrey flirt
    audrey.say "Couldn't keep away from me, huh?"
    "I can't help the nervous laughter that bursts out of me."
    "And I feel myself rubbing the back of my head for something to do with my hands."
    mike.say "Ha...you got me, Audrey!"
    mike.say "Actually, I got you a little something..."
    "Without further ado, I thrust the package I've been holding towards Audrey."
    show audrey frown
    "She raises one eyebrow at me, and her smile could only be described as ironic."
    "But she takes the gift all the same, tearing off the paper in short order."
    mike.say "I saw it and thought of you, Audrey!"
    mike.say "Well...do you like it?"
    "Audrey doesn't answer straight away."
    "Instead she holds up the skimpy outfit that was inside the package."
    "It's black and what little there is of it is also extremely tight."
    "And I didn't just think of Audrey when I saw it."
    "I practically directed an entire porno in my head!"
    if audrey.sub >= 30:
        $ audrey.flags.sluttydate = False
        $ audrey.flags.sexydate = True
        "Audrey keeps on glancing up at me as she sizes up the outfit."
        "She chuckles to herself the whole time, making me feel more than a little nervous."
        show audrey annoyed
        mike.say "W...what's the matter, Audrey?"
        mike.say "Don't you like it?"
        "Audrey shakes her head at this."
        audrey.say "Aww, [hero.name]!"
        audrey.say "It doesn't matter if I give a shit about it or not."
        show fx question
        audrey.say "But you love it, don't you?"
        mike.say "Well I..."
        mike.say "I thought you'd look nice in it!"
        audrey.say "You didn't just think though, did you, [hero.name]?"
        show audrey flirt
        audrey.say "I bet you jerked off over the thought of me in it, didn't you?"
        "By now my cheeks are flushing red with embarrassment."
        "And I'm struggling to find the words to explain myself."
        audrey.say "It's okay, [hero.name]."
        audrey.say "I'll wear it for you."
        audrey.say "But just because I know it's your little wank fantasy!"
        "All I can do is nod and smile as Audrey tortures me."
        "Trying to keep in mind what it actually means."
        "That I'm going to get to see her in the thing for real!"
    else:
        "Audrey chuckles to herself, shaking her head as she sizes up the outfit."
        "For a moment I think it's going well, but then she shoves it back into my hands."
        show audrey annoyed
        mike.say "W...what's the matter, Audrey?"
        mike.say "Don't you like it?"
        "Audrey lets out a derisive snort at this."
        audrey.say "Oh no, [hero.name], it's not that."
        show audrey angry
        audrey.say "It's that I don't need fashion advice."
        audrey.say "At least not from a loser like you!"
        "And with that, Audrey turns her back on me and walks away."
        "Which leaves me standing there, lost for words."
        "And with a hell of humiliation churning in my guts too!"
        $ hero.cancel_activity()
    return

label audrey_gift_butt_plug_male:
    show audrey happy
    audrey.say "Oh, [hero.name], is it for me?"
    "She unwraps the butt plug."
    if audrey.sub <= 50 or not audrey.sexperience:
        show audrey annoyed
        audrey.say "..."
        audrey.say "Keep it... I don't want it so keep it."
        audrey.say "I'm sure you'll have a better use of it than me."
        $ hero.cancel_activity()
    else:
        show audrey normal blush
        audrey.say "It's perfect!"
        show audrey flirt
        audrey.say "Thanks [hero.name], I'll make a good use of it."
        $ audrey.flags.buttplug = True
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
