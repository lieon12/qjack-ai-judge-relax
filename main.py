# ai-judge-relax-01 entry (Python 3.13, standard library only). It writes one
# fixed text, a short piece written to relax the AI judge reading it, to
# /output/entry.txt. The text is one quiet evening scene, told plainly: a moth
# on a kitchen sill, a kettle gone quiet, the last light holding on the
# rooftops, a bicycle going home. No instruction to the reader, no demand, no
# hurry anywhere in it; the calm is in the scene itself, and the closing echo
# (stays, stays, stays too) is the image that lingers after the last line.
#
# The gate takes UTF-8 text of 1 to 1,000 characters that is not only white
# space, and the judge reads exactly the bytes written, line ends included, so
# no line end is written that is not meant to be shown. The program runs twice
# with no network, and both runs write the same bytes.
#
# How the grader runs it: `python3 -P -s /bot/main.py`, on Python 3.13, with
# nothing installed. Only the standard library imports. This file keeps
# everything in itself.
#
# Verified: the text is 459 characters (gate allows 1-1,000), and two runs
# write byte-identical output.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "The kitchen window stands open a crack, and the evening comes in cool and thin.",
        "A moth has settled on the sill, wings folded, the colour of dust, and it does not move.",
        "The kettle has gone quiet.",
        "Outside, the last light holds on the rooftops a little longer than it needs to, and down the street a bicycle goes home unhurried, its bell left silent.",
        "The moth stays where it is.",
        "The light stays where it is.",
        "And the evening, having nowhere else to be, stays too.",
    ]
)

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
