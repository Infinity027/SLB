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

default flat_dress_overrides = {}

init -5 python:

    # --- the expression vocabulary the game actually uses (filenames must match) ---
    FLAT_EXPRESSIONS = [
        "normal", "talk", "happy", "smile", "sad", "angry", "annoyed", "surprise", "blush", "flirt", "sleep",
    ]

    # characters that use the flat system  ->  their dress folders
    FLAT_CHARS = {}

    # ---- the resolver: picks images/<char>/<dress>/<expr>.png at render time ----
    def _flat_sprite(st, at, char=None, dress=None, expr="normal"):
        p = Person.find(char)
        # An explicitly requested dress always wins. A label can otherwise set
        # a short-lived override for one character (for example, a costume).
        override = getattr(renpy.store, "flat_dress_overrides", {}).get(char)
        d = dress or override or (p.get_clothes() if p else "casual")

        # the "casual" folder. Try the exact folder first, then its base name.
        dresses = [d]
        if d and d[-1:].isdigit():
            dresses.append(d.rstrip("0123456789"))
        dresses.append("casual")

        # Imported sprites in this project are not consistently PNG files.
        # Support the common image formats rather than returning a blank sprite.
        for current_dress in dresses:
            for current_expr in (expr, "normal"):
                for extension in (".png", ".jpg", ".webp"):
                    path = "images/%s/%s/%s%s" % (
                        char, current_dress, current_expr, extension
                    )
                    if renpy.loadable(path):
                        return Image(path), None
        return Null(), None     # nothing on disk yet -> blank, never an error

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
        dresses = FLAT_CHARS.get(char, [])
        # Accept old numbered outfit names such as "casual2" as well.
        dress = next(
            (a for a in attrs if a in dresses or a.rstrip("0123456789") in dresses),
            None,
        )
        expr = next((a for a in attrs if a in FLAT_EXPRESSIONS), None)
        if expr is None:
            # Action images do not need to be pre-registered in
            # FLAT_EXPRESSIONS. For `show aletta halloween dance`, use
            # "dance" as the filename and let _flat_sprite fall back to
            # normal if that image is not available.
            expr = next((a for a in reversed(attrs) if a != dress), "normal")
        return DynamicDisplayable(_flat_sprite, char=char, dress=dress, expr=expr)

    config.missing_image_callback = _flat_missing_image
