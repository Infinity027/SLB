label enter_room(back="street", room_present_girls=[], max_time=0):
    $ renpy.dynamic("room")
    if game.room and Room.find(game.room):
        $ room = Room.find(game.room)
    else:
        $ room = Room.find(back)
        $ game.room = back
    $ _window_hide(trans=False)
    if max_time:
        $ end_time = game.hour + max_time
        if end_time > 23:
            $ end_time = end_time - 24
            $ end_day = game.day + 1
        else:
            $ end_day = game.day
    $ room.travel_to()
    $ room.pay_entrance()
    $ hero.flags.visited_rooms.add(game.room)
    $ room.stop_sounds_on_channels()
    scene expression room.bg
    while game.room == room.id:
        if date_girl and (not active_girl or active_girl != date_girl):
            $ active_girl.object = date_girl
        $ Game.update_rooms()
        $ room = Room.find(game.room)
        $ room.play_music()
        $ entering_time = game.hour
        if max_time and end_time <= game.hour and end_day == game.day or not room.test():
            $ game.room = back
            $ game.from_room = room.id
            return
        else:
            $ room.present_girls = room.get_present_girls(girls=room_present_girls)

            $ cache_date_girl = date_girl.object
            $ cache_active_girl = active_girl.object
            $ cache_smartphone_girl = smartphone_girl.object
            $ renpy.dynamic("valid_events")
            $ valid_events = Event.valid_events()

            while valid_events:
                $ event = valid_events.pop(0)
                call event_do (event) from _call_event_do_3
                if (date_girl.object and date_girl.object != cache_date_girl) or (active_girl.object and active_girl.object != cache_active_girl) or (smartphone_girl.object and smartphone_girl.object != cache_smartphone_girl) or (event.quit) or game.flags.EventQuit:
                    $ game.flags.EventQuit = False
                    $ valid_events = []
        scene expression room.bg


        $ hide_people()
        $ game.flags.room_showing_people = []
        if game.room == room.id and entering_time == game.hour:
            python:
                for g in room.present_girls:
                    if not g.hidden:
                        g.desire_bonus()
                Game.update_rooms()

            $ girlidx = 0
            label roomshowloop:
                if room.id == "map":
                    $ quick_menu = False
                    call screen map(room.get_exits()) nopredict
                    $ quick_menu = True
                elif room.id == "housemap":
                    $ quick_menu = False
                    call screen housemap(room.get_exits()) nopredict
                    $ quick_menu = True
                elif room.id == "mallmap":
                    $ quick_menu = False
                    call screen mallmap(room.get_exits()) nopredict
                    $ quick_menu = True
                else:

                    python:
                        present_girls = room.get_present_girls()
                        more_people_present = len(present_girls) > 3
                        shown_girls = present_girls[girlidx:girlidx + 3]


                        showexpr = [(g.id, f"{g.id} {''} {g.get_clothes()}")
    for g in (present_girls if (persistent.lively_bg and hasattr(room, "lively_npc") and room.lively_npc) else shown_girls)
    if (not g.activity_name == "sleep" or game.active_date.on_date(g.id))
    
    ]
                        game.flags.room_showing_people = showexpr
                        show_people()
                    call screen room(room=room, shown_girls=shown_girls, more_people_present=more_people_present, exits=room.get_exits()) nopredict
                if _return == "+":
                    $ girlidx = girlidx + 3
                    if girlidx >= len(present_girls):
                        $ girlidx = 0

                    $ hide_people()
                    $ game.flags.room_showing_people = []
                    jump roomshowloop
                elif isinstance(_return, Person):
                    call girl_interact (_return) from _call_girl_interact
                elif isinstance(_return, BaseActivity):
                    call activity_do (_return) from _call_activity_do_1
                if not ('room' in vars() or 'room' in locals()) or not room:
                    $ room = Room.find("map")
                $ game.from_room = room.id
        else:
            if not ('room' in vars() or 'room' in locals()):
                $ room = Room.find("map")
            $ game.from_room = room.id
            return
    if not ('room' in vars() or 'room' in locals()):
        $ room = Room.find("map")
    $ game.from_room = room.id
    return
return
