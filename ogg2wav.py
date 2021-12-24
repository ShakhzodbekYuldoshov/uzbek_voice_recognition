import os
from pydub import AudioSegment
import shutil


file_names = os.listdir('./voices')
# file_name = 'AwACAgEAAxkBAAEB5jJgOcyXUveraJ6l1UBp_xyvoh4FtgACLQEAAhRt0UVSZEIwIVrI3B4E.ogg'

# file_path = './voices/' + file_name
# dst_path = './wav_voices/' + file_name[:-4] + '.wav'
# print(file_path)
# print(dst_path)
# print(os.path.isfile(file_path))
# sound = AudioSegment.from_ogg(file_path)
# sound.export(dst_path, format="wav")

for file_name in file_names:
    file_path = './voices/' + file_name
    dst_path = './wav_voices/' + file_name[:-4] + '.wav'
    # print(file_path)
    # print(dst_path)
    # print(os.path.isfile(file_path))
    # sound = AudioSegment.from_ogg(file_path)
    # sound.export(dst_path, format="wav")
    shutil.copyfile(file_path, dst_path)
