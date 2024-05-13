import pandas as pd
path=input("Please enter the path/filename.extension")
#C:/Users/chait/OneDrive/Desktop/Python Learning/Sample Data for PowerBI Assignment 2024.xlsx
df = pd.read_excel(path, sheet_name="Raw Data",header=3)
df_split = df['Service Provider #1, Service Provider #2, Service Provider #3, Service Provider #4'].str.split(', ', expand=True).iloc[:, :4]
split_column_names = ['Service Provider #1', 'Service Provider #2', 'Service Provider #3', 'Service Provider #4']
df_split.columns = split_column_names
df_split.reset_index(drop=True, inplace=True)

df = pd.concat([df, df_split], axis=1)
df.drop(['Service Provider #1, Service Provider #2, Service Provider #3, Service Provider #4'], axis=1, inplace=True)

def combine_similar_column(name, df):
    columns_starts_with = [str(col) for col in df.columns if str(col).startswith(name)]
    combined_column = df[columns_starts_with].apply(lambda x: ', '.join(x.dropna().astype(str)), axis=1)
    df = pd.concat([df, combined_column.rename("New_"+name)], axis=1)
    df.drop(columns_starts_with, axis=1, inplace=True)
    return df

df = combine_similar_column('Service Provider #1', df)
df = combine_similar_column('Service Provider #2', df)
df = combine_similar_column('Service Provider #3', df)
df = combine_similar_column('Service Provider #4', df)
df.drop(columns=['Strongly Agree'], inplace=True)

#j=0
#for i in df['New_Service Provider #1']:
 #   commas_in_row = i.count(',')
 #   j += commas_in_row        
#print(j)
df['New_Service Provider #1']=df['New_Service Provider #1'].str.split(',')
df['New_Service Provider #2']=df['New_Service Provider #2'].str.split(',')
df['New_Service Provider #3']=df['New_Service Provider #3'].str.split(',')
df['New_Service Provider #4']=df['New_Service Provider #4'].str.split(',')
df = df.explode('New_Service Provider #1').explode('New_Service Provider #2').explode('New_Service Provider #3').explode('New_Service Provider #4')
df.reset_index(drop=True, inplace=True)
print(df)