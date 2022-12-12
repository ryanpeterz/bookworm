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
    tokens: int

    def __init__(self, text: str, tokens: Optional[int] = None):
        self.text = text
        # tokens, tokens, tokens!
        if tokens is None:
            tokens = len(_BookWorm_tokenizer(text)['input_ids']) 
        self.tokens = tokens

    def __add__(self, other: Hunk) -> Hunk:
        return Hunk(text=self.text + other.text,
                    tokens=self.tokens + other.tokens)

    def __str__(self) -> str:
        return f"Hunk({self.tokens}, {self.text})"

    def __repr__(self) -> str:
        if len(self.text) < 13: return str(self)
        return f"Hunk({self.tokens}, {self.text[:14]}...)" 

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
def of_known_size(tokens: int, text: str) -> Hunk: return Hunk(text, tokens)

