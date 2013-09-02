
Farhan's Twitter Project requirements
-------------------------------------
https://github.com/Nearhan/facuet/blob/master/requirements.txt


Pivoting data and applying a filter
-----------------------------------
_Example from moviedata.py_

First, pivot your data

```python
mean_ratings = data.pivot_table('rating', rows='title',
                                cols='gender', aggfunc='mean')
```
Next, you can create a Series object from the data, grouped by title.
This yields a series of *counts*

```python
ratings_by_title = data.groupby('title').size()
```
Use the Series object (*ratings_by_title*) to create an *index*
The index contains only titles with 250 or more ratings.

```python
active_titles = ratings_by_title.index[ratings_by_title >= 250]  # creates an index
```

Use the index object to select rows from a DataFrame

```python
mean_ratings = mean_ratings.ix[active_titles]  # reduce the data set to popular records
```

Sort DataFrame objects by column name, ascending

```python
top_female_ratings = mean_ratings.sort_index(by='F', ascending=False)
```

Adding a column to the DataFrame is easy, because you can just assign to a new key/column

```python
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
```


Stacking data frames
---------------------
First make a list of DataFrame objects in a for loop, then 