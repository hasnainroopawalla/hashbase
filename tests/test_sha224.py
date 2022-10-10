import unittest

from hashbase import SHA224


class TestSHA1Strings(unittest.TestCase):
    def test_sha1_string_input(self):
        self.assertEqual(
            SHA224().generate_hash(""),
            "d14a028c2a3a2bc9476102bb288234c415a2b01f828ea62ac5b3e42f",
        )
        self.assertEqual(
            SHA224().generate_hash("abc"),
            "23097d223405d8228642a477bda255b32aadbce4bda0b3f7e36c9da7",
        )
        self.assertEqual(
            SHA224().generate_hash(
                "abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq"
            ),
            "75388b16512776cc5dba5da1fd890150b0c6455cb4f58b1952522525",
        )
        self.assertEqual(
            SHA224().generate_hash(
                "abcdefghbcdefghicdefghijdefghijkefghijklfghijklmghijklmnhijklmnoijklmnopjklmnopqklmnopqrlmnopqrsmnopqrstnopqrstu"
            ),
            "c97ca9a559850ce97a04a96def6d99a9e0e0e2ab14e6b8df265fc0b3",
        )
        self.assertEqual(
            SHA224().generate_hash(
                "12345678901234567890123456789012345678901234567890123456789012345678901234567890"
            ),
            "b50aecbe4e9bb0b57bc5f3ae760a8e01db24f203fb3cdcd13148046e",
        )
