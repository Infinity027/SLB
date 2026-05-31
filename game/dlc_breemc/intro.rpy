label mc_selection_female:
    scene expression "gui/game_menu.png"
    if not renpy.variant( [ "touch", "android" ] ):
        show screen message(title="⚠️ WARNING ⚠️",what="Bree (our female protagonist) is very early beta and lacking in content right now you should start with Mike and enjoy his content first.{p}{p}Click to continue.")
    else:
        show screen message(title="⚠️ WARNING ⚠️",what="Bree (our female protagonist) is very early beta and lacking in content right now you should start with Mike and enjoy his content first.{p}{p}Touch to continue.")
    pause
    hide screen message
    call screen choose_sex
    $ sex_choice = _return
    if sex_choice == "male":
        $ heroname = "Mike"
        $ family_name = "Seeker"
        $ Person.find("mike").hide()
        $ starting_money = 500
    else:
        $ heroname = "Bree"
        $ family_name = "Cheese"
        $ Person.find("bree").hide()
        $ game.flags.female = 1
        $ starting_money = 200
        $ shiori.flags.schedule = "stripclub"
        $ hanna.flags.schedule = "stripclub"
        $ harmony.flags.schedule = "stripclub"
    return

label female_intro:
    $ IN_EVENT_WITH = "intro"
    $ game.room = "livingroom"
    scene bg coffeeshop
    $ quick_menu = True
    "The interior of the coffee shop is bustling and loud, like it always is near the end of a workday."
    "I can hardly hear it. My heart is pounding in my ears."
    "I'm lucky to find a seat in this clamor, but there's one open near the window, and I pull it out and flop my messenger bag onto the table, taking a long hard swig of my coffee."
    "It's too hot. It burns my tongue with that familiar immediate numbing feeling, and I try not to make a scene as I suck in a few quick puffs of cooling air before swallowing it down."
    "No time to dwell on it. I pull out my laptop and set it on top of my bag, swinging it open."
    "It brings up my login screen, prompting me for my name."
    "[hero.name]. That's me."
    "The webcam blinks for a second while the laptop scans my face, then the screen goes bright, opening up onto my desktop."
    "I click the browser immediately, impatiently tapping a fingernail against my touchpad while I wait for my laptop to finish waking up."
    "I'm done."
    "Finito."
    "I'd thought I'd been done for a while now, but I didn't know what truly, completely done felt like until today."
    "I have the worst roommate on the planet. Name something you've heard in threads of roommate horror stories, and mine has done it."
    "I'm almost completely convinced she's actually a goblin who's been seeking out my family for years to enact some centuries-old curse, and of course, she found me."
    "She's inhuman. This afternoon, after I finished brushing her actual toenail clippings off my bed after being stabbed by them when I flopped down onto what should have been my space..."
    "...my sanctuary, she had the nerve to step into my doorway, dripping toothpaste-y slobber onto my carpet while she brushed (at 3pm!) and casually reminded me that our lease is up and we should renew."
    "Good luck with that."
    "My browser window finally finishes loading, and I click the search bar and immediately type in 'available apartments' and my zipcode."
    "If there's anything -- anything at all -- available for me to GTFO as soon as possible, she's renewing that lease on her own."
    "In fact, even if there's nothing available at all, I'm considering a stint of homelessness just to be out of her immediate area. Forever."
    "I click a webpage when the results come up, my eyes falling immediately to the first, newest listing."
    "It's not an apartment at all, but a house for rent. Three bedrooms, yadda yadda, seeking two roommates, sure, and--"
    "Oh, wow."
    "I lean myself forward a little, though I've got near perfect vision, just to make sure I'm seeing that number right."
    "This might be the winner right off the bat. A house, no stomping upstairs neighbors, a pool, and the square-footage is definitely more than our current place... for that much?"
    "I whip my cell phone out of my pocket and dial the number listed, already hooked. I need some answers."
    play sound "<from 0 to 10>sd/SFX/phone/phone_calling.ogg"
    "A male's voice picks up after the second ring."
    ryan.say "Y'ello? This is Ryan. "
    bree.say "Hey! So I'm looking at the listing you put up, and I'm just wondering if this is, like, a typo or--?"
    ryan.say "Nope, not a typo."
    ryan.say "That'll be your rent, split three ways."
    ryan.say "It's a pretty sweet deal."
    "Yeah it is!"
    bree.say "Great! So do I, uh, like need to bring you guys anything, like a background check, or--"
    ryan.say "Nope, you sound great for the position already."
    "I'm not entirely sure what that means, but I'm a little too starstruck by the prospect of this place to dwell on it."
    ryan.say "Why don't you stop by and check the place out?"
    bree.say "Like, right now?"
    "I can tell that my voice has raised a pitch in my excitement, and for the briefest moment am aware of the fact that I'm being over-eager. But I cannot let this place pass me by. This is my salvation! I'm out!"
    ryan.say "Yeah, why not? You can swing by around uhh--"
    "There's a pause, where I assume he checks the time."
    ryan.say "Oh, around now, actually. [mike.name] should be ready to meet you by the time you're there."
    bree.say "Great! Perfect!"
    "I can feel a beaming, helpless grin across my face, and hope nobody's staring at me. Balancing my phone between my cheek and my shoulder, I snap my laptop closed and shove it away, gathering my bag back onto my shoulder."
    bree.say "I'll be right over then! Bye!"
    "My cellphone beeps in confirmation as I tap the end call button and lock it, shoving it into my bag and snatching my coffee before I turn and practically bolt out of the shop."
    scene bg street with fade
    "It's cold outside, and my breath puffs out before my lips as I alternate between a powerwalk and, admittedly, brief stints of giddy jogging on my way to the apartment."
    "Finally, breathing a little heavily from the exertion, I stop in front of a quaint, pretty house, letting my gaze trail up it to the gloomy evening sky."
    "My attention falls back to my phone screen, opened to a GPS page where my blinking blue dot is settled just beside the destination marker."
    "I can feel it already."
    scene bg house with fade
    "This is my new home. Excitement bubbles back up in my chest, and, flashing my best, beaming smile, I jog up the front steps, pressing the doorbell and waiting for my salvation to swing the door open."
    "But it... doesn't."
    "Doorbell must be broken. No prob. Been in a couple places like that."
    "Readjusting my bag onto my shoulder a little, I clear my throat and rap my knuckles against the door, calling out as clearly as I can."
    bree.say "Hey! I'm here about the rooms?"
    "Nothing."
    "My smile fades a bit as a minute passes, while I give them time to get to the door."
    "Maybe they're old, anyway. I immediately assumed they'd be my age, but they don't necessarily have to be. Maybe it's Ryan's grandpa or something, looking to fill some empty space?"
    "I leave enough time for even the creakiest of old men to get to their feet and waddle over to the door before I huff an exasperated breath and let my weak smile fade to a frown."
    "Maybe they're in the shower."
    "I lean on the doorbell a few times, trying to catch their attention, or wake them up."
    "After a few minutes, I double check my GPS, and the address, and match the map to the image on the real estate site... this is the place, I'm almost positive."
    "Plus, I feel it, deep in my bones. My new room is in there. I'll be waking up with beaming sunlight through my window and birds chirping and I'll be free and happy and far, far away from my current place and my current state."
    "This is the one. It has to be."
    "I don't know how long I spend alternating between the doorbell, yelling, and pounding my fist on the front door."
    "Probably an embarrassingly long time, honestly, before I finally consider that I should maybe call Ryan again."
    "I'm just desperate. I need this. I need it. I pound my fist one last time in frustration against the door, but before I can pull my phone back out to try calling Ryan a voice comes from behind me."
    mike.say "Can I help you?"
    "The frustration inside me that had been steadily bubbling into anger dissipates in an instant, and I whirl back to face the source of the voice."
    show mike work with dissolve
    "It's a young man, standing in clothing that says he just got off work. He blinks at me, which I take for confusion. Maybe he's a neighbor or something."
    bree.say "Oh, hey."
    "I adjust the strap of my bag again on my shoulder, propping a hand on my opposite hip."
    bree.say "You know who lives here? I'm supposed to meet them, but I don't think they're in."
    "He's quiet, for the briefest moments, as he seems to process what I've said."
    mike.say "Oh... That's me."
    "He makes his way down the front walk towards me, and hope thrills back up through my spine, immediately renewing the light to my eyes and the smile on my face."
    mike.say "You here for the place?"
    bree.say "Oh, yeah!"
    "I clear my throat to try to control my voice, at least to not sound so manic about it. Don't want to scare him off before I even get my foot in the door."
    bree.say "I'm [hero.name]. I take it you're [mike.name]?"
    show mike work at center, zoomAt(1.5, (640, 1040))
    "He reaches out his hand to give the formal greeting handshake, and I take it eagerly, giving it a firm, single shake while he sort of limply obliges, like he's still stuck trying to catch up to what's going on."
    "I wonder, briefly, if Ryan even told him I was stopping by, but don't dwell on it too much."
    mike.say "Yeah, that's me."
    "I decide to just carry the interaction for him. Poor guy might be tuckered from work."
    "That's fine. I've got the energy for both of us."
    bree.say "Nice to meet you!"
    "He gives a nod."
    mike.say "Likewise."
    "He reaches into his pocket and steps up beside me, and I move to allow him space to the front door as he pulls out a jingling set of keys."
    mike.say "Here, come on in. I'll show you around."
    hide mike with dissolve
    "I could dance through the doorway behind him, I'm so elated."
    "But I control myself, for now."
    scene bg livingroom with fade
    "When I'm behind the closed door of my bedroom, I can do all the dancing I need to. Just keep it together."
    bree.say "Wow."
    "I breathe, stepping past him and letting my gaze sweep across the room, taking it all in."
    bree.say "This place is pretty nice!"
    "I can picture myself, draped across that couch."
    "Playing video games on that TV."
    "This is it, for sure. No questions. This is home, sweet home. Ryan and his perfectly timed ad are my salvation, and this is paradise."
    "I whirl back around to face [mike.name] where he stands, still lingering near the doorway."
    "Ryan already said I was perfect, no further investigation needed, and even if it's maybe a little bit childish I take that as fact, speaking the next sentence through my eager smile."
    bree.say "When can I move in?"
    show mike work at right with dissolve
    "[mike.name] blinks at me a second, looking like he's reeling a bit from the whiplash."
    "Maybe I'm moving a little fast for him. But, hey, if he's going to be my roommate, he'd better learn to keep the hell up with me!"
    mike.say "Move in?"
    "He repeats."
    show mike work at right4 with move
    mike.say "I've known you for less than a minute!"
    "He seems to fumble a bit over his words, like he's trying to salvage something of normalcy out of this."
    mike.say "Should we, like, ask questions and get to know each other, or something?"
    bree.say "Okay, shoot."
    "[mike.name] hesitates again, obviously not ready to be put in that situation."
    "In attempt to lighten the mood a little bit, I giggle and bring my hands up into finger guns."
    bree.say "Hmm?"
    "I could feel the tension in the air, so I decided to lighten things up."
    bree.say "C'mon, Desperado."
    "I feign firing my guns at him, resisting the pew pew, though they sound in my head."
    mike.say "Then... Do you like sports?"
    if start_plus and all([(hero.has_skill(sport) or (hero.skills[sport].value and hero.skills[sport].value > 0)) for sport in ["martial_arts", "golf", "cooking", "dance", "shooting", "sneaky"]]):
        bree.say "Hehe, I'm not really the sporty type."
        $ hero.knowledge += 1
        $ hero.charm += 1
        $ hero.fitness += 1
        show mike happy
        mike.say "Same here. Music is more my thing."
    else:
        menu:
            "Martial Arts" if not start_plus or not (hero.has_skill("martial_arts") or (hero.skills["martial_arts"].value and hero.skills["martial_arts"].value > 0) ):
                bree.say "I do martial arts."
                $ hero.gain_skill("martial_arts")
                $ hero.fitness += 5
                show fx exclamation at right4
                mike.say "Oh, cool! You'll have to show me some moves sometime!"
            "Golf" if not start_plus or not (hero.has_skill("golf") or (hero.skills["golf"].value and hero.skills["golf"].value > 0) ):
                bree.say "I am an accomplished golfer."
                $ hero.gain_skill("golf")
                $ hero.charm += 4
                $ hero.fitness += 6
                show fx question at right4
                mike.say "Really? You don't seem like a golfer."
                bree.say "What, not a middle aged businessman in a suit?"
                mike.say "Exactly!"
                "I shake my head dramatically, before moving on."
            "Discreet" if not start_plus or not (hero.has_skill("sneaky") or (hero.skills["sneaky"].value and hero.skills["sneaky"].value > 0) ):
                bree.say "I am fucking sneaky."
                $ hero.gain_skill("sneaky")
                $ hero.charm += 10
                show fx question at right4
                mike.say "Really? You don't look like a ninja to me."
                bree.say "Pffff Ninjas are pretty noisy next to me?"
                mike.say "Cool!"
                "I shake my head dramatically, before moving on."
            "Cooking" if not start_plus or not (hero.has_skill("cooking") or (hero.skills["cooking"].value and hero.skills["cooking"].value > 0) ):
                bree.say "Does cooking count?"
                $ hero.gain_skill("cooking")
                $ hero.charm += 3
                $ hero.knowledge += 2
                mike.say "Cooking? Well, it's not really a sport..."
                show mike happy
                mike.say "But I'll forget about that if you make me something good!"
                "I can already tell he's going to be a handful."
            "Dancing" if not start_plus or not (hero.has_skill("dance") or (hero.skills["dance"].value and hero.skills["dance"].value > 0) ):
                bree.say "Not really, closest I get is dancing."
                $ hero.gain_skill("dance")
                $ hero.charm += 4
                $ hero.fitness += 6
                mike.say "How romantic."
            "Shooting" if not start_plus or not (hero.has_skill("shooting") or (hero.skills["shooting"].value and hero.skills["shooting"].value > 0) ):
                bree.say "I love shooting and guns."
                $ hero.gain_skill("shooting")
                $ hero.knowledge += 4
                $ hero.fitness += 6
                show fx drop at right4
                mike.say "..."
            "No, I don't":
                bree.say "Hehe, I'm not really the sporty type."
                $ hero.knowledge += 8
                $ hero.charm += 6
                $ hero.fitness += 6
                show mike happy
                mike.say "Same here. Music is more my thing."
    show mike normal
    mike.say "Then, how do you unwind?"
    mike.say "You gotta have a hobby or two to relax with."
    $ p = False
    menu:
        "Food" if not start_plus or not (hero.has_skill("foodie") or (hero.skills["foodie"].value and hero.skills["foodie"].value > 0) ):
            bree.say "I love food."
            $ hero.gain_skill("foodie")
            $ hero.fitness -= 3
            $ hero.charm += 3
            mike.say "As in cooking?"
            bree.say "No as in eating..."
            show fx exclamation at right4
            mike.say "Oh, cool! We should go for dinner sometimes!"
        "Video Games" if not start_plus or not (hero.has_skill("video_games") or (hero.skills["video_games"].value and hero.skills["video_games"].value > 0) ):
            bree.say "I play a lot of video games."
            $ hero.gain_skill("video_games")
            $ hero.knowledge += 5
            show mike happy
            mike.say "Oh, nice! We should play together sometimes!"
        "Fitness":
            bree.say "I love running and working out."
            $ hero.fitness += 20
            show mike happy
            mike.say "I could guessed that."
            "I strike a heroic pose, which draws a laugh out of [mike.name]."
            "Maybe he won't be so bad after all, he seems like fun."
            show mike normal
        "Partying":
            $ p = True
            bree.say "I am a bit of a party animal."
            $ hero.charm += 20
            mike.say "You mean, clubs and stuff?"
            mike.say "I never liked clubs, too loud."
            bree.say "I love a good night out."
        "Working" if not start_plus or not (hero.has_skill("work") or (hero.skills["work"].value and hero.skills["work"].value > 0) ):
            bree.say "I am very good at my work."
            $ hero.gain_skill("work")
            $ hero.charm += 5
            show fx drop at right4
            mike.say "That's a bit boring..."
        "Cars":
            bree.say "I like cars, and I got a pretty nice one."
            $ hero.gain_item("sports_car")
            $ game.flags.debt = 20000
            $ hero.fitness += 5
            show fx drop at right4
            bree.say "I'm still paying it off."
            bree.say "It feels like I'll be paying it off forever."
        "Reading" if not start_plus or not (hero.has_skill("bookworm") or (hero.skills["bookworm"].value and hero.skills["bookworm"].value > 0) ):
            bree.say "I like to stay home with a good book."
            $ hero.gain_skill("bookworm")
            show fx heart at right4
            $ mike.love += 1
            $ hero.knowledge += 5
            show mike happy
            mike.say "Ooh, I like some books. More geeky stuff but still."
            show mike normal
        "Playing guitar" if not start_plus or not (hero.has_skill("guitar") or (hero.skills["guitar"].value and hero.skills["guitar"].value > 0) ):
            bree.say "I started playing guitar when I was little."
            $ hero.gain_skill("guitar")
            $ hero.charm += 10
            show fx exclamation at right4
            mike.say "Ooh, I like music."
        "Not really":
            bree.say "Little bit of this and a little bit of that."
            $ hero.knowledge += 6
            $ hero.charm += 8
            $ hero.fitness += 6
            show fx drop at right4
            mike.say "Yeah..."
    mike.say "Nobody's perfect so..."
    mike.say "Can you tell us something bad or shameful about you?"
    $ BAD = True
    menu:
        "No, nothing...":
            bree.say "Must be one of those rare perfect ones..."
            mike.say "You are no fun..."
            $ hero.knowledge += 2
            $ hero.charm += 2
            $ hero.fitness += 2
            $ BAD = False
        "I am unlucky":
            bree.say "I am pretty unlucky..."
            $ hero.luck -= 1
            $ hero.knowledge += 2
            $ hero.charm += 2
            $ hero.fitness += 2
        "I have some big debt." if not hero.has_item('sports_car'):
            bree.say "I am in debt."
            $ game.flags.debt = 10000
        "I am kinda possessive.":
            "I cock my head on one side as I consider the question."
            "I even end up kind of scrunching my lips up."
            "You know,really trying to think it over?"
            bree.say "Hmm..."
            bree.say "I guess I can be kind of possessive when it comes to guys."
            bree.say "But that's only to be expected, right?"
            bree.say "To want my boyfriend only to have eyes for me?"
            bree.say "To be the only girl in his life?"
            "[mike.name]'s staring at me as I say all of this."
            "And I can see that he's listening intently to every word."
            "I mean, he really should be nodding in agreement by now."
            "But I just take it that he's too busy soaking up what I'm saying to him."
            bree.say "Well..."
            bree.say "That's what true love is, right?"
            bree.say "Being totally together and only thinking about each other."
            $ hero.gain_skill("yandere")
        "Animals hate me" if not start_plus or not (hero.has_skill("animalhated") or (hero.skills["animalhated"].value and hero.skills["animalhated"].value > 0) ):
            bree.say "I am not really an animal person, they don't like me at all."
            $ hero.gain_skill("animalhated")
    if BAD:
        mike.say "So, did you get up to anything noteworthy, or are you just focused on work these days?"
        "His comment caught me off guard for a second. But I did a good job covering it up with a fake, confident demeanor."
        menu:
            "I won a marathon":
                bree.say "I won a marathon once."
                $ hero.fitness += 20
                show fx exclamation at right4
                mike.say "Wow, that's really impressive!"
                bree.say "Thanks [mike.name], took a lot of work."
            "I am a people person":
                bree.say "I was the most liked person in all of my classes."
                $ hero.charm += 20
            "I won a eating contest" if not start_plus or not (hero.has_skill("iron_stomach") or (hero.skills["iron_stomach"].value and hero.skills["iron_stomach"].value > 0) ):
                bree.say "I won a burger eating contest."
                bree.say "Twice."
                $ hero.gain_skill("iron_stomach")
                $ hero.fitness += 5
                show fx drop at right4
                mike.say "Well, that’s... quite an achievement, I suppose."
                bree.say "Really? I am proud. Really proud."
                "[mike.name] at the very least seems impressed."
            "I am pretty lucky" if not hero.is_unlucky:
                bree.say "I won the lottery once."
                $ hero.luck += 1
                $ hero.money += 500
                show fx exclamation at right4
                mike.say "Wow! So you can take care of all the rent, right?"
                bree.say "Oh, it uh, wasn't that much."
            "I was the best in my class.":
                bree.say "I was the top of my class coming out of college."
                $ hero.knowledge += 20
                mike.say "Ho, you're a hard worker! No one will take that away from you."
            "I don't sleep" if not start_plus or not (hero.has_skill("no_sleep") or (hero.skills["no_sleep"].value and hero.skills["no_sleep"].value > 0) ):
                bree.say "I once stayed awake for a week straight."
                $ hero.gain_skill("no_sleep")
                $ hero.knowledge += 5
                show fx question at right4
                mike.say "Whoa, I can't do that for that long. It's great to see you’re proud of it."
    show mike normal
    show mike work at center with move
    "He seems to gather himself a little bit."
    mike.say "I dunno, uhh... I guess, what would you say is the worst thing you've ever done?"
    "I can tell that that's the best he can do as a final question to gauge my character. He's obviously never been the interviewer for a rental applicant before. The way he's flustered by this is kind of cute."
    menu:
        "I stole something once... but I gave it back.":
            bree.say "Well..."
            "I shift my weight a little bit and clear my throat. I don't really like talking about these kinds of cringey memories. They make my ears feel like they're burning, for some reason."
            "But, he asked, and I'm trying to make a good impression, so..."
            bree.say "One time when I was like nine, my parents took me to this garden store. And there were these little fairy garden decorations, and on one of them the little fairy statue had broken off, and I shoved it into my pocket and took it."
            "I swallow hard and shoot my eyes back up to his face, realizing suddenly that I'd dropped it in a mirroring childlike shame."
            mike.say "Really?"
            bree.say "I brought it back, though!"
            "I quickly amend."
            bree.say "I tried to play with it for a little while, but I felt so terrible the whole time, even though it was so pretty. I started crying and made my parents bring me back to return it."
            "[mike.name] laughs, folding his arms and scanning me up and down."
            "A peeved huff escapes me, but a smile crosses my face helplessly anyway as I see the humor in the situation."
            bree.say "The store... laughed at me, too."
            bree.say "They thought it was really cute."
            mike.say "So what you're saying is, you're an insufferably good girl?"
            bree.say "I was a criminal!"
            "My protest seems to fall on deaf ears as he shakes his head in what seems like disapproval."
            "Is being a good kid such a bad thing, anyway?"
            $ hero.morality += 10
        "Yuck. Don't you have any less... personal questions?":
            "I wrinkle my nose."
            bree.say "That's digging kind of deep right off the bat, huh?"
            "I see [mike.name] shift his weight, uncomfortable, and I snicker a little bit at him."
            bree.say "Kind of a hard-hitting first date question. You don't do this much, huh?"
            "[mike.name] throws his arms up a little bit in frustration before letting them fall back to his sides."
            mike.say "Kind of got thrown into this. Didn't have a ton of time to prepare."
            "Aw. Poor guy."
        "Hehe... You don't want to know.":
            "A wicked smile curls at one corner of my lips, and I lid my eyes a little, giving a mischievous chuckle deep in my chest."
            bree.say "Don't ask questions you can't handle the answers to."
            "[mike.name] seems a little taken aback by this, his eyes widening a little bit."
            mike.say "I, uh... that bad, huh?"
            "I shut my eyes breezily and shrug, turning a little bit away from him."
            bree.say "Look, it wasn't murder or arson, so there's nothing for you to worry about, right?"
            "[mike.name] seems unsure."
            bree.say "Well."
            "I decide to flip his game back on him."
            bree.say "What about you?"
            mike.say "Huh?"
            "I fold my arms, popping out a hip casually as I look him up and down."
            bree.say "What's the worst thing you've done, then. Isn't it more important that I know?"
            "He frowned a bit."
            mike.say "Why would it be more important for you?"
            bree.say "Well, what if you're like, an abuser, or a sexual deviant? What if you're just trying to lure pretty young girls into your lair so you can tie us up at night and drag us into your dungeon? Huh?"
            "I was joking at first, but the more I talk, the more I start to freak myself out."
            bree.say "On the phone your friend said I sounded 'perfect,' it's 'cause I'm young and female, isn't it?"
            "[mike.name] seems completely speechless, holding up his hands as if as some kind of shield against my accusations."
            $ hero.morality -= 10
    play sound door_knock
    "Before he can say anything, though, there's a knock at the door behind him, and both of our attentions turn suddenly toward it."
    "Girl" "Hello?"
    "It's a female voice."
    hide mike with moveoutright
    "[mike.name] turns back to me, as if it might be my doing that she's here."
    "But I only hold out a hand, presenting the new voice as more evidence to my claims. See? Another young hot piece of meat, huh?"
    scene bg house
    show sasha casual
    with wiperight
    "I see [mike.name] gulp as he pulls the door open to reveal a dark-haired young woman on the other side, her arms folded in a confident stance."
    mike.say "Hello?"
    "Girl" "Hey. I'm here for the roommate position."
    "She looks like she doesn't take crap from anyone."
    "If I was freaking myself out about [mike.name] being out to take advantage of us, I feel a little more secure seeing her standing there."
    "I'm no pushover, myself, but with this goth rocker chick at my side, we can kick this dude's ass into oblivion if he tries it. No doubt."
    scene bg livingroom with fade
    show sasha casual at right
    show mike work at center
    with moveinright
    mike.say "Uh, yeah. Come in. I was just showing--"
    bree.say "Me to my room."
    "I cut in, stepping forward and holding my hand out to greet this new girl."
    bree.say "Hey! You must be our new roommate."
    "There's no look of devious glee in [mike.name]'s eyes at the prospect of the two of us moving in. In fact, he looks a little shaken and overwhelmed, like a skittish kitten in a room where too much is going on."
    "Somehow I highly doubt he's going to be taking advantage of anyone."
    "Girl" "Sasha."
    "She shakes it back with me, firm and confident, in the way [mike.name] hadn't."
    show sasha casual at right5
    show mike work at left5
    with move
    "I get the feeling everything's going to go real smoothly for me here."
    bree.say "So."
    "I bring my gaze back up to [mike.name], and Sasha steps aside to face him as well, putting him on the spot."
    bree.say "Where's our paperwork then, big boy?"
    "He seems to accept that he's lost control of the situation. With a sigh, he brings a hand up to massage the bridge of his nose and nods."
    mike.say "Yeah, I'll... need to go print that out, I guess."
    sasha.say "Sounds good."
    bree.say "Yeah, I'll go start packing!"
    sasha.say "I'll get my things, too."
    mike.say "I guess I'll have that ready when you guys get back...?"
    bree.say "Tomorrow."
    "There was no question that I'd have my things packed up and ready to get out of the hellhole of my current apartment by tonight, but I figured I'd give the poor kid some time to recuperate first."
    mike.say "Tomorrow."
    "He stands aside as Sasha steps past him and out the door, and I skip happily out behind her, breaking into a jog immediately down the sidewalk toward my place."
    scene bg amyhome at blur(16), dark with timelaps
    "I can't wait."
    "I think I even like the two of them already."
    "I click the tip of the pen back into its holster, dropping it onto the table beside my paperwork."
    "It feels so much easier to breathe here, like a huge weight has been lifted off my chest."
    "I knew I hated my last place, but I didn't realize just how much it was affecting me until it was finally over."
    scene bg kitchen with timelaps
    bree.say "So, that's that, then?"
    show mike casual
    "I glance back up to where [mike.name] is sitting opposite me at the table."
    "He looks a little less exhausted than he had yesterday. Sleeping on it definitely did him some favors."
    mike.say "Yeah, I guess that's it then."
    "He motions vaguely toward the rest of the room with the hand not lazily propping up his jaw."
    show mike casual happy
    mike.say "Welcome home."
    "I can feel my face light up like a disney princess, and it takes all of my strength not to squeal with glee."
    "Home. Home! This place is my home now."
    show mike casual normal
    "And [mike.name] and Sasha... maybe we won't be the best of best friends, I won't be that naive. But I can tell I'm gonna at least get along with them."
    "Or, at least, I assume I will, based off our short encounter. It's gonna be great. Nothing like my ex-roommate and that hellhole."
    "My voice is a little bit quiet, like a kid asking about their birthday present, when I speak next."
    bree.say "Which room is mine?"
    play sound door_knock
    "A knock at the door interrupts before [mike.name] can answer me, and my heart leaps again with renewed excitement."
    show mike at right with move
    mike.say "That's probably Sasha."
    show bg house
    show mike casual at left5
    show sasha box normal at right5
    with fade
    "There's a stack of boxes with shapely legs on the other side of it, and after a moment, [mike.name] grabs the top half of the mountain from her, revealing her pretty face."
    "She blows a tuft of hair off of her forehead before shifting her gaze past him over to me."
    sasha.say "Hey, earlybirds. Did I miss the party?"
    "Okay, so I was kind of excited. I'd been bouncing on the edge of my bed ready to head over this morning, practically before the sun even rose."
    "But I'd managed to control myself enough to drive around town a bit after I'd packed my car, get myself a coffee, then a breakfast from the other side of the city, just to kill time and let [mike.name] sleep."
    "I didn't even tell my roommate I was leaving. I taped a note on her door telling her that I wasn't renewing, and wishing her good luck finding either a replacement or a new place."
    "Thank God Sasha took the last room in this place. How mortified would I have been if she had shown up here, ringing the doorbell about the ad?"
    "A physical shudder rolls down my spine as [mike.name] moves over and sets the boxes he's carrying onto the edge of the table to bear some of the weight."
    "Sasha stands unbothered by the door, holding hers with seemingly no problem."
    "What a badass. I can't help feeling a bit of an envycrush building in me."
    "I really want to be good friends with her. Alright, I admit it. It feels like first days at new schools all over again, scoping out the 'cool kids' and wishing shamelessly that they'd end up thinking I was cool, too."
    scene bg livingroom
    show mike casual at left5
    show sasha casual2 at right5
    with fade
    mike.say "Okay, well, there's actually some bad news."
    "[mike.name] huffs, glancing toward the stairway and motioning with his head toward the floor above us."
    mike.say "Your rooms are up there, but one of them's gonna be completely emptied--"
    sasha.say "I'll take that one."
    hide sasha with moveoutright
    mike.say "--oh. Okay, that works."
    "Works for me, too."
    "I hop up out of my seat, rarin' and ready to get this show on the road."
    bree.say "So the other one's mine, then?"
    show mike casual happy at center with move
    mike.say "All yours."
    scene bg bedroom2 with fade
    "I don't waste any time before making my way over to my things, hoisting one backpack over my shoulder and grabbing the handle of a rolling suitcase in the other hand."
    "There weren't a ton of things I needed to bring, honestly."
    "My last place had been pre-furnished, too, so I'd only had knick-knacks and a few personal items that I'd needed to pack."
    "I'd managed to fit all of it into two backpacks, two suitcases, a purse, a laundry bag, and my messenger bag, and admittedly most of what filled them were my clothes."
    "It's easy to unpack my necessities once I hike all of my belongings up into my room, flopping myself back onto my bed and reveling for a moment in the feeling of fresh surroundings and fresh starts."
    "I breathe it in, just for a bit, closing my eyes and drawing a slow, deep, filling breath in through my nose, before huffing it out and hopping back to my feet."
    "Within the hour, I've got my place set up -- laptop set neatly on the desk, plugged in and charging, my gaming mouse and headset waiting on either side of it."
    "My trinkets, memories from old friends and from home, are set up appealingly across the top of my dresser and the odd shelf here and there, making the place look already like it's lived in and welcoming."
    "I'll deal with the clothes later. That's always my least favorite part of cleaning up, and admittedly it's pretty likely I'll be dressing myself out of my suitcases for a bit before I get my act together and put stuff into the closet and dresser."
    "But for now, I can hardly wait to start exploring. I wonder if Sasha's done unpacking yet? Maybe they need help with something. What's [mike.name] doing right now?"
    "Maybe I can check out that pool I saw in the ad."
    $ IN_EVENT_WITH = None
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
