'''
This script downloads the dataset from Kaggle using the kagglehub library.
It then copies the downloaded file to the current working directory.
'''

import kagglehub
import os
import shutil

FILENAME="cost_of_international_education.csv"

path = kagglehub.dataset_download("adilshamim8/cost-of-international-education")
print("path: ", path)

# copy file

file_path = os.path.join(path, os.listdir(path)[0])
print("file_path: ", file_path)

if os.path.isfile(file_path):
    print("File exists, copying to current directory")
    destination_dir = os.path.join(os.path.dirname(__file__),FILENAME)
    shutil.copy(file_path, destination_dir)
    print(f"Copied: {file_path} → {destination_dir}")


