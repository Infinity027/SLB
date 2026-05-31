init 1:
    layeredimage bg university:
        attribute_function Pickers([DayNightPicker, SeasonPicker])
        group season auto variant "day"
        always:
            "snow"

init python:
    Room(**{
    "name": "university",
    "display_name": "University",
    "exits": ["map","library","classroom","dininghall"],
    "hours": (8, 18),
    "conditions": [
        IsDayOfWeek("123456"),
        IsHour(8, 18),
        Not(IsSpecialDate("christmas"))
        ],
    "music": season_music(),
    "random_music": True,
    "outfit": "casual",
    "tags": ["uni"],
    })

    Event(**{
    "name": "reona_teaser",
    "label": "reona_teaser",
    "conditions": [
        HeroTarget(
            IsGender("male"),
            IsRoom("university")),
        PersonTarget(bree,
            IsPresent(),
            Not(IsHidden()),
            MinStat("love", 100),
            ),
        ],
    "priority": 500,
    "do_once": True,
    })

label reona_teaser:
    "I make my way through the hall, only half paying attention."
    "I don't notice a group of people taking up too much space in the hallway and talking too loudly until one of them makes a gesture that goes too wide, almost hitting me in the face."
    mike.say "Hey!"
    "They don't seem to notice me even after shouting, and it's up to me to dodge myself out of the way, stumbling a bit to avoid a broken nose and bumping into another body as I do."
    "Great."
    "Now I'm the bad guy."
    show reona
    "I turn back to apologize to the petite girl I almost knocked over and pause, struck immediately by the sight of her."
    "Her skirt is so short it barely even begins to cover the curve of her hips, and my eyes linger for a moment on the hem of it, where I know her panties must only be hidden from me by a single fiber of the material."
    "My eyes trail up the bare, flawless, tanned skin of her midriff to her cleavage, full and generously present in what must be the highest grade push-up bra, practically smacking me in the face."
    "That must have been the plush, soft, blissful feeling of flesh I'd felt when I'd run into her."
    "The knowledge even in hindsight makes something in me stir."
    "She's stunning, though she looks like a caricature of that trend I've heard about...ganguro or gyaru?"
    "She's got flashy, admittedly tacky accessories and heavily bleached hair and thick, dark makeup painting her pretty features."
    "She's shamelessly, openly sucking on a lollipop shaped like a cock as she looks up at me with her big doe eyes."
    "Girl" "Hey."
    mike.say "I-I'm sorry."
    "I clear my throat to control my stammer before speaking on."
    mike.say "These idiots almost hit me, I didn't mean--"
    "Girl" "I know."
    "Her voice was soft and sultry and sweet all at once, and makes me feel strangely good inside, knowing I've got her full attention."
    "Girl" "I was watching you come down. I saw what happened."
    mike.say "Watching me?"
    "Why would she have been? Was I doing something stupid? Is there something in my teeth?"
    "She pops out her hip, exposing another half inch of her thighs on that side, and my eyes drop back down to the bare skin helplessly."
    "The girl brings the free hand not holding her lollipop up to the top button of her shirt, struggling to hold her bursting breasts inside, and she toys with it, slowly and intentionally, tugging it down a bit to give me a bit more of a view down into her shirt."
    "Girl" "Mhmm. You look like the kinda guy who can give a girl a good time."
    "A coy little smile curled at one corner of her lips, and she slipped the head of the lollipop back between them, trailing her tongue down along the shaft for a moment before continuing her thought."
    "Girl" "I can smell them from a mile away."
    "I'm stunned to silence for a moment by her brashness, shifting my weight and slipping my hands into my pockets, knowing I'll probably need to make some adjustments."
    menu:
        "That's right.":
            "I mean, I'm not going to deny that."
            mike.say "You're not wrong. Where'd you pick up a talent like that?"
            "Girl" "Mmm."
            "She slips the lollipop back into her mouth, pumping it between her pursed lips a few times before drawing it back out with an audible, satisfying pop."
            "Girl" "Call it practice."
            "She moves forward, just a little bit, but I'm highly conscious of the shrinking space between us, nearly suffocating me here in public in the sexual aura radiating off of her."
            "I know that she can show me a good time, too, and my pulse is helplessly quickening."
            "Girl" "Let's show each other what we can do..."
            "She purrs, winking as she reaches into her cleavage and pulls out a folded piece of paper, pressing it forward into my hand before I can even react."
        "Are you serious?":
            mike.say "Is this some kind of prank?"
            "I glance around the hallway, trying to find the group of people who are snickering at my expense. Girls like this don't really exist outside of tacky porn and wet dreams, right?"
            "...Right?"
            "The girl folds her arms beneath her amazing breasts, pursing her glossy lips into a pout."
            "Girl" "Are you telling me I'm wrong?"
            "I'm still not entirely convinced she's for real and not just messing with me, but I distinctly get the impression, suddenly, that I didn't answer her the way I should have."
            "Girl" "What's the matter? Can't get it up? I promise I can help with that."
            "She moved forward just the tiniest bit, but I'm hyper aware of the shrinking space between us, especially as she brings the lollicock back up to her tongue and runs it, tantalizingly, down the center of her tongue."
            "Girl" "Cum too quickly?"
            "She continues, and gives the candy one deep, good suck before popping it back out with an audible smack and running her tongue along her top lip."
            "Girl" "We can always just go again."
            "My heart is starting to beat harder in my chest, and I say nothing more as she reaches into her cleavage and pulls out a folded piece of paper pressing it forward against my chest with a flat palm."
            "Girl" "Give me a call sometime."
            "She winks."
            "Girl" "I'll show you."
    "I take the paper, given no choice in the matter, glancing up to watch her walk away as she turns and leaves me there, a little bit drunk off the encounter."
    "Her hips sway deliciously as she walks away, the bottom half of her ass cheeks visible and bouncing as she does, and I know full well that it's intentional."
    hide reona
    "I look down at the paper in my hand, unfolding it curiously. I can smell the perfume she used on it from here."
    "It says REONA, with a little heart and star doodled next to it, and then a phone number."
    "At the bottom corner there's a little dick doodled, cumming all over a tongue emoji."
    "Not subtle, maybe, but she's made damn sure I won't forget who Reona is when I read this again."
    show bree annoyed
    bree.say "Hey!"
    "I'm shocked out of my dreamy state, smiling down at her phone number as I daydream, by the sound of [bree.name]'s voice."
    "She sounds a little bit upset."
    "I turn back to see her jogging down the hall toward me, her brows knit."
    mike.say "[bree.name]? What's wrong?"
    bree.say "I saw you talking to that girl..."
    bree.say "Nobody knows what happened to her. She used to be sweet and quiet and now she's a total, shameless slut."
    "I didn't need to be told that; Reona had made that more than clear to me herself."
    "Still, [bree.name] seems genuinely concerned about it, and I can see it swimming in her big brown eyes."
    bree.say "Stay away from that one, alright? Everyone around here knows about her."
    "I'm not completely sure whether or not I want to stay away from her."
    "Something about her bold, blatant desire for my dick, the look in her eyes that told me she'd rather get on her knees and suck me off right there in the hall than be limited to her candy... was almost hypnotizing."
    "I don't think I've ever seen a girl that I knew wanted me that badly, for no reason at all except for the pleasure of it, and something about the idea is driving me crazy."
    mike.say "I'll keep it in mind."
    show bree cry
    "[bree.name] pouts a little bit, but seems to accept it for what it is."
    bree.say "I'm just looking out for you."
    "I give her a smile that's a little more reassuring, and she seems to relax entirely, smiling slightly back, though her brows remain slightly furrowed."
    mike.say "I know, [bree.name]. Thanks. You ready to head home?"
    bree.say "I've gotta stop and talk with one of my professors, actually, but I'll totally catch you later!"
    "I wave her off as she turns and jogs off, and exhale a sigh in the middle of the hallway where I'm left alone by both girls, processing my thoughts for a minute before I move on."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
