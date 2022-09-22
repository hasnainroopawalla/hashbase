from typing import List
from hashing.utils import binary_string_to_hex
from utils import format_int_to_binary_string
from textwrap import wrap


A = 0x01234567
B = 0x89ABCDEF
C = 0xFEDCBA98
D = 0x76543210


def text_to_binary_message(text: str) -> str:
    return "".join([format_int_to_binary_string(ord(ch), 8) for ch in text])


def apply_padding(message: str) -> str:
    message_length = len(message)

    # Pad a trailing '1'
    message += "1"

    # Pad 0s to assert a message length of 448 bits
    message = message.ljust(512 - 64, "0")

    # Pad the last 64 bits that indicate the message length
    message += format_int_to_binary_string(message_length, 64)

    return message


def split_message_block(message_block: str, message_bit_count: int = 32) -> List[str]:
    return wrap(message_block, message_bit_count)


def message_to_hex(message_words: List[str]) -> List[int]:
    return [binary_string_to_hex(m) for m in message_words]


if __name__ == "__main__":
    text = "They are deterministic"
    assert len(text) <= 56  # 448/8

    message_block = text_to_binary_message(text)
    padded_message_block = apply_padding(message_block)

    message_words = split_message_block(padded_message_block)

    message_words_hex = message_to_hex(message_words)

    print([[m, hex(m), int(hex(m), 16)] for m in message_words_hex])
