import sys
import os
from fontParts.world import *

try:
	if sys.argv[1]:
		print("Getting UFO paths")
		dirToUpdate = sys.argv[1]
		subDirs = next(os.walk(dirToUpdate))[1]
		ufosToCheck = [ path for path in subDirs if path.endswith(".ufo")]
		head = dirToUpdate
	if sys.argv[2]:
		glyphToCheck = sys.argv[2]
		print(glyphToCheck)

except IndexError:
	print("Please include args: <glyphName> and <directory containing UFOs>")

print(ufosToCheck)

firstColWidth = 20

print("")
print("FONT".ljust(firstColWidth + 1), end=" ")
print("|", end=" ")

key = "| 🥐 = curve | 📏 = line | 🚚 = move | 🥨 = qcurve"
print(f"Contours & segments in /{glyphToCheck} {key}")

print("".ljust(firstColWidth + 1, "-") + " | " + "".ljust(96, "-"))


for ufo in sorted(ufosToCheck):
	ufoPath = f"{head}/{ufo}"
	# print(ufoPath)

	f = OpenFont(ufoPath, showInterface=False)

	# g = f[glyphToCheck]

	print(f.info.styleName.ljust(firstColWidth + 1), end=" ")
	print("|", end=" ")
	for i, c in enumerate(f[glyphToCheck]):
		print(f"C{str(i).rjust(2, '0')}", end=" ")
		print(f"[{len(c.segments)}]", end=" ")
		for s in c:
			if s.type == "line":
				print("📏", end=" ")
			elif s.type == "curve":
				print("🥐", end=" ")
			elif s.type == "move":
				print("🚚", end=" ")
			elif s.type == "qcurve":
				print("🥨", end=" ")
		print("|", end=" ")
	print("")
		
	f.close()