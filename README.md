A collection of functions for random phrase generation, DataFrame manipulation, and data cleaning.

Description

This project contains a set of functions designed to perform various tasks, such as generating random phrases, manipulating pandas DataFrames, and cleaning data. The functions are categorized into two parts: random phrase and numeric generation functions, and DataFrame manipulation and data cleaning functions.

Installation

To use the functions in this project, you'll need to have Python installed along with the following packages:
pandas
numpy

Functions

Part 2: Random Phrase and Numeric Generation
random_phrase(): Generate a random phrase consisting of an adjective and a noun.
random_float(min_val, max_val): Generate a random float between min_val and max_val.
random_bowling_score(): Generate a random bowling score between 0 and 300.
silly_tuple(): Generate a tuple with a random phrase, a random float between 1 and 5, and a random bowling score.
silly_tuple_list(num_tuples): Generate a list of silly tuples.


Part 3: DataFrame Manipulation and Data Cleaning
null_count(df): Count the number of null values in a DataFrame.
train_test_split(df, frac=0.8): Split a DataFrame into training and testing sets.
randomize(df, seed): Randomize the order of rows in a DataFrame.
addy_split(addy_series): Split an address series into separate columns for city, state, and zip code.
list_2_series(lst, df): Convert a list to a pandas Series and append it as a new column to a DataFrame.
rm_outlier(df): Remove outliers from a DataFrame using the IQR method.
