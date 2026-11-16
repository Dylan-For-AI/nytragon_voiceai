from pathlib import Path
from pydantic import BaseModel

SPEAKERS = {"Nurse", "Patient"}


class DialogueError(ValueError):
    """Raised when a dialogue does not follow the expected format."""


class Turn(BaseModel):
    speaker: str
    text: str


def parse_dialogue(text: str) -> list[Turn]:
    turns: list[Turn] = []
    for number, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.strip()
        if not line:
            continue
        if ":" not in line:
            raise DialogueError(f"Line {number}: missing ':' separator")
        speaker, content = line.split(":", 1)
        speaker = speaker.strip()
        content = content.strip()
        if speaker not in SPEAKERS:
            raise DialogueError(f"Line {number}: unknown speaker '{speaker}'")
        if not content:
            raise DialogueError(f"Line {number}: empty text for '{speaker}'")
        turns.append(Turn(speaker=speaker, text=content))
    return turns


def load_dialogue(path: Path) -> list[Turn]:
    return parse_dialogue(path.read_text(encoding="utf-8"))