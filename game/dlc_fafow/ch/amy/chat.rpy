label amy_desire_0_male:
    amy.say "Working at the electronics store with Shawn is okay."
    amy.say "But I'm only doing it to pay the bills."
    amy.say "Because I think I'm wasted working there."
    menu:
        "You could do much better":
            mike.say "I totally agree with you, Amy."
            mike.say "You could do anything - like even be a model or something like that!"
            amy.say "You really think so, [hero.name]?"
            $ amy.love += 1
            amy.say "Thank you!"
        "All work is noble!":
            mike.say "There's nothing wrong with working retail, Amy."
            mike.say "You shouldn't be so snobbish about your job."
            amy.say "Oh..."
            $ amy.love -= 1
            amy.say "I didn't know you felt that way..."
        "Keep her feet on the ground" if hero.charm >= 50:
            mike.say "Shawn keeps telling me you're lucky to even have that job, Amy."
            mike.say "Like, you'd be way in over your head with anything more complicated!"
            amy.say "He really said that?"
            amy.say "Wow...I thought it was just a boring job."
            $ amy.sub += 1
    return

label amy_desire_1_male:
    amy.say "I've been a goth for like, I dunno...since forever."
    amy.say "And people are always telling me I'd be prettier if I ditched the look."
    amy.say "What do you think?"
    menu:
        "You are perfect the way you are" if hero.charm >= 50:
            mike.say "Personally, Amy, I love your look."
            mike.say "And you shouldn't let people's opinions get to you either!"
            amy.say "Yeah, you're right!"
            amy.say "Thanks, [hero.name]."
            $ amy.love += 1
        "You should explore other styles":
            mike.say "Hmm...maybe they have a point?"
            mike.say "I'd like to see you without all the goth stuff on."
            amy.say "You would?"
            amy.say "Oh...I thought you liked my look!"
            $ amy.love -= 1
        "Please, don't change!":
            mike.say "Oh no, Amy - no way!"
            mike.say "I...I really like it."
            mike.say "It's...very powerful!"
            amy.say "It is?"
            amy.say "Hmm...tell me more..."
            $ amy.sub -= 1
    return

label amy_desire_2_male:
    amy.say "Urgh..."
    amy.say "It's SO boring at work sometimes."
    amy.say "My head fills up with so many thoughts - some of them are pretty wild too!"
    menu:
        "Be responsible":
            mike.say "That's very unprofessional of you, Amy."
            mike.say "Part of being an adult is being able to control yourself!"
            amy.say "Okay, Mister Killjoy!"
            amy.say "I was only trying to make conversation..."
            $ amy.love -= 1
        "Be flirty" if hero.charm >= 75:
            mike.say "Don't waste your time thinking about that stuff, Amy."
            mike.say "Just drop me a line next time, and I'll do SO much better than you ever could!"
            amy.say "Really, [hero.name]?"
            amy.say "Is that a promise?"
            $ amy.sub += 1
        "Be helpful":
            mike.say "Wow, Amy - that sounds so naughty!"
            mike.say "I wish you'd call me up and work when I'm bored."
            mike.say "And...you know...make me do stuff?"
            amy.say "Oh yeah?"
            amy.say "Well, maybe I will!"
            $ amy.sub -= 1
    return

label amy_desire_3_male:
    amy.say "I can't wait to get off work today."
    amy.say "I'm SO tired of having someone telling me what to do all the time!"
    menu:
        "You can take charge with me":
            mike.say "Well, you can tell me what to do when we meet up, Amy."
            mike.say "I'd really like that!"
            amy.say "You would, huh?"
            amy.say "I like the sound of that!"
            $ amy.sub -= 1
        "No need to take charge" if hero.charm >= 75:
            mike.say "Okay, Amy, I promise I won't ask you to do a thing when we meet up."
            mike.say "I'll do the best I can to read your mind..."
            mike.say "Oh my - all I'm getting is sex, sex, sex!"
            amy.say "Stop it!"
            amy.say "Actually don't - just save it for later, okay?"
            $ amy.love += 1
        "I can take charge better":
            mike.say "Oh, you're going to have someone telling you what to do when we hook up."
            mike.say "But I promise it's not going to involve stacking shelves!"
            amy.say "Oh my!"
            amy.say "You promise?"
            $ amy.sub += 1
    return

label amy_desire_4_male:
    amy.say "Hey, [hero.name]..."
    amy.say "I've been thinking about you all day."
    amy.say "I can't wait to see what you've got in store for me!"
    menu:
        "Nothing":
            mike.say "Thanks, Amy..."
            mike.say "Way to put all the pressure on me!"
            amy.say "Thanks, [hero.name]..."
            amy.say "Way to be a jerk!"
            $ amy.love -= 1
        "Nothing I can tell":
            mike.say "Well you're just going to have to wait."
            mike.say "But it'll be worth it, I promise you!"
            amy.say "NO!"
            amy.say "You have to tell me!"
            amy.say "Now I'm going to die of curiosity!"
            $ amy.love += 1
        "Anything you want":
            mike.say "Whatever you want, Amy!"
            mike.say "Just say so, and it's yours!"
            amy.say "Me in total control?"
            amy.say "I like the sound of that..."
            $ amy.sub -= 1
        "Something... later":
            mike.say "You just keep on waiting."
            mike.say "You'll find out when I'm good and ready to show you!"
            amy.say "Oh...okay!"
            amy.say "I'll be good, I promise..."
            $ amy.sub += 1
    return

label amy_desire_5_male:
    amy.say "Urgh..."
    amy.say "[hero.name], I'm bored!"
    amy.say "Come over and do something to me - something fun!"
    menu:
        "Get ready for me!":
            mike.say "You'd better be ready for me when I get there, Amy."
            mike.say "Because I'm in the mood to take what I want!"
            amy.say "Oh, [hero.name]..."
            amy.say "I'll be ready and waiting for you!"
            $ amy.sub += 1
        "I am ready for you":
            mike.say "I...I'm coming, Amy!"
            mike.say "I'll do anything you want!"
            mike.say "And I do mean anything..."
            amy.say "Mmm...I like the sound of that!"
            amy.say "So you'd better get here fast!"
            $ amy.sub -= 1
        "Get ready for me":
            mike.say "Hold that thought, Amy..."
            mike.say "I'm on my way!"
            mike.say "And make sure you're ready for me!"
            amy.say "Hurry on over!"
            amy.say "I promise you'll like the position you find me in..."
            $ amy.love += 1
        "No can do right now":
            mike.say "I'm a little busy right now, Amy."
            mike.say "Don't you have a vibrator or something?"
            amy.say "Yeah, I do..."
            amy.say "And it's better company than you are!"
            $ amy.love -= 1
    return

label amy_love_0_male:
    amy.say "I'm kind of glad I got the job at the electronics store, [hero.name]."
    amy.say "Because if not, then I'd never have been introduced to you."
    menu:
        "Shawn is a good fellow":
            mike.say "I dunno, Amy..."
            mike.say "I kind of liked going in there to browse or talk with Shawn the most."
            amy.say "Really?"
            amy.say "Well, I'll try to avoid you in future!"
            $ amy.love -= 1
        "Good vibes":
            mike.say "Yeah, I know!"
            mike.say "You've certainly made visiting the store more fun!"
            amy.say "Thank you, [hero.name]!"
            amy.say "That's kind of you to say."
            $ amy.love += 1
        "Good customer service":
            mike.say "Well, I love being served by you, Amy."
            mike.say "Sometimes I wish I could have you wait on me all day long!"
            amy.say "Y...you do?!?"
            amy.say "That...that doesn't sound too bad!"
            $ amy.sub += 1
    return

label amy_love_1_male:
    amy.say "You're in the store so often these days, [hero.name]."
    amy.say "Sometimes I think you only come here to see me!"
    menu:
        "I can not do otherwise":
            mike.say "You...you kind of draw me back, Amy!"
            mike.say "It's like you have some weird power over me..."
            amy.say "You really mean that?"
            amy.say "Now there's an interesting idea..."
            $ amy.sub -= 1
        "Are you watching my comings and goings?":
            mike.say "You've been counting the times I come in here?"
            mike.say "What are you, Amy, some kind of stalker?"
            amy.say "No...I just..."
            amy.say "Forget I mentioned it, okay?"
            $ amy.love -= 1
        "Oh, you noticed!":
            mike.say "Well...don't be mad, Amy..."
            mike.say "But I kind of do!"
            amy.say "Oh, I'm not mad, [hero.name]!"
            amy.say "I just like that we're becoming friends..."
            $ amy.love += 1
    return

label amy_love_2_male:
    amy.say "I know I started out as someone who worked with your friend."
    amy.say "But I really feel like we're more than that now, right?"
    menu:
        "It is good to be with you":
            mike.say "Y...yeah, Amy, I can't go five minutes without thinking about you."
            mike.say "As soon as I hear your voice, I can't help rushing to obey!"
            amy.say "Oh really?"
            amy.say "Now that is interesting..."
            $ amy.sub -= 1
        "Once again we are talking about you feelings":
            mike.say "You ever wonder about what I think, Amy?"
            mike.say "Ever wonder if I might see things differently?"
            amy.say "I...I guess not, [hero.name]!"
            amy.say "Geez...I was only trying to be nice."
            $ amy.love -= 1
        "It is good to have you around":
            mike.say "Yeah, Amy, I feel like I need to have you around me."
            mike.say "Like I need to know where you are all the time!"
            amy.say "Y...you do?"
            amy.say "I had no idea you liked me that much!"
            $ amy.sub += 1
    return

label amy_love_3_male:
    amy.say "It's a relief to be able to be totally honest with you, [hero.name]."
    amy.say "Now that we're dating, I feel like I can really open up about how I feel."
    menu:
        "I was always curious before":
            mike.say "I was always curious before, Amy..."
            mike.say "Curious about what you'd do to me given the chance!"
            amy.say "Well, [hero.name]..."
            amy.say "I think it's about time you found out!"
            $ amy.sub -= 1
        "I always wanted to share with you":
            mike.say "I feel the same way, Amy."
            mike.say "I hated not being able to tell you how much I wanted to be with you!"
            amy.say "You can tell me anything you like now, [hero.name]."
            amy.say "Especially when we're alone together..."
            $ amy.love += 1
        "I want you to be mine, always":
            mike.say "I feel the same way, Amy."
            mike.say "For so long I've wanted to possess you, to mould you to my desires!"
            amy.say "Oh, [hero.name]!"
            amy.say "Just hearing you talk like that - it makes me melt inside!"
            $ amy.sub += 1
    return

label amy_love_4_male:
    amy.say "It's weird, [hero.name]..."
    amy.say "I just worked in a store you happened to walk into."
    amy.say "Now we're like, an item!"
    menu:
        "I am what you need":
            mike.say "I don't think it was as much down to chance as that, Amy."
            mike.say "I think you knew that you needed someone like me."
            mike.say "Someone to take hold of the reins!"
            amy.say "Oh, [hero.name], don't talk about reins!"
            amy.say "You know what that does to me..."
            $ amy.sub += 1
        "I just do what I need":
            mike.say "I feel like it was fate, Amy."
            mike.say "Like I was drawn to someone with your...strength!"
            amy.say "Aww...aren't you sweet!"
            amy.say "And so needy too!"
            $ amy.sub -= 1
        "I need more":
            mike.say "An item?"
            mike.say "I hope we're more than that, Amy!"
            amy.say "Oh yeah, of course we are!"
            amy.say "I'm crazy about you!"
            $ amy.love += 1
        "Do you know what I need?":
            mike.say "When did we sit down and decide that we were an item, Amy?"
            mike.say "Sounds to me like you just decided that yourself!"
            amy.say "Sounds like you decided you were a jerk without my help!"
            amy.say "So that makes us even..."
            $ amy.love -= 1
    return

label amy_love_5_male:
    amy.say "I'm tired of trying to be edgy and clever about it, [hero.name]."
    amy.say "I love you!"
    amy.say "There, I came out and said it!"
    menu:
        "I love you too" if hero.charm >= 75:
            mike.say "You didn't have to do that, Amy."
            mike.say "I know you love me, and I love you too."
            amy.say "It was worth it, [hero.name]."
            amy.say "Worth it to hear you say that!"
            $ amy.love += 1
        "I love you more":
            mike.say "I love you too, Amy!"
            mike.say "More than anything in the whole world!"
            mike.say "And I'll do whatever you ask of me too!"
            amy.say "Will you now?"
            amy.say "I intend to test that statement..."
            $ amy.sub -= 1
        "Keep it quiet, please":
            mike.say "Shhh!"
            mike.say "Keep your voice down, Amy!"
            mike.say "People are going to stare!"
            amy.say "Yeah, [hero.name]."
            amy.say "And we wouldn't want that, would we?!?"
            $ amy.love -= 1
        "Of course":
            mike.say "Of course you do, Amy."
            mike.say "Because I've trained you so well."
            mike.say "Trained AND disciplined you..."
            amy.say "Mmm..."
            amy.say "I think I might need a little more instruction!"
            $ amy.sub += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
