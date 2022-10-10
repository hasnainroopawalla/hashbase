import unittest

from hashbase import MD2

# Test suite obtained from the original RFC publication: https://www.rfc-editor.org/rfc/rfc1319


class TestMD2Strings(unittest.TestCase):
    def test_md2_string_input(self):
        self.assertEqual(MD2().generate_hash(""), "8350e5a3e24c153df2275c9f80692773")
        self.assertEqual(MD2().generate_hash("a"), "32ec01ec4a6dac72c0ab96fb34c0b5d1")
        self.assertEqual(MD2().generate_hash("abc"), "da853b0d3f88d99b30283a69e6ded6bb")
        self.assertEqual(
            MD2().generate_hash("message digest"), "ab4f496bfb2a530b219ff33031fe06b0"
        )
        self.assertEqual(
            MD2().generate_hash("abcdefghijklmnopqrstuvwxyz"),
            "4e8ddff3650292ab5a4108c3aa47940b",
        )
        self.assertEqual(
            MD2().generate_hash(
                "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
            ),
            "da33def2a42df13975352846c30338cd",
        )
        self.assertEqual(
            MD2().generate_hash(
                "12345678901234567890123456789012345678901234567890123456789012345678901234567890"
            ),
            "d5976f79d83d3a0dc9806c3c66f3efd8",
        )
