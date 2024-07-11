#!/usr/bin/env python3
# gen.py

def gen():
    ans = yield 0x10, 0x20, 0x30
    
    return ans


g = gen()
g # Nothing much happens -- need to iterate with '__next__()'

next(g)
