import csv
import pandas as pd
import numpy as np
csvFile=pd.read_csv("jcn.csv",skiprows=[0,2,3,4])
s1=csvFile.max(axis=0)
d1=s1.reset_index()
#print(type(d1))
d1 = d1.rename(columns={0:'MAX','index':'instance'})
d1 = d1.iloc[1:]
#print(d1)

s2=csvFile.min(axis=0)
d2=s2.reset_index()
#print(type(d1))
d2 = d2.rename(columns={0:'MIN','index':'instance'})
d2 = d2.iloc[1:]
#print(d2)

d1=d1.merge(d2)

s3=csvFile.mean(axis=0);
d3=s3.reset_index()
#print(type(d1))
d3 = d3.rename(columns={0:'AVG','index':'instance'})

#print(d3)

d1 = d1.merge(d3)
print(d1)

d1.to_csv('test.csv',index = False)