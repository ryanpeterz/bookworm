import parse
from pathlib import Path

def get(title: str) -> parse.Wad:
    if title != "Answer to Burke":
        raise KeyError("The only known source is 'Answer to Burke'") 
    
    return parse.main(Path(__file__).parent/'data'/'rights_of_man',
                      override=True)[0]  # the 0th Wad is Answer to Burke

