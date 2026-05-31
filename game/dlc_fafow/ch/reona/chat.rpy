label reona_desire_0_male:
    reona.say "I gotta say, [hero.name]..."
    reona.say "I'm a little worried Jack put me onto you."
    reona.say "I've known him a hell of a long time."
    reona.say "But he's kind of a geek!"
    reona.say "You're not one too, are you?"
    menu:
        "Jack and I are just too cool":
            mike.say "Hey, Reona!"
            mike.say "What are you talking about?"
            mike.say "Jack's like one of my best friends!"
            mike.say "And the stuff we're into is not geeky."
            mike.say "It's just that most people don't appreciate it, that's all."
            $ reona.love -= 1
        "I was... and I adapted":
            mike.say "I know, I know..."
            mike.say "We weren't the most popular kids in school."
            mike.say "And yeah, we got picked on a lot too."
            mike.say "But that doesn't have to be a bad thing."
            mike.say "It means I'm VERY good at taking orders!"
            $ reona.sub -= 1
        "I am beyond that" if hero.charm >= 50:
            mike.say "Don't worry, Reona."
            mike.say "Jack and I were into that kind of stuff back in school."
            mike.say "And he never really grew out of it."
            mike.say "But you should know that I did."
            mike.say "He stayed a boy, and I became a man!"
            $ reona.love += 1
    return

label reona_desire_1_male:
    reona.say "Everyone used to judge me at high-school."
    reona.say "You know, like say that I was a massive slut?"
    reona.say "Just because I was a little bit more experienced than the other girls!"
    reona.say "Anyway, I think they were just jealous of me."
    reona.say "Their boyfriends were a lot more appreciative anyway!"
    menu:
        "You are what you were":
            mike.say "Oh yeah, I heard all about that."
            mike.say "Jack's told me all the stories about you."
            mike.say "Even the really juicy ones!"
            mike.say "Thing is, he did say you were a slut at school."
            mike.say "But he also said you were much worse now!"
            $ reona.love -= 1
        "Let go of the past":
            mike.say "That's all in the past, Reona."
            mike.say "What kids at school said doesn't matter."
            mike.say "But what is important is that you love yourself."
            mike.say "And well, now you're an adult."
            mike.say "So nobody has the right to judge you."
            $ reona.love += 1
        "You are who you are":
            mike.say "You can tell yourself that all you like, Reona."
            mike.say "But we all know that stuff leaves deep, lasting scars."
            mike.say "Deep down you can't hide the fact you really are what you are."
            mike.say "You like cock and you don't care where it comes from."
            mike.say "What you need is someone that knows you, and still cares - like me."
            $ reona.sub += 1
    return

label reona_desire_2_male:
    reona.say "You know what, [hero.name]..."
    reona.say "Some guys are kinda put off by the way I am."
    reona.say "They find me too full on, you know, too honest?"
    reona.say "But not you."
    reona.say "I feel like I can really be myself around you."
    menu:
        "Honesty is good":
            mike.say "That's just because they can't handle you, Reona."
            mike.say "They expect a girl to be all meek and shy."
            mike.say "And when you say it how it is, they get scared."
            mike.say "But not me."
            mike.say "I love a girl that speaks her mind."
            $ reona.love += 1
        "Honesty? Really?":
            mike.say "Oh, that's just because I know it's all bravado, Reona."
            mike.say "I can read the signs, I see that you're really terrified."
            mike.say "You act like a tough chick to hide your insecurities."
            mike.say "Deep down, you're just a slut that feels ashamed of herself."
            mike.say "But I'll keep your secret - for a price!"
            $ reona.sub += 1
        "Too much honesty can hurt":
            mike.say "Yeah..."
            mike.say "I was meaning to talk to you about that."
            mike.say "Thing is, I've been ignoring you being all rude and vulgar, Reona."
            mike.say "Because I thought you were just doing it to look tough."
            mike.say "I really do think you need to watch your mouth!"
            $ reona.love -= 1
    return

label reona_desire_3_male:
    reona.say "What do you think about experimenting in the bedroom, [hero.name]?"
    reona.say "You know, like trying out new stuff?"
    reona.say "Stuff that's maybe a little crazy?"
    reona.say "I wanna try all kinds of things."
    reona.say "But most guys are frightened by a girl like that!"
    menu:
        "You know how it starts, but you never know how far it can go":
            mike.say "Nah..."
            mike.say "I don't go in for all that perverted stuff."
            mike.say "It usually means you're a weirdo."
            mike.say "And once you start down that path..."
            mike.say "Well, who knows where you'll end up?"
            $ reona.love -= 1
        "When do we start my initiation?":
            mike.say "I...I always wanted to do stuff like that."
            mike.say "But I was too scared to ask a girl about it!"
            mike.say "If you'd show me how it works..."
            mike.say "Well, I'd be very grateful!"
            mike.say "So grateful you could do anything to me in return..."
            $ reona.sub -= 1
        "Time to find a safe word":
            mike.say "I have a pretty open mind, Reona."
            mike.say "So long as everyone's on the page."
            mike.say "And nobody's getting hurt."
            mike.say "Well...unless that's their thing!"
            mike.say "If you know what I mean?"
            $ reona.love += 1
    return

label reona_desire_4_male:
    reona.say "You know what, [hero.name]..."
    reona.say "When we met, I thought you were pretty lame."
    reona.say "But since then, you've really grown on me!"
    reona.say "Aw, who am I trying to kid!"
    reona.say "You turned out to be super hot - and you get me hot too!"
    menu:
        "Shine":
            mike.say "You have no idea how happy that makes me, Reona."
            mike.say "I think you're a real hottie too."
            mike.say "And just to be clear..."
            mike.say "I thought that the first moment I saw you!"
            mike.say "So, so hot!"
            $ reona.love += 1
        "Burn":
            mike.say "Wow..."
            mike.say "I'm kind of amazed you'd admit to that, Reona!"
            mike.say "I mean, it's super shallow."
            mike.say "And as for the admission I've grown on you..."
            mike.say "Well, we both know that you're super easy too!"
            $ reona.love -= 1
        "Melt":
            mike.say "That makes me so happy, Reona!"
            mike.say "Because I liked you the very moment I saw you!"
            mike.say "And since then, I've been hoping you liked me too."
            mike.say "But now I know that you do..."
            mike.say "Well, I'll do anything to keep it that way!"
            $ reona.sub -= 1
    return

label reona_desire_5_male:
    reona.say "Urggh..."
    reona.say "It's not fair, [hero.name]!"
    reona.say "Every time I look at you, I get turned-on!"
    reona.say "I just can't help it."
    reona.say "I wanna throw myself at you!"
    menu:
        "You have a condition":
            mike.say "You know what, Reona..."
            mike.say "You really should see a doctor about that."
            mike.say "Like a head doctor or something."
            mike.say "Because I really think you might be ill."
            mike.say "You might be a nympho or something."
            $ reona.love -= 1
        "You have my attention":
            mike.say "Then what are you holding back for, Reona?"
            mike.say "You have to know I feel the same way about you!"
            mike.say "So just let me know wherever you get the urge."
            mike.say "Because I'll drop whatever I'm doing."
            mike.say "And I'll pick you up instead!"
            $ reona.love += 1
        "You have an addiction":
            mike.say "Of course you do, Reona."
            mike.say "You need me to feed your desires."
            mike.say "Or should I say your addictions?"
            mike.say "And you know that nobody else understands you, right?"
            mike.say "Not like I do..."
            $ reona.sub += 1
    return

label reona_love_0_male:
    reona.say "I don't know what I was expecting you to be like, [hero.name]."
    reona.say "Probably some kind of boring geek, like I used to know at school!"
    reona.say "But you're not like that at all."
    reona.say "You're really funny, you know?"
    reona.say "You always seem to make me laugh!"
    menu:
        "Mission accomplished":
            mike.say "I do?"
            mike.say "Oh, Reona!"
            mike.say "I'm SO glad to hear that!"
            mike.say "I've been trying so hard to get your attention."
            mike.say "And I'm so happy you noticed me!"
            $ reona.sub -= 1
        "Keep an open mind":
            mike.say "You've just got to give people a chance, Reona."
            mike.say "That way you get to see the real person inside."
            mike.say "You see them for who they are."
            mike.say "And they see you for who you are too."
            mike.say "You get it?"
            $ reona.love += 1
        "Geek you said?":
            mike.say "Oh, is that so?"
            mike.say "You know what, Reona..."
            mike.say "People like you used to call people like me geeks."
            mike.say "Back at school, they made my life a misery!"
            mike.say "And I doubt you've changed much since then too."
            $ reona.love -= 1
    return

label reona_love_1_male:
    reona.say "You know, it's weird..."
    reona.say "I've dated a lot of guys, [hero.name]."
    reona.say "But you're not like any of them."
    reona.say "You're different, but in a good way."
    reona.say "And it kinda makes me want to find out more about you."
    menu:
        "These guys were not special":
            mike.say "That's probably because I'm not some dumb jock."
            mike.say "Or a sleaze-bag that's just interested in your body."
            mike.say "In all that time, sounds like you never dated one decent guy!"
            mike.say "Did you ever stop to take a look at them before you went for it?"
            mike.say "Or was it more just a case of checking they had a pulse?"
            $ reona.love -= 1
        "I am special":
            mike.say "You must have had a lot of bad experiences with guys, Reona."
            mike.say "I bet that was pretty damaging?"
            mike.say "You know, left a lot of mental and emotional scars?"
            mike.say "Just remember how lucky you are to have a guy like me, yeah?"
            mike.say "And do your best to make sure you keep me as well."
            $ reona.sub += 1
        "You make me special":
            mike.say "I don't know what would make me different, Reona."
            mike.say "But I do know that I'm enjoying spending more time with you."
            mike.say "Maybe that has something to do with it?"
            mike.say "Like we're getting to know each other better."
            mike.say "And liking what we discover too."
            $ reona.love += 1
    return

label reona_love_2_male:
    reona.say "It's weird, [hero.name]..."
    reona.say "I keep thinking about you when we're not together."
    reona.say "And I'm always in a good mood when I see you too!"
    reona.say "I don't normally get like that with guys."
    reona.say "I do when I see a cute outfit I want - but not with guys!"
    menu:
        "It's love":
            mike.say "I've been thinking about you a lot too, Reona."
            mike.say "I guess that's what happens when you click with someone."
            mike.say "And you always put a smile on my face too."
            mike.say "Seriously, I get happier when you're around!"
            mike.say "And yes, I know that sounds corny!"
            $ reona.love += 1
        "It's friendship":
            mike.say "Maybe that's because I took the time to get to know you, Reona?"
            mike.say "I mean how many guy's have ever done that before, huh?"
            mike.say "I bet most of them were just trying to get you into bed!"
            mike.say "What you're experiencing is how friendship really feels."
            mike.say "Not just some guy getting your motor running."
            $ reona.love -= 1
        "It's obsession":
            mike.say "Me too, Reona, me too!"
            mike.say "I'm always thinking of you when we're apart."
            mike.say "And my heart skips a beat when I see you again!"
            mike.say "In fact, I feel kind of empty when we're apart."
            mike.say "Like I'm lost and everything's pointless..."
            $ reona.sub -= 1
    return

label reona_love_3_male:
    reona.say "Hey, [hero.name]!"
    reona.say "What have you done to me?!?"
    reona.say "It's getting worse than it was before."
    reona.say "Now I'm getting moody when I'm not with you!"
    reona.say "Did you hypnotise me or something?"
    menu:
        "We miss each other":
            mike.say "I was just about to ask you the same thing, Reona!"
            mike.say "I'm always wondering what you're doing."
            mike.say "Or having to stop myself sending you endless texts!"
            mike.say "Whatever's going on, we're both suffering from it."
            mike.say "You think we're getting that close already?"
            $ reona.love += 1
        "It's just a little crush":
            mike.say "Hah!"
            mike.say "It's called affection, Reona."
            mike.say "The emotions you feel when you really like someone!"
            mike.say "Have you really never felt like that before?"
            mike.say "Geez, you must be pretty damaged!"
            $ reona.love -= 1
        "You just need me":
            mike.say "That's just you beginning to realise something, Reona."
            mike.say "And that's how much you need me in your life."
            mike.say "But don't worry, Reona."
            mike.say "You're going to be able to keep me around."
            mike.say "So long as you convince me that you're loyal..."
            $ reona.sub += 1
    return

label reona_love_4_male:
    reona.say "Since we've been getting closer, it's odd..."
    reona.say "But I haven't been looking at other guys as much."
    reona.say "You know - in that certain way?"
    reona.say "I mean, I have been looking..."
    reona.say "But then I always start thinking of you, [hero.name]!"
    menu:
        "I'm lucky":
            mike.say "Oh, Reona!"
            mike.say "Just the thought of you thinking about me!"
            mike.say "That makes me feel so special."
            mike.say "Knowing that I get a look in too."
            mike.say "I feel so lucky!"
            $ reona.sub -= 1
        "I'm flattered":
            mike.say "Ha, ha..."
            mike.say "That's pretty flattering coming from you, Reona!"
            mike.say "Of course you're going to look at other guys."
            mike.say "The important thing is that I popped in there too!"
            mike.say "That means you care about me."
            $ reona.love += 1
        "I'm stunned":
            mike.say "Urgh..."
            mike.say "Is that supposed to make me feel special, Reona?"
            mike.say "And what were you doing when you saw these other guys?"
            mike.say "Remembering them for later?"
            mike.say "When you were on your own and feeling horny?"
            $ reona.love -= 1
    return

label reona_love_5_male:
    reona.say "I...I never had to do this before, [hero.name]."
    reona.say "I've been in a tough position a couple of times."
    reona.say "But I never had to admit to this..."
    reona.say "I never had to admit that I loved someone."
    reona.say "But I do - I really love you!"
    menu:
        "I do not deserve this":
            mike.say "Huh..."
            mike.say "So it finally happened?"
            mike.say "You actually developed feelings for someone!"
            mike.say "And I'm the unlucky guy you've fallen for."
            mike.say "What did I ever do to deserve this?"
            $ reona.love -= 1
        "Of course" if hero.charm >= 50:
            mike.say "Well of course you have, Reona."
            mike.say "Even someone like you can sense what they need."
            mike.say "And what you need is to be with someone like me."
            mike.say "Someone that understands you, knows all your flaws."
            mike.say "But is still prepared to give you a chance!"
            $ reona.sub += 1
        "I love you too":
            mike.say "That's exactly what I wanted to hear, Reona."
            mike.say "Because it makes saying what I have to say easier too."
            mike.say "I feel the exact same way."
            mike.say "I love you too, Reona."
            mike.say "In fact, I'm crazy about you!"
            $ reona.love += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
