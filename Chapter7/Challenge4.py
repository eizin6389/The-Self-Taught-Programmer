number_list = {1,3,5,6,8,11}

while True:
    answer = input("文字を入力して下さい。または q で終了します")
    if answer in number_list:
        print("正解")
    elif answer.isdecimal():
        print("不正解")
    elif answer in "q":
        break
    else:
        print("数字を入力するか、qで終了します")
