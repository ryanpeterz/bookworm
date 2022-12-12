r"""Parse the 'Rights of Man' source text into hunks.

Author: Thomas Paine
Source: https://www.ushistory.org/Paine/rights/
Format:
    .
    |-Answer to Burke (1.AtB)
    | |-01-
    | |-::
    | |-16-
    | '
    |-Society and Civilization (2.SaC)-
    |-Present Old Governments (3.POG)-
    |-Systems of Government (4.SoG)-
    |-Constitutions (5.C)-
    |-Ways and Means (6.WaM)
    ' |-1-
      |-:
      |-8-
      '
    Each of the leaves in the above tree is a file, while non-leaves are
    directories. Each file contains text which is separated into hunks. The
    hunks are delineated by double newline character '\n\n'.

A hunk is an atomic unit of text with respect to comprehension. A hunk may have
multiple lines, but if any line is missing, the hunk will read as incomplete.
A well-defined hunk has a static token size, though the token size is not given
in the source.

Knowing the correct token size is neither trivial nor frivolous.
This parser splits text into hunks and identifies the number of tokens in each.
"""
import json
import hunk
import ask
import os

from pathlib import Path
from dataclasses import dataclass
from typing import List

@dataclass
class Wad:
    label: str
    title: hunk.Hunk
    hunks: List[hunk.Hunk]


VERIFY_ATTEMPTS: int = 3

def verify_parse(fp, attempts: int = 3, override: bool = False) -> bool:
    if override: return True
    for _ in range(attempts):
        yn = input(f"Parse file '{fp}'? [y/n]: ")
        if yn == 'y': return True
        if yn == 'n': return False
        print(f"Unrecognized option: {yn}")

    raise RuntimeError("Exceeded max number of verification attempts.")


def main(src: Path, override: bool = False) -> List[Wad]:
    """
    
    """
    if not src.is_dir(): raise ValueError(f"{src=} must be a directory.")

    # Answer to Burke (AtB)
    title = "Being an Answer to Mr. Burke's Attack on the French Revolution"
    AtB = Wad(label="Answer to Burke",
              title=hunk.of_text(title),
              hunks=[])

    for i, fp in enumerate(sorted(src.glob('AtB/*'))):
        if not verify_parse(fp, override=override):
            print(f"Skipping file '{fp}'")
            continue

        for h in hunk.generator(fp):
            AtB.hunks.append(h)

    # Society and Civilization (SaC)
    # Present Old Governments (POG)
    # Systems of Government (SoG)
    # Constitutions (C)
    # Ways and Means (WaM)

    return [AtB,]


if __name__ == "__main__":
    import argparse
    import pathlib
    parser = argparse.ArgumentParser(
        prog = 'HunkParser',
        description = 'Parses raw text into hunks for BookWorm',
        epilog = 'Slow due to missed rustful tokenizer implementation.'
                 'Remember to compute calmly ^_^')
    parser.add_argument('src',
                        type=pathlib.Path,
                        help="The base directory of the source, "
			     "e.g. sources/rights_of_man")
    parser.add_argument('-y',
                        action='store_true',
                        help="Override file parser verification (force yes)")
    args = parser.parse_args()
    main(args.src, args.y)

