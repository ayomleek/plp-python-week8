# Personal Mini-Toolkit

A menu-driven Python program that bundles four small tools into one app. It loops until you choose Quit and never crashes on bad input.

## What the toolkit does

| # | Tool | Description |
|---|------|-------------|
| 1 | Number Guessing Game | Guess a secret number from 1 to 100 in 7 tries, with "too high / too low" hints. |
| 2 | To-Do List | Add, view, complete and remove tasks. The list is kept while the program runs. |
| 3 | Simple Calculator | Add, subtract, multiply or divide two numbers, with divide-by-zero and bad-input protection. |
| 4 | Countdown Timer | Counts down from 1 to 30 seconds, one second at a time. |
| 5 | Quit | Exits with a friendly goodbye. |

**Concepts practised:** variables, input/output, f-strings, `if` / `elif` / `else`, `while` and `for` loops, lists (`append`, `pop`, `enumerate`), functions, `try` / `except`, and the `random` and `time` modules.

## How to run

You need Python 3.6 or newer. No extra packages are required.

```bash
git clone https://github.com/ayomleek/plp-python-week8.git
cd plp-python-week8
python toolkit.py
```

On some systems use `python3 toolkit.py`. Type a number from 1 to 5 and press Enter. Press `Ctrl+C` at any time to exit safely.

## Repository contents

- `toolkit_plan.txt` – the plan written before coding
- `toolkit.py` – the program
- `screenshots/` – the menu (including an invalid choice) and each tool running
- `README.md` – this file

## Reflection

The hardest part was making every tool survive unexpected input, because users can type letters, blanks or out-of-range numbers at any prompt. Wrapping conversions in `try` / `except` and validating ranges fixed most of that. The bug that took longest was in the guessing game, where an invalid guess like "abc" was being counted as a used attempt. I fixed it by using `continue` before the attempt counter increases. Writing `toolkit_plan.txt` first really helped, since I already knew the exact menu text and which concept each tool would show off. Splitting each tool into its own function also made the menu loop short and easy to read. Keeping the to-do list in `main()` and passing it into the tool meant tasks are not lost when returning to the menu. With one more week I would save the to-do list to a file so it survives restarts, add a name formatter and unit converter, and keep a high-score table for the guessing game.