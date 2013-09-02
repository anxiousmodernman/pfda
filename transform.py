import pandas as pd
from pandas import DataFrame, Series
# from matplotlib import plot
import json
import numpy as np

from settings import PROJECT_ROOT


path = PROJECT_ROOT + '/ch02/usagov_bitly_data2012-03-16-1331923249.txt'

records = [json.loads(line) for line in open(path)]  # records can be accessed by index records[0]

# NOTE not a standard pandas way
# time_zones = [rec['tz'] for rec in records if 'tz' in rec]  # if statement required or else key error
# print time_zones[:10]  # just a list of timezones, still have to filter empty string

frame = DataFrame(records)

# print frame['tz'][:10]  # nice

# frame cleaning pattern; column reference returns a Series object with fillna() method
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'

tz_counts = clean_tz.value_counts()  # Series also has value_counts()

print '\nprinting time zone counts after cleaning'
print tz_counts[:10]

# user agent is column 'a'
results = Series([x.split()[0] for x in frame.a.dropna()])  # create Series after breaking off first token (sep=" ")

print '\nprinting counts of first token of user agent strings'
print results.value_counts()[:8]


cframe = frame[frame.a.notnull()]  # remove rows where 'a' column is
operating_system = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')


print '\nprinting operating_system first 8'
print operating_system[:8]

by_tz_os = cframe.groupby(['tz', operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)

print '\nagg_counts'
print agg_counts[:5]


indexer = agg_counts.sum(1).argsort()  # sort in ascending order
count_subset = agg_counts.take(indexer)[-10:]  # use take() to in indexer order, slice off last 10 rows
normed_subset = count_subset.div(count_subset.sum(1), axis=0) # rows normalized to sum to 1




pass























