label give_lapdance_female:
    $ renpy.dynamic("choices")
    $ choices = []
    python:
        for npc in sorted(Room.find(game.room).get_present_npcs(), key=lambda x: x.name):
            if npc.love >= 150 and renpy.has_label(f"give_{npc.id}_lapdance"):
                choices.append((f"{npc.name}", f"give_{npc.id}_lapdance"))
    if not choices:
        return "canceled"
    $ choices.append(("Cancel", "canceled"))
    $ narrator("Who will have a private show?", interact=False)
    $ lapdance_result = renpy.display_menu(choices)
    if lapdance_result == "canceled":
        return "canceled"
    else:
        call expression lapdance_result from _call_expression_458
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
