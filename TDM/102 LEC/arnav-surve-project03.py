ls /anvil/projects/tdm/data/flights/subset/
import pandas as pd
from pathlib import Path

files = [Path(f'/anvil/projects/tdm/data/flights/subset/{year}.csv') for year in range(1987,2009)]
files
eightyseven = pd.read_csv(files[0])
print(eightyseven.columns)
print(len(eightyseven.columns))
print(eightyseven.columns[:5])

eightyseven['Origin']
eightyseven['Origin'].value_counts()['IND']

eightyeight = pd.read_csv(files[1])
eightynine = pd.read_csv(files[2])
ninety = pd.read_csv(files[3])
eightyeight['Origin'].value_counts()['IND']
eightynine['Origin'].value_counts()['IND']
ninety['Origin'].value_counts()['IND']

origin_ind = 0
for file in files:
    with open(file,'r') as f:
        for line in f:
            if line.split(",")[16] == 'IND':
                origin_ind += 1
print(origin_ind)
