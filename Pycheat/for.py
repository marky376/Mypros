#!/usr/bin/env python3
lst = [11, 18, 9, 12, 23, 4, 17]
lost = []

for idx in range(len(lst)):
    val = lst[idx]
    if val > 15:
        lost.append(val)
        lst[idx] = 15
print("modif:", lst, "-lost:", lost)
