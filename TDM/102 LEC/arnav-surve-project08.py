import pandas as pd
users = pd.read_parquet("/anvil/projects/tdm/data/yelp/data/parquet/users.parquet")
reviews = pd.read_parquet("/anvil/projects/tdm/data/yelp/data/parquet/reviews.parquet")
pd.set_option('display.max_columns', None)
users.head()
reviews.head()
mylistoffriends = users[users['user_id'] == 'ntlvfPzc8eglqvk92iDIAw']['friends'].iloc[0].split(", ")
users[users['user_id'].isin(mylistoffriends)].shape
mylistoffriends = users[users['user_id'] == 'FOBRPlBHa3WPHFB5qYDlVg']['friends'].iloc[0].split(", ")
users[users['user_id'].isin(mylistoffriends)].shape
mylistoffriends = users[users['user_id'] == 'zZUnPeh2hEp0WydbAZEOOg']['friends'].iloc[0].split(", ")
users[users['user_id'].isin(mylistoffriends)].shape
def get_friends_data(myuserid: str) -> pd.DataFrame:
    # accepts myuserid and returns pd dataframe contaaining user info for each friend of myuserid
    mylistoffriends = users[users['user_id'] == myuserid]['friends'].iloc[0].split(", ")
    return users[users['user_id'].isin(mylistoffriends)]
get_friends_data('ntlvfPzc8eglqvk92iDIAw')
get_friends_data('FOBRPlBHa3WPHFB5qYDlVg')
get_friends_data('zZUnPeh2hEp0WydbAZEOOg')


reviews[reviews['business_id'] == '-MhfebM0QIsKt87iDN-FNw']['stars'].mean()
reviews[reviews['business_id'] == '5JxlZaqCnk1MnbgRirs40Q']['stars'].mean()
reviews[reviews['business_id'] == 'faPVqws-x-5k2CQKDNtHxw']['stars'].mean()
def calculate_avg_business_stars(mybusinessid: str) -> float:
    # accepts mybusinessid and returns a float of the average number of stars
    return reviews[reviews['business_id'] == mybusinessid]['stars'].mean()
calculate_avg_business_stars('-MhfebM0QIsKt87iDN-FNw')
calculate_avg_business_stars('5JxlZaqCnk1MnbgRirs40Q')
calculate_avg_business_stars('faPVqws-x-5k2CQKDNtHxw')


import matplotlib.pyplot as plt
mydf = reviews[reviews['business_id'] == "-MhfebM0QIsKt87iDN-FNw"]
plt.plot(mydf.groupby(mydf['date'].dt.year)['stars'].mean())
mydf = reviews[reviews['business_id'] == "5JxlZaqCnk1MnbgRirs40Q"]
plt.plot(mydf.groupby(mydf['date'].dt.year)['stars'].mean())
mydf = reviews[reviews['business_id'] == "faPVqws-x-5k2CQKDNtHxw"]
plt.plot(mydf.groupby(mydf['date'].dt.year)['stars'].mean())
def visualize_stars_over_time(mybusinessid: str) -> None:
    # Accepts mybusinessid string and generates a line plot showing the average number of stars in each year (for which the business has reviews)
    mydf = reviews[reviews['business_id'] == mybusinessid]
    plt.plot(mydf.groupby(mydf['date'].dt.year)['stars'].mean())
    return None
visualize_stars_over_time("-MhfebM0QIsKt87iDN-FNw")
visualize_stars_over_time("5JxlZaqCnk1MnbgRirs40Q")
visualize_stars_over_time("faPVqws-x-5k2CQKDNtHxw")


def visualize_stars_over_time(mybusinessid: str, granularity: str = "years") -> None:
    # Accepts mybusinessid string and generates a line plot showing the average number of stars in each year (for which the business has reviews)
    mydf = reviews[reviews['business_id'] == mybusinessid]
    
    if granularity == "months":
        plt.plot(mydf.groupby([mydf['date'].dt.year,mydf['date'].dt.month])['stars'].mean().reset_index(drop=True))
    else:
        plt.plot(mydf.groupby(mydf['date'].dt.year)['stars'].mean())
    return None
visualize_stars_over_time("-MhfebM0QIsKt87iDN-FNw")
visualize_stars_over_time("-MhfebM0QIsKt87iDN-FNw", "years")
visualize_stars_over_time("-MhfebM0QIsKt87iDN-FNw", "months")
visualize_stars_over_time("5JxlZaqCnk1MnbgRirs40Q")
visualize_stars_over_time("5JxlZaqCnk1MnbgRirs40Q", "years")
visualize_stars_over_time("5JxlZaqCnk1MnbgRirs40Q", "months")
visualize_stars_over_time("faPVqws-x-5k2CQKDNtHxw")
visualize_stars_over_time("faPVqws-x-5k2CQKDNtHxw", "years")
visualize_stars_over_time("faPVqws-x-5k2CQKDNtHxw", "months")


def visualize_stars_over_time(*allofmybusinessids) -> None:
    # Accepts mybusinessid string and generates a line plot showing the average number of stars in each year (for which the business has reviews)
    
    for mybusinessid in allofmybusinessids:
        mydf = reviews[reviews['business_id'] == mybusinessid]
        plt.plot(mydf.groupby(mydf['date'].dt.year)['stars'].mean())
    plt.show()
    return None
visualize_stars_over_time("-MhfebM0QIsKt87iDN-FNw", "5JxlZaqCnk1MnbgRirs40Q", "faPVqws-x-5k2CQKDNtHxw")
