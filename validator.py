# =====================================================================
# PART 1 — VALIDATED INPUTS
# str, int, float, bool | while + try/except | correct boolean
# CONTRIBUTOR: KABORE Albertine
# =====================================================================

def read_string(prompt: str) -> str:
    """Validated string input — re-prompts if the field is left empty."""
    while True:
        value = input(prompt).strip()           # str
        if value:
            return value
        print(f"  Error: this field cannot be empty.")


def read_int(prompt: str) -> int:
    """Validated integer input — try/except prevents crash on bad input."""
    while True:
        try:
            return int(input(prompt))           # int — explicit type cast
        except ValueError:
            print(f"  Error: please enter a whole number (e.g. 28).")


def read_float(prompt: str) -> float:
    """Validated decimal input — try/except prevents crash on bad input."""
    while True:
        try:
            return float(input(prompt))         # float — explicit type cast
        except ValueError:
            print(f"  Error: please enter a decimal number (e.g. 3.5).")


def read_bool(prompt: str) -> bool:
    """
    Validated boolean input.
    CORRECT:  input().strip().lower() == "yes"  →  True / False
    WRONG:    bool(input())  →  always True for any non-empty string
    """
    while True:
        answer = input(prompt).strip().lower()  # str first
        if answer in ["yes", "y", "oui", "o"]:
            return True                         # bool
        elif answer in ["no", "n", "non"]:
            return False                        # bool
        print(f"  Error: please answer yes or no.")

