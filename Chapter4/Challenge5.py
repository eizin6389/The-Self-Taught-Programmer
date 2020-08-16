def aaa(a):
    return(float(a))

try:
    a = input("type a String")
    print(aaa(str(a)))
except ValueError:
    print("Invalid input")
