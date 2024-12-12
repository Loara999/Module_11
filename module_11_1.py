import requests
from pprint import pprint
import numpy as np
import pandas as pd
import openpyxl

#1 - requests
r = requests.get('https://api.github.com')
r_json = r.json()
pprint(r_json)
img = requests.get('https://sun9-61.userapi.com/impg/12i35FDHolTZF1sp71Ho372tQmvH75GD0vT6zg/fZS5J227rY8.jpg?size=1280x1280&quality=95&sign=2a62113c683c5fa1974067e2c61f015b&type=album')
with open('image.jpg', 'wb') as file:
    file.write(img.content)

#2 - numpy
a = np.arange(5, 100, 5)
b = np.eye(5)
print(a)
print(np.sum(a))
print (np.sqrt(a))
a = np.random.randint(1, 10, 10)
print(a)
print(np.sort(a))

#3 - pandas
keys = [chr(65 + n) for n in range(10)]
values = [np.random.randint(1, 10, 10) for _ in range(10)]
Matrix = {k: v for k, v in zip(keys,values)}
Matrix = pd.DataFrame(Matrix, index=keys)
Matrix.to_excel('file_1.xlsx')
Matrix_analysis = Matrix.agg(['sum', 'min','max', 'mean'])
Matrix = pd.read_excel('./file_1.xlsx', index_col=0)
print(Matrix)
print()
print(Matrix_analysis)
