import csv
import numpy 
import operator
def getTrainDataset():
    features = []
    labels = []
    with open("bag/train.csv") as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            x = float(row[0])
            y = float(row[1])
            feature = [x,y]
            
            feature = numpy.array(feature)  
            label = row[3]
    
            features.append(feature)
            labels.append(label)

    return features,labels

def getTestDataset():
    features = []
    with open("bag/test.csv") as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            x = float(row[0])
            y = float(row[1])
            feature = [x,y]
            feature = numpy.array(feature)
            features.append(feature)
    return features

def calEuclideanDistance(vec1,vec2):  
    dist = numpy.sqrt(numpy.sum(numpy.square(vec1 - vec2)))  
    return dist  

def knn(k):
    trainFeatures,trainLabels = getTrainDataset()
    testFeatures = getTestDataset()
    predict = {}
    testRecordId = 0
    for testFeature in testFeatures:
        testRecordId = testRecordId + 1
        trainRecordId = 0 
        allDist = []
        for trainFeature in trainFeatures:
            trainRecordId = trainRecordId + 1
            dist = calEuclideanDistance(testFeature,trainFeature)
            allDist.append([trainRecordId,dist])
            #allDist[trainRecordId] = dist
        sortedDists = sorted(allDist, key=lambda k: k[1])
        knears = sortedDists[:k]
        knearlabels = [trainLabels[knear[0]-1] for knear in knears]
        knearlabelset = set(knearlabels) #myset是另外一个列表，里面的内容是mylist里面的无重复 项
        knearlabelsCounter = {}
        for item in knearlabelset:
            knearlabelsCounter[item] = knearlabels.count(item)

        predictLabel = sorted(knearlabelsCounter.items(), key=operator.itemgetter(1))[0][0]
       # print(knearlabelsCounter) 
       # print(predictLabel)   
        predict[testRecordId] = predictLabel      
    return predict


k = input("input the value of k:")
result = knn(int(k))
print("The predicted type of the test items is as follows")
for X in range(1,11):
    print("Item" + str(X) + "------->" + result[X])




#计算已知类别数据集中的点与当前点之间的距离（欧式距离）
#按照距离递增次序排序
#选取与当前点距离最小的K个点
#确定前K个点所在类别的出现频率
#返回前k个点出现频率最高的类别最为当前点的预测分类
#k表示用于选择最近邻的数目          
