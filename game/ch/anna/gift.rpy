init python:
    Consumable("guitar_practice_book", display_name="Great bands of History", label="guitar_practice_book", uses=10)

    Event(**{
    "name": "anna_give_a_gift",
    "label": "npc_give_a_gift",
    "conditions": [
        Or(
            HeroTarget(IsBirthday()),
            IsSpecialDate("christmas"),
            IsSpecialDate("valentine"),
            ),
        PersonTarget(anna,
            IsPresent(),
            Not(IsHidden()),
            ),
        ],
    "girl": "anna",
    "once_day": True,
    "do_once": False,
    "quit": False,
    }
    )

label anna_give_male:
    if "guitar_practice_book" not in hero.inventory:
        $ gift = "guitar_practice_book"
        "She hands me a pretty large book."
        mike.say "Wow!\nIs that a book with guitar tricks?"
        anna.say "It sure is..."
        mike.say "Thank you so much."
    else:
        $ gift = "cake"
        "She hands me box, obviously from a pastry shop."
        mike.say "Thanks."
    $ hero.gain_item(gift)
    return

label anna_give_valentine_male:
    "Anna walks hesitantly towards me."
    call anna_greet from _call_anna_greet_7
    show anna blush
    anna.say "Happy valentine's day [hero.name]..."
    "Anna hands me a box of chocolates."
    mike.say "Thank you, Anna."
    $ hero.gain_item("valentine_chocolates")
    return

label anna_give_birthday_male:
    "Anna walks towards me."
    call anna_greet from _call_anna_greet_8
    show anna happy
    anna.say "Happy birthday [hero.name]!"
    call anna_give_male from _call_anna_give_male
    return

label anna_give_christmas_male:
    "Anna walks towards me."
    call anna_greet from _call_anna_greet_9
    show anna happy
    anna.say "Merry Christmas [hero.name]."
    call anna_give_male from _call_anna_give_male_1
    return

label anna_birthday_gift_male:
    show anna
    if anna.flags.birthdayknown:
        mike.say "Happy birthday Anna."
        anna.say "How sweet, you remembered my birthday!"
    else:
        anna.say "How do you know my birthday?"
        mike.say "I didn't, it's just pure luck."
        $ anna.flags.birthdayknown = True
    return

label anna_gift_collar_male:
    show anna
    "I can feel my mouth going dry, and I swallow almost painfully."
    "This is it - I either find the courage to do it now, or I baulk and come up with some pathetically lame excuse."
    "Hoping that it'll take a little of the attention off of me and make saying what I have to say easier, I whip out the box from behind my back."
    anna.say "Oh, wow, [hero.name]!"
    anna.say "Is...is that for me?"
    "The box clutched in my outstretched hands is about four inches on a side and maybe two or three tall."
    "That it's a gift is made obvious by the fact it's a pink that matches Anna's hair, and tied with a black ribbon in a bow."
    "I hand the box over to Anna, offering a weak smile in response to the beaming one that's currently splitting her face in two."
    mike.say "Yeah, Anna."
    mike.say "I...wanted to get you something nice."
    mike.say "Something that I think symbolises where our relationship is going right now."
    "This last statement seems to make Anna's ears prick up all the more."
    "The obvious thing to expect might have been a ring, followed by me getting down on one knee and making a proposal."
    "But the box is way too big for that, and so I can see that it's making her all the more intrigued to discover just what's inside."
    anna.say "Aww, thanks, [hero.name]!"
    "Anna says this as she tugs at the ribbon and starts to yank the lid off of the box."
    anna.say "It's really sweet of you."
    anna.say "But you didn't have to get me a...COLLAR?!?"
    "From the look of surprise on Anna's face as she holds up what was in the box, I sense a chance to jump in."
    "Strangely the fact that she's now the one on the back-foot makes me feel more confident in saying what I have to say."
    mike.say "Don't worry, it should fit real snug."
    mike.say "I had it made to your measurements and it's a one-off too."
    mike.say "That didn't come from any pet shop, it was made just for you!"
    "The collar itself is a choker of silvery metal, lined with soft leather and with a loop on the front for a leash."
    "I wasn't lying about the quality of it either - it really was made just for Anna, and as such, it wasn't cheap either!"
    mike.say "You're my favourite little pet, Anna."
    mike.say "And with this collar around your neck, everyone will know that you belong to me!"
    if anna.sub < 90:
        show anna annoyed
        $ anna.love -= 20
        "I can't say any more than that, as Anna suddenly shoves the collar and box back at me."
        "In fact, she does so with such force that they hit me in the gut, making me gasp for air."
        mike.say "Anna...can't...breathe!"
        anna.say "Funny, because I thought something already cut off the oxygen supply to your brain!"
        anna.say "How else could you be so stupid?!?"
        "Still trying to catch my breath, I look at her with a dumbfounded expression on my face."
        mike.say "Are you...trying to say...you don't...like it?"
        anna.say "Is it that obvious?"
        anna.say "Of course I don't like it, you jerk!"
        anna.say "I thought I was your girlfriend."
        anna.say "But all this time you wanted me to be your...what - your dog?!?"
        "With that, Anna turns her back on me, shaking her head as she walks away."
        "I reach out, trying to plead with her to wait."
        "But I'm still pretty badly winded, and she's gone before I can even stand up straight."
        $ hero.cancel_activity()
    elif not anna.love >= 100:
        show anna annoyed
        $ anna.love -= 10
        anna.say "Okay...that's not at all weird and creepy!"
        anna.say "Is it, [hero.name]?"
        "I shake my head, sensing that she's looking to me for reassurance."
        mike.say "Of course not, Anna."
        mike.say "Sure, it LOOKS like a dog collar."
        mike.say "But it was made for a person to wear."
        mike.say "Trust me, the nightclubs in town are full of people wearing them!"
        "Anna turns the collar over in her hands, looking like she's not totally convinced."
        anna.say "Well, it is made of metal."
        anna.say "And I do like heavy metal..."
        mike.say "You don't have to put it on now."
        mike.say "Why not take it home with you and try it on there?"
        "Anna nods slowly, putting the collar back into the box and replacing the lid."
        "Sure, it might not have been an instant hit."
        "But the important thing is that she didn't say no straight away."
        "And the idea's been planted in her head, where it'll have time to take root and grow."
        $ hero.cancel_activity()
    else:
        show anna happy
        anna.say "OH WOW!"
        anna.say "[hero.name] - this is so cool!"
        "I'd been so ready for this whole thing to blow up in my face, her response take me by complete surprise."
        mike.say "It...it is?!?"
        anna.say "Of course it is, silly!"
        anna.say "I thought for a minute that you'd got me something small."
        anna.say "Like a crappy little ring that nobody's gonna see or something."
        anna.say "But there's no way anyone'll miss seeing this!"
        anna.say "Put it on me...quick!"
        $ anna.set_sex_slave()
        "I hurry to oblige, all fingers and thumbs as Anna giggles and claps in delight."
        hide anna
        show anna close blush at bottom_to_top
        "Once the collar is fastened around her neck, she adopts the pose of a begging puppy."
        "With her hands held up and her huge eyes staring up at me, she practically pouts."
        anna.say "Well, how do I look...Master?"
        "I can only gulp, suddenly feeling very exposed and self-conscious."
        mike.say "Erm...maybe we should...go somewhere else, Anna?"
        mike.say "Like somewhere more private?"
        "Anna cocks her head on one side and leans in closer still."
        anna.say "Sure thing, Master."
        anna.say "Does this thing come with a leash?"
    hide anna
    return

label anna_gift_butt_plug_male:
    show anna happy
    anna.say "Oh, [hero.name], is it for me?"
    "She unwraps the butt plug."
    show anna blush
    anna.say "It's so pretty, thank you [hero.name], I love it."
    $ anna.flags.buttplug = True
    return

label anna_gift_swimsuit_male:
    show anna happy
    anna.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy swimsuit."
    if anna.sub >= 60:
        show anna blush
        anna.say "It's so pretty, thank you [hero.name]."
        $ anna.flags.sexyswimsuit = True
    else:
        show anna angry
        $ anna.love -= 10
        anna.say "Thanks but no thanks [hero.name]."
        anna.say "You think I would wear that?"
        $ hero.cancel_activity()
    return

label anna_gift_sexy_dress_male:
    show anna happy
    anna.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy dress."
    if anna.sub >= 30:
        show anna blush
        anna.say "Thank you [hero.name]."
        $ anna.flags.sexydate = True
        $ anna.flags.sluttydate = False
    else:
        show anna annoyed
        $ anna.love -= 4
        anna.say "Thanks but no thanks [hero.name], I would feel very awkward with that..."
        $ hero.cancel_activity()
    return

label anna_gift_slutty_dress_male:
    "I've been nervously hiding a certain box behind my back for a few minutes now."
    "So much so that I can feel my arms starting to go numb from the effort."
    "And that means this is as good a time as any to spring my surprise on Anna."
    "But when I whip it out a moment later, I'm surprised that it's to no reaction."
    "Instead of leaping into the air and squealing with joy, Anna doesn't even seem to notice."
    mike.say "Erm..."
    mike.say "Anna?"
    "Anna answers me promptly, but without bothering to look up."
    show anna talkative
    anna.say "Yeah, [hero.name]?"
    anna.say "Wassup?"
    show anna normal
    mike.say "I..."
    mike.say "Well, I have something to show you."
    mike.say "Something I think you're going to like."
    "I see Anna's brows furrow at this."
    show anna angry
    anna.say "Come on, [hero.name]..."
    anna.say "I'm not that dumb!"
    anna.say "So put it back in your pants and stop messing around, yeah?"
    show anna annoyed
    "Already beginning to blush, I do all I can to reassure Anna."
    "Practically shoving the box under her nose as I do so."
    mike.say "No, no, no!"
    mike.say "It's a nice surprise - look!"
    "Finally Anna seems to catch on, and her mood instantly changes."
    "Now she's all smiles as she eagerly takes the box from me."
    show anna surprised
    anna.say "Ooh!"
    anna.say "A present?"
    anna.say "For me?"
    show anna normal
    play sound [paper_ripping_1, paper_ripping_2]
    "I nod happily as I watch Anna tear the thing open."
    "And as she pulls out the daring dress from inside of it, I wait to see her reaction."
    if anna.sub >= 70:
        show anna happy
        "Anna suddenly presses the dress to her not insignificant bosom."
        "Pressing it against her chest as though she's hugging it for all she's worth."
        mike.say "So..."
        mike.say "I'm guessing that you...like it?"
        "Anna can't keep from nodding as she beams at me."
        show anna talkative
        anna.say "Of course I do, silly!"
        anna.say "What girl wouldn't want a dress as sexy as this?"
        anna.say "And it's going to look so good once I'm in it too!"
        show anna happy
        "I feel a flood of genuine relief sweep over me."
        "So much so that I swear I almost swoon for a second."
        mike.say "Oh that's a relief!"
        mike.say "I just had to buy the dress when I saw it, Anna..."
        mike.say "Or to be more honest, the moment I thought of you in it!"
        "Anna stops pouring over the dress long enough to look meet my gaze."
        "And when she does so, I can see a spark of mischief in her eyes."
        show anna evil
        anna.say "Oh, just you wait and see!"
        anna.say "The real thing is going to be so much better."
        anna.say "I'd never have bought myself something like this, [hero.name]."
        anna.say "I don't think I'd have had the courage."
        anna.say "So it's only fair I reward you for thinking of me..."
        show anna happy
        $ anna.flags.sexydate = False
        $ anna.flags.sluttydate = True
    else:
        "Anna stares at the dress for a moment, shaking her head."
        show anna annoyed
        "And then she surprises me by handing it straight back."
        "I hurry to take it, remembering how expensive the thing was."
        "But at the same time I'm struggling to understand why."
        mike.say "What's wrong, Anna?"
        mike.say "Did I get the wrong size?"
        show anna angry
        anna.say "No, [hero.name]..."
        anna.say "You got the wrong girl!"
        show anna annoyed
        "I'm blinking and shaking my head too by now."
        "Totally thrown by what Anna's telling me."
        mike.say "What do you mean?"
        mike.say "I thought you'd look amazing in this!"
        show anna angry
        anna.say "Seriously, [hero.name]..."
        anna.say "When have you ever seen me in something like that?"
        anna.say "It's, like, totally not in keeping with my image!"
        show anna annoyed
        "All I can do is nod my head in agreement as Anna lectures me."
        "Because I don't want to argue, and in doing so cause more damage."
        "I already managed to screw up pretty badly."
        "And the last thing I want is to make things worse."
        $ anna.love -= 10
        $ hero.cancel_activity()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
