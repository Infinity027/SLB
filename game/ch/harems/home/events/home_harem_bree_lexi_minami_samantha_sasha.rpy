init python:
    Event(**{
    "name": "home_harem_sixsome",
    "label": "home_harem_sixsome_intro",
    "duration": 8,
    "priority": 1000,
    "conditions": [
        PersonTarget("lexi"),
        IsActiveHarem('home'),
        TogetherInHarem('home', 'bree', 'minami', 'samantha', 'sasha', 'lexi'),
        IsDayOfWeek(6, 7),
        IsTimeOfDay("afternoon"),
        HeroTarget(
            IsGender("male"),
            IsRoom("livingroom")),
        ],
    "do_once": True,
    })

label home_harem_sixsome_intro:
    scene bg livingroom with fade
    "This is it - I feel like I'm living the dream, like they'll write books about my exploits and adventures in years to come!"
    "I turn the corner into the living room, on what feels like an average weekend afternoon."
    "But I've also just walked in on five girls, all of them in the act of stripping off their clothes."
    show sasha underwear topless zorder 4 at center, zoomAt (1.0, (1080, 740))
    show bree underwear topless zorder 5 at center, zoomAt (1.0, (640, 740))
    with dissolve
    "Sasha and [bree.name], my housemates, already down to their underwear, all smiles and knowing glances."
    show minami topless zorder 1 at center, zoomAt (1.0, (420, 740)) with dissolve
    "Minami, my adopted sister, giggling in anticipation of what lies ahead as she pulls off her top."
    show lexi naked nophone bubblegum zorder 2 at center, zoomAt (1.0, (200, 740)) with dissolve
    "Lexi, already naked and chewing on her gum, as if this is something she does on a regular basis."
    show samantha underwear zorder 3 at center, zoomAt (1.0, (860, 740)) with dissolve
    "And Sam - the one that I was sure had got away from me, taking her time as she knows my eyes are on her."
    mike.say "Ah...I..."
    mike.say "What's going on in here?"
    sasha.say "Oh, hey, [hero.name]."
    show sasha happy
    sasha.say "I asked Sam and Lexi over for a little bit of fun."
    mike.say "I...I can see that!"
    show sasha normal
    sasha.say "I was going to tell you all about it."
    show sasha happy
    sasha.say "But then I thought it'd make a nice surprise."
    show sasha normal
    mike.say "I'm invited too?!?"
    show bree happy at startle
    show fx exclamation at center
    bree.say "Of course you are!"
    show bree normal
    show lexi happy
    lexi.say "You're bringing the cock!"
    show lexi normal
    show minami happy
    minami.say "It wouldn't be the same without you, big bro!"
    show minami normal
    show samantha blush
    samantha.say "After all, you're the one that brought us all together!"
    "I can't quite get my head around what all of this actually means."
    "Me and five girls?"
    "Five girls - did I say that already?"
    "Ah, who cares if I did!"
    "I'm about to fool around with five girls for god's sake!!!"
    "I feel like I'm part of some crazy reality show."
    "Or like I'm a character in one of those video games where you try to fuck your crush."
    "But most of all, I feel like I'm finally winning at the game of life!"
    "It seems like my feelings are plain to be seen, like they're written on my face."
    "Because each and every one of the girls is looking straight at me right now."
    "I see them whispering to each other, sharing secretive giggles of amusement."
    show sasha at center, traveling (1.2, 1.0, (1040, 800))
    show bree at center, traveling (1.2, 1.0, (640, 800))
    show minami at center, traveling (1.2, 1.0, (440, 800))
    show lexi at center, traveling (1.2, 1.0, (240, 800))
    show samantha at center, traveling (1.2, 1.0, (840, 800))
    "They advance as one, surrounding me and cutting off all potential means of escape."
    "Yeah, right - like I'm even thinking of escape!"
    "The next thing I know, their hands are all over me."
    "Only it's not in the pleasant way that you might think."
    "They're stripping me!"
    "I can hardly keep track of who's hands are where as they pull off my clothes."
    "And it doesn't take them long, thanks to the fact that I'm not wearing that much to begin with."
    "T-shirt, pants, socks and shorts - all of them are gone in a matter of seconds."
    show sasha naked happy
    show bree naked happy
    show minami naked happy
    show lexi naked
    show samantha naked
    with dissolve
    "That leaves me standing there, as naked as the girls are themselves."
    show lexi happy
    show samantha happy
    "They keep right on laughing and making sly comments, proud of their handiwork."
    "I can already feel my cock beginning to get hard."
    "It was even before they stripped me naked, and now it stiffens all the way."
    "Of course, this elicits another round of excited giggles and clapping."
    show sasha normal
    sasha.say "Okay, girls."
    sasha.say "On your knees, like we agreed!"
    show sasha at center, zoomAt (1.2, (1040, 1000))
    show bree at center, zoomAt (1.2, (640, 1000))
    show minami at center, zoomAt (1.2, (440, 1000))
    show lexi at center, zoomAt (1.2, (240, 1000))
    show samantha at center, zoomAt (1.2, (840, 1000))
    with ease
    "I watch as the five of them kneel before me, all looking up as they do so."
    scene bj breeleximinamisamsasha with fade
    "They're smiling and as they wait patiently for whatever's supposed to happen next."
    show bj breeleximinamisamsasha mike with dissolve
    sasha.say "Now it's your turn, [hero.name]."
    sasha.say "Five mouths, all watering for a taste of your cock."
    sasha.say "Which one of us are you going to choose?"
    $ sixsome_bj_bree = False
    $ sixsome_bj_lexi = False
    $ sixsome_bj_minami = False
    $ sixsome_bj_samantha = False
    $ sixsome_bj_sasha = False
    $ sixsome_bj = 5
    while sixsome_bj != 0 and hero.energy > 0:
        menu:
            "Sasha" if not sixsome_bj_sasha:
                $ sixsome_bj_sasha = True
                call home_harem_sixsome_bj_sasha from _call_home_harem_sixsome_bj_sasha
                $ hero.energy -= 1
                $ sixsome_bj -= 1
            "Samantha" if not sixsome_bj_samantha:
                $ sixsome_bj_samantha = True
                call home_harem_sixsome_bj_samantha from _call_home_harem_sixsome_bj_samantha
                $ hero.energy -= 1
                $ sixsome_bj -= 1
            "[bree.name]" if not sixsome_bj_bree:
                $ sixsome_bj_bree = True
                call home_harem_sixsome_bj_bree from _call_home_harem_sixsome_bj_bree
                $ hero.energy -= 1
                $ sixsome_bj -= 1
            "Minami" if not sixsome_bj_minami:
                $ sixsome_bj_minami = True
                call home_harem_sixsome_bj_minami from _call_home_harem_sixsome_bj_minami
                $ hero.energy -= 1
                $ sixsome_bj -= 1
            "Lexi" if not sixsome_bj_lexi:
                $ sixsome_bj_lexi = True
                call home_harem_sixsome_bj_lexi from _call_home_harem_sixsome_bj_lexi
                $ hero.energy -= 1
                $ sixsome_bj -= 1
    show bj breeleximinamisamsasha -mike
    if hero.energy <= 0:
        call home_harem_sixsome_disappointed_bj_ending from _call_home_harem_sixsome_disappointed_bj_ending
        if 'do_event' in locals() and do_event:
            $ hero.cancel_event()
        if not sixsome_bj_bree:
            $ bree.love -= 5
        if not sixsome_bj_lexi:
            $ lexi.love -= 5
        if not sixsome_bj_minami:
            $ minami.love -= 5
        if not sixsome_bj_samantha:
            $ samantha.love -= 5
        if not sixsome_bj_sasha:
            $ sasha.love -= 5
        $ game.pass_time(2)
        return
    jump home_harem_sixsome_sex_intro

label home_harem_sixsome_bj_bree:
    "I don't know why, but the moment I catch [bree.name]'s brown eyes, it just has to be her."
    "Maybe I'm just a sucker for a cute blonde."

    mike.say "[bree.name]."
    "[bree.name] looks almost surprised that I've chosen her out of all the girls before me."
    "And the happiness it brings out in her expression makes me want her all the more."
    "I can feel my cock twitching with anticipation as she crawls toward me."
    show bj breeleximinamisamsasha breefront breelick
    "[bree.name] reaches out with both hands, gently guiding my cock to her mouth."
    "Her lips open slowly, and she takes it inside a little way."

    show bj breeleximinamisamsasha breeblow
    "And when she wraps her lips around it, the sensation is like heaven."
    "[bree.name] really is concentrating that hard - concentrating on pleasing me!"
    "Her head begins to move back and forth, slowly working the length of my cock."
    "This means that every moment is drawn out and lingering."
    "I feel like [bree.name]'s taking me on a journey, lifting me to a higher plane."
    "I could see myself floating away in a trance."
    "But not before I let her lick and suck me enough to lose it!"
    "That's why it becomes almost a battle to keep my head in the moment."
    "[bree.name]'s doing such a good job that I was starting to forget where I am!"
    "I shake my head, trying to throw off the almost hypnotic feeling that's taken hold."
    "And [bree.name] seems to pick up on it too, redoubling her efforts as I do so."
    "The sudden change in pace is more than enough to do the trick."
    "But it's also enough to make me cum too!"
    menu:
        "Cum in her mouth.":
            "There's no chance of me stopping it now, no chance in hell."
            with hpunch
            "Which means that I cum while my cock is still in [bree.name]'s mouth."
            show bj breeleximinamisamsasha breeinmouth with hpunch
            "That breaks the spell almost instantly, making [bree.name]'s eyes pop open in surprise!"
            with hpunch
            "She chokes on the mouthful that I've just given her, swallowing it reflexively."
            "[bree.name] smiles at me as I pull my cock out of her mouth."
            "But I can see that her eyes are watering all the same."
        "Cum on her face.":
            "I whip my cock out of [bree.name]'s mouth, much to her evident surprise."
            show bj breeleximinamisamsasha breecumshot breelick with hpunch
            pause 0.2
            with hpunch
            "Her eyes pop open just in time to see me cum in her face."
            show bj breeleximinamisamsasha breeonface with hpunch
            "Seeing it all spattering her cheeks and nose kind of breaks the spell."
            "But the yelping sounds that she lets out as it rains down on her more than make up for it."
    show bj breeleximinamisamsasha breeback -breeblow -breelick -breecumshot
    return

label home_harem_sixsome_bj_lexi:
    "You know what they say - when you want a job done right, call a professional!"
    mike.say "Lexi."

    "She responds by raising an eyebrow while regarding it bobbing in front of her face."
    "And somehow that nonchalant look turns me on more than any show of enthusiasm ever could!"
    "Lexi makes a show of pulling the gum out of her mouth before she gets down to it."
    show bj breeleximinamisamsasha lexifront lexilick
    "Then she finally leans forward towards my cock, happy to take her time in doing so."
    "When her lips wrap themselves around it, I know that I'm in for a ride."
    "Lexi begins slowly, showing me what she can do even at such a sedate pace."
    show bj breeleximinamisamsasha lexiblow
    "The feeling makes me pant almost instantly, hinting at what's still to come."
    "Seriously, her tongue feels like a snake inside of her mouth."
    "I can feel its every move and I swear it shouldn't be able to do half of what it does!"
    "When Lexi's head begins to move back and forth, she picks up speed."
    "Gradually the pace of the blowjob increases and the sensations along with it."
    "Pretty soon she's working on me like a jack-hammer."
    "And the sounds that I'm making in sympathy become louder too."
    "I don't know what the other girls are thinking as they watch Lexi."
    "But I hope that it's making them think about upping their games to match hers!"
    "It's no surprise that I can soon feel the urge to come taking hold of me."
    "And I'm pretty sure that Lexi knows it too."
    "As she seems to redouble her efforts at the same time."
    menu:
        "Cum in her mouth.":
            "It comes on me quicker than even I was expecting."
            show bj breeleximinamisamsasha lexiinmouth with hpunch
            "And so I end up shooting my load in Lexi's mouth mere seconds later."
            with hpunch
            "But she doesn't even seem to slow down for a moment as I do so."
            with hpunch
            "Instead she takes all that I have to give and swallows it down."
            "Lexi gulps every drop of the cum, not coughing even once."
        "Cum on her face.":
            "When I pull my cock out of her mouth, Lexi gasps reflexively."
            show bj breeleximinamisamsasha lexicumshot lexilick with hpunch
            "But she doesn't look at all surprised by my course of action."
            with hpunch
            "Instead she closes her eyes and opens her mouth as wide as possible."
            show bj breeleximinamisamsasha lexionface with hpunch
            "This means that a good portion of my cum actually lands on her waiting tongue."
            "Lexi seems to bask in the shower, enjoying every moment."
            "It's almost as if she sees it as a reward for her performance."
    show bj breeleximinamisamsasha lexiback -lexiblow -lexilick -lexicumshot
    return

label home_harem_sixsome_bj_minami:
    "Even as I'm looking from one girl to the next, I can feel Minami's eyes upon me."
    "And when I finally cast a glance in her direction, she almost jumps to her feet!"
    "It's like she wants to stand up and wave at me, desperate to be chosen over the others."
    "I don't know if that's what actually makes my mind up, the eagerness she's showing."
    "Or I just like the idea of choosing the youngest and least experienced of all the girls."

    show bj breeleximinamisamsasha minamifront minamilick
    "She leans forward to meet my cock, actually clapping at having been chosen."
    "Her eyes are fixed on the tip, almost making them go crossed as it comes closer."
    "Minami licks her lips one last time, and then parts them to wrap around the head."
    show bj breeleximinamisamsasha minamiblow
    "She begins sucking almost the same moment that her lips are sealed."
    "And what she lacks in experience, she more than makes up for in enthusiasm."
    "Her head goes back and forth, making her short bob bounce in sympathy."
    "I can see Minami's cheeks becoming hollow from the effort too."
    "And it reminds me of watching her suck a milkshake through a straw!"
    "But joking aside, the sensation of it is something else entirely."
    "All of that enthusiasm means that I'm already gasping from her efforts."
    "I have no idea of Minami's been practising in private, or if she's just got a natural talent."
    "Either way, I have to ask her to do this more often!"
    "Maybe next time I'll be more prepared and able to last longer too."
    "Because I'm going to shoot my load any second!"
    menu:
        "Cum in her mouth.":
            with hpunch
            "Minami's eyes pop open in surprise as I shoot everything I have down the back of her throat."
            show bj breeleximinamisamsasha minamiinmouth with hpunch
            "She almost spits my cock out of her mouth as she struggles to swallow it all down without choking."
            with hpunch
            "There's still cum dripping from her lips once she's managed to recover her senses."
            "But she smiles up at me the whole time, clearly delighted to have been my first choice."
        "Cum on her face.":
            "My cock pops out of Minami's mouth with an audible sound."
            show bj breeleximinamisamsasha minamicumshot minamilick with hpunch
            pause 0.2
            with hpunch
            "She opens her eyes in surprise, just as the cum hits her in the face."
            show bj breeleximinamisamsasha minamionface with hpunch
            "Minami yelps and cries out as it stripes her cheeks and lips."
            "Her hands wave desperately and she bounces on the spot."
            "All of which makes the act just that much more rewarding!"
    show bj breeleximinamisamsasha minamiback -minamiblow -minamilick -minamicumshot
    return

label home_harem_sixsome_bj_samantha:
    "Even with all of this feminine beauty lined up before me, there's still only one girl I can choose."
    "And that's Sam, something that I know the moment that I look my cupcake in the eye."
    "She smiles up at me, batting her eyelids just enough to hopelessly ensnare me."
    "And I think she knows that she's won out in that moment too."
    "As I see her lips curl into a knowing smile, even before I turn to face her."
    show bj breeleximinamisamsasha samanthafront samanthalick
    "Sam keeps things demure and understated as she reaches out for my cock."
    "But all that does is serve to make my breathing that much heavier."
    "Somehow the promise of her destroying the illusion of her innocence is so very hot!"
    "She purses her lips a little, and then sticks out her tongue."
    "The tip strokes the head of my cock, and I shiver at the sensation."
    "The sound makes Sam look up at me, and she giggles with glee."
    "This means that I'm panting in anticipation even before she swallows it."
    show bj breeleximinamisamsasha samanthablow
    "And when she does I almost moan at the sensation."
    "Sam works me eagerly, licking and sucking energetically."
    "Every time her head bobs up and down, I think that it's going to be the end."
    "Every thrill she manages to send through me makes me think I'm going to cum."
    "All of which means that, when the actual moment comes, I'm taken by surprise."
    "I have no idea if Sam senses what's about to happen."
    "But if not, she's about to find out!"
    menu:
        "Cum in her mouth.":
            with hpunch
            "As soon as I shoot my load in her mouth, Sam's eyes open in shock."
            show bj breeleximinamisamsasha samanthainmouth with hpunch
            "She coughs and splutters as the cum hits the back of her throat."
            with hpunch
            "Sam soon manages to recover and keep herself from choking on it."
            "She drags her mouth off of my cock, still coughing a little."
            "But the smile on her face as she wipes her mouth lets me know there's no harm done."
        "Cum on her face.":
            "The first thing that Sam knows about it is me pulling my cock out of her mouth."
            show bj breeleximinamisamsasha samanthacumshot samanthalick with hpunch
            pause 0.2
            with hpunch
            "And she still looks puzzled when she gets a shower of cum in the face too!"
            show bj breeleximinamisamsasha samanthaonface with hpunch
            "But soon enough I see her expression turn into one of amusement."
            "She opens her mouth in an effort to catch some of the stuff."
            "And she's smiling the whole time she does so."
    show bj breeleximinamisamsasha samanthaback -samanthablow -samanthalick -samanthacumshot
    return

label home_harem_sixsome_bj_sasha:
    "Maybe it's because she seems to be the one taking the lead in all of this."
    "Or maybe it's because I want to put something in that sly mouth of hers."
    "But I just can't help pointing my cock straight towards Sasha."
    "She smiles up at me knowingly as I do so, as if she was sure I'd pick her all along."
    show bj breeleximinamisamsasha sashafront sashalick
    "And then she lowers her eyes, devoting all of her attention to the task at hand."
    "Sasha purses her lips, placing a kiss on the very tip of my cock."
    "But then she parts them just a little, enough to let in an inch at the most."
    "I can feel her tongue begin to caress it, even with so little inside if her mouth."
    show bj breeleximinamisamsasha sashablow
    "And the sensation becomes all the more incredible as she inches it deeper inside."
    "Soon she's taken me as deep as it's possible to go, holding it there for a moment."
    "Then Sasha starts to work her head back and forth, sucking as she goes."
    "The feeling is so good, so intense, that I forget there's anyone else here."
    "And it's only when I actually look down that I remember the others are there too!"
    "Their presence doesn't seem to be doing anything to stop Sasha though."
    "As she keeps right on working away at my cock for all she's worth."
    "It's only now that I realise I've been gasping the whole time."
    "But now the sound is getting all the more intense, as though I'm building up to something."
    "Sasha seems to notice it too."
    "Her eyes open and she looks up at me knowingly."
    "We both know that I'm about to cum..."
    menu:
        "Cum in her mouth.":
            "It's too late for me to do anything other than keep right on going."
            with hpunch
            "And so I don't hesitate to let myself go inside of Sasha's mouth."
            show bj breeleximinamisamsasha sashainmouth with hpunch
            "She gags a little as it hits the back of her throat."
            with hpunch
            "But she's prepared for it, and begins to swallow it down without complaint."
            "I pull my cock out of her mouth once I'm done, strings of semen still dripping from the tip."
        "Cum on her face.":
            "At the last moment, I pull my cock out of Sasha's mouth."
            show bj breeleximinamisamsasha sashacumshot sashalick with hpunch
            "This leaves it hanging open as I shoot my load into her a second later."
            with hpunch
            "Cum rains down on her cheeks, nose and lips in sticky loops."
            show bj breeleximinamisamsasha sashaonface with hpunch
            "And there's not even time for her to blink before it hits her face."
    show bj breeleximinamisamsasha sashaback -sashablow -sashalick -sashacumshot
    return

label home_harem_sixsome_disappointed_bj_ending:
    "I stagger backwards almost as soon as I'm finished cumming, panting and gasping for breath."
    "It's all that I can do to keep upright, my legs feeling wobbly and weak from my exertions."
    "The girls are all watching me, expectant looks on their faces for what's going to happen next."
    "But slowly it dawns on one of them after another that I'm not putting on a show for their benefit."
    "I really am totally and utterly spent, ready to collapse at the mere thought of going on."
    "They look more than a little disappointed, especially those that sat out the blowjob just now."
    mike.say "Sorry...girls...I..."
    mike.say "I...just...can't..."
    "They greet my attempt at an apology and explanation with nods and smiles."
    "But I can see from the look in their eyes that they're seriously disappointed."
    "All I can do is offer a weak smile and a shrug in return."
    "That and hope they don't go looking for someone with more stamina..."
    return

label home_harem_sixsome_sex_intro:
    "Sure, I'm panting and sweaty from the effects of the blowjob that I just got given."
    "But I can already feel my heart-rate slowing down, and my breathing's almost back to normal too."
    "I guess all that time spent hitting the gym and getting in shape paid off after all."
    "Because I'm already feeling my second wind, and I'm more than ready for another round!"
    "And it seems as though the girls have noticed it too."
    "Sasha walks over to the sofa and waves for the others to join her."
    "She climbs onto the cushions with her back turned to me."
    scene sixsome breeleximinamisamsasha with fade
    "And soon enough she's flanked by Lexi and Minami on the left, with Sam and [bree.name] on the right."
    "Without saying a word, Sasha begins to shake her ass at me."
    "The others are quick to follow her example, putting on quite a show."
    "And it's made that much better by them looking back over their shoulders, laughing and smiling."
    mike.say "Mmm..."
    mike.say "It's like a sexy coconut shy!"
    mike.say "But which one am I gonna choose to throw my balls at?"
    sasha.say "Right down the middle!"
    bree.say "NO - a little to the right!"
    samantha.say "Yes to the right - but a bit further!"
    lexi.say "Uh-uh...you know you want to shoot to the left!"
    minami.say "Right here, if you want a tight little target!"
    "Look, I know that we're all of us playing this up for laughs."
    "But I just have to stand back for a moment and really take it all in."
    "Every one of these girls is gorgeous in their own unique way."
    "And a guy'd be as lucky as hell to have a chance with any one of them."
    "So how on earth am I supposed to be able to choose?"
    "In an ideal world, I'd be superhuman and able to satisfy them one by one."
    "But as it is, I just have to bite the bullet and choose!"
    "So I take a step forward and reach out for the ass of my choice..."
    $ sixsome_sex_bree = False
    $ sixsome_sex_lexi = False
    $ sixsome_sex_minami = False
    $ sixsome_sex_samantha = False
    $ sixsome_sex_sasha = False
    $ sixsome_sex = 5
    while sixsome_sex != 0 and hero.energy > 0:
        menu:
            "[bree.name]" if not sixsome_sex_bree:
                $ sixsome_sex_bree = True
                call home_harem_sixsome_sex_bree from _call_home_harem_sixsome_sex_bree
                $ hero.energy -= 1
                $ sixsome_sex -= 1
                $ bree.sexperience += 1
            "Lexi" if not sixsome_sex_lexi:
                $ sixsome_sex_lexi = True
                call home_harem_sixsome_sex_lexi from _call_home_harem_sixsome_sex_lexi
                $ hero.energy -= 1
                $ sixsome_sex -= 1
                $ lexi.sexperience += 1
            "Minami" if not sixsome_sex_minami:
                $ sixsome_sex_minami = True
                call home_harem_sixsome_sex_minami from _call_home_harem_sixsome_sex_minami
                $ hero.energy -= 1
                $ sixsome_sex -= 1
                $ minami.sexperience += 1
            "Samantha" if not sixsome_sex_samantha:
                $ sixsome_sex_samantha = True
                call home_harem_sixsome_sex_samantha from _call_home_harem_sixsome_sex_samantha
                $ hero.energy -= 1
                $ sixsome_sex -= 1
                $ samantha.sexperience += 1
            "Sasha" if not sixsome_sex_sasha:
                $ sixsome_sex_sasha = True
                call home_harem_sixsome_sex_sasha from _call_home_harem_sixsome_sex_sasha
                $ hero.energy -= 1
                $ sixsome_sex -= 1
                $ sasha.sexperience += 1
    show sixsome breeleximinamisamsasha -mikebree -mikelexi -mikeminami -mikesamantha -mikesasha
    if hero.energy <= 0:
        call home_harem_sixsome_disappointed_sex_ending from _call_home_harem_sixsome_disappointed_sex_ending
        if 'do_event' in locals() and do_event:
            $ hero.cancel_event()
        if not sixsome_sex_bree:
            $ bree.love -= 5
        if not sixsome_sex_lexi:
            $ lexi.love -= 5
        if not sixsome_sex_minami:
            $ minami.love -= 5
        if not sixsome_sex_samantha:
            $ samantha.love -= 5
        if not sixsome_sex_sasha:
            $ sasha.love -= 5
        $ game.pass_time(2)
        return
    else:
        call home_harem_sixsome_satisfied_sex_ending from _call_home_harem_sixsome_satisfied_sex_ending
        $ bree.love += 5
        $ lexi.love += 5
        $ minami.love += 5
        $ samantha.love += 5
        $ sasha.love += 5
        call sleep (["bree", "lexi", "minami", "samantha", "sasha"]) from _call_sleep_home_harem_sixsome
        return

label home_harem_sixsome_sex_bree:
    "I don't know exactly what it is that makes my mind up in the end."
    "But maybe it's the wink that [bree.name] gives me over her shoulder that seals the deal."
    show sixsome breeleximinamisamsasha mikebree
    "As soon as she does that, I feel like I'm being drawn straight to her."
    "She sees that she's caught my eye a second later, smiling as I come ever closer."
    "[bree.name] shakes her ass, as if I need any more encouragement, and giggles."
    bree.say "Ooh..."
    bree.say "Do you want some of this?"
    bree.say "Then you just come and get it!"
    show sixsome breeleximinamisamsasha big
    "I can almost feel my cock begin to twitch at the promise of what's ahead."
    "So not wanting to waste another moment, I take hold of [bree.name]'s haunches."
    menu:
        "Fuck her ass":
            "I wonder if [bree.name] knew exactly what I had in mind when she offered me her ass like that."
            "Because that's what I'm coming for, drawn hypnotically towards her perfect, pert buttocks."
            "I'd say not, as she gasps pretty loud when I part them and stick my cock in the space between."
            "[bree.name] looks back over her shoulder as I begin to press the head against her asshole."
            show sixsome breeleximinamisamsasha breeblush
            "The expression on her face is one of shock, but not alarmed."
            "It's as though surprise and intrigue are fighting it out inside of her head right now."
            show sixsome breeleximinamisamsasha breefuck anal
            "But that doesn't stop me for a second, and I push my cock further into her ass."
            "As I do so, I see the look on her face undergo a subtle change."
            "[bree.name]'s eyes almost glaze over as the muscles of her ass are forced to part."
            "Her mouth begins to fall open as the sensations overtake her."
            "And by then I'm too far into her to even consider stopping."
            show sixsome breeleximinamisamsasha breepleasure
            "[bree.name] seems to be melting from what I'm doing to her."
            "But all the same, I see her hands holding into the sofa for dear life."
            "And that grip only gets stronger as I begin to thrust in and out of her."
            "By now [bree.name]'s ass is offering almost no resistance at all."
            "Sure, it still feels nice and tight around my cock."
            "But it's getting softer and more yielding the whole time."
            "This just makes me want to pound her that much harder."
            "And so that's exactly what I do, using all of my energy to do it."
            show sixsome breeleximinamisamsasha breeahegao
            "Every thrust seems to make [bree.name] sink that much deeper into a state of helplessness."
            "My guess is that, without the support of the sofa, she's be in a heap on the floor by now!"
            "And on top of that, she's about to get a whole lot more in that department."
            "Because I can feel myself getting ready to cum!"
            menu:
                "Cum inside":
                    "Even if I did choose to warn her, I don't think [bree.name]'s in any state to hear me."
                    show sixsome breeleximinamisamsasha breeanalcum with hpunch
                    "And so I just keep on going until the very moment that I shoot my load inside of her."
                    with hpunch
                    "She makes a strangled sound that's part surprise and part ecstasy."
                    with hpunch
                    "And then collapses forwards onto the back of the sofa, panting for dear life."
                    "She slides off of my cock as she does so."
                    show sixsome breeleximinamisamsasha -breefuck -breeanalcum breeanal breecum breeanalgape
                    "Which leaves strings of cum stretched between it and her quivering ass."
                "Pull out":
                    "There's no point warning [bree.name] of what I'm about to do."
                    "She's too far gone to even hear me, let alone understand."
                    show sixsome breeleximinamisamsasha breecumshot breecum -breefuck with hpunch
                    "And so I just pull my cock out of her ass without warning."
                    "[bree.name] let's out a cry that's equal parts shock and delight."
                    with hpunch
                    "She collapses onto the back of the sofa, just as I shoot my load over her."
                    show sixsome breeleximinamisamsasha breeonbody breeanalgape with hpunch
                    "The cum paints her buttocks and thighs as she pants in sheer exhaustion."
            $ bree.flags.anal += 1
        "Fuck her pussy":
            "Eager to show [bree.name] just how much I want her right now, I don't waste any more time."
            "All it takes is a quick thrust of the pelvis, and she knows all she need to know about my intentions."
            "[bree.name] makes a kind of breathy gasping sound as I push the head of my cock against her pussy."
            "The lips are already soft and slick, enough that she offers almost no resistance to me."
            show sixsome breeleximinamisamsasha breefuck vaginal
            "Even so, I choose to go in slowly, enjoying the sensation of sinking into her."
            "And the restraint that I'm showing pays off in spades, as [bree.name] quivers and shakes in response."
            "This means that by the time I'm as deep into her as I can go, she's totally helpless."
            "And as I start to move inside of her, I have [bree.name] in the palm of my hand."

            show sixsome breeleximinamisamsasha breepleasure
            "Her eyes are wide and her mouth hangs open."
            "And yet she's nodding for all that she's worth, urging me on."
            "It's good to know what we're on the same page right now."
            "But it's not like I need any kind of encouragement!"
            "I redouble my efforts almost without as much as a conscious thought."
            show sixsome breeleximinamisamsasha breeblush
            "Which means that the last of the attention [bree.name] was able to give me is soon gone."
            "Instead, all she can do is turn her head forwards."
            "That and take what she's being given in ever larger doses too!"
            "Pretty soon it's almost impossible to say which is louder."
            show sixsome breeleximinamisamsasha breeahegao
            "The grunts that I'm making as I relentlessly pound away at [bree.name]."
            "Or else the moans and cries that she lets out in sympathy to them."
            "And then there's the sound of my thighs slapping against her buttocks!"
            "Neither of us can go on like this for much longer."
            "So it comes as no surprise when I feel myself reaching my climax mere moments later..."
            menu:
                "Cum inside":
                    "[bree.name]'s way too far gone to know what's about to happen."
                    with hpunch
                    "And so I don't say a word as I shoot my load inside of her."
                    show sixsome breeleximinamisamsasha breevaginalcum with hpunch
                    "Her head rears up as she cries out from the sensation."
                    with hpunch
                    "Then she suddenly goes limp, falling onto the back of the sofa."
                    "This means that she also slides straight off of me."
                    show sixsome breeleximinamisamsasha -breefuck -breevaginalcum breevaginal breecum breevaginalgape
                    "And strings of cum stretch out from her pussy to my cock."
                "Pull out":
                    "I don't stop to let [bree.name] know what I'm about to do."
                    "And even if I did, I doubt that she'd even hear me."
                    show sixsome breeleximinamisamsasha breecumshot breecum -breefuck with hpunch
                    "That means that when I pull my cock out of her pussy, it's totally without warning."
                    "The moan that comes out of [bree.name] then is a mixture of surprise and pleasure."
                    with hpunch
                    "All that keeps her from collapsing into a heap is the back of the sofa."
                    show sixsome breeleximinamisamsasha breeonbody breevaginalgape with hpunch
                    "And she pants helplessly as my cum spatters all over her back, buttocks and thighs."
    show sixsome breeleximinamisamsasha breepleasure -breeblush -breecum -anal -vaginal -breecumshot
    return

label home_harem_sixsome_sex_lexi:
    "Sure, I have a choice of five gorgeous asses lined up before me to choose from."
    "And yeah, all of the girls are trying their best to show off their own unique charms."
    "But when it comes to the crunch, Lexi doesn't even have to try all that hard to ensnare me."
    "Sometimes you want sweet and innocent, almost virginal qualities in a girl."
    "But sometimes you just want something filthy that'll leave you feeling the same way."
    "It's like the old saying about steak and a burger - and Lexi's definitely the burger!"
    show sixsome breeleximinamisamsasha mikelexi bubblegum
    "She winks at me as I approach her, still blowing bubbles with the gum she's chewing."
    lexi.say "Oh yeah, [hero.name]?"
    lexi.say "Why are you lookin' at me like that, huh?"
    lexi.say "You want somethin'?"
    lexi.say "Maybe you want me?"
    "Only now does Lexi begin to shake her ass at me."
    "And the effect is almost immediate."
    show sixsome breeleximinamisamsasha big
    "I go instantly from eyeing her up to wanting her desperately!"
    "The very next second, my hands seize on that hypnotic ass of hers."
    "And Lexi let's out the filthiest peal of laughter that I've heard in my life."
    menu:
        "Fuck her ass":
            "I don't know what it is that makes me part her buttocks and aim for her ass."
            "It's not any desire to conquer Lexi or teach her an imagined lesson."
            "More likely it's just my natural response to the dirtiness of her nature."
            "Either way, Lexi shows no shock or surprise when she feels my cock between her buttocks."
            lexi.say "Oh, I see."
            lexi.say "THAT'S what you want!"
            lexi.say "Sure, you can have it."
            lexi.say "So long as you promise to make me feel it!"
            "Is that...is that a challenge?!?"
            "Before I can even think of a response to that, I'm already acting on it."
            show sixsome breeleximinamisamsasha lexifuck anal
            "I push the head of my cock into Lexi's ass without a moment of hesitation."
            show sixsome breeleximinamisamsasha lexipleasure
            "She lets out a sound that's part grunt and part snigger."
            "But I can feel her muscles trying to resist all the same."
            "Another forceful push on my part and I'm past the point of no return."
            "One more serious push and I'm all the way into her, as deep as I can go."
            "Only now does Lexi's demeanour begin to change."
            show sixsome breeleximinamisamsasha lexiblush
            "Where before she was goading me into action, now she seems to lose that air of arrogance."
            "And as I start to move my cock in her ass, she succumbs to the sensations she's feeling."
            "Pretty soon she's gone from defiant to almost submissive."
            show sixsome breeleximinamisamsasha lexiahegao
            "And all the while she's been made to ride my cock!"
            "I don't know if this is all part of the act that Lexi likes to put on."
            "Whether she's letting me think that I've made her submit to get more out of me."
            "But it's not like I really care if she's for real or not right now."
            "I'm enjoying myself far too much to start playing mind-games."
            "Instead I keep right on pounding away at Lexi's ass."
            "But my enthusiasm means that I'm galloping ahead without pacing myself."
            "And soon enough I can feel the first throes of my climax fast approaching!"
            menu:
                "Cum inside":
                    "I've come this far, if you'll forgive the pun."
                    "And I'm not about to stop now, right at the climax."
                    "So I don't, instead pushing my cock as deep into Lexi as possible."
                    show sixsome breeleximinamisamsasha lexianal with vpunch
                    "I hear her gasp and moan as I shoot my load up her ass."
                    with vpunch
                    "And the sound of it squelching around my cock inside of her..."
                    show sixsome breeleximinamisamsasha -lexifuck lexicum lexianalgape with vpunch
                    "Well, it's almost as satisfying as the feeling I experience at the same time."
                "Pull out":
                    "I feel the need to underline the act in some way."
                    with vpunch
                    "And so I yank my cock out of Lexi's ass just before I cum."
                    show sixsome breeleximinamisamsasha lexicumshot lexicum -lexifuck with vpunch
                    "She makes a helpless sighing sound as I do so, moaning at the loss."
                    show sixsome breeleximinamisamsasha lexionbody lexianalgape with vpunch
                    "But I'm already painting her buttocks with sticky stripes of semen."
                    "Lexi looks back over her shoulder at me, panting and gasping in sheer exhaustion."
            $ lexi.flags.anal += 1
        "Fuck her pussy":
            "All it takes is for me to catch the merest glimpse of Lexi's pussy between her buttocks."
            "The light catches it as I do so, letting me know just how much it's glistening right now."
            "She's already wet and ready for it, and so who am I to say no to an invitation like that?"
            "The moment that I have my hands on her, Lexi seems to know it as well."
            lexi.say "Ooh..."
            lexi.say "My pussy's SO ready for you, [hero.name]."
            lexi.say "It's so hot and wet..."
            lexi.say "Just waiting for you to..."
            "I don't give Lexi enough time to finish what she was about to say."
            show sixsome breeleximinamisamsasha lexifuck vaginal
            "Instead I cut her off in mid-flow by pushing my cock between her slick lips."
            "There's only a token moment of resistance before she melts."
            "And I feel myself sinking into her, going as far as I can in one motion."
            show sixsome breeleximinamisamsasha lexipleasure
            lexi.say "Mmm..."
            lexi.say "That's more like it!"
            lexi.say "Now fuck me, [hero.name] - fuck me real hard!"
            "It's not like she needs to encourage me!"
            "Even as Lexi issues the order, I'm already thrusting in and out of her."
            show sixsome breeleximinamisamsasha lexiblush
            "She laughs in sheer delight at the pace I'm setting."
            "And her body seems more than ready to take all that I have to give."
            "It's not gentle or delicate in any way, just me pounding Lexi for all I'm worth."
            show sixsome breeleximinamisamsasha lexiahegao
            "She eats it up eagerly, her gasps and cries only serving to spur me on."
            "The only thing as loud as Lexi right now is the sound of my thighs slapping against her ass!"
            "I want to keep on going until she collapses from exhaustion."
            "I want to fuck her until she can't take it anymore and begs me to stop."
            "But unfortunately, I'm only human."
            "And I can feel that I'm about to cum!"
            menu:
                "Cum inside":
                    "I'm going too fast and in too deep to have a hope of pulling out now."
                    "And so I just keep right on going, thrusting into Lexi until the very last moment."
                    show sixsome breeleximinamisamsasha lexivaginal with vpunch
                    "When I shoot my load, I hold still, as far into her as I can possibly go."
                    with vpunch
                    "Lexi lets out a what's almost a scream as I fill her with all I have."
                    show sixsome breeleximinamisamsasha -lexifuck lexicum lexivaginalgape with vpunch
                    "And I can feel the sensation of it beginning to seep out of her around my cock."
                "Pull out":
                    "I pull my cock out of Lexi the moment before I cum."
                    show sixsome breeleximinamisamsasha lexicumshot lexicum -lexifuck with vpunch
                    "She groans at the sensation, shivering as it's dragged out of her."
                    with vpunch
                    "But then she wails in surprise as her buttocks are painted with semen."
                    show sixsome breeleximinamisamsasha lexionbody lexivaginalgape with vpunch
                    "Lexi looks back over her shoulder, head hanging low with exhaustion."
                    "But I can see that she's smiling, still quivering from the after-shocks."
    show sixsome breeleximinamisamsasha lexipleasure -lexiblush -lexicum -bubblegum -anal -vaginal -lexicumshot
    return

label home_harem_sixsome_sex_minami:
    "I think I already knew that I was going to choose Minami over all the other girls."
    "And from the look on her face as I make for her, she must have know it too!"
    show sixsome breeleximinamisamsasha mikeminami
    "She's just so petite and cute, all of that mischief wrapped up in a sexy little package."
    "I swear that my cock's actually getting harder the closer I get to her!"
    show sixsome breeleximinamisamsasha big
    "Minami covers her mouth to stifle and giggle of anticipation."
    "Which of course only serves to make me want her all the more."
    minami.say "Oh, big bro..."
    minami.say "It's SO big!"
    minami.say "Do you really think there's room inside of me?!?"
    "With that, Minami makes a show of wiggling her ass and thrusting it out towards me."
    "And from that moment on, I know that I couldn't change my mind if I wanted to."
    "I put my hands around her slender little waist and pull her roughly backwards."
    "She yelps in alarm, but then bursts into another peal of giggles."
    "And now all I have to decide is what I'm going to do with her..."
    menu:
        "Fuck her ass":
            "Minami already teased me enough to make this about more than just fucking."
            "In fact it feels like she's almost challenging me, seeing how far I'll go."
            "Which is why it just feels right to part her buttocks and aim for her ass."
            "She barely has time to notice what I'm doing before it's too late to object."
            minami.say "Huh..."
            minami.say "Wha..."
            minami.say "Oh...oooh..."
            minami.say "Oh...big bro!"
            show sixsome breeleximinamisamsasha minamifuck anal
            "Minami all but purrs and pouts as I push my cock into her tight little ass."
            "It's firm and puts up a genuine fight as I enter her."
            "But her muscles just aren't strong enough to keep me out."
            "And I can tell from the way she's beginning to pant that Minami's enjoying every moment."
            "That means that once I've conquered her unconscious resistance, she's totally defenceless."
            "She's mine to do with as I like!"
            "I start out slow and gentle, enjoying the feeling of being inside her."
            show sixsome breeleximinamisamsasha minamipleasure
            "Every inch of Minami's body seems to quiver in response to my presence."
            "But slowly I ramp up the speed and strength of my thrusts."
            show sixsome breeleximinamisamsasha minamiblush
            "And each one makes her tremble and shake all the more."
            "I could be disappointed in the fact that Minami's frame is petite."
            "Which means that she can't absorb what I'm giving her with any kind of ease."
            "But the reverse is true, as I'm getting off on just how much my size affects her."
            "Every action that I take is magnified thanks to her slight body."
            show sixsome breeleximinamisamsasha minamiahegao
            "And all of my efforts are plain to see in the way she twitches on the end of my cock."
            "The only problem is that she can't keep up the pace forever."
            "So it must be at least a small mercy for her when I begin to cum!"
            menu:
                "Cum inside":
                    "It's partly out of curiosity that I keep my cock inside of Minami as I cum."
                    show sixsome breeleximinamisamsasha minamianal with vpunch
                    "I want to see what her neat little body can do with all that I have to give."
                    with vpunch
                    "And I know that she can feel me lose myself in her, because she lets out a cry of surprise."
                    with vpunch
                    "I feel the muscles of Minami's ass almost go into spasm around my cock."
                    show sixsome breeleximinamisamsasha -minamifuck minamicum minamianalgape
                    "But I keep it as deep inside of her as possible, even as the cum begins to seep out around it."
                "Pull out":
                    "I'm actually worried that Minami's ass is just too small for me to cum inside."
                    show sixsome breeleximinamisamsasha minamicumshot minamicum -minamifuck with vpunch
                    "And that's why I yank my cock out of there in the last moments before I lose it."
                    with vpunch
                    "Minami writhes and wriggles as I do so, like she's been shocked with a taser."
                    show sixsome breeleximinamisamsasha minamionbody minamianalgape with vpunch
                    "And she's still not recovered when I paint her buttocks with semen a second later."
                    show sixsome breeleximinamisamsasha sashaonbody lexionbody
                    "She's so slim and slender that some of it misses her entirely, hitting the girls to their side!"
            $ minami.flags.anal += 1
        "Fuck her pussy":
            "I know that Minami was only teasing me just now, trying to get me more worked up."
            "But something about the idea of it not fitting inside of her is stuck in my mind."
            "I just can't stop thinking about that tight little pussy of hers."
            "Well, that and the chance to see how much it can actually take!"
            "Parting her buttocks, I aim my cock straight for the neat folds of her pussy."
            "The lips are soft and slick against the head, inviting me to go further."
            minami.say "I promise that I'll try, big bro."
            minami.say "I'll let you put as much in me as you can."
            minami.say "I hope I can take it all..."
            "Minami hardly needed to give me a sultry pep-talk like that."
            "But hearing the promise and fake submission in her voice certainly spurs me on."
            "And I don't hesitate to pull her onto my cock a moment later."
            show sixsome breeleximinamisamsasha minamifuck vaginal
            "Minami squeals in genuine surprise as I enter her, pushing as deep as I can."
            "I don't stop until my cock is buried as far inside as I can manage."
            show sixsome breeleximinamisamsasha minamipleasure
            "As I do this, her squeals turn into pants and then moans of pleasure."
            "I stay there for what feels like an eternity, just enjoying the moment."
            "But as still as I manage to remain, the same can't be said for Minami."
            show sixsome breeleximinamisamsasha minamiblush
            "She writhes and squirms on the end of my cock, wriggling in the sensations it's causing her to feel."
            "And I enjoy the feeling that it gives me in turn, even without the need to move a muscle."
            "Finally I relent and begin to move inside of Minami."
            "The effect that this has on her is easy to imagine."
            show sixsome breeleximinamisamsasha minamiahegao
            "She starts to moan and cry out, digging her fingers into the back of the sofa."
            "Pretty soon I feel like she's being hoisted into the air on my cock."
            "And even her slight weight is enough to make me reach my climax."
            menu:
                "Cum inside":
                    "Minami's eyes go wide as I shoot my load deep inside of her little pussy."
                    show sixsome breeleximinamisamsasha minamivaginal with vpunch
                    "She makes sounds that are barely identifiable as words, babbling all the while."
                    with vpunch
                    "But I keep right on riding her until the last moment, filling her all the way."
                    with vpunch
                    "Cum begins to seep out around the shaft of my cock even before I'm done."
                    show sixsome breeleximinamisamsasha -minamifuck minamicum minamivaginalgape
                    "And when I finally pull out of her, Minami collapses onto the back of the sofa, utterly spent."
                "Pull out":
                    "At the last moment, I actually start to worry that Minami's pussy might be too small after all."
                    show sixsome breeleximinamisamsasha minamicumshot minamicum -minamifuck
                    "That's why I drag it out of her the moment before I actually cum."
                    with vpunch
                    "She begins to writhe as it slips out of her pussy, as if she's being shocked with a taser."
                    show sixsome breeleximinamisamsasha minamionbody minamivaginalgape with vpunch
                    "And she's still wriggling when I lose it over her buttocks a second later."
                    show sixsome breeleximinamisamsasha sashaonbody lexionbody with vpunch
                    "Thanks to her ass being so petite and slender, Sasha and Lexi get a share to either side of her too!"
    show sixsome breeleximinamisamsasha minamipleasure -minamiblush -minamicum -anal -vaginal -minamicumshot
    return

label home_harem_sixsome_sex_samantha:
    "All it takes is one look over the shoulder from Sam to make my mind up completely."
    "It just has to be my cupcake that gets it this time around, no contest."
    "And I think she knows that she's ensnared me the moment that our eyes meet."
    "Which would explain why she giggles and sticks her ass out towards me."
    show sixsome breeleximinamisamsasha mikesamantha
    "And all of that before I even start to make a move in her direction too!"
    "Where I'm sure most of the other girls would tease or taunt me, Sam stays silent."
    "I think it's because of the strong bond that we share after all this time."
    "She doesn't need to make a show of it, she has me in her power enough already!"
    show sixsome breeleximinamisamsasha big
    "And as soon as that peach of an ass is in my hands, that's it."
    "No power on earth could tear me away from what I'm about to do!"
    menu:
        "Fuck her ass":
            "I know I just waxed lyrical about the bond that exists between Sam and me."
            "But that doesn't mean I see her in a high-minded, poetical manner."
            "In fact, she makes me feel downright filthy most of the time."
            "And that's why I part her buttocks, pushing my cock against her asshole."
            samantha.say "Ooh..."
            samantha.say "What are you doing back there?"
            samantha.say "You naughty boy!"
            "I can't help chuckling to myself at the feigned innocence in her voice."
            "And my response is merely to pull her towards me."
            "Pull her towards me and at the same time thrust my pelvis forwards too."
            "The result is that my cock hits it's target square and true."
            show sixsome breeleximinamisamsasha samanthafuck anal
            "And I begin to push my way into Sam in earnest."
            show sixsome breeleximinamisamsasha samanthapleasure
            "It takes some effort to begin with, and I hear her moan at the sensation."
            "But the fact that Sam's ass is nice and tight is a large part of the appeal."
            "All the resistance does is make me that much more resigned to overcome it."
            "Pretty soon I'm as far into her as I can go, loving every moment."
            "Sam seems to be getting as much out of it as me."
            show sixsome breeleximinamisamsasha samanthablush
            "She gasps and sighs as I move in and out of her."
            "And the way her muscles are quivering and trembling is something else!"
            "It makes fucking her ass feel like I'm getting a hand-job at the same time."
            "Taken with the sounds that she's making, it's the complete package."
            show sixsome breeleximinamisamsasha samanthaahegao
            "There's not much more that Sam could be doing to please me right now."
            "Well, apart from making me cum."
            "And she's just about to add that to the list too!"
            menu:
                "Cum inside":
                    "It's not like I planned to shoot my load this deep into Sam's ass."
                    show sixsome breeleximinamisamsasha samanthaanalcum with hpunch
                    "But things have kind of gotten away from me in the last couple of minutes."
                    with hpunch
                    "And so that's just what I end up doing!"
                    with hpunch
                    "Her low sounds of pleasure suddenly transform into yelps of surprise."
                    show sixsome breeleximinamisamsasha -samanthafuck -samanthaanalcum samanthaanal samanthacum samanthaanalgape
                    "Not that it makes me stop for an instant as I fill her to bursting."
                "Pull out":
                    "I somehow manage to shake myself into awareness as I feel myself cumming."
                    show sixsome breeleximinamisamsasha samanthacumshot samanthacum -samanthafuck with hpunch
                    "A moment later I yank my cock out of Sam's ass, shooting my load even as I do so."
                    with hpunch
                    "She yelps in surprise at the sudden sensation, and then again as it rains down."
                    show sixsome breeleximinamisamsasha samanthaonbody samanthaanalgape with hpunch
                    "The cum spatters Sam's buttocks, running down her thighs and onto the sofa beneath."
            $ samantha.flags.anal += 1
        "Fuck her pussy":
            "And perhaps it's that same connection that leads me straight to Sam's pussy."
            "Seriously, it's like the thing has a hold on me, pulling me in with it's own gravity!"
            "No sooner am I close enough to push my cock between her thighs than I can feel it."
            "The head brushes those hidden folds, and that's it."
            "Sam's pussy is the only thing that I can think of."
            "It's the only thing that'll satisfy my cravings!"
            samantha.say "Ooh..."
            samantha.say "That feels nice..."
            samantha.say "Please - put it inside of me!"
            "With an invitation like that - how can I say no?!?"
            "It takes me just a couple of seconds and a twitch of the thighs."
            show sixsome breeleximinamisamsasha samanthafuck vaginal
            "And with that, I feel myself slip inside of Sam."
            "If anything, she's even more willing than I am right now."
            "She swallows me all the way, until I'm balls deep into her."
            "And there's not a hint of resistance the whole way in."
            show sixsome breeleximinamisamsasha samanthapleasure
            "Sam begins to sigh and moan even before that point."
            "Meaning that as I begin to move back and forth, she's already practically panting."
            "It's like her body is one gigantic sponge, soaking up all that I have to give."
            show sixsome breeleximinamisamsasha samanthablush
            "She doesn't object in the slightest as I push her against the back of the sofa."
            "Which is good, because that's the only thing keeping her upright!"
            "Well, maybe that and the length of my cock that's inside of her right now..."
            show sixsome breeleximinamisamsasha samanthaahegao
            "Either way, Sam seems to be in a state of delirium."
            "She sways and writhes as I pound away at her."
            "And I feel like I've never been this deep inside of her."
            "That and as though I never made her melt like this before now!"
            "But I can't keep on going forever."
            "And a moment later, I feel myself starting to cum..."
            menu:
                "Cum inside":
                    "It's not like I planned to shoot my load this deep into Sam's pussy."
                    show sixsome breeleximinamisamsasha samanthavaginalcum with hpunch
                    "But I'm so into it now that there's no chance of turning back."
                    with hpunch
                    "And I hardly have time to breathe before I'm filling her!"
                    with hpunch
                    "At this, Sam seems to come back to the waking worlds."
                    show sixsome breeleximinamisamsasha -samanthafuck -samanthavaginalcum samanthavaginal samanthacum samanthavaginalgape
                    "Sitting up and riding my cock to the very last."
                "Pull out":
                    "Sam sags forwards as I pull my cock out of her pussy in one smooth motion."
                    show sixsome breeleximinamisamsasha samanthacumshot samanthacum -samanthafuck with hpunch
                    "I'm starting to cum even as I do this, and so she gets a showering a second later."
                    "This seems to snap Sam out of the trance that she'd fallen into."
                    with hpunch
                    "She sits up and let's out a yelp of surprise as it does so."
                    show sixsome breeleximinamisamsasha samanthaonbody samanthavaginalgape with hpunch
                    "The cum spattering her buttocks, running down her thighs and onto the sofa beneath."
    show sixsome breeleximinamisamsasha samanthapleasure -samanthablush -samanthacum -anal -vaginal -samanthacumshot
    return

label home_harem_sixsome_sex_sasha:
    "It's almost too easy to just walk straight forwards and place my hands on Sasha's ass."
    show sixsome breeleximinamisamsasha mikesasha
    "But that's what I find myself doing without even thinking about it for as much as a second."
    "Maybe it's because she seems to have been the ring-leader in all of this fun and games."
    "Or maybe she's just the one that perks my interest the most at this moment in time."
    "Either way, I zero in on her and that's it decided, there's no one else I want to fuck more!"
    sasha.say "Well, hello there!"
    sasha.say "I've been expecting you..."
    "It's not like Sasha's banter is putting me off."
    "But I feel the urge to get down to business."
    show sixsome breeleximinamisamsasha big
    "And so I pull her backwards and onto my cock without answering."
    menu:
        "Fuck her ass":
            "And as soon as she feels it pressing against her asshole, Sasha shuts up too."
            show sixsome breeleximinamisamsasha sashafuck anal
            "Well, when I say that, what I mean is that she stops talking!"
            "Instead she starts to make the cutest little yelping sounds."
            "And she keeps these up as I begin to push my way into her too."
            "Sasha's ass resists me to begin with."
            "Which only makes it feel that much better."
            "But then her muscles finally surrender."
            "And it's like her entire body melts around my cock."
            "Only now do her yelps seem to melt too, stretching out into long moans of pleasure."
            "The sound has an effect on me too, making me slow down my pace more than a little."
            "This means that I can enjoy the sensation of thrusting in and out of Sasha."
            "But at the same time I also feel the need to draw out more moans too."
            show sixsome breeleximinamisamsasha sashapleasure
            "Sasha looks back over her shoulder at me, her mouth hanging open."
            "And I can tell from the look in her eye that she's loving every moment of this!"
            "Spurred on by her approval, I begin to pick up speed."
            show sixsome breeleximinamisamsasha sashablush
            "Sasha holds my eye for a while, nodding eagerly."
            "But soon I'm going so fast and pounding her so hard that she can't keep it up."
            "Instead her head turns around to face forwards as the sensation becomes too much."
            "All that she can do now is hold onto the sofa as if for dear life!"
            "I have no idea what the other girls are doing right now."
            show sixsome breeleximinamisamsasha sashaahegao
            "They could be a million miles away for all it seems to matter."
            "There's only me, Sasha and my cock shoved as far up her ass as I can get it!"
            "And neither of us can keep up this pace for much longer..."
            menu:
                "Cum inside":
                    with vpunch
                    "So it comes as no great shock to me that I shoot my load into Sasha's ass a moment later."
                    show sixsome breeleximinamisamsasha sashaanal with vpunch
                    "Though from the sound that she makes as I do so, it wasn't something she was expecting either!"
                    with vpunch
                    "Sasha practically wails as I thrust into her as far a possible while I'm cumming."
                    "And I hold my cock there as long as I can manage once it's over too."
                    show sixsome breeleximinamisamsasha -sashafuck sashacum sashaanalgape
                    "I can feel the muscles of her ass quivering around my cock even before I pull it out of her."
                    "And feel the first of the cum begin to drip out around it."
                "Pull out":
                    "I end one of the backwards thrusts by pulling my cock all the way out of Sasha's ass."
                    show sixsome breeleximinamisamsasha sashacumshot sashacum -sashafuck with vpunch
                    "She wails at the sensation of it leaving her body, her muscles quivering at the loss."
                    with vpunch
                    "But I'm too busy watching as I shoot my load over her exposed buttocks."
                    show sixsome breeleximinamisamsasha sashaonbody sashaanalgape with vpunch
                    "It rains down on them, beginning to run in rivulets over her thighs and towards the mattress."
            $ sasha.flags.anal += 1
        "Fuck her pussy":
            "All it takes is a little angling for my cock to press against Sasha's pussy."
            "And the sensation seems to be more than enough to put her at a loss for words."
            "Because she immediately stops talking and instead lets out a long moan."
            "And the moan keeps right on going as I stroke the head of my cock against her lips."
            "She's already slick down there, her pussy feeling like it's begging to be fucked."
            show sixsome breeleximinamisamsasha sashafuck vaginal
            "So I don't hesitate to put on a little more pressure and begin to sneak inside."
            "My guess is right, as she parts with almost no protest or resistance."
            "And sliding into her feels as smooth as silk."
            "A sensation that makes me hold it right there once it's all the way in."
            show sixsome breeleximinamisamsasha sashapleasure
            "By now, Sasha's moans have turned into pants of arousal."
            "She looks back over her shoulder at me, mouth hanging open."
            "But for all that I can see she's loving it, the look in her eyes tells me she wants more."
            "That's why I begin to move inside of her then, slowly at first."
            "As soon as I do, Sasha begins to nod eagerly."
            show sixsome breeleximinamisamsasha sashablush
            "And the approval is all that I need to know that this is what she wants."
            "After that, my speed starts to increase, thrusting in and out of Sasha's pussy."
            "There's no way that she can keep on looking back over her shoulder."
            "And her head begins to sag forwards as the sensation overtakes her entire body."
            show sixsome breeleximinamisamsasha sashaahegao
            "The sounds that she's making are more like the groans of an animal now."
            "As if she's being reduced to a state of pure pleasure and delight."
            "But she's not the only one that's feeling the effects of what I'm doing."
            "And I know that I can't keep this up much longer..."
            menu:
                "Cum inside":
                    with vpunch
                    "So it's inevitable that I shoot my load a couple of seconds later."
                    show sixsome breeleximinamisamsasha sashavaginal with vpunch
                    "Yet the sound that comes out of Sasha at the same moment suggests she wasn't ready for it!"
                    with vpunch
                    "She cries out as I fill her with all that I have to give, not stopping until I'm spent."
                    "Even afterwards I keep my cock buried deep inside of her."
                    show sixsome breeleximinamisamsasha -sashafuck sashacum sashavaginalgape
                    "The sensation of her soft pussy quivering around me is just that good."
                    "As well as that of the first drops of cum starting to leak out of her too."
                "Pull out":
                    "Without warning, I pull my cock all the way out of Sasha's pussy."
                    show sixsome breeleximinamisamsasha sashacumshot sashacum -sashafuck with vpunch
                    "She lets out a wail of surprise, and her buttocks quiver as I do so."
                    with vpunch
                    "But then I shoot my load over her ass, spattering her thighs with my cum."
                    show sixsome breeleximinamisamsasha sashaonbody sashavaginalgape with vpunch
                    "It begins to run down her thighs as she pants from utter exhaustion."
    show sixsome breeleximinamisamsasha sashapleasure -sashablush -sashacum -anal -vaginal -sashacumshot
    return

label home_harem_sixsome_disappointed_sex_ending:
    "My breathing is finally back under control, and my heart's no longer pounding away inside of my chest."
    "And though I feel utterly spent, I'm also feeling like I just had one of the best times of my entire life!"
    "But it's not just me that's feeling that way either."
    "I look around the room, noting where my cock's been."
    "And I'm greeted by similarly tired, yet satisfied smiles too."
    "It's only when I bother to take a look at where it hasn't that I feel my mood begin to plummet."
    "Sure, no one that missed out on getting some is actually complaining about it."
    "They're all smiles, putting a happy face over their feelings."
    "But I can tell that, this time, there just wasn't enough of me to go around."
    "This means that my own smile becomes forced too, as I start worrying about it."
    "Maybe next time I can do something to work on my stamina and staying power."
    "Well, that is if there's going to be a next time!"
    "I certainly hope that there will."
    "I just hope the girls are up for giving me a second chance to please them all..."
    return

label home_harem_sixsome_satisfied_sex_ending:
    "I'm breathing hard and I can feel my heart beating like a jack-hammer inside of my chest."
    "But all the same, I'm feeling great - like I could keep this up all night!"
    "Yet when I stop to take a look around, I realise that the same can't be said for the girls."
    "Each and every one of them is slumped on the sofa, panting and gasping for breath."
    "All in all, they look like a collection of marionettes with their string cut."
    "Well...if the puppets in question were all naked and freshly-fucked!"
    mike.say "Erm...guys?"
    mike.say "Are you okay?"
    "Almost as one, they make a groaning sound."
    "Their heads turn to regard me, exhaustion written all over their faces."
    sasha.say "Jesus, did you drop a Viagra or something?"
    bree.say "I feel like I got ridden in a horse race!"
    minami.say "Oooh...big bro - I can't feel my pussy!"
    lexi.say "Yeah - I feel like I should be paying for that kind of treatment!"
    samantha.say "Warn me the next time you're going to do that!"
    "I can't help smiling at the responses they just gave me."
    "Sure, they're pretty much collapsed in a heap of limbs right now."
    "But every last one of them is completely and utterly satisfied."
    "I did it, I handled all five of them!"
    "I feel like some kind of sexual superhero."
    "Or at least like I should get some kind of title and a medal to go with it!"
    return

label bree_lexi_minami_samantha_sasha_male_ending:

    if renpy.has_label("home_harem_achievement_7") and not game.flags.cheat:
        call home_harem_achievement_7 from _call_home_harem_achievement_7
    $ game.room = "church"
    scene bg church
    scene bg church wedding
    with fade
    "You know, some days it feels like the most normal and natural thing in the world to be marrying five girls."
    "I mean it's legal, we're all consenting adults that are more or less sane, and nobody's being blackmailed into it."
    "But on the other hand, I can sometimes find myself feeling like the leader of some crazy sex cult too!"
    "It was hard enough to get to grips with the fact that I managed to hook up with [bree.name] or Sasha."
    "So it felt crazy to become involved with the pair of them at the same time."
    "And when Minami moved in, I was almost sure it'd put an end to what we had going on."
    "But instead she wound up getting in on the action too, which none of us saw coming."
    "Likewise I'd written Sam off as the one that got away."
    "After all, she was married and I was spoken for three times over."
    "Yet somehow she not only found out about the threesome I had going, but joined it too!"
    "And then there was Lexi..."
    "Wow..."
    "How do you factor someone like Lexi into any picture?"
    "Let alone how do you fit her into what was going on between me and four other girls?"
    "But somehow she just seemed to slot right in there, like it was meant to be!"
    "And there was no need to sugar-coat it for her either."
    "Lexi just jumped straight in there and took to the whole thing like a duck to water!"
    "In the end, it all worked out well."
    "So well, in fact, that we decided to make it official."
    "Which is how I come to be here."
    "Standing at the altar and waiting for five brides to walk down the aisle!"
    "Even when the music begins to play, it still doesn't quite feel real."
    "And I actually consider pinching myself just to check I'm not dreaming."
    "But what snaps me out of it in the end is the sight of the girls coming towards me."
    show sasha wedding normal zorder 4 at center, zoomAt (1.0, (1080, 740))
    show bree wedding normal zorder 5 at center, zoomAt (1.0, (640, 740))
    show minami wedding normal zorder 1 at center, zoomAt (1.0, (420, 740))
    show lexi wedding normal nophone zorder 2 at center, zoomAt (1.0, (200, 740))
    show samantha wedding normal zorder 3 at center, zoomAt (1.0, (860, 740))
    with dissolve
    "[bree.name], Sasha, Minami, Sam and Lexi walk down the aisle together."
    "They come in a loose knot, rather than turning it into some kind of procession."
    "This means that they look like a group of friends and equals, for which I'm glad."
    "Because them trooping up one after another would have made this feel a little too weird!"
    "They chose to keep their dresses under wraps while we were planning all of this."
    "And so I'm seeing them for the very first time as they walk towards me."
    "Every one of them is different, their choices a perfect reflection of their personalities."
    show bree wedding happy
    "[bree.name]'s dress is perhaps the closest to the traditional, being white and floaty."
    "But somehow she manages to make it come alive with the warmth of her smile."
    show sasha wedding happy
    "Sasha is almost the exact opposite, clad in black that contrasts her pale skin."
    "She's every bit as mysterious and intriguing as [bree.name] is open and honest."
    show minami wedding happy
    "Next comes Minami, the shortest of the five, but the most bursting with life."
    "Her dress is made of traditional, patterned silk."
    "But the cut is modern and quirky, just like her."
    show samantha wedding happy
    "Sure, I've seen Sam in a wedding dress before now."
    "Though I find myself forgetting that mental image as soon as I see her in this one."
    "Somehow she looks a million times better from the altar than from amongst the guests!"
    show lexi wedding happy
    "And Lexi, the girl that I've always thought of as the princess of the trailer park."
    "Well, let's just say she looks more like a princess than ever."
    "She'll always be trash."
    "But who knew that trash could look so good?"
    if bree.is_visibly_pregnant and lexi.is_visibly_pregnant and minami.is_visibly_pregnant and samantha.is_visibly_pregnant and sasha.is_visibly_pregnant:
        "Maybe I should be sweating and nervous at the sight of five large baby-bumps."
        "And I have no idea what the guests sitting in the pews must think of the girls all being pregnant at once."
        "But the truth is that I really don't care - we're already a big family, and soon to be bigger still!"
    elif not bree.is_visibly_pregnant and not lexi.is_visibly_pregnant and not minami.is_visibly_pregnant and not samantha.is_visibly_pregnant and not sasha.is_visibly_pregnant:
        "I can't stop staring at [bree.name], Sasha, Minami, Sam and Lexi as they stand beside me at the altar."
        "My five brides - soon to be my five wives!"
    else:
        if bree.is_visibly_pregnant:
            "[bree.name]'s dress looks like it's performing a minor miracle."
            "Her bump is getting huge, but I can hardly see it right now!"
            "Not that either of us wants to hide the fact she's expecting."
        if sasha.is_visibly_pregnant:
            "Sure, Sasha has a lot of make-up on today, but she's looking pale under it all."
            "For a moment I worry that she's not doing well, glancing at her swollen belly."
            "She seems to note my concern, nodding and smiling to assure me that she's okay."
        if minami.is_visibly_pregnant:
            "Minami's dress could never hope to hide the fact that she's pregnant."
            "And I guess that's because she's more than proud to show off the fact."
            "She's crazily happy to be carrying my baby, and I feel the same way too!"
        if samantha.is_visibly_pregnant:
            "One thing's very different to the last time I saw Sam in a wedding dress."
            "And that's the fact that she's visibly pregnant."
            "But then I guess that, based on how her last marriage turned out, the difference can only be a good thing!"
        if lexi.is_visibly_pregnant:
            "It's a cliche for a trailer park girl to be sporting a swollen belly."
            "But somehow it just serves to make Lexi look all the more desirable, at least in my eyes."
            "She carries it so well that I just know she's going to make a wonderful mother."
    "There's barely enough time for the five of us to exchange glances and nervous smiles."
    "And that's because the priest leaps into the ceremony almost as soon as the music come to an end."
    show bree wedding normal
    show sasha wedding normal
    show minami wedding normal
    show samantha wedding normal
    show lexi wedding normal
    "Priest" "Dearly beloved..."
    "Priest" "We are gathered here today..."
    "Priest" "To join these SIX people in the bonds of holy matrimony!"
    "The priest's tone is a little exasperated, but more amused than anything."
    "And there's an appreciative ripple of laughter from the assembled guests too."
    show bree wedding flirt blush
    show minami wedding normal blush
    show samantha wedding flirt
    "Even the five of us share a round of giggles and laughter, some cheeks flushing too."
    "Sure, this is all legal now, but it's still pretty new for all concerned."
    "I guess this is just part of the journey to it becoming part of the new normal."
    "The priest dives into the task ahead, doing the best he can to keep up."
    "Before too long, we're already at the point where we're making our vows!"
    "Priest" "Do you, [bree.name], take Sasha, Sam, Minami, Lexi and [hero.name], to be your lawful, wedded partners?"
    show bree wedding happy -blush
    bree.say "Oh, I do!"
    "Priest" "Do you, Sasha, take [bree.name], Sam, Minami, Lexi and [hero.name], to be your lawful, wedded partners?"
    show sasha wedding happy
    sasha.say "Yeah, I do."
    "Priest" "Do you, Sam, take [bree.name], Sasha, Minami, Lexi and [hero.name], to be your lawful, wedded partners?"
    show samantha wedding happy
    samantha.say "I do."
    "Priest" "Do you, Minami, take [bree.name], Sasha, Sam, Lexi and [hero.name], to be your lawful, wedded partners?"
    show minami wedding happy
    minami.say "I sure do!"
    "Priest" "Do you, Lexi, take [bree.name], Sasha, Sam, Minami and [hero.name], to be your lawful, wedded partners?"
    show lexi wedding happy
    lexi.say "Hell yeah, I do!"
    "The priest makes a dramatic pause, filling his lungs for the final push."
    "Priest" "And do you, [hero.name], take [bree.name], Sasha, Sam, Minami and Lexi, to be your lawful, wedded partners?"
    "Now it's my turn to take an equally deep breath before answering."
    mike.say "I do."
    "The priest nods, clearly happy to be reaching the end of the ceremony."
    "Priest" "If anyone present knows of any lawful reason these six may not be joined in holy matrimony..."
    "Priest" "Let them speak now, or forever hold their peace!"
    "There's the usual pause and nervous laughter as he surveys the crowd."
    "I can't help feeling nervous as the seconds seem to stretch on."
    "Any moment I expect the doors to fly open to reveal [bree.name]'s dad, Scottie, Danny, Ryan or my own parents."
    "I can even imagine an unholy alliance of all six of them, united in their desire to derail our wedding!"
    "But nobody leaps to their feet to call a halt to the proceedings."
    "Priest" "The I hereby pronounce you husband and wives."
    "Priest" "You may kiss the brides."
    "Priest" "Or each other..."
    "Priest" "I'm not sure how this bit is supposed to work!"
    show sasha at center, traveling (1.2, 1.0, (1040, 800))
    show bree at center, traveling (1.2, 1.0, (640, 800))
    show minami at center, traveling (1.2, 1.0, (440, 800))
    show lexi at center, traveling (1.2, 1.0, (240, 800))
    show samantha at center, traveling (1.2, 1.0, (840, 800))
    "Neither are we, and so we come together in a kind of group hug."
    "We exchange kisses with each other, each one as passionate as the last."
    "And we did it - the six of us actually managed to tie the knot!"
    "We're not doing this behind closed doors anymore - we're a sixsome in the eyes of the law!"

    scene home ending
    show home ending sasha
    with fade
    sasha.say "Don't sweat it, guys."
    sasha.say "I've got this one."
    show home ending bree with dissolve
    bree.say "Huh - what does that mean?"
    sasha.say "Well, I was the first to move in with [hero.name]."
    sasha.say "That means I've known him the longest."
    bree.say "Ah...no way, Sasha!"
    bree.say "There's like a couple of days in it at the most."
    bree.say "And [hero.name] hit if off with me before you!"
    show home ending samantha with dissolve
    samantha.say "Are you two for real?"
    samantha.say "I was living with [hero.name] before you were even in the picture!"
    samantha.say "And he was hung up on me from the moment that I moved out too."
    show home ending minami with dissolve
    minami.say "Erm, hello - adorably spunky and cute little sister here!"
    minami.say "None of you guys have known big bro as long as I have."
    show home ending lexi with dissolve
    lexi.say "That's sweet, Minami."
    lexi.say "But did he rescue you from the clutches of a bad guy?"
    lexi.say "[hero.name] kicked that piece of shit's ass."
    lexi.say "And he did it all for me!"
    minami.say "Urgh..."
    minami.say "I've heard that story like a hundred times already!"
    samantha.say "Guys, guys..."
    samantha.say "This isn't getting us anywhere."
    samantha.say "We're supposed to be telling our side of the story."
    samantha.say "How we're all living happily ever after, yeah?"
    sasha.say "You're right, Sam."
    bree.say "Yeah, I guess so."
    minami.say "Sorry, Sam!"
    lexi.say "Okay, okay - but my story's still awesome."
    samantha.say "Ah, it's alright."
    samantha.say "I guess we're going to be on different pages sometimes."
    samantha.say "There are six of us involved in this relationship after all!"
    lexi.say "There's six of us for now!"

    if bree.is_visibly_pregnant and lexi.is_visibly_pregnant and minami.is_visibly_pregnant and samantha.is_visibly_pregnant and sasha.is_visibly_pregnant:
        bree.say "Are we still technically a sixsome?"
        sasha.say "Yeah, we might have accidentally become a tribe somewhere along the way!"
        sasha.say "[hero.name] could be the founder of a whole new nation."
        lexi.say "Ah...weird!"
        minami.say "No - that's sweet."
        minami.say "But please don't tell big bro that."
        samantha.say "I agree - his head's big enough as it is!"
    elif not bree.is_visibly_pregnant and not lexi.is_visibly_pregnant and not minami.is_visibly_pregnant and not samantha.is_visibly_pregnant and not sasha.is_visibly_pregnant:
        bree.say "Yeah, always room for more!"
        lexi.say "Squeeze a couple in there, huh?"
        minami.say "Erm...is someone else moving in?"
        sasha.say "She means the patter of tiny feet, Minami!"
        samantha.say "You know - babies?"
        minami.say "Oh..."
    else:
        if bree.is_visibly_pregnant:
            bree.say "Yeah - don't forget Poppy."
            bree.say "She's loud enough to count for two!"
        if minami.is_visibly_pregnant:
            minami.say "I sometimes forget that Mei's just my kid."
            minami.say "You guys are so good with her and she loves you all so much!"
        if sasha.is_visibly_pregnant:
            sasha.say "Dahlia's a tearaway, I know."
            sasha.say "But what do you expect from a kid with five moms!"

        if samantha.is_visibly_pregnant:
            samantha.say "Ha...Jemima's already got us all wrapped around her finger."
            samantha.say "I hate to think what she'll be like when she's older!"
        if lexi.is_visibly_pregnant:
            lexi.say "Chantel and Tyrone make it feel like there's four of them, let alone two!"
            lexi.say "Good job there are so many pairs of hands to throw in."

    bree.say "It would have been nice to be able to stay in the old house."
    bree.say "You know, where all of this got started?"
    sasha.say "Nah, it was getting cramped when there were only three of us!"
    samantha.say "That's why we ended up pooling our resources for a new place."
    minami.say "And I LOVE our place in the suburbs - it has everything!"
    lexi.say "I still think we should have bought a couple of trailers."
    lexi.say "We could have claimed most of the park where I was living..."
    minami.say "Oh, Lexi - don't start with that again!"
    samantha.say "Anyway, it doesn't matter where we're living."
    show home ending glasses with dissolve
    samantha.say "What matters is that we're all together."
    bree.say "Yeah, and that we outnumber [hero.name] five to one!"
    sasha.say "Poor guy - I almost feel sorry for him!"
    minami.say "Oh, don't be silly."
    minami.say "Big bro loves it really!"
    show home ending cum with vpunch
    pause 2.0
    scene bg black with dissolve
    $ game.set_new_game_plus()
    $ renpy.full_restart()
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
