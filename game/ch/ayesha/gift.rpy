
label ayesha_birthday_gift_male:
    show ayesha
    if ayesha.flags.birthdayknown:
        mike.say "Happy birthday Ayesha."
        ayesha.say "How sweet, you remembered my birthday!"
    else:
        ayesha.say "How do you know my birthday?"
        mike.say "I didn't, it's just pure luck."
        $ ayesha.flags.birthdayknown = True
    return

label ayesha_christmas_gift_male:
    show ayesha
    mike.say "Merry Christmas Ayesha."
    ayesha.say "Thanks!"
    $ ayesha.love += 2
    return

label ayesha_valentine_gift_male:
    show ayesha
    mike.say "Happy valentine's day Ayesha."
    ayesha.say "Thank you."
    $ ayesha.love += 2
    return

label ayesha_gift_swimsuit_male:
    if ayesha.sub >= 60:
        show ayesha happy
        ayesha.say "Oh thank you so much [hero.name]! It looks so good."
        $ ayesha.flags.sexyswimsuit = True
    else:
        show ayesha angry
        $ ayesha.love -= 4
        ayesha.say "No. I am not wearing that."
        $ hero.cancel_activity()
    return

label ayesha_gift_sexy_dress_male:
    show ayesha happy
    ayesha.say "Oh, [hero.name], is it for me?"
    "She unwraps the sexy dress."
    if ayesha.sub >= 30:
        show ayesha blush
        ayesha.say "Thank you [hero.name]."
        $ ayesha.flags.sexydate = True
        $ ayesha.flags.sluttydate = False
    else:
        show ayesha annoyed
        $ ayesha.love -= 4
        ayesha.say "Thanks but no thanks [hero.name], I would feel very awkward with that..."
        $ hero.cancel_activity()
    return

label ayesha_gift_slutty_dress_male:
    "I'm waiting for the right moment to present Ayesha with the present that I got for her."
    "And obviously I want this to be a surprise - one of the pleasant kind, of course."
    "But the problem is that I keep getting distracted by the very sight of her body in motion."
    "The irony being that the present is something I was inspired to get her for that very reason."
    show ayesha talkative
    ayesha.say "Hey there!"
    ayesha.say "Are you feeling okay?"
    show ayesha normal
    "Suddenly I realise that Ayesha's trying to catch my eye."
    "And she's waving a hand in front of my face too."
    mike.say "Oh..."
    mike.say "Oh yeah..."
    mike.say "Sorry, Ayesha - I was miles away!"
    "Ayesha greets this admission with a knowing grin."
    show ayesha talkative
    ayesha.say "You don't say?"
    ayesha.say "You wouldn't happen to be distracted, would you?"
    ayesha.say "Maybe by what you're hiding behind your back?"
    show ayesha normal
    "All of a sudden I feel myself getting into a panic, as I realise Ayesha's onto me."
    "I've been trying so hard to hide the gift that I've managed to do the exact opposite."
    "And now I find myself struggling to regain my balance and pull it back again."
    mike.say "Okay, Ayesha..."
    mike.say "You got me, I admit it."
    mike.say "I do have a little something for you right here."
    "I hand the giftwrapped box over to Ayesha, who can't hide her excitement."
    play sound [paper_ripping_2, paper_ripping_1]
    "And the I watch with baited breath as she hurries to open it."
    "But once she pulls out the daring dress that's inside, her expression changes."
    "Becoming one of amazement as her eyes struggle to take it all in."
    show ayesha surprised
    ayesha.say "It's..."
    show ayesha stuned
    mike.say "Yes?"
    show ayesha talkative
    ayesha.say "It's..."
    show ayesha normal
    mike.say "It's what?"
    if ayesha.sub >= 70:
        show ayesha surprised
        ayesha.say "It's SO daring!"
        ayesha.say "Do you really think I could pull it off?"
        show ayesha stuned
        "Ayesha's looking me straight in the eye as she asks the question."
        "And I can feel the emotion in her gaze already beginning to pull at my heartstrings."
        "Like she's asking me for the permission she needs to take this massive step forwards."
        mike.say "Ayesha, you really have to ask me that?"
        mike.say "You're the most beautiful woman I've ever met."
        mike.say "You're my Amazon princess - dating you is like being with a fricking superhero!"
        mike.say "You can do anything you put your mind to."
        "By now Ayesha's looking at me with actual fire in her eyes."
        "Holding the dress against her chest like it's become precious to her."
        "Then she begins to nod, as if my words are inspiring her."
        show ayesha blush
        ayesha.say "I..."
        ayesha.say "I never thought I could wear something like this."
        show ayesha flirt
        ayesha.say "But...if you think I can, [hero.name]..."
        ayesha.say "Then I'll do it!"
        show ayesha happy
        "I can't help grinning from ear to ear as Ayesha holds the dress up against herself."
        "Because I can already see just how good it's going to look on her."
        "And the mere thought of all that stuff in motion is almost too much."
        "Making the purchase of the dress more than worth my while."
        $ ayesha.flags.sexydate = False
        $ ayesha.flags.sluttydate = True
    else:
        show ayesha angry
        ayesha.say "It's totally hideous..."
        ayesha.say "That's what it is!"
        show ayesha annoyed
        "Suddenly I feel like I've been slapped in the face."
        "Because I can't believe what Ayesha just said."
        mike.say "But, but, but..."
        mike.say "It's totally stunning, Ayesha."
        mike.say "You'd look amazing in that dress."
        mike.say "Everyone would be looking at you with it on!"
        "Ayesha shakes her head, eyes wide with disbelief."
        show ayesha angry
        ayesha.say "Don't you get it, [hero.name]?"
        ayesha.say "That's the last thing I want."
        ayesha.say "Everyone staring at me, making jokes about how big I am!"
        ayesha.say "Asking me if I'm really a woman at all!"
        show ayesha annoyed
        "I'm already opening my mouth, trying to come up with an answer to all of that."
        "But before I can speak a word, Ayesha throws the dress right in my face."
        "And by the time I manage to get it under control, she's already stormed off."
        $ ayesha.love -= 10
        $ hero.cancel_activity()
    return

label ayesha_gift_collar_male:
    show ayesha
    "You'd think that a girl as big and strong as Ayesha would be brimming with confidence, right?"
    "I mean, she's not just physically imposing either - she's stunningly gorgeous too!"
    "Just looking at her, there's nothing that Ayesha hasn't got going for her."
    "But as I've spent time with her, I've noticed that's not really the case."
    "Ayesha's just not the same person that she pretends to be in the wrestling ring."
    "In fact, she's often painfully shy and awkward, like she doesn't believe in herself."
    "Sure, she comes out of her shell when she's with me and we're having fun."
    "Even more so when we're alone, then her true personality shines through."
    "But I hate to see her lacking in confidence, and I want to help her any way I can."
    "So I spend some serious time racking my brains, trying to think up a solution."
    "And when I do, I'm sure that it'll be the answer to Ayesha's problems."
    "Once I've gotten my hands on everything I need, I just have to choose my moment..."
    mike.say "Oh, yeah...I almost forgot!"
    mike.say "I got you a little something, Ayesha."
    mike.say "Just let me get it for you..."
    "Ayesha looks instantly intrigued at the prospect of me giving her a gift."
    "She hides it well, but I know that she's bursting to see what it is."
    show ayesha happy
    ayesha.say "Aw, [hero.name]!"
    ayesha.say "You shouldn't have done that!"
    ayesha.say "But I DO love it when you spoil me!"
    "I can't help smiling at the look on Ayesha's face right now."
    "She's excited, even a little embarrassed."
    "And it brings out the natural beauty she possesses so much of too."
    "Let's just hope she looks even happier once she sees what I got her..."
    mike.say "Well...I kind of noticed that you don't wear much jewellery, Ayesha."
    mike.say "And I thought it was time I did something about that."
    ayesha.say "Ah...that's kind of a habit, [hero.name]."
    show ayesha normal
    ayesha.say "I grew up pretty poor."
    ayesha.say "And there wasn't money for that kind of thing."
    ayesha.say "So I guess I just got used to not wearing it."
    mike.say "That must have been tough, Ayesha."
    mike.say "But I hope that you'll wear this..."
    "I hold up the collar that I've been hiding behind my back."
    "At first glance, it could be mistaken for an ordinary dog collar."
    "But a closer look reveals that it's made from far more expensive materials."
    "It's also sized for a neck larger than that of the average dog too."
    "Though it does bear a bone-shaped tag with the word 'Puppy' engraved on it."
    "I hold up the collar, offering it to Ayesha."
    "And the whole time I can feel my heart beating in my chest."
    "It's pounding away in anticipation as I wait for her reaction!"
    if ayesha.sub >= 90:
        "Ayesha looks at the collar in my hands and then back up at me."
        "There's a strange quality to the look in her eyes."
        "It's hard to place at first, as I'm not used to seeing it with her."
        "But then I realise that it's amazement."
        "Amazement mixed in with a hell of a lot of arousal!"
        show ayesha happy
        ayesha.say "Whoa..."
        ayesha.say "That's...for me?!?"
        mike.say "Yeah, Ayesha - it's for you."
        mike.say "I know you like to act tough in the ring."
        mike.say "But I think I know the real you better now."
        mike.say "And you're sweet, sensitive and playful."
        mike.say "Kind of like a puppy, yeah?"
        "I feel the words catch in my throat."
        "And I realise that I'm getting embarrassed."
        mike.say "And...I..."
        mike.say "I want to show off the fact that you're mine too!"
        mike.say "But you don't have to wear it - not if you think it's too much!"
        "Ayesha nods slowly, but she doesn't say a word."
        "Instead she reaches out and takes the collar from me."
        "Then she proceeds to fasten it around her neck."
        "I watch as she adjusts it, and then smiles at me."
        $ ayesha.set_sex_slave()
        hide ayesha
        show ayesha blush
        ayesha.say "Well - how do I look?"
        mike.say "Perfect, Ayesha - you look perfect!"
        "Ayesha giggles and looks away, like she's suddenly bashful."
        "She plays with the tag on the collar as a smile spreads across her face."
        ayesha.say "I shouldn't like this, [hero.name]."
        ayesha.say "I should be all angry and feminist about it."
        show ayesha happy
        ayesha.say "But it just feels right somehow - I don't know how to explain it!"
        mike.say "Then don't try, Ayesha."
        mike.say "Sometimes you don't need to over-analyse these things."
        "Ayesha nods, still smiling in that cute, bashful manner."
        ayesha.say "I...I don't suppose..."
        mike.say "What's that, Ayesha?"
        ayesha.say "It sound silly, but..."
        ayesha.say "You don't have a leash to match the collar, do you?"
        ayesha.say "I kinda like the idea of you walking me around, [hero.name]!"
        ayesha.say "You know - like I'm your dog or something?"
        "I nod, loving the fact that Ayesha's getting into the idea."
        "And I'm already planning on getting the leash she mentioned."
        $ ayesha.love += 2
        $ ayesha.sub += 5
    else:
        "Ayesha starts to shake her head almost the moment she sees the collar."
        "And I can already feel myself beginning to regret this as she does so."
        "When I try to look deeper into her eyes, things only get worse."
        "As I can see that she's also on the brink of bursting into tears."
        show ayesha annoyed
        ayesha.say "Y...you want me to wear a collar?"
        ayesha.say "Like I'm some kind of animal?!?"
        ayesha.say "Oh god...you think I'm like a dog!"
        ayesha.say "That I'm ugly and clumsy!"
        "I begin to shake my own head at this."
        "I'm desperate to tell Ayesha that she's wrong."
        mike.say "No, Ayesha, no!"
        mike.say "That's not it at all!"
        mike.say "If you're any kind of dog, you're a pedigree one!"
        mike.say "The kind they take to all of those big dog shows!"
        "Ayesha all but roars in despair."
        "Which is not the reaction I'd hoped for."
        ayesha.say "So you mean I'm inbred?"
        show ayesha angry
        ayesha.say "That I should be paraded around on a leash?!?"
        "Ayesha really is crying now, tears rolling down her cheeks."
        "I glance around, worried at what anyone seeing us must be thinking."
        "But what's worse than the embarrassment is the sight of Ayesha right now."
        "She looks genuinely distressed, like I've hurt her deeply."
        mike.say "I...I'm sorry, Ayesha."
        mike.say "This was a terrible idea, I see that now."
        "I toss the collar away, not caring how much it cost me."
        "But the gesture and my words don't seem to be enough."
        "Ayesha sniffles and blubs, then she turns away from me."
        show ayesha sad
        ayesha.say "I...I want to be alone, okay?"
        ayesha.say "In fact...I don't think I want to see you for a while!"
        "All I can do is nod in silence as Ayesha turns on her heel."
        hide ayesha
        "My head sags as she walks away, and I feel ashamed of myself."
        "Will she ever forgive me, let me have another chance?"
        "I guess all I can do is wait and see."
        $ ayesha.love -= 20
        $ ayesha.sub -= 10
        $ hero.cancel_activity()
    return

label ayesha_gift_butt_plug_male:
    show ayesha happy
    ayesha.say "Oh, [hero.name], is it for me?"
    "She unwraps the butt plug."
    if ayesha.sub <= 50 or not ayesha.sexperience:
        show ayesha annoyed
        ayesha.say "..."
        ayesha.say "Keep it... I don't want it so keep it."
        ayesha.say "I'm sure you'll have a better use of it than me."
        $ hero.cancel_activity()
    else:
        show ayesha blush
        ayesha.say "It's perfect!"
        ayesha.say "Thanks [hero.name], I'll make a good use of it."
        $ ayesha.flags.buttplug = True
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
