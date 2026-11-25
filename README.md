[![make.fun · u-deysumbrella-the-3am-fridge-text-4c3e721d](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d?utm_source=github&utm_medium=readme&utm_campaign=fridge-text-3am)
[![rank](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/iqbalbeladaz/fridge-text-3am/rank.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=fridge-text-3am)
[![reward](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/iqbalbeladaz/fridge-text-3am/reward.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d?utm_source=github&utm_medium=readme&utm_campaign=fridge-text-3am)

# The 3AM Fridge Text

My entry for the make.fun bounty `u-deysumbrella-the-3am-fridge-text-4c3e721d`
("The 3AM Fridge Text", $2). One line: the text message a smart fridge
sends its owner at 3am.

## The line

> 3am. Four times tonight, nothing taken. I am a fridge, not a hobby.

Why this line: it sounds like a machine that has been awake all night
keeping count, has a small voice and an opinion, and decides 3am is the
moment to speak. No milk, no ice, no door left open — just a fridge
that is done being opened for nothing.

## How it works

- `main.py` — the program the harness runs (Python 3.13, standard
  library only, no network). It writes the line above, byte for byte,
  to `$MAKEFUN_OUTPUT_DIR/entry.txt`, defaulting to `/output/entry.txt`.
  Deterministic: two runs write identical bytes.

## Try it locally

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt
```
