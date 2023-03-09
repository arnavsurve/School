import pandas as pd
pd.set_option('display.max_columns', None)
%%bash
head -n1 /anvil/projects/tdm/data/flights/subset/1987.csv >~/INDflights.csv
grep -h ",IND," /anvil/projects/tdm/data/flights/subset/*.csv >>~/INDflights.csv
myDF = pd.read_csv('~/INDflights.csv')
myDF.shape
myDF[myDF['Origin'] == 'IND'].shape
myDF[myDF['Dest'] == 'IND'].shape


myDF[myDF['Origin'] == 'IND']['Dest'].value_counts().head(20)
myDF[myDF['Origin'] == 'IND']['UniqueCarrier'].value_counts().head(5)
myDF.head()
myDF.tail()
myDF.value_counts()


def popularAirports(myDF: pd.DataFrame, airport: str) -> pd.Series:
    return myDF[myDF['Origin'] == airport]['Dest'].value_counts().head(20)
popularAirports(myDF, 'IND')
def popularAirlines(myDF: pd.DataFrame, airport: str) -> pd.Series:
    return myDF[myDF['Origin'] == 'IND']['UniqueCarrier'].value_counts().head(5)
popularAirlines(myDF, 'IND')


%%bash
head -n1 /anvil/projects/tdm/data/flights/subset/1987.csv >~/BUFflights.csv
grep -h ",BUF," /anvil/projects/tdm/data/flights/subset/*.csv >>~/BUFflights.csv
myDF = pd.read_csv('~/BUFflights.csv')
popularAirports(myDF, 'BUF')
popularAirlines(myDF, 'BUF')
popularAirports(myDF, 'JAX')
popularAirlines(myDF, 'JAX')
