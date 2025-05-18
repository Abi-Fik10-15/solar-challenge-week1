"""
main.py - Entry point for the Solar Challenge project.

This script defines a basic Greeter class as a starting point for developing more complex logic.
"""

class Greeter:
    """A simple class to greet the user."""

    def __init__(self, name="world"):
        """
        Initialize the greeter with a name.

        Args:
            name (str): The name to greet.
        """
        self.name = name

    def greet(self):
        """
        Generate a greeting message.

        Returns:
            str: A greeting string.
        """
        return f"Hello, {self.name}!"

def main():
    """
    Main function to execute the greeting logic.
    """
    greeter = Greeter()
    print(greeter.greet())

if __name__ == "__main__":
    main()
