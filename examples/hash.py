from hashing.md5 import MD5
from hashing.sha1 import SHA1

message: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

print(f"MD5: {MD5().generate_hash(message)}")
print(f"SHA-1: {SHA1().generate_hash(message)}")
