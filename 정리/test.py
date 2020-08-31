import csv
import pandas as pd

arr = []

with open('./1.6만_워크맨+에버랜드_UQYCWLrCUy4.csv', 'r',encoding = "utf-8") as f:
    reader = csv.reader(f)
    # next(reader) Header 스킵
    for v in reader:
        arr.append(v)

print(len(arr))



# data = pd.read_csv('./black_pink.csv')
# print(data)
# print(data.shape)