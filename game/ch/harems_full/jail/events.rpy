init python:
    InteractActivity(**{
    "name": "camila_kylie_propose",
    "display_name": "Propose to Kylie and Camila",
    "icon": "askmarry",
    "conditions": [
        InInventory("wedding_ring"),
        HeroTarget(
                IsGender("male"),
                HasRoomTag("policestation"),
                ),
        PersonTarget(kylie,
            Not(IsHidden()),
            IsActive(),
            IsFlag("schedule", "jail"),
            HasRoomTag("policestation"),
            Not(IsActivity("sleep")),
            IsFlag("engagedmike", False),
            IsFlag("nopropose", False),
            MinStat("love", 160),
            ),
        PersonTarget(camila,
            Not(IsHidden()),
            HasRoomTag("policestation"),
            Not(IsActivity("sleep")),
            IsFlag("engagedmike", True),
            ),
        ],
    "label": "camila_kylie_propose",
    })


label camila_kylie_propose_male:
    scene expression "bg [game.room]"
    "It's weird that visiting time at the prison's become such a part of my daily routine."
    "When Kylie was convicted and sent down, part of me thought that would be the end of it."
    show camila normal at right with dissolve
    "And I was almost certain that it'd turn Camila totally against her too."
    "But oddly it seems to have had the opposite effect, making the bond between the three of us stronger."
    "Somehow all of the madness and insanity coming out means we've seen Kylie for who she really is."
    "And we've actually found that we're totally in love with the girl in the middle of it all."
    "Also, it's not like Kylie's turned into a ravening monster now she's behind bars."
    "She actually seems sorry for what she's done, willing to make amends too."
    "And I can't help thinking about what we could have done differently."
    "Like, maybe if we'd been a better partners to her, if we'd listened to her more."
    "Then maybe we could have spotted the signs and saved her from doing what she did."
    "That's why we're resolved to do whatever I can for her now."
    "We want to make sure Kylie and I have a future together."
    "We want to prove to her that we'll always be there at her side."
    "So the next time we go to the prison at visiting time, Camila and I are on the same page."
    "We exchange a nod as we walk in there, and then we wait for what feels like the right moment."
    "When it comes, I pull out the ring I've been clutching in my pocket."
    "Then we get down on one knee in front of Kylie's cell door."
    show kylie annoyed with dissolve
    kylie.say "Wh...what's happening?"
    kylie.say "[hero.name], Camila..."
    show kylie normal
    kylie.say "What are you doing?"
    mike.say "I've wanted to do this for a long time, Kylie."
    camila.say "Me too - we both have."
    mike.say "I want tell you that I love you."
    camila.say "Same here, Kylie - I'm crazy about you!"
    mike.say "That we'll always be there for you."
    mike.say "So...will you marry us?"
    camila.say "Say yes, Kylie - please!"
    show kylie surprised
    "Kylie looks shocked, like she can't believe what's happening."
    "And that means I genuinely can't read the expression on her face."
    "But luckily for me, it doesn't take long for her to recover."
    if kylie.love >= 195:
        "Kylie nods her head eagerly, holding out her hand."
        "And I don't hesitate to take the chance."
        "I slide the ring onto her finger without hesitation."
        show kylie happy
        kylie.say "Oh, [hero.name], Camila!"
        kylie.say "I thought you'd never ask me to marry you."
        kylie.say "Not after everything that I've done."
        "As Kylie's nodding her head, we're shaking ours."
        mike.say "God no, Kylie!"
        show camila happy
        camila.say "No way!"
        mike.say "All that stuff..."
        mike.say "It just made me realise how much I love you."
        camila.say "It wasn't your fault, Kylie."
        camila.say "It was a cry for help."
        mike.say "It made me want to try all the harder to be with you."
        camila.say "And I never thought I'd feel this way about a felon!"
        mike.say "I want to build a life for the three of us."
        camila.say "Come on, Kylie - say you're into it!"
        "I'm not prepared for what happens next."
        "Kylie reaches through the bars and grabs me with one hand, Camilla with the other."
        "She pulls us bodily against the cell door, almost knocking the wind out of me."
        "But I hardly have time to grunt in pain before she clamps her lips onto mine."
        "I'm pretty sure that we shouldn't be doing this right now."
        "But I can't bring myself to pull away from her."
        "Instead I return the kiss with what I hope is a similar level of passion."
        "Camilla gets in on the act too, and we swap between the three of us."
        "A moment later I hear the door opening behind me."
        "I know that it's one of the guards, coming in to break it up."
        "So I pull back and break off the kiss."
        "And Camila does the same too."
        "There's just enough time to say goodbye to Kylie."
        "And then we're ushered out of the door and away."
        "My head's spinning from what just happened."
        "What I need is time to get my thoughts straight."
        "But visiting time will come round again soon enough."
        "And then Kylie, Camila and I can really start planning where we go from here."
        $ kylie.set_fiance()
        $ Harem.join_by_name("jail", "camila", "kylie")
    else:
        "Kylie shakes her head and begins to back away from us."
        show kylie annoyed
        "And she doesn't stop until she's literally backed up to the far wall."
        "This leaves us clinging to the bars of the cell door, trying to figure out what's happening."
        camila.say "Kylie!"
        show camila annoyed
        mike.say "What's wrong?"
        mike.say "Are we going too fast for you?"
        camila.say "Yeah, Kylie - it's a lot to take in."
        mike.say "Because you don't have to say yes or no right now."
        mike.say "If you want to take your time, we can wait for an answer."
        camila.say "Sure thing - we can wait."
        kylie.say "No, no, no!"
        $ kylie.love -= 25
        $ kylie.sub -= 25
        kylie.say "You can't ask me to do that, [hero.name]!"
        show kylie cry
        kylie.say "I have to be punished - don't you understand?!?"
        mike.say "What are you talking about, Kylie?"
        mike.say "You're in jail for what happened."
        mike.say "Isn't that your punishment?"
        camila.say "Trust me, I know how these things work."
        camila.say "Almost anyone can be rehabilitated!"
        mike.say "Camila's right, Kylie."
        mike.say "I want us to start planning our life together!"
        kylie.say "No, that can't happen!"
        show kylie angry
        kylie.say "I tried to make it work, [hero.name]."
        kylie.say "But it all ended in disaster."
        kylie.say "We can't save something that's been ruined."
        "I open my mouth to argue, to plead with Kylie."
        "But she cuts me off, shouting and looking past me."
        kylie.say "GUARD...GUARD!"
        kylie.say "I want to be alone now!"
        kylie.say "I want them to leave!"
        "I stand up and put the ring away as the guards come in."
        "Camila does the same, more than used to this kind of thing."
        "And neither of us protest when they kindly but firmly ask us to leave."
        hide kylie with dissolve
        "My head's spinning from what just happened."
        "What I need is time to get my thoughts straight."
        "And the inside of a prison isn't the place to do that."
        "For her part, Camila looks like she's handling it."
        "But I know how good she is at hiding her emotions."
        "So I'll just have to wait and see how she really feels."
    scene bg black with dissolve
    return

label camila_kylie_male_ending:
    $ game.hour = 16
    $ game.room = "church"
    scene bg church wedding with fade
    "I feel like my life has been a non-stop rollercoaster ride ever since Camila and Kylie came along."
    "One minute I'm dating a cute girl that seems a little intense and seeing tough female cop on the side."
    "The next the cute girl turns out to be pretty crazy, and the cop is helping to have her arrested!"
    "But the craziest thing of all is how it turned out in the end."
    "The most I expected was for Kylie to end up in an insane asylum."
    "For Camila to get a promotion and forget all about my sorry ass."
    "And for me to end up all alone, nursing the physical and emotional scars from it all."
    "Yet here we are, the three of us admitting that we love each other."
    "Making a genuine commitment to spend the rest of our lives together!"
    "I still can't quite believe that I'm standing at the alter right now."
    "That I'm waiting for Camila and Kylie to come walking down the aisle!"
    "I risk a quick glance over my shoulder, surveying the crowd."
    "And it doesn't take much to spot who's here for who."
    "Kylie and I have our relatives and friends looking on."
    "Even Kylie's sister, and my own ex Alexis is here."
    "But almost all of Camila's guests are obviously cops."
    "Sure, they're out of uniform for the ceremony."
    "But they all still have that unmistakable cop look about them."
    "Suddenly music begins to play, and all heads turn to look backwards."
    "I do the same, straining to see Camila and Kylie as they enter the chapel."
    show camila wedding normal at center, zoomAt (1.0, (400, 740))
    show kylie wedding normal at center, zoomAt (1.0, (880, 740))
    with dissolve
    "I hardly hear the music as they come into view."
    "And that's because the sight of them takes my breath away."
    "Camila normally looks tough and uncompromising."
    "But the dress she's in somehow reveals her true beauty."
    "And I don't think I've ever seen her looking so good."
    if camila.is_visibly_pregnant:
        "She's practically glowing too."
        "Holding her swelling belly with pride."
        "Almost like she's challenging anyone to say they have a problem with it."
    "Kylie's a sight to behold too."
    "That long, blonde hair and the amazing figure!"
    "And in a wedding dress, she's just breath-taking."
    "Luckily the dress is also long enough to cover the electronic tag on her ankle."
    "Which is a constant reminder of the fact that she's still serving her prison sentence."
    "And she'll have to go back there almost as soon as the ceremony is over."
    if kylie.is_visibly_pregnant:
        "But Kylie seems more interested in showing off her belly."
        "In fact I can see how much pride being visibly pregnant gives her."
        "Because it's a visual display of the bond between us all."
    show camila wedding happy at center, zoomAt (1.75, (440, 1200))
    show kylie wedding happy at center, zoomAt (1.75, (840, 1200))
    with dissolve
    "Camila and Kylie join me at the altar."
    "And before we can say a word, the priest beats us to it."
    "Priest" "Dearly beloved..."
    show camila normal
    show kylie normal
    "Priest" "We are gathered here today..."
    "Priest" "To join these three people in the bonds of holy matrimony."
    "I honestly don't hear much more of what the priest says."
    "We've walked through the ceremony so many time already."
    "All I can do is look from one of my brides to the other."
    "Just thinking how lucky I am to be doing this!"
    "Priest" "Do you, Camila..."
    "Priest" "Take this man and woman..."
    "Priest" "To be your lawfully wedded partners?"
    show camila happy at startle
    camila.say "I do."
    "Priest" "And do you, Kylie..."
    "Priest" "Also take this man and woman..."
    "Priest" "To be your lawfully wedded partners?"
    show kylie happy at startle
    kylie.say "I do, I do!"
    "Priest" "And finally - do you, [hero.name]..."
    "Priest" "Take these women..."
    "Priest" "To be your lawfully wedded partners?"
    mike.say "You bet I do!"
    "Priest" "Very good..."
    "Priest" "I call upon those here present..."
    "Priest" "That if you know of any reason this may not be so..."
    "Priest" "Speak now, or forever hold your peace!"
    "There's the customary pause and awkward smiles."
    "But part of me is actually worried while we wait."
    "I can imagine gangsters busting in to get revenge on Camila and a gunfight breaking out."
    "Or else a bunch of orderlies rushing through the doors with a butterfly net to catch Kylie."
    "But thankfully none of that happens."
    "Priest" "Then I take great pleasure in pronouncing you married."
    "Priest" "You may kiss the brides!"
    show camila happy zorder 4 at center, zoomAt (2.0, (460, 1340))
    show kylie happy zorder 5 at center, zoomAt (2.0, (820, 1340))
    with hpunch
    "Camila, Kylie and I come together in a three-way embrace."
    "And we share kisses that become more passionate with each second that passes."
    "I know that this will all be over soon enough."
    "That Kylie will have to return to prison."
    "But for now, everything is perfect."
    "And whatever the future holds, I know that we can weather it together."

    scene bg park
    show camila casual at left5
    with fade
    camila.say "Before we get started here, let me state for the record..."
    show kylie casual annoyed at right5
    kylie.say "Oh for heaven's sake, Camila!"
    kylie.say "You're not testifying under oath."
    kylie.say "Take that night-stick out of your ass for once!"
    show camila casual angry at left5, startle
    camila.say "HEY!"
    camila.say "I do not have a night-stick up my ass!"
    show camila flirt
    camila.say "And I seem to remember you letting [hero.name] put one in a certain hole more than once!"
    show kylie surprised at right5, startle
    kylie.say "Whoa, whoa, whoa!"
    show kylie annoyed
    kylie.say "What happens in conjugal visits stays in conjugal visits."
    kylie.say "You know the rules as well as I do!"
    show camila normal
    show kylie normal
    camila.say "Okay, Kylie, okay..."
    camila.say "Weren't we supposed to be talking about life with [hero.name]?"
    camila.say "Like, telling them how great it is."
    camila.say "And glossing over all the stuff that sucks?"
    kylie.say "It's not like we can gloss over the big stuff, Camila."
    kylie.say "Like the fact that I'm still in prison."
    kylie.say "So we should probably just be honest, yeah?"
    show camila annoyed
    camila.say "Urgh..."
    camila.say "You're right, Kylie."
    show kylie sad
    kylie.say "Aww..."
    show kylie normal
    kylie.say "Don't sound so sad, Camila!"
    show kylie happy
    kylie.say "I really wouldn't change anything."
    kylie.say "I mean, I never thought I could be as happy as I am right now."
    show camila normal
    camila.say "Yeah...I guess you're right."
    camila.say "Being married to a non-cop and a convict looks bad on paper."
    show camila happy
    camila.say "But I couldn't imagine being without you and [hero.name]."
    show kylie happy
    kylie.say "Same here, Camila."
    kylie.say "I may still be crazy."
    kylie.say "But at least I know that I'm crazy!"
    show camila normal
    camila.say "Yeah, yeah..."
    camila.say "Being with you guys really made me take a long hard look in the mirror too."


    camila.say "And I'm so glad you guys supported me in staying on the force."
    camila.say "Now I feel like I'm not just pounding the beat for no reason."
    camila.say "I'm doing it to keep [hero.name] safe."
    camila.say "And to make sure the streets are clean for when you get out too!"





    kylie.say "That's what being a family is all about, Camila."
    show camila happy
    kylie.say "Everyone supporting each other."
    if (camila.is_visibly_pregnant or camila.flags.mikeBabies >= 1) and (kylie.is_visibly_pregnant or kylie.flags.mikeBabies >= 1):
        camila.say "You know, I just didn't get that."
        camila.say "Not until Nova, Seren and Alexis came along."
        show kylie happy
        kylie.say "Oh-oh!"
        kylie.say "Those little imps!"
        camila.say "Yeah, yeah..."
        show camila normal
        camila.say "Why don't Nova and Seren ever play with the dolls I buy them?"
        camila.say "All they want is to play cops and robbers!"
        show kylie happy
        kylie.say "Aww!"
        kylie.say "They just want to be like their mommy!"
        show kylie normal
        camila.say "You and [hero.name] are always encouraging them too!"
        camila.say "I just know he wants them to be tomboys."
        camila.say "And they're a bad influence on Alexis too!"
        show camila sad
        camila.say "I hate that you're not there for her, Kylie."
        show kylie happy
        show camila normal
        kylie.say "Don't worry about it, Camila."
        kylie.say "I know that she's in good hands."
        kylie.say "You and [hero.name] love her just as much as I do."
    elif (camila.is_visibly_pregnant or camila.flags.mikeBabies >= 1):
        camila.say "You know, I just didn't get that."
        camila.say "Not until Nova and Seren came along."
        show kylie happy
        kylie.say "Oh-oh!"
        kylie.say "Those little imps!"
        show kylie normal
        camila.say "Yeah, yeah..."
        camila.say "Why don't they ever play with the dolls I buy them?"
        camila.say "All they want is to play cops and robbers!"
        show kylie happy
        kylie.say "Aww!"
        kylie.say "They just want to be like their mommy!"
        show kylie normal
        camila.say "You and [hero.name] are always encouraging them too!"
        camila.say "I just know he wants them to be tomboys."
    elif (kylie.is_visibly_pregnant or kylie.flags.mikeBabies >= 1):
        kylie.say "Especially now that we have little Alexis."
        kylie.say "Because I know that she's safe and sound with you guys."
        show camila sad
        camila.say "Urgh..."
        camila.say "I hate that you're not there for her, Kylie."
        show kylie happy
        show camila normal
        kylie.say "Don't worry about it, Camila."
        kylie.say "I know that she's in good hands."
        kylie.say "You and [hero.name] love her just as much as I do."
    show camila annoyed
    camila.say "Wow..."
    camila.say "We sure chose to make things hard for ourselves, didn't we?"
    show kylie normal
    kylie.say "That's how it looks to people on the outside, Camila."
    kylie.say "You and I both know we only did what was right for us."
    kylie.say "Sure, we're not together right now."
    kylie.say "But one day we will be."
    show camila normal
    camila.say "And we're still a family - no matter what!"
    show camila happy
    camila.say "You, me and [hero.name]."
    camila.say "We stick together until the end."
    show kylie happy
    kylie.say "You got it, Camila!"
    scene bg black with dissolve
    pause 2.0
    $ game.set_new_game_plus()
    $ renpy.full_restart()
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
