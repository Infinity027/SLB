init python:
    Event(**{
    "name": "home_xmas_party_planned",
    "label": "home_xmas_party_planned",
    "priority": 1000,
    "conditions": [
        IsSeason(3),
        'game.calendar.day_of_season == 18',
        HeroTarget(
            IsGender("male")
            ),
        PersonTarget(bree,
            Not(IsHidden()),
            ),
        PersonTarget(sasha,
            Not(IsHidden()),
            ),
        ],
    "once_day": True,
    "do_once": False
    })

    Event(**{
    "name": "home_xmas_party_cancelled",
    "label": "home_xmas_party_cancelled",
    "priority": 1000,
    "conditions": [
        IsSeason(3),
        IsLabelAppointmentPlanned("xmas_party_snacks"),
        HeroTarget(
            IsGender("male")
            ),
        Or(
            PersonTarget(bree,
                Or(
                    IsHidden(),
                    IsGone(),
                    ),
                ),
            PersonTarget(sasha,
                Or(
                    IsHidden(),
                    IsGone(),
                    ),
                ),
            )
        ],
    "do_once": False
    })

label home_xmas_party_planned:
    $ renpy.dynamic("home_xmas_party", "appointment")
    $ home_xmas_party = game.calendar.get_future_days_played("christmaseve")
    if Harem.find_by_name("home"):
        $ party_participants = list({"bree", "sasha"} | set(Harem.find_by_name("home").active_members))
    else:
        $ party_participants = ["bree", "sasha"]
    $ appointment = LabelAppointment((18, 21), party_participants, "Home Christmas Party", "xmas_party_snacks", "home_xmas_party_missed")
    $ hero.calendar.add(home_xmas_party, appointment)
    return

label home_xmas_party_missed:
    "Shit, I missed the Christmas home party. The girls are going to be mad."
    $ bree.love -= 4
    $ sasha.love -= 4
    return

label home_xmas_party_cancelled:
    if bree.hidden and sasha.hidden:
        "[bree.name] and Sasha are not available this Christmas."
    if bree.hidden:
        "[bree.name] is not available this Christmas."
    if sasha.hidden:
        "Sasha is not available this Christmas."
    "I have to cancel the party."
    $ hero.calendar.find_and_remove(label="xmas_party_snacks")
    return

label xmas_party_snacks(appointment=None):
    if renpy.has_label("christmas_achievement_1") and not game.flags.cheat:
        call christmas_achievement_1 from _call_christmas_achievement_1
    scene bg livingroom with fade


    $ xmas_party_appetiser = "mike"
    if Harem.find(samantha, name='home') and not sasha.hidden:
        $ xmas_party_appetiser = ["samantha", "sasha"][renpy.random.randint(0, 1)]
    elif samantha.flags.schedule == "harem":
        $ xmas_party_appetiser = "samantha"
    elif not sasha.hidden:
        $ xmas_party_appetiser = "sasha"

    "Normally the festive season would see everyone disappearing off to visit their relatives."
    "So either the house ends up being empty, or else someone's here all on their own at Christmas."
    "I know the latter sounds like it sucks, but it's happened to me before, and it's quite relaxing!"
    "But this year it just so happens that everyone is staying put, and so we've decided to have a party together."
    "Well, I say we decided, but I don't recall there ever being a house meeting or a vote of any kind."
    "People just kind of started talking about it, and then it snowballed from there."
    "One person volunteered to cook a course for dinner, then another the next one."
    show xmas snacks mikemc
    if not bree.hidden:
        show xmas snacks bree
    if not sasha.hidden:
        show xmas snacks sasha
        if xmas_party_appetiser == 'sasha':
            show xmas snacks industrial mikemc_disgust samantha_disgust
    if Person.find("lexi") and lexi.flags.schedule == "harem":
        show xmas snacks lexi
    if not minami.hidden:
        show xmas snacks minami
    if samantha.flags.schedule == "harem":
        show xmas snacks samantha
        if xmas_party_appetiser == 'samantha':
            show xmas snacks sasha_disgust
    with fade
    "And now here we are, gathering round the table to see what's been cooked up for us!"
    "One by one, everyone comes down from their rooms, drawn by the smell of the food."
    if not bree.hidden:
        bree.say "Ooh - I wonder what we're having to start off with?"
    if Person.find("lexi") and lexi.flags.schedule == "harem":
        lexi.say "Where are the plates?"
        lexi.say "I'm frikin' starving!"
    if not minami.hidden:
        minami.say "This is SO much better than back home, big bro."
        minami.say "Mom and Dad aren't here to make us say grace!"
    if samantha.flags.schedule == "harem" and not xmas_party_appetiser == 'samantha':
        samantha.say "Hmm...this looks...interesting!"
    if not sasha.hidden and not xmas_party_appetiser == 'sasha':
        sasha.say "Hmm...that all looks very...wholesome!"
    if xmas_party_appetiser == 'samantha':
        "I didn't know what to expect, but the food spread out before me looks amazing."
        "Sam insisted on being the one to prepare the appetizers, and she's outdone herself!"
        "Everything looks like it was handmade with an eye for detail from natural ingredients."
        "I honestly can't remember the last time I saw food that looked this healthy."
        "And by that I don't mean that it looks like some kind of weird health food either."
        "The whole spread looks and smells like it's going to taste amazing!"
        if samantha.flags.nickname == "cupcake":
            mike.say "Wow, Cupcake!"
        else:
            mike.say "Wow, Sam!"
        mike.say "This looks incredible!"
        mike.say "Where did you learn to cook like this?"
        "Sam beams at me, enjoying the praise that I'm heaping on her."
        "She looks every bit the domestic goddess as she serves up the fruit of her labours."
        samantha.say "Oh, it's nothing special really!"
        samantha.say "Just some recipes my grandma handed down to me."
        samantha.say "And some of my own creations thrown in for good measure too."
        samantha.say "When you use all natural ingredients, you can do this with ease!"
        "I look around the table, seeing that everyone has a plate."
        "Not everyone seems to be listening to Sam as they shovel food into their faces."
        "But I make a point of nodding to everything that she says."
        if not bree.hidden:
            bree.say "Watch out - these things are spicy!"
        if Person.find("lexi") and lexi.flags.schedule == "harem":
            lexi.say "Which are the spicy ones?"
            lexi.say "Gimmie some more of those!"
        if not minami.hidden:
            minami.say "Mmm...these are great, Sam!"
            minami.say "Can I have another helping, please?"
        if not sasha.hidden:
            sasha.say "I think I'm allergic to like ninety percent of this stuff!"
    elif xmas_party_appetiser == 'sasha':
        "Sasha did some pretty big talking when she took on the task of cooking the appetisers."
        "She told us that not only could she handle it, but that she could do it in record time too."
        "And as soon as I take in the food on offer, I can see why she made that claim."
        "Sure, there's a lot of stuff on the table, and it all looks perfectly edible."
        "But I can't see one thing that's not come out of a tin or a packet!"
        "Processed meat, processed cheese and every form of fat known to humankind!"
        "What did she do - just sweep stuff off the supermarket shelf and into her shopping cart?!?"
        mike.say "Ah..."
        mike.say "Wow, Sasha..."
        mike.say "I really don't know what to say!"
        "Sasha seems to mistake my surprise for amazement."
        "She grins and jabs me in the ribs with her elbow."
        sasha.say "You see - I can do the domestic goddess thing too!"
        sasha.say "All you have to do is not be too fussy about it."
        sasha.say "This stuff is WAY cheaper than all the organic crap."
        sasha.say "And most of it'd survive a nuclear blast too!"
        "Speaking of nuclear blasts, that reminds me."
        "I should try to be first in the queue for the bathroom after we've eaten all this junk!"
        "I look around the table, seeing that everyone has a plate."
        "Not everyone seems to be listening to Sasha as they shovel food into their faces."
        if not bree.hidden:
            bree.say "Whoa...that's mega hot!"
            bree.say "Normally I only snack on this kind of stuff when I'm having a marathon on the Zbox!"
        if Person.find("lexi") and lexi.flags.schedule == "harem":
            lexi.say "Yeah, this is more like it!"
            lexi.say "I used to live on this stuff back at the trailer-park!"
        if not minami.hidden:
            minami.say "Oh wow, big bro!"
            minami.say "Mom and Dad would flip if they saw all this stuff!"
        if samantha.flags.schedule == "harem":
            samantha.say "Oh dear...oh dear, oh dear!"
            samantha.say "How many additives are there in all of this?"
    else:
        "It feels so weird that Sasha's not here with us today."
        "I keep thinking that she's going to walk in any moment."
        "And I can almost hear her making sarcastic jokes about all of this."
        "You know, like making fun of [bree.name] and me for being too into it all."
        "I guess we're just going to have to raise a glass to her memory."
    scene bg black with dissolve
    pause 1

label xmas_party_turkey:
    $ game.pass_time(1)
    scene bg livingroom
    call xmas_party_hh_display from _call_xmas_party_hh_display
    with dissolve


    $ xmas_party_cook = "mike"
    if Person.find("lexi") and lexi.flags.schedule == "harem" and not bree.hidden:
        $ xmas_party_cook = ["bree", "lexi"][renpy.random.randint(0, 1)]
    elif Person.find("lexi") and lexi.flags.schedule == "harem":
        $ xmas_party_cook = "lexi"
    elif not bree.hidden:
        $ xmas_party_cook = "bree"

    "Once the first course is over and all the appetisers have been devoured, it's time for the main event!"
    "By which, of course, I mean the main course of our house festive meal - the turkey!"
    "Nobody held back when it came to the starters, but none of them seem to be close to full yet."
    "In fact, everyone looks like they're anticipating the arrival of the turkey with baited breath!"
    "Well, in a figurative sense at least - none of my housemates are ever lost for words."
    if not bree.hidden and not xmas_party_cook == 'bree':
        show bree happy at startle
        bree.say "Hmm...that smells pretty good, Lexi!"
        bree.say "But you know what they say - the proof of the pudding is in the eating."
        show bree normal
        bree.say "Well...it's in the turkey...you know what I mean!"
    if Person.find("lexi") and lexi.flags.schedule == "harem" and not xmas_party_cook == 'lexi':
        show lexi sad
        lexi.say "Wow...that smells...erm...."
        lexi.say "Well...it sure smells, [bree.name]!"
        lexi.say "I wonder how it tastes?"
    if not minami.hidden:
        minami.say "I never knew how anyone could cook a turkey."
        minami.say "I mean, don't you have to pull it's guts out or something?!?"
    if samantha.flags.schedule == "harem":
        samantha.say "I could never have handled a bird that size!"
        samantha.say "You're braver than me taking it on."
    if not sasha.hidden:
        show sasha annoyed
        sasha.say "You remembered the cranberry sauce, right?"
        sasha.say "Please tell me somebody remembered the cranberry sauce!"
    "Once the turkey takes pride of place on the table, there's an awkward pause."
    "And then I realise that, for some reason, everyone's looking at me!"
    mike.say "Erm..."
    mike.say "What's going on?"
    mike.say "Why are you all staring at me like that?"
    if not bree.hidden:
        show bree happy
        bree.say "We're waiting for you to carve the turkey, of course!"
    if not sasha.hidden:
        show sasha normal
        sasha.say "Not because you're a guy or anything - it's just you've lived here longest!"
    if Person.find("lexi") and lexi.flags.schedule == "harem":
        show lexi happy
        lexi.say "Hurry up and carve the bird already!"
    if not minami.hidden:
        show minami tehe
        minami.say "I can't cut it up, big bro - it's WAY too big!"
    if samantha.flags.schedule == "harem":
        samantha.say "You should do the carving, if you'd like?"
    "All I can do is shrug as I pick up the knife and fork."
    "If they want me to man up and carve the turkey, then so be it."
    "I mean, I've never done it before in my entire life."
    "But how hard can it be?"
    "I'm just cutting flesh off the carcass of a dead bird, right?"
    "So after a few false starts, I get into the swing of it."
    show xmas diner mikemc
    if not bree.hidden:
        show xmas diner bree
        if xmas_party_cook == 'bree':
            show xmas diner badmeal bree_disgust sasha_disgust minami_disgust samantha_disgust lexi_disgust
    if not sasha.hidden:
        show xmas diner sasha
    if Person.find("lexi") and lexi.flags.schedule == "harem":
        show xmas diner lexi
    if not minami.hidden:
        show xmas diner minami
    if samantha.flags.schedule == "harem":
        show xmas diner samantha
    with fade
    "Soon enough I'm doling out slices of freshly cooked turkey to my housemates."
    if xmas_party_cook == 'bree':
        "[bree.name] watches eagerly as everyone tucks into their food."
        "She's tried to play things as if she's really not concerned."
        "But it's plain to see that she's hoping everyone likes it."
        "I put a smile on my face as I stuff the turkey into my mouth."
        "But as I begin to chew, there's just no way I can keep it up."
        bree.say "What's the matter, [hero.name]?"
        bree.say "It's the aftertaste of the starters, right?"
        bree.say "You just need a little more gravy to wash it down?"
        "I force myself to swallow, feeling my eyes water at the effort."
        "Then I gasp for breath and shake my head."
        mike.say "Oh wow..."
        mike.say "That was...that was..."
        if not sasha.hidden:
            sasha.say "GROSS!"
            sasha.say "That's so gross, [bree.name]!"
        if Person.find("lexi") and lexi.flags.schedule == "harem":
            "Lexi spits out a mouthful of half-chewed turkey onto her plate."
            lexi.say "Gah...urgh..."
            lexi.say "Are you trying to poison me?!?"
        if not minami.hidden:
            minami.say "Eww...this turkey tastes weird!"
            minami.say "I'm not eating it, big bro!"
        if samantha.flags.schedule == "harem":
            samantha.say "Oh dear..."
            samantha.say "I don't think it's supposed to taste like this!"
        "[bree.name] shakes her head as she looks around the table."
        "But everywhere she sees people reacting badly to her cooking."
        bree.say "I...I don't understand!"
        bree.say "I looked up cooking a turkey on the internet!"
        bree.say "I must have watched a thousand tutorial videos!"
        mike.say "It's okay, [bree.name], really."
        mike.say "What matters is that you tried your best."
        "[bree.name] nods at my attempts to reassure her."
        "But I can see that she's really upset."
        "I guess I'll have to think of some way to make her feel better."
    elif xmas_party_cook == 'lexi':
        "Lexi hardly seems to care as everyone tucks into their food."
        "It's as if she's not concerned in the slightest as to how whether we like it."
        "I smile and shake my head, secretly thinking that she's got the right idea."
        "I mean, Lexi used to live in a trailer-park."
        "So what are the chances she's a decent cook?"
        "But as I stuff the turkey into my mouth and begin to chew, something odd happens."
        "The food in my mouth tastes amazing - like my mom used to make, only so much better!"
        "I can't help talking around the mouthful I'm chewing!"
        mike.say "Lexi..."
        mike.say "This is amazing!"
        if not bree.hidden:
            bree.say "He...he's right, Lexi!"
            bree.say "This is the best turkey ever!"
        if not sasha.hidden:
            sasha.say "Shit, Lexi!"
            sasha.say "Where did you learn to cook like this?!?"
        if not minami.hidden:
            minami.say "Mmm..."
            minami.say "This is SO delicious, Lexi!"
            minami.say "The best Christmas dinner of all time!"
        if samantha.flags.schedule == "harem":
            samantha.say "Oh my..."
            samantha.say "This is pretty special, Lexi!"
            samantha.say "It tastes very good!"
        "Lexi looks more than a little embarrassed at the sudden chorus of praise."
        "She actually blushes and shifts in her chair a little, shaking her head."
        lexi.say "What?!?"
        lexi.say "It's nothing special, yeah?"
        lexi.say "Just the recipe that my grandma used to use!"
        "I find myself shaking my head too."
        "Perhaps there are hidden depths to Lexi."
        "Things about her that I could never have guessed."
        mike.say "They're right, Lexi."
        mike.say "This is a really great meal."
        mike.say "Maybe you should cook more often?"
        mike.say "Because you're very good at it."
        "Lexi smiles and goes back to eating her food."
        "But I can see that her cheeks are still more than a little flushed."
    else:
        "It feels weird that [bree.name]'s not here with is today."
        "I keep thinking that she's going to walk in any moment."
        "And I can almost hear her chiding Sasha for not getting into the festive spirit."
        "Then I imagine Sasha firing back, making fun of her for being such a big kid!"
        "I guess we're just going to have to raise a glass to her memory."
    scene bg black with dissolve
    pause 1

label xmas_party_singing:
    $ game.pass_time(1)
    scene bg livingroom
    call xmas_party_hh_display from _call_xmas_party_hh_display_1
    with dissolve


    $ xmas_party_singer = ["mike", "minami"][renpy.random.randint(0, 1)] if Harem.find(minami, name="home") else "mike"

    "Once the last of the Christmas dinner has been finished off, I feel like a beached whale!"
    "We're going to be eating left-over turkey well into the New Year, and the thought terrifies me."
    "But right now I'm gearing up for the inevitable argument over who gets lumbered with washing the dishes."
    "It was always a big deal back home until Mom blackmailed Dad into buying a dish-washer."
    "And I've memorised my own list of excuses in the hope that they'll be enough..."
    if not bree.hidden:
        show bree happy
        bree.say "Okay, guys - now it's time to sing some carols!"
    if not sasha.hidden:
        show sasha happy
        sasha.say "Gather round and we can all sing together!"
        sasha.say "[hero.name], what's your favourite carol?"
    "At the mere mention of Christmas Carols I feel terror rising inside of me."
    "What the hell is going on here?!?"
    "We're not in a damn church!"
    if Person.find("lexi") and lexi.flags.schedule == "harem":
        show lexi happy
        lexi.say "Oh yeah!"
        lexi.say "I think I remember some carols."
        lexi.say "Well...the versions with rude words in them anyway!"
    if not minami.hidden:
        show minami happy
        minami.say "Oh, that's a great idea!"
        minami.say "It'll be like something out of a Christmas movie!"
    if samantha.flags.schedule == "harem":
        show samantha happy
        samantha.say "That does sound really nice."
        samantha.say "All cosy and traditional!"
    "I look this way and that, unable to believe what I'm hearing."
    "We just ate a massive Christmas dinner."
    "The only tradition I know about is sitting on my ass and sleeping it off!"
    "But it looks like everyone else is suddenly obsessed with the idea of singing."
    mike.say "Urgh..."
    mike.say "I suppose we could sing a few quick carols."
    mike.say "So who's going to get things started?"
    call xmas_party_hh_display from _call_xmas_party_hh_display_2
    "Suddenly the mood in the room seems to undergo a change."
    "A second ago all of them were eager to get singing."
    "But now none of them are stepping up to the plate!"
    if xmas_party_singer == 'mike':
        "So I let out a sigh of frustration and get to my feet."
        mike.say "Okay...okay..."
        mike.say "I see where this is going!"
        mike.say "I'll sing the first carol."
        mike.say "But after that, I'm off the hook until next year!"
        "I rack my brains to remember a carol that I can reel off."
        "And in the end I settle on the one about the king looking out of his window."
        show xmas singing bree_annoyed sasha_annoyed lexi_annoyed minami_annoyed samantha_annoyed
        if not bree.hidden:
            show xmas singing bree
        if not sasha.hidden:
            show xmas singing sasha
        if Person.find("lexi") and lexi.flags.schedule == "harem":
            show xmas singing lexi
        if not minami.hidden:
            show xmas singing minami
        if samantha.flags.schedule == "harem":
            show xmas singing samantha
        with fade
        "I clear my throat and launch into the carol, giving it all I've got."
        "And it doesn't take long for me to get a reaction."
        if not bree.hidden:
            bree.say "Oh no - I think my ears are bleeding!"
        if not sasha.hidden:
            sasha.say "Whoa...way to murder a classic!"
        if Person.find("lexi") and lexi.flags.schedule == "harem":
            lexi.say "Man, you sound like cats screwing!"
        if not minami.hidden:
            minami.say "Oh, big bro - that does not sound good!"
        if samantha.flags.schedule == "harem":
            samantha.say "Erm...I think you can stop now!"
        "Once I come to the end of the carol, I glare at the lot of them."
        "First they make me sing the damn song, then they complain about it!"
        "There really is no pleasing some people!"
        "But at least that's over until next Christmas."
    else:
        "Then Minami pipes up."
        show minami tehe
        minami.say "I'll sing something!"
        minami.say "And I think I know just the thing..."
        show xmas singing minami singminami
        if not bree.hidden:
            show xmas singing bree
        if not sasha.hidden:
            show xmas singing sasha
        if Person.find("lexi") and lexi.flags.schedule == "harem":
            show xmas singing lexi
        if samantha.flags.schedule == "harem":
            show xmas singing samantha
        with fade
        "Minami wastes no time in launching into the carol."
        "It's one of the older ones, I can't remember the title."
        "But it suits her voice perfectly and she sounds divine."
        "Soon enough, Minami has everyone in the room spellbound."
        "And by the time she's done, she seems embarrassed by the attention."
        if not bree.hidden:
            bree.say "That was amazing, Minami!"
        if not sasha.hidden:
            sasha.say "Wow - who taught you to sing like that?!?"
        if Person.find("lexi") and lexi.flags.schedule == "harem":
            lexi.say "You could be in a choir or something!"
        if samantha.flags.schedule == "harem":
            samantha.say "That was lovely, Minami - you have a beautiful voice!"
        "Minami blushes and looks away from everyone."
        "But she's smiling the whole time, which I take as a good sign."
        mike.say "They're right, Minami."
        mike.say "That was a really beautiful performance."
        mike.say "Your voice is amazing!"
        minami.say "Thanks, big bro!"
        minami.say "Coming from you, that means a lot!"
    scene bg black with dissolve
    pause 1

label xmas_party_pudding:
    $ game.pass_time(1)
    scene bg livingroom
    call xmas_party_hh_display from _call_xmas_party_hh_display_3
    with dissolve
    "As soon as we're done with the torture of singing, I get the creepy feeling that I'm being watched."
    "And all it takes is a quick glance around the room to prove that I'm right in my suspicions."
    "Everyone is staring at me with expectant looks on their faces, like they're waiting for something."
    mike.say "Erm..."
    mike.say "Guys...what's up?"
    mike.say "You're kind of making me nervous!"
    "I hear a chorus of gasps and looks of surprise are exchanged before me."
    if not bree.hidden:
        show bree dazed
        bree.say "The pudding!"
        bree.say "Don't tell me you've forgotten?!?"
    if not sasha.hidden:
        sasha.say "No excuses!"
        sasha.say "I want my Christmas pudding!"
    if Person.find("lexi") and lexi.flags.schedule == "harem":
        show lexi happy
        lexi.say "You've got a brain like a sieve!"
        lexi.say "Make with the pudding already!"
    if not minami.hidden:
        minami.say "Oh, big bro, you're so forgetful!"
        minami.say "You promised to make pudding, remember?"
    if samantha.flags.schedule == "harem":
        show samantha happy
        samantha.say "I think all that singing's made you dizzy!"
        samantha.say "But it's made us hungry for pudding!"
    "Of course, I'd agreed to handle the last course of the meal - the pudding!"
    scene bg kitchen with fade
    "Without another word, I race into the kitchen to discharge my responsibilities."
    scene bg livingroom
    call xmas_party_hh_display from _call_xmas_party_hh_display_4
    with fade
    "And it doesn't take long for the others to begin showing an interest in my progress."
    if not bree.hidden:
        show bree happy
        bree.say "Ooh...that smells good!"
    if not sasha.hidden:
        sasha.say "This better be worth the wait!"
    if Person.find("lexi") and lexi.flags.schedule == "harem":
        lexi.say "The proof's in the pudding!"
    if not minami.hidden:
        show minami happy
        minami.say "Make mine an extra large portion!"
    if samantha.flags.schedule == "harem":
        samantha.say "I'm sure this will be great!"
    "I smile as I dole out a portion of the pudding for everyone."
    "Then all I can do is hand them over and wait."
    "And with all the eager spoonful's being swallowed, I soon get a reaction."
    call xmas_party_hh_display from _call_xmas_party_hh_display_5
    if hero.has_skill("cooking"):
        "Soon I see their eyes open and bulging."
        "And I try to chalk that up to the pudding being hot."
        "What's the matter with them all?"
        "Does it really taste that bad?"
        "Suddenly I get my answer as the spoons begin to move faster and faster."
        "I stare around the table in amazement as everyone seems to forget their manners."
        "They're shovelling the pudding into their mouths as fast as they possibly can!"
        "And when anyone finished their own portion, they eye up whatever the person next to them has left."
        "But all this gets them is a jealous, sideways glance, like a dog growling over it's dinner!"
        "All I can do is watch in silent amazement as they last of the pudding is polished off."
        if not bree.hidden:
            show bree happy
            bree.say "That was SO good!"
            bree.say "Erm...there wouldn't be any more, would there?"
        if not sasha.hidden:
            show sasha happy
            sasha.say "I never tasted pudding like that before!"
            sasha.say "There's got to be second helpings, right?"
        if Person.find("lexi") and lexi.flags.schedule == "harem":
            show lexi happy
            lexi.say "That tasted fucking amazing!"
            lexi.say "What do I gotta do to get another bowl?"
        if not minami.hidden:
            minami.say "I loved that, big bro!"
            minami.say "You saved some more for me, yeah?"
        if samantha.flags.schedule == "harem":
            show samantha happy
            samantha.say "That was really great!"
            samantha.say "I'd love seconds, if there's anything left?"
        "I can hardly believe the chorus of praise I'm hearing."
        "And I fetch the last of the pudding without saying a word."
        "But when I get back to the table, it's snatched out of my hands!"
        "I watch as everyone literally fights over the last of the pudding."
        "And all I can do is stand back and shake my head in amazement."
    else:
        "Soon I see their eyes open and bulging."
        "And I try to chalk that up to the pudding being hot."
        "But then first mouthfuls have been swallowed with some effort."
        "And once their mouths are empty, I begin to get my feedback."
        if not bree.hidden:
            show bree lose
            bree.say "Oh...oh dear..."
            bree.say "I feel like I've swallowed a bowling ball!"
        if not sasha.hidden:
            show sasha surprised
            sasha.say "Wow...that was bad!"
            sasha.say "Like, really bad!"
        if Person.find("lexi") and lexi.flags.schedule == "harem":
            show lexi sad
            lexi.say "Eww..."
            lexi.say "I don't think I want seconds!"
        if not minami.hidden:
            show minami scared
            minami.say "Yuck!"
            minami.say "That was SO bad, big bro!"
        if samantha.flags.schedule == "harem":
            show samantha sad
            samantha.say "Oh dear..."
            samantha.say "I don't think that's sitting too well..."
        "I look up from my own bowl, disbelief written all over my face."
        "I tried my hardest to whip up that pudding!"
        "The least they could do is pretend to like it!"
        mike.say "Hey!"
        mike.say "That thing took me ages to cook!"
        mike.say "And it was my first time too!"
        "But for all of my protests, I'm sure it'll be my last."
        "Everyone is pushing their bowls away in disgust."
        "And more than one face around the table looks a little green too!"
    scene bg black with dissolve
    pause 1

label xmas_party_presents:
    $ game.pass_time(1)
    scene bg livingroom with dissolve
    "Now we really are done eating and nobody wants to hear another damn carol."
    "That means we can get down to the serious side of the holiday season."
    "And, of course, by that I mean swapping presents!"
    "Everyone's been eyeing up the neatly-wrapped packages under the tree."
    "Trying to sneak a look at the labels when they think nobody else is looking."
    "But now, as we all gather around in the sitting room, I'm starting to feel nervous."
    "I'm always worried that the gifts I've chosen for people are going to be wrong somehow."
    "I try really hard to pick something that I think they'll love."
    "But sometimes it just doesn't seem to turn out how I'd hoped!"
    if not bree.hidden:
        show bree close casual happy
        bree.say "Here you go, [hero.name]!"
        bree.say "You have to open my gift first!"
        "[bree.name] almost leaps atop me as she thrusts her gift in my face."
        "But the expression on her own features makes me smile at her enthusiasm."
        "I mean, who doesn't want to indulge a cute blonde bearing gifts?"
        mike.say "Sure thing, [bree.name]!"
        mike.say "I can't wait to see what you got me..."
        play sound [paper_ripping_1, paper_ripping_2]
        if bree.is_girlfriend:
            "I hastily tear open the wrapping paper to reveal [bree.name]'s gift."
            "But I've already guessed from the size and shape what it has to be."
            "And I'm right, it's a game for the Zbox!"
            mike.say "Aw, thanks, [bree.name]!"
            mike.say "It's...it's...'JIM'S EARTHWORM'?!?"
            mike.say "I...I never even knew this game existed!"
            "[bree.name]'s cheeks are already flushing red."
            "And I can feel mine starting to do the same too!"
            show bree close flirt
            bree.say "I...I know it's a little bit naughty."
            bree.say "You know - buying you an adult videogame..."
            bree.say "But it looked really fun too!"
            mike.say "No need to explain yourself, [bree.name]."
            mike.say "I love it!"
            show bree close happy
            "[bree.name] smiles, delighted with my reaction."
        else:
            "I hastily tear open the wrapping paper to reveal [bree.name]'s gift."
            "But I've already guessed from the size and shape what it has to be."
            "And I'm right, it's a game for the Zbox!"
            mike.say "Aw, thanks, [bree.name]!"
            mike.say "It's 'Immortal Wombat' - the remastered edition too!"
            mike.say "I can't wait to kick some mutant marsupial ass!"
            "[bree.name] smiles, delighted with my reaction."
            bree.say "I'm glad you like it."
            show bree close normal
            bree.say "But you've got to let me play too!"
        "Now it's my turn to return the favour and give [bree.name] my gift."
        "I snatch it up from under the table and hand it over to her."
        show bree happy
        play sound [paper_ripping_1, paper_ripping_2]
        "[bree.name] looks delighted as she begins to unwrap her gift."
        menu:
            "Offer style clothes":
                show bree close normal
                bree.say "It's something to wear!"
                bree.say "It's...it's..."
                show bree close dazed
                bree.say "Oh...it's a tracksuit!"
                "I see the disappointment on [bree.name]'s face."
                "But I'm ready to jump in and make the save."
                mike.say "Read what's printed on the back, [bree.name]!"
                bree.say "Ooh..."
                show bree close surprised
                $ bree.love += 2
                bree.say "It says 'Number One Gamer Girl'!"
                $ bree.love += 1
                bree.say "And it has my name printed on it too!"
                mike.say "Yeah, think of it more as something to wear around the house, [bree.name]!"
                mike.say "While you're hanging out and playing videogames."
                show bree close happy
                "[bree.name] giggles with enthusiasm and then gives me a hug."
                "Which I choose to take as proof I made the right choice."
            "Offer gym clothes":
                show bree close normal
                bree.say "It's something to wear!"
                bree.say "It's...it's..."
                show bree close dazed
                bree.say "Oh...it's a tracksuit!"
                "In my enthusiasm, I totally miss the disappointment in [bree.name]'s tone."
                "Instead I plough straight on, trying to explain the logic behind the gift."
                mike.say "Yeah, [bree.name], a tracksuit!"
                mike.say "I figured you spend too much time on the Zbox."
                mike.say "So this should motivate you to get up off of your ass, yeah?"
                show bree close angry
                $ bree.love -= 3
                bree.say "What are you trying to say?"
                bree.say "That I'm getting fat?!?"
                show bree close annoyed
                "All I can do is shrug helplessly as [bree.name] rolls her eyes."
                "Well, that could have gone better..."
    if not sasha.hidden:
        scene bg livingroom
        show sasha close casual happy
        sasha.say "Open mine next!"
        sasha.say "I can't wait for you to see what it is!"
        "I nod as Sasha shoves her gift into my hands."
        "I'm almost as eager to unwrap it as she is to see me do it!"
        "After all, she looks so cute when she's this enthusiastic."
        "It's not a large gift, but that's not really a problem."
        "It's the thought that counts."
        mike.say "Okay, Sasha, okay!"
        mike.say "Let me open the damn thing already!"
        play sound [paper_ripping_2, paper_ripping_2]
        if sasha.is_girlfriend:
            "I make quick work of tearing open Sasha's gift."
            "And I'm left holding a small remote control."
            "It doesn't look familiar and I have no idea what it's for."
            "I look at Sasha in the hope she's going to help me out."
            show sasha close normal
            sasha.say "It's a remote control."
            mike.say "Ah, yeah, Sasha..."
            mike.say "I kind of worked that out for myself!"
            show sasha close flirt
            "At this, Sasha gives me a wicked smile."
            "She leans in close so that only I can hear her."
            sasha.say "It's for one of those remote-controlled vibrators!"
            sasha.say "The little egg-shaped ones."
            sasha.say "Specifically for the one I have inside of me right now!"
            "I look at the remote control, and then back at Sasha."
            show sasha close joke
            "And she nods her head slowly."
            "Suddenly I feel like I've been empowered beyond my wildest dreams."
            "I can't wait for the right moment to press the button."
            "That and see what effect it has on Sasha too!"
        else:
            "I make quick work of tearing open Sasha's gift."
            "And I'm left holding a keychain dangling from my fingers."
            "I mean, it's a very nice keychain, don't get me wrong."
            "But it's still a bit of an anti-climax!"
            mike.say "Oh..."
            mike.say "Thanks, Sasha..."
            show sasha close normal
            "Sasha seems to sense the surprise her gift has inspired."
            "And she wastes no time in jumping in to explain herself."
            sasha.say "You're always losing your keys, yeah?"
            sasha.say "So I figured you could use one of those things."
            show sasha close happy
            sasha.say "Should make it so much easier to find them, huh?"
            mike.say "Yeah, Sasha, I guess so!"
        "I don't waste any time in grabbing my gift for Sasha."
        "I hand it straight over to her with a smile on my face."
        play sound [paper_ripping_2, paper_ripping_1, paper_ripping_2]
        "Nodding my head for her to take it and tear off the paper."
        menu:
            "Offer ear-plugs":
                show sasha close normal
                sasha.say "Oh yeah..."
                sasha.say "I can't wait to see what this is!"
                "Sasha rips off the wrapping paper and holds up her present."
                "I was hoping to see her crack a smile, maybe even laugh."
                show sasha close annoyed
                "But instead she just looks confused."
                sasha.say "Huh?!?"
                sasha.say "Why'd you buy me a load of ear-plugs?"
                mike.say "They're for when you play guitar, Sasha."
                show sasha close vangry
                $ sasha.love -= 3
                sasha.say "But I need to be able to hear myself play!"
                mike.say "I know - but nobody else does!"
                mike.say "They're for you to hand out to the rest of us!"
                show sasha close angry
                "Sasha glares at me, shaking her head in disbelief."
                "And all I can do is offer her an apologetic smile as I cringe away."
            "Offer an amp":
                show sasha close normal
                sasha.say "Oh yeah..."
                sasha.say "I can't wait to see what this is!"
                "Sasha rips off the wrapping paper and holds up her present."
                "She holds up a perfect miniature of an amp by its handle."
                show sasha close sad
                show fx question
                sasha.say "Whoa..."
                sasha.say "What is this thing?"
                sasha.say "Like a model or something?"
                mike.say "No, Sasha - it's a real amp."
                mike.say "Just a smaller one, so you can take it anywhere!"
                hide fx
                show sasha close surprised
                $ sasha.love += 3
                sasha.say "Which means I can practice anywhere too!"
                mike.say "Exactly!"
                show sasha close happy
                "Sasha and I are both beaming right now."
                "But I can see that not everyone in the room feels the same way."
                "I can't blame them, as Sasha's notoriously loud when she practices."
                "But I'm enjoying basking in her approval far too much to care!"
    if Person.find("lexi") and lexi.flags.schedule == "harem":
        scene bg livingroom
        show lexi close casual normal
        with fade
        lexi.say "Here you go, [hero.name]."
        lexi.say "I hope you like what I got ya!"
        "Lexi hands me a present which is surprisingly well wrapped."
        "And she watches intently as I take it from her and begin to tear at the paper."
        "It seems like she's really keen to see my reaction to what she's got me."
        "So I make a point of smiling and looking interested in getting into it."
        mike.say "Thanks, Lexi."
        mike.say "That's really thoughtful of you!"
        show lexi close happy
        "Lexi nods and smiles back at me, urging me on to unwrap her gift."
        play sound paper_ripping_1
        if lexi.is_girlfriend:
            "I'm more than a little puzzled by what I find inside the wrapping paper."
            "It seems to be a wad of paper or thin card."
            "Each one is around the size of a credit card."
            "Totally non-plussed, I look up at Lexi."
            show lexi close normal
            lexi.say "Read 'em, you dope!"
            lexi.say "Read what's on 'em!"
            "I do as I'm told, seeing that they all have the same thing written on them."
            "The words are in black ink, and I recognise Lexi's distinctive handwriting."
            mike.say "'Redeemable for any sexual activity'!"
            show lexi close angry
            lexi.say "Shhh!"
            lexi.say "Don't shout it out loud!"
            show lexi close wink
            lexi.say "They're coupons for sex - with me, yeah?"
            lexi.say "You whip one of those babies out, and I gotta do whatever you want!"
            show lexi close normal
            "I nod as I hastily stuff the coupons into my pocket."
            "But I'm already thinking of what I can ask Lexi to do for me."
        else:
            "It doesn't take me long to feel that what's inside is hard."
            "Also that it's weight shifts as I turn the gift over in my hands."
            "That means it can only be a bottle of some kind with liquid inside."
            "And sure enough, I open it to discover a bottle of tequila."
            mike.say "Thanks again, Lexi."
            mike.say "I never tried this brand of tequila before!"
            "In truth, I've never really been a massive tequila drinker."
            "But it'd be ungrateful to tell Lexi that, so I keep it to myself."
            show lexi close normal
            lexi.say "It's a pretty good one."
            lexi.say "Danny used to drink it all the time..."
            show lexi sad
            "At the mention of her abusive ex, Lexi trails off."
            "She seems to have dragged up bad memories."
            mike.say "We can drink it together, Lexi."
            mike.say "Just you and me."
            mike.say "How does that sound?"
            show lexi close normal
            "Lexi seems to cheer up a little at this."
            "She nods and smiles like she's looking forward to it."
        "Now it's my turn to pick up a gift from under the tree and hand it to Lexi."
        play sound [paper_ripping_1, paper_ripping_2, paper_ripping_1]
        "She takes it eagerly from me, already tearing at the paper."
        "I smile and nod, hoping that she likes what I got her."
        menu:
            "Offer warm clothes":
                "Lexi attacks the wrapping paper like her life depends on it."
                "And it doesn't take her more than a couple of seconds to get inside."
                "But when she does, Lexi stops and frowns at what she sees."
                show lexi close sad
                lexi.say "Huh?!?"
                lexi.say "Is this...is this knit-wear?"
                "I force a weak smile onto my face."
                "It looks like I fucked up."
                "But maybe I can salvage something from this potential disaster."
                mike.say "It's a cardigan, Lexi."
                mike.say "Something to keep you nice and warm now winter's here?"
                mike.say "I mean, most of your clothes are pretty skimpy!"
                $ lexi.love -= 3
                "Lexi stares at me through narrowed eyes."
                "And I do my best to look the other way."
            "Offer light clothes":
                "Lexi attacks the wrapping paper like her life depends on it."
                "And it doesn't take her more than a couple of seconds to get inside."
                "But when she does, Lexi stops and smiles at what she sees."
                show lexi close surprised
                lexi.say "Are these what I think they are?"
                lexi.say "Christmas stockings?"
                "Lexi holds up the pair of stockings in question."
                "They're hold-ups, striped red and white like candy canes."
                mike.say "Well, I was going to get you something warm."
                mike.say "But that just didn't seem like the kind of thing you'd like!"
                show lexi close happy
                $ lexi.love += 3
                lexi.say "You got that right!"
                "Lexi chuckles as she leans forward and plants a kiss on my cheek."
                "Sure, I could have got her something more conservative and sensible."
                "But this time of year the idea is to try and make people happy."
                "So to hell with being sensible."
    if not minami.hidden:
        scene bg livingroom
        show minami close casual happy
        with fade
        minami.say "Happy Christmas, big bro!"
        minami.say "Time to open my present, okay?"
        minami.say "Hurry up and rip into it!"
        "I nod and smile as I accept the gift from Minami."
        "She was always this excited on Christmas morning when we were kids."
        "And the only way to make her calm down is to actually do what she says."
        "Not that I don't want to see what she got me too!"
        mike.say "Okay, Minami!"
        mike.say "I'm doing it!"
        show minami close normal
        play sound [paper_ripping_1, paper_ripping_1]
        "Minami watches me intently as I tear at the wrapping paper."
        if minami.is_girlfriend:
            "I have no idea what to expect once the paper is torn away."
            "Minami never really bought me anything for Christmas back home."
            "She was younger and so it was never expected of her."
            mike.say "Oh..."
            mike.say "Oh wow..."
            "I hold up a pair of panties and study them with interest."
            "But Minami pushes my hand down before anyone else can see."
            mike.say "H...huh?!?"
            mike.say "What's the matter, Minami?"
            mike.say "Why don't you want anyone to see the panties?"
            show minami close tehe
            minami.say "Because they're a pair of mine!"
            minami.say "A pair that I've been wearing!"
            "It takes a moment for that revelation to sink in."
            "And when it does, I have to fight the instinct to instantly sniff them!"
            mike.say "B...but why..."
            minami.say "So you can always remind yourself how my pussy smells!"
            minami.say "Even when we're not together!"
            "I return Minami's grin as I hastily stuff her present into my pocket."
        else:
            "I have no idea what to expect once the paper is torn away."
            "Minami never really bought me anything for Christmas back home."
            "She was younger and so it was never expected of her."
            mike.say "Oh..."
            mike.say "Oh wow..."
            "I hold up a large mug by the handle."
            "It's unremarkable, save for the words \"Best Big Bro\" printed on it."
            minami.say "You like it, yeah?"
            minami.say "You drink coffee and you are my big bro!"
            minami.say "So it's the perfect gift, right?"
            mike.say "Sure, Minami, sure."
            mike.say "It's the best gift ever..."
            "I smile as I try to sound convincing."
            "And it seems to work, as Minami beams happily back at me."
        mike.say "Now it's my turn, Minami."
        mike.say "Here's your gift from me!"
        "I pick up the right gift from under the tree."
        "And I pass it into Minami's eager hands."
        menu:
            "Offer white panties":
                play sound [paper_ripping_2, paper_ripping_1, paper_ripping_2]
                "It only takes a couple of seconds for Minami to tear away the wrapping paper."
                "And then she holds up the contents of the package, studying them intensely."
                show minami close surprised
                "Then she turns to look me straight in the eye."
                minami.say "Oh, big bro!"
                minami.say "How did you know?!?"
                "Minami holds up a pair of delicate little white panties."
                "Which to anyone else I'm sure look just like any other little white panties."
                "But we both know they're exactly the kind worn by one of Minami's favourite anime heroines."
                mike.say "Oh, I've seen you working on that outfit, Minami."
                mike.say "And I remember you telling me you couldn't find the panties for it."
                show minami close happy
                $ minami.love += 3
                minami.say "This is perfect, big bro!"
                minami.say "Now I can finish it off in time for the New Year."
                minami.say "And I think you should get a reward."
                show minami close normal
                minami.say "How about being the first to see me in it?"
                "I nod and smile, already forming a picture in my mind."
            "Offer blue panties":
                play sound [paper_ripping_2, paper_ripping_1, paper_ripping_2]
                "It only takes a couple of seconds for Minami to tear away the wrapping paper."
                "And then she holds up the contents of the package, studying them intensely."
                show minami close sad
                "Then she turns to look me straight in the eye."
                minami.say "I...I don't get it, big bro."
                minami.say "Why did you buy me such an ugly pair of panties?"
                "I look at the large, navy blue panties she's holding."
                "And then I shrug as I look Minami straight in the eye."
                mike.say "You're always dressing up like a Japanese schoolgirl, Minami."
                mike.say "And those are the kind of underwear that go with the uniform."
                mike.say "You don't seem to have any, as I never see you wearing them."
                show minami close angry
                $ minami.love -= 3
                minami.say "Urgh...that's not the point, big bro!"
                minami.say "I'm not trying to convince people I'm an actual schoolgirl!"
                mike.say "You're not?"
                "Minami makes a muttering sound under her breath."
                "And then she turns her back on me in disgust."
    if samantha.flags.schedule == "harem":
        scene bg livingroom
        show samantha close casual happy
        with fade
        samantha.say "Happy Christmas, [hero.name]!"
        samantha.say "I hope you like what I got you."
        "I almost miss the fact that Sam's handing me a gift."
        "Her smile is that sweet and lovely it almost hypnotises me!"
        "But I do my best to shake it off and accept her package."
        if samantha.flags.nickname == "cupcake":
            mike.say "Aw, thanks, Cupcake!"
        else:
            mike.say "Aw, thanks, Sam!"
        mike.say "I'm sure I'm going to love it."
        "Sam's smile grows wider still as I unwrap the present."
        "All the time wondering just what she could have got me."
        play sound [paper_ripping_1, paper_ripping_1, paper_ripping_2]
        if samantha.is_girlfriend:
            "Tearing away the last of the wrapping paper, I gaze at what's inside."
            "I honestly had no idea what to expect, but it still surprises me."
            mike.say "It's..."
            mike.say "It's a picture of you..."
            mike.say "And you're naked!"
            show samantha close annoyed
            "Sam leans in and claps her hand over my mouth."
            samantha.say "Shhh!"
            samantha.say "Don't tell everyone else in the house!"
            "Sam waits until she's sure that I've got it under control."
            show samantha close normal
            "And only then does she remove her hand from my mouth."
            if samantha.flags.nickname == "cupcake":
                mike.say "Wow, Cupcake...this is amazing!"
            else:
                mike.say "Wow, Sam...this is amazing!"
            samantha.say "Well, I figured you didn't have a picture of me."
            samantha.say "And this way you can look at me anytime you want."
            samantha.say "As well as be reminded of what we mean to each other too."
            hide samantha
            show samantha kiss casual
            $ samantha.flags.kiss += 1
            "Sam leans in and kisses me full on the lips."
            "I return the gesture, enjoying every moment."
            hide samantha
            show samantha close casual normal
        else:
            "Tearing away the last of the wrapping paper, I gaze at what's inside."
            "I honestly had no idea what to expect, but it still surprises me."
            mike.say "It's..."
            mike.say "It's a teddy bear?!?"
            show samantha close normal
            samantha.say "Well, you always seemed so lonely in that room on your own."
            samantha.say "So I figured that you could use something to keep you company in bed!"
            "I look at Sam for a moment, trying to figure something out."
            "Does she know what a torch I'm carrying for her?"
            "Or is she just trying to make a kind gesture for someone she considers a friend?"
            "In the end, I choose to go with the latter."
            if samantha.flags.nickname == "cupcake":
                mike.say "Thanks, Cupcake."
            else:
                mike.say "Thanks, Sam."
            mike.say "That's really thoughtful of you."
            "Sam leans in and plants a chaste kiss on my cheek."
            "And all the time I'm wondering if the bear might have her scent on it."
        "I search under the tree until I find my gift for Sam."
        if samantha.flags.nickname == "cupcake":
            mike.say "My turn, Cupcake."
        else:
            mike.say "My turn, Sam."
        mike.say "Here you go!"
        "Sam positively beams as she accepts her gift."
        show samantha close happy
        play sound [paper_ripping_1, paper_ripping_2]
        "And she begins to unwrap it without hesitation."
        menu:
            "Offer an old picture of you":
                "Sam's enthusiasm seems to build as she opens her present."
                show samantha close sad
                "But when she takes a look inside, the expression on her face changes."
                "Suddenly Sam looks puzzled, and then she frowns."
                samantha.say "It's a picture..."
                show samantha close surprised
                $ samantha.love += 3
                samantha.say "A picture of you and me!"
                show samantha close sad
                $ samantha.love -= 6
                samantha.say "...and Ryan."
                if samantha.flags.nickname == "cupcake":
                    mike.say "Yeah, Cupcake, that's right."
                else:
                    mike.say "Yeah, Sam, that's right."
                mike.say "I thought it might bring back happy memories?"
                samantha.say "Well, you were half right."
                samantha.say "It brings back memories."
                samantha.say "Just not good ones!"
                "How could I be such a dummy?"
                "The last thing Sam would want to remember is being with Ryan!"
                if samantha.flags.nickname == "cupcake":
                    mike.say "Ah...sorry, Cupcake!"
                else:
                    mike.say "Ah...sorry, Sam!"
                show samantha close normal
                samantha.say "It's okay, [hero.name]."
                samantha.say "Let's just forget about it, okay?"
                "I nod in agreement and let the matter drop."
                "But I can't help wondering just how much damage I've done."
            "Offer a new picture of you":
                "Sam's enthusiasm seems to build as she opens her present."
                show samantha close sad
                "But when she takes a look inside, the expression on her face changes."
                "Suddenly Sam looks puzzled, and then she frowns."
                samantha.say "It's a picture..."
                show samantha close surprised
                $ samantha.love += 3
                samantha.say "A picture of you and me!"
                if samantha.flags.nickname == "cupcake":
                    mike.say "I hope you don't mind me picking one without Ryan, Cupcake."
                else:
                    mike.say "I hope you don't mind me picking one without Ryan, Sam."
                mike.say "I just thought it was time we started to move on without him, that's all."
                show samantha close normal
                "Sam nods and smiles, giving me an unexpected hug."
                "As soon as I'm over the surprise, I return the gesture."
                samantha.say "Of course I don't mind!"
                samantha.say "And you're right, [hero.name]."
                samantha.say "He's out of our lives now."
                show samantha close happy
                samantha.say "And we're better off for it!"
    scene bg livingroom
    call xmas_party_hh_display from _call_xmas_party_hh_display_6
    if not bree.hidden:
        show bree happy
    if not sasha.hidden:
        show sasha happy
    if Person.find("lexi") and lexi.flags.schedule == "harem":
        show lexi happy
    if not minami.hidden:
        show minami happy
    if samantha.flags.schedule == "harem":
        show samantha happy
    with fade
    "Once everyone has finished opening their gifts, it's getting pretty late."
    "I know that I should be thinking about getting to bed soon."
    "But we're all chilled out and still full of Christmas dinner."
    "And so we stay up a while, talking about nothing in particular and just generally hanging out."
    "All in all it's been great to spend some time with my housemates at Christmas."
    "So why not just sit back and enjoy the atmosphere a little longer?"
    $ hero.hunger += 10
    $ game.pass_time(1)
    $ game.room = "livingroom"
    return

label xmas_party_hh_display:

    if not bree.hidden and not sasha.hidden and not minami.hidden and samantha.flags.schedule == "harem" and Person.find("lexi") and lexi.flags.schedule == "harem":
        show bree casual normal at left5
        show sasha casual normal at right5
        show minami casual normal at center
        show samantha casual normal at mostright5
        show lexi casual normal at mostleft5


    elif not bree.hidden and not sasha.hidden and not minami.hidden and samantha.flags.schedule == "harem":
        show bree casual normal at left4
        show sasha casual normal at right4
        show minami casual normal at mostleft4
        show samantha casual normal at mostright4
    elif not bree.hidden and not sasha.hidden and samantha.flags.schedule == "harem" and Person.find("lexi") and lexi.flags.schedule == "harem":
        show bree casual normal at left4
        show sasha casual normal at right4
        show samantha casual normal at mostright4
        show lexi casual normal at mostleft4
    elif not bree.hidden and not sasha.hidden and not minami.hidden and Person.find("lexi") and lexi.flags.schedule == "harem":
        show bree casual normal at left4
        show sasha casual normal at right4
        show lexi casual normal at mostleft4
        show minami casual normal at mostright4
    elif not sasha.hidden and not minami.hidden and samantha.flags.schedule == "harem" and Person.find("lexi") and lexi.flags.schedule == "harem":
        show sasha casual normal at right4
        show minami casual normal at left4
        show samantha casual normal at mostright4
        show lexi casual normal at mostleft4
    elif not bree.hidden and not minami.hidden and samantha.flags.schedule == "harem" and Person.find("lexi") and lexi.flags.schedule == "harem":
        show bree casual normal at left4
        show minami casual normal at right4
        show samantha casual normal at mostright4
        show lexi casual normal at mostleft4


    elif not bree.hidden and not sasha.hidden and not minami.hidden:
        show bree casual normal at left
        show sasha casual normal at right
        show minami casual normal at center
    elif not bree.hidden and not sasha.hidden and samantha.flags.schedule == "harem":
        show bree casual normal at left
        show sasha casual normal at right
        show samantha casual normal at center
    elif not bree.hidden and not sasha.hidden and Person.find("lexi") and lexi.flags.schedule == "harem":
        show bree casual normal at left
        show sasha casual normal at right
        show lexi casual normal at center
    elif not sasha.hidden and not minami.hidden and samantha.flags.schedule == "harem":
        show sasha casual normal at right
        show minami casual normal at center
        show samantha casual normal at left
    elif not sasha.hidden and samantha.flags.schedule == "harem" and Person.find("lexi") and lexi.flags.schedule == "harem":
        show sasha casual normal at right
        show samantha casual normal at center
        show lexi casual normal at left
    elif not sasha.hidden and not minami.hidden and Person.find("lexi") and lexi.flags.schedule == "harem":
        show sasha casual normal at right
        show lexi casual normal at center
        show minami casual normal at left
    elif not bree.hidden and not minami.hidden and samantha.flags.schedule == "harem":
        show bree casual normal at left
        show minami casual normal at center
        show samantha casual normal at right
    elif not bree.hidden and samantha.flags.schedule == "harem" and Person.find("lexi") and lexi.flags.schedule == "harem":
        show bree casual normal at left
        show samantha casual normal at right
        show lexi casual normal at center
    elif not bree.hidden and not minami.hidden and Person.find("lexi") and lexi.flags.schedule == "harem":
        show bree casual normal at left
        show minami casual normal at center
        show lexi casual normal at right


    elif not bree.hidden and not sasha.hidden:
        show bree casual normal at left
        show sasha casual normal at right
    elif not bree.hidden and not minami.hidden:
        show bree casual normal at left
        show minami casual normal at right
    elif not bree.hidden and samantha.flags.schedule == "harem":
        show bree casual normal at left
        show samantha casual normal at right
    elif not bree.hidden and Person.find("lexi") and lexi.flags.schedule == "harem":
        show bree casual normal at left
        show lexi casual normal at right
    elif not sasha.hidden and not minami.hidden:
        show sasha casual normal at right
        show minami casual normal at left
    elif not sasha.hidden and samantha.flags.schedule == "harem":
        show sasha casual normal at right
        show samantha casual normal at left
    elif not sasha.hidden and Person.find("lexi") and lexi.flags.schedule == "harem":
        show sasha casual normal at right
        show lexi casual normal at left
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
