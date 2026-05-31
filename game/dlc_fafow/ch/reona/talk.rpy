label reona_talk_love_male:
    reona.say "You know what..."
    reona.say "I think love's kind of overrated, yeah?"
    reona.say "Like, it's nice to have - but I'd rather just have fun."
    reona.say "Love's just a way of keeping people in line."
    menu:
        "Fun and love at the same time is pretty special":
            show reona annoyed
            mike.say "I don't think so, Reona."
            mike.say "Being in love doesn't mean you can't have fun."
            mike.say "In fact, enjoying everything with one person is pretty special!"
            $ reona.love -= 1
        "Fun comes first":
            show reona happy
            mike.say "I know just what you mean, Reona."
            mike.say "People are too quick to jump into things."
            mike.say "They should take time to enjoy their lives more."
            $ reona.love += 1
        "That is what I want to hear" if hero.charm >= 50:
            show reona flirt
            mike.say "Got it in one, Reona!"
            mike.say "Like, you'd never stand in the way of me having fun, would you?"
            mike.say "You're not prudish or jealous, and I like that about you..."
            $ reona.sub += 1
    return

label reona_talk_sex_male:
    reona.say "You won't believe me, [hero.name]..."
    reona.say "But I used to have all kinds of hang-ups about sex!"
    reona.say "And then I guess I just learned how to let it all go."
    reona.say "Since then, I never looked back!"
    menu:
        "I admire your liberation":
            show reona happy
            mike.say "Wow, Reona..."
            mike.say "You're such a free-spirit!"
            mike.say "I could never keep you caged..."
            $ reona.sub -= 1
        "You are an example for us all":
            show reona happy
            mike.say "If only more girls could be like you, Reona."
            mike.say "Hell, more guys too!"
            mike.say "You're so free and liberated."
            mike.say "It's a real breath of fresh air!"
            $ reona.love += 1
        "It looks like hedonism":
            mike.say "Hmmm..."
            show reona annoyed
            mike.say "I think you can be a little too free and easy, Reona."
            mike.say "Having boundaries is never a bad thing."
            mike.say "And it helps you to respect yourself too."
            $ reona.love -= 1
    return

label reona_talk_politics_male:
    show reona annoyed
    reona.say "Urgh..."
    reona.say "Politics...boring!"
    reona.say "Who cares about dull shit like that?"
    menu:
        "Serious things are not for you":
            mike.say "Well of course you find it boring, Reona."
            mike.say "Politics is serious stuff, very detailed."
            mike.say "You'd never have the patience to understand it!"
            $ reona.love -= 1
        "Let serious things to me":
            if reona.sub >= 25:
                show reona happy
            else:
                show reona angry
            mike.say "Don't worry about all the big words and complex ideas, Reona."
            mike.say "You just fill your pretty little head up with frivolous stuff."
            mike.say "Let me worry about the important things for you..."
            if reona.sub >= 25:
                $ reona.sub += 1
            else:
                $ reona.love -= 1
        "For a change, an honest opinion":
            mike.say "At least you say it like it is, Reona."
            mike.say "Some people try to sound clever and fake it."
            mike.say "But you're pretty honest about not being interested."
            $ reona.love += 1
    return

label reona_talk_food_male:
    reona.say "To me, food's kinda like sex, yeah?"
    reona.say "It's not like it just tastes good."
    reona.say "It's like I need it to survive!"
    reona.say "Like my body can't cope without it!"
    menu:
        "Such an appetite":
            mike.say "I don't know about needing it, Reona."
            mike.say "But I do think you have an appetite for it."
            show reona annoyed
            mike.say "Like you're always binging!"
            $ reona.love -= 1
        "You have a point":
            show reona happy
            mike.say "I think you might be onto something there, Reona."
            mike.say "I know I always feel better after I've had sex."
            mike.say "Like it perks me up in lots of different ways at once."
            $ reona.love += 1
        "I am here for both" if reona.sub >= 25:
            mike.say "Don't worry about that appetite of yours, Reona."
            mike.say "Just keep me happy and I'll see you right."
            show reona flirt
            mike.say "In fact, I'll make sure you never go hungry again..."
            $ reona.sub += 1
    return

label reona_talk_travels_male:
    reona.say "I never understand people that want to go to far off places."
    reona.say "Like, travelling's a real pain in the butt."
    reona.say "And everywhere has the same fast-food chains these days."
    reona.say "So why go to all that trouble?"
    menu:
        "Home sweet home":
            show reona happy
            mike.say "I'm a homebody too, Reona."
            mike.say "Staying there with the right girl."
            mike.say "That's better than any holiday!"
            $ reona.love += 1
        "If you ever do, I'll follow":
            mike.say "I don't want to go anywhere without you, Reona."
            mike.say "So promise you won't go leaving me behind, okay?"
            mike.say "You promise?"
            $ reona.sub -= 1
        "Travels broadens the mind":
            mike.say "Not everyone's happy to stay home, Reona."
            mike.say "And they do say travel broadens the mind."
            show reona angry
            mike.say "Which wouldn't do you any harm..."
            $ reona.love -= 1
    return

label reona_talk_tv_male:
    reona.say "I love TV, [hero.name]..."
    reona.say "Especially all those reality shows!"
    reona.say "I always wonder if I should try out for one of them."
    reona.say "You know, see if I have what it takes?"
    menu:
        "You would be a celebrity":
            mike.say "You should so do that, Reona!"
            show reona happy
            mike.say "Being with a girl from a reality show would amazing!"
            mike.say "I'd feel like I was part of your entourage."
            mike.say "Like I'd have to do whatever you ordered me to..."
            $ reona.sub -= 1
        "You are better than that":
            show reona annoyed
            mike.say "I dunno, Reona..."
            mike.say "They tend to like bimbos and dim-witts on those shows."
            show reona angry
            mike.say "Do you really think your dumb and shallow enough?"
            $ reona.love -= 1
        "You would be the best":
            show reona happy
            mike.say "You should definitely do that, Reona."
            mike.say "With looks like your's, how could they say no?"
            mike.say "You'd floor them all!"
            $ reona.love += 1
    return

label reona_talk_sports_male:
    reona.say "I don't understand sports, [hero.name]!"
    reona.say "There are so many dumb rules to remember."
    reona.say "So many teams from all kinds of places."
    reona.say "And so many different sports too!"
    reona.say "It makes my head spin!"
    menu:
        "Of course, it's not for you":
            if reona.sub >= 25:
                show reona flirt
            else:
                show reona angry
            mike.say "Of course you don't understand sports, Reona!"
            mike.say "They're not meant for people like you."
            mike.say "So stop worrying about it, yeah?"
            mike.say "Just focus on looking pretty and putting out instead!"
            if reona.sub >= 25:
                $ reona.sub += 1
            else:
                $ reona.love -= 1
        "Of course, it's not for everyone":
            show reona happy
            mike.say "I think some people take sports too seriously, Reona."
            mike.say "They're only games for adults to play, after all."
            mike.say "How can you be so passionate about something like that?"
            $ reona.love += 1
        "Of course, you don't understand":
            show reona annoyed
            mike.say "Maybe the problem is that you don't understand, Reona?"
            mike.say "Did you ever think of actually leaning the rules?"
            mike.say "Then you'd at least know what's going on."
            $ reona.love -= 1
    return

label reona_talk_fashion_male:
    reona.say "I like to keep up to speed with fashion, you know?"
    reona.say "Like, I'm not a slave to it or anything like that."
    reona.say "I kinda pick and choose what I like, ignore what I don't."
    reona.say "You know what I mean?"
    menu:
        "You look good":
            show reona happy
            mike.say "You always look good to me, Reona."
            mike.say "But I have to be honest."
            show reona blush
            mike.say "I think you look best with nothing in at all!"
            $ reona.love += 1
        "You have your own... style":
            mike.say "Really, Reona?"
            mike.say "Wow..."
            show reona annoyed
            mike.say "I always thought you just bought the most revealing stuff you could find!"
            $ reona.love -= 1
        "Anything would suit you":
            mike.say "You could pull of anything, Reona."
            show reona happy
            mike.say "You have one of those perfect bodies."
            mike.say "In fact, I bet you could be a model!"
            $ reona.sub -= 1
    return

label reona_talk_books_male:
    reona.say "People always assume that I don't read books."
    reona.say "And, like, I don't."
    reona.say "But it's because I have a busy lifestyle."
    reona.say "Not because I can't concentrate for that long!"
    menu:
        "It's surprising":
            mike.say "Wow, Reona!"
            mike.say "I'm am amazed to hear that."
            show reona angry
            mike.say "I wasn't sure you could actually read at all!"
            $ reona.love -= 1
        "It's for the best":
            mike.say "That's probably for the best, Reona."
            if reona.sub >= 25:
                show reona flirt
            else:
                show reona angry
            mike.say "I think reading a very long book would confuse you."
            mike.say "Maybe even make your brain overheat!"
            if reona.sub >= 25:
                $ reona.sub += 1
            else:
                $ reona.love -= 1
        "It's honest":
            show reona happy
            mike.say "Of course, Reona, of course."
            mike.say "People are such snobs when it comes to reading."
            mike.say "In fact, I think most of them just pretend."
            mike.say "No way they've read so many big books!"
            $ reona.love += 1
    return

label reona_talk_people_male:
    reona.say "I don't like most people, [hero.name]."
    reona.say "They're nice to your face, sure."
    reona.say "But they always talk behind your back!"
    reona.say "But it's different when I do that."
    reona.say "Because my gossip is always the best!"
    menu:
        "Judge and be judged":
            mike.say "Well, I'm not surprised they do that, Reona."
            show reona annoyed
            mike.say "I mean, you're not exactly a saint, are you?"
            mike.say "You do tend to rub people up the wrong way!"
            $ reona.love -= 1
        "Don't let your ego suffer":
            show reona happy
            mike.say "You're right not to let people get to you, Reona."
            mike.say "You shouldn't let them affect your self-image."
            mike.say "The trick is to know yourself!"
            $ reona.love += 1
        "Against them, you are not alone":
            mike.say "Don't let the haters get to you, Reona."
            mike.say "They're just jealous, that's all."
            mike.say "But you can rely on me - I'll always appreciate your qualities!"
            $ reona.sub -= 1
    return

label reona_talk_computers_male:
    reona.say "Like...I don't get why people still need computers."
    reona.say "You can do so much shit on your phone, right?"
    reona.say "But all these nerd are like 'no, I need a computer, to do nerd stuff!'."
    reona.say "What's up with that?"
    menu:
        "The future is mobile":
            mike.say "Hah!"
            show reona happy
            mike.say "I know what you mean, Reona."
            mike.say "I'm pretty sure desktops are going to die out soon!"
            mike.say "I don't even use one of those at work anymore."
            $ reona.love += 1
        "It is complicated":
            mike.say "Yeah well..."
            show reona annoyed
            mike.say "Some people need to do more than just take selfies!"
            mike.say "And they use the internet for stuff other than social media."
            $ reona.love -= 1
        "Don't pretend" if hero.knowledge >= 50:
            mike.say "You don't have to pretend with me, Reona."
            show reona surprised blush
            mike.say "I know that you don't really understand stuff like computers."
            mike.say "I'll keep your secret - so long as you earn it..."
            $ reona.sub += 1
    return

label reona_talk_music_male:
    reona.say "Everyone says they like this kind of music or that kind of music."
    reona.say "But I'm not like that, you know?"
    reona.say "I have really broad tastes."
    reona.say "I like all different kinds of stuff."
    menu:
        "Music is art and deserves more effort":
            mike.say "Ah, come on, Reona!"
            show reona annoyed
            mike.say "That's just something clueless people say about music!"
            mike.say "It means you just listen to whatever garbage is on the radio!"
            $ reona.love -= 1
        "Music is universal and deserves open minds":
            show reona happy
            mike.say "Yeah..."
            mike.say "It kinda sucks when music gets tribal like that."
            mike.say "Better to be able to appreciate different things."
            $ reona.love += 1
        "It looks like the good way to listen music":
            mike.say "That makes so much sense, Reona!"
            mike.say "You know what..."
            mike.say "You should make me a playlist!"
            $ reona.sub -= 1
    return

label reona_talk_birthday_male:
    mike.say "Happy birthday, Reona!"
    mike.say "And many happy returns!"
    show reona surprised
    "Reona looks at me with a puzzled expression for a moment."
    "Then recognition dawns on her face."
    show reona happy
    reona.say "Oh yeah!"
    reona.say "Today is my birthday!"
    $ reona.love += 5
    reona.say "Thanks, [hero.name] - I almost didn't remember!"
    return

init:
    define nickname_teach = ["Teach", "teach"]
    define nickname_brainiac = ["Brainiac", "brainiac"]
    define nickname_genius = ["Genius", "genius"]

label command_nickname_reona:
    menu:

        "Call me Teach" if active_girl.flags.mikeNickname not in nickname_teach and active_girl.flags.study_help_count >= 1:
            $ active_girl.flags.mikeNickname = "Teach"
        "Stop calling me Teach" if active_girl.flags.mikeNickname in nickname_teach:
            $ active_girl.flags.mikeNickname = None


        "Call me Brainiac" if active_girl.flags.mikeNickname not in nickname_brainiac and hero.knowledge > 70:
            $ active_girl.flags.mikeNickname = "Brainiac"
        "Stop calling me Brainiac" if active_girl.flags.mikeNickname in nickname_brainiac:
            $ active_girl.flags.mikeNickname = None


        "Call me Genius" if active_girl.flags.mikeNickname not in nickname_genius and hero.knowledge > 50:
            $ active_girl.flags.mikeNickname = "Genius"
        "Stop calling me Genius" if active_girl.flags.mikeNickname in nickname_genius:
            $ active_girl.flags.mikeNickname = None
        "Cancel":


            jump command_girl
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
