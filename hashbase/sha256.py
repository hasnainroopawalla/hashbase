from typing import List

from hashbase.utils import modular_add, apply_message_padding, rotate_right, shift_right


class SHA256:
    """The SHA-256 algorithm is a cryptographic hashing function used to produce a 256-bit hash.
    https://en.wikipedia.org/wiki/SHA-2
    """

    def __init__(self) -> None:
        self.h0: int = 0x6A09E667
        self.h1: int = 0xBB67AE85
        self.h2: int = 0x3C6EF372
        self.h3: int = 0xA54FF53A
        self.h4: int = 0x510E527F
        self.h5: int = 0x9B05688C
        self.h6: int = 0x1F83D9AB
        self.h7: int = 0x5BE0CD19
        self.K: List[int] = [
            0x428A2F98,
            0x71374491,
            0xB5C0FBCF,
            0xE9B5DBA5,
            0x3956C25B,
            0x59F111F1,
            0x923F82A4,
            0xAB1C5ED5,
            0xD807AA98,
            0x12835B01,
            0x243185BE,
            0x550C7DC3,
            0x72BE5D74,
            0x80DEB1FE,
            0x9BDC06A7,
            0xC19BF174,
            0xE49B69C1,
            0xEFBE4786,
            0x0FC19DC6,
            0x240CA1CC,
            0x2DE92C6F,
            0x4A7484AA,
            0x5CB0A9DC,
            0x76F988DA,
            0x983E5152,
            0xA831C66D,
            0xB00327C8,
            0xBF597FC7,
            0xC6E00BF3,
            0xD5A79147,
            0x06CA6351,
            0x14292967,
            0x27B70A85,
            0x2E1B2138,
            0x4D2C6DFC,
            0x53380D13,
            0x650A7354,
            0x766A0ABB,
            0x81C2C92E,
            0x92722C85,
            0xA2BFE8A1,
            0xA81A664B,
            0xC24B8B70,
            0xC76C51A3,
            0xD192E819,
            0xD6990624,
            0xF40E3585,
            0x106AA070,
            0x19A4C116,
            0x1E376C08,
            0x2748774C,
            0x34B0BCB5,
            0x391C0CB3,
            0x4ED8AA4A,
            0x5B9CCA4F,
            0x682E6FF3,
            0x748F82EE,
            0x78A5636F,
            0x84C87814,
            0x8CC70208,
            0x90BEFFFA,
            0xA4506CEB,
            0xBEF9A3F7,
            0xC67178F2,
        ]

    @staticmethod
    def break_message_block_into_words(message_block: bytearray) -> List[int]:
        """Split and extend the 64-byte message block into 64 4-byte words.

        Args:
            message_block (bytearray): The 512-bytes message block.

        Returns:
            List[int]: A List of 64 4-byte words created by splitting the message block.
        """
        w = list(range(64))
        for i in range(64):
            if 0 <= i < 16:
                w[i] = int.from_bytes(message_block[4 * i : 4 * i + 4], byteorder="big")
            else:
                s0 = (
                    rotate_right(w[i - 15], 7)
                    ^ rotate_right(w[i - 15], 18)
                    ^ shift_right(w[i - 15], 3)
                )
                s1 = (
                    rotate_right(w[i - 2], 17)
                    ^ rotate_right(w[i - 2], 19)
                    ^ shift_right(w[i - 2], 10)
                )
                w[i] = modular_add([w[i - 16], s0, w[i - 7], s1])
        return w

    def register_values_to_hex_string(self) -> str:
        """Read the values of the 8 registers and convert them to a hexadecimal string.

        Returns:
            str: The hexadecimal string represented by the 8 registers.
        """
        return "%08x%08x%08x%08x%08x%08x%08x%08x" % (
            self.h0,
            self.h1,
            self.h2,
            self.h3,
            self.h4,
            self.h5,
            self.h6,
            self.h7,
        )

    def generate_hash(self, message: str) -> str:
        """Generates a 256-bit SHA-256 hash of the input message.

        Args:
            message (str): The input message/text.

        Returns:
            str: The 256-bit SHA-256 hash of the message.
        """
        message_in_bytes = bytearray(message, "ascii")
        message_chunk = apply_message_padding(message_in_bytes, "big")

        # Loop through each 64-byte message block
        for block in range(len(message_chunk) // 64):
            w = self.break_message_block_into_words(
                message_chunk[block * 64 : block * 64 + 64]
            )
            a, b, c, d, e, f, g, h = (
                self.h0,
                self.h1,
                self.h2,
                self.h3,
                self.h4,
                self.h5,
                self.h6,
                self.h7,
            )

            for i in range(64):
                s1 = rotate_right(e, 6) ^ rotate_right(e, 11) ^ rotate_right(e, 25)
                ch = (e & f) ^ (~e & g)
                temp1 = modular_add([h, s1, ch, self.K[i], w[i]])

                s0 = rotate_right(a, 2) ^ rotate_right(a, 13) ^ rotate_right(a, 22)
                maj = (a & b) ^ (a & c) ^ (b & c)
                temp2 = modular_add([s0, maj])

                h = g
                g = f
                f = e
                e = modular_add([d, temp1])
                d = c
                c = b
                b = a
                a = modular_add([temp1, temp2])

            self.h0 = modular_add([self.h0, a])
            self.h1 = modular_add([self.h1, b])
            self.h2 = modular_add([self.h2, c])
            self.h3 = modular_add([self.h3, d])
            self.h4 = modular_add([self.h4, e])
            self.h5 = modular_add([self.h5, f])
            self.h6 = modular_add([self.h6, g])
            self.h7 = modular_add([self.h7, h])

        return self.register_values_to_hex_string()
