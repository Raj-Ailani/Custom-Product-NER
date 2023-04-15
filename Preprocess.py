import pandas as pd

df = pd.read_csv('dataset.csv')


converted_array = []

for index, row in df.iterrows():
    
    text = row['text']
    points = row['entity']
    splited_points = points.split(',')
    entity = (int(splited_points[0]),int(splited_points[1]),"PRODUCT")
    data = (text , {"entities":[entity]})
    converted_array.append(data)

