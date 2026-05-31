init python:
    Room(**{
    "name": "bedroom5",
    "exits": ["secondfloor", "bedroom2","bedroom3","bedroom4","bathroom"],
    "display_name": "Minami's Bedroom",
    "music": "music/roa_music/new_days.ogg",
    "conditions": [
                IsDone("minami_event_03"),
                PersonTarget(minami,
                    Not(IsHidden())
                    ),
        ],
    "outfit": "casual",
    "valid": False,
    "tags": ["home"],
    })

    Room(**{
    "name": "attic",
    "exits": ["secondfloor", "housemap"],
    "display_name": "Attic",
    "music": house_music(),
    "conditions": [
        Or(
            Not(IsDone("minami_event_03")),
            PersonTarget(minami,
                    Or(
                        IsHidden(),
                        IsGone(),
                        ),
                    ),
            )
        ],
    "outfit": "casual",
    "tags": ["home"],
    })

init python:
    Activity(**{
    "name": "cleaning_attic",
    "rooms": "attic",
    "conditions": [
        IsDone("minami_event_02"),
        HeroTarget(
            MinStat("energy", 5),
            MinStat("hunger", 5),
            MinStat("grooming", 5),
            MinStat("fun", 5),
            ),
        PersonTarget(minami,
            IsFlag("nomovein", False)
            ),
        ],
    "display_name": "Vacuum",
    "icon": "vacuum",
    "label": "cleaning_attic",
    "duration": 8,
    "do_once": True,
    })

label cleaning_attic:
    "So now that the idea of Minami moving in with me is set to become a reality, I need to actually find somewhere to put her."
    "She can't sleep in my room, and there's no way that I can ask [bree.name] or Sasha to share with her either."
    "I could stick her on one of the sofas in the sitting room, but that's not going to cut it in the long term."
    "Which leaves the attic as the only possibility, short of pitching a tent for Minami in the garden."
    "And that's not going to happen, as I just know that she'd find some way to make sure I was the one to use it!"
    "The only real problem that I can see with the plan of sticking Minami in the attic is that it'll need cleaning out."
    "And again, it's going to have to be me that does it, because it's pretty much my fault she's moving in to begin with."
    "So I resolve myself to the task ahead, trying to think of it as my punishment for inflicting Minami on all of us."
    "Thing is though, I haven't been in the attic since before I moved in here with Sam and Ryan."
    "Even then it was nothing more than the agent just showing us the space and then moving on."
    "All I remember is a dusty room, which we were assured would be gone before we arrived."
    "That's why I make my way up to the attic thinking that all it'll need is a good cleaning out."
    "But the moment that I walk through the door and flick on the light, my heart sinks into my feet."
    "The room looks just like it did the last time I was up here."
    "Save, that is, for the piles of cardboard boxes in the middle of the floor."
    "Where in the hell did this lot come from?"
    "I let out a tortured sigh, knowing full well how much harder the job just became."
    "Well, I did say that this was supposed to be my punishment."
    "So maybe I shouldn't complain, but just knuckle down and get it over with."
    "To this end, I drop all of the cleaning products and brushes that I've carried up there in a pile."
    "And then I take a look at the piles of boxes, trying to figure out where to start."
    "My first thought is to just toss the whole lot out with the trash."
    "Even if it's too much to cram into the bins, I could call the authorities to come take it away."
    "Failing that, I could even load it into the back of my car and drive it to the recycling centre myself."
    "It's then that I realise I have absolutely no idea just what's in any of the boxes."
    "If I want to go down the route of recycling it, then I need to know what I'm dealing with."
    "So I grab a box-cutter from my pile of tools, and then walk over to the nearest stack."
    "I see that there's something written on the flaps, though it's hard to make out."
    "It could be a date or an address, scrawled on there in permanent marker."
    "The handwriting looks vaguely familiar, but whatever it says means nothing to me."
    "So I just ignore it and slice through the tape sealing the box shut."
    "I honestly don't know what I was expecting to find inside of the first box."
    "But I swear it wasn't that it'd be full to the brim with photographs."
    "There are bundles and bundles of photographs - Polaroids and prints."
    "All of them are bound together with string, neatly tied and stacked up to the brim."
    "Intrigued by the find, I pick up a bundle at random, holding them up to the light."
    "What I see when my eyes adjust is totally unexpected, almost making me drop it in shock."
    "The picture at the top of the pile is a shot of a girl, laid on a bed in her underwear."
    "Intrigued, I leaf through the rest of the pile, watching the image move like a flip-book."
    "All of the shots are of the same girl, who seems not to care that her image is being captured."
    "As the images progress, she strips off ever more of her clothes until she's completely naked."
    "At first I'm surprised by the nature of the find, but not freaked out."
    "After all, it looks like I've simply stumbled on someone's forgotten porn stash."
    "But as I choose more of the bundles at random, a pattern begins to emerge."
    "Each and every one is of a girl in a compromising position, and none seem to know they're being photographed."
    "Little by little, this is starting to look more like the photo collection of a stalker than just a simple wank bank."
    "The true horror and realisation of just what I've stumbled upon becomes clear a moment later."
    "And it happens when I recognise one of the girls in the photos as someone I know all too well."
    "I see Sam, stripping off in a bathroom that I can't place."
    "I know that I should stop flipping through the photos right there and then."
    "But a terrible, morbid fascination keeps me going as she steps into the shower and washes herself."
    "Finally, with a shudder that leaves me feeling filthy, I toss the photos back into the box."
    "Taking a second glance at the handwriting on the box, I suddenly recall where I've seen it before."
    "It belongs to Ryan, no question about it."
    "For a moment I have absolutely no idea what to do next."
    "Should I call him and confront him?"
    "Or should I call Sam and tell her what I found?"
    "The logical thing would be to do neither and call the police."
    "But a large part of me would also be happy to just toss the whole lot in the garbage and forget all about it."
    "In the end, all I can decide is that I can't decide."
    "And so I gather up all of the boxes and stash them in the hallway cupboard, covering them with the junk already in there."
    "I try to forget about it as I hurry to clean the attic as I was supposed to."
    "But the idea of Minami sleeping where that creepy stuff was left still bugs me."
    "Once I'm done scrubbing and cleaning, the attic looks like an entirely different room."
    "I just hope it'll be enough to expunge the memory of what I found."
    "Though it won't do a thing to help me make a decision as to just what I do next..."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
