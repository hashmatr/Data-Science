import pandas as pd
data = {
     "name":['Ali','Fari','Sahi','Rani'],
     "age":[23,43,23,43],
     "salary":[324,545,342,453],
     "id":['1','2','3','4'],
     "class":['1','2','3','5']
 }
df = pd.DataFrame(data) 
# print('Original data')
# print(df)
# print('data description')
# print(df.describe())
print('shape:', df.shape)
print('column names :',df.columns)
print('Rows names :',df.pow)