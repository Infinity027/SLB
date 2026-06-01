init offset = -1

style default:
    properties gui.text_properties()
    language gui.language
    emoji_font "gui/fonts/NotoEmoji/NotoEmoji-Bold.ttf"

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    font "palanquin_bold"
    hover_color "#ffffff"
    idle_color "#006284"
    size 20
    xalign 0.5
    yalign 0.5

style invisible_button is gui_button:
    background None

style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")

style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"

style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

style invisible_frame is frame:
    background None




















screen say(who, what, person=None):
    zorder 2
    style_prefix "say"

    frame:
        xsize 800
        ysize 144
        yanchor "bottom"
        ypos 700
        xalign 0.5

        background Transform(im.Scale("gui/textbox.png", 800, 144), alpha=persistent.window_opacity)

        if who:
            window:
                style "namebox"
                pos -30, -30
                $ Who = who.upper()
                hbox:
                    yalign 0.5
                    spacing 10
                    hbox:
                        xminimum 168
                        text Who xpos 5 yalign 0.5 font "palanquin_bold" size 25 color "#006284"
                    if isinstance(person, Person):
                        add f"sayicon {person.id}" yalign 0.5
                    elif isinstance(person, Hero):
                        if hero.is_female:
                            add "sayicon bree" yalign 0.5
                        else:
                            add "sayicon mike" yalign 0.5
                    elif renpy.exists(f"gui/action_icons/button_{who}.png"):
                        add f"gui/action_icons/button_{who}.png" xysize (40, 40) yalign 0.5

        frame:
            style "invisible_frame"
            xsize 780
            ysize 120
            xpos 10
            ypos 15
            text what font "exo2_regular" size 23 color "#ffffff" id "what" align 0.0,0.0








    add SideImage() xalign 0.0 yalign 1.0


init python:
    config.character_id_prefixes.append('namebox')

style say_window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style say_window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Transform("gui/textbox.png", xalign=0.5, yalign=0.9, xsize=0.9, ysize=0.9, alpha=1.0)


style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    xminimum 218

    background Frame("gui/pname_box.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5
    color "#006284"

style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    font "exo2_regular"
    size 23
    color "#ffffff"
    outlines [( 1, "#00688C80", 0, 0)]
    outline_scaling "step"
    adjust_spacing False











screen input(prompt):
    modal True
    zorder 200
    style_prefix "confirm"

    frame:
        xysize 560,80
        xalign 0.5
        yalign 0.5
        vbox:

            input id "input" color "#ffffff"

            hbox:
                xalign 0.5
                spacing 10

        frame:
            minimum 0, 47
            maximum 550, 47
            background Frame("gui/pname_box.png", Borders(15, 15, 15, 15), tile=gui.frame_tile)
            xalign 0
            text prompt xpos -25 ypos -35 font "palanquin_bold" size 20 color "#006284"

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width










define shuffle_choices = True
init python:
    renpy_menu = menu
    typical_cancel_sentences = (
    "back",
    "cancel",
    "do nothing",
    "exit",
    "leave",
    "nevermind",
    "no, i don't",
    "no, nothing...",
    "not really",
    "not yet",
)

    def menu(items):
        last_choices = [i for i in items if "(FORCE_LAST)" in i[0]]
        cancel_choices = [i for i in items if i not in last_choices and i[0].strip().lower() in typical_cancel_sentences]
        valid_choices = [i for i in items if i not in last_choices and i not in cancel_choices]
        if persistent.choices_shuffle and shuffle_choices:
            renpy.random.shuffle(valid_choices)
        items = valid_choices + cancel_choices + [type(c)([c[0].replace("(FORCE_LAST)", "")] + list(c[1:])) for c in last_choices]
        return renpy_menu(items)

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

screen orbit_choice(items):
    default current_choice = items[0]
    style_prefix "choice_round"
    vbox:
        xsize 0.75
        xalign 0.5
        yalign 0.5
        spacing 20
        hbox:
            box_justify True
            textbutton _("<") action [SetScreenVariable("current_choice", find_prev(current_choice, items))] xysize (47, 47)
            textbutton _(current_choice.caption) action current_choice.action style "choice_button" xsize 0.5 ysize 47 text_yalign 0.3
            textbutton _(">") action [SetScreenVariable("current_choice", find_next(current_choice, items))] xysize (47, 47)
        hbox:
            xalign 0.5
            box_justify True
            spacing 20
            for i in current_choice.kwargs.get("displayed_fiances"):
                add Composite(
                    (50, 50),
                    (0, 0), "gui/phone/ico_phone_idle.png",
                    (15, 15), f"gui/action_icons/button_{i}.png"
                    ):
                    at Position(anchor=(0.5, 0.5))


define config.narrator_menu = True

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    yalign 0.5
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    background Frame("gui/choicebox_idle.png", Borders(100, 5, 100, 5))
    hover_background Frame("gui/choicebox_hover.png", Borders(100, 5, 100, 5))

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    font "exo2_regular"
    hover_color "#ffffff"
    idle_color "#ffffff"
    insensitive_color "#ffffff"

style choice_round_text is text:
    xalign 0.5

style choice_round_button is button:
    background Frame("gui/button/choice_round_idle.png")
    hover_background Frame("gui/button/choice_round_hover.png")


style choice_round_button_text is text:
    align (0.5, 0.5)






screen quick_menu():


    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"
            style "quick_menu"

            textbutton _("Back") action Rollback()

            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")

            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()





init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = False

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 1.0

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")
    font "DejaVuSans.ttf"
    hover_color "#0099ff"
    insensitive_color "#aaaaaa7f"











screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            if persistent.start_plus:
                textbutton _("Start plus") action Start("start_plus")
            else:
                textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("game_save")

        textbutton _("Load") action ShowMenu("load")



        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc"):


            textbutton _("controls") action ShowMenu("help")

            textbutton _("Quit") action Quit()

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")







init -2:
    define main_menu_configuration = "main_menu_generic"

screen main_menu():
    tag menu
    use expression main_menu_configuration

    if renpy.has_screen("advertising"):
        use advertising('vertical', box_offset=(25, 0), button_bg_border_size=12, button_bg_idle=Frame("gui/confirm_frame.png"), button_bg_hover="#ea6383", arrow_idle_color="#52b2e6", arrow_hover_color="#ea6383", zoom=0.85)






style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 0.5
    xoffset -20
    yalign 1.0
    yoffset -5

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    font "exo2_light"
    size 18
    xalign 0.97
    yalign 0.97
    color "#ffffff"
    properties gui.text_properties("version")

style information_panel is main_menu
style information_panel_text is main_menu_text
style information_panel_vbox is main_menu_vbox
style information_panel_button is main_menu_button
style information_panel_button_text is main_menu_button_text

style information_panel_button_text:
    xalign 0.85
    yalign 0.7
    hover_size 24
    outlines [ (absolute(1), "#006488", absolute(0), absolute(0)) ]


style information_panel_vbox:
    xoffset 0
    yoffset 0

style information_panel_button:
    xalign 1.0
    xsize 300
    background Frame(Transform("gui/phone/empty_idle.png", xzoom=-1.0))
    hover_background Frame(Transform("gui/phone/empty_hover.png", xzoom=-1.0))










screen game_menu(title='', scroll=None, yinitial=0.0, spacing=0):
    tag menu
    style_prefix "game_menu"
    key ["K_ESCAPE", "mouseup_3", "pad_b_press"] action Return()
    modal True
    if not is_sub_screen():
        vbox:
            spacing 5
            align 0.5, 0.5
            frame:
                background Frame("gui/prompt/prompt_box.png")
                xsize 760
                align 0.5, 0.5
                has vbox
                spacing 5
                align 0.5, 0.5
                null height 10
                textbutton "RESUME" action Return() default_focus check_controller()
                textbutton "SAVE" action [ShowMenu("game_save"), Hide("game_menu")]
                textbutton "LOAD" action ShowMenu("load")
                textbutton "OPTIONS" action ShowMenu("preferences")
                textbutton "GALLERY" action [SensitiveIf(persistent.start_plus), If(GALLERY_WARNING, ShowMenu("main_gallery"), ShowMenu("warning_gallery"))]
                if renpy.variant("pc"):
                    textbutton _("CONTROLS") action ShowMenu("help")
                null height 10
                textbutton "MAIN MENU" action MainMenu(confirm=True)
                textbutton "QUIT" action Quit(confirm=True)
                null height 15
            textbutton "Report Bug" action OpenURL("https://discord.com/channels/392691429840781315/481382104802918400") style "bug_button" xalign 0.0

style game_menu_button is main_menu_button
style game_menu_button_text is main_menu_button_text:
    font "palanquin_regular"
    color "#fff"

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_return_button:
    xsize 315
    xalign 0.5
    yalign 1.0
    yoffset -30

style game_menu_return_button_text:
    color "#ffffff"

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30

style bug_button is custom_button
style bug_button_text is gui_text:
    align (0.5, 0.5)
    size 18
    font "exo2_bold"
    color "#ffffff"








screen about():
    tag menu





    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size










screen load_save_slot(number):
    $ save_name = FileSaveName(number)
    frame:
        align (0.5, 0.5)
        style "empty"
        add FileScreenshot(number) size 279, 154 align (0.5, 0.5)
        add "gui/main/screenshot_mask.png" align (0.5, 0.5)
        text FileTime(number) yalign 1.15 style "slot_save_load_text"
        text "[save_name!q]" yalign 1.35 style "slot_save_load_text"

    key "save_delete" action FileDelete(number)

screen access_slots():
    if renpy.get_screen('game_save') and FileCurrentPage() == "auto":
        $ FilePage("quick")

    hbox:
        style_prefix "page"
        xsize 1015
        ysize 36
        yalign 0.90
        xalign 0.50

        hbox:
            xalign 0.0
            if config.has_autosave and not renpy.get_screen('game_save'):
                textbutton _("{#auto_page}A") action FilePage("auto") keysym "K_a"

            if config.has_quicksave:
                textbutton _("{#quick_page}Q") action FilePage("quick") keysym "K_q"

        hbox:
            xalign 0.5
            xsize 700

            if FileCurrentPage() in ["auto", "quick"] or int(FileCurrentPage()) <= 5:
                $ page_range = range(1, 10)
            else:
                $ page_range = range(int(FileCurrentPage()) - 4, int(FileCurrentPage()) + 5)
            for page in page_range:
                textbutton "[page]" action FilePage(page)

        hbox:
            xalign 1.0
            if FileCurrentPage() in ["auto", "quick"] or int(FileCurrentPage()) - 5 < 1:
                $ page_min = 1
                $ page_max = 6
            else:
                $ page_min = int(FileCurrentPage()) - 5
                $ page_max = int(FileCurrentPage()) + 5
            textbutton _("<<") action FilePage(page_min) keysym "shift_mousedown_4"
            textbutton _("<") action FilePagePrevious() keysym 'noshift_mousedown_4'
            textbutton _(">") action FilePageNext() keysym 'noshift_mousedown_5'
            textbutton _(">>") action FilePage(page_max) keysym "shift_mousedown_5"

screen save_name_dialogue(slotnumber):
    modal True
    zorder 200
    style_prefix "confirm"

    frame:
        style "invisible_frame"
        xysize 545, 130
        yalign 0.5
        xalign 0.5
        frame:
            yalign 0.5
            xalign 0.5
            xysize 450,60
            background Frame("gui/prompt/prompt_box.png", Borders(40, 40, 40, 40))
            input value SaveNameValue('save_name', slotnumber) exclude "*{}[]()" size 20 color "#FFF" length 34 ypos -20
        textbutton "Save Name":
            xysize 180, 45
            xalign 0.05
            text_size 20
            text_color "#006284"
            background Frame("gui/pname_box.png", Borders(15, 15, 15, 15), tile=gui.frame_tile)
        textbutton "Save" style "custom_button" action [FileSave(slotnumber), Hide('save_name_dialogue')] xalign 0.95 yalign 0.85


style custom_button:
    xpadding 15
    background Frame("gui/button_idle.png", Borders(15, 15, 15, 15), tile=gui.frame_tile)
    hover_background Frame("gui/button_hover.png", Borders(15, 15, 15, 15), tile=gui.frame_tile)

style custom_button_text is gui_text:
    xalign 0.5
    size 20
    font "exo2_bold"
    color "#ffffff"

screen save_name_dialogue(slotnumber):
    modal True
    zorder 200
    style_prefix "confirm"
    variant "small"

    frame:
        style "invisible_frame"
        xysize 545, 130
        yalign 0.25
        xalign 0.5
        frame:
            yalign 0.5
            xalign 0.5
            xysize 450,60
            background Frame("gui/prompt/prompt_box.png", Borders(40, 40, 40, 40))
            input value SaveNameValue('save_name', slotnumber) exclude "*{}[]()" size 20 color "#FFF" length 34 ypos -20
        textbutton "Save Name":
            xysize 180, 45
            xalign 0.05
            text_size 20
            text_color "#006284"
            background Frame("gui/pname_box.png", Borders(15, 15, 15, 15), tile=gui.frame_tile)
        textbutton "Save" style "custom_button" action [FileSave(slotnumber), Hide('save_name_dialogue')] xalign 0.95 yalign 0.8


screen save():
    use game_menu()

screen game_save():
    key ["K_ESCAPE", "mouseup_3", "pad_b_press"] action [Hide("game_save"), Return()]
    use file_slots('game_save')
    button style "return_arrow_button" action [Hide("game_save"),Return()] tooltip ""

screen load():
    key ["K_ESCAPE", "mouseup_3", "pad_b_press"] action [Hide("load"), Return()]
    use file_slots('load')
    button style "return_arrow_button" action [Hide("load"),Return()] tooltip ""

screen file_slots(title):
    zorder 50 tag menu


    if renpy.get_screen('game_save'):
        add "gui/main/save_bg.png"
    else:
        add "gui/main/load_bg.png"


    $ positions = [(133, 143), (498, 143), (850, 143), (133, 377), (498, 377), (850, 377)]


    for i, pos in enumerate(positions, start=1):
        button style "slot_save_load_button" pos pos default_focus (1 if i == 0 and check_controller() else 0):
            if renpy.get_screen('game_save'):
                action [SetVariable('save_name', FileSaveName(i)), ShowMenu('save_name_dialogue', i)]
            else:
                action FileLoad(i)
            use load_save_slot(number=i)

    use access_slots()

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is invisible_button:
    align (0.5, 0.5)

style slot_save_load_button:
    background "gui/main/button_saveload_idle.png"
    hover_background "gui/main/button_saveload_hover.png"
    selected_idle_background Transform("gui/main/button_saveload_selected_idle.png", matrixcolor=SaturationMatrix(0))
    xysize (298, 173)

style slot_save_load_text:
    xalign 0.5
    size 20
    color "#ffffff"
    outlines [(3, "#006284", 0, 0)]

style return_arrow_button:
    background "gui/return_idle.png"
    hover_background "gui/return_hover.png"
    xysize (57, 44)
    align (0.95, 0.1)

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button_text:
    properties gui.text_properties("page_button")
    font "palanquin_medium"
    yalign 0.5
    size 32
    color "#61bbe7"
    outlines [(2, "#00678b")]
    selected_color "#7d7d7d"
    selected_outlines [(2, "#ffffff")]
    hover_color "#e76e8a"
    hover_outlines [(2, "#ffffff")]

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")








style lspref_slider:
    ysize 31
    xsize 343
    left_bar Frame("gui/main/bar_left.png")
    right_bar Frame("gui/main/bar_right.png")
    thumb "gui/main/bar_thumb_idle.png"
    thumb_offset 10
    left_gutter 10.5
    right_gutter 10.5

style lspref_text:
    color "#ffffff"
    xalign 0.5
    yalign 0.5
    font "exo2_bold"

style lspref_label_text:
    color "#ffffff"
    font "palanquin_bold"
    size 30
    outlines [(2, "#006284")]

style lspref_label_text_title:
    color "#62ACD1"
    font "palanquin_bold"
    size 40
    outlines [(3, "#000000")]

style lspref_button:
    idle_background "gui/small_button_idle.png"
    hover_background "gui/small_button_hover.png"
    selected_background "gui/small_button_selected_idle.png"
    selected_hover_background "gui/small_button_idle.png"
    yalign 0.5
    ysize 39
    xsize 230

style lspref_button_text is lspref_text

screen text_tooltip(textvalue="_text", texttooltip="_tooltip", textstyle="text"):
    frame:
        style "invisible_frame"
        has button
        style "invisible_button"
        action NullAction()
        yalign 0.5
        text textvalue yalign 0.5 style textstyle
        tooltip texttooltip

screen preferences():
    tag menu
    style_prefix "lspref"
    add "gui/main/prefs_bg2.png"
    key ["K_ESCAPE", "mouseup_3", "pad_b_press"] action [Hide("preferences"), Return()]
    zorder 50

    frame:
        style "invisible_frame"
        minimum 1100,500
        maximum 1100,500
        ypos 150
        xalign 0.5
        viewport id "prefs":
            draggable True
            mousewheel True
            has vbox
            spacing 40
            vbox:
                spacing 20
                use text_tooltip(text_tag_resize(_("Global Setting:"), 343, 30), "", "lspref_label_text_title")
                hbox:
                    box_wrap True
                    spacing 20
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(text_tag_resize(_("Force update check"), 230, 30), _("Force the check for new version"), "lspref_label_text")
                        textbutton _("Force update") action [SetVariable("persistent._update_last_checked", {}), SetVariable("persistent._update_version", {})]
                    if renpy.android:
                        if config.basedir.endswith('base'):

                            vbox:
                                xysize (450, 60)
                                use text_tooltip(text_tag_resize(_("Downloader:"), 450, 30), "", "lspref_label_text_title")
                                use text_tooltip(text_tag_resize(_("Force downloader startup"), 450, 30), _("Force launch downloader instead of the game"), "lspref_label_text")
                                textbutton text_tag_resize(_("Startup downloader"), 450) selected os.environ.get("USE_DOWNLOADER") action Function(search_in_path)
                        vbox:
                            xysize (300, 60)
                            use text_tooltip(text_tag_resize(_("DLCs:"), 300, 30), "", "lspref_label_text_title")
                            use text_tooltip(text_tag_resize(_("DLC Location"), 300, 30), _("Relocate your DLC file for the game to correctly load it (restart the game after locating the file)"), "lspref_label_text")
                            textbutton text_tag_resize(_("Import DLC file"), 300) action Function(move_rpa)
            vbox:
                spacing 20
                use text_tooltip(text_tag_resize(_("Video Setting:"), 343, 30), "", "lspref_label_text_title")
                hbox:
                    box_wrap True
                    spacing 20
                    if renpy.variant("pc"):
                        vbox:
                            xysize (230, 60)
                            use text_tooltip(text_tag_resize(_("Screen Display"), 230, 30), _("Change the game's window display"), "lspref_label_text")
                            textbutton _("Window") action Preference("display", "window")
                            textbutton _("Fullscreen") action Preference("display", "fullscreen")
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(text_tag_resize(_("Powersave"), 230, 30), _("Turn on, save power and reduce heat by updating the screen less often.\nTurn off for smoother visuals but higher power use."), "lspref_label_text")
                        textbutton _("Enable") action Preference("gl powersave", True)
                        textbutton _("Disable") action Preference("gl powersave", False)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_("New UI"), _("Enable new UI"), "lspref_label_text")
                        textbutton _("On") action SetField(persistent, 'new_ui', True)
                        textbutton _("Off") action SetField(persistent, 'new_ui', False)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(_("X-Ray"), _("Allow to see through body during some scenes"), "lspref_label_text")
                        textbutton _("On") action SetField(persistent, 'xray', True)
                        textbutton _("Off") action SetField(persistent, 'xray', False)
                    # LIVE2D DISABLED — the Animations (Live2D) on/off toggle is hidden so it
                    # cannot be re-enabled. To restore, change "if False" back to:
                    #   if renpy.has_live2d() and any(dlc in DLCS for dlc in ('lively', 'fafow', 'fafwm')):
                    if False:
                        vbox:
                            xysize (230, 60)
                            use text_tooltip(text_tag_resize(_("Animations"), 230, 30), _("Enable/Disable sprites animations"), "lspref_label_text")
                            textbutton _("On") action SetField(persistent, 'live2d_on', True)
                            textbutton _("Off") action SetField(persistent, 'live2d_on', False)
                    if 'lively' in DLCS:
                        vbox:
                            xysize (230, 60)
                            use text_tooltip(text_tag_resize(_("Lively backgrounds"), 230, 30), _("Enable/Disable sprites in backgrounds"), "lspref_label_text")
                            textbutton _("On") action SetField(persistent, 'lively_bg', True)
                            textbutton _("Off") action SetField(persistent, 'lively_bg', False)
            vbox:
                spacing 20
                use text_tooltip(text_tag_resize(_("Gameplay Setting:"), 343, 30), "", "lspref_label_text_title")
                hbox:
                    box_wrap True
                    spacing 20
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(text_tag_resize(_("Tutorial"), 230, 30), _("Enable/Disable the tutorial at the start of a new game"), "lspref_label_text")
                        textbutton _("Show") action SetField(persistent, 'skip_tutorial', False)
                        textbutton _("Skip") action SetField(persistent, 'skip_tutorial', True)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(text_tag_resize(_("Difficulty"), 230, 30), _("Change the game difficulty"), "lspref_label_text")
                        textbutton _("Easy") action SetField(persistent, 'difficulty', -1)
                        textbutton _("Normal") action SetField(persistent, 'difficulty', 0)
                        textbutton _("Difficult") action SetField(persistent, 'difficulty', 1)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(text_tag_resize(_("Random Schedule"), 230, 30), _("Allow non-player characters to choose among several locations during this routine"), "lspref_label_text")
                        textbutton _("On") action SetField(persistent, 'schedule_randomness', True)
                        textbutton _("Off") action SetField(persistent, 'schedule_randomness', False)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(text_tag_resize(_("Random Needs"), 225, 30), _("The need's cost can fluctuate when performing actions"), "lspref_label_text")
                        textbutton _("On") action SetField(persistent, 'needs_randomness', True)
                        textbutton _("Off") action SetField(persistent, 'needs_randomness', False)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(text_tag_resize(_("Shuffle Choices"), 225, 30), _("Modify the order of the selections in nearly all of the menu choices"), "lspref_label_text")
                        textbutton _("On") action SetField(persistent, 'choices_shuffle', True)
                        textbutton _("Off") action SetField(persistent, 'choices_shuffle', False)

                    vbox:
                        xysize (230, 60)
                        use text_tooltip(text_tag_resize(_("Notifications pop-up"), 230, 30), _("Enable/Disable the notification pop-up"), "lspref_label_text")
                        textbutton _("Show") action SetField(persistent, 'notifications', True)
                        textbutton _("Hide") action SetField(persistent, 'notifications', False)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(text_tag_resize(_("Pregnancy duration"), 230, 30), _("Change the pregnancy duration to suit your preference"), "lspref_label_text")
                        textbutton _("Endless") action SetField(persistent, 'pregnancy_end', False)
                        textbutton _("Immersive") action SetField(persistent, 'pregnancy_end', True)
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(text_tag_resize(_("Pregnancy pop-up"), 230, 30), _("Enable/Disable pregnancy pop-up"), "lspref_label_text")
                        textbutton _("Show") action SetField(persistent, 'pregnancy_notification', True)
                        textbutton _("Hide") action SetField(persistent, 'pregnancy_notification', False)
                    if persistent.start_plus:
                        vbox:
                            xysize (230, 60)
                            use text_tooltip(text_tag_resize(_("Reset NG+"), 230, 30), _("Clear NG+ saved statistics"), "lspref_label_text")
                            textbutton _("Clear stats") action Confirm("You're going to clear NG+ statistics.", Function(game.clear_new_game_plus))
                    if Achievement.total_unlocked:
                        vbox:
                            xysize (230, 60)
                            use text_tooltip(text_tag_resize(_("Reset Achievements"), 230, 30), _("Clear all unlocked achievements"), "lspref_label_text")
                            textbutton _("Clear achievements") action Confirm("You're going to clear achievements.", Function(Achievement.reset))
                    if check_controller():
                        vbox:
                            xysize (230, 60)
                            use text_tooltip(text_tag_resize(_("Frame Selector"), 230, 30), _("Allow to see selection with a framed border"), "lspref_label_text")
                            textbutton _("On") action SetField(persistent, 'selector', True)
                            textbutton _("Off") action SetField(persistent, 'selector', False)
            vbox:
                spacing 20
                use text_tooltip(text_tag_resize(_("Dialogue Setting:"), 343, 30), "", "lspref_label_text_title")
                hbox:
                    box_wrap True
                    spacing 20
                    vbox:
                        xysize (343, 60)
                        use text_tooltip(text_tag_resize(_("Text Speed"), 343, 30), _("Controls the rate at which text displays.\nThe further to the right this slider is, the faster the text will display.\nAll the way to the right causes text to be shown instantly."), "lspref_label_text")
                        bar value Preference("text speed")
                    vbox:
                        xysize (343, 60)
                        use text_tooltip(text_tag_resize(_("Auto forward Time"), 343, 30), _("Controls automatic advance.\nThe further to the left this slider is, the shorter the amount of time before the game advances.\nAll the way to the right means text will never auto-forward."), "lspref_label_text")
                        bar value Preference("auto-forward time")
                hbox:
                    box_wrap True
                    spacing 20
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(text_tag_resize(_("Rollback Side"), 230, 30), _("Enable a side of the screen to causes rollback"), "lspref_label_text")
                        textbutton _("Disable") action Preference("rollback side", "disable")
                        textbutton _("Left") action Preference("rollback side", "left")
                        textbutton _("Right") action Preference("rollback side", "right")
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(text_tag_resize(_("Skip"), 230, 30), _("Allow the game to skipping parts, like texts or transitions"), "lspref_label_text")
                        textbutton _("Unseen Text") action Preference("skip", "toggle")
                        textbutton _("After Choices") action Preference("after choices", "toggle")
                        textbutton _("Transitions") action Preference("transitions", "toggle")
            vbox:
                spacing 20
                use text_tooltip(text_tag_resize(_("Audio Setting:"), 343, 30), "", "lspref_label_text_title")
                hbox:
                    box_wrap True
                    spacing 20
                    vbox:
                        xysize (343, 60)
                        use text_tooltip(text_tag_resize(_("Music Volume"), 343, 30), _("Controls the volume of the music.\nThe further to the right these are, the louder the volume."), "lspref_label_text")
                        bar value Preference("music volume")
                    vbox:
                        xysize (343, 60)
                        use text_tooltip(text_tag_resize(_("Sound Volume"), 343, 30), _("Controls the volume of the sounds.\nThe further to the right these are, the louder the volume."), "lspref_label_text")
                        bar value Preference("sound volume")
                    vbox:
                        xysize (343, 60)
                        use text_tooltip(text_tag_resize(_("Voice Volume"), 343, 30), _("Controls the volume of the voices.\nThe further to the right these are, the louder the volume."), "lspref_label_text")
                        bar value Preference("voice volume")
                    vbox:
                        xysize (343, 60)
                        use text_tooltip(text_tag_resize(_("Ambience Volume"), 343, 30), _("Controls the volume of the sound ambience.\nThe further to the right these are, the louder the volume."), "lspref_label_text")
                        bar value Preference("ambience volume")
                    vbox:
                        xysize (343, 60)
                        use text_tooltip(text_tag_resize(_("Sex Sounds Volume"), 343, 30), _("Controls the volume of the sex sounds.\nThe further to the right these are, the louder the volume."), "lspref_label_text")
                        bar value Preference("sexsfx volume")
                hbox:
                    box_wrap True
                    spacing 20
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(text_tag_resize(_("Mute audio"), 230, 30), _("Enable/Disable game audio"), "lspref_label_text")
                        textbutton _("Mute all") action Preference("all mute", "toggle") alt f"Mute all is {'On' if persistent.mute_characters else 'Off'}."
                        textbutton _("Mute alarm clock") selected persistent.mute_alarm_clock action ToggleField(persistent, 'mute_alarm_clock', True, False) alt f"Alarm clock sound is {'On' if not persistent.mute_alarm_clock else 'Off'}."
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(text_tag_resize(_("Mute voice"), 230, 30), _("Enable/Disable character voice"), "lspref_label_text")
                        textbutton _("Mute Bree") action [ToggleVoiceMute("bree")] alt f"Mute Bree is {'On' if 'bree' in persistent._voice_mute else 'Off'}."
                        textbutton _("Mute Mike") action [ToggleVoiceMute("mike")] alt f"Mute Mike is {'On' if 'mike' in persistent._voice_mute else 'Off'}."
                        textbutton _("Mute all characters") selected persistent.mute_characters action Function(toggle_mute_all_characters) alt f"Mute all characters is {'On' if persistent.mute_characters else 'Off'}."
                    vbox:
                        xysize (230, 60)
                        use text_tooltip(text_tag_resize(_("Self-voicing"), 230, 30), _("Self-voicing setting"), "lspref_label_text")
                        textbutton _("Override voice") selected persistent.tts_override action Function(toggle_tts_override_voice_channel) alt f"Self-voicing override voice is {'On' if persistent.tts_override else 'Off'}."
        vbar:
            value YScrollValue("prefs")
            left_bar "gui/inv/vertical_idle_bar.png"
            right_bar "gui/inv/vertical_idle_bar.png"
            thumb "gui/inv/vertical_idle_thumb.png"
            thumb_offset 63
            left_gutter 63
            right_gutter 63
            maximum 11,359
            xpos 1100
            yalign 0.5
    button style "return_arrow_button" action [Hide("preferences"),Return()] tooltip "" default_focus check_controller()

    $ tooltip = GetTooltip()
    if tooltip:
        nearrect:
            focus "tooltip"
            style_prefix "tooltips"

            has frame
            yanchor 0
            xalign 0.5
            xpadding 20
            text tooltip substitute False yalign 0.05

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 450










screen history():
    tag menu



    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:


                has fixed
                yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False



                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")




define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5







style help_label is text:
    color "#ffffff"
    font "palanquin_bold"
    size 24
    xanchor 1.0
    xalign 1.0
    yalign 0.5

style help_t is text:
    color "#ffffff"
    font "exo2_regular"
    size 24
    yalign 0.5

screen help():
    tag menu
    add "gui/main/bg.png" blur 5
    key ["K_ESCAPE", "mouseup_3", "pad_b_press"] action [Hide("help"), Return()]

    if check_controller():
        frame:
            style "empty"
            background Solid("#00000080")

            text "GAMEPAD" color "#ffffff" font "palanquin_bold" size 24 xalign 0.5 ypos 100

            vbox:
                ypos 150
                xalign 0.5
                spacing 30
                xsize 700
                hbox xalign 0.5 xsize 700 spacing 30:
                    frame xsize 500 style "empty":
                        text _("Right Trigger\nA/Bottom Button") style "help_label_text"
                    frame ypos 5 xsize 500 style "empty":
                        text _("Advances dialogue and activates the interface.") style "help_t" yalign 0.11

                hbox xalign 0.5 xsize 700 spacing 30:
                    frame xsize 500 style "empty":
                        text _("Left Trigger\nLeft Shoulder") style "help_label_text"
                    frame ypos 5 xsize 500 style "empty":
                        text _("Rolls back to earlier dialogue.") style "help_t" yalign 0.11

                hbox xalign 0.5 xsize 700 spacing 30:
                    frame xsize 500 style "empty":
                        text _("Right Shoulder") style "help_label_text"
                    frame ypos 5 xsize 500 style "empty":
                        text _("Rolls forward to later dialogue.") style "help_t" yalign 0.11

                hbox xalign 0.5 xsize 700 spacing 30:
                    frame xsize 500 style "empty":
                        text _("D-Pad, Sticks") style "help_label_text"
                    frame ypos 5 xsize 500 style "empty":
                        text _("Navigate the interface.") style "help_t" yalign 0.11

                hbox xalign 0.5 xsize 700 spacing 30:
                    frame xsize 500 style "empty":
                        text _("Start, Guide,\nB/Right Button") style "help_label_text"
                    frame ypos 5 xsize 500 style "empty":
                        text _("Accesses the game menu.") style "help_t" yalign 0.11

                hbox xalign 0.5 xsize 700 spacing 30:
                    frame xsize 500 style "empty":
                        text _("Y/Top Button") style "help_label_text"
                    frame ypos 5 xsize 500 style "empty":
                        text _("Hides the user interface.") style "help_t" yalign 0.11
    else:
        frame:
            style "empty"
            background Solid("#00000080")

            text "KEYBOARD" color "#ffffff" font "palanquin_bold" size 24 xpos 245 ypos 100

            hbox:
                ypos 150
                xpos 50
                spacing 30

                vbox:
                    text _("ENTER") style "help_label"
                    text _("SPACE") style "help_label"
                    text _("ARROW KEYS") style "help_label"
                    text _("ESCAPE") style "help_label"
                    text _("CTRL") style "help_label"
                    text _("TAB") style "help_label"
                    text _("PAGE UP") style "help_label"
                    text _("PAGE DOWN") style "help_label"
                    text "H" style "help_label"
                    text "S" style "help_label"
                    text "V" style "help_label"

                vbox:
                    ypos 7
                    spacing 15
                    text _("Advances dialogue and activates the interface.") style "help_t"
                    text _("Advances dialogue without selecting choices.") style "help_t"
                    text _("Navigate the interface.") style "help_t"
                    text _("Accesses the game menu.") style "help_t"
                    text _("Skips dialogue while held down.") style "help_t"
                    text _("Toggles dialogue skipping.") style "help_t"
                    text _("Rolls back to earlier dialogue.") style "help_t"
                    text _("Rolls forward to later dialogue.") style "help_t"
                    text _("Hides the user interface.") style "help_t"
                    text _("Takes a screenshot.") style "help_t"
                    text _("Toggles assistive {color=#00ff00}{a=https://www.renpy.org/l/voicing}self-voicing{/a}{/color}.") style "help_t"
        text "MOUSE" color "#ffffff" font "palanquin_bold" size 24 xpos 905 ypos 340
        hbox:
            xpos 700 ypos 415
            spacing 30
            vbox:
                text _("LEFT CLICK") style "help_label" ypos -8
                text _("MIDDLE CLICK") style "help_label"
                text _("RIGHT CLICK") style "help_label"
                text _("WHEEL UP") style "help_label"
                text _("WHEEL DOWN") style "help_label"
            vbox:
                ypos -20
                spacing 15
                text _("Advances dialogue and\nactivates the interface.") style "help_t"
                text _("Hides the user interface.") style "help_t"
                text _("Accesses the game menu.") style "help_t"
                text _("Rolls back to earlier dialogue.") style "help_t"
                text _("Rolls forward to later dialogue.") style "help_t"

    button style "return_arrow_button" action [Hide("help"),Return()] tooltip ""

screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0















screen confirm(message, yes_action, no_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/prompt/prompt_overlay.png"

    frame:
        xsize 560
        xalign 0.5
        yalign 0.5
        has vbox
        xalign .5
        yalign .5
        spacing 30
        if not message:
            label _("ARE YOU SURE?"):
                style "confirm_prompt"
                xalign 0.5
        else:
            label _(message):
                style "confirm_prompt"
                xalign 0.5
        vbox:
            spacing 5
            textbutton "YES" action yes_action style "main_menu_button"
            textbutton "NO" action no_action style "main_menu_button" default_focus check_controller()


    key ["K_ESCAPE", "mouseup_3", "pad_b_press"] action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame("gui/prompt/prompt_box.png", Borders(40, 40, 40, 40))
    padding (40, 40, 40, 40)


style confirm_prompt_text:
    textalign 0.5
    color "#ffffff"
    font "palanquin_bold"
    size 22
    layout "subtitle"

style confirm_image_button:
    xalign 0.5

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")









screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox
        spacing 6

        text _("Skipping")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:


    font "DejaVuSans.ttf"









screen notify(message, y=5):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        ypos y
        text message

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")









screen nvl(dialogue, items=None):
    if nvl_mode == "phone":
        use PhoneDialogue(dialogue, items)
    else:
        window:
            style "nvl_window"

            has vbox
            spacing gui.nvl_spacing


            if gui.nvl_height:

                vpgrid:
                    cols 1
                    yinitial 1.0

                    use nvl_dialogue(dialogue)

            else:

                use nvl_dialogue(dialogue)



            for i in items:

                textbutton i.caption:
                    action i.action
                    style "nvl_button"

        add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed
            yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id




define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")











screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}







style pref_vbox:
    variant "medium"
    xsize 450



screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Save") action ShowMenu("game_save")
            textbutton _("Auto") action Preference("auto-forward", "toggle")


style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 600

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 600


screen credits():
    tag menu
    add "gui/main/bg.png" blur 5
    add Solid("#00000080")
    add "gui/main/blue_ls_logo.png" xalign 0.5
    key ["K_ESCAPE", "mouseup_3", "pad_b_press"] action [Hide("credits"), Return()]

    frame:
        style "invisible_frame"
        minimum 700,400
        maximum 700,400
        align 0.5,0.8
        viewport id "credits":
            draggable True
            mousewheel True
            has vbox
            style_prefix "credits"
            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            if DLCS:
                label "Enabled DLCS"
                for k,v in DLCS.items():
                    if v == config.version:
                        text _(f"{k.capitalize()} ({v})")
                    else:
                        text _(f"⚠️ {k.capitalize()} ({v})"):
                            color "#ea6383"
                            bold True
                text ("\n")


            label "PROJECT LEADER"
            text "Andrealphus"

            label "CHARACTER ARTISTS"
            text "Dark-Oshigan, Senturi and HXL"

            label "BACKGROUND ARTISTS"
            text "Kjkjmulo, Dark-Oshigan, wrenCali, Mirko B, Jin and Dan"

            label "CHIBI ARTIST"
            text "Bea Draven"

            label "ANIMATORS"
            text "BoubreRig"
            text "Cain"

            label "NARRATIVE DIRECTOR"
            text "Nico"

            label "WRITERS"
            text "Nate Walis, Devious Dingbat, Waking Dreamland, Tik Tik,"
            text "Spirit Writer, Paris, Phoenix, Andrealphus,"
            text "Cherrywood"

            label "DEVELOPERS"
            text "Andrealphus, Lent1, Spirit Writer, BlissfulDarkness, Firesparq,"
            text "Paradoxal Deviant"

            label "VOICE ACTORS"
            text "MissMoonified as Bree & Kylie"
            text "LadyJem as Sasha"
            text "Mintea as Samantha"
            text "SilkyMilk as Aletta"
            text "SeekerZero as Audrey"
            text "AngstyExistence as Mike"
            text "LusterRose as Ryan"
            text "LadyELiseVA as Minami"
            text "MidnightDatura as Ayesha, Kiara & Cherie"
            text "KumBomb as Cassidy"
            text "Miradessa as Hanna"
            text "Squeaky as Lexi"
            text "Ko Clover as Kleio"
            text "DornVA as Angela"
            text "Shennychwan as Shiori"
            text "Mizz Peachy as Emma"
            text "Zaidan as Jack"
            text "VoiceLikeCandy as Anna"

            label "MUSIC"
            text "TeknoAXE"
            text "Darren Curtis"
            text "Roa Music"
            text "Johny Grimes"

            label "SPECIAL CONTRIBUTOR"
            text "Gouvernathor"
            text "Feniks"
            text "OmegaT"

            label "VERY IMPORTANT PATRONS"
            text "Mighty Heimskr, Jacob Brickner, alexlycan805, Kory Davis,"
            text "ZhiZhong Yan, Arruzaki, Ian Ponce, Dagon.san, kyle holland,"
            text "bradley, Reo44, itslydiabxtch, James Rabbit, Beau FastrÃ©,"
            text "Massma, Jonathan Santos-Rea, Pretzel Warrior,"
            text "Mutkamuikkunen, Manuel, Marcos Barrera, Mh1334, Mikax, qfa,"
            text "James Roberts, Eric Baughman, Liam Evans, yeah budy,"
            text "maylie alderete, DragonMan5, Hasten Bridges, Parkey,"
            text "AnimeIsMyWaifu, Rem Rem, Stéphane Pasquier, Ryan Samr,"
            text "themadsciencedivison, Obey Monster, JD, PoorMorale,"
            text "Jacob C Grooms, M, Justin Hefner, frank, Bart57070, Terry Dow,"
            text "Hendrik Baumbach, Andre Bernhardt, Coda_118, vakknight .,"
            text "Now this, Fynn Stephan, Moroyrii, Steward Sosn, Royce Wiens,"
            text "IronKing, ChronoMox, Uncle Yakko, Amaury Martinez,"
            text "Peter Pham, Jake Bilodeau, Lucifer Seraphim, Libertas90,"
            text "Zih Kidwell, Andrew Kennedy, Tesserakt, Jan DÃ¼rr, Laziy,"
            text "Lucas Myers, BOI1234, matt, paksin689, Skaer Krowe,"
            text "ElysianReign, Cosmic_SK, Chris, lee osterloh, Joe Kieler,"
            text "ThePostalGamer, Nir Zonenshtein, Rykia, Jonas Hueber,"
            text "dxxx, dosel, Lafenya Lou, Aeon, Archie themoon, Mike Johnson,"
            text "Axium, Thormakar, Tomcat2k, CouncilOfOne, Zach Johnson,"
            text "Alice Taylor, LordTouchMe, Devilman1987, Abdul, lucas lofgren,"
            text "Fenpai, A.K.A wut, WilliamS, Sir. BYM, Sly, HalfFang,"
            text "The Exorzists, yeetus, SomeoneWhoIsntMe, Tidus Reidan,"
            text "Joe Gillis, Jesse Moore, David Oneill, Aaron Bershell,"
            text "Nicolas Mai phung, Ouron, Armando Sapien, Jack Sparling,"
            text "Bron-vito, Mr.dragon, Astre, DMan4g00d, Losstinhere,"
            text "Blaze Foley, AzazelTheCursed, apoctriforce, mc 14028,"
            text "Auhiie, Alexa, Fabien L\'hermitte, Peaches652, Ultra Violet,"
            text "colison, BrotherDom, Kyle, Louka, slimsam9999, Tomb,"
            text "Wendigo The Lewd, Abi Usus, Nino Chief, Matthew Dennis,"
            text "RussianBee, Negative Wizard, death_the_kid123, MaxStorm,"
            text "zampa16, Bruce Burke, BiggusBonggus, Scar, Damian Derby,"
            text "Nate, Jacory Hammock, W1HOLESALE, June117, Woolfell,"
            text "Mr What, Akanan, Nexus, Juliann Lardeux, Bay McClendon,"
            text "David Aguiari, Soul, Smitty, Goeuriot, Merc#2077,"
            text "Max Kupriianov, brett, Joker, ramses301, Vito Scaletta,"
            text "jimmy401, Deadsummer, Anthony Schreiber, SelimTenebris,"
            text "Icy Raptor, Mateo Brewer, Lahteu, Kenov, Toobaa, Spiffle,"
            text "hell543, AJChaser, Human1134, BumChuzzler, Markus,"
            text "Kevin Kirk, José Luis Velasco, The Hoax Reality,"
            text "Dallas Runchel, huunam Lee, Kevin Tra, Nathaniel Thomas,"
            text "kathrynne, Christianweg, Toedkest, Mikey Boy, Blazedsteelwolf,"
            text "Troy Sewell, Rookie One, Nattie, Azrael morningstar,"
            text "Zhang Qian, Nick, Luke Richardson, Mirogan, Chrono Designs,"
            text "jmfindorff, Adam Sutor, Negativatron, Sage, Penn,"
            text "David Washington, Dready, King leoric, Lucas, jason rodger,"
            text "razor wolf, M\'Sauvea Reynolds, louie najera, Antoine Daudelin,"
            text "Four Leaf, Sovereign16, Wutthiwat Wiriyathanacharoenkit,"
            text "Christian, melodygreek, Justin Hood, NullVoided, Brian Embry,"
            text "Mufti300, Alex Bennett, Warqueen, SoftEis,"
            text "Jacob Pagan Thacker, LambChopSoldier, Benji, Eric Nivens,"
            text "Samael, Michael, laurynas, cestmir, Locke, Doc Pan As,"
            text "Nanaimo Kobayashi, Karn, Gerson Velasquez, david whoo,"
            text "Blackspack, Evan Laforet, Hunter ingram, Phillip Razlow,"
            text "ryan adkins, VIVIDave, Joshua Taylor, Vlad Sadilovskiy,"
            text "NemoMeow, KKGG DARKS, Darthzack566, Kenodoxia,"
            text "Frank Mecka, CheeseMasta, TheDevilYouKnow, Roknor, Rawk,"
            text "Alkatraz, Kyle Weber, Frank Mecka, Tobi, Manuel Fernandez,"
            text "Rameses Bucay, King of Acetonien, PR, Jeffrey Eaton,"
            text "fouassier, Ellis, Kugel2456, That Asshole Vlogger,"
            text "CharDucks, darkabyss987, Chad Dreaney, Benjamin Loke,"
            text "Zimmaster7, Herecomethepit, dblkrose, Lexi Mace,"
            text "Muramasa Manamune, Josh Wong, Nicholas Sheard,"
            text "Storyteller, Dirtyduck, Jonathan Brooks, Lucifer, Lejo98,"
            text "Shitty Cuz, Vigilant, Blitzreigkai97, Antonio Serrano,"
            text "Scotty Doesn\'t Know, Nightmare Spyro, jerald imo, cj33,"
            text "ViPo, Norberis, Long Shot, Unknown Player, Donald Kane,"
            text "Kogan Sheda, Jason Miller, Phazonmasher, Alric darkflame,"
            text "robert, Vincent, DarkAges85, Jett Smith, Jakaa9,"
            text "Arendall, Zula D. Varr, Russ, Dung O\'Dea, Dylan Ahling,"
            text "Junge Yu, markg20_7, natane, Truckerguy257, Doe,"
            text "IANQIN, Jannes Holtkamp, Barismati, greenarrow25,"
            text "John, dominik43572, Mackenzie, kainan, Markg207 l,"
            text "Bob Jones, Schumacher0318, Scomf13, Greg Bloomberg,"
            text "AndrÃ© Nilsen, Valnik, NightFury95, Ruben, Cal,"
            text "JORDAN HANSEN, Nubs, BlissfulDarkness, TheBeard,"
            text "Ryan Darkstar, Joe Joe, Florian Jacquet, karel-de-macil,"
            text "Drew Turner, Brandon Ferguson, Buttery Biscuit, Scottie,"
            text "joeger, Valken77, Rahl, ROBERT CARR, trainblub,"
            text "JantsoP, TheGhost, Kekesuro, Kristoffer Norgren, Purpleman,"
            text "dotdotdot, Aphelion, Dr.Pancakes, CSP, nebs"
            text "    "
            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].")
            text "\n[renpy.license!t]"

        vbar:
            value YScrollValue("credits")
            left_bar "gui/inv/vertical_idle_bar.png"
            right_bar "gui/inv/vertical_idle_bar.png"
            thumb "gui/inv/vertical_idle_thumb.png"
            thumb_offset 63
            left_gutter 63
            right_gutter 63
            maximum 11,340
            xpos 700
    button style "return_arrow_button" action [Hide("credits"),Return()] tooltip ""

style credits_label is label:
    color "#ffffff"
    font "palanquin_bold"
    size 24
    xalign 0.5
    yalign 0.5

style credits_text is text:
    color "#ffffff"
    font "exo2_regular"
    size 24
    xalign 0.5
    yalign 0.5


init python:
    changelog_lines = None
    changelog_path = os.path.join(config.basedir, 'changelog.txt')
    if os.path.exists(changelog_path):
        with open(changelog_path, "r") as f:
            ch_content = f.read()
        re_newline = r"\n\s+([\w ]+)$"
        changelog_lines = re.sub(re_newline, r" \1", ch_content, flags=re.M)
        changelog_lines = changelog_lines.split('\n')
screen changelog():
    tag menu
    add "gui/main/bg.png" blur 5
    add Solid("#00000080")
    label "CHANGELOG" align 0.5, 0.1 text_size 50
    key ["K_ESCAPE", "mouseup_3", "pad_b_press"] action [Hide("changelog"), Return()]

    viewport id "changelog":
        xsize 800 ysize 400
        align 0.5, 0.7
        scrollbars "vertical"
        vscrollbar_base_bar Frame("gui/inv/vertical_idle_bar_long.png")
        vscrollbar_thumb "gui/inv/vertical_idle_thumb.png"
        draggable True
        mousewheel True

        if changelog_lines:
            vbox:
                style_prefix "credits"
                spacing 2

                $ stop_version = "24.12.0a"
                for line in changelog_lines:


                    if not line:
                        null height 80


                    elif line.startswith("- "):
                        $ line = line[2:]
                        text line size 18 substitute False


                    elif line[0].isdigit():
                        if line[:-1] == stop_version:
                            break
                        text line[:-1] bold True italic True size 30


                    else:
                        null height 20
                        text line[:-1] bold True

    button style "return_arrow_button" action [Hide("changelog"),Return()] tooltip ""







style story_text is text:
    font "palanquin_medium"
    size 20
    yalign 0.5

style story_hbox is hbox:
    yalign 0.5

style story_frame is frame:
    background Frame(Transform("gui/frame_message.png", matrixcolor=OpacityMatrix(0.9) * BrightnessMatrix(0.0)), Borders(20, 20, 20, 20))

style story_vscrollbar is vscrollbar:
    left_bar "gui/inv/vertical_idle_bar_long.png"
    right_bar "gui/inv/vertical_idle_bar_long.png"
    thumb "gui/inv/vertical_idle_thumb.png"
    xanchor 1.0
    xalign 1.0
    xsize 36
    bar_invert True
    thumb_offset 5
    top_gutter 5
    bottom_gutter 25

style story_button is button:
    idle_background "gui/phone/empty_idle.png"
    hover_background "gui/phone/empty_hover.png"
    insensitive_background "gui/phone/empty_insensitive.png"
    selected_background "gui/phone/empty_selected.png"
    selected_idle_background "gui/phone/empty_selected_idle.png"
    selected_hover_background "gui/phone/empty_selected_hover.png"
    xminimum 275
    yalign 0.5

style story_button_text is story_text

style story_fixed is fixed:
    xsize 25
    ysize 25
    xalign 0.5
    yalign 0.5


style story_title_text is story_text:
    size 30
    hover_color "#006284"

style story_title_button is button:
    background None
    xalign 0.0
    yalign 0.5
    ysize 55

style story_title_button_text is story_title_text

style story_title_frame is frame:
    background Frame("gui/pname_box.png", Borders(5, 5, 5, 5))
    xpadding 20
    ypadding 0

style story_title_label_text is text:
    font "palanquin_bold"
    color "#006284"
    size 25
    ypos -3


style story_type_button is button:
    idle_background Frame("gui/button_idle.png", Borders(15, 15, 15, 15))
    selected_idle_background Frame("gui/button_hover.png", Borders(15, 15, 15, 15))
    hover_background Frame("gui/button_hover.png", Borders(15, 15, 15, 15))
    selected_hover_background Frame("gui/button_idle.png", Borders(15, 15, 15, 15))
    insensitive_background Frame("gui/button_insensitive.png", Borders(15, 15, 15, 15))
    xpadding 10
    ypadding 5

style story_type_button_text is story_text:
    yalign 0.75
    size 22

style story_type_button_text is story_text:
    variant "small"
    yalign 0.0
    size 22


style story_description_hbox is hbox

style story_description_text is text:
    font "exo2_regular"
    size 23

style story_description_button is button:
    background None
    yminimum 36
    ymaximum 55

style story_description_button_text is story_description_text


style story_description_icon_text is story_description_text:
    yalign 0.5
    xalign 0.5

style story_description_icon_fixed is fixed:
    xsize 100
    ysize 25
    xalign 0.5
    yalign 0.5


style story_select_text is story_description_text:
    hover_color "#006284"

style story_select_button is invisible_button
style story_select_button_text is story_select_text


style main_menu_button:
    background "gui/box_w_transparent.png"
    hover_background "gui/prompt/empty_hover.png"
    insensitive_background Transform("gui/box_w_transparent.png", matrixcolor=SaturationMatrix(0))
    xminimum 426
    xalign 0.5

style main_menu_button_text is text:
    font "palanquin_bold"
    color "#006488"
    hover_color "#ffffff"
    insensitive_color "#666666"
    size 20
    xalign 0.5
    yalign 0.5

define config.gestures = {
        "n" : "game_menu",
        "s" : "hide_windows",
        "e" : "toggle_skip",
        "w" : "rollback"
        }

screen button_screen():
    key ["K_ESCAPE", "mouseup_3", "pad_b_press"] action [FileTakeScreenshot(), ShowMenu("game_menu")]
    key "l" action ShowMenu("load")
    if renpy.get_screen(["room", "smartphone", "map", "housemap"]):
        key "p" action ToggleScreen("smartphone")
    if renpy.get_screen(["room", "story_tracker", "map", "housemap"]):
        key "q" action ToggleScreen("story_tracker")


init python:
    config.keymap['game_menu'] = []
    config.pad_bindings["pad_b_press"] = []

screen disclaimer():
    add "gui/main/bg.png" blur 5
    frame:
        style "empty"
        background Solid("#000000BF")
    add "gui/disclaimer_chibi.png" xalign 0.5 yalign 0.5
    style_prefix "disclaimer"
    vbox:
        xmaximum 960
        xalign 0.5
        yalign 0.5
        text "WARNING!" xalign 0.5
        text "" xalign 0.5
        vbox:
            hbox:
                text "1. "
                text "This game is intended for mature audiences only so if you are not legally adult in your residence country please press Alt+F4 and go play Fortnite."
            hbox:
                text "2. "
                text "Only grown ups now? Great!"
            hbox:
                text "3. "
                text "This game contains a lot of sexual themes and situations, also boobies. So if you don't like those please refer to number one."
            hbox:
                text "4. "
                text "This game is intended to be funny (hopefully it succeeds). All characters, names, locations are purely fictitious and any resemblance is purely coincidental."
            hbox:
                text "5. "
                text "All characters depicted in this game are over the age of 18, maybe more."
            hbox:
                text "6. "
                text "No bears or sharks of any kind were hurt during the making of this game."
        text "" xalign 0.5
        text "Thanks for understanding." xalign 0.5
        text "Have fun!" xalign 0.5
    text "Click to continue" align (0.1, 0.9)

style disclaimer_text is text:
    size 24
    outlines [(2, "#006284", 0, 0)]
    color "#fff"

init -25 python:
    from renpy.display.video import Movie as PlayMovie

screen promo():
    add PlayMovie(channel="movie_dp", play="gui/promo/MDR_trailer.webm", size=(1280, 720))
    hbox:
        ypos 600
        xpos 130
        imagebutton at promo_pulse:
            if build_platform in ['steam', 'itchio', 'patreon']:
                auto f"gui/promo/button_{build_platform}_%s.png"
                action OpenURL(platforms_games_links.get(build_platform).get('mydemonicromance'))
            else:
                auto "gui/promo/button_patreon_%s.png"
                action OpenURL("https://www.patreon.com/mydemonicromance")

transform promo_pulse:
    xanchor 0.5
    yanchor 0.5
    parallel:
        ease 0.07 zoom 1.01
        ease 0.07 zoom 1.02
        ease 0.07 zoom 1.03
        ease 0.105 zoom 1.02
        ease 0.105 zoom 1.01
        ease 0.105 zoom 1
        ease 0.105 zoom 0.99
        ease 0.105 zoom 0.98
        ease 0.07 zoom 0.97
        ease 0.07 zoom 0.98
        ease 0.07 zoom 0.99
        ease 0.07 zoom 1
        repeat


define map_location_positions = {
        "alley": (135, 380),
        "amusement": (1200, 630),
        "amyhome": (930, 220),
        "aquarium": (740, 325),
        "audreylivingroom": (185, 190),
        "beach": (1010, 95),
        "cemetery": (200, 125),
        "church": (280, 170),
        "cinema": (810, 670),
        "forest": (285, 100),
        "garage": (380, 415),
        "golf": (1125, 110),
        "gymreception": (780, 480),
        "hospital": (980, 420),
        "kart": (480, 465),
        "kathome": (150, 460),
        "housemap": (1190, 280),
        "maidcafe": (980, 635),
        "mallmap": (880, 565),
        "mansion": (110, 160),
        "map": (-50, -50),
        "restaurant": (550, 400),
        "rooftop": (400, 175),
        "nightclub": (600, 460),
        "office": (875, 295),
        "pallalivingroom": (1120, 330),
        "park": (1050, 480),
        "photostudio": (300, 330),
        "policestation": (740, 550),
        "pub": (680, 635),
        "sexshop": (220, 330),
        "shootingrange": (415, 350),
        "street": (985, 300),
        "stripclub": (175, 270),
        "studio": (300, 680),
        "trailer": (950, 105),
        "university": (150, 605),
        "victorsafehouse": (75, 150),
        "waterpark": (1125, 670),
        "zoo": (1240, 540),
    }

screen map(locations):
    if not (renpy.get_screen("smartphone") or renpy.get_screen("story_tracker")):
        default destination = ""
        add "bg map"
        for location in locations:

            if location.id == "mall1":
                $ location = Room.find("mallmap")
            if location.id == "gym":
                $ location = Room.find("gymreception")
            $ x, y = map_location_positions[location.id]
            $ npcs = location.get_present_npcs_ids_by_tag()[:6]
            $ self_voicing_location = f"{location.display_name}; {'; '.join(npcs)}"
            imagebutton auto "gui/map/button_map_%s.png" xpos x ypos y xanchor 0.5 yanchor 0.5 alt self_voicing_location:
                action [Function(location.travel_to), SetVariable("game.room", location.id), Return()]
                hovered SetScreenVariable("destination", location)
                unhovered SetScreenVariable("destination", "")
            for n_index, npc in enumerate(npcs):
                $ x_g = x
                $ y_g = y
                if n_index == 1:
                    $ y_g += 35
                elif n_index:
                    if n_index in [2, 4]:
                        $ x_g += 29
                    else:
                        $ x_g = x - 29
                    if n_index in [2, 3]:
                        $ y_g += 19
                    else:
                        $ y_g = y - 19
                fixed:
                    xpos x_g
                    ypos y_g
                    xsize 25
                    ysize 25
                    xanchor 0.5
                    yanchor 0.5
                    add "gui/icons/icon_bg_small.png"
                    add f"notify {npc}"
            if location.id == "housemap":
                $ location_name = "Home"
            elif location.id == "mallmap":
                $ location_name = "Mall"
            elif location.id == "street":
                $ location_name = "Street"
            elif location.id == "nightclub":
                $ location_name = "Club"
            elif location.id == "gymreception":
                $ location_name = "Gym"
            elif location.id == "waterpark":
                $ location_name = "Waterpark"
            else:
                $ location_name = location.display_name
            text "{b}" + location_name.replace(" ", "\n") xpos x ypos y-22 xanchor 0.5 yanchor 1.0 outlines [ (2, "#06698c") ] color "#5fb2d8" size 15 text_align 0.5 alt ""

        if persistent.new_ui:
            use actions([(a, a.icon, a.display_name) for a in Activity.valid_activities()])
            use tooltip
        use ui_destination_helper(destination, location)


define housemap_location_positions = [
        {
            "kitchen": (590, 210),
            "livingroom": (580, 405),
            "pool": (345, 320),
            "bedroom1": (545, 575),
            "bedroom6": (545, 575),
            "house": (910, 360),
            "firstfloorbathroom": (760, 490),
        },
        {
            "pool": (345, 320),
            "house": (910, 360),
            "attic": (770, 160),
            "secondfloor": (630, 300),
            "bedroom2": (730, 270),
            "bedroom3": (550, 190),
            "bedroom4": (730, 270),
            "bedroom5": (770, 160),
            "bathroom": (710, 460),
            "houselibrary": (545, 465),
        }
    ]

define house_floor = 0

screen housemap(locations):
    if not (renpy.get_screen("smartphone") or renpy.get_screen("story_tracker")):
        default destination = ""
        if house_floor != 0:
            add "bg housemap first"
            imagebutton auto "gui/down_%s.png" action SetVariable("house_floor",0) xpos 250 ypos 530 xanchor 0.5 yanchor 0.5 alt "go to home first floor"
            text "{b}" + "First\nFloor" outlines [ (3, "#06698c") ] color "#5fb2d8" xpos 250 ypos 610 xanchor 0.5 yanchor 0.5 alt ""
        else:
            imagebutton auto "gui/up_%s.png" action SetVariable("house_floor",1) xpos 250 ypos 530 xanchor 0.5 yanchor 0.5 alt "go to home second floor"
            text "{b}" + "Second\nFloor" outlines [ (3, "#06698c") ] color "#5fb2d8" xpos 250 ypos 610 xanchor 0.5 yanchor 0.5 alt ""
        imagebutton auto "gui/map/city_%s.png" action SetVariable("game.room", "map"), Return() xpos 1000 ypos 530 xanchor 0.5 yanchor 0.5 alt "go to city"
        text "{b}" + "City" outlines [ (3, "#06698c") ] color "#5fb2d8" xpos 1000 ypos 610 xanchor 0.5 yanchor 0.5 alt ""
        for location in [l for l in locations if l.id in housemap_location_positions[house_floor]]:
            $ x, y = housemap_location_positions[house_floor][location.id]
            $ npcs = location.get_present_npcs_ids()[:6]
            $ self_voicing_location = f"{location.display_name}; {'; '.join(npcs)}"
            imagebutton auto "gui/map/button_map_%s.png" xpos x ypos y xanchor 0.5 yanchor 0.5 alt self_voicing_location:
                action SetVariable("game.room",location.id), Return()
                hovered SetScreenVariable("destination", location)
                unhovered SetScreenVariable("destination", "")
            for n_index, npc in enumerate(npcs):
                $ x_g = x
                $ y_g = y
                if n_index == 1:
                    $ y_g += 35
                elif n_index:
                    if n_index in [2, 4]:
                        $ x_g += 29
                    else:
                        $ x_g = x - 29
                    if n_index in [2, 3]:
                        $ y_g += 19
                    else:
                        $ y_g = y - 19
                fixed:
                    xpos x_g
                    ypos y_g
                    xsize 25
                    ysize 25
                    xanchor 0.5
                    yanchor 0.5
                    add "gui/icons/icon_bg_small.png"
                    add f"notify {npc}"
            $ location_name = location.display_name
            text "{b}" + location_name.replace(" ", "\n") xpos x ypos y-22 xanchor 0.5 yanchor 1.0 outlines [ (2, "#06698c") ] color "#5fb2d8" size 15 text_align 0.5 alt ""
        if persistent.new_ui:
            use actions([(a, a.icon, a.display_name) for a in Activity.valid_activities()])
            use tooltip
        else:
            use ui_destination_helper(destination, location)

screen ui_destination_helper(destination, location):
    if destination:
        if destination.id == "map":
            $ destination_name = "City"
        elif destination.id == "housemap":
            $ destination_name = "Home"
        elif destination.id == "mallmap":
            $ destination_name = "Mall"
        elif destination.id == "street":
            $ destination_name = "Street"
        elif destination.id == "nightclub":
            $ destination_name = "Club"
        elif destination.id == "gymreception":
            $ destination_name = "Gym"
        elif destination.id == "waterpark":
            $ destination_name = "Waterpark"
        else:
            $ destination_name = destination.display_name
        vbox:
            if renpy.get_screen("housemap") or (renpy.get_screen("map") and persistent.new_ui):
                align (0.5, 0.1)
            else:
                align (0.5, 0.2)
            spacing 20
            text "{b}" + destination_name outlines [ (3, "#06698c") ] color "#5fb2d8" size 40 xalign 0.5 alt ""
            hbox:
                xalign 0.5
                box_justify True
                spacing 5
                if renpy.get_screen("housemap"):
                    $ present_people = destination.get_present_npcs_ids()
                else:
                    $ present_people = destination.get_present_npcs_ids_by_tag()

                for p in present_people:
                    add Composite(
                        (50, 50),
                        (0, 0), Transform("gui/phone/ico_phone_idle.png", zoom=0.8),
                        (7, 7), f"gui/action_icons/button_{p}.png"
                        ):
                        at Position(anchor=(0.5, 0.5))
screen too_old_save():
    style_prefix "lspref"
    zorder 50
    frame:
        background "gui/main/bg.png"
        add "ch/bree/st/bree_smartphone.webp" xalign 0.25 yalign 0.25
        add "ch/mike/st/mike_smartphone.webp" xalign 0.75 yalign 0.25
        vbox:
            xmaximum 960
            xalign 0.5
            yalign 0.7
            text "ERROR!" size 24 outlines [(2, "#FF0000")] color "#ffffff" xalign 0.5
            text "" size 24 outlines [(2, "#FF0000")] color "#ffffff" xalign 0.5
            text "Unfortunately, your save is not compatible with this game version." size 24 outlines [(1, "#FF0000")] color "#ffffff"
            text "Playing with this save will lead to errors." size 24 outlines [(1, "#FF0000")] color "#ffffff"
            text "" size 24 outlines [(2, "#FF0000")] color "#ffffff" xalign 0.5
            vbox:
                xalign 0.5
                textbutton "Go back" action Show("load") style "main_menu_button"
                textbutton "I understand" action Return(True) style "main_menu_button"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
