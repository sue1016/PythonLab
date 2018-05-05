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
answerSeq = []
while True:
    predictions = []
    seq = []
    createRandomSeq(seq)
    if seq not in seqList:
        seqList.append(seq)
#        print(len(seqList))
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
       # print("no!",(A,B,C,D,E))
        if allIsHalfRight(predictions):
            print("Got it")
            print((A,B,C,D,E))
            answerSeq.append(seq)
        if len(seqList) == 120:
            print(answerSeq)
            break
'''
# 3 歌手排名预测 

“我是歌手”节目进行最后一期的歌王争夺，共有5名实力唱将进入到最终环节，某娱乐记者私下请5名歌手对结果进行预测，得到如下答案： 

Ａ歌手说：Ｂ第二，我第三； 

Ｂ歌手说：我第二，Ｅ第四； 

Ｃ歌手说：我第一，Ｄ第二； 

Ｄ歌手说：Ｃ最后，我第三； 

Ｅ歌手说：我第四，Ａ第一； 

歌王之战结果出来后，每位歌手的预测都只说对了一半，即一对一错。请编程给出比赛的实际名次（将ABCDE按名次顺序排序，例如BCEAD代表B是第一名，D是最后一名）。

--------
####while True:
     1.随机产生一个没产生过的1到5的排列seq来表示待验证的ABCDE名次顺序  
       并把A,B,C,D,E = seq 
           # 用一个list记录产生过的排列，通过只要没在list中的来实现每次都随机产生没产生过的排列。用计数器记录list的长度，当等于可能出现的所有排列数120时，停止验证，此时若存在这样的名次，则已有结果，否则所求名次顺序不存在。  
     2.用当前A,B,C,D,E(假设当前产生的是3,2,1,4,5)来给每句话的真假赋值，如A的第一句话A1 = (B == 2) ==> A1 = True,以此类推求出A1,A2,B1,B2.....E1,E2的布尔值。我把它们以predictions = [(A,(A1,A2)).....(E,(E1,E2))]的形式存下来
     3.判断当前是否是每个人都对且只对了一半。如果是，则是需要的结果，否则不是。  
     
          
'''
