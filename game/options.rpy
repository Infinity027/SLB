
define config.name = _(f"Love & Sex : Second Base - {config.version}")
define build.game_only_update = False
define build.include_update = True
define gui.show_name = True
define config.version = "26.4.0c"
# --- Development mode: enables console (Shift+O), dev menu (Shift+D), reload
# (Shift+R) and full tracebacks. Set back to "auto" (or remove) for distribution.
define config.developer = True
define gui.about = _p("""""")
define build.name = "LoSeSb"
define config.gl2 = True
define config.has_sound = True
define config.has_music = True
define config.has_voice = True
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.after_load_callbacks = [after_load_callback]
define config.end_game_transition = None
define config.end_splash_transition = Dissolve(2.0)
define config.window = "auto"
define config.window_show_transition = None
define config.window_hide_transition = None
default preferences.show_empty_window = False
default preferences.text_cps = 0
default preferences.afm_time = 15
define config.save_directory = "LoSe_20_1-1512630773"
define build.itch_project = "andrealphus/love-sex-second-base"
define config.window_icon = "gui/window_icon.png"
define config.overlay_screens = ["quick_menu", "overlay_notification", "continue_feedback"]
define portal_url = "https://portal.andrealphusgames.com"
define update_url = f"{portal_url}/updates/prod/releases/loveandsexsecondbase/full/patreon/updates.json"
define config.has_sync = False
init -20 python:
    build_type = "full"
    build_platform = "patreon"
    steam = "steam" in build_platform.lower()
    demo = "demo" in build_type.lower()
    weekly = "weekly" in build_type.lower()
init python:
    re_ch = re.compile(r'ch\/([\w-]+)\/(?:.+)\.webp')
    ch_names = {re_ch.match(f).group(1) for f in files if re_ch.match(f)}
    # --- Development: keep assets as loose files instead of packing them into
    # .rpa archives. Set create_archives = True (or remove the guard) when
    # building for distribution. (ch_names above is still needed by the
    # build.classify loop further down, so it stays outside this guard.)
    create_archives = False
    if create_archives:
        for ch_name in ch_names:
            build.archive(ch_name, "all")
        build.archive("scripts", "all")
        build.archive("audio", "all")
        build.archive("interface", "all")
        build.archive("vi", "all")
        build.archive("bg", "all")
        build.archive("updater_module", "all")
        build.archive("dlc_breemc", "breemc dlcs itchio patreon")
        build.archive("dlc_fafow", "fafow dlcs patreon")
        build.archive("dlc_fafwm", "fafwm dlcs patreon")
        build.archive("dlc_lively", "lively dlcs patreon")
    if demo:
        config.name = _("Love & Sex : Second Base - Demo")
        build.name = "LoSeSb-Demo"
        build.classify('game/ch/aletta/**', None)
        build.classify('game/ch/alexis/**', None)
        build.classify('game/ch/amy/**', None)
        build.classify('game/ch/angela/**', None)
        build.classify('game/ch/anna/**', None)
        build.classify('game/ch/audrey/**', None)
        build.classify('game/ch/ayesha/**', None)
        build.classify('game/ch/camila/**', None)
        build.classify('game/ch/cassidy/**', None)
        build.classify('game/ch/cherie/**', None)
        build.classify('game/ch/gen_full/**', None)
        build.classify('game/ch/hanna/**', None)
        build.classify('game/ch/harems_full/**', None)
        build.classify('game/ch/harmony/**', None)
        build.classify('game/ch/kiara/**', None)
        build.classify('game/ch/kleio/**', None)
        build.classify('game/ch/kylie/**', None)
        build.classify('game/ch/lavish/**', None)
        build.classify('game/ch/lexi/**', None)
        build.classify('game/ch/morgan/**', None)
        build.classify('game/ch/palla/**', None)
        build.classify('game/ch/shiori/**', None)
        build.classify('game/ch/victor/**', None)
        build.classify('game/dlc_breemc/**', None)
        build.classify('game/dlc_fafow/**', None)
        build.classify('game/dlc_fafwm/**', None)
        build.classify('game/dlc_lively/**', None)
        build.classify('Supporter Pack/**', None)
    if steam:
        build.classify('game/platforms_generic.rpyc', None)
    else:
        build.classify('game/steam.rpyc', None)
        build.classify('game/platforms_steam.rpyc', None)
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('game/**.rpy', None)
    build.classify('game/**_ren.py', None)
    build.classify('game/**.xcf', None)
    build.classify('geany_project.pj', None)
    build.classify('game/elite.rpyc', None)
    build.classify('game/debug_tools.rpyc', None)
    build.classify('ideas.txt', None)
    build.classify('requirements.txt', None)
    build.classify('game/**.txt', None)
    build.classify('**.geany', None)
    build.classify('docs/**', None)
    build.classify('game/dev/**', None)
    build.classify('game/python-packages/timeit.py', None)
    build.classify('scripts/**', None)
    build.classify('platform_configs/**', None)
    build.classify('.gitlab/**', None)
    build.classify('var/**', None)
    build.classify('ci_changelog.txt', None)
    build.classify('**.keystore', None)
    build.classify('game/updater_module/**', 'updater_module')
    build.classify('game/dlc_breemc/**', 'dlc_breemc')
    build.classify('game/dlc_fafow/**', 'dlc_fafow')
    build.classify('game/dlc_fafwm/**', 'dlc_fafwm')
    build.classify('game/dlc_lively/**', 'dlc_lively')
    build.classify('game/**.rpyc', 'scripts')
    build.classify('game/**.yml', 'scripts')
    build.classify('game/music/**.ogg', 'audio')
    build.classify('game/sd/**.ogg', 'audio')
    if renpy.android:
        build.classify('game/vo/**.ogg', None)
    else:
        build.classify('game/vo/**.ogg', 'audio')
    build.classify('game/**.webm', 'vi')
    build.classify('game/ads/**', 'interface')
    build.classify('game/gui/**', 'interface')
    build.classify('game/bg/**.png', 'bg')
    build.classify('game/bg/**.webp', 'bg')
    build.classify('game/bg/**.rpyc', 'bg')
    for ch_name in ch_names:
        build.classify('game/ch/' + ch_name + '/**', ch_name)
    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.webp', 'archive')
    if not steam:
        build.classify("Supporter Pack/**", "supporter_pack")
    if steam and not demo:
        build.classify('Supporter Pack', "all")
    build.classify('game/temp/**', None)
    build.documentation('*.html')
    build.documentation('*.txt')
    # build.package("supporter_pack", "bare-zip", "supporter_pack")
    # build.package("standalone_dlcs", "directory", "dlcs", "Standalone all DLCS only", update=False, dlc=True)
    # build.package("market_complete", "bare-zip", "windows linux mac renpy all dlcs", "Markets Core files and all DLCS")
    # build.package("market_dlcs", "directory", "dlcs", "Markets all DLCS only", update=False, dlc=True)
    # build.package("pc_itchio", "zip", "windows linux renpy all itchio", "Itchio PC: Core files and defined DLCS")
    # build.package("mac_itchio", "app-zip app-dmg", "mac renpy all itchio", "Itchio Macintosh Core files and defined DLCS")
    # build.package("android_itchio", "directory", "android all", "Itchio Android Core files", hidden=True, update=False, dlc=True)
    # build.package("pc_patreon", "zip", "windows linux renpy all patreon", "Patreon PC: Core files and defined DLCS")
    # build.package("mac_patreon", "app-zip app-dmg", "mac renpy all patreon", "Patreon Macintosh Core files and defined DLCS")
    # build.package("android_patreon", "directory", "android all", "Patreon Android Core files", hidden=True, update=False, dlc=True)
    # build.package("gameonly_patreon", "null", "all patreon", "Game-Only Update for Mobile")
    # build.package("gameonly_itchio", "null", "all itchio", "Game-Only Update for Mobile")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
