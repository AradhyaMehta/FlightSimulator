import sys
from sklearn import tree
import csv

# this class take the data set and
# splits it into the attributes and the
# class labels respectively
class Data:
    def __init__(self, fileName):
        self.data = []
        self.x1=[]
        self.x2=[]
        self.y=[]
        self.attb=[]
        for example in csv.reader(open(fileName, 'rb')):
            sample=[]
            sample=[float(example[0]),float(example[1]),float(example[2])]
            attb1=[float(example[0]),float(example[1])]
            self.data.append(sample)
            self.attb.append(attb1)
            self.x1.append(float(example[0]))
            self.x2.append(float(example[1]))
            self.y.append(float(example[2]))

def takeInput():

    # take the training data, departure city and arrival city
    train_data_file = sys.argv[1]
    dept_time = float(sys.argv[2])
    arr_time = float(sys.argv[3])
    
    train_data = Data(train_data_file)
    train_X = train_data.attb
    train_Y = train_data.y

    check = 1.0
    count = 0
    
    for k in range(0, len(train_Y)):
        if ( float(check) == float(train_Y[k]) ):
            count = count + 1
    
    print "Probability of delay " + str((count*1.0/len(train_Y)))
    
    # train and predict
    prediction = train(train_X,train_Y,dept_time,arr_time)
    
    if prediction == 1:
        print "Todays Verdict: Flight Delayed"
    if prediction == 0:
        print "Todays Verdict: Flight On Time"


# this function trains the decision tree with
# the training data set provided.
# and then predicts the class of the sample provided
def train(train_X, train_Y, dep_time, arr_time):

    # create an object of the scikit learn classifer
    clf = tree.DecisionTreeClassifier()

    # train the classifier
    clf = clf.fit(train_X, train_Y)

    test=[dep_time,arr_time]

    # use the classifer to predict
    # the y label for the test departure city and arrival city
    pred=clf.predict(test)
    prob=clf.predict_proba(test)
    return pred

takeInput()
