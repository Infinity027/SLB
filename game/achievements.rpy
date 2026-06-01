init -50 python:
    class Achievement:
        
        all_achievements = dict()
        popup_on_screen = dict()
        
        def __init__(self, id, name, description, locked_description=None, hidden=False):
            self.id = id
            self.name = name
            self.unlocked_description = description
            self.locked_description = locked_description
            self.unlocked_image = f"gui/achievements/{id}.jpg"
            self.locked_image = Transform(
            self.unlocked_image, matrixcolor=SaturationMatrix(0)
        )
            self.hidden = hidden
            
            self.all_achievements[self.id] = self
            achievement.register(self.id)
        
        @property
        def description(self):
            if not self.has() and self.locked_description is not None:
                return self.locked_description
            else:
                return self.unlocked_description
        
        @property
        def image(self):
            if self.has():
                return self.unlocked_image
            else:
                return self.locked_image
        
        def has(self):
            return achievement.has(self.id)
        
        def grant(self):
            if game.flags.cheat:
                return
            if not self.has():
                self.popup()
            ach = achievement.grant(self.id)
            achievement.sync()
            return ach
        
        def popup(self):
            if renpy.is_init_phase() or achievement.steamapi:
                return
            
            
            for i in range(4):
                if self.popup_on_screen.get(i, None) is None:
                    self.popup_on_screen[i] = True
                    break
            else:
                return
            renpy.music.play("sd/SFX/game/achievement.ogg", channel="audio")
            renpy.show_screen(
            "achievement_popup",
            _tag=f"popup_{i}",
            ach=self,
            index_pos=i,
            screen_tag=f"popup_{i}",
        )
        
        def clear(self):
            ach = achievement.clear(self.id)
            achievement.sync()      
            return ach
        
        @classmethod
        def reset(self):
            for ach in self.all_achievements:
                self.all_achievements[ach].clear()
        
        @classmethod
        def refresh(self):
            for ev in [i for i in DONE.keys() if "_achievement_" in i]:
                DONE.pop(ev)
        
        @classmethod
        @property
        def all_sorted_achievements(self):
            unlocked, locked = (dict() for i in range(2))
            for ach in self.all_achievements:
                if self.all_achievements[ach].has():
                    unlocked[ach] = self.all_achievements[ach]
                else:
                    locked[ach] = self.all_achievements[ach]
            return (unlocked, locked)
        
        @classmethod
        @property
        def total(self):
            return len(self.all_achievements)
        
        @classmethod
        @property
        def total_unlocked(self):
            return len(
            [ach for ach in self.all_achievements if self.all_achievements[ach].has()]
        )

transform achievement_popout():
    on show:
        xpos 0.0 xanchor 1.0
        easein_back 1.0 xpos 0.0 xanchor 0.0
    on hide:
        easeout_back 1.0 xpos 0.0 xanchor 1.0
    on replaced:
        easeout_back 1.0 xpos 0.0 xanchor 1.0
screen achievement_popup(ach, index_pos, screen_tag):
    zorder 190

    frame:
        background None xalign 0.0 yalign 0.0 xoffset 5 yoffset 90 + (index_pos * 100)
        add "gui/actions_box_big.png" xsize 500 ysize 80
        at achievement_popout()
        hbox:
            xoffset 8 yoffset 8
            add ach.unlocked_image yalign 0.5
            vbox:
                xfill True
                xsize 435
                text ach.name color "#ffffff" size 18 font "exo2_regular" xpos 7 bold True
                text ach.unlocked_description color "#ffffff" size 17 font "exo2_regular" xoffset 7 xalign 0.0 italic True

    timer 3.0 action [Hide("achievement_popup"), Show('achievement_popup_end', _tag=screen_tag+"_end", index_pos=index_pos)]

screen achievement_popup_end(index_pos):

    timer 3.0 action [SetDict(Achievement.popup_on_screen, index_pos, None), Hide()]



define aletta_achievement_1 = Achievement(
    id="aletta_1",
    name="First kiss with Aletta",
    description="Kiss Aletta for the first time")
define aletta_achievement_2 = Achievement(
    id="aletta_2",
    name="Aletta's hot coffee",
    description="Have fun with Aletta for the first time")
define aletta_achievement_3 = Achievement(
    id="aletta_3",
    name="Aletta's wedding",
    description="Get married with Aletta")

define alexis_achievement_1 = Achievement(
    id="alexis_1",
    name="First kiss with Alexis",
    description="Kiss Alexis for the first time")
define alexis_achievement_2 = Achievement(
    id="alexis_2",
    name="Alexis's hot coffee",
    description="Have fun with Alexis for the first time")
define alexis_achievement_3 = Achievement(
    id="alexis_3",
    name="Alexis' wedding",
    description="Get married with Alexis")

define alexis_achievement_4 = Achievement(
    id="alexis_4",
    name="AVENGE HER",
    description="Beat up your old sport teacher",
    locked_description="???",
    hidden=True)



define anna_achievement_1 = Achievement(
    id="anna_1",
    name="First kiss with Anna",
    description="Kiss Anna for the first time")
define anna_achievement_2 = Achievement(
    id="anna_2",
    name="Anna's hot coffee",
    description="Have fun with Anna for the first time")
define anna_achievement_3 = Achievement(
    id="anna_3",
    name="Anna's wedding",
    description="Get married with Anna")


define audrey_achievement_1 = Achievement(
    id="audrey_1",
    name="First kiss with Audrey",
    description="Kiss Audrey for the first time")
define audrey_achievement_2 = Achievement(
    id="audrey_2",
    name="Audrey's hot coffee",
    description="Have fun with Audrey for the first time")
define audrey_achievement_3 = Achievement(
    id="audrey_3",
    name="Audrey's wedding",
    description="Get married with Audrey")

define bree_achievement_1 = Achievement(
    id="bree_1",
    name="First kiss with Bree",
    description="Kiss Bree for the first time")
define bree_achievement_2 = Achievement(
    id="bree_2",
    name="Bree's hot coffee",
    description="Have fun with Bree for the first time")
define bree_achievement_3 = Achievement(
    id="bree_3",
    name="Bree's wedding",
    description="Get married with Bree")


define camila_achievement_1 = Achievement(
    id="camila_1",
    name="First kiss with Camila",
    description="Kiss Camila for the first time")
define camila_achievement_2 = Achievement(
    id="camila_2",
    name="Camila's hot coffee",
    description="Have fun with Camila for the first time")
define camila_achievement_3 = Achievement(
    id="camila_3",
    name="Camila's wedding",
    description="Get married with Camila")

define cassidy_achievement_1 = Achievement(
    id="cassidy_1",
    name="First kiss with Cassidy",
    description="Kiss Cassidy for the first time")
define cassidy_achievement_2 = Achievement(
    id="cassidy_2",
    name="Cassidy's hot coffee",
    description="Have fun with Cassidy for the first time")
define cassidy_achievement_3 = Achievement(
    id="cassidy_3",
    name="Cassidy's wedding",
    description="Get married with Cassidy")


define emma_achievement_1 = Achievement(
    id="emma_1",
    name="First kiss with Emma",
    description="Kiss Emma for the first time")
define emma_achievement_2 = Achievement(
    id="emma_2",
    name="Emma's hot coffee",
    description="Have fun with Emma for the first time")
define emma_achievement_3 = Achievement(
    id="emma_3",
    name="Emma's wedding",
    description="Get married with Emma")

define emma_achievement_5 = Achievement(
    id="emma_5",
    name="The elephant in the room",
    description="Succeed to use your massive tool on Emma's door",
    locked_description="???",
    hidden=True)



define hanna_achievement_1 = Achievement(
    id="hanna_1",
    name="First kiss with Hanna",
    description="Kiss Hanna for the first time")
define hanna_achievement_2 = Achievement(
    id="hanna_2",
    name="Hanna's hot coffee",
    description="Have fun with Hanna for the first time")
define hanna_achievement_3 = Achievement(
    id="hanna_3",
    name="Hanna's wedding",
    description="Get married with Hanna")

define hanna_achievement_4 = Achievement(
    id="hanna_4",
    name="Marketing expert",
    description="Make the gym a lewd place")



define harmony_achievement_1 = Achievement(
    id="harmony_1",
    name="First kiss with Harmony",
    description="Kiss Harmony for the first time")
define harmony_achievement_2 = Achievement(
    id="harmony_2",
    name="Harmony's hot coffee",
    description="Have fun with Harmony for the first time")
define harmony_achievement_3 = Achievement(
    id="harmony_3",
    name="Harmony's wedding",
    description="Get married with Harmony")

define harmony_achievement_4 = Achievement(
    id="harmony_4",
    name="Bad influence",
    description="Make Harmony a real pervert")
define harmony_achievement_5 = Achievement(
    id="harmony_5",
    name="Shower with holy water",
    description="Make sure Harmony stays pure until the end game")


define kleio_achievement_1 = Achievement(
    id="kleio_1",
    name="First kiss with Kleio",
    description="Kiss Kleio for the first time")
define kleio_achievement_2 = Achievement(
    id="kleio_2",
    name="Kleio's hot coffee",
    description="Have fun with Kleio for the first time")
define kleio_achievement_3 = Achievement(
    id="kleio_3",
    name="Kleio's wedding",
    description="Get married with Kleio")



define kylie_achievement_1 = Achievement(
    id="kylie_1",
    name="First kiss with Kylie",
    description="Kiss Kylie for the first time")
define kylie_achievement_2 = Achievement(
    id="kylie_2",
    name="Kylie's hot coffee",
    description="Have fun with Kylie for the first time")
define kylie_achievement_3 = Achievement(
    id="kylie_3",
    name="Release the kraken!",
    description="Get assaulted by Kylie",
    locked_description="???",
    hidden=True)
define kylie_achievement_4 = Achievement(
    id="kylie_4",
    name="Bloody Christmas!",
    description="Get killed by Kylie at Christmas",
    locked_description="???",
    hidden=True)
define kylie_achievement_5 = Achievement(
    id="kylie_5",
    name="Kylie's wedding",
    description="Get married with Kylie")

define kylie_achievement_7 = Achievement(
    id="kylie_7",
    name="Love and Thunder",
    description="Lead Kylie to her death",
    locked_description="???",
    hidden=True)
define kylie_achievement_8 = Achievement(
    id="kylie_8",
    name="Death's Appointment",
    description="Get killed by Kylie on Friday 13th",
    locked_description="???",
    hidden=True)



define lavish_achievement_1 = Achievement(
    id="lavish_1",
    name="First kiss with Lavish",
    description="Kiss Lavish for the first time")
define lavish_achievement_2 = Achievement(
    id="lavish_2",
    name="Lavish's hot coffee",
    description="Have fun with Lavish for the first time")
define lavish_achievement_3 = Achievement(
    id="lavish_3",
    name="Lavish's wedding",
    description="Get married with Lavish")
define lavish_achievement_4 = Achievement(
    id="lavish_4",
    name="Lavish's pregnancy",
    description="Get Lavish pregnant")



define lexi_achievement_1 = Achievement(
    id="lexi_1",
    name="First kiss with Lexi",
    description="Kiss Lexi for the first time")
define lexi_achievement_2 = Achievement(
    id="lexi_2",
    name="Lexi's hot coffee",
    description="Have fun with Lexi for the first time")
define lexi_achievement_3 = Achievement(
    id="lexi_3",
    name="Lexi's wedding",
    description="Get married with Lexi")
define lexi_achievement_4 = Achievement(
    id="lexi_4",
    name="Lexi's pregnancy",
    description="Get Lexi pregnant")
define lexi_achievement_5 = Achievement(
    id="lexi_5",
    name="Risky business",
    description="Become Lexi's new pimp")


define minami_achievement_1 = Achievement(
    id="minami_1",
    name="First kiss with Minami",
    description="Kiss Minami for the first time")
define minami_achievement_2 = Achievement(
    id="minami_2",
    name="Minami's hot coffee",
    description="Have fun with Minami for the first time")
define minami_achievement_3 = Achievement(
    id="minami_3",
    name="Minami's wedding",
    description="Get married with Minami")


define morgan_achievement_1 = Achievement(
    id="morgan_1",
    name="First kiss with Morgan",
    description="Kiss Morgan for the first time")
define morgan_achievement_2 = Achievement(
    id="morgan_2",
    name="Morgan's hot coffee",
    description="Have fun with Morgan for the first time")
define morgan_achievement_3 = Achievement(
    id="morgan_3",
    name="Morgan's wedding",
    description="Get married with Morgan")

define morgan_achievement_4 = Achievement(
    id="morgan_4",
    name="My Fair Lady",
    description="Totally feminize Morgan")



define palla_achievement_1 = Achievement(
    id="palla_1",
    name="First kiss with Palla",
    description="Kiss Palla for the first time")
define palla_achievement_2 = Achievement(
    id="palla_2",
    name="Palla's hot coffee",
    description="Have fun with Palla for the first time")
define palla_achievement_3 = Achievement(
    id="palla_3",
    name="Palla's wedding",
    description="Get married with Palla")

define palla_achievement_5 = Achievement(
    id="palla_5",
    name="Palla Poundin",
    description="Make Palla a famous pornstar",
    locked_description="???",
    hidden=True)
define palla_achievement_6 = Achievement(
    id="palla_6",
    name="Business model",
    description="Pay off Palla's job loan")



define samantha_achievement_1 = Achievement(
    id="samantha_1",
    name="First kiss with Samantha",
    description="Kiss Samantha for the first time")
define samantha_achievement_2 = Achievement(
    id="samantha_2",
    name="Samantha's hot coffee",
    description="Have fun with Samantha for the first time")
define samantha_achievement_3 = Achievement(
    id="samantha_3",
    name="Samantha's wedding",
    description="Get married with Samantha")

define samantha_achievement_5 = Achievement(
    id="samantha_5",
    name="Netori enjoyer",
    description="Truly cuck Ryan with Samantha",
    locked_description="???",
    hidden=True)



define sasha_achievement_1 = Achievement(
    id="sasha_1",
    name="First kiss with Sasha",
    description="Kiss Sasha for the first time")
define sasha_achievement_2 = Achievement(
    id="sasha_2",
    name="Sasha's hot coffee",
    description="Have fun with Sasha for the first time")
define sasha_achievement_3 = Achievement(
    id="sasha_3",
    name="Sasha's wedding",
    description="Get married with Sasha")



define shiori_achievement_1 = Achievement(
    id="shiori_1",
    name="First kiss with Shiori",
    description="Kiss Shiori for the first time")
define shiori_achievement_2 = Achievement(
    id="shiori_2",
    name="Shiori's hot coffee",
    description="Have fun with Shiori for the first time")
define shiori_achievement_3 = Achievement(
    id="shiori_3",
    name="Shiori's wedding",
    description="Get married with Shiori")

define shiori_achievement_5 = Achievement(
    id="shiori_5",
    name="This is the Milky Way",
    description="Get a cup of coffee with milk")


define danny_achievement_0 = Achievement(
    id="danny_0",
    name="42nd on-screen death",
    description="Kill Danny",
    locked_description="???",
    hidden=True)
define dwayne_achievement_0 = Achievement(
    id="dwayne_0",
    name="What is he cooking?",
    description="Kill Dwayne",
    locked_description="???",
    hidden=True)
define ryan_achievement_0 = Achievement(
    id="ryan_0",
    name="18h17 - The Jerk",
    description="Kill Ryan",
    locked_description="???",
    hidden=True)
define mike_achievement_0 = Achievement(
    id="mike_0",
    name="Mike Bauer",
    description="Reach a game's ending in the first 24 hours",
    locked_description="???",
    hidden=True)


define cherie_achievement_0 = Achievement(
    id="cherie_0",
    name="Widow in need",
    description="Have fun with Cherie during the office christmas party",
    locked_description="???",
    hidden=True)
define kiara_achievement_0 = Achievement(
    id="kiara_0",
    name="The manager's special",
    description="Have fun with Kiara when helping Bree at the maid cafe")
define natalie_achievement_1 = Achievement(
    id="natalie_1",
    name="A friendly reprimand",
    description="Have fun with Natalie and Samantha",
    locked_description="???",
    hidden=True)
define scottie_achievement_1 = Achievement(
    id="scottie_1",
    name="A beautiful rebel and a wonderful idiot",
    description="Have fun with Scottie and Sasha")
define angela_bruce_achievement_1 = Achievement(
    id="angela_bruce_1",
    name="We said not moms!",
    description="Caught Angela committing adultery",
    locked_description="???",
    hidden=True)



define band_harem_achievement_1 = Achievement(
    id="band_harem_1",
    name="Official guitarist",
    description="Get in a three way relationship with Anna and Kleio")
define band_harem_achievement_2 = Achievement(
    id="band_harem_2",
    name="Tattooed girls",
    description="Have fun with Anna and Kleio")
define band_harem_achievement_3 = Achievement(
    id="band_harem_3",
    name="Song of love",
    description="Get married with both Anna and Kleio")
define band_harem_achievement_4 = Achievement(
    id="band_harem_4",
    name="Best with a bass",
    description="Add Sasha to the Band Harem")
define band_harem_achievement_5 = Achievement(
    id="band_harem_5",
    name="Goin' Rock'n'Roll",
    description="Have fun with Anna, Kleio and Sasha")
define band_harem_achievement_6 = Achievement(
    id="band_harem_6",
    name="Deathless Harpies forever",
    description="Get married with all Anna, Kleio and Sasha")



define bitchy_harem_achievement_1 = Achievement(
    id="bitchy_harem_1",
    name="Hot and cold",
    description="Get in a three way relationship with Audrey and Palla")
define bitchy_harem_achievement_2 = Achievement(
    id="bitchy_harem_2",
    name="Scylla and Charybdis",
    description="Have fun with Audrey and Palla")
define bitchy_harem_achievement_3 = Achievement(
    id="bitchy_harem_3",
    name="Infinite wedding gift list",
    description="Get married with both Audrey and Palla")
define bitchy_harem_achievement_4 = Achievement(
    id="bitchy_harem_4",
    name="Jet-setters",
    description="Add Cassidy to the Bitchy Harem")
define bitchy_harem_achievement_5 = Achievement(
    id="bitchy_harem_5",
    name="Champagne!",
    description="Have fun with Audrey, Cassidy and Palla")
define bitchy_harem_achievement_6 = Achievement(
    id="bitchy_harem_6",
    name="Luxury lifestyle",
    description="Get married with all Audrey, Cassidy and Palla")



define college_harem_achievement_1 = Achievement(
    id="college_harem_1",
    name="College project",
    description="Get in a three way relationship with Anna and Bree")
define college_harem_achievement_2 = Achievement(
    id="college_harem_2",
    name="For science only",
    description="Have fun with Anna and Bree")
define college_harem_achievement_3 = Achievement(
    id="college_harem_3",
    name="Lemon and Strawberry Mix",
    description="Get married with both Anna and Bree")


define criminal_harem_achievement_1 = Achievement(
    id="criminal_harem_1",
    name="Get out of jail free card",
    description="Get in a three way relationship with Camila and Lexi")
define criminal_harem_achievement_2 = Achievement(
    id="criminal_harem_2",
    name="A game of cops and robbers",
    description="Have fun with Camila and Lexi")
define criminal_harem_achievement_3 = Achievement(
    id="criminal_harem_3",
    name="Rings and bracelets",
    description="Get married with both Camila and Lexi")



define fashion_harem_achievement_1 = Achievement(
    id="fashion_harem_1",
    name="Best customer service",
    description="Get in a three way relationship with Palla and Sasha")
define fashion_harem_achievement_2 = Achievement(
    id="fashion_harem_2",
    name="Fashionistas",
    description="Have fun with Palla and Sasha")
define fashion_harem_achievement_3 = Achievement(
    id="fashion_harem_3",
    name="Extended Fashion Week",
    description="Get married with both Palla and Sasha")



define friendly_harem_achievement_1 = Achievement(
    id="friendly_harem_1",
    name="Good friends",
    description="Get in a three way relationship with Emma and Samantha")
define friendly_harem_achievement_2 = Achievement(
    id="friendly_harem_2",
    name="Very good friends",
    description="Have fun with Emma and Samantha")
define friendly_harem_achievement_3 = Achievement(
    id="friendly_harem_3",
    name="BFF",
    description="Get married with both Emma and Samantha")



define gaming_harem_achievement_2 = Achievement(
    id="gaming_harem_2",
    name="There's more than video games",
    description="Have fun with Kat and Bree")



define home_harem_achievement_1 = Achievement(
    id="home_harem_1",
    name="The roommates agreement",
    description="Get in a three way relationship with Bree and Sasha")
define home_harem_achievement_2 = Achievement(
    id="home_harem_2",
    name="A party of three",
    description="Have fun with Bree and Sasha")
define home_harem_achievement_3 = Achievement(
    id="home_harem_3",
    name="Polyamory's the way",
    description="Get married with both Bree and Sasha")
define home_harem_achievement_4 = Achievement(
    id="home_harem_4",
    name="Share a taste of lollipop",
    description="Add Lexi to the Home Harem")
define home_harem_achievement_5 = Achievement(
    id="home_harem_5",
    name="Manga touch",
    description="Add Minami to the Home Harem")
define home_harem_achievement_6 = Achievement(
    id="home_harem_6",
    name="A bite of cinnamon roll",
    description="Add Samantha to the Home Harem")
define home_harem_achievement_7 = Achievement(
    id="home_harem_7",
    name="A quintet of brides",
    description="Get married with all Bree, Lexi, Minami, Samantha, Sasha")



define jealous_harem_achievement_1 = Achievement(
    id="jealous_harem_1",
    name="Brunettes battle",
    description="Get in a three way relationship with Audrey and Sasha")
define jealous_harem_achievement_2 = Achievement(
    id="jealous_harem_2",
    name="Brunettes peace",
    description="Have fun with Audrey and Sasha")
define jealous_harem_achievement_3 = Achievement(
    id="jealous_harem_3",
    name="Brunettes love",
    description="Get married with both Audrey and Sasha")



define office_harem_achievement_1 = Achievement(
    id="office_harem_1",
    name="Call me boss",
    description="Get in a five way relationship with Aletta, Audrey, Lavish and Shiori")
define office_harem_achievement_2 = Achievement(
    id="office_harem_2",
    name="Working on me, for me",
    description="Have fun with Aletta, Audrey, Lavish and Shiori")
define office_harem_achievement_3 = Achievement(
    id="office_harem_3",
    name="Bringing the office at home",
    description="Get married with all Aletta, Audrey, Lavish and Shiori")
define office_harem_achievement_4 = Achievement(
    id="office_harem_4",
    name="Diversification",
    description="Pimp at least one of the girl at the office",
    locked_description="???",
    hidden=True)



define pixie_harem_achievement_1 = Achievement(
    id="pixie_harem_1",
    name="Back together",
    description="Get in a three way relationship with Kleio and Morgan")
define pixie_harem_achievement_2 = Achievement(
    id="pixie_harem_2",
    name="Colorful",
    description="Have fun with Kleio and Morgan")
define pixie_harem_achievement_3 = Achievement(
    id="pixie_harem_3",
    name="Like a rainbow",
    description="Get married with both Kleio and Morgan")

define battle_of_bands_achievement_1 = Achievement(
    id="battle_of_bands_1",
    name="We really shook the pillars of heaven, didn't we?",
    description="Win the Battle of the Bands")



define job_achievement_1 = Achievement(
    id="job_1",
    name="Max level of incompetence",
    description="Get all promotions possible at your job")



define pet_achievement_1 = Achievement(
    id="pet_1",
    name="It's just a pet, nothing more",
    description="Adopt an animal")
define shark_achievement_1 = Achievement(
    id="shark_1",
    name="Have you met Shark-chan?",
    description="Get eaten by the shark",
    locked_description="???",
    hidden=True)
define shark_achievement_2 = Achievement(
    id="shark_2",
    name="Again? Really?",
    description="Get eaten by the shark, again...",
    locked_description="???",
    hidden=True)
define bear_achievement_1 = Achievement(
    id="bear_1",
    name="Life is un\"bear\"able",
    description="Get to play with the bear",
    locked_description="???",
    hidden=True)
define animals_attack_achievement_1 = Achievement(
    id="animals_attack_1",
    name="Zoophobia",
    description="Be attacked by all animals (multiple saves)",
    locked_description="???",
    hidden=True)
define bear_shark_achievement_1 = Achievement(
    id="bear_shark_1",
    name="Happy Three Friends",
    description="Quit all for true friendship",
    locked_description="???",
    hidden=True)


define halloween_achievement_1 = Achievement(
    id="halloween_1",
    name="Halloween costume expectancy",
    description="Throw a party at home for Halloween")
define christmas_achievement_1 = Achievement(
    id="christmas_1",
    name="Jingle Bells",
    description="Throw a party at home for Christmas")
define christmas_achievement_2 = Achievement(
    id="christmas_2",
    name="Corporate Christmas party",
    description="Throw a party at the office for Christmas")


define sexperience_achievement_1 = Achievement(
    id="sexperience_1",
    name="Like a rabbit",
    description="Have fun 300 times with girls (single save)",
    locked_description="???",
    hidden=True)
define sexperience_achievement_2 = Achievement(
    id="sexperience_2",
    name="Platonic Love",
    description="Reach a girl's wedding without having fun with that girl",
    locked_description="???",
    hidden=True)
define sexperience_achievement_3 = Achievement(
    id="sexperience_3",
    name="Like a virgin",
    description="Reach a wedding without having fun with any girl",
    locked_description="???",
    hidden=True)
define sexperience_achievement_4 = Achievement(
    id="sexperience_4",
    name="Around the World in Eighty Days",
    description="Have fun at least once with all girls in less than 80 days without any of them leaving the game (DLC girls not included)",
    locked_description="???",
    hidden=True)
define bluepill_achievement_1 = Achievement(
    id="bluepill_1",
    name="Sex Overdose",
    description="Abuse of the little blue pill",
    locked_description="???",
    hidden=True)


define alone_achievement_1 = Achievement(
    id="alone_1",
    name="Solitude & Sorrow: Final Base",
    description="Get rid of every love interest (FAFWM girls not included {b}yet{/b})",
    locked_description="???",
    hidden=True)


define tea_achievement_1 = Achievement(
    id="tea_1",
    name="Tea Time",
    description="Drink all possible teas")


init python:
    Event(**{
    "name": "aletta_achievement_1",
    "label": "aletta_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("aletta",
            MinFlag("kiss", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "aletta_achievement_2",
    "label": "aletta_achievement_2",
    "conditions": [
        
        PersonTarget("aletta",
            MinStat("sexperience", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "aletta_achievement_4",
    "label": "aletta_achievement_4",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("aletta",
            Or(
                MinFlag("pregnancies_number", 1),
                MinFlag("mikeBabies", 1)
                )
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label aletta_achievement_1:
    $ aletta_achievement_1.grant()
    return
label aletta_achievement_2:
    $ aletta_achievement_2.grant()
    return
label aletta_achievement_3:
    $ aletta_achievement_3.grant()
    return
label aletta_achievement_4:
    $ aletta_achievement_4.grant()
    return


init python:
    Event(**{
    "name": "alexis_achievement_1",
    "label": "alexis_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("alexis",
            MinFlag("kiss", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "alexis_achievement_2",
    "label": "alexis_achievement_2",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("alexis",
            MinStat("sexperience", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "alexis_achievement_4",
    "label": "alexis_achievement_4",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("alexis",
            Or(
                MinFlag("pregnancies_number", 1),
                MinFlag("mikeBabies", 1)
                )
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "alexis_achievement_5",
    "label": "alexis_achievement_5",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("alexis",
            IsFlag("coachVictory", True)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label alexis_achievement_1:
    $ alexis_achievement_1.grant()
    return
label alexis_achievement_2:
    $ alexis_achievement_2.grant()
    return
label alexis_achievement_3:
    $ alexis_achievement_3.grant()
    return
label alexis_achievement_4:
    $ alexis_achievement_4.grant()
    return
label alexis_achievement_5:
    $ alexis_achievement_5.grant()
    return


init python:
    Event(**{
    "name": "anna_achievement_1",
    "label": "anna_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("anna",
            MinFlag("kiss", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "anna_achievement_2",
    "label": "anna_achievement_2",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("anna",
            MinStat("sexperience", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "anna_achievement_4",
    "label": "anna_achievement_4",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("anna",
            Or(
                MinFlag("pregnancies_number", 1),
                MinFlag("mikeBabies", 1)
                )
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label anna_achievement_1:
    $ anna_achievement_1.grant()
    return
label anna_achievement_2:
    $ anna_achievement_2.grant()
    return
label anna_achievement_3:
    $ anna_achievement_3.grant()
    return
label anna_achievement_4:
    $ anna_achievement_4.grant()
    return


init python:
    Event(**{
    "name": "audrey_achievement_1",
    "label": "audrey_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("audrey",
            MinFlag("kiss", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "audrey_achievement_2",
    "label": "audrey_achievement_2",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("audrey",
            MinStat("sexperience", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "audrey_achievement_4",
    "label": "audrey_achievement_4",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("audrey",
            Or(
                MinFlag("pregnancies_number", 1),
                MinFlag("mikeBabies", 1)
                )
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label audrey_achievement_1:
    $ audrey_achievement_1.grant()
    return
label audrey_achievement_2:
    $ audrey_achievement_2.grant()
    return
label audrey_achievement_3:
    $ audrey_achievement_3.grant()
    return
label audrey_achievement_4:
    $ audrey_achievement_4.grant()
    return


init python:
    Event(**{
    "name": "bree_achievement_1",
    "label": "bree_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("bree",
            MinFlag("kiss", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "bree_achievement_2",
    "label": "bree_achievement_2",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("bree",
            MinStat("sexperience", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "bree_achievement_4",
    "label": "bree_achievement_4",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("bree",
            Or(
                MinFlag("pregnancies_number", 1),
                MinFlag("mikeBabies", 1)
                )
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label bree_achievement_1:
    $ bree_achievement_1.grant()
    return
label bree_achievement_2:
    $ bree_achievement_2.grant()
    return
label bree_achievement_3:
    $ bree_achievement_3.grant()
    return
label bree_achievement_4:
    $ bree_achievement_4.grant()
    return


init python:
    Event(**{
    "name": "camila_achievement_1",
    "label": "camila_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("camila",
            MinFlag("kiss", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "camila_achievement_2",
    "label": "camila_achievement_2",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("camila",
            MinStat("sexperience", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "camila_achievement_4",
    "label": "camila_achievement_4",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("camila",
            Or(
                MinFlag("pregnancies_number", 1),
                MinFlag("mikeBabies", 1)
                )
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label camila_achievement_1:
    $ camila_achievement_1.grant()
    return
label camila_achievement_2:
    $ camila_achievement_2.grant()
    return
label camila_achievement_3:
    $ camila_achievement_3.grant()
    return
label camila_achievement_4:
    $ camila_achievement_4.grant()
    return


init python:
    Event(**{
    "name": "cassidy_achievement_1",
    "label": "cassidy_achievement_1",
    "conditions": [
        GameTarget(
            IsFlag("cheat", False)
            ),
        PersonTarget("cassidy",
            MinFlag("kiss", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "cassidy_achievement_2",
    "label": "cassidy_achievement_2",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("cassidy",
            MinStat("sexperience", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "cassidy_achievement_4",
    "label": "cassidy_achievement_4",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("cassidy",
            Or(
                MinFlag("pregnancies_number", 1),
                MinFlag("mikeBabies", 1)
                )
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label cassidy_achievement_1:
    $ cassidy_achievement_1.grant()
    return
label cassidy_achievement_2:
    $ cassidy_achievement_2.grant()
    return
label cassidy_achievement_3:
    $ cassidy_achievement_3.grant()
    return
label cassidy_achievement_4:
    $ cassidy_achievement_4.grant()
    return


init python:
    Event(**{
    "name": "emma_achievement_1",
    "label": "emma_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("emma",
            MinFlag("kiss", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "emma_achievement_2",
    "label": "emma_achievement_2",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("emma",
            MinStat("sexperience", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "emma_achievement_4",
    "label": "emma_achievement_4",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("emma",
            Or(
                MinFlag("pregnancies_number", 1),
                MinFlag("mikeBabies", 1)
                )
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label emma_achievement_1:
    $ emma_achievement_1.grant()
    return
label emma_achievement_2:
    $ emma_achievement_2.grant()
    return
label emma_achievement_3:
    $ emma_achievement_3.grant()
    return
label emma_achievement_4:
    $ emma_achievement_4.grant()
    return
label emma_achievement_5:
    $ emma_achievement_5.grant()
    return


init python:
    Event(**{
    "name": "hanna_achievement_1",
    "label": "hanna_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("hanna",
            MinFlag("kiss", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "hanna_achievement_2",
    "label": "hanna_achievement_2",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("hanna",
            MinStat("sexperience", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "hanna_achievement_4",
    "label": "hanna_achievement_4",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("hanna",
            Or(
                MinFlag("pregnancies_number", 1),
                MinFlag("mikeBabies", 1)
                )
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "hanna_achievement_5",
    "label": "hanna_achievement_5",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("hanna",
            IsFlag("gymSolution", "lewd")
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label hanna_achievement_1:
    $ hanna_achievement_1.grant()
    return
label hanna_achievement_2:
    $ hanna_achievement_2.grant()
    return
label hanna_achievement_3:
    $ hanna_achievement_3.grant()
    return
label hanna_achievement_4:
    $ hanna_achievement_4.grant()
    return
label hanna_achievement_5:
    $ hanna_achievement_5.grant()
    return


init python:
    Event(**{
    "name": "harmony_achievement_1",
    "label": "harmony_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("harmony",
            MinFlag("kiss", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "harmony_achievement_2",
    "label": "harmony_achievement_2",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("harmony",
            MinStat("sexperience", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "harmony_achievement_4",
    "label": "harmony_achievement_4",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("harmony",
            Or(
                MinFlag("pregnancies_number", 1),
                MinFlag("mikeBabies", 1)
                )
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "harmony_achievement_5",
    "label": "harmony_achievement_5",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("harmony",
            HasTrait("slutty")
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label harmony_achievement_1:
    $ harmony_achievement_1.grant()
    return
label harmony_achievement_2:
    $ harmony_achievement_2.grant()
    return
label harmony_achievement_3:
    $ harmony_achievement_3.grant()
    return
label harmony_achievement_4:
    $ harmony_achievement_4.grant()
    return
label harmony_achievement_5:
    $ harmony_achievement_5.grant()
    return
label harmony_achievement_6:
    $ harmony_achievement_6.grant()
    return


init python:
    Event(**{
    "name": "kleio_achievement_1",
    "label": "kleio_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("kleio",
            MinFlag("kiss", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "kleio_achievement_2",
    "label": "kleio_achievement_2",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("kleio",
            MinStat("sexperience", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "kleio_achievement_4",
    "label": "kleio_achievement_4",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("kleio",
            Or(
                MinFlag("pregnancies_number", 1),
                MinFlag("mikeBabies", 1)
                )
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label kleio_achievement_1:
    $ kleio_achievement_1.grant()
    return
label kleio_achievement_2:
    $ kleio_achievement_2.grant()
    return
label kleio_achievement_3:
    $ kleio_achievement_3.grant()
    return
label kleio_achievement_4:
    $ kleio_achievement_4.grant()
    return


init python:
    Event(**{
    "name": "kylie_achievement_1",
    "label": "kylie_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("kylie",
            MinFlag("kiss", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "kylie_achievement_2",
    "label": "kylie_achievement_2",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("kylie",
            MinStat("sexperience", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "kylie_achievement_6",
    "label": "kylie_achievement_6",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("kylie",
            Or(
                MinFlag("pregnancies_number", 1),
                MinFlag("mikeBabies", 1)
                )
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label kylie_achievement_1:
    $ kylie_achievement_1.grant()
    return
label kylie_achievement_2:
    $ kylie_achievement_2.grant()
    return
label kylie_achievement_3:
    $ kylie_achievement_3.grant()
    return
label kylie_achievement_4:
    $ kylie_achievement_4.grant()
    return
label kylie_achievement_5:
    $ kylie_achievement_5.grant()
    return
label kylie_achievement_6:
    $ kylie_achievement_6.grant()
    return
label kylie_achievement_7:
    $ kylie_achievement_7.grant()
    return
label kylie_achievement_8:
    $ kylie_achievement_8.grant()
    return


init python:
    Event(**{
    "name": "lavish_achievement_1",
    "label": "lavish_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("lavish",
            MinFlag("kiss", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "lavish_achievement_2",
    "label": "lavish_achievement_2",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("lavish",
            MinStat("sexperience", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "lavish_achievement_4",
    "label": "lavish_achievement_4",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("lavish",
            Or(
                MinFlag("pregnancies_number", 1),
                MinFlag("mikeBabies", 1)
                )
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label lavish_achievement_1:
    $ lavish_achievement_1.grant()
    return
label lavish_achievement_2:
    $ lavish_achievement_2.grant()
    return
label lavish_achievement_3:
    $ lavish_achievement_3.grant()
    return
label lavish_achievement_4:
    $ lavish_achievement_4.grant()
    return


init python:
    Event(**{
    "name": "lexi_achievement_1",
    "label": "lexi_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("lexi",
            MinFlag("kiss", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "lexi_achievement_2",
    "label": "lexi_achievement_2",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("lexi",
            MinStat("sexperience", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "lexi_achievement_4",
    "label": "lexi_achievement_4",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("lexi",
            Or(
                MinFlag("pregnancies_number", 1),
                MinFlag("mikeBabies", 1)
                )
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label lexi_achievement_1:
    $ lexi_achievement_1.grant()
    return
label lexi_achievement_2:
    $ lexi_achievement_2.grant()
    return
label lexi_achievement_3:
    $ lexi_achievement_3.grant()
    return
label lexi_achievement_4:
    $ lexi_achievement_4.grant()
    return
label lexi_achievement_5:
    $ lexi_achievement_5.grant()
    return


init python:
    Event(**{
    "name": "minami_achievement_1",
    "label": "minami_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("minami",
            MinFlag("kiss", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "minami_achievement_2",
    "label": "minami_achievement_2",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("minami",
            MinStat("sexperience", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "minami_achievement_4",
    "label": "minami_achievement_4",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("minami",
            Or(
                MinFlag("pregnancies_number", 1),
                MinFlag("mikeBabies", 1)
                )
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label minami_achievement_1:
    $ minami_achievement_1.grant()
    return
label minami_achievement_2:
    $ minami_achievement_2.grant()
    return
label minami_achievement_3:
    $ minami_achievement_3.grant()
    return
label minami_achievement_4:
    $ minami_achievement_4.grant()
    return


init python:
    Event(**{
    "name": "morgan_achievement_1",
    "label": "morgan_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("morgan",
            MinFlag("kiss", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "morgan_achievement_2",
    "label": "morgan_achievement_2",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("morgan",
            MinStat("sexperience", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "morgan_achievement_4",
    "label": "morgan_achievement_4",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("morgan",
            Or(
                MinFlag("pregnancies_number", 1),
                MinFlag("mikeBabies", 1)
                )
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "morgan_achievement_5",
    "label": "morgan_achievement_5",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("morgan",
            MaxStat("male", 0)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label morgan_achievement_1:
    $ morgan_achievement_1.grant()
    return
label morgan_achievement_2:
    $ morgan_achievement_2.grant()
    return
label morgan_achievement_3:
    $ morgan_achievement_3.grant()
    return
label morgan_achievement_4:
    $ morgan_achievement_4.grant()
    return
label morgan_achievement_5:
    $ morgan_achievement_5.grant()
    return


init python:
    Event(**{
    "name": "palla_achievement_1",
    "label": "palla_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("palla",
            MinFlag("kiss", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "palla_achievement_2",
    "label": "palla_achievement_2",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("palla",
            MinStat("sexperience", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "palla_achievement_4",
    "label": "palla_achievement_4",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("palla",
            Or(
                MinFlag("pregnancies_number", 1),
                MinFlag("mikeBabies", 1)
                )
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "palla_achievement_6",
    "label": "palla_achievement_6",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("palla",
            IsFlag("career"),
            MinFlag("jobloan", 0)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label palla_achievement_1:
    $ palla_achievement_1.grant()
    return
label palla_achievement_2:
    $ palla_achievement_2.grant()
    return
label palla_achievement_3:
    $ palla_achievement_3.grant()
    return
label palla_achievement_4:
    $ palla_achievement_4.grant()
    return
label palla_achievement_5:
    $ palla_achievement_5.grant()
    return
label palla_achievement_6:
    $ palla_achievement_6.grant()
    return


init python:
    Event(**{
    "name": "samantha_achievement_1",
    "label": "samantha_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("samantha",
            MinFlag("kiss", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "samantha_achievement_2",
    "label": "samantha_achievement_2",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("samantha",
            MinStat("sexperience", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "samantha_achievement_4",
    "label": "samantha_achievement_4",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("samantha",
            Or(
                MinFlag("pregnancies_number", 1),
                MinFlag("mikeBabies", 1)
                )
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label samantha_achievement_1:
    $ samantha_achievement_1.grant()
    return
label samantha_achievement_2:
    $ samantha_achievement_2.grant()
    return
label samantha_achievement_3:
    $ samantha_achievement_3.grant()
    return
label samantha_achievement_4:
    $ samantha_achievement_4.grant()
    return
label samantha_achievement_5:
    $ samantha_achievement_5.grant()
    return


init python:
    Event(**{
    "name": "sasha_achievement_1",
    "label": "sasha_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("sasha",
            MinFlag("kiss", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "sasha_achievement_2",
    "label": "sasha_achievement_2",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("sasha",
            MinStat("sexperience", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "sasha_achievement_4",
    "label": "sasha_achievement_4",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("sasha",
            Or(
                MinFlag("pregnancies_number", 1),
                MinFlag("mikeBabies", 1)
                )
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label sasha_achievement_1:
    $ sasha_achievement_1.grant()
    return
label sasha_achievement_2:
    $ sasha_achievement_2.grant()
    return
label sasha_achievement_3:
    $ sasha_achievement_3.grant()
    return
label sasha_achievement_4:
    $ sasha_achievement_4.grant()
    return


init python:
    Event(**{
    "name": "shiori_achievement_1",
    "label": "shiori_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("shiori",
            MinFlag("kiss", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "shiori_achievement_2",
    "label": "shiori_achievement_2",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("shiori",
            MinStat("sexperience", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "shiori_achievement_4",
    "label": "shiori_achievement_4",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("shiori",
            Or(
                MinFlag("pregnancies_number", 1),
                MinFlag("mikeBabies", 1)
                )
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label shiori_achievement_1:
    $ shiori_achievement_1.grant()
    return
label shiori_achievement_2:
    $ shiori_achievement_2.grant()
    return
label shiori_achievement_3:
    $ shiori_achievement_3.grant()
    return
label shiori_achievement_4:
    $ shiori_achievement_4.grant()
    return
label shiori_achievement_5:
    $ shiori_achievement_5.grant()
    return


init python:
    Event(**{
    "name": "danny_achievement_0",
    "label": "danny_achievement_0",
    "conditions": [
        GameTarget(IsFlag("cheat", False),
                   IsFlag("dannydead", True)
                   ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "dwayne_achievement_0",
    "label": "dwayne_achievement_0",
    "conditions": [
        GameTarget(IsFlag("cheat", False),
                   IsFlag("dwaynedead", True)
                   ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "ryan_achievement_0",
    "label": "ryan_achievement_0",
    "conditions": [
        GameTarget(IsFlag("cheat", False),
                   IsFlag("ryandead", True)
                   ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label danny_achievement_0:
    $ danny_achievement_0.grant()
    return
label dwayne_achievement_0:
    $ dwayne_achievement_0.grant()
    return
label ryan_achievement_0:
    $ ryan_achievement_0.grant()
    return
label mike_achievement_0:
    $ mike_achievement_0.grant()
    return


init python:
    Event(**{
    "name": "angela_bruce_achievement_1",
    "label": "angela_bruce_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False),
                   IsFlag("angelaBlow", True)
                   ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label cherie_achievement_0:
    $ cherie_achievement_0.grant()
    return
label kiara_achievement_0:
    $ kiara_achievement_0.grant()
    return
label natalie_achievement_1:
    $ natalie_achievement_1.grant()
    return
label scottie_achievement_1:
    $ scottie_achievement_1.grant()
    return
label angela_bruce_achievement_1:
    $ angela_bruce_achievement_1.grant()
    return
label violaine_achievement_1:
    $ violaine_achievement_1.grant()
    return


init python:
    Event(**{
    "name": "band_harem_achievement_1",
    "label": "band_harem_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        TogetherInHarem('band', 'anna', 'kleio'),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label band_harem_achievement_1:
    $ band_harem_achievement_1.grant()
    return
label band_harem_achievement_2:
    $ band_harem_achievement_2.grant()
    return
label band_harem_achievement_3:
    $ band_harem_achievement_3.grant()
    return
label band_harem_achievement_4:
    $ band_harem_achievement_4.grant()
    return
label band_harem_achievement_5:
    $ band_harem_achievement_5.grant()
    return
label band_harem_achievement_6:
    $ band_harem_achievement_6.grant()
    return


init python:
    Event(**{
    "name": "bitchy_harem_achievement_1",
    "label": "bitchy_harem_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        TogetherInHarem('bitchy', 'audrey', 'palla'),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "bitchy_harem_achievement_4",
    "label": "bitchy_harem_achievement_4",
    "conditions": [
        GameTarget(
            IsFlag("cheat", False)
            ),
        PersonTarget("cassidy",
            InHarem("bitchy"),
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label bitchy_harem_achievement_1:
    $ bitchy_harem_achievement_1.grant()
    return
label bitchy_harem_achievement_2:
    $ bitchy_harem_achievement_2.grant()
    return
label bitchy_harem_achievement_3:
    $ bitchy_harem_achievement_3.grant()
    return
label bitchy_harem_achievement_4:
    $ bitchy_harem_achievement_4.grant()
    return
label bitchy_harem_achievement_5:
    $ bitchy_harem_achievement_5.grant()
    return
label bitchy_harem_achievement_6:
    $ bitchy_harem_achievement_6.grant()
    return


init python:
    Event(**{
    "name": "college_harem_achievement_1",
    "label": "college_harem_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        TogetherInHarem('college', 'anna', 'bree'),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label college_harem_achievement_1:
    $ college_harem_achievement_1.grant()
    return
label college_harem_achievement_2:
    $ college_harem_achievement_2.grant()
    return
label college_harem_achievement_3:
    $ college_harem_achievement_3.grant()
    return


init python:
    Event(**{
    "name": "criminal_harem_achievement_1",
    "label": "criminal_harem_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        TogetherInHarem('criminal', 'camila', 'lexi'),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label criminal_harem_achievement_1:
    $ criminal_harem_achievement_1.grant()
    return
label criminal_harem_achievement_2:
    $ criminal_harem_achievement_2.grant()
    return
label criminal_harem_achievement_3:
    $ criminal_harem_achievement_3.grant()
    return


init python:
    Event(**{
    "name": "fashion_harem_achievement_1",
    "label": "fashion_harem_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        TogetherInHarem('fashion', 'palla', 'sasha',),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label fashion_harem_achievement_1:
    $ fashion_harem_achievement_1.grant()
    return
label fashion_harem_achievement_2:
    $ fashion_harem_achievement_2.grant()
    return
label fashion_harem_achievement_3:
    $ fashion_harem_achievement_3.grant()
    return


init python:
    Event(**{
    "name": "friendly_harem_achievement_1",
    "label": "friendly_harem_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        TogetherInHarem('friendly', 'emma', 'samantha'),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label friendly_harem_achievement_1:
    $ friendly_harem_achievement_1.grant()
    return
label friendly_harem_achievement_2:
    $ friendly_harem_achievement_2.grant()
    return
label friendly_harem_achievement_3:
    $ friendly_harem_achievement_3.grant()
    return


label gaming_harem_achievement_2:
    $ gaming_harem_achievement_2.grant()
    return


init python:
    Event(**{
    "name": "home_harem_achievement_1",
    "label": "home_harem_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        TogetherInHarem('home', 'bree', 'sasha'),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "home_harem_achievement_4",
    "label": "home_harem_achievement_4",
    "conditions": [
        GameTarget(
            IsFlag("cheat", False)
            ),
        PersonTarget("lexi",
            InHarem("home"),
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "home_harem_achievement_5",
    "label": "home_harem_achievement_5",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("minami",
            InHarem('home'),
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "home_harem_achievement_6",
    "label": "home_harem_achievement_6",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        PersonTarget(samantha,
            InHarem('home'),
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label home_harem_achievement_1:
    $ home_harem_achievement_1.grant()
    return
label home_harem_achievement_2:
    $ home_harem_achievement_2.grant()
    return
label home_harem_achievement_3:
    $ home_harem_achievement_3.grant()
    return
label home_harem_achievement_4:
    $ home_harem_achievement_4.grant()
    return
label home_harem_achievement_5:
    $ home_harem_achievement_5.grant()
    return
label home_harem_achievement_6:
    $ home_harem_achievement_6.grant()
    return
label home_harem_achievement_7:
    $ home_harem_achievement_7.grant()
    return


init python:
    Event(**{
    "name": "jealous_harem_achievement_1",
    "label": "jealous_harem_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        TogetherInHarem('jealous', 'audrey', 'sasha'),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label jealous_harem_achievement_1:
    $ jealous_harem_achievement_1.grant()
    return
label jealous_harem_achievement_2:
    $ jealous_harem_achievement_2.grant()
    return
label jealous_harem_achievement_3:
    $ jealous_harem_achievement_3.grant()
    return


init python:
    Event(**{
    "name": "office_harem_achievement_1",
    "label": "office_harem_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        TogetherInHarem('office', 'aletta', 'audrey', 'lavish', 'shiori'),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label office_harem_achievement_1:
    $ office_harem_achievement_1.grant()
    return
label office_harem_achievement_2:
    $ office_harem_achievement_2.grant()
    return
label office_harem_achievement_3:
    $ office_harem_achievement_3.grant()
    return
label office_harem_achievement_4:
    $ office_harem_achievement_4.grant()
    return


init python:
    Event(**{
    "name": "pixie_harem_achievement_1",
    "label": "pixie_harem_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        TogetherInHarem('pixie', 'kleio', 'morgan'),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label pixie_harem_achievement_1:
    $ pixie_harem_achievement_1.grant()
    return
label pixie_harem_achievement_2:
    $ pixie_harem_achievement_2.grant()
    return
label pixie_harem_achievement_3:
    $ pixie_harem_achievement_3.grant()
    return


init python:
    Event(**{
    "name": "taming_harem_achievement_1",
    "label": "taming_harem_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        TogetherInHarem('taming', 'ayesha', 'kylie'),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label taming_harem_achievement_1:
    $ taming_harem_achievement_1.grant()
    return
label taming_harem_achievement_2:
    $ taming_harem_achievement_2.grant()
    return
label taming_harem_achievement_3:
    $ taming_harem_achievement_3.grant()
    return


label battle_of_bands_achievement_1:
    $ battle_of_bands_achievement_1.grant()
    return


init python:
    Event(**{
    "name": "job_achievement_1",
    "label": "job_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False),
                   IsFlag("capped_promotion", True)
                   ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label job_achievement_1:
    $ job_achievement_1.grant()
    return


init python:
    Event(**{
    "name": "pet_achievement_1",
    "label": "pet_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False),
                   Not(IsFlag("chosen_pet", False))
                   ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "animals_attack_achievement_1",
    "label": "animals_attack_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        "persistent.shark_attack == True",
        "persistent.bear_attack == True",
        "persistent.bird_attack == True",
        "persistent.dog_attack == True"
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label pet_achievement_1:
    $ pet_achievement_1.grant()
    return
label shark_achievement_1:
    $ shark_achievement_1.grant()
    return
label shark_achievement_2:
    $ shark_achievement_2.grant()
    return
label bear_achievement_1:
    $ bear_achievement_1.grant()
    return
label animals_attack_achievement_1:
    $ animals_attack_achievement_1.grant()
    return
label bear_shark_achievement_1:
    $ bear_shark_achievement_1.grant()
    return


label halloween_achievement_1:
    $ halloween_achievement_1.grant()
    return
label christmas_achievement_1:
    $ christmas_achievement_1.grant()
    return
label christmas_achievement_2:
    $ christmas_achievement_2.grant()
    return


init python:
    Event(**{
    "name": "sexperience_achievement_1",
    "label": "sexperience_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        "sum([girl.sexperience for girl in Person.all_people(ignore_hidden=False) if girl.sexperience]) >= 300"
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "sexperience_achievement_4",
    "label": "sexperience_achievement_4",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        "game.days_played < 80",
        "all([Person.find(g).sexperience >= 1 for g in ['aletta', 'alexis', 'anna', 'audrey', 'bree', 'camila', 'cassidy', 'emma', 'hanna', 'harmony', 'kleio', 'kylie', 'lavish', 'lexi', 'minami', 'morgan', 'palla', 'samantha', 'sasha', 'shiori']])",
        "not any([Person.find(g).is_gone_forever for g in ['aletta', 'alexis', 'anna', 'audrey', 'bree', 'camila', 'cassidy', 'emma', 'hanna', 'harmony', 'kleio', 'kylie', 'lavish', 'lexi', 'minami', 'morgan', 'palla', 'samantha', 'sasha', 'shiori']])"
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label sexperience_achievement_1:
    $ sexperience_achievement_1.grant()
    return
label sexperience_achievement_2:
    $ sexperience_achievement_2.grant()
    return
label sexperience_achievement_3:
    $ sexperience_achievement_3.grant()
    return
label sexperience_achievement_4:
    $ sexperience_achievement_4.grant()
    return
label bluepill_achievement_1:
    $ bluepill_achievement_1.grant()
    return


init python:
    Event(**{
    "name": "children_achievement_1",
    "label": "children_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        "sum([g.flags.mikeBabies for g in Person.all_people(ignore_hidden=False)]) >= 50"
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "children_achievement_2",
    "label": "children_achievement_2",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        "all([Person.find(g).flags.mikeBabies >= 1 for g in ['aletta', 'alexis', 'anna', 'audrey', 'ayesha', 'bree', 'camila', 'cassidy', 'emma', 'hanna', 'harmony', 'kleio', 'kylie', 'lavish', 'lexi', 'minami', 'morgan', 'palla', 'samantha', 'sasha', 'shiori']])"
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label children_achievement_1:
    $ children_achievement_1.grant()
    return
label children_achievement_2:
    $ children_achievement_2.grant()
    return


init python:
    Event(**{
    "name": "alone_achievement_1",
    "label": "alone_achievement_1",
    "conditions": [
        GameTarget(IsFlag("cheat", False)),
        "all(g.is_gone_forever for g in Girl.all() if g.id not in ['angela', 'natalie', 'cherie', 'claire', 'kiara'] + ([] if 'fafow' in DLCS else ['amy', 'kat', 'reona']))"
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label alone_achievement_1:
    $ alone_achievement_1.grant()
    return


label tea_achievement_1:
    $ tea_achievement_1.grant()
    return








define amy_achievement_1 = Achievement(
    id="amy_1",
    name="First kiss with Amy",
    description="Kiss Amy for the first time")
define amy_achievement_2 = Achievement(
    id="amy_2",
    name="Amy's hot coffee",
    description="Have fun with Amy for the first time")
define amy_achievement_3 = Achievement(
    id="amy_3",
    name="Amy's wedding",
    description="Get married with Amy")
define amy_achievement_4 = Achievement(
    id="amy_4",
    name="Amy's pregnancy",
    description="Get Amy pregnant")



define kat_achievement_1 = Achievement(
    id="kat_1",
    name="First kiss with Kat",
    description="Kiss Kat for the first time")
define kat_achievement_2 = Achievement(
    id="kat_2",
    name="Kat's hot coffee",
    description="Have fun with Kat for the first time")
define kat_achievement_3 = Achievement(
    id="kat_3",
    name="Kat's wedding",
    description="Get married with Kat")
define kat_achievement_4 = Achievement(
    id="kat_4",
    name="Kat's pregnancy",
    description="Get Kat pregnant")



define reona_achievement_1 = Achievement(
    id="reona_1",
    name="First kiss with Reona",
    description="Kiss Reona for the first time")
define reona_achievement_2 = Achievement(
    id="reona_2",
    name="Reona's hot coffee",
    description="Have fun with Reona for the first time")
define reona_achievement_3 = Achievement(
    id="reona_3",
    name="Reona's wedding",
    description="Get married with Reona")
define reona_achievement_4 = Achievement(
    id="reona_4",
    name="Reona's pregnancy",
    description="Get Reona pregnant")



define goth_harem_achievement_1 = Achievement(
    id="goth_harem_1",
    name="Ghouls 'n Goths",
    description="Have fun with Amy and Violaine")




define goth_harem_achievement_3 = Achievement(
    id="goth_harem_3",
    name="Ghouls 'n Goths 'n Goblins",
    description="Have fun with Amy, Violaine and Vincent")



define electronic_harem_achievement_1 = Achievement(
    id="electronic_harem_1",
    name="RadioShag",
    description="Have fun with Amy and Shawn")
define electronic_harem_achievement_2 = Achievement(
    id="electronic_harem_2",
    name="Shawn Business",
    description="Have fun with Amy, Palla, and Shawn")



define petite_harem_achievement_1 = Achievement(
    id="petite_harem_1",
    name="My little homies",
    description="Get in a four way relationship with Anna, Emma and Kat")
define petite_harem_achievement_2 = Achievement(
    id="petite_harem_2",
    name="Biggest of the world",
    description="Have fun with Anna, Emma and Kat")
define petite_harem_achievement_3 = Achievement(
    id="petite_harem_3",
    name="Poly pocket wives",
    description="Get married with all Anna, Emma and Kat")


















define thot_harem_achievement_1 = Achievement(
    id="thot_harem_1",
    name="Free spirits",
    description="Get in a three way relationship with Alexis and Reona")
define thot_harem_achievement_2 = Achievement(
    id="thot_harem_2",
    name="Debauchery",
    description="Have fun with Alexis and Reona")




define thot_harem_achievement_4 = Achievement(
    id="thot_harem_4",
    name="Three free spirits",
    description="Add Audrey to the Thot Harem")
define thot_harem_achievement_5 = Achievement(
    id="thot_harem_5",
    name="Libertines",
    description="Have fun with Alexis, Audrey and Reona")







define whore_harem_achievement_1 = Achievement(
    id="whore_harem_1",
    name="Bad company",
    description="Get in a three way relationship with Lexi and Reona")
define whore_harem_achievement_2 = Achievement(
    id="whore_harem_2",
    name="More than one trick up their sleeves",
    description="Have fun with Lexi and Reona")
define whore_harem_achievement_3 = Achievement(
    id="whore_harem_3",
    name="Tied the knot, tired nuts",
    description="Get married with all Lexi and Reona")




init python:
    Event(**{
    "name": "amy_achievement_1",
    "label": "amy_achievement_1",
    "conditions": [
        "'fafow' in DLCS",
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("amy",
            MinFlag("kiss", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "amy_achievement_2",
    "label": "amy_achievement_2",
    "conditions": [
        "'fafow' in DLCS",
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("amy",
            MinStat("sexperience", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "amy_achievement_4",
    "label": "amy_achievement_4",
    "conditions": [
        "'fafow' in DLCS",
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("amy",
            Or(
                MinFlag("pregnancies_number", 1),
                MinFlag("mikeBabies", 1)
                )
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label amy_achievement_1:
    $ amy_achievement_1.grant()
    return
label amy_achievement_2:
    $ amy_achievement_2.grant()
    return
label amy_achievement_3:
    $ amy_achievement_3.grant()
    return
label amy_achievement_4:
    $ amy_achievement_4.grant()
    return


init python:
    Event(**{
    "name": "kat_achievement_1",
    "label": "kat_achievement_1",
    "conditions": [
        "'fafow' in DLCS",
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("kat",
            MinFlag("kiss", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "kat_achievement_2",
    "label": "kat_achievement_2",
    "conditions": [
        "'fafow' in DLCS",
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("kat",
            MinStat("sexperience", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "kat_achievement_4",
    "label": "kat_achievement_4",
    "conditions": [
        "'fafow' in DLCS",
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("kat",
            Or(
                MinFlag("pregnancies_number", 1),
                MinFlag("mikeBabies", 1)
                )
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label kat_achievement_1:
    $ kat_achievement_1.grant()
    return
label kat_achievement_2:
    $ kat_achievement_2.grant()
    return
label kat_achievement_3:
    $ kat_achievement_3.grant()
    return
label kat_achievement_4:
    $ kat_achievement_4.grant()
    return


init python:
    Event(**{
    "name": "reona_achievement_1",
    "label": "reona_achievement_1",
    "conditions": [
        "'fafow' in DLCS",
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("reona",
            MinFlag("kiss", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "reona_achievement_2",
    "label": "reona_achievement_2",
    "conditions": [
        "'fafow' in DLCS",
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("reona",
            MinStat("sexperience", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "reona_achievement_4",
    "label": "reona_achievement_4",
    "conditions": [
        "'fafow' in DLCS",
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("reona",
            Or(
                MinFlag("pregnancies_number", 1),
                MinFlag("mikeBabies", 1)
                )
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label reona_achievement_1:
    $ reona_achievement_1.grant()
    return
label reona_achievement_2:
    $ reona_achievement_2.grant()
    return
label reona_achievement_3:
    $ reona_achievement_3.grant()
    return
label reona_achievement_4:
    $ reona_achievement_4.grant()
    return


label electronic_harem_achievement_1:
    $ electronic_harem_achievement_1.grant()
    return
label electronic_harem_achievement_2:
    $ electronic_harem_achievement_2.grant()
    return


label goth_harem_achievement_1:
    $ goth_harem_achievement_1.grant()
    return



label goth_harem_achievement_3:
    $ goth_harem_achievement_3.grant()
    return


init python:
    Event(**{
    "name": "petite_harem_achievement_1",
    "label": "petite_harem_achievement_1",
    "conditions": [
        "'fafow' in DLCS",
        GameTarget(IsFlag("cheat", False)),
        TogetherInHarem('petite', 'anna', 'emma', 'kat',),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label petite_harem_achievement_1:
    $ petite_harem_achievement_1.grant()
    return
label petite_harem_achievement_2:
    $ petite_harem_achievement_2.grant()
    return
label petite_harem_achievement_3:
    $ petite_harem_achievement_3.grant()
    return



























init python:
    Event(**{
    "name": "thot_harem_achievement_1",
    "label": "thot_harem_achievement_1",
    "conditions": [
        "'fafow' in DLCS",
        GameTarget(IsFlag("cheat", False)),
        TogetherInHarem('thot', 'alexis', 'reona',),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "thot_harem_achievement_4",
    "label": "thot_harem_achievement_4",
    "conditions": [
        "'fafow' in DLCS",
        GameTarget(IsFlag("cheat", False)),
        TogetherInHarem('thot', 'alexis', 'audrey', 'reona',),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label thot_harem_achievement_1:
    $ thot_harem_achievement_1.grant()
    return
label thot_harem_achievement_2:
    $ thot_harem_achievement_2.grant()
    return



label thot_harem_achievement_4:
    $ thot_harem_achievement_4.grant()
    return
label thot_harem_achievement_5:
    $ thot_harem_achievement_5.grant()
    return





init python:
    Event(**{
    "name": "whore_harem_achievement_1",
    "label": "whore_harem_achievement_1",
    "conditions": [
        "'fafow' in DLCS",
        GameTarget(IsFlag("cheat", False)),
        TogetherInHarem('whore', 'lexi', 'reona',),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label whore_harem_achievement_1:
    $ whore_harem_achievement_1.grant()
    return
label whore_harem_achievement_2:
    $ whore_harem_achievement_2.grant()
    return
label whore_harem_achievement_3:
    $ whore_harem_achievement_3.grant()
    return








define cherie_achievement_1 = Achievement(
    id="cherie_1",
    name="First kiss with Cherie",
    description="Kiss Cherie for the first time")
define cherie_achievement_2 = Achievement(
    id="cherie_2",
    name="Cherie's hot coffee",
    description="Have fun with Cherie for the first time")
define cherie_achievement_3 = Achievement(
    id="cherie_3",
    name="Cherie's wedding",
    description="Get married with Cherie")
define cherie_achievement_4 = Achievement(
    id="cherie_4",
    name="Cherie's pregnancy",
    description="Get Cherie pregnant")



define claire_achievement_1 = Achievement(
    id="claire_1",
    name="First kiss with Claire",
    description="Kiss Claire for the first time")
define claire_achievement_2 = Achievement(
    id="claire_2",
    name="Claire's hot coffee",
    description="Have fun with Claire for the first time")
define claire_achievement_3 = Achievement(
    id="claire_3",
    name="Claire's wedding",
    description="Get married with Claire")
define claire_achievement_4 = Achievement(
    id="claire_4",
    name="Claire's pregnancy",
    description="Get Claire pregnant")



define kiara_achievement_1 = Achievement(
    id="kiara_1",
    name="First kiss with Kiara",
    description="Kiss Kiara for the first time")
define kiara_achievement_2 = Achievement(
    id="kiara_2",
    name="Kiara's hot coffee",
    description="Have fun with Kiara for the first time")
define kiara_achievement_3 = Achievement(
    id="kiara_3",
    name="Kiara's wedding",
    description="Get married with Kiara")
define kiara_achievement_4 = Achievement(
    id="kiara_4",
    name="Kiara's pregnancy",
    description="Get Kiara pregnant")



















init python:
    Event(**{
    "name": "cherie_achievement_1",
    "label": "cherie_achievement_1",
    "conditions": [
        "'fafwm' in DLCS",
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("cherie",
            MinFlag("kiss", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "cherie_achievement_2",
    "label": "cherie_achievement_2",
    "conditions": [
        "'fafwm' in DLCS",
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("cherie",
            MinStat("sexperience", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "cherie_achievement_4",
    "label": "cherie_achievement_4",
    "conditions": [
        "'fafwm' in DLCS",
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("cherie",
            Or(
                MinFlag("pregnancies_number", 1),
                MinFlag("mikeBabies", 1)
                )
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label cherie_achievement_1:
    $ cherie_achievement_1.grant()
    return
label cherie_achievement_2:
    $ cherie_achievement_2.grant()
    return
label cherie_achievement_3:
    $ cherie_achievement_3.grant()
    return
label cherie_achievement_4:
    $ cherie_achievement_4.grant()
    return


init python:
    Event(**{
    "name": "claire_achievement_1",
    "label": "claire_achievement_1",
    "conditions": [
        "'fafwm' in DLCS",
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("claire",
            MinFlag("kiss", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "claire_achievement_2",
    "label": "claire_achievement_2",
    "conditions": [
        "'fafwm' in DLCS",
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("claire",
            MinStat("sexperience", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "claire_achievement_4",
    "label": "claire_achievement_4",
    "conditions": [
        "'fafwm' in DLCS",
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("claire",
            Or(
                MinFlag("pregnancies_number", 1),
                MinFlag("mikeBabies", 1)
                )
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label claire_achievement_1:
    $ claire_achievement_1.grant()
    return
label claire_achievement_2:
    $ claire_achievement_2.grant()
    return
label claire_achievement_3:
    $ claire_achievement_3.grant()
    return
label claire_achievement_4:
    $ claire_achievement_4.grant()
    return


init python:
    Event(**{
    "name": "kiara_achievement_1",
    "label": "kiara_achievement_1",
    "conditions": [
        "'fafwm' in DLCS",
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("kiara",
            MinFlag("kiss", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "kiara_achievement_2",
    "label": "kiara_achievement_2",
    "conditions": [
        "'fafwm' in DLCS",
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("kiara",
            MinStat("sexperience", 1)
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

    Event(**{
    "name": "kiara_achievement_4",
    "label": "kiara_achievement_4",
    "conditions": [
        "'fafwm' in DLCS",
        GameTarget(IsFlag("cheat", False)),
        PersonTarget("kiara",
            Or(
                MinFlag("pregnancies_number", 1),
                MinFlag("mikeBabies", 1)
                )
            ),
        ],
    "priority": 1000,
    "do_once": True,
    "quit": False,
    })

label kiara_achievement_1:
    $ kiara_achievement_1.grant()
    return
label kiara_achievement_2:
    $ kiara_achievement_2.grant()
    return
label kiara_achievement_3:
    $ kiara_achievement_3.grant()
    return
label kiara_achievement_4:
    $ kiara_achievement_4.grant()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
