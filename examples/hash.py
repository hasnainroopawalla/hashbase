from hashbase import MD2, MD4, MD5, SHA1, CRC8, CRC16, SHA256, SHA224


message: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!"

print(f"MD2: {MD2().generate_hash(message)}")
print(f"MD4: {MD4().generate_hash(message)}")
print(f"MD5: {MD5().generate_hash(message)}")
print(f"SHA-1: {SHA1().generate_hash(message)}")
print(f"SHA-224: {SHA224().generate_hash(message)}")
print(f"SHA-256: {SHA256().generate_hash(message)}")
print(f"CRC-8: {CRC8().generate_hash(message)}")
print(f"CRC-16: {CRC16().generate_hash(message)}")
