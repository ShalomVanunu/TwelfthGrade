"""
this prog will has CAT picture that cahnged
and will check it
"""

import hashlib
with open('cat.jpg','rb') as afile:
    content = afile.read()
    hasher = hashlib.md5(content)
print(hasher.hexdigest())


with open('catchange.jpg','rb') as afile:
    content = afile.read()
    hasher = hashlib.md5(content)
print(hasher.hexdigest())
