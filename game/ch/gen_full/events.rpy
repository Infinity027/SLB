init python:
    Event(**{
    "name": "ryan_bus",
    "label": "ryan_bus",
    "conditions": [
        IsDone("cleaning_attic"),
        Or(
            IsDone("samantha_event_A02"),
            IsDone("samantha_event_B04"),
            IsDone("samantha_event_C03"),
            ),
        HeroTarget(
            IsRoom("map"),
            IsFlag("dwaynedead", True),
            IsFlag("dannydead", True),
            ),
        ],
    "priority": 500,
    "music": "music/darren_curtis/come_out_and_play.ogg",
    "do_once": True,
    })

    # Event(**{
    # "name": "ayesha_emma_event_01",
    # "label": "ayesha_emma_event_01",
    # "conditions": [
    #     HeroTarget(
    #         IsRoom("coffeeshop"),
    #         ),
    #     PersonTarget(ayesha,
    #         IsPresent(),
    #         Not(IsHidden()),
    #         MinStat("love", 60),
    #         ),
    #     PersonTarget(emma,
    #         IsPresent(),
    #         Not(IsHidden()),
    #         MinStat("love", 60),
    #         ),
    #     ],
    # "priority": 500,
    # "music": "music/darren_curtis/come_out_and_play.ogg",
    # "do_once": True,
    # })

label ryan_bus:
    scene bg street with fade
    "I was just walking down the road, minding my own business until literally a few seconds ago."
    "Honestly, there was almost nothing in my mind apart from walking to where I'm headed."
    "Then I laid eyes on a familiar face up ahead, just standing at the crosswalk."
    show ryan casual annoyed with dissolve
    "It's Ryan..."
    "Normally I'd feel a sense of irritation and jealousy at the mere sight of the guy."
    "I've hated his guts for the longest time because of the way he cheated on Sam."
    "But that was before I found out about all of the photos that creep had stashed in the attic."
    "Now I know that Ryan's more than just a cheating louse."
    "I know that he's a seriously sick bastard too!"
    "He's standing only a couple of metres away from me right now."
    "And all of his attention is on the crosswalk lights too."
    "I'm pretty sure that he hasn't noticed me at all."
    "That's a relief, as it means that I can just walk straight past him."
    "Even better, I don't have to choose between pretending to be his friend or confronting him too!"
    "It's about then that my eyes settle on the bus coming down the street towards us."
    "Out of nowhere, the thought pops into my head."
    "All it'd take is one little push at just the right moment."
    "There's no way the driver of the bus would be able to stop in time."
    "In fact, if I did it just right, nobody would even know that I pushed him."
    "They'd just assume that he tripped and fell into the road."
    "That or he walked out into traffic without looking."
    "Just one push and that'd be the end of Ryan."
    "Sam would be rid of him and he'd never be able to hurt another girl too."
    show ryan bus
    pause 1.0
    show ryan casual annoyed
    "I look at the bus again, and the back to Ryan."
    "It's almost level with him by now."
    "In a few seconds more it'll have passed him by..."
    menu:
        "Push him":
            "Before my conscience has the time to react, I make my move."
            "Deviating through the crowd, I lurch towards where Ryan's standing."
            "All it takes is an elbow in the small of his back."
            show ryan angry at center, rotation (-10), zoomAt (1.1, (600, 880)), vshake
            ryan.say "Argh..."
            hide ryan angry with moveoutleft
            ryan.say "Wha..."
            "I don't stop moving to see if I pulled it off."
            show ryan bus bodies
            play sound "<from 0 to 3>sd/SFX/vehicles/bus_accident.ogg" fadeout 0.5
            "Instead I keep on going, listening out for what happens next."
            "It's then that I hear the sound of a loud horn and the screeching of brakes."
            play sound bus_accident
            pause 3.2
            show ryan bus bodies hit with hpunch
            with hpunch
            "But I'm not prepared for the human screech that follows."
            "And I'm definitely not ready for the sick crunching sound either!"
            hide ryan with fade
            "Even so, I don't stop or look back until I'm well away from the scene of the crime."
            "Only when I reach the next street corner do I stop and risk looking back."
            "The bus is stopped over the crosswalk and people are milling around."
            "They're crowded together, so I can't see what happened to Ryan."
            "But from the horrified looks on their faces, I know it has to be bad."
            "People are even taking photos on their phones!"
            "Which means this is going to be all over social media pretty soon."
            "I turn the corner, hurrying away with my head down."
            "Part of me was expecting to feel guilty right now."
            "But the truth is that I feel relieved instead."
            "Now nobody has to worry about Ryan anymore."
            "The bonus is that it all looks like an accident."
            "And all it took was a shove in the right direction."
            $ game.flags.ryandead = True
        "Don't push him":
            "What in the hell am I thinking?"
            "Sure, Ryan's a bigger creep than I ever thought possible."
            "But if I murder him, then what does that make me?"
            "How could I look Sam in the face knowing what I did?"
            "I stop dead in my tracks on the sidewalk."
            "And a moment later, the bus hurtles by."
            "The people standing at the crosswalk are buffeted by the breeze."
            "But none of them move an inch."
            "A second later, the lights change in their favour."
            show ryan at left with ease
            pause 0.1
            hide ryan with moveoutleft
            "I watch as Ryan walks across the street and disappears from sight."
            "He'll never know how close he came to a grizzly end today."
            "But I'm relieved that I came to my senses in time."
            "As I walk away, my legs feel a little wobbly, my head light."
            "I almost did it."
            "I almost pushed him under the bus!"
            "But I have to remember that I didn't go through with it."
            "Something stopped me before I could do it."
            "I'd like to think it was my conscience."
            "That or the fear of what it'd do to my relationship with Sam."
            "Hell, I'd even settle for it being sheer cowardice!"
            "That's better than being capable of killing a guy!"
    return

# label ayesha_emma_event_01:
#     scene bg coffeeshop with fade
#     "I always seem to be on autopilot whenever I walk into the coffee shop."
#     "I mean, I know the place like the back of my hand, and I know what I want too."
#     "Plus the baristas know me as well, and they always have my order ready for me."
#     "Most of the time I hardly have to look up from my mobile."
#     "I just grunt something vaguely friendly, swipe with it to pay."
#     "Then I reach out, grab my coffee and leave."
#     "Only today, when I reach out, it's not my coffee I grab hold of."
#     emma.say "Hey!"
#     show emma b casual angry zorder 2 at center, zoomAt(1.5, (640, 1040)) with hpunch
#     emma.say "What the hell?!?"
#     emma.say "Why are you grabbing me?!?"
#     mike.say "H...huh..."
#     mike.say "What?!?"
#     "I shake off the funk that I've been walking around in and look up."
#     "And it's only now I see that I have a hold of somebody else's hand."
#     "It's wrapped around a coffee cup that I thought was mine!"
#     "My eyes dart up the attached arm and I let go instantly."
#     show emma b surprised at startle
#     "The hand and arm belong to Emma, who looks visibly surprised."
#     mike.say "Oh, Emma..."
#     mike.say "I'm so sorry!"
#     mike.say "I thought this was my super-skinny, double espresso, flat white!"
#     show emma b annoyed
#     emma.say "Well it isn't, [hero.name]!"
#     emma.say "It's MY super-skinny, double espresso flat white!"
#     emma.say "It has my name written on it, see?"
#     emma.say "And I know it's mine because nobody else orders that!"
#     show emma b surprised
#     "As soon as she says this, Emma realises her mistake."
#     mike.say "Well...except me!"
#     mike.say "And I grabbed it for the same reason too!"
#     mike.say "Erm...this is weird and awkward, right?"
#     show emma b blush
#     "Emma's mood breaks and her cheeks flush red."
#     show emma a at startle
#     "She puts her hands over her mouth and giggles."
#     "All of which makes her look super cute!"
#     emma.say "I don't know, [hero.name]."
#     emma.say "Maybe it's more like a destiny thing?"
#     emma.say "I mean, how could two people order something so specific?"
#     mike.say "I know, I know..."
#     mike.say "You want to grab a table and drink those coffees here?"
#     mike.say "I'm not going anywhere, and I'd kind of like the company."
#     show emma normal
#     emma.say "Okay, [hero.name]."
#     emma.say "That sounds like fun!"
#     menu:
#         "Pay for her order":
#             "I want to make a good impression on Emma."
#             "So I decide to do the gentlemanly thing and pick up the tab."
#             mike.say "I'll pay for the coffees, Emma."
#             mike.say "After all, you're already paying me the compliment of your company."
#             mike.say "If that's okay with you?"
#             show emma surprised
#             "Emma looks a little surprised at the gesture."
#             "But then she nods her head and smiles."
#             emma.say "Okay, [hero.name]."
#             show emma happy
#             emma.say "You can pay this time."
#             emma.say "But don't think that means I'm a helpless little woman!"
#             emma.say "Next time we split the bill, okay?"
#             "I nod and smile, happy to have won her over."
#             show emma normal
#             "Maybe there is a way to be a gentleman and still treat a modern girl like you should!"
#             $ emma.love += 2
#         "Find an empty seat":
#             "I pick up the right coffee this time, and nod towards an empty table."
#             "Emma hesitates for a moment, like she was expecting me to do something."
#             show emma annoyed
#             "But then she nods and heads over to the table."
#             "Maybe she was expecting me to offer to pay for her coffee."
#             show emma normal
#             "And maybe that would have been the gentlemanly thing to do."
#             "But she's a modern girl, and modern girls are pretty independent."
#             "So hopefully she's going to think I'm a modern guy too."
#             "Rather than just thinking that I'm a cheapskate with no manners!"
#             $ emma.sub += 1
#     show emma b casual at center, zoomAt(1.5, (440, 1040)) with fade
#     pause 0.5
#     show emma b casual at center, zoomAt(1.5, (440, 1140)) with ease
#     "Emma and I sit down at the table, already chatting away."
#     "It's one of those times when you're talking about everything and nothing."
#     "And you'd be hard pressed to remember what you were talking about afterwards."
#     show bg coffeeshop at dark with dissolve
#     "But we're having a great time, and so I hardly notice when the lighting seems to change."
#     "The light was pretty good a moment before, but now we're in the shade."
#     "I look up, thinking that somebody must have closed a blind."
#     "Either that or a truck pulled up outside and blocked out the sun."
#     hide bg coffeeshop
#     show bg coffeeshop
#     with dissolve
#     show ayesha casual normal zorder 1 at center, zoomAt(1.5, (940, 1020)) with easeinright
#     ayesha.say "Hey, [hero.name]."
#     ayesha.say "Fancy seeing you here!"
#     mike.say "Ayesha!"
#     mike.say "I'm sorry - I didn't see you there!"
#     show ayesha annoyed
#     "Ayesha frowns a little at my explanation."
#     "Which makes sense when you consider that she's so physically imposing."
#     "But she seems to shake it off a moment later, looking at Emma."
#     show ayesha normal
#     ayesha.say "Well, aren't you going to introduce me?"
#     mike.say "Sure...sure..."
#     mike.say "Emma, this is Ayesha."
#     mike.say "Ayesha, this is Emma."
#     ayesha.say "Hey, Emma - nice to meet you!"
#     show emma surprised
#     "Emma looks up from her coffee, glancing this way and that."
#     "She has a similar look of confusion on her face to mine a moment before."
#     emma.say "Huh?!?"
#     show emma annoyed
#     emma.say "Who said that?"
#     ayesha.say "Erm...I did."
#     show ayesha annoyed
#     ayesha.say "Hello...up here?"
#     "I watch as Emma follows the sound of Ayesha's voice."
#     show emma surprised at startle
#     "And then she jumps in surprise as she realises the other girl is towering over her."
#     emma.say "Oh wow!"
#     emma.say "I didn't see you there, Ayesha!"
#     emma.say "I thought you were part of the wall!"
#     "Ayesha looks at me and then back at Emma."
#     show ayesha angry
#     "And I can tell that she's kind of thrown by the comment."
#     ayesha.say "Ah, yeah...thanks, Emma!"
#     show ayesha normal
#     ayesha.say "I get mistaken for architecture all the time..."
#     emma.say "Oh, really?"
#     show emma normal
#     emma.say "That must be awkward!"
#     emma.say "But you're SO big - like a giantess or something!"
#     emma.say "What do you do for a job?"
#     emma.say "Are you like a weight-lifter?"
#     "Ayesha looks sideways at me with a knowing smile."
#     "Clearly she's waiting for me to fill Emma in on the details."
#     menu:
#         "Ayesha is a professional wrestler":
#             "It's not like Ayesha's just a professional wrestler."
#             "But it is kind of the most interesting and unusual thing about her."
#             "And I want to make a good impression on Emma for her."
#             "So let's go with that and see what happens."
#             mike.say "Ayesha's a professional wrestler, Emma!"
#             mike.say "That's why she's such an Amazon!"
#             mike.say "She gets to kick ass in spandex."
#             mike.say "And she looks amazing in the ring!"
#             show ayesha happy at startle
#             "Ayesha laughs and waves a hand in the air at this."
#             "I can tell that she's trying to play down my praise."
#             "But I can also see that she's grinning my way too."
#             "Like she's secretly enjoying my gushing over her abilities."
#             $ ayesha.love += 2
#         "Ayesha is a personal trainer":
#             "I feel kind of embarrassed about admitting that Ayesha's a wrestler."
#             "But that's not the only thing that she does, right?"
#             mike.say "Ayesha's a personal trainer, Emma."
#             mike.say "And she does MMA as well."
#             mike.say "She can really teach you how to defend yourself!"
#             show emma surprised
#             emma.say "Oh my!"
#             show ayesha joke
#             ayesha.say "I'm a professional wrestler too."
#             show ayesha annoyed
#             ayesha.say "Which [hero.name] chose not to mention!"
#             $ ayesha.sub += 1
#     show emma happy
#     emma.say "No way, Ayesha!"
#     show ayesha happy
#     emma.say "That is SO cool!"
#     emma.say "No wonder you're such a big girl."
#     emma.say "You must be unstoppable!"
#     show ayesha normal
#     "Ayesha shakes her head, trying to look humble."
#     show emma normal
#     "And to Emma's untrained eye, that probably works."
#     "Me, on the other hand, I can see straight through her act."
#     "Ayesha's a natural performer, but she's also a sucker for praise."
#     "And Emma's giving her a massive ego-boost right now."
#     "Maybe I should do something to help the conversation along..."
#     menu:
#         "Emma, we can go to one of her shows":
#             mike.say "Seriously, Emma..."
#             mike.say "You have to see Ayesha in an actual match."
#             mike.say "She's amazing - totally dominant!"
#             "Emma nods eagerly at this."
#             emma.say "That sounds great!"
#             show emma happy
#             emma.say "When can we do it?"
#             emma.say "When's your next show, Ayesha?"
#             ayesha.say "Well..."
#             show ayesha annoyed
#             ayesha.say "We have one booked at the gym in a couple of days."
#             ayesha.say "Maybe I could fix you up with a pair of tickets?"
#             show ayesha normal
#             "Emma nods again."
#             show emma normal
#             emma.say "Can we, [hero.name]?"
#             mike.say "I don't see why not, Emma."
#             ayesha.say "Okay, guys - leave it with me."
#             show ayesha happy
#             "Ayesha gives us a last nod and a smile."
#             "Then she walks out of the coffee-shop."
#             hide ayesha with easeoutright
#             "Once we're alone again, Emma still seems giddy."
#             emma.say "Oh, this is going to be SO cool, [hero.name]!"
#             show emma happy
#             emma.say "I used to watch wrestling when I was a kid."
#             emma.say "But I never got to see it live before."
#             emma.say "And even better, now we know one of the wrestlers!"
#             "I can't help smiling, as Emma's enthusiasm is infectious."
#             mike.say "You're right, Emma."
#             mike.say "This is going to be great."
#             mike.say "I'm sure that with us cheering her on, Ayesha can't lose!"
#             $ emma.love += 4
#             $ ayesha.love += 4
#         "Emma, you should try a wrestling class once":
#             mike.say "Ayesha's a great teacher too, Emma."
#             mike.say "And you sound like you love wrestling."
#             mike.say "Why don't you try out at one of her classes?"
#             show emma surprised
#             "Emma's eyes go as wide as saucers as she hears my suggestion."
#             emma.say "Oh...oh no..."
#             emma.say "I couldn't possibly..."
#             show emma annoyed
#             emma.say "I'm WAY too small to..."
#             "Ayesha cuts the other girl off before she can finish."
#             "And I can already feel the momentum shifting in her favour."
#             ayesha.say "Don't worry about it, Emma!"
#             show ayesha happy
#             ayesha.say "Not all wrestlers are as big as me!"
#             ayesha.say "You have the build of a natural cruiserweight."
#             show ayesha normal
#             ayesha.say "You could be a great high-flyer!"
#             show emma fear
#             emma.say "But I..."
#             ayesha.say "I'll put you down in my schedule, okay?"
#             show emma annoyed
#             emma.say "Well, I don't..."
#             show ayesha happy
#             ayesha.say "No worries, your name's in there!"
#             show emma fear
#             emma.say "But what if I..."
#             ayesha.say "See you in the sparring ring!"
#             "With that, Ayesha strides off happily."
#             hide ayesha with easeoutright
#             show emma surprised
#             "But Emma looks at me with panic in her eyes."
#             emma.say "Wh...what just happened to me?"
#             mike.say "I think you got signed up for wrestling classes, Emma!"
#             show emma fear
#             emma.say "B...but...I don't want to be a wrestler!"
#             mike.say "Hmm..."
#             mike.say "I don't get the feeling you have much choice in the matter!"
#             $ emma.sub += 4
#     return
# return
