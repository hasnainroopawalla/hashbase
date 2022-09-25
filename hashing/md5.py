from math import floor, sin
from typing import List
from hashing.utils import (
    bytearray_to_binary_string,
    binary_string_to_hex,
    left_shift,
    modular_addition,
    format_int_to_binary_string,
)
from textwrap import wrap


# A = 0x01234567
# B = 0x89ABCDEF
# C = 0xFEDCBA98
# D = 0x76543210

A, initial_A = 0x67452301, 0x67452301
B, initial_B = 0xEFCDAB89, 0xEFCDAB89
C, initial_C = 0x98BADCFE, 0x98BADCFE
D, initial_D = 0x10325476, 0x10325476


def text_to_binary_message(text: str) -> str:
    return "".join([format_int_to_binary_string(ord(ch), 8) for ch in text])


def apply_padding(message: bytearray) -> bytearray:
    message_length = len(message)

    # Pad a trailing '1'
    message.append(0x80)

    # Pad 0s to assert a message length of 448 bits (56 bytes)
    message = message.ljust(56, b"\0")

    # Pad the last 64 bits that indicate the message length in the little endian format
    message += (message_length * 8).to_bytes(8, byteorder="little")

    return message


def split_message_block(
    message_block: bytearray, message_block_length: int = 4
) -> List[bytearray]:
    return [
        int.from_bytes(
            message_block[4 * i : 4 * i + message_block_length], byteorder="little"
        )
        for i in range(len(message_block) // message_block_length)
    ]


def message_to_hex(message_words: List[str]) -> List[int]:
    return [binary_string_to_hex(m) for m in message_words]


def F(x, y, z):
    return (x & y) | (~x & z)


def G(x, y, z):
    return (x & z) | (y & ~z)


def H(x, y, z):
    return x ^ y ^ z


def I(x, y, z):
    return y ^ (x | ~z)


if __name__ == "__main__":
    text = "They are deterministic"
    assert len(text) <= 56  # 448/8

    msg_in_bytes = bytearray(text, "ascii")
    padded_message = apply_padding(msg_in_bytes)

    # message_words = int.from_bytes(block[4*G : 4*G + 4], byteorder='little')

    message_words = split_message_block(padded_message)
    # print(len(message_words))
    # message_words = [i[::-1] for i in message_words]
    # print(message_words)

    # message_words_hex = message_to_hex(message_words)

    k = [int(hex(floor(abs(sin(i)) * (pow(2, 32)))), 16) for i in range(1, 65)]

    # # ans = F(B, C, D)
    # # print(hex(ans))

    # # ans2 = modular_addition(A, ans)
    # # ans3 = modular_addition(message_words_hex[0], ans2)

    # # ans4 = modular_addition(k[0], ans3)

    # # ans5 = hex_32_bit_shift_left(ans4, 7)

    # # ans6 = modular_addition(B, ans5)
    # # print(hex(ans6))
    # # print(bin(message_words_hex[0]), hex(message_words_hex[0]))
    for i in range(64):
        # Round 1
        if 0 <= i < 16:
            p = F(B, C, D)
            m_i = i
            shift = [7, 12, 17, 22]

        # Round 2
        elif 16 <= i < 32:
            p = G(B, C, D)
            m_i = ((5 * i) + 1) % 16
            shift = [5, 9, 14, 20]

        # Round 3
        elif 32 <= i < 48:
            p = H(B, C, D)
            m_i = ((3 * i) + 5) % 16
            shift = [4, 11, 16, 23]

        # Round 4
        elif 48 <= i < 64:
            p = I(B, C, D)
            m_i = (7 * i) % 16
            shift = [6, 10, 15, 21]

        # print()
        # print(A, p, k[i], message_words_hex[i])#, int.from_bytes(message_to_hex[4*G : 4*G + 4], byteorder='little'))

        # j = (k[i] + A + p + message_words_hex[m_i]) & 0xffffffff
        j = A + p + k[i] + message_words[m_i]
        # print(A ,p ,k[i] ,message_words[m_i])
        # print(f'j: {j}, shift {shift[i % 4]}')
        # p = modular_addition(k[i], p)

        # p = modular_addition(A, p)

        # p = modular_addition(message_words_hex[m_i], p)
        print()
        after_shift = B + left_shift(j, shift[i % 4])

        # 0xFFFFFFFF masks the variable, leaving only the last 8 bits and ignoring the remaining
        final_new_b = after_shift & 0xFFFFFFFF
        # p = modular_addition(B, p)

        A, B, C, D = D, final_new_b, B, C

        # if (i + 1) % 16 == 0 :
        #     print(i, hex(A), hex(B), hex(C), hex(D))

    final_A = (A + initial_A) & 0xFFFFFFFF
    final_B = (B + initial_B) & 0xFFFFFFFF
    final_C = (C + initial_C) & 0xFFFFFFFF
    final_D = (D + initial_D) & 0xFFFFFFFF

    # print(final_A, final_B, final_C, final_D)
    # print('LAST', final_A << (32*0))
    # print('LAST', final_B << (32*1))
    # print('LAST', final_C << (32*2))
    # print('LAST', final_D << (32*3))

    digest = sum(
        buffer_content << (32 * i)
        for i, buffer_content in enumerate([final_A, final_B, final_C, final_D])
    )

    raw = digest.to_bytes(16, byteorder="little").hex()
    print(raw)
    # print('{:032x}'.format(int.from_bytes(raw, byteorder='big')))
