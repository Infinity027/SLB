label girl_interact(ig):
    $ interact_girl.object = ig
    $ _return = interact_girl
    $ active_girl.object = interact_girl
    $ hero.activity = Activity.find("interact")
    scene expression f"bg {game.room}"
    if renpy.has_label(f"{interact_girl.id}_greet"):
        call expression interact_girl.id + "_greet" from _call_expression_105


    $ cache_date_girl = date_girl.object
    $ cache_active_girl = active_girl.object
    $ cache_smartphone_girl = smartphone_girl.object

    $ event_triggered = False

    $ renpy.dynamic("valid_events")
    $ valid_events = InteractEvent.valid_events()

    while valid_events:
        $ event = valid_events.pop(0)
        $ event_triggered = True
        call event_do (event) from _call_event_do_2
        if (date_girl.object and date_girl.object != cache_date_girl) or (active_girl.object and active_girl.object != cache_active_girl) or (smartphone_girl.object and smartphone_girl.object != cache_smartphone_girl) or (event.quit):
            $ valid_events = []

    if event_triggered:
        $ active_girl.object = None
        $ hero.activity = None
        $ renpy.hide(interact_girl.id)
        return
    else:

        while True:
            $ active_girl.object = interact_girl
            $ bye_outfit = interact_girl.get_clothes()
            scene expression f"bg {game.room}"
            if persistent.new_ui:
                $ renpy.show(interact_girl.id, at_list=[npc_info_npc])
            else:
                $ renpy.show(interact_girl.id)
            call screen interact(interact_girl)

            if isinstance(_return, BaseActivity):
                call activity_do (_return) from _call_activity_do
                if _return == "end_event":
                    $ active_girl.object = None
                    $ hero.activity = None
                    $ renpy.hide(interact_girl.id)
                    return
            else:
                $ active_girl.object = None
                $ hero.activity = None
                $ renpy.hide(interact_girl.id)
                return

            if interact_girl.room != game.room:
                if randint(0, (interact_girl.love + 1) // 10) != 0:
                    if renpy.has_label(interact_girl.id + "_bye"):
                        call expression interact_girl.id + "_bye" pass (bye_outfit=bye_outfit) from _call_expression_106
                $ active_girl.object = None
                $ hero.activity = None
                $ renpy.hide(interact_girl.id)
                return

            if not Room.find(game.room).test():
                $ active_girl.object = None
                $ hero.activity = None
                $ renpy.hide(interact_girl.id)
                return

            if bool(game.active_date) and game.hour in (0, 18, 24, 4):
                $ active_girl.object = None
                $ hero.activity = None
                $ renpy.hide(interact_girl.id)
                return

label loose_trait(person, trait):
    python:
        person = Person.find(person)
        if person is not None:
            person.traits -= trait
    return

label gain_trait(person, trait):
    python:
        person = Person.find(person)
        if person is not None:
            person.traits += trait
    return

label npc_bye_outfit(npc, bye_outfit=None):
    $ renpy.dynamic("npc_outfit", "bye_day", "bye_hour", "h", "activity")
    if bye_outfit:
        $ npc_outfit = bye_outfit
    else:
        $ npc_outfit = npc.get_clothes()
    $ bye_day = game.week_day
    $ bye_hour = game.hour
    if bye_hour > 23:
        $ bye_hour = 0
        $ bye_day = bye_day + 1
        if bye_day > 7:
            $ bye_day = 1
    $ (h, activity) = npc.get_activity(bye_hour)
    return bye_day, h, activity, npc_outfit
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
