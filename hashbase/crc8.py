class CRC8:
    """This implementation of CRC-8 is inspired by https://sourceforge.net/projects/crccheck/"""

    def __init__(
        self, poly: int = 0x07, init_value: int = 0x00, xor_out: int = 0x00
    ) -> None:
        self.poly = poly
        self.init_value = init_value
        self.xor_out = xor_out

    def generate_hash(self, message: str) -> str:
        """Generates a CRC-8 hash of the input message.

        Args:
            message (str): The input message/text.

        Returns:
            str: The CRC-8 hash of the message.
        """
        message_bytes = bytearray(message, "ascii")
        crc = self.init_value
        for byte in message_bytes:
            crc ^= byte
            for _ in range(8):
                crc = (crc << 1) ^ self.poly if crc & 0x80 else crc << 1
            crc &= 0xFF
        return hex(crc ^ self.xor_out)
