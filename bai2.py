import pandas as pd
import csv
import random

file = pd.read_csv('C:\\Users\\used\\Downloads\\kem11')
print(file.head(10))
print("-"*50)
#Chọn ngẫu nhiên 7 sv trong ds
files = file.sample(n=7)
#Lưu vào file csv mới tên DSSVmoi.csv
files.to_csv(r'C:\\Users\\used\\Downloads\\DSSVmoi.csv', index = None, header=True)
print(files)