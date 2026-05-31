define amy_nvl = Character("Amy", kind=nvl, callback=Phone_SendSound)
label text_sentence_amy(sentence):
    if sentence.endswith((".", "?", "!")):
        amy_nvl "[sentence]"
    else:
        amy_nvl "[sentence]."
    return

define kat_nvl = Character("Kat", kind=nvl, callback=Phone_SendSound)
label text_sentence_kat(sentence):
    if sentence.endswith((".", "?", "!")):
        kat_nvl "[sentence]"
    else:
        kat_nvl "[sentence]."
    return

define reona_nvl = Character("Reona", kind=nvl, callback=Phone_SendSound)
label text_sentence_reona(sentence):
    if sentence.endswith((".", "?", "!")):
        reona_nvl "[sentence]"
    else:
        reona_nvl "[sentence]."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
