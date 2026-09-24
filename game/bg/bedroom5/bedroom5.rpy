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
    "Now that Minami moving in is becoming a reality, I need to actually find somewhere to put her."
    "She can't sleep in my room, and I can't ask [bree.name] or Sasha to share with her either."
    "That leaves the attic as the only real option — short of pitching a tent in the garden, which Minami would somehow turn into my problem."
    "The catch, of course, is that the attic needs cleaning out, and since it's my fault she's moving in, it has to be me who does it."
    "I haven't been up here since before I moved in with Sam and Ryan. Back then, the letting agent gave us a quick look and moved on."
    "All I remembered was a dusty room. So I head up expecting a straightforward clean."
    "The moment I flip on the light, my heart drops."
    "The room is exactly as I left it — except for the piles of cardboard boxes stacked in the middle of the floor."
    "Where on earth did those come from?"
    "I let out a heavy sigh. I'd said this was supposed to be my punishment, so I guess I can't complain."
    "I set down my cleaning supplies and grab a box-cutter, figuring I need to know what I'm dealing with before I decide whether to trash the lot."
    "Something is written on the flaps of the nearest box — a date or an address, scrawled in permanent marker."
    "The handwriting looks vaguely familiar, but I don't stop to think about it. I just slice through the tape and open the box."
    "I'm not sure what I expected to find. Certainly not this."
    "The box is packed to the brim with photographs — Polaroids and prints, bundled with string and stacked neatly inside."
    "Intrigued, I pick up a bundle at random and hold it up to the light."
    "The top photo is a girl lying on a bed in her underwear. I flip through the rest like a flip-book — the same girl, progressively undressing until there's nothing left."
    "At first I assume I've stumbled across someone's forgotten stash. Embarrassing, but not alarming."
    "Then I open more bundles, and a pattern begins to emerge."
    "Every single one features a different girl in a compromising position — and not one of them looks like they know they're being photographed."
    "The uneasy feeling in my gut hardens into something colder. This isn't a porn stash. This looks like the collection of a stalker."
    "Then I see her."
    "Sam. Photographed in a bathroom I don't recognise, completely unaware."
    "I know I should stop. I stop anyway — but not before a sick, morbid curiosity keeps me going just long enough to feel truly disgusted with myself."
    "With a shudder, I shove the photos back into the box and take a proper look at the handwriting on the flap."
    "It's Ryan's. I'm certain of it."
    "For a long moment I just stand there, not knowing what to do."
    "Call Ryan and confront him? Call Sam and tell her? Call the police? Or just throw the whole lot in the bin and act like I never saw any of it?"
    "I can't decide. So I do the only thing I can think of — I gather up every box and stash them in the hallway cupboard, burying them under the junk already there."
    "Then I get on with cleaning the attic, trying to push the whole thing out of my head."
    "It doesn't entirely work. The thought of Minami sleeping in the same room where that stuff was kept still unsettles me."
    "But once I'm done, the attic looks like a completely different place. Clean, aired out, almost welcoming."
    "I just hope that's enough to scrub the memory of what I found along with the dust."
    "Though it won't help me figure out what to do next — and that problem isn't going away."
    return
return