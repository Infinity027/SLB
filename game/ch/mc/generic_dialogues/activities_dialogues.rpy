label say_sentence_male(sentence):
    if sentence.endswith((".", "?", "!")):
        mike.say "[sentence]"
    else:
        mike.say "[sentence]."
    return

label text_sentence_male(sentence):
    if sentence.endswith((".", "?", "!")):
        mchero_nvl "[sentence]"
    else:
        mchero_nvl "[sentence]."
    return

label apologize_dialogues_1_male:
    mike.say "I'm sorry, I made a mistake..."
    mike.say "I really want us to give it a second chance..."
    return

label ask_birthday_dialogues_1_male:
    mike.say "Hey [active_girl.name], when is your birthday?"
    return

label ask_birthday_dialogues_2_male:
    mike.say "Maybe..."
    return

label ask_number_dialogues_1_male:
    mike.say "Can I have your number?"
    return

label break_up_dialogues_1_male:
    mike.say "I think we should break up."
    return

label break_up_dialogues_2_male:
    mike.say "I'm sorry [active_girl.name], but I'm not interested in you romantically..."
    return

label break_up_dialogues_3_male:
    mike.say "I hope we can stay friends."
    return

label break_up_dialogues_4_male:
    mike.say "I want us to be just friends, nothing more."
    mike.say "I wanted that to be clear."
    return

label friendzone_dialogues_1_male:
    mike.say "I'm sorry [active_girl.name], but I'm not interested in you romantically..."
    $ renpy.show(f"{active_girl.id} sad")
    mike.say "I hope we can stay friends."
    return

label friendzone_dialogues_2_male:
    mike.say "I want us to be just friends, nothing more."
    mike.say "I wanted that to be clear."
    return

label cinema_with_dialogues_1_male:
    mike.say "[active_girl.name], do you want to go watch a movie together?"
    return

label dance_with_dialogues_1_male:
    mike.say "[active_girl.name], do you want to dance?"
    return

label cancel_date_internal_dialogues_1_male:
    mike.say "About our date..."
    mike.say "I won't be able to make it."
    return

label date_her_internal_dialogues_1_male:
    mike.say "[active_girl.name], would you like to go on a date with me?"
    return

label go_steady_dialogues_1_male:
    mike.say "I'd like for us to be an official couple and 'go steady', as they say."
    return

label ask_for_a_job_dialogues_1_male:
    mike.say "I saw the sign saying that you're recruiting and I'd like to apply."
    return

label quit_a_job_dialogues_1_male:
    mike.say "I wanna quit my job!"
    return

label kart_with_dialogues_1_male:
    mike.say "[active_girl.name], do you want to race me on the track?"
    return

label offer_a_drink_dialogues_1_male:
    mike.say "[active_girl.name], would you like a drink?"
    return

label play_with_dialogues_1_male:
    mike.say "[active_girl.name], do you want to play a game?"
    return

label shop_with_dialogues_1_male:
    mike.say "[active_girl.name], do you want to go shopping?"
    return

label sleep_nightmare_dialogues_1_male:
    mike.say "WAAAH!"
    return

label smartphone_booty_call_dialogues_1_male:
    mike.say "Wanna come over for a little fun?"
    return

label smartphone_call_dialogues_1_male:
    mike.say "Where are you?"
    return

label smartphone_call_dialogues_2_male:
    mike.say "Could you come where I am?"
    return

label study_with_dialogues_1_male:
    mike.say "[active_girl.name], do you want some help?"
    return

label sweet_talk_dialogues_1_male:
    "I can't find anything smooth to say..."
    "Maybe I should work on my pickup lines..."
    return

label sweet_talk_dialogues_2_male:
    "Fuck that was stupid to say, she must be so pissed off..."
    "Maybe I should work on my pickup lines..."
    return

label train_with_dialogues_1_male:
    mike.say "[active_girl.name] do you want to work out together?"
    return

label watch_tv_with_dialogues_1_male:
    mike.say "Let's watch a movie together."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
