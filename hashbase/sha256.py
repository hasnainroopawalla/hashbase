from typing import List

from hashbase.utils import rotate_left, modular_add, pad_message, rotate_right, shift_right


class SHA256:
    """The SHA-1 algorithm is a cryptographic hashing function used to produce a 160-bit hash.
    https://en.wikipedia.org/wiki/SHA-1
    """

    def __init__(self) -> None:
        self.h0: int = 0x6a09e667
        self.h1: int = 0xbb67ae85
        self.h2: int = 0x3c6ef372
        self.h3: int = 0xa54ff53a
        self.h4: int = 0x510e527f
        self.h5: int = 0x9b05688c
        self.h6: int = 0x1f83d9ab
        self.h7: int = 0x5be0cd19
        self.k: List[int] = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
                            0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
                            0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
                            0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
                            0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
                            0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
                            0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
                            0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]

    @staticmethod
    def break_message_block_into_words(message_block: bytearray) -> List[int]:
        """Split and extend the 64-byte message block into 80 4-byte words.

        Args:
            message_block (bytearray): The 512-bytes message block.

        Returns:
            List[int]: A List of 80 4-byte words created by splitting the message block.
        """
        w = list(range(64))
        for i in range(64):
            if 0 <= i < 16:
                w[i] = int.from_bytes(message_block[4 * i : 4 * i + 4], byteorder="big")
            else:
                s0 = rotate_right(w[i - 15], 7) ^ rotate_right(w[i - 15], 18) ^ shift_right(w[i - 15], 3)
                s1 = rotate_right(w[i - 2], 17) ^ rotate_right(w[i - 2], 19) ^ shift_right(w[i - 2], 10)
                w[i] = (w[i - 16] + s0 + w[i - 7] + s1) % 2**32
        return w

    def register_values_to_hex_string(self) -> str:
        """Read the values of the 5 registers and convert them to a hexadecimal string.

        Returns:
            str: The hexadecimal string represented by the 5 registers.
        """
        return "%08x%08x%08x%08x%08x%08x%08x%08x" % (self.h0, self.h1, self.h2, self.h3, self.h4, self.h5, self.h6, self.h7)

    def generate_hash(self, message: str) -> str:
        """Generates a 160-bit SHA-1 hash of the input message.

        Args:
            message (str): The input message/text.

        Returns:
            str: The 160-bit SHA-1 hash of the message.
        """
        message_in_bytes = bytearray(message, "ascii")
        message_chunk = pad_message(message_in_bytes, "big")

        # Loop through each 64-byte message block
        for block in range(len(message_chunk) // 64):
            w = self.break_message_block_into_words(
                message_chunk[block * 64 : block * 64 + 64]
            )
            a, b, c, d, e, f, g, h = self.h0, self.h1, self.h2, self.h3, self.h4, self.h5, self.h6, self.h7

            for i in range(64):
                s1 = rotate_right(e, 6) ^ rotate_right(e, 11) ^ rotate_right(e, 25) 
                ch = (e & f) ^ (~e & g)
                temp1 = (h + s1 + ch + self.k[i] + w[i]) % 2**32
                
                s0 = rotate_right(a, 2) ^ rotate_right(a, 13) ^ rotate_right(a, 22)
                maj = (a & b) ^ (a & c) ^ (b & c)
                temp2 = (s0 + maj) % 2**32
                
                h = g
                g = f
                f = e
                e = (d + temp1) % 2**32
                d = c
                c = b
                b = a
                a = (temp1 + temp2) % 2**32
            
            self.h0 = modular_add(self.h0, a)
            self.h1 = modular_add(self.h1, b)
            self.h2 = modular_add(self.h2, c)
            self.h3 = modular_add(self.h3, d)
            self.h4 = modular_add(self.h4, e)
            self.h5 = modular_add(self.h5, f)
            self.h6 = modular_add(self.h6, g)
            self.h7 = modular_add(self.h7, h)

        return self.register_values_to_hex_string()


print(SHA256().generate_hash(""))