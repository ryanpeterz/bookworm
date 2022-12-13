"""
A limited implementation of token algrebra sufficient for BookWorm's purposes.
"""
from __future__ import annotations
from typing import Optional
import token
from pathlib import Path
from typing import List
from transformers import GPT2Tokenizer

_BookWorm_tokenizer = GPT2Tokenizer.from_pretrained("gpt2")


class Hunk:
    text: str
    _len: int
    
    def __init__(self, text: str, size: Optional[int] = None):
        self.text = text
        self._len = size

    @property
    def tokens(self) -> List[int]:
        return _BookWorm_tokenizer(self.text)['input_ids']

    def __len__(self) -> int:
        if _len is None:
            self._len = len(self.tokens)
        return self._len

    def __add__(self, other: Hunk) -> Hunk:
        return Hunk(text=self.text + other.text,
                    size=len(self) + len(other))

    def __str__(self) -> str:
        return f"Hunk({len(self)}, {self.text})"

    def __repr__(self) -> str:
        if len(self.text) < 13: return str(self)
        return f"Hunk({len(self)}, {self.text[:14]}...)" 


MT = Hunk('', 0)
SP = Hunk(' ', 1)
NL = Hunk('\n', 1)

__all__ = ["Hunk", "MT", "SP", "NL"]


def generator(fp: Path, sep: str = '\n\n') -> Hunk:
    with fp.open('r') as f:
        lines: List[str] = []
        for line in f:
            line = line.rstrip()
            if line:
                lines.append(line)
            else:
                yield Hunk(text='\n'.join(lines))
                lines = []
    
    if len(lines):
        yield Hunk(text='\n'.join(lines))

def of_text(text: str) -> Hunk: return Hunk(text)
def of_known_size(size: int, text: str) -> Hunk: return Hunk(text, size)

