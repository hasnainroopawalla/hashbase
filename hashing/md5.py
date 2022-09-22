from utils import format_int_to_binary


def text_to_binary_message(text):
    return ''.join([format_int_to_binary(ord(ch), 8) for ch in text])

def apply_padding(message):
    message_length = len(message)
    
    # Pad a trailing '1'
    message += '1'
    
    # Pad 0s to enforce a message length of 448 bits
    message = message.ljust(512 - 64, '0')
    
    # Pad the last 64 bits that indicate the message length
    message += format_int_to_binary(message_length, 64)
    
    return message
    
if __name__ == "__main__":
    text =  "They are deterministic"
    assert len(text) <= 56
    
    message = text_to_binary_message(text)
    padded_message = apply_padding(message)
    print(padded_message, len(padded_message))
    
    # num1 = '01010100011010000110010101111001'
    # num2 = '01010101011010000110010101001001'
    # num1_hex = hex(int(num1, 2))
    # num2_hex = hex(int(num2, 2))
    
    # print(num1_hex, num2_hex, hex(0x89abcdef & 0xfedcba98))
    
    