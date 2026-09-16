# =============================================================================
#  FLAT SPRITE SYSTEM  (replaces the split eyes/mouth/dress layeredimages)
#
#  One flat image per look:   images/<char>/<dress>/<expression>.png
#  The DRESS is chosen automatically from <char>.get_clothes() (activity-based),
#  so existing `show <char> <expression>` lines keep working unchanged.
#
#  To convert a character:
#    1) in ch/<char>/images.rpy  call:  register_flat_character("<char>", [dresses])
#    2) drop images into          game/images/<char>/<dress>/<expression>.png
#  See ch/sasha/images.rpy for a worked example.
# =============================================================================

init -5 python:

    # --- the expression vocabulary the game actually uses (filenames must match) ---
    FLAT_EXPRESSIONS = [
        "normal", "talk", "happy", "smile", "sad", "angry", "annoyed", "surprise", "blush", "flirt", "sleep",
    ]

    # --- sex-scene poses are a SEPARATE axis: images/<char>/poses/<pose>/<face>.png
    #     (only used as a safety net for now; full pose art comes later) ---
    FLAT_POSES = [
        "doggy", "cowgirl", "missionary", "cunnilingus", "reverse", "bj",
        "blowjob", "tittyfuck", "titfuck", "titjob", "spoon", "piledriver",
        "fullnelson", "carsex", "showersex", "lapdance", "threesome", "hj",
        "handjob", "mast", "stand", "standing", "spank", "spanking", "strap",
    ]

    # characters that use the flat system  ->  their dress folders
    FLAT_CHARS = {}

    # ---- the resolver: picks images/<char>/<dress>/<expr>.png at render time ----
    def _flat_sprite(st, at, char=None, dress=None, expr="normal"):
        p = Person.find(char)
        d = dress or (p.get_clothes() if p else "casual")
        for path in (
            "images/%s/%s/%s.png"     % (char, d, expr),       # exact dress + expression
            "images/%s/%s/normal.png" % (char, d),             # same dress, neutral face
            "images/%s/casual/%s.png" % (char, expr),          # casual dress, requested face
            "images/%s/casual/normal.png" % (char,),           # last resort
        ):
            if renpy.loadable(path):
                return Image(path), None
        return Null(), None     # nothing on disk yet -> blank, never an error

    def _flat_pose(st, at, char=None, pose=None, face="normal"):
        for path in (
            "images/%s/poses/%s/%s.png" % (char, pose, face),
            "images/%s/poses/%s/normal.png" % (char, pose),
        ):
            if renpy.loadable(path):
                return Image(path), None
        return Null(), None

    # ---- register all standard talking forms for a character ----
    def register_flat_character(char_id, dresses):
        # expression only:  show sasha happy   (dress comes from get_clothes())
        for e in FLAT_EXPRESSIONS:
            renpy.image((char_id, e),
                        DynamicDisplayable(_flat_sprite, char=char_id, expr=e))
        # dress only (room display):  show sasha casual
        # and dress + expression:     show sasha casual happy
        for dr in dresses:
            renpy.image((char_id, dr),
                        DynamicDisplayable(_flat_sprite, char=char_id, dress=dr, expr="normal"))
            for e in FLAT_EXPRESSIONS:
                renpy.image((char_id, dr, e),
                            DynamicDisplayable(_flat_sprite, char=char_id, dress=dr, expr=e))
        FLAT_CHARS[char_id] = list(dresses)

    # ---- safety net: any OTHER show of a flat char (poses, odd combos, close-ups)
    #      resolves to a flat image or a blank, so scenes never crash on a missing image.
    def _flat_missing_image(name):
        if not name or name[0] not in FLAT_CHARS:
            return None                       # not a flat char -> let Ren'Py handle it
        char = name[0]
        attrs = list(name[1:])
        pose = next((a for a in attrs if a in FLAT_POSES), None)
        if pose:
            face = next((a for a in attrs if a in FLAT_EXPRESSIONS), "normal")
            return DynamicDisplayable(_flat_pose, char=char, pose=pose, face=face)
        dress = next((a for a in attrs if a in FLAT_CHARS.get(char, [])), None)
        expr = next((a for a in attrs if a in FLAT_EXPRESSIONS), "normal")
        return DynamicDisplayable(_flat_sprite, char=char, dress=dress, expr=expr)

    config.missing_image_callback = _flat_missing_image
