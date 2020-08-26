import csv

list =[["トップガン","リスキービジネス","マイノリティリポート"],["タイタニック","レブナント","インセプション"],["トレーニングデイ","マンオンファイヤー","フライト"]]

with open("./Challenge4.csv","w",encoding="utf-8") as file:
    w = csv.writer(file, delimiter=",")
    for readline in list:
        w.writerow(readline)
        print(readline)
