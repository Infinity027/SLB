init -999:
    screen updater(u):
        style_prefix "downloader"
        add "updater_module/updater_gui/main_menu.png"
        use debug_data(u=u)
        use overlay_buttons(u)

        frame:

            has vbox

            if u.state == u.ERROR:
                text _("An error has occurred:")
            elif u.state == u.ERROR:
                text _("An HTTP error has occurred:")
            elif u.state == u.CHECKING:
                text _("Checking for updates.")
            elif u.state == u.UPDATE_NOT_AVAILABLE:
                text _("This program is up to date.")
            elif u.state == u.UPDATE_AVAILABLE:
                text _("[u.version] is available. Do you want to install it?")
            elif u.state == u.PREPARING:
                text _("Preparing to download the updates.")
            elif u.state == u.DOWNLOADING:
                text _("Downloading the updates.")
            elif u.state == u.UNPACKING:
                text _("Unpacking the updates.")
            elif u.state == u.FINISHING:
                text _("Finishing up.")
            elif u.state == u.DONE:
                text _("The updates have been installed. The program will restart.")
            elif u.state == u.DONE_NO_RESTART:
                text _("The updates have been installed.")
            elif u.state == u.CANCELLED:
                text _("The updates were cancelled.")

            if u.message is not None:
                null height gui._scale(10)
                text "[u.message!q]"

            if u.progress is not None:
                if u.download_total:
                    text "[u.download_done_mb]/[u.download_total_mb] MB"
                else:
                    $ prog = int(u.progress * 100)
                    text "[prog]/100"

                if u.state not in [u.ERROR, u.HTTPERROR]:
                    bar value (u.progress or 0.0) range 1.0 style "_bar"

            hbox:
                xsize 0.95
                spacing 10
                if u.state in [u.ERROR, u.HTTPERROR] and u.can_proceed:
                    textbutton _("Main Menu") action [Call("clear_persistent", restart=True)]

                if u.state not in [u.ERROR, u.HTTPERROR] and u.can_proceed:
                    textbutton _("Proceed") action u.proceed

                if u.state not in [u.ERROR, u.HTTPERROR] and u.can_cancel:
                    textbutton _("Cancel") action [Call("clear_persistent"), u.cancel]

                if u.state not in [u.ERROR, u.HTTPERROR]:
                    textbutton _("Main Menu") action MainMenu(confirm=False)


    screen downloader(u):
        style_prefix "downloader"
        use debug_data(u=u)
        use overlay_buttons(u)

        frame:

            has vbox

            if u.state == u.CHECKING:
                text _("Checking for updates.")
            elif u.state == u.PREPARING:
                text _("Preparing to download the game data.")
            elif u.state == u.DOWNLOADING:
                text _("Downloading the game data.")
            elif u.state == u.UNPACKING:
                text _("Unpacking the game data.")
            elif u.state == u.FINISHING or u.state == u.DONE:
                text _(f"Game data is downloaded.\nIt will take some time to compile new files.\nThe game will/should restart by itself once done.")
            else:
                text _("An error occurred when trying to download game data:")

            if u.message is not None:
                null height gui._scale(10)
                text "[u.message!q]"

            if u.progress is not None:
                if u.download_total:
                    text "[u.download_done_mb]/[u.download_total_mb] MB"
                else:
                    $ prog = int(u.progress * 100)
                    text "[prog]/100"
            if u.state not in [u.ERROR, u.HTTPERROR]:
                bar value (u.progress or 0.0) range 1.0

            hbox:
                xsize 0.95
                spacing 10
                if u.state in [u.ERROR, u.HTTPERROR]:
                    textbutton _("Main Menu") action [Call("clear_persistent", restart=True)]

                if u.state not in [u.ERROR, u.HTTPERROR] and u.can_proceed:
                    textbutton _("Proceed") action u.proceed

                if u.state not in [u.ERROR, u.HTTPERROR] and u.can_cancel:
                    textbutton _("Cancel") action [Call("clear_persistent"), u.cancel]

                if u.state not in [u.ERROR, u.HTTPERROR]:
                    textbutton _("Main Menu") action MainMenu(confirm=False)


    style downloader_frame is default:
        background Frame("updater_module/updater_gui/textbox.png")
        xalign 0.5
        xsize 0.8
        ysize 0.3
        xpadding gui._scale(20)

        ypos .55
        ypadding gui._scale(20)

    style downloader_vbox is default:
        xfill True
        spacing gui._scale(10)

    style downloader_hbox is default:
        xalign 0.5
        yalign 1.0

    style downloader_text is default:
        xalign 0.5
        text_align 0.5
        layout "subtitle"

    style downloader_label is default:
        xalign 0.5

    style downloader_button is default:
        background Frame(["updater_module/updater_gui/button/[prefix_]background.png"], 4, 4, 4, 4)
        padding (4, 4, 4, 4)
        ysize 36
        xminimum 200

    style downloader_button_text is default:
        font "updater_module/updater_gui/fonts/Palanquin_Dark/PalanquinDark-Bold.ttf"
        hover_color "#ffffff"
        idle_color "#00668a"
        insensitive_color "#ffffff"
        selected_color "#7d7d7d"
        textalign 0.0
        size 20
        xalign 0.5
        yalign 0.5

screen debug_data(u=None):
    frame:
        style_prefix "notify"
        has vbox
        text _("authentication_provider: [persistent.authentication_provider]")
        text _("authentication_token: [persistent.authentication_token]")
        text _("portal_environment: [persistent.portal_environment]")
        text _("sio_sid: [persistent.sio_sid]")
        if u and u.debug_message:
            text _("[u.debug_message!q]")

screen overlay_buttons(u=None):
    style_prefix "downloader"
    frame:
        background None
        xsize 0.20
        xalign 1.0
        ysize 1.0
        yfill True
        ypos 0.0
        vbox:
            xalign 1.0
            yalign 0.0
            if os.path.isdir(os.path.join(renpy.config.basedir, "base")):
                if main_menu:
                    textbutton _("Reset application"):
                        xminimum 230
                        action Start("reset_app_state")
                else:
                    textbutton _("Reset application"):
                        xminimum 230
                        action Call("reset_app_state")
        vbox:
            xalign 1.0
            yalign 1.0
            if u:
                textbutton _("Abort"):
                    xminimum 230
                    action [u.cancel, Call("clear_persistent", restart=True)]
            else:
                textbutton _("Abort"):
                    xminimum 230
                    action [Call("clear_persistent", restart=True)]
            text "[config.version]":
                xalign 0.75



screen authentication(timeout=0, message=None, restart=False, manual=False):
    style_prefix "downloader"
    add "updater_module/updater_gui/main_menu.png"
    use debug_data()
    use overlay_buttons()
    frame:
        has vbox
        yfill True
        if message is not None:
            text "[message!q]"
        if restart:
            textbutton _("Restart"):
                action Function(renpy.full_restart)
                xalign 0.5
                yalign 0.95
        if timeout >= 15 or manual:
            if timeout >= 15:
                text "If your reach a timeout, try manual authentication"
            else:
                text "Use manual authentication"
            textbutton _("Manual authentication"):
                action [Hide(), Jump("manual_authentication")]
                xminimum 230
                xalign 0.5
                yalign 0.95

screen manual_authentication():
    if not persistent.authentication_token:
        $ persistent.authentication_token = ""
    if not persistent.portal_environment:
        $ persistent.portal_environment = "prod"
    if not persistent.portal_location:
        $ persistent.portal_location = "eu"

    default manual_entry = ""
    style_prefix "downloader"
    add "updater_module/updater_gui/main_menu.png"
    use debug_data()
    use overlay_buttons()
    frame:
        has vbox
        yfill True
        xfill True
        text "Paste the authentication token here"
        button:
            xalign 0.5
            ysize 0.35
            xsize 0.25
            background Frame("updater_module/updater_gui/namebox.png", Borders(20, 5, 20, 5))
            input:
                yalign 0.5
                value VariableInputValue("persistent.authentication_token")
                allow "0123456789abcdefABCDEF"
                length 8
                color "#00688c"
                copypaste True

        textbutton _("Done"):
            yalign 0.97
            action Return(persistent.authentication_token)
            keysym ('K_RETURN', 'K_KP_ENTER')

screen token_status(authentication_status):
    style_prefix "downloader"
    add "updater_module/updater_gui/main_menu.png"
    use debug_data()

    frame:
        frame:
            style "token_status_title"
            xalign 0.5
            label _("Authorization summary"):
                text_color "#00688c"
        hbox:
            style_prefix "token_status"
            yfill True
            xalign 0.0
            spacing 15

            grid 2 5:
                spacing 5
                text _("authentication_token:")
                text _("[authentication_status.get('authorization_token')]")
                text _("valid_token:")
                text _("[authentication_status.get('valid')]")
                text _("provider:")
                text _("[authentication_status.get('provider')]")
                text _("portal_environment:")
                text _("[authentication_status.get('portal_environment')]")

            if authentication_status.get('game_access'):
                $ rows = len(authentication_status.get("game_access"))
                grid 2 rows:
                    spacing 5
                    for game_id, game_authorization in authentication_status.get('game_access').items():
                        if '_downloader' not in game_id:
                            text _("[game_id]:")
                            text _("{color=#00ff00}{font=DejaVuSans.ttf}\u2713{/font}{/color}" if game_authorization else "{color=#f00}{font=DejaVuSans.ttf}\u2717{/font}{/color}")
            else:
                vbox:
                    yfill True
                    if not authentication_status.get('valid'):
                        text _("{color=#f00}Invalid token [persistent.authentication_token]{/color}"):
                            yalign 0.5
                    else:
                        text _("{color=#f00}Unable to get games ownership from [authentication_status.get('provider')]{/color}"):
                            yalign 0.5

    if authentication_status.get('valid'):
        textbutton _("Continue"):
            action [Call("updater_warning", headers={"User-Agent": f"{config.name}/{config.version}", "portal-token": persistent.authentication_token})]
            yalign 0.97
    else:
        textbutton _("Cancel"):
            action [Call("clear_persistent", restart=True)]
            yalign 0.97


screen game_update(headers={}):
    style_prefix "downloader"
    frame:
        has vbox
        xalign 0.5
        yalign 0.5
        text "This will update the game."
        text "To play this game, you'll need to download some data. If you're not on WiFi, you could be charged for it."
        textbutton "Update" action [SetField(persistent, "has_update", None), SetField(persistent, "last_update_check", None), updater.Update(update_url, allow_empty=True, confirm=False, headers=headers) ]


style token_status_text is downloader_text:
    xalign 0.0

style token_status_title is default:
    xsize gui.namebox_width
    ypos -60
    ysize gui.namebox_height
    background Frame("updater_module/updater_gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style notify_frame:
    background Frame("updater_module/updater_gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)

style notify_text is default:
    font "updater_module/updater_gui/fonts/Palanquin_Dark/PalanquinDark-Bold.ttf"
    size 16
    color "#ffffff"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
