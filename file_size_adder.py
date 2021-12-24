# import dependencies
import os
from pathlib import Path
import pandas as pd


dataset = pd.read_csv('./datalist.csv')
# take only those where is correct is equal to True
# type of is_correcti is bool
# print(type(dataset['is_correct'][0]))
dataset = dataset.loc[dataset['is_correct'] == True]

dataset = dataset.drop(['#', 'is_correct'], axis=1)
dataset.rename(columns={'text': 'transcript', 'voice_id': 'wav_filename'}, inplace=True)

# create array with file sizes
# file_sizes = [Path('./voices\\' + filename + '.ogg').stat().st_size for filename in dataset['wav_filename']]
file_sizes = []
for filename in dataset['wav_filename']:
    try:
        file_sizes.append(Path('./voices\\' + filename + '.ogg').stat().st_size)
    except:
        print(filename + '.ogg  not found and  deleted!')

        dataset = dataset.loc[dataset['wav_filename'] != filename]

# some stats
print(len(file_sizes), ' out of ', len(dataset['wav_filename']))
print(len(dataset['wav_filename']))
dataset['wav_filesize'] = file_sizes

# add .wav at the end of every value of dataset['wav_filename'] column of dataframe
dataset['wav_filename'] = dataset['wav_filename'].astype(str) + '.wav'

# save results
dataset.to_csv("preprocessed_labels1.csv", index=False, encoding='utf8')
