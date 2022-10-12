import unittest

from hashbase import RIPEMD128


class TestRIPEMD128Strings(unittest.TestCase):
    def test_RIPEMD128_string_input(self):
        self.assertEqual(
            RIPEMD128().generate_hash(""), "cdf26213a150dc3ecb610f18f6b38b46"
        )
        self.assertEqual(
            RIPEMD128().generate_hash("a"), "86be7afa339d0fc7cfc785e72f578d33"
        )
        self.assertEqual(
            RIPEMD128().generate_hash("abc"), "c14a12199c66e4ba84636b0f69144c77"
        )
        self.assertEqual(
            RIPEMD128().generate_hash("message digest"),
            "9e327b3d6e523062afc1132d7df9d1b8",
        )
        self.assertEqual(
            RIPEMD128().generate_hash("abcdefghijklmnopqrstuvwxyz"),
            "fd2aa607f71dc8f510714922b371834e",
        )
        self.assertEqual(
            RIPEMD128().generate_hash(
                "abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq"
            ),
            "a1aa0689d0fafa2ddc22e88b49133a06",
        )
        self.assertEqual(
            RIPEMD128().generate_hash(
                "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
            ),
            "d1e959eb179c911faea4624c60c5c702",
        )
