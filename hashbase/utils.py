from typing import List, Literal


def rotate_left(x: int, s: int, size: int = 32) -> int:
    """Circular rotation of x left by s bit positions.

    Args:
        x (int): The input integer.
        s (int): The number of shifts (in bits).
        size (int): The size of the input/output in bits.

    Returns:
        int: The left rotated value of the input integer.
    """
    z = 0xFFFFFFFF if size == 32 else 0xFFFFFFFFFFFFFFFF
    return ((x << s) | (x >> (size - s))) & z


def shift_left(x: int, s: int, size: int = 32) -> int:
    """Shift x left by s bit positions.

    Args:
        x (int): The input integer.
        s (int): The number of shifts (in bits).
        size (int): The size of the input/output in bits.

    Returns:
        int: The left shifted value of the input integer.
    """
    z = 0xFFFFFFFF if size == 32 else 0xFFFFFFFFFFFFFFFF
    return (x << s) & z


def rotate_right(x: int, s: int, size: int = 32):
    """Circular rotation of x right by s bit positions.

    Args:
        x (int): The input integer.
        s (int): The number of shifts (in bits).
        size (int): The size of the input/output in bits.

    Returns:
        int: The right rotated value of the input integer.
    """
    z = 0xFFFFFFFF if size == 32 else 0xFFFFFFFFFFFFFFFF
    return ((x >> s) | (x << (size - s))) & z


def shift_right(x: int, s: int, size: int = 32) -> int:
    """Shift x right by s bit positions.

    Args:
        x (int): The input integer.
        s (int): The number of shifts (in bits).
        size (int): The size of the input/output in bits.

    Returns:
        int: The right shifted value of the input integer.
    """
    z = 0xFFFFFFFF if size == 32 else 0xFFFFFFFFFFFFFFFF
    return (x >> s) & z


def modular_add(nums: List[int], size: int = 32) -> int:
    """Performs modular addition of all elements in nums, modulo 2^32.

    Args:
        nums (List[int]): A List of all the input integers.
        size (int): The size of the input/output in bits.

    Returns:
        int: The value obtained after modular addition of all elements in nums.
    """
    z = 0xFFFFFFFF if size == 32 else 0xFFFFFFFFFFFFFFFF
    return sum(nums) & z


def apply_message_padding(
    message: bytearray,
    message_length_byteorder: Literal["little", "big"],
    message_length_padding_bits: int = 64,
    message_chunk_size_bits: int = 512,
) -> bytearray:
    """Pre-processing for the input message.
    Appends a trailing '1'.
    Pad 0s to the message.
    Append message length to the message in little or big endian.

    Args:
        message (bytearray): The input message in bytes.
        message_length_byteorder (str): Can be either 'big' or 'little', indicating if the last 64 bits of the message (message length) are in the big or little endian convention.
        message_length_padding_bits (int): The number of bits to be appended at the end of the message chunk to indicate the length of the original message.
        message_chunk_size_bits (int): The size of the message chunk in bits.

    Returns:
        bytearray: The pre-processed message in bytes.
    """
    # Store the length of the message in bits
    original_message_length_in_bits = len(message) * 8

    # Pad a trailing '1'
    message.append(0x80)

    # Pad 0s to assert a block length of (message_chunk_size_bits-message_length_padding_bits) bits
    while (
        len(message) * 8 + message_length_padding_bits
    ) % message_chunk_size_bits != 0:
        message.append(0)

    # Pad the last message_length_padding_bits bits that indicate the message length in the specified endian format
    message += (original_message_length_in_bits).to_bytes(
        message_length_padding_bits // 8, byteorder=message_length_byteorder
    )

    return message
