init -20:
    define female_good_pickup_lines = [
            [("mc", "I hear you're good at algebra..."),
                ("mc", "..Will you replace my eX without asking Y?")],
            [("mc", "Do you sleep on your stomach?"),
                ("npc", "No..."),
                ("mc", "Can I?")],
            [("mc", "Do you know what'd look good on you?"),
                ("npc", "No."),
                ("mc", "Me.")],
            [("mc", "Hi, did your license get suspended for driving all these girls crazy?")],
            [("mc", "I don't need a spoonful of sugar to swallow you.")],
            [("mc", "Today I'd like to name a multiple orgasm after you.")],
            [("mc", "Hey baby...I can suck a golf ball thru 50 feet of garden hose.")],
            [("mc", "They're called 'eyebrows' cus my eyes are browsin your fine ass.")],
            [("mc", "I'd like to point out that 'beautiful' has U in it."),
                ("mc", "But, 'quickie' has U & I together.")],
            [("mc", "I'm trying to quit smoking, wanna give me a new oral fixation?")],
            [("mc", "Baby you be the tree, and I'll wrap around you like a koala bear.")],
            [("mc", "I'm not drunk, I'm just intoxicated by you.")],
            [("mc", "Is your name Google? Because you have everything I've been searching for.")],
            [("mc", "You don't need car keys to drive me crazy.")],
            [("mc", "I want you with all my butt, I would say heart, but my butt is bigger.")],
            [("mc", "I'm wearing Revlon Colorstay Lipstick, want to help me test the claim that it won't kiss off?")],
            [("mc", "Hey baby...I can suck the chrome off a trailer hitch.")],
            [("mc", "You're so hot ; a firefighter couldn't put you out.")],
            [("mc", "I make the best milkshakes...")],
            [("mc", "You want to melt in my mouth or in my hand?")],
            [("mc", "Nice package let me help unwrap that!")],
            [("game", "[girlname] touches my shirt."),
                ("npc", "Is this cotton?"),
                ("mc", "No."),
                ("game", "He touch down in my crotch area."),
                ("npc", "Oh, this must be felt.")],
            [("game","I put a dollar bill on my head..."),
                ("npc", "Why are you doing that?"),
                ("mc", "Its all you can eat for under a dollar.")],
            ]
    define female_good_pickup_lines_for_male = [
            [("mc", "Were you in Boy Scouts?"),
                ("mc", "Because you sure have tied my heart in a knot.")],
            [("mc", "Boy is your name homework?"),
                ("npc", "No."),
                ("mc", "Because I'm not doing you and I should be.")],
            [("mc", "My beaver is bored and wants to play, do you have any wood for my beaver?")],
            [("mc", "Hi, i'm wasted but this condom in my pocket doesn't have to be.")],
            [("mc", "Are you a trampoline cuz I wanna bounce on you?")],
            [("mc", "What's a nice guy like you doing with a body like that?")],
            [("mc", "Aren't you the guy who gets fan mail from Ron Jeremy?")],
            [("mc", "Are you a burger cuz you can be the meat between my buns")],
            [("mc", "I know you think I'm sexy, I know you think im fine, but just like all the other guys get a number and wait in line")],
            [("mc", "I could hear your cock talking and it just told me to blow you.... a kiss!")],
            [("mc", "Hey, you look like a big strong guy. You think you could handle my pussy or is it too much for you?")],
            [("mc", "You remind me of a Twinkie."),
                 ("npc", "Why?"),
                 ("mc", "Every time I bite into you, you cream in my mouth.")],
            ]

    define female_nerdy_pickup_lines = [
        [("mc", "I'm Batgirl.")],
        [("mc", "I'm no Wilma Flintstone, but I bet I can make your bed rock.")],
        [("mc", "You could survive a Zombie apocalypse.")],
        ]
    define female_nerdy_pickup_lines_for_male = [
        [("mc", "Wow, you look like Conan the Barbarian!\nWanna date?")],
        [("mc", "I didn't expect the Spanish Inquisition...\nIn your pants.")],
        ]

    define female_bad_pickup_lines = [
        [("mc", "Hey baby, want to socialize our means of reproduction?")],
        [("mc", "I am in for a king-sized meat bun...")],
        [("mc", "If I had a dime for every time a guy tried to pick me up, I'd still be poor.")],
        ]
    define female_bad_pickup_lines_for_male = [
        [("mc", "You look like Hercules's retarded cousin.")],
        [("mc", "Can you show me your 2-incher?")],
        ]

label good_pickup_lines_female(npc_is_male=True):
    $ lines = female_good_pickup_lines
    if npc_is_male:
        $ lines += female_good_pickup_lines_for_male
    if hero.has_skill("video_games"):
        $ lines += female_nerdy_pickup_lines
        if npc_is_male:
            $ lines += female_nerdy_pickup_lines_for_male
    return lines

label bad_pickup_lines_female(npc_is_male=True):
    $ lines = female_bad_pickup_lines
    if npc_is_male:
        $ lines += female_bad_pickup_lines_for_male
    return lines
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
