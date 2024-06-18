"""Import functions"""
import random
import pandas as pd
import numpy as np
from helper_functions import null_count, train_test_split, randomize


# Test cases
df = pd.DataFrame(np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]]))
null_df_1 = pd.DataFrame(
    np.array([[0, np.nan, 2], [3, np.nan, 5], [6, 7, 8]])
)
null_df_2 = pd.DataFrame(
    np.array([[np.nan, np.nan, np.nan], [3, 4, 5], [6, 7, 8]])
)

def test_null_count():
    """ Testing null_count function."""

    assert null_count(df) == 0
    assert null_count(null_df_1) == 2
    assert null_count(null_df_2) == 3


def test_train_test_split():
    """ Testing train_test_split function."""

    train_1, test_1 = train_test_split(df, frac=0.8)
    train_2, test_2 = train_test_split(df, frac=0.2)
    train_3, test_3 = train_test_split(null_df_1, frac=0.8)

    assert len(train_1) == 2
    assert len(test_1) == 1

    assert len(train_2) == 1
    assert len(test_2) == 2

    assert len(train_3) == 2
    assert len(test_3) == 1

def test_randomize():
    """ Testing randomize function"""

    randomized_df = randomize(df, seed=101)
    assert isinstance(randomized_df, pd.DataFrame)
    assert len(randomized_df) == len(df)
    assert not randomized_df.equal(df)