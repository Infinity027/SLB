label emma_talk_love_female:
    bree.say "Did I hear [mike.name] right, Emma?"
    bree.say "He told me that he saw you in a dream!"
    bree.say "That's like a fairy tale or something."
    bree.say "Like you meeting was because of true love!"
    emma.say "Oh, [hero.name]...I don't know about that!"
    emma.say "I think [mike.name] might have been exaggerating a little!"
    emma.say "But it's sweet of him, because I do believe in true love."
    $ emma.love += 1
    return

label emma_talk_sex_female:
    bree.say "I don't want to sound like a crazy nympho, Emma."
    bree.say "But I feel like I've got an itch to scratch, you know?"
    bree.say "Like it's been a long time since I..."
    emma.say "Whoa...hold on there, [hero.name]!"
    emma.say "I get the picture, okay?"
    emma.say "And I'll let you into a little secret too..."
    emma.say "I get the same way some times!"
    $ emma.love += 1
    return

label emma_talk_politics_female:
    bree.say "Young people are so apathetic, Emma."
    bree.say "Nobody's engaged with political issues."
    bree.say "And that sucks!"
    emma.say "Can you really blame them, [hero.name]?"
    emma.say "Politicians talk all the time and don't get anything done!"
    emma.say "The only thing they care about is convincing kids to vote for them!"
    $ emma.love -= 1
    return

label emma_talk_food_female:
    bree.say "Ooh...my stomach's rumbling!"
    bree.say "That means I need a snack!"
    bree.say "You want anything, Emma?"
    emma.say "No, [hero.name]...I'm fine."
    emma.say "I don't make a habit of eating between meals."
    emma.say "I just never seem to have the appetite for it."
    return

label emma_talk_travels_female:
    bree.say "Hmm...will you look at the places in this travel brochure, Emma!"
    bree.say "It's like a dream that can never come true!"
    emma.say "Oh wow!"
    emma.say "That looks like paradise!"
    bree.say "I know - I so wanna go travelling!"
    emma.say "Me too, [hero.name]!"
    emma.say "I've been saving up like forever!"
    $ emma.love += 1
    return

label emma_talk_tv_female:
    emma.say "What's up, [hero.name]?"
    emma.say "You look like your head's somewhere else!"
    bree.say "Oh, sorry, Emma!"
    bree.say "I was just thinking about a TV show I'm binging."
    bree.say "You know what that's like, yeah?"
    emma.say "Hmm...no, not really."
    emma.say "I don't watch too much TV."
    return

label emma_talk_sports_female:
    bree.say "There's some big sports event happening in the city this weekend, Emma."
    bree.say "Looks like they're going to be closing roads and all sorts of stuff!"
    bree.say "That kind of sucks!"
    if emma.sexperience < 3:
        emma.say "Urgh...that's SO typical!"
        emma.say "Why does the world have to fit around sports?!?"
        emma.say "I had plans in the city this weekend!"
        $ emma.love -= 1
    else:
        emma.say "So long as it doesn't affect me!"
        emma.say "Let the dumb sports fans have their dumb sports."
    return

label emma_talk_fashion_female:
    bree.say "I think I need to go on a shopping spree, Emma."
    bree.say "My wardrobe's starting to look as out of fashion as [mike.name]'s!"
    bree.say "And that can't be good."
    emma.say "You always look fine to me, [hero.name]."
    emma.say "But then I really don't get fashions."
    emma.say "They change so often that I can't keep up!"
    $ emma.sub += 1
    return

label emma_talk_books_female:
    emma.say "What's that you're reading, [hero.name]?"
    bree.say "Oh...hey, Emma!"
    bree.say "It's a pretty sweet sci-fi novel."
    bree.say "In fact, I've almost finished it."
    bree.say "You want to borrow it?"
    emma.say "Oh no, [hero.name]...I was just asking to be polite!"
    emma.say "I'm not really the reading type."
    return

label emma_talk_people_female:
    bree.say "It's great to have the chance to know you, Emma."
    bree.say "I feel like I don't get to meet many new people these days."
    bree.say "And I don't want to end up a lock-in!"
    emma.say "You're very different to me, [hero.name]."
    emma.say "I can't stand the thought of meeting loads of new people."
    emma.say "In fact, just thinking about it makes me feel anxious."
    emma.say "It's like I'm going to have a panic attack!"
    return

label emma_talk_computers_female:
    emma.say "Oh, I like your laptop, [hero.name]!"
    emma.say "You seem to really know your stuff!"
    bree.say "Yeah, Emma - I'm a bit of a computer geek!"
    emma.say "Me too!"
    emma.say "I have to keep up with the latest developments."
    emma.say "I hate to think I might miss something important!"
    $ emma.love += 1
    return

label emma_talk_music_female:
    bree.say "You want to put some music on, Emma?"
    bree.say "It's pretty quiet in here."
    bree.say "We could liven things up a bit!"
    emma.say "Oh, don't ask me to choose, [hero.name]!"
    emma.say "I have NO clue where to start."
    emma.say "I think I'm tone deaf when it comes to music!"
    $ emma.sub += 1
    return

label emma_talk_birthday_female:
    bree.say "Happy Birthday, Emma!"
    bree.say "Hope it's a good one!"
    emma.say "Oh, [hero.name]..."
    emma.say "I'm so touched that you remembered!"
    emma.say "It really means a lot to me."
    $ emma.love += 5
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
