'''
Build accented glyphs in RoboFont3 using Glyph Construction.

'''
from vanilla.dialogs import *
from glyphConstruction import ParseGlyphConstructionListFromString, GlyphConstructionBuilder



# zerosuperior.slash = zerosuperior
# zeroinferior.slash = zeroinferior
# zerosuperiorslash.afrc = zerosuperior.afrc
# zeroinferiorslash.afrc = zeroinferior.afrc
txt = '''\
onequarter = onesuperior & fraction.split & fourinferior
threequarters = threesuperior & fraction.split & fourinferior
onethird = onesuperior & fraction.split & threeinferior
twothirds = twosuperior & fraction.split & threeinferior
oneeighth = onesuperior & fraction.split & eightinferior
threeeighths = threesuperior & fraction.split & eightinferior
fiveeighths = fivesuperior & fraction.split & eightinferior
seveneighths = sevensuperior & fraction.split & eightinferior
onequarter.afrc = onesuperior.afrc & fraction.split & fourinferior.afrc 
threequarters.afrc = threesuperior.afrc & fraction.split & fourinferior.afrc 
onethird.afrc = onesuperior.afrc & fraction.split & threeinferior.afrc
twothirds.afrc = twosuperior.afrc & fraction.split & threeinferior.afrc
oneeighth.afrc = onesuperior.afrc &  fraction.split & eightinferior.afrc
threeeighths.afrc = threesuperior.afrc & fraction.split & eightinferior.afrc
fiveeighths.afrc = fivesuperior.afrc & fraction.split & eightinferior.afrc
seveneighths.afrc = sevensuperior.afrc & fraction.split & eightinferior.afrc
'''

print(txt)
# get the actual glyph constructions from text
constructions = ParseGlyphConstructionListFromString(txt)



files = getFile("Select files to build glyphs in", allowsMultipleSelection=True, fileTypes=["ufo"])

# collect glyphs to ignore if they already exist in the font
ignoreExisting = [L.split('=')[0].strip()[1:] for L in txt.split('\n') if L.startswith('?')]

# Set to False to open fonts with RoboFont UI (e.g. to visually check changes before saving)
skipInterface = True

for file in files:

    if skipInterface:
        font = OpenFont(file, showInterface=False)
    else:
        font = OpenFont(file, showInterface=True)

    # iterate over all glyph constructions
    for construction in constructions:

        print(construction)
        # build a construction glyph
        constructionGlyph = GlyphConstructionBuilder(construction, font)

        # if the construction for this glyph was preceded by `?`
        # and the glyph already exists in the font, skip it
        if constructionGlyph.name in font and constructionGlyph.name in ignoreExisting:
            continue

        # get the destination glyph in the font
        glyph = font.newGlyph(constructionGlyph.name, clear=True)

        # draw the construction glyph into the destination glyph
        constructionGlyph.draw(glyph.getPen())

        # copy construction glyph attributes to the destination glyph
        glyph.name = constructionGlyph.name
        glyph.unicode = constructionGlyph.unicode
        glyph.width = constructionGlyph.width
        glyph.markColor = 0, 0, 0, 0.5

        # if no unicode was given, try to set it automatically
        if glyph.unicode is None:
            glyph.autoUnicodes()

    if skipInterface:
        font.save()
        font.close()
