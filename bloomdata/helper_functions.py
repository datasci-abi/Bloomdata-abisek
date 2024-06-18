# pylint: disable=invalid-name
"""Import functions"""
import random
import pandas as pd
import numpy as np

# Part 2 Functions ============

adjectives = ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']
nouns = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']

def random_phrase():
    """Generate a random phrase consisting of an adjective and a noun."""
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    return f"{adj} {noun}"

def random_float(min_val, max_val):
    """Generate a random float between min_val and max_val."""
    return random.uniform(min_val, max_val)

def random_bowling_score():
    """Generate a random bowling score between 0 and 300."""
    return random.randint(0, 300)

def silly_tuple():
    """Generate a tuple with a random phrase"""
    return (random_phrase(), round(random_float(1, 5), 1), random_bowling_score())

def silly_tuple_list(num_tuples):
    """Generate a list of silly tuples."""
    return [silly_tuple() for _ in range(num_tuples)]

# Part 3 Functions ======================

test_df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
null_df = pd.DataFrame(np.array([[1, np.nan, 3], [4, 5, np.nan], [np.nan, 8, np.nan]]))

def null_count(df):
    """Count the number of null values in a DataFrame."""
    return df.isnull().sum().sum()

def train_test_split(df, frac=0.8):
    """Split a DataFrame into training and testing sets."""
    train = df.sample(frac=frac, random_state=42)
    test = df.drop(train.index)
    return train, test

def randomize(df, seed):
    """Randomize the order of rows in a DataFrame."""
    return df.sample(frac=1.0, random_state=seed)

address_df = pd.DataFrame({
    'address': [
        '890 Jennifer Brooks\nNorth Janet, WY 24785',
        '8394 Kim Meadow\nDarrenville, AK 27389',
        '379 Cain Plaza\nJosephburgh, WY 06332',
        '5303 Tina Hill\nAudreychester, VA 97036'
    ]
})

def addy_split(addy_series):
    """Split an address series into separate columns for city, state, and zip code."""
    df = pd.DataFrame()
    city_list = []
    state_list = []
    zip_list = []
    for addy in addy_series:
        second_half = addy.split('\n')[1]
        city = second_half.split(',')[0].strip()
        state = second_half.split()[-2]
        zip_code = second_half.split()[-1]
        city_list.append(city)
        state_list.append(state)
        zip_list.append(zip_code)
    df['city'] = city_list
    df['state'] = state_list
    df['zip'] = zip_list
    return df

def list_2_series(lst, df):
    """Convert a list to a pandas Series and append it as a new column to a DataFrame."""
    new_column = pd.Series(lst)
    return pd.concat([df, new_column.rename("new_column")], axis=1)

outlier_df = pd.DataFrame({
    'a': [1, 2, 3, 4, 5, 6],
    'b': [4, 5, 6, 7, 8, 9],
    'c': [7, 1000, 9, 10, 11, 12]
})

def rm_outlier(df):
    """Remove outliers from a DataFrame using the IQR method."""
    for column_name, column_data in df.iteritems():
        Q1 = column_data.quantile(0.25)
        Q3 = column_data.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df[column_name] = column_data.apply(
            lambda x: x if lower_bound <= x <= upper_bound else np.nan
        )
    return df

# Example usage (uncomment to test)
# print(random_phrase())
# print(random_float(2, 4))
# print(random_bowling_score())
# print(silly_tuple())
# print(silly_tuple_list(5))
# print(null_count(test_df))
# print(null_count(null_df))
# print(train_test_split(test_df))
# print(randomize(test_df, 10))
# print(addy_split(address_df['address']))
# print(list_2_series([10, 11, 12], test_df))
# print(rm_outlier(outlier_df))