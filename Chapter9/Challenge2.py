answer = input("あなたは何歳ですか？")

with open("write-file.txt","w") as file:
    file.write(answer)
