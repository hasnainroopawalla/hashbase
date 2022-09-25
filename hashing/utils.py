Z = 0x100000000


def get_bit_count(binary: str) -> int:
    return len(format(binary, "b"))


def format_int_to_binary_string(integer: int, output_bit_count: int = 8) -> str:
    assert get_bit_count(integer) <= output_bit_count
    return str(format(integer, "b")).zfill(output_bit_count)


def binary_string_to_hex(binary: str) -> int:
    decimal = int(binary, 2)
    return int(hex(decimal), 16)


def modular_addition(x, y):
    return (x + y) % Z


x = "101011110100110000100111110000"
y = "00101011110100110000100111110000"

x_bin = 0b101011110100110000100111110000
y_bin = 0b00101011110100110000100111110000
# print(len(x), len(y))
# print(bin(y_bin << 9))


def left_shift(num: int, shift: int) -> int:
    # binary = str(format(hex_num, "b")).zfill(32)
    # if len(binary) < 32:
    #     binary = binary.zfill(32)
    # return binary_string_to_hex(binary[shift:] + binary[:shift])
    num &= 0xFFFFFFFF
    return (num << shift | num >> (32 - shift)) & 0xFFFFFFFF


# print(left_shift(9945746635, 7))
# # 1745249704


def bytearray_to_binary_string(array: bytearray) -> str:
    def access_bit(data, num):
        base = int(num // 8)
        shift = int(num % 8)
        return (data[base] >> shift) & 0x1

    return "".join([str(access_bit(array, i)) for i in range(len(array) * 8)])
