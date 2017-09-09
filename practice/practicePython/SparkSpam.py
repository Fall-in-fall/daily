#encoding:utf-8
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.feature import HashingTF
from pyspark.mllib.classification import LogisticRegressionWithSGD
spam = sc.textFile("spam.txt")
normal = sc.textFile("normal.txt")
# 创建一个HashingTF示例来Map邮件到1000个特征值
tf = HashingTF(numFeatures = 10000)
# 每个邮件没分割为单词，每个单词作为一个特征
spamFeatures = spam.map(lambda email: tf.transform(email.split(" ")))
normalFeatures = normal.map(lambda email: tf.transform(email.split(" ")))
# 为正样本和负样本创建标签数据集
positiveExamples = spamFeatures.map(lambda features: LabeledPoint(1, features))
negativeExamples = normalFeatures.map(lambda features: LabeledPoint(0, features))
trainingData = positiveExamples.union(negativeExamples)
trainingData.cache() # 逻辑回归是一个迭代算法，因此使用缓存.
# 使用随机梯度下降算法执行逻辑回归
model = LogisticRegressionWithSGD.train(trainingData)
# 测试
posTest = tf.transform("O M G GET cheap stuff by sending money to ...".split(" "))
negTest = tf.transform("Hi Dad, I started studying Spark the other ...".split(" "))
print "Prediction for positive test example: %g" % model.predict(posTest)
print "Prediction for negative test example: %g" % model.predict(negTest)