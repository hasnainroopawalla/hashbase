import unittest
import json

from hashbase import (
    MD2,
    MD4,
    MD5,
    SHA1,
    SHA224,
    SHA256,
    SHA384,
    SHA512,
    SHA512_224,
    SHA512_256,
    RIPEMD128,
    RIPEMD160,
    RIPEMD256,
    RIPEMD320,
)


class TestHashFunctions(unittest.TestCase):
    def test_hash_functions(self):
        with open("tests/test_cases.json", "r") as f:
            test_cases = json.load(f)

        for test_case in test_cases:
            self.assertEqual(
                MD2().generate_hash(test_case["message"]), test_case["expected"]["MD2"]
            )
            self.assertEqual(
                MD4().generate_hash(test_case["message"]), test_case["expected"]["MD4"]
            )
            self.assertEqual(
                MD5().generate_hash(test_case["message"]), test_case["expected"]["MD5"]
            )
            self.assertEqual(
                SHA1().generate_hash(test_case["message"]),
                test_case["expected"]["SHA1"],
            )
            self.assertEqual(
                SHA224().generate_hash(test_case["message"]),
                test_case["expected"]["SHA224"],
            )
            self.assertEqual(
                SHA256().generate_hash(test_case["message"]),
                test_case["expected"]["SHA256"],
            )
            self.assertEqual(
                SHA384().generate_hash(test_case["message"]),
                test_case["expected"]["SHA384"],
            )
            self.assertEqual(
                SHA512().generate_hash(test_case["message"]),
                test_case["expected"]["SHA512"],
            )
            self.assertEqual(
                SHA512_224().generate_hash(test_case["message"]),
                test_case["expected"]["SHA512_224"],
            )
            self.assertEqual(
                SHA512_256().generate_hash(test_case["message"]),
                test_case["expected"]["SHA512_256"],
            )
            self.assertEqual(
                RIPEMD128().generate_hash(test_case["message"]),
                test_case["expected"]["RIPEMD128"],
            )
            self.assertEqual(
                RIPEMD160().generate_hash(test_case["message"]),
                test_case["expected"]["RIPEMD160"],
            )
            self.assertEqual(
                RIPEMD256().generate_hash(test_case["message"]),
                test_case["expected"]["RIPEMD256"],
            )
            self.assertEqual(
                RIPEMD320().generate_hash(test_case["message"]),
                test_case["expected"]["RIPEMD320"],
            )
