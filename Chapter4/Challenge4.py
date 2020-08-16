def aaa(a):
    return(a // 2)

def bbb(b):
    return(b * 4)

try:
    a = input("type a Number")
    b = aaa(int(a))
    c = bbb(b)
    print(c)
except ValueError:
    print("Invalid input")
