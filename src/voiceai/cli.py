import argparse
import sys
from pathlib import Path

from voiceai.parser import DialogueError, load_dialogue


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Parse a synthetic dialogue file.")
    parser.add_argument("path", type=Path, help="Path to a dialogue .txt file")
    args = parser.parse_args(argv)

    try:
        turns = load_dialogue(args.path)
    except (DialogueError, FileNotFoundError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    for turn in turns:
        print(f"[{turn.speaker}] {turn.text}")
    print(f"{len(turns)} turns parsed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())