#red packet

import random
'''
def sendPockets(total,patiNum):
    patitions = []
    count = 0
    while count < patiNum:
        remainCount = 5 - count -1
        upperbound = total - sum(patitions) -  remainCount
        newPati = random.randint(1,upperbound)
        patitions.append(newPati)
        count = count + 1
    return patitions 
'''
def sendPockets(total,patiNum):
    patitions = [1]*patiNum
    count = 0
    while count < total - patiNum:
        nextPocketToAdd = random.randint(0,patiNum - 1)              
        patitions[nextPocketToAdd] = patitions[nextPocketToAdd] + 1
        count = count + 1
    return patitions    
        
total = input("Input the total money you wanna give out: ")
patiNum = input("Input the patitions you wanna divide the money into:")
count = 0
while count < 10:
    print(sendPockets(int(total),int(patiNum)))
    count = count + 1
