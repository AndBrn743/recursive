import os
import shutil
import pync
from pathlib import Path
from build_files import buildFiles, getFolders
from build_variable import build_variable
from build_static import build_static
from utils import getFiles, makeWOFF

if __name__ == "__main__":
    import argparse
    description = """Font builder for Recursive"""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-v", "--version",
                        help="Version for the fonts")
    parser.add_argument("-o", "--out",
                        help="Directory for final fonts")
    parser.add_argument("-a", "--all", action="store_true",
                        help="Build all (source files, variable, static fonts, & WOFF")
    parser.add_argument("-f", "--files", action="store_true",
                        help="Build source files for mastering")
    parser.add_argument("-fvar", "--varfiles", action="store_true",
                        help="Build source files for mastering variable font only")
    parser.add_argument("-fstat", "--statfiles", action="store_true",
                        help="Build source files for mastering static fonts only")
    parser.add_argument("-var", "--variable", action="store_true",
                        help="Build variable font")
    parser.add_argument("-s", "--static", action="store_true",
                        help="Build static fonts")
    parser.add_argument("-w", "--woff", action="store_true",
                        help="Make WOFF & WOFF2 of generated fonts")
    parser.add_argument("-p", "--pync", action="store_true",
                        help="Get pinged with Mac notifications when the build has completed. Mac only.")

    args = parser.parse_args()

    if args.version:
        version = args.version
    else:
        version = "0.000"

    if args.out:
        out = args.out
    else:
        out = os.path.join(Path(os.getcwd()).parents[0], f"fonts_{version}")

    if not os.path.exists(out):
        os.mkdir(out)

    outPaths = [os.path.join(out, "Variable_TTF"),
                os.path.join(out, "Static_OTF"),
                os.path.join(out, "Static_TTF")]

    if args.all:
        args.files = True
        args.variable = True
        args.static = True
        args.woff = True

    if args.files:
        files = buildFiles(version=version)
    else:
        files = getFolders("recursive-MONO_CASL_wght_slnt_ital--full_gsub.designspace")

    if args.variable:
        build_variable(designspacePath=files["designspace"],
                       out=os.path.join(outPaths[0],
                                        f"Recursive_VF_{version}.ttf"))
        if args.pync:
            pync.notify('Variable files built!', title='Recursive Build')

    if args.varfiles:
        files = buildFiles(version=version, static=False)
        if args.pync:
            pync.notify('Variable files prepped!', title='Recursive Build')
    if args.statfiles:
        files = buildFiles(version=version, variable=False)
        if args.pync:
            pync.notify('Static files prepped!', title='Recursive Build')

    if args.static:
        build_static(files["cff"], files["ttf"], out)
        if args.pync:
            pync.notify('Static files built!', title='Recursive Build')

    if args.woff:
        for path in outPaths:
            if os.path.exists(path):
                ttfs = getFiles(path, "ttf")
                otfs = getFiles(path, "otf")
                fonts = ttfs + otfs
                print(f"🏗  Making WOFFs for {path}")
                makeWOFF(fonts, os.path.join(path, "WOFF2"))
        if args.pync:
            pync.notify('Woff & woff2 files built!', title='Recursive Build')
