label lavish_talk_love_female:
    bree.say "You seem pretty hard-nosed and professional, Lavish."
    bree.say "So much so that I'm almost afraid to ask you this!"
    bree.say "Do you believe in love?"
    bree.say "Or do you just think it's a chemical reaction?"
    lavish.say "I'm not a robot, [hero.name]!"
    lavish.say "Of course I believe in love."
    lavish.say "And I hope I'll know it when I find it too."
    $ lavish.love += 1
    return

label lavish_talk_sex_female:
    bree.say "I'm always worried that I'm not getting enough action."
    bree.say "You know what I mean, Lavish?"
    bree.say "Like our generation's supposed to be at it all the time."
    bree.say "But I ages without seeing even a glimpse of cock!"
    if not lavish.sexperience:
        lavish.say "I've never had that problem myself, [hero.name]."
        lavish.say "My experience is that you just have to be confident."
        lavish.say "Do that and you can almost always catch a dick."
    else:
        lavish.say "You're probably just over-thinking it, [hero.name]."
        lavish.say "Stop trying so hard and maybe it'll come easier."
        lavish.say "That or else you're just obsessed with sex!"
        $ lavish.sub += 1
    return

label lavish_talk_politics_female:
    bree.say "Urgh...nobody seems to care about politics!"
    bree.say "You mention it just once, and they turn off!"
    lavish.say "I know exactly what you mean, [hero.name]!"
    bree.say "You do?"
    lavish.say "Of course I do!"
    lavish.say "I face prejudice in the workplace every single day!"
    lavish.say "I don't have a choice other than to be political!"
    $ lavish.love += 1
    return

label lavish_talk_food_female:
    bree.say "Oh...I'm so hungry, Lavish!"
    bree.say "But I have no idea what I want to eat..."
    lavish.say "Make it something special, [hero.name]."
    lavish.say "Something you'll remember!"
    bree.say "Whoa...sounds like you're passionate when it comes to food!"
    lavish.say "I'm passionate about everything I put in me, [hero.name]!"
    $ lavish.love += 1
    return

label lavish_talk_travels_female:
    bree.say "I guess you want to travel the world, Lavish?"
    bree.say "Everyone I ask seems to want to do that!"
    lavish.say "Of course I do, [hero.name]!"
    lavish.say "But unlike most people, I have a plan."
    lavish.say "And it involves working my way up the corporate ladder."
    lavish.say "That way I can afford to make my dreams into reality."
    $ lavish.love += 1
    return

label lavish_talk_tv_female:
    bree.say "You watch much TV, Lavish?"
    lavish.say "I do, [hero.name], I do."
    lavish.say "But who wouldn't when there's so much interesting stuff on offer?"
    lavish.say "I can't get enough of the documentaries and history shows on there!"
    lavish.say "Can you believe some people actually waste time watching soap operas and sci-fi series?"
    bree.say "Erm...no, Lavish!"
    bree.say "Who would watch that sort of stuff..."
    $ lavish.love += 1
    return

label lavish_talk_sports_female:
    bree.say "You the sporty type, Lavish?"
    bree.say "Enjoy working up a sweat?"
    lavish.say "Urgh...don't talk to me about sports, [hero.name]!"
    lavish.say "Don't like them, don't get them, no time for them!"
    lavish.say "Waste of energy, if you ask me."
    bree.say "Whoa, Lavish...you don't mince your words!"
    return

label lavish_talk_fashion_female:
    bree.say "I guess you have to dress to impress in the world of business, Lavish?"
    bree.say "I don't think I'd know where to start!"
    bree.say "But you seem to have a handle on it."
    if lavish.sub < 75:
        lavish.say "Thank you, [hero.name]!"
        lavish.say "But it is hard to get right."
        lavish.say "You have to balance professionalism with femininity."
        lavish.say "Get it wrong and people think you're either a ball-buster or a bimbo!"
    else:
        lavish.say "Oh, I'm so glad you like what I wear, [hero.name]!"
        lavish.say "I try so hard to dress in a way that meets with approval."
        lavish.say "Because that's the most important thing of all."
        lavish.say "I need to know that I'm pleasing people that matter!"
        $ lavish.sub += 1
    $ lavish.love += 1
    return

label lavish_talk_books_female:
    bree.say "You seem like a smart cookie, Lavish."
    bree.say "You must swallow books whole!"
    bree.say "Would you like some recommendations?"
    lavish.say "Erm...no, [hero.name], I wouldn't."
    lavish.say "I didn't get this far letting other people tell me what to do."
    lavish.say "And I certainly don't need you telling me what to read either!"
    $ lavish.love -= 1
    return

label lavish_talk_people_female:
    bree.say "You must be a real people person, Lavish."
    bree.say "How else can you be so good at the job you do?"
    bree.say "Tell me what your secret is!"
    lavish.say "You've got me all wrong, [hero.name]."
    lavish.say "I'm not really a people person at all."
    lavish.say "I mean, I don't hate everyone I meet!"
    lavish.say "But people are just people."
    lavish.say "And most of them are nothing special."
    return

label lavish_talk_computers_female:
    bree.say "I guess you're pretty good with computers, Lavish?"
    bree.say "Show me someone that's a success at work who isn't!"
    lavish.say "Ah..."
    lavish.say "I'll let you into a little secret, [hero.name]."
    lavish.say "I actually hate computers."
    lavish.say "And I'd be happy if they all disappeared overnight!"
    $ lavish.love -= 1
    return

label lavish_talk_music_female:
    bree.say "You ever listen to music while you work, Lavish?"
    bree.say "I do that while I'm studying."
    bree.say "And I find it helps me out loads!"
    lavish.say "No, [hero.name], I don't."
    lavish.say "I won't tolerate any distractions in the workplace."
    lavish.say "And listening to music would be very unprofessional."
    return

label lavish_talk_birthday_female:
    bree.say "Happy Birthday, Lavish!"
    bree.say "Many happy returns!"
    lavish.say "Oh, [hero.name]..."
    lavish.say "It's so kind of you to remember!"
    $ lavish.love += 3
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
