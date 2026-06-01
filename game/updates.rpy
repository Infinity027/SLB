init -999 python:
    def after_load_callback():
        
        renpy.log(f"Loading save from: `{SAVE_VERSION}`")
        renpy.log("Checking calendar")
        try:
            hero.calendar
        except:
            update_calendar()
        
        for name in ["active_girl", "date_girl", "interact_girl"]:
            renpy.log(f"Checking {name}")
            try:
                val = getattr(store, name)
                if isinstance(val, PersonWrapper):
                    
                    if not "_id" in val.__dict__ or val._id != name:
                        val._id = name
                    continue
                if isinstance(val, Person):
                    
                    if val and not game.flags.dateinprogress:
                        val = None
                    setattr(store, name, PersonWrapper(name, val))
                else:
                    setattr(store, name, PersonWrapper(name))
            except:
                setattr(store, name, PersonWrapper(name))
        
        for notification, duration in store.NOTIFICATIONS:
            if "small.png" in notification or "_white.png" in notification:
                renpy.block_rollback()
                store.NOTIFICATIONS = []
                break
        
        if hasattr(store, "re") and isinstance(store.re, int):
            del store.re
        
        if check_too_old_saves("21.12.0d") or check_too_old_saves("weekly.202152"):
            renpy.call_screen("too_old_save")
        
        if compare_version("22.1.0") or compare_version("weekly.20225"):
            update_22_1_0()
        
        if compare_version("22.1.0a") or compare_version("weekly.20226"):
            update_22_1_0a()
        
        if compare_version("22.2.0") or compare_version("weekly.20229"):
            update_22_2_0()
        
        if compare_version("22.2.0c") or compare_version("weekly.202211"):
            update_22_2_0c()
        
        if compare_version("22.4.0") or compare_version("weekly.202217"):
            update_22_4_0()
        
        if compare_version("22.5.0") or compare_version("weekly.202222"):
            update_22_5_0()
        
        if compare_version("22.5.0b") or compare_version("weekly.202223"):
            update_22_5_0b()
        
        if compare_version("22.6.0") or compare_version("week.202226"):
            update_22_6_0()
        
        if compare_version("22.7.0a") or compare_version("week.202230"):
            update_22_7_0()
        
        if compare_version("22.8.0") or compare_version("week.202235"):
            update_22_8_0()
        
        if compare_version("22.9.0") or compare_version("week.202239"):
            update_22_9_0()
        
        if compare_version("22.10.0") or compare_version("week.202244"):
            update_22_10_0()
        
        if compare_version("22.10.0a") or compare_version("week.202244"):
            update_22_10_0a()
        
        if compare_version("22.11.0") or compare_version("week.202245"):
            update_22_11_0()
        
        if compare_version("23.1.0") or compare_version("week.202304"):
            update_23_1_0()
        
        if compare_version("23.2.0") or compare_version("week.202308"):
            update_23_2_0()
        
        if compare_version("23.3.0") or compare_version("week.202312"):
            update_23_3_0()
        
        if compare_version("23.3.0a") or compare_version("week.202313"):
            update_23_3_0a()
        
        if compare_version("23.4.0") or compare_version("week.202316"):
            update_23_4_0()
        
        if compare_version("23.4.0f") or compare_version("week.202318"):
            update_23_4_0f()
        
        if compare_version("23.5.0") or compare_version("week.202321"):
            update_23_5_0()
        
        if compare_version("23.5.0a") or compare_version("week.202322"):
            update_23_5_0a()
        
        if compare_version("23.5.0c") or compare_version("week.202322"):
            update_23_5_0c()
        
        if compare_version("23.6.0") or compare_version("week.202326"):
            update_23_6_0()
        
        if compare_version("23.6.0a") or compare_version("week.202327"):
            update_23_6_0a()
        
        if compare_version("23.6.1") or compare_version("week.202329"):
            update_23_6_1()
        
        if compare_version("23.6.1c") or compare_version("week.202329"):
            update_23_6_1c()
        
        if compare_version("23.6.1d") or compare_version("week.202329"):
            update_23_6_1d()
        
        if compare_version("23.7.0") or compare_version("week.202331"):
            update_23_7_0()
        
        if compare_version("23.8.0") or compare_version("week.202335"):
            update_23_8_0()
        
        if compare_version("23.9.0") or compare_version("week.202339"):
            update_23_9_0()
        
        if compare_version("23.9.0c") or compare_version("week.202340"):
            update_23_9_0c()
        
        if compare_version("23.10.0") or compare_version("week.202344"):
            update_23_10_0()
        
        if compare_version("23.10.0a") or compare_version("week.202345"):
            update_23_10_0a()
        
        if compare_version("23.11.0") or compare_version("week.202348"):
            update_23_11_0()
        
        if compare_version("23.11.0a") or compare_version("week.202349"):
            update_23_11_0a()
        
        if compare_version("24.1.0") or compare_version("week.202405"):
            update_24_1_0()
        
        if compare_version("24.3.0") or compare_version("week.202413"):
            update_24_3_0()
        
        if compare_version("24.4.0") or compare_version("week.202418"):
            update_24_4_0()
        
        if compare_version("24.4.0a") or compare_version("week.202422"):
            update_24_4_0a()
        
        if compare_version("24.5.0") or compare_version("week.202422"):
            update_24_5_0()
        
        if compare_version("24.6.0a") or compare_version("week.202426"):
            update_24_6_0a()
        
        if compare_version("24.7.0") or compare_version("week.202431"):
            update_24_7_0()
        
        if compare_version("24.7.0d") or compare_version("week.202432"):
            update_24_7_0d()
        
        if compare_version("24.8.0") or compare_version("week.202435"):
            update_24_8_0()
        
        if compare_version("24.8.0b") or compare_version("week.202435"):
            update_24_8_0b()
        
        if compare_version("24.9.0") or compare_version("week.202440"):
            update_24_9_0()
        
        if compare_version("24.9.1") or compare_version("week.202440"):
            update_24_9_1()
        
        if compare_version("24.9.1b") or compare_version("week.202441"):
            update_24_9_1b()
        
        if compare_version("24.9.1c") or compare_version("week.202441"):
            update_24_9_1c()
        
        if compare_version("24.9.1d") or compare_version("week.202442"):
            update_24_9_1d()
        
        if compare_version("24.10.0") or compare_version("week.202444"):
            update_24_10_0()
        
        if compare_version("24.10.0a") or compare_version("week.202445"):
            update_24_10_0a()
        
        if compare_version("24.11.0b") or compare_version("week.202449"):
            update_24_11_0b()
        
        if compare_version("25.1.0") or compare_version("week.202505"):
            update_25_1_0()
        
        if compare_version("25.1.0b") or compare_version("week.202507"):
            update_25_1_0b()
        
        if compare_version("25.2.0") or compare_version("week.202509"):
            update_25_2_0()
        
        if compare_version("25.3.0") or compare_version("week.202514"):
            update_25_3_0()
        
        if compare_version("25.3.0c") or compare_version("week.202515"):
            update_25_3_0c()
        
        if compare_version("25.4.0b") or compare_version("week.202519"):
            update_25_4_0b()
        
        if compare_version("25.5.0") or compare_version("week.202522"):
            update_25_5_0()
        
        if compare_version("25.6.0b") or compare_version("week.202528"):
            update_25_6_0b()
        
        if compare_version("25.8.0") or compare_version("week.202533"):
            update_25_8_0()
        
        if compare_version("25.9.0") or compare_version("week.202540"):
            update_25_9_0()
        
        if compare_version("25.10.0a") or compare_version("week.202545"):
            update_25_10_0a()
        
        if compare_version("26.1.0") or compare_version("week.202605"):
            update_26_1_0()
        
        if compare_version("26.1.0a") or compare_version("week.202606"):
            update_26_1_0a()
        
        if compare_version("26.1.0b") or compare_version("week.202606"):
            update_26_1_0b()
        
        if compare_version("26.1.0c") or compare_version("week.202606"):
            update_26_1_0c()
        
        if compare_version("26.2.0") or compare_version("week.202609"):
            update_26_2_0()
        
        if compare_version("26.3.0") or compare_version("week.202614"):
            update_26_3_0()
        
        if compare_version("26.3.1") or compare_version("week.202614"):
            update_26_3_1()
        
        if compare_version("26.4.0b") or compare_version("week.202619"):
            update_26_4_0b()
        
        
        setattr(store, "SAVE_VERSION", config.version)
        storytracker.build_cache()
        storytracker.refresh(skip_notify=True)
        
        
        storytracker.self_test()


    def compare_version(game_version):
        import re
        
        week_regex = re.compile(
        r"^(?:week|weekly)\.(?P<year>\d{4})(?P<week>\d+)(?:\.(?P<patch>\d+))?$"
    )
        
        if re.match(week_regex, SAVE_VERSION) and re.match(week_regex, game_version):
            game_year, game_week, game_patch = re.match(week_regex, game_version).groups(
            "0"
        )
            save_year, save_week, save_patch = re.match(week_regex, SAVE_VERSION).groups(
            "0"
        )
            if int(game_year) > int(save_year):
                return True
            elif int(game_year) == int(save_year) and int(game_week) > int(save_week):
                return True
            elif (
            int(game_year) == int(save_year)
            and int(game_week) == int(save_week)
            and int(game_patch) > int(save_patch)
        ):
                return True
            else:
                return False
        
        
        elif re.match(week_regex, SAVE_VERSION) or re.match(week_regex, game_version):
            return False
        
        
        if not bool(re.match(r"\d+\.\d+\.\w+", game_version)):
            raise Exception(
            "Invalid game version provided to compare_version function: {}".format(
                game_version
            )
        )
        
        new_major, new_minor, new_patch = game_version.split(".")
        old_major, old_minor, old_patch = SAVE_VERSION.split(".")
        
        if int(new_major) > int(old_major):
            return True
        elif new_major == old_major and int(new_minor) > int(old_minor):
            return True
        elif new_major == old_major and new_minor == old_minor and new_patch > old_patch:
            return True
        else:
            return False


    def check_too_old_saves(old_version):
        import re
        
        week_regex = re.compile(
        r"^(?:week|weekly)\.(?P<year>\d{4})(?P<week>\d+)(?:\.(?P<patch>\d+))?$"
    )
        
        if re.match(week_regex, SAVE_VERSION) and re.match(week_regex, old_version):
            old_year, old_week, old_patch = re.match(week_regex, old_version).groups("0")
            save_year, save_week, save_patch = re.match(week_regex, SAVE_VERSION).groups(
            "0"
        )
            if int(old_year) > int(save_year):
                return True
            elif int(old_year) == int(save_year) and int(old_week) > int(save_week):
                return True
            elif (
            int(old_year) == int(save_year)
            and int(old_week) == int(save_week)
            and int(old_patch) >= int(save_patch)
        ):
                return True
            else:
                return False
        
        
        elif re.match(week_regex, SAVE_VERSION) or re.match(week_regex, old_version):
            return False
        
        
        if not bool(re.match(r"\d+\.\d+\.\w+", old_version)):
            raise Exception(
            "Invalid game version provided to compare_version function: {}".format(
                old_version
            )
        )
        
        old_major, old_minor, old_patch = old_version.split(".")
        save_major, save_minor, save_patch = SAVE_VERSION.split(".")
        
        if int(old_major) > int(save_major):
            return True
        elif old_major == save_major and int(old_minor) > int(save_minor):
            return True
        elif (
        old_major == save_major and old_minor == save_minor and old_patch >= save_patch
    ):
            return True
        else:
            return False


    def update_calendar():
        hero.calendar = Calendar()
        for day, hours in hero.appointments.items():
            for hour, appointments in hours.items():
                for appointment in appointments:
                    if Person.find(appointment) is not None:
                        hero.calendar.add(day, DateAppointment(hour, appointment))
                    elif renpy.has_label(appointment):
                        hero.calendar.add(
                        day,
                        LabelAppointment(
                            hour, [], appointment.replace("_", " ").title(), appointment
                        ),
                    )


    def update_22_1_0():
        if "cherie_vault" in DONE:
            game.flags.dwaynedead = True
        renpy.block_rollback()


    def update_22_1_0a():
        if game.active_date and not hasattr(game.active_date, "stay_coffee"):
            date.stay_coffee = True


    def update_22_2_0():
        for girl in Person.all():
            if girl.flags.sex and not girl.sexperience.val:
                girl.sexperience.val = girl.flags.sex
        if aletta.flags.weeklyspank:
            aletta.flags.weeklyspank = game.days_played - 7
        
        if "minami_practice_sex" not in DONE:
            if minami.sexperience:
                minami.sexperience = 0
                minami.flags.sexperience = 0
            if minami.is_visibly_pregnant:
                minami.unpreg()
            if minami.flags.anal:
                minami.flags.anal = 0
            if "minami_dick_reactions" in DONE:
                minami.flags.seendick = 0
            if minami.flags.showersex:
                minami.flags.showersex = False


    def update_22_2_0c():
        if "kylie_investigation_3" in DONE and not kylie.flags.schedule == "jail":
            
            kylie.love.max = 100
            kylie.love.val = 100
            kylie.unhide()
            for harem in Harem.find(kylie, is_active=False):
                harem.apologize(kylie)
            hero.smartphone_contacts.append("kylie")
            
            
            kylie.flags.schedule = "jail"
            kylie.flags.nodate = True
            kylie.flags.noproposedate = True


    def update_22_4_0():
        if hero.flags.base_sexperience == None:
            hero.flags.base_sexperience = 0
        
        if "angela_bj_bruce" in DONE and renpy.seen_image(
        "angela breedad bj mike closed blowjob"
    ):
            game.flags.angelaBlow = True


    def update_22_5_0():
        if "lexi_event_06" in DONE and not hero.has_item("danny_corpse"):
            hero.gain_item("danny_corpse")
        
        if sasha.flags.BreastComplex == 1:
            sasha.flags.BreastComplex = True
        else:
            sasha.flags.BreastComplex = False
        
        hero.energy.update_max(hero.fitness)
        hero.fun.update_max(hero.knowledge)
        hero.grooming.update_max(hero.charm)
        
        for key in FLAGS.keys():
            if key.endswith("knowntraits"):
                
                
                FLAGS[key].value = set(FLAGS[key].value) & set(
                YAML[key.replace("knowntraits", "")]["traits"]
            )
            elif key.endswith("traits"):
                
                default_traits = set(YAML[key.replace("traits", "")]["traits"])
                actual_traits = set(FLAGS[key].value)
                FLAGS[key].value = set(
                "+{}".format(trait) for trait in actual_traits - default_traits
            ) | set("-{}".format(trait) for trait in default_traits - actual_traits)


    def update_22_5_0b():
        if minami.flags.siscon >= 80:
            minami.flags.noFlirtyText = False
            if minami.flags.siscon >= 100:
                minami.flags.noDirtyText = False
        
        if aletta.flags.vibrate:
            aletta.flags.vibrator = True


    def update_22_6_0():
        
        for old, new, condition in (
        
        ("cake", "cake_gift", "isinstance(hero.inventory['cake'], Gift)"),
        
        
        ("sexy underwear", "lingerie", "hero.is_male"),
        
        
        ("Guitar practice book", "skill_book_guitar", "hero.is_female"),
        
        ("Valentine chocolates", "valentine_chocolates", None),
        ("Minty candies", "minty_candies", None),
        ("Energy drink", "energy_drink", None),
        ("Pastry", "pastry", None),
        ("Romance novel", "romance_novel", None),
        ("Mistress Amanda", "mistress_amanda", None),
        ("Yuri Manga", "yuri_manga", None),
        ("Porn magazine", "porn_magazine", None),
        ("A sex slave's story", "a_sex_slave_story", None),
        ("Leather bound bible", "leather_bound_bible", None),
        ("knowledge book", "knowledge_book", None),
        ("fitness book", "fitness_book", None),
        ("charm book", "charm_book", None),
        ("fun book", "fun_book", None),
        ("Skill book: massage", "skill_book_massage", None),
        ("Skill book: guitar", "skill_book_guitar", None),
        ("Skill book: cooking", "skill_book_cooking", None),
        ("Sexperience book", "sexperience_book", None),
        ("Skill book: shibari", "skill_book_shibari", None),
        ("Skill book: SM", "skill_book_sm", None),
        ("Skill book: fertility assessment", "skill_book_fertility", None),
        ("Skill book: fertility", "skill_book_fertility", None),
        ("Fantasy book (signed)", "fantasy_book_signed", None),
        ("fancy dress", "fancy_dress", None),
        ("leather pants", "leather_pants", None),
        ("luxury bracelet", "luxury_bracelet", None),
        ("fancy clothes", "fancy_clothes", None),
        ("tweed blazer", "tweed_blazer", None),
        ("military fatigues", "military_fatigues", None),
        ("luxury watch", "luxury_watch", None),
        ("leather jacket", "leather_jacket", None),
        ("sweat pants", "sweat_pants", None),
        ("funny shirt", "funny_shirt", None),
        ("sport clothes", "sport_clothes", None),
        ("cool sunglasses", "cool_sunglasses", None),
        ("geeky pen", "geeky_pen", None),
        ("sport shoes", "sport_shoes", None),
        ("funny badge", "funny_badge", None),
        ("military boots", "military_boots", None),
        ("sexy dress", "sexy_dress", None),
        ("slutty dress", "slutty_dress", None),
        ("cute top", "cute_top", None),
        ("nice scarf", "nice_scarf", None),
        ("sexy swimsuit", "sexy_swimsuit", None),
        ("cute swimsuit", "cute_swimsuit", None),
        ("fancy purse", "fancy_purse", None),
        ("fancy shoes", "fancy_shoes", None),
        ("sexy underwear", "sexy_underwear", None),
        ("t-shirt", "tshirt", None),
        ("leather shoes", "leather_shoes", None),
        ("swimming t-back", "swimming_tback", None),
        ("swimming trunk", "swimming_trunk", None),
        ("fancy watch", "fancy_watch", None),
        ("sports shoes", "sports_shoes", None),
        ("Coffee", "coffee", None),
        ("Cappucino", "cappuccino", None),
        ("Moka", "moka", None),
        ("box of condoms", "box_of_condoms", None),
        ("bigger staff pill", "bigger_staff_pill", None),
        ("smaller staff pill", "smaller_staff_pill", None),
        ("blue pill", "blue_pill", None),
        ("zbox 360", "zbox_360", None),
        ("fitness machine", "fitness_machine", None),
        ("knowledge machine", "knowledge_machine", None),
        ("charm machine", "charm_machine", None),
        ("spy camera", "spy_camera", None),
        ("electric guitar", "electric_guitar", None),
        ("lots of flowers", "lots_of_flowers", None),
        ("sport_car", "sports_car", None),
        ("silver bracelet", "silver_bracelet", None),
        ("silver necklace", "silver_necklace", None),
        ("gold bracelet", "gold_bracelet", None),
        ("gold necklace", "gold_necklace", None),
        ("diamond necklace", "diamond_necklace", None),
        ("wedding ring", "wedding_ring", None),
        ("teddy bear", "teddy_bear", None),
        ("luxury bed", "luxury_bed", None),
        ("baseball bat", "baseball_bat", None),
        ("anal beads", "anal_beads", None),
        ("large dildo", "large_dildo", None),
        ("bondage ropes", "bondage_ropes", None),
        ("butt plug", "butt_plug", None),
        ("slave collar", "slave_collar", None),
        ("cosplay outfit", "cosplay_outfit", None),
        ("Guitar practice book", "guitar_practice_book", None),
        ("bree's sweater", "bree_sweater", None),
        ("Protein powder", "protein_powder", None),
        ("Kylie's cookies", "kylie_cookies", None),
        ("lavish's tie", "lavish_tie", None),
        ("lavish's lucky panties", "lavish_lucky_panties", None),
        ("lexi's panties", "lexi_panties", None),
        ("minami's sweater", "minami_sweater", None),
        ("Cologne", "cologne", None),
        ("Shiori's milk", "shiori_milk", None),
    ):
            if old in hero.inventory and (condition is None or eval(condition)):
                hero.inventory[new] = hero.inventory[old]
                del hero.inventory[old]
        
        for key, value in hero.inventory.items():
            if isinstance(value, Consumable):
                
                
                hero.inventory[key] = (
                value.uses + (value.nbr - 1) * Consumable.find(key).uses
            )
            elif isinstance(value, ItemBase):
                hero.inventory[key] = value.nbr
        
        
        for girl in Person.all_people(False):
            if girl.collared:
                girl.flags["giftslave_collar"] = True
            if girl.flags.sexyswimsuit_gifted:
                girl.flags["giftsexy_swimsuit"] = True
            if girl.flags.sexydate_gifted:
                girl.flags["giftsexy_dress"] = True
            if girl.flags.sluttydate_gifted:
                girl.flags["giftslutty_dress"] = True
            if girl.flags.buttplug:
                girl.flags["giftbutt_plug"] = True
            
            if girl.id == "shiori":
                if shiori.flags.cowkini:
                    shiori.flags["giftcosplay_outfit"] = True
        
        if "harmony_event_07" in DONE and "harmony_event_08" not in DONE:
            harm_appts = hero.calendar.find(girl=harmony)
            if harm_appts:
                for day, appt in harm_appts:
                    if appt.name == "Date (Harmony)":
                        hero.calendar.remove(day, appt)
                    if appt.name == "Date at the park (Harmony)":
                        break
                else:
                    DONE.pop("harmony_event_07")
        if "harmony_event_09" in DONE and "harmony_event_10" not in DONE:
            harm_appts = hero.calendar.find(girl=harmony)
            if harm_appts:
                for day, appt in harm_appts:
                    if appt.name == "Date (Harmony)":
                        hero.calendar.remove(day, appt)
                    if appt.name == "Date at the mall (Harmony)":
                        break
                else:
                    DONE.pop("harmony_event_09")
        harmony.love.max = harmony.love.max * 2
        harmony.love = harmony.love * 2


    def update_22_7_0():
        if (
        "alexis_event_08b" in DONE or "alexis_event_09a" in DONE
    ) and alexis.love.max < 200:
            alexis.love.max = 200
        if "alexis_event_07b" in DONE and alexis.love.max < 140:
            alexis.love.max = 140


    def update_22_8_0():
        if "hanna_sub_event_01" in DONE and hanna.sub.max < 75:
            hanna.sub.max = 75


    def update_22_9_0():
        if "bree_sasha_bitches_2" in DONE:
            sasha.flags.walk_outside = True
            bree.flags.walk_outside = True
        if "hanna_event_09" in DONE and hanna.sub.max < 100:
            hanna.sub.max = 100
        if game.flags.BoBDelay:
            game.flags.nextgig = TemporaryFlag(
            game.days_played + FLAGS["HERO!BoBDelay"].duration,
            FLAGS["HERO!BoBDelay"].duration,
        )


    def update_22_10_0():
        
        if "morgan_kleio_threesome" in DONE:
            DONE["morgan_kleio_event_04"] = DONE.pop("morgan_kleio_threesome")
            if not Harem.together("kleio", "morgan", name="pixie"):
                Harem.join_by_name("pixie", "kleio", "morgan")
        
        if "date_set_up" in DONE and not "kleio_and_anna" in DONE:
            DONE.pop("date_set_up")
        
        if "palla_event_03g" in DONE and palla.love.max < 80:
            palla.love.max = 80
        
        if kylie.flags.schedule == "jail":
            kylie.flags.nodate = True
            kylie.flags.noproposedate = True


    def update_22_10_0a():
        if kylie.flags.schedule == "jail":
            Harem.leave_by_name("taming", "kylie")
        
        if "palla_event_04" in DONE and palla.love.max < 120:
            palla.love.max = 80


    def update_22_11_0():
        
        if "anna_event_12" in DONE:
            DONE["anna_event_13"] = DONE.pop("anna_event_12")
        if "anna_event_11" in DONE:
            DONE["anna_event_12"] = DONE.pop("anna_event_11")
        if "anna_event_10" in DONE:
            DONE["anna_event_11"] = DONE.pop("anna_event_10")
        if "anna_getting_serious_02" in DONE:
            DONE["anna_event_10"] = DONE.pop("anna_getting_serious_02")
        if "anna_confession" in DONE:
            DONE["anna_event_09"] = DONE.pop("anna_confession")
        if "anna_getting_serious_01" in DONE:
            DONE["anna_event_08"] = DONE.pop("anna_getting_serious_01")
        if "anna_event_02" in DONE and not anna.flags.horrorMovieDate:
            anna.flags.horrorMovieDate = True
        
        if "anna_sub_event_01" in DONE and anna.sub.max < 80:
            anna.sub.max = 80


    def update_23_1_0():
        if "palla_event_08" in DONE and palla.flags.slavepath:
            palla.sub.max = 100
        
        if "alexis_event_07b" in DONE:
            DONE["alexis_event_08b"] = DONE.pop("alexis_event_07b")
        if "alexis_event_06b" in DONE:
            DONE["alexis_event_07b"] = DONE.pop("alexis_event_06b")
        if "alexis_event_08a" in DONE:
            DONE["alexis_event_09a"] = DONE.pop("alexis_event_08a")
        if "alexis_event_07a" in DONE:
            DONE["alexis_event_08a"] = DONE.pop("alexis_event_07a")
        if "alexis_event_06a" in DONE:
            DONE["alexis_event_07a"] = DONE.pop("alexis_event_06a")
        if "alexis_event_05" in DONE:
            DONE["alexis_event_06"] = DONE.pop("alexis_event_05")
        if "alexis_event_04" in DONE:
            DONE["alexis_event_05"] = DONE.pop("alexis_event_04")
        if "alexis_event_03" in DONE:
            DONE["alexis_event_04"] = DONE["alexis_event_03"]


    def update_23_2_0():
        if "watch_tv_with_everyone_bree" in DONE:
            DONE["watch_tv_with_everyone_female"] = DONE.pop("watch_tv_with_everyone_bree")


    def update_23_3_0():
        if "angela_female_event_01" in DONE:
            angela.unhide()
            angela.flags.schedule = "default_female"
        
        if "bree_event_11" in DONE and not bree.flags.befriendKat:
            bree.flags.befriendKat = True
        
        if "camila_event_08" in DONE and not "camila_event_10" in DONE:
            camila.flags.schedule = "hospital"
        if (
        "camila_event_09" in DONE
        and not "camila_event_10" in DONE
        and camila.flags.schedule == "hospital"
    ):
            camila.flags.hospitaldelay = TemporaryFlag(
            "hospital",
            3,
            hook=[
                hook_set_flag,
                {"girl": camila, "flag": "schedule", "value": "default"},
            ],
        )
        
        if not hasattr(hero, "talk_subjects"):
            hero.talk_subjects = sorted(
            GenericTalkSubject.all(), key=lambda x: x.display_name
        )
        
        if hasattr(hero, "known_talk_subjects") and hero.known_talk_subjects:
            
            renpy.block_rollback()
            tmp_subjects = [
            (
                talk_subject + "_talk"
                if isinstance(talk_subject, basestring)
                and not talk_subject.endswith("_talk")
                else talk_subject
            )
            for talk_subject in hero.known_talk_subjects
        ]
            for talk_subject in hero.talk_subjects:
                if talk_subject.name in tmp_subjects:
                    talk_subject.known = True
            hero.known_talk_subjects = None
        
        if persistent.talk_subjects:
            persistent.talk_subjects = [
            (
                talk_subject + "_talk"
                if not talk_subject.endswith("_talk")
                else talk_subject
            )
            for talk_subject in persistent.talk_subjects
        ]
        
        if "harmony_event_09" in DONE and "harmony_event_10" not in DONE:
            harm_appts = hero.calendar.find(girl=harmony)
            if harm_appts:
                for day, appt in harm_appts:
                    if appt.name == "Date (Harmony)":
                        hero.calendar.remove(day, appt)
                    if appt.name == "Date at the mall (Harmony)":
                        break
                else:
                    DONE.pop("harmony_event_09")
            else:
                DONE.pop("harmony_event_09")


    def update_23_3_0a():
        active_harems_members = [i.active_members for i in HAREMS.values() if i.is_active()]
        for members in active_harems_members:
            for member in members:
                person = Person.find(member)
                if person.flags.nonexclusive != "harem":
                    person.flags.previous_nonexclusive = person.flags.nonexclusive
                    person.flags.nonexclusive = "harem"


    def update_23_4_0():
        if not hasattr(hero, "piercings"):
            if hero.is_male:
                hero_file = "ch/mike/person/mike.yml"
            else:
                hero_file = "ch/bree/person/bree.yml"
            
            with renpy.file(hero_file) as stream:
                hero_yaml = yaml.load(stream, OrderedLoader)
            
            hero.piercings = Piercings(
            "hero", hero_yaml["piercings"] if "piercings" in hero_yaml else {}
        )
        
        if not hasattr(hero, "counters"):
            hero.counters = CountersShortcut(hero.id)
        
        
        for person in Person.all():
            
            if person.love == 0 and person.love.max == 0 and person.hidden:
                person.flags.gone_forever = True
                continue
            for p_attr in person.get_attributes():
                if hasattr(p_attr, "min") and p_attr.val <= p_attr.min:
                    p_attr.val = p_attr.min
                if hasattr(p_attr, "max") and p_attr.val >= p_attr.max:
                    p_attr.val = p_attr.max
        
        if isinstance(hero.birthday, tuple):
            hero.birthday = list(hero.birthday)


    def update_23_4_0f():
        
        Achievement.refresh()


    def update_23_5_0():
        for skill in YAML_SKILLS:
            if YAML_SKILLS[skill].gain_effects and hero.has_skill(skill):
                for skill in YAML_SKILLS[skill].gain_effects:
                    exec(skill)


    def update_23_5_0a():
        if "mike_female_event_01" in DONE:
            DONE.pop("mike_female_event_01")
        if "mike_female_event_03" in DONE:
            DONE.pop("mike_female_event_03")
        if "mike_female_event_04" in DONE:
            DONE.pop("mike_female_event_04")
        if "mike_female_event_05" in DONE:
            DONE.pop("mike_female_event_05")
        if "mike_female_event_06" in DONE:
            DONE.pop("mike_female_event_06")
        
        hero.flags.visited_rooms = set()


    def update_23_5_0c():
        if persistent.skills:
            for skill in YAML_SKILLS:
                if YAML_SKILLS[skill].transferable == False and skill in persistent.skills:
                    del persistent.skills[skill]


    def update_23_6_0():
        persistent.pregnancy_notification = True
        
        if shiori.flags.analSex:
            shiori.flags.analsex = True


    def update_23_6_0a():
        
        for p in Person.all_people(ignore_hidden=False):
            
            if p.flags.giftslutty_dress and p.id not in ["audrey", "minami"]:
                p.flags.giftslutty_dress = False
            
            if p.flags.giftsexy_dress and p.id not in [
            "aletta",
            "alexis",
            "angela",
            "anna",
            "audrey",
            "ayesha",
            "bree",
            "camila",
            "cassidy",
            "emma",
            "hanna",
            "harmony",
            "kleio",
            "kylie",
            "lexi",
            "minami",
            "morgan",
            "palla",
            "samantha",
            "sasha",
            "shiori",
        ]:
                p.flags.giftsexy_dress = False
        
        if kylie.flags.rape == True and kylie.sexperience == 0:
            kylie.sexperience += 1


    def update_23_6_1():
        if not isinstance(hero.flags.visited_rooms, set):
            hero.flags.visited_rooms = set()


    def update_23_6_1c():
        for p in Person.all_people(ignore_hidden=False):
            if p.pregnant:
                p.flags.pregnancies_number += 1
        
        if not game.flags.cheat:
            
            if renpy.has_label("aletta_achievement_3") and (
            renpy.seen_image("aletta ending aletta")
            or renpy.seen_image("aletta ending mike")
            or renpy.seen_image("office ending aletta work")
        ):
                achievement.grant("aletta_3")
            if renpy.has_label("alexis_achievement_3") and renpy.seen_image(
            "alexis ending"
        ):
                achievement.grant("alexis_3")
            if renpy.has_label("anna_achievement_3") and renpy.seen_image("anna ending"):
                achievement.grant("anna_3")
            if renpy.has_label("audrey_achievement_3") and renpy.seen_image(
            "audrey ending fuck"
        ):
                achievement.grant("audrey_3")
            if renpy.has_label("ayesha_achievement_3") and renpy.seen_image(
            "ayesha ending"
        ):
                achievement.grant("ayesha_3")
            if renpy.has_label("bree_achievement_3") and renpy.seen_image(
            "bree ending bree"
        ):
                achievement.grant("bree_3")
            if renpy.has_label("camila_achievement_3") and renpy.seen_image(
            "camila ending"
        ):
                achievement.grant("camila_3")
            if renpy.has_label("cassidy_achievement_3") and renpy.seen_image(
            "cassidy ending"
        ):
                achievement.grant("cassidy_3")
            if renpy.has_label("emma_achievement_3") and renpy.seen_image("emma ending"):
                achievement.grant("emma_3")
            if renpy.has_label("hanna_achievement_3") and renpy.seen_image(
            "hanna gym ending"
        ):
                achievement.grant("hanna_3")
            if renpy.has_label("harmony_achievement_3") and renpy.seen_image(
            "harmony ending church"
        ):
                achievement.grant("harmony_3")
            if renpy.has_label("kleio_achievement_3") and renpy.seen_image("kleio ending"):
                achievement.grant("kleio_3")
            if renpy.has_label("kylie_achievement_5") and renpy.seen_image("kylie ending"):
                achievement.grant("kylie_5")
            if renpy.has_label("lavish_achievement_3") and renpy.seen_image(
            "lavish ending"
        ):
                achievement.grant("lavish_3")
            if renpy.has_label("lexi_achievement_3") and (
            renpy.seen_image("lexi ending") or renpy.seen_image("lexi ending2")
        ):
                achievement.grant("lexi_3")
            if renpy.has_label("lexi_achievement_5") and "date_lexi_meet_jack_4" in DONE:
                achievement.grant("lexi_5")
            if renpy.has_label("minami_achievement_3") and renpy.seen_image(
            "minami ending"
        ):
                achievement.grant("minami_3")
            if renpy.has_label("morgan_achievement_3") and (
            renpy.seen_image("morgan househusband ending")
            or renpy.seen_image("morgan housewife ending")
            or renpy.seen_image("morgan ending")
        ):
                achievement.grant("morgan_3")
            if renpy.has_label("palla_achievement_3") and (
            renpy.seen_image("palla pornstar ending")
            or renpy.seen_image("palla model ending")
        ):
                achievement.grant("palla_3")
            if renpy.has_label("palla_achievement_5") and "palla_find_pallapoundin" in DONE:
                achievement.grant("palla_5")
            if renpy.has_label("samantha_achievement_3") and renpy.seen_image(
            "samantha ending"
        ):
                achievement.grant("samantha_3")
            if renpy.has_label("samantha_achievement_5") and "samantha_event_D03" in DONE:
                achievement.grant("samantha_5")
            if renpy.has_label("sasha_achievement_3") and renpy.seen_image(
            "bree ending sasha"
        ):
                achievement.grant("sasha_3")
            if renpy.has_label("shiori_achievement_3") and renpy.seen_image(
            "shiori ending"
        ):
                achievement.grant("shiori_3")
            
            
            if renpy.has_label("band_harem_achievement_2") and renpy.seen_image(
            "band threesome anna suck kleio_pleasure finger vaginal"
        ):
                achievement.grant("band_harem_2")
            if renpy.has_label("band_harem_achievement_3") and renpy.seen_image("picnic"):
                achievement.grant("band_harem_3")
            if renpy.has_label("band_harem_achievement_5") and renpy.seen_image(
            "band foursome"
        ):
                achievement.grant("band_harem_5")
            if renpy.has_label("band_harem_achievement_6") and renpy.seen_image("bus_tour"):
                achievement.grant("band_harem_6")
            if renpy.has_label("bitchy_harem_achievement_2") and renpy.seen_image(
            "bitchy threesome pallafuck strapon pallaclosed"
        ):
                achievement.grant("bitchy_harem_2")
            if renpy.has_label("bitchy_harem_achievement_3") and renpy.seen_image(
            "bitchy harem ending audrey palla"
        ):
                achievement.grant("bitchy_harem_3")
            if (
            renpy.has_label("bitchy_harem_achievement_5")
            and "bitchy_harem_nightclub_encounter" in DONE
        ):
                achievement.grant("bitchy_harem_5")
            if renpy.has_label("bitchy_harem_achievement_6") and renpy.seen_image(
            "bitchy harem ending audrey cassidy palla"
        ):
                achievement.grant("bitchy_harem_6")
            if (
            renpy.has_label("college_harem_achievement_2")
            and "science_project_03" in DONE
        ):
                achievement.grant("college_harem_2")
            if renpy.has_label("criminal_harem_achievement_3") and renpy.seen_image(
            "criminal harem ending"
        ):
                achievement.grant("criminal_harem_3")
            if renpy.has_label("fashion_harem_achievement_2") and renpy.seen_image(
            "fashion doggy mike"
        ):
                achievement.grant("fashion_harem_2")
            if renpy.has_label("friendly_harem_achievement_2") and (
            renpy.seen_image("friendly harem cowgirl")
            or renpy.seen_image("friendly harem doggy")
        ):
                achievement.grant("friendly_harem_2")
            if renpy.has_label("home_harem_achievement_2") and (
            renpy.seen_image("couch fun bree sasha")
            or renpy.seen_image("bj breesasha bree sasha sashaopen")
            or renpy.seen_image("bree rough oral bedroom naked")
            or renpy.seen_image("bree doggy sasha front")
            or renpy.seen_image("threesome breesasha")
            or renpy.seen_image("shower bj breesasha bree sasha")
        ):
                achievement.grant("home_harem_2")
            if renpy.has_label("home_harem_achievement_3") and renpy.seen_image(
            "bree ending bree sasha"
        ):
                achievement.grant("home_harem_3")
            if renpy.has_label("home_harem_achievement_7") and renpy.seen_image(
            "home ending bree lexi minami samantha sasha"
        ):
                achievement.grant("home_harem_7")
            if renpy.has_label("jealous_harem_achievement_2") and renpy.seen_image(
            "jealous missionary kiss"
        ):
                achievement.grant("jealous_harem_2")
            if renpy.has_label("office_harem_achievement_2") and renpy.seen_image(
            "office fivesome alettafuck audrey lavish shiori"
        ):
                achievement.grant("office_harem_2")
            if renpy.has_label("office_harem_achievement_3") and renpy.seen_image(
            "office ending aletta audrey lavish shiori work"
        ):
                achievement.grant("office_harem_3")
            if renpy.has_label("office_harem_achievement_4") and (
            renpy.seen_image("office aletta foursome ahegao")
            or renpy.seen_image("office audrey foursome ahegao")
            or renpy.seen_image("office lavish foursome ahegao")
            or renpy.seen_image("office shiori foursome ahegao")
            or renpy.seen_image("office sixsome lavishahegao")
        ):
                achievement.grant("office_harem_4")
            if renpy.has_label("pixie_harem_achievement_2") and renpy.seen_image(
            "kleio morgan threesome out"
        ):
                achievement.grant("pixie_harem_2")
            if renpy.has_label("pixie_harem_achievement_3") and renpy.seen_image(
            "pixie ending"
        ):
                achievement.grant("pixie_harem_3")
            if renpy.has_label("sporty_harem_achievement_2") and renpy.seen_image(
            "sporty blowjob"
        ):
                achievement.grant("sporty_harem_2")
            if renpy.has_label("sporty_harem_achievement_3") and renpy.seen_image(
            "sporty harem ending"
        ):
                achievement.grant("sporty_harem_3")
            if renpy.has_label("taming_harem_achievement_2") and (
            renpy.seen_image("taming threesome") or renpy.seen_image("taming blowjob")
        ):
                achievement.grant("taming_harem_2")
            if renpy.has_label("taming_harem_achievement_3") and renpy.seen_image(
            "taming harem ending"
        ):
                achievement.grant("taming_harem_3")
            
            
            if renpy.has_label("shark_achievement_1") and renpy.seen_image("shark attack"):
                achievement.grant("shark_1")
            if renpy.has_label("bear_achievement_1") and renpy.seen_image("bear attack"):
                achievement.grant("bear_1")
            if (
            renpy.has_label("battle_of_bands_achievement_1")
            and "battle_of_the_bands_round_two" in DONE
            and BOB_SCORE >= 100
        ):
                achievement.grant("battle_of_bands_1")
            if renpy.has_label("cherie_achievement_0") and renpy.seen_image(
            "cherie stand limp"
        ):
                achievement.grant("cherie_0")
            if renpy.has_label("gaming_harem_achievement_2") and (
            renpy.seen_image("bree kat cowgirl")
            or renpy.seen_image("bree kat rev cowgirl")
        ):
                achievement.grant("gaming_harem_2")
            if renpy.has_label("kiara_achievement_0") and renpy.seen_image(
            "kiara maidcafe blowjob"
        ):
                achievement.grant("kiara_0")
            if renpy.has_label("natalie_achievement_1") and renpy.seen_image(
            "samantha threesome2"
        ):
                achievement.grant("natalie_1")
            if (
            renpy.has_label("scottie_achievement_1")
            and "sasha_scottie_threesome" in DONE
        ):
                achievement.grant("scottie_1")
            if renpy.has_label("violaine_achievement_1") and renpy.seen_image(
            "violaine vincent 3some mike"
        ):
                achievement.grant("violaine_1")
            
            achievement.sync()


    def update_23_6_1d():
        def equip_bug():
            for equip in hero.equipment:
                hero.equipment[equip] = None
        
        if hero.charm.max > 120:
            equip_bug()
            hero.charm.max = 100
        
        if hero.fitness.max > 115:
            equip_bug()
            hero.fitness.max = 100
        
        if hero.knowledge.max > 110:
            equip_bug()
            hero.fitness.max = 100


    def update_23_7_0():
        
        if (
        Harem.together("camila", "lexi", name="criminal")
        and game.flags.CriminalRequest == 1
    ):
            if "criminal_harem_event_03" in DONE:
                game.flags.CriminalRequest = 3
            elif "criminal_harem_event_02" in DONE:
                game.flags.CriminalRequest = 2
        
        
        if "criminal_harem_event_02" in DONE and not game.flags.CriminalRequest == 2:
            game.flags.CriminalRequest = "lie"


    def update_23_8_0():
        if "lavish_spanking_start" in DONE:
            lavish.flags.start_spanking = True
        if "audrey_spanking_start" in DONE:
            audrey.flags.start_spanking = True
        if shiori.flags.spanking > 0:
            shiori.flags.spank_counter = shiori.flags.spanking
            shiori.flags.start_spanking = True
        
        if "jack_female_event_05_bis" in DONE:
            jack.flags.nodate = False
        
        
        if (
        "samantha_wedding_baby" in DONE
        and samantha.flags.post_wedding_baby_talk_delay
        and samantha.counters.pregnant < 50
        and not samantha.flags.reset_post_wedding_baby_talk_delay
    ):
            DONE.pop("samantha_wedding_baby", None)
            samantha.flags.post_wedding_baby_talk_delay = TemporaryFlag(True, 30)
            samantha.flags.reset_post_wedding_baby_talk_delay = True


    def update_23_9_0():
        
        if "bree_event_12b" in DONE:
            game.flags.kiara_bj = True
        
        if samantha.flags.ryancheats:
            hero.flags.knows_ryancheats = True
        if "samantha_event_05" in DONE and hero.flags.knows_ryancheats:
            samantha.flags.knows_ryancheats = True
        if "samantha_event_05" not in DONE and samantha.flags.storyB == 1:
            wedding_day = game.calendar.get_next_day_of_week("sunday")
            hero.calendar.add(
            wedding_day,
            LabelAppointment(
                (12, 20), [], "Sam and Ryan's wedding", "samantha_event_B01"
            ),
        )
        if "samantha_preg_talk_ryan" in DONE and samantha.flags.storyD >= 1:
            samantha.flags.knows_ryancheats = True
        if samantha.flags.storyD >= 1:
            samantha.flags.knows_ryancheats = True
            samantha.flags.cuck_ryan = True
        if "samantha_event_B03" in DONE:
            samantha.flags.cuck_ryan = True
        
        if kylie.flags.AssaultVideo:
            kylie.flags.assault_video = True
        
        hero.counters = CountersShortcut(hero.id)


    def update_23_9_0c():
        if samantha.flags.storyC == 3:
            game.flags.sam_ryan_threesome = True


    def update_23_10_0():
        if hero.flags.vehicule_in_garage:
            hero.flags.vehicle_in_garage = hero.flags.vehicule_in_garage
        if alexis.flags.talkFlirt:
            alexis.flags.ntr_conversation = "flirt"
        if alexis.flags.talkCheat:
            alexis.flags.ntr_conversation = "cheat"
        if alexis.flags.talkLeave:
            alexis.flags.ntr_conversation = "leave"
        if "best_customer_service" in DONE:
            Harem.join_by_name("fashion", "palla", "sasha")


    def update_23_10_0a():
        if sasha.flags.cheated == 1:
            sasha.flags.cheated = True


    def update_23_11_0():
        if palla.flags.minealone:
            palla.flags.minealone = True
        if "kylie_investigation_2" in DONE and not kylie.flags.arrest:
            DONE.pop("kylie_investigation_2")
        if anna.flags.anal_experience and not anna.flags.anal:
            anna.flags.anal = anna.flags.anal_experience
        if shiori.flags.analsex and not shiori.flags.anal:
            shiori.flags.anal = 1
        if "dwayne_female_event_01" in DONE and dwayne.hidden:
            dwayne.unhide()


    def update_23_11_0a():
        if not Harem.find(samantha, name="home") and not samantha.is_gone_forever:
            if (
            "samantha_event_A04" in DONE
            and samantha.flags.nonexclusive
            and samantha.sexperience >= 1
            and Harem.find(sasha, name="home")
        ):
                if game.flags.ongoinghomeharem not in ["samantha", "lexi", "minami"]:
                    game.flags.ongoinghomeharem = "samantha"
        if "alexis_ntr_conversation" not in DONE and alexis.flags.conversation_event in [
        "flirt",
        "cheat",
        "leave",
    ]:
            alexis.flags.ntr_conversation = alexis.flags.conversation_event
            if alexis.flags.ntr_conversation == "flirt":
                alexis.flags.conversation_event = "restaurant"
            else:
                alexis.flags.conversation_event = "cinema"


    def update_24_1_0():
        if "cassidy_dwayne_denoument" in DONE:
            DONE["cassidy_dwayne_denouement"] = DONE["cassidy_dwayne_denoument"]
        
        if game.flags.job:
            if game.flags.job in [
            "church",
            "bakery",
            "bedroom4",
            "bookstore",
            "clothesshop",
            "coffeeshop",
            "electronic",
            "flowershop",
            "gym",
            "homelessshelter",
            "jewelrystore",
            "maidcafe",
            "model",
            "pornstar",
            "prostitute",
        ]:
                game.flags.job_day = game.flags.job
            else:
                game.flags.job_night = game.flags.job
        
        if Person.find("amy") and Person.find("amy").flags.amydelay:
            FLAGS.pop("amyamydelay")
            Person.find("amy").flags.amydelay = TemporaryFlag(True, 1)
        
        if (
        "bree_event_11" in DONE
        and bree.flags.meetthyra
        and "fafow" in DLCS
        and Person.find("kat")
    ):
            kat.unhide()
        
        if "bree_kat_threesome" in DONE and "fafow" in DLCS and Person.find("kat"):
            DONE["gaming_harem_event_01"] = DONE["bree_kat_threesome"]
            DONE["gaming_harem_event_02"] = DONE["bree_kat_threesome"]
            Harem.join_by_name("gaming", "kat", "bree")


    def update_24_3_0():
        if "kat_kink_01" in DONE and kat.sub.max < 20:
            kat.sub.max = 20
        
        if (
        not game.flags.band
        and "kleio_event_04" in DONE
        and all(event not in DONE for event in ["kleio_event_05b", "kleio_event_05c"])
    ):
            hero.gain_item(hero.flags.vehicle_in_garage)


    def update_24_4_0():
        if "amy_event_09" in DONE and amy.hidden:
            amy.unhide()


    def update_24_4_0a():
        if "amy" in hero.smartphone_contacts and "fafow" not in DLCS:
            hero.smartphone_contacts.remove("amy")


    def update_24_5_0():
        if Person.find("kleio") and kleio.flags.sluttydate_gifted:
            kleio.flags.sluttydate_gifted = False
            kleio.flags["giftslutty_dress"] = False


    def update_24_6_0a():
        if "reona_enough_study" in DONE and "reona_event_02" in DONE and not reona.flags.study_blow:
            reona.flags.study_blow = True

    def update_24_7_0():
        if "harmony_lexi_showdown" in DONE and (Person.find("harmony") and not Person.find("harmony").flags.gone_forever) and (Person.find("lexi") and not Person.find("lexi").flags.gone_forever):
            Harem.join_by_name("goodevil", "harmony", "lexi")
        
        if hasattr(persistent, "randomness"):
            if persistent.randomness == 2:
                persistent.schedule_randomness = True
                persistent.needs_randomness = True
            elif persistent.randomness == 1:
                persistent.schedule_randomness = True
                persistent.needs_randomness = False
            else:
                persistent.schedule_randomness = persistent.needs_randomness = False
        
        
        if hero.gender == 'male':
            if Person.find('minami'):
                minami.family_name = hero.family_name
            if Person.find('angela'):
                angela.family_name = hero.family_name
                angela.flags.status = angela.status.replace("Mike", hero.name)
            if Person.find('dwayne'):
                dwayne.flags.status = dwayne.status.replace("Mike", hero.name)
            if Person.find('ryan'):
                ryan.flags.status = ryan.status.replace("Mike", hero.name)
        else:
            if Person.find('minami'):
                minami.family_name = mike.family_name
            if Person.find('angela'):
                angela.family_name = mike.family_name
                angela.flags.status = angela.status.replace("Mike", mike.name)
            if Person.find('dwayne'):
                dwayne.flags.status = dwayne.status.replace("Mike", mike.name)
            if Person.find('ryan'):
                ryan.flags.status = ryan.status.replace("Mike", mike.name)

    def update_24_7_0d():
        appointments = copy.deepcopy(hero.calendar.appointments)
        for day_appointment in appointments:
            updated_appointments = []
            for appointment in appointments[day_appointment]:
                if hasattr(appointment, "label"):
                    appointment_label = appointment.label
                else:
                    appointment_label = appointment.name
                if hasattr(appointment, "fail_label"):
                    fail_label = appointment.fail_label
                else:
                    fail_label = None
                
                if isinstance(appointment, DateAppointment):
                    new_appointment = DateAppointment(appointment.hours, appointment.participants, appointment.name, appointment_label, fail_label)
                    updated_appointments.append(new_appointment)
                
                elif isinstance(appointment, NoDateEvent):
                    new_appointment = NoDateEvent()
                    updated_appointments.append(new_appointment)
                
                elif isinstance(appointment, ReminderAppointment):
                    if appointment.name == "Attend Kylie's trial":
                        new_appointment = LabelAppointment(appointment.hours, [], appointment.name, appointment_label, "kylie_trial_2_missed")
                        updated_appointments.append(new_appointment)
                    elif appointment.name == "Attend Kylie's execution":
                        new_appointment = LabelAppointment(appointment.hours, [], appointment.name, appointment_label, "kylie_trial_3_missed")
                        updated_appointments.append(new_appointment)
                else:
                    updated_appointments.append(appointment)
            hero.calendar.appointments[day_appointment] = updated_appointments
        
        
        if game.active_date:
            game.active_date.skip_nightclub = False
        
        
        for npc in Person.all_people(ignore_hidden=False):
            if npc.flags.lastdate:
                npc.flags.last_date_location = npc.flags.lastdate
            if npc.flags.last_date:
                npc.flags.last_date_day = npc.flags.last_date

    def update_24_8_0():
        if "bree_shower_BJ" in DONE:
            sasha.flags.showerbj = True

    def update_24_8_0b():
        emma_appts = hero.calendar.find(girl="emma")
        if emma_appts and any(isinstance(emma_appt, ScavengerHuntAppointment) for _, emma_appt in emma_appts):
            for appt_day, emma_appt in emma_appts:
                if isinstance(emma_appt, ScavengerHuntAppointment) and emma_appt.start_location == "emma_event_06_missed":
                    emma_appt.start_location = "street"
                    emma_appt.fail_label = "emma_event_06_missed"
        
        if "samantha_event_A01" in DONE and "samantha_event_A02" in DONE and not samantha.flags.gone_forever and samantha.hidden:
            samantha.unhide()
            samantha.flags.cuck_ryan = True
        
        if persistent.skills:
            for skill in YAML_SKILLS:
                if YAML_SKILLS[skill].transferable == False and skill in persistent.skills:
                    del persistent.skills[skill]

    def update_24_9_0():
        if "master_training_female_event_05" in DONE and hero.flags.master_training != False:
            hero.calendar.add(game.days_played + 1, LabelAppointment(10, ["Master"], "Meet the master for the final lesson", "master_training_female_event_06", "master_training_female_event_missed"))
        
        if "angela_female_event_09" in DONE and "angela_female_event_10" not in DONE:
            DONE.pop("angela_female_event_09")

    def update_24_9_1():
        
        if not game.flags.cheat:
            if renpy.has_label("criminal_harem_achievement_2") and renpy.seen_label(
            "camila_lexi_threesome_fuck"
        ):
                achievement.grant("criminal_harem_2")
            if renpy.has_label("friendly_harem_achievement_3") and renpy.seen_label(
            "emma_samantha_ending"
        ):
                achievement.grant("friendly_harem_3")
        
        
        
        if not game.flags.cheat:
            if renpy.has_label("gaming_harem_achievement_2") and (
            renpy.seen_image("bree kat cowgirl")
            or renpy.seen_image("bree kat rev cowgirl")
        ):
                achievement.grant("gaming_harem_2")
        
        achievement.sync()

    def update_24_9_1b():
        achievement.sync()
        if hero.calendar.find(girl="alexis", label="alexis_event_11"):
            dates_appointments = [i for i in hero.calendar.find(girl="alexis", label="alexis_event_11") and isinstance(i[1], DateAppointment)]
            for day, appointment_object in dates_appointments:
                hero.calendar.add(day, LabelAppointment(16, "alexis", "High School Reunion (Alexis)", "alexis_event_11", "missed_alexis_event_11"))
                hero.calendar.remove(day, appointment_object)
        
        if 'fafow' in DLCS:
            if "amy_teaser" in DONE and Person.find('amy'):
                amy.unhide()
            if 'bree_event_11' in DONE and Person.find('kat'):
                kat.unhide()

    def update_24_9_1c():
        if 'fafow' in DLCS:
            
            
            
            if not game.flags.cheat and kat.flags.kiss >= 1:
                kat_achievement_1.grant()
            
            
            for p in [amy, kat, reona]:
                if p.flags.giftslutty_dress:
                    p.flags.giftslutty_dress = False
                    p.flags.sluttydate = False
            
            
            if not 'band_harem_amy_event_07' in DONE:
                if 'band_harem_amy_event_02' in DONE and not (amy.flags.peace_with_kleio or amy.flags.possible_peace_with_kleio):
                    amy.flags.possible_peace_with_kleio = True
                if 'band_harem_amy_event_04' in DONE and not (amy.flags.peace_with_anna or amy.flags.possible_peace_with_anna):
                    amy.flags.possible_peace_with_anna = True
                if 'band_harem_amy_event_06' in DONE and not (amy.flags.peace_with_sasha or amy.flags.possible_peace_with_sasha):
                    amy.flags.possible_peace_with_sasha = True

    def update_24_9_1d():
        if 'hanna_gym_profits' in DONE:
            if not hanna.flags.repay and not hanna.flags.repay_delay:
                hero.money += 1000
                hanna.flags.repay += 1
                hanna.flags.repay_delay = TemporaryFlag(True, max(1, 30 - (game.days_played - DONE.get('hanna_gym_profits'))))
                if 'hanna_gym_profits_pay' in DONE:
                    DONE.pop('hanna_gym_profits_pay')

    def update_24_10_0():
        if 'amy_event_07' in DONE and 'amy_event_07_date' not in DONE and not hero.calendar.find(label="amy_event_07_date"):
            DONE.pop('amy_event_07')
        if 'alexis_event_10' in DONE and 'alexis_event_11' not in DONE and not hero.calendar.find(label="alexis_event_11"):
            DONE.pop('alexis_event_10')
        if "angela_female_event_12a" in DONE:
            DONE.pop('angela_female_event_12a')
        if 'lexi_female_event_04' in DONE or 'lexi_female_event_04b' in DONE:
            lexi.flags.nodate = False
            lexi.flags.nokiss = False

    def update_24_10_0a():
        if "danny_female_event_04" in DONE:
            danny.flags.nokiss = False
            danny.flags.nodate = False
        if "dwayne_female_event_03" in DONE:
            dwayne.flags.nokiss = False
            dwayne.flags.nodate = False

    def update_24_11_0b():
        if "hanna_gym_profits" in DONE and hanna.love.max < 160:
            hanna.love.max = 160

    def update_25_1_0():
        if 'fafow' in DLCS:
            if Harem.together("lexi", "reona", name='whore'):
                if ("whore_harem_event_06" not in DONE and "whore_harem_event_07" not in DONE ) or ("whore_harem_event_06" in DONE and "whore_harem_event_07" in DONE and hero.flags.agree_whore_trouple is False):
                    Harem.leave_by_name("whore", "lexi", "reona")
                    hero.flags.whore_nudist_beach = True

    def update_25_1_0b():
        if 'fafow' in DLCS:
            if "thot_harem_event_04" in DONE:
                Harem.join_by_name("thot", "alexis")

    def update_25_2_0():
        if hasattr(store, "DLCS") and isinstance(store.DLCS, list):
            DLCS = {dlc_name: config.version for dlc_name in DLCS}
        if hasattr(store, "DLCS") and 'fafow' in store.DLCS:
            if "amy_event_06" in DONE and amy.love.max < 140:
                amy.love.max = 140
        if hasattr(store, "DLCS") and 'breemc' in store.DLCS:
            if "shawn_female_event_03" in DONE:
                if shawn.love.max < 60:
                    shawn.love.max = 60
                shawn.flags.nodate = False
                shawn.flags.nokiss = False

    def update_25_3_0():
        if hasattr(store, "DLCS") and 'fafow' in store.DLCS:
            if "kat_jack_06" in DONE and kat.flags.agree_kat_jack_threesome is True and not Harem.together("jack", "kat", name='exclusive_fan'):
                Harem.join_by_name("exclusive_fan", "jack", "kat")
            if "kat_jack_07" in DONE and (not kat.flags.mike_pleased or not kat.flags.jack_pleased):
                kat.flags.mike_pleased += 1
                kat.flags.jack_pleased += 1
            if "electronic_harem_event_05" in DONE and renpy.seen_image("electronic 3some mikeamydoggy"):
                achievement.grant("electronic_harem_1")
            if "electronic_harem_event_09" in DONE and (renpy.seen_image("electronic 4some fuckamy") or renpy.seen_image("electronic 4some fuckpalla")):
                achievement.grant("electronic_harem_2")
            if "goth_harem_event_01" in DONE and (renpy.seen_image("goth 3some violainefuck") or renpy.seen_image("goth 3some amyfuck mike")):
                achievement.grant("goth_harem_1")
            if "goth_harem_event_03" in DONE and renpy.seen_image("goth 4some bj amy violaine"):
                achievement.grant("goth_harem_3")
            if "petite_harem_event_04_sex" in DONE:
                achievement.grant("petite_harem_2")
            if "thot_harem_event_04" in DONE and renpy.seen_image("thot 3some handjob"):
                achievement.grant("thot_harem_2")
            if "thot_harem_event_06" in DONE and renpy.seen_image("thot 4some foreplay audrey"):
                achievement.grant("thot_harem_5")
        if "dwayne_job_offer_female" in DONE:
            day_job_offer = DONE.pop("dwayne_job_offer_female")
            DONE["dwayne_female_event_05"] = day_job_offer
            if dwayne.love.max < 100:
                dwayne.love.max = 100
        if not Harem.find(samantha, name="home") and not samantha.is_gone_forever:
            if (
            "samantha_event_A04" in DONE
            and samantha.flags.nonexclusive
            and samantha.sexperience >= 1
            and Harem.find(sasha, name="home")
        ):
                if game.flags.ongoinghomeharem not in ["samantha", "lexi", "minami"]:
                    game.flags.ongoinghomeharem = "samantha"

    def update_25_3_0c():
        emma_appointment = hero.calendar.find(label="emma_event_03_appointment")
        if emma_appointment:
            emma_appointment[0][1].participants = ["samantha"]
        if "amy_event_03" in DONE and Room.find("electronic").hidden:
            hero.flags.electronic_ban = TemporaryFlag(True, 15, hook=Room.find("electronic").unhide)

    def update_25_4_0b():
        if hasattr(store, "DLCS") and 'fafow' in store.DLCS:
            if len([g for g in [anna, kleio, sasha] if g.flags.amy_accepted]) >= 2 and Harem.find_by_name("band"):
                Harem.join_by_name("band", "amy")
        if game.flags.party_planned and game.season != 2:
            game.flags.party_planned = False

    def update_25_5_0():
        if hasattr(store, "DLCS") and 'fafow' in store.DLCS:
            if "mike_female_event_12a" in DONE and mike.love.max < 200:
                mike.love.max = 200

    def update_25_6_0b():
        if hasattr(store, "DLCS") and 'fafwm' not in store.DLCS and Person.find("cherie"):
            cherie.hide()
        
        
        for i in ["cheriehelping", "cheriemissed", "cherievault", "cheriedwayneconfrontation", "cheriecheriecall", "cheriepromisednotalone", "cheriepromisedsex"]:
            if i in FLAGS:
                game_flag = i.replace('cherie', "HERO!cherie_", 1)
                FLAGS[game_flag] = copy.deepcopy(FLAGS[i])
                del(FLAGS[i])
        
        
        for i in ["cherievaultDelay", "cherieceooffer", "cheriecheriecallDelay", "cheriedwayneDelay"]:
            if i in FLAGS:
                game_flag = i.lower().replace('cherie', "HERO!cherie_", 1)
                temporary_flag = copy.deepcopy(FLAGS[i])
                if temporary_flag.hook:
                    hook_definition = temporary_flag.hook[1]
                    hook_definition['girl'] = game
                    hook_definition['flag'] = f"cherie_{hook_definition['flag']}"
                    temporary_flag.hook[1] = hook_definition
                FLAGS[game_flag] = temporary_flag
                del(FLAGS[i])

    def update_25_8_0():
        if harmony.love.max >= 150:
            if "harmony_event_01_vanilla" in DONE and "harmony_event_02_vanilla" not in DONE:
                DONE["harmony_event_02_vanilla"] = DONE["harmony_event_01_vanilla"] + 1
            if "harmony_event_01_slutty" in DONE and "harmony_event_02_slutty" not in DONE:
                DONE["harmony_event_02_slutty"] = DONE["harmony_event_01_slutty"] + 1
        if harmony.love.max >= 170:
            if "harmony_event_03_vanilla" in DONE and "harmony_event_04_vanilla" not in DONE:
                DONE["harmony_event_04_vanilla"] = DONE["harmony_event_03_vanilla"] + 1
            if "harmony_event_01_religious" in DONE and "harmony_event_02_religious" not in DONE:
                DONE["harmony_event_02_religious"] = DONE["harmony_event_01_religious"] + 1

    def update_25_9_0():
        if "bree_stripclub_intro" in DONE and bree.flags.work_stripclub not in [True, False]:
            bree.flags.work_stripclub = True
        if hasattr(store, "DLCS") and 'breemc' in store.DLCS:
            if "master_female_event_01" in DONE:
                DONE["master_female_meet_event_01"] = DONE.pop("master_female_event_01")
            if "master_female_event_02" in DONE:
                DONE["master_female_meet_event_02"] = DONE.pop("master_female_event_02")

    def update_25_10_0a():
        print("update_25_10_0a")
        if hasattr(store, "DLCS") and 'breemc' in store.DLCS:
            print("Has breemc dlc")
            if "kylie_female_event_01" in DONE:
                kylie.unhide()
            
            if hero.flags.master_training and "master_training_female_event_01" not in DONE and not hero.calendar.find(label="master_training_female_event_01"):
                print("adding label event 01")
                hero.calendar.add(game.days_played + 1, LabelAppointment(10, [], "Meet the master for my first lesson", "master_training_female_event_01", "master_training_female_event_missed"))
            elif hero.flags.master_training and "master_training_female_event_01" in DONE and "master_training_female_event_02" not in DONE and not hero.calendar.find(label="master_training_female_event_02"):
                print("adding label event 02")
                hero.calendar.add(game.days_played + 1, LabelAppointment(10, [], "Meet the master for the second lesson", "master_training_female_event_02", "master_training_female_event_missed"))
            elif hero.flags.master_training and "master_training_female_event_02" in DONE and "master_training_female_event_03" not in DONE and not hero.calendar.find(label="master_training_female_event_03"):
                print("adding label event 03")
                hero.calendar.add(game.days_played + 1, LabelAppointment(10, [], "Meet the master for the third lesson", "master_training_female_event_03", "master_training_female_event_missed"))
            elif hero.flags.master_training and "master_training_female_event_03" in DONE and "master_training_female_event_04" not in DONE and not hero.calendar.find(label="master_training_female_event_04"):
                print("adding label event 04")
                hero.calendar.add(game.days_played + 1, LabelAppointment(10, [], "Meet the master for the fourth lesson", "master_training_female_event_04", "master_training_female_event_missed"))
            elif hero.flags.master_training and "master_training_female_event_04" in DONE and "master_training_female_event_05" not in DONE and not hero.calendar.find(label="master_training_female_event_05"):
                print("adding label event 05")
                hero.calendar.add(game.days_played + 1, LabelAppointment(10, [], "Meet the master for the fifth lesson", "master_training_female_event_05", "master_training_female_event_missed"))
            elif hero.flags.master_training and "master_training_female_event_05" in DONE and "master_training_female_event_06" not in DONE and not hero.calendar.find(label="master_training_female_event_06"):
                print("adding label event final")
                hero.calendar.add(game.days_played + 1, LabelAppointment(10, [], "Meet the master for the final lesson", "master_training_female_event_06", "master_training_female_event_missed"))
            
        
        for p in ('angela', 'dwayne', 'jack', 'ryan'):
            person = Person.find(p)
            if person:
                if "[hero.name]" in person.status:
                    person.status = person.status.replace("[hero.name]", hero.name)
                elif "[bree.name]" in person.status:
                    if hero.gender == "female":
                        person.status = person.status.replace("[bree.name]", hero.name)
                    elif Person.find("bree"):
                        person.status = person.status.replace("[bree.name]", bree.name)
                elif "[mike.name]" in person.status:
                    if hero.gender == "male":
                        person.status = person.status.replace("[mike.name]", hero.name)
                    elif Person.find("mike"):
                        person.status = person.status.replace("[mike.name]", mike.name)

    def update_26_1_0():
        if Person.find("reona"):
            if reona.purity < 10:
                reona.flags.sluttydate = True if reona.flags.giftslutty_dress else False
                reona.flags.sexydate = False
                reona.flags.puredate = False
            elif reona.purity < 20:
                reona.flags.sluttydate = False
                reona.flags.sexydate = True if reona.flags.giftsexy_dress else False
                reona.flags.puredate = False
                if reona.sub >= 50:
                    reona.flags.sexyunderwear = True if reona.flags.giftlingerie else False
            elif reona.purity >= 60:
                reona.flags.sluttydate = False
                reona.flags.sexydate = False
                reona.flags.puredate = True if reona.flags.giftpure_date else False
            if reona.purity >= 50:
                reona.flags.purecasual = True if reona.flags.giftpure_casual else False

    def update_26_1_0a():
        if "claire_event_03" in DONE:
            claire.flags.nokiss = False
            claire.flags.nodate = False
        if "kiara_event_03" in DONE:
            kiara.flags.nokiss = False
            kiara.flags.nodate = False

    def update_26_1_0b():
        if "purity_harem_event_03" in DONE:
            Harem.join_by_name("purity", "harmony", "reona")

    def update_26_1_0c():
        
        if renpy.has_label("cherie_achievement_0") and not achievement.has("cherie_0"):
            achievement.clear("cherie_1")
            if not game.flags.cheat and renpy.seen_image("cherie stand limp"):
                achievement.grant("cherie_0")
        
        if not game.flags.cheat and renpy.has_label("cherie_achievement_1") and cherie.flags.kiss >= 1:
            achievement.grant("cherie_1")
        
        if renpy.has_label("kiara_achievement_0") and not achievement.has("kiara_0"):
            achievement.clear("kiara_1")
            if not game.flags.cheat and renpy.seen_image("kiara maidcafe blowjob"):
                achievement.grant("kiara_0")
        
        if not game.flags.cheat and renpy.has_label("kiara_achievement_1") and kiara.flags.kiss >= 1:
            achievement.grant("kiara_1")
        if "claire_event_03" in DONE:
            claire.flags.nokiss = False
            claire.flags.nodate = False
        if "kiara_event_03" in DONE:
            kiara.flags.nokiss = False
            kiara.flags.nodate = False

    def update_26_2_0():
        
        if "reona_jack_04a" in DONE and "reona_jack_05a" not in DONE:
            reona.unhide()
        
        
        for npc in Person.all_people(False):
            if npc.id != "reona":
                npc.flags.giftpure_casual = False
                npc.flags.purecasual = 0
                npc.flags.giftpure_date = False
                npc.flags.puredate = 0
                npc.flags.giftlingerie = False
                npc.flags.sexyunderwear = 0
        if claire.flags.dwaynedeath_truth:
            cherie.flags.dwaynedeath_truth
        if claire.flags.dwaynedeath_partialtruth:
            cherie.flags.dwaynedeath_partialtruth
        if claire.flags.dwaynedeath_dwaynegone:
            cherie.flags.dwaynedeath_dwaynegone
        if claire.flags.dwaynedeath_claireknife:
            cherie.flags.dwaynedeath_cherieknife
        if claire.flags.dwaynedeath_mikeselfdefense:
            cherie.flags.dwaynedeath_mikeselfdefense
        
        if game.flags.dwaynefired:
            game.flags.dwaynefired = False

    def update_26_3_0():
        if "dump_dwayne_corpse_mansion" in DONE:
            hero.flags.dwayne_corpse = "mansion"
        if "dump_dwayne_corpse_beach" in DONE:
            hero.flags.dwayne_corpse = "beach"
        if "dump_dwayne_corpse_forest" in DONE:
            hero.flags.dwayne_corpse = "forest"
        if "dump_aletta_gun_mansion" in DONE:
            hero.flags.aletta_gun = "mansion"
        if "dump_aletta_gun_beach" in DONE:
            hero.flags.aletta_gun = "beach"
        if "dump_aletta_gun_forest" in DONE:
            hero.flags.aletta_gun = "forest"
        if "cherie_first_story_event" in DONE:
            DONE["cherie_event_01"] = DONE.pop("cherie_first_story_event")
        if aletta.flags.loyability:
            aletta.flags.liability = True

    def update_26_3_1():
        if "bree_event_06" in DONE:
            bree.sub.max = 75
        if "bree_event_12" in DONE:
            bree.sub.max = 100
        if "kiara_sub_event_01" in DONE and "kiara_sub_event_02" not in DONE:
            kiara.sub.max = 50

    def update_26_4_0b():
        if game.flags.dwaynedead and "dwayne_corpse_discovery" not in DONE:
            if not game.flags.dwayne_corpse_discovery_delay:
                game.flags.dwayne_corpse_discovery_delay = TemporaryFlag(True, 7)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
