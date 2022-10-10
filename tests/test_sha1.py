import unittest

from hashbase import SHA1

# Test suite: https://www.di-mgt.com.au/sha_testvectors.html


class TestSHA1Strings(unittest.TestCase):
    def test_sha1_string_input(self):
        self.assertEqual(
            SHA1().generate_hash(""), "da39a3ee5e6b4b0d3255bfef95601890afd80709"
        )
        self.assertEqual(
            SHA1().generate_hash("abc"), "a9993e364706816aba3e25717850c26c9cd0d89d"
        )
        self.assertEqual(
            SHA1().generate_hash(
                "abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq"
            ),
            "84983e441c3bd26ebaae4aa1f95129e5e54670f1",
        )
        self.assertEqual(
            SHA1().generate_hash(
                "abcdefghbcdefghicdefghijdefghijkefghijklfghijklmghijklmnhijklmnoijklmnopjklmnopqklmnopqrlmnopqrsmnopqrstnopqrstu"
            ),
            "a49b2446a02c645bf419f995b67091253a04a259",
        )
