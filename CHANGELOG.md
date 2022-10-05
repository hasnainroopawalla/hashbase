# Change Log

## 05-Oct-2022 [1.0.5]
- Added the following hash functions:
  - SHA-512/224 (`hashbase.SHA512_224`)
  - SHA-512/256 (`hashbase.SHA512_256`)

## 04-Oct-2022 [1.0.4]
- Added the following hash functions:
  - SHA-384 (`hashbase.SHA384`)
  - SHA-512 (`hashbase.SHA512`)
- Modified the `modular_add`, `rotate_left`, `rotate_right`, `shift_left` and `shift_right` utility functions to handle 32-bit and 64-bit numbers
- Modified the `apply_message_padding` utility for more flexible padding

## 03-Oct-2022 [1.0.3]
- Added the following hash function:
  - SHA-224 (`hashbase.SHA224`)

## 03-Oct-2022 [1.0.2]
- Minor docstring update

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
