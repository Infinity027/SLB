label amy_date_eat_a_burger:
    amy.say "Mmm...BURGER!"
    "I watch in amazement as Amy starts to tear into her burger."
    "You'd think she was actually starving from the way she's eating!"
    "All I can do is take a bite of my own burger as I stare at the spectacle."
    return

label amy_date_buy_drink:
    amy.say "Looks like I need another drink!"
    amy.say "You want one of the same?"
    if amy.is_visibly_pregnant:
        mike.say "Ah, Amy..."
        mike.say "Should you really be drinking that much?"
        "Amy looks annoyed at the question."
        $ amy.love += 5
        "But then she seems to become aware of the reason I'm asking."
        amy.say "Oh yeah...I guess not!"
        $ hero.cancel_activity()
    else:
        mike.say "I'm just about done with this one."
        mike.say "So count me in!"
        "Amy nods as she starts walking towards the bar."
        amy.say "You got it, [hero.name]."
        amy.say "I'll be right back."
        $ amy.set_flag("drinks", 1, "day", mod="+")
    return

label amy_date_play_darts:
    mike.say "You want to play some darts, Amy?"
    amy.say "Ah...okay, but it's not really my game!"
    "Amy does her best to look like she's enjoying herself."
    "But she wasn't kidding when she said this wasn't her game."
    "She seems to miss the board more often than she hits it!"
    return

label amy_date_pub_play_pool:
    mike.say "Grab a cue, Amy - we're next up on the pool-table!"
    amy.say "If you really want to, [hero.name]..."
    "Amy follows me reluctantly to the table and we get into a game."
    "But it doesn't take me long to realise why Amy wasn't keen."
    "She seems to pot the cue-ball and nothing else the whole game!"
    return

label amy_date_buy_a_round:
    amy.say "It's my round!"
    amy.say "So what's everyone having?"
    if amy.is_visibly_pregnant:
        mike.say "Ah, Amy..."
        mike.say "Should you really be drinking that much?"
        "Amy looks annoyed at the question."
        $ amy.love += 5
        "But then she seems to become aware of the reason I'm asking."
        amy.say "Oh yeah...I guess not!"
        $ hero.cancel_activity()
    else:
        mike.say "I'm just about done with this one."
        mike.say "So count me in!"
        "Amy nods as she starts walking towards the bar."
        amy.say "You got it, [hero.name]."
        amy.say "I'll be right back."
        $ game.active_date.score += 5
        if "rebel" in amy.traits:
            $ game.active_date.score += 5
        $ amy.set_flag("drinks", 1, "day", mod="+")
    return

label amy_dance_with:
    mike.say "Come on, Amy - let's dance!"
    amy.say "Oh yeah, I thought you'd never ask!"
    "Amy beats me onto the dance-floor and then she's totally unstoppable!"
    "It's all that I can do to keep up with her most of the time."
    "And once we're done, I'm exhausted!"
    return

label amy_date_play_arcade_intro:
    mike.say "Hey, Amy - they have a retro arcade game!"
    mike.say "You want to take me on?"
    "Amy hurries over to the machine."
    "And I can see that there's an intense light in her eyes."
    amy.say "Whoa!"
    amy.say "I never knew they had one of these!"
    amy.say "Prepare to have your ass handed to you!"
    return

label amy_date_play_arcade_win:
    "Amy turns out to be pretty damn good at the game."
    "More than once I'm worried that she's going to beat me."
    "But I think that I have a little more experience than she does."
    "As I manage to inch ahead in the dying moments and snatch victory."
    mike.say "I WON!"
    mike.say "I...I mean, well played, Amy."
    amy.say "No way!"
    amy.say "How did you pull that off?!?"
    amy.say "I want a rematch!"
    return

label amy_date_play_arcade_lose:
    "Amy turns out to be pretty damn good at the game."
    "So good in fact that she starts wiping the floor with me!"
    "I do the best I can, calling on all of my experience."
    "But in the end, she's just too good for me."
    amy.say "I WON!"
    amy.say "I...I mean, well played, [hero.name]."
    mike.say "No way!"
    mike.say "How did you pull that off?!?"
    mike.say "I want a rematch!"
    return

label amy_dick_reactions:
    if not amy.flags.seendick:
        $ amy.flags.seendick = 1
        mike.say "Okay, Amy..."
        mike.say "Let's do this!"
        "I turn around, conscious of this being a first."
        "Specifically the first time Amy's seen me naked."
        if hero.has_skill("hung"):
            show dick reactions amy scared
            amy.say "Sweet Jesus!"
            mike.say "Is...is there something wrong?"
            show dick reactions amy smile
            amy.say "NO...no, of course not."
            amy.say "I just wasn't prepared for it to be..."
            amy.say "To be so BIG!"
            $ amy.sub += 10
        elif hero.has_skill("smalldick"):
            show dick reactions amy mock
            amy.say "Oh..."
            amy.say "It's...it's perfectly formed!"
            mike.say "Is...is there something wrong?"
            show dick reactions amy smile
            amy.say "NO...no, of course not."
            show dick reactions amy mock
            amy.say "I'm just...surprised, that's all..."
            $ amy.sub -= 10
        hide dick reactions
    return

label amy_date_intro_valentine_male:
    mike.say "Happy Valentine's day, Amy!"
    mike.say "And thanks for being my valentine too."
    "Amy shoots me a smile and a wink."
    "Both of which show that she likes what I just said."
    amy.say "No problem, [hero.name]."
    amy.say "Nobody else I'd rather spend today with!"
    amy.say "Now let's have some fun, yeah?"
    return

label amy_date_intro_halloween_male:
    mike.say "Whoa, Amy...you look super hot tonight!"
    mike.say "Is this some kind of special occasion?"
    "Amy chuckles and shakes her head."
    "Then she gently elbows me in the ribs."
    amy.say "Don't be a doofus, [hero.name] - it's Halloween, remember?"
    amy.say "The one time a girl like me can dress how she wants."
    amy.say "And not have everyone telling me to save it FOR Halloween!"
    mike.say "Not me, Amy."
    mike.say "I'd love to see you dressed like that all year round!"
    "Amy chuckles again, then wraps her arm around mine."
    return

label amy_date_intro_christmas_male:
    mike.say "Happy Christmas, Amy!"
    amy.say "Happy Christmas to you too, [hero.name]!"
    "Amy's practically beaming at me as she says this."
    "And I can't help smiling back at her too."
    amy.say "Oh, and keep an eye out for mistletoe, okay?"
    mike.say "Really?"
    amy.say "Yeah - because I want a long, hot kiss under the first sprig we see!"
    return

label amy_date_intro_birthday_male:
    mike.say "Happy birthday, Amy!"
    mike.say "I hope you're ready for our date?"
    amy.say "Urgh...yeah, [hero.name]...I am."
    amy.say "It's just Shawn, yeah?"
    amy.say "He knew it was my birthday, he STILL wouldn't let me off early!"
    mike.say "Ah, forget about him, Amy."
    mike.say "He's just jealous of the great time we're going to have tonight!"
    return

label amy_date_intro_mc_birthday_male:
    amy.say "HAPPY BIRTHDAY, [hero.name]!"
    mike.say "Wow, Amy..."
    mike.say "How did you know?"
    amy.say "How do you think?"
    amy.say "I've been bugging Shawn for all the info I can get on you."
    mike.say "Well...I guess I should be flattered!"
    amy.say "Yeah, you should!"
    amy.say "Now let's go have some fun, yeah?"
    return

label amy_halloween_invitation:
    show amy
    "Almost as soon as my housemates and I agree that we're having a Halloween party, my mind turns to who I want to invite."
    "Well, that's not to say that I spend any great amount of time thinking about a long list of potential candidates."
    "What I mean by that is I know almost instantly that I want to invite Amy, and nobody else even comes close!"
    "So the first chance that I get, I just come straight out and ask."
    mike.say "Halloween's almost here, Amy..."
    "As soon as I mention the word Halloween, Amy's face lights up."
    show amy happy
    amy.say "You think I don't know that already, [hero.name]?"
    amy.say "I'm waiting all year for Halloween to come around."
    amy.say "It's the one night when the goths come out and take over the world!"
    "I smile and nod at Amy's answer."
    "Though I wasn't prepared for such a positive reaction."
    mike.say "Oh..."
    mike.say "Sure...of course!"
    mike.say "Erm..."
    mike.say "I was wondering if you already had any plans?"
    mike.say "Because we're having a Halloween party."
    mike.say "My housemates and me, that is..."
    mike.say "At my place, yeah?"
    show amy normal
    "Amy nods, taking in all that I'm saying."
    "But she doesn't say anything in response straight away."
    "Which of course sets me off babbling."
    mike.say "And I..."
    show amy surprised
    mike.say "I wondered if you wanted to come?"
    mike.say "Kind of...as my...my date?"
    mike.say "Oh...and it's a costume party too!"
    if amy.love >= 100:
        "Amy goes quiet for a while."
        "And I can see that she's thinking it over."
        "So when she finally gives me an answer, I'm waiting with baited breath."
        show amy shy
        amy.say "You know what..."
        amy.say "I usually go to one of the big goth club's in town."
        amy.say "And the events they put on last all night long."
        amy.say "Into the early morning of the next day too."
        "I listen to Amy's every word as she explains her Halloween habits."
        "And I'm becoming ever more convinced she's going to blow me off all the time."
        mike.say "Erm..."
        mike.say "That sounds pretty intense!"
        show amy normal
        amy.say "But you know what..."
        amy.say "Maybe it's time to try something new?"
        mike.say "It...it is?"
        show amy happy
        amy.say "Yeah, [hero.name]."
        amy.say "I mean you're something new in my life, right?"
        show amy normal blush
        amy.say "And I've been having fun getting to know you."
        amy.say "So yeah, I guess I will come along to the party."
        "I blink and stare for a moment, stunned into silence."
        mike.say "Th...that's great, Amy!"
        mike.say "I'll let you know the details as soon as I do myself."
        mike.say "Oh, and remember - it's a costume party!"
        show amy -blush
        "Amy nods and gives me a knowing wink."
        amy.say "Oh, don't worry."
        show amy flirt
        amy.say "I have the perfect costume in mind!"
        $ game.flags.halloween_girl = "amy"
    else:
        show amy sad
        "I watch as Amy screws her face up into a pained expression."
        "And at the same time I can feel my heart beginning to sink."
        "As an expression like that can't mean good news."
        amy.say "Oh, [hero.name]..."
        amy.say "That sounds like it'd be a lot of fun, it really does."
        mike.say "But there's a but coming, isn't there?"
        show fx drop
        "Amy nods, looking even more pained than before as she does so."
        amy.say "It's like I already said."
        amy.say "Halloween's such a big deal for me."
        amy.say "I've already had plans made since the start of Fall last year!"
        hide fx
        "I shrug, trying to look like it's not a big deal."
        mike.say "Well..."
        mike.say "Could you maybe come to the party as well?"
        mike.say "You know, like drop in early or come along later?"
        "Amy shakes her head."
        amy.say "That wouldn't work."
        amy.say "I usually go to one of the big goth club's in town."
        amy.say "And the events they put on last all night long."
        amy.say "Into the early morning of the next day too."
        "I keep on racking my brains for a few moments."
        "But then I have to force an awkward smile onto my face."
        "Because Amy's pretty much talked me out of any and all available options."
        "So there's nothing left to do but admit defeat."
        mike.say "Okay, Amy..."
        mike.say "Maybe next year, yeah?"
        show amy normal
        $ amy.love += 1
        amy.say "Maybe, [hero.name]."
        amy.say "But only if you get in early!"
    return

label amy_halloween_arrival:
    scene bg house
    "Opening the door I remind myself to be more cautious this time around."
    "Especially after the incidents with Jack's sword and Scottie's trident."
    "But as soon as I turn my head to look out of the door, I stagger back again."
    with vpunch
    "And it might not be an actual weapon that surprised me this time."
    "But it's certainly a pair of impressive guns!"
    show amy b halloween at center, zoomAt(1.5, (640, 1040)) with vpunch
    mike.say "WHOA!"
    mike.say "Amy..."
    mike.say "Is that really you?!?"
    hide amy
    show amy a halloween
    with fade
    "Amy smiles at my reaction to seeing her in full costume."
    "Then she pulls a cute little pose and throws me the peace sign."
    "Which only serves to make the whole thing that much more impressive!"
    show amy flirt blush
    amy.say "Ha, ha!"
    amy.say "So what do you think, [hero.name]?"
    show amy normal
    amy.say "Do I make a great Misa-Misa, or what?"
    "For the record, Amy's dressed up in a mass of black lace and nylon."
    "And she looks like the perfect Japanese Lolita, topped off with a blonde wig."
    "I recognise the character she's dressed up as from the manga and anime."
    "Amy's right - she does look really great!"
    menu:
        "Compliment":
            "I shake my head as I take a step back."
            "Because I want to be able to take it all in."
            mike.say "I know you said you had your costume all figured out, Amy."
            mike.say "But this is totally more than I was expecting."
            mike.say "It's awesome - and you look SO hot!"
            show amy happy
            "Amy looks delighted with my reaction at first."
            "But then she looks around as if she's afraid of someone else seeing her."
            "And she leans in a little closer too."
            amy.say "That's great to hear, [hero.name]."
            amy.say "I'm so glad that you like it!"
            show amy shy
            amy.say "But...you don't think it's a little..."
            amy.say "Well...too much?"
            "I'm shaking my head again as I try to answer Amy's question."
            mike.say "I don't understand, Amy..."
            mike.say "You look like one of my favourite manga crushes."
            mike.say "Like you just stepped off of the page!"
            amy.say "But the real Misa, she's..."
            amy.say "She's not...as well endowed as me!"
            "Now I can see what Amy means."
            "And she's right."
            "But I don't see why that's a problem."
            mike.say "So what, Amy?"
            mike.say "You're just like the real thing, only better!"
            $ amy.love += 1
            show amy normal
            "This seems to reassure Amy."
            "She nods and takes a step into the hallway."
            amy.say "Okay, [hero.name]..."
            amy.say "So long as you think it's fine."
            show amy -blush
            amy.say "Let's go party!"
        "Criticize":
            "But the problem for me is that she looks TOO good!"
            mike.say "I have to hand it to you, Amy..."
            mike.say "You really managed to pull off Misa Amane."
            show amy happy -blush
            "Amy begins to smile as I compliment her costume."
            show amy surprised at startle
            "But then she frowns with confusion."
            "Because I'm holding up a finger to let her know I'm not finished."
            mike.say "But the problem is you look too good!"
            show fx question
            amy.say "Huh?"
            amy.say "What do you mean?"
            amy.say "You think I'm going to show everyone else's costumes up?"
            hide fx
            amy.say "Is that it?"
            mike.say "No, Amy..."
            mike.say "It's more to do with the fact most of my friends are geeks."
            mike.say "They're going to recognise the costume in a fraction of a second."
            mike.say "And then they're going to freak out."
            mike.say "Because they're seeing their anime crush come to life."
            mike.say "Add alcohol into the mix and it's a recipe for disaster!"
            "Amy looks at me in amazement, shaking her head."
            show amy upset
            $ amy.love -= 2
            amy.say "They're supposed to be adults, [hero.name]."
            amy.say "I'm sure they can control themselves!"
            hide amy with hpunch
            "With that, Amy pushes past me and into the hallway."
            "I don't have the chance to say anything more."
            "All I can do is hurry after her, hoping that she's right."
    scene bg black with dissolve
    pause 1
    return

label amy_halloween_party:
    $ game.pass_time(2)
    scene bg livingroom with dissolve
    "I hear a squeal coming from behind me, so I spin around."
    "And I do so just in time to see Amy backing towards me."
    show amy b halloween sad zorder 3 with easeinright
    amy.say "[hero.name]..."
    amy.say "Help me!"
    show amy at left5 with move
    "Amy's tone surprises me, even leaves me a little alarmed."
    "That is until I glance over her shoulder."
    "Which is when I see [bree.name] and Jack advancing on her from two sides!"
    show amy surprised
    show bree halloween mindless blush zorder 2 at right4 with easeinright
    bree.say "Misa!"
    show jack halloween blush zorder 1 at mostright4 with easeinright
    jack.say "Amane!"
    show bree at startle
    bree.say "Misa Amane!"
    show jack at startle
    jack.say "Amane Misa!"
    show amy sad
    "They have their hands held out before them, reaching for Amy."
    "And their eyes looks kind of glazed over too, probably from the booze."
    "But it does kind of make them look like a couple of zombies!"
    "It doesn't take me long to figure out what's going on here."
    "[bree.name] and Jack are both quite nuts about manga and anime."
    "So they're geeking out over Amy's costume."
    menu:
        "Defend Amy":
            "I step straight in from of [bree.name] and Jack."
            hide amy with easeoutleft
            "And at the same time Amy scuttles behind me too."
            show jack sad
            jack.say "Huh?"
            show bree annoyed -blush
            bree.say "Wha happened?"
            bree.say "Where'd she go?"
            show jack angry
            jack.say "Yeah...where's Misa-Misa?"
            "I frown at them and shake my head."
            mike.say "Misa Amane?"
            mike.say "You mean the anime character?"
            "I let out a laugh and roll my eyes."
            mike.say "How much have you two had to drink?"
            mike.say "Seriously, you think you're seeing fictional characters?"
            show jack surprised
            show bree surprised
            "[bree.name] and Jack exchange a puzzled glance."
            "Then they look back at me again."
            bree.say "You didn't see her?"
            jack.say "B...but...she was right here!"
            show jack sad
            show bree sad
            "I turn to look around the room."
            "And as I do so, Amy follows so that she's still hidden from view."
            mike.say "I don't see her anywhere around here."
            mike.say "Maybe you two should get a little fresh air?"
            "[bree.name] and Jack nod, then wander off to take me up on my advice."
            hide bree
            hide jack
            with easeoutright
            "As soon as they're gone, Amy pops out again."
            show amy halloween with easeinleft
            amy.say "Phew!"
            $ amy.love += 2
            amy.say "Thanks, [hero.name]."
            amy.say "Nerds are pretty scary when they're worked up like that!"
        "Tell Amy to lighten up":
            "I shake my head and let out a sigh."
            mike.say "Don't be silly, Amy."
            mike.say "They're just really into your costume."
            mike.say "Well...that and they're a little drunk!"
            show amy at left with ease
            "Amy makes to hide behind me."
            "But I dodge to the side to stop her."
            show amy surprised at startle
            amy.say "[hero.name]!"
            amy.say "I don't care if they're drunk, high or crazy."
            show amy sad
            amy.say "They're creeping me out!"
            amy.say "Do something!"
            "I shrug and let out a chuckle."
            mike.say "Like what, Amy?"
            mike.say "You don't want me to spoil the party, do you?"
            mike.say "And anyway, you can probably out-run them!"
            $ amy.love -= 4
            show amy surprised
            "Amy lets out another squeal as [bree.name] and Jack charge her."
            hide amy with easeoutleft
            hide bree
            hide jack
            with easeoutleft
            "I watch as the three of them shoot out of the room."
            "And I can't help laughing my ass off at the sight."
            "I know Amy will probably be mad at me when she finally shakes them off."
            "But it was worth it to see what just when down between them!"
    scene bg black with dissolve
    pause 1
    return

label amy_halloween_dance:
    $ game.pass_time(2)
    scene bg livingroom
    show amy halloween
    with dissolve
    amy.say "Ooh..."
    amy.say "Who's in charge of the playlist tonight?"
    "I look around as Amy asks me the question."
    "More than a little confused from the noise and the throng of people around us."
    mike.say "Erm..."
    mike.say "We all threw in a couple of tracks."
    mike.say "But I think Sasha took care of most of it."
    "Amy nods."
    show amy shy
    "And then she points across the room."
    amy.say "That's Sasha, right?"
    amy.say "The metal-chick right there?"
    "I look in the direction that Amy's pointing."
    "And I can see that she's bang on the money."
    mike.say "Yeah, that's Sasha!"
    amy.say "Wow..."
    show amy flirt
    amy.say "Great taste in music AND she's pretty hot!"
    mike.say "Wha...what?!?"
    "Sometimes I almost forget that Amy's into girls as much as she is guys."
    "So realising that she's checking Sasha out kind of catches me off-guard."
    show amy normal
    show fx question
    amy.say "What was that, [hero.name]?"
    mike.say "Oh, nothing, Amy..."
    mike.say "It was nothing at all!"
    hide fx
    amy.say "Okay..."
    amy.say "So what are we waiting for?"
    show amy flirt at center, zoomAt(1.5, (640, 1040))
    amy.say "Let's go dance already!"
    menu:
        "Agree":
            "I can see that Amy's still glancing over towards Sasha."
            "Let's just be clear, I'm not worried because Amy's eyeing up another girl."
            "I'm just worried that she's eyeing up someone that's not me!"
            "So the best thing I can do is make sure her eyes stay on me."
            mike.say "Sure, Amy..."
            mike.say "Of course I'll dance with you!"
            hide amy
            show dance amy halloween
            with fade
            "Taking Amy by the hand, I lead her out onto the dance floor."
            "Or in this case, the middle of our sitting-room floor."
            "And once we're there, I waste no time on giving it my all."
            "I make a point of focussing all of my attention on Amy."
            "Never once glancing in Sasha's direction the whole time."
            "And it seems like my efforts are paying off too."
            $ amy.love += 2
            "Amy clings onto me the whole time, like she's afraid to let go."
            "Pretty soon we're too exhausted to go on any longer."
            "And Amy seems to have forgotten all about Sasha too."
        "Refuse":
            show amy shy
            "I can see that Amy's still glancing over towards Sasha."
            "And if we end up dancing, I just know she'll head straight for her."
            "Let's just be clear, I'm not worried because Amy's eyeing up another girl."
            "I'm just worried that she's eyeing up someone that's not me!"
            mike.say "Ah..."
            mike.say "You know what, Amy..."
            mike.say "I really don't like this one too much."
            mike.say "So I think I'm gonna pass."
            "Of course what I want Amy to say is that she'll pass up the chance to dance too."
            "I mean, that's what I'd do if my date didn't want to hit the dance-floor."
            "Or in this case, the middle of our sitting-room floor."
            "But instead, Amy just shrugs it off."
            show amy annoyed
            amy.say "Whatever you say, [hero.name]."
            amy.say "I'll see you later!"
            hide amy
            $ amy.love -= 2
            "And with that, she turns her back on me."
            show amy halloween shy at left4
            show sasha halloween happy at right4
            with fade
            "The next thing I know, Amy's headed straight towards Sasha."
            "Then I have to stand there, watching them dance like an impotent prick!"
            "As I stand there totally helpless, I make a promise to myself."
            "Next time I'm just going to come right out and say exactly what I mean."
            "That way I won't end up in this kind of mess again."
    scene bg black with dissolve
    pause 1
    return

label amy_halloween_sex:
    scene bg livingroom with dissolve
    "The Halloween party is in full swing when I feel someone grab hold of my hand."
    show amy halloween at center, zoomAt(1.5, (640, 1040)) with dissolve
    "I look down at the hand holding onto mine and then up to see that it's Amy."
    "I mean, I was fully expecting it to be her and nobody else."
    "But it's still a relief to know that my expectations have proven right."
    "And not to see that it's someone else making a play for me out of the blue."
    "I'm just about to say something, but then Amy pulls me towards her."
    show amy flirt blush at center, zoomAt(1.75, (640, 1190))
    amy.say "Come on, [hero.name]..."
    amy.say "What are you waiting for?"
    hide amy with hpunch
    "I stumble a little as she starts to pull me away from the sitting room."
    scene bg black with dissolve
    "And as soon as we're out of there, the volume drops significantly."
    "Most of the guests are concentrated in there, and we're now moving away from them."
    "That means I can be sure that Amy will here me when I ask the inevitable question."
    mike.say "Ah..."
    mike.say "Amy..."
    mike.say "Where are we going?"
    "Amy doesn't stop to answer me."
    "Instead she keeps right on going."
    "But at least she does offer me some kind of an answer."
    amy.say "Where do you think?"
    amy.say "We're sneaking away from the party!"
    mike.say "Yeah..."
    mike.say "I get that part, Amy."
    mike.say "What's puzzling me is exactly why!"
    "Amy doesn't bother to offer any further explanation."
    "Instead she shoves a door open and then bundles me inside."
    "It's a very familiar door, and it should be - because it's the door to my room!"
    scene bg bedroom1 with fade
    "As soon as we're inside and the door is closed behind us, Amy finally explains herself."
    show amy close halloween flirt blush
    "By which I mean that she pushes me up against it and almost leaps into my arms!"
    "I'm not kidding either - I actually have to catch her as her feet leave the ground."
    "Amy lands in my grasp and then proceeds to half hug and half climb me."
    show amy kiss -close with fade
    $ amy.flags.kiss += 1
    "And as soon as she's high enough, she clamps her lips against mine."
    "Now let me just get one thing straight before we go any further."
    "I have absolutely nothing against what Amy's doing right now."
    "I had a little hesitation at being dragged away from the party."
    "But that was just because I'm supposed to be one of the hosts."
    "Now that Amy's got her way and I'm here..."
    "Well, let's just say that I'm more than up for it!"
    "Which I show by taking an even tighter hold of Amy."
    "And then turning her around so that she's the one pressed against the door."
    "Amy squeals in surprise, and then moans as I return the kiss with renewed passion."
    "Somehow she still manages to sneak out a few words, even as I'm doing it!"
    amy.say "The...the bed..."
    amy.say "Take me...to the...bed!"
    "I nod eagerly as I try to do what she asks of me."
    "Normally carrying her a short distance would be pretty easy."
    "But right now Amy's still trying to climb all over me."
    "Plus my cock is starting to get hard as well."
    "And it's caught at an awkward angle in my pants!"
    "All of this means that I half carry and half stagger to the bed."
    "Once we get there, I pretty much fall forwards onto it too."
    scene bg bedroom1 at dark, center, zoomAt(1.5, (940, 720))
    show amy close halloween flirt blush
    with vpunch
    "As soon as we hit the mattress, Amy leaps into action."
    "She comes up on top, straddling my waist and pinning me down."
    "Amy wraps her hands in mine, pushing them into the pillows above my head."
    show amy normal
    amy.say "Admit it, [hero.name]!"
    "She pushes down with all her weight as she says this."
    mike.say "Whoa..."
    mike.say "What, Amy?"
    mike.say "Admit what?!?"
    show amy happy
    amy.say "That you always wanted to fuck Misa!"
    amy.say "When you read the manga or watched the anime."
    amy.say "You always wished you could have your way with her!"
    show amy flirt
    "I think about denying it for a moment."
    "But then what will that get me?"
    mike.say "Y...yeah, Amy..."
    mike.say "I did!"
    mike.say "I always wanted to reach under her skirt..."
    mike.say "Reach under it and feel her pussy!"
    "As she listens to my confession, Amy starts to nod."
    "At the same time her eyes seem to get ever wider."
    "So much so that part of me thinks she's actually turning into an anime character!"
    show amy happy
    amy.say "Oooh..."
    amy.say "That is SO hot!"
    amy.say "Do that to me - do it right now!"
    show amy at top_to_bottom
    "Amy yanks one of my hands down from above my head."
    show amy finger
    "And then she shoves it under her skirt."
    "I hardly have time to react before she pushes my fingers between her thighs."
    "As soon as she does, I realise two things."
    "The first is that she's not wearing any panties."
    "Though couldn't say if she slipped them off without me seeing."
    "Or if she never had any on to begin with."
    "And the second is that she's already wet to the touch!"
    "Oh, and there's a third thing too."
    "If you count the fact I just realised I'm totally at her mercy!"
    "That I'm going to do whatever the hell she tells me to!"
    "Amy releases my other hand so that she can fumble with my flies."
    "And I do the best I can to help her with my newly-freed hand."
    "I don't once think of using the other one to speed things up."
    "Because that one's still stroking the lips of her pussy the whole time."
    "It's only when Amy finally has my cock out that the spell seems to break."
    show amy halloween naked flirt blush at bottom_to_top with dissolve
    "And in that moment we start tearing off each other's clothes."
    "I don't know if we manage to get naked before it actually happens."
    hide amy
    show amy cowgirl halloween pleasure vaginal
    with fade
    "But somewhere along the way, Amy pushes it hard against her lips."
    "And then there's nothing between us at all."
    show amy cowgirl down ahegao
    "We both gasp in surprise as I sink into her."
    "Because it's not slow or subtle in any way."
    "Instead Amy pushes down hard and I literally plunge into her."
    "All of her weight is on me, which means I go as deep as possible."
    "Amy's eyes go wide again, but this time it's for a different reason."
    "I can see that the sensations she's feeling are almost too much."
    "From the look on her face, she looks like she's going to explode!"
    "But it's already too late for me to think about taking things slow."
    "And even as I'm looking at her, my body's already springing into action."
    "I'm determined to give Amy what she wants, and nothing's going to stop me."
    show amy cowgirl mikehand
    "My hands reach up and take hold of Amy's waist."
    "The grip I have on her tightens as my own body starts to move beneath her."
    "And from that moment on, I don't stop or hesitate once."
    show amy cowgirl up
    pause 0.45
    show amy cowgirl down at startle(0.05,-10)
    pause 0.45
    show amy cowgirl up
    pause 0.45
    show amy cowgirl down at startle(0.05,-10)
    pause 0.45
    show amy cowgirl up
    pause 0.45
    show amy cowgirl down at startle(0.05,-10)
    "The only thing that I focus on is the sight of Amy above me."
    "That and how my motions are affecting her."
    "Amy has her hands on my shoulders, holding herself up."
    "Or maybe it'd be more accurate to say that she's bracing herself."
    "Because she's also bouncing up and down atop me like someone on a bucking horse!"
    show amy cowgirl up pleasure
    pause 0.35
    show amy cowgirl down speed at startle(0.05,-10)
    pause 0.35
    show amy cowgirl up
    pause 0.35
    show amy cowgirl down at startle(0.05,-10)
    pause 0.35
    show amy cowgirl up
    pause 0.35
    show amy cowgirl down -speed at startle(0.05,-10)
    "Amy gasps and moans as I put all of my energy into pleasing her."
    "And those incredible breasts of hers are swinging wildly."
    "At times they seem to be able to hide her face from me."
    "At others I think they're going to swing down and hit me in the face!"
    show amy cowgirl up
    pause 0.35
    show amy cowgirl down speed at startle(0.05,-10)
    pause 0.35
    show amy cowgirl up
    pause 0.35
    show amy cowgirl down at startle(0.05,-10)
    pause 0.35
    show amy cowgirl up
    pause 0.35
    show amy cowgirl down -speed at startle(0.05,-10)
    "Amy's buttocks are likewise slapping against my thighs."
    "The sound is like someone clapping their hands together."
    "In fact the noises that her body is making seem to drown out her cries."
    "So much so that I have no idea Amy's on the brink of losing it."
    "My only warning comes when she sinks her nails into my shoulders."
    "At the same time Amy squeezes me with her thighs too."
    show amy cowgirl up
    pause 0.25
    show amy cowgirl down speed at startle(0.05,-10)
    pause 0.25
    show amy cowgirl up
    pause 0.25
    show amy cowgirl down -speed at startle(0.05,-10)
    mike.say "Oh..."
    show amy cowgirl up
    pause 0.25
    show amy cowgirl down speed at startle(0.05,-10)
    pause 0.25
    show amy cowgirl up
    pause 0.25
    show amy cowgirl down -speed at startle(0.05,-10)
    mike.say "Oh shit!"
    show amy cowgirl up
    pause 0.15
    show amy cowgirl down speed at startle(0.05,-10)
    pause 0.15
    show amy cowgirl up
    pause 0.15
    show amy cowgirl down at startle(0.05,-10)
    pause 0.15
    show amy cowgirl up
    pause 0.15
    show amy cowgirl down at startle(0.05,-10)
    pause 0.15
    show amy cowgirl up
    pause 0.15
    show amy cowgirl down at startle(0.05,-10)
    pause 0.15
    show amy cowgirl up
    pause 0.15
    show amy cowgirl down ahegao cum -speed with vpunch
    $ amy.love += 5
    pause 0.35
    show amy cowgirl up
    pause 0.35
    show amy cowgirl down with vpunch
    pause 0.5
    show amy cowgirl up
    pause 0.5
    show amy cowgirl down with vpunch
    pause 0.75
    show amy cowgirl up
    "The sudden shock of Amy's reaction is enough to make me cum too."
    "I can feel my hands sinking into the soft flesh of her buttocks."
    "And the sensation of her muscles twitching as I lose it inside of her."
    show amy cowgirl down pleasure at startle
    "Finally Amy's muscles seem to lose the strength support her."
    "She falls sideways, rolling off me and onto the mattress."
    "Part of me knows that we should get up and get dressed."
    "Someone's bound to miss us sooner or later."
    "But right now there's no hope of doing anything but lying right here."
    "Waiting for my mind and senses to come back down to earth."
    $ amy.sexperience += 1
    $ game.pass_time(1)
    return

label amy_date_forest_male:
    scene bg forest
    show amy
    with fade
    "I'm never sure if asking a girl like Amy to come along on a hike is a good idea or not."
    "Sure, you shouldn't assume every goth you meet is going to fit the stereotype."
    "But most of them you meet aren't exactly into getting exercise in the fresh air."
    "Because it's not going to help them keep a pale and pasty complexion, now is it?"
    "That said, Amy seemed quite keen on coming along when I asked her."
    "And so far she's not shown any sign of flagging or not wanting to be here."
    "In fact she seems to be enjoying the sights and sounds of nature."
    "So much so that it's me who suggests we stop and take a rest first!"
    mike.say "Let's take a break over there, Amy."
    mike.say "I think I have a rock in my boot or something."
    mike.say "And I bet the view is pretty nice too."
    show amy shy
    "Amy gives me a sideways glance, as if she doesn't quite believe me."
    "But she nods all the same."
    show amy normal
    amy.say "Okay, [hero.name]."
    amy.say "We can take a break if you like."
    show amy flirt
    amy.say "But just for the record, I'm not the one that's getting tired!"
    "I roll my eyes as I walk off the track and over to the spot I pointed out."
    "It's just far enough away to be out of earshot if anyone else walks past."
    "And there are a few trees that should hide us once we're sitting down."
    "Not that I picked it out for those reasons."
    "It's just nice to have a little privacy while we're relaxing."
    "I sit down first, choosing a comfortable-looking spot."
    "And then I make a point of taking off my boots to check for the rock I mentioned before."
    show amy happy
    "Amy seems to find this funny, chuckling and shaking her head as she watches me."
    "Feeling a little insulted, I palm a stone from the ground."
    "I do it when I'm sure she can't see me, and then hold it up."
    show amy surprised at center, startle
    mike.say "There it is!"
    amy.say "There what is?"
    mike.say "The rock that was in my boot."
    mike.say "See, Amy?"
    mike.say "That'll teach you to call me a liar!"
    show amy upset
    amy.say "Let me see that!"
    amy.say "It looks massive even from over here."
    amy.say "I'll bet you couldn't even fit your foot in there with it!"
    "Amy makes a grab for the stone, but I pull in out of her reach."
    show amy angry at center, startle
    amy.say "Hey!"
    amy.say "Gimmie that thing!"
    "Amy makes a second grab for the stone."
    "But this time she lunges at me like she means business."
    "Unprepared for this, I don't have time to get out of the way."
    show amy at center, zoomAt(1.85, (640, 1240)) with vpunch
    "Which means that she pretty much lands on top of me."
    "We roll around on the ground together after that."
    show amy blush
    "Amy still trying to grab the stone while I try to keep it from her."
    "But I slowly become aware of something else too."
    show amy upset
    "Amy's grunting and shoving, pressing her body against mine."
    "I can feel her breath in my ear she's so close to me right now."
    "So why in the hell are we even fighting over a dumb rock?"
    show amy normal
    "A moment later I get a sure sign that Amy's thinking the exact same thing."
    "Because I feel her hand on my groin, squeezing me in a suggestive manner!"
    show amy flirt
    "But then, is there any other way of squeezing a guy's manhood?"
    amy.say "We're out of sight here, right?"
    amy.say "No one can see us from the path, yeah?"
    "I nod hastily, not totally sure I'm telling Amy the truth."
    "The sensation of her hands on me is making me desperate."
    "I'd probably say yes to anything she asked me right now."
    "Whatever it takes to keep her doing what she's doing."
    mike.say "Yeah, Amy..."
    mike.say "That's why I picked this spot!"
    mike.say "We can do whatever we want here..."
    mike.say "Nobody will see!"
    amy.say "Good, good..."
    amy.say "That's just what I wanted to hear!"
    hide amy
    show amy normal blush
    with fade
    "Much to my disappointment, Amy lets go of my cock."
    "But then I see that she's doing so to pull off her top."
    "Which is more than enough to make up for it!"
    "I hurry to follow her lead."
    show amy underwear with dissolve
    "And pretty soon we're both down to our underwear."
    show amy topless with dissolve
    "Amy's unhooking her bra as I pull down my shorts."
    "As soon as I see those amazing breasts set free, that's it."
    "I feel like I can't hold on any longer, not even for a second."
    "I know that I have to have Amy, and right now!"
    show amy flirt
    "She seems to see the hunger in my eyes too."
    "And seeing it doesn't deter her for a second."
    "I'm so drawn to her breasts I almost don't notice what she's doing."
    show amy naked with dissolve
    "Only when Amy tosses her panties straight in my face do I snap out of it!"
    hide amy
    show amy missionary forest
    with fade
    "Amy lies down giving me an unhindered view of her body."
    amy.say "Come on then, [hero.name]..."
    amy.say "What are you waiting for?"
    amy.say "I always wanted to make love in the bosom of nature!"
    mike.say "There's only one bosom I'm interested in Amy!"
    show amy missionary mike
    "With that I pretty much pounce on Amy."
    "Of course she's not trying to get away from me."
    "But all the same she puts on a good show."
    "Amy giggles and squeals, wriggling around under me."
    amy.say "Get on with it!"
    amy.say "Ravish me already!"
    "It looks like Amy wants me to take control here."
    "So I make a point of parting her legs as I lean over her."
    "And as her thighs spread, I can see what I'm after."
    "Once I do, I don't need any more encouragement!"
    menu:
        "Fuck her pussy":
            "Amy's pussy is calling to me."
            "I feel like it's the only thing on my mind right now."
            "I can already image the sensation of sinking into it."
            if amy.flags.buttplug:
                "But just before I can make it happen, Amy holds up a hand."
                amy.say "Wait..."
                amy.say "I wondered if..."
                amy.say "If we could use this?"
                "I look down and see that Amy's holding something small and made of rubber."
                "Then my eyes go wide as I realise that it's a butt-plug!"
                menu:
                    "It's no power cord but I'll plug it in anyway":
                        show amy missionary -mike
                        "Taking the plug from Amy, I nod."
                        mike.say "Sure thing, Amy."
                        mike.say "Do I need to..."
                        amy.say "No need for anything fancy, [hero.name]."
                        amy.say "Just push it right in there!"
                        show amy missionary hurt
                        "I nod and then set about doing as I'm told."
                        "Amy must have done this before."
                        "Because her ass only resists for a short time."
                        $ amy.sub += 1
                        show amy missionary buttplug pleasure
                        "Then the plug slides into her slowly."
                        "She moans with pleasure as it fills her ass."
                        "The sound of which only makes me more eager be inside of her myself!"
                    "Only I have the right to penetrate those forbidden lands":

                        "I shake my head, showing my disapproval."
                        mike.say "No time for that now, Amy."
                        mike.say "I want to get inside of you."
                        mike.say "And I'm not waiting a second longer!"
                        "Amy looks a little disappointed."
                        "But she nods all the same."
                        amy.say "Okay, okay..."
                        amy.say "Maybe next time."
            show amy missionary normal mike
            "I can feel myself getting ever more excited."
            "Almost holding my breath until my cock reaches its target."
            "And the moment that it does, it's my turn to moan."
            show amy missionary pleasure vaginal
            "Amy feels warm and slick, totally welcoming too."
            "But as I begin to push my way inside, there's still resistance."
            "Not that it's going to put me off, as I can see the look on her face."
            "Amy wants this every bit as much as I do."
            "It's like I can feel her desire softening the muscles down there."
            "The more she wants it the more they begin to melt and give way."
            show amy missionary orgasm
            "All of a sudden I feel her body surrender to me."
            "And all of the force I've been using makes me sink deep into her."
            "Before I know it, I'm all the way inside."
            "And now both of us are moaning and panting together."
            "I could stay like this forever."
            "Buried deep inside of Amy, our eyes locked together."
            "But then, all of a sudden, I seem to remember where we are."
            "The realisation fills me with equal measures of fear and excitement."
            "We could get caught doing this!"
            "We could be discovered any second!"
            show amy missionary lock pleasure
            "I can't help beginning to move inside of Amy."
            "I don't know if she's feeling the same things as I am."
            "But the effect that this has on her is instant and dramatic."
            "In what feels like no time at all I'm going as fast as I can."
            "And Amy's nodding like her life depends on my keeping it up!"
            "The truth is that I don't need any encouragement."
            "Nothing could come between me and the task at hand."
            "Part of me wants to throw caution to the wind and shout out loud."
            "Not to care about getting caught."
            "But another wants me to get the job done as soon as possible."
            "To push myself to the limit and force a climax."
            "In the end, Amy takes the choice out of my hands."
            show amy missionary orgasm
            "She begins clutching at her breasts."
            "Her hands are massaging them."
            "Almost kneading them like dough!"
            "I get the vague notion that she's trying to bleed off the tension."
            "To find another way to release what she's feeling."
            "But it doesn't seem to be working."
            show amy missionary pleasure
            "Because a moment later, I can feel her starting to cum."
            "And when that happens, there's no way I can hold on."
            "The only thing I can do is decide how I'm going to end this!"
            menu:
                "Cum inside":
                    "Amy's muscles squeeze me one last time."
                    "And then it happens."
                    show amy missionary cum ahegao with vpunch
                    $ amy.love += 2
                    $ amy.impregnate()
                    "I shoot my load into her, moaning as I do so."
                    mike.say "Oh..."
                    with vpunch
                    mike.say "Oh fuck!"
                    show amy missionary spread orgasm out bodycum -cum with vpunch
                    "I only realise that I just shouted out loud when it's too late."
                    "But luckily for me, Amy's too out of it to even notice."
                "Pull out":
                    show amy missionary spread out
                    "I pull my cock out of Amy, even as her muscles squeeze me one last time."
                    "And then it happens."
                    show amy missionary orgasm cum with hpunch
                    $ amy.love += 1
                    "I shoot my load over Amy's belly, moaning as I do so."
                    mike.say "Oh..."
                    with hpunch
                    mike.say "Oh fuck!"
                    show amy missionary pleasure bodycum -cum with hpunch
                    "I only realise that I just shouted out loud when it's too late."
                    "But luckily for me, Amy's too out of it to even notice."
        "Fuck her ass":
            "Amy's ass is calling to me."
            "I feel like it's the only thing on my mind right now."
            "I can already image the sensation of sinking into it."
            "I can feel myself getting ever more excited."
            "Almost holding my breath until my cock reaches its target."
            "And the moment that it does, it's my turn to moan."
            show amy missionary pleasure anal
            "Amy feels warm and tight, totally welcoming too."
            "But as I begin to push my way inside, there's still resistance."
            "Not that it's going to put me off, as I can see the look on her face."
            "Amy wants this every bit as much as I do."
            "It's like I can feel her desire softening the muscles down there."
            "The more she wants it the more they begin to melt and give way."
            show amy missionary orgasm
            "All of a sudden I feel her body surrender to me."
            "And all of the force I've been using makes me sink deep into her."
            "Before I know it, I'm all the way inside."
            "And now both of us are moaning and panting together."
            "I could stay like this forever."
            "Buried deep inside of Amy, our eyes locked together."
            "But then, all of a sudden, I seem to remember where we are."
            "The realisation fills me with equal measures of fear and excitement."
            "We could get caught doing this!"
            "We could be discovered any second!"
            show amy missionary lock pleasure
            "I can't help beginning to move inside of Amy."
            "I don't know if she's feeling the same things as I am."
            "But the effect that this has on her is instant and dramatic."
            "In what feels like no time at all I'm going as fast as I can."
            "And Amy's nodding like her life depends on my keeping it up!"
            "The truth is that I don't need any encouragement."
            "Nothing could come between me and the task at hand."
            "Part of me wants to throw caution to the wind and shout out loud."
            "Not to care about getting caught."
            "But another wants me to get the job done as soon as possible."
            "To push myself to the limit and force a climax."
            "In the end, Amy takes the choice out of my hands."
            show amy missionary orgasm
            "She begins clutching at her breasts."
            "Her hands are massaging them."
            "Almost kneading them like dough!"
            "I get the vague notion that she's trying to bleed off the tension."
            "To find another way to release what she's feeling."
            "But it doesn't seem to be working."
            show amy missionary pleasure
            "Because a moment later, I can feel her starting to cum."
            "And when that happens, there's no way I can hold on."
            "The only thing I can do is decide how I'm going to end this!"
            menu:
                "Cum inside":
                    "Amy's muscles squeeze me one last time."
                    "And then it happens."
                    show amy missionary cum ahegao with vpunch
                    $ amy.sub += 2
                    "I shoot my load into her, moaning as I do so."
                    mike.say "Oh..."
                    with vpunch
                    mike.say "Oh fuck!"
                    show amy missionary orgasm with vpunch
                    "I only realise that I just shouted out loud when it's too late."
                    "But luckily for me, Amy's too out of it to even notice."
                "Pull out":
                    show amy missionary spread out
                    "I pull my cock out of Amy, even as her muscles squeeze me one last time."
                    "And then it happens."
                    show amy missionary orgasm cum with hpunch
                    $ amy.love += 1
                    "I shoot my load over Amy's belly, moaning as I do so."
                    mike.say "Oh..."
                    with hpunch
                    mike.say "Oh fuck!"
                    show amy missionary pleasure bodycum -cum with hpunch
                    "I only realise that I just shouted out loud when it's too late."
                    "But luckily for me, Amy's too out of it to even notice."
    $ amy.sexperience += 1
    $ game.active_date.stay = False
    $ DONE["amy_date_forest"] = game.days_played
    scene bg forest
    call sleep (sleep_room="forest") from _call_sleep_76
    $ game.pass_time((7 - game.hour) if game.hour <= 7 else (7 + (24 - game.hour)))
    $ game.room = "street"
    scene bg street with fade
    return

init python:
    Event(**{
    "name": "amy_date_park",
    "label": "amy_date_park_male",
    "duration": 1,
    "priority": 500,
    "conditions": [
        IsTimeOfDay("afternoon"),
        HeroTarget(
            IsGender("male"),
            OnDate(),
            IsRoom("date_park")
            ),
        PersonTarget("amy",
            OnDate(),
            MinStat("love", 100),
            MinStat("sub", 10),
            )
        ],
    "do_once": True
    })

label amy_date_park_male:
    scene bg street
    show amy casual
    "It's a bright day with a sky that's perfectly blue and free of clouds."
    "So it's a no-brainer to take full advantage and suggest a stroll to Amy."
    "I mean, she's a goth, so part of me is expecting her to laugh in my face."
    "But to my surprise, she actually seems to be more than up for it."
    "And that's how I find myself walking down the street holding her hand."
    "The problem is that I have no idea where in the hell we're going!"
    "I was so sure that Amy would say no I never thought that far ahead."
    "Luckily for me, I see the entrance to the park ahead."
    "As we reach them, I turn and walk us through the gates."
    mike.say "Here we are, Amy."
    show amy annoyed
    amy.say "Oh great, the park..."
    amy.say "How original and romantic of you!"
    mike.say "Huh?"
    mike.say "You don't like the park?"
    mike.say "Is it too colourful for you or something?"
    show amy happy at startle
    "Amy bursts out laughing and shakes her head."
    amy.say "Oh, [hero.name]..."
    amy.say "You're so gullible!"
    show amy normal
    amy.say "I was just being sarcastic, that's all."
    mike.say "So you're okay with the park?"
    amy.say "Yeah, I'm fine with the park."
    show amy blush
    amy.say "Anywhere's cool, so long as I'm with you!"
    "I can't help feeling a boost of confidence at Amy's words."
    "And I stride into the park with a bounce in my step."
    scene bg park
    show amy casual
    with fade
    "Once we're inside, we do all of the stuff you're supposed to do."
    "We stroll, arm-in-arm, along all of the pleasant footpaths."
    "We lean on the parapets of the bridges over the burbling streams."
    "And we even push each other on the swings in the playground."
    "But I think the reason that we get away with the last one is pretty obvious."
    "Despite the fact that it's a nice day, the park is strangely quiet."
    "In fact, I doubt we've seen a dozen people in total since we arrived."
    "And I feel like I have to say as much to Amy as we take a seat on a bench."
    call amy_fuck_date_park_male from _call_amy_fuck_date_park
    return

label amy_date_amusement_park_male:
    scene bg amusement
    show amy sadsmile
    with fade
    "I'm always pretty eager to get through the gates at the amusement park."
    "Because when I'm this close I can feel my heart starting to beat faster."
    "And my mind is filled with the excitement of getting on the rides."
    "Which is why I find it strange to feel something holding me back."
    "At first I think it must be something in the back of my mind."
    "Something that I've forgotten to take care of before coming here."
    "But much to my surprise, I realise it's an actual physical force."
    "And looking down at my hand, I see that it's Amy hanging onto it."
    "Stopping in my tracks, I turn around to see what the problem is."
    show amy worried
    mike.say "Amy..."
    mike.say "Are you feeling okay?"
    mike.say "Because it kind of feels like you're dragging your feet!"
    "Amy looks conflicted as she listens to my question."
    show amy normal
    "But she manages to force a smile onto her face."
    show amy happy
    amy.say "I'm just not that into this kind of place, [hero.name]."
    amy.say "I know it sounds crazy to admit it now."
    amy.say "But they're not really my thing."
    show amy sadsmile
    "I find myself staring at Amy in amazement."
    mike.say "Really?"
    mike.say "I thought everyone liked amusement parks?"
    show amy whining
    amy.say "Not everyone..."
    show amy lying
    amy.say "But we're here now."
    amy.say "So I guess I'll try to make the best of it."
    show amy normal
    "All I can do is nod and then gesture towards the entrance."
    "Hoping all the time I can find a way to make this work for Amy."
    return

label amy_date_ferris_wheel_male:
    "As soon as I see the Ferris Wheel, I know we have to go on it."
    "It's such a classic amusement park ride, Amy's sure to like it."
    mike.say "Let's ride the Ferris Wheel, Amy."
    mike.say "Right over there."
    amy.say "Okay, [hero.name]..."
    amy.say "If that's what you want to do."
    "I do the best I can to ignore Amy's less than enthusiastic reaction."
    "And soon enough we're sitting on the ride, waiting for it to start."
    "When it does there's nothing to say until we reach the top."
    "We just rise up steadily, getting higher with every second that passes."
    "Amy has a neutral expression on her face as all this is happening."
    "She glances here and there, seeming to be taking it all in."
    "But even when we reach the top and the ride stops, she still stays silent."
    mike.say "Erm..."
    mike.say "What do you think of the view, Amy?"
    mike.say "Pretty impressive, right?"
    "Amy glances this way and that."
    "And then she nods."
    "But she really doesn't seem that impressed."
    amy.say "Yeah, I know..."
    amy.say "But we could have gotten higher."
    amy.say "You know, by going onto the roof of a tall building?"
    "All I can do is nod and shrug as we start to descend."
    "So it seems like the Ferris Wheel isn't going to impress Amy at all."
    $ amy.love += 0
    $ game.active_date.score += 0
    return

label amy_date_merry_go_round_male:
    mike.say "Let's ride the Merry-Go-Round, Amy."
    mike.say "That's a good place to start, right?"
    "Amy looks over the ride in question."
    "And then she makes a kind of shrugging motion."
    amy.say "Ah..."
    amy.say "I guess so."
    amy.say "What have I got to lose?"
    mike.say "That's the spirit!"
    mike.say "Come on, Amy..."
    "Together we climb onto the ride and find a place to sit."
    "Then we sit tight, waiting for it to start up."
    "And if I'm honest, I'm waiting to see Amy get excited too."
    "To my delight, it doesn't take long for her to become animated."
    "But things take a turn for the worse a moment later."
    "Because that's when I realise she's not enjoying herself at all."
    amy.say "Oh no..."
    amy.say "Oh god no..."
    mike.say "What's the matter, Amy?"
    mike.say "Are you okay?"
    amy.say "No..."
    amy.say "I'm not..."
    amy.say "I'm going to puke!"
    "I can see that Amy's not kidding too."
    "She's turning a worrying shade of green right in front of my eyes!"
    "As soon as the ride stops, she staggers off it."
    "And then she runs to the nearest bathroom to throw-up."
    $ amy.love -= 2
    $ game.active_date.score -= 20
    return

label amy_date_haunted_house_male:
    "As soon as I see the Haunted House, I know that we have to go in there."
    "Because Amy's a goth, and goth's love all that spooky stuff, right?"
    mike.say "Let's do the Haunted House, Amy."
    mike.say "Doesn't it look great?"
    "Amy looks the exterior of the ride up and down."
    "And she doesn't look like she agrees with me."
    amy.say "If you want to, [hero.name]."
    amy.say "Then I suppose we can try it."
    "I take that as a resounding yes, and hurry to join the queue."
    "It's pretty short, and so we're soon inside the Haunted House."
    "I do the best I can to show that I'm enjoying myself."
    "Jumping at all the right moments and screaming as loud as I can."
    "But Amy doesn't seem to share my enthusiasm."
    "In fact the whole place seems to bore her rigid."
    "So once we're walking out of there, I ask her what's wrong."
    mike.say "Didn't you like that, Amy?"
    mike.say "I thought you were into all that kind of thing?"
    amy.say "Being a goth isn't all about silly Halloween costumes, [hero.name]."
    amy.say "There's a bit more to it than that!"
    $ amy.love -= 1
    $ game.active_date.score -= 10
    return

label amy_date_love_boat_male:
    "As we walk past the Love Boat, an idea starts to form in my head."
    "That could be just the kind of thing Amy would be into."
    "And it'd also be the perfect chance to have some time alone with her."
    mike.say "Shall we ride the Love Boat, Amy?"
    mike.say "The queue doesn't look very long."
    "Amy doesn't look super enthusiastic."
    amy.say "Yeah..."
    amy.say "But that could be because it's a shitty ride!"
    mike.say "Or because it's a short ride?"
    amy.say "Could be a shitty short ride?"
    mike.say "But at least it'd still be short, right?"
    "Amy relents, nodding her head as we walk towards the ride."
    "Climbing into a boat, we soon find ourselves sailing into the tunnel."
    "And that's when there's the first sign of things going wrong."
    "Suddenly I feel Amy clinging onto me."
    "And I can tell from the way she does it that she's super-tense."
    amy.say "Why is it so dark?"
    amy.say "Where are we going?"
    amy.say "How deep is the water?!?"
    "I do the best I can to calm Amy down."
    "And more than once I'm tempted to try to stop the ride."
    "But I can't help thinking that would do more harm than good."
    "So I keep holding onto her until it's over."
    "Doing all that I can to comfort her and vowing not to do this again."
    $ amy.love -= 1
    $ game.active_date.score -= 10
    return

label amy_date_hedge_maze_male:
    mike.say "Let's do the Hedge Maze, Amy..."
    mike.say "What do you think?"
    "Amy doesn't look convinced as she looks the attraction over."
    amy.say "A maze made out of hedges?"
    amy.say "What's exciting about that?"
    mike.say "Oh come on, Amy..."
    mike.say "Just give it a chance."
    mike.say "If it sucks, then we can walk straight out."
    amy.say "Okay, okay..."
    amy.say "Let's do it, before I change my mind."
    "Amy takes hold of my hand and together we walk into the maze."
    "At first she seems less than impressed by what she sees."
    "But when I duck around a corner and out of sight..."
    "Well that's when things start to change."
    amy.say "Hey..."
    amy.say "Where are you going?"
    mike.say "It's a maze, Amy..."
    mike.say "You have to come find me!"
    "Amy lets out a squeal of alarm as I hurry away."
    "And that sound is how I know that she's right on my heels."
    "We rave around the maze like that for what feels like hours."
    "And by the time we reach the centre, we're both panting for breath."
    "But I note that Amy's laughing at the same time."
    "Which tells me that she's enjoying the experience."
    "So maybe places like this are her kind of thing after all."
    $ amy.love += 3
    $ game.active_date.score += 30
    return


label amy_date_amusement_ice_cream_male:
    amy.say "Ooh..."
    amy.say "Ice-cream!"
    "I turn my head at the sound of Amy's voice."
    "And I see that she's staring at the ice-creams in the hands of people walking by."
    "All of them are pretty impressive, colourful and piled high with sweet sprinkles."
    mike.say "Are you trying to drop a hint, Amy?"
    mike.say "I mean, those things are pretty colourful."
    mike.say "I don't think they come in black and white!"
    "Amy frowns a little at my attempt to be funny."
    "And she plants her balled fists on her hips too."
    amy.say "Hey!"
    amy.say "You know that's anti-goth prejudice?"
    amy.say "We don't want everything to be black and white."
    amy.say "And we do like to have fun things too - like ice-cream!"
    "I hold up my hands in a gesture of surrender."
    mike.say "Geez, Amy..."
    mike.say "You could just say that you want an ice-cream."
    mike.say "There's no need for the lecture!"
    "I find myself scurrying over to the ice-cream stand a moment later."
    "Where I order the one that Amy points to on the menu."
    "When she gets it, the thing looks like an explosion in a rainbow factory."
    "But the smile on Amy's face is huge and seems to be totally genuine too."
    "So I take it as a win and devote myself to enjoying my own ice-cream as we walk away."
    $ amy.love += 1
    $ game.active_date.score += 10
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
