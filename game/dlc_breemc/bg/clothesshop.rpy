init python:


    Equip("fancy_dress", gender="female", price=200, effects={"pacifist": 20, "princess": 20, "charm": 10})
    Equip("cardigan", gender="female", price=100, effects={"bookworm": 20, "family": 20, "knowledge": 5})
    Equip("leather_pants", gender="female", price=100, effects={"submissive": 20, "gourmand": 20, "charm": 5})
    Equip("luxury_bracelet", type="accessory", gender="female", price=200, effects={"pacifist": 20, "princess": 20, "charm": 10})
    Equip("pure_date_equip", display_name="Pure dress", gender="female", price=400, conditions=[HeroTarget(MinStat("morality", 80))])
    Equip("innocent_casual_equip", display_name="Innocent casual", gender="female", price=200, conditions=[HeroTarget(MinStat("morality", 60))])
    Equip("innocent_swimsuit_equip", display_name="Innocent swimsuit", gender="female", price=100, conditions=[HeroTarget(MinStat("morality", 50))])
    Equip("innocent_date_equip", display_name="Innocent dress", gender="female", price=200, conditions=[HeroTarget(MinStat("morality", 20))])
    Equip("sexy_date_equip", display_name="Sexy dress", gender="female", price=200, conditions=[HeroTarget(MaxStat("morality", -20))])
    Equip("sexy_swimsuit_equip", display_name="Sexy swimsuit", gender="female", price=100, conditions=[HeroTarget(MaxStat("morality", -40))])
    Equip("slutty_date_equip", display_name="Slutty dress", gender="female", price=400, conditions=[HeroTarget(MaxStat("morality", -80))])
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
