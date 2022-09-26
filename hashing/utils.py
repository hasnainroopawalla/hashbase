def left_shift(num: int, shift: int) -> int:
    # binary = str(format(hex_num, "b")).zfill(32)
    # if len(binary) < 32:
    #     binary = binary.zfill(32)
    # return binary_string_to_hex(binary[shift:] + binary[:shift])
    num &= 0xFFFFFFFF
    return (num << shift | num >> (32 - shift)) & 0xFFFFFFFF


def little_endian_to_hex_string(little_endian_digest: int) -> str:
    return little_endian_digest.to_bytes(16, byteorder="little").hex()