define cherie_nvl = Character("Cherie", kind=nvl, callback=Phone_SendSound)
label text_sentence_cherie(sentence):
    if sentence.endswith((".", "?", "!")):
        cherie_nvl "[sentence]"
    else:
        cherie_nvl "[sentence]."
    return

define claire_nvl = Character("Claire", kind=nvl, callback=Phone_SendSound)
label text_sentence_claire(sentence):
    if sentence.endswith((".", "?", "!")):
        claire_nvl "[sentence]"
    else:
        claire_nvl "[sentence]."
    return

define kiara_nvl = Character("Kiara", kind=nvl, callback=Phone_SendSound)
label text_sentence_kiara(sentence):
    if sentence.endswith((".", "?", "!")):
        kiara_nvl "[sentence]"
    else:
        kiara_nvl "[sentence]."
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
