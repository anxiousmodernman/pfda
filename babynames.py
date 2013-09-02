__author__ = 'coleman'
import pandas as pd
from pandas import DataFrame, Series
# from matplotlib import plot
import json
import numpy as np

from settings import PROJECT_ROOT

years = range(1880, 2011)
pieces = []
columns = ['name', 'sex', 'births']

for year in years:
    path = PROJECT_ROOT + '/ch02/names/yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year  # add a column
    pieces.append(frame)

names = pd.concat(pieces, ignore_index=True)


pass




