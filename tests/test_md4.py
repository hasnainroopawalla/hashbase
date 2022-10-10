import unittest

from hashbase import MD4

# Test suite obtained from the original RFC publication: https://www.rfc-editor.org/rfc/rfc1319


class TestMD2Strings(unittest.TestCase):
    def test_md2_string_input(self):
        self.assertEqual(MD4().generate_hash(""), "31d6cfe0d16ae931b73c59d7e0c089c0")
        self.assertEqual(MD4().generate_hash("a"), "bde52cb31de33e46245e05fbdbd6fb24")
        self.assertEqual(MD4().generate_hash("abc"), "a448017aaf21d8525fc10ae87aa6729d")
        self.assertEqual(
            MD4().generate_hash("message digest"), "d9130a8164549fe818874806e1c7014b"
        )
        self.assertEqual(
            MD4().generate_hash("abcdefghijklmnopqrstuvwxyz"),
            "d79e1c308aa5bbcdeea8ed63df412da9",
        )
        self.assertEqual(
            MD4().generate_hash(
                "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
            ),
            "043f8582f241db351ce627e153e7f0e4",
        )
        self.assertEqual(
            MD4().generate_hash(
                "12345678901234567890123456789012345678901234567890123456789012345678901234567890"
            ),
            "e33b4ddc9c38f2199c3e7b164fcc0536",
        )
