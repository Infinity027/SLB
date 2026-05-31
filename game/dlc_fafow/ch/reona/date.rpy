label reona_date_eat_a_burger:
    reona.say "Mmm...I'm starving!"
    reona.say "This is just what I need to fill me up!"
    "I look on in sheer amazement as Reona tears into her burger."
    "She bites, chews and swallows like a ravenous beast."
    "And the burger doesn't last more than the blink of an eye!"
    return

label reona_date_buy_drink:
    reona.say "I'm gagging for a drink!"
    reona.say "How about you?"
    reona.say "Should I grab you one too?"
    if reona.is_visibly_pregnant:
        mike.say "Erm, I don't think that's a good idea, Reona!"
        mike.say "Not in your condition, you know?"
        "Reona looks down at her belly, like she forgot all about it."
        $ reona.love += 5
        reona.say "Oh yeah - dammit!"
        reona.say "Better make mine a soda!"
    else:
        mike.say "That sounds great, Reona."
        mike.say "I'll have whatever you're having."
        mike.say "Then it's my turn to get a round in."
        reona.say "You got it, [hero.name]!"
        reona.say "I'll be right back with the drinks..."
    return

label reona_date_play_darts:
    mike.say "You want to play a game of darts, Reona?"
    mike.say "Because the board's free right now."
    reona.say "I guess so."
    reona.say "But go easy on me, yeah?"
    "Reona does her best to give me a good game."
    "But in the end I beat her quite easily."
    "I don't get the feeling darts is her game!"
    return

label reona_date_pub_play_pool:
    mike.say "Grab a cue, Reona - we're playing pool!"
    reona.say "Oh great - I love pool!"
    "Not only does Reona love pool, she's damn good at it too!"
    "In fact, it doesn't take her long to totally trounce me."
    mike.say "Erm...well played, Reona - let's try something else next time..."
    return

label reona_date_buy_a_round:
    reona.say "I'm gagging for a drink!"
    reona.say "How about you?"
    reona.say "Should I grab you one too?"
    if reona.is_visibly_pregnant:
        mike.say "Erm, I don't think that's a good idea, Reona!"
        mike.say "Not in your condition, you know?"
        "Reona looks down at her belly, like she forgot all about it."
        $ reona.love += 5
        reona.say "Oh yeah - dammit!"
        reona.say "Better make mine a soda!"
        $ hero.cancel_activity()
    else:
        mike.say "That sounds great, Reona."
        mike.say "I'll have whatever you're having."
        mike.say "Then it's my turn to get a round in."
        reona.say "You got it, [hero.name]!"
        reona.say "I'll be right back with the drinks..."
        $ game.active_date.score += 5
        if "rebel" in reona.traits:
            $ game.active_date.score += 5
        $ reona.set_flag("drinks", 1, "day", mod="+")
    return

label reona_dance_with:
    reona.say "Come on, [hero.name], let's dance!"
    "Before I can say a word, I find myself dragged up to dance."
    "Well, if you can call what Reona does dancing."
    "It seems to be more like rubbing herself against me to the music!"
    "Not that I'm complaining, you understand?"
    return

label reona_date_play_arcade_intro:
    mike.say "I have some spare change, Reona."
    mike.say "Want to play one of those old-school arcade games with me?"
    "Reona looks at the machines and then back at me."
    reona.say "Sure thing, [hero.name]."
    reona.say "So long as you show me how to play?"
    "I nod as we walk over to them."
    mike.say "No worries, Reona."
    mike.say "It's not as hard as it looks, I promise."
    "I fumble around in my pockets for the coins I need to play."
    "Then I feed them into the slot and we get started."
    return

label reona_date_play_arcade_win:
    reona.say "Hey!"
    reona.say "I wasn't ready!"
    mike.say "You need to be on the ball, Reona!"
    mike.say "Keep your eyes open!"
    "No matter what advice I give to Reona, it doesn't seem to help."
    "She flounders all the time we're playing, falling further behind me."
    "And once it's over, she looks less than pleased."
    reona.say "That was too hard!"
    reona.say "You should have gone easy on me!"
    mike.say "Sorry, Reona - I guess my competitive side just took over."
    return

label reona_date_play_arcade_lose:
    mike.say "What the..."
    mike.say "How are you even doing that?"
    reona.say "Ha, Ha!"
    reona.say "This is so easy, [hero.name]!"
    "Reona doesn't seem to need any of my advice."
    "She takes to the game like a fish to water."
    "This flusters me and I start to make mistakes as well."
    "Once it's over, Reona's roundly trounced me."
    reona.say "That was great - let's play again!"
    mike.say "Ah...no change - sorry!"
    return

label reona_dick_reactions:
    if not reona.flags.seendick:
        $ reona.flags.seendick = 1
        "I notice that Reona's gone quiet as she stares at my dick."
        "Which of course makes me instantly paranoid that there's something wrong."
        mike.say "Ah, Reona..."
        mike.say "Are you okay?"
        mike.say "Is there a problem?"
        if hero.has_skill("hung"):
            show dick reactions reona mock
            "Reona shakes her head and then lets out a long sigh."
            reona.say "I'm fine, [hero.name], just fine."
            reona.say "Or at least I will be when I figure out what to do with all that!"
            "I can feel myself starting to blush at Reona's reaction."
            mike.say "Yeah, I know..."
            mike.say "It is kind of big..."
            mike.say "Is that going to be a problem?"
            show dick reactions reona smile
            "Reona seems to snap out of it as I ask the question."
            "She shakes her head and begins to smile."
            reona.say "Oh no..."
            reona.say "No way!"
            show dick reactions reona tasty
            reona.say "I just kinda feel like I won the lottery, that's all!"
            $ reona.sub += 10
        elif hero.has_skill("smalldick"):
            show dick reactions reona mock
            "Suddenly, Reona bursts out laughing."
            reona.say "Ha, ha, ha!"
            reona.say "Is that all of it?"
            reona.say "Man, you got a raw deal!"
            "I can feel myself starting to blush at Reona's reaction."
            mike.say "I...I can't help it, Reona!"
            mike.say "It's been cold all day, you know?"
            mike.say "And I'm pretty nervous right now!"
            show dick reactions reona smile
            reona.say "Ah, don't worry about it, [hero.name]."
            reona.say "You're not the first guy with a tiny cock I dated!"
            show dick reactions reona tasty
            reona.say "It just means I'm gonna have get creative, that's all..."
            $ reona.sub -= 10
        hide dick reactions
    return

label reona_date_amusement_park_male:
    scene bg amusement
    show reona sadfrustrated
    with fade
    "I honestly thought that I was onto a winning idea when I invited Reona along to the Amusement Park."
    "She's one of the most fun-loving and adventurous girls I've ever met, so it seemed like a no-brainer."
    "Of course she'd want to spend the day somewhere the whole point of which is to just have fun, right?"
    "Well it seems that I was wrong."
    "Because she's dragging her feet as we walk towards the gates of the park."
    "And from the look on her face, she's not looking forward to it at all."
    "So far I've been doing the best I can to ignore that fact."
    "But eventually I feel like I have to stop and say something about it."
    mike.say "Reona..."
    mike.say "Just what is the problem?"
    "Reona stops in her tracks and looks me straight in the eye."
    "And as soon as she does so, I start to wonder if I'm doing the right thing."
    show reona shout
    reona.say "What's that supposed to mean?"
    reona.say "You were the one that wanted me to come here, [hero.name]."
    reona.say "And here I am!"
    show reona sadfrustrated
    "I can't help becoming just as confrontational as Reona's being."
    "Planting my hands on my hips as I do the best I can to respond."
    mike.say "It's not like I forced you to come along, Reona!"
    mike.say "You make it sound like you don't want to be here at all."
    mike.say "If that's so, why did you come?"
    show reona angry
    reona.say "Because I wanted to be nice to you, dummy!"
    reona.say "Why else would I come to a lame kids fairground?!?"
    show reona sadangry
    "I can't help the look of horror that spreads across my face."
    "And the words are spilling out of my mouth before I know what's happening."
    mike.say "This is not some crappy travelling carnival!"
    mike.say "I'll have you know that this is a cutting-edge theme park!"
    mike.say "There are no dodgy guys with mullets and buck-teeth running the rides here."
    mike.say "And I'm going to prove it to you!"
    show reona interested
    "As I bang on about how great the place is, I notice a change in Reona."
    show reona happy
    "Where before she was angry and defiant, now she's starting to smile."
    "Then she begins to chuckle and shake her head."
    show reona shout
    reona.say "Fuck sake..."
    reona.say "Only you could get so passionate about a place like this!"
    reona.say "Come on, you great big kid - let's see if you're right."
    return

label reona_date_ferris_wheel_male:
    mike.say "Okay, Reona..."
    mike.say "We're going to ride the Ferris Wheel."
    "Reona glances up at the Ferris Wheel, towering over us."
    "And I can see that she doesn't seem impressed."
    reona.say "Geez..."
    reona.say "How old is that thing?"
    reona.say "And is it even safe?"
    "I do the best I can to ignore the questions."
    "And instead I make my way through the crowds to join the queue."
    reona.say "Did you hear what I just said?"
    reona.say "Is this thing even safe?!?"
    mike.say "Of course it's safe!"
    mike.say "They inspect all of this stuff on a regular basis."
    "Reona and I continue to squabble as we move up the queue."
    "And we're still going at it as we climb onto the ride."
    "In fact Reona only stops the moment she first looks around her."
    "By that time we're well and truly up in the air."
    "And the view seems to catch her totally off-guard."
    reona.say "I still don't think this thing is..."
    reona.say "Whoa..."
    reona.say "That's...that's quite a view!"
    "I can't help smirking at Reona's amazement."
    "So much for her dismissing all of this as being for kids."
    mike.say "Pretty impressive, huh?"
    reona.say "Yeah..."
    reona.say "I dunno why, but it is."
    reona.say "I've been up loads of tall buildings before."
    reona.say "But this feels different somehow!"
    mike.say "I guess that's because the ride's made to take you up slowly, Reona."
    mike.say "That way you get to really appreciate the altitude."
    "Reona just nods at this, as he keeps on looking out at the view."
    "And she doesn't really start talking again until we come back down to earth."
    "Which I guess means the Ferris Wheel was an unexpected hit."
    $ reona.love += 2
    $ game.active_date.score += 20
    return

label reona_date_merry_go_round_male:
    mike.say "I think we should ride the Merry-Go-Round next."
    "Reona snorts at my suggestion, and shakes her head."
    "Looking at me like I've taken leave of my senses."
    reona.say "Ha!"
    reona.say "Why would you want to do that?"
    reona.say "All it does is go round in a circle!"
    "I can feel myself flushing a little at Reona's reaction."
    "But I still do the best I can to explain myself."
    mike.say "It's one of the oldest rides in the park, Reona."
    mike.say "Riding it is kind of like a rite of passage."
    mike.say "You have to do it at least once."
    reona.say "Says who?"
    mike.say "I don't know..."
    mike.say "People who like theme parks?"
    reona.say "You mean losers?"
    mike.say "Whatever, Reona - let's just ride the damn thing, okay?"
    "Reona reluctantly lets me lead her over to the back of the line."
    "Then we wait patiently as we make our way up the queue."
    "Or maybe impatiently would be a better way to describe it."
    "As soon as our turn comes round, Reona stomps onto the ride."
    "Then she plants her ass on the first spot that she finds."
    "I settle down next to her, being careful to keep my mouth shut."
    "And once the ride starts moving, I keep stealing glances in her direction."
    "Of course I'm hoping that the magic of the ride will have an effect on Reona."
    "That she'll start enjoying herself and admit that I was right all along."
    "But what actually happens is that she keeps on glaring straight ahead."
    "And she doesn't stop even when the ride is over and we're getting off."
    reona.say "Worst ride ever."
    reona.say "Boring as hell too!"
    mike.say "Erm..."
    mike.say "So you didn't like it?"
    reona.say "Does it sound like I did?!?"
    reona.say "Your taste in rides sucks!"
    $ reona.love -= 2
    $ game.active_date.score -= 20
    return

label reona_date_haunted_house_male:
    mike.say "I want to do the Haunted House next, Reona..."
    mike.say "It's one of my favourites."
    "Reona takes a long look at the sign for the Haunted House."
    "And then she shrugs as we start walking towards it."
    reona.say "Could be fun, I guess."
    reona.say "Not really my kind of thing though."
    "I shake my head as we join the queue for the Haunted House."
    "Keen to sell the idea of it to Reona as best I can."
    mike.say "How can you say that?!?"
    mike.say "The Haunted House is the best thing at the park."
    mike.say "It combines all the best aspects of horror movies and Halloween!"
    reona.say "Yeah, well..."
    reona.say "I was never really that big on them either."
    mike.say "Just you wait, Reona..."
    mike.say "You'll see what I mean."
    "Once we make it to the front of the queue, I take hold of Reona's hand."
    "Then we step inside the Haunted House, and the experience begins."
    "I do the best I can to show Reona how much fun the place is."
    "And sure, she jumps in all the right places."
    "Plus the screams she lets out sound genuine."
    "But as we're walking out of the place, she still doesn't seem sold."
    mike.say "So what do you think?"
    mike.say "How great was that?"
    reona.say "Hmm..."
    reona.say "I like that you like it."
    mike.say "Huh?"
    mike.say "What's that supposed to mean?!?"
    reona.say "You're a smart guy, [hero.name]…"
    reona.say "Figure it out for yourself."
    $ reona.love += 2
    $ game.active_date.score +20
    return

label reona_date_love_boat_male:
    mike.say "You want to ride the Love Boat, right?"
    mike.say "I mean, if there's one ride that's made for you..."
    mike.say "It has to be that one!"
    "Reona cocks her head on one side as I say this."
    "And she fixes me with a questioning stare."
    reona.say "What's that supposed to mean?"
    mike.say "Well..."
    mike.say "You know..."
    mike.say "It's dark, and private, yeah?"
    mike.say "And nobody can see what you're getting up to!"
    reona.say "Oh, I see..."
    reona.say "You think I should like it because I'm easy?"
    reona.say "Is that it?"
    "I'm already shaking my head as I try to explain myself."
    "And Reona's pressing me the whole time."
    "But what neither of us seems to have noticed is where we're going."
    "By some strange coincidence, we end up walking straight into the queue."
    "And as it's a quiet ride, we're soon at the front and next up for the ride."
    "We hardly seem to notice that we're stepping into the boat as we argue."
    "And the squabbling only stops once it moves off into the gloom of the tunnel."
    reona.say "Oh great..."
    reona.say "Now we're on the damn thing!"
    mike.say "Erm..."
    mike.say "This is supposed to be romantic!"
    reona.say "Well I don't feel very romantic right now."
    mike.say "So what?"
    mike.say "I should just keep to my side of the boat?"
    reona.say "I think you should."
    mike.say "Okay..."
    mike.say "I will."
    reona.say "You just do that."
    "What follows is probably the frostiest ever ride on the Love Boat."
    "And by the time we get off at the other end, we're both bored rigid."
    $ reona.love -= 2
    $ game.active_date.score -= 20
    return

label reona_date_hedge_maze_male:
    mike.say "You wanna do the Hedge Maze, Reona?"
    mike.say "The queue looks pretty short."
    reona.say "Yeah, of course it does."
    reona.say "Because that ride sucks!"
    reona.say "It's just a dumb maze."
    "I look over to the entrance of the Hedge Maze."
    "And then I turn my attention to Reona again."
    mike.say "So what?"
    mike.say "Is that a yes or a no?"
    reona.say "It's a meh..."
    reona.say "At the most it's a whatever!"
    "I shrug and begin to walk over to where the line begins."
    "And Reona soon follows on my heels."
    "It seems like neither of us is particularly keen on the idea of the maze."
    "But at the same time, neither of us can be bothered to object to it."
    "Never mind summon the will to think up an alternative."
    "The short length of the queue means that we're soon walking into the maze."
    "And from there we go through the motions of wandering around inside."
    "But no matter how many turns we make, nothing seems to click."
    "So when we eventually find the exit, we're just as bored as we were before."
    "And neither of us makes as much as a single comment as we leave it behind."
    "Instead we just wander off, vaguely looking for the next ride that takes our fancy."
    $ reona.love -= 1
    $ game.active_date.score -= 10
    return

label reona_date_amusement_ice_cream_male:
    reona.say "Urgh..."
    reona.say "I'm all hot and sweaty!"
    reona.say "Everything I'm wearing is soaking wet too!"
    "I've been staring at Reona for quite some time now."
    "Amazed that she can be so hot while wearing so little."
    "My eyes almost bulging at the sight of all that glistening flesh."
    mike.say "Oh..."
    mike.say "Oh yeah, Reona..."
    mike.say "It's like...like the worst thing ever!"
    reona.say "So?"
    reona.say "What are you gonna do about it?!?"
    "Suddenly I feel like a traps been sprung on me."
    "And I'm hurrying to think up a solution to the problem."
    mike.say "I..."
    mike.say "Erm..."
    mike.say "I'm going to..."
    mike.say "Buy you an ice-cream?"
    "Suddenly there's a huge smile on Reona's face."
    "And she proceeds to clap her hands together in glee."
    reona.say "Yay!"
    reona.say "That's the right answer."
    "Reona happily lets me take her hand."
    "And then I waste no time in leading her to the nearest ice-cream stand."
    "Where we wait in line as Reona continues to pout and fan herself."
    "But almost as soon as she has her ice-cream, she perks up again."
    "Which means that I can return my attention to watching her."
    "And this time I get to enjoy the sights and sounds of her eating ice-cream."
    "Maybe even with added sighs and moans too!"
    $ reona.love += 2
    $ game.active_date.score += 20
    return

label reona_halloween_invitation:
    "Almost as soon as we've all agreed to host the party, I start thinking about who I want to invite."
    "And it doesn't take me long to settle on Reona as the one girl I'd like to have there as my date."
    "Halloween's fun and so is Reona, so it's the perfect combination, right?"
    "Plus it'll be a really great chance to get to know Reona better."
    "Not to mention show her off to everyone I know too!"
    show reona happy at center, zoomAt(1.25, (640, 880)) with dissolve
    "So by the time I get to meet up with Reona next, I'm totally set on inviting her along."
    mike.say "So..."
    mike.say "I notice that we're into October already."
    mike.say "Fall is creeping in all around us, right?"
    mike.say "Leaves are turning red, yellow and orange then falling to the ground."
    mike.say "The scarves and hats are coming out, pumpkin latte's appearing in coffee shops..."
    "Reona's been listening to me happily while I said most of this."
    "Nodding along and smiling as I invoke the spirit of the season."
    "But by the time I get to the lattes, it seems to be wearing a little thin."
    show reona shout
    reona.say "Okay, [hero.name], okay..."
    reona.say "It's Autumn - I get the message!"
    reona.say "Are you going anywhere with this?"
    reona.say "Or did you just get high on the season?"
    show reona happy
    "With a nervous smile on my face, I begin nodding."
    mike.say "Oh yeah, Reona..."
    mike.say "I was kinda building up to asking you something."
    mike.say "You see we're having a party, my housemates and me..."
    mike.say "On Halloween - it's a Halloween party!"
    show reona interested
    "Reona looks at me with one eyebrow raised."
    show reona shout
    reona.say "Yeah..."
    reona.say "The one kind of suggested the other!"
    reona.say "So are you just bragging about the fact you've already made plans?"
    reona.say "Or does this talk of a party have something to do with me?"
    show reona normal
    "Still nodding, I leap on the change Reona's question just gave me."
    mike.say "That's exactly it, Reona..."
    mike.say "I wanted to invite you along to the party."
    mike.say "You know...as my date for the night?"
    if reona.love >= 100 or reona.sub >= 40:
        show reona pensive
        "Reona looks like she's thinking about it."
        "And all the while she's silent, I have hope."
        "But then she nods her head and confirms them."
        show reona shout
        reona.say "You know what..."
        show reona talkative
        reona.say "That sounds like it could be fun."
        reona.say "In a kind of ironic, cheesy way, yeah?"
        show reona normal
        "Part of me is bristling at the fact Reona just called my party cheesy."
        "But a much larger part of me is bursting at the seams with excitement."
        "Because she just agreed to come along, and that's all that matters."
        mike.say "You'll come then?"
        mike.say "That's great news!"
        mike.say "It's going to be a pretty fun party."
        mike.say "Everyone's dressing up in costumes - sexy ones too!"
        mike.say "We're going to have music and food..."
        mike.say "Oh, and booze - plenty of booze!"
        show reona happy
        "Reona seems to be warming to the idea as I describe it to her."
        "She's nodding and looking thoughtful."
        "Like ideas are already springing into her head."
        show reona shout
        reona.say "Oh, don't worry about the costume."
        show reona talkative
        reona.say "There's one I've been wanting to do for ages."
        reona.say "Just wait until you see me in it, [hero.name]..."
        reona.say "I guarantee it'll blow your mind!"
        show reona devious
        "Reona adds a knowing wink as she says this."
        "And I can almost feel my heartbeat quicken as she does so."
        mike.say "That sounds perfect, Reona!"
        mike.say "And you know..."
        mike.say "If you want an eye running over your costume before the big night..."
        mike.say "I'd be more than happy to help?"
        show reona happy
        "Reona chuckles and shakes her head."
        show reona talkative
        reona.say "Oh no..."
        reona.say "I think we'll keep it a surprise."
        reona.say "Trust me, you'll like it better that way!"
        $ game.flags.halloween_girl = "reona"
    else:
        show reona pensive
        "Reona looks like she's thinking about it."
        "And all the while she's silent, I have hope."
        "But then she shakes her head and dashes it."
        show reona annoyed
        reona.say "Nah..."
        reona.say "I think I'll pass."
        show reona sad
        "I kind of feel like I just had my guts casually ripped out."
        "But I manage to keep a smile on my face and push on through it."
        mike.say "Are you sure about that, Reona?"
        mike.say "It's going to be a pretty fun party."
        mike.say "Everyone's dressing up in costumes - sexy ones too!"
        mike.say "We're going to have music and food..."
        mike.say "Oh, and booze - plenty of booze!"
        show reona happy
        "Reona does me the favour of smiling and nodding."
        "In fact she keeps it up all the time I'm talking."
        "But once I've stopped, the nods turn into a shake of the head."
        show reona talkative
        reona.say "That sounds great, [hero.name]..."
        show reona shout
        reona.say "But it's not my kind of thing."
        reona.say "At least not on Halloween, you know?"
        show reona happy
        "I blink in confusion at this."
        "Because I really don't know."
        "I'd have thought it was totally Reona's kind of thing."
        "But the look on her face tells me that she's made up her mind."
        "And nothing I say is going to change that."
        mike.say "Okay, Reona..."
        mike.say "But the invitation still stands."
        mike.say "Like...if you change your mind?"
        show reona shout
        reona.say "Aww..."
        reona.say "Thanks, [hero.name]..."
        reona.say "I won't - but thanks all the same!"
    return

label reona_halloween_arrival:
    scene bg house with fade
    "I turn around to answer the front door, my head spinning with all the stuff I'm currently dealing with."
    "Which means that I'm not really paying attention to the task at hand when I actually open it."
    show reona halloween at center, zoomAt(3.0, (720, 1440)) with hpunch
    "So it comes as a serious surprise to find a pair of breasts practically thrust into my face!"
    "And don't get me wrong, that's not something I'd object to under almost an circumstances."
    "The reason I take a leap back and cry out in alarm is more on account of the surprise."
    mike.say "Whoa..."
    mike.say "Watch where you're swinging those things..."
    mike.say "There's breakable stuff in here!"
    show reona halloween surprised at center, traveling(1.5, 0.3, (640, 1040))
    "It's only now that I've taken a step back I can actually see who the breasts belong to."
    "And the perspective is helped by the fact their owner has taken one step backwards too."
    show reona annoyed
    reona.say "Well, I have to say..."
    show reona talkative
    reona.say "Nobody ever said that to me before!"
    reona.say "What's the matter, [hero.name]?"
    reona.say "Don't you like my costume?"
    show reona flirt at center, traveling(1.0, 3.0, (640, 740))
    "Without the need to be asked, Reona does a little twirl on the spot."
    "Which allows me to take in the full extent of her outfit for the party."
    "Or perhaps to be more accurate, the limits of it - because she's practically naked!"
    "I'm being serious right now."
    "Reona's wearing a black top with sleeves and a white collar."
    "But it barely covers her breasts, which are thrust straight out in front of her."
    "Apart from that she's only wearing a pair of black panties, a rubber tail and a pair of bat-wings."
    show reona talkative at center, traveling(1.5, 0.3, (640, 1040))
    reona.say "So..."
    reona.say "What do you think?"
    reona.say "Pretty hot, huh?"
    show reona happy
    "I'm mostly struck dumb by the sight of how much flesh is on show in front of me right now."
    "But there's something vaguely familiar about Reona's outfit too."
    "A faint recollection is trying to push itself to the front of my mind."
    "Struggling to get past the almost insurmountable barrier of my growing lust."
    show reona embarrassed blush
    mike.say "Liz..."
    mike.say "You're Liz, the succubus, right?"
    mike.say "From the manga, yeah?"
    show reona interested
    "Reona rewards me for this by clapping her hands together and hopping on the spot."
    "The effects of which only serve to make me all the more horny as I watch them."
    "And the sight of Reona's butt on the way around is almost as devastating as that of her breasts!"
    show reona shout
    reona.say "So?"
    show reona normal
    mike.say "Erm..."
    mike.say "So what, Reona?"
    show reona shout
    reona.say "What do you think?"
    reona.say "You love it, right?"
    show reona normal
    menu:
        "Thanks to the seven hells for this gorgeous demon on my front door!":
            "Part of me is worried about Reona walking around in that outfit."
            "Because she's going to wow every guy that we've invited tonight."
            "Hell, she's going to have the same effect on most of the girls too!"
            "But I have to get a hold of myself and start acting like a grown man, not a jealous kid."
            mike.say "Reona, I adore it!"
            $ reona.love += 1
            mike.say "You look amazing."
            show reona pensive
            "Reona raises an eyebrow at this."
            "Almost like she's not satisfied with my answer."
            show reona annoyed
            reona.say "Amazing?"
            reona.say "Is that really the best you can do?"
            show reona happy
            "It's just about then that I see the curl of her lip."
            "And I know that she's grinning at me in a suggestive manner."
            mike.say "Did I say 'amazing'?"
            $ reona.love += 1
            show reona talkative
            mike.say "I obviously meant super sexy!"
            hide reona
            show reona kiss halloween
            with fade
            $ reona.flags.kiss += 1
            "This has the desired effect of putting a smile on Reona's face."
            "And she all but throws herself at me a moment later."
            "Throwing her arms around my neck, she leans forwards."
            "This means all of her weight in on me, and I have to support her or else collapse to the ground."
            "But it also means that I have to hold Reona against me as I do so, revealing her true intentions."
            "She smiles as she plants a kiss on my unprepared lips, then chuckles."
            hide reona
            show reona halloween talkative at center, zoomAt(1.5, (640, 1040))
            with fade
            reona.say "Ha..."
            reona.say "I knew if anyone would appreciate this costume it'd be you, [hero.name]!"
            show reona shout
            reona.say "Now are you going to invite me inside or what?"
            show reona whining
            reona.say "I'm freezing my tail off out here!"
            show reona normal
            "Reona grabs the tail attached to her costume and swings it for effect."
            "That makes me realise just how cold she must be."
            "Reona's outfit is crazily revealing and it's October."
            "I need to get her inside before she catches her death of cold!"
            mike.say "Where are my manners!"
            show reona happy
            mike.say "In you come."
            "I step to one side, ushering Reona into the hallway."
            "And she takes my up on the invitation, hopping inside so I can close the door behind her."
        "Hmmm... You must be cold.":
            "Well, I certainly would love it - if I were the only guy here!"
            "Hell, looking that good, Reona's going to impress the girls too."
            "But maybe there's a way I can subtly make her think she's showing off too much flesh?"
            "Perhaps even get her to actually cover up a little?"
            mike.say "Oh the outfit's great, Reona..."
            mike.say "Really sexy!"
            show reona embarrassed
            mike.say "But..."
            "Reona's all smiles as she listens to me praise her costume."
            "Then she hears the but, and her smile disappears."
            show reona annoyed
            reona.say "What do you mean 'but'?"
            show reona angry
            reona.say "How can there be a 'but' when I look this good?!?"
            show reona sad
            mike.say "I'm just worried about your health, Reona."
            mike.say "It's October, the beginning of Fall."
            mike.say "You could catch your death of cold walking around like that!"
            $ reona.love -= 4
            show reona guilty
            "Reona rolls her eyes and then reaches out to shove me aside."
            "She strides into the hallway with a look of annoyance on her face."
            reona.say "Nice try, [hero.name]."
            show reona annoyed
            reona.say "Next time try letting me into the warm house..."
            show reona angry
            reona.say "You know, before you lecture me about the dangers of the cold?!?"
            hide reona with easeoutright
            "All I can do is make a silent admission of defeat to myself."
            "That and close the door as I hurry after Reona."
            "Already trying to think up ways to make it up to her."
    scene bg black with dissolve
    pause 1
    return

label reona_halloween_party:
    $ game.pass_time(2)
    scene bg livingroom
    with fade
    "I'm waiting for Reona to come back from a quick trip to the bathroom."
    "Just standing around and trying to keep my head occupied until she's back."
    "I figure that, with an outfit like the one she's wearing, it shouldn't take long."
    "But she's already gone past the amount of time that I estimated, and by quite a way."
    "So I start scanning around the room, looking for any sign of her."
    "It should be easy, as this is the house where I've been living for a year or two."
    "But I soon find that the addition of the Halloween décor gets in the way."
    "So I'm looking this way and that, straining to see Reona until she's almost on top of me!"
    show reona halloween annoyed zorder 2 at center, zoomAt(2.0, (640, 1240))
    reona.say "[hero.name]…"
    reona.say "Will you please help me?"
    show reona halloween pensive at center, traveling(1.5, 0.3, (640, 1040))
    "The moment I hear those words coming from Reona's mouth, I snap to attention."
    "Because I can tell from her tone that she's far from pleased about something."
    mike.say "Huh?"
    mike.say "Reona..."
    mike.say "What's the matter?"
    show reona halloween annoyed at center, traveling(2.0, 0.3, (640, 1240))
    "But as Reona comes closer to me, I can soon see for myself."
    show scottie halloween zorder 1 at center, zoomAt(1.25, (1140, 940)) with easeinright
    "Because Scottie also comes into view a moment later."
    "And I can tell from here that he's too close to her for comfort."
    show reona guilty
    reona.say "That, [hero.name]…"
    reona.say "That's what's the matter!"
    show reona normal
    show scottie surprised
    "Scottie notices that we're both looking straight at him."
    show scottie happy
    "And his shoulders sag while he throws his hands in the air."
    show scottie at center, traveling(1.5, 0.3, (940, 1080))
    scottie.say "Aww..."
    scottie.say "I was only having a little fun!"
    scottie.say "Why'd you have to go and dob me in to Captain Dork?!?"
    show scottie normal
    show reona at center, traveling(1.5, 0.3, (340, 1040))
    "I step up to make sure I put myself between Scottie and Reona."
    "Then I hold up a hand to let Scottie know that he needs to stay back."
    mike.say "Okay..."
    mike.say "What's going on here?"
    show reona shout
    reona.say "I was in the bathroom just now..."
    show reona angry
    reona.say "And this asshole was trying to get in there with me!"
    show reona sadfrustrated
    "I shoot Scottie a shocked glance after Reona's made her accusation."
    "But just as quickly, he shakes his head and waves his hands in the air."
    show scottie angry
    scottie.say "No way!"
    scottie.say "That's not what happened at all, and you know it."
    scottie.say "I didn't know the door was locked when I tried it."
    scottie.say "And I couldn't hear what you were saying through the door."
    scottie.say "I thought you were stuck in there or something!"
    show scottie sad
    "I can see that neither of them is going to accept the other's version of events."
    "And soon enough they're both looking at me, like I should be doing something about it."
    "Clearly they think that I'm the one supposed to settle their dispute!"
    menu:
        "Defend Reona":
            "Sure, it's believable that Scottie could actually be stupid enough to do that."
            "But the fact that Reona's the one accusing him of it means I was never going to side with him."
            "And I make a point of crossing my arms as I put myself between the two of them."
            "At first this seems to amuse Scottie, as I guess he's used to pushing people around."
            "Yet when I stand firm and look him in the eye, that seems to effect a change in him."
            "Somehow me standing up to him rattles his confidence, leaving him visibly unsure of himself."
            mike.say "I don't care how badly you need to go Scottie."
            mike.say "Banging on the door of the bathroom isn't acceptable."
            show scottie angry
            scottie.say "But what would you have me do, huh?"
            scottie.say "I don't want to piss myself..."
            scottie.say "Or go to the bathroom in a corner somewhere!"
            "I listen to Scottie's excuses with an impassive look on my face."
            "And when he's finished, I shake my head."
            mike.say "You should have come and asked Sasha, [bree.name] or me for help."
            mike.say "There's more than one bathroom in the house!"
            show scottie embarrassed
            "By now Scottie's looking down at his feet."
            "And it almost feels like I'm delivering a lecture."
            hide scottie with easeoutright
            "He nods and then shuffles off, moving out of sight."
            "I don't know if he's going somewhere in particular."
            "Or if he's just skulking off to lick his wounds."
            "And the truth is that I don't really care to find out."
            "Even less so when I feel Reona wrap herself around my arm."
            $ reona.love += 4
            show reona talkative
            reona.say "Thanks for that, [hero.name]…"
            reona.say "You really told him!"
            show reona happy
            "I smile and start thinking about what else I want to do with her tonight."
            "Because I get the feeling I just earned myself some serious points with Reona."
            "And I'd love to cash them in before the end of the party."
        "Defend Scottie":
            "Part of me thinks that Scottie could well have followed Reona to the bathroom on purpose."
            "He's a big, dumb pile of muscles, stupid enough to miss all of the negative signals."
            "Though normally none of that would be sufficient for me to take his side in such matters."
            "But then my eyes settle on Reona's costume, and I start to see how this probably played out."
            mike.say "Maybe he saw your tail and was hypnotised, Reona?"
            show reona sadshock
            show scottie normal
            "Reona blinks in surprise, clearly shocked by my statement."
            show reona whining
            reona.say "Huh?"
            reona.say "What's that supposed to mean?!?"
            show reona sadshock
            "I shrug."
            mike.say "Just that you're not exactly hiding your assets, are you?"
            mike.say "Maybe Scottie here just misread the signals you're giving out."
            show reona shock
            mike.say "Maybe it was all a misunderstanding?"
            "While Reona looks shocked, in contrast, Scottie seems delighted."
            "He nods and gives me a hearty slap on the back."
            "Which sends me staggering forward a few steps."
            show scottie happy
            scottie.say "Wow..."
            scottie.say "I used to think you were a total nerd, [hero.name]…"
            scottie.say "But maybe you are a good guy after all!"
            hide scottie with easeoutright
            "Scottie walks off with a huge smile on his face."
            "But once he's gone, I see that Reona is glaring at me."
            $ reona.love -= 10
            show reona angry
            reona.say "What the hell was that about?"
            reona.say "Why did you take his side over mine?"
            show reona sad
            mike.say "I didn't, Reona..."
            mike.say "I just tried to look at it from both sides, that's all."
            "Reona shakes her head and then turns her back on me."
            "And I feel the weight of my choice beginning to press down on my shoulders."
    scene bg black with dissolve
    pause 1
    return

label reona_halloween_dance:
    $ game.pass_time(2)
    scene bg livingroom
    show reona halloween shy
    with fade
    reona.say "[hero.name]…"
    reona.say "Come with me right now!"
    show reona sad
    "Reona practically pounces on me as she says all of this."
    "Leaping out of nowhere to grab me firmly by both wrists."
    "Then, without another word of explanation, she drags me in the direction she just came from."
    "I'm kind of shocked by how strong she actually is, almost jerking me off my feet."
    "Well, at least that's my explanation for how she manages to get me so far before I resist."
    mike.say "Reona..."
    mike.say "Reona, wait..."
    show reona surprised
    mike.say "Will you...will you just wait a damn second?!?"
    "The way I'm digging in my hells doesn't seem to be enough to stop Reona."
    "It's only when she hears me yelling that she actually pauses and turns her head."
    reona.say "Huh?"
    show reona embarrassed
    reona.say "What's the matter, [hero.name]?"
    reona.say "Why are you fighting it?"
    "I blink at the question, still in the dark."
    mike.say "Fighting what, Reona?"
    mike.say "You haven't even told me what we're supposed to be doing!"
    show reona interested rightopen leftnormal
    "Reona shakes her head, a look of amazement on her face."
    "Then she gestures to her ears."
    show reona shout
    reona.say "Are you deaf or something?"
    show reona talkative
    reona.say "The music just got good..."
    reona.say "So we need to dance!"
    show reona normal leftback rightnormal
    "I take a moment to actually listen to the music that's playing."
    "But to my disappointment, it doesn't sound like one of the tracks I picked."
    "Plus I don't recognise it either, so it's a total unknown to me!"
    "I'm about to say no, when I remember something else important."
    "Looking down, I see Reona's body right in front of me."
    "And it's already started to move in time to the music!"
    menu:
        "Oh that...Yeah I'm sorry, let's dance.":
            "I blink as I watch Reona's fantastic form move before my eyes."
            "And then I feel like slapping myself until my head spins."
            "Because what in the hell was I even thinking just now?"
            "So I don't know the track."
            "So what?!?"
            "Only a moron would turn down the chance to dance with a girl like Reona!"
            "I shake my head and start to make for the dancefloor."
            mike.say "Sorry, Reona..."
            mike.say "Of course we can dance."
            mike.say "I'd dance to anything with you!"
            show reona happy
            "Reona's face breaks into a wide smile as she gets her way."
            hide reona
            show dance reona halloween
            with fade
            "But I hardly care about any dumb notion of a power struggle between us."
            "Because I spend the next few minutes pressed as close to her as possible."
            "When Reona said she wanted to dance, she was kidding."
            "What she does is pretty much grind herself against me the whole time!"
            "I can feel my heart beating faster by the moment."
            "I can feel sweat running down the back of my neck."
            "And best of all, I can feel every inch of Reona that's pressed against me!"
            "Plus there's the added bonus of seeing Jack and Scottie watching us."
            "Both of them with miserable, jealous looks on their faces!"
            "Of course that's not the most important thing."
            "But it really adds a sweetness to the experience."
            "One that means I'll remember for a long time to come!"
        "Yeah, I noticed the music, and I'm not dancing on it for a reason!":
            "I can almost hear Reona's body calling out to me."
            "Trying to use the siren's call of it's curves to seduce me!"
            "But I can't dance to a track I don't know."
            "That'll just end with me looking like a total prat!"
            "So I stand my ground and shake my head."
            show reona embarrassed
            mike.say "Uh-uh..."
            mike.say "No way, Reona."
            mike.say "I don't even know this track!"
            "Reona plants her hands on her hips."
            "Clearly more than a little pissed off at my decision."
            show reona sadshock
            reona.say "But, [hero.name]…"
            reona.say "I want to dance!"
            mike.say "Then you're just going to have to find another partner, Reona."
            show reona angry
            reona.say "Fine with me!"
            mike.say "Because there's no way that..."
            mike.say "Wait a minute..."
            hide reona with easeoutright
            mike.say "What did you say?"
            "Even as I'm asking the question, Reona's already walking off."
            "And rather than answer, she gives me a perfect illustration of what she means."
            "Because I watch as she strides straight over to Scottie and whispers in his ear."
            "He looks surprised, then delighted as he nods his head."
            "Then I'm treated to watching them walk onto the makeshift dancefloor together."
            "And I'm sure that Reona makes sure to dance extra close to the jerk as well!"
            "Letting me know that she's punishing me for refusing to do what she wanted just now."
    scene bg black with dissolve
    pause 1
    return

label reona_halloween_sex:
    scene bg livingroom with fade
    "By now it's starting to get late, and the party is beginning to slow down as people get tired."
    "Nobody seems to want to be on the makeshift dancefloor, and the punch bowl is almost totally empty."
    "I'm expecting people to start drifting off home pretty soon, as well as [bree.name] and Sasha to go to bed."
    "But before I can see anyone to the door, I have a minor mystery of my own to solve."
    "Which is that Reona disappeared off to the bathroom a good while ago now."
    "Normally I wouldn't be that concerned about her lingering on the toilet."
    "But with a lot of people wandering about the house and all the alcohol that's been consumed..."
    "Let's just say that I'm a little more keen to keep track of our guests than I normally would be."
    "Reona and I have been hitting the punch quite hard tonight too."
    "And with the costume that she's wearing, as well as some of her bad habits..."
    "Well, let's just say that I don't want her bumping into some of the male party guests right now."
    "But the problem is that I have to make it look like I'm just casually strolling towards the bathroom."
    "And not like I'm a paranoid boyfriend hurrying to keep his date from falling into the hands of another guy."
    "More than once I bump into someone on the way to the bathroom."
    "Which means that I instantly have to slow down and act normal."
    "In some cases I even have to exchange pleasantries with the person I meet too."
    "All of which takes up valuable time, as well as making me twitch with nervous energy."
    scene bg secondfloor
    with fade
    "So when I finally make it to the bathroom door, I feel like I'm on the verge of a breakdown!"
    "But I know that I need to collect myself before I do anything else."
    "I need to centre my energies and devise a coherent plan to get the door open."
    "That and be able to charm Reona out of the bathroom without looking like a total psycho."
    "I need to..."
    "Ah, fuck it..."
    scene bg door bathroom at center, zoomAt(1, (640, 720)) with fade
    "I'll just hammer on the door and yell for Reona's attention."
    show bg door bathroom at center, traveling(1.5, 0.3, (640, 1040))
    pause 0.3
    play sound door_banging
    "Balling up my fist, I raise it and proceed to thump the door pretty damn hard."
    "And at the same time, I shout or Reona to come out as well."
    mike.say "REONA..."
    mike.say "What in the hell are you still doing in there?"
    mike.say "Did you fall in and get stuck, or what?!?"
    "I don't really know what I'm expecting to happen next."
    "Maybe at the very best for Reona to open the door and explain herself."
    "Or at the worst to open it and slap the taste right out of my mouth."
    "But I definitely wasn't prepared for what actually happens."
    "Which is that Reona throws the door open and literally leaps out onto me!"
    show reona halloween shout at center, zoomAt (1.25, (800, 880)) with hpunch
    reona.say "[hero.name]..."
    show reona talkative
    reona.say "Think quickly!"
    show reona happy
    mike.say "What the..."
    show reona at center, zoomAt (2.0, (640, 1300)) with hpunch
    mike.say "Aargh!"
    "I barely manage to catch Reona and stay on my feet at the same time."
    "She must have leaped off the damn toilet and launched herself at me."
    "Because her arms are around my neck and her legs above my waist."
    "And I'm sure she couldn't have jumped that high from a standing start."
    mike.say "Reona..."
    mike.say "What are you..."
    mike.say "What are you doing?"
    show reona flirt
    "Reona's clinging to me so tightly that she pretty much answers straight into my ear."
    show reona talkative
    reona.say "What does it look like?"
    reona.say "I was waiting in here to surprise you, silly..."
    reona.say "And now that I've surprised you, we're supposed to fuck!"
    show reona flirt
    "Now don't get me wrong, normally that would be an offer I couldn't refuse."
    "But having someone leap onto you and hang off will really put a dampener on your mood."
    "So you'll forgive me if I don't instantly jump for joy and start stripping-off!"

    scene bg livingroom with dissolve
    pause 0.3
    scene bg bedroom1 with dissolve
    "Instead I rush her to my bedroom, kicking the closed door, shutting us inside."





    show reona kiss halloween with fade
    $ reona.flags.kiss += 1
    "Reona already has her lips clamped over mine, pushing her tongue into my mouth."
    "Plus I can feel her tearing at my clothes, desperately trying to undress me."
    "I reach down, trying to get a better hold on Reona."
    "My thinking is that maybe with that, I can get her under control."
    "But that's when my hands slide over the curve of her buttocks."
    "And then they pause at the bottom of her butt, weighing one in each palm."
    "All it takes is that one moment of handling Reona's assets to change my mind."
    "In an instant, all thought of trying to stop her simply vanishes."
    "Then I'm suddenly doing all that I can to aid Reona in her efforts."
    "The first thing that I do is twine my thumbs in the waistband of her panties."
    "And the I tug them downwards, not even trying to be subtle as I do so."
    "Ironically, this is the first thing I've done that makes Reona loosen her grip."
    "She does so because now she's realised that I've finally quit fighting her."
    "Now I'm doing all that I can to make sure she gets what she wants."
    "Even so, she only goes as far to give me the room I need to slide her panties down."
    "As soon as they reach her knees, she kicks them off and renews her hold on me."
    "But the next thing I know is that my pants are falling down!"
    "Reona chuckles as she sees my reaction, and I know that she must be responsible."
    "She must have undone them while I was pulling off her panties just now."



    scene bg black
    show reona missionary halloween mike
    with fade
    "I'm already trying to thrust upwards and into Reona."
    "But at the same time, she's doing something far more involved."
    "Because Reona's reaching down, trying to line up my cock just so."
    "She struggles to make things work as I bounce her up and down."
    "Yet somehow, on the third or fourth attempt, she gets it just right."
    show reona missionary eyes_open vaginal
    "This happens as she goes up in the air."
    "So when she comes down again, everything is in place."
    show reona missionary mouth_orgasm
    reona.say "Oh..."
    reona.say "Oh shit..."
    reona.say "That's...that's it!"
    show reona missionary mouth_normal
    "I hardly need Reona to tell me that things are lined up down there."
    "Because I can feel the sensation of my cock pressing against her pussy."
    "There's still resistance there, fighting against gravity and our desires."
    "But soon enough it begins to falter, and then Reona slowly opens up to me."
    "She inches down onto it slowly, a little at a time."
    show reona missionary forth eyes_hurt at stepback(speed=0.1, h=-10, v=0)
    play sexsfx1 slide_in
    play sound "sd/moans/sasha/sasha_breathing.ogg" loop volume 10
    "And the careful manner she uses is a sharp contrast to her former eagerness."
    "I suppose I should take that as a compliment."
    "Now she's getting exactly what she wanted from me."
    "And it's almost too much for her to handle."
    "I think about easing off for a moment, about going slower and more gently."
    play sexsfx1 fuck_calm loop
    play sound "sd/moans/sasha/sasha_panting.ogg" loop volume 10
    show reona missionary back
    pause 0.5
    show reona missionary forth eyes_hurt at stepback(speed=0.1, h=-10, v=0)
    pause 0.35
    show reona missionary back
    pause 0.2
    show reona missionary forth at stepback(speed=0.1, h=-10, v=0)
    pause 0.35
    show reona missionary back
    pause 0.2
    show reona missionary forth at stepback(speed=0.1, h=-10, v=0)
    "That's when Reona springs another surprise on me."
    "Without warning, she seems to come back to life again."
    "It's as if her body just needed to get the measure of my cock."
    "And now that Reona has it, she knows exactly what to do."
    "Not for the first time it strikes me how appropriate Reona's choice of costume is."
    "She's dressed up as a succubus, and she proceeds to pretty much drain the life out of me."
    show reona missionary back
    pause 0.5
    show reona missionary forth eyes_hurt at stepback(speed=0.1, h=-10, v=0)
    pause 0.35
    show reona missionary back
    pause 0.2
    show reona missionary forth at stepback(speed=0.1, h=-10, v=0)
    pause 0.35
    show reona missionary back
    pause 0.2
    show reona missionary forth at stepback(speed=0.1, h=-10, v=0)
    "Now Reona's the one bouncing up and down in my arms."
    "Relying on me to hold her up, she rides my cock like a crazy woman."
    "Every time she goes up, Reona then comes crashing down into the bathroom door."
    "And every time she lets out a gasp of pure pleasure too."
    play sexsfx1 fuck_moderate loop
    play sound "sd/moans/sasha/sasha_moans_hard_low.ogg" loop volume 10
    show reona missionary back
    pause 0.25
    show reona missionary forth mouth_orgasm with hpunch
    pause 0.15
    show reona missionary back
    pause 0.25
    show reona missionary forth with hpunch
    pause 0.15
    show reona missionary back eyes_close
    pause 0.25
    show reona missionary forth with hpunch
    pause 0.15
    show reona missionary back
    pause 0.25
    show reona missionary forth with hpunch
    "I'm worried that someone's going to come hammering on the door, just like I did."
    "Or else our combined weight will prove to be too much for it to take."
    "That it'll crack, then splinter and finally we'll go crashing through it."
    "And the sound of that will surely bring everyone in the house running."
    "But even though all of this is going through my mind, I don't stop for a moment."
    play sound "sd/moans/sasha/sasha_moans_hard_medium.ogg" loop volume 10
    show reona missionary back
    pause 0.15
    show reona missionary forth mouth_orgasm with hpunch
    pause 0.05
    show reona missionary back
    pause 0.15
    show reona missionary forth with hpunch
    pause 0.05
    show reona missionary back eyes_close
    pause 0.15
    show reona missionary forth with hpunch
    pause 0.05
    show reona missionary back
    pause 0.15
    show reona missionary forth with hpunch
    "Instead I keep right on thrusting up and into Reona."
    play sexsfx1 fuck_speed loop
    "Almost like my body's independent of my mind and can't be stopped."
    "Reona's almost as far gone as I am by now, maybe even more so."
    "She's stopped making noises of any kind, and simply clings onto me."
    "Though I have the distinct feeling this can't go on for much longer."
    "That's confirmed a moment later when I feel myself starting to lose it."
    "Reona must be able to feel it too, as she clings on tighter still."
    show reona missionary back
    pause 0.15
    show reona missionary forth mouth_orgasm with hpunch
    pause 0.05
    show reona missionary back
    pause 0.15
    show reona missionary forth with hpunch
    pause 0.05
    show reona missionary back eyes_close
    pause 0.15
    show reona missionary forth with hpunch
    pause 0.05
    show reona missionary back
    pause 0.25
    show reona missionary forth with hpunch
    "Then it happens, I shoot my load while I'm deep inside of her."
    play sexsfx1 fuck_sprint loop
    play sound "sd/moans/sasha/sasha_moans_hard_orgasm.ogg" loop volume 10
    show reona missionary eyes_hurt with hpunch
    "She shivers and then I feel her squeezing me like a hand."
    "And I know that she's being swept along with me too."
    play sexsfx1 final_thrust
    play sound "sd/moans/sasha/sasha_breathing.ogg" loop volume 10
    show reona missionary mouth_normal right_peace
    "Once it's over, I gingerly lower Reona to the ground."
    "Then I watch as she staggers around the bedroom, gathering up the pieces of her costume."

    "I'm not much more stable on my legs as I do the same, and I hurry to get dressed too."
    stop sexsfx1
    stop sound




    $ reona.sexperience += 1
    $ game.pass_time(1)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
