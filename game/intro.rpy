label intro(start_plus):

    $ STORY_HOLD = True
    stop music fadeout .5
    play music "music/roa_music/sunny.ogg" fadeout .5 fadein .5
    scene bg black with dissolve

    if start_plus:
        $ game.flags.ngplus = True

    if renpy.has_label("mc_selection_female"):
        call mc_selection_female from _call_mc_selection_female
    else:
        $ sex_choice = "male"
        $ heroname = "Mike"
        $ family_name = "Seeker"
        $ Person.find("mike").hide()
        $ starting_money = 500


    call screen get_namesurname_screen(heroname, family_name, sex_choice)
    $ birthday_day = "random"
    $ birthday_month = "random"

    call screen get_birthday_screen()
    $ hero.initialize(heroname, family_name, sex_choice, starting_money, birthday_day, birthday_month, start_plus)
    if sex_choice == "male":
        if Person.find("mike"):
            $ mike.name = hero.name
            $ mike.family_name = hero.family_name
        if Person.find("minami"):
            $ minami.family_name = hero.family_name
        if Person.find("angela"):
            $ angela.family_name = hero.family_name
    else:
        if Person.find("bree"):
            $ bree.name = hero.name
            $ bree.family_name = hero.family_name
        if Person.find("mike"):
            if Person.find("minami"):
                $ minami.family_name = mike.family_name
            if Person.find("angela"):
                $ angela.family_name = mike.family_name
    $ hero.flags.visited_rooms = set()

    $ starting_day = randint(1, 31)
    $ starting_month = randchoice(SEASONS)
    call screen get_start_date_screen()
    $ game.season = SEASONS.index(starting_month)
    $ game.day = starting_day

    $ game.room = "livingroom"

    if not persistent.skip_tutorial:
        call tutorial from _call_tutorial

    $ shuffle_choices = False
    call expression hero.gender + "_intro" from _call_expression_448
    $ DONE[hero.gender + "_intro"] = game.days_played
    $ shuffle_choices = True

    $ sasha.love.max = 30
    $ HIDE_UI = False
    hide bree
    hide sasha
    hide mike
    $ STORY_HOLD = False
    scene bg black with dissolve
    return

label tutorial:
    $ game.play_music("music/roa_music/tiny_love.ogg")
    $ IN_EVENT_WITH = "tuto"
    "Andrealphus" "Hi [hero.name]."
    "Andrealphus" "Please allow me to introduce myself..."
    "Andrealphus" "I am Andrealphus, Demon Lord of Lust, Duke of Debauchery, I am one of the Seven Lords of Sin, and honestly..."
    "Andrealphus" "I am the only one that is any fun."
    "Andrealphus" "Just kidding, I am the Dev for that little game you are playing, that's all."
    "Andrealphus" "First of all, thank you for playing my game and I really hope you enjoy it as much as I enjoy making it."
    "Andrealphus" "Now, to help you start in 'Love & Sex' I'll give you a few pointers."
    show bg livingroom
    show screen overlay_ui
    with dissolve
    "Andrealphus" "This is your living room, one of many {b}Locations{/b} in the game world."


    show tuto location with dissolve
    "Andrealphus" "When you are moving around, minding your own business, you will find various {b}Locations{/b}."
    show tuto room with dissolve
    "Andrealphus" "At the bottom of the {b}Location{/b} screen you can see all the activities you can do in that given {b}Location{/b}."
    show tutoarrow at zoomAt(1, (265, 240)), rotation(90) with dissolve
    "Andrealphus" "You can see the {b}Actions{/b} menu, this is what you can do in this {b}Location{/b}. But it will not show you the {b}Actions{/b} you can't do, for example if you lack {b}Needs{/b}, {b}Attributes{/b}, or {b}Money{/b}."
    show tutoarrow at zoomAt(1, (655, 130)), rotation(180) with dissolve
    "Andrealphus" "This button open your {b}inventory{/b}, if you buy or gain new item this is where you can see them."
    show tutoarrow at zoomAt(1, (300, 330)), rotation(90) with dissolve
    "Andrealphus" "The {b}Exits{/b} menu shows you all the {b}Locations{/b} you can access from the current one."
    hide tutoarrow
    hide tuto
    with dissolve


    show tutoarrow at zoomAt(1, (200, 60)) with dissolve
    "Andrealphus" "At the top left you have a handy {b}Calendar{/b}'s date."
    "Andrealphus" "In the game, the year is divided in 4 months (named Spring, Summer, Fall and Winter) of 31 days each, with your usual holidays and birthdays."
    "Andrealphus" "Some {b}Actions{/b} are restricted by the time of day or the current month."


    show tutoarrow at zoomAt(1, (460, 60)) with dissolve
    "Andrealphus" "Next you can see your {b}Needs{/b}. Because, yes, you need to eat, sleep, clean yourself and have a little fun."
    show tutoarrow at zoomAt(1, (350, 60)) with dissolve
    "Andrealphus" "{image=gui/icons/icon_energy.png} {b}Energy{/b} shows you how much stamina you have left before needing to rest."
    show tutoarrow at zoomAt(1, (420, 60)) with dissolve
    "Andrealphus" "{image=gui/icons/icon_fun.png} {b}Fun{/b} lets you know how bored you are."
    show tutoarrow at zoomAt(1, (490, 60)) with dissolve
    "Andrealphus" "{image=gui/icons/icon_grooming.png} {b}Grooming{/b} shows you how smelly and dirty you are."
    show tutoarrow at zoomAt(1, (560, 60)) with dissolve
    "Andrealphus" "{image=gui/icons/icon_hunger.png} {b}Hunger{/b} shows you how hungry you are."
    "Andrealphus" "In general, {b}Actions{/b} will cost you some {b}Needs{/b}. Don't let them go too low, when they get low you lose the ability to perform more and more {b}Actions{/b}."


    show tutoarrow at zoomAt(1, (775, 60)) with dissolve
    "Andrealphus" "Near the {b}Needs{/b} you can see your {b}Attributes{/b}, some girls find some {b}Attributes{/b} more pleasing and some {b}Actions{/b} requires high {b}Attributes{/b}."
    show tutoarrow at zoomAt(1, (675, 60)) with dissolve
    "Andrealphus" "{image=gui/icons/icon_charm.png} {b}Charm{/b} is your charisma."
    show tutoarrow at zoomAt(1, (765, 60)) with dissolve
    "Andrealphus" "{image=gui/icons/icon_fitness.png} {b}Fitness{/b} evaluates your physical abilities."
    show tutoarrow at zoomAt(1, (845, 60)) with dissolve
    "Andrealphus" "{image=gui/icons/icon_knowledge.png} {b}Knowledge{/b} is an accurate evaluation of your intellect."
    "Andrealphus" "I advise you to raise your {b}Attributes{/b} as soon as you can, because for now they are rather low."


    show tutoarrow at zoomAt(1, (1015, 60)) with dissolve
    "Andrealphus" "After the {b}Attributes{/b}, you can see your {b}Money{/b}, girls likes gifts and be taken to dates so this is quite a priority."
    "Andrealphus" "With {b}Money{/b} you can also buy clothes and accessories that will improve your {b}Attributes{/b}, some girls prefer certain clothes over others."
    hide tutoarrow with dissolve


    show tuto progressbar with dissolve
    show tutoarrow at zoomAt(1, (975, 110)) with dissolve
    "Andrealphus" "Sometimes below {b}Money{/b} you will see a {b}progress bar{/b}, it is used in several ways."
    "Andrealphus" "To show you if you have done your share of the chores while at home.\nTo display how far you are from your next promotion at work.\nTo indicate how much a girl is having fun during a date."
    hide tutoarrow
    hide tuto
    with dissolve


    show tutoarrow at zoomAt(1, (1020, 40)), rotation(45) with dissolve
    "Andrealphus" "This top right round button allows you to open the {b}Story Tracker{/b}."
    hide tutoarrow with dissolve
    show tuto storytracker with dissolve
    "Andrealphus" "If you are ever lost it will give you indications on what to do next."
    show tutoarrow at zoomAt(1, (25, 74)), rotation(90) with dissolve
    "Andrealphus" "On the left, you have all story category you have already encounter. Pick witch one you want more details about."
    show tutoarrow at zoomAt(1, (500, 58)), rotation(-90) with dissolve
    "Andrealphus" "If you need more information, some category has an associated wiki page. You can open their wiki by using the 🔗 icon."
    hide tutoarrow
    hide tuto
    with dissolve


    show tutoarrow at zoomAt(1, (87, 40)), rotation(-45) with dissolve
    "Andrealphus" "The round button on the top left corner open up your {b}Smartphone{/b}."
    show tuto phoneA with dissolve
    "Andrealphus" "As I am pretty nice for a Game Dev I uploaded a nice app to your phone."
    show tuto phoneB with dissolve
    "Andrealphus" "Once you get a girl's number you will be able to see her in your contact. You can also check some information about her, like her {image=gui/icons/icon_love.png} {b}Love{/b} and her {image=gui/icons/icon_sub.png} {b}Kink{/b}."
    "Andrealphus" "That should be useful don't you think?"
    show tuto phoneC with dissolve
    "Andrealphus" "You can also use it to see your own stats, but that's a lot less fun."
    hide tutoarrow
    hide tuto
    with dissolve


    show bree flirt blush with dissolve
    "Andrealphus" "As you expect you will date girls. This is {b}[bree.name]{/b} she is a girl, cute and sexy. Your goal is to fuck her or another being of her species."
    hide bree
    show tuto interaction with dissolve
    "Andrealphus" "When you {b}talk{/b} a girl, you can choose what to discuss or do with her. You can also view more details about her, and track the progress of your relationship with her."
    hide tuto


    show tuto quickmenu with dissolve
    "Andrealphus" "At the very bottom, you will find some {b}shortcuts{/b}. That will help you speed up some process."
    show tutoarrow at zoomAt(1, (455, 270)) with dissolve
    "Andrealphus" "First, the {b}Back{/b} button will allows you to go back a little in the past."
    show tutoarrow at zoomAt(1, (510, 270)) with dissolve
    "Andrealphus" "Next, the {b}Skip{/b} button. When skipping is enabled, you will pass through the dialogues at lightning speed."
    show tutoarrow at zoomAt(1, (565, 270)) with dissolve
    "Andrealphus" "The {b}Auto{/b} button will automatically pass step by step the dialogues, so you can read without passing yourself."
    show tutoarrow at zoomAt(1, (635, 270)) with dissolve
    "Andrealphus" "In case of emergency you can use the {b}Q.Save{/b} button. It will quickly save your progress."
    show tutoarrow at zoomAt(1, (715, 270)) with dissolve
    "Andrealphus" "And the {b}Q.Load{/b} button. That will load what is in your quick save."


    "Andrealphus" "I've finish all the basic introduction. Now, go back to this world, full of girls and chicks awaiting you."
    "Andrealphus" "Just three more things before you go:\n1 - Don't hesitate to check the {b}Options{/b} to change the grindiness and randomness of the game to suit your tastes."
    "Andrealphus" "2 - Save often, cause just like in real life, many things can be unpredictable in the game, so take advantage of the fact that it is a game."
    "Andrealphus" "3 - Know that you can do a lot of things in a single play, but not everything... I encourage you to explore as much as possible during your first play and then start again to make different choices and explore other paths."
    "Andrealphus" "Well, now that all is said, I bid you good luck in your virtual 'Love & Sex' life!"
    "Andrealphus" "And remember: the kinkier, the better."
    $ renpy.hide_screen( 'say' )
    window hide dissolve
    hide screen overlay_ui
    show bg white with dissolve
    pause 0.5
    $ persistent.skip_tutorial = True
    $ IN_EVENT_WITH = None
    return

label male_intro:
    $ IN_EVENT_WITH = "intro"
    $ game.play_music("music/roa_music/fly_high.ogg")
    $ hero.smartphone_contacts.append("samantha")
    $ game.room = "office"
    window auto
    scene bg office with dissolve
    show screen overlay_ui with dissolve
    $ quick_menu = True
    "My eyes hurt."
    "I've been staring at this computer screen for what feels like an eternity by now, mindlessly tapping away at my keyboard."
    "Words fill the screen in front of me, more than I needed, or was expected to write."
    "In my mindless trance I barely comprehend the sound of footsteps behind me, approaching with haste."
    show aletta talkative with easeinleft
    show fx exclamation
    aletta.say "Your shift's over, what are you still doing here?"
    show aletta normal
    "The sound of my boss's voice snaps me from my screen."
    "I turn to meet her gaze, rather than disappointed or angry, she simply seems curious."
    mike.say "Working, Boss."
    "I've never been a particularly hard worker. I did what was asked of me, and then moved on, but today was different."
    "I looked back to the screen quickly, attempting to hide in my work yet again."
    show aletta happy
    aletta.say "The day's over, go home, I'm not having some worker's union on my ass for unpaid overtime."
    "I groan."
    show aletta normal
    "Aletta's always been a good boss, fair and understanding."
    "She runs the place with an iron fist, but doesn't mistreat her employees."
    "I get the impression she genuinely cares for us."
    mike.say "Whatever you say, Boss..."
    show aletta normal at left with ease
    "With an exaggerated rolling of her eyes, Aletta turned and began walking back towards her office."
    "I spend a moment admiring her behind as she does so, tightly wrapped in her dress skirt."
    hide aletta normal with easeoutleft
    "Reluctantly, I hit save and close down my computer."
    "I gaze into the empty black void of the screen for a few moments, before sliding from my desk, grabbing my jacket and beginning towards the door."
    $ active_girl.object = audrey
    scene bg office with fade
    pause 0.3
    show audrey talkative at right with easeinright
    audrey.say "Wait! Take me with you!"
    show audrey normal at center with ease
    "I'm stopped in my tracks by my coworker, Audrey, leaping in front of me, clasping onto my shirt with a pleading look in her eyes."
    "Audrey's nice, but she's trouble."
    "She's always getting into all sorts of messes, and expects me to help her clean them up."
    "I don't know why Aletta doesn't fire her already to be honest, she clearly doesn't find Audrey's uselessness endearing."
    "Although, Audrey has been working more nights lately."
    "Maybe Aletta is trying to punish her in some way?"
    "Whatever, it isn't any of my business."
    mike.say "Sorry Audrey, I have to go."
    show audrey flirt
    audrey.say "Come on! I'll make it worth your time~!"
    show audrey normal
    "That was another thing about Audrey, she had the nasty habit of flirting excessively with any male coworker."
    "From what I know, she's never landed."
    mike.say "Bye Audrey."
    "I quickly pry the woman from my arm, hurrying to the exit post haste before they could stop me."
    show audrey angry
    audrey.say "I'll never forget this!"
    hide audrey
    $ active_girl.object = None
    $ game.room = "street"
    scene bg street
    with fade
    if game.season == 0:
        "I trudge out onto the street, the warm breeze hitting me like a brick wall as I pause to get my bearings."
    elif game.season == 1:
        "I trudge out onto the street, the summer heat hitting me like a brick wall as I pause to get my bearings."
    elif game.season == 2:
        "I trudge out onto the street, the autumn wind hitting me like a brick wall as I pause to get my bearings."
    else:
        "I trudge out onto the street, the bitter cold hitting me like a brick wall as I pause to get my bearings."
    "I'm lucky my house is nearby to work, it means I can walk to and from in no time at all."
    "Today though, that feels like more of a curse than a blessing."
    "It started with the call at lunch..."
    scene bg street at dark with dissolve
    play sound cell_vibrate
    $ result = renpy.call_screen("smartphone_choice", "Samantha")
    if not result:
        "Damned phone screen! I just picked up by mistake..."
    if samantha.flags.nickname == "cupcake":
        mike.say "Hey Cupcake."
    else:
        mike.say "Hey Samantha."
    samantha.say "Hey."
    samantha.say "We moved out."
    mike.say "Wait, you what?"
    samantha.say "We moved out!"
    samantha.say "Ryan asked me and whisked me away, it was so romantic!"
    mike.say "What about me? What about your things?"
    samantha.say "Ryan already packed, and we put out an ad on your behalf for a new roommate!"
    mike.say "Woah, just hold on a minute."
    if samantha.flags.nickname == "cupcake":
        mike.say "Put on Ryan, Cupcake."
    else:
        mike.say "Put on Ryan, Samantha."
    "I could hear a few seconds of silence and distant murmuring through my phone, before..."
    ryan.say "Sup?"
    mike.say "What the hell are you doing, man?"
    mike.say "I can't afford rent on my own!"
    ryan.say "Woah, calm down, Samantha just told you we're already looking for a replacement."
    mike.say "That's not the point!"
    mike.say "You didn't think to warn me?"
    ryan.say "You don't understand spontaneity, do you? No wonder Samantha chose me."
    mike.say "Woah, low blow Ryan."
    ryan.say "Whatever dude, later."
    mike.say "Wait!"
    play sound phone_calling
    pause 1.0
    scene bg street with fade
    "Ryan was my old college friend. We were pretty close for a while, so rented a house together after graduating."
    "When the landlord increased our rent, we had to look for a third roommate, and found Samantha."
    "Both of us were clearly interested from the start, and it quickly turned into a contest."
    "Ryan won."
    "He turned into a real douche after that, and would rub his victory in my face at every possible moment. Samantha didn't seem to even notice."
    "I was still reeling from being dumped by my girlfriend, Alexis, at the time, so it really hurt."
    "I caught her sneaking around banging strangers behind my back, it was...rough for a while."
    "Now, all I've got waiting for me is a large, empty place I can't afford to live in."
    $ game.room = "house"
    scene bg house with fade
    "I'd rather be working all night."
    "Huh, who's this?"
    show bree sad with fade
    "A strange woman stands outside my door, hammering the doorbell even though it was clear nobody's home."
    "She seems annoyed, as though the occupant of the home she was trying to enter has wronged her somehow."
    mike.say "Can I help you?"
    show bree normal
    "She turns to me as I speak, and I have to admit, I was struck by her beauty."
    show bree smile
    "Girl" "Oh, hey. You know who lives here? I'm supposed to meet them but I don't think they're in."
    show bree normal
    "There was one likelihood that stood out above all others in my mind, she must have arranged to meet me here with Ryan."
    "He knew what time I get home from work, so probably told her to wait for me then."
    "I feel a slight twinge of guilt as I realise that my moping around made her stand around in the cold for god knows how long."
    mike.say "Oh, that's me."
    mike.say "You here for the place?"
    "I don't question how quickly she responded to the advertisement."
    show fx exclamation zorder 2
    show bree happy
    "Girl" "Oh, yeah! I'm [bree.name], I take it you're my potential roommate?"
    show bree normal
    "She doesn't seem all that mad for making her wait at least, and quickly took my outstretched hand to give a quick shake."
    "I'm given pause by how soft her skin is, but I shake it off. I don't want another Samantha here, even if she is really hot."
    mike.say "Yeah, that's me."
    show bree smile
    bree.say "Nice to meet you!"
    show bree normal
    mike.say "Likewise."
    mike.say "Come on in..."
    mike.say "I'll show you around."
    hide bree
    $ game.room = "livingroom"
    scene bg livingroom
    show bree happy
    with fade
    bree.say "Wow, this place is pretty nice!"
    show bree normal
    "I nod. It's even got a communal pool, for the price I'm lucky. And, well now she is too."
    show bree smile
    bree.say "When can I move in?"
    show bree normal
    "Woah, hold on a minute."
    mike.say "Move in?"
    mike.say "I've known you for less than a minute!"
    mike.say "Shouldn't we like, ask questions and get to know each other first?"
    show bree talkative
    bree.say "Oh, OK!"
    bree.say "In that case, tell me about yourself!"
    show bree normal
    mike.say "Well, that's kinda vague..."
    show bree talkative
    show fx question zorder 2
    bree.say "Then... Do you like sports?"
    show bree normal
    if start_plus and all([(hero.has_skill(sport) or (hero.skills[sport].value and hero.skills[sport].value > 0)) for sport in ["martial_arts", "golf", "cooking", "dance", "shooting", "sneaky"]]):
        mike.say "I'm not really the sporty type."
        $ hero.knowledge += 1
        $ hero.charm += 1
        $ hero.fitness += 1
        show bree happy
        bree.say "Hehe, same here. Give me a good video game or a book any day of the week."
        show bree normal
    else:
        menu:
            "Martial Arts" if not start_plus or not (hero.has_skill("martial_arts") or (hero.skills["martial_arts"].value and hero.skills["martial_arts"].value > 0) ):
                mike.say "I do martial arts."
                $ hero.gain_skill("martial_arts")
                $ hero.fitness += 5
                show bree smile
                show fx exclamation zorder 2
                bree.say "Oh, cool! You'll have to show me some moves sometime!"
                show bree normal
            "Golf" if not start_plus or not (hero.has_skill("golf") or (hero.skills["golf"].value and hero.skills["golf"].value > 0) ):
                mike.say "I am an accomplished golfer."
                $ hero.gain_skill("golf")
                $ hero.charm += 4
                $ hero.fitness += 6
                show fx question zorder 2
                show bree talkative
                bree.say "Really? You don't seem like a golfer."
                show bree normal
                mike.say "What, not a middle aged businessman in a suit?"
                show bree smile
                bree.say "Exactly!"
                show bree normal
                "I shake my head dramatically, before moving on."
            "Discreet" if not start_plus or not (hero.has_skill("sneaky") or (hero.skills["sneaky"].value and hero.skills["sneaky"].value > 0) ):
                mike.say "I am fucking sneaky."
                $ hero.gain_skill("sneaky")
                $ hero.charm += 10
                show bree talkative
                show fx question zorder 2
                bree.say "Really? You don't look like a ninja to me."
                show bree normal
                mike.say "Pffff Ninjas are pretty noisy next to me?"
                show bree smile
                bree.say "Cool!"
                show bree normal
                "I shake my head dramatically, before moving on."
            "Cooking" if not start_plus or not (hero.has_skill("cooking") or (hero.skills["cooking"].value and hero.skills["cooking"].value > 0) ):
                mike.say "Does cooking count?"
                $ hero.gain_skill("cooking")
                $ hero.charm += 3
                $ hero.knowledge += 2
                show bree talkative
                bree.say "Cooking? Well, it's not really a sport..."
                show bree happy
                bree.say "But I'll forget about that if you make me something good!"
                show bree normal
                "I can already tell she's going to be a handful."
            "Dancing" if not start_plus or not (hero.has_skill("dance") or (hero.skills["dance"].value and hero.skills["dance"].value > 0) ):
                mike.say "Not really, closest I get is dancing."
                $ hero.gain_skill("dance")
                $ hero.charm += 4
                $ hero.fitness += 6
                show bree happy
                show fx heart zorder 2
                bree.say "Ooh, how romantic."
                show bree normal
            "Shooting" if not start_plus or not (hero.has_skill("shooting") or (hero.skills["shooting"].value and hero.skills["shooting"].value > 0) ):
                mike.say "I love shooting and guns."
                $ hero.gain_skill("shooting")
                $ hero.knowledge += 4
                $ hero.fitness += 6
                show fx drop zorder 2
                show bree blank
                bree.say "..."
                show bree normal
            "No, I don't":
                mike.say "I'm not really the sporty type."
                $ hero.knowledge += 8
                $ hero.charm += 6
                $ hero.fitness += 6
                show bree happy
                bree.say "Hehe, same here. Give me a good video game or a book any day of the week."
                show bree normal
    show bree smile at right4 with ease
    bree.say "So I'll go get my things!"
    show bree normal
    mike.say "H-Hold on a minute!"
    mike.say "That was one question!"
    show bree happy
    bree.say "Yeah, and now we know each other better! Great!"
    show bree talkative
    bree.say "Which room is mine?"
    show bree normal
    play sound door_bell
    "I didn't have a chance to answer, turning to the front door in response to the call."
    $ game.room = "house"
    scene bg black with dissolve
    pause 0.1
    scene bg house
    show sasha with wiperight
    mike.say "Hello?"
    show sasha shout
    "Girl" "Hey, I'm here for the roommate position?"
    show sasha normal
    "Another? Just what was in that ad to attract them so quickly?"
    mike.say "Yeah, come in."
    "I step away from the door, waiting for the stranger to enter as [bree.name] seems to grow curious."
    $ game.room = "livingroom"
    scene bg livingroom
    show bree talkative at right
    with fade
    show fx question zorder 2 at right
    bree.say "Is that our new roommate?"
    show bree normal
    "I sigh. It's clear arguing with her is futile, and it isn't like I've got much choice, rent is just around the corner and I don't have nearly enough to live here on my own."
    "I give a silent nod, which clearly excites [bree.name]."
    show bree happy
    "She gives the air a quick fist pump when she thinks I'm not looking."
    show bree normal
    "The girl on the other side must have been hesitating, because it took a moment for the front door to open."
    show sasha at left with easeinleft
    "Another stunning girl stands in the entrance, although her demeanor is much darker than [bree.name]'s already."
    show fx question zorder 2 at left
    show sasha shout
    "Girl" "I got the right place?"
    show sasha normal
    "Why she waited to ask until after she'd opened the door was beyond me."
    mike.say "Yeah, nice to meet you."
    show bree happy
    bree.say "And I'm [bree.name]!"
    show bree talkative
    bree.say "Are you going to be moving in too?"
    show bree normal
    show sasha shout
    "Girl" "The ad said three bedrooms, so yeah."
    show sasha normal
    "I push aside that nagging in the back of my mind, annoyed that they seem to have decided they're living here without even asking."
    "It's true that the place is technically three bedrooms, but Ryan and I made one of the rooms into a gym when he and Samantha hooked up."
    "She was sleeping with him after all, no need to leave a room to waste."
    "That reminds me though, all of that equipment was Ryan's, it's probably all gone now..."
    "I groan quietly to myself at the realisation that I'll have to start paying for the gym too."
    show fx anger zorder 2 at left
    show sasha vangry
    "Girl" "Ugh, if it's such a big deal I'll find somewhere else."
    show sasha annoyed at top_mostleft with ease
    "Seeming to misunderstand my groan as being directed towards her, the new girl turned and began to head back towards the door."
    show sasha stuned at left with hpunch
    "I reach out quickly to grasp her arm to stop her in their tracks."
    mike.say "Wait!"
    "I find myself cowering however, as she slowly turned her head to meet me."
    show sasha wtf
    "Her gaze was terrifying, I could have sworn it alone could have driven me to the verge of death."
    "I wordlessly, slowly released her, extending my arms in an apologetic manner as I backed away."
    mike.say "I-I mean, I wasn't groaning at you."
    show fx anger zorder 2 at left
    show sasha angry
    "Girl" "Touch me again like that, and I'll end you."
    show sasha upset
    "Jeez, what was with this girl?"
    mike.say "Yeah! OK, no touching, got it!"
    show bree happy
    "I'm glad [bree.name] finds this whole situation funny, I can see her holding back laughter from out of the corner of my vision."
    show bree normal
    show sasha shout
    "Girl" "Good, then we've reached an understanding. I'm Sasha, you can call me Sasha."
    show sasha normal
    show bree happy
    bree.say "Nice to meet you, Sasha."
    show bree normal
    mike.say "Yeah, likewise."
    "'Nice' was an overstatement, but being rude would be dangerous with a girl like that."
    show bree talkative
    bree.say "Alright, anything else you need from me?"
    show bree normal
    "There's so many questions, I don't know where to begin, so I simply start with what seems obvious."
    mike.say "I'll need your current job for the leasing contract."
    show bree talkative
    bree.say "I'm a student full time."
    show bree normal
    "That gives me slight pause, but I make a mental note of it anyway."
    "I wonder how a student can afford to stay in a place like this, even with three people, and good price for the size, it isn't cheap."
    show sasha shout
    sasha.say "Before you ask, I work at a clothing store at the mall."
    show sasha normal
    "I can imagine it now, gothic architecture and only black clothes."
    "The staff would be pretentious and all have names like 'Winter'."
    "Everything would be expensive to make up for the fact that nobody but goths cares about it, so sales are low."
    "But hey, I don't care how she makes her money as long as I don't have to cover her ass with rent."
    show bree talkative
    bree.say "What do you do?"
    show bree normal
    mike.say "I work as a code monkey in a local company."
    show fx drop zorder 2 at left
    show sasha whining
    sasha.say "That doesn't sound like the most inspiring job."
    show sasha normal
    mike.say "That's because it isn't."
    show bree talkative
    bree.say "Then, how do you unwind?"
    bree.say "You gotta have a hobby or two to relax with."
    show bree normal
    $ p = False
    menu:
        "Food" if not start_plus or not (hero.has_skill("foodie") or (hero.skills["foodie"].value and hero.skills["foodie"].value > 0) ):
            mike.say "I love food."
            $ hero.gain_skill("foodie")
            $ hero.fitness -= 3
            $ hero.charm += 3
            show sasha shout
            sasha.say "As in cooking?"
            show sasha normal
            mike.say "No as in eating..."
            show fx exclamation zorder 2
            show bree happy
            bree.say "Oh, cool! We should go for dinner sometimes!"
            show bree normal
        "Video Games" if not start_plus or not (hero.has_skill("video_games") or (hero.skills["video_games"].value and hero.skills["video_games"].value > 0) ):
            mike.say "I play a lot of video games."
            $ hero.gain_skill("video_games")
            $ hero.knowledge += 5
            show bree happy
            bree.say "Oh, nice! I shoulda made you for a fellow gamer!"
            show bree normal
            show sasha whining
            sasha.say "You both play video games?"
            show sasha normal
            mike.say "Apparently. Do you?"
            show sasha joke
            sasha.say "No thanks, I have grown up hobbies."
            show sasha normal
            mike.say "Like what?"
        "Fitness":
            mike.say "I love running and working out."
            $ hero.fitness += 20
            show bree happy
            bree.say "I coulda guessed that."
            "I strike a heroic pose, which draws a laugh out of [bree.name]."
            "Maybe she won't be so bad after all, she seems like fun."
            show bree normal
            show sasha annoyed
            "Sasha on the other hand, grimaces as I flex."
            show sasha whining
            sasha.say "Working out isn't a hobby."
            show sasha normal
            mike.say "Oh yeah? Then what do you do?"
        "Partying":
            $ p = True
            mike.say "I am a bit of a party animal."
            $ hero.charm += 20
            show bree talkative
            bree.say "You mean, clubs and stuff?"
            show bree normal
            show sasha happy
            sasha.say "Yeah, that's what he said."
            show sasha normal
            show bree talkative
            bree.say "I never liked clubs, too loud."
            show bree sadsmile
            mike.say "I love a good night out."
            "Was... Was that a smile? On Sasha?"
            "It only lasted for a moment, but I could have sworn I saw one..."
            show bree talkative
            bree.say "What about you, Sasha? You do anything fun?"
            show bree normal
        "Working" if not start_plus or not (hero.has_skill("work") or (hero.skills["work"].value and hero.skills["work"].value > 0) ):
            mike.say "I am very good at my work."
            $ hero.gain_skill("work")
            $ hero.charm += 5
            show fx drop zorder 2 at right
            show bree talkative
            bree.say "That's a bit boring..."
            show bree sadsmile
            mike.say "What about you then, Sasha?"
        "Cars":
            mike.say "I like cars, and I got a pretty nice one."
            $ hero.gain_item("sports_car")
            $ game.flags.debt = 20000
            $ hero.fitness += 5
            show fx drop zorder 2 at left
            show sasha annoyed
            "Sasha gives a loud scoff at my statement, clearly unimpressed."
            mike.say "I'm still paying it off."
            mike.say "It feels like I'll be paying it off forever."
            mike.say "What about you then, Sasha?"
        "Reading" if not start_plus or not (hero.has_skill("bookworm") or (hero.skills["bookworm"].value and hero.skills["bookworm"].value > 0) ):
            mike.say "I like to stay home with a good book."
            $ hero.gain_skill("bookworm")
            show fx heart zorder 2 at right
            $ bree.love += 1
            $ hero.knowledge += 5
            show bree happy
            bree.say "Ooh, I like books."
            show bree normal
            show fx drop zorder 2 at left
            show sasha annoyed
            "Sasha gives a loud scoff at [bree.name]'s statement, clearly skeptical."
            mike.say "What about you then, Sasha?"
        "Playing guitar" if not start_plus or not (hero.has_skill("guitar") or (hero.skills["guitar"].value and hero.skills["guitar"].value > 0) ):
            mike.say "I started playing guitar when I was little."
            $ hero.gain_skill("guitar")
            $ hero.charm += 10
            show fx exclamation zorder 2 at left
            show sasha shout
            sasha.say "Pretty sure you play mainly commercial mainstream crap."
            show sasha normal
            "Sasha's comment put a dead stop to the conversation."
            "...."
            mike.say "What about you then, Sasha?"
        "Not really":
            mike.say "Little bit of this and a little bit of that."
            $ hero.knowledge += 6
            $ hero.charm += 8
            $ hero.fitness += 6
            show fx drop zorder 2 at left
            show sasha shout
            sasha.say "That's not much of an answer."
            show sasha normal
            show fx drop zorder 2 at right
            show bree talkative
            bree.say "Yeah..."
            show bree normal
            "Quickly, I move to deflect attention before they start prying."
            mike.say "What about you then, Sasha?"
    show sasha happy
    sasha.say "I drink."
    show sasha shout
    sasha.say "A lot."
    show sasha normal
    mike.say "That's your hobby?"
    show sasha whining
    sasha.say "Well I also listen to heavy metal on full blast, but I guess I'll have to drop that one."
    show sasha annoyed
    "Thank god, I didn't need noise complaints on top of everything else."
    "A short, awkward lull in conversation followed, before I decided to break it with an obvious question."
    show sasha normal
    mike.say "You said you're a student, right [bree.name]? What do you study?"
    show fx exclamation zorder 2 at right
    show bree talkative
    bree.say "Oh, I'm studying to be a doctor."
    show bree normal
    mike.say "Really? Friend of mine just graduated medical school."
    "Wait, maybe telling her that was a bad idea."
    "I don't want Ryan stealing away another hot roommate."
    show bree talkative
    bree.say "Oh wow, tell him I said congrats! It's tough."
    show bree normal
    "Fortunately for me, [bree.name] doesn't seem all that interested in meeting him, letting the conversation move on without another hiccup."
    show bree smile
    bree.say "Nobody's perfect sooooo..."
    bree.say "Can you tell us something bad or shameful about you?"
    show bree normal
    $ BAD = True
    menu:
        "No, nothing...":
            mike.say "Must be one of those rare perfect ones..."
            show bree talkative
            bree.say "You are no fun..."
            show bree normal
            show sasha shout
            sasha.say "Pussy..."
            show sasha normal
            $ hero.knowledge += 2
            $ hero.charm += 2
            $ hero.fitness += 2
            $ BAD = False
        "I am unlucky":
            mike.say "I am pretty unlucky..."
            $ hero.luck -= 1
            $ hero.knowledge += 2
            $ hero.charm += 2
            $ hero.fitness += 2
        "I have some big debt." if not hero.has_item('sports_car'):
            mike.say "I am in debt."
            $ game.flags.debt = 10000
        "Animals hate me" if not start_plus or not (hero.has_skill("animalhated") or (hero.skills["animalhated"].value and hero.skills["animalhated"].value > 0) ):
            mike.say "I am not really an animal person, they don't like me at all."
            $ hero.gain_skill("animalhated")
        "I have a small penis" if not hero.has_skill("hung") and (not start_plus or not(hero.has_skill("smalldick") or (hero.skills["smalldick"].value and hero.skills["smalldick"].value > 0) )):
            mike.say "I... I.. Well I have a small dick actually."
            $ hero.gain_skill("smalldick")
            $ hero.charm -= 10
        "I am prone to erectile problems" if not hero.has_skill("high_libido") and not (hero.has_skill("low_libido") or (hero.skills["low_libido"].value and hero.skills["low_libido"].value > 0) ):
            mike.say "I... I.. Mmmh... No, nothing..."
            $ hero.gain_skill("low_libido")
            $ hero.knowledge += 5

    if BAD:
        show sasha shout
        sasha.say "So? Do anything of note, or is corporate lackey all there is to you?"
        show sasha normal
        "That hit deeper than Sasha realised, but I did a good job covering it up with a fake, confident demeanor."
        menu:
            "I won a marathon":
                mike.say "I won a marathon once."
                $ hero.fitness += 20
                show fx exclamation zorder 2 at right
                show bree happy
                bree.say "Wow, that's really impressive!"
                show bree normal
                mike.say "Thanks [bree.name], took a lot of work."
                "Ryan helped me train for it, he was so pissed when I beat him."
            "I am a people person":
                mike.say "I was the most liked person in all of my classes."
                $ hero.charm += 20
                show fx drop zorder 2 at left
                show sasha whining
                sasha.say "Wow, way to brag."
                show sasha annoyed
                show bree annoyed
                bree.say "Hey, you asked him!"
                mike.say "Don't fight you two."
                show sasha normal
                show bree normal
                "In unison, the pair turned to face me."
                show fx exclamation zorder 2 at right
                show fx exclamation as fx2 zorder 2 at left
                show bree talkative
                bree_sasha "She started it!"
                show bree normal
                "What am I going to do with these two...?"
            "I won a eating contest" if not start_plus or not (hero.has_skill("iron_stomach") or (hero.skills["iron_stomach"].value and hero.skills["iron_stomach"].value > 0) ):
                mike.say "I won a burger eating contest."
                mike.say "Twice."
                $ hero.gain_skill("iron_stomach")
                $ hero.fitness += 5
                show fx drop zorder 2 at left
                show sasha shout
                sasha.say "I am not sure you should be proud of that."
                show sasha annoyed
                mike.say "Really? Because I am proud. Really proud."
                "[bree.name] at the very least seems impressed, although Sasha clearly isn't."
            "I am pretty lucky" if not hero.is_unlucky:
                mike.say "I won the lottery once."
                $ hero.luck += 1
                $ hero.money += 500
                show fx exclamation zorder 2 at right
                show bree happy
                bree.say "Wow! So you can take care of all the rent, right?"
                show bree normal
                mike.say "Oh, it uh, wasn't that much."
                show fx drop zorder 2 at right
                show sasha shout
                sasha.say "Wow, what an accomplishment."
                show sasha normal
            "I was the best in my class.":
                mike.say "I was the top of my class coming out of college."
                $ hero.knowledge += 20
                show sasha shout
                sasha.say "Wow, nerd."
                show sasha normal
                "Sasha acts as though she isn't impressed, but I think I can see through her facade this time. [bree.name] clearly doesn't."
                show fx exclamation zorder 2 at right
                show bree talkative
                bree.say "Hey, he's a hard worker! Don't take that away from him."
                show bree sadsmile
                show sasha shout
                sasha.say "Clearly didn't do him any good with the job he's got."
                show sasha normal
                "Ouch..."
                "Even [bree.name] didn't rush to my rescue for that one. That just makes it worse."
            "I don't sleep" if not start_plus or not (hero.has_skill("no_sleep") or (hero.skills["no_sleep"].value and hero.skills["no_sleep"].value > 0) ):
                mike.say "I once stayed awake for a week straight."
                $ hero.gain_skill("no_sleep")
                $ hero.knowledge += 5
                show fx question zorder 2 at left
                show sasha shout
                sasha.say "And...?"
                show sasha normal
                mike.say "And what?"
                show sasha shout
                sasha.say "If that's the best accomplishment you can think of, I'm sorry for you."
                show sasha normal
                mike.say "..."
                "OK she's got a point."
            "I am hung" if not hero.has_skill("smalldick") and (not start_plus or not (hero.has_skill("hung") or (hero.skills["hung"].value and hero.skills["hung"].value > 0) )):
                mike.say "My exes nicknamed me the horse."
                $ hero.gain_skill("hung")
                $ hero.charm += 10
                show sasha whining
                show bree blank
                show fx drop zorder 2 at left
                sasha.say "Oh, gross."
                show sasha annoyed
                "The pair visibly cringed at my comment, each reeling backwards in disgust."
                "I just wore a dumb smile."
                "It was true, I was larger than most and an animal in the sack, it's one of my best features in fact."
                show bree talkative
                bree.say "Can we just... Forget you ever said that and move on?"
                show bree blank
                show sasha angry
                sasha.say "Seconded."
                show sasha upset
                mike.say "Guys..."
                "I was about to object, but a glare from Sasha cuts me short, so I sigh, and nod in agreement."
            "I have a very high libido" if not hero.has_skill("low_libido") and not (hero.has_skill("high_libido") or (hero.skills["high_libido"].value and hero.skills["high_libido"].value > 0) ):
                mike.say "My exes nicknamed me the machine."
                $ hero.gain_skill("high_libido")
                $ hero.charm += 10
                show sasha whining
                show bree blank
                show fx drop zorder 2 at left
                sasha.say "Oh, gross."
                show sasha annoyed
                "The pair visibly cringed at my comment, each reeling backwards in disgust."
                "I just wore a dumb smile."
                "It was true, I was more enduring than most and an animal in the sack, it's one of my best features in fact."
                show bree talkative
                bree.say "Can we just... Forget you ever said that and move on?"
                show bree blank
                show sasha angry
                sasha.say "Seconded."
                show sasha upset
                mike.say "Guys..."
                "I was about to object, but a glare from Sasha cuts me short, so I sigh, and nod in agreement."
    show sasha normal
    show bree smile
    bree.say "Well, now we all know each other, is it decided?"
    show bree normal
    mike.say "Hmm?"
    "Wait, I DO get the choice?"
    "Both had been so pushy that I'd just accepted them staying here, but suddenly [bree.name] threw the question back at me."
    "Well, [bree.name] seems nice enough, and Sasha is pushy and rude, but I doubt just us two would be able to handle the rent."
    if p:
        "Besides, it looks like she might be interested in going clubbing sometime, maybe she isn't as bad as she makes herself look."
    mike.say "Sure, welcome to the place."
    "[bree.name] silently fist pumps the air again, clearly excited to be here, although this time didn't try to hide it."
    "Sasha however, does try to conceal her joy with being accepted. She might not like us two, but it's a nice place after all."
    "I grin at the slight beginnings of a smile on her lips, but turn away before they can see me."
    mike.say "Alright, couple of things before we start."
    mike.say "The rent and bills are paid on mondays..."
    $ rent = game.get_rent_amount()
    mike.say "I'd say [rent]{image=gui/icons/icon_money.png} from each of us will cover them."
    mike.say "Be sure to have the money ready or you're just going to piss the rest of us off when we have to pay extra."
    mike.say "One of the bedrooms hasn't got any furniture in it, so-"
    show sasha shout
    sasha.say "I'll take that one."
    show sasha normal
    "I'm cut short by Sasha's interruption, but shrug it off. It solves that problem after all."
    mike.say "Then uh... I think that's it."
    show bree happy
    bree.say "Great! That means I can make you help me with my things!"
    show bree normal
    mike.say "Wait, I never agreed to that."
    show bree smile
    bree.say "Aww, come on! They're all outside already!"
    show bree normal
    show sasha shout
    sasha.say "If you brought them all yourself, why'd you need his help?"
    show sasha normal
    show bree smile
    bree.say "He's a guy! They're supposed to help damsels in distress."
    show bree normal
    show sasha shout
    sasha.say "Whatever, I'm out."
    show sasha normal
    mike.say "Where are you going?"
    show sasha whining
    sasha.say "Where'd you think? I didn't bring all my shit with me."
    sasha.say "I didn't come here assuming I'd be given the room like [bree.name] did."
    show sasha annoyed
    show bree happy
    bree.say "But I was right!"
    show bree normal
    show sasha shout
    sasha.say "Yeah. Later."
    show sasha normal
    "I watch Sasha stroll back out of the door and down the street."
    hide sasha with easeoutleft
    show bree at center with ease
    "She had a point, what would [bree.name] have done if they didn't get the room?"
    hide fx
    show fx exclamation zorder 2
    show bree talkative
    bree.say "Hey?"
    show bree normal
    mike.say "Yes...?"
    show bree talkative
    bree.say "Why're you just staring at the door?"
    show bree normal
    mike.say "Just... Thinking."
    show bree happy
    bree.say "Well~ That energy would be better used coming to get my stuff, come on!"
    show bree normal
    "I'm caught by surprise as [bree.name] grasps my wrist, dragging me towards the door before I can resist."
    "I've not known [bree.name] for long, but I can tell it'd be futile to complain."
    scene bg black with timelaps
    scene bg livingroom with timelaps
    "Begrudgingly, I drag the many, many large suitcases she'd stashed around the side of the house."
    "She must have either tried not to seem too eager, or knew I'd never have helped if I knew just how much she'd come with."
    "By the time I'm finished, [bree.name] is beaming at me, but everything hurts and I'm too tired to appreciate her thanks."
    scene bg bedroom1 with timelaps
    "I throw myself onto my bed with a soft thump, and soon drift away to thoughts of the future."
    "Today has taken some twists and turns, but if one thing's for certain, life from now is going to be an adventure..."
    "With friends and roommates like mine, how couldn't it be?"
    $ IN_EVENT_WITH = None
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
