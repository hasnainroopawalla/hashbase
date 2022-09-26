from math import floor, sin
from typing import List

from hashing.utils import left_shift, digest_to_hex_string, modular_add


class MD5:
    def __init__(self) -> None:
        self.A = 0x67452301
        self.B = 0xEFCDAB89
        self.C = 0x98BADCFE
        self.D = 0x10325476
        self.constants = [floor(abs(sin(i) * pow(2, 32))) for i in range(1, 65)]
        self.shifts = ([7, 12, 17, 22] * 4) + ([5, 9, 14, 20] * 4) + ([4, 11, 16, 23] * 4) + ([6, 10, 15, 21] * 4)
    
    
    @staticmethod
    def apply_padding(message: bytearray) -> bytearray:
        message_length = len(message)

        # Pad a trailing '1'
        message.append(0x80)
        
        # Pad 0s to assert a block length of 448 bits (56 bytes)
        while len(message) % 64 != 56:
            message.append(0)

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
    
    
    def generate_hash(self, message: str) -> str:
        message_in_bytes = bytearray(message, "ascii")
        padded_message = self.apply_padding(message_in_bytes)
        
        for block in range(len(padded_message)//64):
            message_words = self.split_message_block(padded_message[block * 64: block * 64 + 64])
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
                
                # f = curr_A + f + self.constants[i] + message_words[g]
                f = modular_add(f, curr_A)
                f = modular_add(f, self.constants[i])
                f = modular_add(f, message_words[g] )

                curr_A = curr_D
                curr_D = curr_C
                curr_C = curr_B
                curr_B += left_shift(f, self.shifts[i])
            
            self.A = modular_add(self.A, curr_A)
            self.B = modular_add(self.B, curr_B)
            self.C = modular_add(self.C, curr_C)
            self.D = modular_add(self.D, curr_D)

        # Create the message digest from the final values of the 4 registers
        digest = sum(
            buffer_content << (32 * i)
            for i, buffer_content in enumerate([self.A, self.B, self.C, self.D])
        )

        return digest_to_hex_string(digest)
    
print(MD5().generate_hash("12345678901234567890123456789012345678901234567890123456789012345678901234567890"))