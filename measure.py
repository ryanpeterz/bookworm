from transformers import GPT2Tokenizer, TFGPT2LMHeadModel
import tensorflow as tf

_tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
_model = TFGPT2LMHeadModel.from_pretrained('gpt2')


def perplexity(text: hunk.Hunk, model=_model, tokenizer=_tokenizer) -> float:
    hk = hunk.MT
    for k in text.tokens:
        hk += k
    inputs = tokenizer(hk, return_tensors="tf")
    breakpoint()


def main():
    

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
            o.write('<sep>)

