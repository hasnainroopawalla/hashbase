from typing import List

from hashbase.utils import rotate_left, modular_add, apply_message_padding


class SHA1:
    """The SHA-1 algorithm is a cryptographic hashing function used to produce a 160-bit hash.
    https://en.wikipedia.org/wiki/SHA-1
    """

    def __init__(self) -> None:
        self.h0: int = 0x67452301
        self.h1: int = 0xEFCDAB89
        self.h2: int = 0x98BADCFE
        self.h3: int = 0x10325476
        self.h4: int = 0xC3D2E1F0

    @staticmethod
    def break_message_block_into_words(message_block: bytearray) -> List[int]:
        """Split and extend the 64-byte message block into 80 4-byte words.

        Args:
            message_block (bytearray): The 512-bytes message block.

        Returns:
            List[int]: A List of 80 4-byte words created by splitting the message block.
        """
        w = list(range(80))
        for i in range(80):
            if 0 <= i < 16:
                w[i] = int.from_bytes(message_block[4 * i : 4 * i + 4], byteorder="big")
            else:
                w[i] = rotate_left((w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]), 1)
        return w

    def register_values_to_hex_string(self) -> str:
        """Read the values of the 5 registers and convert them to a hexadecimal string.

        Returns:
            str: The hexadecimal string represented by the 5 registers.
        """
        return "%08x%08x%08x%08x%08x" % (self.h0, self.h1, self.h2, self.h3, self.h4)

    def generate_hash(self, message: str) -> str:
        """Generates a 160-bit SHA-1 hash of the input message.

        Args:
            message (str): The input message/text.

        Returns:
            str: The 160-bit SHA-1 hash of the message.
        """
        message_in_bytes = bytearray(message, "ascii")
        message_chunk = apply_message_padding(message_in_bytes, "big")

        # Loop through each 64-byte message block
        for block in range(len(message_chunk) // 64):
            w = self.break_message_block_into_words(
                message_chunk[block * 64 : block * 64 + 64]
            )

            a, b, c, d, e = self.h0, self.h1, self.h2, self.h3, self.h4

            for i in range(80):
                if 0 <= i < 20:
                    f = (b & c) | (~b & d)
                    k = 0x5A827999

                elif 20 <= i < 40:
                    f = b ^ c ^ d
                    k = 0x6ED9EBA1

                elif 40 <= i < 60:
                    f = (b & c) | (b & d) | (c & d)
                    k = 0x8F1BBCDC

                elif 60 <= i < 80:
                    f = b ^ c ^ d
                    k = 0xCA62C1D6

                temp = modular_add([rotate_left(a, 5), f, e, k, w[i]])

                e = d
                d = c
                c = rotate_left(b, 30)
                b = a
                a = temp

            self.h0 = modular_add([self.h0, a])
            self.h1 = modular_add([self.h1, b])
            self.h2 = modular_add([self.h2, c])
            self.h3 = modular_add([self.h3, d])
            self.h4 = modular_add([self.h4, e])

        return self.register_values_to_hex_string()
