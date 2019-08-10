
from vanilla.dialogs import *

glyphsWithSupportLayer = "w"

inputFonts = getFile(
    "select UFOs", allowsMultipleSelection=True, fileTypes=["ufo"])


print("Glyphs that shouldn't be in layer `support.w.middle`:")


def checkFont(f):
    print("\n", f.info.styleName)

    problems = []
    for layer in f.layers:
        if layer.name == "support.w.middle":
            for glyphName in layer.keys():
                if glyphName not in glyphsWithSupportLayer.split(" "):
                    print("  •", glyphName)
                    problems.append(glyphName)
    if not problems:
        print("\t🤖 Looks good.")

                    # del layer[glyphName] # NOT WORKING YET


for file in inputFonts:
    f = OpenFont(file, showInterface=False)
    for layer in f.layers:
        if layer.name == "support.w.middle":
            checkFont(f)
    f.close()
