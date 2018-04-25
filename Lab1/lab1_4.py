#compare insert() with append() on their runtime
import datetime

appList = []
insList = []

startTime = datetime.datetime.now()
for i in range(0,50001):
    appList.append(50000-i)
endTime = datetime.datetime.now()
print((endTime - startTime).microseconds)

startTime = datetime.datetime.now()
for i in range(0,50001):
    insList.insert(0,i)
endTime = datetime.datetime.now()
print((endTime - startTime).microseconds)

    
