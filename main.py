"""One-sentence absurd invention pitch.

Writes a single sentence (<= 220 chars) to /output/entry.txt.
"""

import os

# The annoyance: burnt toast always sets off the smoke alarm.
# The fix: dispose of the evidence mid-air, before the alarm can object.
ENTRY = (
    "A toaster with a tiny catapult that flings burnt toast out the window "
    "before the smoke alarm can press charges."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
