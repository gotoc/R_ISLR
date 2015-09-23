with open ("Colors.txt",'rb') as open_file:                         #rb is access mode: read binary; open function accepts filename an access mode
        print 'Colors.text content:\n'+open_file.read()
    
with open ("Colors.txt",'rb') as open_file:         #use "observation" as control 
    for observation in open_file:
        print 'Reading Data'+observation        
    
n=2
with open ("Colors.txt",'rb') as open_file:         #use "observation" as control 
    for j, observation in enumerate(open_file):             #use enumerate to retrieve row number
        if j%n==0:      #Determine if the row number is even nuber
            print ('Reading line:'+str(j)+'content:'+observation)   

import pandas as pd
color_table=pd.io.parsers.read_table("Colors.txt")          #Use pandas to retrieve the data
print color_table    
Test_data=pd.io.parsers.read_csv("Testing.csv")
print Test_data['Adj Close']                               #Use pandas to read csv
xls=pd.ExcelFile("Testing.xlsx")
Test_data2=xls.parse('Sheet1', index_col=None, na_values=['NA'])           #Use Pandas to read Excel xlsx file 
print Test_data2




