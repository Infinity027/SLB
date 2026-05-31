screen main_menu_generic():
    tag menu
    add "gui/main/mainmenu_bg.png"
    if not is_sub_screen():
        frame style "empty":
            style_prefix "main_menu"
            xalign 0.5
            yalign 0.97

            has vbox
            if persistent.start_plus:
                textbutton "+START+" action Start("start_plus") default_focus (2 if check_controller() else 0)
            textbutton "START" action Start() default_focus check_controller()
            textbutton "LOAD" action ShowMenu("load")
            null height 20
            textbutton "OPTION" action ShowMenu("preferences")
            textbutton "GALLERY" action [SensitiveIf(persistent.start_plus), If(GALLERY_WARNING, ShowMenu("main_gallery"), ShowMenu("warning_gallery"))]
            textbutton "CONTROLS" action ShowMenu("help")
            textbutton "ABOUT" action ShowMenu("credits")
            null height 20
            textbutton "QUIT" action Quit()

        imagebutton auto "gui/patreon_button_%s.png" action OpenURL("https://www.patreon.com/Andrealphus") xalign 0.02 yalign 0.05 alt "Patreon"
        textbutton "Report Bug" action OpenURL("https://discord.com/channels/392691429840781315/481382104802918400") style "bug_button" xalign 0.02 yalign 0.98
        vbox:
            style_prefix "information_panel"
            xalign 1.0
            yalign 0.98
            spacing 2
            if not all([dlc_version == config.version for dlc_version in DLCS.values()]):
                textbutton "⚠️ Mismatch DLC version":
                    text_idle_color "#ea6383"
                    action ShowMenu("credits")
            $ new_version = updater.UpdateVersion(update_url, allow_empty=True)
            if new_version and new_version > config.version:
                if renpy.windows:

                    textbutton "Update to latest version":
                        text_idle_color "#eaca63"
                        action OpenURL("https://portal.andrealphusgames.com")
                else:
                    if not demo:
                        textbutton "Update to latest version":
                            text_idle_color "#eaca63"
                            action ShowMenu("download_from_provider")
                    else:
                        textbutton "Update to latest version":
                            text_idle_color "#eaca63"
                            action ShowMenu("update_demo")

            if gui.show_name:
                $ te = "[config.version]" + ("-demo" if demo else "-weekly" if weekly else "")
                hbox:
                    align (0.8, 0.97)
                    spacing 5
                    text te:
                        align (0.5, 0.5)
                        size 18
                        font "exo2_light"
                        color "#ffffff"
                        alt f'Love and Sex: Second Base main menu. version: {te}.'
                    textbutton "📄" action ShowMenu("changelog") align (0.5, 0.5) style "bug_button"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
