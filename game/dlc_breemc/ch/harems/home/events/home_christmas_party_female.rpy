init python:
    Event(**{
    "name": "home_christmas_party_female_planned",
    "label": "home_christmas_party_female_planned",
    "priority": 1000,
    "conditions": [
        HeroTarget(
            IsGender("female"),
        ),
        IsSeason(3),
        'game.calendar.day_of_season == 18',
        'not (mike.hidden or sasha.hidden)'
        ],
    "once_day": True,
    })

    Event(**{
    "name": "home_christmas_party_female_cancelled",
    "label": "home_christmas_party_female_cancelled",
    "priority": 1000,
    "conditions": [
        HeroTarget(
            IsGender("female"),
        ),
        'mike.hidden or sasha.hidden'
        ],
    })



label home_christmas_party_female_planned:
    $ renpy.dynamic("christmas_party_day", "appointment")
    $ christmas_party_day = game.calendar.get_future_days_played("christmaseve")
    $ appointment = LabelAppointment((18, 21), ["mike", "sasha"], "Home Christmas Party", "home_christmas_party_female_01", "home_christmas_party_female_missed")
    $ hero.calendar.add(christmas_party_day, appointment)
    return

label home_christmas_party_female_missed:
    "Shit, I missed the Christmas home party. [mike.name] and Sasha are going to be mad."
    $ bree.love -= 4
    $ sasha.love -= 4
    return

label home_christmas_party_female_cancelled:
    $ hero.calendar.find_and_remove(label="home_christmas_party_female_01")
    return

label home_christmas_party_female_01(appointment=None):

    scene bg livingroom with fade
    "I've always kind of dreaded Christmas coming around while I've been sharing a house with other people."
    "My own family aren't the kind that get together for the holiday season like you see in films and TV shows."
    "But I always seem to end up living with people that do exactly that, head home the moment they can."
    "And so most years I spend Christmas on my own, in a big empty house."
    "It sucks and it's painfully lonely, so I usually end up moping around the place on my own."
    "But this year it just so happens that everyone is staying put."
    "And so we've decided to have a party together."
    "Well, I say we decided, but I don't recall there ever being a house meeting or a vote of any kind."
    "[mike.name] and Sasha just kind of started talking about it, and then it snowballed from there."
    "One person volunteered to cook a course for dinner, then another the next one."
    show xmas snacks breemc mike sasha with fade
    "And now here we are, gathering round the table to see what's been cooked up for us!"
    "One by one, everyone comes down from their rooms, drawn by the smell of the food."
    mike.say "Ooh - I wonder what we're having to start off with?"

































    "Sasha did some pretty big talking when she took on the task of cooking the appetisers."
    "She told us that not only could she handle it, but that she could do it in record time too."
    "And as soon as I take in the food on offer, I can see why she made that claim."
    "Sure, there's a lot of stuff on the table, and it all looks perfectly edible."
    "But I can't see one thing that's not come out of a tin or a packet!"
    "Processed meat, processed cheese and every form of fat known to humankind!"
    "What did she do - just sweep stuff off the supermarket shelf and into her shopping cart?!?"
    bree.say "Ah..."
    bree.say "Wow, Sasha..."
    bree.say "I really don't know what to say!"
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
    mike.say "Whoa...that's mega hot!"
    mike.say "Normally I only snack on this kind of stuff when I'm having a marathon on the Z-Box!"






    scene bg black with dissolve
    pause 1

label home_christmas_party_female_02:
    $ game.pass_time(1)
    scene bg livingroom
    show mike casual normal at left
    show sasha casual normal at right
    with dissolve
    "It feels like we only just got done eating the appetisers."
    "But already the smell of something new is wafting into the room."
    "So I guess that it must be time for the main course."
    "Where we devour the remains of the unfortunate bird sacrificed to our festive celebrations."
    "But I don't know how anyone is going to manage it."
    "Because nobody held anything back when we were eating the last course."
    "And when the turkey emerges, it looks to be one of the biggest I've ever seen!"










    show sasha annoyed
    sasha.say "You remembered the cranberry sauce, right?"
    sasha.say "Please tell me somebody remembered the cranberry sauce!"
    "Once the turkey takes pride of place on the table, there's an awkward pause."
    "And then I realise that, for some reason, everyone's looking at me!"
    bree.say "Erm..."
    bree.say "What's going on?"
    bree.say "Why are you all staring at me like that?"
    show mike happy
    mike.say "We're waiting for you to carve the turkey, of course!"
    show sasha normal
    sasha.say "Not because you're the mom of the house or anything - it's just I don't trust [mike.name] to do it!"
    show mike annoyed
    mike.say "Hey!"
    mike.say "That's not what you told me!"



    "All I can do is shrug as I pick up the knife and fork."
    show xmas diner breemc mike sasha with fade
    "If they want me to man up and carve the turkey, then so be it."
    "I mean, I've never done it before in my entire life."
    "But how hard can it be?"
    "I'm just cutting flesh off the carcass of a dead bird, right?"
    "So after a few false starts, I get into the swing of it."
    "Soon enough I'm doling out slices of freshly cooked turkey to my housemates."





































    "[mike.name] watches eagerly as everyone tucks into their food."
    "He's tried to play things as if she's really not concerned."
    "But it's plain to see that he's hoping everyone likes it."
    "I put a smile on my face as I stuff the turkey into my mouth."
    "But as I begin to chew, there's just no way I can keep it up."
    mike.say "What's the matter, [hero.name]?"
    mike.say "It's the aftertaste of the starters, right?"
    mike.say "You just need a little more gravy to wash it down?"
    "I force myself to swallow, feeling my eyes water at the effort."
    "Then I gasp for breath and shake my head."
    bree.say "Oh wow..."
    bree.say "That was...that was..."
    sasha.say "GROSS!"
    sasha.say "That's so gross, [hero.name]!"







    "[mike.name] shakes his head as he looks around the table."
    "But everywhere he sees people reacting badly to his cooking."
    mike.say "I...I don't understand!"
    mike.say "I looked up cooking a turkey on the internet!"
    mike.say "I must have watched a thousand tutorial videos!"
    bree.say "It's okay, [mike.name], really."
    bree.say "What matters is that you tried your best."
    "[mike.name] nods at my attempts to reassure him."
    "But I can see that he's really upset."
    "I guess I'll have to think of some way to make him feel better."
    scene bg black with dissolve
    pause 1

label home_christmas_party_female_03:
    $ game.pass_time(1)
    scene bg livingroom
    show mike casual normal at left
    show sasha casual normal at right
    with dissolve
    "Once the last of the Christmas dinner has been finished off, I feel like a beached whale!"
    "Oh mu goodness, there's going to be a queue for the bathroom and no mistake."
    "We're also going to be eating left-over turkey well into the New Year, and the thought terrifies me."
    "But right now I'm gearing up for the inevitable argument over who gets lumbered with washing the dishes."
    "It was always a big deal back home until Mom blackmailed Dad into buying a dish-washer."
    "And I've memorised my own list of excuses in the hope that they'll be enough..."
    show mike happy
    mike.say "Okay, guys - now it's time to sing some carols!"
    show sasha happy
    sasha.say "Gather round and we can all sing together!"
    sasha.say "[hero.name], what's your favourite carol?"
    "At the mere mention of Christmas Carols I feel terror rising inside of me."
    "What the hell is going on here?!?"
    "We're not in a damn church!"
    "My dad always used to say that you shouldn't let religion get in the way of Christmas!"
    "And he never let us sing carols either, which means I don't know many of them either."







    "I look this way and that, unable to believe what I'm hearing."
    "We just ate a massive Christmas dinner."
    "The only tradition I know about is sitting on my ass and playing videogames!"
    "But it looks like everyone else is suddenly obsessed with the idea of singing."
    bree.say "Urgh..."
    bree.say "I suppose we could sing a few quick carols."
    bree.say "So who's going to get things started?"
    show mike casual normal at left
    show sasha casual normal at right

























    "Suddenly the mood in the room seems to undergo a change."
    "A second ago all of them were eager to get singing."
    "But now none of them are stepping up to the plate!"
    "So I let out a sigh of frustration and get to my feet."
    bree.say "Okay...okay..."
    bree.say "I see where this is going!"
    bree.say "And for the record, it's not fair!"
    bree.say "I'll sing the first carol."
    bree.say "But after that, I'm off the hook until next year!"
    "I rack my brains to remember a carol that I can reel off."
    "And in the end I settle on the one about the king looking out of his window."
    show xmas singing singbreemc mike mike_annoyed sasha sasha_annoyed with fade
    "I clear my throat and launch into the carol, giving it all I've got."
    "And it doesn't take long for me to get a reaction."
    mike.say "Oh no - I think my ears are bleeding!"
    sasha.say "Whoa...way to murder a classic!"



    "Once I come to the end of the carol, I glare at the lot of them."
    "First they make me sing the damn song, then they complain about it!"
    "There really is no pleasing some people!"
    "But at least that's over until next Christmas."
    scene bg black with dissolve
    pause 1

label home_christmas_party_female_04:
    $ game.pass_time(1)
    scene bg livingroom
    show mike casual normal at left
    show sasha casual normal at right
    with dissolve
    "As soon as we're done with the torture of singing, I get the creepy feeling that I'm being watched."
    "And all it takes is a quick glance around the room to prove that I'm right in my suspicions."
    "Everyone is staring at me with expectant looks on their faces, like they're waiting for something."
    bree.say "Erm..."
    bree.say "Guys...what's up?"
    bree.say "You're kind of making me nervous!"
    bree.say "Come on now - why are you all looking at me like that?!?"
    "I hear a chorus of gasps and looks of surprise are exchanged before me."
    show mike shout
    mike.say "The pudding!"
    mike.say "Don't tell me you've forgotten?!?"
    sasha.say "No excuses!"
    sasha.say "I want my Christmas pudding!"






    "Of course, I'd agreed to handle the last course of the meal - the pudding!"
    scene bg kitchen with fade
    "Without another word, I race into the kitchen to discharge my responsibilities."
    scene bg livingroom
    show mike casual normal at left
    show sasha casual normal at right
    with fade
    "And it doesn't take long for the others to begin showing an interest in my progress."
    "I do the best I can to ignore their comments and focus on the task at hand."
    "But the truth is that I'm hoping they'll be pleased with what I serve up."
    show mike happy
    mike.say "Ooh...that smells good!"
    sasha.say "This better be worth the wait!"



    "I smile as I dole out a portion of the pudding for everyone."
    "Then all I can do is hand them over and wait."
    "And with all the eager spoonful's being swallowed, I soon get a reaction."
    "So I lean in close, hoping to hear only good things."
    show mike casual normal at left
    show sasha casual normal at right
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
        show mike happy
        mike.say "[hero.name]..."
        mike.say "That was SO good!"
        mike.say "Erm...there wouldn't be any more, would there?"
        show sasha happy
        sasha.say "I never tasted pudding like that before!"
        sasha.say "There's got to be second helpings, right?"






        "I can hardly believe the chorus of praise I'm hearing."
        "And I fetch the last of the pudding without saying a word."
        "But when I get back to the table, it's snatched out of my hands!"
        "I watch as everyone literally fights over the last of the pudding."
        "And all I can do is stand back and shake my head in amazement."
        "Maybe I'm better at this cooking thing than I thought?"
    else:
        "Soon I see their eyes open and bulging."
        "And I try to chalk that up to the pudding being hot."
        "But then first mouthfuls have been swallowed with some effort."
        "And once their mouths are empty, I begin to get my feedback."
        show mike surprised
        mike.say "Urgh..."
        mike.say "Help me, please!"
        mike.say "I feel like I've swallowed a bowling ball!"
        show sasha surprised
        sasha.say "Oh man..."
        sasha.say "Wow...that was bad!"
        sasha.say "Like, really bad!"









        "I look up from my own bowl, disbelief written all over my face."
        "I tried my hardest to whip up that pudding!"
        "The least they could do is pretend to like it!"
        bree.say "Hey!"
        bree.say "That thing took me ages to cook!"
        bree.say "And it was my first time too!"
        "But for all of my protests, I'm sure it'll be my last."
        "Everyone is pushing their bowls away in disgust."
        "And more than one face around the table looks a little green too!"
        "Maybe I should cut my losses and leave the cooking to someone else?"
    scene bg black with dissolve
    pause 1

label home_christmas_party_female_05:
    $ game.pass_time(1)
    scene bg livingroom with dissolve
    "Now we really are done eating and nobody wants to hear another damn carol."
    "That means we can get down to the serious side of the holiday season."
    "You know, the part of it that really matters?"
    "The thing that Christmas is really all about?"
    "And, of course, by that I mean swapping presents!"
    "Everyone's been eyeing up the neatly-wrapped packages under the tree."
    "Trying to sneak a look at the labels when they think nobody else is looking."
    "But now, as we all gather around in the sitting room, I'm starting to feel nervous."
    "I'm always worried that the gifts I've chosen for people are going to be wrong somehow."
    "I try really hard to pick something that I think they'll love."
    "But sometimes it just doesn't seem to turn out how I'd hoped!"
    "As people start picking up the gifts and checking the labels, I cross my fingers."
    "Hopefully this year I've been able to pick the right gift for the right friend."

























































































































































































































































    show mike close casual happy
    mike.say "Here you go, [hero.name]!"
    mike.say "You have to open my gift first!"
    "[mike.name] almost leaps atop me as he thrusts his gift in my face."
    "He's like a kid on a massive sugar-rush right now."
    "But the expression on his face makes me smile at his enthusiasm."
    "I mean, who doesn't want to indulge a cute guy bearing gifts?"
    bree.say "Sure thing, [mike.name]!"
    bree.say "I can't wait to see what you got me..."
    play sound [paper_ripping_1, paper_ripping_2]
    if mike.is_boyfriend:
        "I hastily tear open the wrapping paper to reveal [mike.name]'s gift."
        "But I've already guessed from the size and shape what it has to be."
        "And I'm right, it's a game for the Z-Box!"
        bree.say "Aw, thanks, [mike.name]!"
        bree.say "It's...it's...'JIM'S EARTHWORM'?!?"
        bree.say "I...I never even knew this game existed!"
        "[mike.name]'s cheeks are already flushing red."
        "And I can feel mine starting to do the same too!"
        show mike close blush
        mike.say "I...I know it's a little bit dirty..."
        mike.say "You know - buying you an adult videogame..."
        mike.say "But it looked really fun too!"
        bree.say "No need to apologise, [mike.name]."
        bree.say "I love it!"
        bree.say "And we can have so much fun playing it together too!"
        show mike close happy
        "[mike.name] smiles, delighted with my reaction."
    else:
        "I hastily tear open the wrapping paper to reveal [mike.name]'s gift."
        "But I've already guessed from the size and shape what it has to be."
        "And I'm right, it's a game for the Z-Box!"
        bree.say "Aw, thanks, [mike.name]!"
        bree.say "It's 'Immortal Wombat' - the remastered edition too!"
        bree.say "I can't wait to kick some mutant marsupial ass!"
        "[mike.name] smiles, delighted with my reaction."
        mike.say "I'm glad you like it."
        show mike close normal
        mike.say "But you've got to let me play too!"
    "Now it's my turn to return the favour and give [mike.name] my gift."
    "I snatch it up from under the table and hand it over to him."
    show mike happy
    play sound [paper_ripping_1, paper_ripping_2]
    "[mike.name] looks delighted as he begins to unwrap his gift."
    menu:
        "Offer style clothes":
            show mike close normal
            mike.say "It's something to wear!"
            mike.say "It's...it's..."
            show mike close upset
            mike.say "Oh...it's a tracksuit!"
            "I see the disappointment on [mike.name]'s face."
            "But I'm ready to jump in and make the save."
            bree.say "Read what's printed on the back, [mike.name]!"
            mike.say "Oh..."
            show mike close surprised
            $ mike.love += 2
            mike.say "It says 'Number One Gamer Guy'!"
            $ mike.love += 1
            mike.say "And it has my name printed on it too!"
            bree.say "Yeah, think of it more as something to wear around the house, [mike.name]!"
            bree.say "While you're hanging out and playing videogames."
            show mike close happy
            "[mike.name] nods with enthusiasm and then gives me a hug."
            "Which I choose to take as proof I made the right choice."
        "Offer gym clothes":
            show mike close normal
            mike.say "It's something to wear!"
            mike.say "It's...it's..."
            show mike close upset
            mike.say "Oh...it's a tracksuit!"
            "In my enthusiasm, I totally miss the disappointment in [mike.name]'s tone."
            "Instead I plough straight on, trying to explain the logic behind the gift."
            bree.say "Yeah, [mike.name], a tracksuit!"
            bree.say "I figured you spend too much time on the Z-Box."
            bree.say "So this should motivate you to get up off of your ass, yeah?"
            show mike close angry
            $ mike.love -= 3
            mike.say "What are you trying to say?"
            mike.say "That I'm getting fat?!?"
            bree.say "Well..."
            bree.say "You are starting to look a little plump!"
            show mike close annoyed
            "All I can do is shrug helplessly as [mike.name] rolls his eyes."
            "Well, that could have gone better..."

    scene bg livingroom
    show sasha close casual happy
    sasha.say "Open mine next!"
    sasha.say "I can't wait for you to see what it is!"
    "I nod as Sasha shoves her gift into my hands."
    "I'm almost as eager to unwrap it as she is to see me do it!"
    "After all, she looks so cute when she's this enthusiastic."
    "It's not a large gift, but that's not really a problem."
    "It's the thought that counts."
    bree.say "Okay, Sasha, okay!"
    bree.say "Let me open the damn thing already!"
    play sound [paper_ripping_2, paper_ripping_2]
    if sasha.is_girlfriend:
        "I make quick work of tearing open Sasha's gift."
        "And I'm left holding a small remote control."
        "It doesn't look familiar and I have no idea what it's for."
        "I look at Sasha in the hope she's going to help me out."
        show sasha close normal
        sasha.say "It's a remote control."
        bree.say "Ah, yeah, Sasha..."
        bree.say "I kind of worked that out for myself!"
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
        bree.say "Oh..."
        bree.say "Thanks, Sasha..."
        show sasha close normal
        "Sasha seems to sense the surprise her gift has inspired."
        "And she wastes no time in jumping in to explain herself."
        sasha.say "You're always losing your keys, yeah?"
        sasha.say "So I figured you could use one of those things."
        show sasha close happy
        sasha.say "Should make it so much easier to find them, huh?"
        bree.say "Yeah, Sasha, I guess so!"
    "I don't waste any time in grabbing my gift for Sasha."
    "I hand it straight over to her with a smile on my face."
    play sound [paper_ripping_2, paper_ripping_1, paper_ripping_2]
    "Nodding my head for her to take it and tear off the paper."
    menu:
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
            bree.say "No, Sasha - it's a real amp."
            bree.say "Just a smaller one, so you can take it anywhere!"
            hide fx
            show sasha close surprised
            $ sasha.love += 3
            sasha.say "Which means I can practice anywhere too!"
            bree.say "Exactly!"
            show sasha close happy
            "Sasha and I are both beaming right now."
            "But I can see that not everyone in the room feels the same way."
            "I can't blame them, as Sasha's notoriously loud when she practices."
            "But I'm enjoying basking in her approval far too much to care!"
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
            bree.say "They're for when you play guitar, Sasha."
            show sasha close vangry
            $ sasha.love -= 3
            sasha.say "But I need to be able to hear myself play!"
            bree.say "I know - but nobody else does!"
            bree.say "They're for you to hand out to the rest of us!"
            show sasha close angry
            "Sasha glares at me, shaking her head in disbelief."
            "And all I can do is offer her an apologetic smile as I cringe away."
    scene bg livingroom
    show mike casual happy at left
    show sasha casual happy at right
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
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
