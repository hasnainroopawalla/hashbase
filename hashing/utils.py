def get_bit_count(binary: str) -> int:
    return len(format(binary, 'b'))

def format_int_to_binary(integer: int, output_bit_count: int = 8) -> str:
    assert get_bit_count(integer) <= output_bit_count
    return str(format(integer, 'b')).zfill(output_bit_count)
