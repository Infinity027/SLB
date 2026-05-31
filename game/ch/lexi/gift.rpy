init python:
    Consumable("lexi_panties", display_name="Lexi's panties", effects=[("fun", 5)], frequency_limit="day")

    Event(**{
    "name": "lexi_give_a_gift",
    "label": "npc_give_a_gift",
    "conditions": [
        Or(
            HeroTarget(IsBirthday()),
            IsSpecialDate("christmas"),
            IsSpecialDate("valentine"),
            ),
        PersonTarget(lexi,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "girl": "lexi",
    "once_day": True,
    "do_once": False,
    "quit": False,
    }
    )

label lexi_give_male:
    if not hero.has_condom():
        "She hands me a box of condoms."
        mike.say "Thanks..."
        $ hero.gain_item("box_of_condoms")
    elif lexi.love >= 50:
        "She hands me a pair of panties."
        lexi.say "I just took them off."
        mike.say "..."
        lexi.say "You're welcome [hero.name]."
        $ hero.gain_item("lexi_panties")
    return

label lexi_give_valentine_male:
    "Lexi walks hesitantly towards me."
    call lexi_greet from _call_lexi_greet_7
    show lexi blush
    lexi.say "Happy valentine's day [hero.name]..."
    "Lexi throws a box of chocolates towards me."
    mike.say "Thank you, Lexi."
    $ hero.gain_item("valentine_chocolates")
    return

label lexi_give_birthday_male:
    "Lexi walks towards me."
    call lexi_greet from _call_lexi_greet_8
    show lexi happy
    lexi.say "Happy birthday [hero.name]!"
    call lexi_give_male from _call_lexi_give_male
    return

label lexi_give_christmas_male:
    "Lexi walks towards me."
    call lexi_greet from _call_lexi_greet_9
    show lexi happy
    lexi.say "Merry Christmas [hero.name]."
    call lexi_give_male from _call_lexi_give_male_1
    return

label lexi_birthday_gift_male:
    show lexi
    if lexi.flags.birthdayknown:
        mike.say "Happy birthday Lexi."
        lexi.say "How sweet, you remembered my birthday!"
    else:
        lexi.say "How do you know my birthday?"
        mike.say "I didn't, it's just pure luck."
        $ lexi.flags.birthdayknown = True
    return

label lexi_gift_swimsuit_male:
    if lexi.sub >= 60:
        mike.say "Err hey, Lexi..."
        mike.say "I saw this in the store the other day, and thought you might like it."
        show lexi happy
        lexi.say "Oh nice [hero.name]! That is a nice choice."
        show lexi wink
        lexi.say "Maybe I can give you a private show in it."
        $ lexi.flags.sexyswimsuit = True
    else:
        mike.say "Err hey, Lexi..."
        mike.say "I saw this in the store the other day, and thought you might like it."
        show lexi annoyed
        lexi.say "Yeah...maybe not."
        $ hero.cancel_activity()
    return

label lexi_gift_sexy_dress_male:
    show lexi happy
    lexi.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy dress."
    if lexi.sub >= 30:
        show lexi blush
        lexi.say "Thank you [hero.name]."
        $ lexi.flags.sexydate = True
        $ lexi.flags.sluttydate = False
    else:
        show lexi annoyed
        $ lexi.love -= 4
        lexi.say "Thanks but no thanks [hero.name], I would feel very awkward with that..."
        $ hero.cancel_activity()
    return

label lexi_gift_slutty_dress_male:
    "Normally I'd be scared stiff of giving a girl the kind of dress that I have behind my back."
    "Because the garment that I bought in an instant and had gift-wrapped is pretty bloody daring."
    "But the problem that I'm facing is kind of the opposite, that the girl in question might go the other way."
    "As it's not like Lexi tends to walk around in anything that isn't revealing in the extreme most of the time."
    "So the dilemma that I'm facing isn't that she's going to be offended by the raciness of what I've got her."
    "Rather that she might see it as being way too pedestrian for her tastes and toss it aside as a result."
    show lexi normal
    lexi.say "Hey, [hero.name]…"
    lexi.say "What have you got there?"
    lexi.say "Is it a little something for little old me?"
    show lexi smile
    "Ah shit!"
    "While I was busy worrying about the situation, Lexi's gone and spotted the box."
    "Leaving me without the time I'd banked on to be able to think up a decent plan."
    "I guess I'm just going to have to improvise and hope for the best."
    mike.say "It might be, Lexi, it might be."
    mike.say "I was just having a quick look around..."
    mike.say "Seeing if there was anyone else that caught my eye."
    mike.say "But as there isn't, I suppose you'll just have to do!"
    "Lexi lets out a typically filthy chuckle and jabs me in the ribs with her elbow."
    "I think the blow was supposed to be a playful one, but it hurts all the same."
    show lexi bored
    lexi.say "Yeah, yeah..."
    lexi.say "Very funny."
    lexi.say "Now hand it over!"
    show lexi smile
    "Not wanting a second jab in the ribs, I hurry to do as I'm told."
    play sound [paper_ripping_1, paper_ripping_2]
    "Lexi eagerly accepts the box and begins to tear off the gift-wrap."
    "And within the blink of an eye, she's opening the box."
    "But as she pulls out the dress inside, I almost hold my breath."
    show lexi wow
    lexi.say "Huh..."
    lexi.say "It's a dress."
    lexi.say "A dress that looks like it's made of holes stitched together!"
    show lexi smile
    mike.say "So..."
    mike.say "What do you think?"
    mike.say "I thought of you as soon as I saw it."
    if lexi.sub >= 70:
        "Lexi looks at me with a huge smile on her face."
        show lexi normal
        lexi.say "Well, I gotta admit, it's pretty tame for my tastes."
        lexi.say "But it's kinda cute that you'd buy me a dress."
        show lexi smile
        "I do the best I can to seize on the positive things Lexi says."
        "Pushing aside the fact that the dress is, as I suspected, tame by her standards."
        mike.say "Does that mean that..."
        mike.say "That you like it?"
        "Lexi nods her head as she holds the dress up against herself."
        "Something that makes my heart leap as I imagine her actually wearing it."
        show lexi happy
        lexi.say "Oh yeah."
        lexi.say "I mean, guys normally just buy me underwear."
        lexi.say "Or stuff to tie me up with in the bedroom, you know?"
        lexi.say "So you buying me something I can wear out and about is...sweet."
        show lexi smile
        "Okay, sweet wasn't exactly what I was aiming for."
        "But under the circumstances, I'll take it."
        mike.say "So you'll wear it for me?"
        show lexi flirt
        lexi.say "Oh sure thing, of course I will."
        lexi.say "A dress this demure and classy, I could wear to a fancy restaurant!"
        show lexi smile
        "I'm nodding along with everything Lexi's saying."
        "But I can't help thinking there's only one kind of place she'd get away with wearing the dress."
        "And that's the kind of place where she'd be likely to get mistaken for one of the girls dancing topless."
        $ lexi.flags.sluttydate = True
        $ lexi.flags.sexydate = False
    else:
        "Lexi looks at me with a huge smile on her face."
        show lexi happy
        lexi.say "Aww..."
        lexi.say "You're so sweet, [hero.name]!"
        lexi.say "But this is way too conservative for me."
        show lexi normal
        "I feel my hopes dying in my chest as Lexi hands the dress back to me."
        "But there really doesn't seem to be anything I can do to change her mind."
        mike.say "Oh well..."
        mike.say "I guess it was worth a try."
        "Lexi seems to pick up on the dejected tone that I'm using."
        "Because she puts a hand on my arm and gives me a smile."
        show lexi normal
        lexi.say "You kept the receipt, yeah?"
        lexi.say "I bet you did - you're that kind of a guy."
        lexi.say "So why not go back and trade it for some handcuffs or a Shibari rope?"
        $ lexi.love -= 10
        $ hero.cancel_activity()
    return

label lexi_gift_collar_male:
    show lexi
    "Any other girl and I'd have been up half the night worrying about everything being perfect."
    "I'd also have been planning the moment for months beforehand, fretting over how it'd turn out."
    "But this isn't any other girl - this is Lexi."
    "I've kind of gotten to know what makes her tick in the time that we've been together."
    "And I can tell you that she's pretty spontaneous, not the kind to beat around the bush."
    "Which is why I see no problem with just choosing a moment when there's nobody talking."
    "All I do is clear my throat and pull out the box that I've been hiding from her this whole time."
    mike.say "Ah, Lexi..."
    mike.say "I got you a little something."
    show lexi annoyed
    "She looks around, not at all concerned by what I just said."
    lexi.say "Huh?"
    lexi.say "What'd you say?"
    "Then she spots the box in my hands."
    "Lexi smiles, delight spreading across her face."
    show lexi happy
    lexi.say "Aww, [hero.name]."
    lexi.say "You bought me a present!"
    "Her expression becomes a little more naughty and conspiratorial in nature."
    lexi.say "I hope it's something nice."
    lexi.say "Something that makes me look sexy for you!"
    lexi.say "After all - I gotta find a way to say thank you..."
    "I can feel myself starting to sweat as she's saying this."
    "Partly because I obviously know exactly what's in the box."
    "But also because I can now vividly picture Lexi wearing it."
    "Wearing it while she makes good on that promise..."
    mike.say "Ah..."
    mike.say "Why don't you open it, Lexi?"
    mike.say "Open it and see what's inside?"
    lexi.say "Okay, [hero.name]."
    lexi.say "You better hand it over!"
    "I pass the box to her, watching as she eagerly opens the lid."
    "Lexi reaches in and pulls out what's inside."
    "In her hands, she's holding a collar."
    "It's pink in colour, shaped like a choker and hung with a cat-bell."
    "And it has the word 'SLUT' written on it in large, bold letters."
    "Lexi turns it over her in hands a couple of times, not speaking as she does so."
    "But then she looks up at me, and I see that her expression has changed."
    "And it's changed pretty dramatically too..."
    if lexi.sub < 90:
        $ lexi.love -= 20
        $ lexi.sub -= 20
        show lexi angry
        lexi.say "What the fuck, [hero.name]?"
        lexi.say "Is this what you think I am?!?"
        "She holds the collar up."
        "And then she waves it in my face to make her point."
        mike.say "Ah...Lexi, wait..."
        mike.say "It was just supposed to be a little fun."
        mike.say "A joke - that's all!"
        "Lexi sighs and shakes her head."
        lexi.say "[hero.name], I know I'm not a nun."
        lexi.say "But I'm not just some cheap whore either!"
        lexi.say "Sure, I like to have fun as much as the next girl."
        lexi.say "Well...maybe more than the next girl."
        "Lexi shakes her head, trying to get back to what she was saying before."
        lexi.say "But...is that really how you see me?"
        "I can already feel my cheeks beginning to burn with shame."
        "Lexi's right, she is more than just a cheap tart."
        mike.say "I...I'm sorry, Lexi."
        mike.say "I guess I just didn't think it through."
        "I see her expression soften at this."
        lexi.say "Oh, [hero.name]..."
        lexi.say "Don't be such a dumb fuck, okay?"
        lexi.say "And please, don't turn into another Danny!"
        "I nod and watch as Lexi tosses the collar into a nearby bin."
        $ hero.cancel_activity()
    else:
        if lexi.sub.max < 100:
            $ lexi.sub.max = 100
        show lexi happy
        $ lexi.set_sex_slave()
        lexi.say "Oooh...WOW!"
        lexi.say "[hero.name], this is so...kinky!"
        "Lexi says this is such a low, lusty tone."
        "And the way she looks up at me too..."
        "I can feel my cock getting stiffer by the second!"
        mike.say "Ah...yeah, Lexi."
        mike.say "I'm just glad you like it!"
        lexi.say "Like it?!?"
        lexi.say "I fucking LOVE it!"
        lexi.say "Put it on me, [hero.name]."
        lexi.say "Put it on right now!"
        "Lexi claps her hands and bounces up and down on the spot as I oblige her."
        "And she happily lifts her chin, allowing me to tighten the collar too."
        mike.say "How does that feel, Lexi?"
        mike.say "Not too tight?"
        lexi.say "No, [hero.name], no way!"
        lexi.say "It's supposed to be tight - the tighter the better!"
        hide lexi
        show lexi a
        "As soon as the collar is in place, she turns around to face me."
        "Lexi looks down at the thing, batting the bell with her fingers."
        "At the same time she has such a broad grin on her face."
        "And the two together make her look so much like a playful cat!"
        lexi.say "Well, [hero.name] - waddaya think?"
        mike.say "What do I think?"
        mike.say "I think I'd rather show you how it makes me feel, Lexi!"
        "Somehow this actually manages to make Lexi's smile wider still."
        "And I can tell she's already imagining what that might involve..."
    return

label lexi_gift_butt_plug_male:
    show lexi happy
    lexi.say "Oh, [hero.name], is it for me?"
    "She unwraps the butt plug."
    if lexi.sub <= 50 or not lexi.sexperience:
        show lexi annoyed
        lexi.say "..."
        lexi.say "Keep it... I don't want it so keep it."
        lexi.say "I'm sure you'll have a better use of it than me."
        $ hero.cancel_activity()
    else:
        show lexi normal blush
        lexi.say "It's perfect!"
        show lexi flirt
        lexi.say "Thanks [hero.name], I'll make a good use of it."
        $ lexi.flags.buttplug = True
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
