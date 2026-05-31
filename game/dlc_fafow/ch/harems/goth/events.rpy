init python:
    Event(**{
    "name": "goth_harem_event_01",
    "label": "goth_harem_event_01",
    "priority": 500,
    "music": "music/roa_music/reflection.ogg",
    "conditions": [
        IsHour(1, 5),
        IsDone("amy_event_07_date"),
        PersonTarget("amy",
                     MinStat("love", 170),
                     MinStat("sub", 30),
                     MinStat("sexperience", 3),
                     InHarem("goth"),
                     Not(IsPresent()),
                     ),
        HeroTarget(
            IsGender("male"),
            Not(OnDate()),
            Or(
                IsActivity("None"),
                IsActivity("sleep"),
                )
            ),
        ],
    "duration": 2,
    "do_once": True,
    })

    Event(**{
    "name": "goth_harem_event_02",
    "label": "goth_harem_event_02",
    "priority": 500,
    "music": "music/roa_music/reflection.ogg",
    "conditions": [
        IsHour(14, 18),
        IsDone("goth_harem_event_01"),
        PersonTarget("amy",
                     MinStat("love", 190),
                     MinStat("sub", 50),
                     MinStat("sexperience", 5),
                     InHarem("goth"),
                     Not(IsPresent()),
                     ),
        HeroTarget(
            IsGender("male"),
            IsActivity("None"),
            ),
        ],
    "duration": 2,
    "do_once": True,
    })

    Event(**{
    "name": "goth_harem_event_03",
    "label": "goth_harem_event_03",
    "priority": 500,
    "music": "music/roa_music/reflection.ogg",
    "conditions": [
        IsHour(14, 18),
        IsDone("goth_harem_event_02"),
        PersonTarget("amy",
                     MinStat("love", 200),
                     MinStat("sub", 90),
                     InHarem("goth"),
                     Not(IsPresent()),
                     ),
        HeroTarget(
            IsGender("male"),
            IsActivity("None"),
            ),
        ],
    "duration": 3,
    "do_once": True,
    })


label goth_harem_event_01:
    if "amy" not in hero.smartphone_contacts:
        $ hero.smartphone_contacts.append("amy")
    play sound cell_vibrate loop
    "I'm not expecting a call from anyone tonight, so it's surprise when my phone rings."
    "Even so I just go through my usual routine for the situation, I pull it out and check the caller ID."
    "Ninety nine times out of a hundred, this would be followed by me just ignoring the call."

    stop sound
    $ result = renpy.call_screen("smartphone_choice", "Amy")
    if not result:
        $ hero.cancel_event()
        $ amy.love -= 5
        return
    scene expression f"bg {game.room}" at dark with dissolve
    mike.say "Hey, Amy!"
    mike.say "What's up?"
    amy.say "Hi, [hero.name]..."
    amy.say "Are you doing anything right now?"
    "The question comes out of nowhere, throwing me off a little."
    "I was expecting there to be at least some small-talk."
    "Maybe the chance to chat about nothing in particular."
    "But instead Amy seems to want to get straight down to business."
    "Which is pretty intriguing in it's own right."
    mike.say "Erm..."
    mike.say "No, Amy..."
    mike.say "I guess not."
    amy.say "That's great..."
    amy.say "Then you can come over to my place, yeah?"
    "I'm about to go onto total autopilot and say yes."
    "But then something about all of this sets my sixth sense tingling."
    mike.say "I could, Amy."
    mike.say "If you'd tell me what this is all about?"
    "There's a pause on the other end of the line before Amy answers."
    amy.say "I can't tell you yet, [hero.name]."
    amy.say "All I can say is that I need your help to pull something off."
    amy.say "And if you do help, then I promise you it'll be totally awesome!"
    amy.say "So what do you say?"
    menu:
        "... Alright, I'm coming...":
            "Part of me thinks that I should say no on principle."
            "You know, to kind of teach Amy she can't just call and have me come running."
            "But that would require a version of me that's not totally into her."
            "And I'm very much under her dark, gothic spell right now!"
            mike.say "Okay, Amy..."
            mike.say "I'll be there as soon as I can."
            $ amy.love += 2
            amy.say "Great!"
            amy.say "I'll see you real soon."
            amy.say "And trust me, you won't be disappointed!"
            scene expression f"bg {game.room}" with dissolve
            "Amy ends the call, leaving me to make good on my promise."
            scene bg street at blur(16), dark with dissolve
            "So I don't waste any time in heading for Amy's place."
            scene bg black with dissolve
            scene bg amyhome
            show amy casual at center, zoomAt(1.5, (940, 1040))
            with wipeleft
            "As soon as I get there, she's waiting to let me in."
            amy.say "Hurry up and get in here, [hero.name]!"
            "I do as Amy says, stepping into her apartment."
            show amy shy at center, zoomAt(1.5, (1040, 1040)) with ease
            "But as I do so, I see that she's still looking around the door."
            mike.say "Is everything okay, Amy?"
            mike.say "You look like you're expecting someone else."
            show amy normal at center, zoomAt(1.5, (940, 1040)) with ease
            "Amy finally tears herself away from the door."
            "And she nods as she closes it behind her."
            hide amy
            show amy casual happy
            amy.say "That's because I am."
            amy.say "And she should be here any minute now!"
            mike.say "She?"
            "The mention of a friend interests me."
            "Even more so if the friend in question also happens to be a girl."
            show amy flirt
            amy.say "Yeah..."
            amy.say "Okay, [hero.name], cards on the table."
            amy.say "I have this friend called Violaine."
            amy.say "And I was telling her all about the things we've been getting up to."
            if "cemetery_threesome" in DONE:
                "The moment Amy mentions her friend's name, she has my full attention."
                "Because I know that I've heard that name before."
                "And in reference to a pretty hot goth girl too!"
                mike.say "Wait a minute, Amy..."
                mike.say "This Violaine girl..."
                mike.say "About this tall?"
                "I hold up my hand to show Amy the height I mean."
                show amy normal
                amy.say "Erm..."
                amy.say "Yeah, I guess."
                mike.say "Black bob hairdo?"
                amy.say "She does have a black bob."
                mike.say "Wears a black dress, red and black striped tights?"
                amy.say "Wait a minute..."
                show amy surprised
                amy.say "You know her too?!?"
                mike.say "Let's just say I've met her a couple of times."
                mike.say "And a few of those were...intimate encounters."
                if 'electronic_harem_event_05' in DONE:
                    mike.say "And you've been telling her about all the kinky stuff we did?"
                    amy.say "Pretty much, yeah."
                amy.say "And, well..."
                show amy normal
                amy.say "You see Violaine's not having much success with that kind of thing."
                amy.say "So...I kind of said we'd help her out!"
                amy.say "And if you already know her, then that makes it even easier, right?"
                "I find myself blinking and shaking my head."
                "Like I can't quite believe what Amy's telling me."
                mike.say "You mean like what, exactly?"
                mike.say "We sit her down and offer her some advice and pointers?"
                mike.say "Scrutinise her technique, or what?"
                mike.say "Because she didn't seem to have any issues when we last hooked-up!"
                amy.say "Oh no, [hero.name]..."
                show amy happy
                amy.say "I mean that we have a threesome with her!"
                "I'm kind of taken aback by how bold Amy's being about all of this."
                "A few moments ago I had no idea she and Violaine even knew each other."
                mike.say "And Violaine..."
                mike.say "She's on her way over right now?"
                show amy flirt
                "Amy begins to nod."
                amy.say "Yeah..."
                show amy surprised at startle
                play sound cell_vibrate
                "But then her phone chimes and she glances down at it."
                amy.say "Oops!"
                show amy happy at right with ease
                amy.say "Scrub that - she's here right now!"
                hide amy with easeoutright
                "I open my mouth to say something, I'm not sure what."
                "But Amy's already hurrying to the front door."
                "So all I can do is follow along in her wake."
                amy.say "Hey there, gothfriend..."
                amy.say "How are you doing?"
                violaine.say "Oh you know - pretty bad, actually!"
                violaine.say "My barely adequate psychic defences are crumbling."
                "I can only hear the conversation at first."
                "And that's because Amy and Violaine do that French kissy thing."
                "You know the one - where you lean in and pretend to kiss someone on each cheek?"
                "But you don't really touch them at all?"
                show amy casual zorder 1 at center, zoomAt(1.0, (440, 740))
                show violaine zorder 2 at center, zoomAt(1.0, (1140, 740))
                with easeinright
                "It's only when they pull back that I actually see Violaine."
                "And I get an instant hit of the thrill that I felt when I first saw her."
                "Because I guess I'd kind of forgotten just how hot Violaine really is."
                mike.say "Sweet Mother of Goth, Violaine..."
                mike.say "You're looking great!"
                "At the sound of my voice, Violaine looks directly at me."
                "And I can instantly tell that she recognises me too."
                show violaine at center, traveling(1.1, 1.0, (840, 840))
                "She steps into the apartment, walking straight towards me."
                violaine.say "Oh..."
                violaine.say "I had no idea you were the same [hero.name] I already knew!"
                mike.say "I guess it's a small world, Violaine!"
                mike.say "So Amy here tells me that..."
                "Before I can finish what I'm saying, Violaine holds up a single finger to silence me."
                show violaine at center, zoomAt(1.1, (740, 840)) with ease
                "Then she starts to walk around me in a circle."
                show violaine at center, zoomAt(1.1, (940, 840)) with ease
                "Almost like she's inspecting what she sees."
                violaine.say "Oh yes, Amy..."
                violaine.say "Now I know it's this [hero.name]..."
                violaine.say "I totally agree with your opinion that he's a fine specimen!"
                violaine.say "He's so sturdy, so athletic, so ruddy of complexion!"
                violaine.say "I bet he goes outside in the daytime on a regular basis."
                if hero.flags.gymmember:
                    show amy flirt
                    amy.say "I'll go one better than that, Violaine."
                    amy.say "He actually goes to the gym!"
                show violaine at center, zoomAt(1.0, (940, 840)), startle
                "Much to my surprise, Violaine gasps and clasps her hands together."
                "She acts almost like she just heard I was a genius."
                "Or at least like she heard I had a penis of record-breaking size."
                violaine.say "Oh, Amy..."
                violaine.say "I never even knew that about him before!"
                violaine.say "With such sweet meat, you really are spoiling me!"
                show violaine at center, traveling(1.5, 1.0, (840, 1040))
                "Violaine reaches up to stroke me under the chin."
                "Then she looks me straight in the eye."
                violaine.say "So, my pretty..."
                violaine.say "Will you have me a second time?"
                "I look from Violaine to Amy and back again."
                mike.say "You're both one hundred percent serious, right?"
                mike.say "There's no catch or part of the deal I don't know about?"
                mike.say "Just the three of us, together, having sex?"
                show amy normal
                "Amy and Violaine exchange a knowing glance."
                "And then they nod as one."
                mike.say "Then what are we waiting for?!?"
                show amy flirt at center, traveling(1.25, 1.0, (440, 920))
                show violaine at center, traveling(1.25, 1.0, (840, 960))
                "Amy and Violaine seem to take this as their cue to get things started."


                "I feel like that Harker guy in Dracula."
                "Being lead to my doom by his vampiric brides!"
                "Well, Amy and Violaine are pretty pasty - but I'm sure they're not actual vampires!"
                "Though I wouldn't mind letting them put certain parts of my anatomy in their mouths."
                "Maybe even have them bite me a little too!"


                "I let the girls begin to strip off my clothes."
                "Amy's done this before, and so she knows what to expect."
                "But with Violaine, it's another matter entirely."
                "I think she'd be literally tearing off my clothes."
                "That is if she thought she could get away with it!"
                "And every time they uncover a new piece of my body, she gasps at the sight."
                violaine.say "Oh, I forgot how his chest is hairy!"
                violaine.say "Ah, his hands are so strong!"
                violaine.say "Mmm...he has actual muscles!"
                "I look at Amy, confusion clearly written on my face."
                show amy normal
                amy.say "Her last boyfriend was a little...scrawny, yeah?"
                "I shrug and try to put it out of my mind."
                "Vincent's the last thing that I want to be dwelling on right now."
            else:
                "I'm instantly put a little on edge by Amy's confession."
                "The idea of her sharing that kind of information with her friends."
                if 'electronic_harem_event_05' in DONE:
                    mike.say "You mean the threesome and that kind of thing?"
                    amy.say "Pretty much, yeah."
                amy.say "And, well..."
                show amy normal
                amy.say "You see Violaine's not having much success with that kind of thing."
                amy.say "So...I kind of said we'd help her out!"
                "I find myself blinking and shaking my head."
                "Like I can't quite believe what Amy's telling me."
                mike.say "You mean like what, exactly?"
                mike.say "We sit her down and offer her some advice and pointers?"
                mike.say "Scrutinise her technique, or what?"
                amy.say "Oh no, [hero.name]..."
                show amy happy
                amy.say "I mean that we have a threesome with her!"
                "I'm staggered for a moment."
                "Totally unable to process what Amy just told me."
                mike.say "And this Violaine..."
                mike.say "She's on her way over right now?"
                show amy flirt
                "Amy begins to nod."
                amy.say "Yeah..."
                show amy surprised at startle
                play sound cell_vibrate
                "But then her phone chimes and she glances down at it."
                amy.say "Oops!"
                show amy happy at right with ease
                amy.say "Scrub that - she's here right now!"
                hide amy with easeoutright
                "I open my mouth to say something, anything at all."
                "Because I have the image of a hopeless goth girl appearing in the doorway."
                "Let's just say that Amy's brief description of her friend hasn't given me high hopes."
                "But it's way too late for me to be able to raise any kind of objections to the idea."
                "Let alone think of a way I could phrase it that wouldn't make me look like a total jerk!"
                "Amy's already opening the door again, which means Violaine is on the other side."
                "So all I can do is stand there with a grimace on my face."
                "Because I'm convinced that this Violaine girl's going to be a complete mess!"
                amy.say "Hey there, gothfriend..."
                amy.say "How are you doing?"
                violaine.say "Oh you know - pretty bad, actually!"
                violaine.say "My barely adequate psychic defences are crumbling."
                "I can only hear the conversation at first."
                "And that's because Amy and Violaine do that French kissy thing."
                "You know the one - where you lean in and pretend to kiss someone on each cheek?"
                "But you don't really touch them at all?"
                show amy casual zorder 1 at center, zoomAt(1.0, (440, 740))
                show violaine zorder 2 at center, zoomAt(1.0, (1140, 740))
                with easeinright
                "It's only when they pull back that I actually get a glimpse of Violaine."
                "And when I do, I feel like my jaw must have dropped open."
                "Because the girl standing there is drop-dead gorgeous!"
                "She's maybe a head or so taller than Amy and a little more slender."
                "Her (obviously) black hair is cut into a stylish bob."
                "And she has on a tight-fitting black dress with red and black striped stockings."
                mike.say "Sweet Mother of Goth!"
                "At the sound of my voice, Violaine looks directly at me."
                "And I can instantly tell that she's sizing me up too!"
                show violaine at center, traveling(1.1, 1.0, (840, 840))
                "She steps into the apartment, walking straight towards me."
                violaine.say "So..."
                violaine.say "You must be [hero.name], yes?"
                "I find myself nodding as I watch her approach."
                "And as she gets up close, I can't help taking a step backwards."
                mike.say "V...Violaine?"
                violaine.say "No, silly - that's me!"
                show violaine at center, zoomAt(1.1, (740, 840)) with ease
                "Violaine begins to walk around me."
                show violaine at center, zoomAt(1.1, (940, 840)) with ease
                "Almost like she's inspecting what she sees."
                violaine.say "Oh my, Amy..."
                violaine.say "You weren't kidding when you said he was a fine specimen!"
                violaine.say "He's so sturdy, so athletic, so ruddy of complexion!"
                violaine.say "I bet this one goes outside in the daytime on a regular basis."
                if hero.flags.gymmember:
                    show amy flirt
                    amy.say "I'll go one better than that, Violaine."
                    amy.say "He actually goes to the gym!"
                show violaine at center, zoomAt(1.0, (940, 840)), startle
                "Much to my surprise, Violaine gasps and clasps her hands together."
                "She acts almost like she just heard I was a genius."
                "Or at least like she heard I had a penis of record-breaking size."
                violaine.say "Oh, Amy..."
                violaine.say "With such sweet meat, you really are spoiling me!"
                show violaine at center, traveling(1.5, 1.0, (840, 1040))
                "Violaine reaches up to stroke me under the chin."
                "Then she looks me straight in the eye."
                violaine.say "So, my pretty..."
                violaine.say "Will you have me?"
                "I look from Violaine to Amy and back again."
                mike.say "You're both one hundred percent serious, right?"
                mike.say "There's no catch or part of the deal I don't know about?"
                mike.say "Just the three of us, together, having sex?"
                show amy normal
                "Amy and Violaine exchange a knowing glance."
                "And then they nod as one."
                mike.say "Then what are we waiting for?!?"
                show amy flirt at center, traveling(1.25, 1.0, (440, 920))
                show violaine at center, traveling(1.25, 1.0, (840, 960))
                "Amy and Violaine seem to take this as their cue to get things started."


                "I feel like that Harker guy in Dracula."
                "Being lead to my doom by his vampiric brides!"
                "Well, Amy and Violaine are pretty pasty - but I'm sure they're not actual vampires!"
                "Though I wouldn't mind letting them put certain parts of my anatomy in their mouths."
                "Maybe even have them bite me a little too!"


                "I let the girls begin to strip off my clothes."
                "Amy's done this before, and so she knows what to expect."
                "But with Violaine, it's another matter entirely."
                "I think she'd be literally tearing off my clothes."
                "That is if she thought she could get away with it!"
                "And every time they uncover a new piece of my body, she gasps at the sight."
                violaine.say "Oh, his hands are so strong!"
                violaine.say "Mmm...he has actual muscles!"
                "I look at Amy, confusion clearly written on my face."
                show amy normal
                amy.say "Her last boyfriend was a little...scrawny, yeah?"
                "I shrug and try to put it out of my mind."
            "After all, it's not like I have a problem with Violaine swooning over my body!"
            "But now it's their turn to strip-off."
            "And I sit down on the sofa to watch the show."
            show amy naked with dissolve
            "Pretty soon my eyes are going wide as Amy and Violaine get naked."
            "I don't think I've ever seen so much white flesh on show."
            "Or been so aroused by a couple of pale women before in my life!"
            "My arousal must be showing as well."
            "Because they're smiling down at me the whole time."
            call goth_harem_threesome_violaine_fuck from _call_goth_harem_threesome_violaine_fuck
            if renpy.has_label("goth_harem_achievement_1") and not game.flags.cheat:
                call goth_harem_achievement_1 from _call_goth_harem_achievement_1
        "Nah, I'll find something else to do, but thanks.":
            "Sure, I'm intrigued to see what Amy's cooking up at her place."
            "But I'm not into the whole idea of her calling me up like this."
            "Specifically thinking that she can have me come running anytime she likes."
            "Plus I don't want her to think she can keep me in the dark either."
            "So this time I'm going to have to say no in order to make that clear."
            mike.say "When I said I wasn't doing anything, Amy..."
            mike.say "What I actually meant is that I'm not doing anything right now."
            "When Amy responds to this, I can tell that she's a little surprised."
            amy.say "Really?"
            amy.say "You're sure about that?"
            amy.say "Because I wasn't lying when I said it'll be awesome."
            mike.say "Sorry, Amy..."
            mike.say "It sounds great, really it does."
            mike.say "But I can't cancel my plans."
            mike.say "Maybe I could help you out tomorrow instead?"
            amy.say "No, I don't think that'd work."
            amy.say "It kinda has to be right now."
            mike.say "Like I said already, sorry!"
            $ amy.love -= 3
            $ amy.sub -= 3
            $ Harem.leave_by_name("goth", "amy")
            amy.say "Okay, [hero.name], no worries."
            amy.say "Maybe Shawn can help me out instead..."
            mike.say "Sounds good, Amy..."
            mike.say "You do that!"
            scene expression f"bg {game.room}" with dissolve
            "With that, I end the call."
            "And I shake my head at Amy's presumption."
            "Well, maybe this will teach her a little lesson."
    return

label goth_harem_threesome_violaine_intro(appointment=None):
    scene bg black with dissolve
    scene bg amyhome
    show amy casual at center, zoomAt(1.0, (440, 740))
    show violaine at center, zoomAt(1.1, (940, 840))
    with ease
    "By the time I get to Amy's, Violaine's already there."
    "It's obvious they have a specific idea on how we'll spend our time together."
    "And I'm pretty sure it won't be a tea and biscuits affair."
    "How do I know?"
    show amy naked with dissolve
    "Well, Amy being already almost naked is a good hint."
    call goth_harem_threesome_violaine_fuck from _call_goth_harem_threesome_violaine_fuck_1
    return

label goth_harem_threesome_violaine_fuck:
    amy.say "Okay, [hero.name]..."
    amy.say "We're all ready to go!"
    violaine.say "So..."
    violaine.say "Where do you want us?"
    menu:
        "Fuck Violaine":
            "The promise of fucking Amy is always hard to resist."
            "But the sight of Violaine standing next to her does help to relieve it a little."
            "Just enough for me to be able to keep from instinctively reaching out for her."
            mike.say "I think we owe it to Violaine as the newcomer..."
            mike.say "To...you know...be the centre of attention?"
            "Violaine doesn't react to my suggestion straight away."
            "Instead she looks to Amy, as if seeking approval."
            show amy happy
            amy.say "Go ahead, Violaine."
            amy.say "We're about to have a threesome."
            amy.say "So I'm not about to get uptight about it!"
            "I stand up as Violaine walks over me."
            "And I gently guide her down."
            hide violaine
            hide amy
            show goth 3some violainefuck
            with fade
            "She kneels on the rug, her back to me."
            "I wrap my arms around Violaine's waist and step in closer."
            show goth 3some violainefuck mike
            "My chest and belly are against her back."
            "Her ass is pressed into my groin too."
            "I can feel her quivering with anticipation as I begin to touch her naked body."
            "And it doesn't take me long to discover that Violaine feels as good as she looks."
            mike.say "So you and Amy talked about what she got up to with me?"
            violaine.say "Y...yes."
            mike.say "And you liked the sound of it, huh?"
            show goth 3some violainefuck violaine_eyesclose
            violaine.say "Oh yes!"
            violaine.say "It really turned me on..."
            mike.say "And so you thought you'd like some of that for yourself?"
            show goth 3some violainefuck violaine_eyesopen
            violaine.say "I...I could hardly sleep for the thought of it."
            violaine.say "For the thought of how your cock would feel inside of me!"
            "Oh god!"
            "I'm trying really hard to be the one talking dirty here."
            "But Violaine's making me so hard it's insane!"
            violaine.say "And it feels SO hard right now!"
            "Violaine underlines her point by reaching around and taking hold of it."
            "And the squeeze that she gives it a moment later seals the deal."
            show goth 3some violainefuck headdown violaine_eyesclose
            "Without another word, I push Violaine forwards."
            "Not suddenly or with explosive force."
            "Just firmly enough for her to understand what I want."
            "Violaine obliges me by going down on all fours."
            "And that means I can make my next move."
            menu:
                "Fuck her pussy":
                    "Which is to grab a firm hold of her buttocks."
                    "And part them without pause or hesitation."
                    show goth 3some violainefuck violaine_eyesopen
                    "I hear Violaine gasp in surprise as I do this."
                    "But then she begins to lower herself even more."
                    "This spreads her thighs further apart."
                    "Which in turn makes getting between them even easier."
                    "Now I know for sure that Violaine is on the same page as me."
                    "And so I don't hesitate to do exactly what I have in mind."
                    "Pushing myself forwards, I aim the head of my cock precisely."
                    show goth 3some violainefuck violaine_eyesclose
                    "And I'm rewarded with the sensation of it brushing against Violaine's pussy."
                    "This time she doesn't gasp, but instead lets out a deep, sensual moan."
                    "But it's not only the sound Violaine's making that urges me on."
                    "It's the fact that I can instantly tell she's more than ready for me."
                    "Because I feel how hot and wet her pussy is right now."
                    "In fact she's so ready for it that I find I've miscalculated."
                    "I was anticipating the need to tease my way inside of Violaine."
                    "To have to coax her pussy into opening up for me."
                    "And so I wasn't being careful with the strength of my thrusts."
                    "So when the time comes, there's no pause or hesitation."
                    show goth 3some violainefuck headup vaginal
                    "Instead I find myself almost sliding straight into her!"
                    violaine.say "Mmmh..."
                    violaine.say "Oh yes..."
                    violaine.say "Please, put it inside of me!"
                    "Violaine's almost laid flat on the floor now."
                    "Her ass is up in the air with my sinking ever deeper into her."
                    "And I can already feel myself beginning to pick up speed."
                    "Violaine's head is bobbing up and down as she nods."
                    "It's moving in almost perfect sympathy to her ass too."
                    show goth 3some violainefuck headdown
                    "Suddenly I feel Violaine's body rise up."
                    "It's not like she's trying to stand."
                    "But she does rise up at least a foot from the rug."
                    "Puzzled by this, I glance down to see what's going on."
                    show goth 3some violainefuck amy
                    "And that's when I see Amy staring up at me from beneath Violaine!"
                    "In my hurry to have my way with her friend, I'd almost forgotten she was there!"
                    "But it doesn't look like Amy's about to ask my permission for anything."
                    show goth 3some violainefuck amy_eyesclose headup violaine_tongue
                    "As I watch her mouth open, and she starts to lick at Violaine's pussy."
                    "Of course she can't do anything but skirt around the edges."
                    "But all the same this seems to push Violaine to a whole new level."
                    "I'm not about to stop either."
                    "I keep trying to tell myself that we're all working together here."
                    "But I can't help feeling that Amy's in danger of stealing my thunder."
                    "So I redouble my efforts, and together we take Violaine to new heights."
                    show goth 3some violainefuck violaine_eyesahegao headdown -violaine_tongue
                    "She gasps, pants and then even begins to grunt."
                    "And it doesn't take a genius to figure out that she's about to reach her climax!"
                    menu:
                        "Cum inside":
                            "I hold onto Violaine as tightly as I can."
                            "Because I can already feel myself losing it too."
                            "One last thrust is all it takes, and then it happens."
                            show goth 3some violainefuck violaine_tongue headup cum amy_eyesopen with hpunch
                            "I shoot my load into her while I'm as deep as I can go."
                            with hpunch
                            "Violaine seems to stretch every muscle in her body at once."
                            show goth 3some violainefuck violaine_eyesclose headdown out -cum -violaine_tongue -amy with fade
                            "And then just as quickly they all go limp and she collapses onto the rug."
                            "Amy only just manages to roll out from under her before it happens."
                            "The taller girl landing beside her on the carpet."
                        "Pull out":
                            "I hold onto Violaine as tightly as I can."
                            "Because I can already feel myself losing it too."
                            "It takes all of my concentration and effort to do it."
                            show goth 3some violainefuck violaine_eyesopen out
                            "But some how I manage to pull out before it happens."
                            show goth 3some violainefuck cum with hpunch
                            "Then I shoot my load over her quivering buttocks."
                            with hpunch
                            "Violaine seems to stretch every muscle in her body at once."
                            show goth 3some violainefuck violaine_eyesclose -cum -amy with fade
                            "And then just as quickly they all go limp and she collapses onto the carpet."
                            "Amy only just manages to roll out from under her before it happens."
                            "The taller girl landing beside her on the floor."
                        "Leave it to the girls":
                            call goth_harem_event_01_bj from _call_goth_harem_event_01_bj
                "Fuck her ass":
                    "Which is to grab a firm hold of her buttocks."
                    "And part them without pause or hesitation."
                    show goth 3some violainefuck violaine_eyesopen
                    "I hear Violaine gasp in surprise as I do this."
                    "But then she begins to lower herself even more."
                    "This spreads her thighs further apart."
                    "Which in turn makes getting between them even easier."
                    "Now I know for sure that Violaine is on the same page as me."
                    "And so I don't hesitate to do exactly what I have in mind."
                    "Pushing myself forwards, I aim the head of my cock precisely."
                    show goth 3some violainefuck violaine_eyesclose
                    "And I'm rewarded with the sensation of it brushing against her hole."
                    "This time she doesn't gasp, but instead lets out a deep, sensual moan."
                    "But it's not only the sound Violaine's making that urges me on."
                    "It's the fact that I can instantly tell she's more than ready for me."
                    "Because I feel how she's pressing her ass into me right now."
                    "In fact she's so ready for it that I find I've miscalculated."
                    "I was anticipating the need to tease my way inside of Violaine."
                    "To have to coax her ass into opening up for me."
                    "And so I wasn't being careful with the strength of my thrusts."
                    "So when the time comes, there's no pause or hesitation."
                    show goth 3some violainefuck headup anal
                    "Instead I find myself almost sliding straight into her!"
                    violaine.say "Mmmh..."
                    violaine.say "Oh yes..."
                    violaine.say "Please, put it inside of me!"
                    "Violaine's almost laid flat on the floor now."
                    "Her ass is up in the air with my sinking ever deeper into her."
                    "And I can already feel myself beginning to pick up speed."
                    "Violaine's head is bobbing up and down as she nods."
                    "It's moving in almost perfect sympathy to her ass too."
                    show goth 3some violainefuck headdown
                    "Suddenly I feel Violaine's body rise up."
                    "It's not like she's trying to stand."
                    "But she does rise up at least a foot from the carpet."
                    "Puzzled by this, I glance down to see what's going on."
                    show goth 3some violainefuck amy
                    "And that's when I see Amy staring up at me from beneath Violaine!"
                    "In my hurry to have my way with her friend, I'd almost forgotten she was there!"
                    "But it doesn't look like Amy's about to ask my permission for anything."
                    show goth 3some violainefuck amy_eyesclose headup violaine_tongue
                    "As I watch her mouth open, and she starts to lick at Violaine's pussy."
                    "She's taking full advantage of the fact I chose to take the other girl up the ass."
                    "I can only see the briefest glimpses of Amy's tongue as it darts this way and that."
                    "And her efforts seem to push Violaine to a whole new level."
                    "I'm not about to stop either."
                    "I keep trying to tell myself that we're all working together here."
                    "But I can't help feeling that Amy's in danger of stealing my thunder."
                    "So I redouble my efforts, and together we take Violaine to new heights."
                    show goth 3some violainefuck violaine_eyesahegao headdown -violaine_tongue
                    "She gasps, pants and then even begins to grunt."
                    "And it doesn't take a genius to figure out that she's about to reach her climax!"
                    menu:
                        "Cum inside":
                            "I hold onto Violaine as tightly as I can."
                            "Because I can already feel myself losing it too."
                            "One last thrust is all it takes, and then it happens."
                            show goth 3some violainefuck violaine_tongue headup cum amy_eyesopen with hpunch
                            "I shoot my load into her while I'm as deep as I can go."
                            with hpunch
                            "Violaine seems to stretch every muscle in her body at once."
                            show goth 3some violainefuck violaine_eyesclose headdown out -cum -violaine_tongue -amy with fade
                            "And then just as quickly they all go limp and she collapses onto the carpet."
                            "Amy only just manages to roll out from under her before it happens."
                            "The taller girl landing beside her on the floor."
                        "Pull out":
                            "I hold onto Violaine as tightly as I can."
                            "Because I can already feel myself losing it too."
                            "It takes all of my concentration and effort to do it."
                            show goth 3some violainefuck violaine_eyesopen out
                            "But some how I manage to pull out before it happens."
                            show goth 3some violainefuck cum with hpunch
                            "Then I shoot my load over her quivering buttocks."
                            with hpunch
                            "Violaine seems to stretch every muscle in her body at once."
                            show goth 3some violainefuck violaine_eyesclose -cum -amy with fade
                            "And then just as quickly they all go limp and she collapses onto the carpet."
                            "Amy only just manages to roll out from under her before it happens."
                            "The taller girl landing beside her on the floor."
                        "Leave it to the girls":
                            call goth_harem_event_01_bj from _call_goth_harem_event_01_bj_1
        "Fuck Amy":
            "I have to admit that I get a thrill when I think about fucking Violaine."
            "It's the excitement of something new and as visibly hot as she is."
            "But there's still the part of me that's loyal to Amy and keen to let it show."
            "And that's what makes me turn to her when the choice between the two presents itself."
            show amy surprised blush
            "I stand behind Amy and wrap my arms around her waist, pulling her close to me."
            "She doesn't resist for a moment, but I can see that she's more than a little surprised."
            "I guess she was expecting me to go straight for Violaine."
            "But nobody ever said that was part of the deal here."
            show amy flirt
            "And it doesn't take Amy long to warm to the idea either."
            "Embracing her from behind, I lean in and begin to kiss her neck."
            "At the same time I make sure that she can feel how hard I am right now."
            "To begin with, Amy giggles a little nervously at my attention."
            "Probably worried that Violaine is being left out."
            "But as I start to push my cock between her thighs, a change comes over her."
            "Slowly and surely, Amy's giggles become gasps and moans of pleasure."
            "And I can feel her reservations begin to melt away."
            "I make a point of opening my eyes to see what's going on."
            "Which means I can see over Amy's shoulder for the first time."
            "Then my gaze falls on Violaine, who's standing in front of us."
            "She's watching with an obvious and intense interest."
            "And all the time one of her hands is playing with her pussy."
            "I want to say that it's Amy alone who's turning me on right now."
            "But that'd be a lie, because Violaine's making me sweat too!"
            "She seems to notice this and up her game further still."
            "Because the other hand rises to her breasts."
            "I watch as she squeezes one of them."
            "Then pinches her nipple until it becomes hard and erect."
            "Oh fuck..."
            "I can't tell you how badly I want that thing in my mouth!"
            "In an effort to shake off the feeling, I try to take back control."
            hide violaine
            hide amy
            show goth 3some amyfuck mike
            with fade
            "Tearing my eyes away from Violaine, I pull Amy down onto the rug with me."
            "We land in an untidy heap, but I don't give her a moment to recover."
            show goth 3some amyfuck mouthpleasure
            "Instead I flip Amy onto her side and close the distance between us."
            "I'm more than ready to take things to the next level."
            "And it feels like she's in the same place too."
            menu:
                "Fuck pussy":
                    "I reach down between Amy's thighs, my fingers exploring as I do so."
                    "I know exactly what I'm searching for and where to find it."
                    "And when my fingertips brush the edges of her pussy, I go for it."
                    "Amy moans helplessly as I stroke and caress the soft folds."
                    "I can almost feel her lips beginning to open as I do so."
                    "And my fingers are getting slicker by the moment too."
                    show goth 3some amyfuck eyespleasure mouthnormal
                    amy.say "[hero.name]..."
                    amy.say "Don't..."
                    amy.say "Don't tease me!"
                    "Almost without thinking, I act on Amy's plea."
                    "I thrust myself forwards, pushing my cock between her thighs."
                    "As soon as it touches the lips of her pussy, Amy makes her move."
                    "I feel her hand down there too, grabbing hold of the head."
                    show goth 3some amyfuck eyesahegao vaginal
                    "Without a second's pause, she pushes it hard against her pussy."
                    mike.say "Fuck..."
                    mike.say "Amy..."
                    mike.say "Slow down!"
                    "If she hears me at all, Amy chooses to ignore my pleas."
                    show goth 3some amyfuck eyesnormal
                    "Instead she pushes harder still, trying to force my cock into her."
                    "And the crazy thing is that it seems to be working!"
                    "I can already feel the resistance ebbing out of her muscles."
                    "A moment later the mere position we're in starts to have an effect."
                    "It's like I'm sinking into Amy without doing a thing!"
                    "Not happy with being so passive, I leap into action too."
                    "All it takes on my part is to begin pushing forwards."
                    "And then it just happens."
                    "All at once Amy's lips open to me."
                    "Which means there's nothing to keep me out anymore."
                    "The force I was intending to get me in there doesn't just disappear though."
                    show goth 3some amyfuck mouthhurt
                    "It means that I go all the way in, filling Amy in one smooth motion."
                    show goth 3some amyfuck eyespleasure
                    "She shudders in my arms from the sensation."
                    show goth 3some amyfuck mouthpleasure
                    "But there's only a couple of seconds for her to enjoy it."
                    "Because I'm not about to stop for anyone or anything."
                    "Thrusting back and forth, I soon get right up to speed."
                    "Which leaves Amy to lie back, helpless in my arms."
                    "All she can do is try to take what I'm giving her."
                    "And I'm determined to see just how much of it she can take."
                    show goth 3some amyfuck eyesahegao
                    "Suddenly a feel Amy stiffen in my arms and then relax."
                    "I know that it's not on account of anything I did to her."
                    "Because I can feel the effect that my motions are having."
                    "And that means there's someone else muscling in on the action."
                    "A quick glance over Amy's shoulder tells me that I'm right."
                    "Violaine isn't sitting back to watch the show."
                    show goth 3some amyfuck violaine
                    "Instead she's on the rug and exploring Amy's exposed body."
                    "Every possible part of her that can be touched and teased is getting her attention."
                    "Violaine also seems to know just what to do and where to go from one moment to the next."
                    "I can see her watching Amy intently, choosing where and when to touch the other girl."
                    "Her efforts don't get in the way of what I'm doing either."
                    "If anything, they seem to make it all the more intense."
                    "At first I think this is just going to make Amy cum that much quicker."
                    "But then I realise she's having the same effect on me too!"
                    show goth 3some amyfuck mouthhurt
                    amy.say "Oh fuck..."
                    amy.say "I can't...hold on..."
                    amy.say "I'm gonna cum!"
                    mike.say "Me..."
                    mike.say "Me too!"
                    menu:
                        "Cum inside":
                            "I'm too hopelessly lost to do anything but keep on going."
                            show goth 3some amyfuck mouthahegao cum with hpunch
                            $ amy.love += 4
                            "And so, with one last thrust, I shoot my load into Amy."
                            with hpunch
                            "She wriggles and writhes on my cock, cumming at the same time."
                            with hpunch
                            "All the while Violaine's hands are all over us."
                            "Caressing, squeezing and stroking."
                            "And her touch feels as much part of the climax as anything else."
                        "Pull out":
                            show goth 3some amyfuck eyespleasure out
                            "At the last moment I pull myself out of Amy."
                            "And as I do so, Violaine grabs hold of my cock."
                            "She squeezes it hard, making me gasp."
                            show goth 3some amyfuck cum mouthpleasure with hpunch
                            $ amy.love += 2
                            "Then I shoot my load, and it spurts over her fingers."
                            with hpunch
                            "At the same time, Amy wriggles and writhes, cumming in my lap."
                            with hpunch
                            "All the while Violaine's hands are all over us."
                            "Caressing, squeezing and stroking."
                            "And her touch feels as much part of the climax as anything else."
                        "Leave it to the girls":
                            call goth_harem_event_01_bj from _call_goth_harem_event_01_bj_2
                "Fuck her ass":
                    "I reach down between Amy's thighs, my fingers exploring as I do so."
                    "I know exactly what I'm searching for and where to find it."
                    "And when my fingertips find the tight sensation of her ass, I go for it."
                    "Amy moans helplessly as I stroke and caress the neat little hole."
                    "I can almost feel her muscles beginning to relax as I do so."
                    "And my fingers are getting deeper by the moment too."
                    show goth 3some amyfuck eyespleasure mouthnormal
                    amy.say "[hero.name]..."
                    amy.say "Don't..."
                    amy.say "Don't tease me!"
                    "Almost without thinking, I act on Amy's plea."
                    "I thrust myself forwards, pushing my cock between her thighs."
                    "As soon as it touches the edge of her ass, Amy makes her move."
                    "I feel her hand down there too, grabbing hold of the head."
                    show goth 3some amyfuck eyesahegao anal
                    "Without a second's pause, she pushes it hard against her hole."
                    mike.say "Fuck..."
                    mike.say "Amy..."
                    mike.say "Slow down!"
                    "If she hears me at all, Amy chooses to ignore my pleas."
                    show goth 3some amyfuck eyesnormal
                    "Instead she pushes harder still, trying to force my cock into her."
                    "And the crazy thing is that it seems to be working!"
                    "I can already feel the resistance ebbing out of her muscles."
                    "A moment later the mere position we're in starts to have an effect."
                    "It's like I'm sinking into Amy without doing a thing!"
                    "Not happy with being so passive, I leap into action too."
                    "All it takes on my part is to begin pushing forwards."
                    "And then it just happens."
                    "All at once Amy's ass opens to me."
                    "Which means there's nothing to keep me out anymore."
                    "The force I was intending to get me in there doesn't just disappear though."
                    show goth 3some amyfuck mouthhurt
                    "It means that I go all the way in, filling Amy in one smooth motion."
                    show goth 3some amyfuck eyespleasure
                    "She shudders in my arms from the sensation."
                    show goth 3some amyfuck mouthpleasure
                    "But there's only a couple of seconds for her to enjoy it."
                    "Because I'm not about to stop for anyone or anything."
                    "Thrusting back and forth, I soon get right up to speed."
                    "Which leaves Amy to lie back, helpless in my arms."
                    "All she can do is try to take what I'm giving her."
                    "And I'm determined to see just how much of it she can take."
                    show goth 3some amyfuck eyesahegao
                    "Suddenly a feel Amy stiffen in my arms and then relax."
                    "I know that it's not on account of anything I did to her."
                    "Because I can feel the effect that my motions are having."
                    "And that means there's someone else muscling in on the action."
                    "A quick glance over Amy's shoulder tells me that I'm right."
                    "Violaine isn't sitting back to watch the show."
                    show goth 3some amyfuck violaine
                    "Instead she's on the carpet and exploring Amy's exposed body."
                    "Every possible part of her that can be touched and teased is getting her attention."
                    "Violaine also seems to know just what to do and where to go from one moment to the next."
                    "I can see her watching Amy intently, choosing where and when to touch the other girl."
                    "Her efforts don't get in the way of what I'm doing either."
                    "If anything, they seem to make it all the more intense."
                    "At first I think this is just going to make Amy cum that much quicker."
                    "But then I realise she's having the same effect on me too!"
                    show goth 3some amyfuck mouthhurt
                    amy.say "Oh fuck..."
                    amy.say "I can't...hold on..."
                    amy.say "I'm gonna cum!"
                    mike.say "Me..."
                    mike.say "Me too!"
                    menu:
                        "Cum inside":
                            "I'm too hopelessly lost to do anything but keep on going."
                            show goth 3some amyfuck mouthahegao cum with hpunch
                            $ amy.sub += 2
                            "And so, with one last thrust, I shoot my load into Amy."
                            with hpunch
                            "She wriggles and writhes on my cock, cumming at the same time."
                            with hpunch
                            "All the while Violaine's hands are all over us."
                            "Caressing, squeezing and stroking."
                            "And her touch feels as much part of the climax as anything else."
                        "Pull out":
                            show goth 3some amyfuck eyespleasure out
                            "At the last moment I pull myself out of Amy."
                            "And as I do so, Violaine grabs hold of my cock."
                            "She squeezes it hard, making me gasp."
                            show goth 3some amyfuck cum mouthpleasure with hpunch
                            $ amy.sub += 1
                            "Then I shoot my load, and it spurts over her fingers."
                            with hpunch
                            "At the same time, Amy wriggles and writhes, cumming in my lap."
                            with hpunch
                            "All the while Violaine's hands are all over us."
                            "Caressing, squeezing and stroking."
                            "And her touch feels as much part of the climax as anything else."
                        "Leave it to the girls":
                            call goth_harem_event_01_bj from _call_goth_harem_event_01_bj_3
    $ amy.sexperience += 1
    return

label goth_harem_event_01_bj:
    "Before anyone can lose it, Amy and Violaine spring into action."
    "I don't know if they had this all planned out beforehand."
    "Or if what's happening is just spontaneous."
    scene bg black
    show goth 3some blowjob amyblow violaineblow
    with fade
    "But either way I find myself pulled to my feet."
    "Amy and Violaine kneel to either side of me."
    "And then they lean in, opening their mouths."
    "What follows is an almost perfect double blow-job."
    "The girls work as a team, using lips, teeth and tongues."
    show goth 3some blowjob amyblow -violaineblow with fade
    "First one of them takes it into her mouth for a moment."
    show goth 3some blowjob -amyblow violaineblow with fade
    "Then the other seamlessly takes over and moves things on."
    "I was already teetering on the edge of cumming a few moments before."
    "So now it doesn't take long for them to get me back there."
    show goth 3some blowjob high amyblow violaineblow with fade
    "Then they take me further."
    "Amy and Violaine seem to instinctively know when it's going to happen."
    show goth 3some blowjob normal
    "And they stop what they're doing just before, kneeling eagerly in front of me again."
    show goth 3some blowjob high with vpunch
    "They don't have to wait too long before I lost it, shooting my load over them both."
    show goth 3some blowjob low dickcum amyfacecum violainefacecum with vpunch
    "Cum spatters over Amy and Violaine's faces, tracing lines from one to the other."
    with vpunch
    "It runs down their cheeks until it reaches their mouths."
    "And they lick up all they can, swallowing it happily."
    return

label goth_harem_event_02:
    play sound cell_vibrate loop
    if "cemetery_threesome" in DONE:
        "The sensation of my phone ringing in my pocket distracts me from what I'm doing."
        "Without thinking I reach in there and pull it straight out, checking the caller ID."
        $ result = renpy.call_screen("smartphone_choice", "Amy")
        if not result:
            $ hero.cancel_event()
            $ amy.love -= 5
            return
        stop sound
        mike.say "Hey, Amy!"
        mike.say "How are you doing?"
        amy.say "Hey, [hero.name]..."
        amy.say "Not too bad, you know?"
        "I can't help smiling as a memory pops into my mind."
        "And I just have to drop it into the conversation."
        mike.say "And just what can I do for you today?"
        mike.say "Is Violaine wanting another ride on this train?!?"
        "Amy doesn't answer as quickly as I'm expecting her to."
        "In fact the other end of the line goes quiet."
        "Which leaves me regretting mentioning Violaine at all."
        mike.say "Ah..."
        mike.say "Sorry, Amy..."
        mike.say "Did I just say the wrong thing?"
        amy.say "Erm..."
        amy.say "No, [hero.name], it's not that."
        amy.say "I was as much up for the threesome we had with Violaine as you were."
        amy.say "But what I have to tell you does have something to do with it."
        amy.say "Or to be more specific, the fallout from it!"
        mike.say "Fallout?"
        mike.say "What's that supposed to mean?"
        mike.say "What happened was between three consenting adults."
        mike.say "So what are you even talking about?"
        "I hear Amy take a deep breath on the other end of the line."
        amy.say "It's not Violaine that's the problem."
        amy.say "It's Vincent."
        mike.say "Oh..."
        mike.say "I wondered when he was going to get in on the act too!"
        amy.say "Wait..."
        amy.say "You know Vincent too?"
        mike.say "Yeah, I met him when I met Violaine for the first time."
        mike.say "When you said her last boyfriend was kind of skinny..."
        mike.say "Well, I assumed that they'd broken up!"
        amy.say "Oh no, I meant the guys she was dating before Vincent."
        amy.say "But Violaine does have a thing for pale, skinny guys..."
        amy.say "So I can see how you might make that mistake!"
        "I laugh and shake my head."
        "Imagining Violaine going from one skinny goth guy to the next."
        amy.say "This is no joking matter, [hero.name]!"
        amy.say "When Vincent heard about what we did with Violaine, he was very upset."
        amy.say "He's an extremely sensitive person, and we're both worried about him."
        "Amy sounds totally serious, like she's not going to budge on this one."
        "So I let out a resentful sigh and resign myself to hearing her out."
        mike.say "Urgh..."
        mike.say "Okay, Amy, okay..."
        mike.say "What do I need to do in order to placate the jealous boyfriend?"
        mike.say "Do you goths like, I dunno, duel it out with swords or pistols?"
        amy.say "No, [hero.name], you don't understand."
        amy.say "Vincent's not jealous of you and me for sleeping with Violaine."
        amy.say "He's jealous of her for sleeping with US!"
        mike.say "Wait a minute..."
        mike.say "Are you trying to tell me that..."
        amy.say "Yes, [hero.name]..."
        amy.say "Vincent wants to sleep with us, just like Violaine did!"
        amy.say "He says that if we do that, everything will be cool."
        amy.say "Like, honour will be satisfied - or at least that's what he said."
        amy.say "So what do you say?"
        amy.say "Are you up for another threesome?"
        menu:
            "Why not...":
                "I seriously think about saying no to the request."
                "Because what am I supposed to be?"
                "Some kind of emergency sex-therapist for the goth community?"
                "But then it occurs to me that I'd like to see where all of this is going."
                "I mean, Violaine can't have been getting what she needed from Vincent."
                "Or else she'd never have come knocking on my door to satisfy her, would she?"
                "So it's not with a small amount of morbid curiosity that I give Amy my answer."
                mike.say "Ok, Amy - here's the deal."
                mike.say "I'll come over there and meet Vincent."
                mike.say "And if I get a good vibe off of him..."
                mike.say "Well, let's just say we'll see where it goes, yeah?"
                amy.say "Works for me."
                amy.say "Just get your ass over here pronto."
                amy.say "Okay?"
                mike.say "Okay."
                "Amy ends the call, which leaves me to make good on my promise."
                scene bg street with dissolve
                "On the way over there I can't help wondering what awaits me."
                "I mean, I had fun the last time I hooked up with Vincent and Violaine."
                "Even more fun when it was with Violaine and Amy."
                "But I don't know how inserting Vincent into that last encounter is going to turn out."
                scene bg street at blur(16), dark with dissolve
                play sound door_bell
                "Once I'm at Amy's place, I ring the door-bell."
                scene bg black with dissolve
                scene bg amyhome
                show amy casual
                with wipeleft
                "And she appears a few moments later to let me in."
                "Amy ushers me straight in and there's Vincent, as skinny and pale as I remember him."
                show amy at left5 with ease
                show vincent teaser at right5 with easeinright
                "At the moment he has his back turned to me, so all I can see his glossy, black hair."
                amy.say "[hero.name], you already know Vincent."
                amy.say "Vincent, aren't you going to say hello to [hero.name]."
                amy.say "Now you boys be nice to each other."
                mike.say "Erm..."
                mike.say "Hi, Vincent..."
                mike.say "Good to see you again, I guess!"
                "At the sound of my voice, Vincent spins around to face me."
                "And even though I know his face already, I still can't help flinching a little."
                "He's just so damn creepy-looking!"
                "Vincent" "Oh..."
                "Vincent" "Hello there, [hero.name]..."
                "Vincent" "Small world, isn't it?"
                amy.say "So..."
                show amy happy
                amy.say "That's all the pleasantries taken care of."
                show amy flirt
                amy.say "And we all know why we're here, right?"
                "I shrug and turn to Vincent."
                mike.say "Amy told me you were jealous of us hooking up with Violaine the other day."
                mike.say "And that you wanted some of that action for yourself?"
                "Vincent nods."
                "And he does something with his mouth that I guess passes for a smile."
                "Vincent" "In a nutshell, yes."
                "Vincent" "I'm not offended at Violaine having sex with you both."
                "Vincent" "I'm a very open-minded sort of chap myself."
                "Vincent" "It just didn't seem fair that she left me out."
                mike.say "Soo..."
                mike.say "How are we going to work this thing?"
                mike.say "I mean...is it going to be me doing you?"
                mike.say "Or the other way around?"
                "Vincent suddenly looks a little perturbed."
                show vincent at right with ease
                "He takes a step backwards and shakes his head."
                "Vincent" "Oh no!"
                "Vincent" "Don't get me wrong - I'm flattered and all that."
                "Vincent" "But I was more thinking one of us could have sex with Amy here!"
                mike.say "Works for me!"
                show amy happy at startle
                amy.say "Me too!"
                show amy normal zorder 1 at center, zoomAt(1.5, (480, 1020))
                show vincent at center, zoomAt(1.25, (840, 920))
                with hpunch
                "With that, Amy grabs us both by the hand."
                "And she leads us into her bedroom."
                "Vincent" "Ooh!"
                "Vincent" "Here we go."
                "Vincent" "Isn't this exciting?"
                mike.say "Yeah..."
                mike.say "I guess so..."
                show amy blush topless with dissolve
                "Once we're in her bedroom, Amy doesn't hesitate to take the lead."
                "Which is something I'm very grateful for."
                "She begins to strip off her clothes and motions for me to do the same."
                "For a moment, Vincent just stands there awkwardly."
                "Until Amy points to a screen in the corner of the room."
                amy.say "You can undress behind there, Vincent."
                "Vincent looks relieved at this."
                hide vincent with easeoutright
                "Then he nods and disappears behind it."
                "I give Amy a puzzled look."
                show amy flirt at center, zoomAt(1.5, (640, 1020)) with ease
                "But she just shrugs and shakes her head."
                amy.say "He's a little quirky, okay?"
                amy.say "Just go with it."
                "I do the best I can to ignore Vincent's eccentricities."
                show amy naked with dissolve
                "Instead I concentrate on watching Amy undress."
                "She seems to be pretty interested in doing the same to me."
                "And for a moment it almost feels like it's just the two of us."
                "Vincent" "Here I come - ready or not!"
                "I turn to see Vincent emerging from behind the screen."
                "And to my surprise, I find the weirdest thing about him is his pallor."
                "I mean seriously, the guy's as white as milk!"
                "But apart from that, everything else looks pretty normal."
                "Vincent" "Okay, chaps..."
                "Vincent" "How are we going to do this?"
                "Vincent" "Draw straws, flip a coin or something?"
                call goth_harem_threesome_vincent_fuck from _call_goth_harem_event_02_fuck_choice
            "I'm not interested in doing it with Vincent":
                "I can't actually believe that Amy's asking me that question."
                "Sure, I went through with the threesome when it was with Violaine."
                "But that was partly because I thought there would be no consequences."
                "And on a more shallow level, the fact she was a cute girl helped a lot!"
                "But now she wants me to do the same thing with Vincent?"
                "And all for the sake of his feelings being hurt?"
                mike.say "Nah, Amy..."
                mike.say "I think I'm gonna pass on this one!"
                amy.say "I won't lie, [hero.name]..."
                amy.say "I kind of thought you'd say that."
                amy.say "Won't you do it for me?"
                mike.say "No, Amy."
                mike.say "I'd do it WITH you."
                mike.say "But I'm not doing it with Vincent."
                amy.say "Even when you know how much it'll hurt him?"
                mike.say "I'm afraid so."
                mike.say "Who knows, maybe he can channel his pain?"
                mike.say "He could start a goth band or something."
                $ amy.love -= 5
                $ amy.sub -= 5
                $ Harem.leave_by_name("goth", "amy")
                "With that, I end the call."
                "Sure, it doesn't feel good to let Amy down."
                "But this thing with the goth threesomes was really starting to get out of hand."
    else:
        "The sensation of my phone ringing in my pocket distracts me from what I'm doing."
        "Without thinking I reach in there and pull it straight out, checking the caller ID."
        $ result = renpy.call_screen("smartphone_choice", "Amy")
        if not result:
            $ hero.cancel_event()
            $ amy.love -= 5
            return
        stop sound
        mike.say "Hey, Amy!"
        mike.say "How are you doing?"
        amy.say "Hey, [hero.name]..."
        amy.say "Not too bad, you know?"
        "I can't help smiling as a memory pops into my mind."
        "And I just have to drop it into the conversation."
        mike.say "And just what can I do for you today?"
        mike.say "Is Violaine wanting another ride on this train?!?"
        "Amy doesn't answer as quickly as I'm expecting her to."
        "In fact the other end of the line goes quiet."
        "Which leaves me regretting mentioning Violaine at all."
        mike.say "Ah..."
        mike.say "Sorry, Amy..."
        mike.say "Did I just say the wrong thing?"
        amy.say "Erm..."
        amy.say "No, [hero.name], it's not that."
        amy.say "I was as much up for the threesome we had with Violaine as you were."
        amy.say "But what I have to tell you does have something to do with it."
        amy.say "Or to be more specific, the fallout from it!"
        mike.say "Fallout?"
        mike.say "What's that supposed to mean?"
        mike.say "What happened was between three consenting adults."
        mike.say "So what are you even talking about?"
        "I hear Amy take a deep breath on the other end of the line."
        amy.say "It's not Violaine that's the problem."
        amy.say "It's Vincent."
        mike.say "And just who in the hell is he?"
        amy.say "He's Violaine's boyfriend, that's who."
        "A couple of things strike me in that moment."
        "And my brain struggles to process them all."
        mike.say "Okay, Amy..."
        mike.say "Point number one - nobody told me she had a damn boyfriend!"
        mike.say "And point two - Violaine and Vincent?"
        mike.say "Are you serious?!?"
        mike.say "Like, if I became a goth..."
        mike.say "And I wanted to keep dating you..."
        mike.say "Would I have to change my name to...I don't know, Adam?"
        amy.say "This is no joking matter, [hero.name]!"
        amy.say "When Vincent heard about what we did with Violaine, he was very upset."
        amy.say "He's an extremely sensitive person, and we're both worried about him."
        "Amy sounds totally serious, like she's not going to budge on this one."
        "So I let out a resentful sigh and resign myself to hearing her out."
        mike.say "Urgh..."
        mike.say "Okay, Amy, okay..."
        mike.say "What do I need to do in order to placate the jealous boyfriend?"
        mike.say "Do you goths like, I dunno, duel it out with swords or pistols?"
        amy.say "No, [hero.name], you don't understand."
        amy.say "Vincent's not jealous of you and me for sleeping with Violaine."
        amy.say "He's jealous of her for sleeping with US!"
        mike.say "Wait a minute..."
        mike.say "Are you trying to tell me that..."
        amy.say "Yes, [hero.name]..."
        amy.say "Vincent wants to sleep with us, just like Violaine did!"
        amy.say "He says that if we do that, everything will be cool."
        amy.say "Like, honour will be satisfied - or at least that's what he said."
        amy.say "So what do you say?"
        amy.say "Are you up for another threesome?"
        menu:
            "Why not...":
                "I seriously think about saying no to the request."
                "Because what am I supposed to be?"
                "Some kind of emergency sex-therapist for the goth community?"
                "But then it occurs to me that I'd like to see this guy for myself."
                "I mean, Violaine can't have been getting what she needed from him."
                "Or else she'd never have come knocking on my door to satisfy her, would she?"
                "So it's not with a small amount of morbid curiosity that I give Amy my answer."
                mike.say "Ok, Amy - here's the deal."
                mike.say "I'll come over there and meet this Vincent guy."
                mike.say "And if I get a good vibe off of him..."
                mike.say "Well, let's just say we'll see where it goes, yeah?"
                amy.say "Works for me."
                amy.say "Just get your ass over here pronto."
                amy.say "Okay?"
                mike.say "Okay."
                "Amy ends the call, which leaves me to make good on my promise."
                scene bg street with dissolve
                "On the way over there I can't help wondering what awaits me."
                "Maybe this Vicent guy will be the male equivalent of Violaine."
                "Like he'll totally confound my expectations and be a strapping muscle-guy."
                "But that really doesn't sound like the kind of guy that couldn't satisfy Violaine."
                scene bg street at blur(16), dark with dissolve
                play sound door_bell
                "Once I'm at Amy's place, I ring the door-bell."
                scene bg black with dissolve
                scene bg amyhome
                show amy casual
                with wipeleft
                "And she appears a few moments later to let me in."
                "Amy ushers me straight in and presents with a guy whom I presume must be Vincent."
                show amy at left5 with ease
                show vincent teaser at right5 with easeinright
                "At the moment he has his back turned to me, so all I can see his glossy, black hair."
                amy.say "[hero.name], this is Vincent."
                amy.say "Vincent, this is [hero.name]."
                amy.say "Now you boys say hello."
                mike.say "Erm..."
                mike.say "Hi, Vincent!"
                "At the sound of my voice, Vincent spins around to face me."
                if 'ayesha_event_03b' in DONE:
                    "And I find myself recognising him instantly."
                    mike.say "Hey, I know you!"
                    "Vincent" "Oh yes!"
                    "Vincent" "You're the chap that tried to stake me with a bamboo kebab skewer, aren't you?"
                else:
                    "And I find myself staring into a white face with huge eyes."
                    "The features are twisted into a grotesque grimace."
                    "And the figure's hands are held up in the air like a pair of pale claws."
                    mike.say "Fucking hell!"
                    "Vincent" "Do I amaze you?"
                    mike.say "Erm..."
                    mike.say "You could say that!"
                    "Vincent" "Don't worry about it."
                    "Vincent" "I tend to have that effect on first meeting people."
                show amy happy
                amy.say "That's the introductions all done with."
                show amy flirt
                amy.say "And we all know why we're here, right?"
                "I shrug and turn to Vincent."
                mike.say "Amy told me you were jealous of us hooking up with Violaine the other day."
                mike.say "And that you wanted some of that action for yourself?"
                "Vincent nods."
                "And he does something with his mouth that I guess passes for a smile."
                "Vincent" "In a nutshell, yes."
                "Vincent" "I'm not offended at Violaine having sex with you both."
                "Vincent" "I'm a very open-minded sort of chap myself."
                "Vincent" "It just didn't seem fair that she left me out."
                mike.say "Soo..."
                mike.say "How are we going to work this thing?"
                mike.say "I mean...is it going to be me doing you?"
                mike.say "Or the other way around?"
                "Vincent suddenly looks a little perturbed."
                show vincent at right with ease
                "He takes a step backwards and shakes his head."
                "Vincent" "Oh no!"
                "Vincent" "Don't get me wrong - I'm flattered and all that."
                "Vincent" "But I was more thinking one of us could have sex with Amy here!"
                mike.say "Works for me!"
                show amy happy at startle
                amy.say "Me too!"
                show amy normal zorder 1 at center, zoomAt(1.5, (480, 1020))
                show vincent at center, zoomAt(1.25, (840, 920))
                with hpunch
                "With that, Amy grabs us both by the hand."
                "Vincent" "Ooh!"
                "Vincent" "Here we go."
                "Vincent" "Isn't this exciting?"
                mike.say "Yeah..."
                mike.say "I guess so..."
                show amy blush topless with dissolve
                "Amy begins to strip off her clothes and motions for me to do the same."
                "For a moment, Vincent just stands there awkwardly."
                "Until Amy points to a screen in the corner of the room."
                amy.say "You can undress behind there, Vincent."
                "Vincent looks relieved at this."
                hide vincent with easeoutright
                "Then he nods and disappears behind it."
                "I give Amy a puzzled look."
                show amy flirt at center, zoomAt(1.5, (640, 1020)) with ease
                "But she just shrugs and shakes her head."
                amy.say "He's a little quirky, okay?"
                amy.say "Just go with it."
                "I do the best I can to ignore Vincent's eccentricities."
                show amy naked with dissolve
                "Instead I concentrate on watching Amy undress."
                "She seems to be pretty interested in doing the same to me."
                "And for a moment it almost feels like it's just the two of us."
                "Vincent" "Here I come - ready or not!"
                "I turn to see Vincent emerging from behind the screen."
                "And to my surprise, I find the weirdest thing about him is his pallor."
                "I mean seriously, the guy's as white as milk!"
                "But apart from that, everything else looks pretty normal."
                "Vincent" "Okay, chaps..."
                "Vincent" "How are we going to do this?"
                "Vincent" "Draw straws, flip a coin or something?"
                call goth_harem_threesome_vincent_fuck from _call_goth_harem_event_02_fuck_choice_1
            "Whoever it is I'm not interested":
                "I can't actually believe that Amy's asking me that question."
                "Sure, I went through with the threesome when it was with Violaine."
                "But that was partly because I thought there would be no consequences."
                "And on a more shallow level, the fact she was a cute girl helped a lot!"
                "But now she wants me to do the same thing with a goth guy?"
                "And all for the sake of his feelings being hurt?"
                mike.say "Nah, Amy..."
                mike.say "I think I'm gonna pass on this one!"
                amy.say "I won't lie, [hero.name]..."
                amy.say "I kind of thought you'd say that."
                amy.say "Won't you do it for me?"
                mike.say "No, Amy."
                mike.say "I'd do it WITH you."
                mike.say "But I'm not doing it with this Vincent guy."
                amy.say "Even when you know how much it'll hurt him?"
                mike.say "I'm afraid so."
                mike.say "Who knows, maybe he can channel his pain?"
                mike.say "He could start a goth band or something."
                $ amy.love -= 5
                $ amy.sub -= 5
                $ Harem.leave_by_name("goth", "amy")
                "With that, I end the call."
                "Sure, it doesn't feel good to let Amy down."
                "But this thing with the goth threesomes was really starting to get out of hand."
    return

label goth_harem_threesome_vincent_intro(appointment=None):
    call goth_harem_threesome_vincent_fuck from _call_goth_harem_threesome_vincent_fuck
    return

label goth_harem_threesome_vincent_fuck:
    menu:
        "Fuck Amy":
            "I shake my head as I reach out to take Amy's hand."
            mike.say "No need for that, Vincent."
            mike.say "You just follow my lead, okay?"
            "Vincent" "Oh..."
            "Vincent" "Alright then..."
            "Vincent" "If you think that's for the best!"
            "Amy offers no resistance as I walk her over to the floor."
            "And she's just as obedient when I guide her up and onto it."
            hide amy
            show goth 3some amydoggy mouth_smile
            with fade
            "Once she's on her hands and knees, we're ready for what comes next."
            "So I place my hands firmly on her hips."
            "And then I pull her backwards and onto me."
            menu:
                "Fuck her pussy":
                    "I almost forget that Vincent's in the room as I get started."
                    "Because all of my attention is focused on what's before me."
                    "Amy's buttocks are parted just enough for me to see what I want."
                    "And that's the enticing pink folds of her neat little pussy."
                    show goth 3some amydoggy eyes_pleasure
                    amy.say "Come on, [hero.name]..."
                    amy.say "What are you waiting for?"
                    show goth 3some amydoggy eyes_open
                    amy.say "Let's show Vincent what he's been missing out on!"
                    "As she says this, Amy pushes her ass hard against my groin."
                    "I was planning on teasing her a little."
                    "At least making her wait until I was good and ready."
                    "But instead, Amy pretty much forces my hand."
                    "Because it seems she's far more ready for this than I suspected."
                    show goth 3some amydoggy mouth_open eyes_pleasure
                    "I feel the tip of my cock slide along the lips of her pussy."
                    "And at the same time I can also feel them beginning to part."
                    show goth 3some amydoggy vaginal eyes_up
                    "Before it can go from one end to the other, the head slips inside."
                    "And as soon as it's in there, Amy's not going to let it get away!"
                    show goth 3some amydoggy eyes_open
                    "This all comes as a shock to me."
                    "One moment I feel like I'm the one in control."
                    "Like I'm making sure things are moving at my own pace."
                    "The next thing I know, the controlled motion is thrown off."
                    "And it means that I find myself balls deep in Amy a few seconds later."
                    "I maybe gasp and shake my head once."
                    "But then I realise that Vincent is watching my every move."
                    "And the look on his face is one of intense interest."
                    "Suddenly I can't stand the idea of him finding me wanting."
                    "So I renew my grip on Amy's haunches."
                    "My hands slap onto her thighs with an audible sound."
                    show goth 3some amydoggy eyes_up mouth_hurt
                    "And at the same time I pull back, then thrust myself into Amy."
                    "The effect on her is instant and dramatic."
                    "Before she was the one asserting herself."
                    "But now I'm the one setting the pace and she's struggling to keep up."
                    "My groin moves back and forth, going faster all the time."
                    show goth 3some amydoggy eyes_pleasure mouth_open
                    "Amy's head is nodding up and down as I'm doing this."
                    "And her entire body is swaying in time with my movements."
                    "Vincent" "Oh my goodness!"
                    "Vincent" "I can see what Violaine got out of this now."
                    "Vincent" "You two have such raw passion!"
                    "Vincent" "Such sheer, bohemian commitment!"
                    show goth 3some amydoggy mouth_smile
                    "Amy and I both look up at the same time."
                    "The sound of Vincent's voice bringing us back to reality."
                    mike.say "Amy..."
                    mike.say "Urgh..."
                    mike.say "Shut him..."
                    mike.say "Ah..."
                    mike.say "The fuck up!"
                    show goth 3some amydoggy eyes_open
                    "I can see that what I just said caught Vincent off-guard."
                    "And obviously he opens his mouth, probably to protest."
                    show goth 3some amydoggy vincent blowjob with hpunch
                    "But Amy moves quicker than he does, leaning forwards."
                    "I can't see what's happening from my point of view."
                    "Though I can guess, based on what's on the same level as her mouth."
                    show goth 3some amydoggy eyes_pleasure
                    "My suspicions are confirmed when her head starts to move back and forth."
                    "And when Vincent's eyes seem to roll back into his head."
                    "Now the only sounds he's making are moans of pleasure."
                    "Before we got into this situation, it's the last thing I'd have wanted to watch."
                    "Especially when I was well into the act of fucking Amy."
                    "But now I can feel myself getting ever more aroused as she goes to work on Vincent."
                    "Maybe part of that is because she seems to be almost synchronised with me."
                    "Every thrust I make, Amy mirrors it in how she's handling him."
                    "And pretty soon it feels like I'm almost controlling her actions!"
                    "In fact, it feels as though the whole thing is making me speed up."
                    "I'm going faster and the sensations are all the more intense."
                    "Pretty soon I feel like I can't hold on any longer!"
                    menu:
                        "Cum inside":
                            "Making sure to hold onto Amy as best I can, I just let go."
                            "This means that I make one last thrust into her, as deep as I can."
                            show goth 3some amydoggy eyes_up mikecum vincum with hpunch
                            $ amy.love += 4
                            "Then I shoot everything that I have inside of her."
                            with hpunch
                            "Oddly enough, Vincent seems to cum at the exact same time too."
                            show goth 3some amydoggy mouth_tongueout vindickcum -vincum with hpunch
                            "Which forces Amy to swallow at the same time as her own climax hits."
                            show goth 3some amydoggy eyes_pleasure out mikedickcum vaginaldrip -mikecum -blowjob
                            "She coughs and gags for a moment, then recovers and manages to gulp it down."
                            "All the while, Vincent and I look on in sheer amazement."
                        "Pull out":
                            show goth 3some amydoggy eyes_up out
                            "Making sure to hold onto Amy as best I can, I pull my cock out of her."
                            "She shudders and writhes from the unexpected sensation."
                            show goth 3some amydoggy mikecum vincum with hpunch
                            $ amy.love += 2
                            "Then I shoot everything that I have over her exposed ass."
                            with hpunch
                            "Oddly enough, Vincent seems to cum at the exact same time too."
                            show goth 3some amydoggy mouth_tongueout vindickcum -vincum with hpunch
                            "Which forces Amy to swallow at the same time as her own climax hits."
                            show goth 3some amydoggy eyes_pleasure out mikedickcum bodycum -mikecum -blowjob
                            $ amy.sub += 1
                            "She coughs and gags for a moment, then recovers and manages to gulp it down."
                            "All the while, Vincent and I look on in sheer amazement."
                "Fuck her ass":
                    "I almost forget that Vincent's in the room as I get started."
                    "Because all of my attention is focused on what's before me."
                    "Amy's buttocks are parted just enough for me to see what I want."
                    "And that's the enticing shape of her neat little ass."
                    show goth 3some amydoggy eyes_pleasure
                    amy.say "Come on, [hero.name]..."
                    amy.say "What are you waiting for?"
                    show goth 3some amydoggy eyes_open
                    amy.say "Let's show Vincent what he's been missing out on!"
                    "As she says this, Amy pushes her ass hard against my groin."
                    "I was planning on teasing her a little."
                    "At least making her wait until I was good and ready."
                    "But instead, Amy pretty much forces my hand."
                    "Because it seems she's far more ready for this than I suspected."
                    show goth 3some amydoggy mouth_open eyes_pleasure
                    "I feel the tip of my cock slide between her buttocks."
                    "And at the same time I can also feel the muscles beginning to surrender."
                    show goth 3some amydoggy anal eyes_up
                    "Before it can go from one end to the other, the head slips inside."
                    "And as soon as it's in there, Amy's not going to let it get away!"
                    show goth 3some amydoggy eyes_open
                    "This all comes as a shock to me."
                    "One moment I feel like I'm the one in control."
                    "Like I'm making sure things are moving at my own pace."
                    "The next thing I know, the controlled motion is thrown off."
                    "And it means that I find myself balls deep in Amy a few seconds later."
                    "I maybe gasp and shake my head once."
                    "But then I realise that Vincent is watching my every move."
                    "And the look on his face is one of intense interest."
                    "Suddenly I can't stand the idea of him finding me wanting."
                    "So I renew my grip on Amy's haunches."
                    "My hands slap onto her thighs with an audible sound."
                    show goth 3some amydoggy eyes_up mouth_hurt
                    "And at the same time I pull back, then thrust myself into Amy."
                    "The effect on her is instant and dramatic."
                    "Before she was the one asserting herself."
                    "But now I'm the one setting the pace and she's struggling to keep up."
                    "My groin moves back and forth, going faster all the time."
                    show goth 3some amydoggy eyes_pleasure mouth_open
                    "Amy's head is nodding up and down as I'm doing this."
                    "And her entire body is swaying in time with my movements."
                    "Vincent" "Oh my goodness!"
                    "Vincent" "I can see what Violaine got out of this now."
                    "Vincent" "You two have such raw passion!"
                    "Vincent" "Such sheer, bohemian commitment!"
                    show goth 3some amydoggy mouth_smile
                    "Amy and I both look up at the same time."
                    "The sound of Vincent's voice bringing us back to reality."
                    mike.say "Amy..."
                    mike.say "Urgh..."
                    mike.say "Shut him..."
                    mike.say "Ah..."
                    mike.say "The fuck up!"
                    show goth 3some amydoggy eyes_open
                    "I can see that what I just said caught Vincent off-guard."
                    "And obviously he opens his mouth, probably to protest."
                    show goth 3some amydoggy vincent blowjob with hpunch
                    "But Amy moves quicker than he does, leaning forwards."
                    "I can't see what's happening from my point of view."
                    "Though I can guess, based on what's on the same level as her mouth."
                    show goth 3some amydoggy eyes_pleasure
                    "My suspicions are confirmed when her head starts to move back and forth."
                    "And when Vincent's eyes seem to roll back into his head."
                    "Now the only sounds he's making are moans of pleasure."
                    "Before we got into this situation, it's the last thing I'd have wanted to watch."
                    "Especially when I was well into the act of fucking Amy."
                    "But now I can feel myself getting ever more aroused as she goes to work on Vincent."
                    "Maybe part of that is because she seems to be almost synchronised with me."
                    "Every thrust I make, Amy mirrors it in how she's handling him."
                    "And pretty soon it feels like I'm almost controlling her actions!"
                    "In fact, it feels as though the whole thing is making me speed up."
                    "I'm going faster and the sensations are all the more intense."
                    "Pretty soon I feel like I can't hold on any longer!"
                    menu:
                        "Cum inside":
                            "Making sure to hold onto Amy as best I can, I just let go."
                            "This means that I make one last thrust into her, as deep as I can."
                            show goth 3some amydoggy eyes_up mikecum vincum with hpunch
                            $ amy.sub += 2
                            "Then I shoot everything that I have inside of her."
                            with hpunch
                            "Oddly enough, Vincent seems to cum at the exact same time too."
                            show goth 3some amydoggy mouth_tongueout vindickcum -vincum with hpunch
                            "Which forces Amy to swallow at the same time as her own climax hits."
                            show goth 3some amydoggy eyes_pleasure out mikedickcum -mikecum -blowjob
                            "She coughs and gags for a moment, then recovers and manages to gulp it down."
                            "All the while, Vincent and I look on in sheer amazement."
                        "Pull out":
                            show goth 3some amydoggy eyes_up out
                            "Making sure to hold onto Amy as best I can, I pull my cock out of her."
                            "She shudders and writhes from the unexpected sensation."
                            show goth 3some amydoggy mikecum vincum with hpunch
                            $ amy.love += 2
                            "Then I shoot everything that I have over her exposed ass."
                            with hpunch
                            "Oddly enough, Vincent seems to cum at the exact same time too."
                            show goth 3some amydoggy mouth_tongueout vindickcum -vincum with hpunch
                            "Which forces Amy to swallow at the same time as her own climax hits."
                            show goth 3some amydoggy eyes_pleasure out mikedickcum bodycum -mikecum -blowjob
                            $ amy.sub += 1
                            "She coughs and gags for a moment, then recovers and manages to gulp it down."
                            "All the while, Vincent and I look on in sheer amazement."
            $ amy.sexperience += 1
        "Let Vincent go for it":
            "I gesture towards Amy as I look Vincent in the eye."
            mike.say "After you, Vincent."
            mike.say "We are doing this for your benefit."
            mike.say "So I think you should have the honour!"
            "Vincent looks more than a little surprised at my offer."
            "He casts his eyes over to Amy, as if looking for approval."
            "Her response is to raise an eyebrow and give him a nod."
            hide amy
            show goth 3some amyrevcow
            with fade
            amy.say "Works for me, Vincent."
            amy.say "So what are you waiting for, huh?"
            "Vincent" "Erm..."
            "Vincent" "I would."
            "Vincent" "But I think I'm having a little attack of the nerves!"
            show goth 3some amyrevcow vincent
            "With that, Amy seems determined to take charge."
            "He walks the short distance to where Amy is sitting."
            "And without warning, she grabs hold of his cock!"
            "Vincent gasps is surprise and probably not a little pain too."
            "But Amy doesn't stop for a moment."
            "Yanking on his manhood to keep him moving along the way."
            "Then she shoves him hard on the shoulder."
            show goth 3some amyrevcow onfloor with vpunch
            "This sends Vincent falling back onto the floor."
            "And now that she's got him where she wants him, Amy doesn't let up."
            "I watch as she literally pounces on Vincent."
            menu:
                "Wish Vincent would aim for her pussy":
                    "Vincent" "Oh my goodness..."
                    "Vincent" "I had no idea this would be so..."
                    "Vincent" "So energetic!"
                    "I have no idea if Amy is hearing a word Vincent says."
                    "And even if she does, she's choosing to ignore him."
                    "Instead she wastes no time in mounting him."
                    "Which pretty much means pinning him down on the floor!"
                    "She has hold of his cock again, with the same iron grip."
                    "And I can see that she's aiming it straight between her thighs."
                    show goth 3some amyrevcow mouth_hurt
                    amy.say "Okay, Vincent..."
                    amy.say "Let's see what you're made of!"
                    show goth 3some amyrevcow mouth_open
                    "Vincent lets out a strangled gasp as Amy goes to work on him."
                    "And to my ears it sounds like a strange mixture of pain and pleasure."
                    "What she's doing is definitely taking the guy well out of his comfort zone."
                    "But at the same time he's not doing anything to stop her."
                    "Though I have to admit, that might be out of fear!"



                    "As I'd expected, Vincent's manhood is as white as the rest of him."
                    "But even I have to admit that it's not too shabby in terms of actual size."
                    "Though I do feel a slight pang of jealousy as I watch Amy playing with it."
                    show goth 3some amyrevcow eyes_hurt
                    "She's rubbing the head against the lips of her pussy right now."
                    "And I can see them getting wetter and more slippery by the second."
                    call goth_harem_event_02_bj ("vaginal") from _call_goth_harem_event_02_bj
                "Wish Vincent would aim for her ass":
                    "Vincent" "Oh my goodness..."
                    "Vincent" "I had no idea this would be so..."
                    "Vincent" "So energetic!"
                    "I have no idea if Amy is hearing a word Vincent says."
                    "And even if she does, she's choosing to ignore him."
                    "Instead she wastes no time in mounting him."
                    "Which pretty much means pinning him down on the floor!"
                    "She has hold of his cock again, with the same iron grip."
                    "And I can see that she's aiming it straight between her thighs."
                    show goth 3some amyrevcow mouth_hurt
                    amy.say "Okay, Vincent..."
                    amy.say "Let's see what you're made of!"
                    show goth 3some amyrevcow mouth_open
                    "Vincent lets out a strangled gasp as Amy goes to work on him."
                    "And to my ears it sounds like a strange mixture of pain and pleasure."
                    "What she's doing is definitely taking the guy well out of his comfort zone."
                    "But at the same time he's not doing anything to stop her."
                    "Though I have to admit, that might be out of fear!"



                    "As I'd expected, Vincent's manhood is as white as the rest of him."
                    "But even I have to admit that it's not too shabby in terms of actual size."
                    "Though I do feel a slight pang of jealousy as I watch Amy playing with it."
                    show goth 3some amyrevcow eyes_hurt
                    "She's rubbing the head between the cheeks of her ass right now."
                    "And I can see it getting deeper by the second."
                    call goth_harem_event_02_bj ("anal") from _call_goth_harem_event_02_bj_1


    return

label goth_harem_event_02_bj(vinaim):
    "It's about then that I look up and notice that Amy's staring right at me."
    "Sure, she's still working on Vincent, but she's looking into my eyes."
    "Then I realise what's happening here."
    "Amy might be cool with letting Vincent fuck her."
    "But she's letting me know that I'm the one on her mind."
    "The whole time it's happening, she's going to be thinking of me!"
    show goth 3some amyrevcow eyes_close
    "Just then Amy closes her eyes and lets out a helpless moan of pleasure."
    "And I know before I cast my eyes downwards what's happening."
    $ renpy.show("goth 3some amyrevcow mouth_hurt " + vinaim)
    "Vincent starts to moan too his cock inches into Amy."
    "Little by little she slides down it and takes him inside her."
    "I risk a sideways glance at Vincent as all of this is happening."
    "His head is laid back and he looks totally out of it."
    show goth 3some amyrevcow eyes_open mouth_open
    "This means that as she begins to ride him, Amy is still looking at me."
    "Or to be more specific, she's looking down at my cock."
    "Of course it's good and hard by now, almost painfully so."
    "How could it not be?"
    "And it seems like it's captured Amy's interest."
    show goth 3some amyrevcow handjob
    "Without saying a word, she leans forwards."
    show goth 3some amyrevcow eyes_close
    "As she gets closer to it, Amy opens her mouth and closes her eyes."
    "I see her lips close around the head of my cock."
    show goth 3some amyrevcow blowjob
    "And just like that, I go from being a passive observer to an active participant."
    "Amy's head seems to somehow move independently from the rest of her body."
    "All the time she's going up and down as she keep on riding Vincent."
    "But her head is going at a totally different pace."
    "And it's one that suits what she's doing to me perfectly."
    "I can feel my breathing getting heavier, my heart starting to race."
    "Normally I'd be able to stand this for as long as Amy could keep it up."
    "But now I feel like she's releasing all of the built up tension in my body."
    "So that by the time Amy has my cock all the way into her mouth, I'm already starting to lose it!"
    menu:
        "Cum in her mouth":
            "Amy seems to be intent on keeping me in her mouth until the very end."
            "And that's not something I'm about to stop her from doing by any means."
            "If anything, she seems to take it deeper than ever towards the end too."
            show goth 3some amyrevcow eyes_up mikecum vincum with hpunch
            $ amy.love += 2
            "At the moment I lose it, I must be as far into her mouth as possible."
            with hpunch
            "Yet she still manages the whole thing with seeming ease."
            show goth 3some amyrevcow eyes_close with hpunch
            "Amy swallows every drop that I have to give, not gagging once."
            "Whereas I spend the time gasping and panting as if my life depended on it."
        "Cum on her face":
            "Amy seems to be intent on keeping me in her mouth until the very end."
            "But for some reason that's not how I want this whole thing to play out."
            show goth 3some amyrevcow mouth_tongueout eyes_open -blowjob
            "Which is why I pull my cock out of her mouth the moment before I lose it."
            "Amy gasps and looks surprised as it happens, but she doesn't protest."
            show goth 3some amyrevcow mikecum vincum eyes_close with vpunch
            $ amy.sub += 1
            "Not even when I lose it a moment later, spattering her face with sticky white lines."
            with vpunch
            "Instead she opens her mouth, trying to catch as much as she can."
            show goth 3some amyrevcow eyes_hurt facecum -mikecum with vpunch
            "Whereas I spend the time gasping and panting as if my life depended on it."
        "Cover her face with Vincent":
            "At the last possible moment, Amy seems to have a change of mind."
            "Or maybe this is what she was planning all along and just didn't tell anyone else."
            "Either way, Vincent and I find ourselves rudely pushed away from her."
            hide goth
            show goth 3some amydoubleblowjob mikeup vinup
            "And then, before we can even ask what's going on, Amy's kneeling on the floor."
            show goth 3some amydoubleblowjob rightnormal leftnormal
            "She grabs hold of us both, a cock held firmly in each hand."
            "Then she begins to work each cock in earnest."
            show goth 3some amydoubleblowjob rightpull leftpull
            pause 0.35
            show goth 3some amydoubleblowjob rightnormal leftnormal
            pause 0.35
            show goth 3some amydoubleblowjob rightpull leftpull
            pause 0.35
            show goth 3some amydoubleblowjob rightnormal leftnormal
            pause 0.35
            show goth 3some amydoubleblowjob rightpull leftpull
            pause 0.35
            show goth 3some amydoubleblowjob rightnormal leftnormal
            "They're treated to twin massages, the speed getting ever faster."
            "And she divides the attention of her mouth equally between them."
            "I'm amazed that she still has the stamina to pull this off."
            "Because it's clear that Vincent and I are on the verge of collapse."
            show goth 3some amydoubleblowjob rightpull leftpull
            pause 0.25
            show goth 3some amydoubleblowjob rightnormal leftnormal
            pause 0.25
            show goth 3some amydoubleblowjob rightpull leftpull
            pause 0.25
            show goth 3some amydoubleblowjob rightnormal leftnormal
            pause 0.25
            show goth 3some amydoubleblowjob rightpull leftpull
            pause 0.25
            show goth 3some amydoubleblowjob rightnormal leftnormal
            pause 0.25
            show goth 3some amydoubleblowjob rightpull leftpull
            pause 0.25
            show goth 3some amydoubleblowjob rightnormal leftnormal
            "That's why it's not long before we're both gasping and yelping."
            "Then Amy stops, preparing herself for the inevitable."
            "But I can see that she's smiling as she gets hit from both sides at once."
            show goth 3some amydoubleblowjob rightnormal leftnormal
            pause 0.15
            show goth 3some amydoubleblowjob rightpull leftpull
            pause 0.15
            show goth 3some amydoubleblowjob rightnormal leftnormal
            pause 0.15
            show goth 3some amydoubleblowjob rightpull leftpull
            pause 0.15
            show goth 3some amydoubleblowjob rightnormal leftnormal
            pause 0.15
            show goth 3some amydoubleblowjob rightpull leftpull
            pause 0.15
            show goth 3some amydoubleblowjob rightnormal leftnormal eyes_up mikecum vincum
            pause 0.15
            show goth 3some amydoubleblowjob rightpull leftpull
            pause 0.15
            show goth 3some amydoubleblowjob rightnormal leftnormal cumface mouthcum -mikecum -vincum with hpunch
            $ amy.love += 4
            $ amy.sub += 2
            "Vincent shoots his load onto one cheek and I do the same onto the other."
            with hpunch
            "Amy doesn't flinch for a moment, taking it all with a smile on her face."
            show goth 3some amydoubleblowjob mikedown vindown devil -rightnormal -leftnormal with hpunch
            "She stays still as it runs down her cheeks and dribbles off her chin."
            "A process that Vincent and I watch in sheer, helpless fascination."
    return

label goth_harem_event_03:
    play sound cell_vibrate
    "When my phone starts to ring, I can't help flinching just a little."
    "But I tell myself that it's probably nothing, and pull it out of my pocket."
    "Then I see that the call is from Amy, and I seriously consider ignoring it."
    "It's not that I'm pissed off with Amy herself, far from it."
    "The problem is that I keep getting pulled into kinky shit with her fellow goths."
    "Which was all fine and dandy when it involved a hot little number like Violaine."
    "But it started to wear a bit thin when I had to do the same thing for her boyfriend Vincent too!"
    $ result = renpy.call_screen("smartphone_choice", "Amy")
    if not result:
        $ hero.cancel_event()
        $ amy.love -= 5
        return
    "In the end I decide to take the call anyway."
    "Like I already said, none of that was really Amy's fault."
    "She was just trying to help out her friends."
    "So it wouldn't be fair for me to hold it against her."
    mike.say "Hey, Amy..."
    mike.say "How's it going?"
    amy.say "[hero.name]..."
    amy.say "You're not going to believe this..."
    "I jump in before Amy can even finish what she has to tell me."
    "I just can't help myself, because the mental image pops into my head."
    mike.say "Let me take a wild guess, Amy..."
    mike.say "Vincent and Violaine called you, right?"
    mike.say "And now they BOTH want to have sex with us?"
    "There's a protracted silence on the other end of the line."
    "And I can almost picture Amy's face as she tries to pull herself together."
    mike.say "I'm right, aren't I?"
    amy.say "Erm..."
    amy.say "Yeah, [hero.name], you are."
    amy.say "How in the hell did you know that?"
    mike.say "Amy, are you actually serious?"
    mike.say "How many times have you called me recently?"
    mike.say "Every time it's been to provide sexual relief to a goth friend of yours!"
    amy.say "Okay, okay..."
    amy.say "Point taken, [hero.name]."
    amy.say "But that doesn't answer the original question."
    amy.say "Are you up for a foursome with Vincent and Violaine, or what?"
    menu:
        "Yeah, sure...":
            "I open my mouth to say hell no."
            "But then I stop and actually think about it for a moment."
            "Violaine really is one hot Goth girl."
            "And I'd certainly love a chance to play around with her again."
            "Come to think of it, Vincent isn't all that bad either."
            "Once you get past the pallid complexion and make-up, that is."
            mike.say "Urgh..."
            mike.say "Okay, Amy..."
            mike.say "You wore me down."
            amy.say "So you'll do it?"
            mike.say "Yeah, I guess that I will."
            amy.say "That's great news!"
            "For a moment I think I hear something in the background."
            "A sound like whispering voices on Amy's end of the line."
            mike.say "Amy..."
            mike.say "Is there someone there with you?"
            amy.say "Erm..."
            amy.say "There might be..."
            "Vincent" "Hello, old chap!"
            violaine.say "So good of you to say yes!"
            "It sounds to me like Vincent and Violaine have just leaned in close to the phone."
            "So the whispering I heard must have been them, trying to listen in on the call!"
            mike.say "Wait a minute..."
            mike.say "If the two of them are with you right now..."
            mike.say "Then that must mean..."
            amy.say "Ah, yeah..."
            amy.say "Surprise, [hero.name]!"
            amy.say "They want to have the foursome as soon as possible."
            amy.say "Right now, if you can make it?"
            "I shake my head and take a deep breath."
            "But what choice do I really have here?"
            mike.say "Okay, okay..."
            mike.say "I'll be over there as soon as I can make it."
            "I'm as good as my word, heading out of the house as soon as I end the call."
            scene bg door black secure at center, zoomAt(1.0, (640, 720)) with fade
            "And it doesn't take me long to make it over to Amy's place."
            show bg door black secure at center, traveling(1.5, 0.3, (640, 1040))
            pause 0.3
            play sound door_knock
            pause 0.1
            scene bg amyhome
            show amy flirt casual
            show violaine at left
            show vincent teaser at right
            with wipeleft
            "She opens the door as soon as I knock."
            "Almost like she was waiting on the other side this whole time."
            mike.say "Hey, Amy."
            show amy flirt
            amy.say "Hey, [hero.name]..."
            amy.say "Come on in."
            amy.say "Vincent and Violaine are waiting for us in the bedroom."
            "Amy turns on her heel and walks in the direction of the bedroom."
            "And so I have no choice but to follow her."
            mike.say "Erm..."
            mike.say "So I guess that means we're getting straight down to it?"
            "It's only a short distance from the hallway to Amy's bedroom."
            "Which means we're pretty much entering the room as I say this."
            "So it shouldn't come as too much of a surprise that someone else answers me."
            "Vincent" "No point in standing on ceremony, is there?"
            violaine.say "We all know each other already, don't we?"
            amy.say "Plus we all know why we're here too."






            mike.say "Oh yeah..."
            mike.say "I know why we're here."
            "I start to take off my clothes as I say this, which seems to help."
            "Once I'm getting in on the act, it really doesn't feel as weird."
            "Plus there's an awful lot of delectable pale flesh on show."
            call goth_harem_foursome_vincent_violaine_fuck from _call_goth_harem_foursome_vincent_violaine_fuck
            if renpy.has_label("goth_harem_achievement_3") and not game.flags.cheat:
                call goth_harem_achievement_3 from _call_goth_harem_achievement_3
        "I'm tired of this shit... I pass.":
            "This time around I don't have to think about it for very long."
            "In fact the answer is already tripping off my tongue."
            mike.say "You know what, Amy..."
            mike.say "I think I'll pass this time."
            amy.say "Aw, [hero.name]!"
            amy.say "Are you serious?"
            mike.say "You know I really am."
            mike.say "A threesome with Violaine was fun."
            mike.say "I even had a strangely good time with Vincent."
            mike.say "But how many more people are we going to add to the mix?"
            "Amy lets out a sigh."
            "And I can picture her shaking her head too."
            amy.say "This is the last time, I promise!"
            amy.say "Come one, don't make me let my friends down."
            mike.say "What do you think I am, Amy?"
            mike.say "Some kind of stud for a Goth breeding program?!?"
            mike.say "Just tell them I'm not doing it, okay?"
            "I end the call before Amy can respond."
            "I know it's a cheap way to nope out on the situation."
            "But it's all that I can think to do in the heat of the moment."
            "Then I turn my phone off, just to be sure she can't call me back."
            "Sure, Amy might be pissed with me for a while."
            "But I'm sure she'll get over it in time."
            $ amy.love -= 5
            $ Harem.leave_by_name("goth", "amy")
    return

label goth_harem_foursome_vincent_violaine_intro(appointment=None):
    show bg door black secure at center, zoomAt(1.5, (640, 1040))
    pause 0.3
    play sound door_knock
    pause 0.1
    scene bg amyhome
    show amy flirt casual
    show violaine at left
    show vincent teaser at right
    with wipeleft
    "The door opens as soon as I knock."
    mike.say "Hey, Amy."
    show amy flirt
    amy.say "Hey, [hero.name]..."
    amy.say "Come on in."
    amy.say "Vincent and Violaine are waiting for us in the bedroom."
    "Amy turns on her heel and walks in the direction of the bedroom."
    violaine.say "Hey, [hero.name]..."
    "Vincent" "No point in standing on ceremony, is there?"
    violaine.say "We all know each other already, don't we?"
    amy.say "Plus we all know why we're here too."
    mike.say "Oh yeah..."
    mike.say "I know why we're here."
    "I start to take off my clothes as I say this, which seems to help."
    "Once I'm getting in on the act, it really doesn't feel as weird."
    "Plus there's an awful lot of delectable pale flesh on show."
    call goth_harem_foursome_vincent_violaine_fuck from _call_goth_harem_foursome_vincent_violaine_fuck_1
    return

label goth_harem_foursome_vincent_violaine_fuck:
    show goth 4some bj amy violaine with fade
    "Once we're all naked, Vincent sums up what we're all thinking."
    "Vincent" "So..."
    show goth 4some bj vinout vinhand with Dissolve(0.25)
    show goth 4some bj vinmid
    pause 0.2
    show goth 4some bj vinup
    pause 0.2
    show goth 4some bj vinmid
    pause 0.2
    show goth 4some bj vindown
    pause 0.2
    show goth 4some bj vinmid
    pause 0.2
    show goth 4some bj vinup
    pause 0.2
    show goth 4some bj vinmid
    pause 0.2
    show goth 4some bj vindown
    "Vincent" "Who does what to whom?"
    "I think about all the possible variations and combinations."
    "All the crazy shit we could get up two with four bodies involved."
    "It seems to me that we should really try to mix things up."
    "Like making things different will actually make it easier."
    menu:
        "Fuck Violaine":
            "I know it sounds kind of crazy, but the idea just takes hold."
            "And once it does, there's nothing I can do to shake it."
            mike.say "Oh, I think you know the answer to that one, Vincent!"
            show goth 4some bj mikeout mikehand with Dissolve(0.25)
            show goth 4some bj mikemid
            pause 0.175
            show goth 4some bj mikeup
            pause 0.175
            show goth 4some bj mikemid
            pause 0.175
            show goth 4some bj mikedown
            pause 0.175
            show goth 4some bj mikemid
            pause 0.175
            show goth 4some bj mikeup
            pause 0.175
            show goth 4some bj mikemid
            pause 0.175
            show goth 4some bj mikedown
            "Before Vincent can object, I reach out and take hold of Violaine."
            "I come up on her from behind, clapping my hands on her haunches."
            "This takes Violaine by surprise, making her jump."
            "And she lets out a yelp at the same time."
            violaine.say "Oh!"
            violaine.say "Oh, [hero.name]..."
            violaine.say "What ever are you going to do to me?"
            "Again I choose to let actions stand in place of words."
            scene bg black
            show goth 4some fuckviolaine violaine violaineeyes_closed
            with fade
            "Still holding onto Violaine's waist, I begin to lower myself to the floor."
            "She offers no resistance, letting herself be guided in that direction too."
            "I stop once I'm kneeling down, but I keep Violaine going a little lower."
            "Only letting her stop once she's down on all fours."



            "And she doesn't have to wait long to find out."
            "Because the moment I lean a little way forwards, my mind is made up."
            menu:
                "Fuck her pussy":
                    "The head of my cock slides along the lips of Violaine's pussy."
                    "In that moment I feel just how hot and wet she is down there."
                    show goth 4some fuckviolaine onviolaine
                    "And there's nothing I want more than to get inside of it!"
                    "Before I was just holding onto Violaine so that I could steer her downwards."
                    "But now my grip tightens, fingers sinking into the pale skin of her buttocks."
                    violaine.say "Mmm..."
                    show goth 4some fuckviolaine violaineeyes_normal
                    violaine.say "Don't torment me any longer, [hero.name]..."
                    violaine.say "Please, take me now!"
                    "I'm already beginning to thrust forwards as Violaine makes her plea."
                    show goth 4some fuckviolaine violaineeyes_closed
                    "So a moment later her words are replaced with a low, desperate moan."
                    "Her body tries to resist me for a few short seconds."
                    "But this is something she wants with an almost helpless desperation."
                    "And so it doesn't take long for me to feel things begin to relax."
                    "I'm not in the mood to take my time though."
                    "So every fraction of an inch Violaine gives me, I take without hesitation."
                    show goth 4some fuckviolaine mikevaginal violaineeyes_ahegao
                "Fuck her ass":
                    "The head of my cock slides between Violaine's buttocks."
                    "In that moment I feel just how hot she is down there."
                    show goth 4some fuckviolaine onviolaine
                    "And there's nothing I want more than to get inside of it!"
                    "Before I was just holding onto Violaine so that I could steer her downwards."
                    "But now my grip tightens, fingers sinking into the pale skin of her butt cheeks."
                    violaine.say "Mmm..."
                    show goth 4some fuckviolaine violaineeyes_normal
                    violaine.say "Don't torment me any longer, [hero.name]..."
                    violaine.say "Please, take me now!"
                    "I'm already beginning to thrust forwards as Violaine makes her plea."
                    show goth 4some fuckviolaine violaineeyes_closed
                    "So a moment later her words are replaced with a low, desperate moan."
                    "Her body tries to resist me for a few short seconds."
                    "But this is something she wants with an almost helpless desperation."
                    "And so it doesn't take long for me to feel things begin to relax."
                    violaine.say "Y...yes..."
                    violaine.say "Please, [hero.name]..."
                    violaine.say "Put it in my ass!"
                    "I'm not in the mood to take my time though."
                    "So every fraction of an inch Violaine gives me, I take without hesitation."
                    show goth 4some fuckviolaine mikeanal violaineeyes_ahegao
            "Soon enough I've made my way as deep as I can possibly go."
            "I pause just long enough to feel Violaine's muscles twitching around me."
            show goth 4some fuckviolaine violaineeyes_closed
            "Then I begin to thrust in and out of her without mercy."
            "Going ever faster with every second that passes."
            show goth 4some fuckviolaine amy with Dissolve(0.2)
            amy.say "Come on, Vincent."
            amy.say "Stop staring and move your pasty ass!"
            "Vincent" "Alright, alright..."
            "Vincent" "Keep your hair on!"
            $ renpy.show(f"goth 4some fuckviolaine amyeyes_closed {renpy.random.choice(['vinvaginal', 'vinanal'])}")
            "I can't help smiling as I look up to see Amy bossing Vincent around."
            "She's already laid on her back in front of him, legs spread apart."
            "And it looks like he's jumping to attention at her command."
            "I know just how hard he's going to have to work to impress her."
            "Because Amy will have been watching me fuck Violaine."
            "And she's probably feeling pretty jealous right now!"
            "The last time we did something like this, she got to share me with the other girl."
            "But now she's with somebody else entirely."
            "And her cajoling Vincent can only be on account wanting what Violaine's getting!"
            "I'm pretty sure that he can't see the smile on my face as I watch them."
            show goth 4some fuckviolaine amymouth_pleasure
            "But all the same, Amy's demands seem to spur him on."
            "His pale, rangy body begins to tense and flex."
            "And he has a look of sheer determination on his face too."
            "Before I know it, I'm watching Vincent pounding away at Amy."
            show goth 4some fuckviolaine amyeyes_ahegao amymouth_hurt
            "She happens to look up at that very second, our eyes meeting."
            "But then they begin to glaze over."
            show goth 4some fuckviolaine amyeyes_closed amymouth_pleasure
            "And then they roll back into her head completely."
            "Whatever Vincent's doing, it's working!"
            "Vincent" "Oh yes..."
            "Vincent" "Who's the patriarch of your family?"
            "Vincent" "It is I!"
            "Part of me wants to burst out laughing at the sight and sound of Vincent asserting himself."
            "But the part of me that wins out in the end is the one that wants to make the most of fucking Violaine."
            show goth 4some fuckviolaine violainetongue
            "So I turn my attention back to her and devote all of my energy to the task at hand."
            "In fact I'm so lost in it that I almost forget Violaine and I aren't alone."
        "Fuck Amy":
            "But then I get an idea that's pretty much the exact opposite."
            mike.say "No need to reinvent the wheel, Vincent."
            show goth 4some bj mikeout mikehand with Dissolve(0.25)
            show goth 4some bj mikemid
            pause 0.175
            show goth 4some bj mikeup
            pause 0.175
            show goth 4some bj mikemid
            pause 0.175
            show goth 4some bj mikedown
            pause 0.175
            show goth 4some bj mikemid
            pause 0.175
            show goth 4some bj mikeup
            pause 0.175
            show goth 4some bj mikemid
            pause 0.175
            show goth 4some bj mikedown
            mike.say "How about I do Amy and you do Violaine?"
            "Just to be sure, I turn to the girls before Vincent answers me."
            mike.say "Is that okay with you two?"
            "Amy and Violaine exchange a deep and meaningful glance."
            "Then they turn their heads back to me as one and offer up a nod."
            amy.say "Works for me."
            violaine.say "That would be acceptable."
            "Vincent" "I'm on aboard too."
            mike.say "Okay then..."
            mike.say "Let's get started."
            scene bg black
            show goth 4some fuckamy
            "I climb onto the sofa, pulling Amy down in front me at the same time."
            "She yelps in surprise, but doesn't resist and so ends up son all fours in front of me."
            show goth 4some fuckamy onamy
            "I don't waste any time in getting things underway, grabbing her haunches with both hands."
            "Amy responds in kind, pushing her ass backwards into me in the most pleasant way imaginable."
            "The first time I get the chance to look up, I see what Vincent and Violaine are up to."
            "Their approach seems to be somewhat more cautious."
            "Violaine is on all fours, facing Amy and me."
            "And Vincent is laid on the sofa beneath her."
            "They look like they're about to get it on for sure."
            "But it's impossible to miss the reality of the situation."
            "They're both watching Amy and me at the same time!"
            "Before this whole thing got started, I'd have been freaked out."
            "But we're way beyond that now, and so it kind of amuses me."
            "And I silently vow to give them something worth watching."
            "At almost the same moment, Amy reaches back to grab my cock."
            "Now it's my turn to gasp in surprise."
            menu:
                "Fuck her pussy":
                    show goth 4some fuckamy mikevaginal with hpunch
                    "Then I add a second gasp as she shoves it hard against her pussy."
                    amy.say "What are you waiting for?"
                    amy.say "Fuck me already!"
                    "Amy's demand gets my blood up in an instant."
                    "My hands are already around her waist."
                    "So all it takes is for me to pull her backwards even more sharply than before."
                    "I'm as hard as I can be by now."
                    "And it seems that she's more than ready for it herself."
                    "Because I only feel the smallest amount of token resistance down there."
                "Fuck her ass":
                    show goth 4some fuckamy mikeanal with hpunch
                    "Then I add a second gasp as she shoves it hard between her buttocks."
                    amy.say "What are you waiting for?"
                    amy.say "Fuck me already!"
                    "Amy's demand gets my blood up in an instant."
                    "My hands are already around her waist."
                    "So all it takes is for me to pull her backwards even more sharply than before."
                    "I'm as hard as I can be by now."
                    "And it seems that she's more than ready for it herself."
                    "Because I only feel the smallest amount of token resistance from her muscles back there."
            "I push harder and for a moment longer..."
            show goth 4some fuckamy forth amyeyes_ahegao
            amy.say "Oh..."
            amy.say "Oh fuck..."
            "And that's all it takes for me to sink into her."
            "I don't stop either, pulling Amy all the way down and onto me."
            show goth 4some fuckamy forth amyeyes_closed
            "She's pushing down at the same time too, grinding herself into me."
            "I'm expecting to begin thrusting upwards a few seconds later."
            "But instead, Amy takes me by surprise when she starts to move back and forth."
            show goth 4some fuckamy back
            pause 0.25
            show goth 4some fuckamy forth
            pause 0.25
            show goth 4some fuckamy back
            pause 0.25
            show goth 4some fuckamy forth
            pause 0.25
            show goth 4some fuckamy back vinvaginal violaineeyes_closed
            $ renpy.show(f"goth 4some fuckamy back violaineeyes_closed {renpy.random.choice(['vinvaginal', 'vinanal'])}")
            pause 0.25
            show goth 4some fuckamy forth
            pause 0.25
            show goth 4some fuckamy back
            pause 0.25
            show goth 4some fuckamy forth
            "Before I know it, she's riding my cock like her life depends on it."
            "And for a moment, all I can do is stand back and watch."
            "But a then I regain control of my senses."
            "And I start to thrust myself into Amy with renewed vigour."
            show goth 4some fuckamy violaineeyes_normal
            violaine.say "Like that, Vincent."
            violaine.say "Why aren't you fucking me like that?"
            "Vincent" "Alright, alright..."
            "Vincent" "Keep your hair on!"
            "I can't help smiling as I take the chance to look in their direction."
            "And I see that Vincent's already lined himself up beneath Violaine."
            "He looks like he's giving it his best effort."
            "But it doesn't seem to be enough to impress her yet."
            "Not after Violaine's seen what's happening to Amy right now."
            "I feel myself filling up with a vain sort of pride too."
            "Because I know that Violaine's been on the receiving end of my cock before."
            "So she can probably imagine what Amy's feeling as she rides it now."
            "And her cajoling Vincent can only be on account of feeling jealous!"
            "I don't know if he sees my smile or not."
            "But whatever the case, it does seem to light a fire under Vincent."
            show goth 4some fuckamy violaineeyes_closed
            "What passes for musculature on his body tenses and becomes tight."
            "There's a look of intense concentration, even determination on his face too."
            "At first it doesn't seem to make any difference."
            "But then I take a look into Violaine's eyes, and I can see it happening."
            show goth 4some fuckamy violaineeyes_ahegao
            "Little by little they begin to glaze over."
            "And then they roll back into her head completely."
            "Whatever Vincent's doing, it's working!"
            "Vincent" "Oh yes..."
            "Vincent" "Who's the patriarch of your family?"
            "Vincent" "It is I!"
            "Part of me wants to burst out laughing at the sight and sound of Vincent asserting himself."
            "But the part of me that wins out in the end is the one that wants to make the most of fucking Amy."
            "So I turn my attention back to her and devote all of my energy to the task at hand."
            show goth 4some fuckamy back
            pause 0.2
            show goth 4some fuckamy forth
            pause 0.2
            show goth 4some fuckamy back
            pause 0.2
            show goth 4some fuckamy forth
            pause 0.2
            show goth 4some fuckamy back
            pause 0.2
            show goth 4some fuckamy forth
            pause 0.2
            show goth 4some fuckamy back
            pause 0.2
            show goth 4some fuckamy forth
            pause 0.2
            show goth 4some fuckamy back
            pause 0.2
            show goth 4some fuckamy forth
            pause 0.2
            show goth 4some fuckamy back
            pause 0.2
            show goth 4some fuckamy forth
            "In fact I'm so lost in it that I almost forget Amy and I aren't alone."
    "Vincent" "Erm..."
    "Vincent" "[hero.name]..."
    mike.say "Yeah, Vincent?"
    "Vincent" "This is going to sound a little awkward."
    mike.say "We're talking during a foursome, Vincent..."
    mike.say "How could it be anything else?"
    "Vincent" "Oh yes..."
    "Vincent" "Point taken."
    "Vincent" "But still, I think I'm about to ejaculate!"
    mike.say "Yeah, Vincent..."
    mike.say "Me too!"
    "I have no idea what Vincent is thinking of suggesting."
    "And I've only the vaguest concept of an idea myself as to where this is going."
    "But luckily it's not left down to either of us to decide such things."
    "Because a moment later, Amy and Violaine take matters into their own hands."
    scene bg black
    show goth 4some bj amy mikeout amymouth_open
    with fade
    "Amy slides out from underneath and kneels down."
    show goth 4some bj violaine vinout violainemouth_open with dissolve
    "Violaine crawls free and does the same."
    "Then they position themselves in front of our now exposed cocks."
    show goth 4some bj vincum violaineeyes_closed with vpunch
    "Vincent loses it first emitting a weird groan and then exploding in Violaine's face."
    show goth 4some bj mikecum amyeyes_closed with vpunch
    "But I only have a moment to stare at the sight, as I cum within mere seconds too."
    show goth 4some bj amy_facecum violaine_facecum -vincum -mikecum with vpunch
    $ amy.love += 4
    $ amy.sub += 2
    "Amy takes mine full on in the face, cum spattering all over her cheeks, nose and mouth."
    "Violaine seems to have got pretty much the same treatment from Vincent too."
    show goth 4some bj amyeyes_normal violaineeyes_normal -mikeout -vinout
    "Then they lean in close, looking each other in the eye."
    "Their lips touch, and they begin to kiss, deeply and with genuine intent."
    "The cum mingles together on their lips, passing between them before being swallowed."
    "And all Vincent and I can do is look on in amazement."
    "Held still by the sight as we pant from sheer exhaustion."
    "Yet totally unwilling and unable to look away from as much as a second."
    $ amy.sexperience += 1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
