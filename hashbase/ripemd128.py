from typing import List

from hashbase.utils import rotate_left, modular_add, apply_message_padding


class RIPEMD128:
    """The RIPEMD-128 algorithm is a cryptographic hashing function used to produce a 128-bit hash.
    https://homes.esat.kuleuven.be/~bosselae/ripemd/rmd128.txt
    """

    def __init__(self) -> None:
        self.h0: int = 0x67452301
        self.h1: int = 0xEFCDAB89
        self.h2: int = 0x98BADCFE
        self.h3: int = 0x10325476
        self.K: List[int] = (
            [0x00000000] * 16
            + [0x5A827999] * 16
            + [0x6ED9EBA1] * 16
            + [0x8F1BBCDC] * 16
        )
        self.K_C: List[int] = (
            [0x50A28BE6] * 16
            + [0x5C4DD124] * 16
            + [0x6D703EF3] * 16
            + [0x00000000] * 16
        )
        self.R = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 7, 4, 13, 1, 10, 6, 15, 3, 12, 0, 9, 5, 2, 14, 11, 8, 3, 10, 14, 4, 9, 15, 8, 1, 2, 7, 0, 6, 13, 11, 5, 12, 1, 9, 11, 10, 0, 8, 12, 4, 13, 3, 7, 15, 14, 5, 6, 2]  # type: ignore
        self.R_C = [5, 14, 7, 0, 9, 2, 11, 4, 13, 6, 15, 8, 1, 10, 3, 12, 6, 11, 3, 7, 0, 13, 5, 10, 14, 15, 8, 12, 4, 9, 1, 2, 15, 5, 1, 3, 7, 14, 6, 9, 11, 8, 12, 2, 10, 0, 4, 13, 8, 6, 4, 1, 3, 11, 15, 0, 5, 12, 2, 13, 9, 7, 10, 14]  # type: ignore

        self.SHIFTS = [11, 14, 15, 12, 5, 8, 7, 9, 11, 13, 14, 15, 6, 7, 9, 8, 7, 6, 8, 13, 11, 9, 7, 15, 7, 12, 15, 9, 11, 7, 13, 12, 11, 13, 6, 7, 14, 9, 13, 15, 14, 8, 13, 6, 5, 12, 7, 5, 11, 12, 14, 15, 14, 15, 9, 8, 9, 14, 5, 6, 8, 6, 5, 12]  # type: ignore
        self.SHIFTS_C = [8, 9, 9, 11, 13, 15, 15, 5, 7, 7, 8, 11, 14, 14, 12, 6, 9, 13, 15, 7, 12, 8, 9, 11, 7, 7, 12, 7, 6, 15, 13, 11, 9, 7, 15, 11, 8, 6, 6, 14, 12, 13, 5, 14, 13, 13, 7, 5, 15, 5, 8, 11, 14, 14, 6, 14, 6, 9, 12, 9, 12, 5, 15, 8]  # type: ignore

    @staticmethod
    def split_message_block_into_words(
        message_block: bytearray, word_length_in_bytes: int = 4
    ) -> List[int]:
        """Split the 64-byte message block into 16 4-byte words.

        Args:
            message_block (bytearray): The 512-bytes message block.
            word_length_in_bytes (int, optional): The length of each word in the block. Defaults to 4.

        Returns:
            List[int]: A List of 4-byte words created by splitting the message block.
        """
        return [
            int.from_bytes(
                message_block[4 * i : 4 * i + word_length_in_bytes], byteorder="little"
            )
            for i in range(len(message_block) // word_length_in_bytes)
        ]

    @staticmethod
    def F(j: int, x: int, y: int, z: int) -> int:
        if 0 <= j & j < 16:
            f = x ^ y ^ z
        if 16 <= j & j < 32:
            f = (x & y) | (z & ~x)
        if 32 <= j & j < 48:
            f = (~y | x) ^ z
        if 48 <= j & j < 64:
            f = (x & z) | (y & ~z)
        return f

    def register_values_to_hex_string(self) -> str:
        """Read the values of the 4 registers and convert them to a hexadecimal string.

        Returns:
            str: The hexadecimal string represented by the 4 registers.
        """
        # Create the message digest from the final values of the 4 registers (a, b, c, d)
        digest = sum(
            register_value << (32 * i)
            for i, register_value in enumerate([self.h0, self.h1, self.h2, self.h3])
        )
        # Convert the digest to a hexadecimal string
        return digest.to_bytes(16, byteorder="little").hex()

    def generate_hash(self, message: str) -> str:
        """Generates a 128-bit RIPEMD-128 hash of the input message.

        Args:
            message (str): The input message/text.

        Returns:
            str: The 128-bit RIPEMD-128 hash of the message.
        """
        message_in_bytes = bytearray(message, "ascii")
        message_chunk = apply_message_padding(message_in_bytes, "little")

        # Loop through each 64-byte message block
        for block in range(len(message_chunk) // 64):
            message_words = self.split_message_block_into_words(
                message_chunk[block * 64 : block * 64 + 64]
            )
            a, b, c, d = self.h0, self.h1, self.h2, self.h3
            a_c, b_c, c_c, d_c = self.h0, self.h1, self.h2, self.h3

            for j in range(64):
                w = modular_add(
                    [a, self.F(j, b, c, d), message_words[self.R[j]], self.K[j]]
                )
                t = rotate_left(w, self.SHIFTS[j])
                a, d, c, b = d, c, b, t

                w = modular_add(
                    [
                        a_c,
                        self.F(63 - j, b_c, c_c, d_c),
                        message_words[self.R_C[j]],
                        self.K_C[j],
                    ]
                )
                t = rotate_left(w, self.SHIFTS_C[j])
                a_c, d_c, c_c, b_c = d_c, c_c, b_c, t

            t = modular_add([self.h1, c, d_c])
            self.h1 = modular_add([self.h2, d, a_c])
            self.h2 = modular_add([self.h3, a, b_c])
            self.h3 = modular_add([self.h0, b, c_c])
            self.h0 = t

        return self.register_values_to_hex_string()
