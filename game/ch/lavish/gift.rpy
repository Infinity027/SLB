init python:
    Equip("lavish_tie", display_name="Lavish's tie", type="accessory", effects={"lavish": 100, "charm": 10, "princess": 20})
    Item("lavish_lucky_panties", display_name="Lavish's lucky panties")

    Event(**{
    "name": "lavish_give_a_gift",
    "label": "npc_give_a_gift",
    "conditions": [
        Or(
            HeroTarget(IsBirthday()),
            IsSpecialDate("christmas"),
            IsSpecialDate("valentine"),
            ),
        PersonTarget(lavish,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "girl": "lavish",
    "once_day": True,
    "do_once": False,
    "quit": False,
    }
    )

label lavish_give_male:
    if "lavish_tie" not in hero.inventory and lavish.love >= 100:
        $ gift = "lavish_tie"
        "She hands me a pretty nice tie."
        mike.say "Wow!\nThanks!"
        lavish.say "It's nothing..."
    elif "lavish_lucky_panties" not in hero.inventory and lavish.sub >= 50 and lavish.love >= 100:
        $ gift = "lavish_lucky_panties"
        "She hands me a pair of panties."
        mike.say "Wow!\nThanks!"
        show lavish blush
        lavish.say "They are my lucky ones..."
        $ hero.luck += 1
    else:
        $ gift = "cake"
        "She hands me a box, obviously from a pastry shop."
        mike.say "Thanks."
    $ hero.gain_item(gift)
    return

label lavish_give_valentine_male:
    "Lavish walks hesitantly towards me."
    call lavish_greet from _call_lavish_greet_7
    show lavish blush
    lavish.say "Happy valentine's day [hero.name]..."
    "Lavish hands me a box of chocolates."
    mike.say "Thank you, Lavish."
    $ hero.gain_item("valentine_chocolates")
    return

label lavish_give_birthday_male:
    "Lavish walks towards me."
    call lavish_greet from _call_lavish_greet_8
    show lavish happy
    lavish.say "Happy birthday [hero.name]!"
    call lavish_give_male from _call_lavish_give_male
    return

label lavish_give_christmas_male:
    "Lavish walks towards me."
    call lavish_greet from _call_lavish_greet_9
    show lavish happy
    lavish.say "Merry Christmas [hero.name]."
    call lavish_give_male from _call_lavish_give_male_1
    return

label lavish_gift_collar_male:
    "I'm more than a little nervous about giving Lavish the gift that I have for her."
    "It's stashed in my pocket, and I can feel the weight of it tugging on me the whole time."
    "I know that this is a real gamble on my part, me taking a genuine risk."
    "But I think that I've been reading the signals that Lavish gives out pretty well."
    "Sure, she acts all confident and professional at work."
    "She's no-nonsense and focused on her job with the precision of a laser."
    "And yet I'm convinced it's all a front, a way of hiding what she really wants."
    "Surely nobody's actually that obsessed with their career?"
    "And the more extreme a person seems to be in one direction..."
    "Well, behind closed doors they usually bend in the opposite one - right?"
    "So with that in mind, I take a deep breath."
    "And then I pull the gift out of my pocket."
    lavish.say "Oh..."
    lavish.say "[hero.name], what's that you have there?"
    "I pass the box over to Lavish with one hand."
    "And I rub the back of my head with the other."
    mike.say "I...I got you a gift, Lavish."
    mike.say "Just a little something that I think you'll like."
    mike.say "Well, I hope you like it!"
    "Lavish's face lights up as she accepts the box."
    "Like most girls, she's clearly delighted with the idea of a spontaneous gift."
    "At first the smile stays put as Lavish plucks the surprise out of the box."
    "What she holds up is a collar, white in colour and looking like a choker."
    "But then she turns it over in her hands, noticing the pendant hanging from it."
    "Lavish reads the words engraved upon it carefully."
    "And then she blinks before looking up at me, a puzzled expression on her face."
    lavish.say "It...it says 'Doll' on here, [hero.name]."
    lavish.say "And the pendant..."
    lavish.say "It makes the thing look like..."
    lavish.say "Well...like a dog-collar!"
    "I smile broadly as I nod at this."
    mike.say "That's the idea, Lavish."
    mike.say "It's to let everyone know that you're mine."
    mike.say "To show that I'm like your master!"
    "Lavish stares at me in stunned silence for a few moments."
    "Her eyes have gone wider than ever."
    "And I can see that she's turning my words over in her mind."
    "I wait with baited breath to hear what she's going to say next..."
    if lavish.sub >= 90:
        lavish.say "H...how..."
        lavish.say "How did you know?"
        "Lavish looks up at me, eyes wider than I've ever seen them."
        "She clutches the collar to her chest as she asks the question."
        mike.say "I had a feeling, Lavish."
        lavish.say "But how, [hero.name]?"
        lavish.say "I thought I was keeping it a secret from everyone!"
        lavish.say "I thought everyone bought that I was one hundred percent professional!"
        mike.say "Maybe you were too good at it, Lavish?"
        lavish.say "You knew all along, [hero.name]!"
        lavish.say "You knew that what I really wanted..."
        mike.say "Was to have someone that you could belong to?"
        "Lavish nods hastily."
        lavish.say "Someone to praise me."
        lavish.say "Someone to see how clever I am."
        lavish.say "Someone to tell me that..."
        lavish.say "That I'm a good girl!"
        "I nod as I step forward and take the collar from her."
        "Lavish makes no effort to stop me as I slip it around her neck."
        "Instead she lets out little gasps of breath the whole time."
        "And it's almost like she's panting with excitement."
        $ lavish.set_sex_slave()
        hide lavish
        show lavish
        $ lavish.flags.mikeNickname = "Master"
        mike.say "There you go, Lavish."
        mike.say "How does it feel?"
        "Lavish touches the collar with the tips of her fingers."
        "She seems to be testing the sensation of it against her skin."
        lavish.say "It's...weird..."
        lavish.say "It's tight around my neck."
        lavish.say "But I feel...free!"
        "Lavish's face breaks into a smile."
        "She looks genuinely happy as she holds my eye."
        mike.say "That's good, Lavish."
        mike.say "That's my good girl!"
    else:
        $ lavish.love -= 20
        $ lavish.sub -= 20
        lavish.say "Jesus Christ, [hero.name]!"
        lavish.say "Are you even living in the twenty-first century?"
        lavish.say "How could you even think this would be a good idea?!?"
        "Lavish shoves the collar and box into my stomach."
        "I'm totally unprepared for that."
        "And so she manages to wind me pretty well too."
        mike.say "Urgh..."
        mike.say "Lavish..."
        mike.say "Wait..."
        "Lavish crosses her arms over her chest."
        "She stares at me with anger flaring in her eyes."
        lavish.say "I'm a modern, independent woman, [hero.name]."
        lavish.say "Not some kind of livestock!"
        lavish.say "No man is going to put a damn collar on me!"
        "I keep on trying to explain myself."
        "But my efforts only result in failure."
        "Lavish storms off without looking back."
        "Which leaves me alone."
        "Alone and still clutching my ill-judged gift."
        $ hero.cancel_activity()
    return

label lavish_birthday_gift_male:
    show lavish
    if lavish.flags.birthdayknown:
        mike.say "Happy birthday Lavish."
        lavish.say "How sweet, you remembered my birthday!"
    else:
        lavish.say "How do you know my birthday?"
        mike.say "I didn't, it's just pure luck."
        $ lavish.flags.birthdayknown = True
    return

label lavish_gift_swimsuit_male:
    show lavish happy
    lavish.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy swimsuit."
    if lavish.sub >= 60 or lavish.flags.sleaze >= 8:
        show lavish blush
        lavish.say "Thank you [hero.name] but you really wish me to wear that?"
        mike.say "Yes."
        lavish.say "But all men will be looking at me with lewd eyes..."
        mike.say "That's the point."
        $ lavish.flags.sexyswimsuit = True
    else:
        show lavish angry
        lavish.say "Thanks but no thanks [hero.name], I am more classy than that..."
        lavish.say "This is vulgar."
        $ lavish.love -= 5
        $ lavish.sub -= 5
        $ hero.cancel_activity()
    return

label lavish_gift_sexy_dress_male:
    show lavish normal
    "I do the best I can to hide the box that I have behind my back."
    "But I guess there was never any chance Lavish wouldn't see it there."
    "In fact, she spots it the moment that we meet up."
    "I see her eyebrows rise with interest, and she strains to see more."
    "Which, of course, means I have to try even harder to hide it."
    show lavish surprised
    lavish.say "Oh..."
    lavish.say "What's that you have there, [hero.name]?"
    show lavish stuned
    mike.say "Ah..."
    mike.say "It's nothing really, Lavish."
    mike.say "Just a little something I picked up the other day, that's all..."
    "Lavish stops trying to sneak a look at the box."
    show lavish normal
    "Instead she crosses her arms over her chest and smiles."
    "And when she smiles like that, it's hard to resist her, believe me!"
    show lavish happy
    lavish.say "Oh, I see!"
    lavish.say "That's how you want to play things, is it?"
    show lavish normal
    "By now I'm smiling too, enjoying the chance to tease Lavish."
    "I shake my head, trying not to laugh."
    mike.say "I don't know what you mean, Lavish!"
    mike.say "Play what?"
    mike.say "I didn't know this was a game!"
    show lavish whining
    lavish.say "Okay, [hero.name]..."
    lavish.say "PLEASE tell me!"
    lavish.say "Is that a little something for me?"
    show lavish flirt
    "Lavish somehow makes her eyes twinkle as she asks the question."
    "And she looks so innocent, yet so fucking hot at the same time!"
    "There's no way I could ever resist her."
    "I nod and hand the box to her."
    mike.say "Here, Lavish..."
    mike.say "This is for you."
    show lavish happy
    lavish.say "Oh, thank you, [hero.name]!"
    lavish.say "That's so sweet of you..."
    show lavish normal
    play sound [paper_ripping_1, paper_ripping_2]
    "Lavish trails off as she tears the box open then pulls out what's inside."
    show lavish stuned
    "And she's still silent as she holds up the dress I bought her and stares at it."
    mike.say "Well, Lavish..."
    mike.say "What do you think?"
    if lavish.sub >= 30:
        show lavish happy
        lavish.say "What do I think?!?"
        lavish.say "I think I love it, [hero.name]!"
        lavish.say "That's what I think."
        lavish.say "And I love you too for picking it out!"
        show lavish normal
        "The smile spreading across my face is one hundred percent genuine."
        "Just like the feeling of relief sweeping over me too."
        mike.say "You do?"
        mike.say "I'm so glad to hear that, Lavish!"
        show lavish stuned
        "Lavish cocks her head on one side."
        "And she has a puzzled look on her face."
        show lavish surprised
        lavish.say "Why, [hero.name]?"
        lavish.say "Why wouldn't I want a dress like this?"
        show lavish sadsmile
        "I shrug, trying to find a way to express myself."
        mike.say "Well..."
        mike.say "It's hard for a guy to know what to guy a girl, Lavish!"
        mike.say "Sometimes what a guy thinks is sexy..."
        mike.say "Let's just say that a girl might not agree with him!"
        show lavish normal
        "Lavish shakes her head."
        show lavish pleased
        "And she waves a hand, dismissing my concerns."
        show lavish happy
        lavish.say "Well don't you worry about any of that."
        show lavish talkative
        lavish.say "This dress looks pretty good to me."
        lavish.say "And I can't wait to see what it looks like on me."
        lavish.say "That and to see the look on your face when I have it on!"
        show lavish normal
        $ lavish.flags.sexydate = True
        $ lavish.flags.sluttydate = False
    else:
        $ lavish.love -= 4
        show lavish angry
        lavish.say "What do I think?!?"
        lavish.say "I think that you've lost your mind, [hero.name]."
        lavish.say "That's what I think!"
        show lavish upset
        "I shake my head, unable to process Lavish's reaction."
        "I was sure that I'd picked out something she'd like."
        "A dress that she'd look hot in too!"
        mike.say "You...you mean you don't like it?"
        "Lavish shoves the dress back into my open hands."
        "And then she plants one of her hands on her hip."
        "The other she uses to poke a finger at me."
        "And it's worryingly close to my eyeballs!"
        show lavish angry
        lavish.say "No, [hero.name], I don't like it!"
        show lavish whining
        lavish.say "I don't know if you noticed, but I take great care with how I dress."
        lavish.say "A woman from my roots has to do that every day of her life."
        lavish.say "And that's because people are just waiting for an excuse to judge me!"
        lavish.say "So I can't wear something as revealing and slutty as that, can I?"
        show lavish angry
        lavish.say "Because if I did, they'd have a field day!"
        show lavish upset
        "I nod as I shove the dress back into the box."
        "Sure, my feelings are more than a little hurt at Lavish rejecting my gift."
        "But I can see that she has a point."
        mike.say "I'm sorry, Lavish."
        mike.say "I guess I didn't think of that!"
        show lavish sad
        "Lavish's expression softens as I make my apology."
        show lavish sadsmile
        "And she gives me a pained smile."
        show lavish talkative
        lavish.say "That's the problem, [hero.name] - most people don't!"
        lavish.say "But what matters is that you said sorry."
        lavish.say "And I know you well enough to know you mean it too."
        show lavish normal
        $ hero.cancel_activity()
    return

label lavish_gift_slutty_dress_male:
    "Lavish is one of those girls who I can tell spends a lot of time thinking about her appearence."
    "You know, she never looks like she just rolled out of bed and grabbed the nearest thing to wear?"
    "Her outfit always seems to habe been thought out to the very last detail and be totally coordinated."
    "All of which makes the prospect of buying her clothes as a gift a pretty daunting prospect."
    "But the problem is that I just so happened to lay my eyes on a dress that I thought would be perfect for her."
    "One that I was so sure would suit her down to the ground that I had no choice but to buy it on the spot."
    "And now it's in a gift-wrapped box that's hidden behind my back."
    "A box that Lavish seems to have spotted almost as soon as she saw me."
    show lavish talkative
    lavish.say "Hi, [hero.name]..."
    lavish.say "What have you got there?"
    show lavish normal
    "Lavish makes to lean to the side as she greets me."
    "Already angling to see what I have behind my back."
    "So I take a sidestep in the opposite direction to foil her."
    mike.say "What have I got where?"
    mike.say "Why would I have something?"
    mike.say "And even if I did, what would it have to do with you?"
    "I keep my tone light and playful as I evade Lavish's attempts to look behind me."
    "Enjoying the look of pleasant frustration on her face and the thrill of teasing her gently."
    show lavish talkative
    lavish.say "Oh come on!"
    lavish.say "You turn up to meet me with a gift-wrapped box behind your back?"
    lavish.say "Who else am I supposed to think that it's for?"
    show lavish normal
    "I hold out one hand in front of me to keep Lavish at bay."
    "And I use the other to keep the box behind my back."
    mike.say "Okay, okay..."
    mike.say "You win, Lavish..."
    mike.say "I got you a little something."
    "Lavish claps her hands together with excitement as I reveal the box."
    "And her excitement infects me as she plucks it out of my hands."
    "Making me as eager to see her open it as she is to open it herself."
    show lavish happy
    lavish.say "Oh..."
    lavish.say "Thank you, [hero.name]!"
    lavish.say "This is so thoughtful of you..."
    show lavish pleased
    play sound [paper_ripping_1, paper_ripping_2]
    "Lavish's words trail off as she tears through the gift-wrap and opens the box."
    "And her eyes go wide as she pulls out what's been hiding inside all this time."
    show lavish normal
    "It's a dress, unfurling to it's full length as holds it."
    "One that's striking and more than a little shocking in its cut too."
    mike.say "There you go, Lavish..."
    mike.say "I hope you like it?"
    if lavish.sub >= 70:
        "Lavish looks amazed as she shakes her head."
        "Her eyes travelling up and down the length of the dress."
        show lavish happy
        lavish.say "This is..."
        lavish.say "This is...amazing!"
        show lavish pleased
        lavish.say "I would never have picked something like this out for myself."
        mike.say "I know it's a little bit out of your comfort zone, Lavish..."
        mike.say "But I just thought that..."
        "Lavish looks up and waves a hand at me."
        "Cutting off what I was about to say before I can finish."
        show lavish talkative
        lavish.say "No, no, no..."
        lavish.say "I mean that in a good way, [hero.name]!"
        show lavish flirt
        lavish.say "I think that I can pull this off."
        lavish.say "But I wouldn't have had the courage to buy it myself."
        show lavish pleased
        mike.say "So, that's...a good thing?"
        "Lavish nods and then plants a kiss on my cheek."
        "Which staggers me a little, but also reassures me I've done the right thing."
        show lavish flirt
        lavish.say "Of course it is - it reminds me to be brave and try new things."
        lavish.say "And I promise that when I wear this dress..."
        lavish.say "You'll be the first to see me in it!"
        show lavish pleased
        $ lavish.flags.sluttydate = True
        $ lavish.flags.sexydate = False
    else:
        "Lavish looks amazed as she shakes her head."
        "Her eyes travelling up and down the length of the dress."
        show lavish angry
        lavish.say "This is..."
        lavish.say "This is...awful!"
        lavish.say "I would never wear anything this vulgar."
        show lavish upset
        mike.say "I..."
        mike.say "I'm sorry, Lavish..."
        mike.say "I just thought that..."
        "Lavish looks up and waves a hand at me."
        "Cutting off what I was about to say before I can finish."
        show lavish angry
        lavish.say "Well maybe don't try to think in the future!"
        lavish.say "Or at least leave the thinking to me where I'm concerned."
        show lavish upset
        "Lavish hands the dress back to me, still shaking her head."
        show lavish angry
        lavish.say "I hope you kept the receipt for that thing."
        lavish.say "At least you might be able to get store credit."
        show lavish upset
        $ lavish.love -= 10
        $ hero.cancel_activity()
    return

label lavish_gift_butt_plug_male:
    show lavish happy
    lavish.say "Oh, [hero.name], is it for me?"
    "She unwraps the butt plug."
    if lavish.sub <= 50 or not lavish.sexperience:
        show lavish annoyed
        lavish.say "..."
        lavish.say "Keep it... I don't want it so keep it."
        lavish.say "I'm sure you'll have a better use of it than me."
        $ hero.cancel_activity()
    else:
        show lavish normal blush
        lavish.say "It's perfect!"
        show lavish flirt
        lavish.say "Thanks [hero.name], I'll make a good use of it."
        $ lavish.flags.buttplug = True
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
