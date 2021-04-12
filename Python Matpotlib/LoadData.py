import pandas as pd
from pandas import ExcelFile

df = pd.read_excel('data.xlsx', sheetname = 'Sheet1')

X = list(df['X'])
Y = list(df['Y'])

#  Load data from a text file 

X = []
Y = []

with open('values.txt','r') as  myfile:
	for line in myfile:
		y.append(int(line))

X = list(range(0,len(Y)+1))
print(X)
print(Y)