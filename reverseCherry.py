def fwd(c):
    return (((ord(c) << 5) | (ord(c) >> 3)) ^ 127) & 255


def rev(ans):
    i = ans ^ 127   # perform the xor first, then the bit-shifts after
    return ((i << 3) | (i >> 5)) & 255

def reverseNum(num):
    # ( ((i - 2 )
    # result = int((((num+15)-((17/4)+3)*5))
    # charIs = chr(num)
    result = num + 2
    return result
    
list2 = []

passwd = [82, 144, 207, 181, 80, 176, 81, 240, 240, 78, 181, 144, 207, 176, 241, 212, 209]
print(passwd)
for i in passwd:
    result = reverseNum(i)
    list2.append(result)

    
print(list2)
yyy=[]
zzz=[]
string = ""
for x in list2:
    y = rev(x)
    # print(y)
    yyy.append(y)
    # print(x)
    # z = fwd(chr(y))
    # zzz.append(z)
    # print(z)
    char = chr(y)
    string+=char
    # print(fwd(chr(x)))
    # print(chr(y))
    
print('y',yyy)
print('z', zzz)
print(string)
