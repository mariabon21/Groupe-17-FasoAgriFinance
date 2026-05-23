# =====================================================================
# PART 1: THE VALIDATION CLASS (Anti-crash & Input Security)
# CONTRIBUTOR: KABORE Albertine
# =====================================================================
class Validator:
    """
    Groups all keyboard input verification functions.
    Uses the @staticmethod decorator to integrate cleanly in OOP.
    """
    
    @staticmethod
    def validate_string(prompt: str) -> str:
        """INSTRUCTION: Ensures the user enters text and does not leave the field empty."""
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("Error: This field cannot be empty.")

    @staticmethod
    def validate_integer(prompt: str) -> int:
        """INSTRUCTION: Prevents the program from crashing if letters are entered instead of an integer."""
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Type error: Please enter a valid integer.")

    @staticmethod
    def validate_float(prompt: str) -> float:
        """INSTRUCTION: Prevents the program from crashing if letters are entered instead of a decimal."""
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Type error: Please enter a decimal number.")

    @staticmethod
    def validate_boolean(prompt: str) -> bool:
        """
        STRICT INSTRUCTION: BOOLEAN TRAP FIX REQUIRED BY THE INSTRUCTOR.
        Parses the text string instead of doing a simple bool(input()).
        """
        while True:
            response = input(prompt).strip().lower()
            if response in ['yes', 'y', 'oui', 'o']:
                return True
            elif response in ['no', 'n', 'non']:
                return False
            print("Error: Please explicitly answer 'Yes' or 'No'.")
