Z = pow(2, 32)


def left_shift(num: int, shift: int) -> int:
    return (num << shift) | (num >> (32 - shift))


def digest_to_hex_string(digest: int) -> str:
    return digest.to_bytes(16, byteorder="little").hex()


def modular_add(x: int, y: int) -> int:
    return (x + y) % Z