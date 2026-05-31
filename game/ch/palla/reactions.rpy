label palla_ice_cream_reaction_male:
    mike.say "I'm WAY too hot, Palla - let's grab some ice cream!"
    palla.say "Hmm...me too - let's go."
    "At the ice cream stall, I buy myself a cone with a couple of different scoops."
    "But Palla orders herself a pretty fancy sundae that comes with a long spoon."
    mike.say "Wow, Palla - that thing looks really fancy!"
    palla.say "Mmm...it's a little more sophisticated than your average ice cream!"
    "I watch, my mouth hanging open as Palla delicately spoons ice cream into her mouth."
    "She's making me feel hungrier with every spoonful."
    "But let's just say it's not the ice cream that I'm craving!"
    return

label palla_ask_phone_male:
    mike.say "Can I have your number?"
    if palla.love < 10 or not hero.charm >= 40 - palla.love:
        if palla.flags.storeanal:
            palla.say "After what you did? I don't think I like you that much."
        else:
            palla.say "Not a chance!"
    else:
        $ hero.smartphone_contacts.append("palla")
        palla.say "I guess."
    return

label palla_ask_birthday_male:
    mike.say "Erm..."
    mike.say "Palla..."
    mike.say "When is your birthday?"
    if hero.charm >= 40 - palla.love:
        show palla happy
        $ palla.flags.birthdayknown = True
        palla.say "It's pretty easy to remember, [hero.name]."
        palla.say "It's Fall 14."
        palla.say "Just around the time the Autumn collections are out!"
    else:
        show palla annoyed
        $ palla.sub -= 1
        $ palla.love -= 1
        palla.say "What are you trying to say, [hero.name]?"
        palla.say "You think I'm too old to pull off this outfit?!?"
        palla.say "That's pretty mean of you!"
    return

label palla_offer_a_drink_male:
    mike.say "Palla, would you like a drink?"
    mike.say "I'm just going to the bar and I wondered..."
    "Almost the second the words are out of my mouth, Palla turns to face me."
    if palla.is_visibly_pregnant:
        show palla angry
        $ palla.love -= 10
        palla.say "Erm...don't you remember getting me pregnant, [hero.name]?"
        palla.say "Because I certainly do!"
        palla.say "It's basically your fault I can't do anything fun."
        palla.say "At least not while I have your kid inside of me!"
        $ hero.cancel_activity()
        hide palla
    elif (hero.charm >= 60 - palla.love and palla.flags.drinks < 2) or date_girl == palla:
        show palla happy
        palla.say "Hmm..."
        palla.say "Okay, [hero.name], okay."
        palla.say "See if they can whip me up a 'Pornstar Martini'."
        palla.say "Or if they even know what that is!"
        hide palla
        show drink palla
        if palla.love <= 25:
            $ palla.love += 1
        elif date_girl == palla and game.active_date:
            $ game.active_date.score += 5
        call expression palla.get_chat from _call_expression_259
        hide drink palla
        $ palla.set_flag("drinks", 1, "day", mod="+")
    else:
        show palla annoyed
        palla.say "Honestly, [hero.name], don't bother."
        palla.say "I doubt they've even have heard of what I'd order."
        $ hero.cancel_activity()
        hide palla
    return

label palla_slap_ass_intro_male:
    "I don't know how she does it, I really don't."
    "But somehow Palla always manages to dress in just such a way."
    "And it's a way that makes her ass look almost better than when it's naked!"
    "The way it moves, the shape of it under her clothes..."
    "I can't resist giving it a cheeky slap!"
    return

label palla_slap_ass_happy_male:
    "Palla stops in her tracks, letting out a yelp of surprise."
    "She turns on her heel and plants her hands on her hips."
    palla.say "[hero.name], you have one chance to tell me the truth."
    palla.say "Did you just slap me on the ass?!?"
    "There doesn't seem to be any point denying it."
    "So I just shrug my shoulders and nod."
    "Palla seems to consider my confession for a moment."
    "And then she shrugs too."
    palla.say "Well, I suppose you ARE only human."
    palla.say "How could you hope to resist?"
    return

label palla_slap_ass_angry_male:
    "Palla stops in her tracks, letting out a yelp of surprise."
    "She turns on her heel and plants her hands on her hips."
    palla.say "[hero.name], you have one chance to tell me the truth."
    palla.say "Did you just slap me on the ass?!?"
    "There doesn't seem to be any point denying it."
    "So I just shrug my shoulders and nod."
    "Palla seems to consider my confession for a moment."
    "And then she shakes her head."
    palla.say "I'm going to let you off this once, [hero.name]."
    palla.say "But I'd advise you don't do it again."
    return

label palla_breakup_male:
    show palla
    "I hate having to do this, but I don't see any way out of it."
    "Sure, I could just say nothing, keep lying to myself and Palla alike."
    "But how long am I seriously going to be able to keep that up?"
    "No, I need to do this now and deal with the potential fallout."
    "Oops...did I say potential?"
    "I meant inevitable..."
    mike.say "Palla..."
    mike.say "Can we talk?"
    "Palla raises an eyebrow at the question."
    "And probably also at the tone in which I say it."
    palla.say "Hmm..."
    palla.say "I suppose so, [hero.name]."
    palla.say "But this doesn't sound good!"
    "At first, all I can manage in response is a weak grin."
    "But then I gather all of my resolve and come out with it."
    mike.say "I...I don't think this is working out, Palla."
    mike.say "You're a great girl and all that..."
    mike.say "But I think we should break up."
    show palla annoyed
    "Palla blinks and takes a step backwards."
    "I mean, she reacts almost like she's been slapped!"
    "Her mouth opens and closes, but it takes a while for words to emerge."
    palla.say "N...no way!"
    palla.say "You can't be saying that, [hero.name]."
    palla.say "Not to me!"
    mike.say "Ah...yeah, Palla."
    mike.say "I kind of am!"
    "Palla shakes her head at this."
    "As if she's trying to throw off the connotations that come with it."
    palla.say "No, [hero.name], you don't understand - how could you?"
    palla.say "Someone like you doesn't get to dump someone like me."
    palla.say "That's just not how it happens!"
    mike.say "It isn't?"
    palla.say "Of course it isn't!"
    palla.say "The reality is that you probably think you're not good enough for me."
    palla.say "But you can't admit it to yourself, so you're pretending to dump me instead."
    mike.say "Erm...I don't know about that, Palla..."
    "Palla waves away my concerns, beginning to look annoyed."
    palla.say "It doesn't matter what you think."
    palla.say "I'm obviously too good for you, [hero.name]."
    palla.say "So we're over, and I never want to see you again!"
    "I nod and then watch as Palla turns to walk away."
    "And it's only then that a thought occurs to me."
    "Wasn't I supposed to be the one dumping her?!?"
    return

label palla_go_steady_intro_male:
    mike.say "I feel like we're really connecting, Palla."
    mike.say "Like our relationship is on another level."
    mike.say "And that's why I think we should go steady!"
    return

label palla_go_steady_yes_male:
    if "palla_event_07b" not in DONE:
        palla.say "I'm not going to be anybody's girlfriend. I'm not a possession, an object, a thing you can use."
        if palla.sexperience >= 3:
            palla.say "Well, at least, fine you can use me, but not like {b}that{/b}."
    else:
        if game.week_day % 2 == 0:
            palla.say "You know I never thought I'd say this, [hero.name]."
            palla.say "But you're right - we should make it official."
            palla.say "You've really grown on me - like a fungus!"
        else:
            palla.say "I thought you just wanted to be friends?"
            mike.say "Maybe I changed my mind."
            palla.say "Look, I know I've got great tits, but I didn't think you were the type."
            mike.say "It's not about your tits."
            palla.say "Really?"
            mike.say "It's not {b}just{/b} about your tits."
            palla.say "Fine. Convince me and I'll think about it."
            mike.say "Look. You're crazy and at first I thought I was going to hate that, or that it'd be fun to slap some sane into you."
            palla.say "Oh yes, you're so very good at this flattery stuff."
            mike.say "Let me finish!"
            "Palla clasps her hands together in front of her and makes a show of paying attention."
            mike.say "Damn it, Palla, I'm in love with you and I want something...more. More than just friends."
            palla.say "And here I thought romance was dead."
            palla.say "Oh wait, it is."
            mike.say "Ugh, maybe I {b}don't{/b} want you to be my girlfriend."
            palla.say "Now that's what I've been trying to tell you."
            mike.say "Why, why do you have to be such a bitch when I'm trying to be nice?"
            palla.say "Because men suck, dude."
            mike.say "So I suck?"
            palla.say "You can't help it, it's genetic."
            mike.say "Then why are you with me at all?"
            palla.say "Because I can't help it. I'm attracted to assholes."
            mike.say "You're certainly attracted to {b}your{/b} asshole."
            palla.say "Does that make you my asshole then?"
            mike.say "I thought you said you didn't want to be a girlfriend?"
            palla.say "Oh, very clever of you."
            mike.say "So if you're attracted to assholes why the hell won't you just be this asshole's girlfriend?"
            palla.say "Because once I'm your girlfriend, this...thing we have changes."
            mike.say "And?"
            palla.say "Because I don't get to be happy often, and I don't want to ruin it."
            mike.say "Oh fuck me, that's your only excuse? You think the word will ruin what we have? That doesn't even make sense."
            palla.say "Jesus Christ on a crutch, [hero.name]! Will you shut the fuck up if I say yes?"
            mike.say "I was going to say yes, but probably not. But I will fuck you extra hard next chance I get."
            palla.say "Fine, yes, I'll be your, ugh, girlfriend. But don't think that means I'm not still dating other men if I find someone I like."
            mike.say "That's fine, I know you'll always be in my bed when it matters."
            palla.say "Oh, so sure of yourself?"
            mike.say "Yeah, I know you can't get enough of me."
            palla.say "Sounds like a challenge!"
    return

label palla_go_steady_no_male:
    if game.week_day % 2 == 0:
        palla.say "Hmm..."
        palla.say "Don't take this the wrong way, [hero.name]."
        palla.say "But we're SO not on the same page about this!"
    else:
        palla.say "Ugh, why in the world would I want {b}that{/b}!"
    return

label palla_pet_intro_male:
    "I pat Palla on the head before I give it a second thought."
    "But the moment I do so, I begin to wonder what possessed me."
    "That and how she's going to react!"
    return

label palla_pet_happy_male:
    palla.say "Oh..."
    palla.say "Oh...I..."
    palla.say "Thank you, [hero.name]!"
    palla.say "What an old-fashioned compliment!"
    return

label palla_pet_annoyed_male:
    palla.say "I'm going to forget you just did that, [hero.name]."
    palla.say "And neither of us is going to mention it ever again."
    palla.say "You understand me?"
    return

label palla_massage_intro_male:
    mike.say "You look like you're holding your head funny, Palla."
    mike.say "Are you feeling okay, like in terms of your muscles?"
    mike.say "Because I can give you a massage if you like?"
    return

label palla_massage_accept_male:
    palla.say "Urgh..."
    palla.say "So you noticed?"
    palla.say "I...I suppose a massage would be quite nice..."
    return

label palla_massage_refuse_male:
    palla.say "There's nothing wrong with me at all, [hero.name]."
    palla.say "You're just not used to being around someone with poise."
    palla.say "Ouch...it...it just looks painful, that's all!"
    return

label palla_piercing_nipples_reaction_male:
    palla.say "Hmm..."
    palla.say "I never saw the possibilities of a piercing my nipples before."
    palla.say "But it's like I've got a whole new part of me to accessorise!"
    palla.say "Thanks for talking me into doing this, [hero.name]."
    return

label palla_piercing_navel_reaction_male:
    palla.say "This looks WAY better than I ever thought it would, [hero.name]."
    palla.say "You were right on trend to suggest I have it done."
    palla.say "I guess I should be thanking you."
    return

label palla_piercing_clit_reaction_male:
    palla.say "Oh...oh wow..."
    palla.say "This feels super weird, [hero.name]!"
    palla.say "But it's a good kind of weird you know?"
    palla.say "Like I have an exclusive new accessory that nobody else knows about!"
    return

label palla_piercing_head_reaction_male:
    palla.say "I wasn't sure at first, but I think I like the feel of this."
    palla.say "And they had a whole lot of different piercings that I can try too."
    palla.say "I'm sure I can style this thing like anything else I wear."
    palla.say "Thanks, [hero.name], this was a great idea."
    return

label palla_piercing_nose_reaction_male:
    palla.say "Hmm...I think I can pull this one off."
    palla.say "In fact, why am I being so humble?"
    palla.say "I KNOW I can pull this off!"
    palla.say "Good call, [hero.name]!"
    return

label palla_movie_disliked_reaction_male:
    palla.say "What a waste of time that was - awful from start to finish!"
    return

label palla_movie_indifferent_reaction_male:
    palla.say "So boring - I'd could have slept through the whole thing!"
    return

label palla_movie_liked_reaction_male:
    palla.say "I hate to say it...but that was a GREAT movie!"
    return

label palla_belly_kiss_male:
    show palla surprised at center, zoomAt(1.25, (640, 880))
    mike.say "Palla..."
    mike.say "Just come over here..."
    mike.say "And let me..."
    show palla at center, traveling(2.0, 1.0, (640, 980))
    "Palla watches on with obvious interest as I get down on one knee in front of her."
    "And her eyes go wider still when I begin to lift up her top and reveal the curve of her belly."
    show palla angry
    palla.say "[hero.name]…"
    palla.say "What are you doing?"
    palla.say "Stop that right now...people will see how fat I am!"
    show palla annoyed
    "Pallas trying her best to stop me uncovering her belly."
    "But the moment that I see skin, I plant a kiss on it."
    "And it seems that the contact is what makes the difference."
    "Because I can already feel Palla beginning to stop struggling against me."
    show palla normal
    "In fact she actually lets me uncover more of her belly than before."
    "Which means that I instantly step things up and kiss it all the more."
    "By the time I've made a couple of circuits. Palla's even relaxing."
    "I know that because I can hear her sighing and cooing to herself."
    "But I don't want to make her put herself on display for too long."
    "So I make a point of wrapping things up and making to stand."
    "Though what really comes as a surprise is what happens next."
    "When I start to pull Palla's top back down, she stops me."
    show palla happy
    palla.say "Oh..."
    palla.say "No...no..."
    palla.say "Maybe just leave it out for a little longer?"
    "I can feel the way Palla's pressing her belly against me right now."
    "Like she's really enjoying the sensation of me touching it."
    "And she doesn't want that to stop any time soon."
    "I nod and take Palla's belly in my hands, holding it gently."
    "It feels so pleasant to be caressing it like this."
    "Knowing that our unborn child is growing in there."
    "As well as the feeling of Palla warming to the knowledge as well."
    return

label palla_belly_caress_male:
    show palla annoyed at center, zoomAt(1.25, (640, 880))
    palla.say "Urgh..."
    palla.say "How on earth am I supposed to take a selfie like this?!?"
    show palla normal
    "I look up to see Palla holding her phone at arms length."
    "At the same time she looks desperately frustrated too."
    "Like she's totally forgotten how to pull off such a simple task."
    mike.say "Just make sure you're in shot, Palla..."
    mike.say "Then push the button and take the photo!"
    mike.say "I never thought you'd forget something as simple as that."
    show palla angry at center, traveling(1.5, 0.3, (640, 1040))
    "Palla turns to regard me as I walk over to her."
    "And the look in her eyes almost hits me like a slap around the cheeks."
    show palla vangry
    palla.say "What are you talking about, [hero.name]?"
    palla.say "I know how to take a damn selfie."
    palla.say "I just don't know how to work this thing into it!"
    show palla angry
    "Palla underlines her point by shoving her belly at me."
    "And it's not hard to begin seeing her point."
    "She'd need something like a selfie-stick to get all of it in!"
    mike.say "Erm..."
    mike.say "Maybe you need to look at it in a different way, Palla?"
    show palla surprised
    palla.say "You mean take the shot from another angle?"
    palla.say "One that hides the whole thing?"
    show palla normal
    "I shake my head as I reach out and put a hand on Palla's belly."
    mike.say "Ah, no..."
    mike.say "I wasn't so much meaning cut the bump out..."
    mike.say "More like make it a central part of the shot."
    "All the time I'm saying this, I'm taking the chance to caress Palla's belly."
    "And whether she seems to notice it or not, this does appear to improve her mood."
    show palla happy
    "Because she begins to smile and put her hands atop mine."
    show palla talkative
    palla.say "You know, you might be onto something there..."
    palla.say "Pregnant could be a radical new look for this season..."
    palla.say "I have to look through my wardrobe."
    palla.say "Find outfits that just scream 'motherhood'!"
    return

label palla_belly_listen_male:
    show palla normal at center, zoomAt(1.25, (640, 880))
    mike.say "Hold still a minute, Palla..."
    mike.say "I just want to try something..."
    show palla at center, traveling(2.0, 1.0, (640, 980))
    "Palla does as I ask, letting me lean in close to her swollen belly."
    "But I get the feeling it's more on account of surprise than anything else."
    "And I know that the questions are about to start coming, thick and fast."
    show palla surprised
    palla.say "What..."
    palla.say "What are you doing down there?"
    show palla vangry
    palla.say "I have a right to know your intentions towards my body!"
    show palla annoyed
    "I wave a hand in an attempt to get Palla to shut up."
    "Because I have an ear pressed to her belly."
    "And I'm trying to hear what's going on inside of it."
    mike.say "Shhh!"
    mike.say "I want to see if I can hear the baby."
    show palla vangry
    palla.say "Don't you dare shush me!"
    palla.say "I will not be used like a goddamn telephone!"
    show palla angry
    "I'm not really listening to Palla as she complains."
    "Because I can already hear the baby moving inside of her."
    "Sure, it's nothing more than the sound of something moving in liquid."
    "Like a fish or larger creature swimming through water."
    "But what makes the difference is the fact I know it's my kid doing it."
    mike.say "Whoa..."
    mike.say "I...I can hear them!"
    "The moment I speak the words, something in Palla seems to change."
    "Before she was being petulant and throwing a tantrum like a kid."
    "But now that seems to have been replaced by the wonder of a child."
    show palla surprised
    palla.say "You can?"
    palla.say "You can actually hear the baby?"
    palla.say "What's it sound like?"
    palla.say "What's it doing in there?"
    palla.say "Is there any way I can hear it too?!?"
    show palla normal
    "I do the best I can to keep on listening as Palla bombards me with questions."
    "Still following the motions of the baby that's growing inside of her stomach."
    "Sure, I'm going too have to answer then eventually."
    "But for the moment I don't want to do anything but listen."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
