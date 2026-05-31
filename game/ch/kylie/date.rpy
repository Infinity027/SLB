label kylie_date_intro_valentine_male:
    mike.say "Happy Valentine's day, Kylie!"
    mike.say "I've been waiting for it to come round for ages now."
    mike.say "Because there's nobody else I'd rather have as my valentine!"
    "Kylie smiles and claps her hands together with glee."
    kylie.say "Oh, me too, [hero.name]!"
    kylie.say "I'm crazy about you!"
    kylie.say "Totally crazy!"
    return

label kylie_date_intro_halloween_male:
    mike.say "Hey, Kylie, you look great."
    mike.say "But I just remembered, it's Halloween!"
    "Kylie's eyes go wide at this and she shakes her head."
    kylie.say "Damn it, [hero.name], I forgot too!"
    kylie.say "And I SO wanted to dress as a sexy psycho-killer this year!"
    mike.say "Really, Kylie?"
    "Kylie nods, showing real enthusiasm for the subject."
    kylie.say "Oh yeah, I've got all the stuff at home I need."
    kylie.say "Axes, chainsaw and hockey masks!"
    mike.say "Cool, Kylie - but that's all fake, right?"
    kylie.say "Erm...sure, [hero.name], sure - of course it is!"
    return

label kylie_date_intro_christmas_male:
    kylie.say "Hey, [hero.name] - happy Christmas!"
    "Kylie's smiling from ear to ear, waving at me as she hurries over."
    kylie.say "I'm so excited for our date tonight!"
    mike.say "Me too, Kylie - I love this time of year."
    "Kylie nods eagerly at my words."
    kylie.say "Not as much as me, [hero.name]."
    kylie.say "I've been planning this night for years!"
    return

label kylie_date_intro_birthday_male:
    mike.say "Happy birthday, Kylie!"
    kylie.say "What did you just say to me?!?"
    mike.say "Erm...I just said happy birthday, Kylie."
    mike.say "I mean...today IS your birthday, right?"
    kylie.say "It is, it is - but that's not what's important."
    kylie.say "What's important is that you remembered the date!"
    kylie.say "I always knew that my perfect man would remember the date!"
    mike.say "Erm...okay, Kylie..."
    mike.say "Can we go on our date now?"
    return

label kylie_date_intro_mc_birthday_male:
    kylie.say "HAPPY BIRTHDAY, [hero.name]!"
    mike.say "Whoa...Kylie, you made me jump!"
    kylie.say "Aw, you're so cute when you're scared, [hero.name]!"
    mike.say "Th...thanks, I think..."
    mike.say "And thanks for remembering that it's my birthday too."
    kylie.say "How could I ever forget something that important?"
    kylie.say "I have everything I need to know about you stored away."
    kylie.say "Up here in my head - and I do mean everything..."
    return

label kylie_date_eat_a_burger:
    "Kylie eats her burger with visible enthusiasm, firing looks in my direction the whole time."
    "At one point she spills condiments down her chin, and I honestly think it'll land on her cleavage."
    "But she catches it at the last moment, looking embarrassed at her own clumsiness."
    return

label kylie_date_buy_drink:
    if kylie.is_visibly_pregnant:
        show kylie angry
        $ kylie.love -= 10
        kylie.say "Alcohol?"
        kylie.say "Are you trying to hurt our baby?!?"
        kylie.say "What are you, [hero.name] - insane?!?"
        $ hero.cancel_activity()
        hide kylie
    else:
        "Sipping her drink quickly down, Kylie realises that I've noticed how fast she's drinking."
        "Her cheeks colour a little and she can't help letting out a girlish giggle."
        "She makes a joke then, something throwaway about too much alcohol turning her into a crazy woman."
    return

label kylie_date_play_darts:
    "Even though she claims to be terrible at the game, Kylie still agrees to play darts with me."
    "She hangs on my every word as I give her all the tips that I can think of to improve her game."
    "I honestly have no idea if they work or not, but seeing her blush at the attention she's getting is pretty sweet."
    return

label kylie_date_pub_play_pool:
    "Kylie shrugs and makes a non-committal sound when I say that I want to play pool."
    "But she seems happy to humour me all the same."
    "So the game's passable, if not exactly memorable."
    return

label kylie_date_buy_a_round:
    if kylie.is_visibly_pregnant:
        show kylie angry
        $ kylie.love -= 10
        kylie.say "Alcohol?"
        kylie.say "Are you trying to hurt our baby?!?"
        kylie.say "What are you, [hero.name] - insane?!?"
        $ hero.cancel_activity()
    elif (hero.charm >= 60 - kylie.love and kylie.flags.drinks < 2):
        show drink kylie
        "When I suggest that I buy another round of drinks, Kylie merely shrugs in response."
        "If I'm honest, I'm not sure what to make of that."
        "But as she's not actually said no, I feel bound to keep my word anyway."
        $ game.active_date.score += 5
        if "rebel" in kylie.traits:
            $ game.active_date.score += 5
        $ kylie.set_flag("drinks", 1, "day", mod="+")
        hide drink
    else:
        "I want to pay a round of beers to the whole pub."
        "But Kylie doesn't seem to want to drink, so I refrain from doing so."
        $ hero.cancel_activity()
    return

label kylie_smartphone_booty_call_male:
    mike.say "Hey Kylie, wanna come over for some private time together?"
    kylie.say "You know I wouldn't refuse that for the world!"
    call kylie_fuck_date_male from _call_kylie_fuck_date
    return

label kylie_dance_with:
    "As much as I like getting so up close and personal with Kylie, she seems to enjoy it a hell of a lot more!"
    "She presses herself as close to me as possible, laughing and blushing the entire time."
    "All of this makes me feel like she's realising some kind of dream that she's held in her head for a long time..."
    return

label kylie_date_play_arcade_intro_male:
    "I think I made the right decision asking Kylie to come along to the arcade with me."
    "She hasn't complained once, not like some other girls I've done this with in the past."
    "And she has a look of wonder in her eyes, almost like they're glazed over!"
    "I guess she must like videogames more than she let on."
    mike.say "So, Kylie..."
    mike.say "You like what you see?"
    "Kylie looks around and her gaze falls upon me."
    "But she kind of has to shake her head to actually see me."
    "It's like she's been transported by the flashing lights and constant noise."
    kylie.say "Oh...yeah, [hero.name]..."
    kylie.say "Sorry, I was miles away!"
    kylie.say "This place is great - but what games are we going to play?"
    "Kylie and I both look around for a moment."
    "And then her eyes focus on an old-style arcade cabinet."
    kylie.say "What's that game about?"
    kylie.say "The one with the guy in a hockey mask?"
    mike.say "Oh, that's called 'Slaughter House', Kylie."
    mike.say "And that's the hero - he's called 'Mason'."
    kylie.say "Wait...the crazy-looking guy in the mask is the hero?!?"
    mike.say "Yeah, Kylie - the mask gives him special powers."
    mike.say "And he uses them to rescue his girlfriend."
    kylie.say "That is so COOL!"
    kylie.say "I want to play this one, [hero.name]!"
    mike.say "Are you sure, Kylie?"
    mike.say "It's like super violent, and gory too!"
    kylie.say "Ooh...it sounds perfect!"
    "I think about arguing with Kylie that we should play something else."
    "But then why look a gift horse in the mouth?"
    "The girl I invited to the arcade is actually asking to play a game."
    "So what's the problem if it's a gruesome one?"
    "I pump some coins into the slot, and we take turns playing."
    return

label kylie_date_play_arcade_win_male:
    kylie.say "Ooh...a cleaver!"
    kylie.say "Oh no - zombies!"
    kylie.say "Watch out, [hero.name]!"
    "Kylie's turn at the cabinet doesn't last long."
    "Her enthusiasm for the game isn't a substitute for experience."
    "And she's soon relegated to looking over my shoulder as I hack away."
    "But that's all the better for me, as I'm a veteran at this game."
    "And the more zombies and ghouls I mince, the more Kylie seems to like it!"
    kylie.say "Ooh...ooh!"
    kylie.say "Get that one, [hero.name]!"
    kylie.say "Slice him with the chainsaw!"
    kylie.say "Yes...yes...YES!"
    "By now Kylie is practically clinging to my back."
    "She has her arms wrapped tightly around my waist."
    "And I can feel the weight of her chest pressed against me too!"
    mike.say "Ah, it's no big deal, Kylie!"
    mike.say "This is a pretty old game."
    mike.say "And you just have to get into the swing of it, that's all."
    "Kylie hugs me tighter and I can feel her lips on my neck."
    "I have to admit, she's getting me pretty hot right now!"
    kylie.say "Oh no, [hero.name]..."
    kylie.say "You really know how to swing your weapon around!"
    kylie.say "And I love that in a guy..."
    return

label kylie_date_play_arcade_lose_male:
    mike.say "Oh...oh...grab the cleaver!"
    mike.say "Watch out for the zombies!"
    mike.say "Kylie - behind you!"
    "My turn at the cabinet doesn't last long."
    "And that's because I never played this game that often."
    "But Kylie's enthusiasm seems to translate into a natural talent!"
    "And I watch as she minces her way through ghouls and zombies like a pro."
    kylie.say "Hah!"
    kylie.say "Did you see that, [hero.name]?"
    kylie.say "That one exploded when I shot him!"
    kylie.say "This is AMAZING!"
    "By now I'm looking over Kylie's shoulder."
    "And I end up pressing myself against her too."
    "As she hacks and slashes away, I feel her moving."
    "Kylie's pushing herself into me."
    "Grinding her ass into my groin!"
    kylie.say "Mmm..."
    kylie.say "This is getting me SO hot, [hero.name]."
    kylie.say "I like a big, powerful weapon!"
    kylie.say "Just like the kind I can feel right now..."
    "I swallow hard at this, breathing heavily."
    "Kylie's making me so hard right now!"
    kylie.say "Maybe you can show me how you swing your weapon, [hero.name]?"
    kylie.say "Because it feels pretty big right now!"
    return

label kylie_dick_reactions:
    if not kylie.flags.seendick:
        $ kylie.flags.seendick = 1
        if hero.has_skill("hung"):
            show dick reactions kylie smile
            kylie.say "There it is, there it is."
            kylie.say "It's just how I imagined it would be!"
            mike.say "Is that a good thing?"
            kylie.say "You bet it is."
            show dick reactions kylie tasty
            kylie.say "And I already know it'll feel as good as I imagined too!"
            $ kylie.sub += 10
        elif hero.has_skill("smalldick"):
            show dick reactions kylie smile
            kylie.say "There you are, little guy."
            mike.say "'Little guy'?!?"
            kylie.say "Don't worry - it's just how I imagined it would be."
            show dick reactions kylie tasty
            kylie.say "And I already know it'll feel as good as I imagined it too!"
            $ kylie.sub -= 10
        hide dick reactions
    return

label kylie_halloween_invitation:
    show kylie
    "Who better to invite to the Halloween party than Kylie?"
    "She's funny, she loves me to death and she'll look hot in a costume too."
    "Plus she always gives off kind of a kooky, almost spooky vibe."
    "So Halloween should be something that's right up her alley."
    "That's why I don't waste any time bringing it up when I see her next."
    mike.say "Kylie..."
    mike.say "Have you got any plans for Halloween?"
    kylie.say "Oh, you know, just the usual."
    kylie.say "Roaming the streets, scaring people..."
    mike.say "Oh..."
    mike.say "So you're still into trick or treating?"
    mike.say "Isn't that a little weird for someone your age?"
    "Kylie looks at me with puzzlement on her face for a moment."
    show kylie happy
    "Then she seems to snap out of it with a laugh."
    kylie.say "Trick or treating..."
    show kylie normal
    show fx drop
    kylie.say "Yeah...that's what I meant."
    show kylie happy
    kylie.say "Of course that's what I meant!"
    kylie.say "I guess I'm just a big kid at heart!"
    "Okay, that was a little strange."
    "But I'm sure it was nothing to worry about."
    "Back to the more pressing matter of the party and Kylie being my date."
    mike.say "Whatever, Kylie."
    mike.say "It's just that we're having a Halloween party at my place."
    mike.say "And I wondered if you'd be my date?"
    show kylie normal
    if kylie.yandere < 50:
        "Kylie narrows her eyes."
        "And for a moment I'm sure she's going to say no."
        kylie.say "Yes, [hero.name]."
        $ kylie.love += 1
        kylie.say "I'll come with you to the party."
        mike.say "That's great, Kylie!"
        mike.say "We're going to have a great time!"
        "Kylie smiles at me."
        "But then she cocks her head on one side."
        kylie.say "Tell me something, [hero.name]."
        kylie.say "Are there going to be other girls at the party?"
        "The question seems so strange and out of the blue."
        "Of course there are going to be other girls there."
        "But what's that got to do with Kylie coming along too?"
        mike.say "Erm...yeah, Kylie."
        mike.say "My room-mates are all going to be there."
        mike.say "And I guess they might invite other girls too."
        mike.say "Is that a problem?"
        kylie.say "I just like to know what I have to deal with."
        kylie.say "Other girls will be looking at you all night."
        show kylie happy
        kylie.say "So I need to be able to show them that you're all mine!"
        "I can't help letting out a nervous laugh at this."
        "Kylie said that in such an intense way."
        "If I didn't know her better, I might have been scared!"
        "But I suppose I should be flattered."
        "She honestly thinks I'm that hot!"
        mike.say "Okay, Kylie, whatever you say."
        mike.say "Just try to come up with a great costume."
        mike.say "And don't be afraid to make it a bit sexy, yeah?"
        show kylie normal
        kylie.say "Oh, don't worry, [hero.name]."
        kylie.say "I got an idea that'll slay 'em!"
        $ game.flags.halloween_girl = "kylie"
    else:
        "Kylie gives me a broad smile."
        "One that makes me think she's bound to say yes."
        kylie.say "No, [hero.name]."
        kylie.say "I don't want to come to your party."
        "For a moment I don't know what to say."
        "But then I recover my wits enough to speak."
        mike.say "But why not, Kylie?"
        mike.say "I thought you loved spending time with me?"
        kylie.say "That's right, [hero.name]."
        kylie.say "I love spending time with YOU."
        show kylie sad
        kylie.say "But I don't like sharing you."
        kylie.say "There are going to be other girls at this party, right?"
        mike.say "Uh...yeah, I guess so."
        $ kylie.yandere += 2
        "Kylie begins to pout at this."
        kylie.say "And they'll be looking at you - all night!"
        show kylie angry
        kylie.say "I'd be so jealous, [hero.name]."
        kylie.say "I don't know what I'd do!"
        mike.say "Well...when you put it like that..."
        show kylie normal
        kylie.say "Hey, I know."
        kylie.say "Why don't we have a party together - just you and me?"
        kylie.say "Think about it, [hero.name]."
        show kylie happy
        kylie.say "I promise it'd be killer!"
        "I nod at this, and we drop the subject for now."
        "Just as well, because I need time to think."
        "I did want to go to the party."
        "But the offer of a killer night alone with Kylie..."
        "Well, that sounds like something to die for!"
    return

label kylie_halloween_crash:
    $ game.flags.halloween_girl = "kylie"
    "Who could this be?"
    "Everyone that we invited to the party is already here?"
    scene bg house
    "Opening the door, I guess I should have been more cautious."
    "Especially after the incidents with Jack's sword and Scottie's trident."
    "But I get caught out again as an axe-blade misses my head by an inch."
    mike.say "SHIT!"
    mike.say "What the actual fuck?!?"
    "If I was expecting an apology or explanation, none follows."
    show kylie halloween
    "And instead I'm left staring at a figure in a boilersuit and hockey mask."
    "It's still clutching the axe in it's hands, breathing heavily through the mask."
    "Suddenly I notice the long, flowing blonde hair."
    "That and the fact this psycho-killer also has some killer curves."
    mike.say "K...Kylie?!?"

    show kylie happy
    kylie.say "Hey, [hero.name]!"
    kylie.say "You like my costume?"
    menu:
        "Compliment":
            "I can feel my heart hammering in my chest."
            "The shock is still making me feel a little faint."
            "But the sight of Kylie's face is enough to cure me of all that."
            mike.say "I...I...it's amazing, Kylie!"
            mike.say "You scared the life out of me!"
            $ kylie.love += 1
            "Kylie lets out a delighted giggle."
            "There's an odd look in her eyes, almost a craziness."
            "But I put that down to her being excited for the party."
            show kylie normal
            kylie.say "See, [hero.name] - I knew you'd like it."
            kylie.say "I even used a real axe for authenticity!"
            "As if to prove her point, Kylie proffers the axe again."
            "It's almost close enough to slice off my nose."
            "And I can see that she's not kidding either."
            mike.say "H...how did you know we were having a party, Kylie?"
            mike.say "I don't remember telling you about it."
            kylie.say "Oh...I must have overheard you talking about it."
            kylie.say "And I just assumed you'd want me to come along."
            "Well, she's here now and it'd be pretty harsh to turn her away."
            mike.say "Whatever, Kylie - come on in."
            mike.say "But the axe..."
            mike.say "Ah..."
            mike.say "Maybe we leave that in the hallway, Kylie?"
            mike.say "We don't want anyone getting hacked up by accident."
            mike.say "Do we?"
            show kylie sad
            "Kylie lets out a sigh, but does as I ask."
            kylie.say "Maybe you don't..."
        "Criticize":
            mike.say "God's sake, Kylie."
            mike.say "You scared the life out of me!"
            show kylie sad
            "Kylie looks instantly upset with my response."
            "After all, it's clear that I'm not impressed."
            kylie.say "What's the matter, [hero.name]?"
            kylie.say "Don't you like my costume?"
            mike.say "No, Kylie, it's not the costume."
            mike.say "It's the attacking me with an axe that's the problem!"
            mike.say "I mean, at least it's a foam axe..."
            show fx drop
            "I look Kylie straight in the eye as I say this."
            "And I'm waiting for her to tell me that's what it is."
            mike.say "It's not foam, is it?"
            "Kylie shakes her head."
            kylie.say "I...I wanted my costume to be as authentic as possible!"
            mike.say "H...how did you know we were having a party, Kylie?"
            mike.say "I don't remember telling you about it."
            show kylie normal
            kylie.say "Oh...I must have overheard you talking about it."
            kylie.say "And I just assumed you'd want me to come along."
            "Well, she's here now and it'd be pretty harsh to turn her away."
            mike.say "Whatever, Kylie - come on in."
            mike.say "But the axe..."
            mike.say "Ah..."
            mike.say "Look, just leave the axe in the hallway, okay?"
            mike.say "Then maybe we can have fun without someone actually dying?"
            show kylie angry
            $ kylie.love -= 1
            kylie.say "Ah, okay...okay..."
            kylie.say "Spoilsport..."
    scene bg black with dissolve
    pause 1
    return

label kylie_halloween_arrival:
    scene bg house
    "Opening the door, I guess I should have been more cautious."
    "Especially after the incidents with Jack's sword and Scottie's trident."
    "But I get caught out again as an axe-blade misses my head by an inch."
    mike.say "SHIT!"
    mike.say "What the actual fuck?!?"
    "If I was expecting an apology or explanation, none follows."
    show kylie halloween
    "And instead I'm left staring at a figure in a boilersuit and hockey mask."
    "It's still clutching the axe in it's hands, breathing heavily through the mask."
    "Suddenly I notice the long, flowing blonde hair."
    "That and the fact this psycho-killer also has some killer curves."
    mike.say "K...Kylie?!?"
    "The figure pulls up her mask, revealing Kylie's familiar face."
    show kylie happy
    kylie.say "Hey, [hero.name]!"
    kylie.say "You like my costume?"
    menu:
        "Compliment":
            "I can feel my heart hammering in my chest."
            "The shock is still making me feel a little faint."
            "But the sight of Kylie's face is enough to cure me of all that."
            mike.say "I...I...it's amazing, Kylie!"
            mike.say "You scared the life out of me!"
            $ kylie.love += 1
            "Kylie lets out a delighted giggle."
            "There's an odd look in her eyes, almost a craziness."
            "But I put that down to her being excited for the party."
            show kylie normal
            kylie.say "See, [hero.name] - I knew you'd like it."
            kylie.say "I even used a real axe for authenticity!"
            "As if to prove her point, Kylie proffers the axe again."
            "It's almost close enough to slice off my nose."
            "And I can see that she's not kidding either."
            mike.say "Ah..."
            mike.say "Maybe we leave that in the hallway, Kylie?"
            mike.say "We don't want anyone getting hacked up by accident."
            mike.say "Do we?"
            show kylie sad
            "Kylie lets out a sigh, but does as I ask."
            kylie.say "Maybe you don't..."
        "Criticize":
            mike.say "God's sake, Kylie."
            mike.say "You scared the life out of me!"
            show kylie sad
            "Kylie looks instantly upset with my response."
            "After all, it's clear that I'm not impressed."
            kylie.say "What's the matter, [hero.name]?"
            kylie.say "Don't you like my costume?"
            mike.say "No, Kylie, it's not the costume."
            mike.say "It's the attacking me with an axe that's the problem!"
            mike.say "I mean, at least it's a foam axe..."
            show fx drop
            "I look Kylie straight in the eye as I say this."
            "And I'm waiting for her to tell me that's what it is."
            mike.say "It's not foam, is it?"
            "Kylie shakes her head."
            kylie.say "I...I wanted my costume to be as authentic as possible!"
            mike.say "Look, just leave the axe in the hallway, okay?"
            mike.say "Then maybe we can have fun without someone actually dying?"
            $ kylie.love -= 1
            show kylie angry
            kylie.say "Ah, okay...okay..."
            kylie.say "Spoilsport..."
    scene bg black with dissolve
    pause 1
    return

label kylie_halloween_party:
    $ game.pass_time(2)
    scene bg livingroom
    show kylie halloween sad
    with dissolve
    kylie.say "[hero.name]..."
    kylie.say "I really need to pee!"
    "I'm about to tell Kylie where the bathroom is."
    hide kylie
    show kylie halloween sad at left
    show bree halloween at right
    "But then [bree.name] leans over and beats me too it."
    "I guess she must have overheard the conversation."
    bree.say "It's just down the hall and on the left!"
    show kylie angry
    "Kylie surprises me by not acting on the information."
    "Instead she fixes [bree.name] with a mean stare."
    kylie.say "I know where it is."
    kylie.say "I don't need your help, blondie!"
    show bree surprised
    "[bree.name]'s mouth falls open at Kylie's outburst."
    bree.say "Hey!"
    show bree angry
    bree.say "[hero.name], are you going to let her talk to me like that?!?"
    menu:
        "Back up Kylie":
            mike.say "Ah..."
            mike.say "She doesn't need a guided tour, [bree.name]."
            mike.say "She just needs the bathroom!"
            $ kylie.love += 2
            $ bree.love -= 2
            show kylie normal
            "At this, a triumphant smile spreads across Kylie's face."
            "But [bree.name] frowns and shakes her head at me."
            show bree annoyed
            bree.say "Geez, [hero.name], lighten up!"
            bree.say "I was just trying to help."
            "Kylie lets out a chuckle."
            "And then she shakes her head at [bree.name]."
            kylie.say "Hah..."
            kylie.say "You're so transparent, [bree.name]."
            kylie.say "Trying to impress [hero.name] like that!"
            show bree surprised
            bree.say "Wha...what are you talking about?!?"
            "I make to say something."
            "But Kylie sweeps me away before I can speak."
        "Back up [bree.name]":
            mike.say "Whoa, Kylie!"
            mike.say "There was no need for that."
            mike.say "[bree.name] was just trying to be helpful!"
            $ bree.love += 2
            $ kylie.love -= 2
            $ kylie.yandere += 2
            show bree normal
            show fx anger at left
            "[bree.name] looks instantly reassured by my words."
            "But they have the exact opposite effect on Kylie."
            "She almost snarls at the other girl."
            kylie.say "Yeah, [bree.name]."
            kylie.say "That's what you'd like everyone to think."
            kylie.say "But I know your game."
            kylie.say "And I'm watching you!"
            "I try to change the subject as best I can."
            mike.say "Ah, Kylie..."
            mike.say "Didn't you need the bathroom?"
            show fx anger at left
            kylie.say "I'd rather pee my panties than leave you with her!"
            hide kylie
            hide bree
            "All I can do is take Kylie by the arm and lead her away."
    scene bg black with dissolve
    pause 1
    return

label kylie_halloween_dance:
    $ game.pass_time(2)
    scene bg livingroom
    show sasha halloween
    with dissolve
    $ kylie.yandere += 1
    sasha.say "Hey, [hero.name]."
    sasha.say "We should really dance to this one!"
    "I look around to see Sasha beckoning me to the makeshift dance-floor."
    "The song that's playing is a classic by Metallikea, one we both love."
    "And I really want to accept the invitation."
    "The only problem is that Kylie's still in the bathroom."
    "If I dance with Sasha, I'll be leaving her without her date."
    menu:
        "Refuse":
            mike.say "I'd love to, Sasha."
            mike.say "But I'm waiting for Kylie right now."
            show sasha annoyed
            "Sasha looks disappointed at being turned down."
            "But she nods like she understands all the same."
            show sasha normal
            sasha.say "Okay, whatever."
            hide sasha
            "And with that, she hits the dance-floor alone."
            show kylie halloween angry
            "A moment later, Kylie reappears by my side."
            kylie.say "Why were you talking to that rocker girl?"
            kylie.say "What did she want?"
            mike.say "Sasha was just asking if I wanted to dance, that's all."
            kylie.say "Oh, was she now!"
            mike.say "Yeah, but I told her I was waiting for you."
            $ kylie.yandere -= 1
            $ kylie.love += 2
            show kylie normal
            show fx exclamation
            "At this, Kylie seems to change her tune completely."
            "Before she seemed annoyed with me."
            "But now she it's like she's delighted all of a sudden."
            show kylie happy
            kylie.say "Well, what are we waiting for?"
            kylie.say "Let's go dance!"
            hide kylie
            show dance kylie halloween
            "Kylie almost drags me onto the dance-floor."
            "And from the very start she sticks to me like glue."
            "The whole time she's staring at anyone that comes close."
            "She reminds me of a lioness staring down her rivals."
            "You might think that sounds weird."
            "But for me it's kind of sexy."
            "Like she wants me so badly that she'll fight for me!"
            "By the time we're done, I'm a complete mess."
        "Accept":
            mike.say "That sounds great, Sasha."
            mike.say "Kylie can come join us when she's back."
            $ kylie.yandere += 4
            hide sasha
            show dance sasha halloween
            "Sasha and I hurry onto the dance-floor."
            "And I forget myself for a couple of minutes."
            "It's not like anything that intense happens."
            "We just dance together like the friends we are."
            hide dance
            "But once the song ends, I see Kylie staring at me."
            "And boy, does she look pissed!"
            show kylie halloween angry
            "I hurry over to Kylie."
            "Meanwhile, Sasha goes off in the other direction."
            mike.say "Kylie - there you are!"
            mike.say "Why didn't you come and join us?"
            show fx anger
            $ kylie.love -= 4
            kylie.say "Huh!"
            kylie.say "You looked like you were having enough fun without me."
            mike.say "Don't be like that, Kylie."
            mike.say "Sasha's just a friend, that's all."
            kylie.say "Yeah, [hero.name], that's what she wants you to think!"
            kylie.say "But I've got my eye on her."
            "I try to ignore what Kylie just said."
            "She's obviously overreacting, nothing more than that."
            "Quickly changing the subject, I put it out of my mind."
    scene bg black with dissolve
    pause 1
    return

label kylie_halloween_sex:
    scene bg livingroom
    with dissolve
    "By now the party's been going on for a couple of hours and it's getting late."
    "Things have settled down and the music has become more sedate and relaxed too."
    "Everyone that's still here is either drunk or tired, and also pretty chilled out."
    show kylie halloween happy
    "Well, apart from Kylie, that is."
    "She seems to have found a reserve of almost manic energy from somewhere."
    "And it looks like there's only one thing that she wants to do with it!"
    kylie.say "Come on, [hero.name]."
    kylie.say "We need somewhere to lie down!"
    "Before I can say a much as a word, Kylie almost shoves me through the door."
    "I stagger into what I assumed would be my bedroom, and then shake my head."
    scene bg bedroom2
    show kylie halloween happy
    with fade
    mike.say "Ah, Kylie..."
    mike.say "I think we took a wrong turn."
    mike.say "This is [bree.name]'s bedroom, not mine!"
    "Kylie doesn't seem at all concerned by this."
    "In fact she pretty much ignores it."
    "Instead she pushes me roughly onto [bree.name]'s bed."
    mike.say "Oof..."
    mike.say "Kylie!"
    mike.say "I said this is [bree.name]'s room!"
    show kylie normal
    "By way of an answer, Kylie takes hold of my jaw with one hand."
    "And I don't mean she gently cups my chin either."
    "She holds on so tight that it hurts more than a little too."
    "And then she leans in close to address my protests."
    kylie.say "Of course I know this is Blondie's room, [hero.name]."
    kylie.say "You think I don't know this house like the back of my hand?!?"
    kylie.say "What's going to happen here is this..."
    show kylie blush
    kylie.say "I'm going to fuck you, right here on Blondie's bed."
    kylie.say "And you're going to like it, okay?"
    "I manage to nod, even with Kylie's hand still clutching my jaw."
    mike.say "Okay, Kylie, okay!"
    mike.say "You want to get one over on [bree.name], right?!?"
    kylie.say "That's right."
    show kylie yandere
    kylie.say "I'm going to teach her to have eyes for you!"
    "I nod again, trying to justify what Kylie says in my mind."
    "Maybe she's overreacting, as [bree.name] was just being friendly."
    "But what does that matter if I get a fuck out of it?"
    "I mean, [bree.name] doesn't have to know, does she?"
    "In the time it's taken me to think that, Kylie hasn't been idle."
    "She's already managed to strip off most of my clothes."

    show kylie cowgirl halloween with fade
    "With the hockey mask pulled up to reveal her face, I can see her smile."
    "It's wide and full of that almost crazy energy."
    "The kind that I've come to associate with Kylie."


    "I gasp as Kylie grabs hold of my stiffening cock."
    show kylie cowgirl vaginal
    "And not waiting for permission, she thrusts it between her thighs!"
    mike.say "Whoa..."
    mike.say "Oh god..."
    mike.say "Kylie!"
    "All of Kylie's weight comes down in one go."
    "Which means that my cock is thrust straight into her."
    "She pushes down, grinding herself onto me."
    show kylie cowgirl pleasure
    "And then she begins to ride me, hard and without letting up."
    "I hardly have a moment to savour the sensation."
    "But everything feels amazing!"
    show kylie cowgirl lift
    "Kylie grabs my wrists and guides my hands to her thighs."



    kylie.say "Urgh..."
    kylie.say "You're...mine..."
    show kylie cowgirl orgasm
    kylie.say "All...mine..."
    kylie.say "I won't let take you away!"
    "I shake my head, trying to show Kylie that I agree."
    "Right now I can't imagine being with anyone else."
    "All I can think about is wanting to fuck her forever!"
    kylie.say "That's it..."
    kylie.say "Give it to me..."
    kylie.say "I...want...it...all!"
    "I can't hold on any longer."
    show kylie cowgirl creampie ahegao
    "A second later, I shoot my load into Kylie."
    "She literally screams out loud."
    "And I think someone's bound to come running."
    "That [bree.name] or Sasha will burst in on us."
    "But nobody does, and I can feel the relief almost as intensely as the orgasm!"
    show kylie cowgirl -creampie exhausted dickcum openpussy vaginaldrip pleasure
    "Kylie slides off of me and onto the bed."
    "My cum is already seeping out of her, so I expect her to get up."
    show kylie cowgirl normal
    "But instead, I watch in horror as she rubs her pussy into the sheets."
    mike.say "Kylie!"
    mike.say "What are you doing?!?"
    kylie.say "Just marking my territory, [hero.name]."
    kylie.say "Sending Blondie a message, that's all."
    hide kylie
    "I shake my head, already pulling on my clothes."
    "There's no point getting into a fight over it here and now."
    "Maybe I can wash the sheets before [bree.name] finds out?"
    "I could claim that someone spilled a drink on them."
    "Or maybe [bree.name]'ll be so drunk she won't even notice."
    "After all, there's no evidence it was me."
    "I mean, she's not going to have the cum DNA tested."
    "Is she?"
    $ kylie.sexperience += 1
    $ game.pass_time(1)
    return

label kylie_halloween_crash_sex:
    scene bg livingroom
    with dissolve
    "By now the party's been going on for a couple of hours and it's getting late."
    "Things have settled down and the music has become more sedate and relaxed too."
    "Everyone that's still here is either drunk or tired, and also pretty chilled out."
    show kylie halloween happy
    "Well, apart from Kylie, that is."
    "She seems to have found a reserve of almost manic energy from somewhere."
    "And it looks like there's only one thing that she wants to do with it!"
    kylie.say "Come on, [hero.name]."
    kylie.say "We need somewhere to lie down!"
    "Before I can say a much as a word, Kylie almost shoves me through the door."
    "I stagger into what I assumed would be my bedroom, and then shake my head."
    scene bg bedroom2
    show kylie halloween happy
    mike.say "Ah, Kylie..."
    mike.say "I think we took a wrong turn."
    mike.say "This is [bree.name]'s bedroom, not mine!"
    "Kylie doesn't seem at all concerned by this."
    "In fact she pretty much ignores it."
    "Instead she pushes me roughly onto [bree.name]'s bed."
    mike.say "Oof..."
    mike.say "Kylie!"
    mike.say "I said this is [bree.name]'s room!"
    show kylie normal
    "By way of an answer, Kylie takes hold of my jaw with one hand."
    "And I don't mean she gently cups my chin either."
    "She holds on so tight that it hurts more than a little too."
    "And then she leans in close to address my protests."
    kylie.say "Of course I know this is Blondie's room, [hero.name]."
    kylie.say "You think I don't know this house like the back of my hand?!?"
    kylie.say "What's going to happen here is this..."
    show kylie blush
    kylie.say "I'm going to fuck you, right here on Blondie's bed."
    kylie.say "And you're going to like it, okay?"
    "I manage to nod, even with Kylie's hand still clutching my jaw."
    mike.say "Okay, Kylie, okay!"
    mike.say "You want to get one over on [bree.name], right?!?"
    kylie.say "That's right."
    show kylie yandere
    kylie.say "I'm going to teach her to have eyes for you!"
    "I nod again, trying to justify what Kylie says in my mind."
    "Maybe she's overreacting, as [bree.name] was just being friendly."
    "But what does that matter if I get a fuck out of it?"
    "I mean, [bree.name] doesn't have to know, does she?"
    "In the time it's taken me to think that, Kylie hasn't been idle."
    "She's already managed to strip off most of my clothes."

    show kylie cowgirl halloween onface emotionless


    "I gasp as Kylie grabs hold of my stiffening cock."
    show kylie cowgirl vaginal
    "And not waiting for permission, she thrusts it between her thighs!"
    mike.say "Whoa..."
    mike.say "Oh god..."
    mike.say "Kylie!"
    "All of Kylie's weight comes down in one go."
    "Which means that my cock is thrust straight into her."
    "She pushes down, grinding herself onto me."
    show kylie cowgirl pleasure
    "And then she begins to ride me, hard and without letting up."
    "I hardly have a moment to savour the sensation."
    "But everything feels amazing!"
    show kylie cowgirl lift
    "Kylie grabs my wrists and guides my hands to her thighs."



    kylie.say "Urgh..."
    kylie.say "You're...mine..."
    show kylie cowgirl orgasm
    kylie.say "All...mine..."
    kylie.say "I won't let take you away!"
    "I shake my head, trying to show Kylie that I agree."
    "Right now I can't imagine being with anyone else."
    "All I can think about is wanting to fuck her forever!"
    kylie.say "That's it..."
    kylie.say "Give it to me..."
    kylie.say "I...want...it...all!"
    "I can't hold on any longer."
    show kylie cowgirl creampie ahegao blush
    "A second later, I shoot my load into Kylie."
    "She literally screams out loud."
    "And I think someone's bound to come running."
    "That [bree.name] or Sasha will burst in on us."
    "But nobody does, and I can feel the relief almost as intensely as the orgasm!"
    show kylie cowgirl -creampie exhausted dickcum openpussy vaginaldrip pleasure
    "Kylie slides off of me and onto the bed."
    "My cum is already seeping out of her, so I expect her to get up."
    show kylie cowgirl normal
    "But instead, I watch in horror as she rubs her pussy into the sheets."
    mike.say "Kylie!"
    mike.say "What are you doing?!?"
    kylie.say "Just marking my territory, [hero.name]."
    kylie.say "Sending Blondie a message, that's all."
    hide kylie
    "I shake my head, already pulling on my clothes."
    "There's no point getting into a fight over it here and now."
    "Maybe I can wash the sheets before [bree.name] finds out?"
    "I could claim that someone spilled a drink on them."
    "Or maybe [bree.name]'ll be so drunk she won't even notice."
    "After all, there's no evidence it was me."
    "I mean, she's not going to have the cum DNA tested."
    "Is she?"
    $ kylie.sexperience += 1
    $ game.pass_time(1)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
