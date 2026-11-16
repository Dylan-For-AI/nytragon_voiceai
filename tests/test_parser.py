from pathlib import Path

import pytest

from voiceai.parser import DialogueError, parse_dialogue

DATA_DIR = Path(__file__).parent.parent / "data"


def test_normal_dialogue():
    turns = parse_dialogue("Nurse: Hello.\nPatient: Hi.")
    assert len(turns) == 2
    assert turns[0].speaker == "Nurse"
    assert turns[1].text == "Hi."


def test_empty_text_returns_empty_list():
    assert parse_dialogue("") == []


def test_blank_lines_are_ignored():
    turns = parse_dialogue("Nurse: Hello.\n\n   \nPatient: Hi.\n")
    assert len(turns) == 2


def test_unknown_speaker_raises():
    with pytest.raises(DialogueError):
        parse_dialogue("Doctor: Hello.")


def test_line_without_colon_raises():
    with pytest.raises(DialogueError):
        parse_dialogue("Nurse Hello.")


def test_colon_inside_text_is_kept():
    turns = parse_dialogue("Patient: My dose is: one pill.")
    assert turns[0].text == "My dose is: one pill."


@pytest.mark.parametrize("name", ["dialogue1.txt", "dialogue2.txt", "dialogue3.txt"])
def test_real_files_parse(name):
    from voiceai.parser import load_dialogue

    assert len(load_dialogue(DATA_DIR / name)) > 0