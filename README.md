# Wordsearch Solver

Quick little project to generate and solve word searches!

Written mostly on a plane for my brother, who asked me to.

Not very optimized at all, but fast enough on a reasonably sized board.

## Example

```
$ python wordsearch/wordsearch.py --board-size 5 --min-word-length 3
-------------
| w c q w e |
| c x c u v |
| l l h z r |
| h x i p r |
| t o s k b |
-------------
-------------
|         e |
|     c u   |
|     h   r |
|     i   r |
| t o s   b |
-------------
chi
hue
his
sot
brr
```

## Usage

```bash
python wordsearch/wordsearch.py
python wordsearch/wordsearch.py --help
python wordsearch/wordsearch.py --board-size 100
...etc
```

## Testing

Install ``pytest`` and run ``py.test``
