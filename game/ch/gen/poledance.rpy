init python:
    class StripClubPositionPicker(object):
        def __call__(self, attr):
            
            npc_in_attr = attr & set(p.id for p in Person.all())
            
            if game.room == "date_stripclub":
                stripclub_room = "date_stripclub"
            else:
                stripclub_room = "stripclub"
            
            present_girls = set(Room.find(stripclub_room).get_present_girls_ids())
            
            npc_in_attr.discard("kiara")
            present_girls.discard("kiara")
            
            present_girls.difference_update(npc_in_attr)
            
            if ("alone" not in attr or "forced" in attr) and ((randint(1, 100) < 25) or "forced" in attr) and ({"lexi", "reona"} <= present_girls.union(npc_in_attr)):
                present_girls.discard("lexi")
                present_girls.discard("reona")
                npc_in_attr.discard("lexi")
                npc_in_attr.discard("reona")
                
                
                npc_in_attr.add("lexireona")
            
            front_combinations = {f"{i}front" for i in npc_in_attr.union(present_girls)}
            back_combinations = {f"{i}back" for i in npc_in_attr.union(present_girls)}
            if len(npc_in_attr) == 1:
                
                front_girl = npc_in_attr.pop()
                if f"{front_girl}front" not in attr:
                    attr.add(f"{front_girl}front")
                    if f"{front_girl}" not in attr:
                        attr.add(f"{front_girl}")
                    if present_girls and "alone" not in attr:
                        
                        present_girls.discard(front_girl)
                        
                        back_girl = randchoice(list(present_girls))
                        attr.add(f"{back_girl}back")
                        if f"{back_girl}" not in attr:
                            attr.add(f"{back_girl}")
            elif npc_in_attr or present_girls:
                if len(npc_in_attr) > 1:
                    
                    front_girl, back_girl = renpy.random.sample(list(npc_in_attr), 2)
                else:
                    
                    if len(present_girls) == 1:
                        
                        front_girl = present_girls.pop()
                        back_girl = None
                    else:
                        
                        front_girl, back_girl = renpy.random.sample(list(present_girls), 2)
                
                if not front_combinations & attr:
                    attr.add(f"{front_girl}front")
                    if f"{front_girl}" not in attr:
                        attr.add(f"{front_girl}")
                
                if back_girl and not back_combinations & attr:
                    attr.add(f"{back_girl}back")
                    if f"{back_girl}" not in attr:
                        attr.add(f"{back_girl}")
            
            if enable_debug_picker:
                renpy.log(f"StripClubPositionPicker results: {attr}")
            return attr

init 1:
    layeredimage poledance:
        attribute_function MultiPickers([StripClubPositionPicker, CollarPicker, PiercingsPicker, PregnancyPicker, PubesPicker, OutfitPicker], add_simple_naked_attribute=True, append_npc_from_attributes=True)


        attribute alone null

        attribute forced null

        attribute naked null
        attribute date null
        attribute sexydate null

        attribute hanna null
        attribute shiori null
        attribute harmony null
        attribute bree null
        attribute lexi null
        attribute reona null
        attribute lexireona null

        attribute hanna_naked null
        attribute shiori_naked null
        attribute harmony_naked null
        attribute bree_naked null
        attribute lexi_naked null
        attribute reona_naked null

        attribute peace null
        attribute nopeace null
        attribute pressed null
        attribute notpressed null

        attribute reona_nohaircut null

        always:
            "poledance_bg"

        group multiple auto variant shades

        group multiple auto variant girls
        group girls_lexi auto if_any ["lexi"] if_not "lexireona"
        group girls_reona auto if_any ["reona"] if_not "lexireona"

        attribute shiori_pubes null
        attribute hanna_pubes null
        attribute harmony_pubes null
        attribute lexi_pubes null
        group pubes auto variant "shiori" if_any "shiori_pubes"
        group pubes auto variant "hanna" if_any "hanna_pubes"
        group pubes auto variant "harmony" if_any "harmony_pubes"

        attribute bree_pubes null
        attribute hanna_armpits null
        group armpits auto variant "hanna" if_any "hanna_armpits"
        group armpits auto variant "harmony" if_any "harmony_pubes"

        group tanlines auto

        group multiple auto variant piercings_hannaback when hannaback
        group multiple auto variant piercings_hannafront when hannafront
        group multiple:
            attribute hanna_tongue null

        group multiple auto variant piercings_shioriback when shioriback
        group multiple auto variant piercings_shiorifront when shiorifront
        group multiple:
            attribute shiori_clit null
            attribute shiori_ears null
            attribute shiori_pregnant_navel null

        group multiple auto variant piercings_harmonyback when harmonyback
        group multiple auto variant piercings_harmonyfront when harmonyfront
        group multiple:
            attribute harmony_nose null
            attribute harmony_tongue null

        group multiple auto variant piercings_breeback when breeback
        group multiple auto variant piercings_breefront when breefront
        group multiple:
            attribute bree_tongue null

        group multiple auto variant piercings_lexiback when lexiback and not lexireona
        group multiple auto variant piercings_lexifront when lexifront and not lexireona

        group multiple auto variant piercings_reonaback when reonaback and not lexireona
        group multiple auto variant piercings_reonafront when reonafront and not lexireona

        group multiple auto variant piercings_lexireonaback when lexireonaback
        group multiple auto variant piercings_lexireonafront when lexireonafront


        group multiple auto variant outfits when not naked:
            attribute shiori_date null
            attribute shiori_naked null
            attribute reona_naked null
            attribute reona_casual null

        group outfits auto variant "lexiback" if_any "lexiback" if_not ["naked", "lexireona"]:
            attribute lexi_sexydate default
        group outfits auto variant "lexifront" if_any "lexifront" if_not ["naked", "lexireona"]:
            attribute lexi_sexydate default

        group multiple auto variant outfits_lexireonafront when lexireonafront and not naked
        group multiple auto variant outfits_lexireonaback when lexireonaback and not naked

        group outfits auto variant "breeback" if_any "breeback" if_not "naked"
        group outfits auto variant "breefront" if_any "breefront" if_not "naked"

        group outfits auto variant "harmonyback" if_any "harmonyback" if_not "naked":
            attribute harmony_stripper default
        group outfits auto variant "harmonyfront" if_any "harmonyfront" if_not "naked":
            attribute harmony_stripper default

        group outfits auto variant "hannaback" if_any "hannaback" if_not "naked":
            attribute hanna_stripper default
        group outfits auto variant "hannafront" if_any "hannafront" if_not "naked":
            attribute hanna_stripper default

        group outfits auto variant "shioriback" if_any "shioriback" if_not "naked":
            attribute shiori_stripper default
        group outfits auto variant "shiorifront" if_any "shiorifront" if_not "naked":
            attribute shiori_stripper default

        group bot auto variant "reonaback" if_any "reonaback" if_not ["naked", "lexireona"]:
            attribute reona_date default
        group bot auto variant "reonafront" if_any "reonafront" if_not ["naked", "lexireona"]:
            attribute reona_date default

        attribute reona_innersexy null
        group innertop auto variant "reonaback_innercasual" if_any "reonaback" if_not ["naked", "reona_innersexy"]
        group innertop auto variant "reonafront_innercasual" if_any "reonafront" if_not ["naked", "reona_innersexy"]
        group innertop auto variant "reonaback_innersexy" if_all ["reonaback", "reona_innersexy"] if_not "naked"
        group innertop auto variant "reonafront_innersexy" if_all ["reonafront", "reona_innersexy"] if_not "naked"

        group top auto variant "reonaback" if_any "reonaback" if_not ["naked", "lexireona"]
        group top auto variant "reonafront" if_any "reonafront" if_not ["naked", "lexireona"]

        group bot auto variant "lexireonaback" if_any "lexireonaback" if_not "naked"
        group bot auto variant "lexireonafront" if_any "lexireonafront" if_not "naked"

        group innertop auto variant "lexireonaback_innercasual" if_any "lexireonaback" if_not ["naked", "reona_innersexy"]
        group innertop auto variant "lexireonafront_innercasual" if_any "lexireonafront" if_not ["naked", "reona_innersexy"]
        group innertop auto variant "lexireonaback_innersexy" if_all ["lexireonaback", "reona_innersexy"] if_not "naked"
        group innertop auto variant "lexireonafront_innersexy" if_all ["lexireonafront", "reona_innersexy"] if_not "naked"

        group top auto variant "lexireonaback" if_any "lexireonaback" if_not "naked"
        group top auto variant "lexireonafront" if_any "lexireonafront" if_not "naked"

        group shoes auto variant "lexireonaback" if_any "lexireonaback" if_not "naked"
        group shoes auto variant "lexireonafront" if_any "lexireonafront" if_not "naked"

        attribute shiori_pregnant null
        attribute hanna_pregnant null
        attribute harmony_pregnant null
        attribute bree_pregnant null
        attribute lexi_pregnant null
        attribute reona_pregnant null
        group multiple auto variant pregnancy_shiori when shiori_pregnant
        group multiple auto variant pregnancy_hanna when hanna_pregnant
        group multiple auto variant pregnancy_harmony when harmony_pregnant
        group multiple auto variant pregnancy_bree when bree_pregnant
        group multiple auto variant pregnancy_lexi when lexi_pregnant and not lexireona
        group multiple auto variant pregnancy_reona when reona_pregnant and not lexireona

        group piercings_pregnant auto variant "hannafront" if_any "hannafront"
        group piercings_pregnant auto variant "harmonyfront" if_any "harmonyfront"
        group piercings_pregnant auto variant "breeback" if_any "breeback"
        group piercings_pregnant auto variant "lexiback" if_any "lexiback" if_not "lexireona"
        group piercings_pregnant auto variant "reonaback" if_any "reonaback" if_not "lexireona"

        group pregnant_outfits auto variant shiorifront when shiori_pregnant and shiorifront and not naked
        group pregnant_outfits auto variant shioriback when shiori_pregnant and shioriback and not naked

        group pregnant_outfits auto variant hannafront when hanna_pregnant and hannafront and not naked
        group pregnant_outfits auto variant hannaback when hanna_pregnant and hannaback and not naked

        group pregnant_outfits auto variant lexifront when lexi_pregnant and lexifront and not (naked or lexireona)
        group pregnant_outfits auto variant lexiback when lexi_pregnant and lexiback and not (naked or lexireona)

        group pregnant_outfits auto variant harmonyfront when harmony_pregnant and harmonyfront and not naked
        group pregnant_outfits auto variant harmonyback when harmony_pregnant and harmonyback and not naked

        group pregnant_outfits auto variant breefront when bree_pregnant and breefront and not naked
        group pregnant_outfits auto variant breeback when bree_pregnant and breeback and not naked

        group multiple auto variant pregnant_outfits_reonafront when reona_pregnant and reonafront and not (naked or lexireona)
        group multiple auto variant pregnant_outfits_reonaback when reona_pregnant and reonaback and not (naked or lexireona)

        attribute shiori_collar null
        attribute hanna_collar null
        attribute harmony_collar null
        attribute bree_collar null
        attribute lexi_collar null
        attribute reona_collar null
        group collars auto variant "shiori" if_any "shiori_collar"
        group collars auto variant "hanna" if_any "hanna_collar"
        group collars auto variant "harmony" if_any "harmony_collar"
        group collars auto variant "bree" if_any "bree_collar"
        group collars auto variant "lexi" if_any "lexi_collar" if_not "lexireona"
        group collars auto variant "reona" if_any "reona_collar" if_not "lexireona"
        group collars auto variant "lexireona" if_all ["reona_collar", "lexireona"]

        group acc auto variant "reonafront" if_any "reonafront" if_not ["naked", "lexireona"]
        group acc auto variant "reonaback" if_any "reonaback" if_not ["naked", "lexireona"]

        group acc auto variant "lexireonafront" if_any "lexireonafront" if_not "naked"
        group acc auto variant "lexireonaback" if_any "lexireonaback" if_not "naked"

        group glasses auto variant "reonafront" if_any "reonafront" if_not ["naked", "lexireona"]
        group glasses auto variant "reonaback" if_any "reonaback" if_not ["naked", "lexireona"]

        group glasses auto variant "lexireonafront" if_any "lexireonafront" if_not "naked"
        group glasses auto variant "lexireonaback" if_any "lexireonaback" if_not "naked"

        group multiple auto variant lights
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
