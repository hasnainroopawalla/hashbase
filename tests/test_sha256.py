import unittest

from hashbase import SHA256


class TestSHA1Strings(unittest.TestCase):
    def test_sha1_string_input(self):
        self.assertEqual(
            SHA256().generate_hash(""),
            "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        )
        self.assertEqual(
            SHA256().generate_hash("abc"),
            "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
        )
        self.assertEqual(
            SHA256().generate_hash(
                "abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq"
            ),
            "248d6a61d20638b8e5c026930c3e6039a33ce45964ff2167f6ecedd419db06c1",
        )
        self.assertEqual(
            SHA256().generate_hash(
                "abcdefghbcdefghicdefghijdefghijkefghijklfghijklmghijklmnhijklmnoijklmnopjklmnopqklmnopqrlmnopqrsmnopqrstnopqrstu"
            ),
            "cf5b16a778af8380036ce59e7b0492370b249b11e8f07a51afac45037afee9d1",
        )
        self.assertEqual(
            SHA256().generate_hash(
                "12345678901234567890123456789012345678901234567890123456789012345678901234567890"
            ),
            "f371bc4a311f2b009eef952dd83ca80e2b60026c8e935592d0f9c308453c813e",
        )
