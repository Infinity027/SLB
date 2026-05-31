

init python:
    Event(**{
    "name": "morgan_give_phone_number",
    "label": "give_phone_number",
    "girl": "morgan",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(morgan,
            IsPresent(),
            Not(IsHidden()),
            Not(ContactKnown()),
            Not(IsActivity("sleep")),
            MinStat("love", 40),
            ),
        ],
    "chances": 25,
    "do_once": True,
    "once_day": True,
    "music": "music/roa_music/underwater.ogg",
    "quit": False,
    })

    Event(**{
    "name": "morgan_send_text",
    "label": "send_text",
    "priority": 100,
    "conditions": [
        IsHour(15, 16),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        GameTarget(IsFlag("noTexting", False)),
        PersonTarget(morgan,
            Not(IsPresent()),
            Not(IsHidden()),
            ContactKnown(),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "fun": 1,
    "girl": "morgan",
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "morgan_auto_greet",
    "label": "auto_greet",
    "girl": "morgan",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("None")),
        PersonTarget(morgan,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            IsFlag("greeted", False),
            MinStat("love", 50),
            ),
        ],
    "chances": 50,
    "music": "music/roa_music/underwater.ogg",
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "morgan_auto_chat",
    "label": "auto_chat",
    "girl": "morgan",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(morgan,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "chances": 10,
    "music": "music/roa_music/underwater.ogg",
    "do_once": False,
    "once_day": True,
    })

    Event(**{
    "name": "morgan_are_you_sick",
    "label": "are_you_sick",
    "girl": "morgan",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(morgan,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (morgan, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "morgan_ask_out",
    "label": "ask_out",
    "girl": "morgan",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("ask_date"))),
        PersonTarget(morgan,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            Not(IsDatePlanned()),
            IsFlag("nodate", False),
            IsFlag("noaskout", False),
            MinStat("love", 100),
            ),
        ],
    "chances": 5,
    "do_once": False,
    "once_day": True,
    })

    Event(**{
    "name": "morgan_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "morgan",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(morgan,
            IsPresent(),
            Not(IsHidden()),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

label morgan_bye(bye_outfit=None):
    call npc_bye_outfit (npc=morgan, bye_outfit=bye_outfit) from _call_npc_bye_outfit_16
    $ (day, h, activity, bye_outfit) = _return
    if not activity == morgan.activity:
        if day != game.week_day:
            $ morgan.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ morgan.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"morgan {bye_outfit}")
        if activity["activity"] == "sleep":
            morgan.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            morgan.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            morgan.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            morgan.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            morgan.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            morgan.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            morgan.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            morgan.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            morgan.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            morgan.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            morgan.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            morgan.say "I'll go get dressed."
        hide morgan
    return

label morgan_cheated(action, cheat_npc=None):
    show morgan
    if cheat_npc and cheat_npc.id == "kleio" and Harem.together(morgan, cheat_npc):
        show morgan blush
        show fx heart
        $ morgan.sub += 1
        "I see Morgan looking at me [action] someone else with envy and lust in her eyes."
    elif cheat_npc and Harem.together(morgan, cheat_npc):
        show morgan blush
        show fx heart
        $ morgan.love += 1
        "I see Morgan looking at me [action] someone else with envy and lust in her eyes."
    else:
        show morgan angry
        show fx anger
        $ loss = 5
        if morgan.flags.girlfriend or morgan.flags.fiance:
            $ loss += 5
        $ morgan.love -= loss
        "I see Morgan looking at me [action] someone else with an angry look on her face..."
    hide morgan
    return

label morgan_greet:
    if renpy.has_label(f"morgan_greet_dialogues_{hero.gender}") and not morgan.flags.greeted:
        scene expression f"bg {game.room}"
        $ morgan.flags.greeted = TemporaryFlag(True, 1)
        show morgan
        $ result = randint(1, 3)
        if result == 1:
            morgan.say "Hello, [hero.name]."
        elif result == 2:
            morgan.say "Hi, [hero.name]."
        elif result == 3:
            morgan.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                morgan.say "Good morning [hero.name]."
            elif game.hour < 19:
                morgan.say "Good afternoon [hero.name]."
            else:
                morgan.say "Good evening [hero.name]."
        call expression f"morgan_greet_dialogues_{hero.gender}" from _call_expression_255
        if morgan.flags.submissive_interact:
            if randint(0, 1) == 0:
                morgan.say "[hero.name], let me prove that I'm all woman one more time!"
            else:
                morgan.say "🎵I'm just a woman.🎵"
                morgan.say "Do you want a proof [hero.name]?"
        hide morgan
    return

label morgan_greet_dialogues_male:
    $ result = randint(1, 3)
    if result == 1:
        mike.say "Hello, Morgan."
    elif result == 2:
        mike.say "Hi."
    else:
        if game.hour < 6:
            mike.say "Hello Morgan."
        elif game.hour < 12:
            mike.say "Good morning Morgan."
        elif game.hour < 19:
            mike.say "Good afternoon Morgan."
        else:
            mike.say "Good evening Morgan."
    return

label morgan_kiss:
    scene expression f"bg {game.room}"
    if morgan.love + hero.charm < 80 and not morgan.is_girlfriend and not game.active_date.score >= 75:
        show morgan
        "The timing feels right to me, the moment perfect for things to escalate naturally and flow into something more."
        "I have to lean in close, bending more than just my neck in order to be able to account for Morgan's petite size."
        "At first, she doesn't seem to realise what I'm doing, smoothing her electric blue hair out of her eyes as she smiles up at me."
        "My lips must be nothing more than mere inches from her own before she guesses what my intentions are."
        "She's so close to me by now that I can feel the warmth of her breath on my face."
        "But then I see her impish features contort a little, and I feel her arms pushing me backwards, pushing me away from her."
        "The briefest of expressions flashes across Morgan's face in that moment."
        "I can see no hint of disgust or annoyance that would suggest she's outraged by the idea of me kissing her."
        "But there's clearly genuine surprise as she pulls away from my clumsy attempt to kiss her."
        "From there, her features become more open, and she looks at me with wide eyes."
        "The only explanation for this new expression is that she's now feeling concern over something."
        "And then I realise that it's concern for me."
        "Even though she just instinctively refused to be kissed, Morgan's already worried that she's hurt me in the same act."
        "I never knew a girl could push me away and yet make me love her all the more by doing so."
        hide morgan
    elif not morgan.flags.kiss:
        hide morgan
        if morgan.lesbian > MAX_LES_GUY_SEX:
            $ morgan.lesbian -= 1
        $ morgan.love += 6
        show morgan kiss
        "When it happens, it's almost like there's no preamble or build up that I can recall."
        "We go from laughing like a couple of drunk idiots, to twining our hands together."
        "And the next thing I know, we just seem to pull ourselves together and that's it."
        "I'm bending down to put my lips to Morgan's."
        "And she's standing up on the tips of her toes, doing the opposite to achieve the same effect."
        "The kiss is pretty soft and chaste to begin with."
        "Not really much more than us pressing our lips together and enjoying the sensation of the same."
        "It's only when I open my mouth a little and feel Morgan copy the move that things become somewhat more intense."
        "I feel the very tip of her tongue brush against mine."
        "But then it retreats, as though taunting me into following it back to its lair."
        "As I take the bait, I can feel Morgan beginning to melt from the kiss."
        "She wraps her arms around my neck, and I grab her backside with mine."
        "I don't so much pick her up, as I do support her while she tries to climb up me at the same time."
        "I'm not put off or discouraged by Morgan's petite body, quite the opposite."
        "The fact that I can almost enfold her in my embrace and feel the hot tenacity of her desire is a massive turn on."
        "Likewise, I can feel her pointed tongue as it pushes past my teeth."
        "Morgan kisses like she's possessed by a hunger, and she inspires a similar feeling in my desires for her as well."
        hide morgan kiss
        $ morgan.flags.kiss += 1
    else:
        if morgan.lesbian > MAX_LES_GUY_SEX:
            $ morgan.lesbian -= 1
        $ morgan.love += 2
        hide morgan
        show morgan kiss
        "Whenever someone feels the need to comment on the height difference between Morgan and myself, I can't help but crack a smile."
        "They genuinely seem to think that it should be some kind of physical barrier that makes us unsuitable for one another."
        "In fact, it's the very thing that makes the art of kissing her that much more enjoyable."
        "For example, I can't just lean over and peck her on the cheek."
        "I can't even get a good look at her face without inclining my head."
        "Either I have to bend over a little, or she has to stand on her tiptoes - preferably a bit of both for the best possible results."
        "But the real problem for me is trying to resist actually scooping her up and kissing her as I hold her in my arms."
        "It helps to ask, of course, rather than just taking liberties."
        "Though if you've never lifted a petite woman and placed her onto a convenient table or wall so that she was easier to kiss, you've missed out one of life's great pleasures."
        "All of this means that kissing Morgan is an event, and not just a matter of a moment that's forgotten as quickly."
        "And when you have to make an effort to do something, it means so much more that you couldn't believe it."
        "It becomes something to look forward to, something to savour, and a memory that's going to stay with you for a long time after it's done too."
        hide morgan kiss
        $ morgan.flags.kiss += 1
        hide morgan
    return

label morgan_sleep_date_fuck(location="hero"):
    if game.hour > 19 or game.hour < 6:
        scene bg bedroom1
        show cuddle morgan
        "No one speaks as we lie together on my bed, panting for breath is all that we seem to be able to manage."
        "All I can think is how ludicrous this situation would have seemed to be back in the day - or even a couple of weeks ago."
        "I'm sure Morgan is feeling something similar right now."
        "But I also hope that she's thinking that it's something that could become the new normal."
        $ morgan.love += 1
        call sleep ("morgan") from _call_sleep_61
    $ game.room = "bedroom1"
    return

label morgan_propose_male:

    if morgan.male > 66:
        if morgan.love >= 195:
            show morgan blush
            "Normally it's pretty hard for me to tell when a girl is hiding something from me."
            "Usually they're just so much better than guys when it comes to keeping it under wraps."
            "But that would be in the case of an average girl and an equally average guy."
            "And Morgan's certainly never been anything like an average girl!"
            "In some ways, she's actually easier to read than most guys I know too."
            "Which is why I can sense that there's something off with her the moment we meet up."
            "Normally she wouldn't be afraid to speak up and say what she's thinking."
            "But today she seems to pause before she opens her mouth and utters a single word."
            "It's almost as if she wants to say something, but she's actually afraid of the consequences."
            "And it takes me a little while to wrap my head around this and figure out what to do."
            "Also, give me a break for not sitting straight down and offering to be an amateur shrink."
            "I'm a guy, remember?"
            "I'm supposed to be slow on the uptake when it comes to this kind of thing."
            "You know - an emotional cripple?"
            "So, I take a deep breath and get ready to jump in feet first..."
            "I literally have my mouth open and I'm in the process of forming the words."
            show fx exclamation
            "And that's when Morgan takes me completely by surprise, stopping me dead in my tracks."
            "At first I think she must have tripped over something unseen on the ground."
            "But then I realise that she's actually lowering herself down of her own accord."
            "I watch as Morgan settles uncomfortably onto one knee and looks up at me."
            "Still I don't say a word, as the look in her eyes and on her face is so strange."
            "Normally she's a picture of forthright confidence, knowing exactly what she wants."
            "And now Morgan looks unsure of herself, even a little scared."
            morgan.say "[hero.name]..."
            "Even her voice is smaller than usual, quivering as she speaks."
            morgan.say "[hero.name]..."
            mike.say "What's the matter, Morgan?"
            mike.say "Are you feeling okay?"
            "Rather than answering my question, I see her fumble in her pockets."
            "She seems to be looking for something, afraid that she might not find it."
            "But then relief fills her eyes and she tugs whatever she was looking for out."
            morgan.say "I...I wanted to ask you something."
            morgan.say "Would...would you..."
            morgan.say "[hero.name], will you marry me?"
            "For a moment I can't actually make sense of what Morgan just said to me."
            "I mean, I understand the words that she used, but they seem to have no actual meaning."
            "Then there's the sound of hinges, snapping open."
            "And I look down to see what she's holding in her hands."
            "Jesus Christ - it's a ring!"
            show morgan sad
            morgan.say "You...you're not saying anything."
            morgan.say "Oh fuck...fuck, fuck, fuck!"
            morgan.say "It's a no, isn't it?"
            show morgan annoyed
            morgan.say "Argh...I knew this was a mistake!"
            "All of a sudden the reality of the situation hits me, and I shake off my momentary confusion."
            "And maybe more so, I see the pain and embarrassment in Morgan's eyes as she berates herself."
            "This is going to sound pathetic, I know."
            "But in that moment, I swear I can actually feel my heart breaking for her sake."
            mike.say "Yes!"
            show morgan surprised
            "At the sound of my voice, Morgan looks up at me in genuine surprise."
            "I had expected my answer to change her mood almost instantly."
            "But instead she still looks as confused and self-loathing as ever."
            "It's then that it hits me - she has no idea what I'm actually saying yes to."
            "Is it the proposal itself, or the notion that she just fucked up in public!"
            mike.say "I mean, yes, Morgan - I will marry you!"
            "I instinctively reach down and take a gentle hold of her wrists, pulling Morgan to her feet."
            "She offers no resistance, still looking me straight in the eye as if stunned."
            mike.say "Hey, Morgan?"
            mike.say "Earth calling Morgan!"
            show morgan blush
            "Finally Morgan seems to be shaking off her funk and coming back to her senses."
            "Another guy might actually have been offended by what she just did."
            "They might have seen it as a challenge to their fragile masculinity."
            "But I doubt a guy like that would have been able to handle being with Morgan!"
            "She's neither shy nor retiring like some people still expect girls to be."
            "But that's one of the things that makes her so special."
            "And it's one of the things that makes me love her too."
            "She just did something incredibly brave in proposing to me like that."
            "Showing me that she feels just the same way in return."
            mike.say "Morgan, do I have to put that ring on my OWN finger or what?!?"
            show morgan normal
            "Morgan shakes her head, clearing the last of the mental cobwebs."
            "And as she does so, I see a familiar smile begin to creep back onto her face."
            morgan.say "So you want to?"
            morgan.say "Marry me, that is?"
            "I feel her slip the ring onto my finger."
            "And I'm not afraid to admit that I feel a flutter in my chest as she does so."
            mike.say "Of course I do, Morgan."
            mike.say "I can't imagine you ever being out of my life again."
            mike.say "And I swear that I'd have gotten round to asking you myself."
            mike.say "Sooner or later..."
            morgan.say "So you don't mind that I..."
            "I shake my head as I return her smile."
            mike.say "Nah, not really."
            mike.say "I'm a pretty modern guy, you know?"
            mike.say "I even date girls that I used to think were guys!"
            show morgan angry
            "Morgan's eyes go wide at this, and she gives me a playful punch on the shoulder."
            show morgan happy
            "But in the very next moment, she wraps her arms around me and pulls me into a tight embrace."
            "I feel her lay her head upon my shoulder and let out a weary, but satisfied sigh."
            "Returning the embrace, I lay my head atop hers."
            mike.say "Actually, it's pretty special, getting to know how a girl feels in that position."
            show morgan normal
            morgan.say "You really mean that?"
            mike.say "Yeah, Morgan, I do."
            mike.say "I don't think I've ever felt as wanted...no, needed as I do right now."
            morgan.say "I love you, [hero.name]."
            mike.say "Yeah, Morgan, I know."
            mike.say "I love you too."
            $ morgan.set_fiance()
        else:
            show morgan
            "I really thought that I'd come a long way with Morgan recently, that I'd gotten over my previous issues."
            "Since we started dating, things have gone from casual to pretty serious in what feels like no time at all."
            "And all of the awkwardness that I used to feel around her almost a fading memory, a thing of the past."
            "That was why I got it into my head that it was high time I did something to capitalise on all of this progress."
            "But what was that going to be?"
            "I wanted to make a statement to Morgan, let her know just how much I felt for her."
            "And I was also pretty keen to ensure that things kept going the way they had been too."
            "So what better thing to do than buy a ring and propose to her?"
            "Yeah, I know - that makes it sound so simple, when it's anything but."
            "The thing is, I wasn't thinking straight at the time, or I'd have come to the same conclusion."
            "I guess I was just carried along on a wave of affection for Morgan."
            "And so it was only when I found myself getting down on one knee that this finally occurred to me!"
            "So, I'm down here, with the ring in my hand."
            show morgan surprised
            "Morgan's just spotted what I'm doing."
            "But from the look on her face, I can tell that she's not fully grasped the meaning of my actions."
            "Oh God - why is it only now that I realise the gravity of what I'm doing?"
            "I'm putting myself right in the firing line here."
            "What if she says no?"
            "What if she laughs in my face or runs away at the sight of the ring?"
            "What if she actually says yes?!?"
            "I can feel all of the former issues and hang-ups that I had around Morgan begin to return."
            "And suddenly it's like none of the dates that we've been on exist anymore."
            "All of the times that we've talked, been honest with each other and seemed to bond."
            "It's like I can feel all of the confidence and warmth they gave me being stripped away."
            show morgan annoyed
            morgan.say "Ah, [hero.name]..."
            mike.say "Y...yeah, Morgan?"
            show fx question
            morgan.say "What are you doing?"
            "Well, here we go."
            "I guess it's now or never..."
            mike.say "Morgan..."
            mike.say "Will you..."
            show morgan surprised
            mike.say "Will you marry me?"
            "I make sure to hold up the ring as I say this, wanting to be sure that Morgan sees it."
            "The look of surprise on Morgan's face fills me with an instant feeling of panic."
            "Why isn't she saying anything to me?"
            "Why is she looking so confused all of a sudden?"
            "My proposal can't have been that shocking, surely?"
            "I mean, what else does a guy bend the knee to ask his girlfriend?"
            "Surely this can only mean that she's hesitating because of something else?!?"
            "Finally, Morgan shakes her head, seeming to free herself from the momentary funk that had seized her."
            "She opens her mouth to speak."
            "And I'm literally hanging on whatever the next words will be..."
            show morgan sad
            "The very moment that Morgan starts to shake her head, I can feel it begin."
            "The sensation is like my guts turning to water and then draining out of me completely."
            "And so when she actually does speak, it's almost like I already know what she's going to say."
            morgan.say "[hero.name]..."
            morgan.say "I had no idea you were going to ask me that!"
            mike.say "Well, that's kind of the point, Morgan."
            mike.say "It wouldn't have been a surprise if you knew I was going to propose, would it?"
            mike.say "But maybe it'd have saved me looking like such a moron..."
            morgan.say "I'm just not ready for that kind of commitment yet."
            "I put the ring away and start to get slowly to my feet."
            mike.say "Ah...okay, Morgan."
            show morgan normal
            "Morgan smiles at this, and I can see that she's already feeling relieved at being let off the hook."
            $ morgan.love -= 25
            $ morgan.sub -= 25

    elif morgan.male > 33:
        show morgan
        "I really thought that I'd come a long way with Morgan recently, that I'd gotten over my previous issues."
        "Since we started dating, things have gone from casual to pretty serious in what feels like no time at all."
        "And all of the awkwardness that I used to feel around her almost a fading memory, a thing of the past."
        "That was why I got it into my head that it was high time I did something to capitalise on all of this progress."
        "But what was that going to be?"
        "I wanted to make a statement to Morgan, let her know just how much I felt for her."
        "And I was also pretty keen to ensure that things kept going the way they had been too."
        "So what better thing to do than buy a ring and propose to her?"
        "Yeah, I know - that makes it sound so simple, when it's anything but."
        "The thing is, I wasn't thinking straight at the time, or I'd have come to the same conclusion."
        "I guess I was just carried along on a wave of affection for Morgan."
        "And so it was only when I found myself getting down on one knee that this finally occurred to me!"
        "So, I'm down here, with the ring in my hand."
        show morgan surprised
        "Morgan's just spotted what I'm doing."
        "But from the look on her face, I can tell that she's not fully grasped the meaning of my actions."
        "Oh God - why is it only now that I realise the gravity of what I'm doing?"
        "I'm putting myself right in the firing line here."
        "What if she says no?"
        "What if she laughs in my face or runs away at the sight of the ring?"
        "What if she actually says yes?!?"
        "I can feel all of the former issues and hang-ups that I had around Morgan begin to return."
        "And suddenly it's like none of the dates that we've been on exist anymore."
        "All of the times that we've talked, been honest with each other and seemed to bond."
        "It's like I can feel all of the confidence and warmth they gave me being stripped away."
        show morgan annoyed
        morgan.say "Ah, [hero.name]..."
        mike.say "Y...yeah, Morgan?"
        show fx question
        morgan.say "What are you doing?"
        "Well, here we go."
        "I guess it's now or never..."
        mike.say "Morgan..."
        mike.say "Will you..."
        show morgan surprised
        mike.say "Will you marry me?"
        "I make sure to hold up the ring as I say this, wanting to be sure that Morgan sees it."
        "The look of surprise on Morgan's face fills me with an instant feeling of panic."
        "Why isn't she saying anything to me?"
        "Why is she looking so confused all of a sudden?"
        "My proposal can't have been that shocking, surely?"
        "I mean, what else does a guy bend the knee to ask his girlfriend?"
        "Surely this can only mean that she's hesitating because of something else?!?"
        "Finally, Morgan shakes her head, seeming to free herself from the momentary funk that had seized her."
        "She opens her mouth to speak."
        "And I'm literally hanging on whatever the next words will be..."
        if morgan.love >= 195:
            show morgan normal
            "When Morgan starts to nod her head eagerly, I almost forget what the gesture actually means."
            "But a deeper part of me must be more aware of the moment, as I can already feel butterflies in my stomach."
            "Morgan bites her lip as she grabs hold of my hands and pulls me to my feet."
            "She almost looks like she's fit to burst with the emotions building up inside of her!"
            morgan.say "[hero.name], do you really mean it?!?"
            "I have to admit, that wasn't what I was expecting to hear!"
            mike.say "Ah, yeah, Morgan - I mean it!"
            show morgan happy
            morgan.say "Then my answer's yes."
            morgan.say "Yes, I will marry you!"
            "She waggles her fingers in front of my face, an urgent look in her eyes as she does so."
            morgan.say "Well, what are you waiting for?"
            morgan.say "Put the damn ring on my finger, before you change your mind!"
            "I rush to do as I'm told, fumbling the ring onto Morgan's outstretched finger."
            "And as I do so, I note that she said before I changed my mind - not before SHE did!"
            "Does that mean she's actually worried I might be the one to get cold feet?!?"
            "I guess it's perfectly possible for a girl to have all those same insecurities as a guy."
            "But I could never have imagined that someone as cocky and confident as Morgan doubted herself for as much as a second."
            "And it's even more amazing to think that she could have thought my feelings for her might ever have cooled!"
            "Just goes to show that you can never know all there is to know about someone."
            mike.say "I was worried, Morgan."
            mike.say "Worried that you might say no!"
            show morgan normal
            "Morgan's looking down at the ring on her finger as I say this, admiring it intently."
            "But she glances up at my words, a quizzical look in her eyes."
            morgan.say "Well, I was worried that you might never ask."
            morgan.say "So I guess that shows how much either of us doesn't know!"
            morgan.say "But seriously, [hero.name] - I do know that I want to be with you."
            morgan.say "And that's enough for me."
            "All I can do is smile at that statement, lost for words and filled with happiness."
            "It's not just that I'm glad to have Morgan back in my life after so long."
            "Even more so, it's that I've discovered a whole new world of possibilities along with her too."
            $ morgan.set_fiance()
        else:
            show morgan sad
            "The very moment that Morgan starts to shake her head, I can feel it begin."
            "The sensation is like my guts turning to water and then draining out of me completely."
            "And so when she actually does speak, it's almost like I already know what she's going to say."
            morgan.say "Oh, [hero.name]..."
            morgan.say "I had no idea you were going to ask me that!"
            mike.say "Well, that's kind of the point, Morgan."
            mike.say "It wouldn't have been a surprise if you knew I was going to propose, would it?"
            mike.say "But maybe it'd have saved me looking like such a moron..."
            "The way I leave the words hanging in the air makes Morgan jump to attention."
            "Suddenly she seems to realise that she's left me hanging too!"
            morgan.say "Oh, [hero.name]..."
            morgan.say "This is all so sweet of you, so romantic..."
            mike.say "There's a but coming, isn't there?"
            morgan.say "But I'm just not ready for that kind of commitment yet."
            morgan.say "I mean, it's SO great to know that YOU are."
            morgan.say "It's not you though - it's me!"
            "Am I actually hearing this?"
            "Did she just fall back on the biggest cliche of all time?"
            "But even if she did, what can I do about it?"
            "Sure, I could spend the rest of the day trying to talk Morgan around."
            "But it'd just be me arguing that she should do something she obviously doesn't want to."
            "And I'm just not the kind of guy to want to marry someone that's been coerced into it!"
            "So I put the ring away and start to get slowly to my feet."
            mike.say "Ah...okay, Morgan."
            mike.say "I hear what you're saying."
            mike.say "Thanks for being honest with me - it means a lot."
            show morgan normal
            "Morgan smiles at this, and I can see that she's already feeling relieved at being let off the hook."
            "But there's also the sheer amount of guilt that you'd expect at turning down a genuine proposal."
            "I could easily exploit that, but then I don't think I'm comfortable being that guy."
            morgan.say "No, [hero.name] - thank YOU for thinking of me like that."
            morgan.say "And who knows, maybe I'll be in the same place the next time you ask me!"
            "I nod and smile, silently hoping that I'll be able to summon up the courage to try for a second time."
            $ morgan.love -= 25
            $ morgan.sub -= 25
    else:

        show morgan
        "There wasn't one moment when I was planning this when I even as much as stopped to wonder if it was a good idea or not."
        "Right from the start, I was sure that buying a ring and popping the question to Morgan was the right thing to do."
        "After all, we've been getting on like a house on fire since we started dating, and it's almost as hot too!"
        "And even when we're not together, she's almost always on my mind or only a thought away."
        "I'm either remembering what we got up to the last time I saw her or else planning the next time we get together."
        "She's just so sweet, loving and adorable that I can't believe this is the same girl that I knew all those years ago."
        "I mean, the Morgan I used to know was such a tomboy that I actually mistook her for the real thing!"
        "But now she only seems to be interested in making herself pretty for me and doing all she can to make sure I'm happy."
        "And the other day, Morgan almost walked into a web that had one of the biggest spiders in it that I'd ever seen."
        "I was expecting her to brush it out of the way, just like she would have done when we were kids."
        "Instead she let out a squeal and literally jumped into my arms to get away from it!"
        "Sure, I was shocked at first."
        "It's not the kind of thing you expect any modern girl to do in that situation."
        "But I have to admit that, at the time, it was a real turn-on!"
        "Just knowing that she was looking to me to save her from something that scared her."
        "Even though it was a pretty tiny spider that was probably more scared of her than she was of it..."
        "I suppose that's one of the reasons that I wanted to propose to Morgan in the first place."
        "She makes me want to keep right on protecting her."
        "To make sure that nothing in the world can possibly harm her ever again."
        "Well, maybe just scare her, if it's something like that spider I just mentioned..."
        "So as soon as I feel like the time is right, I seize the opportunity and go down on one knee."
        show morgan surprised
        if morgan.love >= 195:
            mike.say "Morgan, I wanted to ask..."
            mike.say "Would you..."
            show morgan normal
            "I find myself stopping before I can get all of my words out."
            "The ring still in its box, is clutched tightly in my hands."
            "And it's not because of the look on Morgan's face."
            "It's more because I swear I can actually hear her vibrating with glee."
            "Her eyes are as large and saucers and her smile almost reaches all the way to her ears."
            "In fact, Morgan looks so elated that she reminds me of something out of a cutesy anime series!"
            mike.say "Ah, Morgan..."
            mike.say "Would you...would you marry me?"
            show morgan happy
            "At this, Morgan clenches her hands under her chin."
            "And then literally starts to jump up and down on the spot."
            morgan.say "Oh yes, yes, yes!"
            morgan.say "One million times yes!"
            morgan.say "Of course I'll marry you, [hero.name]."
            morgan.say "Do you even have to ask?!?"
            morgan.say "Well, of course you did."
            morgan.say "Otherwise you couldn't have proposed just now!"
            mike.say "Whoa, Morgan, settle down a bit, yeah?"
            mike.say "You're babbling like crazy!"
            show morgan normal
            "Morgan shakes her head and I see her eyes become more focused and less glazed-over."
            "It's as if she's throwing off the craziness that had hold of her a moment before."
            morgan.say "Oh, right..."
            morgan.say "Sorry, my head was suddenly so full of wonderful thoughts, that's all!"
            "I smile a little warily as I take the ring out its box and slide it onto her finger."
            "The whole time I'm genuinely worried that she might start up with the babbling again."
            "I stand up slowly, still holding onto Morgan's hand."
            "She looks at me the whole time, as if waiting for some kind of unspoken cue."
            "Not knowing quite what's expected of me, I give her my best and most sincere smile."
            show morgan happy
            "Which prompts Morgan to throw her arms around my waist and hug me as hard as she possibly can."
            "Before I can return the gesture, I feel like the air is being squeezed out of my lungs."
            "Jesus Christ - was she always this strong?"
            "Or has all of this proposal business given her a crazed adrenaline boost?"
            "Whatever the answer, I hug Morgan back the best I can."
            "Because I got the answer that I wanted."
            "And in the end, that's all that matters."
            $ morgan.set_fiance()
        else:
            "Almost as soon as I'm down there and fumbling for the ring, I know that I've made a terrible mistake."
            "Morgan's eyes go as wide as saucers, and I can almost see the moment she realises what's going on."
            "But I'm committed now, the ring in my hand as I pop the box open and prepare to pop the question too."
            "After all, what would be worse - being turned down or having to stop before I actually proposed to her?"
            mike.say "Morgan, I wanted to ask..."
            mike.say "Would you..."
            morgan.say "Oh god...oh god...oh god!"
            morgan.say "This is really happening, isn't it?"
            mike.say "Ah, yeah, Morgan."
            mike.say "I'm really asking you to marry me!"
            "Morgan seems like she's about to say something."
            "But then she clamps both hands over her mouth, shaking her head as she does so."
            "I can see what looks like actual terror in her eyes, as well as confusion."
            "Trying to stand up and ask what's wrong, I inadvertently move the ring even closer to her."
            "Morgan lurches back from it, like a vampire menaced with garlic."
            hide morgan
            "And a moment later, she turns her back on me, running away without another word."
            "She leaves me alone, mouth hanging open and the ring still in the palm of my hand."
            "I guess that's her way of saying no."
            "But she could have perhaps been a little less dramatic about it..."
            $ morgan.love -= 25
            $ morgan.sub -= 25
            $ hero.cancel_activity()
            $ game.pass_time(1)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
