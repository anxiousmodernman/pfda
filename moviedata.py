__author__ = 'coleman'

import pandas as pd
from pandas import DataFrame, Series
# from matplotlib import plot
import json
import numpy as np

from settings import PROJECT_ROOT


path = PROJECT_ROOT + '/ch02/movielens/users.dat'  # NOTE don't forget beginning slash
unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table(path, sep='::', header=None, names=unames)

path = PROJECT_ROOT + '/ch02/movielens/ratings.dat'
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table(path, sep='::', header=None, names=rnames)

path = PROJECT_ROOT + '/ch02/movielens/movies.dat'
mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table(path, sep='::', header=None, names=mnames)

# merge and manipulate
data = pd.merge(pd.merge(ratings, users), movies)  # pandas merges by named column
mean_ratings = data.pivot_table('rating', rows='title',
                                cols='gender', aggfunc='mean')
ratings_by_title = data.groupby('title').size()  # creates a Series
active_titles = ratings_by_title.index[ratings_by_title >= 250]  # creates an index
mean_ratings = mean_ratings.ix[active_titles]  # reduce the data set to popular records
top_female_ratings = mean_ratings.sort_index(by='F', ascending=False)  # sort
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']  # straight up add a column
sorted_by_diff = mean_ratings.sort_index(by='diff')  # you can sort like this
rating_std_by_title = data.groupby('title')['rating'].std()  # NOTE to make a std() Series, supply ['rating'] col name
rating_std_by_title = rating_std_by_title.ix[active_titles]  # apply an index to the series


pass


