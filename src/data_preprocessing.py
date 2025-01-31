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

def get_parameter(dataset, column_name, alpha=None):
    list_metallicities = ["0.0002", "0.0004", "0.0008", "0.0012", "0.0016", "0.002", "0.004", "0.006", "0.008", "0.012", "0.016", "0.02"]
    if alpha is not None:
        return [dataset[str(alpha)][metallicity][column_name] for metallicity in list_metallicities]
    else:
        # TODO: think about keeping this or not
        list_alpha = ["A0.5", "A1", "A3", "A5"]
        for alpha in list_alpha:
            pass