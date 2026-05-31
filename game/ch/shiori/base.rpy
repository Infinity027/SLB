init python:
    Event(**{
    "name": "shiori_give_phone_number",
    "label": "give_phone_number",
    "girl": "shiori",
    "conditions": [
        HeroTarget(IsGender("male")),
        PersonTarget(shiori,
            IsPresent(),
            Not(IsHidden()),
            Not(ContactKnown()),
            Not(IsActivity("sleep")),
            MinStat("love", 40),
            ),
        ],
    "chances": 25,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "shiori_send_text",
    "label": "send_text",
    "priority": 100,
    "conditions": [
        IsHour(19, 20),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        GameTarget(IsFlag("noTexting", False)),
        PersonTarget(shiori,
            Not(IsPresent()),
            Not(IsHidden()),
            ContactKnown(),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "fun": 1,
    "girl": "shiori",
    "chances": 10,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "shiori_auto_greet",
    "label": "auto_greet",
    "girl": "shiori",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsActivity("None")
            ),
        PersonTarget(shiori,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            IsFlag("greeted", False),
            MinStat("love", 50),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "shiori_auto_chat",
    "label": "auto_chat",
    "girl": "shiori",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            IsActivity("None"),
            ),
        PersonTarget(shiori,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            MinStat("love", 50),
            ),
        ],
    "chances": 10,
    "do_once": False,
    "once_day": True,
    })

    Event(**{
    "name": "shiori_are_you_sick",
    "label": "are_you_sick",
    "girl": "shiori",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("sleep")),
            IsFlag("sick"),
            ),
        PersonTarget(shiori,
            IsPresent(),
            Not(IsHidden()),
            Not(IsActivity("sleep")),
            ),
        ],
    "chances": (shiori, "love", 50),
    "do_once": False,
    "once_day": True,
    "quit": False,
    })

    Event(**{
    "name": "shiori_ask_out",
    "label": "ask_out",
    "girl": "shiori",
    "priority": 100,
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(IsActivity("ask_date"))
            ),
        PersonTarget(shiori,
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
    "name": "shiori_time_for_our_date",
    "label": "time_for_our_date",
    "priority": 100,
    "girl": "shiori",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            Not(IsActivity("sleep")),
            ),
        PersonTarget(shiori,
            IsPresent(),
            Not(IsHidden()),
            IsDateTime(),
            ),
        ],
    "chances": 50,
    "do_once": False,
    "once_day": True,
    })

    Event(**{
    "name": "shiori_first_date",
    "label": "shiori_first_date",
    "priority": 300,
    "conditions": [
        PersonTarget(shiori,
            OnDate()
            ),
        ],
    "do_once": True,
    "quit": False,
    })

label shiori_bye(bye_outfit=None):
    call npc_bye_outfit (npc=shiori, bye_outfit=bye_outfit) from _call_npc_bye_outfit_21
    $ (day, h, activity, bye_outfit) = _return
    if not activity == shiori.activity:
        if day != game.week_day:
            $ shiori.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, 2)
        else:
            $ shiori.flags[f"activity-{day}-{h}"] = TemporaryFlag(activity, "day")
        $ renpy.show(f"shiori {bye_outfit}")
        if activity["activity"] == "sleep":
            shiori.say "I should probably go to bed."
        elif activity["activity"] in ["shower", "bath", "brush", "pee", "wash"]:
            shiori.say "I'll go to the bathroom, don't you dare peeking!"
        elif activity["activity"] in ["work"]:
            shiori.say "I've got classes right now, I should probably get going."
        elif activity["activity"] in ["meal"]:
            shiori.say "I am so hungry..."
        elif activity["activity"] in ["tv"]:
            shiori.say "Do you know what is on TV right now?"
        elif activity["activity"] in ["drink"]:
            shiori.say "I'll go to the pub and have a drink, see ya."
        elif activity["activity"] in ["sunbath"]:
            shiori.say "It's sunny today, I think I'll go sunbath."
        elif activity["activity"] in ["shop"]:
            shiori.say "I feel like going shopping."
        elif activity["activity"] in ["read"]:
            shiori.say "I'll go read a book now, I started a pretty great one."
        elif activity["activity"] in ["dance"]:
            shiori.say "I am going to the club, I feel like partying."
        elif activity["activity"] in ["train"]:
            shiori.say "I kind of need to work a sweat, see you later."
        elif activity["activity"] in ["dress"]:
            shiori.say "I'll go get dressed."
        hide shiori
    return

label shiori_cheated(action, cheat_npc=None):
    show shiori
    "I see Shiori looking at me [action] someone else with envy and lust in her eyes."
    $ shiori.sub += 1
    hide shiori
    return

label shiori_greet:
    if renpy.has_label(f"shiori_greet_dialogues_{hero.gender}") and not shiori.flags.greeted:
        scene expression f"bg {game.room}"
        $ shiori.flags.greeted = TemporaryFlag(True, 1)
        show shiori
        $ result = randint(1, 3)
        if result == 1:
            shiori.say "Hello, [hero.name]."
        elif result == 2:
            shiori.say "Hi, [hero.name]."
        elif result == 3:
            shiori.say "Nice to see you [hero.name]."
        else:
            if game.hour < 12:
                shiori.say "Good morning [hero.name]."
            elif game.hour < 19:
                shiori.say "Good afternoon [hero.name]."
            else:
                shiori.say "Good evening [hero.name]."
        call expression f"shiori_greet_dialogues_{hero.gender}" from _call_expression_269
        if shiori.flags.submissive_interact:
            shiori.say "Moo...moo...mooooo - is it time to milk me yet, [hero.name]?"
        hide shiori
    return

label shiori_greet_dialogues_male:
    $ result = randint(1, 3)
    if result == 1:
        mike.say "Hello, Shiori."
    elif result == 2:
        mike.say "Hi."
    else:
        if game.hour < 6:
            mike.say "Hello."
        elif game.hour < 12:
            mike.say "Good morning Shiori."
        elif game.hour < 19:
            mike.say "Good afternoon Shiori."
        else:
            mike.say "Good evening Shiori."
    return

label shiori_kiss:
    if shiori.love + hero.charm < 80 and not shiori.is_girlfriend and not game.active_date.score >= 75:
        show shiori
        "I guess that I've been guilty of reading Shiori as nothing more than a passive little mouse ever since she arrived to work under me in the office."
        "She's always been so shy and retiring, unwilling to even speak up for herself that I suppose that fooled me into thinking that she was utterly passive."
        "On top of that there's also the fact that I'm ninety nine percent sure she keeps fucking up here and there on purpose, almost as if she were trying to get me mad at her."
        "All of that kind of lead me to think that she was going to be a complete pushover, a girl that I could pretty much pounce on at any moment, as soon as the mood took me."
        "That's what inspired me to just lean in when the mood took me just now and try to have an experimental kiss at Shiori's expense."
        "I'd assumed that she wouldn't have it in her to make the slightest objection."
        "And hey, who knew, maybe I'd get a real kick out of it and it could become a regular little distraction around the office whenever the mood took me."
        "But much to my surprise, Shiori actually yelps and dodges quickly out of the way before I can manage to kiss her."
        "She doesn't say a word, offering nothing in the way of an explanation as to just why she's chosen to reject my advances."
        "Instead she hurries well out of the range of any further clumsy attempts to plant one on her."
        "And I find myself scratching my head in puzzlement as she doesn't stop until she's safely within sight of another woman."
        hide shiori
    elif not shiori.flags.kiss:
        if shiori.lesbian > MAX_LES_GUY_SEX:
            $ shiori.lesbian -= 1
        hide shiori
        $ shiori.love += 5
        show shiori kiss
        "I've always known that Shiori was a timid sort of girl, shy and retiring to the point of being paralysed in a social situation or awkward moment."
        "So it's no surprise that, when turning around suddenly and finding her face no more than an inch or two from mine, she freezes instantly."
        "I don't know if she was trying to get closer in order to whisper something to me, or else it's just an accident of us both turning at the same time."
        "But the effect is like that of a deer caught in the headlights of a speeding car, scared rigid and unable to move, no matter the peril bearing down upon it."
        "I can hear Shiori's breathing to the exclusion of all else."
        "And I can only imagine that her heart must be racing right now, pounding in her chest."
        "I've never seen her up this close before, and I had no idea just how huge and expressive her eyes were."
        "They look to me like I could read the details of her most intimate thoughts written in them without her being able to stop me."
        "Without even thinking of what I'm actually doing, I lean in and kiss her full on the lips."
        "At first, Shiori doesn't move a muscle."
        "In fact she keeps so still and silent that I'm worried she's going to flip out and start screaming any second now."
        "But then I see something change in her eyes, and the lids slowly close, as if becoming suddenly too heavy to keep open a moment longer."
        "It's then that Shiori finally begins to return my kiss, becoming animated once more and then twining herself into me as if this is what she wanted all along."
        hide shiori kiss
        $ shiori.flags.kiss += 1
    else:
        hide shiori
        if shiori.lesbian > MAX_LES_GUY_SEX:
            $ shiori.lesbian -= 1
        $ shiori.love += 2
        show shiori kiss
        "While Shiori might have been slow to warm to the idea of me stealing kisses from her to begin with, she soon seems to warm to the idea."
        "Indeed the need to keep our kisses hidden and secret at first means that she begins to derive a subtle, yet growing thrill from such clandestine moments."
        "But she never takes the initiative, never chooses to be the one that seeks me out and makes the kind of furtive gestures that indicate the time has come for another liaison."
        "I start to think that she's almost as fond of the feeling of having me come and seek her out, as she is of the actual physical act itself."
        "All I need to do is give her the signal, and Shiori will come almost skipping to follow me."
        "And while she's certainly not the most impassioned of kissers, the way that she abandons herself to the experience is quite something in and of itself."
        "At times, Shiori has me more than half convinced that she actually enjoys being almost overpowered in this manner."
        "It's as if she finds release in the act of surrendering to me and allowing me to be the one in control, the one making all of the decisions."
        "I keep trying not to dwell on the matter too heavily, and instead remind myself of the fact that I'm having an immense amount of fun here."
        "And surely, if she wasn't enjoying it too, Shiori would have said something to that effect."
        "Wouldn't she?"
        hide shiori kiss
        $ shiori.flags.kiss += 1
        $ shiori.love += 1
    return

label shiori_first_date:
    show shiori
    "If having Shiori around the office to torment and discipline whenever the opportunity arose was some of the most enjoyable times I've ever had at work."
    "Then being out and about with her on a date something on a whole different level when it comes to getting pleasure out of her intimate company."
    "I'm sure every guy's fantasised about the image of a petite, demure little thing like Shiori, shy and submissive, yet with a body that could stop traffic."
    "I can see other guys (and even more than a few girls) casting their eyes over her as we spend the evening together."
    "But all the while, Shiori only has eyes for me, as she hurries along upon my arm, giggling at every joke I make and looking longingly into my eyes."
    "By the time we're in the taxi and heading back to my place, I'm already beginning to fall for her a little."
    "Don't get me wrong - I still can't wait to do something pleasantly filthy to her once we get into the bedroom."
    "It's just that she's so pretty, adorable and utterly attentive, that I can't help but enjoy having her doting on me, hanging upon my every word."
    "Back in the office, her habits of playing dumb when it suits her and trying to manipulate me can be irritating and rather tiresome."
    "But now that she's effectively got what she wants, and we're finally on a date together, she seems to be acting in what I hope is a more natural way."
    "Right now I'm finding that this version of Shiori is endearingly sweet and vulnerable, almost like a precious little porcelain doll."
    "Well, a sexy doll, that is - with rather large breasts and an ass that was just made to be spanked..."
    return


label shiori_propose_male:
    show shiori
    "I'm not used to feeling this nervous around Shiori, and it's a weird sensation."
    "Normally she's the one that's fretting and stressing over the impression she's making on me."
    "But today I'm a mess, with the weight of what I have to do pressing down on me the whole time."
    "Thankfully, Shiori doesn't seem to notice any difference in my mood."
    "She just keeps on shooting me smiles that make my heart leap inside of my chest."
    "And I guess that's why it's come to this - I can't get her out of my mind!"
    "So the only solution that I can think of is to ask her the question..."
    "I stand still and then kneel down on the spot without warning."
    "Shiori keeps on walking for a moment, but then realises that I've stopped."
    "She turns round, looking puzzled my unexplained course of action."
    "And then she sees what I have clutched in the palm of my hand."
    mike.say "Shiori..."
    mike.say "There's something that I have to ask..."
    show shiori embarrassed
    "I don't think I've ever seen Shiori's eyes as wide as they are right now."
    "Her hands are clasped together over her mouth as she gasps in surprise."
    "Undeterred, I hold up the ring that's been burning a hole in my pocket all day."
    mike.say "I love you, Shiori."
    mike.say "And I want you by my side - always!"
    mike.say "So...will you marry me?"
    "I can't help holding my breath as I wait for Shiori's answer."
    "And I'm leaning forward, urging her to speak..."
    if shiori.love < 195:
        show shiori annoyed
        shiori.say "I...I..."
        shiori.say "I can't marry you, [hero.name]!"
        shiori.say "It wouldn't be right."
        "Shiori begins to back away from me as she says this."
        "I shake my head desperately, almost crawling after her on my knees."
        mike.say "Why not, Shiori?"
        mike.say "I'm crazy for you."
        mike.say "And I thought you felt the same way too?!?"
        show shiori sad
        "Now Shiori's the one shaking her head."
        shiori.say "I do love you, [hero.name]."
        shiori.say "I really do!"
        shiori.say "But I'm damaged goods - I already ruined one marriage!"
        mike.say "That wasn't your fault, Shiori!"
        mike.say "We won't make the same mistakes either - I promise!"
        "For a moment I think that I'm getting through to Shiori."
        "And I feel a genuine burst of hope that I can talk her around."
        "But then she sets her face in a stubborn expression."
        shiori.say "No, [hero.name], you won't change my mind."
        shiori.say "I love you too much to let you marry me!"
        "All I can do is nod my head sadly."
        "That and stuff the ring back into my pocket."
        "But none of it stops me feeling sad and humiliated."
        $ shiori.love -= 25
        $ shiori.sub -= 25
    else:
        show shiori happy
        shiori.say "Y...you..."
        shiori.say "You really mean it?!?"
        mike.say "Of course I do, Shiori!"
        mike.say "You're the best thing that's ever happened to me."
        mike.say "The only thing that could make it better is if you agreed to be my wife!"
        "I can see that there are tears welling in the corner of Shiori's eyes."
        "It's almost like she can't believe this is actually happening."
        "But I'm not making it up - I really feel that way about her."
        shiori.say "Y...yes, [hero.name]."
        shiori.say "Of course I'll be your wife!"
        "Smiling broadly, I stand up and put the ring on Shiori's finger."
        "She all but collapses against me, wrapping her arms around my waist."
        "I can feel the soft, heavy sensation of her breasts pressing into me."
        "And it makes me feel instantly happy, satisfied and fulfilled."
        shiori.say "I...I'll try my hardest this time, [hero.name]."
        shiori.say "I promise that I'll be a better wife than I was the first time around!"
        mike.say "What you need is a better husband, Shiori."
        mike.say "One that makes you the centre of his world - like you should be."
        "Shiori clings to me even more tightly as my words sink in."
        "And I mean everything I say too."
        "I can't wait to begin building a life with Shiori."
        "I want to make her as happy as she deserves to be."
        $ shiori.set_fiance()
    hide shiori
    return

label shiori_work_with:
    $ random_event = randint(1, 6)
    if "shiori_meeting" in DONE and random_event == 1:
        scene shiori_stretch_bg
        "After some time of focused paperwork, muffled yawns start coming from across the desk."
        show shiori embarrassed
        shiori.say "Sorry [hero.name]."
        shiori.say "Kanta was up most of the night with a temperature."
        shiori.say "So I didn't get much sleep..."
        mike.say "Don't worry, let's take a break."
        "Shiori nods in agreement, but doesn't speak for the sake of a yawn I can see building up inside of her."
        hide shiori
        show shiori stretch
        "She stretches her back and pulls her arms back at the same time, as if trying to shake off her fatigue in one motion."
        "And I have to confess that I can't help staring at the effect all of this has on her considerable cleavage."
        "Maybe I should say something, but the sight of the buttons on Shiori's blouse straining under the pressure is quite remarkable!"
        "So much so that I find myself licking my lips unconsciously the whole time."
        "But then there's the sudden sound of something snapping or twanging."
        "And something else shooting across the room like a bullet!"
        show shiori stretch pop
        "Shiori is still sitting there, frozen in the same pose as before."
        "Her hands are crossed behind her head and her chest is thrust out."
        "The only difference is that I can now see most of her bra and a good portion of her heaving breasts too!"
        "It sounds crazy, like something out of a cheesy comedy skit."
        "But she actually did just pop the buttons down the front of her blouse!"
        "Shiori's face turns bright red as she slowly lowers her arms and pulls her blouse together."
        shiori.say "Oops..."
        shiori.say "That never happened before!"
        mike.say "Hum..."
        hide shiori stretch
        show shiori topless embarrassed
        shiori.say "I...I'm sorry..."
        mike.say "I guess we're stopping our work session now."
        mike.say "Just make yourself decent before leaving."
        $ shiori.love += 2
    elif "shiori_event_03" in DONE and random_event == 2:
        if "shiori_show_off_3" in DONE:
            call shiori_paper_fall (panties=False, plug=True) from _call_shiori_paper_fall
        elif "shiori_event_06" in DONE:
            call shiori_paper_fall (panties=False) from _call_shiori_paper_fall_1
        else:
            call shiori_paper_fall from _call_shiori_paper_fall_2
    else:
        scene workingwith
        show workingwith shiori
        "I help out Shiori with her work."
    return

label shiori_paper_fall(panties=True, plug=False):
    $ fall_outfit = " nopanties " if not panties else "" + " plug " if plug else ""
    "A massive headache strikes me in the middle of our work session."
    "Regarding the huge piles of paper on the desk, I think we've worked enough for today."
    mike.say "Shiori, I've got a huge headache. We're gonna stop there for now."
    mike.say "Can you put back the files in the closet?"
    show shiori happy
    shiori.say "Don't worry, [hero.name], I can handle it!"
    "I watch as Shiori gamely begins to scoop up the first armful of papers from one of the piles."
    "She struggles, but looks determined to succeed, even as the pile wobbles precariously."
    "And then it happens."
    $ renpy.show("shiori fall closed papers" + fall_outfit)
    "I don't know which comes first - if the pile collapses or she trips over her own feet."
    "Either way, the papers cascade to the floor and Shiori follows then down."
    "She lands on her hands and knees, already scrabbling to collect the papers scattered on the floor."
    "But as she falls, her skirt rides up her back, exposing her from the waist down."
    "Every motion she makes is visible as her buttocks wiggle."
    "Every inch of her curvy legs are on show, thighs calves and all."
    "The effort that she's putting into it means that her body is in almost constant motion."
    "And with a shape like that, there's a lot of her to get animated."
    $ renpy.show("shiori fall open papers" + fall_outfit)
    "Suddenly, Shiori stops moving and looks back over her shoulder at me."
    "Her face is bright red, eyes wide with embarrassment."
    "She grabs for the papers before her while desperately tugging her skirt back down."
    scene expression f"bg {game.room}"
    show shiori close blush
    shiori.say "Oh, [hero.name], I'm so sorry!"
    shiori.say "Whatever must you think of me?"
    "And then scuttles off with as many of the papers as she can carry."
    "I try as best I can to sit down, struggling the whole time with the effect Shiori's had on the contents of my pants..."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
