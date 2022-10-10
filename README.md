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
    CRC8,
    CRC16,
    SHA256,
    SHA224,
    SHA384,
    SHA512,
    SHA512_224,
    SHA512_256,
)
```

Generate the hash of the input string
```python
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
print(f"CRC-8: {CRC8().generate_hash(message)}")
print(f"CRC-16: {CRC16().generate_hash(message)}")
```

The output of the above cell
```
MD2: f03881a88c6e39135f0ecc60efd609b9
MD4: 8a9d093f14f8701df17732b2bb182c74
MD5: 5f4dcc3b5aa765d61d8327deb882cf99
SHA-1: 5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8
SHA-224: d63dc919e201d7bc4c825630d2cf25fdc93d4b2f0d46706d29038d01
SHA-256: 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8
SHA-384: a8b64babd0aca91a59bdbb7761b421d4f2bb38280d3a75ba0f21f2bebc45583d446c598660c94ce680c47d19c30783a7
SHA-512: b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86
SHA-512/224: f2356967afbae0c00f7a58d28a126fe034d555397d0d0772d1427c98
SHA-512/256: f3f22d82ccf54a92cfc584d9f1531cbf29b11b513f7f68a20a2fa707f3450220
CRC-8: 0x4f
CRC-16: 0x7e5b
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

### Cyclic Redundancy Check (CRC)
- CRC-8 (`hashbase.CRC8`)
- CRC-16 (`hashbase.CRC16`)

<hr>


## Contributing

- Post any issues and suggestions on the GitHub [issues](https://github.com/hasnainroopawalla/hashbase/issues) page.
- To contribute, fork the project and then create a pull request back to master.


## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/hasnainroopawalla/hashbase/blob/c6224b72ab7fa08430a3b9f63ec430a4f402ffba/LICENSE) file for details.
