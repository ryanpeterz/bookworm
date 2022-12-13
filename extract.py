import io
import hunk


def preceding(log: io.TextIOWrapper) -> hunk.Hunk:
    """
    Produces a generator from the input_ log that returns PRECEDING hunks
    """
    preceding = hunk.MT  # the empty hunk
    read: bool = False
    with log as i:
        for line in i:
            if "PRECEDING:" in line:
                read = True
                continue

            if read:
                if "PROMPT:" in line:
                    yield preceding
                    read = False
                    preceding = hunk.MT  # the empty hunk
                    continue
                
                preceding += hunk.of_text(line)
                preceding += hunk.NL    


def preceding_stats(log: io.TextIOWrapper) -> dict:
    """
    Extracts the PRECEDING hunks and returns their stats
    """
    # stats to collect:
    cnts, cnt = [], 0  # content
    tkcs, tkc = [], 0  # token_count
    sals      = []     # salience

    # only read lines between "PRECEDING:" and "PROMPT:"
    read: bool = False
    with log as f:
        for line in f:
            if "PRECEDING:" in line:
                read = True
                continue
    
            if read:
                if "PROMPT:" in line:
                    cnts.append(cnt)
                    tkcs.append(tkc)
                    sals.append(cnt / tkc)
                    read = False
                    cnt, tkc = 0, 0
                    continue
                
                hk = hunk.of_text(line)
                cnt += sum(hk.tokens)  # fast and dumb :)
                tkc += len(hk)

    return {'content':  cnts,
            'n_tokens': tkcs,
            'salience': sals}


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", action='store',
                        type=argparse.FileType('r'), dest='input',
                        help="The log file from which to extract")
    parser.add_argument("-o", "--output", action='store', 
                        type=argparse.FileType('w'), dest='output',
                        help="The name of the output file")
    args = parser.parse_args()
    
    with args.output as o:
        for hk in preceding(args.input):
            o.write(hk.text)
            o.write('<sep>')

