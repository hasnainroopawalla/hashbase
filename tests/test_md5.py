import unittest

from hashbase import MD5

# Test suite obtained from the original RFC publication: https://datatracker.ietf.org/doc/html/rfc1321


class TestMD5Strings(unittest.TestCase):
    def test_md5_string_input(self):
        self.assertEqual(MD5().generate_hash(""), "d41d8cd98f00b204e9800998ecf8427e")
        self.assertEqual(MD5().generate_hash("a"), "0cc175b9c0f1b6a831c399e269772661")
        self.assertEqual(MD5().generate_hash("abc"), "900150983cd24fb0d6963f7d28e17f72")
        self.assertEqual(
            MD5().generate_hash("message digest"), "f96b697d7cb7938d525a2f31aaf161d0"
        )
        self.assertEqual(
            MD5().generate_hash("abcdefghijklmnopqrstuvwxyz"),
            "c3fcd3d76192e4007dfb496cca67e13b",
        )
        self.assertEqual(
            MD5().generate_hash(
                "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
            ),
            "d174ab98d277d9f5a5611c2c9f419d9f",
        )
        self.assertEqual(
            MD5().generate_hash(
                "12345678901234567890123456789012345678901234567890123456789012345678901234567890"
            ),
            "57edf4a22be3c955ac49da2e2107b67a",
        )
