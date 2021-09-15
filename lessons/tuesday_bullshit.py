"""Challenge Quesion #1"""

def a(x: int) -> int:
    """a function."""
    x = x // 2 
    if x == 1:
        return 0
    else:
        return 1

def b(x: int) -> int:
    """another"""
    x = a(x + 1)
    return x

x: int = 2
print(b(x))