# `bookworm/ana`
Analysis submodule.
## To Extract Precedings
The logs contain a bunch of information about what requests sent to and responses received from gtp3. The `extract.py` script pulls out only the PRECEDING hunks and saves them to a file, separated with '<sep>'. It is not necessary to run this before running `plot.py`.
*To extract only the PRECEDINGs from the 00th 'Answer to Burke' (AtB) log*
```bash
~/path/to/bookworm$ python3 extract.py -i exp/AtB.00.log -o ana/AtB.00.pre
```

*It is not (currently) necessary to run `extract.py` before running `plot.py`. There is not enough separation/indirection between parsing the logs, calculating the stats, and plotting them. That can all be done via `plot.py`.*
