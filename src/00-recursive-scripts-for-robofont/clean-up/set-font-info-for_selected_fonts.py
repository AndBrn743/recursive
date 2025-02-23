from vanilla.dialogs import *

inputFonts = getFile(
    "select UFOs", allowsMultipleSelection=True, fileTypes=["ufo"])
    
# prop = 'Sans'

for fontPath in inputFonts:
    font = OpenFont(fontPath, showInterface=False)

    # for other font info attributes, see
    # http://unifiedfontobject.org/versions/ufo3/fontinfo.plist/

    print("family: ", font.info.familyName, "\n ", "style: ", font.info.styleName)
    
    

    # f.info.openTypeOS2VendorID = "ARRW"
    # if prop in font.info.familyName:
        
    
    #     currentStyleName = font.info.styleName
        
    #     if currentStyleName.split(' ')[-1] == "Italic":   
    #         font.info.styleName = f"{prop} {currentStyleName.split(' ')[-3]} {currentStyleName.split(' ')[-2]} Slanted"
    #     else:
    #         font.info.styleName = f"{prop} {currentStyleName.split(' ')[-2]} {currentStyleName.split(' ')[-1]}"

    # font.info.copyright = "Copyright 2019 The Recursive Project Authors (github.com/arrowtype/recursive)"
    # print("copyright updated")

    if "Sans" in font.info.familyName:
        font.info.familyName = "RecEditFeb13 Sans"
        font.info.styleName = font.info.styleName.replace("Sans ", "")
    if "Mono" in font.info.familyName:
        font.info.familyName = "RecEditFeb13 Mono"
        font.info.styleName = font.info.styleName.replace("Mono ", "")


    print("changed to:")
    print("family: ", font.info.familyName, "\n ", "style: ", font.info.styleName)
    print("")

    font.save()
    font.close()
