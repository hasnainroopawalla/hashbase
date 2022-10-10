from typing import List

from hashbase.utils import modular_add, apply_message_padding, rotate_right, shift_right


class SHA512:
    """The SHA-512 algorithm is a cryptographic hashing function used to produce a 512-bit hash.
    https://en.wikipedia.org/wiki/SHA-2
    """

    def __init__(self, output_bits=512) -> None:
        self.h0: int = 0x6A09E667F3BCC908
        self.h1: int = 0xBB67AE8584CAA73B
        self.h2: int = 0x3C6EF372FE94F82B
        self.h3: int = 0xA54FF53A5F1D36F1
        self.h4: int = 0x510E527FADE682D1
        self.h5: int = 0x9B05688C2B3E6C1F
        self.h6: int = 0x1F83D9ABFB41BD6B
        self.h7: int = 0x5BE0CD19137E2179
        self.K: List[int] = [
            0x428A2F98D728AE22,
            0x7137449123EF65CD,
            0xB5C0FBCFEC4D3B2F,
            0xE9B5DBA58189DBBC,
            0x3956C25BF348B538,
            0x59F111F1B605D019,
            0x923F82A4AF194F9B,
            0xAB1C5ED5DA6D8118,
            0xD807AA98A3030242,
            0x12835B0145706FBE,
            0x243185BE4EE4B28C,
            0x550C7DC3D5FFB4E2,
            0x72BE5D74F27B896F,
            0x80DEB1FE3B1696B1,
            0x9BDC06A725C71235,
            0xC19BF174CF692694,
            0xE49B69C19EF14AD2,
            0xEFBE4786384F25E3,
            0x0FC19DC68B8CD5B5,
            0x240CA1CC77AC9C65,
            0x2DE92C6F592B0275,
            0x4A7484AA6EA6E483,
            0x5CB0A9DCBD41FBD4,
            0x76F988DA831153B5,
            0x983E5152EE66DFAB,
            0xA831C66D2DB43210,
            0xB00327C898FB213F,
            0xBF597FC7BEEF0EE4,
            0xC6E00BF33DA88FC2,
            0xD5A79147930AA725,
            0x06CA6351E003826F,
            0x142929670A0E6E70,
            0x27B70A8546D22FFC,
            0x2E1B21385C26C926,
            0x4D2C6DFC5AC42AED,
            0x53380D139D95B3DF,
            0x650A73548BAF63DE,
            0x766A0ABB3C77B2A8,
            0x81C2C92E47EDAEE6,
            0x92722C851482353B,
            0xA2BFE8A14CF10364,
            0xA81A664BBC423001,
            0xC24B8B70D0F89791,
            0xC76C51A30654BE30,
            0xD192E819D6EF5218,
            0xD69906245565A910,
            0xF40E35855771202A,
            0x106AA07032BBD1B8,
            0x19A4C116B8D2D0C8,
            0x1E376C085141AB53,
            0x2748774CDF8EEB99,
            0x34B0BCB5E19B48A8,
            0x391C0CB3C5C95A63,
            0x4ED8AA4AE3418ACB,
            0x5B9CCA4F7763E373,
            0x682E6FF3D6B2B8A3,
            0x748F82EE5DEFB2FC,
            0x78A5636F43172F60,
            0x84C87814A1F0AB72,
            0x8CC702081A6439EC,
            0x90BEFFFA23631E28,
            0xA4506CEBDE82BDE9,
            0xBEF9A3F7B2C67915,
            0xC67178F2E372532B,
            0xCA273ECEEA26619C,
            0xD186B8C721C0C207,
            0xEADA7DD6CDE0EB1E,
            0xF57D4F7FEE6ED178,
            0x06F067AA72176FBA,
            0x0A637DC5A2C898A6,
            0x113F9804BEF90DAE,
            0x1B710B35131C471B,
            0x28DB77F523047D84,
            0x32CAAB7B40C72493,
            0x3C9EBE0A15C9BEBC,
            0x431D67C49C100D4C,
            0x4CC5D4BECB3E42B6,
            0x597F299CFC657E2A,
            0x5FCB6FAB3AD6FAEC,
            0x6C44198C4A475817,
        ]
        self.output_bits = output_bits

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
                w[i] = int.from_bytes(message_block[8 * i : 8 * i + 8], byteorder="big")
            else:
                s0 = (
                    rotate_right(w[i - 15], s=1, size=64)
                    ^ rotate_right(w[i - 15], s=8, size=64)
                    ^ shift_right(w[i - 15], s=7, size=64)
                )
                s1 = (
                    rotate_right(w[i - 2], s=19, size=64)
                    ^ rotate_right(w[i - 2], s=61, size=64)
                    ^ shift_right(w[i - 2], s=6, size=64)
                )
                w[i] = modular_add([w[i - 16], s0, w[i - 7], s1], size=64)
        return w

    def register_values_to_hex_string(self) -> str:
        """Read the values of the 8 registers and convert them to a hexadecimal string.

        Returns:
            str: The hexadecimal string represented by the 8 registers.
        """
        digest = "%016x%016x%016x%016x%016x%016x%016x%016x" % (
            self.h0,
            self.h1,
            self.h2,
            self.h3,
            self.h4,
            self.h5,
            self.h6,
            self.h7,
        )
        return digest[: self.output_bits // 4]

    def generate_hash(self, message: str) -> str:
        """Generates a 512-bit SHA-512 hash of the input message.

        Args:
            message (str): The input message/text.

        Returns:
            str: The 512-bit SHA-512 hash of the message.
        """
        message_in_bytes = bytearray(message, "ascii")
        message_chunk = apply_message_padding(
            message_in_bytes,
            message_length_byteorder="big",
            message_length_padding_bits=128,
            message_chunk_size_bits=1024,
        )

        # Loop through each 64-byte message block
        for block in range(len(message_chunk) // 128):
            w = self.break_message_block_into_words(
                message_chunk[block * 128 : block * 128 + 128]
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

            for i in range(80):
                s1 = (
                    rotate_right(e, s=14, size=64)
                    ^ rotate_right(e, s=18, size=64)
                    ^ rotate_right(e, s=41, size=64)
                )
                ch = (e & f) ^ (~e & g)
                temp1 = modular_add([h, s1, ch, self.K[i], w[i]], size=64)

                s0 = (
                    rotate_right(a, s=28, size=64)
                    ^ rotate_right(a, s=34, size=64)
                    ^ rotate_right(a, s=39, size=64)
                )
                maj = (a & b) ^ (a & c) ^ (b & c)
                temp2 = modular_add([s0, maj], size=64)

                h = g
                g = f
                f = e
                e = modular_add([d, temp1], size=64)
                d = c
                c = b
                b = a
                a = modular_add([temp1, temp2], size=64)

            self.h0 = modular_add([self.h0, a], size=64)
            self.h1 = modular_add([self.h1, b], size=64)
            self.h2 = modular_add([self.h2, c], size=64)
            self.h3 = modular_add([self.h3, d], size=64)
            self.h4 = modular_add([self.h4, e], size=64)
            self.h5 = modular_add([self.h5, f], size=64)
            self.h6 = modular_add([self.h6, g], size=64)
            self.h7 = modular_add([self.h7, h], size=64)

        return self.register_values_to_hex_string()
