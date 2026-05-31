init python:
    Event(**{
    "name": "home_harem_girls_couch_fun",
    "label": "home_harem_girls_couch_fun",
    "duration": 1,
    "priority": 0,
    "conditions": [
        TogetherInHarem('home', 'bree', 'minami', 'samantha', 'sasha'),
        PersonTarget(bree,
                Not(IsHidden()),
                Not(IsActivity("sleep")),
                HasRoomTag("home")),
        PersonTarget(minami,
                Not(IsHidden()),
                Not(IsActivity("sleep")),
                HasRoomTag("home")),
        PersonTarget(samantha,
                Not(IsHidden()),
                Not(IsActivity("sleep")),
                HasRoomTag("home")),
        PersonTarget(sasha,
                Not(IsHidden()),
                Not(IsActivity("sleep")),
                HasRoomTag("home")),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home")),
        ],
    "chances": 20,
    "do_once": False,
    "once_month": True,
    "quit": False,
    })


    Event(**{
    "name": "home_harem_compare_bellies",
    "label": "home_harem_compare_bellies",
    "duration": 1,
    "priority": 0,
    "conditions": [
        IsActiveHarem('home'),
        HeroTarget(
            IsGender("male"),
            HasRoomTag("home")),
        ],
    "do_once": False,
    "once_week": True,
    "block_when_canceled": False,
    "quit": False,
    })

label home_harem_girls_couch_fun:
    show bg house with fade
    "It's been one of those days when I feel like I haven't stopped once."
    "From the moment the alarm went off to right this moment as I'm getting home."
    "Everything is a blur of business, stress and frustration."
    "And I feel like just going to my room where I can finally collapse onto the bed."
    "Part of me wants to call out as I close the door behind me."
    "Just for the sake of letting the girls know that I've made it home."
    "I don't want to talk to any of them right now."
    "But it just feels like the polite thing to do."
    "So I open my mouth to shout to whoever's listening."
    "But then I stop, hearing something close by."
    "It's coming from the direction of the sitting-room."
    "And it sounds pretty intense from what I can hear."
    "Hmm...maybe the girls are playing Twister or something?"
    "My bed is still calling to me."
    "But my head keeps turning towards the source of the sounds."
    "And in the end I can't resist taking a quick look for myself."
    "I just want to satisfy my curiosity, that's all."
    "Then I'll go to my room and get some much needed sleep."
    "I'm yawning as I make it to the sitting-room door."
    "And I'm fully expecting to just say hi to the girls once I peek inside."
    "But the yawn turns into a kind of gasping sound as I see them."
    "And I only just manage to strangle that off before I give myself away too."
    "Because what I see inside leaves me in a state of complete surprise."
    scene bg black
    show girls couch fun samantha bree sasha minami
    if Harem.find('lexi', name='home'):
        show girls couch fun lexi
    with fade
    "I was right in as much as the girls are one massive tangle of limbs."
    "But the fact that they're all naked tells me they're not playing Twister!"
    "They're all huddled around one of the sofas, not looking in my direction."
    "Which means I can see Sam, sprawled on one end of the sofa."
    "She's leaning back, her legs spread wide apart."
    "[bree.name]'s on her hands and knees before Sam, head buried between her thighs."
    "Minami is kneeling on the sofa beside Sam, their lips pressed together."
    "Sasha is close by too, licking and nibbling at Minami's exposed breasts."
    if Harem.find('lexi', name='home'):
        "And finally I see Lexi, her tongue exploring Sasha's butt!"
    "I pull a little way back from the door."
    "Just enough to be sure they won't see me."
    "And I try to clear my mind as I consider my next move."
    menu:
        "Leave quietly":
            "Geez..."
            "What in the hell am I actually thinking right now?"
            "There's nothing to consider!"
            "I can't stand here and keep watching them go at it."
            "And that's because I'm not some kind of pervert!"
            "Shaking my head I back away from the sitting-room door."
            scene bg bedroom1 with fade
            "Then I make my way to my bedroom, quickly and quietly."
            "I don't think I'm ever going to forget what I just saw."
            "But at least I can say that seeing it was an accident."
        "Stay and watch":
            "Who am I kidding?"
            "There's only one thing that I'm going to do right now."
            "And that's staying right by the door, watching them go at it!"
            "Peeking back around the door, I get into the perfect position."
            "Damn it - I wish I'd made it home sooner."
            "That way I could have seen them working up to it."
            "But I guess I should just be glad I'm getting to see anything at all."
            "And it's not like I arrived on the scene too late either."
            "The girls are going at it like crazy in there."
            "And I can feel my cock getting harder by the moment."
            "Everything seems to be revolving around Sam."
            "Like the other girls are all clambering to get to her."
            "[bree.name]'s the one getting the most intimacy right now."
            "Her head is almost obscured by Sam's thighs."
            "But then they open wider still, and I get a better view."
            "[bree.name]'s tongue and lips are in constant motion."
            "One moment they're moving around the edges of Sam's pussy."
            "And the next they dive into the centre, probing deeply."
            "Sam moans and rolls her head at the same time."
            "At first I think [bree.name]'s the source of her pleasure."
            "But then I realise she's only moaning when Minami's not kissing her."
            "As if sensing my thoughts, Minami redoubles her efforts."
            "Her tongue darts between Sam's lips, exploring her mouth."
            "And on top of that, I can see their nipples rubbing together!"
            "Sam's large breasts and Minami's petite chest, swaying in time."
            "Their nipples are hard and erect, looking so good from where I'm standing."
            "Then, just as I noticed Minami pleasuring Sam, I see what Sasha's doing to her too."
            "Her hands are all over the smaller girl's body."
            "But what's even more exciting is the way she's nibbling at Minami's nipples!"
            "I swallow at the sight, not only because it's so hot."
            "But also because Sasha seems so demure as she does it."
            "I'd expected her to be the one setting the pace."
            "And yet she's looking up at Minami almost in submission."
            if any(Harem.find('lexi', name='home')):
                "My eyes follow the lines of Sasha's body."
                "And then they reach the curve of her butt."
                "Which is where I see the reason for her mood."
                "Lexi's tongue is right there, darting this way and that."
                "It keeps on probing between Sasha's buttocks."
                "And every time it does, Sasha moans and tosses her head."
                "I can't help looking past Lexi for a moment."
                "Part of me wondering if someone is pleasuring her too!"
                "But to my disappointment, I see Lexi's the last link in the chain."
            menu:
                "Masturbate":
                    "It's not like a make a conscious decision to put my hand into my pants."
                    "I just find myself doing it without thinking."
                    "It happens like the most natural thing in the world."
                    "And before I know it, I'm jerking myself off to what I see in there."
                    "All those bodies moving together."
                    "So much female flesh on show at once."
                    "I hardly know where to look as I go ever faster."
                    "And I feel myself shooting my load as something happens in the sitting room."
                    $ hero.fun += 1
                    $ hero.energy -= 1
                "Just watch":
                    "My heart is pounding in my chest."
                    "My breath is coming in ragged gasps too."
                    "Shit - I feel like I'm in the middle of this thing with them!"
                    "And the feeling only gets more intense as I watch it build to all come to a head."
            "One after another, the girls all start to cum."
            "It works it's way through them like a cascade."
            "And before too long, they're all gripped in the throes of an orgasm."
            "I hold my breath as I watch, wondering how often this kind of thing happens."
            "I mean, it has to be a pretty rare thing, right?"
            "But even as the girls are writhing with pleasure, I'm returning to reality."
            "Now would be a really good time to beat a hasty retreat."
            scene bg bedroom1 with fade
            "And so I turn away from the door, heading for my bedroom."
            "I just hope I can keep the image of what I saw in my head."
            "Because I don't think I'll see something like that again for a long time!"
    return

label home_harem_compare_bellies:
    python:
        hh_members_at_home = Harem.find_by_name("home").active_members_in_room
        hh_pregnant_members = [i for i in hh_members_at_home if Person.find(i).activity["activity"] != "sleep" and Person.find(i).is_visibly_pregnant]
        if game.flags.hh_compared_bellies:
            hh_pregnant_members = list(set(hh_pregnant_members) - set(game.flags.hh_compared_bellies))
    if hh_pregnant_members and len(hh_pregnant_members) > 1:
        "The best thing about a fantasy when it remains a fantasy is that you really don't have to put all that much thought into it."
        "I mean, you might spend a long time fleshing out the details in your mind."
        "But I can almost guarantee that you're just thinking about the fun parts, and not the practical matters."
        "It's only when a fantasy actually becomes reality that some of the less obvious details start to become apparent."
        "Sure, it's a whole lot of fun to be fooling around with a bunch of girls instead of just one."
        "But the inherent pitfalls are multiplied by the same factor as well."
        "Never in my wildest dreams did I ever think that I'd be watching as the girls compare the size of their bellies."
        "I was always worried about getting just the one girl pregnant - never mind a whole bunch of them!"
        if len(hh_pregnant_members) == 5:
            $ renpy.show(hh_pregnant_members[0], at_list=[mostleft5])
            $ renpy.show(hh_pregnant_members[1], at_list=[left5])
            $ renpy.show(hh_pregnant_members[2], at_list=[mostright5])
            $ renpy.show(hh_pregnant_members[3], at_list=[right5])
            $ renpy.show(hh_pregnant_members[4])
        elif len(hh_pregnant_members) == 4:
            $ renpy.show(hh_pregnant_members[0], at_list=[mostleft4])
            $ renpy.show(hh_pregnant_members[1], at_list=[left4])
            $ renpy.show(hh_pregnant_members[2], at_list=[mostright4])
            $ renpy.show(hh_pregnant_members[3], at_list=[right4])
        elif len(hh_pregnant_members) == 3:
            $ renpy.show(hh_pregnant_members[0], at_list=[left])
            $ renpy.show(hh_pregnant_members[1])
            $ renpy.show(hh_pregnant_members[2], at_list=[right])
        elif len(hh_pregnant_members) == 2:
            $ renpy.show(hh_pregnant_members[0], at_list=[left])
            $ renpy.show(hh_pregnant_members[1], at_list=[right])
        if "bree" in hh_pregnant_members:
            show bree normal
            bree.say "I think you're just a little bit bigger than me right now."
        if "sasha" in hh_pregnant_members:
            show sasha normal
            sasha.say "I know, I know...I feel like a whale!"
        if "lexi" in hh_pregnant_members:
            show lexi normal
            lexi.say "Urgh...I never thought I'd be this fat!"
        if "minami" in hh_pregnant_members:
            show minami normal
            minami.say "I always thought I'd have a neat little bump."
        if "samantha" in hh_pregnant_members:
            show samantha normal
            samantha.say "Yeah, I feel like a sumo wrestler!"
            if "bree" in hh_pregnant_members:
                show bree happy
                bree.say "Oh no, don't be silly - you look positively radiant!"
        if "sasha" in hh_pregnant_members:
            show sasha annoyed
            sasha.say "Yeah, yeah...I'm sweating like crazy, you know?"
        if "bree" in hh_pregnant_members:
            show bree annoyed
            bree.say "Tell me about it - and then there's the morning sickness and the swelling ankles..."
        if "lexi" in hh_pregnant_members:
            show lexi annoyed
            lexi.say "I wanna puke every time I wake up in the morning!"
        if "minami" in hh_pregnant_members:
            show minami annoyed
            minami.say "I wish I had some of those paper bags they give you on a plane!"
        if "samantha" in hh_pregnant_members:
            show samantha annoyed
            samantha.say "More like a bucket!"
        if "sasha" in hh_pregnant_members:
            show sasha normal
            sasha.say "Not to mention my breasts!"
        if "bree" in hh_pregnant_members:
            show bree normal
            bree.say "Oh god!"
        if "lexi" in hh_pregnant_members:
            show lexi normal
            lexi.say "My fucking boobs!"
        if "minami" in hh_pregnant_members:
            show minami normal
            minami.say "I wanted bigger breasts, sure - but not like this!"
        if "samantha" in hh_pregnant_members:
            show samantha normal
            samantha.say "Yeah, none of my bra's fit anymore!"
        "My ears can't help perking up at this last topic of discussion."
        if "bree" in hh_pregnant_members:
            bree.say "Urgh...I feel like they're getting bigger every day."
            bree.say "Like I'm going to grow udders and turn into a cow or something!"
        if "lexi" in hh_pregnant_members:
            lexi.say "I feel like I wanna be milked every day!"
        if "minami" in hh_pregnant_members:
            minami.say "I could start going 'MOO!' it's so bad!"
        if "sasha" in hh_pregnant_members:
            sasha.say "My nipples are like..."
        "The conversation trails off as they see that I'm trying to listen in without being noticed."
        "I flash a nervous smile in their direction, shrugging innocently."
        mike.say "I...erm...couldn't help overhearing!"
        "I'm honestly expecting to be told off for eaves-dropping."
        "Or at the very least be told to butt out of their private and rather intimate conversation."
        "But instead they all smile at me as one."
        "And suddenly I have multiple swollen bellies thrust in my direction."
        if "bree" in hh_pregnant_members:
            bree.say "It's okay, [hero.name] - after all, you're going to be a father twice over!"
        "I get the distinct feeling that I'm supposed to touch them."
        "But it's so sudden - and more than a little creepy too!"
        if "sasha" in hh_pregnant_members:
            sasha.say "[hero.name], we should be including you in all of these chats."
            show sasha happy
            sasha.say "You're gonna have a hell of a lot on your shoulders when these babies come along!"
        if "bree" in hh_pregnant_members:
            show bree happy
            bree.say "Nappies to change, bottles to make, a buggy to push!"
        if "lexi" in hh_pregnant_members:
            show lexi happy
            lexi.say "Clothes to buy and cots to put together!"
        if "minami" in hh_pregnant_members:
            show minami happy
            minami.say "Lullabies to learn and bedtime stories to read!"
        if "samantha" in hh_pregnant_members:
            show samantha happy
            samantha.say "Even kindergartens and schools to choose!"
        "I can already feel the ripples of fear making the hairs on the back of my neck stand up."
        "Why has none of this occurred to me before now?"
        "For some crazy reason, I'd thought the fact there were more than two of us in this relationship meant there's be less work involved."
        "But of course, if all the girls are both going to give birth around the same time, the exact opposite will be true."
        "Oh god - it's not just going to be the babies that I have to run around after either."
        "I'll basically be a slave to the hormonally tortured whims of a harem too!"
        "I can feel my eyes growing wide in horror at the thought of what awaits me..."
        if "bree" in hh_pregnant_members:
            bree.say "Aww, look - he's getting all dewy-eyed at the thought of being a daddy!"
        if "lexi" in hh_pregnant_members:
            lexi.say "Aw, you big softie!"
        if "minami" in hh_pregnant_members:
            minami.say "You can't wait to meet them - can you big bro!"
        if "samantha" in hh_pregnant_members:
            samantha.say "You're already thinking about being a parent - right, [hero.name]?"
        "I look up, surprised at the way in which the girls misinterpret my reaction."
        "But before I can say a word, they throw me for a second time by suddenly bursting into floods of tears."
        mike.say "Wh...what's...what's the matter?"
        mike.say "What did I say?!?"
        "By way of answer, they shake their heads and wrap their arms around each other."
        if "sasha" in hh_pregnant_members:
            show sasha cry
            sasha.say "It's not your fault, [hero.name]."
            sasha.say "It's these damn mood swings."
            sasha.say "I HATE THEM SO MUCH!"
        if "bree" in hh_pregnant_members:
            show bree cry
            bree.say "The emotions are crazy - from the hormones!"
        if "lexi" in hh_pregnant_members:
            show lexi sad
            lexi.say "It's like an emotional roller-coaster."
            lexi.say "And I can't get off!"
        if "minami" in hh_pregnant_members:
            show minami cry
            minami.say "This...this is WAY worse than going through puberty!"
        if "samantha" in hh_pregnant_members:
            show samantha cry
            samantha.say "I just can't seem to control my feelings!"
        "With what looks like a serious amount of effort, they shake it off for a moment."
        "And I find myself being stared at by multiple pairs of pink, swollen eyes!"
        if "bree" in hh_pregnant_members:
            bree.say "I'm not upset."
            bree.say "I'm...sniff...just so...sniff...happy!"
        if "sasha" in hh_pregnant_members:
            sasha.say "This is such a...a happy time!"
        if "lexi" in hh_pregnant_members:
            lexi.say "I'm so happy I could puke!"
            lexi.say "And I probably will!"
        if "minami" in hh_pregnant_members:
            minami.say "I've never felt so happy, so complete!"
        if "samantha" in hh_pregnant_members:
            samantha.say "It sounds crazy, I know..."
            samantha.say "But I wouldn't change a thing!"
        "And with that, they collapse into a second round of tears, heads buried into each others shoulders."
        "All that I can think to do is pat them each on the shoulder and offer a few bland platitudes."
        "I feel useless and without a clue as to what would be the best thing to do for any of them."
        "And a large part of me is almost convinced that I'm going to be the only sane person left in the house until the babies are actually born!"
        "But after that, I'm sure things are going to be a whole different kind of crazy..."
        if not game.flags.hh_compared_bellies:
            $ game.flags.hh_compared_bellies = hh_pregnant_members
        else:
            $ game.flags.hh_compared_bellies.extend(hh_pregnant_members)
    else:
        $ hero.cancel_event()
    return


label bree_lexi_minami_samantha_sasha_propose_male:
    "I know that I keep going on about how unbelievably amazing it is to be involved with my housemates."
    "But that's just something that you're going to gave to get used to hearing from me on the subject."
    "Maybe sometime in the future I'll have gotten used to the idea and it won't seem like such a big deal."
    "And then again, maybe I'll never stop waking up and thinking that I'm the luckiest guy in the world!"
    "Either way, everything seems to be going well for us right now."
    "Everyone's getting along fine and we're having a hell of a lot of fun together too."
    "So you're probably thinking that I'm just going to go along with things as they are."
    "I mean, why would I want to mess with success?"
    "Well, maybe I want to make the arrangement a little more, shall we say, permanent?"
    "That's right - I'm going to ask the girls to marry me."
    "It makes sense to me, formalising our relationship and making a commitment to each other."
    "And I'm gambling on the notion that the girls will feel the same way too."
    show minami tehe at mostleft5
    show bree evil at left5
    show sasha annoyed
    show lexi bubblegum at right5
    show samantha happy at mostright5
    with dissolve
    "So as soon as we're all together and the perfect moment arises, I pop the question."
    mike.say "Ah, guys..."
    mike.say "There's something I wanted to ask you..."
    show minami normal
    show bree normal
    show sasha normal
    show lexi normal
    show samantha normal
    "Suddenly their heads turn in unison."
    "And all eyes are on me!"
    "Shit, I thought this was going to be much easier."
    "I feel like they're gazing into my soul!"
    mike.say "I guess I should do this the right way!"
    "I drop onto one knee, right in front of the girls."
    "This causes a flood of mixed reactions from them."
    "One moment they look confused, the next amazed."
    "Maybe this is how it's supposed to be?"
    mike.say "Will..."
    mike.say "Will you marry me?"
    show minami surprised
    show bree surprised
    show sasha surprised
    show lexi surprised
    show samantha surprised
    mike.say "Will all of you marry me?"
    mike.say "And, I guess, each other too?"
    "It doesn't take long for me to get an answer..."
    if bree.love < 195:
        show bree annoyed
        bree.say "[hero.name], you can't be serious?!?"
        bree.say "How would that even work?"
        $ bree.sub -= 25
        $ bree.love -= 25
    else:
        bree.say "[hero.name], are you serious?!?"
        show bree happy
        bree.say "Of course I will!"
        $ bree.set_fiance()
    if sasha.love < 195:
        show sasha annoyed
        sasha.say "Are you out of your mind?!?"
        sasha.say "I didn't get into this thing to get married!"
        $ sasha.sub -= 25
        $ sasha.love -= 25
    else:
        sasha.say "Wow - that came out of the blue!"
        show sasha happy
        sasha.say "But yeah, I will!"
        $ sasha.set_fiance()
    if minami.love < 195:
        show minami annoyed
        minami.say "Big bro, have you gone crazy?"
        minami.say "I can't get married to everyone!"
        $ minami.sub -= 25
        $ minami.love -= 25
    else:
        minami.say "Big bro, you're the best!"
        show minami happy
        minami.say "I will...I will...I will!"
        $ minami.set_fiance()
    if samantha.love < 195:
        show samantha annoyed
        samantha.say "Wow, [hero.name], I already got burnt once."
        samantha.say "And that was with only one spouse!"
        samantha.say "Count me out."
        $ samantha.sub -= 25
        $ samantha.love -= 25
    else:
        samantha.say "Well, I got burned the first time."
        samantha.say "But that was then and this is now."
        show samantha happy
        samantha.say "So yeah, I will!"
        $ samantha.set_fiance()
    if lexi.love < 195:
        show lexi annoyed
        lexi.say "You can't marry all of us."
        lexi.say "That's too wild, even for me!"
        $ lexi.sub -= 25
        $ lexi.love -= 25
    else:
        lexi.say "All of us get married?!?"
        show lexi happy
        lexi.say "That's wild - I'm in!"
        $ lexi.set_fiance()
    "Answering the question must have been a mind-blowing experience for the girls."
    "Because listening to what they had to say certainly was for me."
    "In fact, it takes me a moment to actually wrap my head around what they said."
    if all([g.flags.engagedmike for g in [bree, sasha, minami, samantha, lexi]]):
        mike.say "Y...you all said yes?"
        mike.say "All of you really want to marry me?!?"
        "My second question is met with more amusement and irritation."
        "The girls shake their heads and roll their eyes at me."
        bree.say "Oh, [hero.name]!"
        sasha.say "Seriously, are you deaf or something?"
        minami.say "Big bro!"
        samantha.say "That's so you, [hero.name], that's so you!"
        lexi.say "Geez, you need to clean out your ears!"
        mike.say "So you did?"
        mike.say "You did say yes?"
        "I get a round of nods and smiles this time."
        "Which is probably for the best."
        "As I don't think I could manage to string together a sentence."
        "I'm too excited right now to do anything of the kind!"
    elif not any([g.flags.engagedmike for g in [bree, sasha, minami, samantha, lexi]]):
        "I feel like I've been punched in the gut."
        "And like it was done with serious intent too!"
        "Did I just go from being the luckiest guy in the world to the suckiest?"
        "I can't believe ALL of them said no!"
        mike.say "Y...you all said no..."
        mike.say "None of you want to get married?!?"
        "The girls are exchanging glances again."
        "But this time they look more than a little guilty."
        "Maybe I should at least take that as some small comfort!"
        bree.say "I'm sorry, [hero.name] - I just can't."
        sasha.say "I'm not the marrying type, [hero.name]!"
        minami.say "I'm too young to get married, big bro!"
        samantha.say "I don't want to make the same mistake again."
        lexi.say "Me get married - are you serious?"
        "All I can do is nod and put on a brave face."
        "But all the same, I think they see how weak my smile is right now."
        "The girls gather round me, trying to offer reassurance."
        "Of course, this doesn't mean that our relationship is over."
        "Though it does make me wonder just how long-term it may prove to be..."
    else:
        "I find myself looking this way and that."
        "Some of the girls look elated at the prospect of marriage."
        "But the others look far more surprised, even worried."
        mike.say "So..."
        mike.say "Some of you don't want to marry me."
        mike.say "And some of you do..."
        "All of a sudden the girls who said yes step forwards."
        "Maybe they're trying to offer me support."
        "Or perhaps they want to separate themselves from the girls that said no."
        if bree.flags.engagedmike:
            bree.say "I do, [hero.name]."
        if sasha.flags.engagedmike:
            sasha.say "I want to marry you!"
        if minami.flags.engagedmike:
            minami.say "Count me in, big bro!"
        if samantha.flags.engagedmike:
            samantha.say "It's a yes from me."
        if lexi.flags.engagedmike:
            lexi.say "Hell yeah!"
        "I can't help smiling as the girls step forwards."
        "We form a tight little knot together, hugging and holding each other."
        "But then I catch a glimpse of the ones that said no."
        "They look suddenly isolated and cast out."
        "And I feel a pang of anxiety in the pit of my stomach."
        "Because I have no idea just what this means for them..."
    return

label bree_lexi_minami_samantha_propose_male:
    "I know that I keep going on about how unbelievably amazing it is to be involved with my housemates."
    "But that's just something that you're going to gave to get used to hearing from me on the subject."
    "Maybe sometime in the future I'll have gotten used to the idea and it won't seem like such a big deal."
    "And then again, maybe I'll never stop waking up and thinking that I'm the luckiest guy in the world!"
    "Either way, everything seems to be going well for us right now."
    "Everyone's getting along fine and we're having a hell of a lot of fun together too."
    "So you're probably thinking that I'm just going to go along with things as they are."
    "I mean, why would I want to mess with success?"
    "Well, maybe I want to make the arrangement a little more, shall we say, permanent?"
    "That's right - I'm going to ask the girls to marry me."
    "It makes sense to me, formalising our relationship and making a commitment to each other."
    "And I'm gambling on the notion that the girls will feel the same way too."
    show minami tehe at mostleft4
    show bree evil at left4
    show lexi bubblegum at right4
    show samantha happy at mostright4
    with dissolve
    "So as soon as we're all together and the perfect moment arises, I pop the question."
    mike.say "Ah, guys..."
    mike.say "There's something I wanted to ask you..."
    show minami normal
    show bree normal
    show lexi normal
    show samantha normal
    "Suddenly their heads turn in unison."
    "And all eyes are on me!"
    "Shit, I thought this was going to be much easier."
    "I feel like they're gazing into my soul!"
    mike.say "I guess I should do this the right way!"
    "I drop onto one knee, right in front of the girls."
    "This causes a flood of mixed reactions from them."
    "One moment they look confused, the next amazed."
    "Maybe this is how it's supposed to be?"
    mike.say "Will..."
    show minami surprised
    show bree surprised
    show lexi surprised
    show samantha surprised
    mike.say "Will you marry me?"
    mike.say "Will all of you marry me?"
    mike.say "And, I guess, each other too?"
    "It doesn't take long for me to get an answer..."
    if bree.love < 195:
        show bree annoyed
        bree.say "[hero.name], you can't be serious?!?"
        bree.say "How would that even work?"
        $ bree.sub -= 25
        $ bree.love -= 25
    else:
        bree.say "[hero.name], are you serious?!?"
        show bree happy
        bree.say "Of course I will!"
        $ bree.set_fiance()
    if minami.love < 195:
        show minami annoyed
        minami.say "Big bro, have you gone crazy?"
        minami.say "I can't get married to everyone!"
        $ minami.sub -= 25
        $ minami.love -= 25
    else:
        minami.say "Big bro, you're the best!"
        show minami happy
        minami.say "I will...I will...I will!"
        $ minami.set_fiance()
    if samantha.love < 195:
        show samantha annoyed
        samantha.say "Wow, [hero.name], I already got burnt once."
        samantha.say "And that was with only one spouse!"
        samantha.say "Count me out."
        $ samantha.sub -= 25
        $ samantha.love -= 25
    else:
        samantha.say "Well, I got burned the first time."
        samantha.say "But that was then and this is now."
        show samantha happy
        samantha.say "So yeah, I will!"
        $ samantha.set_fiance()
    if lexi.love < 195:
        show lexi annoyed
        lexi.say "You can't marry all of us."
        lexi.say "That's too wild, even for me!"
        $ lexi.sub -= 25
        $ lexi.love -= 25
    else:
        lexi.say "All of us get married?!?"
        show lexi happy
        lexi.say "That's wild - I'm in!"
        $ lexi.set_fiance()
    "Answering the question must have been a mind-blowing experience for the girls."
    "Because listening to what they had to say certainly was for me."
    "In fact, it takes me a moment to actually wrap my head around what they said."
    if all([g.flags.engagedmike for g in [bree, minami, samantha, lexi]]):
        mike.say "Y...you all said yes?"
        mike.say "All of you really want to marry me?!?"
        "My second question is met with more amusement and irritation."
        "The girls shake their heads and roll their eyes at me."
        bree.say "Oh, [hero.name]!"
        minami.say "Big bro!"
        samantha.say "That's so you, [hero.name], that's so you!"
        lexi.say "Geez, you need to clean out your ears!"
        mike.say "So you did?"
        mike.say "You did say yes?"
        "I get a round of nods and smiles this time."
        "Which is probably for the best."
        "As I don't think I could manage to string together a sentence."
        "I'm too excited right now to do anything of the kind!"
    elif not any([g.flags.engagedmike for g in [bree, minami, samantha, lexi]]):
        "I feel like I've been punched in the gut."
        "And like it was done with serious intent too!"
        "Did I just go from being the luckiest guy in the world to the suckiest?"
        "I can't believe ALL of them said no!"
        mike.say "Y...you all said no..."
        mike.say "None of you want to get married?!?"
        "The girls are exchanging glances again."
        "But this time they look more than a little guilty."
        "Maybe I should at least take that as some small comfort!"
        bree.say "I'm sorry, [hero.name] - I just can't."
        minami.say "I'm too young to get married, big bro!"
        samantha.say "I don't want to make the same mistake again."
        lexi.say "Me get married - are you serious?"
        "All I can do is nod and put on a brave face."
        "But all the same, I think they see how weak my smile is right now."
        "The girls gather round me, trying to offer reassurance."
        "Of course, this doesn't mean that our relationship is over."
        "Though it does make me wonder just how long-term it may prove to be..."
    else:
        "I find myself looking this way and that."
        "Some of the girls look elated at the prospect of marriage."
        "But the others look far more surprised, even worried."
        mike.say "So..."
        mike.say "Some of you don't want to marry me."
        mike.say "And some of you do..."
        "All of a sudden the girls who said yes step forwards."
        "Maybe they're trying to offer me support."
        "Or perhaps they want to separate themselves from the girls that said no."
        if bree.flags.engagedmike:
            bree.say "I do, [hero.name]."
        if minami.flags.engagedmike:
            minami.say "Count me in, big bro!"
        if samantha.flags.engagedmike:
            samantha.say "It's a yes from me."
        if lexi.flags.engagedmike:
            lexi.say "Hell yeah!"
        "I can't help smiling as the girls step forwards."
        "We form a tight little knot together, hugging and holding each other."
        "But then I catch a glimpse of the ones that said no."
        "They look suddenly isolated and cast out."
        "And I feel a pang of anxiety in the pit of my stomach."
        "Because I have no idea just what this means for them..."
    return

label lexi_minami_samantha_sasha_propose_male:
    "I know that I keep going on about how unbelievably amazing it is to be involved with my housemates."
    "But that's just something that you're going to gave to get used to hearing from me on the subject."
    "Maybe sometime in the future I'll have gotten used to the idea and it won't seem like such a big deal."
    "And then again, maybe I'll never stop waking up and thinking that I'm the luckiest guy in the world!"
    "Either way, everything seems to be going well for us right now."
    "Everyone's getting along fine and we're having a hell of a lot of fun together too."
    "So you're probably thinking that I'm just going to go along with things as they are."
    "I mean, why would I want to mess with success?"
    "Well, maybe I want to make the arrangement a little more, shall we say, permanent?"
    "That's right - I'm going to ask the girls to marry me."
    "It makes sense to me, formalising our relationship and making a commitment to each other."
    "And I'm gambling on the notion that the girls will feel the same way too."
    show minami tehe at mostleft4
    show sasha annoyed at left4
    show lexi bubblegum at right4
    show samantha happy at mostright4
    with dissolve
    "So as soon as we're all together and the perfect moment arises, I pop the question."
    mike.say "Ah, guys..."
    mike.say "There's something I wanted to ask you..."
    show minami normal
    show sasha normal
    show lexi normal
    show samantha normal
    "Suddenly their heads turn in unison."
    "And all eyes are on me!"
    "Shit, I thought this was going to be much easier."
    "I feel like they're gazing into my soul!"
    mike.say "I guess I should do this the right way!"
    "I drop onto one knee, right in front of the girls."
    "This causes a flood of mixed reactions from them."
    "One moment they look confused, the next amazed."
    "Maybe this is how it's supposed to be?"
    mike.say "Will..."
    show minami surprised
    show sasha surprised
    show lexi surprised
    show samantha surprised
    mike.say "Will you marry me?"
    mike.say "Will all of you marry me?"
    mike.say "And, I guess, each other too?"
    "It doesn't take long for me to get an answer..."
    if sasha.love < 195:
        show sasha annoyed
        sasha.say "Are you out of your mind?!?"
        sasha.say "I didn't get into this thing to get married!"
        $ sasha.sub -= 25
        $ sasha.love -= 25
    else:
        sasha.say "Wow - that came out of the blue!"
        show sasha happy
        sasha.say "But yeah, I will!"
        $ sasha.set_fiance()
    if minami.love < 195:
        show minami annoyed
        minami.say "Big bro, have you gone crazy?"
        minami.say "I can't get married to everyone!"
        $ minami.sub -= 25
        $ minami.love -= 25
    else:
        minami.say "Big bro, you're the best!"
        show minami happy
        minami.say "I will...I will...I will!"
        $ minami.set_fiance()
    if samantha.love < 195:
        show samantha annoyed
        samantha.say "Wow, [hero.name], I already got burnt once."
        samantha.say "And that was with only one spouse!"
        samantha.say "Count me out."
        $ samantha.sub -= 25
        $ samantha.love -= 25
    else:
        samantha.say "Well, I got burned the first time."
        samantha.say "But that was then and this is now."
        show samantha happy
        samantha.say "So yeah, I will!"
        $ samantha.set_fiance()
    if lexi.love < 195:
        show lexi annoyed
        lexi.say "You can't marry all of us."
        lexi.say "That's too wild, even for me!"
        $ lexi.sub -= 25
        $ lexi.love -= 25
    else:
        lexi.say "All of us get married?!?"
        show lexi happy
        lexi.say "That's wild - I'm in!"
        $ lexi.set_fiance()
    "Answering the question must have been a mind-blowing experience for the girls."
    "Because listening to what they had to say certainly was for me."
    "In fact, it takes me a moment to actually wrap my head around what they said."
    if all([g.flags.engagedmike for g in [sasha, minami, samantha, lexi]]):
        mike.say "Y...you all said yes?"
        mike.say "All of you really want to marry me?!?"
        "My second question is met with more amusement and irritation."
        "The girls shake their heads and roll their eyes at me."
        sasha.say "Seriously, are you deaf or something?"
        minami.say "Big bro!"
        samantha.say "That's so you, [hero.name], that's so you!"
        lexi.say "Geez, you need to clean out your ears!"
        mike.say "So you did?"
        mike.say "You did say yes?"
        "I get a round of nods and smiles this time."
        "Which is probably for the best."
        "As I don't think I could manage to string together a sentence."
        "I'm too excited right now to do anything of the kind!"
    elif not any([g.flags.engagedmike for g in [sasha, minami, samantha, lexi]]):
        "I feel like I've been punched in the gut."
        "And like it was done with serious intent too!"
        "Did I just go from being the luckiest guy in the world to the suckiest?"
        "I can't believe ALL of them said no!"
        mike.say "Y...you all said no..."
        mike.say "None of you want to get married?!?"
        "The girls are exchanging glances again."
        "But this time they look more than a little guilty."
        "Maybe I should at least take that as some small comfort!"
        sasha.say "I'm not the marrying type, [hero.name]!"
        minami.say "I'm too young to get married, big bro!"
        samantha.say "I don't want to make the same mistake again."
        lexi.say "Me get married - are you serious?"
        "All I can do is nod and put on a brave face."
        "But all the same, I think they see how weak my smile is right now."
        "The girls gather round me, trying to offer reassurance."
        "Of course, this doesn't mean that our relationship is over."
        "Though it does make me wonder just how long-term it may prove to be..."
    else:
        "I find myself looking this way and that."
        "Some of the girls look elated at the prospect of marriage."
        "But the others look far more surprised, even worried."
        mike.say "So..."
        mike.say "Some of you don't want to marry me."
        mike.say "And some of you do..."
        "All of a sudden the girls who said yes step forwards."
        "Maybe they're trying to offer me support."
        "Or perhaps they want to separate themselves from the girls that said no."
        if sasha.flags.engagedmike:
            sasha.say "I want to marry you!"
        if minami.flags.engagedmike:
            minami.say "Count me in, big bro!"
        if samantha.flags.engagedmike:
            samantha.say "It's a yes from me."
        if lexi.flags.engagedmike:
            lexi.say "Hell yeah!"
        "I can't help smiling as the girls step forwards."
        "We form a tight little knot together, hugging and holding each other."
        "But then I catch a glimpse of the ones that said no."
        "They look suddenly isolated and cast out."
        "And I feel a pang of anxiety in the pit of my stomach."
        "Because I have no idea just what this means for them..."
    return

label bree_lexi_samantha_sasha_propose_male:
    "I know that I keep going on about how unbelievably amazing it is to be involved with my housemates."
    "But that's just something that you're going to gave to get used to hearing from me on the subject."
    "Maybe sometime in the future I'll have gotten used to the idea and it won't seem like such a big deal."
    "And then again, maybe I'll never stop waking up and thinking that I'm the luckiest guy in the world!"
    "Either way, everything seems to be going well for us right now."
    "Everyone's getting along fine and we're having a hell of a lot of fun together too."
    "So you're probably thinking that I'm just going to go along with things as they are."
    "I mean, why would I want to mess with success?"
    "Well, maybe I want to make the arrangement a little more, shall we say, permanent?"
    "That's right - I'm going to ask the girls to marry me."
    "It makes sense to me, formalising our relationship and making a commitment to each other."
    "And I'm gambling on the notion that the girls will feel the same way too."
    show sasha annoyed at mostleft4
    show bree evil at left4
    show lexi bubblegum at right4
    show samantha happy at mostright4
    with dissolve
    "So as soon as we're all together and the perfect moment arises, I pop the question."
    mike.say "Ah, guys..."
    mike.say "There's something I wanted to ask you..."
    show sasha normal
    show bree normal
    show lexi normal
    show samantha normal
    "Suddenly their heads turn in unison."
    "And all eyes are on me!"
    "Shit, I thought this was going to be much easier."
    "I feel like they're gazing into my soul!"
    mike.say "I guess I should do this the right way!"
    "I drop onto one knee, right in front of the girls."
    "This causes a flood of mixed reactions from them."
    "One moment they look confused, the next amazed."
    "Maybe this is how it's supposed to be?"
    mike.say "Will..."
    show sasha surprised
    show bree surprised
    show lexi surprised
    show samantha surprised
    mike.say "Will you marry me?"
    mike.say "Will all of you marry me?"
    mike.say "And, I guess, each other too?"
    "It doesn't take long for me to get an answer..."
    if bree.love < 195:
        show bree annoyed
        bree.say "[hero.name], you can't be serious?!?"
        bree.say "How would that even work?"
        $ bree.sub -= 25
        $ bree.love -= 25
    else:
        bree.say "[hero.name], are you serious?!?"
        show bree happy
        bree.say "Of course I will!"
        $ bree.set_fiance()
    if sasha.love < 195:
        show sasha annoyed
        sasha.say "Are you out of your mind?!?"
        sasha.say "I didn't get into this thing to get married!"
        $ sasha.sub -= 25
        $ sasha.love -= 25
    else:
        sasha.say "Wow - that came out of the blue!"
        show sasha happy
        sasha.say "But yeah, I will!"
        $ sasha.set_fiance()
    if samantha.love < 195:
        show samantha annoyed
        samantha.say "Wow, [hero.name], I already got burnt once."
        samantha.say "And that was with only one spouse!"
        samantha.say "Count me out."
        $ samantha.sub -= 25
        $ samantha.love -= 25
    else:
        samantha.say "Well, I got burned the first time."
        samantha.say "But that was then and this is now."
        show samantha happy
        samantha.say "So yeah, I will!"
        $ samantha.set_fiance()
    if lexi.love < 195:
        show lexi annoyed
        lexi.say "You can't marry all of us."
        lexi.say "That's too wild, even for me!"
        $ lexi.sub -= 25
        $ lexi.love -= 25
    else:
        lexi.say "All of us get married?!?"
        show lexi happy
        lexi.say "That's wild - I'm in!"
        $ lexi.set_fiance()
    "Answering the question must have been a mind-blowing experience for the girls."
    "Because listening to what they had to say certainly was for me."
    "In fact, it takes me a moment to actually wrap my head around what they said."
    if all([g.flags.engagedmike for g in [bree, sasha, samantha, lexi]]):
        mike.say "Y...you all said yes?"
        mike.say "All of you really want to marry me?!?"
        "My second question is met with more amusement and irritation."
        "The girls shake their heads and roll their eyes at me."
        bree.say "Oh, [hero.name]!"
        sasha.say "Seriously, are you deaf or something?"
        samantha.say "That's so you, [hero.name], that's so you!"
        lexi.say "Geez, you need to clean out your ears!"
        mike.say "So you did?"
        mike.say "You did say yes?"
        "I get a round of nods and smiles this time."
        "Which is probably for the best."
        "As I don't think I could manage to string together a sentence."
        "I'm too excited right now to do anything of the kind!"
    elif not any([g.flags.engagedmike for g in [bree, sasha, samantha, lexi]]):
        "I feel like I've been punched in the gut."
        "And like it was done with serious intent too!"
        "Did I just go from being the luckiest guy in the world to the suckiest?"
        "I can't believe ALL of them said no!"
        mike.say "Y...you all said no..."
        mike.say "None of you want to get married?!?"
        "The girls are exchanging glances again."
        "But this time they look more than a little guilty."
        "Maybe I should at least take that as some small comfort!"
        bree.say "I'm sorry, [hero.name] - I just can't."
        sasha.say "I'm not the marrying type, [hero.name]!"
        samantha.say "I don't want to make the same mistake again."
        lexi.say "Me get married - are you serious?"
        "All I can do is nod and put on a brave face."
        "But all the same, I think they see how weak my smile is right now."
        "The girls gather round me, trying to offer reassurance."
        "Of course, this doesn't mean that our relationship is over."
        "Though it does make me wonder just how long-term it may prove to be..."
    else:
        "I find myself looking this way and that."
        "Some of the girls look elated at the prospect of marriage."
        "But the others look far more surprised, even worried."
        mike.say "So..."
        mike.say "Some of you don't want to marry me."
        mike.say "And some of you do..."
        "All of a sudden the girls who said yes step forwards."
        "Maybe they're trying to offer me support."
        "Or perhaps they want to separate themselves from the girls that said no."
        if bree.flags.engagedmike:
            bree.say "I do, [hero.name]."
        if sasha.flags.engagedmike:
            sasha.say "I want to marry you!"
        if samantha.flags.engagedmike:
            samantha.say "It's a yes from me."
        if lexi.flags.engagedmike:
            lexi.say "Hell yeah!"
        "I can't help smiling as the girls step forwards."
        "We form a tight little knot together, hugging and holding each other."
        "But then I catch a glimpse of the ones that said no."
        "They look suddenly isolated and cast out."
        "And I feel a pang of anxiety in the pit of my stomach."
        "Because I have no idea just what this means for them..."
    return

label bree_lexi_minami_sasha_propose_male:
    "I know that I keep going on about how unbelievably amazing it is to be involved with my housemates."
    "But that's just something that you're going to gave to get used to hearing from me on the subject."
    "Maybe sometime in the future I'll have gotten used to the idea and it won't seem like such a big deal."
    "And then again, maybe I'll never stop waking up and thinking that I'm the luckiest guy in the world!"
    "Either way, everything seems to be going well for us right now."
    "Everyone's getting along fine and we're having a hell of a lot of fun together too."
    "So you're probably thinking that I'm just going to go along with things as they are."
    "I mean, why would I want to mess with success?"
    "Well, maybe I want to make the arrangement a little more, shall we say, permanent?"
    "That's right - I'm going to ask the girls to marry me."
    "It makes sense to me, formalising our relationship and making a commitment to each other."
    "And I'm gambling on the notion that the girls will feel the same way too."
    show minami tehe at mostleft4
    show bree evil at left4
    show sasha annoyed at mostright4
    show lexi bubblegum at right4
    with dissolve
    "So as soon as we're all together and the perfect moment arises, I pop the question."
    mike.say "Ah, guys..."
    mike.say "There's something I wanted to ask you..."
    show minami normal
    show bree normal
    show sasha normal
    show lexi normal
    "Suddenly their heads turn in unison."
    "And all eyes are on me!"
    "Shit, I thought this was going to be much easier."
    "I feel like they're gazing into my soul!"
    mike.say "I guess I should do this the right way!"
    "I drop onto one knee, right in front of the girls."
    "This causes a flood of mixed reactions from them."
    "One moment they look confused, the next amazed."
    "Maybe this is how it's supposed to be?"
    mike.say "Will..."
    show minami surprised
    show bree surprised
    show sasha surprised
    show lexi surprised
    mike.say "Will you marry me?"
    mike.say "Will all of you marry me?"
    mike.say "And, I guess, each other too?"
    "It doesn't take long for me to get an answer..."
    if bree.love < 195:
        show bree annoyed
        bree.say "[hero.name], you can't be serious?!?"
        bree.say "How would that even work?"
        $ bree.sub -= 25
        $ bree.love -= 25
    else:
        bree.say "[hero.name], are you serious?!?"
        show bree happy
        bree.say "Of course I will!"
        $ bree.set_fiance()
    if sasha.love < 195:
        show sasha annoyed
        sasha.say "Are you out of your mind?!?"
        sasha.say "I didn't get into this thing to get married!"
        $ sasha.sub -= 25
        $ sasha.love -= 25
    else:
        sasha.say "Wow - that came out of the blue!"
        show sasha happy
        sasha.say "But yeah, I will!"
        $ sasha.set_fiance()
    if minami.love < 195:
        show minami annoyed
        minami.say "Big bro, have you gone crazy?"
        minami.say "I can't get married to everyone!"
        $ minami.sub -= 25
        $ minami.love -= 25
    else:
        minami.say "Big bro, you're the best!"
        show minami happy
        minami.say "I will...I will...I will!"
        $ minami.set_fiance()
    if lexi.love < 195:
        show lexi annoyed
        lexi.say "You can't marry all of us."
        lexi.say "That's too wild, even for me!"
        $ lexi.sub -= 25
        $ lexi.love -= 25
    else:
        lexi.say "All of us get married?!?"
        show lexi happy
        lexi.say "That's wild - I'm in!"
        $ lexi.set_fiance()
    "Answering the question must have been a mind-blowing experience for the girls."
    "Because listening to what they had to say certainly was for me."
    "In fact, it takes me a moment to actually wrap my head around what they said."
    if all([g.flags.engagedmike for g in [bree, sasha, minami, lexi]]):
        mike.say "Y...you all said yes?"
        mike.say "All of you really want to marry me?!?"
        "My second question is met with more amusement and irritation."
        "The girls shake their heads and roll their eyes at me."
        bree.say "Oh, [hero.name]!"
        sasha.say "Seriously, are you deaf or something?"
        minami.say "Big bro!"
        samantha.say "That's so you, [hero.name], that's so you!"
        lexi.say "Geez, you need to clean out your ears!"
        mike.say "So you did?"
        mike.say "You did say yes?"
        "I get a round of nods and smiles this time."
        "Which is probably for the best."
        "As I don't think I could manage to string together a sentence."
        "I'm too excited right now to do anything of the kind!"
    elif not any([g.flags.engagedmike for g in [bree, sasha, minami, lexi]]):
        "I feel like I've been punched in the gut."
        "And like it was done with serious intent too!"
        "Did I just go from being the luckiest guy in the world to the suckiest?"
        "I can't believe ALL of them said no!"
        mike.say "Y...you all said no..."
        mike.say "None of you want to get married?!?"
        "The girls are exchanging glances again."
        "But this time they look more than a little guilty."
        "Maybe I should at least take that as some small comfort!"
        bree.say "I'm sorry, [hero.name] - I just can't."
        sasha.say "I'm not the marrying type, [hero.name]!"
        minami.say "I'm too young to get married, big bro!"
        lexi.say "Me get married - are you serious?"
        "All I can do is nod and put on a brave face."
        "But all the same, I think they see how weak my smile is right now."
        "The girls gather round me, trying to offer reassurance."
        "Of course, this doesn't mean that our relationship is over."
        "Though it does make me wonder just how long-term it may prove to be..."
    else:
        "I find myself looking this way and that."
        "Some of the girls look elated at the prospect of marriage."
        "But the others look far more surprised, even worried."
        mike.say "So..."
        mike.say "Some of you don't want to marry me."
        mike.say "And some of you do..."
        "All of a sudden the girls who said yes step forwards."
        "Maybe they're trying to offer me support."
        "Or perhaps they want to separate themselves from the girls that said no."
        if bree.flags.engagedmike:
            bree.say "I do, [hero.name]."
        if sasha.flags.engagedmike:
            sasha.say "I want to marry you!"
        if minami.flags.engagedmike:
            minami.say "Count me in, big bro!"
        if lexi.flags.engagedmike:
            lexi.say "Hell yeah!"
        "I can't help smiling as the girls step forwards."
        "We form a tight little knot together, hugging and holding each other."
        "But then I catch a glimpse of the ones that said no."
        "They look suddenly isolated and cast out."
        "And I feel a pang of anxiety in the pit of my stomach."
        "Because I have no idea just what this means for them..."
    return

label bree_minami_samantha_sasha_propose_male:
    "I know that I keep going on about how unbelievably amazing it is to be involved with my housemates."
    "But that's just something that you're going to gave to get used to hearing from me on the subject."
    "Maybe sometime in the future I'll have gotten used to the idea and it won't seem like such a big deal."
    "And then again, maybe I'll never stop waking up and thinking that I'm the luckiest guy in the world!"
    "Either way, everything seems to be going well for us right now."
    "Everyone's getting along fine and we're having a hell of a lot of fun together too."
    "So you're probably thinking that I'm just going to go along with things as they are."
    "I mean, why would I want to mess with success?"
    "Well, maybe I want to make the arrangement a little more, shall we say, permanent?"
    "That's right - I'm going to ask the girls to marry me."
    "It makes sense to me, formalising our relationship and making a commitment to each other."
    "And I'm gambling on the notion that the girls will feel the same way too."
    show minami tehe at mostleft4
    show bree evil at left4
    show sasha annoyed at right4
    show samantha happy at mostright4
    with dissolve
    "So as soon as we're all together and the perfect moment arises, I pop the question."
    mike.say "Ah, guys..."
    mike.say "There's something I wanted to ask you..."
    show minami normal
    show bree normal
    show sasha normal
    show samantha normal
    "Suddenly their heads turn in unison."
    "And all eyes are on me!"
    "Shit, I thought this was going to be much easier."
    "I feel like they're gazing into my soul!"
    mike.say "I guess I should do this the right way!"
    "I drop onto one knee, right in front of the girls."
    "This causes a flood of mixed reactions from them."
    "One moment they look confused, the next amazed."
    "Maybe this is how it's supposed to be?"
    mike.say "Will..."
    show minami surprised
    show bree surprised
    show sasha surprised
    show samantha surprised
    mike.say "Will you marry me?"
    mike.say "Will all of you marry me?"
    mike.say "And, I guess, each other too?"
    "It doesn't take long for me to get an answer..."
    if bree.love < 195:
        show bree annoyed
        bree.say "[hero.name], you can't be serious?!?"
        bree.say "How would that even work?"
        $ bree.sub -= 25
        $ bree.love -= 25
    else:
        bree.say "[hero.name], are you serious?!?"
        show bree happy
        bree.say "Of course I will!"
        $ bree.set_fiance()
    if sasha.love < 195:
        show sasha annoyed
        sasha.say "Are you out of your mind?!?"
        sasha.say "I didn't get into this thing to get married!"
        $ sasha.sub -= 25
        $ sasha.love -= 25
    else:
        sasha.say "Wow - that came out of the blue!"
        show sasha happy
        sasha.say "But yeah, I will!"
        $ sasha.set_fiance()
    if minami.love < 195:
        show minami annoyed
        minami.say "Big bro, have you gone crazy?"
        minami.say "I can't get married to everyone!"
        $ minami.sub -= 25
        $ minami.love -= 25
    else:
        minami.say "Big bro, you're the best!"
        show minami happy
        minami.say "I will...I will...I will!"
        $ minami.set_fiance()
    if samantha.love < 195:
        show samantha annoyed
        samantha.say "Wow, [hero.name], I already got burnt once."
        samantha.say "And that was with only one spouse!"
        samantha.say "Count me out."
        $ samantha.sub -= 25
        $ samantha.love -= 25
    else:
        samantha.say "Well, I got burned the first time."
        samantha.say "But that was then and this is now."
        show samantha happy
        samantha.say "So yeah, I will!"
        $ samantha.set_fiance()
    "Answering the question must have been a mind-blowing experience for the girls."
    "Because listening to what they had to say certainly was for me."
    "In fact, it takes me a moment to actually wrap my head around what they said."
    if all([g.flags.engagedmike for g in [bree, sasha, minami, samantha]]):
        mike.say "Y...you all said yes?"
        mike.say "All of you really want to marry me?!?"
        "My second question is met with more amusement and irritation."
        "The girls shake their heads and roll their eyes at me."
        bree.say "Oh, [hero.name]!"
        sasha.say "Seriously, are you deaf or something?"
        minami.say "Big bro!"
        samantha.say "That's so you, [hero.name], that's so you!"
        mike.say "So you did?"
        mike.say "You did say yes?"
        "I get a round of nods and smiles this time."
        "Which is probably for the best."
        "As I don't think I could manage to string together a sentence."
        "I'm too excited right now to do anything of the kind!"
    elif not any([g.flags.engagedmike for g in [bree, sasha, minami, samantha]]):
        "I feel like I've been punched in the gut."
        "And like it was done with serious intent too!"
        "Did I just go from being the luckiest guy in the world to the suckiest?"
        "I can't believe ALL of them said no!"
        mike.say "Y...you all said no..."
        mike.say "None of you want to get married?!?"
        "The girls are exchanging glances again."
        "But this time they look more than a little guilty."
        "Maybe I should at least take that as some small comfort!"
        bree.say "I'm sorry, [hero.name] - I just can't."
        sasha.say "I'm not the marrying type, [hero.name]!"
        minami.say "I'm too young to get married, big bro!"
        samantha.say "I don't want to make the same mistake again."
        "All I can do is nod and put on a brave face."
        "But all the same, I think they see how weak my smile is right now."
        "The girls gather round me, trying to offer reassurance."
        "Of course, this doesn't mean that our relationship is over."
        "Though it does make me wonder just how long-term it may prove to be..."
    else:
        "I find myself looking this way and that."
        "Some of the girls look elated at the prospect of marriage."
        "But the others look far more surprised, even worried."
        mike.say "So..."
        mike.say "Some of you don't want to marry me."
        mike.say "And some of you do..."
        "All of a sudden the girls who said yes step forwards."
        "Maybe they're trying to offer me support."
        "Or perhaps they want to separate themselves from the girls that said no."
        if bree.flags.engagedmike:
            bree.say "I do, [hero.name]."
        if sasha.flags.engagedmike:
            sasha.say "I want to marry you!"
        if minami.flags.engagedmike:
            minami.say "Count me in, big bro!"
        if samantha.flags.engagedmike:
            samantha.say "It's a yes from me."
        "I can't help smiling as the girls step forwards."
        "We form a tight little knot together, hugging and holding each other."
        "But then I catch a glimpse of the ones that said no."
        "They look suddenly isolated and cast out."
        "And I feel a pang of anxiety in the pit of my stomach."
        "Because I have no idea just what this means for them..."
    return

label lexi_minami_samantha_propose_male:
    "I know that I keep going on about how unbelievably amazing it is to be involved with my housemates."
    "But that's just something that you're going to gave to get used to hearing from me on the subject."
    "Maybe sometime in the future I'll have gotten used to the idea and it won't seem like such a big deal."
    "And then again, maybe I'll never stop waking up and thinking that I'm the luckiest guy in the world!"
    "Either way, everything seems to be going well for us right now."
    "Everyone's getting along fine and we're having a hell of a lot of fun together too."
    "So you're probably thinking that I'm just going to go along with things as they are."
    "I mean, why would I want to mess with success?"
    "Well, maybe I want to make the arrangement a little more, shall we say, permanent?"
    "That's right - I'm going to ask the girls to marry me."
    "It makes sense to me, formalising our relationship and making a commitment to each other."
    "And I'm gambling on the notion that the girls will feel the same way too."
    "So as soon as we're all together and the perfect moment arises, I pop the question."
    show minami tehe at left
    show lexi bubblegum
    show samantha happy at right
    with dissolve
    mike.say "Ah, guys..."
    mike.say "There's something I wanted to ask you..."
    show minami normal
    show lexi normal
    show samantha normal
    "Suddenly their heads turn in unison."
    "And all eyes are on me!"
    "Shit, I thought this was going to be much easier."
    "I feel like they're gazing into my soul!"
    mike.say "I guess I should do this the right way!"
    "I drop onto one knee, right in front of the girls."
    "This causes a flood of mixed reactions from them."
    "One moment they look confused, the next amazed."
    "Maybe this is how it's supposed to be?"
    mike.say "Will..."
    show minami surprised
    show lexi surprised
    show samantha surprised
    mike.say "Will you marry me?"
    mike.say "Will all of you marry me?"
    mike.say "And, I guess, each other too?"
    "It doesn't take long for me to get an answer..."
    if lexi.love < 195:
        show lexi annoyed
        lexi.say "You can't marry all of us."
        lexi.say "That's too wild, even for me!"
        $ lexi.sub -= 25
        $ lexi.love -= 25
    else:
        lexi.say "All of us get married?!?"
        show lexi happy
        lexi.say "That's wild - I'm in!"
        $ lexi.set_fiance()
    if minami.love < 195:
        show minami annoyed
        minami.say "Big bro, have you gone crazy?"
        minami.say "I can't get married to everyone!"
        $ minami.sub -= 25
        $ minami.love -= 25
    else:
        minami.say "Big bro, you're the best!"
        show minami happy
        minami.say "I will...I will...I will!"
        $ minami.set_fiance()
    if samantha.love < 195:
        show samantha annoyed
        samantha.say "Wow, [hero.name], I already got burnt once."
        samantha.say "And that was with only one spouse!"
        samantha.say "Count me out."
        $ samantha.sub -= 25
        $ samantha.love -= 25
    else:
        samantha.say "Well, I got burned the first time."
        samantha.say "But that was then and this is now."
        show samantha happy
        samantha.say "So yeah, I will!"
        $ samantha.set_fiance()
    "Answering the question must have been a mind-blowing experience for the girls."
    "Because listening to what they had to say certainly was for me."
    "In fact, it takes me a moment to actually wrap my head around what they said."
    if all([g.flags.engagedmike for g in [minami, samantha, lexi]]):
        mike.say "Y...you all said yes?"
        mike.say "All of you really want to marry me?!?"
        "My second question is met with more amusement and irritation."
        "The girls shake their heads and roll their eyes at me."
        minami.say "Big bro!"
        samantha.say "That's so you, [hero.name], that's so you!"
        lexi.say "Geez, you need to clean out your ears!"
        mike.say "So you did?"
        mike.say "You did say yes?"
        "I get a round of nods and smiles this time."
        "Which is probably for the best."
        "As I don't think I could manage to string together a sentence."
        "I'm too excited right now to do anything of the kind!"
    elif not any([g.flags.engagedmike for g in [minami, samantha, lexi]]):
        "I feel like I've been punched in the gut."
        "And like it was done with serious intent too!"
        "Did I just go from being the luckiest guy in the world to the suckiest?"
        "I can't believe ALL of them said no!"
        mike.say "Y...you all said no..."
        mike.say "None of you want to get married?!?"
        "The girls are exchanging glances again."
        "But this time they look more than a little guilty."
        "Maybe I should at least take that as some small comfort!"
        minami.say "I'm too young to get married, big bro!"
        samantha.say "I don't want to make the same mistake again."
        lexi.say "Me get married - are you serious?"
        "All I can do is nod and put on a brave face."
        "But all the same, I think they see how weak my smile is right now."
        "The girls gather round me, trying to offer reassurance."
        "Of course, this doesn't mean that our relationship is over."
        "Though it does make me wonder just how long-term it may prove to be..."
    else:
        "I find myself looking this way and that."
        "Some of the girls look elated at the prospect of marriage."
        "But the others look far more surprised, even worried."
        mike.say "So..."
        mike.say "Some of you don't want to marry me."
        mike.say "And some of you do..."
        "All of a sudden the girls who said yes step forwards."
        "Maybe they're trying to offer me support."
        "Or perhaps they want to separate themselves from the girls that said no."
        if minami.flags.engagedmike:
            minami.say "Count me in, big bro!"
        if samantha.flags.engagedmike:
            samantha.say "It's a yes from me."
        if lexi.flags.engagedmike:
            lexi.say "Hell yeah!"
        "I can't help smiling as the girls step forwards."
        "We form a tight little knot together, hugging and holding each other."
        "But then I catch a glimpse of the ones that said no."
        "They look suddenly isolated and cast out."
        "And I feel a pang of anxiety in the pit of my stomach."
        "Because I have no idea just what this means for them..."
    return

label bree_lexi_samantha_propose_male:
    "I know that I keep going on about how unbelievably amazing it is to be involved with my housemates."
    "But that's just something that you're going to gave to get used to hearing from me on the subject."
    "Maybe sometime in the future I'll have gotten used to the idea and it won't seem like such a big deal."
    "And then again, maybe I'll never stop waking up and thinking that I'm the luckiest guy in the world!"
    "Either way, everything seems to be going well for us right now."
    "Everyone's getting along fine and we're having a hell of a lot of fun together too."
    "So you're probably thinking that I'm just going to go along with things as they are."
    "I mean, why would I want to mess with success?"
    "Well, maybe I want to make the arrangement a little more, shall we say, permanent?"
    "That's right - I'm going to ask the girls to marry me."
    "It makes sense to me, formalising our relationship and making a commitment to each other."
    "And I'm gambling on the notion that the girls will feel the same way too."
    show bree evil at left
    show lexi bubblegum
    show samantha happy at right
    with dissolve
    "So as soon as we're all together and the perfect moment arises, I pop the question."
    mike.say "Ah, guys..."
    mike.say "There's something I wanted to ask you..."
    show bree normal
    show lexi normal
    show samantha normal
    "Suddenly their heads turn in unison."
    "And all eyes are on me!"
    "Shit, I thought this was going to be much easier."
    "I feel like they're gazing into my soul!"
    mike.say "I guess I should do this the right way!"
    "I drop onto one knee, right in front of the girls."
    "This causes a flood of mixed reactions from them."
    "One moment they look confused, the next amazed."
    "Maybe this is how it's supposed to be?"
    mike.say "Will..."
    show bree surprised
    show lexi surprised
    show samantha surprised
    mike.say "Will you marry me?"
    mike.say "Will all of you marry me?"
    mike.say "And, I guess, each other too?"
    "It doesn't take long for me to get an answer..."
    if bree.love < 195:
        show bree annoyed
        bree.say "[hero.name], you can't be serious?!?"
        bree.say "How would that even work?"
        $ bree.sub -= 25
        $ bree.love -= 25
    else:
        bree.say "[hero.name], are you serious?!?"
        show bree happy
        bree.say "Of course I will!"
        $ bree.set_fiance()
    if samantha.love < 195:
        show samantha annoyed
        samantha.say "Wow, [hero.name], I already got burnt once."
        samantha.say "And that was with only one spouse!"
        samantha.say "Count me out."
        $ samantha.sub -= 25
        $ samantha.love -= 25
    else:
        samantha.say "Well, I got burned the first time."
        samantha.say "But that was then and this is now."
        show samantha happy
        samantha.say "So yeah, I will!"
        $ samantha.set_fiance()
    if lexi.love < 195:
        show lexi annoyed
        lexi.say "You can't marry all of us."
        lexi.say "That's too wild, even for me!"
        $ lexi.sub -= 25
        $ lexi.love -= 25
    else:
        lexi.say "All of us get married?!?"
        show lexi happy
        lexi.say "That's wild - I'm in!"
        $ lexi.set_fiance()
    "Answering the question must have been a mind-blowing experience for the girls."
    "Because listening to what they had to say certainly was for me."
    "In fact, it takes me a moment to actually wrap my head around what they said."
    if all([g.flags.engagedmike for g in [bree, samantha, lexi]]):
        mike.say "Y...you all said yes?"
        mike.say "All of you really want to marry me?!?"
        "My second question is met with more amusement and irritation."
        "The girls shake their heads and roll their eyes at me."
        bree.say "Oh, [hero.name]!"
        samantha.say "That's so you, [hero.name], that's so you!"
        lexi.say "Geez, you need to clean out your ears!"
        mike.say "So you did?"
        mike.say "You did say yes?"
        "I get a round of nods and smiles this time."
        "Which is probably for the best."
        "As I don't think I could manage to string together a sentence."
        "I'm too excited right now to do anything of the kind!"
    elif not any([g.flags.engagedmike for g in [bree, samantha, lexi]]):
        "I feel like I've been punched in the gut."
        "And like it was done with serious intent too!"
        "Did I just go from being the luckiest guy in the world to the suckiest?"
        "I can't believe ALL of them said no!"
        mike.say "Y...you all said no..."
        mike.say "None of you want to get married?!?"
        "The girls are exchanging glances again."
        "But this time they look more than a little guilty."
        "Maybe I should at least take that as some small comfort!"
        bree.say "I'm sorry, [hero.name] - I just can't."
        samantha.say "I don't want to make the same mistake again."
        lexi.say "Me get married - are you serious?"
        "All I can do is nod and put on a brave face."
        "But all the same, I think they see how weak my smile is right now."
        "The girls gather round me, trying to offer reassurance."
        "Of course, this doesn't mean that our relationship is over."
        "Though it does make me wonder just how long-term it may prove to be..."
    else:
        "I find myself looking this way and that."
        "Some of the girls look elated at the prospect of marriage."
        "But the others look far more surprised, even worried."
        mike.say "So..."
        mike.say "Some of you don't want to marry me."
        mike.say "And some of you do..."
        "All of a sudden the girls who said yes step forwards."
        "Maybe they're trying to offer me support."
        "Or perhaps they want to separate themselves from the girls that said no."
        if bree.flags.engagedmike:
            bree.say "I do, [hero.name]."
        if samantha.flags.engagedmike:
            samantha.say "It's a yes from me."
        if lexi.flags.engagedmike:
            lexi.say "Hell yeah!"
        "I can't help smiling as the girls step forwards."
        "We form a tight little knot together, hugging and holding each other."
        "But then I catch a glimpse of the ones that said no."
        "They look suddenly isolated and cast out."
        "And I feel a pang of anxiety in the pit of my stomach."
        "Because I have no idea just what this means for them..."
    return

label lexi_samantha_sasha_propose_male:
    "I know that I keep going on about how unbelievably amazing it is to be involved with my housemates."
    "But that's just something that you're going to gave to get used to hearing from me on the subject."
    "Maybe sometime in the future I'll have gotten used to the idea and it won't seem like such a big deal."
    "And then again, maybe I'll never stop waking up and thinking that I'm the luckiest guy in the world!"
    "Either way, everything seems to be going well for us right now."
    "Everyone's getting along fine and we're having a hell of a lot of fun together too."
    "So you're probably thinking that I'm just going to go along with things as they are."
    "I mean, why would I want to mess with success?"
    "Well, maybe I want to make the arrangement a little more, shall we say, permanent?"
    "That's right - I'm going to ask the girls to marry me."
    "It makes sense to me, formalising our relationship and making a commitment to each other."
    "And I'm gambling on the notion that the girls will feel the same way too."
    show sasha annoyed
    show lexi bubblegum at right
    show samantha happy at left
    with dissolve
    "So as soon as we're all together and the perfect moment arises, I pop the question."
    mike.say "Ah, guys..."
    mike.say "There's something I wanted to ask you..."
    show sasha normal
    show lexi normal
    show samantha normal
    "Suddenly their heads turn in unison."
    "And all eyes are on me!"
    "Shit, I thought this was going to be much easier."
    "I feel like they're gazing into my soul!"
    mike.say "I guess I should do this the right way!"
    "I drop onto one knee, right in front of the girls."
    "This causes a flood of mixed reactions from them."
    "One moment they look confused, the next amazed."
    "Maybe this is how it's supposed to be?"
    mike.say "Will..."
    show sasha surprised
    show lexi surprised
    show samantha surprised
    mike.say "Will you marry me?"
    mike.say "Will all of you marry me?"
    mike.say "And, I guess, each other too?"
    "It doesn't take long for me to get an answer..."

    if sasha.love < 195:
        show sasha annoyed
        sasha.say "Are you out of your mind?!?"
        sasha.say "I didn't get into this thing to get married!"
        $ sasha.sub -= 25
        $ sasha.love -= 25
    else:
        sasha.say "Wow - that came out of the blue!"
        show sasha happy
        sasha.say "But yeah, I will!"
        $ sasha.set_fiance()

    if samantha.love < 195:
        show samantha annoyed
        samantha.say "Wow, [hero.name], I already got burnt once."
        samantha.say "And that was with only one spouse!"
        samantha.say "Count me out."
        $ samantha.sub -= 25
        $ samantha.love -= 25
    else:
        samantha.say "Well, I got burned the first time."
        samantha.say "But that was then and this is now."
        show samantha happy
        samantha.say "So yeah, I will!"
        $ samantha.set_fiance()
    if lexi.love < 195:
        show lexi annoyed
        lexi.say "You can't marry all of us."
        lexi.say "That's too wild, even for me!"
        $ lexi.sub -= 25
        $ lexi.love -= 25
    else:
        lexi.say "All of us get married?!?"
        show lexi happy
        lexi.say "That's wild - I'm in!"
        $ lexi.set_fiance()
    "Answering the question must have been a mind-blowing experience for the girls."
    "Because listening to what they had to say certainly was for me."
    "In fact, it takes me a moment to actually wrap my head around what they said."
    if all([g.flags.engagedmike for g in [sasha, samantha, lexi]]):
        mike.say "Y...you all said yes?"
        mike.say "All of you really want to marry me?!?"
        "My second question is met with more amusement and irritation."
        "The girls shake their heads and roll their eyes at me."
        sasha.say "Seriously, are you deaf or something?"
        samantha.say "That's so you, [hero.name], that's so you!"
        lexi.say "Geez, you need to clean out your ears!"
        mike.say "So you did?"
        mike.say "You did say yes?"
        "I get a round of nods and smiles this time."
        "Which is probably for the best."
        "As I don't think I could manage to string together a sentence."
        "I'm too excited right now to do anything of the kind!"
    elif not any([g.flags.engagedmike for g in [sasha, samantha, lexi]]):
        "I feel like I've been punched in the gut."
        "And like it was done with serious intent too!"
        "Did I just go from being the luckiest guy in the world to the suckiest?"
        "I can't believe ALL of them said no!"
        mike.say "Y...you all said no..."
        mike.say "None of you want to get married?!?"
        "The girls are exchanging glances again."
        "But this time they look more than a little guilty."
        "Maybe I should at least take that as some small comfort!"
        sasha.say "I'm not the marrying type, [hero.name]!"
        samantha.say "I don't want to make the same mistake again."
        lexi.say "Me get married - are you serious?"
        "All I can do is nod and put on a brave face."
        "But all the same, I think they see how weak my smile is right now."
        "The girls gather round me, trying to offer reassurance."
        "Of course, this doesn't mean that our relationship is over."
        "Though it does make me wonder just how long-term it may prove to be..."
    else:
        "I find myself looking this way and that."
        "Some of the girls look elated at the prospect of marriage."
        "But the others look far more surprised, even worried."
        mike.say "So..."
        mike.say "Some of you don't want to marry me."
        mike.say "And some of you do..."
        "All of a sudden the girls who said yes step forwards."
        "Maybe they're trying to offer me support."
        "Or perhaps they want to separate themselves from the girls that said no."
        if sasha.flags.engagedmike:
            sasha.say "I want to marry you!"
        if samantha.flags.engagedmike:
            samantha.say "It's a yes from me."
        if lexi.flags.engagedmike:
            lexi.say "Hell yeah!"
        "I can't help smiling as the girls step forwards."
        "We form a tight little knot together, hugging and holding each other."
        "But then I catch a glimpse of the ones that said no."
        "They look suddenly isolated and cast out."
        "And I feel a pang of anxiety in the pit of my stomach."
        "Because I have no idea just what this means for them..."
    return

label bree_lexi_minami_propose_male:
    "I know that I keep going on about how unbelievably amazing it is to be involved with my housemates."
    "But that's just something that you're going to gave to get used to hearing from me on the subject."
    "Maybe sometime in the future I'll have gotten used to the idea and it won't seem like such a big deal."
    "And then again, maybe I'll never stop waking up and thinking that I'm the luckiest guy in the world!"
    "Either way, everything seems to be going well for us right now."
    "Everyone's getting along fine and we're having a hell of a lot of fun together too."
    "So you're probably thinking that I'm just going to go along with things as they are."
    "I mean, why would I want to mess with success?"
    "Well, maybe I want to make the arrangement a little more, shall we say, permanent?"
    "That's right - I'm going to ask the girls to marry me."
    "It makes sense to me, formalising our relationship and making a commitment to each other."
    "And I'm gambling on the notion that the girls will feel the same way too."
    show minami tehe at left
    show bree evil
    show lexi bubblegum at right
    with dissolve
    "So as soon as we're all together and the perfect moment arises, I pop the question."
    mike.say "Ah, guys..."
    mike.say "There's something I wanted to ask you..."
    show minami normal
    show bree normal
    show lexi normal
    "Suddenly their heads turn in unison."
    "And all eyes are on me!"
    "Shit, I thought this was going to be much easier."
    "I feel like they're gazing into my soul!"
    mike.say "I guess I should do this the right way!"
    "I drop onto one knee, right in front of the girls."
    "This causes a flood of mixed reactions from them."
    "One moment they look confused, the next amazed."
    "Maybe this is how it's supposed to be?"
    mike.say "Will..."
    show minami surprised
    show bree surprised
    show lexi surprised
    mike.say "Will you marry me?"
    mike.say "Will all of you marry me?"
    mike.say "And, I guess, each other too?"
    "It doesn't take long for me to get an answer..."
    if bree.love < 195:
        show bree annoyed
        bree.say "[hero.name], you can't be serious?!?"
        bree.say "How would that even work?"
        $ bree.sub -= 25
        $ bree.love -= 25
    else:
        bree.say "[hero.name], are you serious?!?"
        show bree happy
        bree.say "Of course I will!"
        $ bree.set_fiance()
    if minami.love < 195:
        show minami annoyed
        minami.say "Big bro, have you gone crazy?"
        minami.say "I can't get married to everyone!"
        $ minami.sub -= 25
        $ minami.love -= 25
    else:
        minami.say "Big bro, you're the best!"
        show minami happy
        minami.say "I will...I will...I will!"
        $ minami.set_fiance()
    if lexi.love < 195:
        show lexi annoyed
        lexi.say "You can't marry all of us."
        lexi.say "That's too wild, even for me!"
        $ lexi.sub -= 25
        $ lexi.love -= 25
    else:
        lexi.say "All of us get married?!?"
        show lexi happy
        lexi.say "That's wild - I'm in!"
        $ lexi.set_fiance()
    "Answering the question must have been a mind-blowing experience for the girls."
    "Because listening to what they had to say certainly was for me."
    "In fact, it takes me a moment to actually wrap my head around what they said."
    if all([g.flags.engagedmike for g in [bree, minami, lexi]]):
        mike.say "Y...you all said yes?"
        mike.say "All of you really want to marry me?!?"
        "My second question is met with more amusement and irritation."
        "The girls shake their heads and roll their eyes at me."
        bree.say "Oh, [hero.name]!"
        minami.say "Big bro!"
        lexi.say "Geez, you need to clean out your ears!"
        mike.say "So you did?"
        mike.say "You did say yes?"
        "I get a round of nods and smiles this time."
        "Which is probably for the best."
        "As I don't think I could manage to string together a sentence."
        "I'm too excited right now to do anything of the kind!"
    elif not any([g.flags.engagedmike for g in [bree, minami, lexi]]):
        "I feel like I've been punched in the gut."
        "And like it was done with serious intent too!"
        "Did I just go from being the luckiest guy in the world to the suckiest?"
        "I can't believe ALL of them said no!"
        mike.say "Y...you all said no..."
        mike.say "None of you want to get married?!?"
        "The girls are exchanging glances again."
        "But this time they look more than a little guilty."
        "Maybe I should at least take that as some small comfort!"
        bree.say "I'm sorry, [hero.name] - I just can't."
        minami.say "I'm too young to get married, big bro!"
        lexi.say "Me get married - are you serious?"
        "All I can do is nod and put on a brave face."
        "But all the same, I think they see how weak my smile is right now."
        "The girls gather round me, trying to offer reassurance."
        "Of course, this doesn't mean that our relationship is over."
        "Though it does make me wonder just how long-term it may prove to be..."
    else:
        "I find myself looking this way and that."
        "Some of the girls look elated at the prospect of marriage."
        "But the others look far more surprised, even worried."
        mike.say "So..."
        mike.say "Some of you don't want to marry me."
        mike.say "And some of you do..."
        "All of a sudden the girls who said yes step forwards."
        "Maybe they're trying to offer me support."
        "Or perhaps they want to separate themselves from the girls that said no."
        if bree.flags.engagedmike:
            bree.say "I do, [hero.name]."
        if minami.flags.engagedmike:
            minami.say "Count me in, big bro!"
        if lexi.flags.engagedmike:
            lexi.say "Hell yeah!"
        "I can't help smiling as the girls step forwards."
        "We form a tight little knot together, hugging and holding each other."
        "But then I catch a glimpse of the ones that said no."
        "They look suddenly isolated and cast out."
        "And I feel a pang of anxiety in the pit of my stomach."
        "Because I have no idea just what this means for them..."
    return

label lexi_minami_sasha_propose_male:
    "I know that I keep going on about how unbelievably amazing it is to be involved with my housemates."
    "But that's just something that you're going to gave to get used to hearing from me on the subject."
    "Maybe sometime in the future I'll have gotten used to the idea and it won't seem like such a big deal."
    "And then again, maybe I'll never stop waking up and thinking that I'm the luckiest guy in the world!"
    "Either way, everything seems to be going well for us right now."
    "Everyone's getting along fine and we're having a hell of a lot of fun together too."
    "So you're probably thinking that I'm just going to go along with things as they are."
    "I mean, why would I want to mess with success?"
    "Well, maybe I want to make the arrangement a little more, shall we say, permanent?"
    "That's right - I'm going to ask the girls to marry me."
    "It makes sense to me, formalising our relationship and making a commitment to each other."
    "And I'm gambling on the notion that the girls will feel the same way too."
    show minami tehe at left
    show sasha annoyed
    show lexi bubblegum at right
    with dissolve
    "So as soon as we're all together and the perfect moment arises, I pop the question."
    mike.say "Ah, guys..."
    mike.say "There's something I wanted to ask you..."
    show minami normal
    show sasha normal
    show lexi normal
    "Suddenly their heads turn in unison."
    "And all eyes are on me!"
    "Shit, I thought this was going to be much easier."
    "I feel like they're gazing into my soul!"
    mike.say "I guess I should do this the right way!"
    "I drop onto one knee, right in front of the girls."
    "This causes a flood of mixed reactions from them."
    "One moment they look confused, the next amazed."
    "Maybe this is how it's supposed to be?"
    mike.say "Will..."
    show minami surprised
    show sasha surprised
    show lexi surprised
    mike.say "Will you marry me?"
    mike.say "Will all of you marry me?"
    mike.say "And, I guess, each other too?"
    "It doesn't take long for me to get an answer..."

    if sasha.love < 195:
        show sasha annoyed
        sasha.say "Are you out of your mind?!?"
        sasha.say "I didn't get into this thing to get married!"
        $ sasha.sub -= 25
        $ sasha.love -= 25
    else:
        sasha.say "Wow - that came out of the blue!"
        show sasha happy
        sasha.say "But yeah, I will!"
        $ sasha.set_fiance()
    if minami.love < 195:
        show minami annoyed
        minami.say "Big bro, have you gone crazy?"
        minami.say "I can't get married to everyone!"
        $ minami.sub -= 25
        $ minami.love -= 25
    else:
        minami.say "Big bro, you're the best!"
        show minami happy
        minami.say "I will...I will...I will!"
        $ minami.set_fiance()
    if lexi.love < 195:
        show lexi annoyed
        lexi.say "You can't marry all of us."
        lexi.say "That's too wild, even for me!"
        $ lexi.sub -= 25
        $ lexi.love -= 25
    else:
        lexi.say "All of us get married?!?"
        show lexi happy
        lexi.say "That's wild - I'm in!"
        $ lexi.set_fiance()
    "Answering the question must have been a mind-blowing experience for the girls."
    "Because listening to what they had to say certainly was for me."
    "In fact, it takes me a moment to actually wrap my head around what they said."
    if all([g.flags.engagedmike for g in [sasha, minami, lexi]]):
        mike.say "Y...you all said yes?"
        mike.say "All of you really want to marry me?!?"
        "My second question is met with more amusement and irritation."
        "The girls shake their heads and roll their eyes at me."
        sasha.say "Seriously, are you deaf or something?"
        minami.say "Big bro!"
        lexi.say "Geez, you need to clean out your ears!"
        mike.say "So you did?"
        mike.say "You did say yes?"
        "I get a round of nods and smiles this time."
        "Which is probably for the best."
        "As I don't think I could manage to string together a sentence."
        "I'm too excited right now to do anything of the kind!"
    elif not any([g.flags.engagedmike for g in [sasha, minami, lexi]]):
        "I feel like I've been punched in the gut."
        "And like it was done with serious intent too!"
        "Did I just go from being the luckiest guy in the world to the suckiest?"
        "I can't believe ALL of them said no!"
        mike.say "Y...you all said no..."
        mike.say "None of you want to get married?!?"
        "The girls are exchanging glances again."
        "But this time they look more than a little guilty."
        "Maybe I should at least take that as some small comfort!"

        sasha.say "I'm not the marrying type, [hero.name]!"
        minami.say "I'm too young to get married, big bro!"
        lexi.say "Me get married - are you serious?"
        "All I can do is nod and put on a brave face."
        "But all the same, I think they see how weak my smile is right now."
        "The girls gather round me, trying to offer reassurance."
        "Of course, this doesn't mean that our relationship is over."
        "Though it does make me wonder just how long-term it may prove to be..."
    else:
        "I find myself looking this way and that."
        "Some of the girls look elated at the prospect of marriage."
        "But the others look far more surprised, even worried."
        mike.say "So..."
        mike.say "Some of you don't want to marry me."
        mike.say "And some of you do..."
        "All of a sudden the girls who said yes step forwards."
        "Maybe they're trying to offer me support."
        "Or perhaps they want to separate themselves from the girls that said no."
        if sasha.flags.engagedmike:
            sasha.say "I want to marry you!"
        if minami.flags.engagedmike:
            minami.say "Count me in, big bro!"
        if lexi.flags.engagedmike:
            lexi.say "Hell yeah!"
        "I can't help smiling as the girls step forwards."
        "We form a tight little knot together, hugging and holding each other."
        "But then I catch a glimpse of the ones that said no."
        "They look suddenly isolated and cast out."
        "And I feel a pang of anxiety in the pit of my stomach."
        "Because I have no idea just what this means for them..."
    return

label bree_lexi_sasha_propose_male:
    "I know that I keep going on about how unbelievably amazing it is to be involved with my housemates."
    "But that's just something that you're going to gave to get used to hearing from me on the subject."
    "Maybe sometime in the future I'll have gotten used to the idea and it won't seem like such a big deal."
    "And then again, maybe I'll never stop waking up and thinking that I'm the luckiest guy in the world!"
    "Either way, everything seems to be going well for us right now."
    "Everyone's getting along fine and we're having a hell of a lot of fun together too."
    "So you're probably thinking that I'm just going to go along with things as they are."
    "I mean, why would I want to mess with success?"
    "Well, maybe I want to make the arrangement a little more, shall we say, permanent?"
    "That's right - I'm going to ask the girls to marry me."
    "It makes sense to me, formalising our relationship and making a commitment to each other."
    "And I'm gambling on the notion that the girls will feel the same way too."
    show bree evil at left
    show sasha annoyed
    show lexi bubblegum at right
    with dissolve
    "So as soon as we're all together and the perfect moment arises, I pop the question."
    mike.say "Ah, guys..."
    mike.say "There's something I wanted to ask you..."
    show bree normal
    show sasha normal
    show lexi normal
    "Suddenly their heads turn in unison."
    "And all eyes are on me!"
    "Shit, I thought this was going to be much easier."
    "I feel like they're gazing into my soul!"
    mike.say "I guess I should do this the right way!"
    "I drop onto one knee, right in front of the girls."
    "This causes a flood of mixed reactions from them."
    "One moment they look confused, the next amazed."
    "Maybe this is how it's supposed to be?"
    mike.say "Will..."
    show bree surprised
    show sasha surprised
    show lexi surprised
    mike.say "Will you marry me?"
    mike.say "Will all of you marry me?"
    mike.say "And, I guess, each other too?"
    "It doesn't take long for me to get an answer..."
    if bree.love < 195:
        show bree annoyed
        bree.say "[hero.name], you can't be serious?!?"
        bree.say "How would that even work?"
        $ bree.sub -= 25
        $ bree.love -= 25
    else:
        bree.say "[hero.name], are you serious?!?"
        show bree happy
        bree.say "Of course I will!"
        $ bree.set_fiance()
    if sasha.love < 195:
        show sasha annoyed
        sasha.say "Are you out of your mind?!?"
        sasha.say "I didn't get into this thing to get married!"
        $ sasha.sub -= 25
        $ sasha.love -= 25
    else:
        sasha.say "Wow - that came out of the blue!"
        show sasha happy
        sasha.say "But yeah, I will!"
        $ sasha.set_fiance()
    if lexi.love < 195:
        show lexi annoyed
        lexi.say "You can't marry all of us."
        lexi.say "That's too wild, even for me!"
        $ lexi.sub -= 25
        $ lexi.love -= 25
    else:
        lexi.say "All of us get married?!?"
        show lexi happy
        lexi.say "That's wild - I'm in!"
        $ lexi.set_fiance()
    "Answering the question must have been a mind-blowing experience for the girls."
    "Because listening to what they had to say certainly was for me."
    "In fact, it takes me a moment to actually wrap my head around what they said."
    if all([g.flags.engagedmike for g in [bree, sasha, lexi]]):
        mike.say "Y...you all said yes?"
        mike.say "All of you really want to marry me?!?"
        "My second question is met with more amusement and irritation."
        "The girls shake their heads and roll their eyes at me."
        bree.say "Oh, [hero.name]!"
        sasha.say "Seriously, are you deaf or something?"
        lexi.say "Geez, you need to clean out your ears!"
        mike.say "So you did?"
        mike.say "You did say yes?"
        "I get a round of nods and smiles this time."
        "Which is probably for the best."
        "As I don't think I could manage to string together a sentence."
        "I'm too excited right now to do anything of the kind!"
    elif not any([g.flags.engagedmike for g in [bree, sasha, lexi]]):
        "I feel like I've been punched in the gut."
        "And like it was done with serious intent too!"
        "Did I just go from being the luckiest guy in the world to the suckiest?"
        "I can't believe ALL of them said no!"
        mike.say "Y...you all said no..."
        mike.say "None of you want to get married?!?"
        "The girls are exchanging glances again."
        "But this time they look more than a little guilty."
        "Maybe I should at least take that as some small comfort!"
        bree.say "I'm sorry, [hero.name] - I just can't."
        sasha.say "I'm not the marrying type, [hero.name]!"

        lexi.say "Me get married - are you serious?"
        "All I can do is nod and put on a brave face."
        "But all the same, I think they see how weak my smile is right now."
        "The girls gather round me, trying to offer reassurance."
        "Of course, this doesn't mean that our relationship is over."
        "Though it does make me wonder just how long-term it may prove to be..."
    else:
        "I find myself looking this way and that."
        "Some of the girls look elated at the prospect of marriage."
        "But the others look far more surprised, even worried."
        mike.say "So..."
        mike.say "Some of you don't want to marry me."
        mike.say "And some of you do..."
        "All of a sudden the girls who said yes step forwards."
        "Maybe they're trying to offer me support."
        "Or perhaps they want to separate themselves from the girls that said no."
        if bree.flags.engagedmike:
            bree.say "I do, [hero.name]."
        if sasha.flags.engagedmike:
            sasha.say "I want to marry you!"
        if lexi.flags.engagedmike:
            lexi.say "Hell yeah!"
        "I can't help smiling as the girls step forwards."
        "We form a tight little knot together, hugging and holding each other."
        "But then I catch a glimpse of the ones that said no."
        "They look suddenly isolated and cast out."
        "And I feel a pang of anxiety in the pit of my stomach."
        "Because I have no idea just what this means for them..."
    return

label bree_minami_samantha_propose_male:
    "I know that I keep going on about how unbelievably amazing it is to be involved with my housemates."
    "But that's just something that you're going to gave to get used to hearing from me on the subject."
    "Maybe sometime in the future I'll have gotten used to the idea and it won't seem like such a big deal."
    "And then again, maybe I'll never stop waking up and thinking that I'm the luckiest guy in the world!"
    "Either way, everything seems to be going well for us right now."
    "Everyone's getting along fine and we're having a hell of a lot of fun together too."
    "So you're probably thinking that I'm just going to go along with things as they are."
    "I mean, why would I want to mess with success?"
    "Well, maybe I want to make the arrangement a little more, shall we say, permanent?"
    "That's right - I'm going to ask the girls to marry me."
    "It makes sense to me, formalising our relationship and making a commitment to each other."
    "And I'm gambling on the notion that the girls will feel the same way too."
    show minami tehe at left
    show bree evil
    show samantha happy at right
    with dissolve
    "So as soon as we're all together and the perfect moment arises, I pop the question."
    mike.say "Ah, guys..."
    mike.say "There's something I wanted to ask you..."
    show minami normal
    show bree normal
    show samantha normal
    "Suddenly their heads turn in unison."
    "And all eyes are on me!"
    "Shit, I thought this was going to be much easier."
    "I feel like they're gazing into my soul!"
    mike.say "I guess I should do this the right way!"
    "I drop onto one knee, right in front of the girls."
    "This causes a flood of mixed reactions from them."
    "One moment they look confused, the next amazed."
    "Maybe this is how it's supposed to be?"
    show minami surprised
    show bree surprised
    show samantha surprised
    mike.say "Will you marry me?"
    mike.say "Will all of you marry me?"
    mike.say "And, I guess, each other too?"
    "It doesn't take long for me to get an answer..."
    if bree.love < 195:
        show bree annoyed
        bree.say "[hero.name], you can't be serious?!?"
        bree.say "How would that even work?"
        $ bree.sub -= 25
        $ bree.love -= 25
    else:
        bree.say "[hero.name], are you serious?!?"
        show bree happy
        bree.say "Of course I will!"
        $ bree.set_fiance()
    if minami.love < 195:
        show minami annoyed
        minami.say "Big bro, have you gone crazy?"
        minami.say "I can't get married to everyone!"
        $ minami.sub -= 25
        $ minami.love -= 25
    else:
        minami.say "Big bro, you're the best!"
        show minami happy
        minami.say "I will...I will...I will!"
        $ minami.set_fiance()
    if samantha.love < 195:
        show samantha annoyed
        samantha.say "Wow, [hero.name], I already got burnt once."
        samantha.say "And that was with only one spouse!"
        samantha.say "Count me out."
        $ samantha.sub -= 25
        $ samantha.love -= 25
    else:
        samantha.say "Well, I got burned the first time."
        samantha.say "But that was then and this is now."
        show samantha happy
        samantha.say "So yeah, I will!"
        $ samantha.set_fiance()
    "Answering the question must have been a mind-blowing experience for the girls."
    "Because listening to what they had to say certainly was for me."
    "In fact, it takes me a moment to actually wrap my head around what they said."
    if all([g.flags.engagedmike for g in [bree, minami, samantha]]):
        mike.say "Y...you all said yes?"
        mike.say "All of you really want to marry me?!?"
        "My second question is met with more amusement and irritation."
        "The girls shake their heads and roll their eyes at me."
        bree.say "Oh, [hero.name]!"
        minami.say "Big bro!"
        samantha.say "That's so you, [hero.name], that's so you!"
        mike.say "So you did?"
        mike.say "You did say yes?"
        "I get a round of nods and smiles this time."
        "Which is probably for the best."
        "As I don't think I could manage to string together a sentence."
        "I'm too excited right now to do anything of the kind!"
    elif not any([g.flags.engagedmike for g in [bree, minami, samantha]]):
        "I feel like I've been punched in the gut."
        "And like it was done with serious intent too!"
        "Did I just go from being the luckiest guy in the world to the suckiest?"
        "I can't believe ALL of them said no!"
        mike.say "Y...you all said no..."
        mike.say "None of you want to get married?!?"
        "The girls are exchanging glances again."
        "But this time they look more than a little guilty."
        "Maybe I should at least take that as some small comfort!"
        bree.say "I'm sorry, [hero.name] - I just can't."
        minami.say "I'm too young to get married, big bro!"
        samantha.say "I don't want to make the same mistake again."
        "All I can do is nod and put on a brave face."
        "But all the same, I think they see how weak my smile is right now."
        "The girls gather round me, trying to offer reassurance."
        "Of course, this doesn't mean that our relationship is over."
        "Though it does make me wonder just how long-term it may prove to be..."
    else:
        "I find myself looking this way and that."
        "Some of the girls look elated at the prospect of marriage."
        "But the others look far more surprised, even worried."
        mike.say "So..."
        mike.say "Some of you don't want to marry me."
        mike.say "And some of you do..."
        "All of a sudden the girls who said yes step forwards."
        "Maybe they're trying to offer me support."
        "Or perhaps they want to separate themselves from the girls that said no."
        if bree.flags.engagedmike:
            bree.say "I do, [hero.name]."
        if minami.flags.engagedmike:
            minami.say "Count me in, big bro!"
        if samantha.flags.engagedmike:
            samantha.say "It's a yes from me."
        "I can't help smiling as the girls step forwards."
        "We form a tight little knot together, hugging and holding each other."
        "But then I catch a glimpse of the ones that said no."
        "They look suddenly isolated and cast out."
        "And I feel a pang of anxiety in the pit of my stomach."
        "Because I have no idea just what this means for them..."
    return

label minami_samantha_sasha_propose_male:
    "I know that I keep going on about how unbelievably amazing it is to be involved with my housemates."
    "But that's just something that you're going to gave to get used to hearing from me on the subject."
    "Maybe sometime in the future I'll have gotten used to the idea and it won't seem like such a big deal."
    "And then again, maybe I'll never stop waking up and thinking that I'm the luckiest guy in the world!"
    "Either way, everything seems to be going well for us right now."
    "Everyone's getting along fine and we're having a hell of a lot of fun together too."
    "So you're probably thinking that I'm just going to go along with things as they are."
    "I mean, why would I want to mess with success?"
    "Well, maybe I want to make the arrangement a little more, shall we say, permanent?"
    "That's right - I'm going to ask the girls to marry me."
    "It makes sense to me, formalising our relationship and making a commitment to each other."
    "And I'm gambling on the notion that the girls will feel the same way too."
    show minami tehe at left
    show sasha annoyed
    show samantha happy at right
    with dissolve
    "So as soon as we're all together and the perfect moment arises, I pop the question."
    mike.say "Ah, guys..."
    mike.say "There's something I wanted to ask you..."
    show minami normal
    show sasha normal
    show samantha normal
    "Suddenly their heads turn in unison."
    "And all eyes are on me!"
    "Shit, I thought this was going to be much easier."
    "I feel like they're gazing into my soul!"
    mike.say "I guess I should do this the right way!"
    "I drop onto one knee, right in front of the girls."
    "This causes a flood of mixed reactions from them."
    "One moment they look confused, the next amazed."
    "Maybe this is how it's supposed to be?"
    mike.say "Will..."
    show minami surprised
    show sasha surprised
    show samantha surprised
    mike.say "Will you marry me?"
    mike.say "Will all of you marry me?"
    mike.say "And, I guess, each other too?"
    "It doesn't take long for me to get an answer..."

    if sasha.love < 195:
        show sasha annoyed
        sasha.say "Are you out of your mind?!?"
        sasha.say "I didn't get into this thing to get married!"
        $ sasha.sub -= 25
        $ sasha.love -= 25
    else:
        sasha.say "Wow - that came out of the blue!"
        show sasha happy
        sasha.say "But yeah, I will!"
        $ sasha.set_fiance()
    if minami.love < 195:
        show minami annoyed
        minami.say "Big bro, have you gone crazy?"
        minami.say "I can't get married to everyone!"
        $ minami.sub -= 25
        $ minami.love -= 25
    else:
        minami.say "Big bro, you're the best!"
        show minami happy
        minami.say "I will...I will...I will!"
        $ minami.set_fiance()
    if samantha.love < 195:
        show samantha annoyed
        samantha.say "Wow, [hero.name], I already got burnt once."
        samantha.say "And that was with only one spouse!"
        samantha.say "Count me out."
        $ samantha.sub -= 25
        $ samantha.love -= 25
    else:
        samantha.say "Well, I got burned the first time."
        samantha.say "But that was then and this is now."
        show samantha happy
        samantha.say "So yeah, I will!"
        $ samantha.set_fiance()
    "Answering the question must have been a mind-blowing experience for the girls."
    "Because listening to what they had to say certainly was for me."
    "In fact, it takes me a moment to actually wrap my head around what they said."
    if all([g.flags.engagedmike for g in [sasha, minami, samantha]]):
        mike.say "Y...you all said yes?"
        mike.say "All of you really want to marry me?!?"
        "My second question is met with more amusement and irritation."
        "The girls shake their heads and roll their eyes at me."
        sasha.say "Seriously, are you deaf or something?"
        minami.say "Big bro!"
        samantha.say "That's so you, [hero.name], that's so you!"
        mike.say "So you did?"
        mike.say "You did say yes?"
        "I get a round of nods and smiles this time."
        "Which is probably for the best."
        "As I don't think I could manage to string together a sentence."
        "I'm too excited right now to do anything of the kind!"
    elif not any([g.flags.engagedmike for g in [sasha, minami, samantha]]):
        "I feel like I've been punched in the gut."
        "And like it was done with serious intent too!"
        "Did I just go from being the luckiest guy in the world to the suckiest?"
        "I can't believe ALL of them said no!"
        mike.say "Y...you all said no..."
        mike.say "None of you want to get married?!?"
        "The girls are exchanging glances again."
        "But this time they look more than a little guilty."
        "Maybe I should at least take that as some small comfort!"
        sasha.say "I'm not the marrying type, [hero.name]!"
        minami.say "I'm too young to get married, big bro!"
        samantha.say "I don't want to make the same mistake again."
        "All I can do is nod and put on a brave face."
        "But all the same, I think they see how weak my smile is right now."
        "The girls gather round me, trying to offer reassurance."
        "Of course, this doesn't mean that our relationship is over."
        "Though it does make me wonder just how long-term it may prove to be..."
    else:
        "I find myself looking this way and that."
        "Some of the girls look elated at the prospect of marriage."
        "But the others look far more surprised, even worried."
        mike.say "So..."
        mike.say "Some of you don't want to marry me."
        mike.say "And some of you do..."
        "All of a sudden the girls who said yes step forwards."
        "Maybe they're trying to offer me support."
        "Or perhaps they want to separate themselves from the girls that said no."
        if sasha.flags.engagedmike:
            sasha.say "I want to marry you!"
        if minami.flags.engagedmike:
            minami.say "Count me in, big bro!"
        if samantha.flags.engagedmike:
            samantha.say "It's a yes from me."
        "I can't help smiling as the girls step forwards."
        "We form a tight little knot together, hugging and holding each other."
        "But then I catch a glimpse of the ones that said no."
        "They look suddenly isolated and cast out."
        "And I feel a pang of anxiety in the pit of my stomach."
        "Because I have no idea just what this means for them..."
    return

label bree_samantha_sasha_propose_male:
    "I know that I keep going on about how unbelievably amazing it is to be involved with my housemates."
    "But that's just something that you're going to gave to get used to hearing from me on the subject."
    "Maybe sometime in the future I'll have gotten used to the idea and it won't seem like such a big deal."
    "And then again, maybe I'll never stop waking up and thinking that I'm the luckiest guy in the world!"
    "Either way, everything seems to be going well for us right now."
    "Everyone's getting along fine and we're having a hell of a lot of fun together too."
    "So you're probably thinking that I'm just going to go along with things as they are."
    "I mean, why would I want to mess with success?"
    "Well, maybe I want to make the arrangement a little more, shall we say, permanent?"
    "That's right - I'm going to ask the girls to marry me."
    "It makes sense to me, formalising our relationship and making a commitment to each other."
    "And I'm gambling on the notion that the girls will feel the same way too."
    show bree evil at left
    show sasha annoyed
    show samantha happy at right
    with dissolve
    "So as soon as we're all together and the perfect moment arises, I pop the question."
    mike.say "Ah, guys..."
    mike.say "There's something I wanted to ask you..."
    show bree normal
    show sasha normal
    show samantha normal
    "Suddenly their heads turn in unison."
    "And all eyes are on me!"
    "Shit, I thought this was going to be much easier."
    "I feel like they're gazing into my soul!"
    mike.say "I guess I should do this the right way!"
    "I drop onto one knee, right in front of the girls."
    "This causes a flood of mixed reactions from them."
    "One moment they look confused, the next amazed."
    "Maybe this is how it's supposed to be?"
    mike.say "Will..."
    show bree surprised
    show sasha surprised
    show samantha surprised
    mike.say "Will you marry me?"
    mike.say "Will all of you marry me?"
    mike.say "And, I guess, each other too?"
    "It doesn't take long for me to get an answer..."
    if bree.love < 195:
        show bree annoyed
        bree.say "[hero.name], you can't be serious?!?"
        bree.say "How would that even work?"
        $ bree.sub -= 25
        $ bree.love -= 25
    else:
        bree.say "[hero.name], are you serious?!?"
        show bree happy
        bree.say "Of course I will!"
        $ bree.set_fiance()
    if sasha.love < 195:
        show sasha annoyed
        sasha.say "Are you out of your mind?!?"
        sasha.say "I didn't get into this thing to get married!"
        $ sasha.sub -= 25
        $ sasha.love -= 25
    else:
        sasha.say "Wow - that came out of the blue!"
        show sasha happy
        sasha.say "But yeah, I will!"
        $ sasha.set_fiance()
    if samantha.love < 195:
        show samantha annoyed
        samantha.say "Wow, [hero.name], I already got burnt once."
        samantha.say "And that was with only one spouse!"
        samantha.say "Count me out."
        $ samantha.sub -= 25
        $ samantha.love -= 25
    else:
        samantha.say "Well, I got burned the first time."
        samantha.say "But that was then and this is now."
        show samantha happy
        samantha.say "So yeah, I will!"
        $ samantha.set_fiance()
    "Answering the question must have been a mind-blowing experience for the girls."
    "Because listening to what they had to say certainly was for me."
    "In fact, it takes me a moment to actually wrap my head around what they said."
    if all([g.flags.engagedmike for g in [bree, sasha, samantha]]):
        mike.say "Y...you all said yes?"
        mike.say "All of you really want to marry me?!?"
        "My second question is met with more amusement and irritation."
        "The girls shake their heads and roll their eyes at me."
        bree.say "Oh, [hero.name]!"
        sasha.say "Seriously, are you deaf or something?"
        samantha.say "That's so you, [hero.name], that's so you!"
        mike.say "So you did?"
        mike.say "You did say yes?"
        "I get a round of nods and smiles this time."
        "Which is probably for the best."
        "As I don't think I could manage to string together a sentence."
        "I'm too excited right now to do anything of the kind!"
    elif not any([g.flags.engagedmike for g in [bree, sasha, samantha]]):
        "I feel like I've been punched in the gut."
        "And like it was done with serious intent too!"
        "Did I just go from being the luckiest guy in the world to the suckiest?"
        "I can't believe ALL of them said no!"
        mike.say "Y...you all said no..."
        mike.say "None of you want to get married?!?"
        "The girls are exchanging glances again."
        "But this time they look more than a little guilty."
        "Maybe I should at least take that as some small comfort!"
        bree.say "I'm sorry, [hero.name] - I just can't."
        sasha.say "I'm not the marrying type, [hero.name]!"
        samantha.say "I don't want to make the same mistake again."
        "All I can do is nod and put on a brave face."
        "But all the same, I think they see how weak my smile is right now."
        "The girls gather round me, trying to offer reassurance."
        "Of course, this doesn't mean that our relationship is over."
        "Though it does make me wonder just how long-term it may prove to be..."
    else:
        "I find myself looking this way and that."
        "Some of the girls look elated at the prospect of marriage."
        "But the others look far more surprised, even worried."
        mike.say "So..."
        mike.say "Some of you don't want to marry me."
        mike.say "And some of you do..."
        "All of a sudden the girls who said yes step forwards."
        "Maybe they're trying to offer me support."
        "Or perhaps they want to separate themselves from the girls that said no."
        if bree.flags.engagedmike:
            bree.say "I do, [hero.name]."
        if sasha.flags.engagedmike:
            sasha.say "I want to marry you!"
        if samantha.flags.engagedmike:
            samantha.say "It's a yes from me."
        "I can't help smiling as the girls step forwards."
        "We form a tight little knot together, hugging and holding each other."
        "But then I catch a glimpse of the ones that said no."
        "They look suddenly isolated and cast out."
        "And I feel a pang of anxiety in the pit of my stomach."
        "Because I have no idea just what this means for them..."
    return

label bree_minami_sasha_propose_male:
    "I know that I keep going on about how unbelievably amazing it is to be involved with my housemates."
    "But that's just something that you're going to gave to get used to hearing from me on the subject."
    "Maybe sometime in the future I'll have gotten used to the idea and it won't seem like such a big deal."
    "And then again, maybe I'll never stop waking up and thinking that I'm the luckiest guy in the world!"
    "Either way, everything seems to be going well for us right now."
    "Everyone's getting along fine and we're having a hell of a lot of fun together too."
    "So you're probably thinking that I'm just going to go along with things as they are."
    "I mean, why would I want to mess with success?"
    "Well, maybe I want to make the arrangement a little more, shall we say, permanent?"
    "That's right - I'm going to ask the girls to marry me."
    "It makes sense to me, formalising our relationship and making a commitment to each other."
    "And I'm gambling on the notion that the girls will feel the same way too."
    show minami tehe at left
    show bree evil
    show sasha annoyed at right
    with dissolve
    "So as soon as we're all together and the perfect moment arises, I pop the question."
    mike.say "Ah, guys..."
    mike.say "There's something I wanted to ask you..."
    show minami normal
    show bree normal
    show sasha normal
    "Suddenly their heads turn in unison."
    "And all eyes are on me!"
    "Shit, I thought this was going to be much easier."
    "I feel like they're gazing into my soul!"
    mike.say "I guess I should do this the right way!"
    "I drop onto one knee, right in front of the girls."
    "This causes a flood of mixed reactions from them."
    "One moment they look confused, the next amazed."
    "Maybe this is how it's supposed to be?"
    mike.say "Will..."
    show minami surprised
    show bree surprised
    show sasha surprised
    mike.say "Will you marry me?"
    mike.say "Will all of you marry me?"
    mike.say "And, I guess, each other too?"
    "It doesn't take long for me to get an answer..."
    if bree.love < 195:
        show bree annoyed
        bree.say "[hero.name], you can't be serious?!?"
        bree.say "How would that even work?"
        $ bree.sub -= 25
        $ bree.love -= 25
    else:
        bree.say "[hero.name], are you serious?!?"
        show bree happy
        bree.say "Of course I will!"
        $ bree.set_fiance()
    if sasha.love < 195:
        show sasha annoyed
        sasha.say "Are you out of your mind?!?"
        sasha.say "I didn't get into this thing to get married!"
        $ sasha.sub -= 25
        $ sasha.love -= 25
    else:
        sasha.say "Wow - that came out of the blue!"
        show sasha happy
        sasha.say "But yeah, I will!"
        $ sasha.set_fiance()
    if minami.love < 195:
        show minami annoyed
        minami.say "Big bro, have you gone crazy?"
        minami.say "I can't get married to everyone!"
        $ minami.sub -= 25
        $ minami.love -= 25
    else:
        minami.say "Big bro, you're the best!"
        show minami happy
        minami.say "I will...I will...I will!"
        $ minami.set_fiance()
    "Answering the question must have been a mind-blowing experience for the girls."
    "Because listening to what they had to say certainly was for me."
    "In fact, it takes me a moment to actually wrap my head around what they said."
    if all([g.flags.engagedmike for g in [bree, sasha, minami]]):
        mike.say "Y...you all said yes?"
        mike.say "All of you really want to marry me?!?"
        "My second question is met with more amusement and irritation."
        "The girls shake their heads and roll their eyes at me."
        bree.say "Oh, [hero.name]!"
        sasha.say "Seriously, are you deaf or something?"
        minami.say "Big bro!"
        mike.say "So you did?"
        mike.say "You did say yes?"
        "I get a round of nods and smiles this time."
        "Which is probably for the best."
        "As I don't think I could manage to string together a sentence."
        "I'm too excited right now to do anything of the kind!"
    elif not any([g.flags.engagedmike for g in [bree, sasha, minami]]):
        "I feel like I've been punched in the gut."
        "And like it was done with serious intent too!"
        "Did I just go from being the luckiest guy in the world to the suckiest?"
        "I can't believe ALL of them said no!"
        mike.say "Y...you all said no..."
        mike.say "None of you want to get married?!?"
        "The girls are exchanging glances again."
        "But this time they look more than a little guilty."
        "Maybe I should at least take that as some small comfort!"
        bree.say "I'm sorry, [hero.name] - I just can't."
        sasha.say "I'm not the marrying type, [hero.name]!"
        minami.say "I'm too young to get married, big bro!"
        "All I can do is nod and put on a brave face."
        "But all the same, I think they see how weak my smile is right now."
        "The girls gather round me, trying to offer reassurance."
        "Of course, this doesn't mean that our relationship is over."
        "Though it does make me wonder just how long-term it may prove to be..."
    else:
        "I find myself looking this way and that."
        "Some of the girls look elated at the prospect of marriage."
        "But the others look far more surprised, even worried."
        mike.say "So..."
        mike.say "Some of you don't want to marry me."
        mike.say "And some of you do..."
        "All of a sudden the girls who said yes step forwards."
        "Maybe they're trying to offer me support."
        "Or perhaps they want to separate themselves from the girls that said no."
        if bree.flags.engagedmike:
            bree.say "I do, [hero.name]."
        if sasha.flags.engagedmike:
            sasha.say "I want to marry you!"
        if minami.flags.engagedmike:
            minami.say "Count me in, big bro!"
        "I can't help smiling as the girls step forwards."
        "We form a tight little knot together, hugging and holding each other."
        "But then I catch a glimpse of the ones that said no."
        "They look suddenly isolated and cast out."
        "And I feel a pang of anxiety in the pit of my stomach."
        "Because I have no idea just what this means for them..."
    return

label lexi_samantha_propose_male:
    "I know that I keep going on about how unbelievably amazing it is to be involved with my housemates."
    "But that's just something that you're going to gave to get used to hearing from me on the subject."
    "Maybe sometime in the future I'll have gotten used to the idea and it won't seem like such a big deal."
    "And then again, maybe I'll never stop waking up and thinking that I'm the luckiest guy in the world!"
    "Either way, everything seems to be going well for us right now."
    "Everyone's getting along fine and we're having a hell of a lot of fun together too."
    "So you're probably thinking that I'm just going to go along with things as they are."
    "I mean, why would I want to mess with success?"
    "Well, maybe I want to make the arrangement a little more, shall we say, permanent?"
    "That's right - I'm going to ask the girls to marry me."
    "It makes sense to me, formalising our relationship and making a commitment to each other."
    "And I'm gambling on the notion that the girls will feel the same way too."
    show lexi bubblegum at right5
    show samantha happy at left5
    with dissolve
    "So as soon as we're all together and the perfect moment arises, I pop the question."
    mike.say "Ah, guys..."
    mike.say "There's something I wanted to ask you..."
    show lexi normal
    show samantha normal
    "Suddenly their heads turn in unison."
    "And all eyes are on me!"
    "Shit, I thought this was going to be much easier."
    "I feel like they're gazing into my soul!"
    mike.say "I guess I should do this the right way!"
    "I drop onto one knee, right in front of the girls."
    "This causes a flood of mixed reactions from them."
    "One moment they look confused, the next amazed."
    "Maybe this is how it's supposed to be?"
    mike.say "Will..."
    show lexi surprised
    show samantha surprised
    mike.say "Will you marry me?"
    mike.say "Will all of you marry me?"
    mike.say "And, I guess, each other too?"
    "It doesn't take long for me to get an answer..."

    if samantha.love < 195:
        show samantha annoyed
        samantha.say "Wow, [hero.name], I already got burnt once."
        samantha.say "And that was with only one spouse!"
        samantha.say "Count me out."
        $ samantha.sub -= 25
        $ samantha.love -= 25
    else:
        samantha.say "Well, I got burned the first time."
        samantha.say "But that was then and this is now."
        show samantha happy
        samantha.say "So yeah, I will!"
        $ samantha.set_fiance()
    if lexi.love < 195:
        show lexi annoyed
        lexi.say "You can't marry all of us."
        lexi.say "That's too wild, even for me!"
        $ lexi.sub -= 25
        $ lexi.love -= 25
    else:
        lexi.say "All of us get married?!?"
        show lexi happy
        lexi.say "That's wild - I'm in!"
        $ lexi.set_fiance()
    "Answering the question must have been a mind-blowing experience for the girls."
    "Because listening to what they had to say certainly was for me."
    "In fact, it takes me a moment to actually wrap my head around what they said."
    if all([g.flags.engagedmike for g in [samantha, lexi]]):
        mike.say "Y...you all said yes?"
        mike.say "All of you really want to marry me?!?"
        "My second question is met with more amusement and irritation."
        "The girls shake their heads and roll their eyes at me."
        samantha.say "That's so you, [hero.name], that's so you!"
        lexi.say "Geez, you need to clean out your ears!"
        mike.say "So you did?"
        mike.say "You did say yes?"
        "I get a round of nods and smiles this time."
        "Which is probably for the best."
        "As I don't think I could manage to string together a sentence."
        "I'm too excited right now to do anything of the kind!"
    elif not any([g.flags.engagedmike for g in [samantha, lexi]]):
        "I feel like I've been punched in the gut."
        "And like it was done with serious intent too!"
        "Did I just go from being the luckiest guy in the world to the suckiest?"
        "I can't believe ALL of them said no!"
        mike.say "Y...you all said no..."
        mike.say "None of you want to get married?!?"
        "The girls are exchanging glances again."
        "But this time they look more than a little guilty."
        "Maybe I should at least take that as some small comfort!"

        samantha.say "I don't want to make the same mistake again."
        lexi.say "Me get married - are you serious?"
        "All I can do is nod and put on a brave face."
        "But all the same, I think they see how weak my smile is right now."
        "The girls gather round me, trying to offer reassurance."
        "Of course, this doesn't mean that our relationship is over."
        "Though it does make me wonder just how long-term it may prove to be..."
    else:
        "I find myself looking this way and that."
        "Some of the girls look elated at the prospect of marriage."
        "But the others look far more surprised, even worried."
        mike.say "So..."
        mike.say "Some of you don't want to marry me."
        mike.say "And some of you do..."
        "All of a sudden the girls who said yes step forwards."
        "Maybe they're trying to offer me support."
        "Or perhaps they want to separate themselves from the girls that said no."
        if samantha.flags.engagedmike:
            samantha.say "It's a yes from me."
        if lexi.flags.engagedmike:
            lexi.say "Hell yeah!"
        "I can't help smiling as the girls step forwards."
        "We form a tight little knot together, hugging and holding each other."
        "But then I catch a glimpse of the ones that said no."
        "They look suddenly isolated and cast out."
        "And I feel a pang of anxiety in the pit of my stomach."
        "Because I have no idea just what this means for them..."
    return

label lexi_minami_propose_male:
    "I know that I keep going on about how unbelievably amazing it is to be involved with my housemates."
    "But that's just something that you're going to gave to get used to hearing from me on the subject."
    "Maybe sometime in the future I'll have gotten used to the idea and it won't seem like such a big deal."
    "And then again, maybe I'll never stop waking up and thinking that I'm the luckiest guy in the world!"
    "Either way, everything seems to be going well for us right now."
    "Everyone's getting along fine and we're having a hell of a lot of fun together too."
    "So you're probably thinking that I'm just going to go along with things as they are."
    "I mean, why would I want to mess with success?"
    "Well, maybe I want to make the arrangement a little more, shall we say, permanent?"
    "That's right - I'm going to ask the girls to marry me."
    "It makes sense to me, formalising our relationship and making a commitment to each other."
    "And I'm gambling on the notion that the girls will feel the same way too."
    show minami tehe at left5
    show lexi bubblegum at right5
    with dissolve
    "So as soon as we're all together and the perfect moment arises, I pop the question."
    mike.say "Ah, guys..."
    mike.say "There's something I wanted to ask you..."
    show minami normal
    show lexi normal
    "Suddenly their heads turn in unison."
    "And all eyes are on me!"
    "Shit, I thought this was going to be much easier."
    "I feel like they're gazing into my soul!"
    mike.say "I guess I should do this the right way!"
    "I drop onto one knee, right in front of the girls."
    "This causes a flood of mixed reactions from them."
    "One moment they look confused, the next amazed."
    "Maybe this is how it's supposed to be?"
    mike.say "Will..."
    show minami surprised
    show lexi surprised
    mike.say "Will you marry me?"
    mike.say "Will all of you marry me?"
    mike.say "And, I guess, each other too?"
    "It doesn't take long for me to get an answer..."

    if minami.love < 195:
        show minami annoyed
        minami.say "Big bro, have you gone crazy?"
        minami.say "I can't get married to everyone!"
        $ minami.sub -= 25
        $ minami.love -= 25
    else:
        minami.say "Big bro, you're the best!"
        show minami happy
        minami.say "I will...I will...I will!"
        $ minami.set_fiance()
    if lexi.love < 195:
        show lexi annoyed
        lexi.say "You can't marry all of us."
        lexi.say "That's too wild, even for me!"
        $ lexi.sub -= 25
        $ lexi.love -= 25
    else:
        lexi.say "All of us get married?!?"
        show lexi happy
        lexi.say "That's wild - I'm in!"
        $ lexi.set_fiance()
    "Answering the question must have been a mind-blowing experience for the girls."
    "Because listening to what they had to say certainly was for me."
    "In fact, it takes me a moment to actually wrap my head around what they said."
    if all([g.flags.engagedmike for g in [minami, lexi]]):
        mike.say "Y...you all said yes?"
        mike.say "All of you really want to marry me?!?"
        "My second question is met with more amusement and irritation."
        "The girls shake their heads and roll their eyes at me."
        minami.say "Big bro!"
        lexi.say "Geez, you need to clean out your ears!"
        mike.say "So you did?"
        mike.say "You did say yes?"
        "I get a round of nods and smiles this time."
        "Which is probably for the best."
        "As I don't think I could manage to string together a sentence."
        "I'm too excited right now to do anything of the kind!"
    elif not any([g.flags.engagedmike for g in [minami, lexi]]):
        "I feel like I've been punched in the gut."
        "And like it was done with serious intent too!"
        "Did I just go from being the luckiest guy in the world to the suckiest?"
        "I can't believe ALL of them said no!"
        mike.say "Y...you all said no..."
        mike.say "None of you want to get married?!?"
        "The girls are exchanging glances again."
        "But this time they look more than a little guilty."
        "Maybe I should at least take that as some small comfort!"
        minami.say "I'm too young to get married, big bro!"
        lexi.say "Me get married - are you serious?"
        "All I can do is nod and put on a brave face."
        "But all the same, I think they see how weak my smile is right now."
        "The girls gather round me, trying to offer reassurance."
        "Of course, this doesn't mean that our relationship is over."
        "Though it does make me wonder just how long-term it may prove to be..."
    else:
        "I find myself looking this way and that."
        "Some of the girls look elated at the prospect of marriage."
        "But the others look far more surprised, even worried."
        mike.say "So..."
        mike.say "Some of you don't want to marry me."
        mike.say "And some of you do..."
        "All of a sudden the girls who said yes step forwards."
        "Maybe they're trying to offer me support."
        "Or perhaps they want to separate themselves from the girls that said no."
        if minami.flags.engagedmike:
            minami.say "Count me in, big bro!"
        if lexi.flags.engagedmike:
            lexi.say "Hell yeah!"
        "I can't help smiling as the girls step forwards."
        "We form a tight little knot together, hugging and holding each other."
        "But then I catch a glimpse of the ones that said no."
        "They look suddenly isolated and cast out."
        "And I feel a pang of anxiety in the pit of my stomach."
        "Because I have no idea just what this means for them..."
    return

label bree_lexi_propose_male:
    "I know that I keep going on about how unbelievably amazing it is to be involved with my housemates."
    "But that's just something that you're going to gave to get used to hearing from me on the subject."
    "Maybe sometime in the future I'll have gotten used to the idea and it won't seem like such a big deal."
    "And then again, maybe I'll never stop waking up and thinking that I'm the luckiest guy in the world!"
    "Either way, everything seems to be going well for us right now."
    "Everyone's getting along fine and we're having a hell of a lot of fun together too."
    "So you're probably thinking that I'm just going to go along with things as they are."
    "I mean, why would I want to mess with success?"
    "Well, maybe I want to make the arrangement a little more, shall we say, permanent?"
    "That's right - I'm going to ask the girls to marry me."
    "It makes sense to me, formalising our relationship and making a commitment to each other."
    "And I'm gambling on the notion that the girls will feel the same way too."
    show bree evil at left5
    show lexi bubblegum at right5
    with dissolve
    "So as soon as we're all together and the perfect moment arises, I pop the question."
    mike.say "Ah, guys..."
    mike.say "There's something I wanted to ask you..."
    show bree normal
    show lexi normal
    "Suddenly their heads turn in unison."
    "And all eyes are on me!"
    "Shit, I thought this was going to be much easier."
    "I feel like they're gazing into my soul!"
    mike.say "I guess I should do this the right way!"
    "I drop onto one knee, right in front of the girls."
    "This causes a flood of mixed reactions from them."
    "One moment they look confused, the next amazed."
    "Maybe this is how it's supposed to be?"
    mike.say "Will..."
    show bree surprised
    show lexi surprised
    mike.say "Will you marry me?"
    mike.say "Will all of you marry me?"
    mike.say "And, I guess, each other too?"
    "It doesn't take long for me to get an answer..."
    if bree.love < 195:
        show bree annoyed
        bree.say "[hero.name], you can't be serious?!?"
        bree.say "How would that even work?"
        $ bree.sub -= 25
        $ bree.love -= 25
    else:
        bree.say "[hero.name], are you serious?!?"
        show bree happy
        bree.say "Of course I will!"
        $ bree.set_fiance()
    if lexi.love < 195:
        show lexi annoyed
        lexi.say "You can't marry all of us."
        lexi.say "That's too wild, even for me!"
        $ lexi.sub -= 25
        $ lexi.love -= 25
    else:
        lexi.say "All of us get married?!?"
        show lexi happy
        lexi.say "That's wild - I'm in!"
        $ lexi.set_fiance()
    "Answering the question must have been a mind-blowing experience for the girls."
    "Because listening to what they had to say certainly was for me."
    "In fact, it takes me a moment to actually wrap my head around what they said."
    if all([g.flags.engagedmike for g in [bree, lexi]]):
        mike.say "Y...you all said yes?"
        mike.say "All of you really want to marry me?!?"
        "My second question is met with more amusement and irritation."
        "The girls shake their heads and roll their eyes at me."
        bree.say "Oh, [hero.name]!"
        lexi.say "Geez, you need to clean out your ears!"
        mike.say "So you did?"
        mike.say "You did say yes?"
        "I get a round of nods and smiles this time."
        "Which is probably for the best."
        "As I don't think I could manage to string together a sentence."
        "I'm too excited right now to do anything of the kind!"
    elif not any([g.flags.engagedmike for g in [bree, lexi]]):
        "I feel like I've been punched in the gut."
        "And like it was done with serious intent too!"
        "Did I just go from being the luckiest guy in the world to the suckiest?"
        "I can't believe ALL of them said no!"
        mike.say "Y...you all said no..."
        mike.say "None of you want to get married?!?"
        "The girls are exchanging glances again."
        "But this time they look more than a little guilty."
        "Maybe I should at least take that as some small comfort!"
        bree.say "I'm sorry, [hero.name] - I just can't."
        lexi.say "Me get married - are you serious?"
        "All I can do is nod and put on a brave face."
        "But all the same, I think they see how weak my smile is right now."
        "The girls gather round me, trying to offer reassurance."
        "Of course, this doesn't mean that our relationship is over."
        "Though it does make me wonder just how long-term it may prove to be..."
    else:
        "I find myself looking this way and that."
        "Some of the girls look elated at the prospect of marriage."
        "But the others look far more surprised, even worried."
        mike.say "So..."
        mike.say "Some of you don't want to marry me."
        mike.say "And some of you do..."
        "All of a sudden the girls who said yes step forwards."
        "Maybe they're trying to offer me support."
        "Or perhaps they want to separate themselves from the girls that said no."
        if bree.flags.engagedmike:
            bree.say "I do, [hero.name]."
        if lexi.flags.engagedmike:
            lexi.say "Hell yeah!"
        "I can't help smiling as the girls step forwards."
        "We form a tight little knot together, hugging and holding each other."
        "But then I catch a glimpse of the ones that said no."
        "They look suddenly isolated and cast out."
        "And I feel a pang of anxiety in the pit of my stomach."
        "Because I have no idea just what this means for them..."
    return

label lexi_sasha_propose_male:
    "I know that I keep going on about how unbelievably amazing it is to be involved with my housemates."
    "But that's just something that you're going to gave to get used to hearing from me on the subject."
    "Maybe sometime in the future I'll have gotten used to the idea and it won't seem like such a big deal."
    "And then again, maybe I'll never stop waking up and thinking that I'm the luckiest guy in the world!"
    "Either way, everything seems to be going well for us right now."
    "Everyone's getting along fine and we're having a hell of a lot of fun together too."
    "So you're probably thinking that I'm just going to go along with things as they are."
    "I mean, why would I want to mess with success?"
    "Well, maybe I want to make the arrangement a little more, shall we say, permanent?"
    "That's right - I'm going to ask the girls to marry me."
    "It makes sense to me, formalising our relationship and making a commitment to each other."
    "And I'm gambling on the notion that the girls will feel the same way too."
    show sasha annoyed at left5
    show lexi happy at right5
    with dissolve
    "So as soon as we're all together and the perfect moment arises, I pop the question."
    mike.say "Ah, guys..."
    mike.say "There's something I wanted to ask you..."
    show sasha normal
    show lexi normal
    "Suddenly their heads turn in unison."
    "And all eyes are on me!"
    "Shit, I thought this was going to be much easier."
    "I feel like they're gazing into my soul!"
    mike.say "I guess I should do this the right way!"
    "I drop onto one knee, right in front of the girls."
    "This causes a flood of mixed reactions from them."
    "One moment they look confused, the next amazed."
    "Maybe this is how it's supposed to be?"
    mike.say "Will..."
    show sasha surprised
    show lexi surprised
    mike.say "Will you marry me?"
    mike.say "Will all of you marry me?"
    mike.say "And, I guess, each other too?"
    "It doesn't take long for me to get an answer..."
    if sasha.love < 195:
        show sasha annoyed
        sasha.say "Are you out of your mind?!?"
        sasha.say "I didn't get into this thing to get married!"
        $ sasha.sub -= 25
        $ sasha.love -= 25
    else:
        sasha.say "Wow - that came out of the blue!"
        show sasha happy
        sasha.say "But yeah, I will!"
        $ sasha.set_fiance()
    if lexi.love < 195:
        show lexi annoyed
        lexi.say "You can't marry all of us."
        lexi.say "That's too wild, even for me!"
        $ lexi.sub -= 25
        $ lexi.love -= 25
    else:
        lexi.say "All of us get married?!?"
        show lexi happy
        lexi.say "That's wild - I'm in!"
        $ lexi.set_fiance()
    "Answering the question must have been a mind-blowing experience for the girls."
    "Because listening to what they had to say certainly was for me."
    "In fact, it takes me a moment to actually wrap my head around what they said."
    if all([g.flags.engagedmike for g in [sasha, lexi]]):
        mike.say "Y...you all said yes?"
        mike.say "All of you really want to marry me?!?"
        "My second question is met with more amusement and irritation."
        "The girls shake their heads and roll their eyes at me."
        sasha.say "Seriously, are you deaf or something?"
        lexi.say "Geez, you need to clean out your ears!"
        mike.say "So you did?"
        mike.say "You did say yes?"
        "I get a round of nods and smiles this time."
        "Which is probably for the best."
        "As I don't think I could manage to string together a sentence."
        "I'm too excited right now to do anything of the kind!"
    elif not any([g.flags.engagedmike for g in [sasha, lexi]]):
        "I feel like I've been punched in the gut."
        "And like it was done with serious intent too!"
        "Did I just go from being the luckiest guy in the world to the suckiest?"
        "I can't believe ALL of them said no!"
        mike.say "Y...you all said no..."
        mike.say "None of you want to get married?!?"
        "The girls are exchanging glances again."
        "But this time they look more than a little guilty."
        "Maybe I should at least take that as some small comfort!"
        sasha.say "I'm not the marrying type, [hero.name]!"
        lexi.say "Me get married - are you serious?"
        "All I can do is nod and put on a brave face."
        "But all the same, I think they see how weak my smile is right now."
        "The girls gather round me, trying to offer reassurance."
        "Of course, this doesn't mean that our relationship is over."
        "Though it does make me wonder just how long-term it may prove to be..."
    else:
        "I find myself looking this way and that."
        "Some of the girls look elated at the prospect of marriage."
        "But the others look far more surprised, even worried."
        mike.say "So..."
        mike.say "Some of you don't want to marry me."
        mike.say "And some of you do..."
        "All of a sudden the girls who said yes step forwards."
        "Maybe they're trying to offer me support."
        "Or perhaps they want to separate themselves from the girls that said no."
        if sasha.flags.engagedmike:
            sasha.say "I want to marry you!"
        if lexi.flags.engagedmike:
            lexi.say "Hell yeah!"
        "I can't help smiling as the girls step forwards."
        "We form a tight little knot together, hugging and holding each other."
        "But then I catch a glimpse of the ones that said no."
        "They look suddenly isolated and cast out."
        "And I feel a pang of anxiety in the pit of my stomach."
        "Because I have no idea just what this means for them..."
    return

label minami_samantha_propose_male:
    "I know that I keep going on about how unbelievably amazing it is to be involved with my housemates."
    "But that's just something that you're going to gave to get used to hearing from me on the subject."
    "Maybe sometime in the future I'll have gotten used to the idea and it won't seem like such a big deal."
    "And then again, maybe I'll never stop waking up and thinking that I'm the luckiest guy in the world!"
    "Either way, everything seems to be going well for us right now."
    "Everyone's getting along fine and we're having a hell of a lot of fun together too."
    "So you're probably thinking that I'm just going to go along with things as they are."
    "I mean, why would I want to mess with success?"
    "Well, maybe I want to make the arrangement a little more, shall we say, permanent?"
    "That's right - I'm going to ask the girls to marry me."
    "It makes sense to me, formalising our relationship and making a commitment to each other."
    "And I'm gambling on the notion that the girls will feel the same way too."
    show minami tehe at left5
    show samantha happy at right5
    with dissolve
    "So as soon as we're all together and the perfect moment arises, I pop the question."
    mike.say "Ah, guys..."
    mike.say "There's something I wanted to ask you..."
    show minami normal
    show samantha normal
    "Suddenly their heads turn in unison."
    "And all eyes are on me!"
    "Shit, I thought this was going to be much easier."
    "I feel like they're gazing into my soul!"
    mike.say "I guess I should do this the right way!"
    "I drop onto one knee, right in front of the girls."
    "This causes a flood of mixed reactions from them."
    "One moment they look confused, the next amazed."
    "Maybe this is how it's supposed to be?"
    mike.say "Will..."
    show minami surprised
    show samantha surprised
    mike.say "Will you marry me?"
    mike.say "Will all of you marry me?"
    mike.say "And, I guess, each other too?"
    "It doesn't take long for me to get an answer..."
    if minami.love < 195:
        show minami annoyed
        minami.say "Big bro, have you gone crazy?"
        minami.say "I can't get married to everyone!"
        $ minami.sub -= 25
        $ minami.love -= 25
    else:
        minami.say "Big bro, you're the best!"
        show minami happy
        minami.say "I will...I will...I will!"
        $ minami.set_fiance()
    if samantha.love < 195:
        show samantha annoyed
        samantha.say "Wow, [hero.name], I already got burnt once."
        samantha.say "And that was with only one spouse!"
        samantha.say "Count me out."
        $ samantha.sub -= 25
        $ samantha.love -= 25
    else:
        samantha.say "Well, I got burned the first time."
        samantha.say "But that was then and this is now."
        show samantha happy
        samantha.say "So yeah, I will!"
        $ samantha.set_fiance()
    "Answering the question must have been a mind-blowing experience for the girls."
    "Because listening to what they had to say certainly was for me."
    "In fact, it takes me a moment to actually wrap my head around what they said."
    if all([g.flags.engagedmike for g in [minami, samantha]]):
        mike.say "Y...you all said yes?"
        mike.say "All of you really want to marry me?!?"
        "My second question is met with more amusement and irritation."
        "The girls shake their heads and roll their eyes at me."
        minami.say "Big bro!"
        samantha.say "That's so you, [hero.name], that's so you!"
        mike.say "So you did?"
        mike.say "You did say yes?"
        "I get a round of nods and smiles this time."
        "Which is probably for the best."
        "As I don't think I could manage to string together a sentence."
        "I'm too excited right now to do anything of the kind!"
    elif not any([g.flags.engagedmike for g in [minami, samantha]]):
        "I feel like I've been punched in the gut."
        "And like it was done with serious intent too!"
        "Did I just go from being the luckiest guy in the world to the suckiest?"
        "I can't believe ALL of them said no!"
        mike.say "Y...you all said no..."
        mike.say "None of you want to get married?!?"
        "The girls are exchanging glances again."
        "But this time they look more than a little guilty."
        "Maybe I should at least take that as some small comfort!"
        minami.say "I'm too young to get married, big bro!"
        samantha.say "I don't want to make the same mistake again."
        "All I can do is nod and put on a brave face."
        "But all the same, I think they see how weak my smile is right now."
        "The girls gather round me, trying to offer reassurance."
        "Of course, this doesn't mean that our relationship is over."
        "Though it does make me wonder just how long-term it may prove to be..."
    else:
        "I find myself looking this way and that."
        "Some of the girls look elated at the prospect of marriage."
        "But the others look far more surprised, even worried."
        mike.say "So..."
        mike.say "Some of you don't want to marry me."
        mike.say "And some of you do..."
        "All of a sudden the girls who said yes step forwards."
        "Maybe they're trying to offer me support."
        "Or perhaps they want to separate themselves from the girls that said no."
        if minami.flags.engagedmike:
            minami.say "Count me in, big bro!"
        if samantha.flags.engagedmike:
            samantha.say "It's a yes from me."
        "I can't help smiling as the girls step forwards."
        "We form a tight little knot together, hugging and holding each other."
        "But then I catch a glimpse of the ones that said no."
        "They look suddenly isolated and cast out."
        "And I feel a pang of anxiety in the pit of my stomach."
        "Because I have no idea just what this means for them..."
    return

label bree_samantha_propose_male:
    "I know that I keep going on about how unbelievably amazing it is to be involved with my housemates."
    "But that's just something that you're going to gave to get used to hearing from me on the subject."
    "Maybe sometime in the future I'll have gotten used to the idea and it won't seem like such a big deal."
    "And then again, maybe I'll never stop waking up and thinking that I'm the luckiest guy in the world!"
    "Either way, everything seems to be going well for us right now."
    "Everyone's getting along fine and we're having a hell of a lot of fun together too."
    "So you're probably thinking that I'm just going to go along with things as they are."
    "I mean, why would I want to mess with success?"
    "Well, maybe I want to make the arrangement a little more, shall we say, permanent?"
    "That's right - I'm going to ask the girls to marry me."
    "It makes sense to me, formalising our relationship and making a commitment to each other."
    "And I'm gambling on the notion that the girls will feel the same way too."
    show bree evil at left5
    show samantha happy at right5
    with dissolve
    "So as soon as we're all together and the perfect moment arises, I pop the question."
    mike.say "Ah, guys..."
    mike.say "There's something I wanted to ask you..."
    show bree normal
    show samantha normal
    "Suddenly their heads turn in unison."
    "And all eyes are on me!"
    "Shit, I thought this was going to be much easier."
    "I feel like they're gazing into my soul!"
    mike.say "I guess I should do this the right way!"
    "I drop onto one knee, right in front of the girls."
    "This causes a flood of mixed reactions from them."
    "One moment they look confused, the next amazed."
    "Maybe this is how it's supposed to be?"
    mike.say "Will..."
    show bree surprised
    show samantha surprised
    mike.say "Will you marry me?"
    mike.say "Will all of you marry me?"
    mike.say "And, I guess, each other too?"
    "It doesn't take long for me to get an answer..."
    if bree.love < 195:
        show bree annoyed
        bree.say "[hero.name], you can't be serious?!?"
        bree.say "How would that even work?"
        $ bree.sub -= 25
        $ bree.love -= 25
    else:
        bree.say "[hero.name], are you serious?!?"
        show bree happy
        bree.say "Of course I will!"
        $ bree.set_fiance()
    if samantha.love < 195:
        show samantha annoyed
        samantha.say "Wow, [hero.name], I already got burnt once."
        samantha.say "And that was with only one spouse!"
        samantha.say "Count me out."
        $ samantha.sub -= 25
        $ samantha.love -= 25
    else:
        samantha.say "Well, I got burned the first time."
        samantha.say "But that was then and this is now."
        show samantha happy
        samantha.say "So yeah, I will!"
        $ samantha.set_fiance()
    "Answering the question must have been a mind-blowing experience for the girls."
    "Because listening to what they had to say certainly was for me."
    "In fact, it takes me a moment to actually wrap my head around what they said."
    if all([g.flags.engagedmike for g in [bree, samantha]]):
        mike.say "Y...you all said yes?"
        mike.say "All of you really want to marry me?!?"
        "My second question is met with more amusement and irritation."
        "The girls shake their heads and roll their eyes at me."
        bree.say "Oh, [hero.name]!"
        samantha.say "That's so you, [hero.name], that's so you!"
        mike.say "So you did?"
        mike.say "You did say yes?"
        "I get a round of nods and smiles this time."
        "Which is probably for the best."
        "As I don't think I could manage to string together a sentence."
        "I'm too excited right now to do anything of the kind!"
    elif not any([g.flags.engagedmike for g in [bree, samantha]]):
        "I feel like I've been punched in the gut."
        "And like it was done with serious intent too!"
        "Did I just go from being the luckiest guy in the world to the suckiest?"
        "I can't believe ALL of them said no!"
        mike.say "Y...you all said no..."
        mike.say "None of you want to get married?!?"
        "The girls are exchanging glances again."
        "But this time they look more than a little guilty."
        "Maybe I should at least take that as some small comfort!"
        bree.say "I'm sorry, [hero.name] - I just can't."
        samantha.say "I don't want to make the same mistake again."
        "All I can do is nod and put on a brave face."
        "But all the same, I think they see how weak my smile is right now."
        "The girls gather round me, trying to offer reassurance."
        "Of course, this doesn't mean that our relationship is over."
        "Though it does make me wonder just how long-term it may prove to be..."
    else:
        "I find myself looking this way and that."
        "Some of the girls look elated at the prospect of marriage."
        "But the others look far more surprised, even worried."
        mike.say "So..."
        mike.say "Some of you don't want to marry me."
        mike.say "And some of you do..."
        "All of a sudden the girls who said yes step forwards."
        "Maybe they're trying to offer me support."
        "Or perhaps they want to separate themselves from the girls that said no."
        if bree.flags.engagedmike:
            bree.say "I do, [hero.name]."
        if samantha.flags.engagedmike:
            samantha.say "It's a yes from me."

        "I can't help smiling as the girls step forwards."
        "We form a tight little knot together, hugging and holding each other."
        "But then I catch a glimpse of the ones that said no."
        "They look suddenly isolated and cast out."
        "And I feel a pang of anxiety in the pit of my stomach."
        "Because I have no idea just what this means for them..."
    return

label samantha_sasha_propose_male:
    "I know that I keep going on about how unbelievably amazing it is to be involved with my housemates."
    "But that's just something that you're going to gave to get used to hearing from me on the subject."
    "Maybe sometime in the future I'll have gotten used to the idea and it won't seem like such a big deal."
    "And then again, maybe I'll never stop waking up and thinking that I'm the luckiest guy in the world!"
    "Either way, everything seems to be going well for us right now."
    "Everyone's getting along fine and we're having a hell of a lot of fun together too."
    "So you're probably thinking that I'm just going to go along with things as they are."
    "I mean, why would I want to mess with success?"
    "Well, maybe I want to make the arrangement a little more, shall we say, permanent?"
    "That's right - I'm going to ask the girls to marry me."
    "It makes sense to me, formalising our relationship and making a commitment to each other."
    "And I'm gambling on the notion that the girls will feel the same way too."
    show sasha annoyed at left5
    show samantha happy at right5
    with dissolve
    "So as soon as we're all together and the perfect moment arises, I pop the question."
    mike.say "Ah, guys..."
    mike.say "There's something I wanted to ask you..."
    show sasha normal
    show samantha normal
    "Suddenly their heads turn in unison."
    "And all eyes are on me!"
    "Shit, I thought this was going to be much easier."
    "I feel like they're gazing into my soul!"
    mike.say "I guess I should do this the right way!"
    "I drop onto one knee, right in front of the girls."
    "This causes a flood of mixed reactions from them."
    "One moment they look confused, the next amazed."
    "Maybe this is how it's supposed to be?"
    mike.say "Will..."
    show sasha surprised
    show samantha surprised
    mike.say "Will you marry me?"
    mike.say "Will all of you marry me?"
    mike.say "And, I guess, each other too?"
    "It doesn't take long for me to get an answer..."
    if sasha.love < 195:
        show sasha annoyed
        sasha.say "Are you out of your mind?!?"
        sasha.say "I didn't get into this thing to get married!"
        $ sasha.sub -= 25
        $ sasha.love -= 25
    else:
        sasha.say "Wow - that came out of the blue!"
        show sasha happy
        sasha.say "But yeah, I will!"
        $ sasha.set_fiance()
    if samantha.love < 195:
        show samantha annoyed
        samantha.say "Wow, [hero.name], I already got burnt once."
        samantha.say "And that was with only one spouse!"
        samantha.say "Count me out."
        $ samantha.sub -= 25
        $ samantha.love -= 25
    else:
        samantha.say "Well, I got burned the first time."
        samantha.say "But that was then and this is now."
        show samantha happy
        samantha.say "So yeah, I will!"
        $ samantha.set_fiance()
    "Answering the question must have been a mind-blowing experience for the girls."
    "Because listening to what they had to say certainly was for me."
    "In fact, it takes me a moment to actually wrap my head around what they said."
    if all([g.flags.engagedmike for g in [sasha, samantha]]):
        mike.say "Y...you all said yes?"
        mike.say "All of you really want to marry me?!?"
        "My second question is met with more amusement and irritation."
        "The girls shake their heads and roll their eyes at me."
        sasha.say "Seriously, are you deaf or something?"
        samantha.say "That's so you, [hero.name], that's so you!"
        mike.say "So you did?"
        mike.say "You did say yes?"
        "I get a round of nods and smiles this time."
        "Which is probably for the best."
        "As I don't think I could manage to string together a sentence."
        "I'm too excited right now to do anything of the kind!"
    elif not any([g.flags.engagedmike for g in [sasha, samantha]]):
        "I feel like I've been punched in the gut."
        "And like it was done with serious intent too!"
        "Did I just go from being the luckiest guy in the world to the suckiest?"
        "I can't believe ALL of them said no!"
        mike.say "Y...you all said no..."
        mike.say "None of you want to get married?!?"
        "The girls are exchanging glances again."
        "But this time they look more than a little guilty."
        "Maybe I should at least take that as some small comfort!"
        sasha.say "I'm not the marrying type, [hero.name]!"
        samantha.say "I don't want to make the same mistake again."
        "All I can do is nod and put on a brave face."
        "But all the same, I think they see how weak my smile is right now."
        "The girls gather round me, trying to offer reassurance."
        "Of course, this doesn't mean that our relationship is over."
        "Though it does make me wonder just how long-term it may prove to be..."
    else:
        "I find myself looking this way and that."
        "Some of the girls look elated at the prospect of marriage."
        "But the others look far more surprised, even worried."
        mike.say "So..."
        mike.say "Some of you don't want to marry me."
        mike.say "And some of you do..."
        "All of a sudden the girls who said yes step forwards."
        "Maybe they're trying to offer me support."
        "Or perhaps they want to separate themselves from the girls that said no."

        if sasha.flags.engagedmike:
            sasha.say "I want to marry you!"

        if samantha.flags.engagedmike:
            samantha.say "It's a yes from me."

        "I can't help smiling as the girls step forwards."
        "We form a tight little knot together, hugging and holding each other."
        "But then I catch a glimpse of the ones that said no."
        "They look suddenly isolated and cast out."
        "And I feel a pang of anxiety in the pit of my stomach."
        "Because I have no idea just what this means for them..."
    return

label bree_minami_propose_male:
    "I know that I keep going on about how unbelievably amazing it is to be involved with my housemates."
    "But that's just something that you're going to gave to get used to hearing from me on the subject."
    "Maybe sometime in the future I'll have gotten used to the idea and it won't seem like such a big deal."
    "And then again, maybe I'll never stop waking up and thinking that I'm the luckiest guy in the world!"
    "Either way, everything seems to be going well for us right now."
    "Everyone's getting along fine and we're having a hell of a lot of fun together too."
    "So you're probably thinking that I'm just going to go along with things as they are."
    "I mean, why would I want to mess with success?"
    "Well, maybe I want to make the arrangement a little more, shall we say, permanent?"
    "That's right - I'm going to ask the girls to marry me."
    "It makes sense to me, formalising our relationship and making a commitment to each other."
    "And I'm gambling on the notion that the girls will feel the same way too."
    show minami tehe at left5
    show bree evil at right5
    with dissolve
    "So as soon as we're all together and the perfect moment arises, I pop the question."
    mike.say "Ah, guys..."
    mike.say "There's something I wanted to ask you..."
    show minami normal
    show bree normal
    "Suddenly their heads turn in unison."
    "And all eyes are on me!"
    "Shit, I thought this was going to be much easier."
    "I feel like they're gazing into my soul!"
    mike.say "I guess I should do this the right way!"
    "I drop onto one knee, right in front of the girls."
    "This causes a flood of mixed reactions from them."
    "One moment they look confused, the next amazed."
    "Maybe this is how it's supposed to be?"
    mike.say "Will..."
    show minami surprised
    show bree surprised
    mike.say "Will you marry me?"
    mike.say "Will all of you marry me?"
    mike.say "And, I guess, each other too?"
    "It doesn't take long for me to get an answer..."
    if bree.love < 195:
        show bree annoyed
        bree.say "[hero.name], you can't be serious?!?"
        bree.say "How would that even work?"
        $ bree.sub -= 25
        $ bree.love -= 25
    else:
        bree.say "[hero.name], are you serious?!?"
        show bree happy
        bree.say "Of course I will!"
        $ bree.set_fiance()
    if minami.love < 195:
        show minami annoyed
        minami.say "Big bro, have you gone crazy?"
        minami.say "I can't get married to everyone!"
        $ minami.sub -= 25
        $ minami.love -= 25
    else:
        minami.say "Big bro, you're the best!"
        show minami happy
        minami.say "I will...I will...I will!"
        $ minami.set_fiance()
    "Answering the question must have been a mind-blowing experience for the girls."
    "Because listening to what they had to say certainly was for me."
    "In fact, it takes me a moment to actually wrap my head around what they said."
    if all([g.flags.engagedmike for g in [bree, minami]]):
        mike.say "Y...you all said yes?"
        mike.say "All of you really want to marry me?!?"
        "My second question is met with more amusement and irritation."
        "The girls shake their heads and roll their eyes at me."
        bree.say "Oh, [hero.name]!"
        minami.say "Big bro!"
        mike.say "So you did?"
        mike.say "You did say yes?"
        "I get a round of nods and smiles this time."
        "Which is probably for the best."
        "As I don't think I could manage to string together a sentence."
        "I'm too excited right now to do anything of the kind!"
    elif not any([g.flags.engagedmike for g in [bree, minami]]):
        "I feel like I've been punched in the gut."
        "And like it was done with serious intent too!"
        "Did I just go from being the luckiest guy in the world to the suckiest?"
        "I can't believe ALL of them said no!"
        mike.say "Y...you all said no..."
        mike.say "None of you want to get married?!?"
        "The girls are exchanging glances again."
        "But this time they look more than a little guilty."
        "Maybe I should at least take that as some small comfort!"
        bree.say "I'm sorry, [hero.name] - I just can't."
        minami.say "I'm too young to get married, big bro!"

        "All I can do is nod and put on a brave face."
        "But all the same, I think they see how weak my smile is right now."
        "The girls gather round me, trying to offer reassurance."
        "Of course, this doesn't mean that our relationship is over."
        "Though it does make me wonder just how long-term it may prove to be..."
    else:
        "I find myself looking this way and that."
        "Some of the girls look elated at the prospect of marriage."
        "But the others look far more surprised, even worried."
        mike.say "So..."
        mike.say "Some of you don't want to marry me."
        mike.say "And some of you do..."
        "All of a sudden the girls who said yes step forwards."
        "Maybe they're trying to offer me support."
        "Or perhaps they want to separate themselves from the girls that said no."
        if bree.flags.engagedmike:
            bree.say "I do, [hero.name]."

        if minami.flags.engagedmike:
            minami.say "Count me in, big bro!"

        "I can't help smiling as the girls step forwards."
        "We form a tight little knot together, hugging and holding each other."
        "But then I catch a glimpse of the ones that said no."
        "They look suddenly isolated and cast out."
        "And I feel a pang of anxiety in the pit of my stomach."
        "Because I have no idea just what this means for them..."
    return

label minami_sasha_propose_male:
    "I know that I keep going on about how unbelievably amazing it is to be involved with my housemates."
    "But that's just something that you're going to gave to get used to hearing from me on the subject."
    "Maybe sometime in the future I'll have gotten used to the idea and it won't seem like such a big deal."
    "And then again, maybe I'll never stop waking up and thinking that I'm the luckiest guy in the world!"
    "Either way, everything seems to be going well for us right now."
    "Everyone's getting along fine and we're having a hell of a lot of fun together too."
    "So you're probably thinking that I'm just going to go along with things as they are."
    "I mean, why would I want to mess with success?"
    "Well, maybe I want to make the arrangement a little more, shall we say, permanent?"
    "That's right - I'm going to ask the girls to marry me."
    "It makes sense to me, formalising our relationship and making a commitment to each other."
    "And I'm gambling on the notion that the girls will feel the same way too."
    show minami tehe at left5
    show sasha annoyed at right5
    with dissolve
    "So as soon as we're all together and the perfect moment arises, I pop the question."
    mike.say "Ah, guys..."
    mike.say "There's something I wanted to ask you..."
    show minami normal
    show sasha normal
    "Suddenly their heads turn in unison."
    "And all eyes are on me!"
    "Shit, I thought this was going to be much easier."
    "I feel like they're gazing into my soul!"
    mike.say "I guess I should do this the right way!"
    "I drop onto one knee, right in front of the girls."
    "This causes a flood of mixed reactions from them."
    "One moment they look confused, the next amazed."
    "Maybe this is how it's supposed to be?"
    mike.say "Will..."
    show minami surprised
    show sasha surprised
    mike.say "Will you marry me?"
    mike.say "Will all of you marry me?"
    mike.say "And, I guess, each other too?"
    "It doesn't take long for me to get an answer..."

    if sasha.love < 195:
        show sasha annoyed
        sasha.say "Are you out of your mind?!?"
        sasha.say "I didn't get into this thing to get married!"
        $ sasha.sub -= 25
        $ sasha.love -= 25
    else:
        sasha.say "Wow - that came out of the blue!"
        show sasha happy
        sasha.say "But yeah, I will!"
        $ sasha.set_fiance()
    if minami.love < 195:
        show minami annoyed
        minami.say "Big bro, have you gone crazy?"
        minami.say "I can't get married to everyone!"
        $ minami.sub -= 25
        $ minami.love -= 25
    else:
        minami.say "Big bro, you're the best!"
        show minami happy
        minami.say "I will...I will...I will!"
        $ minami.set_fiance()
    "Answering the question must have been a mind-blowing experience for the girls."
    "Because listening to what they had to say certainly was for me."
    "In fact, it takes me a moment to actually wrap my head around what they said."
    if all([g.flags.engagedmike for g in [sasha, minami]]):
        mike.say "Y...you all said yes?"
        mike.say "All of you really want to marry me?!?"
        "My second question is met with more amusement and irritation."
        "The girls shake their heads and roll their eyes at me."

        sasha.say "Seriously, are you deaf or something?"
        minami.say "Big bro!"
        mike.say "So you did?"
        mike.say "You did say yes?"
        "I get a round of nods and smiles this time."
        "Which is probably for the best."
        "As I don't think I could manage to string together a sentence."
        "I'm too excited right now to do anything of the kind!"
    elif not any([g.flags.engagedmike for g in [ sasha, minami]]):
        "I feel like I've been punched in the gut."
        "And like it was done with serious intent too!"
        "Did I just go from being the luckiest guy in the world to the suckiest?"
        "I can't believe ALL of them said no!"
        mike.say "Y...you all said no..."
        mike.say "None of you want to get married?!?"
        "The girls are exchanging glances again."
        "But this time they look more than a little guilty."
        "Maybe I should at least take that as some small comfort!"

        sasha.say "I'm not the marrying type, [hero.name]!"
        minami.say "I'm too young to get married, big bro!"
        "All I can do is nod and put on a brave face."
        "But all the same, I think they see how weak my smile is right now."
        "The girls gather round me, trying to offer reassurance."
        "Of course, this doesn't mean that our relationship is over."
        "Though it does make me wonder just how long-term it may prove to be..."
    else:
        "I find myself looking this way and that."
        "Some of the girls look elated at the prospect of marriage."
        "But the others look far more surprised, even worried."
        mike.say "So..."
        mike.say "Some of you don't want to marry me."
        mike.say "And some of you do..."
        "All of a sudden the girls who said yes step forwards."
        "Maybe they're trying to offer me support."
        "Or perhaps they want to separate themselves from the girls that said no."

        if sasha.flags.engagedmike:
            sasha.say "I want to marry you!"
        if minami.flags.engagedmike:
            minami.say "Count me in, big bro!"

        "I can't help smiling as the girls step forwards."
        "We form a tight little knot together, hugging and holding each other."
        "But then I catch a glimpse of the ones that said no."
        "They look suddenly isolated and cast out."
        "And I feel a pang of anxiety in the pit of my stomach."
        "Because I have no idea just what this means for them..."
    return

label bree_sasha_propose_male:
    show bree at left5
    show sasha at right5
    with dissolve
    "I'm in pretty much uncharted territory here, considering how I've never proposed to one girl before, let alone two at once."
    "But what with the recent changes in the polygamy laws and the fact that I've been happily involved in a serious relationship with both [bree.name] and Sasha, it seems like the way to go."
    "As I don't have any experience of this kind of thing, and there aren't exactly many books or movies in which a guy proposes to two girls at once, I decide to go with the old classic."
    "With just a few minor adjustments, that is..."
    "I pick my moment, and get down on one knee before them both, producing a ring in each hand."
    mike.say "[bree.name]...Sasha...will you marry me?"
    mike.say "And, I guess, each other?"
    if bree.love < 195 and sasha.love < 195:
        show bree surprised
        show sasha surprised
        "[bree.name] and Sasha look at each other in genuine surprise for a moment."
        show bree happy at left5, startle
        show sasha happy at right5, startle
        "And then [bree.name] bursts into peals of laughter, followed by Sasha a few seconds later."
        bree.say "Oh, [hero.name] - that's so cute!"
        show sasha joke
        sasha.say "Honestly, is this a joke - did someone put you up to this?"
        mike.say "I...erm...I..."
        show bree evil
        bree.say "I mean, this whole polygamy thing's just a fad, right?"
        sasha.say "Sure it is - mark my words, it'll be out of fashion by this time next year!"
        mike.say "Ah...yeah...of course - but I almost had you there for a minute, didn't I?"
        "I manage a nervous life as I die a little on the inside."
        $ bree.love -= 25
        $ sasha.love -= 25
        $ bree.sub -= 25
        $ sasha.sub -= 25
    elif sasha.love < 195:
        show bree happy
        bree.say "Yes, of course!"
        show sasha annoyed
        sasha.say "Oh, hell no!"
        "Before I can begin to make sense of their conflicting answers, [bree.name] and Sasha turn to stare at each other."
        show bree surprised
        show sasha surprised
        "Both their faces are an image of surprise and shock and hearing the other's honest answer."
        bree.say "What the hell, Sasha - are [hero.name] and I not good enough for you all of a sudden?"
        sasha.say "Huh...no, that's not it at all!"
        sasha.say "I just don't want to get tied down..."
        bree.say "Well, she might only be in it for the thrills - but I'm ready to make a commitment, [hero.name]!"
        "Well, I guess two out of three isn't bad."
        $ bree.set_fiance()
        $ sasha.sub -= 25
        $ sasha.love -= 25
    elif bree.love < 195:
        show bree sad
        bree.say "Oh...oh no!"
        show sasha happy
        sasha.say "Oh, hell yes!"
        show bree surprised
        show sasha surprised
        "Before I can begin to make sense of their conflicting answers, [bree.name] and Sasha turn to stare at each other."
        "Both their faces are an image of surprise and shock and hearing the other's honest answer."
        sasha.say "What the hell, [bree.name] - are [hero.name] and I not good enough for you all of a sudden?"
        sasha.say "What the hell, [bree.name] - are [hero.name] and I not good enough for you all of a sudden?"
        bree.say "No, no...I'm just not ready for that kind of commitment - not yet!"
        sasha.say "Forget her, [hero.name] - we're gonna make quite a pair, you and me!"
        "Well, I guess two out of three isn't bad."
        $ sasha.set_fiance()
        $ bree.sub -= 25
        $ bree.love -= 25
    else:
        show bree happy at right5
        show sasha happy at left5
        bree.say "Yes!"
        sasha.say "Yes!"
        "Both of the girls stare at the expression of sheer amazement on my face."
        "And then they look at each other, seeing the exact same emotion there as well."
        mike.say "You really mean it - both of you?!?"
        bree.say "Sure - we started out as housemates, then became friends and eventually lovers."
        sasha.say "The only thing that could make what we have any better is it being made official."
        bree.say "We're all of us living proof that this kind of relationship can work, if you love each other enough."
        sasha.say "Yeah - I guess you could say we're kind of like pioneers, or something!"
        "I don't know much about being someone that drives social change."
        "But I do know that these two girls have just made me feel like the luckiest guy in the world."
        $ sasha.set_fiance()
        $ bree.set_fiance()
    return

label home_harem_fuck_choices(from_girl=None):
    hide bree
    hide sasha
    hide samantha
    hide minami
    if Person.is_not_hidden("lexi"):
        hide lexi
    if {"home_harem_sixsome"} & set(DONE) and Person.is_not_hidden("lexi") and Harem.together(bree, sasha, minami, samantha, lexi, name="home") and all([(Room.has_tag(g.room, 'home') and not g.activity_name == "sleep" and not g.hidden and not g.flags.cheated) for g in [bree, sasha, minami, samantha, lexi]]):

        if from_girl == "bree":
            show sasha at left5
            show bree
            sasha.say "Can I join in?"
            show samantha at right5
            samantha.say "Can I join too?"
            show minami at mostleft5
            minami.say "Hey I'm here too!"
            show lexi at mostright5
            lexi.say "Don't forget me!"
            menu:
                "Yes":
                    mike.say "That would be great."
                    call home_harem_sixsome_intro from _call_home_harem_sixsome_intro
                "No":
                    mike.say "Sorry, I wanna be alone with [bree.name] a little."
                    $ sasha.love -= 2
                    $ samantha.love -= 2
                    $ minami.love -= 2
                    $ lexi.love -= 2
                    hide sasha
                    hide samantha
                    hide minami
                    hide lexi
                    call bree_fuck_date_male from _call_bree_fuck_date_1
        elif from_girl == "minami":
            show samantha at left5
            show minami
            samantha.say "Can I join in?"
            show lexi at right5
            lexi.say "Can I join too?"
            show bree at mostleft5
            bree.say "Hey I'm here too!"
            show sasha at mostright5
            sasha.say "Don't forget me!"
            menu:
                "Yes":
                    mike.say "That would be great."
                    call home_harem_sixsome_intro from _call_home_harem_sixsome_intro_1
                "No":
                    mike.say "Sorry, I wanna be alone with Minami a little."
                    $ sasha.love -= 2
                    $ samantha.love -= 2
                    $ bree.love -= 2
                    $ lexi.love -= 2
                    hide sasha
                    hide samantha
                    hide bree
                    hide lexi
                    call minami_fuck_date_male from _call_minami_fuck_date
        elif from_girl == "samantha":
            show lexi at left5
            show samantha
            lexi.say "Can I join in?"
            show sasha at right5
            sasha.say "Can I join too?"
            show minami at mostleft5
            minami.say "Hey I'm here too!"
            show bree at mostright5
            bree.say "Don't forget me!"
            menu:
                "Yes":
                    mike.say "That would be great."
                    call home_harem_sixsome_intro from _call_home_harem_sixsome_intro_2
                "No":
                    if samantha.flags.nickname == "cupcake":
                        mike.say "Sorry, I wanna be alone with my Cupcake a little."
                    else:
                        mike.say "Sorry, I wanna be alone with Samantha a little."
                    $ sasha.love -= 2
                    $ bree.love -= 2
                    $ minami.love -= 2
                    $ lexi.love -= 2
                    hide sasha
                    hide bree
                    hide minami
                    hide lexi
                    call samantha_fuck_date_male from _call_samantha_fuck_date
        elif from_girl == "sasha":
            show bree at left5
            show sasha
            bree.say "Can I join in?"
            show lexi at right5
            lexi.say "Can I join too?"
            show minami at mostleft5
            minami.say "Hey I'm here too!"
            show samantha at mostright5
            samantha.say "Don't forget me!"
            menu:
                "Yes":
                    mike.say "That would be great."
                    call home_harem_sixsome_intro from _call_home_harem_sixsome_intro_3
                "No":
                    mike.say "Sorry, I wanna be alone with Sasha a little."
                    $ bree.love -= 2
                    $ samantha.love -= 2
                    $ minami.love -= 2
                    $ lexi.love -= 2
                    hide sasha
                    hide bree
                    hide minami
                    hide lexi
                    call sasha_fuck_date_male from _call_sasha_fuck_date_1
        elif from_girl == "lexi":
            show minami at left5
            show lexi
            minami.say "Can I join in?"
            show sasha at right5
            sasha.say "Can I join too?"
            show bree at mostleft5
            bree.say "Hey I'm here too!"
            show samantha at mostright5
            samantha.say "Don't forget me!"
            menu:
                "Yes":
                    mike.say "That would be great."
                    call home_harem_sixsome_intro from _call_home_harem_sixsome_intro_4
                "No":
                    mike.say "Sorry, I wanna be alone with Lexi a little."
                    $ bree.love -= 2
                    $ samantha.love -= 2
                    $ sasha.love -= 2
                    $ minami.love -= 2
                    hide sasha
                    hide samantha
                    hide minami
                    hide bree
                    call lexi_fuck_date_male from _call_lexi_fuck_date
    elif Harem.find(samantha, name='home') and from_girl in ["bree", "sasha", "minami"] and Harem.together(bree, sasha, minami, samantha, name="home") and all([(Room.has_tag(g.room, 'home') and not g.activity_name == "sleep" and not g.hidden and not g.flags.cheated) for g in [bree, sasha, minami, samantha]]):

        if from_girl == "bree":
            show sasha at left4
            show bree at right4
            sasha.say "Can I join in?"
            show samantha at mostright4
            samantha.say "Can I join too?"
            show minami at mostleft4
            minami.say "Hey I'm here too!"
            menu:
                "Yes":
                    mike.say "That would be great."
                    call fivesome_breeminamisamsasha from _call_fivesome_breeminamisamsasha
                "No":
                    mike.say "Sorry, I wanna be alone with [bree.name] a little."
                    $ sasha.love -= 2
                    $ samantha.love -= 2
                    $ minami.love -= 2
                    hide sasha
                    hide samantha
                    hide minami
                    call bree_fuck_date_male from _call_bree_fuck_date_2
        elif from_girl == "minami":
            show bree at left4
            show minami at right4
            bree.say "Can I join in?"
            show sasha at mostright4
            sasha.say "Can I join too?"
            show samantha at mostleft4
            samantha.say "Hey I'm here too!"
            menu:
                "Yes":
                    mike.say "That would be great."
                    call fivesome_breeminamisamsasha from _call_fivesome_breeminamisamsasha_1
                "No":
                    mike.say "Sorry, I wanna be alone with Minami a little."
                    $ sasha.love -= 2
                    $ samantha.love -= 2
                    $ bree.love -= 2
                    hide sasha
                    hide samantha
                    hide bree
                    call minami_fuck_date_male from _call_minami_fuck_date_1
        elif from_girl == "samantha":
            show minami at left4
            show samantha at right4
            minami.say "Can I join in?"
            show bree at mostright4
            bree.say "Can I join too?"
            show sasha at mostleft4
            sasha.say "Hey I'm here too!"
            menu:
                "Yes":
                    mike.say "That would be great."
                    call fivesome_breeminamisamsasha from _call_fivesome_breeminamisamsasha_2
                "No":
                    if samantha.flags.nickname == "cupcake":
                        mike.say "Sorry, I wanna be alone with Cupcake a little."
                    else:
                        mike.say "Sorry, I wanna be alone with Samantha a little."
                    $ sasha.love -= 2
                    $ bree.love -= 2
                    $ minami.love -= 2
                    hide sasha
                    hide bree
                    hide minami
                    call samantha_fuck_date_male from _call_samantha_fuck_date_1
        elif from_girl == "sasha":
            show samantha at left4
            show sasha at right4
            samantha.say "Can I join in?"
            show bree at mostright4
            bree.say "Can I join too?"
            show minami at mostleft4
            minami.say "Hey I'm here too!"
            menu:
                "Yes":
                    mike.say "That would be great."
                    call fivesome_breeminamisamsasha from _call_fivesome_breeminamisamsasha_3
                "No":
                    mike.say "Sorry, I wanna be alone with Sasha a little."
                    $ bree.love -= 2
                    $ samantha.love -= 2
                    $ minami.love -= 2
                    hide samantha
                    hide bree
                    hide minami
                    call sasha_fuck_date_male from _call_sasha_fuck_date_2
    elif Harem.find(samantha, name='home') and from_girl in ["bree", "sasha", "samantha"] and Harem.together(bree, sasha, samantha, name="home") and all([(Room.has_tag(g.room, 'home') and not g.activity_name == "sleep" and not g.hidden and not g.flags.cheated) for g in [bree, samantha, sasha]]):

        if from_girl == "bree":
            show sasha at left
            show bree
            sasha.say "Can I join in?"
            show samantha at right
            samantha.say "Can I join too?"
            menu:
                "Yes":
                    mike.say "That would be great."
                    call foursome_breesamsasha from _call_foursome_breesamsasha
                "I want some time with Sasha and [bree.name]":
                    if samantha.flags.nickname == "cupcake":
                        mike.say "Sorry Cupcake, I wanna be alone with [bree.name] and Sasha a little."
                    else:
                        mike.say "Sorry Sam, I wanna be alone with [bree.name] and Sasha a little."
                    $ samantha.love -= 2
                    hide samantha
                    if game.flags.minamirefusedinhomeharem and not minami.flags.crash_threesome:
                        call minami_crash_threesome from _call_minami_crash_threesome
                    else:
                        call bree_sasha_threesome from _call_bree_sasha_threesome
                "No":
                    mike.say "Sorry, I wanna be alone with [bree.name] a little."
                    $ sasha.love -= 2
                    $ samantha.love -= 2
                    hide sasha
                    hide samantha
                    call bree_fuck_date_male from _call_bree_fuck_date_3
        elif from_girl == "sasha":
            show samantha at left
            show sasha
            samantha.say "Can I join in?"
            show bree at right
            bree.say "Can I join too?"
            menu:
                "Yes":
                    mike.say "That would be great."
                    call foursome_breesamsasha from _call_foursome_breesamsasha_1
                "I want some time with Sasha and [bree.name]":
                    if samantha.flags.nickname == "cupcake":
                        mike.say "Sorry Cupcake, I wanna be alone with [bree.name] and Sasha a little."
                    else:
                        mike.say "Sorry Sam, I wanna be alone with [bree.name] and Sasha a little."
                    $ samantha.love -= 2
                    hide samantha
                    if game.flags.minamirefusedinhomeharem and not minami.flags.crash_threesome:
                        call minami_crash_threesome from _call_minami_crash_threesome_1
                    else:
                        call bree_sasha_threesome_2 from _call_bree_sasha_threesome_2
                "No":
                    mike.say "Sorry, I wanna be alone with Sasha a little."
                    $ bree.love -= 2
                    $ samantha.love -= 2
                    hide samantha
                    hide bree
                    call sasha_fuck_date_male from _call_sasha_fuck_date_3
        elif from_girl == "samantha":
            show bree at left
            show samantha
            bree.say "Can I join in?"
            show sasha at right
            sasha.say "Can I join too?"
            menu:
                "Yes":
                    mike.say "That would be great."
                    call foursome_breesamsasha from _call_foursome_breesamsasha_2
                "No":
                    if samantha.flags.nickname == "cupcake":
                        mike.say "Sorry, I wanna be alone with my Cupcake a little."
                    else:
                        mike.say "Sorry, I wanna be alone with Samantha a little."
                    $ sasha.love -= 2
                    $ bree.love -= 2
                    hide sasha
                    hide bree
                    call samantha_fuck_date_male from _call_samantha_fuck_date_2
    elif "foursome_lexisamsasha" in DONE and Person.is_not_hidden("lexi") and from_girl in ["lexi", "sasha", "samantha"] and Person.is_not_hidden("lexi") and Harem.together(lexi, sasha, samantha, name="home") and all([(Room.has_tag(g.room, 'home') and not g.activity_name == "sleep" and not g.hidden and not g.flags.cheated) for g in [lexi, samantha, sasha]]):

        if from_girl == "lexi":
            show sasha at left
            show lexi
            sasha.say "Can I join in?"
            show samantha at right
            samantha.say "Can I join too?"
            menu:
                "Yes":
                    mike.say "That would be great."
                    call foursome_lexisamsasha from _call_foursome_lexisamsasha
                "No":
                    mike.say "Sorry, I wanna be alone with Lexi a little."
                    $ sasha.love -= 2
                    $ samantha.love -= 2
                    hide sasha
                    hide samantha
                    call lexi_fuck_date_male from _call_lexi_fuck_date_1
        elif from_girl == "sasha":
            show samantha at left
            show sasha
            samantha.say "Can I join in?"
            show lexi at right
            lexi.say "Can I join too?"
            menu:
                "Yes":
                    mike.say "That would be great."
                    call foursome_lexisamsasha from _call_foursome_lexisamsasha_1
                "No":
                    mike.say "Sorry, I wanna be alone with Sasha a little."
                    $ lexi.love -= 2
                    $ samantha.love -= 2
                    hide lexi
                    hide samantha
                    call sasha_fuck_date_male from _call_sasha_fuck_date_4
        elif from_girl == "samantha":
            show lexi at left
            show samantha
            lexi.say "Can I join in?"
            show sasha at right
            sasha.say "Can I join too?"
            menu:
                "Yes":
                    mike.say "That would be great."
                    call foursome_lexisamsasha from _call_foursome_lexisamsasha_2
                "No":
                    if samantha.flags.nickname == "cupcake":
                        mike.say "Sorry, I wanna be alone with Cupcake a little."
                    else:
                        mike.say "Sorry, I wanna be alone with Samantha a little."
                    $ lexi.love -= 2
                    $ sasha.love -= 2
                    hide lexi
                    hide sasha
                    call samantha_fuck_date_male from _call_samantha_fuck_date_3
    elif {"foursome_bree_minami_sasha"} & set(DONE) and from_girl in ["bree", "sasha", "minami"] and Harem.together(bree, sasha, minami, name="home") and all([(Room.has_tag(g.room, 'home') and not g.activity_name == "sleep" and not g.hidden and not g.flags.cheated) for g in [bree, minami, sasha]]):

        if from_girl == "bree":
            show sasha at left
            show bree
            sasha.say "Can I join in?"
            show minami at right
            minami.say "Can I join too?"
            menu:
                "Yes":
                    mike.say "That would be great."
                    call bj_bree_sasha_minami from _call_bj_bree_sasha_minami
                    call bree_minami_sasha_transition_bj_foursome from _call_bree_minami_sasha_transition_bj_foursome
                    call foursome_bree_minami_sasha from _call_foursome_bree_minami_sasha
                "I want some time with [bree.name] and Minami" if "threesome_bree_minami" in DONE:
                    mike.say "Sorry Sasha, I want some time with [bree.name] and Minami."
                    $ sasha.love -= 2
                    hide sasha
                    call bree_minami_threesome_intro from _call_bree_minami_threesome_intro
                "I want some time with [bree.name] and Sasha":
                    mike.say "Sorry Minami, I want some time with [bree.name] and Sasha."
                    $ minami.love -= 2
                    hide minami
                    call bree_sasha_threesome from _call_bree_sasha_threesome_1
                "I want to be alone with [bree.name]":
                    mike.say "Sorry, I wanna be alone with [bree.name] a little."
                    $ sasha.love -= 2
                    $ minami.love -= 2
                    hide sasha
                    hide minami
                    call bree_fuck_date_male from _call_bree_fuck_date_4
        elif from_girl == "sasha":
            show bree at left
            show sasha
            bree.say "Can I join in?"
            show minami at right
            minami.say "Can I join too?"
            menu:
                "Yes":
                    mike.say "That would be great."
                    call bj_bree_sasha_minami from _call_bj_bree_sasha_minami_1
                    call bree_minami_sasha_transition_bj_foursome from _call_bree_minami_sasha_transition_bj_foursome_1
                    call foursome_bree_minami_sasha from _call_foursome_bree_minami_sasha_1
                "I want some time with Sasha and Minami" if "threesome_sasha_minami" in DONE:
                    mike.say "Sorry [bree.name], I want some time with Sasha and Minami."
                    $ bree.love -= 2
                    hide bree
                    call minami_sasha_threesome_intro from _call_minami_sasha_threesome_intro
                "I want some time with Sasha and [bree.name]":
                    mike.say "Sorry Minami, I want some time with Sasha and [bree.name]."
                    $ minami.love -= 2
                    hide minami
                    call bree_sasha_threesome_2 from _call_bree_sasha_threesome_2_1
                "I want to be alone with Sasha":
                    mike.say "Sorry, I wanna be alone with Sasha a little."
                    $ bree.love -= 2
                    $ minami.love -= 2
                    hide bree
                    hide minami
                    call sasha_fuck_date_male from _call_sasha_fuck_date_6
        elif from_girl == "minami":
            show bree at left
            show minami
            bree.say "Can I join in?"
            show sasha at right
            minami.say "I wouldn't mind too!"
            menu:
                "Yes":
                    mike.say "That would be great."
                    call bj_bree_sasha_minami from _call_bj_bree_sasha_minami_2
                    call bree_minami_sasha_transition_bj_foursome from _call_bree_minami_sasha_transition_bj_foursome_2
                    call foursome_bree_minami_sasha from _call_foursome_bree_minami_sasha_2
                "I want some time with Minami and Sasha" if "threesome_sasha_minami" in DONE:
                    mike.say "Sorry [bree.name], I want some time with Minami and Sasha."
                    $ bree.love -= 2
                    hide bree
                    call minami_sasha_threesome_intro from _call_minami_sasha_threesome_intro_1
                "I want some time with Minami and [bree.name]" if "threesome_bree_minami" in DONE:
                    mike.say "Sorry Sasha, I want some time with Minami and [bree.name]."
                    $ sasha.love -= 2
                    hide sasha
                    call bree_minami_threesome_intro from _call_bree_minami_threesome_intro_1
                "I want to be alone with Minami":
                    mike.say "Sorry, I wanna be alone with Minami a little."
                    $ bree.love -= 2
                    $ sasha.love -= 2
                    hide bree
                    hide sasha
                    call minami_fuck_date_male from _call_minami_fuck_date_2
    elif from_girl in ["bree", "sasha"] and Harem.together(bree, sasha, name="home") and all([(Room.has_tag(g.room, 'home') and not g.activity_name == "sleep" and not g.hidden and not g.flags.cheated) for g in [bree, sasha]]):


        if from_girl == "bree":
            show sasha at left
            show bree at right
            sasha.say "Can I join in?"
            menu:
                "Yes":
                    mike.say "That would be great."
                    if game.flags.minamirefusedinhomeharem and not minami.flags.crash_threesome:
                        call minami_crash_threesome from _call_minami_crash_threesome_2
                    else:
                        call bree_sasha_threesome from _call_bree_sasha_threesome_3
                "No":
                    mike.say "Sorry, I wanna be alone with [bree.name] a little."
                    $ sasha.love -= 2
                    hide sasha
                    call bree_fuck_date_male from _call_bree_fuck_date_5
        elif from_girl == "sasha":
            show sasha at left
            show bree at right
            bree.say "Can I join in?"
            menu:
                "Yes":
                    mike.say "That would be great."
                    if game.flags.minamirefusedinhomeharem and not minami.flags.crash_threesome:
                        call minami_crash_threesome from _call_minami_crash_threesome_3
                    else:
                        call bree_sasha_threesome_2 from _call_bree_sasha_threesome_2_2
                "No":
                    mike.say "Sorry, I wanna be alone with Sasha a little."
                    $ bree.love -= 2
                    hide bree
                    call sasha_fuck_date_male from _call_sasha_fuck_date_7
    elif {"threesome_bree_minami"} & set(DONE) and from_girl in ["bree", "minami"] and Harem.together(bree, minami, name="home") and all([(Room.has_tag(g.room, 'home') and not g.activity_name == "sleep" and not g.hidden and not g.flags.cheated) for g in [bree, minami]]):
        if from_girl == "bree":
            show minami at left
            show bree at right
            minami.say "Can I join in?"
            menu:
                "Yes":
                    mike.say "That would be great."
                    call bree_minami_threesome_intro from _call_bree_minami_threesome_intro_2
                "No":
                    mike.say "Sorry, I wanna be alone with [bree.name] a little."
                    $ minami.love -= 2
                    hide minami
                    call bree_fuck_date_male from _call_bree_fuck_date_6
        elif from_girl == "minami":
            show minami at left
            show bree at right
            bree.say "Can I join in?"
            menu:
                "Yes":
                    mike.say "That would be great."
                    call bree_minami_threesome_intro from _call_bree_minami_threesome_intro_3
                "No":
                    mike.say "Sorry, I wanna be alone with Minami a little."
                    $ bree.love -= 2
                    hide bree
                    call minami_fuck_date_male from _call_minami_fuck_date_4
    elif {"threesome_sasha_minami"} & set(DONE) and from_girl in ["minami", "sasha"] and Harem.together(minami, sasha, name="home") and all([(Room.has_tag(g.room, 'home') and not g.activity_name == "sleep" and not g.hidden and not g.flags.cheated) for g in [minami, sasha]]):
        if from_girl == "minami":
            show minami at left
            show sasha at right
            sasha.say "Can I join in?"
            menu:
                "Yes":
                    mike.say "That would be great."
                    call minami_sasha_threesome_intro from _call_minami_sasha_threesome_intro_2
                "No":
                    mike.say "Sorry, I wanna be alone with Minami a little."
                    $ sasha.love -= 2
                    hide sasha
                    call minami_fuck_date_male from _call_minami_fuck_date_5
        elif from_girl == "sasha":
            show minami at left
            show sasha at right
            minami.say "Can I join in?"
            menu:
                "Yes":
                    mike.say "That would be great."
                    call minami_sasha_threesome_intro from _call_minami_sasha_threesome_intro_3
                "No":
                    mike.say "Sorry, I wanna be alone with Sasha a little."
                    $ minami.love -= 2
                    hide minami
                    call sasha_fuck_date_male from _call_sasha_fuck_date_8
    elif {"threesome_bree_lexi"} & set(DONE) and Person.is_not_hidden("lexi") and from_girl in ["bree", "lexi"] and Harem.together(bree, lexi, name="home") and all([(Room.has_tag(g.room, 'home') and not g.activity_name == "sleep" and not g.hidden and not g.flags.cheated) for g in [bree, lexi]]):
        if from_girl == "bree":
            show lexi at left
            show bree at right
            lexi.say "Can I join in?"
            menu:
                "Yes":
                    mike.say "That would be great."
                    call bree_lexi_threesome_intro from _call_bree_lexi_threesome_intro
                "No":
                    mike.say "Sorry, I wanna be alone with [bree.name] a little."
                    $ lexi.love -= 2
                    hide lexi
                    call bree_fuck_date_male from _call_bree_fuck_date_7
        elif from_girl == "lexi":
            show lexi at left
            show bree at right
            bree.say "Can I join in?"
            menu:
                "Yes":
                    mike.say "That would be great."
                    call bree_lexi_threesome_intro from _call_bree_lexi_threesome_intro_1
                "No":
                    mike.say "Sorry, I wanna be alone with Lexi a little."
                    $ bree.love -= 2
                    hide bree
                    call lexi_fuck_date_male from _call_lexi_fuck_date_3
    elif {"threesome_lexi_sasha"} & set(DONE) and Person.is_not_hidden("lexi") and from_girl in ["lexi", "sasha"] and Harem.together(lexi, sasha, name="home") and all([(Room.has_tag(g.room, 'home') and not g.activity_name == "sleep" and not g.hidden and not g.flags.cheated) for g in [lexi, sasha]]):
        if from_girl == "lexi":
            show lexi at left
            show sasha at right
            sasha.say "Can I join in?"
            menu:
                "Yes":
                    mike.say "That would be great."
                    call lexi_sasha_threesome_intro (from_event=False) from _call_lexi_sasha_threesome_intro
                "No":
                    mike.say "Sorry, I wanna be alone with Lexi a little."
                    $ sasha.love -= 2
                    hide sasha
                    call lexi_fuck_date_male from _call_lexi_fuck_date_4
        elif from_girl == "sasha":
            show lexi at left
            show sasha at right
            lexi.say "Can I join in?"
            menu:
                "Yes":
                    mike.say "That would be great."
                    call lexi_sasha_threesome_intro (from_event=False) from _call_lexi_sasha_threesome_intro_1
                "No":
                    mike.say "Sorry, I wanna be alone with Sasha a little."
                    $ lexi.love -= 2
                    hide lexi
                    call sasha_fuck_date_male from _call_sasha_fuck_date_9
    else:
        call expression f"{from_girl}_fuck_date_{hero.gender}" from _call_expression_230
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
