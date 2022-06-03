import os
with open("amount.txt", "r") as f:
    data = f.read()
    print("你現在的餘額是:"+data)
type = input("請問你要增加(輸入a)還是減少(輸入b)金額")
if type == "a":
    a = int(input("請問你要增加的金額是?"))
    new = int(data)+a
    print("這是你增加後的餘額",new)
    with open('amount.txt','w') as f:
        f.write(str(new))

elif type == "b":
    a = int(input("請問你要減少的金額是?"))
    new = int(data)-a
    print("這是你減少後的餘額",new)
    with open('amount.txt','w') as f:
        f.write(str(new))
os.system("pause")
