from lib.stack import Stack
s = Stack()

def base_converter(dec_number, base):
    string=[]
    while dec_number!=0:
        rem=dec_number%base
        dec_number=dec_number//base
        if rem<=9:
            rem=rem
        if rem==10:
            rem='A'
        if rem==11:
            rem='B'
        if rem==12:
            rem='C'
        if rem==13:
            rem= 'D'
        if rem==14:
            rem= 'E'
        if rem==15:
            rem= 'F'
        s.push(rem)
        
    while s.size()!=0:
        string.append(s.pop())
    return string

base_converter(1000, 16)  # 回傳 3E8
base_converter(700, 12)   # 回傳 4A4
str1=' '.join(str(e) for e in base_converter(1000, 16))
str2=' '.join(str(e) for e in base_converter(700, 12))
print(str1)
print(str2)