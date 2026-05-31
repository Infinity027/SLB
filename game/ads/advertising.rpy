init -50 python:
    displayed_links_offset, displayed_links_max = 0, 3
    platforms_games_links = {
    "itchio": {
        "LoSeSb": {"url": "https://andrealphus.itch.io/love-sex-second-base", "priority": 1},
        "mydemonicromance": {"url": "https://andrealphus.itch.io/my-demonic-romance", "priority": 2},
        "LoSeSb_Shawn_Story": {"url": "https://andrealphus.itch.io/shawns-story", "priority": 3},
        "LeapofLove": {"url": "https://andrealphus.itch.io/leap-of-love", "priority": 6},
        "TruLove": {"url": "https://andrealphus.itch.io/trulove", "priority": 7},
    },
    "patreon": {
        "LoSeSb": {"url": "https://www.patreon.com/Andrealphus/", "priority": 1},
        "mydemonicromance": {"url": "https://www.patreon.com/mydemonicromance", "priority": 2},
    },
    "steam": {
        "LoSeSb": {"url": "https://store.steampowered.com/app/1264710/Love_and_Sex_Second_Base/", "priority": 1},
        "mydemonicromance": {"url": "https://store.steampowered.com/app/2370140/My_Demonic_Romance/", "priority": 2},
        "LoSeSb_Shawn_Story": {"url": "https://store.steampowered.com/app/3795260/Love_and_Sex_Second_Base__Shawns_story/", "priority": 3},
        "LeapofLove": {"url": "https://store.steampowered.com/app/1469300/Leap_of_Love/", "priority": 6},
    },
    "gog": {
        "LoSeSb": {"url": "https://www.gog.com/en/game/love_sex_second_base", "priority": 1},
        "LeapofLove": {"url": "https://www.gog.com/en/game/leap_of_love", "priority": 6},
        "TruLove": {"url": "https://www.gog.com/en/game/trulove", "priority": 7},
    },
}
    platforms_dlcs_links = {
    "itchio": {
        "fafow": {"url": "https://andrealphus.itch.io/fafow", "priority": 4},
        "fafwm": {"url": "https://andrealphus.itch.io/fafwm", "priority": 5},
    },
    "steam": {
        "fafow": {"url": "https://store.steampowered.com/app/2945780/Love_and_Sex_Second_Base__For_A_Fistful_Of_Waifu/", "priority": 4},
        "fafwm": {"url": "https://store.steampowered.com/app/4190270/Love_and_Sex_Second_Base__For_A_Few_Waifus_More/", "priority": 5},
        
    },
    "gog": {
        "fafow": {"url": "https://www.gog.com/en/game/love_and_sex_second_base_for_a_fistful_of_waifu", "priority": 4},
        
    },
}

screen advertising(orientation, box_offset=(0, 0), box_spacing=10, box_reverse=False, button_fg_offset=(0, 0), button_bg_border_size=10, button_bg_idle=Frame("gui/frame.png"), button_bg_hover=Color("#ededed"), arrow_idle_color="#ffffff", arrow_hover_color="#ffffff", zoom=1.0):

    if platforms_games_links.get(build_platform) and not is_sub_screen():


        $ game_list = platforms_games_links.get(build_platform,{})


        $ game_list.update(platforms_dlcs_links.get(build_platform, {}))

        $ game_list = {k:v for k,v in game_list.items() if (k != build.name and k not in DLCS)}


        $ game_list = {game_build_name: game_list[game_build_name]["url"] for game_build_name in sort_dict(game_list, lambda x: x[1]["priority"])}


        if len(game_list) > displayed_links_max:
            $ displayed_list = dict()
            for i in range(0, displayed_links_max):
                $ dict_key = list(game_list)[(i + displayed_links_offset) % len(game_list)]
                $ displayed_list[dict_key] = game_list[dict_key]
        else:
            $ displayed_list = game_list.copy()



        if orientation == 'horizontal':
            hbox:
                align (0.5, 0.95)
                offset box_offset
                spacing box_spacing
                box_reverse box_reverse


                if len(game_list) > displayed_links_max:
                    imagebutton align (0.5, 0.5):
                        idle Transform("ads/arrow_right.png" if box_reverse else "ads/arrow_left.png", zoom=zoom, matrixcolor=TintMatrix(arrow_idle_color))
                        hover Transform("ads/arrow_right.png" if box_reverse else "ads/arrow_left.png", zoom=zoom, matrixcolor=TintMatrix(arrow_hover_color))
                        action SetVariable("displayed_links_offset", displayed_links_offset-1)


                for game, game_url in displayed_list.items():
                    button:
                        idle_background button_bg_idle
                        hover_background button_bg_hover
                        xsize int(240*zoom+button_bg_border_size)
                        ysize int(138*zoom+button_bg_border_size)
                        action OpenURL(game_url)
                        add Transform(f"ads/{game}.png", zoom=zoom) align (0.5, 0.5) offset button_fg_offset


                if len(game_list) > displayed_links_max:
                    imagebutton align (0.5, 0.5):
                        idle Transform("ads/arrow_left.png" if box_reverse else "ads/arrow_right.png", zoom=zoom, matrixcolor=TintMatrix(arrow_idle_color))
                        hover Transform("ads/arrow_left.png" if box_reverse else "ads/arrow_right.png", zoom=zoom, matrixcolor=TintMatrix(arrow_hover_color))
                        action SetVariable("displayed_links_offset", displayed_links_offset+1)


        elif orientation == 'vertical':
            vbox:
                align (0.95, 0.5)
                offset box_offset
                spacing box_spacing
                box_reverse box_reverse


                if len(game_list) > displayed_links_max:
                    imagebutton align (0.5, 0.5):
                        idle Transform("ads/arrow_down.png" if box_reverse else "ads/arrow_up.png", zoom=zoom, matrixcolor=TintMatrix(arrow_idle_color))
                        hover Transform("ads/arrow_down.png" if box_reverse else "ads/arrow_up.png", zoom=zoom, matrixcolor=TintMatrix(arrow_hover_color))
                        action SetVariable("displayed_links_offset", displayed_links_offset-1)


                for game, game_url in displayed_list.items():
                    button:
                        idle_background button_bg_idle
                        hover_background button_bg_hover
                        xsize int(240*zoom+button_bg_border_size)
                        ysize int(138*zoom+button_bg_border_size)
                        action OpenURL(game_url)
                        add Transform(f"ads/{game}.png", zoom=zoom) align (0.5, 0.5) offset button_fg_offset


                if len(game_list) > displayed_links_max:
                    imagebutton align (0.5, 0.5):
                        idle Transform("ads/arrow_up.png" if box_reverse else "ads/arrow_down.png", zoom=zoom, matrixcolor=TintMatrix(arrow_idle_color))
                        hover Transform("ads/arrow_up.png" if box_reverse else "ads/arrow_down.png", zoom=zoom, matrixcolor=TintMatrix(arrow_hover_color))
                        action SetVariable("displayed_links_offset", displayed_links_offset+1)


        else:
            python:
                raise Error("orientation must be 'horizontal' or 'vertical'")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
