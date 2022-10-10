import unittest

from hashbase import CRC8


class TestCRC8Strings(unittest.TestCase):
    def test_crc8_string_input(self):
        self.assertEqual(CRC8(poly=0x07, init_value=0x00).generate_hash(""), hex(0x00))
        self.assertEqual(CRC8(poly=0x9B, init_value=0xFF).generate_hash(""), hex(0xFF))
        self.assertEqual(
            CRC8(poly=0x07, init_value=0x00).generate_hash("123456789"), hex(0xF4)
        )
        self.assertEqual(
            CRC8(poly=0x9B, init_value=0xFF).generate_hash("123456789"), hex(0xDA)
        )
        self.assertEqual(
            CRC8(poly=0xD5, init_value=0x00).generate_hash("123456789"), hex(0xBC)
        )
        self.assertEqual(
            CRC8(poly=0x1D, init_value=0xFD).generate_hash("abcd"), hex(0x3A)
        )
        self.assertEqual(
            CRC8(poly=0xD5, init_value=0x00).generate_hash("abcd"), hex(0x5E)
        )
        self.assertEqual(
            CRC8(poly=0x07, init_value=0x00, xor_out=0x55).generate_hash("abcdefg1234"),
            hex(0x13),
        )
