label amy_talk_love_male:
    show amy
    amy.say "For some reason, when you're a goth..."
    amy.say "I dunno, some people just assume you're not into the whole love thing."
    amy.say "Like because your music's dark, they think you're miserable the whole time!"
    menu:
        "Indeed you are":
            mike.say "Yeah, I can see why they'd think that, Amy."
            mike.say "I mean, you are a pretty miserable bunch!"
            show amy sad
            mike.say "Maybe if you cheered up a bit, they'd change their minds?"
            $ amy.love -= 1
        "I don't think like these people":
            mike.say "Not me, Amy..."
            mike.say "I've always dreamed of being in the thrall of a gothic princess!"
            show amy flirt
            mike.say "And now my dream's come true!"
            $ amy.sub -= 1
        "Of course you are not":
            mike.say "Huh?"
            mike.say "It never seemed that way to me, Amy."
            show amy happy
            mike.say "I always thought goths were like, darkly passionate, you know?"
            mike.say "Really intense!"
            $ amy.love += 1
    return

label amy_talk_sex_male:
    show amy
    amy.say "I hate all of the politics and bullshit that comes along with sex."
    amy.say "If you ask me, all that's important is everyone enjoying themselves."
    amy.say "So long as nobody gets hurt, what's the problem?"
    menu:
        "Sex is power":
            mike.say "Oh, Amy..."
            mike.say "You obviously haven't been told what to do by the right guy yet."
            mike.say "Wait until I get you alone."
            show amy shy
            mike.say "I promise you'll be falling over yourself to do as I tell you!"
            $ amy.sub += 1
        "Sex is liberation":
            mike.say "You read my mind, Amy!"
            mike.say "I wish more of the girls I met in the past were like you."
            show amy happy
            mike.say "You'd think modern women would be more sexually liberated!"
            $ amy.love += 1
        "Sex is serious matter":
            mike.say "Hmm..."
            mike.say "I'm gonna sound like a prude, Amy..."
            mike.say "But I think you need to be more responsible."
            show amy annoyed
            mike.say "Playing fast and loose is how accidents happen."
            $ amy.love -= 1
    return

label amy_talk_politics_male:
    show amy
    amy.say "I know that I should pay more attention to stuff like politics."
    amy.say "But when they're all old white guys - on both sides too!"
    amy.say "How am I supposed to be interested in that?"
    amy.say "None of them are going to be appeal to me!"
    menu:
        "I will follow you":
            mike.say "I don't really know much about politics, Amy."
            mike.say "Most of it just goes over my head!"
            mike.say "But you sound like you know what you're talking about."
            show amy happy
            mike.say "So I'll take your word for it!"
            $ amy.sub -= 1
        "We have to change them":
            mike.say "Don't you get it, Amy?"
            mike.say "That's exactly why politics is all old white guys!"
            show amy surprised
            mike.say "You shouldn't be complaining."
            mike.say "Not if you aren't going to do anything to change it."
            $ amy.love -= 1
        "Politics need to change":
            mike.say "You've got a point, Amy."
            mike.say "We could do with more politicians from different backgrounds."
            show amy happy
            mike.say "Let's hope that we see that change happening soon."
            $ amy.love += 1
    return

label amy_talk_food_male:
    show amy
    amy.say "You ever get pissed at just how much different food there is in the world?"
    amy.say "Like, it looks so great - I want to be able to try all of it!"
    amy.say "But there's no way I can do that."
    amy.say "It's SO frustrating!"
    menu:
        "Food is food":
            mike.say "I dunno, Amy..."
            mike.say "I think most of it tastes the same."
            mike.say "They're just calling it something fancy."
            show amy sad
            mike.say "You know - so they can charge you more for it?"
            $ amy.love -= 1
        "If only we could...":
            mike.say "Tell me about it, Amy!"
            mike.say "I always wanted one of those replicators they have in sci-fi shows."
            mike.say "That way you could try something different at every meal!"
            show amy happy
            mike.say "Just imagine that!"
            $ amy.love += 1
        "I am a food expert" if hero.knowledge >= 50:
            mike.say "You should let me do the choosing for you, Amy."
            mike.say "I have excellent taste and a good eye for quality."
            show amy shy
            mike.say "Whether it's food or women..."
            $ amy.sub += 1
    return

label amy_talk_travels_male:
    show amy
    amy.say "I want to visit all the gothic hot-spots, you know?"
    amy.say "Like Whitby, where Dracula's ship ran aground!"
    amy.say "It's all Victorian and filled with cobbled streets."
    amy.say "Oh...and those romantic English accents!"
    menu:
        "We should go":
            mike.say "That sounds really cool, Amy."
            show amy happy
            mike.say "I'd love to visit Europe too someday."
            mike.say "So, tell me more about this Whitby place?"
            $ amy.love += 1
        "Or we could go somewhere else":
            mike.say "Urgh..."
            mike.say "It always rains in England."
            mike.say "And their food sucks too."
            show amy sad
            mike.say "Don't you want to go anywhere warm?"
            $ amy.love -= 1
        "We should go properly":
            mike.say "Oh wow..."
            mike.say "We could like, dress up in period costume."
            mike.say "You could be a Victorian noble-woman, Amy."
            show amy happy
            mike.say "Or a vampire princess - with me as your loyal subject!"
            $ amy.sub -= 1
    return

label amy_talk_tv_male:
    show amy
    amy.say "I can't get enough TV these days - it's crazy!"
    amy.say "There's so many games made into series, books made into series..."
    amy.say "Hell, there's even movies made into series!"
    amy.say "How am I supposed to watch it all?"
    menu:
        "You should let me help organize":
            mike.say "I know exactly what you mean, Amy."
            mike.say "We need to make sure that we don't miss out."
            mike.say "So how about we make a pact?"
            show amy happy
            mike.say "How about we watch all those series together?"
            $ amy.love += 1
        "You should prioritize":
            mike.say "You sound like you need help making up your mind, Amy!"
            mike.say "Just leave it to me to choose what you watch from now on."
            mike.say "That way you can be sure you're watching the best."
            $ amy.sub += 1
        "You should go out too":
            mike.say "Meh..."
            mike.say "I bet most of them are just lazy rip-offs and crappy reboots."
            show amy annoyed
            mike.say "You really should get out and touch grass more, Amy!"
            $ amy.love -= 1
    return

label amy_talk_sports_male:
    show amy annoyed
    amy.say "Urgh..."
    amy.say "Sports, sports, sports!"
    amy.say "That's all people want to talk about!"
    amy.say "It's SO boring!"
    menu:
        "A waste of energy":
            mike.say "I'm not interested in sports, Amy."
            mike.say "They're pointless, a real waste of energy."
            show amy happy
            mike.say "Especially when I could be using that energy to please you..."
            $ amy.sub -= 1
        "A lack of personality":
            mike.say "I know what you mean, Amy."
            mike.say "It's like some people can't cope without sports."
            mike.say "Like they use being into it to hide not having a personality!"
            mike.say "Am I right or what?"
            $ amy.love += 1
        "A statement from a goth":
            mike.say "Oh, Amy..."
            mike.say "That's such a stereotypical goth statement!"
            show amy annoyed
            mike.say "Just because you got picked last in gym class..."
            mike.say "You don't have to ruin it for everyone else!"
            $ amy.love -= 1
    return

label amy_talk_fashion_male:
    show amy
    amy.say "As a goth, you always get people treating it like it's just a fashion."
    amy.say "They ask if that's what's in this season."
    amy.say "Or they try to tell you that the look was so last season."
    amy.say "None of them seem to realise it's a lifestyle choice!"
    menu:
        "People are shallow":
            mike.say "That's just because they're shallow, Amy."
            mike.say "They're obsessed with what they see on the surface."
            show amy happy
            mike.say "And they can't appreciate what lies beneath."
            $ amy.love += 1
        "It is not just fashion?!?":
            mike.say "You mean all of that black isn't a fad?"
            mike.say "I was kind of hoping you might move on soon!"
            show amy annoyed
            mike.say "I mean...I'd like to see you in some bright colours..."
            $ amy.love -= 1
        "I can see through these dark veils" if hero.charm >= 50:
            mike.say "I know it's more than a fashion statement, Amy."
            mike.say "Because I can read you like a book."
            mike.say "Trust me, you'll never find another guy that understands you."
            show amy shy
            mike.say "Not like I do..."
            $ amy.sub += 1
    return

label amy_talk_books_male:
    show amy
    amy.say "You read any good books lately, [hero.name]?"
    amy.say "When you're a goth, people assume you only read gloomy stuff."
    amy.say "So nobody ever recommends anything fun to me!"
    menu:
        "What do you usually read?":
            mike.say "I was going to ask you the same thing, Amy!"
            mike.say "You're so interesting, so dark and edgy..."
            show amy happy
            mike.say "I'd love to know what you read!"
            $ amy.sub -= 1
        "What would suit your tastes?":
            mike.say "I dunno, Amy..."
            mike.say "I still think my choice of reading material would be too happy for you."
            show amy upset
            mike.say "But if I come across something about teenage vampires, I'll hook you up."
            $ amy.love -= 1
        "What do you want to read?":
            mike.say "Sure, Amy - I'd be happy to recommend something."
            mike.say "I read all kinds of stuff, from comic-books to classics."
            show amy happy
            mike.say "Did you have anything in mind?"
            mike.say "Or would you just like me to suggest something I think you'll enjoy?"
            $ amy.love += 1
    return

label amy_talk_people_male:
    show amy annoyed
    amy.say "People suck, you know?"
    amy.say "Yeah, yeah - big surprise, the goth chick hates people!"
    amy.say "But they DO suck!"
    amy.say "They're shallow, ignorant, and worst of all, judgemental!"
    menu:
        "Too bad for them!":
            mike.say "I wish more people took the time to get to know the real you, Amy."
            mike.say "Because when you do, there's a hell of a lot to like."
            show amy happy
            mike.say "But I guess that's their loss and my gain!"
            $ amy.love += 1
        "Judgemental, you said?":
            mike.say "Wow..."
            show amy surprised
            mike.say "Do you ever actually listen to yourself, Amy?"
            show amy upset
            mike.say "Because you're guilty of pretty much all that stuff yourself!"
            $ amy.love -= 1
        "Lucky you!" if hero.charm >= 50:
            mike.say "You're lucky you met a guy like me, Amy."
            show amy shy
            mike.say "I appreciate you for who you really are."
            mike.say "But other people won't, so just you do as I say, okay?"
            mike.say "That way, everything will turn out fine..."
            $ amy.sub += 1
    return

label amy_talk_computers_male:
    show amy
    amy.say "It's hard being a female goth around computers, [hero.name]."
    amy.say "Because you're a girl, half of the people in the store assume I'm clueless."
    amy.say "But because most goths are a little nerdy too, half assume I'm a genius!"
    amy.say "The truth is that I'm somewhere in the middle!"
    menu:
        "But you are a genius!":
            mike.say "I bet you know more than I do, Amy!"
            mike.say "That's one of the best things about knowing you."
            mike.say "Whenever I'm unsure, I can always rely on you to tell me how it is!"
            $ amy.sub -= 1
        "You are more than that":
            mike.say "People are too quick to judge on appearances, Amy."
            mike.say "All they see is a girl or a goth."
            mike.say "That's why I'm glad that we've become friends."
            show amy happy
            mike.say "Because it means I know the real you."
            $ amy.love += 1
        "Looks can be deceiving":
            mike.say "You can't blame people for making assumptions, Amy."
            mike.say "That kind of comes along with having such a strong look."
            show amy annoyed
            mike.say "Either tone it down or get used to it!"
            $ amy.love -= 1
    return

label amy_talk_music_male:
    show amy
    amy.say "I kinda hate it when people assume goth is all one kind of music."
    amy.say "There's goth metal, folk goth, electro goth..."
    amy.say "So many kinds I couldn't list them all!"
    amy.say "There's probably a goth for everyone out there!"
    menu:
        "Anyway, they all seem more or less the same":
            mike.say "Yeah, yeah, yeah..."
            mike.say "You say that they're different, Amy."
            show amy annoyed
            mike.say "But I'm sure they all sound the same to non-goths."
            mike.say "Just pasty dudes in black, singing about being miserable!"
            $ amy.love -= 1
        "I didn't know that":
            mike.say "Is that right, Amy?"
            mike.say "Wow...I had no idea!"
            mike.say "You've got to introduce me to some of them."
            show amy happy
            mike.say "Because they sound really interesting!"
            $ amy.love += 1
        "Wanna try my tastes in music?":
            mike.say "You should let me introduce you to my tastes in music, Amy."
            mike.say "I promise you that it'd break you out of your little rut."
            show amy shy
            mike.say "Open your mind to a whole new world of possibilities."
            $ amy.sub += 1
    return

label amy_talk_birthday_male:
    show amy
    mike.say "Happy birthday, Amy!"
    mike.say "Do goths say stuff like 'many happy returns'?"
    mike.say "Or is that too cheerful?"
    $ amy.love += 5
    show amy happy
    "Amy smiles and shakes her head."
    amy.say "Yeah, it kind of is..."
    amy.say "But then you're not a goth, [hero.name]."
    amy.say "So I guess it's okay for you to say it!"
    return

label amy_talk_love_female:
    bree.say "You believe in true love, right, Amy?"
    bree.say "I mean, not like a fairy tale."
    bree.say "More like love's real and it can work."
    amy.say "Ah...I'd like to, [hero.name]."
    amy.say "But that kind of stuff's for some time down the road."
    amy.say "Right now I just want to have some serious fun!"
    return

label amy_talk_sex_female:
    bree.say "What's your philosophy on sex, Amy?"
    bree.say "Are you saving yourself for the right guy or girl?"
    bree.say "Or are you the kind that likes to experiment and try everything on for size?"
    amy.say "I want to try it all, [hero.name] - sample every flavour!"
    amy.say "If I don't, then I'm going to be missing out."
    amy.say "Who wants to pass on something that might be the best thing ever?"

    return

label amy_talk_politics_female:
    bree.say "Do you get involved in politics, Amy?"
    bree.say "You know, like protests and marches?"
    bree.say "Make your voice heard by shouting it out loud?"
    amy.say "Nah, that's too much hassle for me."
    amy.say "I'm not into confrontation, [hero.name]."
    amy.say "I'm more the laid back type."

    return

label amy_talk_food_female:
    bree.say "You want to try some of this soup, Amy?"
    bree.say "I made it myself, using all natural ingredients!"
    amy.say "Urgh...no way, [hero.name]!"
    amy.say "That sounds like hippy food!"
    amy.say "I don't trust anything that doesn't come out of a can."
    amy.say "And I won't eat it until it's been blasted in a microwave either!"

    return

label amy_talk_travels_female:
    bree.say "Have you been anywhere exotic, Amy?"
    bree.say "It seems like everyone wants to travel the world!"
    amy.say "No, [hero.name]...I've never been anywhere that's not here."
    amy.say "But why would I want to go some place else?"
    amy.say "This is where all my stuff is!"
    return

label amy_talk_tv_female:
    bree.say "See anything good on the TV recently, Amy?"
    bree.say "I'm always looking for tips to top up the VCR!"
    amy.say "Oh hell, [hero.name]...where do I even start?"
    amy.say "There's the new series of Weirder Shit."
    amy.say "The Marvellous Expanded Universe stuff!"
    amy.say "And some wicked shows from Korea too!"
    bree.say "Hold that thought, Amy!"
    bree.say "I'll go grab a pen and paper!"

    return

label amy_talk_sports_female:
    bree.say "I don't want to just assume that you're not into sports, Amy."
    bree.say "You know, because you're a goth - and the two don't really go together?"
    bree.say "But I'm right, aren't I - you probably hate sports?"
    amy.say "Yeah, yeah...I fucking hate them!"
    amy.say "They're just an excuse for dumb jocks to feel like they're good for something."
    amy.say "And I can think of far better ways to get exercise too..."

    return

label amy_talk_fashion_female:
    bree.say "What's new in the world of goth fashion, Amy?"
    bree.say "I mean, did they finally discover a new shade of black?"
    amy.say "Hey, watch it, [hero.name]!"
    amy.say "Goth's not some frivolous fashion trend, you know?"
    amy.say "It's literally a way of life!"
    return

label amy_talk_books_female:
    bree.say "Are you one of those bookish goths, Amy?"
    bree.say "Or the tougher ones that are in it for the tattoos and piercings?"
    amy.say "What are you trying to say, [hero.name]?"
    amy.say "I read books, lots of books!"
    amy.say "There isn't one about a sensitive, misunderstood vampire I haven't read!"

    return

label amy_talk_people_female:
    bree.say "Most goths don't seem to like people, Amy."
    bree.say "Well, they don't seem to like people that aren't goths!"
    bree.say "How about you?"
    amy.say "People are shit, [hero.name]!"
    amy.say "So why would I like them?"
    bree.say "Well, when you put it like that..."

    return

label amy_talk_computers_female:
    bree.say "Do you do computers, Amy?"
    bree.say "I mean, I know you work in an electronics store."
    bree.say "But you're not living a primitive lifestyle in your time off, right?"
    amy.say "Of course I do computers, [hero.name] - most goths do!"
    amy.say "They let you communicate with other goths."
    amy.say "And you don't have to go out in direct sunlight to do it."
    amy.say "So what's not to like?"
    return

label amy_talk_music_female:
    amy.say "Hey, [hero.name]...what the hell is that you're listening to?!?"
    bree.say "Oh...it's Sasha's band 'The Deathless Harpies'!"
    bree.say "Do you want me to turn it off, Amy?"
    bree.say "Is it too upbeat for you?"
    amy.say "No way, it sounds pretty good!"
    amy.say "That girl can really play!"

    return

label amy_talk_birthday_female:
    bree.say "Happy Birthday, Amy!"
    bree.say "Or Gloomy Birthday..."
    bree.say "I don't know how it is with you goths!"
    amy.say "Oh wow...thanks, [hero.name]!"
    amy.say "No, I'm not crying!"
    amy.say "I just have mascara in my eye, that's all!"

    return

init:
    define nickname_second_string = ["Second string", "second string"]

label command_nickname_amy:
    menu:

        "Call me Second string" if active_girl.flags.mikeNickname not in nickname_second_string and "band_harem_amy_event_11" in DONE:
            $ active_girl.flags.mikeNickname = "Second String"
        "Stop calling me Second string" if active_girl.flags.mikeNickname in nickname_second_string:
            $ active_girl.flags.mikeNickname = None
        "Cancel":


            jump command_girl
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
