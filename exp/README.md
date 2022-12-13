# `bookworm/exp`
Experiment submodule.
* `main.py` produces .gpt.log files
* They get moved here and renamed something informative. I've gone with 'SRC.NUM.log'.

## Example Use
```bash
~/path/to/bookworm$ python3 main.py "Answer to Burke"
~/path/to/bookworm$ mv .gpt.log exp/AtB.001.log
```

