from math import floor, sin
from typing import List
from hashing.utils import hex_32_bit_shift_left, binary_string_to_hex, modular_addition, format_int_to_binary_string
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


def f(b, c, d):
    # F(B, C, D) = (B∧C)∨(¬B∧D)
    ans = (b & c) | (~b & d)
    return ans
    

if __name__ == "__main__":
    text = "They are deterministic"
    assert len(text) <= 56  # 448/8

    message_block = text_to_binary_message(text)
    padded_message_block = apply_padding(message_block)

    message_words = split_message_block(padded_message_block)

    message_words_hex = message_to_hex(message_words)
    
    k = [int(hex(floor(abs(sin(i))*(pow(2, 32)))), 16) for i in range(1, 65)]

    # print([[m, hex(m), int(hex(m), 16)] for m in message_words_hex])
    
    ans = f(B, C, D)
    
    ans2 = modular_addition(A, ans)
    ans3 = modular_addition(message_words_hex[0], ans2)
    
    ans4 = modular_addition(k[0], ans3)
    
    ans5 = hex(hex_32_bit_shift_left(ans4, 7))
    print(ans5)

    
    
