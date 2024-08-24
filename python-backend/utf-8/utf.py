#!/usr/bin/env python3
# Encoding a Unicode string to UTF-8

unicode_string = "Hello, 🤣"
utf8_encoded = unicode_string.encode('utf-8')
print(f"UTF-8 Encoded: {utf8_encoded}")


# Decoding a UTF-8 byte sequence back to a Unicode string

decoded_string = utf8_encoded.decode('utf-8')
print(f"Decoded String: {decoded_string}")
