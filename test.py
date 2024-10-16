import matplotlib.pyplot
import pandas as pd
import json

with open('C:\Coding\DataVisualization_report\people_database.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
database = pd.DataFrame(data)

