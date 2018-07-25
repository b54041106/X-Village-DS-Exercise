from lib.stack import Stack
s = Stack()

def dec_to_bin(dec):
    binary=[] 
    while dec!=0:
        rem=dec%2
        dec=dec//2
        s.push(rem)
        
    while s.size()!=0:
        binary.append(s.pop())
    return binary


dec_to_bin(42)   # 回傳 101010
str1=' '.join(str(e) for e in dec_to_bin(42))
print(str1)
dec_to_bin(100)  # 回傳 1100100
print(dec_to_bin(100))