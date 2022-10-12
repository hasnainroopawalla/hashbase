import unittest

from hashbase import CRC16


class TestCRC16Strings(unittest.TestCase):
    def test_crc16_string_input(self):
        self.assertEqual(
            CRC16(poly=0xC867, init_value=0xFFFF).generate_hash(""), hex(0xFFFF)
        )
        self.assertEqual(
            CRC16(poly=0x1021, init_value=0x1D0F).generate_hash("123456789"),
            hex(0xE5CC),
        )
        self.assertEqual(
            CRC16(poly=0x8005, init_value=0x0000).generate_hash("123456789"),
            hex(0xFEE8),
        )
        self.assertEqual(
            CRC16(poly=0x0589, init_value=0x0000, xor_out=0x0001).generate_hash("abcd"),
            hex(0x9F06),
        )
        self.assertEqual(
            CRC16(poly=0x3D65, init_value=0x0000, xor_out=0xFFFF).generate_hash("abcd"),
            hex(0x787C),
        )
