import os
from random import randrange
import pandas as pd


used_idexes = []

ds = pd.read_csv('./preprocessed_labels1.csv')

for i in range(1200):
    index = randrange(5982)
    if index not in used_idexes:
        used_idexes.append(index)

# print(len(used_idexes))
test_ds = ds[ds.index.isin(used_idexes)]
train_ds = ds[~ds.index.isin(used_idexes)]

# some stats
print(len(train_ds))
print(len(test_ds))
print(len(ds))

# save files
train_ds.to_csv("train.csv", index=False, encoding='utf8')
test_ds.to_csv('test.csv', index=False, encoding='utf8')
