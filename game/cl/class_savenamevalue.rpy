
init python:



    class SaveNameValue(InputValue):
        def __init__(self, var, slotnumber, default=""):
            self.var = var
            self.slotnumber = slotnumber
            
            if not hasattr(store, var):
                setattr(store, var, default)
        
        def get_text(self):
            return FileSaveName(self.slotnumber)
        
        def set_text(self, s):
            setattr(store, self.var, s)
        
        def enter(self):
            renpy.run(FileSave(self.slotnumber))
            renpy.run(Hide("save_name_dialogue"))


    def jsoncallback(d):
        d["save_version"] = config.version


    config.save_json_callbacks.append(jsoncallback)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
