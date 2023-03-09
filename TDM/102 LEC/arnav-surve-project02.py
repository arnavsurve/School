data = {
    'shoes':['red', 'purple', 'red', 'purple', 'red', 'red', 'red'],
    'hats': ['blue', 'blue', 'blue', 'white', 'white', 'blue', 'blue']
}
data
import pandas as pd
store = pd.DataFrame(data, index=['Jay', 'Mary', 'Bill', 'Chris', 'Martha', 'Karen', 'Rob'])
store


myDF = pd.read_csv("/anvil/projects/tdm/data/death_records/DeathRecords.csv")
pd.options.display.max_columns = None
myDF.head()
myDF.iloc[10,]
myDF.tail()
myDF.shape
myDF.columns


len(myDF['Age'][myDF['Age'] > 52])
myDF['Sex'].value_counts()
len(myDF['Sex'][ (myDF['Age'] > 52) & (myDF['Sex'] == 'F')])


import matplotlib.pyplot as plt
mydata = myDF['MaritalStatus'].value_counts()
mydata
plt.bar(mydata.index, mydata)
mydata2 = myDF['Age'][myDF['Age'] < 999].value_counts()
plt.bar(mydata2.index, mydata2)


mydata3 = myDF['MonthOfDeath'].value_counts()
plt.bar(mydata3.index, mydata3)
