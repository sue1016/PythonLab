#singers ranking prediction
import random
def allIsHalfRight(predictions):
    for (X,(X1,X2)) in predictions:
        if (X1 is True and X2 is False) or (X1 is False and X2 is True):
            continue
        else:
            return False
    return True    

def createRandomSeq(seq):
    count = 0
    while count < 5:
        new = random.randint(1,5)
        if new not in seq:
            seq.append(new)
            count = count + 1
seqList = []
while True:
    predictions = []
    seq = []
    createRandomSeq(seq)
    if seq not in seqList:
        seqList.append(seq)
        print(len(seqList))
        A,B,C,D,E = seq
    
        #A said A1,A2
        A1 = (B == 2)
        A2 = (A == 3)
        predictions.append((A,(A1,A2)))
        #B said..... and the same with C,D,E

        B1 = (B == 2)
        B2 = (E == 4)
        predictions.append((B,(B1,B2))) 

        C1 = (C == 1)
        C2 = (D == 2)
        predictions.append((C,(C1,C2)))

        D1 = (C == 5)
        D2 = (D == 3)
        predictions.append((D,(D1,D2)))

        E1 = (E == 4)
        E2 = (A == 1)
        predictions.append((E,(E1,E2))) 
        print("no!",(A,B,C,D,E))
        if allIsHalfRight(predictions):
            print("Got it")
            print((A,B,C,D,E))
            break;
    
