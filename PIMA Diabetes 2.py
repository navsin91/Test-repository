import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("E:\\pyhon practice files\\Practice round 2\\Logistic regression with dataset\\npima-indians-diabetes.csv")

#EXPLORATORY ANALYSIS

#print data.head(10)
#print data.info()
#print data.shape
#print data.describe()
#print data.isnull().sum()

#displaying zero values

  
#for field in data.columns[:8]:
#    print('Number of 0-entries for "{field_name}" feature: {amount}'.format(
#        field_name=field,
#        amount=np.count_nonzero(data[field] == 0)))

#FEATURE ENGINEERING
    
#features=data.columns[:8]
#print features
#
#x=data[features]
#y=data.label
#print x.head()
#print y.head()

#sns.heatmap(data=x.corr(),annot=True,cmap='RdYlGn',fmt='.2f')
#plt.show()
#
#correlation=data.corr()
#print correlation['label'].sort_values(ascending=False)














