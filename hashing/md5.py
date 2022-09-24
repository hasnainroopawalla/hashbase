from math import floor, sin
from typing import List
from hashing.utils import bytearray_to_binary_string, hex_32_bit_shift_left, binary_string_to_hex, modular_addition, format_int_to_binary_string
from textwrap import wrap


# A = 0x01234567
# B = 0x89ABCDEF
# C = 0xFEDCBA98
# D = 0x76543210

A = 0x67452301
B = 0xEFCDAB89
C = 0x98BADCFE
D = 0x10325476


def text_to_binary_message(text: str) -> str:
    return "".join([format_int_to_binary_string(ord(ch), 8) for ch in text])


def apply_padding(message: bytearray) -> bytearray:
    message_length = len(message)
    
    # Pad a trailing '1'
    message.append(0x80)
    
    # Pad 0s to assert a message length of 448 bits
    message = message.ljust(56, b'\0')
    
    # Pad the last 64 bits that indicate the message length in the little endian format 
    message += (message_length * 8).to_bytes(8, byteorder='little')
    
    return message


def split_message_block(message_block: str, message_bit_count: int = 32) -> List[str]:
    return wrap(message_block, message_bit_count)


def message_to_hex(message_words: List[str]) -> List[int]:
    return [binary_string_to_hex(m) for m in message_words]


def F(x, y, z):
    return (x & y) | (~x & z)

def G(x, y, z):
    return (x & y) | (y & ~z)

def H(x, y, z):
    return x ^ y ^ z

def I(x, y, z):
    return y ^ (x | ~z)


if __name__ == "__main__":
    text = "They are deterministic"
    assert len(text) <= 56  # 448/8
    
    msg_in_bytes = bytearray(text, 'ascii')
    apply_padding(msg_in_bytes)
    
    
    

    # message_block = text_to_binary_message(text)
    # padded_message_block = apply_padding(message_block)

    # message_words = split_message_block(padded_message_block)
    # message_words = [i[::-1] for i in message_words]
    # print(message_words)
    
    # message_words_hex = message_to_hex(message_words)
    
    # k = [int(hex(floor(abs(sin(i))*(pow(2, 32)))), 16) for i in range(1, 65)]
    
    # # print([[m, hex(m), int(hex(m), 16)] for m in message_words_hex])
    
    
    # # ans = F(B, C, D)
    # # print(hex(ans))
    
    # # ans2 = modular_addition(A, ans)
    # # ans3 = modular_addition(message_words_hex[0], ans2)
    
    # # ans4 = modular_addition(k[0], ans3)
    
    # # ans5 = hex_32_bit_shift_left(ans4, 7)
    
    # # ans6 = modular_addition(B, ans5)
    # # print(hex(ans6))
    # # print(bin(message_words_hex[0]), hex(message_words_hex[0]))
    # for i in range(64):
        
    #     # Round 1
    #     if 0 <= i < 16:
    #         p = F(B, C, D)
    #         m_i = i
    #         shift = [7, 12, 17, 22]
    #         # print(hex(p))
            
    #     # Round 2
    #     elif 16 <= i < 32:
    #         p = G(B, C, D)
    #         m_i = ((5 * i) + 1) % 16
    #         shift = [5, 9, 14, 20]
            
    #     # Round 3
    #     elif 32 <= i < 48:
    #         p = H(B, C, D)
    #         m_i = ((3 * i) + 5) % 16
    #         shift = [4, 11, 16, 23]
            
    #     # Round 4
    #     elif 48 <= i < 64:
    #         p = I(B, C, D)
    #         m_i = (7 * i) % 16
    #         shift = [6, 10, 15, 21]
        
    #     print()
    #     print(A, p, k[i], message_words_hex[i])#, int.from_bytes(message_to_hex[4*G : 4*G + 4], byteorder='little'))
        
        
    #     # j = (k[i] + A + p + message_words_hex[m_i]) & 0xffffffff
    #     j = A + p + k[i] + int.from_bytes(bytearray.fromhex(hex(message_words_hex[i])[2:]), byteorder='little')
    #     print(j)
    #     # p = modular_addition(k[i], p)
        
    #     # p = modular_addition(A, p)

    #     # p = modular_addition(message_words_hex[m_i], p)
        
    #     p = hex_32_bit_shift_left(p, shift[i % 4])
        
    #     p = modular_addition(B, p)

    #     A = D
    #     B = p
    #     D = C
    #     C = B
            
    #     # if (i + 1) % 16 == 0 : 
    #     #     print(i, hex(A), hex(B), hex(C), hex(D))  
            
    # # print(hex(A), hex(B), hex(C), hex(D))  
