init 1:
    layeredimage dylan:
        always:
            "dylan_body"
        group exp auto:
            attribute normal default
        group arms auto:
            attribute back default
        attribute hypnoze null
        always:
            if_any "fx"
            "dylan_fx_light"
        always:
            if_any "fx"
            "dylan_fx_spiral"

    layeredimage dylan close:
        yalign 0.0
        always:
            "dylan_body"
        group exp auto:
            attribute normal default
        attribute fx null
        always:
            if_any "fx"
            "dylan_fx_light"
        always:
            if_any "fx"
            "dylan_fx_spiral"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
