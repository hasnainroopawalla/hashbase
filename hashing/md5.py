from typing import List
from utils import format_int_to_binary
from textwrap import wrap


def text_to_binary_message(text: str):
    return ''.join([format_int_to_binary(ord(ch), 8) for ch in text])

def apply_padding(message):
    message_length = len(message)
    
    # Pad a trailing '1'
    message += '1'
    
    # Pad 0s to assert a message length of 448 bits
    message = message.ljust(512 - 64, '0')
    
    # Pad the last 64 bits that indicate the message length
    message += format_int_to_binary(message_length, 64)
    
    return message


def split_message_block(message_block: str, message_bit_count: int = 32) -> List[str]:
    return wrap(message_block, message_bit_count)
    
    
if __name__ == "__main__":
    text =  "They are deterministic"
    assert len(text) <= 56 # 448/8
    
    message_block = text_to_binary_message(text)
    padded_message_block = apply_padding(message_block)
    
    m = split_message_block(padded_message_block)
    print(m, len(m))
    
    # print(hex(int(m[0], 2)))
    
    
    
    
    # num1 = '01010100011010000110010101111001'
    # num2 = '01010101011010000110010101001001'
    # num1_hex = hex(int(num1, 2))
    # num2_hex = hex(int(num2, 2))
    
    # print(num1_hex, num2_hex, hex(0x89abcdef & 0xfedcba98))
    
    