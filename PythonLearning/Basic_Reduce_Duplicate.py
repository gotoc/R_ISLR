from lxml import objectify
import pandas as pd

TST=objectify.parse(open("Testing.xml"))
root=TST.getroot()
df=pd.DataFrame(columns=('Number','String','Boolean'))
for i in range (0,4):
    obj=root.getchildren()[i].getchildren()
    row=dict(zip(['Number','String','Boolean'],[obj[0].text,obj[1].text,obj[2].text]))
    row_s=pd.Series(row)
    row_s.name=i
    df=df.append(row_s)
    
search=pd.DataFrame.duplicated(df)

print df.drop_duplicates()




