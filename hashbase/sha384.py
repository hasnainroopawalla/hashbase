from hashbase import SHA512


class SHA384(SHA512):
    """The SHA-384 algorithm is a cryptographic hashing function used to produce a 384-bit hash.
    The algorithm is identical to SHA-512, except the initial register values and output digest size.
    https://en.wikipedia.org/wiki/SHA-2
    """

    def __init__(self) -> None:
        super().__init__(output_bits=384)
        self.h0: int = 0xCBBB9D5DC1059ED8
        self.h1: int = 0x629A292A367CD507
        self.h2: int = 0x9159015A3070DD17
        self.h3: int = 0x152FECD8F70E5939
        self.h4: int = 0x67332667FFC00B31
        self.h5: int = 0x8EB44A8768581511
        self.h6: int = 0xDB0C2E0D64F98FA7
        self.h7: int = 0x47B5481DBEFA4FA4
