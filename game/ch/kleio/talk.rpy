label kleio_talk_love_male:
    show kleio
    kleio.say "I mean, what is love, really?"
    mike.say "What do you mean?"
    "Kleio leans back, scoffing off the idea almost entirely."
    kleio.say "It just feels like—I dunno, a sham I guess?"
    kleio.say "Like, people put all this pressure on people and their relationship to be that perfect thing, the best one possible, their soulmate—blech—and it just feels so disingenuous, you know?"
    kleio.say "A product of, at best, a materialistic society, and, at worst, a way to make sure the spirits of the general public are always disappointed."
    menu:
        "Disagree":
            "I shuffle, feeling somewhat uncomfortable. I was raised on the idea that there's one person out there for you."
            "Although, I'm not one hundred percent sure I really believe in soulmates, I definitely think there's someone out there for me, designed to perfectly reflect me."
            "Hesitantly, I decide to explain this to her."
            mike.say "I dunno, Kleio. I can see where you're coming from, but honestly, I do think that someone is out there for me."
            mike.say "Like, someone who really cares about me, reflects me honestly—sort of like a soulmate, I guess?"
            "She snorts, clearly amused."
            kleio.say "So you're an idealist, huh? The world hasn't broken you yet?"
            "Her words sting, but I don't back down."
            mike.say "No. No, I guess not."
            "She sighs, staying silent for a moment. The pause is pregnant, uncomfortable."
            "Finally, she decides to break the silence, her voice much lower, and more far away than usual."
            show kleio annoyed
            kleio.say "I envy you, and your optimism. I used to be like you, [hero.name]."
            mike.say "And then what happened?"
            show kleio sad
            kleio.say "I learned the lesson that my parents always wanted to teach me: life isn't fair."
            kleio.say "You get your heart broken, you get your dreams stomped on and your aspirations shrivel into dust."
            show kleio annoyed
            kleio.say "In a perfect world, yeah, I think soulmates would exist."
            kleio.say "But, our world is far from perfect, and I've had my heart broken one too many times to keep my hopes up."
            kleio.say "Frankly, It's exhausting."
            mike.say "So, what, then? You just close yourself off, don't let yourself feel things for people?"
            show kleio normal
            kleio.say "No, I mean I do, I just—you're not gonna get it, [hero.name]. You'll know when you know."
            mike.say "So, now I just have to wait on getting my heart broken?"
            kleio.say "I hope it doesn't happen to you. But hope hasn't gotten me very far yet, so...I don't know."
            kleio.say "It's basically inevitable, I guess."
            mike.say "Yeah..."
        "Agree":
            "I find myself letting out a small sigh of relief. Honestly, I hate the idea of soulmates, and it's refreshing to hear that there isn't any pressure in—well, whatever it is going on between us."
            "It's just Kleio and I—no pressure."
            mike.say "It's refreshing to hear that, in a weird way."
            kleio.say "Really? Most people find it depressing."
            mike.say "I mean, I guess it totally can be that way, but, honestly, it's an insane amount of pressure to place on yourself and a relationship if you really believe in true love."
            mike.say "Plus, can you imagine how depressed you'd be all the time if you weren't in a relationship?"
            mike.say "It's much easier to just let things happen and the chips fall as they may."
            show kleio happy
            kleio.say "Thank god you agree."
            show kleio normal
            kleio.say "So many people have tried to change my mind on this, and, honestly, it just gets exhausting and weird."
            kleio.say "Relationships shouldn't be based on some spiritual feeling or direction from the cosmos or the Great Beyond or whatever—they should be built on compatibility and communication and, basically, doing the best you can with what you've got."
            "I stifle a laugh, and, on instinct reach over to grab her hand."
            mike.say "Guess the Beatles had it wrong, huh? All you need is not love."
            show kleio happy
            "She smiles, looking down on our hands, but, for a brief moment, an expression I can't read flashes across her face, before she returns to her familiar, smirking grin."
            show kleio normal
            kleio.say "Yeah. Exactly."
            $ kleio.love += 1
    hide kleio
    return

label kleio_talk_sex_male:
    show kleio
    mike.say "Hey Kleio? Can I ask you a question."
    kleio.say "Depends. What kind of question?"
    "I squirm. It's a question I've wanted to ask her for a while, but I've never been completely sure how she was going to take it."
    mike.say "It's kind of a personal question."
    kleio.say "Well, then let's just get it over with."
    mike.say "I'm sorry if this offends you, I just—I have to ask. How many people have you had sex with?"
    show kleio annoyed
    "Kleio lets out a loud, annoyed sigh, as though she had had this conversation a million times before, and was not in the mood for rehashing it."
    kleio.say "Look, [hero.name], I know some people take sex so damned seriously."
    kleio.say "I used to be one of them—I think every girl was one of them, at some point."
    "I raise an eyebrow, but stay silent, allowing her to go on."
    show kleio normal
    kleio.say "As I got older, though, I realized I was placing so much of my self-worth on how many people wanted to have sex with me, and my sex appeal, as though that was what determined and dictated my personality."
    kleio.say "On top of that, with me liking both men and women, the constant pressure on me to have these ultra-serious, very meaningful sexual encounters, lest I was looking for attention or not really bisexual, got too much for me."
    kleio.say "So, finally, I let all that bullshit go. Sex is sex, and I don't place this inherent weight or meaning on any of it."
    kleio.say "It's just a physical encounter between two people—any other weight I place on it is entirely at my discretion."
    menu:
        "Insist":
            mike.say "I appreciate that Kleio, but you didn't answer my question."
            show kleio angry
            "Kleio lets out an annoyed groan, rolling her eyes."
            kleio.say "Didn't I, though? The answer is I don't know."
            "I could not hide my shock. She had no idea?"
            kleio.say "I know that may be too hard for your sexless pea-brain to comprehend, but it's the truth. Take it as you will."
            "Uncomfortable and ashamed, I drop the topic, giving Kleio the space she needed, and mentally making a note to go get myself tested as soon as I can."
            $ kleio.love -= 1
        "Let go" if hero.charm >= 25:
            mike.say "You know, Kleio, that's a really powerful perspective. I'm sorry I asked, and thank you for sharing."
            "Kleio looks at me sideways."
            show kleio surprised
            kleio.say "So you don't mind?"
            mike.say "So long as you're being safe and you're happy, who am I to judge?"
            show kleio normal
            "Kleio lets out a breath, and I catch the hint of a smile growing across her face."
            kleio.say "Yeah. Exactly. That's how it should be, I think. Thank you for being understanding."
            mike.say "Anytime. And thank you for sharing."
            $ kleio.love += 1
    hide kleio
    return

label kleio_talk_politics_male:
    show kleio
    kleio.say "Do you seriously want to talk about this? Now?"
    kleio.say "Isn't there some sort of unspoken rule that people just don't talk about politics?"
    mike.say "I mean, I guess sometimes it's not a good idea. But it can also be beneficial to talk about them."
    mike.say "Healthy discussion is, well, healthy, and I think we're both mature enough to handle it."
    kleio.say "Whatever you say, Loverboy. Talk away."
    menu:
        "I am a conservative":
            mike.say "Well, I guess you could say I've been a conservative my whole life, so..."
            show kleio angry
            "Kleio doesn't even allow me to finish my sentence before she snorts and rolls her eyes."
            kleio.say "Oh, God, are you serious?"
            "I shuffle uncomfortably. I knew she would have a bad reaction, but it still made me feel gross."
            mike.say "Yes, Kleio, I'm 100%% serious. I know it's not the popular opinion, or the politically correct opinion, but it's my opinion."
            kleio.say "You realize I'm bisexual, right?"
            mike.say "Yes, I do?"
            kleio.say "And that I'm vegan, and have tattoos, and part Native American, right?"
            kleio.say "And that I literally go to protests, and talk about them often?"
            kleio.say "And that I say I'm feminist?"
            kleio.say "Jesus, [hero.name], why are you even fucking around me if everything you believe is the antithesis of who I am?"
            mike.say "I don't exclude people from myself just because I don't necessarily agree with everything they do. I think that's immature, and, besides, I don't think politics is that big of a deal."
            kleio.say "It's a big deal when your beliefs concern my existence."
            mike.say "Kleio, I don't want to argue with you."
            kleio.say "Whatever, [hero.name]. Forget I asked, and keep living in your damn bubble. Maybe I can pop it someday."
            $ kleio.love -= 1
        "I am a liberal":
            mike.say "What else do you expect from a 20-something living in an apartment in a big city, playing in a band where I have to crossdress? I'm a liberal."
            "Kleio sighs, a sigh suspiciously tinged with relief, and smirks."
            kleio.say "I'm glad to hear that. Not that I don't respect everyone, but, well, I don't think everyone respects me."
            mike.say "Well, I definitely do. In fact, I think you're the coolest goddamned person I've ever met."
            "Her smirk breaks into a full smile, surprised by my honesty."
            kleio.say "Thank you, [hero.name]. You aren't too shabby yourself."
            "Both of us smile now, relieved to exit this conversation as gracefully, and as quickly, as we can."
            $ kleio.love += 1
    hide kleio
    return

label kleio_talk_food_male:
    show kleio
    mike.say "What's your favorite food, Kleio?"
    "Kleio looks at me, bewildered, hiding a smile."
    kleio.say "My favorite food? What is this, an interview?"
    mike.say "I'm just curious! I'm not much of a cook, but maybe, if it's something simple, I can make it for you sometime."
    show kleio happy
    "She laughs, but I can tell that what I said had an impact on her. Hiding a blush, she begins to explain."
    show kleio normal
    kleio.say "Well, it sounds stupid, but when I was a kid, we grew up really poor."
    show kleio annoyed
    kleio.say "Like, really, really poor."
    kleio.say "Trailer park trash, I guess you could call us."
    kleio.say "So most of my childhood meals were just, like McDonald's, or whatever was fast and cheap and easy to get."
    show kleio normal
    kleio.say "But, sometimes, if there was a special occasion, my mom would make this amazing soup."
    kleio.say "It was called three sisters soup, which I thought was after my sisters and I, but it turns out it was a traditional native American dish my grandmother taught her."
    kleio.say "It was basically just corn, squash, and beans, but honestly, to me, it tasted like fine dining."
    show kleio happy
    kleio.say "I still think about that soup sometimes."
    show kleio normal
    kleio.say "A lot, actually."
    menu:
        "I can take you to fast food":
            mike.say "Well, I can't really make soup, but we can always go out to fast food whenever you want."
            "Kleio laughs, but flinches, her eyes looking sort of far away. I realize that my joke hit her a little too close to home."
            kleio.say "Yeah, of course, [hero.name]. I love fast food—reminds me of my childhood."
            "Her voice is light, but the hurt within it is unmistakable. Feeling ashamed, I turn my head, waiting for the conversation to drop."
        "I can cook for you." if hero.has_skill("cooking"):
            mike.say "I'll see what I can do. It probably won't be as good as home's, but I want to try—for you."
            show kleio happy
            "For a moment, Kleio's face lights up with pure, child-like delight, before I see the cynical, adult her return, clouding her excitement."
            kleio.say "Well, I hope you'll try—my mom is a pretty damn good cook, and it'd be hard to beat her."
            mike.say "I'll do my best for you, one day—you'll see. I promise."
            show kleio normal blush
            "Slyly, she looks up at me."
            kleio.say "Pinkie promise?"
            "I sigh, sticking out my pinkie to meet hers."
            mike.say "I pinkie promise, from the very bottom of my heart, that I will try to make three sisters soup as well as your mom did for you one day."
            kleio.say "Good. I'm holding you to that, you know?"
            mike.say "I know. I'd hoped you would."
            "Smiling to herself, Kleio turns away, not allowing me to see the child-like delight forming unabashed on her grinning face."
            $ kleio.love += 1
    hide kleio
    return

label kleio_talk_travels_male:
    show kleio happy
    kleio.say "I want to go volunteer in africa."
    $ kleio.love += 1
    hide kleio
    return

label kleio_talk_tv_male:
    show kleio angry
    kleio.say "TV is a drug used to keep the people under control."
    $ kleio.love -= 1
    hide kleio
    return

label kleio_talk_sports_male:
    show kleio annoyed
    kleio.say "I don't see why we should glorify stupid people that just know how to throw a ball."
    hide kleio
    return

label kleio_talk_fashion_male:
    show kleio
    "I look over at Kleio, her clothes so different and eye-catching, tears in strange places and colors so muddled, skin showing in every place you'd expect it to show and more..."
    "Before I even realize it, I have my mouth open, asking a question I didn't even realize I had."
    mike.say "Kleio, why do you dress the way that you do?"
    "Kleio turns to face me, an eyebrow arched in suspicion."
    kleio.say "What do you mean?"
    "I stumble, desperate to not offend her, but also desperate to know, to really get inside her head."
    mike.say "I mean, you always wear these really grungy clothes, and they're always, like, black or grey with these really bright pops of colors, and they always have tears in them, and, I mean, I get fashion, I do, but like...why?"
    "Kleio hides a smile, looking slightly irritated but also strangely amused."
    kleio.say "It's just how I've always been, I guess."
    kleio.say "I've never been the type of girl to wear dresses or baby pink or whatever else girls are wearing these days."
    kleio.say "I like my hair short and I like my tattoos and skin showing, and I like that, when people look at me, they know, one hundred percent, that I couldn't give less of a fuck about what they think."
    menu:
        "What's wrong with girls in pink dresses?":
            "Her words shock me. In my panic to relate, the only words that come to mind are, probably, the worst words I could have possibly said."
            mike.say "What's wrong with girls in pink dresses?"
            show kleio angry
            "Kleio scowls, realizing that, in my panic, I missed her point entirely."
            kleio.say "Nothing, dumbass. That's just not who I am, and it never will be."
            kleio.say "And, if you're looking for that kind of girl, you had better start looking elsewhere, because you aren't going to find her here."
            show kleio annoyed
            "I panic even more, struggling to back peddle."
            mike.say "No, no, Kleio, that's not what I meant—"
            "She turns and looks back at me, her eyes empty and void of any emotion."
            kleio.say "It's whatever, [hero.name]. I know what you meant."
            $ kleio.love -= 1
        "You look badass":
            "Her words almost seem to empower me, and, almost unconsciously, I find my hand pulling at a small hole in my jeans, wishing it was bigger, wishing I had more to show and as powerful of a reason to show it."
            "Quietly, I look at Kleio, her confidence rushing out of her pores, infecting me, as she waited for a reaction."
            mike.say "Kleio, that's the most badass thing I've ever heard."
            show kleio happy
            "Kleio grins wildly, even doing a small spin to show off her outfit for that day, allowing my eyes to rake over her body, unabashed."
            show kleio normal
            kleio.say "Good. That's the goal, isn't it? Come on, Loverboy, I can see it in your eyes—you want some cool clothes, too, don't you?"
            "Gulping, I nod, and Kleio grins even wider, allowing the emotion to nearly take over her face as she reaches out to take my hand."
            kleio.say "Well, then we have no time to waste. Come on, then—let's go get you some kickass fucking ripped jeans."
            $ kleio.love += 1
    hide kleio
    return

label kleio_talk_books_male:
    show kleio
    "Kleio looks me dead in the eye, her face unreadable."
    kleio.say "You think I'm stupid, don't you? Or, at least, that I think education is like, pointless, or whatever, don't you?"
    menu:
        "Disagree" if hero.charm >= 25:
            mike.say "No! Of course not! I just wanted to read, Kleio. I'm sure you love to read—what's you favorite book?"
            "Kleio rolls her eyes, but her unreadable anger seems to have subsided somewhat."
            show kleio angry
            kleio.say "You're not going to believe me."
            mike.say "Of course I will. Who lies about their favorite book?"
            kleio.say "People always think that I'm lying about mine."
            mike.say "Well, I won't. Pinkie swear. What is it?"
            show kleio annoyed
            "Kleio sighs, looking away from me before she's able to answer."
            kleio.say "East of Eden."
            "My confusion is evident on my face. From her reaction, I was expecting something a little more juvenile. But East of Eden?"
            mike.say "The Steinbeck novel?"
            show kleio angry
            kleio.say "See! You don't believe me."
            mike.say "No! No, I do—I promise. I was just a little surprised is all—the way you were talking, I thought you were about to say, like, a comic book or something like that."
            show kleio normal blush
            "She smiles shyly, clearly embarrassed."
            kleio.say "No, although I like those too. I guess people just seem to think that having tattoos takes away your ability to read, or something. I don't know—people just never believe me."
            mike.say "Well, I do, and, for the record, East of Eden is a beautiful book. It's easy to see why it's your favorite."
            show kleio happy
            "Kleio smiles, nodding along, before gesturing back to my book, allowing me to finish up my novel."
            $ kleio.love += 1
        "Say nothing":
            "I hesitate, not quite knowing how to react. Before I can come up with an excuse, Kleio's eyes rage as she cuts me off."
            show kleio angry
            kleio.say "So I'm right! You think I'm stupid!"
            mike.say "I just—Kleio, you have to understand—every interaction I've had with people who look like you dropped out of high school."
            mike.say "They hate school—it's nothing against you, I just figured you were the same."
            show kleio annoyed
            "Kleio rolls her eyes, refusing to look at me."
            kleio.say "Didn't they teach you in school not to judge a book by its cover? For the record, I have a degree in English, and my favorite novel is East of Eden."
            kleio.say "I probably know more about books and academia than you do... Does that satisfy you a little bit?"
            "Ashamed, I duck my head."
            mike.say "I'm sorry, Kleio. I shouldn't have stereotyped you like that."
            show kleio angry
            kleio.say "Damn right you shouldn't have. Go back to your damn book—sorry I bothered you."
            "I return to my book, but I find myself unable to focus, the white-hot shame flaring deep in my chest at my hurtful words."
            $ kleio.love -= 1
    hide kleio
    return

label kleio_talk_people_male:
    show kleio annoyed
    kleio.say "People are plain stupid."
    hide kleio
    return

label kleio_talk_computers_male:
    show kleio angry
    kleio.say "A tool to keep us under surveillance."
    $ kleio.love -= 1
    hide kleio
    return

label kleio_talk_music_male:
    show kleio
    mike.say "Kleio, why do you like the music that you like?"
    show kleio surprised
    "Kleio turns to face me, looking almost puzzled as to why I would ask such a question to her."
    kleio.say "Uh, isn't it obvious?"
    show kleio normal
    "She gestures her hands out to her clothes, as though that will better explain the situation. I see what she's getting at—her short hair, her studded clothes, her tattoos—it's obvious that her music taste matches the aesthetic she's going for."
    "But that misses the point of my question entirely—it points to how she shows she enjoys it, but doesn't actually answer why. Tentatively, I swallow, readying myself to attempt explaining this to her."
    mike.say "I get that you're into punk and alternative stuff and whatever—it's obvious. But Kleio, that just indicates to everyone else that you enjoy it. But it doesn't actually tell me why."
    kleio.say "Can't the answer be that I just like the look of it?"
    mike.say "It can be, but I don't want to believe that you're that shallow. You care about your music too much just to listen to it for your fashion sense."
    "Kleio rolls her eyes, but I can see my words get to her. Sighing, she slowly begins to explain."
    kleio.say "I don't know. When I was a kid, I was ridiculed for any number of things—my heritage, my fashion choices, my sexuality—anything those kids could latch onto to tease me for, they would."
    kleio.say "My music became my armor, shielding me from the world in a way I couldn't have done for myself. In a way, although it physically made me a loner, it emotionally made me realize I wasn't alone."
    kleio.say "I feel like I owe my life to punk, hardcore rock music, in a way. Without it, I wouldn't be the kickass person I am today. Does that make any sense?"
    $ kleio.love += 1
    menu:
        "Yes":
            mike.say "I think that's awesome Kleio. Much better reason than mine for liking any kind of rock music—I just like guitars"
            show kleio happy
            "Kleio smiles, allowing me, for a brief moment, inside her walls."
            kleio.say "Yeah, well, it's kinda silly crediting your life to a musical genre, but, what can I say. Plus, I'd have to agree with you—the guitars are pretty sick."
            "I smile back at her, leaning into her vulnerability and embracing it, hoping that she knows that, no matter how bad things get, she can always be her pop-punk self with me."
        "No":
            mike.say "I get why you did it then, but don't you think you'd outgrow that tendency eventually?"
            show kleio annoyed
            "Kleio rolls her eyes, turning away from me, grumbling."
            kleio.say "I didn't expect you to understand."
            mike.say "That wasn't a slight against you, Kleio. I just figured that everyone outgrew their childhood armor, that's all."
            show kleio angry
            "Spinning to face me, eyes flaring, I realize too late that my words have hit closer to home than I intended."
            kleio.say "Is it too much for your tiny dick brain to imagine that I'd want to dedicate some part of my life to the music that made me feel like it was okay to be me?"
            kleio.say "Yes? Alright, great, good thing that's established."
            mike.say "Kleio, I—"
            kleio.say "Just shut up, [hero.name]."
            $ kleio.love -= 1
    hide kleio
    return

label kleio_talk_birthday_male:
    show kleio happy
    kleio.say "Thank you for remembering."
    $ kleio.love += 3
    hide kleio
    return

init python:
    SpecificTalkSubject(**{
    "name": "kleio_talk_anna",
    "display_name": "About Anna",
    "label": "kleio_talk_anna_male",
    "duration": 0,
    "icon": "button_anna",
    "conditions": [
        IsDone("anna_event_06"),
        HeroTarget(
            IsGender("male"),
            ),
        PersonTarget(kleio,
            IsActive(),
            ),
        ],
    "do_once": True,
    })

label kleio_talk_anna_male:
    show kleio
    "Part of me thinks that getting myself involved in the argument between Anna and Kleio is just asking for trouble."
    "And in an ideal world, I'd be happy to leave well enough alone, to let them sort it out like a couple of adults."
    "But past experience tells me Kleio is far too pig-headed to even think of admitting that she might be in the wrong."
    "So if I want her to get her head out of her ass and settle this thing, I'm going to need to make it happen myself."
    "With all of that in mind, I gather my courage and walk towards Kleio."
    mike.say "Hey, Kleio - we need to talk."
    show kleio angry
    kleio.say "Urgh..."
    kleio.say "I should have known Anna would go running to you!"
    show kleio annoyed
    mike.say "Yeah, well, I'm not Anna."
    mike.say "So you won't get rid of me that easily."
    show kleio angry
    kleio.say "Okay, okay..."
    show kleio annoyed
    kleio.say "Just name the time and the place."
    kleio.say "And then you can say your piece."
    "It's not long after the conversation wraps up that I find myself face-to-face with Kleio."
    "She crosses her arms over her chest at the sight of me, looking as defensive as I'd expected."
    "But I know her better than she thinks I do."
    "And I know that sometimes she puts on her meanest face when she feels the most insecure."
    kleio.say "So, [hero.name], is this where I get the lecture, huh?"
    kleio.say "Where you tell me not to be mean to poor, little Anna?"
    "I'm not in the mood to trade insults with Kleio, be they aimed at me or Anna."
    "So with a rueful shake of the head, I get ready to jump into what I expect to be yet another argument."
    if Harem.together(anna, kleio):
        $ kleio.love += 5
        mike.say "Does what we have together mean that little to you, Kleio?"
        mike.say "That you'd throw it all away over some dumb argument?"
        "Kleio bristles instantly, clearly resenting my throwing the threesome in her face."
        show kleio angry
        kleio.say "Hey, don't you act like that's what this is about!"
        kleio.say "I didn't sign away my right to an opinion when we got into this thing."
        kleio.say "And I won't bite my tongue for the sake of getting laid, either!"
        show kleio annoyed
        mike.say "With an attitude like that, Kleio, I'm amazed you ever got laid."
        mike.say "Keep on this way, and maybe you won't have to worry about that or having to play nice."
        show kleio angry
        "Kleio's eyes go wide as the meaning of my words sinks in."
        kleio.say "What...what are you saying, [hero.name]?"
        mike.say "What does it sound like to you, Kleio?"
        mike.say "If being right is more important to you than treating Anna and me right..."
        mike.say "Well, maybe you're better off out of this relationship."
        show kleio annoyed
        "Kleio shakes her head, as if giving me the chance to take back what I just said."
        kleio.say "You don't mean that, [hero.name]."
        kleio.say "No guy would ever end something like what we have."
        mike.say "Jesus Christ, Kleio - is that all you think we are?"
        mike.say "I'm just a cock and Anna's just a second pussy to you - is that it?!?"
        "Kleio pushes her hands out in front of her, waving them as if to push my words away."
        show kleio normal
        kleio.say "No, no..."
        kleio.say "That's not what I meant, [hero.name]."
        show kleio sad
        kleio.say "You have to believe me!"
        mike.say "Oh, do I?"
        mike.say "And what'd make me do that?"
        "For a moment, Kleio looks almost desperate, as though she's at a loss for an answer."
        "But then a thought seems to occur to her, and she looks down at the ground by her feet."
        kleio.say "Maybe if I said that I was sorry?"
        kleio.say "If I said sorry and I meant it?"
        "Fuck sake - is this what it takes to get through to her every time?"
        mike.say "That'd be a start, for sure."
        mike.say "But maybe you should be saying that to Anna?"
        show kleio normal blush
        "Kleio lets out a weary sigh, finally admitting defeat."
        kleio.say "Okay, you win - I'll make the call!"
    else:
        mike.say "Cut the crap, Kleio."
        mike.say "We both know that Anna's capable of being an air-head sometimes."
        mike.say "But since when has the way to deal with it been to put her down like that?"
        show kleio angry
        "Kleio starts to say something, a retort of some kind."
        show kleio surprised
        "But I can instantly tell from the curl of her lip that it's not going to be helpful in the slightest."
        "And so I cut her off before she can get as much as a word of it out."
        mike.say "And don't tell me that she deserved it, Kleio."
        mike.say "Don't tell me that she should grow a pair."
        mike.say "For such a radical feminist, you sure seem to hate women!"
        "I hadn't meant for this to turn into me blistering Kleio."
        "The idea was for me to play the peacemaker and be all understanding."
        "But I guess that I just have too much suppressed anger towards her for that to work."
        show kleio annoyed blush
        kleio.say "Ah..."
        kleio.say "Alright, alright..."
        kleio.say "I admit that I was too hard on her."
        "Kleio plants her hands on her hips, rolling her eyes in frustration."
        kleio.say "I was already having a bad day."
        kleio.say "She just pushed my buttons at the wrong moment."
        mike.say "And how's that worth losing a friend over?"
        show kleio normal
        "Kleio looks at me in silence for a while, her mouth a thin, bloodless line."
        "It's like there's a battle going on inside of her."
        "And either she'll make me vanish by sheer force of will, or else she'll crack."
        kleio.say "Argh..."
        kleio.say "It's not...of course it's not!"
        kleio.say "There you go, you made me say it."
        mike.say "Was that really so hard to admit, Kleio?"
        "Who am I trying to kid?"
        "That was like trying to get blood out of a stone!"
        mike.say "So you'll speak to her?"
        mike.say "You'll try to work this thing out?"
        "Kleio nods grudgingly, as though she can't bear to say another word on the subject."
        "Well, it might not be a written guarantee."
        "But it's certainly better than nothing."
    hide kleio
    return

init:
    define nickname_boy = ["Boy", "boy"]

    define nickname_twink = ["Twink", "twink"]
    define nickname_playboy = ["Playboy", "playboy"]
    define nickname_boytoy = ["Boytoy", "boytoy"]
    define nickname_love = ["Love", "love"]

label command_nickname_kleio:
    menu:

        "Call me Boy" if active_girl.flags.mikeNickname not in nickname_boy and active_girl.love > 30:
            $ active_girl.flags.mikeNickname = "Boy"
        "Stop calling me Boy" if active_girl.flags.mikeNickname in nickname_boy:
            $ active_girl.flags.mikeNickname = None


        "Call me Dumbass" if active_girl.flags.mikeNickname not in nickname_dumbass and active_girl.sub < 80:
            $ active_girl.flags.mikeNickname = "Dumbass"
        "Stop calling me Dumbass" if active_girl.flags.mikeNickname in nickname_dumbass:
            $ active_girl.flags.mikeNickname = None


        "Call me Twink" if active_girl.flags.mikeNickname not in nickname_twink and game.flags.bandcrossdress == True:
            $ active_girl.flags.mikeNickname = "Twink"
        "Stop calling me Twink" if active_girl.flags.mikeNickname in nickname_twink:
            $ active_girl.flags.mikeNickname = None


        "Call me Playboy" if active_girl.flags.mikeNickname not in nickname_playboy and Harem.find(active_girl):
            $ active_girl.flags.mikeNickname = "Playboy"
        "Stop calling me Playboy" if active_girl.flags.mikeNickname in nickname_playboy:
            $ active_girl.flags.mikeNickname = None


        "Call me Boytoy" if active_girl.flags.mikeNickname not in nickname_boytoy and not Harem.find(active_girl):
            $ active_girl.flags.mikeNickname = "Boytoy"
        "Stop calling me Boytoy" if active_girl.flags.mikeNickname in nickname_boytoy:
            $ active_girl.flags.mikeNickname = None


        "Call me Love" if active_girl.flags.mikeNickname not in nickname_love and active_girl.love > 100:
            $ active_girl.flags.mikeNickname = "Love"
        "Stop calling me Love" if active_girl.flags.mikeNickname in nickname_love:
            $ active_girl.flags.mikeNickname = None
        "Cancel":


            jump command_girl

label submissive_interact_kleio_male:
    mike.say "Ah, Kleio..."
    mike.say "I got a pretty crazy idea."
    mike.say "So just hear me out, okay?"
    show kleio talkative
    kleio.say "I'm all ears, Loverboy!"
    show kleio normal
    mike.say "How about you spice things up when you say hi to me?"
    mike.say "Maybe even mention how much you want me inside of you?"
    if kleio.sub >= 70 or kleio.is_sex_slave:
        show kleio annoyed
        kleio.say "Urgh..."
        show kleio talkative
        kleio.say "I can't believe you've reduced me to this."
        show kleio seductive
        kleio.say "But you're right - I do want you that badly!"
        $ kleio.flags.submissive_interact = True
    else:
        show kleio surprised
        kleio.say "Whoa, whoa, whoa..."
        show kleio angry
        kleio.say "Are we even living on the same planet right now?"
        show kleio annoyed
        mike.say "Ah, my mistake, Kleio."
        mike.say "Let's just put that idea on ice..."
        $ kleio.love -= 4
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
