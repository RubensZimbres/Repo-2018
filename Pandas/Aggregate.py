df.set_index('Data', inplace=True)

df2=df.groupby([df.Serial,df.index.year,df.index.month,df.index.day]).sum()

df3=df2.reset_index(level=['Serial'])

df3.index.names=['Year','Month','Day']

df4=df3.reset_index()

df4['Date'] = pd.to_datetime(df4[['Year','Month','Day']])
