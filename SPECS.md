# SPECS: Week 1 (dialogue parser and note model)

## Goal
I build a program that reads a synthetic dialogue file with nurse and patient (3 scenarios/dialogues) and turns it into a clean list of speaker turns. This is the first step of the VoiceAI pipeline.

## Input (what a dialogue file looks like)
A .txt file in data/. Each line has the format "Speaker: text".
The only valid speakers are "Nurse" and "Patient".

## Output (what the program returns)
A list of turns. Each turn contains a speaker and the text they said.

## Edge cases (empty file, unknown speaker, blank lines)
- Empty file: returns an empty list.
- Unknown speaker (for example "Doctor:"): raises an error (fail fast),
  because silently accepting bad data is worse than a visible failure.
- Blank line: ignored.
- Line without a colon: raises an error.

## Out of scope (what I will NOT do this week)
- No audio and no AI model this week.
- No real patient data, only dialogues I wrote myself.
- No extraction of symptoms or allergies yet.

## Done when (3 checkable conditions)
1. pytest passes with at least 4 tests (normal case, empty file,
   unknown speaker, blank line).
2. The program reads the 3 files in data/ without error.
3. ruff reports no problem.