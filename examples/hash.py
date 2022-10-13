from hashbase import (
    MD2,
    MD4,
    MD5,
    SHA1,
    SHA224,
    SHA256,
    SHA384,
    SHA512,
    SHA512_224,
    SHA512_256,
    RIPEMD128,
    RIPEMD160,
    RIPEMD256,
    RIPEMD320,
    CRC8,
    CRC16,
)


message: str = "password"

print(f"MD2: {MD2().generate_hash(message)}")
print(f"MD4: {MD4().generate_hash(message)}")
print(f"MD5: {MD5().generate_hash(message)}")
print(f"SHA-1: {SHA1().generate_hash(message)}")
print(f"SHA-224: {SHA224().generate_hash(message)}")
print(f"SHA-256: {SHA256().generate_hash(message)}")
print(f"SHA-384: {SHA384().generate_hash(message)}")
print(f"SHA-512: {SHA512().generate_hash(message)}")
print(f"SHA-512/224: {SHA512_224().generate_hash(message)}")
print(f"SHA-512/256: {SHA512_256().generate_hash(message)}")
print(f"RIPEMD-128: {RIPEMD128().generate_hash(message)}")
print(f"RIPEMD-160: {RIPEMD160().generate_hash(message)}")
print(f"RIPEMD-256: {RIPEMD256().generate_hash(message)}")
print(f"RIPEMD-320: {RIPEMD320().generate_hash(message)}")
print(f"CRC-8: {CRC8().generate_hash(message)}")
print(f"CRC-16: {CRC16().generate_hash(message)}")
