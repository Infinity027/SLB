label palla_ask_phone_female:
    bree.say "Can I have your number?"
    if palla.love < 10 or not hero.charm >= 40 - palla.love:
        if palla.flags.storeanal:
            palla.say "After what you did? I don't think I like you that much."
        else:
            palla.say "Not a chance!"
    else:
        $ hero.smartphone_contacts.append("palla")
        palla.say "I guess."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
