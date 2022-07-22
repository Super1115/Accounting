import os,time
with open("do_not_delete.txt", "r") as f:
    dataa = f.readlines()
    datab = dataa[0]
    data = datab.replace('\n', '')
    print("你現在的餘額是:"+data)
type = input("請問你要增加(輸入a)還是減少(輸入b)金額")
if type == "a":
    a = int(input("請問你要增加的金額是?"))
    b = input("收入簡介:")
    time = time.asctime( time.localtime(time.time()) )
    log = time+","+"增加:"+str(a)+","+"收入簡介:"+b
    print(log)
    new = int(data)+a
    print("這是你增加後的餘額",new)
    with open('do_not_delete.txt','r+') as f:
        f.write(str(new))
        f.write('\n')
        f.write(str(log))
        f.write('\n')
elif type == "b":
    a = int(input("請問你要減少的金額是?"))
    b = input("支出簡介:")
    time = time.asctime( time.localtime(time.time()) )
    log = time+","+"減少:"+str(a)+",""支出簡介:"+b
    print(log)
    new = int(data)-a
    print("這是你減少後的餘額",new)
    with open('do_not_delete.txt','r+') as f:
        f.write(str(new))
        f.write('\n')
        f.write(str(log))
        f.write('\n')
        
else:
    print("無效，請輸入a或b")
os.system("pause")
