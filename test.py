def fwd(c):
    return (((ord(c) << 5) | (ord(c) >> 3)) ^ 127) & 255


def rev(ans):
    i = ans ^ 111   # perform the xor first, then the bit-shifts after
    return ((i << 3) | (i >> 5)) & 255

# print(fwd(chr(0xa5)))  # sample byte to test this out with =>219

# print(rev(219))  # can we reverse 219 to get back to 0xa5 or 165?

# print(rev(233)) 
x = rev(84)
print(fwd(chr(x)))
print(chr(68))
# print(chr(rev(146)))
# print(chr(rev(209)))
# print(chr(rev(183)))
# print(65//5)
# print(13*5)