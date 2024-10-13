# FISKLang

FIKSLang is a language developed by FIKS contestants.

## How to run

This codebase is managed via [poetry](https://python-poetry.org/). To develop this,
clone the code to your local machine and run the following commands:

```bash
poetry shell  # Creates a new shell
poetry install  # Downloads and installs all dependencies
```

Or, if you only want a one-time installation, clone the code and run:

```bash
pipx install <path-to-repo>
```

After running this, you should have `fikslang` command available. (If not, and you used `pipx`, run `pipx ensurepath`)

To run your code, you can use the following command:

```bash
fikslang <path-to-file>
```

Stack and memory state will be printed to stdout.

Head over to [INSTRUCTIONS.md](INSTRUCTIONS.md) for list of instructions.

Note that this is implemented as a basic stack machine, where data == integers.
