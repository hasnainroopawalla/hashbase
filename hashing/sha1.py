from math import floor, sin
from typing import List

from hashing.utils import left_shift, modular_add


class SHA1:
    """A cryptographic hashing function used to produce a 128-bit hash.
    https://en.wikipedia.org/wiki/MD5
    """

    def __init__(self) -> None:
        self.h0: int = 0x67452301
        self.h1: int = 0xEFCDAB89
        self.h2: int = 0x98BADCFE
        self.h3: int = 0x10325476
        self.h4: int = 0xC3D2E1F0

    @staticmethod
    def apply_padding(message: bytearray) -> bytearray:
        """Pre-processing for the input message.
        Appends a trailing '1'.
        Pad 0s to the message.
        Append message length to the message.

        Args:
            message (bytearray): The input message in bytes.

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

        # Pad the last 64 bits that indicate the message length in the little endian format
        message += (message_length * 8).to_bytes(8, byteorder="big")

        return message

    @staticmethod
    def break_message_block_into_words(message_block: bytearray) -> List[int]:
        w = [0 for _ in range(80)]
        for i in range(80):
            if 0 <= i < 16:
                w[i] = int.from_bytes(message_block[4 * i : 4 * i + 4], byteorder="big")

            else:
                w[i] = left_shift((w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]), 1)

        return w

    @staticmethod
    def F(x: int, y: int, z: int) -> int:
        return (x & y) | (~x & z)

    @staticmethod
    def G(x: int, y: int, z: int) -> int:
        return x ^ y ^ z

    @staticmethod
    def H(x: int, y: int, z: int) -> int:
        return (x & y) | (x & z) | (y & z)

    def register_values_to_hex_string(self) -> str:
        """Read the values of the 5 registers and convert them to a hexadecimal string.

        Returns:
            str: The hexadecimal string represented by the 5 registers.
        """
        return "%08x%08x%08x%08x%08x" % (self.h0, self.h1, self.h2, self.h3, self.h4)

    def generate_hash(self, message: str) -> str:
        """Generates a 128-bit MD5 hash of the input message.

        Args:
            message (str): The input message/text.

        Returns:
            str: The 128-bit MD5 hash of the message.
        """
        message_in_bytes = bytearray(message, "ascii")
        message_chunk = self.apply_padding(message_in_bytes)

        # Loop through each 64-byte message block
        for block in range(len(message_chunk) // 64):
            w = self.break_message_block_into_words(
                message_chunk[block * 64 : block * 64 + 64]
            )

            a, b, c, d, e = self.h0, self.h1, self.h2, self.h3, self.h4

            # 4 rounds of 16 operations
            for i in range(80):
                # Round 1
                if 0 <= i < 20:
                    f = self.F(b, c, d)
                    k = 0x5A827999

                # Round 2
                elif 20 <= i < 40:
                    f = self.G(b, c, d)
                    k = 0x6ED9EBA1

                # Round 3
                elif 40 <= i < 60:
                    f = self.H(b, c, d)
                    k = 0x8F1BBCDC

                # Round 4
                elif 60 <= i < 80:
                    f = self.G(b, c, d)
                    k = 0xCA62C1D6

                temp = modular_add(left_shift(a, 5), f)
                temp = modular_add(temp, e)
                temp = modular_add(temp, k)
                temp = modular_add(temp, w[i])

                e = d
                d = c
                c = left_shift(b, 30)
                b = a
                a = temp

            self.h0 = modular_add(self.h0, a)
            self.h1 = modular_add(self.h1, b)
            self.h2 = modular_add(self.h2, c)
            self.h3 = modular_add(self.h3, d)
            self.h4 = modular_add(self.h4, e)

        return self.register_values_to_hex_string()


print(SHA1().generate_hash("abc"))
