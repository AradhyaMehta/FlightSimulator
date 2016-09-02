import sys
from sklearn import tree
import csv
        
def takeInput():
    readfile = open(sys.argv[1])
    readfilecsv = csv.reader(readfile)
    dept_time = sys.argv[2]
    arr_time = sys.argv[3]
    departure_airport = sys.argv[4]
    arrival_airport = sys.argv[5]
    departures_list_airports = []
    arrivals_list_airports = []
    original_arrival_times = []
    estimated_arrival_times = []
    original_departure_times = []
    estimated_departure_times = []
    data = []
    attb = []

    print departure_airport
    print arrival_airport
    
    X1 = []
    X2 = []
    Y = []
    origin_arr = []
    estim_arr = []
    
    for row in readfilecsv:
        data.append(row)

    for i in range(0, len(data)):
        departures_list_airports.append(data[i][1])
        arrivals_list_airports.append(data[i][2])
        original_departure_times.append((data[i][4]).split())
        estimated_departure_times.append((data[i][5]).split())
        original_arrival_times.append((data[i][6]).split())
        estimated_arrival_times.append((data[i][7]).split())

    #dummy = []
    #out = csv.writer(open("MYFILE.csv", "wb"))
    count = 0
    for k in range(0, len(data)):
        if departure_airport == departures_list_airports[k] and arrival_airport == arrivals_list_airports[k]:

            if estimated_arrival_times[k+1] > original_arrival_times[k+1]:
                Y.append('1')
                X1.append(estimated_departure_times[k+1][1][0:2])
                X2.append(estimated_arrival_times[k+1][1][0:2])
                count = count + 1
                    
            else:
                Y.append('0')
                X1.append(estimated_departure_times[k+1][1][0:2])
                X2.append(estimated_arrival_times[k+1][1][0:2])
                count = count + 1
    
    #rows = zip(X1,X2,Y)
    #for row in rows:
    #    out.writerow(row)

    data1 = []
    x1 = []
    x2 = []
    y = []
    attb = []


    for example in range(0,len(Y)):
        sample = []    
        sample = [float(X1[example]),float(X2[example]),float(Y[example])]
        attb1 = [float(X1[example]),float(X2[example])]
        data1.append(sample)
        attb.append(attb1)
        x1.append(float(X1[example]))
        x2.append(float(X2[example]))
        y.append(float(Y[example]))


    train_X = attb
    train_Y = y

    
    # train and predict
    prediction = train(train_X, train_Y, dept_time, arr_time)

    if prediction == 1:
        print 'Flight Delayed'
    if prediction == 0:
        print 'Flight On Time'
    
    print "probability of flight delay"
    print float(count/len(Y))

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
    pred = clf.predict(test)
    prob = clf.predict_proba(test)
    
    return pred


takeInput()
