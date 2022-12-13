import io
import os
import hunk
import extract
import matplotlib.pyplot as plt


def main(input_: io.TextIOWrapper, output: io.TextIOWrapper = None):
    """
    Extract stats from a LLM request log and plot them to a file.

    Args:
      :input_: something like 'AtB.00.stats'
      :output: something like 'AtB.00.stats.png'. Defaults to the input_
               filename appended with '.plot.png'
    
    Returns: None
    """

    if output is None:
        output = input_.name + '.plot.png'
    else:
        output = output.name

    stats = extract.preceding_stats(input_)

    fig, ax = plt.subplots(3, 1, figsize=(4, 6))
    
    utilization = [k / 4096 for k in stats['n_tokens']]

    ax[0].plot(stats['content'],  label='cnt')
    ax[1].plot(utilization,       label='uti')
    ax[2].plot(stats['salience'], label='sal')

    ax[0].set_title("content")
    ax[1].set_title("utilization")
    ax[2].set_title("salience")

    fig.suptitle("BookWorm attention head stats")
    plt.tight_layout()
    plt.savefig(output)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", action='store',
                        type=argparse.FileType('r'), dest='input',
                        help="The log file from which to extract")
    parser.add_argument("-o", "--output", action='store', 
                        type=argparse.FileType('w'), dest='output',
                        help="The name of the output file", default=None)
    args = parser.parse_args()

    main(args.input, args.output)

