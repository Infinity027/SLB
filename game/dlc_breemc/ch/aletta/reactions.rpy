label aletta_ask_birthday_female:
    bree.say "When's your birthday, Aletta?"
    bree.say "I don't think you told me yet."
    if aletta.love >= 50:
        show aletta happy
        $ aletta.flags.birthdayknown = True
        aletta.say "Oh..."
        aletta.say "It's Winter 14..."
        aletta.say "Thank you for asking, [hero.name]!"
        $ aletta.love += 1
    else:
        show aletta annoyed
        $ aletta.love -= 1
        aletta.say "Don't mention my birthday, [hero.name]!"
        aletta.say "All that does is remind me how old I am."
        aletta.say "That and how much more I wanted to have achieved by now!"
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
