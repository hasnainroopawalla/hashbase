class CRC16:
    """This implementation of CRC-16 is inspired by https://sourceforge.net/projects/crccheck/"""

    def __init__(
        self, poly: int = 0x8005, init_value: int = 0x0000, xor_out: int = 0x0000
    ) -> None:
        self.poly = poly
        self.init_value = init_value
        self.xor_out = xor_out

    def generate_hash(self, message: str) -> str:
        """Generates a CRC-16 hash of the input message.

        Args:
            message (str): The input message/text.

        Returns:
            str: The CRC-16 hash of the message.
        """
        message_bytes = bytearray(message, "ascii")
        crc = self.init_value
        for byte in message_bytes:
            crc ^= byte << 8
            for _ in range(8):
                crc = (crc << 1) ^ self.poly if crc & 0x8000 else crc << 1
            crc &= 0xFFFF
        return hex(crc ^ self.xor_out)
