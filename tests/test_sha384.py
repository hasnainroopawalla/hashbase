import unittest

from hashbase import SHA384


class TestSHA1Strings(unittest.TestCase):
    def test_sha1_string_input(self):
        self.assertEqual(
            SHA384().generate_hash(""),
            "38b060a751ac96384cd9327eb1b1e36a21fdb71114be07434c0cc7bf63f6e1da274edebfe76f65fbd51ad2f14898b95b",
        )
        self.assertEqual(
            SHA384().generate_hash("abc"),
            "cb00753f45a35e8bb5a03d699ac65007272c32ab0eded1631a8b605a43ff5bed8086072ba1e7cc2358baeca134c825a7",
        )
        self.assertEqual(
            SHA384().generate_hash(
                "abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq"
            ),
            "3391fdddfc8dc7393707a65b1b4709397cf8b1d162af05abfe8f450de5f36bc6b0455a8520bc4e6f5fe95b1fe3c8452b",
        )
        self.assertEqual(
            SHA384().generate_hash(
                "abcdefghbcdefghicdefghijdefghijkefghijklfghijklmghijklmnhijklmnoijklmnopjklmnopqklmnopqrlmnopqrsmnopqrstnopqrstu"
            ),
            "09330c33f71147e83d192fc782cd1b4753111b173b3b05d22fa08086e3b0f712fcc7c71a557e2db966c3e9fa91746039",
        )
        self.assertEqual(
            SHA384().generate_hash(
                "12345678901234567890123456789012345678901234567890123456789012345678901234567890"
            ),
            "b12932b0627d1c060942f5447764155655bd4da0c9afa6dd9b9ef53129af1b8fb0195996d2de9ca0df9d821ffee67026",
        )
