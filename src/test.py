import os
import base64
import hashlib
from math import * 
def checkSNT(a):
    if a < 2:
        return False
    for i in range(2, isqrt(a) + 1):
        if a % i == 0:
            return False
    return True


a = int(input())
print(checkSNT(a))