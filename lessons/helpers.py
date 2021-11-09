"""Example of functions imported elsewhere."""


THE_ANSWER: int = 42


def main() -> None:
    print(powerful(2, 16))
    print(f"helpers.py: {__name__}")
    print("Evaluated as a program")


def powerful(x: float, n: float) -> float:
    """Raise x to the power of n."""
    return x ** n


print(f"helpers.py: {__name__}")

if __name__ == "__main__":
    # Python idiom:
    main()