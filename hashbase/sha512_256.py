from hashbase import SHA512


class SHA512_256(SHA512):
    """The SHA-512/256 algorithm is a cryptographic hashing function used to produce a 256-bit hash.
    The algorithm is identical to SHA-512, except the initial register values and output digest size.
    https://en.wikipedia.org/wiki/SHA-2
    """

    def __init__(self) -> None:
        super().__init__(output_bits=256)
        self.h0: int = 0x22312194FC2BF72C
        self.h1: int = 0x9F555FA3C84C64C2
        self.h2: int = 0x2393B86B6F53B151
        self.h3: int = 0x963877195940EABD
        self.h4: int = 0x96283EE2A88EFFE3
        self.h5: int = 0xBE5E1E2553863992
        self.h6: int = 0x2B0199FC2C85B8AA
        self.h7: int = 0x0EB72DDC81C52CA2
