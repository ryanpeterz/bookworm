import parse
from pathlib import Path


def get(title: str) -> object:
    if title != "Rights of Man": raise KeyError
    
    return parse.main(Path(__file__).parent/'data'/'rights_of_man',
                      override=True)

