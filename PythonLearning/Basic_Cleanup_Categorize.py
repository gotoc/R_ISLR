import pandas as pd
car_colors=pd.Series(['Blue','Red','Green'], dtype='category')
car_data=pd.Series(pd.Categorical(['Yellow','Green', 'Red', 'Blue', 'Purple'], categories=car_colors,ordered=False))
find_entries=pd.isnull(car_data)

print car_colors
print 
print car_data
print
print find_entries[find_entries==True]

