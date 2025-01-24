import pandas as pd
import os

def load_data(folder):
    dict_dataset = {}
    for filename1 in os.listdir(folder):
        folder_path = os.path.join(folder, filename1)
        list_dataset = {}

        for filename2 in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename2)
            df = pd.read_csv(file_path, delimiter=" ", skiprows=2)
            list_dataset[filename2.split("_")[2].split(".txt")[0]] = df
        
        dict_dataset[filename1] = list_dataset
    
    return dict_dataset