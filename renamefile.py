
import os

format = ".CSV"
iskom = "_202102_"
final = "_202107_"

c=0

files = os.listdir()
print(files)
for i in files:
    if(format in i):
        itog_name = i.replace(iskom, final)
        os.rename(i, itog_name)
        c=c+1
        print("Переименован: ",i, " Новое имя: " ,itog_name, " Общее кол-во :", c)
