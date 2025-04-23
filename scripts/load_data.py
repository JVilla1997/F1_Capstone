import pandas as pd
import os

def load_kaggle_data(data_dir = 'data'):
    files = {
        'constructors': 'constructors.csv',
        'results': 'constructor_results.csv',
        'qualifying': 'qualifying.csv',
        'lap_times': 'lap_times.csv',
        'pit_stops': 'pit_stops.csv'
    }
    data = {}
    for key, file in files.items():
        file_path = os.path.join(data_dir, file)
        if os.path.exists(file_path):
            data[key] = pd.read_csv(file_path)
        else:
            print(f"Warning: {file_path} not found")
    return data

def load_f1db_data(data_dir = 'f1db_data'):
    files = {
        'constructors': 'constructors.csv',
        'standings': 'constructor_standings.csv',
        'lap_times': 'lap_times.csv'
    }
    data = {}
    for key, file in files.items():
        file_path = os.path.join(data_dir, file)
        if os.path.exists(file_path):
            data[key] = pd.read_csv(file_path)
        else:
            print(f"Warning: {file_path} not found")
    return data
