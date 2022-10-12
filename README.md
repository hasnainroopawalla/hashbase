<h1 align="center">Hashbase</h1>


[![Develop](https://github.com/hasnainroopawalla/hashbase/actions/workflows/develop.yml/badge.svg)](https://github.com/hasnainroopawalla/Ant-Colony-Optimization/actions/workflows/develop.yml)
[![Deploy](https://github.com/hasnainroopawalla/hashbase/actions/workflows/deploy.yml/badge.svg)](https://github.com/hasnainroopawalla/hashbase/actions/workflows/deploy.yml)
[![PyPi version](https://img.shields.io/pypi/v/hashbase.svg)](https://pypi.python.org/pypi/aco_routing/)
[![Python versions](https://img.shields.io/pypi/pyversions/hashbase.svg?style=plastic)](https://img.shields.io/pypi/pyversions/aco_routing.svg?style=plastic)
![Downloads](https://img.shields.io/pypi/dm/hashbase.svg)


A Python package to compute the hash value of an input string using various cryptographic hashing algorithms.

Definition: A hash function is any function that can be used to map data of arbitrary size to fixed-size values ([source](https://en.wikipedia.org/wiki/Hash_function)).


## 📝 Table of Contents

- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contents](#contents)


## 🏁 Getting Started <a name = "getting_started"></a>

### To install the package directly from PyPi:
```
$ pip install hashbase
```


## 🎈 Usage <a name="usage"></a>
> **_Check out:_** [examples/hash.py](https://github.com/hasnainroopawalla/hashbase/blob/master/examples/hash.py)

Import the required hash function(s)
```python
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
    CRC8,
    CRC16,
)
```

Generate the hash of the input string
```python
message: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!"

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
print(f"CRC-8: {CRC8().generate_hash(message)}")
print(f"CRC-16: {CRC16().generate_hash(message)}")
```

The output of the above cell
```
MD2: ebd512bd0162b1c3723f3326f352f50d
MD4: c9066409e6cd86045088ab7e130b7c51
MD5: 641ba60288c17a2da5090077eb8958ad
SHA-1: ad75aab2b0f1b220dcba62f48ce86b387aad225f
SHA-224: c50557bb4de98a3efd31b24cab5b8fe0ed9e081bdd5a2842c646e007
SHA-256: aaa7932dcc5db1e35047bcd1bb857f85c23fc647aebd08290b626b797a336e24
SHA-384: 13fbfe276cd33cf7f219428be7216ed72f913fcf529902b9ff073300fd92f335b4a3e85729d6a1bbc73bca5475e52b8a
SHA-512: cd2abc78ef9694299e3bda722f9535735e4481a07cc422e1609dbd67b126b82f1b72f829f7c4074ded396d25d8363872b60197a421f5f46a1eb430797eb3cfae
SHA-512/224: 4b685ee6fb3fa679785512dd0178c3523c1c4f11cd88ef207ffc8500
SHA-512/256: 4110ce7e37cde62c723f1ef2b7826ff02712a6789642453e5ab9a6ccbde8b0c5
RIPEMD-128: 9eb4516a0b0cfedd3e5cf41eb7c85285
CRC-8: 0x15
CRC-16: 0x3958
```

## 📦 Contents <a name = "contents"></a>

### Message-Digest (MD)
- MD2 (`hashbase.MD2`)
- MD4 (`hashbase.MD4`)
- MD5 (`hashbase.MD5`)

### Secure Hash Algorithm (SHA)
- SHA-1 (`hashbase.SHA1`)
- SHA-224 (`hashbase.SHA224`)
- SHA-256 (`hashbase.SHA256`)
- SHA-512 (`hashbase.SHA512`)
- SHA-512/224 (`hashbase.SHA512_224`)
- SHA-512/256 (`hashbase.SHA512_256`)
- SHA-384 (`hashbase.SHA384`)

### RIPE Message Digest (RIPEMD)
- RIPEMD-128 (`hashbase.RIPEMD128`)

### Cyclic Redundancy Check (CRC)
- CRC-8 (`hashbase.CRC8`)
- CRC-16 (`hashbase.CRC16`)

<hr>


## Contributing

- Post any issues and suggestions on the GitHub [issues](https://github.com/hasnainroopawalla/hashbase/issues) page.
- To contribute, fork the project and then create a pull request back to master.


## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/hasnainroopawalla/hashbase/blob/c6224b72ab7fa08430a3b9f63ec430a4f402ffba/LICENSE) file for details.
