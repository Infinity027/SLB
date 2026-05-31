label event_do(do_event, debug=False):
    scene expression f"bg {game.room}"
    if do_event:
        $ do_event.flags.cancel_activity = False
        $ do_event.flags.canceled = False
        if do_event.girl:
            $ active_girl.object = Person.find(do_event.girl)
        if hasattr(do_event, "disable_clothing_policy") and do_event.disable_clothing_policy:
            $ game.flags.disable_clothing_policy = True
        $ do_event.play_music()
        if do_event.label:
            if isinstance(do_event.label, tuple):
                $ IN_EVENT_WITH = do_event.label[0].split("_")[0]
                scene expression f"bg {game.room}"
                call expression do_event.label[0] pass (*do_event.label[1:]) from _call_expression_513
            else:
                $ IN_EVENT_WITH = do_event.label.split("_")[0]
                scene expression f"bg {game.room}"
                call expression do_event.label from _call_expression_514
            $ IN_EVENT_WITH = ""
        if hasattr(do_event, "disable_clothing_policy") and do_event.disable_clothing_policy:
            $ game.flags.disable_clothing_policy = False
        if do_event.flags.canceled:
            if do_event.block_when_canceled:
                $ do_event.flags.blocked = TemporaryFlag(True, "day")
            return
        $ do_event.apply_changes()
        if do_event.girl:
            $ active_girl.object = None
        if do_event.cancel_activity:
            $ hero.activity = None
    $ game.do_event = None
    $ game.story_heartbeat()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
