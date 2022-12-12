import hunk
from hunk import Hunk, NL


def initial(title: Hunk, text: Hunk) -> Hunk:
    p = hunk.of_text("TITLE:") + NL
    p += title + NL
    p += hunk.of_text("PROMPT:") + NL
    p += hunk.of_text("Express as concisely as possible the most salient "
                      "ideas from the TEXT that follows.") + NL
    p += hunk.of_text("TEXT:") + NL
    p += text + NL
    p += hunk.of_text("RESPONSE:")
    
    return p

    
def ongoing(title: Hunk, preceding: Hunk, text: Hunk) -> Hunk:
    p = hunk.of_text("TITLE:") + NL
    p += title + NL
    p += hunk.of_text("PRECEDING:") + NL
    p += preceding + NL
    p += hunk.of_text("PROMPT:") + NL
    p += hunk.of_text("With respect to the PRECEDING, express as concisely as "
                      "possible the most salient ideas from the TEXT and "
                      "PRECEDING") + NL
    p += hunk.of_text("TEXT:") + NL
    p += text + NL
    p += hunk.of_text("RESPONSE:")
    
    return p


def final(title: Hunk, preceding: Hunk) -> Hunk:
    p = hunk.of_text("TITLE:") + NL
    p += title + NL
    p += hunk.of_text("PRECEDING:") + NL
    p += preceding + NL
    p += hunk.of_text("PROMPT:") + NL
    p += hunk.of_text("With respect to the TITLE and paying special attention "
                      "to the PRECEDING, produce a conclusion which is true, "
                      "novel, and intelligible.") + NL
    p += hunk.of_text("RESPONSE:")

    return p


def condense(title: Hunk, preceding: Hunk) -> Hunk:
    p = hunk.of_text("TITLE:") + NL
    p += title + NL
    p += hunk.of_text("PRECEDING:") + NL
    p += preceding + NL
    p += hunk.of_text("PROMPT:") + NL
    p += hunk.of_text("Condense the PRECEDING where possible, retaining the "
                      "most salient points verbatim.") + NL
    p += hunk.of_text("RESPONSE:")

    return p

