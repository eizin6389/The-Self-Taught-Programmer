colors1 = ["puple","orange","green"]
colors2 = ["red","blue","black"]

colors1.pop()
guess = input("何色でしょう？(入力してください)")

if guess in colors1:
    print("当たり")
else:
    print("ハズレ")

print(colors1 + colors2)
