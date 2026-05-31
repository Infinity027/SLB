init python:

    renpy.music.register_channel('music1', "music", loop=False)
    renpy.music.register_channel('music2', "music", loop=False)

    renpy.music.register_channel("sexsfx1", "sexsfx", loop=False)
    renpy.music.register_channel("sexsfx2", "sexsfx", loop=False)

    renpy.music.register_channel("ambience", "ambience", loop=False)


    if not renpy.music.channel_defined("tts"):
        renpy.music.register_channel("tts")


    renpy.music.register_channel('sfx1', "sfx", loop=False)
    renpy.music.register_channel('sfx2', "sfx", loop=False)
    renpy.music.register_channel('sfx3', "sfx", loop=False)
    renpy.music.register_channel('sfx4', "sfx", loop=False)

    def toggle_mute_all_characters():
        if not persistent.mute_characters:
            for c in people_ids:
                if c not in persistent._voice_mute:
                    persistent._voice_mute.add(c)
            persistent.mute_characters = True
        else:
            for c in people_ids:
                if c in persistent._voice_mute:
                    persistent._voice_mute.discard(c)
            persistent.mute_characters = False
        renpy.restart_interaction()

    def toggle_tts_override_voice_channel():
        
        if not persistent.tts_override:
            renpy.config.tts_voice_channels = ["tts"]
            persistent.tts_override = True
            if not persistent.mute_characters:
                toggle_mute_all_characters()
        else:
            renpy.config.tts_voice_channels = ["voice"]
            persistent.tts_override = False
            if persistent.mute_characters:
                toggle_mute_all_characters()

define af = renpy.audio.filter

label stop_all_sfx:

    stop sound
    $ renpy.music.set_pan(pan=0,delay=0,channel="sound")
    $ renpy.music.set_audio_filter("sound", None)
    stop voice
    $ renpy.music.set_pan(pan=0,delay=0,channel="voice")
    $ renpy.music.set_audio_filter("voice", None)
    stop sexsfx1
    $ renpy.music.set_pan(pan=0,delay=0,channel="sexsfx1")
    $ renpy.music.set_audio_filter("sexsfx1", None)
    stop sexsfx2
    $ renpy.music.set_pan(pan=0,delay=0,channel="sexsfx2")
    $ renpy.music.set_audio_filter("sexsfx2", None)
    stop sfx1
    $ renpy.music.set_pan(pan=0,delay=0,channel="sfx1")
    $ renpy.music.set_audio_filter("sfx1", None)
    stop sfx2
    $ renpy.music.set_pan(pan=0,delay=0,channel="sfx2")
    $ renpy.music.set_audio_filter("sfx2", None)
    stop sfx3
    $ renpy.music.set_pan(pan=0,delay=0,channel="sfx3")
    $ renpy.music.set_audio_filter("sfx3", None)
    stop sfx4
    $ renpy.music.set_pan(pan=0,delay=0,channel="sfx4")
    $ renpy.music.set_audio_filter("sfx4", None)
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
