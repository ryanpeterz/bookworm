"""
BookWorm: Book --> Notes

The highest quality answers derive from prompts that include as much 
information as possible in the PREAMBLE.

Human beings are adept at working on systems too large for them to comprehend.
(Our attention is so pervasively mediated that the medium is invisible to us.)
By using cognitive tools like written language and diagramatic representation,
the limited attention space of human mind can ingest information and reason
between concepts of staggering complexity. As the tower of concepts grows, the
effects of compression become evident --- it is difficult to reason about two
high-level concepts which do not share a pedagogical foundation.

Although GPT-3 lacks the wisdom of transcendental experience, it does have a
different reasoning advantage --- it can natively attend to a far greater
amount of language information than any human being can. In order to derive
novel conclusions from GPT-3, this advantage must be put to its fullest use.

No matter how large the attention head grows for GPT-n, highly relevant text
will remain too long to feed directly into a prompt. One may attempt to
circumvent the issue by designing a memory module and giving CRUD affordances
to a controlling agent.

:Toward an LLM-embedded Virtual Computer:

In this work, I investigate whether it is possible to use linguistic ability
alone to simulate the short-to-medium-term memory module necessary for 
comprehension. Since LLMs have well-documented summarization capabilities, I
use this capacity in analogy with a blockchain hashing protocol. As the
ingested text reaches the size of GPT-3's attention, I ask it to summarize
what it has read, and feed that summary back into the preamble for
the next prompt.

I believe this method can be extended to many established blockchain data
structures. I am most excited about the possiblity of a Merkle-tree analogy as
a method to synthesize multiple sources and arrive at a well-reasoned,
explainable conclusion. This established chain of reasoning can be interrogated
just as any human's, but, as in the courts and in our scientific pursuits,
the explanation can be established as *prior* to the action.

The completions may derive from internet garbage text, but the validity of the
connections is what compels their use for sensationalized narrativism. By
enforcing that the connections are followed forward from first principles
instead of confabulated from shallowly desired conclusions, I predispose
BookWorm to draw *authentically* explainable conclusions.

Furthermore, because these conclusions are derived from a text processor with
larger available attention than any human, it may be possible to establish
relationships of a different character from human internet discourse, while
maintaining the human readable nature that defines LLM the completion objective.

In reimagining physics, Copenhagen & Mermin espoused to "shut up and calculate".
If we wish to put large language models to the task of comprehension and novel
suggestion, there is no substitute for doing the reading.
"""

import sources
import hunk
import ask
import prompts

def main(source, token_budget: int = 4096, preamble_budget: int = 3000):
    """
    An LLM can attend to a limited token space. That token space can be used
    for every describable purpose. To account for this finite resource, I
    partition the token space into human-meaningful pieces:

    1. CONTEXT:  the environment & history
    2. SUBJECT:  the 'working memory' of the operation
    3. PROMPT:   the objective, policy, etc. 
    4. RESPONSE: model output

    When working with a Completion-based LLM, I have found it useful to refer
    to the CONTEXT, SUBJECT and PROMPT partitions as falling into the PREAMBLE.
    From the LLM perspective, the PREAMBLE is a heady introduction to its work
    which must be lived up to.

    BookWorm's CONTEXT initially contains only the title of the work. As the
    LLM progresses through the material, summaries of the content are appended
    to the CONTEXT after the title. To ensure the LLM properly attends to the
    CONTEXT, I change the PROMPT to reflect the ontology of the CONTEXT as it
    progresses.

    Inspired by blockchain construction techniques, I implement BookWorm via
    the following program:

    1. Identify the largest hunk of text which can fit into the SUBJECT
    2. Politely ask the LLM to compress this hunk into a summary
    3. Append the summary to the CONTEXT
    4. If necessary, condense the CONTEXT
    5. Update the PROMPT to draw due attention to the new CONTEXT
    6. Repeat

    Due to the simple nature of linear text ingestion, the PROMPT iterations
    fall into only three forms: Initial, Ongoing, and Final. These forms also
    serve as prototypes for a recursive knowledge tree implementation, but some
    node-rank-conditional adjustments must be made in order to properly map the
    LLM attention in each case.
    """
    
    # PHASE 0: Collect sources, define resources
    n: int = len(source.hunks)  # hunk count
    i: int = 0                  # hunk index

    # PHASE 1: Initial Prompt
    empty_prompt = prompts.initial(source.title, hunk.MT)
    
    remaining_tokens = token_budget - len(empty_prompt)
    text_token_limit = 2 * remaining_tokens // 3
    text = hunk.MT

    # Accumulate hunks up to limit
    while i < n:
        if len(source.hunks[i]) < text_token_limit:
            text_token_limit -= len(source.hunks[i])
            text += source.hunks[i]
            i += 1
        else:
            break

    if i >= n:
        raise RuntimeError("BookWorm reads long form text >_>'")

    # Return initial salients
    preceding = ask.politely(prompts.initial(source.title, text)) 
    
    # PHASE 2: Ongoing Prompt
    empty_prompt = prompts.ongoing(source.title, preceding, hunk.MT)
    remaining_tokens = token_budget - len(empty_prompt)
    text_token_limit = 2 * remaining_tokens // 3
    text = hunk.MT
        
    # Accumulate hunks up to limit
    while i < n:
        if len(source.hunks[i]) < text_token_limit:
            text_token_limit -= len(source.hunks[i])
            text += source.hunks[i]
            i += 1
        elif len(text) > 0:
            preceding += ask.politely(prompts.ongoing(source.title,
                                                      preceding, text))
            # Refresh text buffer
            empty_prompt = prompts.ongoing(source.title, preceding, hunk.MT)
            if len(empty_prompt) > preamble_budget:
                preceding = ask.politely(prompts.condense(source.title,
                                                          preceding))
                empty_prompt = prompts.ongoing(source.title, preceding,
                                               hunk.MT)
            remaining_tokens = token_budget - len(empty_prompt)
            text_token_limit = 2 * remaining_tokens // 3
            text = hunk.MT
        else:
            print(f"Bad hunk >:( {i=} ):<")
            breakpoint()

    return preceding

    # Phase 3: Comprehension
    response = ask.politely(prompts.final(source.title, preceding))
    print(response.text)
    return response


if __name__ == "__main__": 
    import argparse
    parser = argparse.ArgumentParser(description="Read some text and return notes.")
    parser.add_argument('title', type=str, help="What to read.", default="Answer to Burke")
    args = parser.parse_args()
    
    source = sources.get(args.title)
    main(source)

