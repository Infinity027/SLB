label smartphone_booty_call(girl):
    $ smartphone_girl.object = girl
    $ DONE[f"smartphone_booty_call_{girl.id}"] = game.days_played
    if girl.flags.schedule in ['jail', 'hospital']:
        "I call [girl.name]."
        "No answer."
    else:
        if renpy.has_label(f"{girl.id}_smartphone_booty_call_{hero.gender}"):
            call expression f"{girl.id}_smartphone_booty_call_{hero.gender}" from _call_expression_120
        else:
            call expression f"smartphone_booty_call_dialogues_1_{hero.gender}" from _call_expression_139

            if ((girl.love >= 150 and girl.sub >= 25 and girl.sexperience >= 1) or (girl.id == "reona" and Person.find("reona").purity < 50)) and renpy.has_label(f"{girl.id}_fuck_date_{hero.gender}"):
                smartphone_girl.say "Sure."
                call expression f"{girl.id}_fuck_date_{hero.gender}" from _call_expression_135
            else:
                smartphone_girl.say "No fucking way!"
                $ girl.love -= 1
                $ girl.sub -= 1
    return

label smartphone_send_friendly_text(girl):
    $ nvl_mode = "phone"
    nvl clear
    $ smartphone_girl.object = girl
    $ DONE[f"smartphone_send_friendly_text_{girl.id}"] = game.days_played
    if girl.flags.schedule == 'jail':
        "I send [girl.name] a message."
        "..."
        "[girl.subject_pronoun.capitalize()] doesn't answer..."
    else:
        if renpy.has_label(f"{smartphone_girl.id}_friendly_texts_{hero.gender}") and randint(0, 2) >= 1:
            call expression f"{smartphone_girl.id}_friendly_texts_{hero.gender}" from _call_expression_140
        else:
            $ renpy.dynamic("text_list", "text_index", "text_line")
            $ text_list = list(enumerate(randchoice(mc_friendly_texts)))
            while text_list:
                $ text_index, text_line = text_list.pop(0)
                if text_line[0] == "mc":
                    call expression f"text_sentence_{hero.gender}" pass (sentence=text_line[1]) from _call_expression_152
                else:
                    call expression f"text_sentence_{smartphone_girl.id}" pass (sentence=text_line[1]) from _call_expression_494
                if text_index == 0:
                    if girl.activity_name == "sleep" and girl.love < 70:
                        call expression f"text_sentence_{smartphone_girl.id}" pass (sentence="Leave me alone, I was asleep...") from _call_expression_495
                        $ girl.love -= 2
                        $ renpy.hide(girl.id)
                        $ girl.set_flag("interact", 1, 1, "+")
                        $ renpy.show_screen("smartphone", char=girl, selected_screen="text")
                        return
            if persistent.difficulty >= 0:
                if girl.love <= 50:
                    $ girl.love += 1
            else:
                $ girl.love += 1
            $ hero.fun += 0.2
        $ renpy.hide(girl.id)
        $ girl.set_flag("interact", 1, 1, "+")
        $ renpy.show_screen("smartphone", char=girl, selected_screen="text")
    $ nvl_mode = None
    return

label smartphone_send_flirty_text(girl):
    $ nvl_mode = "phone"
    nvl clear
    $ smartphone_girl.object = girl
    $ DONE[f"smartphone_send_flirty_text_{girl.id}"] = game.days_played
    if girl.flags.schedule == 'jail':
        "I send [girl.name] a message."
        "..."
        "[girl.subject_pronoun.capitalize()] doesn't answer..."
    else:
        if renpy.has_label(f"{smartphone_girl.id}_flirty_texts_{hero.gender}") and randint(0, 2) >= 1:
            call expression f"{smartphone_girl.id}_flirty_texts_{hero.gender}" from _call_expression_153
        else:
            $ renpy.dynamic("text_list", "text_index", "text_line")
            $ text_list = list(enumerate(randchoice(mc_flirty_texts)))
            while text_list:
                $ text_index, text_line = text_list.pop(0)
                if text_line[0] == "mc":
                    call expression f"text_sentence_{hero.gender}" pass (sentence=text_line[1]) from _call_expression_155
                else:
                    call expression f"text_sentence_{smartphone_girl.id}" pass (sentence=text_line[1]) from _call_expression_496
                if text_index == 0:
                    if girl.activity_name == "sleep" and girl.love < 140:
                        call expression f"text_sentence_{smartphone_girl.id}" pass (sentence="Leave me alone, I was asleep...") from _call_expression_497
                        $ girl.love -= 2
                        $ renpy.hide(girl.id)
                        $ girl.set_flag("interact", 1, 1, "+")
                        $ renpy.show_screen("smartphone", char=girl, selected_screen="text")
                        return
            if (girl.love <= 80 or girl.sexperience == 0) and not hero.charm >= 30:
                call expression f"text_sentence_{smartphone_girl.id}" pass (sentence="Don't send me that kind of text, it's inappropriate.") from _call_expression_498
                $ girl.love -= 1
            elif girl.sexperience == 0 or (girl.love <= 100 and not hero.charm >= 50):
                call expression f"text_sentence_{smartphone_girl.id}" pass (sentence="Stop joking around ;)") from _call_expression_499
                $ girl.love += 1
            else:
                call expression f"text_sentence_{smartphone_girl.id}" pass (sentence="You make me blush :$") from _call_expression_500
                if persistent.difficulty >= 0:
                    if girl.love <= 100:
                        $ girl.love += 1
                else:
                    $ girl.love += 1
            $ hero.fun += 0.3
        $ renpy.hide(girl.id)
        $ girl.set_flag("interact", 1, 1, "+")
        $ renpy.show_screen("smartphone", char=girl, selected_screen="text")
    $ nvl_mode = None
    return

label smartphone_send_dirty_text(girl):
    $ nvl_mode = "phone"
    nvl clear
    $ smartphone_girl.object = girl
    $ DONE[f"smartphone_send_dirty_text_{girl.id}"] = game.days_played
    if girl.flags.schedule == 'jail':
        "I send [girl.name] a message."
        "..."
        "She's doesn't answer..."
    else:
        if renpy.has_label(f"{smartphone_girl.id}_dirty_texts_{hero.gender}") and randint(0, 2) >= 1:
            call expression f"{smartphone_girl.id}_dirty_texts_{hero.gender}" from _call_expression_158
        else:
            $ renpy.dynamic("text_list", "text_index", "text_line")
            $ text_list = list(enumerate(randchoice(mc_dirty_texts)))
            while text_list:
                $ text_index, text_line = text_list.pop(0)
                if text_line[0] == "mc":
                    call expression f"text_sentence_{hero.gender}" pass (sentence=text_line[1]) from _call_expression_162
                else:
                    call expression f"text_sentence_{smartphone_girl.id}" pass (sentence=text_line[1]) from _call_expression_501
                if text_index == 0:
                    if girl.activity_name == "sleep" and girl.love < 140:
                        call expression f"text_sentence_{smartphone_girl.id}" pass (sentence="Leave me alone, I was asleep...") from _call_expression_502
                        $ girl.love -= 2
                        $ renpy.hide(girl.id)
                        $ girl.set_flag("interact", 1, 1, "+")
                        $ renpy.show_screen("smartphone", char=girl, selected_screen="text")
                        return
            if girl.love <= 100 and not hero.charm >= 40:
                call expression f"text_sentence_{smartphone_girl.id}" pass (sentence="Don't send me that kind of text, it's inappropriate.") from _call_expression_503
                $ girl.love -= 2
            elif girl.sexperience < 2 or girl.love <= 150:
                call expression f"text_sentence_{smartphone_girl.id}" pass (sentence="OK, I am horny now, what will you do about it? :*") from _call_expression_504
                $ girl.love += 2
            else:
                call expression f"text_sentence_{smartphone_girl.id}" pass (sentence="You make me so wet :$") from _call_expression_505
                if persistent.difficulty >= 0:
                    if girl.love <= 150:
                        $ girl.love += 2
                    elif girl.love <= 175:
                        $ girl.love += 1
                else:
                    $ girl.love += 2
            $ hero.fun += 0.2
        $ renpy.hide(girl.id)
        $ girl.set_flag("interact", 1, 1, "+")
        $ renpy.show_screen("smartphone", char=girl, selected_screen="text")
    $ nvl_mode = None
    return

label smartphone_call(girl):
    $ smartphone_girl.object = girl
    $ DONE[f"smartphone_call_{girl.id}"] = game.days_played
    $ old_active_girl = active_girl.object
    $ active_girl.object = girl
    $ prior_activity = hero.activity
    $ hero.activity = "call_girl"

    $ renpy.dynamic("valid_events")
    $ valid_events = CallEvent.valid_events()
    if valid_events:
        call event_do (valid_events.pop(0)) from _call_event_do
    else:
        "I call [girl.name]."
        if girl.flags.schedule == 'jail':
            "No answer."
        elif (not randint(1, 100) <= girl.love and not hero.charm >= 40) or girl.activity_name == "sleep" or girl.hidden:
            "[girl.subject_pronoun.capitalize()] doesn't pick up."
        else:
            smartphone_girl.say "Yes?"
            $ choices = [("Chat", 1), ("Ask location", 2)]
            $ dates = hero.calendar.find(girl=girl.id, date_only=True)
            if not game.active_date and game.room not in ["map", "housemap", "mallmap"] and girl.flags.schedule != 'hospital' and girl.love >= 50 and Room.find(game.room).hours[1] > game.hour:
                $ choices.append(("Ask to join you", 3))
            if not dates:
                if smartphone_girl.love >= 20 and not smartphone_girl.flags.breakup and not smartphone_girl.flags.noproposedate and girl.flags.schedule != 'hospital':
                    $ choices.append(("Ask on a date", 4))
            else:
                $ choices.append(("Cancel date", 5))
            $ result = renpy.display_menu(choices)
            if result == 1:
                call expression girl.get_chat from _call_expression_57
            elif result == 2:
                call expression f"smartphone_call_dialogues_1_{hero.gender}" from _call_expression_163
                $ smart_room = girl.room
                if smart_room != "None":
                    if girl.love >= 40:
                        if smart_room in ["amusementpark"]:
                            smartphone_girl.say "I am at the amusement park."
                        elif smart_room in ["apartmentbuilding", "house", "bedroom1", "bedroom2", "bedroom3", "bedroom4", "bedroom5", "bedroom6", "bathroom", "kitchen", "pool", "livingroom", "secondfloor", "attic"]:
                            smartphone_girl.say "I am at home."
                        elif smart_room in ["map", "alley", "street", "street2"]:
                            smartphone_girl.say "I am in the city."
                        elif smart_room in ["bookstore", "bakery", "clothesshop", "arcade", "flowershop", "mall1", "publicpool", "jewelrystore", "mall2", "tattooshop", "electronic", "drugstore", "coffeeshop"]:
                            smartphone_girl.say "I am at the mall."
                        elif smart_room in ["beach"]:
                            smartphone_girl.say "I am at the beach."
                        elif smart_room in ["waterpark", "waterpark2"]:
                            smartphone_girl.say "I am at the waterpark."
                        elif smart_room in ["cinema"]:
                            smartphone_girl.say "I am at the cinema."
                        elif smart_room in ["familyrestaurant", "restaurant"]:
                            smartphone_girl.say "I am at the restaurant."
                        elif smart_room in ["hospital", "hospitalroom"]:
                            smartphone_girl.say "I am at the hospital."
                        elif smart_room in ["gym", "gymreception", "gymmachine", "gymlockers","mma"]:
                            smartphone_girl.say "I am at the gym."
                        elif smart_room in ["lounge"]:
                            smartphone_girl.say "I am at the lounge."
                        elif smart_room in ["office", "personal", "breakroom", "alettaoffice", "ceo"]:
                            smartphone_girl.say "I am at work."
                        elif smart_room in ["onsen"]:
                            smartphone_girl.say "I am on a little trip."
                        elif smart_room in ["park", "pond"]:
                            smartphone_girl.say "I am at the park."
                        elif smart_room in ["station"]:
                            smartphone_girl.say "I am at the train station."
                        elif smart_room in ["stripclub"]:
                            smartphone_girl.say "I am at the strip club."
                        elif smart_room in ["sexshop"]:
                            smartphone_girl.say "I am at the sex shop."
                        elif smart_room in ["university", "classroom", "library"]:
                            smartphone_girl.say "I am at the university."
                        elif smart_room in ["pub", "pubexterior", "pubplay", "pubseat"]:
                            smartphone_girl.say "I am at the pub."
                        elif smart_room in ["nightclub", "nightclubbar", "vip"]:
                            smartphone_girl.say "I am at the nightclub."
                        elif smart_room in ["church"]:
                            smartphone_girl.say "I am at the church."
                        elif smart_room in ["punkbar"]:
                            smartphone_girl.say "I am at the punk bar downtown."
                        elif smart_room in ["policestation", "jail"]:
                            smartphone_girl.say "I am at the police station."
                        elif smart_room in ["kart"]:
                            smartphone_girl.say "I am at the kart track."
                        elif smart_room in ["studio"]:
                            smartphone_girl.say "I am practicing the studio."
                        elif smart_room in ["maidcafe"]:
                            smartphone_girl.say "I am at the maid cafe."
                        elif smart_room in ["garage"]:
                            smartphone_girl.say "I am at the garage."
                        elif smart_room in ["forest"]:
                            smartphone_girl.say "I am in the forest."
                        elif smart_room in ["cemetery"]:
                            smartphone_girl.say "I am at the cemetery."
                        elif smart_room in ["aquarium"]:
                            smartphone_girl.say "I am at the aquarium."
                        else:
                            smartphone_girl.say "I think I'm a little lost."
                    else:
                        smartphone_girl.say "I am quite sure this is not your problem."
                else:
                    smartphone_girl.say "Try to guess."
            elif result == 3:
                call expression f"smartphone_call_dialogues_2_{hero.gender}" from _call_expression_178
                if girl.status == "mistress":
                    smartphone_girl.say "Not a chance. You do the travel, not I!"
                elif girl.activity_name == "work" and (girl.status in ["sex slave", "pet"] or girl.sub < 75):
                    smartphone_girl.say "Sorry but I'm currently working..."
                else:
                    $ room_travel_time = Room.find(game.room)._travel_time
                    if room_travel_time > 0:
                        smartphone_girl.say "Alright! Wait for me, I'll be there in [room_travel_time] hour['s' if room_travel_time > 1 else '']."
                    else:
                        smartphone_girl.say "Alright! I come right away."
                    $ girl.flags.forceLocation = (game.days_played, game.hour + room_travel_time, game.room)
                    $ game.pass_time(0)
            elif result == 4:
                $ active_girl.object = girl
                call date_her_internal (True) from _date_her_smartphone
                $ active_girl.object = girl
            elif result == 5:
                $ active_girl.object = girl
                call cancel_date_internal from _cancel_date_smartphone
            $ girl.set_flag("interact", 1, 1, "+")
    $ active_girl.object = old_active_girl
    $ hero.activity = prior_activity
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
