import random
import numpy as np
import pandas as pd
from hamming_practice import hamming

df = pd.read_csv('sample.csv', names=['word','bin'])

count = 0
h_min = 32

for i in range(0,100):
	for j in range(i+1,100):
		hd = hamming(df.iloc[i,1],df.iloc[j,1])
		print(count,"(",df.iloc[i,0],df.iloc[j,0],")hamming_distance: ",hd)
		count = count+1
		if h_min > hd:
			h_min = hd

print("min hamming distance", h_min)

		




