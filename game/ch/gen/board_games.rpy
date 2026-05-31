init python:
    class CG_BoardGames_Picker(object):
        def __call__(self, attr):
            games = {'dungeon', 'imperium', 'island', 'lovecraft', 'zombie'}
            if not attr & games:
                attr.add(randchoice(tuple(games)))
            
            if attr & {"bree", "sasha", "minami", "lexi", "audrey", "aletta", "mike", "samantha", "jack", "shiori"}:
                attr.add("01")
            elif attr & {"palla", "morgan", "lavish", "alexis", "cassidy", "camila", "victor", "shawn"}:
                attr.add("02")
            elif attr & {"harmony", "angela", "dwayne", "scottie", "ayesha", "kleio", "amy", "kat", "reona"}:
                attr.add("03")
            elif attr & {"anna", "ryan", "master", "danny", "kylie", "emma", "hanna", "cherie", "claire", "kiara"}:
                attr.add("04")
            
            if enable_debug_picker:
                renpy.log(f"CG_BoardGames_Picker results: {attr}")
            return attr

init 1:
    layeredimage board games:
        attribute_function MultiPickers([PubesPicker, PregnancyPicker, PiercingsPicker, HaircutPicker, CollarPicker, OutfitPicker, MCCGPicker, CG_BoardGames_Picker], append_npc_from_attributes=True, add_simple_pregnant_attribute=True, add_simple_naked_attribute=True)

        attribute naked null
        attribute mc_naked null

        group dicks:
            attribute mc_big null
            attribute mc_medium null
            attribute mc_small null

        group bg auto




        group couch_behind_npc auto
        group couch_behind_boobjobs auto:
            attribute sasha_noboobjob null
        group couch_behind_pregnancies auto
        group couch_behind_collars auto
        group couch_behind_haircuts auto

        group multiple auto variant couch_behind_piercings_under
        group multiple auto variant couch_behind_piercings_under_boobjob when sasha_boobjob
        group multiple auto variant couch_behind_piercings_under_noboobjob when sasha_noboobjob

        group couch_behind_outfits auto when not naked
        group couch_behind_outfits auto variant boobjob when sasha_boobjob and not naked
        group couch_behind_outfits auto variant pregnant when pregnant and not naked

        group couch_behind_acc auto when not naked


        group couch_behind_bot auto when not naked
        group couch_behind_bot auto variant pregnant when pregnant and not naked
        group couch_behind_top auto when not naked
        group couch_behind_top auto variant pregnant when pregnant and not naked
        group couch_behind_makeup auto

        group multiple auto variant couch_behind_piercings


        group mc auto variant 01 when 01
        group mc auto variant 02 when 02
        group mc auto variant 03 when 03
        group mc auto variant 04 when 04

        group mchaircuts_01 auto when breemc and 01
        group mchaircuts_02 auto when breemc and 02
        group mchaircuts_03 auto when breemc and 03
        group mchaircuts_04 auto when breemc and 04

        group mcoutfits_01 auto variant mikemc when mikemc and 01 and not mc_naked
        group mcoutfits_01 auto variant breemc when breemc and 01 and not mc_naked

        group mcoutfits_02 auto variant mikemc when mikemc and 02 and not mc_naked
        group mcoutfits_02 auto variant breemc when breemc and 02 and not mc_naked

        group mcoutfits_03 auto variant mikemc when mikemc and 03 and not mc_naked
        group mcoutfits_03 auto variant breemc when breemc and 03 and not mc_naked

        group mcoutfits_04 auto variant mikemc when mikemc and 04 and not mc_naked
        group mcoutfits_04 auto variant breemc when breemc and 04 and not mc_naked

        group mc_fg_01 auto when 01


        group couch_ahead_npc auto
        group couch_ahead_pregnancies auto when pregnant and naked
        group couch_ahead_collars auto when collar
        group couch_ahead_haircuts auto

        group multiple auto variant couch_ahead_piercings_under

        group couch_ahead_outfits auto when not naked
        group couch_ahead_outfits auto variant pregnant when pregnant and not naked

        group multiple auto variant couch_ahead_piercings


        group table_npc auto
        group table_pubes auto when pubes and naked
        group table_armpits auto when armpits
        group table_pregnancies auto when pregnant and naked
        group table_collars auto when collar
        group table_haircuts auto

        group multiple auto variant table_piercings_under

        group table_outfits auto when not naked
        group table_outfits auto variant pregnant when pregnant and not naked

        group multiple auto variant table_piercings


        group table auto


        group boardgames:
            attribute dungeon null
            attribute imperium null
            attribute island null
            attribute lovecraft null
            attribute zombie null

        group boardgame auto variant dungeon when dungeon
        group boardgame auto variant imperium when imperium
        group boardgame auto variant island when island
        group boardgame auto variant lovecraft when lovecraft
        group boardgame auto variant zombie when zombie


        group multiple:
            attribute hanna_clit null
            attribute hanna_navel null
            attribute hanna_nipples null
            attribute hanna_tongue null
            attribute minami_clit null
            attribute minami_ears null
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
