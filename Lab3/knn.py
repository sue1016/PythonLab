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

print(knn(20))        




#计算已知类别数据集中的点与当前点之间的距离（欧式距离）
#按照距离递增次序排序
#选取与当前点距离最小的K个点
#确定前K个点所在类别的出现频率
#返回前k个点出现频率最高的类别最为当前点的预测分类
#k表示用于选择最近邻的数目          
# 
# [ref:读写CSV数据](http://python3-cookbook-personal.readthedocs.io/zh_CN/latest/c06/p01_read_write_csv_data.html)
# [ref:计算向量欧氏距离](https://blog.csdn.net/sscssz/article/details/52456848)
# [ref:knn](https://github.com/frankstar007/kNN/blob/master/python%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E4%B9%8B%20K-%E9%82%BB%E8%BF%91%E7%AE%97%E6%B3%95.md)
# [ref:使用lambda应对各种复杂情况的排序，包括list嵌套dict](https://www.polarxiong.com/archives/Python-%E4%BD%BF%E7%94%A8lambda%E5%BA%94%E5%AF%B9%E5%90%84%E7%A7%8D%E5%A4%8D%E6%9D%82%E6%83%85%E5%86%B5%E7%9A%84%E6%8E%92%E5%BA%8F-%E5%8C%85%E6%8B%AClist%E5%B5%8C%E5%A5%97dict.html)
# [ref:统计列表中的重复项出现的次数](https://site.douban.com/136082/widget/notes/6031056/note/215926715/)
# [ref:How do I sort a dictionary by value?](https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value)
