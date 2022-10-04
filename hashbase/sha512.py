from typing import List

from hashbase.utils import modular_add, apply_message_padding, rotate_right, shift_right


class SHA512:
    """The SHA-512 algorithm is a cryptographic hashing function used to produce a 512-bit hash.
    https://en.wikipedia.org/wiki/SHA-2
    """

    def __init__(self) -> None:
        self.h0: int = 0x6a09e667f3bcc908
        self.h1: int = 0xbb67ae8584caa73b
        self.h2: int = 0x3c6ef372fe94f82b
        self.h3: int = 0xa54ff53a5f1d36f1
        self.h4: int = 0x510e527fade682d1
        self.h5: int = 0x9b05688c2b3e6c1f
        self.h6: int = 0x1f83d9abfb41bd6b
        self.h7: int = 0x5be0cd19137e2179
        self.K: List[int] = [
            0x428a2f98d728ae22, 0x7137449123ef65cd, 0xb5c0fbcfec4d3b2f, 0xe9b5dba58189dbbc, 0x3956c25bf348b538, 
            0x59f111f1b605d019, 0x923f82a4af194f9b, 0xab1c5ed5da6d8118, 0xd807aa98a3030242, 0x12835b0145706fbe, 
            0x243185be4ee4b28c, 0x550c7dc3d5ffb4e2, 0x72be5d74f27b896f, 0x80deb1fe3b1696b1, 0x9bdc06a725c71235, 
            0xc19bf174cf692694, 0xe49b69c19ef14ad2, 0xefbe4786384f25e3, 0x0fc19dc68b8cd5b5, 0x240ca1cc77ac9c65, 
            0x2de92c6f592b0275, 0x4a7484aa6ea6e483, 0x5cb0a9dcbd41fbd4, 0x76f988da831153b5, 0x983e5152ee66dfab, 
            0xa831c66d2db43210, 0xb00327c898fb213f, 0xbf597fc7beef0ee4, 0xc6e00bf33da88fc2, 0xd5a79147930aa725, 
            0x06ca6351e003826f, 0x142929670a0e6e70, 0x27b70a8546d22ffc, 0x2e1b21385c26c926, 0x4d2c6dfc5ac42aed, 
            0x53380d139d95b3df, 0x650a73548baf63de, 0x766a0abb3c77b2a8, 0x81c2c92e47edaee6, 0x92722c851482353b, 
            0xa2bfe8a14cf10364, 0xa81a664bbc423001, 0xc24b8b70d0f89791, 0xc76c51a30654be30, 0xd192e819d6ef5218, 
            0xd69906245565a910, 0xf40e35855771202a, 0x106aa07032bbd1b8, 0x19a4c116b8d2d0c8, 0x1e376c085141ab53, 
            0x2748774cdf8eeb99, 0x34b0bcb5e19b48a8, 0x391c0cb3c5c95a63, 0x4ed8aa4ae3418acb, 0x5b9cca4f7763e373, 
            0x682e6ff3d6b2b8a3, 0x748f82ee5defb2fc, 0x78a5636f43172f60, 0x84c87814a1f0ab72, 0x8cc702081a6439ec, 
            0x90befffa23631e28, 0xa4506cebde82bde9, 0xbef9a3f7b2c67915, 0xc67178f2e372532b, 0xca273eceea26619c, 
            0xd186b8c721c0c207, 0xeada7dd6cde0eb1e, 0xf57d4f7fee6ed178, 0x06f067aa72176fba, 0x0a637dc5a2c898a6, 
            0x113f9804bef90dae, 0x1b710b35131c471b, 0x28db77f523047d84, 0x32caab7b40c72493, 0x3c9ebe0a15c9bebc, 
            0x431d67c49c100d4c, 0x4cc5d4becb3e42b6, 0x597f299cfc657e2a, 0x5fcb6fab3ad6faec, 0x6c44198c4a475817
        ]

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
        """Generates a 512-bit SHA-512 hash of the input message.

        Args:
            message (str): The input message/text.

        Returns:
            str: The 512-bit SHA-512 hash of the message.
        """
        message_in_bytes = bytearray(message, "ascii")
        message_chunk = apply_message_padding(message_in_bytes, message_length_byteorder="big", message_length_padding_bits=128, message_chunk_size_bits=1024)
        # Loop through each 64-byte message block
        for block in range(len(message_chunk) // 128):
            w = self.break_message_block_into_words(
                message_chunk[block * 128 : block * 128 + 128]
            )
            # print(w)
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
                s1 = rotate_right(e, s=14, size=64) ^ rotate_right(e, s=18, size=64) ^ rotate_right(e, s=41, size=64)
                ch = (e & f) ^ (~e & g)
                temp1 = modular_add([h, s1, ch, self.K[i], w[i]], size=64)

                s0 = rotate_right(a, s=28, size=64) ^ rotate_right(a, s=34, size=64) ^ rotate_right(a, s=39, size=64)
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


print(SHA512().generate_hash(''))

# cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e
# cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e