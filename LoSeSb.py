#!/usr/bin/env python

# This file is part of Ren'Py. The license below applies to Ren'Py only.
# Games and other projects that use Ren'Py may use a different license.

# Copyright 2004-2026 Tom Rothamel <pytom@bishoujo.us>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from __future__ import print_function, absolute_import

import os
import sys
import warnings
from pathlib import Path
import shutil


# Functions to be customized by distributors. ################################

def get_android_game_name():
    import renpy
    if renpy.config.basedir.endswith("/base"):
        android_game_name = os.path.basename(os.path.dirname(os.path.dirname(renpy.config.basedir)))
    else:
        android_game_name = os.path.basename(os.path.dirname(renpy.config.basedir))
    return android_game_name.replace("com.andrealphusgames.", "")


def try_create_folder(d):
    try:
        os.makedirs(d)
        print(f"try_create_folder: created_folder: {d}")
        return True
    except Exception as e:
        print(f"try_create_folder: fail_to_create_folder: {d} - {e}")
        return False

def path_to_gamedir(basedir, name):
    """
    Returns the absolute path to the directory containing the game
    scripts an assets. (This becomes config.gamedir.)

    `basedir`
        The base directory (config.basedir)
    `name`
        The basename of the executable, with the extension removed.
    """

    # A list of candidate game directory names.
    candidates = [ name ]

    # Add candidate names that are based on the name of the executable,
    # split at spaces and underscores.
    game_name = name

    while game_name:
        prefix = game_name[0]
        game_name = game_name[1:]

        if prefix == ' ' or prefix == '_':
            candidates.append(game_name)

    # Add default candidates.
    candidates.extend([ 'game', 'data', 'launcher/game' ])

    # Take the first candidate that exists.
    for i in candidates:

        if i == "renpy":
            continue

        gamedir = os.path.join(basedir, i)

        if os.path.isdir(gamedir):
            break

    else:
        gamedir = basedir

    return gamedir


def path_to_common(renpy_base):
    """
    Returns the absolute path to the Ren'Py common directory.

    `renpy_base`
        The absolute path to the Ren'Py base directory, the directory
        containing this file.
    """
    path = renpy_base + "/renpy/common"

    if os.path.isdir(path):
        return path
    return None


def path_to_saves(gamedir, save_directory=None): # type: (str, str|None) -> str
    """
    Given the path to a Ren'Py game directory, and the value of config.
    save_directory, returns absolute path to the directory where save files
    will be placed.

    `gamedir`
        The absolute path to the game directory.

    `save_directory`
        The value of config.save_directory.
    """

    import renpy # @UnresolvedImport

    if save_directory is None:
        save_directory = renpy.config.save_directory
        save_directory = renpy.exports.fsencode(save_directory) # type: ignore

    # Makes sure the permissions are right on the save directory.
    def test_writable(d):
        try:
            fn = os.path.join(d, "test.txt")
            open(fn, "w").close()
            open(fn, "r").close()
            os.unlink(fn)
            return True
        except Exception:
            return False

    # Android.
    if renpy.android:

        android_game_name = get_android_game_name()

        root_documents_renpy_saves = os.path.join(os.environ["ANDROID_DOCUMENTS"], "RenPy_Saves")
        root_documents_game_name = os.path.join(root_documents_renpy_saves, android_game_name)
        root_documents_game_assets = os.path.join(root_documents_game_name, "game")

        paths = [
            root_documents_game_name,
            os.path.join(os.environ["ANDROID_OLD_PUBLIC"], "game/saves"),
            os.path.join(os.environ["ANDROID_PRIVATE"], "saves"),
            os.path.join(os.environ["ANDROID_PUBLIC"], "saves"),
            ]

        if not os.path.isdir(
            root_documents_game_assets
        ):
            try_create_folder(
                root_documents_game_assets
            )
        if not os.path.isdir(os.path.join(os.environ["ANDROID_PUBLIC"], "game")):
            try_create_folder(os.path.join(os.environ["ANDROID_PUBLIC"], "game"))

        for rv in paths:
            if not os.path.isdir(rv):
                try_create_folder(rv)
            if os.path.isdir(rv) and test_writable(rv):
                break
        else:
            rv = paths[-1]

        print("Saving to", rv)
        return rv

    if renpy.ios:
        from pyobjus import autoclass # type: ignore
        from pyobjus.objc_py_types import enum # type: ignore

        NSSearchPathDirectory = enum("NSSearchPathDirectory", NSDocumentDirectory=9)
        NSSearchPathDomainMask = enum("NSSearchPathDomainMask", NSUserDomainMask=1)

        NSFileManager = autoclass('NSFileManager')
        manager = NSFileManager.defaultManager()
        url = manager.URLsForDirectory_inDomains_(
            NSSearchPathDirectory.NSDocumentDirectory,
            NSSearchPathDomainMask.NSUserDomainMask,
            ).lastObject()

        # url.path seems to change type based on iOS version, for some reason.
        try:
            rv = url.path().UTF8String()
        except Exception:
            rv = url.path.UTF8String()


        if isinstance(rv, bytes):
            rv = rv.decode("utf-8")

        print("Saving to", rv)
        return rv

    # No save directory given.
    if not save_directory:
        return os.path.join(gamedir, "saves")

    if "RENPY_PATH_TO_SAVES" in os.environ:
        return os.environ["RENPY_PATH_TO_SAVES"] + "/" + save_directory

    # Search the path above Ren'Py for a directory named "Ren'Py Data".
    # If it exists, then use that for our save directory.
    path = renpy.config.renpy_base

    while True:
        if os.path.isdir(path + "/Ren'Py Data"):
            return path + "/Ren'Py Data/" + save_directory

        newpath = os.path.dirname(path)
        if path == newpath:
            break
        path = newpath

    # Otherwise, put the saves in a platform-specific location.
    if renpy.macintosh:
        rv = "~/Library/RenPy/" + save_directory
        return os.path.expanduser(rv)

    elif renpy.windows:
        if 'APPDATA' in os.environ:
            return os.environ['APPDATA'] + "/RenPy/" + save_directory
        else:
            rv = "~/RenPy/" + renpy.config.save_directory # type: ignore
            return os.path.expanduser(rv)

    else:
        rv = "~/.renpy/" + save_directory
        return os.path.expanduser(rv)


# Returns the path to the Ren'Py base directory (containing common and
# the launcher, usually.)
def path_to_renpy_base():
    """
    Returns the absolute path to the Ren'Py base directory.
    """

    renpy_base = os.path.dirname(os.path.abspath(__file__))
    renpy_base = os.path.abspath(renpy_base)

    return renpy_base

def path_to_logdir(basedir):
    """
    Returns the absolute path to the log directory.
    `basedir`
        The base directory (config.basedir)
    """

    import renpy # @UnresolvedImport

    if renpy.android:
        return os.environ['ANDROID_PUBLIC']

    return basedir


def copy_dir(s, d):
    import os
    import shutil

    # specify the source and destination directories
    src_dir = s
    dst_dir = d

    # use os.listdir() to get a list of all files in the source directory
    files = os.listdir(src_dir)

    # iterate through the list of files
    for file in files:
        if file.endswith(".save") or file == "persistent":
            # construct the full path to the file in the source and destination directories
            src_file = os.path.join(src_dir, file)
            dst_file = os.path.join(dst_dir, file)
            if os.path.isfile(src_file):
                # check if the file already exists in the destination directory
                if os.path.exists(dst_file):
                    # if the file already exists, check if it has been modified
                    if os.path.getmtime(src_file) > os.path.getmtime(dst_file):
                        # if the file has been modified, copy it to the destination directory
                        shutil.copy2(src_file, dst_file)
                else:
                    # if the file does not exist in the destination directory, copy it
                    shutil.copy2(src_file, dst_file)


def predefined_searchpath(commondir):
    import renpy # @UnresolvedImport

    # The default gamedir, in private.
    searchpath = [ renpy.config.gamedir ]

    # The default gamedir, in private.
    renpy.config.searchpath = [renpy.config.gamedir]

    # The public android directory.
    if "ANDROID_PUBLIC" in os.environ:

        android_game = os.path.join(os.environ["ANDROID_PUBLIC"], "game")

        android_game_name = get_android_game_name()

        root_documents_renpy_saves = os.path.join(os.environ["ANDROID_DOCUMENTS"], "RenPy_Saves")
        root_documents_game_name = os.path.join(root_documents_renpy_saves, android_game_name)
        root_documents_game_assets = os.path.join(root_documents_game_name, "game")
        root_documents_game_saves = os.path.join(root_documents_game_name, "saves")

        ##COPY DATA FROM STOCK
        if os.path.exists("//sdcard//Android//data//"):
            if os.path.exists(
                root_documents_game_name
            ):
                if os.path.exists(os.path.join(os.environ["ANDROID_PRIVATE"], "saves")):
                    try:
                        copy_dir(
                            os.path.join(os.environ["ANDROID_PRIVATE"], "saves"),
                            root_documents_game_name,
                        )

                        copy_dir(
                            root_documents_game_name,
                            os.path.join(os.environ["ANDROID_PRIVATE"], "saves"),
                        )
                        print(
                            "Attempting to sync your saves from/to stock ANDROID_PRIVATE location..."
                        )
                    except Exception:
                        print("Failed to sync your saves from/to stock ANDROID_PRIVATE")
                        pass

                if not os.path.exists(
                    os.path.join(os.environ["ANDROID_PUBLIC"], "saves")
                ):
                    try:
                        try_create_folder(
                            os.path.join(os.environ["ANDROID_PUBLIC"], "saves")
                        )
                    except Exception:
                        print("Failed to create ANDROID_PUBLIC")
                        pass
                if os.path.exists(os.path.join(os.environ["ANDROID_PUBLIC"], "saves")):
                    if not os.path.exists(root_documents_game_saves):
                        try:
                            copy_dir(
                                os.path.join(os.environ["ANDROID_PUBLIC"], "saves"),
                                root_documents_game_name,
                            )

                            copy_dir(
                                root_documents_game_name,
                                os.path.join(os.environ["ANDROID_PUBLIC"], "saves"),
                            )
                            print(
                                "Attempting to sync your saves to/from stock ANDROID_PUBLIC location..."
                            )
                        except Exception:
                            print(
                                "Failed to sync your saves to/from stock ANDROID_PUBLIC"
                            )
                            pass

                if os.path.exists(
                    os.path.join(os.environ["ANDROID_OLD_PUBLIC"], "game/saves")
                ):
                    if not os.path.exists(root_documents_game_saves):
                        try:
                            copy_dir(
                                os.path.join(os.environ["ANDROID_OLD_PUBLIC"], "game/saves"),
                                root_documents_game_name,
                            )

                            copy_dir(
                                root_documents_game_name,
                                os.path.join(os.environ["ANDROID_OLD_PUBLIC"], "game/saves"),
                            )
                            print(
                                "Attempting to sync your saves to/from stock ANDROID_OLD_PUBLIC location..."
                            )
                        except Exception:
                            print(
                                "Failed to sync your saves to/from stock ANDROID_OLD_PUBLIC"
                            )
                            pass
                if os.path.exists(root_documents_game_saves):
                    try:
                        src_path = root_documents_game_saves

                        for each_file in Path(src_path).glob("*.*"):
                            trg_path = each_file.parent.parent
                            each_file.rename(trg_path.joinpath(each_file.name))

                        if os.path.exists(
                            os.path.join(root_documents_game_saves, "persistent")
                        ):
                            shutil.move(
                                os.path.join(root_documents_game_saves, "persistent"),
                                os.path.join(root_documents_game_name, "persistent")
                            )

                        if os.path.exists(
                            root_documents_game_saves
                        ):
                            os.rmdir(
                                root_documents_game_saves
                            )
                            print(f"Saves copied to /sdcard/Documents/RenPy_Saves/{android_game_name}")
                    except Exception:
                        print("Failed correct save placement ")
                        pass

                if os.path.exists(
                    os.path.join(root_documents_game_name, "temp",)
                ):
                    try:
                        src_path = os.path.join(root_documents_game_name, "temp",)

                        for each_file in Path(src_path).glob("*.*"):
                            trg_path = each_file.parent.parent
                            each_file.rename(trg_path.joinpath(each_file.name))
                            print(f"Saves and mods moved to /sdcard/Documents/RenPy_Saves/{android_game_name}")

                        if os.path.exists(
                            os.path.join(root_documents_game_name, "temp", "persistent",)
                        ):
                            shutil.move(
                                os.path.join(root_documents_game_name, "temp", "persistent",),
                                os.path.join(root_documents_game_name, "persistent",),
                            )
                        if os.path.exists(
                            os.path.join(root_documents_game_name, "temp",)
                        ):
                            os.rmdir(os.path.join(root_documents_game_name, "temp",)
                            )
                    except Exception:
                        print("Failed correct save placement ")
                        pass

        if not os.path.isdir(root_documents_game_name):
            try_create_folder(root_documents_game_name)

        if not os.path.exists(os.path.join(root_documents_game_name, "text.txt")):
            with open(os.path.join(root_documents_game_name, "text.txt"), "w") as f:
                f.write(f"Ren'Py Game - {android_game_name}\n")

        if not os.path.exists(os.path.join(root_documents_game_name, "test.txt")):
            with open(os.path.join(root_documents_game_name, "test.txt"), "w") as f:
                f.write(f"Ren'Py Game - {android_game_name}\n")

        if not os.path.isdir(
            root_documents_game_assets
        ):
            try_create_folder(root_documents_game_assets
            )

        if os.path.isdir(
            root_documents_game_assets
        ):
            searchpath.append(
                root_documents_game_assets
            )

        if os.path.exists(android_game):
            renpy.config.searchpath.insert(1, android_game)

        # Asset packs.
        packs = [
            "ANDROID_PACK_FF1", "ANDROID_PACK_FF2",
            "ANDROID_PACK_FF3", "ANDROID_PACK_FF4",
        ]

        for i in packs:
            if i not in os.environ:
                continue

            assets = os.environ[i]

            for i in [ "renpy/common", "game" ]:
                dn = os.path.join(assets, i)
                if os.path.isdir(dn):
                    searchpath.append(dn)
    else:
        # Add path from env variable, if any
        if "RENPY_SEARCHPATH" in os.environ:
            searchpath.extend(os.environ["RENPY_SEARCHPATH"].split("::"))

    if "ANDROID_PUBLIC" not in os.environ:
        if commondir and os.path.isdir(commondir):
            searchpath.append(commondir)

    if renpy.android or renpy.ios:
        print("Mobile search paths:" , " ".join(searchpath))

    return searchpath

##############################################################################


android = ("ANDROID_PRIVATE" in os.environ)

def main():

    renpy_base = path_to_renpy_base()

    sys.path.append(renpy_base)

    # Ignore warnings.
    warnings.simplefilter("ignore", DeprecationWarning)

    # Start Ren'Py proper.
    try:
        import renpy.bootstrap
    except ImportError:
        print("Could not import renpy.bootstrap. Please ensure you decompressed Ren'Py", file=sys.stderr)
        print("correctly, preserving the directory structure.", file=sys.stderr)
        raise

    # Set renpy.__main__ to this module.
    renpy.__main__ = sys.modules[__name__] # type: ignore

    renpy.bootstrap.bootstrap(renpy_base)


if __name__ == "__main__":
    main()
