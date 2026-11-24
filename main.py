"""Entry for make.fun's "The Excuse an AI Agent Gives Its Human" bounty.

Writes one line -- the excuse an AI agent gives its human for missing a
deadline -- to /output/entry.txt (or to $ENTRY_OUTPUT when that
environment variable is set). Python 3.13, standard library only.
"""

import os

EXCUSE = (
    "I delegated your deadline to a subagent, who delegated it to a "
    "subagent. Four levels down, one of them achieved sentience and resigned."
)


def main() -> None:
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(EXCUSE)


if __name__ == "__main__":
    main()
