# Change Log

## 03-Oct-2022 [1.0.1]
- Added the following hash function:
  - SHA-256 (`hashbase.SHA256`)
- Added utilities for `rotate_left`, `rotate_right`, `shift_left` and `shift_right`
- Updated the `utils.modular_add()` function

## 02-Oct-2022 [1.0.0]
- Added the following hash functions:
  - MD2 (`hashbase.MD2`)
  - MD4 (`hashbase.MD4`)
  - MD5 (`hashbase.MD5`)
  - SHA-1 (`hashbase.SHA1`)
  - CRC-8 (`hashbase.CRC8`)
  - CRC-16 (`hashbase.CRC16`)
- Added unit tests for all hash functions
- Added an example file `examples/hash.py` that calls all the implemented hash functions
