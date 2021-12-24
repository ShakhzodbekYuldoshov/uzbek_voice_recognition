import string
import pandas as pd


def clean_dataset(path_to_csv, exclude):
    ds = pd.read_csv(path_to_csv)
    for i, transcript in enumerate(ds['transcript']):
        ds['transcript'][i] = ''.join(ch for ch in ds['transcript'][i] if ch not in exclude).lower()
    return ds


exclude = set(string.punctuation)
print(string.punctuation)

# preprocess files
ds_test = clean_dataset('./test1.csv', exclude)
ds_train = clean_dataset('./train1.csv', exclude)
ds_dev = clean_dataset('./dev1.csv', exclude)

# save files
ds_test.to_csv("test.csv", index=False, encoding='utf8')
ds_train.to_csv("train.csv", index=False, encoding='utf8')
ds_dev.to_csv("dev.csv", index=False, encoding='utf8')
