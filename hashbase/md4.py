from typing import List

from hashbase.utils import rotate_left, modular_add, apply_message_padding


class MD4:
    """The MD4 algorithm is a cryptographic hashing function used to produce a 128-bit hash.
    https://en.wikipedia.org/wiki/MD4
    """

    def __init__(self) -> None:
        self.a: int = 0x67452301
        self.b: int = 0xEFCDAB89
        self.c: int = 0x98BADCFE
        self.d: int = 0x10325476
        self.SHIFTS: List[int] = (
            ([3, 7, 11, 19] * 4) + ([3, 5, 9, 13] * 4) + ([3, 9, 11, 15] * 4)
        )

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
    def F(x: int, y: int, z: int) -> int:
        """F(x, y, z) = (x AND y) OR (NOT x AND z)"""
        return (x & y) | (~x & z)

    @staticmethod
    def G(x: int, y: int, z: int) -> int:
        """G(x, y, z) = (x AND y) OR (x AND z) OR (y AND z)"""
        return (x & y) | (x & z) | (y & z)

    @staticmethod
    def H(x: int, y: int, z: int) -> int:
        """H(x, y, z) = x XOR y XOR z"""
        return x ^ y ^ z

    def register_values_to_hex_string(self) -> str:
        """Read the values of the 4 registers and convert them to a hexadecimal string.

        Returns:
            str: The hexadecimal string represented by the 4 registers.
        """
        # Create the message digest from the final values of the 4 registers (a, b, c, d)
        digest = sum(
            register_value << (32 * i)
            for i, register_value in enumerate([self.a, self.b, self.c, self.d])
        )
        # Convert the digest to a hexadecimal string
        return digest.to_bytes(16, byteorder="little").hex()

    def generate_hash(self, message: str) -> str:
        """Generates a 128-bit MD4 hash of the input message.

        Args:
            message (str): The input message/text.

        Returns:
            str: The 128-bit MD4 hash of the message.
        """
        message_in_bytes = bytearray(message, "ascii")
        message_chunk = apply_message_padding(message_in_bytes, "little")

        # Loop through each 64-byte message block
        for block in range(len(message_chunk) // 64):
            message_words = self.split_message_block_into_words(
                message_chunk[block * 64 : block * 64 + 64]
            )
            curr_a, curr_b, curr_c, curr_d = self.a, self.b, self.c, self.d

            # 3 rounds of 16 operations
            for i in range(48):
                # Round 1
                if 0 <= i < 16:
                    f = self.F(curr_b, curr_c, curr_d)
                    k = i

                # Round 2
                elif 16 <= i < 32:
                    f = self.G(curr_b, curr_c, curr_d) + 0x5A827999
                    k = 4 * (i % 4) + (i % 16) // 4

                # Round 3
                elif 32 <= i < 48:
                    f = self.H(curr_b, curr_c, curr_d) + 0x6ED9EBA1
                    k = (
                        8 * ((i - 32) % 2)
                        + ((i - 32) // 2)
                        - 3 * ((i - 32) // 8)
                        + 3 * (((i - 32) // 2) % 2)
                    )

                f = modular_add([f, curr_a, message_words[k]])

                curr_a = curr_d
                curr_d = curr_c
                curr_c = curr_b
                curr_b = rotate_left(f, self.SHIFTS[i])

            self.a = modular_add([self.a, curr_a])
            self.b = modular_add([self.b, curr_b])
            self.c = modular_add([self.c, curr_c])
            self.d = modular_add([self.d, curr_d])

        return self.register_values_to_hex_string()
