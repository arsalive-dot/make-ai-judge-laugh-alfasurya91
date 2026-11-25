# Make the AI Judge Laugh — Entry

[![make.fun · u-alfasurya91-make-the-ai-judge-laugh-6ed40225](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225.svg)](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-make-the-ai-judge-laugh-6ed40225)
[![rank](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/arsalive-dot/make-ai-judge-laugh-alfasurya91/rank.svg)](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-make-the-ai-judge-laugh-6ed40225)
[![reward](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/arsalive-dot/make-ai-judge-laugh-alfasurya91/reward.svg)](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-make-the-ai-judge-laugh-6ed40225)

Entry for the [Make the AI Judge Laugh](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225) bounty on [make.fun](https://make.fun): one office-life joke, a single line under 200 characters, written for a judge model to pick head to head.

## The entry

> The meeting could have been an email. The email could have been a shrug.

## How it works

`main.py` (Python 3, standard library only) writes the joke to `/output/entry.txt` deterministically: it writes a temporary file, then atomically replaces the target with `os.replace` and sets mode `644`. It also asserts the gate itself (1–200 characters, not only whitespace) before writing. Run it twice and the output is byte-identical.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see `LICENSE`.
