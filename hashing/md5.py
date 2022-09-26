from math import floor, sin
from typing import List

from hashing.utils import left_shift, little_endian_to_hex_string


class MD5:
    def __init__(self) -> None:
        self.A = 0x67452301
        self.B = 0xEFCDAB89
        self.C = 0x98BADCFE
        self.D = 0x10325476
        self.constants = [int(hex(floor(abs(sin(i)) * (pow(2, 32)))), 16) for i in range(1, 65)]
        self.shifts = ([7, 12, 17, 22] * 4) + ([5, 9, 14, 20] * 4) + ([4, 11, 16, 23] * 4) + ([6, 10, 15, 21] * 4)
    
    
    @staticmethod
    def apply_padding(message: bytearray) -> bytearray:
        message_length = len(message)

        # Pad a trailing '1'
        message.append(0x80)

        # Pad 0s to assert a message length of 448 bits (56 bytes)
        message = message.ljust(56, b"\0")

        # Pad the last 64 bits that indicate the message length in the little endian format
        message += (message_length * 8).to_bytes(8, byteorder="little")

        return message
    
    
    @staticmethod
    def split_message_block(
        message_block: bytearray, message_block_length: int = 4
    ) -> List[bytearray]:
        return [
            int.from_bytes(
                message_block[4 * i : 4 * i + message_block_length], byteorder="little"
            )
            for i in range(len(message_block) // message_block_length)
        ]
    
    @staticmethod
    def F(x, y, z):
        return (x & y) | (~x & z)

    @staticmethod
    def G(x, y, z):
        return (x & z) | (y & ~z)

    @staticmethod
    def H(x, y, z):
        return x ^ y ^ z

    @staticmethod
    def I(x, y, z):
        return y ^ (x | ~z)
    
    
    def generate_hash(self, text: str) -> str:
        assert len(text) <= 56  # 448/8

        msg_in_bytes = bytearray(text, "ascii")
        padded_message = self.apply_padding(msg_in_bytes)
        message_words = self.split_message_block(padded_message)
        
        curr_A, curr_B, curr_C, curr_D = self.A, self.B, self.C, self.D

        for i in range(64):
            # Round 1
            if 0 <= i < 16:
                f = self.F(curr_B, curr_C, curr_D)
                g = i

            # Round 2
            elif 16 <= i < 32:
                f = self.G(curr_B, curr_C, curr_D)
                g = ((5 * i) + 1) % 16

            # Round 3
            elif 32 <= i < 48:
                f = self.H(curr_B, curr_C, curr_D)
                g = ((3 * i) + 5) % 16

            # Round 4
            elif 48 <= i < 64:
                f = self.I(curr_B, curr_C, curr_D)
                g = (7 * i) % 16
            
            f = curr_A + f + self.constants[i] + message_words[g]

            # 0xFFFFFFFF masks the variable, leaving only the last 8 bits and ignoring the remaining
            curr_A = curr_D
            curr_D = curr_C
            curr_C = curr_B
            curr_B += left_shift(f, self.shifts[i]) & 0xFFFFFFFF
        
        final_A = (curr_A + self.A) & 0xFFFFFFFF
        final_B = (curr_B + self.B) & 0xFFFFFFFF
        final_C = (curr_C + self.C) & 0xFFFFFFFF
        final_D = (curr_D + self.D) & 0xFFFFFFFF

        digest = sum(
            buffer_content << (32 * i)
            for i, buffer_content in enumerate([final_A, final_B, final_C, final_D])
        )

        return little_endian_to_hex_string(digest)
    
print(MD5().generate_hash("They are deterministic"))