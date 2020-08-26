import csv

list =[["TOP GUN","Risky Business","Minority Report"],["Titanic","The Revenant","Inception"],["Training Day","Man on Fire","Flight"]]

with open("./Challenge3.csv","w") as file:
    w = csv.writer(file, delimiter=",")
    for readline in list:
        w.writerow(readline)
        print(readline)
