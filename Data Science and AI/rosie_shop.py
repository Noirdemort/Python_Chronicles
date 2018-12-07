import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import math, datetime
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv('lemonade.csv')
df['Day'] = df['Day'].map({'Friday':6,'Saturday':0,'Sunday':1, 'Monday':2,'Tuesday':3,'Wednesday':4,'Thursday':5})

cdf = df.loc[:,('Date','Day','Temperature','Rainfall','Price','Flyers','Sales')]
cdf['Date'] = pd.to_datetime(cdf['Date'])
#cdf['hl_pct'] = (cdf.adj_high - cdf.adj_close)*100/cdf.adj_close
#cdf['pct_change'] = (cdf.adj_close - cdf.adj_open)*100/cdf.adj_open
cdf.dropna(inplace=True)
forecast_col = 'Sales'
forecast_out = int(math.floor(0.012*len(cdf)))
cdf['label'] = cdf[forecast_col].shift(-forecast_out)
cdf.dropna(inplace=True)
cdf.set_index('Date',inplace=True)
cdf.head()

X = np.array(cdf.drop(['label'],1))
y = np.array(cdf.label)
len(cdf.label)
X = preprocessing.scale(X)
x = X[:-forecast_out:]
x_lately = X[-forecast_out:]
x_train, x_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size=0.1)

#clf = svm.SVR() # LinearRegression() or svm.SVR(kernel='poly') poly for poly or else don't use it
## n_jobs = -1 makes use of all processes it can
#clf = LinearRegression(n_jobs=-1)
#clf.fit(x_train,y_train)
#
##uncomment above to perform fresh training

# creates pickle file for training dump
#with open('rosie_lemonade.pickle','wb') as f:
#    pickle.dump(clf, f)

pickle_in = open('rosie_lemonade.pickle','rb')
clf = pickle.load(pickle_in)

accuracy = clf.score(x_test, y_test)
print('Accuracy = ',accuracy)

forecast_set = clf.predict(x_lately)
print(forecast_set,accuracy,forecast_out)
style.use('seaborn-deep') # change and find styles on style.available
# predicting values
cdf['forecast'] = np.nan
last_date = cdf.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    cdf.loc[next_date] = [np.nan for jk in range(len(cdf.columns)-1)] + [i]

#cdf['forecast'].plot()
#cdf['Sales'].plot()
#plt.plot(cdf.index[len(cdf)//3:len(cdf)-10],cdf.Sales[len(cdf)//3:len(cdf)-10])
plt.plot(cdf.index[len(cdf)//2:],cdf.forecast[len(cdf)//2:])
#plt.bar(cdf.forecast,cdf.Sales)
plt.legend(loc='best')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

