init 2:
    $ persistent.sio_sid = None
    if not persistent.authentication_token:
        $ persistent.authentication_token = False
    if not persistent.portal_environment:
        $ persistent.portal_environment = "prod"
    if not persistent.portal_location:
        $ persistent.portal_location = "eu"


label download_demo:
    if not persistent.portal_location:
        $ persistent.portal_location = "eu"
    $ update_url = f"{portal_url}/updates/prod/releases/loveandsexsecondbase/demo/itchio/updates.json"
    $ package = "gameonly_itchio"
    show expression "gui/main/mainmenu_bg.png"
    call downloader (headers={"User-Agent": f"{config.name}/{config.version}"}) from _call_downloader
    return

label download_from_provider:
    show expression "gui/main/mainmenu_bg.png"
    $ timeout = 0
    show screen authentication
    python:
        try:
            websocket.start()
        except:
            renpy.call_screen("authentication", message="ERROR: Unable to connect. Switch to manual authentication", restart=True)
    $ timeout = 0
    while not persistent.sio_sid:
        hide screen authentication
        show screen authentication(timeout, message="Waiting for sio sid.")
        $ renpy.pause(5, hard=True)
        $ timeout += 5

    if persistent.sio_sid:
        $ token_url = f"{portal_url}/token?dl_sid={persistent.sio_sid}"
    else:
        $ token_url = f"{portal_url}/token"
    hide screen authentication
    show screen authentication(message="OpenURL on {token_url} {store.persistent.sio_sid}")
    $ renpy.run(OpenURL(token_url))

    $ timeout = 0
    while not persistent.authentication_token:
        hide screen authentication
        show screen authentication(timeout, message="Waiting for authentication.")
        $ renpy.pause(3, hard=True)
        $ timeout += 5

    $ timeout = 0
    while not (persistent.authentication_provider and persistent.portal_environment):
        hide screen authentication
        show screen authentication(timeout, message="Request more data")
        $ renpy.pause(3, hard=True)
        $ timeout += 5
    $ websocket.stop()
    hide screen authentication
    show screen authentication(message=f"")

    if "week" in config.version:
        $ release = "weekly"
    else:
        $ release = "releases"

    $ package = f"gameonly_{persistent.authentication_provider}"

    if persistent.portal_location == 'local':
        $ update_url = f"http://127.0.0.1:5000/updates/{persistent.portal_environment}/{release}/loveandsexsecondbase/full/{persistent.authentication_provider}/updates.json"
        $ authentication_status = renpy.fetch(f"http://127.0.0.1:5000/token_check/{persistent.authentication_token}?to_json=True", timeout=15, result="json")
    else:
        $ update_url = f"{portal_url}/updates/{persistent.portal_environment}/{release}/loveandsexsecondbase/full/{persistent.authentication_provider}/updates.json"
        $ authentication_status = renpy.fetch(f"{portal_url}/token_check/{persistent.authentication_token}?to_json=True", timeout=15, result="json")

    hide screen authentication

    call screen token_status(authentication_status) nopredict
    hide screen token_status
    return

label downloader(headers={}):
    show expression "gui/main/mainmenu_bg.png"
    $ downloader = updater.start_game_download(update_url, headers=headers, add=[package])

    None "Welcome to the downloader game."

    None "This will download the main game onto your phone, so you can play it."

    if downloader.download_total:
        $ download_mb = int(round(downloader.download_total / 1024 / 1024, 0))

        None "To play this game, you'll need to download [download_mb] megabytes of data. If you're not on WiFi, you could be charged for it. Tap the screen to proceed."
    else:
        $ download_mb = None
        None "To play this game, you'll need to download some data. If you're not on WiFi, you could be charged for it. Tap the screen to proceed."
    scene bg black
    show expression "gui/main/mainmenu_bg.png"
    $ updater.continue_game_download()
    return


label updater_warning(headers={}):
    call screen game_update(headers) nopredict
    return


label manual_authentication:
    $ renpy.run(OpenURL(f"{portal_url}/token?manual=True"))
    if not persistent.authentication_token:
        $ persistent.authentication_token = ""
    $ _skipping = False
    call screen manual_authentication
    if persistent.authentication_token != _return:
        $ persistent.authentication_token = _return
    hide screen manual_authentication
    $ _skipping = True

    show screen authentication(message=f"Found authentication_token: {persistent.authentication_token}")
    pause
    hide screen authentication
    python:
        try:
            authentication_status = renpy.fetch(f"{portal_url}/token_check/{persistent.authentication_token}?to_json=True", timeout=15, result="json")
        except:
            renpy.call_screen("authentication", message="ERROR: Unable to check token validity\nRestart.", restart=True)
    call screen token_status(authentication_status)
    pause
    hide screen token_status

    $ persistent.authentication_provider = authentication_status.get("provider")
    $ persistent.portal_environment = authentication_status.get("portal_environment")
    $ persistent.portal_location = authentication_status.get("portal_location")

    if "week" in config.version:
        $ release = "weekly"
    else:
        $ release = "releases"
    $ update_url = f"{portal_url}/updates/{persistent.portal_environment}/{release}/loveandsexsecondbase/full/{persistent.authentication_provider}/updates.json"
    $ package = f"gameonly_{persistent.authentication_provider}"
    call updater_warning (headers={"User-Agent": f"{config.name}/{config.version}", "portal-token": persistent.authentication_token}) from _call_updater_warning
    return


label clear_persistent(restart=False):
    $ persistent.authentication_token = False
    $ persistent.authentication_provider = None
    $ persistent.portal_location = None
    $ persistent.portal_environment = None
    $ persistent.sio_sid = None
    $ websocket.stop()
    if restart:
        $ renpy.full_restart()

label clear_local_files():
    if os.path.isdir(os.path.join(renpy.config.basedir, "base")):
        $ shutil.rmtree(os.path.join(renpy.config.basedir, "base"))
    return

label reset_app_state():
    scene bg black
    show expression "gui/main/mainmenu_bg.png"
    None "You are going to reset application to a clean state."
    None "Your saves won't be affected."
    None "Use this only if the application is in an incoherent state."
    if main_menu:
        call screen confirm("Reset application?", [Call("clear_persistent"), Call("clear_local_files")], Return())
    else:
        call screen confirm("Reset application?", [Call("clear_persistent"), Call("clear_local_files")], ShowMenu("main_menu"))
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
