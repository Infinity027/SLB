init 1:
    layeredimage lily teaser:
        group body_version:
            attribute human null default
            attribute succubus null

        group outfit_version:
            attribute casual null default
            attribute naked null

        group body auto variant human when human
        group body auto variant succubus when succubus
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
