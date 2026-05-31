label activity_do(do_activity):
    scene expression f"bg {game.room}"

    if date_girl and date_girl != active_girl:
        $ active_girl.object = date_girl
    $ do_activity.flags.canceled = False
    $ do_activity.flags.replaced = False
    $ do_activity.flags.end_event = False
    $ hero.activity = do_activity


    $ cache_date_girl = date_girl.object
    $ cache_active_girl = active_girl.object
    $ cache_smartphone_girl = smartphone_girl.object

    $ renpy.dynamic("valid_events")
    $ valid_events = Event.valid_events()
    while valid_events:
        $ event = valid_events.pop(0)
        call event_do (event) from _call_event_do_1
        if (date_girl.object and date_girl.object != cache_date_girl) or (active_girl.object and active_girl.object != cache_active_girl) or (smartphone_girl.object and smartphone_girl.object != cache_smartphone_girl) or (event.quit):
            $ valid_events = []

    if not active_girl:
        $ active_girl.object = cache_active_girl

    if not do_activity.flags.canceled:
        if not do_activity.flags.replaced:
            if do_activity.label:
                if isinstance(do_activity.label, tuple):
                    $ lab = do_activity.label[0]
                    $ args = do_activity.label[1:]
                else:
                    $ lab = do_activity.label
                    $ args = ()
                if active_girl:
                    $ lab = lab.replace("ACTIVE_GIRL", active_girl.id)
                if game.room:
                    $ lab = lab.replace("ROOM", game.room)
                if renpy.has_label(lab):
                    if hasattr(do_activity, "force_new_context") and do_activity.force_new_context:
                        $ renpy.call_in_new_context(lab, *args)
                    else:
                        call expression lab pass (*args) from _call_expression_512
                if not active_girl:
                    $ active_girl.object = cache_active_girl
            elif do_activity.say:
                $ renpy.say(None, randchoice(do_activity.say))
        if not do_activity.flags.canceled:
            $ do_activity.apply_changes()
        $ hero.activity = None
        $ active_girl.object = None
        $ game.story_heartbeat()
    if do_activity.flags.end_event:
        return "end_event"
    else:
        return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
