MLB_teams = dict([
    ('Chicago', 'White Sox'),
    ('Cleveland', 'Guardians'),
    ('Detroit', 'Tigers'),
    ('Kansas City', 'Royals'),
    ('Minnesota', 'Twins'),
    ('Baltimore', 'Orioles'),
    ('Boston', 'Red Sox'),
    ('New York', 'Yankees'),
    ('Tampa Bay', 'Rays'),
    ('Toronto', 'Blue Jays'),
    ('Houston', 'Astros'),
    ('Los Angeles', 'Angels'),
    ('Oakland', 'Athletics'),
    ('Seattle', 'Mariners'),
    ('Texas', 'Rangers'),
])

MLB_teams.update([
    ('Chicago', 'Cubs'),
    ('Cincinatti', 'Reds'),
    ('Milwaukee', 'Brewers'),
    ('Pittsburgh', 'Pirates'),
    ('St. Louis', 'Cardinals'),
    ('Atlanta', 'Braves'),
    ('Miami', 'Marlins'),
    ('New York', 'Mets'),
    ('Philadelphia', 'Phillies'),
    ('Washington', 'Nationals'),
    ('Arizona', 'Diamondbacks'),
    ('Colorado', 'Rockies'),
    ('Los Angeles', 'Dodgers'),
    ('San Diego', 'Padres'),
    ('San Francisco', 'Giants'),
])

MLB_teams
del MLB_teams['Atlanta']
del MLB_teams['Cincinatti']
MLB_teams


count = 0
while count < 200:
    count += 10
    print(count)

words = "Old McDonald had a farm e-i-e-i-o"

for letter in list(words):
    if letter != 'a':
        print(letter, end='')

for letter in list(words):
    if letter == '-':
        print('*', end='')
    else:
        print(letter, end='')


#create list of fruit
fruit = ['cherry', 'banana', 'orange', 'kiwi', 'apple']
#enumerate fruit but start at number one since default is 0
num_fruit = enumerate(fruit, start=1)
#print the enumerate object as a list
print (list(num_fruit))
#output from code
[(1, 'cherry'), (2, 'banana'), (3, 'orange'), (4, 'kiwi'), (5, 'apple')]

mydict = dict(enumerate(fruit, start=300))
mydict[304]

for myfruit in enumerate(fruit, start=300):
    print(myfruit)

for myfruit in enumerate(fruit, start=300):
    print(myfruit[0])

for myfruit in enumerate(fruit, start=300):
    print(myfruit[1])

for mynumber in range(50):
    print(mynumber)


import pandas as pd
cars = pd.read_csv('/anvil/projects/tdm/data/craigslist/vehicles.csv')
cars.shape
pd.options.display.max_columns = None
cars.head()
cars['year'].value_counts()
mydict = {}

for myyear in cars['year']:
    if (myyear not in mydict):
        mydict[myyear] = 1
    else:
        mydict[myyear] += 1

mydict[2011.0]
mydict[1989.0]
mydict[1997.0]


import matplotlib.pyplot as plt

years = list(cars['year'])
vehicles = list(cars['year'].value_counts())

plt.bar(years, vehicles)
plt.xlabel("Years")
plt.ylabel("Number of Vehicles")
plt.title("Vehicles per Year")
plt.show()
