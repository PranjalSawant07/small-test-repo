# test_script.py
def add_numbers(a, b):
    """Add two numbers and return the sum."""
    return a + b


def greet_user(name):
    """Return a friendly greeting for the given user."""
    return f"Hello, {name}! Welcome to the automation test."


if __name__ == "__main__":
    print(add_numbers(5, 3))
    print(greet_user("Pranjal"))
