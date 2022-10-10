import unittest

from hashbase import SHA512_224


class TestSHA1Strings(unittest.TestCase):
    def test_sha1_string_input(self):
        self.assertEqual(
            SHA512_224().generate_hash(""),
            "6ed0dd02806fa89e25de060c19d3ac86cabb87d6a0ddd05c333b84f4",
        )
        self.assertEqual(
            SHA512_224().generate_hash("abc"),
            "4634270f707b6a54daae7530460842e20e37ed265ceee9a43e8924aa",
        )
        self.assertEqual(
            SHA512_224().generate_hash(
                "abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq"
            ),
            "e5302d6d54bb242275d1e7622d68df6eb02dedd13f564c13dbda2174",
        )
        self.assertEqual(
            SHA512_224().generate_hash(
                "abcdefghbcdefghicdefghijdefghijkefghijklfghijklmghijklmnhijklmnoijklmnopjklmnopqklmnopqrlmnopqrsmnopqrstnopqrstu"
            ),
            "23fec5bb94d60b23308192640b0c453335d664734fe40e7268674af9",
        )
        self.assertEqual(
            SHA512_224().generate_hash(
                "12345678901234567890123456789012345678901234567890123456789012345678901234567890"
            ),
            "ae988faaa47e401a45f704d1272d99702458fea2ddc6582827556dd2",
        )
