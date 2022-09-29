Z = pow(2, 32)


def left_shift(x: int, s: int) -> int:
    """Circularly shift (rotate) x left by s bit positions.

    Args:
        x (int): The input integer.
        s (int): The number of shifts (in bits).

    Returns:
        int: The left shifted value of the input integer.
    """
    return ((x << s) | (x >> (32 - s))) & 0xFFFFFFFF


def modular_add(x: int, y: int) -> int:
    """Performs modular addition of x and y modulo 2^32.

    Args:
        x (int): The first integer.
        y (int): The second integer.

    Returns:
        int: The value obtained after modulo addition of x and y.
    """
    return (x + y) % Z
