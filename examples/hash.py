from hashing.md2 import MD2
from hashing.md5 import MD5
from hashing.sha1 import SHA1

message: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

print(f"MD2: {MD2().generate_hash(message)}")
print(f"MD5: {MD5().generate_hash(message)}")
print(f"SHA-1: {SHA1().generate_hash(message)}")
