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
# =====================================================================
# PART 2 — INHERITANCE
# Parent class, child class, super().__init__()
# CONTRIBUTOR: SIMPORE Alima
# =====================================================================
 
class Person:
    """Parent class — stores the identity shared by all system users."""
 
    def __init__(self, last_name: str, first_name: str, age: int, phone: str):
        self.last_name  = last_name    # str
        self.first_name = first_name   # str
        self.age        = age          # int
        self.phone      = phone        # str
 
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
 
 
class FarmerAccount(Person):
    """
    Child class — a FarmerAccount IS A Person.
    Inherits identity from Person and adds farm-specific data and methods.
    """
 
    total_accounts = 0
 
    def __init__(self, last_name: str, first_name: str, age: int, phone: str,
                 farm_size: float, crop: str, savings: float, is_coop_member: bool):
 
        super().__init__(last_name, first_name, age, phone)
 
        self.farm_size      = farm_size        # float
        self.crop           = crop             # str
        self.savings        = savings          # float
        self.is_coop_member = is_coop_member   # bool
 
        FarmerAccount.total_accounts += 1

