label claire_talk_love_male:
    claire.say "This might sound like a total cliche, [hero.name], but hear me out, okay?"
    claire.say "When you're a woman, everyone expects you to be passionate and loving."
    claire.say "But then the second that you get married, all of that's supposed to stop."
    claire.say "Then it's just running after your husband and raising his damn kids!"
    menu:
        "A woman shouldn't be so limited":
            mike.say "It's not fair at all, Claire."
            mike.say "And it's like they want you to give up being who you are too."
            mike.say "To throw away who you are, all for the sake of others."
            claire.say "That's it exactly!"
            claire.say "I knew you'd understand."
            $ claire.love += 1
        "That's a very old-fashioned mindset":
            mike.say "Well that's a very old-fashioned and out-dated way to look at it, Claire."
            mike.say "I honestly don't think that society is expecting you to do that anymore."
            mike.say "So by holding yourself to those expectations, you're only hurting yourself."
            claire.say "Urgh...you sound like the kids in the neighbourhood back home."
            claire.say "I should have known that you'd be too young to get it."
            $ claire.love -= 1
        "Wow, your generation really is domesticated":
            mike.say "Wow, Claire - are you really still hanging onto that boomer-era nonsense?"
            mike.say "I can see that you're going to need to be reeducated on a load of stuff."
            mike.say "But don't worry, I can take care of that."
            claire.say "Really, [hero.name]?"
            claire.say "You think I need to be reeducated?"
            $ claire.sub += 1
        "Your generation really has it's finger on the pulse":
            mike.say "I'll be honest with you, Claire..."
            mike.say "My generation doesn't have a clue when it comes to that kind of thing!"
            mike.say "I think yours was the last one that really got it right."
            claire.say "Oh...you really think so?"
            claire.say "Most people your age don't seem to think so."
            $ claire.sub -= 1
    return

label claire_talk_sex_male:
    claire.say "I've spent so many years being a dutiful wife, fulfilling my conjugal obligations."
    claire.say "And I feel like every moment of it was totally stifling and utterly boring!"
    claire.say "Now I want to make up for lost time, to try everything that I missed out on."
    menu:
        "I am totally up for making that happen":
            mike.say "Good for you, Claire..."
            mike.say "You want to regret what you have done, not what you haven't."
            mike.say "And I for one am totally up for helping you to make it happen!"
            claire.say "You are?"
            claire.say "Then let's not waste any more precious time!"
            $ claire.love += 1
        "Don't give into temptation":
            mike.say "You only just got your freedom, Claire..."
            mike.say "Don't let it go to your head before you get used to it."
            mike.say "If not, you could end up doing something that you'll regret."
            claire.say "Okay...I was not expecting that answer from you."
            claire.say "Kind of the opposite, actually."
            $ claire.love -= 1
        "You need me to hold your hand through this":
            mike.say "This must all be pretty scary for you, Claire..."
            mike.say "Being let loose in a world of infinite sexual possibilities."
            mike.say "But don't worry, because I'm here to be your guide."
            claire.say "Really, you'd do that for me?"
            claire.say "Because it is kind of intimidating."
            $ claire.sub += 1
        "Will you take me along for the ride?":
            mike.say "It sounds like you're off on an awfully big adventure, Claire!"
            mike.say "Is there any chance that you could take me along with you?"
            mike.say "Because I'm always here and ready to help."
            claire.say "Of course you can come along, [hero.name]."
            claire.say "For most of the journey, anyway..."
            $ claire.sub -= 1
    return

label claire_talk_politics_male:
    claire.say "I've been reading the newspaper and watching TV more recently than I used to."
    claire.say "I kind of tuned out of all that stuff when I was raising Adam and running a home."
    claire.say "But now I'm reconnecting with it, I'm amazed - politicians seem worse than ever!"
    menu:
        "They do seem to be getting more brazen":
            mike.say "Maybe you missed the change, Claire - but you're not wrong."
            mike.say "I mean, don't get me wrong, they've always been a bunch of shits."
            mike.say "But recently they seem to be even more brazen about it."
            claire.say "I'm glad it's not just me."
            claire.say "God knows who I'll vote for at the next election."
            $ claire.love += 1
        "You just admitted that you're out of touch":
            mike.say "Did you actually just say you're out of touch and then offer up an opinion?"
            mike.say "Don't you know that the latter means the former is pretty much worthless?"
            mike.say "Finish reeducating yourself before you share your take on current affairs, Claire."
            claire.say "Wow, [hero.name], just...wow!"
            claire.say "You sound so much like Hector it's not even funny."
            $ claire.love -= 1
        "Don't worry about it, I'll do the thinking for you":
            mike.say "It's good that you want to get back into it, Claire."
            mike.say "But until you do that, maybe let me clue you in, okay?"
            mike.say "We wouldn't want you embarrassing yourself, would we?"
            claire.say "Now that I think about it...maybe you're right."
            claire.say "I have been out of the loop for a long time."
            $ claire.sub += 1
        "Your take on things is quiet refreshing":
            mike.say "Maybe your being unfamiliar with things is actually a plus?"
            mike.say "It means that you're looking at things in a totally different way, right?"
            mike.say "In fact, I'd like to hear what your take on current affairs is, Claire."
            claire.say "You know what...I think you're right."
            claire.say "My take on stuff is pretty unique."
            $ claire.sub -= 1
    return

label claire_talk_food_male:
    claire.say "I don't care what anyone says, I'm going to go out there and sample every different cuisine I can find."
    claire.say "That's what happens when you marry a guy who's idea of fine dining is a goddamn chilli-dog."
    claire.say "And if it means that my ass ends up getting bigger as a result - then people can kiss it!"
    menu:
        "Variety is the spice of life":
            mike.say "I love that you want to go out there and try everything, Claire."
            mike.say "Let's see if there's anything that we both haven't tried yet."
            mike.say "Then we can discover it together, yeah?"
            claire.say "That's a great idea!"
            claire.say "Let's compare notes and find out."
            $ claire.love += 1
        "You should be thinking of your health":
            mike.say "Are you really sure that's wise, Claire?"
            mike.say "Even someone way younger than you needs to keep their health in mind."
            mike.say "And once those pounds are added to your frame, they're so hard to shed."
            claire.say "Wait a minute..."
            claire.say "Are you...are you actually calling me fat?!?"
            $ claire.love -= 1
        "You need to be supervised in that":
            mike.say "I don't think you realise how much more choice there is out there these days, Claire."
            mike.say "There's a real danger you could get disoriented by all of those new types of cuisine."
            mike.say "Tell you what, I'll be your guide on this culinary adventure!"
            claire.say "Oh, is it really that confusing?"
            claire.say "Then maybe that would be for the best."
            $ claire.sub += 1
        "Please take me with you!":
            mike.say "Oh, I never got to really explore that kind of thing either, Claire."
            mike.say "And I've not had the courage to try new things for a long time."
            mike.say "Do you think I could try some of the stuff you're going to be having?"
            claire.say "Sure, [hero.name], I don't see why not."
            claire.say "I'll be sure to order an extra portion, just for you!"
            $ claire.sub -= 1
    return

label claire_talk_travels_male:
    claire.say "One of the things I regret about getting married and settling down is not being able to travel."
    claire.say "I didn't even get to do it back when I was a student either, which is a real shame."
    claire.say "Maybe now I'll finally get the chance to see more of the world?"
    menu:
        "Yes, and you won't be seeing it alone either":
            mike.say "Totally, Claire - the world's your oyster now."
            mike.say "And I hope you don't mind me saying this..."
            mike.say "But you won't be seeing them alone either!"
            claire.say "I won't - who's going to be..."
            claire.say "Oh...oh, I see - we'll go there together!"
            $ claire.love += 1
        "Good luck affording that":
            mike.say "Have you seen the price of a plane ticket these days, Claire?"
            mike.say "And don't get me started on how much it costs to go on a cruise!"
            mike.say "You'll be lucky to afford a day at the beach, the way it's going."
            claire.say "So what are you saying, [hero.name]?"
            claire.say "That I'm a fool for having a dream?"
            $ claire.love -= 1
        "You're going to need someone to take you there":
            mike.say "Sounds to me like you're not the most worldly of people, Claire."
            mike.say "There's no way you could ever go to any of these places alone."
            mike.say "So it's a good job you've got me to accompany you!"
            claire.say "You'd really do that for me?"
            claire.say "You're the best, [hero.name]!"
            $ claire.sub += 1
        "Do you need a travelling companion?":
            mike.say "Wow, Claire...sounds like you have it all figured out!"
            mike.say "I get into such a muddle when it comes to planning a trip."
            mike.say "I don't suppose you'd want a travelling companion, would you?"
            claire.say "Hmm...now there's an intriguing proposition."
            claire.say "Let me take a look at your resume, and maybe you can come along too."
            $ claire.sub -= 1
    return

label claire_talk_tv_male:
    claire.say "Hector always used to spend his evenings on the couch, eyes glued to the TV."
    claire.say "Sometimes I swear that he had no idea what was even on the damn screen."
    claire.say "It always made me want to leave him to it and read a book instead."
    menu:
        "And that's to your credit":
            mike.say "I can really believe that of you, Claire."
            mike.say "You don't seem like the kind of person to just lounge on the sofa."
            mike.say "No, you want to get more out of life than that, right?"
            claire.say "You are so right, [hero.name]."
            claire.say "It's like you totally get me."
            $ claire.love += 1
        "Maybe the poor guy was just exhausted?":
            mike.say "Wait a minute, Claire - wasn't Hector the bread-winner in the house?"
            mike.say "And you were the one staying home and just doing the cleaning, right?"
            mike.say "So did it ever occur to you that the poor schlep could have been exhausted?"
            claire.say "Wow...I did not think you were going to go there."
            claire.say "I did not think you were going to simp for my deadbeat husband!"
            $ claire.love -= 1
        "Don't worry, I won't be sitting on the sofa all night, and neither will you!":
            mike.say "Oh, don't worry, Claire - I won't be sitting on the sofa all night."
            mike.say "And neither will you, because I have far better things for us to do."
            mike.say "Most, but not all of them requiring us to be horizontal!"
            claire.say "Oh, [hero.name] - you're so outrageous!"
            claire.say "But please, don't stop it."
            $ claire.sub += 1
        "I want to be a better partner for you":
            mike.say "Eurgh...I never want to be like that guy!"
            mike.say "So you have to promise to keep me in line, Claire."
            mike.say "To tell me if I'm not meeting the standards you deserve."
            claire.say "Are...are you serious?"
            claire.say "Well, that does sound like it'd be nice."
            $ claire.sub -= 1
    return

label claire_talk_sports_male:
    claire.say "Urgh...is it sports season already?"
    claire.say "It always seems to be sports season - and I hate every last one of them!"
    claire.say "And yeah, no surprise that my slob of a husband is totally religious about them."
    menu:
        "Sports are totally overrated":
            mike.say "Sports are for people that don't have a personality of their own, Clare."
            mike.say "Like, they use them to cover up the fact they don't have anything interesting to say."
            mike.say "I'd rather watch paint dry than an actual game of football."
            claire.say "Oh, I am SO relieved to hear you say that!"
            claire.say "Sometimes it feels like all men are boring sports drones."
            $ claire.love += 1
        "Not all sports are bad":
            mike.say "I mean, yeah, Claire - some sports are boring."
            mike.say "And a lot of guys end up getting totally obsessed."
            mike.say "But you can't just dismiss all sports like that."
            claire.say "Oh, I think you'll find that I can."
            claire.say "And the only thing worse than a sports fan is a sports fan apologist!"
            $ claire.love -= 1
        "There are other games that you might enjoy":
            mike.say "Don't worry, Claire - I'm not into competitive sports."
            mike.say "No, the kind of games I like to play are more one-on-one."
            mike.say "And they're always played in private!"
            claire.say "Ooh...that sounds like fun!"
            claire.say "Will you teach me the rules?"
            $ claire.sub += 1
        "I want to be cured of my addiction":
            mike.say "I've been guilty of bingeing sports in the past, Claire."
            mike.say "But I'll stop watching them, if that's what makes you happy?"
            mike.say "It's just that, well...I might need your help to kick the habit."
            claire.say "Don't you worry about a thing, [hero.name]."
            claire.say "If you go cold turkey on one addiction, I'll feed another!"
            $ claire.sub -= 1
    return

label claire_talk_fashion_male:
    claire.say "I feel like the world of fashion's kind of left me behind, [hero.name]."
    claire.say "As a mother and housewife, you're not exactly keeping your finger on the pulse."
    claire.say "So it's going to take some work to catch up again."
    menu:
        "I think your look is pretty timeless":
            mike.say "I've always thought your look was pretty timeless, Claire."
            mike.say "So you shouldn't have to try too hard."
            mike.say "Because that kind of thing never really goes out of fashion."
            claire.say "Oh, you really think so?"
            claire.say "Thank you, [hero.name]!"
            $ claire.love += 1
        "You really shouldn't be so obsessed with your appearance":
            mike.say "Wait a minute, Claire - aren't you women always saying you resent that kind of stuff?"
            mike.say "Like, I hear girls complaining that they're expected to look pretty all the time."
            mike.say "So why would you want to put yourself through that?"
            claire.say "Bloody hell, [hero.name], it's not like I want to become a catwalk model!"
            claire.say "There's a happy medium between that and looking like a hopeless frump."
            $ claire.love -= 1
        "You'd better run those outfits by me first!":
            mike.say "That all sounds great, Claire..."
            mike.say "But remember to get my approval first."
            mike.say "I don't want you going out in something that's not appropriate."
            claire.say "You...you're serious?"
            claire.say "You think I'd wear some thing you don't approve of?"
            $ claire.sub += 1
        "I'm sure whatever you wear will look amazing!":
            mike.say "Let's face it, Claire - you'd look amazing in a bin-bag!"
            mike.say "I'm sure whatever you wear will get you right back on track."
            mike.say "And I can't wait to be seen with you once you've got it on."
            claire.say "Thank you, [hero.name]..."
            claire.say "You always seem to know just what to say!"
            $ claire.sub -= 1
    return

label claire_talk_books_male:
    claire.say "I feel like I haven't read a good book in years."
    claire.say "And it's definitely something that I want get back into."
    claire.say "Any recommendations to get me started?"
    menu:
        "Sure, I bet we have a lot in common":
            mike.say "I can have a think about it, Claire."
            mike.say "You should probably tell me what you like to read first."
            mike.say "But I think we'll probably have a lot in common when it comes to books."
            claire.say "You really think so?"
            claire.say "I hope we do."
            $ claire.love += 1
        "I might be a little too high brow for you":
            mike.say "I'm not sure about that, claire."
            mike.say "I like to read pretty high-brow stuff."
            mike.say "And I'm not sure you're up to it!"
            claire.say "What are you trying to say?"
            claire.say "That you think I'm stupid?!?"
            $ claire.love -= 1
        "I'll have to vet the choices first":
            mike.say "Sure thing, Claire - but I'll have to vet them first."
            mike.say "You just admitted it's been a while since you read a book."
            mike.say "So I don't want to give you too much of a challenge and scare you off!"
            claire.say "Oh, well..."
            claire.say "When you put it like that..."
            $ claire.sub += 1
        "How about you pick some reading material for me?":
            mike.say "Actually, Claire, I'm curious about your bookshelf."
            mike.say "I bet there are some interesting titles on there."
            mike.say "So how about you suggest some books for me to read?"
            claire.say "Huh...I never thought of that!"
            claire.say "Why the hell not?"
            $ claire.sub -= 1
    return

label claire_talk_people_male:
    claire.say "A lot of people tell me that I've lead a sheltered life, that I'm not worldly."
    claire.say "But I don't think that stops me from being a god judge of character, you know?"
    claire.say "And I can't help thinking that, save for a few notable exceptions, people are basically good."
    menu:
        "I think that's true":
            mike.say "People say the same thing about me for being young, Claire."
            mike.say "But I think they're all wrong."
            mike.say "And I agree with you about people too."
            claire.say "Good to know that, [hero.name]."
            claire.say "I think we're in fine company."
            $ claire.love += 1
        "You do seem a little naive":
            mike.say "You do seem to be a little naive, Claire."
            mike.say "So I can see why they'd say that about you."
            mike.say "And your ability to judge a person's character too."
            claire.say "Oh, is that so?"
            claire.say "Well at least I'm not a complete cynic, like some people I could mention!"
            $ claire.love -= 1
        "You just need to be educated":
            mike.say "Well of course you're not going to be a good judge of character, Claire..."
            mike.say "You've been trapped inside the house for years - but that's not your fault."
            mike.say "You just need to leave all of that stuff up to someone with more experience."
            mike.say "Some one like me."
            claire.say "You really think so?"
            claire.say "I guess that could work."
            $ claire.sub += 1
        "Don't ask me, I'm totally hopeless!":
            mike.say "Please don't ask me for an opinion, Claire..."
            mike.say "I wouldn't know where to even start!"
            mike.say "In fact, it sounds like you'd know better than me."
            claire.say "Is that so?"
            claire.say "Well, I don't mind taking the lead."
            $ claire.sub -= 1
    return

label claire_talk_computers_male:
    claire.say "I think I get computers, [hero.name] - I mean, we had one at home."
    claire.say "Not that I tended to get much use out of it though."
    claire.say "That was more Adam and Hector's kind of thing."
    menu:
        "Don't worry, it's easy":
            mike.say "I wouldn't worry about it too much, Claire."
            mike.say "Computers are pretty easy to handle these days."
            mike.say "I'll bet we can get you up to speed in no time."
            claire.say "You really think so?"
            claire.say "That would be great!"
            $ claire.love += 1
        "Oh no, not another technophobe!":
            mike.say "You really can't avoid using computers in the modern world, Claire."
            mike.say "And if you had one in the house then you could have learned how to use it."
            mike.say "So you only really have yourself to blame."
            claire.say "Are you serious?"
            claire.say "That is so insensitive."
            $ claire.love -= 1
        "I know computers seem scary":
            mike.say "I get it, Claire - computers are scary."
            mike.say "But don't worry your pretty little head about it."
            mike.say "I can handle them for you."
            claire.say "You'd really do that for me?"
            claire.say "Well, it would make things easier..."
            $ claire.sub += 1
        "You're right, computers are bad":
            mike.say "I know that I seem to be okay with them, Claire..."
            mike.say "But the truth is that I'm a technological fraud."
            mike.say "I really don't know the first thing about them!"
            claire.say "Hah...I knew it!"
            claire.say "It couldn't just be my generation."
            $ claire.sub -= 1
    return

label claire_talk_music_male:
    claire.say "I'm not like most people my age when it comes to music."
    claire.say "I mean sure, of course I like the stuff from when I was young."
    claire.say "But I really love a lot of the more modern songs I hear too."
    menu:
        "That's refreshing to hear":
            mike.say "That's really to your credit, Claire..."
            mike.say "Most people a little older than me hate new music."
            mike.say "It's like they take it as personal insult or something!"
            claire.say "Not me..."
            claire.say "I really enjoy it!"
            $ claire.love += 1
        "You're just saying that":
            mike.say "Are you really sure about that, Claire?"
            mike.say "Like, most people your are that say that..."
            mike.say "They're usually just trying to sound cool."
            claire.say "Hey, I was being sincere!"
            claire.say "I don't lie - at least not when it comes to music."
            $ claire.love -= 1
        "I bet you don't know what the best of it is":
            mike.say "You say that, Claire..."
            mike.say "But I'll bet you don't really know what the best of it is."
            mike.say "Don't worry though - I'll soon educate you."
            claire.say "Oh...erm..."
            claire.say "Thank you - I suppose!"
            $ claire.sub += 1
        "I'm totally clueless when it comes to music!":
            mike.say "You do?!?"
            mike.say "Well that's great news, Claire..."
            mike.say "You can help me out then - because I don't have a clue where to begin!"
            claire.say "Are you being serious?"
            claire.say "I...I suppose I could share what I know."
            $ claire.sub -= 1
    return

label claire_talk_birthday_male:
    mike.say "Happy birthday, Claire!"
    mike.say "Hope you're having a great day?"
    claire.say "Oh, thank you, [hero.name]!"
    claire.say "It's so nice of you to remember."
    return

init:
    define nickname_pumpkin = ["Pumpkin", "pumpkin"]

label command_nickname_claire:
    menu:

        "Call me Pumpkin" if active_girl.flags.mikeNickname not in nickname_pumpkin and active_girl.love > 100:
            $ active_girl.flags.mikeNickname = "Pumpkin"
        "Stop calling me Pumpkin" if active_girl.flags.mikeNickname in nickname_pumpkin:
            $ active_girl.flags.mikeNickname = None
        "Cancel":


            jump command_girl
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
