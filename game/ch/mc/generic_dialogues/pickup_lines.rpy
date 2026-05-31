init -20:
    define male_good_pickup_lines = [
            [("mc", "You are absolutely, astoundingly gorgeous and that's the least interesting thing about you.")],
            [("mc", "Damn, that confidence looks sexy on you.")],
            [("mc", "I love seeing your smile, it brightens my day every time.")],
            [("mc", "I wish I could make you smile more often."),
                ("mc", "You're beautiful all the time, but when you smile, I swear my world stops.")],
            [("mc", "You look gorgeous today [girlname].")],
            [("mc", "Love is the jelly to sunshine's peanut butter."),
                ("mc", "And if I tell you that I'm in sandwich with you, I'm not just saying it to get in your Ziploc bag.")],
            [("mc", "Your smile is contagious.")],
            [("mc", "I bet you make babies smile.")],
            [("mc", "I like your style.")],
            [("mc", "You have the best laugh.")],
            [("mc", "You are the most perfect you there is.")],
            [("mc", "You're an awesome friend.")],
            [("mc", "You light up the room.")],
            [("mc", "Is that your picture next to 'charming' in the dictionary?")],
            [("mc", "On a scale from 1 to 10, you're an 11.")],
            [("mc", "You're even more beautiful on the inside than you are on the outside.")],
            [("mc", "Your eyes are breathtaking.")],
            [("mc", "If cartoon bluebirds were real, a bunch of them would be sitting on your shoulders singing right now.")],
            [("mc", "You're like sunshine on a rainy day.")],
            [("mc", "Your ability to recall random factoids at just the right time is impressive.")],
            [("mc", "How is it that you always look great, even in sweatpants?")],
            [("mc", "That color is perfect on you.")],
            [("mc", "Being around you makes everything better!")],
            [("mc", "You're better than a triple-scoop ice cream cone. With sprinkles.")],
            [("mc", "Your bellybutton is kind of adorable.")],
            [("mc", "Your hair looks stunning.")],
            [("mc", "You're one of a kind!")],
            [("mc", "You should be thanked more often. So thank you!!")],
            [("mc", "You're more fun than bubble wrap.")],
            [("mc", "Who raised you? They deserve a medal for a job well done.")],
            [("mc", "You're irresistible when you blush.")],
            [("mc", "Somehow you make time stop and fly at the same time.")],
            [("mc", "There's ordinary, and then there's you.")],
            [("mc", "You're really something special.")],
            [("mc", "You take so much care of yourself to look beautiful. That's what I love about you.")],
            [("mc", "With that smile of yours, you give me the confidence to make possible the seemingly impossible stuff.")],
            [("mc", "That shirt looks damn pretty on you.")],
            [("mc", "You look gorgeous today.")],
            [("mc", "How do you be at your best every day?")],
            [("mc", "You spoke smartly thorough the debate.")],
            [("mc", "I can hardly take my eyes off you, believe me you have beautiful eyes.")],
            [("mc", "That was so nice of you to help him.")],
            [("mc", "I know it might have been so difficult for you, but I'm impressed with the way you handled it.")],
            [("mc", "Hey, you are the girl with the cute smile!")],
            [("mc", "How did you do that? That looks awesome.")],
            [("mc", "That color looks perfect on you.")],
            [("mc", "I am so lucky to have you beside me.")],
            [("mc", "Each time I'm with you, you make me feel so special.")],
            [("mc", "You look beautiful, as always.")],
            [("mc", "I love your fragrance.")],
            [("mc", "You're good looking, you got a beautiful body, beautiful legs, beautiful face, all these guys in love with you."),
                ("mc", "Only you've got a look in your eye like you haven't been fucked in a year.")],
            [("mc", "You make me want to be a better man.")],
            [("mc", "I used to live like Robinson Crusoe, shipwrecked among eight million people. But one day I saw a footprint in the sand and there you were.")],
            [("mc", "The thing is, um, what I'm trying to say, very inarticulately, is that, um, in fact, perhaps despite appearances, I like you, very much. Just as you are.")],
            [("mc", "I know what I want, because I have it in my hands right now. You.")],
            [("mc", "I couldn't help but notice that you look a lot like my next girlfriend.")],
            ]

    define male_nerdy_pickup_lines = [
        [("mc", "Wow, you look like Xena the Warrior Princess!\nWanna date?")],
        [("mc", "Your eyes are like limpid pools of primordial ooze, and I am the protozoa that wish to swim in their depths.")],
        [("mc", "I'm Batman.")],
        [("mc", "I didn't expect the Spanish Inquisition...\nIn my pants.")],
        [("mc", "I'm no Fred Flintstone, but I bet I can make your bed rock.")],
        [("mc", "You could survive a Zombie apocalypse.")],
        [("mc", "Hey pretty lady, I know Klingon, and tonight I'm going to Klingon to you!")]
        ]

    define male_bad_pickup_lines = [
        [("mc", "You look like an angel that fell from heaven and hit its face on the pavement.")],
        [("mc", "Have you ever seen a 2-incher?")],
        [("mc", "Hey baby, want to socialize our means of reproduction?")],
        [("mc", "Burger King isn't the only thing that is king-sized...")],
        [("mc", "Dammit, I creamed my trousers again!")],
        [("mc", "Secret Service, ma'am.\nI need to do a full body cavity search. National security, you know.")],
        [("mc", "If I had a dime for every time I tried to pick up a chick, I'd still be poor.")],
        [("mc", "If I flip a coin, what are my chances of getting head")],
        [("mc", "You look like my next wife. I don't know though, I've never been married.")],
        [("mc", "I'm good at algebra; I can replace your X and you wouldn't need to figure out Y.")],
        [("mc", "You look like trash! Let me take you out.")],
        [("mc", "Are you an antique collector? Because I have some junk that hasn't been touched in years.")],
        [("mc", "Do you like magic? Because after we have sex I will disappear.")],
        ]

label good_pickup_lines_male(npc_is_male=False):
    $ lines = male_good_pickup_lines
    if hero.has_skill("video_games"):
        $ lines += male_nerdy_pickup_lines
    return lines

label bad_pickup_lines_male(npc_is_male=False):
    return male_bad_pickup_lines
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
