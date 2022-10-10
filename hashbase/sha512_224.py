from hashbase import SHA512


class SHA512_224(SHA512):
    """The SHA-512/224 algorithm is a cryptographic hashing function used to produce a 224-bit hash.
    The algorithm is identical to SHA-512, except the initial register values and output digest size.
    https://en.wikipedia.org/wiki/SHA-2
    """

    def __init__(self) -> None:
        super().__init__(output_bits=224)
        self.h0: int = 0x8C3D37C819544DA2
        self.h1: int = 0x73E1996689DCD4D6
        self.h2: int = 0x1DFAB7AE32FF9C82
        self.h3: int = 0x679DD514582F9FCF
        self.h4: int = 0x0F6D2B697BD44DA8
        self.h5: int = 0x77E36F7304C48942
        self.h6: int = 0x3F9D85A86A1D36C8
        self.h7: int = 0x1112E6AD91D692A1
