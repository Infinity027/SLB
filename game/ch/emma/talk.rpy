label emma_talk_love_male:
    show emma
    if emma.love < 80:
        emma.say "Love is being there for someone, and being able to rely on those same people being there for you."
        emma.say "I used to always be there for my sisters. And they were there for me."
        mike.say "It sounds like there's a story there."
        emma.say "There is, but not right now."
    elif emma.status == "girlfriend" or emma.love > 175:
        emma.say "Love is...I read a lot about love, but I always thought it was for other people."
        show emma blush
        emma.say "But then I found you, and..."
        emma.say "I, um. I guess that's, um. Maybe the stories are all right after all!"
    elif emma.love < 50 and emma.sexperience > 0:
        show emma angry
        emma.say "You're not one to talk about love."
        hide emma
        return
    else:
        emma.say "I think I understand why anime girls get heart eyes now."
        mike.say "Why's that?"
        show emma blush
        emma.say "It's...that feeling in your stomach you get when you see someone you love. Like butterflies but made of chocolate!"
        emma.say "And that smell on their clothes. One whiff and your mind is far away, like a private cloud to a dream."
        mike.say "Wow."
        emma.say "Can I borrow your shirt?"
        mike.say "What?!"
        "Emma giggles."
        emma.say "Never mind!"
    $ emma.love += 1
    hide emma
    return

label emma_talk_sex_male:
    show emma blush
    if emma.love < 50 and emma.sexperience == 0:
        emma.say "Oh, um, I. It's fun in manga!"
        "I look at her, trying to conceal my amusement."
        emma.say "Shut up!"
        mike.say "I didn't say anything!"
        emma.say "I heard you thinking it."
    elif emma.love < 150 and emma.sexperience == 0:
        emma.say "Oh, um, I..."
        "Emma trails off, as though she had intended to complete the thought but didn't."
        mike.say "You what?"
        emma.say "Oh! I've been thinking about sex a lot lately, I guess."
        mike.say "Oh!"
        "Her voice quickens a little bit."
        emma.say "It's the new issues of Orange Highway. The lead, uh, Hikaru is very, um."
        "She turns away from me, and then mumbles something, but I can't pick it out."
        mike.say "What was that?"
        emma.say "Oh, um. He reminds me of you, a little."
    elif emma.sexperience == 0:
        emma.say "I've been thinking."
        mike.say "About sex?"
        emma.say "Yes."
        mike.say "And?"
        emma.say "And you."
        mike.say "Oh!"
        emma.say "So, um, how's work going?"
    elif emma.sexperience == 1:
        emma.say "It was...everything I ever imagined. And completely different at the same time."
        emma.say "I loved feeling you inside me, but even more than that I loved the feeling of you holding me, afterward."
        emma.say "I loved falling asleep, smelling you."
        emma.say "Did you know you smell different after sex?"
        mike.say "I did not know that."
        emma.say "Neither did I!"
        mike.say "Is it a good thing?"
        emma.say "Let's just say I want to smell it again."
        "And then she offers me a wink."

    elif emma.love < 50:
        show emma angry
        emma.say "Don't ask me about that."
        hide emma
        return
    elif not emma.flags.pregnant:
        show emma happy
        emma.say "I love it when I'm next to you at night."
        emma.say "The orgasm is good, but the closeness is better."
    else:
        show emma happy
        "Emma puts a hand on her belly."
        emma.say "I think this tells you exactly what I think of sex."
    $ emma.love += 1
    hide emma
    return

label emma_talk_politics_male:
    show emma angry
    emma.say "Politics is just a reason for people to hate each other. Even the ones who say to come together just spread hate."
    emma.say "I hate it."
    $ emma.love -= 1
    hide emma
    return

label emma_talk_food_male:
    show emma
    if not emma.pregnant:
        emma.say "I know I need to eat better, but I can never quite manage to do it. It just takes too much time away from other stuff I want to do."
    else:
        emma.say "It's like everything I want to eat has changed now that I'm pregnant. Suddenly I love sour things and hate chocolate."
        emma.say "It's just not fair that I hate chocolate now."
        emma.say "But for this, I guess I can get over that!"
    hide emma
    return

label emma_talk_travels_male:
    show emma
    emma.say "I really want to visit Japan. I'd love to move there for a year, maybe get a job teaching English to little kids."
    mike.say "Do you know Japanese?"
    show emma happy
    emma.say "A little! I took two years in college. I'd need more to teach there, but it's a long term goal!"
    $ emma.love += 1
    hide emma
    return

label emma_talk_tv_male:
    show emma annoyed
    emma.say "I don't really watch much TV. I do like anime, but I like manga more."
    hide emma
    return

label emma_talk_sports_male:
    show emma
    if emma.sexperience < 3:
        show emma annoyed
        emma.say "I was never really good at sports. In school, all the boys said it was because I'm a girl."
        emma.say "But the other girls were a lot better at them than I was."
        emma.say "Anyway none of that really matters."
        $ emma.love -= 1
    else:
        emma.say "I've been a lot more active lately, thanks to you. It's got me wanting to work out more just so I can keep up with you."
    hide emma
    return

label emma_talk_fashion_male:
    show emma
    if emma.love < 80:
        show emma annoyed
        emma.say "I'm not really into fashion that much."
    elif not emma.pregnant:
        emma.say "I like to say I'm not really into fashion, but I can't help picking out clothes that make me feel closer to the people and things I love."
    else:
        emma.say "I'm not into fashion, and maternity shopping is seriously the worst. It's all so...bleh."
    return

label emma_talk_books_male:
    show emma happy
    emma.say "I love books, and I love libraries. I spent a lot of time in our library in school."
    emma.say "Our teachers always said that reading opens your mind. And it does!"
    emma.say "So I try to read a little bit of everything. I've read all the classics -- you have to getting a teaching degree."
    emma.say "Those are great for knowing who we are as people."
    emma.say "But really, I like a lot of fiction. A little fantasy and scifi, but mostly manga. And maybe a few other things."
    mike.say "Manga, huh?"
    show emma blush
    emma.say "I, uh, I mean some of the Japanese b--people can be so {b}cute{/b}!"
    hide emma
    $ emma.love += 1
    return

label emma_talk_people_male:
    show emma
    emma.say "People can really be a mystery sometimes. Some people are loving and caring and genuine."
    emma.say "And some people are mean and full of hate, and you know from the first second that you want nothing to do with them."
    emma.say "Those are fine, I guess. But the worst are the ones who act like the first kind and turn out to be the second kind."
    show emma sad
    emma.say "Those people just like to hurt you."
    $ emma.love -= 1
    if emma.love > 100:
        show emma normal
        emma.say "I'm glad you're not one of those people, [hero.name]!"
    hide emma
    return

label emma_talk_computers_male:
    show emma
    if emma.love < 80:
        emma.say "I just use computers for teaching stuff, mostly. Internet research, grading papers, stuff I can't do on my phone."
    else:
        emma.say "You want to know a secret?"
        mike.say "Always."
        if emma.love < 120 or not emma.flags.confessedvn:
            emma.say "I really like visual novels. They're like manga, but you get to be {b}in{/b} the manga! I mean, lots of them aren't as good."
            show emma happy
            emma.say "But people on the internet can surprise you and make really good stuff sometimes."
            $ emma.flags.confessedvn = True
        else:
            emma.say "There's a whole bunch of erotic visual novels on the internet that I really like."
            mike.say "Oh yeah, I may've played a few of them. Though they seem a little more hardcore than you'd usually go for?"
            show emma blush
            emma.say "Maybe a little, but...sometimes I like that."
            if emma.love > 150 and emma.sexperience > 3:
                emma.say "Want to re-enact one sometime?"
                mike.say "Oh! That sounds...interesting!"
        $ emma.love += 1
    hide emma
    return

label emma_talk_music_male:
    show emma
    emma.say "I listen to whatever's on the radio. A little J-Pop and K-Pop sometimes, when the mood strikes me. Music doesn't move me as well as reading does."
    hide emma
    return

label emma_talk_birthday_male:
    show emma
    mike.say "Happy birthday, Emma!"
    show emma happy
    emma.say "Thank you, [hero.name]!"
    if emma.love > 120 and emma.sexperience > 3:
        show emma normal
        emma.say "I know what you can get me for my birthday!"
        mike.say "What's that?"
        emma.say "I want a picture of you standing there, leaning against the wall, with a \"come hither\" look on your face."
        mike.say "That's it?"
        show emma happy
        emma.say "No, then I'm going to put that on a body pillow so I can sleep with you {b}every{/b} night!"
    hide emma
    $ emma.love += 5
    return

init:
    define nickname_dreamboat = ["Dreamboat", "dreamboat"]
    define nickname_senpai = ["Senpai", "senpai"]
    define nickname_my_prince = ["My Prince", "my prince"]
    define nickname_my_king = ["My King", "my king"]

label command_nickname_emma:
    menu:

        "Call me Honey" if active_girl.flags.mikeNickname not in nickname_honey and "emma_fuck_date_third" in DONE:
            $ active_girl.flags.mikeNickname = "Honey"
        "Stop calling me Honey" if active_girl.flags.mikeNickname in nickname_honey:
            $ active_girl.flags.mikeNickname = None


        "Call me Dreamboat" if active_girl.flags.mikeNickname not in nickname_dreamboat and "emma_fuck_date_fifth" in DONE:
            $ active_girl.flags.mikeNickname = "Dreamboat"
        "Stop calling me Dreamboat" if active_girl.flags.mikeNickname in nickname_dreamboat:
            $ active_girl.flags.mikeNickname = None


        "Call me Senpai" if active_girl.flags.mikeNickname not in nickname_senpai and "emma_fuck_date_ninth" in DONE:
            $ active_girl.flags.mikeNickname = "Senpai"
        "Stop calling me Senpai" if active_girl.flags.mikeNickname in nickname_senpai:
            $ active_girl.flags.mikeNickname = None


        "Call me My Prince" if active_girl.flags.mikeNickname not in nickname_my_prince and "emma_fuck_date_seventh" in DONE and active_girl.love > 180:
            $ active_girl.flags.mikeNickname = "My Prince"
        "Stop calling me My Prince" if active_girl.flags.mikeNickname in nickname_my_prince:
            $ active_girl.flags.mikeNickname = None


        "Call me My King" if active_girl.flags.mikeNickname not in nickname_my_king and "emma_fuck_date_seventh" in DONE and active_girl.sub > 90:
            $ active_girl.flags.mikeNickname = "My King"
        "Stop calling me My King" if active_girl.flags.mikeNickname in nickname_my_king:
            $ active_girl.flags.mikeNickname = None
        "Cancel":


            jump command_girl

label submissive_interact_emma_male:
    mike.say "Hey, Emma..."
    mike.say "Would you be cool with saying hi to me in a certain way?"
    show emma surprised
    emma.say "Erm...what do you mean, [hero.name]?"
    emma.say "Like in a different language or something?"
    show emma normal
    mike.say "No, not like that."
    mike.say "I was thinking more like something to do with how we met."
    mike.say "Like how I saw you in a dream, and I'm a dream come true?"
    if emma.sub >= 70 or emma.is_sex_slave:
        show emma talkative
        emma.say "It...sounds a little weird, [hero.name]."
        emma.say "But if that's what you really want."
        emma.say "Then I'll do my best."
        $ emma.flags.submissive_interact = True
    else:
        show emma whining
        emma.say "I...I couldn't do something like that, [hero.name]."
        emma.say "I'd be scared of what people might think!"
        show emma sad
        mike.say "Okay, Emma - let's forget about that idea."
        $ emma.love -= 4
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
