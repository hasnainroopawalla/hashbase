from typing import List, Literal


Z = pow(2, 32)


def rotate_left(x: int, s: int) -> int:
    """Circular rotation of x left by s bit positions.

    Args:
        x (int): The input integer.
        s (int): The number of shifts (in bits).

    Returns:
        int: The left rotated value of the input integer.
    """
    return ((x << s) | (x >> (32 - s))) & 0xFFFFFFFF


def shift_left(x: int, s: int) -> int:
    """Shift x left by s bit positions.

    Args:
        x (int): The input integer.
        s (int): The number of shifts (in bits).

    Returns:
        int: The left shifted value of the input integer.
    """
    return (x << s) & 0xFFFFFFFF


def rotate_right(x: int, s: int):
    """Circular rotation of x right by s bit positions.

    Args:
        x (int): The input integer.
        s (int): The number of shifts (in bits).

    Returns:
        int: The right rotated value of the input integer.
    """
    return ((x >> s) | (x << (32 - s))) & 0xFFFFFFFF


def shift_right(x: int, s: int) -> int:
    """Shift x right by s bit positions.

    Args:
        x (int): The input integer.
        s (int): The number of shifts (in bits).

    Returns:
        int: The right shifted value of the input integer.
    """
    return (x >> s) & 0xFFFFFFFF


def modular_add(nums: List[int]) -> int:
    """Performs modular addition of all elements in nums, modulo 2^32.

    Args:
        nums (List[int]): A List of all the input integers.

    Returns:
        int: The value obtained after modular addition of all elements in nums.
    """
    return sum(nums) % Z


def apply_message_padding(
    message: bytearray, message_length_byteorder: Literal["little", "big"]
) -> bytearray:
    """Pre-processing for the input message.
    Appends a trailing '1'.
    Pad 0s to the message.
    Append message length to the message in little or big endian.

    Args:
        message (bytearray): The input message in bytes.
        message_length_byteorder (str): Can be either 'big' or 'little', indicating if the last 64 bits of the message (message length) are in the big or little endian convention.

    Returns:
        bytearray: The pre-processed message in bytes.
    """
    # Store the length of the message in bytes
    message_length = len(message)

    # Pad a trailing '1'
    message.append(0x80)

    # Pad 0s to assert a block length of 448 bits (56 bytes)
    while len(message) % 64 != 56:
        message.append(0)

    # Pad the last 64 bits that indicate the message length in the specified endian format
    message += (message_length * 8).to_bytes(8, byteorder=message_length_byteorder)

    return message
